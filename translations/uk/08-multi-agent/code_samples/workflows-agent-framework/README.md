# Створення багатокомпонентних додатків за допомогою Microsoft Agent Framework Workflow

Цей посібник допоможе вам зрозуміти та створити багатокомпонентні додатки, використовуючи Microsoft Agent Framework. Ми розглянемо основні концепції багатокомпонентних систем, заглибимося в архітектуру компонента Workflow цього фреймворку та пройдемо практичні приклади на Python і .NET для різних шаблонів робочих процесів.

## 1\. Розуміння багатокомпонентних систем

AI-агент — це система, яка перевершує можливості стандартної великої мовної моделі (LLM). Вона може сприймати своє середовище, приймати рішення та виконувати дії для досягнення конкретних цілей. Багатокомпонентна система включає кілька таких агентів, які співпрацюють для вирішення проблеми, яку було б складно або неможливо вирішити одному агенту.

### Загальні сценарії застосування

  * **Розв'язання складних задач**: Розбиття великого завдання (наприклад, планування корпоративного заходу) на менші підзадачі, які виконують спеціалізовані агенти (наприклад, агент бюджету, агент логістики, агент маркетингу).
  * **Віртуальні асистенти**: Основний агент-асистент делегує завдання, такі як планування, дослідження та бронювання, іншим спеціалізованим агентам.
  * **Автоматизоване створення контенту**: Робочий процес, де один агент створює контент, інший перевіряє його на точність і тональність, а третій публікує його.

### Шаблони багатокомпонентних систем

Багатокомпонентні системи можуть бути організовані за кількома шаблонами, які визначають, як вони взаємодіють:

  * **Послідовний**: Агенти працюють у визначеному порядку, як на конвеєрі. Вихід одного агента стає входом для наступного.
  * **Паралельний**: Агенти працюють одночасно над різними частинами завдання, а їх результати об'єднуються в кінці.
  * **Умовний**: Робочий процес слідує різними шляхами залежно від результату роботи агента, подібно до оператора if-then-else.

## 2\. Архітектура Workflow у Microsoft Agent Framework

