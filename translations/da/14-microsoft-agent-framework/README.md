# Udforskning af Microsoft Agent Framework

![Agent Framework](../../../translated_images/da/lesson-14-thumbnail.90df0065b9d234ee.webp)

### Introduktion

Denne lektion vil dække:

- Forståelse af Microsoft Agent Framework: Nøglefunktioner og værdi  
- Udforskning af nøglebegreberne i Microsoft Agent Framework
- Avancerede MAF-mønstre: Workflows, middleware og hukommelse

## Læringsmål

Efter at have gennemført denne lektion vil du kunne:

- Bygge produktionsklare AI-agenter ved hjælp af Microsoft Agent Framework
- Anvende de centrale funktioner i Microsoft Agent Framework til dine agentiske anvendelsestilfælde
- Bruge avancerede mønstre herunder workflows, middleware og observabilitet

## Kodeeksempler

Kodeeksempler til [Microsoft Agent Framework (MAF)](https://aka.ms/ai-agents-beginners/agent-framewrok) findes i dette repository under filer `xx-python-agent-framework` og `xx-dotnet-agent-framework`.

## Forståelse af Microsoft Agent Framework

![Framework Intro](../../../translated_images/da/framework-intro.077af16617cf130c.webp)

[Microsoft Agent Framework (MAF)](https://aka.ms/ai-agents-beginners/agent-framewrok) er Microsofts samlede framework til opbygning af AI-agenter. Det tilbyder fleksibilitet til at håndtere den brede vifte af agentiske anvendelsestilfælde, der ses både i produktion og forskningsmiljøer, herunder:

- **Sekventiel agentorkestrering** i scenarier, hvor trin-for-trin workflows er nødvendige.
- **Konkurrrende orkestrering** i scenarier, hvor agenter skal fuldføre opgaver samtidig.
- **Gruppechat-orkestrering** i scenarier, hvor agenter kan samarbejde om en opgave.
- **Overdragelsesorkestrering** i scenarier, hvor agenter videregiver opgaven til hinanden, efterhånden som delopgaver færdiggøres.
- **Magnetisk orkestrering** i scenarier, hvor en lederagent opretter og modificerer en opgaveliste og håndterer koordineringen af underagenter, der skal fuldføre opgaven.

For at levere AI-agenter i produktion har MAF også indbyggede funktioner til:

- **Observabilitet** gennem brug af OpenTelemetry, hvor hver handling af AI-agenten inklusive værktøjsopkald, orkestreringstrin, ræsonnementsforløb og ydelsesovervågning sker via Microsoft Foundry dashboards.
- **Sikkerhed** ved at hoste agenter native på Microsoft Foundry, som inkluderer sikkerhedskontroller som rollebaseret adgang, håndtering af private data og indbygget indholdssikkerhed.
- **Holdbarhed** da agent-tråde og workflows kan pause, genoptage og komme sig efter fejl, hvilket muliggør længerevarende processer.
- **Kontrol** da workflows med menneskelig indblanding understøttes, hvor opgaver markeres som krævende menneskelig godkendelse.

Microsoft Agent Framework fokuserer også på at være interoperabelt ved:

- **At være cloud-agnostisk** – agenter kan køre i containere, on-premises og på tværs af flere forskellige clouds.
- **At være leverandør-agnostisk** – agenter kan oprettes via dit foretrukne SDK, herunder Azure OpenAI og OpenAI.
- **Integration af åbne standarder** – agenter kan benytte protokoller som Agent-til-Agent (A2A) og Model Context Protocol (MCP) til at opdage og bruge andre agenter og værktøjer.
- **Plugins og connectors** – forbindelser kan laves til data- og hukommelsestjenester som Microsoft Fabric, SharePoint, Pinecone og Qdrant.

Lad os se på, hvordan disse funktioner anvendes i nogle af de centrale begreber i Microsoft Agent Framework.

## Nøglebegreber i Microsoft Agent Framework

### Agenter

![Agent Framework](../../../translated_images/da/agent-components.410a06daf87b4fef.webp)

**Oprettelse af agenter**

Agentoprettelse sker ved at definere inferencetjenesten (LLM-udbyder), et sæt instruktioner for AI-agenten at følge, og et tildelt `name`:

```python
agent = AzureOpenAIChatClient(credential=AzureCliCredential()).create_agent( instructions="You are good at recommending trips to customers based on their preferences.", name="TripRecommender" )
```

Ovenstående bruger `Azure OpenAI`, men agenter kan oprettes ved hjælp af en række tjenester, herunder `Microsoft Foundry Agent Service`:

```python
AzureAIAgentClient(async_credential=credential).create_agent( name="HelperAgent", instructions="You are a helpful assistant." ) as agent
```

OpenAI `Responses`, `ChatCompletion` API’er

```python
agent = OpenAIResponsesClient().create_agent( name="WeatherBot", instructions="You are a helpful weather assistant.", )
```

```python
agent = OpenAIChatClient().create_agent( name="HelpfulAssistant", instructions="You are a helpful assistant.", )
```

eller fjernagenter ved brug af A2A-protokollen:

```python
agent = A2AAgent( name=agent_card.name, description=agent_card.description, agent_card=agent_card, url="https://your-a2a-agent-host" )
```

**Kørselsagenter**

Agenter køres ved hjælp af metoderne `.run` eller `.run_stream` for enten ikke-streaming eller streaming svar.

```python
result = await agent.run("What are good places to visit in Amsterdam?")
print(result.text)
```

```python
async for update in agent.run_stream("What are the good places to visit in Amsterdam?"):
    if update.text:
        print(update.text, end="", flush=True)

```

Hver agentkørsel kan også have muligheder for at tilpasse parametre som `max_tokens` anvendt af agenten, `tools` som agenten kan kalde, og endda den `model`, der bruges til agenten.

Dette er nyttigt i tilfælde, hvor specifikke modeller eller værktøjer kræves for at fuldføre en brugers opgave.

**Værktøjer**

Værktøjer kan defineres både ved agentdefinitionen:

```python
def get_attractions( location: Annotated[str, Field(description="The location to get the top tourist attractions for")], ) -> str: """Get the top tourist attractions for a given location.""" return f"The top attractions for {location} are." 


# Når du opretter en ChatAgent direkte

agent = ChatAgent( chat_client=OpenAIChatClient(), instructions="You are a helpful assistant", tools=[get_attractions]

```

og også når agenten køres:

```python

result1 = await agent.run( "What's the best place to visit in Seattle?", tools=[get_attractions] # Værktøj leveret kun til denne kørsel )
```

**Agent-tråde**

Agent-tråde anvendes til at håndtere samtaler med flere omgange. Tråde kan oprettes enten ved:

- At bruge `get_new_thread()`, som muliggør, at tråden kan gemmes over tid
- Automatisk at oprette en tråd, når agenten køres, hvor tråden kun varer under den aktuelle kørsel.

For at oprette en tråd ser koden således ud:

```python
# Opret en ny tråd.
thread = agent.get_new_thread() # Kør agenten med tråden.
response = await agent.run("Hello, I am here to help you book travel. Where would you like to go?", thread=thread)

```

Du kan derefter serialisere tråden for at gemme den til senere brug:

```python
# Opret en ny tråd.
thread = agent.get_new_thread() 

# Kør agenten med tråden.

response = await agent.run("Hello, how are you?", thread=thread) 

# Serialiser tråden til opbevaring.

serialized_thread = await thread.serialize() 

# Deserialiser trådtilstanden efter indlæsning fra opbevaring.

resumed_thread = await agent.deserialize_thread(serialized_thread)
```

**Agent-middleware**

Agenter interagerer med værktøjer og LLM'er for at udføre brugerens opgaver. I visse scenarier ønsker vi at udføre eller spore handlinger imellem disse interaktioner. Agent-middleware muliggør dette igennem:

*Funktionsmiddleware*

Denne middleware giver os mulighed for at udføre en handling mellem agenten og en funktion/værktøj, som den vil kalde. Et eksempel på brug er, når man ønsker at logge opkaldet til funktionen.

I koden nedenfor definerer `next` om den næste middleware eller den faktiske funktion skal kaldes.

```python
async def logging_function_middleware(
    context: FunctionInvocationContext,
    next: Callable[[FunctionInvocationContext], Awaitable[None]],
) -> None:
    """Function middleware that logs function execution."""
    # Forbehandling: Log før funktionsudførelse
    print(f"[Function] Calling {context.function.name}")

    # Fortsæt til næste middleware eller funktionsudførelse
    await next(context)

    # Efterbehandling: Log efter funktionsudførelse
    print(f"[Function] {context.function.name} completed")
```

*Chatmiddleware*

Denne middleware giver os mulighed for at udføre eller logge en handling mellem agenten og forespørgsler til LLM'en.

Dette indeholder vigtig information som `messages`, der sendes til AI-tjenesten.

```python
async def logging_chat_middleware(
    context: ChatContext,
    next: Callable[[ChatContext], Awaitable[None]],
) -> None:
    """Chat middleware that logs AI interactions."""
    # Forbehandling: Log før AI-kald
    print(f"[Chat] Sending {len(context.messages)} messages to AI")

    # Fortsæt til næste middleware eller AI-tjeneste
    await next(context)

    # Efterbehandling: Log efter AI-svar
    print("[Chat] AI response received")

```

**Agent-hukommelse**

Som dækket i lektionen `Agentic Memory`, er hukommelse et vigtigt element til at gøre agenten i stand til at operere over forskellige kontekster. MAF tilbyder flere forskellige typer hukommelser:

*Hukommelse i tråden*

Dette er hukommelsen lagret i tråde under applikationskørsel.

```python
# Opret en ny tråd.
thread = agent.get_new_thread() # Kør agenten med tråden.
response = await agent.run("Hello, I am here to help you book travel. Where would you like to go?", thread=thread)
```

*Vedvarende beskeder*

Denne hukommelse anvendes til opbevaring af samtalehistorik på tværs af forskellige sessioner. Den defineres ved hjælp af `chat_message_store_factory`:

```python
from agent_framework import ChatMessageStore

# Opret en brugerdefineret meddelelseslager
def create_message_store():
    return ChatMessageStore()

agent = ChatAgent(
    chat_client=OpenAIChatClient(),
    instructions="You are a Travel assistant.",
    chat_message_store_factory=create_message_store
)

```

*Dynamisk hukommelse*

Denne hukommelse tilføjes til konteksten, før agenter køres. Disse hukommelser kan gemmes i eksterne tjenester som mem0:

```python
from agent_framework.mem0 import Mem0Provider

# Bruger Mem0 til avancerede hukommelsesfunktioner
memory_provider = Mem0Provider(
    api_key="your-mem0-api-key",
    user_id="user_123",
    application_id="my_app"
)

agent = ChatAgent(
    chat_client=OpenAIChatClient(),
    instructions="You are a helpful assistant with memory.",
    context_providers=memory_provider
)

```

**Agent-observabilitet**

Observabilitet er vigtigt for at opbygge pålidelige og vedligeholdbare agentiske systemer. MAF integrerer med OpenTelemetry for at levere tracing og målere til bedre observabilitet.

```python
from agent_framework.observability import get_tracer, get_meter

tracer = get_tracer()
meter = get_meter()
with tracer.start_as_current_span("my_custom_span"):
    # gør noget
    pass
counter = meter.create_counter("my_custom_counter")
counter.add(1, {"key": "value"})
```

### Workflows

MAF tilbyder workflows, som er foruddefinerede trin til at fuldføre en opgave, og som inkluderer AI-agenter som komponenter i disse trin.

Workflows består af forskellige komponenter, der tillader bedre kontrolflow. Workflows muliggør også **multi-agent orkestrering** og **checkpointing** for at gemme workflow-tilstande.

De centrale komponenter i en workflow er:

**Executorer**

Executorer modtager inputbeskeder, udfører deres tildelte opgaver og producerer derefter en outputbesked. Dette fører workflowet videre mod at færdiggøre den større opgave. Executorer kan være både AI-agent eller brugerdefineret logik.

**Edges**

Edges bruges til at definere beskedflow i en workflow. Disse kan være:

*Direkte Edges* – Enkle en-til-en forbindelser mellem executor:

```python
from agent_framework import WorkflowBuilder

builder = WorkflowBuilder()
builder.add_edge(source_executor, target_executor)
builder.set_start_executor(source_executor)
workflow = builder.build()
```

*Betingede Edges* – Aktiveres efter en bestemt betingelse er opfyldt. For eksempel, når hotelværelser ikke er tilgængelige, kan en executor foreslå andre muligheder.

*Switch-case Edges* – Rute beskeder til forskellige executor baseret på definerede betingelser. For eksempel hvis en rejsekunde har prioriteret adgang, og deres opgaver bliver håndteret gennem en anden workflow.

*Fan-out Edges* – Sender en besked til flere mål.

*Fan-in Edges* – Samler flere beskeder fra forskellige executor og sender til ét mål.

**Events**

For at give bedre observabilitet i workflows tilbyder MAF indbyggede events for eksekvering, herunder:

- `WorkflowStartedEvent`  - Workflow eksekvering begynder
- `WorkflowOutputEvent` - Workflow producerer en output
- `WorkflowErrorEvent` - Workflow støder på en fejl
- `ExecutorInvokeEvent`  - Executor starter behandling
- `ExecutorCompleteEvent`  -  Executor afslutter behandling
- `RequestInfoEvent` - En forespørgsel udsendes

## Avancerede MAF-mønstre

De ovenstående sektioner dækker de centrale begreber i Microsoft Agent Framework. Når du bygger mere komplekse agenter, er her nogle avancerede mønstre at overveje:

- **Middleware-sammensætning**: Kæd flere middleware-håndterere (logging, autentificering, hastighedsbegrænsning) ved hjælp af funktion- og chatmiddleware for finstyring af agentens opførsel.
- **Workflow Checkpointing**: Brug workflovevents og serialisering til at gemme og genoptage langvarige agentprocesser.
- **Dynamisk værktøjsvalg**: Kombiner RAG over værktøjsbeskrivelser med MAF’s værktøjsregistrering for kun at præsentere relevante værktøjer pr. forespørgsel.
- **Multi-agent Overdragelse**: Brug workflow-edges og betinget routing til at orkestrere overdragelser mellem specialiserede agenter.

## Kodeeksempler

Kodeeksempler til Microsoft Agent Framework findes i dette repository under filer `xx-python-agent-framework` og `xx-dotnet-agent-framework`.

## Har du flere spørgsmål om Microsoft Agent Framework?

Deltag i [Microsoft Foundry Discord](https://aka.ms/ai-agents/discord) for at møde andre lærende, deltage i kontortimer og få besvaret dine spørgsmål om AI-agenter.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfraskrivelse**:
Dette dokument er blevet oversat ved hjælp af AI-oversættelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selvom vi stræber efter nøjagtighed, bedes du være opmærksom på, at automatiserede oversættelser kan indeholde fejl eller unøjagtigheder. Det oprindelige dokument på dets modersmål bør betragtes som den autoritative kilde. For kritisk information anbefales professionel menneskelig oversættelse. Vi påtager os intet ansvar for eventuelle misforståelser eller fejltolkninger, der opstår ved brug af denne oversættelse.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->