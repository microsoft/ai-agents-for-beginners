# Fejlfinding, Risiko-tabel & Faldgruber

## Fejlfinding 400-fejl

| Fejl | Løsning |
|-------|-----|
| `missing_required_parameter: tools[0].name` | Værktøjsdefinition bruger gammelt Chat Completions indlejret format | Flad ud fra `{"type": "function", "function": {"name": ...}}` til `{"type": "function", "name": ..., "parameters": ...}` — navn, beskrivelse, parametre skal være i topniveau |
| `unknown_parameter: input[N].tool_calls` | Multi-turn værktøjsresultater bruger gammelt Chat Completions format | Erstat `{"role": "assistant", "tool_calls": [...]}` + `{"role": "tool", ...}` med `response.output` elementer + `{"type": "function_call_output", "call_id": ..., "output": ...}` |
| `invalid_function_parameters: 'required' is required` | `strict: true` værktøj mangler `required` array | Når `strict: true`, skal alle egenskaber listes i `required` og `additionalProperties: false` skal sættes |
| `invalid_function_parameters: 'additionalProperties' is required` | `strict: true` værktøj mangler `additionalProperties: false` | Tilføj `"additionalProperties": false` til parameterobjektet |
| `invalid input[N].id: Expected an ID that begins with 'fc'` | Few-shot function_call ID har forkert præfiks | Function call IDs skal starte med `fc_` (f.eks. `fc_example1`), ikke `call_` |
| `missing_required_parameter: text.format.name` | Tilføj `"name"` nøgle til format dict (f.eks. `"name": "Output"`) |
| `invalid_type: text.format` | Sørg for at `text.format` er en dict med `type`, `name`, `strict`, `schema` nøgler — ikke en streng |
| `invalid input content type` | Brug `input_text`/`output_text` indholdstyper i stedet for Chat `text` |
| `invalid input content type` (billede) | Billedindhold bruger stadig `"type": "image_url"` | Skift til `"type": "input_image"` |
| `Expected object, got string` på `image_url` | `image_url` er stadig et indlejret objekt `{"url": "..."}` | Flad ud til en almindelig streng: `"image_url": "https://..."` eller `"image_url": "data:image/...;base64,..."` |
| `integer below minimum value` for `max_output_tokens` | Minimum er **16** på Azure OpenAI. Brug 50+ til tests, 1000+ til produktion. |
| `429 Too Many Requests` under streaming | Ratebegrænset. Pak streaming i `try/except`, send fejl-JSON til frontend, implementer backoff/genforsøg. |
| `KeyError: 'innererror'` ved content filter fejl | Content filter fejl kropsstruktur ændret i Responses API | Chat Completions brugte `error.body["innererror"]["content_filter_result"]`; Responses API bruger `error.body["content_filters"][0]["content_filter_results"]` (flertal, inde i en array). Omskriv alle `innererror` adgang. |

---

## Risiko-tabel for Migration

