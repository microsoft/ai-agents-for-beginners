# Журнал змін

Всі помітні зміни у курсі **AI Agents for Beginners** задокументовані у цьому файлі.

## [Випущено] — 2026-07-14

Це оновлення переводить курс із двох нещодавно застарілих моделей, мігрує решту блокнотів уроків на стабільний API Microsoft Agent Framework і перевіряє Python-блокноти на реальному розгортанні Microsoft Foundry.

### Зміни

- **Переведено з застарілих моделей (`gpt-4.1` / `gpt-4.1-mini` → `gpt-5-mini`).** Обидві моделі `gpt-4.1` та `gpt-4.1-mini` тепер застарілі (офіційна дата припинення підтримки **14 жовтня 2026**). Замінено всі згадки в курсі (документи, `.env.example`, Python/.NET блокноти та приклади) на незастарілу `gpt-5-mini`. Приклад маршрутизації моделей в уроці 16 зберігає контраст між малою та великою моделлю, використовуючи `gpt-5-nano` (мала) та `gpt-5-mini` (велика). Вендоровані файли третіх сторін ([15-browser-use/llms.txt](../../15-browser-use/llms.txt)), історичний текст GitHub Models та нотатки про можливості навику `azure-openai-to-responses` залишені без змін.
- **Блокнот передачі в Уроці 14 мігрував на стабільний API.** [14-handoff.ipynb](./14-microsoft-agent-framework/code-samples/14-handoff.ipynb) тепер використовує `agent_framework.orchestrations.HandoffBuilder` з `.with_start_agent(...)`, `HandoffAgentUserRequest.create_response(...)`, потокову обробку на основі `event.type` і `FoundryChatClient` (замінюючи вилучені символи версій pre-1.0 `HandoffBuilder`/`ChatMessage`/`RequestInfoEvent`).
- **Блокнот з участю людини в циклі Уроку 14 мігрував на стабільний API.** [14-human-loop.ipynb](./14-microsoft-agent-framework/code-samples/14-human-loop.ipynb) тепер призупиняється через `ctx.request_info(...)` + `@response_handler` (замість вилучених `RequestInfoExecutor` / `RequestInfoMessage` / `RequestResponse`), будується з `WorkflowBuilder(start_executor=..., output_executors=[...])`, керує структурованим виводом через `default_options={"response_format": ...}`, і використовує скриптовану відповідь, щоб блокнот працював без взаємодії користувача (без блокуючого `input()`).
- **Конфігурація оточення** ([.env.example](../../.env.example)): змінено назви розгортань моделей на `gpt-5-mini`; додано `AZURE_AI_SMALL_MODEL` / `AZURE_AI_LARGE_MODEL` (маршрутизація в уроці 16) та відсутній раніше `AZURE_OPENAI_CHAT_DEPLOYMENT_NAME` (використання браузером в уроці 15).
- **Залежності** ([requirements.txt](../../requirements.txt)): зафіксовано версії `agent-framework`, `agent-framework-foundry` та `agent-framework-openai` на `~=1.10.0` для узгодженого, перевіреного набору (версія 1.11.0 містить експериментальні сумісні злами інтерфейсів, які використовують ці уроки).

### Примітки та відомі обмеження

- **Перевірено на реальному Microsoft Foundry.** Python-блокноти були виконані без інтерфейсу з `nbconvert` проти проєкту Microsoft Foundry із моделлю `gpt-5-mini` (та `gpt-5-nano` для маршрутизації в уроці 16). Розгорніть еквівалентні незастарілі моделі у власному проєкті; блокноти читають ім'я розгортання з `AZURE_AI_MODEL_DEPLOYMENT_NAME` / `AZURE_OPENAI_DEPLOYMENT`.
- **Для деяких уроків потрібні додаткові ресурси.** Уроці 05 потрібен Azure AI Search; уроці 08 робочий процес Bing-ґрунтування (`04.python-agent-framework-workflow-aifoundry-condition.ipynb`) вимагає підключення Bing і інструментів служби Microsoft Foundry Agent Service; уроки 13 (Cognee) та 17 (Foundry Local) потребують власних рантаймів.

