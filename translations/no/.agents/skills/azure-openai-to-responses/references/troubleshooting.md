# Feilsøking, Risikotabell & Fallgruver

## Feilsøking 400-feil

| Feil | Løsning |
|-------|-----|
| `missing_required_parameter: tools[0].name` | Verktøydefinisjonen bruker gammelt innpakket Chat Completions-format | Flatt ut fra `{"type": "function", "function": {"name": ...}}` til `{"type": "function", "name": ..., "parameters": ...}` — name, description, parameters skal opp på toppnivå |
| `unknown_parameter: input[N].tool_calls` | Multi-turn verktøyresultater bruker gammelt Chat Completions-format | Erstatt `{"role": "assistant", "tool_calls": [...]}` + `{"role": "tool", ...}` med `response.output`-elementer + `{"type": "function_call_output", "call_id": ..., "output": ...}` |
| `invalid_function_parameters: 'required' is required` | `strict: true` verktøy mangler `required`-array | Når `strict: true`, må alle egenskaper være oppført i `required` og `additionalProperties: false` må settes |
| `invalid_function_parameters: 'additionalProperties' is required` | `strict: true` verktøy mangler `additionalProperties: false` | Legg til `"additionalProperties": false` i parameterobjektet |
| `invalid input[N].id: Expected an ID that begins with 'fc'` | Few-shot function_call ID har feil prefiks | Funksjonskall-IDer må starte med `fc_` (f.eks. `fc_eksempel1`), ikke `call_` |
| `missing_required_parameter: text.format.name` | Legg til `"name"`-nøkkel i format-diktet (f.eks. `"name": "Output"`) |
| `invalid_type: text.format` | Sørg for at `text.format` er et dikt med nøklene `type`, `name`, `strict`, `schema` — ikke en streng |
| `invalid input content type` | Bruk `input_text`/`output_text` innholdstyper i stedet for Chat `text` |
| `invalid input content type` (bilde) | Bildeinnhold bruker fortsatt `"type": "image_url"` | Endre til `"type": "input_image"` |
| `Expected object, got string` på `image_url` | `image_url` er fortsatt et innpakket objekt `{"url": "..."}` | Flatt ut til en vanlig streng: `"image_url": "https://..."` eller `"image_url": "data:image/...;base64,..."` |
| `integer below minimum value` for `max_output_tokens` | Minimum er **16** på Azure OpenAI. Bruk 50+ for tester, 1000+ for produksjon. |
| `429 Too Many Requests` under streaming | Ratebegrenset. Pakk streaming i `try/except`, lever feilen som JSON til frontend, implementer tilbakekobling/nytt forsøk. |
| `KeyError: 'innererror'` ved innholdsfilter-feil | Struktur på feilmelding endret i Responses API | Chat Completions brukte `error.body["innererror"]["content_filter_result"]`; Responses API bruker `error.body["content_filters"][0]["content_filter_results"]` (flertall, i en matrise). Omskriv all tilgang til `innererror`. |

---

## Migrasjonsrisikotabell

