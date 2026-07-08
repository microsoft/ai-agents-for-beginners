# Bygge fleragentapplikasjoner med Microsoft Agent Framework Workflow

Denne veiledningen vil lede deg gjennom å forstå og bygge fleragentapplikasjoner ved hjelp av Microsoft Agent Framework. Vi vil utforske kjernebegrepene i fleragentsystemer, dykke inn i arkitekturen til rammeverkets Workflow-komponent, og gå gjennom praktiske eksempler i både Python og .NET for forskjellige arbeidsflytmønstre.

## 1\. Forstå fleragentsystemer

En AI-agent er et system som går utover kapabilitetene til en standard stor språkmodell (LLM). Den kan oppfatte sitt miljø, ta beslutninger og iverksette tiltak for å oppnå spesifikke mål. Et fleragentsystem involverer flere av disse agentene som samarbeider for å løse et problem som ville vært vanskelig eller umulig for en enkelt agent å håndtere alene.

### Vanlige bruksområder

  * **Kompleks problemløsning**: Bryte ned en stor oppgave (f.eks. planlegging av et bedriftsomfattende arrangement) i mindre deloppgaver håndtert av spesialiserte agenter (f.eks. en budsjettagent, en logistikkagent, en markedsføringsagent).
  * **Virtuelle assistenter**: En primær assistentagent som delegerer oppgaver som planlegging, forskning og booking til andre spesialiserte agenter.
  * **Automatisert innholdsskaping**: En arbeidsflyt der en agent utarbeider innhold, en annen vurderer det for nøyaktighet og tone, og en tredje publiserer det.

### Fleragentmønstre

Fleragentsystemer kan organiseres i flere mønstre, som bestemmer hvordan de interagerer:

  * **Sekvensiell**: Agenter arbeider i en forhåndsdefinert rekkefølge, som en samlebånd. Utdataene fra en agent blir inngangen for den neste.
  * **Samtidig**: Agenter jobber parallelt med forskjellige deler av en oppgave, og resultatene deres samles opp til slutt.
  * **Betinget**: Arbeidsflyten følger forskjellige stier basert på utdata fra en agent, lik en hvis-så-ellersetning.

## 2\. Microsoft Agent Framework Workflow-arkitektur

