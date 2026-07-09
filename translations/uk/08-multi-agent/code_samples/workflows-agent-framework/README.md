# Побудова багатокористувацьких застосунків із Microsoft Agent Framework Workflow

Цей підручник допоможе вам розібратися та створювати багатокористувацькі застосунки з використанням Microsoft Agent Framework. Ми розглянемо основні концепції багатокористувацьких систем, зануримося в архітектуру компонента Workflow фреймворку та розглянемо практичні приклади на Python і .NET для різних шаблонів робочого процесу.

## 1\. Розуміння багатокористувацьких систем

AI-агент — це система, яка виходить за рамки можливостей стандартної моделі великої мови (LLM). Він може сприймати своє оточення, приймати рішення та виконувати дії для досягнення конкретних цілей. Багатокористувацька система включає кілька таких агентів, які співпрацюють для розв’язання проблеми, яку було б складно або неможливо вирішити одному агенту.

### Поширені сценарії застосування

  * **Ускладнене розв’язання проблем**: Розбиття великого завдання (наприклад, планування події для всієї компанії) на менші підзавдання, якими керують спеціалізовані агенти (наприклад, агент бюджету, агент логістики, маркетинговий агент).
  * **Віртуальні помічники**: Головний агент-помічник, який делегує завдання, такі як планування, дослідження та бронювання іншим спеціалізованим агентам.
  * **Автоматизоване створення контенту**: Робочий процес, у якому один агент створює чернетку контенту, інший її перевіряє на точність і тон, а третій публікує.

### Шаблони багатокористувацьких систем

Багатокористувацькі системи можна організувати за кількома шаблонами, які визначають, як вони взаємодіють:

  * **Послідовний**: Агенти працюють у заздалегідь визначеному порядку, як конвеєр. Вихід одного агента стає вхідними даними для наступного.
  * **Паралельний**: Агенти працюють одночасно над різними частинами завдання, а їхні результати збираються в кінці.
  * **Умовний**: Робочий процес слідує різним шляхам залежно від виходу агента, як у конструкції if-then-else.

## 2\. Архітектура Microsoft Agent Framework Workflow

