<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "b39c052ef109db90ad9251183791e2d6",
  "translation_date": "2025-10-11T11:09:44+00:00",
  "source_file": "08-multi-agent/code_samples/workflows-agent-framework/README.md",
  "language_code": "et"
}
-->
# Mitmeagendiliste rakenduste loomine Microsoft Agent Framework Workflow abil

See juhend aitab teil mõista ja luua mitmeagendilisi rakendusi, kasutades Microsoft Agent Frameworki. Uurime mitmeagendiliste süsteemide põhikontseptsioone, süveneme raamistikus Workflow komponendi arhitektuuri ning läbime praktilisi näiteid nii Pythonis kui .NET-is erinevate töövoomustrite jaoks.

## 1\. Mitmeagendiliste süsteemide mõistmine

Tehisintellekti agent on süsteem, mis ületab standardse suure keelemudeli (LLM) võimekuse. See suudab tajuda oma keskkonda, teha otsuseid ja võtta meetmeid konkreetsete eesmärkide saavutamiseks. Mitmeagendiline süsteem hõlmab mitut sellist agenti, kes teevad koostööd, et lahendada probleeme, mida üksik agent ei suudaks lahendada.

### Levinud rakendusstsenaariumid

  * **Komplekssete probleemide lahendamine**: Suure ülesande (nt ettevõtteürituse planeerimine) jagamine väiksemateks alamülesanneteks, mida käsitlevad spetsialiseeritud agendid (nt eelarveagent, logistikaagent, turundusagent).
  * **Virtuaalsed assistendid**: Peamine assistentagent, kes delegeerib ülesandeid, nagu ajakava koostamine, uurimistöö ja broneerimine, teistele spetsialiseeritud agentidele.
  * **Automatiseeritud sisuloome**: Töövoog, kus üks agent koostab sisu, teine kontrollib selle täpsust ja tooni ning kolmas avaldab selle.

### Mitmeagendilised mustrid

Mitmeagendilised süsteemid võivad olla organiseeritud mitmel viisil, mis määravad nendevahelise suhtluse:

  * **Järjestikune**: Agendid töötavad etteantud järjekorras, nagu tootmisliinil. Ühe agendi väljund muutub järgmise agendi sisendiks.
  * **Paralleelne**: Agendid töötavad samaaegselt erinevate ülesande osade kallal ning nende tulemused koondatakse lõpus.
  * **Tingimuslik**: Töövoog järgib erinevaid teid, sõltuvalt agendi väljundist, sarnaselt if-then-else loogikale.

## 2\. Microsoft Agent Framework Workflow arhitektuur

