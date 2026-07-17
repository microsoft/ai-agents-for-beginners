# Прављење мулти-агентских апликација са Microsoft Agent Framework Workflow-ом

Овај туторијал ће вас провести кроз разумевање и изградњу мулти-агентских апликација користећи Microsoft Agent Framework. Истражићемо основне концепте мулти-агентских система, упознати се са архитектуром Workflow компонененте фрејмворка и проћи кроз практичне примере у Python-у и .NET-у за различите обрасце токова рада.

## 1\. Разумевање мулти-агентских система

AI агент је систем који превазилази могућности стандардног Large Language Model-а (LLM). Он може перципирати своје окружење, доносити одлуке и предузимати акције да би постигао специфичне циљеве. Мулти-агентски систем укључује више оваквих агената који сарађују да реше проблем који би био тежак или немогућ једном агенту самостално.

### Уобичајени сценарији примене

  * **Решавање сложених проблема**: Разлагање великог задатка (нпр. планирање догађаја за целу компанију) на мање подзадатке које обрађују специјализовани агенти (нпр. агент за буџет, агент за логистику, агент за маркетинг).
  * **Виртуелни асистенти**: Примарни асистент агент који делегира задатке као што су заказивање, истраживање и резервација другим специјализованим агентима.
  * **Аутоматска креирања садржаја**: Радни ток у којем један агент саставља нацрт садржаја, други га прегледа по тачности и тону, а трећи објављује.

### Обрасци мулти-агентских система

Мулти-агентски системи могу бити организовани у више образаца који одређују како агенти комуницирају:

  * **Секвенцијални**: Агенти раде у унапред дефинисаном редоследу, као на монтажној траци. Излаз једног агента постаје улаз за следећег.
  * **Паралелни**: Агенти раде истовремено на различитим деловима задатка, а резултати се на крају агрегирају.
  * **Условни**: Ток рада прати различите путање засноване на излазу агента, слично као if-then-else израз.

## 2\. Архитектура Microsoft Agent Framework Workflow-а

