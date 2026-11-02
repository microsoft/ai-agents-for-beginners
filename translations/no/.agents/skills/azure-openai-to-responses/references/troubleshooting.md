# Feilsøking, Risikotabell & Fallgruver

## Feilsøking 400-serien

| Feil | Løsning |
|-------|-----|
| `missing_required_parameter: tools[0].name` | Verktøydefinisjon bruker gammelt Chat Completions nestet format | Flatt ut fra `{"type": "function", "function": {"name": ...}}` til `{"type": "function", "name": ..., "parameters": ...}` — navn, beskrivelse, parametre går på toppnivå |
| `unknown_parameter: input[N].tool_calls` | Multiturn verktøyresultater bruker gammelt Chat Completions-format | Bytt ut `{"role": "assistant", "tool_calls": [...]}` + `{"role": "tool", ...}` med `response.output`-elementer + `{"type": "function_call_output", "call_id": ..., "output": ...}` |
| `invalid_function_parameters: 'required' is required` | `strict: true` verktøy mangler `required` array | Når `strict: true`, må alle egenskaper listes i `required` og `additionalProperties: false` må settes |
| `invalid_function_parameters: 'additionalProperties' is required` | `strict: true` verktøy mangler `additionalProperties: false` | Legg til `"additionalProperties": false` i parameterobjektet |
| `invalid input[N].id: Expected an ID that begins with 'fc'` | Few-shot function_call ID har feil prefiks | Funksjonskall-IDer må starte med `fc_` (f.eks. `fc_example1`), ikke `call_` |
| `missing_required_parameter: text.format.name` | Legg til `"name"` nøkkel i format-ordboken (f.eks. `"name": "Output"`) |
| `invalid_type: text.format` | Sørg for at `text.format` er en ordbok med nøklene `type`, `name`, `strict`, `schema` — ikke en streng |
| `invalid input content type` | Bruk `input_text`/`output_text` innholdstyper i stedet for Chat `text` |
| `invalid input content type` (bilde) | Bildinnhold bruker fortsatt `"type": "image_url"` | Endre til `"type": "input_image"` |
| `Expected object, got string` på `image_url` | `image_url` er fortsatt et nestet objekt `{"url": "..."}` | Flatt ut til en vanlig streng: `"image_url": "https://..."` eller `"image_url": "data:image/...;base64,..."` |
| `integer below minimum value` for `max_output_tokens` | Minimum er **16** på Azure OpenAI. Bruk 50+ for testing, 1000+ for produksjon. |
| `429 Too Many Requests` under strømmetesting | Ratebegrenset. Pakk streaming i `try/except`, gi feil-JSON til frontend, implementer backoff/retry. |
| `KeyError: 'innererror'` på innholdsfilter-feil | Struktur på innholdsfilter-feil endret i Responses API | Chat Completions brukte `error.body["innererror"]["content_filter_result"]`; Responses API bruker `error.body["content_filters"][0]["content_filter_results"]` (flertall, inne i array). Omskriv all `innererror`-tilgang. |

---

## Migrasjonsrisikotabell

