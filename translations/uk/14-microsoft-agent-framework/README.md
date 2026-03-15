# Ознайомлення з Microsoft Agent Framework

![Фреймворк агентів](../../../translated_images/uk/lesson-14-thumbnail.90df0065b9d234ee.webp)

### Вступ

У цьому уроці розглядається:

- Розуміння Microsoft Agent Framework: ключові особливості та цінність  
- Дослідження ключових концепцій Microsoft Agent Framework
- Розширені шаблони MAF: робочі процеси, middleware та пам'ять

## Цілі навчання

Після завершення цього уроку ви знатимете, як:

- Створювати готові до виробництва AI-агенти за допомогою Microsoft Agent Framework
- Застосовувати основні функції Microsoft Agent Framework до ваших агентних сценаріїв
- Використовувати розширені шаблони, включаючи робочі процеси, middleware та трасування

## Приклади коду 

Приклади коду для [Microsoft Agent Framework (MAF)](https://aka.ms/ai-agents-beginners/agent-framewrok) можна знайти в цьому репозиторії у файлах `xx-python-agent-framework` та `xx-dotnet-agent-framework`.

## Розуміння Microsoft Agent Framework

![Вступ до фреймворку](../../../translated_images/uk/framework-intro.077af16617cf130c.webp)

[Microsoft Agent Framework (MAF)](https://aka.ms/ai-agents-beginners/agent-framewrok) — це уніфікований фреймворк Microsoft для побудови агентів штучного інтелекту. Він пропонує гнучкість для вирішення широкого спектра застосувань з агентною логікою як у виробничих, так і в дослідницьких середовищах, зокрема:

- **Послідовна оркестрація агентів** у сценаріях, де потрібні покрокові робочі процеси.
- **Одночасна оркестрація** у сценаріях, де агенти повинні виконувати завдання одночасно.
- **Оркестрація групового чату** у сценаріях, де агенти можуть співпрацювати над одним завданням.
- **Оркестрація передачі** у сценаріях, де агенти передають завдання один одному по мірі виконання підзавдань.
- **Магнітна оркестрація** у сценаріях, де менеджер-агент створює та змінює список завдань і координує підагентів для завершення завдання.

Для впровадження AI-агентів у виробництві MAF також включає функції для:

- **Спостережуваність** через використання OpenTelemetry, де кожна дія AI-агента включно з викликом інструментів, кроками оркестрації, потоками міркувань і моніторингом продуктивності відображається через приладні дошки Microsoft Foundry.
- **Безпеки** завдяки розміщенню агентів безпосередньо на Microsoft Foundry, що включає засоби контролю безпеки, такі як керування доступом за ролями, обробка приватних даних і вбудований контроль вмісту.
- **Місткості (durability)** оскільки потоки агентів і робочі процеси можуть призупинятись, відновлюватись і відновлюватись після помилок, що дозволяє виконувати триваліші процеси.
- **Контролю** оскільки підтримуються робочі процеси з людиною в циклі, де завдання позначаються як такі, що вимагають затвердження людиною.

Microsoft Agent Framework також орієнтований на сумісність шляхом:

- **Незалежності від хмари** - агенти можуть працювати в контейнерах, локально та в різних хмарних середовищах.
- **Незалежності від постачальника** - агенти можна створювати через ваш улюблений SDK, включаючи Azure OpenAI та OpenAI
- **Інтеграції відкритих стандартів** - агенти можуть використовувати протоколи, такі як Agent-to-Agent (A2A) та Model Context Protocol (MCP), для виявлення і використання інших агентів та інструментів.
- **Плагінів і конекторів** - можна підключатися до сервісів даних та пам'яті, таких як Microsoft Fabric, SharePoint, Pinecone та Qdrant.

Далі подивимося, як ці функції застосовуються до деяких ключових концепцій Microsoft Agent Framework.

## Ключові концепції Microsoft Agent Framework

### Агенти

![Фреймворк агентів](../../../translated_images/uk/agent-components.410a06daf87b4fef.webp)

**Створення агентів**

Створення агента здійснюється шляхом визначення сервісу висновку (постачальник LLM), набору інструкцій для виконання агентом ШІ та призначеного `name`:

```python
agent = AzureOpenAIChatClient(credential=AzureCliCredential()).create_agent( instructions="You are good at recommending trips to customers based on their preferences.", name="TripRecommender" )
```

Вищезазначене використовує `Azure OpenAI`, але агенти можна створювати за допомогою різних сервісів, включаючи `Microsoft Foundry Agent Service`:

```python
AzureAIAgentClient(async_credential=credential).create_agent( name="HelperAgent", instructions="You are a helpful assistant." ) as agent
```

OpenAI `Responses`, `ChatCompletion` APIs

```python
agent = OpenAIResponsesClient().create_agent( name="WeatherBot", instructions="You are a helpful weather assistant.", )
```

```python
agent = OpenAIChatClient().create_agent( name="HelpfulAssistant", instructions="You are a helpful assistant.", )
```

або віддалених агентів, використовуючи протокол A2A:

```python
agent = A2AAgent( name=agent_card.name, description=agent_card.description, agent_card=agent_card, url="https://your-a2a-agent-host" )
```

**Запуск агентів**

Агенти запускаються за допомогою методів `.run` або `.run_stream` для відповідей без стріму або зі стрімом відповідно.

```python
result = await agent.run("What are good places to visit in Amsterdam?")
print(result.text)
```

```python
async for update in agent.run_stream("What are the good places to visit in Amsterdam?"):
    if update.text:
        print(update.text, end="", flush=True)

```

Кожен запуск агента також може мати параметри для налаштування таких параметрів, як `max_tokens`, `tools`, до яких агент може звертатися, і навіть сам `model`, що використовується агентом.

Це корисно у випадках, коли для виконання завдання користувача потрібні конкретні моделі або інструменти.

**Інструменти**

Інструменти можна визначати як під час визначення агента:

```python
def get_attractions( location: Annotated[str, Field(description="The location to get the top tourist attractions for")], ) -> str: """Get the top tourist attractions for a given location.""" return f"The top attractions for {location} are." 


# При безпосередньому створенні ChatAgent

agent = ChatAgent( chat_client=OpenAIChatClient(), instructions="You are a helpful assistant", tools=[get_attractions]

```

так і під час запуску агента:

```python

result1 = await agent.run( "What's the best place to visit in Seattle?", tools=[get_attractions] # Інструмент наданий лише для цього запуску )
```

**Потоки агентів**

Потоки агентів використовуються для обробки багатокрокових розмов. Потоки можна створити або шляхом:

- Використання `get_new_thread()`, що дозволяє зберігати потік з часом
- Автоматичного створення потоку під час запуску агента, коли потік існує лише під час поточного запуску.

Щоб створити потік, код виглядає так:

```python
# Створити новий потік.
thread = agent.get_new_thread() # Запустити агента у цьому потоці.
response = await agent.run("Hello, I am here to help you book travel. Where would you like to go?", thread=thread)

```

Потім ви можете серіалізувати потік для збереження і подальшого використання:

```python
# Створити новий потік.
thread = agent.get_new_thread() 

# Запустити агента з потоком.

response = await agent.run("Hello, how are you?", thread=thread) 

# Серіалізувати потік для зберігання.

serialized_thread = await thread.serialize() 

# Десеріалізувати стан потоку після завантаження зі сховища.

resumed_thread = await agent.deserialize_thread(serialized_thread)
```

**Middleware агента**

Агенти взаємодіють з інструментами та LLM, щоб виконувати завдання користувачів. В у деяких сценаріях ми хочемо виконувати або відстежувати дії між цими взаємодіями. Middleware агента дозволяє це робити через:

*Функціональний middleware*

Цей middleware дозволяє виконати дію між агентом та функцією/інструментом, який він викликає. Приклад використання — коли потрібно виконати логування виклику функції.

У наступному коді `next` визначає, чи має бути викликаний наступний middleware або фактична функція.

```python
async def logging_function_middleware(
    context: FunctionInvocationContext,
    next: Callable[[FunctionInvocationContext], Awaitable[None]],
) -> None:
    """Function middleware that logs function execution."""
    # Попередня обробка: запис у журнал перед виконанням функції
    print(f"[Function] Calling {context.function.name}")

    # Продовжити до наступного проміжного обробника або до виконання функції
    await next(context)

    # Післяобробка: запис у журнал після виконання функції
    print(f"[Function] {context.function.name} completed")
```

*Чат-мідлвар (Chat Middleware)*

Цей middleware дозволяє виконувати або реєструвати дію між агентом і запитами до LLM.

Тут міститься важлива інформація, така як `messages`, які надсилаються до сервісу ШІ.

```python
async def logging_chat_middleware(
    context: ChatContext,
    next: Callable[[ChatContext], Awaitable[None]],
) -> None:
    """Chat middleware that logs AI interactions."""
    # Попередня обробка: логування перед викликом ШІ
    print(f"[Chat] Sending {len(context.messages)} messages to AI")

    # Продовжити до наступного проміжного програмного забезпечення або сервісу ШІ
    await next(context)

    # Постобробка: логування після відповіді ШІ
    print("[Chat] AI response received")

```

**Пам'ять агента**

Як розглянуто в уроці `Agentic Memory`, пам'ять є важливим елементом, що дає можливість агенту працювати в різних контекстах. MAF пропонує кілька різних типів пам'яті:

*Зберігання в пам'яті (In-Memory Storage)*

Це пам'ять, що зберігається в потоках під час виконання програми.

```python
# Створіть новий потік.
thread = agent.get_new_thread() # Запустіть агента з цим потоком.
response = await agent.run("Hello, I am here to help you book travel. Where would you like to go?", thread=thread)
```

*Постійні повідомлення (Persistent Messages)*

Ця пам'ять використовується для зберігання історії розмов між різними сесіями. Вона визначається за допомогою `chat_message_store_factory` :

```python
from agent_framework import ChatMessageStore

# Створіть власне сховище повідомлень
def create_message_store():
    return ChatMessageStore()

agent = ChatAgent(
    chat_client=OpenAIChatClient(),
    instructions="You are a Travel assistant.",
    chat_message_store_factory=create_message_store
)

```

*Динамічна пам'ять (Dynamic Memory)*

Ця пам'ять додається до контексту перед запуском агентів. Такі пам'яті можуть зберігатися у зовнішніх сервісах, таких як mem0:

```python
from agent_framework.mem0 import Mem0Provider

# Використання Mem0 для розширених можливостей пам'яті
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

**Спостережуваність агента**

Спостережуваність важлива для побудови надійних і підтримуваних агентних систем. MAF інтегрується з OpenTelemetry для надання трасування та метрик для кращої спостережуваності.

```python
from agent_framework.observability import get_tracer, get_meter

tracer = get_tracer()
meter = get_meter()
with tracer.start_as_current_span("my_custom_span"):
    # зробити щось
    pass
counter = meter.create_counter("my_custom_counter")
counter.add(1, {"key": "value"})
```

### Робочі процеси

MAF пропонує робочі процеси — попередньо визначені кроки для виконання завдання, які включають AI-агентів як компоненти на цих кроках.

Робочі процеси складаються з різних компонентів, які дозволяють кращий контроль потоку. Робочі процеси також забезпечують **оркестрацію декількох агентів** і **чекпоінти** для збереження станів робочого процесу.

Основні компоненти робочого процесу:

**Виконавці**

Виконавці приймають вхідні повідомлення, виконують призначені їм завдання і потім генерують вихідне повідомлення. Це просуває робочий процес до завершення більшого завдання. Виконавцями можуть бути як агенти ШІ, так і кастомна логіка.

**Зв'язки (Edges)**

Зв'язки використовуються для визначення потоку повідомлень у робочому процесі. Вони можуть бути:

*Прямі зв'язки* - прості "один-до-одного" з'єднання між виконавцями:

```python
from agent_framework import WorkflowBuilder

builder = WorkflowBuilder()
builder.add_edge(source_executor, target_executor)
builder.set_start_executor(source_executor)
workflow = builder.build()
```

*Умовні зв'язки* - активуються після виконання певної умови. Наприклад, коли номери в готелі недоступні, виконавець може запропонувати інші варіанти.

*Switch-case зв'язки* - маршрутизують повідомлення до різних виконавців на основі визначених умов. Наприклад, якщо клієнт подорожі має пріоритетний доступ, його завдання можуть оброблятися в іншому робочому процесі.

*Fan-out зв'язки* - надсилають одне повідомлення до кількох цілей.

*Fan-in зв'язки* - збирають кілька повідомлень від різних виконавців і надсилають їх до однієї цілі.

**Події**

Для кращої спостережуваності робочих процесів MAF пропонує вбудовані події для виконання, включаючи:

- `WorkflowStartedEvent`  - початок виконання робочого процесу
- `WorkflowOutputEvent` - робочий процес генерує вихід
- `WorkflowErrorEvent` - робочий процес натрапив на помилку
- `ExecutorInvokeEvent`  - виконавець починає обробку
- `ExecutorCompleteEvent`  - виконавець завершує обробку
- `RequestInfoEvent` - надходить запит

## Розширені шаблони MAF

Вищевказані розділи охоплюють ключові концепції Microsoft Agent Framework. Коли ви створюєте більш складні агенти, розгляньте такі розширені шаблони:

- **Композиція middleware**: ланцюжте кілька обробників middleware (логування, авторизація, лімітування) за допомогою функціонального та чат-middleware для тонкого контролю поведінки агента.
- **Чекпоінти робочого процесу**: використовуйте події робочого процесу та серіалізацію для збереження й відновлення тривалих процесів агента.
- **Динамічний вибір інструментів**: комбінуйте RAG поверх описів інструментів з реєстрацією інструментів у MAF, щоб показувати лише релевантні інструменти для кожного запиту.
- **Передача між агентами (Multi-Agent Handoff)**: використовуйте крайові зв'язки робочого процесу та умовне маршрутування для оркестрації передач між спеціалізованими агентами.

## Приклади коду 

Приклади коду для Microsoft Agent Framework можна знайти в цьому репозиторії у файлах `xx-python-agent-framework` та `xx-dotnet-agent-framework`.

## Є ще питання щодо Microsoft Agent Framework?

Приєднуйтеся до [Microsoft Foundry Discord](https://aka.ms/ai-agents/discord), щоб зустрітися з іншими учнями, відвідати години консультацій і отримати відповіді на свої питання щодо AI-агентів.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
Відмова від відповідальності:
Цей документ було перекладено за допомогою сервісу машинного перекладу на базі штучного інтелекту Co‑op Translator (https://github.com/Azure/co-op-translator). Хоча ми прагнемо до точності, зверніть увагу, що автоматизовані переклади можуть містити помилки або неточності. Оригінальний документ мовою оригіналу слід вважати авторитетним джерелом. Для критично важливої інформації рекомендовано звернутися до професійного перекладача. Ми не несемо відповідальності за будь-які непорозуміння чи неправильні тлумачення, що виникли внаслідок використання цього перекладу.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->