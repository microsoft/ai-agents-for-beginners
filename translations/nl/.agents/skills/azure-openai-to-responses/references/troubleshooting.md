# Probleemoplossing, Risicotabel & Valkuilen

## Probleemoplossing 400s

| Fout | Oplossing |
|-------|-----|
| `missing_required_parameter: tools[0].name` | Hulpmiddeldefinitie gebruikt oud genest formaat van Chat Completions | Vlakt af van `{"type": "function", "function": {"name": ...}}` naar `{"type": "function", "name": ..., "parameters": ...}` — naam, beschrijving, parameters gaan op topniveau |
| `unknown_parameter: input[N].tool_calls` | Meerdere rondes hulpprogrammaresultaten gebruiken oud Chat Completions-formaat | Vervang `{"role": "assistant", "tool_calls": [...]}` + `{"role": "tool", ...}` met `response.output` items + `{"type": "function_call_output", "call_id": ..., "output": ...}` |
| `invalid_function_parameters: 'required' is required` | `strict: true` hulpprogramma mist `required` array | Bij `strict: true` moeten alle eigenschappen in `required` staan en moet `additionalProperties: false` ingesteld zijn |
| `invalid_function_parameters: 'additionalProperties' is required` | `strict: true` hulpprogramma mist `additionalProperties: false` | Voeg `"additionalProperties": false` toe aan het parameters-object |
| `invalid input[N].id: Expected an ID that begins with 'fc'` | Few-shot function_call ID heeft verkeerd voorvoegsel | Function call IDs moeten beginnen met `fc_` (bv. `fc_example1`), niet met `call_` |
| `missing_required_parameter: text.format.name` | Voeg `"name"` sleutel toe aan het formaat dict (bv. `"name": "Output"`) |
| `invalid_type: text.format` | Zorg dat `text.format` een dict is met sleutels `type`, `name`, `strict`, `schema` — geen string |
| `invalid input content type` | Gebruik `input_text`/`output_text` contenttypes in plaats van Chat `text` |
| `invalid input content type` (afbeelding) | Afbeeldingsinhoud gebruikt nog `"type": "image_url"` | Verander naar `"type": "input_image"` |
| `Expected object, got string` op `image_url` | `image_url` is nog een genest object `{"url": "..."}` | Vlak af naar platte string: `"image_url": "https://..."` of `"image_url": "data:image/...;base64,..."` |
| `integer below minimum value` voor `max_output_tokens` | Minimum is **16** bij Azure OpenAI. Gebruik 50+ voor tests, 1000+ voor productie. |
| `429 Too Many Requests` tijdens streamen | Rate limit. Wikkel streamen in `try/except`, retourneer fout JSON naar frontend, implementeer backoff/herhaling. |
| `KeyError: 'innererror'` bij content filter fout | Structuur van content filter fout in Responses API veranderd | Chat Completions gebruikte `error.body["innererror"]["content_filter_result"]`; Responses API gebruikt `error.body["content_filters"][0]["content_filter_results"]` (meervoud, binnen een array). Herschrijf alle `innererror` toegang. |

---

## Migratie Risicotabel