| Symptom | Sannsynlig Feil | Løsning |
|---------|---------------|-----|
| Tomt `output_text` / avkortet svar | `max_output_tokens` for lav for resonneringsmodeller | Sett `max_output_tokens=1000` eller høyere — resonneringstokener teller mot grensen |
| `400 invalid_type: text.format` | Sendt `response_format` streng i stedet for `text.format` dikt | Bruk `text={"format": {"type": "json_schema", "name": "...", "strict": True, "schema": {...}}}` |
| `404 Not Found` på `/openai/v1/responses` | Feil `base_url` — mangler `/openai/v1/` suffix | Sørg for `base_url=f"{endpoint}/openai/v1/"` (med skråstrek på slutten) |
| `401 Unauthorized` etter bytte til `OpenAI()` | `api_key` ikke satt eller token provider ikke sendt riktig | For EntraID: `api_key=token_provider` (den kallbare). For API-nøkkel: `api_key=os.environ["AZURE_OPENAI_API_KEY"]` |
| Modell returnerer `deployment not found` | `model`-parameter samsvarer ikke med ditt Azure distribusjonsnavn | Bruk `model=os.environ["AZURE_OPENAI_DEPLOYMENT"]` — dette er distribusjonsnavnet, ikke modellnavnet |
| `json.loads(resp.output_text)` gir `JSONDecodeError` | Skjema ikke håndhevet eller modell støtter ikke streng JSON | Sørg for `"strict": True` i skjemaet, og verifiser at modell støtter strukturert output |
| Streaming gir ingen `delta`-hendelser | Sjekker feil hendelsestype | Filtrer på `event.type == "response.output_text.delta"`, ikke Chats `chat.completion.chunk` |
| `400` feil på bildeinput etter migrasjon | Bildeinnholdstype ikke oppdatert | Endre `"type": "image_url"` → `"type": "input_image"` og flatt ut `"image_url": {"url": "..."}` → `"image_url": "..."` (vanlig streng) |
| Verktøykall løkker uendelig | Mangler verktøyresultat i oppfølgende `input` | Etter å ha kjørt et verktøy, legg til et `{"type": "function_call_output", "call_id": ..., "output": ...}`-element i `input` i neste forespørsel |
| `temperature`-feil med GPT-5 eller o-serie | Eksplisitt `temperature`-verdi annen enn 1 | Fjern `temperature` eller sett til `1` for GPT-5 og o-serie modeller (o1, o3-mini, o3, o4-mini) |
| `top_p`-feil med o-serie | `top_p` ikke støttet | Fjern `top_p` når du retter mot o-serie modeller |
| `max_completion_tokens` ikke gjenkjent | Bruker Azure-spesifikk parameter | Erstatt `max_completion_tokens` med `max_output_tokens`. Sett til 4096+ for o-serie (resonneringstokener teller mot grensen). |
| Tomt/avkortet output fra o-serie | `max_output_tokens` for lav | O-serien bruker resonneringstokener internt. Sett `max_output_tokens=4096` eller høyere — ikke 500–1000. |
| `400 integer_below_min_value` for `max_output_tokens` | Verdi under 16 | Azure OpenAI krever `max_output_tokens >= 16`. Bruk 50+ for røyktester, 1000+ for produksjon. |
| `429 Too Many Requests` midt i stream | Ratebegrensning av Azure OpenAI | Stream brytes stille uten feilhåndtering. Pakk alltid `async for event in await coroutine:` i `try/except` og send `{"error": str(e)}` til frontend. |
| `AzureDeveloperCliCredential` → `CredentialUnavailableError` | Feil tenant eller ikke logget inn | Send `tenant_id=os.getenv("AZURE_TENANT_ID")` eksplisitt. Kjør `azd auth login --tenant <tenant-id>` lokalt. |
| `404 Not Found` med GitHub Models (`models.github.ai`) | GitHub Models støtter ikke Responses API | Fjern GitHub Models-kodebanen helt. Bruk Azure OpenAI, OpenAI eller en kompatibel lokal endepunkt (f.eks. Ollama med Responses-støtte). |
| MAF `OpenAIChatCompletionClient` bruker fortsatt Chat Completions | Bruker legacy MAF-klient i 1.0.0+ | I MAF 1.0.0+ bruker `OpenAIChatClient` Responses API som standard. Erstatt `OpenAIChatCompletionClient` med `OpenAIChatClient`. For pre-1.0.0, oppgrader til `agent-framework-openai>=1.0.0`. |
| LangChain agent returnerer tomt eller feiler med verktøykall | `ChatOpenAI` bruker ikke Responses API | Legg til `use_responses_api=True` i `ChatOpenAI(...)`. Endre også `.content` → `.text` på responsmeldinger. |
| `KeyError: 'innererror'` i innholdsfilter-feilhåndtering | Feilmeldingsstruktur endret i Responses API | Omskriv `error.body["innererror"]["content_filter_result"]["jailbreak"]` → `error.body["content_filters"][0]["content_filter_results"]["jailbreak"]`. `innererror`-innpakningen er borte; innholdsfilterdetaljer finnes nå i et toppnivå `content_filters` array med `content_filter_results` (flertall) inni hver post. |
| Rå HTTP-kall til `/openai/deployments/.../chat/completions` gir 404 | Gammelt Chat Completions REST-endepunkt | Omskriv URL til `/openai/v1/responses`. Endre forespørselskropp: `messages` → `input`, legg til `max_output_tokens` + `store: false`, fjern `api-version` query param. Endre responsparsing: `choices[0].message.content` → `output[0].content[0].text` (merk: `output_text` er en SDK-hjelpeegenskap, ikke i rå REST JSON). |

