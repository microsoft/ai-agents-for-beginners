# Създаване на приложения с множество агенти с Microsoft Agent Framework Workflow

Този урок ще ви помогне да разберете и създадете приложения с множество агенти, използвайки Microsoft Agent Framework. Ще разгледаме основните концепции на системите с множество агенти, ще се запознаем с архитектурата на Workflow компонента на рамката и ще преминем през практически примери на Python и .NET за различни модели на работни потоци.

## 1\. Разбиране на системите с множество агенти

AI агент е система, която надхвърля възможностите на стандартен модел с голям езиков обхват (LLM). Тя може да възприема средата си, да взема решения и да предприема действия за постигане на конкретни цели. Система с множество агенти включва няколко такива агенти, които си сътрудничат за решаване на проблем, който би бил труден или невъзможен за един агент.

### Чести сценарии за приложение

  * **Решаване на сложни проблеми**: Разделяне на голяма задача (например планиране на събитие за цялата компания) на по-малки подзадачи, обработвани от специализирани агенти (например агент за бюджет, агент за логистика, агент за маркетинг).
  * **Виртуални асистенти**: Основен асистент агент, който делегира задачи като планиране, проучване и резервации на други специализирани агенти.
  * **Автоматизирано създаване на съдържание**: Работен поток, при който един агент създава чернова на съдържание, друг го преглежда за точност и тон, а трети го публикува.

### Модели на множество агенти

Системите с множество агенти могат да бъдат организирани в различни модели, които определят как те взаимодействат:

  * **Последователен**: Агенти работят в предварително определен ред, подобно на производствена линия. Изходът на един агент става вход за следващия.
  * **Едновременен**: Агенти работят паралелно върху различни части от задача, а резултатите им се обединяват в края.
  * **Условен**: Работният поток следва различни пътища въз основа на изхода на агент, подобно на if-then-else израз.

## 2\. Архитектура на Workflow в Microsoft Agent Framework