Система Workflow у Agent Framework — це вдосконалений механізм оркестрації, призначений для управління складними взаємодіями між кількома агентами. Вона побудована на графовій архітектурі, яка використовує [модель виконання Pregel](https://kowshik.github.io/JPregel/pregel_paper.pdf), де обробка відбувається в синхронізованих кроках, які називаються "суперкроками".

### Основні компоненти

Архітектура складається з трьох основних частин:

1.  **Виконавці**: Це основні одиниці обробки. У наших прикладах `Agent` є типом виконавця. Кожен виконавець може мати кілька обробників повідомлень, які автоматично викликаються залежно від типу отриманого повідомлення.
2.  **Ребра**: Визначають шлях, яким повідомлення передаються між виконавцями. Ребра можуть мати умови, що дозволяють динамічно маршрутизувати інформацію через граф робочого процесу.
3.  **Workflow**: Цей компонент оркеструє весь процес, керуючи виконавцями, ребрами та загальним потоком виконання. Він забезпечує обробку повідомлень у правильному порядку та транслює події для спостереження.

*Діаграма, що ілюструє основні компоненти системи Workflow.*

Ця структура дозволяє створювати надійні та масштабовані додатки, використовуючи базові шаблони, такі як послідовні ланцюги, fan-out/fan-in для паралельної обробки та логіку switch-case для умовних потоків.

## 3\. Практичні приклади та аналіз коду

Тепер розглянемо, як реалізувати різні шаблони робочих процесів за допомогою фреймворку. Ми розглянемо приклади коду на Python і .NET для кожного випадку.

### Випадок 1: Базовий послідовний робочий процес

Це найпростіший шаблон, де вихід одного агента передається безпосередньо іншому. Наш сценарій включає агента `FrontDesk`, який робить рекомендацію щодо подорожі, а потім її переглядає агент `Concierge`.

*Діаграма базового робочого процесу FrontDesk -\> Concierge.*

#### Сценарій

Мандрівник запитує рекомендацію щодо Парижа.

1.  Агент `FrontDesk`, орієнтований на стислість, пропонує відвідати Лувр.
2.  Агент `Concierge`, який надає перевагу автентичним враженням, отримує цю пропозицію. Він переглядає рекомендацію та пропонує більш локальну, менш туристичну альтернативу.

#### Аналіз реалізації на Python

У прикладі на Python ми спочатку визначаємо та створюємо двох агентів, кожен із конкретними інструкціями.

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

Далі використовується `WorkflowBuilder` для побудови графа. `front_desk_agent` встановлюється як початкова точка, і створюється ребро для з'єднання його виходу з `reviewer_agent`.

```python
# 01.python-agent-framework-workflow-ghmodel-basic.ipynb

workflow = WorkflowBuilder().set_start_executor(front_desk_agent).add_edge(front_desk_agent, reviewer_agent).build()
```

Нарешті, робочий процес виконується з початковим запитом користувача.

```python
# 01.python-agent-framework-workflow-ghmodel-basic.ipynb

result =''
# The run_stream method executes the workflow and streams events.
async for event in workflow.run_stream('I would like to go to Paris.'):
    if isinstance(event, WorkflowEvent):
        result += str(event.data)
```

#### Аналіз реалізації на .NET (C#)

Реалізація на .NET дотримується дуже схожої логіки. Спочатку визначаються константи для імен агентів та їх інструкцій.

```csharp
// 01.dotnet-agent-framework-workflow-ghmodel-basic.ipynb

const string ReviewerAgentName = "Concierge";
const string ReviewerAgentInstructions = @"
    You are an are hotel concierge who has opinions about providing the most local and authentic experiences for travelers...";

const string FrontDeskAgentName = "FrontDesk";
const string FrontDeskAgentInstructions = @"""
    You are a Front Desk Travel Agent with ten years of experience and are known for brevity...";
```

Агенти створюються за допомогою `OpenAIClient`, а потім `WorkflowBuilder` визначає послідовний потік, додаючи ребро від `frontDeskAgent` до `reviewerAgent`.

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

Робочий процес запускається з повідомленням користувача, а результати транслюються назад.

### Випадок 2: Багатокроковий послідовний робочий процес

Цей шаблон розширює базову послідовність, включаючи більше агентів. Він ідеально підходить для процесів, які потребують кількох етапів уточнення або трансформації.

#### Сценарій

Користувач надає зображення вітальні та запитує оцінку меблів.

1.  **Sales-Agent**: Визначає меблі на зображенні та створює список.
2.  **Price-Agent**: Береться за список предметів і надає детальний розрахунок вартості, включаючи бюджетні, середні та преміум-варіанти.
3.  **Quote-Agent**: Отримує список із цінами та форматує його у формальний документ пропозиції в Markdown.

*Діаграма робочого процесу Sales -\> Price -\> Quote.*

#### Аналіз реалізації на Python

Три агенти визначаються, кожен із спеціалізованою роллю. Робочий процес будується за допомогою `add_edge`, щоб створити ланцюг: `sales_agent` -\> `price_agent` -\> `quote_agent`.

```python
# 02.python-agent-framework-workflow-ghmodel-sequential.ipynb

# Create three specialized agents
sales_agent = chat_client.create_agent(...)
price_agent = chat_client.create_agent(...)
quote_agent = chat_client.create_agent(...)

# Build the sequential workflow
workflow = WorkflowBuilder().set_start_executor(sales_agent).add_edge(sales_agent, price_agent).add_edge(price_agent, quote_agent).build()
```

Вхідні дані — це `ChatMessage`, що включає текст і URI зображення. Фреймворк обробляє передачу виходу кожного агента до наступного в послідовності, поки не буде створено фінальну пропозицію.

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

#### Аналіз реалізації на .NET (C#)

Приклад на .NET повторює версію на Python. Три агенти (`salesagent`, `priceagent`, `quoteagent`) створюються. `WorkflowBuilder` зв'язує їх послідовно.

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

Повідомлення користувача створюється з даними зображення (у вигляді байтів) і текстовим запитом. Метод `InProcessExecution.StreamAsync` запускає робочий процес, а фінальний результат отримується зі стріму.

### Випадок 3: Паралельний робочий процес

Цей шаблон використовується, коли завдання можна виконувати одночасно для економії часу. Він включає "fan-out" для кількох агентів і "fan-in" для об'єднання результатів.

#### Сценарій

Користувач просить спланувати поїздку до Сіетла.

1.  **Dispatcher (Fan-Out)**: Запит користувача надсилається двом агентам одночасно.
2.  **Researcher-Agent**: Досліджує пам'ятки, погоду та ключові аспекти поїздки до Сіетла в грудні.
3.  **Plan-Agent**: Незалежно створює детальний щоденний маршрут подорожі.
4.  **Aggregator (Fan-In)**: Результати від дослідника та планувальника збираються та представляються разом як фінальний результат.

*Діаграма паралельного робочого процесу Researcher і Planner.*

#### Аналіз реалізації на Python

`ConcurrentBuilder` спрощує створення цього шаблону. Ви просто перераховуєте агентів-учасників, і конструктор автоматично створює необхідну логіку fan-out і fan-in.

```python
# 03.python-agent-framework-workflow-ghmodel-concurrent.ipynb

research_agent = chat_client.create_agent(name="Researcher-Agent", ...)
plan_agent = chat_client.create_agent(name="Plan-Agent", ...)

# ConcurrentBuilder handles the fan-out/fan-in logic
workflow = ConcurrentBuilder().participants([research_agent, plan_agent]).build()

# Run the workflow
events = await workflow.run("Plan a trip to Seattle in December")
```

Фреймворк забезпечує виконання `research_agent` і `plan_agent` паралельно, а їх фінальні результати збираються в список.

#### Аналіз реалізації на .NET (C#)

У .NET цей шаблон вимагає більш явного визначення. Створюються спеціальні виконавці (`ConcurrentStartExecutor` і `ConcurrentAggregationExecutor`) для обробки логіки fan-out і fan-in.

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

`WorkflowBuilder` використовує `AddFanOutEdge` і `AddFanInEdge` для побудови графа з цими спеціальними виконавцями та агентами.

```csharp
// 03.dotnet-agent-framework-workflow-ghmodel-concurrent.ipynb

var workflow = new WorkflowBuilder(startExecutor)
            .AddFanOutEdge(startExecutor, targets: [researcherAgent, plannerAgent])
            .AddFanInEdge(aggregationExecutor, sources: [researcherAgent, plannerAgent])
            .WithOutputFrom(aggregationExecutor)
            .Build();
```

### Випадок 4: Умовний робочий процес

Умовні робочі процеси вводять логіку розгалуження, дозволяючи системі вибирати різні шляхи залежно від проміжних результатів.

#### Сценарій

Цей робочий процес автоматизує створення та публікацію технічного посібника.

1.  **Evangelist-Agent**: Пише чернетку посібника на основі заданого плану та URL-адрес.
2.  **ContentReviewer-Agent**: Переглядає чернетку. Перевіряє, чи кількість слів перевищує 200.
3.  **Умовне розгалуження**:
      * **Якщо схвалено (`Yes`)**: Робочий процес переходить до `Publisher-Agent`.
      * **Якщо відхилено (`No`)**: Робочий процес зупиняється та виводить причину відхилення.
4.  **Publisher-Agent**: Якщо чернетка схвалена, цей агент зберігає контент у файл Markdown.

#### Аналіз реалізації на Python

У цьому прикладі використовується спеціальна функція `select_targets` для реалізації умовної логіки. Ця функція передається до `add_multi_selection_edge_group` і спрямовує робочий процес на основі поля `review_result` з виходу рецензента.

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

Спеціальні виконавці, такі як `to_reviewer_result`, використовуються для аналізу JSON-виходу агентів і перетворення його в строго типізовані об'єкти, які функція вибору може перевірити.

#### Аналіз реалізації на .NET (C#)

Версія на .NET використовує схожий підхід із функцією умови. Визначається `Func<object?, bool` для перевірки властивості `Result` об'єкта `ReviewResult`.

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

Параметр `condition` методу `AddEdge` дозволяє `WorkflowBuilder` створити розгалужений шлях. Робочий процес слідуватиме ребру до `publishExecutor`, лише якщо умова `GetCondition(expectedResult: "Yes")` повертає true. В іншому випадку він слідує шляхом до `sendReviewerExecutor`.

## Висновок

Microsoft Agent Framework Workflow забезпечує надійну та гнучку основу для оркестрації складних багатокомпонентних систем. Використовуючи його графову архітектуру та основні компоненти, розробники можуть проектувати та реалізовувати складні робочі процеси як на Python, так і на .NET. Незалежно від того, чи ваш додаток потребує простого послідовного оброблення, паралельного виконання або динамічної умовної логіки, фреймворк пропонує інструменти для створення потужних, масштабованих і типізованих рішень на основі штучного інтелекту.

---

**Відмова від відповідальності**:  
Цей документ був перекладений за допомогою сервісу автоматичного перекладу [Co-op Translator](https://github.com/Azure/co-op-translator). Хоча ми прагнемо до точності, будь ласка, майте на увазі, що автоматичні переклади можуть містити помилки або неточності. Оригінальний документ на його рідній мові слід вважати авторитетним джерелом. Для критичної інформації рекомендується професійний людський переклад. Ми не несемо відповідальності за будь-які непорозуміння або неправильні тлумачення, що виникають внаслідок використання цього перекладу.