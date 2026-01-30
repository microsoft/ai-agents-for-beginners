# Izrada aplikacija s više agenata pomoću Microsoft Agent Framework Workflowa

Ovaj vodič će vas provesti kroz razumijevanje i izradu aplikacija s više agenata koristeći Microsoft Agent Framework. Istražit ćemo osnovne koncepte sustava s više agenata, detaljno analizirati arhitekturu Workflow komponenti okvira i proći kroz praktične primjere u Pythonu i .NET-u za različite obrasce rada.

## 1\. Razumijevanje sustava s više agenata

AI agent je sustav koji nadilazi mogućnosti standardnog velikog jezičnog modela (LLM). Može opažati svoje okruženje, donositi odluke i poduzimati radnje kako bi postigao određene ciljeve. Sustav s više agenata uključuje nekoliko takvih agenata koji surađuju kako bi riješili problem koji bi bio težak ili nemoguć za jednog agenta.

### Uobičajeni scenariji primjene

  * **Rješavanje složenih problema**: Razbijanje velikog zadatka (npr. planiranje događaja za cijelu tvrtku) na manje podzadatke koje obrađuju specijalizirani agenti (npr. agent za proračun, agent za logistiku, agent za marketing).
  * **Virtualni asistenti**: Glavni agent-asistent delegira zadatke poput zakazivanja, istraživanja i rezervacija drugim specijaliziranim agentima.
  * **Automatizirano stvaranje sadržaja**: Radni proces u kojem jedan agent izrađuje nacrt sadržaja, drugi ga pregledava radi točnosti i tona, a treći ga objavljuje.

### Obrasci sustava s više agenata

Sustavi s više agenata mogu se organizirati prema različitim obrascima koji određuju način njihove interakcije:

  * **Sekvencijalni**: Agenti rade u unaprijed definiranom redoslijedu, poput proizvodne linije. Izlaz jednog agenta postaje ulaz za sljedećeg.
  * **Istovremeni**: Agenti rade paralelno na različitim dijelovima zadatka, a njihovi rezultati se agregiraju na kraju.
  * **Uvjetni**: Radni proces slijedi različite puteve na temelju izlaza jednog agenta, slično if-then-else logici.

## 2\. Arhitektura Workflow sustava Microsoft Agent Frameworka