## [Випущено] — 2026-07-13

Це оновлення додає два нові уроки, які завершують дугу розгортання — масштабування агентів у Microsoft Foundry і запуск агента на одній робочій станції — а також пайплайн для тестування, оновлену навігацію курсу, нові навички учнів і оновлений брендинг.

### Додано

- **Урок 16 — Розгортання масштабованих агентів з Microsoft Foundry.** Новий урок [16-deploying-scalable-agents/README.md](./16-deploying-scalable-agents/README.md) і виконуємий блокнот [16-python-agent-framework.ipynb](./16-deploying-scalable-agents/code_samples/16-python-agent-framework.ipynb), що створює продакшн-агента техпідтримки (інструменти, RAG, пам'ять, маршрутизація моделей, кешування відповідей, затвердження людиною, контроль оцінки та трасування OpenTelemetry), із діаграмами розвитку/розгортання/рантайму Mermaid, перевіркою знань, домашнім завданням та викликом.
- **Урок 17 — Створення локальних AI агентів з Foundry Local і Qwen.** Новий урок [17-creating-local-ai-agents/README.md](./17-creating-local-ai-agents/README.md) і блокнот [17-local-agent-foundry-local.ipynb](./17-creating-local-ai-agents/code_samples/17-local-agent-foundry-local.ipynb) для створення повноцінного помічника з інженерії на пристрої (виклик функцій Qwen через Foundry Local, ізольовані файлові інструменти, локальний RAG з Chroma, опціональний локальний MCP), з діаграмами локальний/локальний-RAG/виклик інструментів, перевіркою знань, домашнім завданням та викликом.
- **Пайплайн для димового тестування.** Новий робочий процес [AI Smoke Test](https://github.com/marketplace/actions/ai-smoke-test) [.github/workflows/smoke-test.yml](../../.github/workflows/smoke-test.yml) плюс каталоги по уроках під [tests/](./tests/README.md) для розгорнутих агентів в Уроках 01, 04, 05 і 16, з індексним README, що відображає кожен каталог до відповідного уроку і імені хостового агента. Урок 16 отримує розділ "Перевірка розгорнутого агента димовими тестами"; уроки 01/04/05 — необов’язкові посилання на димовий тест.
- **Навички учнів.** Нові навички агента під `.agents/skills/`: [deploying-scalable-agents](./.agents/skills/deploying-scalable-agents/SKILL.md), [local-ai-agents](./.agents/skills/local-ai-agents/SKILL.md) (пакетування вказівок з Уроків 16 та 17) і [testing-course-samples](./.agents/skills/testing-course-samples/SKILL.md) (як перевірити приклади блокнотів проти реального Microsoft Foundry / Azure OpenAI оточення).
- **Запуск перевірки блокнотів.** Новий [scripts/validate-notebooks.ps1](../../scripts/validate-notebooks.ps1), який виконує кожен Python-блокнот без інтерфейсу з `nbconvert` і виводить матрицю PASS/FAIL (плюс `results.json`). Він автоматично визначає корінь репозиторію і Python, виключає за замовчуванням некурсові блокноти (`.venv`, `site-packages`, `translations`, акти в шаблонах навиків) і `.NET` блокноти, підтримує параметри `-Filter`, `-Timeout`, `-List`, `-IncludeDotnet` і `-Python`.
- **Навігація курсу.** Додано посилання на попередній/наступний уроки для уроків 11–15 (раніше відсутні), так що весь курс ланцюжком 00 → 18 працює в обох напрямках.
- **Нові ескізи.** Ескізи уроків 16 і 17, а також оновлене соціальне зображення репозиторію [images/repo-thumbnailv3.png](./images/repo-thumbnailv3.png) (тепер рекламує два нові уроки та URL `aka.ms/ai-agents-beginners`).
- **Залежності** ([requirements.txt](../../requirements.txt)): додано `foundry-local-sdk` і `chromadb` для Уроку 17.

### Зміни

- **Головна таблиця уроків у [README.md](./README.md):** уроки 16 і 17 тепер містять посилання на свій контент (раніше «Скоро»); зображення репозиторію оновлено на `repo-thumbnailv3.png`.
- **[STUDY_GUIDE.md](./STUDY_GUIDE.md):** додано Уроки 16 і 17 до посібника по уроках та навчальних шляхах, а також розділ "Перевірка розгорнутих агентів димовими тестами".
- **[AGENTS.md](./AGENTS.md):** оновлено кількість/опис уроків (00–18), додано розділ перевірки димовим тестуванням, додано приклади іменування для Уроків 16/17.
- **[18-securing-ai-agents/README.md](./18-securing-ai-agents/README.md):** "Попередній урок" тепер вказує на Урок 17 (було Урок 15), замикання ланцюжка.
- **Стандартизовані посилання на незастарілі моделі.** Замінено всі посилання `gpt-4o` / `gpt-4o-mini` у всьому курсі (документи, `.env.example`, Python/.NET блокноти і приклади) на `gpt-4.1-mini` — `gpt-4o` (всіх версій) буде застарілим у 2026 році. Приклад маршрутизації моделей в уроці 16 зберігає контраст між малою та великою моделлю, використовуючи `gpt-4.1-mini` (мала) та `gpt-4.1` (велика). Тепер Python-блокноти вибирають модель із змінних оточення (`AZURE_AI_MODEL_DEPLOYMENT_NAME` / `AZURE_OPENAI_DEPLOYMENT`) замість жорстко закодованої назви моделі.

### Примітки та відомі обмеження

- **Не виконувались на реальному Azure.** Нові блокноти уроків є навчальними прикладами; запускайте й перевіряйте їх у власному оточенні Microsoft Foundry / Foundry Local. Робочий процес димового тестування вимагає розгортання агента уроку і налаштування секретів Azure OIDC (`AZURE_CLIENT_ID`, `AZURE_TENANT_ID`, `AZURE_SUBSCRIPTION_ID`) з роллю **Azure AI User** в межах проєкту Foundry.
- **Урок 17 локальний лише.** Він не має кінцевої точки Foundry Responses, отже дія димового тестування не застосовується; перевірте його, запустивши блокнот на вашій робочій станції.

## [Випущено] — 2026-07-06

Це оновлення мігрує курс на **Azure OpenAI Responses API**, стандартизує назви продуктів **Microsoft Foundry** та **Microsoft Agent Framework (MAF)**, припиняє підтримку GitHub Models, оновлює версії SDK і додає новий контент про локальні моделі та хостинг інших фреймворків на Foundry.

### Додано

- **Навик міграції** — Встановлено Agent Skill [`azure-openai-to-responses`](./.agents/skills/azure-openai-to-responses/SKILL.md) (з [Azure-Samples/azure-openai-to-responses](https://github.com/Azure-Samples/azure-openai-to-responses)) у `.agents/skills/`, включно з посиланнями та скриптом сканування.
- **Foundry Local (запуск моделей на пристрої)** — Новий розділ "Alternative Provider: Foundry Local" у [00-course-setup/README.md](./00-course-setup/README.md), що описує встановлення (`winget` / `brew`), команду `foundry model run`, `foundry-local-sdk` та підключення `FoundryLocalManager` до Microsoft Agent Framework через `OpenAIChatClient`.
- **Хостинг агентів LangChain / LangGraph на Microsoft Foundry** — Новий розділ у [14-microsoft-agent-framework/README.md](./14-microsoft-agent-framework/README.md) плюс виконуємий приклад [14-langchain-hosted-agent.py](../../14-microsoft-agent-framework/code-samples/14-langchain-hosted-agent.py), який використовує `langchain-azure-ai[hosting]` і `ResponsesHostServer` (протокол `/responses`), базується на [Microsoft Learn](https://learn.microsoft.com/azure/foundry/how-to/develop/langchain-hosted-agents).
- **Microsoft Project Opal** — Новий розділ "Приклад із реального світу: Microsoft Project Opal" у [15-browser-use/README.md](./15-browser-use/README.md), що подає Opal як корпоративного агента користувача комп’ютера і відображає його на концепти курсу (людина в циклі, довіра/безпека, планування, Навички).
- **Другий приклад Python для Уроку 02** — Додано [02-python-agent-framework-azure-openai.ipynb](./02-explore-agentic-frameworks/code_samples/02-python-agent-framework-azure-openai.ipynb) (дивись "Зміни" — міграція із колишнього блокноту Semantic Kernel) і додано посилання у README уроку.
- Додано розділ "Models and Providers" у [STUDY_GUIDE.md](./STUDY_GUIDE.md).

### Зміни

- **Chat Completions → Responses API (Python).** Приклади, які викликали модель безпосередньо, мігрували з Chat Completions на Responses API (`client.responses.create(input=..., store=False)`, `resp.output_text`), використовуючи клієнта `OpenAI` проти стабільної Azure OpenAI `/openai/v1/` кінцевої точки (без `api_version`). Затронуті приклади:
  - [06-building-trustworthy-agents/code_samples/06-system-message-framework.ipynb](./06-building-trustworthy-agents/code_samples/06-system-message-framework.ipynb)
  - [06-building-trustworthy-agents/code_samples/06-human-in-the-loop.ipynb](./06-building-trustworthy-agents/code_samples/06-human-in-the-loop.ipynb)
  - [04-tool-use/README.md](./04-tool-use/README.md) — повний покроковий приклад виклику функцій (схема інструменту спрощена до формату Responses, результати інструментів повертаються як `function_call_output`, `max_output_tokens` тощо).

- **Моделі GitHub → Azure OpenAI.** Моделі GitHub застарівають (припинення підтримки **у липні 2026 року**) і не підтримують Responses API. Всі кодові шляхи моделей GitHub були конвертовані на Azure OpenAI / Microsoft Foundry у прикладах Python та .NET:
  - Python: блокноти робочих процесів уроку 08 (`01`–`03`), урок 14 (`14-handoff`, `14-human-loop`, `hotel_booking_workflow_sample.py`).
  - .NET: `01`–`04`, `07`, `08` `*-dotnet-agent-framework.cs` + супровідні `.md` документи, а також робочі блокноти/`.md` уроку 08 dotNET (`01`–`03`) тепер використовують `AzureOpenAIClient(...).GetOpenAIResponseClient(deployment).CreateAIAgent(...)` з `AzureCliCredential`.
- **Semantic Kernel → Microsoft Agent Framework.** Колишній `02-semantic-kernel.ipynb` було переписано для використання Microsoft Agent Framework з Azure OpenAI (Responses API) та перейменовано на `02-python-agent-framework-azure-openai.ipynb`.
- **Стандартизовано на `FoundryChatClient` + `as_agent`.** README та код блокнотів, які зверталися до `AzureAIProjectAgentProvider`, було стандартизовано на канонічний паттерн, що використовується у уроці 01 та у власних прикладах фреймворку: `FoundryChatClient(project_endpoint=..., model=..., credential=AzureCliCredential())` з `provider.as_agent(...)`. Оновлено у README та блокнотах уроків 02–14 (наприклад, пам'ять уроку 13, всі блокноти уроку 14, `11-agentic-protocols/code_samples/github-mcp/app.py`).
- **Назви продуктів.** Перейменовано по всьому англомовному контенту:
  - "Azure AI Foundry" / "Azure AI Studio" → **Microsoft Foundry**
  - "Azure AI Agent Service" → **Microsoft Foundry Agent Service**
  - (Не змінено: "Azure OpenAI", "Azure AI Search", "Azure AI Inference" та імена змінних середовища.)
- **Залежності** ([requirements.txt](../../requirements.txt)):
  - Зафіксовані версії `agent-framework>=1.10.0`, `agent-framework-foundry>=1.10.0`, `agent-framework-openai>=1.10.0`.
  - Зафіксована версія `openai>=1.108.1` (мінімальна для Responses API).
  - Видалено `azure-ai-inference` (використовувався лише у мігрованих прикладах моделей GitHub).
- **Конфігурація середовища** ([.env.example](../../.env.example)): видалено змінні GitHub Models (`GITHUB_TOKEN`, `GITHUB_ENDPOINT`, `GITHUB_MODEL_ID`); додано `AZURE_OPENAI_ENDPOINT`, `AZURE_OPENAI_DEPLOYMENT` та опціональний `AZURE_OPENAI_API_KEY`; оновлено іменування для Microsoft Foundry.
- **Документація** — оновлено [00-course-setup/README.md](./00-course-setup/README.md), [AGENTS.md](./AGENTS.md), [README.md](./README.md) та [STUDY_GUIDE.md](./STUDY_GUIDE.md) для вищезазначеного (налаштування змінних середовища, код перевірки, інструкції по провайдеру, іменування).

### Видалено

- Кроки онбордингу моделей GitHub та змінні середовища з документації налаштування (замінені на Azure OpenAI / Microsoft Foundry).

### Безпека / Конфіденційність (очищення публічного спільного доступу)

- Очищено виводи з виконання Jupyter-блокнотів, які випадково розкривали справжній **ID підписки Azure**, назви ресурсних груп/ресурсів та Bing connection ID, а також **локальні шляхи до файлів та імена користувачів розробників**, у:
  - `08-multi-agent/code_samples/workflows-agent-framework/dotNET/04.dotnet-agent-framework-workflow-aifoundry-condition.ipynb`
  - `08-multi-agent/code_samples/workflows-agent-framework/python/04.python-agent-framework-workflow-aifoundry-condition.ipynb`
  - `15-browser-use/15-browser-user.ipynb`
- Перевірено відсутність ключів API, токенів, ID підписок або персональних шляхів у відстежуваному англомовному контенті (залишки `GITHUB_TOKEN` є токеном GitHub Actions у робочих процесах та PAT сервера GitHub MCP в налаштуванні Уроку 11 — обидва легітимні і не пов’язані з моделями GitHub).

### Примітки та відомі обмеження

- **Не виконувались/не компілювались.** Це освітні приклади, оновлені для коректності API/іменування; вони не запускались з живими ресурсами Azure, і приклади .NET не компілювались у цьому середовищі. Перевірте у вашому власному розгортанні Microsoft Foundry / Azure OpenAI.
- **Розгортання моделей має підтримувати Responses API.** Використовуйте розгортання, як-от `gpt-4.1-mini`, `gpt-4.1` або модель `gpt-5.x`. Старіші моделі підтримують базові функції Responses, але не всі можливості.
- **Версія agent-framework.** Приклади орієнтовані на останній MAF (`>=1.10.0`). Канонічний виклик створення агента — `client.as_agent(...)`; API перевірено відповідно до офіційної документації фреймворку та встановленої збірки. Якщо використовується інша версія, підтвердіть доступність методів (`as_agent` проти `create_agent`).
- **Робочий блокнот уроку 08, приклад 04** навмисно зберігає `AzureAIAgentClient` (з `agent-framework-azure-ai`), бо використовує хостинговані інструменти Microsoft Foundry Agent Service (прив’язка до Bing, інтерпретатор коду); він вже базується на Responses.
- **За замовчуванням розгортання .NET.** Два зразки робочих процесів уроку 08 dotNET раніше жорстко задавали конкретну модель; тепер за замовчуванням використовується `AZURE_OPENAI_DEPLOYMENT` (`gpt-4.1-mini`). Якщо приклад потребує мультимодального/зорового вводу, встановіть `AZURE_OPENAI_DEPLOYMENT` на відповідну модель.
- **Foundry Local** надає кінцеву точку OpenAI-сумісної **Chat Completions** і призначений для локальної розробки; для повного набору функцій Responses API використовуйте Azure OpenAI / Microsoft Foundry.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Відмова від відповідальності**:
Цей документ було перекладено за допомогою сервісу штучного інтелекту для перекладу [Co-op Translator](https://github.com/Azure/co-op-translator). Хоча ми прагнемо до точності, будь ласка, майте на увазі, що автоматичні переклади можуть містити помилки або неточності. Оригінальний документ рідною мовою слід вважати авторитетним джерелом. Для критично важливої інформації рекомендується професійний людський переклад. Ми не несемо відповідальності за будь-які непорозуміння або неправильні тлумачення, що виникли внаслідок використання цього перекладу.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->