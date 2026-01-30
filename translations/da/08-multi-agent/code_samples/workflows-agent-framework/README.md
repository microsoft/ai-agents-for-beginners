# Bygning af Multi-Agent Applikationer med Microsoft Agent Framework Workflow

Denne vejledning vil guide dig gennem forståelsen og opbygningen af multi-agent applikationer ved hjælp af Microsoft Agent Framework. Vi vil udforske de grundlæggende begreber inden for multi-agent systemer, dykke ned i arkitekturen af frameworkets Workflow-komponent og gennemgå praktiske eksempler i både Python og .NET for forskellige workflow-mønstre.

## 1\. Forståelse af Multi-Agent Systemer

En AI-agent er et system, der går ud over kapaciteterne i en standard Large Language Model (LLM). Den kan opfatte sin omverden, træffe beslutninger og udføre handlinger for at opnå specifikke mål. Et multi-agent system involverer flere af disse agenter, der samarbejder om at løse et problem, som ville være svært eller umuligt for en enkelt agent at håndtere alene.

### Almindelige Anvendelsesscenarier

  * **Kompleks Problemløsning**: Opdeling af en stor opgave (f.eks. planlægning af en virksomhedsbegivenhed) i mindre delopgaver, der håndteres af specialiserede agenter (f.eks. en budgetagent, en logistikagent, en marketingagent).
  * **Virtuelle Assistenter**: En primær assistentagent, der delegerer opgaver som planlægning, research og booking til andre specialiserede agenter.
  * **Automatiseret Indholdsskabelse**: Et workflow, hvor én agent udarbejder indhold, en anden gennemgår det for nøjagtighed og tone, og en tredje offentliggør det.

### Multi-Agent Mønstre

Multi-agent systemer kan organiseres i flere mønstre, som bestemmer, hvordan de interagerer:

  * **Sekventiel**: Agenter arbejder i en forudbestemt rækkefølge, som en samlebåndsproces. Output fra én agent bliver input for den næste.
  * **Samtidig**: Agenter arbejder parallelt på forskellige dele af en opgave, og deres resultater samles til sidst.
  * **Betinget**: Workflowet følger forskellige veje baseret på output fra en agent, ligesom en if-then-else erklæring.

## 2\. Microsoft Agent Framework Workflow Arkitektur

