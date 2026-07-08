# Fejlfinding, Risikotabel & Faldgruber

## Fejlfinding 400'er

| Fejl | Løsning |
|-------|-----|
| `missing_required_parameter: tools[0].name` | Værktøjsdefinition bruger gammelt Chat Completions indlejret format | Flad ud fra `{"type": "function", "function": {"name": ...}}` til `{"type": "function", "name": ..., "parameters": ...}` — name, description, parameters går på topniveau |
| `unknown_parameter: input[N].tool_calls` | Multi-turn værktøjsresultater bruger gammelt Chat Completions format | Erstat `{"role": "assistant", "tool_calls": [...]}` + `{"role": "tool", ...}` med `response.output` elementer + `{"type": "function_call_output", "call_id": ..., "output": ...}` |
| `invalid_function_parameters: 'required' is required` | `strict: true` værktøj mangler `required` array | Når `strict: true`, skal alle properties listes i `required`, og `additionalProperties: false` skal sættes |
| `invalid_function_parameters: 'additionalProperties' is required` | `strict: true` værktøj mangler `additionalProperties: false` | Tilføj `"additionalProperties": false` til parameters-objektet |
| `invalid input[N].id: Expected an ID that begins with 'fc'` | Few-shot function_call ID har forkert præfiks | Funktionskalds-ID’er skal starte med `fc_` (fx `fc_example1`), ikke `call_` |
| `missing_required_parameter: text.format.name` | Tilføj `"name"` nøgle til format-dict (fx `"name": "Output"`) |
| `invalid_type: text.format` | Sørg for at `text.format` er en dict med nøglerne `type`, `name`, `strict`, `schema` — ikke en streng |
| `invalid input content type` | Brug `input_text`/`output_text` indholdstyper i stedet for Chat `text` |
| `invalid input content type` (billede) | Billedindhold bruger stadig `"type": "image_url"` | Skift til `"type": "input_image"` |
| `Expected object, got string` på `image_url` | `image_url` er stadig et indlejret objekt `{"url": "..."}` | Flad ud til en simpel streng: `"image_url": "https://..."` eller `"image_url": "data:image/...;base64,..."` |
| `integer below minimum value` for `max_output_tokens` | Minimum er **16** på Azure OpenAI. Brug 50+ til tests, 1000+ til produktion. |
| `429 Too Many Requests` under streaming | Ratebegrænset. Pak streaming i `try/except`, send fejl-JSON til frontend, implementer backoff/genforsøg. |
| `KeyError: 'innererror'` på content filter fejl | Content filter fejl body-struktur ændret i Responses API | Chat Completions brugte `error.body["innererror"]["content_filter_result"]`; Responses API bruger `error.body["content_filters"][0]["content_filter_results"]` (flertal, inde i array). Omskriv alle `innererror` adgang. |

---

## Migration Risikotabel

