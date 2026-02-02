# Multi-Agent Applicaties Bouwen met Microsoft Agent Framework Workflow

Deze tutorial begeleidt je bij het begrijpen en bouwen van multi-agent applicaties met behulp van het Microsoft Agent Framework. We verkennen de kernconcepten van multi-agent systemen, duiken in de architectuur van de Workflow-component van het framework, en doorlopen praktische voorbeelden in zowel Python als .NET voor verschillende workflowpatronen.

## 1\. Begrijpen van Multi-Agent Systemen

Een AI-agent is een systeem dat verder gaat dan de mogelijkheden van een standaard Large Language Model (LLM). Het kan zijn omgeving waarnemen, beslissingen nemen en acties ondernemen om specifieke doelen te bereiken. Een multi-agent systeem omvat meerdere van deze agents die samenwerken om een probleem op te lossen dat moeilijk of onmogelijk door een enkele agent kan worden afgehandeld.

### Veelvoorkomende Toepassingsscenario's

  * **Complex Probleemoplossing**: Het opsplitsen van een grote taak (bijv. het plannen van een bedrijfsbreed evenement) in kleinere subtaken die worden afgehandeld door gespecialiseerde agents (bijv. een budgetagent, een logistieke agent, een marketingagent).
  * **Virtuele Assistenten**: Een primaire assistent-agent die taken zoals plannen, onderzoek en boeken delegeert aan andere gespecialiseerde agents.
  * **Geautomatiseerde Contentcreatie**: Een workflow waarbij één agent content opstelt, een andere deze controleert op nauwkeurigheid en toon, en een derde deze publiceert.

### Multi-Agent Patronen

Multi-agent systemen kunnen worden georganiseerd in verschillende patronen, die bepalen hoe ze interageren:

  * **Sequentieel**: Agents werken in een vooraf bepaalde volgorde, zoals een assemblagelijn. De output van de ene agent wordt de input voor de volgende.
  * **Gelijktijdig**: Agents werken parallel aan verschillende delen van een taak, en hun resultaten worden aan het einde samengevoegd.
  * **Conditioneel**: De workflow volgt verschillende paden op basis van de output van een agent, vergelijkbaar met een if-then-else statement.

## 2\. De Microsoft Agent Framework Workflow Architectuur