---

## Fallgruver

1. Hvis du tidligere brukte Chat Completions til samtalestatus, må du selv håndtere tilstanden eksplisitt med Responses.
2. Bruk heller `max_output_tokens` enn det gamle `max_tokens`.
3. Ved migrering til `gpt-5`, sørg for at `temperature` ikke er spesifisert eller er satt til `1`.
4. Erstatt Chat `content[].type: "text"` med Responses `content[].type: "input_text"` for bruker-/system-input.
5. For `text.format`, lever et gyldig dikt (f.eks. `{"type": "json_schema", "name": "Output", "schema": ..., "strict": True}`), ikke en vanlig streng.
6. `seed`-parameteren støttes ikke i Responses; fjern den fra forespørsler.
7. **Resonnering**: Inkluder bare `reasoning` hvis originalkoden allerede brukte det. Ikke legg til `reasoning` i API-kall som ikke hadde det — mange modeller (f.eks. gpt-4o-mini) støtter ikke denne parameteren.
8. **Størrelse på `max_output_tokens`**: For resonneringsmodeller (GPT-5-mini, GPT-5, o-serie), bruk `max_output_tokens=4096` eller høyere — ikke 50–1000. Modellen bruker resonneringstokener internt før den lager synlig output; for lave grenser gir avkortede eller tomme svar.
9. **O-serie `max_completion_tokens`**: Hvis originalkoden brukte `max_completion_tokens` (Azure-spesifikk for o-serien), erstatt med `max_output_tokens`. Responses API godtar ikke `max_completion_tokens`.
10. **O-serie `reasoning_effort`**: Hvis originalkoden bruker `reasoning_effort` (lav/middels/høy), migrer til `reasoning={"effort": "<verdi>"}` i Responses API-kallet.
11. **O-serie streamingforsinkelse**: O-serie modeller gjør intern resonnering før output-generering. Ved streaming forventes en lengre forsinkelse før første `response.output_text.delta`-hendelse. Dette er normalt — modellen resonnerer, ikke henger.
9. **`_azure_ad_token_provider` er borte**: `AsyncOpenAI` / `OpenAI` har ikke `_azure_ad_token_provider`-attributt. Tester eller kode som prøver å hente dette vil feile med `AttributeError`. Token provider sendes som `api_key` og kan ikke inspiseres på klientobjektet.
10. **Snapshot / golden files**: Hvis testpakken bruker snapshot-testing, må **alle** snapshot-filer som inneholder Chat Completions streamingstruktur (`choices[0]`, `content_filter_results`, `function_call`, osv.) oppdateres til den nye Responses-strukturen. Dette er lett å overse og forårsaker snapshot-feil.
11. **Mock monkeypatch-path**: Monkeypatch-målet endres fra `openai.resources.chat.AsyncCompletions.create` → `openai.resources.responses.AsyncResponses.create` (eller `Responses.create` for synkront). Bruk av gammel sti gjør ingenting stille — mocken fanger ikke opp, og tester går mot ekte API eller feiler.
12. **`input` ikke `messages`**: Mock-funksjoner må lese `kwargs.get("input")` ikke `kwargs.get("messages")`. Responses API bruker `input` for samtalehistorikk.
13. **Miljøvariabelnavn**: Azure Identity SDK bruker `AZURE_CLIENT_ID` (ikke `AZURE_OPENAI_CLIENT_ID`) for `ManagedIdentityCredential(client_id=...)`. Endre navn i tester, `.env`-filer, app-innstillinger og Bicep/infrastruktur.
14. **Minste `max_output_tokens` er 16**: Azure OpenAI avviser verdier under 16 med `400 integer_below_min_value`. Bruk `50` for røyktester, `1000`+ for produksjon. Det gamle `max_tokens` hadde ingen slik minstegrense.
15. **`tenant_id` for `AzureDeveloperCliCredential`**: Når Azure OpenAI-ressursen er i en annen tenant, **må** du sende `tenant_id` eksplisitt — `AzureDeveloperCliCredential(tenant_id=os.getenv("AZURE_TENANT_ID"))`. Uten dette bruker legitimasjonen feil tenant stille og returnerer `401`.
16. **Ratebegrensninger opptrer annerledes i streaming**: Med Chat Completions ville en 429 typisk forhindre oppstart av streamen. Med Responses API streaming kan en 429 forekomme **midt i streamen** — den asynkrone iteratoren kaster et unntak. Pakk alltid streaming-løkken i `try/except` og send en feilmelding som JSON-linje så frontend kan håndtere det pent.

