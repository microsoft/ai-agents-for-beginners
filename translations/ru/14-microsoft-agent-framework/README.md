# Исследование Microsoft Agent Framework

![Agent Framework](../../../translated_images/ru/lesson-14-thumbnail.90df0065b9d234ee.webp)

### Введение

В этом уроке будут рассмотрены:

- Понимание Microsoft Agent Framework: ключевые особенности и ценность  
- Изучение основных концепций Microsoft Agent Framework
- Продвинутые паттерны MAF: рабочие процессы, промежуточное ПО и память

## Цели обучения

После прохождения этого урока вы узнаете, как:

- Создавать готовых к промышленному использованию AI Агентов с использованием Microsoft Agent Framework
- Применять основные функции Microsoft Agent Framework для ваших агентских случаев использования
- Использовать продвинутые паттерны, включая рабочие процессы, промежуточное ПО и наблюдаемость

## Примеры кода 

Примеры кода для [Microsoft Agent Framework (MAF)](https://learn.microsoft.com/en-us/agent-framework/overview/?wt.mc_id=youtube_26688_organicsocial_reactor&pivots=programming-language-python) можно найти в этом репозитории в файлах `xx-python-agent-framework` и `xx-dotnet-agent-framework`.

## Понимание Microsoft Agent Framework

![Framework Intro](../../../translated_images/ru/framework-intro.077af16617cf130c.webp)

[Microsoft Agent Framework (MAF)](https://learn.microsoft.com/en-us/agent-framework/overview/?wt.mc_id=youtube_26688_organicsocial_reactor&pivots=programming-language-python) — это унифицированный фреймворк Microsoft для создания AI агентов. Он предлагает гибкость для решения широкого спектра агентских задач, встречающихся как в промышленной эксплуатации, так и в исследовательской среде, включая:

- **Последовательную оркестровку агентов** в сценариях, где необходимы пошаговые рабочие процессы.
- **Параллельную оркестровку** в сценариях, где агенты должны выполнять задачи одновременно.
- **Оркестровку группового чата** в сценариях, где агенты могут совместно работать над одной задачей.
- **Оркестровку передачи задач** в сценариях, где агенты передают задачи друг другу по мере выполнения подзадач.
- **Магнитную оркестровку** в сценариях, где управляющий агент создает и изменяет список задач и координирует подагентов для их выполнения.

Для развертывания AI Агентов в промышленной эксплуатации MAF также включает функции для:

- **Наблюдаемости** через использование OpenTelemetry, где фиксируются каждое действие AI Агента, включая вызов инструментов, шаги оркестровки, логические потоки и мониторинг производительности через панели мониторинга Microsoft Foundry.
- **Безопасности** за счет размещения агентов непосредственно на Microsoft Foundry, что включает в себя контроль доступа на основе ролей, обработку приватных данных и встроенную безопасность содержимого.
- **Надежности**, так как потоки и рабочие процессы агента могут приостанавливаться, возобновляться и восстанавливаться после ошибок, что позволяет запускать более длинные процессы.
- **Контроля**, поскольку поддерживаются рабочие процессы с участием человека, где задачи отмечаются как требующие одобрения человеком.

Microsoft Agent Framework также ориентирован на совместимость благодаря:

- **Независимости от облака** — агенты могут запускаться в контейнерах, локально и в различных облаках.
- **Независимости от провайдера** — агенты могут создаваться с использованием вашего предпочтительного SDK, включая Azure OpenAI и OpenAI
- **Интеграции с открытыми стандартами** — агенты могут использовать протоколы, такие как Agent-to-Agent (A2A) и Model Context Protocol (MCP), для обнаружения и использования других агентов и инструментов.
- **Плагинах и коннекторах** — могут подключаться сервисы данных и памяти, такие как Microsoft Fabric, SharePoint, Pinecone и Qdrant.

Давайте рассмотрим, как эти функции применяются к основным концепциям Microsoft Agent Framework.

## Основные концепции Microsoft Agent Framework

### Агенты

![Agent Framework](../../../translated_images/ru/agent-components.410a06daf87b4fef.webp)

**Создание Агентов**

Создание агента происходит путём определения сервиса вывода (LLM-провайдера),  
набора инструкций для выполнения AI Агентом и присвоенного `имени`:

```python
agent = AzureOpenAIChatClient(credential=AzureCliCredential()).create_agent( instructions="You are good at recommending trips to customers based on their preferences.", name="TripRecommender" )
```

Пример выше использует `Azure OpenAI`, но агенты могут быть созданы с помощью различных сервисов, включая `Microsoft Foundry Agent Service`:

```python
AzureAIAgentClient(async_credential=credential).create_agent( name="HelperAgent", instructions="You are a helpful assistant." ) as agent
```

OpenAI API для `Responses`, `ChatCompletion`

```python
agent = OpenAIResponsesClient().create_agent( name="WeatherBot", instructions="You are a helpful weather assistant.", )
```

```python
agent = OpenAIChatClient().create_agent( name="HelpfulAssistant", instructions="You are a helpful assistant.", )
```

или [MiniMax](https://platform.minimaxi.com/), который предоставляет совместимый с OpenAI API с большими окнами контекста (до 204K токенов):

```python
agent = OpenAIChatClient(base_url="https://api.minimax.io/v1", api_key=os.environ["MINIMAX_API_KEY"], model_id="MiniMax-M3").create_agent( name="HelpfulAssistant", instructions="You are a helpful assistant.", )
```

или удалённые агенты с использованием протокола A2A:

```python
agent = A2AAgent( name=agent_card.name, description=agent_card.description, agent_card=agent_card, url="https://your-a2a-agent-host" )
```

**Запуск Агентов**

Агенты запускаются с помощью методов `.run` или `.run_stream` для получения ответов без потока или с потоком.

```python
result = await agent.run("What are good places to visit in Amsterdam?")
print(result.text)
```

```python
async for update in agent.run_stream("What are the good places to visit in Amsterdam?"):
    if update.text:
        print(update.text, end="", flush=True)

```

У каждого запуска агента также могут быть параметры для настройки таких параметров, как `max_tokens`, используемых агентом, `tools` — инструментов, которые агент может вызвать, и даже самого `модели`, используемой агентом.

Это полезно в случаях, когда для выполнения задачи пользователя требуются определённые модели или инструменты.

**Инструменты**

Инструменты могут быть определены как при создании агента:

```python
def get_attractions( location: Annotated[str, Field(description="The location to get the top tourist attractions for")], ) -> str: """Get the top tourist attractions for a given location.""" return f"The top attractions for {location} are." 


# При создании ChatAgent напрямую

agent = ChatAgent( chat_client=OpenAIChatClient(), instructions="You are a helpful assistant", tools=[get_attractions]

```

так и при запуске агента:

```python

result1 = await agent.run( "What's the best place to visit in Seattle?", tools=[get_attractions] # Инструмент предоставлен только для этого запуска )
```

**Потоки агента**

Потоки агента используются для обработки многошаговых разговоров. Потоки могут создаваться:

- с использованием `get_new_thread()`, что позволяет сохранять поток со временем
- автоматически при запуске агента, и поток действует только в рамках текущего запуска.

Код для создания потока выглядит так:

```python
# Создать новый поток.
thread = agent.get_new_thread() # Запустить агента с потоком.
response = await agent.run("Hello, I am here to help you book travel. Where would you like to go?", thread=thread)

```

Затем поток можно сериализовать для хранения и последующего использования:

```python
# Создать новый поток.
thread = agent.get_new_thread() 

# Запустить агента с потоком.

response = await agent.run("Hello, how are you?", thread=thread) 

# Сериализовать поток для сохранения.

serialized_thread = await thread.serialize() 

# Десериализовать состояние потока после загрузки из хранения.

resumed_thread = await agent.deserialize_thread(serialized_thread)
```

**Промежуточное ПО Агентов**

Агенты взаимодействуют с инструментами и LLM для выполнения задач пользователя. В определённых сценариях мы хотим выполнять действия или отслеживать их между этими взаимодействиями. Промежуточное ПО агентов позволяет это делать через:

*Функциональное промежуточное ПО*

Это промежуточное ПО позволяет выполнить действие между агентом и вызовом функции/инструмента. Пример использования — ведение журнала вызова функции.

В приведённом ниже коде `next` определяет, следует ли вызывать следующее промежуточное ПО или реальную функцию.

```python
async def logging_function_middleware(
    context: FunctionInvocationContext,
    next: Callable[[FunctionInvocationContext], Awaitable[None]],
) -> None:
    """Function middleware that logs function execution."""
    # Предобработка: Логирование перед выполнением функции
    print(f"[Function] Calling {context.function.name}")

    # Продолжить к следующему промежуточному обработчику или выполнению функции
    await next(context)

    # Постобработка: Логирование после выполнения функции
    print(f"[Function] {context.function.name} completed")
```

*Промежуточное ПО чата*

Это промежуточное ПО позволяет выполнять действия или вести журнал между агентом и запросами к LLM.

Здесь содержится важная информация, такая как `messages`, отправляемые в AI сервис.

```python
async def logging_chat_middleware(
    context: ChatContext,
    next: Callable[[ChatContext], Awaitable[None]],
) -> None:
    """Chat middleware that logs AI interactions."""
    # Предобработка: журнал до вызова ИИ
    print(f"[Chat] Sending {len(context.messages)} messages to AI")

    # Продолжить к следующему промежуточному ПО или сервису ИИ
    await next(context)

    # Постобработка: журнал после ответа ИИ
    print("[Chat] AI response received")

```

**Память Агентов**

Как было рассмотрено в уроке `Agentic Memory`, память — важный элемент, позволяющий агенту работать с разными контекстами. MAF предлагает несколько типов памяти:

*Память в памяти (In-Memory Storage)*

Это память, хранящаяся в потоках во время работы приложения.

```python
# Создать новый поток.
thread = agent.get_new_thread() # Запустить агента с этим потоком.
response = await agent.run("Hello, I am here to help you book travel. Where would you like to go?", thread=thread)
```

*Постоянные сообщения*

Эта память используется для сохранения истории разговоров между сессиями. Она определяется с помощью `chat_message_store_factory`:

```python
from agent_framework import ChatMessageStore

# Создать пользовательское хранилище сообщений
def create_message_store():
    return ChatMessageStore()

agent = ChatAgent(
    chat_client=OpenAIChatClient(),
    instructions="You are a Travel assistant.",
    chat_message_store_factory=create_message_store
)

```

*Динамическая память*

Эта память добавляется в контекст до запуска агентов. Такие памяти могут храниться во внешних сервисах, например, mem0:

```python
from agent_framework.mem0 import Mem0Provider

# Использование Mem0 для расширенных возможностей памяти
memory_provider = Mem0Provider(
    api_key="your-mem0-api-key",
    user_id="user_123",
    application_id="my_app"
)

agent = ChatAgent(
    chat_client=OpenAIChatClient(),
    instructions="You are a helpful assistant with memory.",
    context_providers=memory_provider
)

```

**Наблюдаемость Агентов**

Наблюдаемость важна для создания надежных и удобных в обслуживании агентских систем. MAF интегрируется с OpenTelemetry для предоставления трассировки и счётчиков для улучшения наблюдаемости.

```python
from agent_framework.observability import get_tracer, get_meter

tracer = get_tracer()
meter = get_meter()
with tracer.start_as_current_span("my_custom_span"):
    # сделать что-нибудь
    pass
counter = meter.create_counter("my_custom_counter")
counter.add(1, {"key": "value"})
```

### Рабочие процессы

MAF предлагает рабочие процессы — предварительно определённые шаги для выполнения задачи, включающие AI агентов как компоненты этих шагов.

Рабочие процессы состоят из различных компонентов, которые обеспечивают лучшее управление потоком выполнения. Они также позволяют **оркестровку с несколькими агентами** и **контрольные точки** для сохранения состояний рабочих процессов.

Основные компоненты рабочего процесса:

**Исполнители**

Исполнители принимают входящие сообщения, выполняют назначенные задачи и создают выходное сообщение. Это продвигает рабочий процесс вперед к выполнению общей задачи. Исполнителями могут быть как AI агенты, так и пользовательская логика.

**Рёбра**

Рёбра используются для определения потока сообщений в рабочем процессе. Они могут быть:

*Прямые рёбра* — простые связи один-к-одному между исполнителями:

```python
from agent_framework import WorkflowBuilder

builder = WorkflowBuilder()
builder.add_edge(source_executor, target_executor)
builder.set_start_executor(source_executor)
workflow = builder.build()
```

*Условные рёбра* — активируются после выполнения определённого условия. Например, когда номера в отелях недоступны, исполнитель может предложить другие варианты.

*Switch-case рёбра* — направляют сообщения разным исполнителям на основе заданных условий. Например, если у туриста приоритетный доступ, его задачи будут обработаны через другой рабочий процесс.

*Рёбра распространения (Fan-out)* — отправляют одно сообщение нескольким получателям.

*Рёбра сбора (Fan-in)* — собирают несколько сообщений от разных исполнителей и отправляют одному получателю.

**События**

Для улучшения наблюдаемости рабочих процессов MAF предлагает встроенные события выполнения, включая:

- `WorkflowStartedEvent`  — запуск рабочего процесса
- `WorkflowOutputEvent` — рабочий процесс создает результат
- `WorkflowErrorEvent` — рабочий процесс столкнулся с ошибкой
- `ExecutorInvokeEvent`  — исполнитель начал обработку
- `ExecutorCompleteEvent`  — исполнитель завершил обработку
- `RequestInfoEvent` — выполнен запрос

## Продвинутые паттерны MAF

В предыдущих разделах рассмотрены основные концепции Microsoft Agent Framework. При создании более сложных агентов рассмотрите следующие продвинутые паттерны:

- **Композиция промежуточного ПО**: цепочка нескольких обработчиков промежуточного ПО (логирование, аутентификация, ограничение скорости) с использованием функционального и чат-промежуточного ПО для тонкого контроля поведения агента.
- **Контрольные точки рабочего процесса**: используйте события рабочего процесса и сериализацию для сохранения и возобновления длительных процессов агентов.
- **Динамический выбор инструментов**: комбинируйте RAG по описаниям инструментов с регистрацией инструментов в MAF, чтобы показывать только релевантные инструменты на запрос.
- **Передача между несколькими агентами**: используйте рёбра рабочего процесса и условную маршрутизацию для координации передачи между специализированными агентами.

## Размещение агентов LangChain / LangGraph на Microsoft Foundry

Microsoft Agent Framework является **фреймворк-совместимым** — вы не ограничены агентами, написанными с помощью MAF. Если у вас уже есть агент, созданный с **LangChain** или **LangGraph**, вы можете запускать его как **хостинг-агент Foundry**, чтобы Foundry управляла временем выполнения, сессиями, масштабированием, идентификацией и конечными точками протоколов, в то время как логика вашего агента остаётся в LangGraph.

Это реализуется с помощью пакета `langchain_azure_ai.agents.hosting`, который открывает скомпилированный граф LangGraph по тем же протоколам, которые используют агенты Foundry.

**1. Установите пакет hosting extra:**

```bash
pip install -U "langchain-azure-ai[hosting]>=1.2.4" azure-identity
```

Пакет `hosting extra` устанавливает протокольные библиотеки Foundry: `azure-ai-agentserver-responses` (совместимый с OpenAI `/responses` endpoint) и `azure-ai-agentserver-invocations` (универсальный `/invocations` endpoint).

**2. Выберите протокол хостинга:**

| Протокол | Класс хоста | Конечная точка | Используйте, когда |
|----------|-------------|---------------|-------------------|
| **Responses** | `ResponsesHostServer` | `/responses` | Требуется совместимый с OpenAI чат, потоковые ответы, история ответов и нити разговоров — рекомендованный вариант для разговорных агентов. |
| **Invocations** | `InvocationsHostServer` | `/invocations` | Нужно кастомное JSON-форматирование, webhook-стиль endpoint или непереговорная обработка. |

Поскольку **Responses API является основным API для разработки агентов в Foundry**, начните с `ResponsesHostServer` для большинства агентов.

**3. Настройте переменные окружения** (сначала выполните `az login`, чтобы `DefaultAzureCredential` мог аутентифицироваться):

```bash
export FOUNDRY_PROJECT_ENDPOINT="https://<resource>.services.ai.azure.com/api/projects/<project>"
export FOUNDRY_MODEL_NAME="gpt-5-mini"
```

Когда агент запустится как хостинг-агент в Foundry, платформа автоматически добавит `FOUNDRY_PROJECT_ENDPOINT`.

**4. Откройте агент LangGraph по протоколу Responses:**

```python
import os

from azure.ai.projects import AIProjectClient
from azure.identity import DefaultAzureCredential, get_bearer_token_provider
from langchain.agents import create_agent
from langchain_openai import ChatOpenAI
from langchain_azure_ai.agents.hosting import ResponsesHostServer

_AZURE_AI_SCOPE = "https://ai.azure.com/.default"


def build_chat_model() -> ChatOpenAI:
    project_endpoint = os.environ["FOUNDRY_PROJECT_ENDPOINT"].rstrip("/")
    deployment = os.environ.get("FOUNDRY_MODEL_NAME", "gpt-5-mini")
    credential = DefaultAzureCredential()
    project = AIProjectClient(endpoint=project_endpoint, credential=credential)
    openai_client = project.get_openai_client()
    token_provider = get_bearer_token_provider(credential, _AZURE_AI_SCOPE)

    # ChatOpenAI здесь нацелен на совместимую с OpenAI конечную точку (Responses) проекта Foundry.
    return ChatOpenAI(
        model=deployment,
        base_url=str(openai_client.base_url),
        api_key=token_provider,
    )


def main() -> None:
    graph = create_agent(build_chat_model(), tools=[])
    port = int(os.environ.get("PORT", "8088"))
    ResponsesHostServer(graph).run(port=port)


if __name__ == "__main__":
    main()
```

Запустите локально с помощью `python main.py`, затем отправляйте запросы Responses на `http://localhost:8088/responses`.

**Ключевые особенности:**

- **Разговоры**: Клиенты продолжают разговор, передавая `previous_response_id` или ID `conversation`. Если ваш граф скомпилирован с проверкой LangGraph, Foundry связывает состояние переговоров с контрольной точкой (используйте долговременную контрольную точку в продакшене; `MemorySaver` подходит для локального тестирования).
- **Человек в цикле**: Если ваш граф использует LangGraph `interrupt()`, `ResponsesHostServer` отображает ожидающее прерывание как элемент Responses `function_call` / `mcp_approval_request`, а клиенты продолжают с соответствующим `function_call_output` / `mcp_approval_response`.
- **Развертывание в Foundry**: Используйте Azure Developer CLI — `azd ext install azure.ai.agents`, `azd ai agent init -m <manifest>`, `azd ai agent run` (локально, требуется Docker), затем `azd provision` и `azd deploy`. Для развертывания хостинг-агента нужна роль **Foundry Project Manager**.

Рабочий пример находится в [code-samples/14-langchain-hosted-agent.py](../../../14-microsoft-agent-framework/code-samples/14-langchain-hosted-agent.py). Полное руководство (протокол Invocations, кастомные схемы запросов, и устранение проблем) смотрите здесь [Host LangGraph agents as Foundry hosted agents](https://learn.microsoft.com/azure/foundry/how-to/develop/langchain-hosted-agents).

## Примеры кода 

Примеры кода для Microsoft Agent Framework можно найти в этом репозитории в файлах `xx-python-agent-framework` и `xx-dotnet-agent-framework`.

## Есть вопросы по Microsoft Agent Framework?

Присоединяйтесь к [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D), чтобы встретиться с другими учащимися, посетить часы консультаций и получить ответы на вопросы по AI Агентам.
## Предыдущий урок

[Память для AI Агентов](../13-agent-memory/README.md)

## Следующий урок

[Создание агентов для использования компьютера (CUA)](../15-browser-use/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Отказ от ответственности**:
Этот документ был переведен с использованием сервиса машинного перевода [Co-op Translator](https://github.com/Azure/co-op-translator). Несмотря на наши усилия по обеспечению точности, имейте в виду, что автоматический перевод может содержать ошибки или неточности. Оригинальный документ на его исходном языке следует считать авторитетным источником. Для получения критически важной информации рекомендуется обратиться к профессиональному человеческому переводу. Мы не несем ответственности за любые недоразумения или неправильные толкования, возникшие в результате использования этого перевода.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->