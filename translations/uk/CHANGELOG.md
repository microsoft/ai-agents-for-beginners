# Історія змін

Усі помітні зміни курсу **AI Agents for Beginners** документуються у цьому файлі.

## [Неопубліковано] — 2026-07-06

Це оновлення мігрує курс на **Azure OpenAI Responses API**, стандартизує номенклатуру продуктів на **Microsoft Foundry** та **Microsoft Agent Framework (MAF)**, припиняє використання GitHub Models, оновлює версії SDK і додає новий контент про локальні моделі та хостинг інших фреймворків на Foundry.

### Додано

- **Навик міграції** — Встановлено Agent Skill [`azure-openai-to-responses`](./.agents/skills/azure-openai-to-responses/SKILL.md) (з [Azure-Samples/azure-openai-to-responses](https://github.com/Azure-Samples/azure-openai-to-responses)) у `.agents/skills/`, включно з посиланнями та скриптом сканера.
- **Foundry Local (запуск моделей на пристрої)** — Нова секція "Alternative Provider: Foundry Local" у [00-course-setup/README.md](./00-course-setup/README.md) охоплює встановлення (`winget` / `brew`), `foundry model run`, `foundry-local-sdk` та підключення `FoundryLocalManager` до Microsoft Agent Framework через `OpenAIChatClient`.
- **Хостинг агентів LangChain / LangGraph на Microsoft Foundry** — Нова секція в [14-microsoft-agent-framework/README.md](./14-microsoft-agent-framework/README.md) і runnable приклад [14-langchain-hosted-agent.py](../../14-microsoft-agent-framework/code-samples/14-langchain-hosted-agent.py) з використанням `langchain-azure-ai[hosting]` та `ResponsesHostServer` (протокол `/responses`), на основі [Microsoft Learn](https://learn.microsoft.com/azure/foundry/how-to/develop/langchain-hosted-agents).
- **Microsoft Project Opal** — Нова секція "Real-World Example: Microsoft Project Opal" у [15-browser-use/README.md](./15-browser-use/README.md), що описує Opal як агент для корпоративного використання комп’ютера та зв’язок із концепціями курсу (людина в циклі, довіра/безпека, планування, навички).
- **Другий приклад з уроку 02 Python** — Додано [02-python-agent-framework-azure-openai.ipynb](./02-explore-agentic-frameworks/code_samples/02-python-agent-framework-azure-openai.ipynb) (див. "Змінено" — міграція з колишньої тетрадки Semantic Kernel) і додано посилання в README уроку.
- Додано секцію "Models and Providers" у [STUDY_GUIDE.md](./STUDY_GUIDE.md).

### Змінено

- **Chat Completions → Responses API (Python).** Приклади, які викликали модель безпосередньо, мігрували з Chat Completions на Responses API (`client.responses.create(input=..., store=False)`, `resp.output_text`), використовуючи клієнт `OpenAI` проти стабільної кінцевої точки Azure OpenAI `/openai/v1/` (без `api_version`). Змінені приклади включають:
  - [06-building-trustworthy-agents/code_samples/06-system-message-framework.ipynb](./06-building-trustworthy-agents/code_samples/06-system-message-framework.ipynb)
  - [06-building-trustworthy-agents/code_samples/06-human-in-the-loop.ipynb](./06-building-trustworthy-agents/code_samples/06-human-in-the-loop.ipynb)
  - [04-tool-use/README.md](./04-tool-use/README.md) — повний крок за кроком виклик функцій (схема інструментів перетворена у формат Responses, результати інструментів повертаються як `function_call_output`, `max_output_tokens` тощо).
- **GitHub Models → Azure OpenAI.** GitHub Models застарілий (припиняється **липень 2026**) і не підтримує Responses API. Усі шляхи коду GitHub Models конвертовані на Azure OpenAI / Microsoft Foundry у прикладах Python та .NET:
  - Python: workflow-тетрадки уроку 08 (`01`–`03`), урок 14 (`14-handoff`, `14-human-loop`, `hotel_booking_workflow_sample.py`).
  - .NET: `01`–`04`, `07`, `08` файли `*-dotnet-agent-framework.cs` + супровідна документація `.md`, та workflow-тетрадки / `.md` уроку 08 dotNET (`01`–`03`) тепер використовують `AzureOpenAIClient(...).GetOpenAIResponseClient(deployment).CreateAIAgent(...)` з `AzureCliCredential`.
- **Semantic Kernel → Microsoft Agent Framework.** Колишній `02-semantic-kernel.ipynb` переписано на Microsoft Agent Framework з Azure OpenAI (Responses API) і перейменовано в `02-python-agent-framework-azure-openai.ipynb`.
- **Стандартизовано `FoundryChatClient` + `as_agent`.** README і код тетрадок, що посилалися на `AzureAIProjectAgentProvider`, стандартизовані під канонічний патерн, що використовується в Уроці 01 і власних прикладах фреймворку: `FoundryChatClient(project_endpoint=..., model=..., credential=AzureCliCredential())` з `provider.as_agent(...)`. Оновлено у README та тетрадках Построк 02–14 (наприклад, пам’ять у уроці 13, всі тетрадки уроку 14, `11-agentic-protocols/code_samples/github-mcp/app.py`).
- **Номенклатура продуктів.** Перейменовано по всьому англомовному контенту:
  - "Azure AI Foundry" / "Azure AI Studio" → **Microsoft Foundry**
  - "Azure AI Agent Service" → **Microsoft Foundry Agent Service**
  - (Без змін: "Azure OpenAI", "Azure AI Search", "Azure AI Inference" та імена змінних оточення.)
- **Залежності** ([requirements.txt](../../requirements.txt)):
  - Закріплено `agent-framework>=1.10.0`, `agent-framework-foundry>=1.10.0`, `agent-framework-openai>=1.10.0`.
  - Закріплено `openai>=1.108.1` (мінімально для Responses API).
  - Видалено `azure-ai-inference` (використовувався лише у мігрованих прикладах GitHub Models).
- **Конфігурація оточення** ([.env.example](../../.env.example)): видалено змінні для GitHub Models (`GITHUB_TOKEN`, `GITHUB_ENDPOINT`, `GITHUB_MODEL_ID`); додано `AZURE_OPENAI_ENDPOINT`, `AZURE_OPENAI_DEPLOYMENT` і необов’язковий `AZURE_OPENAI_API_KEY`; оновлено назви на Microsoft Foundry.
- **Документація** — Оновлено [00-course-setup/README.md](./00-course-setup/README.md), [AGENTS.md](./AGENTS.md), [README.md](./README.md) та [STUDY_GUIDE.md](./STUDY_GUIDE.md) відповідно (налаштування змінних, фрагмент перевірки, рекомендації провайдера, номенклатура).

### Видалено

- Кроки початкової настройки GitHub Models та змінні оточення з документації (замінено Azure OpenAI / Microsoft Foundry).

### Безпека / Конфіденційність (прибирання публічних даних)

- Очищено виводи виконання у Jupyter notebook, що містили реальний **ідентифікатор підписки Azure**, назви ресурсних груп / ресурсів і Bing connection ID, а також локальні шляхи файлів та імена користувачів розробника, у:
  - `08-multi-agent/code_samples/workflows-agent-framework/dotNET/04.dotnet-agent-framework-workflow-aifoundry-condition.ipynb`
  - `08-multi-agent/code_samples/workflows-agent-framework/python/04.python-agent-framework-workflow-aifoundry-condition.ipynb`
  - `15-browser-use/15-browser-user.ipynb`
- Перевірено, що у відслідкованому англомовному контенті не залишилось API ключів, токенів, ідентифікаторів підписок чи особистих шляхів (посилання на `GITHUB_TOKEN` залишились у workflows GitHub Actions та PAT серверу GitHub MCP у налаштуванні Уроку 11 — обидва є легітимними і не пов’язані з GitHub Models).

### Примітки і відомі обмеження

- **Не виконувались/не компілювались.** Це освітні приклади, оновлені для правильності API / номенклатури; вони не запускались проти живих ресурсів Azure, а приклади .NET не компілювались у цьому середовищі. Перевіряйте з вашим власним розгортанням Microsoft Foundry / Azure OpenAI.
- **Розгортання моделі має підтримувати Responses API.** Використовуйте розгортання типу `gpt-4o-mini`, `gpt-4.1` або модель `gpt-5.x`. Старіші моделі підтримують основний функціонал Responses, але не всі функції.
- **Версія agent-framework.** Приклади орієнтовані на останню версію MAF (`>=1.10.0`). Канонічним викликом створення агента є `client.as_agent(...)`; API були перевірені за опублікованою документацією фреймворку і встановленою збіркою. Якщо ви фіксуєте іншу версію — перевірте наявність методу (`as_agent` vs `create_agent`).
- **Workflow-тетрадка 04 уроку 08** свідомо зберігає `AzureAIAgentClient` (з `agent-framework-azure-ai`), бо використовує хостингові інструменти Microsoft Foundry Agent Service (Bing grounding, code interpreter); вона вже на Responses API.
- **.NET розгортання за замовчуванням.** Два workflow-приклади уроку 08 dotNET раніше жорстко кодували `gpt-4o`; тепер вони за замовчуванням використовують `AZURE_OPENAI_DEPLOYMENT` (`gpt-4o-mini`). Якщо приклад потребує мультимодального/візуального вводу — встановіть `AZURE_OPENAI_DEPLOYMENT` на відповідну модель.
- **Foundry Local** відкриває OpenAI-сумісну кінцеву точку **Chat Completions** і призначений для локальної розробки; для повного набору функцій Responses API використовуйте Azure OpenAI / Microsoft Foundry.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Відмова від відповідальності**:
Цей документ було перекладено за допомогою сервісу штучного інтелекту для перекладу [Co-op Translator](https://github.com/Azure/co-op-translator). Хоча ми прагнемо до точності, будь ласка, майте на увазі, що автоматичні переклади можуть містити помилки або неточності. Оригінальний документ рідною мовою слід вважати авторитетним джерелом. Для критично важливої інформації рекомендується професійний людський переклад. Ми не несемо відповідальності за будь-які непорозуміння або неправильні тлумачення, що виникли внаслідок використання цього перекладу.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->