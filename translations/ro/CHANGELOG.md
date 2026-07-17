# Istoric modificări

Toate schimbările notabile pentru cursul **AI Agents for Beginners** sunt documentate în acest fișier.

## [Lansat] — 2026-07-13

Această versiune adaugă două lecții noi care completează arcul de implementare — scalarea agenților pe Microsoft Foundry și coborârea la un singur post de lucru — plus un pipeline de testare de bază, navigare reîmprospătată în curs, noi competențe pentru cursanți și branding actualizat.

### Adăugat

- **Lecția 16 — Implementarea Agenților Scalabili cu Microsoft Foundry.** Lecție nouă [16-deploying-scalable-agents/README.md](./16-deploying-scalable-agents/README.md) și notebook rulabil [16-python-agent-framework.ipynb](./16-deploying-scalable-agents/code_samples/16-python-agent-framework.ipynb) care construiește un agent de suport clienți pentru producție (unelte, RAG, memorie, rutare model, cache de răspuns, aprobare umană, poartă de evaluare și trasare OpenTelemetry), cu diagrame Mermaid de dezvoltare/implementare/runtime, verificare de cunoștințe, o temă și o provocare.
- **Lecția 17 — Crearea Agenților AI Locali cu Foundry Local și Qwen.** Lecție nouă [17-creating-local-ai-agents/README.md](./17-creating-local-ai-agents/README.md) și notebook [17-local-agent-foundry-local.ipynb](./17-creating-local-ai-agents/code_samples/17-local-agent-foundry-local.ipynb) care construiește un asistent inginereasc complet pe dispozitiv (apelare funcție Qwen prin Foundry Local, unelte pentru fișiere sandboxed, RAG local cu Chroma, MCP local opțional), cu diagrame local-only / local-RAG / apelare unelte, verificare de cunoștințe, o temă și o provocare.
- **Pipeline de testare de bază.** Workflow nou [AI Smoke Test](https://github.com/marketplace/actions/ai-smoke-test) [.github/workflows/smoke-test.yml](../../.github/workflows/smoke-test.yml) plus cataloage pe lecții sub [tests/](./tests/README.md) pentru agenții implementabili din Lecțiile 01, 04, 05 și 16, cu un README index ce mapează fiecare catalog cu lecția și numele agentului găzduit. Lecția 16 primește o secțiune „Validarea unui Agent Implementat cu Teste Smoke”; Lecțiile 01/04/05 primesc un indicator opțional pentru testele smoke.
- **Competențe pentru cursanți.** Noi competențe Agent sub `.agents/skills/`: [deploying-scalable-agents](./.agents/skills/deploying-scalable-agents/SKILL.md), [local-ai-agents](./.agents/skills/local-ai-agents/SKILL.md) (împachetând ghidajul Lecțiilor 16 și 17), și [testing-course-samples](./.agents/skills/testing-course-samples/SKILL.md) (cum să validezi exemplele notebook împotriva unei configurații live Microsoft Foundry / Azure OpenAI).
- **Rularea validării notebook-urilor.** Script nou [scripts/validate-notebooks.ps1](../../scripts/validate-notebooks.ps1) care execută fiecare notebook Python headless folosind `nbconvert` și tipărește o matrice PASS/FAIL (plus `results.json`). Detectează automat rădăcina repo-ului și Python-ul, exclude implicit notebook-urile non-curs (`.venv`, `site-packages`, `translations`, resurse temă competență) și notebook-urile `.NET`, și suportă opțiunile `-Filter`, `-Timeout`, `-List`, `-IncludeDotnet` și `-Python`.
- **Navigarea în curs.** Au fost adăugate link-uri lecției Anterioară/Următoare pentru Lecțiile 11–15 (anterior lipsă) astfel încât întregul curs să se lege 00 → 18 în ambele direcții.
- **Miniaturi noi.** Miniaturi pentru Lecțiile 16 și 17, plus o imagine socială reîmprospătată a depozitului [images/repo-thumbnailv3.png](./images/repo-thumbnailv3.png) (care acum promovează cele două lecții noi și URL-ul `aka.ms/ai-agents-beginners`).
- **Dependențe** ([requirements.txt](../../requirements.txt)): adăugate `foundry-local-sdk` și `chromadb` pentru Lecția 17.

### Modificat

- **Tabelul principal din [README.md](./README.md) pentru lecții:** Lecțiile 16 și 17 acum leagă către conținutul lor (anterior „Coming Soon”); imaginea depozitului a fost actualizată la `repo-thumbnailv3.png`.
- **[STUDY_GUIDE.md](./STUDY_GUIDE.md):** au fost adăugate Lecțiile 16 și 17 în ghidul lecție cu lecție și căile de învățare, plus o secțiune „Validarea Agenților Implementați cu Teste Smoke”.
- **[AGENTS.md](./AGENTS.md):** actualizat numărul/descreția lecțiilor (00–18), adăugată o secțiune de validare prin teste smoke, și exemple de denumire pentru Lecțiile 16/17.
- **[18-securing-ai-agents/README.md](./18-securing-ai-agents/README.md):** „Lecția Anterioară” indică acum Lecția 17 (era Lecția 15), închizând lanțul.
- **Referințe standardizate la modele pe modelele care nu sunt deprecate.** Toate referințele `gpt-4o` / `gpt-4o-mini` din curs (documentație, `.env.example`, notebook-uri Python/.NET și exemple) au fost înlocuite cu `gpt-4.1-mini` — `gpt-4o` (toate versiunile) se retrag în 2026. Exemplul de rutare model din Lecția 16 păstrează un contrast mic/mare folosind `gpt-4.1-mini` (mic) și `gpt-4.1` (mare). Notebook-urile Python selectează acum modelul din variabile de mediu (`AZURE_AI_MODEL_DEPLOYMENT_NAME` / `AZURE_OPENAI_DEPLOYMENT`) în loc să fixeze un nume de model.

### Note și limitări cunoscute

- **Nu sunt executate împotriva unui Azure live.** Notebook-urile noilor lecții sunt exemple educaționale; rulează și validează-le cu propria ta configurație Microsoft Foundry / Foundry Local. Workflow-ul de testare smoke necesită să implementezi agentul lecției și să configurezi secrete Azure OIDC (`AZURE_CLIENT_ID`, `AZURE_TENANT_ID`, `AZURE_SUBSCRIPTION_ID`) cu rolul **Azure AI User** la nivelul proiectului Foundry.
- **Lecția 17 este doar locală.** Nu are punct final Foundry Responses, deci acțiunea de test smoke nu se aplică; valideaz-o rulând notebook-ul pe stația ta de lucru.

## [Lansat] — 2026-07-06

Această versiune mută cursul către **Azure OpenAI Responses API**, standardizează denumirile produselor în **Microsoft Foundry** și **Microsoft Agent Framework (MAF)**, retrage GitHub Models, actualizează versiunile SDK și adaugă conținut nou despre modelele locale și găzduirea altor cadre pe Foundry.

### Adăugat

- **Competența de migrare** — Competență Agent instalată [`azure-openai-to-responses`](./.agents/skills/azure-openai-to-responses/SKILL.md) (din [Azure-Samples/azure-openai-to-responses](https://github.com/Azure-Samples/azure-openai-to-responses)) sub `.agents/skills/`, inclusiv referințele și script-ul de scanare.
- **Foundry Local (rulează modele pe dispozitiv)** — Secțiune nouă „Furnizor Alternativ: Foundry Local” în [00-course-setup/README.md](./00-course-setup/README.md) care acoperă instalarea (`winget` / `brew`), `foundry model run`, `foundry-local-sdk`, și conectarea `FoundryLocalManager` la Microsoft Agent Framework prin `OpenAIChatClient`.
- **Găzduirea agenților LangChain / LangGraph pe Microsoft Foundry** — Secțiune nouă în [14-microsoft-agent-framework/README.md](./14-microsoft-agent-framework/README.md) plus exemplu rulabil [14-langchain-hosted-agent.py](../../14-microsoft-agent-framework/code-samples/14-langchain-hosted-agent.py) folosind `langchain-azure-ai[hosting]` și `ResponsesHostServer` (protocolul `/responses`), bazat pe [Microsoft Learn](https://learn.microsoft.com/azure/foundry/how-to/develop/langchain-hosted-agents).
- **Microsoft Project Opal** — Secțiune nouă „Exemplu din lumea reală: Microsoft Project Opal” în [15-browser-use/README.md](./15-browser-use/README.md) care încadrează Opal ca agent de utilizare enterprise și îl mapează pe conceptele cursului (uman-in-the-loop, încredere/securitate, planificare, Competențe).
- **Al doilea exemplu Python Lecția 02** — Adăugat [02-python-agent-framework-azure-openai.ipynb](./02-explore-agentic-frameworks/code_samples/02-python-agent-framework-azure-openai.ipynb) (vezi „Modificat” — migrat din fostul notebook Semantic Kernel) și legat în README-ul lecției.
- Secțiunea **Models and Providers** adăugată în [STUDY_GUIDE.md](./STUDY_GUIDE.md).

### Modificat

- **Chat Completions → Responses API (Python).** Exemplele care apelau modelul direct au fost migrate de la Chat Completions la Responses API (`client.responses.create(input=..., store=False)`, `resp.output_text`), folosind clientul `OpenAI` împotriva endpoint-ului stabil Azure OpenAI `/openai/v1/` (fără `api_version`). Exemple afectate includ:
  - [06-building-trustworthy-agents/code_samples/06-system-message-framework.ipynb](./06-building-trustworthy-agents/code_samples/06-system-message-framework.ipynb)
  - [06-building-trustworthy-agents/code_samples/06-human-in-the-loop.ipynb](./06-building-trustworthy-agents/code_samples/06-human-in-the-loop.ipynb)
  - [04-tool-use/README.md](./04-tool-use/README.md) — parcurgerea completă a apelului de funcții (schema uneltei adusă la formatul Responses, rezultatele uneltei returnate ca `function_call_output`, `max_output_tokens`, etc.).
- **GitHub Models → Azure OpenAI.** GitHub Models este depreciat (se retrage **iulie 2026**) și nu suportă Responses API. Toate căile de cod GitHub Models au fost convertite la Azure OpenAI / Microsoft Foundry în exemple Python și .NET:
  - Python: notebook-uri workflow Lecția 08 (`01`–`03`), Lecția 14 (`14-handoff`, `14-human-loop`, `hotel_booking_workflow_sample.py`).
  - .NET: `01`–`04`, `07`, `08` fișiere `*-dotnet-agent-framework.cs` + docuri `.md` companion, și notebook-urile workflow dotNET Lecția 08/`.md` (`01`–`03`) folosesc acum `AzureOpenAIClient(...).GetOpenAIResponseClient(deployment).CreateAIAgent(...)` cu `AzureCliCredential`.
- **Semantic Kernel → Microsoft Agent Framework.** Fostul `02-semantic-kernel.ipynb` a fost rescris să folosească Microsoft Agent Framework cu Azure OpenAI (Responses API) și redenumit `02-python-agent-framework-azure-openai.ipynb`.
- **Standardizat pe `FoundryChatClient` + `as_agent`.** Codul README și notebook care făceau referire la `AzureAIProjectAgentProvider` a fost standardizat după șablonul canonic folosit de Lecția 01 și propriile exemple ale framework-ului: `FoundryChatClient(project_endpoint=..., model=..., credential=AzureCliCredential())` cu `provider.as_agent(...)`. Actualizat în README-urile și notebook-urile Lecțiile 02–14 (ex: memoria din Lecția 13, toate notebook-urile Lecția 14, `11-agentic-protocols/code_samples/github-mcp/app.py`).
- **Denumiri produse.** Redenumit în tot conținutul în limba engleză:
  - „Azure AI Foundry” / „Azure AI Studio” → **Microsoft Foundry**
  - „Azure AI Agent Service” → **Microsoft Foundry Agent Service**
  - (Neschimbat: „Azure OpenAI”, „Azure AI Search”, „Azure AI Inference” și numele variabilelor de mediu.)
- **Dependențe** ([requirements.txt](../../requirements.txt)):
  - Blocaje pentru `agent-framework>=1.10.0`, `agent-framework-foundry>=1.10.0`, `agent-framework-openai>=1.10.0`.
  - Blocaj pentru `openai>=1.108.1` (minim pentru Responses API).
  - Eliminat `azure-ai-inference` (folosit doar de exemplele GitHub Models migrate).
- **Configurare mediu** ([.env.example](../../.env.example)): eliminate variabile GitHub Models (`GITHUB_TOKEN`, `GITHUB_ENDPOINT`, `GITHUB_MODEL_ID`); adăugate `AZURE_OPENAI_ENDPOINT`, `AZURE_OPENAI_DEPLOYMENT` și opțional `AZURE_OPENAI_API_KEY`; actualizat nume la Microsoft Foundry.
- **Docuri** — Actualizate [00-course-setup/README.md](./00-course-setup/README.md), [AGENTS.md](./AGENTS.md), [README.md](./README.md) și [STUDY_GUIDE.md](./STUDY_GUIDE.md) pentru cele de mai sus (variabile mediu setup, snippet verificare, ghid furnizor, denumiri).

### Eliminat

- Pașii de onboarding GitHub Models și variabilele de mediu din docurile de setup (înlocuite de Azure OpenAI / Microsoft Foundry).

### Securitate / Confidențialitate (curățare partajare publică)

- Șters output-ul execuției notebook-urilor Jupyter care scotea la lumină un adevărat **ID de subscripție Azure**, nume de grupuri de resurse / resurse și ID conexiune Bing, plus **cale locale fișiere și nume de utilizatori** ale dezvoltatorilor, în:
  - `08-multi-agent/code_samples/workflows-agent-framework/dotNET/04.dotnet-agent-framework-workflow-aifoundry-condition.ipynb`

  - `08-multi-agent/code_samples/workflows-agent-framework/python/04.python-agent-framework-workflow-aifoundry-condition.ipynb`
  - `15-browser-use/15-browser-user.ipynb`
- Verificat că nu există chei API, tokenuri, ID-uri de abonament sau cai personale în conținutul urmăribil în limba engleză (referințele `GITHUB_TOKEN` rămase sunt tokenul GitHub Actions în fluxurile de lucru și PAT-ul serverului GitHub MCP în configurarea Lecției 11 — ambele legitime și fără legătură cu GitHub Models).

### Note și limitări cunoscute

- **Nu sunt executate/compilate.** Acestea sunt exemple educaționale actualizate pentru corectitudinea API/nomenclaturii; nu au fost rulate împotriva resurselor Azure live și exemplele .NET nu au fost compilate în acest mediu. Validați cu propria implementare Microsoft Foundry / Azure OpenAI.
- **Implementarea modelului trebuie să suporte API-ul Responses.** Folosiți o implementare cum ar fi `gpt-4.1-mini`, `gpt-4.1` sau un model `gpt-5.x`. Modelele mai vechi suportă funcționalitatea de bază Responses, dar nu toate caracteristicile.
- **Versiunea agent-framework.** Exemplele vizează cea mai recentă versiune MAF (`>=1.10.0`). Apelul canonic pentru crearea agentului este `client.as_agent(...)`; API-urile au fost validate față de documentația publicată a framework-ului și o build instalată. Dacă fixați o versiune diferită, confirmați disponibilitatea metodei (`as_agent` vs `create_agent`).
- **Notebook-ul fluxului de lucru Lecția 08, fișierul 04** păstrează intenționat `AzureAIAgentClient` (din `agent-framework-azure-ai`) deoarece utilizează unelte găzduite Microsoft Foundry Agent Service (Bing grounding, interpret de cod); acesta este deja bazat pe Responses.
- **Implementarea implicită .NET.** Două exemple dotNET din Lecția 08 din fluxul de lucru au codificat anterior un model specific; acum folosesc implicit `AZURE_OPENAI_DEPLOYMENT` (`gpt-4.1-mini`). Dacă un exemplu depinde de intrare multimodală/vizuală, setați `AZURE_OPENAI_DEPLOYMENT` la un model potrivit.
- **Foundry Local** expune un endpoint compatibil OpenAI pentru **Chat Completions** și este destinat dezvoltării locale; pentru setul complet de funcții API Responses folosiți Azure OpenAI / Microsoft Foundry.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Declinare a responsabilității**:
Acest document a fost tradus folosind serviciul de traducere AI [Co-op Translator](https://github.com/Azure/co-op-translator). În timp ce ne străduim pentru acuratețe, vă rugăm să rețineți că traducerile automate pot conține erori sau inexactități. Documentul original în limba sa nativă trebuie considerat sursa autorizată. Pentru informații critice, se recomandă traducerea profesională realizată de un om. Nu ne asumăm responsabilitatea pentru eventualele neînțelegeri sau interpretări greșite care decurg din utilizarea acestei traduceri.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->