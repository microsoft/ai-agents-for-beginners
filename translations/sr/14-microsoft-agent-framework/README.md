# Истраживање Microsoft Agent Framework

![Agent Framework](../../../translated_images/sr/lesson-14-thumbnail.90df0065b9d234ee.webp)

### Увод

Ова лекција ће обухватити:

- Разумевање Microsoft Agent Framework: Кључне карактеристике и вредност  
- Истраживање кључних појмова Microsoft Agent Framework
- Напредни MAF обрасци: Радни токови, Middleware и Меморија

## Циљеви учења

Након завршетка ове лекције, знаћете како да:

- Креирате AI агенте спремне за производњу користећи Microsoft Agent Framework
- Примењујете основне карактеристике Microsoft Agent Framework за ваше агенцијске случајеве употребе
- Користите напредне обрасце укључујући радне токове, middleware и посматрање

## Примери кода

Примери кода за [Microsoft Agent Framework (MAF)](https://aka.ms/ai-agents-beginners/agent-framework) могу се наћи у овом репозиторијуму у датотекама `xx-python-agent-framework` и `xx-dotnet-agent-framework`.

## Разумевање Microsoft Agent Framework

![Framework Intro](../../../translated_images/sr/framework-intro.077af16617cf130c.webp)

[Microsoft Agent Framework (MAF)](https://aka.ms/ai-agents-beginners/agent-framework) је јединствени Microsoft-ов оквир за креирање AI агената. Пружа флексибилност за решавање широког спектра агенцијских случајева употребе у производним и истраживачким окружењима, укључујући:

- **Секвенцијалну оркестрацију агената** у сценаријима где су потребни корак-по-корак радни токови.
- **Истовремену оркестрацију** у сценаријима где агенти морају истовремено да заврше задатке.
- **Оркестрацију групног разговора** у сценаријима где агенти могу заједно сарађивати на једном задатку.
- **Оркестрацију преноса задатака** у сценаријима када агенти предају задатак један другом по завршетку подзадака.
- **Магнетску оркестрацију** у сценаријима када менаџер агент креира и модификује листу задатака и управља координацијом подагената за завршетак задатка.

Да би испоручио AI агенте у производњи, MAF такође укључује карактеристике као што су:

- **Посматрање** кроз коришћење OpenTelemetry, где се свака акција AI агента укључујући позив инструмената, кораке оркестрације, ток мисли и праћење перформанси преко Microsoft Foundry надзорних панела.
- **Безбедност** хостовањем агената нативно на Microsoft Foundry, што укључује контроле приступа засноване на улогама, руковање приватним подацима и уграђене безбедносне мере садржаја.
- **Издржљивост** јер агенцијске нитове и радне токове могу да паузирају, наставе и опораве се од грешака, омогућавајући дуже трајање процеса.
- **Контролу** јер су подржани радни токови са човеком у петљи, где су задаци означени као захтевајући људско одобрење.

Microsoft Agent Framework је такође усмерен ка интероперабилности путем:

- **Бити независан од облака** - Агенти могу да раде у контејнерима, локално и преко више различитих облака.
- **Бити независан од провајдера** - Агенти се могу креирати коришћењем ваше омиљене SDK, укључујући Azure OpenAI и OpenAI
- **Интеграција отворених стандарда** - Агенти могу користити протоколе као што су Agent-to-Agent (A2A) и Model Context Protocol (MCP) за откривање и коришћење других агената и алата.
- **Плгинови и конектори** - Могуће је повезивање са сервисима за податке и меморију као што су Microsoft Fabric, SharePoint, Pinecone и Qdrant.

Погледајмо како се ове карактеристике примењују на неке од основних појмова Microsoft Agent Framework.

## Кључни појмови Microsoft Agent Framework

### Агенти

![Agent Framework](../../../translated_images/sr/agent-components.410a06daf87b4fef.webp)

**Креирање агената**

Креирање агената врши се дефинисањем сервиса за инференцију (LLM провајдер), сета упутстава која AI агент треба да прати и додељеним `name`:

```python
agent = AzureOpenAIChatClient(credential=AzureCliCredential()).create_agent( instructions="You are good at recommending trips to customers based on their preferences.", name="TripRecommender" )
```

Горе се користи `Azure OpenAI` али агенти се могу креирати коришћењем различитих сервиса укључујући `Microsoft Foundry Agent Service`:

```python
AzureAIAgentClient(async_credential=credential).create_agent( name="HelperAgent", instructions="You are a helpful assistant." ) as agent
```

OpenAI `Responses`, `ChatCompletion` API-ји

```python
agent = OpenAIResponsesClient().create_agent( name="WeatherBot", instructions="You are a helpful weather assistant.", )
```

```python
agent = OpenAIChatClient().create_agent( name="HelpfulAssistant", instructions="You are a helpful assistant.", )
```

или [MiniMax](https://platform.minimaxi.com/), који пружа OpenAI-компатибилан API са великим контекстуалним прозорима (до 204К токена):

```python
agent = OpenAIChatClient(base_url="https://api.minimax.io/v1", api_key=os.environ["MINIMAX_API_KEY"], model_id="MiniMax-M3").create_agent( name="HelpfulAssistant", instructions="You are a helpful assistant.", )
```

или удаљене агенте помоћу A2A протокола:

```python
agent = A2AAgent( name=agent_card.name, description=agent_card.description, agent_card=agent_card, url="https://your-a2a-agent-host" )
```

**Покретање агената**

Агенти се покрећу методом `.run` или `.run_stream` за одговоре без стримовања или са стримовањем.

```python
result = await agent.run("What are good places to visit in Amsterdam?")
print(result.text)
```

```python
async for update in agent.run_stream("What are the good places to visit in Amsterdam?"):
    if update.text:
        print(update.text, end="", flush=True)

```

Сваки покретач агента може имати опције за прилагођавање параметара као што су `max_tokens` које агент користи, `tools` које агент може позивати и чак и сам `model` који агент користи.

Ово је корисно у случајевима када су потребни специфични модели или алати за извршење корисничког задатка.

**Алати**

Алати могу бити дефинисани и приликом дефинисања агента:

```python
def get_attractions( location: Annotated[str, Field(description="The location to get the top tourist attractions for")], ) -> str: """Get the top tourist attractions for a given location.""" return f"The top attractions for {location} are." 


# При директном креирању ChatAgent-а

agent = ChatAgent( chat_client=OpenAIChatClient(), instructions="You are a helpful assistant", tools=[get_attractions]

```

и такође приликом покретања агента:

```python

result1 = await agent.run( "What's the best place to visit in Seattle?", tools=[get_attractions] # Алат обезбеђен само за ову примену )
```

**Нитови агената**

Нитови агената се користе за руковање вишекратним разговорима. Нитови могу бити креирани на два начина:

- Коришћењем `get_new_thread()` што омогућава да нит буде сачувана током времена
- Аутоматским креирањем нити приликом покретања агента и трајањем нити само током тренутног извршавања.

За креирање нити код изгледа овако:

```python
# Креирај нови тред.
thread = agent.get_new_thread() # Покрени агента са тредом.
response = await agent.run("Hello, I am here to help you book travel. Where would you like to go?", thread=thread)

```

Онда нит можете серијализовати да би била сачувана за каснију употребу:

```python
# Креирајте нови нит.
thread = agent.get_new_thread() 

# Покрените агента са нити.

response = await agent.run("Hello, how are you?", thread=thread) 

# Серијализујте нит за складиштење.

serialized_thread = await thread.serialize() 

# Десеријализујте стање нити након учитавања са складишта.

resumed_thread = await agent.deserialize_thread(serialized_thread)
```

**Middleware агента**

Агенти комуницирају са алатима и LLM-овима да би извршили корисничке задатке. У одређеним сценаријима желимо да извршимо или пратимо радње између тих интеракција. Middleware агента нам то омогућава кроз:

*Middleware функција*

Овај middleware нам омогућава да извршимо радњу између агента и функције/алата који ће бити позван. Пример када се то користи је када желите да забележите позив функције.

У доњем коду `next` одређује да ли треба позвати следећи middleware или саму функцију.

```python
async def logging_function_middleware(
    context: FunctionInvocationContext,
    next: Callable[[FunctionInvocationContext], Awaitable[None]],
) -> None:
    """Function middleware that logs function execution."""
    # Предобрада: Логовање пре извршавања функције
    print(f"[Function] Calling {context.function.name}")

    # Настави са следећим посредником или извршавањем функције
    await next(context)

    # Пособрада: Логовање после извршавања функције
    print(f"[Function] {context.function.name} completed")
```

*Middleware разговора*

Овај middleware омогућава извршавање или бележење радње између агента и захтева ка LLM-у.

Ово садржи важне информације као што су `messages` који се шаљу AI сервису.

```python
async def logging_chat_middleware(
    context: ChatContext,
    next: Callable[[ChatContext], Awaitable[None]],
) -> None:
    """Chat middleware that logs AI interactions."""
    # Пре-обрада: Запиши пре позива вештачке интелигенције
    print(f"[Chat] Sending {len(context.messages)} messages to AI")

    # Настави на следећи middleware или AI сервис
    await next(context)

    # Пост-обрада: Запиши након одговора вештачке интелигенције
    print("[Chat] AI response received")

```

**Меморија агента**

Као што је обухваћено у лекцији `Agentic Memory`, меморија је важан елемент који омогућава агенту да делује у различитим контекстима. MAF нуди неколико различитих типова меморија:

*У меморији складиштење*

Ово је меморија која се чува у нитима током рада апликације.

```python
# Креирајте нови нити.
thread = agent.get_new_thread() # Покрените агента са нитом.
response = await agent.run("Hello, I am here to help you book travel. Where would you like to go?", thread=thread)
```

*Постојане поруке*

Ова меморија се користи за чување историје разговора преко различитих сесија. Дефинише се помоћу `chat_message_store_factory`:

```python
from agent_framework import ChatMessageStore

# Направите прилагођену продавницу порука
def create_message_store():
    return ChatMessageStore()

agent = ChatAgent(
    chat_client=OpenAIChatClient(),
    instructions="You are a Travel assistant.",
    chat_message_store_factory=create_message_store
)

```

*Динамична меморија*

Ова меморија се додаје контексту пре покретања агената. Ове меморије се могу чувати у спољним сервисима као што је mem0:

```python
from agent_framework.mem0 import Mem0Provider

# Коришћење Mem0 за напредне могућности меморије
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

**Посматрање агента**

Посматрање је важно за изградњу поузданих и одрживих агенцијских система. MAF се интегрише са OpenTelemetry да обезбеди праћење и мерење за боље посматрање.

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

MAF нуди радне токове који су унапред дефинисани кораци за завршетак задатка и укључују AI агенте као компоненте тих корака.

Радни токови се састоје из различитих компоненти које омогућавају бољу контролу тока. Радни токови такође омогућавају **оркестрацију више агената** и **checkpointing** за чување стања радног тока.

Основне компоненте радног тока су:

**Извршиоци**

Извршиоци примају улазне поруке, обављају додељене задатке и производе излазну поруку. Ово помера радни ток напред ка завршетку већег задатка. Извршиоци могу бити AI агенти или прилагођена логика.

**Ивица**

Ивице се користе за дефинисање тока порука у радном току. То могу бити:

*Директне ивице* - Једноставне један-на-један везе између извршилаца:

```python
from agent_framework import WorkflowBuilder

builder = WorkflowBuilder()
builder.add_edge(source_executor, target_executor)
builder.set_start_executor(source_executor)
workflow = builder.build()
```

*Условне ивице* - Активирају се након што је испуњен одређени услов. На пример, када собе у хотелу нису доступне, извршилац може предложити друге опције.

*Switch-case ивице* - Усмеравају поруке различитим извршиоцима на основу дефинисаних услова. На пример, ако путнички купац има приоритетни приступ, њихови задаци ће бити обрађени кроз други радни ток.

*Fan-out ивице* - Шаљу једну поруку на више одредишта.

*Fan-in ивице* - Прикупљају више порука од различитих извршилаца и шаљу на једно одредиште.

**Догађаји**

Да би пружио боље посматрање радних токова, MAF нуди уграђене догађаје за извршење укључујући:

- `WorkflowStartedEvent`  - Почетак извршења радног тока
- `WorkflowOutputEvent` - Радни ток производи излаз
- `WorkflowErrorEvent` - Радни ток наилази на грешку
- `ExecutorInvokeEvent`  - Извршилац почиње обраду
- `ExecutorCompleteEvent`  -  Извршилац завршава обраду
- `RequestInfoEvent` - Постављен је захтев

## Напредни MAF обрасци

Горње секције покривају кључне појмове Microsoft Agent Framework. Док градите сложеније агенте, ево неких напредних образаца које треба размотрити:

- **Композиција middleware-а**: Ланац више middleware обрађивача (логовање, ауторизација, ограничење брзине) користећи функције и middleware разговора за прецизну контролу понашања агента.
- **Checkpointing радног тока**: Користите догађаје радног тока и серијализацију за чување и наставак дуготрајних агентских процеса.
- **Динамичан избор алата**: Комбинујте RAG преко описа алата са регистрацијом алата у MAF-у како бисте приказали само релевантне алате по упиту.
- **Пренос између више агената**: Користите ивице радних токова и условно усмерење за оркестрацију преноса задатака између специјализованих агената.

## Примери кода

Примери кода за Microsoft Agent Framework могу се наћи у овом репозиторијуму у датотекама `xx-python-agent-framework` и `xx-dotnet-agent-framework`.

## Имате још питања о Microsoft Agent Framework?

Придружите се [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D) за сусрет са другим учесницима, похађање канцеларијских сати и добијање одговора на ваша питања о AI агентима.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Изјава о одрицању одговорности**:
Овај документ је преведен коришћењем услуге за аутоматски превод [Co-op Translator](https://github.com/Azure/co-op-translator). Иако тежимо тачности, имајте у виду да аутоматски преводи могу садржати грешке или нетачности. Оригинални документ на његовом изворном језику треба сматрати ауторитативним извором. За критичне информације препоручује се професионални људски превод. Нисмо одговорни за било каква неспоразума или погрешна тумачења која произилазе из коришћења овог превода.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->