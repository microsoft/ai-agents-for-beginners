# Побудова багатофункціональних додатків із Microsoft Agent Framework Workflow

Цей посібник допоможе вам зрозуміти та створювати багатофункціональні додатки, використовуючи Microsoft Agent Framework. Ми розглянемо основні концепції багатофункціональних систем, зануримось в архітектуру компонента Workflow фреймворку та пройдемося практичними прикладами на Python та .NET для різних шаблонів робочих процесів.

## 1\. Розуміння багатофункціональних систем

AI_agent — це система, яка виходить за межі можливостей стандартної великої мовної моделі (LLM). Вона може сприймати своє оточення, приймати рішення та здійснювати дії для досягнення конкретних цілей. Багатофункціональна система включає кілька таких агентів, які співпрацюють для вирішення проблеми, яку одному агенту було б складно або неможливо вирішити самостійно.

### Загальні сценарії застосування

  * **Розв’язання складних задач**: Розбиття великого завдання (наприклад, планування корпоративної події) на менші підзадачі, які обробляють спеціалізовані агенти (наприклад, агент з бюджету, агент логістики, маркетинговий агент).
  * **Віртуальні помічники**: Основний агент-помічник делегує завдання, такі як планування, дослідження та бронювання, іншим спеціалізованим агентам.
  * **Автоматичне створення контенту**: Робочий процес, де один агент готує чернетку контенту, інший перевіряє її на точність і тональність, а третій публікує її.

### Шаблони багатофункціональних систем

Багатофункціональні системи можуть бути організовані за кількома шаблонами, які визначають їхню взаємодію:

  * **Послідовний**: Агенти працюють у заздалегідь визначеному порядку, як конвеєр. Вихідні дані одного агента стають вхідними для наступного.
  * **Паралельний**: Агенти працюють одночасно над різними частинами завдання, а їхні результати об'єднуються наприкінці.
  * **Умовний**: Робочий процес слідує різними шляхами залежно від результату агента, подібно до оператора if-then-else.

## 2\. Архітектура Microsoft Agent Framework Workflow

