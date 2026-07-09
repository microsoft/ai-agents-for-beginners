# Izgradnja Višeagentnih Aplikacija pomoću Microsoft Agent Framework Workflow-a

Ovaj vodič će vas provesti kroz razumijevanje i izgradnju višeagentnih aplikacija koristeći Microsoft Agent Framework. Istražit ćemo osnovne koncepte višeagentnih sustava, zaroniti u arhitekturu Workflow komponente framework-a i proći kroz praktične primjere u Pythona i .NET-a za različite obrasce workflow-a.

## 1\. Razumijevanje Višeagentnih Sustava

AI Agent je sustav koji nadilazi mogućnosti standardnog Velikog Jezičnog Modela (LLM). Može percipirati svoju okolinu, donositi odluke i poduzimati radnje za postizanje određenih ciljeva. Višeagentni sustav uključuje nekoliko ovih agenata koji surađuju na rješavanju problema koji bi bilo teško ili nemoguće riješiti samostalno jednim agentom.

### Uobičajeni Scenariji Primjene

  * **Rješavanje Složenih Problema**: Razbijanje velikog zadatka (npr., planiranje događanja za cijelu tvrtku) na manje podzadatke koje obavljaju specijalizirani agenti (npr., agent za budžet, agent za logistiku, agent za marketing).
  * **Virtualni Asistenti**: Primarni pomoćni agent koji delegira zadatke poput zakazivanja, istraživanja i rezervacija drugim specijaliziranim agentima.
  * **Automatizirano Kreiranje Sadržaja**: Workflow u kojem jedan agent sastavlja sadržaj, drugi ga pregledava radi točnosti i tona, a treći ga objavljuje.

### Obrasci Višeagenta

Višeagentni sustavi mogu biti organizirani u nekoliko obrazaca, koji određuju kako međusobno djeluju:

  * **Sekvencijski**: Agenti rade u unaprijed određenom redoslijedu, poput sklapanja na traci. Izlaz jednog agenta postaje ulaz za sljedećeg.
  * **Paralelni**: Agenti rade paralelno na različitim dijelovima zadatka, a njihovi se rezultati na kraju zbrajaju.
  * **Uvjetni**: Workflow prati različite putove na temelju izlaza agenta, slično if-then-else izrazu.

## 2\. Arhitektura Microsoft Agent Framework Workflow-a

