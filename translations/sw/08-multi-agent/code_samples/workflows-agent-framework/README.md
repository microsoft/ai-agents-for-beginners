# Kujenga Programu za Wakala Wengi kwa Kutumia Microsoft Agent Framework Workflow

Mafunzo haya yatakusaidia kuelewa na kujenga programu za wakala wengi kwa kutumia Microsoft Agent Framework. Tutachunguza dhana kuu za mifumo ya wakala wengi, kuingia ndani ya usanifu wa sehemu ya Workflow ya mfumo, na kupitia mifano ya vitendo katika Python na .NET kwa mifumo tofauti ya kazi.

## 1\. Kuelewa Mifumo ya Wakala Wengi

Wakala wa AI ni mfumo unaozidi uwezo wa Kielezo Kikubwa cha Lugha (LLM) cha kawaida. Unaweza kutambua mazingira yake, kufanya maamuzi, na kuchukua hatua ili kufanikisha malengo maalum. Mfumo wa wakala wengi unahusisha wakala kadhaa wakishirikiana kutatua tatizo ambalo lingekuwa gumu au lisilowezekana kwa wakala mmoja kushughulikia peke yake.

### Matukio ya Kawaida ya Matumizi

  * **Kutatua Matatizo Magumu**: Kugawanya kazi kubwa (mfano, kupanga tukio la kampuni) katika kazi ndogo zinazoshughulikiwa na wakala maalum (mfano, wakala wa bajeti, wakala wa vifaa, wakala wa masoko).
  * **Msaidizi wa Kijanja**: Wakala mkuu wa msaidizi akigawa kazi kama kupanga ratiba, utafiti, na uhifadhi kwa mawakala wengine maalum.
  * **Uundaji wa Maudhui Kiotomatiki**: Mchakato ambapo wakala mmoja anaandika maudhui, mwingine anayakagua kwa usahihi na mtindo, na wa tatu anayachapisha.

### Mifumo ya Wakala Wengi

Mifumo ya wakala wengi inaweza kupangwa kwa mifumo kadhaa, ambayo huamua jinsi wanavyoshirikiana:

  * **Mfululizo**: Mawakala hufanya kazi kwa mpangilio uliowekwa, kama mstari wa mkusanyiko. Matokeo ya wakala mmoja yanakuwa pembejeo kwa wakala mwingine.
  * **Sambamba**: Mawakala hufanya kazi kwa wakati mmoja kwenye sehemu tofauti za kazi, na matokeo yao hukusanywa mwishoni.
  * **Masharti**: Mchakato hufuata njia tofauti kulingana na matokeo ya wakala, sawa na kauli ya if-then-else.

## 2\. Usanifu wa Microsoft Agent Framework Workflow

