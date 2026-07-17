# Дневник на промените

Всички забележителни промени в курса **AI Agents for Beginners** са документирани в този файл.

## [Пуснат] — 2026-07-13

Тази версия добавя два нови урока, които завършват цикъла на внедряване — мащабиране на агентите до Microsoft Foundry и намаляване до един работен компютър — плюс pipeline за бързо тестване, обновена навигация в курса, нови умения за учащите и обновен брандинг.

### Добавени

- **Урок 16 — Внедряване на мащабируеми агенти с Microsoft Foundry.** Нов урок [16-deploying-scalable-agents/README.md](./16-deploying-scalable-agents/README.md) и изпълним бележник [16-python-agent-framework.ipynb](./16-deploying-scalable-agents/code_samples/16-python-agent-framework.ipynb), създаващ продукционен агент за клиентска поддръжка (инструменти, RAG, памет, маршрут на модел, кеширане на отговори, одобрение от човек, контролна точка за оценка и OpenTelemetry проследяване), с диаграми за разработка/внедряване/работно време в Mermaid, проверка на знанията, задание и предизвикателство.
- **Урок 17 — Създаване на локални AI агенти с Foundry Local и Qwen.** Нов урок [17-creating-local-ai-agents/README.md](./17-creating-local-ai-agents/README.md) и бележник [17-local-agent-foundry-local.ipynb](./17-creating-local-ai-agents/code_samples/17-local-agent-foundry-local.ipynb), създаващ напълно локален инженеринг асистент (Qwen function calling през Foundry Local, пясъчни файлови инструменти, локален RAG с Chroma, по избор локален MCP), с диаграми за локално само / локален-RAG / извикване на инструменти, проверка на знанията, задание и предизвикателство.
- **Pipeline за бързо тестване.** Нов workflow [AI Smoke Test](https://github.com/marketplace/actions/ai-smoke-test) [.github/workflows/smoke-test.yml](../../.github/workflows/smoke-test.yml) плюс каталози на ниво урок под [tests/](./tests/README.md) за внедрими агенти от Урок 01, 04, 05 и 16, с индекс README, който картографира всеки каталог към съответния урок и име на хостван агент. Урок 16 получава секция "Валидиране на внедрен агент с бързи тестове"; Уроците 01/04/05 получават опционален показалец за бърз тест.
- **Умения на учащите се.** Нови Умения за Агенти под `.agents/skills/`: [deploying-scalable-agents](./.agents/skills/deploying-scalable-agents/SKILL.md), [local-ai-agents](./.agents/skills/local-ai-agents/SKILL.md) (опаковащи ръководствата на Урок 16 и 17) и [testing-course-samples](./.agents/skills/testing-course-samples/SKILL.md) (как да валидираме примерите в бележниците спрямо работещ Microsoft Foundry / Azure OpenAI).
- **Изпълнител за валидация на бележници.** Нов [scripts/validate-notebooks.ps1](../../scripts/validate-notebooks.ps1), който изпълнява всеки Python бележник без графичен интерфейс чрез `nbconvert` и отпечатва PASS/FAIL матрица (плюс `results.json`). Автоматично открива корена на репото и Python, изключва по подразбиране не-курсови бележници (`.venv`, `site-packages`, `translations`, шаблони за умения) и `.NET` бележници, и поддържа опции `-Filter`, `-Timeout`, `-List`, `-IncludeDotnet` и `-Python`.
- **Навигация в курса.** Добавени връзки към Предишен/Следващ урок за Уроци 11–15 (преди липсваха), така че целият курс се свързва 00 → 18 в двете посоки.
- **Нови миниатюри.** Миниатюри за Уроци 16 и 17, плюс обновено социално изображение на хранилището [images/repo-thumbnailv3.png](./images/repo-thumbnailv3.png) (сега рекламиращо двата нови урока и URL `aka.ms/ai-agents-beginners`).
- **Зависимости** ([requirements.txt](../../requirements.txt)): добавени `foundry-local-sdk` и `chromadb` за Урок 17.

### Променени

- **Основна таблица в [README.md](./README.md)**: Уроците 16 и 17 вече се свързват със съдържанието си (предишно стоеше "Coming Soon"); изображението на репото е сменено на `repo-thumbnailv3.png`.
- **[STUDY_GUIDE.md](./STUDY_GUIDE.md)**: добавени Уроци 16 и 17 към урок по урок ръководство и учебни пътеки, плюс секция "Валидиране на внедрени агенти с бързи тестове".
- **[AGENTS.md](./AGENTS.md)**: обновен брой и описание на уроците (00–18), добавена секция за валидиране с бързи тестове и примери за именуване на образци от Уроци 16/17.
- **[18-securing-ai-agents/README.md](./18-securing-ai-agents/README.md)**: "Предишен урок" сега сочи към Урок 17 (преди беше Урок 15), като затваря веригата.
- **Стандартизирани препратки към модели без оттегляне.** Заменени всички препратки `gpt-4o` / `gpt-4o-mini` в целия курс (доки, `.env.example`, Python/.NET бележници и примери) с `gpt-4.1-mini` — `gpt-4o` (всички версии) се оттегля през 2026. Примерът с маршрутизация на модели в Урок 16 запазва контраст малък/голям с `gpt-4.1-mini` (малък) и `gpt-4.1` (голям). Python бележниците сега избират модела от променливите за обкръжението (`AZURE_AI_MODEL_DEPLOYMENT_NAME` / `AZURE_OPENAI_DEPLOYMENT`) вместо фиксирано име на модел.

### Бележки и известни ограничения

- **Не се изпълнява срещу жив Azure.** Новите бележници към уроците са образователни примери; изпълнявайте и валидирайте спрямо собствената си инсталация Microsoft Foundry / Foundry Local. Workflow за бързо тестване изисква да внедрите агента от урока и да конфигурирате Azure OIDC тайни (`AZURE_CLIENT_ID`, `AZURE_TENANT_ID`, `AZURE_SUBSCRIPTION_ID`) с ролята **Azure AI User** в обхвата на Foundry проекта.
- **Урок 17 е само локален.** Не разполага с крайна точка Foundry Responses, затова действието за бърз тест не важи; валидирайте го чрез стартиране на бележника на вашата работна станция.

## [Пуснат] — 2026-07-06

Тази версия мигрира курса към **Azure OpenAI Responses API**, стандартизира имената на продуктите като **Microsoft Foundry** и **Microsoft Agent Framework (MAF)**, изважда от експлоатация GitHub Models, актуализира версии на SDK и добавя ново съдържание за локални модели и хостване на други рамки в Foundry.

### Добавени

- **Умение за миграция** — Инсталирано Агентско Умение [`azure-openai-to-responses`](./.agents/skills/azure-openai-to-responses/SKILL.md) (от [Azure-Samples/azure-openai-to-responses](https://github.com/Azure-Samples/azure-openai-to-responses)) под `.agents/skills/`, включително референции и скрипт за сканиране.
- **Foundry Local (стартиране на модели на устройството)** — Нова секция "Алтернативен доставчик: Foundry Local" в [00-course-setup/README.md](./00-course-setup/README.md), обхващаща инсталация (`winget` / `brew`), `foundry model run`, `foundry-local-sdk` и свързване на `FoundryLocalManager` с Microsoft Agent Framework чрез `OpenAIChatClient`.
- **Хостване на LangChain / LangGraph агенти в Microsoft Foundry** — Нова секция в [14-microsoft-agent-framework/README.md](./14-microsoft-agent-framework/README.md) плюс изпълним пример [14-langchain-hosted-agent.py](../../14-microsoft-agent-framework/code-samples/14-langchain-hosted-agent.py), използващ `langchain-azure-ai[hosting]` и `ResponsesHostServer` (протокол `/responses`), базиран на [Microsoft Learn](https://learn.microsoft.com/azure/foundry/how-to/develop/langchain-hosted-agents).
- **Microsoft Project Opal** — Нова секция "Пример от реалния свят: Microsoft Project Opal" в [15-browser-use/README.md](./15-browser-use/README.md), представяща Opal като агент за използване на компютър на предприятие и картографираща го към концепциите на курса (човек в цикъла, доверие/сигурност, планиране, умения).
- **Втори Python пример за Урок 02** — Добавен [02-python-agent-framework-azure-openai.ipynb](./02-explore-agentic-frameworks/code_samples/02-python-agent-framework-azure-openai.ipynb) (виж "Променени" — мигриран от предишния понятиен бележник Semantic Kernel) и свързан в README на урока.
- Добавена секция Модели и Доставчици в [STUDY_GUIDE.md](./STUDY_GUIDE.md).

### Променени

- **Chat Completions → Responses API (Python).** Примерите, които извикваха модела директно, бяха мигрирани от Chat Completions към Responses API (`client.responses.create(input=..., store=False)`, `resp.output_text`), използвайки клиента `OpenAI` срещу стабилния Azure OpenAI `/openai/v1/` краен пункт (без `api_version`). Засегнати примери включват:
  - [06-building-trustworthy-agents/code_samples/06-system-message-framework.ipynb](./06-building-trustworthy-agents/code_samples/06-system-message-framework.ipynb)
  - [06-building-trustworthy-agents/code_samples/06-human-in-the-loop.ipynb](./06-building-trustworthy-agents/code_samples/06-human-in-the-loop.ipynb)
  - [04-tool-use/README.md](./04-tool-use/README.md) — пълното ръководство за извикване на функции (инструментната схема е опростена до Responses формат, резултатите от инструмента се връщат като `function_call_output`, `max_output_tokens` и др.).
- **GitHub Models → Azure OpenAI.** GitHub Models е остарял (ще бъде изтеглен **юли 2026**) и не поддържа Responses API. Всички кодови пътища за GitHub Models бяха превключени към Azure OpenAI / Microsoft Foundry както за Python, така и за .NET примери:
  - Python: бележниците в workflow на Урок 08 (`01`–`03`), Урок 14 (`14-handoff`, `14-human-loop`, `hotel_booking_workflow_sample.py`).
  - .NET: `01`–`04`, `07`, `08` `*-dotnet-agent-framework.cs` + спомагателни `.md` документи, както и dotNET workflow бележниците/`.md` на Урок 08 (`01`–`03`) вече използват `AzureOpenAIClient(...).GetOpenAIResponseClient(deployment).CreateAIAgent(...)` с `AzureCliCredential`.
- **Semantic Kernel → Microsoft Agent Framework.** Предишният `02-semantic-kernel.ipynb` бе пренаписан да използва Microsoft Agent Framework с Azure OpenAI (Responses API) и беше преименуван в `02-python-agent-framework-azure-openai.ipynb`.
- **Стандартизация на `FoundryChatClient` + `as_agent`.** README и код в бележниците, които препращаха към `AzureAIProjectAgentProvider`, бяха стандартизирани към каноничния шаблон, използван в Урок 01 и собствените примери на рамката: `FoundryChatClient(project_endpoint=..., model=..., credential=AzureCliCredential())` с `provider.as_agent(...)`. Обновено във README-тата и бележниците на Урок 02–14 (например паметта в Урок 13, всички бележници на Урок 14, `11-agentic-protocols/code_samples/github-mcp/app.py`).
- **Именуване на продукти.** Преименувано из целия английски текст:
  - "Azure AI Foundry" / "Azure AI Studio" → **Microsoft Foundry**
  - "Azure AI Agent Service" → **Microsoft Foundry Agent Service**
  - (Без промени: "Azure OpenAI", "Azure AI Search", "Azure AI Inference" и имена на променливи на средата.)
- **Зависимости** ([requirements.txt](../../requirements.txt)):
  - Закотвени `agent-framework>=1.10.0`, `agent-framework-foundry>=1.10.0`, `agent-framework-openai>=1.10.0`.
  - Закотвен `openai>=1.108.1` (минимален за Responses API).
  - Премахнат `azure-ai-inference` (ползваше се само от мигрираните примери за GitHub Models).
- **Конфигурация на средата** ([.env.example](../../.env.example)): премахнати променливите за GitHub Models (`GITHUB_TOKEN`, `GITHUB_ENDPOINT`, `GITHUB_MODEL_ID`); добавени `AZURE_OPENAI_ENDPOINT`, `AZURE_OPENAI_DEPLOYMENT` и опционален `AZURE_OPENAI_API_KEY`; актуализирано именуване към Microsoft Foundry.
- **Документи** — Обновени [00-course-setup/README.md](./00-course-setup/README.md), [AGENTS.md](./AGENTS.md), [README.md](./README.md) и [STUDY_GUIDE.md](./STUDY_GUIDE.md) за горепосоченото (настройки на променливи, верификационни фрагменти, ръководство за доставчици, именуване).

### Премахнати

- Стъпките за интеграция и променливите на средата за GitHub Models от документацията за настройка (заменени от Azure OpenAI / Microsoft Foundry).

### Сигурност / Поверителност (почистване на публични споделяния)

- Почистени изходи от изпълнение на Jupyter бележници, които излагаха реален **Azure subscription ID**, имена на ресурсни групи/ресурси и Bing connection ID, както и **локални пътища и потребителски имена на разработчици**, в:
  - `08-multi-agent/code_samples/workflows-agent-framework/dotNET/04.dotnet-agent-framework-workflow-aifoundry-condition.ipynb`

  - `08-multi-agent/code_samples/workflows-agent-framework/python/04.python-agent-framework-workflow-aifoundry-condition.ipynb`
  - `15-browser-use/15-browser-user.ipynb`
- Потвърдено е, че в проследеното съдържание на английски няма останали API ключове, токени, ID-та на абонаменти или лични пътища (препратките към `GITHUB_TOKEN`, които остават, са токени на GitHub Actions в работните потоци и GitHub MCP сървърния PAT в настройката на Урок 11 — и двете легитимни и несвързани с GitHub Models).

### Бележки и известни ограничения

- **Не са изпълнени/компилирани.** Това са образователни примери, актуализирани за коректност на API/имената; не са пускани срещу живи Azure ресурси и .NET примерите не са компилирани в тази среда. Валидирайте според собственото си Microsoft Foundry / Azure OpenAI разгръщане.
- **Разгръщането на модела трябва да поддържа Responses API.** Използвайте разгръщане като `gpt-4.1-mini`, `gpt-4.1` или модел `gpt-5.x`. По-старите модели поддържат основната функционалност на Responses, но не всички функции.
- **Версия на agent-framework.** Примерите са насочени към последната MAF (`>=1.10.0`). Каноничният повик за създаване на агент е `client.as_agent(...)`; API-тата са валидирани спрямо публикуваната документация на framework-а и инсталирана версия. Ако използвате различна версия, потвърдете наличността на метода (`as_agent` срещу `create_agent`).
- **Урок 08 workflow notebook 04** умишлено запазва `AzureAIAgentClient` (от `agent-framework-azure-ai`), тъй като използва хоствани инструменти на Microsoft Foundry Agent Service (Bing grounding, code interpreter); вече е базиран на Responses.
- **.NET по подразбиране разгръщане.** Два dotNET workflow примера от Урок 08 по-рано имаха твърдо зададен модел; сега по подразбиране използват `AZURE_OPENAI_DEPLOYMENT` (`gpt-4.1-mini`). Ако пример разчита на мултимодален/визуален вход, настройте `AZURE_OPENAI_DEPLOYMENT` към подходящ модел.
- **Foundry Local** предлага съвместима с OpenAI крайна точка за **Chat Completions** и е предназначен за локална разработка; за пълния набор от функции на Responses API използвайте Azure OpenAI / Microsoft Foundry.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Отказ от отговорност**:
Този документ е преведен с помощта на AI преводачески услуга [Co-op Translator](https://github.com/Azure/co-op-translator). Въпреки че се стремим към точност, моля имайте предвид, че автоматизираните преводи могат да съдържат грешки или неточности. Оригиналният документ на неговия роден език трябва да се счита за авторитетен източник. За критична информация се препоръчва професионален човешки превод. Ние не носим отговорност за каквито и да е недоразумения или неправилни тълкувания, произтичащи от използването на този превод.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->