Система робочого процесу Agent Framework — це розвинений двигун оркестрації, спроектований для керування складними взаємодіями між кількома агентами. Вона побудована на архітектурі на основі графа, яка використовує [модель виконання стилю Pregel](https://kowshik.github.io/JPregel/pregel_paper.pdf), де обробка відбувається в синхронізованих кроках, званих "supersteps".

### Основні компоненти

Архітектура складається з трьох основних частин:

1.  **Виконавці (Executors)**: це фундаментальні обчислювальні одиниці. У наших прикладах `Agent` — це тип виконавця. Кожен виконавець може мати кілька обробників повідомлень, які автоматично викликаються в залежності від типу отриманого повідомлення.
2.  **Ребра (Edges)**: вони визначають шлях, яким повідомлення передаються між виконавцями. Ребра можуть містити умови, що дозволяє динамічно маршрутизувати інформацію через граф робочого процесу.
3.  **Workflow**: цей компонент керує всім процесом, координуючи виконавців, ребра та загальний потік виконання. Він забезпечує правильний порядок обробки повідомлень і транслює події для моніторингу.

*Діаграма, що ілюструє основні компоненти системи робочого процесу.*

Ця структура дозволяє створювати надійні та масштабовані додатки, використовуючи базові шаблони, такі як послідовні ланцюжки, fan-out/fan-in для паралельної обробки та логіку switch-case для умовних потоків.

## 3\. Практичні приклади та аналіз коду

Тепер розглянемо, як реалізувати різні шаблони робочих процесів за допомогою фреймворку. Для кожного прикладу розглянемо код на Python та .NET.

### Приклад 1: Базовий послідовний робочий процес

Це найпростіший шаблон, де вихідні дані одного агента безпосередньо передаються іншому. Наш сценарій включає агента готелю `FrontDesk`, який робить рекомендацію для подорожі, потім її перевіряє агент `Concierge`.

*Діаграма базового робочого процесу FrontDesk -\> Concierge.*

#### Сценарій

Мандрівник просить рекомендацію для Парижа.

1.  Агент `FrontDesk`, націлений на короткі відповіді, пропонує відвідати Лувр.
2.  Агент `Concierge`, який цінує автентичний досвід, отримує цю пропозицію. Він переглядає рекомендацію та дає відгук, пропонуючи більш місцеву, менш туристичну альтернативу.

#### Аналіз реалізації на Python

У прикладі на Python спочатку визначаються та створюються два агенти, кожен зі своїми інструкціями.

```python
# 01.python-agent-framework-workflow-ghmodel-basic.ipynb

# Визначте ролі агентів та інструкції
REVIEWER_NAME = "Concierge"
REVIEWER_INSTRUCTIONS = """
    You are a hotel concierge who has opinions about providing the most local and authentic experiences for travelers...
    """

FRONTDESK_NAME = "FrontDesk"
FRONTDESK_INSTRUCTIONS = """
    You are a Front Desk Travel Agent with ten years of experience and are known for brevity...
    """

# Створіть екземпляри агентів
reviewer_agent = chat_client.as_agent(
    instructions=(REVIEWER_INSTRUCTIONS),
    name=REVIEWER_NAME,
)

front_desk_agent = chat_client.as_agent(
    instructions=(FRONTDESK_INSTRUCTIONS),
    name=FRONTDESK_NAME,
)
```

Далі за допомогою `WorkflowBuilder` будується граф. `front_desk_agent` встановлюється як початкова точка, створюється ребро, що з'єднує його вихід з `reviewer_agent`.

```python
# 01.python-agent-framework-workflow-ghmodel-basic.ipynb

workflow = WorkflowBuilder(start_executor=front_desk_agent).add_edge(front_desk_agent, reviewer_agent).build()
```

Нарешті, робочий процес запускається з початковим повідомленням користувача.

```python
# 01.python-agent-framework-workflow-ghmodel-basic.ipynb

result =''
# run виконує робочий процес; get_outputs() повертає результат виконавця виходу.
events = await workflow.run('I would like to go to Paris.')
outputs = events.get_outputs()
result = outputs[0].text if outputs else ''
```

#### Аналіз реалізації на .NET (C#)

Реалізація на .NET має дуже схожу логіку. Спочатку визначаються константи для імен та інструкцій агентів.

```csharp
// 01.dotnet-agent-framework-workflow-ghmodel-basic.ipynb

const string ReviewerAgentName = "Concierge";
const string ReviewerAgentInstructions = @"
    You are a hotel concierge who has opinions about providing the most local and authentic experiences for travelers...";

const string FrontDeskAgentName = "FrontDesk";
const string FrontDeskAgentInstructions = @"""
    You are a Front Desk Travel Agent with ten years of experience and are known for brevity...";
```

Агенти створюються за допомогою `AzureOpenAIClient` (Responses API), а `WorkflowBuilder` встановлює послідовний потік, додаючи ребро від `frontDeskAgent` до `reviewerAgent`.

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

Робочий процес виконується з повідомленням користувача, результати транслюються назад.

### Приклад 2: Багатокроковий послідовний робочий процес

Цей шаблон розширює базову послідовність, включаючи більшу кількість агентів. Ідеально підходить для процесів, які потребують кількох етапів уточнення або трансформації.

#### Сценарій

Користувач надає зображення вітальні й просить оцінку вартості меблів.

1.  **Sales-Agent**: Визначає меблі на зображенні та створює список.
2.  **Price-Agent**: Визначає ціну для кожного елемента, формуючи детальну калькуляцію з бюджетними, середніми та преміальними варіантами.
3.  **Quote-Agent**: Отримує цінову калькуляцію і форматує її у офіційний документ котирування у Markdown.

*Діаграма робочого процесу Sales -\> Price -\> Quote.*

#### Аналіз реалізації на Python

Визначено три агенти з спеціалізованими ролями. Робочий процес створюється методом `add_edge`, що формує ланцюжок: `sales_agent` -\> `price_agent` -\> `quote_agent`.

```python
# 02.python-agent-framework-workflow-ghmodel-sequential.ipynb

# Створіть трьох спеціалізованих агентів
sales_agent = chat_client.as_agent(...)
price_agent = chat_client.as_agent(...)
quote_agent = chat_client.as_agent(...)

# Побудуйте послідовний робочий процес
workflow = WorkflowBuilder(start_executor=sales_agent).add_edge(sales_agent, price_agent).add_edge(price_agent, quote_agent).build()
```

Вхідним повідомленням є `ChatMessage`, що включає текст і посилання на зображення. Фреймворк забезпечує передачу виходів кожного агента наступному в послідовності до створення кінцевої котирування.

```python
# 02.python-agent-framework-workflow-ghmodel-sequential.ipynb

# Повідомлення користувача містить як текст, так і зображення
message = ChatMessage(
        role=Role.USER,
        contents=[
            TextContent(text="Please find the relevant furniture..."),
            DataContent(uri=image_uri, media_type="image/png")
        ]
)

# Запустити робочий процес
events = await workflow.run(message)
```

#### Аналіз реалізації на .NET (C#)

Приклад на .NET повторює логіку Python версії. Створюються три агенти (`salesagent`, `priceagent`, `quoteagent`), які послідовно ланцюжком зв’язуються у `WorkflowBuilder`.

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

Повідомлення користувача формується з даних зображення (у вигляді байтів) та текстового запиту. Метод `InProcessExecution.RunStreamingAsync` запускає робочий процес, а кінцевий результат отримується зі стріму.

### Приклад 3: Паралельний робочий процес

Цей шаблон використовується, коли завдання можна виконувати одночасно, щоб заощадити час. Він включає "fan-out" до кількох агентів і "fan-in" для збирання результатів.

#### Сценарій

Користувач просить спланувати поїздку до Сіетла.

1.  **Dispatcher (Fan-Out)**: Запит користувача одночасно відправляється двом агентам.
2.  **Researcher-Agent**: Досліджує атракції, погоду та ключові особливості поїздки у Сіетл у грудні.
3.  **Plan-Agent**: Самостійно створює детальний покроковий план подорожі.
4.  **Aggregator (Fan-In)**: Результати роботи дослідника та планувальника збираються і подаються разом як кінцевий результат.

*Діаграма паралельного робочого процесу дослідника та планувальника.*

#### Аналіз реалізації на Python

`ConcurrentBuilder` спрощує створення цього шаблону. Просто перелікуйте агентів, що беруть участь, а билдер автоматично створить необхідну логіку fan-out і fan-in.

```python
# 03.python-agent-framework-workflow-ghmodel-concurrent.ipynb

research_agent = chat_client.as_agent(name="Researcher-Agent", ...)
plan_agent = chat_client.as_agent(name="Plan-Agent", ...)

# ConcurrentBuilder обробляє логіку розподілу/збирання
workflow = ConcurrentBuilder().participants([research_agent, plan_agent]).build()

# Запустити робочий процес
events = await workflow.run("Plan a trip to Seattle in December")
```

Фреймворк гарантує, що `research_agent` та `plan_agent` виконуються паралельно, а їхні кончені виходи збираються у список.

#### Аналіз реалізації на .NET (C#)

У .NET цей шаблон вимагає чіткішого визначення. Створюються користувацькі виконавці (`ConcurrentStartExecutor` і `ConcurrentAggregationExecutor`), які керують логікою fan-out і fan-in.

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

`WorkflowBuilder` використовує `AddFanOutEdge` і `AddFanInEdge` для побудови графа з цими виконавцями та агентами.

```csharp
// 03.dotnet-agent-framework-workflow-ghmodel-concurrent.ipynb

var workflow = new WorkflowBuilder(startExecutor)
            .AddFanOutEdge(startExecutor, targets: [researcherAgent, plannerAgent])
            .AddFanInEdge(aggregationExecutor, sources: [researcherAgent, plannerAgent])
            .WithOutputFrom(aggregationExecutor)
            .Build();
```

### Приклад 4: Умовний робочий процес

Умовні робочі процеси вводять логіку гілкування, дозволяючи системі обирати різні шляхи залежно від проміжних результатів.

#### Сценарій

Цей робочий процес автоматизує створення та публікацію технічного підручника.

1.  **Evangelist-Agent**: Пише чернетку підручника, базуючись на наданому плані та URL-адресах.
2.  **ContentReviewer-Agent**: Перевіряє чернетку. Переконується, що кількість слів більша за 200.
3.  **Умовна гілка**:
      * **Якщо затверджено (`Yes`)**: Робочий процес переходить до агента `Publisher-Agent`.
      * **Якщо відхилено (`No`)**: Робочий процес припиняється і виводиться причина відмови.
4.  **Publisher-Agent**: Якщо чернетку затверджено, цей агент зберігає контент у файл Markdown.

#### Аналіз реалізації на Python

У цьому прикладі використовується користувацька функція `select_targets`, яка реалізує умовну логіку. Ця функція передається методу `add_multi_selection_edge_group` і спрямовує робочий процес за полем `review_result` у виводі рев’юера.

```python
# 04.python-agent-framework-workflow-aifoundry-condition.ipynb

# Ця функція визначає наступний крок на основі результату перегляду
def select_targets(review: ReviewResult, target_ids: list[str]) -> list[str]:
    handle_review_id, save_draft_id = target_ids
    if review.review_result == "Yes":
        # Якщо затверджено, перейти до виконавця 'save_draft'
        return [save_draft_id]
    else:
        # Якщо відхилено, перейти до виконавця 'handle_review' для повідомлення про помилку
        return [handle_review_id]

# Конструктор робочого процесу використовує функцію вибору для маршрутизації
workflow = (
    WorkflowBuilder()
        .set_start_executor(evangelist_agent)
        .add_edge(evangelist_agent, reviewer_agent)
        .add_edge(reviewer_agent, to_reviewer_result)
        # Мультивибірне ребро реалізує умовну логіку
        .add_multi_selection_edge_group(
            to_reviewer_result,
            [handle_review, save_draft],
            selection_func=select_targets,
        )
        .add_edge(save_draft, publisher_agent)
        .build()
)
```

Використовуються користувацькі виконавці, такі як `to_reviewer_result`, для розбору JSON-виводу агентів і перетворення його у строго типізовані об’єкти, які може перевіряти функція вибору.

#### Аналіз реалізації на .NET (C#)

Версія для .NET використовує подібний підхід з функцією умови. Визначено `Func<object?, bool>`, яка перевіряє властивість `Result` об’єкта `ReviewResult`.

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

Параметр `condition` методу `AddEdge` дозволяє `WorkflowBuilder` створити гілкувальний шлях. Робочий процес йде по ребру до `publishExecutor` лише якщо умова `GetCondition(expectedResult: "Yes")` виконується. Інакше проходить шлях до `sendReviewerExecutor`.

## Висновок

Microsoft Agent Framework Workflow надає надійну та гнучку основу для оркестрації складних багатофункціональних систем. Використовуючи її архітектуру на основі графів та основні компоненти, розробники можуть проектувати та реалізовувати складні робочі процеси як на Python, так і на .NET. Незалежно від того, чи потрібен вам простий послідовний процес, паралельне виконання чи динамічна умовна логіка, цей фреймворк пропонує інструменти для створення потужних, масштабованих та типобезпечних рішень із підтримкою ШІ.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Відмова від відповідальності**:
Цей документ було перекладено за допомогою сервісу штучного інтелекту для перекладу [Co-op Translator](https://github.com/Azure/co-op-translator). Хоча ми прагнемо до точності, будь ласка, майте на увазі, що автоматичні переклади можуть містити помилки або неточності. Оригінальний документ рідною мовою слід вважати авторитетним джерелом. Для критично важливої інформації рекомендується професійний людський переклад. Ми не несемо відповідальності за будь-які непорозуміння або неправильні тлумачення, що виникли внаслідок використання цього перекладу.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->