| Symptom | Sandsynlig Fejl | Løsning |
|---------|---------------|-----|
| Tom `output_text` / afkortet svar | `max_output_tokens` for lav for ræsonneringsmodeller | Sæt `max_output_tokens=1000` eller højere — ræsonneringstokens tæller mod grænsen |
| `400 invalid_type: text.format` | Sendt `response_format` streng i stedet for `text.format` dict | Brug `text={"format": {"type": "json_schema", "name": "...", "strict": True, "schema": {...}}}` |
| `404 Not Found` på `/openai/v1/responses` | Forkert `base_url` — mangler `/openai/v1/` suffix | Sørg for `base_url=f"{endpoint}/openai/v1/"` (med trailing slash) |
| `401 Unauthorized` efter skift til `OpenAI()` | `api_key` ikke sat eller token provider ikke korrekt givet | For EntraID: `api_key=token_provider` (callable). For API-nøgle: `api_key=os.environ["AZURE_OPENAI_API_KEY"]` |
| Model returnerer `deployment not found` | `model` parameter matcher ikke dit Azure deployment navn | Brug `model=os.environ["AZURE_OPENAI_DEPLOYMENT"]` — dette er deploymentsnavnet, ikke modelnavnet |
| `json.loads(resp.output_text)` kaster `JSONDecodeError` | Skema ikke håndhævet eller model understøtter ikke strict JSON | Sørg for `"strict": True` i skemaet, og verificer at modellen understøtter struktureret output |
| Streaming giver ingen `delta` events | Tjekker forkert event-type | Filtrer på `event.type == "response.output_text.delta"`, ikke Chat's `chat.completion.chunk` |
| `400` fejl på billedeinput efter migration | Billedindholdstype ikke opdateret | Skift `"type": "image_url"` → `"type": "input_image"` og flad `"image_url": {"url": "..."}` → `"image_url": "..."` (ren streng) |
| Værktøjskald kører i uendelig løkke | Manglende værktøjsresultat i opfølgende `input` | Efter værktøjskald, tilføj et `{"type": "function_call_output", "call_id": ..., "output": ...}` element til `input` i næste anmodning |
| `temperature` fejl med GPT-5 eller o-serie | Eksplícit `temperature` værdi forskellig fra 1 | Fjern `temperature` eller sæt til `1` for GPT-5 og o-serie modeller (o1, o3-mini, o3, o4-mini) |
| `top_p` fejl med o-serie | `top_p` ikke understøttet | Fjern `top_p` når du målretter mod o-serie modeller |
| `max_completion_tokens` ikke genkendt | Brug af Azure-specifik parameter | Erstat `max_completion_tokens` med `max_output_tokens`. Sæt til 4096+ for o-serien (ræsonneringstokens tæller mod grænsen). |
| Tomt/afkortet output fra o-serien | `max_output_tokens` for lav | O-serien bruger intern ræsonneringstokens. Sæt `max_output_tokens=4096` eller højere — ikke 500–1000. |
| `400 integer_below_min_value` for `max_output_tokens` | Værdi under 16 | Azure OpenAI håndhæver `max_output_tokens >= 16`. Brug 50+ til tests, 1000+ til produktion. |
| `429 Too Many Requests` midt i stream | Ratebegrænset af Azure OpenAI | Stream bryder stille uden fejlhåndtering. Pak altid `async for event in await coroutine:` i `try/except` og send `{"error": str(e)}` til frontend. |
| `AzureDeveloperCliCredential` → `CredentialUnavailableError` | Forkert tenant eller ikke logget ind | Giv `tenant_id=os.getenv("AZURE_TENANT_ID")` eksplicit. Kør `azd auth login --tenant <tenant-id>` lokalt. |
| `404 Not Found` med GitHub Models (`models.github.ai`) | GitHub Models understøtter ikke Responses API | Fjern GitHub Models kodebanen helt. Brug Azure OpenAI, OpenAI eller en kompatibel lokal endpoint (fx Ollama med Responses support). |
| MAF `OpenAIChatCompletionClient` bruger stadig Chat Completions | Bruger legacy MAF client i 1.0.0+ | I MAF 1.0.0+ bruger `OpenAIChatClient` Responses API som standard. Erstat `OpenAIChatCompletionClient` med `OpenAIChatClient`. For pre-1.0.0, opgrader til `agent-framework-openai>=1.0.0`. |
| LangChain agent returnerer tomt eller fejler med værktøjskald | `ChatOpenAI` bruger ikke Responses API | Tilføj `use_responses_api=True` til `ChatOpenAI(...)`. Ændr også `.content` → `.text` på svarbeskeder. |
| `KeyError: 'innererror'` i content filter fejlbehandler | Fejl body struktur ændret i Responses API | Omskriv `error.body["innererror"]["content_filter_result"]["jailbreak"]` → `error.body["content_filters"][0]["content_filter_results"]["jailbreak"]`. `innererror` wrapperen er væk; content filter detaljer findes nu i et topniveau `content_filters` array med `content_filter_results` (flertal) inde i hvert element. |
| Råt HTTP-kald til `/openai/deployments/.../chat/completions` returnerer 404 | Gammel Chat Completions REST endpoint | Omskriv URL til `/openai/v1/responses`. Skift request body: `messages` → `input`, tilføj `max_output_tokens` + `store: false`, fjern `api-version` query param. Skift response parsing: `choices[0].message.content` → `output[0].content[0].text` (bemærk: `output_text` er en SDK convenience property, ikke i rå REST JSON). |

---

