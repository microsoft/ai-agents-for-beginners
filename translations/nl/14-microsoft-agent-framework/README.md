# Verkennen van het Microsoft Agent Framework

![Agent Framework](../../../translated_images/nl/lesson-14-thumbnail.90df0065b9d234ee.webp)

### Introductie

Deze les behandelt:

- Begrip van Microsoft Agent Framework: Belangrijke kenmerken en waarde  
- Verkennen van de kernconcepten van Microsoft Agent Framework
- Geavanceerde MAF-patronen: Workflows, middleware en geheugen

## Leerdoelen

Na het voltooien van deze les weet je hoe je:

- Productierijpe AI-agents bouwt met behulp van Microsoft Agent Framework
- De kernfuncties van Microsoft Agent Framework toepast op jouw agentische use cases
- Geavanceerde patronen gebruikt, waaronder workflows, middleware en observeerbaarheid

## Codesamples 

Codesamples voor [Microsoft Agent Framework (MAF)](https://aka.ms/ai-agents-beginners/agent-framework) vind je in deze repository onder de bestanden `xx-python-agent-framework` en `xx-dotnet-agent-framework`.

## Begrip van Microsoft Agent Framework

![Framework Intro](../../../translated_images/nl/framework-intro.077af16617cf130c.webp)

[Microsoft Agent Framework (MAF)](https://aka.ms/ai-agents-beginners/agent-framework) is het uniforme framework van Microsoft voor het bouwen van AI-agents. Het biedt de flexibiliteit om de grote verscheidenheid aan agentische use cases aan te pakken die voorkomen in zowel productie- als onderzoeksomgevingen, waaronder:

- **Sequentiële agentorchestratie** in scenario's waar stapsgewijze workflows nodig zijn.
- **Gelijktijdige orchestratie** in scenario's waar agents tegelijkertijd taken moeten voltooien.
- **Groepschat-orchestratie** in scenario's waar agents samen kunnen werken aan één taak.
- **Overdrachtsorchestratie** in scenario's waar agents taken aan elkaar overdragen naarmate subtaken worden voltooid.
- **Magnetische orchestratie** in scenario's waar een manager-agent een takenlijst aanmaakt en wijzigt en de coördinatie van subagents regelt om de taak te voltooien.

Voor het leveren van AI-agents in productie heeft MAF ook functies opgenomen voor:

- **Observeerbaarheid** via het gebruik van OpenTelemetry waarbij elke actie van de AI-agent wordt gevolgd, inclusief tool-aanroepen, orchestratiestappen, redeneerstromen en prestatiebewaking via Microsoft Foundry dashboards.
- **Beveiliging** door agents natively te hosten op Microsoft Foundry, dat beveiligingscontroles zoals rolgebaseerde toegang, privégegevensverwerking en ingebouwde contentveiligheid bevat.
- **Duurzaamheid** aangezien agent-threads en workflows kunnen pauzeren, hervatten en herstellen van fouten, wat langere lopende processen mogelijk maakt.
- **Controle** omdat workflows met menselijke tussenkomst worden ondersteund waarbij taken als goedkeuring door een mens worden gemarkeerd.

Microsoft Agent Framework richt zich ook op interoperabiliteit door:

- **Cloud-agnostisch te zijn** - Agents kunnen draaien in containers, on-premises en op meerdere verschillende clouds.
- **Provider-agnostisch te zijn** - Agents kunnen worden gemaakt via jouw voorkeurs-SDK waaronder Azure OpenAI en OpenAI.
- **Open standaarden te integreren** - Agents kunnen protocollen gebruiken zoals Agent-to-Agent (A2A) en Model Context Protocol (MCP) om andere agents en tools te ontdekken en te gebruiken.
- **Plugins en Connectors** - Verbindingen kunnen worden gemaakt met data- en geheugenservices zoals Microsoft Fabric, SharePoint, Pinecone en Qdrant.

Laten we kijken hoe deze functies worden toegepast op enkele kernconcepten van Microsoft Agent Framework.

## Kernconcepten van Microsoft Agent Framework

### Agents

![Agent Framework](../../../translated_images/nl/agent-components.410a06daf87b4fef.webp)

**Agents maken**

Het maken van agents gebeurt door het definiëren van de inference service (LLM Provider), een
reeks instructies die de AI-agent moet volgen en een toegewezen `name`:

```python
agent = AzureOpenAIChatClient(credential=AzureCliCredential()).create_agent( instructions="You are good at recommending trips to customers based on their preferences.", name="TripRecommender" )
```

Bovenstaand voorbeeld gebruikt `Azure OpenAI`, maar agents kunnen worden gemaakt met verschillende services waaronder `Microsoft Foundry Agent Service`:

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

of remote agents via het A2A-protocol:

```python
agent = A2AAgent( name=agent_card.name, description=agent_card.description, agent_card=agent_card, url="https://your-a2a-agent-host" )
```

**Agents uitvoeren**

Agents worden uitgevoerd met behulp van de `.run` of `.run_stream` methodes voor respectievelijk niet-streamende of streamende responses.

```python
result = await agent.run("What are good places to visit in Amsterdam?")
print(result.text)
```

```python
async for update in agent.run_stream("What are the good places to visit in Amsterdam?"):
    if update.text:
        print(update.text, end="", flush=True)

```

Elke agent-run kan ook opties bevatten om parameters aan te passen zoals `max_tokens` die door de agent worden gebruikt, `tools` die door de agent kunnen worden aangeroepen, en zelfs het gebruikte `model` zelf.

Dit is nuttig in gevallen waar specifieke modellen of tools vereist zijn om de taak van een gebruiker te voltooien.

**Tools**

Tools kunnen worden gedefinieerd zowel bij het definiëren van de agent:

```python
def get_attractions( location: Annotated[str, Field(description="The location to get the top tourist attractions for")], ) -> str: """Get the top tourist attractions for a given location.""" return f"The top attractions for {location} are." 


# Bij het direct aanmaken van een ChatAgent

agent = ChatAgent( chat_client=OpenAIChatClient(), instructions="You are a helpful assistant", tools=[get_attractions]

```

alsook bij het uitvoeren van de agent:

```python

result1 = await agent.run( "What's the best place to visit in Seattle?", tools=[get_attractions] # Hulpmiddel uitsluitend voor deze uitvoering geleverd )
```

**Agent Threads**

Agent Threads worden gebruikt voor het afhandelen van multi-turn conversaties. Threads kunnen worden gemaakt door:

- Het gebruik van `get_new_thread()` waarmee de thread in de loop van de tijd opgeslagen kan worden
- Het automatisch aanmaken van een thread bij het uitvoeren van een agent, waarbij de thread alleen tijdens de huidige run bestaat.

De code om een thread te maken ziet er als volgt uit:

```python
# Maak een nieuwe thread aan.
thread = agent.get_new_thread() # Voer de agent uit met de thread.
response = await agent.run("Hello, I am here to help you book travel. Where would you like to go?", thread=thread)

```

Je kunt de thread daarna serialiseren om hem voor later gebruik op te slaan:

```python
# Maak een nieuwe thread aan.
thread = agent.get_new_thread() 

# Voer de agent uit met de thread.

response = await agent.run("Hello, how are you?", thread=thread) 

# Serialiseer de thread voor opslag.

serialized_thread = await thread.serialize() 

# Deserialiseer de thread status na het laden uit opslag.

resumed_thread = await agent.deserialize_thread(serialized_thread)
```

**Agent Middleware**

Agents interageren met tools en LLM's om de taken van een gebruiker te voltooien. In bepaalde scenario's willen we acties uitvoeren of bijhouden tussen deze interacties. Agent middleware stelt ons in staat dit te doen door middel van:

*Function Middleware*

Deze middleware maakt het mogelijk een actie uit te voeren tussen de agent en een functie/tool die wordt aangeroepen. Een voorbeeld van wanneer dit wordt gebruikt is als je logging wilt doen bij de functiemaak aanroep.

In onderstaande code bepaalt `next` of de volgende middleware of de daadwerkelijke functie moet worden aangeroepen.

```python
async def logging_function_middleware(
    context: FunctionInvocationContext,
    next: Callable[[FunctionInvocationContext], Awaitable[None]],
) -> None:
    """Function middleware that logs function execution."""
    # Voorbewerking: Log vóór de uitvoering van de functie
    print(f"[Function] Calling {context.function.name}")

    # Ga door naar de volgende middleware of functie-uitvoering
    await next(context)

    # Nabewerking: Log na de uitvoering van de functie
    print(f"[Function] {context.function.name} completed")
```

*Chat Middleware*

Deze middleware maakt het mogelijk een actie uit te voeren of te loggen tussen de agent en de verzoeken aan de LLM.

Dit bevat belangrijke informatie zoals de `messages` die naar de AI-service worden gestuurd.

```python
async def logging_chat_middleware(
    context: ChatContext,
    next: Callable[[ChatContext], Awaitable[None]],
) -> None:
    """Chat middleware that logs AI interactions."""
    # Voorbewerking: Loggen vóór AI-aanroep
    print(f"[Chat] Sending {len(context.messages)} messages to AI")

    # Ga door naar de volgende middleware of AI-service
    await next(context)

    # Nabewerking: Loggen na AI-antwoord
    print("[Chat] AI response received")

```

**Agent Memory**

Zoals behandeld in de les `Agentic Memory`, is geheugen een belangrijk element om de agent in staat te stellen over verschillende contexten te opereren. MAF biedt verschillende soorten geheugen:

*In-Memory Opslag*

Dit is het geheugen dat wordt opgeslagen in threads tijdens de runtime van de applicatie.

```python
# Maak een nieuwe thread aan.
thread = agent.get_new_thread() # Voer de agent uit met de thread.
response = await agent.run("Hello, I am here to help you book travel. Where would you like to go?", thread=thread)
```

*Persistent Messages*

Dit geheugen wordt gebruikt om de gespreksgeschiedenis over verschillende sessies op te slaan. Het wordt gedefinieerd via de `chat_message_store_factory`:

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

*Dynamic Memory*

Dit geheugen wordt toegevoegd aan de context voordat agents worden uitgevoerd. Deze geheugens kunnen worden opgeslagen in externe services zoals mem0:

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

**Agent Observeerbaarheid**

Observeerbaarheid is belangrijk om betrouwbare en onderhoudbare agentische systemen te bouwen. MAF integreert met OpenTelemetry om tracing en meters te bieden voor betere observeerbaarheid.

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

MAF biedt workflows die vooraf gedefinieerde stappen zijn om een taak te voltooien en AI-agents bevatten als componenten in die stappen.

Workflows bestaan uit verschillende componenten die een betere controleflow mogelijk maken. Workflows ondersteunen ook **multi-agent orchestratie** en **checkpointing** om workflowstatussen op te slaan.

De kerncomponenten van een workflow zijn:

**Executors**

Executors ontvangen inputberichten, voeren hun toegewezen taken uit en produceren daarna een outputbericht. Dit brengt de workflow vooruit richting de voltooiing van de grotere taak. Executors kunnen AI-agent of aangepaste logica zijn.

**Edges**

Edges worden gebruikt om de stroom van berichten in een workflow te definiëren. Deze kunnen zijn:

*Directe Edges* - Eenvoudige één-op-één verbindingen tussen executors:

```python
from agent_framework import WorkflowBuilder

builder = WorkflowBuilder()
builder.add_edge(source_executor, target_executor)
builder.set_start_executor(source_executor)
workflow = builder.build()
```

*Voorwaardelijke Edges* - Worden geactiveerd nadat aan een bepaalde voorwaarde is voldaan. Bijvoorbeeld, als hotelkamers niet beschikbaar zijn, kan een executor andere opties voorstellen.

*Switch-case Edges* - Routeren berichten naar verschillende executors op basis van gedefinieerde voorwaarden. Bijvoorbeeld, als een reizende klant prioriteits toegang heeft zullen hun taken via een andere workflow worden afgehandeld.

*Fan-out Edges* - Sturen één bericht naar meerdere doelen.

*Fan-in Edges* - Verzamelen meerdere berichten van verschillende executors en sturen naar één doel.

**Gebeurtenissen**

Om betere observeerbaarheid in workflows te bieden, biedt MAF ingebouwde gebeurtenissen voor uitvoering waaronder:

- `WorkflowStartedEvent`  - Workflowuitvoering begint
- `WorkflowOutputEvent` - Workflow produceert een output
- `WorkflowErrorEvent` - Workflow ondervindt een fout
- `ExecutorInvokeEvent`  - Executor begint met verwerken
- `ExecutorCompleteEvent`  -  Executor beëindigt verwerking
- `RequestInfoEvent` - Er wordt een verzoek uitgegeven

## Geavanceerde MAF-patronen

De bovenstaande secties behandelen de kernconcepten van Microsoft Agent Framework. Naarmate je complexere agents bouwt, zijn hier enkele geavanceerde patronen om te overwegen:

- **Middleware-compositie**: Koppel meerdere middleware handlers (logging, authenticatie, rate-limiting) met function en chat middleware voor fijnmazige controle over het gedrag van de agent.
- **Workflow Checkpointing**: Gebruik workflowgebeurtenissen en serialisatie om langlopende agentprocessen op te slaan en te hervatten.
- **Dynamische toolselectie**: Combineer RAG over toolbeschrijvingen met de toolregistratie van MAF om enkel relevante tools per query te presenteren.
- **Multi-agent overdracht**: Gebruik workflow-edges en conditionele routering om de overdracht tussen gespecialiseerde agents te orkestreren.

## Hosting LangChain / LangGraph Agents op Microsoft Foundry

Microsoft Agent Framework is **framework-interoperabel** — je bent niet beperkt tot agents geschreven met MAF. Als je al een agent hebt gebouwd met **LangChain** of **LangGraph**, kun je deze als een **Microsoft Foundry hosted agent** draaien zodat Foundry runtime, sessies, schaalvergroting, identiteit en protocol endpoints voor je beheert, terwijl jouw agentlogica in LangGraph blijft.

Dit wordt gedaan met het `langchain_azure_ai.agents.hosting` pakket, dat een gecompileerde LangGraph-grafiek blootstelt via dezelfde protocollen die Foundry hosted agents gebruiken.

**1. Installeer de hosting extra:**

```bash
pip install -U "langchain-azure-ai[hosting]>=1.2.4" azure-identity
```

De `hosting` extra installeert de Foundry protocolbibliotheken: `azure-ai-agentserver-responses` (de OpenAI-compatibele `/responses` endpoint) en `azure-ai-agentserver-invocations` (de generieke `/invocations` endpoint).

**2. Kies een hostingprotocol:**

| Protocol | Hostklasse | Endpoint | Gebruik wanneer |
|----------|------------|----------|----------------|
| **Responses** | `ResponsesHostServer` | `/responses` | Je OpenAI-compatibele chat, streaming, responsegeschiedenis en conversatiedraden wilt — de aanbevolen standaard voor converserende agents. |
| **Invocations** | `InvocationsHostServer` | `/invocations` | Je een aangepaste JSON-vorm, een webhook-achtige endpoint, of niet-conversatieverwerking nodig hebt. |

Omdat de **Responses API de primaire API is voor agent-style ontwikkeling in Foundry**, begin je meestal met `ResponsesHostServer` voor de meeste agents.

**3. Configureer omgevingsvariabelen** (`az login` eerst zodat `DefaultAzureCredential` kan authenticeren):

```bash
export FOUNDRY_PROJECT_ENDPOINT="https://<resource>.services.ai.azure.com/api/projects/<project>"
export FOUNDRY_MODEL_NAME="gpt-4.1"
```

Wanneer de agent later als hosted agent in Foundry draait, injecteert het platform automatisch `FOUNDRY_PROJECT_ENDPOINT`.

**4. Stel een LangGraph-agent bloot via het Responses-protocol:**

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

    # ChatOpenAI richt zich hier op het OpenAI-compatibele (Responses) eindpunt van het Foundry-project.
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

Voer het lokaal uit met `python main.py`, stuur vervolgens een Responses-verzoek naar `http://localhost:8088/responses`.

**Belangrijkste gedragingen:**

- **Conversaties**: Clients zetten een gesprek voort door `previous_response_id` of een `conversation` ID mee te geven. Als je grafiek is gecompileerd met een LangGraph-checkpointer, koppelt Foundry de gespreksstatus aan de checkpoint (gebruik een duurzame checkpointer in productie; `MemorySaver` is goed voor lokaal testen).
- **Mens-in-de-lus**: Als je grafiek LangGraph `interrupt()` gebruikt, toont `ResponsesHostServer` de openstaande interrupt als een Responses `function_call` / `mcp_approval_request` item, en clients hervatten met een overeenkomende `function_call_output` / `mcp_approval_response`.
- **Deploy naar Foundry**: Gebruik de Azure Developer CLI — `azd ext install azure.ai.agents`, `azd ai agent init -m <manifest>`, `azd ai agent run` (lokaal, vereist Docker), daarna `azd provision` en `azd deploy`. Hosting van agents vereist de rol **Foundry Project Manager**.

Een uitvoerbare versie van dit voorbeeld staat in [code-samples/14-langchain-hosted-agent.py](../../../14-microsoft-agent-framework/code-samples/14-langchain-hosted-agent.py). Voor de volledige handleiding (Invocations-protocol, aangepaste verzoekschemas en probleemoplossing), zie [Host LangGraph agents as Foundry hosted agents](https://learn.microsoft.com/azure/foundry/how-to/develop/langchain-hosted-agents).

## Codesamples 

Codesamples voor Microsoft Agent Framework vind je in deze repository onder de bestanden `xx-python-agent-framework` en `xx-dotnet-agent-framework`.

## Meer vragen over Microsoft Agent Framework?

Word lid van de [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D) om andere leerlingen te ontmoeten, aanwezig te zijn bij office hours en antwoorden op je AI Agents-vragen te krijgen.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:
Dit document is vertaald met behulp van de AI vertaaldienst [Co-op Translator](https://github.com/Azure/co-op-translator). Hoewel we streven naar nauwkeurigheid, dient u er rekening mee te houden dat geautomatiseerde vertalingen fouten of onnauwkeurigheden kunnen bevatten. Het originele document in de oorspronkelijke taal moet worden beschouwd als de gezaghebbende bron. Voor kritieke informatie wordt professionele menselijke vertaling aanbevolen. Wij zijn niet aansprakelijk voor eventuele misverstanden of verkeerde interpretaties die voortvloeien uit het gebruik van deze vertaling.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->