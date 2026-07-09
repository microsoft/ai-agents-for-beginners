# Depanare, Tabel de risc & Capcane

## Depanare pentru erorile 400

| Eroare | Soluție |
|-------|---------|
| `missing_required_parameter: tools[0].name` | Definiția instrumentului folosește vechiul format imbricat Chat Completions | Se aplatizează de la `{"type": "function", "function": {"name": ...}}` la `{"type": "function", "name": ..., "parameters": ...}` — numele, descrierea, parametrii trebuie la nivel superior |
| `unknown_parameter: input[N].tool_calls` | Rezultatele în mai multe ture ale unui instrument folosesc vechiul format Chat Completions | Se înlocuiește `{"role": "assistant", "tool_calls": [...]}` + `{"role": "tool", ...}` cu elementele din `response.output` + `{"type": "function_call_output", "call_id": ..., "output": ...}` |
| `invalid_function_parameters: 'required' is required` | Instrument cu `strict: true` lipsește array-ul `required` | Când `strict: true`, toate proprietățile trebuie listate în `required` și `additionalProperties: false` trebuie setat |
| `invalid_function_parameters: 'additionalProperties' is required` | Instrument cu `strict: true` lipsește `additionalProperties: false` | Se adaugă `"additionalProperties": false` în obiectul de parametri |
| `invalid input[N].id: Expected an ID that begins with 'fc'` | ID-ul apeluui funcției few-shot are prefix greșit | ID-urile apelului funcției trebuie să înceapă cu `fc_` (ex. `fc_example1`), nu cu `call_` |
| `missing_required_parameter: text.format.name` | Se adaugă cheia `"name"` în dicționarul format (ex. `"name": "Output"`) |
| `invalid_type: text.format` | Asigurați-vă că `text.format` este un dicționar cu cheile `type`, `name`, `strict`, `schema` — nu un string |
| `invalid input content type` | Folosiți tipurile de conținut `input_text`/`output_text` în loc de Chat `text` |
| `invalid input content type` (imagine) | Tipul conținutului imagine folosește încă `"type": "image_url"` | Schimbați în `"type": "input_image"` |
| `Expected object, got string` pe `image_url` | `image_url` este încă un obiect imbricat `{"url": "..."}` | Se aplatizează la un string simplu: `"image_url": "https://..."` sau `"image_url": "data:image/...;base64,..."` |
| `integer below minimum value` pentru `max_output_tokens` | Minim este **16** pe Azure OpenAI. Folosiți 50+ pentru teste, 1000+ pentru producție. |
| `429 Too Many Requests` în timpul streamingului | Limită de rată atinsă. Înfășurați streamingul în `try/except`, returnați JSON-ul erorii către frontend, implementați backoff/retry. |
| `KeyError: 'innererror'` la eroare de filtru conținut | Structura corpului erorii filtru conținut s-a schimbat în Responses API | Chat Completions folosea `error.body["innererror"]["content_filter_result"]`; Responses API folosește `error.body["content_filters"][0]["content_filter_results"]` (plural, într-un array). Rescrieți toate accesările `innererror`. |

---

## Tabel de risc pentru migrare

