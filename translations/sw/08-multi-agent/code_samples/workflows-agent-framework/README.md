# Kujenga Programu za Wakala Wengi kwa Microsoft Agent Framework Workflow

Mafunzo haya yatakuongoza kuelewa na kujenga programu za wakala wengi kwa kutumia Microsoft Agent Framework. Tutachunguza dhana za msingi za mifumo ya wakala wengi, kuingia ndani ya usanifu wa sehemu ya Workflow ya mfumo, na kutembea kupitia mifano halisi katika Python na .NET kwa mifumo tofauti ya workflow.

## 1\. Kuelewa Mifumo ya Wakala Wengi

Wakala wa AI ni mfumo unaozidi uwezo wa Mfano wa Lugha Kubwa (LLM) wa kawaida. Unaweza kugundua mazingira yake, kufanya maamuzi, na kuchukua hatua kufanikisha malengo maalum. Mfumo wa wakala wengi unahusisha wakala kadhaa wanaoshirikiana kutatua tatizo ambalo lingekuwa gumu au lisiyowezekana kwa wakala mmoja peke yake.

### Matukio ya Kawaida ya Maombi

  * **Kutatua Tatizo Zito**: Kugawanya jukumu kubwa (mfano, kupanga tukio kwa kampuni nzima) kuwa kazi ndogo ndogo zinazoshughulikiwa na wakala maalum (mfano, wakala wa bajeti, wakala wa usafirishaji, wakala wa masoko).
  * **Msaidizi wa Kidijitali**: Wakala mkuu wa msaidizi anayetoa majukumu kama kupanga ratiba, utafiti, na kuweka booking kwa wakala wengine maalum.
  * **Uundaji wa Maudhui Otomatiki**: Workflow ambapo wakala mmoja huandika rasimu ya maudhui, mwingine hurekebisha kwa usahihi na mtindo, na mwingine hutangaza.

### Mifumo ya Wakala Wengi

Mifumo ya wakala wengi inaweza kuandaliwa kwa mifumo kadhaa, ambayo huamua jinsi wanavyoshirikiana:

  * **Mfuatano**: Wakala hufanya kazi kwa mpangilio uliowekwa awali, kama mkusanyiko wa uzalishaji. Matokeo ya wakala mmoja hutumika kama ingizo kwa wakala anayefuata.
  * **Simultaneous**: Wakala hufanya kazi kwa wakati mmoja kwenye sehemu tofauti za kazi, na matokeo yao huunganishwa mwishoni.
  * **Conditional**: Workflow husifu njia tofauti kulingana na matokeo ya wakala, kama kauli ya ikiwa-basi-vinginevyo.

## 2\. Usanifu wa Microsoft Agent Framework Workflow

