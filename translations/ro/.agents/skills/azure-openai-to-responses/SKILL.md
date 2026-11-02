---
name: azure-openai-to-responses
license: MIT
---
# Migrarea aplicațiilor Python de la Azure OpenAI Chat Completions la Responses API

> **GHID AUTORITATIV — URMĂRIȚI EXACT**
>
> Această abilitate migrează bazele de cod Python care folosesc Azure OpenAI Chat Completions
> la API-ul unificat Responses. Urmați aceste instrucțiuni cu precizie.
> Nu improvizați maparea parametrilor și nu inventați forme de API.

---

## Declanșatoare

Activați această abilitate când utilizatorul dorește să:
- Migreze o aplicație Python de la Azure OpenAI Chat Completions la Responses API
- Actualizeze utilizarea SDK-ului Python OpenAI la cea mai recentă formă a API-ului pentru Azure OpenAI
- Pregătească cod Python pentru modelele GPT-5 sau mai noi care necesită Responses pe Azure
- Schimbe de la `AzureOpenAI`/`AsyncAzureOpenAI` la clientul standard `OpenAI`/`AsyncOpenAI` cu endpoint-ul v1
- Remedieze avertismentele de depreciere legate de constructorii `AzureOpenAI` sau `api_version`

---

## ⚠️ Compatibilitatea modelului — VERIFICAȚI ÎNTÂI

> **Înainte de migrare, verificați dacă implementarea Azure OpenAI suportă Responses API.**

### 1. Test rapid al implementării (cel mai rapid)

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

> **Notă**: `max_output_tokens` are un **minim de 16** pe Azure OpenAI. Valorile mai mici de 16 returnează eroare 400. Folosiți 50+ pentru testele rapide.

Dacă se returnează 404, modelul din implementare nu suportă încă Responses — verificați referința de mai jos sau redeployați cu un model suportat.

### 2. Verificați modelele disponibile în regiunea dvs. (recomandat)

Rulați instrumentul încorporat de compatibilitate a modelelor pentru a vedea ce este disponibil cu suport Responses API în regiunea dvs. specifică:

```bash
python migrate.py models --subscription YOUR_SUB_ID --location YOUR_REGION
```

Aceasta interoghează Azure ARM live și afișează o matrice de compatibilitate — care modele suportă Responses, output structurat, unelte etc. Folosiți `--filter gpt-5.1,gpt-5.2` pentru a restrânge rezultatele sau `--json` pentru scripting.

### 3. Referință completă a suportului modelelor