| Simptom | Greșeală Probabilă | Soluție |
|---------|-------------------|---------|
| `output_text` gol / răspuns trunchiat | `max_output_tokens` prea mic pentru modelele de raționament | Setează `max_output_tokens=1000` sau mai mare — tokenii de raționament contează în limită |
| `400 invalid_type: text.format` | A fost folosit un string `response_format` în loc de dicționar `text.format` | Folosiți `text={"format": {"type": "json_schema", "name": "...", "strict": True, "schema": {...}}}` |
| `404 Not Found` la `/openai/v1/responses` | `base_url` greșit — lipsește sufixul `/openai/v1/` | Asigurați-vă că `base_url=f"{endpoint}/openai/v1/"` (cu slash la final) |
| `401 Unauthorized` după schimbarea la `OpenAI()` | `api_key` ne-setat sau token provider transmis incorect | Pentru EntraID: `api_key=token_provider` (funcția apelabilă). Pentru cheia API: `api_key=os.environ["AZURE_OPENAI_API_KEY"]` |
| Modelul returnează `deployment not found` | Parametrul `model` nu corespunde cu numele desfășurării Azure | Folosiți `model=os.environ["AZURE_OPENAI_DEPLOYMENT"]` — este numele desfășurării, nu modelul |
| `json.loads(resp.output_text)` ridică `JSONDecodeError` | Schema nu este aplicată sau modelul nu suportă JSON strict | Asigurați `"strict": True` în schema și verificați dacă modelul suportă output structurat |
| Streaming-ul nu emite evenimente `delta` | Verificare pe tip eveniment greșit | Filtrați pe `event.type == "response.output_text.delta"`, nu pe `chat.completion.chunk` din Chat |
| Eroare `400` la input imagine după migrare | Tipul conținutului imagine nu a fost actualizat | Schimbați `"type": "image_url"` → `"type": "input_image"` și aplatizați `"image_url": {"url": "..."}` → `"image_url": "..."` (string simplu) |
| Apelurile instrumentului intră în buclă infinită | Lipsește rezultatul instrumentului în următorul `input` | După executarea unui instrument, adăugați un element `{"type": "function_call_output", "call_id": ..., "output": ...}` la `input` în următoarea cerere |
| Eroare la `temperature` cu GPT-5 sau seria o | Valoare explicită `temperature` diferită de 1 | Scoateți `temperature` sau setați la `1` pentru GPT-5 și modelele o-series (o1, o3-mini, o3, o4-mini) |
| Eroare `top_p` cu seria o | `top_p` nu este suportat | Scoateți `top_p` când vizați modelele o-series |
| `max_completion_tokens` nerecunoscut | Folosirea parametrului specific Azure | Înlocuiți `max_completion_tokens` cu `max_output_tokens`. Puneți 4096+ pentru o-series (tokenii de raționament contează) |
| Output gol/trunchiat din o-series | `max_output_tokens` prea mic | O-series folosește intern tokeni de raționament. Folosiți `max_output_tokens=4096` sau mai mult — nu 500–1000 |
| `400 integer_below_min_value` pentru `max_output_tokens` | Valoare sub 16 | Azure OpenAI impune `max_output_tokens >= 16`. Folosiți 50+ pentru teste rapide, 1000+ pentru producție |
| `429 Too Many Requests` în mijlocul streamingului | Limitat de Azure OpenAI | Stream-ul se oprește fără eroare vizibilă dacă nu gestionați. Înfășurați întotdeauna `async for event in await coroutine:` în `try/except` și returnați `{"error": str(e)}` la frontend |
| `AzureDeveloperCliCredential` → `CredentialUnavailableError` | Tenant greșit sau neautentificat | Trebuie să transmiteți explicit `tenant_id=os.getenv("AZURE_TENANT_ID")`. Rulați `azd auth login --tenant <tenant-id>` local |
| `404 Not Found` folosind modelele GitHub (`models.github.ai`) | Modelele GitHub nu suportă API-ul Responses | Scoateți complet calea codului GitHub Models. Folosiți Azure OpenAI, OpenAI, sau un endpoint local compatibil cu Responses (ex. Ollama) |
| MAF `OpenAIChatCompletionClient` încă folosește Chat Completions | Folosirea clientului MAF vechi în 1.0.0+ | În MAF 1.0.0+, `OpenAIChatClient` folosește Responses API implicit. Înlocuiți `OpenAIChatCompletionClient` cu `OpenAIChatClient`. Pentru versiunile pre-1.0.0, faceți upgrade la `agent-framework-openai>=1.0.0` |
| Agent LangChain returnează gol sau eșuează cu apeluri la instrumente | `ChatOpenAI` nu folosește Responses API | Adăugați `use_responses_api=True` la `ChatOpenAI(...)`. De asemenea schimbați `.content` → `.text` pe mesajele răspunsului |
| `KeyError: 'innererror'` în handlerul erorilor filtru conținut | Structura corpului erorii s-a schimbat în Responses API | Rescrieți accesul `error.body["innererror"]["content_filter_result"]["jailbreak"]` → `error.body["content_filters"][0]["content_filter_results"]["jailbreak"]`. Wrapper-ul `innererror` a dispărut; detaliile filtrului sunt acum în array-ul de top-level `content_filters`, fiecare cu `content_filter_results` (plural) |
| Apel HTTP brut la `/openai/deployments/.../chat/completions` întoarce 404 | Endpoint vechi REST Chat Completions | Rescrieți URL-ul pentru `/openai/v1/responses`. Schimbați corpul cererii: `messages` → `input`, adăugați `max_output_tokens` + `store: false`, eliminați query-parametrul `api-version`. Schimbați parsarea răspunsului: `choices[0].message.content` → `output[0].content[0].text` (notă: `output_text` este o proprietate comoditate SDK, nu în JSON-ul brut REST) |

