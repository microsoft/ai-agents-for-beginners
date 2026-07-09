# Дневник на промените

Всички забележителни промени в курса **AI агенти за начинаещи** са документирани в този файл.

## [Нерелизиран] — 2026-07-06

Това издание мигрира курса към **Azure OpenAI Responses API**, стандартизира именуването на продуктите в **Microsoft Foundry** и **Microsoft Agent Framework (MAF)**, прекратява използването на GitHub Models, актуализира версии на SDK и добавя ново съдържание за локални модели и хостване на други рамки в Foundry.

### Добавено

- **Умение за миграция** — Инсталиран е агентски умение [`azure-openai-to-responses`](./.agents/skills/azure-openai-to-responses/SKILL.md) (от [Azure-Samples/azure-openai-to-responses](https://github.com/Azure-Samples/azure-openai-to-responses)) под `.agents/skills/`, включително препратките и скрипта за сканиране.
- **Foundry Local (изпълнение на модели локално)** — Нов раздел "Алтернативен доставчик: Foundry Local" в [00-course-setup/README.md](./00-course-setup/README.md), обхващащ инсталация (`winget` / `brew`), `foundry model run`, `foundry-local-sdk` и връзката на `FoundryLocalManager` с Microsoft Agent Framework чрез `OpenAIChatClient`.
- **Хостване на LangChain / LangGraph агенти в Microsoft Foundry** — Нов раздел в [14-microsoft-agent-framework/README.md](./14-microsoft-agent-framework/README.md), плюс изпълним пример [14-langchain-hosted-agent.py](../../14-microsoft-agent-framework/code-samples/14-langchain-hosted-agent.py) с използване на `langchain-azure-ai[hosting]` и `ResponsesHostServer` (протоколът `/responses`), базиран на [Microsoft Learn](https://learn.microsoft.com/azure/foundry/how-to/develop/langchain-hosted-agents).
- **Microsoft Project Opal** — Нов раздел "Пример от реалния свят: Microsoft Project Opal" в [15-browser-use/README.md](./15-browser-use/README.md), който представя Opal като агент за корпоративно използване на компютър и го свързва с концепциите от курса (човек в цикъла, доверие/сигурност, планиране, умения).
- **Втори урок 02 Python пример** — Добавен е [02-python-agent-framework-azure-openai.ipynb](./02-explore-agentic-frameworks/code_samples/02-python-agent-framework-azure-openai.ipynb) (виж "Променено" — мигриран от предишния Semantic Kernel бележник) и е добавена препратка в README на урока.
- Добавен раздел **Модели и доставчици** в [STUDY_GUIDE.md](./STUDY_GUIDE.md).

### Променено

- **Chat Completions → Responses API (Python).** Примерите, които извикваха модела директно, бяха мигрирани от Chat Completions към Responses API (`client.responses.create(input=..., store=False)`, `resp.output_text`), използвайки `OpenAI` клиент към стабилния Azure OpenAI `/openai/v1/` крайна точка (без `api_version`). Влияние имат следните примери:
  - [06-building-trustworthy-agents/code_samples/06-system-message-framework.ipynb](./06-building-trustworthy-agents/code_samples/06-system-message-framework.ipynb)
  - [06-building-trustworthy-agents/code_samples/06-human-in-the-loop.ipynb](./06-building-trustworthy-agents/code_samples/06-human-in-the-loop.ipynb)
  - [04-tool-use/README.md](./04-tool-use/README.md) — пълното ръководство за извикване на функция (инструментната схема е преформатирана към Responses формат, резултатите от инструмента се връщат като `function_call_output`, `max_output_tokens` и други).
- **GitHub Models → Azure OpenAI.** GitHub Models е остарял (оттегля се през **юли 2026**) и не поддържа Responses API. Всички кодови пътища с GitHub Models бяха прехвърлени към Azure OpenAI / Microsoft Foundry в Python и .NET примерите:
  - Python: бележници от урок 08 (`01`–`03`), урок 14 (`14-handoff`, `14-human-loop`, `hotel_booking_workflow_sample.py`).
  - .NET: `01`–`04`, `07`, `08` `*-dotnet-agent-framework.cs` + съпътстващи `.md` документи, и бележници с работни потоци/`.md` от урок 08 (`01`–`03`) вече използват `AzureOpenAIClient(...).GetOpenAIResponseClient(deployment).CreateAIAgent(...)` с `AzureCliCredential`.
- **Semantic Kernel → Microsoft Agent Framework.** Предишният `02-semantic-kernel.ipynb` беше пренаписан да използва Microsoft Agent Framework с Azure OpenAI (Responses API) и беше преименуван на `02-python-agent-framework-azure-openai.ipynb`.
- **Стандартизиране върху `FoundryChatClient` + `as_agent`.** README и кодът в бележниците, които препращаха към `AzureAIProjectAgentProvider`, са стандартизирани по каноничния модел, използван в урок 01 и официалните примери: `FoundryChatClient(project_endpoint=..., model=..., credential=AzureCliCredential())` с `provider.as_agent(...)`. Обновено е в README-та и бележниците от урок 02 до 14 (напр. памет на урок 13, всички бележници на урок 14, `11-agentic-protocols/code_samples/github-mcp/app.py`).
- **Именуване на продукти.** Преименувано в целия англоезичен материал:
  - "Azure AI Foundry" / "Azure AI Studio" → **Microsoft Foundry**
  - "Azure AI Agent Service" → **Microsoft Foundry Agent Service**
  - (Без промяна: "Azure OpenAI", "Azure AI Search", "Azure AI Inference" и имената на променливите на средата.)
- **Зависимости** ([requirements.txt](../../requirements.txt)):
  - Заключени версии `agent-framework>=1.10.0`, `agent-framework-foundry>=1.10.0`, `agent-framework-openai>=1.10.0`.
  - Заключена версия `openai>=1.108.1` (минимум за Responses API).
  - Премахнат `azure-ai-inference` (ползван само от мигрираните примери с GitHub Models).
- **Конфигурация на средата** ([.env.example](../../.env.example)): премахнати променливите за GitHub Models (`GITHUB_TOKEN`, `GITHUB_ENDPOINT`, `GITHUB_MODEL_ID`); добавени `AZURE_OPENAI_ENDPOINT`, `AZURE_OPENAI_DEPLOYMENT` и опционален `AZURE_OPENAI_API_KEY`; именуването актуализирано към Microsoft Foundry.
- **Документация** — Обновени [00-course-setup/README.md](./00-course-setup/README.md), [AGENTS.md](./AGENTS.md), [README.md](./README.md) и [STUDY_GUIDE.md](./STUDY_GUIDE.md) за горепосочените промени (настройка на променливи на средата, проверка, насоки за доставчици, именуване).

### Премахнато

- Стъпките за въвеждане в GitHub Models и променливите на средата бяха премахнати от документацията за настройка (преобхванати от Azure OpenAI / Microsoft Foundry).

### Сигурност / Поверителност (почистване за публично споделяне)

- Изчистени резултатите от изпълнение на Jupyter бележници, които разкриваха реален **Azure subscription ID**, имена на resource group / ресурси, Bing connection ID, както и **локални пътища на файлове и имена на потребители** на разработчиците, в:
  - `08-multi-agent/code_samples/workflows-agent-framework/dotNET/04.dotnet-agent-framework-workflow-aifoundry-condition.ipynb`
  - `08-multi-agent/code_samples/workflows-agent-framework/python/04.python-agent-framework-workflow-aifoundry-condition.ipynb`
  - `15-browser-use/15-browser-user.ipynb`
- Потвърдено е, че няма останали API ключове, токени, subscription IDs или лични пътища в проследяваното английско съдържание (референтните места за `GITHUB_TOKEN` остават в GitHub Actions токена във workflow-ите и GitHub MCP сървърния PAT в настройката на урок 11 — и двата легитимни и несвързани с GitHub Models).

### Бележки и известни ограничения

- **Не са изпълнявани/компилирани.** Това са учебни примери, обновени за коректност на API и именуване; не са изпълнявани срещу реални Azure ресурси и .NET примерите не са компилирани в тази среда. Проверявайте спрямо собствената си Microsoft Foundry / Azure OpenAI инсталация.
- **Деплойментът на модела трябва да поддържа Responses API.** Използвайте деплоймент като `gpt-4o-mini`, `gpt-4.1` или модел от `gpt-5.x` серия. По-старите модели поддържат основна функционалност на Responses, но не всички функции.
- **Версия на agent-framework.** Примерите са насочени към най-новия MAF (`>=1.10.0`). Каноничното извикване за създаване на агент е `client.as_agent(...)`; API-тата са валидирани спрямо публикуваната документация и инсталиран билд на фреймуърка. Ако използвате различна версия, проверете наличността на метода (`as_agent` срещу `create_agent`).
- **Бележник за работен поток от урок 08, номер 04** умишлено запазва използването на `AzureAIAgentClient` (от `agent-framework-azure-ai`), тъй като използва хоствани инструменти от Microsoft Foundry Agent Service (Bing grounding, code interpreter); вече е базиран на Responses.
- **По подразбиране деплоймент в .NET.** Два dotNET примера за работен поток от урок 08 първоначално използваха хардкоднат `gpt-4o`; сега по подразбиране използват `AZURE_OPENAI_DEPLOYMENT` (`gpt-4o-mini`). Ако примерът изисква мултимодален/визуален вход, задайте `AZURE_OPENAI_DEPLOYMENT` с подходящ модел.
- **Foundry Local** предоставя OpenAI-съвместима крайна точка за **Chat Completions** и е предназначен за локална разработка; използвайте Azure OpenAI / Microsoft Foundry за пълния набор от функции на Responses API.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Отказ от отговорност**:
Този документ е преведен с помощта на AI преводачески услуга [Co-op Translator](https://github.com/Azure/co-op-translator). Въпреки че се стремим към точност, моля имайте предвид, че автоматизираните преводи могат да съдържат грешки или неточности. Оригиналният документ на неговия роден език трябва да се счита за авторитетен източник. За критична информация се препоръчва професионален човешки превод. Ние не носим отговорност за каквито и да е недоразумения или неправилни тълкувания, произтичащи от използването на този превод.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->