Agent Frameworks workflow-system er en avanceret orkestreringsmotor designet til at håndtere komplekse interaktioner mellem flere agenter. Det er bygget på en grafbaseret arkitektur, der bruger en [Pregel-stil eksekveringsmodel](https://kowshik.github.io/JPregel/pregel_paper.pdf), hvor behandlingen sker i synkroniserede trin kaldet "supersteps."

### Kernekomponenter

Arkitekturen består af tre hoveddele:

1.  **Executors**: Disse er de grundlæggende behandlingsenheder. I vores eksempler er en `Agent` en type executor. Hver executor kan have flere beskedhåndterere, der automatisk aktiveres baseret på typen af modtaget besked.
2.  **Edges**: Disse definerer stien, som beskeder tager mellem executors. Edges kan have betingelser, der tillader dynamisk routing af information gennem workflow-grafen.
3.  **Workflow**: Denne komponent orkestrerer hele processen, styrer executors, edges og den overordnede eksekveringsflow. Den sikrer, at beskeder behandles i den korrekte rækkefølge og streamer begivenheder for observabilitet.

*Et diagram, der illustrerer workflow-systemets kernekomponenter.*

Denne struktur gør det muligt at bygge robuste og skalerbare applikationer ved hjælp af grundlæggende mønstre som sekventielle kæder, fan-out/fan-in til parallel behandling og switch-case logik til betingede flows.

## 3\. Praktiske Eksempler og Kodeanalyse

Lad os nu udforske, hvordan man implementerer forskellige workflow-mønstre ved hjælp af frameworket. Vi vil se på både Python og .NET kode for hvert eksempel.

### Case 1: Grundlæggende Sekventielt Workflow

Dette er det simpleste mønster, hvor én agents output sendes direkte til en anden. Vores scenarie involverer en hotel `FrontDesk` agent, der giver en rejseanbefaling, som derefter gennemgås af en `Concierge` agent.

*Diagram af det grundlæggende FrontDesk -\> Concierge workflow.*

#### Scenarie Baggrund

En rejsende beder om en anbefaling i Paris.

1.  `FrontDesk` agenten, designet til kortfattethed, foreslår et besøg på Louvre Museum.
2.  `Concierge` agenten, der prioriterer autentiske oplevelser, modtager denne anbefaling. Den gennemgår anbefalingen og giver feedback, der foreslår et mere lokalt, mindre turistet alternativ.

#### Python Implementeringsanalyse

I Python-eksemplet definerer og opretter vi først de to agenter, hver med specifikke instruktioner.

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

Derefter bruges `WorkflowBuilder` til at konstruere grafen. `front_desk_agent` sættes som startpunkt, og en edge oprettes for at forbinde dens output til `reviewer_agent`.

```python
# 01.python-agent-framework-workflow-ghmodel-basic.ipynb

workflow = WorkflowBuilder().set_start_executor(front_desk_agent).add_edge(front_desk_agent, reviewer_agent).build()
```

Til sidst eksekveres workflowet med den oprindelige brugerforespørgsel.

```python
# 01.python-agent-framework-workflow-ghmodel-basic.ipynb

result =''
# The run_stream method executes the workflow and streams events.
async for event in workflow.run_stream('I would like to go to Paris.'):
    if isinstance(event, WorkflowEvent):
        result += str(event.data)
```

#### .NET (C\#) Implementeringsanalyse

.NET-implementeringen følger en meget lignende logik. Først defineres konstanter for agenternes navne og instruktioner.

```csharp
// 01.dotnet-agent-framework-workflow-ghmodel-basic.ipynb

const string ReviewerAgentName = "Concierge";
const string ReviewerAgentInstructions = @"
    You are an are hotel concierge who has opinions about providing the most local and authentic experiences for travelers...";

const string FrontDeskAgentName = "FrontDesk";
const string FrontDeskAgentInstructions = @"""
    You are a Front Desk Travel Agent with ten years of experience and are known for brevity...";
```

Agentene oprettes ved hjælp af en `OpenAIClient`, og derefter definerer `WorkflowBuilder` den sekventielle flow ved at tilføje en edge fra `frontDeskAgent` til `reviewerAgent`.

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

Workflowet køres derefter med brugerens besked, og resultaterne streames tilbage.

### Case 2: Multi-Step Sekventielt Workflow

Dette mønster udvider den grundlæggende sekvens til at inkludere flere agenter. Det er ideelt til processer, der kræver flere stadier af forfining eller transformation.

#### Scenarie Baggrund

En bruger sender et billede af en stue og beder om et møbeltilbud.

1.  **Sales-Agent**: Identificerer møbelgenstandene på billedet og opretter en liste.
2.  **Price-Agent**: Tager listen over genstande og giver en detaljeret prisoversigt, inklusive budget-, mellemklasse- og premium-muligheder.
3.  **Quote-Agent**: Modtager den prissatte liste og formaterer den til et formelt tilbudsdokument i Markdown.

*Diagram af Sales -\> Price -\> Quote workflow.*

#### Python Implementeringsanalyse

Tre agenter defineres, hver med en specialiseret rolle. Workflowet konstrueres ved hjælp af `add_edge` for at skabe en kæde: `sales_agent` -\> `price_agent` -\> `quote_agent`.

```python
# 02.python-agent-framework-workflow-ghmodel-sequential.ipynb

# Create three specialized agents
sales_agent = chat_client.create_agent(...)
price_agent = chat_client.create_agent(...)
quote_agent = chat_client.create_agent(...)

# Build the sequential workflow
workflow = WorkflowBuilder().set_start_executor(sales_agent).add_edge(sales_agent, price_agent).add_edge(price_agent, quote_agent).build()
```

Inputtet er en `ChatMessage`, der inkluderer både tekst og billedets URI. Frameworket håndterer overførsel af output fra hver agent til den næste i sekvensen, indtil det endelige tilbud genereres.

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

#### .NET (C\#) Implementeringsanalyse

.NET-eksemplet afspejler Python-versionen. Tre agenter (`salesagent`, `priceagent`, `quoteagent`) oprettes. `WorkflowBuilder` forbinder dem sekventielt.

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

Brugerens besked konstrueres med både billeddata (som bytes) og tekstprompten. `InProcessExecution.StreamAsync` metoden initierer workflowet, og det endelige output fanges fra streamen.

### Case 3: Samtidigt Workflow

Dette mønster bruges, når opgaver kan udføres samtidig for at spare tid. Det involverer en "fan-out" til flere agenter og en "fan-in" for at samle resultaterne.

#### Scenarie Baggrund

En bruger beder om at planlægge en tur til Seattle.

1.  **Dispatcher (Fan-Out)**: Brugerens forespørgsel sendes til to agenter på samme tid.
2.  **Researcher-Agent**: Undersøger attraktioner, vejr og nøgleovervejelser for en tur til Seattle i december.
3.  **Plan-Agent**: Opretter uafhængigt en detaljeret dag-for-dag rejseplan.
4.  **Aggregator (Fan-In)**: Output fra både forskeren og planlæggeren samles og præsenteres sammen som det endelige resultat.

*Diagram af det samtidige Researcher og Planner workflow.*

#### Python Implementeringsanalyse

`ConcurrentBuilder` forenkler oprettelsen af dette mønster. Du angiver blot de deltagende agenter, og builderen opretter automatisk den nødvendige fan-out og fan-in logik.

```python
# 03.python-agent-framework-workflow-ghmodel-concurrent.ipynb

research_agent = chat_client.create_agent(name="Researcher-Agent", ...)
plan_agent = chat_client.create_agent(name="Plan-Agent", ...)

# ConcurrentBuilder handles the fan-out/fan-in logic
workflow = ConcurrentBuilder().participants([research_agent, plan_agent]).build()

# Run the workflow
events = await workflow.run("Plan a trip to Seattle in December")
```

Frameworket sikrer, at `research_agent` og `plan_agent` eksekverer parallelt, og deres endelige output samles i en liste.

#### .NET (C\#) Implementeringsanalyse

I .NET kræver dette mønster en mere eksplicit definition. Custom executors (`ConcurrentStartExecutor` og `ConcurrentAggregationExecutor`) oprettes for at håndtere fan-out og fan-in logikken.

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

`WorkflowBuilder` bruger derefter `AddFanOutEdge` og `AddFanInEdge` til at konstruere grafen med disse custom executors og agenterne.

```csharp
// 03.dotnet-agent-framework-workflow-ghmodel-concurrent.ipynb

var workflow = new WorkflowBuilder(startExecutor)
            .AddFanOutEdge(startExecutor, targets: [researcherAgent, plannerAgent])
            .AddFanInEdge(aggregationExecutor, sources: [researcherAgent, plannerAgent])
            .WithOutputFrom(aggregationExecutor)
            .Build();
```

### Case 4: Betinget Workflow

Betingede workflows introducerer forgrenet logik, der gør det muligt for systemet at tage forskellige veje baseret på mellemliggende resultater.

#### Scenarie Baggrund

Dette workflow automatiserer oprettelsen og offentliggørelsen af en teknisk vejledning.

1.  **Evangelist-Agent**: Skriver et udkast til vejledningen baseret på en given disposition og URL'er.
2.  **ContentReviewer-Agent**: Gennemgår udkastet. Den kontrollerer, om ordantallet er over 200 ord.
3.  **Betinget Forgrening**:
      * **Hvis Godkendt (`Yes`)**: Workflowet fortsætter til `Publisher-Agent`.
      * **Hvis Afvist (`No`)**: Workflowet stopper og outputter årsagen til afvisning.
4.  **Publisher-Agent**: Hvis udkastet er godkendt, gemmer denne agent indholdet i en Markdown-fil.

#### Python Implementeringsanalyse

Dette eksempel bruger en custom funktion, `select_targets`, til at implementere den betingede logik. Denne funktion gives til `add_multi_selection_edge_group` og dirigerer workflowet baseret på `review_result` feltet fra reviewer's output.

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

Custom executors som `to_reviewer_result` bruges til at analysere JSON-output fra agenterne og konvertere det til stærkt typede objekter, som udvælgelsesfunktionen kan inspicere.

#### .NET (C\#) Implementeringsanalyse

.NET-versionen bruger en lignende tilgang med en betingelsesfunktion. En `Func<object?, bool>` defineres for at kontrollere `Result` egenskaben af `ReviewResult` objektet.

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

`AddEdge` metodens `condition` parameter gør det muligt for `WorkflowBuilder` at skabe en forgrenet sti. Workflowet vil kun følge kanten til `publishExecutor`, hvis betingelsen `GetCondition(expectedResult: "Yes")` returnerer sand. Ellers følger det stien til `sendReviewerExecutor`.

## Konklusion

Microsoft Agent Framework Workflow giver et robust og fleksibelt fundament for orkestrering af komplekse multi-agent systemer. Ved at udnytte dets grafbaserede arkitektur og kernekomponenter kan udviklere designe og implementere sofistikerede workflows i både Python og .NET. Uanset om din applikation kræver simpel sekventiel behandling, parallel eksekvering eller dynamisk betinget logik, tilbyder frameworket værktøjerne til at bygge kraftfulde, skalerbare og type-sikre AI-drevne løsninger.

---

**Ansvarsfraskrivelse**:  
Dette dokument er blevet oversat ved hjælp af AI-oversættelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selvom vi bestræber os på nøjagtighed, skal det bemærkes, at automatiserede oversættelser kan indeholde fejl eller unøjagtigheder. Det originale dokument på dets oprindelige sprog bør betragtes som den autoritative kilde. For kritisk information anbefales professionel menneskelig oversættelse. Vi påtager os ikke ansvar for misforståelser eller fejltolkninger, der måtte opstå som følge af brugen af denne oversættelse.