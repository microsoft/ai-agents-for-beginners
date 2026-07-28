# Bygga flermedelsprogram med Microsoft Agent Framework Workflow

Denna handledning guidar dig genom att förstå och bygga flermedelsprogram med hjälp av Microsoft Agent Framework. Vi kommer att utforska kärnbegreppen för flermedelssystem, dyka ner i arkitekturen för ramverkets Workflow-komponent och gå igenom praktiska exempel i både Python och .NET för olika arbetsflödesmönster.

## 1\. Förståelse av flermedelssystem

En AI-agent är ett system som går bortom kapabiliteterna hos en standard Stor Språkmodell (LLM). Den kan uppfatta sin miljö, fatta beslut och vidta åtgärder för att uppnå specifika mål. Ett flermedelssystem involverar flera av dessa agenter som samarbetar för att lösa ett problem som skulle vara svårt eller omöjligt för en enskild agent att hantera ensam.

### Vanliga tillämpningsscenarier

  * **Komplex problemlösning**: Att bryta ner en stor uppgift (t.ex. planera ett företagsomfattande evenemang) i mindre deluppgifter som hanteras av specialiserade agenter (t.ex. en budgetagent, en logistikagent, en marknadsföringsagent).
  * **Virtuella assistenter**: En huvudassistentagent som delegerar uppgifter som schemaläggning, forskning och bokning till andra specialiserade agenter.
  * **Automatiserad innehållsskapande**: Ett arbetsflöde där en agent skissar innehåll, en annan granskar det för korrekthet och ton, och en tredje publicerar det.

### Flermedelsmönster

Flermedelssystem kan organiseras i flera mönster, som bestämmer hur de interagerar:

  * **Sekventiell**: Agenter arbetar i en förutbestämd ordning, som en löpande band. Utdata från en agent blir indata för nästa.
  * **Parallell**: Agenter arbetar samtidigt på olika delar av en uppgift, och deras resultat sammanställs i slutet.
  * **Villkorlig**: Arbetsflödet följer olika vägar baserat på en agents utdata, liknande en if-then-else-sats.

## 2\. Microsoft Agent Framework Workflows arkitektur

