# Izgradnja Višeagentnih Aplikacija s Microsoft Agent Framework Workflow

Ovaj vodič će vas provesti kroz razumijevanje i izradu višeagentnih aplikacija koristeći Microsoft Agent Framework. Istražit ćemo osnovne koncepte višeagentnih sustava, zaroniti u arhitekturu komponenti Workflow okvira te proći kroz praktične primjere u Pythonu i .NET-u za različite obrasce tijeka rada.

## 1\. Razumijevanje Višeagentnih Sustava

AI agent je sustav koji nadilazi mogućnosti standardnog velikog jezičnog modela (LLM). Može percipirati svoje okruženje, donositi odluke i poduzimati radnje za postizanje određenih ciljeva. Višeagentni sustav uključuje nekoliko takvih agenata koji surađuju u rješavanju problema koji bi bilo teško ili nemoguće riješiti jednim agentom.

### Uobičajeni Scenariji Primjene

  * **Rješavanje složenih problema**: Razbijanje velikog zadatka (npr. planiranje događaja za cijelu tvrtku) na manje podzadatke kojima upravljaju specijalizirani agenti (npr. agent za budžet, agent za logistiku, agent za marketing).
  * **Virtualni asistenti**: Glavni pomoćni agent koji delegira zadatke poput zakazivanja, istraživanja i rezervacija drugim specijaliziranim agentima.
  * **Automatizirana kreacija sadržaja**: Tijek rada u kojem jedan agent izrađuje nacrt sadržaja, drugi ga pregledava radi točnosti i tona, a treći ga objavljuje.

### Obrasci Višeagenta

Višeagentni sustavi mogu se organizirati u nekoliko obrazaca koji određuju način njihove interakcije:

  * **Sekvencijski**: Agenti rade u unaprijed određenom redoslijedu, poput proizvodne trakе. Izlaz jednog agenta postaje ulaz sljedećeg.
  * **Paralelni**: Agenti rade paralelno na različitim dijelovima zadatka, a njihovi se rezultati na kraju objedine.
  * **Uvjetni**: Tijek rada prati različite putanje na temelju izlaza agenta, slično izrazu ako-onda-inače.

## 2\. Arhitektura Microsoft Agent Framework Workflow

