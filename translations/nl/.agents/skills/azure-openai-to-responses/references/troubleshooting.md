# Probleemoplossing, Risicotabel & Valkuilen

## Probleemoplossing 400s

| Fout | Oplossing |
|-------|-----|
| `missing_required_parameter: tools[0].name` | Tooldefinitie gebruikt oud genest Chat Completions-formaat | Plat maken van `{"type": "function", "function": {"name": ...}}` naar `{"type": "function", "name": ..., "parameters": ...}` — naam, beschrijving, parameters gaan op het topniveau |
| `unknown_parameter: input[N].tool_calls` | Multi-turn tool resultaten gebruiken oud Chat Completions-formaat | Vervang `{"role": "assistant", "tool_calls": [...]}` + `{"role": "tool", ...}` met `response.output` items + `{"type": "function_call_output", "call_id": ..., "output": ...}` |
| `invalid_function_parameters: 'required' is required` | `strict: true` tool mist `required` array | Bij `strict: true` moeten alle eigenschappen in `required` staan en moet `additionalProperties: false` worden ingesteld |
| `invalid_function_parameters: 'additionalProperties' is required` | `strict: true` tool mist `additionalProperties: false` | Voeg `"additionalProperties": false` toe aan het parameters-object |
| `invalid input[N].id: Expected an ID that begins with 'fc'` | Few-shot function_call ID heeft verkeerde prefix | Function call IDs moeten beginnen met `fc_` (bijv. `fc_example1`), niet met `call_` |
| `missing_required_parameter: text.format.name` | Voeg `"name"` sleutel toe aan het format dict (bijv. `"name": "Output"`) |
| `invalid_type: text.format` | Zorg dat `text.format` een dict is met `type`, `name`, `strict`, `schema` keys — geen string |
| `invalid input content type` | Gebruik `input_text`/`output_text` content types in plaats van Chat `text` |
| `invalid input content type` (image) | Beeldinhoud gebruikt nog `"type": "image_url"` | Verander naar `"type": "input_image"` |
| `Expected object, got string` on `image_url` | `image_url` is nog een genest object `{"url": "..."}` | Maak het plat naar een gewone string: `"image_url": "https://..."` of `"image_url": "data:image/...;base64,..."` |
| `integer below minimum value` for `max_output_tokens` | Minimum is **16** op Azure OpenAI. Gebruik 50+ voor testen, 1000+ voor productie. |
| `429 Too Many Requests` tijdens streaming | Rate limit. Omwikkel streaming met `try/except`, geef fout-JSON door aan frontend, implementeer backoff/herhaling. |
| `KeyError: 'innererror'` bij content filter fout | Structuur van content filter fout in Responses API veranderd | Chat Completions gebruikte `error.body["innererror"]["content_filter_result"]`; Responses API gebruikt `error.body["content_filters"][0]["content_filter_results"]` (meervoud, in een array). Herschrijf alle `innererror` toegang. |

---

## Migratie Risicotabel

