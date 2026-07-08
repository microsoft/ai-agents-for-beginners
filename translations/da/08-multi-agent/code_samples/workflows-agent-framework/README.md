# Opbygning af Multi-Agent Applikationer med Microsoft Agent Framework Workflow

Denne vejledning vil guide dig gennem forståelse og opbygning af multi-agent applikationer ved hjælp af Microsoft Agent Framework. Vi vil udforske kernekoncepterne af multi-agent systemer, dykke ned i arkitekturen af frameworkets Workflow-komponent, og gennemgå praktiske eksempler i både Python og .NET for forskellige workflow-mønstre.

## 1\. Forståelse af Multi-Agent Systemer

En AI Agent er et system, der går ud over kapabiliteterne af en standard Large Language Model (LLM). Den kan opfatte sit miljø, træffe beslutninger og tage handlinger for at nå specifikke mål. Et multi-agent system involverer flere af disse agenter, der samarbejder om at løse et problem, som ville være svært eller umuligt for en enkelt agent at håndtere alene.

### Almindelige Anvendelsesscenarier

  * **Kompleks Problemløsning**: Opdeling af en stor opgave (f.eks. planlægning af et firmaomspændende arrangement) i mindre delopgaver håndteret af specialiserede agenter (f.eks. en budgetagent, en logistikagent, en marketingagent).
  * **Virtuelle Assistenter**: En primær assistentagent, der delegerer opgaver som kalenderstyring, research og booking til andre specialiserede agenter.
  * **Automatiseret Indholdsskabelse**: Et workflow, hvor én agent skriver udkast til indhold, en anden gennemgår det for nøjagtighed og tone, og en tredje udgiver det.

### Multi-Agent Mønstre

Multi-agent systemer kan organiseres i flere mønstre, som bestemmer, hvordan de interagerer:

  * **Sekventielt**: Agenter arbejder i en foruddefineret rækkefølge, som på en samlebånd. Outputtet fra én agent bliver inputtet for den næste.
  * **Samtidig**: Agenter arbejder parallelt på forskellige dele af en opgave, og deres resultater samles til sidst.
  * **Betinget**: Workflowet følger forskellige spor baseret på outputtet fra en agent, som en if-then-else-sætning.

## 2\. Microsoft Agent Framework Workflow Arkitektur

