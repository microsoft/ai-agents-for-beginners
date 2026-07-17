# Журнал изменений

Все заметные изменения в курсе **AI Agents for Beginners** задокументированы в этом файле.

## [Выпущено] — 2026-07-13

В этом выпуске добавлены два новых урока, завершающих цикл развертывания — масштабирование агентов до Microsoft Foundry и уменьшение до одной рабочей станции — а также пайплайн для дымового тестирования, обновленная навигация по курсу, новые навыки для обучающихся и обновленный брендинг.

### Добавлено

- **Урок 16 — Развертывание масштабируемых агентов с помощью Microsoft Foundry.** Новый урок [16-deploying-scalable-agents/README.md](./16-deploying-scalable-agents/README.md) и исполняемый блокнот [16-python-agent-framework.ipynb](./16-deploying-scalable-agents/code_samples/16-python-agent-framework.ipynb), создающий продакшен-агента поддержки клиентов (инструменты, RAG, память, маршрутизация моделей, кеширование ответов, одобрение человеком, шлюз оценки и трассировка OpenTelemetry), c диаграммами развития/развертывания/исполнения Mermaid, проверкой знаний, заданием и челленджем.
- **Урок 17 — Создание локальных AI-агентов с Foundry Local и Qwen.** Новый урок [17-creating-local-ai-agents/README.md](./17-creating-local-ai-agents/README.md) и блокнот [17-local-agent-foundry-local.ipynb](./17-creating-local-ai-agents/code_samples/17-local-agent-foundry-local.ipynb), создающий полностью локального инженерного помощника (вызов функций Qwen через Foundry Local, песочница для файловых инструментов, локальный RAG с Chroma, опциональный локальный MCP), с диаграммами только для локального / локального-RAG / вызова инструментов, проверкой знаний, заданием и челленджем.
- **Пайплайн дымового тестирования.** Новый workflow [AI Smoke Test](https://github.com/marketplace/actions/ai-smoke-test) [.github/workflows/smoke-test.yml](../../.github/workflows/smoke-test.yml) плюс каталоги по урокам в [tests/](./tests/README.md) для развертываемых агентов в Уроках 01, 04, 05 и 16, с индексным README, связывающим каждый каталог с уроком и именем размещенного агента. Урок 16 получил раздел "Проверка развернутого агента с помощью дымовых тестов"; уроки 01/04/05 получили опциональную ссылку на дымовое тестирование.
- **Навыки обучающихся.** Новые навыки агента в `.agents/skills/`: [deploying-scalable-agents](./.agents/skills/deploying-scalable-agents/SKILL.md), [local-ai-agents](./.agents/skills/local-ai-agents/SKILL.md) (содержащие рекомендации из Уроков 16 и 17) и [testing-course-samples](./.agents/skills/testing-course-samples/SKILL.md) (о том, как валидировать примеры ноутбуков на живой установке Microsoft Foundry / Azure OpenAI).
- **Запуск валидации блокнотов.** Новый скрипт [scripts/validate-notebooks.ps1](../../scripts/validate-notebooks.ps1), который безголово выполняет каждый Python-блокнот с помощью `nbconvert` и выводит матрицу ПРОШЕЛ/НЕ ПРОШЕЛ (плюс `results.json`). Автоматически определяет корень репозитория и Python, по умолчанию исключает некурсовые блокноты (`.venv`, `site-packages`, `translations`, ассеты шаблона навыков) и `.NET` блокноты, поддерживает параметры `-Filter`, `-Timeout`, `-List`, `-IncludeDotnet` и `-Python`.
- **Навигация по курсу.** Добавлены ссылки на предыдущий/следующий уроки для уроков 11–15 (которые раньше отсутствовали), так что весь курс упорядочен цепочкой 00 → 18 в обе стороны.
- **Новые миниатюры.** Миниатюры уроков для уроков 16 и 17, а также обновленное социальное изображение репозитория [images/repo-thumbnailv3.png](./images/repo-thumbnailv3.png) (теперь рекламирует два новых урока и URL `aka.ms/ai-agents-beginners`).
- **Зависимости** ([requirements.txt](../../requirements.txt)): добавлены `foundry-local-sdk` и `chromadb` для урока 17.

### Изменено

- **Основная таблица уроков в [README.md](./README.md):** уроки 16 и 17 теперь ссылаются на свой контент (ранее "Скоро будет"); изображение репозитория обновлено на `repo-thumbnailv3.png`.
- **[STUDY_GUIDE.md](./STUDY_GUIDE.md):** добавлены уроки 16 и 17 в руководство по урокам и учебным маршрутам, а также раздел "Проверка развернутых агентов дымовыми тестами".
- **[AGENTS.md](./AGENTS.md):** обновлено количество и описание уроков (00–18), добавлен раздел валидации дымового тестирования, добавлены примеры именования для уроков 16/17.
- **[18-securing-ai-agents/README.md](./18-securing-ai-agents/README.md):** "Предыдущий урок" теперь указывает на урок 17 (раньше был урок 15), замыкая цепочку.
- **Стандартизация ссылок на модели без устаревших.** Заменены все упоминания `gpt-4o` / `gpt-4o-mini` по всему курсу (документы, `.env.example`, Python/.NET блокноты и примеры) на `gpt-4.1-mini` — `gpt-4o` (все версии) выводится из эксплуатации в 2026 году. В примере маршрутизации моделей в уроке 16 сохраняется контраст между маленькой и большой моделью с использованием `gpt-4.1-mini` (маленькая) и `gpt-4.1` (большая). Python-блокноты теперь выбирают модель из переменных окружения (`AZURE_AI_MODEL_DEPLOYMENT_NAME` / `AZURE_OPENAI_DEPLOYMENT`) вместо жестко заданного имени модели.

### Примечания и известные ограничения

- **Не выполнено на живом Azure.** Ноутбуки новых уроков являются образовательными примерами; запускайте и проверяйте их на собственной установке Microsoft Foundry / Foundry Local. Для workflow дымового тестирования требуется развернуть агента урока и настроить секреты Azure OIDC (`AZURE_CLIENT_ID`, `AZURE_TENANT_ID`, `AZURE_SUBSCRIPTION_ID`) с ролью **Azure AI User** в области проекта Foundry.
- **Урок 17 только локальный.** У него нет конечной точки Foundry Responses, поэтому действие дымового тестирования не применяется; проверьте его, запустив блокнот на своей рабочей станции.

## [Выпущено] — 2026-07-06

В этом выпуске курс мигрирован на **Azure OpenAI Responses API**, стандартизированы наименования продукта как **Microsoft Foundry** и **Microsoft Agent Framework (MAF)**, сняты с поддержки GitHub Models, обновлены версии SDK и добавлено новое содержимое по локальным моделям и хостингу других фреймворков на Foundry.

### Добавлено

- **Навык миграции** — установлен агент-навык [`azure-openai-to-responses`](./.agents/skills/azure-openai-to-responses/SKILL.md) (из [Azure-Samples/azure-openai-to-responses](https://github.com/Azure-Samples/azure-openai-to-responses)) в `.agents/skills/`, включая ссылки и скрипт сканирования.
- **Foundry Local (запуск моделей на устройстве)** — новый раздел "Альтернативный провайдер: Foundry Local" в [00-course-setup/README.md](./00-course-setup/README.md), охватывающий установку (`winget` / `brew`), `foundry model run`, `foundry-local-sdk` и интеграцию `FoundryLocalManager` с Microsoft Agent Framework через `OpenAIChatClient`.
- **Хостинг агентов LangChain / LangGraph на Microsoft Foundry** — новый раздел в [14-microsoft-agent-framework/README.md](./14-microsoft-agent-framework/README.md), плюс исполняемый пример [14-langchain-hosted-agent.py](../../14-microsoft-agent-framework/code-samples/14-langchain-hosted-agent.py) с использованием `langchain-azure-ai[hosting]` и `ResponsesHostServer` (протокол `/responses`), основанный на [Microsoft Learn](https://learn.microsoft.com/azure/foundry/how-to/develop/langchain-hosted-agents).
- **Microsoft Project Opal** — новый раздел "Пример из реального мира: Microsoft Project Opal" в [15-browser-use/README.md](./15-browser-use/README.md), представляющий Opal как корпоративного агента по использованию компьютера и связывающий его с концепциями курса (человек в петле, доверие/безопасность, планирование, навыки).
- **Второй Python-пример для Урока 02** — добавлен [02-python-agent-framework-azure-openai.ipynb](./02-explore-agentic-frameworks/code_samples/02-python-agent-framework-azure-openai.ipynb) (см. "Изменено" — мигрировано с прежнего Semantic Kernel блокнота) и линкирован в README урока.
- Добавлен раздел "Модели и провайдеры" в [STUDY_GUIDE.md](./STUDY_GUIDE.md).

### Изменено

- **Chat Completions → Responses API (Python).** Примеры, которые напрямую вызывали модель, мигрированы с Chat Completions на Responses API (`client.responses.create(input=..., store=False)`, `resp.output_text`), используя клиент `OpenAI` для стабильного Azure OpenAI `/openai/v1/` эндпоинта (без `api_version`). Затронутые примеры:
  - [06-building-trustworthy-agents/code_samples/06-system-message-framework.ipynb](./06-building-trustworthy-agents/code_samples/06-system-message-framework.ipynb)
  - [06-building-trustworthy-agents/code_samples/06-human-in-the-loop.ipynb](./06-building-trustworthy-agents/code_samples/06-human-in-the-loop.ipynb)
  - [04-tool-use/README.md](./04-tool-use/README.md) — полный разбор функции вызова (схема инструмента преобразована в формат Responses, результаты инструмента возвращаются как `function_call_output`, `max_output_tokens` и др.).
- **GitHub Models → Azure OpenAI.** GitHub Models устарел (выводится из эксплуатации **в июле 2026**) и не поддерживает Responses API. Все кодовые пути GitHub Models были конвертированы в Azure OpenAI / Microsoft Foundry в примерах Python и .NET:
  - Python: блокноты рабочего процесса урока 08 (`01`–`03`), урок 14 (`14-handoff`, `14-human-loop`, `hotel_booking_workflow_sample.py`).
  - .NET: `01`–`04`, `07`, `08` `*-dotnet-agent-framework.cs` + сопутствующая документация `.md`, а также блокноты/`.md` рабочего процесса урока 08 дотнет (`01`–`03`) теперь используют `AzureOpenAIClient(...).GetOpenAIResponseClient(deployment).CreateAIAgent(...)` с `AzureCliCredential`.
- **Semantic Kernel → Microsoft Agent Framework.** Прежний `02-semantic-kernel.ipynb` был переписан на использование Microsoft Agent Framework с Azure OpenAI (Responses API) и переименован в `02-python-agent-framework-azure-openai.ipynb`.
- **Стандартизация на `FoundryChatClient` + `as_agent`.** README и код в блокнотах, которые ссылались на `AzureAIProjectAgentProvider`, стандартизированы на канонический паттерн, используемый в уроке 01 и собственных примерах фреймворка: `FoundryChatClient(project_endpoint=..., model=..., credential=AzureCliCredential())` с `provider.as_agent(...)`. Обновлено по урокам 02–14 в README и блокнотах (например, память в уроке 13, все блокноты урока 14, `11-agentic-protocols/code_samples/github-mcp/app.py`).
- **Наименование продукта.** Переименовано по всему англоязычному контенту:
  - "Azure AI Foundry" / "Azure AI Studio" → **Microsoft Foundry**
  - "Azure AI Agent Service" → **Microsoft Foundry Agent Service**
  - (Без изменений: "Azure OpenAI", "Azure AI Search", "Azure AI Inference" и переменные окружения.)
- **Зависимости** ([requirements.txt](../../requirements.txt)):
  - Зафиксированы версии `agent-framework>=1.10.0`, `agent-framework-foundry>=1.10.0`, `agent-framework-openai>=1.10.0`.
  - Зафиксирована версия `openai>=1.108.1` (минимум для Responses API).
  - Удален пакет `azure-ai-inference` (был лишь в примерах с миграцией GitHub Models).
- **Конфигурация окружения** ([.env.example](../../.env.example)): удалены переменные GitHub Models (`GITHUB_TOKEN`, `GITHUB_ENDPOINT`, `GITHUB_MODEL_ID`); добавлены `AZURE_OPENAI_ENDPOINT`, `AZURE_OPENAI_DEPLOYMENT` и опциональный `AZURE_OPENAI_API_KEY`; обновлены именования для Microsoft Foundry.
- **Документация** — обновлены [00-course-setup/README.md](./00-course-setup/README.md), [AGENTS.md](./AGENTS.md), [README.md](./README.md) и [STUDY_GUIDE.md](./STUDY_GUIDE.md) для вышеуказанного (переменные окружения настройки, сниппет проверки, рекомендации по провайдеру, наименования).

### Удалено

- Шаги подключения GitHub Models и переменные окружения удалены из документации по настройке (заменены Azure OpenAI / Microsoft Foundry).

### Безопасность / Конфиденциальность (очистка публичных данных)

- Очищены выводы выполнения блокнотов Jupyter, которые содержали реальные **ID подписки Azure**, имена групп ресурсов/ресурсов и ID подключения Bing, а также локальные пути файлов и имена пользователей разработчиков в:
  - `08-multi-agent/code_samples/workflows-agent-framework/dotNET/04.dotnet-agent-framework-workflow-aifoundry-condition.ipynb`

  - `08-multi-agent/code_samples/workflows-agent-framework/python/04.python-agent-framework-workflow-aifoundry-condition.ipynb`
  - `15-browser-use/15-browser-user.ipynb`
- Проверено, что в отслеживаемом английском содержимом не осталось ключей API, токенов, идентификаторов подписок или личных путей (упоминания `GITHUB_TOKEN` — это токен GitHub Actions в workflow и PAT сервера GitHub MCP в настройке Урока 11 — оба легитимны и не связаны с моделями GitHub).

### Заметки и известные ограничения

- **Не выполнялись/не компилировались.** Это учебные примеры, обновленные для корректности API/имен; они не запускались на живых ресурсах Azure, а .NET-примеры не компилировались в этой среде. Проверяйте их на собственной среде Microsoft Foundry / Azure OpenAI.
- **Развертывание модели должно поддерживать Responses API.** Используйте развертывание вроде `gpt-4.1-mini`, `gpt-4.1` или модели `gpt-5.x`. Старые модели поддерживают базовый функционал Responses, но не все возможности.
- **Версия agent-framework.** Примеры рассчитаны на последнюю версию MAF (`>=1.10.0`). Каноничный вызов создания агента — `client.as_agent(...)`; API проверялись согласно опубликованной документации фреймворка и установленной сборке. Если используете другую версию, проверьте доступность метода (`as_agent` против `create_agent`).
- **Блокнот урока 08 workflow 04** целенаправленно сохраняет `AzureAIAgentClient` (из `agent-framework-azure-ai`), так как он использует инструменты Microsoft Foundry Agent Service (основание на Bing, интерпретатор кода); он уже основан на Responses.
- **Развертывание по умолчанию для .NET.** Два примера dotNET из урока 08 ранее жестко задавали конкретную модель; теперь по умолчанию используется `AZURE_OPENAI_DEPLOYMENT` (`gpt-4.1-mini`). Если пример использует мультимодальный/визуальный ввод, установите `AZURE_OPENAI_DEPLOYMENT` в подходящую модель.
- **Foundry Local** предоставляет совместимую с OpenAI конечную точку **Chat Completions** и предназначен для локальной разработки; для полного набора функций Responses API используйте Azure OpenAI / Microsoft Foundry.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Отказ от ответственности**:
Этот документ был переведен с использованием сервиса машинного перевода [Co-op Translator](https://github.com/Azure/co-op-translator). Несмотря на наши усилия по обеспечению точности, имейте в виду, что автоматический перевод может содержать ошибки или неточности. Оригинальный документ на его исходном языке следует считать авторитетным источником. Для получения критически важной информации рекомендуется обратиться к профессиональному человеческому переводу. Мы не несем ответственности за любые недоразумения или неправильные толкования, возникшие в результате использования этого перевода.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->