# Создание многозадачных приложений с использованием Microsoft Agent Framework Workflow

Это руководство поможет вам понять и создать многозадачные приложения с использованием Microsoft Agent Framework. Мы рассмотрим основные концепции многозадачных систем, погрузимся в архитектуру компонента Workflow этого фреймворка и пройдемся по практическим примерам как на Python, так и на .NET для различных шаблонов рабочих процессов.

## 1\. Понимание многозадачных систем

ИИ-Агент — это система, выходящая за рамки возможностей обычной большой языковой модели (LLM). Он может воспринимать окружение, принимать решения и предпринимать действия для достижения конкретных целей. Многозадачная система включает несколько таких агентов, которые совместно решают проблему, с которой одному агенту справиться было бы трудно или невозможно.

### Распространенные сценарии применения

  * **Решение сложных задач**: Разбиение большой задачи (например, планирование мероприятия на всю компанию) на более мелкие подзадачи, которые выполняют специализированные агенты (например, агент по бюджету, агент по логистике, маркетинговый агент).
  * **Виртуальные ассистенты**: Главный помощник-агент делегирует задачи, такие как планирование, исследование и бронирование, другим специализированным агентам.
  * **Автоматическое создание контента**: Рабочий процесс, где один агент создает черновик, другой проверяет его на точность и стиль, а третий публикует.

### Шаблоны многозадачности

Многозадачные системы могут быть организованы по нескольким шаблонам, которые определяют их взаимодействие:

  * **Последовательный**: Агенты работают в заранее определенном порядке, как на конвейере. Вывод одного агента становится вводом для следующего.
  * **Параллельный**: Агенты работают одновременно над разными частями задачи, а их результаты агрегируются в конце.
  * **Условный**: Рабочий процесс идет по разным путям в зависимости от результата агента, подобно конструкции if-then-else.

## 2\. Архитектура Workflow Microsoft Agent Framework

