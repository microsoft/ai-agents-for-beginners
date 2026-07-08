# Bygga multi-agent-applikationer med Microsoft Agent Framework Workflow

Denna handledning kommer att guida dig genom att förstå och bygga multi-agent-applikationer med Microsoft Agent Framework. Vi kommer att utforska kärnbegreppen för multi-agent-system, dyka in i arkitekturen för ramverkets Workflow-komponent och gå igenom praktiska exempel i både Python och .NET för olika arbetsflödesmönster.

## 1\. Förstå multi-agent-system

En AI-agent är ett system som går bortom kapaciteterna för en standard Large Language Model (LLM). Den kan uppfatta sin omgivning, fatta beslut och vidta åtgärder för att uppnå specifika mål. Ett multi-agent-system involverar flera av dessa agenter som samarbetar för att lösa ett problem som skulle vara svårt eller omöjligt för en enda agent att hantera ensam.

### Vanliga användningsscenarier

  * **Komplicerad problemlösning**: Att bryta ned en stor uppgift (t.ex. planera ett evenemang för hela företaget) i mindre deluppgifter som hanteras av specialiserade agenter (t.ex. en budgetagent, en logistikagent, en marknadsföringsagent).
  * **Virtuella assistenter**: En primär assistentagent som delegerar uppgifter som schemaläggning, forskning och bokning till andra specialiserade agenter.
  * **Automatiserad innehållsskapande**: Ett arbetsflöde där en agent skriver ett utkast, en annan granskar det för noggrannhet och ton, och en tredje publicerar det.

### Multi-agent-mönster

Multi-agent-system kan organiseras i flera mönster som bestämmer hur de interagerar:

  * **Sekventiell**: Agenter arbetar i förutbestämd ordning, som en löpande band. Utgången från en agent blir ingången för nästa.
  * **Samtidig**: Agenter arbetar parallellt med olika delar av en uppgift, och deras resultat summeras i slutet.
  * **Villkorlig**: Arbetsflödet följer olika vägar baserat på en agents utdata, likt en if-then-else-sats.

## 2\. Microsoft Agent Framework Workflow Arkitektur