| Symptom | Sandsynlig Fejl | Løsning |
|---------|---------------|-----|
| Tom `output_text` / afkortet respons | `max_output_tokens` for lav for ræsonnerende modeller | Sæt `max_output_tokens=1000` eller højere — ræsonnementstokens tæller mod grænsen |
| `400 invalid_type: text.format` | Sendt `response_format` streng i stedet for `text.format` dict | Brug `text={"format": {"type": "json_schema", "name": "...", "strict": True, "schema": {...}}}` |
| `404 Not Found` på `/openai/v1/responses` | Forkert `base_url` — mangler `/openai/v1/` suffix | Sørg for `base_url=f"{endpoint}/openai/v1/"` (med skråstreg til sidst) |
| `401 Unauthorized` efter skift til `OpenAI()` | `api_key` ikke sat eller token provider ikke korrekt givet | For EntraID: `api_key=token_provider` (den callable). For API nøgle: `api_key=os.environ["AZURE_OPENAI_API_KEY"]` |
| Model returnerer `deployment not found` | `model` parameter matcher ikke dit Azure deployment navn | Brug `model=os.environ["AZURE_OPENAI_DEPLOYMENT"]` — dette er deploymentsnavnet, ikke modelnavnet |
| `json.loads(resp.output_text)` kaster `JSONDecodeError` | Skema ikke håndhævet eller model understøtter ikke strikt JSON | Sørg for `"strict": True` i skema, og verificer at model understøtter struktureret output |
| Streaming returnerer ingen `delta` events | Tjekker forkert event type | Filtrer på `event.type == "response.output_text.delta"`, ikke Chats `chat.completion.chunk` |
| `400` fejl på billede input efter migration | Billedindholdstype ikke opdateret | Skift `"type": "image_url"` → `"type": "input_image"` og flad ud `"image_url": {"url": "..."}` → `"image_url": "..."` (almindelig streng) |
| Værktøjskald kører i uendelig løkke | Mangler værktøjsresultat i opfølgende `input` | Efter eksekvering af værktøj, tilføj en `{"type": "function_call_output", "call_id": ..., "output": ...}` post til `input` i næste request |
| `temperature` fejl med GPT-5 eller o-serie | Eksplícit `temperature` værdi andet end 1 | Fjern `temperature` eller sæt til `1` for GPT-5 og o-serie modeller (o1, o3-mini, o3, o4-mini) |
| `top_p` fejl med o-serie | `top_p` ikke understøttet | Fjern `top_p` når du sigter på o-serie modeller |
| `max_completion_tokens` ikke genkendt | Brug af Azure-specifik parameter | Erstat `max_completion_tokens` med `max_output_tokens`. Sæt til 4096+ for o-serie (ræsonnementstokens tæller mod grænsen). |
| Tomt/afkortet output fra o-serie | `max_output_tokens` for lav | O-serie bruger ræsonnementstokens internt. Sæt `max_output_tokens=4096` eller højere — ikke 500–1000. |
| `400 integer_below_min_value` for `max_output_tokens` | Værdi under 16 | Azure OpenAI håndhæver `max_output_tokens >= 16`. Brug 50+ til tests, 1000+ til produktion. |
| `429 Too Many Requests` midt i stream | Ratebegrænset af Azure OpenAI | Stream brydes stille uden fejlbehandling. Pak altid `async for event in await coroutine:` i `try/except` og send `{"error": str(e)}` til frontend. |
| `AzureDeveloperCliCredential` → `CredentialUnavailableError` | Forkert tenant eller ikke logget ind | Giv `tenant_id=os.getenv("AZURE_TENANT_ID")` eksplicit. Kør `azd auth login --tenant <tenant-id>` lokalt. |
| `404 Not Found` med GitHub Models (`models.github.ai`) | GitHub Models understøtter ikke Responses API | Fjern GitHub Models kodevej helt. Brug Azure OpenAI, OpenAI eller en kompatibel lokal endpoint (f.eks. Ollama med Responses support). |
| MAF `OpenAIChatCompletionClient` bruger stadig Chat Completions | Brug af legacy MAF client i 1.0.0+ | I MAF 1.0.0+, bruger `OpenAIChatClient` Responses API som standard. Udskift `OpenAIChatCompletionClient` med `OpenAIChatClient`. For pre-1.0.0, opgrader til `agent-framework-openai>=1.0.0`. |
| LangChain agent returnerer tomt eller fejler ved værktøjskald | `ChatOpenAI` bruger ikke Responses API | Tilføj `use_responses_api=True` til `ChatOpenAI(...)`. Skift også `.content` → `.text` på respons beskeder. |
| `KeyError: 'innererror'` i content filter fejlhandler | Fejl kropsstruktur ændret i Responses API | Omskriv `error.body["innererror"]["content_filter_result"]["jailbreak"]` → `error.body["content_filters"][0]["content_filter_results"]["jailbreak"]`. `innererror` wrapperen er væk; content filter detaljer er nu i topniveau `content_filters` array med `content_filter_results` (flertal) inde i hver post. |
| Råt HTTP kald til `/openai/deployments/.../chat/completions` returnerer 404 | Gammel Chat Completions REST endpoint | Omskriv URL til `/openai/v1/responses`. Skift request body: `messages` → `input`, tilføj `max_output_tokens` + `store: false`, fjern `api-version` query param. Skift respons parsing: `choices[0].message.content` → `output[0].content[0].text` (bemærk: `output_text` er en SDK convenience egenskab, ikke i rå REST JSON). |

