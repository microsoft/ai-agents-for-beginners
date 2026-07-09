# Mitmeagendi rakenduste loomine Microsoft Agent Frameworki töövoo abil

See juhend aitab sul mõista ja luua mitmeagendi rakendusi, kasutades Microsoft Agent Frameworki. Uurime mitmeagendisüsteemide põhimõisteid, sukeldume raamistikus töövoo komponendi arhitektuuri ja vaatame praktilisi näiteid nii Pythonis kui .NET-is erinevate töövoo mustrite kohta.

## 1\. Mitmeagendisüsteemide mõistmine

Tehisintellekti agent on süsteem, mis ületab tavalise suure keelemudeli (LLM) võimalused. See suudab tajuda oma keskkonda, teha otsuseid ja võtta meetmeid konkreetsete eesmärkide saavutamiseks. Mitmeagendisüsteem hõlmab mitut sellist agenti, kes teevad koostööd probleemi lahendamiseks, mida oleks ühe agendi jaoks raske või võimatu üksinda hallata.

### Levinumad rakendussituatsioonid

  * **Kompleksete probleemide lahendamine**: Suure ülesande (nt ettevõtteürituse planeerimine) jagamine väiksemateks alamelementideks, mida haldavad spetsialiseeritud agendid (nt eelarveagent, logistikaagent, turundusagent).
  * **Virtuaalsed assistendid**: Peamine assistentagent delegeerib ülesandeid nagu ajakava koostamine, uurimistöö ja broneerimine teistele spetsialiseerunud agentidele.
  * **Automatiseeritud sisu loomine**: Töövoog, kus üks agent koostab sisu, teine kontrollib selle täpsust ja tooni ning kolmas avaldab selle.

### Mitmeagendi mustrid

Mitmeagendisüsteemid võivad olla organiseeritud mitmel erineval mustril, mis määravad, kuidas nad omavahel suhtlevad:

  * **Järjestikune**: Agendid töötavad eelnevalt määratud järjekorras, nagu tootmislinnas. Ühe agendi väljund on järgmise sisend.
  * **Samaaegne**: Agendid töötavad paralleelselt erinevate ülesannete kallal ja nende tulemused koondatakse lõpus.
  * **Tingimuslik**: Töövoog järgib erinevaid radu, sõltuvalt agendi väljundist, sarnaselt tingimusavaldise if-then-else loogikaga.

## 2\. Microsoft Agent Framework töövoo arhitektuur

