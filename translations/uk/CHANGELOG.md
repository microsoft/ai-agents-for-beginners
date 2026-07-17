# Журнал змін

Усі помітні зміни до курсу **AI Agents for Beginners** задокументовані в цьому файлі.

## [Випущено] — 2026-07-13

У цьому релізі додано два нові уроки, які завершують арку розгортання — масштабування агентів до Microsoft Foundry та до однієї робочої станції — а також тестовий конвеєр, оновлену навігацію курсу, нові навички учнів і оновлену брендинг.

### Додано

- **Урок 16 — Розгортання масштабованих агентів за допомогою Microsoft Foundry.** Новий урок [16-deploying-scalable-agents/README.md](./16-deploying-scalable-agents/README.md) та запускаємий нотатник [16-python-agent-framework.ipynb](./16-deploying-scalable-agents/code_samples/16-python-agent-framework.ipynb), що створює виробничого агента для підтримки клієнтів (інструменти, RAG, пам’ять, маршрутизація моделей, кешування відповідей, схвалення людиною, ворота оцінювання та трасування OpenTelemetry), з діаграмами розробки/розгортання/виконання Mermaid, перевіркою знань, завданням та викликом.
- **Урок 17 — Створення локальних AI-агентів за допомогою Foundry Local і Qwen.** Новий урок [17-creating-local-ai-agents/README.md](./17-creating-local-ai-agents/README.md) та нотатник [17-local-agent-foundry-local.ipynb](./17-creating-local-ai-agents/code_samples/17-local-agent-foundry-local.ipynb), що створює повністю локального інженерного помічника (функціональний виклик Qwen через Foundry Local, ізольовані файлові інструменти, локальний RAG з Chroma, необов’язковий локальний MCP), з діаграмами лише локальних, локальних-RAG та виклику інструментів, перевіркою знань, завданням та викликом.
- **Тестовий конвеєр.** Новий workflow [AI Smoke Test](https://github.com/marketplace/actions/ai-smoke-test) [.github/workflows/smoke-test.yml](../../.github/workflows/smoke-test.yml) разом з каталогами для кожного уроку в папці [tests/](./tests/README.md) для розгортальних агентів у Уроках 01, 04, 05 та 16, з індексним README, що зіставляє кожен каталог з відповідним уроком та ім’ям хостованого агента. Урок 16 отримує розділ «Перевірка розгорнутого агента за допомогою smoke-тестів», а Уроки 01/04/05 — необов’язковий покажчик на smoke-тест.
- **Навички учня.** Нові навички агента у `.agents/skills/`: [deploying-scalable-agents](./.agents/skills/deploying-scalable-agents/SKILL.md), [local-ai-agents](./.agents/skills/local-ai-agents/SKILL.md) (упаковка рекомендацій з Уроків 16 та 17) і [testing-course-samples](./.agents/skills/testing-course-samples/SKILL.md) (як перевіряти зразки з нотатників проти живої установки Microsoft Foundry / Azure OpenAI).
- **Запуск валідації нотатників.** Новий скрипт [scripts/validate-notebooks.ps1](../../scripts/validate-notebooks.ps1), який безголосо виконує всі Python нотатники через `nbconvert` і виводить матрицю PASS/FAIL (а також `results.json`). Він автоматично визначає корінь репозиторію та Python, виключає нотатники, що не відносяться до курсу (`.venv`, `site-packages`, `translations`, шаблонні ресурси навичок), а також `.NET` нотатники за замовчуванням, підтримує параметри `-Filter`, `-Timeout`, `-List`, `-IncludeDotnet` і `-Python`.
- **Навігація по курсу.** Додано посилання Попередній/Наступний уроки в Уроках 11–15 (раніше відсутні), щоб увесь курс з'єднувався ланцюжком від 00 до 18 в обох напрямках.
- **Нові мініатюри.** Мініатюри уроків 16 і 17, а також оновлене соціальне зображення репозиторію [images/repo-thumbnailv3.png](./images/repo-thumbnailv3.png) (тепер рекламуюче два нові уроки та URL `aka.ms/ai-agents-beginners`).
- **Залежності** ([requirements.txt](../../requirements.txt)): додано `foundry-local-sdk` і `chromadb` для Уроку 17.

### Змінено

- **Головна таблиця уроків у [README.md](./README.md):** Уроки 16 і 17 тепер посилаються на їхній контент (раніше було «Незабаром»); зображення репозиторію оновлено до `repo-thumbnailv3.png`.
- **[STUDY_GUIDE.md](./STUDY_GUIDE.md):** додано Уроки 16 і 17 до поурочного керівництва та навчальних шляхів, а також секцію «Перевірка розгорнутих агентів за допомогою smoke-тестів».
- **[AGENTS.md](./AGENTS.md):** оновлено кількість/опис уроків (00–18), додано секцію перевірки smoke-тестів, додано приклади найменування зразків Уроків 16/17.
- **[18-securing-ai-agents/README.md](./18-securing-ai-agents/README.md):** «Попередній урок» тепер посилається на Урок 17 (було Урок 15), замкнувши ланцюг.
- **Стандартизовані посилання на моделі, які не застарілі.** Замінено всі посилання `gpt-4o` / `gpt-4o-mini` по курсу (документація, `.env.example`, Python/.NET нотатники та приклади) на `gpt-4.1-mini` — `gpt-4o` (всі версії) буде припинено в 2026 році. Приклад маршрутизації моделей з Уроку 16 зберігає контраст маленька/велика, використовуючи `gpt-4.1-mini` (маленька) і `gpt-4.1` (велика). Python нотатники тепер вибирають модель з змінних оточення (`AZURE_AI_MODEL_DEPLOYMENT_NAME` / `AZURE_OPENAI_DEPLOYMENT`) замість жорсткого кодування назви моделі.

### Примітки й відомі обмеження

- **Не виконувалося проти живого Azure.** Нотатники нових уроків — це освітні зразки; запускайте і перевіряйте їх на вашій установці Microsoft Foundry / Foundry Local. Конвеєр smoke-тесту вимагає розгорнути агента уроку та налаштувати секрети Azure OIDC (`AZURE_CLIENT_ID`, `AZURE_TENANT_ID`, `AZURE_SUBSCRIPTION_ID`) із роллю **Azure AI User** в межах проєкту Foundry.
- **Урок 17 — лише локальний.** У нього немає кінцевої точки Foundry Responses, тому дія smoke-тесту не застосовується; перевіряйте його, виконуючи нотатник на вашій робочій станції.

## [Випущено] — 2026-07-06

Цей реліз мігрує курс на **Azure OpenAI Responses API**, стандартизує найменування продуктів на **Microsoft Foundry** і **Microsoft Agent Framework (MAF)**, припиняє підтримку GitHub Models, оновлює версії SDK і додає новий контент про локальні моделі та хостинг інших фреймворків на Foundry.

### Додано

- **Навичка міграції** — Встановлена навичка агента [`azure-openai-to-responses`](./.agents/skills/azure-openai-to-responses/SKILL.md) (з репозиторію [Azure-Samples/azure-openai-to-responses](https://github.com/Azure-Samples/azure-openai-to-responses)) під `.agents/skills/`, включно з посиланнями та скриптом сканера.
- **Foundry Local (запуск моделей на пристрої)** — Новий розділ «Альтернативний провайдер: Foundry Local» в [00-course-setup/README.md](./00-course-setup/README.md), що охоплює інсталяцію (`winget` / `brew`), команду `foundry model run`, `foundry-local-sdk` та інтеграцію `FoundryLocalManager` з Microsoft Agent Framework через `OpenAIChatClient`.
- **Хостинг агентів LangChain / LangGraph на Microsoft Foundry** — Новий розділ у [14-microsoft-agent-framework/README.md](./14-microsoft-agent-framework/README.md) та запускаємий приклад [14-langchain-hosted-agent.py](../../14-microsoft-agent-framework/code-samples/14-langchain-hosted-agent.py), що використовує `langchain-azure-ai[hosting]` і `ResponsesHostServer` (протокол `/responses`), базуючись на [Microsoft Learn](https://learn.microsoft.com/azure/foundry/how-to/develop/langchain-hosted-agents).
- **Microsoft Project Opal** — Новий розділ «Приклад з реального світу: Microsoft Project Opal» у [15-browser-use/README.md](./15-browser-use/README.md), що подає Opal як агента корпоративного використання комп’ютера та відображає його відповідність концепціям курсу (людина в циклі, довіра/безпека, планування, Навички).
- **Другий приклад Python з Уроку 02** — Додано [02-python-agent-framework-azure-openai.ipynb](./02-explore-agentic-frameworks/code_samples/02-python-agent-framework-azure-openai.ipynb) (див. «Змінено» — міграція зі старого нотатника Semantic Kernel) і додано посилання на нього в README уроку.
- Додано розділ «Моделі та Провайдери» в [STUDY_GUIDE.md](./STUDY_GUIDE.md).

### Змінено

- **Chat Completions → Responses API (Python).** Зразки, які безпосередньо викликали модель, були мігровані з Chat Completions на Responses API (`client.responses.create(input=..., store=False)`, `resp.output_text`), використовуючи клієнт `OpenAI` для стабільної точки Azure OpenAI `/openai/v1/` без `api_version`. Постраждалі зразки включають:
  - [06-building-trustworthy-agents/code_samples/06-system-message-framework.ipynb](./06-building-trustworthy-agents/code_samples/06-system-message-framework.ipynb)
  - [06-building-trustworthy-agents/code_samples/06-human-in-the-loop.ipynb](./06-building-trustworthy-agents/code_samples/06-human-in-the-loop.ipynb)
  - [04-tool-use/README.md](./04-tool-use/README.md) — повний крок за кроком виклик функції (схема інструменту сплощена до формату Responses, результати інструменту повертаються як `function_call_output`, `max_output_tokens` тощо).
- **GitHub Models → Azure OpenAI.** GitHub Models застаріває (припиняється **в липні 2026**) і не підтримує Responses API. Всі шляхи коду GitHub Models були конвертовані до Azure OpenAI / Microsoft Foundry у прикладах Python та .NET:
  - Python: нотатники робочих процесів Уроку 08 (`01`–`03`), Урок 14 (`14-handoff`, `14-human-loop`, `hotel_booking_workflow_sample.py`).
  - .NET: `01`–`04`, `07`, `08` `*-dotnet-agent-framework.cs` + супровідна документація `.md`, а робочі нотатники/`.md` з Уроку 08 тепер використовують `AzureOpenAIClient(...).GetOpenAIResponseClient(deployment).CreateAIAgent(...)` з `AzureCliCredential`.
- **Semantic Kernel → Microsoft Agent Framework.** Старий нотатник `02-semantic-kernel.ipynb` був переписаний під Microsoft Agent Framework з Azure OpenAI (Responses API) і перейменований на `02-python-agent-framework-azure-openai.ipynb`.
- **Стандартизовано використання `FoundryChatClient` + `as_agent`.** README та код нотатників, що посилались на `AzureAIProjectAgentProvider`, були стандартизовані на канонічний патерн із Уроку 01 та власних прикладів фреймворку: `FoundryChatClient(project_endpoint=..., model=..., credential=AzureCliCredential())` з `provider.as_agent(...)`. Оновлено у README і нотатниках Уроків 02–14 (наприклад, пам’ять Уроку 13, усі нотатники Уроку 14, `11-agentic-protocols/code_samples/github-mcp/app.py`).
- **Найменування продукту.** Перейменовано в англомовному контенті:
  - "Azure AI Foundry" / "Azure AI Studio" → **Microsoft Foundry**
  - "Azure AI Agent Service" → **Microsoft Foundry Agent Service**
  - (Без змін: "Azure OpenAI", "Azure AI Search", "Azure AI Inference" та імена змінних оточення.)
- **Залежності** ([requirements.txt](../../requirements.txt)):
  - Закріплено `agent-framework>=1.10.0`, `agent-framework-foundry>=1.10.0`, `agent-framework-openai>=1.10.0`.
  - Закріплено `openai>=1.108.1` (мінімум для Responses API).
  - Видалено `azure-ai-inference` (використовувався лише у мігрованих прикладах GitHub Models).
- **Конфігурація оточення** ([.env.example](../../.env.example)): видалено змінні GitHub Models (`GITHUB_TOKEN`, `GITHUB_ENDPOINT`, `GITHUB_MODEL_ID`); додано `AZURE_OPENAI_ENDPOINT`, `AZURE_OPENAI_DEPLOYMENT` та необов’язковий `AZURE_OPENAI_API_KEY`; оновлено найменування на Microsoft Foundry.
- **Документація** — Оновлено [00-course-setup/README.md](./00-course-setup/README.md), [AGENTS.md](./AGENTS.md), [README.md](./README.md) і [STUDY_GUIDE.md](./STUDY_GUIDE.md) відповідно до вищезгаданого (налаштування змінних оточення, фрагмент перевірки, керівництво провайдера, найменування).

### Видалено

- Кроки початку роботи з GitHub Models і змінні оточення вилучені з документації з налаштування (замінено на Azure OpenAI / Microsoft Foundry).

### Безпека / Приватність (очищення публічного доступу)

- Очищено виводи виконання Jupyter нотатників, які містили дійсний **Azure subscription ID**, імена груп ресурсів/ресурсів та ідентифікатор Bing, а також локальні шляхи файлів і імена користувачів розробників у:
  - `08-multi-agent/code_samples/workflows-agent-framework/dotNET/04.dotnet-agent-framework-workflow-aifoundry-condition.ipynb`

  - `08-multi-agent/code_samples/workflows-agent-framework/python/04.python-agent-framework-workflow-aifoundry-condition.ipynb`
  - `15-browser-use/15-browser-user.ipynb`
- Перевірено, що у відстеженому англійському вмісті не залишилось ключів API, токенів, ідентифікаторів підписок чи персональних шляхів (посилання на `GITHUB_TOKEN`, що залишилися, це токен GitHub Actions у робочих процесах і PAT сервера GitHub MCP у налаштуванні Уроку 11 — обидва законні та не пов’язані з GitHub Models).

### Примітки та відомі обмеження

- **Не виконувались/не компілювались.** Це навчальні зразки, оновлені для коректності API/імен; вони не запускалися на живих ресурсах Azure, а зразки .NET не компілювалися у цьому середовищі. Перевіряйте на власному розгортанні Microsoft Foundry / Azure OpenAI.
- **Розгортання моделі має підтримувати Responses API.** Використовуйте розгортання, наприклад, `gpt-4.1-mini`, `gpt-4.1` або модель `gpt-5.x`. Старші моделі підтримують основний функціонал Responses, але не всі особливості.
- **Версія agent-framework.** Зразки орієнтовані на останню MAF (`>=1.10.0`). Канонічний виклик створення агента — `client.as_agent(...)`; API перевірялися за опублікованою документацією фреймворку та встановленою збіркою. Якщо ви використовуєте іншу версію, підтвердіть наявність методу (`as_agent` чи `create_agent`).
- **Ноутбук робочого процесу Уроку 08, файл 04** свідомо залишає `AzureAIAgentClient` (з `agent-framework-azure-ai`), оскільки він використовує інструменти Microsoft Foundry Agent Service (Bing grounding, кодовий інтерпретатор); він вже базується на Responses.
- **За замовчуванням розгортання .NET.** Два зразки робочого процесу dotNET з Уроку 08 раніше жорстко прив’язувалися до конкретної моделі; тепер за замовчуванням використовують `AZURE_OPENAI_DEPLOYMENT` (`gpt-4.1-mini`). Якщо зразок залежить від мультимодального/зорового вводу, задайте `AZURE_OPENAI_DEPLOYMENT` відповідною моделлю.
- **Foundry Local** надає сумісну з OpenAI кінцеву точку **Chat Completions** і призначений для локальної розробки; для повного набору функцій Responses API використовуйте Azure OpenAI / Microsoft Foundry.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Відмова від відповідальності**:
Цей документ було перекладено за допомогою сервісу штучного інтелекту для перекладу [Co-op Translator](https://github.com/Azure/co-op-translator). Хоча ми прагнемо до точності, будь ласка, майте на увазі, що автоматичні переклади можуть містити помилки або неточності. Оригінальний документ рідною мовою слід вважати авторитетним джерелом. Для критично важливої інформації рекомендується професійний людський переклад. Ми не несемо відповідальності за будь-які непорозуміння або неправильні тлумачення, що виникли внаслідок використання цього перекладу.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->