Agent Frameworks arbeidsflytsystem er en avansert orkestreringsmotor designet for å håndtere komplekse interaksjoner mellom flere agenter. Det er bygget på en graf-basert arkitektur som bruker en [Pregel-stil kjøremodell](https://kowshik.github.io/JPregel/pregel_paper.pdf), der prosessering skjer i synkroniserte steg kalt "supersteps."

### Kjernekomponenter

Arkitekturen består av tre hoveddeler:

1.  **Executorer**: Dette er de grunnleggende behandlingsenhetene. I våre eksempler er en `Agent` en type executor. Hver executor kan ha flere meldinghåndterere som automatisk kalles basert på typen melding som mottas.
2.  **Kanter (Edges)**: Disse definerer veien meldingene tar mellom executorene. Kanter kan ha betingelser, noe som tillater dynamisk ruting av informasjon gjennom arbeidsflytgrafen.
3.  **Workflow**: Denne komponenten orkestrerer hele prosessen, håndterer executorene, kantene og den generelle kjøringsflyten. Den sikrer at meldinger behandles i riktig rekkefølge og strømmer hendelser for observabilitet.

*Et diagram som illustrerer kjernekomponentene i arbeidsflytsystemet.*

Denne strukturen tillater bygging av robuste og skalerbare applikasjoner ved bruk av grunnleggende mønstre som sekvensielle kjeder, fan-out/fan-in for parallell behandling, og switch-case-logikk for betingede flyter.

## 3\. Praktiske eksempler og kodeanalyse

Nå skal vi utforske hvordan man kan implementere ulike arbeidsflytmønstre ved hjelp av rammeverket. Vi ser på både Python- og .NET-kode for hvert eksempel.

### Case 1: Grunnleggende sekvensiell arbeidsflyt

Dette er det enkleste mønsteret, hvor en agents utdata sendes direkte til en annen. Vårt scenario involverer en hotell-`FrontDesk`-agent som gir en reiseanbefaling, som deretter blir gjennomgått av en `Concierge`-agent.

*Diagram av den grunnleggende FrontDesk -> Concierge arbeidsflyten.*

#### Scenario Bakgrunn

En reisende ber om en anbefaling i Paris.

1.  `FrontDesk`-agenten, designet for korthet, foreslår å besøke Louvre-museet.
2.  `Concierge`-agenten, som prioriterer autentiske opplevelser, mottar denne anbefalingen. Den vurderer anbefalingen og gir tilbakemelding, og foreslår et mer lokalt og mindre turistpreget alternativ.

#### Analyse av Python-implementasjon

I Python-eksemplet definerer og oppretter vi først de to agentene, hver med spesifikke instruksjoner.

```python
# 01.python-agent-framework-workflow-ghmodel-basic.ipynb

# Definer agentroller og instruksjoner
REVIEWER_NAME = "Concierge"
REVIEWER_INSTRUCTIONS = """
    You are an are hotel concierge who has opinions about providing the most local and authentic experiences for travelers...
    """

FRONTDESK_NAME = "FrontDesk"
FRONTDESK_INSTRUCTIONS = """
    You are a Front Desk Travel Agent with ten years of experience and are known for brevity...
    """

# Opprett agentinstanser
reviewer_agent = chat_client.as_agent(
    instructions=(REVIEWER_INSTRUCTIONS),
    name=REVIEWER_NAME,
)

front_desk_agent = chat_client.as_agent(
    instructions=(FRONTDESK_INSTRUCTIONS),
    name=FRONTDESK_NAME,
)
```

Deretter brukes `WorkflowBuilder` til å konstruere grafen. `front_desk_agent` settes som startpunkt, og en kant opprettes for å koble utdataene til `reviewer_agent`.

```python
# 01.python-agent-framework-arbeidsflyt-ghmodel-grunnleggende.ipynb

workflow = WorkflowBuilder(start_executor=front_desk_agent).add_edge(front_desk_agent, reviewer_agent).build()
```

Til slutt kjøres arbeidsflyten med den opprinnelige brukerprompten.

```python
# 01.python-agent-framework-workflow-ghmodel-basic.ipynb

result =''
# run kjører arbeidsflyten; get_outputs() returnerer resultatet fra output-utføreren.
events = await workflow.run('I would like to go to Paris.')
outputs = events.get_outputs()
result = outputs[0].text if outputs else ''
```

#### Analyse av .NET (C\#) implementasjon

.NET-implementasjonen følger en svært lik logikk. Først defineres konstanter for agentenes navn og instruksjoner.

```csharp
// 01.dotnet-agent-framework-workflow-ghmodel-basic.ipynb

const string ReviewerAgentName = "Concierge";
const string ReviewerAgentInstructions = @"
    You are an are hotel concierge who has opinions about providing the most local and authentic experiences for travelers...";

const string FrontDeskAgentName = "FrontDesk";
const string FrontDeskAgentInstructions = @"""
    You are a Front Desk Travel Agent with ten years of experience and are known for brevity...";
```

Agentene opprettes ved hjelp av en `AzureOpenAIClient` (Responses API), og deretter definerer `WorkflowBuilder` den sekvensielle flyten ved å legge til en kant fra `frontDeskAgent` til `reviewerAgent`.

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

Arbeidsflyten kjøres så med brukerens melding, og resultatene strømmes tilbake.

### Case 2: Sekvensiell arbeidsflyt med flere steg

Dette mønsteret utvider grunnsekvensen til å inkludere flere agenter. Det er ideelt for prosesser som krever flere stadier med raffinering eller transformasjon.

#### Scenario Bakgrunn

En bruker gir et bilde av et stueområde og ber om et møbeltilbud.

1.  **Salgsagent**: Identifiserer møbelobjektene i bildet og lager en liste.
2.  **Prisagent**: Tar listen over objekter og gir en detaljert prisoversikt, inkludert budsjett-, mellomklasse- og premiumalternativer.
3.  **Tilbudsagent**: Mottar den prissatte listen og formaterer den til et formelt tilbudsdokument i Markdown.

*Diagram av Sales -> Price -> Quote arbeidsflyten.*

#### Analyse av Python-implementasjon

Tre agenter defineres, hver med en spesialisert rolle. Arbeidsflyten bygges ved hjelp av `add_edge` for å lage en kjede: `sales_agent` -> `price_agent` -> `quote_agent`.

```python
# 02.python-agent-framework-workflow-ghmodel-sequential.ipynb

# Opprett tre spesialiserte agenter
sales_agent = chat_client.as_agent(...)
price_agent = chat_client.as_agent(...)
quote_agent = chat_client.as_agent(...)

# Bygg den sekvensielle arbeidsflyten
workflow = WorkflowBuilder(start_executor=sales_agent).add_edge(sales_agent, price_agent).add_edge(price_agent, quote_agent).build()
```

Inndata er en `ChatMessage` som inkluderer både tekst og bilde-URI. Rammeverket håndterer overføring av utdata fra hver agent til den neste i sekvensen inntil det endelige tilbudet genereres.

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

#### Analyse av .NET (C\#) implementasjon

.NET-eksemplet speiler Python-versjonen. Tre agenter (`salesagent`, `priceagent`, `quoteagent`) opprettes. `WorkflowBuilder` lenker dem sekvensielt.

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

Brukerens melding konstrueres med både billedata (som bytes) og tekstprompt. `InProcessExecution.StreamAsync`-metoden starter arbeidsflyten, og det endelige resultatet hentes fra strømmen.

### Case 3: Samtidig arbeidsflyt

Dette mønsteret brukes når oppgaver kan utføres samtidig for å spare tid. Det innebærer en "fan-out" til flere agenter og en "fan-in" for å samle resultatene.

#### Scenario Bakgrunn

En bruker planlegger en tur til Seattle.

1.  **Dispatcher (Fan-Out)**: Brukerens forespørsel sendes til to agenter samtidig.
2.  **Researcher-Agent**: Undersøker attraksjoner, vær og viktige hensyn for en tur til Seattle i desember.
3.  **Plan-Agent**: Lager uavhengig en detaljert dag-for-dag reiserute.
4.  **Aggregator (Fan-In)**: Resultatene fra både researcheren og planleggeren samles og presenteres sammen som det endelige resultatet.

*Diagram av samtidig Researcher og Planner arbeidsflyt.*

#### Analyse av Python-implementasjon

`ConcurrentBuilder` forenkler opprettelsen av dette mønsteret. Du lister bare opp de deltagende agentene, og builderen lager automatisk den nødvendige fan-out og fan-in logikken.

```python
# 03.python-agent-framework-workflow-ghmodel-concurrent.ipynb

research_agent = chat_client.as_agent(name="Researcher-Agent", ...)
plan_agent = chat_client.as_agent(name="Plan-Agent", ...)

# ConcurrentBuilder håndterer fan-out/fan-in logikken
workflow = ConcurrentBuilder().participants([research_agent, plan_agent]).build()

# Kjør arbeidsflyten
events = await workflow.run("Plan a trip to Seattle in December")
```

Rammeverket sørger for at `research_agent` og `plan_agent` kjører parallelt, og at deres endelige resultater samles i en liste.

#### Analyse av .NET (C\#) implementasjon

I .NET krever dette mønsteret en mer eksplisitt definisjon. Egendefinerte executorere (`ConcurrentStartExecutor` og `ConcurrentAggregationExecutor`) opprettes for å håndtere fan-out og fan-in logikken.

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

`WorkflowBuilder` bruker deretter `AddFanOutEdge` og `AddFanInEdge` til å bygge grafen med disse egendefinerte executorene og agentene.

```csharp
// 03.dotnet-agent-framework-workflow-ghmodel-concurrent.ipynb

var workflow = new WorkflowBuilder(startExecutor)
            .AddFanOutEdge(startExecutor, targets: [researcherAgent, plannerAgent])
            .AddFanInEdge(aggregationExecutor, sources: [researcherAgent, plannerAgent])
            .WithOutputFrom(aggregationExecutor)
            .Build();
```

### Case 4: Betinget arbeidsflyt

Betingede arbeidsflyter introduserer forgrening, som gjør at systemet kan ta forskjellige veier basert på mellomresultater.

#### Scenario Bakgrunn

Denne arbeidsflyten automatiserer opprettelse og publisering av en teknisk veiledning.

1.  **Evangelist-Agent**: Skriver et utkast til veiledningen basert på en gitt disposisjon og URL-er.
2.  **ContentReviewer-Agent**: Gjennomgår utkastet. Sjekker om antall ord er over 200.
3.  **Betinget gren**:
      * **Hvis godkjent (`Ja`)**: Arbeidsflyten fortsetter til `Publisher-Agent`.
      * **Hvis avvist (`Nei`)**: Arbeidsflyten stopper og viser årsaken til avvisning.
4.  **Publisher-Agent**: Hvis utkastet er godkjent, lagrer denne agenten innholdet til en Markdown-fil.

#### Analyse av Python-implementasjon

Dette eksemplet bruker en tilpasset funksjon, `select_targets`, for å implementere betinget logikk. Denne funksjonen sendes til `add_multi_selection_edge_group` og styrer arbeidsflyten basert på `review_result`-feltet fra anmelderens utdata.

```python
# 04.python-agent-framework-workflow-aifoundry-condition.ipynb

# Denne funksjonen bestemmer neste steg basert på vurderingsresultatet
def select_targets(review: ReviewResult, target_ids: list[str]) -> list[str]:
    handle_review_id, save_draft_id = target_ids
    if review.review_result == "Yes":
        # Hvis godkjent, fortsett til 'save_draft'-utføreren
        return [save_draft_id]
    else:
        # Hvis avvist, fortsett til 'handle_review'-utføreren for å rapportere feil
        return [handle_review_id]

# Arbeidsflytbyggeren bruker valgfunksjonen for ruting
workflow = (
    WorkflowBuilder()
        .set_start_executor(evangelist_agent)
        .add_edge(evangelist_agent, reviewer_agent)
        .add_edge(reviewer_agent, to_reviewer_result)
        # Flere-valg-kanten implementerer betinget logikk
        .add_multi_selection_edge_group(
            to_reviewer_result,
            [handle_review, save_draft],
            selection_func=select_targets,
        )
        .add_edge(save_draft, publisher_agent)
        .build()
)
```

Tilpassede executorere som `to_reviewer_result` brukes til å analysere JSON-utdata fra agentene og konvertere det til sterkt typede objekter som valgfunksjonen kan inspisere.

#### Analyse av .NET (C\#) implementasjon

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

`AddEdge`-metodens `condition`-parameter gjør det mulig for `WorkflowBuilder` å lage en forgrenet sti. Arbeidsflyten følger bare kanten til `publishExecutor` hvis betingelsen `GetCondition(expectedResult: "Yes")` returnerer sant. Ellers følger den stien til `sendReviewerExecutor`.

## Konklusjon

Microsoft Agent Framework Workflow gir et robust og fleksibelt grunnlag for orkestrering av komplekse fleragentsystemer. Ved å utnytte den graf-baserte arkitekturen og kjernekomponentene kan utviklere designe og implementere sofistikerte arbeidsflyter i både Python og .NET. Enten applikasjonen din krever enkel sekvensiell behandling, parallell utføring eller dynamisk betinget logikk, tilbyr rammeverket verktøyene til å bygge kraftige, skalerbare og typesikre AI-drevne løsninger.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfraskrivelse**:
Dette dokumentet er oversatt ved hjelp av AI-oversettelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selv om vi streber etter nøyaktighet, vær oppmerksom på at automatiske oversettelser kan inneholde feil eller unøyaktigheter. Det opprinnelige dokumentet på originalspråket skal betraktes som den autoritative kilden. For kritisk informasjon anbefales profesjonell menneskelig oversettelse. Vi er ikke ansvarlige for eventuelle misforståelser eller feiltolkninger som oppstår ved bruk av denne oversettelsen.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->