Sustav tijeka rada Agent Frameworka je napredni motor orkestracije dizajniran za upravljanje složenim interakcijama između višestrukih agenata. Izgrađen je na arhitekturi zasnovanoj na grafu koja koristi [Pregel-style execution model](https://kowshik.github.io/JPregel/pregel_paper.pdf), gdje se obrada događa u sinkroniziranim koracima nazvanim "supersteps."

### Temeljne Komponente

Arhitektura se sastoji od tri glavna dijela:

1.  **Izvršitelji (Executors)**: Ovo su temeljne jedinice obrade. U našim primjerima, `Agent` je tip izvršitelja. Svaki izvršitelj može imati više rukovatelja poruka koji se automatski pozivaju ovisno o tipu primljene poruke.
2.  **Rubovi (Edges)**: Definiraju put kojim poruke putuju između izvršitelja. Rubovi mogu imati uvjete, što omogućuje dinamičko usmjeravanje informacija kroz graf tijeka rada.
3.  **Workflow**: Ova komponenta orkestrira cijeli proces, upravljajući izvršiteljima, rubovima i cjelokupnim tokom izvršavanja. Osigurava da se poruke obrađuju u ispravnom redoslijedu i struji događaje za mogućnost nadzora.

*Dijagram koji ilustrira temeljne komponente sustava tijeka rada.*

Ova struktura omogućuje izgradnju robusnih i skalabilnih aplikacija koristeći temeljne obrasce poput sekvencijskih lanaca, fan-out/fan-in za paralelnu obradu i switch-case logiku za uvjetne tokove.

## 3\. Praktični Primjeri i Analiza Koda

Sada ćemo istražiti kako implementirati različite obrasce tijeka rada koristeći okvir. Pogledat ćemo i Python i .NET kod za svaki primjer.

### Slučaj 1: Osnovni Sekvencijski Tijek Rada

Ovo je najjednostavniji obrazac, gdje se izlaz jednog agenta izravno prosljeđuje drugom. Naš scenarij uključuje hotelarskog `FrontDesk` agenta koji daje putnički prijedlog, a zatim ga pregledava agent `Concierge`.

*Dijagram osnovnog FrontDesk -> Concierge tijeka rada.*

#### Pozadina Scenarija

Putnik traži preporuku za Pariz.

1.  Agent `FrontDesk`, dizajniran za sažetost, predlaže posjet Muzeju Louvre.
2.  Agent `Concierge`, koji daje prednost autentičnim iskustvima, prima ovu preporuku. Pregledava preporuku i pruža povratnu informaciju, predlažući lokalniju, manje turističku alternativu.

#### Analiza Python Implementacije

U Python primjeru najprije definiramo i kreiramo dva agenta, svaki sa specifičnim uputama.

```python
# 01.python-agent-framework-workflow-ghmodel-basic.ipynb

# Definiraj uloge agenata i upute
REVIEWER_NAME = "Concierge"
REVIEWER_INSTRUCTIONS = """
    You are a hotel concierge who has opinions about providing the most local and authentic experiences for travelers...
    """

FRONTDESK_NAME = "FrontDesk"
FRONTDESK_INSTRUCTIONS = """
    You are a Front Desk Travel Agent with ten years of experience and are known for brevity...
    """

# Kreiraj instance agenata
reviewer_agent = chat_client.as_agent(
    instructions=(REVIEWER_INSTRUCTIONS),
    name=REVIEWER_NAME,
)

front_desk_agent = chat_client.as_agent(
    instructions=(FRONTDESK_INSTRUCTIONS),
    name=FRONTDESK_NAME,
)
```

Zatim se koristi `WorkflowBuilder` za izgradnju grafa. `front_desk_agent` se postavlja kao početna točka, a rub je kreiran za povezivanje njegovog izlaza s `reviewer_agent`.

```python
# 01.python-agent-framework-workflow-ghmodel-basic.ipynb

workflow = WorkflowBuilder(start_executor=front_desk_agent).add_edge(front_desk_agent, reviewer_agent).build()
```

Na kraju, tijek rada se izvodi s početnim upitom korisnika.

```python
# 01.python-agent-framework-workflow-ghmodel-basic.ipynb

result =''
# run izvršava tijek rada; get_outputs() vraća rezultat izvršitelja izlaza.
events = await workflow.run('I would like to go to Paris.')
outputs = events.get_outputs()
result = outputs[0].text if outputs else ''
```

#### Analiza .NET (C\#) Implementacije

.NET implementacija slijedi vrlo sličnu logiku. Najprije se definiraju konstante za imena agenata i upute.

```csharp
// 01.dotnet-agent-framework-workflow-ghmodel-basic.ipynb

const string ReviewerAgentName = "Concierge";
const string ReviewerAgentInstructions = @"
    You are a hotel concierge who has opinions about providing the most local and authentic experiences for travelers...";

const string FrontDeskAgentName = "FrontDesk";
const string FrontDeskAgentInstructions = @"""
    You are a Front Desk Travel Agent with ten years of experience and are known for brevity...";
```

Agenti se kreiraju korištenjem `AzureOpenAIClient` (Responses API), a zatim `WorkflowBuilder` definira sekvencijski tok dodavanjem ruba od `frontDeskAgent` do `reviewerAgent`.

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

Tijek rada se potom izvršava s korisničkom porukom, a rezultati se strimuju natrag.

### Slučaj 2: Višestupanjski Sekvencijski Tijek Rada

Ovaj obrazac proširuje osnovnu sekvencu uključujući više agenata. Izvrsno je za procese koji zahtijevaju više faza dorade ili transformacije.

#### Pozadina Scenarija

Korisnik dostavlja sliku dnevnog boravka i traži ponudu za namještaj.

1.  **Prodajni agent**: Identificira stavke namještaja na slici i sastavlja popis.
2.  **Agent za cijene**: Uzima popis stavki i daje detaljan prijedlog cijena, uključujući opcije proračuna, srednjeg ranga i premium klase.
3.  **Agent za ponudu**: Prima cjenovni popis i formatira ga u formalni dokument ponude u Markdown formatu.

*Dijagram tijeka Sales -> Price -> Quote.*

#### Analiza Python Implementacije

Definiraju se tri agenta, svaki sa specijaliziranom ulogom. Tijek rada se gradi korištenjem `add_edge` za stvaranje lanca: `sales_agent` -> `price_agent` -> `quote_agent`.

```python
# 02.python-agent-framework-workflow-ghmodel-sequential.ipynb

# Kreirajte tri specijalizirana agenta
sales_agent = chat_client.as_agent(...)
price_agent = chat_client.as_agent(...)
quote_agent = chat_client.as_agent(...)

# Izgradite sekvencijalni tijek rada
workflow = WorkflowBuilder(start_executor=sales_agent).add_edge(sales_agent, price_agent).add_edge(price_agent, quote_agent).build()
```

Ulaz je `ChatMessage` koji uključuje i tekst i URI slike. Framework rukuje prenošenjem izlaza svakog agenta sljedećem u nizu dok se ne generira konačna ponuda.

```python
# 02.python-agent-framework-workflow-ghmodel-sequential.ipynb

# Poruka korisnika sadrži i tekst i sliku
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

.NET primjer odražava Python verziju. Kreiraju se tri agenta (`salesagent`, `priceagent`, `quoteagent`). `WorkflowBuilder` ih povezuje sekvencijski.

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

Korisnička poruka se konstruira s podacima o slici (kao bajtovi) i tekstualnim upitom. Metoda `InProcessExecution.RunStreamingAsync` započinje tijek rada, a konačni izlaz se hvata iz streama.

### Slučaj 3: Paralelni Tijek Rada

Ovaj obrazac se koristi kada se zadaci mogu obavljati istovremeno radi uštede vremena. Uključuje "fan-out" ka višestrukim agentima i "fan-in" za objedinjavanje rezultata.

#### Pozadina Scenarija

Korisnik traži planiranje putovanja u Seattle.

1.  **Dispatcher (fan-out)**: Korisnikov zahtjev se istovremeno šalje dvama agentima.
2.  **Agent istraživač**: Istražuje atrakcije, vrijeme i ključne čimbenike za putovanje u Seattle u prosincu.
3.  **Agent planer**: Neovisno kreira detaljan dnevni itinerar putovanja.
4.  **Aggregator (fan-in)**: Izlazi od istraživača i planera se prikupljaju i zajedno prikazuju kao konačni rezultat.

*Dijagram paralelnog tijeka Researcher i Planner.*

#### Analiza Python Implementacije

`ConcurrentBuilder` pojednostavljuje izgradnju ovog obrasca. Dovoljno je navesti sudjelujuće agente, a builder automatski kreira potrebnu logiku fan-out i fan-in.

```python
# 03.python-agent-framework-workflow-ghmodel-concurrent.ipynb

research_agent = chat_client.as_agent(name="Researcher-Agent", ...)
plan_agent = chat_client.as_agent(name="Plan-Agent", ...)

# ConcurrentBuilder upravlja logikom raširenja i skupljanja
workflow = ConcurrentBuilder().participants([research_agent, plan_agent]).build()

# Pokreni tijek rada
events = await workflow.run("Plan a trip to Seattle in December")
```

Framework osigurava da se `research_agent` i `plan_agent` izvode paralelno, a njihovi konačni izlazi prikupljaju u listu.

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

`WorkflowBuilder` potom koristi `AddFanOutEdge` i `AddFanInEdge` za izgradnju grafa s ovim prilagođenim izvršiteljima i agentima.

```csharp
// 03.dotnet-agent-framework-workflow-ghmodel-concurrent.ipynb

var workflow = new WorkflowBuilder(startExecutor)
            .AddFanOutEdge(startExecutor, targets: [researcherAgent, plannerAgent])
            .AddFanInEdge(aggregationExecutor, sources: [researcherAgent, plannerAgent])
            .WithOutputFrom(aggregationExecutor)
            .Build();
```

### Slučaj 4: Uvjetni Tijek Rada

Uvjetni tijekovi rada uvode granu logiku, dopuštajući sustavu da slijedi različite puteve temeljene na međurezultatima.

#### Pozadina Scenarija

Ovaj tijek rada automatizira izradu i objavu tehničkog vodiča.

1.  **Evangelist-Agent**: Piše nacrt vodiča na temelju danog sažetka i URL-ova.
2.  **ContentReviewer-Agent**: Pregledava nacrt. Provjerava je li broj riječi veći od 200.
3.  **Uvjetna grana**:
      * **Ako je odobreno (`Yes`)**: Tijek rada nastavlja se prema `Publisher-Agent`.
      * **Ako je odbijeno (`No`)**: Tijek rada se zaustavlja i ispisuje razlog odbijanja.
4.  **Publisher-Agent**: Ako je nacrt odobren, ovaj agent sprema sadržaj u Markdown datoteku.

#### Analiza Python Implementacije

Ovaj primjer koristi prilagođenu funkciju `select_targets` za implementaciju uvjetne logike. Funkcija se prosljeđuje u `add_multi_selection_edge_group` i usmjerava tijek rada prema polju `review_result` iz izlaza recenzenta.

```python
# 04.python-agent-framework-workflow-aifoundry-condition.ipynb

# Ova funkcija određuje sljedeći korak na temelju rezultata pregleda
def select_targets(review: ReviewResult, target_ids: list[str]) -> list[str]:
    handle_review_id, save_draft_id = target_ids
    if review.review_result == "Yes":
        # Ako je odobreno, nastavi do izvršitelja 'save_draft'
        return [save_draft_id]
    else:
        # Ako je odbijeno, nastavi do izvršitelja 'handle_review' za prijavu neuspjeha
        return [handle_review_id]

# Graditelj tijeka rada koristi funkciju odabira za usmjeravanje
workflow = (
    WorkflowBuilder()
        .set_start_executor(evangelist_agent)
        .add_edge(evangelist_agent, reviewer_agent)
        .add_edge(reviewer_agent, to_reviewer_result)
        # Višestruki rub za odabir implementira uvjetnu logiku
        .add_multi_selection_edge_group(
            to_reviewer_result,
            [handle_review, save_draft],
            selection_func=select_targets,
        )
        .add_edge(save_draft, publisher_agent)
        .build()
)
```

Prilagođeni izvršitelji poput `to_reviewer_result` koriste se za parsiranje JSON izlaza agenata i pretvaranje u strogo tipizirane objekte koje funkcija selekcije može pregledati.

#### Analiza .NET (C\#) Implementacije

.NET verzija koristi sličan pristup s funkcijom uvjeta. Definira se `Func<object?, bool>` za provjeru `Result` svojstva objekta `ReviewResult`.

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

`AddEdge` metoda s parametrima `condition` omogućuje `WorkflowBuilderu` kreiranje grananja toka. Tijek rada će slijediti rub do `publishExecutor` samo ako uvjet `GetCondition(expectedResult: "Yes")` vrati true. Inače slijedi put do `sendReviewerExecutor`.

## Zaključak

Microsoft Agent Framework Workflow pruža robusnu i fleksibilnu osnovu za orkestraciju složenih višeagentnih sustava. Iskorištavanjem njegove arhitekture zasnovane na grafu i temeljnih komponenti, programeri mogu dizajnirati i implementirati sofisticirane tijekove rada u Pythonu i .NET-u. Bilo da vaša aplikacija zahtijeva jednostavnu sekvencijsku obradu, paralelno izvršavanje ili dinamičku uvjetnu logiku, okvir nudi alate za izgradnju moćnih, skalabilnih i tipno sigurnih AI-pokretanih rješenja.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Napomena**:
Ovaj dokument je preveden korištenjem AI prevoditeljskog servisa [Co-op Translator](https://github.com/Azure/co-op-translator). Iako težimo točnosti, imajte na umu da automatski prijevodi mogu sadržavati greške ili netočnosti. Izvorni dokument na izvornom jeziku treba smatrati autoritativnim izvorom. Za važne informacije preporuča se profesionalni ljudski prijevod. Nismo odgovorni za bilo kakva nesporazumevanja ili pogrešne interpretacije koje proizlaze iz korištenja ovog prijevoda.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->