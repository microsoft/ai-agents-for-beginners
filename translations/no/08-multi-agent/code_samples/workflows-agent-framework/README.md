# Bygge Multi-Agent Applikasjoner med Microsoft Agent Framework Workflow

Denne veiledningen vil lede deg gjennom forståelsen og byggingen av multi-agent applikasjoner ved bruk av Microsoft Agent Framework. Vi vil utforske kjernkonseptene for multi-agent systemer, dykke ned i arkitekturen til rammeverkets Workflow-komponent, og gå gjennom praktiske eksempler i både Python og .NET for ulike arbeidsflytmønstre.

## 1\. Forstå Multi-Agent Systemer

En AI-agent er et system som går utover kapabilitetene til en standard stor språkmodell (LLM). Den kan oppfatte sitt miljø, ta beslutninger og utføre handlinger for å oppnå spesifikke mål. Et multi-agent system involverer flere av disse agentene som samarbeider for å løse et problem som ville vært vanskelig eller umulig for en enkelt agent å håndtere alene.

### Vanlige Anvendelsesscenarier

  * **Kompleks Problemløsning**: Å bryte ned en stor oppgave (for eksempel planlegging av et selskapsomfattende arrangement) i mindre deloppgaver håndtert av spesialiserte agenter (for eksempel en budsjettagent, en logistikkagent, en markedsføringsagent).
  * **Virtuelle Assistenter**: En primær assistentagent som delegerer oppgaver som timeplanlegging, research og booking til andre spesialiserte agenter.
  * **Automatisert Innholdsproduksjon**: En arbeidsflyt hvor en agent utarbeider innhold, en annen gjennomgår det for nøyaktighet og tone, og en tredje publiserer det.

### Multi-Agent Mønstre

Multi-agent systemer kan organiseres i flere mønstre som bestemmer hvordan de samhandler:

  * **Sekvensiell**: Agenter jobber i en forhåndsdefinert rekkefølge, som en samlebåndsprosess. Utdata fra en agent blir inndata for neste.
  * **Parallell**: Agenter jobber samtidig på ulike deler av en oppgave, og resultatene samles opp til slutt.
  * **Betinget**: Arbeidsflyten følger ulike veier basert på utdata fra en agent, lik en if-then-else-setning.

## 2\. Microsoft Agent Framework Workflow Arkitektur

