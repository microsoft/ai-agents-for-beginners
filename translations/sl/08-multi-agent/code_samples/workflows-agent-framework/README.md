# Izgradnja večagentnih aplikacij z Microsoft Agent Framework Workflow

Ta vodič vas bo popeljal skozi razumevanje in izgradnjo večagentnih aplikacij z uporabo Microsoft Agent Framework. Raziščemo osnovne koncepte večagentnih sistemov, se poglobimo v arhitekturo komponent Workflow tega ogrodja in predstavimo praktične primere v Pythonu in .NET za različne vzorce workflowa.

## 1\. Razumevanje večagentnih sistemov

AI agent je sistem, ki presega zmogljivosti običajnega velikega jezikovnega modela (LLM). Lahko zaznava svoje okolje, sprejema odločitve in izvaja dejanja za doseganje specifičnih ciljev. Večagentni sistem vključuje več teh agentov, ki sodelujejo pri reševanju problema, ki bi bil za enega samega agenta težaven ali nemogoč.

### Pogoste scenarije uporabe

  * **Reševanje kompleksnih problemov**: Razdelitev velike naloge (npr. načrtovanje dogodka za celotno podjetje) na manjše podnaloge, ki jih obvladujejo specializirani agenti (npr. agent za proračun, agent za logistiko, agent za marketing).
  * **Virtualni pomočniki**: Glavni agent-pomočnik delegira naloge, kot so načrtovanje, raziskave in rezervacije, drugim specializiranim agentom.
  * **Samodejna ustvaritev vsebin**: Workflow, kjer en agent oblikuje vsebino, drugi jo pregleda zaradi točnosti in tona, tretji pa jo objavi.

### Vzorci večagentnih sistemov

Večagentni sistemi so lahko organizirani v več vzorcev, ki določajo, kako medsebojno delujejo:

  * **Zaporedni**: Agenti delajo v predhodno določenem vrstnem redu, kot na tekočem traku. Izhod enega agenta postane vhod za naslednjega.
  * **Vzporedni**: Agenti delajo vzporedno na različnih delih naloge, na koncu pa se njihovi rezultati združijo.
  * **Pogojni**: Workflow sledi različnim potezam na podlagi izhoda agenta, podobno kot stavek če-potem-drugače.

## 2\. Arhitektura Microsoft Agent Framework Workflow

