# Вивчення Microsoft Agent Framework

![Agent Framework](../../../translated_images/uk/lesson-14-thumbnail.90df0065b9d234ee.webp)

### Вступ

У цьому уроці буде розглянуто:

- Розуміння Microsoft Agent Framework: ключові особливості та цінність  
- Вивчення основних концепцій Microsoft Agent Framework
- Розширені патерни MAF: робочі процеси, проміжне програмне забезпечення та пам’ять

## Цілі навчання

Після завершення цього уроку ви знатимете, як:

- Створити AI-агентів, готових до виробництва, за допомогою Microsoft Agent Framework
- Застосовувати основні функції Microsoft Agent Framework для ваших агентських сценаріїв
- Використовувати розширені патерни, включаючи робочі процеси, проміжне ПЗ та спостережуваність

## Приклади коду 

Приклади коду для [Microsoft Agent Framework (MAF)](https://learn.microsoft.com/en-us/agent-framework/overview/?wt.mc_id=youtube_26688_organicsocial_reactor&pivots=programming-language-python) можна знайти у цьому репозиторії у файлах `xx-python-agent-framework` та `xx-dotnet-agent-framework`.

## Розуміння Microsoft Agent Framework

![Framework Intro](../../../translated_images/uk/framework-intro.077af16617cf130c.webp)

[Microsoft Agent Framework (MAF)](https://learn.microsoft.com/en-us/agent-framework/overview/?wt.mc_id=youtube_26688_organicsocial_reactor&pivots=programming-language-python) — це уніфікований фреймворк Microsoft для створення AI-агентів. Він пропонує гнучкість для вирішення широкого спектра агентських сценаріїв, що зустрічаються як у виробничому, так і в дослідницькому середовищах, зокрема:

- **Послідовна оркестрація агентів** у випадках, коли потрібні покрокові робочі процеси.
- **Паралельна оркестрація** у ситуаціях, коли агенти повинні виконувати завдання одночасно.
- **Оркестрація групового чату** у випадках, коли агенти можуть співпрацювати над одним завданням.
- **Оркестрація передачі завдань** у ситуаціях, коли агенти передають завдання один одному у міру виконання підзавдань.
- **Магнітна оркестрація** у випадках, коли агент-менеджер створює та змінює список завдань і координує субагентів для їх виконання.

Для впровадження AI-агентів у виробництві MAF також містить можливості для:

- **Спостережуваність** через використання OpenTelemetry, де кожна дія AI-агента, включно з викликами інструментів, кроками оркестрації, потоками міркувань і моніторингом продуктивності через інформаційні панелі Microsoft Foundry.
- **Безпеки** завдяки розміщенню агентів безпосередньо на Microsoft Foundry, що включає засоби контролю безпеки, такі як доступ на основі ролей, обробка приватних даних і вбудована безпека контенту.
- **Надійності** — потоки агентів і робочі процеси можуть призупинятися, відновлюватися і відновлюватись після помилок, що дозволяє виконувати довготривалі процеси.
- **Контролю** — підтримка робочих процесів із людиною в циклі, де завдання позначаються як ті, що потребують людського затвердження.

Microsoft Agent Framework також орієнтований на сумісність, забезпечуючи:

- **Незалежність від хмари** — агенти можуть працювати у контейнерах, локально та в різних хмарах.
- **Незалежність від провайдера** — агенти можуть створюватися через улюблені SDK, включаючи Azure OpenAI та OpenAI.
- **Інтеграцію відкритих стандартів** — агенти можуть використовувати протоколи, такі як Agent-to-Agent (A2A) та Model Context Protocol (MCP), щоб знаходити і використовувати інших агентів і інструменти.
- **Плагіни та конектори** — зв’язки з даними та сервісами пам’яті, такими як Microsoft Fabric, SharePoint, Pinecone і Qdrant.

Розглянемо, як ці функції застосовуються до основних концепцій Microsoft Agent Framework.

## Основні концепції Microsoft Agent Framework

### Агенти

![Agent Framework](../../../translated_images/uk/agent-components.410a06daf87b4fef.webp)

**Створення агентів**

Створення агента здійснюється шляхом визначення сервісу інференції (провайдера LLM),
набору інструкцій для виконання AI-агентом та призначеного `name`:

```python
agent = AzureOpenAIChatClient(credential=AzureCliCredential()).create_agent( instructions="You are good at recommending trips to customers based on their preferences.", name="TripRecommender" )
```

Вище використовується `Azure OpenAI`, але агенти можуть створюватися за допомогою різних сервісів, включаючи `Microsoft Foundry Agent Service`:

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

або [MiniMax](https://platform.minimaxi.com/), який надає сумісний з OpenAI API з великими контекстними вікнами (до 204K токенів):

```python
agent = OpenAIChatClient(base_url="https://api.minimax.io/v1", api_key=os.environ["MINIMAX_API_KEY"], model_id="MiniMax-M3").create_agent( name="HelpfulAssistant", instructions="You are a helpful assistant.", )
```

або віддалені агенти з використанням протоколу A2A:

```python
agent = A2AAgent( name=agent_card.name, description=agent_card.description, agent_card=agent_card, url="https://your-a2a-agent-host" )
```

**Запуск агентів**

Агенти запускаються за допомогою методів `.run` або `.run_stream` для нестрімінгових або стрімінгових відповідей відповідно.

```python
result = await agent.run("What are good places to visit in Amsterdam?")
print(result.text)
```

```python
async for update in agent.run_stream("What are the good places to visit in Amsterdam?"):
    if update.text:
        print(update.text, end="", flush=True)

```

Кожен запуск агента також може мати параметри для налаштування таких параметрів, як `max_tokens`, які використовує агент, `tools`, які агент може викликати, і навіть сам `model`, що використовується агентом.

Це корисно у випадках, коли для виконання завдання користувача потрібні певні моделі або інструменти.

**Інструменти**

Інструменти можна визначати як при створенні агента:

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

Потоки агента використовуються для обробки багатокрокових розмов. Потоки можна створювати або за допомогою:

- Виклику `get_new_thread()`, що дозволяє зберігати потік з часом
- Автоматичного створення потоку при запуску агента, який існує тільки протягом поточного запуску.

Для створення потоку код виглядає так:

```python
# Створити новий потік.
thread = agent.get_new_thread() # Запустити агента з потоком.
response = await agent.run("Hello, I am here to help you book travel. Where would you like to go?", thread=thread)

```

Потім ви можете серіалізувати потік для збереження на майбутнє:

```python
# Створити новий потік.
thread = agent.get_new_thread() 

# Запустити агента з потоком.

response = await agent.run("Hello, how are you?", thread=thread) 

# Серіалізувати потік для зберігання.

serialized_thread = await thread.serialize() 

# Десеріалізувати стан потоку після завантаження із сховища.

resumed_thread = await agent.deserialize_thread(serialized_thread)
```

**Проміжне програмне забезпечення агента**

Агенти взаємодіють з інструментами та LLM для виконання завдань користувача. В окремих сценаріях ми хочемо виконати або відстежити дії між цими взаємодіями. Проміжне ПЗ агента дозволяє це зробити за допомогою:

*Проміжне ПЗ для функцій*

Це проміжне ПЗ дозволяє виконати дію між агентом та функцією/інструментом, який він викликає. Приклад використання — ведення логів виклику функції.

У коді нижче `next` визначає, чи слід викликати наступне проміжне ПЗ або фактичну функцію.

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

*Проміжне ПЗ для чату*

Це проміжне ПЗ дозволяє виконувати або вести лог дій між агентом і запитами до LLM.

Воно містить важливу інформацію, таку як `messages`, що відправляються AI-сервісу.

```python
async def logging_chat_middleware(
    context: ChatContext,
    next: Callable[[ChatContext], Awaitable[None]],
) -> None:
    """Chat middleware that logs AI interactions."""
    # Попередня обробка: запис у лог перед викликом ШІ
    print(f"[Chat] Sending {len(context.messages)} messages to AI")

    # Продовжити до наступного проміжного програмного забезпечення або сервісу ШІ
    await next(context)

    # Пост-обробка: запис у лог після відповіді ШІ
    print("[Chat] AI response received")

```

**Пам’ять агента**

Як було розглянуто в уроці `Agentic Memory`, пам’ять є важливим елементом, що дозволяє агенту працювати з різними контекстами. MAF пропонує кілька типів пам’яті:

*Пам’ять у оперативній пам’яті*

Ця пам’ять зберігається у потоках під час виконання застосунку.

```python
# Створити новий потік.
thread = agent.get_new_thread() # Запустити агента у потоці.
response = await agent.run("Hello, I am here to help you book travel. Where would you like to go?", thread=thread)
```

*Стійкі повідомлення*

Ця пам’ять використовується для збереження історії розмов між сесіями. Визначається за допомогою `chat_message_store_factory`:

```python
from agent_framework import ChatMessageStore

# Створити користувацьке сховище повідомлень
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

# Використання Mem0 для розширених можливостей пам’яті
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

Спостережуваність важлива для створення надійних та підтримуваних агентських систем. MAF інтегрується з OpenTelemetry для забезпечення трасування та метрів для кращої спостережуваності.

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

MAF пропонує робочі процеси — попередньо визначені кроки для виконання завдання, які включають AI-агентів як компоненти цих кроків.

Робочі процеси складаються з різних компонентів, що дозволяють краще контролювати потік. Робочі процеси також забезпечують **оркестрацію багатьох агентів** та **контрольні точки** для збереження станів робочого процесу.

Основні компоненти робочого процесу:

**Виконавці**

Виконавці отримують вхідні повідомлення, виконують покладені на них завдання, а потім генерують вихідне повідомлення. Це забезпечує просування робочого процесу до завершення великого завдання. Виконавцями можуть бути AI-агенти або кастомна логіка.

**Ребра**

Ребра використовуються для визначення потоку повідомлень у робочому процесі. Вони можуть бути:

*Прямі ребра* — прості одно-на-один з'єднання між виконавцями:

```python
from agent_framework import WorkflowBuilder

builder = WorkflowBuilder()
builder.add_edge(source_executor, target_executor)
builder.set_start_executor(source_executor)
workflow = builder.build()
```

*Умовні ребра* — активуються після виконання певної умови. Наприклад, якщо номери в готелі недоступні, виконавець може запропонувати інші варіанти.

*Ребра за схемою switch-case* — направляють повідомлення до різних виконавців на основі визначених умов. Наприклад, якщо у клієнта пріоритетний доступ, його завдання будуть оброблятись іншим робочим процесом.

*Розподільчі ребра* — надсилають одне повідомлення кільком адресатам.

*Об’єднувальні ребра* — збирають кілька повідомлень від різних виконавців і надсилають одному адресату.

**Події**

Для кращої спостережуваності робочих процесів MAF пропонує вбудовані події виконання, зокрема:

- `WorkflowStartedEvent`  — запуск робочого процесу
- `WorkflowOutputEvent` — робочий процес генерує вихідні дані
- `WorkflowErrorEvent` — в робочому процесі сталася помилка
- `ExecutorInvokeEvent`  — виконавець починає обробку
- `ExecutorCompleteEvent`  — виконавець завершує обробку
- `RequestInfoEvent` — здійснюється запит

## Розширені патерни MAF

Вище описано ключові концепції Microsoft Agent Framework. При побудові більш складних агентів зверніть увагу на такі розширені патерни:

- **Композиція проміжного ПЗ**: ланцюжок кількох обробників проміжного ПЗ (логування, автентифікація, обмеження швидкості) за допомогою функціонального та чат-проміжного ПЗ для тонкого контролю поведінки агента.
- **Контрольні точки робочих процесів**: використання подій робочого процесу та серіалізація для збереження і відновлення тривалих процесів агента.
- **Динамічний вибір інструментів**: поєднання RAG за описом інструментів із реєстрацією інструментів у MAF, щоб показувати лише релевантні інструменти за запитом.
- **Передача між кількома агентами**: використання ребер робочих процесів та умовної маршрутизації для оркестрації передач між спеціалізованими агентами.

## Розміщення LangChain / LangGraph агентів на Microsoft Foundry

Microsoft Agent Framework є **фреймворк-інтероперабельним** — ви не обмежені агентами, написаними з MAF. Якщо у вас вже є агент, створений за допомогою **LangChain** або **LangGraph**, ви можете запустити його як **агент, розміщений у Microsoft Foundry**, щоб Foundry керував часом виконання, сесіями, масштабуванням, аутентифікацією та кінцевими точками протоколів, у той час як логіка агента залишатиметься у LangGraph.

Це реалізується за допомогою пакету `langchain_azure_ai.agents.hosting`, який відкриває скомпільований граф LangGraph через ті ж протоколи, що використовують агенти, розміщені у Foundry.

**1. Встановіть додатковий пакет для хостингу:**

```bash
pip install -U "langchain-azure-ai[hosting]>=1.2.4" azure-identity
```

Додатковий пакет `hosting` встановлює бібліотеки протоколів Foundry: `azure-ai-agentserver-responses` (сумісний з OpenAI `/responses` кінцевий пункт) та `azure-ai-agentserver-invocations` (універсальний `/invocations` кінцевий пункт).

**2. Оберіть протокол хостингу:**

| Протокол | Клас хоста | Кінцева точка | Використання |
|----------|------------|--------------|------------|
| **Responses** | `ResponsesHostServer` | `/responses` | Рекомендується для розмовних агентів: сумісний з OpenAI чат, стрімінг, історія відповідей, потоки розмов. |
| **Invocations** | `InvocationsHostServer` | `/invocations` | Потрібні кастомні JSON форми, webhook-стиль або не розмовна обробка. |

Оскільки **Responses API є основним API для розробки агентів у Foundry**, починайте використовувати `ResponsesHostServer` для більшості агентів.

**3. Налаштуйте змінні середовища** (`az login` перед тим, щоб `DefaultAzureCredential` могла аутентифікуватися):

```bash
export FOUNDRY_PROJECT_ENDPOINT="https://<resource>.services.ai.azure.com/api/projects/<project>"
export FOUNDRY_MODEL_NAME="gpt-5-mini"
```

Коли агент пізніше запускатиметься як хостований агент у Foundry, платформа автоматично додасть `FOUNDRY_PROJECT_ENDPOINT`.

**4. Відкрийте LangGraph агента через протокол Responses:**

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

    # ChatOpenAI тут націлено на сумісний з OpenAI (Responses) кінцевий пункт проекту Foundry.
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

**Ключові особливості:**

- **Розмови**: Клієнти можуть продовжувати розмову, передаючи `previous_response_id` або `conversation` ID. Якщо ваш граф скомпільовано з LangGraph чекпойнтером, Foundry зв’язує стан розмови з цією контрольною точкою (для продакшену використовуйте надійний чекпойнтер; `MemorySaver` підходить для локального тестування).
- **Людина в циклі**: Якщо граф використовує LangGraph `interrupt()`, `ResponsesHostServer` відображає очікуюче переривання як Response `function_call` / `mcp_approval_request`, а клієнти відновлюють роботу відповіддю `function_call_output` / `mcp_approval_response`.
- **Розгортання у Foundry**: Використовуйте Azure Developer CLI — `azd ext install azure.ai.agents`, `azd ai agent init -m <manifest>`, `azd ai agent run` (локально, потрібно Docker), потім `azd provision` і `azd deploy`. Для розгортання хостованих агентів потрібна роль **Foundry Project Manager**.

Запускаюча версія цього прикладу знаходиться у [code-samples/14-langchain-hosted-agent.py](../../../14-microsoft-agent-framework/code-samples/14-langchain-hosted-agent.py). Для повного керівництва (протокол Invocations, кастомні схеми запитів і усунення неполадок) див. [Host LangGraph agents as Foundry hosted agents](https://learn.microsoft.com/azure/foundry/how-to/develop/langchain-hosted-agents).

## Приклади коду 

Приклади коду для Microsoft Agent Framework можна знайти у цьому репозиторії у файлах `xx-python-agent-framework` та `xx-dotnet-agent-framework`.

## Є ще питання щодо Microsoft Agent Framework?

Приєднуйтесь до [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D), щоб зустрітися з іншими учнями, відвідувати години консультацій та отримувати відповіді на питання про AI-агентів.
## Попередній урок

[Пам’ять для AI-агентів](../13-agent-memory/README.md)

## Наступний урок

[Створення агентів для користування комп’ютером (CUA)](../15-browser-use/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Відмова від відповідальності**:
Цей документ було перекладено за допомогою сервісу штучного інтелекту для перекладу [Co-op Translator](https://github.com/Azure/co-op-translator). Хоча ми прагнемо до точності, будь ласка, майте на увазі, що автоматичні переклади можуть містити помилки або неточності. Оригінальний документ рідною мовою слід вважати авторитетним джерелом. Для критично важливої інформації рекомендується професійний людський переклад. Ми не несемо відповідальності за будь-які непорозуміння або неправильні тлумачення, що виникли внаслідок використання цього перекладу.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->