Mfumo wa workflow wa Agent Framework ni injini ya hali ya juu ya kupanga mwingiliano tata kati ya wakala wengi. Imejengwa kwa usanifu wa msingi wa grafu unaotumia [mfano wa utekelezaji wa mtindo Pregel](https://kowshik.github.io/JPregel/pregel_paper.pdf), ambapo usindikaji hufanyika kwa hatua za kusawazisha zinazoitwa "supersteps."

### Sehemu Muhimu

Usanifu unajumuisha sehemu kuu tatu:

1.  **Watekelezaji**: Hawa ndio vitengo msingi vya usindikaji. Katika mifano yetu, `Agent` ni aina ya mtekelezaji. Kila mtekelezaji anaweza kuwa na wachunguzi wa ujumbe ambao huita moja kwa moja kulingana na aina ya ujumbe unaopokelewa.
2.  **Miganano**: Hii inaelezea njia ambazo ujumbe hukitumia kati ya watekelezaji. Miganano inaweza kuwa na masharti, kuwezesha usambazaji wa mwelekeo wa taarifa kwa njia ya mfano wa workflow wa grafu.
3.  **Workflow**: Sehemu hii inapanga mchakato mzima, kusimamia watekelezaji, miganano, na mtiririko wa utekelezaji kwa jumla. Inahakikisha kuwa ujumbe unasindika kwa mpangilio sahihi na kupeleka matukio kwa ajili ya ufuatiliaji.

*Mchoro unaoonyesha sehemu kuu za mfumo wa workflow.*

Muundo huu unaruhusu kujenga programu imara na zinazoweza kupanuka kwa kutumia mifumo ya msingi kama minyororo ya mfuatano, fan-out/fan-in kwa usindikaji sambamba, na mantiki ya switch-case kwa miale ya masharti.

## 3\. Mifano Halisi na Uchambuzi wa Msimbo

Sasa, tuchambue jinsi ya kutekeleza mifumo tofauti ya workflow kwa kutumia mfumo huu. Tutatazama msimbo wa Python na .NET kwa kila mfano.

### Kesi 1: Workflow ya Mfuatano Msingi

Huu ni mfumo rahisi kabisa, ambapo matokeo ya wakala mmoja hutumwa moja kwa moja kwa mwingine. Hali yetu inahusisha wakala wa hoteli `FrontDesk` anayetoa mapendekezo ya safari, ambayo kisha hakiki na wakala `Concierge`.

*Mchoro wa workflow rahisi wa FrontDesk -\> Concierge.*

#### Muhtasari wa Hali

Msafiri anaomba pendekezo huko Paris.

1.  Wakala `FrontDesk`, ambaye ameundwa kwa kifupi, anapendekeza kutembelea Makumbusho ya Louvre.
2.  Wakala `Concierge`, anayeoanisha uzoefu halisi, anapokea pendekezo hili. Analipitia na kutoa maoni, akipendekeza mbadala wa maeneo ya ndani zaidi na yasiyo ya watalii.

#### Uchambuzi wa Utekelezaji wa Python

Katika mfano wa Python, kwanza tunaeleza na kuunda wakala wawili, kila mmoja akiwa na maagizo maalum.

```python
# 01.python-agent-framework-workflow-ghmodel-basic.ipynb

# Fafanua majukumu na maelekezo ya wakala
REVIEWER_NAME = "Concierge"
REVIEWER_INSTRUCTIONS = """
    You are a hotel concierge who has opinions about providing the most local and authentic experiences for travelers...
    """

FRONTDESK_NAME = "FrontDesk"
FRONTDESK_INSTRUCTIONS = """
    You are a Front Desk Travel Agent with ten years of experience and are known for brevity...
    """

# Unda visa vya wakala
reviewer_agent = chat_client.as_agent(
    instructions=(REVIEWER_INSTRUCTIONS),
    name=REVIEWER_NAME,
)

front_desk_agent = chat_client.as_agent(
    instructions=(FRONTDESK_INSTRUCTIONS),
    name=FRONTDESK_NAME,
)
```

Kinyume chake, `WorkflowBuilder` hutumika kujenga grafu. `front_desk_agent` amewekwa kama mwanzo, na miganano imetengenezwa kuunganisha matokeo yake na `reviewer_agent`.

```python
# 01.python-wakala-muundo-mtiririko-ghmodel-msingi.ipynb

workflow = WorkflowBuilder(start_executor=front_desk_agent).add_edge(front_desk_agent, reviewer_agent).build()
```

Mwishowe, workflow inatekelezwa na ombi la mwanzo la mtumiaji.

```python
# 01.python-agent-framework-workflow-ghmodel-basic.ipynb

result =''
# run hutekeleza mtiririko wa kazi; get_outputs() hurudisha matokeo ya mtendaji wa pato.
events = await workflow.run('I would like to go to Paris.')
outputs = events.get_outputs()
result = outputs[0].text if outputs else ''
```

#### Uchambuzi wa Utekelezaji wa .NET (C#)

Utekelezaji wa .NET unafuata mantiki sawa. Kwanza, vigezo vimeainishwa kwa majina na maagizo ya wakala.

```csharp
// 01.dotnet-agent-framework-workflow-ghmodel-basic.ipynb

const string ReviewerAgentName = "Concierge";
const string ReviewerAgentInstructions = @"
    You are a hotel concierge who has opinions about providing the most local and authentic experiences for travelers...";

const string FrontDeskAgentName = "FrontDesk";
const string FrontDeskAgentInstructions = @"""
    You are a Front Desk Travel Agent with ten years of experience and are known for brevity...";
```

Wakala hao huundwa kwa kutumia `AzureOpenAIClient` (API ya Majibu), na kisha `WorkflowBuilder` huvutia mtiririko wa mfuatano kwa kuongeza miganano kutoka `frontDeskAgent` kwenda `reviewerAgent`.

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

Workflow huendeshwa kisha na ujumbe wa mtumiaji na matokeo hutiririka kurudi.

### Kesi 2: Workflow ya Mfuatano wa Hatua Nyingi

Mfumo huu unaendelea na mfuatano wa msingi kuhusisha wakala zaidi. Ni bora kwa michakato inayohitaji hatua kadhaa za uboreshaji au mabadiliko.

#### Muhtasari wa Hali

Mtumiaji anatoa picha ya chumba cha kuishi na kuomba bei ya samani.

1.  **Wakala wa Mauzo**: Huutambua vitu vya samani kwenye picha na kuunda orodha.
2.  **Wakala wa Bei**: Anachukua orodha na kutoa mgawanyo wa bei kwa kina, ikiwa ni pamoja na chaguo la bajeti, la wastani, na la premium.
3.  **Wakala wa Nukuu**: Anakubali orodha yenye bei na kuibadilisha kuwa hati rasmi ya nukuu katika Markdown.

*Mchoro wa workflow wa Mauzo -\> Bei -\> Nukuu.*

#### Uchambuzi wa Utekelezaji wa Python

Wakala watatu wameelezwa, kila mmoja na jukumu maalum. Workflow inajengwa kwa kutumia `add_edge` kuunda mnyororo: `sales_agent` -\> `price_agent` -\> `quote_agent`.

```python
# 02.python-agent-framework-workflow-ghmodel-sequential.ipynb

# Unda mawakala wengi maalum
sales_agent = chat_client.as_agent(...)
price_agent = chat_client.as_agent(...)
quote_agent = chat_client.as_agent(...)

# Jenga mtiririko kazi mfululizo
workflow = WorkflowBuilder(start_executor=sales_agent).add_edge(sales_agent, price_agent).add_edge(price_agent, quote_agent).build()
```

Ingizo ni `ChatMessage` iliyojumuisha maandishi na kiungo cha picha. Mfumo unashughulikia kufikisha matokeo ya kila wakala kwa mwingine hadi nukuu ya mwisho itolewe.

```python
# 02.python-agent-framework-workflow-ghmodel-sequential.ipynb

# Ujumbe wa mtumiaji una maandishi na picha
message = ChatMessage(
        role=Role.USER,
        contents=[
            TextContent(text="Please find the relevant furniture..."),
            DataContent(uri=image_uri, media_type="image/png")
        ]
)

# Endesha mtiririko wa kazi
events = await workflow.run(message)
```

#### Uchambuzi wa Utekelezaji wa .NET (C#)

Mfano wa .NET unafanana na wa Python. Wakala watatu (`salesagent`, `priceagent`, `quoteagent`) huundwa. `WorkflowBuilder` huunganisha mfuatano wao.

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

Ujumbe wa mtumiaji umeundwa pamoja na data ya picha (kwa bajeti) na maandishi ya ombi. Mbinu `InProcessExecution.RunStreamingAsync` huanzisha workflow, na matokeo ya mwisho yanakamatwa kutoka kwenye mtiririko.

### Kesi 3: Workflow ya Simultaneous

Mfumo huu hutumika wakati kazi zinaweza kufanywa kwa wakati mmoja kuhifadhi muda. Unahusisha "fan-out" kwa wakala wengi na "fan-in" kukuza matokeo.

#### Muhtasari wa Hali

Mtumiaji anaomba kupanga safari kwenda Seattle.

1.  **Msambazaji (Fan-Out)**: Ombi la mtumiaji linatumwa kwa wakala wawili kwa wakati mmoja.
2.  **Wakala wa Utafiti**: Hufanya utafiti wa vivutio, hali ya hewa, na mambo muhimu ya safari ya Desemba Seattle.
3.  **Wakala wa Mpango**: Hutoa ratiba ya safari ya siku hadi siku kwa uhuru.
4.  **Mkusanyaji (Fan-In)**: Matokeo kutoka kwa mtafiti na mpangaji hukusanywa na kuwasilishwa pamoja kama matokeo ya mwisho.

*Mchoro wa workflow wa mtafiti na mpangaji wa wakati mmoja.*

#### Uchambuzi wa Utekelezaji wa Python

`ConcurrentBuilder` huweka kwa urahisi uundaji wa mfumo huu. Unaorodhesha wakala washiriki, na builder huunda kiotomatiki mantiki ya fan-out na fan-in.

```python
# 03.python-agent-framework-workflow-ghmodel-concurrent.ipynb

research_agent = chat_client.as_agent(name="Researcher-Agent", ...)
plan_agent = chat_client.as_agent(name="Plan-Agent", ...)

# ConcurrentBuilder inasimamia mantiki ya fan-out/fan-in
workflow = ConcurrentBuilder().participants([research_agent, plan_agent]).build()

# Endesha mtiririko wa kazi
events = await workflow.run("Plan a trip to Seattle in December")
```

Mfumo unahakikisha kuwa `research_agent` na `plan_agent` hufanya kazi kwa wakati mmoja, na matokeo yao ya mwisho hukusanywa kwenye orodha.

#### Uchambuzi wa Utekelezaji wa .NET (C#)

Katika .NET, mfumo huu unahitaji ufafanaji wazi zaidi. Watendaji maalum (`ConcurrentStartExecutor` na `ConcurrentAggregationExecutor`) huundwa kushughulikia mantiki ya fan-out na fan-in.

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

`WorkflowBuilder` hutumia `AddFanOutEdge` na `AddFanInEdge` kujenga grafu na watendaji maalum na wakala hao.

```csharp
// 03.dotnet-agent-framework-workflow-ghmodel-concurrent.ipynb

var workflow = new WorkflowBuilder(startExecutor)
            .AddFanOutEdge(startExecutor, targets: [researcherAgent, plannerAgent])
            .AddFanInEdge(aggregationExecutor, sources: [researcherAgent, plannerAgent])
            .WithOutputFrom(aggregationExecutor)
            .Build();
```

### Kesi 4: Workflow ya Masharti

Workflow za masharti huleta mantiki ya matawi, kuruhusu mfumo kuchukua njia tofauti kulingana na matokeo ya kati.

#### Muhtasari wa Hali

Workflow hii huunda otomatiki na kuchapisha somo la kiufundi.

1.  **Wakala wa Uenezi**: Huuandika rasimu ya somo kulingana na muhtasari na URL.
2.  **Mkaguzi wa Maudhui**: Hukagua rasimu. Anakagua kama idadi ya maneno ni zaidi ya maneno 200.
3.  **Tawi la Masharti**:
      * **Endapo Imetambuliwa (`Ndiyo`)**: Workflow inaendelea kwa `Publisher-Agent`.
      * **Endapo Haikutambuliwa (`Hapana`)**: Workflow inaisha na kutoa sababu ya kukataliwa.
4.  **Publisher-Agent**: ikiwa rasimu imethibitishwa, wakala huyu hutoa maudhui kwenye faili la Markdown.

#### Uchambuzi wa Utekelezaji wa Python

Mfano huu unatumia kazi maalum, `select_targets`, kutekeleza mantiki ya masharti. Kazi hii hupitishwa kwa `add_multi_selection_edge_group` na kuelekeza workflow kulingana na uwanja `review_result` kutoka kwa matokeo ya mkaguzi.

```python
# 04.python-agent-framework-workflow-aifoundry-condition.ipynb

# Kazi hii inaamua hatua inayofuata kulingana na matokeo ya ukaguzi
def select_targets(review: ReviewResult, target_ids: list[str]) -> list[str]:
    handle_review_id, save_draft_id = target_ids
    if review.review_result == "Yes":
        # Ikiidhinishwa, endelea kwa mtendaji 'save_draft'
        return [save_draft_id]
    else:
        # Ikiyekataliwa, endelea kwa mtendaji 'handle_review' kuripoti kushindwa
        return [handle_review_id]

# Mjenzi wa mtiririko wa kazi hutumia kazi ya uchaguzi kwa ajili ya upangaji njia
workflow = (
    WorkflowBuilder()
        .set_start_executor(evangelist_agent)
        .add_edge(evangelist_agent, reviewer_agent)
        .add_edge(reviewer_agent, to_reviewer_result)
        # Mkatazo wa uchaguzi wa wengi unatekeleza mantiki ya masharti
        .add_multi_selection_edge_group(
            to_reviewer_result,
            [handle_review, save_draft],
            selection_func=select_targets,
        )
        .add_edge(save_draft, publisher_agent)
        .build()
)
```

Watendaji maalum kama `to_reviewer_result` hutumiwa kusoma matokeo ya JSON kutoka kwa wakala na kuyageuza kuwa aina zenye nguvu ambazo kazi ya uchaguzi inaweza kuchunguza.

#### Uchambuzi wa Utekelezaji wa .NET (C#)

Toleo la .NET linatumia mbinu sawa na kazi ya masharti. `Func<object?, bool>` hutumiwa kukagua mali `Result` ya kitu cha `ReviewResult`.

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

Parameta `condition` ya `AddEdge` inaruhusu `WorkflowBuilder` kujenga njia ya matawi. Workflow itafuata mganano kwenda `publishExecutor` tu ikiwa hali `GetCondition(expectedResult: "Yes")` itarudi kweli. Vinginevyo, itafuata njia kwenda `sendReviewerExecutor`.

## Hitimisho

Microsoft Agent Framework Workflow hutoa msingi thabiti na rahisi kwa kupanga mifumo tata ya wakala wengi. Kwa kutumia usanifu wake wa msingi wa grafu na sehemu kuu, waendelezaji wanaweza kubuni na kutekeleza workflows tata katika Python na .NET. Iwe programu yako inahitaji usindikaji rahisi wa mfuatano, utekelezaji wa sambamba, au mantiki ya masharti yenye mabadiliko, mfumo huu unatoa zana za kujenga suluhisho zenye nguvu, zinazoweza kupanuka, na zilizo salama kwa aina zenye nguvu zenye nguvu za AI.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Kionyozo**:
Hati hii imetafsiriwa kwa kutumia huduma ya tafsiri ya AI [Co-op Translator](https://github.com/Azure/co-op-translator). Ingawa tunajitahidi kupata usahihi, tafadhali fahamu kwamba tafsiri za kiotomatiki zinaweza kuwa na makosa au upungufu wa usahihi. Hati ya asili katika lugha yake halisi inapaswa kuchukuliwa kama chanzo cha mamlaka. Kwa taarifa muhimu, tafsiri ya kitaalamu inayofanywa na binadamu inapendekezwa. Hatutojibu kwa kuelewa vibaya au tafsiri potofu zinazotokea kutokana na matumizi ya tafsiri hii.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->