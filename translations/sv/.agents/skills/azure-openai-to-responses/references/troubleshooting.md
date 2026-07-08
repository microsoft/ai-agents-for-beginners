# Felsökning, Risklista & Fallgropar

## Felsökning 400-fel

| Fel | Åtgärd |
|-------|-----|
| `missing_required_parameter: tools[0].name` | Verktygsdefinitionen använder gammalt inbäddat Chat Completions-format | Platta ut från `{"type": "function", "function": {"name": ...}}` till `{"type": "function", "name": ..., "parameters": ...}` — namn, beskrivning, parametrar ska ligga på toppnivå |
| `unknown_parameter: input[N].tool_calls` | Verktyg resultat från flera omgångar använder gammalt Chat Completions-format | Ersätt `{"role": "assistant", "tool_calls": [...]}` + `{"role": "tool", ...}` med `response.output`-objekt + `{"type": "function_call_output", "call_id": ..., "output": ...}` |
| `invalid_function_parameters: 'required' is required` | `strict: true`-verktyg saknar `required`-fält | När `strict: true` måste alla egenskaper listas i `required` och `additionalProperties: false` måste anges |
| `invalid_function_parameters: 'additionalProperties' is required` | `strict: true`-verktyg saknar `additionalProperties: false` | Lägg till `"additionalProperties": false` i parametrar-objektet |
| `invalid input[N].id: Expected an ID that begins with 'fc'` | Few-shot function_call-ID har fel prefix | Funktionsanrops-ID:n måste börja med `fc_` (t.ex. `fc_example1`), inte med `call_` |
| `missing_required_parameter: text.format.name` | Lägg till `"name"`-nyckel i format-dikt (t.ex. `"name": "Output"`) |
| `invalid_type: text.format` | Säkerställ att `text.format` är en dikt med nycklarna `type`, `name`, `strict`, `schema` — inte en sträng |
| `invalid input content type` | Använd `input_text`/`output_text`-innehållstyper istället för Chat `text` |
| `invalid input content type` (bild) | Bildinnehåll använder fortfarande `"type": "image_url"` | Ändra till `"type": "input_image"` |
| `Expected object, got string` på `image_url` | `image_url` är fortfarande ett inbäddat objekt `{"url": "..."}` | Platta ut till en vanlig sträng: `"image_url": "https://..."` eller `"image_url": "data:image/...;base64,..."` |
| `integer below minimum value` för `max_output_tokens` | Minimum är **16** på Azure OpenAI. Använd 50+ för tester, 1000+ för produktion. |
| `429 Too Many Requests` under streaming | Rate limitad. Wrappa streamingen i `try/except`, returnera fel-JSON till frontend, implementera backoff/retry. |
| `KeyError: 'innererror'` vid content filter-fel | Struktur för fel-kropp ändrad i Responses API | Chat Completions använde `error.body["innererror"]["content_filter_result"]`; Responses API använder `error.body["content_filters"][0]["content_filter_results"]` (flertal, i array). Skriv om alla accesser till `innererror`. |

---

## Risklista för migrering

