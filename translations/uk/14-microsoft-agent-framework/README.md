# Вивчення Microsoft Agent Framework

![Agent Framework](../../../translated_images/uk/lesson-14-thumbnail.90df0065b9d234ee.webp)

### Вступ

У цьому уроці буде розглянуто:

- Розуміння Microsoft Agent Framework: Ключові особливості та цінність  
- Ознайомлення з основними поняттями Microsoft Agent Framework
- Просунуті шаблони MAF: Робочі процеси, проміжне програмне забезпечення та пам’ять

## Навчальні цілі

Після проходження цього уроку ви знатимете, як:

- Створювати AI-агентів, готових до виробництва, використовуючи Microsoft Agent Framework
- Застосовувати основні функції Microsoft Agent Framework у ваших агентських сценаріях
- Використовувати просунуті шаблони, включаючи робочі процеси, проміжне програмне забезпечення та спостережливість

## Приклади коду 

Приклади коду для [Microsoft Agent Framework (MAF)](https://aka.ms/ai-agents-beginners/agent-framework) можна знайти в цьому репозиторії у файлах `xx-python-agent-framework` та `xx-dotnet-agent-framework`.

## Розуміння Microsoft Agent Framework

![Framework Intro](../../../translated_images/uk/framework-intro.077af16617cf130c.webp)

[Microsoft Agent Framework (MAF)](https://aka.ms/ai-agents-beginners/agent-framework) — це єдина рамка Microsoft для створення AI-агентів. Вона пропонує гнучкість для вирішення широкого спектра агентських сценаріїв, що зустрічаються як у виробництві, так і в дослідницьких середовищах, зокрема:

- **Послідовне управління агентами** у випадках, коли потрібні покрокові робочі процеси.
- **Паралельне управління** у випадках, коли агенти мають виконувати завдання одночасно.
- **Управління груповим чатом** у випадках, коли агенти можуть спільно працювати над одним завданням.
- **Управління передачами** у випадках, коли агенти передають завдання один одному після завершення підзавдань.
- **Магнітне управління** у випадках, коли менеджер-агент створює та змінює список завдань і координує субагентів для виконання завдання.

Для впровадження AI-агентів у виробництві MAF також включає функції для:

- **Спостережливості** за допомогою OpenTelemetry, де кожна дія AI-агента, включно з викликом інструментів, кроками оркестрації, потоками міркувань та моніторингом продуктивності через панелі Microsoft Foundry.
- **Безпеки** шляхом розміщення агентів безпосередньо на Microsoft Foundry, що включає елементи контролю безпеки, такі як рольовий доступ, обробка приватних даних і вбудований захист контенту.
- **Надійності**, оскільки потоки агентів і робочі процеси можуть призупинятися, відновлюватися та відновлюватися після помилок, що забезпечує довготривалі процеси.
- **Керування**, підтримуючи робочі процеси із залученням людини, де завдання позначені як такі, що потребують схвалення людиною.

Microsoft Agent Framework також орієнтований на сумісність шляхом:

- **Будучи незалежним від хмари** — агенти можуть працювати в контейнерах, локально та в різних хмарах.
- **Будучи незалежним від провайдера** — агенти можуть створюватися через ваш улюблений SDK, включно з Azure OpenAI та OpenAI
- **Інтеграції відкритих стандартів** — агенти можуть використовувати протоколи, такі як Agent-to-Agent (A2A) і Model Context Protocol (MCP), щоб знаходити та використовувати інших агентів та інструменти.
- **Плагіни та конектори** — можна підключатися до сервісів даних і пам’яті, таких як Microsoft Fabric, SharePoint, Pinecone та Qdrant.

Давайте розглянемо, як ці функції застосовуються до деяких основних понять Microsoft Agent Framework.

## Ключові поняття Microsoft Agent Framework

### Агенти

![Agent Framework](../../../translated_images/uk/agent-components.410a06daf87b4fef.webp)

**Створення агентів**

Створення агента здійснюється шляхом визначення сервісу висновків (LLM Provider),  
набору інструкцій для AI-агента та призначеного `name`:


```python
agent = AzureOpenAIChatClient(credential=AzureCliCredential()).create_agent( instructions="You are good at recommending trips to customers based on their preferences.", name="TripRecommender" )
```

Вище використовується `Azure OpenAI`, але агенти можуть бути створені з використанням різноманітних сервісів, включно з `Microsoft Foundry Agent Service`:

```python
AzureAIAgentClient(async_credential=credential).create_agent( name="HelperAgent", instructions="You are a helpful assistant." ) as agent
```

OpenAI `Responses`, `ChatCompletion` API

```python
agent = OpenAIResponsesClient().create_agent( name="WeatherBot", instructions="You are a helpful weather assistant.", )
```

```python
agent = OpenAIChatClient().create_agent( name="HelpfulAssistant", instructions="You are a helpful assistant.", )
```

або [MiniMax](https://platform.minimaxi.com/), який надає сумісний з OpenAI API з великими контекстними вікнами (до 204К токенів):

```python
agent = OpenAIChatClient(base_url="https://api.minimax.io/v1", api_key=os.environ["MINIMAX_API_KEY"], model_id="MiniMax-M3").create_agent( name="HelpfulAssistant", instructions="You are a helpful assistant.", )
```

або віддалені агенти, що працюють з протоколом A2A:

```python
agent = A2AAgent( name=agent_card.name, description=agent_card.description, agent_card=agent_card, url="https://your-a2a-agent-host" )
```

**Запуск агентів**

Агенти запускаються за допомогою методів `.run` або `.run_stream` для отримання відповідей без потокової передачі або з нею відповідно.

```python
result = await agent.run("What are good places to visit in Amsterdam?")
print(result.text)
```

```python
async for update in agent.run_stream("What are the good places to visit in Amsterdam?"):
    if update.text:
        print(update.text, end="", flush=True)

```

Для кожного запуску агента також можна вказати параметри, наприклад, `max_tokens`, які використовує агент, `tools`, які агент може викликати, і навіть безпосередньо `model`, що використовується агентом.

Це корисно у випадках, коли потрібні конкретні моделі або інструменти для виконання завдання користувача.

**Інструменти**

Інструменти можна визначати як під час створення агента:

```python
def get_attractions( location: Annotated[str, Field(description="The location to get the top tourist attractions for")], ) -> str: """Get the top tourist attractions for a given location.""" return f"The top attractions for {location} are." 


# При безпосередньому створенні ChatAgent

agent = ChatAgent( chat_client=OpenAIChatClient(), instructions="You are a helpful assistant", tools=[get_attractions]

```

так і при запуску агента:

```python

result1 = await agent.run( "What's the best place to visit in Seattle?", tools=[get_attractions] # Інструмент надано лише для цього запуску )
```

**Потоки агента**

Потоки агентів використовуються для обробки багатокрокових розмов. Потоки можна створювати двома способами:

- Використанням `get_new_thread()`, що дозволяє зберігати потік з часом
- Автоматичне створення потоку під час запуску агента, який існує лише протягом поточного запуску.

Код для створення потоку виглядає так:

```python
# Створити новий потік.
thread = agent.get_new_thread() # Запустити агента з потоком.
response = await agent.run("Hello, I am here to help you book travel. Where would you like to go?", thread=thread)

```

Потім потік можна серіалізувати і зберегти для подальшого використання:

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

**Проміжне програмне забезпечення агента**

Агенти взаємодіють із інструментами та великими мовними моделями для виконання завдань користувача. У певних ситуаціях хочеться виконати або відстежити дії між цими взаємодіями. Проміжне програмне забезпечення агента дозволяє робити це за допомогою:

*Проміжного програмного забезпечення функцій*

Це проміжне програмне забезпечення дозволяє виконати дію між агентом і викликом функції чи інструменту. Приклад — ведення журналу виклику функції.

У коді нижче `next` визначає, чи слід викликати наступне проміжне ПЗ або безпосередньо функцію.

```python
async def logging_function_middleware(
    context: FunctionInvocationContext,
    next: Callable[[FunctionInvocationContext], Awaitable[None]],
) -> None:
    """Function middleware that logs function execution."""
    # Попередня обробка: журналювання перед виконанням функції
    print(f"[Function] Calling {context.function.name}")

    # Продовжити до наступного middleware або виконання функції
    await next(context)

    # Пост-обробка: журналювання після виконання функції
    print(f"[Function] {context.function.name} completed")
```

*Чат-проміжне програмне забезпечення*

Це проміжне ПЗ дозволяє виконати або зафіксувати дію між агентом і запитами між великими мовними моделями.

Воно містить важливу інформацію, таку як `messages`, що надсилаються до AI-сервісу.

```python
async def logging_chat_middleware(
    context: ChatContext,
    next: Callable[[ChatContext], Awaitable[None]],
) -> None:
    """Chat middleware that logs AI interactions."""
    # Попередня обробка: Логування перед викликом ШІ
    print(f"[Chat] Sending {len(context.messages)} messages to AI")

    # Продовжити до наступного проміжного програмного забезпечення або сервісу ШІ
    await next(context)

    # Постобробка: Логування після відповіді ШІ
    print("[Chat] AI response received")

```

**Пам’ять агента**

Як було розглянуто у уроці `Agentic Memory`, пам’ять є важливим елементом для забезпечення роботи агента у різних контекстах. MAF пропонує кілька типів пам’яті:

*Пам’ять в оперативній пам’яті*

Це пам’ять, що зберігається в потоках під час роботи застосунку.

```python
# Створити новий потік.
thread = agent.get_new_thread() # Запустити агента з потоком.
response = await agent.run("Hello, I am here to help you book travel. Where would you like to go?", thread=thread)
```

*Постійні повідомлення*

Ця пам’ять використовується для збереження історії розмов між сесіями. Визначається за допомогою `chat_message_store_factory`:

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

*Динамічна пам’ять*

Ця пам’ять додається до контексту перед запуском агента. Вона може зберігатися у зовнішніх сервісах, таких як mem0:

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


Наблюваність важлива для створення надійних та підтримуваних агентських систем. MAF інтегрується з OpenTelemetry для забезпечення трасування та лічильників для кращої наблюваності.

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

MAF пропонує робочі процеси, які є попередньо визначеними кроками для виконання завдання і включають AI-агентів як компоненти цих кроків.

Робочі процеси складаються з різних компонентів, що дозволяють кращий контроль потоку. Робочі процеси також забезпечують **оркестрацію з кількома агентами** та **контрольні точки** для збереження станів робочих процесів.

Основні компоненти робочого процесу:

**Виконавці**

Виконавці отримують вхідні повідомлення, виконують призначені завдання, а потім виробляють вихідне повідомлення. Це рухає робочий процес вперед до завершення більшого завдання. Виконавці можуть бути як AI-агентами, так і користувацькою логікою.

**Ребра**

Ребра використовуються для визначення потоку повідомлень у робочому процесі. Вони можуть бути:

*Прямі ребра* - прості одно-до-одного з'єднання між виконавцями:

```python
from agent_framework import WorkflowBuilder

builder = WorkflowBuilder()
builder.add_edge(source_executor, target_executor)
builder.set_start_executor(source_executor)
workflow = builder.build()
```

*Умовні ребра* - активуються після виконання певної умови. Наприклад, коли готельні номери недоступні, виконавець може запропонувати інші варіанти.

*Ребра з вибором (switch-case)* - маршрутизують повідомлення до різних виконавців на основі визначених умов. Наприклад, якщо клієнт подорожі має пріоритетний доступ, їхні завдання будуть оброблятися через інший робочий процес.

*Ребра розгалуження (fan-out)* - надсилають одне повідомлення до кількох цілей.

*Ребра збору (fan-in)* - збирають кілька повідомлень від різних виконавців і надсилають на одну ціль.

**Події**

Для кращої наблюваності робочих процесів MAF пропонує вбудовані події виконання, які включають:

- `WorkflowStartedEvent`  - Початок виконання робочого процесу
- `WorkflowOutputEvent` - Робочий процес генерує вихідні дані
- `WorkflowErrorEvent` - Робочий процес зустрів помилку
- `ExecutorInvokeEvent`  - Запуск обробки виконавцем
- `ExecutorCompleteEvent`  - Завершення обробки виконавцем
- `RequestInfoEvent` - Відправлено запит

## Розширені патерни MAF

Вище описані ключові концепції Microsoft Agent Framework. Коли ви будуєте складніших агентів, розгляньте ці розширені патерни:

- **Композиція проміжного програмного забезпечення (middleware)**: об’єднання кількох обробників middleware (логування, автентифікація, обмеження швидкості) за допомогою функціонального і чат middleware для тонкого контролю поведінки агента.
- **Контрольні точки робочих процесів**: використання подій робочого процесу та серіалізації для збереження та відновлення довготривалих процесів агентів.
- **Динамічний вибір інструментів**: поєднання RAG на основі описів інструментів з реєстрацією інструментів у MAF для подання лише релевантних інструментів за запитом.
- **Передача між кількома агентами**: використання ребер робочих процесів і умовного маршрутування для оркестрації передачі між спеціалізованими агентами.

## Розміщення агентів LangChain / LangGraph у Microsoft Foundry

Microsoft Agent Framework є **інтероперабельним фреймворком** — ви не обмежені агентами, створеними з MAF. Якщо у вас вже є агент, побудований з **LangChain** або **LangGraph**, ви можете запустити його як **розміщеного агента Microsoft Foundry**, щоб Foundry керував виконанням, сесіями, масштабуванням, ідентичністю та кінцевими точками протоколу, в той час як логіка агента лишається в LangGraph.

Це зроблено за допомогою пакету `langchain_azure_ai.agents.hosting`, який надає скомпільований граф LangGraph через ті ж протоколи, що використовують розміщені агенти Foundry.

**1. Встановіть додатковий пакет hosting:**

```bash
pip install -U "langchain-azure-ai[hosting]>=1.2.4" azure-identity
```

Додаток `hosting` встановлює бібліотеки протоколу Foundry: `azure-ai-agentserver-responses` (сумісний з OpenAI кінцевий пункт `/responses`) та `azure-ai-agentserver-invocations` (узагальнений кінцевий пункт `/invocations`).

**2. Оберіть протокол хостингу:**

| Протокол | Клас хоста | Кінцева точка | Використання |
|----------|-----------|----------|----------|
| **Responses** | `ResponsesHostServer` | `/responses` | Ви хочете чат, потокову передачу, історію відповідей і теми розмов сумісні з OpenAI — рекомендований за замовчуванням для розмовних агентів. |
| **Invocations** | `InvocationsHostServer` | `/invocations` | Вам потрібна користувацька структура JSON, API у стилі webhook, або неконверсаційна обробка. |

Оскільки **Responses API є основним API для агент-стильного розвитку в Foundry**, починайте з `ResponsesHostServer` для більшості агентів.

**3. Налаштуйте змінні середовища** (`az login` спочатку, щоб `DefaultAzureCredential` міг автентифікуватися):

```bash
export FOUNDRY_PROJECT_ENDPOINT="https://<resource>.services.ai.azure.com/api/projects/<project>"
export FOUNDRY_MODEL_NAME="gpt-4.1"
```

Коли агент пізніше запускатиметься як розміщений агент у Foundry, платформа автоматично вставляє `FOUNDRY_PROJECT_ENDPOINT`.

**4. Експортуйте агента LangGraph через протокол Responses:**

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

    # ChatOpenAI тут орієнтується на сумісний з OpenAI (Responses) кінцевий пункт проєкту Foundry.
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

**Ключові поведінкові властивості:**

- **Розмови**: Клієнти продовжують розмову, передаючи `previous_response_id` або `conversation` ID. Якщо граф скомпільовано з LangGraph checkpoint, Foundry зберігає стан розмови у контрольній точці (для продакшену використовуйте надійний checkpoint; `MemorySaver` підходить для локального тестування).
- **Людина в циклі**: Якщо граф використовує LangGraph `interrupt()`, `ResponsesHostServer` відображає очікуване переривання як Responses елемент `function_call` / `mcp_approval_request`, і клієнти відновлюють із відповіддю `function_call_output` / `mcp_approval_response`.
- **Розгортання в Foundry**: Використовуйте Azure Developer CLI — `azd ext install azure.ai.agents`, `azd ai agent init -m <manifest>`, `azd ai agent run` (локально, потрібен Docker), потім `azd provision` і `azd deploy`. Розгортання розміщених агентів вимагає ролі **Foundry Project Manager**.

Запускаюча версія цього прикладу знаходиться у [code-samples/14-langchain-hosted-agent.py](../../../14-microsoft-agent-framework/code-samples/14-langchain-hosted-agent.py). Для повного керівництва (протокол Invocations, користувацькі схеми запитів і усунення помилок) дивіться [Host LangGraph agents as Foundry hosted agents](https://learn.microsoft.com/azure/foundry/how-to/develop/langchain-hosted-agents).

## Приклади коду 

Приклади коду для Microsoft Agent Framework можна знайти у цьому репозиторії у файлах `xx-python-agent-framework` та `xx-dotnet-agent-framework`.

## Маєте більше запитань щодо Microsoft Agent Framework?

Приєднуйтесь до [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D), щоб зустрітися з іншими учасниками, відвідати консультації та отримати відповіді на запитання про AI-агентів.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Відмова від відповідальності**:
Цей документ було перекладено за допомогою сервісу штучного інтелекту для перекладу [Co-op Translator](https://github.com/Azure/co-op-translator). Хоча ми прагнемо до точності, будь ласка, майте на увазі, що автоматичні переклади можуть містити помилки або неточності. Оригінальний документ рідною мовою слід вважати авторитетним джерелом. Для критично важливої інформації рекомендується професійний людський переклад. Ми не несемо відповідальності за будь-які непорозуміння або неправильні тлумачення, що виникли внаслідок використання цього перекладу.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->