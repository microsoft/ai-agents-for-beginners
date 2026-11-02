# Istoricul modificărilor

Toate modificările notabile ale cursului **AI Agents for Beginners** sunt documentate în acest fișier.

## [Lansat] — 2026-07-14

Această lansare mută cursul de pe două modele nou-depreciate, migrează caietele rămase ale lecțiilor către API-ul stabil Microsoft Agent Framework și validează caietele Python împotriva unei implementări live Microsoft Foundry.

### Modificat

- **Mutat de pe modelele depreciate (`gpt-4.1` / `gpt-4.1-mini` → `gpt-5-mini`).** Atât `gpt-4.1`, cât și `gpt-4.1-mini` sunt acum depreciate (data oficială de retragere **14 octombrie 2026**). Înlocuite toate referințele din curs (documentație, `.env.example`, caiete Python/.NET și exemple) cu `gpt-5-mini` care nu este depreciat. Exemplul de rutare a modelului din Lecția 16 păstrează un contrast mic/mare folosind `gpt-5-nano` (mic) și `gpt-5-mini` (mare). Fișierele terțe vândute ([15-browser-use/llms.txt](../../15-browser-use/llms.txt)), textul istoric GitHub Models și notele de capacitate ale skill-ului `azure-openai-to-responses` au fost lăsate intenționat neschimbate.
- **Notebook-ul Lecția 14 handoff migrează la API-ul stabil.** [14-handoff.ipynb](./14-microsoft-agent-framework/code-samples/14-handoff.ipynb) folosește acum `agent_framework.orchestrations.HandoffBuilder` cu `.with_start_agent(...)`, `HandoffAgentUserRequest.create_response(...)`, streaming bazat pe `event.type` și `FoundryChatClient` (înlocuind simbolurile eliminate pre-1.0 `HandoffBuilder`/`ChatMessage`/`RequestInfoEvent`).
- **Notebook-ul Lecția 14 human-in-the-loop migrează la API-ul stabil.** [14-human-loop.ipynb](./14-microsoft-agent-framework/code-samples/14-human-loop.ipynb) pune acum pauză prin `ctx.request_info(...)` + `@response_handler` (înlocuind `RequestInfoExecutor` / `RequestInfoMessage` / `RequestResponse` eliminate), construiește cu `WorkflowBuilder(start_executor=..., output_executors=[...])`, conduce output structurat prin `default_options={"response_format": ...}`, și folosește un răspuns scriptat astfel încât caietul să ruleze fără supraveghere (fără blocarea `input()`).
- **Configurarea mediului** ([.env.example](../../.env.example)): schimbate numele implementărilor modelului la `gpt-5-mini`; adăugate `AZURE_AI_SMALL_MODEL` / `AZURE_AI_LARGE_MODEL` (rutare Lecția 16) și `AZURE_OPENAI_CHAT_DEPLOYMENT_NAME` care lipsea anterior (Lecția 15 utilizarea browser-ului).
- **Dependențe** ([requirements.txt](../../requirements.txt)): fixate versiunile pentru `agent-framework`, `agent-framework-foundry` și `agent-framework-openai` la `~=1.10.0` pentru un set auto-consistent și validat (versiunea 1.11.0 introduce schimbări de rupere experimentale în suprafețele folosite de aceste lecții).

### Note și limitări cunoscute

- **Validat împotriva unei implementări live Microsoft Foundry.** Caietele Python au fost executate headless cu `nbconvert` împotriva unui proiect Microsoft Foundry folosind `gpt-5-mini` (și `gpt-5-nano` pentru rutarea din Lecția 16). Implementați modele echivalente ne-depreciate în propriul proiect; caietele citesc numele implementării din `AZURE_AI_MODEL_DEPLOYMENT_NAME` / `AZURE_OPENAI_DEPLOYMENT`.
- **Unele lecții încă necesită resurse suplimentare.** Lecția 05 necesită Azure AI Search; fluxul de lucru de ground Bing din Lecția 08 (`04.python-agent-framework-workflow-aifoundry-condition.ipynb`) are nevoie de o conexiune Bing și unelte găzduite de Microsoft Foundry Agent Service; Lecțiile 13 (Cognee) și 17 (Foundry Local) au nevoie de propriile runtime-uri.

