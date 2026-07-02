# Udforskning af Microsoft Agent Framework

![Agent Framework](../../../translated_images/da/lesson-14-thumbnail.90df0065b9d234ee.webp)

### Introduktion

Denne lektion vil dække:

- Forståelse af Microsoft Agent Framework: Nøglefunktioner og værdi  
- Udforskning af de centrale begreber i Microsoft Agent Framework
- Avancerede MAF-mønstre: Arbejdsgange, middleware og hukommelse

## Læringsmål

Efter at have gennemført denne lektion vil du kunne:

- Bygge produktionsklare AI-agenter ved hjælp af Microsoft Agent Framework
- Anvende de centrale funktioner i Microsoft Agent Framework på dine agentiske brugssager
- Bruge avancerede mønstre herunder arbejdsgange, middleware og observerbarhed

## Kodeeksempler

Kodeeksempler for [Microsoft Agent Framework (MAF)](https://aka.ms/ai-agents-beginners/agent-framework) findes i dette repository under filerne `xx-python-agent-framework` og `xx-dotnet-agent-framework`.

## Forståelse af Microsoft Agent Framework

![Framework Intro](../../../translated_images/da/framework-intro.077af16617cf130c.webp)

[Microsoft Agent Framework (MAF)](https://aka.ms/ai-agents-beginners/agent-framework) er Microsofts samlede rammeværk til at bygge AI-agenter. Det tilbyder fleksibiliteten til at adressere den brede variation af agentiske brugssager, der ses i både produktions- og forskningsmiljøer, herunder:

- **Sekventiel agentorkestrering** i scenarier hvor trin-for-trin arbejdsgange er nødvendige.
- **Samtidig orkestrering** i scenarier hvor agenter skal udføre opgaver samtidigt.
- **Gruppechat-orkestrering** i scenarier hvor agenter kan samarbejde om én opgave.
- **Overdragelses-orkestrering** i scenarier hvor agenter overdrager opgaven til hinanden, efterhånden som delopgaver bliver udført.
- **Magnetisk orkestrering** i scenarier hvor en lederagent opretter og ændrer en opgaveliste og håndterer koordineringen af underagenter for at fuldføre opgaven.

For at levere AI-agenter i produktion har MAF også inkluderet funktioner til:

- **Observerbarhed** gennem brug af OpenTelemetry, hvor hver handling fra AI-agenten inklusive værktøjsopkald, orkestreringstrin, ræsonnementflows og ydelsesovervågning via Microsoft Foundry dashboards.
- **Sikkerhed** ved at hoste agenter indbygget i Microsoft Foundry, som inkluderer sikkerhedskontroller som rollebaseret adgang, håndtering af private data og indbygget indholdssikkerhed.
- **Holdbarhed** da agenttråde og arbejdsgange kan pause, genoptage og komme sig efter fejl, hvilket muliggør længerevarende processer.
- **Kontrol** da menneskelig inddragelse i arbejdsgange understøttes, hvor opgaver markeres som krævende menneskelig godkendelse.

Microsoft Agent Framework fokuserer også på interoperabilitet ved:

- **At være cloud-agnostisk** - Agenter kan køre i containere, lokalt og på tværs af flere forskellige clouds.
- **At være leverandør-agnostisk** - Agenter kan oprettes via dit foretrukne SDK, inklusiv Azure OpenAI og OpenAI
- **Integration af åbne standarder** - Agenter kan anvende protokoller såsom Agent-to-Agent (A2A) og Model Context Protocol (MCP) til at finde og bruge andre agenter og værktøjer.
- **Plugins og connectorer** - Der kan oprettes forbindelser til data- og hukommelsestjenester som Microsoft Fabric, SharePoint, Pinecone og Qdrant.

Lad os se på, hvordan disse funktioner anvendes på nogle af Microsoft Agent Frameworks centrale begreber.

## Centrale Begreber i Microsoft Agent Framework

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

OpenAI `Responses`, `ChatCompletion` API'er

```python
agent = OpenAIResponsesClient().create_agent( name="WeatherBot", instructions="You are a helpful weather assistant.", )
```

```python
agent = OpenAIChatClient().create_agent( name="HelpfulAssistant", instructions="You are a helpful assistant.", )
```

eller [MiniMax](https://platform.minimaxi.com/), som tilbyder en OpenAI-kompatibel API med store kontekstvinduer (op til 204K tokens):

```python
agent = OpenAIChatClient(base_url="https://api.minimax.io/v1", api_key=os.environ["MINIMAX_API_KEY"], model_id="MiniMax-M3").create_agent( name="HelpfulAssistant", instructions="You are a helpful assistant.", )
```

eller fjernagenter via A2A-protokollen:

```python
agent = A2AAgent( name=agent_card.name, description=agent_card.description, agent_card=agent_card, url="https://your-a2a-agent-host" )
```

**Kørsel af agenter**

Agenter køres ved hjælp af `.run` eller `.run_stream` metoderne for enten ikke-streaming eller streaming svar.

```python
result = await agent.run("What are good places to visit in Amsterdam?")
print(result.text)
```

```python
async for update in agent.run_stream("What are the good places to visit in Amsterdam?"):
    if update.text:
        print(update.text, end="", flush=True)

```

Hver agentkørsel kan også have muligheder for at tilpasse parametre såsom `max_tokens` brugt af agenten, `tools` som agenten kan kalde, og endda selve `modellen`, der bruges til agenten.

Dette er nyttigt i tilfælde hvor specifikke modeller eller værktøjer er nødvendige for at fuldføre en brugers opgave.

**Værktøjer**

Værktøjer kan defineres både når agenten defineres:

```python
def get_attractions( location: Annotated[str, Field(description="The location to get the top tourist attractions for")], ) -> str: """Get the top tourist attractions for a given location.""" return f"The top attractions for {location} are." 


# Når man opretter en ChatAgent direkte

agent = ChatAgent( chat_client=OpenAIChatClient(), instructions="You are a helpful assistant", tools=[get_attractions]

```

og også når agenten køres:

```python

result1 = await agent.run( "What's the best place to visit in Seattle?", tools=[get_attractions] # Værktøj leveret kun til denne kørsel )
```

**Agenttråde**

Agenttråde bruges til at håndtere samtaler med flere runder. Tråde kan oprettes enten ved:

- At bruge `get_new_thread()`, som gør det muligt at gemme tråden over tid
- Automatisk at oprette en tråd når en agent køres og kun lade tråden vare under den aktuelle kørsel.

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

# Serialiser tråden til lagring.

serialized_thread = await thread.serialize() 

# Deserialiser trådens tilstand efter indlæsning fra lagring.

resumed_thread = await agent.deserialize_thread(serialized_thread)
```

**Agent Middleware**

Agenter interagerer med værktøjer og LLM'er for at fuldføre brugerens opgaver. I visse scenarier ønsker vi at udføre eller spore handlinger imellem disse interaktioner. Agent middleware muliggør dette ved:

*Funktionsmiddleware*

Denne middleware giver mulighed for at udføre en handling mellem agenten og en funktion/værktøj, som agenten kalder. Et eksempel på brug er, hvis man ønsker at logge funktionskaldet.

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

*Chat Middleware*

Denne middleware giver mulighed for at udføre eller logge en handling mellem agenten og forespørgslerne til LLM.

Dette indeholder vigtig information såsom de `beskeder` som sendes til AI-servicen.

```python
async def logging_chat_middleware(
    context: ChatContext,
    next: Callable[[ChatContext], Awaitable[None]],
) -> None:
    """Chat middleware that logs AI interactions."""
    # Forbehandling: Log før AI-kald
    print(f"[Chat] Sending {len(context.messages)} messages to AI")

    # Fortsæt til næste middleware eller AI-service
    await next(context)

    # Efterbehandling: Log efter AI-svar
    print("[Chat] AI response received")

```

**Agent Hukommelse**

Som dækket i lektionen `Agentic Memory` er hukommelse et vigtigt element for at muliggøre agenten at operere over forskellige kontekster. MAF tilbyder flere forskellige typer hukommelser:

*Hukommelse i hukommelsen (In-Memory Storage)*

Dette er hukommelsen, som lagres i tråde under applikationskørslen.

```python
# Opret en ny tråd.
thread = agent.get_new_thread() # Kør agenten med tråden.
response = await agent.run("Hello, I am here to help you book travel. Where would you like to go?", thread=thread)
```

*Vedvarende beskeder*

Denne hukommelse bruges til at lagre samtalehistorik på tværs af forskellige sessioner. Den defineres ved hjælp af `chat_message_store_factory`:

```python
from agent_framework import ChatMessageStore

# Opret en brugerdefineret beskedlager
def create_message_store():
    return ChatMessageStore()

agent = ChatAgent(
    chat_client=OpenAIChatClient(),
    instructions="You are a Travel assistant.",
    chat_message_store_factory=create_message_store
)

```

*Dynamisk hukommelse*

Denne hukommelse tilføjes til konteksten før agenter køres. Disse hukommelser kan gemmes i eksterne tjenester som mem0:

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

**Agent Observerbarhed**

Observerbarhed er vigtigt for at bygge pålidelige og vedligeholdelsesvenlige agentiske systemer. MAF integrerer med OpenTelemetry for at give tracing og måleinstrumenter for bedre observerbarhed.

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

### Arbejdsgange

MAF tilbyder arbejdsgange som er foruddefinerede trin for at fuldføre en opgave og inkluderer AI-agenter som komponenter i disse trin.

Arbejdsgange består af forskellige komponenter der muliggør bedre kontrolflow. Arbejdsgange muliggør også **multi-agent orkestrering** og **checkpointing** for at gemme arbejdsgangstilstande.

Hovedkomponenterne i en arbejdsgang er:

**Executorer**

Executorer modtager inputbeskeder, udfører deres tildelte opgaver og producerer derefter en outputbesked. Dette driver arbejdsgangen frem mod at fuldføre den større opgave. Executorer kan være enten AI-agent eller kundetilpasset logik.

**Kanter**

Kanterne bruges til at definere flowet af beskeder i en arbejdsgang. Disse kan være:

*Direkte kanter* - Enkle en-til-en forbindelser mellem executorer:

```python
from agent_framework import WorkflowBuilder

builder = WorkflowBuilder()
builder.add_edge(source_executor, target_executor)
builder.set_start_executor(source_executor)
workflow = builder.build()
```

*Betingede kanter* - Aktiveres efter en bestemt betingelse er opfyldt. For eksempel, når hotelværelser ikke er tilgængelige, kan en executor foreslå andre muligheder.

*Switch-case kanter* - Leder beskeder til forskellige executorer baseret på definerede betingelser. For eksempel, hvis en rejsekunde har prioriteret adgang, og deres opgaver bliver håndteret via en anden arbejdsgang.

*Fan-out kanter* - Sender en besked til flere mål.

*Fan-in kanter* - Samler flere beskeder fra forskellige executorer og sender til ét mål.

**Begivenheder**

For at give bedre observerbarhed i arbejdsgange tilbyder MAF indbyggede begivenheder for eksekvering, herunder:

- `WorkflowStartedEvent`  - Arbejdsgangseksekvering begynder
- `WorkflowOutputEvent` - Arbejdsgang producerer output
- `WorkflowErrorEvent` - Arbejdsgang støder på en fejl
- `ExecutorInvokeEvent`  - Executor begynder behandling
- `ExecutorCompleteEvent`  -  Executor afslutter behandling
- `RequestInfoEvent` - En forespørgsel udstedes

## Avancerede MAF-mønstre

Sektionerne ovenfor dækker de centrale begreber i Microsoft Agent Framework. Som du opbygger mere komplekse agenter, er her nogle avancerede mønstre at overveje:

- **Middlewarekomposition**: Kæd flere middlewarehåndterere (logning, autentificering, ratenedbringelse) ved hjælp af funktions- og chatmiddleware for finstyret kontrol over agenters adfærd.
- **Arbejdsgang-checkpointing**: Brug arbejdsgangs-begivenheder og serialisering til at gemme og genoptage langtidskørende agentprocesser.
- **Dynamisk værktøjsvalg**: Kombiner RAG over værktøjsbeskrivelser med MAF’s værktøjsregistrering for kun at præsentere relevante værktøjer pr. forespørgsel.
- **Multi-agent overdragelse**: Brug arbejdsgangskanter og betinget routing til at orkestrere overdragelser mellem specialiserede agenter.

## Kodeeksempler

Kodeeksempler for Microsoft Agent Framework findes i dette repository under filerne `xx-python-agent-framework` og `xx-dotnet-agent-framework`.

## Har du flere spørgsmål om Microsoft Agent Framework?

Deltag i [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D) for at møde andre elever, deltage i åbent kontortid og få svar på dine spørgsmål om AI-agenter.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfraskrivelse**:
Dette dokument er blevet oversat ved hjælp af AI-oversættelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selvom vi bestræber os på nøjagtighed, skal du være opmærksom på, at automatiserede oversættelser kan indeholde fejl eller unøjagtigheder. Det originale dokument på dets oprindelige sprog bør betragtes som den autoritative kilde. For kritisk information anbefales professionel menneskelig oversættelse. Vi påtager os intet ansvar for misforståelser eller fejltolkninger, der opstår som følge af brugen af denne oversættelse.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->