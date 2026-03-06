# Изучение Microsoft Agent Framework

![Фреймворк агентов](../../../translated_images/ru/lesson-14-thumbnail.90df0065b9d234ee.webp)

### Введение

В этом уроке будут рассмотрены:

- Понимание Microsoft Agent Framework: ключевые функции и ценность  
- Изучение ключевых концепций Microsoft Agent Framework
- Продвинутые паттерны MAF: рабочие процессы, middleware и память

## Цели обучения

После прохождения этого урока вы будете уметь:

- Создавать готовых к производству AI-агентов с использованием Microsoft Agent Framework
- Применять основные возможности Microsoft Agent Framework к вашим агентным сценариям
- Использовать продвинутые паттерны, включая рабочие процессы, middleware и наблюдаемость

## Примеры кода 

Примеры кода для [Microsoft Agent Framework (MAF)](https://aka.ms/ai-agents-beginners/agent-framewrok) можно найти в этом репозитории в файлах `xx-python-agent-framework` и `xx-dotnet-agent-framework`.

## Понимание Microsoft Agent Framework

![Введение во фреймворк](../../../translated_images/ru/framework-intro.077af16617cf130c.webp)

[Microsoft Agent Framework (MAF)](https://aka.ms/ai-agents-beginners/agent-framewrok) — это унифицированный фреймворк от Microsoft для создания AI-агентов. Он предоставляет гибкость для решения широкого спектра агентных сценариев, встречающихся как в производственной, так и в исследовательской среде, включая:

- **Sequential Agent orchestration** в сценариях, где необходимы пошаговые рабочие процессы.
- **Concurrent orchestration** в сценариях, где агенты должны выполнять задачи одновременно.
- **Group chat orchestration** в сценариях, где агенты могут совместно работать над одной задачей.
- **Handoff Orchestration** в сценариях, где агенты передают задачу друг другу по мере выполнения подзадач.
- **Magnetic Orchestration** в сценариях, где управляющий агент создаёт и изменяет список задач и обрабатывает координацию субагентов для выполнения задачи.

Для развертывания AI-агентов в продакшене MAF также включает функции для:

- **Observability** через использование OpenTelemetry, где каждое действие AI-агента включая вызовы инструментов, шаги оркестрации, цепочки рассуждений и мониторинг производительности отображается через дашборды Microsoft Foundry.
- **Security** за счёт хостинга агентов нативно в Microsoft Foundry, который включает механизмы безопасности такие как ролевой доступ, обработка приватных данных и встроенная контентная безопасность.
- **Durability** поскольку потоки агентов и рабочие процессы могут приостанавливаться, возобновляться и восстанавливаться после ошибок, что позволяет запускать длительные процессы.
- **Control** — поддерживаются рабочие процессы с человеком в цикле, где задачи помечаются как требующие одобрения человека.

Microsoft Agent Framework также ориентирован на совместимость за счёт:

- **Being Cloud-agnostic** - агенты могут запускаться в контейнерах, локально (on-prem) и в разных облачных средах.
- **Being Provider-agnostic** - агенты можно создавать через предпочитаемые SDK, включая Azure OpenAI и OpenAI
- **Integrating Open Standards** - агенты могут использовать протоколы такие как Agent-to-Agent(A2A) и Model Context Protocol (MCP) для обнаружения и использования других агентов и инструментов.
- **Plugins and Connectors** - можно подключаться к сервисам данных и памяти таким как Microsoft Fabric, SharePoint, Pinecone и Qdrant.

Давайте рассмотрим, как эти функции применяются к некоторым ключевым концепциям Microsoft Agent Framework.

## Ключевые концепции Microsoft Agent Framework

### Агенты

![Фреймворк агентов](../../../translated_images/ru/agent-components.410a06daf87b4fef.webp)

**Создание агентов**

Создание агента осуществляется путем определения inference service (LLM Provider), набора инструкций для агента и присвоения `name`:

```python
agent = AzureOpenAIChatClient(credential=AzureCliCredential()).create_agent( instructions="You are good at recommending trips to customers based on their preferences.", name="TripRecommender" )
```

Выше используется `Azure OpenAI`, но агенты можно создавать с использованием различных сервисов, включая `Microsoft Foundry Agent Service`:

```python
AzureAIAgentClient(async_credential=credential).create_agent( name="HelperAgent", instructions="You are a helpful assistant." ) as agent
```

API OpenAI `Responses`, `ChatCompletion`

```python
agent = OpenAIResponsesClient().create_agent( name="WeatherBot", instructions="You are a helpful weather assistant.", )
```

```python
agent = OpenAIChatClient().create_agent( name="HelpfulAssistant", instructions="You are a helpful assistant.", )
```

или удалённых агентов с использованием протокола A2A:

```python
agent = A2AAgent( name=agent_card.name, description=agent_card.description, agent_card=agent_card, url="https://your-a2a-agent-host" )
```

**Запуск агентов**

Агенты запускаются с помощью методов `.run` или `.run_stream` для нестриминговых или стриминговых ответов.

```python
result = await agent.run("What are good places to visit in Amsterdam?")
print(result.text)
```

```python
async for update in agent.run_stream("What are the good places to visit in Amsterdam?"):
    if update.text:
        print(update.text, end="", flush=True)

```

Каждый запуск агента также может иметь опции для настройки параметров, таких как `max_tokens`, используемые агентом, `tools`, которые агент может вызывать, и даже сам `model`, используемый агентом.

Это полезно в случаях, когда для выполнения задачи пользователя требуются конкретные модели или инструменты.

**Инструменты**

Инструменты можно задавать как при определении агента:

```python
def get_attractions( location: Annotated[str, Field(description="The location to get the top tourist attractions for")], ) -> str: """Get the top tourist attractions for a given location.""" return f"The top attractions for {location} are." 


# При прямом создании ChatAgent

agent = ChatAgent( chat_client=OpenAIChatClient(), instructions="You are a helpful assistant", tools=[get_attractions]

```

таким и при запуске агента:

```python

result1 = await agent.run( "What's the best place to visit in Seattle?", tools=[get_attractions] # Инструмент предоставлен только для этого запуска )
```

**Потоки агента**

Потоки агента используются для обработки многошаговых разговоров. Треды могут создаваться либо:

- Использование `get_new_thread()`, которое позволяет сохранять поток со временем
- Автоматическое создание потока при запуске агента, при котором поток существует только в течение текущего запуска.

Чтобы создать поток, код выглядит так:

```python
# Создайте новый поток.
thread = agent.get_new_thread() # Запустите агента в этом потоке.
response = await agent.run("Hello, I am here to help you book travel. Where would you like to go?", thread=thread)

```

Затем вы можете сериализовать поток для хранения и последующего использования:

```python
# Создать новый поток.
thread = agent.get_new_thread() 

# Запустить агента в этом потоке.

response = await agent.run("Hello, how are you?", thread=thread) 

# Сериализовать поток для хранения.

serialized_thread = await thread.serialize() 

# Десериализовать состояние потока после загрузки из хранилища.

resumed_thread = await agent.deserialize_thread(serialized_thread)
```

**Middleware агента**

Агенты взаимодействуют с инструментами и LLM для выполнения задач пользователей. В определённых сценариях мы хотим выполнять действия или отслеживать события между этими взаимодействиями. Middleware агента позволяет делать это посредством:

*Function Middleware*

Этот middleware позволяет выполнять действие между агентом и функцией/инструментом, который он будет вызывать. Пример использования — логирование вызова функции.

В коде ниже `next` определяет, должен ли быть вызван следующий middleware или реальная функция.

```python
async def logging_function_middleware(
    context: FunctionInvocationContext,
    next: Callable[[FunctionInvocationContext], Awaitable[None]],
) -> None:
    """Function middleware that logs function execution."""
    # Предварительная обработка: запись в журнал перед выполнением функции
    print(f"[Function] Calling {context.function.name}")

    # Продолжить к следующему промежуточному обработчику или к выполнению функции
    await next(context)

    # Постобработка: запись в журнал после выполнения функции
    print(f"[Function] {context.function.name} completed")
```

*Chat Middleware*

Этот middleware позволяет выполнять или логировать действие между агентом и запросами к LLM.

Он содержит важную информацию, такую как `messages`, которые отправляются в AI-сервис.

```python
async def logging_chat_middleware(
    context: ChatContext,
    next: Callable[[ChatContext], Awaitable[None]],
) -> None:
    """Chat middleware that logs AI interactions."""
    # Предобработка: логирование перед вызовом ИИ
    print(f"[Chat] Sending {len(context.messages)} messages to AI")

    # Продолжить к следующему промежуточному ПО или сервису ИИ
    await next(context)

    # Постобработка: логирование после ответа ИИ
    print("[Chat] AI response received")

```

**Память агента**

Как было рассмотрено в уроке `Agentic Memory`, память является важным элементом, позволяющим агенту работать в разных контекстах. MAF предлагает несколько разных типов памяти:

*In-Memory Storage*

Это память, хранимая в потоках во время выполнения приложения.

```python
# Создать новый поток.
thread = agent.get_new_thread() # Запустить агента в этом потоке.
response = await agent.run("Hello, I am here to help you book travel. Where would you like to go?", thread=thread)
```

*Persistent Messages*

Эта память используется для хранения истории бесед между разными сессиями. Она определяется с помощью `chat_message_store_factory` :

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

*Dynamic Memory*

Эта память добавляется в контекст перед запуском агентов. Эти виды памяти могут храниться во внешних сервисах, таких как mem0:

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

Наблюдаемость важна для построения надежных и удобных в сопровождении агентных систем. MAF интегрируется с OpenTelemetry для предоставления трассировки и метрик для лучшей наблюдаемости.

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

MAF предлагает рабочие процессы — заранее определённые шаги для выполнения задачи, в которые включаются AI-агенты как компоненты.

Рабочие процессы состоят из различных компонентов, которые обеспечивают лучший контроль потока. Рабочие процессы также позволяют реализовать **многоагентную оркестрацию** и **контрольные точки (checkpointing)** для сохранения состояний рабочего процесса.

Основные компоненты рабочего процесса:

**Executors**

Исполнители получают входные сообщения, выполняют назначенные задачи и затем формируют выходное сообщение. Это продвигает рабочий процесс к выполнению более крупной задачи. Исполнителями могут быть либо AI-агенты, либо пользовательская логика.

**Переходы (Edges)**

Переходы используются для определения потока сообщений в рабочем процессе. Они могут быть:

*Прямые переходы (Direct Edges)* - простые связи один-к-одному между исполнителями:

```python
from agent_framework import WorkflowBuilder

builder = WorkflowBuilder()
builder.add_edge(source_executor, target_executor)
builder.set_start_executor(source_executor)
workflow = builder.build()
```

*Условные переходы (Conditional Edges)* - активируются после выполнения определённого условия. Например, когда номера в отеле недоступны, исполнитель может предложить другие варианты.

*Switch-case Edges* - направляют сообщения к разным исполнителям в зависимости от заданных условий. Например: если у клиента приоритетный доступ, его задачи будут обрабатываться в другом рабочем процессе.

*Fan-out Edges* - отправляют одно сообщение нескольким целям.

*Fan-in Edges* - собирают несколько сообщений от разных исполнителей и отправляют их одному получателю.

**События**

Для лучшей наблюдаемости рабочих процессов MAF предоставляет встроенные события для выполнения, включая:

- `WorkflowStartedEvent`  - Выполнение рабочего процесса начинается
- `WorkflowOutputEvent` - Рабочий процесс формирует выходные данные
- `WorkflowErrorEvent` - Во время выполнения рабочего процесса возникает ошибка
- `ExecutorInvokeEvent`  - Исполнитель начинает обработку
- `ExecutorCompleteEvent`  -  Исполнитель завершил обработку
- `RequestInfoEvent` - Отправлен запрос

## Продвинутые паттерны MAF

Разделы выше охватывают ключевые концепции Microsoft Agent Framework. По мере создания более сложных агентов, рассмотрите следующие продвинутые паттерны:

- **Middleware Composition**: цепочка нескольких обработчиков middleware (логирование, аутентификация, ограничение скорости) с использованием function и chat middleware для тонкого управления поведением агента.
- **Workflow Checkpointing**: использовать события рабочего процесса и сериализацию для сохранения и возобновления долгоживущих процессов агентов.
- **Dynamic Tool Selection**: комбинировать RAG поверх описаний инструментов с регистрацией инструментов в MAF, чтобы показывать только релевантные инструменты для каждого запроса.
- **Multi-Agent Handoff**: использовать переходы рабочего процесса и условную маршрутизацию для оркестровки передачи задач между специализированными агентами.

## Примеры кода 

Примеры кода для Microsoft Agent Framework можно найти в этом репозитории в файлах `xx-python-agent-framework` и `xx-dotnet-agent-framework`.

## Есть ещё вопросы по Microsoft Agent Framework?

Присоединяйтесь к [Microsoft Foundry Discord](https://aka.ms/ai-agents/discord) , чтобы общаться с другими учащимися, посещать консультации и получить ответы на вопросы по вашим AI-агентам.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
Отказ от ответственности:
Этот документ был переведен с помощью сервиса перевода на основе ИИ Co-op Translator (https://github.com/Azure/co-op-translator). Хотя мы стремимся к точности, обратите внимание, что автоматические переводы могут содержать ошибки или неточности. Оригинальный документ на исходном языке следует считать авторитетным источником. Для критически важной информации рекомендуется пользоваться услугами профессионального переводчика. Мы не несем ответственности за любые недоразумения или неправильные толкования, возникшие в результате использования данного перевода.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->