# Risoluzione dei problemi, tabella dei rischi e insidie

## Risoluzione dei problemi 400s

| Errore | Correzione |
|-------|-----|
| `missing_required_parameter: tools[0].name` | La definizione dello strumento usa il vecchio formato annidato di Chat Completions | Appiattire da `{"type": "function", "function": {"name": ...}}` a `{"type": "function", "name": ..., "parameters": ...}` — name, description, parameters vanno al livello superiore |
| `unknown_parameter: input[N].tool_calls` | I risultati dello strumento multi-turn usano il vecchio formato di Chat Completions | Sostituire `{"role": "assistant", "tool_calls": [...]}` + `{"role": "tool", ...}` con elementi `response.output` + `{"type": "function_call_output", "call_id": ..., "output": ...}` |
| `invalid_function_parameters: 'required' is required` | Lo strumento con `strict: true` manca dell'array `required` | Quando `strict: true`, tutte le proprietà devono essere elencate in `required` e deve essere impostato `additionalProperties: false` |
| `invalid_function_parameters: 'additionalProperties' is required` | Lo strumento con `strict: true` manca di `additionalProperties: false` | Aggiungere `"additionalProperties": false` all'oggetto dei parametri |
| `invalid input[N].id: Expected an ID that begins with 'fc'` | L'ID di function_call few-shot ha prefisso sbagliato | Gli ID delle chiamate di funzione devono iniziare con `fc_` (esempio `fc_example1`), non con `call_` |
| `missing_required_parameter: text.format.name` | Aggiungere la chiave `"name"` al dizionario del formato (es. `"name": "Output"`) |
| `invalid_type: text.format` | Assicurarsi che `text.format` sia un dizionario con le chiavi `type`, `name`, `strict`, `schema` — non una stringa |
| `invalid input content type` | Usare i tipi di contenuto `input_text`/`output_text` invece del testo Chat `text` |
| `invalid input content type` (immagine) | Il contenuto dell'immagine usa ancora `"type": "image_url"` | Cambiare in `"type": "input_image"` |
| `Expected object, got string` su `image_url` | `image_url` è ancora un oggetto annidato `{"url": "..."}` | Appiattirlo a stringa semplice: `"image_url": "https://..."` o `"image_url": "data:image/...;base64,..."` |
| `integer below minimum value` per `max_output_tokens` | Il minimo è **16** su Azure OpenAI. Usare 50+ per test, 1000+ per produzione. |
| `429 Too Many Requests` durante lo streaming | Rate limitato. Impacchettare lo streaming in `try/except`, restituire JSON di errore al frontend, implementare backoff/ritentativi. |
| `KeyError: 'innererror'` su errore di filtro contenuti | La struttura del corpo errore filtro contenuti è cambiata nelle Responses API | Chat Completions usava `error.body["innererror"]["content_filter_result"]`; Responses API usa `error.body["content_filters"][0]["content_filter_results"]` (plurale, dentro un array). Riscrivere tutti gli accessi a `innererror`. |

---

## Tabella dei rischi di migrazione

