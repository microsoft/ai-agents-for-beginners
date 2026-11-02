# Създаване на мулти-агентни приложения с Microsoft Agent Framework Workflow

Този урок ще ви преведе през разбирането и създаването на мулти-агентни приложения с използване на Microsoft Agent Framework. Ще разгледаме основните концепции на мулти-агентните системи, ще се потопим в архитектурата на Workflow компонента на фреймуърка и ще преминем през практически примери както на Python, така и на .NET за различни модели на работен процес.

## 1\. Разбиране на мулти-агентните системи

AI агентът е система, която надхвърля възможностите на стандартен голям езиков модел (LLM). Той може да възприема своята среда, да взема решения и да предприема действия за постигане на конкретни цели. Мулти-агентната система включва няколко такива агента, които си сътрудничат за решаване на проблем, който би бил труден или невъзможен за обработка от един агент самостоятелно.

### Чести приложения

  * **Сложно решаване на проблеми**: Разделяне на голяма задача (напр. планиране на фирмено събитие) на по-малки подзадачи, които се обработват от специализирани агенти (напр. агент за бюджет, агент за логистика, агент за маркетинг).
  * **Виртуални асистенти**: Главен асистент, който делегира задачи като планиране, проучване и резервации на други специализирани агенти.
  * **Автоматизирано създаване на съдържание**: Работен процес, в който един агент чернова съдържание, друг го преглежда за точност и тон, а трети го публикува.

### Мулти-агентни модели

Мулти-агентните системи могат да бъдат организирани в няколко модела, които определят как те си взаимодействат:

  * **Последователен**: Агентите работят в предварително определен ред, подобно на конвейерна линия. Изходните данни от един агент стават вход за следващия.
  * **Паралелен**: Агентите работят едновременно по различни части от задачата, а техните резултати се агрегатират накрая.
  * **Условен**: Работният процес следва различни пътища в зависимост от изхода на агент, подобно на конструкция if-then-else.

## 2\. Архитектура на Microsoft Agent Framework Workflow

