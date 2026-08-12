# Felsökning, Risktabell & Fallgropar

## Felsökning 400-fel

| Fel | Lösning |
|-------|-----|
| `missing_required_parameter: tools[0].name` | Verktygsdefinition använder gammalt inbäddat format för Chat Completions | Omstrukturera från `{"type": "function", "function": {"name": ...}}` till `{"type": "function", "name": ..., "parameters": ...}` — namn, beskrivning, parametrar ska ligga på toppnivå |
| `unknown_parameter: input[N].tool_calls` | Flera steg med verktygsresultat använder gammalt format för Chat Completions | Ersätt `{"role": "assistant", "tool_calls": [...]}` + `{"role": "tool", ...}` med `response.output`-poster + `{"type": "function_call_output", "call_id": ..., "output": ...}` |
| `invalid_function_parameters: 'required' is required` | `strict: true`-verktyg saknar `required`-array | När `strict: true`, måste alla egenskaper anges i `required` och `additionalProperties: false` måste sättas |
| `invalid_function_parameters: 'additionalProperties' is required` | `strict: true`-verktyg saknar `additionalProperties: false` | Lägg till `"additionalProperties": false` i parameters-objektet |
| `invalid input[N].id: Expected an ID that begins with 'fc'` | Few-shot function_call ID har fel prefix | Funktionsanrops-ID måste börja med `fc_` (t.ex. `fc_example1`), inte `call_` |
| `missing_required_parameter: text.format.name` | Lägg till nyckeln `"name"` i format-dikt (t.ex. `"name": "Output"`) |
| `invalid_type: text.format` | Säkerställ att `text.format` är ett dikt med nycklarna `type`, `name`, `strict`, `schema` — inte en sträng |
| `invalid input content type` | Använd innehållstyperna `input_text`/`output_text` istället för Chat `text` |
| `invalid input content type` (bild) | Bildinnehåll använder fortfarande `"type": "image_url"` | Byt till `"type": "input_image"` |
| `Expected object, got string` på `image_url` | `image_url` är fortfarande ett inbäddat objekt `{"url": "..."}` | Omstrukturera till en vanlig sträng: `"image_url": "https://..."` eller `"image_url": "data:image/...;base64,..."` |
| `integer below minimum value` för `max_output_tokens` | Minsta värdet är **16** på Azure OpenAI. Använd 50+ för tester, 1000+ för produktion. |
| `429 Too Many Requests` under strömning | Begränsad av takten. Omge strömning med `try/except`, returnera fel-JSON till frontend, implementera backoff/omförsök. |
| `KeyError: 'innererror'` vid fel i innehållsfilter | Felstruktur för innehållsfilter ändrad i Responses API | Chat Completions använde `error.body["innererror"]["content_filter_result"]`; Responses API använder `error.body["content_filters"][0]["content_filter_results"]` (plural, i en array). Omskriv alla `innererror`-åtkomster. |

---

## Riskskala för migration