Mfumo wa kazi wa Agent Framework ni injini ya hali ya juu ya uratibu iliyoundwa kusimamia mwingiliano mgumu kati ya mawakala wengi. Imejengwa juu ya usanifu wa msingi wa grafu unaotumia [Mfano wa utekelezaji wa Pregel](https://kowshik.github.io/JPregel/pregel_paper.pdf), ambapo usindikaji hufanyika kwa hatua zilizosawazishwa zinazoitwa "supersteps."

### Vipengele Vikuu

Usanifu unajumuisha sehemu kuu tatu:

1.  **Watekelezaji**: Hizi ni vitengo vya msingi vya usindikaji. Katika mifano yetu, `Agent` ni aina ya mtekelezaji. Kila mtekelezaji anaweza kuwa na wahandaji wa ujumbe kadhaa ambao huanzishwa kiotomatiki kulingana na aina ya ujumbe uliopokelewa.
2.  **Edges**: Hizi hufafanua njia ambayo ujumbe huchukua kati ya watekelezaji. Edges zinaweza kuwa na masharti, kuruhusu uelekezaji wa habari kwa njia ya grafu ya kazi.
3.  **Workflow**: Sehemu hii inaratibu mchakato mzima, kusimamia watekelezaji, edges, na mtiririko wa jumla wa utekelezaji. Inahakikisha kwamba ujumbe unashughulikiwa kwa mpangilio sahihi na kutiririsha matukio kwa ufuatiliaji.

*Diagramu inayoonyesha vipengele vikuu vya mfumo wa kazi.*

Muundo huu unaruhusu kujenga programu thabiti na zinazoweza kupanuka kwa kutumia mifumo ya msingi kama minyororo ya mfululizo, fan-out/fan-in kwa usindikaji sambamba, na mantiki ya switch-case kwa mtiririko wa masharti.

## 3\. Mifano ya Vitendo na Uchambuzi wa Nambari

Sasa, hebu tuchunguze jinsi ya kutekeleza mifumo tofauti ya kazi kwa kutumia mfumo. Tutaangalia nambari za Python na .NET kwa kila mfano.

### Kesi 1: Mchakato wa Mfululizo wa Msingi

Hii ni mifumo rahisi zaidi, ambapo matokeo ya wakala mmoja yanapokelewa moja kwa moja na mwingine. Tukio letu linahusisha wakala wa hoteli `FrontDesk` anayetoa mapendekezo ya kusafiri, ambayo yanakaguliwa na wakala wa `Concierge`.

*Diagramu ya mchakato wa msingi wa FrontDesk -\> Concierge.*

#### Historia ya Tukio

Msafiri anauliza mapendekezo ya Paris.

1.  Wakala wa `FrontDesk`, aliyebuniwa kwa ufupi, anapendekeza kutembelea Louvre Museum.
2.  Wakala wa `Concierge`, anayependelea uzoefu halisi, anapokea pendekezo hili. Anakagua pendekezo na kutoa maoni, akipendekeza mbadala wa ndani, usio wa kitalii.

#### Uchambuzi wa Utekelezaji wa Python

Katika mfano wa Python, tunaanza kwa kufafanua na kuunda mawakala wawili, kila mmoja akiwa na maagizo maalum.

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

Kisha, `WorkflowBuilder` hutumika kujenga grafu. `front_desk_agent` huwekwa kama sehemu ya kuanzia, na edge huundwa kuunganisha matokeo yake na `reviewer_agent`.

```python
# 01.python-agent-framework-workflow-ghmodel-basic.ipynb

workflow = WorkflowBuilder().set_start_executor(front_desk_agent).add_edge(front_desk_agent, reviewer_agent).build()
```

Hatimaye, mchakato unatekelezwa na maelezo ya awali ya mtumiaji.

```python
# 01.python-agent-framework-workflow-ghmodel-basic.ipynb

result =''
# The run_stream method executes the workflow and streams events.
async for event in workflow.run_stream('I would like to go to Paris.'):
    if isinstance(event, WorkflowEvent):
        result += str(event.data)
```

#### Uchambuzi wa Utekelezaji wa .NET (C\#)

Utekelezaji wa .NET unafuata mantiki sawa. Kwanza, constants hufafanuliwa kwa majina ya mawakala na maagizo yao.

```csharp
// 01.dotnet-agent-framework-workflow-ghmodel-basic.ipynb

const string ReviewerAgentName = "Concierge";
const string ReviewerAgentInstructions = @"
    You are an are hotel concierge who has opinions about providing the most local and authentic experiences for travelers...";

const string FrontDeskAgentName = "FrontDesk";
const string FrontDeskAgentInstructions = @"""
    You are a Front Desk Travel Agent with ten years of experience and are known for brevity...";
```

Mawakala huundwa kwa kutumia `OpenAIClient`, kisha `WorkflowBuilder` hufafanua mtiririko wa mfululizo kwa kuongeza edge kutoka `frontDeskAgent` hadi `reviewerAgent`.

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

Mchakato kisha huendeshwa na ujumbe wa mtumiaji, na matokeo hutiririshwa kurudi.

### Kesi 2: Mchakato wa Mfululizo wa Hatua Nyingi

Mfumo huu unapanua mfululizo wa msingi ili kujumuisha mawakala zaidi. Ni bora kwa michakato inayohitaji hatua nyingi za uboreshaji au mabadiliko.

#### Historia ya Tukio

Mtumiaji anatoa picha ya sebule na kuomba nukuu ya samani.

1.  **Sales-Agent**: Inatambua vitu vya samani kwenye picha na kuunda orodha.
2.  **Price-Agent**: Inachukua orodha ya vitu na kutoa maelezo ya bei, ikijumuisha chaguo za bajeti, za kati, na za hali ya juu.
3.  **Quote-Agent**: Inapokea orodha yenye bei na kuibadilisha kuwa hati rasmi ya nukuu katika Markdown.

*Diagramu ya mchakato wa Sales -\> Price -\> Quote.*

#### Uchambuzi wa Utekelezaji wa Python

Mawakala watatu hufafanuliwa, kila mmoja akiwa na jukumu maalum. Mchakato huundwa kwa kutumia `add_edge` kuunda mnyororo: `sales_agent` -\> `price_agent` -\> `quote_agent`.

```python
# 02.python-agent-framework-workflow-ghmodel-sequential.ipynb

# Create three specialized agents
sales_agent = chat_client.create_agent(...)
price_agent = chat_client.create_agent(...)
quote_agent = chat_client.create_agent(...)

# Build the sequential workflow
workflow = WorkflowBuilder().set_start_executor(sales_agent).add_edge(sales_agent, price_agent).add_edge(price_agent, quote_agent).build()
```

Pembejeo ni `ChatMessage` inayojumuisha maandishi na URI ya picha. Mfumo hushughulikia kupitisha matokeo ya kila wakala kwa mwingine katika mfululizo hadi nukuu ya mwisho itakapozalishwa.

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

#### Uchambuzi wa Utekelezaji wa .NET (C\#)

Mfano wa .NET unafanana na toleo la Python. Mawakala watatu (`salesagent`, `priceagent`, `quoteagent`) huundwa. `WorkflowBuilder` huunganisha kwa mfululizo.

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

Ujumbe wa mtumiaji huundwa na data ya picha (kama bytes) na maelezo ya maandishi. Njia ya `InProcessExecution.StreamAsync` huanzisha mchakato, na matokeo ya mwisho hukamatwa kutoka kwa mtiririko.

### Kesi 3: Mchakato Sambamba

Mfumo huu hutumika wakati kazi zinaweza kufanywa kwa wakati mmoja ili kuokoa muda. Inahusisha "fan-out" kwa mawakala wengi na "fan-in" ili kukusanya matokeo.

#### Historia ya Tukio

Mtumiaji anaomba kupanga safari ya Seattle.

1.  **Dispatcher (Fan-Out)**: Ombi la mtumiaji linatumwa kwa mawakala wawili kwa wakati mmoja.
2.  **Researcher-Agent**: Inatafiti vivutio, hali ya hewa, na mambo muhimu ya safari ya Seattle mwezi wa Desemba.
3.  **Plan-Agent**: Inaunda ratiba ya kina ya safari ya kila siku kwa kujitegemea.
4.  **Aggregator (Fan-In)**: Matokeo kutoka kwa mtafiti na mpangaji hukusanywa na kuwasilishwa pamoja kama matokeo ya mwisho.

*Diagramu ya mchakato sambamba wa Researcher na Planner.*

#### Uchambuzi wa Utekelezaji wa Python

`ConcurrentBuilder` hurahisisha uundaji wa mfumo huu. Unataja tu mawakala wanaoshiriki, na builder huunda kiotomatiki mantiki ya fan-out na fan-in.

```python
# 03.python-agent-framework-workflow-ghmodel-concurrent.ipynb

research_agent = chat_client.create_agent(name="Researcher-Agent", ...)
plan_agent = chat_client.create_agent(name="Plan-Agent", ...)

# ConcurrentBuilder handles the fan-out/fan-in logic
workflow = ConcurrentBuilder().participants([research_agent, plan_agent]).build()

# Run the workflow
events = await workflow.run("Plan a trip to Seattle in December")
```

Mfumo unahakikisha kwamba `research_agent` na `plan_agent` hufanya kazi sambamba, na matokeo yao ya mwisho hukusanywa katika orodha.

#### Uchambuzi wa Utekelezaji wa .NET (C\#)

Katika .NET, mfumo huu unahitaji ufafanuzi wa wazi zaidi. Watekelezaji maalum (`ConcurrentStartExecutor` na `ConcurrentAggregationExecutor`) huundwa kushughulikia mantiki ya fan-out na fan-in.

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

`WorkflowBuilder` kisha hutumia `AddFanOutEdge` na `AddFanInEdge` kujenga grafu na watekelezaji hawa maalum na mawakala.

```csharp
// 03.dotnet-agent-framework-workflow-ghmodel-concurrent.ipynb

var workflow = new WorkflowBuilder(startExecutor)
            .AddFanOutEdge(startExecutor, targets: [researcherAgent, plannerAgent])
            .AddFanInEdge(aggregationExecutor, sources: [researcherAgent, plannerAgent])
            .WithOutputFrom(aggregationExecutor)
            .Build();
```

### Kesi 4: Mchakato wa Masharti

Mchakato wa masharti huanzisha mantiki ya matawi, kuruhusu mfumo kuchukua njia tofauti kulingana na matokeo ya kati.

#### Historia ya Tukio

Mchakato huu unaharakisha uundaji na uchapishaji wa mafunzo ya kiufundi.

1.  **Evangelist-Agent**: Anaandika rasimu ya mafunzo kulingana na muhtasari uliotolewa na URL.
2.  **ContentReviewer-Agent**: Anakagua rasimu. Anakagua ikiwa idadi ya maneno ni zaidi ya 200.
3.  **Tawi la Masharti**:
      * **Ikiwa Imeidhinishwa (`Yes`)**: Mchakato unaendelea kwa `Publisher-Agent`.
      * **Ikiwa Imebatilishwa (`No`)**: Mchakato unakoma na kutoa sababu ya kukataliwa.
4.  **Publisher-Agent**: Ikiwa rasimu imeidhinishwa, wakala huyu huokoa maudhui kwenye faili ya Markdown.

#### Uchambuzi wa Utekelezaji wa Python

Mfano huu hutumia kazi maalum, `select_targets`, kutekeleza mantiki ya masharti. Kazi hii hupitishwa kwa `add_multi_selection_edge_group` na kuelekeza mchakato kulingana na uwanja wa `review_result` kutoka kwa matokeo ya mkaguzi.

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

Watekelezaji maalum kama `to_reviewer_result` hutumika kuchambua matokeo ya JSON kutoka kwa mawakala na kuyabadilisha kuwa vitu vilivyo na aina kali ambavyo kazi ya uteuzi inaweza kuchunguza.

#### Uchambuzi wa Utekelezaji wa .NET (C\#)

Toleo la .NET hutumia mbinu sawa na kazi ya masharti. `Func<object?, bool>` hufafanuliwa ili kukagua mali ya `Result` ya kitu cha `ReviewResult`.

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

Kigezo cha `condition` cha njia ya `AddEdge` huruhusu `WorkflowBuilder` kuunda njia ya matawi. Mchakato utafuata edge hadi `publishExecutor` tu ikiwa hali ya `GetCondition(expectedResult: "Yes")` inarudi kweli. Vinginevyo, utafuata njia hadi `sendReviewerExecutor`.

## Hitimisho

Microsoft Agent Framework Workflow hutoa msingi thabiti na rahisi kwa uratibu wa mifumo tata ya wakala wengi. Kwa kutumia usanifu wake wa grafu na vipengele vikuu, watengenezaji wanaweza kubuni na kutekeleza michakato ya kazi ya hali ya juu katika Python na .NET. Ikiwa programu yako inahitaji usindikaji rahisi wa mfululizo, utekelezaji sambamba, au mantiki ya masharti ya nguvu, mfumo huu unatoa zana za kujenga suluhisho za AI zenye nguvu, zinazoweza kupanuka, na salama kwa aina.

---

**Kanusho**:  
Hati hii imetafsiriwa kwa kutumia huduma ya tafsiri ya AI [Co-op Translator](https://github.com/Azure/co-op-translator). Ingawa tunajitahidi kwa usahihi, tafadhali fahamu kuwa tafsiri za kiotomatiki zinaweza kuwa na makosa au kutokuwa sahihi. Hati ya asili katika lugha yake ya awali inapaswa kuzingatiwa kama chanzo cha mamlaka. Kwa taarifa muhimu, inashauriwa kutumia huduma ya tafsiri ya kibinadamu ya kitaalamu. Hatutawajibika kwa maelewano au tafsiri zisizo sahihi zinazotokana na matumizi ya tafsiri hii.