Системата за работни потоци на Agent Framework е усъвършенстван двигател за оркестрация, предназначен за управление на сложни взаимодействия между множество агенти. Тя е изградена върху архитектура, базирана на граф, която използва [Pregel-стил модел за изпълнение](https://kowshik.github.io/JPregel/pregel_paper.pdf), където обработката се извършва в синхронизирани стъпки, наречени "суперстъпки".

### Основни компоненти

Архитектурата се състои от три основни части:

1.  **Изпълнители**: Това са основните единици за обработка. В нашите примери, `Agent` е тип изпълнител. Всеки изпълнител може да има множество обработващи съобщения, които се извикват автоматично въз основа на типа на полученото съобщение.
2.  **Ръбове**: Те определят пътя, който съобщенията следват между изпълнителите. Ръбовете могат да имат условия, позволяващи динамично маршрутизиране на информацията през графа на работния поток.
3.  **Работен поток**: Този компонент оркестрира целия процес, управлява изпълнителите, ръбовете и общия поток на изпълнение. Той гарантира, че съобщенията се обработват в правилния ред и стриймва събития за наблюдение.

*Диаграма, илюстрираща основните компоненти на системата за работни потоци.*

Тази структура позволява изграждането на надеждни и мащабируеми приложения, използвайки основни модели като последователни вериги, разпределение и събиране за паралелна обработка и логика switch-case за условни потоци.

## 3\. Практически примери и анализ на код

Сега ще разгледаме как да реализираме различни модели на работни потоци, използвайки рамката. Ще разгледаме примери на Python и .NET за всеки случай.

### Случай 1: Основен последователен работен поток

Това е най-простият модел, при който изходът на един агент се предава директно на друг. Нашият сценарий включва агент `FrontDesk`, който прави препоръка за пътуване, която след това се преглежда от агент `Concierge`.

*Диаграма на основния работен поток FrontDesk -\> Concierge.*

#### Фон на сценария

Пътешественик пита за препоръка в Париж.

1.  Агентът `FrontDesk`, проектиран за краткост, предлага посещение на Лувъра.
2.  Агентът `Concierge`, който приоритизира автентични преживявания, получава тази препоръка. Той я преглежда и предлага обратна връзка, препоръчвайки по-местна, по-малко туристическа алтернатива.

#### Анализ на реализацията на Python

В Python примера първо дефинираме и създаваме двата агента, всеки със специфични инструкции.

```python
# 01.python-agent-framework-workflow-ghmodel-basic.ipynb

# Define agent roles and instructions
REVIEWER_NAME = "Concierge"
REVIEWER_INSTRUCTIONS = """
    You are an are hotel concierge who has opinions about providing the most local and authentic experiences for travelers...
    """

FRONTDESK_NAME = "FrontDesk"
FRONTDESK_INSTRUCTIONS = """
    You are a Front Desk Travel Agent with ten years of experience and are known for brevity...
    """

# Create agent instances
reviewer_agent = chat_client.create_agent(
    instructions=(REVIEWER_INSTRUCTIONS),
    name=REVIEWER_NAME,
)

front_desk_agent = chat_client.create_agent(
    instructions=(FRONTDESK_INSTRUCTIONS),
    name=FRONTDESK_NAME,
)
```

След това използваме `WorkflowBuilder`, за да изградим графа. `front_desk_agent` е зададен като начална точка, а ръб е създаден, за да свърже неговия изход с `reviewer_agent`.

```python
# 01.python-agent-framework-workflow-ghmodel-basic.ipynb

workflow = WorkflowBuilder().set_start_executor(front_desk_agent).add_edge(front_desk_agent, reviewer_agent).build()
```

Накрая, работният поток се изпълнява с първоначалния потребителски въпрос.

```python
# 01.python-agent-framework-workflow-ghmodel-basic.ipynb

result =''
# The run_stream method executes the workflow and streams events.
async for event in workflow.run_stream('I would like to go to Paris.'):
    if isinstance(event, WorkflowEvent):
        result += str(event.data)
```

#### Анализ на реализацията на .NET (C#)

Реализацията на .NET следва много подобна логика. Първо се дефинират константи за имената и инструкциите на агентите.

```csharp
// 01.dotnet-agent-framework-workflow-ghmodel-basic.ipynb

const string ReviewerAgentName = "Concierge";
const string ReviewerAgentInstructions = @"
    You are an are hotel concierge who has opinions about providing the most local and authentic experiences for travelers...";

const string FrontDeskAgentName = "FrontDesk";
const string FrontDeskAgentInstructions = @"""
    You are a Front Desk Travel Agent with ten years of experience and are known for brevity...";
```

Агентите се създават с помощта на `OpenAIClient`, след което `WorkflowBuilder` дефинира последователния поток, добавяйки ръб от `frontDeskAgent` към `reviewerAgent`.

```csharp
// 01.dotnet-agent-framework-workflow-ghmodel-basic.ipynb

// Create AIAgent instances
AIAgent reviewerAgent = openAIClient.GetChatClient(github_model_id).CreateAIAgent(
    name:ReviewerAgentName,instructions:ReviewerAgentInstructions);
AIAgent frontDeskAgent  = openAIClient.GetChatClient(github_model_id).CreateAIAgent(
    name:FrontDeskAgentName,instructions:FrontDeskAgentInstructions);

// Build the workflow
var workflow = new WorkflowBuilder(frontDeskAgent)
            .AddEdge(frontDeskAgent, reviewerAgent)
            .Build();
```

Работният поток се изпълнява с потребителското съобщение, а резултатите се стриймват обратно.

### Случай 2: Многоетапен последователен работен поток

Този модел разширява основната последователност, за да включи повече агенти. Той е идеален за процеси, които изискват множество етапи на усъвършенстване или трансформация.

#### Фон на сценария

Потребител предоставя изображение на дневна и иска оферта за мебели.

1.  **Sales-Agent**: Идентифицира мебелите в изображението и създава списък.
2.  **Price-Agent**: Взема списъка с артикули и предоставя подробна разбивка на цените, включително бюджетни, средни и премиум опции.
3.  **Quote-Agent**: Получава списъка с цени и го форматира в официален документ за оферта в Markdown.

*Диаграма на работния поток Sales -\> Price -\> Quote.*

#### Анализ на реализацията на Python

Три агента са дефинирани, всеки със специализирана роля. Работният поток се изгражда с помощта на `add_edge`, за да се създаде верига: `sales_agent` -\> `price_agent` -\> `quote_agent`.

```python
# 02.python-agent-framework-workflow-ghmodel-sequential.ipynb

# Create three specialized agents
sales_agent = chat_client.create_agent(...)
price_agent = chat_client.create_agent(...)
quote_agent = chat_client.create_agent(...)

# Build the sequential workflow
workflow = WorkflowBuilder().set_start_executor(sales_agent).add_edge(sales_agent, price_agent).add_edge(price_agent, quote_agent).build()
```

Входът е `ChatMessage`, който включва както текст, така и URI на изображението. Рамката обработва предаването на изхода на всеки агент към следващия в последователността, докато се генерира окончателната оферта.

```python
# 02.python-agent-framework-workflow-ghmodel-sequential.ipynb

# The user message contains both text and an image
message = ChatMessage(
        role=Role.USER,
        contents=[
            TextContent(text="Please find the relevant furniture..."),
            DataContent(uri=image_uri, media_type="image/png")
        ]
)

# Run the workflow
async for event in workflow.run_stream(message):
    ...
```

#### Анализ на реализацията на .NET (C#)

Примерът на .NET отразява версията на Python. Три агента (`salesagent`, `priceagent`, `quoteagent`) са създадени. `WorkflowBuilder` ги свързва последователно.

```csharp
// 02.dotnet-agent-framework-workflow-ghmodel-sequential.ipynb

// Create agent instances
AIAgent salesagent = openAIClient.GetChatClient(github_model_id).CreateAIAgent(...);
AIAgent priceagent  = openAIClient.GetChatClient(github_model_id).CreateAIAgent(...);
AIAgent quoteagent = openAIClient.GetChatClient(github_model_id).CreateAIAgent(...);

// Build the workflow by adding edges sequentially
var workflow = new WorkflowBuilder(salesagent)
            .AddEdge(salesagent,priceagent)
            .AddEdge(priceagent, quoteagent)
            .Build();
```

Потребителското съобщение е съставено както с данните за изображението (като байтове), така и с текстовия въпрос. Методът `InProcessExecution.StreamAsync` стартира работния поток, а окончателният изход се улавя от стрийма.

### Случай 3: Едновременен работен поток

Този модел се използва, когато задачите могат да се изпълняват едновременно, за да се спести време. Той включва "разпределение" към множество агенти и "събиране" за обединяване на резултатите.

#### Фон на сценария

Потребител иска да планира пътуване до Сиатъл.

1.  **Dispatcher (Разпределение)**: Заявката на потребителя се изпраща на два агента едновременно.
2.  **Researcher-Agent**: Проучва атракции, времето и ключови съображения за пътуване до Сиатъл през декември.
3.  **Plan-Agent**: Независимо създава подробен дневен план за пътуване.
4.  **Aggregator (Събиране)**: Резултатите от изследователя и планера се събират и представят заедно като окончателен резултат.

*Диаграма на едновременния работен поток Researcher и Planner.*

#### Анализ на реализацията на Python

`ConcurrentBuilder` опростява създаването на този модел. Просто изброявате участващите агенти, а билдърът автоматично създава необходимата логика за разпределение и събиране.

```python
# 03.python-agent-framework-workflow-ghmodel-concurrent.ipynb

research_agent = chat_client.create_agent(name="Researcher-Agent", ...)
plan_agent = chat_client.create_agent(name="Plan-Agent", ...)

# ConcurrentBuilder handles the fan-out/fan-in logic
workflow = ConcurrentBuilder().participants([research_agent, plan_agent]).build()

# Run the workflow
events = await workflow.run("Plan a trip to Seattle in December")
```

Рамката гарантира, че `research_agent` и `plan_agent` се изпълняват паралелно, а окончателните им изходи се събират в списък.

#### Анализ на реализацията на .NET (C#)

В .NET този модел изисква по-явно дефиниране. Създават се персонализирани изпълнители (`ConcurrentStartExecutor` и `ConcurrentAggregationExecutor`), за да се обработи логиката за разпределение и събиране.

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

`WorkflowBuilder` използва `AddFanOutEdge` и `AddFanInEdge`, за да изгради графа с тези персонализирани изпълнители и агентите.

```csharp
// 03.dotnet-agent-framework-workflow-ghmodel-concurrent.ipynb

var workflow = new WorkflowBuilder(startExecutor)
            .AddFanOutEdge(startExecutor, targets: [researcherAgent, plannerAgent])
            .AddFanInEdge(aggregationExecutor, sources: [researcherAgent, plannerAgent])
            .WithOutputFrom(aggregationExecutor)
            .Build();
```

### Случай 4: Условен работен поток

Условните работни потоци въвеждат логика за разклоняване, позволявайки на системата да следва различни пътища въз основа на междинни резултати.

#### Фон на сценария

Този работен поток автоматизира създаването и публикуването на технически урок.

1.  **Evangelist-Agent**: Пише чернова на урока въз основа на даден контур и URL адреси.
2.  **ContentReviewer-Agent**: Преглежда черновата. Проверява дали броят на думите е над 200.
3.  **Условен клон**:
      * **Ако е одобрено (`Yes`)**: Работният поток продължава към `Publisher-Agent`.
      * **Ако е отхвърлено (`No`)**: Работният поток спира и изходът е причината за отхвърляне.
4.  **Publisher-Agent**: Ако черновата е одобрена, този агент запазва съдържанието в Markdown файл.

#### Анализ на реализацията на Python

Този пример използва персонализирана функция, `select_targets`, за да реализира условната логика. Тази функция се предава на `add_multi_selection_edge_group` и насочва работния поток въз основа на полето `review_result` от изхода на рецензента.

```python
# 04.python-agent-framework-workflow-aifoundry-condition.ipynb

# This function determines the next step based on the review result
def select_targets(review: ReviewResult, target_ids: list[str]) -> list[str]:
    handle_review_id, save_draft_id = target_ids
    if review.review_result == "Yes":
        # If approved, proceed to the 'save_draft' executor
        return [save_draft_id]
    else:
        # If rejected, proceed to the 'handle_review' executor to report failure
        return [handle_review_id]

# The workflow builder uses the selection function for routing
workflow = (
    WorkflowBuilder()
        .set_start_executor(evangelist_agent)
        .add_edge(evangelist_agent, reviewer_agent)
        .add_edge(reviewer_agent, to_reviewer_result)
        # The multi-selection edge implements the conditional logic
        .add_multi_selection_edge_group(
            to_reviewer_result,
            [handle_review, save_draft],
            selection_func=select_targets,
        )
        .add_edge(save_draft, publisher_agent)
        .build()
)
```

Персонализирани изпълнители като `to_reviewer_result` се използват за анализиране на JSON изхода от агентите и конвертирането му в силно типизирани обекти, които функцията за избор може да инспектира.

#### Анализ на реализацията на .NET (C#)

Версията на .NET използва подобен подход с условна функция. `Func<object?, bool>` е дефинирана, за да провери свойството `Result` на обекта `ReviewResult`.

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

Параметърът `condition` на метода `AddEdge` позволява на `WorkflowBuilder` да създаде разклоняващ се път. Работният поток ще следва ръба към `publishExecutor` само ако условието `GetCondition(expectedResult: "Yes")` върне true. В противен случай следва пътя към `sendReviewerExecutor`.

## Заключение

Microsoft Agent Framework Workflow предоставя надеждна и гъвкава основа за оркестриране на сложни системи с множество агенти. Чрез използване на архитектурата, базирана на граф, и основните компоненти, разработчиците могат да проектират и реализират сложни работни потоци както на Python, така и на .NET. Независимо дали вашето приложение изисква проста последователна обработка, паралелно изпълнение или динамична условна логика, рамката предлага инструментите за изграждане на мощни, мащабируеми и типизирани AI решения.

---

**Отказ от отговорност**:  
Този документ е преведен с помощта на AI услуга за превод [Co-op Translator](https://github.com/Azure/co-op-translator). Въпреки че се стремим към точност, моля, имайте предвид, че автоматизираните преводи може да съдържат грешки или неточности. Оригиналният документ на неговия изходен език трябва да се счита за авторитетен източник. За критична информация се препоръчва професионален човешки превод. Ние не носим отговорност за каквито и да е недоразумения или погрешни интерпретации, произтичащи от използването на този превод.