# Истраживање Microsoft Agent Framework-а

![Agent Framework](../../../translated_images/sr/lesson-14-thumbnail.90df0065b9d234ee.webp)

### Увод

Ова лекција ће обухватити:

- Разумевање Microsoft Agent Framework-а: Кључне карактеристике и вредност  
- Истраживање кључних концепата Microsoft Agent Framework-а
- Напредни МАФ обрасци: Радни токови, посредници и меморија

## Циљеви учења

Након завршетка ове лекције, знаћете како да:

- Креирате AI агенте спремне за производњу користећи Microsoft Agent Framework
- Примените основне карактеристике Microsoft Agent Framework-а на ваше агентске случајеве употребе
- Користите напредне обрасце укључујући радне токове, посреднике и посматрање

## Примери кода 

Примери кода за [Microsoft Agent Framework (MAF)](https://learn.microsoft.com/en-us/agent-framework/overview/?wt.mc_id=youtube_26688_organicsocial_reactor&pivots=programming-language-python) могу се пронаћи у овом репозиторијуму у датотекама `xx-python-agent-framework` и `xx-dotnet-agent-framework`.

## Разумевање Microsoft Agent Framework-а

![Framework Intro](../../../translated_images/sr/framework-intro.077af16617cf130c.webp)

[Microsoft Agent Framework (MAF)](https://learn.microsoft.com/en-us/agent-framework/overview/?wt.mc_id=youtube_26688_organicsocial_reactor&pivots=programming-language-python) је Microsoft-ов јединствени оквир за изградњу AI агената. Пружа флексибилност да се реше разни агентски случајеви употребе који се виде у производним и истраживачким окружењима укључујући:

- **Секвенцијална оркестрација агената** у сценаријима где су потребни радни токови корак-по-корак.
- **Паралелна оркестрација** у сценаријима где агенти треба да заврше задатке у исто време.
- **Оркестрација групног ћаскања** у сценаријима где агенти могу заједно сарађивати на једном задатку.
- **Оркестрација преноса задатка** у сценаријима где агенти један другом предају задатак како се подзадатци завршавају.
- **Магнетна оркестрација** у сценаријима где менаџер агент креира и мења листу задатака и управља координацијом подагената да заврше задатак.

За испоруку AI агената у производњи, MAF такође укључује могућности за:

- **Посматрање** преко коришћења OpenTelemetry где свака акција AI агента укључујући позиве алата, кораке оркестрације, токове разматрања и праћење перформанси преко Microsoft Foundry контролних табли.
- **Безбедност** домаћином агената директно на Microsoft Foundry што укључује безбедносне контроле као што су приступ заснован на улогама, руковање приватним подацима и уграђена безбедност садржаја.
- **Издржљивост** јер се агентске нити и радни токови могу паузирати, наставити и опоравити од грешака што омогућава дуготрајне процесе.
- **Контролу** јер су подржани људски циклуси где се задаци означавају као они који захтевају људско одобрење.

Microsoft Agent Framework је такође усмерен на интероперабилност кроз:

- **Бити облачно-агностичан** - Агенти могу радити у контејнерима, локално и на више различитих облака.
- **Бити провајдер-агностичан** - Агенти се могу креирати преко вашег омиљеног SDK укључујући Azure OpenAI и OpenAI
- **Интеграцију отворених стандарда** - Агенти могу користити протоколе као што су Agent-to-Agent (A2A) и Model Context Protocol (MCP) за откривање и коришћење других агената и алата.
- **Плугинова и конектора** - Могуће су везе ка сервисима података и меморије као што су Microsoft Fabric, SharePoint, Pinecone и Qdrant.

Погледајмо како се ове карактеристике примењују на неке од кључних концепата Microsoft Agent Framework-а.

## Кључни концепти Microsoft Agent Framework-а

### Агенти

![Agent Framework](../../../translated_images/sr/agent-components.410a06daf87b4fef.webp)


**Креирање агената**

Креирање агената се врши дефинисањем инференцијске услуге (ЛЛМ провајдер), скупа упутстава која АИ агент треба да прати, и додељеним `име`:


```python
agent = AzureOpenAIChatClient(credential=AzureCliCredential()).create_agent( instructions="You are good at recommending trips to customers based on their preferences.", name="TripRecommender" )
```

Горње је коришћење `Azure OpenAI`, али агенти се могу креирати уз помоћ различитих услуга укључујући `Microsoft Foundry Agent Service`:

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

или [MiniMax](https://platform.minimaxi.com/), који пружа OpenAI-компатибилан API са великим контекстним прозорима (до 204К токена):

```python
agent = OpenAIChatClient(base_url="https://api.minimax.io/v1", api_key=os.environ["MINIMAX_API_KEY"], model_id="MiniMax-M3").create_agent( name="HelpfulAssistant", instructions="You are a helpful assistant.", )
```

или удаљени агенти који користе A2A протокол:

```python
agent = A2AAgent( name=agent_card.name, description=agent_card.description, agent_card=agent_card, url="https://your-a2a-agent-host" )
```

**Покретање агената**

Агенти се покрећу помоћу метода `.run` или `.run_stream` за одговарајуће не-стриминг или стриминг одговоре.

```python
result = await agent.run("What are good places to visit in Amsterdam?")
print(result.text)
```

```python
async for update in agent.run_stream("What are the good places to visit in Amsterdam?"):
    if update.text:
        print(update.text, end="", flush=True)

```

Свако покретање агента такође може имати опције за прилагођавање параметара као што су `max_tokens` које агент користи, `tools` које агент може да позове, па чак и сам `model` који се користи за агента.

Ово је корисно у случајевима када су специфични модели или алати потребни за извршење задатка корисника.

**Алатке**

Алатке се могу дефинисати и приликом дефинисања агента:

```python
def get_attractions( location: Annotated[str, Field(description="The location to get the top tourist attractions for")], ) -> str: """Get the top tourist attractions for a given location.""" return f"The top attractions for {location} are." 


# Када се ChatAgent директно креира

agent = ChatAgent( chat_client=OpenAIChatClient(), instructions="You are a helpful assistant", tools=[get_attractions]

```

и такође приликом покретања агента:

```python

result1 = await agent.run( "What's the best place to visit in Seattle?", tools=[get_attractions] # Алат пружен само за ово покретање )
```

**Теме агената**

Теме агената се користе за руковање вишекратним дијалозима. Теме се могу креирати на следеће начине:

- Коришћењем `get_new_thread()` што омогућава да се тема чува током времена
- Аутоматским креирањем теме приликом покретања агента и да тема траје само током текућег покретања.

За креирање теме, код изгледа овако:

```python
# Креирајте нови нити.
thread = agent.get_new_thread() # Покрените агента са нитима.
response = await agent.run("Hello, I am here to help you book travel. Where would you like to go?", thread=thread)

```

Затим можете серијализовати тему да бисте је сачували за каснију употребу:

```python
# Креирајте нови нит.
thread = agent.get_new_thread() 

# Покрените агента са нити.

response = await agent.run("Hello, how are you?", thread=thread) 

# Сериализујте нит за складиштење.

serialized_thread = await thread.serialize() 

# Десериализујте стање нити након учитавања из складишта.

resumed_thread = await agent.deserialize_thread(serialized_thread)
```

**Мидлвер агената**

Агенти комуницирају са алатима и ЛЛМ-овима да би извршили задатке корисника. У одређеним сценаријима желимо да извршимо или пратимо нешто у интеракцијама између ових елемената. Мидлвер агената нам омогућава да то урадимо кроз:

*Функциони мидлвер*

Овај мидлвер нам дозвољава да извршимо радњу између агента и функције/алата који ће агент позивати. Пример када би ово било корисно је ако желите да водите евиденцију о позиву функције.

У једном коду испод, `next` одређује да ли ће следећи мидлвер или сама функција бити позвани.

```python
async def logging_function_middleware(
    context: FunctionInvocationContext,
    next: Callable[[FunctionInvocationContext], Awaitable[None]],
) -> None:
    """Function middleware that logs function execution."""
    # Пре-обрада: Логовање пре извршења функције
    print(f"[Function] Calling {context.function.name}")

    # Настави на следећи middleware или извршење функције
    await next(context)

    # Пост-обрада: Логовање након извршења функције
    print(f"[Function] {context.function.name} completed")
```

*Чат мидлвер*

Овај мидлвер нам дозвољава да извршимо или евидентирамо радњу између агента и захтева према ЛЛМ.

Ово садржи важне информације као што су `messages` који се шаљу AI услузи.

```python
async def logging_chat_middleware(
    context: ChatContext,
    next: Callable[[ChatContext], Awaitable[None]],
) -> None:
    """Chat middleware that logs AI interactions."""
    # Предобрада: Логовање пре позива вештачке интелигенције
    print(f"[Chat] Sending {len(context.messages)} messages to AI")

    # Наставите на следећи посреднички слој или услугу вештачке интелигенције
    await next(context)

    # Постобрада: Логовање након одговора вештачке интелигенције
    print("[Chat] AI response received")

```

**Меморија агената**

Као што је објашњено у лекцији о `Agentic Memory`, меморија је важан елемент који омогућава агенту да ради у различитим контекстима. MAF нуди неколико врста меморија:

*Меморија у меморији (In-Memory Storage)*

Ово је меморија која се чува у темама током извршавања апликације.

```python
# Креирајте нови нит.
thread = agent.get_new_thread() # Покрените агента са нити.
response = await agent.run("Hello, I am here to help you book travel. Where would you like to go?", thread=thread)
```

*Персистентне поруке*

Ова меморија се користи за чување историје разговора преко различитих сесија. Дефинише се помоћу `chat_message_store_factory`:

```python
from agent_framework import ChatMessageStore

# Креирај прилагођену продавницу порука
def create_message_store():
    return ChatMessageStore()

agent = ChatAgent(
    chat_client=OpenAIChatClient(),
    instructions="You are a Travel assistant.",
    chat_message_store_factory=create_message_store
)

```

*Динамичка меморија*


Ова меморија се додаје у контекст пре покретања агената. Ове меморије могу бити смештене у спољне сервисе као што је mem0:

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

Посматрање је важно за изградњу поузданих и одрживих агентских система. MAF се интегрише са OpenTelemetry како би обезбедио трасисање и метре за боље посматрање.

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

MAF нуди радне токове који су унапред дефинисане кораке за завршетак задатка и укључују AI агенте као компоненте у тим корацима.

Радни токови се састоје од различитих компоненти које омогућавају бољу контролу тока. Радни токови такође омогућавају **оркестрацију више агената** и **checkpointing** за чување стања радног тока.

Кључне компоненте радног тока су:

**Извршиоци**

Извршиоци примају улазне поруке, извршавају додељене задатке и затим производе излазну поруку. Ово помера радни ток напред ка завршетку већег задатка. Извршиоци могу бити AI агент или прилагођена логика.

**Ивице**

Ивице се користе за дефинисање тока порука у радном току. Оне могу бити:

*Директне ивице* - Једноставне везе један-на-један између извршилаца:

```python
from agent_framework import WorkflowBuilder

builder = WorkflowBuilder()
builder.add_edge(source_executor, target_executor)
builder.set_start_executor(source_executor)
workflow = builder.build()
```

*Условне ивице* - Активирају се након испуњења одређеног услова. На пример, када собе у хотелу нису доступне, извршилац може предложити друге опције.

*Switch-case ивице* - Умаршира поруке ка различитим извршиоцима на основу дефинисаних услова. На пример, ако корисник путовања има приоритетни приступ, њихови задаци ће се обрађивати преко другог радног тока.

*Fan-out ивице* - Шаљу једну поруку више циљевима.

*Fan-in ивице* - Прикупљају више порука од различитих извршилаца и шаљу једном циљу.

**Догађаји**

Да би пружио боље посматрање радних токова, MAF нуди уграђене догађаје за извршење, укључујући:

- `WorkflowStartedEvent`  - Започиње извршење радног тока
- `WorkflowOutputEvent` - Радни ток производи излаз
- `WorkflowErrorEvent` - Радни ток наилази на грешку
- `ExecutorInvokeEvent`  - Извршилац почиње обраду
- `ExecutorCompleteEvent`  -  Извршилац завршава обраду
- `RequestInfoEvent` - Издаје се захтев

## Напредни обрасци MAF

Горње секције покривају кључне појмове Microsoft Agent Framework. Како правите комплексније агенте, ево неких напредних образаца које треба размотрити:

- **Композиција middleware-а**: Повежите више middleware handlere (логовање, аутентификација, ограничење бројчане стопе) користећи функције и chat middleware за прецизну контролу понашања агента.
- **Checkpointing радног тока**: Користите догађаје радног тока и серијализацију за чување и наставак дугорочних процеса агента.
- **Динамичан избор алата**: Комбинујте RAG преко описа алата са MAF регистрацијом алата како бисте приказали само релевантне алате по упиту.
- **Пренос између више агената**: Користите ивице радног тока и условно усмеравање за оркестрацију преноса између специјализованих агената.

## Хостовање LangChain / LangGraph агената на Microsoft Foundry

Microsoft Agent Framework је **framework-interoperable** — нисте ограничени на агенте написане са MAF. Ако већ имате агента изграђеног са **LangChain** или **LangGraph**, можете га покренути као **Microsoft Foundry hostованог агента** тако да Foundry управља покретањем, сесијама, скалирањем, идентитетом и крајњим тачкама протокола, док ваша агенцијска логика остаје у LangGraph.

Ово се постиже помоћу `langchain_azure_ai.agents.hosting` пакета, који изложи састављен LangGraph граф преко истих протокола који користе Foundry hostовани агенти.

**1. Инсталирајте hosting extra:**

```bash
pip install -U "langchain-azure-ai[hosting]>=1.2.4" azure-identity
```

`hosting` extra инсталира Foundry protocol библиотеке: `azure-ai-agentserver-responses` (OpenAI-компатибилна `/responses` крајња тачка) и `azure-ai-agentserver-invocations` (генеричка `/invocations` крајња тачка).

**2. Изаберите хостинг протокол:**

| Протокол | Хост класа | Крајња тачка | Користи када |
|----------|------------|-------------|--------------|
| **Responses** | `ResponsesHostServer` | `/responses` | Желите OpenAI-компатибилни чат, стриминг, историју одговора и нитовање разговора — препоручени подразумевани за разговорне агенте. |
| **Invocations** | `InvocationsHostServer` | `/invocations` | Потребан вам је прилагођени JSON формат, webhook-стил крајња тачка или неразговорна обрада. |

Због тога што је **Responses API примарни API за агентски развој у Foundry**, започните са `ResponsesHostServer` за већину агената.

**3. Конфигуришите променљиве окружења** (`az login` прво да би `DefaultAzureCredential` могао да аутентификује):

```bash
export FOUNDRY_PROJECT_ENDPOINT="https://<resource>.services.ai.azure.com/api/projects/<project>"
export FOUNDRY_MODEL_NAME="gpt-5-mini"
```

Када агент касније ради као hostovani агент у Foundry, платформа аутоматски убацује `FOUNDRY_PROJECT_ENDPOINT`.

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

    # ChatOpenAI овде циља OpenAI-компатибилну (Responses) крајњу тачку Foundry пројекта.
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

Покрените локално са `python main.py`, затим пошаљите Responses захтев на `http://localhost:8088/responses`.

**Кључна понашања:**

- **Разговори**: Клијенти настављају разговор прослеђивањем `previous_response_id` или `conversation` ID-ја. Ако је ваш граф састављен са LangGraph checkpoint-ом, Foundry везује стање разговора за checkpoint (користите трајни checkpoint у продукцији; `MemorySaver` је добар за локално тестирање).
- **Човек у петљи**: Ако ваш граф користи LangGraph `interrupt()`, `ResponsesHostServer` приказује предстојеће прекиде као Responses `function_call` / `mcp_approval_request` ставке, а клијенти настављају са одговарајућим `function_call_output` / `mcp_approval_response`.
- **Деплој на Foundry**: Користите Azure Developer CLI — `azd ext install azure.ai.agents`, `azd ai agent init -m <manifest>`, `azd ai agent run` (локално, захтева Docker), затим `azd provision` и `azd deploy`. Деплој hostovanih агената захтева улогу **Foundry Project Manager**.

Извршна верзија овог примера налази се у [code-samples/14-langchain-hosted-agent.py](../../../14-microsoft-agent-framework/code-samples/14-langchain-hosted-agent.py). За комплетан водич (Invocations протокол, прилагођене схеме захтева и решавање проблема), погледајте [Host LangGraph agents as Foundry hosted agents](https://learn.microsoft.com/azure/foundry/how-to/develop/langchain-hosted-agents).

## Примери кода 

Примере кода за Microsoft Agent Framework можете пронаћи у овом репозиторијуму у фајловима `xx-python-agent-framework` и `xx-dotnet-agent-framework`.

## Имате још питања о Microsoft Agent Framework?

Придружите се [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D) да се упознате са другим учесницима, присуствујете канцеларијским часовима и добијете одговоре на питања везана за AI агенте.
## Претходна лекција

[Memory for AI Agents](../13-agent-memory/README.md)

## Следећа лекција


[Прављење агената за коришћење рачунара (CUA)](../15-browser-use/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Изјава о одрицању одговорности**:
Овај документ је преведен коришћењем услуге за аутоматски превод [Co-op Translator](https://github.com/Azure/co-op-translator). Иако тежимо тачности, имајте у виду да аутоматски преводи могу садржати грешке или нетачности. Оригинални документ на његовом изворном језику треба сматрати ауторитативним извором. За критичне информације препоручује се професионални људски превод. Нисмо одговорни за било каква неспоразума или погрешна тумачења која произилазе из коришћења овог превода.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->