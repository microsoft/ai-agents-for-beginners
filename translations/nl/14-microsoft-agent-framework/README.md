# Verkenning van Microsoft Agent Framework

![Agent Framework](../../../translated_images/nl/lesson-14-thumbnail.90df0065b9d234ee.webp)

### Introductie

Deze les behandelt:

- Inzicht in Microsoft Agent Framework: Belangrijke functies en waarde  
- Verkenning van de kernconcepten van Microsoft Agent Framework
- Geavanceerde MAF-patronen: Workflows, Middleware en Geheugen

## Leerdoelen

Na het voltooien van deze les weet je hoe je:

- Productieklaar AI-agents bouwt met Microsoft Agent Framework
- De kernfuncties van Microsoft Agent Framework toepast op jouw agentusecases
- Geavanceerde patronen gebruikt, waaronder workflows, middleware en observability

## Codevoorbeelden 

Codevoorbeelden voor [Microsoft Agent Framework (MAF)](https://aka.ms/ai-agents-beginners/agent-framewrok) zijn te vinden in deze repository onder de bestanden `xx-python-agent-framework` en `xx-dotnet-agent-framework`.

## Inzicht in Microsoft Agent Framework

![Framework Intro](../../../translated_images/nl/framework-intro.077af16617cf130c.webp)

[Microsoft Agent Framework (MAF)](https://aka.ms/ai-agents-beginners/agent-framewrok) is het uniforme framework van Microsoft voor het bouwen van AI-agents. Het biedt de flexibiliteit om een breed scala aan agentgebaseerde usecases aan te pakken die zowel in productie als onderzoeksomgevingen voorkomen, waaronder:

- **Sequentiële agentorkestratie** in scenario's waar stapsgewijze workflows nodig zijn.
- **Gelijktijdige orkestratie** in scenario's waar agents taken tegelijkertijd moeten voltooien.
- **Groepschatorkestratie** in scenario's waar agents samen aan één taak kunnen samenwerken.
- **Overdrachtorkestratie** in scenario's waar agents taken aan elkaar overdragen na voltooiing van subtaken.
- **Magnetische orkestratie** in scenario's waar een manager-agent een takenlijst maakt en wijzigt en de coördinatie van subagents regelt om de taak te voltooien.

Om AI-agents in productie te brengen, bevat MAF ook functies voor:

- **Observability** via OpenTelemetry waarbij elke actie van de AI-agent wordt gevolgd, inclusief tool-oproepen, orkestratiestappen, redeneerstromen en prestatiebewaking via Microsoft Foundry dashboards.
- **Beveiliging** door agents native te hosten op Microsoft Foundry met beveiligingscontroles zoals op rollen gebaseerde toegang, privégegevensverwerking en ingebouwde contentveiligheid.
- **Duurzaamheid** doordat agentthreads en workflows kunnen pauzeren, hervatten en herstellen van fouten, wat langere processen mogelijk maakt.
- **Controle** doordat workflows met menselijke tussenkomst worden ondersteund waarbij taken worden gemarkeerd als zijnde onderhevig aan menselijke goedkeuring.

Microsoft Agent Framework is ook gericht op interoperabiliteit door:

- **Cloud-agnostisch zijn** - Agents kunnen draaien in containers, on-premise en in meerdere verschillende clouds.
- **Provider-agnostisch zijn** - Agents kunnen worden gemaakt via jouw voorkeurs-SDK, inclusief Azure OpenAI en OpenAI.
- **Integratie van open standaarden** - Agents kunnen protocollen zoals Agent-to-Agent (A2A) en Model Context Protocol (MCP) gebruiken om andere agents en tools te ontdekken en te gebruiken.
- **Plugins en connectors** - Verbindingen kunnen worden gemaakt met data- en geheugendiensten zoals Microsoft Fabric, SharePoint, Pinecone en Qdrant.

Laten we kijken hoe deze functies worden toegepast op enkele kernconcepten van Microsoft Agent Framework.

## Kernconcepten van Microsoft Agent Framework

### Agents

![Agent Framework](../../../translated_images/nl/agent-components.410a06daf87b4fef.webp)

**Agents maken**

Het maken van een agent gebeurt door het definiëren van de inference service (LLM Provider), een set instructies die de AI-agent moet volgen, en een toegewezen `name`:

```python
agent = AzureOpenAIChatClient(credential=AzureCliCredential()).create_agent( instructions="You are good at recommending trips to customers based on their preferences.", name="TripRecommender" )
```

Bovenstaand voorbeeld maakt gebruik van `Azure OpenAI`, maar agents kunnen worden gemaakt met verschillende services, inclusief `Microsoft Foundry Agent Service`:

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

of remote agents via het A2A-protocol:

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

Elke uitvoering van een agent kan ook opties hebben om parameters aan te passen zoals `max_tokens` die door de agent worden gebruikt, `tools` die de agent kan aanroepen, en zelfs het `model` dat door de agent wordt ingezet.

Dit is nuttig in gevallen waar specifieke modellen of tools nodig zijn om een taak van de gebruiker te voltooien.

**Tools**

Tools kunnen worden gedefinieerd zowel bij het definiëren van de agent:

```python
def get_attractions( location: Annotated[str, Field(description="The location to get the top tourist attractions for")], ) -> str: """Get the top tourist attractions for a given location.""" return f"The top attractions for {location} are." 


# Bij het direct aanmaken van een ChatAgent

agent = ChatAgent( chat_client=OpenAIChatClient(), instructions="You are a helpful assistant", tools=[get_attractions]

```

alsook bij het uitvoeren van de agent:

```python

result1 = await agent.run( "What's the best place to visit in Seattle?", tools=[get_attractions] # Hulpmiddel alleen geleverd voor deze uitvoering )
```

**Agent Threads**

Agent Threads worden gebruikt om multi-turn gesprekken te beheren. Threads kunnen worden gemaakt door:

- Gebruik van `get_new_thread()` waarmee de thread over tijd kan worden opgeslagen
- Het automatisch creëren van een thread bij het uitvoeren van een agent waarbij de thread alleen tijdens de huidige uitvoering bestaat.

Om een thread te maken, ziet de code er als volgt uit:

```python
# Maak een nieuwe thread aan.
thread = agent.get_new_thread() # Voer de agent uit met de thread.
response = await agent.run("Hello, I am here to help you book travel. Where would you like to go?", thread=thread)

```

Je kunt vervolgens de thread serialiseren om deze later op te slaan:

```python
# Maak een nieuwe thread aan.
thread = agent.get_new_thread() 

# Voer de agent uit met de thread.

response = await agent.run("Hello, how are you?", thread=thread) 

# Serialiseer de thread voor opslag.

serialized_thread = await thread.serialize() 

# Deserialiseer de threadstatus na het laden uit opslag.

resumed_thread = await agent.deserialize_thread(serialized_thread)
```

**Agent Middleware**

Agents communiceren met tools en LLMs om taken van gebruikers te voltooien. In bepaalde scenario's willen we tussen deze interacties acties uitvoeren of bijhouden. Agent middleware stelt ons in staat dit te doen via:

*Function Middleware*

Deze middleware stelt ons in staat om een actie uit te voeren tussen de agent en een functie/tool die het zal aanroepen. Een voorbeeld waarbij dit gebruikt kan worden is het loggen van een functieaanroep.

In de onderstaande code bepaalt `next` of de volgende middleware of de daadwerkelijke functie wordt opgeroepen.

```python
async def logging_function_middleware(
    context: FunctionInvocationContext,
    next: Callable[[FunctionInvocationContext], Awaitable[None]],
) -> None:
    """Function middleware that logs function execution."""
    # Voorbewerking: Loggen vóór functie-uitvoering
    print(f"[Function] Calling {context.function.name}")

    # Ga door naar de volgende middleware of functie-uitvoering
    await next(context)

    # Nabewerking: Loggen na functie-uitvoering
    print(f"[Function] {context.function.name} completed")
```

*Chat Middleware*

Deze middleware maakt het mogelijk te handelen of loggen tussen de agent en de verzoeken aan de LLM.

Dit bevat belangrijke informatie zoals de `messages` die naar de AI-service worden gestuurd.

```python
async def logging_chat_middleware(
    context: ChatContext,
    next: Callable[[ChatContext], Awaitable[None]],
) -> None:
    """Chat middleware that logs AI interactions."""
    # Voorbewerking: Loggen vóór AI-aanroep
    print(f"[Chat] Sending {len(context.messages)} messages to AI")

    # Ga verder naar de volgende middleware of AI-service
    await next(context)

    # Nabewerking: Loggen na AI-antwoord
    print("[Chat] AI response received")

```

**Agent Memory**

Zoals behandeld in de les `Agentic Memory`, is geheugen een belangrijk element om de agent over verschillende contexten te laten opereren. MAF biedt verschillende soorten geheugen:

*In-Memory Opslag*

Dit is het geheugen dat in threads wordt opgeslagen tijdens de uitvoering van de applicatie.

```python
# Maak een nieuwe thread aan.
thread = agent.get_new_thread() # Voer de agent uit met de thread.
response = await agent.run("Hello, I am here to help you book travel. Where would you like to go?", thread=thread)
```

*Persistent Messages*

Dit geheugen wordt gebruikt om gespreksgeschiedenis op te slaan over verschillende sessies. Het wordt gedefinieerd met de `chat_message_store_factory`:

```python
from agent_framework import ChatMessageStore

# Maak een aangepaste berichtenopslag
def create_message_store():
    return ChatMessageStore()

agent = ChatAgent(
    chat_client=OpenAIChatClient(),
    instructions="You are a Travel assistant.",
    chat_message_store_factory=create_message_store
)

```

*Dynamisch geheugen*

Dit geheugen wordt toegevoegd aan de context voordat agents worden uitgevoerd. Deze geheugens kunnen worden opgeslagen in externe diensten zoals mem0:

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

Observability is belangrijk om betrouwbare en onderhoudbare agentgebaseerde systemen te bouwen. MAF integreert met OpenTelemetry om tracing en meters te bieden voor betere observeerbaarheid.

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

MAF biedt workflows die vooraf gedefinieerde stappen zijn om een taak te voltooien en AI-agents als componenten in die stappen bevatten.

Workflows bestaan uit verschillende componenten die een betere controle over de stroom mogelijk maken. Workflows ondersteunen ook **multi-agent orkestratie** en **checkpointing** om de workflowstatussen op te slaan.

De kerncomponenten van een workflow zijn:

**Executors**

Executors ontvangen inputberichten, voeren hun toegewezen taken uit en produceren vervolgens een outputbericht. Dit brengt de workflow vooruit richting het voltooien van de grotere taak. Executors kunnen zowel AI-agenten als aangepaste logica zijn.

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

*Voorwaardelijke Edges* - Geactiveerd nadat aan een bepaalde voorwaarde is voldaan. Bijvoorbeeld als hotelkamers niet beschikbaar zijn, kan een executor andere opties voorstellen.

*Switch-case Edges* - Leidt berichten naar verschillende executors op basis van gedefinieerde voorwaarden. Bijvoorbeeld als een reisklant prioriteitstoegang heeft en hun taken via een andere workflow worden afgehandeld.

*Fan-out Edges* - Sturen één bericht naar meerdere doelen.

*Fan-in Edges* - Verzamelen meerdere berichten van verschillende executors en sturen ze naar één doel.

**Events**

Om betere observability in workflows te bieden, heeft MAF ingebouwde events voor uitvoering, waaronder:

- `WorkflowStartedEvent`  - Workflow uitvoering begint
- `WorkflowOutputEvent` - Workflow produceert een output
- `WorkflowErrorEvent` - Workflow ondervindt een fout
- `ExecutorInvokeEvent`  - Executor begint verwerking
- `ExecutorCompleteEvent`  -  Executor voltooit verwerking
- `RequestInfoEvent` - Een verzoek wordt verstuurd

## Geavanceerde MAF-patronen

De bovenstaande secties behandelen de kernconcepten van Microsoft Agent Framework. Naarmate je complexere agents bouwt, zijn hier enkele geavanceerde patronen om te overwegen:

- **Middleware-compositie**: Koppel meerdere middleware handlers (logging, authenticatie, rate-limiting) met function en chat middleware voor fijnmazige controle over het gedrag van de agent.
- **Workflow-checkpointing**: Gebruik workflowevents en serialisatie om langlopende agentprocessen op te slaan en te hervatten.
- **Dynamische toolselectie**: Combineer RAG over toolbeschrijvingen met MAF’s toolregistratie om alleen relevante tools per query te presenteren.
- **Multi-agent overdracht**: Gebruik workflowedges en voorwaardelijke routering om overdrachten tussen gespecialiseerde agents te orkestreren.

## Codevoorbeelden 

Codevoorbeelden voor Microsoft Agent Framework zijn te vinden in deze repository onder de bestanden `xx-python-agent-framework` en `xx-dotnet-agent-framework`.

## Meer vragen over Microsoft Agent Framework?

Word lid van de [Microsoft Foundry Discord](https://aka.ms/ai-agents/discord) om andere leerlingen te ontmoeten, kantooruren bij te wonen en antwoorden op je AI Agents-vragen te krijgen.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:  
Dit document is vertaald met behulp van de AI-vertalingsdienst [Co-op Translator](https://github.com/Azure/co-op-translator). Hoewel we streven naar nauwkeurigheid, dient u er rekening mee te houden dat automatische vertalingen fouten of onjuistheden kunnen bevatten. Het originele document in de oorspronkelijke taal wordt beschouwd als de gezaghebbende bron. Voor cruciale informatie wordt professionele menselijke vertaling aanbevolen. Wij zijn niet aansprakelijk voor eventuele misverstanden of verkeerde interpretaties die voortvloeien uit het gebruik van deze vertaling.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->