| Symptoom | Waarschijnlijke Fout | Oplossing |
|---------|---------------|-----|
| Lege `output_text` / ingekorte respons | `max_output_tokens` te laag voor reasoning-modellen | Stel `max_output_tokens=1000` of hoger in — reasoning tokens tellen mee voor de limiet |
| `400 invalid_type: text.format` | `response_format` string doorgegeven in plaats van `text.format` dict | Gebruik `text={"format": {"type": "json_schema", "name": "...", "strict": True, "schema": {...}}}` |
| `404 Not Found` op `/openai/v1/responses` | Verkeerde `base_url` — mist `/openai/v1/` suffix | Zorg dat `base_url=f"{endpoint}/openai/v1/"` is (met trailing slash) |
| `401 Unauthorized` na switch naar `OpenAI()` | `api_key` niet ingesteld of token provider verkeerd doorgegeven | Voor EntraID: `api_key=token_provider` (de callable). Voor API key: `api_key=os.environ["AZURE_OPENAI_API_KEY"]` |
| Model geeft `deployment not found` | `model` parameter komt niet overeen met je Azure deployment naam | Gebruik `model=os.environ["AZURE_OPENAI_DEPLOYMENT"]` — dit is de deployment naam, niet de modelnaam |
| `json.loads(resp.output_text)` geeft `JSONDecodeError` | Schema niet afgedwongen of model ondersteunt geen strikt JSON | Zorg dat `"strict": True` in schema staat, en verifieer dat model gestructureerde output ondersteunt |
| Streaming geeft geen `delta` events | Controleert verkeerde event type | Filter op `event.type == "response.output_text.delta"`, niet Chat's `chat.completion.chunk` |
| `400` fout bij afbeelding invoer na migratie | Afbeelding content type niet bijgewerkt | Verander `"type": "image_url"` → `"type": "input_image"` en maak `"image_url": {"url": "..."}` plat naar `"image_url": "..."` (platte string) |
| Tool calls lopen in oneindige lus | Ontbrekende tool resultaat in vervolg-`input` | Na het uitvoeren van een tool, voeg een `{"type": "function_call_output", "call_id": ..., "output": ...}` item toe aan `input` bij het volgende verzoek |
| `temperature` fout met GPT-5 of o-series | Expliciete `temperature` waarde anders dan 1 | Verwijder `temperature` of stel in op `1` voor GPT-5 en o-series modellen (o1, o3-mini, o3, o4-mini) |
| `top_p` fout met o-series | `top_p` niet ondersteund | Verwijder `top_p` bij het gebruik van o-series modellen |
| `max_completion_tokens` wordt niet herkend | Gebruik van Azure-specifieke parameter | Vervang `max_completion_tokens` door `max_output_tokens`. Stel in op 4096+ voor o-series (reasoning tokens tellen mee). |
| Lege/afgekorte output van o-series | `max_output_tokens` te laag | O-series gebruikt reasoning tokens intern. Stel `max_output_tokens=4096` of hoger in — niet 500–1000. |
| `400 integer_below_min_value` voor `max_output_tokens` | Waarde onder 16 | Azure OpenAI vereist `max_output_tokens >= 16`. Gebruik 50+ voor snelle tests, 1000+ voor productie. |
| `429 Too Many Requests` midden in stream | Rate limit door Azure OpenAI | Stream breekt stil zonder foutafhandeling. Altijd `async for event in await coroutine:` omwikkelen met `try/except` en `{"error": str(e)}` naar frontend sturen. |
| `AzureDeveloperCliCredential` → `CredentialUnavailableError` | Verkeerde tenant of niet ingelogd | Geef `tenant_id=os.getenv("AZURE_TENANT_ID")` expliciet door. Voer lokaal `azd auth login --tenant <tenant-id>` uit. |
| `404 Not Found` met GitHub Models (`models.github.ai`) | GitHub Models ondersteunt Responses API niet | Verwijder de GitHub Models codepad volledig. Gebruik Azure OpenAI, OpenAI, of een compatibele lokale endpoint (bijv. Ollama met Responses ondersteuning). |
| MAF `OpenAIChatCompletionClient` gebruikt nog Chat Completions | Gebruik van legacy MAF client in 1.0.0+ | In MAF 1.0.0+ gebruikt `OpenAIChatClient` standaard de Responses API. Vervang `OpenAIChatCompletionClient` door `OpenAIChatClient`. Voor pre-1.0.0: upgrade naar `agent-framework-openai>=1.0.0`. |
| LangChain agent geeft lege output of faalt met tool calls | `ChatOpenAI` gebruikt niet de Responses API | Voeg `use_responses_api=True` toe aan `ChatOpenAI(...)`. Verander ook `.content` → `.text` op response messages. |
| `KeyError: 'innererror'` in content filter foutafhandelaar | Fout body structuur veranderd in Responses API | Herschrijf `error.body["innererror"]["content_filter_result"]["jailbreak"]` → `error.body["content_filters"][0]["content_filter_results"]["jailbreak"]`. De `innererror` wrapper is verdwenen; content filter details zitten nu in een topniveau `content_filters` array met `content_filter_results` (meervoud) binnen elke entry. |
| Raw HTTP call naar `/openai/deployments/.../chat/completions` geeft 404 | Oude Chat Completions REST endpoint | Herschrijf URL naar `/openai/v1/responses`. Verander request body: `messages` → `input`, voeg `max_output_tokens` + `store: false` toe, verwijder `api-version` query param. Verander response parsing: `choices[0].message.content` → `output[0].content[0].text` (let op: `output_text` is een SDK gemaksproperty, niet aanwezig in de raw REST JSON). |

---

## Valkuilen