| Symptom | Trolig misstag | Lösning |
|---------|---------------|-----|
| Tom `output_text` / avklippt svar | `max_output_tokens` för lågt för resonemangsmodeller | Sätt `max_output_tokens=1000` eller högre — resonemangstokens räknas mot gränsen |
| `400 invalid_type: text.format` | Skickat `response_format`-sträng istället för `text.format`-dikt | Använd `text={"format": {"type": "json_schema", "name": "...", "strict": True, "schema": {...}}}` |
| `404 Not Found` på `/openai/v1/responses` | Fel `base_url` — saknar `/openai/v1/`-suffix | Säkerställ `base_url=f"{endpoint}/openai/v1/"` (med snedstreck i slutet) |
| `401 Unauthorized` efter byte till `OpenAI()` | `api_key` inte satt eller tokenleverantör skickad fel | För EntraID: `api_key=token_provider` (det anropbara). För API-nyckel: `api_key=os.environ["AZURE_OPENAI_API_KEY"]` |
| Modell returnerar `deployment not found` | `model`-param matchar inte din Azure-distribution | Använd `model=os.environ["AZURE_OPENAI_DEPLOYMENT"]` — detta är distributionsnamnet, inte modellnamnet |
| `json.loads(resp.output_text)` kastar `JSONDecodeError` | Schema inte tvingat eller modellen stödjer inte strikt JSON | Säkerställ `"strict": True` i schemat, och verifiera att modellen stödjer strukturerad output |
| Strömning ger inga `delta`-händelser | Kontrollerar fel händelsetyp | Filtrera på `event.type == "response.output_text.delta"`, inte Chat:s `chat.completion.chunk` |
| `400` fel på bildinmatning efter migration | Bildinnehållstyp uppdaterad ej | Ändra `"type": "image_url"` → `"type": "input_image"` och omstrukturera `"image_url": {"url": "..."}` → `"image_url": "..."` (vanlig sträng) |
| Verktygsanrop loopar oändligt | Saknat verktygsresultat i efterföljande `input` | Efter att ha använt ett verktyg, lägg till en `{"type": "function_call_output", "call_id": ..., "output": ...}`-post i `input` i nästa förfrågan |
| `temperature`-fel med GPT-5 eller o-serien | Tydligt `temperature`-värde annat än 1 | Ta bort `temperature` eller sätt till `1` för GPT-5 och o-seriens modeller (o1, o3-mini, o3, o4-mini) |
| `top_p`-fel med o-serien | `top_p` stödjs ej | Ta bort `top_p` när du riktar mot o-serien |
| `max_completion_tokens` ej igenkänt | Använder Azure-specifik parameter | Ersätt `max_completion_tokens` med `max_output_tokens`. Sätt till 4096+ för o-serien (resonemangstokens räknas mot gränsen). |
| Tomt/avklippt utdata från o-serien | `max_output_tokens` för lågt | O-serien använder resonemangstokens internt. Sätt `max_output_tokens=4096` eller högre — inte 500–1000. |
| `400 integer_below_min_value` för `max_output_tokens` | Värde under 16 | Azure OpenAI kräver `max_output_tokens >= 16`. Använd 50+ för enkla tester, 1000+ för produktion. |
| `429 Too Many Requests` mitt i strömmen | Begränsad av Azure OpenAI | Strömmen bryts tyst utan felhantering. Omslut alltid `async for event in await coroutine:` i `try/except` och returnera `{"error": str(e)}` till frontend. |
| `AzureDeveloperCliCredential` → `CredentialUnavailableError` | Fel tenant eller inte inloggad | Skicka `tenant_id=os.getenv("AZURE_TENANT_ID")` explicit. Kör `azd auth login --tenant <tenant-id>` lokalt. |
| `404 Not Found` med GitHub Models (`models.github.ai`) | GitHub Models stödjer ej Responses API | Ta bort GitHub Models-kodvägen helt. Använd Azure OpenAI, OpenAI eller en kompatibel lokal endpoint (t.ex. Ollama med Responses-stöd). |
| MAF `OpenAIChatCompletionClient` använder fortfarande Chat Completions | Använder legacy MAF-klient i 1.0.0+ | I MAF 1.0.0+ använder `OpenAIChatClient` Responses API som standard. Byt `OpenAIChatCompletionClient` till `OpenAIChatClient`. För pre-1.0.0, uppgradera till `agent-framework-openai>=1.0.0`. |
| LangChain-agenter returnerar tomt eller misslyckas med verktygsanrop | `ChatOpenAI` använder inte Responses API | Lägg till `use_responses_api=True` i `ChatOpenAI(...)`. Ändra även `.content` → `.text` på svarmeddelanden. |
| `KeyError: 'innererror'` i felhantering för innehållsfilter | Felkroppsstruktur ändrad i Responses API | Omskriv `error.body["innererror"]["content_filter_result"]["jailbreak"]` → `error.body["content_filters"][0]["content_filter_results"]["jailbreak"]`. `innererror` wrappern är borttagen; innehållsfilterdetaljer finns nu i en top-nivå `content_filters`-array med `content_filter_results` (plural) inuti varje post. |
| Rå HTTP-anrop till `/openai/deployments/.../chat/completions` ger 404 | Gammal Chat Completions REST-endpoint | Omskriv URL till `/openai/v1/responses`. Ändra förfrågningskropp: `messages` → `input`, lägg till `max_output_tokens` + `store: false`, ta bort `api-version`-queryparam. Ändra svarstolkning: `choices[0].message.content` → `output[0].content[0].text` (notera: `output_text` är en SDK-bekvämlighets-egenskap, ej i den råa REST JSON). |

