# Gradnja aplikacij z več agenti z uporabo Microsoft Agent Framework Workflow

Ta vadnica vas bo vodila skozi razumevanje in gradnjo aplikacij z več agenti z uporabo Microsoft Agent Framework. Raziskali bomo osnovne koncepte sistemov z več agenti, se poglobili v arhitekturo komponent Workflow v okviru in preučili praktične primere v Pythonu in .NET za različne vzorce delovnih tokov.

## 1\. Razumevanje sistemov z več agenti

AI agent je sistem, ki presega zmogljivosti standardnega modela velikih jezikov (LLM). Lahko zaznava svoje okolje, sprejema odločitve in izvaja dejanja za dosego določenih ciljev. Sistem z več agenti vključuje več teh agentov, ki sodelujejo pri reševanju problema, ki bi bil za enega agenta težaven ali nemogoč.

### Pogosti scenariji uporabe

  * **Reševanje kompleksnih problemov**: Razdelitev velike naloge (npr. načrtovanje dogodka za celotno podjetje) na manjše podnaloge, ki jih obravnavajo specializirani agenti (npr. agent za proračun, agent za logistiko, agent za marketing).
  * **Virtualni asistenti**: Glavni asistent delegira naloge, kot so načrtovanje, raziskovanje in rezervacije, drugim specializiranim agentom.
  * **Avtomatizirano ustvarjanje vsebine**: Delovni tok, kjer en agent pripravi osnutek vsebine, drugi preveri točnost in ton, tretji pa objavi vsebino.

### Vzorci sistemov z več agenti

Sistemi z več agenti se lahko organizirajo v več vzorcev, ki določajo, kako medsebojno delujejo:

  * **Zaporedni**: Agenti delujejo v vnaprej določenem vrstnem redu, podobno kot na proizvodni liniji. Izhod enega agenta postane vhod za naslednjega.
  * **Sočasni**: Agenti delujejo vzporedno na različnih delih naloge, njihovi rezultati pa se na koncu združijo.
  * **Pogojni**: Delovni tok sledi različnim potem glede na izhod agenta, podobno kot stavek if-then-else.

## 2\. Arhitektura Workflow v Microsoft Agent Framework