Agent Frameworki töövoosüsteem on täiustatud orkestreerimismootor, mis on loodud mitmeagendiliste keerukate interaktsioonide haldamiseks. See põhineb graafipõhisel arhitektuuril, mis kasutab [Pregel-stiilis täitmisloogikat](https://kowshik.github.io/JPregel/pregel_paper.pdf), kus töötlemine toimub sünkroniseeritud sammudes, mida nimetatakse "superetappideks".

### Põhikomponendid

Arhitektuur koosneb kolmest peamisest osast:

1.  **Täitjad**: Need on põhilised töötlemisüksused. Meie näidetes on `Agent` täitja tüüp. Igal täitjal võib olla mitu sõnumikäsitlust, mis käivitatakse automaatselt vastavalt saadud sõnumi tüübile.
2.  **Servad**: Need määravad tee, mida mööda sõnumid täitjate vahel liiguvad. Servadel võivad olla tingimused, mis võimaldavad dünaamilist teabe suunamist töövoo graafis.
3.  **Töövoog**: See komponent orkestreerib kogu protsessi, hallates täitjaid, servi ja üldist täitmisvoogu. See tagab, et sõnumid töödeldakse õiges järjekorras ja voogesitab sündmusi jälgitavuse jaoks.

*Diagramm, mis illustreerib töövoosüsteemi põhikomponente.*

See struktuur võimaldab luua vastupidavaid ja skaleeritavaid rakendusi, kasutades põhimustreid nagu järjestikused ahelad, fan-out/fan-in paralleelseks töötlemiseks ja switch-case loogikat tingimuslike voogude jaoks.

## 3\. Praktilised näited ja koodianalüüs

Nüüd uurime, kuidas rakendada erinevaid töövoomustreid, kasutades raamistikku. Vaatame iga näite jaoks nii Pythonis kui .NET-is koodi.

### Juhtum 1: Põhiline järjestikune töövoog

See on lihtsaim muster, kus ühe agendi väljund edastatakse otse teisele. Meie stsenaarium hõlmab hotelli `FrontDesk` agenti, kes teeb reisisoovituse, mida seejärel hindab `Concierge` agent.

*Diagramm FrontDesk -\> Concierge töövoost.*

#### Stsenaariumi taust

Reisija küsib soovitust Pariisis.

1.  `FrontDesk` agent, kes eelistab lühidust, soovitab külastada Louvre'i muuseumi.
2.  `Concierge` agent, kes eelistab autentseid kogemusi, võtab selle soovituse vastu. Ta hindab soovitust ja pakub tagasisidet, soovitades kohalikumat ja vähem turistiderohket alternatiivi.

#### Python-i rakenduse analüüs

Python-i näites määratleme ja loome esmalt kaks agenti, igaühel konkreetsed juhised.

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

Seejärel kasutatakse `WorkflowBuilder`-it graafi loomiseks. `front_desk_agent` määratakse alguspunktiks ja serv luuakse, et ühendada selle väljund `reviewer_agent`-iga.

```python
# 01.python-agent-framework-workflow-ghmodel-basic.ipynb

workflow = WorkflowBuilder().set_start_executor(front_desk_agent).add_edge(front_desk_agent, reviewer_agent).build()
```

Lõpuks käivitatakse töövoog algse kasutaja sisendiga.

```python
# 01.python-agent-framework-workflow-ghmodel-basic.ipynb

result =''
# The run_stream method executes the workflow and streams events.
async for event in workflow.run_stream('I would like to go to Paris.'):
    if isinstance(event, WorkflowEvent):
        result += str(event.data)
```

#### .NET (C#) rakenduse analüüs

.NET-i rakendus järgib väga sarnast loogikat. Kõigepealt määratakse agentide nimed ja juhised konstantidena.

```csharp
// 01.dotnet-agent-framework-workflow-ghmodel-basic.ipynb

const string ReviewerAgentName = "Concierge";
const string ReviewerAgentInstructions = @"
    You are an are hotel concierge who has opinions about providing the most local and authentic experiences for travelers...";

const string FrontDeskAgentName = "FrontDesk";
const string FrontDeskAgentInstructions = @"""
    You are a Front Desk Travel Agent with ten years of experience and are known for brevity...";
```

Agendid luuakse `OpenAIClient` abil ning seejärel määratleb `WorkflowBuilder` järjestikuse voo, lisades serva `frontDeskAgent`-ist `reviewerAgent`-ile.

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

Töövoog käivitatakse kasutaja sõnumiga ja tulemused voogesitatakse tagasi.

### Juhtum 2: Mitmeastmeline järjestikune töövoog

See muster laiendab põhilist järjestikust voogu, lisades rohkem agente. See sobib ideaalselt protsesside jaoks, mis vajavad mitut etappi täpsustamiseks või ümberkujundamiseks.

#### Stsenaariumi taust

Kasutaja esitab elutoa pildi ja palub mööbli hinnapakkumist.

1.  **Sales-Agent**: Tuvastab pildil mööbliesemed ja koostab nimekirja.
2.  **Price-Agent**: Võtab nimekirja ja annab üksikasjaliku hinnajaotuse, sealhulgas eelarve-, keskmise ja premium-valikud.
3.  **Quote-Agent**: Võtab hinnatud nimekirja ja vormindab selle ametlikuks hinnapakkumise dokumendiks Markdownis.

*Diagramm Sales -\> Price -\> Quote töövoost.*

#### Python-i rakenduse analüüs

Kolm agenti määratletakse, igaüks oma spetsialiseeritud rolliga. Töövoog konstrueeritakse `add_edge` abil, et luua ahel: `sales_agent` -\> `price_agent` -\> `quote_agent`.

```python
# 02.python-agent-framework-workflow-ghmodel-sequential.ipynb

# Create three specialized agents
sales_agent = chat_client.create_agent(...)
price_agent = chat_client.create_agent(...)
quote_agent = chat_client.create_agent(...)

# Build the sequential workflow
workflow = WorkflowBuilder().set_start_executor(sales_agent).add_edge(sales_agent, price_agent).add_edge(price_agent, quote_agent).build()
```

Sisend on `ChatMessage`, mis sisaldab nii teksti kui ka pildi URI-d. Raamistik haldab iga agendi väljundi edastamist järgmisele järjestuses, kuni lõplik hinnapakkumine on genereeritud.

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

#### .NET (C#) rakenduse analüüs

.NET-i näide peegeldab Python-i versiooni. Kolm agenti (`salesagent`, `priceagent`, `quoteagent`) luuakse. `WorkflowBuilder` ühendab need järjestikku.

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

Kasutaja sõnum konstrueeritakse nii pildiga (baitidena) kui ka tekstilise sisendiga. `InProcessExecution.StreamAsync` meetod käivitab töövoo ja lõplik väljund salvestatakse voost.

### Juhtum 3: Paralleelne töövoog

See muster kasutatakse, kui ülesandeid saab samaaegselt täita, et säästa aega. See hõlmab "fan-out" mitmele agendile ja "fan-in" tulemuste koondamiseks.

#### Stsenaariumi taust

Kasutaja palub planeerida reisi Seattle'isse.

1.  **Dispatcher (Fan-Out)**: Kasutaja päring saadetakse samaaegselt kahele agendile.
2.  **Researcher-Agent**: Uurib vaatamisväärsusi, ilma ja olulisi kaalutlusi Seattle'i külastamiseks detsembris.
3.  **Plan-Agent**: Koostab iseseisvalt üksikasjaliku päevapõhise reisikava.
4.  **Aggregator (Fan-In)**: Mõlema agendi väljundid kogutakse ja esitatakse koos lõpptulemusena.

*Diagramm paralleelsest Researcher ja Planner töövoost.*

#### Python-i rakenduse analüüs

`ConcurrentBuilder` lihtsustab selle mustri loomist. Loetletakse osalevad agendid ja ehitaja loob automaatselt vajaliku fan-out ja fan-in loogika.

```python
# 03.python-agent-framework-workflow-ghmodel-concurrent.ipynb

research_agent = chat_client.create_agent(name="Researcher-Agent", ...)
plan_agent = chat_client.create_agent(name="Plan-Agent", ...)

# ConcurrentBuilder handles the fan-out/fan-in logic
workflow = ConcurrentBuilder().participants([research_agent, plan_agent]).build()

# Run the workflow
events = await workflow.run("Plan a trip to Seattle in December")
```

Raamistik tagab, et `research_agent` ja `plan_agent` töötavad paralleelselt ning nende lõplikud väljundid kogutakse loendisse.

#### .NET (C#) rakenduse analüüs

.NET-is nõuab see muster täpsemat määratlust. Kohandatud täitjad (`ConcurrentStartExecutor` ja `ConcurrentAggregationExecutor`) luuakse fan-out ja fan-in loogika haldamiseks.

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

Seejärel kasutab `WorkflowBuilder` `AddFanOutEdge` ja `AddFanInEdge`, et ehitada graaf nende kohandatud täitjate ja agentidega.

```csharp
// 03.dotnet-agent-framework-workflow-ghmodel-concurrent.ipynb

var workflow = new WorkflowBuilder(startExecutor)
            .AddFanOutEdge(startExecutor, targets: [researcherAgent, plannerAgent])
            .AddFanInEdge(aggregationExecutor, sources: [researcherAgent, plannerAgent])
            .WithOutputFrom(aggregationExecutor)
            .Build();
```

### Juhtum 4: Tingimuslik töövoog

Tingimuslikud töövood lisavad hargnemisloogikat, võimaldades süsteemil võtta erinevaid teid, sõltuvalt vahepealsetest tulemustest.

#### Stsenaariumi taust

See töövoog automatiseerib tehnilise juhendi loomise ja avaldamise.

1.  **Evangelist-Agent**: Koostab juhendi mustandi, lähtudes antud ülevaatest ja URL-idest.
2.  **ContentReviewer-Agent**: Hindab mustandit. Kontrollib, kas sõnade arv ületab 200.
3.  **Tingimuslik haru**:
      * **Kui heaks kiidetud (`Yes`)**: Töövoog jätkub `Publisher-Agent`-iga.
      * **Kui tagasi lükatud (`No`)**: Töövoog peatub ja väljastab tagasilükkamise põhjuse.
4.  **Publisher-Agent**: Kui mustand on heaks kiidetud, salvestab see agent sisu Markdown-faili.

#### Python-i rakenduse analüüs

Selles näites kasutatakse kohandatud funktsiooni `select_targets`, et rakendada tingimuslikku loogikat. See funktsioon edastatakse `add_multi_selection_edge_group`-ile ja suunab töövoo, lähtudes `review_result` väljundist.

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

Kohandatud täitjad, nagu `to_reviewer_result`, kasutatakse JSON-väljundi analüüsimiseks agentidelt ja selle teisendamiseks tugevalt tüpiseeritud objektideks, mida valikufunktsioon saab kontrollida.

#### .NET (C#) rakenduse analüüs

.NET-i versioon kasutab sarnast lähenemist tingimusfunktsiooniga. Määratletakse `Func<object?, bool`, et kontrollida `ReviewResult` objekti `Result` omadust.

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

`AddEdge` meetodi `condition` parameeter võimaldab `WorkflowBuilder`-il luua hargnemistee. Töövoog järgib serva `publishExecutor`-ile ainult siis, kui tingimus `GetCondition(expectedResult: "Yes")` tagastab true. Vastasel juhul järgib see teed `sendReviewerExecutor`-ile.

## Kokkuvõte

Microsoft Agent Framework Workflow pakub tugevat ja paindlikku alust keerukate mitmeagendiliste süsteemide orkestreerimiseks. Kasutades selle graafipõhist arhitektuuri ja põhikomponente, saavad arendajad kujundada ja rakendada keerukaid töövooge nii Pythonis kui .NET-is. Olenemata sellest, kas teie rakendus vajab lihtsat järjestikust töötlemist, paralleelset täitmist või dünaamilist tingimuslikku loogikat, pakub raamistik tööriistu võimsate, skaleeritavate ja tüübikindlate tehisintellekti lahenduste loomiseks.

---

**Lahtiütlus**:  
See dokument on tõlgitud, kasutades AI tõlketeenust [Co-op Translator](https://github.com/Azure/co-op-translator). Kuigi püüame tagada täpsust, palun arvestage, et automaatsed tõlked võivad sisaldada vigu või ebatäpsusi. Algne dokument selle algkeeles tuleks lugeda autoriteetseks allikaks. Olulise teabe puhul on soovitatav kasutada professionaalset inimtõlget. Me ei vastuta selle tõlke kasutamisest tulenevate arusaamatuste või valede tõlgenduste eest.