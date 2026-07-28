---
name: azure-openai-to-responses
license: MIT
---
# Migrare app Python da Azure OpenAI Chat Completions all'API Responses

> **GUIDA AUTOREVOLE — SEGUIRE ESATTAMENTE**
>
> Questa skill migra basi di codice Python che usano Azure OpenAI Chat Completions
> all'API unificata Responses. Seguire queste istruzioni alla lettera.
> Non improvvisare mappature di parametri o inventare forme API.

---

## Trigger

Attiva questa skill quando un utente vuole:
- Migrare un'app Python da Azure OpenAI Chat Completions all'API Responses
- Aggiornare l'uso del Python OpenAI SDK all'ultima forma API contro Azure OpenAI
- Preparare codice Python per modelli GPT-5 o più recenti che richiedono Responses su Azure
- Passare da `AzureOpenAI`/`AsyncAzureOpenAI` al client standard `OpenAI`/`AsyncOpenAI` con endpoint v1
- Risolvere avvisi di deprecazione relativi a costruttori `AzureOpenAI` o `api_version`

---

## ⚠️ Compatibilità Modello — VERIFICARE PRIMA

> **Prima di migrare, verifica che il tuo deployment Azure OpenAI supporti l'API Responses.**

### 1. Test rapido del deployment (più veloce)

```python
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ["AZURE_OPENAI_API_KEY"],
    base_url=f"{os.environ['AZURE_OPENAI_ENDPOINT'].rstrip('/')}/openai/v1/",
)

try:
    resp = client.responses.create(
        model=os.environ["AZURE_OPENAI_DEPLOYMENT"],
        input="ping",
        max_output_tokens=50,
        store=False,
    )
    print(f"✅ Deployment supports Responses API: {resp.output_text}")
except Exception as e:
    print(f"❌ Deployment does NOT support Responses API: {e}")
```

> **Nota**: `max_output_tokens` ha un **minimo di 16** su Azure OpenAI. Valori sotto 16 restituiscono errore 400. Usa 50+ per test rapidi.

Se questo restituisce un 404, il modello del deployment non supporta ancora Responses — vedi riferimento sotto o ridistribuisci con un modello supportato.

### 2. Controlla i modelli disponibili nella tua regione (consigliato)

Esegui lo strumento integrato di verifica compatibilità modelli per vedere cosa è disponibile con supporto API Responses nella tua regione specifica:

```bash
python migrate.py models --subscription YOUR_SUB_ID --location YOUR_REGION
```

Questa interroga Azure ARM dal vivo e mostra una matrice di compatibilità — quali modelli supportano Responses, output strutturato, strumenti, ecc. Usa `--filter gpt-5.1,gpt-5.2` per restringere i risultati o `--json` per scripting.

### 3. Riferimento completo supporto modelli

