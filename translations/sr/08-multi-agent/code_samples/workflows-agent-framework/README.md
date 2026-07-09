# Изградња апликација са више агената помоћу Microsoft Agent Framework Workflow

Овај туторијал ће вас водити кроз разумевање и изградњу апликација са више агената користећи Microsoft Agent Framework. Истражићемо основне концепте мултиагентских система, упознаћемо архитектуру компонената Workflow у оквиру Framework-а, и проћи кроз практичне примере у Питону и .NET-у за различите шаблоне токова рада.

## 1\. Разумевање мултиагентских система

AI агент је систем који превазилази могућности стандардног великог језичког модела (LLM). Може да перципира своју околину, доноси одлуке и предузима активности како би остварио одређене циљеве. Мултиагентски систем укључује више таквих агената који сарађују да реше проблем који би био тежак или немогућ за једног агента самог да обради.

### Уобичајени сценарији примена

  * **Сложено решавање проблема**: Разбијање великог задатка (нпр. планирање догађаја за целу компанију) на мање подзадаке које обрађују специјализовани агенти (нпр. буџетски агент, логистички агент, маркетиншки агент).
  * **Виртуелни асистенти**: Главни агент асистент који делегира задатке као што су заказивање, истраживање и резервације другим специјализованим агентима.
  * **Аутоматизовано креирање садржаја**: Ток рада где један агент саставља садржај, други га прегледа због тачности и тона, а трећи га објављује.

### Шаблони мултиагената

Мултиагентски системи могу бити организовани у више шаблона, који одређују како они комуницирају:

  * **Секвенцијални**: Агенти раде по унапред дефинисаном редоследу, као на монтажној траци. Излаз једног агента постаје улаз за следећег.
  * **Паралелни**: Агенти раде истовремено на различитим деловима задатка, а њихови резултати се на крају сабирају.
  * **Условни**: Ток рада прати различите путеве у зависности од излаза агента, слично као if-then-else изјава.

## 2\. Архитектура Microsoft Agent Framework Workflow