Система рабочих процессов Agent Framework — это усовершенствованный движок оркестровки, предназначенный для управления сложными взаимодействиями между несколькими агентами. Он построен на графовой архитектуре с использованием [модели выполнения в стиле Pregel](https://kowshik.github.io/JPregel/pregel_paper.pdf), где обработка происходит в синхронизированных шагах, называемых «супершагами».

### Основные компоненты

Архитектура состоит из трех основных частей:

1.  **Исполнители (Executors)**: Основные единицы обработки. В наших примерах `Agent` является типом исполнителя. Каждый исполнитель может иметь несколько обработчиков сообщений, которые автоматически вызываются в зависимости от типа полученного сообщения.
2.  **Ребра (Edges)**: Определяют пути, по которым сообщения передаются между исполнителями. Ребра могут иметь условия, позволяющие динамически маршрутизировать информацию по графу рабочего процесса.
3.  **Workflow**: Этот компонент управляет всем процессом, координируя исполнителей, ребра и общий поток выполнения. Он обеспечивает правильную последовательность обработки сообщений и транслирует события для наблюдаемости.

*Диаграмма, иллюстрирующая основные компоненты системы рабочего процесса.*

Такая структура позволяет создавать надежные и масштабируемые приложения, используя базовые шаблоны, такие как последовательные цепочки, fan-out/fan-in для параллельной обработки и логику switch-case для условных потоков.

## 3\. Практические примеры и анализ кода

Теперь давайте рассмотрим, как реализовать разные шаблоны рабочих процессов с помощью фреймворка. Мы посмотрим примеры кода как на Python, так и на .NET для каждого случая.

### Случай 1: Простейший последовательный рабочий процесс

Это самый простой шаблон, в котором вывод одного агента напрямую передается другому. В нашем сценарии агент отеля `FrontDesk` делает туристическую рекомендацию, которую затем проверяет агент `Concierge`.

*Диаграмма базового рабочего процесса FrontDesk -> Concierge.*

#### Предыстория сценария

Путешественник запрашивает рекомендацию для Парижа.

1.  Агент `FrontDesk`, настроенный на краткость, предлагает посетить Лувр.
2.  Агент `Concierge`, который ценит аутентичный опыт, получает предложение. Он проверяет рекомендацию и предлагает альтернативу, более ориентированную на местных жителей, а не на туристов.

#### Анализ реализации на Python

В примере на Python сначала определяются и создаются два агента, каждый с конкретными инструкциями.

```python
# 01.python-agent-framework-workflow-ghmodel-basic.ipynb

# Определить роли агентов и инструкции
REVIEWER_NAME = "Concierge"
REVIEWER_INSTRUCTIONS = """
    You are a hotel concierge who has opinions about providing the most local and authentic experiences for travelers...
    """

FRONTDESK_NAME = "FrontDesk"
FRONTDESK_INSTRUCTIONS = """
    You are a Front Desk Travel Agent with ten years of experience and are known for brevity...
    """

# Создать экземпляры агентов
reviewer_agent = chat_client.as_agent(
    instructions=(REVIEWER_INSTRUCTIONS),
    name=REVIEWER_NAME,
)

front_desk_agent = chat_client.as_agent(
    instructions=(FRONTDESK_INSTRUCTIONS),
    name=FRONTDESK_NAME,
)
```

Затем с помощью `WorkflowBuilder` строится граф. Агент `front_desk_agent` установлен в качестве стартового, создается ребро, соединяющее его вывод с `reviewer_agent`.

```python
# 01.python-agent-framework-workflow-ghmodel-basic.ipynb

workflow = WorkflowBuilder(start_executor=front_desk_agent).add_edge(front_desk_agent, reviewer_agent).build()
```

Наконец, рабочий процесс запускается с начальным пользовательским запросом.

```python
# 01.python-agent-framework-workflow-ghmodel-basic.ipynb

result =''
# run выполняет рабочий процесс; get_outputs() возвращает результат выполнения исполнителя.
events = await workflow.run('I would like to go to Paris.')
outputs = events.get_outputs()
result = outputs[0].text if outputs else ''
```

#### Анализ реализации на .NET (C\#)

Реализация на .NET имеет очень похожую логику. Сначала задаются константы для имен и инструкций агентов.

```csharp
// 01.dotnet-agent-framework-workflow-ghmodel-basic.ipynb

const string ReviewerAgentName = "Concierge";
const string ReviewerAgentInstructions = @"
    You are a hotel concierge who has opinions about providing the most local and authentic experiences for travelers...";

const string FrontDeskAgentName = "FrontDesk";
const string FrontDeskAgentInstructions = @"""
    You are a Front Desk Travel Agent with ten years of experience and are known for brevity...";
```

Затем агенты создаются с помощью `AzureOpenAIClient` (Responses API), а `WorkflowBuilder` определяет последовательный поток, добавляя ребро от `frontDeskAgent` к `reviewerAgent`.

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

Рабочий процесс запускается с сообщением пользователя, и результаты передаются обратно потоковым способом.

### Случай 2: Многошаговый последовательный рабочий процесс

Этот шаблон расширяет базовую последовательность, добавляя больше агентов. Он идеален для процессов, требующих нескольких этапов уточнения или преобразования.

#### Предыстория сценария

Пользователь предоставляет изображение гостиной и запрашивает коммерческое предложение на мебель.

1.  **Sales-Agent**: Определяет предметы мебели на изображении и формирует список.
2.  **Price-Agent**: Принимает список и предоставляет подробное ценовое предложение с бюджетными, средними и премиальными вариантами.
3.  **Quote-Agent**: Получает оцененный список и форматирует его в официальный документ предложения в формате Markdown.

*Диаграмма рабочего процесса Sales -> Price -> Quote.*

#### Анализ реализации на Python

Определены три агента с конкретными ролями. Рабочий процесс строится с помощью `add_edge`, создавая цепочку: `sales_agent` -> `price_agent` -> `quote_agent`.

```python
# 02.python-agent-framework-workflow-ghmodel-sequential.ipynb

# Создайте три специализированных агента
sales_agent = chat_client.as_agent(...)
price_agent = chat_client.as_agent(...)
quote_agent = chat_client.as_agent(...)

# Постройте последовательный рабочий процесс
workflow = WorkflowBuilder(start_executor=sales_agent).add_edge(sales_agent, price_agent).add_edge(price_agent, quote_agent).build()
```

Входом является `ChatMessage`, содержащий как текст, так и URI изображения. Фреймворк обеспечивает передачу вывода каждого агента следующему, пока не будет сформировано окончательное предложение.

```python
# 02.python-agent-framework-workflow-ghmodel-sequential.ipynb

# Сообщение пользователя содержит как текст, так и изображение
message = ChatMessage(
        role=Role.USER,
        contents=[
            TextContent(text="Please find the relevant furniture..."),
            DataContent(uri=image_uri, media_type="image/png")
        ]
)

# Запустить рабочий процесс
events = await workflow.run(message)
```

#### Анализ реализации на .NET (C\#)

Пример на .NET повторяет Python-версию. Создаются три агента (`salesagent`, `priceagent`, `quoteagent`). `WorkflowBuilder` связывает их последовательно.

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

Сообщение пользователя формируется с данными изображения (в виде байтов) и текстовым запросом. Метод `InProcessExecution.RunStreamingAsync` запускает рабочий процесс, а итоговый вывод считывается из потока.

### Случай 3: Параллельный рабочий процесс

Этот шаблон используется, когда задачи можно выполнять одновременно для экономии времени. Он включает в себя «fan-out» к нескольким агентам и «fan-in» для агрегирования результатов.

#### Предыстория сценария

Пользователь просит спланировать поездку в Сиэтл.

1.  **Dispatcher (Fan-Out)**: Запрос пользователя одновременно отправляется двум агентам.
2.  **Researcher-Agent**: Исследует достопримечательности, погоду и ключевые условия поездки в Сиэтл в декабре.
3.  **Plan-Agent**: Независимо создает подробный по дням маршрут путешествия.
4.  **Aggregator (Fan-In)**: Полученные результаты от исследователя и планировщика собираются и представляются вместе как итоговый результат.

*Диаграмма параллельного рабочего процесса с Researcher и Planner.*

#### Анализ реализации на Python

`ConcurrentBuilder` упрощает создание такого шаблона. Вы просто перечисляете агентов, а билдер автоматически создает необходимую логику fan-out и fan-in.

```python
# 03.python-agent-framework-workflow-ghmodel-concurrent.ipynb

research_agent = chat_client.as_agent(name="Researcher-Agent", ...)
plan_agent = chat_client.as_agent(name="Plan-Agent", ...)

# ConcurrentBuilder обрабатывает логику расширения/объединения
workflow = ConcurrentBuilder().participants([research_agent, plan_agent]).build()

# Запустить рабочий процесс
events = await workflow.run("Plan a trip to Seattle in December")
```

Фреймворк гарантирует, что `research_agent` и `plan_agent` выполняются параллельно, а их итоговые выводы собираются в список.

#### Анализ реализации на .NET (C\#)

В .NET этот шаблон требует более явного определения. Создаются специальные исполнители (`ConcurrentStartExecutor` и `ConcurrentAggregationExecutor`) для обработки логики fan-out и fan-in.

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

Затем `WorkflowBuilder` использует `AddFanOutEdge` и `AddFanInEdge` для построения графа с этими кастомными исполнителями и агентами.

```csharp
// 03.dotnet-agent-framework-workflow-ghmodel-concurrent.ipynb

var workflow = new WorkflowBuilder(startExecutor)
            .AddFanOutEdge(startExecutor, targets: [researcherAgent, plannerAgent])
            .AddFanInEdge(aggregationExecutor, sources: [researcherAgent, plannerAgent])
            .WithOutputFrom(aggregationExecutor)
            .Build();
```

### Случай 4: Условный рабочий процесс

Условные рабочие процессы вводят ветвление логики, позволяя системе выбирать различные пути в зависимости от промежуточных результатов.

#### Предыстория сценария

Этот рабочий процесс автоматизирует создание и публикацию технического руководства.

1.  **Evangelist-Agent**: Пишет черновик руководства на основе заданного плана и URL-адресов.
2.  **ContentReviewer-Agent**: Проверяет черновик. Оценивает, что количество слов превышает 200.
3.  **Условная ветвь**:
      * **Если одобрено (`Да`)**: Рабочий процесс переходит к `Publisher-Agent`.
      * **Если отклонено (`Нет`)**: Рабочий процесс останавливается и выводит причину отклонения.
4.  **Publisher-Agent**: Если черновик одобрен, этот агент сохраняет содержимое в файл Markdown.

#### Анализ реализации на Python

В этом примере используется пользовательская функция `select_targets`, реализующая условную логику. Она передается в `add_multi_selection_edge_group` и управляет маршрутом рабочего процесса на основе поля `review_result` из вывода рецензента.

```python
# 04.python-agent-framework-workflow-aifoundry-condition.ipynb

# Эта функция определяет следующий шаг на основе результата проверки
def select_targets(review: ReviewResult, target_ids: list[str]) -> list[str]:
    handle_review_id, save_draft_id = target_ids
    if review.review_result == "Yes":
        # Если одобрено, перейти к исполнителю 'save_draft'
        return [save_draft_id]
    else:
        # Если отклонено, перейти к исполнителю 'handle_review' для сообщения о неудаче
        return [handle_review_id]

# Конструктор рабочего процесса использует функцию выбора для маршрутизации
workflow = (
    WorkflowBuilder()
        .set_start_executor(evangelist_agent)
        .add_edge(evangelist_agent, reviewer_agent)
        .add_edge(reviewer_agent, to_reviewer_result)
        # Многоадресный переход реализует условную логику
        .add_multi_selection_edge_group(
            to_reviewer_result,
            [handle_review, save_draft],
            selection_func=select_targets,
        )
        .add_edge(save_draft, publisher_agent)
        .build()
)
```

Пользовательские исполнители, такие как `to_reviewer_result`, используются для парсинга JSON-вывода агентов и преобразования его в строго типизированные объекты, которые может анализировать функция выбора.

#### Анализ реализации на .NET (C\#)

Версия на .NET использует похожий подход с функцией условия. Определена `Func<object?, bool>`, проверяющая свойство `Result` объекта `ReviewResult`.

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

Параметр `condition` метода `AddEdge` позволяет `WorkflowBuilder` создать ветвящийся путь. Рабочий процесс пойдет по ребру к `publishExecutor` только если условие `GetCondition(expectedResult: "Yes")` возвращает true. Иначе он пойдет по пути к `sendReviewerExecutor`.

## Заключение

Microsoft Agent Framework Workflow предоставляет надежную и гибкую основу для оркестровки сложных многозадачных систем. Используя графовую архитектуру и основные компоненты, разработчики могут проектировать и реализовывать сложные рабочие процессы как на Python, так и на .NET. Будь то простая последовательная обработка, параллельное выполнение или динамическая условная логика, фреймворк предлагает инструменты для создания мощных, масштабируемых и типобезопасных решений с искусственным интеллектом.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Отказ от ответственности**:
Этот документ был переведен с использованием сервиса машинного перевода [Co-op Translator](https://github.com/Azure/co-op-translator). Несмотря на наши усилия по обеспечению точности, имейте в виду, что автоматический перевод может содержать ошибки или неточности. Оригинальный документ на его исходном языке следует считать авторитетным источником. Для получения критически важной информации рекомендуется обратиться к профессиональному человеческому переводу. Мы не несем ответственности за любые недоразумения или неправильные толкования, возникшие в результате использования этого перевода.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->