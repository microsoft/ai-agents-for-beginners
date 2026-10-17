# Utforske Microsoft Agent Framework

![Agent Framework](../../../translated_images/no/lesson-14-thumbnail.90df0065b9d234ee.webp)

### Innledning

Denne leksjonen vil dekke:

- Forstå Microsoft Agent Framework: Nøkkelfunksjoner og verdi  
- Utforske nøkkelkoncepter i Microsoft Agent Framework
- Avanserte MAF-mønstre: Arbeidsflyter, mellomvare og minne

## Læringsmål

Etter å ha fullført denne leksjon vil du kunne:

- Bygge produksjonsklare AI-agenter ved bruk av Microsoft Agent Framework
- Anvende kjernefunksjonene i Microsoft Agent Framework på dine agent-baserte bruksområder
- Bruke avanserte mønstre inkludert arbeidsflyter, mellomvare og observasjon

## Kodeeksempler 

Kodeeksempler for [Microsoft Agent Framework (MAF)](https://learn.microsoft.com/en-us/agent-framework/overview/?wt.mc_id=youtube_26688_organicsocial_reactor&pivots=programming-language-python) finnes i dette arkivet under filene `xx-python-agent-framework` og `xx-dotnet-agent-framework`.

## Forstå Microsoft Agent Framework

![Framework Intro](../../../translated_images/no/framework-intro.077af16617cf130c.webp)

[Microsoft Agent Framework (MAF)](https://learn.microsoft.com/en-us/agent-framework/overview/?wt.mc_id=youtube_26688_organicsocial_reactor&pivots=programming-language-python) er Microsofts enhetlige rammeverk for å bygge AI-agenter. Det tilbyr fleksibilitet for å møte det brede utvalget av agent-baserte bruksområder som sees i både produksjons- og forskningsmiljøer, inkludert:

- **Sekvensiell agentorchestration** i scenarier der trinnvise arbeidsflyter er nødvendig.
- **Samtidig orchestration** i scenarier der agenter må fullføre oppgaver samtidig.
- **Gruppechat orchestration** i scenarier der agenter kan samarbeide om én oppgave.
- **Overlevering orchestration** i scenarier der agenter overleverer oppgaven til hverandre etterhvert som underoppgaver fullføres.
- **Magnetisk orchestration** i scenarier der en lederagent oppretter og endrer en oppgaveliste og håndterer koordineringen av underagenter for å fullføre oppgaven.

For å levere AI-agenter i produksjon har MAF også inkludert funksjoner for:

- **Observasjon** gjennom bruk av OpenTelemetry der hver handling til AI-agenten inkludert verktøysanrop, orkestreringssteg, resonnementflyter og ytelsesovervåkning via Microsoft Foundry-dashboards.
- **Sikkerhet** ved å kjøre agenter nativt på Microsoft Foundry som inkluderer sikkerhetskontroller som rollebasert tilgang, håndtering av private data og innebygd innholdssikkerhet.
- **Varighet** med agenttråder og arbeidsflyter som kan pause, gjenoppta og komme seg fra feil, noe som muliggjør lengre kjørende prosesser.
- **Kontroll** med menneske i løkka-arbeidsflyter der oppgaver merkes som krever menneskelig godkjenning.

Microsoft Agent Framework fokuserer også på interoperabilitet ved å:

- **Være skyuavhengig** - Agenter kan kjøre i containere, lokalt og på flere ulike skyer.
- **Være leverandøruavhengig** - Agenter kan opprettes med ditt foretrukne SDK inkludert Azure OpenAI og OpenAI
- **Integrere åpne standarder** - Agenter kan benytte protokoller som Agent-to-Agent (A2A) og Model Context Protocol (MCP) for å oppdage og bruke andre agenter og verktøy.
- **Plugins og koblinger** - Tilkoblinger kan gjøres til data- og minnetjenester som Microsoft Fabric, SharePoint, Pinecone og Qdrant.

La oss se på hvordan disse funksjonene anvendes på noen av de kjernebegrepene i Microsoft Agent Framework.

## Nøkkelkonsepter i Microsoft Agent Framework

### Agenter

![Agent Framework](../../../translated_images/no/agent-components.410a06daf87b4fef.webp)

**Opprette agenter**

Agentopprettelse gjøres ved å definere inferenstjenesten (LLM-leverandør), et
sett med instruksjoner AI-agenten skal følge, og et tilordnet `name`:

```python
agent = AzureOpenAIChatClient(credential=AzureCliCredential()).create_agent( instructions="You are good at recommending trips to customers based on their preferences.", name="TripRecommender" )
```

Ovenfor brukes `Azure OpenAI`, men agenter kan opprettes ved bruk av en rekke tjenester inkludert `Microsoft Foundry Agent Service`:

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

eller eksterne agenter som bruker A2A-protokollen:

```python
agent = A2AAgent( name=agent_card.name, description=agent_card.description, agent_card=agent_card, url="https://your-a2a-agent-host" )
```

**Kjøre agenter**

Agenter kjøres ved bruk av `.run` eller `.run_stream` metodene for henholdsvis ikke-strømmende eller strømmende svar.

```python
result = await agent.run("What are good places to visit in Amsterdam?")
print(result.text)
```

```python
async for update in agent.run_stream("What are the good places to visit in Amsterdam?"):
    if update.text:
        print(update.text, end="", flush=True)

```

Hver agentkjøring kan også ha alternativer for å tilpasse parametere som `max_tokens` brukt av agenten, `tools` som agenten kan kalle, og til og med selve `model` som brukes for agenten.

Dette er nyttig i tilfeller hvor spesifikke modeller eller verktøy kreves for å fullføre en brukers oppgave.

**Verktøy**

Verktøy kan defineres både når agenten opprettes:

```python
def get_attractions( location: Annotated[str, Field(description="The location to get the top tourist attractions for")], ) -> str: """Get the top tourist attractions for a given location.""" return f"The top attractions for {location} are." 


# Når du oppretter en ChatAgent direkte

agent = ChatAgent( chat_client=OpenAIChatClient(), instructions="You are a helpful assistant", tools=[get_attractions]

```

og også når agenten kjøres:

```python

result1 = await agent.run( "What's the best place to visit in Seattle?", tools=[get_attractions] # Verktøy levert kun for denne kjøringen )
```

**Agenttråder**

Agenttråder brukes til å håndtere samtaler med flere runder. Tråder kan opprettes enten ved:

- Bruke `get_new_thread()` som gjør at tråden kan lagres over tid
- Automatisk opprette en tråd når agenten kjører som kun varer under gjeldende kjøring.

For å opprette en tråd ser koden slik ut:

```python
# Opprett en ny tråd.
thread = agent.get_new_thread() # Kjør agenten med tråden.
response = await agent.run("Hello, I am here to help you book travel. Where would you like to go?", thread=thread)

```

Du kan deretter serialisere tråden for å lagres for senere bruk:

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

Agenter samhandler med verktøy og LLMs for å fullføre brukeroppgaver. I visse scenarier ønsker vi å utføre eller spore handlinger mellom disse interaksjonene. Agent middleware muliggjør dette gjennom:

*Funksjons-mellomvare*

Denne mellomvaren lar oss utføre en handling mellom agenten og en funksjon/verktøy den skal kalle. Et eksempel på bruk er hvis du vil logge funksjonskallet.

I koden under definerer `next` om neste mellomvare eller selve funksjonen skal kalles.

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

    # Etterbehandling: Logg etter AI-respons
    print("[Chat] AI response received")

```

**Agentminne**

Som dekket i leksjonen `Agentic Memory`, er minne et viktig element for å la agenten operere over ulike kontekster. MAF tilbyr flere ulike typer minner:

*Minne i minnet (In-Memory Storage)*

Dette er minnet som lagres i tråder under applikasjonskjøring.

```python
# Opprett en ny tråd.
thread = agent.get_new_thread() # Kjør agenten med tråden.
response = await agent.run("Hello, I am here to help you book travel. Where would you like to go?", thread=thread)
```

*Vedvarende meldinger*

Dette minnet brukes ved lagring av samtalehistorikk over flere økter. Det defineres med `chat_message_store_factory` :

```python
from agent_framework import ChatMessageStore

# Opprett et tilpasset meldingslager
def create_message_store():
    return ChatMessageStore()

agent = ChatAgent(
    chat_client=OpenAIChatClient(),
    instructions="You are a Travel assistant.",
    chat_message_store_factory=create_message_store
)

```

*Dynamisk minne*

Dette minnet legges til konteksten før agenter kjøres. Disse minnene kan lagres i eksterne tjenester som mem0:

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

**Agentobservasjon**

Observasjon er viktig for å bygge pålitelige og vedlikeholdbare agentbaserte systemer. MAF integreres med OpenTelemetry for å gi sporing og målere for bedre observasjon.

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

MAF tilbyr arbeidsflyter som er forhåndsdefinerte steg for å fullføre en oppgave, og inkluderer AI-agenter som komponenter i disse stegene.

Arbeidsflyter består av ulike komponenter som tillater bedre kontrollflyt. Arbeidsflyter muliggjør også **multi-agent orchestrering** og **checkpointing** for å lagre tilstander i arbeidsflyter.

Kjernekomponentene i en arbeidsflyt er:

**Utførere (Executors)**

Utførere mottar innkommende meldinger, utfører sine oppgaver, og produserer en utgående melding. Dette beveger arbeidsflyten fremover mot å fullføre den større oppgaven. Utførere kan være AI-agent eller egendefinert logikk.

**Kanter (Edges)**

Kanter brukes for å definere flyten av meldinger i en arbeidsflyt. Disse kan være:

*Direkte kanter* - Enkle en-til-en koblinger mellom utførere:

```python
from agent_framework import WorkflowBuilder

builder = WorkflowBuilder()
builder.add_edge(source_executor, target_executor)
builder.set_start_executor(source_executor)
workflow = builder.build()
```

*Betingede kanter* - Aktiveres når en bestemt betingelse er oppfylt. For eksempel kan en utfører foreslå andre alternativer når hotellrom ikke er tilgjengelige.

*Switch-case kanter* - Ruter meldinger til ulike utførere basert på definerte betingelser. For eksempel hvis en reise kunde har prioritert tilgang og oppgavene deres håndteres gjennom en annen arbeidsflyt.

*Fan-out kanter* - Sender én melding til flere mottakere.

*Fan-in kanter* - Samler flere meldinger fra ulike utførere og sender til én mottaker.

**Hendelser (Events)**

For å gi bedre observasjon i arbeidsflyter tilbyr MAF innebygde hendelser for utførelse som inkluderer:

- `WorkflowStartedEvent`  - Arbeidsflytutførelse starter
- `WorkflowOutputEvent` - Arbeidsflyt produserer et utdata
- `WorkflowErrorEvent` - Arbeidsflyt støter på en feil
- `ExecutorInvokeEvent`  - Utfører starter prosessering
- `ExecutorCompleteEvent`  -  Utfører fullfører prosessering
- `RequestInfoEvent` - En forespørsel gis ut

## Avanserte MAF-mønstre

Seksjonene ovenfor dekker nøkkelkonseptene i Microsoft Agent Framework. Når du bygger mer komplekse agenter, her er noen avanserte mønstre å vurdere:

- **Mellomvarekomposisjon**: Kjede flere mellomvarehåndterere (logging, autentisering, ratelimiting) ved bruk av funksjons- og chat-mellomvare for finmasket kontroll over agentadferd.
- **Arbeidsflytcheckpointing**: Bruk arbeidsflythendelser og serialisering for å lagre og gjenoppta langtidskjørende agentprosesser.
- **Dynamisk verktøyvalg**: Kombinér RAG over verktøybeskrivelser med MAFs verktøyregistrering for å presentere kun relevante verktøy per forespørsel.
- **Multi-agent overlevering**: Bruk arbeidsflytkanter og betinget ruting for å orkestrere overleveringer mellom spesialiserte agenter.

## Kjøre LangChain / LangGraph-agenter på Microsoft Foundry

Microsoft Agent Framework er **rammeverks-interopabel** — du er ikke begrenset til agenter skrevet med MAF. Hvis du allerede har en agent bygd med **LangChain** eller **LangGraph**, kan du kjøre den som en **Microsoft Foundry-hostet agent** slik at Foundry håndterer runtime, økter, skalering, identitet og protokollendepunkter for deg, mens agentlogikken din forblir i LangGraph.

Dette gjøres med `langchain_azure_ai.agents.hosting`-pakken, som eksponerer en kompilert LangGraph-graf over de samme protokollene som Foundry-hostede agenter bruker.

**1. Installer hosting-ekstra:**

```bash
pip install -U "langchain-azure-ai[hosting]>=1.2.4" azure-identity
```

`hosting`-ekstraen installerer Foundry-protokollbibliotekene: `azure-ai-agentserver-responses` (det OpenAI-kompatible `/responses` endepunktet) og `azure-ai-agentserver-invocations` (det generiske `/invocations` endepunktet).

**2. Velg en hostingprotokoll:**

| Protokoll | Vertklasse | Endepunkt | Bruk når |
|----------|-----------|----------|----------|
| **Responses** | `ResponsesHostServer` | `/responses` | Du ønsker OpenAI-kompatibel chat, streaming, svarhistorikk og samtaletasking — anbefalt standard for konversasjonelle agenter. |
| **Invocations** | `InvocationsHostServer` | `/invocations` | Du trenger et tilpasset JSON-format, et webhook-stil endepunkt eller ikke-konversasjonell prosessering. |

Fordi **Responses API er den primære API for agentstil utvikling i Foundry**, start med `ResponsesHostServer` for de fleste agenter.

**3. Konfigurer miljøvariabler** (`az login` først slik at `DefaultAzureCredential` kan autentisere):

```bash
export FOUNDRY_PROJECT_ENDPOINT="https://<resource>.services.ai.azure.com/api/projects/<project>"
export FOUNDRY_MODEL_NAME="gpt-5-mini"
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

**Nøkkeladferd:**

- **Samtaler**: Klienter fortsetter en samtale ved å sende `previous_response_id` eller en `conversation` ID. Hvis grafen din er kompilert med en LangGraph sjekkpointer, nøkkelsattes samtalestatus i Foundry til sjekkpunktet (bruk en varig sjekkpointer i produksjon; `MemorySaver` fungerer fint for lokal testing).
- **Menneske i løkka**: Hvis grafen bruker LangGraph `interrupt()`, eksponerer `ResponsesHostServer` den ventende avbruddet som et Responses `function_call` / `mcp_approval_request` element, og klienter fortsetter med et tilsvarende `function_call_output` / `mcp_approval_response`.
- **Distribuer til Foundry**: Bruk Azure Developer CLI — `azd ext install azure.ai.agents`, `azd ai agent init -m <manifest>`, `azd ai agent run` (lokalt, krever Docker), deretter `azd provision` og `azd deploy`. Distribusjon av hostet agent krever **Foundry Project Manager**-rollen.

En kjørbar versjon av dette eksempelet finnes i [code-samples/14-langchain-hosted-agent.py](../../../14-microsoft-agent-framework/code-samples/14-langchain-hosted-agent.py). For full gjennomgang (Invocations-protokoll, tilpassede forespørselskjemaer og feilsøking), se [Host LangGraph agents as Foundry hosted agents](https://learn.microsoft.com/azure/foundry/how-to/develop/langchain-hosted-agents).

## Kodeeksempler 

Kodeeksempler for Microsoft Agent Framework kan finnes i dette arkivet under filene `xx-python-agent-framework` og `xx-dotnet-agent-framework`.

## Har du flere spørsmål om Microsoft Agent Framework?

Bli med i [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D) for å møte andre lærende, delta på kontortimer og få svar på spørsmål om AI-agenter.
## Forrige leksjon

[Memory for AI Agents](../13-agent-memory/README.md)

## Neste leksjon

[Building Computer Use Agents (CUA)](../15-browser-use/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfraskrivelse**:
Dette dokumentet er oversatt ved hjelp av AI-oversettelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selv om vi streber etter nøyaktighet, vær oppmerksom på at automatiske oversettelser kan inneholde feil eller unøyaktigheter. Det opprinnelige dokumentet på originalspråket skal betraktes som den autoritative kilden. For kritisk informasjon anbefales profesjonell menneskelig oversettelse. Vi er ikke ansvarlige for eventuelle misforståelser eller feiltolkninger som oppstår ved bruk av denne oversettelsen.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->