Workflow sustav Agent Frameworka je napredni orkestracijski motor dizajniran za upravljanje složenim interakcijama između više agenata. Izgrađen je na arhitekturi temeljenoj na grafovima koja koristi [Pregel-stil model izvršavanja](https://kowshik.github.io/JPregel/pregel_paper.pdf), gdje se obrada odvija u sinkroniziranim koracima nazvanim "superkoraci".

### Osnovne komponente

Arhitektura se sastoji od tri glavna dijela:

1.  **Izvršitelji**: To su osnovne jedinice obrade. U našim primjerima, `Agent` je vrsta izvršitelja. Svaki izvršitelj može imati više rukovatelja porukama koji se automatski pozivaju na temelju vrste primljene poruke.
2.  **Rubovi**: Definiraju put kojim poruke prolaze između izvršitelja. Rubovi mogu imati uvjete, omogućujući dinamičko usmjeravanje informacija kroz graf radnog procesa.
3.  **Workflow**: Ova komponenta orkestrira cijeli proces, upravlja izvršiteljima, rubovima i ukupnim tokom izvršavanja. Osigurava da se poruke obrađuju u ispravnom redoslijedu i emitira događaje za praćenje.

*Dijagram koji ilustrira osnovne komponente sustava radnog procesa.*

Ova struktura omogućuje izradu robusnih i skalabilnih aplikacija koristeći osnovne obrasce poput sekvencijalnih lanaca, fan-out/fan-in za paralelnu obradu i switch-case logike za uvjetne tokove.

## 3\. Praktični primjeri i analiza koda

Sada ćemo istražiti kako implementirati različite obrasce radnog procesa koristeći okvir. Pogledat ćemo primjere koda u Pythonu i .NET-u za svaki slučaj.

### Slučaj 1: Osnovni sekvencijalni radni proces

Ovo je najjednostavniji obrazac, gdje se izlaz jednog agenta izravno prosljeđuje drugom. Naš scenarij uključuje hotelskog agenta `FrontDesk` koji daje preporuku za putovanje, koju zatim pregledava agent `Concierge`.

*Dijagram osnovnog FrontDesk -\> Concierge radnog procesa.*

#### Pozadina scenarija

Putnik traži preporuku za Pariz.

1.  Agent `FrontDesk`, dizajniran za sažetost, predlaže posjet Louvre muzeju.
2.  Agent `Concierge`, koji daje prednost autentičnim iskustvima, prima ovaj prijedlog. Pregledava preporuku i daje povratnu informaciju, predlažući lokalniju, manje turističku alternativu.

#### Analiza implementacije u Pythonu

U Python primjeru prvo definiramo i kreiramo dva agenta, svaki s posebnim uputama.

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

Zatim se koristi `WorkflowBuilder` za izgradnju grafa. `front_desk_agent` postavlja se kao početna točka, a rub se kreira za povezivanje njegovog izlaza s `reviewer_agent`.

```python
# 01.python-agent-framework-workflow-ghmodel-basic.ipynb

workflow = WorkflowBuilder().set_start_executor(front_desk_agent).add_edge(front_desk_agent, reviewer_agent).build()
```

Na kraju, radni proces se izvršava s početnim korisničkim upitom.

```python
# 01.python-agent-framework-workflow-ghmodel-basic.ipynb

result =''
# The run_stream method executes the workflow and streams events.
async for event in workflow.run_stream('I would like to go to Paris.'):
    if isinstance(event, WorkflowEvent):
        result += str(event.data)
```

#### Analiza implementacije u .NET-u (C#)

Implementacija u .NET-u slijedi vrlo sličnu logiku. Prvo se definiraju konstante za imena agenata i njihove upute.

```csharp
// 01.dotnet-agent-framework-workflow-ghmodel-basic.ipynb

const string ReviewerAgentName = "Concierge";
const string ReviewerAgentInstructions = @"
    You are an are hotel concierge who has opinions about providing the most local and authentic experiences for travelers...";

const string FrontDeskAgentName = "FrontDesk";
const string FrontDeskAgentInstructions = @"""
    You are a Front Desk Travel Agent with ten years of experience and are known for brevity...";
```

Agenti se kreiraju pomoću `OpenAIClient`, a zatim `WorkflowBuilder` definira sekvencijalni tok dodavanjem ruba od `frontDeskAgent` do `reviewerAgent`.

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

Radni proces se zatim pokreće s korisničkom porukom, a rezultati se emitiraju natrag.

### Slučaj 2: Višestupanjski sekvencijalni radni proces

Ovaj obrazac proširuje osnovnu sekvencu uključivanjem više agenata. Idealan je za procese koji zahtijevaju više faza dorade ili transformacije.

#### Pozadina scenarija

Korisnik dostavlja sliku dnevnog boravka i traži ponudu za namještaj.

1.  **Sales-Agent**: Identificira komade namještaja na slici i stvara popis.
2.  **Price-Agent**: Uzima popis stavki i daje detaljnu razradu cijena, uključujući opcije za budžet, srednji raspon i premium.
3.  **Quote-Agent**: Prima popis s cijenama i formatira ga u formalni dokument ponude u Markdownu.

*Dijagram Sales -\> Price -\> Quote radnog procesa.*

#### Analiza implementacije u Pythonu

Definiraju se tri agenta, svaki sa specijaliziranom ulogom. Radni proces se konstruira pomoću `add_edge` za stvaranje lanca: `sales_agent` -\> `price_agent` -\> `quote_agent`.

```python
# 02.python-agent-framework-workflow-ghmodel-sequential.ipynb

# Create three specialized agents
sales_agent = chat_client.create_agent(...)
price_agent = chat_client.create_agent(...)
quote_agent = chat_client.create_agent(...)

# Build the sequential workflow
workflow = WorkflowBuilder().set_start_executor(sales_agent).add_edge(sales_agent, price_agent).add_edge(price_agent, quote_agent).build()
```

Ulaz je `ChatMessage` koji uključuje tekst i URI slike. Okvir automatski prosljeđuje izlaz svakog agenta sljedećem u sekvenci dok se ne generira konačna ponuda.

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

#### Analiza implementacije u .NET-u (C#)

.NET primjer odražava Python verziju. Tri agenta (`salesagent`, `priceagent`, `quoteagent`) se kreiraju. `WorkflowBuilder` ih povezuje sekvencijalno.

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

Korisnička poruka se konstruira s podacima slike (kao bajtovima) i tekstualnim upitom. Metoda `InProcessExecution.StreamAsync` pokreće radni proces, a konačni izlaz se hvata iz toka.

### Slučaj 3: Istovremeni radni proces

Ovaj obrazac koristi se kada se zadaci mogu obavljati istovremeno radi uštede vremena. Uključuje "fan-out" prema više agenata i "fan-in" za agregaciju rezultata.

#### Pozadina scenarija

Korisnik traži planiranje putovanja u Seattle.

1.  **Dispatcher (Fan-Out)**: Korisnički zahtjev šalje se istovremeno dvama agentima.
2.  **Researcher-Agent**: Istražuje atrakcije, vremenske uvjete i ključne aspekte za putovanje u Seattle u prosincu.
3.  **Plan-Agent**: Neovisno izrađuje detaljan dnevni plan putovanja.
4.  **Aggregator (Fan-In)**: Izlazi od istraživača i planera se prikupljaju i zajedno predstavljaju kao konačni rezultat.

*Dijagram istovremenog Researcher i Planner radnog procesa.*

#### Analiza implementacije u Pythonu

`ConcurrentBuilder` pojednostavljuje stvaranje ovog obrasca. Jednostavno navedete sudjelujuće agente, a graditelj automatski kreira potrebnu logiku fan-out i fan-in.

```python
# 03.python-agent-framework-workflow-ghmodel-concurrent.ipynb

research_agent = chat_client.create_agent(name="Researcher-Agent", ...)
plan_agent = chat_client.create_agent(name="Plan-Agent", ...)

# ConcurrentBuilder handles the fan-out/fan-in logic
workflow = ConcurrentBuilder().participants([research_agent, plan_agent]).build()

# Run the workflow
events = await workflow.run("Plan a trip to Seattle in December")
```

Okvir osigurava da `research_agent` i `plan_agent` rade paralelno, a njihovi konačni izlazi se prikupljaju u popis.

#### Analiza implementacije u .NET-u (C#)

U .NET-u, ovaj obrazac zahtijeva eksplicitniju definiciju. Prilagođeni izvršitelji (`ConcurrentStartExecutor` i `ConcurrentAggregationExecutor`) se kreiraju za upravljanje logikom fan-out i fan-in.

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

`WorkflowBuilder` zatim koristi `AddFanOutEdge` i `AddFanInEdge` za izgradnju grafa s ovim prilagođenim izvršiteljima i agentima.

```csharp
// 03.dotnet-agent-framework-workflow-ghmodel-concurrent.ipynb

var workflow = new WorkflowBuilder(startExecutor)
            .AddFanOutEdge(startExecutor, targets: [researcherAgent, plannerAgent])
            .AddFanInEdge(aggregationExecutor, sources: [researcherAgent, plannerAgent])
            .WithOutputFrom(aggregationExecutor)
            .Build();
```

### Slučaj 4: Uvjetni radni proces

Uvjetni radni procesi uvode logiku grananja, omogućujući sustavu da slijedi različite puteve na temelju međurezultata.

#### Pozadina scenarija

Ovaj radni proces automatizira izradu i objavu tehničkog vodiča.

1.  **Evangelist-Agent**: Piše nacrt vodiča na temelju danog okvira i URL-ova.
2.  **ContentReviewer-Agent**: Pregledava nacrt. Provjerava je li broj riječi veći od 200.
3.  **Uvjetno grananje**:
      * **Ako je odobreno (`Yes`)**: Radni proces prelazi na `Publisher-Agent`.
      * **Ako je odbijeno (`No`)**: Radni proces se zaustavlja i daje razlog odbijanja.
4.  **Publisher-Agent**: Ako je nacrt odobren, ovaj agent sprema sadržaj u Markdown datoteku.

#### Analiza implementacije u Pythonu

Ovaj primjer koristi prilagođenu funkciju `select_targets` za implementaciju uvjetne logike. Ova funkcija se prosljeđuje `add_multi_selection_edge_group` i usmjerava radni proces na temelju polja `review_result` iz izlaza recenzenta.

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

Prilagođeni izvršitelji poput `to_reviewer_result` koriste se za parsiranje JSON izlaza agenata i pretvaranje u snažno tipizirane objekte koje funkcija za odabir može pregledati.

#### Analiza implementacije u .NET-u (C#)

.NET verzija koristi sličan pristup s funkcijom uvjeta. Definira se `Func<object?, bool>` za provjeru svojstva `Result` objekta `ReviewResult`.

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

Parametar `condition` metode `AddEdge` omogućuje `WorkflowBuilderu` stvaranje grananja. Radni proces slijedi rub prema `publishExecutor` samo ako funkcija `GetCondition(expectedResult: "Yes")` vraća true. Inače, slijedi put prema `sendReviewerExecutor`.

## Zaključak

Microsoft Agent Framework Workflow pruža robusnu i fleksibilnu osnovu za orkestraciju složenih sustava s više agenata. Koristeći njegovu arhitekturu temeljenu na grafovima i osnovne komponente, programeri mogu dizajnirati i implementirati sofisticirane radne procese u Pythonu i .NET-u. Bez obzira zahtijeva li vaša aplikacija jednostavnu sekvencijalnu obradu, paralelno izvršavanje ili dinamičku uvjetnu logiku, okvir nudi alate za izradu moćnih, skalabilnih i tipiziranih AI rješenja.

---

**Izjava o odricanju odgovornosti**:  
Ovaj dokument je preveden pomoću AI usluge za prevođenje [Co-op Translator](https://github.com/Azure/co-op-translator). Iako nastojimo osigurati točnost, imajte na umu da automatski prijevodi mogu sadržavati pogreške ili netočnosti. Izvorni dokument na izvornom jeziku treba smatrati autoritativnim izvorom. Za ključne informacije preporučuje se profesionalni prijevod od strane stručnjaka. Ne preuzimamo odgovornost za nesporazume ili pogrešna tumačenja koja mogu proizaći iz korištenja ovog prijevoda.