# Изградња апликација са више агената уз Microsoft Agent Framework Workflow

Овај туторијал ће вас водити кроз разумевање и изградњу апликација са више агената користећи Microsoft Agent Framework. Истражићемо основне концепте система са више агената, дубље ући у архитектуру Workflow компонента оквира и проћи кроз практичне примере у Python-у и .NET-у за различите шаблоне радних токова.

## 1\. Разумевање система са више агената

АИ агент је систем који превазилази могућности стандардног модела великог језика (LLM). Он може да перципира своје окружење, доноси одлуке и предузима акције како би постигао одређене циљеве. Систем са више агената укључује неколико ових агената који сарађују како би решили проблем који би био тежак или немогућ за једног агента.

### Уобичајени сценарији примене

  * **Решавање сложених проблема**: Разбијање великог задатка (нпр. планирање догађаја на нивоу компаније) на мање подзадатке које обрађују специјализовани агенти (нпр. агент за буџет, агент за логистику, агент за маркетинг).
  * **Виртуелни асистенти**: Примарни агент асистент делегира задатке као што су заказивање, истраживање и резервације другим специјализованим агентима.
  * **Аутоматизовано креирање садржаја**: Радни ток где један агент пише нацрт садржаја, други га прегледа ради тачности и тона, а трећи га објављује.

### Шаблони система са више агената

Системи са више агената могу бити организовани у неколико шаблона који одређују како они међусобно интерагују:

  * **Секвенцијално**: Агенти раде у унапред дефинисаном редоследу, као на производној линији. Излаз једног агента постаје улаз за следећег.
  * **Паралелно**: Агенти раде истовремено на различитим деловима задатка, а њихови резултати се агрегирају на крају.
  * **Условно**: Радни ток прати различите путеве на основу излаза агента, слично if-then-else изјави.

## 2\. Архитектура Workflow компонента Microsoft Agent Framework-а

