# Rezolvarea problemelor, Tabel de riscuri & Capcane

## Rezolvarea problemelor 400s

| Eroare | Remediere |
|-------|-----|
| `missing_required_parameter: tools[0].name` | Definiția uneltei folosește vechiul format imbricat Chat Completions | Aplatizați de la `{"type": "function", "function": {"name": ...}}` la `{"type": "function", "name": ..., "parameters": ...}` — name, description, parameters se mută la nivelul principal |
| `unknown_parameter: input[N].tool_calls` | Rezultatele multi-turn folosesc vechiul format Chat Completions | Înlocuiți `{"role": "assistant", "tool_calls": [...]}` + `{"role": "tool", ...}` cu elemente `response.output` + `{"type": "function_call_output", "call_id": ..., "output": ...}` |
| `invalid_function_parameters: 'required' is required` | Unealta cu `strict: true` lipsește array-ul `required` | Când `strict: true`, toate proprietățile trebuie enumerate în `required` și trebuie setat `additionalProperties: false` |
| `invalid_function_parameters: 'additionalProperties' is required` | Unealta cu `strict: true` lipsește `additionalProperties: false` | Adăugați `"additionalProperties": false` în obiectul parameters |
| `invalid input[N].id: Expected an ID that begins with 'fc'` | ID-ul function_call few-shot are prefix greșit | ID-urile apelurilor de funcții trebuie să înceapă cu `fc_` (ex., `fc_example1`), nu `call_` |
| `missing_required_parameter: text.format.name` | Adăugați cheia `"name"` în dicționarul format (ex., `"name": "Output"`) |
| `invalid_type: text.format` | Asigurați-vă că `text.format` este un dicționar cu cheile `type`, `name`, `strict`, `schema` — nu un string |
| `invalid input content type` | Folosiți tipurile de conținut `input_text`/`output_text` în loc de Chat `text` |
| `invalid input content type` (imagine) | Tipul conținutului imagine folosește încă `"type": "image_url"` | Schimbați în `"type": "input_image"` |
| `Expected object, got string` pe `image_url` | `image_url` este încă un obiect imbricat `{"url": "..."}` | Aplatizați la un string simplu: `"image_url": "https://..."` sau `"image_url": "data:image/...;base64,..."` |
| `integer below minimum value` pentru `max_output_tokens` | Minim este **16** pe Azure OpenAI. Folosiți 50+ pentru testări, 1000+ pentru producție. |
| `429 Too Many Requests` în timpul streamingului | Limitare de rată. Încapsulați streamingul în `try/except`, returnați JSON de eroare către frontend, implementați backoff/retry. |
| `KeyError: 'innererror'` la eroarea filtrului de conținut | Structura corpului erorii filtrului de conținut s-a schimbat în Responses API | Chat Completions folosea `error.body["innererror"]["content_filter_result"]`; Responses API folosește `error.body["content_filters"][0]["content_filter_results"]` (plural, într-un array). Rescrieți toate accesările `innererror`. |

---

## Tabel Riscuri Migrare

