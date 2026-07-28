# Zoznam zmien

Všetky významné zmeny v kurze **AI agenti pre začiatočníkov** sú zdokumentované v tomto súbore.

## [Vydané] — 2026-07-14

Toto vydanie presúva kurz z dvoch novozastaraných modelov, migruje zostávajúce lekčné poznámkové bloky na stabilné rozhranie API Microsoft Agent Framework a overuje Python poznámkové bloky proti aktívnemu nasadeniu Microsoft Foundry.

### Zmenené

- **Presunuté z zastaraných modelov (`gpt-4.1` / `gpt-4.1-mini` → `gpt-5-mini`).** Oba modely `gpt-4.1` a `gpt-4.1-mini` sú teraz zastarané (dátum ukončenia platnosti **14. október 2026**). Nahraďte všetky odkazy v kurze (dokumentácia, `.env.example`, Python/.NET poznámkové bloky a príklady) novým ne-zastaraným modelom `gpt-5-mini`. V ukážke smerovania modelov v lekcii 16 zostáva kontrast malý/veľký s `gpt-5-nano` (malý) a `gpt-5-mini` (veľký). Tretie strany súborov ([15-browser-use/llms.txt](../../15-browser-use/llms.txt)), historický text GitHub Models a poznámky ku schopnostiam zručnosti `azure-openai-to-responses` zostali zámerne nezmenené.
- **Poznámkový blok lekcie 14 handoff migrovaný do stabilného API.** [14-handoff.ipynb](./14-microsoft-agent-framework/code-samples/14-handoff.ipynb) teraz používa `agent_framework.orchestrations.HandoffBuilder` s `.with_start_agent(...)`, `HandoffAgentUserRequest.create_response(...)`, streamovanie na základe `event.type` a `FoundryChatClient` (nahrádza odstránené symboly pre verzie pred 1.0 ako `HandoffBuilder` / `ChatMessage` / `RequestInfoEvent`).
- **Poznámkový blok lekcie 14 human-in-the-loop migrovaný do stabilného API.** [14-human-loop.ipynb](./14-microsoft-agent-framework/code-samples/14-human-loop.ipynb) teraz pauzuje cez `ctx.request_info(...)` + `@response_handler` (nahrádza odstránené `RequestInfoExecutor` / `RequestInfoMessage` / `RequestResponse`), vytvára s `WorkflowBuilder(start_executor=..., output_executors=[...])`, riadi štruktúrovaný výstup cez `default_options={"response_format": ...}`, a používa skriptovanú odpoveď tak, aby poznámkový blok bežal bez obsluhy (bez blokujúceho `input()`).
- **Konfigurácia prostredia** ([.env.example](../../.env.example)): prepnuté názvy nasadení modelov na `gpt-5-mini`; pridané `AZURE_AI_SMALL_MODEL` / `AZURE_AI_LARGE_MODEL` (smerovanie lekcie 16) a predtým chýbajúce `AZURE_OPENAI_CHAT_DEPLOYMENT_NAME` (lekcia 15 využitie prehliadača).
- **Závislosti** ([requirements.txt](../../requirements.txt)): pripnuté verzie `agent-framework`, `agent-framework-foundry` a `agent-framework-openai` na `~=1.10.0` pre samokonzistentnú a overenú sadu (verzia 1.11.0 obsahuje experimentálne zlomové zmeny pre rozhrania používané v týchto lekciách).

### Poznámky a známe obmedzenia

- **Overené naživo na Microsoft Foundry.** Python poznámkové bloky boli spustené bezhlavo pomocou `nbconvert` proti projektu Microsoft Foundry používajúcemu `gpt-5-mini` (a `gpt-5-nano` pre smerovanie lekcie 16). Nasadte ekvivalentné nezastarané modely vo vlastnom projekte; poznámkové bloky čítajú názov nasadenia z `AZURE_AI_MODEL_DEPLOYMENT_NAME` / `AZURE_OPENAI_DEPLOYMENT`.
- **Niektoré lekcie stále vyžadujú dodatočné zdroje.** Lekcia 05 potrebuje Azure AI Search; pracovný tok lekcie 08 s Bing groundingom (`04.python-agent-framework-workflow-aifoundry-condition.ipynb`) potrebuje pripojenie k Bing a Microsoft Foundry Agent Service hostované nástroje; lekcie 13 (Cognee) a 17 (Foundry Local) potrebujú vlastné runtime.

