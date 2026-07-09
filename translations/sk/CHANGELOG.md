# Zmeny

Všetky významné zmeny v kurze **AI Agents for Beginners** sú zdokumentované v tomto súbore.

## [Neuvoľnené] — 2026-07-06

Toto vydanie migruje kurz na **Azure OpenAI Responses API**, štandardizuje názvy produktov na **Microsoft Foundry** a **Microsoft Agent Framework (MAF)**, ukončuje GitHub Models, aktualizuje verzie SDK a pridáva nový obsah o lokálnych modeloch a hosťovaní ďalších rámcov na Foundry.

### Pridané

- **Migračná zručnosť** — Nainštalovaná Agent Skill [`azure-openai-to-responses`](./.agents/skills/azure-openai-to-responses/SKILL.md) (z [Azure-Samples/azure-openai-to-responses](https://github.com/Azure-Samples/azure-openai-to-responses)) v `.agents/skills/`, vrátane jej referencií a skriptu skenera.
- **Foundry Local (spustenie modelov lokálne na zariadení)** — Nová sekcia "Alternatívny poskytovateľ: Foundry Local" v [00-course-setup/README.md](./00-course-setup/README.md) pokrývajúca inštaláciu (`winget` / `brew`), `foundry model run`, `foundry-local-sdk` a prepojenie `FoundryLocalManager` s Microsoft Agent Framework cez `OpenAIChatClient`.
- **Hosťovanie LangChain / LangGraph agentov na Microsoft Foundry** — Nová sekcia v [14-microsoft-agent-framework/README.md](./14-microsoft-agent-framework/README.md) plus spustiteľný príklad [14-langchain-hosted-agent.py](../../14-microsoft-agent-framework/code-samples/14-langchain-hosted-agent.py) používajúci `langchain-azure-ai[hosting]` a `ResponsesHostServer` (protokol `/responses`), na základe [Microsoft Learn](https://learn.microsoft.com/azure/foundry/how-to/develop/langchain-hosted-agents).
- **Microsoft Project Opal** — Nová sekcia "Reálny príklad: Microsoft Project Opal" v [15-browser-use/README.md](./15-browser-use/README.md), ktorá rámcuje Opal ako podnikový agent používajúci počítač a mapuje ho na pojmy z kurzu (človek v slučke, dôvera/bezpečnosť, plánovanie, zručnosti).
- **Druhý ukážkový Python kód k lekcii 02** — Pridaný [02-python-agent-framework-azure-openai.ipynb](./02-explore-agentic-frameworks/code_samples/02-python-agent-framework-azure-openai.ipynb) (pozri "Zmenené" — migrované z bývalého notebooku Semantic Kernel) a prepojený v README lekcie.
- Pridaná sekcia **Modely a poskytovatelia** do [STUDY_GUIDE.md](./STUDY_GUIDE.md).

### Zmenené

- **Chat Completions → Responses API (Python).** Ukážky, ktoré volali model priamo, boli migrované z Chat Completions na Responses API (`client.responses.create(input=..., store=False)`, `resp.output_text`) pomocou klienta `OpenAI` voči stabilnému Azure OpenAI `/openai/v1/` koncovému bodu (bez `api_version`). Týka sa ukážok:
  - [06-building-trustworthy-agents/code_samples/06-system-message-framework.ipynb](./06-building-trustworthy-agents/code_samples/06-system-message-framework.ipynb)
  - [06-building-trustworthy-agents/code_samples/06-human-in-the-loop.ipynb](./06-building-trustworthy-agents/code_samples/06-human-in-the-loop.ipynb)
  - [04-tool-use/README.md](./04-tool-use/README.md) — kompletná ukážka volania funkcie (schema nástrojov zjednodušená do formátu Responses, výsledky nástrojov vracané ako `function_call_output`, `max_output_tokens` atď.).
- **GitHub Models → Azure OpenAI.** GitHub Models je zastaralý (ukončenie **júl 2026**) a nepodporuje Responses API. Všetky cesty kódu pre GitHub Models boli premenené na Azure OpenAI / Microsoft Foundry v ukážkach pre Python a .NET:
  - Python: pracovné zošity lekcie 08 (`01`–`03`), lekcia 14 (`14-handoff`, `14-human-loop`, `hotel_booking_workflow_sample.py`).
  - .NET: `01`–`04`, `07`, `08` `*-dotnet-agent-framework.cs` + sprievodné `.md` dokumenty a lekcia 08 dotNET pracovné zošity/`.md` (`01`–`03`) teraz používajú `AzureOpenAIClient(...).GetOpenAIResponseClient(deployment).CreateAIAgent(...)` s `AzureCliCredential`.
- **Semantic Kernel → Microsoft Agent Framework.** Bývalý `02-semantic-kernel.ipynb` bol prepísaný na použitie Microsoft Agent Framework s Azure OpenAI (Responses API) a premenovaný na `02-python-agent-framework-azure-openai.ipynb`.
- **Štandardizácia na `FoundryChatClient` + `as_agent`.** README a kód v notebookoch, ktoré odkazovali na `AzureAIProjectAgentProvider`, boli štandardizované podľa kanonického vzoru používaného v Lekcii 01 a vo vlastných príkladoch frameworku: `FoundryChatClient(project_endpoint=..., model=..., credential=AzureCliCredential())` s `provider.as_agent(...)`. Aktualizované naprieč README a notebookmi Lekcií 02–14 (napr. pamäť v Lekcii 13, všetky notebooky v Lekcii 14, `11-agentic-protocols/code_samples/github-mcp/app.py`).
- **Názvoslovie produktov.** Premenované v anglickom obsahu:
  - "Azure AI Foundry" / "Azure AI Studio" → **Microsoft Foundry**
  - "Azure AI Agent Service" → **Microsoft Foundry Agent Service**
  - (Nezmenené: "Azure OpenAI", "Azure AI Search", "Azure AI Inference" a názvy premenných prostredia.)
- **Závislosti** ([requirements.txt](../../requirements.txt)):
  - Zamknuté verzie `agent-framework>=1.10.0`, `agent-framework-foundry>=1.10.0`, `agent-framework-openai>=1.10.0`.
  - Zamknutá verzia `openai>=1.108.1` (minimum pre Responses API).
  - Odstránený `azure-ai-inference` (bol používaný len v migrovaných ukážkach GitHub Models).
- **Konfigurácia prostredia** ([.env.example](../../.env.example)): odstránené premenné GitHub Models (`GITHUB_TOKEN`, `GITHUB_ENDPOINT`, `GITHUB_MODEL_ID`); pridané `AZURE_OPENAI_ENDPOINT`, `AZURE_OPENAI_DEPLOYMENT` a voliteľné `AZURE_OPENAI_API_KEY`; upravené názvy na Microsoft Foundry.
- **Dokumentácia** — Aktualizované [00-course-setup/README.md](./00-course-setup/README.md), [AGENTS.md](./AGENTS.md), [README.md](./README.md) a [STUDY_GUIDE.md](./STUDY_GUIDE.md) podľa vyššie uvedeného (nastavenie premenných prostredia, snippet na overenie, smerovanie poskytovateľa, názvy).

### Odstránené

- Kroky násadzenia GitHub Models a premenné prostredia zo setup dokumentácie (nahradené Azure OpenAI / Microsoft Foundry).

### Bezpečnosť / Ochrana súkromia (čistenie verejného zdieľania)

- Vymazané výstupy vykonávania Jupyter notebookov, ktoré obsahovali skutočné **Azure subscription ID**, názvy resource-group / resource, a Bing connection ID, plus vývojárske **lokálne cesty k súborom a používateľské mená**, v:
  - `08-multi-agent/code_samples/workflows-agent-framework/dotNET/04.dotnet-agent-framework-workflow-aifoundry-condition.ipynb`
  - `08-multi-agent/code_samples/workflows-agent-framework/python/04.python-agent-framework-workflow-aifoundry-condition.ipynb`
  - `15-browser-use/15-browser-user.ipynb`
- Overené, že v sledovanom anglickom obsahu nezostali žiadne API kľúče, tokeny, subscription ID alebo osobné cesty (referencie na `GITHUB_TOKEN`, ktoré zostali, sú tokeny GitHub Actions v workflowoch a GitHub MCP server PAT v nastavení Lekcie 11 — oboje legitímne a nesúvisiace s GitHub Models).

### Poznámky a známe obmedzenia

- **Nevykonané/nekontrolované.** Ide o vzdelávacie príklady aktualizované pre správnosť API/názvov; neboli spustené proti živým zdrojom Azure a .NET ukážky neboli skompilované v tomto prostredí. Overte si ich s vlastným nasadením Microsoft Foundry / Azure OpenAI.
- **Nasadený model musí podporovať Responses API.** Používajte nasadenia ako `gpt-4o-mini`, `gpt-4.1` alebo modely `gpt-5.x`. Staršie modely podporujú základné funkcie Responses, ale nie každý prvok.
- **Verzia agent-frameworku.** Ukážky cielia na najnovší MAF (`>=1.10.0`). Kanonický spôsob vytvárania agenta je `client.as_agent(...)`; API boli overené s publikovanými dokumentmi frameworku a nainštalovanou verziou. Ak použijete inú verziu, overte dostupnosť metódy (`as_agent` vs `create_agent`).
- **Pracovný zošit Lekcie 08, ukážka 04** záměrne ponecháva `AzureAIAgentClient` (z `agent-framework-azure-ai`), pretože používa nástroje hosťované Microsoft Foundry Agent Service (Bing grounding, kódový interpret); už je založená na Responses.
- **Predvolené nasadenie pre .NET.** Dve ukážky pracovného postupu Lekcie 08 pre dotNET predtým pevne uvádzali `gpt-4o`; teraz predvolené je `AZURE_OPENAI_DEPLOYMENT` (`gpt-4o-mini`). Ak ukážka vyžaduje multimodálny/vizuálny vstup, nastavte `AZURE_OPENAI_DEPLOYMENT` na vhodný model.
- **Foundry Local** vystavuje OpenAI-kompatibilnú koncovú stanicu **Chat Completions** a je určený pre lokálny vývoj; pre plnú funkcionalitu Responses API používajte Azure OpenAI / Microsoft Foundry.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Vyhlásenie o zodpovednosti**:
Tento dokument bol preložený pomocou AI prekladateľskej služby [Co-op Translator](https://github.com/Azure/co-op-translator). Hoci sa snažíme o presnosť, vezmite prosím na vedomie, že automatické preklady môžu obsahovať chyby alebo nepresnosti. Pôvodný dokument v jeho natívnom jazyku by mal byť považovaný za autoritatívny zdroj. Pre kritické informácie sa odporúča profesionálny ľudský preklad. Nie sme zodpovední za žiadne nedorozumenia alebo nesprávne interpretácie vyplývajúce z použitia tohto prekladu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->