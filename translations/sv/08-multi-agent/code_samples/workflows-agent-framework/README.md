# Bygga Multi-Agent Applikationer med Microsoft Agent Framework Workflow

Den här handledningen hjälper dig att förstå och bygga multi-agent applikationer med Microsoft Agent Framework. Vi kommer att utforska kärnkoncepten för multi-agent system, dyka in i arkitekturen för ramverkets Workflow-komponent och gå igenom praktiska exempel i både Python och .NET för olika arbetsflödesmönster.

## 1\. Förstå Multi-Agent System

En AI-agent är ett system som går bortom kapabiliteterna hos en standard Large Language Model (LLM). Den kan uppfatta sin omgivning, fatta beslut och vidta åtgärder för att uppnå specifika mål. Ett multi-agent system involverar flera sådana agenter som samarbetar för att lösa ett problem som skulle vara svårt eller omöjligt för en enskild agent att hantera ensam.

### Vanliga Applikationsscenarier

  * **Komplex Problemlösning**: Dela upp en stor uppgift (t.ex. planera ett företagsevent) i mindre deluppgifter som hanteras av specialiserade agenter (t.ex. en budgetagent, en logistikagent, en marknadsföringsagent).
  * **Virtuella Assistenter**: En primär assistentagent delegerar uppgifter som schemaläggning, forskning och bokning till andra specialiserade agenter.
  * **Automatiserad Innehållsskapande**: Ett arbetsflöde där en agent skriver utkast, en annan granskar det för noggrannhet och ton, och en tredje publicerar det.

### Multi-Agent Mönster

Multi-agent system kan organiseras i flera mönster som bestämmer hur de interagerar:

  * **Sekventiellt**: Agenter arbetar i en förutbestämd ordning, som på en produktionslinje. Utdata från en agent blir indata för nästa.
  * **Samtidigt**: Agenter arbetar parallellt med olika delar av en uppgift, och deras resultat samlas ihop i slutet.
  * **Villkorligt**: Arbetsflödet följer olika vägar baserat på en agents utdata, liknande en if-then-else-sats.

## 2\. Microsoft Agent Framework Workflow Arkitektur