| Symptom | Waarschijnlijke fout | Oplossing |
|---------|---------------|-----|
| Lege `output_text` / afgekorte respons | `max_output_tokens` te laag voor redeneermodellen | Stel `max_output_tokens=1000` of hoger in — redeneertokens tellen mee voor de limiet |
| `400 invalid_type: text.format` | `response_format` string doorgegeven i.p.v. `text.format` dict | Gebruik `text={"format": {"type": "json_schema", "name": "...", "strict": True, "schema": {...}}}` |
| `404 Not Found` op `/openai/v1/responses` | Verkeerde `base_url` — mist `/openai/v1/` suffix | Zorg dat `base_url=f"{endpoint}/openai/v1/"` is (met afsluitende slash) |
| `401 Unauthorized` na switch naar `OpenAI()` | `api_key` niet ingesteld of token provider niet correct doorgegeven | Voor EntraID: `api_key=token_provider` (de callable). Voor API key: `api_key=os.environ["AZURE_OPENAI_API_KEY"]` |
| Model geeft `deployment not found` | `model` parameter komt niet overeen met je Azure deployment naam | Gebruik `model=os.environ["AZURE_OPENAI_DEPLOYMENT"]` — dit is de deployment naam, niet de modelnaam |
| `json.loads(resp.output_text)` geeft `JSONDecodeError` | Schema niet afgedwongen of model ondersteunt geen strikte JSON | Zorg dat `"strict": True` in schema staat en controleer of model gestructureerde output ondersteunt |
| Streamen geeft geen `delta` events | Verkeerd event type gecontroleerd | Filter op `event.type == "response.output_text.delta"`, niet Chats `chat.completion.chunk` |
| `400` fout bij afbeeldingsinput na migratie | Afbeeldingscontenttype niet bijgewerkt | Verander `"type": "image_url"` → `"type": "input_image"` en vlak `"image_url": {"url": "..."}` af naar `"image_url": "..."` (platte string) |
| Hulpprogramma aanroepen lus oneindig | Hulpprogrammaresultaat ontbreekt in vervolg `input` | Voeg na het uitvoeren van een hulpprogramma een item `{"type": "function_call_output", "call_id": ..., "output": ...}` toe aan `input` in het volgende verzoek |
| `temperature` fout bij GPT-5 of o-series | Expliciete `temperature` waarde andere dan 1 | Verwijder `temperature` of stel in op `1` voor GPT-5 en o-series modellen (o1, o3-mini, o3, o4-mini) |
| `top_p` fout bij o-series | `top_p` wordt niet ondersteund | Verwijder `top_p` bij o-series modellen |
| `max_completion_tokens` niet herkend | Azure-specifieke parameter gebruikt | Vervang `max_completion_tokens` door `max_output_tokens`. Stel in op 4096+ voor o-series (redeneertokens tellen mee). |
| Lege/afgekorte output van o-series | `max_output_tokens` te laag | O-series gebruikt redeneertokens intern. Stel `max_output_tokens=4096` of hoger in — niet 500–1000. |
| `400 integer_below_min_value` voor `max_output_tokens` | Waarde onder 16 | Azure OpenAI vereist `max_output_tokens >= 16`. Gebruik 50+ voor tests, 1000+ voor productie. |
| `429 Too Many Requests` halverwege stream | Rate limited bij Azure OpenAI | Stream breekt stil zonder foutafhandeling. Wikkel altijd `async for event in await coroutine:` in `try/except` en retourneer `{"error": str(e)}` naar frontend. |
| `AzureDeveloperCliCredential` → `CredentialUnavailableError` | Verkeerde tenant of niet ingelogd | Geef `tenant_id=os.getenv("AZURE_TENANT_ID")` expliciet door. Run lokaal `azd auth login --tenant <tenant-id>`. |
| `404 Not Found` bij gebruik van GitHub Models (`models.github.ai`) | GitHub Models ondersteunt Responses API niet | Verwijder GitHub Models codepath volledig. Gebruik Azure OpenAI, OpenAI of compatibele lokale endpoint (bv. Ollama met Responses ondersteuning). |
| MAF `OpenAIChatCompletionClient` gebruikt nog Chat Completions | Legacy MAF client gebruikt in 1.0.0+ | In MAF 1.0.0+ gebruikt `OpenAIChatClient` standaard Responses API. Vervang `OpenAIChatCompletionClient` door `OpenAIChatClient`. Voor pre-1.0.0 versies upgrade naar `agent-framework-openai>=1.0.0`. |
| LangChain agent geeft lege output of faalt bij hulpprogramma aanroepen | `ChatOpenAI` gebruikt geen Responses API | Voeg `use_responses_api=True` toe aan `ChatOpenAI(...)`. Verander ook `.content` → `.text` in response berichten. |
| `KeyError: 'innererror'` in content filter foutafhandeling | Foutbody structuur veranderd in Responses API | Herschrijf `error.body["innererror"]["content_filter_result"]["jailbreak"]` → `error.body["content_filters"][0]["content_filter_results"]["jailbreak"]`. `innererror` wrapper is verdwenen; content filter details zitten nu in top-level `content_filters` array met `content_filter_results` (meervoud) binnen elke entry. |
| Raw HTTP-call naar `/openai/deployments/.../chat/completions` geeft 404 | Oude Chat Completions REST endpoint | Herschrijf URL naar `/openai/v1/responses`. Verander request body: `messages` → `input`, voeg `max_output_tokens` + `store: false` toe, verwijder `api-version` query parameter. Verander response parsing: `choices[0].message.content` → `output[0].content[0].text` (let op: `output_text` is SDK gemak, niet in rauwe REST JSON). |

---