---

## Faldgruber

1. Hvis du tidligere brugte Chat Completions til samtalestatus, styr din egen status eksplicit med Responses.
2. Foretræk `max_output_tokens` over gammeldags `max_tokens`.
3. Ved migration til `gpt-5`, sørg for at `temperature` ikke er angivet eller er sat til `1`.
4. Erstat Chat `content[].type: "text"` med Responses `content[].type: "input_text"` for bruger/system input.
5. For `text.format`, angiv en korrekt dict (f.eks. `{"type": "json_schema", "name": "Output", "schema": ..., "strict": True}`), ikke en almindelig streng.
6. `seed` parameter understøttes ikke i Responses; fjern den fra requests.
7. **Ræsonnement**: Inkluder kun `reasoning` hvis den oprindelige kode allerede brugte det. Tilføj ikke `reasoning` til API kald, der ikke havde det — mange ikke-ræsonnerende modeller understøtter ikke denne parameter.
8. **`max_output_tokens` størrelse**: For ræsonnerende modeller (GPT-5-mini, GPT-5, o-serie), brug `max_output_tokens=4096` eller højere — ikke 50–1000. Modellen bruger ræsonnementstokens internt før synligt output; for lave grænser giver afkortede eller tomme svar.
9. **O-serie `max_completion_tokens`**: Hvis den oprindelige kode brugte `max_completion_tokens` (Azure-specifikt for o-serie), erstat med `max_output_tokens`. Responses API accepterer ikke `max_completion_tokens`.
10. **O-serie `reasoning_effort`**: Hvis den oprindelige kode bruger `reasoning_effort` (lav/mellem/høj), migrer det til `reasoning={"effort": "<værdi>"}` i Responses API kald.
11. **O-serie streaming forsinkelse**: O-serie modeller udfører internt ræsonnement før output genereres. Ved streaming forvent en længere forsinkelse før første `response.output_text.delta` event. Dette er normalt — modellen ræsonnerer, ikke frøs.
9. **`_azure_ad_token_provider` er væk**: `AsyncOpenAI` / `OpenAI` har ikke `_azure_ad_token_provider` attribut. Tests eller kode, der tilgår denne attribut, fejler med `AttributeError`. Token provideren gives som `api_key` og er ikke inspicerbar på klientobjektet.
10. **Snapshot / guldfiler**: Hvis testsuiten bruger snapshot tests, skal **alle** snapshot filer med Chat Completions streaming strukturer (`choices[0]`, `content_filter_results`, `function_call`, etc.) opdateres til det nye Responses format. Dette er let at overse og forårsager snapshot assertionsfejl.
11. **Mock monkeypatch sti**: Monkeypatch målet ændres fra `openai.resources.chat.AsyncCompletions.create` → `openai.resources.responses.AsyncResponses.create` (eller `Responses.create` for sync). Brug af gammel sti gør ingenting — mock fanger ikke, og tests rammer den ægte API eller fejler.
12. **`input` ikke `messages`**: Mock funktioner skal læse `kwargs.get("input")` ikke `kwargs.get("messages")`. Responses API bruger `input` til samtalehistorik.
13. **Miljøvariabel navngivning**: Azure Identity SDK bruger `AZURE_CLIENT_ID` (ikke `AZURE_OPENAI_CLIENT_ID`) til `ManagedIdentityCredential(client_id=...)`. Omdøb i tests, `.env` filer, app settings og Bicep/infrastruktur.
14. **`max_output_tokens` minimum er 16**: Azure OpenAI afviser værdier under 16 med `400 integer_below_min_value`. Brug `50` til tests, `1000`+ til produktion. Det gamle `max_tokens` havde ikke dette minimum.
15. **`tenant_id` for `AzureDeveloperCliCredential`**: Når Azure OpenAI ressourcen er i en anden tenant, skal du **eksplicit** angive `tenant_id` — `AzureDeveloperCliCredential(tenant_id=os.getenv("AZURE_TENANT_ID"))`. Uden det bruger credential tyst forkert tenant og returnerer `401`.
16. **Ratebegrænsninger optræder anderledes ved streaming**: Med Chat Completions forhindrede en 429 normalt at streamen startede. Med Responses API streaming kan en 429 opstå **midt i streamen** — den async iterator kaster en undtagelse. Pak altid streaming løkken i `try/except` og returnér en fejl-JSON linje så frontend kan håndtere det pænt.