Систем тока рада у Agent Framework-у је напредни механизам за оркестрацију, дизајниран да управља комплексним интеракцијама између више агената. Изграђен је на архитектури заснованој на графу која користи [Pregel-стил модел извршења](https://kowshik.github.io/JPregel/pregel_paper.pdf), где се обрада врши у синхронизованим корацима названим „supersteps“.

### Основне компоненте

Архитектуру чине три главна дела:

1.  **Извршиоци**: Ово су основне јединице за обраду. У нашим примерима, `Agent` је тип извршиоца. Сваки извршилац може имати више обрађивача порука које се аутоматски позивају у зависности од типа примљене поруке.
2.  **Гране**: Оне дефинишу пут којим поруке путују између извршилаца. Гране могу имати услове, омогућавајући динамичко усмеравање информација кроз граф тока рада.
3.  **Ток рада**: Ова компонента оркестрира цео процес, управљајући извршиоцима, гранама и општим током извршења. Обезбеђује да се поруке обрађују у исправном редоследу и емитује догађаје за посматрање.

*Дијаграм који илуструје основне компоненте система тока рада.*

Ова структура омогућава изградњу поузданих и скалабилних апликација користећи основне шаблоне као што су секвенцијалне ланце, fan-out/fan-in за паралелну обраду и switch-case логику за условне токове.

## 3\. Практични примери и анализа кода

Хајде сада да истражимо како имплементирати различите шаблоне тока рада користећи Framework. Погледаћемо Python и .NET код за сваки пример.

### Случај 1: Основни секвенцијални ток рада

Ово је најједноставнији шаблон, где се излаз једног агента директно шаље другом. Наш сценарио укључује хотелског агента `FrontDesk` који даје препоруку за путовање, коју затим прегледа агент `Concierge`.

*Дијаграм основног тока рада FrontDesk -> Concierge.*

#### Позадина сценарија

Путник тражи препоруку у Паризу.

1.  `FrontDesk` агент, дизајниран за краткоћу, предлаже посету Лувру.
2.  `Concierge` агент, који преферира аутентична искуства, прими овај предлог. Прегледа препоруку и даје повратне информације, предлажући локалнију, мање туристичку алтернативу.

#### Анализа имплементације у Питону

У примеру Питона прво дефинишемо и креирамо два агента, сваки са специфичним инструкцијама.

```python
# 01.python-agent-framework-workflow-ghmodel-basic.ipynb

# Дефинишите улоге агента и упутства
REVIEWER_NAME = "Concierge"
REVIEWER_INSTRUCTIONS = """
    You are an are hotel concierge who has opinions about providing the most local and authentic experiences for travelers...
    """

FRONTDESK_NAME = "FrontDesk"
FRONTDESK_INSTRUCTIONS = """
    You are a Front Desk Travel Agent with ten years of experience and are known for brevity...
    """

# Креирајте инстанце агента
reviewer_agent = chat_client.as_agent(
    instructions=(REVIEWER_INSTRUCTIONS),
    name=REVIEWER_NAME,
)

front_desk_agent = chat_client.as_agent(
    instructions=(FRONTDESK_INSTRUCTIONS),
    name=FRONTDESK_NAME,
)
```

Затим се користи `WorkflowBuilder` за конструисање графа. `front_desk_agent` је постављен као почетна тачка, а грана повезује његов излаз са `reviewer_agent`.

```python
# 01.python-agent-framework-radni-tok-ghmodel-osnovni.ipynb

workflow = WorkflowBuilder(start_executor=front_desk_agent).add_edge(front_desk_agent, reviewer_agent).build()
```

На крају, ток рада се извршава са почетним корисничким упитом.

```python
# 01.python-agent-framework-workflow-ghmodel-basic.ipynb

result =''
# run извршава радни ток; get_outputs() враћа резултат извршиоца.
events = await workflow.run('I would like to go to Paris.')
outputs = events.get_outputs()
result = outputs[0].text if outputs else ''
```

#### Анализа имплементације у .NET (C#)

.NET имплементација следи веома сличну логику. Прво се дефинишу константе за имена агената и инструкције.

```csharp
// 01.dotnet-agent-framework-workflow-ghmodel-basic.ipynb

const string ReviewerAgentName = "Concierge";
const string ReviewerAgentInstructions = @"
    You are an are hotel concierge who has opinions about providing the most local and authentic experiences for travelers...";

const string FrontDeskAgentName = "FrontDesk";
const string FrontDeskAgentInstructions = @"""
    You are a Front Desk Travel Agent with ten years of experience and are known for brevity...";
```

Агенти се креирају користећи `AzureOpenAIClient` (Responses API), а затим `WorkflowBuilder` дефинише секвенцијални ток додавањем гране од `frontDeskAgent` до `reviewerAgent`.

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

Ток рада се покреће корисниковом поруком, а резултати се емитују назад.

### Случај 2: Мултистепени секвенцијални ток рада

Овај шаблон проширује основни секвенцијални ток да укључи више агената. Идеалан је за процесе који захтевају неколико фаза прераде или трансформације.

#### Позадина сценарија

Корисник доставља слику дневне собе и тражи понуду за намештај.

1.  **Sales-Agent**: Идентификује комаде намештаја на слици и креира листу.
2.  **Price-Agent**: Узима листу ставки и пружа детаљан преглед цена, укључујући буџетске, средњег ранга и премиум опције.
3.  **Quote-Agent**: Прима ценовник и форматира га у формални документ понуде у Markdown формату.

*Дијаграм тока рада Sales -> Price -> Quote.*

#### Анализа имплементације у Питону

Дефинисана су три агента, сваки са својом специјализованом улогом. Ток рада је конструисан коришћењем `add_edge` да се створи ланац: `sales_agent` -> `price_agent` -> `quote_agent`.

```python
# 02.python-agent-framework-workflow-ghmodel-sequential.ipynb

# Креирајте три специјализована агента
sales_agent = chat_client.as_agent(...)
price_agent = chat_client.as_agent(...)
quote_agent = chat_client.as_agent(...)

# Направите секвенцијални ток рада
workflow = WorkflowBuilder(start_executor=sales_agent).add_edge(sales_agent, price_agent).add_edge(price_agent, quote_agent).build()
```

Улаз је `ChatMessage` који укључује и текст и URI слике. Framework се брине о преносу излаза сваког агента следећем у низу док се коначна понуда не генерише.

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

#### Анализа имплементације у .NET (C#)

.NET пример одражава Питонову верзију. Креирају се три агента (`salesagent`, `priceagent`, `quoteagent`). `WorkflowBuilder` их повезује секвенцијално.

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

Корисничка порука се конструише са подацима слике (у бајтовима) и текстуалним упитом. Метода `InProcessExecution.StreamAsync` покреће ток рада, а коначни излаз се узима из стрима.

### Случај 3: Паралелни ток рада

Овај шаблон се користи када се задаци могу изводити истовремено ради уштеде времена. Укључује “fan-out” ка више агената и “fan-in” за сабирање резултата.

#### Позадина сценарија

Корисник тражи да испланира путовање у Сијетл.

1.  **Dispatcher (Fan-Out)**: Кориснички захтев се истовремено шаље двојици агената.
2.  **Researcher-Agent**: Истражује атракције, време и кључне аспекте путовања у Сијетл у децембру.
3.  **Plan-Agent**: Самостално креира детаљан дневни план путовања.
4.  **Aggregator (Fan-In)**: Резултати истраживача и планирача се сакупљају и презентују као коначан резултат.

*Дијаграм паралелног тока рада Researcher и Planner.*

#### Анализа имплементације у Питону

`ConcurrentBuilder` поједностављује креирање овог шаблона. Једноставно наведете агенте учеснике, и builder аутоматски креира потребну fan-out и fan-in логику.

```python
# 03.python-agent-framework-workflow-ghmodel-concurrent.ipynb

research_agent = chat_client.as_agent(name="Researcher-Agent", ...)
plan_agent = chat_client.as_agent(name="Plan-Agent", ...)

# ConcurrentBuilder обрађује логику расподеле и прикупљања
workflow = ConcurrentBuilder().participants([research_agent, plan_agent]).build()

# Покрени ток рада
events = await workflow.run("Plan a trip to Seattle in December")
```

Framework води рачуна да `research_agent` и `plan_agent` раде паралелно, и њихови коначни излази се сакупљају у листу.

#### Анализа имплементације у .NET (C#)

У .NET-у, овај шаблон захтева експлицитнију дефиницију. Креирају се прилагођени извршиоци (`ConcurrentStartExecutor` и `ConcurrentAggregationExecutor`) који обрађују фан-аут и фан-ин логику.

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

`WorkflowBuilder` затим користи `AddFanOutEdge` и `AddFanInEdge` за изградњу графа са овим прилагођеним извршиоцима и агенатима.

```csharp
// 03.dotnet-agent-framework-workflow-ghmodel-concurrent.ipynb

var workflow = new WorkflowBuilder(startExecutor)
            .AddFanOutEdge(startExecutor, targets: [researcherAgent, plannerAgent])
            .AddFanInEdge(aggregationExecutor, sources: [researcherAgent, plannerAgent])
            .WithOutputFrom(aggregationExecutor)
            .Build();
```

### Случај 4: Условни ток рада

Условни токови рада уводе разгранавајућу логику, која омогућава систему да иде различитим путевима на основу посредних резултата.

#### Позадина сценарија

Овај ток рада аутоматизује креирање и објављивање техничког туторијала.

1.  **Evangelist-Agent**: Пише нацрт туторијала на основу датума и URL адреса.
2.  **ContentReviewer-Agent**: Прегледа нацрт и проверава да ли број речи прелази 200.
3.  **Условна грана**:
      * **Ако је одобрено (`Yes`)**: Ток рада наставља ка `Publisher-Agent`.
      * **Ако је одбијено (`No`)**: Ток рада се зауставља и приказује разлог одбијања.
4.  **Publisher-Agent**: Ако је нацрт одобрен, овај агент чува садржај у Markdown фајлу.

#### Анализа имплементације у Питону

Овај пример користи прилагођену функцију `select_targets` за имплементацију условне логике. Функција се прослеђује `add_multi_selection_edge_group` и усмерава ток рада на основу поља `review_result` из излаза рецензента.

```python
# 04.python-agent-framework-workflow-aifoundry-condition.ipynb

# Ова функција одређује следећи корак на основу резултата прегледа
def select_targets(review: ReviewResult, target_ids: list[str]) -> list[str]:
    handle_review_id, save_draft_id = target_ids
    if review.review_result == "Yes":
        # Ако је одобрено, пређи на извршиоца 'save_draft'
        return [save_draft_id]
    else:
        # Ако је одбијено, пређи на извршиоца 'handle_review' да пријави неуспех
        return [handle_review_id]

# Конструктор радног процеса користи функцију избора за усмеравање
workflow = (
    WorkflowBuilder()
        .set_start_executor(evangelist_agent)
        .add_edge(evangelist_agent, reviewer_agent)
        .add_edge(reviewer_agent, to_reviewer_result)
        # Вишеструки изборни руб спроводи условну логику
        .add_multi_selection_edge_group(
            to_reviewer_result,
            [handle_review, save_draft],
            selection_func=select_targets,
        )
        .add_edge(save_draft, publisher_agent)
        .build()
)
```

Прилагођени извршиоци као `to_reviewer_result` користе се за парсирање JSON излаза агената и претварање у снажно типизиране објекте које функција за селекцију може да проверава.

#### Анализа имплементације у .NET (C#)

.NET верзија користи сличан приступ са функцијом услова. Дефинисан је `Func<object?, bool>` да провери својство `Result` објекта `ReviewResult`.

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

Параметар `condition` методе `AddEdge` омогућава `WorkflowBuilder`-у да створи разгранавајући пут. Ток рада ће пратити грану ка `publishExecutor` само ако услов `GetCondition(expectedResult: "Yes")` врати истину. У супротном, иде путем ка `sendReviewerExecutor`.

## Закључак

Microsoft Agent Framework Workflow пружа робусну и флексибилну основу за оркестрацију комплексних мултиагентских система. Коришћењем његове граф-базиране архитектуре и основних компоненти, програмери могу дизајнирати и имплементирати сложене токове рада у Питону и .NET-у. Без обзира да ли ваша апликација захтева једноставну секвенцијалну обраду, паралелно извршење или динамичку условну логику, овај framework нуди алате за изградњу моћних, скалабилних и типски безбедних AI решења.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Изјава о одрицању одговорности**:
Овај документ је преведен коришћењем услуге за аутоматски превод [Co-op Translator](https://github.com/Azure/co-op-translator). Иако тежимо тачности, имајте у виду да аутоматски преводи могу садржати грешке или нетачности. Оригинални документ на његовом изворном језику треба сматрати ауторитативним извором. За критичне информације препоручује се професионални људски превод. Нисмо одговорни за било каква неспоразума или погрешна тумачења која произилазе из коришћења овог превода.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->