Систем радног тока оквира агента је напредни оркестрациони мотор дизајниран за управљање сложеним интеракцијама између више агената. Заснован је на архитектури заснованој на графу која користи [Pregel-style модел извршења](https://kowshik.github.io/JPregel/pregel_paper.pdf), где се обрада одвија у синхронизованим корацима названим "supersteps".

### Основне компоненте

Архитектура се састоји од три главна дела:

1.  **Извршиоци**: Основне јединице за обраду. У нашим примерима, `Agent` је тип извршиоца. Сваки извршилац може имати више обрађивача порука који се аутоматски позивају на основу типа примљене поруке.
2.  **Ивице**: Оне дефинишу пут којим поруке пролазе између извршилаца. Ивице могу имати услове, омогућавајући динамичко усмеравање информација кроз граф радног тока.
3.  **Workflow**: Ова компонента оркестрира цео процес, управља извршиоцима, ивицама и целокупним током извршења. Она осигурава да се поруке обрађују у исправном редоследу и стримује догађаје ради посматрања.

*Дијаграм који илуструје основне компоненте система радног тока.*

Ова структура омогућава изградњу робусних и скалабилних апликација користећи основне шаблоне као што су секвенцијални ланци, fan-out/fan-in за паралелну обраду и switch-case логика за условне токове.

## 3\. Практични примери и анализа кода

Сада ћемо истражити како имплементирати различите шаблоне радних токова користећи оквир. Погледаћемо Python и .NET код за сваки пример.

### Случај 1: Основни секвенцијални радни ток

Ово је најједноставнији шаблон, где се излаз једног агента директно прослеђује другом. Наш сценарио укључује хотелског агента `FrontDesk` који даје препоруку за путовање, коју затим прегледа агент `Concierge`.

*Дијаграм основног FrontDesk -\> Concierge радног тока.*

#### Позадина сценарија

Путник тражи препоруку за Париз.

1.  Агент `FrontDesk`, дизајниран за кратке одговоре, предлаже посету музеју Лувр.
2.  Агент `Concierge`, који приоритет даје аутентичним искуствима, прима овај предлог. Он прегледа препоруку и даје повратну информацију, предлажући локалну, мање туристичку алтернативу.

#### Анализа имплементације у Python-у

У Python примеру, прво дефинишемо и креирамо два агента, сваки са специфичним упутствима.

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

Затим се користи `WorkflowBuilder` за конструисање графа. `front_desk_agent` се поставља као почетна тачка, а креира се ивица која повезује његов излаз са `reviewer_agent`.

```python
# 01.python-agent-framework-workflow-ghmodel-basic.ipynb

workflow = WorkflowBuilder().set_start_executor(front_desk_agent).add_edge(front_desk_agent, reviewer_agent).build()
```

На крају, радни ток се извршава са почетним упитом корисника.

```python
# 01.python-agent-framework-workflow-ghmodel-basic.ipynb

result =''
# The run_stream method executes the workflow and streams events.
async for event in workflow.run_stream('I would like to go to Paris.'):
    if isinstance(event, WorkflowEvent):
        result += str(event.data)
```

#### Анализа имплементације у .NET (C#)

Имплементација у .NET-у прати веома сличну логику. Прво се дефинишу константе за имена и упутства агената.

```csharp
// 01.dotnet-agent-framework-workflow-ghmodel-basic.ipynb

const string ReviewerAgentName = "Concierge";
const string ReviewerAgentInstructions = @"
    You are an are hotel concierge who has opinions about providing the most local and authentic experiences for travelers...";

const string FrontDeskAgentName = "FrontDesk";
const string FrontDeskAgentInstructions = @"""
    You are a Front Desk Travel Agent with ten years of experience and are known for brevity...";
```

Агенти се креирају користећи `OpenAIClient`, а затим `WorkflowBuilder` дефинише секвенцијални ток додавањем ивице од `frontDeskAgent` до `reviewerAgent`.

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

Радни ток се затим покреће са поруком корисника, а резултати се стримују назад.

### Случај 2: Секвенцијални радни ток са више корака

Овај шаблон проширује основну секвенцу да укључи више агената. Идеалан је за процесе који захтевају више фаза рафинирања или трансформације.

#### Позадина сценарија

Корисник доставља слику дневне собе и тражи понуду за намештај.

1.  **Sales-Agent**: Идентификује ставке намештаја на слици и креира листу.
2.  **Price-Agent**: Узима листу ставки и пружа детаљан ценовник, укључујући опције за буџет, средњи и премијум сегмент.
3.  **Quote-Agent**: Прима листу са ценама и форматира је у формалну понуду у Markdown-у.

*Дијаграм Sales -\> Price -\> Quote радног тока.*

#### Анализа имплементације у Python-у

Три агента су дефинисана, сваки са специјализованом улогом. Радни ток се конструише користећи `add_edge` за креирање ланца: `sales_agent` -\> `price_agent` -\> `quote_agent`.

```python
# 02.python-agent-framework-workflow-ghmodel-sequential.ipynb

# Create three specialized agents
sales_agent = chat_client.create_agent(...)
price_agent = chat_client.create_agent(...)
quote_agent = chat_client.create_agent(...)

# Build the sequential workflow
workflow = WorkflowBuilder().set_start_executor(sales_agent).add_edge(sales_agent, price_agent).add_edge(price_agent, quote_agent).build()
```

Улаз је `ChatMessage` који укључује текст и URI слике. Оквир обрађује прослеђивање излаза сваког агента следећем у секвенци све док се не генерише финална понуда.

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

#### Анализа имплементације у .NET (C#)

.NET пример одражава Python верзију. Три агента (`salesagent`, `priceagent`, `quoteagent`) су креирана. `WorkflowBuilder` их повезује секвенцијално.

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

Порука корисника се конструише са подацима о слици (као бајтовима) и текстуалним упитом. `InProcessExecution.StreamAsync` метода покреће радни ток, а финални излаз се хвата из стрима.

### Случај 3: Паралелни радни ток

Овај шаблон се користи када се задаци могу извршавати истовремено ради уштеде времена. Укључује "fan-out" ка више агената и "fan-in" за агрегирање резултата.

#### Позадина сценарија

Корисник тражи планирање путовања у Сијетл.

1.  **Dispatcher (Fan-Out)**: Захтев корисника се шаље двојици агената истовремено.
2.  **Researcher-Agent**: Истражује атракције, временске услове и кључне аспекте путовања у Сијетл у децембру.
3.  **Plan-Agent**: Независно креира детаљан дневни план путовања.
4.  **Aggregator (Fan-In)**: Излази истраживача и планера се прикупљају и представљају заједно као финални резултат.

*Дијаграм паралелног Researcher и Planner радног тока.*

#### Анализа имплементације у Python-у

`ConcurrentBuilder` поједностављује креирање овог шаблона. Само наведете учеснике, а градитељ аутоматски креира потребну fan-out и fan-in логику.

```python
# 03.python-agent-framework-workflow-ghmodel-concurrent.ipynb

research_agent = chat_client.create_agent(name="Researcher-Agent", ...)
plan_agent = chat_client.create_agent(name="Plan-Agent", ...)

# ConcurrentBuilder handles the fan-out/fan-in logic
workflow = ConcurrentBuilder().participants([research_agent, plan_agent]).build()

# Run the workflow
events = await workflow.run("Plan a trip to Seattle in December")
```

Оквир осигурава да `research_agent` и `plan_agent` извршавају паралелно, а њихови финални излази се прикупљају у листу.

#### Анализа имплементације у .NET (C#)

У .NET-у, овај шаблон захтева експлицитнију дефиницију. Прилагођени извршиоци (`ConcurrentStartExecutor` и `ConcurrentAggregationExecutor`) се креирају за обраду fan-out и fan-in логике.

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

`WorkflowBuilder` затим користи `AddFanOutEdge` и `AddFanInEdge` за конструисање графа са овим прилагођеним извршиоцима и агентима.

```csharp
// 03.dotnet-agent-framework-workflow-ghmodel-concurrent.ipynb

var workflow = new WorkflowBuilder(startExecutor)
            .AddFanOutEdge(startExecutor, targets: [researcherAgent, plannerAgent])
            .AddFanInEdge(aggregationExecutor, sources: [researcherAgent, plannerAgent])
            .WithOutputFrom(aggregationExecutor)
            .Build();
```

### Случај 4: Условни радни ток

Условни радни токови уводе логичко гранање, омогућавајући систему да прати различите путеве на основу међурезултата.

#### Позадина сценарија

Овај радни ток аутоматизује креирање и објављивање техничког туторијала.

1.  **Evangelist-Agent**: Пише нацрт туторијала на основу датог оквира и URL-ова.
2.  **ContentReviewer-Agent**: Прегледа нацрт. Проверава да ли је број речи већи од 200.
3.  **Условно гранање**:
      * **Ако је одобрено (`Yes`)**: Радни ток се наставља ка `Publisher-Agent`.
      * **Ако је одбијено (`No`)**: Радни ток се зауставља и излази разлог одбијања.
4.  **Publisher-Agent**: Ако је нацрт одобрен, овај агент чува садржај у Markdown фајлу.

#### Анализа имплементације у Python-у

Овај пример користи прилагођену функцију, `select_targets`, за имплементацију условне логике. Ова функција се прослеђује `add_multi_selection_edge_group` и усмерава радни ток на основу поља `review_result` из излаза рецензента.

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

Прилагођени извршиоци као `to_reviewer_result` се користе за парсирање JSON излаза агената и конвертовање у јако типизоване објекте које функција селекције може да анализира.

#### Анализа имплементације у .NET (C#)

.NET верзија користи сличан приступ са функцијом услова. `Func<object?, bool>` је дефинисан за проверу својства `Result` објекта `ReviewResult`.

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

Параметар `condition` методе `AddEdge` омогућава `WorkflowBuilder`-у да креира гранајући пут. Радни ток ће пратити ивицу ка `publishExecutor` само ако услов `GetCondition(expectedResult: "Yes")` врати true. У супротном, прати пут ка `sendReviewerExecutor`.

## Закључак

Microsoft Agent Framework Workflow пружа робусну и флексибилну основу за оркестрацију сложених система са више агената. Користећи његову архитектуру засновану на графу и основне компоненте, програмери могу дизајнирати и имплементирати софистициране радне токове у Python-у и .NET-у. Без обзира да ли ваша апликација захтева једноставну секвенцијалну обраду, паралелно извршење или динамичку условну логику, оквир нуди алате за изградњу моћних, скалабилних и типизованих решења заснованих на АИ.

---

**Одрицање од одговорности**:  
Овај документ је преведен коришћењем услуге за превођење помоћу вештачке интелигенције [Co-op Translator](https://github.com/Azure/co-op-translator). Иако се трудимо да обезбедимо тачност, молимо вас да имате у виду да аутоматски преводи могу садржати грешке или нетачности. Оригинални документ на његовом изворном језику треба сматрати ауторитативним извором. За критичне информације препоручује се професионални превод од стране људи. Не преузимамо одговорност за било каква погрешна тумачења или неспоразуме који могу произаћи из коришћења овог превода.