| Symptom | Sannsynlig feil | Løsning |
|---------|---------------|-----|
| Tom `output_text` / avkortet respons | `max_output_tokens` for lav for resonneringsmodeller | Sett `max_output_tokens=1000` eller høyere — resonningstokens teller mot grensen |
| `400 invalid_type: text.format` | Sendte `response_format` streng i stedet for `text.format` ordbok | Bruk `text={"format": {"type": "json_schema", "name": "...", "strict": True, "schema": {...}}}` |
| `404 Not Found` på `/openai/v1/responses` | Feil `base_url` — mangler `/openai/v1/` suffix | Sørg for `base_url=f"{endpoint}/openai/v1/"` (med skråstrek bak) |
| `401 Unauthorized` etter bytte til `OpenAI()` | `api_key` ikke satt eller token-leverandør sendt feil | For EntraID: `api_key=token_provider` (callable). For API-nøkkel: `api_key=os.environ["AZURE_OPENAI_API_KEY"]` |
| Modell returnerer `deployment not found` | `model`-parameter passer ikke til Azure-distribusjonsnavnet | Bruk `model=os.environ["AZURE_OPENAI_DEPLOYMENT"]` — dette er distribusjonsnavnet, ikke modellnavnet |
| `json.loads(resp.output_text)` kaster `JSONDecodeError` | Skjema blir ikke håndhevet eller modellen støtter ikke streng JSON | Sørg for `"strict": True` i skjema og verifiser modell støtter strukturert utdata |
| Streaming gir ingen `delta`-hendelser | Sjekker feil hendelsestype | Filtrer på `event.type == "response.output_text.delta"`, ikke Chats `chat.completion.chunk` |
| `400`-feil på bildeinput etter migrasjon | Bildets innholdstype ikke oppdatert | Endre `"type": "image_url"` → `"type": "input_image"` og flatt ut `"image_url": {"url": "..."}` → `"image_url": "..."` (vanlig streng) |
| Verktøysamtaler løper i uendelig sløyfe | Mangler verktøyresultat i etterfølgende `input` | Etter kjøring av et verktøy, legg til et `{"type": "function_call_output", "call_id": ..., "output": ...}` element i `input` i neste forespørsel |
| `temperature`-feil med GPT-5 eller o-serien | Eksplisitt `temperature`-verdi ulik 1 | Fjern `temperature` eller sett til `1` for GPT-5 og o-serie modeller (o1, o3-mini, o3, o4-mini) |
| `top_p`-feil med o-serien | `top_p` støttes ikke | Fjern `top_p` når du retter mot o-serie modeller |
| `max_completion_tokens` ikke gjenkjent | Bruker Azure-spesifikk parameter | Erstatt `max_completion_tokens` med `max_output_tokens`. Sett til 4096+ for o-serien (resonneringstokens teller mot begrensningen). |
| Tom/avkortet utdata fra o-serien | `max_output_tokens` for lav | O-serien bruker resonningstokens internt. Sett `max_output_tokens=4096` eller høyere — ikke 500–1000. |
| `400 integer_below_min_value` for `max_output_tokens` | Verdi under 16 | Azure OpenAI håndhever `max_output_tokens >= 16`. Bruk 50+ for røyktester, 1000+ for produksjon. |
| `429 Too Many Requests` midt i streaming | Ratebegrenset av Azure OpenAI | Streamen brytes stille uten feilhåndtering. Pakk alltid `async for event in await coroutine:` i `try/except` og gi `{"error": str(e)}` til frontend. |
| `AzureDeveloperCliCredential` → `CredentialUnavailableError` | Feil tenant eller ikke innlogget | Send `tenant_id=os.getenv("AZURE_TENANT_ID")` eksplisitt. Kjør `azd auth login --tenant <tenant-id>` lokalt. |
| `404 Not Found` med GitHub Models (`models.github.ai`) | GitHub Models støtter ikke Responses API | Fjern GitHub Models-kodeveien helt. Bruk Azure OpenAI, OpenAI, eller en kompatibel lokal endepunkt (f.eks. Ollama med Responses-støtte). |
| MAF `OpenAIChatCompletionClient` bruker fortsatt Chat Completions | Bruker legacy MAF-klient i 1.0.0+ | I MAF 1.0.0+ bruker `OpenAIChatClient` Responses API som standard. Bytt `OpenAIChatCompletionClient` med `OpenAIChatClient`. For pre-1.0.0, oppgrader til `agent-framework-openai>=1.0.0`. |
| LangChain-agent returnerer tomt eller feiler med verktøysamtaler | `ChatOpenAI` bruker ikke Responses API | Legg til `use_responses_api=True` i `ChatOpenAI(...)`. Endre også `.content` → `.text` på responsmeldinger. |
| `KeyError: 'innererror'` i innholdsfilter-feilhåndterer | Feilstrukturen endret i Responses API | Omskriv `error.body["innererror"]["content_filter_result"]["jailbreak"]` → `error.body["content_filters"][0]["content_filter_results"]["jailbreak"]`. `innererror`-wrapper er borte; detaljer for innholdsfilter finnes nå i en toppnivås `content_filters`-array med `content_filter_results` (flertall) inni hver oppføring. |
| Rå HTTP-kall til `/openai/deployments/.../chat/completions` returnerer 404 | Gammelt Chat Completions REST-endepunkt | Omskriv URL til `/openai/v1/responses`. Endre forespørselsbody: `messages` → `input`, legg til `max_output_tokens` + `store: false`, fjern `api-version` query parameter. Endre respons-parsing: `choices[0].message.content` → `output[0].content[0].text` (merk: `output_text` er en SDK-hjelpemetode, ikke i rå REST JSON). |