17. **Streaming-fejlbehandling er obligatorisk for webapps**: Mønstret `try: async for event in await coroutine: ... except Exception as e: yield json.dumps({"error": str(e)})` er kritisk. Uden det dør SSE/JSONL-streamen lydløst ved enhver server-side fejl, og frontend hænger.
18. **Værktøjsdefinitioner skal bruge flad format**: Responses API forventer `{"type": "function", "name": ..., "parameters": ...}` — ikke den Chat Completions indlejrede `{"type": "function", "function": {"name": ..., "parameters": ...}}`. Dette er den mest almindelige migrationsfejl for funktion-kaldende kode.
19. **`pydantic_function_tool()` er inkompatibel**: `openai.pydantic_function_tool()` hjælperen genererer stadig det gamle indlejrede format. Brug det ikke sammen med `responses.create()`. Definer værktøjs skemaer manuelt eller fladgør outputtet.
20. **Værktøjsresultater bruger `function_call_output`, ikke `role: tool`**: Efter udførelse af et værktøj, tilføj `{"type": "function_call_output", "call_id": ..., "output": ...}` — ikke `{"role": "tool", "tool_call_id": ..., "content": ...}`. For assistentens værktøjsanmodning brug `messages.extend(response.output)` — ikke en manuel `{"role": "assistant", "tool_calls": [...]}` dict.
21. **`strict: true` kræver `required` + `additionalProperties: false`**: Når du bruger `strict: true` på et værktøj, skal hver egenskab være opført i `required` arrayet, og `additionalProperties` skal være `false`. Mangler enten forårsager en 400-fejl.
22. **Funktionskald ID’er har specifikke præfikser**: Ved få-skud `function_call` elementer i `input`, skal `id` feltet starte med `fc_` og `call_id` feltet starte med `call_` (fx `"id": "fc_example1", "call_id": "call_example1"`). Brug af det gamle Chat Completions `call_` præfiks til `id` afvises.
23. **GitHub Models understøtter ikke Responses API**: Hvis appen har en GitHub Models kodevej (`base_url` peger på `models.github.ai` eller `models.inference.ai.azure.com`), skal den fjernes helt. Der findes ingen migrationssti — skift til Azure OpenAI, OpenAI eller et kompatibelt lokalt endpoint.
24. **Strukturen for fejl i indholdsfilteret er ændret**: Chat Completions fejl brugte `error.body["innererror"]["content_filter_result"]` (ental). Responses API fejl bruger `error.body["content_filters"][0]["content_filter_results"]` (flertal, inde i en liste). `innererror` nøglen findes ikke længere. Kode der direkte tilgår `innererror` vil kaste `KeyError` ved kørsel — dette er let at overse ved migration, da det kun opstår når indholdsfilteret faktisk aktiveres. Søg altid efter `innererror` under migration.
25. **Rå HTTP-kald kræver URL + body omskrivning**: Apps der kalder Azure OpenAI REST direkte (via `requests`, `httpx`, `aiohttp`) med `/openai/deployments/{name}/chat/completions?api-version=...` skal skifte til `/openai/v1/responses`. Anmodningsbody bruger `input` i stedet for `messages`, kræver `max_output_tokens` og `store`, og `api-version` query-parametret fjernes. Responsbody tekst findes i `output[0].content[0].text` — **ikke** `output_text`, som er en SDK bekvemmelighedsegenskab, der ikke findes i rå REST JSON.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfraskrivelse**:
Dette dokument er blevet oversat ved hjælp af AI-oversættelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selvom vi bestræber os på nøjagtighed, skal du være opmærksom på, at automatiserede oversættelser kan indeholde fejl eller unøjagtigheder. Det originale dokument på dets oprindelige sprog bør betragtes som den autoritative kilde. For kritisk information anbefales professionel menneskelig oversættelse. Vi påtager os intet ansvar for misforståelser eller fejltolkninger, der opstår som følge af brugen af denne oversættelse.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->