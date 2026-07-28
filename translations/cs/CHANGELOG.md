# Změny

Veškeré významné změny kurzu **AI Agents for Beginners** jsou zdokumentovány v tomto souboru.

## [Vydáno] — 2026-07-14

Toto vydání přesunulo kurz z dvou nově zastaralých modelů, migrovalo zbylé Lekce sešity na stabilní Microsoft Agent Framework API a ověřilo Python sešity proti nasazení Microsoft Foundry v reálném čase.

### Změněno

- **Přesun z zastaralých modelů (`gpt-4.1` / `gpt-4.1-mini` → `gpt-5-mini`).** Oba modely `gpt-4.1` a `gpt-4.1-mini` jsou nyní zastaralé (oficiální datum ukončení je **14. října 2026**). Nahrazeny všechny odkazy v kurzu (dokumentace, `.env.example`, Python/.NET sešity a příklady) novým, nezastaralým modelem `gpt-5-mini`. Příklad směrování modelů v Lekci 16 zachovává kontrast malý/velký pomocí `gpt-5-nano` (malý) a `gpt-5-mini` (velký). Zahrnuté externí soubory ([15-browser-use/llms.txt](../../15-browser-use/llms.txt)), historický text GitHub Models a poznámky schopností dovednosti `azure-openai-to-responses` byly záměrně ponechány beze změny.
- **Sešit předání v Lekci 14 byl migrován na stabilní API.** [14-handoff.ipynb](./14-microsoft-agent-framework/code-samples/14-handoff.ipynb) nyní používá `agent_framework.orchestrations.HandoffBuilder` s `.with_start_agent(...)`, `HandoffAgentUserRequest.create_response(...)`, proudové zpracování založené na `event.type` a `FoundryChatClient` (nahrazující odstraněné symboly `HandoffBuilder`/`ChatMessage`/`RequestInfoEvent` před verzí 1.0).
- **Sešit s lidským zapojením v Lekci 14 byl migrován na stabilní API.** [14-human-loop.ipynb](./14-microsoft-agent-framework/code-samples/14-human-loop.ipynb) nyní přerušuje přes `ctx.request_info(...)` + `@response_handler` (nahrazující odstraněné `RequestInfoExecutor` / `RequestInfoMessage` / `RequestResponse`), staví s `WorkflowBuilder(start_executor=..., output_executors=[...])`, vede strukturovaný výstup skrze `default_options={"response_format": ...}`, a používá skriptovanou odpověď, takže sešit běží automaticky (bez blokujícího `input()`).
- **Konfigurace prostředí** ([.env.example](../../.env.example)): změněny názvy nasazení modelů na `gpt-5-mini`; přidáno `AZURE_AI_SMALL_MODEL` / `AZURE_AI_LARGE_MODEL` (směrování v Lekci 16) a dříve chybějící `AZURE_OPENAI_CHAT_DEPLOYMENT_NAME` (pro použití v prohlížeči v Lekci 15).
- **Závislosti** ([requirements.txt](../../requirements.txt)): připnuty verze `agent-framework`, `agent-framework-foundry` a `agent-framework-openai` na `~=1.10.0` pro samosprávný, ověřený set (verze 1.11.0 obsahuje experimentální nekompatibilní změny v rozhraní používaném v těchto lekcích).

### Poznámky a známá omezení

- **Ověřeno vůči živému Microsoft Foundry.** Python sešity byly spuštěny bez uživatelského rozhraní pomocí `nbconvert` proti Microsoft Foundry projektu s modelem `gpt-5-mini` (a `gpt-5-nano` pro směrování v Lekci 16). Ve vašem vlastním projektu nasaďte ekvivalentní nezastaralé modely; sešity čtou název nasazení z `AZURE_AI_MODEL_DEPLOYMENT_NAME` / `AZURE_OPENAI_DEPLOYMENT`.
- **Některé lekce stále vyžadují dodatečné zdroje.** Lekce 05 potřebuje Azure AI Search; workflow Lekce 08 Bing grounding (`04.python-agent-framework-workflow-aifoundry-condition.ipynb`) potřebuje Bing připojení a hostované nástroje Microsoft Foundry Agent Service; Lekce 13 (Cognee) a Lekce 17 (Foundry Local) potřebují vlastní runtime.

