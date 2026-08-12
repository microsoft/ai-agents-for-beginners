# Дневник промена

Све значајне промене на курсу **AI агенти за почетнике** су документоване у овом фајлу.

## [Објављено] — 2026-07-14

Ово издање помера курс са два недавно застарела модела, мигрира преостале свеске Леcона на стабилан Microsoft Agent Framework API и валидаје Python свеске против живог Microsoft Foundry окружења.

### Измењено

- **Померање са застарелих модела (`gpt-4.1` / `gpt-4.1-mini` → `gpt-5-mini`).** И `gpt-4.1` и `gpt-4.1-mini` су сада застарели (датум пензионисања **14. октобар 2026**). Замењене све референце у курсу (документација, `.env.example`, Python/.NET свеске и примерци) са незастарелим `gpt-5-mini`. Пример рутирања модела из Лекције 16 задржава контраст мали/велик користећи `gpt-5-nano` (мали) и `gpt-5-mini` (велики). Трећепартијски фајлови ([15-browser-use/llms.txt](../../15-browser-use/llms.txt)), историјски GitHub Models текст и примедбе способности вештине `azure-openai-to-responses` намерно су остали непромењени.
- **Свеска за предају из Лекције 14 мигрирана на стабилан API.** [14-handoff.ipynb](./14-microsoft-agent-framework/code-samples/14-handoff.ipynb) сада користи `agent_framework.orchestrations.HandoffBuilder` са `.with_start_agent(...)`, `HandoffAgentUserRequest.create_response(...)`, струјање базирано на `event.type`, и `FoundryChatClient` (умињена пре-1.0 симбола `HandoffBuilder`/`ChatMessage`/`RequestInfoEvent`).
- **Свеска за људски низак смер из Лекције 14 мигрирана на стабилан API.** [14-human-loop.ipynb](./14-microsoft-agent-framework/code-samples/14-human-loop.ipynb) сада паузира преко `ctx.request_info(...)` + `@response_handler` (умињене симболе `RequestInfoExecutor` / `RequestInfoMessage` / `RequestResponse`), гради се са `WorkflowBuilder(start_executor=..., output_executors=[...])`, управља структуираним излазом кроз `default_options={"response_format": ...}`, и користи скриптован одговор да свеска ради аутоматски (без блокирања `input()`).
- **Конфигурација окружења** ([.env.example](../../.env.example)): пребачени називи распореда модела на `gpt-5-mini`; додати `AZURE_AI_SMALL_MODEL` / `AZURE_AI_LARGE_MODEL` (рутирање из Лекције 16) и раније недостајући `AZURE_OPENAI_CHAT_DEPLOYMENT_NAME` (рутирање из Лекције 15).
- **Зависности** ([requirements.txt](../../requirements.txt)): фиксиране верзије `agent-framework`, `agent-framework-foundry` и `agent-framework-openai` на `~=1.10.0` за самоконзистентан и валидиран скуп (1.11.0 доноси експерименталне промене које искачу у овој лекцији).

### Напомене и позната ограничења

- **Валидирано против живог Microsoft Foundry.** Python свеске су извршаване без главе користећи `nbconvert` против Microsoft Foundry пројекта користећи `gpt-5-mini` (и `gpt-5-nano` за Лекцију 16 рутирање). Разместите еквивалентне незастареле моделе у свом пројекту; свеске читају назив распореда из `AZURE_AI_MODEL_DEPLOYMENT_NAME` / `AZURE_OPENAI_DEPLOYMENT`.
- **Неке лекције захтевају додатне ресурсе.** Лекција 05 захтева Azure AI Search; радни ток Лекције 08 Bing-grounding-а (`04.python-agent-framework-workflow-aifoundry-condition.ipynb`) захтева Bing конекцију и Microsoft Foundry Agent Service домаћинске алате; Лекције 13 (Cognee) и 17 (Foundry Local) захтевају своје окружење за извршавање.

## [Објављено] — 2026-07-13