---

## Fallgropar

1. Om du tidigare använt Chat Completions för konversationsstatus, hantera ditt eget tillstånd explicit med Responses.
2. Föredra `max_output_tokens` framför äldre `max_tokens`.
3. Vid migrering till `gpt-5`, säkerställ att `temperature` inte anges eller sätts till `1`.
4. Ersätt Chat `content[].type: "text"` med Responses `content[].type: "input_text"` för användar-/systeminmatningar.
5. För `text.format`, ange ett korrekt dikt (t.ex. `{"type": "json_schema", "name": "Output", "schema": ..., "strict": True}`), inte en vanlig sträng.
6. Parametern `seed` stöds ej i Responses; ta bort den från förfrågningarna.
7. **Resonemang**: Inkludera endast `reasoning` om originalkoden redan använde det. Lägg inte till `reasoning` i API-anrop som inte hade det — många icke-resonemangsmodeller stödjer inte denna parameter.
8. **Storlek på `max_output_tokens`**: För resonemangsmodeller (GPT-5-mini, GPT-5, o-serien), använd `max_output_tokens=4096` eller högre — inte 50–1000. Modellen använder resonemangstokens internt innan synligt utdata genereras; för låga gränser orsakar avklippta eller tomma svar.
9. **O-serien `max_completion_tokens`**: Om originalkoden använde `max_completion_tokens` (Azure-specifikt för o-serien), ersätt med `max_output_tokens`. Responses API accepterar inte `max_completion_tokens`.
10. **O-serien `reasoning_effort`**: Om originalkoden använder `reasoning_effort` (low/medium/high), migrera det till `reasoning={"effort": "<value>"}` i Responses API-anropet.
11. **O-seriens strömningsfördröjning**: O-seriens modeller gör internt resonemang innan utdata genereras. Vid strömning förvänta längre fördröjning innan första `response.output_text.delta`-händelsen. Detta är normalt — modellen resonerar, den är inte fast.
9. **`_azure_ad_token_provider` är borttagen**: `AsyncOpenAI` / `OpenAI` har ingen `_azure_ad_token_provider`-attribut. Tester eller kod som använder detta attribut kommer att misslyckas med `AttributeError`. Token-leverantören skickas som `api_key` och är inte åtkomlig på klientobjektet.
10. **Snapshot / guldfiler**: Om testsuiten använder snapshot-testning måste **alla** snapshot-filer som innehåller Chat Completions strömningsformat (`choices[0]`, `content_filter_results`, `function_call`, etc.) uppdateras till nya Responses-formatet. Detta är lätt att missa och orsakar fel i snapshot-assertioner.
11. **Mock monkeypatch-sökväg**: Monkeypatch-målet ändras från `openai.resources.chat.AsyncCompletions.create` → `openai.resources.responses.AsyncResponses.create` (eller `Responses.create` för synkront). Användning av gammal sökväg gör ingenting tyst — mocken fångar inte upp och tester använder den riktiga API:n eller misslyckas.
12. **`input` inte `messages`**: Mock-funktioner måste läsa `kwargs.get("input")` och inte `kwargs.get("messages")`. Responses API använder `input` för konversationshistorik.
13. **Miljövariabelnamn**: Azure Identity SDK använder `AZURE_CLIENT_ID` (inte `AZURE_OPENAI_CLIENT_ID`) för `ManagedIdentityCredential(client_id=...)`. Byt namn i tester, `.env`-filer, app-inställningar och Bicep/infra.
14. **`max_output_tokens` minimum är 16**: Azure OpenAI avvisar värden under 16 med `400 integer_below_min_value`. Använd `50` för snabba tester, `1000`+ för produktion. Det gamla `max_tokens` hade inget sådant minimum.
15. **`tenant_id` för `AzureDeveloperCliCredential`**: När Azure OpenAI-resursen finns i annan tenant måste du **skicka `tenant_id` explicit** — `AzureDeveloperCliCredential(tenant_id=os.getenv("AZURE_TENANT_ID"))`. Utan detta används fel tenant tyst och ger `401`.
16. **Takthantering uppstår annorlunda vid strömning**: Med Chat Completions stoppades strömmen oftast vid 429-fel innan starten. Med Responses API kan en 429 inträffa **mitt i strömmen** — den asynkrona iteratorn kastar undantag. Omslut alltid strömningsloopen i `try/except` och returnera en fel-JSON-rad så frontend kan hantera det snyggt.

