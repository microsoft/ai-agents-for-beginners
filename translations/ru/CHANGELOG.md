# Журнал изменений

Все заметные изменения курса **AI Agents for Beginners** задокументированы в этом файле.

## [Выпущено] — 2026-07-14

Этот релиз переводит курс с двух недавно устаревших моделей, мигрирует оставшиеся ноутбуки уроков на стабильный API Microsoft Agent Framework и проверяет Python-ноутбуки на живом развертывании Microsoft Foundry.

### Изменено

- **Переход с устаревших моделей (`gpt-4.1` / `gpt-4.1-mini` → `gpt-5-mini`).** Обе модели `gpt-4.1` и `gpt-4.1-mini` теперь устарели (дата официального вывода из эксплуатации **14 октября 2026**). Каждое упоминание модели в курсе (документация, `.env.example`, Python/.NET ноутбуки и примеры) заменено на неустаревшую `gpt-5-mini`. В примере маршрутизации модели урока 16 сохраняется контраст «маленькая/большая» с использованием `gpt-5-nano` (маленькая) и `gpt-5-mini` (большая). Вендорные сторонние файлы ([15-browser-use/llms.txt](../../15-browser-use/llms.txt)), исторический текст GitHub Models и заметки о возможностях скилла `azure-openai-to-responses` оставлены без изменений намеренно.
- **Ноутбук передачи управления урока 14 мигрирован на стабильный API.** [14-handoff.ipynb](./14-microsoft-agent-framework/code-samples/14-handoff.ipynb) теперь использует `agent_framework.orchestrations.HandoffBuilder` с `.with_start_agent(...)`, `HandoffAgentUserRequest.create_response(...)`, потоковую передачу на основе `event.type` и `FoundryChatClient` (замена удалённых символов до версии 1.0: `HandoffBuilder`/`ChatMessage`/`RequestInfoEvent`).
- **Ноутбук «человек в цикле» урока 14 мигрирован на стабильный API.** [14-human-loop.ipynb](./14-microsoft-agent-framework/code-samples/14-human-loop.ipynb) теперь приостанавливает выполнение с помощью `ctx.request_info(...)` + `@response_handler` (замена удалённых `RequestInfoExecutor` / `RequestInfoMessage` / `RequestResponse`), строится с `WorkflowBuilder(start_executor=..., output_executors=[...])`, формирует структурированный вывод с `default_options={"response_format": ...}`, и использует скриптовый ответ для запуска без блокировок (`input()` отсутствует).
- **Конфигурация окружения** ([.env.example](../../.env.example)): изменены имена развертываний моделей на `gpt-5-mini`; добавлены `AZURE_AI_SMALL_MODEL` / `AZURE_AI_LARGE_MODEL` (маршрутизация урока 16) и ранее отсутствующий `AZURE_OPENAI_CHAT_DEPLOYMENT_NAME` (использование браузера урока 15).
- **Зависимости** ([requirements.txt](../../requirements.txt)): зафиксированы версии `agent-framework`, `agent-framework-foundry` и `agent-framework-openai` на `~=1.10.0` для согласованного и проверенного набора (версия 1.11.0 включает экспериментальные несовместимые изменения в интерфейсах, используемых в уроках).

### Примечания и известные ограничения

- **Проверено на живом Microsoft Foundry.** Python-ноутбуки запускались без интерфейса с `nbconvert` на проекте Microsoft Foundry с использованием `gpt-5-mini` (и `gpt-5-nano` для маршрутизации урока 16). Разверните эквивалентные неустаревшие модели в своём проекте; ноутбуки читают имя развертывания из `AZURE_AI_MODEL_DEPLOYMENT_NAME` / `AZURE_OPENAI_DEPLOYMENT`.
- **Некоторые уроки по-прежнему требуют дополнительных ресурсов.** Урок 05 нуждается в Azure AI Search; рабочий процесс Bing урока 08 (`04.python-agent-framework-workflow-aifoundry-condition.ipynb`) требует подключения к Bing и инструментов Microsoft Foundry Agent Service; уроки 13 (Cognee) и 17 (Foundry Local) требуют собственных рантаймов.