## Valkuilen

1. Als je eerder Chat Completions gebruikte voor conversatiestatus, beheer dan je eigen status expliciet met Responses.
2. Geef de voorkeur aan `max_output_tokens` boven legacy `max_tokens`.
3. Bij migratie naar `gpt-5`, zorg dat `temperature` niet gespecificeerd is of op `1` staat.
4. Vervang Chat `content[].type: "text"` door Responses `content[].type: "input_text"` voor gebruiker-/systeem-invoer.
5. Voor `text.format`, lever een juiste dict aan (bijv. `{"type": "json_schema", "name": "Output", "schema": ..., "strict": True}`), geen platte string.
6. De `seed` parameter wordt niet ondersteund in Responses; verwijder deze uit verzoeken.
7. **Redeneren**: Neem `reasoning` alleen op als de originele code dit al gebruikte. Voeg `reasoning` niet toe aan API-aanroepen die dit niet hadden — veel modellen (bv. gpt-4o-mini) ondersteunen deze parameter niet.
8. **`max_output_tokens` grootte**: Voor redeneermodellen (GPT-5-mini, GPT-5, o-series), gebruik `max_output_tokens=4096` of hoger — niet 50–1000. Het model gebruikt redeneertokens intern vóór zichtbare output; te lage limieten veroorzaken afgekorte of lege responsen.
9. **O-series `max_completion_tokens`**: Als de originele code `max_completion_tokens` (Azure-specifiek voor o-series) gebruikte, vervang dit door `max_output_tokens`. Responses API accepteert `max_completion_tokens` niet.
10. **O-series `reasoning_effort`**: Als de originele code `reasoning_effort` (laag/middel/hoog) gebruikt, migreer dit naar `reasoning={"effort": "<waarde>"}` in de Responses API-aanroep.
11. **O-series streaming vertraging**: O-series modellen doen interne redenering voordat output gegenereerd wordt. Bij streaming verwacht je een langere vertraging voor het eerste `response.output_text.delta` event. Dit is normaal — het model redeneert, is niet vastgelopen.
9. **`_azure_ad_token_provider` is verdwenen**: `AsyncOpenAI` / `OpenAI` hebben geen `_azure_ad_token_provider` attribuut meer. Tests of code die dit gebruiken falen met `AttributeError`. De token provider wordt als `api_key` doorgegeven en is niet inspecteerbaar op het client object.
10. **Snapshot / golden files**: Als de testset snapshot testing gebruikt, moeten **alle** snapshot-bestanden met Chat Completions streaming vormen (`choices[0]`, `content_filter_results`, `function_call`, etc.) geüpdatet worden naar de nieuwe Responses vorm. Dit is makkelijk te missen en veroorzaakt snapshot assert-fouten.
11. **Mock monkeypatch pad**: Het monkeypatch target verandert van `openai.resources.chat.AsyncCompletions.create` → `openai.resources.responses.AsyncResponses.create` (of `Responses.create` voor sync). Gebruik van het oude pad doet stilletjes niets — de mock onderschept niet, en tests raken de echte API of falen.
12. **`input` niet `messages`**: Mock functies moeten `kwargs.get("input")` lezen, niet `kwargs.get("messages")`. Responses API gebruikt `input` voor gesprekshistorie.
13. **Omgevingsvariabele naamgeving**: Azure Identity SDK gebruikt `AZURE_CLIENT_ID` (niet `AZURE_OPENAI_CLIENT_ID`) voor `ManagedIdentityCredential(client_id=...)`. Hernoem in tests, `.env` bestanden, appinstellingen en Bicep/infrastructuur.
14. **`max_output_tokens` minimum is 16**: Azure OpenAI weigert waarden onder 16 met `400 integer_below_min_value`. Gebruik 50 voor tests, 1000+ voor productie. Oudere `max_tokens` had deze minimum niet.
15. **`tenant_id` voor `AzureDeveloperCliCredential`**: Wanneer de Azure OpenAI resource in een andere tenant staat, **moet** je `tenant_id` expliciet doorgeven — `AzureDeveloperCliCredential(tenant_id=os.getenv("AZURE_TENANT_ID"))`. Zonder dit gebruikt de credential stilletjes de verkeerde tenant en geeft `401`.
16. **Rate limits verschijnen anders bij streaming**: Bij Chat Completions voorkwam een 429 meestal dat de stream startte. Bij Responses API streaming kan een 429 **midden in de stream** voorkomen — de async iterator gooit een exceptie. Wikkel streaming loop altijd in `try/except` en geef een fout-JSON regel terug zodat de frontend dit netjes kan afhandelen.

