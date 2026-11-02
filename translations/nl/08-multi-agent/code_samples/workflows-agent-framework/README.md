# Multi-Agent Toepassingen bouwen met Microsoft Agent Framework Workflow

Deze tutorial leidt je door het begrijpen en bouwen van multi-agent toepassingen met behulp van het Microsoft Agent Framework. We verkennen de kernconcepten van multi-agent systemen, duiken in de architectuur van de Workflow-component van het framework, en lopen door praktische voorbeelden in zowel Python als .NET voor verschillende workflowpatronen.

## 1\. Begrijpen van Multi-Agent Systemen

Een AI-agent is een systeem dat verder gaat dan de mogelijkheden van een standaard Large Language Model (LLM). Het kan zijn omgeving waarnemen, besluiten nemen en acties uitvoeren om specifieke doelen te bereiken. Een multi-agent systeem omvat meerdere van deze agenten die samenwerken om een probleem op te lossen dat moeilijk of onmogelijk is voor een enkele agent om alleen aan te pakken.

### Veelvoorkomende Toepassingsscenario's

  * **Complex Probleemoplossen**: Het opsplitsen van een grote taak (bijv. het plannen van een bedrijfsevenement) in kleinere subtaken die worden afgehandeld door gespecialiseerde agenten (bijv. een budgetagent, een logistieke agent, een marketingagent).
  * **Virtuele Assistenten**: Een hoofdassistent-agent die taken delegeert zoals planning, onderzoek en boekingen aan andere gespecialiseerde agenten.
  * **Geautomatiseerde Contentcreatie**: Een workflow waarbij de ene agent content opstelt, een andere agent deze controleert op nauwkeurigheid en toon, en een derde agent deze publiceert.

### Multi-Agent Patronen

Multi-agent systemen kunnen in verschillende patronen worden georganiseerd, die bepalen hoe ze met elkaar communiceren:

  * **Sequentieel**: Agenten werken in een vooraf bepaalde volgorde, zoals op een lopende band. De output van de ene agent wordt de input voor de volgende.
  * **Gelijktijdig**: Agenten werken parallel aan verschillende delen van een taak, en hun resultaten worden aan het einde samengevoegd.
  * **Conditioneel**: De workflow volgt verschillende paden gebaseerd op de output van een agent, vergelijkbaar met een if-then-else-structuur.

## 2\. De Architectuur van Microsoft Agent Framework Workflow

