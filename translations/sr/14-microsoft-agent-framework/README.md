# Истраживање Microsoft Agent Framework

![Agent Framework](../../../translated_images/sr/lesson-14-thumbnail.90df0065b9d234ee.webp)

### Увод

Ова лекција ће покрити:

- Разумевање Microsoft Agent Framework: Кључне карактеристике и вредност  
- Истраживање кључних појмова Microsoft Agent Framework
- Напредни MAF шаблони: Радни токови, посредници и меморија

## Циљеви учења

Након завршетка ове лекције, знаћете како да:

- Креирате производно спремне AI агенте користећи Microsoft Agent Framework
- Примените основне карактеристике Microsoft Agent Framework у вашима агентским случајевима употребе
- Користите напредне шаблоне укључујући радне токове, посреднике и опсервабилност

## Примери кода

Примери кода за [Microsoft Agent Framework (MAF)](https://aka.ms/ai-agents-beginners/agent-framewrok) могу се наћи у овом репозиторијуму под фајловима `xx-python-agent-framework` и `xx-dotnet-agent-framework`.

## Разумевање Microsoft Agent Framework

![Framework Intro](../../../translated_images/sr/framework-intro.077af16617cf130c.webp)

[Microsoft Agent Framework (MAF)](https://aka.ms/ai-agents-beginners/agent-framewrok) је јединствени Microsoft-ов оквир за израду AI агената. Он нуди флексибилност да обради широк спектар агентских случајева употребе виђених и у производним и у истраживачким окружењима укључујући:

- **Секвенцијална оркестрација агената** у сценаријима где су потребни корак по корак радни токови.
- **Паралелна оркестрација** у сценаријима где агенти треба да заврше задатке истовремено.
- **Оркестрација групног ћаскања** у сценаријима где агенти могу сарађивати на једном задатку.
- **Оркестрација преузимања задатка** у сценаријима где агенти предају задатак један другом како се подсетови задатака завршавају.
- **Магнетна оркестрација** у сценаријима где агент-менаџер креира и мења листу задатака и координише субагенте да заврше задатак.

Да би испоручио AI агенте у производњи, MAF такође укључује функције за:

- **Опсервабилност** кроз коришћење OpenTelemetry где свака акција AI агента укључујући позив алата, кораке оркестрације, процесе размишљања и праћење перформанси преко Microsoft Foundry контролних табли.
- **Безбедност** хостовањем агената нативно на Microsoft Foundry која укључује безбедносне контроле као што су приступ заснован на улогама, руковање приватним подацима и уграђена сигурност садржаја.
- **Отпорност** јер нитови и радни токови агената могу да паузирају, наставе и опораве се од грешака, што омогућава дуже процесе.
- **Контрола** јер раде радни токови са људским уметањем где су задаци означени као потребни одобрење од људи.

Microsoft Agent Framework је такође фокусиран на интероперабилност кроз:

- **Бити независан од облака** - агенти могу да раде у контејнерима, локално и преко више различитих облака.
- **Бити независан од провајдера** - агенти се могу креирати користећи ваш омиљени SDK укључујући Azure OpenAI и OpenAI.
- **Интеграцију отворених стандарда** - агенти могу користити протоколе као што су Agent-to-Agent (A2A) и Model Context Protocol (MCP) за откривање и коришћење других агената и алата.
- **Плугин-ове и конекторе** - могу се повезивати са сервисима за податке и меморију као што су Microsoft Fabric, SharePoint, Pinecone и Qdrant.

Хајде да погледамо како се ове функције примењују на неке од основних појмова Microsoft Agent Framework.

## Кључни појмови Microsoft Agent Framework

### Агенти

![Agent Framework](../../../translated_images/sr/agent-components.410a06daf87b4fef.webp)

**Креирање агената**

Креирање агената се обавља дефинисањем сервиса за извођење закључивања (LLM провајдер), скупом упутстава која AI агент треба да прати и додељеним `name`:

```python
agent = AzureOpenAIChatClient(credential=AzureCliCredential()).create_agent( instructions="You are good at recommending trips to customers based on their preferences.", name="TripRecommender" )
```

Горњи пример користи `Azure OpenAI` али агенти се могу креирати користећи различите сервисе укључујући и `Microsoft Foundry Agent Service`:

```python
AzureAIAgentClient(async_credential=credential).create_agent( name="HelperAgent", instructions="You are a helpful assistant." ) as agent
```

OpenAI `Responses`, `ChatCompletion` API-је

```python
agent = OpenAIResponsesClient().create_agent( name="WeatherBot", instructions="You are a helpful weather assistant.", )
```

```python
agent = OpenAIChatClient().create_agent( name="HelpfulAssistant", instructions="You are a helpful assistant.", )
```

или удаљене агенте користећи A2A протокол:

```python
agent = A2AAgent( name=agent_card.name, description=agent_card.description, agent_card=agent_card, url="https://your-a2a-agent-host" )
```

**Покретање агената**

Агенти се извршавају помоћу метода `.run` или `.run_stream` за нетрансмијуће или стриминг одговоре.

```python
result = await agent.run("What are good places to visit in Amsterdam?")
print(result.text)
```

```python
async for update in agent.run_stream("What are the good places to visit in Amsterdam?"):
    if update.text:
        print(update.text, end="", flush=True)

```

За сваки покретач агента могу се подесити опције за прилагођавање параметара као што су `max_tokens` које агент користи, `tools` које агент може позивати, па чак и сам `model` који се користи.

Ово је корисно у случајевима када су специфични модели или алати потребни за извршење корисничког задатка.

**Алатке**

Алатке могу бити дефинисане и приликом дефинисања агента:

```python
def get_attractions( location: Annotated[str, Field(description="The location to get the top tourist attractions for")], ) -> str: """Get the top tourist attractions for a given location.""" return f"The top attractions for {location} are." 


# Када се директно креира ChatAgent

agent = ChatAgent( chat_client=OpenAIChatClient(), instructions="You are a helpful assistant", tools=[get_attractions]

```

али и приликом покретања агента:

```python

result1 = await agent.run( "What's the best place to visit in Seattle?", tools=[get_attractions] # Алат обезбеђен само за ову извршну поставку )
```

**Нитови агената**

Нитови агената се користе за руковање вишекратним разговорама. Нитови могу бити креирани на два начина:

- Коришћењем `get_new_thread()` што омогућава да се нит сачува током времена
- Аутоматским креирањем нити приликом покретања агента, а нит траје само током тренутног покретања.

Код за креирање нити изгледа овако:

```python
# Направите нови нит.
thread = agent.get_new_thread() # Покрените агента са нити.
response = await agent.run("Hello, I am here to help you book travel. Where would you like to go?", thread=thread)

```

Нит се затим може серијализовати да би се сачувала за каснију употребу:

```python
# Креирајте нови нит.
thread = agent.get_new_thread() 

# Покрените агента са ништом.

response = await agent.run("Hello, how are you?", thread=thread) 

# Серијализујте нит за складиштење.

serialized_thread = await thread.serialize() 

# Десеријализујте стање нити након учитавања из складишта.

resumed_thread = await agent.deserialize_thread(serialized_thread)
```

**Посредник агената**

Агенти комуницирају са алаткама и LLM-овима како би завршили корисничке задатке. У одређеним сценаријима желимо да извршавамо или пратимо радње између ових интеракција. Посредник агента нам омогућава да то радимо кроз:

*Функцијски посредник*

Овај посредник омогућава извршавање радње између агента и функције/алата који ће позивати. Пример када би се ово користило је када желите да бележите позив функције.

У коду испод, `next` одређује да ли се позива следећи посредник или сама функција.

```python
async def logging_function_middleware(
    context: FunctionInvocationContext,
    next: Callable[[FunctionInvocationContext], Awaitable[None]],
) -> None:
    """Function middleware that logs function execution."""
    # Предобрада: Логовање пре извршења функције
    print(f"[Function] Calling {context.function.name}")

    # Настави на следећи посреднички софтвер или извршење функције
    await next(context)

    # Побрaда: Логовање након извршења функције
    print(f"[Function] {context.function.name} completed")
```

*Чат посредник*

Овај посредник омогућава извршење или бележење радње између агента и захтева LLM-у.

Ово садржи важне информације као што су `messages` које се шаљу AI сервису.

```python
async def logging_chat_middleware(
    context: ChatContext,
    next: Callable[[ChatContext], Awaitable[None]],
) -> None:
    """Chat middleware that logs AI interactions."""
    # Предобрада: Логовање пре позива АИ-а
    print(f"[Chat] Sending {len(context.messages)} messages to AI")

    # Настави на следећи посреднички слој или АИ сервис
    await next(context)

    # Постобрада: Логовање након одговора АИ-а
    print("[Chat] AI response received")

```

**Меморија агента**

Као што је обрађено у лекцији `Agentic Memory`, меморија је важан елемент за омогућавање агента да ради у различитим контекстима. MAF нуди неколико врста меморија:

*Складиштење у меморији*

Ово је меморија која се чува у нитима током извршења апликације.

```python
# Креирај нови тред.
thread = agent.get_new_thread() # Покрени агента са тредом.
response = await agent.run("Hello, I am here to help you book travel. Where would you like to go?", thread=thread)
```

*Перзистентне поруке*

Ова меморија се користи за чување историје разговора између различитих сесија. Дефинише се користећи фабрику `chat_message_store_factory`:

```python
from agent_framework import ChatMessageStore

# Креирајте прилагођену продавницу порука
def create_message_store():
    return ChatMessageStore()

agent = ChatAgent(
    chat_client=OpenAIChatClient(),
    instructions="You are a Travel assistant.",
    chat_message_store_factory=create_message_store
)

```

*Динамична меморија*

Ова меморија се додаје у контекст пре покретања агената. Ове меморије могу се чувати у спољним сервисима као што је mem0:

```python
from agent_framework.mem0 import Mem0Provider

# Коришћење Mem0 за напредне меморијске могућности
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

**Опсервабилност агента**

Опсервабилност је важна за израду поузданих и одрживих агентских система. MAF се интегрише са OpenTelemetry за пружање праћења и мера за бољу опсервабилност.

```python
from agent_framework.observability import get_tracer, get_meter

tracer = get_tracer()
meter = get_meter()
with tracer.start_as_current_span("my_custom_span"):
    # уради нешто
    pass
counter = meter.create_counter("my_custom_counter")
counter.add(1, {"key": "value"})
```

### Радни токови

MAF нуди радне токове који су унапред дефинисани кораци за завршетак задатка и укључују AI агенте као компоненте у тим корацима.

Радни токови се састоје из различитих компоненти које омогућавају боље управљање током контроле. Радни токови такође омогућавају **мулти-агентску оркестрацију** и **чување стања радног тока**.

Основне компоненте радног тока су:

**Екзекутори**

Екзекутори примају улазне поруке, обављају додељене задатке и производе излазне поруке. Ово покреће радни ток унапред ка завршетку већег задатка. Екзекутора могу бити AI агенти или прилагођена логика.

**Ивице**

Ивице се користе за дефинисање протока порука унутар радног тока. Оне могу бити:

*Директне ивице* - Једноставне један-на-један везе између екзекутора:

```python
from agent_framework import WorkflowBuilder

builder = WorkflowBuilder()
builder.add_edge(source_executor, target_executor)
builder.set_start_executor(source_executor)
workflow = builder.build()
```

*Условане ивице* - Активирају се након што је испуњен одређени услов. На пример, када хотели немају слободне собе, екзекутор може предложити друге опције.

*Switch-case ивице* - Роутују поруке различитим екзекуторама на основу дефинисаних услова. На пример, ако путник има приоритетни приступ, њихови задаци ће бити обрађени кроз други радни ток.

*Fan-out ивице* - Шаљу једну поруку више циљева.

*Fan-in ивице* - Прикупљају више порука од различитих екзекутора и шаљу их једном циљу.

**Догађаји**

Да би осигурао бољу опсервабилност унутар радних токова, MAF нуди уграђене догађаје за извршење укључујући:

- `WorkflowStartedEvent`  - Започиње извршење радног тока
- `WorkflowOutputEvent` - Радни ток производи излаз
- `WorkflowErrorEvent` - Радни ток наиђе на грешку
- `ExecutorInvokeEvent`  - Екзекутор почиње обраду
- `ExecutorCompleteEvent`  -  Екзекутор завршава обраду
- `RequestInfoEvent` - Захтев је постављен

## Напредни MAF шаблони

Горње секције покривају кључне појмове Microsoft Agent Framework. Како градите сложеније агенте, ево неких напредних шаблона које треба размотрити:

- **Композиција посредника**: Повежите више обрада посредника (логовање, аутентикација, ограничење брзине) користећи функцијски и чат посредник за прецизну контролу понашања агента.
- **Снимање тачака рада у радном току**: Користите догађаје радног тока и серијализацију да бисте сачували и наставили дуготрајне процесе агената.
- **Динамичан избор алата**: Комбинујте RAG преко описа алата са регистрацијом алата у MAF-у да бисте приказали само релевантне алате по упиту.
- **Мулти-агентско преузимање задатка**: Користите ивице радног тока и условно рутирање за оркестрацију преузимања задатака између специјализованих агената.

## Примери кода

Примери кода за Microsoft Agent Framework могу се наћи у овом репозиторијуму под фајловима `xx-python-agent-framework` и `xx-dotnet-agent-framework`.

## Имате још питања о Microsoft Agent Framework?

Придружите се [Microsoft Foundry Discord](https://aka.ms/ai-agents/discord) да бисте упознали друге учеснике, присуствовали канцеларијским сатима и добили одговоре на ваша питања о AI агентима.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Одрицање од одговорности**:  
Овај документ је преведен коришћењем AI сервиса за превођење [Co-op Translator](https://github.com/Azure/co-op-translator). Иако се трудимо да превод буде што прецизнији, треба имати у виду да аутоматски преводи могу садржати грешке или нетачности. Оригинални документ на његовом изворном језику треба сматрати коначним и ауторитетним извором. За кључне информације препоручује се професионални људски превод. Не сносимо одговорност за било каква неспоразуме или погрешне интерпретације које могу настати коришћењем овог превода.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->