17. **Felsökning vid streaming är obligatoriskt för webbappar**: Mönstret `try: async for event in await coroutine: ... except Exception as e: yield json.dumps({"error": str(e)})` är avgörande. Utan det dör SSE/JSONL-strömmen tyst vid vilket serverfel som helst och frontend hänger sig.
18. **Verktygsdefinitioner måste använda platt format**: Responses API förväntar sig `{"type": "function", "name": ..., "parameters": ...}` — inte Chat Completions inbäddade `{"type": "function", "function": {"name": ..., "parameters": ...}}`. Detta är det vanligaste migrationsfelet för funktion-anropande kod.
19. **`pydantic_function_tool()` är inkompatibel**: Hjälpen `openai.pydantic_function_tool()` genererar fortfarande det gamla inbäddade formatet. Använd det inte med `responses.create()`. Definiera verktygsscheman manuellt eller platta ut utdata.
20. **Verktygsresultat använder `function_call_output`, inte `role: tool`**: Efter att ett verktyg körts, lägg till `{"type": "function_call_output", "call_id": ..., "output": ...}` — inte `{"role": "tool", "tool_call_id": ..., "content": ...}`. För assistentens verktygsförfrågan, använd `messages.extend(response.output)` — inte en manuell dict `{"role": "assistant", "tool_calls": [...]}`.
21. **`strict: true` kräver `required` + `additionalProperties: false`**: När `strict: true` används på ett verktyg måste varje egenskap listas i arrayen `required` och `additionalProperties` måste vara `false`. Saknas något av dessa uppstår en 400-felkod.
22. **Funktionsanrops-ID har specifika prefix**: Vid few-shot `function_call`-objekt i `input` måste fältet `id` börja med `fc_` och fältet `call_id` börja med `call_` (t.ex. `"id": "fc_example1", "call_id": "call_example1"`). Det gamla Chat Completions-prefixet `call_` för `id` avvisas.
23. **GitHub Models stöder inte Responses API**: Om appen har en GitHub Models-kodväg (`base_url` som pekar på `models.github.ai` eller `models.inference.ai.azure.com`), ta bort den helt. Det finns ingen migrationsväg — växla till Azure OpenAI, OpenAI eller en kompatibel lokal endpoint.
24. **Felstruktur för innehållsfilter ändrad**: Chat Completions-fel använde `error.body["innererror"]["content_filter_result"]` (singular). Responses API-fel använder `error.body["content_filters"][0]["content_filter_results"]` (plural, i en array). Nyckeln `innererror` finns inte längre. Kod som direkt går åt `innererror` kastar `KeyError` vid körning — detta är lätt att missa vid migrering eftersom det bara blir synligt när innehållsfiltret faktiskt utlöses. Sök alltid efter `innererror` vid migrering.
25. **Direkta HTTP-anrop behöver omskrivning av URL + kropp**: Appar som anropar Azure OpenAI REST direkt (via `requests`, `httpx`, `aiohttp`) med `/openai/deployments/{name}/chat/completions?api-version=...` måste byta till `/openai/v1/responses`. Begärans kropp använder `input` istället för `messages`, kräver `max_output_tokens` och `store`, och query-parametern `api-version` tas bort. Svars-kroppens text finns i `output[0].content[0].text` — **inte** `output_text`, som är en SDK-bekvämlighets-egenskap som saknas i råa REST JSON.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfriskrivning**:
Detta dokument har översatts med hjälp av AI-översättningstjänsten [Co-op Translator](https://github.com/Azure/co-op-translator). Även om vi strävar efter noggrannhet, var vänlig notera att automatiska översättningar kan innehålla fel eller brister. Det ursprungliga dokumentet på dess modersmål bör betraktas som den auktoritativa källan. För kritisk information rekommenderas professionell mänsklig översättning. Vi ansvarar inte för några missförstånd eller feltolkningar som uppstår till följd av användningen av denna översättning.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->