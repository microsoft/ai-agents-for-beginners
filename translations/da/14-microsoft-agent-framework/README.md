# Udforskning af Microsoft Agent Framework

![Agent Framework](../../../translated_images/da/lesson-14-thumbnail.90df0065b9d234ee.webp)

### Introduktion

Denne lektion omfatter:

- Forståelse af Microsoft Agent Framework: Nøglefunktioner og Værdi  
- Udforskning af de vigtigste begreber i Microsoft Agent Framework
- Avancerede MAF-mønstre: Arbejdsgange, Middleware og Hukommelse

## Læringsmål

Efter at have gennemført denne lektion vil du vide, hvordan du:

- Bygger produktionsklare AI-agenter ved hjælp af Microsoft Agent Framework
- Anvender kernefunktionerne i Microsoft Agent Framework til dine agentiske brugsscenarier
- Bruger avancerede mønstre inklusive arbejdsgange, middleware og observabilitet

## Kodeeksempler 

Kodeeksempler for [Microsoft Agent Framework (MAF)](https://aka.ms/ai-agents-beginners/agent-framework) kan findes i dette repository under filerne `xx-python-agent-framework` og `xx-dotnet-agent-framework`.

## Forståelse af Microsoft Agent Framework

![Framework Intro](../../../translated_images/da/framework-intro.077af16617cf130c.webp)

[Microsoft Agent Framework (MAF)](https://aka.ms/ai-agents-beginners/agent-framework) er Microsofts samlede rammeværk til at bygge AI-agenter. Det tilbyder fleksibilitet til at håndtere den brede variation af agentiske brugsscenarier, som ses både i produktion og forskningsmiljøer, herunder:

- **Sekventiel agent-orchestration** i scenarier, hvor trin-for-trin arbejdsgange er nødvendige.
- **Samtidig orchestration** i scenarier, hvor agenter skal fuldføre opgaver samtidig.
- **Gruppesamtale-orchestration** i scenarier, hvor agenter kan samarbejde om en opgave.
- **Overlevering/ Handoff orchestration** i scenarier, hvor agenter overleverer opgaver til hinanden, efterhånden som delopgaver fuldføres.
- **Magnetisk orchestration** i scenarier, hvor en manager-agent opretter og ændrer en opgaveliste og håndterer koordineringen af underagenter til at fuldføre opgaven.

For at levere AI-agenter i produktion indeholder MAF også funktioner til:

- **Observabilitet** via brug af OpenTelemetry, hvor hver handling af AI-agenten, inklusive værktøjskald, orchestrationstrin, ræsonneringsflows og ydeevnemåling, sker gennem Microsoft Foundry dashboards.
- **Sikkerhed** ved at hoste agenter nativt på Microsoft Foundry, som inkluderer sikkerhedskontroller såsom rollebaseret adgang, håndtering af privat data og indbygget indholdssikkerhed.
- **Holdbarhed** da agenttråde og arbejdsgange kan pause, genoptage og komme sig efter fejl, hvilket muliggør længerevarende processer.
- **Kontrol**, da human-in-the-loop arbejdsgange understøttes, hvor opgaver markeres som krævende menneskelig godkendelse.

Microsoft Agent Framework fokuserer også på at være interoperabel ved at:

- **Være cloud-agnostisk** - Agenter kan køre i containere, lokalt (on-prem) og på tværs af flere forskellige clouds.
- **Være udbyder-agnostisk** - Agenter kan oprettes via dit foretrukne SDK, herunder Azure OpenAI og OpenAI
- **Integrere åbne standarder** - Agenter kan bruge protokoller såsom Agent-to-Agent (A2A) og Model Context Protocol (MCP) til at finde og bruge andre agenter og værktøjer.
- **Plugins og Connectors** - Forbindelser kan oprettes til data- og hukommelsestjenester som Microsoft Fabric, SharePoint, Pinecone og Qdrant.

Lad os se på, hvordan disse funktioner anvendes på nogle af kernebegreberne i Microsoft Agent Framework.

## Centrale Begreber i Microsoft Agent Framework

### Agenter

![Agent Framework](../../../translated_images/da/agent-components.410a06daf87b4fef.webp)

**Oprettelse af agenter**

Agentoprettelse sker ved at definere inferencetjenesten (LLM-udbyder), et
sæt instruktioner for AI-agenten at følge, og et tildelt `name`:

```python
agent = AzureOpenAIChatClient(credential=AzureCliCredential()).create_agent( instructions="You are good at recommending trips to customers based on their preferences.", name="TripRecommender" )
```

Ovenstående bruger `Azure OpenAI`, men agenter kan oprettes ved brug af en række tjenester, herunder `Microsoft Foundry Agent Service`:

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

Agenter køres ved hjælp af `.run` eller `.run_stream` metoderne for enten ikke-streamende eller streamende svar.

```python
result = await agent.run("What are good places to visit in Amsterdam?")
print(result.text)
```

```python
async for update in agent.run_stream("What are the good places to visit in Amsterdam?"):
    if update.text:
        print(update.text, end="", flush=True)

```

Hver agentkørsel kan også have muligheder for at tilpasse parametre såsom `max_tokens`, der bruges af agenten, `tools`, som agenten kan kalde, og endda den `model` selv, som agenten anvender.

Dette er nyttigt i tilfælde, hvor specifikke modeller eller værktøjer kræves for at fuldføre brugerens opgave.

**Værktøjer**

Værktøjer kan defineres både ved oprettelse af agenten:

```python
def get_attractions( location: Annotated[str, Field(description="The location to get the top tourist attractions for")], ) -> str: """Get the top tourist attractions for a given location.""" return f"The top attractions for {location} are." 


# Når du opretter en ChatAgent direkte

agent = ChatAgent( chat_client=OpenAIChatClient(), instructions="You are a helpful assistant", tools=[get_attractions]

```

og også når agenten kører:

```python

result1 = await agent.run( "What's the best place to visit in Seattle?", tools=[get_attractions] # Værktøj leveret kun til denne kørsel )
```

**Agent Threads**

Agent Threads bruges til at håndtere samtaler med flere runder. Tråde kan oprettes enten ved:

- Brug af `get_new_thread()`, som gør det muligt at gemme tråden over tid
- Automatisk at oprette en tråd, når en agent kører, og tråden kun varer under den aktuelle kørsel.

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

Agenter interagerer med værktøjer og LLM'er for at fuldføre brugeropgaver. I visse scenarier ønsker vi at udføre eller spore handlinger mellem disse interaktioner. Agent middleware muliggør dette gennem:

*Funktion Middleware*

Denne middleware giver os mulighed for at udføre en handling mellem agenten og en funktion/værktøj, som den vil kalde. Et eksempel på brug er, når du ønsker at logge på funktionskaldet.

I koden nedenfor definerer `next`, om den næste middleware eller den faktiske funktion skal kaldes.

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

Denne middleware giver os mulighed for at udføre eller logge en handling mellem agenten og forespørgsler mellem LLM.

Dette indeholder vigtig information såsom de `messages`, der sendes til AI-tjenesten.

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

**Agent Hukommelse**

Som dækket i `Agentisk Hukommelse`-lektionen, er hukommelse et vigtigt element for at muliggøre agentens arbejde over forskellige kontekster. MAF tilbyder flere forskellige typer hukommelser:

*In-Memory Storage*

Dette er hukommelsen, der gemmes i tråde under applikationens runtime.

```python
# Opret en ny tråd.
thread = agent.get_new_thread() # Kør agenten med tråden.
response = await agent.run("Hello, I am here to help you book travel. Where would you like to go?", thread=thread)
```

*Persistent Messages*

Denne hukommelse bruges til at gemme samtalehistorik på tværs af sessioner. Den defineres ved hjælp af `chat_message_store_factory`:

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

*Dynamisk Hukommelse*

Denne hukommelse føjes til konteksten, før agenter kører. Disse hukommelser kan gemmes i eksterne tjenester såsom mem0:

```python
from agent_framework.mem0 import Mem0Provider

# Brug af Mem0 til avancerede hukommelsesfunktioner
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

Observabilitet er vigtig for at bygge pålidelige og vedligeholdelsesvenlige agentiske systemer. MAF integrerer med OpenTelemetry for at levere tracing og metere til bedre observabilitet.

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

MAF tilbyder arbejdsgange, der er foruddefinerede trin til at fuldføre en opgave og inkluderer AI-agenter som komponenter i disse trin.

Arbejdsgange består af forskellige komponenter, der tillader bedre kontrolflow. Arbejdsgange muliggør også **multi-agent orchestration** og **checkpointing** til at gemme arbejdsgangstilstande.

Kernekomponenterne i en arbejdsgang er:

**Executors**

Executors modtager indgående beskeder, udfører deres tildelte opgaver, og producerer derefter en udgående besked. Dette fører arbejdsgangen frem mod fuldførelsen af den større opgave. Executors kan være enten AI-agenter eller brugerdefineret logik.

**Edges**

Edges bruges til at definere flowet af beskeder i en arbejdsgang. Disse kan være:

*Direkte Edges* - Enkle en-til-en forbindelser mellem executors:

```python
from agent_framework import WorkflowBuilder

builder = WorkflowBuilder()
builder.add_edge(source_executor, target_executor)
builder.set_start_executor(source_executor)
workflow = builder.build()
```

*Betingede Edges* - Aktiveres efter at en bestemt betingelse er opfyldt. For eksempel, når hotelværelser ikke er tilgængelige, kan en executor foreslå andre muligheder.

*Switch-case Edges* - Sender beskeder til forskellige executors baseret på definerede betingelser. For eksempel, hvis en rejsekunde har prioriteret adgang, håndteres deres opgaver gennem en anden arbejdsgang.

*Fan-out Edges* - Sender én besked til flere modtagere.

*Fan-in Edges* - Samler flere beskeder fra forskellige executors og sender til én modtager.

**Events**

For at give bedre observabilitet i arbejdsgange tilbyder MAF indbyggede events for eksekvering, herunder:

- `WorkflowStartedEvent`  - Arbejdsgangseksekvering begynder
- `WorkflowOutputEvent` - Arbejdsgang producerer output
- `WorkflowErrorEvent` - Arbejdsgang støder på en fejl
- `ExecutorInvokeEvent`  - Executor starter behandling
- `ExecutorCompleteEvent`  - Executor afslutter behandling
- `RequestInfoEvent` - En anmodning udføres

## Avancerede MAF-mønstre

Sektionerne ovenfor dækker de centrale begreber i Microsoft Agent Framework. Når du bygger mere komplekse agenter, er her nogle avancerede mønstre at overveje:

- **Middleware-komposition**: Kæd flere middleware-handlere (logning, autentificering, rate-begrænsning) sammen ved at bruge funktion og chat-middleware for detaljeret kontrol over agentadfærd.
- **Workflow Checkpointing**: Brug workflow-events og serialisering til at gemme og genoptage langvarige agentprocesser.
- **Dynamisk værktøjsvalg**: Kombinér RAG over værktøjsbeskrivelser med MAF's værktøjsregistrering for kun at præsentere relevante værktøjer pr. forespørgsel.
- **Multi-agent hånd-off**: Brug workflow-edges og betinget routing til at orkestrere overleveringer mellem specialiserede agenter.

## Hosting af LangChain / LangGraph-agenter på Microsoft Foundry

Microsoft Agent Framework er **framework-interoperabelt** — du er ikke begrænset til agenter skrevet med MAF. Hvis du allerede har en agent bygget med **LangChain** eller **LangGraph**, kan du køre den som en **Microsoft Foundry-hostet agent**, så Foundry administrerer runtime, sessioner, skalering, identitet og protokolendepunkter for dig, mens din agentlogik forbliver i LangGraph.

Dette gøres med `langchain_azure_ai.agents.hosting`-pakken, som eksponerer en kompileret LangGraph-graf over de samme protokoller, som Foundry-hostede agenter bruger.

**1. Installer hosting-udvidelsen:**

```bash
pip install -U "langchain-azure-ai[hosting]>=1.2.4" azure-identity
```

`hosting`-udvidelsen installerer Foundry-protokolbibliotekerne: `azure-ai-agentserver-responses` (det OpenAI-kompatible `/responses` endpoint) og `azure-ai-agentserver-invocations` (det generiske `/invocations` endpoint).

**2. Vælg en hosting-protokol:**

| Protokol | Host-klasse | Endpoint | Bruges når |
|----------|-------------|----------|-------------|
| **Responses** | `ResponsesHostServer` | `/responses` | Du ønsker OpenAI-kompatibel chat, streaming, svarhistorik og samtaletråde — den anbefalede standard for konversationelle agenter. |
| **Invocations** | `InvocationsHostServer` | `/invocations` | Du har behov for et brugerdefineret JSON-format, et webhook-lignende endpoint eller ikke-konversationel behandling. |

Fordi **Responses API er den primære API for agent-stil udvikling i Foundry**, start med `ResponsesHostServer` for de fleste agenter.

**3. Konfigurer miljøvariabler** (`az login` først, så `DefaultAzureCredential` kan autentificere):

```bash
export FOUNDRY_PROJECT_ENDPOINT="https://<resource>.services.ai.azure.com/api/projects/<project>"
export FOUNDRY_MODEL_NAME="gpt-5-mini"
```

Når agenten senere kører som hostet agent i Foundry, indsætter platformen `FOUNDRY_PROJECT_ENDPOINT` automatisk.

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

    # ChatOpenAI her retter sig mod Foundry-projektets OpenAI-kompatible (Respons) slutpunkt.
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

Kør den lokalt med `python main.py`, og send derefter en Responses-forespørgsel til `http://localhost:8088/responses`.

**Nøgleadfærd:**

- **Samtaler**: Klienter fortsætter en samtale ved at sende `previous_response_id` eller en `conversation` ID. Hvis din graf er komplieret med en LangGraph-checkpointer, binder Foundry samtaletilstanden til checkpointen (brug en holdbar checkpointer i produktion; `MemorySaver` er fin til lokal test).
- **Human-in-the-loop**: Hvis din graf bruger LangGraph `interrupt()`, viser `ResponsesHostServer` den ventende afbrydelse som et Responses `function_call` / `mcp_approval_request` element, og klienter genoptager med et tilsvarende `function_call_output` / `mcp_approval_response`.
- **Deploy til Foundry**: Brug Azure Developer CLI — `azd ext install azure.ai.agents`, `azd ai agent init -m <manifest>`, `azd ai agent run` (lokalt, kræver Docker), derefter `azd provision` og `azd deploy`. Hostet-agent-implementering kræver **Foundry Project Manager**-rollen.

En kørbar version af dette eksempel findes i [code-samples/14-langchain-hosted-agent.py](../../../14-microsoft-agent-framework/code-samples/14-langchain-hosted-agent.py). For fuld gennemgang (Invocations-protokol, brugerdefinerede anmodningsskemaer og fejlfinding), se [Host LangGraph agents as Foundry hosted agents](https://learn.microsoft.com/azure/foundry/how-to/develop/langchain-hosted-agents).

## Kodeeksempler 

Kodeeksempler for Microsoft Agent Framework kan findes i dette repository under filerne `xx-python-agent-framework` og `xx-dotnet-agent-framework`.

## Har du flere spørgsmål om Microsoft Agent Framework?

Deltag i [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D) for at mødes med andre lærende, deltage i vejledningssamtaler og få besvaret dine spørgsmål om AI-agenter.
## Forrige lektion

[Memory for AI Agents](../13-agent-memory/README.md)

## Næste lektion

[Bygning af Computer Use Agents (CUA)](../15-browser-use/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfraskrivelse**:
Dette dokument er blevet oversat ved hjælp af AI-oversættelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selvom vi bestræber os på nøjagtighed, skal du være opmærksom på, at automatiserede oversættelser kan indeholde fejl eller unøjagtigheder. Det originale dokument på dets oprindelige sprog bør betragtes som den autoritative kilde. For kritisk information anbefales professionel menneskelig oversættelse. Vi påtager os intet ansvar for misforståelser eller fejltolkninger, der opstår som følge af brugen af denne oversættelse.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->