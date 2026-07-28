# История на промените

Всички забележителни промени в курса **AI Agents for Beginners** са документирани в този файл.

## [Издаден] — 2026-07-14

Това издание премества курса от два вече остарели модела, мигрира останалите тетрадки с уроци към стабилния Microsoft Agent Framework API и валидира Python тетрадките спрямо работеща инсталация на Microsoft Foundry.

### Променено

- **Преминаване от остарели модели (`gpt-4.1` / `gpt-4.1-mini` → `gpt-5-mini`).** И двата `gpt-4.1` и `gpt-4.1-mini` са вече остарели (официална дата на пенсиониране **14 октомври 2026**). Заменени са всички препратки в курса (документи, `.env.example`, Python/.NET тетрадки и примери) с неостарелия `gpt-5-mini`. В урок 16 примерът за разпределяне на модели запазва контраста малък/голям като използва `gpt-5-nano` (малък) и `gpt-5-mini` (голям). Инсталираните файлове на трети страни ([15-browser-use/llms.txt](../../15-browser-use/llms.txt)), историческият текст от GitHub Models и бележките за възможностите на умението `azure-openai-to-responses` съзнателно не са променяни.
- **Тетрадката за предаване на управление в урок 14 е мигрирана към стабилния API.** [14-handoff.ipynb](./14-microsoft-agent-framework/code-samples/14-handoff.ipynb) вече използва `agent_framework.orchestrations.HandoffBuilder` с `.with_start_agent(...)`, `HandoffAgentUserRequest.create_response(...)`, стрийминг базиран на `event.type` и `FoundryChatClient` (замествайки премахнатите символи преди версия 1.0 `HandoffBuilder`/`ChatMessage`/`RequestInfoEvent`).
- **Тетрадката за човешка намеса в урок 14 е мигрирана към стабилния API.** [14-human-loop.ipynb](./14-microsoft-agent-framework/code-samples/14-human-loop.ipynb) сега спира чрез `ctx.request_info(...)` + `@response_handler` (замествайки премахнатите `RequestInfoExecutor` / `RequestInfoMessage` / `RequestResponse`), изгражда се с `WorkflowBuilder(start_executor=..., output_executors=[...])`, управлява структурирания изход чрез `default_options={"response_format": ...}` и използва скриптиран отговор, така че тетрадката може да се изпълнява без намеса (без блокиращ `input()`).
- **Конфигурация на средата** ([.env.example](../../.env.example)): сменени са имената на разгръщанията на моделите на `gpt-5-mini`; добавени са `AZURE_AI_SMALL_MODEL` / `AZURE_AI_LARGE_MODEL` (маршрутизиране в урок 16) и липсващият до момента `AZURE_OPENAI_CHAT_DEPLOYMENT_NAME` (ползване на браузър в урок 15).
- **Зависимости** ([requirements.txt](../../requirements.txt)): фиксирани са `agent-framework`, `agent-framework-foundry` и `agent-framework-openai` на версия `~=1.10.0` за самоконсистентен, валидиран набор (версия 1.11.0 въвежда експериментални променящи интерфейси промени, използвани в тези уроци).

### Забележки и известни ограничения

- **Валидирани спрямо жив Microsoft Foundry.** Python тетрадките бяха изпълнени без графичен интерфейс с `nbconvert` спрямо проект на Microsoft Foundry, използващ `gpt-5-mini` (и `gpt-5-nano` за маршрутизиране в урок 16). Разгръщайте еквивалентни неостарели модели в собствения си проект; тетрадките четат името на разгръщането от `AZURE_AI_MODEL_DEPLOYMENT_NAME` / `AZURE_OPENAI_DEPLOYMENT`.
- **Все още изисква допълнителни ресурси за някои уроци.** Урок 05 изисква Azure AI Search; работният поток с внедряване на Bing в урок 08 (`04.python-agent-framework-workflow-aifoundry-condition.ipynb`) изисква връзка с Bing и хоствани инструменти от Microsoft Foundry Agent Service; урок 13 (Cognee) и урок 17 (Foundry Local) изискват собствени среди за изпълнение.

