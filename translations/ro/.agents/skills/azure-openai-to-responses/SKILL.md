---
name: azure-openai-to-responses
license: MIT
---
# Migrarea aplicațiilor Python de la Azure OpenAI Chat Completions la Responses API

> **GHID AUTORITAR — URMEAZĂ EXACT**
>
> Această abilitate migrează coduri Python folosind Azure OpenAI Chat Completions
> către API-ul unificat Responses. Urmează aceste instrucțiuni precis.
> Nu improvizați mapările parametrilor și nu inventați forme API.

---

## Declanșatori

Activează această abilitate când utilizatorul dorește să:
- Migreze o aplicație Python de la Azure OpenAI Chat Completions la Responses API
- Actualizeze utilizarea SDK-ului Python OpenAI la ultima formă API pentru Azure OpenAI
- Pregătească cod Python pentru modelele GPT-5 sau mai noi care necesită Responses pe Azure
- Schimbe de la `AzureOpenAI`/`AsyncAzureOpenAI` la clientul standard `OpenAI`/`AsyncOpenAI` cu endpoint-ul v1
- Corecteze avertismente de deprecieri legate de constructorii `AzureOpenAI` sau `api_version`

---

## ⚠️ Compatibilitatea modelului — VERIFICĂ ÎNTÂI

> **Înainte de migrare, verifică dacă implementarea Azure OpenAI suportă Responses API.**

### 1. Test simplu al implementării (cel mai rapid)

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

> **Notă**: `max_output_tokens` are un **minim de 16** pe Azure OpenAI. Valorile sub 16 returnează eroare 400. Folosește 50+ pentru testare rapidă.

Dacă răspunsul este 404, modelul implementării nu suportă încă Responses — consultă referința de mai jos sau redeploy cu un model suportat.

### 2. Verifică modelele disponibile în regiunea ta (recomandat)

Rulează instrumentul de compatibilitate modele încorporat ca să vezi ce este disponibil cu suport Responses API în regiunea ta specifică:

```bash
python migrate.py models --subscription YOUR_SUB_ID --location YOUR_REGION
```

Aceasta interoghează Azure ARM live și afișează o matrice de compatibilitate — ce modele suportă Responses, output structurat, unelte, etc. Folosește `--filter gpt-5.1,gpt-5.2` pentru a restrânge rezultatele sau `--json` pentru scripting.

### 3. Referință completă a suportului modelelor

