# Изучение Microsoft Agent Framework

![Agent Framework](../../../translated_images/ru/lesson-14-thumbnail.90df0065b9d234ee.webp)

### Введение

В этом уроке будут рассмотрены:

- Понимание Microsoft Agent Framework: ключевые особенности и ценность  
- Изучение основных концепций Microsoft Agent Framework
- Расширенные паттерны MAF: рабочие процессы, промежуточное ПО и память

## Цели обучения

После завершения этого урока вы сможете:

- Создавать готовых к производству ИИ-агентов с использованием Microsoft Agent Framework
- Применять основные функции Microsoft Agent Framework для ваших агентских сценариев использования
- Использовать расширенные паттерны, включая рабочие процессы, промежуточное ПО и наблюдаемость

## Примеры кода 

Примеры кода для [Microsoft Agent Framework (MAF)](https://aka.ms/ai-agents-beginners/agent-framework) можно найти в этом репозитории в файлах `xx-python-agent-framework` и `xx-dotnet-agent-framework`.

## Понимание Microsoft Agent Framework

![Framework Intro](../../../translated_images/ru/framework-intro.077af16617cf130c.webp)

[Microsoft Agent Framework (MAF)](https://aka.ms/ai-agents-beginners/agent-framework) — это единая платформа Microsoft для создания ИИ-агентов. Она предлагает гибкость для решения широкого спектра агентских сценариев, встречающихся как в производственной среде, так и в научных исследованиях, включая:

- **Последовательная оркестрация агентов** в сценариях, где требуются пошаговые рабочие процессы.
- **Параллельная оркестрация** в случаях, когда агенты должны выполнять задачи одновременно.
- **Оркестрация группового чата** в сценариях, когда агенты могут совместно работать над одной задачей.
- **Оркестрация передачи задач** в сценариях, когда агенты передают задачи друг другу по мере выполнения подзадач.
- **Магнитная оркестрация** в сценариях, когда менеджер-агент создаёт и изменяет список задач и координирует подагентов для выполнения задачи.

Для внедрения ИИ-агентов в производство MAF также включает функции:

- **Наблюдаемость** с использованием OpenTelemetry, где фиксируется каждое действие ИИ-агента, включая вызовы инструментов, этапы оркестрации, логические выводы и мониторинг производительности с помощью панелей Microsoft Foundry.
- **Безопасность** за счёт хостинга агентов напрямую на Microsoft Foundry, который включает меры контроля безопасности, такие как разграничение доступа по ролям, обработка конфиденциальных данных и встроенная безопасность контента.
- **Устойчивость** — потоки и рабочие процессы агентов могут приостанавливаться, возобновляться и восстанавливаться после ошибок, что позволяет запускать длительные процессы.
- **Контроль** — поддерживаются рабочие процессы с участием человека, где задачи помечаются как требующие одобрения человеком.

Microsoft Agent Framework также ориентирован на обеспечение совместимости:

- **Независимость от облака** — агенты могут работать в контейнерах, локально и на разных облачных платформах.
- **Независимость от провайдера** — агенты могут создаваться с использованием предпочитаемых SDK, включая Azure OpenAI и OpenAI.
- **Интеграция открытых стандартов** — агенты могут использовать протоколы, такие как Agent-to-Agent (A2A) и Model Context Protocol (MCP), для обнаружения и использования других агентов и инструментов.
- **Плагины и коннекторы** — возможны подключения к сервисам данных и памяти, таким как Microsoft Fabric, SharePoint, Pinecone и Qdrant.

Рассмотрим, как эти функции применяются к основным концепциям Microsoft Agent Framework.

## Ключевые концепции Microsoft Agent Framework

### Агенты

![Agent Framework](../../../translated_images/ru/agent-components.410a06daf87b4fef.webp)

**Создание агентов**

Создание агента осуществляется путём определения службы вывода (поставщика LLM),
набора инструкций для выполнения ИИ-агентом и присвоения `name`:

```python
agent = AzureOpenAIChatClient(credential=AzureCliCredential()).create_agent( instructions="You are good at recommending trips to customers based on their preferences.", name="TripRecommender" )
```

В приведённом примере используется `Azure OpenAI`, но агенты могут создаваться с использованием различных служб, включая `Microsoft Foundry Agent Service`:

```python
AzureAIAgentClient(async_credential=credential).create_agent( name="HelperAgent", instructions="You are a helpful assistant." ) as agent
```

OpenAI API `Responses`, `ChatCompletion`

```python
agent = OpenAIResponsesClient().create_agent( name="WeatherBot", instructions="You are a helpful weather assistant.", )
```

```python
agent = OpenAIChatClient().create_agent( name="HelpfulAssistant", instructions="You are a helpful assistant.", )
```

или [MiniMax](https://platform.minimaxi.com/), который предоставляет совместимый с OpenAI API с большими контекстными окнами (до 204K токенов):

```python
agent = OpenAIChatClient(base_url="https://api.minimax.io/v1", api_key=os.environ["MINIMAX_API_KEY"], model_id="MiniMax-M3").create_agent( name="HelpfulAssistant", instructions="You are a helpful assistant.", )
```

или удалённые агенты с использованием протокола A2A:

```python
agent = A2AAgent( name=agent_card.name, description=agent_card.description, agent_card=agent_card, url="https://your-a2a-agent-host" )
```

**Запуск агентов**

Агенты запускаются с помощью методов `.run` или `.run_stream` для получения либо неряделённых, либо потоковых ответов.

```python
result = await agent.run("What are good places to visit in Amsterdam?")
print(result.text)
```

```python
async for update in agent.run_stream("What are the good places to visit in Amsterdam?"):
    if update.text:
        print(update.text, end="", flush=True)

```

Каждый запуск агента может иметь параметры для настройки, такие как `max_tokens` для ограничения числа токенов, `tools` — инструменты, доступные агенту, и даже используемая `model`.

Это полезно, когда для выполнения задачи пользователя требуются конкретные модели или инструменты.

**Инструменты**

Инструменты можно определять как при создании агента:

```python
def get_attractions( location: Annotated[str, Field(description="The location to get the top tourist attractions for")], ) -> str: """Get the top tourist attractions for a given location.""" return f"The top attractions for {location} are." 


# При прямом создании ChatAgent

agent = ChatAgent( chat_client=OpenAIChatClient(), instructions="You are a helpful assistant", tools=[get_attractions]

```

так и при запуске агента:

```python

result1 = await agent.run( "What's the best place to visit in Seattle?", tools=[get_attractions] # Инструмент предоставлен только для этого запуска )
```

**Потоки агентов**

Потоки агентов используются для обработки многоходовых диалогов. Потоки могут создаваться:

- Используя `get_new_thread()`, что позволяет сохранить поток с течением времени
- Автоматически при запуске агента, где поток длится только во время текущего запуска.

Для создания потока код выглядит так:

```python
# Создать новый поток.
thread = agent.get_new_thread() # Запустить агента с этим потоком.
response = await agent.run("Hello, I am here to help you book travel. Where would you like to go?", thread=thread)

```

Поток можно сериализовать и сохранить для последующего использования:

```python
# Создать новый поток.
thread = agent.get_new_thread() 

# Запустить агента с потоком.

response = await agent.run("Hello, how are you?", thread=thread) 

# Сериализовать поток для хранения.

serialized_thread = await thread.serialize() 

# Десериализовать состояние потока после загрузки из хранилища.

resumed_thread = await agent.deserialize_thread(serialized_thread)
```

**Промежуточное ПО агента**

Агенты взаимодействуют с инструментами и LLM для выполнения задач пользователя. В некоторых сценариях мы хотим выполнять действия или отслеживать события между этими взаимодействиями. Промежуточное ПО агента позволяет это сделать следующим образом:

*Функциональное промежуточное ПО*

Это промежуточное ПО позволяет выполнять действия между агентом и функцией/инструментом, которые вызываются. Пример — логирование вызова функции.

В коде ниже `next` определяет, вызывается ли следующее промежуточное ПО или сама функция.

```python
async def logging_function_middleware(
    context: FunctionInvocationContext,
    next: Callable[[FunctionInvocationContext], Awaitable[None]],
) -> None:
    """Function middleware that logs function execution."""
    # Предобработка: Логирование перед выполнением функции
    print(f"[Function] Calling {context.function.name}")

    # Продолжить к следующему промежуточному ПО или выполнению функции
    await next(context)

    # Постобработка: Логирование после выполнения функции
    print(f"[Function] {context.function.name} completed")
```

*Промежуточное ПО чата*

Это промежуточное ПО позволяет выполнять действия или логировать запросы между агентом и LLM.

Оно содержит важную информацию, такую как `messages`, отправляемые в AI-сервис.

```python
async def logging_chat_middleware(
    context: ChatContext,
    next: Callable[[ChatContext], Awaitable[None]],
) -> None:
    """Chat middleware that logs AI interactions."""
    # Предварительная обработка: логирование перед вызовом ИИ
    print(f"[Chat] Sending {len(context.messages)} messages to AI")

    # Продолжить к следующему промежуточному ПО или AI-сервису
    await next(context)

    # Последующая обработка: логирование после ответа ИИ
    print("[Chat] AI response received")

```

**Память агента**

Как описано в уроке `Agentic Memory`, память — важный элемент, позволяющий агенту работать в разных контекстах. MAF предлагает несколько типов памяти:

*В оперативной памяти (In-Memory Storage)*

Эта память хранится в потоках во время выполнения приложения.

```python
# Создайте новый поток.
thread = agent.get_new_thread() # Запустите агента с этим потоком.
response = await agent.run("Hello, I am here to help you book travel. Where would you like to go?", thread=thread)
```

*Постоянные сообщения (Persistent Messages)*

Эта память используется для хранения истории общения между сессиями. Она определяется с помощью `chat_message_store_factory`:

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

*Динамическая память (Dynamic Memory)*

Эта память добавляется к контексту перед запуском агентов. Она может храниться во внешних сервисах, таких как mem0:

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

**Наблюдаемость агента**

Наблюдаемость важна для создания надёжных и удобных в сопровождении агентских систем. MAF интегрируется с OpenTelemetry для трассировки и метрик, что улучшает наблюдаемость.

```python
from agent_framework.observability import get_tracer, get_meter

tracer = get_tracer()
meter = get_meter()
with tracer.start_as_current_span("my_custom_span"):
    # сделать что-то
    pass
counter = meter.create_counter("my_custom_counter")
counter.add(1, {"key": "value"})
```

### Рабочие процессы

MAF предлагает рабочие процессы — предопределённые шаги для выполнения задачи, включающие ИИ-агентов в качестве компонентов.

Рабочие процессы состоят из различных компонентов, обеспечивающих лучший контроль потока. Они также поддерживают **оркестрацию нескольких агентов** и **контрольные точки** для сохранения состояний рабочих процессов.

Основные компоненты рабочего процесса:

**Исполнители (Executors)**

Исполнители получают входящие сообщения, выполняют назначенные задачи и затем создают выходящее сообщение. Это продвигает рабочий процесс к выполнению основной задачи. Исполнителем может быть ИИ-агент или индивидуальная логика.

**Ребра (Edges)**

Ребра определяют поток сообщений в рабочем процессе. Они бывают:

*Прямые ребра* — простые однонаправленные соединения между исполнителями:

```python
from agent_framework import WorkflowBuilder

builder = WorkflowBuilder()
builder.add_edge(source_executor, target_executor)
builder.set_start_executor(source_executor)
workflow = builder.build()
```

*Условные ребра* — активируются при выполнении определённого условия. Например, если номера в отеле недоступны, исполнитель может предложить другие варианты.

*Ребра switch-case* — маршрутизируют сообщения к разным исполнителям в зависимости от условий. Например, если у путешественника есть приоритетный доступ, его задачи обрабатываются другим рабочим процессом.

*Ребра Fan-out* — отправляют одно сообщение сразу нескольким получателям.

*Ребра Fan-in* — собирают несколько сообщений от разных исполнителей и отправляют одному получателю.

**События**

Для улучшения наблюдаемости рабочих процессов MAF предлагает встроенные события выполнения, включая:

- `WorkflowStartedEvent` — Начало выполнения рабочего процесса
- `WorkflowOutputEvent` — Рабочий процесс создаёт выходные данные
- `WorkflowErrorEvent` — Рабочий процесс столкнулся с ошибкой
- `ExecutorInvokeEvent` — Исполнитель начинает обработку
- `ExecutorCompleteEvent` — Исполнитель завершил обработку
- `RequestInfoEvent` — Отправлен запрос

## Расширенные паттерны MAF

Выше были рассмотрены основные концепции Microsoft Agent Framework. При создании более сложных агентов учтите следующие расширенные паттерны:

- **Композиция промежуточного ПО**: объединение нескольких обработчиков промежуточного ПО (логирование, аутентификация, ограничение скорости) с использованием функционального и чат-промежуточного ПО для точного контроля поведения агента.
- **Контрольные точки рабочего процесса**: использование событий рабочего процесса и сериализации для сохранения и возобновления долгих процессов агента.
- **Динамический выбор инструментов**: комбинирование RAG с описанием инструментов и регистрацией инструментов в MAF для показа только релевантных инструментов по запросу.
- **Передача между несколькими агентами**: использование ребер рабочего процесса и условного маршрутизирования для организации передачи задач между специализированными агентами.

## Размещение агентов LangChain / LangGraph на Microsoft Foundry

Microsoft Agent Framework является **фреймворк-совместимым** — вы не ограничены агентами, написанными с помощью MAF. Если у вас уже есть агент, созданный с помощью **LangChain** или **LangGraph**, вы можете запустить его как **хостинг агент Foundry**, чтобы Foundry управляла временем выполнения, сессиями, масштабированием, идентификацией и протокольными конечными точками, при этом логика вашего агента остаётся в LangGraph.

Это реализуется с помощью пакета `langchain_azure_ai.agents.hosting`, который предоставляет скомпилированный граф LangGraph по тем же протоколам, что и агенты, размещённые в Foundry.

**1. Установите extra для хостинга:**

```bash
pip install -U "langchain-azure-ai[hosting]>=1.2.4" azure-identity
```

Пакет `hosting` устанавливает библиотеки протокола Foundry: `azure-ai-agentserver-responses` (конечная точка `/responses`, совместимая с OpenAI) и `azure-ai-agentserver-invocations` (универсальная конечная точка `/invocations`).

**2. Выберите протокол хостинга:**

| Протокол | Класс хоста | Конечная точка | Используйте, если |
|----------|-----------|----------|----------|
| **Responses** | `ResponsesHostServer` | `/responses` | Вам нужен чат, потоковая обработка, история ответов и многоходовые диалоги, совместимые с OpenAI — рекомендуемый вариант для разговорных агентов. |
| **Invocations** | `InvocationsHostServer` | `/invocations` | Требуется настраиваемый JSON, точка webhook или неконверсационная обработка. |

Поскольку **Responses API является основным API для разработки агентов в Foundry**, начните с `ResponsesHostServer` для большинства агентов.

**3. Настройте переменные окружения** (сначала выполните `az login`, чтобы `DefaultAzureCredential` мог аутентифицироваться):

```bash
export FOUNDRY_PROJECT_ENDPOINT="https://<resource>.services.ai.azure.com/api/projects/<project>"
export FOUNDRY_MODEL_NAME="gpt-4.1"
```

При том, что агент позже запускается как хостинг агент в Foundry, платформа автоматически добавит `FOUNDRY_PROJECT_ENDPOINT`.

**4. Предоставьте агент LangGraph через протокол Responses:**

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
    deployment = os.environ.get("FOUNDRY_MODEL_NAME", "gpt-4.1")
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

Запустите локально с помощью `python main.py`, затем отправьте запрос Responses на `http://localhost:8088/responses`.

**Ключевые особенности:**

- **Диалоги**: Клиенты продолжают разговор, передавая `previous_response_id` или ID `conversation`. Если граф скомпилирован с контрольной точкой LangGraph, Foundry связывает состояние разговора с контрольной точкой (в производстве используйте устойчивый чекпоинтер; для локального тестирования подходит `MemorySaver`).
- **Участие человека в цикле**: Если граф использует `interrupt()`, `ResponsesHostServer` отображает ожидающие прерывания как элементы `function_call` / `mcp_approval_request` в Responses, а клиенты продолжают с соответствующим `function_call_output` / `mcp_approval_response`.
- **Деплой в Foundry**: Используйте Azure Developer CLI — `azd ext install azure.ai.agents`, `azd ai agent init -m <manifest>`, `azd ai agent run` (локально, требуется Docker), затем `azd provision` и `azd deploy`. Для деплоя хостинг агента нужна роль **Foundry Project Manager**.

Рабочий пример этого можно найти в [code-samples/14-langchain-hosted-agent.py](../../../14-microsoft-agent-framework/code-samples/14-langchain-hosted-agent.py). Полное руководство (протокол Invocations, кастомные схемы запросов и устранение неполадок) смотрите в [Host LangGraph agents as Foundry hosted agents](https://learn.microsoft.com/azure/foundry/how-to/develop/langchain-hosted-agents).

## Примеры кода 

Примеры кода для Microsoft Agent Framework доступны в этом репозитории в файлах `xx-python-agent-framework` и `xx-dotnet-agent-framework`.

## Есть вопросы по Microsoft Agent Framework?

Присоединяйтесь к [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D), чтобы общаться с другими учащимися, посещать часы консультаций и получать ответы на вопросы по AI-агентам.
## Предыдущий урок

[Память для AI-агентов](../13-agent-memory/README.md)

## Следующий урок

[Создание агентов для использования ПК (CUA)](../15-browser-use/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Отказ от ответственности**:
Этот документ был переведен с использованием сервиса машинного перевода [Co-op Translator](https://github.com/Azure/co-op-translator). Несмотря на наши усилия по обеспечению точности, имейте в виду, что автоматический перевод может содержать ошибки или неточности. Оригинальный документ на его исходном языке следует считать авторитетным источником. Для получения критически важной информации рекомендуется обратиться к профессиональному человеческому переводу. Мы не несем ответственности за любые недоразумения или неправильные толкования, возникшие в результате использования этого перевода.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->