---

## Fallgruver

1. Hvis du tidligere brukte Chat Completions for samtalestatus, må du håndtere din egen status eksplisitt med Responses.
2. Foretrekk `max_output_tokens` fremfor legacy `max_tokens`.
3. Når du migrerer til `gpt-5`, sørg for at `temperature` ikke er spesifisert eller er satt til `1`.
4. Erstatt Chat `content[].type: "text"` med Responses `content[].type: "input_text"` for bruker-/systeminput.
5. For `text.format`, oppgi en gyldig ordbok (f.eks. `{"type": "json_schema", "name": "Output", "schema": ..., "strict": True}`), ikke en enkel streng.
6. `seed`-parameteren støttes ikke i Responses; fjern den fra forespørsler.
7. **Resonnering**: Inkluder kun `reasoning` hvis den opprinnelige koden allerede brukte det. Ikke legg til `reasoning` i API-kall som ikke hadde det — mange ikke-resonneringsmodeller støtter ikke denne parameteren.
8. **`max_output_tokens` størrelse**: For resonneringsmodeller (GPT-5-mini, GPT-5, o-serien), bruk `max_output_tokens=4096` eller høyere — ikke 50–1000. Modellen bruker resonningstokens internt før synlig utdata; for lave grenser gir avkortede eller tomme svar.
9. **O-serien `max_completion_tokens`**: Om opprinnelig kode brukte `max_completion_tokens` (Azure-spesifikk for o-serien), bytt til `max_output_tokens`. Responses API aksepterer ikke `max_completion_tokens`.
10. **O-serien `reasoning_effort`**: Om opprinnelig kode bruker `reasoning_effort` (lav/middels/høy), migrer til `reasoning={"effort": "<verdi>"}` i Responses API-kallet.
11. **O-serien streamingforsinkelse**: O-seriemodeller utfører intern resonnering før de genererer utdata. Ved streaming, forvent en lengre forsinkelse før første `response.output_text.delta`-hendelse. Dette er normalt — modellen resonnerer, den har ikke hengt seg opp.
9. **`_azure_ad_token_provider` er borte**: `AsyncOpenAI` / `OpenAI` har ikke `_azure_ad_token_provider`-attributt. Tester eller kode som bruker dette vil feile med `AttributeError`. Token-leverandøren sendes som `api_key` og kan ikke inspiseres på klientobjektet.
10. **Snapshot / gullfiler**: Hvis testsettet bruker snapshot-testing, må **alle** snapshot-filer som inneholder Chat Completions streaming-struktur (`choices[0]`, `content_filter_results`, `function_call`, osv.) oppdateres til ny Responses-struktur. Dette er lett å overse og gir snapshot-assert-feil.
11. **Mock monkeypatch-sti**: Monkeypatch-målet endres fra `openai.resources.chat.AsyncCompletions.create` → `openai.resources.responses.AsyncResponses.create` (eller `Responses.create` for synkront). Bruk av gammel sti gjør ingenting stille — mocken griper ikke inn, og tester treffer ekte API eller feiler.
12. **`input` ikke `messages`**: Mock-funksjoner må lese `kwargs.get("input")`, ikke `kwargs.get("messages")`. Responses API bruker `input` for samtalehistorikk.
13. **Miljøvariabelnavn**: Azure Identity SDK bruker `AZURE_CLIENT_ID` (ikke `AZURE_OPENAI_CLIENT_ID`) for `ManagedIdentityCredential(client_id=...)`. Endre navn i tester, `.env`-filer, app-innstillinger og Bicep/infrastruktur.
14. **`max_output_tokens` minimum er 16**: Azure OpenAI avviser verdier under 16 med `400 integer_below_min_value`. Bruk `50` for røyktester, `1000`+ for produksjon. Den gamle `max_tokens` hadde ikke slik minimum.
15. **`tenant_id` for `AzureDeveloperCliCredential`**: Når Azure OpenAI-ressursen er i en annen tenant, må du **alltid** sende `tenant_id` eksplisitt — `AzureDeveloperCliCredential(tenant_id=os.getenv("AZURE_TENANT_ID"))`. Uten dette bruker legitimasjonen stille feil tenant og returnerer `401`.
16. **Ratebegrensninger opptrer annerledes i streaming**: Med Chat Completions hindret 429 som regel at streamen startet. Med Responses API streaming kan 429 oppstå **midt i strømmen** — den asynkrone iteratoren kaster unntak. Pakk alltid streaming-løkken i `try/except` og gi en feil-JSON-linje slik at frontend kan håndtere det pent.