## Faldgruber

1. Hvis du tidligere brugte Chat Completions til samtalestatus, håndtér din egen status eksplicit med Responses.
2. Foretræk `max_output_tokens` frem for gammel `max_tokens`.
3. Ved migration til `gpt-5` skal du sikre, at `temperature` ikke er angivet eller sat til `1`.
4. Erstat Chat `content[].type: "text"` med Responses `content[].type: "input_text"` for bruger-/systeminput.
5. For `text.format`, giv en korrekt dict (fx `{"type": "json_schema", "name": "Output", "schema": ..., "strict": True}`), ikke en simpel streng.
6. `seed` parameteren understøttes ikke i Responses; fjern den fra requests.
7. **Ræsonnering**: Inkludér kun `reasoning`, hvis originalkode allerede brugte det. Tilføj ikke `reasoning` til API-kald, der ikke havde det — mange modeller (fx gpt-4o-mini) understøtter ikke denne parameter.
8. **`max_output_tokens` størrelse**: For ræsonneringsmodeller (GPT-5-mini, GPT-5, o-serien) brug `max_output_tokens=4096` eller højere — ikke 50–1000. Modellen bruger ræsonneringstokens internt før generering af synligt output; for lave grænser forårsager afkortede eller tomme svar.
9. **O-serie `max_completion_tokens`**: Hvis originalkode brugte `max_completion_tokens` (Azure-specifik til o-serien), erstat med `max_output_tokens`. Responses API accepterer ikke `max_completion_tokens`.
10. **O-serie `reasoning_effort`**: Hvis originalkode bruger `reasoning_effort` (low/medium/high), migrér det til `reasoning={"effort": "<value>"}` i Responses API kaldet.
11. **O-serie streaming forsinkelse**: O-serie modeller udfører intern ræsonnering før outputgenerering. Ved streaming forventes en længere forsinkelse før første `response.output_text.delta` event. Dette er normalt — modellen ræsonnerer, ikke hænger.
9. **`_azure_ad_token_provider` er væk**: `AsyncOpenAI` / `OpenAI` har ikke `_azure_ad_token_provider` attribut. Tests eller kode, der tilgår denne attribut, fejler med `AttributeError`. Token provideren gives som `api_key` og kan ikke inspiceres på klientobjektet.
10. **Snapshot / golden filer**: Hvis testsuiten bruger snapshot-testning, skal **alle** snapshot-filer med Chat Completions streaming-strukturer (`choices[0]`, `content_filter_results`, `function_call` osv.) opdateres til nyt Responses format. Dette er let at overse og forårsager snapshot assertion-fejl.
11. **Mock monkeypatch sti**: Monkeypatch målet ændres fra `openai.resources.chat.AsyncCompletions.create` → `openai.resources.responses.AsyncResponses.create` (eller `Responses.create` for sync). Brug af gammel sti gør ingenting stiltiende — mock’en opfanger ikke, og tests rammer den rigtige API eller fejler.
12. **`input` ikke `messages`**: Mock-funktioner skal læse `kwargs.get("input")`, ikke `kwargs.get("messages")`. Responses API bruger `input` til samtalehistorik.
13. **Miljøvariabel-navngivning**: Azure Identity SDK bruger `AZURE_CLIENT_ID` (ikke `AZURE_OPENAI_CLIENT_ID`) for `ManagedIdentityCredential(client_id=...)`. Omdøb i tests, `.env` filer, appindstillinger og Bicep/infra.
14. **`max_output_tokens` minimum er 16**: Azure OpenAI afviser værdier under 16 med `400 integer_below_min_value`. Brug 50 til smoke tests, 1000+ til produktion. Den gamle `max_tokens` havde ikke dette minimum.
15. **`tenant_id` for `AzureDeveloperCliCredential`**: Når Azure OpenAI ressourcen er i en anden tenant, skal du **udtrykkeligt** angive `tenant_id` — `AzureDeveloperCliCredential(tenant_id=os.getenv("AZURE_TENANT_ID"))`. Uden dette bruger credentialen stille den forkerte tenant og returnerer `401`.
16. **Ratebegrænsninger viser sig forskelligt ved streaming**: Med Chat Completions forhindrede en 429 typisk at streamen startede. Med Responses API streaming kan 429 forekomme **midt i streamen** — den asynkrone iterator kaster en undtagelse. Pak altid streaming-løkken i `try/except` og send en fejl-JSON-linje, så frontend kan håndtere det elegant.

