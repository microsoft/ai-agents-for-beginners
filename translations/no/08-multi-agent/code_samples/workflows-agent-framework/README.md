# Bygge Multi-Agent Applikasjoner med Microsoft Agent Framework Workflow

Denne veiledningen hjelper deg med å forstå og bygge multi-agent applikasjoner ved bruk av Microsoft Agent Framework. Vi skal utforske kjernekonseptene for multi-agent systemer, dykke ned i arkitekturen til rammeverkets Workflow-komponent, og gå gjennom praktiske eksempler i både Python og .NET for ulike workflow-mønstre.

## 1\. Forståelse av Multi-Agent Systemer

En AI-agent er et system som går utover kapasiteten til en standard Large Language Model (LLM). Den kan oppfatte sitt miljø, ta beslutninger og utføre handlinger for å oppnå spesifikke mål. Et multi-agent system involverer flere slike agenter som samarbeider for å løse et problem som ville vært vanskelig eller umulig for en enkelt agent å håndtere alene.

### Vanlige Bruksområder

  * **Løsning av komplekse problemer**: Dele opp en stor oppgave (f.eks. planlegging av et firmaarrangement) i mindre deloppgaver som håndteres av spesialiserte agenter (f.eks. en budsjettagent, en logistikkagent, en markedsføringsagent).
  * **Virtuelle assistenter**: En primær assistentagent som delegerer oppgaver som planlegging, forskning og bestilling til andre spesialiserte agenter.
  * **Automatisert innholdsskaping**: En workflow hvor én agent utarbeider innhold, en annen gjennomgår det for nøyaktighet og tone, og en tredje publiserer det.

### Multi-Agent Mønstre

Multi-agent systemer kan organiseres i flere mønstre som bestemmer hvordan de interagerer:

  * **Sekvensiell**: Agenter arbeider i en forhåndsdefinert rekkefølge, som på en samlebånd. Utdata fra én agent blir inngangsdata for den neste.
  * **Samtidig**: Agenter arbeider parallelt med ulike deler av en oppgave, og resultatene deres samles til slutt.
  * **Betinget**: Workflow følger ulike veier basert på utdata fra en agent, lik en if-then-else-logikk.

## 2\. Microsoft Agent Framework Workflow Arkitektur