17. **Streaming-feilhåndtering er obligatorisk for nettppløsninger**: Mønsteret `try: async for event in await coroutine: ... except Exception as e: yield json.dumps({"error": str(e)})` er kritisk. Uten det dør SSE/JSONL-strømmen stille ved enhver serverfeil, og frontend henger.
18. **Verktøydefinisjoner må bruke flat format**: Responses API forventer `{"type": "function", "name": ..., "parameters": ...}` — ikke den nestede Chat Completions `{"type": "function", "function": {"name": ..., "parameters": ...}}`. Dette er den vanligste migrasjonsfeilen for funksjonskallende kode.
19. **`pydantic_function_tool()` er inkompatibel**: `openai.pydantic_function_tool()`-hjelperen genererer fortsatt det gamle nested formatet. Ikke bruk den med `responses.create()`. Definer verktøyskjemaer manuelt eller flat ut outputen.
20. **Verktøyresultater bruker `function_call_output`, ikke `role: tool`**: Etter å ha kjørt et verktøy, legg til `{"type": "function_call_output", "call_id": ..., "output": ...}` — ikke `{"role": "tool", "tool_call_id": ..., "content": ...}`. For assistentens verktøyforespørsel, bruk `messages.extend(response.output)` — ikke et manuelt `{"role": "assistant", "tool_calls": [...]}`-ordbok.
21. **`strict: true` krever `required` + `additionalProperties: false`**: Når `strict: true` brukes på et verktøy, må alle egenskaper listes i `required`-arrayen, og `additionalProperties` må være `false`. Mangler ett av disse gir 400-feil.
22. **Funksjonskall-IDer har spesifikke prefikser**: Ved få-skudds `function_call`-elementer i `input`, må `id`-feltet starte med `fc_` og `call_id` må starte med `call_` (f.eks. `"id": "fc_example1", "call_id": "call_example1"`). Å bruke det gamle Chat Completions `call_`-prefikset for `id` avvises.
23. **GitHub Models støtter ikke Responses API**: Hvis appen har en GitHub Models-kodebane (`base_url` peker til `models.github.ai` eller `models.inference.ai.azure.com`), fjern den fullstendig. Det finnes ingen migrasjonsvei — bytt til Azure OpenAI, OpenAI eller en kompatibel lokal endepunkt.
24. **Innholdsfiltreringsfeilens kroppstruktur har endret seg**: Chat Completions-feil brukte `error.body["innererror"]["content_filter_result"]` (entall). Responses API-feil bruker `error.body["content_filters"][0]["content_filter_results"]` (flertall, inni en array). `innererror`-nøkkelen finnes ikke lenger. Kode som direkte adresserer `innererror` vil gi `KeyError` ved kjøretid — dette er lett å overse under migrasjon siden det bare oppstår når innholdsfilteret faktisk trigges. Søk alltid etter `innererror` under migrasjon.
25. **Rå HTTP-kall trenger URL + kropps-omskriving**: Apper som kaller Azure OpenAI REST direkte (via `requests`, `httpx`, `aiohttp`) med `/openai/deployments/{name}/chat/completions?api-version=...` må bytte til `/openai/v1/responses`. Forespørselskroppen bruker `input` i stedet for `messages`, krever `max_output_tokens` og `store`, og `api-version`-spørringsparameteren droppes. Responsens kroppstekst ligger i `output[0].content[0].text` — **ikke** `output_text`, som er et SDK-bekvemmelighetsegenskap som ikke finnes i det rå REST JSON.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfraskrivelse**:
Dette dokumentet er oversatt ved hjelp av AI-oversettelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selv om vi streber etter nøyaktighet, vær oppmerksom på at automatiske oversettelser kan inneholde feil eller unøyaktigheter. Det opprinnelige dokumentet på originalspråket skal betraktes som den autoritative kilden. For kritisk informasjon anbefales profesjonell menneskelig oversettelse. Vi er ikke ansvarlige for eventuelle misforståelser eller feiltolkninger som oppstår ved bruk av denne oversettelsen.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->