- **Interogare live**: `python migrate.py models` (vezi mai sus — specific zonei, mereu actualizat)
- **Răsfoiește disponibilitatea**: [Tabel sumar modele și disponibilitate pe regiuni](https://learn.microsoft.com/en-us/azure/foundry/foundry-models/concepts/models-sold-directly-by-azure?tabs=global-standard-aoai%2Cglobal-standard&pivots=azure-openai#model-summary-table-and-region-availability)
- **Ghid rapid & instrucțiuni**: **https://aka.ms/openai/start**

### ⚠️ Limitări ale modelelor vechi

> **ATENȚIE**: Modele mai vechi (ex.: `gpt-4o`, `gpt-4`) pot să nu suporte complet toate funcțiile API-ului Responses.
>
> Limitări cunoscute pentru modelele vechi:
> - **Parametrul `reasoning`**: Nu este suportat pe `gpt-4o-mini`, `gpt-4o` și multe modele fără reasoning. Migrează doar `reasoning` dacă era deja prezent în codul original.
> - **Parametrul `seed`**: Nu este suportat deloc în Responses API — elimină-l din toate cererile.
> - **Output structurat prin `text.format`**: Modelele vechi pot să nu aplice fiabil scheme JSON cu `strict: true`.
> - **Orchestration tool**: GPT-5+ orchestrează apelurile uneltelor ca parte a reasoning-ului intern. Modelele vechi pe Responses funcționează, dar nu au această integrare profundă.
> - **Constrângeri de temperatură**: La migrarea la `gpt-5`, temperatura trebuie omit sau setată la `1`. Modelele vechi nu au această restricție.

### Modele de reasoning seria O (o1, o3-mini, o3, o4-mini)

Modelele seria O au constrângeri specifice de parametri. La migrarea aplicațiilor pentru modelele seria O:

- **`temperature`**: Trebuie să fie `1` (sau omit). Modelele seria O nu acceptă alte valori.
- **`max_completion_tokens` → `max_output_tokens`**: Aplicațiile care folosesc `max_completion_tokens` specific Azure trebuie să treacă la `max_output_tokens`. Pune valori mari (4096+) deoarece tokenii pentru reasoning se scad din limită.
- **`reasoning_effort`**: Dacă aplicația folosește `reasoning_effort` (low/medium/high), păstreaz-o — Responses API suportă acest parametru pentru modelele seria O.
- **Comportament de streaming**: Modelele seria O pot bufferiza output până la finalizarea reasoning-ului înainte să emită evenimente de text delta. Streaming-ul funcționează încă, dar primul `response.output_text.delta` poate veni cu o întârziere mai mare decât modelele GPT.
- **`top_p`**: Nu este suportat pe seria O — elimină dacă este prezent.
- **Utilizarea uneltelor**: Modelele seria O suportă uneltele prin Responses API similar cu modelele GPT, dar calitatea orchestration-ului variază după model.

**Acțiune — sfat proactiv despre model**: În faza de scanare, verifică ce model vizează aplicația (nume implementări, variabile de mediu, config). Dacă modelul este `gpt-4o` sau mai vechi (nu `gpt-4.1+`), spune proactiv utilizatorului:
- Migrarea va funcționa pentru text simplu, chat, streaming și unelte pe modelul actual.
- Modelele mai noi (`gpt-5.1`, `gpt-5.2`) oferă orchestrare unelte îmbunătățită, aplicare output structurat, reasoning și disponibilitate cross-region.
- Ar trebui să ia în considerare upgrade-ul implementării când sunt gata — nu blochează migrarea.

Nu bloca sau refuza migrarea pe baza versiunii modelului. Sfatul este informativ.

### GitHub Models NU suportă Responses API

> **GitHub Models (`models.github.ai`, `models.inference.ai.azure.com`) nu suportă Responses API.**

Dacă codul are o cale GitHub Models (caută `base_url` care arată spre `models.github.ai` sau `models.inference.ai.azure.com`), **elimin-o complet** în migrare. Responses API necesită Azure OpenAI, OpenAI sau un endpoint local compatibil (ex.: Ollama cu suport Responses).

Acțiune în scanare:
- Marchează orice cale GitHub Models pentru eliminare.

---

## Migrarea Framework-ului

Multe aplicații folosesc framework-uri la nivel înalt deasupra OpenAI. La migrarea lor, se schimbă API-ul framework-ului, nu doar apelurile OpenAI de bază.

### Microsoft Agent Framework (MAF)

**Verifică mai întâi versiunea MAF** — migrarea depinde dacă ești pe MAF 1.0.0+ sau pe o versiune beta/rc pre-1.0.0.

#### MAF 1.0.0+ (agent-framework-openai >= 1.0.0)

`OpenAIChatClient` **folosește deja Responses API** — nu trebuie migrat. Dacă codul folosește vechiul `OpenAIChatCompletionClient` (care folosea `chat.completions.create`), înlocuiește-l cu `OpenAIChatClient`.

| Înainte | După |
|--------|-------|
| `from agent_framework.openai import OpenAIChatCompletionClient` | `from agent_framework.openai import OpenAIChatClient` |
| `OpenAIChatCompletionClient(...)` | `OpenAIChatClient(...)` |

Pentru a verifica versiunea: `python -c "import agent_framework_openai; print(agent_framework_openai.__version__)"`

#### MAF pre-1.0.0 (versiuni beta/rc)

În MAF pre-1.0.0, `OpenAIChatClient` folosea Chat Completions. Actualizează la `agent-framework-openai>=1.0.0` unde `OpenAIChatClient` folosește Responses API implicit.

Nu sunt necesare alte modificări — API-ul `Agent` și al instrumentelor rămâne același.

### LangChain (`langchain-openai`)

Adaugă `use_responses_api=True` la `ChatOpenAI()`. Actualizează accesul la răspuns de la `.content` la `.text`.

| Înainte | După |
|--------|-------|
| `ChatOpenAI(model=..., base_url=..., api_key=...)` | `ChatOpenAI(model=..., base_url=..., api_key=..., use_responses_api=True)` |
| `result['messages'][-1].content` | `result['messages'][-1].text` |

Pentru exemple complete înainte/după, vezi [cheat-sheet.md](./references/cheat-sheet.md).

---

## Ghid de migrare frontend

> **Responses API este o preocupare de server.** Migrează backend-ul Python; contractul HTTP al frontend-ului ar trebui să rămână neschimbat, cu excepția cazului când backend-ul este doar un passthrough subțire — atunci ia în considerare adoptarea formei cererii Responses pentru a elimina un strat de traducere. Dacă frontend-ul apelează direct OpenAI cu o cheie client-side, mută acele apeluri întâi în backend.

### Deprecarea `@microsoft/ai-chat-protocol`

Pachetul npm `@microsoft/ai-chat-protocol` este depreciat și ar trebui înlocuit cu [`ndjson-readablestream`](https://www.npmjs.com/package/ndjson-readablestream). Dacă-l găsești în frontend:

1. Înlocuiește tag-ul script CDN:
   ```html
   <!-- Before -->
   <script src="https://cdn.jsdelivr.net/npm/@microsoft/ai-chat-protocol@.../dist/iife/index.js"></script>
   <!-- After -->
   <script src="https://cdn.jsdelivr.net/npm/ndjson-readablestream@1.0.7/dist/ndjson-readablestream.umd.js"></script>
   ```
2. Elimină instanțierea `AIChatProtocolClient` (`new ChatProtocol.AIChatProtocolClient("/chat")`).
3. Înlocuiește `client.getStreamedCompletion(messages)` cu un apel direct `fetch()` către endpoint-ul streaming backend.
4. Înlocuiește `for await (const response of result)` cu `for await (const chunk of readNDJSONStream(response.body))`.
5. Actualizează accesul la proprietăți de la `response.delta.content` / `response.error` la `chunk.delta.content` / `chunk.error`.

---

## Obiective

- Enumerarea tuturor punctelor de apel Python care folosesc Chat Completions sau Completions vechi pe Azure OpenAI.
- Propunerea unui plan și ordonare de migrare pentru codul Python.
- Aplicarea unor modificări sigure, minime pentru schimbarea la Responses API.
- Actualizarea apelanților pentru a consumă schema output-ului Responses; fără învelișuri backward-compatibile.
- Rularea testelor/lint-urilor; corectarea problemelor triviale introduse de migrare.
- Pregătirea unor seturi mici, revizuite de schimbări și oferirea unui sumar final cu dif-uri (fără commit).

---

## Reguli de siguranță

- Modifică doar fișierele din spațiul de lucru git. Nu scrie niciodată în afară.
- Nu păstra shim-uri pentru compatibilitate înapoi; migrează codul la noua formă API.
- Nu lăsa comentarii de tranziție sau fișiere de backup.
- Păstrează semanticile streaming dacă au fost folosite anterior; altfel folosește non-streaming.
- Cere aprobare înainte de a rula comenzi sau apeluri de rețea dacă ești în modul de aprobare.
- Nu rula `git add`/`git commit`/`git push`; generează doar modificări în arborele de lucru.

---

## Pasul 0: Migrarea clientului Azure OpenAI (prerechizită)

Dacă codul folosește constructorii `AzureOpenAI` sau `AsyncAzureOpenAI`, migrează mai întâi la constructorii standard `OpenAI` / `AsyncOpenAI`. Constructorii specifici Azure sunt depreciate în `openai>=1.108.1`.

### De ce endpoint-ul v1 API?

Noul endpoint `/openai/v1` folosește clientul standard `OpenAI()` în loc de `AzureOpenAI()`, nu necesită parametrul `api_version` și funcționează identic pe OpenAI și Azure OpenAI. Același cod client e pregătit pentru viitor — nu e nevoie de gestionare versiuni.

### Schimbări cheie

| Înainte | După |
|--------|-------|
| `AzureOpenAI` | `OpenAI` |
| `AsyncAzureOpenAI` | `AsyncOpenAI` |
| `azure_endpoint` | `base_url` |
| `azure_ad_token_provider` | `api_key` |
| `api_version=...` | Elimină complet |

### Lista de verificare curățare

- Elimină argumentul `api_version` din construcția clientului.
- Elimină variabilele de mediu `AZURE_OPENAI_VERSION` / `AZURE_OPENAI_API_VERSION` din `.env`, setări app și fișiere Bicep/infra.
- Redenumește `AZURE_OPENAI_CLIENT_ID` → `AZURE_CLIENT_ID` în `.env`, setări app, Bicep/infra și în fixture-uri de test (convenție standard Azure Identity SDK).
- Asigură `openai>=1.108.1` în `requirements.txt` sau `pyproject.toml`.

### Migrarea variabilelor de mediu

| Var env vechi | Acțiune | Note |
|-------------|--------|-------|
| `AZURE_OPENAI_VERSION` | **Elimină** | Nu mai trebuie `api_version` cu endpoint v1 |
| `AZURE_OPENAI_API_VERSION` | **Elimină** | La fel ca mai sus |
| `AZURE_OPENAI_CLIENT_ID` | **Redenumește** → `AZURE_CLIENT_ID` | Convenție standard Azure Identity SDK pentru `ManagedIdentityCredential(client_id=...)` |
| `AZURE_OPENAI_ENDPOINT` | **Păstrează** | Încă necesar pentru construcția `base_url` |
| `AZURE_OPENAI_CHAT_DEPLOYMENT` | **Păstrează** | Folosit ca parametru `model` la `responses.create` |
| `AZURE_OPENAI_API_KEY` | **Păstrează** | Folosit ca `api_key` pentru autentificare bazată pe cheie |

Pentru exemple de cod setup client (sync, async, EntraID, API key, multi-tenant), vezi [cheat-sheet.md](./references/cheat-sheet.md).

---

## Pasul 1: Detectează locurile de apel vechi

Rulează scriptul [detect_legacy.py](../../../../../.agents/skills/azure-openai-to-responses/scripts/detect_legacy.py) pentru a găsi toate locurile de apel ce necesită migrare:

```bash
python skills/azure-openai-to-responses/scripts/detect_legacy.py .
```

Sau rulează aceste căutări manual — fiecare potrivire este o țintă de migrare:

```bash
# Apeluri API moștenite (trebuie rescrise)
rg "chat\.completions\.create"
rg "ChatCompletion\.create"
rg "Completion\.create"

# Constructori învechiți ai clientului Azure (trebuie înlocuiți)
rg "AzureOpenAI\("
rg "AsyncAzureOpenAI\("

# Modele de acces la structura răspunsului (trebuie actualizate)
rg "choices\[0\]\.message\.content"
rg "choices\[0\]\.delta\.content"
rg "choices\[0\]\.message\.function_call"
rg "choices\[0\]\.message\.tool_calls"

# Definiții de instrumente în format vechi imbricat (trebuie aplatizate)
rg '"function":\s*{\s*"name"'
rg "pydantic_function_tool"

# Rezultate ale instrumentelor în format vechi (trebuie convertite în function_call_output)
rg '"role":\s*"tool"'
rg '"tool_call_id"'

# Parametri învechiți (trebuie eliminați sau redenumiți)
rg "response_format"
rg "max_tokens\b"        # redenumește în max_output_tokens
rg "['\"]seed['\"]"      # remove entirely

# Variabile de mediu învechite (curățare)
rg "AZURE_OPENAI_API_VERSION|AZURE_OPENAI_VERSION"
rg "AZURE_OPENAI_CLIENT_ID"  # ar trebui să fie AZURE_CLIENT_ID

# Endpoint-uri GitHub Models (trebuie eliminate — API pentru răspunsuri nu este suportat)
rg "models\.github\.ai|models\.inference\.ai\.azure"

# Modele moștenite la nivel de framework (trebuie actualizate)
rg "OpenAIChatCompletionClient"  # MAF 1.0.0+: înlocuiește cu OpenAIChatClient
rg "ChatOpenAI\(" | grep -v "use_responses_api"  # LangChain: necesită use_responses_api=True

# Infrastructură de testare (trebuie actualizată)
rg "ChatCompletionChunk|AsyncCompletions\.create" tests/
rg "_azure_ad_token_provider" tests/
rg "prompt_filter_results|content_filter_results" tests/
rg "choices\[0\]" tests/

# Acces la corpul erorii filtrului de conținut (trebuie actualizat — structura s-a schimbat)
rg 'innererror.*content_filter_result|error\.body\["innererror"\]'
rg "content_filter_result\[" # formă veche singulară — acum content_filter_results (plural) în interiorul matricei content_filters

# Apeluri HTTP brute către endpoint-ul Chat Completions (trebuie actualizat URL-ul)
rg "/openai/deployments/.*/chat/completions"
rg "api-version="
```

### Euristici (detectează și rescrie)

- **Client Chat Completions**: `client.chat.completions.create` → `client.responses.create(...)`.

- **Constructori client Azure**: `AzureOpenAI(...)` → `OpenAI(base_url=..., api_key=...)`.
- **Unelte**: convertiți definițiile instrumentelor pentru apel funcțional din formatul imbricat (`{"type": "function", "function": {"name": ...}}`) în format plat Responses (`{"type": "function", "name": ...}`); folosiți `tool_choice`; returnați rezultatele uneltelor ca elemente `{"type": "function_call_output", "call_id": ..., "output": ...}` (nu `{"role": "tool", ...}`).
- **Parcurgeri-unelte**: când modelul returnează apeluri funcționale, adăugați elementele `response.output` în conversație (nu un manual dict `{"role": "assistant", "tool_calls": [...]}`), apoi adăugați elementele `function_call_output` pentru fiecare rezultat.
- **Exemple unelte few-shot**: dacă conversația include exemple fix codificate de apeluri de unelte, convertiți-le în elemente `{"type": "function_call", "id": "fc_...", "call_id": "fc_...", ...}` + `{"type": "function_call_output", ...}`. ID-urile trebuie să înceapă cu `fc_`.
- **`pydantic_function_tool()`**: acest ajutor încă generează formatul vechi imbricat și **nu este compatibil** cu `responses.create()`. Înlocuiți cu definiții manuale de unelte sau cu un wrapper de aplatizare.
- **Multi-turn**: mențineți istoricul conversației în aplicație; transmiteți runde anterioare prin elemente `input`.
- **Formatare**: înlocuiți `response_format` de nivel superior din Chat cu `text.format` în Responses. Forma canonică: `text={"format": {"type": "json_schema", "name": "Output", "strict": True, "schema": {...}}}`.
- **Elemente conținut**: înlocuiți Chat `content[].type: "text"` cu Responses `content[].type: "input_text"` pentru turele utilizator/sistem.
- **Elemente conținut imagine**: înlocuiți Chat `content[].type: "image_url"` cu Responses `content[].type: "input_image"`. Câmpul `image_url` trece de la un obiect imbricat `{"url": "..."}` la un string plat. Consultați fișa de referință pentru exemple înainte/după.
- **Efort raționalizare**: **migrați `reasoning` doar dacă există deja în codul original**.
- **Gestionare erori filtru conținut**: structura corpului erorii s-a schimbat. Chat Completions folosea `error.body["innererror"]["content_filter_result"]` (singular); Responses API folosește `error.body["content_filters"][0]["content_filter_results"]` (plural, într-un vector). Codul care accesează `innererror` va genera `KeyError`. Rescrieți pentru a folosi noul drum.
- **Apeluri HTTP brute**: dacă aplicația apelează direct REST API Azure OpenAI (prin `requests`, `httpx` etc.) folosind `/openai/deployments/{name}/chat/completions?api-version=...`, rescrieți la `/openai/v1/responses`. Corpul cererii se schimbă: `messages` → `input`, adăugați `max_output_tokens` și `store: false`, eliminați parametru query `api-version`. Corpul răspunsului se schimbă: `choices[0].message.content` → `output[0].content[0].text` (notă: `output_text` este o proprietate convenabilă SDK, absentă în JSON REST brut).

---

## Pasul 2: Aplicați Migrarea

### Notițe migrare (Chat Completions → Responses)

- **De ce să migrați**: Responses este API-ul unificat pentru text, unelte și streaming; Chat Completions este moștenire. Cu GPT-5, Responses este obligatoriu pentru performanță maximă.
- **HTTP**: endpoint-ul Azure se schimbă de la `/openai/deployments/{name}/chat/completions` la `/openai/v1/responses`.
- **Câmpuri**: `messages` → `input`, `max_tokens` → `max_output_tokens`. `temperature` rămâne aceeași.
- **Formatare**: `response_format` → `text.format` cu un obiect corect.
- **Elemente conținut**: Înlocuiți Chat `content[].type: "text"` cu Responses `content[].type: "input_text"` pentru turele sistem/utilizator.
- **Elemente conținut imagine**: Înlocuiți Chat `content[].type: "image_url"` cu Responses `content[].type: "input_image"`. Aplatizați câmpul `image_url` de la `{"image_url": {"url": "..."}}` la `{"image_url": "..."}` (un string simplu — fie URL HTTPS fie URI de date `data:image/...;base64,...`).

### Referință mapare parametri

| Chat Completions | Responses API |
|-----------------|---------------|
| `prompt` | `input` |
| `messages` | `input` (vector de elemente) |
| `max_tokens` | `max_output_tokens` |
| `response_format` | `text.format` (obiect) |
| `temperature` | `temperature` (nemodificat) |
| `stop` | `stop` (nemodificat) |
| `frequency_penalty` | `frequency_penalty` (nemodificat) |
| `presence_penalty` | `presence_penalty` (nemodificat) |
| `tools` / apel funcțional | `tools` (nemodificat) |
| `seed` | **Eliminați** (nesuportat) |
| `store` | `store` (setat la `false`) |
| `content[].type: "text"` | `content[].type: "input_text"` |
| `content[].type: "image_url"` | `content[].type: "input_image"` |
| `"image_url": {"url": "..."}` | `"image_url": "..."` (string plat) |

Pentru exemple complete cod înainte/după, consultați [cheat-sheet.md](./references/cheat-sheet.md).

Pentru migrarea infrastructurii test (mocks, snapshot-uri, aserțiuni), vedeți [test-migration.md](./references/test-migration.md).

Pentru depanarea erorilor și capcanelor, consultați [troubleshooting.md](./references/troubleshooting.md).

---

## Retenția datelor & Starea

- Setează `store: false` pe toate cererile Responses.
- Nu vă bazați pe ID-uri de mesaje anterioare sau context stocat pe server; mențineți starea gestionată de client și minimizați metadatele.

---

## Criterii de acceptare

### Condiții la nivel de cod (toate trebuie să treacă)

- [ ] Zero rezultate la căutarea `rg "chat\.completions\.create|ChatCompletion\.create|Completion\.create"` în fișierele migrate.
- [ ] Zero rezultate la căutarea `rg "AzureOpenAI\(|AsyncAzureOpenAI\("` — toți constructorii folosesc `OpenAI`/`AsyncOpenAI` cu endpoint v1.
- [ ] Zero rezultate la căutarea `rg "models\.github\.ai|models\.inference\.ai\.azure"` — căile cod GitHub Models eliminate.
- [ ] Zero rezultate la căutarea `rg "OpenAIChatCompletionClient"` — cod MAF 1.0.0+ folosește `OpenAIChatClient` (care folosește Responses API). Înainte de 1.0.0, upgradați la `agent-framework-openai>=1.0.0`.
- [ ] Toate apelurile `ChatOpenAI(...)` includ `use_responses_api=True`.
- [ ] Zero rezultate la căutarea `rg "choices\[0\]"` — accesul răspunsurilor folosește `resp.output_text` sau schema Responses output.
- [ ] Nu există `response_format` la nivel superior; tot output-ul structurat folosește `text={"format": {...}}`.
- [ ] `openai>=1.108.1` și `azure-identity` în `requirements.txt` sau `pyproject.toml`; dependențele sunt reinstalate.
- [ ] `store=False` setat pe fiecare apel `responses.create`.
- [ ] Fără `api_version` în construcția clientului; `AZURE_OPENAI_API_VERSION` eliminat din fișierele de mediu și infra.

### Condiții infrastructură test (toate trebuie să treacă)

- [ ] Zero rezultate la căutarea `rg "ChatCompletionChunk|AsyncCompletions\.create|chat\.completions" tests/`.
- [ ] Zero rezultate la căutarea `rg "_azure_ad_token_provider" tests/` — aserțiunile actualizate să verifice `isinstance(client, AsyncOpenAI)` sau `base_url`.
- [ ] Zero rezultate la căutarea `rg "prompt_filter_results|content_filter_results" tests/` — mocks de filtre specifice Azure eliminate.
- [ ] Fixture-urile mock folosesc `kwargs.get("input")` nu `kwargs.get("messages")`.
- [ ] Snapshot-urile / fișierele golden actualizate la forma streaming Responses (fără `choices[0]`, `function_call`, `logprobs`, etc.).
- [ ] `pytest` rulează fără eșecuri după toate actualizările testelor.

### Condiții comportamentale (verificare manuală sau prin test harness)

- [ ] **Completarie basică**: `responses.create` non-streaming returnează `output_text` nenul.
- [ ] **Paritate streaming**: dacă codul original folosea streaming, codul migrat face streaming și emite evenimente `response.output_text.delta` cu delta nenulă.
- [ ] **Output structurat**: dacă folosește `text.format` cu `json_schema`, `json.loads(resp.output_text)` reușește și corespunde schemei.
- [ ] **Loop apel unelte**: dacă uneltele sunt folosite, modelul emite apeluri unelte, aplicația le execută, și cererea ulterioară returnează un `output_text` final (nu loop infinit).
- [ ] **Paritate async**: dacă a fost folosit `AsyncAzureOpenAI`, echivalentul `AsyncOpenAI` funcționează cu `await`.
- [ ] **Rată erori**: fără erori noi 400/401/404 comparativ cu baseline-ul pre-migrare.

### Livrabile

- Rezumat include fișierele editate, numărul de situri apel pre/post migrare, și pașii următori.
- Modificările sunt doar în working-tree (fără commit-uri).

---

## Cerințe versiune SDK

| Pachet | Versiune Minimă |
|---------|----------------|
| `openai` | `>=1.108.1` |
| `azure-identity` | Ultima (pentru autentificare EntraID) |

---

## Referințe

- [Fișă de referință — toate snippet-urile de cod](./references/cheat-sheet.md)
- [Migrare test — mocks, snapshot-uri, aserțiuni](./references/test-migration.md)
- [Depanare — erori, tabel risc, capcane](./references/troubleshooting.md)
- [detect_legacy.py — scaner automatizat](../../../../../.agents/skills/azure-openai-to-responses/scripts/detect_legacy.py)
- [Azure OpenAI Starter Kit](https://aka.ms/openai/start)
- [Documentație Azure OpenAI Responses API](https://learn.microsoft.com/en-us/azure/ai-foundry/openai/how-to/responses)
- [Ciclul de viață versiune API Azure OpenAI](https://learn.microsoft.com/en-us/azure/ai-foundry/openai/api-version-lifecycle?view=foundry-classic&tabs=python#api-evolution)
- [Referință OpenAI Responses API](https://platform.openai.com/docs/api-reference/responses)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Declinare a responsabilității**:
Acest document a fost tradus folosind serviciul de traducere AI [Co-op Translator](https://github.com/Azure/co-op-translator). În timp ce ne străduim pentru acuratețe, vă rugăm să rețineți că traducerile automate pot conține erori sau inexactități. Documentul original în limba sa nativă trebuie considerat sursa autorizată. Pentru informații critice, se recomandă traducerea profesională realizată de un om. Nu ne asumăm responsabilitatea pentru eventualele neînțelegeri sau interpretări greșite care decurg din utilizarea acestei traduceri.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->