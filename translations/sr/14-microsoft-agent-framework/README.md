# Истраживање Microsoft Agent Framework-а

![Agent Framework](../../../translated_images/sr/lesson-14-thumbnail.90df0065b9d234ee.webp)

### Увод

Ова лекција ће обухватити:

- Разумевање Microsoft Agent Framework-а: Кључне карактеристике и вредност  
- Истраживање кључних појмова Microsoft Agent Framework-а
- Напредни MAF обрасци: радни токови, посреднички софтвер и меморија

## Циљеви учења

Након завршетка ове лекције, знаћете како да:

- Креирате производно спремне AI агенте користећи Microsoft Agent Framework
- Примените основне карактеристике Microsoft Agent Framework-а на своје агентске случајеве коришћења
- Користите напредне обрасце укључујући радне токове, посреднички софтвер и праћење

## Примери кода 

Примери кода за [Microsoft Agent Framework (MAF)](https://learn.microsoft.com/en-us/agent-framework/overview/?wt.mc_id=youtube_26688_organicsocial_reactor&pivots=programming-language-python) можете пронаћи у овом репозиторијуму у фајловима `xx-python-agent-framework` и `xx-dotnet-agent-framework`.

## Разумевање Microsoft Agent Framework-а

![Framework Intro](../../../translated_images/sr/framework-intro.077af16617cf130c.webp)

[Microsoft Agent Framework (MAF)](https://learn.microsoft.com/en-us/agent-framework/overview/?wt.mc_id=youtube_26688_organicsocial_reactor&pivots=programming-language-python) је јединствени оквир компаније Microsoft за креирање AI агената. Он омогућава флексибилност да се реше широк спектар агентских случајева коришћења примењених у производним и истраживачким срединама, укључујући:

- **Секвенцијална оркестрација агената** у сценаријима где су потребни корак по корак радни токови.
- **Паралелна оркестрација** у сценаријима где агенти морају истовремено да обаве задатке.
- **Оркестрација групног ћаскања** у сценаријима где агенти могу сарађивати на једном задатку.
- **Оркестрација преноса задатака** у сценаријима где агенти предају задатке један другом како се подзадатци завршавају.
- **Магнетна оркестрација** у сценаријима где агент менаџер креира и мења листу задатака и рукује координацијом подагената да заврше задатак.

Да би омогућио испоруку AI агената у производњи, MAF такође укључује функције за:

- **Праћење** коришћењем OpenTelemetry-а где свака акција AI агента укључујући позиве алата, кораке оркестрације, токове размишљања и праћење перформанси путем Microsoft Foundry контролних табли.
- **Безбедност** смештањем агената нативно у Microsoft Foundry, који укључује контроле безбедности као што су приступ заснован на улогама, руковање приватним подацима и уграђена заштита садржаја.
- **Издржљивост** јер агентски задаци и радни токови могу да паузирају, наставе и опораве се од грешака што омогућава дуготрајне процесе.
- **Контролу** јер су подржани радни токови са човеком у петљи где се задаци означавају као захтевају људско одобрење.

Microsoft Agent Framework је такође фокусиран на међусобну повезивост кроз:

- **Бити независан од облака** - Агенти могу да раде у контејнерима, локално и преко различитих облака.
- **Бити независан од провајдера** - Агенти могу бити креирани помоћу омиљеног SDK-а укључујући Azure OpenAI и OpenAI.
- **Интегрисати отворене стандарде** - Агенти могу користити протоколе као што су Agent-to-Agent (A2A) и Model Context Protocol (MCP) за откривање и коришћење других агената и алата.
- **Плугин који конектори** - Могу бити остварене везе са сервисима за податке и меморију као што су Microsoft Fabric, SharePoint, Pinecone и Qdrant.

Хајде да погледамо како су ове функционалности примењене на неке главне појмове Microsoft Agent Framework-а.

## Кључни појмови Microsoft Agent Framework-а

### Агенти

![Agent Framework](../../../translated_images/sr/agent-components.410a06daf87b4fef.webp)


**Креирање агената**

Креирање агената се врши дефинисањем сервиса за извлачење закључака (LLM провајдер), низа инструкција које AI агент треба да прати, и додељеног `name`:


```python
agent = AzureOpenAIChatClient(credential=AzureCliCredential()).create_agent( instructions="You are good at recommending trips to customers based on their preferences.", name="TripRecommender" )
```

Горњи пример користи `Azure OpenAI` али агенти се могу креирати коришћењем разних сервиса укључујући и `Microsoft Foundry Agent Service`:

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

или [MiniMax](https://platform.minimaxi.com/), који обезбеђује API компатибилан са OpenAI и има велике контекстуалне прозоре (до 204К токена):

```python
agent = OpenAIChatClient(base_url="https://api.minimax.io/v1", api_key=os.environ["MINIMAX_API_KEY"], model_id="MiniMax-M3").create_agent( name="HelpfulAssistant", instructions="You are a helpful assistant.", )
```

или удаљене агенте користећи A2A протокол:

```python
agent = A2AAgent( name=agent_card.name, description=agent_card.description, agent_card=agent_card, url="https://your-a2a-agent-host" )
```

**Покретање агената**

Агенти се покрећу коришћењем метода `.run` или `.run_stream` за одговарајуће нестримоване или стримоване одговоре.

```python
result = await agent.run("What are good places to visit in Amsterdam?")
print(result.text)
```

```python
async for update in agent.run_stream("What are the good places to visit in Amsterdam?"):
    if update.text:
        print(update.text, end="", flush=True)

```

Свако покретање агента може имати и опције за прилагођавање параметара као што су `max_tokens` које агент користи, `tools` које агент може позивати, па чак и сам `model` који се користи за агента.

Ово је корисно у случајевима када су потребни одређени модели или алати за извршење задатка корисника.

**Алатке**

Алатке се могу дефинисати и при дефинисању агента:

```python
def get_attractions( location: Annotated[str, Field(description="The location to get the top tourist attractions for")], ) -> str: """Get the top tourist attractions for a given location.""" return f"The top attractions for {location} are." 


# Када се креира ChatAgent директно

agent = ChatAgent( chat_client=OpenAIChatClient(), instructions="You are a helpful assistant", tools=[get_attractions]

```

а такође и при покретању агента:

```python

result1 = await agent.run( "What's the best place to visit in Seattle?", tools=[get_attractions] # Алат обезбеђен само за ову вожњу )
```

**Нитови агената**

Нитови агената се користе за руковање разговорима са више корака. Нитови се могу креирати на два начина:

- Коришћењем `get_new_thread()` што омогућава да нит буде сачувана током времена
- Аутоматским креирањем нити приликом покретања агента где нит траје само током текућег покретања.

Код за креирање нити изгледа овако:

```python
# Креирајте нови нит.
thread = agent.get_new_thread() # Покрените агента са нишком.
response = await agent.run("Hello, I am here to help you book travel. Where would you like to go?", thread=thread)

```

Потом нит можете серијализовати како бисте је сачували за каснију употребу:

```python
# Креирајте нови нит.
thread = agent.get_new_thread() 

# Покрените агента са нитима.

response = await agent.run("Hello, how are you?", thread=thread) 

# Сериализујте нит за складиштење.

serialized_thread = await thread.serialize() 

# Десериализујте стање нити након учитавања из складишта.

resumed_thread = await agent.deserialize_thread(serialized_thread)
```

**Средњи слој агента (Agent Middleware)**

Агенти интерагују са алаткама и LLM-овима да би извршили задатке корисника. У неким сценаријима желимо да извршимо или пратимо радње између ових интеракција. Средњи слој агента нам омогућава ово кроз:

*Функцијски средњи слој*

Овај средњи слој нам дозвољава да извршимо неку акцију између агента и функције/алата који ће бити позивани. Пример када се ово користи јесте када желите да забележите позив функције.

У следећем коду `next` одређује да ли треба позвати следећи средњи слој или саму функцију.

```python
async def logging_function_middleware(
    context: FunctionInvocationContext,
    next: Callable[[FunctionInvocationContext], Awaitable[None]],
) -> None:
    """Function middleware that logs function execution."""
    # Предобрада: Логовање пре извршења функције
    print(f"[Function] Calling {context.function.name}")

    # Настави на следећи middleware или извршење функције
    await next(context)

    # Постобрада: Логовање након извршења функције
    print(f"[Function] {context.function.name} completed")
```

*Чат средњи слој*

Овај средњи слој нам дозвољава да извршимо или забележимо акцију између агента и захтева између LLM-а.

Ово садржи важне информације као што су `messages` које се шаљу AI сервису.

```python
async def logging_chat_middleware(
    context: ChatContext,
    next: Callable[[ChatContext], Awaitable[None]],
) -> None:
    """Chat middleware that logs AI interactions."""
    # Предобрада: Логовање пре позива АИ-а
    print(f"[Chat] Sending {len(context.messages)} messages to AI")

    # Наставак ка следећем посреднику или АИ услузи
    await next(context)

    # Потоња обрада: Логовање након одговора АИ-а
    print("[Chat] AI response received")

```

**Меморија агента**

Као што је покривено лекцијом `Agentic Memory`, меморија је важан елемент који омогућава агенту да ради у различитим контекстима. MAF нуди неколико различитих типова меморије:

*Меморија у опису (In-Memory Storage)*

Ово је меморија смештена у нитима током извршавања апликације.

```python
# Креирај нови нит.
thread = agent.get_new_thread() # Покрени агента са нит.
response = await agent.run("Hello, I am here to help you book travel. Where would you like to go?", thread=thread)
```

*Постојане поруке (Persistent Messages)*

Ова меморија се користи за чување историје разговора кроз различите сесије. Дефинише се коришћењем `chat_message_store_factory` :

```python
from agent_framework import ChatMessageStore

# Креирајте прилагођено складиште порука
def create_message_store():
    return ChatMessageStore()

agent = ChatAgent(
    chat_client=OpenAIChatClient(),
    instructions="You are a Travel assistant.",
    chat_message_store_factory=create_message_store
)

```

*Динамичка меморија*


Ово сећање се додаје у контекст пре него што агенти почну да раде. Ова сећања могу бити сачувана у спољним сервисима као што је mem0:

```python
from agent_framework.mem0 import Mem0Provider

# Користећи Mem0 за напредне могућности меморије
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

Посматрање је важно за израду поузданих и одрживих агенцијских система. MAF се интегрише са OpenTelemetry како би пружио праћење и бројаче за боље посматрање.

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

Радни токови се састоје од различитих компоненти које омогућавају бољу контролу протока. Радни токови такође омогућавају **оркестрацију више агената** и **снимање тачака контроле** за чување стања радног тока.

Основне компоненте радног тока су:

**Извршиоци**

Извршиоци примају улазне поруке, извршавају додељене задатке, а затим производе излазну поруку. Ово помера радни ток напред ка завршетку већег задатка. Извршиоци могу бити AI агенти или прилагођена логика.

**Везе**

Везе се користе за дефинисање протока порука у радном току. Оне могу бити:

*Директне везе* - Једноставне један-на-један везе између извршилаца:

```python
from agent_framework import WorkflowBuilder

builder = WorkflowBuilder()
builder.add_edge(source_executor, target_executor)
builder.set_start_executor(source_executor)
workflow = builder.build()
```

*Условне везе* - Активирају се након испуњења одређеног услова. На пример, када собе у хотелу нису доступне, извршилац може предложити друге опције.

*Switch-case везе* - Усмеравате поруке на различите извршиоце на основу дефинисаних услова. На пример, ако путник има приоритетни приступ, њихови задаци ће бити обрађени кроз други радни ток.

*Fan-out везе* - Пошаљите једну поруку више циљева.

*Fan-in везе* - Прикупите више порука са различитих извршилаца и пошаљите их једном циљу.

**Догађаји**

Да би се обезбедило боље посматрање радних токова, MAF нуди уграђене догађаје за извршење, укључујући:

- `WorkflowStartedEvent`  - Радни ток почиње
- `WorkflowOutputEvent` - Радни ток производи излаз
- `WorkflowErrorEvent` - Радни ток наилази на грешку
- `ExecutorInvokeEvent`  - Извршилац почиње обраду
- `ExecutorCompleteEvent`  - Извршилац завршава обраду
- `RequestInfoEvent` - Захтев је издат

## Напредни MAF обрасци

Горње секције покривају кључне појмове Microsoft Agent Framework-а. Када градите сложеније агенте, ево неких напредних облика које треба узети у обзир:

- **Композиција посредника**: Ланцирање више посредника (логовање, аутентификација, ограничење брзине) коришћењем функцијских и чат посредника за детаљну контролу понашања агента.
- **Снимање тачака контроле у радном току**: Коришћење догађаја радних токова и серијализације за чување и наставак дуготрајних агенцијских процеса.
- **Динамички избор алата**: Комбиновање RAG-а над описима алата са MAF-овом регистрацијом алата за приказивање само релевантних алата по упиту.
- **Пренос између више агената**: Коришћење веза радног тока и условног усмеравања за оркестрацију преноса између специјализованих агената.

## Хостирање LangChain / LangGraph агената на Microsoft Foundry-у

Microsoft Agent Framework је **интероперабилан са различитим фрејмворцима** — нисте ограничени на агенте написане само са MAF-ом. Ако већ имате агента направљеног са **LangChain** или **LangGraph**, можете га покренути као **Microsoft Foundry хостираног агента** тако да Foundry управља временом извршења, сесијама, скалирањем, идентитетом и крајњим тачкама протокола за вас, док ваша агенцијска логика остаје у LangGraph-у.

Ово се ради са `langchain_azure_ai.agents.hosting` пакетом, који излаже компајлирани LangGraph граф преко истих протокола које користе Foundry хостирани агенти.

**1. Инсталирајте хостинг екстра:**

```bash
pip install -U "langchain-azure-ai[hosting]>=1.2.4" azure-identity
```

`hosting` екстра инсталира библиотеке Foundry протокола: `azure-ai-agentserver-responses` (OpenAI-компатибилна `/responses` крајња тачка) и `azure-ai-agentserver-invocations` (општа `/invocations` крајња тачка).

**2. Изаберите хостинг протокол:**

| Протокол | Класа хоста | Крајња тачка | Користи се када |
|----------|-------------|-------------|-----------------|
| **Responses** | `ResponsesHostServer` | `/responses` | Желите OpenAI-компатибилни чат, стреаминг, историју одговора и нитовање разговора — препоручени подразумевани за разговорне агенте. |
| **Invocations** | `InvocationsHostServer` | `/invocations` | Потребан вам је прилагођени JSON облик, вебхук-стил крајња тачка или обрада ван разговора. |

Пошто је **Responses API примарни API за агенцијски развој у Foundry-у**, почните са `ResponsesHostServer` за већину агената.

**3. Конфигуришите променљиве окружења** (`az login` прво да `DefaultAzureCredential` може да се аутентификује):

```bash
export FOUNDRY_PROJECT_ENDPOINT="https://<resource>.services.ai.azure.com/api/projects/<project>"
export FOUNDRY_MODEL_NAME="gpt-5-mini"
```

Када агент касније ради као хостирани агент у Foundry-у, платформа аутоматски убацује `FOUNDRY_PROJECT_ENDPOINT`.

**4. Изложите LangGraph агента преко Responses протокола:**

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

    # ChatOpenAI овде циља на OpenAI-компатибилан (Responses) крајњи тачку пројекта Foundry.
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

Покрените га локално са `python main.py`, затим пошаљите Responses захтев на `http://localhost:8088/responses`.

**Кључна понашања:**

- **Разговори**: Клијенти настављају разговор прослеђивањем `previous_response_id` или `conversation` ID. Ако је ваш граф компајлиран са LangGraph checkpointer-ом, Foundry кључује стање разговора уз тачку контроле (користите дуготрајни checkpointer у производњи; `MemorySaver` је довољан за локално тестирање).
- **Човек-у-лусуци**: Ако ваш граф користи LangGraph `interrupt()`, `ResponsesHostServer` приказује непоступљени прекид као Responses `function_call` / `mcp_approval_request` ставку, а клијенти настављају са одговарајућим `function_call_output` / `mcp_approval_response`.
- **Деплој у Foundry**: Користите Azure Developer CLI — `azd ext install azure.ai.agents`, `azd ai agent init -m <manifest>`, `azd ai agent run` (локално, захтева Docker), затим `azd provision` и `azd deploy`. Деплој хостираног агента захтева улогу **Foundry Project Manager**.

Рун-ујемљива верзија овог примера налази се у [code-samples/14-langchain-hosted-agent.py](../../../14-microsoft-agent-framework/code-samples/14-langchain-hosted-agent.py). За цео преглед (Invocations протокол, прилагођени шеме захтева и решавање проблема), погледајте [Host LangGraph agents as Foundry hosted agents](https://learn.microsoft.com/azure/foundry/how-to/develop/langchain-hosted-agents).

## Примери кода 

Примери кода за Microsoft Agent Framework могу се наћи у овом репозиторијуму у фајловима `xx-python-agent-framework` и `xx-dotnet-agent-framework`.

## Имате још питања о Microsoft Agent Framework-у?

Придружите се [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D) да бисте се срели са другим ученицима, похађали радне сате и добили одговоре на питања о AI агентима.
## Претходна лекција

[Memory for AI Agents](../13-agent-memory/README.md)

## Следећа лекција


[Прављење агената за коришћење рачунара (CUA)](../15-browser-use/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Изјава о одрицању одговорности**:
Овај документ је преведен коришћењем услуге за аутоматски превод [Co-op Translator](https://github.com/Azure/co-op-translator). Иако тежимо тачности, имајте у виду да аутоматски преводи могу садржати грешке или нетачности. Оригинални документ на његовом изворном језику треба сматрати ауторитативним извором. За критичне информације препоручује се професионални људски превод. Нисмо одговорни за било каква неспоразума или погрешна тумачења која произилазе из коришћења овог превода.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->