Agent Frameworks arbetsflödessystem är en avancerad orkestreringsmotor som är designad för att hantera komplexa interaktioner mellan flera agenter. Den är byggd på en grafbaserad arkitektur som använder en [Pregel-stil exekveringsmodell](https://kowshik.github.io/JPregel/pregel_paper.pdf), där bearbetning sker i synkroniserade steg kallade "supersteps".

### Kärnkomponenter

Arkitekturen består av tre huvudsakliga delar:

1.  **Executors**: Dessa är de grundläggande bearbetningsenheterna. I våra exempel är en `Agent` en typ av executor. Varje executor kan ha flera meddelandehanterare som automatiskt anropas baserat på typen av meddelande som mottas.
2.  **Edges**: Dessa definierar vägen som meddelanden tar mellan executorer. Edges kan ha villkor som tillåter dynamisk styrning av information genom arbetsflödesgrafen.
3.  **Workflow**: Denna komponent orkestrerar hela processen, hanterar executorer, edges och det övergripande flödet av exekvering. Den säkerställer att meddelanden behandlas i korrekt ordning och strömmar händelser för observabilitet.

*En diagram som illustrerar kärnkomponenterna i arbetsflödessystemet.*

Denna struktur möjliggör att bygga robusta och skalbara applikationer med grundläggande mönster som sekventiella kedjor, fan-out/fan-in för parallell bearbetning och switch-case-logik för villkorliga flöden.

## 3\. Praktiska exempel och kodanalys

Nu ska vi utforska hur man implementerar olika arbetsflödesmönster med ramverket. Vi tittar på både Python- och .NET-kod för varje exempel.

### Fall 1: Grundläggande sekventiellt arbetsflöde

Det här är det enklaste mönstret där en agents utdata skickas direkt till en annan. Vårt scenario involverar en hotellagent `FrontDesk` som ger en rese-rekommendation, vilken sedan granskas av en `Concierge`-agent.

*Diagram över det grundläggande FrontDesk -> Concierge arbetsflödet.*

#### Scenariobakgrund

En resenär frågar om en rekommendation i Paris.

1.  `FrontDesk`-agenten, designad för korthet, föreslår att besöka Louvren.
2.  `Concierge`-agenten, som prioriterar äkta upplevelser, får detta förslag, granskar rekommendationen och ger feedback med ett förslag på ett mer lokalt, mindre turistigt alternativ.

#### Python-implementationsanalys

I Python-exemplet definierar och skapar vi först de två agenterna, var och en med specifika instruktioner.

```python
# 01.python-agent-framework-workflow-ghmodel-basic.ipynb

# Definiera agentroller och instruktioner
REVIEWER_NAME = "Concierge"
REVIEWER_INSTRUCTIONS = """
    You are an are hotel concierge who has opinions about providing the most local and authentic experiences for travelers...
    """

FRONTDESK_NAME = "FrontDesk"
FRONTDESK_INSTRUCTIONS = """
    You are a Front Desk Travel Agent with ten years of experience and are known for brevity...
    """

# Skapa agentinstanser
reviewer_agent = chat_client.as_agent(
    instructions=(REVIEWER_INSTRUCTIONS),
    name=REVIEWER_NAME,
)

front_desk_agent = chat_client.as_agent(
    instructions=(FRONTDESK_INSTRUCTIONS),
    name=FRONTDESK_NAME,
)
```

Därefter används `WorkflowBuilder` för att konstruera grafen. `front_desk_agent` sätts som startpunkt och en edge skapas för att koppla dess utdata till `reviewer_agent`.

```python
# 01.python-agent-framework-arbetsflöde-ghmodel-basic.ipynb

workflow = WorkflowBuilder(start_executor=front_desk_agent).add_edge(front_desk_agent, reviewer_agent).build()
```

Slutligen körs arbetsflödet med den initiala användarprompten.

```python
# 01.python-agent-framework-workflow-ghmodel-basic.ipynb

result =''
# run kör arbetsflödet; get_outputs() returnerar resultatet från utdatautföraren.
events = await workflow.run('I would like to go to Paris.')
outputs = events.get_outputs()
result = outputs[0].text if outputs else ''
```

#### .NET (C\#) implementationsanalys

.NET-implementeringen följer en mycket liknande logik. Först definieras konstanter för agenternas namn och instruktioner.

```csharp
// 01.dotnet-agent-framework-workflow-ghmodel-basic.ipynb

const string ReviewerAgentName = "Concierge";
const string ReviewerAgentInstructions = @"
    You are an are hotel concierge who has opinions about providing the most local and authentic experiences for travelers...";

const string FrontDeskAgentName = "FrontDesk";
const string FrontDeskAgentInstructions = @"""
    You are a Front Desk Travel Agent with ten years of experience and are known for brevity...";
```

Agenterna skapas med en `AzureOpenAIClient` (Responses API), och sedan definierar `WorkflowBuilder` det sekventiella flödet genom att lägga till en edge från `frontDeskAgent` till `reviewerAgent`.

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

Arbetsflödet körs sedan med användarens meddelande och resultaten strömmas tillbaka.

### Fall 2: Flerskikts sekventiellt arbetsflöde

Detta mönster utvidgar den grundläggande sekvensen för att inkludera fler agenter. Det är idealiskt för processer som kräver flera steg av förfining eller transformation.

#### Scenariobakgrund

En användare tillhandahåller en bild av ett vardagsrum och begär en offert på möbler.

1.  **Sales-Agent**: Identifierar möblerna i bilden och skapar en lista.
2.  **Price-Agent**: Tar listan och ger en detaljerad prisuppdelning, med budget-, medel- och premiumalternativ.
3.  **Quote-Agent**: Tar emot den prissatta listan och formaterar den till ett formellt offertdokument i Markdown.

*Diagram över Sales -> Price -> Quote arbetsflödet.*

#### Python-implementationsanalys

Tre agenter definieras, var och en med en specialiserad roll. Arbetsflödet byggs med `add_edge` för att skapa en kedja: `sales_agent` -> `price_agent` -> `quote_agent`.

```python
# 02.python-agent-framework-workflow-ghmodel-sequential.ipynb

# Skapa tre specialiserade agenter
sales_agent = chat_client.as_agent(...)
price_agent = chat_client.as_agent(...)
quote_agent = chat_client.as_agent(...)

# Bygg det sekventiella arbetsflödet
workflow = WorkflowBuilder(start_executor=sales_agent).add_edge(sales_agent, price_agent).add_edge(price_agent, quote_agent).build()
```

Indatan är ett `ChatMessage` som inkluderar både text och bild-URI. Ramverket hanterar att föra vidare varje agents utdata till nästa i sekvensen tills slutofferten genereras.

```python
# 02.python-agent-framework-workflow-ghmodel-sequential.ipynb

# Användarmeddelandet innehåller både text och en bild
message = ChatMessage(
        role=Role.USER,
        contents=[
            TextContent(text="Please find the relevant furniture..."),
            DataContent(uri=image_uri, media_type="image/png")
        ]
)

# Kör arbetsflödet
events = await workflow.run(message)
```

#### .NET (C\#) implementationsanalys

.NET-exemplet speglar Pythonversionen. Tre agenter (`salesagent`, `priceagent`, `quoteagent`) skapas. `WorkflowBuilder` länkar dem sekventiellt.

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

Användarens meddelande konstrueras med både bilddata (som bytes) och textprompten. Metoden `InProcessExecution.StreamAsync` initierar arbetsflödet och den slutliga utdata fångas från strömmen.

### Fall 3: Samtidigt arbetsflöde

Detta mönster används när uppgifter kan utföras samtidigt för att spara tid. Det involverar en "fan-out" till flera agenter och en "fan-in" för att sammanställa resultaten.

#### Scenariobakgrund

En användare ber om att planera en resa till Seattle.

1.  **Dispatcher (Fan-Out)**: Användarens förfrågan skickas till två agenter samtidigt.
2.  **Researcher-Agent**: Forskar om sevärdheter, väder och viktiga aspekter för en resa till Seattle i december.
3.  **Plan-Agent**: Skapar självständigt en detaljerad dag-för-dag reseplan.
4.  **Aggregator (Fan-In)**: Resultaten från både forskaren och planläggaren samlas in och presenteras tillsammans som slutresultat.

*Diagram över det samtidiga Researcher och Planner arbetsflödet.*

#### Python-implementationsanalys

`ConcurrentBuilder` förenklar skapandet av detta mönster. Du listar bara deltagande agenter, och buildern skapar automatiskt den nödvändiga fan-out och fan-in-logiken.

```python
# 03.python-agent-framework-workflow-ghmodel-concurrent.ipynb

research_agent = chat_client.as_agent(name="Researcher-Agent", ...)
plan_agent = chat_client.as_agent(name="Plan-Agent", ...)

# ConcurrentBuilder hanterar fan-out/fan-in-logiken
workflow = ConcurrentBuilder().participants([research_agent, plan_agent]).build()

# Kör arbetsflödet
events = await workflow.run("Plan a trip to Seattle in December")
```

Ramverket säkerställer att `research_agent` och `plan_agent` kör parallellt och deras slutresultat samlas i en lista.

#### .NET (C\#) implementationsanalys

I .NET kräver detta mönster en mer explicit definition. Anpassade executorer (`ConcurrentStartExecutor` och `ConcurrentAggregationExecutor`) skapas för att hantera fan-out och fan-in-logiken.

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

`WorkflowBuilder` använder sedan `AddFanOutEdge` och `AddFanInEdge` för att konstruera grafen med dessa anpassade executorer och agenter.

```csharp
// 03.dotnet-agent-framework-workflow-ghmodel-concurrent.ipynb

var workflow = new WorkflowBuilder(startExecutor)
            .AddFanOutEdge(startExecutor, targets: [researcherAgent, plannerAgent])
            .AddFanInEdge(aggregationExecutor, sources: [researcherAgent, plannerAgent])
            .WithOutputFrom(aggregationExecutor)
            .Build();
```

### Fall 4: Villkorligt arbetsflöde

Villkorliga arbetsflöden introducerar förgreningslogik, vilket tillåter systemet att ta olika vägar baserat på mellanresultat.

#### Scenariobakgrund

Detta arbetsflöde automatiserar skapandet och publiceringen av en teknisk handledning.

1.  **Evangelist-Agent**: Skriver ett utkast till handledningen baserat på en given disposition och URL:er.
2.  **ContentReviewer-Agent**: Granskar utkastet. Kontrollerar om ordantalet överstiger 200 ord.
3.  **Villkorlig gren**:
      * **Om godkänd (`Yes`)**: Arbetsflödet fortsätter till `Publisher-Agent`.
      * **Om avvisad (`No`)**: Arbetsflödet stoppas och skälet för avvisning returneras.
4.  **Publisher-Agent**: Om utkastet är godkänt sparas innehållet till en Markdown-fil.

#### Python-implementationsanalys

Detta exempel använder en anpassad funktion, `select_targets`, för att implementera den villkorliga logiken. Denna funktion skickas till `add_multi_selection_edge_group` och styr arbetsflödet baserat på fältet `review_result` från granskarens utdata.

```python
# 04.python-agent-framework-workflow-aifoundry-condition.ipynb

# Denna funktion bestämmer nästa steg baserat på granskningsresultatet
def select_targets(review: ReviewResult, target_ids: list[str]) -> list[str]:
    handle_review_id, save_draft_id = target_ids
    if review.review_result == "Yes":
        # Om godkänt, fortsätt till 'save_draft' exekutorn
        return [save_draft_id]
    else:
        # Om avvisat, fortsätt till 'handle_review' exekutorn för att rapportera fel
        return [handle_review_id]

# Arbetsflödesbyggaren använder urvalsfunktionen för dirigering
workflow = (
    WorkflowBuilder()
        .set_start_executor(evangelist_agent)
        .add_edge(evangelist_agent, reviewer_agent)
        .add_edge(reviewer_agent, to_reviewer_result)
        # Multi-val kanten implementerar den villkorliga logiken
        .add_multi_selection_edge_group(
            to_reviewer_result,
            [handle_review, save_draft],
            selection_func=select_targets,
        )
        .add_edge(save_draft, publisher_agent)
        .build()
)
```

Anpassade executorer som `to_reviewer_result` används för att parsa JSON-utdata från agenterna och konvertera den till starkt typade objekt som urvals-funktionen kan inspektera.

#### .NET (C\#) implementationsanalys

.NET-versionen använder en liknande metod med en villkorsfunktion. En `Func<object?, bool>` definieras för att kontrollera egenskapen `Result` i objektet `ReviewResult`.

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

`AddEdge`-metodens parameter `condition` gör att `WorkflowBuilder` kan skapa en förgreningsväg. Arbetsflödet följer bara edge till `publishExecutor` om villkoret `GetCondition(expectedResult: "Yes")` returnerar sant. Annars följer det vägen till `sendReviewerExecutor`.

## Slutsats

Microsoft Agent Framework Workflow erbjuder en robust och flexibel grund för att orkestrera komplexa multi-agent-system. Genom att utnyttja dess grafbaserade arkitektur och kärnkomponenter kan utvecklare designa och implementera avancerade arbetsflöden i både Python och .NET. Oavsett om din applikation kräver enkel sekventiell bearbetning, parallell exekvering eller dynamisk villkorslogik erbjuder ramverket verktygen för att bygga kraftfulla, skalbara och typ-säkra AI-drivna lösningar.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfriskrivning**:
Detta dokument har översatts med hjälp av AI-översättningstjänsten [Co-op Translator](https://github.com/Azure/co-op-translator). Även om vi strävar efter noggrannhet, var vänlig notera att automatiska översättningar kan innehålla fel eller brister. Det ursprungliga dokumentet på dess modersmål bör betraktas som den auktoritativa källan. För kritisk information rekommenderas professionell mänsklig översättning. Vi ansvarar inte för några missförstånd eller feltolkningar som uppstår till följd av användningen av denna översättning.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->