| Sintomo | Probabile errore | Correzione |
|---------|---------------|-----|
| `output_text` vuoto / risposta troncata | `max_output_tokens` troppo basso per modelli di ragionamento | Impostare `max_output_tokens=1000` o superiore — i token di ragionamento contano nel limite |
| `400 invalid_type: text.format` | Passata stringa `response_format` invece di dizionario `text.format` | Usare `text={"format": {"type": "json_schema", "name": "...", "strict": True, "schema": {...}}}` |
| `404 Not Found` su `/openai/v1/responses` | `base_url` errato — manca il suffisso `/openai/v1/` | Assicurarsi che `base_url=f"{endpoint}/openai/v1/"` (con slash finale) |
| `401 Unauthorized` dopo passaggio a `OpenAI()` | `api_key` non impostata o provider token non passato correttamente | Per EntraID: `api_key=token_provider` (il callable). Per API key: `api_key=os.environ["AZURE_OPENAI_API_KEY"]` |
| Il modello restituisce `deployment not found` | Il parametro `model` non corrisponde al nome del deployment Azure | Usare `model=os.environ["AZURE_OPENAI_DEPLOYMENT"]` — questo è il nome del deployment, non del modello |
| `json.loads(resp.output_text)` genera `JSONDecodeError` | Schema non forzato o modello non supporta JSON rigoroso | Assicurarsi che `"strict": True` nello schema, e che il modello supporti output strutturati |
| Lo streaming non produce eventi `delta` | Verifica tipo evento errato | Filtrare per `event.type == "response.output_text.delta"`, non `chat.completion.chunk` di Chat |
| Errore 400 su input immagine dopo migrazione | Tipo contenuto immagine non aggiornato | Cambiare `"type": "image_url"` → `"type": "input_image"` e appiattire `"image_url": {"url": "..."}` → `"image_url": "..."` (stringa semplice) |
| Chiamate a strumenti entrano in loop infinito | Risultato dello strumento mancante nell'`input` della chiamata seguente | Dopo l'esecuzione dello strumento, aggiungere un elemento `{"type": "function_call_output", "call_id": ..., "output": ...}` all'`input` della richiesta successiva |
| Errore `temperature` con GPT-5 o serie o | Valore esplicito `temperature` diverso da 1 | Rimuovere `temperature` o impostare a `1` per GPT-5 e modelli serie o (o1, o3-mini, o3, o4-mini) |
| Errore `top_p` con serie o | `top_p` non supportato | Rimuovere `top_p` quando si utilizza modelli serie o |
| `max_completion_tokens` non riconosciuto | Parametro specifico Azure utilizzato | Sostituire `max_completion_tokens` con `max_output_tokens`. Impostare a 4096+ per serie o (i token di ragionamento contano nel limite). |
| Output vuoto/troncato dalla serie o | `max_output_tokens` troppo basso | Serie o usa token di ragionamento internamente. Impostare `max_output_tokens=4096` o superiore — non 500–1000. |
| `400 integer_below_min_value` per `max_output_tokens` | Valore inferiore a 16 | Azure OpenAI impone `max_output_tokens >= 16`. Usare 50+ per test rapidi, 1000+ per produzione. |
| `429 Too Many Requests` a metà stream | Rate limit di Azure OpenAI | Lo stream si interrompe silenziosamente senza gestione errori. Impacchettare sempre `async for event in await coroutine:` in `try/except` e restituire `{"error": str(e)}` al frontend. |
| `AzureDeveloperCliCredential` → `CredentialUnavailableError` | Tenant errato o non loggato | Passare esplicitamente `tenant_id=os.getenv("AZURE_TENANT_ID")`. Eseguire localmente `azd auth login --tenant <tenant-id>`. |
| `404 Not Found` usando GitHub Models (`models.github.ai`) | GitHub Models non supporta Responses API | Rimuovere completamente il percorso codice GitHub Models. Usare Azure OpenAI, OpenAI o endpoint locale compatibile (es. Ollama con supporto Responses). |
| MAF `OpenAIChatCompletionClient` ancora usa Chat Completions | Usa client legacy MAF in 1.0.0+ | In MAF 1.0.0+, `OpenAIChatClient` usa di default Responses API. Sostituire `OpenAIChatCompletionClient` con `OpenAIChatClient`. Per pre-1.0.0, aggiornare a `agent-framework-openai>=1.0.0`. |
| L'agente LangChain restituisce vuoto o fallisce con chiamate a strumenti | `ChatOpenAI` non usa Responses API | Aggiungere `use_responses_api=True` a `ChatOpenAI(...)`. Cambiare anche `.content` → `.text` sui messaggi risposta. |
| `KeyError: 'innererror'` nel gestore errori filtro contenuti | Struttura corpo errore cambiata in Responses API | Riscrivere `error.body["innererror"]["content_filter_result"]["jailbreak"]` → `error.body["content_filters"][0]["content_filter_results"]["jailbreak"]`. Il wrapper `innererror` è scomparso; i dettagli filtro contenuti sono ora in un array top-level `content_filters` con `content_filter_results` (plurale) dentro ogni voce. |
| Chiamata HTTP raw a `/openai/deployments/.../chat/completions` ritorna 404 | Vecchio endpoint REST Chat Completions | Riscrivere URL in `/openai/v1/responses`. Cambiare corpo richiesta: `messages` → `input`, aggiungere `max_output_tokens` + `store: false`, rimuovere parametro query `api-version`. Cambiare parsing risposta: `choices[0].message.content` → `output[0].content[0].text` (nota: `output_text` è proprietà di comodità SDK, non presente nel JSON REST raw). |