- **Interogare live**: `python migrate.py models` (vezi mai sus — specifică regiunii, mereu actualizat)
- **Răsfoire disponibilitate**: [Tabel sumar modele și disponibilitate regiuni](https://learn.microsoft.com/en-us/azure/foundry/foundry-models/concepts/models-sold-directly-by-azure?tabs=global-standard-aoai%2Cglobal-standard&pivots=azure-openai#model-summary-table-and-region-availability)
- **Pornire rapidă & ghid**: **https://aka.ms/openai/start**

### ⚠️ Limitări modele vechi

> **AVERTISMENT**: Modelele vechi (anterioare `gpt-4.1`) s-ar putea să nu suporte complet toate funcțiile Responses API.
>
> Limitări cunoscute pentru modelele vechi:
> - **parametrul `reasoning`**: Nu este suportat pe multe modele fără raționament. Migrați `reasoning` doar dacă era deja prezent în codul original.
> - **parametrul `seed`**: Nu este suportat deloc în Responses API — eliminați din toate cererile.
> - **Output structurat prin `text.format`**: Modelele vechi pot să nu impună fiabil scheme JSON `strict: true`.
> - **Orchestrarea uneltelor**: GPT-5+ orchestrează apelurile uneltelor ca parte a raționamentului intern. Modelele vechi pe Responses funcționează, dar fără această integrare profundă.
> - **Constriângeri temperatură**: La migrarea la `gpt-5`, temperatura trebuie omisă sau setată la `1`. Modelele vechi nu au această constrângere.

### Modelele de raționament serie O (o1, o3-mini, o3, o4-mini)

Modelele serie O au constrângeri unice de parametri. La migrarea aplicațiilor care vizează modelele serie O:

- **`temperature`**: Trebuie să fie `1` (sau omis). Modelele serie O nu acceptă alte valori.
- **`max_completion_tokens` → `max_output_tokens`**: Aplicațiile care folosesc parametrul specific Azure `max_completion_tokens` trebuie să-l schimbe în `max_output_tokens`. Setați valori mari (4096+) deoarece tokenii de raționament contează în limita tokenilor.
- **`reasoning_effort`**: Dacă aplicația folosește `reasoning_effort` (low/medium/high), păstrați-l — Responses API suportă acest parametru pentru modelele serie O.
- **Comportamentul streaming**: Modelele serie O pot reține output-ul până la finalizarea raționamentului înainte de a emite evenimente delta text. Streaming-ul funcționează, dar primul `response.output_text.delta` poate sosi cu o întârziere mai mare decât la modelele GPT.
- **`top_p`**: Nu este suportat pe seria O — eliminați dacă este prezent.
- **Utilizarea uneltelor**: Modelele serie O suportă unelte prin Responses API la fel ca modelele GPT, dar calitatea orchestrării apelurilor către unelte variază după model.

**Acțiune — consiliere proactivă model**: În faza de scanare, verificați ce model vizează aplicația (numele implementărilor, variabile de mediu, configurare). Dacă modelul este anterior lui `gpt-4.1` (nu e gpt-4.1+), anunțați proactiv utilizatorul:
- Migrarea va funcționa pentru text simplu, chat, streaming și unelte pe modelul curent.
- Modelele mai noi (`gpt-5.1`, `gpt-5.2`) oferă orchestrare mai bună a uneltelor, impunere a output-ului structurat, raționament și disponibilitate cross-region.
- Ar trebui să ia în considerare actualizarea implementării când sunt pregătiți — nu blochează migrarea.

Nu blocați și nu refuzați migrarea bazat pe versiunea modelului. Consilierea este informativă.

### GitHub Models NU suportă Responses API

> **GitHub Models (`models.github.ai`, `models.inference.ai.azure.com`) nu suportă Responses API.**

Dacă baza de cod are un traseu GitHub Models (căutați `base_url` indicând spre `models.github.ai` sau `models.inference.ai.azure.com`), **eliminați-l complet** în timpul migrării. Responses API necesită Azure OpenAI, OpenAI, sau un endpoint local compatibil (de ex., Ollama cu suport Responses).

Acțiune la scanare:
- Marcați orice cod GitHub Models pentru eliminare.

---

## Migrarea Framework-ului

Multe aplicații folosesc framework-uri de nivel înalt peste OpenAI. La migrarea acestora, se schimbă API-ul framework-ului, nu doar apelurile OpenAI subiacente.

### Microsoft Agent Framework (MAF)

**Verificați versiunea MAF întâi** — migrarea depinde dacă aveți MAF 1.0.0+ sau o versiune beta/rc pre-1.0.0.

#### MAF 1.0.0+ (agent-framework-openai >= 1.0.0)

`OpenAIChatClient` **folosește deja Responses API** — nu este nevoie de migrare. Dacă baza de cod folosește vechiul `OpenAIChatCompletionClient` (care folosește `chat.completions.create`), înlocuiți-l cu `OpenAIChatClient`.

| Înainte | După |
|--------|-------|
| `from agent_framework.openai import OpenAIChatCompletionClient` | `from agent_framework.openai import OpenAIChatClient` |
| `OpenAIChatCompletionClient(...)` | `OpenAIChatClient(...)` |

Pentru a verifica versiunea: `python -c "import agent_framework_openai; print(agent_framework_openai.__version__)"`

#### MAF pre-1.0.0 (versiuni beta/rc)

În MAF pre-1.0.0, `OpenAIChatClient` folosea Chat Completions. Actualizați la `agent-framework-openai>=1.0.0` unde `OpenAIChatClient` folosește Responses API implicit.

Nu sunt necesare alte modificări — API-urile `Agent` și uneltelor rămân aceleași.

### LangChain (`langchain-openai`)

Adăugați `use_responses_api=True` la `ChatOpenAI()`. De asemenea, actualizați accesul la răspuns de la `.content` la `.text`.

| Înainte | După |
|--------|-------|
| `ChatOpenAI(model=..., base_url=..., api_key=...)` | `ChatOpenAI(model=..., base_url=..., api_key=..., use_responses_api=True)` |
| `result['messages'][-1].content` | `result['messages'][-1].text` |

Pentru exemple complete înainte/după cod, vedeți [cheat-sheet.md](./references/cheat-sheet.md).

---

## Ghid pentru migrarea front-end

> **Responses API este o preocupare server-side.** Migrați backend-ul Python; contractul HTTP al front-end-ului ar trebui să rămână neschimbat, cu excepția cazului când backend-ul este un simplu pas-through — în această situație, luați în considerare adoptarea formei de cerere Responses pentru a elimina un strat de traducere. Dacă front-end-ul apelează direct OpenAI cu o cheie client-side, mutați acele apeluri către backend mai întâi.

### Deprecierea `@microsoft/ai-chat-protocol`

Pachetul npm `@microsoft/ai-chat-protocol` este depreciat și ar trebui înlocuit cu [`ndjson-readablestream`](https://www.npmjs.com/package/ndjson-readablestream). Dacă îl găsiți în front-end:

1. Înlocuiți tagul script CDN:
   ```html
   <!-- Before -->
   <script src="https://cdn.jsdelivr.net/npm/@microsoft/ai-chat-protocol@.../dist/iife/index.js"></script>
   <!-- After -->
   <script src="https://cdn.jsdelivr.net/npm/ndjson-readablestream@1.0.7/dist/ndjson-readablestream.umd.js"></script>
   ```
2. Eliminați instanțierea `AIChatProtocolClient` (`new ChatProtocol.AIChatProtocolClient("/chat")`).
3. Înlocuiți `client.getStreamedCompletion(messages)` cu un apel direct `fetch()` către endpoint-ul de streaming backend.
4. Înlocuiți `for await (const response of result)` cu `for await (const chunk of readNDJSONStream(response.body))`.
5. Actualizați accesul la proprietăți de la `response.delta.content` / `response.error` la `chunk.delta.content` / `chunk.error`.

---

## Obiective

- Numerotați toate locurile din codul Python care apelează Chat Completions sau legacy Completions față de Azure OpenAI.
- Propuneți un plan și o ordine de migrare pentru baza de cod Python.
- Aplicați modificări minimale, sigure pentru a trece la Responses API.
- Actualizați apelanții să consume schema de output Responses; fără wrapper-e de compatibilitate inversă.
- Rulați teste/linter; remediați erorile triviale introduse de migrare.
- Pregătiți seturi mici de modificări revizuibile și oferiți un rezumat final cu diferențe (nu comiteți).

---

## Reguli de siguranță

- Modificați doar fișierele din spațiul de lucru git. Nu scrieți niciodată în afara acestuia.
- Nu păstrați shim-uri de compatibilitate inversă; migrați codul la noua formă a API-ului.
- Nu lăsați comentarii de tranziție sau fișiere de backup.
- Păstrați semanticile de streaming dacă erau folosite anterior; altfel folosiți fără streaming.
- Cereți aprobarea înainte de a rula comenzi sau apeluri de rețea dacă sunteți în modul de aprobare.
- Nu rulați `git add`/`git commit`/`git push`; faceți doar modificări în arborele de lucru.

---

## Pasul 0: Migrarea clientului Azure OpenAI (prerechizită)

Dacă baza de cod folosește constructorii `AzureOpenAI` sau `AsyncAzureOpenAI`, migrați mai întâi la constructorii standard `OpenAI` / `AsyncOpenAI`. Constructorii specifici Azure sunt depozați în `openai>=1.108.1`.

### De ce calea API v1?

Noul endpoint `/openai/v1` folosește clientul standard `OpenAI()` în loc de `AzureOpenAI()`, nu necesită parametrul `api_version` și funcționează identic pe OpenAI și Azure OpenAI. Același cod client este pregătit pentru viitor — nu necesită gestionarea versiunii.

### Schimbări cheie

| Înainte | După |
|--------|-------|
| `AzureOpenAI` | `OpenAI` |
| `AsyncAzureOpenAI` | `AsyncOpenAI` |
| `azure_endpoint` | `base_url` |
| `azure_ad_token_provider` | `api_key` |
| `api_version=...` | Eliminat complet |

### Lista de verificare pentru curățare

- Eliminați argumentul `api_version` din construcția clientului.
- Eliminați variabilele de mediu `AZURE_OPENAI_VERSION` / `AZURE_OPENAI_API_VERSION` din `.env`, setări aplicație și fișiere Bicep/infra.
- Redenumiți `AZURE_OPENAI_CLIENT_ID` → `AZURE_CLIENT_ID` în `.env`, setări aplicație, Bicep/infra, și fixturi de test (convenția standard Azure Identity SDK).
- Asigurați `openai>=1.108.1` în `requirements.txt` sau `pyproject.toml`.

### Migrarea variabilelor de mediu

| Variabilă veche | Acțiune | Note |
|-------------|--------|-------|
| `AZURE_OPENAI_VERSION` | **Eliminați** | Nu mai este nevoie de `api_version` cu endpoint v1 |
| `AZURE_OPENAI_API_VERSION` | **Eliminați** | La fel ca mai sus |
| `AZURE_OPENAI_CLIENT_ID` | **Redenumiți** → `AZURE_CLIENT_ID` | Convenție standard Azure Identity SDK pentru `ManagedIdentityCredential(client_id=...)` |
| `AZURE_OPENAI_ENDPOINT` | **Păstrați** | Încă necesar pentru construcția `base_url` |
| `AZURE_OPENAI_CHAT_DEPLOYMENT` | **Păstrați** | Folosit ca parametru `model` în `responses.create` |
| `AZURE_OPENAI_API_KEY` | **Păstrați** | Folosit ca `api_key` pentru autentificare prin cheie |

Pentru exemple de setup client (sync, async, EntraID, cheie API, multi-tenant), vedeți [cheat-sheet.md](./references/cheat-sheet.md).

---

## Pasul 1: Detectarea locurilor legacy de apel

Rulați scriptul [detect_legacy.py](../../../../../.agents/skills/azure-openai-to-responses/scripts/detect_legacy.py) pentru a găsi toate locurile de apel care necesită migrare:

```bash
python skills/azure-openai-to-responses/scripts/detect_legacy.py .
```

Sau rulați aceste căutări manual — fiecare potrivire este o țintă de migrare:

```bash
# Apeluri API vechi (trebuie rescrise)
rg "chat\.completions\.create"
rg "ChatCompletion\.create"
rg "Completion\.create"

# Constructori Azure client învechiți (trebuie înlocuiți)
rg "AzureOpenAI\("
rg "AsyncAzureOpenAI\("

# Modele de acces pentru forma răspunsului (trebuie actualizate)
rg "choices\[0\]\.message\.content"
rg "choices\[0\]\.delta\.content"
rg "choices\[0\]\.message\.function_call"
rg "choices\[0\]\.message\.tool_calls"

# Definiții de unelte în formatul vechi imbricat (trebuie simplificate)
rg '"function":\s*{\s*"name"'
rg "pydantic_function_tool"

# Rezultatele uneltelor în format vechi (trebuie convertite în function_call_output)
rg '"role":\s*"tool"'
rg '"tool_call_id"'

# Parametri învechiți (trebuie eliminați sau redenumiți)
rg "response_format"
rg "max_tokens\b"        # redenumiți în max_output_tokens
rg "['\"]seed['\"]"      # remove entirely

# Variabile de mediu învechite (curățare)
rg "AZURE_OPENAI_API_VERSION|AZURE_OPENAI_VERSION"
rg "AZURE_OPENAI_CLIENT_ID"  # ar trebui să fie AZURE_CLIENT_ID

# Endpoint-uri modele GitHub (trebuie eliminate — API răspunsuri nesuportat)
rg "models\.github\.ai|models\.inference\.ai\.azure"

# Modele vechi la nivel de framework (trebuie actualizate)
rg "OpenAIChatCompletionClient"  # MAF 1.0.0+: înlocuiți cu OpenAIChatClient
rg "ChatOpenAI\(" | grep -v "use_responses_api"  # LangChain: necesită use_responses_api=True

# Infrastructură de testare (trebuie actualizată)
rg "ChatCompletionChunk|AsyncCompletions\.create" tests/
rg "_azure_ad_token_provider" tests/
rg "prompt_filter_results|content_filter_results" tests/
rg "choices\[0\]" tests/

# Accesare corp eroare filtru conținut (trebuie actualizată — structura s-a schimbat)
rg 'innererror.*content_filter_result|error\.body\["innererror"\]'
rg "content_filter_result\[" # formă veche singulară — acum content_filter_results (plural) în interiorul array-ului content_filters

# Apeluri HTTP brute către endpoint-ul Chat Completions (trebuie actualizat URL-ul)
rg "/openai/deployments/.*/chat/completions"
rg "api-version="
```

### Heuristici (detectare și rescriere)

- **Client Chat Completions**: `client.chat.completions.create` → `client.responses.create(...)`.

- **Constructorii clientului Azure**: `AzureOpenAI(...)` → `OpenAI(base_url=..., api_key=...)`.
- **Instrumente**: convertește definițiile instrumentelor pentru apelare de funcții din formatul încastrat (`{"type": "function", "function": {"name": ...}}`) în formatul plat Responses (`{"type": "function", "name": ...}`); folosește `tool_choice`; returnează rezultatele instrumentelor ca elemente `{"type": "function_call_output", "call_id": ..., "output": ...}` (nu `{"role": "tool", ...}`).
- **Rotiri pentru instrumente**: când modelul returnează apeluri de funcții, adaugă elementele `response.output` la conversație (nu un dicționar manual `{"role": "assistant", "tool_calls": [...]}`), apoi adaugă elemente `function_call_output` pentru fiecare rezultat.
- **Exemple cu instrumente Few-shot**: dacă conversația include exemple hardcodate de apeluri către instrumente, convertește-le în elemente `{"type": "function_call", "id": "fc_...", "call_id": "fc_...", ...}` + `{"type": "function_call_output", ...}`. ID-urile trebuie să înceapă cu `fc_`.
- **`pydantic_function_tool()`**: acest ajutor generează în continuare formatul vechi încastrat și **nu este compatibil** cu `responses.create()`. Înlocuiește cu definiții manuale ale instrumentelor sau un înveliș de aplatizare.
- **Multi-turn**: menține istoricul conversației în aplicație; transmite tururile anterioare prin elemente `input`.
- **Formatare**: înlocuiește `response_format` de top-level din Chat cu `text.format` în Responses. Formă canonică: `text={"format": {"type": "json_schema", "name": "Output", "strict": True, "schema": {...}}}`.
- **Elemente de conținut**: înlocuiește `content[].type: "text"` din Chat cu `content[].type: "input_text"` pentru tururile utilizatorului/sistemului în Responses.
- **Elemente de conținut imagine**: înlocuiește `content[].type: "image_url"` din Chat cu `content[].type: "input_image"` în Responses. Câmpul `image_url` se schimbă dintr-un obiect încastrat `{"url": "..."}` într-un string plat. Consultă fișa de referință pentru exemple înainte/după.
- **Efort de raționament**: **migrează `reasoning` numai dacă există deja în codul original**.
- **Gestionarea erorilor de filtrare conținut**: structura corpului erorii s-a schimbat. Chat Completions folosea `error.body["innererror"]["content_filter_result"]` (singular); Responses API folosește `error.body["content_filters"][0]["content_filter_results"]` (plural, într-un array). Codul care accesează `innererror` va genera `KeyError`. Rescrie pentru a folosi noul traseu.
- **Apeluri HTTP brute**: dacă aplicația apelează direct API-ul REST Azure OpenAI (prin `requests`, `httpx` etc.) folosind `/openai/deployments/{name}/chat/completions?api-version=...`, rescrie la `/openai/v1/responses`. Corpul cererii se schimbă: `messages` → `input`, adaugă `max_output_tokens` și `store: false`, elimină parametrul de interogare `api-version`. Corpul răspunsului se schimbă: `choices[0].message.content` → `output[0].content[0].text` (notă: `output_text` este o proprietate comodă SDK, absentă în JSON-ul REST brut).

---

## Pasul 2: Aplică Migrarea

### Note de migrare (Chat Completions → Responses)

- **De ce să migrezi**: Responses este API-ul unificat pentru text, instrumente și streaming; Chat Completions este învechit. Cu GPT-5, Responses este obligatoriu pentru performanță optimă.
- **HTTP**: punctul final Azure schimbă de la `/openai/deployments/{name}/chat/completions` la `/openai/v1/responses`.
- **Câmpuri**: `messages` → `input`, `max_tokens` → `max_output_tokens`. `temperature` rămâne.
- **Formatare**: `response_format` → `text.format` cu un obiect adecvat.
- **Elemente de conținut**: înlocuiește `content[].type: "text"` din Chat cu `content[].type: "input_text"` în Responses pentru tururile sistem/utilizator.
- **Elemente de conținut imagine**: înlocuiește `content[].type: "image_url"` din Chat cu `content[].type: "input_image"` în Responses. Aplatizează câmpul `image_url` din `{"image_url": {"url": "..."}}` la `{"image_url": "..."}` (un string simplu — fie un URL HTTPS sau un URI de date `data:image/...;base64,...`).

### Referință mapare parametri

| Chat Completions | Responses API |
|-----------------|---------------|
| `prompt` | `input` |
| `messages` | `input` (listă de elemente) |
| `max_tokens` | `max_output_tokens` |
| `response_format` | `text.format` (obiect) |
| `temperature` | `temperature` (neschimbat) |
| `stop` | `stop` (neschimbat) |
| `frequency_penalty` | `frequency_penalty` (neschimbat) |
| `presence_penalty` | `presence_penalty` (neschimbat) |
| `tools` / function-calling | `tools` (neschimbat) |
| `seed` | **Elimină** (nu este suportat) |
| `store` | `store` (setează la `false`) |
| `content[].type: "text"` | `content[].type: "input_text"` |
| `content[].type: "image_url"` | `content[].type: "input_image"` |
| `"image_url": {"url": "..."}` | `"image_url": "..."` (string plat) |

Pentru exemple complete de cod înainte/după, vezi [cheat-sheet.md](./references/cheat-sheet.md).

Pentru migrarea infrastructurii de testare (mock-uri, snapshot-uri, aserțiuni), vezi [test-migration.md](./references/test-migration.md).

Pentru depanarea erorilor și capcanelor, vezi [troubleshooting.md](./references/troubleshooting.md).

---

## Păstrarea datelor și starea

- Setează `store: false` pe toate cererile Responses.
- Nu te baza pe ID-urile mesajelor anterioare sau pe context stocat pe server; păstrează starea gestionată la client și minimizează metadatele.

---

## Criterii de acceptare

### Porți la nivel de cod (toate trebuie să fie verificate)

- [ ] Zero rezultate pentru `rg "chat\.completions\.create|ChatCompletion\.create|Completion\.create"` în fișiere migrate.
- [ ] Zero rezultate pentru `rg "AzureOpenAI\(|AsyncAzureOpenAI\("` — toți constructorii folosesc `OpenAI`/`AsyncOpenAI` cu punctul final v1.
- [ ] Zero rezultate pentru `rg "models\.github\.ai|models\.inference\.ai\.azure"` — căile de cod GitHub Models au fost eliminate.
- [ ] Zero rezultate pentru `rg "OpenAIChatCompletionClient"` — cod MAF 1.0.0+ folosește `OpenAIChatClient` (care folosește Responses API). Înainte de 1.0.0, actualizează la `agent-framework-openai>=1.0.0`.
- [ ] Toate apelurile `ChatOpenAI(...)` includ `use_responses_api=True`.
- [ ] Zero rezultate pentru `rg "choices\[0\]"` — toate accesările răspunsului folosesc `resp.output_text` sau schema de output Responses.
- [ ] Niciun `response_format` de nivel superior; tot output-ul structurat folosește `text={"format": {...}}`.
- [ ] `openai>=1.108.1` și `azure-identity` în `requirements.txt` sau `pyproject.toml`; dependențele reinstalate.
- [ ] `store=False` setează pe fiecare apel `responses.create`.
- [ ] Niciun `api_version` în construcția clientului; `AZURE_OPENAI_API_VERSION` eliminat din fișierele de mediu și infrastructură.

### Porți infrastructură de testare (toate trebuie să fie verificate)

- [ ] Zero rezultate pentru `rg "ChatCompletionChunk|AsyncCompletions\.create|chat\.completions" tests/`.
- [ ] Zero rezultate pentru `rg "_azure_ad_token_provider" tests/` — aserțiunile actualizate să verifice `isinstance(client, AsyncOpenAI)` sau `base_url`.
- [ ] Zero rezultate pentru `rg "prompt_filter_results|content_filter_results" tests/` — mock-urile de filtrare specifice Azure au fost eliminate.
- [ ] Fixture-urile mock folosesc `kwargs.get("input")` nu `kwargs.get("messages")`.
- [ ] Fișierele snapshot / golden actualizate la forma streaming Responses (fără `choices[0]`, `function_call`, `logprobs` etc.).
- [ ] `pytest` trece cu zero erori după toate actualizările testelor.

### Porți comportamentale (verificare manuală sau prin test harness)

- [ ] **Completare de bază**: `responses.create` non-streaming returnează `output_text` nenul.
- [ ] **Paritate streaming**: dacă codul original folosea streaming, codul migrat face streaming și emite evenimente `response.output_text.delta` cu delte nenule.
- [ ] **Output structurat**: dacă se folosește `text.format` cu `json_schema`, `json.loads(resp.output_text)` reușește și corespunde schemei.
- [ ] **Bucle cu apeluri de instrumente**: dacă sunt folosite instrumente, modelul emite apeluri către ele, aplicația le execută, iar cererea follow-up returnează un `output_text` final (fără bucle infinite).
- [ ] **Paritate Async**: dacă s-a folosit `AsyncAzureOpenAI`, echivalentul `AsyncOpenAI` funcționează cu `await`.
- [ ] **Rată erori**: fără erori noi 400/401/404 comparativ cu baseline-ul pre-migrare.

### Livrabile

- Sumar include fișierele editate, numărul punctelor de apel legacy înainte/după, și pașii următori.
- Modificările sunt doar în arborele de lucru (fără commit-uri).

---

## Cerințe versiune SDK

| Pachet | Versiune minimă |
|---------|----------------|
| `openai` | `>=1.108.1` |
| `azure-identity` | Ultima versiune (pentru autentificare EntraID) |

---

## Referințe

- [Fișa de referință — toate fragmentele de cod](./references/cheat-sheet.md)
- [Migrarea testelor — mocks, snapshots, aserțiuni](./references/test-migration.md)
- [Depanare — erori, tabel de riscuri, capcane](./references/troubleshooting.md)
- [detect_legacy.py — scaner automatizat](../../../../../.agents/skills/azure-openai-to-responses/scripts/detect_legacy.py)
- [Azure OpenAI Starter Kit](https://aka.ms/openai/start)
- [Documentație API Azure OpenAI Responses](https://learn.microsoft.com/en-us/azure/ai-foundry/openai/how-to/responses)
- [Ciclul de viață al versiunilor API Azure OpenAI](https://learn.microsoft.com/en-us/azure/ai-foundry/openai/api-version-lifecycle?view=foundry-classic&tabs=python#api-evolution)
- [Referință API OpenAI Responses](https://platform.openai.com/docs/api-reference/responses)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Declinare a responsabilității**:
Acest document a fost tradus folosind serviciul de traducere AI [Co-op Translator](https://github.com/Azure/co-op-translator). În timp ce ne străduim pentru acuratețe, vă rugăm să rețineți că traducerile automate pot conține erori sau inexactități. Documentul original în limba sa nativă trebuie considerat sursa autorizată. Pentru informații critice, se recomandă traducerea profesională realizată de un om. Nu ne asumăm responsabilitatea pentru eventualele neînțelegeri sau interpretări greșite care decurg din utilizarea acestei traduceri.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->