Agent Frameworks workflowsystem er en avanceret orkestreringsmotor designet til at håndtere komplekse interaktioner mellem flere agenter. Det er bygget på en grafbaseret arkitektur, der bruger en [Pregel-stil eksekveringsmodel](https://kowshik.github.io/JPregel/pregel_paper.pdf), hvor behandling foregår i synkroniserede trin kaldet "supersteps."

### Kernekomponenter

Arkitekturen består af tre hoveddele:

1.  **Executorer**: Disse er de fundamentale behandlingsenheder. I vores eksempler er en `Agent` en type executor. Hver executor kan have flere beskedbehandlere, som automatisk påkaldes baseret på typen af modtaget besked.
2.  **Edges**: Disse definerer vejen, som beskeder følger mellem executorerne. Edges kan have betingelser, hvilket tillader dynamisk routing af information gennem workflow-grafen.
3.  **Workflow**: Denne komponent orkestrerer hele processen, styrer executorerne, edges og den overordnede udførelsesflow. Den sikrer, at beskeder behandles i korrekt rækkefølge og streamer events for observabilitet.

*Et diagram, der illustrerer kernekomponenterne i workflowsystemet.*

Denne struktur muliggør opbygning af robuste og skalerbare applikationer ved hjælp af fundamentale mønstre som sekventielle kæder, fan-out/fan-in for parallel behandling og switch-case logik til betingede flows.

## 3\. Praktiske Eksempler og Kodeanalyse

Lad os nu udforske, hvordan forskellige workflow-mønstre implementeres ved hjælp af frameworket. Vi ser på både Python og .NET kode for hvert eksempel.

### Case 1: Grundlæggende Sekventielt Workflow

Dette er det simpleste mønster, hvor én agents output sendes direkte til en anden. Vores scenarie involverer en hotel-`FrontDesk` agent, der kommer med en rejseanbefaling, som derefter bliver gennemgået af en `Concierge` agent.

*Diagram af det grundlæggende FrontDesk -\> Concierge workflow.*

#### Scenarie Baggrund

En rejsende beder om en anbefaling i Paris.

1.  `FrontDesk` agenten, designet til kortfattethed, foreslår at besøge Louvre-museet.
2.  `Concierge` agenten, som prioriterer autentiske oplevelser, modtager denne anbefaling. Den gennemgår forslaget og giver feedback, og foreslår et mere lokalt, mindre turistet alternativ.

#### Python Implementeringsanalyse

I Python-eksemplet definerer og opretter vi først de to agenter, hver med specifikke instruktioner.

```python
# 01.python-agent-framework-workflow-ghmodel-basic.ipynb

# Definer agentroller og instruktioner
REVIEWER_NAME = "Concierge"
REVIEWER_INSTRUCTIONS = """
    You are an are hotel concierge who has opinions about providing the most local and authentic experiences for travelers...
    """

FRONTDESK_NAME = "FrontDesk"
FRONTDESK_INSTRUCTIONS = """
    You are a Front Desk Travel Agent with ten years of experience and are known for brevity...
    """

# Opret agentinstanser
reviewer_agent = chat_client.as_agent(
    instructions=(REVIEWER_INSTRUCTIONS),
    name=REVIEWER_NAME,
)

front_desk_agent = chat_client.as_agent(
    instructions=(FRONTDESK_INSTRUCTIONS),
    name=FRONTDESK_NAME,
)
```

Derefter bruges `WorkflowBuilder` til at opbygge grafen. `front_desk_agent` sættes som startpunkt, og der oprettes en edge, som forbinder dets output til `reviewer_agent`.

```python
# 01.python-agent-framework-workflow-ghmodel-basic.ipynb

workflow = WorkflowBuilder(start_executor=front_desk_agent).add_edge(front_desk_agent, reviewer_agent).build()
```

Til sidst udføres workflowet med den indledende brugerprompt.

```python
# 01.python-agent-framework-workflow-ghmodel-basic.ipynb

result =''
# run udfører arbejdsprocessen; get_outputs() returnerer outputudførerens resultat.
events = await workflow.run('I would like to go to Paris.')
outputs = events.get_outputs()
result = outputs[0].text if outputs else ''
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

Agenterne oprettes med en `AzureOpenAIClient` (Responses API), og derefter definerer `WorkflowBuilder` det sekventielle flow ved at tilføje en edge fra `frontDeskAgent` til `reviewerAgent`.

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

Workflowet køres derefter med brugerens besked, og resultaterne streames tilbage.

### Case 2: Multi-Trins Sekventielt Workflow

Dette mønster udvider den grundlæggende sekvens til at inkludere flere agenter. Det er ideelt til processer, der kræver flere faser af forfining eller transformation.

#### Scenarie Baggrund

En bruger leverer et billede af en stue og beder om et møbeltilbud.

1.  **Salg-Agent**: Identificerer møbelelementerne på billedet og laver en liste.
2.  **Pris-Agent**: Tager listen af elementer og giver en detaljeret prisopdeling, inklusiv budget-, mellem- og premium-muligheder.
3.  **Tilbuds-Agent**: Modtager den prissatte liste og formaterer den til et formelt tilbudsdokument i Markdown.

*Diagram af Salg -\> Pris -\> Tilbud workflow.*

#### Python Implementeringsanalyse

Tre agenter defineres, hver med en specialiseret rolle. Workflowet bygges ved hjælp af `add_edge` til at skabe en kæde: `sales_agent` -\> `price_agent` -\> `quote_agent`.

```python
# 02.python-agent-framework-workflow-ghmodel-sequential.ipynb

# Opret tre specialiserede agenter
sales_agent = chat_client.as_agent(...)
price_agent = chat_client.as_agent(...)
quote_agent = chat_client.as_agent(...)

# Byg det sekventielle workflow
workflow = WorkflowBuilder(start_executor=sales_agent).add_edge(sales_agent, price_agent).add_edge(price_agent, quote_agent).build()
```

Input er en `ChatMessage`, der inkluderer både tekst og billedets URI. Frameworket håndterer at sende output fra hver agent til den næste i rækkefølgen, indtil det endelige tilbud genereres.

```python
# 02.python-agent-framework-workflow-ghmodel-sequential.ipynb

# Brugerbeskeden indeholder både tekst og et billede
message = ChatMessage(
        role=Role.USER,
        contents=[
            TextContent(text="Please find the relevant furniture..."),
            DataContent(uri=image_uri, media_type="image/png")
        ]
)

# Kør arbejdsgangen
events = await workflow.run(message)
```

#### .NET (C\#) Implementeringsanalyse

.NET-eksemplet spejler Python-versionen. Tre agenter (`salesagent`, `priceagent`, `quoteagent`) oprettes. `WorkflowBuilder` forbinder dem sekventielt.

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

Brugerens besked konstrueres med både billeddata (som bytes) og tekstprompten. Metoden `InProcessExecution.StreamAsync` starter workflowet, og det endelige output opfanges fra streamen.

### Case 3: Samtidigt Workflow

Dette mønster bruges, når opgaver kan udføres samtidig for at spare tid. Det involverer en "fan-out" til flere agenter og en "fan-in" til at samle resultaterne.

#### Scenarie Baggrund

En bruger beder om at planlægge en rejse til Seattle.

1.  **Dispatcher (Fan-Out)**: Brugerens anmodning sendes til to agenter samtidig.
2.  **Researcher-Agent**: Undersøger seværdigheder, vejr og nøglehensyn for en rejse til Seattle i december.
3.  **Plan-Agent**: Uafhængigt laver en detaljeret dags-for-dags rejseplan.
4.  **Aggregator (Fan-In)**: Outputtet fra både researcher og planner samles og præsenteres samlet som det endelige resultat.

*Diagram af det samtidige Researcher og Planner workflow.*

#### Python Implementeringsanalyse

`ConcurrentBuilder` forenkler oprettelsen af dette mønster. Du skal blot liste de deltagende agenter, og builderen opretter automatisk den nødvendige fan-out og fan-in logik.

```python
# 03.python-agent-framework-workflow-ghmodel-concurrent.ipynb

research_agent = chat_client.as_agent(name="Researcher-Agent", ...)
plan_agent = chat_client.as_agent(name="Plan-Agent", ...)

# ConcurrentBuilder håndterer fan-out/fan-in logikken
workflow = ConcurrentBuilder().participants([research_agent, plan_agent]).build()

# Kør arbejdsflowet
events = await workflow.run("Plan a trip to Seattle in December")
```

Frameworket sikrer, at `research_agent` og `plan_agent` udføres parallelt, og deres endelige outputs samles i en liste.

#### .NET (C\#) Implementeringsanalyse

I .NET kræver dette mønster en mere eksplicit definition. Tilpassede executorere (`ConcurrentStartExecutor` og `ConcurrentAggregationExecutor`) oprettes for at håndtere fan-out og fan-in logikken.

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

`WorkflowBuilder` bruger derefter `AddFanOutEdge` og `AddFanInEdge` til at bygge grafen med disse tilpassede executorere og agenter.

```csharp
// 03.dotnet-agent-framework-workflow-ghmodel-concurrent.ipynb

var workflow = new WorkflowBuilder(startExecutor)
            .AddFanOutEdge(startExecutor, targets: [researcherAgent, plannerAgent])
            .AddFanInEdge(aggregationExecutor, sources: [researcherAgent, plannerAgent])
            .WithOutputFrom(aggregationExecutor)
            .Build();
```

### Case 4: Betinget Workflow

Betingede workflows indfører forgrenet logik, som tillader systemet at følge forskellige spor baseret på mellemliggende resultater.

#### Scenarie Baggrund

Dette workflow automatiserer oprettelse og udgivelse af en teknisk vejledning.

1.  **Evangelist-Agent**: Skriver et udkast til vejledningen baseret på en given disposition og URLs.
2.  **ContentReviewer-Agent**: Gennemgår udkastet. Den tjekker, om ordtællingen overstiger 200 ord.
3.  **Betinget Gren**:
      * **Hvis Godkendt (`Ja`)**: Workflowet fortsætter til `Publisher-Agent`.
      * **Hvis Afvist (`Nej`)**: Workflowet stopper og outputter årsagen til afvisningen.
4.  **Publisher-Agent**: Hvis udkastet er godkendt, gemmer denne agent indholdet i en Markdown-fil.

#### Python Implementeringsanalyse

Dette eksempel bruger en brugerdefineret funktion, `select_targets`, til at implementere den betingede logik. Funktionen sendes til `add_multi_selection_edge_group` og styrer workflowet baseret på `review_result`-feltet fra anmelderens output.

```python
# 04.python-agent-framework-workflow-aifoundry-condition.ipynb

# Denne funktion bestemmer næste trin baseret på anmeldelsesresultatet
def select_targets(review: ReviewResult, target_ids: list[str]) -> list[str]:
    handle_review_id, save_draft_id = target_ids
    if review.review_result == "Yes":
        # Hvis godkendt, fortsæt til 'save_draft' eksekutoren
        return [save_draft_id]
    else:
        # Hvis afvist, fortsæt til 'handle_review' eksekutoren for at rapportere fejl
        return [handle_review_id]

# Workflow-builderen bruger valgfunktionen til routing
workflow = (
    WorkflowBuilder()
        .set_start_executor(evangelist_agent)
        .add_edge(evangelist_agent, reviewer_agent)
        .add_edge(reviewer_agent, to_reviewer_result)
        # Multi-valg kanten implementerer den betingede logik
        .add_multi_selection_edge_group(
            to_reviewer_result,
            [handle_review, save_draft],
            selection_func=select_targets,
        )
        .add_edge(save_draft, publisher_agent)
        .build()
)
```

Tilpassede executorere som `to_reviewer_result` bruges til at parse JSON-outputtet fra agenterne og konvertere det til stærkt typede objekter, som valgfunktionen kan inspicere.

#### .NET (C\#) Implementeringsanalyse

.NET-versionen bruger en lignende tilgang med en betingelsesfunktion. En `Func<object?, bool>` defineres for at tjekke `Result`-egenskaben hos `ReviewResult` objektet.

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

`AddEdge`-metodens `condition`-parameter tillader `WorkflowBuilder` at skabe en forgrenet sti. Workflowet følger kun edge til `publishExecutor`, hvis betingelsen `GetCondition(expectedResult: "Yes")` returnerer sandt. Ellers følger den stien til `sendReviewerExecutor`.

## Konklusion

Microsoft Agent Framework Workflow giver et robust og fleksibelt fundament for orkestrering af komplekse, multi-agent systemer. Ved at udnytte den grafbaserede arkitektur og kernekomponenter kan udviklere designe og implementere sofistikerede workflows i både Python og .NET. Uanset om din applikation kræver simpel sekventiel behandling, parallel udførelse eller dynamisk betinget logik, tilbyder frameworket værktøjerne til at bygge kraftfulde, skalerbare og typesikre AI-drevne løsninger.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfraskrivelse**:
Dette dokument er blevet oversat ved hjælp af AI-oversættelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selvom vi bestræber os på nøjagtighed, skal du være opmærksom på, at automatiserede oversættelser kan indeholde fejl eller unøjagtigheder. Det originale dokument på dets oprindelige sprog bør betragtes som den autoritative kilde. For kritisk information anbefales professionel menneskelig oversættelse. Vi påtager os intet ansvar for misforståelser eller fejltolkninger, der opstår som følge af brugen af denne oversættelse.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->