Agent Frameworki töövoosüsteem on keerukas orkestreerimise mootor, mis haldab mitme agendi vahelist keerukat suhtlust. See põhineb graafipõhisel arhitektuuril, mis kasutab [Pregel-tüüpi täitmismudelit](https://kowshik.github.io/JPregel/pregel_paper.pdf), kus töötlemine toimub sünkroniseeritud sammudes, mida nimetatakse "superstepideks".

### Põhikompendid

Arhitektuur koosneb kolmest põhiosast:

1.  **Täiturid**: Need on põhilised töötlemise üksused. Meie näidetes on `Agent` üks täiturite tüüp. Igal täituril võib olla mitu sõnumikäitlejat, mis kutsutakse automaatselt välja vastavalt sõnumi tüübile.
2.  **Servad**: Defineerivad tee, mida pidi sõnumid täiturite vahel liiguvad. Servadel võivad olla tingimused, võimaldades informatsiooni dünaamilist suunamist töövoo graafis.
3.  **Töövoog**: See komponent orkestreerib kogu protsessi, haldades täitureid, servasid ja töödeldava täitmise üldvoogu. See tagab sõnumite õige järjestuse töötlemise ning voogesitab sündmusi jälgitavuse jaoks.

*Diagramm, mis kujutab töövoosüsteemi põhikomponente.*

See struktuur võimaldab luua vastupidavaid ja skaleeritavaid rakendusi, kasutades põhimustreid nagu järjestikused ahelad, fan-out/fan-in paralleelprotsessimiseks ja switch-case loogikat tingimuslikeks töövoogudeks.

## 3\. Praktilised näited ja koodi analüüs

Vaatame nüüd, kuidas erinevaid töövoo mustreid raamistikus rakendada. Tutvume nii Python kui .NET-i koodiga iga näite puhul.

### Juhtum 1: Lihtne järjestikune töövoog

See on kõige lihtsam muster, kus ühe agendi väljund antakse otse edasi teisele. Meie stsenaariumis annab hotelli `FrontDesk` agent reisinõuande, mida üle vaatab `Concierge` agent.

*Diagramm lihtsast FrontDesk -\> Concierge töövoost.*

#### Stsenaariumi taust

Reisija küsib soovitust Pariisis.

1.  `FrontDesk` agent, kes on lühidust hindav, soovitab külastada Louvre'i muuseumi.
2.  `Concierge` agent, kes eelistab autentseid kogemusi, saab selle soovituse, vaatab selle üle ja annab tagasisidet, pakkudes välja kohaliku ja vähem turisti kaasava alternatiivi.

#### Python'i rakenduse analüüs

Python'i näites defineerime esmalt kaks agenti, igaühel on oma spetsiifilised juhised.

```python
# 01.python-agent-framework-workflow-ghmodel-basic.ipynb

# Määratle agendi rollid ja juhised
REVIEWER_NAME = "Concierge"
REVIEWER_INSTRUCTIONS = """
    You are an are hotel concierge who has opinions about providing the most local and authentic experiences for travelers...
    """

FRONTDESK_NAME = "FrontDesk"
FRONTDESK_INSTRUCTIONS = """
    You are a Front Desk Travel Agent with ten years of experience and are known for brevity...
    """

# Loo agendi eksemplarid
reviewer_agent = chat_client.as_agent(
    instructions=(REVIEWER_INSTRUCTIONS),
    name=REVIEWER_NAME,
)

front_desk_agent = chat_client.as_agent(
    instructions=(FRONTDESK_INSTRUCTIONS),
    name=FRONTDESK_NAME,
)
```

Järgmiseks kasutatakse `WorkflowBuilder`i, et koostada graaf. `front_desk_agent` määratakse lähtepunktiks ning tehakse serv, mis ühendab selle väljundi `reviewer_agent`iga.

```python
# 01.python-agent-framework-workflow-ghmodel-basic.ipynb

workflow = WorkflowBuilder(start_executor=front_desk_agent).add_edge(front_desk_agent, reviewer_agent).build()
```

Lõpuks käivitatakse töövoog algse kasutaja sisendiga.

```python
# 01.python-agent-framework-workflow-ghmodel-basic.ipynb

result =''
# run käivitab töövoo; get_outputs() tagastab väljundi täitja tulemuse.
events = await workflow.run('I would like to go to Paris.')
outputs = events.get_outputs()
result = outputs[0].text if outputs else ''
```

#### .NET (C\#) rakenduse analüüs

.NET rakendus järgib väga sarnast loogikat. Esiteks määratakse agendi nimed ja juhised konstantidena.

```csharp
// 01.dotnet-agent-framework-workflow-ghmodel-basic.ipynb

const string ReviewerAgentName = "Concierge";
const string ReviewerAgentInstructions = @"
    You are an are hotel concierge who has opinions about providing the most local and authentic experiences for travelers...";

const string FrontDeskAgentName = "FrontDesk";
const string FrontDeskAgentInstructions = @"""
    You are a Front Desk Travel Agent with ten years of experience and are known for brevity...";
```

Agendid luuakse kasutades `AzureOpenAIClient`i (Responses API) ja seejärel defineerib `WorkflowBuilder` järjestikulise voo, lisades servi `frontDeskAgent`ist `reviewerAgent`ini.

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

Tööd algatatakse kasutaja sõnumiga ning tulemused edastatakse voona tagasi.

### Juhtum 2: Mitmeastmeline järjestikune töövoog

See muster laiendab lihtsat järjestust, lisades rohkem agente. See sobib protsesside jaoks, mis vajavad mitmeid täiendamise või transformeerimise etappe.

#### Stsenaariumi taust

Kasutaja esitab elutoa pildi ja küsib mööbli hinnapakkumist.

1.  **Müügagent**: Tuletab pildilt tuvastatud mööbliesemed ja koostab nimekirja.
2.  **Hinnagent**: Võtab nimekirja ja esitab detailse hinnalõhendi, mis sisaldab odavat, keskmist ja premium-varianti.
3.  **Pakkumise agent**: Võtab hinnatud nimekirja vastu ja vormindab selle ametlikuks pakkumiseks Markdown'is.

*Diagramm töövoost Müük -\> Hind -\> Pakkumine.*

#### Python'i rakenduse analüüs

Määratletakse kolm agenti igaüks oma ülesandega. Töövoog ehitatakse `add_edge` abil, mis loob ahela: `sales_agent` -\> `price_agent` -\> `quote_agent`.

```python
# 02.python-agent-framework-workflow-ghmodel-sequential.ipynb

# Loo kolm spetsialiseerunud agenti
sales_agent = chat_client.as_agent(...)
price_agent = chat_client.as_agent(...)
quote_agent = chat_client.as_agent(...)

# Ehita järjestikune töövoog
workflow = WorkflowBuilder(start_executor=sales_agent).add_edge(sales_agent, price_agent).add_edge(price_agent, quote_agent).build()
```

Sisendiks on `ChatMessage`, mis sisaldab nii teksti kui ka pildi URI-d. Raamistik haldab iga agendi väljundi edastamist järgmisele järjestuses kuni lõpliku pakkumise valmimiseni.

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

# Käivita töökäik
events = await workflow.run(message)
```

#### .NET (C\#) rakenduse analüüs

.NET näide peegeldab Python versiooni. Luuakse kolm agenti (`salesagent`, `priceagent`, `quoteagent`) ning `WorkflowBuilder` lingib need järjestikku.

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

Kasutaja sõnum on koostatud nii pildisignaali (baitidena) kui teksti sisendina. Meetod `InProcessExecution.StreamAsync` alustab töövoogu ja lõplik väljund võetakse voo kaudu.

### Juhtum 3: Samaaegne töövoog

See muster sobib ülesannetele, mida saab teha samaaegselt aja säästmiseks. See hõlmab "fan-out" mitmele agendile ja "fan-in" tulemuste koondamiseks.

#### Stsenaariumi taust

Kasutaja palub koostada reisiplaan Seattle'i.

1.  **Saaja (Fan-Out)**: Kasutaja päring saadetakse korraga kahele agentele.
2.  **Uurija-agent**: Uurib vaatamisväärsusi, ilmaolusid ja olulisi tegureid detsembris Seattle'is reisimiseks.
3.  **Plaanimeister-agent**: Iseseisvalt koostab üksikasjaliku päevapõhise reisiplaani.
4.  **Kogujah (Fan-In)**: Kogub nii uurija kui planeri väljundid ja esitab need koos lõpptulemusena.

*Diagramm samaajalisest Uurija ja Planer töövoost.*

#### Python'i rakenduse analüüs

`ConcurrentBuilder` lihtsustab selle mustri loomist. Lihtsalt loetled agentid ja ehitaja loob automaatselt vajalikud fan-out ja fan-in loogikad.

```python
# 03.python-agent-framework-workflow-ghmodel-concurrent.ipynb

research_agent = chat_client.as_agent(name="Researcher-Agent", ...)
plan_agent = chat_client.as_agent(name="Plan-Agent", ...)

# ConcurrentBuilder haldab fan-out/fan-in loogikat
workflow = ConcurrentBuilder().participants([research_agent, plan_agent]).build()

# Käivita töövoog
events = await workflow.run("Plan a trip to Seattle in December")
```

Raamistik tagab, et `research_agent` ja `plan_agent` täidavad paralleelselt ning nende lõplikud väljundid koondatakse nimekirjaks.

#### .NET (C\#) rakenduse analüüs

.NET-is nõuab see muster selgemat määratlust. Luuakse kohandatud täiturid (`ConcurrentStartExecutor` ja `ConcurrentAggregationExecutor`), mis haldavad fan-out ja fan-in loogikat.

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

Seejärel kasutab `WorkflowBuilder` meetodeid `AddFanOutEdge` ja `AddFanInEdge`, et ehitada graaf kohandatud täiturite ja agentidega.

```csharp
// 03.dotnet-agent-framework-workflow-ghmodel-concurrent.ipynb

var workflow = new WorkflowBuilder(startExecutor)
            .AddFanOutEdge(startExecutor, targets: [researcherAgent, plannerAgent])
            .AddFanInEdge(aggregationExecutor, sources: [researcherAgent, plannerAgent])
            .WithOutputFrom(aggregationExecutor)
            .Build();
```

### Juhtum 4: Tingimuslik töövoog

Tingimuslikud töövood lisavad harunemisloogika, võimaldades süsteemil võtta erinevaid radu põhinedes vahetulemustel.

#### Stsenaariumi taust

See töövoog automatiseerib tehnilise juhendi loomist ja avaldamist.

1.  **Evangelist-agent**: Koostab juhendi mustandi antud sissejuhatuse ja URL-ide põhjal.
2.  **Sisuülevaataja-agent**: Kontrollib mustandit. Kontrollib, kas sõnade arv on üle 200.
3.  **Tingimuslik haru**:
      * **Kui heaks kiidetud (`Jah`)**: Töövoog läheb edasi `Publisher-Agent`i poole.
      * **Kui tagasi lükatud (`Ei`)**: Töövoog lõppeb ja väljastab tagasilükkamise põhjuse.
4.  **Publisher-Agent**: Kui mustand kiidetakse heaks, salvestab see agent sisu Markdown-faili.

#### Python'i rakenduse analüüs

Selles näites kasutatakse kohandatud funktsiooni `select_targets`, mis realiseerib tingimusloogika. See funktsioon antakse `add_multi_selection_edge_group`ile ja juhib töövoogu põhinedes `review_result` väljal ülevaataja väljundis.

```python
# 04.python-agent-framework-workflow-aifoundry-condition.ipynb

# See funktsioon määrab järgmise sammu ülevaatustulemuse põhjal
def select_targets(review: ReviewResult, target_ids: list[str]) -> list[str]:
    handle_review_id, save_draft_id = target_ids
    if review.review_result == "Yes":
        # Kui heaks kiidetud, jätkatakse täitjaga 'save_draft'
        return [save_draft_id]
    else:
        # Kui tagasi lükatud, jätkatakse täitjaga 'handle_review', et teatada ebaõnnestumisest
        return [handle_review_id]

# Töövoo ehitaja kasutab marsruutimiseks valikfunktsiooni
workflow = (
    WorkflowBuilder()
        .set_start_executor(evangelist_agent)
        .add_edge(evangelist_agent, reviewer_agent)
        .add_edge(reviewer_agent, to_reviewer_result)
        # Mitmevaliku serv rakendab tingimusloogikat
        .add_multi_selection_edge_group(
            to_reviewer_result,
            [handle_review, save_draft],
            selection_func=select_targets,
        )
        .add_edge(save_draft, publisher_agent)
        .build()
)
```

Kohandatud täiturid nagu `to_reviewer_result` teisendavad agentide JSON väljundi tugevalt tüübistatavateks objektideks, mida valikufunktsioon saab kontrollida.

#### .NET (C\#) rakenduse analüüs

.NET versioon kasutab sarnast lähenemist tingimusfunktsiooniga. Defineeritakse `Func<object?, bool>`, mis kontrollib `ReviewResult` objekti `Result` omadust.

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

Meetodi `AddEdge` parameeter `condition` lubab `WorkflowBuilderil` luua harunduva tee. Töövoog järgib serva `publishExecutor`i suunas, kui tingimus `GetCondition(expectedResult: "Yes")` on tõene. Muul juhul järgib tee `sendReviewerExecutor`i suunas.

## Kokkuvõte

Microsoft Agent Framework Workflow pakub tugevat ja paindlikku alust keerukate mitmeagendisüsteemide orkestreerimiseks. Kasutades graafipõhist arhitektuuri ja põhikomponente, saavad arendajad kavandada ja ellu viia keerukaid töövooge nii Pythonis kui ka .NETis. Olgu su rakendus lihtsa järjestikuse töötlemise, paralleelse täitmise või dünaamilise tingimusloogika vajadusega, raamistik pakub vahendid võimsate, skaleeritavate ja tüübiturvaliste tehisintellektil põhinevate lahenduste ehitamiseks.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Lahtiütlus**:
See dokument on tõlgitud kasutades AI tõlketeenust [Co-op Translator](https://github.com/Azure/co-op-translator). Kuigi me püüdleme täpsuse poole, palun pange tähele, et automatiseeritud tõlgetes võib esineda vigu või ebatäpsusi. Originaaldokument selle emakeeles tuleks pidada autoriteetseks allikaks. Olulise teabe puhul soovitatakse kasutada professionaalset inimtõlget. Me ei vastuta selle tõlkega seotud eksimustest või valesti mõistmistest.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->