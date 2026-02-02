# Создание приложений с несколькими агентами с использованием Microsoft Agent Framework Workflow

Этот учебник поможет вам понять и создать приложения с несколькими агентами, используя Microsoft Agent Framework. Мы изучим основные концепции систем с несколькими агентами, рассмотрим архитектуру компонента Workflow фреймворка и разберем практические примеры на Python и .NET для различных шаблонов рабочих процессов.

## 1\. Понимание систем с несколькими агентами

AI-агент — это система, которая превосходит возможности стандартной модели большого языка (LLM). Она может воспринимать окружающую среду, принимать решения и выполнять действия для достижения конкретных целей. Система с несколькими агентами включает несколько таких агентов, которые сотрудничают для решения задачи, которая была бы сложной или невозможной для одного агента.

### Общие сценарии применения

  * **Решение сложных задач**: Разделение крупной задачи (например, планирование корпоративного мероприятия) на более мелкие подзадачи, которые выполняются специализированными агентами (например, агент бюджета, агент логистики, агент маркетинга).
  * **Виртуальные помощники**: Основной агент-помощник делегирует задачи, такие как планирование, исследования и бронирование, другим специализированным агентам.
  * **Автоматизированное создание контента**: Рабочий процесс, где один агент создает черновик контента, другой проверяет его на точность и тон, а третий публикует его.

### Шаблоны систем с несколькими агентами

Системы с несколькими агентами могут быть организованы в различных шаблонах, которые определяют их взаимодействие:

  * **Последовательный**: Агенты работают в заранее определенном порядке, как на конвейере. Выход одного агента становится входом для следующего.
  * **Параллельный**: Агенты работают одновременно над разными частями задачи, а их результаты объединяются в конце.
  * **Условный**: Рабочий процесс следует разным путям в зависимости от результата работы агента, подобно конструкции if-then-else.

## 2\. Архитектура Workflow в Microsoft Agent Framework