Системата за работен процес на Agent Framework е усъвършенстван механизъм за оркестрация, проектиран да управлява сложни взаимодействия между няколко агента. Тя е изградена върху графово-базирана архитектура, която използва [Pregel-стил модел на изпълнение](https://kowshik.github.io/JPregel/pregel_paper.pdf), където обработката се извършва в синхронизирани стъпки, наречени "supersteps".

### Основни компоненти

Архитектурата се състои от три основни части:

1.  **Изпълнители**: Това са основните обработващи единици. В нашите примери `Agent` е тип изпълнител. Всеки изпълнител може да има множество обработващи съобщения функции, които се извикват автоматично според типа на полученото съобщение.
2.  **Ръбове**: Те дефинират пътя, по който съобщенията се преместват между изпълнителите. Ръбовете могат да имат условия, позволяващи динамично маршрутизиране на информация през графа на работния процес.
3.  **Workflow**: Този компонент оркестрира целия процес, управлявайки изпълнителите, ръбовете и общия поток на изпълнение. Той гарантира, че съобщенията се обработват в правилния ред и излъчва събития за наблюдаемост.

*Диаграма, илюстрираща основните компоненти на системата за работен процес.*

Тази структура позволява създаване на надеждни и разширяеми приложения, използвайки фундаментални модели като последователни вериги, fan-out/fan-in за паралелна обработка и switch-case логика за условни потоци.

## 3\. Практически примери и анализ на кода

Сега нека разгледаме как да реализираме различни модели на работен процес с използване на фреймуърка. Ще разгледаме примери и за Python, и за .NET.

### Случай 1: Основен последователен работен процес

Това е най-простият модел, при който изхода на един агент се предава директно на друг. В нашия сценарий хотелският агент `FrontDesk` прави препоръка за пътуване, която се разглежда от агент `Concierge`.

*Диаграма на основния работен процес FrontDesk -> Concierge.*

#### Фонов сценарий

Пътешественик иска препоръка за Париж.

1.  Агентът `FrontDesk`, настроен за краткост, предлага посещение на Лувъра.
2.  Агентът `Concierge`, който предпочита автентични преживявания, получава предложението. Той го преглежда и дава обратна връзка, препоръчвайки по-местна, по-малко туристическа алтернатива.

#### Анализ на Python имплементация

В Python примера първо се дефинират и създават двата агента, всеки с конкретни инструкции.

```python
# 01.python-agent-framework-workflow-ghmodel-basic.ipynb

# Определете роли и инструкции на агенти
REVIEWER_NAME = "Concierge"
REVIEWER_INSTRUCTIONS = """
    You are a hotel concierge who has opinions about providing the most local and authentic experiences for travelers...
    """

FRONTDESK_NAME = "FrontDesk"
FRONTDESK_INSTRUCTIONS = """
    You are a Front Desk Travel Agent with ten years of experience and are known for brevity...
    """

# Създайте екземпляри на агенти
reviewer_agent = chat_client.as_agent(
    instructions=(REVIEWER_INSTRUCTIONS),
    name=REVIEWER_NAME,
)

front_desk_agent = chat_client.as_agent(
    instructions=(FRONTDESK_INSTRUCTIONS),
    name=FRONTDESK_NAME,
)
```

След това се използва `WorkflowBuilder` за конструиране на графа. `front_desk_agent` е зададен като начална точка и се създава ръб, който свързва изхода му с `reviewer_agent`.

```python
# 01.python-agent-framework-workflow-ghmodel-basic.ipynb

workflow = WorkflowBuilder(start_executor=front_desk_agent).add_edge(front_desk_agent, reviewer_agent).build()
```

Накрая работният процес се изпълнява с началния потребителски въпрос.

```python
# 01.python-agent-framework-workflow-ghmodel-basic.ipynb

result =''
# run изпълнява работния процес; get_outputs() връща резултата на изпълнителя на изхода.
events = await workflow.run('I would like to go to Paris.')
outputs = events.get_outputs()
result = outputs[0].text if outputs else ''
```

#### Анализ на .NET (C\#) имплементация

Имплементацията на .NET следва много подобна логика. Първо се дефинират константи за имената и инструкциите на агентите.

```csharp
// 01.dotnet-agent-framework-workflow-ghmodel-basic.ipynb

const string ReviewerAgentName = "Concierge";
const string ReviewerAgentInstructions = @"
    You are a hotel concierge who has opinions about providing the most local and authentic experiences for travelers...";

const string FrontDeskAgentName = "FrontDesk";
const string FrontDeskAgentInstructions = @"""
    You are a Front Desk Travel Agent with ten years of experience and are known for brevity...";
```

Агентите се създават чрез `AzureOpenAIClient` (Responses API), след което `WorkflowBuilder` дефинира последователния поток, като добавя ръб от `frontDeskAgent` към `reviewerAgent`.

```csharp
// 01.dotnet-agent-framework-workflow-ghmodel-basic.ipynb

// Create AIAgent instances
AIAgent reviewerAgent = azureClient.GetChatClient(deployment).AsAIAgent(
    name:ReviewerAgentName,instructions:ReviewerAgentInstructions);
AIAgent frontDeskAgent  = azureClient.GetChatClient(deployment).AsAIAgent(
    name:FrontDeskAgentName,instructions:FrontDeskAgentInstructions);

// Build the workflow
var workflow = new WorkflowBuilder(frontDeskAgent)
            .AddEdge(frontDeskAgent, reviewerAgent)
            .Build();
```

Работният процес после се изпълнява с потребителско съобщение, а резултатите се предават обратно в стрийм.

### Случай 2: Многостепенен последователен работен процес

Този модел разширява основната последователност с повече агенти. Подходящ е за процеси, изискващи няколко етапа на усъвършенстване или трансформация.

#### Фонов сценарий

Потребител предоставя изображение на хол и иска оферта за мебели.

1.  **Агент по продажбите**: Идентифицира мебелите на изображението и съставя списък.
2.  **Агент по цените**: Взима списъка и дава подробна разбивка на цените, включително бюджетни, средни и премиум опции.
3.  **Агент по офертата**: Получава ценовия списък и го форматира във формален документ с оферта в Markdown.

*Диаграма на работния процес Sales -> Price -> Quote.*

#### Анализ на Python имплементация

Три агента са дефинирани, всеки със специализирана роля. Работният процес се построява чрез `add_edge` за създаване на верига: `sales_agent` -> `price_agent` -> `quote_agent`.

```python
# 02.python-agent-framework-workflow-ghmodel-sequential.ipynb

# Създайте три специализирани агенти
sales_agent = chat_client.as_agent(...)
price_agent = chat_client.as_agent(...)
quote_agent = chat_client.as_agent(...)

# Постройте последователния работен процес
workflow = WorkflowBuilder(start_executor=sales_agent).add_edge(sales_agent, price_agent).add_edge(price_agent, quote_agent).build()
```

Входящите данни са `ChatMessage`, които включват текст и URI на изображението. Фреймуъркът управлява предаването на изхода на всеки агент към следващия в последователността, докато се генерира финалната оферта.

```python
# 02.python-agent-framework-workflow-ghmodel-sequential.ipynb

# Съобщението от потребителя съдържа както текст, така и изображение
message = ChatMessage(
        role=Role.USER,
        contents=[
            TextContent(text="Please find the relevant furniture..."),
            DataContent(uri=image_uri, media_type="image/png")
        ]
)

# Стартирайте работния процес
events = await workflow.run(message)
```

#### Анализ на .NET (C\#) имплементация

.NET примерът отразява версията на Python. Три агента (`salesagent`, `priceagent`, `quoteagent`) са създадени. `WorkflowBuilder` ги свързва последователно.

```csharp
// 02.dotnet-agent-framework-workflow-ghmodel-sequential.ipynb

// Create agent instances
AIAgent salesagent = azureClient.GetChatClient(deployment).AsAIAgent(...);
AIAgent priceagent  = azureClient.GetChatClient(deployment).AsAIAgent(...);
AIAgent quoteagent = azureClient.GetChatClient(deployment).AsAIAgent(...);

// Build the workflow by adding edges sequentially
var workflow = new WorkflowBuilder(salesagent)
            .AddEdge(salesagent,priceagent)
            .AddEdge(priceagent, quoteagent)
            .Build();
```

Съобщението на потребителя се конструира с данни за изображението (като байтове) и текстовия въпрос. Методът `InProcessExecution.RunStreamingAsync` стартира работния процес, а крайният изход се извлича от потока.

### Случай 3: Паралелен работен процес

Този модел се използва, когато задачите могат да се изпълняват едновременно за пестене на време. Включва "fan-out" към няколко агента и "fan-in" за агрегиране на резултатите.

#### Фонов сценарий

Потребител иска да планира пътуване до Сиатъл.

1.  **Диспетчер (Fan-Out)**: Заявката се изпраща до два агента едновременно.
2.  **Агент изследовател**: Проучва забележителности, метеорология и ключови съображения за пътуване до Сиатъл през декември.
3.  **Агент планировчик**: Независимо създава подробен дневен маршрут за пътуването.
4.  **Агрегатор (Fan-In)**: Изходите от изследователя и планировчика се събират и представят заедно като крайния резултат.

*Диаграма на паралелния работен процес Researcher и Planner.*

#### Анализ на Python имплементация

`ConcurrentBuilder` опростява създаването на този модел. Просто изреждате участващите агенти, а билдърът автоматично създава необходимата логика за fan-out и fan-in.

```python
# 03.python-agent-framework-workflow-ghmodel-concurrent.ipynb

research_agent = chat_client.as_agent(name="Researcher-Agent", ...)
plan_agent = chat_client.as_agent(name="Plan-Agent", ...)

# ConcurrentBuilder обработва логиката за разклоняване/събиране
workflow = ConcurrentBuilder().participants([research_agent, plan_agent]).build()

# Стартиране на работния процес
events = await workflow.run("Plan a trip to Seattle in December")
```

Фреймуъркът гарантира, че `research_agent` и `plan_agent` изпълняват паралелно, а техните крайни резултати се събират в списък.

#### Анализ на .NET (C\#) имплементация

В .NET този модел изисква по-явно определение. Създават се потребителски изпълнители (`ConcurrentStartExecutor` и `ConcurrentAggregationExecutor`), които управляват логиката за fan-out и fan-in.

```csharp
// 03.dotnet-agent-framework-workflow-ghmodel-concurrent.ipynb

// Custom executor to broadcast the message to all agents
public class ConcurrentStartExecutor() : ...
{
    public async ValueTask HandleAsync(string message, IWorkflowContext context)
    {
        // Send message to all connected agents
        await context.SendMessageAsync(new ChatMessage(ChatRole.User, message));
        // Send a token to start processing
        await context.SendMessageAsync(new TurnToken(emitEvents: true));
    }
}

// Custom executor to collect results
public class ConcurrentAggregationExecutor() : ...
{
    private readonly List<ChatMessage> _messages = [];
    public async ValueTask HandleAsync(ChatMessage message, IWorkflowContext context)
    {
        this._messages.Add(message);
        // Once both agents have responded, yield the final output
        if (this._messages.Count == 2)
        {
            ...
            await context.YieldOutputAsync(formattedMessages);
        }
    }
}
```

`WorkflowBuilder` използва `AddFanOutEdge` и `AddFanInEdge`, за да изгради графа с тези потребителски изпълнители и агентите.

```csharp
// 03.dotnet-agent-framework-workflow-ghmodel-concurrent.ipynb

var workflow = new WorkflowBuilder(startExecutor)
            .AddFanOutEdge(startExecutor, targets: [researcherAgent, plannerAgent])
            .AddFanInEdge(aggregationExecutor, sources: [researcherAgent, plannerAgent])
            .WithOutputFrom(aggregationExecutor)
            .Build();
```

### Случай 4: Условен работен процес

Условните работни процеси въвеждат клонова логика, позволяваща системата да поеме различни пътища според междинни резултати.

#### Фонов сценарий

Този работен процес автоматизира създаването и публикуването на технически урок.

1.  **Агент евангелист**: Пише чернова на урока въз основа на зададен план и URL адреси.
2.  **Агент рецензент**: Преглежда черновата. Проверява дали броят на думите надвишава 200.
3.  **Условна клонка**:
      * **Ако одобрено (`Да`)**: Работният процес продължава към `Publisher-Agent`.
      * **Ако отхвърлено (`Не`)**: Работният процес спира и изкарва причина за отхвърлянето.
4.  **Агент издател**: Ако черновата е одобрена, този агент записва съдържанието във Markdown файл.

#### Анализ на Python имплементация

Този пример използва потребителска функция `select_targets`, за да реализира условната логика. Функцията се подава на `add_multi_selection_edge_group` и насочва работния процес според полето `review_result` от изхода на рецензента.

```python
# 04.python-agent-framework-workflow-aifoundry-condition.ipynb

# Тази функция определя следващата стъпка въз основа на резултата от прегледа
def select_targets(review: ReviewResult, target_ids: list[str]) -> list[str]:
    handle_review_id, save_draft_id = target_ids
    if review.review_result == "Yes":
        # Ако е одобрено, преминете към изпълнителя 'save_draft'
        return [save_draft_id]
    else:
        # Ако е отхвърлено, преминете към изпълнителя 'handle_review', за да отчетете неуспех
        return [handle_review_id]

# Създателят на работния процес използва функцията за избор за маршрутизиране
workflow = (
    WorkflowBuilder()
        .set_start_executor(evangelist_agent)
        .add_edge(evangelist_agent, reviewer_agent)
        .add_edge(reviewer_agent, to_reviewer_result)
        # Ръбът с множествен избор реализира условната логика
        .add_multi_selection_edge_group(
            to_reviewer_result,
            [handle_review, save_draft],
            selection_func=select_targets,
        )
        .add_edge(save_draft, publisher_agent)
        .build()
)
```

Персонализирани изпълнители като `to_reviewer_result` се използват, за да разпарцелират JSON изхода на агенти и да го конвертират в строго типизирани обекти, които функцията за избор може да преглежда.

#### Анализ на .NET (C\#) имплементация

Версията за .NET използва подобен подход с функция на условие. Дефинира се `Func<object?, bool>`, която проверява свойството `Result` на обекта `ReviewResult`.

```csharp
// 04.dotnet-agent-framework-workflow-aifoundry-condition.ipynb

// This function creates a lambda for the condition check
public Func<object?, bool> GetCondition(string expectedResult) =>
        reviewResult => reviewResult is ReviewResult review && review.Result == expectedResult;

// The workflow is built with conditional edges
var workflow = new WorkflowBuilder(draftExecutor)
            .AddEdge(draftExecutor, contentReviewerExecutor)
            // Add an edge to the publisher only if the review result is "Yes"
            .AddEdge(contentReviewerExecutor, publishExecutor, condition: GetCondition(expectedResult: "Yes"))
            // Add an edge to the reviewer feedback executor if the result is "No"
            .AddEdge(contentReviewerExecutor, sendReviewerExecutor, condition: GetCondition(expectedResult: "No"))
            .Build();
```

Параметърът `condition` на метода `AddEdge` позволява на `WorkflowBuilder` да създаде клонов път. Работният процес ще следва ръба към `publishExecutor` само ако условието `GetCondition(expectedResult: "Yes")` е вярно. В противен случай следва пътя към `sendReviewerExecutor`.

## Заключение

Microsoft Agent Framework Workflow предоставя стабилна и гъвкава основа за оркестриране на сложни мулти-агентни системи. Използвайки графово-базирана архитектура и основни компоненти, разработчиците могат да проектират и реализират усъвършенствани работни процеси както на Python, така и на .NET. Независимо дали вашето приложение изисква проста последователна обработка, паралелно изпълнение или динамична условна логика, фреймуъркът предлага инструменти за изграждане на мощни, мащабируеми и тип-безопасни AI-базирани решения.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Отказ от отговорност**:
Този документ е преведен с помощта на AI преводачески услуга [Co-op Translator](https://github.com/Azure/co-op-translator). Въпреки че се стремим към точност, моля имайте предвид, че автоматизираните преводи могат да съдържат грешки или неточности. Оригиналният документ на неговия роден език трябва да се счита за авторитетен източник. За критична информация се препоръчва професионален човешки превод. Ние не носим отговорност за каквито и да е недоразумения или неправилни тълкувания, произтичащи от използването на този превод.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->