---

## Capcane

1. Dacă foloseați anterior Chat Completions pentru starea conversației, gestionați-vă acum propriul stat explicit cu Responses.
2. Preferabil `max_output_tokens` în locul vechiului `max_tokens`.
3. La migrarea la `gpt-5`, asigurați-vă că nu specificați `temperature` sau este setat la `1`.
4. Înlocuiți Chat `content[].type: "text"` cu Responses `content[].type: "input_text"` pentru inputurile utilizator/sistem.
5. Pentru `text.format`, furnizați un dicționar corect (ex. `{"type": "json_schema", "name": "Output", "schema": ..., "strict": True}`), nu un string simplu.
6. Parametrul `seed` nu e suportat în Responses; scoateți-l din cereri.
7. **Raționament**: Includeți `reasoning` doar dacă codul original îl folosea deja. Nu adăugați `reasoning` la apelurile API care nu-l aveau — multe modele (ex. gpt-4o-mini) nu-l suportă.
8. **Dimensionarea `max_output_tokens`**: Pentru modelele de raționament (GPT-5-mini, GPT-5, o-series), folosiți `max_output_tokens=4096` sau mai mare — nu 50–1000. Modelul folosește intern tokeni pentru raționament înainte de output vizibil; limite prea mici duc la răspunsuri trunchiate sau goale.
9. **`max_completion_tokens` pentru o-series**: Dacă codul original folosea `max_completion_tokens` (Azure-specific pentru o-series), înlocuiți cu `max_output_tokens`. Responses API nu acceptă `max_completion_tokens`.
10. **`reasoning_effort` pentru o-series**: Dacă codul original folosea `reasoning_effort` (low/medium/high), migrați-l la `reasoning={"effort": "<valoare>"}` în apelul Responses API.
11. **Întârzierea streaming-ului la o-series**: Modelele o-series efectuează raționament intern înainte de generarea outputului. La streaming, așteptați o întârziere mai lungă până la primul eveniment `response.output_text.delta`. Este normal — modelul raționează, nu este blocat.
9. **`_azure_ad_token_provider` a dispărut**: `AsyncOpenAI` / `OpenAI` nu mai au atributul `_azure_ad_token_provider`. Testele sau codul care îl folosesc vor eșua cu `AttributeError`. Providerul de tokeni se transmite ca `api_key` și nu este inspectabil pe obiectul client.
10. **Snapshot / fișiere auriu**: Dacă suita de teste folosește testare snapshot, **toate** fișierele snapshot care conțin formele streaming Chat Completions (`choices[0]`, `content_filter_results`, `function_call`, etc.) trebuie actualizate la noua formă Responses. Este ușor de ratat și cauzează eșecuri la aserțiuni snapshot.
11. **Calea pentru mock monkeypatch**: Ținta pentru monkeypatch se schimbă de la `openai.resources.chat.AsyncCompletions.create` → `openai.resources.responses.AsyncResponses.create` (sau `Responses.create` pentru sync). Folosirea vechii căi nu face nimic în mod tăcut — mock-ul nu interceptează, iar testele accesează API-ul real sau eșuează.
12. **`input`, nu `messages`**: Funcțiile mock trebuie să citească `kwargs.get("input")` nu `kwargs.get("messages")`. Responses API folosește `input` pentru istoricul conversației.
13. **Numele variabilelor de mediu**: Azure Identity SDK folosește `AZURE_CLIENT_ID` (nu `AZURE_OPENAI_CLIENT_ID`) pentru `ManagedIdentityCredential(client_id=...)`. Renumiți în teste, fișiere `.env`, setări aplicație și Bicep/infrastructură.
14. **Minimul `max_output_tokens` este 16**: Azure OpenAI respinge valorile sub 16 cu `400 integer_below_min_value`. Folosiți 50 pentru teste rapide, 1000+ pentru producție. Vechiul `max_tokens` nu avea acest minim.
15. **`tenant_id` pentru `AzureDeveloperCliCredential`**: Dacă resursa Azure OpenAI se află într-un tenant diferit, **trebuie** să transmiteți explicit `tenant_id` — `AzureDeveloperCliCredential(tenant_id=os.getenv("AZURE_TENANT_ID"))`. Fără asta, credentialele folosesc tenantul greșit în mod tăcut și întorc `401`.
16. **Limitele de rată apar diferit în streaming**: Cu Chat Completions, un 429 bloca începerea stream-ului. Cu Responses API streaming, un 429 poate apărea **în mijlocul stream-ului** — iteratorul asincron ridică o excepție. Înfășurați întotdeauna bucla de streaming în `try/except` și returnați o linie JSON de eroare ca frontend-ul să o poată gestiona frumos.