---

## Insidie

1. Se in precedenza usavi Chat Completions per lo stato della conversazione, gestisci esplicitamente il tuo stato con Responses.
2. Preferisci `max_output_tokens` rispetto al legacy `max_tokens`.
3. Durante la migrazione a `gpt-5`, assicurati che `temperature` non sia specificato o sia impostato a `1`.
4. Sostituisci Chat `content[].type: "text"` con Responses `content[].type: "input_text"` per input utente/sistema.
5. Per `text.format`, fornire un dizionario appropriato (es. `{"type": "json_schema", "name": "Output", "schema": ..., "strict": True}`), non una semplice stringa.
6. Il parametro `seed` non è supportato in Responses; rimuoverlo dalle richieste.
7. **Reasoning**: Includi `reasoning` solo se il codice originale lo usava già. Non aggiungere `reasoning` alle chiamate API che non lo avevano — molti modelli non di ragionamento non supportano questo parametro.
8. **Dimensionamento di `max_output_tokens`**: Per modelli di ragionamento (GPT-5-mini, GPT-5, serie o), usare `max_output_tokens=4096` o superiore — non 50–1000. Il modello usa token di ragionamento internamente prima di generare output visibile; limiti troppo bassi causano risposte troncate o vuote.
9. **`max_completion_tokens` della serie o**: Se il codice originale usava `max_completion_tokens` (specifico Azure per serie o), sostituirlo con `max_output_tokens`. Responses API non accetta `max_completion_tokens`.
10. **`reasoning_effort` della serie o**: Se il codice originale usa `reasoning_effort` (low/medium/high), migrarlo in `reasoning={"effort": "<valore>"}` nella chiamata Responses API.
11. **Ritardo streaming serie o**: I modelli serie o eseguono ragionamento interno prima di generare output. In streaming, aspettarsi un ritardo più lungo prima del primo evento `response.output_text.delta`. È normale — il modello sta ragionando, non è bloccato.
9. **`_azure_ad_token_provider` è sparito**: `AsyncOpenAI` / `OpenAI` non hanno l'attributo `_azure_ad_token_provider`. I test o codice che accedono a questo attributo falliranno con `AttributeError`. Il token provider è passato come `api_key` e non è ispezionabile nell'oggetto client.
10. **File snapshot / golden**: Se la suite di test usa snapshot testing, **tutti** i file snapshot contenenti forme di streaming Chat Completions (`choices[0]`, `content_filter_results`, `function_call`, ecc.) devono essere aggiornati alla nuova forma Responses. È facile da dimenticare e causa fallimenti di asserzioni snapshot.
11. **Percorso mock monkeypatch**: Il target del monkeypatch cambia da `openai.resources.chat.AsyncCompletions.create` → `openai.resources.responses.AsyncResponses.create` (o `Responses.create` per sync). Usare il vecchio percorso non ha effetto silenziosamente — il mock non intercetta, e i test chiamano la vera API o falliscono.
12. **`input` non `messages`**: Le funzioni mock devono leggere `kwargs.get("input")` non `kwargs.get("messages")`. Responses API usa `input` per la cronologia conversazione.
13. **Nomenclatura variabili ambiente**: Azure Identity SDK usa `AZURE_CLIENT_ID` (non `AZURE_OPENAI_CLIENT_ID`) per `ManagedIdentityCredential(client_id=...)`. Rinominare in test, file `.env`, impostazioni app e Bicep/infra.
14. **Minimo `max_output_tokens` è 16**: Azure OpenAI respinge valori sotto 16 con `400 integer_below_min_value`. Usare 50 per test rapidi, 1000+ per produzione. Il vecchio `max_tokens` non aveva questo minimo.
15. **`tenant_id` per `AzureDeveloperCliCredential`**: Se la risorsa Azure OpenAI è in tenant diverso, è **obbligatorio** passare `tenant_id` esplicitamente — `AzureDeveloperCliCredential(tenant_id=os.getenv("AZURE_TENANT_ID"))`. Senza questo, la credential usa silenziosamente tenant sbagliato e restituisce `401`.
16. **I limiti di velocità si manifestano diversamente nello streaming**: Con Chat Completions, un 429 solitamente impediva l'avvio dello stream. Con Responses API streaming, un 429 può comparire **a metà stream** — l'iteratore async solleva un'eccezione. Incapsulare sempre il loop di streaming in `try/except` e restituire una riga JSON di errore così il frontend può gestirla con grazia.

