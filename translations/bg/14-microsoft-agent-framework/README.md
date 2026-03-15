# Изследване на Microsoft Agent Framework

![Agent Framework](../../../translated_images/bg/lesson-14-thumbnail.90df0065b9d234ee.webp)

### Въведение

Този урок ще включва:

- Разбиране на Microsoft Agent Framework: Основни характеристики и стойност  
- Изследване на ключовите концепции на Microsoft Agent Framework
- Разширени MAF модели: Работни потоци, Middleware и памет

## Цели на обучението

След завършване на този урок ще знаете как да:

- Създавате AI агенти, готови за продукция, използвайки Microsoft Agent Framework
- Прилагате основните характеристики на Microsoft Agent Framework към вашите агентни случаи на употреба
- Използвате разширени модели, включително работни потоци, middleware и наблюдаемост

## Примери с код 

Примери с код за [Microsoft Agent Framework (MAF)](https://aka.ms/ai-agents-beginners/agent-framewrok) могат да бъдат намерени в това хранилище в файловете `xx-python-agent-framework` и `xx-dotnet-agent-framework`.

## Разбиране на Microsoft Agent Framework

![Framework Intro](../../../translated_images/bg/framework-intro.077af16617cf130c.webp)

[Microsoft Agent Framework (MAF)](https://aka.ms/ai-agents-beginners/agent-framewrok) е унифицирана рамка на Microsoft за създаване на AI агенти. Тя предлага гъвкавост за адресиране на широк спектър от агентни случаи на употреба, срещани както в продукционни, така и в изследователски среди, включително:

- **Последователна оркестрация на агенти** в сценарии, където са необходими работни потоци стъпка по стъпка.
- **Паралелна оркестрация** в сценарии, в които агентите трябва да изпълнят задачи едновременно.
- **Оркестрация на групов чат** в сценарии, в които агентите могат да си сътрудничат по една задача.
- **Оркестрация на подаване** в сценарии, където агентите предават задачата един на друг след приключване на подзадачите.
- **Магнитна оркестрация** в сценарии, в които управляващ агент създава и модифицира списък със задачи и координира подагентите за изпълнение на задачата.

За да достави AI агенти в продукция, MAF също така включва функции за:

- **Наблюдаемост** чрез използването на OpenTelemetry, където всяко действие на AI агента, включително повикване на инструменти, стъпки на оркестрация, потоци на разсъждение и мониторинг на производителността чрез таблата на Microsoft Foundry.
- **Сигурност** чрез хостване на агентите нативно в Microsoft Foundry, което включва контрол на достъпа на базата на роли, обработка на лични данни и вградена безопасност на съдържанието.
- **Надеждност** тъй като нишките и работните потоци на агента могат да бъдат паузирани, възобновявани и възстановявани при грешки, което позволява дълго протичащи процеси.
- **Контрол** с поддръжка на работни потоци с човешко участие, където задачите са маркирани като изискващи човешко одобрение.

Microsoft Agent Framework също така се фокусира върху интероперативността чрез:

- **Независимост от облак** - агентите могат да работят в контейнери, на локални сървъри и в множество различни облаци.
- **Независимост от доставчик** - агентите могат да бъдат създавани чрез предпочитания от вас SDK, включително Azure OpenAI и OpenAI
- **Интегриране на отворени стандарти** - агентите могат да използват протоколи като Agent-to-Agent (A2A) и Model Context Protocol (MCP) за откриване и използване на други агенти и инструменти.
- **Плъгини и конектори** - могат да се правят връзки към услуги за данни и памет като Microsoft Fabric, SharePoint, Pinecone и Qdrant.

Нека видим как тези характеристики се прилагат към някои от основните концепции на Microsoft Agent Framework.

## Ключови понятия на Microsoft Agent Framework

### Агенти

![Agent Framework](../../../translated_images/bg/agent-components.410a06daf87b4fef.webp)

**Създаване на агенти**

Създаването на агент става чрез дефиниране на услугата за извод (LLM доставчик), набор от инструкции, които AI агентът трябва да следва, и зададено `име`:

```python
agent = AzureOpenAIChatClient(credential=AzureCliCredential()).create_agent( instructions="You are good at recommending trips to customers based on their preferences.", name="TripRecommender" )
```

Горният код използва `Azure OpenAI`, но агентите могат да се създават чрез разнообразни услуги, включително `Microsoft Foundry Agent Service`:

```python
AzureAIAgentClient(async_credential=credential).create_agent( name="HelperAgent", instructions="You are a helpful assistant." ) as agent
```

OpenAI `Responses`, `ChatCompletion` APIs

```python
agent = OpenAIResponsesClient().create_agent( name="WeatherBot", instructions="You are a helpful weather assistant.", )
```

```python
agent = OpenAIChatClient().create_agent( name="HelpfulAssistant", instructions="You are a helpful assistant.", )
```

или отдалечени агенти чрез протокола A2A:

```python
agent = A2AAgent( name=agent_card.name, description=agent_card.description, agent_card=agent_card, url="https://your-a2a-agent-host" )
```

**Работа с агенти**

Агентите се стартират чрез методите `.run` или `.run_stream` за отговори без стрийминг или със стрийминг.

```python
result = await agent.run("What are good places to visit in Amsterdam?")
print(result.text)
```

```python
async for update in agent.run_stream("What are the good places to visit in Amsterdam?"):
    if update.text:
        print(update.text, end="", flush=True)

```

Всяко стартиране на агент може да има опции за персонализиране на параметри като `max_tokens`, използвани от агента, `tools`, които агентът може да извиква, и дори самия `model`, използван за агента.

Това е полезно в случаи, когато са необходими конкретни модели или инструменти за изпълнение на задачата на потребителя.

**Инструменти**

Инструментите могат да се дефинират както при създаването на агента:

```python
def get_attractions( location: Annotated[str, Field(description="The location to get the top tourist attractions for")], ) -> str: """Get the top tourist attractions for a given location.""" return f"The top attractions for {location} are." 


# Когато създавате ChatAgent директно

agent = ChatAgent( chat_client=OpenAIChatClient(), instructions="You are a helpful assistant", tools=[get_attractions]

```

така и при стартиране на агента:

```python

result1 = await agent.run( "What's the best place to visit in Seattle?", tools=[get_attractions] # Инструмент, предоставен само за това изпълнение )
```

**Агентни нишки**

Агентните нишки се използват за обработка на разговори с множество завъртания. Нишки могат да се създават чрез:

- Използване на `get_new_thread()`, което позволява нишката да се запазва във времето
- Автоматично създаване на нишка при стартиране на агент, която съществува само по време на текущото изпълнение.

За създаване на нишка, кодът изглежда така:

```python
# Създайте нов нишка.
thread = agent.get_new_thread() # Стартирайте агента с нишката.
response = await agent.run("Hello, I am here to help you book travel. Where would you like to go?", thread=thread)

```

След това можете да сериализирате нишката за съхранение и по-късна употреба:

```python
# Създайте нов нишка.
thread = agent.get_new_thread() 

# Изпълнете агента с нишката.

response = await agent.run("Hello, how are you?", thread=thread) 

# Сериализирайте нишката за съхранение.

serialized_thread = await thread.serialize() 

# Десериализирайте състоянието на нишката след зареждане от съхранение.

resumed_thread = await agent.deserialize_thread(serialized_thread)
```

**Агент Middleware**

Агентите взаимодействат с инструменти и LLM, за да изпълняват задачите на потребителя. В определени сценарии искаме да изпълним или проследим действия между тези взаимодействия. Агент Middlewares ни позволяват това:

*Function Middleware*

Този middleware позволява да се изпълнява действие между агента и функция/инструмент, който той ще извиква. Пример за използване е, ако искате да направите логване на повикването на функцията.

В кода по-долу `next` определя дали следващият middleware или действителната функция трябва да бъдат извикани.

```python
async def logging_function_middleware(
    context: FunctionInvocationContext,
    next: Callable[[FunctionInvocationContext], Awaitable[None]],
) -> None:
    """Function middleware that logs function execution."""
    # Предварителна обработка: Запис в лог преди изпълнението на функцията
    print(f"[Function] Calling {context.function.name}")

    # Продължи към следващия междинен слой или изпълнение на функцията
    await next(context)

    # Последваща обработка: Запис в лог след изпълнението на функцията
    print(f"[Function] {context.function.name} completed")
```

*Chat Middleware*

Този middleware позволява да се изпълнява или логва действие между агента и заявките към LLM.

Тук има важна информация като `messages`, които се изпращат към AI услугата.

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

    # Последваща обработка: Запис след отговор от AI
    print("[Chat] AI response received")

```

**Агентна памет**

Както беше разгледано в урока `Agentic Memory`, паметта е важен елемент за позволяване на агента да работи в различни контексти. MAF предлага няколко различни типа памет:

*Вътрешна памет*

Това е паметта, съхранявана в нишките по време на изпълнението на приложението.

```python
# Създайте нов нишка.
thread = agent.get_new_thread() # Стартирайте агента с нишката.
response = await agent.run("Hello, I am here to help you book travel. Where would you like to go?", thread=thread)
```

*Постоянни съобщения*

Тази памет се използва за съхраняване на история на разговори през различни сесии. Тя се дефинира чрез `chat_message_store_factory`:

```python
from agent_framework import ChatMessageStore

# Създайте персонално хранилище за съобщения
def create_message_store():
    return ChatMessageStore()

agent = ChatAgent(
    chat_client=OpenAIChatClient(),
    instructions="You are a Travel assistant.",
    chat_message_store_factory=create_message_store
)

```

*Динамична памет*

Тази памет се добавя към контекста преди да се стартират агентите. Тази памет може да се съхранява в външни услуги като mem0:

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

**Агентна наблюдаемост**

Наблюдаемостта е важна за създаване на надеждни и поддържани агентни системи. MAF се интегрира с OpenTelemetry за предоставяне на трасировки и метри за по-добра наблюдаемост.

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

Работните потоци се състоят от различни компоненти, които позволяват по-добър контрол на потока. Работните потоци също така позволяват **мултиагентна оркестрация** и **checkpointing** за запазване на състоянията на работните потоци.

Основните компоненти на работен поток са:

**Изпълнители**

Изпълнителите получават входни съобщения, изпълняват възложените им задачи и след това произвеждат изходно съобщение. Това подпомага напредъка на работния поток към завършване на по-голямата задача. Изпълнителите могат да бъдат както AI агенти, така и персонализирана логика.

**Ръбове**

Ръбовете се използват за дефиниране на потока на съобщенията в работния поток. Те могат да бъдат:

*Директни ръбове* - Прост едно към едно връзки между изпълнители:

```python
from agent_framework import WorkflowBuilder

builder = WorkflowBuilder()
builder.add_edge(source_executor, target_executor)
builder.set_start_executor(source_executor)
workflow = builder.build()
```

*Условни ръбове* - Активират се след като определено условие е изпълнено. Например, при липса на свободни хотели, изпълнителят може да предложи други опции.

*Switch-case ръбове* - Изпращат съобщения към различни изпълнители въз основа на условия. Например, ако клиентът за пътуване има приоритетен достъп, задачите му ще бъдат обработени чрез друг работен поток.

*Fan-out ръбове* - Изпращат едно съобщение към множество получатели.

*Fan-in ръбове* - Събират множество съобщения от различни изпълнители и ги изпращат към един получател.

**Събития**

За по-добра наблюдаемост на работните потоци, MAF предоставя вградени събития за изпълнение, включително:

- `WorkflowStartedEvent`  - Започване на изпълнение на работния поток
- `WorkflowOutputEvent` - Работният поток произвежда изход
- `WorkflowErrorEvent` - Работният поток среща грешка
- `ExecutorInvokeEvent`  - Изпълнителят започва обработка
- `ExecutorCompleteEvent`  -  Изпълнителят приключва обработка
- `RequestInfoEvent` - Извършва се заявка

## Разширени модели на MAF

Горните раздели покриват ключовите концепции на Microsoft Agent Framework. Докато изграждате по-сложни агенти, ето някои разширени модели за разглеждане:

- **Съставяне на middleware**: Верижно свързване на множество middleware обработващи (логване, удостоверяване, ограничаване на честотата) чрез function и chat middleware за прецизен контрол на поведението на агента.
- **Checkpointing на работни потоци**: Използване на събития от работния поток и сериализация за запазване и възобновяване на дългосрочни процеси на агента.
- **Динамичен избор на инструменти**: Комбиниране на RAG върху описания на инструменти с регистрирането на инструменти в MAF, за да се представят само релевантни инструменти спрямо заявката.
- **Мултиагентно подаване**: Използване на ръбове в работни потоци и условно маршрутизиране за оркестрация на подавания между специализирани агенти.

## Примери с код 

Примери с код за Microsoft Agent Framework могат да бъдат намерени в това хранилище в файловете `xx-python-agent-framework` и `xx-dotnet-agent-framework`.

## Имате ли още въпроси за Microsoft Agent Framework?

Присъединете се към [Microsoft Foundry Discord](https://aka.ms/ai-agents/discord), за да се срещнете с други обучаващи се, да посетите офис часове и да получите отговори на въпросите си за AI агенти.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Отказ от отговорност**:
Този документ е преведен с помощта на AI преводаческа услуга [Co-op Translator](https://github.com/Azure/co-op-translator). Въпреки че се стремим към точност, моля, имайте предвид, че автоматичните преводи могат да съдържат грешки или неточности. Оригиналният документ на неговия роден език трябва да се счита за авторитетен източник. За важна информация се препоръчва професионален човешки превод. Ние не носим отговорност за каквито и да е недоразумения или неправилни тълкувания, произтичащи от използването на този превод.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->