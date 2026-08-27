# Изследване на Microsoft Agent Framework

![Agent Framework](../../../translated_images/bg/lesson-14-thumbnail.90df0065b9d234ee.webp)

### Въведение

Този урок ще обхване:

- Разбиране на Microsoft Agent Framework: Основни характеристики и стойност  
- Изследване на ключовите концепции на Microsoft Agent Framework
- Разширени MAF модели: Работни потоци, междинен софтуер и памет

## Цели за учене

След завършване на този урок ще знаете как да:

- Създавате AI агенти, готови за продукция, използвайки Microsoft Agent Framework
- Прилагате основните характеристики на Microsoft Agent Framework към вашите агентни случаи на употреба
- Използвате усъвършенствани модели, включително работни потоци, междинен софтуер и наблюдаемост

## Примери с код 

Примери с код за [Microsoft Agent Framework (MAF)](https://learn.microsoft.com/en-us/agent-framework/overview/?wt.mc_id=youtube_26688_organicsocial_reactor&pivots=programming-language-python) могат да бъдат намерени в това хранилище под файловете `xx-python-agent-framework` и `xx-dotnet-agent-framework`.

## Разбиране на Microsoft Agent Framework

![Framework Intro](../../../translated_images/bg/framework-intro.077af16617cf130c.webp)

[Microsoft Agent Framework (MAF)](https://learn.microsoft.com/en-us/agent-framework/overview/?wt.mc_id=youtube_26688_organicsocial_reactor&pivots=programming-language-python) е унифицираната рамка на Microsoft за изграждане на AI агенти. Тя предлага гъвкавост да се адресират широк спектър от агентни случаи на употреба, наблюдавани както в производствени, така и в изследователски среди, включително:

- **Последователно оркестриране на агенти** в сценарии, където са нужни работни потоци стъпка по стъпка.
- **Паралелно оркестриране** в сценарии, където агентите трябва да изпълнят задачи едновременно.
- **Оркестриране в групов чат** в сценарии, където агентите могат да си сътрудничат по една задача.
- **Прехвърляне на задачи** в сценарии, където агентите предават задачата един на друг, докато подзадачите се изпълняват.
- **Магнитно оркестриране** в сценарии, където мениджър агент създава и променя списък със задачи и координира подагенти за изпълнение на задачата.

За да предостави AI агенти в продукция, MAF също включва характеристики за:

- **Наблюдаемост** чрез използването на OpenTelemetry, където всяко действие на AI агента, включително извикване на инструменти, стъпки на оркестрация, потоци на разсъждение и мониторинг на производителността чрез таблата на Microsoft Foundry.
- **Сигурност** чрез хостване на агентите нативно в Microsoft Foundry, което включва контрол на достъпа въз основа на роли, обработка на лични данни и вградена безопасност на съдържанието.
- **Издръжливост** тъй като нишките и работните потоци на агента могат да бъдат паузирани, възобновявани и възстановявани при грешки, което позволява по-дълги процеси.
- **Контрол** тъй като се поддържат работни потоци с човешко участие, където задачите са маркирани като изискващи човешко одобрение.

Microsoft Agent Framework също е фокусиран върху интероперативността чрез:

- **Облачно-агностичен** - Агентите могат да работят в контейнери, локално и в различни облаци.
- **Доставчик-агностичен** - Агентите могат да се създават чрез предпочитания от вас SDK, включително Azure OpenAI и OpenAI
- **Интеграция на отворени стандарти** - Агентите могат да използват протоколи като Agent-to-Agent (A2A) и Model Context Protocol (MCP) за откриване и използване на други агенти и инструменти.
- **Плъгини и конектори** - Възможни са връзки към услуги за данни и памет като Microsoft Fabric, SharePoint, Pinecone и Qdrant.

Нека видим как тези характеристики се прилагат към някои от основните концепции на Microsoft Agent Framework.

## Ключови концепции на Microsoft Agent Framework

### Агенти

![Agent Framework](../../../translated_images/bg/agent-components.410a06daf87b4fef.webp)

**Създаване на агенти**

Създаването на агент става чрез дефиниране на услугата за извод (доставчик на LLM), 
набор от инструкции, които AI агентът трябва да следва, и зададено `име`:

```python
agent = AzureOpenAIChatClient(credential=AzureCliCredential()).create_agent( instructions="You are good at recommending trips to customers based on their preferences.", name="TripRecommender" )
```

Горното използва `Azure OpenAI`, но агенти могат да се създават чрез различни услуги, включително `Microsoft Foundry Agent Service`:

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

или [MiniMax](https://platform.minimaxi.com/), който предоставя OpenAI-съвместим API с големи контекстови прозорци (до 204К токена):

```python
agent = OpenAIChatClient(base_url="https://api.minimax.io/v1", api_key=os.environ["MINIMAX_API_KEY"], model_id="MiniMax-M3").create_agent( name="HelpfulAssistant", instructions="You are a helpful assistant.", )
```

или дистанционни агенти с помощта на A2A протокол:

```python
agent = A2AAgent( name=agent_card.name, description=agent_card.description, agent_card=agent_card, url="https://your-a2a-agent-host" )
```

**Изпълнение на агенти**

Агентите се изпълняват чрез методите `.run` или `.run_stream` за отговори без поток или с поток.

```python
result = await agent.run("What are good places to visit in Amsterdam?")
print(result.text)
```

```python
async for update in agent.run_stream("What are the good places to visit in Amsterdam?"):
    if update.text:
        print(update.text, end="", flush=True)

```

Всяко изпълнение на агент може да има и опции за персонализиране на параметри като `max_tokens`, използвани от агента, `tools`, които агентът може да извиква, и дори самия `model`, използван за агента.

Това е полезно при случаи, когато за изпълнението на задачата на потребителя са изисквани специфични модели или инструменти.

**Инструменти**

Инструментите могат да се дефинират както при създаване на агента:

```python
def get_attractions( location: Annotated[str, Field(description="The location to get the top tourist attractions for")], ) -> str: """Get the top tourist attractions for a given location.""" return f"The top attractions for {location} are." 


# При създаване на ChatAgent директно

agent = ChatAgent( chat_client=OpenAIChatClient(), instructions="You are a helpful assistant", tools=[get_attractions]

```

и също така при изпълнение на агента:

```python

result1 = await agent.run( "What's the best place to visit in Seattle?", tools=[get_attractions] # Инструмент, предоставен само за това изпълнение )
```

**Нишки на агенти**

Нишките на агенти се използват за управление на многоходови разговори. Нишки могат да се създават чрез:

- Използване на `get_new_thread()`, което позволява нишката да бъде запазена за по-късна употреба
- Автоматично създаване на нишка при изпълнение на агент, която трае само по време на текущото изпълнение.

За да се създаде нишка, кодът изглежда така:

```python
# Създайте нова нишка.
thread = agent.get_new_thread() # Стартирайте агента с нишката.
response = await agent.run("Hello, I am here to help you book travel. Where would you like to go?", thread=thread)

```

След това нишката може да бъде сериализирана и съхранявана за по-късна употреба:

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

**Междинен софтуер за агенти**

Агентите взаимодействат с инструменти и LLM, за да изпълнят задачите на потребителя. В определени сценарии искаме да изпълним или проследим действия между тези взаимодействия. Междинният софтуер на агентите ни позволява да го направим чрез:

*Функционален междинен софтуер*

Този междинен софтуер ни позволява да изпълним действие между агента и функция/инструмент, който той ще извика. Пример за използването му е, когато искате да направите запис при извикване на функция.

В кода по-долу `next` определя дали да бъде извикан следващия междинен софтуер или действителната функция.

```python
async def logging_function_middleware(
    context: FunctionInvocationContext,
    next: Callable[[FunctionInvocationContext], Awaitable[None]],
) -> None:
    """Function middleware that logs function execution."""
    # Предварителна обработка: Запис преди изпълнението на функцията
    print(f"[Function] Calling {context.function.name}")

    # Продължи към следващия междинен софтуер или изпълнение на функция
    await next(context)

    # Последваща обработка: Запис след изпълнението на функцията
    print(f"[Function] {context.function.name} completed")
```

*Чат междинен софтуер*

Този междинен софтуер ни позволява да изпълняваме или записваме действие между агента и заявките към LLM.

Той съдържа важна информация като `messages`, които се изпращат към AI услугата.

```python
async def logging_chat_middleware(
    context: ChatContext,
    next: Callable[[ChatContext], Awaitable[None]],
) -> None:
    """Chat middleware that logs AI interactions."""
    # Предварителна обработка: Запис преди извикване на AI
    print(f"[Chat] Sending {len(context.messages)} messages to AI")

    # Продължаване към следващия посредник или AI услуга
    await next(context)

    # Последваща обработка: Запис след отговор от AI
    print("[Chat] AI response received")

```

**Памет на агента**

Както беше разгледано в урока `Agentic Memory`, паметта е важен елемент, който позволява на агента да оперира върху различни контексти. MAF предлага няколко различни вида памет:

*Памет в рамките на приложението (In-Memory Storage)*

Това е паметта, съхранявана в нишките по време на изпълнение на приложението.

```python
# Създайте нов нишка.
thread = agent.get_new_thread() # Стартирайте агента с нишката.
response = await agent.run("Hello, I am here to help you book travel. Where would you like to go?", thread=thread)
```

*Постоянни съобщения (Persistent Messages)*

Тази памет се използва при съхраняване на историята на разговори през различни сесии. Тя се дефинира чрез `chat_message_store_factory`:

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

*Динамична памет (Dynamic Memory)*


Тази памет се добавя към контекста преди да се стартират агентите. Тези спомени могат да се съхраняват в външни услуги като mem0:

```python
from agent_framework.mem0 import Mem0Provider

# Използване на Mem0 за усъвършенствани възможности за памет
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

Наблюдаемостта е важна за изграждането на надеждни и поддържими агентни системи. MAF се интегрира с OpenTelemetry, за да осигури проследяване и измервателни уреди за по-добра наблюдаемост.

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

MAF предлага работни потоци, които са предварително дефинирани стъпки за завършване на задача и включват AI агенти като компоненти в тези стъпки.

Работните потоци се състоят от различни компоненти, които позволяват по-добър контрол на потока. Работните потоци също така позволяват **оркестрация с множество агенти** и **чекпойнтинг** за запазване на състоянията на работните потоци.

Основните компоненти на работния поток са:

**Изпълнители**

Изпълнителите получават входни съобщения, изпълняват възложените задачи и след това произвеждат изходно съобщение. Това движи работния поток напред към завършване на по-голямата задача. Изпълнителите могат да бъдат AI агент или персонализирана логика.

**Ръбове**

Ръбовете се използват за дефиниране на потока на съобщенията в работен поток. Те могат да бъдат:

*Пряк Ръб* - Прости връзки една към една между изпълнителите:

```python
from agent_framework import WorkflowBuilder

builder = WorkflowBuilder()
builder.add_edge(source_executor, target_executor)
builder.set_start_executor(source_executor)
workflow = builder.build()
```

*Условни Ръбове* - Активират се след изпълнение на определено условие. Например, когато хотелските стаи са изчерпани, изпълнителят може да предложи други опции.

*Switch-case Ръбове* - Насочват съобщенията към различни изпълнители въз основа на дефинирани условия. Например, ако пътникът има приоритетен достъп, неговите задачи ще се обработват чрез друг работен поток.

*Fan-out Ръбове* - Изпращат едно съобщение към множество получатели.

*Fan-in Ръбове* - Събират множество съобщения от различни изпълнители и ги изпращат към един получател.

**Събития**

За да осигури по-добра наблюдаемост на работните потоци, MAF предлага вградени събития за изпълнение, включително:

- `WorkflowStartedEvent`  - Започва изпълнението на работния поток
- `WorkflowOutputEvent` - Работният поток генерира изход
- `WorkflowErrorEvent` - Работният поток среща грешка
- `ExecutorInvokeEvent`  - Изпълнителят започва обработка
- `ExecutorCompleteEvent`  -  Изпълнителят завършва обработка
- `RequestInfoEvent` - Извършва се заявка

## Разширени модели на MAF

Горните раздели покриват основните концепции на Microsoft Agent Framework. Когато изграждате по-сложни агенти, ето някои разширени модели, които да вземете предвид:

- **Съставяне на междинен слой**: Свържете множество обработващи функции на междинен слой (логване, удостоверяване, ограничаване на честотата) чрез функционална и чат междинна обработка за фино управление на поведението на агента.
- **Чекпойнтинг на работен поток**: Използвайте събитията на работния поток и сериализацията за запазване и възобновяване на дълго изпълняващи се агентни процеси.
- **Динамичен избор на инструменти**: Комбинирайте RAG върху описания на инструменти с регистрацията на инструменти в MAF, за да представите само релевантни инструменти за всяка заявка.
- **Прехвърляне между агенти**: Използвайте ръбовете на работния поток и условното маршрутизиране за оркестриране на прехвърляния между специализирани агенти.

## Хостинг на LangChain / LangGraph Агенти в Microsoft Foundry

Microsoft Agent Framework е **съвместим с други рамки** — не сте ограничени до агенти, написани с MAF. Ако вече имате агент, изграден с **LangChain** или **LangGraph**, можете да го стартирате като **хостван агент в Microsoft Foundry**, така че Foundry да управлява времето за изпълнение, сесиите, мащабирането, идентичността и протоколните крайни точки, докато логиката на вашия агент остава в LangGraph.

Това се постига с пакета `langchain_azure_ai.agents.hosting`, който предоставя компилиран LangGraph граф през същите протоколи, които използват хостваните агенти на Foundry.

**1. Инсталирайте хостинг допълнението:**

```bash
pip install -U "langchain-azure-ai[hosting]>=1.2.4" azure-identity
```

Допълнението `hosting` инсталира протоколните библиотеки на Foundry: `azure-ai-agentserver-responses` (OpenAI-съвместима крайна точка `/responses`) и `azure-ai-agentserver-invocations` (общата крайна точка `/invocations`).

**2. Изберете протокол за хостинг:**

| Протокол | Клас хост | Крайна точка | Използва се при |
|----------|------------|-------------|-----------------|
| **Responses** | `ResponsesHostServer` | `/responses` | Искате OpenAI-съвместим чат, стрийминг, история на отговорите и нишките на разговори — препоръчителна по подразбиране за разговорни агенти. |
| **Invocations** | `InvocationsHostServer` | `/invocations` | Имaте нужда от персонализирана JSON форма, webhook стил крайна точка или обработка, която не е разговорна. |

Тъй като **Responses API е основният API за разработка на агенти в Foundry**, започнете с `ResponsesHostServer` за повечето агенти.

**3. Конфигурирайте променливите на средата** (първо изпълнете `az login`, за да може `DefaultAzureCredential` да се автентикира):

```bash
export FOUNDRY_PROJECT_ENDPOINT="https://<resource>.services.ai.azure.com/api/projects/<project>"
export FOUNDRY_MODEL_NAME="gpt-5-mini"
```

Когато агентът по-късно се изпълнява като хостван агент в Foundry, платформата автоматично инжектира `FOUNDRY_PROJECT_ENDPOINT`.

**4. Изложете LangGraph агент през Responses протокола:**

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

    # ChatOpenAI тук насочва към OpenAI-съвместимия (Responses) крайна точка на проекта Foundry.
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

Стартирайте го локално с `python main.py`, след това изпратете заявка към Responses на `http://localhost:8088/responses`.

**Ключови поведения:**

- **Разговори**: Клиентите продължават разговор, като предават `previous_response_id` или `conversation` ID. Ако вашият граф е компилиран с LangGraph чекпойнтър, Foundry асоциира състоянието на разговора с чекпойнта (за продукция използвайте траен чекпойнтър; `MemorySaver` е подходящ за локално тестване).
- **Човек в цикъла**: Ако вашият граф използва LangGraph `interrupt()`, `ResponsesHostServer` показва чакащия прекъсвач като Responses `function_call` / `mcp_approval_request` елемент, а клиентите продължават с подходящия `function_call_output` / `mcp_approval_response`.
- **Разгръщане в Foundry**: Използвайте Azure Developer CLI — `azd ext install azure.ai.agents`, `azd ai agent init -m <manifest>`, `azd ai agent run` (локално, изисква Docker), след това `azd provision` и `azd deploy`. Разгръщането на хостван агент изисква ролята **Foundry Project Manager**.

Изпълнима версия на този пример се намира в [code-samples/14-langchain-hosted-agent.py](../../../14-microsoft-agent-framework/code-samples/14-langchain-hosted-agent.py). За пълния урок (протокол Invocations, персонализирани схеми на заявки и отстраняване на проблеми), вижте [Host LangGraph agents as Foundry hosted agents](https://learn.microsoft.com/azure/foundry/how-to/develop/langchain-hosted-agents).

## Примери с код 

Примери с код за Microsoft Agent Framework можете да намерите в това хранилище под файловете `xx-python-agent-framework` и `xx-dotnet-agent-framework`.

## Имате още въпроси за Microsoft Agent Framework?

Присъединете се към [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D), за да се срещнете с други учащи, да присъствате на часове за въпроси и да получите отговори на вашите въпроси за AI агенти.
## Предишен урок

[Памет за AI агенти](../13-agent-memory/README.md)

## Следващ урок


[Създаване на агенти за използване на компютър (CUA)](../15-browser-use/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Отказ от отговорност**:
Този документ е преведен с помощта на AI преводачески услуга [Co-op Translator](https://github.com/Azure/co-op-translator). Въпреки че се стремим към точност, моля имайте предвид, че автоматизираните преводи могат да съдържат грешки или неточности. Оригиналният документ на неговия роден език трябва да се счита за авторитетен източник. За критична информация се препоръчва професионален човешки превод. Ние не носим отговорност за каквито и да е недоразумения или неправилни тълкувания, произтичащи от използването на този превод.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->