- **Query live**: `python migrate.py models` (vedi sopra — specifico per regione, sempre aggiornato)
- **Sfoglia disponibilità**: [Tabella riepilogativa modelli e disponibilità regionale](https://learn.microsoft.com/en-us/azure/foundry/foundry-models/concepts/models-sold-directly-by-azure?tabs=global-standard-aoai%2Cglobal-standard&pivots=azure-openai#model-summary-table-and-region-availability)
- **Quickstart & guida**: **https://aka.ms/openai/start**

### ⚠️ Limitazioni modelli più vecchi

> **ATTENZIONE**: I modelli più vecchi (precedenti a `gpt-4.1`) potrebbero non supportare tutte le funzionalità dell'API Responses in modo completo.
>
> Limitazioni note con modelli più vecchi:
> - **Parametro `reasoning`**: Non supportato su molti modelli senza reasoning. Migra `reasoning` solo se era già presente nel codice originale.
> - **Parametro `seed`**: Non supportato affatto nell'API Responses — rimuoverlo da tutte le richieste.
> - **Output strutturato via `text.format`**: I modelli più vecchi potrebbero non applicare affidabilmente schemi JSON con `strict: true`.
> - **Orchestrazione strumenti**: GPT-5+ orchestra chiamate strumenti come parte del reasoning interno. I modelli più vecchi su Responses funzionano, ma senza questa integrazione profonda.
> - **Vincoli di temperatura**: Migrando a `gpt-5`, la temperatura deve essere omessa o impostata a `1`. I modelli più vecchi non hanno questo vincolo.

### Modelli di reasoning serie O (o1, o3-mini, o3, o4-mini)

I modelli serie O hanno vincoli parametrici unici. Quando si migrano app che usano modelli serie O:

- **`temperature`**: Deve essere `1` (o omesso). I modelli serie O non accettano altri valori.
- **`max_completion_tokens` → `max_output_tokens`**: Le app che usano lo specifico `max_completion_tokens` di Azure devono passare a `max_output_tokens`. Imposta valori alti (4096+) perché i token di reasoning contano nel limite.
- **`reasoning_effort`**: Se l'app usa `reasoning_effort` (low/medium/high), mantenerlo — l'API Responses supporta questo parametro per modelli serie O.
- **Comportamento streaming**: I modelli serie O possono bufferizzare l'output fino al termine del reasoning prima di emettere eventi delta testo. Lo streaming funziona ancora, ma il primo `response.output_text.delta` può arrivare dopo un ritardo maggiore rispetto ai modelli GPT.
- **`top_p`**: Non supportato sui modelli serie O — rimuovere se presente.
- **Uso strumenti**: I modelli serie O supportano strumenti via l'API Responses come i modelli GPT, ma l'orchestrazione di chiamate strumenti varia per modello.

**Azione — avviso proattivo modello**: Durante la fase di scansione, verifica quale modello l'app usa (nomi deployment, variabili ambiente, config). Se il modello è precedente a `gpt-4.1` (non gpt-4.1+), informa proattivamente l'utente:
- La migrazione funzionerà per testo base, chat, streaming e strumenti sul loro modello corrente.
- I modelli più recenti (`gpt-5.1`, `gpt-5.2`) offrono migliore orchestrazione strumenti, applicazione output strutturato, reasoning e disponibilità cross-regione.
- Dovrebbero considerare di aggiornare il deployment quando pronti — non è un blocco alla migrazione.

Non bloccare o rifiutare la migrazione in base alla versione modello. L'avviso è informativo.

### GitHub Models NON supporta l'API Responses

> **GitHub Models (`models.github.ai`, `models.inference.ai.azure.com`) non supporta l'API Responses.**

Se il codice contiene un percorso GitHub Models (cerca `base_url` che punta a `models.github.ai` o `models.inference.ai.azure.com`), **rimuoverlo interamente** durante la migrazione. L'API Responses richiede Azure OpenAI, OpenAI o un endpoint locale compatibile (es. Ollama con supporto Responses).

Azione durante la scansione:
- Segnala tutti i percorsi codice GitHub Models per rimozione.

---

## Migrazione Framework

Molte app usano framework di livello superiore sopra OpenAI. Migrandoli, cambiano anche le API del framework, non solo le chiamate OpenAI sottostanti.

### Microsoft Agent Framework (MAF)

**Controlla la tua versione MAF prima** — la migrazione dipende se sei su MAF 1.0.0+ o beta/rc pre-1.0.0.

#### MAF 1.0.0+ (agent-framework-openai >= 1.0.0)

`OpenAIChatClient` **usa già l'API Responses** — nessuna migrazione necessaria. Se il codice usa il legacy `OpenAIChatCompletionClient` (che usa `chat.completions.create`), sostituiscilo con `OpenAIChatClient`.

| Prima | Dopo |
|--------|-------|
| `from agent_framework.openai import OpenAIChatCompletionClient` | `from agent_framework.openai import OpenAIChatClient` |
| `OpenAIChatCompletionClient(...)` | `OpenAIChatClient(...)` |

Per controllare la versione: `python -c "import agent_framework_openai; print(agent_framework_openai.__version__)"`

#### MAF pre-1.0.0 (beta/rc)

In MAF pre-1.0.0, `OpenAIChatClient` usava Chat Completions. Aggiorna a `agent-framework-openai>=1.0.0` dove `OpenAIChatClient` usa l'API Responses di default.

Nessun altro cambiamento necessario — le API di `Agent` e strumenti restano uguali.

### LangChain (`langchain-openai`)

Aggiungi `use_responses_api=True` a `ChatOpenAI()`. Aggiorna anche l'accesso alla risposta da `.content` a `.text`.

| Prima | Dopo |
|--------|-------|
| `ChatOpenAI(model=..., base_url=..., api_key=...)` | `ChatOpenAI(model=..., base_url=..., api_key=..., use_responses_api=True)` |
| `result['messages'][-1].content` | `result['messages'][-1].text` |

Per esempi completi di prima/dopo codice, vedi [cheat-sheet.md](./references/cheat-sheet.md).

---

## Guida Migrazione Frontend

> **L'API Responses è una questione lato server.** Migra il tuo backend Python; il contratto HTTP del frontend dovrebbe restare invariato a meno che il backend sia un semplice pass-through — in quel caso, considera di adottare la forma richiesta Responses per eliminare il livello di traduzione. Se il frontend chiama OpenAI direttamente con una chiave client-side, sposta quelle chiamate prima in un backend.

### Deprecazione `@microsoft/ai-chat-protocol`

Il pacchetto npm `@microsoft/ai-chat-protocol` è deprecato e dovrebbe essere sostituito con [`ndjson-readablestream`](https://www.npmjs.com/package/ndjson-readablestream). Se lo incontri in un frontend:

1. Sostituisci il tag script CDN:
   ```html
   <!-- Before -->
   <script src="https://cdn.jsdelivr.net/npm/@microsoft/ai-chat-protocol@.../dist/iife/index.js"></script>
   <!-- After -->
   <script src="https://cdn.jsdelivr.net/npm/ndjson-readablestream@1.0.7/dist/ndjson-readablestream.umd.js"></script>
   ```
2. Rimuovi l'istanza `AIChatProtocolClient` (`new ChatProtocol.AIChatProtocolClient("/chat")`).
3. Sostituisci `client.getStreamedCompletion(messages)` con una chiamata diretta `fetch()` all'endpoint di streaming del backend.
4. Sostituisci `for await (const response of result)` con `for await (const chunk of readNDJSONStream(response.body))`.
5. Aggiorna accesso proprietà da `response.delta.content` / `response.error` a `chunk.delta.content` / `chunk.error`.

---

## Obiettivi

- Elencare tutti i punti di chiamata Python che usano Chat Completions o Completions legacy contro Azure OpenAI.
- Proporre un piano e sequenza di migrazione per la codebase Python.
- Applicare modifiche minime e sicure per passare all'API Responses.
- Aggiornare i chiamanti per consumare lo schema output di Responses; niente wrapper retrocompatibili.
- Eseguire test/lint; correggere rotture banali introdotte dalla migrazione.
- Preparare piccoli set di modifiche revisionabili e fornire un riepilogo finale con diff (non commettere).

---

## Limiti

- Modificare solo file all'interno dello spazio git. Mai scrivere fuori.
- Non preservare shim retrocompatibili; migrare il codice alla nuova forma API.
- Non lasciare commenti di transizione o file di backup.
- Preservare la semantica streaming se usata prima; altrimenti usare modalità non streaming.
- Chiedere approvazione prima di eseguire comandi o chiamate di rete se in modalità approvazione.
- Non eseguire `git add`/`git commit`/`git push`; produrre solo modifiche al working-tree.

---

## Passo 0: Migrazione Cliente Azure OpenAI (Prerequisito)

Se la codebase usa i costruttori `AzureOpenAI` o `AsyncAzureOpenAI`, migrare prima ai costruttori standard `OpenAI` / `AsyncOpenAI`. I costruttori specifici Azure sono deprecati da `openai>=1.108.1`.

### Perché il percorso API v1?

Il nuovo endpoint `/openai/v1` usa il client standard `OpenAI()` invece di `AzureOpenAI()`, non richiede il parametro `api_version`, e funziona identico su OpenAI e Azure OpenAI. Lo stesso codice client è a prova di futuro — nessuna gestione versioni necessaria.

### Cambiamenti chiave

| Prima | Dopo |
|--------|-------|
| `AzureOpenAI` | `OpenAI` |
| `AsyncAzureOpenAI` | `AsyncOpenAI` |
| `azure_endpoint` | `base_url` |
| `azure_ad_token_provider` | `api_key` |
| `api_version=...` | Rimuovere completamente |

### Lista di pulizia

- Rimuovere l'argomento `api_version` dalla costruzione del client.
- Rimuovere le variabili ambiente `AZURE_OPENAI_VERSION` / `AZURE_OPENAI_API_VERSION` da `.env`, impostazioni app, e file Bicep/infra.
- Rinominare `AZURE_OPENAI_CLIENT_ID` → `AZURE_CLIENT_ID` in `.env`, impostazioni app, Bicep/infra e fixture di test (convenzione standard SDK Azure Identity).
- Assicurare `openai>=1.108.1` in `requirements.txt` o `pyproject.toml`.

### Migrazione variabili ambiente

| Vecchia var env | Azione | Note |
|-------------|--------|-------|
| `AZURE_OPENAI_VERSION` | **Rimuovere** | Nessun `api_version` necessario con endpoint v1 |
| `AZURE_OPENAI_API_VERSION` | **Rimuovere** | Come sopra |
| `AZURE_OPENAI_CLIENT_ID` | **Rinominare** → `AZURE_CLIENT_ID` | Convenzione standard SDK Azure Identity per `ManagedIdentityCredential(client_id=...)` |
| `AZURE_OPENAI_ENDPOINT` | **Mantenere** | Ancora necessario per costruzione `base_url` |
| `AZURE_OPENAI_CHAT_DEPLOYMENT` | **Mantenere** | Usato come param `model` in `responses.create` |
| `AZURE_OPENAI_API_KEY` | **Mantenere** | Usato come `api_key` per autenticazione tramite chiave |

Per esempi di setup client (sync, async, EntraID, chiave API, multi-tenant), vedi [cheat-sheet.md](./references/cheat-sheet.md).

---

## Passo 1: Rilevare Punti di Chiamata Legacy

Esegui lo script [detect_legacy.py](../../../../../.agents/skills/azure-openai-to-responses/scripts/detect_legacy.py) per trovare tutti i punti di chiamata che necessitano migrazione:

```bash
python skills/azure-openai-to-responses/scripts/detect_legacy.py .
```

Oppure esegui queste ricerche manualmente — ogni corrispondenza è un obiettivo di migrazione:

```bash
# Chiamate API legacy (deve essere riscritto)
rg "chat\.completions\.create"
rg "ChatCompletion\.create"
rg "Completion\.create"

# Costruttori client Azure deprecati (deve essere sostituito)
rg "AzureOpenAI\("
rg "AsyncAzureOpenAI\("

# Modelli di accesso alla forma di risposta (deve essere aggiornato)
rg "choices\[0\]\.message\.content"
rg "choices\[0\]\.delta\.content"
rg "choices\[0\]\.message\.function_call"
rg "choices\[0\]\.message\.tool_calls"

# Definizioni degli strumenti in vecchio formato annidato (deve essere appiattito)
rg '"function":\s*{\s*"name"'
rg "pydantic_function_tool"

# Risultati degli strumenti in vecchio formato (deve essere convertito in function_call_output)
rg '"role":\s*"tool"'
rg '"tool_call_id"'

# Parametri deprecati (deve essere rimosso o rinominato)
rg "response_format"
rg "max_tokens\b"        # rinominare in max_output_tokens
rg "['\"]seed['\"]"      # remove entirely

# Variabili d'ambiente deprecate (pulire)
rg "AZURE_OPENAI_API_VERSION|AZURE_OPENAI_VERSION"
rg "AZURE_OPENAI_CLIENT_ID"  # dovrebbe essere AZURE_CLIENT_ID

# Endpoint modelli GitHub (deve essere rimosso — API Risposte non supportata)
rg "models\.github\.ai|models\.inference\.ai\.azure"

# Modelli legacy a livello di framework (deve essere aggiornato)
rg "OpenAIChatCompletionClient"  # MAF 1.0.0+: sostituire con OpenAIChatClient
rg "ChatOpenAI\(" | grep -v "use_responses_api"  # LangChain: necessita di use_responses_api=True

# Infrastruttura di test (deve essere aggiornata)
rg "ChatCompletionChunk|AsyncCompletions\.create" tests/
rg "_azure_ad_token_provider" tests/
rg "prompt_filter_results|content_filter_results" tests/
rg "choices\[0\]" tests/

# Accesso al corpo dell'errore del filtro contenuti (deve essere aggiornato — struttura cambiata)
rg 'innererror.*content_filter_result|error\.body\["innererror"\]'
rg "content_filter_result\[" # vecchia forma singolare — ora content_filter_results (plurale) dentro l'array content_filters

# Chiamate HTTP raw all'endpoint Chat Completions (deve aggiornare l'URL)
rg "/openai/deployments/.*/chat/completions"
rg "api-version="
```

### Euristiche (rileva e riscrivi)

- **Client Chat Completions**: `client.chat.completions.create` → `client.responses.create(...)`.

- **Costruttori client Azure**: `AzureOpenAI(...)` → `OpenAI(base_url=..., api_key=...)`.
- **Strumenti**: convertire le definizioni degli strumenti di chiamata funzione dal formato annidato (`{"type": "function", "function": {"name": ...}}`) al formato piatto Responses (`{"type": "function", "name": ...}`); usare `tool_choice`; restituire i risultati degli strumenti come elementi `{"type": "function_call_output", "call_id": ..., "output": ...}` (non `{"role": "tool", ...}`).
- **Giri di chiamata degli strumenti**: quando il modello restituisce chiamate di funzioni, aggiungere gli elementi `response.output` alla conversazione (non un dizionario manuale `{"role": "assistant", "tool_calls": [...]}`), quindi aggiungere elementi `function_call_output` per ogni risultato.
- **Esempi di strumenti few-shot**: se la conversazione include esempi hardcoded di chiamate a strumenti, convertirli in elementi `{"type": "function_call", "id": "fc_...", "call_id": "fc_...", ...}` + `{"type": "function_call_output", ...}`. Gli ID devono iniziare con `fc_`.
- **`pydantic_function_tool()`**: questo helper genera ancora il vecchio formato annidato ed è **non compatibile** con `responses.create()`. Sostituire con definizioni manuali degli strumenti o un wrapper di appiattimento.
- **Multi-turn**: mantenere la cronologia della conversazione nell'app; passare i turni precedenti tramite elementi `input`.
- **Formattazione**: sostituire `response_format` di primo livello di Chat con `text.format` in Responses. Forma canonica: `text={"format": {"type": "json_schema", "name": "Output", "strict": True, "schema": {...}}}`.
- **Elementi di contenuto**: sostituire Chat `content[].type: "text"` con Responses `content[].type: "input_text"` per i turni utente/sistema.
- **Elementi di contenuto immagine**: sostituire Chat `content[].type: "image_url"` con Responses `content[].type: "input_image"`. Il campo `image_url` cambia da un oggetto annidato `{"url": "..."}` a una stringa piatta. Vedi la cheat sheet per esempi prima/dopo.
- **Sforzo di ragionamento**: **migrare `reasoning` solo se esiste già nel codice originale**.
- **Gestione degli errori filtro contenuto**: la struttura del corpo errore è cambiata. Chat Completions usava `error.body["innererror"]["content_filter_result"]` (singolare); Responses API usa `error.body["content_filters"][0]["content_filter_results"]` (plurale, dentro un array). Il codice che accede a `innererror` solleverà `KeyError`. Riscrivere per usare il nuovo percorso.
- **Chiamate HTTP raw**: se l'app chiama direttamente l'API REST Azure OpenAI (tramite `requests`, `httpx`, ecc.) usando `/openai/deployments/{name}/chat/completions?api-version=...`, riscrivere con `/openai/v1/responses`. Il corpo della richiesta cambia: `messages` → `input`, aggiungere `max_output_tokens` e `store: false`, rimuovere il parametro query `api-version`. Il corpo della risposta cambia: `choices[0].message.content` → `output[0].content[0].text` (nota: `output_text` è una proprietà di comodità SDK non presente nel JSON REST grezzo).

---

## Passo 2: Applicare la migrazione

### Note di migrazione (Chat Completions → Responses)

- **Perché migrare**: Responses è l'API unificata per testo, strumenti e streaming; Chat Completions è legacy. Con GPT-5, Responses è obbligatoria per le migliori prestazioni.
- **HTTP**: il endpoint Azure cambia da `/openai/deployments/{name}/chat/completions` a `/openai/v1/responses`.
- **Campi**: `messages` → `input`, `max_tokens` → `max_output_tokens`. `temperature` resta invariato.
- **Formattazione**: `response_format` → `text.format` con un oggetto adeguato.
- **Elementi di contenuto**: sostituire Chat `content[].type: "text"` con Responses `content[].type: "input_text"` per i turni sistema/utente.
- **Elementi di contenuto immagine**: sostituire Chat `content[].type: "image_url"` con Responses `content[].type: "input_image"`. Appiattire il campo `image_url` da `{"image_url": {"url": "..."}}` a `{"image_url": "..."}` (una stringa semplice — URL HTTPS o URI dati `data:image/...;base64,...`).

### Riferimento mappatura parametri

| Chat Completions | Responses API |
|-----------------|---------------|
| `prompt` | `input` |
| `messages` | `input` (array di elementi) |
| `max_tokens` | `max_output_tokens` |
| `response_format` | `text.format` (oggetto) |
| `temperature` | `temperature` (invariato) |
| `stop` | `stop` (invariato) |
| `frequency_penalty` | `frequency_penalty` (invariato) |
| `presence_penalty` | `presence_penalty` (invariato) |
| `tools` / function-calling | `tools` (invariato) |
| `seed` | **Rimuovere** (non supportato) |
| `store` | `store` (impostato a `false`) |
| `content[].type: "text"` | `content[].type: "input_text"` |
| `content[].type: "image_url"` | `content[].type: "input_image"` |
| `"image_url": {"url": "..."}` | `"image_url": "..."` (stringa piatta) |

Per esempi completi prima/dopo, vedere [cheat-sheet.md](./references/cheat-sheet.md).

Per la migrazione dell'infrastruttura di test (mock, snapshot, asserzioni), vedere [test-migration.md](./references/test-migration.md).

Per risoluzione degli errori e problemi comuni, vedere [troubleshooting.md](./references/troubleshooting.md).

---

## Conservazione dati & Stato

- Impostare `store: false` su tutte le richieste Responses.
- Non fare affidamento su ID messaggi precedenti o contesto memorizzato dal server; mantenere lo stato gestito dal client e minimizzare i metadati.

---

## Criteri di Accettazione

### Requisiti a livello di codice (tutti devono passare)

- [ ] Zero riscontri per `rg "chat\.completions\.create|ChatCompletion\.create|Completion\.create"` nei file migrati.
- [ ] Zero riscontri per `rg "AzureOpenAI\(|AsyncAzureOpenAI\("` — tutti i costruttori usano `OpenAI`/`AsyncOpenAI` con endpoint v1.
- [ ] Zero riscontri per `rg "models\.github\.ai|models\.inference\.ai\.azure"` — Rimosse le vie codice GitHub Models.
- [ ] Zero riscontri per `rg "OpenAIChatCompletionClient"` — Il codice MAF 1.0.0+ usa `OpenAIChatClient` (che usa Responses API). Su versioni pre-1.0.0, aggiornare a `agent-framework-openai>=1.0.0`.
- [ ] Tutte le chiamate `ChatOpenAI(...)` includono `use_responses_api=True`.
- [ ] Zero riscontri per `rg "choices\[0\]"` — tutto l'accesso alla risposta usa `resp.output_text` o lo schema output Responses.
- [ ] Nessun `response_format` di primo livello; tutte le uscite strutturate usano `text={"format": {...}}`.
- [ ] `openai>=1.108.1` e `azure-identity` in `requirements.txt` o `pyproject.toml`; dipendenze reinstallate.
- [ ] `store=False` impostato su ogni chiamata `responses.create`.
- [ ] Nessun `api_version` nella costruzione client; `AZURE_OPENAI_API_VERSION` rimosso dai file env e dall'infrastruttura.

### Requisiti infrastrutturali di test (tutti devono passare)

- [ ] Zero riscontri per `rg "ChatCompletionChunk|AsyncCompletions\.create|chat\.completions" tests/`.
- [ ] Zero riscontri per `rg "_azure_ad_token_provider" tests/` — asserzioni aggiornate per verificare `isinstance(client, AsyncOpenAI)` o `base_url`.
- [ ] Zero riscontri per `rg "prompt_filter_results|content_filter_results" tests/` — Rimosse mock filtro specifiche Azure.
- [ ] Le fixture mock usano `kwargs.get("input")` non `kwargs.get("messages")`.
- [ ] Snapshot / file golden aggiornati alla forma streaming Responses (nessun `choices[0]`, `function_call`, `logprobs`, ecc.).
- [ ] `pytest` passa senza errori dopo tutti gli aggiornamenti ai test.

### Requisiti comportamentali (verificare manualmente o tramite test harness)

- [ ] **Completamento base**: `responses.create` non in streaming produce `output_text` non vuoto.
- [ ] **Parità streaming**: se il codice originale usava streaming, il codice migrato esegue streaming ed emette eventi `response.output_text.delta` con delta non vuoti.
- [ ] **Output strutturato**: se si usa `text.format` con `json_schema`, `json.loads(resp.output_text)` riesce e corrisponde allo schema.
- [ ] **Loop chiamate strumenti**: se si usano strumenti, il modello emette chiamate strumenti, l'app le esegue, e la richiesta successiva restituisce un `output_text` finale (nessun loop infinito).
- [ ] **Parità async**: se si usava `AsyncAzureOpenAI`, l'equivalente `AsyncOpenAI` funziona con `await`.
- [ ] **Tasso errori**: nessun nuovo errore 400/401/404 rispetto al baseline pre-migrazione.

### Deliverable

- Il sommario include file modificati, conteggi prima/dopo per i siti di chiamata legacy, e passi successivi.
- Le modifiche sono solo nel working tree (nessun commit).

---

## Requisiti Versione SDK

| Pacchetto | Versione Minima |
|---------|----------------|
| `openai` | `>=1.108.1` |
| `azure-identity` | Ultima (per autenticazione EntraID) |

---

## Riferimenti

- [Cheat Sheet — tutti gli snippet di codice](./references/cheat-sheet.md)
- [Test Migration — mock, snapshot, asserzioni](./references/test-migration.md)
- [Troubleshooting — errori, tabella rischi, insidie](./references/troubleshooting.md)
- [detect_legacy.py — scanner automatizzato](../../../../../.agents/skills/azure-openai-to-responses/scripts/detect_legacy.py)
- [Azure OpenAI Starter Kit](https://aka.ms/openai/start)
- [Documentazione Azure OpenAI Responses API](https://learn.microsoft.com/en-us/azure/ai-foundry/openai/how-to/responses)
- [Ciclo di vita versioni Azure OpenAI API](https://learn.microsoft.com/en-us/azure/ai-foundry/openai/api-version-lifecycle?view=foundry-classic&tabs=python#api-evolution)
- [Riferimento API OpenAI Responses](https://platform.openai.com/docs/api-reference/responses)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:
Questo documento è stato tradotto utilizzando il servizio di traduzione AI [Co-op Translator](https://github.com/Azure/co-op-translator). Sebbene ci impegniamo per garantire la precisione, si prega di notare che le traduzioni automatizzate possono contenere errori o imprecisioni. Il documento originale nella sua lingua nativa deve essere considerato la fonte autorevole. Per informazioni critiche, si raccomanda una traduzione professionale effettuata da un essere umano. Non siamo responsabili per eventuali malintesi o interpretazioni errate derivanti dall’uso di questa traduzione.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->