1. Als je eerder Chat Completions gebruikte voor gespreksstaat, beheer dan je eigen staat expliciet met Responses.
2. Geef de voorkeur aan `max_output_tokens` boven legacy `max_tokens`.
3. Bij migratie naar `gpt-5`, zorg dat `temperature` niet is opgegeven of ingesteld is op `1`.
4. Vervang Chat `content[].type: "text"` door Responses `content[].type: "input_text"` voor gebruiker/system invoer.
5. Voor `text.format`, lever een juiste dict aan (bijv. `{"type": "json_schema", "name": "Output", "schema": ..., "strict": True}`), geen platte string.
6. De `seed` parameter wordt niet ondersteund in Responses; verwijder hem uit verzoeken.
7. **Redeneren**: Voeg `reasoning` alleen toe als de oorspronkelijke code dat al gebruikte. Voeg geen `reasoning` toe aan API calls die het niet hadden — veel niet-redenerende modellen ondersteunen deze parameter niet.
8. **`max_output_tokens` sizing**: Voor reasoning modellen (GPT-5-mini, GPT-5, o-series), gebruik `max_output_tokens=4096` of hoger — niet 50–1000. Het model gebruikt reasoning tokens intern vóór het genereren van zichtbare output; te lage limieten veroorzaken ingekorte of lege respons.
9. **O-series `max_completion_tokens`**: Als de originele code `max_completion_tokens` gebruikte (Azure-specifiek voor o-series), vervang door `max_output_tokens`. De Responses API accepteert `max_completion_tokens` niet.
10. **O-series `reasoning_effort`**: Als de originele code `reasoning_effort` gebruikt (laag/midden/hoog), migreer naar `reasoning={"effort": "<waarde>"}` in de Responses API oproep.
11. **O-series streaming vertraging**: O-series modellen voeren interne redenering uit vóór outputgeneratie. Bij streaming verwacht een langere vertraging vóór het eerste `response.output_text.delta` event. Dit is normaal — het model is aan het redeneren, niet vastgelopen.
9. **`_azure_ad_token_provider` is verdwenen**: `AsyncOpenAI` / `OpenAI` hebben geen `_azure_ad_token_provider` attribuut. Tests of code die dit attribuut benaderen falen met `AttributeError`. De token provider wordt als `api_key` doorgegeven en is niet inspecteerbaar op het client object.
10. **Snapshot / gouden bestanden**: Als de testsuite snapshot testing gebruikt, moeten **alle** snapshot bestanden met Chat Completions streaming vormen (`choices[0]`, `content_filter_results`, `function_call`, etc.) worden bijgewerkt naar de nieuwe Responses vorm. Dit wordt gemakkelijk gemist en veroorzaakt snapshot assertie fouten.
11. **Mock monkeypatch pad**: De monkeypatch target verandert van `openai.resources.chat.AsyncCompletions.create` → `openai.resources.responses.AsyncResponses.create` (of `Responses.create` voor sync). Gebruik van het oude pad doet stilzwijgend niets — de mock onderschept niet, en tests raken de echte API of falen.
12. **`input` niet `messages`**: Mock-functies moeten `kwargs.get("input")` lezen, niet `kwargs.get("messages")`. De Responses API gebruikt `input` voor de gesprekshistorie.
13. **Omgevingsvariabele naamgeving**: Azure Identity SDK gebruikt `AZURE_CLIENT_ID` (niet `AZURE_OPENAI_CLIENT_ID`) voor `ManagedIdentityCredential(client_id=...)`. Hernoem in tests, `.env` bestanden, app settings en Bicep/infra.
14. **`max_output_tokens` minimum is 16**: Azure OpenAI wijst waarden onder 16 af met `400 integer_below_min_value`. Gebruik `50` voor snelle tests, `1000`+ voor productie. De oude `max_tokens` had geen dergelijk minimum.
15. **`tenant_id` voor `AzureDeveloperCliCredential`**: Wanneer de Azure OpenAI resource in een andere tenant staat, **moet** je expliciet `tenant_id` doorgeven — `AzureDeveloperCliCredential(tenant_id=os.getenv("AZURE_TENANT_ID"))`. Zonder dit gebruikt de credential stilzwijgend de verkeerde tenant en geeft `401`.
16. **Rate limits verschijnen anders bij streaming**: Met Chat Completions voorkwam een 429 meestal dat de stream begon. Met Responses API streaming kan een 429 **midden in de stream** voorkomen — de async iterator gooit een uitzondering. Omwikkel de streaming loop altijd met `try/except` en geef een fout-JSON regel terug zodat de frontend het mooi kan afhandelen.

