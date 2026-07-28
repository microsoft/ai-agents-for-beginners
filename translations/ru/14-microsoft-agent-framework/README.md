# Изучение Microsoft Agent Framework

![Agent Framework](../../../translated_images/ru/lesson-14-thumbnail.90df0065b9d234ee.webp)

### Введение

В этом уроке будут рассмотрены:

- Понимание Microsoft Agent Framework: Ключевые особенности и ценность  
- Изучение основных концепций Microsoft Agent Framework
- Продвинутые шаблоны MAF: рабочие процессы, промежуточное ПО и память

## Цели обучения

После завершения этого урока вы сможете:

- Создавать готовых к производству AI-агентов с помощью Microsoft Agent Framework
- Применять основные функции Microsoft Agent Framework в ваших агентных сценариях
- Использовать продвинутые шаблоны, включая рабочие процессы, промежуточное ПО и обеспечиваемость наблюдения

## Примеры кода 

Примеры кода для [Microsoft Agent Framework (MAF)](https://aka.ms/ai-agents-beginners/agent-framework) находятся в этом репозитории в файлах `xx-python-agent-framework` и `xx-dotnet-agent-framework`.

## Понимание Microsoft Agent Framework

![Framework Intro](../../../translated_images/ru/framework-intro.077af16617cf130c.webp)

[Microsoft Agent Framework (MAF)](https://aka.ms/ai-agents-beginners/agent-framework) — это единая платформа Microsoft для создания AI-агентов. Она обеспечивает гибкость для решения широкого спектра агентных сценариев, встречающихся как в продуктивной среде, так и в исследовательских проектах, включая:

- **Последовательную оркестрацию агентов** в сценариях, где нужны поэтапные рабочие процессы.
- **Параллельную оркестрацию** в сценариях, когда агенты должны выполнять задачи одновременно.
- **Оркестрацию группового чата** в случаях, когда агенты могут совместно работать над одной задачей.
- **Оркестрацию передачи задач** в сценариях, когда агенты передают задачи друг другу по мере выполнения подзадач.
- **Магнитную оркестрацию** в случаях, когда управляющий агент создает и изменяет список задач и координирует подагентов для выполнения задачи.

Для запуска AI-агентов в продакшене MAF также включает функции для:

- **Обеспечения наблюдаемости** через OpenTelemetry, где фиксируется каждое действие AI-агента, включая вызовы инструментов, шаги оркестрации, потоки рассуждений и мониторинг производительности через панели Microsoft Foundry.
- **Безопасности**, предоставляемой размещением агентов непосредственно на Microsoft Foundry, включая контроль доступа на основе ролей, обработку конфиденциальных данных и встроенную безопасность контента.
- **Устойчивости**, так как потоки и рабочие процессы агента могут приостанавливаться, возобновляться и восстанавливаться после ошибок, что позволяет выполнять долгосрочные процессы.
- **Управления**, поскольку поддерживаются рабочие процессы с участием человека, где задачи отмечаются как требующие одобрения человеком.

Microsoft Agent Framework также ориентирован на обеспечение совместимости благодаря:

- **Независимости от облака** — агенты могут запускаться в контейнерах, на локальных серверах и в различных облаках.
- **Независимости от провайдера** — агенты могут создаваться через предпочитаемые SDK, включая Azure OpenAI и OpenAI.
- **Интеграции открытых стандартов** — агенты могут использовать протоколы, такие как Agent-to-Agent (A2A) и Model Context Protocol (MCP), для обнаружения и использования других агентов и инструментов.
- **Плагины и коннекторы** — связи могут устанавливаться с сервисами данных и памяти, такими как Microsoft Fabric, SharePoint, Pinecone и Qdrant.

Рассмотрим, как эти функции применяются к основным концепциям Microsoft Agent Framework.

## Ключевые концепции Microsoft Agent Framework

### Агенты

![Agent Framework](../../../translated_images/ru/agent-components.410a06daf87b4fef.webp)

**Создание агентов**

Создание агента осуществляется путем определения сервиса вывода (поставщика LLM),  
набора инструкций для AI-агента и присвоения ему `имени`:

```python
agent = AzureOpenAIChatClient(credential=AzureCliCredential()).create_agent( instructions="You are good at recommending trips to customers based on their preferences.", name="TripRecommender" )
```

Приведенный выше пример использует `Azure OpenAI`, но агенты могут создаваться с использованием различных сервисов, включая `Microsoft Foundry Agent Service`:

```python
AzureAIAgentClient(async_credential=credential).create_agent( name="HelperAgent", instructions="You are a helpful assistant." ) as agent
```

OpenAI `Responses`, API `ChatCompletion`

```python
agent = OpenAIResponsesClient().create_agent( name="WeatherBot", instructions="You are a helpful weather assistant.", )
```

```python
agent = OpenAIChatClient().create_agent( name="HelpfulAssistant", instructions="You are a helpful assistant.", )
```

или [MiniMax](https://platform.minimaxi.com/), предоставляющий OpenAI-совместимый API с большим контекстным окном (до 204К токенов):

```python
agent = OpenAIChatClient(base_url="https://api.minimax.io/v1", api_key=os.environ["MINIMAX_API_KEY"], model_id="MiniMax-M3").create_agent( name="HelpfulAssistant", instructions="You are a helpful assistant.", )
```

или удаленных агентов с использованием протокола A2A:

```python
agent = A2AAgent( name=agent_card.name, description=agent_card.description, agent_card=agent_card, url="https://your-a2a-agent-host" )
```

**Запуск агентов**

Агенты запускаются с помощью методов `.run` или `.run_stream` для не потоковых или потоковых ответов соответственно.

```python
result = await agent.run("What are good places to visit in Amsterdam?")
print(result.text)
```

```python
async for update in agent.run_stream("What are the good places to visit in Amsterdam?"):
    if update.text:
        print(update.text, end="", flush=True)

```

При запуске агента также можно задать параметры, например, `max_tokens`, используемые агентом, `tools` (инструменты), которые агент может вызывать, и даже сам `model`, применяемую для агента.

Это полезно в случаях, когда для выполнения задачи пользователя требуются определённые модели или инструменты.

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

**Потоки агента**

Потоки агента используются для ведения многотуровых диалогов. Потоки могут создаваться либо:

- С помощью `get_new_thread()`, что позволяет сохранять поток с течением времени
- Автоматически при запуске агента, причем поток действует только в течение текущего выполнения.

Для создания потока код выглядит так:

```python
# Создать новый поток.
thread = agent.get_new_thread() # Запустить агент с этим потоком.
response = await agent.run("Hello, I am here to help you book travel. Where would you like to go?", thread=thread)

```

Вы можете сериализовать поток, чтобы сохранить его для последующего использования:

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

Агенты взаимодействуют с инструментами и LLM для выполнения задач пользователя. В некоторых сценариях требуется выполнение действий или отслеживание между этими взаимодействиями. Промежуточное ПО агента позволяет это делать:

*Функциональное промежуточное ПО*

Это промежуточное ПО позволяет выполнять действие между агентом и вызываемой им функцией/инструментом. Пример использования — логирование вызова функции.

В приведенном коде `next` определяет, вызывать ли следующее промежуточное ПО или саму функцию.

```python
async def logging_function_middleware(
    context: FunctionInvocationContext,
    next: Callable[[FunctionInvocationContext], Awaitable[None]],
) -> None:
    """Function middleware that logs function execution."""
    # Предварительная обработка: Лог перед выполнением функции
    print(f"[Function] Calling {context.function.name}")

    # Продолжить к следующему промежуточному ПО или выполнению функции
    await next(context)

    # Постобработка: Лог после выполнения функции
    print(f"[Function] {context.function.name} completed")
```

*Промежуточное ПО чата*

Это промежуточное ПО позволяет выполнять действия или вести логирование между агентом и запросами к LLM.

Содержит важную информацию, такую как `messages`, отправляемые AI-сервису.

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

**Память агента**

Как рассмотрено в уроке `Agentic Memory`, память — важный элемент, позволяющий агенту работать в различных контекстах. MAF предлагает несколько видов памяти:

*Временное хранение в памяти*

Это память, хранящаяся в потоках во время выполнения приложения.

```python
# Создайте новый поток.
thread = agent.get_new_thread() # Запустите агент с потоком.
response = await agent.run("Hello, I am here to help you book travel. Where would you like to go?", thread=thread)
```

*Постоянные сообщения*

Эта память используется для хранения истории разговоров в разных сессиях. Определяется с помощью `chat_message_store_factory`:

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

Эта память добавляется в контекст перед запуском агентов. Она может храниться во внешних сервисах, таких как mem0:

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

Наблюдаемость важна для создания надежных и поддерживаемых агентных систем. MAF интегрируется с OpenTelemetry для обеспечения трассировки и метрик для улучшенной наблюдаемости.

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

MAF предлагает рабочие процессы — предопределенные шаги для выполнения задачи с включением AI-агентов в качестве компонентов на этих шагах.

Рабочие процессы состоят из различных компонентов, которые обеспечивают лучший контроль потока. Рабочие процессы также поддерживают **оркестрацию нескольких агентов** и **контрольные точки** для сохранения состояния рабочего процесса.

Основные компоненты рабочего процесса:

**Исполнители**

Исполнители получают входящие сообщения, выполняют назначенные задачи и генерируют выходное сообщение. Благодаря этому рабочий процесс продвигается к завершению большой задачи. Исполнители могут быть AI-агентами или настраиваемой логикой.

**Рёбра**

Рёбра используются для определения потока сообщений внутри рабочего процесса. Они бывают:

*Прямые рёбра* — простые однонаправленные связи между исполнителями:

```python
from agent_framework import WorkflowBuilder

builder = WorkflowBuilder()
builder.add_edge(source_executor, target_executor)
builder.set_start_executor(source_executor)
workflow = builder.build()
```

*Условные рёбра* — активируются при выполнении определенного условия. Например, когда гостиничные номера недоступны, исполнитель может предложить другие варианты.

*Рёбра switch-case* — направляют сообщения к разным исполнителям в зависимости от заданных условий. Например, если у туриста есть приоритетный доступ, их задачи обрабатываются другим рабочим процессом.

*Рёбра fan-out* — отправляют одно сообщение нескольким получателям.

*Рёбра fan-in* — собирают несколько сообщений от разных исполнителей и направляют их одному получателю.

**События**

Для улучшения наблюдаемости рабочих процессов MAF предоставляет встроенные события выполнения, включая:

- `WorkflowStartedEvent` — запуск выполнения рабочего процесса
- `WorkflowOutputEvent` — рабочий процесс выдает результат
- `WorkflowErrorEvent` — рабочий процесс столкнулся с ошибкой
- `ExecutorInvokeEvent` — исполнитель начал обработку
- `ExecutorCompleteEvent` — исполнитель завершил обработку
- `RequestInfoEvent` — выполнен запрос

## Продвинутые шаблоны MAF

В приведенных разделах описаны ключевые концепции Microsoft Agent Framework. При построении более сложных агентов рассмотрите следующие продвинутые шаблоны:

- **Композиция промежуточного ПО**: объединение нескольких обработчиков промежуточного ПО (логирование, аутентификация, ограничение частоты) с помощью функционального и чат-промежуточного ПО для тонкой настройки поведения агента.
- **Сохранение контрольных точек рабочего процесса**: использование событий рабочего процесса и сериализации для сохранения и возобновления долгосрочных процессов агента.
- **Динамический выбор инструментов**: сочетание RAG по описаниям инструментов с регистрацией инструментов в MAF для представления только релевантных инструментов по запросу.
- **Передача между несколькими агентами**: использование рёбер рабочего процесса и условной маршрутизации для оркестрации передачи задач между специализированными агентами.

## Размещение агентов LangChain / LangGraph на Microsoft Foundry

Microsoft Agent Framework является **фреймворк-интероперабельным** — вы не ограничены агентами, написанными только с помощью MAF. Если у вас уже есть агент, созданный с использованием **LangChain** или **LangGraph**, вы можете запускать его как **размещенный в Microsoft Foundry агент**, чтобы Foundry управлял средой выполнения, сессиями, масштабированием, идентификацией и конечными точками протокола, а логика агента оставалась в LangGraph.

Это реализуется с помощью пакета `langchain_azure_ai.agents.hosting`, который предоставляет скомпилированный граф LangGraph через те же протоколы, что и агенты, размещенные в Foundry.

**1. Установите вспомогательную библиотеку для размещения:**

```bash
pip install -U "langchain-azure-ai[hosting]>=1.2.4" azure-identity
```

Вспомогательная установка (`hosting`) включает библиотеки протокола Foundry: `azure-ai-agentserver-responses` (совместимый с OpenAI эндпоинт `/responses`) и `azure-ai-agentserver-invocations` (универсальный эндпоинт `/invocations`).

**2. Выберите протокол размещения:**

| Протокол | Класс хоста | Конечная точка | Использование |
|----------|-------------|---------------|-------------|
| **Responses** | `ResponsesHostServer` | `/responses` | Используйте для совместимого с OpenAI чата, потоковой передачи, истории ответов и ведения диалогов — рекомендованный вариант для разговорных агентов. |
| **Invocations** | `InvocationsHostServer` | `/invocations` | Используйте для пользовательского JSON-формата, webhook-подобного эндпоинта или неперсонального процесса. |

Поскольку **API Responses является основным API для разработки агентов в Foundry**, начните с `ResponsesHostServer` для большинства агентов.

**3. Настройте переменные окружения** (сначала выполните `az login`, чтобы `DefaultAzureCredential` мог аутентифицироваться):

```bash
export FOUNDRY_PROJECT_ENDPOINT="https://<resource>.services.ai.azure.com/api/projects/<project>"
export FOUNDRY_MODEL_NAME="gpt-5-mini"
```

При запуске агента как размещенного агента в Foundry платформа автоматически добавит `FOUNDRY_PROJECT_ENDPOINT`.

**4. Опубликуйте агента LangGraph через протокол Responses:**

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

    # ChatOpenAI здесь нацелен на конечную точку Foundry проекта, совместимую с OpenAI (Responses).
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

Запустите локально с помощью `python main.py`, затем отправьте запрос на Responses к `http://localhost:8088/responses`.

**Ключевые особенности:**

- **Диалоги**: Клиенты продолжают разговор, передавая `previous_response_id` или идентификатор `conversation`. Если граф скомпилирован с контроллером LangGraph, Foundry привязывает состояние диалога к контрольной точке (используйте устойчивый контроллер в производстве; для локального тестирования подойдет `MemorySaver`).
- **Человек в цепочке**: Если граф использует LangGraph `interrupt()`, `ResponsesHostServer` показывает ожидающий прерыватель как элемент Responses `function_call` / `mcp_approval_request`, и клиенты продолжают с соответствующим `function_call_output` / `mcp_approval_response`.
- **Развертывание в Foundry**: Используйте Azure Developer CLI — `azd ext install azure.ai.agents`, `azd ai agent init -m <manifest>`, `azd ai agent run` (локально, требуется Docker), затем `azd provision` и `azd deploy`. Для развертывания размещенного агента требуется роль **Foundry Project Manager**.

Рабочая версия этого примера доступна в [code-samples/14-langchain-hosted-agent.py](../../../14-microsoft-agent-framework/code-samples/14-langchain-hosted-agent.py). Для полного руководства (протокол Invocations, пользовательские схемы запросов и устранение неполадок) смотрите [Host LangGraph agents as Foundry hosted agents](https://learn.microsoft.com/azure/foundry/how-to/develop/langchain-hosted-agents).

## Примеры кода 

Примеры кода для Microsoft Agent Framework находятся в этом репозитории в файлах `xx-python-agent-framework` и `xx-dotnet-agent-framework`.

## Есть вопросы по Microsoft Agent Framework?

Присоединяйтесь к [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D), чтобы встретиться с другими учащимися, посетить часы работы офиса и получить ответы на вопросы об AI-агентах.
## Предыдущий урок

[Память для AI-агентов](../13-agent-memory/README.md)

## Следующий урок

[Создание агентов для работы с компьютером (CUA)](../15-browser-use/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Отказ от ответственности**:
Этот документ был переведен с использованием сервиса машинного перевода [Co-op Translator](https://github.com/Azure/co-op-translator). Несмотря на наши усилия по обеспечению точности, имейте в виду, что автоматический перевод может содержать ошибки или неточности. Оригинальный документ на его исходном языке следует считать авторитетным источником. Для получения критически важной информации рекомендуется обратиться к профессиональному человеческому переводу. Мы не несем ответственности за любые недоразумения или неправильные толкования, возникшие в результате использования этого перевода.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->