Agent Frameworks arbetsflödessystem är en avancerad orkestreringsmotor designad för att hantera komplexa interaktioner mellan flera agenter. Det är byggt på en grafbaserad arkitektur som använder en [Pregel-stil exekveringsmodell](https://kowshik.github.io/JPregel/pregel_paper.pdf), där bearbetning sker i synkroniserade steg kallade "supersteps."

### Kärnkomponenter

Arkitekturen består av tre huvuddelar:

1.  **Executors**: Dessa är de grundläggande bearbetningsenheterna. I våra exempel är en `Agent` en typ av executor. Varje executor kan ha flera meddelandehanterare som automatiskt anropas baserat på typen av mottaget meddelande.
2.  **Edges**: Dessa definierar vägen som meddelanden tar mellan executors. Edges kan ha villkor, vilket möjliggör dynamisk routing av information genom arbetsflödesgrafen.
3.  **Workflow**: Denna komponent orkestrerar hela processen, hanterar executors, edges och det övergripande exekveringsflödet. Den säkerställer att meddelanden bearbetas i rätt ordning och strömmar händelser för observabilitet.

*En diagram som illustrerar kärnkomponenterna i arbetsflödessystemet.*

Denna struktur möjliggör att bygga robusta och skalbara applikationer med grundläggande mönster som sekventiella kedjor, fan-out/fan-in för parallell bearbetning och switch-case logik för villkorliga flöden.

## 3\. Praktiska Exempel och Kodanalys

Nu ska vi utforska hur man implementerar olika arbetsflödesmönster med ramverket. Vi kommer att titta på både Python och .NET-kod för varje exempel.

### Fall 1: Grundläggande Sekventiellt Arbetsflöde

Detta är det enklaste mönstret, där en agents utdata skickas direkt till en annan. Vårt scenario involverar en hotellagent `FrontDesk` som ger en reseförslag, vilket sedan granskas av en `Concierge`-agent.

*Diagram över det grundläggande FrontDesk -\> Concierge arbetsflödet.*

#### Scenario Bakgrund

En resenär ber om ett förslag i Paris.

1.  `FrontDesk`-agenten, designad för kortfattade svar, föreslår ett besök på Louvren.
2.  `Concierge`-agenten, som prioriterar autentiska upplevelser, tar emot detta förslag. Den granskar rekommendationen och ger feedback, föreslår ett mer lokalt, mindre turistigt alternativ.

#### Python Implementationsanalys

I Python-exemplet definierar och skapar vi först de två agenterna, var och en med specifika instruktioner.

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

Därefter används `WorkflowBuilder` för att konstruera grafen. `front_desk_agent` sätts som startpunkt, och en edge skapas för att koppla dess utdata till `reviewer_agent`.

```python
# 01.python-agent-framework-workflow-ghmodel-basic.ipynb

workflow = WorkflowBuilder().set_start_executor(front_desk_agent).add_edge(front_desk_agent, reviewer_agent).build()
```

Slutligen exekveras arbetsflödet med den initiala användarfrågan.

```python
# 01.python-agent-framework-workflow-ghmodel-basic.ipynb

result =''
# The run_stream method executes the workflow and streams events.
async for event in workflow.run_stream('I would like to go to Paris.'):
    if isinstance(event, WorkflowEvent):
        result += str(event.data)
```

#### .NET (C\#) Implementationsanalys

.NET-implementationen följer en mycket liknande logik. Först definieras konstanter för agenternas namn och instruktioner.

```csharp
// 01.dotnet-agent-framework-workflow-ghmodel-basic.ipynb

const string ReviewerAgentName = "Concierge";
const string ReviewerAgentInstructions = @"
    You are an are hotel concierge who has opinions about providing the most local and authentic experiences for travelers...";

const string FrontDeskAgentName = "FrontDesk";
const string FrontDeskAgentInstructions = @"""
    You are a Front Desk Travel Agent with ten years of experience and are known for brevity...";
```

Agenterna skapas med en `OpenAIClient`, och sedan definierar `WorkflowBuilder` det sekventiella flödet genom att lägga till en edge från `frontDeskAgent` till `reviewerAgent`.

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

Arbetsflödet körs sedan med användarens meddelande, och resultaten strömmas tillbaka.

### Fall 2: Multi-Step Sekventiellt Arbetsflöde

Detta mönster utökar den grundläggande sekvensen för att inkludera fler agenter. Det är idealiskt för processer som kräver flera steg av förfining eller transformation.

#### Scenario Bakgrund

En användare tillhandahåller en bild av ett vardagsrum och ber om en möbeloffert.

1.  **Sales-Agent**: Identifierar möbelobjekten i bilden och skapar en lista.
2.  **Price-Agent**: Tar listan över objekt och ger en detaljerad prisuppdelning, inklusive budget-, mellan- och premiumalternativ.
3.  **Quote-Agent**: Tar emot den prissatta listan och formaterar den till ett formellt offertdokument i Markdown.

*Diagram över Sales -\> Price -\> Quote arbetsflödet.*

#### Python Implementationsanalys

Tre agenter definieras, var och en med en specialiserad roll. Arbetsflödet konstrueras med `add_edge` för att skapa en kedja: `sales_agent` -\> `price_agent` -\> `quote_agent`.

```python
# 02.python-agent-framework-workflow-ghmodel-sequential.ipynb

# Create three specialized agents
sales_agent = chat_client.create_agent(...)
price_agent = chat_client.create_agent(...)
quote_agent = chat_client.create_agent(...)

# Build the sequential workflow
workflow = WorkflowBuilder().set_start_executor(sales_agent).add_edge(sales_agent, price_agent).add_edge(price_agent, quote_agent).build()
```

Indatan är ett `ChatMessage` som inkluderar både text och bildens URI. Ramverket hanterar att skicka utdatan från varje agent till nästa i sekvensen tills den slutliga offerten genereras.

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

#### .NET (C\#) Implementationsanalys

.NET-exemplet speglar Python-versionen. Tre agenter (`salesagent`, `priceagent`, `quoteagent`) skapas. `WorkflowBuilder` länkar dem sekventiellt.

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

Användarens meddelande konstrueras med både bilddata (som bytes) och textprompten. `InProcessExecution.StreamAsync`-metoden initierar arbetsflödet, och den slutliga utdatan fångas från strömmen.

### Fall 3: Samtidigt Arbetsflöde

Detta mönster används när uppgifter kan utföras samtidigt för att spara tid. Det involverar en "fan-out" till flera agenter och en "fan-in" för att samla resultaten.

#### Scenario Bakgrund

En användare ber om att planera en resa till Seattle.

1.  **Dispatcher (Fan-Out)**: Användarens begäran skickas till två agenter samtidigt.
2.  **Researcher-Agent**: Undersöker sevärdheter, väder och viktiga överväganden för en resa till Seattle i december.
3.  **Plan-Agent**: Skapar oberoende en detaljerad dag-för-dag resplan.
4.  **Aggregator (Fan-In)**: Utdatan från både forskaren och planeraren samlas och presenteras tillsammans som slutresultatet.

*Diagram över det samtidiga Researcher och Planner arbetsflödet.*

#### Python Implementationsanalys

`ConcurrentBuilder` förenklar skapandet av detta mönster. Du listar helt enkelt de deltagande agenterna, och byggaren skapar automatiskt den nödvändiga fan-out och fan-in logiken.

```python
# 03.python-agent-framework-workflow-ghmodel-concurrent.ipynb

research_agent = chat_client.create_agent(name="Researcher-Agent", ...)
plan_agent = chat_client.create_agent(name="Plan-Agent", ...)

# ConcurrentBuilder handles the fan-out/fan-in logic
workflow = ConcurrentBuilder().participants([research_agent, plan_agent]).build()

# Run the workflow
events = await workflow.run("Plan a trip to Seattle in December")
```

Ramverket säkerställer att `research_agent` och `plan_agent` exekverar parallellt, och deras slutliga utdatan samlas i en lista.

#### .NET (C\#) Implementationsanalys

I .NET kräver detta mönster en mer explicit definition. Anpassade executors (`ConcurrentStartExecutor` och `ConcurrentAggregationExecutor`) skapas för att hantera fan-out och fan-in logiken.

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

`WorkflowBuilder` använder sedan `AddFanOutEdge` och `AddFanInEdge` för att konstruera grafen med dessa anpassade executors och agenter.

```csharp
// 03.dotnet-agent-framework-workflow-ghmodel-concurrent.ipynb

var workflow = new WorkflowBuilder(startExecutor)
            .AddFanOutEdge(startExecutor, targets: [researcherAgent, plannerAgent])
            .AddFanInEdge(aggregationExecutor, sources: [researcherAgent, plannerAgent])
            .WithOutputFrom(aggregationExecutor)
            .Build();
```

### Fall 4: Villkorligt Arbetsflöde

Villkorliga arbetsflöden introducerar förgreningslogik, vilket gör att systemet kan ta olika vägar baserat på mellanresultat.

#### Scenario Bakgrund

Detta arbetsflöde automatiserar skapandet och publiceringen av en teknisk handledning.

1.  **Evangelist-Agent**: Skriver ett utkast till handledningen baserat på en given disposition och URL:er.
2.  **ContentReviewer-Agent**: Granskar utkastet. Den kontrollerar om ordantalet är över 200 ord.
3.  **Villkorlig Förgrening**:
      * **Om Godkänd (`Yes`)**: Arbetsflödet fortsätter till `Publisher-Agent`.
      * **Om Avvisad (`No`)**: Arbetsflödet stannar och ger orsaken till avvisningen.
4.  **Publisher-Agent**: Om utkastet godkänns, sparar denna agent innehållet till en Markdown-fil.

#### Python Implementationsanalys

Detta exempel använder en anpassad funktion, `select_targets`, för att implementera den villkorliga logiken. Denna funktion skickas till `add_multi_selection_edge_group` och styr arbetsflödet baserat på fältet `review_result` från granskarens utdata.

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

Anpassade executors som `to_reviewer_result` används för att analysera JSON-utdata från agenterna och konvertera det till starkt typade objekt som urvalsfunktionen kan inspektera.

#### .NET (C\#) Implementationsanalys

.NET-versionen använder en liknande metod med en villkorsfunktion. En `Func<object?, bool>` definieras för att kontrollera egenskapen `Result` i `ReviewResult`-objektet.

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

`AddEdge`-metodens `condition`-parameter gör att `WorkflowBuilder` kan skapa en förgreningsväg. Arbetsflödet följer endast kanten till `publishExecutor` om villkoret `GetCondition(expectedResult: "Yes")` returnerar true. Annars följer det vägen till `sendReviewerExecutor`.

## Slutsats

Microsoft Agent Framework Workflow erbjuder en robust och flexibel grund för att orkestrera komplexa multi-agent system. Genom att utnyttja dess grafbaserade arkitektur och kärnkomponenter kan utvecklare designa och implementera sofistikerade arbetsflöden i både Python och .NET. Oavsett om din applikation kräver enkel sekventiell bearbetning, parallell exekvering eller dynamisk villkorlig logik, erbjuder ramverket verktygen för att bygga kraftfulla, skalbara och typ-säkra AI-drivna lösningar.

---

**Ansvarsfriskrivning**:  
Detta dokument har översatts med hjälp av AI-översättningstjänsten [Co-op Translator](https://github.com/Azure/co-op-translator). Även om vi strävar efter noggrannhet, bör det noteras att automatiserade översättningar kan innehålla fel eller felaktigheter. Det ursprungliga dokumentet på dess originalspråk bör betraktas som den auktoritativa källan. För kritisk information rekommenderas professionell mänsklig översättning. Vi ansvarar inte för eventuella missförstånd eller feltolkningar som uppstår vid användning av denna översättning.