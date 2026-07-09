# Izdelava večagentnih aplikacij z Microsoft Agent Framework Workflow

Ta vodnik vas bo vodil skozi razumevanje in izdelavo večagentnih aplikacij z uporabo Microsoft Agent Framework. Raziskali bomo osnovne pojme večagentnih sistemov, se poglobili v arhitekturo komponent workflow okvira in pregledali praktične primere v Pythonu in .NET za različne vzorce workflow.

## 1\. Razumevanje večagentnih sistemov

AI agent je sistem, ki presega zmožnosti standardnega velikega jezikovnega modela (LLM). Zmore zaznavati svoje okolje, sprejemati odločitve in izvajati akcije za dosego specifičnih ciljev. Večagentni sistem vključuje več takih agentov, ki sodelujejo pri reševanju problema, ki bi ga bilo težko ali nemogoče rešiti z enim samim agentom.

### Pogoste uporabe

  * **Reševanje kompleksnih problemov**: Razdelitev velike naloge (npr. organizacija dogodka za celotno podjetje) na manjše podnaloge, ki jih opravljajo specializirani agenti (npr. agent za proračun, agent za logistiko, agent za marketing).
  * **Virtualni asistenti**: Primarni pomočnik agent dodeljuje naloge, kot so razporejanje, raziskave in rezervacije, drugim specializiranim agentom.
  * **Avtomatizirano ustvarjanje vsebin**: Workflow, kjer en agent osnutkuje vsebino, drug jo pregleda glede točnosti in tona, tretji pa jo objavi.

### Večagentni vzorci

Večagentni sistemi so lahko organizirani v več vzorcev, ki določajo, kako medsebojno sodelujejo:

  * **Zaporedni**: Agenti delajo v vnaprej določenem vrstnem redu, kot na tekočem traku. Izhod enega agenta postane vhod za naslednjega.
  * **Vzporedni**: Agenti sočasno delajo na različnih delih naloge, njihovi rezultati pa se na koncu združijo.
  * **Pogojni**: Workflow sledi različnim potem glede na izhod agenta, podobno kot izjava če-potem-drugače.

## 2\. Arhitektura Microsoft Agent Framework Workflow