| Simptom | Greșeală Probabilă | Remediere |
|---------|---------------|-----|
| `output_text` gol / răspuns trunchiat | `max_output_tokens` prea mic pentru modelele de raționament | Setați `max_output_tokens=1000` sau mai mult — tokenii de raționament contează în limită |
| `400 invalid_type: text.format` | Ați transmis un string `response_format` în loc de dicționar `text.format` | Folosiți `text={"format": {"type": "json_schema", "name": "...", "strict": True, "schema": {...}}}` |
| `404 Not Found` pe `/openai/v1/responses` | `base_url` greșit — lipsește sufixul `/openai/v1/` | Asigurați `base_url=f"{endpoint}/openai/v1/"` (cu slash la final) |
| `401 Unauthorized` după schimbare la `OpenAI()` | `api_key` nu este setat sau token provider nu este transmis corect | Pentru EntraID: `api_key=token_provider` (callable). Pentru cheie API: `api_key=os.environ["AZURE_OPENAI_API_KEY"]` |
| Modelul returnează `deployment not found` | Parametrul `model` nu coincide cu numele deployment-ului Azure | Folosiți `model=os.environ["AZURE_OPENAI_DEPLOYMENT"]` — acesta este numele deployment-ului, nu al modelului |
| `json.loads(resp.output_text)` ridică `JSONDecodeError` | Schema nu se aplică sau modelul nu suportă JSON strict | Asigurați `"strict": True` în schemă și verificați suportul modelului pentru output structurat |
| Streaming nu livrează evenimente `delta` | Verificați tipul greșit de eveniment | Filtrați pe `event.type == "response.output_text.delta"`, nu pe `chat.completion.chunk` al Chatului |
| Eroare `400` pe input imagine după migrare | Tipul conținutului imaginii nu actualizat | Schimbați `"type": "image_url"` → `"type": "input_image"` și aplatizați `"image_url": {"url": "..."}` → `"image_url": "..."` (string simplu) |
| Apeluri unelte în buclă infinită | Rezultat unealtă lipsă în următorul `input` | După executarea unei unelte, adăugați un element `{"type": "function_call_output", "call_id": ..., "output": ...}` în `input` la următoarea cerere |
| Eroare `temperature` cu GPT-5 sau seria o | Valoare explicită `temperature` diferită de 1 | Scoateți `temperature` sau setați la `1` pentru modelele GPT-5 și seria o (o1, o3-mini, o3, o4-mini) |
| Eroare `top_p` cu seria o | `top_p` nu este suportat | Scoateți `top_p` când vizați modelele din seria o |
| `max_completion_tokens` nerecunoscut | Folosire parametru specific Azure | Înlocuiți `max_completion_tokens` cu `max_output_tokens`. Setați la 4096+ pentru seria o (tokenii de raționament contează în limită). |
| Output gol/trunchiat de la seria o | `max_output_tokens` prea mic | Seria o folosește tokeni de raționament intern. Setați `max_output_tokens=4096` sau mai mult — nu 500–1000. |
| `400 integer_below_min_value` pentru `max_output_tokens` | Valoare sub 16 | Azure OpenAI impune `max_output_tokens >= 16`. Folosiți 50+ pentru teste rapide, 1000+ pentru producție. |
| `429 Too Many Requests` pe parcursul streamului | Limitare Azure OpenAI | Streamul se întrerupe silențios fără gestionare eroare. Întotdeauna încapsulați `async for event in await coroutine:` în `try/except` și returnați `{"error": str(e)}` către frontend. |
| `AzureDeveloperCliCredential` → `CredentialUnavailableError` | Tenant greșit sau logout | Transmiteți explicit `tenant_id=os.getenv("AZURE_TENANT_ID")`. Rulați local `azd auth login --tenant <tenant-id>`. |
| `404 Not Found` folosind Modele GitHub (`models.github.ai`) | Modelele GitHub nu suportă Responses API | Eliminați complet calea de cod pentru modelele GitHub. Folosiți Azure OpenAI, OpenAI sau endpoint local compatibil (ex. Ollama cu suport Responses). |
| MAF `OpenAIChatCompletionClient` încă folosește Chat Completions | Client MAF legacy în 1.0.0+ | În MAF 1.0.0+, `OpenAIChatClient` folosește Responses API implicit. Înlocuiți `OpenAIChatCompletionClient` cu `OpenAIChatClient`. Pentru versiuni pre-1.0.0, faceți upgrade la `agent-framework-openai>=1.0.0`. |
| Agent LangChain returnează gol sau eșuează cu apeluri unelte | `ChatOpenAI` nu folosește Responses API | Adăugați `use_responses_api=True` la `ChatOpenAI(...)`. De asemenea, schimbați `.content` în `.text` pe mesajele răspuns. |
| `KeyError: 'innererror'` în handler eroare filtru conținut | Structura corpului erorii s-a schimbat în Responses API | Rescrieți `error.body["innererror"]["content_filter_result"]["jailbreak"]` → `error.body["content_filters"][0]["content_filter_results"]["jailbreak"]`. Wrapper-ul `innererror` a dispărut; detaliile filtrului conținut sunt acum într-un array la nivel superior `content_filters`, fiecare intrare având `content_filter_results` (plural). |
| Apel HTTP brut la `/openai/deployments/.../chat/completions` întoarce 404 | Endpoint REST Chat Completions vechi | Rescrieți URL în `/openai/v1/responses`. Schimbați corpul cererii: `messages` → `input`, adăugați `max_output_tokens` + `store: false`, eliminați parametru query `api-version`. Schimbați parsarea răspunsului: `choices[0].message.content` → `output[0].content[0].text` (notă: `output_text` este o proprietate comoditate SDK, nu în JSON-ul REST brut). |

---

## Capcane

