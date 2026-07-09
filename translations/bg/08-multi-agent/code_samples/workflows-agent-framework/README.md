# Създаване на многоагентни приложения с Microsoft Agent Framework Workflow

Това ръководство ще ви преведе през разбирането и създаването на многоагентни приложения с помощта на Microsoft Agent Framework. Ще разгледаме основните концепции на многоагентните системи, ще навлезем в архитектурата на Workflow компонента на фреймуърка и ще преминем през практически примери както на Python, така и на .NET за различни модели на работни потоци.

## 1\. Разбиране на многоагентните системи

AI агент е система, която надхвърля възможностите на стандартен голям езиков модел (LLM). Той може да възприема своето обкръжение, да взема решения и да предприема действия за постигане на конкретни цели. Многоагентната система включва няколко такива агенти, които си сътрудничат за решаване на проблем, който би бил труден или невъзможен за един-единствен агент да реши самостоятелно.

### Общи сценарии на приложение

  * **Решаване на сложни проблеми**: Разделяне на голяма задача (напр. планиране на фирмено събитие) на по-малки подзадачи, управляеми от специализирани агенти (напр. агент за бюджет, агент по логистика, маркетингов агент).
  * **Виртуални асистенти**: Основен агент асистент, който делегира задачи като планиране, проучване и резервации на други специализирани агенти.
  * **Автоматизирано създаване на съдържание**: Работен поток, в който един агент изготвя съдържание, друг го преглежда за точност и тон, а трети го публикува.

### Многоагентни модели

Многоагентните системи могат да бъдат организирани в няколко модела, които определят как те взаимодействат:

  * **Последователен**: Агентите работят в предварително зададен ред, като на поточна линия. Изходът от един агент става вход за следващия.
  * **Паралелен**: Агентите работят едновременно по различни части на задача, а резултатите им се събират накрая.
  * **Условен**: Работният поток следва различни пътища в зависимост от изхода на агента, подобно на условие if-then-else.

## 2\. Архитектура на Microsoft Agent Framework Workflow