| Symptom | Trolig felaktighet | Åtgärd |
|---------|---------------|-----|
| Tom `output_text` / avkapad respons | `max_output_tokens` för lågt för resonemangsmodeller | Sätt `max_output_tokens=1000` eller högre — resonemangs-token räknas mot gränsen |
| `400 invalid_type: text.format` | Skickat `response_format`-sträng istället för `text.format`-dikt | Använd `text={"format": {"type": "json_schema", "name": "...", "strict": True, "schema": {...}}}` |
| `404 Not Found` på `/openai/v1/responses` | Fel `base_url` — saknar `/openai/v1/`-suffix | Säkerställ `base_url=f"{endpoint}/openai/v1/"` (med avslutande snedstreck) |
| `401 Unauthorized` efter byte till `OpenAI()` | `api_key` ej satt eller token-leverantör skickades felaktigt | För EntraID: `api_key=token_provider` (en callable). För API-nyckel: `api_key=os.environ["AZURE_OPENAI_API_KEY"]` |
| Modell returnerar `deployment not found` | `model`-param matchar inte ditt Azure deployments-namn | Använd `model=os.environ["AZURE_OPENAI_DEPLOYMENT"]` — det är deployment-namnet, inte modellnamnet |
| `json.loads(resp.output_text)` kastar `JSONDecodeError` | Schema inte tvingat eller modell stöder inte strikt JSON | Säkerställ `"strict": True` i schemat, och verifiera att modellen stödjer strukturerad output |
| Streaming ger inga `delta`-händelser | Fel event-typ filtreras på | Filtrera på `event.type == "response.output_text.delta"`, inte Chat's `chat.completion.chunk` |
| `400`-fel på bildinput efter migrering | Bildinnehållstyp inte uppdaterad | Ändra `"type": "image_url"` → `"type": "input_image"` och platta ut `"image_url": {"url": "..."}` → `"image_url": "..."` (vanlig sträng) |
| Verktygsanrop loopar oändligt | Saknas verktygsresultat i efterföljande `input` | Efter verktygets körning, lägg till ett `{"type": "function_call_output", "call_id": ..., "output": ...}` i `input` i nästa anrop |
| `temperature`-fel med GPT-5 eller o-serien | Explicit `temperature` som inte är 1 | Ta bort `temperature` eller sätt till `1` för GPT-5 och o-serien (o1, o3-mini, o3, o4-mini) |
| `top_p`-fel med o-serien | `top_p` ej stöds | Ta bort `top_p` när du riktar mot o-serien modeller |
| `max_completion_tokens` ej igenkänt | Använder Azure-specifik parameter | Ersätt `max_completion_tokens` med `max_output_tokens`. Sätt till 4096+ för o-serien (resonemangs-token räknas mot gränsen). |
| Tom/avkapad output från o-serien | `max_output_tokens` för lågt | O-serien använder resonemangs-token internt. Sätt `max_output_tokens=4096` eller högre — inte 500–1000. |
| `400 integer_below_min_value` för `max_output_tokens` | Värde under 16 | Azure OpenAI kräver `max_output_tokens >= 16`. Använd 50+ för snabbstester, 1000+ för produktion. |
| `429 Too Many Requests` mitt i streamen | Rate limit från Azure OpenAI | Streamen avbryts tyst utan felhantering. Wrappa alltid `async for event in await coroutine:` i `try/except` och yielda `{"error": str(e)}` till frontend. |
| `AzureDeveloperCliCredential` → `CredentialUnavailableError` | Fel tenant eller ej inloggad | Skicka `tenant_id=os.getenv("AZURE_TENANT_ID")` explicit. Kör `azd auth login --tenant <tenant-id>` lokalt. |
| `404 Not Found` med GitHub Models (`models.github.ai`) | GitHub Models stödjer inte Responses API | Ta bort GitHub Models-koden helt. Använd Azure OpenAI, OpenAI, eller kompatibel lokal endpoint (t.ex. Ollama med Responses-stöd). |
| MAF `OpenAIChatCompletionClient` använder fortfarande Chat Completions | Använder legacy MAF-client i 1.0.0+ | Från MAF 1.0.0+ använder `OpenAIChatClient` Responses API som standard. Byt ut `OpenAIChatCompletionClient` mot `OpenAIChatClient`. För versioner före 1.0.0, uppgradera till `agent-framework-openai>=1.0.0`. |
| LangChain-agent ger tomt eller fel vid verktygsanrop | `ChatOpenAI` använder inte Responses API | Lägg till `use_responses_api=True` i `ChatOpenAI(...)`. Ändra också `.content` → `.text` på svarsmeldingar. |
| `KeyError: 'innererror'` i content filter-felhanterare | Felkroppsstruktur ändrad i Responses API | Skriv om `error.body["innererror"]["content_filter_result"]["jailbreak"]` → `error.body["content_filters"][0]["content_filter_results"]["jailbreak"]`. `innererror`-wrappern är borta; content filter-info finns nu i top-nivåns `content_filters`-array med `content_filter_results` (flertal) inuti varje entry. |
| Rå HTTP-anrop till `/openai/deployments/.../chat/completions` ger 404 | Gammalt Chat Completions REST-endpoint | Skriv om URL till `/openai/v1/responses`. Ändra request-body: `messages` → `input`, lägg till `max_output_tokens` + `store: false`, ta bort `api-version` query-param. Ändra response-tolkning: `choices[0].message.content` → `output[0].content[0].text` (observera: `output_text` är en SDK-convenience, finns ej i rå REST JSON). |

