# Промене

Све значајне промене у курсу **AI агенти за почетнике** документоване су у овом фајлу.

## [Објављено] — 2026-07-13

Ово издање додаје две нове лекције које комплетирају циклус распореда — скалирање агената до Microsoft Foundry и смањење на једну радну станицу — плус smoke-test pipeline, освежену навигацију курса, нове вештине учења и ажуриран брендинг.

### Додато

- **Лекција 16 — Распоређивање скалабилних агената са Microsoft Foundry.** Нова лекција [16-deploying-scalable-agents/README.md](./16-deploying-scalable-agents/README.md) и извршиви нотебоок [16-python-agent-framework.ipynb](./16-deploying-scalable-agents/code_samples/16-python-agent-framework.ipynb) који гради продукцијског агента за корисничку подршку (алати, RAG, меморија, рутирање модела, кеширање одговора, људско одобрење, оцена, и OpenTelemetry трасирање), са развојним/распоређивачким/извршним Mermaid дијаграмима, провером знања, задатком и изазовом.
- **Лекција 17 — Креирање локалних AI агената са Foundry Local и Qwen.** Нова лекција [17-creating-local-ai-agents/README.md](./17-creating-local-ai-agents/README.md) и нотебоок [17-local-agent-foundry-local.ipynb](./17-creating-local-ai-agents/code_samples/17-local-agent-foundry-local.ipynb) који гради потпуно помоћника за инжењеринг на уређају (Qwen позив функција преко Foundry Local, sandbox-овани фајл алати, локални RAG са Chromom, опционални локални MCP), са дијаграмима само за локално / локални-RAG / позив алата, провером знања, задатком и изазовом.
- **Smoke-test pipeline.** Нова [AI Smoke Test](https://github.com/marketplace/actions/ai-smoke-test) радни ток [.github/workflows/smoke-test.yml](../../.github/workflows/smoke-test.yml) плус каталози по лекцијама у [tests/](./tests/README.md) за агенте који се могу распоредити у Лекцијама 01, 04, 05 и 16, са индексним README који мапира сваки каталог на његову лекцију и име агента. Лекција 16 добија одељак "Валидација деплојованог агента са smoke тестовима"; Лекције 01/04/05 добијају опциони показивач за smoke-тест.
- **Вештине закупаца.** Нове вештине агената у `.agents/skills/`: [deploying-scalable-agents](./.agents/skills/deploying-scalable-agents/SKILL.md), [local-ai-agents](./.agents/skills/local-ai-agents/SKILL.md) (пакетирање смерница из Лекција 16 и 17), и [testing-course-samples](./.agents/skills/testing-course-samples/SKILL.md) (како верификовати нотебоок примерке према живој Microsoft Foundry / Azure OpenAI поставци).
- **Извршивач валидације нотебоока.** Нови [scripts/validate-notebooks.ps1](../../scripts/validate-notebooks.ps1) који извршава сваки Python нотебоок без главе корисничког интерфејса са `nbconvert` и исписује PASS/FAIL матрицу (плус `results.json`). Аутоматски детектује корен репоа и Python, искључује нотебооке који нису из курса (`.venv`, `site-packages`, `translations`, assets шаблона вештина) и `.NET` нотебооке по заданом, и подржава `-Filter`, `-Timeout`, `-List`, `-IncludeDotnet`, и `-Python`.
- **Навигација курса.** Додате везе Претходна/Следећа лекција за Лекције 11–15 (раније недостајуће) тако да цео курс повезује 00 → 18 у оба смера.
- **Нови иконички прикази.** Иконице лекција за Лекције 16 и 17, плус освежена друштвена слика репозиторијума [images/repo-thumbnailv3.png](./images/repo-thumbnailv3.png) (сада рекламира две нове лекције и URL `aka.ms/ai-agents-beginners`).
- **Зависности** ([requirements.txt](../../requirements.txt)): додати `foundry-local-sdk` и `chromadb` за Лекцију 17.

### Промењено

- **Главни [README.md](./README.md)** табела лекција: Лекције 16 и 17 сада повезују свој садржај (раније "Ускоро"); слика репозиторијума ажурирана на `repo-thumbnailv3.png`.
- **[STUDY_GUIDE.md](./STUDY_GUIDE.md)**: додате Лекције 16 и 17 у водич кроз лекције и образовне путеве, и одељак „Валидација деплојованих агената са smoke тестовима“.
- **[AGENTS.md](./AGENTS.md)**: ажурирана бројност/опис лекција (00–18), додат одељак за валидацију smoke-тестом, и додати примери именовања за Лекцију 16/17.
- **[18-securing-ai-agents/README.md](./18-securing-ai-agents/README.md)**: "Претходна лекција" сада указује на Лекцију 17 (раније Лекција 15), затварајући ланац.
- **Стандаризовани референци модела на не-депрецирираним моделима.** Замена свих `gpt-4o` / `gpt-4o-mini` референци у курсу (документација, `.env.example`, Python/.NET нотебоокови и примери) са `gpt-4.1-mini` — `gpt-4o` (све верзије) се укидају 2026. Лекција 16 својим примером рутирања модела задржава контраст малог/великог користећи `gpt-4.1-mini` (мали) и `gpt-4.1` (велики). Python нотебоокови сада бирају модел из променљивих окружења (`AZURE_AI_MODEL_DEPLOYMENT_NAME` / `AZURE_OPENAI_DEPLOYMENT`) уместо да имена модела буду у коду.

### Напомене и позната ограничења

- **Није извршавано на живом Azure-у.** Нотебоокови нових лекција су образовни примерци; покрените и верификујте их на сопственој Microsoft Foundry / Foundry Local поставци. smoke-test радни ток захтева да поставите агента из лекције и конфигуришете Azure OIDC тајне (`AZURE_CLIENT_ID`, `AZURE_TENANT_ID`, `AZURE_SUBSCRIPTION_ID`) са улогом **Azure AI User** у Foundry скоупу пројекта.
- **Лекција 17 је само локална.** Нема Foundry Responses крајњу тачку, па smoke-test радња се не односи; валидација се врши покретањем нотебоока на вашој радној станици.

## [Објављено] — 2026-07-06

Ово издање мигрира курс на **Azure OpenAI Responses API**, стандардизује назив производа на **Microsoft Foundry** и **Microsoft Agent Framework (MAF)**, укида GitHub Models, ажурира верзије SDK-а и додаје нови садржај о локалним моделима и хостингу других оквира у Foundry.

### Додато

- **Вештина миграције** — Инсталирана [`azure-openai-to-responses`](./.agents/skills/azure-openai-to-responses/SKILL.md) вештина агента (путања [Azure-Samples/azure-openai-to-responses](https://github.com/Azure-Samples/azure-openai-to-responses)) у `.agents/skills/`, укључујући њене референце и скрипту за скенирање.
- **Foundry Local (покретање модела на уређају)** — Нови одељак "Алтернативни провајдер: Foundry Local" у [00-course-setup/README.md](./00-course-setup/README.md) који обухвата инсталацију (`winget` / `brew`), `foundry model run`, `foundry-local-sdk`, и повезивање `FoundryLocalManager` са Microsoft Agent Framework преко `OpenAIChatClient`.
- **Хостинг LangChain / LangGraph агената на Microsoft Foundry** — Нови одељак у [14-microsoft-agent-framework/README.md](./14-microsoft-agent-framework/README.md) плус извршив пример [14-langchain-hosted-agent.py](../../14-microsoft-agent-framework/code-samples/14-langchain-hosted-agent.py) који користи `langchain-azure-ai[hosting]` и `ResponsesHostServer` (протокол `/responses`), на основу [Microsoft Learn](https://learn.microsoft.com/azure/foundry/how-to/develop/langchain-hosted-agents).
- **Microsoft Project Opal** — Нови одељак "Пример из стварног света: Microsoft Project Opal" у [15-browser-use/README.md](./15-browser-use/README.md) који представља Opal као агента за коришћење рачунара у предузећу и повезује га са концептима курса (човек у петљи, поверење/безбедност, планирање, вештине).
- **Други пример из Лекције 02 Python** — Додат [02-python-agent-framework-azure-openai.ipynb](./02-explore-agentic-frameworks/code_samples/02-python-agent-framework-azure-openai.ipynb) (погледати "Промењено" — мигрирано са бившег Semantic Kernel нотебоока) и увезан у README лекције.
- Додат одељак „Модели и провајдери“ у [STUDY_GUIDE.md](./STUDY_GUIDE.md).

### Промењено

- **Chat Completions → Responses API (Python).** Примери који су директно позивали модел мигрирани са Chat Completions на Responses API (`client.responses.create(input=..., store=False)`, `resp.output_text`), користећи `OpenAI` клијент према стабилној Azure OpenAI `/openai/v1/` крајњој тачки (без `api_version`). Погођени примери укључују:
  - [06-building-trustworthy-agents/code_samples/06-system-message-framework.ipynb](./06-building-trustworthy-agents/code_samples/06-system-message-framework.ipynb)
  - [06-building-trustworthy-agents/code_samples/06-human-in-the-loop.ipynb](./06-building-trustworthy-agents/code_samples/06-human-in-the-loop.ipynb)
  - [04-tool-use/README.md](./04-tool-use/README.md) — комплетан проход кроз позивање функција (шема алата претворена у Responses формат, резултати алата враћени као `function_call_output`, `max_output_tokens`, итд.).
- **GitHub Models → Azure OpenAI.** GitHub Models је депрецирирано (уклања се **јул 2026**) и не подржава Responses API. Сви GitHub Models код пути су конвертовани у Azure OpenAI / Microsoft Foundry у Python и .NET примерима:
  - Python: Лекција 08 workflow нотебоокови (`01`–`03`), Лекција 14 (`14-handoff`, `14-human-loop`, `hotel_booking_workflow_sample.py`).
  - .NET: `01`–`04`, `07`, `08` `*-dotnet-agent-framework.cs` + пратилац `.md` докс, и Лекција 08 dotNET workflow нотебоокови/`.md` (`01`–`03`) сада користе `AzureOpenAIClient(...).GetOpenAIResponseClient(deployment).CreateAIAgent(...)` са `AzureCliCredential`.
- **Semantic Kernel → Microsoft Agent Framework.** Бивши `02-semantic-kernel.ipynb` преписан да користи Microsoft Agent Framework са Azure OpenAI (Responses API) и преименован у `02-python-agent-framework-azure-openai.ipynb`.
- **Стандаризовано на `FoundryChatClient` + `as_agent`.** README и нотебоок код који је користио `AzureAIProjectAgentProvider` стандаризован према канонском образцу коришћеном у Лекцији 01 и оквирним примерима: `FoundryChatClient(project_endpoint=..., model=..., credential=AzureCliCredential())` са `provider.as_agent(...)`. Ажурирано кроз README и нотебооке Лекција 02–14 (нпр. меморија из Лекције 13, сви нотебоокови Лекције 14, `11-agentic-protocols/code_samples/github-mcp/app.py`).
- **Назив производа.** Преименовано кроз цео садржај на енглеском:
  - "Azure AI Foundry" / "Azure AI Studio" → **Microsoft Foundry**
  - "Azure AI Agent Service" → **Microsoft Foundry Agent Service**
  - (Неизмењено: "Azure OpenAI", "Azure AI Search", "Azure AI Inference", и имена променљивих окружења.)
- **Зависности** ([requirements.txt](../../requirements.txt)):
  - Закључано на `agent-framework>=1.10.0`, `agent-framework-foundry>=1.10.0`, `agent-framework-openai>=1.10.0`.
  - Закључано на `openai>=1.108.1` (минимум за Responses API).
  - Уклонјен `azure-ai-inference` (коришћен само у мигрираним GitHub Models примерима).
- **Конфигурација окружења** ([.env.example](../../.env.example)): уклоњене GitHub Models променљиве (`GITHUB_TOKEN`, `GITHUB_ENDPOINT`, `GITHUB_MODEL_ID`); додате `AZURE_OPENAI_ENDPOINT`, `AZURE_OPENAI_DEPLOYMENT`, и опционално `AZURE_OPENAI_API_KEY`; ажурирано именовање на Microsoft Foundry.
- **Документација** — Ажурирани [00-course-setup/README.md](./00-course-setup/README.md), [AGENTS.md](./AGENTS.md), [README.md](./README.md), и [STUDY_GUIDE.md](./STUDY_GUIDE.md) за горе наведено (подешавање env променљивих, верификациони пример, смернице провајдера, именовање).

### Уклонио

- GitHub Models кораке за укључивање и променљиве окружења из документације за подешавање (замењено са Azure OpenAI / Microsoft Foundry).

### Сигурност / Приватност (чишћење јавне поделе)

- Обрисани излази извршавања Jupyter нотебоока који су цурили стварни **Azure subscription ID**, имена ресурсних група / ресурса, и Bing connection ID, плус развојачи **локалних путања и корисничких имена**, у:
  - `08-multi-agent/code_samples/workflows-agent-framework/dotNET/04.dotnet-agent-framework-workflow-aifoundry-condition.ipynb`

  - `08-multi-agent/code_samples/workflows-agent-framework/python/04.python-agent-framework-workflow-aifoundry-condition.ipynb`
  - `15-browser-use/15-browser-user.ipynb`
- Потврђено да у пратећем енглеском садржају нема API кључева, токена, ID-а претплата или личних путања (reference на `GITHUB_TOKEN` које остају су GitHub Actions token у workflow-има и GitHub MCP сервер PAT у подешавању Лекције 11 — оба легитимна и нису повезана са GitHub Models).

### Напомене и позната ограничења

- **Није извршавано/компилирано.** Ово су едукативни примери ажурирани за исправност API/naming; нису покретани против живих Azure ресурса, а .NET примери нису компилирани у овом окружењу. Верификујте против своје Microsoft Foundry / Azure OpenAI имплементације.
- **Деплојмент модела мора подржавати Responses API.** Користите деплојмент као што је `gpt-4.1-mini`, `gpt-4.1` или `gpt-5.x` модел. Старији модели подржавају основну функционалност Responses, али не сваки фичер.
- **Верзија agent-framework-а.** Примери циљају најновији MAF (`>=1.10.0`). Канонски позив за креирање агента је `client.as_agent(...)`; API је верификован према званичној документацији framework-а и инсталираној верзији. Ако користите другу верзију, проверите доступност метода (`as_agent` уместо `create_agent`).
- **Лекција 08 workflow notebook 04** намерно чува `AzureAIAgentClient` (из `agent-framework-azure-ai`) јер користи Microsoft Foundry Agent Service host-оване алате (Bing grounding, code interpreter); већ је базиран на Responses.
- **.NET подразумевани деплојмент.** Два dotNET примера Лекције 08 раније су били hard-coded на специфичан модел; сада подразумевано користе `AZURE_OPENAI_DEPLOYMENT` (`gpt-4.1-mini`). Ако пример зависи од мултимодалног/визуелног улаза, поставите `AZURE_OPENAI_DEPLOYMENT` на одговарајући модел.
- **Foundry Local** нуди OpenAI компатибилан **Chat Completions** endpoint и намењен је за локални развој; за пун скуп функција Responses API користите Azure OpenAI / Microsoft Foundry.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Изјава о одрицању одговорности**:
Овај документ је преведен коришћењем услуге за аутоматски превод [Co-op Translator](https://github.com/Azure/co-op-translator). Иако тежимо тачности, имајте у виду да аутоматски преводи могу садржати грешке или нетачности. Оригинални документ на његовом изворном језику треба сматрати ауторитативним извором. За критичне информације препоручује се професионални људски превод. Нисмо одговорни за било каква неспоразума или погрешна тумачења која произилазе из коришћења овог превода.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->