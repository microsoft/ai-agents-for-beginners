# Mitmeagentsete rakenduste ehitamine Microsoft Agent Framework töövooga

See juhend juhendab teid mitmeagentsete rakenduste mõistmisel ja loomisel, kasutades Microsoft Agent Frameworki. Uurime mitmeagentsete süsteemide põhikontseptsioone, sukeldume raamistikus oleva töövoo komponendi arhitektuuri ning läbime praktilised näited nii Pythonis kui ka .NET-is erinevate töövoo mustrite puhul.

## 1\. Mitmeagentsete süsteemide mõistmine

Tehisintellekti agent on süsteem, mis ületab tavapärase suure keelemudeli (LLM) võimeid. Ta suudab tajuda oma keskkonda, teha otsuseid ja võtta samme kindlate eesmärkide saavutamiseks. Mitmeagentne süsteem hõlmab mitut sellist agenti, kes teevad koostööd probleemi lahendamiseks, mida ühe agendi üksinda lahendada on keeruline või võimatu.

### Levinumad rakendussituatsioonid

  * **Komplekssed probleemide lahendused**: Suure ülesande (nt ettevõtteürituse planeerimine) jagamine väiksemateks alamülesanneteks, mida haldavad spetsialiseeritud agendid (nt eelarveagent, logistikaagent, turundusagent).
  * **Virtuaalsed assistendid**: Põhijuhendaja agent, kes delegeerib ülesandeid nagu ajakava koostamine, uurimistöö ja broneerimine teistele spetsialiseerunud agentidele.
  * **Automatiseeritud sisu loomine**: Töövoog, kus üks agent koostab sisu mustandi, teine kontrollib selle täpsust ja stiili ning kolmas avaldab selle.

### Mitmeagentsed mustrid

Mitmeagentseid süsteeme saab korraldada mitmetes mustrites, mis määravad, kuidas nad omavahel suhtlevad:

  * **Järjestikune**: Agendid töötavad etteantud järjekorras, nagu konveieril. Ühe agendi väljundist saab järgmise sisend.
  * **Samaaegne**: Agendid töötavad paralleelselt erinevate ülesannete kallal ja nende tulemused koondatakse lõpuks.
  * **Tingimuslik**: Töövoog järgib erinevaid teid vastavalt ühe agendi väljundile, sarnaselt kui-siis-else tingimuslausel.

## 2\. Microsoft Agent Framework töövoo arhitektuur

