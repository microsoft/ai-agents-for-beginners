# Multi-Agenttoepassingen bouwen met Microsoft Agent Framework Workflow

Deze handleiding begeleidt je bij het begrijpen en bouwen van multi-agenttoepassingen met behulp van het Microsoft Agent Framework. We verkennen de kernconcepten van multi-agent systemen, duiken in de architectuur van het Workflow-component van het framework, en behandelen praktische voorbeelden in zowel Python als .NET voor verschillende workflowpatronen.

## 1\. Begrijpen van Multi-Agent Systemen

Een AI Agent is een systeem dat verder gaat dan de mogelijkheden van een standaard Large Language Model (LLM). Het kan zijn omgeving waarnemen, beslissingen nemen, en acties uitvoeren om specifieke doelen te bereiken. Een multi-agent systeem omvat meerdere van deze agents die samenwerken om een probleem op te lossen dat moeilijk of onmogelijk zou zijn voor een enkele agent alleen.

### Veelvoorkomende Toepassingsscenario’s

  * **Complex Probleemoplossen**: Het opsplitsen van een grote taak (bijv. het plannen van een bedrijfsevenement) in kleinere deelopdrachten die worden afgehandeld door gespecialiseerde agents (bijv. een budgetagent, een logistiek agent, een marketingagent).
  * **Virtuele Assistenten**: Een primaire assistent-agent die taken delegeert zoals planning, onderzoek en boekingen aan andere gespecialiseerde agents.
  * **Geautomatiseerde Contentcreatie**: Een workflow waarbij één agent inhoud opstelt, een andere deze controleert op nauwkeurigheid en toon, en een derde deze publiceert.

### Multi-Agent Patronen

Multi-agent systemen kunnen in verschillende patronen worden georganiseerd, die bepalen hoe ze interactie hebben:

  * **Sequentieel**: Agents werken in een vooraf bepaalde volgorde, zoals een assemblagelijn. De output van de ene agent wordt de input voor de volgende.
  * **Gelijktijdig**: Agents werken parallel aan verschillende delen van een taak, en hun resultaten worden aan het einde samengevoegd.
  * **Voorwaardelijk**: De workflow volgt verschillende paden gebaseerd op de output van een agent, vergelijkbaar met een if-then-else-structuur.

## 2\. De Architectuur van het Microsoft Agent Framework Workflow