Agent Frameworks workflow-system er en avansert orkestreringsmotor designet for å håndtere komplekse interaksjoner mellom flere agenter. Det er bygget på en grafbasert arkitektur som bruker en [Pregel-stil utførelsesmodell](https://kowshik.github.io/JPregel/pregel_paper.pdf), hvor prosessering skjer i synkroniserte steg kalt "supersteps."

### Kjernekomponenter

Arkitekturen består av tre hoveddeler:

1.  **Executors**: Dette er de grunnleggende prosesseringsenhetene. I våre eksempler er en `Agent` en type executor. Hver executor kan ha flere meldingshåndterere som automatisk aktiveres basert på typen melding som mottas.
2.  **Edges**: Disse definerer banen som meldinger tar mellom executors. Edges kan ha betingelser, som tillater dynamisk ruting av informasjon gjennom workflow-grafen.
3.  **Workflow**: Denne komponenten orkestrerer hele prosessen, administrerer executors, edges og den overordnede flyten av utførelse. Den sørger for at meldinger behandles i riktig rekkefølge og strømmer hendelser for observasjon.

*Et diagram som illustrerer kjernekomponentene i workflow-systemet.*

Denne strukturen gjør det mulig å bygge robuste og skalerbare applikasjoner ved bruk av grunnleggende mønstre som sekvensielle kjeder, fan-out/fan-in for parallell prosessering, og switch-case logikk for betingede flyter.

## 3\. Praktiske Eksempler og Kodeanalyse

La oss nå utforske hvordan man implementerer ulike workflow-mønstre ved bruk av rammeverket. Vi skal se på både Python- og .NET-kode for hvert eksempel.

### Case 1: Grunnleggende Sekvensiell Workflow

Dette er det enkleste mønsteret, hvor én agents utdata sendes direkte til en annen. Vårt scenario involverer en hotell-`FrontDesk` agent som gir en reiseanbefaling, som deretter vurderes av en `Concierge` agent.

*Diagram av den grunnleggende FrontDesk -\> Concierge workflow.*

#### Scenario Bakgrunn

En reisende ber om en anbefaling i Paris.

1.  `FrontDesk`-agenten, designet for kortfattethet, foreslår et besøk til Louvre-museet.
2.  `Concierge`-agenten, som prioriterer autentiske opplevelser, mottar dette forslaget. Den vurderer anbefalingen og gir tilbakemelding, med et forslag til et mer lokalt, mindre turistpreget alternativ.

#### Python Implementering Analyse

I Python-eksemplet definerer og oppretter vi først de to agentene, hver med spesifikke instruksjoner.

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

Deretter brukes `WorkflowBuilder` til å konstruere grafen. `front_desk_agent` settes som startpunkt, og en edge opprettes for å koble dens utdata til `reviewer_agent`.

```python
# 01.python-agent-framework-workflow-ghmodel-basic.ipynb

workflow = WorkflowBuilder().set_start_executor(front_desk_agent).add_edge(front_desk_agent, reviewer_agent).build()
```

Til slutt utføres workflow med den innledende brukerforespørselen.

```python
# 01.python-agent-framework-workflow-ghmodel-basic.ipynb

result =''
# The run_stream method executes the workflow and streams events.
async for event in workflow.run_stream('I would like to go to Paris.'):
    if isinstance(event, WorkflowEvent):
        result += str(event.data)
```

#### .NET (C\#) Implementering Analyse

.NET-implementeringen følger en veldig lik logikk. Først defineres konstanter for agentenes navn og instruksjoner.

```csharp
// 01.dotnet-agent-framework-workflow-ghmodel-basic.ipynb

const string ReviewerAgentName = "Concierge";
const string ReviewerAgentInstructions = @"
    You are an are hotel concierge who has opinions about providing the most local and authentic experiences for travelers...";

const string FrontDeskAgentName = "FrontDesk";
const string FrontDeskAgentInstructions = @"""
    You are a Front Desk Travel Agent with ten years of experience and are known for brevity...";
```

Agentene opprettes ved bruk av en `OpenAIClient`, og deretter definerer `WorkflowBuilder` den sekvensielle flyten ved å legge til en edge fra `frontDeskAgent` til `reviewerAgent`.

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

Workflow kjøres deretter med brukerens melding, og resultatene strømmes tilbake.

### Case 2: Multi-Step Sekvensiell Workflow

Dette mønsteret utvider den grunnleggende sekvensen til å inkludere flere agenter. Det er ideelt for prosesser som krever flere stadier av raffinering eller transformasjon.

#### Scenario Bakgrunn

En bruker gir et bilde av en stue og ber om et møbeltilbud.

1.  **Sales-Agent**: Identifiserer møbelartiklene i bildet og lager en liste.
2.  **Price-Agent**: Tar listen over artikler og gir en detaljert prisoversikt, inkludert budsjett-, mellomklasse- og premiumalternativer.
3.  **Quote-Agent**: Mottar den prissatte listen og formaterer den til et formelt tilbudsdokument i Markdown.

*Diagram av Sales -\> Price -\> Quote workflow.*

#### Python Implementering Analyse

Tre agenter defineres, hver med en spesialisert rolle. Workflow konstrueres ved bruk av `add_edge` for å lage en kjede: `sales_agent` -\> `price_agent` -\> `quote_agent`.

```python
# 02.python-agent-framework-workflow-ghmodel-sequential.ipynb

# Create three specialized agents
sales_agent = chat_client.create_agent(...)
price_agent = chat_client.create_agent(...)
quote_agent = chat_client.create_agent(...)

# Build the sequential workflow
workflow = WorkflowBuilder().set_start_executor(sales_agent).add_edge(sales_agent, price_agent).add_edge(price_agent, quote_agent).build()
```

Inndata er en `ChatMessage` som inkluderer både tekst og bilde-URI. Rammeverket håndterer overføringen av utdata fra hver agent til den neste i sekvensen til det endelige tilbudet er generert.

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

#### .NET (C\#) Implementering Analyse

.NET-eksemplet speiler Python-versjonen. Tre agenter (`salesagent`, `priceagent`, `quoteagent`) opprettes. `WorkflowBuilder` kobler dem sekvensielt.

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

Brukerens melding konstrueres med både bildedata (som bytes) og tekstprompt. `InProcessExecution.StreamAsync`-metoden initierer workflow, og sluttresultatet fanges opp fra strømmen.

### Case 3: Samtidig Workflow

Dette mønsteret brukes når oppgaver kan utføres samtidig for å spare tid. Det involverer en "fan-out" til flere agenter og en "fan-in" for å samle resultatene.

#### Scenario Bakgrunn

En bruker ber om å planlegge en tur til Seattle.

1.  **Dispatcher (Fan-Out)**: Brukerens forespørsel sendes til to agenter samtidig.
2.  **Researcher-Agent**: Undersøker attraksjoner, vær og viktige hensyn for en tur til Seattle i desember.
3.  **Plan-Agent**: Lager uavhengig en detaljert dag-for-dag reiseplan.
4.  **Aggregator (Fan-In)**: Utdataene fra både forskeren og planleggeren samles og presenteres sammen som sluttresultatet.

*Diagram av den samtidige Researcher og Planner workflow.*

#### Python Implementering Analyse

`ConcurrentBuilder` forenkler opprettelsen av dette mønsteret. Du lister bare opp de deltakende agentene, og builderen oppretter automatisk nødvendig fan-out og fan-in logikk.

```python
# 03.python-agent-framework-workflow-ghmodel-concurrent.ipynb

research_agent = chat_client.create_agent(name="Researcher-Agent", ...)
plan_agent = chat_client.create_agent(name="Plan-Agent", ...)

# ConcurrentBuilder handles the fan-out/fan-in logic
workflow = ConcurrentBuilder().participants([research_agent, plan_agent]).build()

# Run the workflow
events = await workflow.run("Plan a trip to Seattle in December")
```

Rammeverket sørger for at `research_agent` og `plan_agent` utføres parallelt, og deres endelige utdata samles i en liste.

#### .NET (C\#) Implementering Analyse

I .NET krever dette mønsteret en mer eksplisitt definisjon. Egendefinerte executors (`ConcurrentStartExecutor` og `ConcurrentAggregationExecutor`) opprettes for å håndtere fan-out og fan-in logikk.

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

`WorkflowBuilder` bruker deretter `AddFanOutEdge` og `AddFanInEdge` for å konstruere grafen med disse egendefinerte executors og agentene.

```csharp
// 03.dotnet-agent-framework-workflow-ghmodel-concurrent.ipynb

var workflow = new WorkflowBuilder(startExecutor)
            .AddFanOutEdge(startExecutor, targets: [researcherAgent, plannerAgent])
            .AddFanInEdge(aggregationExecutor, sources: [researcherAgent, plannerAgent])
            .WithOutputFrom(aggregationExecutor)
            .Build();
```

### Case 4: Betinget Workflow

Betingede workflows introduserer forgrenet logikk, som lar systemet ta ulike veier basert på mellomresultater.

#### Scenario Bakgrunn

Denne workflow automatiserer opprettelsen og publiseringen av en teknisk veiledning.

1.  **Evangelist-Agent**: Skriver et utkast til veiledningen basert på en gitt disposisjon og URL-er.
2.  **ContentReviewer-Agent**: Gjennomgår utkastet. Den sjekker om ordantallet er over 200 ord.
3.  **Betinget Forgrening**:
      * **Hvis Godkjent (`Yes`)**: Workflow fortsetter til `Publisher-Agent`.
      * **Hvis Avvist (`No`)**: Workflow stopper og gir ut årsaken til avvisning.
4.  **Publisher-Agent**: Hvis utkastet er godkjent, lagrer denne agenten innholdet til en Markdown-fil.

#### Python Implementering Analyse

Dette eksemplet bruker en egendefinert funksjon, `select_targets`, for å implementere den betingede logikken. Denne funksjonen sendes til `add_multi_selection_edge_group` og styrer workflow basert på `review_result`-feltet fra anmelderens utdata.

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

Egendefinerte executors som `to_reviewer_result` brukes til å analysere JSON-utdata fra agentene og konvertere dem til sterkt typede objekter som utvalgsfunksjonen kan inspisere.

#### .NET (C\#) Implementering Analyse

.NET-versjonen bruker en lignende tilnærming med en betingelsesfunksjon. En `Func<object?, bool>` defineres for å sjekke `Result`-egenskapen til `ReviewResult`-objektet.

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

`AddEdge`-metodens `condition`-parameter lar `WorkflowBuilder` opprette en forgrenet vei. Workflow vil kun følge kanten til `publishExecutor` hvis betingelsen `GetCondition(expectedResult: "Yes")` returnerer true. Ellers følger den veien til `sendReviewerExecutor`.

## Konklusjon

Microsoft Agent Framework Workflow gir et robust og fleksibelt grunnlag for orkestrering av komplekse, multi-agent systemer. Ved å utnytte dens grafbaserte arkitektur og kjernekomponenter kan utviklere designe og implementere sofistikerte workflows i både Python og .NET. Enten applikasjonen din krever enkel sekvensiell prosessering, parallell utførelse eller dynamisk betinget logikk, tilbyr rammeverket verktøyene for å bygge kraftige, skalerbare og type-sikre AI-drevne løsninger.

---

**Ansvarsfraskrivelse**:  
Dette dokumentet er oversatt ved hjelp av AI-oversettelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selv om vi tilstreber nøyaktighet, vær oppmerksom på at automatiserte oversettelser kan inneholde feil eller unøyaktigheter. Det originale dokumentet på sitt opprinnelige språk bør anses som den autoritative kilden. For kritisk informasjon anbefales profesjonell menneskelig oversettelse. Vi er ikke ansvarlige for misforståelser eller feiltolkninger som oppstår ved bruk av denne oversettelsen.