17. **Gestionarea erorilor de streaming este obligatorie pentru aplicațiile web**: Modelul `try: async for event in await coroutine: ... except Exception as e: yield json.dumps({"error": str(e)})` este esențial. Fără acesta, fluxul SSE/JSONL moare silențios la orice eroare de pe server și frontend-ul se blochează.
18. **Definițiile instrumentelor trebuie să folosească formatul plat**: API-ul Responses așteaptă `{"type": "function", "name": ..., "parameters": ...}` — nu formatul imbricat de la Chat Completions `{"type": "function", "function": {"name": ..., "parameters": ...}}`. Aceasta este cea mai frecventă eroare de migrare pentru codul care apelează funcții.
19. **`pydantic_function_tool()` este incompatibil**: Helper-ul `openai.pydantic_function_tool()` generează încă vechiul format imbricat. Nu-l folosi împreună cu `responses.create()`. Defineste schemele uneltelor manual sau aplatizează rezultatul.
20. **Rezultatele instrumentelor folosesc `function_call_output`, nu `role: tool`**: După executarea unui instrument, adaugă `{"type": "function_call_output", "call_id": ..., "output": ...}` — nu `{"role": "tool", "tool_call_id": ..., "content": ...}`. Pentru cererea de instrument a asistentului, folosește `messages.extend(response.output)` — nu un dicționar manual `{"role": "assistant", "tool_calls": [...]}`.
21. **`strict: true` necesită `required` + `additionalProperties: false`**: Când folosești `strict: true` pe un instrument, fiecare proprietate trebuie listată în array-ul `required` și `additionalProperties` trebuie să fie `false`. Lipsa uneia dintre acestea cauzează o eroare 400.
22. **ID-urile apelurilor de funcție au prefixe specifice**: Când oferi elemente `function_call` în stil few-shot în `input`, câmpul `id` trebuie să înceapă cu `fc_` iar câmpul `call_id` să înceapă cu `call_` (ex. `"id": "fc_example1", "call_id": "call_example1"`). Utilizarea vechiului prefix `call_` pentru `id` este respinsă.
23. **GitHub Models nu suportă Responses API**: Dacă aplicația are o cale de cod pentru GitHub Models (`base_url` indicând spre `models.github.ai` sau `models.inference.ai.azure.com`), elimin-o complet. Nu există cale de migrare — treci la Azure OpenAI, OpenAI, sau un endpoint local compatibil.
24. **Structura corpului de eroare pentru filtrul de conținut s-a schimbat**: Erorile din Chat Completions foloseau `error.body["innererror"]["content_filter_result"]` (la singular). Erorile din Responses API folosesc `error.body["content_filters"][0]["content_filter_results"]` (la plural, într-un array). Cheia `innererror` nu mai există. Codul care accesează direct `innererror` va genera `KeyError` la rulare — acest lucru este ușor de ratat în migrare deoarece apare doar când filtrul de conținut se activează. Caută întotdeauna `innererror` în migrare.
25. **Apelurile HTTP brute necesită rescrierea URL-ului și a corpului**: Aplicațiile care apelează direct Azure OpenAI REST (prin `requests`, `httpx`, `aiohttp`) folosind `/openai/deployments/{name}/chat/completions?api-version=...` trebuie să treacă la `/openai/v1/responses`. Corpul cererii folosește `input` în loc de `messages`, necesită `max_output_tokens` și `store`, iar parametrul de interogare `api-version` este eliminat. Textul din corpul răspunsului se găsește în `output[0].content[0].text` — **nu** în `output_text`, care este o proprietate convenabilă SDK, absentă în JSON-ul REST brut.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Declinare a responsabilității**:
Acest document a fost tradus folosind serviciul de traducere AI [Co-op Translator](https://github.com/Azure/co-op-translator). În timp ce ne străduim pentru acuratețe, vă rugăm să rețineți că traducerile automate pot conține erori sau inexactități. Documentul original în limba sa nativă trebuie considerat sursa autorizată. Pentru informații critice, se recomandă traducerea profesională realizată de un om. Nu ne asumăm responsabilitatea pentru eventualele neînțelegeri sau interpretări greșite care decurg din utilizarea acestei traduceri.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->