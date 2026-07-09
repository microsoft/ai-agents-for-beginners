# Kujenga Programu za Wakala wengi kwa Kutumia Microsoft Agent Framework Workflow

Mafunzo haya yatakuongoza kuelewa na kujenga programu za wakala wengi kwa kutumia Microsoft Agent Framework. Tutachunguza dhana kuu za mifumo ya wakala wengi, tazame usanifu wa kipengele cha Workflow cha mfumo huo, na kupitia mifano ya vitendo kwa Python na .NET kwa mifumo tofauti ya workflow.

## 1\. Kuelewa Mifumo ya Wakala Wengi

Wakala wa AI ni mfumo unaozidi uwezo wa Mfano wa Lugha Kubwa (LLM) wa kawaida. Inaweza kuona mazingira yake, kufanya maamuzi, na kuchukua hatua kufikia malengo maalum. Mfumo wa wakala wengi unahusisha wakala kadhaa wanaoshirikiana kutatua tatizo ambalo lingekuwa gumu au lisilowezekana kwa wakala mmoja kughandle pekee.

### Mifano ya Maombi ya Kawaida

  * **Kutatua Tatizo Changamu**: Kuvunjisha jukumu kubwa (mfano, kupanga tukio la kampuni nzima) katika vitendo vidogo vinavyoshughulikiwa na wakala maalum (mfano, wakala wa bajeti, wakala wa usafirishaji, wakala wa masoko).
  * **Msaidizi wa Mtandao**: Mwakala mkuu anayeagiza kazi kama kupanga ratiba, utafiti, na uhifadhi kwa wakala wengine maalum.
  * **Uundaji wa Maudhui Kiotomatiki**: Workflow ambapo wakala mmoja anatayarisha maudhui, mwingine anaridhia kwa usahihi na ladha, na wa tatu huchapisha.

### Mifano ya Wakala Wengi

Mifumo ya wakala wengi inaweza kupanga katika mifano kadhaa, ambayo huamua jinsi wanavyoshirikiana:

  * **Mfuatano**: Wakala hufanya kazi kwa mpangilio uliowekwa, kama kwenye mstari wa mkusanyiko. Matokeo ya wakala mmoja yanakuwa pembejeo kwa wakala inayofuata.
  * **Simultaneous**: Wakala hufanya kazi kwa wakati mmoja juu ya sehemu tofauti za kazi, na matokeo yao hukusanywa mwishoni.
  * **Masharti**: Workflow hufuata njia tofauti kulingana na matokeo ya wakala, kama taarifa ya if-then-else.

## 2\. Usanifu wa Microsoft Agent Framework Workflow