## [Выпущено] — 2026-07-13

В этом релизе добавлены два новых урока, завершающих арку развертывания — масштабирование агентов до Microsoft Foundry и сворачивание до одного рабочего места — а также новый pipeline дымового теста, обновлённая навигация по курсу, новые навыки для обучающихся и обновлённый брендинг.

### Добавлено

- **Урок 16 — Развёртывание масштабируемых агентов с Microsoft Foundry.** Новый урок [16-deploying-scalable-agents/README.md](./16-deploying-scalable-agents/README.md) и рабочий ноутбук [16-python-agent-framework.ipynb](./16-deploying-scalable-agents/code_samples/16-python-agent-framework.ipynb), создающий продакшн агента поддержки клиентов (инструменты, RAG, память, маршрутизация моделей, кеширование ответов, утверждение человеком, оценочный шлюз, трассировка OpenTelemetry), с диаграммами разработки, развертывания и работы Mermaid, проверкой знаний, заданием и вызовом к действию.
- **Урок 17 — Создание локальных AI-агентов с Foundry Local и Qwen.** Новый урок [17-creating-local-ai-agents/README.md](./17-creating-local-ai-agents/README.md) и ноутбук [17-local-agent-foundry-local.ipynb](./17-creating-local-ai-agents/code_samples/17-local-agent-foundry-local.ipynb), строящий полностью локального помощника инженера (вызовы функций Qwen через Foundry Local, песочница для файловых инструментов, локальный RAG с Chroma, опциональный локальный MCP), с локальными/локальным RAG/инструментальными диаграммами, проверкой знаний, заданием и вызовом к действию.
- **Pipeline дымового тестирования.** Новый workflow [AI Smoke Test](https://github.com/marketplace/actions/ai-smoke-test) [.github/workflows/smoke-test.yml](../../.github/workflows/smoke-test.yml) и каталоги по урокам в [tests/](./tests/README.md) для развертываемых агентов в уроках 01, 04, 05 и 16, с индексным README, сопоставляющим каталоги с уроками и именами размещённых агентов. Урок 16 получил раздел "Проверка развернутого агента дымовыми тестами"; уроки 01/04/05 получили опциональный указатель к дымовому тесту.
- **Навыки обучающихся.** Новые навыки агента под `.agents/skills/`: [deploying-scalable-agents](./.agents/skills/deploying-scalable-agents/SKILL.md), [local-ai-agents](./.agents/skills/local-ai-agents/SKILL.md) (объединяющие рекомендации уроков 16 и 17) и [testing-course-samples](./.agents/skills/testing-course-samples/SKILL.md) (способы проверки ноутбуков с жизненным Microsoft Foundry / Azure OpenAI).
- **Запуск проверки ноутбуков.** Новый скрипт [scripts/validate-notebooks.ps1](../../scripts/validate-notebooks.ps1), который последовательно выполняет все Python-ноутбуки без интерфейса с помощью `nbconvert` и выводит матрицу PASS/FAIL (плюс `results.json`). Автоматически определяет корень репозитория и Python, по умолчанию исключает ноутбуки вне курса (`.venv`, `site-packages`, `translations`, служебные файлы скиллов) и `.NET` ноутбуки, поддерживает параметры `-Filter`, `-Timeout`, `-List`, `-IncludeDotnet` и `-Python`.
- **Навигация по курсу.** Добавлены ссылки "Предыдущий"/"Следующий" для уроков 11–15 (которые ранее отсутствовали), чтобы весь курс шел с 00 до 18 и в прямом, и в обратном порядке.
- **Новые миниатюры.** Миниатюры уроков 16 и 17, а также обновлённое социальное изображение репозитория [images/repo-thumbnailv3.png](./images/repo-thumbnailv3.png) (теперь с рекламой двух новых уроков и URL `aka.ms/ai-agents-beginners`).
- **Зависимости** ([requirements.txt](../../requirements.txt)): добавлены `foundry-local-sdk` и `chromadb` для урока 17.

### Изменено

- **Основная таблица уроков [README.md](./README.md):** уроки 16 и 17 теперь ссылаются на свой контент (раньше было "Скоро"); изображение репозитория обновлено на `repo-thumbnailv3.png`.
- **[STUDY_GUIDE.md](./STUDY_GUIDE.md):** добавлены уроки 16 и 17 в пошаговое руководство и пути обучения, а также раздел "Проверка развернутых агентов с помощью дымовых тестов".
- **[AGENTS.md](./AGENTS.md):** обновлено количество и описание уроков (с 00 по 18), добавлен раздел про проверку с помощью дымовых тестов и примеры имен агентов для уроков 16 и 17.
- **[18-securing-ai-agents/README.md](./18-securing-ai-agents/README.md):** "Предыдущий урок" теперь указывает на урок 17 (раньше был урок 15), замыкая цепочку.
- **Унификация ссылок на модели, снятые с поддержки.** Заменены все упоминания `gpt-4o` / `gpt-4o-mini` по всему курсу (документация, `.env.example`, Python/.NET ноутбуки и примеры) на `gpt-4.1-mini` — `gpt-4o` (всех версий) будет снят с поддержки в 2026 году. В примере маршрутизации моделей урока 16 сохраняется контраст маленькой/большой модели с использованием `gpt-4.1-mini` (маленькая) и `gpt-4.1` (большая). Python-ноутбуки теперь выбирают модель из переменных окружения (`AZURE_AI_MODEL_DEPLOYMENT_NAME` / `AZURE_OPENAI_DEPLOYMENT`), а не из жестко закодированного имени модели.

### Примечания и известные ограничения

- **Не выполнено на живом Azure.** Новые ноутбуки уроков — учебные образцы; запуск и проверка должны происходить на вашей собственной установке Microsoft Foundry / Foundry Local. Workflow дымового теста требует развертывания агента урока и настройки секретов Azure OIDC (`AZURE_CLIENT_ID`, `AZURE_TENANT_ID`, `AZURE_SUBSCRIPTION_ID`) с ролью **Azure AI User** на уровне проекта Foundry.
- **Урок 17 исключительно локальный.** У него нет конечной точки Foundry Responses, поэтому действие дымового теста не применимо; проверяйте его путем запуска ноутбука на своем рабочем месте.

## [Выпущено] — 2026-07-06

Этот релиз мигрирует курс на **API Azure OpenAI Responses**, стандартизирует названия продуктов на **Microsoft Foundry** и **Microsoft Agent Framework (MAF)**, выводит из эксплуатации GitHub Models, обновляет версии SDK и добавляет новый контент по локальным моделям и хостингу других фреймворков на Foundry.

### Добавлено

- **Скилл миграции** — Установлен агент скилл [`azure-openai-to-responses`](./.agents/skills/azure-openai-to-responses/SKILL.md) (с [Azure-Samples/azure-openai-to-responses](https://github.com/Azure-Samples/azure-openai-to-responses)) под `.agents/skills/`, включая все ссылки и скрипт сканера.
- **Foundry Local (запуск моделей на устройстве)** — Новый раздел "Альтернативный провайдер: Foundry Local" в [00-course-setup/README.md](./00-course-setup/README.md), описывающий установку (`winget` / `brew`), `foundry model run`, `foundry-local-sdk`, и интеграцию `FoundryLocalManager` с Microsoft Agent Framework через `OpenAIChatClient`.
- **Хостинг агентов LangChain / LangGraph на Microsoft Foundry** — Новый раздел в [14-microsoft-agent-framework/README.md](./14-microsoft-agent-framework/README.md) и запускаемый пример [14-langchain-hosted-agent.py](../../14-microsoft-agent-framework/code-samples/14-langchain-hosted-agent.py), использующий `langchain-azure-ai[hosting]` и `ResponsesHostServer` (протокол `/responses`), основанный на материалах [Microsoft Learn](https://learn.microsoft.com/azure/foundry/how-to/develop/langchain-hosted-agents).
- **Microsoft Project Opal** — Новый раздел "Пример из реальной жизни: Microsoft Project Opal" в [15-browser-use/README.md](./15-browser-use/README.md), представляющий Opal как корпоративного агента для работы с компьютером и сопоставляющий его с концепциями курса (человек в цикле, доверие/безопасность, планирование, Скиллы).
- **Второй Python-пример урока 02** — Добавлен [02-python-agent-framework-azure-openai.ipynb](./02-explore-agentic-frameworks/code_samples/02-python-agent-framework-azure-openai.ipynb) (см. раздел «Изменено» — мигрирован из бывшего ноутбука Semantic Kernel) и ссылка на него в README урока.
- Добавлен раздел "Модели и провайдеры" в [STUDY_GUIDE.md](./STUDY_GUIDE.md).

### Изменено

- **Chat Completions → Responses API (Python).** Образцы, напрямую вызывавшие модель, были мигрированы с Chat Completions на Responses API (`client.responses.create(input=..., store=False)`, `resp.output_text`), используя клиент `OpenAI` с стабильной точки Azure OpenAI `/openai/v1/` (без `api_version`). Затронутые образцы включают:
  - [06-building-trustworthy-agents/code_samples/06-system-message-framework.ipynb](./06-building-trustworthy-agents/code_samples/06-system-message-framework.ipynb)
  - [06-building-trustworthy-agents/code_samples/06-human-in-the-loop.ipynb](./06-building-trustworthy-agents/code_samples/06-human-in-the-loop.ipynb)
  - [04-tool-use/README.md](./04/tool-use/README.md) — полный разбор функции вызова (схема инструментов приведена к формату Responses, результаты инструментов возвращаются как `function_call_output`, `max_output_tokens` и т. д.).

- **GitHub Models → Azure OpenAI.** GitHub Models устарел (будет закрыт в **июле 2026**) и не поддерживает Responses API. Все пути кода GitHub Models были преобразованы в Azure OpenAI / Microsoft Foundry в примерах на Python и .NET:
  - Python: workflow notebooks урока 08 (`01`–`03`), урок 14 (`14-handoff`, `14-human-loop`, `hotel_booking_workflow_sample.py`).
  - .NET: `01`–`04`, `07`, `08` `*-dotnet-agent-framework.cs` + сопутствующая документация `.md`, а также workflow notebooks/`.md` урока 08 на dotNET (`01`–`03`) теперь используют `AzureOpenAIClient(...).GetOpenAIResponseClient(deployment).CreateAIAgent(...)` с `AzureCliCredential`.
- **Semantic Kernel → Microsoft Agent Framework.** Старый файл `02-semantic-kernel.ipynb` был переписан с использованием Microsoft Agent Framework с Azure OpenAI (Responses API) и переименован в `02-python-agent-framework-azure-openai.ipynb`.
- **Стандартизировано на `FoundryChatClient` + `as_agent`.** README и код в ноутбуках, которые ссылались на `AzureAIProjectAgentProvider`, стандартизированы по каноническому шаблону, использованному в уроке 01 и собственных примерах фреймворка: `FoundryChatClient(project_endpoint=..., model=..., credential=AzureCliCredential())` с `provider.as_agent(...)`. Обновлено во всех README и ноутбуках уроков 02–14 (например, память урока 13, все ноутбуки урока 14, `11-agentic-protocols/code_samples/github-mcp/app.py`).
- **Именование продуктов.** Переименовано во всём англоязычном контенте:
  - "Azure AI Foundry" / "Azure AI Studio" → **Microsoft Foundry**
  - "Azure AI Agent Service" → **Microsoft Foundry Agent Service**
  - (Без изменений: "Azure OpenAI", "Azure AI Search", "Azure AI Inference" и имена переменных окружения.)
- **Зависимости** ([requirements.txt](../../requirements.txt)):
  - Зафиксированы версии `agent-framework>=1.10.0`, `agent-framework-foundry>=1.10.0`, `agent-framework-openai>=1.10.0`.
  - Зафиксирована версия `openai>=1.108.1` (минимум для Responses API).
  - Удалён пакет `azure-ai-inference` (использовался только в мигрированных примерах GitHub Models).
- **Настройка окружения** ([.env.example](../../.env.example)): удалены переменные GitHub Models (`GITHUB_TOKEN`, `GITHUB_ENDPOINT`, `GITHUB_MODEL_ID`); добавлены `AZURE_OPENAI_ENDPOINT`, `AZURE_OPENAI_DEPLOYMENT` и опционально `AZURE_OPENAI_API_KEY`; обновлено именование на Microsoft Foundry.
- **Документация** — Обновлены [00-course-setup/README.md](./00-course-setup/README.md), [AGENTS.md](./AGENTS.md), [README.md](./README.md) и [STUDY_GUIDE.md](./STUDY_GUIDE.md) для вышеуказанного (установка переменных окружения, проверочный код, руководство по провайдеру, именование).

### Удалено

- Шаги начальной настройки GitHub Models и переменные окружения из документов по установке (заменены Azure OpenAI / Microsoft Foundry).

### Безопасность / Конфиденциальность (очистка при публичном распространении)

- Очищены выводы выполнения Jupyter notebooks, в которых были видны реальные **ID подписки Azure**, имена групп ресурсов / ресурсов и ID подключения Bing, а также **локальные пути к файлам и имена пользователей разработчиков**, в:
  - `08-multi-agent/code_samples/workflows-agent-framework/dotNET/04.dotnet-agent-framework-workflow-aifoundry-condition.ipynb`
  - `08-multi-agent/code_samples/workflows-agent-framework/python/04.python-agent-framework-workflow-aifoundry-condition.ipynb`
  - `15-browser-use/15-browser-user.ipynb`
- Проверено, что в отслеживаемом англоязычном контенте не осталось API-ключей, токенов, ID подписок или личных путей (ссылки на `GITHUB_TOKEN`, которые остались, относятся к токену GitHub Actions в workflow и PAT сервера GitHub MCP в настройке урока 11 — оба легитимны и не связаны с GitHub Models).

### Заметки и известные ограничения

- **Не исполнялось/не компилировалось.** Это образовательные примеры, обновленные для корректности API / именования; они не запускались с реальными ресурсами Azure, а примеры .NET не компилировались в этой среде. Проверяйте на своей развернутой среде Microsoft Foundry / Azure OpenAI.
- **Развернутый модельный деплоймент должен поддерживать Responses API.** Используйте деплойменты, такие как `gpt-4.1-mini`, `gpt-4.1` или модель `gpt-5.x`. Старые модели поддерживают основные функции Responses, но не все возможности.
- **Версия agent-framework.** Примеры ориентированы на последнюю версию MAF (`>=1.10.0`). Канонический вызов создания агента — `client.as_agent(...)`; API сверены с опубликованной документацией фреймворка и установленной сборкой. Если зафиксируете другую версию, проверьте наличие методов (`as_agent` vs `create_agent`).
- **В workflow notebook урока 08, номер 04** намеренно сохраняется `AzureAIAgentClient` (из `agent-framework-azure-ai`), потому что он использует инструменты Microsoft Foundry Agent Service (привязка к Bing, интерпретатор кода); он уже основан на Responses.
- **Стандартное развертывание .NET.** Два workflow примера урока 08 на dotNET ранее жёстко задавали конкретную модель; сейчас они по умолчанию используют `AZURE_OPENAI_DEPLOYMENT` (`gpt-4.1-mini`). Если пример требует мультимодальный/визуальный ввод, установите для `AZURE_OPENAI_DEPLOYMENT` подходящую модель.
- **Foundry Local** предоставляет совместимую с OpenAI конечную точку **Chat Completions** и предназначен для локальной разработки; для полного функционала Responses API используйте Azure OpenAI / Microsoft Foundry.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Отказ от ответственности**:
Этот документ был переведен с использованием сервиса машинного перевода [Co-op Translator](https://github.com/Azure/co-op-translator). Несмотря на наши усилия по обеспечению точности, имейте в виду, что автоматический перевод может содержать ошибки или неточности. Оригинальный документ на его исходном языке следует считать авторитетным источником. Для получения критически важной информации рекомендуется обратиться к профессиональному человеческому переводу. Мы не несем ответственности за любые недоразумения или неправильные толкования, возникшие в результате использования этого перевода.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->