Системата за работни потоци на Agent Framework е усъвършенстван оркестрационен двигател, предназначен за управление на сложни взаимодействия между множество агенти. Тя е изградена върху графова архитектура, която използва [Pregel-стил изпълнителен модел](https://kowshik.github.io/JPregel/pregel_paper.pdf), където обработката се осъществява в синхронизирани стъпки, наречени "supersteps."

### Основни компоненти

Архитектурата се състои от три основни части:

1.  **Изпълнители (Executors)**: Това са основните процесорни единици. В нашите примери `Agent` е тип изпълнител. Всеки изпълнител може да има множество обработващи съобщения функции, които се извикват автоматично в зависимост от типа на полученото съобщение.
2.  **Ръбове (Edges)**: Те дефинират пътя, по който съобщенията се движат между изпълнителите. Ръбовете могат да имат условия, позволяващи динамично маршрутизиране на информация през графа на работния поток.
3.  **Работен поток (Workflow)**: Този компонент оркестрира целия процес, управлявайки изпълнителите, ръбовете и цялостния поток на изпълнение. Той гарантира, че съобщенията се обработват в правилния ред и предава събития за наблюдение.

*Диаграма, илюстрираща основните компоненти на системата за работни потоци.*

Тази структура позволява създаването на надеждни и мащабируеми приложения, използвайки фундаментални модели като последователни вериги, fan-out/fan-in за паралелна обработка и switch-case логика за условни потоци.

## 3\. Практически примери и анализ на кода

Сега нека разгледаме как да реализираме различни модели на работни потоци с помощта на фреймуърка. Ще разгледаме както Python, така и .NET код за всеки пример.

### Случай 1: Основен последователен работен поток

Това е най-простият модел, при който изходът на един агент се предава директно на друг. Нашият сценарий включва хотелски агент `FrontDesk`, който дава препоръка за пътуване, която после се преглежда от агент `Concierge`.

*Диаграма на основния FrontDesk -\> Concierge работен поток.*

#### Контекст на сценария

Пътешественик иска препоръка за Париж.

1.  Агентът `FrontDesk`, ориентиран към краткост, предлага посещение на Лувъра.
2.  Агентът `Concierge`, който предпочита автентични преживявания, получава тази препоръка. Той я преглежда и дава обратна връзка, предлагайки по-местен, по-малко туристически вариант.

#### Анализ на имплементацията на Python

В Python примера първо дефинираме и създаваме двата агента, всеки със специфични инструкции.

```python
# 01.python-agent-framework-workflow-ghmodel-basic.ipynb

# Дефинирайте роли и инструкции на агентите
REVIEWER_NAME = "Concierge"
REVIEWER_INSTRUCTIONS = """
    You are an are hotel concierge who has opinions about providing the most local and authentic experiences for travelers...
    """

FRONTDESK_NAME = "FrontDesk"
FRONTDESK_INSTRUCTIONS = """
    You are a Front Desk Travel Agent with ten years of experience and are known for brevity...
    """

# Създайте инстанции на агенти
reviewer_agent = chat_client.as_agent(
    instructions=(REVIEWER_INSTRUCTIONS),
    name=REVIEWER_NAME,
)

front_desk_agent = chat_client.as_agent(
    instructions=(FRONTDESK_INSTRUCTIONS),
    name=FRONTDESK_NAME,
)
```

След това се използва `WorkflowBuilder` за изграждане на графа. `front_desk_agent` е зададен като начален, и се създава ръб, който свързва неговия изход с `reviewer_agent`.

```python
# 01.python-agent-framework-workflow-ghmodel-basic.ipynb

workflow = WorkflowBuilder(start_executor=front_desk_agent).add_edge(front_desk_agent, reviewer_agent).build()
```

Накрая, работният поток се изпълнява с първоначалното потребителско запитване.

```python
# 01.python-agent-framework-workflow-ghmodel-basic.ipynb

result =''
# run изпълнява работния процес; get_outputs() връща резултата от изпълнителя на изхода.
events = await workflow.run('I would like to go to Paris.')
outputs = events.get_outputs()
result = outputs[0].text if outputs else ''
```

#### Анализ на имплементацията на .NET (C#)

Имплементацията на .NET следва много подобна логика. Първо се дефинират константи за имената и инструкциите на агентите.

```csharp
// 01.dotnet-agent-framework-workflow-ghmodel-basic.ipynb

const string ReviewerAgentName = "Concierge";
const string ReviewerAgentInstructions = @"
    You are an are hotel concierge who has opinions about providing the most local and authentic experiences for travelers...";

const string FrontDeskAgentName = "FrontDesk";
const string FrontDeskAgentInstructions = @"""
    You are a Front Desk Travel Agent with ten years of experience and are known for brevity...";
```

Агентите се създават чрез `AzureOpenAIClient` (Responses API), след което `WorkflowBuilder` дефинира последователния поток чрез добавяне на ръб от `frontDeskAgent` към `reviewerAgent`.

```csharp
// 01.dotnet-agent-framework-workflow-ghmodel-basic.ipynb

// Create AIAgent instances
AIAgent reviewerAgent = azureClient.GetOpenAIResponseClient(deployment).CreateAIAgent(
    name:ReviewerAgentName,instructions:ReviewerAgentInstructions);
AIAgent frontDeskAgent  = azureClient.GetOpenAIResponseClient(deployment).CreateAIAgent(
    name:FrontDeskAgentName,instructions:FrontDeskAgentInstructions);

// Build the workflow
var workflow = new WorkflowBuilder(frontDeskAgent)
            .AddEdge(frontDeskAgent, reviewerAgent)
            .Build();
```

Работният поток се изпълнява със съобщението на потребителя, а резултатите се предават обратно чрез стрийм.

### Случай 2: Многоетапен последователен работен поток

Този модел разширява основната последователност, включвайки повече агенти. Подходящ е за процеси, които изискват множество етапи на усъвършенстване или трансформация.

#### Контекст на сценария

Потребител предоставя снимка на дневна и иска оферта за мебели.

1.  **Sales-Agent**: Идентифицира мебелите на снимката и съставя списък.
2.  **Price-Agent**: Взема списъка и предоставя детайлна разбивка на цените, включително бюджетни, среден клас и премиум опции.
3.  **Quote-Agent**: Получава ценовия списък и го форматира във формален офертен документ в Markdown.

*Диаграма на работния поток Sales -\> Price -\> Quote.*

#### Анализ на имплементацията на Python

Дефинират се трима агенти с ясни роли. Работният поток се изгражда с помощта на `add_edge`, който свързва в последователност: `sales_agent` -\> `price_agent` -\> `quote_agent`.

```python
# 02.python-agent-framework-workflow-ghmodel-sequential.ipynb

# Създайте трима специализирани агенти
sales_agent = chat_client.as_agent(...)
price_agent = chat_client.as_agent(...)
quote_agent = chat_client.as_agent(...)

# Изградете последователния работен поток
workflow = WorkflowBuilder(start_executor=sales_agent).add_edge(sales_agent, price_agent).add_edge(price_agent, quote_agent).build()
```

Входът е `ChatMessage`, който включва текст и URI на изображението. Фреймуъркът управлява предаването на изхода на всеки агент към следващия в реда, докато не се генерира крайната оферта.

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

#### Анализ на имплементацията на .NET (C#)

Примерът на .NET е подобен на версията на Python. Създават се трима агенти (`salesagent`, `priceagent`, `quoteagent`). `WorkflowBuilder` ги свързва последователно.

```csharp
// 02.dotnet-agent-framework-workflow-ghmodel-sequential.ipynb

// Create agent instances
AIAgent salesagent = azureClient.GetOpenAIResponseClient(deployment).CreateAIAgent(...);
AIAgent priceagent  = azureClient.GetOpenAIResponseClient(deployment).CreateAIAgent(...);
AIAgent quoteagent = azureClient.GetOpenAIResponseClient(deployment).CreateAIAgent(...);

// Build the workflow by adding edges sequentially
var workflow = new WorkflowBuilder(salesagent)
            .AddEdge(salesagent,priceagent)
            .AddEdge(priceagent, quoteagent)
            .Build();
```

Съобщението на потребителя съдържа както данни за изображението (като байтове), така и текстовия подсказ. Методът `InProcessExecution.StreamAsync` стартира работния поток, а крайните резултати се получават от потока.

### Случай 3: Паралелен работен поток

Този модел се използва когато задачите могат да се изпълняват едновременно, за да се спести време. Включва "fan-out" към множество агенти и "fan-in" за събиране на резултатите.

#### Контекст на сценария

Потребител иска да планира пътуване до Сиатъл.

1.  **Dispatcher (Fan-Out)**: Искането на потребителя се изпраща едновременно до два агента.
2.  **Researcher-Agent**: Проучва атракции, времето и ключови фактори за пътуване до Сиатъл през декември.
3.  **Plan-Agent**: Независимо съставя подробен дневен план за пътуването.
4.  **Aggregator (Fan-In)**: Изходите от изследователя и планиращия се събират и представят като краен резултат.

*Диаграма на паралелния работен поток Researcher и Planner.*

#### Анализ на имплементацията на Python

`ConcurrentBuilder` опростява създаването на този модел. Просто се изброяват участващите агенти, а билдърът автоматично създава необходимата fan-out и fan-in логика.

```python
# 03.python-agent-framework-workflow-ghmodel-concurrent.ipynb

research_agent = chat_client.as_agent(name="Researcher-Agent", ...)
plan_agent = chat_client.as_agent(name="Plan-Agent", ...)

# ConcurrentBuilder управлява логиката за разклоняване и събиране
workflow = ConcurrentBuilder().participants([research_agent, plan_agent]).build()

# Стартирайте работния поток
events = await workflow.run("Plan a trip to Seattle in December")
```

Фреймуъркът гарантира, че `research_agent` и `plan_agent` изпълняват паралелно, а крайните им изходи се събират в списък.

#### Анализ на имплементацията на .NET (C#)

В .NET този модел изисква по-явно дефиниране. Създават се персонализирани изпълнители (`ConcurrentStartExecutor` и `ConcurrentAggregationExecutor`), които обработват fan-out и fan-in логиката.

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

След това `WorkflowBuilder` използва `AddFanOutEdge` и `AddFanInEdge` за изграждането на графа с тези персонализирани изпълнители и агенти.

```csharp
// 03.dotnet-agent-framework-workflow-ghmodel-concurrent.ipynb

var workflow = new WorkflowBuilder(startExecutor)
            .AddFanOutEdge(startExecutor, targets: [researcherAgent, plannerAgent])
            .AddFanInEdge(aggregationExecutor, sources: [researcherAgent, plannerAgent])
            .WithOutputFrom(aggregationExecutor)
            .Build();
```

### Случай 4: Условен работен поток

Условните работни потоци въвеждат логика на разклонение, която позволява системата да следва различни пътища според междинни резултати.

#### Контекст на сценария

Този работен поток автоматизира създаването и публикуването на техническо ръководство.

1.  **Evangelist-Agent**: Пише чернова на ръководството въз основа на зададен план и URL адреси.
2.  **ContentReviewer-Agent**: Преглежда черновата. Проверява дали броят на думите е над 200.
3.  **Условно разклонение**:
      * **Ако одобрено (`Yes`)**: Работният поток продължава към `Publisher-Agent`.
      * **Ако отхвърлено (`No`)**: Работният поток спира и показва причината за отхвърляне.
4.  **Publisher-Agent**: Ако черновата е одобрена, този агент записва съдържанието в Markdown файл.

#### Анализ на имплементацията на Python

Този пример използва персонализирана функция `select_targets`, за да реализира условната логика. Функцията се подава на `add_multi_selection_edge_group` и насочва потока въз основа на полето `review_result` в изхода на рецензента.

```python
# 04.python-agent-framework-workflow-aifoundry-condition.ipynb

# Тази функция определя следващата стъпка въз основа на резултата от прегледа
def select_targets(review: ReviewResult, target_ids: list[str]) -> list[str]:
    handle_review_id, save_draft_id = target_ids
    if review.review_result == "Yes":
        # Ако е одобрено, продължете към изпълнителя 'save_draft'
        return [save_draft_id]
    else:
        # Ако е отхвърлено, продължете към изпълнителя 'handle_review', за да докладвате за неуспех
        return [handle_review_id]

# Създателят на работния процес използва функцията за избор за маршрутизиране
workflow = (
    WorkflowBuilder()
        .set_start_executor(evangelist_agent)
        .add_edge(evangelist_agent, reviewer_agent)
        .add_edge(reviewer_agent, to_reviewer_result)
        # Ръбът с множество избори реализира условната логика
        .add_multi_selection_edge_group(
            to_reviewer_result,
            [handle_review, save_draft],
            selection_func=select_targets,
        )
        .add_edge(save_draft, publisher_agent)
        .build()
)
```

Персонализирани изпълнители като `to_reviewer_result` се използват, за да парсират JSON изхода от агентите и да го конвертират в силно типизирани обекти, които функцията за избор може да инспектира.

#### Анализ на имплементацията на .NET (C#)

Версията на .NET използва подобен подход с функция за условие. Дефинира се `Func<object?, bool>`, която проверява свойството `Result` на обекта `ReviewResult`.

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

Методът `AddEdge` с параметър `condition` позволява на `WorkflowBuilder` да създаде разклонен път. Работният поток ще следва ръба към `publishExecutor` само ако условието `GetCondition(expectedResult: "Yes")` е вярно. В противен случай следва пътя към `sendReviewerExecutor`.

## Заключение

Microsoft Agent Framework Workflow предоставя стабилна и гъвкава основа за оркестриране на сложни многоагентни системи. Използвайки графовата архитектура и основните му компоненти, разработчиците могат да проектират и реализират усъвършенствани работни потоци както на Python, така и на .NET. Независимо дали вашето приложение изисква проста последователна обработка, паралелно изпълнение или динамична условна логика, фреймуъркът предлага инструменти за създаване на мощни, мащабируеми и типобезопасни AI решения.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Отказ от отговорност**:
Този документ е преведен с помощта на AI преводачески услуга [Co-op Translator](https://github.com/Azure/co-op-translator). Въпреки че се стремим към точност, моля имайте предвид, че автоматизираните преводи могат да съдържат грешки или неточности. Оригиналният документ на неговия роден език трябва да се счита за авторитетен източник. За критична информация се препоръчва професионален човешки превод. Ние не носим отговорност за каквито и да е недоразумения или неправилни тълкувания, произтичащи от използването на този превод.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->