Mfumo wa workflow wa Agent Framework ni injini ya hali ya juu ya upangaji wa michakato iliyoundwa kusimamia mwingiliano tata kati ya wakala wengi. Umejengwa kwenye usanifu wa grafu unaotumia [mfano wa utekelezaji wa mtindo wa Pregel](https://kowshik.github.io/JPregel/pregel_paper.pdf), ambapo usindikaji hufanyika kwa hatua zinazoratibiwa zinazojulikana kama "supersteps."

### Vipengele Vikuu

Usanifu unajumuisha sehemu kuu tatu:

1.  **Watekelezaji**: Hizi ni vitengo vya msingi vya usindikaji. Katika mifano yetu, `Agent` ni aina ya mtekelezaji. Kila mtekelezaji anaweza kuwa na wasimamizi wa jumbe kadhaa wanaoitwa moja kwa moja kulingana na aina ya ujumbe unaopokelewa.
2.  **Mikondo**: Hizi huainisha njia ambayo jumbe husafiri kati ya watekelezaji. Mikondo inaweza kuwa na masharti, ambayo huruhusu uelekeo wa taarifa kwa nguvu kupitia grafu ya workflow.
3.  **Workflow**: Kipengele hiki husimamia mchakato mzima, kusimamia watekelezaji, mikondo, na mtiririko mzima wa utekelezaji. Inahakikisha jumbe zinashughulikiwa kwa mpangilio sahihi na kusambaza matukio kwa ajili ya uangalizi.

*Mchoro unaoonyesha vipengele kuu vya mfumo wa workflow.*

Muundo huu unaruhusu kujenga programu zenye nguvu na zinazoweza kupanuka kwa kutumia mifano ya msingi kama mikondo ya mfuatano, fan-out/fan-in kwa usindikaji sambamba, na mantiki ya switch-case kwa mikondo yenye masharti.

## 3\. Mifano ya Vitendo na Uchambuzi wa Msimbo

Sasa, tuchunguze jinsi ya kutekeleza mifano tofauti ya workflow kwa kutumia mfumo huu. Tutaangalia msimbo wa Python na .NET kwa kila mfano.

### Kesi 1: Workflow ya Mfuatano wa Msingi

Huu ni mfano rahisi zaidi, ambapo matokeo ya wakala mmoja hupitishwa moja kwa moja kwa mwingine. Hali yetu ni wakala wa hoteli `FrontDesk` anayetoa ushauri wa safari, halafu wakala wa `Concierge` anauguzia ushauri huo.

*Mchoro wa workflow wa FrontDesk -\> Concierge ya msingi.*

#### Maelezo ya Hali

Mtembeleaji anaomba ushauri mjini Paris.

1.  Wakala `FrontDesk`, aliyeundwa kwa ufupi, anapendekeza kutembelea Jumba la sanaa la Louvre.
2.  Wakala `Concierge`, anayethamini uzoefu halisi, anapokea pendekezo hilo. Anakagua ushauri na kutoa maoni, akipendekeza mbadala wa maeneo ya karibu, yasiyokuwa maarufu kwa watalii.

#### Uchambuzi wa Utekelezaji wa Python

Katika mfano wa Python, kwanza tunaeleza na kuunda wakala wawili, kila mmoja na maagizo maalum.

```python
# 01.python-agent-framework-workflow-ghmodel-basic.ipynb

# Eleza majukumu ya mawakala na maagizo
REVIEWER_NAME = "Concierge"
REVIEWER_INSTRUCTIONS = """
    You are an are hotel concierge who has opinions about providing the most local and authentic experiences for travelers...
    """

FRONTDESK_NAME = "FrontDesk"
FRONTDESK_INSTRUCTIONS = """
    You are a Front Desk Travel Agent with ten years of experience and are known for brevity...
    """

# Unda mfano wa mawakala
reviewer_agent = chat_client.as_agent(
    instructions=(REVIEWER_INSTRUCTIONS),
    name=REVIEWER_NAME,
)

front_desk_agent = chat_client.as_agent(
    instructions=(FRONTDESK_INSTRUCTIONS),
    name=FRONTDESK_NAME,
)
```

Kisha, `WorkflowBuilder` hutumiwa kujenga grafu. `front_desk_agent` imesanidiwa kuwa sehemu ya mwanzo, na mkondo umeundwa kuunganisha matokeo yake na `reviewer_agent`.

```python
# 01.python-agent-framework-workflow-ghmodel-basic.ipynb

workflow = WorkflowBuilder(start_executor=front_desk_agent).add_edge(front_desk_agent, reviewer_agent).build()
```

Mwishowe, workflow inaendeshwa kwa agizo la mtumiaji la awali.

```python
# 01.python-agent-framework-workflow-ghmodel-basic.ipynb

result =''
# run inatekeleza mchakato; get_outputs() inarudisha matokeo ya mtendaji wa pato.
events = await workflow.run('I would like to go to Paris.')
outputs = events.get_outputs()
result = outputs[0].text if outputs else ''
```

#### Uchambuzi wa Utekelezaji wa .NET (C\#)

Utekelezaji wa .NET unafuata mantiki sawa kabisa. Kwanza, vigezo vinatolewa kwa majina na maagizo ya wakala.

```csharp
// 01.dotnet-agent-framework-workflow-ghmodel-basic.ipynb

const string ReviewerAgentName = "Concierge";
const string ReviewerAgentInstructions = @"
    You are an are hotel concierge who has opinions about providing the most local and authentic experiences for travelers...";

const string FrontDeskAgentName = "FrontDesk";
const string FrontDeskAgentInstructions = @"""
    You are a Front Desk Travel Agent with ten years of experience and are known for brevity...";
```

Wakala wanaundwa kwa kutumia `AzureOpenAIClient` (API ya Majibu), halafu `WorkflowBuilder` huweka mfuatano kwa kuongeza mkondo kutoka `frontDeskAgent` hadi `reviewerAgent`.

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

Workflow inaendeshwa kwa ujumbe wa mtumiaji, na matokeo hutiririshwa kurudi.

### Kesi 2: Workflow ya Mfuatano wa Hatua Nyingi

Mfano huu unaongezea mfuatano wa msingi kwa kuhusisha wakala zaidi. Ni bora kwa michakato inayohitaji hatua kadhaa za marekebisho au mabadiliko.

#### Maelezo ya Hali

Mtumiaji anatoa picha ya chumba cha kuishi na anaomba nukuu ya samani.

1.  **Mwakala wa Mauzo**: Hutatua vitu vya samani kwenye picha na kutengeneza orodha.
2.  **Mwakala wa Bei**: Anapokea orodha ya vitu na kutoa mgawanyo wa bei kwa undani, pamoja na bajeti, kiwango cha kati, na chaguzi za hali ya juu.
3.  **Mwakala wa Nukuu**: Anapokea orodha iliyopimwa bei na kuifanya kuwa hati rasmi ya nukuu katika Markdown.

*Mchoro wa workflow wa Mauzo -\> Bei -\> Nukuu.*

#### Uchambuzi wa Utekelezaji wa Python

Wakala watatu wameelezwa, kila mmoja na jukumu maalum. Workflow inajengwa kwa kutumia `add_edge` kuunda mfuatano: `sales_agent` -\> `price_agent` -\> `quote_agent`.

```python
# 02.python-agent-framework-workflow-ghmodel-sequential.ipynb

# Unda maajenti maalum watatu
sales_agent = chat_client.as_agent(...)
price_agent = chat_client.as_agent(...)
quote_agent = chat_client.as_agent(...)

# Jenga mtiririko wa kazi wa mfululizo
workflow = WorkflowBuilder(start_executor=sales_agent).add_edge(sales_agent, price_agent).add_edge(price_agent, quote_agent).build()
```

Ingizo ni `ChatMessage` inayojumuisha maandishi na URI ya picha. Mfumo hushughulikia kupitisha matokeo ya kila wakala kwa wakala anayefuata katika mfuatano hadi nukuu ya mwisho itengenezwe.

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

#### Uchambuzi wa Utekelezaji wa .NET (C\#)

Mfano wa .NET unaiga toleo la Python. Wakala watatu (`salesagent`, `priceagent`, `quoteagent`) wanaundwa. `WorkflowBuilder` hukunga mfuatano wao.

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

Ujumbe wa mtumiaji unaandaliwa na data ya picha (kama bytes) na agizo la maandishi. Njia `InProcessExecution.StreamAsync` huanzisha workflow, na matokeo ya mwisho yanakamatwa kutoka kwenye mto.

### Kesi 3: Workflow Sambamba

Mfano huu hutumiwa wakati kazi zinaweza kufanywa kwa wakati mmoja ili kuokoa muda. Inahusisha "fan-out" kwa wakala wengi na "fan-in" kukusanya matokeo.

#### Maelezo ya Hali

Mtumiaji anaomba kupanga ziara ya kwenda Seattle.

1.  **Mfanyakazi wa Usambazaji (Fan-Out)**: Ombi la mtumiaji linatumwa kwa wakala wawili kwa wakati mmoja.
2.  **Mwakala wa Utafiti**: Hufanya utafiti wa vivutio, hali ya hewa, na mambo muhimu kwa safari Seattle Desemba.
3.  **Mwakala wa Mipango**: Huatengeneza ratiba ya safari ya siku kwa siku.
4.  **Mkusanyaji (Fan-In)**: Matokeo ya mtaalamu wa utafiti na mpangaji hukusanywa na kuwasilishwa pamoja kama matokeo ya mwisho.

*Mchoro wa workflow sambamba wa Mtaalamu wa Utafiti na Mpangaji.*

#### Uchambuzi wa Utekelezaji wa Python

`ConcurrentBuilder` hurahisisha uundaji wa mfano huu. Unataja wakala waliohusika, na builder huunda moja kwa moja mantiki ya fan-out na fan-in inayohitajika.

```python
# 03.python-agent-framework-workflow-ghmodel-concurrent.ipynb

research_agent = chat_client.as_agent(name="Researcher-Agent", ...)
plan_agent = chat_client.as_agent(name="Plan-Agent", ...)

# ConcurrentBuilder hushughulikia mantiki ya usambazaji/ukusanyaji
workflow = ConcurrentBuilder().participants([research_agent, plan_agent]).build()

# Endesha mtiririko wa kazi
events = await workflow.run("Plan a trip to Seattle in December")
```

Mfumo huhakiki kwamba `research_agent` na `plan_agent` hufanya kazi sambamba, na matokeo yao ya mwisho hukusanywa kwenye orodha.

#### Uchambuzi wa Utekelezaji wa .NET (C\#)

Katika .NET, mfano huu unahitaji ufafanuzi zaidi wazi. Watendaji maalum (`ConcurrentStartExecutor` na `ConcurrentAggregationExecutor`) huundwa kushughulikia mantiki ya fan-out na fan-in.

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

Kisha `WorkflowBuilder` hutumia `AddFanOutEdge` na `AddFanInEdge` kujenga grafu na watendaji hawa maalum na wakala.

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

#### Maelezo ya Hali

Workflow hii inaotomatisha uundaji na uchapishaji wa mafunzo ya kiufundi.

1.  **Mwakala Mtangazaji**: Anaandika rasimu ya mafunzo kulingana na muhtasari na URL zilizotolewa.
2.  **Mwakala Mhakiki wa Maudhui**: Anakagua rasimu. Anakagua kama maneno yamezidi 200.
3.  **Tawi la Masharti**:
      * **Ikiidhinishwa (`Ndiyo`)**: Workflow inaendelea hadi `Mwakala Mchapishaji`.
      * **Ikiyekataliwa (`Hapana`)**: Workflow inasimama na kutoa sababu ya kukataliwa.
4.  **Mwakala Mchapishaji**: Ikiwa rasimu imeidhinishwa, wakala huyu anaweka maudhui kwenye faili la Markdown.

#### Uchambuzi wa Utekelezaji wa Python

Mfano huu hutumia kazi maalum, `select_targets`, kutekeleza mantiki ya masharti. Kazi hii hupitishwa kwa `add_multi_selection_edge_group` na inaelekeza workflow kulingana na uwanja wa `review_result` kutoka matokeo ya mhakiki.

```python
# 04.python-agent-framework-workflow-aifoundry-condition.ipynb

# Kazi hii inabainisha hatua inayofuata kulingana na matokeo ya ukaguzi
def select_targets(review: ReviewResult, target_ids: list[str]) -> list[str]:
    handle_review_id, save_draft_id = target_ids
    if review.review_result == "Yes":
        # Ikiidhinishwa, endelea na mtendaji wa 'save_draft'
        return [save_draft_id]
    else:
        # Ikiukubaliwa, endelea na mtendaji wa 'handle_review' ili kuripoti kushindwa
        return [handle_review_id]

# Mjenzi wa mtiririko wa kazi hutumia kazi ya uteuzi kwa ajili ya kupanga njia
workflow = (
    WorkflowBuilder()
        .set_start_executor(evangelist_agent)
        .add_edge(evangelist_agent, reviewer_agent)
        .add_edge(reviewer_agent, to_reviewer_result)
        # Mfinyazo wa uteuzi wa wengi hutekeleza mantiki ya masharti
        .add_multi_selection_edge_group(
            to_reviewer_result,
            [handle_review, save_draft],
            selection_func=select_targets,
        )
        .add_edge(save_draft, publisher_agent)
        .build()
)
```

Watendaji maalum kama `to_reviewer_result` hutumiwa kutafsiri matokeo ya JSON kutoka kwa wakala na kuyageuza kuwa vitu vyenye aina thabiti ambavyo kazi ya uteuzi inaweza kuchunguza.

#### Uchambuzi wa Utekelezaji wa .NET (C\#)

Toleo la .NET linatumia njia sawa na kazi ya masharti. `Func<object?, bool>` imetengenezwa kuchunguza mali `Result` ya kitu cha `ReviewResult`.

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

Kigezo cha `condition` cha njia ya `AddEdge` huruhusu `WorkflowBuilder` kuunda njia ya matawi. Workflow itafuata mkondo hadi `publishExecutor` ikiwa sharti `GetCondition(expectedResult: "Yes")` litarejea kweli. Vinginevyo, itafuata njia hadi `sendReviewerExecutor`.

## Hitimisho

Microsoft Agent Framework Workflow hutoa msingi thabiti na rahisi kwa kupanga mifumo tata ya wakala wengi. Kwa kutumia usanifu wake wa grafu na vipengele vikuu, watengenezaji wanaweza kubuni na kutekeleza workflow za hali ya juu katika Python na .NET. Iwe programu yako inahitaji usindikaji rahisi wa mfuatano, utekelezaji sambamba, au mantiki ya masharti yenye nguvu, mfumo huu unatoa zana za kujenga suluhisho zenye nguvu, zinazoweza kupanuka, na salama kwa aina za AI.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Kionyozo**:
Hati hii imetafsiriwa kwa kutumia huduma ya tafsiri ya AI [Co-op Translator](https://github.com/Azure/co-op-translator). Ingawa tunajitahidi kupata usahihi, tafadhali fahamu kwamba tafsiri za kiotomatiki zinaweza kuwa na makosa au upungufu wa usahihi. Hati ya asili katika lugha yake halisi inapaswa kuchukuliwa kama chanzo cha mamlaka. Kwa taarifa muhimu, tafsiri ya kitaalamu inayofanywa na binadamu inapendekezwa. Hatutojibu kwa kuelewa vibaya au tafsiri potofu zinazotokea kutokana na matumizi ya tafsiri hii.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->