---

## Fallgropar

1. Om du tidigare använde Chat Completions för samtalstillstånd, hantera ditt eget tillstånd explicit med Responses.
2. Föredra `max_output_tokens` framför det äldre `max_tokens`.
3. Vid migrering till `gpt-5`, säkerställ att `temperature` inte är angivet eller är satt till `1`.
4. Byt ut Chat `content[].type: "text"` mot Responses `content[].type: "input_text"` för användar-/systeminmatningar.
5. För `text.format`, leverera en korrekt dikt (t.ex. `{"type": "json_schema", "name": "Output", "schema": ..., "strict": True}`), inte en vanlig sträng.
6. `seed`-parametern stöds inte i Responses; ta bort den från anrop.
7. **Resonemang**: Inkludera endast `reasoning` om den ursprungliga koden redan använde den. Lägg inte till `reasoning` i API-anrop som inte hade det — många modeller (t.ex. gpt-4o-mini) stöder inte denna parameter.
8. **`max_output_tokens` storlek**: För resonemangsmodeller (GPT-5-mini, GPT-5, o-serien), använd `max_output_tokens=4096` eller högre — inte 50–1000. Modellen använder resonemangs-token internt innan synligt resultat genereras; för låga gränser ger avklippta eller tomma svar.
9. **O-serien `max_completion_tokens`**: Om ursprunglig kod använde `max_completion_tokens` (Azure-specifikt för o-serien), byt ut mot `max_output_tokens`. Responses API accepterar inte `max_completion_tokens`.
10. **O-serien `reasoning_effort`**: Om ursprunglig kod använde `reasoning_effort` (low/medium/high), migrera till `reasoning={"effort": "<värde>"}` i Responses API-anropet.
11. **O-serien streamingfördröjning**: O-seriemodeller genomför internt resonemang innan output genereras. Vid streaming, räkna med längre fördröjning innan första `response.output_text.delta`-eventet. Detta är normalt — modellen resonerar, inte hänger sig.
9. **`_azure_ad_token_provider` är borta**: `AsyncOpenAI` / `OpenAI` har ingen `_azure_ad_token_provider`-attribut. Tester eller kod som försöker komma åt detta ger `AttributeError`. Token-leverantören skickas som `api_key` och kan inte inspekteras på klientobjektet.
10. **Snapshot / golden filer**: Om testsuiten använder snapshot-testning, **alla** snapshot-filer som innehåller Chat Completions streaming-strukturer (`choices[0]`, `content_filter_results`, `function_call`, etc.) måste uppdateras till nya Responses-formatet. Detta är lätt att missa och orsakar snapshot-fel.
11. **Mock monkeypatch-path**: Monkeypatch-mål ändras från `openai.resources.chat.AsyncCompletions.create` → `openai.resources.responses.AsyncResponses.create` (eller `Responses.create` för sync). Användning av gamla path gör att mocken tyst ignoreras — mocken fångar inte anrop, och tester träffar verkliga API eller misslyckas.
12. **`input` inte `messages`**: Mock-funktioner måste läsa `kwargs.get("input")` inte `kwargs.get("messages")`. Responses API använder `input` för samtalshistorik.
13. **Miljövariabelnamn**: Azure Identity SDK använder `AZURE_CLIENT_ID` (inte `AZURE_OPENAI_CLIENT_ID`) för `ManagedIdentityCredential(client_id=...)`. Byt namn i tester, `.env`-filer, app-inställningar och Bicep/infrastruktur.
14. **`max_output_tokens` minimum är 16**: Azure OpenAI avvisar värden under 16 med `400 integer_below_min_value`. Använd `50` för snabbstester, `1000`+ för produktion. Det gamla `max_tokens` hade inget sådant minimum.
15. **`tenant_id` för `AzureDeveloperCliCredential`**: När Azure OpenAI-resursen finns i annan tenant måste du **explicit** skicka `tenant_id` — `AzureDeveloperCliCredential(tenant_id=os.getenv("AZURE_TENANT_ID"))`. Utan detta används tyst fel tenant och `401` returneras.
16. **Rate limits visas annorlunda vid streaming**: Med Chat Completions förhindrade 429 oftast att streamen startade. Med Responses API-streaming kan 429 inträffa **mitt i streamen** — den asynkrona iteratorn kastar ett undantag. Wrappa alltid streaming-loop i `try/except` och yielda en fel-JSON-rad så frontend kan hantera det smidigt.
17. **Streaming-felhante måste vara obligatoriskt för webbappar**: Mönstret `try: async for event in await coroutine: ... except Exception as e: yield json.dumps({"error": str(e)})` är kritiskt. Utan det dör SSE/JSONL-strömmen tyst vid vilket serverfel som helst och frontend hänger sig.  
18. **Verktygsdefinitioner måste använda platt format**: Responses API förväntar sig `{"type": "function", "name": ..., "parameters": ...}` — inte den nästlade Chat Completions `{"type": "function", "function": {"name": ..., "parameters": ...}}`. Detta är det vanligaste migrationsfelet för funktion-anropskod.  
19. **`pydantic_function_tool()` är inkompatibel**: Hjälparen `openai.pydantic_function_tool()` genererar fortfarande det gamla nästlade formatet. Använd den inte med `responses.create()`. Definiera verktygsscheman manuellt eller platta ut utdata.  
20. **Verktygsresultat använder `function_call_output`, inte `role: tool`**: Efter att ha kört ett verktyg, lägg till `{"type": "function_call_output", "call_id": ..., "output": ...}` — inte `{"role": "tool", "tool_call_id": ..., "content": ...}`. För assistentens verktygsförfrågan, använd `messages.extend(response.output)` — inte en manuell dict `{"role": "assistant", "tool_calls": [...]}`.  
21. **`strict: true` kräver `required` + `additionalProperties: false`**: Vid användning av `strict: true` på ett verktyg måste varje egenskap listas i arrayen `required` och `additionalProperties` måste vara `false`. Att sakna något av dessa orsakar ett 400-fel.  
22. **Funktionsanrops-ID:n har specifika prefix**: Vid användning av få-skott `function_call`-objekt i `input` måste fältet `id` börja med `fc_` och fältet `call_id` med `call_` (t.ex. `"id": "fc_example1", "call_id": "call_example1"`). Att använda det gamla Chat Completions-prefixet `call_` för `id` accepteras inte.  
23. **GitHub Models stöder inte Responses API**: Om appen har en GitHub Models-kodväg (`base_url` som pekar på `models.github.ai` eller `models.inference.ai.azure.com`), ta bort den helt. Det finns ingen migrationsväg — byt till Azure OpenAI, OpenAI eller en kompatibel lokal endpoint.  
24. **Felstruktur för content filter har ändrats**: Chat Completions-fel använde `error.body["innererror"]["content_filter_result"]` (singular). Responses API-fel använder `error.body["content_filters"][0]["content_filter_results"]` (plural, inuti en array). Nyckeln `innererror` finns inte längre. Kod som direkt refererar till `innererror` kastar `KeyError` i runtime — detta är lätt att missa vid migration eftersom det bara syns när content filter faktiskt triggas. Sök alltid efter `innererror` vid migration.  
25. **Råa HTTP-anrop behöver URL + body-omskrivning**: Appar som anropar Azure OpenAI REST direkt (via `requests`, `httpx`, `aiohttp`) med `/openai/deployments/{name}/chat/completions?api-version=...` måste byta till `/openai/v1/responses`. Begäran använder `input` istället för `messages`, kräver `max_output_tokens` och `store`, och frågeparametern `api-version` tas bort. Svarsbodyns text finns i `output[0].content[0].text` — **inte** `output_text`, vilket är en SDK-komfortegenskap som inte finns i rå REST JSON.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfriskrivning**:
Detta dokument har översatts med hjälp av AI-översättningstjänsten [Co-op Translator](https://github.com/Azure/co-op-translator). Även om vi strävar efter noggrannhet, var vänlig notera att automatiska översättningar kan innehålla fel eller brister. Det ursprungliga dokumentet på dess modersmål bör betraktas som den auktoritativa källan. För kritisk information rekommenderas professionell mänsklig översättning. Vi ansvarar inte för några missförstånd eller feltolkningar som uppstår till följd av användningen av denna översättning.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->