17. **Streaming errorafhandeling is verplicht voor webapps**: Het patroon `try: async for event in await coroutine: ... except Exception as e: yield json.dumps({"error": str(e)})` is cruciaal. Zonder dit stopt de SSE/JSONL-stream geruisloos bij elke server-side fout en blijft de frontend hangen.
18. **Tooldefinities moeten het platte formaat gebruiken**: De Responses API verwacht `{"type": "function", "name": ..., "parameters": ...}` — niet het geneste Chat Completions formaat `{"type": "function", "function": {"name": ..., "parameters": ...}}`. Dit is de meest voorkomende migratiefout bij code voor functie-aanroep.
19. **`pydantic_function_tool()` is incompatibel**: De helper `openai.pydantic_function_tool()` genereert nog het oude geneste formaat. Gebruik deze niet met `responses.create()`. Definieer tool-schema’s handmatig of maak de output plat.
20. **Toolresultaten gebruiken `function_call_output`, niet `role: tool`**: Na het uitvoeren van een tool voeg je toe `{"type": "function_call_output", "call_id": ..., "output": ...}` — niet `{"role": "tool", "tool_call_id": ..., "content": ...}`. Voor de tool-aanvraag van de assistent gebruik je `messages.extend(response.output)` — niet handmatig een `{"role": "assistant", "tool_calls": [...]}` dict.
21. **`strict: true` vereist `required` + `additionalProperties: false`**: Bij gebruik van `strict: true` op een tool moet elke eigenschap in de `required` array staan en moet `additionalProperties` `false` zijn. Het ontbreken van een van beide veroorzaakt een 400-fout.
22. **Functie-aanroep-ID’s hebben specifieke voorvoegsels**: Bij het leveren van few-shot `function_call` items in `input` moet het `id`-veld beginnen met `fc_` en het `call_id`-veld met `call_` (bijv. `"id": "fc_example1", "call_id": "call_example1"`). Het oude Chat Completions prefix `call_` voor `id` wordt afgewezen.
23. **GitHub Models ondersteunt de Responses API niet**: Als de app een GitHub Models codepad heeft (`base_url` wijzend naar `models.github.ai` of `models.inference.ai.azure.com`), verwijder dit dan volledig. Er is geen migratiepad — schakel over naar Azure OpenAI, OpenAI of een compatibele lokale endpoint.
24. **Structuur van foutbody contentfilter is veranderd**: Chat Completions fouten gebruikten `error.body["innererror"]["content_filter_result"]` (enkelvoud). Responses API fouten gebruiken `error.body["content_filters"][0]["content_filter_results"]` (meervoud, binnen een array). De sleutel `innererror` bestaat niet meer. Code die direct `innererror` aanspreekt veroorzaakt `KeyError` tijdens runtime — dit is makkelijk te missen bij migratie omdat het alleen optreedt als het contentfilter daadwerkelijk afgaat. Zoek altijd naar `innererror` tijdens migratie.
25. **Raw HTTP-aanroepen vereisen URL + body herschrijving**: Apps die Azure OpenAI REST direct aanroepen (via `requests`, `httpx`, `aiohttp`) met `/openai/deployments/{name}/chat/completions?api-version=...` moeten overschakelen naar `/openai/v1/responses`. De request-body gebruikt `input` in plaats van `messages`, vereist `max_output_tokens` en `store`, en de query param `api-version` wordt weggelaten. De response-body tekst staat in `output[0].content[0].text` — **niet** in `output_text`, wat een SDK gemaksattribuut is dat niet voorkomt in de ruwe REST JSON.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:
Dit document is vertaald met behulp van de AI vertaaldienst [Co-op Translator](https://github.com/Azure/co-op-translator). Hoewel we streven naar nauwkeurigheid, dient u er rekening mee te houden dat geautomatiseerde vertalingen fouten of onnauwkeurigheden kunnen bevatten. Het originele document in de oorspronkelijke taal moet worden beschouwd als de gezaghebbende bron. Voor kritieke informatie wordt professionele menselijke vertaling aanbevolen. Wij zijn niet aansprakelijk voor eventuele misverstanden of verkeerde interpretaties die voortvloeien uit het gebruik van deze vertaling.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->