1. Dacă ați folosit anterior Chat Completions pentru starea conversației, gestionați-vă propria stare explicit cu Responses.
2. Preferabil `max_output_tokens` în loc de `max_tokens` legacy.
3. La migrarea la `gpt-5`, asigurați-vă că `temperature` nu este specificat sau este setat la `1`.
4. Înlocuiți Chat `content[].type: "text"` cu Responses `content[].type: "input_text"` pentru input-uri user/sistem.
5. Pentru `text.format`, furnizați un dicționar corect (ex., `{"type": "json_schema", "name": "Output", "schema": ..., "strict": True}`), nu un string simplu.
6. Parametrul `seed` nu este suportat în Responses; eliminați-l din cereri.
7. **Raționament**: Includeți `reasoning` doar dacă codul original îl folosea deja. Nu adăugați `reasoning` la apelurile API care nu-l aveau — multe modele fără raționament nu suportă acest parametru.
8. **Dimensionarea `max_output_tokens`**: Pentru modelele de raționament (GPT-5-mini, GPT-5, seria o), folosiți `max_output_tokens=4096` sau mai mult — nu 50–1000. Modelul folosește tokeni de raționament intern înainte de a genera output vizibil; limite prea mici duc la răspunsuri trunchiate sau goale.
9. **`max_completion_tokens` în seria o**: Dacă codul original folosea `max_completion_tokens` (specific Azure pentru seria o), înlocuiți cu `max_output_tokens`. Responses API nu acceptă `max_completion_tokens`.
10. **`reasoning_effort` pentru seria o**: Dacă codul original folosea `reasoning_effort` (low/medium/high), migrați-l la `reasoning={"effort": "<valoare>"}` în apelul Responses API.
11. **Întârzierea la streaming în seria o**: Modelele seria o efectuează raționament intern înainte de a genera output. La streaming, așteptați o întârziere mai lungă înainte de primul eveniment `response.output_text.delta`. Este normal — modelul raționează, nu este blocat.
9. **`_azure_ad_token_provider` a dispărut**: `AsyncOpenAI` / `OpenAI` nu mai au atributul `_azure_ad_token_provider`. Testele sau codurile care accesează acest atribut vor eșua cu `AttributeError`. Providerul de token este transmis ca `api_key` și nu este inspectabil pe client.
10. **Fișiere snapshot / golden**: Dacă suita de teste folosește testare snapshot, **toate** fișierele snapshot care conțin formele de streaming Chat Completions (`choices[0]`, `content_filter_results`, `function_call`, etc.) trebuie actualizate la noua formă Responses. Este ușor să treceți cu vederea și cauzează erori de aserțiune în snapshot.
11. **Calea de monkeypatch pentru mock**: Ținta monkeypatch se schimbă de la `openai.resources.chat.AsyncCompletions.create` → `openai.resources.responses.AsyncResponses.create` (sau `Responses.create` pentru sync). Folosirea căii vechi nu are efect — mockul nu va intercepta, iar testele vor apela API-ul real sau vor eșua.
12. **`input` nu `messages`**: Funcțiile mock trebuie să citească `kwargs.get("input")`, nu `kwargs.get("messages")`. Responses API folosește `input` pentru istoricul conversației.
13. **Numele variabilelor de mediu**: Azure Identity SDK folosește `AZURE_CLIENT_ID` (nu `AZURE_OPENAI_CLIENT_ID`) pentru `ManagedIdentityCredential(client_id=...)`. Schimbați în teste, fișiere `.env`, setări app și în infrastructură/Bicep.
14. **Minimul `max_output_tokens` este 16**: Azure OpenAI respinge valori sub 16 cu `400 integer_below_min_value`. Folosiți 50 pentru teste rapide, 1000+ pentru producție. Vechiul `max_tokens` nu impunea acest minim.
15. **`tenant_id` pentru `AzureDeveloperCliCredential`**: Când resursa Azure OpenAI este într-un tenant diferit, trebuie să transmiteți explicit `tenant_id` — `AzureDeveloperCliCredential(tenant_id=os.getenv("AZURE_TENANT_ID"))`. Altfel, credentialul folosește silențios tenantul greșit și returnează `401`.
16. **Limitele de rată apar diferit în streaming**: Cu Chat Completions, un 429 prevenea de obicei începutul streamului. Cu Responses API streaming, un 429 se poate produce **în timpul streamului** — iteratorul async ridică o excepție. Încapsulați întotdeauna bucla de streaming în `try/except` și returnați o linie JSON de eroare pentru ca frontendul să o gestioneze elegant.

