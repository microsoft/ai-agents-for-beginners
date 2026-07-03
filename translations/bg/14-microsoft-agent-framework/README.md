# Запознаване с Microsoft Agent Framework

![Agent Framework](../../../translated_images/bg/lesson-14-thumbnail.90df0065b9d234ee.webp)

### Въведение

Този урок ще обхване:

- Разбиране на Microsoft Agent Framework: Основни характеристики и стойност  
- Изследване на ключовите концепции на Microsoft Agent Framework
- Напреднали MAF модели: Работни потоци, междинен софтуер и памет

## Цели на обучението

След завършване на този урок, ще знаете как да:

- Създавате AI агенти, готови за продукция, използвайки Microsoft Agent Framework
- Прилагате основните функции на Microsoft Agent Framework към вашите агентни случаи на употреба
- Използвате напреднали модели, включващи работни потоци, междинен софтуер и наблюдаемост

## Примери с код

Примери с код за [Microsoft Agent Framework (MAF)](https://aka.ms/ai-agents-beginners/agent-framework) могат да бъдат намерени в това хранилище под файловете `xx-python-agent-framework` и `xx-dotnet-agent-framework`.

## Разбиране на Microsoft Agent Framework

![Framework Intro](../../../translated_images/bg/framework-intro.077af16617cf130c.webp)

[Microsoft Agent Framework (MAF)](https://aka.ms/ai-agents-beginners/agent/framework) е унифицираната рамка на Microsoft за създаване на AI агенти. Тя предлага гъвкавост за адресиране на широкия спектър от агентни случаи на употреба както в производствени, така и в изследователски среди, включително:

- **Последователна оркестрация на агенти** в сценарии, където са необходими работни потоци стъпка по стъпка.
- **Паралелна оркестрация** в сценарии, в които агентите трябва да изпълняват задачи едновременно.
- **Оркестрация на групов чат** в сценарии, в които агентите могат да си сътрудничат по една задача.
- **Оркестрация на предаване на задачи** в сценарии, в които агентите предават задачата един на друг след изпълнение на подзадачите.
- **Магнитна оркестрация** в сценарии, където управляващ агент създава и променя списък със задачи и координира подпомагащите агенти за изпълнение на задачата.

За да достави AI агенти в продукция, MAF също включва функции за:

- **Наблюдаемост** чрез използване на OpenTelemetry, където всяко действие на AI агента, включително извикване на инструменти, стъпки на оркестрация, потоци на разсъждение и мониторинг на производителността чрез таблата на Microsoft Foundry.
- **Сигурност** чрез хостинг на агентите нативно в Microsoft Foundry, който включва контрол на достъпа на база роли, обработка на лични данни и вградена безопасност на съдържанието.
- **Издръжливост** тъй като нишките и работните потоци на агента могат да спират, възобновяват и възстановяват от грешки, което позволява по-дълго изпълнение на процеси.
- **Контрол** чрез поддръжка на работни потоци с човешко участие, където задачите са маркирани като изискващи човешко одобрение.

Microsoft Agent Framework също се фокусира върху съвместимостта чрез:

- **Облачна неутралност** - агентите могат да се изпълняват в контейнери, локално и в различни облачни среди.
- **Провайдър независимост** - агентите могат да бъдат създавани чрез предпочитания SDK, включително Azure OpenAI и OpenAI.
- **Интегриране на отворени стандарти** - агентите могат да използват протоколи като Agent-to-Agent(A2A) и Model Context Protocol (MCP) за откриване и използване на други агенти и инструменти.
- **Добавки и конектори** - възможна е връзка с данни и паметни услуги като Microsoft Fabric, SharePoint, Pinecone и Qdrant.

Нека разгледаме как тези характеристики се прилагат към някои от основните концепции на Microsoft Agent Framework.

## Основни концепции на Microsoft Agent Framework

### Агенти

![Agent Framework](../../../translated_images/bg/agent-components.410a06daf87b4fef.webp)

**Създаване на агенти**

Създаването на агент става чрез дефиниране на услугата за извод (доставчик на LLM), набор от инструкции, които AI агентът да следва, и зададено име `name`:

```python
agent = AzureOpenAIChatClient(credential=AzureCliCredential()).create_agent( instructions="You are good at recommending trips to customers based on their preferences.", name="TripRecommender" )
```

Горният код използва `Azure OpenAI`, но агентите могат да се създават чрез различни услуги, включително `Microsoft Foundry Agent Service`:

```python
AzureAIAgentClient(async_credential=credential).create_agent( name="HelperAgent", instructions="You are a helpful assistant." ) as agent
```

OpenAI API-та за `Responses`, `ChatCompletion`

```python
agent = OpenAIResponsesClient().create_agent( name="WeatherBot", instructions="You are a helpful weather assistant.", )
```

```python
agent = OpenAIChatClient().create_agent( name="HelpfulAssistant", instructions="You are a helpful assistant.", )
```

или [MiniMax](https://platform.minimaxi.com/), която предоставя OpenAI-съвместим API с големи контекстуални прозорци (до 204K токена):

```python
agent = OpenAIChatClient(base_url="https://api.minimax.io/v1", api_key=os.environ["MINIMAX_API_KEY"], model_id="MiniMax-M3").create_agent( name="HelpfulAssistant", instructions="You are a helpful assistant.", )
```

или отдалечени агенти чрез протокола A2A:

```python
agent = A2AAgent( name=agent_card.name, description=agent_card.description, agent_card=agent_card, url="https://your-a2a-agent-host" )
```

**Изпълнение на агенти**

Агентите се изпълняват чрез методите `.run` или `.run_stream` за отговори без стрийминг или със стрийминг.

```python
result = await agent.run("What are good places to visit in Amsterdam?")
print(result.text)
```

```python
async for update in agent.run_stream("What are the good places to visit in Amsterdam?"):
    if update.text:
        print(update.text, end="", flush=True)

```

Всяко изпълнение на агент може да има опции за персонализиране на параметри като `max_tokens`, които агентът използва, `tools`, които агентът може да извиква, и дори самия `model`, използван за агента.

Това е полезно в случаи, когато за изпълнението на задача на потребителя са необходими конкретни модели или инструменти.

**Инструменти**

Инструментите могат да се дефинират както при създаването на агента:

```python
def get_attractions( location: Annotated[str, Field(description="The location to get the top tourist attractions for")], ) -> str: """Get the top tourist attractions for a given location.""" return f"The top attractions for {location} are." 


# Когато създавате директно ChatAgent

agent = ChatAgent( chat_client=OpenAIChatClient(), instructions="You are a helpful assistant", tools=[get_attractions]

```

така и при изпълнението на агента:

```python

result1 = await agent.run( "What's the best place to visit in Seattle?", tools=[get_attractions] # Инструмент, предоставен само за това изпълнение )
```

**Нишки на агента**

Нишките на агента се използват за обработка на многократни разговори. Нишки могат да се създадат чрез:

- Използване на `get_new_thread()`, което позволява нишката да се запазва във времето
- Автоматично създаване на нишка при изпълнение на агент, която съществува само по време на текущото изпълнение.

За създаване на нишка, кодът изглежда така:

```python
# Създайте нова нишка.
thread = agent.get_new_thread() # Стартирайте агента с нишката.
response = await agent.run("Hello, I am here to help you book travel. Where would you like to go?", thread=thread)

```

След това нишката може да бъде сериализирана за съхранение и по-късна употреба:

```python
# Създайте нов нишков процес.
thread = agent.get_new_thread() 

# Стартирайте агента с нишковия процес.

response = await agent.run("Hello, how are you?", thread=thread) 

# Серилизирайте нишковия процес за съхранение.

serialized_thread = await thread.serialize() 

# Десерилиширайте състоянието на нишковия процес след зареждане от съхранение.

resumed_thread = await agent.deserialize_thread(serialized_thread)
```

**Междинен софтуер на агента**

Агентите взаимодействат с инструменти и LLM, за да изпълняват задачи на потребителя. В определени ситуации искаме да изпълним или проследим действия при тези взаимодействия. Мидълуеърът на агента ни позволява това чрез:

*Функционален междинен софтуер*

Този междинен софтуер позволява изпълнение на действие между агента и функция/инструмент, който той ще извиква. Пример за използване може да бъде логиране при извикване на функцията.

В кода по-долу `next` определя дали да се извика следващият междинен софтуер или самата функция.

```python
async def logging_function_middleware(
    context: FunctionInvocationContext,
    next: Callable[[FunctionInvocationContext], Awaitable[None]],
) -> None:
    """Function middleware that logs function execution."""
    # Предварителна обработка: Лог преди изпълнението на функцията
    print(f"[Function] Calling {context.function.name}")

    # Продължи към следващия middleware или изпълнение на функцията
    await next(context)

    # Последваща обработка: Лог след изпълнението на функцията
    print(f"[Function] {context.function.name} completed")
```

*Чат междинен софтуер*

Този междинен софтуер позволява изпълнение или логване на действие между агента и заявките към LLM.

Той съдържа важна информация като `messages`, които се изпращат към AI услугата.

```python
async def logging_chat_middleware(
    context: ChatContext,
    next: Callable[[ChatContext], Awaitable[None]],
) -> None:
    """Chat middleware that logs AI interactions."""
    # Предварителна обработка: Запис преди извикване на AI
    print(f"[Chat] Sending {len(context.messages)} messages to AI")

    # Продължаване към следващия посреднически слой или AI услуга
    await next(context)

    # Последваща обработка: Запис след отговор от AI
    print("[Chat] AI response received")

```

**Памет на агента**

Както беше разгледано в урока `Agentic Memory`, паметта е важен елемент за работа на агента в различни контексти. MAF предлага няколко различни типа памет:

*Вътрешна памет*

Това е паметта, съхранявана в нишки по време на работа на приложението.

```python
# Създайте нов поток.
thread = agent.get_new_thread() # Стартирайте агента с потока.
response = await agent.run("Hello, I am here to help you book travel. Where would you like to go?", thread=thread)
```

*Постоянни съобщения*

Тази памет се използва за съхраняване на история на разговорите през различни сесии. Тя се дефинира чрез `chat_message_store_factory`:

```python
from agent_framework import ChatMessageStore

# Създаване на персонализирано хранилище за съобщения
def create_message_store():
    return ChatMessageStore()

agent = ChatAgent(
    chat_client=OpenAIChatClient(),
    instructions="You are a Travel assistant.",
    chat_message_store_factory=create_message_store
)

```

*Динамична памет*

Тази памет се добавя към контекста преди изпълняване на агентите. Тя може да се съхранява в външни услуги като mem0:

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

Наблюдаемостта е важна за създаване на надеждни и поддържани агентни системи. MAF се интегрира с OpenTelemetry за осигуряване на проследяване и метрики за по-добра наблюдаемост.

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

MAF предлага работни потоци, които са предефинирани стъпки за изпълнение на задача и включват AI агенти като компоненти в тези стъпки.

Работните потоци се състоят от различни компоненти, които позволяват по-добър контрол на потока. Те също така позволяват **оркестрация с много агенти** и **запазване на състояние** за съхранение на състояния на работния поток.

Основните компоненти на работния поток са:

**Изпълнители**

Изпълнителите получават входни съобщения, изпълняват възложените им задачи и произвеждат изходно съобщение. Това придвижва работния поток към завършване на по-голямата задача. Изпълнителите могат да бъдат AI агенти или потребителска логика.

**Връзки**

Връзките се използват за дефиниране на потока на съобщенията в работния поток. Те могат да бъдат:

*Директни връзки* – прости връзки едно към едно между изпълнители:

```python
from agent_framework import WorkflowBuilder

builder = WorkflowBuilder()
builder.add_edge(source_executor, target_executor)
builder.set_start_executor(source_executor)
workflow = builder.build()
```

*Условни връзки* – активират се след като определено условие е изпълнено. Например, когато хотелските стаи не са налични, изпълнителят може да предложи други опции.

*Връзки тип "switch-case"* – маршрутизират съобщенията към различни изпълнители на базата на дефинирани условия. Например, ако клиент за пътуване има приоритетен достъп, задачите му ще се обработват през друг работен поток.

*Връзки за разклонение (Fan-out)* – изпращат едно съобщение към множество цели.

*Връзки за сливане (Fan-in)* – събират множество съобщения от различни изпълнители и ги изпращат към една цел.

**Събития**

За по-добра наблюдаемост на работните потоци, MAF предлага вградени събития за изпълнение, включващи:

- `WorkflowStartedEvent` - Започване на изпълнение на работния поток
- `WorkflowOutputEvent` - Работният поток произвежда изход
- `WorkflowErrorEvent` - Възниква грешка в работния поток
- `ExecutorInvokeEvent` - Изпълнителят започва обработка
- `ExecutorCompleteEvent` - Изпълнителят завършва обработката
- `RequestInfoEvent` - Извършва се заявка

## Напреднали модели на MAF

Горните раздели покриват основните концепции на Microsoft Agent Framework. При създаване на по-сложни агенти, ето някои напреднали модели за разглеждане:

- **Състав на междинен софтуер**: Свържете множество обработващи междинен софтуер (логиране, удостоверяване, ограничаване на честота) чрез функционален и чат междинен софтуер за прецизен контрол върху поведението на агента.
- **Запазване на състояние на работния поток**: Използвайте събития и сериализация на работния поток за съхранение и възобновяване на дългосрочни процеси на агента.
- **Динамичен избор на инструменти**: Комбинирайте RAG върху описания на инструменти с регистрацията на инструменти на MAF, за да представите само релевантните инструменти за всяка заявка.
- **Множество агенти при прехвърляне**: Използвайте връзките и условната маршрутизация в работния поток за оркестрация на прехвърляне между специализирани агенти.

## Примери с код

Примери с код за Microsoft Agent Framework могат да бъдат намерени в това хранилище под файловете `xx-python-agent-framework` и `xx-dotnet-agent-framework`.

## Имате още въпроси за Microsoft Agent Framework?

Присъединете се към [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D), за да се срещнете с други учащи, да участвате в офис часове и да получите отговори на въпросите си за AI агенти.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Отказ от отговорност**:
Този документ е преведен с помощта на AI преводачески услуга [Co-op Translator](https://github.com/Azure/co-op-translator). Въпреки че се стремим към точност, моля имайте предвид, че автоматизираните преводи могат да съдържат грешки или неточности. Оригиналният документ на неговия роден език трябва да се счита за авторитетен източник. За критична информация се препоръчва професионален човешки превод. Ние не носим отговорност за каквито и да е недоразумения или неправилни тълкувания, произтичащи от използването на този превод.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->