17. **Streaming fejlbehandling er obligatorisk for webapps**: Mønstret `try: async for event in await coroutine: ... except Exception as e: yield json.dumps({"error": str(e)})` er kritisk. Uden det dør SSE/JSONL-strømmen stille ved enhver serverfejl, og frontend hænger.
18. **Værktøjsdefinitioner skal bruge fladt format**: Responses API forventer `{"type": "function", "name": ..., "parameters": ...}` — ikke den indlejrede Chat Completions `{"type": "function", "function": {"name": ..., "parameters": ...}}`. Dette er den mest almindelige migrationsfejl for funktionkaldskode.
19. **`pydantic_function_tool()` er inkompatibel**: Hjælpefunktionen `openai.pydantic_function_tool()` genererer stadig det gamle indlejrede format. Brug den ikke med `responses.create()`. Definer værktøjs-skemaer manuelt eller flad udgangen.
20. **Værktøjsresultater bruger `function_call_output`, ikke `role: tool`**: Efter udførelse af et værktøj, tilføj `{"type": "function_call_output", "call_id": ..., "output": ...}` — ikke `{"role": "tool", "tool_call_id": ..., "content": ...}`. For assistentens værktøjsanmodning, brug `messages.extend(response.output)` — ikke en manuel `{"role": "assistant", "tool_calls": [...]}` dict.
21. **`strict: true` kræver `required` + `additionalProperties: false`**: Ved brug af `strict: true` på et værktøj skal hver egenskab være opført i `required` arrayet og `additionalProperties` skal være `false`. Manglende af en af disse forårsager en 400-fejl.
22. **Funktionkald-ID’er har specifikke præfikser**: Når få-skud `function_call` elementer gives i `input`, skal `id` feltet starte med `fc_` og `call_id` feltet starte med `call_` (fx `"id": "fc_example1", "call_id": "call_example1"`). Brug af den gamle Chat Completions `call_` præfiks til `id` afvises.
23. **GitHub Models understøtter ikke Responses API**: Hvis appen har en GitHub Models-kodevej (`base_url` der peger på `models.github.ai` eller `models.inference.ai.azure.com`), fjern den helt. Der findes ingen migrationsvej — skift til Azure OpenAI, OpenAI eller en kompatibel lokal endpoint.
24. **Strukturen for fejlindhold ved content filter er ændret**: Chat Completions fejl brugte `error.body["innererror"]["content_filter_result"]` (ental). Responses API fejl bruger `error.body["content_filters"][0]["content_filter_results"]` (flertal, inde i et array). `innererror` nøglen findes ikke længere. Kode der direkte tilgår `innererror` vil rejse `KeyError` ved kørsel – dette er nemt at overse i migration da det kun opstår, når content filteret rent faktisk udløses. Søg altid efter `innererror` under migration.
25. **Rå HTTP-kald kræver URL + body omskrivning**: Apps der kalder Azure OpenAI REST direkte (via `requests`, `httpx`, `aiohttp`) med `/openai/deployments/{name}/chat/completions?api-version=...` skal skifte til `/openai/v1/responses`. Anmodnings-body bruger `input` i stedet for `messages`, kræver `max_output_tokens` og `store`, og `api-version` query parametret droppes. Svar-body teksten findes ved `output[0].content[0].text` — **ikke** `output_text`, som er en SDK bekvemmelighedsegenskab, ikke til stede i rå REST JSON.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfraskrivelse**:
Dette dokument er blevet oversat ved hjælp af AI-oversættelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selvom vi bestræber os på nøjagtighed, skal du være opmærksom på, at automatiserede oversættelser kan indeholde fejl eller unøjagtigheder. Det originale dokument på dets oprindelige sprog bør betragtes som den autoritative kilde. For kritisk information anbefales professionel menneskelig oversættelse. Vi påtager os intet ansvar for misforståelser eller fejltolkninger, der opstår som følge af brugen af denne oversættelse.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->