Agent Frameworks arbeidsflytsystem er en avansert orkestreringsmotor designet for å håndtere komplekse interaksjoner mellom flere agenter. Det er bygget på en grafbasert arkitektur som bruker en [Pregel-stil eksekveringsmodell](https://kowshik.github.io/JPregel/pregel_paper.pdf), hvor prosessering skjer i synkroniserte steg kalt "supersteps."

### Kjernekomponenter

Arkitekturen består av tre hoveddeler:

1.  **Executorer**: Disse er de fundamentale prosesseringsenhetene. I våre eksempler er en `Agent` en type executor. Hver executor kan ha flere meldingshåndterere som automatisk kalles opp basert på meldingstypen som mottas.
2.  **Edges**: Disse definerer hvilken vei meldinger tar mellom executorene. Edges kan ha betingelser som tillater dynamisk styring av informasjon gjennom arbeidsflytgrafen.
3.  **Workflow**: Denne komponenten orkestrerer hele prosessen, styrer executorene, edgene og den overordnede kjøringsflyten. Den sikrer at meldinger behandles i riktig rekkefølge og strømmer hendelser for observabilitet.

*Et diagram som illustrerer kjernekomponentene i arbeidsflytsystemet.*

Denne strukturen tillater bygging av robuste og skalerbare applikasjoner ved bruk av grunnleggende mønstre som sekvensielle kjeder, fan-out/fan-in for parallell prosessering, og switch-case-logikk for betingede flyter.

## 3\. Praktiske Eksempler og Kodeanalyse

Nå skal vi utforske hvordan man implementerer ulike arbeidsflytmønstre med rammeverket. Vi ser på både Python- og .NET-kode for hvert eksempel.

### Case 1: Enkel Sekvensiell Arbeidsflyt

Dette er det enkleste mønsteret, hvor utdata fra en agent sendes direkte til en annen. Scenariet vårt involverer en hotell-`FrontDesk`-agent som gir en reiseanbefaling, som deretter blir gjennomgått av en `Concierge`-agent.

*Diagram over den grunnleggende FrontDesk -> Concierge arbeidsflyten.*

#### Scenario Bakgrunn

En reisende ber om en anbefaling i Paris.

1.  `FrontDesk`-agenten, designet for kortfattethet, foreslår å besøke Louvre-museet.
2.  `Concierge`-agenten, som prioriterer autentiske opplevelser, mottar denne anbefalingen. Den gjennomgår anbefalingen og gir tilbakemelding, og foreslår et mer lokalt, mindre turistpreget alternativ.

#### Python Implementasjonsanalyse

I Python-eksemplet definerer og oppretter vi først de to agentene, hver med spesifikke instruksjoner.

```python
# 01.python-agent-framework-workflow-ghmodel-basic.ipynb

# Definer agentroller og instruksjoner
REVIEWER_NAME = "Concierge"
REVIEWER_INSTRUCTIONS = """
    You are a hotel concierge who has opinions about providing the most local and authentic experiences for travelers...
    """

FRONTDESK_NAME = "FrontDesk"
FRONTDESK_INSTRUCTIONS = """
    You are a Front Desk Travel Agent with ten years of experience and are known for brevity...
    """

# Opprett agentforekomster
reviewer_agent = chat_client.as_agent(
    instructions=(REVIEWER_INSTRUCTIONS),
    name=REVIEWER_NAME,
)

front_desk_agent = chat_client.as_agent(
    instructions=(FRONTDESK_INSTRUCTIONS),
    name=FRONTDESK_NAME,
)
```

Deretter brukes `WorkflowBuilder` for å bygge grafen. `front_desk_agent` settes som startpunkt, og en edge opprettes for å koble utdata fra denne til `reviewer_agent`.

```python
# 01.python-agent-framework-arbeidsflyt-ghmodel-grunnleggende.ipynb

workflow = WorkflowBuilder(start_executor=front_desk_agent).add_edge(front_desk_agent, reviewer_agent).build()
```

Til slutt kjøres arbeidsflyten med den initielle brukerprompten.

```python
# 01.python-agent-framework-workflow-ghmodel-basic.ipynb

result =''
# run kjører arbeidsflyten; get_outputs() returnerer resultatet fra utdatautføreren.
events = await workflow.run('I would like to go to Paris.')
outputs = events.get_outputs()
result = outputs[0].text if outputs else ''
```

#### .NET (C\#) Implementasjonsanalyse

.NET-implementasjonen følger en svært lik logikk. Først defineres konstanter for agentenes navn og instruksjoner.

```csharp
// 01.dotnet-agent-framework-workflow-ghmodel-basic.ipynb

const string ReviewerAgentName = "Concierge";
const string ReviewerAgentInstructions = @"
    You are a hotel concierge who has opinions about providing the most local and authentic experiences for travelers...";

const string FrontDeskAgentName = "FrontDesk";
const string FrontDeskAgentInstructions = @"""
    You are a Front Desk Travel Agent with ten years of experience and are known for brevity...";
```

Agentene opprettes med en `AzureOpenAIClient` (Responses API), og `WorkflowBuilder` definerer den sekvensielle flyten ved å legge til en edge fra `frontDeskAgent` til `reviewerAgent`.

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

Arbeidsflyten kjøres deretter med brukerens melding, og resultatene streames tilbake.

### Case 2: Sekvensiell Arbeidsflyt med Flere Steg

Dette mønsteret utvider den grunnleggende sekvensen til å inkludere flere agenter. Det er ideelt for prosesser som krever flere stadier av forbedring eller transformasjon.

#### Scenario Bakgrunn

En bruker sender inn et bilde av en stue og ber om et møbeltilbud.

1.  **Salgagent**: Identifiserer møblene i bildet og lager en liste.
2.  **Prisagent**: Tar listen over gjenstander og gir en detaljert prisoversikt, inkludert budsjett-, mellomklasse- og premiumalternativer.
3.  **Tilbudsagent**: Mottar prislisten og formaterer det til et formelt tilbudsdokument i Markdown.

*Diagram over Salg -> Pris -> Tilbud arbeidsflyten.*

#### Python Implementasjonsanalyse

Tre agenter defineres, hver med en spesialisert rolle. Arbeidsflyten bygges med `add_edge` for å skape en kjede: `sales_agent` -> `price_agent` -> `quote_agent`.

```python
# 02.python-agent-framework-workflow-ghmodel-sequential.ipynb

# Lag tre spesialiserte agenter
sales_agent = chat_client.as_agent(...)
price_agent = chat_client.as_agent(...)
quote_agent = chat_client.as_agent(...)

# Bygg den sekvensielle arbeidsflyten
workflow = WorkflowBuilder(start_executor=sales_agent).add_edge(sales_agent, price_agent).add_edge(price_agent, quote_agent).build()
```

Inngangen er en `ChatMessage` som inkluderer både tekst og bilde-URI. Rammeverket håndterer å sende utdata fra hver agent til den neste i sekvensen til det endelige tilbudet genereres.

```python
# 02.python-agent-framework-workflow-ghmodel-sequential.ipynb

# Brukermeldingen inneholder både tekst og et bilde
message = ChatMessage(
        role=Role.USER,
        contents=[
            TextContent(text="Please find the relevant furniture..."),
            DataContent(uri=image_uri, media_type="image/png")
        ]
)

# Kjør arbeidsflyten
events = await workflow.run(message)
```

#### .NET (C#) Implementasjonsanalyse

.NET-eksemplet speiler Python-versjonen. Tre agenter (`salesagent`, `priceagent`, `quoteagent`) opprettes. `WorkflowBuilder` kobler dem sekvensielt.

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

Brukerens melding bygges med både bildeinformasjon (som bytes) og tekstprompt. Metoden `InProcessExecution.RunStreamingAsync` starter arbeidsflyten, og det endelige resultatet hentes fra strømmen.

### Case 3: Parallell Arbeidsflyt

Dette mønsteret brukes når oppgaver kan utføres samtidig for å spare tid. Det involverer en "fan-out" til flere agenter og en "fan-in" for å samle resultatene.

#### Scenario Bakgrunn

En bruker ber om å planlegge en tur til Seattle.

1.  **Dispatcher (Fan-Out)**: Brukerens forespørsel sendes til to agenter samtidig.
2.  **Forsker-Agent**: Undersøker attraksjoner, vær og viktige hensyn for en tur til Seattle i desember.
3.  **Planlegger-Agent**: Lager uavhengig en detaljert dag-for-dag reiserute.
4.  **Aggregator (Fan-In)**: Resultatene fra både forskeren og planleggeren samles og presenteres samlet som sluttresultat.

*Diagram over den parallelle Forsker- og Planlegger-arbeidsflyten.*

#### Python Implementasjonsanalyse

`ConcurrentBuilder` forenkler opprettelsen av dette mønsteret. Du lister bare opp de deltakende agentene, og builderen lager automatisk nødvendig fan-out og fan-in-logikk.

```python
# 03.python-agent-framework-workflow-ghmodel-concurrent.ipynb

research_agent = chat_client.as_agent(name="Researcher-Agent", ...)
plan_agent = chat_client.as_agent(name="Plan-Agent", ...)

# ConcurrentBuilder håndterer fan-out/fan-in logikken
workflow = ConcurrentBuilder().participants([research_agent, plan_agent]).build()

# Kjør arbeidsflyten
events = await workflow.run("Plan a trip to Seattle in December")
```

Rammeverket sørger for at `research_agent` og `plan_agent` kjører parallelt, og deres endelige utdata samles i en liste.

#### .NET (C#) Implementasjonsanalyse

I .NET krever dette mønsteret en mer eksplisitt definisjon. Tilpassede executor’er (`ConcurrentStartExecutor` og `ConcurrentAggregationExecutor`) opprettes for å håndtere fan-out og fan-in logikk.

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

`WorkflowBuilder` bruker deretter `AddFanOutEdge` og `AddFanInEdge` for å bygge grafen med disse tilpassede executorene og agentene.

```csharp
// 03.dotnet-agent-framework-workflow-ghmodel-concurrent.ipynb

var workflow = new WorkflowBuilder(startExecutor)
            .AddFanOutEdge(startExecutor, targets: [researcherAgent, plannerAgent])
            .AddFanInEdge(aggregationExecutor, sources: [researcherAgent, plannerAgent])
            .WithOutputFrom(aggregationExecutor)
            .Build();
```

### Case 4: Betinget Arbeidsflyt

Betingede arbeidsflyter introduserer forgreningslogikk, som tillater systemet å ta ulike veier basert på mellomliggende resultater.

#### Scenario Bakgrunn

Denne arbeidsflyten automatiserer opprettelse og publisering av en teknisk veiledning.

1.  **Evangelist-Agent**: Skriver et utkast til veiledningen basert på en gitt disposisjon og URL-er.
2.  **ContentReviewer-Agent**: Gjennomgår utkastet. Sjekker om antall ord er over 200.
3.  **Betinget Gren**:
      * **Hvis godkjent (`Yes`)**: Arbeidsflyten fortsetter til `Publisher-Agent`.
      * **Hvis avvist (`No`)**: Arbeidsflyten stopper og gir grunnlaget for avvisningen.
4.  **Publisher-Agent**: Hvis utkastet er godkjent, lagrer denne agenten innholdet til en Markdown-fil.

#### Python Implementasjonsanalyse

Dette eksemplet bruker en egendefinert funksjon, `select_targets`, for å implementere den betingede logikken. Denne funksjonen gis til `add_multi_selection_edge_group` og styrer arbeidsflyten basert på feltet `review_result` fra anmelderens utdata.

```python
# 04.python-agent-framework-workflow-aifoundry-condition.ipynb

# Denne funksjonen bestemmer neste steg basert på gjennomgangsresultatet
def select_targets(review: ReviewResult, target_ids: list[str]) -> list[str]:
    handle_review_id, save_draft_id = target_ids
    if review.review_result == "Yes":
        # Hvis godkjent, fortsett til 'save_draft' utføreren
        return [save_draft_id]
    else:
        # Hvis avvist, fortsett til 'handle_review' utføreren for å rapportere feil
        return [handle_review_id]

# Arbeidsflytbyggeren bruker utvalgsfunksjonen for ruting
workflow = (
    WorkflowBuilder()
        .set_start_executor(evangelist_agent)
        .add_edge(evangelist_agent, reviewer_agent)
        .add_edge(reviewer_agent, to_reviewer_result)
        # Multi-utvalgskanten implementerer den betingede logikken
        .add_multi_selection_edge_group(
            to_reviewer_result,
            [handle_review, save_draft],
            selection_func=select_targets,
        )
        .add_edge(save_draft, publisher_agent)
        .build()
)
```

Tilpassede executor’er som `to_reviewer_result` brukes for å analysere JSON-utdata fra agentene og konvertere dem til sterkt typede objekter som valgfunksjonen kan inspisere.

#### .NET (C#) Implementasjonsanalyse

.NET-versjonen bruker en tilsvarende tilnærming med en betingelsesfunksjon. En `Func<object?, bool>` defineres for å sjekke `Result`-egenskapen til `ReviewResult`-objektet.

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

`AddEdge`-metodens `condition`-parameter tillater `WorkflowBuilder` å lage en forgreningsvei. Arbeidsflyten følger kun kanten til `publishExecutor` hvis betingelsen `GetCondition(expectedResult: "Yes")` returnerer true. Ellers følger den veien til `sendReviewerExecutor`.

## Konklusjon

Microsoft Agent Framework Workflow gir et robust og fleksibelt fundament for orkestrering av komplekse multi-agent systemer. Ved å utnytte dens grafbaserte arkitektur og kjernekomponenter kan utviklere designe og implementere sofistikerte arbeidsflyter i både Python og .NET. Enten applikasjonen din krever enkel sekvensiell prosessering, parallell eksekvering eller dynamisk betinget logikk, tilbyr rammeverket verktøyene for å bygge kraftige, skalerbare og typesikre AI-drevne løsninger.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfraskrivelse**:
Dette dokumentet er oversatt ved hjelp av AI-oversettelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selv om vi streber etter nøyaktighet, vær oppmerksom på at automatiske oversettelser kan inneholde feil eller unøyaktigheter. Det opprinnelige dokumentet på originalspråket skal betraktes som den autoritative kilden. For kritisk informasjon anbefales profesjonell menneskelig oversettelse. Vi er ikke ansvarlige for eventuelle misforståelser eller feiltolkninger som oppstår ved bruk av denne oversettelsen.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->