Система робочого процесу Agent Framework — це сучасний механізм оркестрації, призначений для управління складними взаємодіями між кількома агентами. Вона побудована на графовій архітектурі, яка використовує [модель виконання в стилі Pregel](https://kowshik.github.io/JPregel/pregel_paper.pdf), де обробка відбувається у синхронізованих кроках, що називаються "суперкроками".

### Основні компоненти

Архітектура складається з трьох основних частин:

1.  **Виконавці**: Це базові обчислювальні одиниці. У наших прикладах `Agent` є типом виконавця. Кожен виконавець може мати декілька обробників повідомлень, які автоматично викликаються залежно від типу отриманого повідомлення.
2.  **Ребра**: Визначають шлях, яким передаються повідомлення між виконавцями. Ребра можуть мати умови, що дозволяє динамічно маршрутизувати інформацію через граф робочого процесу.
3.  **Workflow**: Цей компонент координує весь процес, керуючи виконавцями, ребрами та загальним потоком виконання. Він забезпечує обробку повідомлень у правильному порядку та транслює події для спостереження.

*Діаграма, що ілюструє основні компоненти системи робочого процесу.*

Ця структура дозволяє створювати надійні та масштабовані застосунки, використовуючи базові шаблони, такі як послідовні ланцюги, фан-аут/фан-ін для паралельної обробки та логіку switch-case для умовних потоків.

## 3\. Практичні приклади та аналіз коду

Тепер давайте розглянемо, як реалізувати різні шаблони робочого процесу за допомогою фреймворку. Для кожного прикладу ми розглянемо код на Python і .NET.

### Випадок 1: Базовий послідовний робочий процес

Це найпростіший шаблон, де вихід одного агента безпосередньо передається іншому. Наш сценарій передбачає агента готельної `FrontDesk`, який дає рекомендацію щодо подорожі, а потім це перевіряє агент `Concierge`.

*Діаграма базового робочого процесу FrontDesk -> Concierge.*

#### Опис сценарію

Мандрівник просить рекомендацію для Парижа.

1.  Агент `FrontDesk`, призначений для лаконічності, пропонує відвідати Лувр.
2.  Агент `Concierge`, який віддає перевагу автентичним враженням, отримує цю пропозицію. Він переглядає рекомендацію та надає зворотній зв’язок, пропонуючи більш місцевий, менш туристичний варіант.

#### Аналіз реалізації на Python

У прикладі на Python спочатку визначаються та створюються два агенти з конкретними інструкціями.

```python
# 01.python-agent-framework-workflow-ghmodel-basic.ipynb

# Визначте ролі агентів та інструкції
REVIEWER_NAME = "Concierge"
REVIEWER_INSTRUCTIONS = """
    You are an are hotel concierge who has opinions about providing the most local and authentic experiences for travelers...
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

Потім використовується `WorkflowBuilder` для створення графа. Агент `front_desk_agent` встановлюється як початкова точка, і створюється ребро, що з’єднує його вихід з агентом `reviewer_agent`.

```python
# 01.python-agent-framework-workflow-ghmodel-basic.ipynb

workflow = WorkflowBuilder(start_executor=front_desk_agent).add_edge(front_desk_agent, reviewer_agent).build()
```

Нарешті, робочий процес виконується з початковим запитом користувача.

```python
# 01.python-agent-framework-workflow-ghmodel-basic.ipynb

result =''
# run виконує робочий процес; get_outputs() повертає результат виконавця виводу.
events = await workflow.run('I would like to go to Paris.')
outputs = events.get_outputs()
result = outputs[0].text if outputs else ''
```

#### Аналіз реалізації на .NET (C#)

Реалізація на .NET слідує дуже схожій логіці. Спочатку визначаються константи для імен агентів та інструкцій.

```csharp
// 01.dotnet-agent-framework-workflow-ghmodel-basic.ipynb

const string ReviewerAgentName = "Concierge";
const string ReviewerAgentInstructions = @"
    You are an are hotel concierge who has opinions about providing the most local and authentic experiences for travelers...";

const string FrontDeskAgentName = "FrontDesk";
const string FrontDeskAgentInstructions = @"""
    You are a Front Desk Travel Agent with ten years of experience and are known for brevity...";
```

Агенти створюються за допомогою `AzureOpenAIClient` (Responses API), а потім `WorkflowBuilder` визначає послідовний потік, додаючи ребро від `frontDeskAgent` до `reviewerAgent`.

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

Робочий процес запускається з повідомленням користувача, і результати транслюються назад.

### Випадок 2: Послідовний багатокроковий робочий процес

Цей шаблон розширює базову послідовність, включаючи більше агентів. Ідеальний для процесів, що потребують кількох етапів уточнення чи трансформації.

#### Опис сценарію

Користувач надає зображення вітальні і просить про кошторис меблів.

1.  **Агент продажу**: Визначає меблі на зображенні і створює список.
2.  **Агент ціноутворення**: Береться за список і надає детальний розподіл цін, включаючи бюджетні, середні та преміум варіанти.
3.  **Агент кошторису**: Отримує оціночний список і форматує його у формальний кошторис у Markdown.

*Діаграма робочого процесу Sales -> Price -> Quote.*

#### Аналіз реалізації на Python

Визначено трьох агентів з конкретними ролями. Робочий процес створюється за допомогою `add_edge`, формуючи ланцюг: `sales_agent` -> `price_agent` -> `quote_agent`.

```python
# 02.python-agent-framework-workflow-ghmodel-sequential.ipynb

# Створіть трьох спеціалізованих агентів
sales_agent = chat_client.as_agent(...)
price_agent = chat_client.as_agent(...)
quote_agent = chat_client.as_agent(...)

# Побудуйте послідовний робочий процес
workflow = WorkflowBuilder(start_executor=sales_agent).add_edge(sales_agent, price_agent).add_edge(price_agent, quote_agent).build()
```

Вхідними даними є `ChatMessage`, що включає текст і URI зображення. Фреймворк автоматично передає вихід кожного агента до наступного у послідовності, поки не буде створено кінцевий кошторис.

```python
# 02.python-agent-framework-workflow-ghmodel-sequential.ipynb

# Повідомлення користувача містить текст і зображення
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

Приклад на .NET відображає Python-версію. Створюється троє агентів (`salesagent`, `priceagent`, `quoteagent`), а `WorkflowBuilder` зв’язує їх послідовно.

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

Повідомлення користувача формується з даними зображення (у вигляді байтів) та текстовим запитом. Метод `InProcessExecution.StreamAsync` запускає робочий процес, і фінальний результат збирається з потоку.

### Випадок 3: Паралельний робочий процес

Цей шаблон використовується, коли завдання можуть виконуватись одночасно для економії часу. Він передбачає "fan-out" на кілька агентів і "fan-in" для збору результатів.

#### Опис сценарію

Користувач просить спланувати подорож до Сіетла.

1.  **Диспетчер (Fan-Out)**: Запит користувача одночасно надсилається двом агентам.
2.  **Агент-дослідник**: Досліджує пам’ятки, погоду та основні моменти для подорожі у Сіетл у грудні.
3.  **Агент планування**: Самостійно створює детальний щоденний маршрут подорожі.
4.  **Агрегатор (Fan-In)**: Виходи від обох агентів збираються та подаються разом як кінцевий результат.

*Діаграма паралельного робочого процесу для агентів-дослідника і планувальника.*

#### Аналіз реалізації на Python

`ConcurrentBuilder` спрощує створення цього шаблону. Достатньо перерахувати агентів, що беруть участь, і побудовник автоматично створює необхідну логіку fan-out і fan-in.

```python
# 03.python-agent-framework-workflow-ghmodel-concurrent.ipynb

research_agent = chat_client.as_agent(name="Researcher-Agent", ...)
plan_agent = chat_client.as_agent(name="Plan-Agent", ...)

# ConcurrentBuilder обробляє логіку розподілу та об’єднання потоків
workflow = ConcurrentBuilder().participants([research_agent, plan_agent]).build()

# Запустити робочий процес
events = await workflow.run("Plan a trip to Seattle in December")
```

Фреймворк забезпечує виконання `research_agent` та `plan_agent` паралельно, а їхні фінальні результати збираються у список.

#### Аналіз реалізації на .NET (C#)

У .NET цей шаблон потребує більш чіткого визначення. Створюються спеціальні виконавці (`ConcurrentStartExecutor` і `ConcurrentAggregationExecutor`) для обробки логіки fan-out і fan-in.

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

`WorkflowBuilder` потім використовує `AddFanOutEdge` і `AddFanInEdge`, щоб побудувати граф із цими спеціальними виконавцями та агентами.

```csharp
// 03.dotnet-agent-framework-workflow-ghmodel-concurrent.ipynb

var workflow = new WorkflowBuilder(startExecutor)
            .AddFanOutEdge(startExecutor, targets: [researcherAgent, plannerAgent])
            .AddFanInEdge(aggregationExecutor, sources: [researcherAgent, plannerAgent])
            .WithOutputFrom(aggregationExecutor)
            .Build();
```

### Випадок 4: Умовний робочий процес

Умовні робочі процеси вводять логіку розгалуження, яка дозволяє системі вибирати різні шляхи на основі проміжних результатів.

#### Опис сценарію

Цей робочий процес автоматизує створення та публікацію технічного підручника.

1.  **Агент-Євангеліст**: Пише чернетку підручника на основі заданої структури та URL-адрес.
2.  **Агент рецензента**: Перевіряє чернетку. Він перевіряє, чи кількість слів перевищує 200.
3.  **Умовна гілка**:
      * **Якщо схвалено (`Так`)**: робочий процес переходить до агента-видавця.
      * **Якщо відхилено (`Ні`)**: робочий процес зупиняється та виводить причину відхилення.
4.  **Агент-видавець**: Якщо чернетку схвалено, цей агент зберігає контент у Markdown файл.

#### Аналіз реалізації на Python

У цьому прикладі використовується користувацька функція `select_targets` для реалізації умовної логіки. Ця функція передається у `add_multi_selection_edge_group` і керує робочим процесом на основі поля `review_result` у виході рецензента.

```python
# 04.python-agent-framework-workflow-aifoundry-condition.ipynb

# Ця функція визначає наступний крок на основі результату рецензії
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
        # Край з множинним вибором реалізує умовну логіку
        .add_multi_selection_edge_group(
            to_reviewer_result,
            [handle_review, save_draft],
            selection_func=select_targets,
        )
        .add_edge(save_draft, publisher_agent)
        .build()
)
```

Користувацькі виконавці, як `to_reviewer_result`, використовуються для парсингу JSON-виходу агентів і перетворення його у строго типізовані об’єкти, які функція вибору може аналізувати.

#### Аналіз реалізації на .NET (C#)

Версія .NET використовує подібний підхід з умовною функцією. Визначається `Func<object?, bool>` для перевірки властивості `Result` об’єкта `ReviewResult`.

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

Параметр `condition` методу `AddEdge` дозволяє `WorkflowBuilder` створити розгалужений шлях. Робочий процес проходитиме ребро до `publishExecutor`, лише якщо умова `GetCondition(expectedResult: "Yes")` повертає true. Інакше буде обрано шлях до `sendReviewerExecutor`.

## Висновок

Microsoft Agent Framework Workflow забезпечує надійну та гнучку основу для оркестрації складних багатокористувацьких систем. Використовуючи його графову архітектуру та основні компоненти, розробники можуть проектувати та реалізовувати складні робочі процеси на Python і .NET. Незалежно від того, чи потребує ваш застосунок просту послідовну обробку, паралельне виконання або динамічну умовну логіку, фреймворк пропонує інструменти для створення потужних, масштабованих та типобезпечних AI-рішень.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Відмова від відповідальності**:
Цей документ було перекладено за допомогою сервісу штучного інтелекту для перекладу [Co-op Translator](https://github.com/Azure/co-op-translator). Хоча ми прагнемо до точності, будь ласка, майте на увазі, що автоматичні переклади можуть містити помилки або неточності. Оригінальний документ рідною мовою слід вважати авторитетним джерелом. Для критично важливої інформації рекомендується професійний людський переклад. Ми не несемо відповідальності за будь-які непорозуміння або неправильні тлумачення, що виникли внаслідок використання цього перекладу.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->