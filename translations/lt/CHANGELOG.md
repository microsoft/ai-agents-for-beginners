# Pokyčių žurnalas

Visos reikšmingos **AI agentai pradedantiesiems** kurso pakeitimai yra dokumentuoti šiame faile.

## [Neišleista] — 2026-07-06

Ši versija migruoja kursą į **Azure OpenAI Responses API**, standartizuoja produktų pavadinimus **Microsoft Foundry** ir **Microsoft Agent Framework (MAF)**, atsisako GitHub modelių, atnaujina SDK versijas ir prideda naujo turinio apie vietinius modelius bei kitų sistemų talpinimą „Foundry“.

### Pridėta

- **Migracijos įgūdis** — Įdiegtas [`azure-openai-to-responses`](./.agents/skills/azure-openai-to-responses/SKILL.md) Agentų įgūdis (iš [Azure-Samples/azure-openai-to-responses](https://github.com/Azure-Samples/azure-openai-to-responses)) į `.agents/skills/`, kartu su jo nuorodomis ir nuskaitymo skriptu.
- **Foundry Local (modelių paleidimas įrenginyje)** — Nauja skiltis „Alternatyvus tiekėjas: Foundry Local“ [00-course-setup/README.md](./00-course-setup/README.md), apimanti diegimą (`winget` / `brew`), `foundry model run`, `foundry-local-sdk` ir `FoundryLocalManager` sujungimą su Microsoft Agent Framework per `OpenAIChatClient`.
- **LangChain / LangGraph agentų talpinimas Microsoft Foundry** — Nauja skiltis [14-microsoft-agent-framework/README.md](./14-microsoft-agent-framework/README.md) ir paleidžiamas pavyzdys [14-langchain-hosted-agent.py](../../14-microsoft-agent-framework/code-samples/14-langchain-hosted-agent.py), naudojantis `langchain-azure-ai[hosting]` ir `ResponsesHostServer` (protokoletas `/responses`), remiantis [Microsoft Learn](https://learn.microsoft.com/azure/foundry/how-to/develop/langchain-hosted-agents).
- **Microsoft Project Opal** — Nauja skiltis „Realus pavyzdys: Microsoft Project Opal“ [15-browser-use/README.md](./15-browser-use/README.md), pristatanti Opal kaip įmonės kompiuterio naudojimo agentą ir susiejančią jį su kurso koncepcijomis (žmogus grandinėje, pasitikėjimas/saugumas, planavimas, įgūdžiai).
- **Antras 02 Python pamokos pavyzdys** — Pridėtas [02-python-agent-framework-azure-openai.ipynb](./02-explore-agentic-frameworks/code_samples/02-python-agent-framework-azure-openai.ipynb) (žr. „Pakeista“ — perkeltas iš ankstesnio Semantic Kernel užrašyno) ir pridėtas ryšys pamokos README.
- Pridėta „Modeliai ir tiekėjai“ skiltis į [STUDY_GUIDE.md](./STUDY_GUIDE.md).

### Pakeista

- **Chat Completions → Responses API (Python).** Pavyzdžiai, kurie tiesiogiai kvietė modelį, buvo perkelti nuo Chat Completions prie Responses API (`client.responses.create(input=..., store=False)`, `resp.output_text`), naudojant `OpenAI` klientą su stabiliu Azure OpenAI `/openai/v1/` galiniu tašku (be `api_version`). Keičiami pavyzdžiai:
  - [06-building-trustworthy-agents/code_samples/06-system-message-framework.ipynb](./06-building-trustworthy-agents/code_samples/06-system-message-framework.ipynb)
  - [06-building-trustworthy-agents/code_samples/06-human-in-the-loop.ipynb](./06-building-trustworthy-agents/code_samples/06-human-in-the-loop.ipynb)
  - [04-tool-use/README.md](./04-tool-use/README.md) — pilnas funkcijos kvietimo pavyzdys (įrankių schema pritaikyta Responses formatui, įrankių rezultatai pateikiami kaip `function_call_output`, `max_output_tokens` ir pan.).
- **GitHub modeliai → Azure OpenAI.** GitHub modeliai yra pasenę (atsisakoma **2026 metų liepos mėn.**) ir nepalaiko Responses API. Visi GitHub Modelių kodo takai buvo perkelti į Azure OpenAI / Microsoft Foundry Python ir .NET pavyzdžiuose:
  - Python: Pamoka 08 darbo eigos užrašynai (`01`–`03`), Pamoka 14 (`14-handoff`, `14-human-loop`, `hotel_booking_workflow_sample.py`).
  - .NET: `01`–`04`, `07`, `08` `*-dotnet-agent-framework.cs` + susieti `.md` dokumentai, taip pat Pamoka 08 dotNET darbo eigos užrašynai/`.md` (`01`–`03`) dabar naudoja `AzureOpenAIClient(...).GetOpenAIResponseClient(deployment).CreateAIAgent(...)` su `AzureCliCredential`.
- **Semantic Kernel → Microsoft Agent Framework.** Ankstesnis `02-semantic-kernel.ipynb` buvo perrašytas naudoti Microsoft Agent Framework su Azure OpenAI (Responses API) ir pervadintas į `02-python-agent-framework-azure-openai.ipynb`.
- **Standartizuota `FoundryChatClient` + `as_agent`.** README ir užrašynų kodas, kuris naudojo `AzureAIProjectAgentProvider`, buvo standartizuotas pagal kanoninį modelį, naudojamą Pamokoje 01 bei framework'o pavyzdžiuose: `FoundryChatClient(project_endpoint=..., model=..., credential=AzureCliCredential())` su `provider.as_agent(...)`. Atnaujinta Pamokose nuo 02 iki 14 README ir užrašynuose (pvz., Pamokos 13 atmintis, visi Pamokos 14 užrašynai, `11-agentic-protocols/code_samples/github-mcp/app.py`).
- **Produktų pavadinimai.** Pervadinta visame anglų kalbos turinyje:
  - "Azure AI Foundry" / "Azure AI Studio" → **Microsoft Foundry**
  - "Azure AI Agent Service" → **Microsoft Foundry Agent Service**
  - (Nepliuskeista: "Azure OpenAI", "Azure AI Search", "Azure AI Inference" ir aplinkos kintamųjų pavadinimai.)
- **Priklausomybės** ([requirements.txt](../../requirements.txt)):
  - Užfiksuota `agent-framework>=1.10.0`, `agent-framework-foundry>=1.10.0`, `agent-framework-openai>=1.10.0`.
  - Užfiksuota `openai>=1.108.1` (minimalus Responses API palaikymas).
  - Pašalinta `azure-ai-inference` (naudota tik migravimuose su GitHub modeliais).
- **Aplinkos konfigūracija** ([.env.example](../../.env.example)): pašalinti GitHub modeliams skirti kintamieji (`GITHUB_TOKEN`, `GITHUB_ENDPOINT`, `GITHUB_MODEL_ID`); pridėti `AZURE_OPENAI_ENDPOINT`, `AZURE_OPENAI_DEPLOYMENT` ir neprivalomas `AZURE_OPENAI_API_KEY`; atnaujintas pavadinimas į Microsoft Foundry.
- **Dokumentacija** — Atnaujinta [00-course-setup/README.md](./00-course-setup/README.md), [AGENTS.md](./AGENTS.md), [README.md](./README.md) ir [STUDY_GUIDE.md](./STUDY_GUIDE.md) aukščiau nurodytoms temoms (apl env kint, tikrinimo fragmentas, tiekėjo gairės, pavadinimai).

### Pašalinta

- GitHub modelių įvedimo žingsniai ir aplinkos kintamieji iš diegimo dokumentų (pakeista Azure OpenAI / Microsoft Foundry).

### Saugumas / Privatumas (viešo dalijimosi valymas)

- Išvalyti Jupyter užrašyno vykdymo rezultatai, kuriuose nutekėjo tikras **Azure prenumeratos ID**, resursų grupių / resursų pavadinimai, Bing prisijungimo ID, o taip pat kūrėjų **vietiniai failų keliai ir vartotojo vardai**:
  - `08-multi-agent/code_samples/workflows-agent-framework/dotNET/04.dotnet-agent-framework-workflow-aifoundry-condition.ipynb`
  - `08-multi-agent/code_samples/workflows-agent-framework/python/04.python-agent-framework-workflow-aifoundry-condition.ipynb`
  - `15-browser-use/15-browser-user.ipynb`
- Patikrinta, kad nesimatytų API raktų, žetonų, prenumeratos ID ar asmeninių kelių anglų kalbos turinyje (likusios `GITHUB_TOKEN` nuorodos yra GitHub Actions žetonai darbo eigoje ir GitHub MCP serverio PAT Pamokoje 11 — jie yra teisėtas ir nesusiję su GitHub modeliais).

### Pastabos ir žinomi apribojimai

- **Nevykdyti/nekokliuoti.** Tai mokomieji pavyzdžiai, atnaujinti pagal API ir vardynų taisykles; jie nebuvo vykdyti su tiesiogine Azure infrastruktūra, o .NET pavyzdžiai nebuvo kokliuojami šioje aplinkoje. Patikrinkite su savo Microsoft Foundry / Azure OpenAI diegimu.
- **Modelio diegimas turi palaikyti Responses API.** Naudokite diegimą kaip `gpt-4o-mini`, `gpt-4.1` arba `gpt-5.x` modelį. Senesni modeliai palaiko pagrindinę Responses funkcionalumą, bet ne visas funkcijas.
- **Agent-framework versija.** Pavyzdžiai taikomi naujausiai MAF (`>=1.10.0`). Kanoninis agento kūrimo kvietimas yra `client.as_agent(...)`; API buvo patikrintos pagal oficialią dokumentaciją ir įdiegtą versiją. Jei naudosite kitą versiją, patikrinkite metodų prieinamumą (`as_agent` vs `create_agent`).
- **Pamokos 08 darbo eigos užrašynas 04** specialiai paliekamas `AzureAIAgentClient` (iš `agent-framework-azure-ai`), nes naudojami Microsoft Foundry Agent Service įrankiai (Bing pagrindimas, kodų interpretatorius); jis jau yra paremtas Responses.
- **.NET numatytasis diegimas.** Du Pamokos 08 dotNET darbo eigos pavyzdžiai anksčiau turėjo įkoduotą `gpt-4o`; dabar jie pagal nutylėjimą naudoja `AZURE_OPENAI_DEPLOYMENT` (`gpt-4o-mini`). Jei pavyzdys naudoja multimodalinį / vaizdo įvestį, nustatykite `AZURE_OPENAI_DEPLOYMENT` į tinkamą modelį.
- **Foundry Local** suteikia OpenAI suderinamą **Chat Completions** galinį tašką ir skirtas vietiniam vystymui; naudokite Azure OpenAI / Microsoft Foundry, kad gautumėte pilną Responses API funkcionalumą.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Atsakomybės apribojimas**:
Šis dokumentas buvo išverstas naudojant dirbtinio intelekto vertimo paslaugą [Co-op Translator](https://github.com/Azure/co-op-translator). Nors siekiame tikslumo, prašome atkreipti dėmesį, kad automatiniai vertimai gali turėti klaidų ar netikslumų. Originalus dokumentas jo gimtąja kalba laikomas autoritetingu šaltiniu. Svarbiai informacijai rekomenduojama naudoti profesionalų žmogiškąjį vertimą. Mes neatsakome už jokius nesusipratimus ar neteisingą interpretaciją, kilusią naudojantis šiuo vertimu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->