Workflow sustav Agent Framework-a je napredni orkestracijski motor dizajniran za upravljanje složenim interakcijama između više agenata. Izgrađen je na arhitekturi baziranoj na grafu koja koristi [Pregel-style execution model](https://kowshik.github.io/JPregel/pregel_paper.pdf), gdje se obrada odvija u sinkroniziranim koracima nazvanim "supersteps."

### Osnovne Komponente

Arhitektura se sastoji od tri glavna dijela:

1.  **Izvršitelji**: To su osnovne jedinice za obradu. U našim primjerima, `Agent` je tip izvršitelja. Svaki izvršitelj može imati višestruke rukovatelje poruka koji se automatski pozivaju na temelju vrste primljene poruke.
2.  **Rubovi**: Oni definiraju put kojim poruke putuju između izvršitelja. Rubovi mogu imati uvjete, što omogućuje dinamičko usmjeravanje informacija kroz graf workflow-a.
3.  **Workflow**: Ova komponenta orkestrira cijeli proces, upravljajući izvršiteljima, rubovima i ukupnim tijek izvršenja. Osigurava da se poruke obrađuju u ispravnom redoslijedu i emitira događaje za promatranje.

*Dijagram koji ilustrira osnovne komponente workflow sustava.*

Ova struktura omogućuje izgradnju robusnih i skalabilnih aplikacija koristeći osnovne obrasce poput sekvencijskih lanaca, fan-out/fan-in za paralelnu obradu i uvjetnu logiku switch-case.

## 3\. Praktični Primjeri i Analiza Koda

Sada ćemo istražiti kako implementirati različite obrasce workflow-a koristeći framework. Pogledat ćemo kod u Pythonu i .NET-u za svaki primjer.

### Primjer 1: Osnovni Sekvencijski Workflow

Ovo je najjednostavniji obrazac, gdje se izlaz jednog agenta izravno prosljeđuje drugom. Naš scenarij uključuje hotelskog agenta `FrontDesk` koji daje preporuku za putovanje, a zatim je pregledava agent `Concierge`.

*Dijagram osnovnog FrontDesk -> Concierge workflow-a.*

#### Pozadina Scenarija

Putnik traži preporuku u Parizu.

1.  Agent `FrontDesk`, dizajniran za sažetost, predlaže posjet Louvre muzeju.
2.  Agent `Concierge`, koji daje prioritet autentičnim iskustvima, prima ovaj prijedlog. Pregledava preporuku i daje povratnu informaciju, predlažući lokalniju, manje turističku alternativu.

#### Analiza Python Implementacije

U Python primjeru najprije definiramo i kreiramo dva agenta, svakog s posebnim uputama.

```python
# 01.python-agent-framework-workflow-ghmodel-basic.ipynb

# Definirajte uloge agenata i upute
REVIEWER_NAME = "Concierge"
REVIEWER_INSTRUCTIONS = """
    You are an are hotel concierge who has opinions about providing the most local and authentic experiences for travelers...
    """

FRONTDESK_NAME = "FrontDesk"
FRONTDESK_INSTRUCTIONS = """
    You are a Front Desk Travel Agent with ten years of experience and are known for brevity...
    """

# Kreirajte instance agenata
reviewer_agent = chat_client.as_agent(
    instructions=(REVIEWER_INSTRUCTIONS),
    name=REVIEWER_NAME,
)

front_desk_agent = chat_client.as_agent(
    instructions=(FRONTDESK_INSTRUCTIONS),
    name=FRONTDESK_NAME,
)
```

Zatim se koristi `WorkflowBuilder` za konstruiranje grafa. `front_desk_agent` je postavljen kao početna točka, a kreira se rub koji povezuje njegov izlaz s `reviewer_agent`.

```python
# 01.python-agent-framework-workflow-ghmodel-basic.ipynb

workflow = WorkflowBuilder(start_executor=front_desk_agent).add_edge(front_desk_agent, reviewer_agent).build()
```

Na kraju se workflow izvršava s početnim korisničkim zahtjevom.

```python
# 01.python-agent-framework-workflow-ghmodel-basic.ipynb

result =''
# run izvršava tijek rada; get_outputs() vraća rezultat izvršitelja izlaza.
events = await workflow.run('I would like to go to Paris.')
outputs = events.get_outputs()
result = outputs[0].text if outputs else ''
```

#### Analiza .NET (C\#) Implementacije

.NET implementacija slijedi vrlo sličnu logiku. Prvo se definiraju konstante za imena i upute agenata.

```csharp
// 01.dotnet-agent-framework-workflow-ghmodel-basic.ipynb

const string ReviewerAgentName = "Concierge";
const string ReviewerAgentInstructions = @"
    You are an are hotel concierge who has opinions about providing the most local and authentic experiences for travelers...";

const string FrontDeskAgentName = "FrontDesk";
const string FrontDeskAgentInstructions = @"""
    You are a Front Desk Travel Agent with ten years of experience and are known for brevity...";
```

Agenti se stvaraju koristeći `AzureOpenAIClient` (Responses API), a zatim `WorkflowBuilder` definira sekvencijski tijek dodavanjem ruba od `frontDeskAgent` do `reviewerAgent`.

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

Workflow se zatim pokreće s korisničkom porukom, a rezultati se emitiraju natrag.

### Primjer 2: Višestupanjski Sekvencijski Workflow

Ovaj obrazac proširuje osnovnu sekvencu uključivanjem više agenata. Idealan je za procese koji zahtijevaju višestruke faze dorade ili transformacije.

#### Pozadina Scenarija

Korisnik daje sliku dnevnog boravka i traži ponudu za namještaj.

1.  **Sales-Agent**: Identificira predmete namještaja na slici i sastavlja listu.
2.  **Price-Agent**: Prima listu predmeta i daje detaljan pregled cijena, uključujući budžetsku, srednju i premium ponudu.
3.  **Quote-Agent**: Prima listu s cijenama i formatira je u službeni dokument s ponudom u Markdownu.

*Dijagram Sales -> Price -> Quote workflow-a.*

#### Analiza Python Implementacije

Definirana su tri agenta, svaki sa specijaliziranom ulogom. Workflow se konstruira koristeći `add_edge` za stvaranje lanca: `sales_agent` -> `price_agent` -> `quote_agent`.

```python
# 02.python-agent-framework-workflow-ghmodel-sequential.ipynb

# Kreirajte tri specijalizirana agenta
sales_agent = chat_client.as_agent(...)
price_agent = chat_client.as_agent(...)
quote_agent = chat_client.as_agent(...)

# Izgradite sekvencijalni tijek rada
workflow = WorkflowBuilder(start_executor=sales_agent).add_edge(sales_agent, price_agent).add_edge(price_agent, quote_agent).build()
```

Ulaz je `ChatMessage` koji uključuje i tekst i URI slike. Framework upravlja prosljeđivanjem izlaza svakog agenta sljedećem u nizu dok se ne generira konačna ponuda.

```python
# 02.python-agent-framework-workflow-ghmodel-sequential.ipynb

# Korisnička poruka sadrži i tekst i sliku
message = ChatMessage(
        role=Role.USER,
        contents=[
            TextContent(text="Please find the relevant furniture..."),
            DataContent(uri=image_uri, media_type="image/png")
        ]
)

# Pokreni tijek rada
events = await workflow.run(message)
```

#### Analiza .NET (C\#) Implementacije

.NET primjer odražava Python verziju. Tri agenta (`salesagent`, `priceagent`, `quoteagent`) se kreiraju. `WorkflowBuilder` ih povezuje sekvencijski.

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

Poruka korisnika se sastavlja sa slikovnim podacima (kao bajtovi) i tekstualnim promptom. Metoda `InProcessExecution.StreamAsync` pokreće workflow, a konačni izlaz se dohvaća iz streama.

### Primjer 3: Paralelni Workflow

Ovaj obrazac se koristi kada se zadaci mogu izvršavati istovremeno radi uštede vremena. Uključuje "fan-out" na više agenata i "fan-in" za objedinjavanje rezultata.

#### Pozadina Scenarija

Korisnik traži planiranje putovanja u Seattle.

1.  **Dispatcher (Fan-Out)**: Korisnikov zahtjev se istovremeno šalje na dva agenta.
2.  **Researcher-Agent**: Istražuje atrakcije, vremenske uvjete i ključne čimbenike za putovanje u Seattle u prosincu.
3.  **Plan-Agent**: Neovisno kreira detaljan dnevni itinerar putovanja.
4.  **Aggregator (Fan-In)**: Izlazi istraživača i planer-a se prikupljaju i zajedno prikazuju kao konačni rezultat.

*Dijagram paralelnog Researcher i Planner workflow-a.*

#### Analiza Python Implementacije

`ConcurrentBuilder` pojednostavljuje stvaranje ovog obrasca. Jednostavno navedete agente koji sudjeluju, a builder automatski kreira potrebnu logiku fan-out i fan-in.

```python
# 03.python-agent-framework-workflow-ghmodel-concurrent.ipynb

research_agent = chat_client.as_agent(name="Researcher-Agent", ...)
plan_agent = chat_client.as_agent(name="Plan-Agent", ...)

# ConcurrentBuilder upravlja logikom širenja/skupljanja
workflow = ConcurrentBuilder().participants([research_agent, plan_agent]).build()

# Pokreni tijek rada
events = await workflow.run("Plan a trip to Seattle in December")
```

Framework osigurava da `research_agent` i `plan_agent` izvršavaju paralelno, a njihovi konačni izlazi se prikupljaju u listu.

#### Analiza .NET (C\#) Implementacije

U .NET-u ovaj obrazac zahtijeva eksplicitniju definiciju. Kreiraju se prilagođeni izvršitelji (`ConcurrentStartExecutor` i `ConcurrentAggregationExecutor`) za upravljanje fan-out i fan-in logikom.

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

`WorkflowBuilder` tada koristi `AddFanOutEdge` i `AddFanInEdge` za konstruiranje grafa s ovim prilagođenim izvršiteljima i agentima.

```csharp
// 03.dotnet-agent-framework-workflow-ghmodel-concurrent.ipynb

var workflow = new WorkflowBuilder(startExecutor)
            .AddFanOutEdge(startExecutor, targets: [researcherAgent, plannerAgent])
            .AddFanInEdge(aggregationExecutor, sources: [researcherAgent, plannerAgent])
            .WithOutputFrom(aggregationExecutor)
            .Build();
```

### Primjer 4: Uvjetni Workflow

Uvjetni workflow-i uvode granu logike, dopuštajući sustavu da ide različitim putovima na temelju međurezultata.

#### Pozadina Scenarija

Ovaj workflow automatizira izradu i objavu tehničkog tutorijala.

1.  **Evangelist-Agent**: Piše nacrt tutorijala na temelju danog okvira i URL-ova.
2.  **ContentReviewer-Agent**: Pregledava nacrt. Provjerava je li broj riječi veći od 200.
3.  **Uvjetna Grana**:
      * **Ako je odobreno (`Da`)**: Workflow ide prema `Publisher-Agent`.
      * **Ako je odbijeno (`Ne`)**: Workflow završava i izlazi razlog odbijanja.
4.  **Publisher-Agent**: Ako je nacrt odobren, ovaj agent sprema sadržaj u Markdown datoteku.

#### Analiza Python Implementacije

Ovaj primjer koristi prilagođenu funkciju `select_targets` za implementaciju uvjetne logike. Ta se funkcija prosljeđuje `add_multi_selection_edge_group` i usmjerava workflow na temelju polja `review_result` u izlazu recenzenta.

```python
# 04.python-agent-framework-workflow-aifoundry-condition.ipynb

# Ova funkcija određuje sljedeći korak na temelju rezultata pregleda
def select_targets(review: ReviewResult, target_ids: list[str]) -> list[str]:
    handle_review_id, save_draft_id = target_ids
    if review.review_result == "Yes":
        # Ako je odobreno, nastavi na izvršitelja 'save_draft'
        return [save_draft_id]
    else:
        # Ako je odbijeno, nastavi na izvršitelja 'handle_review' za prijavu neuspjeha
        return [handle_review_id]

# Graditelj tijeka rada koristi funkciju odabira za usmjeravanje
workflow = (
    WorkflowBuilder()
        .set_start_executor(evangelist_agent)
        .add_edge(evangelist_agent, reviewer_agent)
        .add_edge(reviewer_agent, to_reviewer_result)
        # Višestruki izborni rub implementira uvjetnu logiku
        .add_multi_selection_edge_group(
            to_reviewer_result,
            [handle_review, save_draft],
            selection_func=select_targets,
        )
        .add_edge(save_draft, publisher_agent)
        .build()
)
```

Prilagođeni izvršitelji poput `to_reviewer_result` se koriste za parsiranje JSON izlaza agenata i konverziju u strogo tipizirane objekte koje funkcija izbora može ispitati.

#### Analiza .NET (C\#) Implementacije

Verzija u .NET-u koristi sličan pristup s funkcijom uvjeta. Definiran je `Func<object?, bool>` za provjeru svojstva `Result` objekta `ReviewResult`.

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

Parametar `condition` metode `AddEdge` omogućuje `WorkflowBuilder`u da kreira granajuću putanju. Workflow će slijediti rub do `publishExecutor` samo ako uvjet `GetCondition(expectedResult: "Yes")` vraća true. Inače slijedi put do `sendReviewerExecutor`.

## Zaključak

Microsoft Agent Framework Workflow pruža robusnu i fleksibilnu osnovu za orkestraciju složenih, višeagentnih sustava. Korištenjem njegove arhitekture bazirane na grafovima i osnovnih komponenti, developeri mogu dizajnirati i implementirati sofisticirane workflow-e u Pythonu i .NET-u. Bilo da vaša aplikacija zahtijeva jednostavnu sekvencijsku obradu, paralelno izvršenje ili dinamičku uvjetnu logiku, framework nudi alate za izgradnju moćnih, skalabilnih i tip-Sigurnih AI-podržanih rješenja.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Napomena**:
Ovaj dokument je preveden korištenjem AI prevoditeljskog servisa [Co-op Translator](https://github.com/Azure/co-op-translator). Iako težimo točnosti, imajte na umu da automatski prijevodi mogu sadržavati greške ili netočnosti. Izvorni dokument na izvornom jeziku treba smatrati autoritativnim izvorom. Za važne informacije preporuča se profesionalni ljudski prijevod. Nismo odgovorni za bilo kakva nesporazumevanja ili pogrešne interpretacije koje proizlaze iz korištenja ovog prijevoda.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->