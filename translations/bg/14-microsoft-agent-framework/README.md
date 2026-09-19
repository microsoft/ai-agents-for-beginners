# Изследване на Microsoft Agent Framework

![Agent Framework](../../../translated_images/bg/lesson-14-thumbnail.90df0065b9d234ee.webp)

### Въведение

Този урок ще обхване:

- Разбиране на Microsoft Agent Framework: Ключови функции и стойност  
- Изследване на ключовите концепции на Microsoft Agent Framework
- Разширени MAF модели: Работни процеси, междинен слой и памет

## Обучителни цели

След завършване на този урок ще знаете как да:

- Създавате AI агенти готови за продукция с помощта на Microsoft Agent Framework
- Прилагате основните функции на Microsoft Agent Framework към вашите агентни употребни случаи
- Използвате разширени модели, включително работни процеси, междинен слой и наблюдаемост

## Примери с код 

Примери с код за [Microsoft Agent Framework (MAF)](https://learn.microsoft.com/en-us/agent-framework/overview/?wt.mc_id=youtube_26688_organicsocial_reactor&pivots=programming-language-python) могат да бъдат намерени в това хранилище под файловете `xx-python-agent-framework` и `xx-dotnet-agent-framework`.

## Разбиране на Microsoft Agent Framework

![Framework Intro](../../../translated_images/bg/framework-intro.077af16617cf130c.webp)

[Microsoft Agent Framework (MAF)](https://learn.microsoft.com/en-us/agent-framework/overview/?wt.mc_id=youtube_26688_organicsocial_reactor&pivots=programming-language-python) е единната рамка на Microsoft за изграждане на AI агенти. Тя предлага гъвкавост за адресиране на широка гама от агентни употребни случаи, наблюдавани както в продукционни, така и в изследователски среди, включително:

- **Последователна агентна оркестрация** в ситуации, където са необходими стъпка по стъпка работни процеси.
- **Паралелна оркестрация** в ситуации, където агентите трябва да изпълнят задачи едновременно.
- **Групова чат оркестрация** в ситуации, където агентите могат да си сътрудничат по една задача.
- **Оркестрация с предаване на задачи** в ситуации, където агентите предават задачата един на друг след завършване на подзадачите.
- **Магнитна оркестрация** в ситуации, където управляващ агент създава и модифицира списък със задачи и координира подагенти за изпълнение на задачите.

За да предоставя AI агенти в продукция, MAF също така включва функции за:

- **Наблюдаемост** чрез използването на OpenTelemetry, където всяко действие на AI агента, включително извикване на инструменти, стъпки за оркестрация, потоци на разсъждения и мониторинг на производителността чрез таблата за управление на Microsoft Foundry.
- **Сигурност** чрез хостване на агентите нативно в Microsoft Foundry, което включва контрол на достъпа базиран на роли, работа с лични данни и вградена безопасност на съдържанието.
- **Издръжливост** тъй като нишките и работните процеси на агентите могат да бъдат поставяни на пауза, възобновявани и възстановявани след грешки, което позволява изпълнение на по-дълги процеси.
- **Контрол** чрез подкрепа на работни процеси с участието на човек, където задачите са маркирани като изискващи човешко одобрение.

Microsoft Agent Framework също се фокусира върху съвместимостта чрез:

- **Областна независимост** - Агентите могат да работят в контейнери, на локален сървър и в множество различни облаци.
- **Независимост от доставчик** - Агентите могат да бъдат създавани чрез предпочитаното SDK, включително Azure OpenAI и OpenAI.
- **Интеграция на отворени стандарти** - Агентите могат да използват протоколи като Agent-to-Agent (A2A) и Model Context Protocol (MCP) за откриване и използване на други агенти и инструменти.
- **Разширения и конектори** - Могат да се осъществяват връзки към услуги за данни и памет като Microsoft Fabric, SharePoint, Pinecone и Qdrant.

Нека видим как тези функции се прилагат към някои от основните концепции на Microsoft Agent Framework.

## Ключови концепции на Microsoft Agent Framework

### Агенти

![Agent Framework](../../../translated_images/bg/agent-components.410a06daf87b4fef.webp)

**Създаване на агенти**

Създаването на агент се извършва чрез дефиниране на услуга за извеждане (LLM доставчик), 
набор от инструкции, които AI агентът трябва да следва, и зададено `име`:

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

или [MiniMax](https://platform.minimaxi.com/), който предоставя OpenAI-съвместим API с големи контекстови прозорци (до 204K токена):

```python
agent = OpenAIChatClient(base_url="https://api.minimax.io/v1", api_key=os.environ["MINIMAX_API_KEY"], model_id="MiniMax-M3").create_agent( name="HelpfulAssistant", instructions="You are a helpful assistant.", )
```

или отдалечени агенти, използващи A2A протокола:

```python
agent = A2AAgent( name=agent_card.name, description=agent_card.description, agent_card=agent_card, url="https://your-a2a-agent-host" )
```

**Стартиране на агенти**

Агентите се стартират чрез методите `.run` или `.run_stream` за отговори без поток или с поток.

```python
result = await agent.run("What are good places to visit in Amsterdam?")
print(result.text)
```

```python
async for update in agent.run_stream("What are the good places to visit in Amsterdam?"):
    if update.text:
        print(update.text, end="", flush=True)

```

Всеки старт на агент може да включва опции за персонализиране на параметри като `max_tokens` използвани от агента, `tools` които агентът може да използва, и дори самия `model`, използван за агента.

Това е полезно в случаи, когато са необходими специфични модели или инструменти за изпълнение на задачата на потребителя.

**Инструменти**

Инструменти могат да бъдат дефинирани както при създаване на агента:

```python
def get_attractions( location: Annotated[str, Field(description="The location to get the top tourist attractions for")], ) -> str: """Get the top tourist attractions for a given location.""" return f"The top attractions for {location} are." 


# Когато създавате ChatAgent директно

agent = ChatAgent( chat_client=OpenAIChatClient(), instructions="You are a helpful assistant", tools=[get_attractions]

```

и също така при стартиране на агента:

```python

result1 = await agent.run( "What's the best place to visit in Seattle?", tools=[get_attractions] # Инструмент, предоставен само за този път )
```

**Нишки на агента**

Нишките на агента се използват за управление на разговори с множество ходове. Нишки могат да бъдат създадени или чрез:

- Използване на `get_new_thread()`, което позволява нишката да се запазва с времето
- Автоматично създаване на нишка при стартиране на агент и нишката да съществува само за текущия цикъл на изпълнение.

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

# Сериализирайте нишката за съхранение.

serialized_thread = await thread.serialize() 

# Десериализирайте състоянието на нишката след зареждане от съхранението.

resumed_thread = await agent.deserialize_thread(serialized_thread)
```

**Междинен слой на агента**

Агентите взаимодействат с инструменти и LLM, за да изпълнят задачите на потребителя. В определени ситуации искаме да изпълним или следим действия между тези взаимодействия. Междинният слой на агента ни позволява да направим това чрез:

*Функционален междинен слой*

Този междинен слой позволява да се изпълни действие между агента и функция/инструмент, към които агентът ще се обръща. Пример за използване е водене на лог за извикванията на функцията.

В кода по-долу `next` определя дали да се извика следващият междинен слой или самата функция.

```python
async def logging_function_middleware(
    context: FunctionInvocationContext,
    next: Callable[[FunctionInvocationContext], Awaitable[None]],
) -> None:
    """Function middleware that logs function execution."""
    # Предварителна обработка: Запис в лог преди изпълнение на функцията
    print(f"[Function] Calling {context.function.name}")

    # Продължи към следващия междинен слой или изпълнение на функцията
    await next(context)

    # Последваща обработка: Запис в лог след изпълнение на функцията
    print(f"[Function] {context.function.name} completed")
```

*Чат междинен слой*

Този междинен слой позволява да се изпълни или регистрира действие между агента и заявките към LLM.

Съдържа важна информация като `messages`, които се изпращат към AI услугата.

```python
async def logging_chat_middleware(
    context: ChatContext,
    next: Callable[[ChatContext], Awaitable[None]],
) -> None:
    """Chat middleware that logs AI interactions."""
    # Предварителна обработка: Запис преди извикване на AI
    print(f"[Chat] Sending {len(context.messages)} messages to AI")

    # Продължи към следващия middleware или AI услуга
    await next(context)

    # Следобработка: Запис след отговор от AI
    print("[Chat] AI response received")

```

**Памет на агента**

Както е разгледано в урока `Agentic Memory`, паметта е важен елемент за позволяващ агентът да оперира в различни контексти. MAF предлага няколко различни вида памет:

*Памет в паметта (In-Memory Storage)*

Това е паметта, запазена в нишките по време на изпълнението на приложението.

```python
# Създайте нов нишка.
thread = agent.get_new_thread() # Стартирайте агента с нишката.
response = await agent.run("Hello, I am here to help you book travel. Where would you like to go?", thread=thread)
```

*Постоянни съобщения (Persistent Messages)*

Тази памет се използва за съхраняване на историята на разговорите през различни сесии. Дефинира се чрез `chat_message_store_factory`:

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

Тази памет се добавя към контекста преди стартирането на агенти. Тя може да се съхранява в външни услуги като mem0:

```python
from agent_framework.mem0 import Mem0Provider

# Използване на Mem0 за разширени възможности на паметта
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

Наблюдаемостта е важна за изграждане на надеждни и поддържими агентни системи. MAF интегрира OpenTelemetry за предоставяне на проследяване и измервателни уреди за по-добра наблюдаемост.

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

MAF предлага работни процеси, които са предварително дефинирани стъпки за изпълнение на задача и включват AI агенти като компоненти в тези стъпки.

Работните процеси са съставени от различни компоненти, които позволяват по-добър контрол на потока. Те също така позволяват **оркестрация с множество агенти** и **съхранение на контролни точки** за запазване на състоянието на работния процес.

Основните компоненти на работен процес са:

**Изпълнители**

Изпълнителите получават входящи съобщения, изпълняват възложените им задачи и произвеждат изходящо съобщение. Това придвижва работния процес напред към завършването на по-голямата задача. Изпълнителите могат да бъдат AI агент или персонализирана логика.

**Връзки (Edges)**

Връзките се използват за дефиниране на потока на съобщения в работен процес. Те могат да бъдат:

*Директни връзки* - Прости един към един връзки между изпълнителите:

```python
from agent_framework import WorkflowBuilder

builder = WorkflowBuilder()
builder.add_edge(source_executor, target_executor)
builder.set_start_executor(source_executor)
workflow = builder.build()
```

*Условни връзки* - Активират се след изпълнение на определено условие. Например, когато хотелските стаи са недостъпни, изпълнителят може да предложи други опции.

*Разклонени връзки (Switch-case Edges)* - Насочват съобщения към различни изпълнители въз основа на дефинирани условия. Например, ако клиент за пътуване има приоритетен достъп, задачите му ще се обработват чрез друг работен процес.

*Fan-out връзки* - Изпращат едно съобщение към няколко получатели.

*Fan-in връзки* - Събират множество съобщения от различни изпълнители и ги изпращат към един получател.

**Събития**

За по-добра наблюдаемост на работните процеси, MAF предлага вградени събития по време на изпълнението, включително:

- `WorkflowStartedEvent`  - Започва изпълнението на работния процес
- `WorkflowOutputEvent` - Работният процес произвежда изход
- `WorkflowErrorEvent` - Възниква грешка в работния процес
- `ExecutorInvokeEvent`  - Изпълнителят започва обработка
- `ExecutorCompleteEvent`  -  Изпълнителят приключва обработката
- `RequestInfoEvent` - Заявка е направена

## Разширени MAF модели

По-горе се покриват ключовите концепции на Microsoft Agent Framework. При изграждане на по-сложни агенти, имайте предвид някои разширени модели:

- **Композиция на междинен слой**: Свързвайте множество междинни обработващи звена (логване, автентикация, ограничаване на честота) чрез функционален и чат междинен слой за прецизен контрол върху поведението на агента.
- **Съхранение на контролни точки в работни процеси**: Използвайте събития в работния процес и сериализация за запазване и възобновяване на дълги процеси на агента.
- **Динамичен избор на инструменти**: Комбинирайте RAG върху описания на инструменти с регистрацията на инструменти на MAF, за да представяте само релевантните инструменти за всяка заявка.
- **Предаване между множество агенти**: Използвайте връзки в работния процес и условно насочване за оркестрация на предаване между специализирани агенти.

## Хостване на LangChain / LangGraph агенти в Microsoft Foundry

Microsoft Agent Framework е **съвместим с други рамки** — не сте ограничени само до агенти, написани с MAF. Ако вече имате агент, изграден с **LangChain** или **LangGraph**, можете да го стартирате като **хостван агент в Microsoft Foundry**, така че Foundry да управлява изпълнението, сесиите, мащабирането, идентичността и интерфейсните крайни точки, докато логиката на вашия агент остава в LangGraph.

Това се извършва с пакета `langchain_azure_ai.agents.hosting`, който излага компилиран LangGraph граф върху същите протоколи, които използват хостваните агенти на Foundry.

**1. Инсталирайте хостинг допълнението:**

```bash
pip install -U "langchain-azure-ai[hosting]>=1.2.4" azure-identity
```

Допълнението `hosting` инсталира библиотеките на протокола Foundry: `azure-ai-agentserver-responses` (OpenAI-съвместимия `/responses` интерфейс) и `azure-ai-agentserver-invocations` (общия `/invocations` интерфейс).

**2. Изберете хостинг протокол:**

| Протокол | Клас на хоста | Крайна точка | Използвайте когато |
|----------|-----------|----------|----------|
| **Responses** | `ResponsesHostServer` | `/responses` | Искате OpenAI-съвместим чат, стрийминг, история на отговорите и нишки на разговор — препоръчаният по подразбиране за разговорни агенти. |
| **Invocations** | `InvocationsHostServer` | `/invocations` | Трябва ви персонализиран JSON формат, уебхук стил крайна точка или неразговорна обработка. |

Тъй като **Responses API е основният API за разработка на агенти в Foundry**, започнете с `ResponsesHostServer` за повечето агенти.

**3. Конфигурирайте променливи на околната среда** (`az login` първо, за да може `DefaultAzureCredential` да се автентикира):

```bash
export FOUNDRY_PROJECT_ENDPOINT="https://<resource>.services.ai.azure.com/api/projects/<project>"
export FOUNDRY_MODEL_NAME="gpt-5-mini"
```

Когато агентът по-късно се стартира като хостван агент в Foundry, платформата автоматично инжектира `FOUNDRY_PROJECT_ENDPOINT`.

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

Стартирайте локално с `python main.py`, след което изпратете заявка Responses към `http://localhost:8088/responses`.

**Ключови поведения:**

- **Разговори**: Клиентите продължават разговор, като подават `previous_response_id` или `conversation` ID. Ако вашият граф е компилиран с LangGraph чекпойнтер, Foundry свързва състоянието на разговора с контролната точка (използвайте издръжлив чекпойнтер в продукция; `MemorySaver` е подходящ за локални тестове).
- **Човек в цикъла**: Ако вашият граф използва LangGraph `interrupt()`, `ResponsesHostServer` показва чакащото прекъсване като Responses `function_call` / `mcp_approval_request` елемент, и клиентите продължават с подходящ `function_call_output` / `mcp_approval_response`.
- **Деплой в Foundry**: Използвайте Azure Developer CLI — `azd ext install azure.ai.agents`, `azd ai agent init -m <manifest>`, `azd ai agent run` (локално, изисква Docker), след това `azd provision` и `azd deploy`. Деплоймънтът на хоствани агенти изисква роля **Foundry Project Manager**.

Работеща версия на този пример може да бъде намерена в [code-samples/14-langchain-hosted-agent.py](../../../14-microsoft-agent-framework/code-samples/14-langchain-hosted-agent.py). За пълния урок (протокол Invocations, персонализирани схеми на заявки и отстраняване на проблеми), вижте [Host LangGraph agents as Foundry hosted agents](https://learn.microsoft.com/azure/foundry/how-to/develop/langchain-hosted-agents).

## Примери с код 

Примери с код за Microsoft Agent Framework могат да бъдат намерени в това хранилище под файловете `xx-python-agent-framework` и `xx-dotnet-agent-framework`.

## Искате ли още въпроси за Microsoft Agent Framework?

Присъединете се към [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D), за да се срещнете с други обучаващи се, да участвате в консултации и да получите отговори на въпросите си за AI агенти.
## Предишен урок

[Памет за AI агенти](../13-agent-memory/README.md)

## Следващ урок

[Изграждане на агенти за използване на компютър (CUA)](../15-browser-use/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Отказ от отговорност**:
Този документ е преведен с помощта на AI преводачески услуга [Co-op Translator](https://github.com/Azure/co-op-translator). Въпреки че се стремим към точност, моля имайте предвид, че автоматизираните преводи могат да съдържат грешки или неточности. Оригиналният документ на неговия роден език трябва да се счита за авторитетен източник. За критична информация се препоръчва професионален човешки превод. Ние не носим отговорност за каквито и да е недоразумения или неправилни тълкувания, произтичащи от използването на този превод.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->