Agent Frameworki töövoosüsteem on arenenud orkestreerimismootor, mis haldab keerukaid mitme agendi vahelist suhtlust. See põhineb graafipõhisel arhitektuuril, kasutades [Pregel-tüüpi täitmismudelit](https://kowshik.github.io/JPregel/pregel_paper.pdf), kus töötlemine toimub sünkroniseeritud sammudes, mida nimetatakse "supersteps" sammudeks.

### Põhikompidendid

Arhitektuur koosneb kolmest põhiosast:

1.  **Täiturid**: Need on põhilised töötlemise üksused. Meie näidetes on `Agent` tüüpi täitur. Igal täituril võib olla mitu sõnumikäsitlejat, mis kutsutakse automaatselt vastavalt vastuvõetud sõnumi tüübile.
2.  **Servad**: Need määravad sõnumite liikumisteed täiturite vahel. Servadel võivad olla tingimused, võimaldades dünaamilist info marsruutimist töövoo graafis.
3.  **Töövoog**: See komponent orkestreerib kogu protsessi, haldades täitureid, servi ja täitmise üldvoogu. Tagab sõnumite õigeaegse töötlemise ja sündmuste voogedastuse vaatlusvõimaluseks.

*Diagramm, mis illustreerib töövoosüsteemi põhikomponente.*

See struktuur võimaldab ehitada tugevaid ja skaleeritavaid rakendusi, kasutades põhimustena järjestikuseid ahelaid, fan-out/fan-in mustrit paralleeltöötluseks ning switch-case loogikat tingimusvoogude jaoks.

## 3\. Praktilised näited ja koodi analüüs

Vaatame nüüd, kuidas erinevaid töövoo mustreid raamistikus rakendada. Iga näite puhul vaatame nii Python kui .NET koodi.

### Juhul 1: Põhiline järjestikune töövoog

See on kõige lihtsam muster, kus ühe agendi väljund antakse otse teisele. Meie stsenaariumis teeb hotelli `FrontDesk` agent reisisoovituse, mida seejärel hindab `Concierge` agent.

*Diagramm lihtsast FrontDesk -\> Concierge töövoost.*

#### Stsenaariumi taust

Reisija palub soovitust Pariisis.

1.  `FrontDesk` agent, kes on paindlikke lihtsuse poolest, soovitab külastada Louvre muuseumi.
2.  `Concierge` agent, kes eelistab autentseid kogemusi, võtab selle soovituse vastu, hindab ja annab tagasisidet, pakkudes kohalikumat ja vähem turismi sihtkat alternatiivi.

#### Python'i rakenduse analüüs

Python näites määratleme ja loome esmalt kaks agenti, igaühel oma spetsiifilised juhised.

```python
# 01.python-agent-framework-workflow-ghmodel-basic.ipynb

# Määra agendi rollid ja juhised
REVIEWER_NAME = "Concierge"
REVIEWER_INSTRUCTIONS = """
    You are a hotel concierge who has opinions about providing the most local and authentic experiences for travelers...
    """

FRONTDESK_NAME = "FrontDesk"
FRONTDESK_INSTRUCTIONS = """
    You are a Front Desk Travel Agent with ten years of experience and are known for brevity...
    """

# Loo agendi instantsid
reviewer_agent = chat_client.as_agent(
    instructions=(REVIEWER_INSTRUCTIONS),
    name=REVIEWER_NAME,
)

front_desk_agent = chat_client.as_agent(
    instructions=(FRONTDESK_INSTRUCTIONS),
    name=FRONTDESK_NAME,
)
```

Seejärel kasutatakse `WorkflowBuilder`i graafi koostamiseks. `front_desk_agent` on määratud alguspunktiks ja serv ühendab selle väljundi `reviewer_agent`iga.

```python
# 01.python-agent-framework-töövoog-ghmudel-põhiline.ipynb

workflow = WorkflowBuilder(start_executor=front_desk_agent).add_edge(front_desk_agent, reviewer_agent).build()
```

Lõpuks käivitatakse töövoog algse kasutaja sisendiga.

```python
# 01.python-agent-framework-workflow-ghmodel-basic.ipynb

result =''
# run täidab töövoo; get_outputs() tagastab väljundite täitja tulemuse.
events = await workflow.run('I would like to go to Paris.')
outputs = events.get_outputs()
result = outputs[0].text if outputs else ''
```

#### .NET (C\#) rakenduse analüüs

.NET-i rakendus järgib sarnast loogikat. Esmalt määratletakse konstandid agentide nimede ja juhiste jaoks.

```csharp
// 01.dotnet-agent-framework-workflow-ghmodel-basic.ipynb

const string ReviewerAgentName = "Concierge";
const string ReviewerAgentInstructions = @"
    You are a hotel concierge who has opinions about providing the most local and authentic experiences for travelers...";

const string FrontDeskAgentName = "FrontDesk";
const string FrontDeskAgentInstructions = @"""
    You are a Front Desk Travel Agent with ten years of experience and are known for brevity...";
```

Agendid luuakse `AzureOpenAIClient` (Responses API) abil, seejärel `WorkflowBuilder` määrab järjestikulise voo, lisades servi `frontDeskAgent`ist `reviewerAgent`i.

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

Töövoog käivitatakse kasutaja sõnumiga ja tulemused voogedastatakse tagasi.

### Juhul 2: Mitmeastmeline järjestikune töövoog

See muster laiendab põhilist järjestust, kaasates rohkem agente. Sobib protsessidele, mis nõuavad mitut täpsustus- või teisendusetappi.

#### Stsenaariumi taust

Kasutaja esitab elutoa pildi ja küsib mööblitootjalt hinnapakkumist.

1.  **Sales-Agent**: Tuletab pildilt välja mööblitükid ja koostab nimekirja.
2.  **Price-Agent**: Võtab nimekirja ja annab detailse hinnajaotuse, hõlmates eelarvelisi, keskmise taseme ja premium variandid.
3.  **Quote-Agent**: Võtab hinnastatud nimekirja ja vormindab selle ametlikuks hinnapakkumiseks Markdowni formaadis.

*Diagramm Sales -\> Price -\> Quote töövoost.*

#### Python'i rakenduse analüüs

Määratletakse kolm agenti, igaüks oma spetsiifilise rolliga. Töövoog luuakse `add_edge` abil ahelana: `sales_agent` -\> `price_agent` -\> `quote_agent`.

```python
# 02.python-agent-framework-workflow-ghmodel-sequential.ipynb

# Loo kolm spetsialiseerunud agenti
sales_agent = chat_client.as_agent(...)
price_agent = chat_client.as_agent(...)
quote_agent = chat_client.as_agent(...)

# Ehita järjestikune töövoog
workflow = WorkflowBuilder(start_executor=sales_agent).add_edge(sales_agent, price_agent).add_edge(price_agent, quote_agent).build()
```

Sisendiks on `ChatMessage`, mis sisaldab nii teksti kui ka pildi URI-d. Raamistik haldab iga agendi väljundi edastamist järgmisele järjestuses, kuni lõpuks genereeritakse hinnapakkumine.

```python
# 02.python-agent-framework-workflow-ghmodel-sequential.ipynb

# Kasutaja sõnum sisaldab nii teksti kui pilti
message = ChatMessage(
        role=Role.USER,
        contents=[
            TextContent(text="Please find the relevant furniture..."),
            DataContent(uri=image_uri, media_type="image/png")
        ]
)

# Käivita töövoog
events = await workflow.run(message)
```

#### .NET (C\#) rakenduse analüüs

.NET näide peegeldab Pythoni versiooni. Luuakse kolm agenti (`salesagent`, `priceagent`, `quoteagent`) ja `WorkflowBuilder` ühendab need järjestatult.

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

Kasutaja sõnum koosneb nii pildiandmetest (baiti kujul) kui ka tekstilistest juhistest. `InProcessExecution.RunStreamingAsync` meetod käivitab töövoo ja lõplik väljund võetakse voost.

### Juhul 3: Samaaegne töövoog

Seda mustrit kasutatakse ülesannete samaaegseks täitmiseks aja säästmiseks. See sisaldab "fan-out" mitme agendi poole ja "fan-in" tulemuste kogumiseks.

#### Stsenaariumi taust

Kasutaja palub planeerida reisi Seattle'i.

1.  **Dispatcher (Fan-Out)**: Kasutaja päring saadetakse samaaegselt kahele agendile.
2.  **Researcher-Agent**: Uurib atraktsioonid, ilma- ja muud tähtsad aspektid detsembris Seattle'is.
3.  **Plan-Agent**: Loob sõltumatult üksikasjaliku päev-päevalt reisikava.
4.  **Aggregator (Fan-In)**: Kogub nii uurija kui ka planeerija väljundid ja esitab need koos lõpptulemuses.

*Diagramm samaaegsest Researcher ja Planner töövoost.*

#### Python'i rakenduse analüüs

`ConcurrentBuilder` lihtsustab selle mustri loomist. Kõik osalevad agendid loetletakse ja builder loob automaatselt vajaliku fan-out ja fan-in loogika.

```python
# 03.python-agent-framework-workflow-ghmodel-concurrent.ipynb

research_agent = chat_client.as_agent(name="Researcher-Agent", ...)
plan_agent = chat_client.as_agent(name="Plan-Agent", ...)

# ConcurrentBuilder haldab fan-out/fan-in loogikat
workflow = ConcurrentBuilder().participants([research_agent, plan_agent]).build()

# Käivita töövoog
events = await workflow.run("Plan a trip to Seattle in December")
```

Raamistik tagab, et `research_agent` ja `plan_agent` töötavad paralleelselt ning nende lõplikud väljundid kogutakse listina.

#### .NET (C\#) rakenduse analüüs

.NET-is nõuab see muster selgemat määratlust. Kohandatud täiturid (`ConcurrentStartExecutor` ja `ConcurrentAggregationExecutor`) luuakse fan-out ja fan-in loogika haldamiseks.

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

Seejärel kasutab `WorkflowBuilder` meetodeid `AddFanOutEdge` ja `AddFanInEdge` graafi ehitamiseks koos nende kohandatud täiturite ja agentidega.

```csharp
// 03.dotnet-agent-framework-workflow-ghmodel-concurrent.ipynb

var workflow = new WorkflowBuilder(startExecutor)
            .AddFanOutEdge(startExecutor, targets: [researcherAgent, plannerAgent])
            .AddFanInEdge(aggregationExecutor, sources: [researcherAgent, plannerAgent])
            .WithOutputFrom(aggregationExecutor)
            .Build();
```

### Juhul 4: Tingimuslik töövoog

Tingimuslikud töövood lisavad harustamisloogikat, võimaldades süsteemil võtta erinevaid radu vahetulemuste põhjal.

#### Stsenaariumi taust

See töövoog automatiseerib tehnilise juhendi loomise ja avaldamise.

1.  **Evangelist-Agent**: Kirjutab juhendi mustandi antud sisukorra ja URL-ide põhjal.
2.  **ContentReviewer-Agent**: Kontrollib mustandit. Kontrollib, kas sõnade arv on üle 200.
3.  **Tingimuslik haru**:
      * **Kui heaks kiidetud (`Jah`)**: Töövoog jätkub `Publisher-Agent`i juurde.
      * **Kui tagasi lükatud (`Ei`)**: Töövoog peatub ja tagastab tagasilükkamise põhjuse.
4.  **Publisher-Agent**: Kui mustand on heaks kiidetud, salvestab agent sisu Markdown faili.

#### Python'i rakenduse analüüs

Selles näites kasutatakse kohandatud funktsiooni `select_targets`, mis rakendab tingimusloogikat. See funktsioon antakse `add_multi_selection_edge_group` meetodile ja suunab töövoo vastavalt review tulemusväljadele (`review_result`).

```python
# 04.python-agent-framework-workflow-aifoundry-condition.ipynb

# See funktsioon määrab järgmise sammu ülevaatustulemuse põhjal
def select_targets(review: ReviewResult, target_ids: list[str]) -> list[str]:
    handle_review_id, save_draft_id = target_ids
    if review.review_result == "Yes":
        # Kui heaks kiidetud, liigu 'save_draft' täitjani
        return [save_draft_id]
    else:
        # Kui tagasi lükatud, liigu 'handle_review' täitjani ebaõnnestumise teatamiseks
        return [handle_review_id]

# Töövoo koostaja kasutab marsruutimiseks valikufunktsiooni
workflow = (
    WorkflowBuilder()
        .set_start_executor(evangelist_agent)
        .add_edge(evangelist_agent, reviewer_agent)
        .add_edge(reviewer_agent, to_reviewer_result)
        # Mitme valiku serv rakendab tingimusloogikat
        .add_multi_selection_edge_group(
            to_reviewer_result,
            [handle_review, save_draft],
            selection_func=select_targets,
        )
        .add_edge(save_draft, publisher_agent)
        .build()
)
```

Kohandatud täiturid nagu `to_reviewer_result` analüüsivad agentide JSON-väljundeid ja teisendavad need tugevalt tüübistatavateks objektideks, mida valikufunktsioon saab kontrollida.

#### .NET (C\#) rakenduse analüüs

.NET versioon kasutab sarnast lähenemist tingimuse funktsiooniga. Määratletakse `Func<object?, bool>`, mis kontrollib `ReviewResult` objekti `Result` omadust.

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

`AddEdge` meetodi `condition` parameeter võimaldab `WorkflowBuilder`il luua harustamise tee. Töövoog järgib servi `publishExecutor` juurde ainult, kui tingimus `GetCondition(expectedResult: "Yes")` on täidetud. Vastasel juhul järgib rada `sendReviewerExecutor` suunda.

## Kokkuvõte

Microsoft Agent Framework Workflow pakub tugevat ja paindlikku alust keerukate mitmeagentsete süsteemide orkestreerimiseks. Pidades silmas selle graafipõhist arhitektuuri ja põhikomponente, saavad arendajad kavandada ja rakendada keerukaid töövooge nii Pythonis kui ka .NET-is. Kas teie rakendus vajab lihtsat järjestikust töötlemist, paralleelset täitmist või dünaamilist tingimusloogikat, raamistik pakub tööriistu võimaste, skaleeritavate ja tüübikindlate tehisintellekti lahenduste loomiseks.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Lahtiütlus**:
See dokument on tõlgitud kasutades AI tõlketeenust [Co-op Translator](https://github.com/Azure/co-op-translator). Kuigi me püüdleme täpsuse poole, palun pange tähele, et automatiseeritud tõlgetes võib esineda vigu või ebatäpsusi. Originaaldokument selle emakeeles tuleks pidada autoriteetseks allikaks. Olulise teabe puhul soovitatakse kasutada professionaalset inimtõlget. Me ei vastuta selle tõlkega seotud eksimustest või valesti mõistmistest.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->