# Utforske Microsoft Agent Framework

![Agent Framework](../../../translated_images/no/lesson-14-thumbnail.90df0065b9d234ee.webp)

### Introduksjon

Denne leksjonen vil dekke:

- Forstå Microsoft Agent Framework: Nøkkelfunksjoner og verdi  
- Utforske nøkkelkonsepter i Microsoft Agent Framework
- Avanserte MAF-mønstre: Arbeidsflyter, middleware og minne

## Læringsmål

Etter å ha fullført denne leksjonen vil du vite hvordan du:

- Bygger produksjonsklare AI-agenter ved hjelp av Microsoft Agent Framework
- Anvender kjernefunksjonene i Microsoft Agent Framework på dine agentiske brukstilfeller
- Bruker avanserte mønstre inkludert arbeidsflyter, middleware og observabilitet

## Kodeeksempler 

Kodeeksempler for [Microsoft Agent Framework (MAF)](https://learn.microsoft.com/en-us/agent-framework/overview/?wt.mc_id=youtube_26688_organicsocial_reactor&pivots=programming-language-python) finnes i dette depotet under filene `xx-python-agent-framework` og `xx-dotnet-agent-framework`.

## Forstå Microsoft Agent Framework

![Framework Intro](../../../translated_images/no/framework-intro.077af16617cf130c.webp)

[Microsoft Agent Framework (MAF)](https://learn.microsoft.com/en-us/agent-framework/overview/?wt.mc_id=youtube_26688_organicsocial_reactor&pivots=programming-language-python) er Microsofts samlede rammeverk for å bygge AI-agenter. Det tilbyr fleksibilitet til å dekke det brede spekteret av agentiske brukstilfeller som sees både i produksjon og forskningsmiljøer, inkludert:

- **Sekvensiell agentorkestrering** i scenarier hvor trinnvise arbeidsflyter er nødvendig.
- **Parallell orkestrering** i scenarier hvor agenter må utføre oppgaver samtidig.
- **Gruppechatorchestring** i scenarier hvor agenter kan samarbeide om én oppgave.
- **Overleveringsorkestrering** i scenarier hvor agenter overfører oppgaven til hverandre etter hvert som deloppgavene fullføres.
- **Magnetisk orkestrering** i scenarier hvor en lederagent oppretter og modifiserer en oppgaveliste og håndterer koordineringen av underagenter for å fullføre oppgaven.

For å levere AI-agenter i produksjon har MAF også inkludert funksjoner for:

- **Observabilitet** gjennom bruk av OpenTelemetry hvor hver handling til AI-agenten, inkludert verktøy-innkalling, orkestreringstrinn, resonneringsflyter og ytelsesovervåkning gjennom Microsoft Foundry-dashbord.
- **Sikkerhet** ved å hoste agenter nativt på Microsoft Foundry som inkluderer sikkerhetskontroller som rollebasert tilgang, håndtering av privat data og innebygd innholdssikkerhet.
- **Holdbarhet** ettersom agenttråder og arbeidsflyter kan pause, gjenoppta og gjenopprette fra feil, noe som muliggjør lengre kjørende prosesser.
- **Kontroll** ettersom arbeidsflyter med menneskelig innblanding støttes der oppgaver merkes som krever menneskelig godkjenning.

Microsoft Agent Framework fokuserer også på interoperabilitet ved:

- **Å være sky-agnostisk** - Agenter kan kjøre i containere, lokalt og på tvers av flere ulike skyer.
- **Å være leverandør-agnostisk** - Agenter kan opprettes via ditt foretrukne SDK inkludert Azure OpenAI og OpenAI.
- **Å integrere åpne standarder** - Agenter kan bruke protokoller som Agent-to-Agent (A2A) og Model Context Protocol (MCP) for å oppdage og bruke andre agenter og verktøy.
- **Plugins og koblinger** - Tilkoblinger kan gjøres til data- og minnetjenester som Microsoft Fabric, SharePoint, Pinecone og Qdrant.

La oss se på hvordan disse funksjonene anvendes på noen av de kjernebegrepene i Microsoft Agent Framework.

## Nøkkelkonsepter for Microsoft Agent Framework

### Agenter

![Agent Framework](../../../translated_images/no/agent-components.410a06daf87b4fef.webp)

**Opprette agenter**

Agentopprettelse gjøres ved å definere inferenstjenesten (LLM-leverandør), et
sett med instruksjoner som AI-agenten skal følge, og et tildelt `navn`:

```python
agent = AzureOpenAIChatClient(credential=AzureCliCredential()).create_agent( instructions="You are good at recommending trips to customers based on their preferences.", name="TripRecommender" )
```

Ovenfor brukes `Azure OpenAI`, men agenter kan opprettes ved hjelp av en rekke tjenester inkludert `Microsoft Foundry Agent Service`:

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

eller [MiniMax](https://platform.minimaxi.com/), som tilbyr en OpenAI-kompatibel API med store kontekstvinduer (opptil 204K tokens):

```python
agent = OpenAIChatClient(base_url="https://api.minimax.io/v1", api_key=os.environ["MINIMAX_API_KEY"], model_id="MiniMax-M3").create_agent( name="HelpfulAssistant", instructions="You are a helpful assistant.", )
```

eller eksterne agenter som bruker A2A-protokollen:

```python
agent = A2AAgent( name=agent_card.name, description=agent_card.description, agent_card=agent_card, url="https://your-a2a-agent-host" )
```

**Kjøre agenter**

Agenter kjøres ved hjelp av `.run` eller `.run_stream` metodene for henholdsvis ikke-strømmende eller strømmende svar.

```python
result = await agent.run("What are good places to visit in Amsterdam?")
print(result.text)
```

```python
async for update in agent.run_stream("What are the good places to visit in Amsterdam?"):
    if update.text:
        print(update.text, end="", flush=True)

```

Hver agentkjøring kan også ha alternativer for å tilpasse parametere som `max_tokens` brukt av agenten, `tools` som agenten kan kalle, og til og med `model` selv brukt av agenten.

Dette er nyttig i tilfeller hvor spesifikke modeller eller verktøy kreves for å fullføre en brukers oppgave.

**Verktøy**

Verktøy kan defineres både når agenten defineres:

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

Agenttråder brukes til å håndtere flerturssamtaler. Tråder kan opprettes ved enten:

- Bruke `get_new_thread()` som gjør at tråden kan lagres over tid
- Automatisk opprettelse av en tråd ved kjøring av en agent, hvor tråden kun varer under gjeldende kjøring.

For å opprette en tråd ser koden slik ut:

```python
# Opprett en ny tråd.
thread = agent.get_new_thread() # Kjør agenten med tråden.
response = await agent.run("Hello, I am here to help you book travel. Where would you like to go?", thread=thread)

```

Du kan så serialisere tråden for å lagre den til senere bruk:

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

**Agent Middleware**

Agenter interagerer med verktøy og LLMer for å utføre brukerens oppgaver. I enkelte scenarier ønsker vi å utføre eller spore handlinger mellom disse interaksjonene. Agent middleware gjør dette mulig gjennom:

*Funksjonsmiddleware*

Denne middleware tillater oss å utføre en handling mellom agenten og en funksjon/verktøy som den skal kalle. Et eksempel på når dette kan brukes er hvis du ønsker å logge funksjonskallet.

I koden nedenfor definerer `next` om neste middleware eller den faktiske funksjonen skal kalles.

```python
async def logging_function_middleware(
    context: FunctionInvocationContext,
    next: Callable[[FunctionInvocationContext], Awaitable[None]],
) -> None:
    """Function middleware that logs function execution."""
    # Forbehandling: Logg før funksjonskjøring
    print(f"[Function] Calling {context.function.name}")

    # Fortsett til neste mellomvare eller funksjonskjøring
    await next(context)

    # Etterbehandling: Logg etter funksjonskjøring
    print(f"[Function] {context.function.name} completed")
```

*Chat Middleware*

Denne middleware gjør det mulig å utføre eller logge en handling mellom agenten og forespørsler mellom LLM.

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

    # Etterbehandling: Logg etter AI-respons
    print("[Chat] AI response received")

```

**Agentminne**

Som dekket i leksjonen `Agentic Memory`, er minne et viktig element for å gjøre agenten i stand til å operere over ulike kontekster. MAF tilbyr flere forskjellige typer minner:

*Minne i Minne*

Dette er minnet lagret i tråder under applikasjonens kjøring.

```python
# Opprett en ny tråd.
thread = agent.get_new_thread() # Kjør agenten med tråden.
response = await agent.run("Hello, I am here to help you book travel. Where would you like to go?", thread=thread)
```

*Vedvarende meldinger*

Dette minnet brukes når samtalehistorikk lagres på tvers av ulike økter. Det defineres med `chat_message_store_factory`:

```python
from agent_framework import ChatMessageStore

# Opprett en egendefinert meldingslager
def create_message_store():
    return ChatMessageStore()

agent = ChatAgent(
    chat_client=OpenAIChatClient(),
    instructions="You are a Travel assistant.",
    chat_message_store_factory=create_message_store
)

```

*Dynamisk minne*

Dette minnet legges til konteksten før agenter kjører. Disse minnene kan lagres i eksterne tjenester som mem0:

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

**Agent Observability**

Observabilitet er viktig for å bygge pålitelige og vedlikeholdbare agentiske systemer. MAF integreres med OpenTelemetry for å tilby sporing og målere for bedre observabilitet.

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

Arbeidsflyter består av ulike komponenter som muliggjør bedre kontrollflyt. Arbeidsflyter muliggjør også **multi-agent orkestrering** og **kontrollpunkter** for å lagre arbeidsflyt-tilstander.

Kjernekomponentene i en arbeidsflyt er:

**Utøvere**

Utøvere mottar inndata-meldinger, utfører deres tildelte oppgaver, og produserer deretter en utgangsmelding. Dette driver arbeidsflyten fremover mot å fullføre den større oppgaven. Utøvere kan være enten AI-agent eller egendefinert logikk.

**Kanter**

Kanter brukes til å definere flyten av meldinger i en arbeidsflyt. Disse kan være:

*Direkte kanter* - Enkle én-til-én tilkoblinger mellom utøvere:

```python
from agent_framework import WorkflowBuilder

builder = WorkflowBuilder()
builder.add_edge(source_executor, target_executor)
builder.set_start_executor(source_executor)
workflow = builder.build()
```

*Betingede kanter* - Aktiveres etter at en viss betingelse er oppfylt. For eksempel, når hotellrom er utilgjengelige, kan en utøver foreslå andre alternativer.

*Switch-case kanter* - Ruter meldinger til forskjellige utøvere basert på definerte betingelser. For eksempel, hvis en reisekunde har prioritetstilgang, håndteres deres oppgaver gjennom en annen arbeidsflyt.

*Fan-ut kanter* - Sender én melding til flere mål.

*Fan-inn kanter* - Samler meldinger fra flere utøvere og sender til ett mål.

**Hendelser**

For å tilby bedre observabilitet i arbeidsflyter tilbyr MAF innebygde hendelser for utførelse, inkludert:

- `WorkflowStartedEvent`  - Arbeidsflytens utførelse begynner
- `WorkflowOutputEvent` - Arbeidsflyten produserer en utgang
- `WorkflowErrorEvent` - Arbeidsflyten møter en feil
- `ExecutorInvokeEvent`  - Utøver starter behandling
- `ExecutorCompleteEvent`  -  Utøver ferdigstiller behandling
- `RequestInfoEvent` - En forespørsel sendes ut

## Avanserte MAF-mønstre

Seksjonene over dekker nøkkelkonsepter for Microsoft Agent Framework. Når du bygger mer komplekse agenter, er her noen avanserte mønstre å vurdere:

- **Middleware-sammensetning**: Kjed flere middleware-håndterere (logging, autentisering, rate-begrensning) ved bruk av både funksjons- og chat-middleware for finstilt kontroll over agentoppførsel.
- **Arbeidsflyt-kontrollpunkter**: Bruk arbeidsflythendelser og serialisering for å lagre og gjenoppta langvarige agentprosesser.
- **Dynamisk verktøyvalg**: Kombiner RAG over verktøybeskrivelser med MAF sin verktøyregistrering for å bare presentere relevante verktøy per forespørsel.
- **Multi-agent overlevering**: Bruk arbeidsflytkanter og betinget ruting for å orkestrere overlevering mellom spesialiserte agenter.

## Hosting av LangChain / LangGraph Agenter på Microsoft Foundry

Microsoft Agent Framework er **rammeverksinteroperabelt** — du er ikke begrenset til agenter skrevet med MAF. Hvis du allerede har en agent bygget med **LangChain** eller **LangGraph**, kan du kjøre den som en **Microsoft Foundry-hostet agent** slik at Foundry håndterer runtime, økter, skalering, identitet og protokollendepunkter for deg, mens agentlogikken din forblir i LangGraph.

Dette gjøres med `langchain_azure_ai.agents.hosting` pakken, som eksponerer en kompilert LangGraph-graf over de samme protokollene som Foundry-hostede agenter bruker.

**1. Installer hosting-tillegget:**

```bash
pip install -U "langchain-azure-ai[hosting]>=1.2.4" azure-identity
```

`hosting`-tillegget installerer Foundry-protokollbibliotekene: `azure-ai-agentserver-responses` (det OpenAI-kompatible `/responses` endepunktet) og `azure-ai-agentserver-invocations` (det generiske `/invocations` endepunktet).

**2. Velg en hosting-protokoll:**

| Protokoll | Host-klasse | Endepunkt | Brukes når |
|----------|-----------|----------|----------|
| **Responses** | `ResponsesHostServer` | `/responses` | Du ønsker OpenAI-kompatibel chat, streaming, svarhistorikk og samtaletråding — anbefalt standard for konversasjonsagenter. |
| **Invocations** | `InvocationsHostServer` | `/invocations` | Du trenger et tilpasset JSON-format, et webhook-lignende endepunkt, eller ikke-konversasjonell behandling. |

Fordi **Responses API er hoved-APIen for agent-stil utvikling i Foundry**, start med `ResponsesHostServer` for de fleste agenter.

**3. Konfigurer miljøvariabler** (`az login` først så `DefaultAzureCredential` kan autentisere):

```bash
export FOUNDRY_PROJECT_ENDPOINT="https://<resource>.services.ai.azure.com/api/projects/<project>"
export FOUNDRY_MODEL_NAME="gpt-5-mini"
```

Når agenten senere kjører som hostet agent i Foundry, injiserer plattformen automatisk `FOUNDRY_PROJECT_ENDPOINT`.

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
    deployment = os.environ.get("FOUNDRY_MODEL_NAME", "gpt-5-mini")
    credential = DefaultAzureCredential()
    project = AIProjectClient(endpoint=project_endpoint, credential=credential)
    openai_client = project.get_openai_client()
    token_provider = get_bearer_token_provider(credential, _AZURE_AI_SCOPE)

    # ChatOpenAI her retter seg mot Foundry-prosjektets OpenAI-kompatible (Responses) endepunkt.
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

**Nøkkeloppførsler:**

- **Samtaler**: Klienter fortsetter en samtale ved å sende `previous_response_id` eller en `conversation` ID. Hvis grafen din er kompilert med en LangGraph checkpointer, nøkkelsetter Foundry samtalestaten til kontrollpunktet (bruk en holdbar checkpointer i produksjon; `MemorySaver` er grei for lokal testing).
- **Menneskelig i sløyfen**: Hvis grafen din bruker LangGraph `interrupt()`, viser `ResponsesHostServer` den ventende avbrytelsen som en Responses `function_call` / `mcp_approval_request` post, og klienter fortsetter med en tilsvarende `function_call_output` / `mcp_approval_response`.
- **Deploy til Foundry**: Bruk Azure Developer CLI — `azd ext install azure.ai.agents`, `azd ai agent init -m <manifest>`, `azd ai agent run` (lokalt, krever Docker), deretter `azd provision` og `azd deploy`. Hosting av agent krever **Foundry Project Manager** rolle.

En kjørbar versjon av dette eksemplet finnes i [code-samples/14-langchain-hosted-agent.py](../../../14-microsoft-agent-framework/code-samples/14-langchain-hosted-agent.py). For full gjennomgang (Invocations protokoll, egendefinerte forespørsels-skjemaer, og feilsøking), se [Host LangGraph agents as Foundry hosted agents](https://learn.microsoft.com/azure/foundry/how-to/develop/langchain-hosted-agents).

## Kodeeksempler 

Kodeeksempler for Microsoft Agent Framework finnes i dette depotet under filene `xx-python-agent-framework` og `xx-dotnet-agent-framework`.

## Har du flere spørsmål om Microsoft Agent Framework?

Bli med i [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D) for å møte andre lærende, delta på kontortid og få spørsmål om AI-agenter besvart.
## Forrige leksjon

[Minne for AI-agenter](../13-agent-memory/README.md)

## Neste leksjon

[Bygge databrukagenter (CUA)](../15-browser-use/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfraskrivelse**:
Dette dokumentet er oversatt ved hjelp av AI-oversettelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selv om vi streber etter nøyaktighet, vær oppmerksom på at automatiske oversettelser kan inneholde feil eller unøyaktigheter. Det opprinnelige dokumentet på originalspråket skal betraktes som den autoritative kilden. For kritisk informasjon anbefales profesjonell menneskelig oversettelse. Vi er ikke ansvarlige for eventuelle misforståelser eller feiltolkninger som oppstår ved bruk av denne oversettelsen.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->