Agent Frameworks arbetsflödessystem är en avancerad orkestreringsmotor designad för att hantera komplexa interaktioner mellan flera agenter. Den är byggd på en grafbaserad arkitektur som använder en [Pregel-stil exekveringsmodell](https://kowshik.github.io/JPregel/pregel_paper.pdf), där bearbetning sker i synkroniserade steg kallade "supersteg."

### Kärnkomponenter

Arkitekturen består av tre huvuddelar:

1.  **Exekutörer**: Dessa är de grundläggande bearbetningsenheterna. I våra exempel är en `Agent` en typ av exekutör. Varje exekutör kan ha flera meddelandehanterare som automatiskt anropas baserat på typen av mottaget meddelande.
2.  **Kanter**: Dessa definierar vägen som meddelanden tar mellan exekutörer. Kanter kan ha villkor som tillåter dynamisk routning av information genom arbetsflödesgrafen.
3.  **Workflow**: Denna komponent orkestrerar hela processen, hanterar exekutörerna, kanterna och det övergripande utförandeflödet. Den säkerställer att meddelanden bearbetas i rätt ordning och strömmar händelser för observerbarhet.

*Ett diagram som illustrerar kärnkomponenterna i arbetsflödessystemet.*

Denna struktur möjliggör att bygga robusta och skalbara program med grundläggande mönster som sekventiella kedjor, fan-out/fan-in för parallell bearbetning och switch-case-logik för villkorliga flöden.

## 3\. Praktiska exempel och kodanalys

Nu ska vi utforska hur man implementerar olika arbetsflödesmönster med ramverket. Vi tittar både på Python- och .NET-kod för varje exempel.

### Fall 1: Grundläggande sekventiellt arbetsflöde

Detta är det enklaste mönstret, där en agents utdata direkt skickas vidare till en annan. Vårt scenario involverar en hotellagent `FrontDesk` som ger en resetipsrekommendation, vilket sedan granskas av en `Concierge`-agent.

*Diagram över det grundläggande FrontDesk -\> Concierge-arbetsflödet.*

#### Scenario bakgrund

En resenär ber om en rekommendation i Paris.

1.  `FrontDesk`-agenten, designad för kortfattning, föreslår ett besök på Louvren.
2.  `Concierge`-agenten, som prioriterar autentiska upplevelser, mottar förslaget. Den granskar rekommendationen och ger feedback, föreslår ett mer lokalt, mindre turistigt alternativ.

#### Python-implementeringsanalys

I Python-exemplet definierar och skapar vi först de två agenterna, varje med specifika instruktioner.

```python
# 01.python-agent-framework-workflow-ghmodel-basic.ipynb

# Definiera agentroller och instruktioner
REVIEWER_NAME = "Concierge"
REVIEWER_INSTRUCTIONS = """
    You are a hotel concierge who has opinions about providing the most local and authentic experiences for travelers...
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

Därefter används `WorkflowBuilder` för att konstruera grafen. `front_desk_agent` sätts som startpunkt och en kant skapas för att koppla dess utdata till `reviewer_agent`.

```python
# 01.python-agent-framework-arbetsflöde-ghmodel-basic.ipynb

workflow = WorkflowBuilder(start_executor=front_desk_agent).add_edge(front_desk_agent, reviewer_agent).build()
```

Slutligen körs arbetsflödet med den initiala användarfrågan.

```python
# 01.python-agent-framework-workflow-ghmodel-basic.ipynb

result =''
# run kör arbetsflödet; get_outputs() returnerar resultatet från output-exekutorn.
events = await workflow.run('I would like to go to Paris.')
outputs = events.get_outputs()
result = outputs[0].text if outputs else ''
```

#### .NET (C\#) implementeringsanalys

.NET-implementeringen följer en mycket liknande logik. Först definieras konstanter för agenternas namn och instruktioner.

```csharp
// 01.dotnet-agent-framework-workflow-ghmodel-basic.ipynb

const string ReviewerAgentName = "Concierge";
const string ReviewerAgentInstructions = @"
    You are a hotel concierge who has opinions about providing the most local and authentic experiences for travelers...";

const string FrontDeskAgentName = "FrontDesk";
const string FrontDeskAgentInstructions = @"""
    You are a Front Desk Travel Agent with ten years of experience and are known for brevity...";
```

Agenterna skapas med en `AzureOpenAIClient` (Responses API), och sedan definierar `WorkflowBuilder` det sekventiella flödet genom att lägga till en kant från `frontDeskAgent` till `reviewerAgent`.

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

Arbetsflödet körs sedan med användarens meddelande och resultaten strömmas tillbaka.

### Fall 2: Flerstegs sekventiellt arbetsflöde

Detta mönster förlänger den grundläggande sekvensen för att inkludera fler agenter. Det är idealiskt för processer som kräver flera steg av förfining eller omvandling.

#### Scenario bakgrund

En användare tillhandahåller en bild av ett vardagsrum och ber om en offert på möbler.

1.  **Försäljningsagent**: Identifierar möbelobjekten i bilden och skapar en lista.
2.  **Prisagent**: Tar listan med objekt och ger en detaljerad prisuppdelning, inklusive budget-, mellan- och premiumalternativ.
3.  **Offertagent**: Tar emot den prissatta listan och formaterar den till ett formellt offertdokument i Markdown.

*Diagram över Sales -\> Price -\> Quote-arbetsflödet.*

#### Python-implementeringsanalys

Tre agenter definieras, var och en med en specialiserad roll. Arbetsflödet konstrueras med `add_edge` för att skapa en kedja: `sales_agent` -\> `price_agent` -\> `quote_agent`.

```python
# 02.python-agent-framework-workflow-ghmodel-sequential.ipynb

# Skapa tre specialiserade agenter
sales_agent = chat_client.as_agent(...)
price_agent = chat_client.as_agent(...)
quote_agent = chat_client.as_agent(...)

# Bygg den sekventiella arbetsflödet
workflow = WorkflowBuilder(start_executor=sales_agent).add_edge(sales_agent, price_agent).add_edge(price_agent, quote_agent).build()
```

Indatan är ett `ChatMessage` som inkluderar både text och bild-URI. Ramverket hanterar att skicka varje agents utdata till nästa i sekvensen tills slutofferten genereras.

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

#### .NET (C\#) implementeringsanalys

.NET-exemplet speglar Python-versionen. Tre agenter (`salesagent`, `priceagent`, `quoteagent`) skapas. `WorkflowBuilder` länkar dem sekventiellt.

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

Användarens meddelande konstrueras med både bilddata (som bytes) och textprompt. Metoden `InProcessExecution.RunStreamingAsync` initierar arbetsflödet, och slutresultatet fångas från strömmen.

### Fall 3: Parallellt arbetsflöde

Detta mönster används när uppgifter kan utföras samtidigt för att spara tid. Det involverar en "fan-out" till flera agenter och en "fan-in" för att sammanställa resultaten.

#### Scenario bakgrund

En användare ber om hjälp att planera en resa till Seattle.

1.  **Dispatch (Fan-Out)**: Användarens begäran skickas samtidigt till två agenter.
2.  **Researcher-Agent**: Undersöker sevärdheter, väder och viktiga överväganden för en resa till Seattle i december.
3.  **Plan-Agent**: Skapar oberoende en detaljerad dag-för-dag-resplan.
4.  **Aggregator (Fan-In)**: Resultaten från både forskaren och planeraren samlas in och presenteras ihop som slutresultat.

*Diagram över det parallella Researcher och Planner-arbetsflödet.*

#### Python-implementeringsanalys

`ConcurrentBuilder` förenklar skapandet av detta mönster. Du listar helt enkelt de deltagande agenterna, och buildern skapar automatiskt nödvändig fan-out och fan-in-logik.

```python
# 03.python-agent-framework-workflow-ghmodel-concurrent.ipynb

research_agent = chat_client.as_agent(name="Researcher-Agent", ...)
plan_agent = chat_client.as_agent(name="Plan-Agent", ...)

# ConcurrentBuilder hanterar fan-out/fan-in-logiken
workflow = ConcurrentBuilder().participants([research_agent, plan_agent]).build()

# Kör arbetsflödet
events = await workflow.run("Plan a trip to Seattle in December")
```

Ramverket säkerställer att `research_agent` och `plan_agent` körs parallellt, och deras slutliga utdata samlas i en lista.

#### .NET (C\#) implementeringsanalys

I .NET kräver detta mönster en mer explicit definition. Anpassade exekutörer (`ConcurrentStartExecutor` och `ConcurrentAggregationExecutor`) skapas för att hantera fan-out och fan-in-logiken.

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

`WorkflowBuilder` använder därefter `AddFanOutEdge` och `AddFanInEdge` för att konstruera grafen med dessa anpassade exekutörer och agenter.

```csharp
// 03.dotnet-agent-framework-workflow-ghmodel-concurrent.ipynb

var workflow = new WorkflowBuilder(startExecutor)
            .AddFanOutEdge(startExecutor, targets: [researcherAgent, plannerAgent])
            .AddFanInEdge(aggregationExecutor, sources: [researcherAgent, plannerAgent])
            .WithOutputFrom(aggregationExecutor)
            .Build();
```

### Fall 4: Villkorligt arbetsflöde

Villkorliga arbetsflöden introducerar förgreningslogik, vilket gör att systemet kan ta olika vägar baserat på mellanresultat.

#### Scenario bakgrund

Detta arbetsflöde automatiserar skapandet och publiceringen av en teknisk handledning.

1.  **Evangelist-Agent**: Skriver ett utkast till handledningen baserat på en given disposition och URL:er.
2.  **ContentReviewer-Agent**: Granskar utkastet. Kontrollerar om ordantalet överstiger 200 ord.
3.  **Villkorlig gren**:
      * **Om godkänd (`Yes`)**: Arbetsflödet fortsätter till `Publisher-Agent`.
      * **Om avvisad (`No`)**: Arbetsflödet stoppas och ett avvisningsskäl ges som utdata.
4.  **Publisher-Agent**: Om utkastet godkänns sparar denna agent innehållet till en Markdown-fil.

#### Python-implementeringsanalys

Detta exempel använder en anpassad funktion, `select_targets`, för att implementera den villkorliga logiken. Denna funktion skickas till `add_multi_selection_edge_group` och styr arbetsflödet baserat på fältet `review_result` från granskarens utdata.

```python
# 04.python-agent-framework-workflow-aifoundry-condition.ipynb

# Denna funktion bestämmer nästa steg baserat på granskningsresultatet
def select_targets(review: ReviewResult, target_ids: list[str]) -> list[str]:
    handle_review_id, save_draft_id = target_ids
    if review.review_result == "Yes":
        # Om godkänd, fortsätt till 'save_draft'-exekutorn
        return [save_draft_id]
    else:
        # Om avvisad, fortsätt till 'handle_review'-exekutorn för att rapportera fel
        return [handle_review_id]

# Arbetsflödesbyggaren använder urvals-funktionen för routing
workflow = (
    WorkflowBuilder()
        .set_start_executor(evangelist_agent)
        .add_edge(evangelist_agent, reviewer_agent)
        .add_edge(reviewer_agent, to_reviewer_result)
        # Det flervalda kanter implementerar det villkorade logiken
        .add_multi_selection_edge_group(
            to_reviewer_result,
            [handle_review, save_draft],
            selection_func=select_targets,
        )
        .add_edge(save_draft, publisher_agent)
        .build()
)
```

Anpassade exekutörer som `to_reviewer_result` används för att tolka JSON-utdata från agenterna och konvertera den till starkt typade objekt som valfunktionen kan inspektera.

#### .NET (C\#) implementeringsanalys

.NET-versionen använder en liknande metod med en villkorsfunktion. En `Func<object?, bool>` definieras för att kontrollera `Result`-egenskapen hos `ReviewResult`-objektet.

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

Parametern `condition` i `AddEdge`-metoden låter `WorkflowBuilder` skapa en förgreningsväg. Arbetsflödet följer endast kanten till `publishExecutor` om villkoret `GetCondition(expectedResult: "Yes")` är sant. Annars följer det vägen till `sendReviewerExecutor`.

## Slutsats

Microsoft Agent Framework Workflow erbjuder en robust och flexibel grund för att orkestrera komplexa flermedelssystem. Genom att utnyttja dess grafbaserade arkitektur och kärnkomponenter kan utvecklare designa och implementera sofistikerade arbetsflöden i både Python och .NET. Oavsett om din applikation kräver enkel sekventiell bearbetning, parallell exekvering eller dynamisk villkorslogik, erbjuder ramverket verktygen för att bygga kraftfulla, skalbara och typ-säkra AI-drivna lösningar.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfriskrivning**:
Detta dokument har översatts med hjälp av AI-översättningstjänsten [Co-op Translator](https://github.com/Azure/co-op-translator). Även om vi strävar efter noggrannhet, var vänlig notera att automatiska översättningar kan innehålla fel eller brister. Det ursprungliga dokumentet på dess modersmål bör betraktas som den auktoritativa källan. För kritisk information rekommenderas professionell mänsklig översättning. Vi ansvarar inte för några missförstånd eller feltolkningar som uppstår till följd av användningen av denna översättning.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->