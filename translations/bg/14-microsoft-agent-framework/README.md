# Изследване на Microsoft Agent Framework

![Agent Framework](../../../translated_images/bg/lesson-14-thumbnail.90df0065b9d234ee.webp)

### Въведение

Този урок ще обхване:

- Разбиране на Microsoft Agent Framework: Основни характеристики и стойност  
- Изследване на ключовите концепции на Microsoft Agent Framework
- Разширени MAF шаблони: Работни потоци, междинен софтуер и памет

## Цели за учене

След завършване на този урок, ще знаете как да:

- Създавате AI агенти, готови за продукция, използвайки Microsoft Agent Framework
- Прилагате основните функции на Microsoft Agent Framework към вашите агентски случаи на използване
- Използвате разширени шаблони включително работни потоци, междинен софтуер и наблюдаемост

## Примерен код

Примерите за код за [Microsoft Agent Framework (MAF)](https://aka.ms/ai-agents-beginners/agent-framework) могат да бъдат намерени в това хранилище в файловете `xx-python-agent-framework` и `xx-dotnet-agent-framework`.

## Разбиране на Microsoft Agent Framework

![Framework Intro](../../../translated_images/bg/framework-intro.077af16617cf130c.webp)

[Microsoft Agent Framework (MAF)](https://aka.ms/ai-agents-beginners/agent-framework) е унифицирана рамка на Microsoft за създаване на AI агенти. Тя предлага гъвкавост за адресиране на широкото разнообразие от агентски случаи на използване, наблюдавани както в продукционни, така и в изследователски среди, включително:

- **Последователна агентна оркестрация** в сценарии, където са нужни работни потоци стъпка по стъпка.
- **Паралелна оркестрация** в сценарии, където агентите трябва да завършат задачи едновременно.
- **Оркестрация на групов чат** в сценарии, където агентите могат да си сътрудничат за една задача.
- **Оркестрация на препредаване** в сценарии, където агентите предават задачата един на друг, докато подзадачите се изпълняват.
- **Магнитна оркестрация** в сценарии, където управляващ агент създава и модифицира списък със задачи и координира подагенти за изпълнението на задачата.

За предоставяне на AI агенти в продукция, MAF включва и функции за:

- **Наблюдаемост** чрез използване на OpenTelemetry, където всяко действие на AI агента, включително извикване на инструменти, стъпки на оркестрация, потоци на размисъл и мониторинг на производителността чрез Microsoft Foundry табла.
- **Сигурност** чрез хостинг на агентите нативно в Microsoft Foundry, което включва контрол на достъпа на база роли, обработка на лични данни и вградена безопасност на съдържанието.
- **Издръжливост** тъй като агентните нишки и работни потоци могат да бъдат паузирани, възобновявани и възстановявани от грешки, което позволява продължителни процеси.
- **Контрол** тъй като се поддържат работни потоци с човека в цикъла, където задачите са маркирани като изискващи човешко одобрение.

Microsoft Agent Framework се фокусира и върху интероперабилността чрез:

- **Бъдене на облак-независим** - агентите могат да се изпълняват в контейнери, локално и в множество различни облаци.
- **Бъдене на доставчик-независим** - агентите могат да се създават чрез предпочитания SDK, включително Azure OpenAI и OpenAI
- **Интеграция на отворени стандарти** - агентите могат да използват протоколи като Agent-to-Agent (A2A) и Model Context Protocol (MCP) за откриване и използване на други агенти и инструменти.
- **Плъгини и Конектори** - връзки могат да се създават с данни и услуги за памет като Microsoft Fabric, SharePoint, Pinecone и Qdrant.

Нека да разгледаме как тези функции се прилагат към някои основни концепции на Microsoft Agent Framework.

## Ключови концепции на Microsoft Agent Framework

### Агенти

![Agent Framework](../../../translated_images/bg/agent-components.410a06daf87b4fef.webp)

**Създаване на агенти**

Създаването на агенти се извършва чрез дефиниране на услугата за извеждане на изводи (LLM доставчик), 
набор от инструкции за AI агента да следва и зададено `име`:

```python
agent = AzureOpenAIChatClient(credential=AzureCliCredential()).create_agent( instructions="You are good at recommending trips to customers based on their preferences.", name="TripRecommender" )
```

Горният пример използва `Azure OpenAI`, но агентите могат да бъдат създавани с различни услуги, включително `Microsoft Foundry Agent Service`:

```python
AzureAIAgentClient(async_credential=credential).create_agent( name="HelperAgent", instructions="You are a helpful assistant." ) as agent
```

OpenAI `Responses`, `ChatCompletion` API-та

```python
agent = OpenAIResponsesClient().create_agent( name="WeatherBot", instructions="You are a helpful weather assistant.", )
```

```python
agent = OpenAIChatClient().create_agent( name="HelpfulAssistant", instructions="You are a helpful assistant.", )
```

или [MiniMax](https://platform.minimaxi.com/), който предлага OpenAI-съвместим API с големи контекстови прозорци (до 204K токена):

```python
agent = OpenAIChatClient(base_url="https://api.minimax.io/v1", api_key=os.environ["MINIMAX_API_KEY"], model_id="MiniMax-M3").create_agent( name="HelpfulAssistant", instructions="You are a helpful assistant.", )
```

или отдалечени агенти, използващи протокола A2A:

```python
agent = A2AAgent( name=agent_card.name, description=agent_card.description, agent_card=agent_card, url="https://your-a2a-agent-host" )
```

**Изпълнение на агенти**

Агентите се изпълняват чрез методите `.run` или `.run_stream` за ненасочени или потокови отговори.

```python
result = await agent.run("What are good places to visit in Amsterdam?")
print(result.text)
```

```python
async for update in agent.run_stream("What are the good places to visit in Amsterdam?"):
    if update.text:
        print(update.text, end="", flush=True)

```

При всяко изпълнение на агент могат да се зададат опции за персонализиране на параметри като `max_tokens` използвани от агента, `tools`, които агентът може да извиква, и дори самият `модел`, използван от агента.

Това е полезно в случаи, когато са необходими специфични модели или инструменти за изпълнение на задача на потребителя.

**Инструменти**

Инструментите могат да се дефинират както при създаване на агента:

```python
def get_attractions( location: Annotated[str, Field(description="The location to get the top tourist attractions for")], ) -> str: """Get the top tourist attractions for a given location.""" return f"The top attractions for {location} are." 


# Когато се създава ChatAgent директно

agent = ChatAgent( chat_client=OpenAIChatClient(), instructions="You are a helpful assistant", tools=[get_attractions]

```

така и при изпълнение на агента:

```python

result1 = await agent.run( "What's the best place to visit in Seattle?", tools=[get_attractions] # Инструмент, предоставен само за това изпълнение )
```

**Агентни нишки**

Агентните нишки се използват за обработка на разговори с много ходове. Нишките могат да бъдат създадени чрез:

- Използване на `get_new_thread()`, което позволява нишката да се запаметява с течение на времето
- Автоматично създаване на нишка при изпълнение на агент, която да съществува само в рамките на текущото изпълнение.

Кодът за създаване на нишка изглежда така:

```python
# Създайте нов нишка.
thread = agent.get_new_thread() # Стартирайте агента с нишката.
response = await agent.run("Hello, I am here to help you book travel. Where would you like to go?", thread=thread)

```

Нишката може да бъде сериализирана за съхранение и по-късна употреба:

```python
# Създайте нов нишка.
thread = agent.get_new_thread() 

# Стартирайте агента с нишката.

response = await agent.run("Hello, how are you?", thread=thread) 

# Сериализирайте нишката за съхранение.

serialized_thread = await thread.serialize() 

# Десериализирайте състоянието на нишката след зареждане от съхранение.

resumed_thread = await agent.deserialize_thread(serialized_thread)
```

**Междинен софтуер на агента**

Агентите взаимодействат с инструменти и LLM, за да изпълнят задачите на потребителите. В някои сценарии искаме да изпълним действие или да проведем проследяване между тези взаимодействия. Агентният междинен софтуер ни позволява да направим това чрез:

*Функционален междинен софтуер*

Този междинен софтуер ни позволява да изпълним действие между агента и функция/инструмент, който ще извиква. Пример за неговото използване е, когато искаме да направим логване на извикването на функция.

В кода по-долу `next` определя дали да бъде извикан следващия междинен софтуер или самата функция.

```python
async def logging_function_middleware(
    context: FunctionInvocationContext,
    next: Callable[[FunctionInvocationContext], Awaitable[None]],
) -> None:
    """Function middleware that logs function execution."""
    # Предварителна обработка: Запис в лог преди изпълнението на функцията
    print(f"[Function] Calling {context.function.name}")

    # Продължи към следващия междинен софтуер или изпълнение на функцията
    await next(context)

    # Следобработка: Запис в лог след изпълнението на функцията
    print(f"[Function] {context.function.name} completed")
```

*Чат междинен софтуер*

Този междинен софтуер ни позволява да изпълним или логнем действие между агента и заявките към LLM.

Той съдържа важна информация като `messages`, които се изпращат към AI услугата.

```python
async def logging_chat_middleware(
    context: ChatContext,
    next: Callable[[ChatContext], Awaitable[None]],
) -> None:
    """Chat middleware that logs AI interactions."""
    # Предварителна обработка: Запис преди извикване на AI
    print(f"[Chat] Sending {len(context.messages)} messages to AI")

    # Продължете към следващия middleware или AI услуга
    await next(context)

    # Последваща обработка: Запис след отговор от AI
    print("[Chat] AI response received")

```

**Памет на агента**

Както е разгледано в урока „Agentic Memory“, паметта е важен елемент за позволяване на агента да работи в различни контексти. MAF предлага няколко различни вида памет:

*Памет в оперативната памет*

Това е паметта, съхранена в нишките по време на изпълнение на приложението.

```python
# Създайте нов низ.
thread = agent.get_new_thread() # Стартирайте агента с низа.
response = await agent.run("Hello, I am here to help you book travel. Where would you like to go?", thread=thread)
```

*Постоянни съобщения*

Тази памет се използва за съхранение на историята на разговорите през различни сесии. Тя се дефинира чрез `chat_message_store_factory` :

```python
from agent_framework import ChatMessageStore

# Създайте персонализирано хранилище за съобщения
def create_message_store():
    return ChatMessageStore()

agent = ChatAgent(
    chat_client=OpenAIChatClient(),
    instructions="You are a Travel assistant.",
    chat_message_store_factory=create_message_store
)

```

*Динамична памет*

Тази памет се добавя в контекста преди изпълнението на агентите. Тя може да се съхранява в външни услуги като mem0:

```python
from agent_framework.mem0 import Mem0Provider

# Използване на Mem0 за разширени възможности за памет
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

**Наблюдаемост на агента**


Наблюдаемостта е важна за изграждането на надеждни и поддържки системи с агенти. MAF се интегрира с OpenTelemetry за предоставяне на трасировка и метри за по-добра наблюдаемост.

```python
from agent_framework.observability import get_tracer, get_meter

tracer = get_tracer()
meter = get_meter()
with tracer.start_as_current_span("my_custom_span"):
    # направи нещо
    pass
counter = meter.create_counter("my_custom_counter")
counter.add(1, {"key": "value"})
```

### Работни потоци

MAF предлага работни потоци, които са предварително дефинирани стъпки за изпълнение на задача и включват AI агенти като компоненти в тези стъпки.

Работните потоци се състоят от различни компоненти, които позволяват по-добър контрол на потока. Работните потоци също така позволяват **оркестрация с множество агенти** и **съхранение на контролни точки** за запазване на състоянието на работния поток.

Основните компоненти на работния поток са:

**Изпълнители**

Изпълнителите получават входящи съобщения, изпълняват възложените им задачи и генерират изходящо съобщение. Това придвижва работния поток напред към завършването на по-голямата задача. Изпълнителите могат да бъдат AI агент или персонализирана логика.

**Връзки**

Връзките се използват за дефиниране на потока на съобщенията в работния поток. Те могат да бъдат:

*Преки връзки* - Прости едно-към-едно връзки между изпълнители:

```python
from agent_framework import WorkflowBuilder

builder = WorkflowBuilder()
builder.add_edge(source_executor, target_executor)
builder.set_start_executor(source_executor)
workflow = builder.build()
```

*Условни връзки* - Активират се след като е изпълнено определено условие. Например, когато хотелските стаи са изчерпани, изпълнителят може да предложи други опции.

*Връзки с превключвател (Switch-case)* - Насочват съобщения към различни изпълнители въз основа на дефинирани условия. Например, ако клиентът на пътуване има приоритетен достъп, задачите му ще се обработват чрез друг работен поток.

*Множество изходящи връзки (Fan-out)* - Изпраща едно съобщение към множество получатели.

*Събиране на множество входящи връзки (Fan-in)* - Събира множество съобщения от различни изпълнители и ги изпраща към един получател.

**Събития**

За да осигури по-добра наблюдаемост на работните потоци, MAF предлага вградени събития за изпълнение, включително:

- `WorkflowStartedEvent`  - Започва изпълнения на работния поток
- `WorkflowOutputEvent` - Работният поток генерира изход
- `WorkflowErrorEvent` - Възниква грешка в работния поток
- `ExecutorInvokeEvent`  - Изпълнителят започва обработка
- `ExecutorCompleteEvent`  -  Изпълнителят завършва обработка
- `RequestInfoEvent` - Стартиране на заявка

## Разширени модели на MAF

Горните раздели обхващат основните концепции на Microsoft Agent Framework. Когато изграждате по-сложни агенти, ето някои разширени модели за разглеждане:

- **Композиция на междинен софтуер (Middleware Composition)**: Свързване на множество обработващи модули (логване, удостоверяване, ограничаване на скоростта) с използване на функционален и чат middleware за прецизен контрол над поведението на агента.
- **Записване на контролни точки в работния поток (Workflow Checkpointing)**: Използване на събития в работния поток и сериализация за запазване и възобновяване на дългосрочни процеси на агенти.
- **Динамичен избор на инструменти (Dynamic Tool Selection)**: Комбиниране на RAG върху описания на инструменти с регистрацията на инструменти в MAF за представяне само на релевантни инструменти при заявка.
- **Предаване между множество агенти (Multi-Agent Handoff)**: Използване на връзките в работния поток и условното маршрутизиране за оркестрация на предавания между специализирани агенти.

## Хостване на LangChain / LangGraph агенти на Microsoft Foundry

Microsoft Agent Framework е **framework-interoperable** — не сте ограничени до агенти, написани с MAF. Ако вече имате агент, изградени с **LangChain** или **LangGraph**, можете да го стартирате като **hosted агент в Microsoft Foundry**, така че Foundry да управлява средата за изпълнение, сесиите, мащабирането, идентичността и протоколните крайни точки за вас, докато логиката на агента остава в LangGraph.

Това се прави с пакета `langchain_azure_ai.agents.hosting`, който експонира компилиран LangGraph граф по същите протоколи, които използват агенти, хоствани в Foundry.

**1. Инсталирайте хостинг разширението:**

```bash
pip install -U "langchain-azure-ai[hosting]>=1.2.4" azure-identity
```

Разширението `hosting` инсталира библиотеките на протокола Foundry: `azure-ai-agentserver-responses` (OpenAI-съвместима крайна точка `/responses`) и `azure-ai-agentserver-invocations` (общата крайна точка `/invocations`).

**2. Изберете протокол за хостване:**

| Протокол | Клас хост | Крайна точка | Използвайте когато |
|----------|-----------|----------|----------|
| **Responses** | `ResponsesHostServer` | `/responses` | Искате OpenAI-съвместим чат, стрийминг, история на отговорите и нишки на разговор — препоръчителният по подразбиране за разговорни агенти. |
| **Invocations** | `InvocationsHostServer` | `/invocations` | Имате нужда от персонализирана JSON форма, webhook-стил крайна точка или неразговорна обработка. |

Тъй като **Responses API е основният API за развитие на агент-стил в Foundry**, започнете с `ResponsesHostServer` за повечето агенти.

**3. Конфигурирайте променливите на средата** (`az login` първо, за да може `DefaultAzureCredential` да се удостоверява):

```bash
export FOUNDRY_PROJECT_ENDPOINT="https://<resource>.services.ai.azure.com/api/projects/<project>"
export FOUNDRY_MODEL_NAME="gpt-4.1"
```

Когато агентът по-късно работи като хостван агент в Foundry, платформата автоматично въвежда `FOUNDRY_PROJECT_ENDPOINT`.

**4. Експонирайте LangGraph агент по протокола Responses:**

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

    # ChatOpenAI тук се насочва към OpenAI-съвместимия (Responses) крайна точка на проекта Foundry.
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

Стартирайте го локално с `python main.py`, след което изпратете заявка Responses към `http://localhost:8088/responses`.

**Ключови поведения:**

- **Разговори**: Клиентите продължават разговора като подават `previous_response_id` или `conversation` ID. Ако вашият граф е компилиран с LangGraph чекпойнтер, Foundry свързва състоянието на разговора с контролната точка (в продукция използвайте траен чекпойнтер; `MemorySaver` е подходящ за локално тестване).
- **Человек в цикъла (Human-in-the-loop)**: Ако вашият граф използва LangGraph `interrupt()`, `ResponsesHostServer` показва чакащото прекъсване като Responses `function_call` / `mcp_approval_request` елемент, и клиентите продължават със съвпадащ `function_call_output` / `mcp_approval_response`.
- **Деплой в Foundry**: Използвайте Azure Developer CLI — `azd ext install azure.ai.agents`, `azd ai agent init -m <manifest>`, `azd ai agent run` (локално, изисква Docker), след това `azd provision` и `azd deploy`. Деплойментът на хостван агент изисква ролята **Foundry Project Manager**.

Работеща версия на този пример се намира в [code-samples/14-langchain-hosted-agent.py](../../../14-microsoft-agent-framework/code-samples/14-langchain-hosted-agent.py). За пълното ръководство (протокол Invocations, персонализирани схеми на заявки и отстраняване на проблеми) вижте [Host LangGraph agents as Foundry hosted agents](https://learn.microsoft.com/azure/foundry/how-to/develop/langchain-hosted-agents).

## Примери с код 

Примери с код за Microsoft Agent Framework могат да бъдат намерени в това репозитори под файловете `xx-python-agent-framework` и `xx-dotnet-agent-framework`.

## Имате ли още въпроси за Microsoft Agent Framework?

Присъединете се към [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D), за да срещнете други учащи се, да участвате в офис часове и да получите отговори на въпросите си за AI агенти.
## Предишен урок

[Памет за AI агенти](../13-agent-memory/README.md)

## Следващ урок

[Изграждане на агенти за ползване на компютър (CUA)](../15-browser-use/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Отказ от отговорност**:
Този документ е преведен с помощта на AI преводачески услуга [Co-op Translator](https://github.com/Azure/co-op-translator). Въпреки че се стремим към точност, моля имайте предвид, че автоматизираните преводи могат да съдържат грешки или неточности. Оригиналният документ на неговия роден език трябва да се счита за авторитетен източник. За критична информация се препоръчва професионален човешки превод. Ние не носим отговорност за каквито и да е недоразумения или неправилни тълкувания, произтичащи от използването на този превод.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->