Систем тока рада у Agent Framework-у је напредни мотор за оркестрацију дизајниран да управља сложеним интеракцијама између више агената. Заснован је на графској архитектури која користи [Pregel-style execution model](https://kowshik.github.io/JPregel/pregel_paper.pdf), где обрада тече у синхронизованим корацима названим „supersteps“.

### Основне компоненте

Архитектура се састоји од три главна дела:

1.  **Извршиоци (Executors)**: Ово су основне јединице обраде. У нашим примерима, `Agent` је тип извршиоца. Сваки извршилац може имати више обрада порука који се аутоматски позивају на основу типа примљене поруке.
2.  **Ивице (Edges)**: Оне дефинишу путању коју поруке следе између извршилаца. Ивице могу имати услове, омогућавајући динамичко усмеравање информација кроз граф тока рада.
3.  **Workflow**: Ова компонента оркестрира цео процес, управљајући извршиоцима, ивицама и укупним током извршења. Обезбеђује да се поруке обрађују у исправном редоследу и емитује догађаје ради посматрања.

*Дијаграм који илуструје основне компоненте система тока рада.*

Ова структура омогућава прављење робусних и скалабилних апликација користећи основне обрасце као што су секвенцијални ланци, фан-аути/фан-инови за паралелну обраду, као и switch-case логику за условне токове.

## 3\. Практични примери и анализа кода

Сада ћемо истражити како имплементирати различите обрасце тока рада користећи овај фрејмворк. Погледаћемо примерe и у Python-у и у .NET-у за сваки случај.

### Случај 1: Основни секвенцијални ток рада

Ово је најједноставнији образац у којем се излаз једног агента директно прослеђује другом. Наш сценарио укључује хотелског агента `FrontDesk` који даје препоруку за путовање, коју затим прегледа агент `Concierge`.

*Дијаграм основног FrontDesk -> Concierge тока рада.*

#### Позадина сценарија

Путник тражи препоруку за Париз.

1.  Агент `FrontDesk`, дизајниран за концизност, предлаже посету Лувру.
2.  Агент `Concierge`, који придаје значај аутентичним искуствима, прегледа ову препоруку и даје повратну информацију, предлажући локалнију, мање туристичку алтернативу.

#### Анализа Python имплементације

У Python примеру најпре дефинишемо и креирамо два агента, сваки са својим специфичним инструкцијама.

```python
# 01.python-agent-framework-workflow-ghmodel-basic.ipynb

# Дефинишите улоге агената и упутства
REVIEWER_NAME = "Concierge"
REVIEWER_INSTRUCTIONS = """
    You are a hotel concierge who has opinions about providing the most local and authentic experiences for travelers...
    """

FRONTDESK_NAME = "FrontDesk"
FRONTDESK_INSTRUCTIONS = """
    You are a Front Desk Travel Agent with ten years of experience and are known for brevity...
    """

# Креирајте инстанце агената
reviewer_agent = chat_client.as_agent(
    instructions=(REVIEWER_INSTRUCTIONS),
    name=REVIEWER_NAME,
)

front_desk_agent = chat_client.as_agent(
    instructions=(FRONTDESK_INSTRUCTIONS),
    name=FRONTDESK_NAME,
)
```

Затим користимо `WorkflowBuilder` за конструисање графа. `front_desk_agent` је почетна тачка, и креира се ивица која повезује његов излаз са `reviewer_agent`.

```python
# 01.python-agent-framework-radni-proces-ghmodel-osnovni.ipynb

workflow = WorkflowBuilder(start_executor=front_desk_agent).add_edge(front_desk_agent, reviewer_agent).build()
```

На крају, ток рада се извршава са почетним корисничким упитом.

```python
# 01.python-agent-framework-workflow-ghmodel-basic.ipynb

result =''
# run извршава ток рада; get_outputs() враћа резултат извршиоца излаза.
events = await workflow.run('I would like to go to Paris.')
outputs = events.get_outputs()
result = outputs[0].text if outputs else ''
```

#### Анализа .NET (C#) имплементације

.NET имплементација прати сличну логику. Прво су дефинисане константе за имена и инструкције агената.

```csharp
// 01.dotnet-agent-framework-workflow-ghmodel-basic.ipynb

const string ReviewerAgentName = "Concierge";
const string ReviewerAgentInstructions = @"
    You are a hotel concierge who has opinions about providing the most local and authentic experiences for travelers...";

const string FrontDeskAgentName = "FrontDesk";
const string FrontDeskAgentInstructions = @"""
    You are a Front Desk Travel Agent with ten years of experience and are known for brevity...";
```

Агенти се креирају коришћењем `AzureOpenAIClient` (Responses API), а затим `WorkflowBuilder` дефинише секвенцијални ток додавањем ивице између `frontDeskAgent` и `reviewerAgent`.

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

Ток рада се покреће уз корисничку поруку, а резултати се емитују у реалном времену.

### Случај 2: Мулти-степени секвенцијални ток рада

Овај образац проширује основну секвенцу да укључи више агената. Идеалан је за процес који захтева неколико фаза прецизирања или трансформације.

#### Позадина сценарија

Корисник доставља слику дневне собе и тражи понуду за намештај.

1.  **Агент продаје**: Идентификује намештај на слици и прави листу.
2.  **Агент за цену**: Прима листу и даје детаљан преглед цена укључујући буџетске, средње и премијум опције.
3.  **Агент за понуде**: Прима оцењену листу и форматира је у формални понудни документ у Markdown формату.

*Дијаграм тока рада Sales -> Price -> Quote.*

#### Анализа Python имплементације

Дефинисано је три агента са специјализованим улогама. Ток рада је конструисан коришћењем `add_edge` да би се направио ланац: `sales_agent` -> `price_agent` -> `quote_agent`.

```python
# 02.python-agent-framework-workflow-ghmodel-sequential.ipynb

# Направите три специјализована агента
sales_agent = chat_client.as_agent(...)
price_agent = chat_client.as_agent(...)
quote_agent = chat_client.as_agent(...)

# Направите секвенцијални радни ток
workflow = WorkflowBuilder(start_executor=sales_agent).add_edge(sales_agent, price_agent).add_edge(price_agent, quote_agent).build()
```

Улаз је `ChatMessage` који садржи текст и URI слике. Фрејмворк управља прослеђивањем излаза сваког агента следећем у низу док се не генерише коначна понуда.

```python
# 02.python-agent-framework-workflow-ghmodel-sequential.ipynb

# Корисничка порука садржи и текст и слику
message = ChatMessage(
        role=Role.USER,
        contents=[
            TextContent(text="Please find the relevant furniture..."),
            DataContent(uri=image_uri, media_type="image/png")
        ]
)

# Покрени ток рада
events = await workflow.run(message)
```

#### Анализа .NET (C#) имплементације

.NET пример одражава Python верзију. Креирани су три агента (`salesagent`, `priceagent`, `quoteagent`). `WorkflowBuilder` их повезује секвенцијално.

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

Корисничка порука садржи податке о слици (у бајтовима) и текстуални упит. `InProcessExecution.RunStreamingAsync` покреће ток рада, а коначни излаз се хвата са стрима.

### Случај 3: Паралелни ток рада

Овај образац се користи када се задаци могу извршавати истовремено ради уштеде времена. Обухвата „fan-out“ ка више агената и „fan-in“ за агрегирање резултата.

#### Позадина сценарија

Корисник тражи да испланира путовање у Сијетл.

1.  **Диспетчер (Fan-Out)**: Кориснички захтев се истовремено шаље двојици агената.
2.  **Агент за истраживање**: Истражује атракције, време и кључне аспекте путовања у Сијетл у децембру.
3.  **Агент за план**: Самостално креира детаљни дневни план путовања.
4.  **Агент за агрегирање (Fan-In)**: Резултати истраживача и планирача се прикупљају и приказују заједно као коначни резултат.

*Дијаграм паралелног тока рада Researcher и Planner агената.*

#### Анализа Python имплементације

`ConcurrentBuilder` поједностављује креирање овог образаца. Једноставно наведете учесничке агенте, а билдера аутоматски прави fan-out и fan-in логику.

```python
# 03.python-agent-framework-workflow-ghmodel-concurrent.ipynb

research_agent = chat_client.as_agent(name="Researcher-Agent", ...)
plan_agent = chat_client.as_agent(name="Plan-Agent", ...)

# ConcurrentBuilder управља логиком разгранавања и спајања
workflow = ConcurrentBuilder().participants([research_agent, plan_agent]).build()

# Покрени ток рада
events = await workflow.run("Plan a trip to Seattle in December")
```

Фрејмворк обезбеђује да `research_agent` и `plan_agent` истовремено извршавају задатке, а њихови коначни излази се прикупљају у листу.

#### Анализа .NET (C#) имплементације

У .NET-у овај образац захтева експлицитнију дефиницију. Креирани су прилагођени извршиоци (`ConcurrentStartExecutor` и `ConcurrentAggregationExecutor`) који обрађују fan-out и fan-in логику.

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

`WorkflowBuilder` користи `AddFanOutEdge` и `AddFanInEdge` за конструисање графа са овим прилагођеним извршиоцима и агентима.

```csharp
// 03.dotnet-agent-framework-workflow-ghmodel-concurrent.ipynb

var workflow = new WorkflowBuilder(startExecutor)
            .AddFanOutEdge(startExecutor, targets: [researcherAgent, plannerAgent])
            .AddFanInEdge(aggregationExecutor, sources: [researcherAgent, plannerAgent])
            .WithOutputFrom(aggregationExecutor)
            .Build();
```

### Случај 4: Условни ток рада

Условни токови рада уводе разгранату логику, омогућавајући систему да изабере различите путеве на основу резултата у току извршења.

#### Позадина сценарија

Овај ток рада аутоматизује креирање и објављивање техничког туторијала.

1.  **Агент евангелизатор**: Пише нацрт туторијала на основу датог плана и URL адреса.
2.  **Агент рецензент садржаја**: Прегледа нацрт. Проверава да ли број речи прелази 200.
3.  **Условно разгранaвање**:
      * **Ако је одобрено (Да)**: Ток рада наставља ка агенту за објављивање.
      * **Ако је одбачено (Не)**: Ток рада се зауставља и излаже разлог одбијања.
4.  **Агент за објављивање**: Ако је нацрт одобрен, овај агент чува садржај у Markdown датотеку.

#### Анализа Python имплементације

Овај пример користи прилагођену функцију `select_targets` која имплементира условну логику. Она се прослеђује `add_multi_selection_edge_group` и усмеравa ток рада на основу поља `review_result` из излаза рецензента.

```python
# 04.python-agent-framework-workflow-aifoundry-condition.ipynb

# Ова функција одређује следећи корак на основу резултата прегледа
def select_targets(review: ReviewResult, target_ids: list[str]) -> list[str]:
    handle_review_id, save_draft_id = target_ids
    if review.review_result == "Yes":
        # Ако је одобрено, настави са извршиоцем 'save_draft'
        return [save_draft_id]
    else:
        # Ако је одбијено, настави са извршиоцем 'handle_review' да пријавиш неуспех
        return [handle_review_id]

# Креатор радног тока користи функцију одабира за усмеравање
workflow = (
    WorkflowBuilder()
        .set_start_executor(evangelist_agent)
        .add_edge(evangelist_agent, reviewer_agent)
        .add_edge(reviewer_agent, to_reviewer_result)
        # Вишестрани угао имплементира условну логику
        .add_multi_selection_edge_group(
            to_reviewer_result,
            [handle_review, save_draft],
            selection_func=select_targets,
        )
        .add_edge(save_draft, publisher_agent)
        .build()
)
```

Прилагођени извршиоци као `to_reviewer_result` користе се за парсирање JSON излаза агената и претварање у јако типизиране објекте које функција за селекцију може да испита.

#### Анализа .NET (C#) имплементације

.NET верзија користи сличан приступ са функцијом услова. Дефинисан је `Func<object?, bool>` који проверава `Result` својство објекта `ReviewResult`.

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

Параметар `condition` методе `AddEdge` омогућава `WorkflowBuilder`-у да створи разгранату путању. Ток рада ће следити ивицу ка `publishExecutor` само ако услов `GetCondition(expectedResult: "Yes")` врати true. У супротном, прати се пут ка `sendReviewerExecutor`.

## Закључак

Microsoft Agent Framework Workflow пружа робусну и флексибилну основу за оркестрацију сложених мулти-агентских система. Користећи графску архитектуру и основне компоненте, програмери могу дизајнирати и имплементирати сложене токове рада и у Python-у и у .NET-у. Без обзира да ли ваша апликација захтева једноставну секвенцијалну обраду, паралелно извршење или динамичку условну логику, овај фрејмворк нуди алате за прављење моћних, скалабилних и типски-сигурних AI решења.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Изјава о одрицању одговорности**:
Овај документ је преведен коришћењем услуге за аутоматски превод [Co-op Translator](https://github.com/Azure/co-op-translator). Иако тежимо тачности, имајте у виду да аутоматски преводи могу садржати грешке или нетачности. Оригинални документ на његовом изворном језику треба сматрати ауторитативним извором. За критичне информације препоручује се професионални људски превод. Нисмо одговорни за било каква неспоразума или погрешна тумачења која произилазе из коришћења овог превода.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->