## [Издаден] — 2026-07-13

Това издание добавя два нови урока, които завършват арката на разгъване — мащабиране на агентите до Microsoft Foundry и свиване до едно работно място — плюс димна пробна последователност, обновена навигация в курса, нови умения за учениците и обновено брандиране.

### Добавено

- **Урок 16 — Разгръщане на мащабируеми агенти с Microsoft Foundry.** Нов урок [16-deploying-scalable-agents/README.md](./16-deploying-scalable-agents/README.md) и изпълнима тетрадка [16-python-agent-framework.ipynb](./16-deploying-scalable-agents/code_samples/16-python-agent-framework.ipynb), изграждащи продукционен агент за поддръжка на клиенти (инструменти, RAG, памет, маршрутизиране на модел, кеширане на отговори, одобрение от човек, контролна точка за оценка и OpenTelemetry трасировка), с диаграми Mermaid за разработка/разгръщане/изпълнение, проверка на знания, задание и предизвикателство.
- **Урок 17 — Създаване на локални AI агенти с Foundry Local и Qwen.** Нов урок [17-creating-local-ai-agents/README.md](./17-creating-local-ai-agents/README.md) и тетрадка [17-local-agent-foundry-local.ipynb](./17-creating-local-ai-agents/code_samples/17-local-agent-foundry-local.ipynb), изграждащи напълно локален инженеринг асистент (викане на функции Qwen чрез Foundry Local, изолирани файлови инструменти, локален RAG с Chroma, опционален локален MCP), с диаграми за локални, локален-RAG и викане на инструменти, проверка на знания, задание и предизвикателство.
- **Димна пробна последователност.** Нова работна последователност [AI Smoke Test](https://github.com/marketplace/actions/ai-smoke-test) [.github/workflows/smoke-test.yml](../../.github/workflows/smoke-test.yml) плюс каталози за всеки урок в [tests/](./tests/README.md) за разгъваемите агенти в уроци 01, 04, 05 и 16, с индексен README, който свързва всеки каталог с урока и името на хостван агент. Урок 16 добавя раздел "Валидиране на разгънат агент с димни тестове"; уроци 01/04/05 добавят по избор указател към димни тестове.
- **Умения за учениците.** Нови умения за агенти под `.agents/skills/`: [deploying-scalable-agents](./.agents/skills/deploying-scalable-agents/SKILL.md), [local-ai-agents](./.agents/skills/local-ai-agents/SKILL.md) (обобщаващи указанията от уроци 16 и 17) и [testing-course-samples](./.agents/skills/testing-course-samples/SKILL.md) (как да се валидират примерните тетрадки спрямо жив Microsoft Foundry / Azure OpenAI).
- **Изпълнител за валидация на тетрадките.** Нов [scripts/validate-notebooks.ps1](../../scripts/validate-notebooks.ps1), който изпълнява всяка Python тетрадка без графичен интерфейс с `nbconvert` и отпечатва матрица PASS/FAIL (плюс `results.json`). Автоматично открива корена на репото и Python, по подразбиране изключва некурсови тетрадки (`.venv`, `site-packages`, `translations`, активи на уменията) и `.NET` тетрадки, и поддържа `-Filter`, `-Timeout`, `-List`, `-IncludeDotnet` и `-Python`.
- **Навигация в курса.** Добавени бяха връзки за Предишен/Следващ урок към уроци 11–15 (които преди липсваха), така че целият курс е свързан по веригата 00 → 18 в двете посоки.
- **Нови миниатюри.** Миниатюри за уроци 16 и 17, плюс обновена социална репо снимка [images/repo-thumbnailv3.png](./images/repo-thumbnailv3.png) (сега рекламира двата нови урока и URL `aka.ms/ai-agents-beginners`).
- **Зависимости** ([requirements.txt](../../requirements.txt)): добавени `foundry-local-sdk` и `chromadb` за урок 17.

### Променено

- **Главната таблица на уроците в [README.md](./README.md):** Уроци 16 и 17 вече са с препратки към съдържанието си (преди "Скоро предстои"); изображението на репото е обновено на `repo-thumbnailv3.png`.
- **[STUDY_GUIDE.md](./STUDY_GUIDE.md):** Добавени уроци 16 и 17 в ръководството по уроци и учебните пътеки, както и раздел "Валидиране на разгърнати агенти с димни тестове".
- **[AGENTS.md](./AGENTS.md):** Обновен брой и описание на уроците (00–18), добавен раздел за валидиране чрез димни тестове и примери за именуване на проби от уроци 16/17.
- **[18-securing-ai-agents/README.md](./18-securing-ai-agents/README.md):** "Предишен урок" вече сочи към урок 17 (беше урок 15), затваряйки веригата.
- **Стандартизирани препратки към модели на неостарели модели.** Заменени са всички препратки `gpt-4o` / `gpt-4o-mini` в курса (документи, `.env.example`, Python/.NET тетрадки и проби) с `gpt-4.1-mini` — `gpt-4o` (всички версии) ще се пенсионира през 2026 г. Примерът за маршрутизиране на моделите в урок 16 запазва контраст малък/голям с `gpt-4.1-mini` (малък) и `gpt-4.1` (голям). Python тетрадките вече избират модел от променливи на средата (`AZURE_AI_MODEL_DEPLOYMENT_NAME` / `AZURE_OPENAI_DEPLOYMENT`) вместо да имат твърдо зададен модел.

### Забележки и известни ограничения

- **Не е изпълнявано срещу жив Azure.** Новите тетрадки са учебни проби; изпълнявайте и валидирайте ги спрямо собствената си инсталация на Microsoft Foundry / Foundry Local. Работният поток за димни тестове изисква да разположите агента на урока и да конфигурирате Azure OIDC тайни (`AZURE_CLIENT_ID`, `AZURE_TENANT_ID`, `AZURE_SUBSCRIPTION_ID`) с роля **Azure AI User** в рамките на проекта Foundry.
- **Урок 17 е само локален.** Няма крайна точка Foundry Responses, затова действието за димни тестове не важи; валидирайте го като стартирате тетрадката на вашата работна станция.

## [Издаден] — 2026-07-06

Това издание мигрира курса към **Azure OpenAI Responses API**, стандартизира наименованията на продуктите Microsoft Foundry и Microsoft Agent Framework (MAF), пенсионира GitHub Models, обновява версии на SDK и добавя ново съдържание за локални модели и хостване на други рамки в Foundry.

### Добавено

- **Умение за миграция** — Инсталирано е умението за агент [`azure-openai-to-responses`](./.agents/skills/azure-openai-to-responses/SKILL.md) (от [Azure-Samples/azure-openai-to-responses](https://github.com/Azure-Samples/azure-openai-to-responses)) под `.agents/skills/`, включително неговите препратки и скрипт за сканиране.
- **Foundry Local (изпълнение на модели на устройството)** — Нов раздел "Алтернативен доставчик: Foundry Local" в [00-course-setup/README.md](./00-course-setup/README.md), описващ инсталиране (`winget` / `brew`), `foundry model run`, `foundry-local-sdk` и свързване на `FoundryLocalManager` с Microsoft Agent Framework чрез `OpenAIChatClient`.
- **Хостване на LangChain / LangGraph агенти в Microsoft Foundry** — Нов раздел в [14-microsoft-agent-framework/README.md](./14-microsoft-agent-framework/README.md) плюс изпълним пример [14-langchain-hosted-agent.py](../../14-microsoft-agent-framework/code-samples/14-langchain-hosted-agent.py), използващ `langchain-azure-ai[hosting]` и `ResponsesHostServer` (протоколът `/responses`), базиран на [Microsoft Learn](https://learn.microsoft.com/azure/foundry/how-to/develop/langchain-hosted-agents).
- **Microsoft Project Opal** — Нов раздел "Пример от реалния свят: Microsoft Project Opal" в [15-browser-use/README.md](./15-browser-use/README.md), представящ Opal като агент за използване на компютър в предприятие и обвързващ го с концепциите в курса (човек в цикъла, доверие/сигурност, планиране, умения).
- **Втория Python пример в урок 02** — Добавен [02-python-agent-framework-azure-openai.ipynb](./02-explore-agentic-frameworks/code_samples/02-python-agent-framework-azure-openai.ipynb) (виж в раздел "Променено" — мигриран от предишната тетрадка Semantic Kernel) и добавен в README на урока.
- Добавен раздел "Модели и доставчици" към [STUDY_GUIDE.md](./STUDY_GUIDE.md).

### Променено

- **Chat Completions → Responses API (Python).** Примерите, които извикваха модела директно, бяха мигрирани от Chat Completions към Responses API (`client.responses.create(input=..., store=False)`, `resp.output_text`), използвайки клиента `OpenAI` към стабилната Azure OpenAI крайна точка `/openai/v1/` (без `api_version`). Засегнатите примери включват:
  - [06-building-trustworthy-agents/code_samples/06-system-message-framework.ipynb](./06-building-trustworthy-agents/code_samples/06-system-message-framework.ipynb)
  - [06-building-trustworthy-agents/code_samples/06-human-in-the-loop.ipynb](./06-building-trustworthy-agents/code_samples/06-human-in-the-loop.ipynb)
  - [04-tool-use/README.md](./04-tool-use/README.md) — пълното презентиране на извикване на функции (инструментната схема преустроена в Responses формат, резултатите от инструмента върнати като `function_call_output`, `max_output_tokens` и др.).

- **GitHub Models → Azure OpenAI.** GitHub Models е остарял (ще бъде прекратен **юли 2026**) и не поддържа Responses API. Всички кодови пътеки на GitHub Models бяха конвертирани към Azure OpenAI / Microsoft Foundry в примерите за Python и .NET:
  - Python: Работни бележници от урок 08 (`01`–`03`), урок 14 (`14-handoff`, `14-human-loop`, `hotel_booking_workflow_sample.py`).
  - .NET: `01`–`04`, `07`, `08` `*-dotnet-agent-framework.cs` + спътникови `.md` документи, както и работните бележници/`.md` от урок 08 dotNET (`01`–`03`) вече използват `AzureOpenAIClient(...).GetOpenAIResponseClient(deployment).CreateAIAgent(...)` с `AzureCliCredential`.
- **Semantic Kernel → Microsoft Agent Framework.** Старият `02-semantic-kernel.ipynb` беше пренаписан за използване на Microsoft Agent Framework с Azure OpenAI (Responses API) и преименуван на `02-python-agent-framework-azure-openai.ipynb`.
- **Стандартизирано използване на `FoundryChatClient` + `as_agent`.** README и кодът в бележниците, които препращаха към `AzureAIProjectAgentProvider`, бяха стандартизирани по каноничния модел, използван от урок 01 и собствените примери на рамката: `FoundryChatClient(project_endpoint=..., model=..., credential=AzureCliCredential())` с `provider.as_agent(...)`. Обновено във всички README и бележници от урок 02 до 14 (например памет на урок 13, всички бележници на урок 14, `11-agentic-protocols/code_samples/github-mcp/app.py`).
- **Именуване на продукти.** Преименувано във всички английски материали:
  - "Azure AI Foundry" / "Azure AI Studio" → **Microsoft Foundry**
  - "Azure AI Agent Service" → **Microsoft Foundry Agent Service**
  - (Без промяна: "Azure OpenAI", "Azure AI Search", "Azure AI Inference" и имената на променливите на околната среда.)
- **Зависимости** ([requirements.txt](../../requirements.txt)):
  - Зададени версии за `agent-framework>=1.10.0`, `agent-framework-foundry>=1.10.0`, `agent-framework-openai>=1.10.0`.
  - Зададена версия `openai>=1.108.1` (минимална за Responses API).
  - Премахнат `azure-ai-inference` (използваше се само в мигрираните примери за GitHub Models).
- **Конфигурация на средата** ([.env.example](../../.env.example)): премахнати променливите за GitHub Models (`GITHUB_TOKEN`, `GITHUB_ENDPOINT`, `GITHUB_MODEL_ID`); добавени `AZURE_OPENAI_ENDPOINT`, `AZURE_OPENAI_DEPLOYMENT` и опционално `AZURE_OPENAI_API_KEY`; обновени имена към Microsoft Foundry.
- **Документация** — Обновени [00-course-setup/README.md](./00-course-setup/README.md), [AGENTS.md](./AGENTS.md), [README.md](./README.md) и [STUDY_GUIDE.md](./STUDY_GUIDE.md) за гореописаното (настройка на променливи на средата, проверочен фрагмент, насоки за доставчик, именуване).

### Премахнати

- Стъпките за включване на GitHub Models и променливите на средата от документацията за настройка (заменени от Azure OpenAI / Microsoft Foundry).

### Сигурност / Поверителност (прочистване за публично споделяне)

- Почистени изходите на изпълнение на Jupyter бележници, които разкриваха реален **Azure subscription ID**, имена на resource-group / ресурси и Bing connection ID, както и **локални пътища и потребителски имена на разработчици**, в:
  - `08-multi-agent/code_samples/workflows-agent-framework/dotNET/04.dotnet-agent-framework-workflow-aifoundry-condition.ipynb`
  - `08-multi-agent/code_samples/workflows-agent-framework/python/04.python-agent-framework-workflow-aifoundry-condition.ipynb`
  - `15-browser-use/15-browser-user.ipynb`
- Проверено, че няма останали API ключове, токени, subscription ID или лични пътища в проследяваното английско съдържание (присъстващи референции към `GITHUB_TOKEN` са токена на GitHub Actions в workflows и PAT на GitHub MCP сървъра в настройката от урок 11 — и двете легитимни и несвързани с GitHub Models).

### Бележки и известни ограничения

- **Не са изпълнявани/компилирани.** Това са образователни примери, обновени за коректност на API/именуване; не са изпълнявани срещу живи Azure ресурси, а .NET примерите не бяха компилирани в тази среда. Вярвайте на собственото си разгръщане с Microsoft Foundry / Azure OpenAI.
- **Разгръщането на модела трябва да поддържа Responses API.** Използвайте разгръщение като `gpt-4.1-mini`, `gpt-4.1` или модел `gpt-5.x`. По-старите модели поддържат основна функционалност на Responses, но не всички функции.
- **Версия на agent-framework.** Примерите са за най-новия MAF (`>=1.10.0`). Каноничният подход за създаване на агент е `client.as_agent(...)`; API бяха валидирани според публикуваната документация на рамката и инсталирана версия. Ако ползвате друга версия, уверете се за наличността на методите (`as_agent` срещу `create_agent`).
- **Работен бележник от урок 08, номер 04** умишлено запазва `AzureAIAgentClient` (от `agent-framework-azure-ai`), защото използва инструменти на Microsoft Foundry Agent Service, хоствани (Bing grounding, code interpreter); вече е базиран на Responses.
- **.NET стандартно разгръщане.** Два примера за работни бележници от урок 08 dotNET преди това имаха хардкоднат специфичен модел; сега по подразбиране използват `AZURE_OPENAI_DEPLOYMENT` (`gpt-4.1-mini`). Ако примерът разчита на мултимодален/визуален вход, задайте `AZURE_OPENAI_DEPLOYMENT` на подходящ модел.
- **Foundry Local** предлага OpenAI-съвместима точка за край **Chat Completions** и е предназначен за локална разработка; за пълния набор от функции на Responses API използвайте Azure OpenAI / Microsoft Foundry.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Отказ от отговорност**:
Този документ е преведен с помощта на AI преводачески услуга [Co-op Translator](https://github.com/Azure/co-op-translator). Въпреки че се стремим към точност, моля имайте предвид, че автоматизираните преводи могат да съдържат грешки или неточности. Оригиналният документ на неговия роден език трябва да се счита за авторитетен източник. За критична информация се препоръчва професионален човешки превод. Ние не носим отговорност за каквито и да е недоразумения или неправилни тълкувания, произтичащи от използването на този превод.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->