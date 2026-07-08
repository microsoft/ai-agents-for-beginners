# Utforske Microsoft Agent Framework

![Agent Framework](../../../translated_images/no/lesson-14-thumbnail.90df0065b9d234ee.webp)

### Introduksjon

Denne leksjonen vil dekke:

- Forstå Microsoft Agent Framework: Nøkkelfunksjoner og verdi  
- Utforske nøkkelkonsepter i Microsoft Agent Framework
- Avanserte MAF-mønstre: Arbeidsflyter, mellomvare og minne

## Læringsmål

Etter å ha fullført denne leksjonen vil du vite hvordan du:

- Bygger produksjonsklare AI-agenter ved bruk av Microsoft Agent Framework
- Anvender kjernefunksjonene til Microsoft Agent Framework på dine agent-baserte bruksområder
- Bruker avanserte mønstre inkludert arbeidsflyter, mellomvare og observabilitet

## Kodeeksempler 

Kodeeksempler for [Microsoft Agent Framework (MAF)](https://aka.ms/ai-agents-beginners/agent-framework) kan finnes i dette depotet under `xx-python-agent-framework` og `xx-dotnet-agent-framework` filer.

## Forstå Microsoft Agent Framework

![Framework Intro](../../../translated_images/no/framework-intro.077af16617cf130c.webp)

[Microsoft Agent Framework (MAF)](https://aka.ms/ai-agents-beginners/agent-framework) er Microsofts samlete rammeverk for å bygge AI-agenter. Det tilbyr fleksibilitet til å dekke det brede spekteret av agent-baserte bruksområder som ses både i produksjon og forskningsmiljøer, inkludert:

- **Sekvensiell agentorkestrering** i scenarier hvor trinnvise arbeidsflyter er nødvendige.
- **Samtidig orkestrering** i scenarier hvor agenter må fullføre oppgaver samtidig.
- **Gruppechatsorkestrering** i scenarier hvor agenter kan samarbeide om én oppgave.
- **Overleveringsorkestrering** i scenarier hvor agenter overleverer oppgaven til hverandre etter hvert som deloppgaver fullføres.
- **Magnetisk orkestrering** i scenarier der en lederagent oppretter og endrer en oppgaveliste og håndterer koordineringen av underagenter for å fullføre oppgaven.

For å levere AI-agenter i produksjon, inkluderer MAF også funksjoner for:

- **Observabilitet** gjennom bruk av OpenTelemetry hvor hver handling til AI-agenten, inkludert verktøysanrop, orkestreringssteg, begrunnelsesflyt og ytelsesmåling skjer via Microsoft Foundry dashbord.
- **Sikkerhet** ved å hoste agenter nativt på Microsoft Foundry som inkluderer sikkerhetskontroller som rollebasert tilgang, håndtering av private data og innebygd innholdssikkerhet.
- **Holdbarhet** da agenttråder og arbeidsflyter kan pause, gjenoppta og komme seg fra feil som muliggjør lengre kjørende prosesser.
- **Kontroll** da arbeidsflyter med menneskelig innblanding støttes der oppgaver merkes som krevende menneskelig godkjenning.

Microsoft Agent Framework fokuserer også på å være interoperabel ved å:

- **Være skyleverandøruavhengig** - Agenter kan kjøre i containere, lokalt og på tvers av flere forskjellige skyer.
- **Være leverandøruavhengig** - Agenter kan opprettes med ditt foretrukne SDK inkludert Azure OpenAI og OpenAI
- **Integrere åpne standarder** - Agenter kan bruke protokoller som Agent-to-Agent (A2A) og Model Context Protocol (MCP) for å oppdage og bruke andre agenter og verktøy.
- **Plugins og tilkoblinger** - Tilkoblinger kan gjøres til data- og minnetjenester som Microsoft Fabric, SharePoint, Pinecone og Qdrant.

La oss se på hvordan disse funksjonene anvendes på noen av kjernebegrepene i Microsoft Agent Framework.

## Nøkkelkonsepter i Microsoft Agent Framework

### Agenter

![Agent Framework](../../../translated_images/no/agent-components.410a06daf87b4fef.webp)

**Opprette Agenter**

Agentopprettelse gjøres ved å definere inferenstjenesten (LLM-leverandør), et
sett med instruksjoner for AI-agenten å følge, og et tildelt `navn`:

```python
agent = AzureOpenAIChatClient(credential=AzureCliCredential()).create_agent( instructions="You are good at recommending trips to customers based on their preferences.", name="TripRecommender" )
```

Ovenfor brukes `Azure OpenAI` men agenter kan opprettes ved bruk av en rekke tjenester inkludert `Microsoft Foundry Agent Service`:

```python
AzureAIAgentClient(async_credential=credential).create_agent( name="HelperAgent", instructions="You are a helpful assistant." ) as agent
```

OpenAI `Responses`, `ChatCompletion` API-er

```python
agent = OpenAIResponsesClient().create_agent( name="WeatherBot", instructions="You are a helpful weather assistant.", )
```

```python
agent = OpenAIChatClient().create_agent( name="HelpfulAssistant", instructions="You are a helpful assistant.", )
```

eller [MiniMax](https://platform.minimaxi.com/), som tilbyr en OpenAI-kompatibel API med store kontekstvinduer (opptil 204K tokens):

```python
agent = OpenAIChatClient(base_url="https://api.minimax.io/v1", api_key=os.environ["MINIMAX_API_KEY"], model_id="MiniMax-M3").create_agent( name="HelpfulAssistant", instructions="You are a helpful assistant.", )
```

eller eksterne agenter ved bruk av A2A-protokollen:

```python
agent = A2AAgent( name=agent_card.name, description=agent_card.description, agent_card=agent_card, url="https://your-a2a-agent-host" )
```

**Kjøre Agenter**

Agenter kjøres ved bruk av `.run` eller `.run_stream` metodene for enten ikke-strømmende eller strømmende svar.

```python
result = await agent.run("What are good places to visit in Amsterdam?")
print(result.text)
```

```python
async for update in agent.run_stream("What are the good places to visit in Amsterdam?"):
    if update.text:
        print(update.text, end="", flush=True)

```

Hver agentkjøring kan også ha alternativer for å tilpasse parametere som `max_tokens` brukt av agenten, `tools` agenten kan kalle, og til og med `model` selv som brukes for agenten.

Dette er nyttig i tilfeller hvor spesifikke modeller eller verktøy er nødvendige for å fullføre brukerens oppgave.

**Verktøy**

Verktøy kan defineres både ved definering av agenten:

```python
def get_attractions( location: Annotated[str, Field(description="The location to get the top tourist attractions for")], ) -> str: """Get the top tourist attractions for a given location.""" return f"The top attractions for {location} are." 


# Når du oppretter en ChatAgent direkte

agent = ChatAgent( chat_client=OpenAIChatClient(), instructions="You are a helpful assistant", tools=[get_attractions]

```

og også når agenten kjøres:

```python

result1 = await agent.run( "What's the best place to visit in Seattle?", tools=[get_attractions] # Verktøy gitt kun for denne kjøringen )
```

**Agenttråder**

Agenttråder brukes til å håndtere flerturisamtaler. Tråder kan opprettes enten ved:

- Bruk av `get_new_thread()` som gjør at tråden kan lagres over tid
- Automatisk opprettelse av tråd når agenten kjøres, og bare ha tråden aktiv under gjeldende kjøring.

For å opprette en tråd ser koden slik ut:

```python
# Opprett en ny tråd.
thread = agent.get_new_thread() # Kjør agenten med tråden.
response = await agent.run("Hello, I am here to help you book travel. Where would you like to go?", thread=thread)

```

Du kan deretter seraliserer tråden for lagring til senere bruk:

```python
# Opprett en ny tråd.
thread = agent.get_new_thread() 

# Kjør agenten med tråden.

response = await agent.run("Hello, how are you?", thread=thread) 

# Serialiser tråden for lagring.

serialized_thread = await thread.serialize() 

# Deserialiser trådtilstanden etter lasting fra lagring.

resumed_thread = await agent.deserialize_thread(serialized_thread)
```

**Agent Mellomvare**

Agenter samhandler med verktøy og LLM-er for å fullføre brukeroppgaver. I visse scenarioer ønsker vi å kjøre eller spore mellom disse interaksjonene. Agent-mellomvare gjør dette mulig gjennom:

*Funksjon Mellomvare*

Denne mellomvaren lar oss utføre en handling mellom agenten og en funksjon/verktøy den vil kalle. Et eksempel på bruk er når du ønsker å logge funksjonskallet.

I koden under definerer `next` om neste mellomvare eller den faktiske funksjonen skal kalles.

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

*Chat Mellomvare*

Denne mellomvaren lar oss utføre eller logge en handling mellom agenten og forespørslene til LLM.

Dette inneholder viktig informasjon som `messages` som sendes til AI-tjenesten.

```python
async def logging_chat_middleware(
    context: ChatContext,
    next: Callable[[ChatContext], Awaitable[None]],
) -> None:
    """Chat middleware that logs AI interactions."""
    # Forbehandling: Logg før AI-kall
    print(f"[Chat] Sending {len(context.messages)} messages to AI")

    # Fortsett til neste mellomvare eller AI-tjeneste
    await next(context)

    # Etterbehandling: Logg etter AI-svar
    print("[Chat] AI response received")

```

**Agentminne**

Som dekket i leksjonen `Agentic Memory`, er minnet et viktig element for å la agenten operere over forskjellige kontekster. MAF tilbyr flere forskjellige typer minne:

*In-Memory Lagring*

Dette er minnet som lagres i tråder under applikasjonskjøringen.

```python
# Opprett en ny tråd.
thread = agent.get_new_thread() # Kjør agenten med tråden.
response = await agent.run("Hello, I am here to help you book travel. Where would you like to go?", thread=thread)
```

*Vedvarende Meldinger*

Dette minnet brukes til å lagre samtalehistorikk på tvers av sesjoner. Det defineres ved å bruke `chat_message_store_factory` :

```python
from agent_framework import ChatMessageStore

# Opprett en tilpasset meldingslagring
def create_message_store():
    return ChatMessageStore()

agent = ChatAgent(
    chat_client=OpenAIChatClient(),
    instructions="You are a Travel assistant.",
    chat_message_store_factory=create_message_store
)

```

*Dynamisk Minne*

Dette minnet legges til i konteksten før agenter kjører. Disse minnene kan lagres i eksterne tjenester som mem0:

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

**Agentobservabilitet**

Observabilitet er viktig for å bygge pålitelige og vedlikeholdbare agentbaserte systemer. MAF integrerer med OpenTelemetry for å tilby tracing og målinger for bedre observabilitet.

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

MAF tilbyr arbeidsflyter som er forhåndsdefinerte steg for å fullføre en oppgave og inkluderer AI-agenter som komponenter i disse stegene.

Arbeidsflyter består av ulike komponenter som gir bedre kontrollflyt. Arbeidsflyter muliggjør også **multi-agent orkestrering** og **checkpointing** for å lagre arbeidsflytstatus.

Kjernen i en arbeidsflyt er:

**Utførere**

Utførere mottar inngangsmeldinger, utfører sine tildelte oppgaver, og produserer deretter en utgangsmelding. Dette beveger arbeidsflyten fremover mot å fullføre den større oppgaven. Utførere kan være enten AI-agent eller egendefinert logikk.

**Kantrer**

Kantrer brukes for å definere flyten av meldinger i en arbeidsflyt. Disse kan være:

*Direkte Kantrer* - Enkle en-til-en forbindelser mellom utførere:

```python
from agent_framework import WorkflowBuilder

builder = WorkflowBuilder()
builder.add_edge(source_executor, target_executor)
builder.set_start_executor(source_executor)
workflow = builder.build()
```

*Betingede Kantrer* - Aktiveres etter at en betingelse er oppfylt. For eksempel, hvis hotellrom ikke er tilgjengelig, kan en utfører foreslå andre alternativer.

*Switch-case Kantrer* - Ruter meldinger til forskjellige utførere basert på definerte betingelser. For eksempel, hvis en reisekunde har prioritert tilgang og deres oppgaver håndteres gjennom en annen arbeidsflyt.

*Fan-ut Kantrer* - Sender én melding til flere mål.

*Fan-inn Kantrer* - Samler flere meldinger fra forskjellige utførere og sender til ett mål.

**Hendelser**

For å gi bedre observabilitet i arbeidsflyter, tilbyr MAF innebygde hendelser for utførelse som inkluderer:

- `WorkflowStartedEvent`  - Arbeidsflytutførelse starter
- `WorkflowOutputEvent` - Arbeidsflyten produserer en utgang
- `WorkflowErrorEvent` - Arbeidsflyten støter på en feil
- `ExecutorInvokeEvent`  - Utfører starter prosessering
- `ExecutorCompleteEvent`  -  Utfører fullfører prosessering
- `RequestInfoEvent` - En forespørsel utstedes

## Avanserte MAF-mønstre

Seksjonene ovenfor dekker nøkkelkonseptene i Microsoft Agent Framework. Når du bygger mer komplekse agenter, bør du vurdere noen avanserte mønstre:

- **Sammensetning av Mellomvare**: Kjede sammen flere mellomvarebehandlere (logging, autentisering, rate-begrensning) ved bruk av funksjon- og chat-mellomvare for finjustert kontroll over agentatferd.
- **Arbeidsflyt Checkpointing**: Bruk arbeidsflythendelser og serialisering for å lagre og gjenoppta langvarige agentprosesser.
- **Dynamisk Verktøyvalg**: Kombiner RAG over verktøybeskrivelser med MAF sin verktøyregistrering for å presentere kun relevante verktøy per spørring.
- **Multi-Agent Overlevering**: Bruk arbeidsflytkantene og betinget ruting for å orkestrere overlevering mellom spesialiserte agenter.

## Hosting av LangChain / LangGraph Agenter på Microsoft Foundry

Microsoft Agent Framework er **rammeverksinteroperabelt** — du er ikke begrenset til agenter skrevet med MAF. Hvis du allerede har en agent bygget med **LangChain** eller **LangGraph**, kan du kjøre den som en **Microsoft Foundry hostet agent** slik at Foundry håndterer kjøretid, sesjoner, skalering, identitet og protokollendepunkter for deg, mens agentlogikken din forblir i LangGraph.

Dette gjøres med `langchain_azure_ai.agents.hosting`-pakken, som eksponerer en kompilert LangGraph-graf over de samme protokollene som Foundry-hostede agenter bruker.

**1. Installer hosting-ekstraen:**

```bash
pip install -U "langchain-azure-ai[hosting]>=1.2.4" azure-identity
```

`hosting`-ekstraen installerer Foundry-protokollbibliotekene: `azure-ai-agentserver-responses` (det OpenAI-kompatible `/responses` endepunktet) og `azure-ai-agentserver-invocations` (det generiske `/invocations` endepunktet).

**2. Velg en hostingprotokoll:**

| Protokoll | Host-klasse | Endepunkt | Bruk når |
|----------|-------------|-----------|----------|
| **Responses** | `ResponsesHostServer` | `/responses` | Du ønsker OpenAI-kompatibel chat, streaming, svarhistorikk og samtaletråding — anbefalt standard for konversasjonsagenter. |
| **Invocations** | `InvocationsHostServer` | `/invocations` | Du trenger et egendefinert JSON-format, et webhook-lignende endepunkt, eller ikke-konversasjonell prosessering. |

Fordi **Responses API er hoved-API-en for agentstil utvikling i Foundry**, start med `ResponsesHostServer` for de fleste agenter.

**3. Konfigurer miljøvariabler** (`az login` først slik at `DefaultAzureCredential` kan autentisere):

```bash
export FOUNDRY_PROJECT_ENDPOINT="https://<resource>.services.ai.azure.com/api/projects/<project>"
export FOUNDRY_MODEL_NAME="gpt-4.1"
```

Når agenten senere kjører som en hostet agent i Foundry, injiserer plattformen `FOUNDRY_PROJECT_ENDPOINT` automatisk.

**4. Eksponer en LangGraph-agent over Responses-protokollen:**

```python
import os

from azure.ai.projects import AIProjectClient
from azure.identity import DefaultAzureCredential, get_bearer_token_provider
from langchain.agents import create_agent
from langchain_openai import ChatOpenAI
from langchain_azure_ai.agents.hosting import ResponsesHostServer

_AZURE_AI_SCOPE = "https://ai.azure.com/.default"


def build_chat_model() -> ChatOpenAI:
    project_endpoint = os.environ["FOUNDRY_PROJECT_ENDPOINT"].rstrip("/")
    deployment = os.environ.get("FOUNDRY_MODEL_NAME", "gpt-4.1")
    credential = DefaultAzureCredential()
    project = AIProjectClient(endpoint=project_endpoint, credential=credential)
    openai_client = project.get_openai_client()
    token_provider = get_bearer_token_provider(credential, _AZURE_AI_SCOPE)

    # ChatOpenAI her retter seg mot Foundry-prosjektets OpenAI-kompatible (Responses)-endepunkt.
    return ChatOpenAI(
        model=deployment,
        base_url=str(openai_client.base_url),
        api_key=token_provider,
    )


def main() -> None:
    graph = create_agent(build_chat_model(), tools=[])
    port = int(os.environ.get("PORT", "8088"))
    ResponsesHostServer(graph).run(port=port)


if __name__ == "__main__":
    main()
```

Kjør den lokalt med `python main.py`, og send deretter en Responses-forespørsel til `http://localhost:8088/responses`.

**Nøkkelatferd:**

- **Samtaler**: Klienter fortsetter en samtale ved å sende `previous_response_id` eller en `conversation` ID. Hvis grafen din er kompilert med en LangGraph-sjekkpunktfunksjon, nøkkelreferer Foundry samtalestatus til sjekkpunktet (bruk en holdbar sjekkpunktfunksjon i produksjon; `MemorySaver` er greit for lokal testing).
- **Menneske i løkken**: Hvis grafen bruker LangGraph `interrupt()`, eksponerer `ResponsesHostServer` den ventende avbrytelsen som en Responses `function_call` / `mcp_approval_request`-post, og klienter gjenopptar med en tilsvarende `function_call_output` / `mcp_approval_response`.
- **Deploy til Foundry**: Bruk Azure Developer CLI — `azd ext install azure.ai.agents`, `azd ai agent init -m <manifest>`, `azd ai agent run` (lokalt, krever Docker), deretter `azd provision` og `azd deploy`. Hosting-agent-utplassering krever rollen **Foundry Project Manager**.

En kjørbar versjon av dette eksemplet finnes i [code-samples/14-langchain-hosted-agent.py](../../../14-microsoft-agent-framework/code-samples/14-langchain-hosted-agent.py). For full gjennomgang (Invocations-protokoll, egendefinerte forespørselsskjemaer, og feilsøking), se [Host LangGraph agents as Foundry hosted agents](https://learn.microsoft.com/azure/foundry/how-to/develop/langchain-hosted-agents).

## Kodeeksempler 

Kodeeksempler for Microsoft Agent Framework finnes i dette depotet under `xx-python-agent-framework` og `xx-dotnet-agent-framework` filer.

## Har du flere spørsmål om Microsoft Agent Framework?

Bli med i [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D) for å møte andre lærende, delta på kontortid og få svar på spørsmål om AI-agentene dine.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfraskrivelse**:
Dette dokumentet er oversatt ved hjelp av AI-oversettelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selv om vi streber etter nøyaktighet, vær oppmerksom på at automatiske oversettelser kan inneholde feil eller unøyaktigheter. Det opprinnelige dokumentet på originalspråket skal betraktes som den autoritative kilden. For kritisk informasjon anbefales profesjonell menneskelig oversettelse. Vi er ikke ansvarlige for eventuelle misforståelser eller feiltolkninger som oppstår ved bruk av denne oversettelsen.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->