17. **Gestionarea erorilor în streaming este obligatorie pentru aplicațiile web**: Modelul `try: async for event in await coroutine: ... except Exception as e: yield json.dumps({"error": str(e)})` este esențial. Fără acesta, fluxul SSE/JSONL moare silențios la orice eroare de pe server și frontendul rămâne blocat.
18. **Definițiile instrumentelor trebuie să folosească formatul plat**: API-ul Responses așteaptă `{"type": "function", "name": ..., "parameters": ...}` — nu forma încastrată specifică Chat Completions `{"type": "function", "function": {"name": ..., "parameters": ...}}`. Aceasta este cea mai frecventă eroare la migrarea codului pentru apelul funcțiilor.
19. **`pydantic_function_tool()` este incompatibil**: Helperul `openai.pydantic_function_tool()` încă generează vechiul format încastrat. Nu îl utilizați cu `responses.create()`. Definiți manual schemele pentru instrumente sau aplatizați ieșirea.
20. **Rezultatele instrumentelor folosesc `function_call_output`, nu `role: tool`**: După executarea unui instrument, adăugați `{"type": "function_call_output", "call_id": ..., "output": ...}` — nu `{"role": "tool", "tool_call_id": ..., "content": ...}`. Pentru cererea de instrument a asistentului, folosiți `messages.extend(response.output)` — nu un dicționar manual `{"role": "assistant", "tool_calls": [...]}`.
21. **`strict: true` necesită `required` + `additionalProperties: false`**: Când folosiți `strict: true` pe un instrument, fiecare proprietate trebuie listată în array-ul `required` iar `additionalProperties` trebuie să fie `false`. Lipsa oricăruia cauzează o eroare 400.
22. **ID-urile apelurilor funcțiilor au prefixe specifice**: Când furnizați itemi `function_call` few-shot în `input`, câmpul `id` trebuie să înceapă cu `fc_` iar câmpul `call_id` trebuie să înceapă cu `call_` (exemplu: `"id": "fc_example1", "call_id": "call_example1"`). Utilizarea vechiului prefix `call_` pentru `id` în Chat Completions este respinsă.
23. **GitHub Models nu suportă Responses API**: Dacă aplicația are o cale de cod GitHub Models (`base_url` indicând către `models.github.ai` sau `models.inference.ai.azure.com`), ștergeți-o complet. Nu există cale de migrare — treceți la Azure OpenAI, OpenAI sau un endpoint local compatibil.
24. **Structura corpului erorii filtrului de conținut s-a schimbat**: Erorile din Chat Completions foloseau `error.body["innererror"]["content_filter_result"]` (la singular). Erorile API-ului Responses folosesc `error.body["content_filters"][0]["content_filter_results"]` (la plural, într-un array). Cheia `innererror` nu mai există. Codul care accesează direct `innererror` va arunca `KeyError` la rulare — ușor de ratat la migrare deoarece apare doar când filtrul de conținut declanșează o excepție. Căutați întotdeauna `innererror` în timpul migrației.
25. **Apelurile HTTP brute necesită rescrierea URL-ului și a corpului**: Aplicațiile care apelează direct REST-ul Azure OpenAI (prin `requests`, `httpx`, `aiohttp`) folosind `/openai/deployments/{name}/chat/completions?api-version=...` trebuie să treacă la `/openai/v1/responses`. Corpul cererii folosește `input` în loc de `messages`, necesită `max_output_tokens` și `store`, iar parametrul de interogare `api-version` este eliminat. Textul corpului răspunsului este la `output[0].content[0].text` — **nu** `output_text`, care este o proprietate convenabilă a SDK-ului ce nu există în JSON-ul raw REST.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Declinare a responsabilității**:
Acest document a fost tradus folosind serviciul de traducere AI [Co-op Translator](https://github.com/Azure/co-op-translator). În timp ce ne străduim pentru acuratețe, vă rugăm să rețineți că traducerile automate pot conține erori sau inexactități. Documentul original în limba sa nativă trebuie considerat sursa autorizată. Pentru informații critice, se recomandă traducerea profesională realizată de un om. Nu ne asumăm responsabilitatea pentru eventualele neînțelegeri sau interpretări greșite care decurg din utilizarea acestei traduceri.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->