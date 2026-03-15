# Utforske Microsoft Agent Framework

![Agent-rammeverk](../../../translated_images/no/lesson-14-thumbnail.90df0065b9d234ee.webp)

### Introduksjon

Denne leksjonen vil dekke:

- Forstå Microsoft Agent Framework: Nøkkelfunksjoner og verdi  
- Utforske kjernebegrepene i Microsoft Agent Framework
- Avanserte MAF-mønstre: Arbeidsflyter, mellomvare og minne

## Læringsmål

Etter å ha fullført denne leksjonen vil du vite hvordan du:

- Bygger produksjonsklare AI-agenter ved hjelp av Microsoft Agent Framework
- Anvender kjernefunksjonene i Microsoft Agent Framework på dine agentiske brukstilfeller
- Bruker avanserte mønstre inkludert arbeidsflyter, mellomvare og observabilitet

## Kodeeksempler 

Kodeeksempler for [Microsoft Agent Framework (MAF)](https://aka.ms/ai-agents-beginners/agent-framewrok) finnes i dette depotet under `xx-python-agent-framework` og `xx-dotnet-agent-framework` filer.

## Forstå Microsoft Agent Framework

![Introduksjon til rammeverk](../../../translated_images/no/framework-intro.077af16617cf130c.webp)

[Microsoft Agent Framework (MAF)](https://aka.ms/ai-agents-beginners/agent-framewrok) er Microsofts samordnede rammeverk for å bygge AI-agenter. Det tilbyr fleksibilitet for å håndtere et bredt spekter av agentiske brukstilfeller i både produksjons- og forskningsmiljøer, inkludert:

- **Sekvensiell agentorkestrering** i scenarier der trinnvise arbeidsflyter er nødvendig.
- **Samtidig orkestrering** i scenarier der agenter må fullføre oppgaver samtidig.
- **Gruppesamtale-orkestrering** i scenarier der agenter kan samarbeide om én oppgave.
- **Overleveringsorkestrering** i scenarier der agenter overgir oppgaven til hverandre etter hvert som deloppgaver fullføres.
- **Magnetisk orkestrering** i scenarier der en lederagent oppretter og endrer en oppgaveliste og håndterer koordineringen av underagenter for å fullføre oppgaven.

For å levere AI-agenter i produksjon har MAF også funksjoner for:

- **Observabilitet** gjennom bruk av OpenTelemetry, der hver handling til AI-agenten inkludert verktøykall, orkestreringstrinn, resonnementsflyt og ytelsesovervåking gjennom Microsoft Foundry-dashbord blir sporet.
- **Sikkerhet** ved å hoste agenter nativt på Microsoft Foundry, som inkluderer sikkerhetskontroller som rollebasert tilgang, håndtering av privat data og innebygd innholdssikkerhet.
- **Varighet (Durability)** ettersom agenttråder og arbeidsflyter kan pause, gjenoppta og gjenopprette fra feil, noe som muliggjør lengre kjørende prosesser.
- **Kontroll** ettersom arbeidsflyter med menneskelig innblanding støttes, der oppgaver merkes som krever menneskelig godkjenning.

Microsoft Agent Framework er også fokusert på å være interoperabelt ved å:

- **Sky-agnostisk** - Agenter kan kjøre i containere, on-prem og på tvers av flere ulike skyer.
- **Leverandør-agnostisk** - Agenter kan opprettes gjennom ditt foretrukne SDK inkludert Azure OpenAI og OpenAI
- **Integrering av åpne standarder** - Agenter kan bruke protokoller som Agent-to-Agent(A2A) og Model Context Protocol (MCP) for å oppdage og bruke andre agenter og verktøy.
- **Pluginer og tilkoblinger** - Tilkoblinger kan lages til data- og minnetjenester som Microsoft Fabric, SharePoint, Pinecone og Qdrant.

La oss se på hvordan disse funksjonene anvendes på noen av kjernebegrepene i Microsoft Agent Framework.

## Kjernebegreper i Microsoft Agent Framework

### Agenter

![Agent-komponenter](../../../translated_images/no/agent-components.410a06daf87b4fef.webp)

**Opprette agenter**

Opprettelse av agenter gjøres ved å definere inferenstjenesten (LLM-leverandør), et sett med instruksjoner for AI-agenten å følge, og et tildelt `name`:

```python
agent = AzureOpenAIChatClient(credential=AzureCliCredential()).create_agent( instructions="You are good at recommending trips to customers based on their preferences.", name="TripRecommender" )
```

Ovenfor brukes `Azure OpenAI` men agenter kan opprettes ved hjelp av en rekke tjenester inkludert `Microsoft Foundry Agent Service`:

```python
AzureAIAgentClient(async_credential=credential).create_agent( name="HelperAgent", instructions="You are a helpful assistant." ) as agent
```

OpenAI `Responses`, `ChatCompletion` APIer

```python
agent = OpenAIResponsesClient().create_agent( name="WeatherBot", instructions="You are a helpful weather assistant.", )
```

```python
agent = OpenAIChatClient().create_agent( name="HelpfulAssistant", instructions="You are a helpful assistant.", )
```

eller fjernagenter som bruker A2A-protokollen:

```python
agent = A2AAgent( name=agent_card.name, description=agent_card.description, agent_card=agent_card, url="https://your-a2a-agent-host" )
```

**Kjøre agenter**

Agenter kjøres ved hjelp av `.run` eller `.run_stream`-metodene for enten ikke-strømmede eller strømmede svar.

```python
result = await agent.run("What are good places to visit in Amsterdam?")
print(result.text)
```

```python
async for update in agent.run_stream("What are the good places to visit in Amsterdam?"):
    if update.text:
        print(update.text, end="", flush=True)

```

Hver agentkjøring kan også ha alternativer for å tilpasse parametere som `max_tokens` brukt av agenten, `tools` som agenten kan kalle, og til og med selve `model` som brukes av agenten.

Dette er nyttig i tilfeller der spesifikke modeller eller verktøy kreves for å fullføre en brukers oppgave.

**Verktøy**

Verktøy kan defineres både ved opprettelse av agenten:

```python
def get_attractions( location: Annotated[str, Field(description="The location to get the top tourist attractions for")], ) -> str: """Get the top tourist attractions for a given location.""" return f"The top attractions for {location} are." 


# Når du oppretter en ChatAgent direkte

agent = ChatAgent( chat_client=OpenAIChatClient(), instructions="You are a helpful assistant", tools=[get_attractions]

```

og også når agenten kjøres:

```python

result1 = await agent.run( "What's the best place to visit in Seattle?", tools=[get_attractions] # Verktøyet er kun tilgjengelig for denne kjøringen )
```

**Agenttråder**

Agenttråder brukes for å håndtere samtaler med flere runder. Tråder kan opprettes enten ved:

- Å bruke `get_new_thread()` som gjør det mulig å lagre tråden over tid
- Å opprette en tråd automatisk når en agent kjøres, slik at tråden kun varer under den nåværende kjøringen.

For å opprette en tråd ser koden slik ut:

```python
# Opprett en ny tråd.
thread = agent.get_new_thread() # Kjør agenten med tråden.
response = await agent.run("Hello, I am here to help you book travel. Where would you like to go?", thread=thread)

```

Du kan deretter serialisere tråden for å lagre den for senere bruk:

```python
# Opprett en ny tråd.
thread = agent.get_new_thread() 

# Kjør agenten med tråden.

response = await agent.run("Hello, how are you?", thread=thread) 

# Serialiser tråden for lagring.

serialized_thread = await thread.serialize() 

# Deserialiser trådens tilstand etter lasting fra lagring.

resumed_thread = await agent.deserialize_thread(serialized_thread)
```

**Agent-mellomvare**

Agenter interagerer med verktøy og LLM-er for å fullføre brukerens oppgaver. I visse scenarier ønsker vi å utføre eller spore handlinger mellom disse interaksjonene. Agent-mellomvare gjør oss i stand til å gjøre dette gjennom:

*Funksjons-mellomvare*

Denne mellomvaren gjør at vi kan utføre en handling mellom agenten og en funksjon/verktøy som den skal kalle. Et eksempel på når dette kan brukes er når du ønsker å gjøre logging av funksjonskallet.

I koden nedenfor definerer `next` om neste mellomvare eller den faktiske funksjonen skal kalles.

```python
async def logging_function_middleware(
    context: FunctionInvocationContext,
    next: Callable[[FunctionInvocationContext], Awaitable[None]],
) -> None:
    """Function middleware that logs function execution."""
    # Forbehandling: Logg før funksjonsutførelse
    print(f"[Function] Calling {context.function.name}")

    # Fortsett til neste mellomvare eller funksjonsutførelse
    await next(context)

    # Etterbehandling: Logg etter funksjonsutførelse
    print(f"[Function] {context.function.name} completed")
```

*Chat-mellomvare*

Denne mellomvaren lar oss utføre eller loggføre en handling mellom agenten og forespørslene mot LLM-en.

Dette inneholder viktig informasjon slik som `messages` som sendes til AI-tjenesten.

```python
async def logging_chat_middleware(
    context: ChatContext,
    next: Callable[[ChatContext], Awaitable[None]],
) -> None:
    """Chat middleware that logs AI interactions."""
    # Forbehandling: logg før AI-kall
    print(f"[Chat] Sending {len(context.messages)} messages to AI")

    # Fortsett til neste mellomvare eller AI-tjeneste
    await next(context)

    # Etterbehandling: logg etter AI-respons
    print("[Chat] AI response received")

```

**Agent-minne**

Som dekket i `Agentic Memory`-leksjonen, er minne et viktig element som gjør det mulig for agenten å operere over ulike kontekster. MAF tilbyr flere typer minner:

*In-Memory-lagring*

Dette er minnet som lagres i tråder under applikasjonens kjøring.

```python
# Opprett en ny tråd.
thread = agent.get_new_thread() # Kjør agenten med tråden.
response = await agent.run("Hello, I am here to help you book travel. Where would you like to go?", thread=thread)
```

*Vedvarende meldinger*

Dette minnet brukes når samtalehistorikk lagres på tvers av forskjellige økter. Det defineres ved hjelp av `chat_message_store_factory` :

```python
from agent_framework import ChatMessageStore

# Opprett en tilpasset meldingslager
def create_message_store():
    return ChatMessageStore()

agent = ChatAgent(
    chat_client=OpenAIChatClient(),
    instructions="You are a Travel assistant.",
    chat_message_store_factory=create_message_store
)

```

*Dynamisk minne*

Dette minnet legges til i konteksten før agenter kjøres. Disse minnene kan lagres i eksterne tjenester som mem0:

```python
from agent_framework.mem0 import Mem0Provider

# Bruker Mem0 for avanserte minnefunksjoner
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

Observabilitet er viktig for å bygge pålitelige og vedlikeholdbare agentiske systemer. MAF integreres med OpenTelemetry for å tilby tracing og målere for bedre observabilitet.

```python
from agent_framework.observability import get_tracer, get_meter

tracer = get_tracer()
meter = get_meter()
with tracer.start_as_current_span("my_custom_span"):
    # gjør noe
    pass
counter = meter.create_counter("my_custom_counter")
counter.add(1, {"key": "value"})
```

### Arbeidsflyter

MAF tilbyr arbeidsflyter som er forhåndsdefinerte trinn for å fullføre en oppgave og inkluderer AI-agenter som komponenter i disse trinnene.

Arbeidsflyter består av forskjellige komponenter som gir bedre kontrollflyt. Arbeidsflyter muliggjør også **multi-agent orkestrering** og **sjekkpunktering** for å lagre arbeidsflytens tilstander.

Kjernekomponentene i en arbeidsflyt er:

**Utførere**

Utførere mottar inngangsmeldinger, utfører sine tildelte oppgaver, og produserer deretter en utgangsmelding. Dette driver arbeidsflyten fremover mot å fullføre den større oppgaven. Utførere kan være enten AI-agenter eller egendefinert logikk.

**Kanter**

Kanter brukes for å definere flyten av meldinger i en arbeidsflyt. Disse kan være:

*Direkte kanter* - Enkle én-til-én-tilkoblinger mellom utførere:

```python
from agent_framework import WorkflowBuilder

builder = WorkflowBuilder()
builder.add_edge(source_executor, target_executor)
builder.set_start_executor(source_executor)
workflow = builder.build()
```

*Betingede kanter* - Aktiveres etter at en bestemt betingelse er oppfylt. For eksempel, når hotellrom er utilgjengelige, kan en utfører foreslå andre alternativer.

*Switch-case-kanter* - Ruter meldinger til forskjellige utførere basert på definerte betingelser. For eksempel, hvis en reisekunde har prioritert tilgang, kan deres oppgaver håndteres gjennom en annen arbeidsflyt.

*Fan-out-kanter* - Sender én melding til flere mål.

*Fan-in-kanter* - Samler flere meldinger fra forskjellige utførere og sender dem til ett mål.

**Hendelser**

For å gi bedre observabilitet i arbeidsflyter tilbyr MAF innebygde hendelser for kjøring, inkludert:

- `WorkflowStartedEvent`  - Arbeidsflytkjøring begynner
- `WorkflowOutputEvent` - Arbeidsflyten produserer en utdata
- `WorkflowErrorEvent` - Arbeidsflyten støter på en feil
- `ExecutorInvokeEvent`  - Utføreren begynner behandling
- `ExecutorCompleteEvent`  -  Utføreren avslutter behandlingen
- `RequestInfoEvent` - En forespørsel blir sendt

## Avanserte MAF-mønstre

Avsnittene ovenfor dekker kjernebegrepene i Microsoft Agent Framework. Når du bygger mer komplekse agenter, er her noen avanserte mønstre å vurdere:

- **Sammensetning av mellomvare**: Kjed flere mellomvarehåndterere (logging, autentisering, rate-begrensning) ved å bruke funksjons- og chat-mellomvare for finmasket kontroll over agentens oppførsel.
- **Sjekkpunktering av arbeidsflyt**: Bruk arbeidsflythendelser og serialisering for å lagre og gjenoppta langvarige agentprosesser.
- **Dynamisk verktøyvalg**: Kombiner RAG over verktøybeskrivelser med MAFs verktøyregistrering for å presentere kun relevante verktøy per forespørsel.
- **Multi-agent-overlevering**: Bruk arbeidsflytkanter og betinget ruting for å orkestrere overleveringer mellom spesialiserte agenter.

## Kodeeksempler 

Kodeeksempler for Microsoft Agent Framework finnes i dette depotet under filene `xx-python-agent-framework` og `xx-dotnet-agent-framework`.

## Har du flere spørsmål om Microsoft Agent Framework?

Bli med i [Microsoft Foundry Discord](https://aka.ms/ai-agents/discord) for å møte andre lærende, delta på veiledningstimer og få svar på spørsmål om AI-agentene dine.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfraskrivelse:**
Dette dokumentet er oversatt ved hjelp av AI-oversettelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selv om vi streber etter nøyaktighet, vennligst vær oppmerksom på at automatiske oversettelser kan inneholde feil eller unøyaktigheter. Det opprinnelige dokumentet i sitt originale språk bør anses som den autoritative kilden. For kritisk informasjon anbefales profesjonell menneskelig oversettelse. Vi er ikke ansvarlige for eventuelle misforståelser eller feiltolkninger som oppstår ved bruk av denne oversettelsen.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->