17. **La gestione degli errori nello streaming è obbligatoria per le web app**: Il pattern `try: async for event in await coroutine: ... except Exception as e: yield json.dumps({"error": str(e)})` è fondamentale. Senza di esso, lo stream SSE/JSONL si interrompe silenziosamente in caso di qualsiasi errore lato server e il frontend si blocca.
18. **Le definizioni degli strumenti devono usare un formato piatto**: L’API Responses si aspetta `{"type": "function", "name": ..., "parameters": ...}` — non il formato annidato di Chat Completions `{"type": "function", "function": {"name": ..., "parameters": ...}}`. Questo è l’errore di migrazione più comune nel codice che invoca funzioni.
19. **`pydantic_function_tool()` è incompatibile**: Il helper `openai.pydantic_function_tool()` genera ancora il vecchio formato annidato. Non usarlo con `responses.create()`. Definisci gli schemi dello strumento manualmente o appiattisci l’output.
20. **I risultati degli strumenti usano `function_call_output`, non `role: tool`**: Dopo aver eseguito uno strumento, aggiungi `{"type": "function_call_output", "call_id": ..., "output": ...}` — non `{"role": "tool", "tool_call_id": ..., "content": ...}`. Per la richiesta dello strumento da parte dell’assistente, usa `messages.extend(response.output)` — non un dizionario manuale `{"role": "assistant", "tool_calls": [...]}`.
21. **`strict: true` richiede `required` + `additionalProperties: false`**: Quando si usa `strict: true` su uno strumento, ogni proprietà deve essere elencata nell’array `required` e `additionalProperties` deve essere `false`. La mancanza di uno di questi genera un errore 400.
22. **Gli ID delle chiamate di funzione hanno prefissi specifici**: Quando si forniscono pochi esempi `function_call` in `input`, il campo `id` deve iniziare con `fc_` e il campo `call_id` deve iniziare con `call_` (es. `"id": "fc_example1", "call_id": "call_example1"`). Usare il vecchio prefisso `call_` di Chat Completions per `id` è rifiutato.
23. **GitHub Models non supporta l’API Responses**: Se l’app ha un percorso code con GitHub Models (`base_url` che punta a `models.github.ai` o `models.inference.ai.azure.com`), rimuoverlo completamente. Non esiste un percorso di migrazione — passa a Azure OpenAI, OpenAI o a un endpoint locale compatibile.
24. **La struttura del corpo dell’errore del filtro contenuti è cambiata**: Gli errori di Chat Completions usavano `error.body["innererror"]["content_filter_result"]` (singolare). Gli errori dell’API Responses usano `error.body["content_filters"][0]["content_filter_results"]` (plurale, dentro un array). La chiave `innererror` non esiste più. Il codice che accede direttamente a `innererror` genera `KeyError` a runtime — questo è facile da non notare nella migrazione perché si manifesta solo quando il filtro contenuti si attiva. Cerca sempre `innererror` durante la migrazione.
25. **Le chiamate HTTP raw richiedono la riscrittura di URL + body**: Le app che chiamano direttamente REST di Azure OpenAI (via `requests`, `httpx`, `aiohttp`) usando `/openai/deployments/{name}/chat/completions?api-version=...` devono passare a `/openai/v1/responses`. Il corpo della richiesta usa `input` invece di `messages`, richiede `max_output_tokens` e `store`, e il parametro di query `api-version` non è più necessario. Il testo del corpo della risposta è in `output[0].content[0].text` — **non** in `output_text`, che è una proprietà di comodità SDK non presente nel JSON REST raw.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:
Questo documento è stato tradotto utilizzando il servizio di traduzione AI [Co-op Translator](https://github.com/Azure/co-op-translator). Sebbene ci impegniamo per garantire la precisione, si prega di notare che le traduzioni automatizzate possono contenere errori o imprecisioni. Il documento originale nella sua lingua nativa deve essere considerato la fonte autorevole. Per informazioni critiche, si raccomanda una traduzione professionale effettuata da un essere umano. Non siamo responsabili per eventuali malintesi o interpretazioni errate derivanti dall’uso di questa traduzione.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->