Ово издање додаје две нове лекције које завршавају лук извршења — скалирање агената до Microsoft Foundry и смањење на једну радну станицу — плус димни тестни систем, освежену навигацију курса, нове вештине ученика и ажуриран бренд.

### Додато

- **Лекција 16 — Распоређивање скалабилних агената са Microsoft Foundry.** Нова лекција [16-deploying-scalable-agents/README.md](./16-deploying-scalable-agents/README.md) и покретна свеска [16-python-agent-framework.ipynb](./16-deploying-scalable-agents/code_samples/16-python-agent-framework.ipynb) која гради производног агента за корисничку подршку (али, РАГ, меморија, рутирање модела, кеширање одговора, људско одобрење, врата процене и OpenTelemetry праћење), са развојним/распоредним/извршним Mermaid дијаграмима, провером знања, задатком и изазовом.
- **Лекција 17 — Креирање локалних AI агената са Foundry Local и Qwen.** Нова лекција [17-creating-local-ai-agents/README.md](./17-creating-local-ai-agents/README.md) и свеска [17-local-agent-foundry-local.ipynb](./17-creating-local-ai-agents/code_samples/17-local-agent-foundry-local.ipynb) која гради потпуно уређајског помоћника у инжењерингу (Qwen функцијско позивање преко Foundry Local, изоловани алати за фајлове, локални РАГ са Chroma, опциони локални MCP), са дијаграмима локални-само / локални-РАГ / позив алата, провером знања, задатком и изазовом.
- **Димни тестни систем.** Нова [AI Smoke Test](https://github.com/marketplace/actions/ai-smoke-test) радна процедура [.github/workflows/smoke-test.yml](../../.github/workflows/smoke-test.yml) плус каталози по лекцијама под [tests/](./tests/README.md) за распоредиве агенте у Лекцијама 01, 04, 05 и 16, са индексираном README мапом која каталоге повезује са лекцијом и именом домаћег агента. Лекција 16 добија одељак „Валидирање распорђеног агента димним тестовима“; Лекције 01/04/05 добијају опционални показивач за димни тест.
- **Вештине ученика.** Нове вештине агената у `.agents/skills/`: [deploying-scalable-agents](./.agents/skills/deploying-scalable-agents/SKILL.md), [local-ai-agents](./.agents/skills/local-ai-agents/SKILL.md) (паковање смерница Лекције 16 и 17), и [testing-course-samples](./.agents/skills/testing-course-samples/SKILL.md) (како верификовати примерке свески против живог Microsoft Foundry / Azure OpenAI окружења).
- **Извршни валидатор свески.** Нови [scripts/validate-notebooks.ps1](../../scripts/validate-notebooks.ps1) који извршава све Python свеске без главе користећи `nbconvert` и исписује PASS/FAIL матрицу (плус `results.json`). Аутоматски открива корен репозиторијума и Python, изузима не-курсне свеске (`.venv`, `site-packages`, `translations`, шаблоне умештених вештина) и `.NET` свеске по дифолту, и подржава `-Filter`, `-Timeout`, `-List`, `-IncludeDotnet`, и `-Python`.
- **Навигација курса.** Додати линкови Претходна/Следећа лекција за Лекције 11–15 (раније су недостајали) тако да цео курс повезује 00 → 18 у оба правца.
- **Нови сличице.** Сличице за Лекције 16 и 17, плус освежена друштвена слика репозиторијума [images/repo-thumbnailv3.png](./images/repo-thumbnailv3.png) (сада рекламирају две нове лекције и УРЛ `aka.ms/ai-agents-beginners`).
- **Зависности** ([requirements.txt](../../requirements.txt)): додати `foundry-local-sdk` и `chromadb` за Лекцију 17.

### Измењено

- **Главна табела лекција у [README.md](./README.md):** Лекције 16 и 17 сада воде ка свом садржају (раније "Ускоро"); репозиторијум слика подижeна на `repo-thumbnailv3.png`.
- **[STUDY_GUIDE.md](./STUDY_GUIDE.md):** додате Лекције 16 и 17 у водич и учењачке стазе лекција, и одељак "Валидирање распорђених агената димним тестовима".
- **[AGENTS.md](./AGENTS.md):** ажуриран број/опис лекција (00–18), додат одељак за валидацију димним тестовима, и додаци примери именовања за Лекције 16/17.
- **[18-securing-ai-agents/README.md](./18-securing-ai-agents/README.md):** „Претходна лекција“ сада показује на Лекцију 17 (раније Лекција 15), затварајући ланац.
- **Стандардизоване референце модела на незастарелим моделима.** Замењене све референце `gpt-4o` / `gpt-4o-mini` у целокупном курсу (документација, `.env.example`, Python/.NET свеске и примерци) са `gpt-4.1-mini` — `gpt-4o` (све верзије) пензионише се 2026. Пример рутирања модела Лекције 16 задржава контраст мали/велики користећи `gpt-4.1-mini` (мали) и `gpt-4.1` (велики). Python свеске сада бирају модел из променљивих окружења (`AZURE_AI_MODEL_DEPLOYMENT_NAME` / `AZURE_OPENAI_DEPLOYMENT`) уместо хардкодованог имена модела.

### Напомене и позната ограничења

- **Није извршено против живог Azure-а.** Нове лекције су образовни примерци; покрените и валидирајте их против свог Microsoft Foundry / Foundry Local окружења. Димна тест радна процедура захтева да распоредите агента лекције и конфигуришете Azure OIDC тајне (`AZURE_CLIENT_ID`, `AZURE_TENANT_ID`, `AZURE_SUBSCRIPTION_ID`) са улогом **Azure AI User** у Foundry пројекатском домену.
- **Лекција 17 је само локална.** Нема Foundry Responses крајњу тачку, тако да се димни тест не примењује; валидирајте је покретањем свеске на својој радној станици.

## [Објављено] — 2026-07-06

Ово издање мигрира курс на **Azure OpenAI Responses API**, стандардизује назив производа на **Microsoft Foundry** и **Microsoft Agent Framework (MAF)**, пензионише GitHub Models, ажурира верзије SDK и додаје нови садржај о локалним моделима и домаћинству других оквира на Foundry.

### Додато

- **Вештина миграције** — Инсталирана [`azure-openai-to-responses`](./.agents/skills/azure-openai-to-responses/SKILL.md) Вештина агента (из [Azure-Samples/azure-openai-to-responses](https://github.com/Azure-Samples/azure-openai-to-responses)) у `.agents/skills/`, укључујући њене референце и скрипту за скенирање.
- **Foundry Local (извршавање модела на уређају)** — Нови одељак "Алтернативни провајдер: Foundry Local" у [00-course-setup/README.md](./00-course-setup/README.md) који покрива инсталацију (`winget` / `brew`), `foundry model run`, `foundry-local-sdk` и повезивање `FoundryLocalManager` са Microsoft Agent Framework преко `OpenAIChatClient`.
- **Домаћинство LangChain / LangGraph агената на Microsoft Foundry** — Нови одељак у [14-microsoft-agent-framework/README.md](./14-microsoft-agent-framework/README.md) плус покретни пример [14-langchain-hosted-agent.py](../../14-microsoft-agent-framework/code-samples/14-langchain-hosted-agent.py) који користи `langchain-azure-ai[hosting]` и `ResponsesHostServer` (протокол `/responses`), заснован на [Microsoft Learn](https://learn.microsoft.com/azure/foundry/how-to/develop/langchain-hosted-agents).
- **Microsoft Project Opal** — Нови одељак "Пример из стварног света: Microsoft Project Opal" у [15-browser-use/README.md](./15-browser-use/README.md) који поставља Opal као ентерпрајс агента за коришћење компјутера и мапира га на концепте курса (људски у петљи, поверење/безбедност, планирање, Вештине).
- **Други Python пример за Лекцију 02** — Додат [02-python-agent-framework-azure-openai.ipynb](./02-explore-agentic-frameworks/code_samples/02-python-agent-framework-azure-openai.ipynb) (погледај "Измењено" — мигрирано из бивше Semantic Kernel свеске) и повезан у README лекције.
- Додат одељак Models and Providers у [STUDY_GUIDE.md](./STUDY_GUIDE.md).

### Измењено

- **Chat Completions → Responses API (Python).** Примери који су директно позивали модел мигрирани су са Chat Completions на Responses API (`client.responses.create(input=..., store=False)`, `resp.output_text`), користећи `OpenAI` клијента преко стабилне Azure OpenAI `/openai/v1/` крајње тачке (без `api_version`). Погођени примерци укључују:
  - [06-building-trustworthy-agents/code_samples/06-system-message-framework.ipynb](./06-building-trustworthy-agents/code_samples/06-system-message-framework.ipynb)
  - [06-building-trustworthy-agents/code_samples/06-human-in-the-loop.ipynb](./06-building-trustworthy-agents/code_samples/06-human-in-the-loop.ipynb)
  - [04-tool-use/README.md](./04-tool-use/README.md) — комплетан преглед позива функција (шема алата равњена у Responses формат, резултати алата враћени као `function_call_output`, `max_output_tokens`, итд.).

- **GitHub модели → Azure OpenAI.** GitHub модели су застарели (повлаче се у **јулу 2026.**) и не подржавају Responses API. Сви GitHub Models кодни путеви су конвертовани у Azure OpenAI / Microsoft Foundry у Python и .NET примерима:
  - Python: лекција 08 workflow нотебоокови (`01`–`03`), лекција 14 (`14-handoff`, `14-human-loop`, `hotel_booking_workflow_sample.py`).
  - .NET: `01`–`04`, `07`, `08` `*-dotnet-agent-framework.cs` + пратећа `.md` документација, и лекција 08 dotNET workflow нотебоокови/`.md` (`01`–`03`) сада користе `AzureOpenAIClient(...).GetOpenAIResponseClient(deployment).CreateAIAgent(...)` са `AzureCliCredential`.
- **Semantic Kernel → Microsoft Agent Framework.** Претходни `02-semantic-kernel.ipynb` је преписан да користи Microsoft Agent Framework са Azure OpenAI (Responses API) и преименован у `02-python-agent-framework-azure-openai.ipynb`.
- **Стандардизовано на `FoundryChatClient` + `as_agent`.** README и нотебоок код који је референцирао `AzureAIProjectAgentProvider` је стандардизован на канонски образац који користи лекција 01 и оквирни примери: `FoundryChatClient(project_endpoint=..., model=..., credential=AzureCliCredential())` са `provider.as_agent(...)`. Ажурирано кроз лекције 02–14 README и нотебоокове (нпр. лекција 13 memory, сви нотебоокови лекције 14, `11-agentic-protocols/code_samples/github-mcp/app.py`).
- **Назив производа.** Преименовано кроз цео енглески садржај:
  - "Azure AI Foundry" / "Azure AI Studio" → **Microsoft Foundry**
  - "Azure AI Agent Service" → **Microsoft Foundry Agent Service**
  - (Непромењено: "Azure OpenAI", "Azure AI Search", "Azure AI Inference", и имена променљивих окружења.)
- **Зависности** ([requirements.txt](../../requirements.txt)):
  - Присилно постављено `agent-framework>=1.10.0`, `agent-framework-foundry>=1.10.0`, `agent-framework-openai>=1.10.0`.
  - Присилно постављено `openai>=1.108.1` (минимум за Responses API).
  - Уклоњен `azure-ai-inference` (коришћен само од стране мигрираних GitHub Models примера).
- **Конфигурација окружења** ([.env.example](../../.env.example)): уклоњене променљиве GitHub Models (`GITHUB_TOKEN`, `GITHUB_ENDPOINT`, `GITHUB_MODEL_ID`); додате `AZURE_OPENAI_ENDPOINT`, `AZURE_OPENAI_DEPLOYMENT` и опционални `AZURE_OPENAI_API_KEY`; именовање ажурирано у складу са Microsoft Foundry.
- **Документација** — Ажурирани [00-course-setup/README.md](./00-course-setup/README.md), [AGENTS.md](./AGENTS.md), [README.md](./README.md), и [STUDY_GUIDE.md](./STUDY_GUIDE.md) за горе наведено (постављање env var, верификациони исечак, упутства за провајдер, именовање).

### Уклоњено

- Почетни кораци и променљиве окружења GitHub Models из упутстава за подешавање (замењени Azure OpenAI / Microsoft Foundry).

### Безбедност / Приватност (чишћење јавног дељења)

- Очишћени излази извршења Јупитер нотебоокова који су открили стварни **Azure subscription ID**, називе ресурсних група / ресурса и Bing connection ID, као и девелоперске **локалне путеве и корисничка имена**, у:
  - `08-multi-agent/code_samples/workflows-agent-framework/dotNET/04.dotnet-agent-framework-workflow-aifoundry-condition.ipynb`
  - `08-multi-agent/code_samples/workflows-agent-framework/python/04.python-agent-framework-workflow-aifoundry-condition.ipynb`
  - `15-browser-use/15-browser-user.ipynb`
- Потврђено да нема кључева API, токена, subscription ID-ева или личних путева у праћеном енглеском садржају (референце `GITHUB_TOKEN` које остају су GitHub Actions token у workflow-има и GitHub MCP server PAT у подешавању лекције 11 — оба легитимна и немају везе са GitHub моделима).

### Напомене и позната ограничења

- **Нису извршавани/компилирани.** Ово су образовни примери ажурирани за исправност API-а и именовања; нису извршавани против живих Azure ресурса, а .NET примери нису компајлирани у овом окружењу. Верификујте на свом Microsoft Foundry / Azure OpenAI развоју.
- **Деплојмент модела мора подржавати Responses API.** Користите деплојмент као што су `gpt-4.1-mini`, `gpt-4.1`, или модел `gpt-5.x`. Старији модели подржавају основну функционалност Responses али не све могућности.
- **Верзија agent-framework-a.** Примери су циљали најновији MAF (`>=1.10.0`). Канонски позив за креирање агента је `client.as_agent(...)`; API-ји су верификовани на основу службене документације и инсталиране верзије оквира. Ако користите другачију верзију, потврдите доступност метода (`as_agent` против `create_agent`).
- **Workflow нотебоок лекције 08, 04** намерно задржава `AzureAIAgentClient` (из `agent-framework-azure-ai`) јер користи Microsoft Foundry Agent Service хостоване алате (Bing grounding, code interpreter); већ је на бази Responses API.
- **Подразумевани деплојмент за .NET.** Два доктора 08 dotNET workflow примера која су раније била тврдокодирана на конкретан модел сада подразумевано користе `AZURE_OPENAI_DEPLOYMENT` (`gpt-4.1-mini`). Ако пример зависи од мултимодалног/визуелног уноса, поставите `AZURE_OPENAI_DEPLOYMENT` на одговарајући модел.
- **Foundry Local** излаже OpenAI- компатибилан **Chat Completions** крајњу тачку и намењен је за локални развој; за потпун скуп функција Responses API користите Azure OpenAI / Microsoft Foundry.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Изјава о одрицању одговорности**:
Овај документ је преведен коришћењем услуге за аутоматски превод [Co-op Translator](https://github.com/Azure/co-op-translator). Иако тежимо тачности, имајте у виду да аутоматски преводи могу садржати грешке или нетачности. Оригинални документ на његовом изворном језику треба сматрати ауторитативним извором. За критичне информације препоручује се професионални људски превод. Нисмо одговорни за било каква неспоразума или погрешна тумачења која произилазе из коришћења овог превода.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->