Het workflow-systeem van het Agent Framework is een geavanceerde orkestratie-engine ontworpen om complexe interacties tussen meerdere agenten te beheren. Het is gebouwd op een grafiekgebaseerde architectuur die een [Pregel-stijl uitvoermodel](https://kowshik.github.io/JPregel/pregel_paper.pdf) gebruikt, waarbij verwerking plaatsvindt in gesynchroniseerde stappen die "supersteps" worden genoemd.

### Kerncomponenten

De architectuur bestaat uit drie hoofdonderdelen:

1.  **Executors**: Dit zijn de fundamentele verwerkingseenheden. In onze voorbeelden is een `Agent` een type executor. Elke executor kan meerdere berichtverwerkers hebben die automatisch worden aangeroepen op basis van het type ontvangen bericht.
2.  **Edges**: Deze definiëren het pad dat berichten afleggen tussen executors. Edges kunnen voorwaarden hebben, waardoor dynamische routering van informatie door de workflowgrafiek mogelijk is.
3.  **Workflow**: Deze component orkestreert het gehele proces, beheert de executors, edges en de algemene uitvoerflow. Het zorgt ervoor dat berichten in de juiste volgorde worden verwerkt en streamt gebeurtenissen voor observeerbaarheid.

*Een diagram dat de kerncomponenten van het workflowsysteem illustreert.*

Deze structuur maakt het mogelijk om robuuste en schaalbare applicaties te bouwen met fundamentele patronen zoals sequentiële ketens, fan-out/fan-in voor parallelle verwerking, en switch-case logica voor conditionele flows.

## 3\. Praktische Voorbeelden en Codeanalyse

Laten we nu verkennen hoe we verschillende workflowpatronen kunnen implementeren met het framework. We bekijken zowel Python- als .NET-code voor elk voorbeeld.

### Geval 1: Basis Sequentiële Workflow

Dit is het eenvoudigste patroon, waarbij de output van één agent direct wordt doorgegeven aan een andere. Ons scenario omvat een hotel `FrontDesk` agent die een reisadvies geeft, dat vervolgens wordt beoordeeld door een `Concierge` agent.

*Diagram van de basis FrontDesk -> Concierge workflow.*

#### Scenario Achtergrond

Een reiziger vraagt om een aanbeveling in Parijs.

1.  De `FrontDesk` agent, ontworpen voor beknoptheid, stelt voor om het Louvre Museum te bezoeken.
2.  De `Concierge` agent, die authenticiteit belangrijk vindt, ontvangt deze suggestie. Hij beoordeelt de aanbeveling en geeft feedback, met een voorstel voor een lokale, minder toeristische optie.

#### Python Implementatie Analyse

In het Python-voorbeeld definiëren we eerst en creëren we de twee agenten, elk met specifieke instructies.

```python
# 01.python-agent-framework-workflow-ghmodel-basic.ipynb

# Definieer agentrollen en instructies
REVIEWER_NAME = "Concierge"
REVIEWER_INSTRUCTIONS = """
    You are a hotel concierge who has opinions about providing the most local and authentic experiences for travelers...
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

Vervolgens wordt `WorkflowBuilder` gebruikt om de grafiek op te bouwen. De `front_desk_agent` wordt ingesteld als startpunt, en er wordt een edge gemaakt om zijn output te verbinden met de `reviewer_agent`.

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

#### .NET (C\#) Implementatie Analyse

De .NET-implementatie volgt een vergelijkbare logica. Eerst worden constanten gedefinieerd voor de namen van de agenten en hun instructies.

```csharp
// 01.dotnet-agent-framework-workflow-ghmodel-basic.ipynb

const string ReviewerAgentName = "Concierge";
const string ReviewerAgentInstructions = @"
    You are a hotel concierge who has opinions about providing the most local and authentic experiences for travelers...";

const string FrontDeskAgentName = "FrontDesk";
const string FrontDeskAgentInstructions = @"""
    You are a Front Desk Travel Agent with ten years of experience and are known for brevity...";
```

De agenten worden gecreëerd met behulp van een `AzureOpenAIClient` (Responses API), en vervolgens definieert `WorkflowBuilder` de sequentiële flow door een edge toe te voegen van `frontDeskAgent` naar `reviewerAgent`.

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

Daarna wordt de workflow uitgevoerd met het bericht van de gebruiker, en worden de resultaten gestreamd terug.

### Geval 2: Multi-Stap Sequentiële Workflow

Dit patroon breidt de basisreeks uit met meer agenten. Het is ideaal voor processen die meerdere verfijnings- of transformatiefasen vereisen.

#### Scenario Achtergrond

Een gebruiker levert een afbeelding van een woonkamer aan en vraagt om een meubelofferte.

1.  **Sales-Agent**: Identificeert de meubels in de afbeelding en maakt een lijst.
2.  **Price-Agent**: Neemt de lijst met items en geeft een gedetailleerde prijsopbouw, inclusief budget-, middenklasse- en premiumopties.
3.  **Quote-Agent**: Ontvangt de geprijsde lijst en formatteert deze in een formeel offerte-document in Markdown.

*Diagram van de Sales -> Price -> Quote workflow.*

#### Python Implementatie Analyse

Drie agenten worden gedefinieerd, elk met een gespecialiseerde rol. De workflow wordt opgebouwd met `add_edge` om een keten te maken: `sales_agent` -> `price_agent` -> `quote_agent`.

```python
# 02.python-agent-framework-workflow-ghmodel-sequential.ipynb

# Maak drie gespecialiseerde agenten
sales_agent = chat_client.as_agent(...)
price_agent = chat_client.as_agent(...)
quote_agent = chat_client.as_agent(...)

# Bouw de sequentiële workflow op
workflow = WorkflowBuilder(start_executor=sales_agent).add_edge(sales_agent, price_agent).add_edge(price_agent, quote_agent).build()
```

De input is een `ChatMessage` die zowel tekst als de afbeeldings-URI bevat. Het framework zorgt ervoor dat de output van elke agent wordt doorgegeven aan de volgende in de keten totdat de definitieve offerte is gegenereerd.

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

#### .NET (C\#) Implementatie Analyse

Het .NET-voorbeeld weerspiegelt de Python-versie. Drie agenten (`salesagent`, `priceagent`, `quoteagent`) worden gecreëerd. De `WorkflowBuilder` koppelt ze achtereenvolgens.

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

Het bericht van de gebruiker wordt samengesteld met zowel de afbeeldingsgegevens (als bytes) als de tekstprompt. De methode `InProcessExecution.RunStreamingAsync` start de workflow, en de uiteindelijke uitvoer wordt uit de stream opgehaald.

### Geval 3: Gelijktijdige Workflow

Dit patroon wordt gebruikt wanneer taken gelijktijdig kunnen worden uitgevoerd om tijd te besparen. Het omvat een "fan-out" naar meerdere agenten en een "fan-in" om de resultaten te aggregeren.

#### Scenario Achtergrond

Een gebruiker vraagt om een reis naar Seattle te plannen.

1.  **Dispatcher (Fan-Out)**: Het verzoek van de gebruiker wordt tegelijkertijd naar twee agenten gestuurd.
2.  **Researcher-Agent**: Onderzoekt attracties, weer en belangrijke overwegingen voor een reis naar Seattle in december.
3.  **Plan-Agent**: Maakt zelfstandig een gedetailleerde dag-tot-dag reisroute.
4.  **Aggregator (Fan-In)**: De outputs van zowel de onderzoeker als de planner worden verzameld en samen gepresenteerd als het eindresultaat.

*Diagram van de gelijktijdige Researcher- en Planner-workflow.*

#### Python Implementatie Analyse

De `ConcurrentBuilder` vereenvoudigt het maken van dit patroon. Je geeft simpelweg de deelnemende agenten op, en de builder maakt automatisch de benodigde fan-out en fan-in logica aan.

```python
# 03.python-agent-framework-workflow-ghmodel-concurrent.ipynb

research_agent = chat_client.as_agent(name="Researcher-Agent", ...)
plan_agent = chat_client.as_agent(name="Plan-Agent", ...)

# ConcurrentBuilder handelt de fan-out/fan-in logica af
workflow = ConcurrentBuilder().participants([research_agent, plan_agent]).build()

# Voer de workflow uit
events = await workflow.run("Plan a trip to Seattle in December")
```

Het framework zorgt ervoor dat de `research_agent` en `plan_agent` parallel uitvoeren, en hun eindresultaten worden verzameld in een lijst.

#### .NET (C\#) Implementatie Analyse

In .NET vereist dit patroon een explicietere definitie. Aangepaste executors (`ConcurrentStartExecutor` en `ConcurrentAggregationExecutor`) worden gecreëerd om de fan-out en fan-in logica af te handelen.

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

De `WorkflowBuilder` gebruikt dan `AddFanOutEdge` en `AddFanInEdge` om de grafiek te bouwen met deze aangepaste executors en de agenten.

```csharp
// 03.dotnet-agent-framework-workflow-ghmodel-concurrent.ipynb

var workflow = new WorkflowBuilder(startExecutor)
            .AddFanOutEdge(startExecutor, targets: [researcherAgent, plannerAgent])
            .AddFanInEdge(aggregationExecutor, sources: [researcherAgent, plannerAgent])
            .WithOutputFrom(aggregationExecutor)
            .Build();
```

### Geval 4: Conditionele Workflow

Conditionele workflows introduceren vertakkingslogica, waardoor het systeem verschillende paden kan volgen op basis van tussentijdse resultaten.

#### Scenario Achtergrond

Deze workflow automatiseert het aanmaken en publiceren van een technische tutorial.

1.  **Evangelist-Agent**: Schrijft een concept van de tutorial op basis van een gegeven overzicht en URL's.
2.  **ContentReviewer-Agent**: Beoordeelt het concept. Controleert of het aantal woorden boven de 200 ligt.
3.  **Conditionele Vertakking**:
      * **Als Goedgekeurd (`Ja`)**: De workflow gaat verder naar de `Publisher-Agent`.
      * **Als Afgewezen (`Nee`)**: De workflow stopt en geeft de reden van afwijzing.
4.  **Publisher-Agent**: Als het concept is goedgekeurd, slaat deze agent de inhoud op in een Markdown-bestand.

#### Python Implementatie Analyse

Dit voorbeeld gebruikt een aangepaste functie, `select_targets`, om de conditionele logica te implementeren. Deze functie wordt doorgegeven aan `add_multi_selection_edge_group` en leidt de workflow op basis van het veld `review_result` uit de output van de reviewer.

```python
# 04.python-agent-framework-workflow-aifoundry-condition.ipynb

# Deze functie bepaalt de volgende stap op basis van het beoordelingsresultaat
def select_targets(review: ReviewResult, target_ids: list[str]) -> list[str]:
    handle_review_id, save_draft_id = target_ids
    if review.review_result == "Yes":
        # Bij goedkeuring, verder naar de 'save_draft' executor
        return [save_draft_id]
    else:
        # Bij afwijzing, verder naar de 'handle_review' executor om de fout te rapporteren
        return [handle_review_id]

# De workflow-bouwer gebruikt de selectiefunctie voor routinguitschakeling
workflow = (
    WorkflowBuilder()
        .set_start_executor(evangelist_agent)
        .add_edge(evangelist_agent, reviewer_agent)
        .add_edge(reviewer_agent, to_reviewer_result)
        # De multi-selectierand implementeert de conditionele logica
        .add_multi_selection_edge_group(
            to_reviewer_result,
            [handle_review, save_draft],
            selection_func=select_targets,
        )
        .add_edge(save_draft, publisher_agent)
        .build()
)
```

Aangepaste executors zoals `to_reviewer_result` worden gebruikt om de JSON-output van de agenten te parseren en om te zetten in sterk getypte objecten die de selectiefunctie kan inspecteren.

#### .NET (C\#) Implementatie Analyse

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

De `AddEdge`-methode met het `condition`-parameter maakt het voor de `WorkflowBuilder` mogelijk om een vertakkend pad te creëren. De workflow volgt alleen de edge naar `publishExecutor` als de conditie `GetCondition(expectedResult: "Yes")` waar retourneert. Anders volgt het het pad naar `sendReviewerExecutor`.

## Conclusie

Het Microsoft Agent Framework Workflow biedt een robuuste en flexibele basis voor het orkestreren van complexe multi-agent systemen. Door gebruik te maken van de grafiekgebaseerde architectuur en kerncomponenten kunnen ontwikkelaars geavanceerde workflows ontwerpen en implementeren in zowel Python als .NET. Of je applicatie nu eenvoudige sequentiële verwerkingen, parallelle uitvoeringen, of dynamische conditionele logica vereist, het framework biedt de tools om krachtige, schaalbare en type-veilige AI-aangedreven oplossingen te bouwen.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:
Dit document is vertaald met behulp van de AI vertaaldienst [Co-op Translator](https://github.com/Azure/co-op-translator). Hoewel we streven naar nauwkeurigheid, dient u er rekening mee te houden dat geautomatiseerde vertalingen fouten of onnauwkeurigheden kunnen bevatten. Het originele document in de oorspronkelijke taal moet worden beschouwd als de gezaghebbende bron. Voor kritieke informatie wordt professionele menselijke vertaling aanbevolen. Wij zijn niet aansprakelijk voor eventuele misverstanden of verkeerde interpretaties die voortvloeien uit het gebruik van deze vertaling.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->