Het workflow-systeem van het Agent Framework is een geavanceerde orkestratie-engine die complexe interacties tussen meerdere agents beheert. Het is gebouwd op een grafiek-gebaseerde architectuur die een [Pregel-stijl uitvoeringsmodel](https://kowshik.github.io/JPregel/pregel_paper.pdf) gebruikt, waarbij de verwerking plaatsvindt in gesynchroniseerde stappen genaamd "supersteps."

### Kerncomponenten

De architectuur bestaat uit drie hoofdonderdelen:

1.  **Executors**: Dit zijn de fundamentele verwerkingsunits. In onze voorbeelden is een `Agent` een type executor. Elke executor kan meerdere berichtverwerkers hebben die automatisch worden aangeroepen op basis van het type bericht dat binnenkomt.
2.  **Edges**: Deze definiëren het pad waarlangs berichten tussen executors reizen. Edges kunnen voorwaarden bevatten, waardoor dynamische routering van informatie door de workflow-grafiek mogelijk is.
3.  **Workflow**: Dit onderdeel orkestreert het volledige proces, beheert de executors, edges en de algemene uitvoering. Het zorgt ervoor dat berichten in de juiste volgorde worden verwerkt en streamt gebeurtenissen voor observeerbaarheid.

*Een diagram dat de kerncomponenten van het workflow-systeem illustreert.*

Deze structuur maakt het mogelijk robuuste en schaalbare applicaties te bouwen met fundamentele patronen zoals sequentiële ketens, fan-out/fan-in voor parallelle verwerking, en switch-case logica voor voorwaardelijke stromen.

## 3\. Praktische Voorbeelden en Codeanalyse

Laten we nu bekijken hoe verschillende workflowpatronen met het framework geïmplementeerd kunnen worden. We bekijken voor elk voorbeeld zowel Python- als .NET-code.

### Geval 1: Basis Sequentiële Workflow

Dit is het eenvoudigste patroon, waarbij de output van één agent direct aan een andere wordt doorgegeven. Onze situatie betreft een hotel `FrontDesk` agent die een reisaanbeveling doet, die vervolgens wordt beoordeeld door een `Concierge` agent.

*Diagram van de basis FrontDesk -\> Concierge workflow.*

#### Situatie Achtergrond

Een reiziger vraagt om een aanbeveling in Parijs.

1.  De `FrontDesk` agent, ontworpen voor beknoptheid, stelt een bezoek aan het Louvre voor.
2.  De `Concierge` agent, die authentieke ervaringen waardeert, ontvangt deze suggestie. Hij beoordeelt de aanbeveling en geeft feedback, met een voorstel voor een meer lokale, minder toeristische optie.

#### Analyse van Python-implementatie

In het Python-voorbeeld definiëren en creëren we eerst de twee agents, elk met specifieke instructies.

```python
# 01.python-agent-framework-workflow-ghmodel-basic.ipynb

# Definieer agentrollen en instructies
REVIEWER_NAME = "Concierge"
REVIEWER_INSTRUCTIONS = """
    You are an are hotel concierge who has opinions about providing the most local and authentic experiences for travelers...
    """

FRONTDESK_NAME = "FrontDesk"
FRONTDESK_INSTRUCTIONS = """
    You are a Front Desk Travel Agent with ten years of experience and are known for brevity...
    """

# Maak agentinstanties aan
reviewer_agent = chat_client.as_agent(
    instructions=(REVIEWER_INSTRUCTIONS),
    name=REVIEWER_NAME,
)

front_desk_agent = chat_client.as_agent(
    instructions=(FRONTDESK_INSTRUCTIONS),
    name=FRONTDESK_NAME,
)
```

Vervolgens gebruiken we de `WorkflowBuilder` om de grafiek op te bouwen. De `front_desk_agent` wordt als startpunt ingesteld, en er wordt een edge gemaakt die de output verbindt met de `reviewer_agent`.

```python
# 01.python-agent-framework-workflow-ghmodel-basic.ipynb

workflow = WorkflowBuilder(start_executor=front_desk_agent).add_edge(front_desk_agent, reviewer_agent).build()
```

Tot slot wordt de workflow uitgevoerd met de initiële gebruikersprompt.

```python
# 01.python-agent-framework-workflow-ghmodel-basic.ipynb

result =''
# run voert de workflow uit; get_outputs() geeft het resultaat van de uitvoerder terug.
events = await workflow.run('I would like to go to Paris.')
outputs = events.get_outputs()
result = outputs[0].text if outputs else ''
```

#### Analyse van .NET (C\#) implementatie

De .NET-implementatie volgt een vergelijkbare logica. Eerst worden constanten gedefinieerd voor de namen en instructies van de agents.

```csharp
// 01.dotnet-agent-framework-workflow-ghmodel-basic.ipynb

const string ReviewerAgentName = "Concierge";
const string ReviewerAgentInstructions = @"
    You are an are hotel concierge who has opinions about providing the most local and authentic experiences for travelers...";

const string FrontDeskAgentName = "FrontDesk";
const string FrontDeskAgentInstructions = @"""
    You are a Front Desk Travel Agent with ten years of experience and are known for brevity...";
```

De agents worden gemaakt met behulp van een `AzureOpenAIClient` (Responses API), en daarna definieert de `WorkflowBuilder` de sequentiële stroom door een edge toe te voegen van `frontDeskAgent` naar `reviewerAgent`.

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

De workflow wordt vervolgens uitgevoerd met het bericht van de gebruiker, en de resultaten worden teruggestreamd.

### Geval 2: Multi-Stap Sequentiële Workflow

Dit patroon breidt de basisvolgorde uit met meer agents. Het is ideaal voor processen die meerdere verfijnings- of transformatiefasen vereisen.

#### Situatie Achtergrond

Een gebruiker levert een afbeelding van een woonkamer en vraagt om een offerte voor meubels.

1.  **Sales-Agent**: Identificeert de meubels op de afbeelding en maakt een lijst.
2.  **Prijs-Agent**: Neemt de lijst met items en geeft een gedetailleerde prijsopgave, inclusief budget-, middenklasse- en premiumopties.
3.  **Offerte-Agent**: Ontvangt de geprijsde lijst en formatteert deze tot een formeel offerte-document in Markdown.

*Diagram van de Sales -\> Price -\> Quote workflow.*

#### Analyse van Python-implementatie

Drie agents worden gedefinieerd, elk met een gespecialiseerde rol. De workflow wordt opgebouwd door `add_edge` te gebruiken om een keten te maken: `sales_agent` -\> `price_agent` -\> `quote_agent`.

```python
# 02.python-agent-framework-workflow-ghmodel-sequential.ipynb

# Maak drie gespecialiseerde agenten
sales_agent = chat_client.as_agent(...)
price_agent = chat_client.as_agent(...)
quote_agent = chat_client.as_agent(...)

# Bouw de sequentiële workflow op
workflow = WorkflowBuilder(start_executor=sales_agent).add_edge(sales_agent, price_agent).add_edge(price_agent, quote_agent).build()
```

De input is een `ChatMessage` dat zowel tekst als de URI van de afbeelding bevat. Het framework zorgt ervoor dat de output van elke agent wordt doorgegeven aan de volgende in de volgorde totdat de definitieve offerte is gegenereerd.

```python
# 02.python-agent-framework-workflow-ghmodel-sequential.ipynb

# Het gebruikersbericht bevat zowel tekst als een afbeelding
message = ChatMessage(
        role=Role.USER,
        contents=[
            TextContent(text="Please find the relevant furniture..."),
            DataContent(uri=image_uri, media_type="image/png")
        ]
)

# Voer de workflow uit
events = await workflow.run(message)
```

#### Analyse van .NET (C\#) implementatie

Het .NET-voorbeeld weerspiegelt de Python-versie. Drie agents (`salesagent`, `priceagent`, `quoteagent`) worden gemaakt. De `WorkflowBuilder` koppelt ze sequentieel.

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

Het bericht van de gebruiker wordt samengesteld met zowel de afbeeldingsgegevens (als bytes) als de tekstprompt. De `InProcessExecution.StreamAsync`-methode start de workflow, en de definitieve output wordt uit de stream gehaald.

### Geval 3: Gelijktijdige Workflow

Dit patroon wordt gebruikt wanneer taken gelijktijdig kunnen worden uitgevoerd om tijd te besparen. Het omvat een "fan-out" naar meerdere agents en een "fan-in" om de resultaten te verzamelen.

#### Situatie Achtergrond

Een gebruiker vraagt om een reis naar Seattle te plannen.

1.  **Dispatcher (Fan-Out)**: Het verzoek van de gebruiker wordt tegelijkertijd naar twee agents gestuurd.
2.  **Onderzoeks-Agent**: Onderzoekt attracties, het weer, en belangrijke overwegingen voor een reis naar Seattle in december.
3.  **Plan-Agent**: Maakt zelfstandig een gedetailleerd dag-tot-dag reisschema.
4.  **Aggregator (Fan-In)**: De output van zowel de onderzoeker als de planner wordt verzameld en samen gepresenteerd als het eindresultaat.

*Diagram van de gelijktijdige Researcher en Planner workflow.*

#### Analyse van Python-implementatie

De `ConcurrentBuilder` maakt het creëren van dit patroon eenvoudiger. Je hoeft alleen de deelnemende agents te vermelden, en de builder maakt automatisch de benodigde fan-out en fan-in logica.

```python
# 03.python-agent-framework-workflow-ghmodel-concurrent.ipynb

research_agent = chat_client.as_agent(name="Researcher-Agent", ...)
plan_agent = chat_client.as_agent(name="Plan-Agent", ...)

# ConcurrentBuilder handelt de fan-out/fan-in logica af
workflow = ConcurrentBuilder().participants([research_agent, plan_agent]).build()

# Voer de workflow uit
events = await workflow.run("Plan a trip to Seattle in December")
```

Het framework zorgt ervoor dat de `research_agent` en `plan_agent` parallel uitvoeren, en hun uiteindelijke outputs worden verzameld in een lijst.

#### Analyse van .NET (C\#) implementatie

In .NET vereist dit patroon een explicietere definitie. Aangepaste executors (`ConcurrentStartExecutor` en `ConcurrentAggregationExecutor`) worden gemaakt om de fan-out en fan-in logica af te handelen.

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

De `WorkflowBuilder` gebruikt vervolgens `AddFanOutEdge` en `AddFanInEdge` om de grafiek te bouwen met deze aangepaste executors en de agents.

```csharp
// 03.dotnet-agent-framework-workflow-ghmodel-concurrent.ipynb

var workflow = new WorkflowBuilder(startExecutor)
            .AddFanOutEdge(startExecutor, targets: [researcherAgent, plannerAgent])
            .AddFanInEdge(aggregationExecutor, sources: [researcherAgent, plannerAgent])
            .WithOutputFrom(aggregationExecutor)
            .Build();
```

### Geval 4: Voorwaardelijke Workflow

Voorwaardelijke workflows introduceren vertakkingslogica, waardoor het systeem verschillende paden kan volgen op basis van tussentijdse resultaten.

#### Situatie Achtergrond

Deze workflow automatiseert het maken en publiceren van een technische tutorial.

1.  **Evangelist-Agent**: Schrijft een concept van de tutorial op basis van een gegeven overzicht en URL’s.
2.  **ContentReviewer-Agent**: Beoordeelt het concept. Het controleert of het woordenaantal meer dan 200 is.
3.  **Voorwaardelijke Vertakking**:
      * **Als Goedgekeurd (`Ja`)**: De workflow gaat door naar de `Publisher-Agent`.
      * **Als Afgewezen (`Nee`)**: De workflow stopt en geeft de reden van afwijzing weer.
4.  **Publisher-Agent**: Als het concept is goedgekeurd, slaat deze agent de inhoud op in een Markdown-bestand.

#### Analyse van Python-implementatie

Dit voorbeeld gebruikt een aangepaste functie, `select_targets`, om de voorwaardelijke logica te implementeren. Deze functie wordt doorgegeven aan `add_multi_selection_edge_group` en stuurt de workflow op basis van het `review_result`-veld uit de output van de reviewer.

```python
# 04.python-agent-framework-workflow-aifoundry-condition.ipynb

# Deze functie bepaalt de volgende stap op basis van het beoordelingsresultaat
def select_targets(review: ReviewResult, target_ids: list[str]) -> list[str]:
    handle_review_id, save_draft_id = target_ids
    if review.review_result == "Yes":
        # Indien goedgekeurd, ga verder naar de 'save_draft' executor
        return [save_draft_id]
    else:
        # Indien afgewezen, ga verder naar de 'handle_review' executor om de mislukking te melden
        return [handle_review_id]

# De workflow-builder gebruikt de selectiefunctie voor routering
workflow = (
    WorkflowBuilder()
        .set_start_executor(evangelist_agent)
        .add_edge(evangelist_agent, reviewer_agent)
        .add_edge(reviewer_agent, to_reviewer_result)
        # De multi-selectie rand implementeert de conditionele logica
        .add_multi_selection_edge_group(
            to_reviewer_result,
            [handle_review, save_draft],
            selection_func=select_targets,
        )
        .add_edge(save_draft, publisher_agent)
        .build()
)
```

Aangepaste executors zoals `to_reviewer_result` worden gebruikt om de JSON-output van de agents te parsen en om te zetten in sterk getypeerde objecten die de selectiefunctie kan inspecteren.

#### Analyse van .NET (C\#) implementatie

De .NET-versie gebruikt een vergelijkbare aanpak met een conditiefunctie. Een `Func<object?, bool>` wordt gedefinieerd om de `Result`-eigenschap van het `ReviewResult`-object te controleren.

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

De `AddEdge`-methode met de `condition`-parameter maakt het voor de `WorkflowBuilder` mogelijk een vertakkend pad te creëren. De workflow volgt alleen de edge naar `publishExecutor` als de conditie `GetCondition(expectedResult: "Yes")` waar is. Anders volgt hij het pad naar `sendReviewerExecutor`.

## Conclusie

Het Microsoft Agent Framework Workflow biedt een robuuste en flexibele basis voor het orkestreren van complexe multi-agent systemen. Door gebruik te maken van zijn grafiek-gebaseerde architectuur en kerncomponenten, kunnen ontwikkelaars geavanceerde workflows ontwerpen en implementeren in zowel Python als .NET. Of je applicatie nu eenvoudige sequentiële verwerking, parallelle uitvoering, of dynamische voorwaardelijke logica vereist, het framework biedt de tools om krachtige, schaalbare en type-veilige AI-gestuurde oplossingen te bouwen.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:
Dit document is vertaald met behulp van de AI vertaaldienst [Co-op Translator](https://github.com/Azure/co-op-translator). Hoewel we streven naar nauwkeurigheid, dient u er rekening mee te houden dat geautomatiseerde vertalingen fouten of onnauwkeurigheden kunnen bevatten. Het originele document in de oorspronkelijke taal moet worden beschouwd als de gezaghebbende bron. Voor kritieke informatie wordt professionele menselijke vertaling aanbevolen. Wij zijn niet aansprakelijk voor eventuele misverstanden of verkeerde interpretaties die voortvloeien uit het gebruik van deze vertaling.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->