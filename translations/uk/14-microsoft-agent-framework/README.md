# Дослідження Microsoft Agent Framework

![Agent Framework](../../../translated_images/uk/lesson-14-thumbnail.90df0065b9d234ee.webp)

### Вступ

У цьому уроці буде розглянуто:

- Розуміння Microsoft Agent Framework: Ключові особливості та цінність  
- Дослідження основних концепцій Microsoft Agent Framework
- Розширені шаблони MAF: Робочі процеси, посередники та пам'ять

## Цілі навчання

Після цього уроку ви знатимете, як:

- Створювати готових до виробництва AI агентів за допомогою Microsoft Agent Framework
- Застосовувати основні функції Microsoft Agent Framework до ваших агентних сценаріїв використання
- Використовувати розширені шаблони, включаючи робочі процеси, посередників та нагляд

## Приклади коду 

Приклади коду для [Microsoft Agent Framework (MAF)](https://aka.ms/ai-agents-beginners/agent-framework) можна знайти в цьому репозиторії у файлах `xx-python-agent-framework` і `xx-dotnet-agent-framework`.

## Розуміння Microsoft Agent Framework

![Framework Intro](../../../translated_images/uk/framework-intro.077af16617cf130c.webp)

[Microsoft Agent Framework (MAF)](https://aka.ms/ai-agents-beginners/agent-framework) — це уніфіковане середовище Microsoft для створення AI агентів. Воно пропонує гнучкість для вирішення широкого кола агентних сценаріїв використання, які зустрічаються як у виробничих, так і в науково-дослідних середовищах, включно з:

- **Покроковою оркестрацією агентів** у сценаріях, де потрібні послідовні робочі процеси.
- **Паралельною оркестрацією** у випадках, коли агенти повинні виконувати завдання одночасно.
- **Оркестрацією групового чату** у випадках, коли агенти можуть співпрацювати над одним завданням.
- **Оркестрацією передачі** у випадках, коли агенти передають завдання один одному по мірі виконання підзавдань.
- **Магнітною оркестрацією**, коли агент-менеджер створює та змінює список завдань і координує субагентів для виконання завдання.

Для розгортання AI агентів у виробництві, MAF також включає можливості для:

- **Нагляду** за допомогою OpenTelemetry, де кожна дія AI агента, включно з викликом інструментів, кроками оркестрації, логікою ухвалення рішень та моніторингом продуктивності через панелі Microsoft Foundry.
- **Безпеки** шляхом розміщення агентів безпосередньо на Microsoft Foundry, що включає контролі безпеки, такі як керування доступом на основі ролей, обробка приватних даних та вбудований захист контенту.
- **Надійності** – оскільки потоки агентів і робочі процеси можуть паузуватися, відновлюватися та виправляти помилки, що дозволяє виконувати тривалі процеси.
- **Контролю**, бо підтримуються робочі процеси з участю людини, де завдання позначені як ті, що потребують затвердження людиною.

Microsoft Agent Framework також орієнтований на взаємодію з іншими системами:

- **Незалежність від хмарної платформи** – агенти можуть працювати в контейнерах, локально та на різних хмарах.
- **Незалежність від провайдера** – агенти можуть бути створені з використанням вашого улюбленого SDK, включно з Azure OpenAI та OpenAI.
- **Інтеграція відкритих стандартів** – агенти можуть використовувати протоколи, такі як Agent-to-Agent (A2A) та Model Context Protocol (MCP), для пошуку і використання інших агентів та інструментів.
- **Плагіни та конектори** – підключення до сервісів даних і пам’яті, таких як Microsoft Fabric, SharePoint, Pinecone і Qdrant.

Розглянемо, як ці функції застосовуються до основних концепцій Microsoft Agent Framework.

## Ключові концепції Microsoft Agent Framework

### Агенти

![Agent Framework](../../../translated_images/uk/agent-components.410a06daf87b4fef.webp)

**Створення агентів**

Створення агента здійснюється шляхом визначення сервісу висновку (провайдера LLM),
набору інструкцій для AI агента та присвоєння `name`:

```python
agent = AzureOpenAIChatClient(credential=AzureCliCredential()).create_agent( instructions="You are good at recommending trips to customers based on their preferences.", name="TripRecommender" )
```

Наведене вище приклад використовує `Azure OpenAI`, але агенти можуть бути створені з використанням різних сервісів, включно з `Microsoft Foundry Agent Service`:

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

або [MiniMax](https://platform.minimaxi.com/), який надає OpenAI-сумісний API з великими контекстними вікнами (до 204К токенів):

```python
agent = OpenAIChatClient(base_url="https://api.minimax.io/v1", api_key=os.environ["MINIMAX_API_KEY"], model_id="MiniMax-M3").create_agent( name="HelpfulAssistant", instructions="You are a helpful assistant.", )
```

або віддалені агенти, які працюють за протоколом A2A:

```python
agent = A2AAgent( name=agent_card.name, description=agent_card.description, agent_card=agent_card, url="https://your-a2a-agent-host" )
```

**Запуск агентів**

Агенти запускаються за допомогою методів `.run` або `.run_stream` для відповідей без трансляції або з трансляцією.

```python
result = await agent.run("What are good places to visit in Amsterdam?")
print(result.text)
```

```python
async for update in agent.run_stream("What are the good places to visit in Amsterdam?"):
    if update.text:
        print(update.text, end="", flush=True)

```

Кожен запуск агента також може мати параметри для налаштування таких параметрів, як `max_tokens`, інструменти `tools`, які агент може викликати, та навіть сама модель `model`, що використовується агентом.

Це корисно у випадках, коли для виконання завдання користувача потрібні певні моделі або інструменти.

**Інструменти**

Інструменти можна визначати як при створенні агента:

```python
def get_attractions( location: Annotated[str, Field(description="The location to get the top tourist attractions for")], ) -> str: """Get the top tourist attractions for a given location.""" return f"The top attractions for {location} are." 


# При безпосередньому створенні ChatAgent

agent = ChatAgent( chat_client=OpenAIChatClient(), instructions="You are a helpful assistant", tools=[get_attractions]

```

так і під час запуску агента:

```python

result1 = await agent.run( "What's the best place to visit in Seattle?", tools=[get_attractions] # Інструмент надано лише для цього запуску )
```

**Потоки агента**

Потоки агента використовуються для обробки діалогів у кілька кроків. Потоки можна створювати:

- Використанням `get_new_thread()`, що дозволяє зберігати потік протягом часу
- Автоматичним створенням потоку під час запуску агента, такий потік триватиме лише під час поточного запуску.

Для створення потоку код виглядає так:

```python
# Створити новий потік.
thread = agent.get_new_thread() # Запустити агента з потоком.
response = await agent.run("Hello, I am here to help you book travel. Where would you like to go?", thread=thread)

```

Потім можна серіалізувати потік для подальшого збереження:

```python
# Створити новий потік.
thread = agent.get_new_thread() 

# Запустити агента з потоком.

response = await agent.run("Hello, how are you?", thread=thread) 

# Серіалізувати потік для збереження.

serialized_thread = await thread.serialize() 

# Десеріалізувати стан потоку після завантаження з пам'яті.

resumed_thread = await agent.deserialize_thread(serialized_thread)
```

**Проміжне програмне забезпечення агента (Middleware)**

Агенти взаємодіють з інструментами та LLM для виконання завдань користувача. У певних сценаріях ми хочемо виконувати чи відстежувати дії між цими взаємодіями. Middleware агента дозволяє це робити через:

*Middleware функцій*

Цей middleware дає змогу виконати дію між агентом та функцією/інструментом, який він викликає. Приклад використання – логування виклику функції.

У коді нижче `next` визначає, чи слід викликати наступний middleware або фактичну функцію.

```python
async def logging_function_middleware(
    context: FunctionInvocationContext,
    next: Callable[[FunctionInvocationContext], Awaitable[None]],
) -> None:
    """Function middleware that logs function execution."""
    # Попередня обробка: Логування перед виконанням функції
    print(f"[Function] Calling {context.function.name}")

    # Продовжити до наступного проміжного програмного забезпечення або виконання функції
    await next(context)

    # Постобробка: Логування після виконання функції
    print(f"[Function] {context.function.name} completed")
```

*Middleware чату*

Цей middleware дозволяє виконувати або записувати дію між агентом та запитами до LLM.

Він містить важливу інформацію, таку як `messages`, що надсилаються до AI сервісу.

```python
async def logging_chat_middleware(
    context: ChatContext,
    next: Callable[[ChatContext], Awaitable[None]],
) -> None:
    """Chat middleware that logs AI interactions."""
    # Попередня обробка: журнал перед викликом AI
    print(f"[Chat] Sending {len(context.messages)} messages to AI")

    # Продовжити до наступного проміжного програмного забезпечення або AI сервісу
    await next(context)

    # Постобробка: журнал після відповіді AI
    print("[Chat] AI response received")

```

**Пам’ять агента**

Як розглянуто в уроці `Agentic Memory`, пам’ять – важливий елемент для роботи агента в різних контекстах. MAF пропонує кілька типів пам’яті:

*Пам’ять у оперативній пам’яті*

Це пам’ять, що зберігається у потоках під час роботи додатку.

```python
# Створити новий потік.
thread = agent.get_new_thread() # Запустити агента з потоком.
response = await agent.run("Hello, I am here to help you book travel. Where would you like to go?", thread=thread)
```

*Постійні повідомлення*

Ця пам’ять використовується для збереження історії розмов між сесіями. Визначається через `chat_message_store_factory`:

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

Ця пам’ять додається до контексту перед запуском агентів. Вона може зберігатися у зовнішніх сервісах, таких як mem0:

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

**Нагляд агента**

Нагляд важливий для створення надійних і керованих агентних систем. MAF інтегрується з OpenTelemetry для забезпечення трасування та лічильників для кращого нагляду.

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

MAF пропонує робочі процеси – це заздалегідь визначені кроки для виконання завдання, які включають AI агентів як компоненти на цих кроках.

Робочі процеси складаються з різних компонентів, що забезпечують кращий потік керування. Вони також дозволяють **оркестрацію багатьох агентів** та **контрольні точки (checkpointing)** для збереження станів робочого процесу.

Основні компоненти робочого процесу:

**Виконавці (Executors)**

Виконавці приймають вхідні повідомлення, виконують покладені на них завдання, а потім генерують вихідне повідомлення. Це просуває робочий процес до виконання більшого завдання. Виконавцями можуть бути як AI агенти, так і власна логіка.

**Зв’язки (Edges)**

Зв’язки використовуються для визначення потоку повідомлень у робочому процесі. Вони можуть бути:

*Прямі зв’язки* — прості з’єднання один-до-одного між виконавцями:

```python
from agent_framework import WorkflowBuilder

builder = WorkflowBuilder()
builder.add_edge(source_executor, target_executor)
builder.set_start_executor(source_executor)
workflow = builder.build()
```

*Умовні зв’язки* — активуються після виконання певної умови. Наприклад, коли готельні номери недоступні, виконавець може запропонувати інші варіанти.

*Edge з вибором (Switch-case Edges)* — маршрутують повідомлення до різних виконавців на основі визначених умов. Наприклад, якщо у клієнта пріоритетний доступ, його завдання обробляються іншим робочим процесом.

*Розгалужувачі (Fan-out Edges)* — надсилають одне повідомлення кільком одержувачам.

*Збірники (Fan-in Edges)* — збирають кілька повідомлень від різних виконавців та надсилають одному одержувачу.

**Події**

Для кращого нагляду робочих процесів MAF пропонує вбудовані події виконання, зокрема:

- `WorkflowStartedEvent`  - Початок виконання робочого процесу
- `WorkflowOutputEvent` - Робочий процес генерує вихід
- `WorkflowErrorEvent` - В робочому процесі виникає помилка
- `ExecutorInvokeEvent`  - Виконавець починає обробку
- `ExecutorCompleteEvent`  - Виконавець завершує обробку
- `RequestInfoEvent` - Надходить запит

## Розширені шаблони MAF

Попередні розділи охопили ключові концепції Microsoft Agent Framework. Коли ви створюєте складніші агенти, ось деякі розширені шаблони на розгляд:

- **Композиція Middleware**: ланцюжок кількох обробників middleware (логування, аутентифікація, обмеження швидкості) з використанням middleware функцій і чату для тонкого контролю поведінки агента.
- **Контрольні точки робочого процесу**: використання подій робочого процесу та серіалізації для збереження і відновлення тривалих процесів агента.
- **Динамічний вибір інструментів**: поєднання RAG над описами інструментів з реєстрацією інструментів MAF для представлення лише релевантних інструментів за запитом.
- **Передача між багатьма агентами**: використання зв’язків робочого процесу та умовної маршрутизації для організації передачі між спеціалізованими агентами.

## Розміщення агентів LangChain / LangGraph на Microsoft Foundry

Microsoft Agent Framework є **інтероперабельним фреймворком** — ви не обмежені агентами, написаними за допомогою MAF. Якщо у вас вже є агент, створений за допомогою **LangChain** або **LangGraph**, ви можете запускати його як **агента, розміщеного в Microsoft Foundry**, так що Foundry керуватиме часом виконання, сесіями, масштабуванням, автентифікацією та протокольними кінцевими точками, а логіка вашого агента залишатиметься в LangGraph.

Це здійснюється за допомогою пакета `langchain_azure_ai.agents.hosting`, який відкриває скомпільований граф LangGraph через ті самі протоколи, що використовують агенти, розміщені у Foundry.

**1. Встановіть додаткові пакети для розміщення:**

```bash
pip install -U "langchain-azure-ai[hosting]>=1.2.4" azure-identity
```

Пакет `hosting` встановлює бібліотеки протоколів Foundry: `azure-ai-agentserver-responses` (OpenAI-сумісний кінцевий пункт `/responses`) та `azure-ai-agentserver-invocations` (загальний кінцевий пункт `/invocations`).

**2. Оберіть протокол розміщення:**

| Протокол | Клас хоста | Кінцевий пункт | Використовуйте коли |
|----------|-----------|----------|----------|
| **Responses** | `ResponsesHostServer` | `/responses` | Якщо вам потрібен OpenAI-сумісний чат, трансляція, історія відповідей і багатопоточність у розмовах – рекомендований за замовчуванням для розмовних агентів. |
| **Invocations** | `InvocationsHostServer` | `/invocations` | Коли потрібна власна структура JSON, endpoint у стилі webhook або неконверсійна обробка. |

Оскільки **API Responses є основним API для розробки агентів у Foundry**, починайте з `ResponsesHostServer` для більшості агентів.

**3. Налаштуйте змінні оточення** (спочатку виконайте `az login`, щоб `DefaultAzureCredential` міг автентифікуватись):

```bash
export FOUNDRY_PROJECT_ENDPOINT="https://<resource>.services.ai.azure.com/api/projects/<project>"
export FOUNDRY_MODEL_NAME="gpt-4.1"
```

Коли агент пізніше запускається як розміщений агент у Foundry, платформа автоматично вставляє `FOUNDRY_PROJECT_ENDPOINT`.

**4. Відкрийте агента LangGraph через протокол Responses:**

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

    # ChatOpenAI тут звертається до кінцевої точки, сумісної з OpenAI (Responses) проєкту Foundry.
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

Запустіть локально командою `python main.py`, потім надішліть запит Responses на `http://localhost:8088/responses`.

**Основні особливості:**

- **Розмови**: Клієнти продовжують розмову, передаючи `previous_response_id` або `conversation` ID. Якщо ваш граф скомпільований із LangGraph чекпоінтером, Foundry зв’язує стан розмови з чекпоінтом (у виробництві використовуйте стійкий чекпоінтер; `MemorySaver` підходить для локального тестування).
- **Людина в циклі**: Якщо ваш граф використовує LangGraph `interrupt()`, `ResponsesHostServer` відображає очікуваний перерив як пункт Responses `function_call` / `mcp_approval_request`, а клієнти продовжують із відповіддю `function_call_output` / `mcp_approval_response`.
- **Розгортання в Foundry**: Використовуйте Azure Developer CLI — `azd ext install azure.ai.agents`, `azd ai agent init -m <manifest>`, `azd ai agent run` (локально, потрібен Docker), потім `azd provision` та `azd deploy`. Для розгортання розміщених агентів потрібна роль **Foundry Project Manager**.

Запускаюча версія цього прикладу знаходиться в [code-samples/14-langchain-hosted-agent.py](../../../14-microsoft-agent-framework/code-samples/14-langchain-hosted-agent.py). Для повного проходження (протокол Invocations, користувацькі схеми запитів та усунення проблем) дивіться [Host LangGraph agents as Foundry hosted agents](https://learn.microsoft.com/azure/foundry/how-to/develop/langchain-hosted-agents).

## Приклади коду 

Приклади коду для Microsoft Agent Framework можна знайти в цьому репозиторії у файлах `xx-python-agent-framework` і `xx-dotnet-agent-framework`.

## Є ще запитання щодо Microsoft Agent Framework?

Приєднуйтесь до [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D), щоб зустріти інших учнів, відвідати години консультацій і отримати відповіді на ваші питання про AI агентів.
## Попередній урок

[Пам’ять для AI агентів](../13-agent-memory/README.md)

## Наступний урок

[Створення агентів для використання комп’ютера (CUA)](../15-browser-use/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Відмова від відповідальності**:
Цей документ було перекладено за допомогою сервісу штучного інтелекту для перекладу [Co-op Translator](https://github.com/Azure/co-op-translator). Хоча ми прагнемо до точності, будь ласка, майте на увазі, що автоматичні переклади можуть містити помилки або неточності. Оригінальний документ рідною мовою слід вважати авторитетним джерелом. Для критично важливої інформації рекомендується професійний людський переклад. Ми не несемо відповідальності за будь-які непорозуміння або неправильні тлумачення, що виникли внаслідок використання цього перекладу.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->