## [Lansat] — 2026-07-13

Această lansare adaugă două lecții noi care completează arcul de implementare — scalarea agenților la Microsoft Foundry și până la o singură stație de lucru — plus un pipeline de testare rapidă, navigare actualizată a cursului, noi competențe pentru cursanți și branding actualizat.

### Adăugat

- **Lecția 16 — Implementarea agenților scalabili cu Microsoft Foundry.** Lecție nouă [16-deploying-scalable-agents/README.md](./16-deploying-scalable-agents/README.md) și caiet executabil [16-python-agent-framework.ipynb](./16-deploying-scalable-agents/code_samples/16-python-agent-framework.ipynb) care construiesc un agent de suport clienți de producție (unelte, RAG, memorie, rutare model, caching răspunsuri, aprobare umană, poartă de evaluare și trasare OpenTelemetry), cu diagrame Mermaid pentru dezvoltare/implementare/runtime, un test de cunoștințe, o temă și o provocare.
- **Lecția 17 — Crearea agenților AI locali cu Foundry Local și Qwen.** Lecție nouă [17-creating-local-ai-agents/README.md](./17-creating-local-ai-agents/README.md) și caiet [17-local-agent-foundry-local.ipynb](./17-creating-local-ai-agents/code_samples/17-local-agent-foundry-local.ipynb) care construiesc un asistent ingineresc complet pe dispozitiv (apeluri de funcții Qwen prin Foundry Local, unelte sandboxed de fișiere, RAG local cu Chroma, MCP local opțional), cu diagrame pentru local-only / local-RAG / apelare unelte, un test de cunoștințe, o temă și o provocare.
- **Pipeline de testare rapidă.** Flux de lucru nou [AI Smoke Test](https://github.com/marketplace/actions/ai-smoke-test) [.github/workflows/smoke-test.yml](../../.github/workflows/smoke-test.yml) plus cataloage pe lecții sub [tests/](./tests/README.md) pentru agenții implementabili în Lecțiile 01, 04, 05 și 16, cu un README index care mapează fiecare catalog la lecția și numele agentului găzduit. Lecția 16 primește o secțiune „Validarea unui agent implementat cu teste rapide”; Lecțiile 01/04/05 primesc o indicație opțională pentru testarea rapidă.
- **Competențe pentru cursanți.** Noi competențe Agent sub `.agents/skills/`: [deploying-scalable-agents](./.agents/skills/deploying-scalable-agents/SKILL.md), [local-ai-agents](./.agents/skills/local-ai-agents/SKILL.md) (împachetând ghidajul din Lecția 16 și 17), și [testing-course-samples](./.agents/skills/testing-course-samples/SKILL.md) (cum să validezi exemplele de caiete împotriva unei implementări live Microsoft Foundry / Azure OpenAI).
- **Rulant de validare a caietelor.** Nou [scripts/validate-notebooks.ps1](../../scripts/validate-notebooks.ps1) care execută fiecare caiet Python headless cu `nbconvert` și afișează o matrice PASS/FAIL (plus `results.json`). Detectează automat rădăcina repo-ului și Python, exclude implicit caietele non-curs (`.venv`, `site-packages`, `translations`, asset-uri sablon skill) și caietele `.NET`, și suportă `-Filter`, `-Timeout`, `-List`, `-IncludeDotnet` și `-Python`.
- **Navigare curs.** Adăugate linkuri Lecție Anterioară/Următoare pentru Lecțiile 11–15 (lipsă anterior) astfel încât întregul curs se leagă 00 → 18 în ambele direcții.
- **Miniaturi noi.** Miniaturi ale lecțiilor pentru Lecțiile 16 și 17, plus o imagine socială a repository-ului reîmprospătată [images/repo-thumbnailv3.png](./images/repo-thumbnailv3.png) (anunțând cele două lecții noi și URL-ul `aka.ms/ai-agents-beginners`).
- **Dependențe** ([requirements.txt](../../requirements.txt)): adăugat `foundry-local-sdk` și `chromadb` pentru Lecția 17.

### Modificat

- **Tabelul principal din [README.md](./README.md)**: Lecțiile 16 și 17 se leagă acum la conținutul lor (anterior „În curând”); imaginea repository-ului actualizată la `repo-thumbnailv3.png`.
- **[STUDY_GUIDE.md](./STUDY_GUIDE.md)**: adăugate Lecțiile 16 și 17 în ghidul lecție cu lecție și căile de învățare, plus o secțiune „Validarea agenților implementați cu teste rapide”.
- **[AGENTS.md](./AGENTS.md)**: actualizat numărul/descreția lecțiilor (00–18), adăugată o secțiune de validare pentru testarea rapidă, plus exemple de denumire a sample-urilor pentru Lecțiile 16/17.
- **[18-securing-ai-agents/README.md](./18-securing-ai-agents/README.md)**: „Lecția Anterioară” indică acum Lecția 17 (în loc de Lecția 15), închizând lanțul.
- **Referințe standardizate la modele ne-depreciate.** Înlocuite toate referințele `gpt-4o` / `gpt-4o-mini` în curs (documentație, `.env.example`, caiete Python/.NET și exemple) cu `gpt-4.1-mini` — `gpt-4o` (toate versiunile) va fi retras în 2026. Exemplul de rutare model din Lecția 16 păstrează contrastul mic/mare folosind `gpt-4.1-mini` (mic) și `gpt-4.1` (mare). Caietele Python selectează acum modelul din variabilele de mediu (`AZURE_AI_MODEL_DEPLOYMENT_NAME` / `AZURE_OPENAI_DEPLOYMENT`) în loc să aibă numele modelului hardcodat.

### Note și limitări cunoscute

- **Nu au fost executate împotriva Azure live.** Caietele lecțiilor noi sunt exemple educaționale; rulați-le și validați-le în propriul setup Microsoft Foundry / Foundry Local. Fluxul de lucru pentru testarea rapidă necesită să implementați agentul lecției și să configurați secrete Azure OIDC (`AZURE_CLIENT_ID`, `AZURE_TENANT_ID`, `AZURE_SUBSCRIPTION_ID`) cu rolul **Azure AI User** în scope-ul proiectului Foundry.
- **Lecția 17 este doar locală.** Nu are punct final Foundry Responses, deci acțiunea testării rapide nu se aplică; validați rulând caietul pe stația dumneavoastră de lucru.

## [Lansat] — 2026-07-06

Această lansare migrează cursul la **Azure OpenAI Responses API**, standardizează denumirile produsului pentru **Microsoft Foundry** și **Microsoft Agent Framework (MAF)**, retrage GitHub Models, actualizează versiunile SDK, și adaugă conținut nou despre modele locale și găzduirea altor framework-uri pe Foundry.

### Adăugat

- **Skill de migrare** — Instalată Agent Skill [`azure-openai-to-responses`](./.agents/skills/azure-openai-to-responses/SKILL.md) (din [Azure-Samples/azure-openai-to-responses](https://github.com/Azure-Samples/azure-openai-to-responses)) sub `.agents/skills/`, inclusiv referințele sale și scriptul scanner.
- **Foundry Local (rulează modele pe dispozitiv)** — Secțiune nouă "Alternative Provider: Foundry Local" în [00-course-setup/README.md](./00-course-setup/README.md) care acoperă instalarea (`winget` / `brew`), `foundry model run`, `foundry-local-sdk`, și conectarea `FoundryLocalManager` la Microsoft Agent Framework prin `OpenAIChatClient`.
- **Găzduirea agenților LangChain / LangGraph pe Microsoft Foundry** — Secțiune nouă în [14-microsoft-agent-framework/README.md](./14-microsoft-agent-framework/README.md) plus un exemplu executabil [14-langchain-hosted-agent.py](../../14-microsoft-agent-framework/code-samples/14-langchain-hosted-agent.py) folosind `langchain-azure-ai[hosting]` și `ResponsesHostServer` (protocolul `/responses`), bazat pe [Microsoft Learn](https://learn.microsoft.com/azure/foundry/how-to/develop/langchain-hosted-agents).
- **Microsoft Project Opal** — Secțiune nouă "Exemplu din viața reală: Microsoft Project Opal" în [15-browser-use/README.md](./15-browser-use/README.md) care plasează Opal ca un agent enterprise pentru utilizarea computerului și îl mapează la conceptele cursului (human-in-the-loop, încredere/securitate, planificare, Skills).
- **Al doilea exemplu Python din Lecția 02** — Adăugat [02-python-agent-framework-azure-openai.ipynb](./02-explore-agentic-frameworks/code_samples/02-python-agent-framework-azure-openai.ipynb) (vezi „Modificat” — migrat din fostul caiet Semantic Kernel) și legat în README-ul lecției.
- Secțiunea **Models and Providers** adăugată în [STUDY_GUIDE.md](./STUDY_GUIDE.md).

### Modificat

- **Chat Completions → Responses API (Python).** Exemplele care apelau modelul direct au fost migrate de la Chat Completions la Responses API (`client.responses.create(input=..., store=False)`, `resp.output_text`), folosind clientul `OpenAI` împotriva endpointului stabil Azure OpenAI `/openai/v1/` (fără `api_version`). Exemple afectate includ:
  - [06-building-trustworthy-agents/code_samples/06-system-message-framework.ipynb](./06-building-trustworthy-agents/code_samples/06-system-message-framework.ipynb)
  - [06-building-trustworthy-agents/code_samples/06-human-in-the-loop.ipynb](./06-building-trustworthy-agents/code_samples/06-human-in-the-loop.ipynb)
  - [04-tool-use/README.md](./04-tool-use/README.md) — prezentarea completă a apelării funcțiilor (schema uneltelor adaptată la formatul Responses, rezultatele uneltelor returnate ca `function_call_output`, `max_output_tokens`, etc.).

- **GitHub Models → Azure OpenAI.** GitHub Models este învechit (se retrage în **iulie 2026**) și nu suportă API-ul Responses. Toate traseele de cod pentru GitHub Models au fost convertite la Azure OpenAI / Microsoft Foundry în exemplele Python și .NET:
  - Python: caietele de notițe pentru lecția 08 workflow (`01`–`03`), lecția 14 (`14-handoff`, `14-human-loop`, `hotel_booking_workflow_sample.py`).
  - .NET: `01`–`04`, `07`, `08` `*-dotnet-agent-framework.cs` + documentațiile companion `.md`, și caietele de notițe / `.md` .NET pentru workflow-ul lecției 08 (`01`–`03`) folosesc acum `AzureOpenAIClient(...).GetOpenAIResponseClient(deployment).CreateAIAgent(...)` cu `AzureCliCredential`.
- **Semantic Kernel → Microsoft Agent Framework.** Fostul `02-semantic-kernel.ipynb` a fost rescris pentru a folosi Microsoft Agent Framework cu Azure OpenAI (API Responses) și redenumit în `02-python-agent-framework-azure-openai.ipynb`.
- **Standardizat pe `FoundryChatClient` + `as_agent`.** Codul README și din caietele de notițe care făceau referire la `AzureAIProjectAgentProvider` a fost standardizat pe modelul canonic folosit de Lecția 01 și exemplele framework-ului: `FoundryChatClient(project_endpoint=..., model=..., credential=AzureCliCredential())` cu `provider.as_agent(...)`. Actualizat în README-urile și caietele de notițe pentru lecțiile 02–14 (de ex., memoria din lecția 13, toate caietele din lecția 14, `11-agentic-protocols/code_samples/github-mcp/app.py`).
- **Numele produsului.** Redenumit în tot conținutul în limba engleză:
  - "Azure AI Foundry" / "Azure AI Studio" → **Microsoft Foundry**
  - "Azure AI Agent Service" → **Microsoft Foundry Agent Service**
  - (Neschimbat: "Azure OpenAI", "Azure AI Search", "Azure AI Inference" și numele variabilelor de mediu.)
- **Dependențe** ([requirements.txt](../../requirements.txt)):
  - Blocare versiuni pentru `agent-framework>=1.10.0`, `agent-framework-foundry>=1.10.0`, `agent-framework-openai>=1.10.0`.
  - Blocare versiuni pentru `openai>=1.108.1` (minim pentru API-ul Responses).
  - Eliminat `azure-ai-inference` (folosit doar în exemplele migrate de la GitHub Models).
- **Configurarea mediului** ([.env.example](../../.env.example)): eliminate variabilele GitHub Models (`GITHUB_TOKEN`, `GITHUB_ENDPOINT`, `GITHUB_MODEL_ID`); adăugate `AZURE_OPENAI_ENDPOINT`, `AZURE_OPENAI_DEPLOYMENT` și opțional `AZURE_OPENAI_API_KEY`; actualizate denumirile la Microsoft Foundry.
- **Documentație** — Actualizate [00-course-setup/README.md](./00-course-setup/README.md), [AGENTS.md](./AGENTS.md), [README.md](./README.md), și [STUDY_GUIDE.md](./STUDY_GUIDE.md) pentru cele de mai sus (variabile de mediu pentru configurare, fragment de verificare, ghid pentru provider, denumiri).

### Eliminat

- Pașii de integrare GitHub Models și variabilele de mediu corespunzătoare din documentația de configurare (înlocuite de Azure OpenAI / Microsoft Foundry).

### Securitate / Confidențialitate (curățare pentru partajare publică)

- Șterse ieșirile din execuția caietelor Jupyter care dezvăluiau un adevărat **ID de abonament Azure**, nume de grupuri de resurse / resurse și ID de conexiune Bing, plus **căi locale de fișiere și nume de utilizator** ale dezvoltatorilor, în:
  - `08-multi-agent/code_samples/workflows-agent-framework/dotNET/04.dotnet-agent-framework-workflow-aifoundry-condition.ipynb`
  - `08-multi-agent/code_samples/workflows-agent-framework/python/04.python-agent-framework-workflow-aifoundry-condition.ipynb`
  - `15-browser-use/15-browser-user.ipynb`
- Confirmat că nu mai există chei API, tokenuri, ID-uri de abonament sau căi personale detectate în conținutul urmărit în limba engleză (referințele `GITHUB_TOKEN` rămase sunt tokenul GitHub Actions în workflow-uri și PAT server GitHub MCP în configurarea lecției 11 — ambele legitime și fără legătură cu GitHub Models).

### Note și limitări cunoscute

- **Nu au fost executate/comilate.** Acestea sunt exemple educaționale actualizate pentru corectitudinea API/denumiri; nu au fost rulate pe resurse Azure reale, iar exemplele .NET nu au fost compilate în acest mediu. Validati cu propria dvs. implementare Microsoft Foundry / Azure OpenAI.
- **Implementarea modelului trebuie să suporte API-ul Responses.** Folosiți o implementare precum `gpt-4.1-mini`, `gpt-4.1` sau un model `gpt-5.x`. Modelele mai vechi suportă funcționalități de bază Responses, dar nu toate caracteristicile.
- **Versiunea agent-framework.** Exemplele vizează cea mai recentă versiune MAF (`>=1.10.0`). Apelul canonic pentru creare agent este `client.as_agent(...)`; API-urile au fost validate cu documentația publicată a framework-ului și o versiune instalată. Dacă blocați o versiune diferită, confirmați disponibilitatea metodei (`as_agent` vs `create_agent`).
- **Caietul de notițe al fluxului de lucru lecția 08 – 04** păstrează intenționat `AzureAIAgentClient` (din `agent-framework-azure-ai`) deoarece folosește instrumente găzduite Microsoft Foundry Agent Service (fundamentare Bing, interpret cod); este deja bazat pe Responses.
- **Implementarea .NET implicită.** Două exemple .NET pentru workflow-ul lecției 08 codau anterior un model specific; acum folosesc implicit `AZURE_OPENAI_DEPLOYMENT` (`gpt-4.1-mini`). Dacă un exemplu se bazează pe input multimodal/viziune, setați `AZURE_OPENAI_DEPLOYMENT` la un model potrivit.
- **Foundry Local** oferă un endpoint compatibil OpenAI **Chat Completions** și este destinat dezvoltării locale; folosiți Azure OpenAI / Microsoft Foundry pentru întregul set de funcționalități API Responses.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Declinare a responsabilității**:
Acest document a fost tradus folosind serviciul de traducere AI [Co-op Translator](https://github.com/Azure/co-op-translator). În timp ce ne străduim pentru acuratețe, vă rugăm să rețineți că traducerile automate pot conține erori sau inexactități. Documentul original în limba sa nativă trebuie considerat sursa autorizată. Pentru informații critice, se recomandă traducerea profesională realizată de un om. Nu ne asumăm responsabilitatea pentru eventualele neînțelegeri sau interpretări greșite care decurg din utilizarea acestei traduceri.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->