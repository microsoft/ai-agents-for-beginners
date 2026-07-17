# Zoznam zmien

Všetky významné zmeny v kurze **AI Agents for Beginners** sú zdokumentované v tomto súbore.

## [Vydané] — 2026-07-13

Toto vydanie pridáva dve nové lekcie, ktoré dokončia nasadzovací cyklus — škálovanie agentov na Microsoft Foundry a zmenšovanie na jedno pracovisko — plus testovací pipeline, obnovenú navigáciu v kurze, nové zručnosti študenta a aktualizovanú značku.

### Pridané

- **Lekcia 16 — Nasadzovanie škálovateľných agentov s Microsoft Foundry.** Nová lekcia [16-deploying-scalable-agents/README.md](./16-deploying-scalable-agents/README.md) a spustiteľný notebook [16-python-agent-framework.ipynb](./16-deploying-scalable-agents/code_samples/16-python-agent-framework.ipynb) vytvárajúci produkčného agenta zákazníckej podpory (nástroje, RAG, pamäť, smerovanie modelu, kešovanie odpovedí, ľudské schvaľovanie, vyhodnocovací brána a OpenTelemetry trasovanie), s vývojovými/nasadzovacími/runtime Mermaid diagramami, kontrolou vedomostí, úlohou a výzvou.
- **Lekcia 17 — Vytváranie lokálnych AI agentov s Foundry Local a Qwen.** Nová lekcia [17-creating-local-ai-agents/README.md](./17-creating-local-ai-agents/README.md) a notebook [17-local-agent-foundry-local.ipynb](./17-creating-local-ai-agents/code_samples/17-local-agent-foundry-local.ipynb) vytvárajúci plne lokálneho inžinierskeho asistenta (Qwen volanie funkcií cez Foundry Local, sandboxované nástroje na súbory, lokálny RAG s Chromou, voliteľný lokálny MCP), s diagramami iba lokálneho / lokálneho RAG / volania nástrojov, kontrolou vedomostí, úlohou a výzvou.
- **Testovací pipeline (smoke-test pipeline).** Nový [AI Smoke Test](https://github.com/marketplace/actions/ai-smoke-test) workflow [.github/workflows/smoke-test.yml](../../.github/workflows/smoke-test.yml) plus katalógy pre každú lekciu pod [tests/](./tests/README.md) pre nasaditeľných agentov v Lekciách 01, 04, 05 a 16, s indexovým README mapujúcim každý katalóg na príslušnú lekciu a názov hostovaného agenta. Lekcia 16 získava sekciu "Validácia nasadeného agenta pomocou Smoke Testov"; Lekcie 01/04/05 získavajú voliteľný odkaz na smoke-test.
- **Zručnosti študenta.** Nové zručnosti agenta pod `.agents/skills/`: [deploying-scalable-agents](./.agents/skills/deploying-scalable-agents/SKILL.md), [local-ai-agents](./.agents/skills/local-ai-agents/SKILL.md) (balíkovanie návodov Lekcií 16 a 17) a [testing-course-samples](./.agents/skills/testing-course-samples/SKILL.md) (ako validovať príklady notebookov voči živému Microsoft Foundry / Azure OpenAI prostrediu).
- **Spúšťač validácie notebookov.** Nový [scripts/validate-notebooks.ps1](../../scripts/validate-notebooks.ps1), ktorý vykonáva každý Python notebook bez hlavičky pomocou `nbconvert` a vypisuje maticu PASS/FAIL (plus `results.json`). Automaticky detekuje koreň repozitára a Python, vylučuje nekurzové notebooky (`.venv`, `site-packages`, `translations`, šablóny zručností) a `.NET` notebooky podľa predvoleného nastavenia, a podporuje `-Filter`, `-Timeout`, `-List`, `-IncludeDotnet` a `-Python`.
- **Navigácia v kurze.** Pridané odkazy Predchádzajúca/Nasledujúca lekcia do Lekcií 11–15 (predtým chýbali), takže celý kurz teraz spája 00 → 18 v oboch smeroch.
- **Nové náhľady (thumbnails).** Náhľady pre Lekcie 16 a 17, plus obnovený sociálny obrázok repozitára [images/repo-thumbnailv3.png](./images/repo-thumbnailv3.png) (teraz inzerujúci dve nové lekcie a URL `aka.ms/ai-agents-beginners`).
- **Závislosti** ([requirements.txt](../../requirements.txt)): pridané `foundry-local-sdk` a `chromadb` pre Lekciu 17.

### Zmenené

- **Hlavná tabuľka lekcií v [README.md](./README.md):** Lekcie 16 a 17 teraz odkazujú na svoj obsah (predtým "Čoskoro k dispozícii"); obrázok repozitára aktualizovaný na `repo-thumbnailv3.png`.
- **[STUDY_GUIDE.md](./STUDY_GUIDE.md):** pridané Lekcie 16 a 17 do sprievodcu lekcia po lekcii a do študijných ciest, a sekcia "Validácia nasadených agentov pomocou Smoke Testov".
- **[AGENTS.md](./AGENTS.md):** aktualizovaný počet/popis lekcií (00–18), pridaná sekcia o validácii pomocou smoke-testov, a príklady pomenovania vzoriek pre Lekcie 16/17.
- **[18-securing-ai-agents/README.md](./18-securing-ai-agents/README.md):** "Predchádzajúca lekcia" teraz smeruje na Lekciu 17 (predtým Lekcia 15), čím uzatvára reťazec.
- **Štandardizované odkazy na modely na neumierajúce modely.** Nahradili sa všetky odkazy na `gpt-4o` / `gpt-4o-mini` v celom kurze (dokumentácia, `.env.example`, Python/.NET notebooky a príklady) za `gpt-4.1-mini` — `gpt-4o` (všetky verzie) sa stiahne v roku 2026. Príklad smerovania modelov v Lekcii 16 si zachováva kontrast mala/veľká pomocou `gpt-4.1-mini` (malý) a `gpt-4.1` (veľký). Python notebooky teraz vyberajú model z environmentálnych premenných (`AZURE_AI_MODEL_DEPLOYMENT_NAME` / `AZURE_OPENAI_DEPLOYMENT`) namiesto tvrdého zakódovania mena modelu.

### Poznámky a známe obmedzenia

- **Neboli spustené na živom Azure.** Nové lekcie sú vzdelávacie vzory; spustite a validujte ich vo vlastnom prostredí Microsoft Foundry / Foundry Local. Workflow smoke-test vyžaduje nasadenie agenta lekcie a nastavenie Azure OIDC tajomstiev (`AZURE_CLIENT_ID`, `AZURE_TENANT_ID`, `AZURE_SUBSCRIPTION_ID`) s rolou **Azure AI User** na úrovni projektu Foundry.
- **Lekcia 17 je iba lokálna.** Nemá endpoint Foundry Responses, preto akcia smoke-test sa na ňu nevzťahuje; validujte ju spustením notebooku na vašom pracovisku.

## [Vydané] — 2026-07-06

Toto vydanie migruje kurz na **Azure OpenAI Responses API**, štandardizuje názvy produktov na **Microsoft Foundry** a **Microsoft Agent Framework (MAF)**, ruší GitHub Models, aktualizuje verzie SDK a pridáva nový obsah o lokálnych modeloch a hostovaní iných frameworkov na Foundry.

### Pridané

- **Migračná zručnosť** — Nainštalovaná Agent Skill [`azure-openai-to-responses`](./.agents/skills/azure-openai-to-responses/SKILL.md) (z [Azure-Samples/azure-openai-to-responses](https://github.com/Azure-Samples/azure-openai-to-responses)) pod `.agents/skills/`, vrátane jej odkazov a skriptu skenera.
- **Foundry Local (spúšťanie modelov na zariadení)** — Nová sekcia "Alternatívny poskytovateľ: Foundry Local" v [00-course-setup/README.md](./00-course-setup/README.md) pokrývajúca inštaláciu (`winget` / `brew`), `foundry model run`, `foundry-local-sdk` a prepojenie `FoundryLocalManager` s Microsoft Agent Framework cez `OpenAIChatClient`.
- **Hostovanie LangChain / LangGraph agentov na Microsoft Foundry** — Nová sekcia v [14-microsoft-agent-framework/README.md](./14-microsoft-agent-framework/README.md) plus spustiteľný príklad [14-langchain-hosted-agent.py](../../14-microsoft-agent-framework/code-samples/14-langchain-hosted-agent.py) používajúci `langchain-azure-ai[hosting]` a `ResponsesHostServer` (protokol `/responses`), založený na [Microsoft Learn](https://learn.microsoft.com/azure/foundry/how-to/develop/langchain-hosted-agents).
- **Microsoft Project Opal** — Nová sekcia "Príklad z praxe: Microsoft Project Opal" v [15-browser-use/README.md](./15-browser-use/README.md), ktorá rámcuje Opal ako agenta na podnikové využitie počítača a mapuje ho na koncepty kurzu (human-in-the-loop, dôvera/bezpečnosť, plánovanie, zručnosti).
- **Druhý príklad Lekcie 02 v Pythone** — Pridaný [02-python-agent-framework-azure-openai.ipynb](./02-explore-agentic-frameworks/code_samples/02-python-agent-framework-azure-openai.ipynb) (viď "Zmenené" — migrovaný z bývalého notebooku Semantic Kernel) a prelinkovaný v README lekcie.
- Pridaná sekcia **Modely a poskytovatelia** do [STUDY_GUIDE.md](./STUDY_GUIDE.md).

### Zmenené

- **Chat Completions → Responses API (Python).** Príklady, ktoré volali model priamo, boli migrované z Chat Completions na Responses API (`client.responses.create(input=..., store=False)`, `resp.output_text`), používajúc `OpenAI` klienta proti stabilnému Azure OpenAI `/openai/v1/` endpointu (bez `api_version`). Dotknuté príklady zahŕňajú:
  - [06-building-trustworthy-agents/code_samples/06-system-message-framework.ipynb](./06-building-trustworthy-agents/code_samples/06-system-message-framework.ipynb)
  - [06-building-trustworthy-agents/code_samples/06-human-in-the-loop.ipynb](./06-building-trustworthy-agents/code_samples/06-human-in-the-loop.ipynb)
  - [04-tool-use/README.md](./04-tool-use/README.md) — úplný walkthrough volania funkcií (schéma nástrojov zosúladená na formát Responses, výsledky nástrojov vrátené ako `function_call_output`, `max_output_tokens` atď.).
- **GitHub Models → Azure OpenAI.** GitHub Models sú ukončené (odchod v **júl 2026**) a nepodporujú Responses API. Všetky cesty kódu GitHub Models boli prevedené na Azure OpenAI / Microsoft Foundry v Python a .NET príkladoch:
  - Python: Lekcia 08 workflow notebooky (`01`–`03`), Lekcia 14 (`14-handoff`, `14-human-loop`, `hotel_booking_workflow_sample.py`).
  - .NET: `01`–`04`, `07`, `08` `*-dotnet-agent-framework.cs` + sprievodné `.md` dokumenty a workflow notebooky Lekcie 08 dotNET/`.md` (`01`–`03`) teraz používajú `AzureOpenAIClient(...).GetOpenAIResponseClient(deployment).CreateAIAgent(...)` s `AzureCliCredential`.
- **Semantic Kernel → Microsoft Agent Framework.** Bývalý `02-semantic-kernel.ipynb` bol prepísaný tak, aby používal Microsoft Agent Framework s Azure OpenAI (Responses API) a premenovaný na `02-python-agent-framework-azure-openai.ipynb`.
- **Štandardizácia na `FoundryChatClient` + `as_agent`.** README a kód notebookov, ktoré odkazovali na `AzureAIProjectAgentProvider`, boli štandardizované podľa kanonického vzoru používaného v Lekcii 01 a samostatných príkladoch frameworku: `FoundryChatClient(project_endpoint=..., model=..., credential=AzureCliCredential())` s `provider.as_agent(...)`. Aktualizované v README a notebookoch Lekcií 02–14 (napr. pamäť v Lekcii 13, všetky notebooky Lekcie 14, `11-agentic-protocols/code_samples/github-mcp/app.py`).
- **Názvoslovie produktov.** Premenované v celej anglickej dokumentácii:
  - "Azure AI Foundry" / "Azure AI Studio" → **Microsoft Foundry**
  - "Azure AI Agent Service" → **Microsoft Foundry Agent Service**
  - (Nezmenené: "Azure OpenAI", "Azure AI Search", "Azure AI Inference" a názvy environmentálnych premenných.)
- **Závislosti** ([requirements.txt](../../requirements.txt)):
  - Zamknuté `agent-framework>=1.10.0`, `agent-framework-foundry>=1.10.0`, `agent-framework-openai>=1.10.0`.
  - Zamknuté `openai>=1.108.1` (minimálne pre Responses API).
  - Odstránené `azure-ai-inference` (bolo použité iba v migrovaných príkladoch GitHub Models).
- **Konfigurácia prostredia** ([.env.example](../../.env.example)): odstránené premenné GitHub Models (`GITHUB_TOKEN`, `GITHUB_ENDPOINT`, `GITHUB_MODEL_ID`); pridané `AZURE_OPENAI_ENDPOINT`, `AZURE_OPENAI_DEPLOYMENT` a voliteľné `AZURE_OPENAI_API_KEY`; aktualizované názvy na Microsoft Foundry.
- **Dokumentácia** — Aktualizované [00-course-setup/README.md](./00-course-setup/README.md), [AGENTS.md](./AGENTS.md), [README.md](./README.md) a [STUDY_GUIDE.md](./STUDY_GUIDE.md) zodpovedajúce vyššie uvedeným zmenám (nastavenie env premenných, overovací úryvok, návod poskytovateľa, názvoslovie).

### Odstránené

- Krok po kroku onboardingu GitHub Models a environmentálne premenné z dokumentácie nastavenia (nahradené Azure OpenAI / Microsoft Foundry).

### Bezpečnosť / Súkromie (očistenie verejného zdieľania)

- Vymazané výstupy z vykonávania Jupyter notebookov, ktoré odhaľovali skutočné **ID predplatného Azure**, názvy skupiny zdrojov / zdrojov a ID Bing pripojenia, plus vývojárske **lokálne cesty k súborom a používateľské mená**, v:
  - `08-multi-agent/code_samples/workflows-agent-framework/dotNET/04.dotnet-agent-framework-workflow-aifoundry-condition.ipynb`

  - `08-multi-agent/code_samples/workflows-agent-framework/python/04.python-agent-framework-workflow-aifoundry-condition.ipynb`
  - `15-browser-use/15-browser-user.ipynb`
- Overené, že v sledovanom anglickom obsahu nezostali žiadne API kľúče, tokeny, ID predplatného ani osobné cesty (odkazy na `GITHUB_TOKEN`, ktoré zostali, sú tokeny GitHub Actions vo workflow a PAT servera GitHub MCP v nastavení Lekcie 11 — obe sú legitímne a nesúvisia s GitHub Models).

### Poznámky a známe obmedzenia

- **Nevykonané/neskompilované.** Toto sú vzorové vzdelávacie ukážky aktualizované pre správnosť API/názvov; neboli spustené na živých Azure zdrojoch a .NET ukážky neboli skompilované v tomto prostredí. Overte ich na vlastnom nasadení Microsoft Foundry / Azure OpenAI.
- **Nasadenie modelu musí podporovať Response API.** Použite nasadenie ako `gpt-4.1-mini`, `gpt-4.1` alebo model `gpt-5.x`. Staršie modely podporujú základnú funkcionalitu Response, ale nie všetky funkcie.
- **Verzia agent-framework.** Ukážky sú zamerané na najnovší MAF (`>=1.10.0`). Kanonický volací príkaz na vytvorenie agenta je `client.as_agent(...)`; API boli overené podľa publikovanej dokumentácie frameworku a nainštalovanej zostavy. Ak používate inú verziu, overte dostupnosť metódy (`as_agent` vs `create_agent`).
- **Workflow notebook lekcie 08, 04** zámerne využíva `AzureAIAgentClient` (z `agent-framework-azure-ai`), pretože používa nástroje Microsoft Foundry Agent Service (základ Bing, interpret kódu); je už založený na Responses.
- **Predvolené nasadenie .NET.** Dve ukážky workflow .NET z Lekcie 08 mali predtým pevne zakódovaný špecifický model; teraz používajú predvolený `AZURE_OPENAI_DEPLOYMENT` (`gpt-4.1-mini`). Ak ukážka vyžaduje multimodálny/vizuálny vstup, nastavte `AZURE_OPENAI_DEPLOYMENT` na vhodný model.
- **Foundry Local** poskytuje OpenAI-kompatibilný endpoint **Chat Completions** a je určený na lokálny vývoj; pre plnú funkcionalitu Response API použite Azure OpenAI / Microsoft Foundry.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Vyhlásenie o zodpovednosti**:
Tento dokument bol preložený pomocou AI prekladateľskej služby [Co-op Translator](https://github.com/Azure/co-op-translator). Hoci sa snažíme o presnosť, vezmite prosím na vedomie, že automatické preklady môžu obsahovať chyby alebo nepresnosti. Pôvodný dokument v jeho natívnom jazyku by mal byť považovaný za autoritatívny zdroj. Pre kritické informácie sa odporúča profesionálny ľudský preklad. Nie sme zodpovední za žiadne nedorozumenia alebo nesprávne interpretácie vyplývajúce z použitia tohto prekladu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->