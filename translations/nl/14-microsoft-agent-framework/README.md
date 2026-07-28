# Verkenning van het Microsoft Agent Framework

![Agent Framework](../../../translated_images/nl/lesson-14-thumbnail.90df0065b9d234ee.webp)

### Introductie

Deze les behandelt:

- Inzicht in Microsoft Agent Framework: Belangrijkste kenmerken en waarde  
- Verkenning van de kernconcepten van Microsoft Agent Framework
- Geavanceerde MAF-patronen: Workflows, Middleware en Geheugen

## Leerdoelen

Na het voltooien van deze les weet je hoe je:

- Productieklaar AI-agents bouwt met het Microsoft Agent Framework
- De kernfuncties van Microsoft Agent Framework toepast op jouw agentusecases
- Geavanceerde patronen gebruikt, waaronder workflows, middleware en observability

## Codevoorbeelden 

Codevoorbeelden voor [Microsoft Agent Framework (MAF)](https://aka.ms/ai-agents-beginners/agent-framework) vind je in deze repository onder de bestanden `xx-python-agent-framework` en `xx-dotnet-agent-framework`.

## Inzicht in Microsoft Agent Framework

![Framework Intro](../../../translated_images/nl/framework-intro.077af16617cf130c.webp)

[Microsoft Agent Framework (MAF)](https://aka.ms/ai-agents-beginners/agent-framework) is het verenigde framework van Microsoft voor het bouwen van AI-agents. Het biedt de flexibiliteit om de grote verscheidenheid aan agentusecases aan te pakken, die zowel in productie als in onderzoeksomgevingen voorkomen, waaronder:

- **Sequentiële agentorchestratie** in scenario's waar stapsgewijze workflows nodig zijn.
- **Gelijktijdige orchestratie** in scenario's waar agents taken gelijktijdig moeten voltooien.
- **Groepschatorchestratie** in scenario's waar agents samen aan één taak kunnen samenwerken.
- **Handoff-orchestratie** in scenario's waar agents taken aan elkaar overdragen zodra subtaken voltooid zijn.
- **Magnetische orchestratie** in scenario's waar een manager agent een takenlijst maakt en aanpast en de coördinatie van subagents beheert om de taak te voltooien.

Om AI Agents in productie te leveren, heeft MAF ook functies opgenomen voor:

- **Observability** door gebruik te maken van OpenTelemetry, waarbij elke actie van de AI Agent wordt gevolgd, inclusief oproepen van tools, orchestratiestappen, redeneerstromen en prestatiemonitoring via Microsoft Foundry dashboards.
- **Beveiliging** door agents native te hosten op Microsoft Foundry, wat beveiligingscontroles bevat zoals rolgebaseerde toegang, privégegevensverwerking en ingebouwde contentveiligheid.
- **Duurzaamheid** doordat agent-threads en workflows kunnen pauzeren, hervatten en herstellen van fouten, wat langere processen mogelijk maakt.
- **Controle** doordat human-in-the-loop-workflows worden ondersteund waarbij taken gemarkeerd worden als zijnde goedkeuringsplichtig door een mens.

Microsoft Agent Framework richt zich ook op interoperabiliteit door:

- **Cloud-agnostisch te zijn** - Agents kunnen draaien in containers, on-premises en in meerdere verschillende clouds.
- **Provider-agnostisch te zijn** - Agents kunnen worden gemaakt via je voorkeurs-SDK, waaronder Azure OpenAI en OpenAI.
- **Open standaarden te integreren** - Agents kunnen protocollen gebruiken zoals Agent-to-Agent(A2A) en Model Context Protocol (MCP) om andere agents en tools te ontdekken en te gebruiken.
- **Plug-ins en connectors** - Verbindingen kunnen worden gemaakt met data- en geheugendiensten zoals Microsoft Fabric, SharePoint, Pinecone en Qdrant.

Laten we bekijken hoe deze functies worden toegepast op enkele kernconcepten van Microsoft Agent Framework.

## Kernconcepten van Microsoft Agent Framework

### Agents

![Agent Framework](../../../translated_images/nl/agent-components.410a06daf87b4fef.webp)

**Agents maken**

Het aanmaken van een agent gebeurt door het definiëren van de inference-service (LLM-provider), een
set instructies die de AI-agent moet volgen, en het toewijzen van een `naam`:

```python
agent = AzureOpenAIChatClient(credential=AzureCliCredential()).create_agent( instructions="You are good at recommending trips to customers based on their preferences.", name="TripRecommender" )
```

Het bovenstaande gebruikt `Azure OpenAI`, maar agents kunnen worden aangemaakt met verschillende services, waaronder `Microsoft Foundry Agent Service`:

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

of [MiniMax](https://platform.minimaxi.com/), die een OpenAI-compatibele API aanbiedt met grote contextvensters (tot 204K tokens):

```python
agent = OpenAIChatClient(base_url="https://api.minimax.io/v1", api_key=os.environ["MINIMAX_API_KEY"], model_id="MiniMax-M3").create_agent( name="HelpfulAssistant", instructions="You are a helpful assistant.", )
```

of remote agents die het A2A-protocol gebruiken:

```python
agent = A2AAgent( name=agent_card.name, description=agent_card.description, agent_card=agent_card, url="https://your-a2a-agent-host" )
```

**Agents uitvoeren**

Agents worden uitgevoerd met de `.run` of `.run_stream` methoden voor respectievelijk niet-streaming of streaming responses.

```python
result = await agent.run("What are good places to visit in Amsterdam?")
print(result.text)
```

```python
async for update in agent.run_stream("What are the good places to visit in Amsterdam?"):
    if update.text:
        print(update.text, end="", flush=True)

```

Elke agentuitvoering kan ook opties bevatten om parameters aan te passen, zoals `max_tokens` die door de agent worden gebruikt, `tools` die de agent kan aanroepen, en zelfs het gebruikte `model` zelf.

Dit is nuttig in gevallen waar specifieke modellen of tools nodig zijn om de taak van een gebruiker te voltooien.

**Tools**

Tools kunnen zowel bij het definiëren van de agent worden opgegeven:

```python
def get_attractions( location: Annotated[str, Field(description="The location to get the top tourist attractions for")], ) -> str: """Get the top tourist attractions for a given location.""" return f"The top attractions for {location} are." 


# Bij het rechtstreeks aanmaken van een ChatAgent

agent = ChatAgent( chat_client=OpenAIChatClient(), instructions="You are a helpful assistant", tools=[get_attractions]

```

en ook bij het uitvoeren van de agent:

```python

result1 = await agent.run( "What's the best place to visit in Seattle?", tools=[get_attractions] # Tool alleen beschikbaar voor deze uitvoering )
```

**Agent Threads**

Agent Threads worden gebruikt om multi-turn gesprekken af te handelen. Threads kunnen worden aangemaakt door:

- Gebruik te maken van `get_new_thread()`, waarmee de thread over langere tijd kan worden opgeslagen
- Automatisch een thread te genereren wanneer een agent wordt uitgevoerd, waarbij de thread slechts gedurende de huidige run blijft bestaan.

De code voor het aanmaken van een thread ziet er als volgt uit:

```python
# Maak een nieuwe thread aan.
thread = agent.get_new_thread() # Voer de agent uit met de thread.
response = await agent.run("Hello, I am here to help you book travel. Where would you like to go?", thread=thread)

```

Je kunt de thread vervolgens serialiseren zodat die later gebruikt kan worden:

```python
# Maak een nieuwe thread aan.
thread = agent.get_new_thread() 

# Voer de agent uit met de thread.

response = await agent.run("Hello, how are you?", thread=thread) 

# Serialiseer de thread voor opslag.

serialized_thread = await thread.serialize() 

# Deserializeer de threadstatus na het laden uit opslag.

resumed_thread = await agent.deserialize_thread(serialized_thread)
```

**Agent Middleware**

Agents communiceren met tools en LLM's om taken van gebruikers te voltooien. In bepaalde scenario’s willen we acties tussen deze interacties uitvoeren of volgen. Agent middleware stelt ons in staat dit te doen via:

*Function Middleware*

Deze middleware laat ons een actie uitvoeren tussen de agent en een functie/tool die wordt aangeroepen. Een voorbeeld van het gebruik is logging van de functietoeroep.

In onderstaande code bepaalt `next` of de volgende middleware of de daadwerkelijke functie moet worden aangeroepen.

```python
async def logging_function_middleware(
    context: FunctionInvocationContext,
    next: Callable[[FunctionInvocationContext], Awaitable[None]],
) -> None:
    """Function middleware that logs function execution."""
    # Voorbewerking: Loggen vóór functievermijding
    print(f"[Function] Calling {context.function.name}")

    # Ga door naar de volgende middleware of functie-uitvoering
    await next(context)

    # Nabewerking: Loggen na functievermijding
    print(f"[Function] {context.function.name} completed")
```

*Chat Middleware*

Deze middleware laat ons een actie uitvoeren of loggen tussen de agent en de verzoeken naar de LLM.

Dit bevat belangrijke informatie zoals de `messages` die naar de AI-service worden gestuurd.

```python
async def logging_chat_middleware(
    context: ChatContext,
    next: Callable[[ChatContext], Awaitable[None]],
) -> None:
    """Chat middleware that logs AI interactions."""
    # Voorverwerking: Log vóór AI-aanroep
    print(f"[Chat] Sending {len(context.messages)} messages to AI")

    # Ga door naar de volgende middleware of AI-service
    await next(context)

    # Naverwerking: Log na AI-antwoord
    print("[Chat] AI response received")

```

**Agentgeheugen**

Zoals beschreven in de les `Agentic Memory`, is geheugen een belangrijk element om de agent in verschillende contexten te laten opereren. MAF biedt verschillende soorten geheugen:

*In-Memory Storage*

Dit is het geheugen dat wordt opgeslagen in threads tijdens runtime van de applicatie.

```python
# Maak een nieuwe thread aan.
thread = agent.get_new_thread() # Voer de agent uit met de thread.
response = await agent.run("Hello, I am here to help you book travel. Where would you like to go?", thread=thread)
```

*Persistent Messages*

Dit geheugen wordt gebruikt voor het opslaan van gespreksgeschiedenis over verschillende sessies heen. Het wordt gedefinieerd met behulp van `chat_message_store_factory`:

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

Dit geheugen wordt aan de context toegevoegd voordat agents worden uitgevoerd. Deze geheugens kunnen worden opgeslagen in externe diensten zoals mem0:

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

**Agent Observability**

Observability is belangrijk om betrouwbare en onderhoudbare agentsystemen te bouwen. MAF integreert met OpenTelemetry om tracing en meters te bieden voor betere observability.

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

MAF biedt workflows aan die vooraf gedefinieerde stappen zijn om een taak te voltooien en AI agents als componenten in die stappen bevatten.

Workflows bestaan uit verschillende componenten die zorgen voor betere controle over de flow. Workflows maken ook **multi-agent orchestratie** en **checkpointing** mogelijk om workflow toestanden op te slaan.

De kerncomponenten van een workflow zijn:

**Executors**

Executors ontvangen invoerberichten, voeren hun toegewezen taken uit en produceren daarna een uitvoerbericht. Dit brengt de workflow vooruit richting het voltooien van de grotere taak. Executors kunnen AI agents zijn of aangepaste logica.

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

*Switch-case Edges* - Sturen berichten naar verschillende executors op basis van gedefinieerde voorwaarden. Bijvoorbeeld als een reiziger prioriteitstoegang heeft en hun taken via een andere workflow worden afgehandeld.

*Fan-out Edges* - Verstuur één bericht naar meerdere doelen.

*Fan-in Edges* - Verzamelt meerdere berichten van verschillende executors en verstuurt deze naar één doel.

**Events**

Om betere observability in workflows te bieden, heeft MAF ingebouwde events voor uitvoering, waaronder:

- `WorkflowStartedEvent`  - Workflow-uitvoering begint
- `WorkflowOutputEvent` - Workflow produceert een output
- `WorkflowErrorEvent` - Workflow ondervindt een fout
- `ExecutorInvokeEvent`  - Executor begint met verwerken
- `ExecutorCompleteEvent`  -  Executor voltooit verwerken
- `RequestInfoEvent` - Er is een verzoek verstuurd

## Geavanceerde MAF-patronen

De voorgaande secties behandelen de kernconcepten van Microsoft Agent Framework. Naarmate je complexere agents bouwt, zijn er enkele geavanceerde patronen om te overwegen:

- **Middleware-compositie**: Koppel meerdere middleware handlers (logging, authenticatie, rate-limiting) via functie- en chatmiddleware voor fijnmazige controle over het gedrag van de agent.
- **Workflow Checkpointing**: Gebruik workflow-events en serialisatie om langlopende agentprocessen op te slaan en te hervatten.
- **Dynamische toolselectie**: Combineer RAG over toolbeschrijvingen met MAF’s toolregistratie om alleen relevante tools per query te tonen.
- **Multi-agent Handoff**: Gebruik workflow-edges en voorwaardelijke routering om overdrachten tussen gespecialiseerde agents te orkestreren.

## LangChain / LangGraph Agents hosten op Microsoft Foundry

Microsoft Agent Framework is **framework-interoperabel** — je bent niet beperkt tot agents geschreven met MAF. Als je al een agent hebt gebouwd met **LangChain** of **LangGraph**, kun je die uitvoeren als een **Microsoft Foundry gehoste agent** zodat Foundry de runtime, sessies, schaalbaarheid, identiteit en protocol endpoints voor je beheert, terwijl je agentlogica blijft in LangGraph.

Dit wordt gedaan met het `langchain_azure_ai.agents.hosting` pakket, dat een gecompileerde LangGraph graph blootlegt over dezelfde protocollen die Foundry gehoste agents gebruiken.

**1. Installeer de hosting extra:**

```bash
pip install -U "langchain-azure-ai[hosting]>=1.2.4" azure-identity
```

De `hosting` extra installeert de Foundry protocolbibliotheken: `azure-ai-agentserver-responses` (de OpenAI-compatibele `/responses` endpoint) en `azure-ai-agentserver-invocations` (de generieke `/invocations` endpoint).

**2. Kies een hostingprotocol:**

| Protocol | Hostklasse | Endpoint | Gebruik wanneer |
|----------|-----------|----------|----------|
| **Responses** | `ResponsesHostServer` | `/responses` | Je een OpenAI-compatibele chat, streaming, responsehistory en conversatietheading wilt – de aanbevolen standaard voor conversationele agents. |
| **Invocations** | `InvocationsHostServer` | `/invocations` | Je een aangepaste JSON-structuur, een webhook-achtige endpoint of niet-conversationele verwerking nodig hebt. |

Omdat de **Responses API de primaire API is voor agent-ontwikkeling in Foundry**, begin met `ResponsesHostServer` voor de meeste agents.

**3. Configureer omgevingsvariabelen** (`az login` eerst zodat `DefaultAzureCredential` kan authenticeren):

```bash
export FOUNDRY_PROJECT_ENDPOINT="https://<resource>.services.ai.azure.com/api/projects/<project>"
export FOUNDRY_MODEL_NAME="gpt-5-mini"
```

Wanneer de agent later draait als gehoste agent in Foundry, injecteert het platform automatisch `FOUNDRY_PROJECT_ENDPOINT`.

**4. Stel een LangGraph agent bloot over het Responses-protocol:**

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

    # ChatOpenAI hier richt zich op het OpenAI-compatibele (Responses) eindpunt van het Foundry-project.
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

Voer het lokaal uit met `python main.py`, en stuur vervolgens een Responses-verzoek naar `http://localhost:8088/responses`.

**Belangrijke eigenschappen:**

- **Gesprekken**: Clients zetten een gesprek voort door `previous_response_id` of een `conversation` ID mee te geven. Als je graph is gecompileerd met een LangGraph checkpointer, koppelt Foundry de gesprekstoestand aan de checkpoint (gebruik een duurzame checkpointer in productie; `MemorySaver` volstaat voor lokale tests).
- **Human-in-the-loop**: Als je graph LangGraph `interrupt()` gebruikt, toont `ResponsesHostServer` de openstaande interrupt als een Responses `function_call` / `mcp_approval_request` item, en clients hervatten met een overeenkomstige `function_call_output` / `mcp_approval_response`.
- **Deploy naar Foundry**: Gebruik de Azure Developer CLI — `azd ext install azure.ai.agents`, `azd ai agent init -m <manifest>`, `azd ai agent run` (lokaal, vereist Docker), daarna `azd provision` en `azd deploy`. Voor het uitrollen als gehoste agent heb je de rol **Foundry Project Manager** nodig.

Een uitvoerbare versie van dit voorbeeld staat in [code-samples/14-langchain-hosted-agent.py](../../../14-microsoft-agent-framework/code-samples/14-langchain-hosted-agent.py). Voor de volledige walkthrough (Invocations-protocol, aangepaste requestschemas en probleemoplossing), zie [Host LangGraph agents als Foundry gehoste agents](https://learn.microsoft.com/azure/foundry/how-to/develop/langchain-hosted-agents).

## Codevoorbeelden 

Codevoorbeelden voor Microsoft Agent Framework vind je in deze repository onder de bestanden `xx-python-agent-framework` en `xx-dotnet-agent-framework`.

## Meer vragen over Microsoft Agent Framework?

Word lid van de [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D) om andere lerenden te ontmoeten, deel te nemen aan office hours en je vragen over AI Agents beantwoord te krijgen.
## Vorige les

[Geheugen voor AI Agents](../13-agent-memory/README.md)

## Volgende les

[Bouwen van Computer Use Agents (CUA)](../15-browser-use/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:
Dit document is vertaald met behulp van de AI vertaaldienst [Co-op Translator](https://github.com/Azure/co-op-translator). Hoewel we streven naar nauwkeurigheid, dient u er rekening mee te houden dat geautomatiseerde vertalingen fouten of onnauwkeurigheden kunnen bevatten. Het originele document in de oorspronkelijke taal moet worden beschouwd als de gezaghebbende bron. Voor kritieke informatie wordt professionele menselijke vertaling aanbevolen. Wij zijn niet aansprakelijk voor eventuele misverstanden of verkeerde interpretaties die voortvloeien uit het gebruik van deze vertaling.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->