Het workflowsysteem van het Agent Framework is een geavanceerde orkestratiemotor die complexe interacties tussen meerdere agents beheert. Het is gebouwd op een grafgebaseerde architectuur die gebruikmaakt van een [Pregel-stijl uitvoeringsmodel](https://kowshik.github.io/JPregel/pregel_paper.pdf), waarbij verwerking plaatsvindt in gesynchroniseerde stappen, "supersteps" genoemd.

### Kerncomponenten

De architectuur bestaat uit drie hoofdonderdelen:

1.  **Executors**: Dit zijn de fundamentele verwerkingsunits. In onze voorbeelden is een `Agent` een type executor. Elke executor kan meerdere berichtverwerkers hebben die automatisch worden aangeroepen op basis van het type ontvangen bericht.
2.  **Edges**: Deze definiëren het pad dat berichten nemen tussen executors. Edges kunnen voorwaarden hebben, waardoor dynamische routering van informatie door de workflowgrafiek mogelijk is.
3.  **Workflow**: Dit onderdeel orkestreert het hele proces, beheert de executors, edges en de algehele uitvoeringsstroom. Het zorgt ervoor dat berichten in de juiste volgorde worden verwerkt en streamt gebeurtenissen voor observatie.

*Een diagram dat de kerncomponenten van het workflowsysteem illustreert.*

Deze structuur maakt het mogelijk om robuuste en schaalbare applicaties te bouwen met fundamentele patronen zoals sequentiële ketens, fan-out/fan-in voor parallelle verwerking, en switch-case logica voor conditionele stromen.

## 3\. Praktische Voorbeelden en Codeanalyse

Laten we nu bekijken hoe verschillende workflowpatronen kunnen worden geïmplementeerd met het framework. We zullen zowel Python- als .NET-code voor elk voorbeeld bekijken.

### Case 1: Basis Sequentiële Workflow

Dit is het eenvoudigste patroon, waarbij de output van één agent direct wordt doorgegeven aan een andere. Ons scenario omvat een hotel `FrontDesk` agent die een reisaanbeveling doet, die vervolgens wordt beoordeeld door een `Concierge` agent.

*Diagram van de basis FrontDesk -\> Concierge workflow.*

#### Scenario Achtergrond

Een reiziger vraagt om een aanbeveling in Parijs.

1.  De `FrontDesk` agent, ontworpen voor beknoptheid, stelt voor om het Louvre Museum te bezoeken.
2.  De `Concierge` agent, die authentieke ervaringen prioriteert, ontvangt deze suggestie. Het beoordeelt de aanbeveling en geeft feedback, waarbij een meer lokale, minder toeristische alternatieve wordt voorgesteld.

#### Python Implementatie Analyse

In het Python-voorbeeld definiëren en maken we eerst de twee agents, elk met specifieke instructies.

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

Vervolgens wordt de `WorkflowBuilder` gebruikt om de grafiek te construeren. De `front_desk_agent` wordt ingesteld als het startpunt, en er wordt een edge gemaakt om de output ervan te verbinden met de `reviewer_agent`.

```python
# 01.python-agent-framework-workflow-ghmodel-basic.ipynb

workflow = WorkflowBuilder().set_start_executor(front_desk_agent).add_edge(front_desk_agent, reviewer_agent).build()
```

Ten slotte wordt de workflow uitgevoerd met de initiële gebruikersprompt.

```python
# 01.python-agent-framework-workflow-ghmodel-basic.ipynb

result =''
# The run_stream method executes the workflow and streams events.
async for event in workflow.run_stream('I would like to go to Paris.'):
    if isinstance(event, WorkflowEvent):
        result += str(event.data)
```

#### .NET (C\#) Implementatie Analyse

De .NET-implementatie volgt een zeer vergelijkbare logica. Eerst worden constanten gedefinieerd voor de namen en instructies van de agents.

```csharp
// 01.dotnet-agent-framework-workflow-ghmodel-basic.ipynb

const string ReviewerAgentName = "Concierge";
const string ReviewerAgentInstructions = @"
    You are an are hotel concierge who has opinions about providing the most local and authentic experiences for travelers...";

const string FrontDeskAgentName = "FrontDesk";
const string FrontDeskAgentInstructions = @"""
    You are a Front Desk Travel Agent with ten years of experience and are known for brevity...";
```

De agents worden gemaakt met behulp van een `OpenAIClient`, en vervolgens definieert de `WorkflowBuilder` de sequentiële stroom door een edge toe te voegen van de `frontDeskAgent` naar de `reviewerAgent`.

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

De workflow wordt vervolgens uitgevoerd met het bericht van de gebruiker, en de resultaten worden gestreamd.

### Case 2: Multi-Step Sequentiële Workflow

Dit patroon breidt de basisvolgorde uit met meer agents. Het is ideaal voor processen die meerdere stadia van verfijning of transformatie vereisen.

#### Scenario Achtergrond

Een gebruiker levert een afbeelding van een woonkamer en vraagt om een meubelofferte.

1.  **Sales-Agent**: Identificeert de meubelstukken in de afbeelding en maakt een lijst.
2.  **Price-Agent**: Neemt de lijst met items en biedt een gedetailleerde prijsopgave, inclusief budget-, middenklasse- en premiumopties.
3.  **Quote-Agent**: Ontvangt de geprijsde lijst en formatteert deze tot een formeel offerte-document in Markdown.

*Diagram van de Sales -\> Price -\> Quote workflow.*

#### Python Implementatie Analyse

Drie agents worden gedefinieerd, elk met een gespecialiseerde rol. De workflow wordt geconstrueerd met behulp van `add_edge` om een keten te maken: `sales_agent` -\> `price_agent` -\> `quote_agent`.

```python
# 02.python-agent-framework-workflow-ghmodel-sequential.ipynb

# Create three specialized agents
sales_agent = chat_client.create_agent(...)
price_agent = chat_client.create_agent(...)
quote_agent = chat_client.create_agent(...)

# Build the sequential workflow
workflow = WorkflowBuilder().set_start_executor(sales_agent).add_edge(sales_agent, price_agent).add_edge(price_agent, quote_agent).build()
```

De input is een `ChatMessage` die zowel tekst als de afbeelding-URI bevat. Het framework zorgt ervoor dat de output van elke agent wordt doorgegeven aan de volgende in de volgorde totdat de uiteindelijke offerte is gegenereerd.

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

#### .NET (C\#) Implementatie Analyse

Het .NET-voorbeeld weerspiegelt de Python-versie. Drie agents (`salesagent`, `priceagent`, `quoteagent`) worden gemaakt. De `WorkflowBuilder` koppelt ze sequentieel.

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

Het bericht van de gebruiker wordt samengesteld met zowel de afbeeldingsgegevens (als bytes) als de tekstprompt. De `InProcessExecution.StreamAsync` methode start de workflow, en de uiteindelijke output wordt uit de stream gehaald.

### Case 3: Gelijktijdige Workflow

Dit patroon wordt gebruikt wanneer taken gelijktijdig kunnen worden uitgevoerd om tijd te besparen. Het omvat een "fan-out" naar meerdere agents en een "fan-in" om de resultaten te verzamelen.

#### Scenario Achtergrond

Een gebruiker vraagt om een reis naar Seattle te plannen.

1.  **Dispatcher (Fan-Out)**: Het verzoek van de gebruiker wordt tegelijkertijd naar twee agents gestuurd.
2.  **Researcher-Agent**: Onderzoekt attracties, weer en belangrijke overwegingen voor een reis naar Seattle in december.
3.  **Plan-Agent**: Maakt onafhankelijk een gedetailleerd dag-tot-dag reisplan.
4.  **Aggregator (Fan-In)**: De outputs van zowel de onderzoeker als de planner worden verzameld en samen gepresenteerd als het eindresultaat.

*Diagram van de gelijktijdige Researcher en Planner workflow.*

#### Python Implementatie Analyse

De `ConcurrentBuilder` vereenvoudigt het maken van dit patroon. Je geeft eenvoudig de deelnemende agents op, en de builder creëert automatisch de benodigde fan-out en fan-in logica.

```python
# 03.python-agent-framework-workflow-ghmodel-concurrent.ipynb

research_agent = chat_client.create_agent(name="Researcher-Agent", ...)
plan_agent = chat_client.create_agent(name="Plan-Agent", ...)

# ConcurrentBuilder handles the fan-out/fan-in logic
workflow = ConcurrentBuilder().participants([research_agent, plan_agent]).build()

# Run the workflow
events = await workflow.run("Plan a trip to Seattle in December")
```

Het framework zorgt ervoor dat de `research_agent` en `plan_agent` parallel worden uitgevoerd, en hun uiteindelijke outputs worden verzameld in een lijst.

#### .NET (C\#) Implementatie Analyse

In .NET vereist dit patroon een meer expliciete definitie. Aangepaste executors (`ConcurrentStartExecutor` en `ConcurrentAggregationExecutor`) worden gemaakt om de fan-out en fan-in logica te beheren.

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

De `WorkflowBuilder` gebruikt vervolgens `AddFanOutEdge` en `AddFanInEdge` om de grafiek te construeren met deze aangepaste executors en de agents.

```csharp
// 03.dotnet-agent-framework-workflow-ghmodel-concurrent.ipynb

var workflow = new WorkflowBuilder(startExecutor)
            .AddFanOutEdge(startExecutor, targets: [researcherAgent, plannerAgent])
            .AddFanInEdge(aggregationExecutor, sources: [researcherAgent, plannerAgent])
            .WithOutputFrom(aggregationExecutor)
            .Build();
```

### Case 4: Conditionele Workflow

Conditionele workflows introduceren vertakkingslogica, waardoor het systeem verschillende paden kan volgen op basis van tussentijdse resultaten.

#### Scenario Achtergrond

Deze workflow automatiseert het maken en publiceren van een technische tutorial.

1.  **Evangelist-Agent**: Schrijft een concept van de tutorial op basis van een gegeven outline en URL's.
2.  **ContentReviewer-Agent**: Beoordeelt het concept. Het controleert of het aantal woorden meer dan 200 is.
3.  **Conditionele Vertakking**:
      * **Als Goedgekeurd (`Ja`)**: De workflow gaat verder naar de `Publisher-Agent`.
      * **Als Afgewezen (`Nee`)**: De workflow stopt en geeft de reden voor afwijzing.
4.  **Publisher-Agent**: Als het concept is goedgekeurd, slaat deze agent de inhoud op in een Markdown-bestand.

#### Python Implementatie Analyse

Dit voorbeeld gebruikt een aangepaste functie, `select_targets`, om de conditionele logica te implementeren. Deze functie wordt doorgegeven aan `add_multi_selection_edge_group` en stuurt de workflow op basis van het `review_result` veld van de output van de reviewer.

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

Aangepaste executors zoals `to_reviewer_result` worden gebruikt om de JSON-output van de agents te parseren en om te zetten in sterk getypeerde objecten die de selectiefunctie kan inspecteren.

#### .NET (C\#) Implementatie Analyse

De .NET-versie gebruikt een vergelijkbare aanpak met een conditiefunctie. Een `Func<object?, bool>` wordt gedefinieerd om de `Result` eigenschap van het `ReviewResult` object te controleren.

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

De `AddEdge` methode's `condition` parameter stelt de `WorkflowBuilder` in staat om een vertakkingspad te creëren. De workflow volgt alleen de edge naar `publishExecutor` als de conditie `GetCondition(expectedResult: "Yes")` true retourneert. Anders volgt het het pad naar `sendReviewerExecutor`.

## Conclusie

Het Microsoft Agent Framework Workflow biedt een robuuste en flexibele basis voor het orkestreren van complexe, multi-agent systemen. Door gebruik te maken van de grafgebaseerde architectuur en kerncomponenten kunnen ontwikkelaars geavanceerde workflows ontwerpen en implementeren in zowel Python als .NET. Of je applicatie nu eenvoudige sequentiële verwerking, parallelle uitvoering of dynamische conditionele logica vereist, het framework biedt de tools om krachtige, schaalbare en type-veilige AI-oplossingen te bouwen.

---

**Disclaimer**:  
Dit document is vertaald met behulp van de AI-vertalingsservice [Co-op Translator](https://github.com/Azure/co-op-translator). Hoewel we streven naar nauwkeurigheid, dient u zich ervan bewust te zijn dat geautomatiseerde vertalingen fouten of onnauwkeurigheden kunnen bevatten. Het originele document in de oorspronkelijke taal moet worden beschouwd als de gezaghebbende bron. Voor cruciale informatie wordt professionele menselijke vertaling aanbevolen. Wij zijn niet aansprakelijk voor misverstanden of verkeerde interpretaties die voortvloeien uit het gebruik van deze vertaling.