Sistem delovnega toka v Agent Framework je napreden orkestracijski motor, zasnovan za upravljanje kompleksnih interakcij med več agenti. Temelji na arhitekturi, ki uporablja [Pregel-style execution model](https://kowshik.github.io/JPregel/pregel_paper.pdf), kjer obdelava poteka v sinhroniziranih korakih, imenovanih "supersteps".

### Osnovne komponente

Arhitektura je sestavljena iz treh glavnih delov:

1.  **Izvajalci**: To so osnovne enote za obdelavo. V naših primerih je `Agent` vrsta izvajalca. Vsak izvajalec lahko ima več obdelovalcev sporočil, ki se samodejno sprožijo glede na vrsto prejetega sporočila.
2.  **Povezave**: Določajo pot, po kateri sporočila potujejo med izvajalci. Povezave lahko imajo pogoje, kar omogoča dinamično usmerjanje informacij skozi graf delovnega toka.
3.  **Workflow**: Ta komponenta orkestrira celoten proces, upravlja izvajalce, povezave in celoten tok obdelave. Zagotavlja, da se sporočila obdelajo v pravilnem vrstnem redu in pretaka dogodke za opazovanje.

*Diagram, ki prikazuje osnovne komponente sistema delovnega toka.*

Ta struktura omogoča gradnjo robustnih in skalabilnih aplikacij z uporabo osnovnih vzorcev, kot so zaporedne verige, fan-out/fan-in za vzporedno obdelavo in logika switch-case za pogojne tokove.

## 3\. Praktični primeri in analiza kode

Zdaj si bomo ogledali, kako implementirati različne vzorce delovnih tokov z uporabo okvira. Preučili bomo primere kode v Pythonu in .NET za vsak primer.

### Primer 1: Osnovni zaporedni delovni tok

To je najpreprostejši vzorec, kjer se izhod enega agenta neposredno prenese na drugega. Naš scenarij vključuje hotelskega agenta `FrontDesk`, ki poda priporočilo za potovanje, ki ga nato pregleda agent `Concierge`.

*Diagram osnovnega delovnega toka FrontDesk -\> Concierge.*

#### Ozadje scenarija

Popotnik prosi za priporočilo v Parizu.

1.  Agent `FrontDesk`, zasnovan za jedrnatost, predlaga obisk muzeja Louvre.
2.  Agent `Concierge`, ki daje prednost pristnim izkušnjam, prejme ta predlog. Pregleda priporočilo in poda povratne informacije, predlaga bolj lokalno, manj turistično alternativo.

#### Analiza implementacije v Pythonu

V Pythonu najprej definiramo in ustvarimo dva agenta, vsak s specifičnimi navodili.

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

Nato uporabimo `WorkflowBuilder` za sestavo grafa. `front_desk_agent` je nastavljen kot začetna točka, in ustvarjena je povezava za povezavo njegovega izhoda z `reviewer_agent`.

```python
# 01.python-agent-framework-workflow-ghmodel-basic.ipynb

workflow = WorkflowBuilder().set_start_executor(front_desk_agent).add_edge(front_desk_agent, reviewer_agent).build()
```

Na koncu se delovni tok izvede z začetnim uporabniškim pozivom.

```python
# 01.python-agent-framework-workflow-ghmodel-basic.ipynb

result =''
# The run_stream method executes the workflow and streams events.
async for event in workflow.run_stream('I would like to go to Paris.'):
    if isinstance(event, WorkflowEvent):
        result += str(event.data)
```

#### Analiza implementacije v .NET (C\#)

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

Agenti so ustvarjeni z uporabo `OpenAIClient`, nato pa `WorkflowBuilder` definira zaporedni tok z dodajanjem povezave od `frontDeskAgent` do `reviewerAgent`.

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

Delovni tok se nato zažene z uporabnikovim sporočilom, rezultati pa se pretakajo nazaj.

### Primer 2: Večstopenjski zaporedni delovni tok

Ta vzorec razširi osnovno zaporedje z vključitvijo več agentov. Idealen je za procese, ki zahtevajo več stopenj izboljšanja ali preoblikovanja.

#### Ozadje scenarija

Uporabnik priskrbi sliko dnevne sobe in zahteva ponudbo za pohištvo.

1.  **Sales-Agent**: Identificira pohištvene predmete na sliki in ustvari seznam.
2.  **Price-Agent**: Vzame seznam predmetov in poda podroben cenovni razčlenitev, vključno z možnostmi za proračun, srednji razred in premium.
3.  **Quote-Agent**: Prejme cenovni seznam in ga oblikuje v formalni dokument ponudbe v Markdownu.

*Diagram delovnega toka Sales -\> Price -\> Quote.*

#### Analiza implementacije v Pythonu

Trije agenti so definirani, vsak s specializirano vlogo. Delovni tok je sestavljen z uporabo `add_edge` za ustvarjanje verige: `sales_agent` -\> `price_agent` -\> `quote_agent`.

```python
# 02.python-agent-framework-workflow-ghmodel-sequential.ipynb

# Create three specialized agents
sales_agent = chat_client.create_agent(...)
price_agent = chat_client.create_agent(...)
quote_agent = chat_client.create_agent(...)

# Build the sequential workflow
workflow = WorkflowBuilder().set_start_executor(sales_agent).add_edge(sales_agent, price_agent).add_edge(price_agent, quote_agent).build()
```

Vhod je `ChatMessage`, ki vključuje tako besedilo kot URI slike. Okvir obravnava prenos izhoda vsakega agenta na naslednjega v zaporedju, dokler ni ustvarjena končna ponudba.

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

#### Analiza implementacije v .NET (C\#)

Primer v .NET odraža različico v Pythonu. Trije agenti (`salesagent`, `priceagent`, `quoteagent`) so ustvarjeni. `WorkflowBuilder` jih poveže zaporedno.

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

Uporabnikovo sporočilo je sestavljeno z obema podatkoma slike (kot bajti) in besedilnim pozivom. Metoda `InProcessExecution.StreamAsync` sproži delovni tok, končni izhod pa se zajame iz toka.

### Primer 3: Sočasni delovni tok

Ta vzorec se uporablja, ko je naloge mogoče izvajati hkrati za prihranek časa. Vključuje "fan-out" za več agentov in "fan-in" za združevanje rezultatov.

#### Ozadje scenarija

Uporabnik prosi za načrtovanje potovanja v Seattle.

1.  **Dispatcher (Fan-Out)**: Uporabnikova zahteva se pošlje dvema agentoma hkrati.
2.  **Researcher-Agent**: Raziskuje znamenitosti, vreme in ključne vidike za potovanje v Seattle decembra.
3.  **Plan-Agent**: Neodvisno ustvari podroben dnevni načrt potovanja.
4.  **Aggregator (Fan-In)**: Izhodi obeh, raziskovalca in načrtovalca, se zberejo in predstavijo skupaj kot končni rezultat.

*Diagram sočasnega delovnega toka Researcher in Planner.*

#### Analiza implementacije v Pythonu

`ConcurrentBuilder` poenostavi ustvarjanje tega vzorca. Preprosto navedete sodelujoče agente, graditelj pa samodejno ustvari potrebno logiko fan-out in fan-in.

```python
# 03.python-agent-framework-workflow-ghmodel-concurrent.ipynb

research_agent = chat_client.create_agent(name="Researcher-Agent", ...)
plan_agent = chat_client.create_agent(name="Plan-Agent", ...)

# ConcurrentBuilder handles the fan-out/fan-in logic
workflow = ConcurrentBuilder().participants([research_agent, plan_agent]).build()

# Run the workflow
events = await workflow.run("Plan a trip to Seattle in December")
```

Okvir zagotavlja, da `research_agent` in `plan_agent` delujeta vzporedno, njihovi končni izhodi pa se zberejo v seznam.

#### Analiza implementacije v .NET (C\#)

V .NET ta vzorec zahteva bolj eksplicitno definicijo. Ustvarjeni so prilagojeni izvajalci (`ConcurrentStartExecutor` in `ConcurrentAggregationExecutor`) za obravnavo logike fan-out in fan-in.

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

`WorkflowBuilder` nato uporabi `AddFanOutEdge` in `AddFanInEdge` za sestavo grafa s temi prilagojenimi izvajalci in agenti.

```csharp
// 03.dotnet-agent-framework-workflow-ghmodel-concurrent.ipynb

var workflow = new WorkflowBuilder(startExecutor)
            .AddFanOutEdge(startExecutor, targets: [researcherAgent, plannerAgent])
            .AddFanInEdge(aggregationExecutor, sources: [researcherAgent, plannerAgent])
            .WithOutputFrom(aggregationExecutor)
            .Build();
```

### Primer 4: Pogojni delovni tok

Pogojni delovni tokovi uvajajo logiko razvejanja, ki omogoča sistemu, da sledi različnim potem glede na vmesne rezultate.

#### Ozadje scenarija

Ta delovni tok avtomatizira ustvarjanje in objavo tehnične vadnice.

1.  **Evangelist-Agent**: Napiše osnutek vadnice na podlagi danega orisa in URL-jev.
2.  **ContentReviewer-Agent**: Pregleda osnutek. Preveri, ali je število besed več kot 200.
3.  **Pogojna veja**:
      * **Če je odobreno (`Yes`)**: Delovni tok nadaljuje do `Publisher-Agent`.
      * **Če je zavrnjeno (`No`)**: Delovni tok se ustavi in poda razlog za zavrnitev.
4.  **Publisher-Agent**: Če je osnutek odobren, ta agent shrani vsebino v Markdown datoteko.

#### Analiza implementacije v Pythonu

Ta primer uporablja prilagojeno funkcijo `select_targets` za implementacijo pogojne logike. Funkcija se prenese v `add_multi_selection_edge_group` in usmerja delovni tok na podlagi polja `review_result` iz izhoda pregledovalca.

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

Prilagojeni izvajalci, kot je `to_reviewer_result`, se uporabljajo za razčlenitev JSON izhoda agentov in pretvorbo v močno tipizirane objekte, ki jih funkcija za izbiro lahko pregleda.

#### Analiza implementacije v .NET (C\#)

Različica v .NET uporablja podoben pristop s funkcijo pogoja. Definiran je `Func<object?, bool>` za preverjanje lastnosti `Result` objekta `ReviewResult`.

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

Parameter `condition` metode `AddEdge` omogoča `WorkflowBuilder`, da ustvari razvejano pot. Delovni tok bo sledil povezavi do `publishExecutor` le, če funkcija pogoja `GetCondition(expectedResult: "Yes")` vrne true. Sicer sledi poti do `sendReviewerExecutor`.

## Zaključek

Microsoft Agent Framework Workflow ponuja robustno in prilagodljivo osnovo za orkestracijo kompleksnih sistemov z več agenti. Z izkoriščanjem njegove grafične arhitekture in osnovnih komponent lahko razvijalci oblikujejo in implementirajo sofisticirane delovne tokove v Pythonu in .NET. Ne glede na to, ali vaša aplikacija zahteva preprosto zaporedno obdelavo, vzporedno izvajanje ali dinamično pogojno logiko, okvir ponuja orodja za gradnjo zmogljivih, skalabilnih in tipiziranih rešitev, ki jih poganja AI.

---

**Omejitev odgovornosti**:  
Ta dokument je bil preveden z uporabo storitve AI za prevajanje [Co-op Translator](https://github.com/Azure/co-op-translator). Čeprav si prizadevamo za natančnost, vas prosimo, da upoštevate, da lahko avtomatizirani prevodi vsebujejo napake ali netočnosti. Izvirni dokument v njegovem izvirnem jeziku je treba obravnavati kot avtoritativni vir. Za ključne informacije priporočamo profesionalni človeški prevod. Ne prevzemamo odgovornosti za morebitna nesporazumevanja ali napačne razlage, ki izhajajo iz uporabe tega prevoda.