17. **Streamingfoutafhandeling is verplicht voor web-apps**: Het patroon `try: async for event in await coroutine: ... except Exception as e: yield json.dumps({"error": str(e)})` is cruciaal. Zonder dit sterft de SSE/JSONL-stream geruisloos af bij elke serverfout en blijft de frontend hangen.
18. **Tooldefinities moeten het platte formaat gebruiken**: De Responses API verwacht `{"type": "function", "name": ..., "parameters": ...}` — niet het geneste `{"type": "function", "function": {"name": ..., "parameters": ...}}` van Chat Completions. Dit is de meest voorkomende migratiefout voor functie-aanroepcode.
19. **`pydantic_function_tool()` is incompatibel**: De helper `openai.pydantic_function_tool()` genereert nog steeds het oude geneste formaat. Gebruik het niet met `responses.create()`. Definieer toolschema's handmatig of vlak de uitvoer af.
20. **Toolresultaten gebruiken `function_call_output`, niet `role: tool`**: Voeg na het uitvoeren van een tool `{"type": "function_call_output", "call_id": ..., "output": ...}` toe — niet `{"role": "tool", "tool_call_id": ..., "content": ...}`. Voor het toolverzoek van de assistent gebruik je `messages.extend(response.output)` — niet een handmatig `{"role": "assistant", "tool_calls": [...]}`-dictionary.
21. **`strict: true` vereist `required` + `additionalProperties: false`**: Bij gebruik van `strict: true` op een tool moet elke eigenschap in de array `required` staan en moet `additionalProperties` `false` zijn. Het ontbreken van een van beide veroorzaakt een 400-fout.
22. **Functie-aanroep-ID's hebben specifieke voorvoegsels**: Bij het aanleveren van few-shot `function_call` items in `input` moet het `id`-veld beginnen met `fc_` en het `call_id`-veld met `call_` (bijv. `"id": "fc_example1", "call_id": "call_example1"`). Het oude voorvoegsel `call_` gebruiken voor `id` in Chat Completions wordt afgewezen.
23. **GitHub Models ondersteunt de Responses API niet**: Als de app een GitHub Models-codepad heeft (`base_url` die verwijst naar `models.github.ai` of `models.inference.ai.azure.com`), verwijder het dan volledig. Er is geen migratieroute — schakel over naar Azure OpenAI, OpenAI of een compatibele lokale endpoint.
24. **Contentfilter-foutlichaamstructuur is gewijzigd**: Chat Completions-fouten gebruikten `error.body["innererror"]["content_filter_result"]` (enkelvoud). Responses API-fouten gebruiken `error.body["content_filters"][0]["content_filter_results"]` (meervoud, in een array). De sleutel `innererror` bestaat niet meer. Code die direct `innererror` aanspreekt, veroorzaakt tijdens runtime een `KeyError` — dit is makkelijk te missen tijdens migratie omdat het alleen voorkomt als het contentfilter daadwerkelijk wordt geactiveerd. Doorzoek altijd op `innererror` tijdens migratie.
25. **Ruwe HTTP-aanroepen vereisen URL- en bodyherschrijving**: Apps die Azure OpenAI REST direct aanroepen (via `requests`, `httpx`, `aiohttp`) met `/openai/deployments/{name}/chat/completions?api-version=...` moeten overschakelen naar `/openai/v1/responses`. De requestbody gebruikt `input` in plaats van `messages`, vereist `max_output_tokens` en `store`, en de queryparameter `api-version` wordt verwijderd. De responsebody-tekst staat in `output[0].content[0].text` — **niet** in `output_text`, dat is een SDK handigheid die niet in de ruwe REST JSON voorkomt.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:
Dit document is vertaald met behulp van de AI vertaaldienst [Co-op Translator](https://github.com/Azure/co-op-translator). Hoewel we streven naar nauwkeurigheid, dient u er rekening mee te houden dat geautomatiseerde vertalingen fouten of onnauwkeurigheden kunnen bevatten. Het originele document in de oorspronkelijke taal moet worden beschouwd als de gezaghebbende bron. Voor kritieke informatie wordt professionele menselijke vertaling aanbevolen. Wij zijn niet aansprakelijk voor eventuele misverstanden of verkeerde interpretaties die voortvloeien uit het gebruik van deze vertaling.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->