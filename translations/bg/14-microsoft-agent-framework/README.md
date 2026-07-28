# Изследване на Microsoft Agent Framework

![Agent Framework](../../../translated_images/bg/lesson-14-thumbnail.90df0065b9d234ee.webp)

### Въведение

Този урок ще обхване:

- Разбиране на Microsoft Agent Framework: Основни характеристики и стойност  
- Изследване на ключовите концепции на Microsoft Agent Framework
- Разширени MAF шаблони: Работни процеси, Middleware и Памет

## Цели за учене

След завършване на този урок, ще знаете как да:

- Създавате продукционно готови AI агенти, използвайки Microsoft Agent Framework
- Прилагате основните функции на Microsoft Agent Framework към вашите агентски случаи на употреба
- Използвате разширени шаблони, включително работни процеси, middleware и наблюдаемост

## Примери с код

Примери с код за [Microsoft Agent Framework (MAF)](https://aka.ms/ai-agents-beginners/agent-framework) могат да бъдат намерени в това репозиториум под файловете `xx-python-agent-framework` и `xx-dotnet-agent-framework`.

## Разбиране на Microsoft Agent Framework

![Framework Intro](../../../translated_images/bg/framework-intro.077af16617cf130c.webp)

[Microsoft Agent Framework (MAF)](https://aka.ms/ai-agents-beginners/agent-framework) е единната рамка на Microsoft за изграждане на AI агенти. Тя предлага гъвкавост да се адресират широката гама от агентски случаи на употреба, наблюдавани както в продукционна, така и в изследователска среда, включително:

- **Последователна агентска оркестрация** в сценарии, където са необходими стъпка по стъпка работни процеси.
- **Паралелна оркестрация** в сценарии, при които агентите трябва да изпълняват задачи едновременно.
- **Оркестрация на групов чат** в сценарии, при които агентите могат да си сътрудничат по една задача.
- **Оркестрация при предаване на задачи** в сценарии, при които агентите предават задачата един на друг при завършване на подзадачите.
- **Магнитна оркестрация** в сценарии, при които управляващ агент създава и променя списък със задачи и координира подагенти за изпълнение на задачата.

За да осигури AI агенти в продукция, MAF също включва функции за:

- **Наблюдаемост** чрез използване на OpenTelemetry, където всяко действие на AI агента, включително извикване на инструменти, стъпки на оркестрация, потоци на разсъждение и мониторинг на производителността чрез Microsoft Foundry табла за управление.
- **Сигурност** чрез хостване на агентите нативно в Microsoft Foundry, което включва контроли за сигурност като достъп базиран на роли, обработка на частни данни и вградена безопасност на съдържанието.
- **Издръжливост** тъй като нишките и работните процеси на агента могат да бъдат паузирани, възстановени и да се възстановяват от грешки, което позволява по-дълги изпълнения.
- **Контрол** тъй като се поддържат човешки работни процеси, където задачите са маркирани като изискващи човешко одобрение.

Microsoft Agent Framework е също насочен към интероперативност, като:

- **Облачна независимост** - Агенти могат да работят в контейнери, на място и в различни облачни платформи.
- **Независимост от доставчик** - Агентите могат да се създават чрез предпочитания от вас SDK, включително Azure OpenAI и OpenAI
- **Интеграция на отворени стандарти** - Агентите могат да използват протоколи като Agent-to-Agent(A2A) и Model Context Protocol (MCP) за откриване и използване на други агенти и инструменти.
- **Плъгини и свързващи компоненти** - Връзки могат да се създадат към услуги за данни и памет като Microsoft Fabric, SharePoint, Pinecone и Qdrant.

Нека разгледаме как тези функции се прилагат към някои от основните концепции на Microsoft Agent Framework.

## Ключови концепции на Microsoft Agent Framework

### Агенти

![Agent Framework](../../../translated_images/bg/agent-components.410a06daf87b4fef.webp)

**Създаване на агенти**

Създаването на агент се извършва чрез дефиниране на услугата за разсъждение (LLM доставчик), 
набор от инструкции за AI агента за изпълнение и зададено `име`:

```python
agent = AzureOpenAIChatClient(credential=AzureCliCredential()).create_agent( instructions="You are good at recommending trips to customers based on their preferences.", name="TripRecommender" )
```

По-горе се използва `Azure OpenAI`, но агентите могат да се създават чрез различни услуги, включително `Microsoft Foundry Agent Service`:

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

или [MiniMax](https://platform.minimaxi.com/), който предоставя OpenAI-съвместим API с големи контекстови прозорци (до 204K токена):

```python
agent = OpenAIChatClient(base_url="https://api.minimax.io/v1", api_key=os.environ["MINIMAX_API_KEY"], model_id="MiniMax-M3").create_agent( name="HelpfulAssistant", instructions="You are a helpful assistant.", )
```

или отдалечени агенти чрез A2A протокола:

```python
agent = A2AAgent( name=agent_card.name, description=agent_card.description, agent_card=agent_card, url="https://your-a2a-agent-host" )
```

**Изпълнение на агенти**

Агентите се изпълняват чрез методите `.run` или `.run_stream` за не-стрийминг или стрийминг отговори.

```python
result = await agent.run("What are good places to visit in Amsterdam?")
print(result.text)
```

```python
async for update in agent.run_stream("What are the good places to visit in Amsterdam?"):
    if update.text:
        print(update.text, end="", flush=True)

```

Всяко изпълнение на агент може да има опции за персонализиране на параметри като `max_tokens`, използвани от агента, `tools`, които агентът може да извиква, и дори самият `model`, използван от агента.

Това е полезно в случаи, когато са необходими специфични модели или инструменти за изпълнение на задачата на потребителя.

**Инструменти**

Инструментите могат да се дефинират както при дефиниране на агента:

```python
def get_attractions( location: Annotated[str, Field(description="The location to get the top tourist attractions for")], ) -> str: """Get the top tourist attractions for a given location.""" return f"The top attractions for {location} are." 


# При директно създаване на ChatAgent

agent = ChatAgent( chat_client=OpenAIChatClient(), instructions="You are a helpful assistant", tools=[get_attractions]

```

и също при изпълнение на агента:

```python

result1 = await agent.run( "What's the best place to visit in Seattle?", tools=[get_attractions] # Инструмент, предоставен само за тази сесия )
```

**Агентски нишки**

Агентските нишки се използват за обработка на многоходови разговори. Нишките могат да бъдат създавани чрез:

- Използване на `get_new_thread()`, което позволява нишката да се запази във времето
- Автоматично създаване на нишка при изпълнение на агент, която съществува само по време на текущото изпълнение.

За да създадете нишка, кодът изглежда така:

```python
# Създайте нов нишка.
thread = agent.get_new_thread() # Стартирайте агента с нишката.
response = await agent.run("Hello, I am here to help you book travel. Where would you like to go?", thread=thread)

```

След това можете да сериализирате нишката за съхранение за по-късна употреба:

```python
# Създайте нова нишка.
thread = agent.get_new_thread() 

# Стартирайте агента с нишката.

response = await agent.run("Hello, how are you?", thread=thread) 

# Сериалирайте нишката за съхранение.

serialized_thread = await thread.serialize() 

# Десериалирайте състоянието на нишката след зареждане от съхранение.

resumed_thread = await agent.deserialize_thread(serialized_thread)
```

**Агентски middleware**

Агентите взаимодействат с инструменти и LLM за изпълнение на потребителските задачи. В определени сценарии искаме да изпълним или проследим действия между тези взаимодействия. Агентският middleware ни позволява да правим това чрез:

*Функционален middleware*

Този middleware ни позволява да изпълним действие между агента и функция/инструмент, който той ще извика. Пример за използване е когато искаме да правим логване при извикване на функция.

В кода по-долу `next` определя дали ще бъде извикан следващият middleware или реалната функция.

```python
async def logging_function_middleware(
    context: FunctionInvocationContext,
    next: Callable[[FunctionInvocationContext], Awaitable[None]],
) -> None:
    """Function middleware that logs function execution."""
    # Предварителна обработка: Записване в лог преди изпълнението на функцията
    print(f"[Function] Calling {context.function.name}")

    # Продължете към следващия middleware или изпълнение на функцията
    await next(context)

    # Последваща обработка: Записване в лог след изпълнението на функцията
    print(f"[Function] {context.function.name} completed")
```

*Chat middleware*

Този middleware ни позволява да изпълним или логнем действие между агента и заявките между LLM.

Тук се съдържа важна информация като `messages`, които се изпращат към AI услугата.

```python
async def logging_chat_middleware(
    context: ChatContext,
    next: Callable[[ChatContext], Awaitable[None]],
) -> None:
    """Chat middleware that logs AI interactions."""
    # Предварителна обработка: Запис преди извикване на AI
    print(f"[Chat] Sending {len(context.messages)} messages to AI")

    # Продължава към следващия посредник или AI услуга
    await next(context)

    # Последваща обработка: Запис след отговор на AI
    print("[Chat] AI response received")

```

**Агентска памет**

Както е разгледано в урока `Agentic Memory`, паметта е важен елемент за позволяващ агента да оперира в различни контексти. MAF предлага няколко различни типа памет:

*Памет в оперативната памет*

Това е паметта, съхранявана в нишките по време на изпълнение на приложението.

```python
# Създайте нов нишка.
thread = agent.get_new_thread() # Стартирайте агента с нишката.
response = await agent.run("Hello, I am here to help you book travel. Where would you like to go?", thread=thread)
```

*Постоянни съобщения*

Тази памет се използва при съхранение на историята на разговора през различни сесии. Тя се дефинира чрез `chat_message_store_factory` :

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

Тази памет се добавя към контекста преди да се изпълнят агентите. Тя може да се съхранява в външни услуги като mem0:

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

**Наблюдаемост на агенти**

Наблюдаемостта е важна за изграждане на надеждни и поддържани агентски системи. MAF интегрира OpenTelemetry за предоставяне на проследяване и метри за по-добра наблюдаемост.

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

### Работни процеси

MAF предлага работни процеси - предефинирани стъпки за изпълнение на задача, включващи AI агенти като компоненти в тези стъпки.

Работните процеси се състоят от различни компоненти, които позволяват по-добър контрол на потока. Работните процеси също позволяват **многоагентска оркестрация** и **чекпойнти** за съхраняване на състоянията на работния процес.

Основните компоненти на работния процес са:

**Изпълнители**

Изпълнителите получават входни съобщения, извършват възложените задачи и след това произвеждат изходно съобщение. Това придвижва работния процес към завършване на по-голямата задача. Изпълнителите могат да бъдат AI агент или персонализирана логика.

**Свързващи ребра**

Ребрата се използват за дефиниране на потока на съобщенията в работния процес. Те могат да бъдат:

*Директни ребра* - Прости връзки един-към-един между изпълнителите:

```python
from agent_framework import WorkflowBuilder

builder = WorkflowBuilder()
builder.add_edge(source_executor, target_executor)
builder.set_start_executor(source_executor)
workflow = builder.build()
```

*Условни ребра* - Активират се след като е изпълнено определено условие. Например, когато хотелските стаи не са налични, изпълнителят може да предложи други опции.

*Ребра от тип switch-case* - Пренасочват съобщения към различни изпълнители в зависимост от дефинирани условия. Например, ако пътникът има приоритетен достъп, неговите задачи ще бъдат обработени през друг работен процес.

*Fan-out ребра* - Изпращат едно съобщение към множество цели.

*Fan-in ребра* - Събират множество съобщения от различни изпълнители и ги изпращат към една цел.

**Събития**

За по-добра наблюдаемост на работните процеси, MAF предлага вградени събития за изпълнение, включително:

- `WorkflowStartedEvent`  - Започва изпълнението на работния процес
- `WorkflowOutputEvent` - Работният процес произвежда изход
- `WorkflowErrorEvent` - Възниква грешка при работния процес
- `ExecutorInvokeEvent`  - Изпълнителят започва обработка
- `ExecutorCompleteEvent`  -  Изпълнителят завършва обработка
- `RequestInfoEvent` - Издава се заявка

## Разширени MAF шаблони

По-горните секции обхващат ключовите концепции на Microsoft Agent Framework. Докато създавате по-сложни агенти, ето някои разширени шаблони за разглеждане:

- **Съставяне на middleware**: Свързване на няколко middleware обработващи (логване, автентикация, ограничение на скорост) чрез функционален и чат middleware за фино управление на поведението на агента.
- **Чекпойнти на работни процеси**: Използване на събития в работните процеси и сериализация за запазване и възобновяване на дълготрайни процеси на агентите.
- **Динамичен избор на инструменти**: Комбиниране на RAG върху описания на инструменти с регистриране на инструменти в MAF, за да се представят само релевантни инструменти за всяка заявка.
- **Многоагентско предаване**: Използване на ребра в работния процес и условно маршрутизиране за оркестрация на предаване между специализирани агенти.

## Хостване на LangChain / LangGraph агенти в Microsoft Foundry

Microsoft Agent Framework е **framework-interoperable** - не сте ограничени до агенти, написани с MAF. Ако вече имате агент, създаден с **LangChain** или **LangGraph**, можете да го изпълнявате като **хостван агент в Microsoft Foundry**, така че Foundry да управлява изпълнението, сесиите, мащабирането, идентичността и крайни точки на протокола за вас, докато логиката на вашия агент остане в LangGraph.

Това се прави чрез пакета `langchain_azure_ai.agents.hosting`, който излага компилиран LangGraph граф по същите протоколи, които използват хостваните агенти на Foundry.

**1. Инсталирайте хостинг допълнението:**

```bash
pip install -U "langchain-azure-ai[hosting]>=1.2.4" azure-identity
```

Допълнението `hosting` инсталира протоколните библиотеки на Foundry: `azure-ai-agentserver-responses` (OpenAI-съвместимата крайна точка `/responses`) и `azure-ai-agentserver-invocations` (универсалната крайна точка `/invocations`).

**2. Изберете протокол за хостване:**

| Протокол | Клас хост | Крайна точка | Използвайте когато |
|----------|-----------|----------|----------|
| **Responses** | `ResponsesHostServer` | `/responses` | Искате OpenAI-съвместим чат, стрийминг, история на отговорите и нишкуване на разговор — препоръчителният стандарт за разговорни агенти. |
| **Invocations** | `InvocationsHostServer` | `/invocations` | Имаш нужда от персонализиран JSON формат, webhook-стил крайна точка или несъбразителна обработка. |

Тъй като **Responses API е основният API за агентско разработване в Foundry**, започнете с `ResponsesHostServer` за повечето агенти.

**3. Конфигурирайте променливи на средата** (`az login` първо, за да може `DefaultAzureCredential` да се автентикира):

```bash
export FOUNDRY_PROJECT_ENDPOINT="https://<resource>.services.ai.azure.com/api/projects/<project>"
export FOUNDRY_MODEL_NAME="gpt-5-mini"
```

Когато агентът по-късно работи като хостван агент в Foundry, платформата автоматично инжектира `FOUNDRY_PROJECT_ENDPOINT`.

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

    # ChatOpenAI тук е насочен към OpenAI-съвместимия (Responses) крайна точка на проекта Foundry.
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

Стартирайте локално с `python main.py`, след което изпратете заявка към Responses на `http://localhost:8088/responses`.

**Ключови поведения:**

- **Разговори**: Клиентите продължават разговор, като подават `previous_response_id` или `conversation` ID. Ако вашият граф е компилиран с LangGraph чекпойнтер, Foundry ключва състоянието на разговора към чекпойнта (използвайте издръжлив чекпойнтер в продукция; `MemorySaver` е подходящ за локално тестване).
- **Човек в цикъла**: Ако графът ви използва LangGraph `interrupt()`, `ResponsesHostServer` показва чакащото прекъсване като Response `function_call` / `mcp_approval_request` елемент, а клиентите продължават с съвпадащ `function_call_output` / `mcp_approval_response`.
- **Деплой в Foundry**: Използвайте Azure Developer CLI — `azd ext install azure.ai.agents`, `azd ai agent init -m <manifest>`, `azd ai agent run` (локално, изисква Docker), след това `azd provision` и `azd deploy`. Деплойментът на хостван агент изисква ролята **Foundry Project Manager**.

Работеща версия на този пример се намира в [code-samples/14-langchain-hosted-agent.py](../../../14-microsoft-agent-framework/code-samples/14-langchain-hosted-agent.py). За пълния урок (протокол Invocations, персонализирани схеми на заявки и отстраняване на грешки), вижте [Host LangGraph agents as Foundry hosted agents](https://learn.microsoft.com/azure/foundry/how-to/develop/langchain-hosted-agents).

## Примери с код

Примери с код за Microsoft Agent Framework могат да бъдат намерени в това репозиториум под файловете `xx-python-agent-framework` и `xx-dotnet-agent-framework`.

## Имате ли още въпроси за Microsoft Agent Framework?

Присъединете се към [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D), за да се срещнете с други обучаеми, да посещавате офис часове и да получите отговори на въпросите си за AI агенти.
## Предишен урок

[Памет за AI агенти](../13-agent-memory/README.md)

## Следващ урок

[Изграждане на агенти за използване на компютър (CUA)](../15-browser-use/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Отказ от отговорност**:
Този документ е преведен с помощта на AI преводачески услуга [Co-op Translator](https://github.com/Azure/co-op-translator). Въпреки че се стремим към точност, моля имайте предвид, че автоматизираните преводи могат да съдържат грешки или неточности. Оригиналният документ на неговия роден език трябва да се счита за авторитетен източник. За критична информация се препоръчва професионален човешки превод. Ние не носим отговорност за каквито и да е недоразумения или неправилни тълкувания, произтичащи от използването на този превод.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->