## [Vydáno] — 2026-07-13

Toto vydání přidává dvě nové lekce, které uzavírají nasazovací oblouk — škálování agentů do Microsoft Foundry a zpět na jedno stanoviště — plus testovací pipeline, aktualizováno navigování kurzu, nové schopnosti pro studenty a aktualizované značkování.

### Přidáno

- **Lekce 16 — Nasazení škálovatelných agentů s Microsoft Foundry.** Nová lekce [16-deploying-scalable-agents/README.md](./16-deploying-scalable-agents/README.md) a spustitelný sešit [16-python-agent-framework.ipynb](./16-deploying-scalable-agents/code_samples/16-python-agent-framework.ipynb) stavějící produkčního zákaznického podpůrného agenta (nástroje, RAG, paměť, směrování modelů, ukládání odpovědí, lidské schválení, brána hodnocení a OpenTelemetry tracing), s vývojovými/nasazovacími/runtime diagramy v Mermaid, kontrolou znalostí, zadáním a výzvou.
- **Lekce 17 — Vytváření lokálních AI agentů pomocí Foundry Local a Qwen.** Nová lekce [17-creating-local-ai-agents/README.md](./17-creating-local-ai-agents/README.md) a sešit [17-local-agent-foundry-local.ipynb](./17-creating-local-ai-agents/code_samples/17-local-agent-foundry-local.ipynb) stavějící plně on-device inženýrského asistenta (volání funkcí Qwen přes Foundry Local, sandboxované nástroje pro soubory, lokální RAG s Chromou, volitelný lokální MCP), s diagramy pouze pro lokální provoz / lokální RAG / volání nástrojů, kontrolou znalostí, zadáním a výzvou.
- **Testovací pipeline.** Nový workflow [AI Smoke Test](https://github.com/marketplace/actions/ai-smoke-test) [.github/workflows/smoke-test.yml](../../.github/workflows/smoke-test.yml) a katalogy pro každou lekci v [tests/](./tests/README.md) pro nasaditelné agenty v Lekcích 01, 04, 05 a 16, s indexovým README mapujícím každý katalog na lekci a jméno hostovaného agenta. Lekce 16 získává sekci "Ověření nasazeného agenta pomocí smoke testů"; Lekce 01/04/05 získávají nepovinný indikátor smoke testů.
- **Schopnosti studenta.** Nové dovednosti agentů v `.agents/skills/`: [deploying-scalable-agents](./.agents/skills/deploying-scalable-agents/SKILL.md), [local-ai-agents](./.agents/skills/local-ai-agents/SKILL.md) (zahrnující pokyny z lekcí 16 a 17) a [testing-course-samples](./.agents/skills/testing-course-samples/SKILL.md) (jak ověřit příklady v sešitech proti živému Microsoft Foundry / Azure OpenAI nasazení).
- **Spouštěč ověření sešitů.** Nový skript [scripts/validate-notebooks.ps1](../../scripts/validate-notebooks.ps1), který spustí každý Python sešit bez uživatelského rozhraní pomocí `nbconvert` a vypíše matici PASS/FAIL (a `results.json`). Automaticky detekuje kořen repozitáře a Python, ve výchozím nastavení vynechá nesešitové adresáře (`.venv`, `site-packages`, `translations`, zdroje šablon dovedností) a `.NET` sešity, a podporuje parametry `-Filter`, `-Timeout`, `-List`, `-IncludeDotnet` a `-Python`.
- **Navigace kurzu.** Přidány odkazy Předchozí/Následující lekce do lekcí 11–15 (dříve chyběly), takže celý kurz nyní řetězí 00 → 18 v obou směrech.
- **Nové miniatury.** Miniatury lekcí pro Lekce 16 a 17, plus obnovený sociální obrázek repozitáře [images/repo-thumbnailv3.png](./images/repo-thumbnailv3.png) (nyní propagující dvě nové lekce a URL `aka.ms/ai-agents-beginners`).
- **Závislosti** ([requirements.txt](../../requirements.txt)): přidány `foundry-local-sdk` a `chromadb` pro Lekci 17.

### Změněno

- **Hlavní tabulka lekcí v [README.md](./README.md)**: Lekce 16 a 17 nyní odkazují na svůj obsah (dříve "Brzy k dispozici"); obrázek repozitáře aktualizován na `repo-thumbnailv3.png`.
- **[STUDY_GUIDE.md](./STUDY_GUIDE.md)**: přidány Lekce 16 a 17 do průvodce lekce po lekci a do učebních cest, a sekce "Ověření nasazených agentů pomocí smoke testů".
- **[AGENTS.md](./AGENTS.md)**: aktualizován počet/popis lekcí (00–18), přidána sekce pro validaci smoke testů a přidány příklady pojmenování vzorků pro Lekce 16/17.
- **[18-securing-ai-agents/README.md](./18-securing-ai-agents/README.md)**: odkaz "Předchozí lekce" nyní ukazuje na Lekci 17 (původně Lekce 15), tím se uzavírá řetězec.
- **Standardizované odkazy na modely na nezastaralé modely.** Nahrazeny všechny odkazy `gpt-4o` / `gpt-4o-mini` v kurzu (dokumentace, `.env.example`, Python/.NET sešity a příklady) modelem `gpt-4.1-mini` — `gpt-4o` (všechny verze) bude ukončen v roce 2026. Příklad směrování modelů v Lekci 16 zachovává kontrast malý/velký pomocí `gpt-4.1-mini` (malý) a `gpt-4.1` (velký). Python sešity nyní vybírají model z proměnných prostředí (`AZURE_AI_MODEL_DEPLOYMENT_NAME` / `AZURE_OPENAI_DEPLOYMENT`) místo pevného zadání názvu modelu.

### Poznámky a známá omezení

- **Neprověřeno proti živému Azure.** Nové sešity lekcí jsou ukázkové příklady; spusťte a ověřte je proti vlastnímu prostředí Microsoft Foundry / Foundry Local. Smoke-test workflow vyžaduje nasazení lekčního agenta a konfiguraci Azure OIDC tajemství (`AZURE_CLIENT_ID`, `AZURE_TENANT_ID`, `AZURE_SUBSCRIPTION_ID`) s rolí **Azure AI User** na úrovni projektu Foundry.
- **Lekce 17 je pouze lokální.** Nemá endpoint Foundry Responses, proto na ni smoke-test akce neplatí; ověřte ji spuštěním sešitu na svém pracovním stanovišti.

## [Vydáno] — 2026-07-06

Toto vydání migruje kurz na **Azure OpenAI Responses API**, standardizuje názvy produktů na **Microsoft Foundry** a **Microsoft Agent Framework (MAF)**, ukončuje GitHub Models, aktualizuje verze SDK a přidává nový obsah o lokálních modelech a hostování jiných frameworků na Foundry.

### Přidáno

- **Migrační dovednost** — Nainstalovaná Agent Skill [`azure-openai-to-responses`](./.agents/skills/azure-openai-to-responses/SKILL.md) (z [Azure-Samples/azure-openai-to-responses](https://github.com/Azure-Samples/azure-openai-to-responses)) pod `.agents/skills/`, včetně jeho odkazů a skenovacího skriptu.
- **Foundry Local (spouštění modelů lokálně na zařízení)** — Nová sekce "Alternativní poskytovatel: Foundry Local" v [00-course-setup/README.md](./00-course-setup/README.md), pokrývající instalaci (`winget` / `brew`), `foundry model run`, `foundry-local-sdk` a propojení `FoundryLocalManager` s Microsoft Agent Framework přes `OpenAIChatClient`.
- **Hostování agentů LangChain / LangGraph na Microsoft Foundry** — Nová sekce v [14-microsoft-agent-framework/README.md](./14-microsoft-agent-framework/README.md) plus spustitelný příklad [14-langchain-hosted-agent.py](../../14-microsoft-agent-framework/code-samples/14-langchain-hosted-agent.py) používající `langchain-azure-ai[hosting]` a `ResponsesHostServer` (protokol `/responses`), založený na [Microsoft Learn](https://learn.microsoft.com/azure/foundry/how-to/develop/langchain-hosted-agents).
- **Microsoft Project Opal** — Nová sekce "Reálný příklad: Microsoft Project Opal" v [15-browser-use/README.md](./15-browser-use/README.md) uvádějící Opal jako agenta pro podnikové počítačové použití a mapující ho na koncepty kurzu (lidské zapojení, důvěra/bezpečnost, plánování, Dovednosti).
- **Druhý Python příklad k Lekci 02** — Přidán [02-python-agent-framework-azure-openai.ipynb](./02-explore-agentic-frameworks/code_samples/02-python-agent-framework-azure-openai.ipynb) (viz "Změněno" — migrováno ze starého Semantic Kernel sešitu) a propojen v README lekce.
- Přidána sekce "Models and Providers" do [STUDY_GUIDE.md](./STUDY_GUIDE.md).

### Změněno

- **Chat Completions → Responses API (Python).** Příklady, které volaly model přímo, byly migrovány z Chat Completions na Responses API (`client.responses.create(input=..., store=False)`, `resp.output_text`), s využitím `OpenAI` klienta proti stabilnímu Azure OpenAI `/openai/v1/` endpointu (bez `api_version`). Ovlivněné příklady zahrnují:
  - [06-building-trustworthy-agents/code_samples/06-system-message-framework.ipynb](./06-building-trustworthy-agents/code_samples/06-system-message-framework.ipynb)
  - [06-building-trustworthy-agents/code_samples/06-human-in-the-loop.ipynb](./06-building-trustworthy-agents/code_samples/06-human-in-the-loop.ipynb)
  - [04-tool-use/README.md](./04-tool-use/README.md) — kompletní průvodce funkčním voláním (schéma nástrojů převedeno na formát Responses, výsledky nástrojů vráceny jako `function_call_output`, `max_output_tokens` atd.).

- **GitHub Models → Azure OpenAI.** GitHub Models je zastaralý (ukončení **červenec 2026**) a nepodporuje Responses API. Všechny cesty kódu GitHub Models byly převedeny na Azure OpenAI / Microsoft Foundry v ukázkách pro Python a .NET:
  - Python: poznámkové bloky workflow Lesson 08 (`01`–`03`), Lesson 14 (`14-handoff`, `14-human-loop`, `hotel_booking_workflow_sample.py`).
  - .NET: `01`–`04`, `07`, `08` `*-dotnet-agent-framework.cs` + doprovodné `.md` dokumenty a poznámkové bloky/`.md` workflow Lesson 08 dotNET (`01`–`03`) nyní používají `AzureOpenAIClient(...).GetOpenAIResponseClient(deployment).CreateAIAgent(...)` s `AzureCliCredential`.
- **Semantic Kernel → Microsoft Agent Framework.** Původní `02-semantic-kernel.ipynb` byl přepsán pro použití Microsoft Agent Framework s Azure OpenAI (Responses API) a přejmenován na `02-python-agent-framework-azure-openai.ipynb`.
- **Standardizováno na `FoundryChatClient` + `as_agent`.** Kód README a poznámkových bloků, který odkazoval na `AzureAIProjectAgentProvider`, byl standardizován na kanonický vzor použitý v Lesson 01 a vlastních ukázkách frameworku: `FoundryChatClient(project_endpoint=..., model=..., credential=AzureCliCredential())` s `provider.as_agent(...)`. Aktualizováno v README a poznámkových blocích lekcí 02–14 (např. paměť Lesson 13, všechny poznámkové bloky Lesson 14, `11-agentic-protocols/code_samples/github-mcp/app.py`).
- **Pojmenování produktu.** Přejmenováno napříč anglickým obsahem:
  - "Azure AI Foundry" / "Azure AI Studio" → **Microsoft Foundry**
  - "Azure AI Agent Service" → **Microsoft Foundry Agent Service**
  - (Beze změny: "Azure OpenAI", "Azure AI Search", "Azure AI Inference" a názvy proměnných prostředí.)
- **Závislosti** ([requirements.txt](../../requirements.txt)):
  - Stanoveny verze `agent-framework>=1.10.0`, `agent-framework-foundry>=1.10.0`, `agent-framework-openai>=1.10.0`.
  - Stanovena verze `openai>=1.108.1` (minimálně pro Responses API).
  - Odebrán `azure-ai-inference` (byl používán pouze ve zmigrovaných ukázkách GitHub Models).
- **Konfigurace prostředí** ([.env.example](../../.env.example)): odstraněny proměnné GitHub Models (`GITHUB_TOKEN`, `GITHUB_ENDPOINT`, `GITHUB_MODEL_ID`); přidány `AZURE_OPENAI_ENDPOINT`, `AZURE_OPENAI_DEPLOYMENT` a volitelně `AZURE_OPENAI_API_KEY`; aktualizováno pojmenování na Microsoft Foundry.
- **Dokumentace** — aktualizovány [00-course-setup/README.md](./00-course-setup/README.md), [AGENTS.md](./AGENTS.md), [README.md](./README.md) a [STUDY_GUIDE.md](./STUDY_GUIDE.md) dle výše uvedeného (nastavení env proměnných, ověřovací útržek, doporučení poskytovatele, pojmenování).

### Odstraněno

- Krok zařazení GitHub Models a proměnné prostředí z instalačních dokumentů (nahrazeno Azure OpenAI / Microsoft Foundry).

### Zabezpečení / Soukromí (vyčištění veřejného sdílení)

- Vyčištěny výstupy z Jupyter poznámkových bloků, které odhalovaly skutečné **ID Azure předplatného**, názvy resource-groups / zdrojů a Bing connection ID, a také vývojářské **místní cesty k souborům a uživatelská jména**, ve:
  - `08-multi-agent/code_samples/workflows-agent-framework/dotNET/04.dotnet-agent-framework-workflow-aifoundry-condition.ipynb`
  - `08-multi-agent/code_samples/workflows-agent-framework/python/04.python-agent-framework-workflow-aifoundry-condition.ipynb`
  - `15-browser-use/15-browser-user.ipynb`
- Ověřeno, že v sledovaném anglickém obsahu nezůstaly žádné API klíče, tokeny, ID předplatného ani osobní cesty (ze zbytků `GITHUB_TOKEN` jsou token GitHub Actions v pracovních postupech a GitHub MCP server PAT v nastavení Lekce 11 — oba legitimní a nesouvisející s GitHub Models).

### Poznámky a známá omezení

- **Nespouštěno/nesestavováno.** Jedná se o vzdělávací ukázky aktualizované pro správnost API/pojmenování; nebyly prováděny vůči živým Azure zdrojům a .NET ukázky v tomto prostředí nesestaveny. Ověřte na vlastní nasazení Microsoft Foundry / Azure OpenAI.
- **Nasazení modelu musí podporovat Responses API.** Použijte nasazení jako `gpt-4.1-mini`, `gpt-4.1` nebo model `gpt-5.x`. Starší modely podporují základní funkcionalitu Responses, ale nikoli všechny funkce.
- **Verze agent-frameworku.** Ukázky cílí na nejnovější MAF (`>=1.10.0`). Kanonické volání pro tvorbu agenta je `client.as_agent(...)`; API bylo ověřeno podle zveřejněné dokumentace frameworku a nainstalované sestavení. Pokud připnete jinou verzi, ověřte dostupnost metody (`as_agent` vs `create_agent`).
- **Workflow poznámkový blok Lesson 08 04** záměrně zachovává `AzureAIAgentClient` (z `agent-framework-azure-ai`), protože používá nástroje hostované Microsoft Foundry Agent Service (Bing grounding, code interpreter); již je založený na Responses.
- **.NET výchozí nasazení.** Dvě ukázky workflow Lesson 08 dotNET dříve pevně kódovaly konkrétní model; nyní defaultně používají `AZURE_OPENAI_DEPLOYMENT` (`gpt-4.1-mini`). Pokud ukázka spoléhá na multimodální/vizuální vstup, nastavte `AZURE_OPENAI_DEPLOYMENT` na vhodný model.
- **Foundry Local** vystavuje OpenAI-kompatibilní endpoint **Chat Completions** a je určen pro lokální vývoj; pro plnou funkcionalitu Responses API použijte Azure OpenAI / Microsoft Foundry.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Prohlášení o omezení odpovědnosti**:
Tento dokument byl přeložen pomocí AI překladatelské služby [Co-op Translator](https://github.com/Azure/co-op-translator). Přestože usilujeme o co největší přesnost, mějte prosím na paměti, že automatizované překlady mohou obsahovat chyby nebo nepřesnosti. Originální dokument v jeho mateřském jazyce by měl být považován za autoritativní zdroj. Pro kritické informace se doporučuje profesionální lidský překlad. Nejsme odpovědní za jakékoli nedorozumění nebo nesprávné interpretace vzniklé použitím tohoto překladu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->