17. **Streaming feilhåndtering er obligatorisk for nettapper**: Mønsteret `try: async for event in await coroutine: ... except Exception as e: yield json.dumps({"error": str(e)})` er kritisk. Uten det dør SSE/JSONL-strømmen stille ved enhver serverfeil og frontenden henger seg opp.
18. **Verktøydefinisjoner må bruke flat format**: Responses API forventer `{"type": "function", "name": ..., "parameters": ...}` — ikke den nestede Chat Completions `{"type": "function", "function": {"name": ..., "parameters": ...}}`. Dette er den vanligste migrasjonsfeilen for funksjonskallende kode.
19. **`pydantic_function_tool()` er inkompatibel**: Hjelperen `openai.pydantic_function_tool()` genererer fortsatt det gamle nestede formatet. Ikke bruk den med `responses.create()`. Definer verktøyskjemaer manuelt eller flate ut utskriften.
20. **Verktøyresultater bruker `function_call_output`, ikke `role: tool`**: Etter å ha utført et verktøy, legg til `{"type": "function_call_output", "call_id": ..., "output": ...}` — ikke `{"role": "tool", "tool_call_id": ..., "content": ...}`. For assistentens verktøyforespørsel, bruk `messages.extend(response.output)` — ikke en manuell `{"role": "assistant", "tool_calls": [...]}`-ordbok.
21. **`strict: true` krever `required` + `additionalProperties: false`**: Når man bruker `strict: true` på et verktøy, må alle egenskaper være oppført i `required`-arrayen og `additionalProperties` må være `false`. Mangler noen av disse gir 400-feil.
22. **Funksjonskall-IDer har spesifikke prefikser**: Når du oppgir få-skudd `function_call`-elementer i `input`, må `id`-feltet begynne med `fc_` og `call_id`-feltet med `call_` (f.eks. `"id": "fc_example1", "call_id": "call_example1"`). Bruk av det gamle Chat Completions `call_`-prefikset for `id` blir avvist.
23. **GitHub Models støtter ikke Responses API**: Hvis appen har en GitHub Models-kodevei (`base_url` som peker til `models.github.ai` eller `models.inference.ai.azure.com`), må den fjernes helt. Det finnes ingen migrasjonsvei — bytt til Azure OpenAI, OpenAI eller en kompatibel lokal endepunkt.
24. **Strukturen på feil for innholdsfilter har endret seg**: Chat Completions-feil brukte `error.body["innererror"]["content_filter_result"]` (entall). Responses API-feil bruker `error.body["content_filters"][0]["content_filter_results"]` (flertall, inne i en liste). Nøkkelen `innererror` eksisterer ikke lenger. Kode som direkte aksesserer `innererror` vil kaste `KeyError` ved kjøring — dette er lett å overse ved migrering siden det bare dukker opp når innholdsfilteret faktisk trigges. Søk alltid etter `innererror` under migrering.
25. **Rå HTTP-kall trenger URL- og kropp-omskriving**: Apper som kaller Azure OpenAI REST direkte (via `requests`, `httpx`, `aiohttp`) med `/openai/deployments/{name}/chat/completions?api-version=...` må bytte til `/openai/v1/responses`. Forespørselskroppen bruker `input` i stedet for `messages`, krever `max_output_tokens` og `store`, og `api-version`-spørringsparameteren droppes. Svarkroppens tekst er på `output[0].content[0].text` — **ikke** `output_text`, som er en SDK bekvemmelighetsegenskap som ikke finnes i den rå REST JSON.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfraskrivelse**:
Dette dokumentet er oversatt ved hjelp av AI-oversettelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selv om vi streber etter nøyaktighet, vær oppmerksom på at automatiske oversettelser kan inneholde feil eller unøyaktigheter. Det opprinnelige dokumentet på originalspråket skal betraktes som den autoritative kilden. For kritisk informasjon anbefales profesjonell menneskelig oversettelse. Vi er ikke ansvarlige for eventuelle misforståelser eller feiltolkninger som oppstår ved bruk av denne oversettelsen.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->