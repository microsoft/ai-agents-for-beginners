# Istoricul modificărilor

Toate modificările notabile aduse cursului **AI Agents for Beginners** sunt documentate în acest fișier.

## [Nerelease] — 2026-07-06

Această versiune migrează cursul la **Azure OpenAI Responses API**, standardizează denumirile de produs pe **Microsoft Foundry** și pe **Microsoft Agent Framework (MAF)**, retrage GitHub Models, actualizează versiunile SDK, și adaugă conținut nou despre modele locale și găzduirea altor framework-uri pe Foundry.

### Adăugat

- **Skill de migrare** — Instalată Agent Skill [`azure-openai-to-responses`](./.agents/skills/azure-openai-to-responses/SKILL.md) (din [Azure-Samples/azure-openai-to-responses](https://github.com/Azure-Samples/azure-openai-to-responses)) sub `.agents/skills/`, inclusiv referințele și scriptul scaner.
- **Foundry Local (rularea modelelor pe dispozitiv)** — Secțiune nouă "Alternative Provider: Foundry Local" în [00-course-setup/README.md](./00-course-setup/README.md) care acoperă instalarea (`winget` / `brew`), `foundry model run`, SDK-ul `foundry-local-sdk` și conectarea `FoundryLocalManager` la Microsoft Agent Framework prin `OpenAIChatClient`.
- **Găzduirea agenților LangChain / LangGraph pe Microsoft Foundry** — Secțiune nouă în [14-microsoft-agent-framework/README.md](./14-microsoft-agent-framework/README.md) plus un exemplu rulabil [14-langchain-hosted-agent.py](../../14-microsoft-agent-framework/code-samples/14-langchain-hosted-agent.py) folosind `langchain-azure-ai[hosting]` și `ResponsesHostServer` (protocolul `/responses`), bazat pe [Microsoft Learn](https://learn.microsoft.com/azure/foundry/how-to/develop/langchain-hosted-agents).
- **Microsoft Project Opal** — Secțiune nouă "Exemplu din lumea reală: Microsoft Project Opal" în [15-browser-use/README.md](./15-browser-use/README.md) care prezintă Opal ca agent de utilizare computerizată în mediul enterprise și îl mapează la conceptele cursului (omul în buclă, încredere/securitate, planificare, Skills).
- **Al doilea exemplu Python pentru Lecția 02** — Adăugat [02-python-agent-framework-azure-openai.ipynb](./02-explore-agentic-frameworks/code_samples/02-python-agent-framework-azure-openai.ipynb) (vezi "Schimbat" — migrat din fostul notebook Semantic Kernel) și legat în README-ul lecției.
- Secțiunea **Modele și Furnizori** a fost adăugată în [STUDY_GUIDE.md](./STUDY_GUIDE.md).

### Schimbat

- **Chat Completions → Responses API (Python).** Exemplele care apelau modelul direct au fost migrate de la Chat Completions la Responses API (`client.responses.create(input=..., store=False)`, `resp.output_text`), folosind clientul `OpenAI` contra endpoint-ului stabil Azure OpenAI `/openai/v1/` (fără `api_version`). Exemple afectate includ:
  - [06-building-trustworthy-agents/code_samples/06-system-message-framework.ipynb](./06-building-trustworthy-agents/code_samples/06-system-message-framework.ipynb)
  - [06-building-trustworthy-agents/code_samples/06-human-in-the-loop.ipynb](./06-building-trustworthy-agents/code_samples/06-human-in-the-loop.ipynb)
  - [04-tool-use/README.md](./04-tool-use/README.md) — tot walkthrough-ul funcției de apelare (schema tool-ului a fost aplatizată în formatul Responses, rezultatele tool-ului returnate ca `function_call_output`, `max_output_tokens`, etc.).
- **GitHub Models → Azure OpenAI.** GitHub Models este depreciat (va fi retras **în iulie 2026**) și nu suportă Responses API. Toate căile de cod ale GitHub Models au fost convertite la Azure OpenAI / Microsoft Foundry în exemplarele Python și .NET:
  - Python: notebook-urile workflow ale Lecției 08 (`01`–`03`), Lecția 14 (`14-handoff`, `14-human-loop`, `hotel_booking_workflow_sample.py`).
  - .NET: `01`–`04`, `07`, `08` `*-dotnet-agent-framework.cs` + documentația companion `.md`, iar notebook-urile/workflow dotNET din Lecția 08 / `.md` (`01`–`03`) folosesc acum `AzureOpenAIClient(...).GetOpenAIResponseClient(deployment).CreateAIAgent(...)` cu `AzureCliCredential`.
- **Semantic Kernel → Microsoft Agent Framework.** Fostul `02-semantic-kernel.ipynb` a fost rescris pentru a folosi Microsoft Agent Framework cu Azure OpenAI (Responses API) și redenumit `02-python-agent-framework-azure-openai.ipynb`.
- **Standardizarea pe `FoundryChatClient` + `as_agent`.** Codul din README și notebook care făcea referire la `AzureAIProjectAgentProvider` a fost standardizat pe modelul canonic folosit în Lecția 01 și în propriile exemple ale framework-ului: `FoundryChatClient(project_endpoint=..., model=..., credential=AzureCliCredential())` cu `provider.as_agent(...)`. Actualizat în toate README-urile și notebook-urile din Lecțiile 02–14 (ex.: memoria din Lecția 13, toate notebook-urile din Lecția 14, `11-agentic-protocols/code_samples/github-mcp/app.py`).
- **Denumiri de produs.** Redenumit în întreg conținutul în limba engleză:
  - "Azure AI Foundry" / "Azure AI Studio" → **Microsoft Foundry**
  - "Azure AI Agent Service" → **Microsoft Foundry Agent Service**
  - (Nemodificat: "Azure OpenAI", "Azure AI Search", "Azure AI Inference", și numele variabilelor de mediu.)
- **Dependențe** ([requirements.txt](../../requirements.txt)):
  - Blocare versiuni pentru `agent-framework>=1.10.0`, `agent-framework-foundry>=1.10.0`, `agent-framework-openai>=1.10.0`.
  - Blocare versiune `openai>=1.108.1` (minimul pentru Responses API).
  - Eliminat `azure-ai-inference` (folosit doar în exemplele migrate GitHub Models).
- **Configurare mediu** ([.env.example](../../.env.example)): eliminate variabilele GitHub Models (`GITHUB_TOKEN`, `GITHUB_ENDPOINT`, `GITHUB_MODEL_ID`); adăugate `AZURE_OPENAI_ENDPOINT`, `AZURE_OPENAI_DEPLOYMENT` și opțional `AZURE_OPENAI_API_KEY`; actualizate denumirile către Microsoft Foundry.
- **Documentație** — Actualizate [00-course-setup/README.md](./00-course-setup/README.md), [AGENTS.md](./AGENTS.md), [README.md](./README.md), și [STUDY_GUIDE.md](./STUDY_GUIDE.md) pentru cele de mai sus (variabile mediu setup, snippet de verificare, ghidare furnizor, denumiri).

### Eliminat

- Pașii de onboarding GitHub Models și variabilele de mediu din documentația de setup (înlocuite de Azure OpenAI / Microsoft Foundry).

### Securitate / Confidențialitate (curățare conținut partajat public)

- Șterse rezultatele execuțiilor din Jupyter notebook-uri care au expus un **ID real de abonament Azure**, numele grupurilor de resurse / resurse, ID-ul de conexiune Bing, plus **cale locale către fișiere și utilizatori ale dezvoltatorului**, în:
  - `08-multi-agent/code_samples/workflows-agent-framework/dotNET/04.dotnet-agent-framework-workflow-aifoundry-condition.ipynb`
  - `08-multi-agent/code_samples/workflows-agent-framework/python/04.python-agent-framework-workflow-aifoundry-condition.ipynb`
  - `15-browser-use/15-browser-user.ipynb`
- Verificat ca să nu rămână API keys, token-uri, ID-uri abonament sau căi personale în conținutul urmărit în engleză (referințele `GITHUB_TOKEN` rămase sunt token-ul GitHub Actions din workflow-uri și PAT-ul serverului GitHub MCP din setup-ul lecției 11 — ambele legitime și nelegate de GitHub Models).

### Note și limitări cunoscute

- **Neexecutate/necuncompilează.** Acestea sunt exemple educaționale actualizate pentru corectitudinea API/denumiri; nu au fost rulate împotriva resurselor Azure live și exemplele .NET nu au fost compilate în acest mediu. Validare cu propriul dvs. deployment Microsoft Foundry / Azure OpenAI.
- **Deployment-ul modelului trebuie să suporte Responses API.** Folosiți un deployment precum `gpt-4o-mini`, `gpt-4.1`, sau un model `gpt-5.x`. Modelele mai vechi suportă funcționalitatea de bază Responses, dar nu toate caracteristicile.
- **Versiunea agent-framework.** Exemplele sunt țintite pe cea mai nouă MAF (`>=1.10.0`). Apelul canonic de creare agent este `client.as_agent(...)`; API-urile au fost validate cu documentația publicată a framework-ului și o versiune instalată. Dacă fixați o versiune diferită, confirmați disponibilitatea metodei (`as_agent` vs `create_agent`).
- **Notebook-ul workflow al Lecției 08, nr. 04** păstrează intenționat `AzureAIAgentClient` (din `agent-framework-azure-ai`) deoarece folosește unelte găzduite Microsoft Foundry Agent Service (fundamentare Bing, interpreter cod); este deja bazat pe Responses.
- **Deployment-ul implicit .NET.** Două exemple workflow dotNET din Lecția 08 au codificat anterior `gpt-4o`; acum folosesc implicit `AZURE_OPENAI_DEPLOYMENT` (`gpt-4o-mini`). Dacă un exemplu necesită input multimodal/vizual, setați `AZURE_OPENAI_DEPLOYMENT` la un model potrivit.
- **Foundry Local** expune un endpoint compatibil OpenAI **Chat Completions** și este destinat dezvoltării locale; folosiți Azure OpenAI / Microsoft Foundry pentru setul complet de funcții Responses API.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Declinare a responsabilității**:
Acest document a fost tradus folosind serviciul de traducere AI [Co-op Translator](https://github.com/Azure/co-op-translator). În timp ce ne străduim pentru acuratețe, vă rugăm să rețineți că traducerile automate pot conține erori sau inexactități. Documentul original în limba sa nativă trebuie considerat sursa autorizată. Pentru informații critice, se recomandă traducerea profesională realizată de un om. Nu ne asumăm responsabilitatea pentru eventualele neînțelegeri sau interpretări greșite care decurg din utilizarea acestei traduceri.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->