Система Workflow в Agent Framework — это продвинутый механизм оркестрации, предназначенный для управления сложными взаимодействиями между несколькими агентами. Она построена на графовой архитектуре, использующей [Pregel-style execution model](https://kowshik.github.io/JPregel/pregel_paper.pdf), где обработка происходит в синхронизированных шагах, называемых "супершагами".

### Основные компоненты

Архитектура состоит из трех основных частей:

1.  **Исполнители**: Это основные единицы обработки. В наших примерах `Agent` является типом исполнителя. Каждый исполнитель может иметь несколько обработчиков сообщений, которые автоматически вызываются в зависимости от типа полученного сообщения.
2.  **Ребра**: Они определяют путь, по которому сообщения передаются между исполнителями. Ребра могут иметь условия, позволяя динамически маршрутизировать информацию через граф рабочего процесса.
3.  **Workflow**: Этот компонент управляет всем процессом, организуя исполнителей, ребра и общий поток выполнения. Он гарантирует, что сообщения обрабатываются в правильном порядке, и транслирует события для наблюдения.

*Диаграмма, иллюстрирующая основные компоненты системы Workflow.*

Эта структура позволяет создавать надежные и масштабируемые приложения, используя базовые шаблоны, такие как последовательные цепочки, fan-out/fan-in для параллельной обработки и логика switch-case для условных потоков.

## 3\. Практические примеры и анализ кода

Теперь давайте рассмотрим, как реализовать различные шаблоны рабочих процессов с использованием фреймворка. Мы изучим примеры кода на Python и .NET для каждого случая.

### Случай 1: Базовый последовательный рабочий процесс

Это самый простой шаблон, где выход одного агента передается напрямую другому. Наш сценарий включает агента `FrontDesk`, который делает рекомендацию по путешествию, а затем ее проверяет агент `Concierge`.

*Диаграмма базового рабочего процесса FrontDesk -\> Concierge.*

#### Сценарий

Путешественник спрашивает рекомендацию в Париже.

1.  Агент `FrontDesk`, ориентированный на краткость, предлагает посетить Лувр.
2.  Агент `Concierge`, который отдает предпочтение аутентичным впечатлениям, получает это предложение. Он проверяет рекомендацию и предлагает более локальную, менее туристическую альтернативу.

#### Анализ реализации на Python

В примере на Python мы сначала определяем и создаем двух агентов, каждый с конкретными инструкциями.

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

Затем используется `WorkflowBuilder` для построения графа. `front_desk_agent` устанавливается как начальная точка, и создается ребро для соединения его выхода с `reviewer_agent`.

```python
# 01.python-agent-framework-workflow-ghmodel-basic.ipynb

workflow = WorkflowBuilder().set_start_executor(front_desk_agent).add_edge(front_desk_agent, reviewer_agent).build()
```

Наконец, рабочий процесс выполняется с начальным запросом пользователя.

```python
# 01.python-agent-framework-workflow-ghmodel-basic.ipynb

result =''
# The run_stream method executes the workflow and streams events.
async for event in workflow.run_stream('I would like to go to Paris.'):
    if isinstance(event, WorkflowEvent):
        result += str(event.data)
```

#### Анализ реализации на .NET (C#)

Реализация на .NET следует аналогичной логике. Сначала определяются константы для имен агентов и их инструкций.

```csharp
// 01.dotnet-agent-framework-workflow-ghmodel-basic.ipynb

const string ReviewerAgentName = "Concierge";
const string ReviewerAgentInstructions = @"
    You are an are hotel concierge who has opinions about providing the most local and authentic experiences for travelers...";

const string FrontDeskAgentName = "FrontDesk";
const string FrontDeskAgentInstructions = @"""
    You are a Front Desk Travel Agent with ten years of experience and are known for brevity...";
```

Агенты создаются с использованием `OpenAIClient`, а затем `WorkflowBuilder` определяет последовательный поток, добавляя ребро от `frontDeskAgent` к `reviewerAgent`.

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

Рабочий процесс запускается с сообщением пользователя, а результаты транслируются обратно.

### Случай 2: Многошаговый последовательный рабочий процесс

Этот шаблон расширяет базовую последовательность, включая больше агентов. Он идеально подходит для процессов, требующих нескольких этапов уточнения или преобразования.

#### Сценарий

Пользователь предоставляет изображение гостиной и запрашивает оценку стоимости мебели.

1.  **Sales-Agent**: Определяет предметы мебели на изображении и создает список.
2.  **Price-Agent**: Берет список предметов и предоставляет подробный расчет стоимости, включая бюджетные, средние и премиум-опции.
3.  **Quote-Agent**: Получает список с ценами и форматирует его в официальный документ с предложением в Markdown.

*Диаграмма рабочего процесса Sales -\> Price -\> Quote.*

#### Анализ реализации на Python

Определяются три агента, каждый с специализированной ролью. Рабочий процесс строится с использованием `add_edge` для создания цепочки: `sales_agent` -\> `price_agent` -\> `quote_agent`.

```python
# 02.python-agent-framework-workflow-ghmodel-sequential.ipynb

# Create three specialized agents
sales_agent = chat_client.create_agent(...)
price_agent = chat_client.create_agent(...)
quote_agent = chat_client.create_agent(...)

# Build the sequential workflow
workflow = WorkflowBuilder().set_start_executor(sales_agent).add_edge(sales_agent, price_agent).add_edge(price_agent, quote_agent).build()
```

Входные данные — это `ChatMessage`, включающее текст и URI изображения. Фреймворк обрабатывает передачу выхода каждого агента следующему в последовательности, пока не будет создано окончательное предложение.

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

#### Анализ реализации на .NET (C#)

Пример на .NET повторяет версию на Python. Создаются три агента (`salesagent`, `priceagent`, `quoteagent`). `WorkflowBuilder` связывает их последовательно.

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

Сообщение пользователя создается с данными изображения (в виде байтов) и текстовым запросом. Метод `InProcessExecution.StreamAsync` инициирует рабочий процесс, а окончательный результат захватывается из потока.

### Случай 3: Параллельный рабочий процесс

Этот шаблон используется, когда задачи можно выполнять одновременно для экономии времени. Он включает "fan-out" для нескольких агентов и "fan-in" для агрегирования результатов.

#### Сценарий

Пользователь просит спланировать поездку в Сиэтл.

1.  **Dispatcher (Fan-Out)**: Запрос пользователя отправляется двум агентам одновременно.
2.  **Researcher-Agent**: Исследует достопримечательности, погоду и ключевые моменты для поездки в Сиэтл в декабре.
3.  **Plan-Agent**: Независимо создает подробный план поездки по дням.
4.  **Aggregator (Fan-In)**: Результаты от исследователя и планировщика собираются и представляются вместе как окончательный результат.

*Диаграмма параллельного рабочего процесса Researcher и Planner.*

#### Анализ реализации на Python

`ConcurrentBuilder` упрощает создание этого шаблона. Вы просто перечисляете участвующих агентов, и билдер автоматически создает необходимую логику fan-out и fan-in.

```python
# 03.python-agent-framework-workflow-ghmodel-concurrent.ipynb

research_agent = chat_client.create_agent(name="Researcher-Agent", ...)
plan_agent = chat_client.create_agent(name="Plan-Agent", ...)

# ConcurrentBuilder handles the fan-out/fan-in logic
workflow = ConcurrentBuilder().participants([research_agent, plan_agent]).build()

# Run the workflow
events = await workflow.run("Plan a trip to Seattle in December")
```

Фреймворк гарантирует, что `research_agent` и `plan_agent` выполняются параллельно, а их окончательные результаты собираются в список.

#### Анализ реализации на .NET (C#)

В .NET этот шаблон требует более явного определения. Создаются пользовательские исполнители (`ConcurrentStartExecutor` и `ConcurrentAggregationExecutor`) для обработки логики fan-out и fan-in.

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

`WorkflowBuilder` затем использует `AddFanOutEdge` и `AddFanInEdge` для построения графа с этими пользовательскими исполнителями и агентами.

```csharp
// 03.dotnet-agent-framework-workflow-ghmodel-concurrent.ipynb

var workflow = new WorkflowBuilder(startExecutor)
            .AddFanOutEdge(startExecutor, targets: [researcherAgent, plannerAgent])
            .AddFanInEdge(aggregationExecutor, sources: [researcherAgent, plannerAgent])
            .WithOutputFrom(aggregationExecutor)
            .Build();
```

### Случай 4: Условный рабочий процесс

Условные рабочие процессы вводят ветвление логики, позволяя системе выбирать разные пути на основе промежуточных результатов.

#### Сценарий

Этот рабочий процесс автоматизирует создание и публикацию технического учебника.

1.  **Evangelist-Agent**: Пишет черновик учебника на основе предоставленного плана и URL-адресов.
2.  **ContentReviewer-Agent**: Проверяет черновик. Он проверяет, превышает ли количество слов 200.
3.  **Условное ветвление**:
      * **Если одобрено (`Yes`)**: Рабочий процесс переходит к `Publisher-Agent`.
      * **Если отклонено (`No`)**: Рабочий процесс останавливается и выводит причину отклонения.
4.  **Publisher-Agent**: Если черновик одобрен, этот агент сохраняет контент в файл Markdown.

#### Анализ реализации на Python

В этом примере используется пользовательская функция `select_targets` для реализации условной логики. Эта функция передается в `add_multi_selection_edge_group` и направляет рабочий процесс на основе поля `review_result` из выхода рецензента.

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

Пользовательские исполнители, такие как `to_reviewer_result`, используются для анализа JSON-выхода агентов и преобразования его в строго типизированные объекты, которые может проверить функция выбора.

#### Анализ реализации на .NET (C#)

Версия на .NET использует аналогичный подход с функцией условия. Определяется `Func<object?, bool>` для проверки свойства `Result` объекта `ReviewResult`.

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

Параметр `condition` метода `AddEdge` позволяет `WorkflowBuilder` создать ветвление. Рабочий процесс будет следовать ребру к `publishExecutor`, только если условие `GetCondition(expectedResult: "Yes")` возвращает true. В противном случае он следует пути к `sendReviewerExecutor`.

## Заключение

Microsoft Agent Framework Workflow предоставляет надежную и гибкую основу для оркестрации сложных систем с несколькими агентами. Используя его графовую архитектуру и основные компоненты, разработчики могут проектировать и реализовывать сложные рабочие процессы как на Python, так и на .NET. Независимо от того, требуется ли вашему приложению простая последовательная обработка, параллельное выполнение или динамическая условная логика, фреймворк предлагает инструменты для создания мощных, масштабируемых и типобезопасных решений на основе ИИ.

---

**Отказ от ответственности**:  
Этот документ был переведен с использованием сервиса автоматического перевода [Co-op Translator](https://github.com/Azure/co-op-translator). Несмотря на наши усилия обеспечить точность, автоматические переводы могут содержать ошибки или неточности. Оригинальный документ на его родном языке следует считать авторитетным источником. Для получения критически важной информации рекомендуется профессиональный перевод человеком. Мы не несем ответственности за любые недоразумения или неправильные интерпретации, возникшие в результате использования данного перевода.