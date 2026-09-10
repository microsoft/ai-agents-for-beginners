# Verkennen van het Microsoft Agent Framework

![Agent Framework](../../../translated_images/nl/lesson-14-thumbnail.90df0065b9d234ee.webp)

### Introductie

Deze les behandelt:

- Inzicht in Microsoft Agent Framework: Belangrijkste kenmerken en waarde  
- Verkenning van de kernconcepten van Microsoft Agent Framework
- Geavanceerde MAF-patronen: Workflows, Middleware en Geheugen

## Leerdoelen

Na het voltooien van deze les weet je hoe je:

- Productieklaar AI-agents bouwt met Microsoft Agent Framework
- De kernfuncties van Microsoft Agent Framework toepast op jouw agent-georiënteerde use-cases
- Geavanceerde patronen gebruikt, waaronder workflows, middleware en observability

## Codevoorbeelden 

Codevoorbeelden voor [Microsoft Agent Framework (MAF)](https://learn.microsoft.com/en-us/agent-framework/overview/?wt.mc_id=youtube_26688_organicsocial_reactor&pivots=programming-language-python) zijn te vinden in deze repository onder de bestanden `xx-python-agent-framework` en `xx-dotnet-agent-framework`.

## Inzicht in Microsoft Agent Framework

![Framework Intro](../../../translated_images/nl/framework-intro.077af16617cf130c.webp)

[Microsoft Agent Framework (MAF)](https://learn.microsoft.com/en-us/agent-framework/overview/?wt.mc_id=youtube_26688_organicsocial_reactor&pivots=programming-language-python) is het verenigde framework van Microsoft voor het bouwen van AI-agenten. Het biedt de flexibiliteit om de grote verscheidenheid aan agent-georiënteerde gebruikssituaties aan te pakken die zowel in productie als onderzoeksomgevingen voorkomen, waaronder:

- **Sequentiële agentorkestratie** in scenario's waar stapsgewijze workflows nodig zijn.
- **Gelijktijdige orkestratie** in scenario's waar agenten taken tegelijkertijd moeten voltooien.
- **Groepschat-orkestratie** in scenario's waar agenten samen aan één taak kunnen samenwerken.
- **Overdrachtsorkestratie** in scenario's waar agenten de taak aan elkaar overdragen naarmate subtaken worden voltooid.
- **Magnetische orkestratie** in scenario's waar een manageragent een takenlijst maakt en wijzigt en de coördinatie van subagenten afhandelt om de taak te voltooien.

Om AI-agenten in productie te leveren, bevat MAF ook functies voor:

- **Observability** via het gebruik van OpenTelemetry, waarbij elke actie van de AI-agent wordt gevolgd, inclusief tool-aanroepen, orkestratiestappen, redeneerstromen en prestatiemonitoring via Microsoft Foundry dashboards.
- **Beveiliging** door agenten native te hosten op Microsoft Foundry, dat beveiligingscontroles biedt zoals rolgebaseerde toegang, privégegevensverwerking en ingebouwde contentveiligheid.
- **Duurzaamheid** doordat agentthreads en workflows kunnen pauzeren, hervatten en herstellen van fouten, wat langere processen mogelijk maakt.
- **Controle** doordat workflows met menselijke tussenkomst worden ondersteund waarbij taken worden gemarkeerd als zijnde goedkeuringsplichtig door een mens.

Microsoft Agent Framework richt zich ook op interoperabiliteit door:

- **Cloud-onafhankelijk te zijn** - agenten kunnen draaien in containers, on-premises en op meerdere verschillende clouds.
- **Provider-onafhankelijk te zijn** - agenten kunnen gemaakt worden via jouw voorkeurs-SDK, waaronder Azure OpenAI en OpenAI.
- **Open standaarden te integreren** - agenten kunnen protocollen gebruiken zoals Agent-to-Agent (A2A) en Model Context Protocol (MCP) om andere agenten en tools te ontdekken en te gebruiken.
- **Plugins en Connectors** - connecties kunnen worden gemaakt naar data- en geheugenservices zoals Microsoft Fabric, SharePoint, Pinecone en Qdrant.

Laten we bekijken hoe deze functies worden toegepast op enkele kernconcepten van Microsoft Agent Framework.

## Kernconcepten van Microsoft Agent Framework

### Agenten

![Agent Framework](../../../translated_images/nl/agent-components.410a06daf87b4fef.webp)

**Agenten maken**

Het maken van agenten gebeurt door het definiëren van de inference service (LLM-provider), een
reeks instructies voor de AI-agent om te volgen, en een toegewezen `name`:

```python
agent = AzureOpenAIChatClient(credential=AzureCliCredential()).create_agent( instructions="You are good at recommending trips to customers based on their preferences.", name="TripRecommender" )
```

Bovenstaand gebruikt `Azure OpenAI` maar agenten kunnen ook worden gemaakt met behulp van diverse services zoals `Microsoft Foundry Agent Service`:

```python
AzureAIAgentClient(async_credential=credential).create_agent( name="HelperAgent", instructions="You are a helpful assistant." ) as agent
```

OpenAI `Responses`, `ChatCompletion` APIs

```python
agent = OpenAIResponsesClient().create_agent( name="WeatherBot", instructions="You are a helpful weather assistant.", )
```

```python
agent = OpenAIChatClient().create_agent( name="HelpfulAssistant", instructions="You are a helpful assistant.", )
```

of [MiniMax](https://platform.minimaxi.com/), dat een OpenAI-compatibele API biedt met grote contextvensters (tot 204K tokens):

```python
agent = OpenAIChatClient(base_url="https://api.minimax.io/v1", api_key=os.environ["MINIMAX_API_KEY"], model_id="MiniMax-M3").create_agent( name="HelpfulAssistant", instructions="You are a helpful assistant.", )
```

of remote agenten via het A2A-protocol:

```python
agent = A2AAgent( name=agent_card.name, description=agent_card.description, agent_card=agent_card, url="https://your-a2a-agent-host" )
```

**Agenten uitvoeren**

Agenten worden uitgevoerd met de `.run` of `.run_stream` methodes voor respectievelijk niet-streaming of streaming antwoorden.

```python
result = await agent.run("What are good places to visit in Amsterdam?")
print(result.text)
```

```python
async for update in agent.run_stream("What are the good places to visit in Amsterdam?"):
    if update.text:
        print(update.text, end="", flush=True)

```

Elke agent-run kan ook opties bevatten om parameters aan te passen zoals `max_tokens` die door de agent worden gebruikt, `tools` die de agent kan aanroepen, en zelfs het `model` zelf dat voor de agent wordt gebruikt.

Dit is nuttig in situaties waarin specifieke modellen of tools nodig zijn om een taak van de gebruiker te voltooien.

**Tools**

Tools kunnen worden gedefinieerd zowel bij het definiëren van de agent:

```python
def get_attractions( location: Annotated[str, Field(description="The location to get the top tourist attractions for")], ) -> str: """Get the top tourist attractions for a given location.""" return f"The top attractions for {location} are." 


# Bij het direct aanmaken van een ChatAgent

agent = ChatAgent( chat_client=OpenAIChatClient(), instructions="You are a helpful assistant", tools=[get_attractions]

```

als ook bij het uitvoeren van de agent:

```python

result1 = await agent.run( "What's the best place to visit in Seattle?", tools=[get_attractions] # Hulpmiddel alleen beschikbaar voor deze run )
```

**Agent Threads**

Agent Threads worden gebruikt om multi-turn gesprekken af te handelen. Threads kunnen worden gemaakt door:

- Gebruik te maken van `get_new_thread()` waarmee de thread in de loop van de tijd kan worden opgeslagen
- Automatisch een thread te creëren wanneer een agent wordt uitgevoerd en waarbij de thread alleen tijdens de huidige uitvoering bestaat.

Om een thread te maken, ziet de code er als volgt uit:

```python
# Maak een nieuwe thread aan.
thread = agent.get_new_thread() # Voer de agent uit met de thread.
response = await agent.run("Hello, I am here to help you book travel. Where would you like to go?", thread=thread)

```

Je kunt de thread vervolgens serialiseren om deze later op te slaan:

```python
# Maak een nieuwe thread aan.
thread = agent.get_new_thread() 

# Voer de agent uit met de thread.

response = await agent.run("Hello, how are you?", thread=thread) 

# Seriëleer de thread voor opslag.

serialized_thread = await thread.serialize() 

# Deserialiseer de thread status na het laden uit opslag.

resumed_thread = await agent.deserialize_thread(serialized_thread)
```

**Agent Middleware**

Agenten communiceren met tools en LLM's om taken van gebruikers te voltooien. In bepaalde scenario's willen we tussen deze interacties acties uitvoeren of volgen. Agent middleware stelt ons hierbij in staat door:

*Function Middleware*

Deze middleware maakt het mogelijk om een actie uit te voeren tussen de agent en een functie/tool die wordt aangeroepen. Een voorbeeld hiervan is wanneer je bijvoorbeeld logging wilt uitvoeren op de functie-aanroep.

In de onderstaande code bepaalt `next` of de volgende middleware of de daadwerkelijke functie wordt aangeroepen.

```python
async def logging_function_middleware(
    context: FunctionInvocationContext,
    next: Callable[[FunctionInvocationContext], Awaitable[None]],
) -> None:
    """Function middleware that logs function execution."""
    # Voorbewerking: Loggen vóór functieverwerking
    print(f"[Function] Calling {context.function.name}")

    # Ga verder naar de volgende middleware of functieverwerking
    await next(context)

    # Nabewerking: Loggen na functieverwerking
    print(f"[Function] {context.function.name} completed")
```

*Chat Middleware*

Deze middleware maakt het mogelijk om een actie uit te voeren of te loggen tussen de agent en de verzoeken aan de LLM.

Dit bevat belangrijke informatie zoals de `messages` die naar de AI-service worden gestuurd.

```python
async def logging_chat_middleware(
    context: ChatContext,
    next: Callable[[ChatContext], Awaitable[None]],
) -> None:
    """Chat middleware that logs AI interactions."""
    # Voorverwerking: Loggen vóór AI-aanroep
    print(f"[Chat] Sending {len(context.messages)} messages to AI")

    # Ga verder naar de volgende middleware of AI-service
    await next(context)

    # Nazorg: Loggen na AI-respons
    print("[Chat] AI response received")

```

**Agentgeheugen**

Zoals behandeld in de les `Agentic Memory`, is geheugen een belangrijk element om de agent te laten opereren over verschillende contexten. MAF biedt verschillende soorten geheugen:

*In-Memory Opslag*

Dit is het geheugen dat tijdens de runtime van de applicatie in threads wordt opgeslagen.

```python
# Maak een nieuwe thread aan.
thread = agent.get_new_thread() # Voer de agent uit met de thread.
response = await agent.run("Hello, I am here to help you book travel. Where would you like to go?", thread=thread)
```

*Persistent Messages*

Dit geheugen wordt gebruikt om gespreksgeschiedenis op te slaan over verschillende sessies heen. Het wordt gedefinieerd met behulp van de `chat_message_store_factory`:

```python
from agent_framework import ChatMessageStore

# Maak een aangepaste berichtopslag
def create_message_store():
    return ChatMessageStore()

agent = ChatAgent(
    chat_client=OpenAIChatClient(),
    instructions="You are a Travel assistant.",
    chat_message_store_factory=create_message_store
)

```

*Dynamisch geheugen*

Dit geheugen wordt toegevoegd aan de context voordat agenten worden uitgevoerd. Deze geheugens kunnen worden opgeslagen in externe services zoals mem0:

```python
from agent_framework.mem0 import Mem0Provider

# Mem0 gebruiken voor geavanceerde geheugenmogelijkheden
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

**Agent observability**

Observability is belangrijk voor het bouwen van betrouwbare en onderhoudbare agent-gebaseerde systemen. MAF integreert met OpenTelemetry om tracing en meters te bieden voor betere observability.

```python
from agent_framework.observability import get_tracer, get_meter

tracer = get_tracer()
meter = get_meter()
with tracer.start_as_current_span("my_custom_span"):
    # doe iets
    pass
counter = meter.create_counter("my_custom_counter")
counter.add(1, {"key": "value"})
```

### Workflows

MAF biedt workflows die vooraf gedefinieerde stappen zijn om een taak te voltooien en waarin AI-agenten als componenten in die stappen zijn opgenomen.

Workflows bestaan uit verschillende componenten die betere stroomregeling mogelijk maken. Workflows ondersteunen ook **multi-agent orkestratie** en **checkpointing** om workflowstatussen op te slaan.

De kerncomponenten van een workflow zijn:

**Executors**

Executors ontvangen inputberichten, voeren hun toegewezen taken uit en produceren vervolgens een outputbericht. Dit brengt de workflow vooruit naar het voltooien van de grotere taak. Executors kunnen AI-agenten zijn of aangepaste logica.

**Edges**

Edges worden gebruikt om de stroom van berichten in een workflow te definiëren. Deze kunnen zijn:

*Directe Edges* - Simpele één-op-één verbindingen tussen executors:

```python
from agent_framework import WorkflowBuilder

builder = WorkflowBuilder()
builder.add_edge(source_executor, target_executor)
builder.set_start_executor(source_executor)
workflow = builder.build()
```

*Conditionele Edges* - Worden geactiveerd nadat aan een bepaalde voorwaarde is voldaan. Bijvoorbeeld, wanneer hotelkamers niet beschikbaar zijn, kan een executor andere opties suggereren.

*Switch-case Edges* - Routeren berichten naar verschillende executors op basis van gedefinieerde voorwaarden. Bijvoorbeeld als een reiziger prioriteits toegang heeft en zijn/haar taken via een andere workflow zullen worden afgehandeld.

*Fan-out Edges* - Verzend één bericht naar meerdere bestemmingen.

*Fan-in Edges* - Verzamel meerdere berichten van verschillende executors en stuur naar één bestemming.

**Events**

Om betere observability in workflows te bieden, biedt MAF ingebouwde events voor uitvoering, waaronder:

- `WorkflowStartedEvent`  - Workflow-uitvoering begint
- `WorkflowOutputEvent` - Workflow produceert een output
- `WorkflowErrorEvent` - Workflow ondervindt een fout
- `ExecutorInvokeEvent`  - Executor start verwerking
- `ExecutorCompleteEvent`  -  Executor voltooit verwerking
- `RequestInfoEvent` - Een verzoek wordt uitgegeven

## Geavanceerde MAF-patronen

De bovenstaande secties behandelen de kernconcepten van Microsoft Agent Framework. Naarmate je complexere agenten bouwt, zijn hier enkele geavanceerde patronen om te overwegen:

- **Middlewarecompositie**: Keten meerdere middleware handlers (logging, authenticatie, rate-limiting) met functie- en chatmiddleware voor fijne controle over agentgedrag.
- **Workflow Checkpointing**: Gebruik workflow-events en serialisatie om langdurige agentprocessen op te slaan en te hervatten.
- **Dynamische toolselectie**: Combineer RAG over toolbeschrijvingen met MAF's toolregistratie om alleen relevante tools per query aan te bieden.
- **Multi-agent overdracht**: Gebruik workflow-edges en conditionele routering om overdrachten tussen gespecialiseerde agenten te orkestreren.

## LangChain / LangGraph Agents hosten op Microsoft Foundry

Microsoft Agent Framework is **framework-interoperabel** — je bent niet beperkt tot agenten geschreven met MAF. Als je al een agent hebt gebouwd met **LangChain** of **LangGraph**, kun je deze als een **door Microsoft Foundry gehoste agent** draaien zodat Foundry runtime, sessies, scaling, identiteit en protocol endpoints beheert, terwijl jouw agentlogica in LangGraph blijft.

Dit wordt gedaan met het `langchain_azure_ai.agents.hosting` pakket, dat een gecompileerde LangGraph-grafiek over dezelfde protocollen aanbiedt die Foundry-gehoste agenten gebruiken.

**1. Installeer de hosting extra:**

```bash
pip install -U "langchain-azure-ai[hosting]>=1.2.4" azure-identity
```

De `hosting` extra installeert de Foundry-protocolbibliotheken: `azure-ai-agentserver-responses` (de OpenAI-compatibele `/responses` endpoint) en `azure-ai-agentserver-invocations` (de generieke `/invocations` endpoint).

**2. Kies een hostingprotocol:**

| Protocol | Hostklasse | Endpoint | Gebruik wanneer |
|----------|-----------|----------|----------|
| **Responses** | `ResponsesHostServer` | `/responses` | Je OpenAI-compatibele chat, streaming, responsgeschiedenis en gesprek-threading wilt — de aanbevolen standaard voor conversatieagenten. |
| **Invocations** | `InvocationsHostServer` | `/invocations` | Je een custom JSON-formaat, een webhook-achtig endpoint of niet-conversationale verwerking nodig hebt. |

Omdat de **Responses API de primaire API is voor agent-stijl ontwikkeling in Foundry**, start je meestal met `ResponsesHostServer` voor de meeste agenten.

**3. Configureer omgevingsvariabelen** (`az login` eerst zodat `DefaultAzureCredential` kan authenticeren):

```bash
export FOUNDRY_PROJECT_ENDPOINT="https://<resource>.services.ai.azure.com/api/projects/<project>"
export FOUNDRY_MODEL_NAME="gpt-5-mini"
```

Wanneer de agent later als gehoste agent in Foundry draait, voegt het platform automatisch `FOUNDRY_PROJECT_ENDPOINT` toe.

**4. Stel een LangGraph-agent beschikbaar via het Responses-protocol:**

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

    # ChatOpenAI richt zich hier op de OpenAI-compatibele (Responses) endpoint van het Foundry-project.
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

Draai lokaal met `python main.py`, stuur dan een Responses-verzoek naar `http://localhost:8088/responses`.

**Belangrijk gedrag:**

- **Gesprekken**: Clients zetten een gesprek voort door `previous_response_id` of een `conversation` ID mee te geven. Als jouw grafiek is gecompileerd met een LangGraph checkpointer, koppelt Foundry de gesprekstoestand aan de checkpoint (gebruik een duurzaam checkpointer in productie; `MemorySaver` is prima voor lokaal testen).
- **Mens-in-de-lus**: Als je grafiek LangGraph`s `interrupt()` gebruikt, toont `ResponsesHostServer` de hangende interrupt als een Responses `function_call` / `mcp_approval_request` item, en hervatten clients met een overeenkomstige `function_call_output` / `mcp_approval_response`.
- **Deploy naar Foundry**: Gebruik de Azure Developer CLI — `azd ext install azure.ai.agents`, `azd ai agent init -m <manifest>`, `azd ai agent run` (lokaal, vereist Docker), dan `azd provision` en `azd deploy`. Deployen van gehoste agenten vereist de **Foundry Project Manager** rol.

Een draaiende versie van dit voorbeeld staat in [code-samples/14-langchain-hosted-agent.py](../../../14-microsoft-agent-framework/code-samples/14-langchain-hosted-agent.py). Voor de volledige walkthrough (Invocations-protocol, aangepaste request-schema's en probleemoplossing), zie [Host LangGraph agents as Foundry hosted agents](https://learn.microsoft.com/azure/foundry/how-to/develop/langchain-hosted-agents).

## Codevoorbeelden 

Codevoorbeelden voor Microsoft Agent Framework zijn te vinden in deze repository onder de bestanden `xx-python-agent-framework` en `xx-dotnet-agent-framework`.

## Nog meer vragen over Microsoft Agent Framework?

Sluit je aan bij de [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D) om andere leerlingen te ontmoeten, deel te nemen aan kantooruren en je vragen over AI-agenten beantwoord te krijgen.
## Vorige les

[Geheugen voor AI-agenten](../13-agent-memory/README.md)

## Volgende les

[Computer Use Agents (CUA) bouwen](../15-browser-use/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:
Dit document is vertaald met behulp van de AI vertaaldienst [Co-op Translator](https://github.com/Azure/co-op-translator). Hoewel we streven naar nauwkeurigheid, dient u er rekening mee te houden dat geautomatiseerde vertalingen fouten of onnauwkeurigheden kunnen bevatten. Het originele document in de oorspronkelijke taal moet worden beschouwd als de gezaghebbende bron. Voor kritieke informatie wordt professionele menselijke vertaling aanbevolen. Wij zijn niet aansprakelijk voor eventuele misverstanden of verkeerde interpretaties die voortvloeien uit het gebruik van deze vertaling.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->