Workflow sistem Agent Framework je napreden orkestracijski mehanizem, namenjen upravljanju kompleksnih interakcij med več agenti. Zgrajen je na arhitekturi, osnovani na grafih, ki uporablja [Pregel-slog model izvajanja](https://kowshik.github.io/JPregel/pregel_paper.pdf), kjer se obdelava izvaja v sinhroniziranih korakih, imenovanih "supersteps".

### Osnovne komponente

Arhitektura je sestavljena iz treh glavnih delov:

1.  **Izvajalci (Executors)**: To so osnovne obdelovalne enote. V naših primerih je `Agent` tip izvajalca. Vsak izvajalec ima lahko več obdelovalcev sporočil, ki se samodejno sprožijo glede na prejeto vrsto sporočila.
2.  **Povezave (Edges)**: Določajo pot, po kateri sporočila potujejo med izvajalci. Povezave lahko imajo pogoje, ki omogočajo dinamično usmerjanje informacij skozi graf workflowa.
3.  **Workflow**: Ta komponenta orkestrira celoten proces, upravlja izvajalce, povezave in potek izvajanja. Zagotavlja pravilno zaporedje obdelave sporočil in pretaka dogodke za opazovanje.

*Diagram, ki prikazuje osnovne komponente sistema workflow.*

Ta struktura omogoča izdelavo robustnih in razširljivih aplikacij z osnovnimi vzorci, kot so zaporedne verige, fan-out/fan-in za vzporedno obdelavo in logiko preklopa (switch-case) za pogojne tokove.

## 3\. Praktični primeri in analiza kode

Sedaj bomo raziskali, kako implementirati različne vzorce workflowa z uporabo okvira. Oglejmo si kodo v Pythonu in .NET za vsak primer.

### Primer 1: Osnovni zaporedni workflow

To je najpreprostejši vzorec, kjer se izhod enega agenta neposredno poda drugemu. Naš scenarij vključuje hotelirskega agenta `FrontDesk`, ki poda potovalno priporočilo, ki ga nato pregleda agent `Concierge`.

*Diagram osnovnega workflowa FrontDesk -> Concierge.*

#### Scenarij

Potnik prosi za priporočilo v Parizu.

1.  Agent `FrontDesk`, zasnovan za jedrnatost, predlaga obisk muzeja Louvre.
2.  Agent `Concierge`, ki daje prednost avtentičnim izkušnjam, prejme to priporočilo. Pregleda ga in poda povratno informacijo, predlagajoč bolj lokalno, manj turistično alternativo.

#### Analiza implementacije v Pythonu

V Python primeru najprej definiramo in ustvarimo dva agenta, vsak s specifičnimi navodili.

```python
# 01.python-agent-framework-workflow-ghmodel-basic.ipynb

# Določite vloge agentov in navodila
REVIEWER_NAME = "Concierge"
REVIEWER_INSTRUCTIONS = """
    You are an are hotel concierge who has opinions about providing the most local and authentic experiences for travelers...
    """

FRONTDESK_NAME = "FrontDesk"
FRONTDESK_INSTRUCTIONS = """
    You are a Front Desk Travel Agent with ten years of experience and are known for brevity...
    """

# Ustvarite primere agentov
reviewer_agent = chat_client.as_agent(
    instructions=(REVIEWER_INSTRUCTIONS),
    name=REVIEWER_NAME,
)

front_desk_agent = chat_client.as_agent(
    instructions=(FRONTDESK_INSTRUCTIONS),
    name=FRONTDESK_NAME,
)
```

Nato uporabimo `WorkflowBuilder` za konstrukcijo grafa. Agent `front_desk_agent` je nastavljen kot začetna točka, ustvarjena je povezava iz njegovega izhoda do `reviewer_agent`.

```python
# 01.python-agent-framework-workflow-ghmodel-basic.ipynb

workflow = WorkflowBuilder(start_executor=front_desk_agent).add_edge(front_desk_agent, reviewer_agent).build()
```

Na koncu se workflow izvede z začetnim uporabniškim pozivom.

```python
# 01.python-agent-framework-workflow-ghmodel-basic.ipynb

result =''
# run izvede potek dela; get_outputs() vrača rezultat izvrševalca izhoda.
events = await workflow.run('I would like to go to Paris.')
outputs = events.get_outputs()
result = outputs[0].text if outputs else ''
```

#### Analiza implementacije v .NET (C#)

Implementacija v .NET sledi zelo podobni logiki. Najprej so definirane konstante za imena agentov in navodila.

```csharp
// 01.dotnet-agent-framework-workflow-ghmodel-basic.ipynb

const string ReviewerAgentName = "Concierge";
const string ReviewerAgentInstructions = @"
    You are an are hotel concierge who has opinions about providing the most local and authentic experiences for travelers...";

const string FrontDeskAgentName = "FrontDesk";
const string FrontDeskAgentInstructions = @"""
    You are a Front Desk Travel Agent with ten years of experience and are known for brevity...";
```

Agente ustvarimo z uporabo `AzureOpenAIClient` (Responses API), nato `WorkflowBuilder` definira zaporedni potek z dodajanjem povezave od `frontDeskAgent` do `reviewerAgent`.

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

Workflow se nato zažene z uporabnikovim sporočilom, rezultati pa se pretakajo nazaj.

### Primer 2: Večstopenjski zaporedni workflow

Ta vzorec razširi osnovno zaporedje z vključitvijo več agentov. Idealno za procese, ki zahtevajo več faz izpopolnjevanja ali transformacije.

#### Scenarij

Uporabnik poda sliko dnevne sobe in zahteva cenovni predračun pohištva.

1.  **Prodajni agent**: Identificira pohištvo na sliki in sestavi seznam.
2.  **Cenovni agent**: Na seznam elementov poda podroben cenovni razčlenitev, vključno z ekonomično, srednjo in vrhunsko kategorijo.
3.  **Agent za predračun**: Prejme cenjeni seznam in ga oblikuje v uraden predračun v Markdown obliki.

*Diagram workflowa Sales -> Price -> Quote.*

#### Analiza implementacije v Pythonu

Definiramo tri agente, vsak z določeno specializacijo. Workflow zgradimo z `add_edge`, da ustvarimo verigo: `sales_agent` -> `price_agent` -> `quote_agent`.

```python
# 02.python-agent-framework-workflow-ghmodel-sequential.ipynb

# Ustvarite tri specializirane agente
sales_agent = chat_client.as_agent(...)
price_agent = chat_client.as_agent(...)
quote_agent = chat_client.as_agent(...)

# Zgradite zaporedni potek dela
workflow = WorkflowBuilder(start_executor=sales_agent).add_edge(sales_agent, price_agent).add_edge(price_agent, quote_agent).build()
```

Vhod je `ChatMessage`, ki vključuje tako besedilo kot URI slike. Okvir poskrbi, da izhod vsakega agenta gre kot vhod naslednjemu v zaporedju, dokler ni končni predračun ustvarjen.

```python
# 02.python-agent-framework-workflow-ghmodel-sequential.ipynb

# Uporabniško sporočilo vsebuje tako besedilo kot sliko
message = ChatMessage(
        role=Role.USER,
        contents=[
            TextContent(text="Please find the relevant furniture..."),
            DataContent(uri=image_uri, media_type="image/png")
        ]
)

# Zaženi potek dela
events = await workflow.run(message)
```

#### Analiza implementacije v .NET (C#)

Primer v .NET odraža Python verzijo. Ustvarjeni so trije agenti (`salesagent`, `priceagent`, `quoteagent`). `WorkflowBuilder` jih poveže zaporedno.

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

Uporabnikovo sporočilo je sestavljeno iz podatkov slike (v bajtih) in besedilnega poziva. Metoda `InProcessExecution.StreamAsync` zažene workflow, končni izhod pa se zajame iz toka.

### Primer 3: Vzporedni workflow

Ta vzorec se uporablja, kadar je mogoče naloge opravljati sočasno za prihranek časa. Vključuje "fan-out" k več agentom in "fan-in" za zbiranje rezultatov.

#### Scenarij

Uporabnik prosi za načrtovanje potovanja v Seattle.

1.  **Dispatcher (fan-out)**: Uporabnikovo zahtevo pošlje dvema agentoma istočasno.
2.  **Researcher-agent**: Raziskuje znamenitosti, vreme in ključne dejavnike za potovanje v Seattle decembra.
3.  **Plan-agent**: Samostojno ustvarja podroben dnevni načrt potovanja.
4.  **Aggregator (fan-in)**: Izide iz raziskovalca in načrtovalca zbira skupaj in jih predstavi kot končni rezultat.

*Diagram vzporednega workflowa Researcher in Planner.*

#### Analiza implementacije v Pythonu

`ConcurrentBuilder` poenostavi ustvarjanje tega vzorca. Preprosto navedete udeležene agente, builder pa samodejno pripravi potrebno logiko fan-out in fan-in.

```python
# 03.python-agent-framework-workflow-ghmodel-concurrent.ipynb

research_agent = chat_client.as_agent(name="Researcher-Agent", ...)
plan_agent = chat_client.as_agent(name="Plan-Agent", ...)

# ConcurrentBuilder upravlja logiko razvejanja/združevanja
workflow = ConcurrentBuilder().participants([research_agent, plan_agent]).build()

# Zaženi delovni proces
events = await workflow.run("Plan a trip to Seattle in December")
```

Okvir zagotovi, da `research_agent` in `plan_agent` izvajata vzporedno, končne izhode pa se zbere v seznam.

#### Analiza implementacije v .NET (C#)

V .NET mora biti vzorec definirano bolj eksplicitno. Ustvarjeni so prilagojeni izvajalci (`ConcurrentStartExecutor` in `ConcurrentAggregationExecutor`), ki obravnavajo logiko fan-out in fan-in.

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

`WorkflowBuilder` nato uporabi `AddFanOutEdge` in `AddFanInEdge` za konstrukcijo grafa s temi prilagojenimi izvajalci in agenti.

```csharp
// 03.dotnet-agent-framework-workflow-ghmodel-concurrent.ipynb

var workflow = new WorkflowBuilder(startExecutor)
            .AddFanOutEdge(startExecutor, targets: [researcherAgent, plannerAgent])
            .AddFanInEdge(aggregationExecutor, sources: [researcherAgent, plannerAgent])
            .WithOutputFrom(aggregationExecutor)
            .Build();
```

### Primer 4: Pogojni workflow

Pogojni workflowi uvajajo vejo logike, ki sistemu omogoča izbiranje različnih poti glede na vmesne rezultate.

#### Scenarij

Ta workflow avtomatizira ustvarjanje in objavo tehničnega vodiča.

1.  **Evangelist-agent**: Piše osnutek vodiča na podlagi dane osnove in URL-jev.
2.  **ContentReviewer-agent**: Pregleduje osnutek. Preverja, ali je število besed prek 200.
3.  **Pogojna veja**:
      * **Če odobreno (`Da`)**: Workflow nadaljuje do `Publisher-agent`.
      * **Če zavrnjeno (`Ne`)**: Workflow se ustavi in izpiše razlog za zavrnitev.
4.  **Publisher-agent**: Če je osnutek odobren, ta agent shrani vsebino kot Markdown datoteko.

#### Analiza implementacije v Pythonu

Primer uporablja prilagojeno funkcijo `select_targets` za implementacijo pogojne logike. Funkcija se posreduje `add_multi_selection_edge_group` in usmerja workflow glede na polje `review_result` v izhodu pregledovalca.

```python
# 04.python-agent-framework-workflow-aifoundry-condition.ipynb

# Ta funkcija določi naslednji korak na podlagi rezultata pregleda
def select_targets(review: ReviewResult, target_ids: list[str]) -> list[str]:
    handle_review_id, save_draft_id = target_ids
    if review.review_result == "Yes":
        # Če je odobreno, nadaljuj z izvajalcem 'save_draft'
        return [save_draft_id]
    else:
        # Če je zavrnjeno, nadaljuj z izvajalcem 'handle_review' za poročanje o neuspehu
        return [handle_review_id]

# Graditelj poteka dela uporablja funkcijo izbire za usmerjanje
workflow = (
    WorkflowBuilder()
        .set_start_executor(evangelist_agent)
        .add_edge(evangelist_agent, reviewer_agent)
        .add_edge(reviewer_agent, to_reviewer_result)
        # Večkratna izbira rob implementira pogojno logiko
        .add_multi_selection_edge_group(
            to_reviewer_result,
            [handle_review, save_draft],
            selection_func=select_targets,
        )
        .add_edge(save_draft, publisher_agent)
        .build()
)
```

Prilagojeni izvajalci, kot je `to_reviewer_result`, se uporabljajo za razčlenitev JSON izhodov agentov v močno tipizirane objekte, ki jih funkcija izbire lahko pregleda.

#### Analiza implementacije v .NET (C#)

Verzija v .NET uporablja podoben pristop s funkcijo pogoja. Definiran je `Func<object?, bool>`, ki preveri lastnost `Result` objekta `ReviewResult`.

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

Parameter `condition` metode `AddEdge` omogoča `WorkflowBuilder` ustvarjanje razvejane poti. Workflow bo sledil povezavi do `publishExecutor` samo, če `GetCondition(expectedResult: "Yes")` vrne true. V nasprotnem primeru sledi poti do `sendReviewerExecutor`.

## Zaključek

Microsoft Agent Framework Workflow nudi robustno in prilagodljivo osnovo za orkestracijo kompleksnih večagentnih sistemov. Z uporabo njegove grafne arhitekture in osnovnih komponent lahko razvijalci načrtujejo in implementirajo sofisticirane workflowe tako v Pythonu kot .NET. Ne glede na to, ali vaša aplikacija potrebuje preprosto zaporedno obdelavo, vzporedno izvajanje ali dinamično pogojno logiko, okvir ponuja orodja za izdelavo zmogljivih, razširljivih in tipu-varnih rešitev, ki temeljijo na AI.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Omejitev odgovornosti**:
Ta dokument je bil preveden z uporabo AI prevajalske storitve [Co-op Translator](https://github.com/Azure/co-op-translator). Čeprav si prizadevamo za natančnost, vas prosimo, da upoštevate, da avtomatizirani prevodi lahko vsebujejo napake ali netočnosti. Izvirni dokument v njegovem izvirnem jeziku je treba obravnavati kot avtoritativni vir. Za kritične informacije je priporočljiv strokovni človeški prevod. Ne odgovarjamo za morebitna nesporazume ali napačne interpretacije, ki izhajajo iz uporabe tega prevoda.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->