# Вивчення Microsoft Agent Framework

![Agent Framework](../../../translated_images/uk/lesson-14-thumbnail.90df0065b9d234ee.webp)

### Вступ

У цьому уроці буде розглянуто:

- Розуміння Microsoft Agent Framework: ключові особливості та цінність  
- Ознайомлення з основними поняттями Microsoft Agent Framework
- Розширені шаблони MAF: робочі процеси, проміжне програмне забезпечення та пам’ять

## Цілі навчання

Після проходження цього уроку ви знатимете, як:

- Створювати готових до виробництва AI агентів за допомогою Microsoft Agent Framework
- Застосовувати основні функції Microsoft Agent Framework до ваших агентських випадків використання
- Використовувати розширені шаблони, включаючи робочі процеси, проміжне програмне забезпечення та спостережуваність

## Приклади коду

Приклади коду для [Microsoft Agent Framework (MAF)](https://aka.ms/ai-agents-beginners/agent-framework) можна знайти в цьому репозиторії у файлах `xx-python-agent-framework` та `xx-dotnet-agent-framework`.

## Розуміння Microsoft Agent Framework

![Framework Intro](../../../translated_images/uk/framework-intro.077af16617cf130c.webp)

[Microsoft Agent Framework (MAF)](https://aka.ms/ai-agents-beginners/agent-framework) — це уніфікована платформа Microsoft для створення AI агентів. Вона пропонує гнучкість для вирішення широкого спектру агентських випадків використання, які зустрічаються як у виробництві, так і в дослідницьких середовищах, включаючи:

- **Послідовну оркестрацію агентів** у сценаріях, де потрібні покрокові робочі процеси.
- **Паралельну оркестрацію** у сценаріях, де агенти повинні виконувати завдання одночасно.
- **Оркестрацію групового чату** у сценаріях, де агенти можуть спільно працювати над одним завданням.
- **Оркестрацію передачі завдань** у сценаріях, де агенти передають завдання один одному по мірі виконання підзавдань.
- **Магнітну оркестрацію** у сценаріях, де агент-менеджер створює та змінює список завдань і координує підлеглих агентів для їх виконання.

Для забезпечення AI агентів у виробництві MAF також включає функції для:

- **Спостережуваності** через використання OpenTelemetry, де кожна дія AI агента, включаючи виклик інструментів, кроки оркестрації, розумові процеси та моніторинг продуктивності через панелі Microsoft Foundry.
- **Безпеки** за рахунок розміщення агентів нативно в Microsoft Foundry, що включає контроль доступу на основі ролей, обробку конфіденційних даних і вбудований захист від небажаного контенту.
- **Стійкості** оскільки потоки агентів і робочі процеси можуть призупинятися, відновлюватись та відновлюватись після помилок, що дозволяє тривале виконання процесів.
- **Керування** через підтримку робочих процесів із участю людини, де завдання позначаються як такі, що потребують підтвердження людиною.

Microsoft Agent Framework також орієнтований на взаємодію з іншими системами за рахунок:

- **Незалежності від хмарних платформ** - агенти можуть працювати у контейнерах, локально та в різних хмарах.
- **Незалежності від провайдерів** - агенти можуть створюватись через улюблені SDK, включно з Azure OpenAI та OpenAI.
- **Інтеграції відкритих стандартів** - агенти можуть використовувати протоколи, такі як Agent-to-Agent (A2A) та Model Context Protocol (MCP) для пошуку й використання інших агентів та інструментів.
- **Плагіни та конектори** - можуть підключатися до служб даних і пам’яті, таких як Microsoft Fabric, SharePoint, Pinecone і Qdrant.

Розглянемо, як ці функції застосовуються до деяких основних понять Microsoft Agent Framework.

## Основні поняття Microsoft Agent Framework

### Агенти

![Agent Framework](../../../translated_images/uk/agent-components.410a06daf87b4fef.webp)

**Створення агентів**

Створення агента здійснюється шляхом визначення служби виведення (провайдера LLM),
набору інструкцій для AI агента і призначеної `name`:

```python
agent = AzureOpenAIChatClient(credential=AzureCliCredential()).create_agent( instructions="You are good at recommending trips to customers based on their preferences.", name="TripRecommender" )
```

Наведено приклад із використанням `Azure OpenAI`, однак агенти можуть створюватись із використанням різних служб, включаючи `Microsoft Foundry Agent Service`:

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

або [MiniMax](https://platform.minimaxi.com/), який надає сумісний з OpenAI API з великими контекстними вікнами (до 204 тис. токенів):

```python
agent = OpenAIChatClient(base_url="https://api.minimax.io/v1", api_key=os.environ["MINIMAX_API_KEY"], model_id="MiniMax-M3").create_agent( name="HelpfulAssistant", instructions="You are a helpful assistant.", )
```

або віддалені агенти, що працюють за протоколом A2A:

```python
agent = A2AAgent( name=agent_card.name, description=agent_card.description, agent_card=agent_card, url="https://your-a2a-agent-host" )
```

**Запуск агентів**

Агенти запускаються з використанням методів `.run` або `.run_stream` для відповідно не потокових або потокових відповідей.

```python
result = await agent.run("What are good places to visit in Amsterdam?")
print(result.text)
```

```python
async for update in agent.run_stream("What are the good places to visit in Amsterdam?"):
    if update.text:
        print(update.text, end="", flush=True)

```

Кожен запуск агента може мати опції налаштування параметрів, таких як `max_tokens`, які використовує агент, `tools`, які агент може викликати, та навіть безпосередньо `model`, що використовується для агента.

Це корисно у випадках, коли для виконання завдання користувача потрібні конкретні моделі або інструменти.

**Інструменти**

Інструменти можна визначати як при створенні агента:

```python
def get_attractions( location: Annotated[str, Field(description="The location to get the top tourist attractions for")], ) -> str: """Get the top tourist attractions for a given location.""" return f"The top attractions for {location} are." 


# При безпосередньому створенні ChatAgent

agent = ChatAgent( chat_client=OpenAIChatClient(), instructions="You are a helpful assistant", tools=[get_attractions]

```

так і під час запуску агента:

```python

result1 = await agent.run( "What's the best place to visit in Seattle?", tools=[get_attractions] # Інструмент надається лише для цього запуску )
```

**Потоки агента**

Потоки агента використовуються для обробки діалогів із кількома циклами. Потоки можуть створюватись:

- Використанням `get_new_thread()`, що дозволяє зберігати потік із часом
- Автоматичним створенням потоку при запуску агента, при цьому потік існує лише під час поточного запуску.

Код для створення потоку виглядає так:

```python
# Створіть новий потік.
thread = agent.get_new_thread() # Запустіть агента з потоком.
response = await agent.run("Hello, I am here to help you book travel. Where would you like to go?", thread=thread)

```

Потім потік можна серіалізувати для збереження і подальшого використання:

```python
# Створити новий потік.
thread = agent.get_new_thread() 

# Запустити агента разом з потоком.

response = await agent.run("Hello, how are you?", thread=thread) 

# Серіалізувати потік для збереження.

serialized_thread = await thread.serialize() 

# Десеріалізувати стан потоку після завантаження з сховища.

resumed_thread = await agent.deserialize_thread(serialized_thread)
```

**Проміжне програмне забезпечення агента**

Агенти взаємодіють з інструментами та LLM для виконання завдань користувача. У певних випадках ми хочемо виконувати або відслідковувати дії між цими взаємодіями. Проміжне ПЗ агента дозволяє це робити через:

*Проміжне ПЗ для функцій*

Це проміжне ПЗ дозволяє виконати дію між агентом і функцією/інструментом, який викликається. Прикладом такого використання може бути логування виклику функції.

У коді нижче `next` визначає, чи слід викликати наступне проміжне ПЗ або безпосередньо функцію.

```python
async def logging_function_middleware(
    context: FunctionInvocationContext,
    next: Callable[[FunctionInvocationContext], Awaitable[None]],
) -> None:
    """Function middleware that logs function execution."""
    # Попередня обробка: Журналювання перед виконанням функції
    print(f"[Function] Calling {context.function.name}")

    # Продовжити до наступного проміжного програмного забезпечення або виконання функції
    await next(context)

    # Постобробка: Журналювання після виконання функції
    print(f"[Function] {context.function.name} completed")
```

*Проміжне ПЗ для чату*

Це проміжне ПЗ дозволяє виконати або зафіксувати дію між агентом і запитами між LLM.

Воно містить важливу інформацію, таку як `messages`, що відправляються до AI-служби.

```python
async def logging_chat_middleware(
    context: ChatContext,
    next: Callable[[ChatContext], Awaitable[None]],
) -> None:
    """Chat middleware that logs AI interactions."""
    # Попередня обробка: Запис у журнал перед викликом ШІ
    print(f"[Chat] Sending {len(context.messages)} messages to AI")

    # Продовжити до наступного проміжного програмного забезпечення або сервісу ШІ
    await next(context)

    # Постобробка: Запис у журнал після відповіді ШІ
    print("[Chat] AI response received")

```

**Пам'ять агента**

Як було розглянуто в уроці «Agentic Memory», пам’ять є важливим елементом, що дозволяє агенту працювати з різними контекстами. MAF пропонує кілька типів пам’яті:

*Пам’ять у оперативній пам’яті*

Це пам’ять, що зберігається в потоках під час роботи додатку.

```python
# Створити новий потік.
thread = agent.get_new_thread() # Запустити агента з потоком.
response = await agent.run("Hello, I am here to help you book travel. Where would you like to go?", thread=thread)
```

*Постійні повідомлення*

Ця пам’ять використовується для збереження історії розмови між різними сесіями. Визначається через `chat_message_store_factory`:

```python
from agent_framework import ChatMessageStore

# Створити власне сховище повідомлень
def create_message_store():
    return ChatMessageStore()

agent = ChatAgent(
    chat_client=OpenAIChatClient(),
    instructions="You are a Travel assistant.",
    chat_message_store_factory=create_message_store
)

```

*Динамічна пам’ять*

Ця пам’ять додається до контексту перед запуском агентів. Ці пам’яті можуть зберігатися у зовнішніх службах, таких як mem0:

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

Спостережуваність важлива для створення надійних і підтримуваних агентських систем. MAF інтегрується з OpenTelemetry для забезпечення трасування і метрик для кращої спостережуваності.

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

MAF пропонує робочі процеси як попередньо визначені кроки для виконання завдання, включаючи AI агентів як компоненти цих кроків.

Робочі процеси складаються з різних компонентів, які забезпечують кращий контроль потоку. Робочі процеси також підтримують **оркестрацію кількох агентів** та **створення контрольних точок** для збереження станів робочого процесу.

Основні компоненти робочого процесу:

**Виконавці**

Виконавці отримують вхідні повідомлення, виконують призначені завдання і створюють вихідне повідомлення. Це просуває робочий процес до виконання більшого завдання. Виконавцями можуть бути AI агенти або кастомна логіка.

**Ребра**

Ребра використовуються для визначення потоку повідомлень у робочому процесі. Вони можуть бути:

*Прямі ребра* — прості одно-на-один з’єднання між виконавцями:

```python
from agent_framework import WorkflowBuilder

builder = WorkflowBuilder()
builder.add_edge(source_executor, target_executor)
builder.set_start_executor(source_executor)
workflow = builder.build()
```

*Умовні ребра* — активуються після виконання певної умови. Наприклад, коли номери в готелях відсутні, виконавець може запропонувати інші варіанти.

*Ребра типу switch-case* — направляють повідомлення до різних виконавців залежно від визначених умов. Наприклад, якщо у клієнта подорожі є пріоритетний доступ, їхні завдання обробляються через інший робочий процес.

*Ребра Fan-out* — надсилають одне повідомлення до кількох цілей.

*Ребра Fan-in* — збирають кілька повідомлень від різних виконавців і надсилають одному адресату.

**Події**

Для забезпечення кращої спостережуваності робочих процесів MAF пропонує вбудовані події для виконання, включаючи:

- `WorkflowStartedEvent`  - Початок виконання робочого процесу
- `WorkflowOutputEvent` - Робочий процес створює вихідні дані
- `WorkflowErrorEvent` - Помилка у робочому процесі
- `ExecutorInvokeEvent`  - Виконавець починає обробку
- `ExecutorCompleteEvent`  -  Виконавець завершує обробку
- `RequestInfoEvent` - Відправлено запит

## Розширені шаблони MAF

Вище наведено основні поняття Microsoft Agent Framework. При створенні складніших агентів варто розглянути такі розширені шаблони:

- **Композиція проміжного ПЗ**: ланцюжок кількох обробників проміжного ПЗ (логування, автентифікація, обмеження швидкості) з використанням функціонального та чат-проміжного ПЗ для тонкого керування поведінкою агента.
- **Створення контрольних точок робочих процесів**: використання подій робочого процесу та серіалізації для збереження та відновлення тривалих процесів агента.
- **Динамічний вибір інструментів**: поєднання RAG над описами інструментів із реєстрацією інструментів MAF для представлення лише релевантних інструментів на запит.
- **Передача завдань між кількома агентами**: використання ребер робочого процесу і умовного маршрутизу для координації передачі між спеціалізованими агентами.

## Розміщення LangChain / LangGraph агентів на Microsoft Foundry

Microsoft Agent Framework є **інтероперабельним** — ви не обмежені агентами, написаними за допомогою MAF. Якщо у вас вже є агент, створений за допомогою **LangChain** або **LangGraph**, ви можете запустити його як **розміщеного агента Microsoft Foundry**, щоб Foundry керував часом виконання, сесіями, масштабуванням, ідентичністю та кінцевими точками протоколів, тоді як ваша логіка агента залишатиметься у LangGraph.

Це реалізовано за допомогою пакету `langchain_azure_ai.agents.hosting`, який експонує скомпільований граф LangGraph через ті ж протоколи, що і агенти Foundry.

**1. Встановіть додаткові компоненти для хостингу:**

```bash
pip install -U "langchain-azure-ai[hosting]>=1.2.4" azure-identity
```

Додатковий пакет `hosting` встановлює бібліотеки протоколів Foundry: `azure-ai-agentserver-responses` (сумісна з OpenAI кінцева точка `/responses`) і `azure-ai-agentserver-invocations` (загальна кінцева точка `/invocations`).

**2. Виберіть протокол хостингу:**

| Протокол | Клас хоста | Кінцева точка | Використовуйте коли |
|----------|-----------|----------|----------|
| **Responses** | `ResponsesHostServer` | `/responses` | Хочете чат, потокову передачу, історію відповідей і ведення розмов сумісні з OpenAI — рекомендований варіант для розмовних агентів. |
| **Invocations** | `InvocationsHostServer` | `/invocations` | Потрібен власний JSON-формат, точка webhook або неконверсійна обробка. |

Оскільки **API Responses є основним API для розвитку агентів у Foundry**, починайте з `ResponsesHostServer` для більшості агентів.

**3. Налаштуйте змінні середовища** (`az login` спочатку, щоб `DefaultAzureCredential` міг аутентифікуватися):

```bash
export FOUNDRY_PROJECT_ENDPOINT="https://<resource>.services.ai.azure.com/api/projects/<project>"
export FOUNDRY_MODEL_NAME="gpt-5-mini"
```

Коли агент пізніше працюватиме як розміщений агент у Foundry, платформа автоматично інджектує `FOUNDRY_PROJECT_ENDPOINT`.

**4. Експонуйте агента LangGraph через протокол Responses:**

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

    # ChatOpenAI тут орієнтується на сумісну з OpenAI кінцеву точку (Responses) проекту Foundry.
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

Запустіть локально за допомогою `python main.py`, потім надішліть запит Responses на `http://localhost:8088/responses`.

**Ключові особливості:**

- **Розмови**: клієнти продовжують розмову, передаючи `previous_response_id` або ID `conversation`. Якщо ваш граф скомпільовано з використанням контрольної точки LangGraph, Foundry ключує стан розмови відповідно до контрольної точки (використовуйте стійкий чекпоінтер у виробництві; `MemorySaver` корисний для локального тестування).
- **Людина в циклі**: Якщо ваш граф використовує LangGraph `interrupt()`, `ResponsesHostServer` відображає очікуваний перерив як елемент Responses `function_call` / `mcp_approval_request`, і клієнти продовжують із відповіддю `function_call_output` / `mcp_approval_response`.
- **Розгортання у Foundry**: Використовуйте Azure Developer CLI — `azd ext install azure.ai.agents`, `azd ai agent init -m <manifest>`, `azd ai agent run` (локально, потребує Docker), потім `azd provision` та `azd deploy`. Для розгортання розміщених агентів потрібна роль **Foundry Project Manager**.

Рабоча версія цього прикладу доступна у [code-samples/14-langchain-hosted-agent.py](../../../14-microsoft-agent-framework/code-samples/14-langchain-hosted-agent.py). Повний посібник (протокол Invocations, персоналізовані схеми запитів і усунення несправностей) дивіться у [Host LangGraph agents as Foundry hosted agents](https://learn.microsoft.com/azure/foundry/how-to/develop/langchain-hosted-agents).

## Приклади коду

Приклади коду для Microsoft Agent Framework можна знайти в цьому репозиторії у файлах `xx-python-agent-framework` та `xx-dotnet-agent-framework`.

## Маєте додаткові питання про Microsoft Agent Framework?

Приєднуйтесь до [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D), щоб поспілкуватись з іншими учнями, відвідати години консультацій та отримати відповіді на питання про AI агентів.
## Попередній урок

[Пам’ять для AI агентів](../13-agent-memory/README.md)

## Наступний урок

[Створення агентів для використання комп’ютера (CUA)](../15-browser-use/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Відмова від відповідальності**:
Цей документ було перекладено за допомогою сервісу штучного інтелекту для перекладу [Co-op Translator](https://github.com/Azure/co-op-translator). Хоча ми прагнемо до точності, будь ласка, майте на увазі, що автоматичні переклади можуть містити помилки або неточності. Оригінальний документ рідною мовою слід вважати авторитетним джерелом. Для критично важливої інформації рекомендується професійний людський переклад. Ми не несемо відповідальності за будь-які непорозуміння або неправильні тлумачення, що виникли внаслідок використання цього перекладу.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->