## [Vydané] — 2026-07-13

Toto vydanie pridáva dve nové lekcie, ktoré dokončujú nasadzovací oblúk — škálovanie agentov do Microsoft Foundry a zmenšenie na jedno pracovisko — plus dymovú testovaciu pipeline, obnovenú navigáciu kurzu, nové zručnosti študenta a aktualizovaný branding.

### Pridané

- **Lekcia 16 — Nasadzovanie škálovateľných agentov s Microsoft Foundry.** Nová lekcia [16-deploying-scalable-agents/README.md](./16-deploying-scalable-agents/README.md) a spustiteľný poznámkový blok [16-python-agent-framework.ipynb](./16-deploying-scalable-agents/code_samples/16-python-agent-framework.ipynb) budujúci produkčného zákazníckeho podporného agenta (nástroje, RAG, pamäť, smerovanie modelu, cachovanie odpovedí, ľudské schvaľovanie, hodnotiaca brána a sledovanie OpenTelemetry), s diagramami vývoja/nasadenia/runtime v Mermaid, kontrolou vedomostí, úlohou a výzvou.
- **Lekcia 17 — Vytváranie lokálnych AI agentov s Foundry Local a Qwen.** Nová lekcia [17-creating-local-ai-agents/README.md](./17-creating-local-ai-agents/README.md) a poznámkový blok [17-local-agent-foundry-local.ipynb](./17-creating-local-ai-agents/code_samples/17-local-agent-foundry-local.ipynb) budujúci plne na zariadení pracujúceho inžinierskeho asistenta (volanie funkcií Qwen cez Foundry Local, sandboxované súborové nástroje, lokálny RAG s Chromou, voliteľný lokálny MCP), s diagramami pre lokálne/ lokálny RAG / volanie nástrojov, kontrolou vedomostí, úlohou a výzvou.
- **Dymová testovacia pipeline.** Nový pracovný tok [AI Smoke Test](https://github.com/marketplace/actions/ai-smoke-test) [.github/workflows/smoke-test.yml](../../.github/workflows/smoke-test.yml) plus katalógy pre jednotlivé lekcie pod [tests/](./tests/README.md) pre nasaditeľných agentov v lekciách 01, 04, 05 a 16, s indexovým README spájajúcim každý katalóg s lekciou a menom hostovaného agenta. Lekcia 16 získava sekciu "Validácia nasadeného agenta dymovými testami"; lekcie 01/04/05 pridávajú voliteľný odkaz na dymový test.
- **Zručnosti študenta.** Nové Agent Skills v `.agents/skills/`: [deploying-scalable-agents](./.agents/skills/deploying-scalable-agents/SKILL.md), [local-ai-agents](./.agents/skills/local-ai-agents/SKILL.md) (balíčok vedení z lekcií 16 a 17) a [testing-course-samples](./.agents/skills/testing-course-samples/SKILL.md) (ako overiť vzorky poznámkových blokov proti živému Microsoft Foundry / Azure OpenAI nastaveniu).
- **Spúšťač validácie poznámkových blokov.** Nový [scripts/validate-notebooks.ps1](../../scripts/validate-notebooks.ps1) ktorý vykoná každých Python poznámkový blok bezhlavo pomocou `nbconvert` a vytlačí matica PASS/FAIL (plus `results.json`). Automaticky zisťuje koreň repozitára a Python, štandardne vylučuje nepokryté poznámkové bloky (`.venv`, `site-packages`, `translations`, šablóny zručností) a `.NET` poznámkové bloky, podporuje `-Filter`, `-Timeout`, `-List`, `-IncludeDotnet` a `-Python`.
- **Navigácia kurzu.** Pridané odkazy Precedujúca/Nasledujúca lekcia pre lekcie 11–15 (predtým chýbajúce), takže celý kurz teraz reťazí 00 → 18 v oboch smeroch.
- **Nové náhľady.** Náhľady lekcií 16 a 17, a obnovený sociálny obrázok repozitára [images/repo-thumbnailv3.png](./images/repo-thumbnailv3.png) (teraz propagujúci dve nové lekcie a URL `aka.ms/ai-agents-beginners`).
- **Závislosti** ([requirements.txt](../../requirements.txt)): pridané `foundry-local-sdk` a `chromadb` pre lekciu 17.

### Zmenené

- **Hlavná tabuľka lekcií v [README.md](./README.md):** Lekcie 16 a 17 teraz odkazujú na svoj obsah (predtým "Čoskoro k dispozícii"); obrázok repozitára aktualizovaný na `repo-thumbnailv3.png`.
- **[STUDY_GUIDE.md](./STUDY_GUIDE.md):** pridané lekcie 16 a 17 do sprievodcu lekciou po lekcii a učebných ciest, a sekciu "Validácia nasadených agentov dymovými testami".
- **[AGENTS.md](./AGENTS.md):** aktualizovaný počet/ popis lekcií (00–18), pridaná sekcia validácie dymového testovania, a príklady pomenovania vzoriek lekcií 16 a 17.
- **[18-securing-ai-agents/README.md](./18-securing-ai-agents/README.md):** „Predchádzajúca lekcia“ teraz ukazuje na lekciu 17 (predtým to bola lekcia 15), čím sa reťaz uzatvára.
- **Štandardizované odkazy na modely na nezastarané modely.** Vymenené všetky odkazy `gpt-4o` / `gpt-4o-mini` v celom kurze (dokumentácia, `.env.example`, Python/.NET poznámkové bloky a príklady) za `gpt-4.1-mini` — `gpt-4o` (všetky verzie) bude ukončený v roku 2026. V ukážke smerovania modelov v lekcii 16 zostáva kontrast malý/veľký s `gpt-4.1-mini` (malý) a `gpt-4.1` (veľký). Python poznámkové bloky teraz vyberajú model z premenných prostredia (`AZURE_AI_MODEL_DEPLOYMENT_NAME` / `AZURE_OPENAI_DEPLOYMENT`) namiesto pevne zakódovaného mena modelu.

### Poznámky a známe obmedzenia

- **Nepoužité proti aktívnemu Azure.** Nové lekcie sú vzorové učebné príklady; spúšťajte a overujte ich vo svojom vlastnom nastavení Microsoft Foundry / Foundry Local. Pracovný tok dymového testu vyžaduje nasadenie agenta lekcie a konfiguráciu Azure OIDC tajomstiev (`AZURE_CLIENT_ID`, `AZURE_TENANT_ID`, `AZURE_SUBSCRIPTION_ID`) s rolou **Azure AI User** v rozsahu projektu Foundry.
- **Lekcia 17 je len lokálna.** Nemá koncový bod Foundry Responses, takže dymový test sa na ňu nevzťahuje; overte ju spustením poznámkového bloku na svojom pracovisku.

## [Vydané] — 2026-07-06

Toto vydanie migruje kurz na **Azure OpenAI Responses API**, štandardizuje názvy produktov na **Microsoft Foundry** a **Microsoft Agent Framework (MAF)**, ukončuje GitHub Models, aktualizuje verzie SDK a pridáva nový obsah o lokálnych modeloch a hostovaní iných frameworkov na Foundry.

### Pridané

- **Migračná zručnosť** — Inštalovaná zručnosť agenta [`azure-openai-to-responses`](./.agents/skills/azure-openai-to-responses/SKILL.md) (z [Azure-Samples/azure-openai-to-responses](https://github.com/Azure-Samples/azure-openai-to-responses)) v `.agents/skills/`, vrátane odkazov a skriptu skenera.
- **Foundry Local (spúšťanie modelov na zariadení)** — Nová sekcia "Alternatívny poskytovateľ: Foundry Local" v [00-course-setup/README.md](./00-course-setup/README.md) pokrývajúca inštaláciu (`winget` / `brew`), `foundry model run`, `foundry-local-sdk` a prepojenie `FoundryLocalManager` na Microsoft Agent Framework cez `OpenAIChatClient`.
- **Hostovanie agentov LangChain / LangGraph na Microsoft Foundry** — Nová sekcia v [14-microsoft-agent-framework/README.md](./14-microsoft-agent-framework/README.md) plus spustiteľný príklad [14-langchain-hosted-agent.py](../../14-microsoft-agent-framework/code-samples/14-langchain-hosted-agent.py) používajúci `langchain-azure-ai[hosting]` a `ResponsesHostServer` (protokol `/responses`), na základe [Microsoft Learn](https://learn.microsoft.com/azure/foundry/how-to/develop/langchain-hosted-agents).
- **Microsoft Project Opal** — Nová sekcia "Príklad zo skutočného sveta: Microsoft Project Opal" v [15-browser-use/README.md](./15-browser-use/README.md) rámcujúca Opal ako podnikateľského agenta na použitie počítača a mapujúca ho na koncepty kurzu (ľud v slučke, dôvera/bezpečnosť, plánovanie, Zručnosti).
- **Druhý vzorový Python kód pre lekciu 02** — Pridaný [02-python-agent-framework-azure-openai.ipynb](./02-explore-agentic-frameworks/code_samples/02-python-agent-framework-azure-openai.ipynb) (pozri "Zmenené" — migrovaný z bývalého Semantic Kernel poznámkového bloku) a prepojený v README lekcie.
- **Sekcia Modely a poskytovatelia** pridaná do [STUDY_GUIDE.md](./STUDY_GUIDE.md).

### Zmenené

- **Chat Completions → Responses API (Python).** Vzorky, ktoré volali model priamo, boli migrované z Chat Completions na Responses API (`client.responses.create(input=..., store=False)`, `resp.output_text`), používajúc klienta `OpenAI` proti stabilnému Azure OpenAI `/openai/v1/` koncovému bodu (bez `api_version`). Postihnuté vzorky zahŕňajú:
  - [06-building-trustworthy-agents/code_samples/06-system-message-framework.ipynb](./06-building-trustworthy-agents/code_samples/06-system-message-framework.ipynb)
  - [06-building-trustworthy-agents/code_samples/06-human-in-the-loop.ipynb](./06-building-trustworthy-agents/code_samples/06-human-in-the-loop.ipynb)
  - [04-tool-use/README.md](./04-tool-use/README.md) — úplný prechod funkcie volania (schéma nástroja zjednodušená do formátu Responses, výsledky nástroja vrátené ako `function_call_output`, `max_output_tokens` atď.).

- **GitHub Models → Azure OpenAI.** GitHub Models je zastaraný (odchod **júl 2026**) a nepodporuje Responses API. Všetky GitHub Models kódy boli prevedené na Azure OpenAI / Microsoft Foundry v ukážkach pre Python a .NET:
  - Python: pracovné zošity Lesson 08 (`01`–`03`), Lesson 14 (`14-handoff`, `14-human-loop`, `hotel_booking_workflow_sample.py`).
  - .NET: `01`–`04`, `07`, `08` `*-dotnet-agent-framework.cs` + doplnkové `.md` dokumenty, a pracovné zošity/`.md` Lesson 08 dotNET (`01`–`03`) teraz používajú `AzureOpenAIClient(...).GetOpenAIResponseClient(deployment).CreateAIAgent(...)` s `AzureCliCredential`.
- **Semantic Kernel → Microsoft Agent Framework.** Pôvodný `02-semantic-kernel.ipynb` bol prepísaný tak, aby používal Microsoft Agent Framework s Azure OpenAI (Responses API) a premenovaný na `02-python-agent-framework-azure-openai.ipynb`.
- **Štandardizácia na `FoundryChatClient` + `as_agent`.** README a kód v zošitoch, ktoré odkazovali na `AzureAIProjectAgentProvider`, boli štandardizované na kanonický vzor používaný v Lesson 01 a ukážkach frameworku: `FoundryChatClient(project_endpoint=..., model=..., credential=AzureCliCredential())` s `provider.as_agent(...)`. Aktualizované v README a zošitoch od Lesson 02 do 14 (napr. Lesson 13 pamäť, všetky zošity Lesson 14, `11-agentic-protocols/code_samples/github-mcp/app.py`).
- **Produktové pomenovanie.** Premenované v celom anglickom obsahu:
  - "Azure AI Foundry" / "Azure AI Studio" → **Microsoft Foundry**
  - "Azure AI Agent Service" → **Microsoft Foundry Agent Service**
  - (Bez zmeny: "Azure OpenAI", "Azure AI Search", "Azure AI Inference" a názvy environmentálnych premenných.)
- **Závislosti** ([requirements.txt](../../requirements.txt)):
  - Pripnuté `agent-framework>=1.10.0`, `agent-framework-foundry>=1.10.0`, `agent-framework-openai>=1.10.0`.
  - Pripnuté `openai>=1.108.1` (minimálne pre Responses API).
  - Odstránený `azure-ai-inference` (bolo používané iba v migrovaných ukážkach GitHub Models).
- **Konfigurácia prostredia** ([.env.example](../../.env.example)): odstránené premenné GitHub Models (`GITHUB_TOKEN`, `GITHUB_ENDPOINT`, `GITHUB_MODEL_ID`); pridané `AZURE_OPENAI_ENDPOINT`, `AZURE_OPENAI_DEPLOYMENT` a voliteľné `AZURE_OPENAI_API_KEY`; aktualizované pomenovanie na Microsoft Foundry.
- **Dokumentácia** — Aktualizované [00-course-setup/README.md](./00-course-setup/README.md), [AGENTS.md](./AGENTS.md), [README.md](./README.md) a [STUDY_GUIDE.md](./STUDY_GUIDE.md) pre vyššie uvedené (nastavenie environmentálnych premenných, overovací útržok, návody k poskytovateľovi, pomenovanie).

### Odstránené

- Krok začiatočníka GitHub Models a environmentálne premenné z inštrukcií pre nastavenie (nahradené Azure OpenAI / Microsoft Foundry).

### Bezpečnosť / Ochrana osobných údajov (čistenie verejných zdieľaní)

- Vymazané výstupy spustenia Jupyter notebookov, ktoré unikli skutočné **ID predplatného Azure**, názvy resource-group / resource, a ID pripojenia Bing, plus vývojárske **lokálne cesty k súborom a používateľské mená**, v:
  - `08-multi-agent/code_samples/workflows-agent-framework/dotNET/04.dotnet-agent-framework-workflow-aifoundry-condition.ipynb`
  - `08-multi-agent/code_samples/workflows-agent-framework/python/04.python-agent-framework-workflow-aifoundry-condition.ipynb`
  - `15-browser-use/15-browser-user.ipynb`
- Overené, že žiadne API kľúče, tokeny, ID predplatného alebo osobné cesty nezostali v sledovanom anglickom obsahu (zvyšné odkazy na `GITHUB_TOKEN` sú token GitHub Actions v workflowoch a GitHub MCP server PAT v nastavení Lesson 11 — obidva legitímne a nesúvisiace s GitHub Models).

### Poznámky a známe obmedzenia

- **Nie sú spustené/kompilované.** Ide o vzdelávacie ukážky aktualizované pre správnosť API/pomenovania; neboli spustené proti reálnym Azure zdrojom a .NET ukážky neboli skompilované v tomto prostredí. Validujte na vlastnom nasadení Microsoft Foundry / Azure OpenAI.
- **Nasadenie modelu musí podporovať Responses API.** Použite nasadenie ako `gpt-4.1-mini`, `gpt-4.1`, alebo model `gpt-5.x`. Staršie modely podporujú základné funkcie Responses, ale nie všetky.
- **Verzia agent-framework.** Ukážky cília na najnovší MAF (`>=1.10.0`). Kanonický volací spôsob agent-creation je `client.as_agent(...)`; API boli overené podľa publikovanej dokumentácie frameworku a nainštalovanej kompilácie. Ak používate inú verziu, overte dostupnosť metódy (`as_agent` vs `create_agent`).
- **Pracovný zošit Lesson 08 workflow 04** zámerne ponecháva `AzureAIAgentClient` (z `agent-framework-azure-ai`), pretože využíva nástroje Microsoft Foundry Agent Service (Bing grounding, interpret kódu); už je založený na Responses.
- **Predvolené nasadenie .NET.** Dve ukážky pracovného postupu Lesson 08 dotNET predtým pevne kódovali konkrétny model; teraz majú predvolené `AZURE_OPENAI_DEPLOYMENT` (`gpt-4.1-mini`). Ak ukážka vyžaduje multimodálny/vizuálny vstup, nastavte `AZURE_OPENAI_DEPLOYMENT` na vhodný model.
- **Foundry Local** vystavuje endpoint kompatibilný s OpenAI **Chat Completions** a je určený pre lokálny vývoj; pre plnú funkčnosť Responses API používajte Azure OpenAI / Microsoft Foundry.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Vyhlásenie o zodpovednosti**:
Tento dokument bol preložený pomocou AI prekladateľskej služby [Co-op Translator](https://github.com/Azure/co-op-translator). Hoci sa snažíme o presnosť, vezmite prosím na vedomie, že automatické preklady môžu obsahovať chyby alebo nepresnosti. Pôvodný dokument v jeho natívnom jazyku by mal byť považovaný za autoritatívny zdroj. Pre kritické informácie sa odporúča profesionálny ľudský preklad. Nie sme zodpovední za žiadne nedorozumenia alebo nesprávne interpretácie vyplývajúce z použitia tohto prekladu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->