Workflow sistem v Agent Frameworku je napreden orkestracijski mehanizem, zasnovan za upravljanje kompleksnih interakcij med več agenti. Zgrajen je na arhitekturi, osnovani na grafu, ki uporablja [Pregel-style execution model](https://kowshik.github.io/JPregel/pregel_paper.pdf), kjer se procesiranje izvaja v sinhroniziranih korakih, imenovanih "superkoraki."

### Osnovne komponente

Arhitektura je sestavljena iz treh glavnih delov:

1.  **Izvajalci (Executors)**: To so osnovne enote procesiranja. V naših primerih je `Agent` tip izvajalca. Vsak izvajalec lahko ima več upravljavcev sporočil, ki se samodejno kličejo glede na vrsto prejetega sporočila.
2.  **Povezave (Edges)**: Opredeljujejo pot, po kateri sporočila potujejo med izvajalci. Povezave lahko imajo pogoje, ki omogočajo dinamično usmerjanje informacij skozi graf workflowa.
3.  **Workflow**: Ta komponenta orkestrira celoten proces, upravlja izvajalce, povezave in celoten potek izvajanja. Zagotavlja, da se sporočila obdelujejo v pravilnem vrstnem redu in pretaka dogodke za opazovanje.

*Diagram, ki prikazuje osnovne komponente workflow sistema.*

Ta struktura omogoča gradnjo robustnih in skalabilnih aplikacij z uporabo osnovnih vzorcev, kot so zaporedne verige, fan-out/fan-in za vzporedno procesiranje in preklopna logika za pogojne poti.

## 3\. Praktični primeri in analiza kode

Sedaj si oglejmo, kako implementirati različne vzorce workflowa z uporabo ogrodja. Ogledali si bomo primere kode v Pythonu in .NET.

### Primer 1: Osnovni zaporedni workflow

To je najpreprostejši vzorec, kjer se izhod enega agenta neposredno predaja drugemu. Naš primer vključuje hotelskega agenta `FrontDesk`, ki poda priporočilo za potovanje, ki ga nato pregleda agent `Concierge`.

*Diagram osnovnega workflowa FrontDesk -\> Concierge.*

#### Ozadje primera

Potnik zaprosi za priporočilo v Parizu.

1.  Agent `FrontDesk`, zasnovan za jedrnatost, predlaga obisk muzeja Louvre.
2.  Agent `Concierge`, ki ceni pristne izkušnje, prejme to priporočilo. Pregleda ga in da povratno informacijo, predlagajoč bolj lokalno, manj turistično alternativo.

#### Analiza implementacije v Pythonu

V Python primeru najprej definiramo in ustvarimo dva agenta, vsak s specifičnimi navodili.

```python
# 01.python-agent-framework-workflow-ghmodel-basic.ipynb

# Določite vloge agentov in navodila
REVIEWER_NAME = "Concierge"
REVIEWER_INSTRUCTIONS = """
    You are a hotel concierge who has opinions about providing the most local and authentic experiences for travelers...
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

Nato se uporabi `WorkflowBuilder` za izgradnjo grafa. `front_desk_agent` je nastavljen kot izhodišče, ustvarjena pa je povezava, ki njegov izhod poveže z `reviewer_agent`.

```python
# 01.python-agent-framework-potek-dela-ghmodel-osnovno.ipynb

workflow = WorkflowBuilder(start_executor=front_desk_agent).add_edge(front_desk_agent, reviewer_agent).build()
```

Na koncu se workflow izvede z začetnim uporabniškim pozivom.

```python
# 01.python-agent-framework-workflow-ghmodel-basic.ipynb

result =''
# run izvede potek dela; get_outputs() vrne rezultat izvajalca izhoda.
events = await workflow.run('I would like to go to Paris.')
outputs = events.get_outputs()
result = outputs[0].text if outputs else ''
```

#### Analiza implementacije v .NET (C#)

Implementacija v .NET sledi zelo podobni logiki. Najprej se definirajo konstante za imena agentov in navodila.

```csharp
// 01.dotnet-agent-framework-workflow-ghmodel-basic.ipynb

const string ReviewerAgentName = "Concierge";
const string ReviewerAgentInstructions = @"
    You are a hotel concierge who has opinions about providing the most local and authentic experiences for travelers...";

const string FrontDeskAgentName = "FrontDesk";
const string FrontDeskAgentInstructions = @"""
    You are a Front Desk Travel Agent with ten years of experience and are known for brevity...";
```

Agenti se ustvarijo z uporabo `AzureOpenAIClient` (Responses API), nato pa `WorkflowBuilder` definira zaporedni potek z dodajanjem povezave iz `frontDeskAgent` do `reviewerAgent`.

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

Workflow se nato izvaja z uporabnikovim sporočilom, rezultati pa se pretakajo nazaj.

### Primer 2: Zaporedni workflow z več koraki

Ta vzorec razširja osnovni zaporedni potek, da vključuje več agentov. Primeren je za postopke, ki zahtevajo več stopenj izpopolnjevanja ali transformacije.

#### Ozadje primera

Uporabnik poda sliko dnevne sobe in zaprosi za ponudbo pohištva.

1.  **Prodajni agent**: Prepozna pohištvo na sliki in naredi seznam.
2.  **Agent za cene**: Prevzame seznam in poda podrobno cenovno razčlenitev, vključno z izbirami v proračunu, srednjem razredu in premiumu.
3.  **Agent za ponudbo**: Prejme cenjeni seznam in ga oblikuje v uradni dokument s ponudbo v Markdownu.

*Diagram workflowa Sales -\> Price -\> Quote.*

#### Analiza implementacije v Pythonu

Definiramo tri agente, vsak s specializirano vlogo. Workflow se sestavi z uporabo `add_edge` za ustvarjanje verige: `sales_agent` -\> `price_agent` -\> `quote_agent`.

```python
# 02.python-agent-framework-workflow-ghmodel-sequential.ipynb

# Ustvarite tri specializirane agente
sales_agent = chat_client.as_agent(...)
price_agent = chat_client.as_agent(...)
quote_agent = chat_client.as_agent(...)

# Zgradite zaporedni potek dela
workflow = WorkflowBuilder(start_executor=sales_agent).add_edge(sales_agent, price_agent).add_edge(price_agent, quote_agent).build()
```

Vhod je `ChatMessage`, ki vključuje tako besedilo kot URI slike. Ogrodje skrbi za prenašanje izhoda vsakega agenta naslednjemu v zaporedju, dokler se ne ustvari končna ponudba.

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

.NET primer se ujema s Python različico. Ustvarjeni so trije agenti (`salesagent`, `priceagent`, `quoteagent`). `WorkflowBuilder` jih zaporedno poveže.

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

Uporabnikovo sporočilo vsebuje tako binarne podatke slike kot tekstovni poziv. Metoda `InProcessExecution.RunStreamingAsync` zažene workflow, končni izhod pa je zajet iz pretoka.

### Primer 3: Vzporedni workflow

Ta vzorec se uporablja, ko se naloge lahko izvajajo vzporedno za prihranek časa. Vključuje "fan-out" k več agentom in "fan-in" za združevanje rezultatov.

#### Ozadje primera

Uporabnik zaprosi za načrtovanje poti v Seattle.

1.  **Razporejevalec (Fan-Out)**: Uporabnikov zahtevek je poslan dvema agentoma hkrati.
2.  **Raziskovalni agent**: Razišče atrakcije, vreme in ključne dejavnike za potovanje v Seattle decembra.
3.  **Agent za načrtovanje**: Neodvisno ustvari podroben dnevni načrt potovanja.
4.  **Združevalec (Fan-In)**: Izvide obeh agentov, raziskovalnega in načrtovalnega, zbere skupaj in jih predstavi kot končni rezultat.

*Diagram vzporednega workflowa Raziskovalec in Načrtovalec.*

#### Analiza implementacije v Pythonu

`ConcurrentBuilder` poenostavi ustvarjanje tega vzorca. Preprosto navedete sodelujoče agente in builder samodejno ustvari potrebno logiko fan-out in fan-in.

```python
# 03.python-agent-framework-workflow-ghmodel-concurrent.ipynb

research_agent = chat_client.as_agent(name="Researcher-Agent", ...)
plan_agent = chat_client.as_agent(name="Plan-Agent", ...)

# ConcurrentBuilder upravlja logiko razvejanja/združevanja
workflow = ConcurrentBuilder().participants([research_agent, plan_agent]).build()

# Zaženi potek dela
events = await workflow.run("Plan a trip to Seattle in December")
```

Ogrodje zagotovi, da se `research_agent` in `plan_agent` izvajata vzporedno, njihove končne izhode pa zbere v seznam.

#### Analiza implementacije v .NET (C#)

V .NET je ta vzorec potrebno bolj eksplicitno definirati. Ustvarjeni so po meri izvajalci (`ConcurrentStartExecutor` in `ConcurrentAggregationExecutor`) za upravljanje fan-out in fan-in logike.

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

Nato `WorkflowBuilder` uporabi `AddFanOutEdge` in `AddFanInEdge` za sestavo grafa s temi prilagojenimi izvajalci in agenti.

```csharp
// 03.dotnet-agent-framework-workflow-ghmodel-concurrent.ipynb

var workflow = new WorkflowBuilder(startExecutor)
            .AddFanOutEdge(startExecutor, targets: [researcherAgent, plannerAgent])
            .AddFanInEdge(aggregationExecutor, sources: [researcherAgent, plannerAgent])
            .WithOutputFrom(aggregationExecutor)
            .Build();
```

### Primer 4: Pogojni workflow

Pogojni workflow uvaja vejno logiko, ki sistemu omogoča, da izbere različne poti na podlagi vmesnih rezultatov.

#### Ozadje primera

Ta workflow avtomatizira ustvarjanje in objavo tehničnega vodiča.

1.  **Evangelist-Agent**: Napiše osnutek vodiča glede na dane smernice in URL-je.
2.  **ContentReviewer-Agent**: Pregleda osnutek. Preveri, ali je število besed večje od 200.
3.  **Pogojna veja**:
      * **Če je odobreno (`Da`)**: Workflow nadaljuje do `Publisher-Agent`.
      * **Če je zavrnjeno (`Ne`)**: Workflow se ustavi in izpiše razlog zavrnitve.
4.  **Publisher-Agent**: Če je osnutek odobren, ta agent shrani vsebino v Markdown datoteko.

#### Analiza implementacije v Pythonu

Ta primer uporablja prilagojeno funkcijo `select_targets` za implementacijo pogojne logike. Funkcija se posreduje v `add_multi_selection_edge_group` in usmerja workflow na podlagi polja `review_result` v izhodu recenzenta.

```python
# 04.python-agent-framework-workflow-aifoundry-condition.ipynb

# Ta funkcija določi naslednji korak glede na rezultat pregleda
def select_targets(review: ReviewResult, target_ids: list[str]) -> list[str]:
    handle_review_id, save_draft_id = target_ids
    if review.review_result == "Yes":
        # Če je odobreno, nadaljuj z izvajalcem 'save_draft'
        return [save_draft_id]
    else:
        # Če je zavrnjeno, nadaljuj z izvajalcem 'handle_review', da poročaš o neuspehu
        return [handle_review_id]

# Graditelj poteka dela uporablja izbirno funkcijo za usmerjanje
workflow = (
    WorkflowBuilder()
        .set_start_executor(evangelist_agent)
        .add_edge(evangelist_agent, reviewer_agent)
        .add_edge(reviewer_agent, to_reviewer_result)
        # Večkratna izbira robu implementira pogojno logiko
        .add_multi_selection_edge_group(
            to_reviewer_result,
            [handle_review, save_draft],
            selection_func=select_targets,
        )
        .add_edge(save_draft, publisher_agent)
        .build()
)
```

Prilagojeni izvajalci, kot je `to_reviewer_result`, se uporabljajo za razčlenitev JSON izhoda agentov in njegovo pretvorbo v močno tipizirane objekte, ki jih lahko funkcija za izbor pregleda.

#### Analiza implementacije v .NET (C#)

.NET različica uporablja podoben pristop s pogojevalno funkcijo. Definirana je `Func<object?, bool>`, ki preveri lastnost `Result` objekta `ReviewResult`.

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

Parameter `condition` metode `AddEdge` omogoča `WorkflowBuilderju`, da ustvari vejo poti. Workflow bo sledil povezavi do `publishExecutor` samo, če pogoj `GetCondition(expectedResult: "Yes")` vrne true. V nasprotnem primeru bo sledil poti do `sendReviewerExecutor`.

## Zaključek

Microsoft Agent Framework Workflow omogoča robustno in prilagodljivo osnovo za orkestracijo kompleksnih večagentnih sistemov. Z uporabo njegove arhitekture na osnovi grafov in osnovnih komponent lahko razvijalci načrtujejo in implementirajo zahtevne workflowe tako v Pythonu kot v .NET. Ne glede na to, ali vaša aplikacija zahteva preprosto zaporedno procesiranje, vzporedno izvajanje ali dinamično pogojno logiko, ogrodje ponuja orodja za izgradnjo zmogljivih, skalabilnih in tipno varnih AI-podprtih rešitev.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Omejitev odgovornosti**:
Ta dokument je bil preveden z uporabo AI prevajalske storitve [Co-op Translator](https://github.com/Azure/co-op-translator). Čeprav si prizadevamo za natančnost, vas prosimo, da upoštevate, da avtomatizirani prevodi lahko vsebujejo napake ali netočnosti. Izvirni dokument v njegovem izvirnem jeziku je treba obravnavati kot avtoritativni vir. Za kritične informacije je priporočljiv strokovni človeški prevod. Ne odgovarjamo za morebitna nesporazume ali napačne interpretacije, ki izhajajo iz uporabe tega prevoda.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->