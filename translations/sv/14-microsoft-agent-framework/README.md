# Utforska Microsoft Agent Framework

![Agent Framework](../../../translated_images/sv/lesson-14-thumbnail.90df0065b9d234ee.webp)

### Introduktion

Denna lektion kommer att täcka:

- Förstå Microsoft Agent Framework: Nyckelfunktioner och värde  
- Utforska nyckelkoncepten i Microsoft Agent Framework
- Avancerade MAF-mönster: Arbetsflöden, middleware och minne

## Lärandemål

Efter att ha slutfört denna lektion kommer du att kunna:

- Bygga produktionsklara AI-agenter med Microsoft Agent Framework
- Använda kärnfunktionerna i Microsoft Agent Framework för dina agentiska användningsfall
- Använda avancerade mönster inklusive arbetsflöden, middleware och observerbarhet

## Kodexempel

Kodexempel för [Microsoft Agent Framework (MAF)](https://aka.ms/ai-agents-beginners/agent-framewrok) finns i detta repository under filerna `xx-python-agent-framework` och `xx-dotnet-agent-framework`.

## Förstå Microsoft Agent Framework

![Framework Intro](../../../translated_images/sv/framework-intro.077af16617cf130c.webp)

[Microsoft Agent Framework (MAF)](https://aka.ms/ai-agents-beginners/agent-framewrok) är Microsofts enhetliga ramverk för att bygga AI-agenter. Det erbjuder flexibilitet för att hantera den stora variationen av agentiska användningsfall som ses i både produktions- och forskningsmiljöer, inklusive:

- **Sekventiell agentorkestrering** i scenarier där steg-för-steg arbetsflöden behövs.
- **Samtida orkestrering** i scenarier där agenter behöver slutföra uppgifter samtidigt.
- **Gruppchattorkestrering** i scenarier där agenter kan samarbeta om en uppgift.
- **Överlämningsorkestrering** i scenarier där agenter överlämnar uppgiften till varandra när deluppgifterna är klara.
- **Magnetisk orkestrering** i scenarier där en chefagent skapar och ändrar en uppgiftslista och hanterar samordningen av underagenter för att slutföra uppgiften.

För att leverera AI-agenter i produktion har MAF också funktioner för:

- **Observerbarhet** genom användning av OpenTelemetry där varje åtgärd av AI-agenten inklusive verktygsanrop, orkestreringssteg, resonemangsflöden och prestandaövervakning sker via Microsoft Foundry-dashboardar.
- **Säkerhet** genom att hosta agenter inbyggt på Microsoft Foundry, vilket inkluderar säkerhetskontroller som rollbaserad åtkomst, hantering av privat data och inbyggd innehållssäkerhet.
- **Hållbarhet** eftersom agenttrådar och arbetsflöden kan pausas, återupptas och återhämta sig från fel, vilket möjliggör längre processer.
- **Kontroll** då arbetsflöden med mänsklig inblandning stöds där uppgifter markeras som kräver mänskligt godkännande.

Microsoft Agent Framework är också inriktat på interoperabilitet genom att:

- **Vara molnoberoende** - Agenter kan köras i containrar, lokalt och över flera olika moln.
- **Vara leverantörsoberoende** - Agenter kan skapas genom ditt föredragna SDK inklusive Azure OpenAI och OpenAI
- **Integrera öppna standarder** - Agenter kan använda protokoll såsom Agent-to-Agent (A2A) och Model Context Protocol (MCP) för att upptäcka och använda andra agenter och verktyg.
- **Plugins och kopplingar** - Anslutningar kan göras till data- och minnestjänster såsom Microsoft Fabric, SharePoint, Pinecone och Qdrant.

Låt oss titta på hur dessa funktioner tillämpas på några av kärnkoncepten i Microsoft Agent Framework.

## Nyckelkoncept i Microsoft Agent Framework

### Agenter

![Agent Framework](../../../translated_images/sv/agent-components.410a06daf87b4fef.webp)

**Skapa agenter**

Agentskapande görs genom att definiera inferenstjänsten (LLM Provider), en
uppsättning instruktioner för AI-agenten att följa, och ett tilldelat `name`:

```python
agent = AzureOpenAIChatClient(credential=AzureCliCredential()).create_agent( instructions="You are good at recommending trips to customers based on their preferences.", name="TripRecommender" )
```

Ovan används `Azure OpenAI` men agenter kan skapas med en mängd olika tjänster inklusive `Microsoft Foundry Agent Service`:

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

eller fjärrstyrda agenter med A2A-protokollet:

```python
agent = A2AAgent( name=agent_card.name, description=agent_card.description, agent_card=agent_card, url="https://your-a2a-agent-host" )
```

**Köra agenter**

Agenter körs med `.run` eller `.run_stream` metoder för antingen icke-strömmade eller strömmade svar.

```python
result = await agent.run("What are good places to visit in Amsterdam?")
print(result.text)
```

```python
async for update in agent.run_stream("What are the good places to visit in Amsterdam?"):
    if update.text:
        print(update.text, end="", flush=True)

```

Varje agentkörning kan också ha alternativ för att anpassa parametrar som `max_tokens` som används av agenten, `tools` som agenten kan anropa, och till och med den `model` som används för agenten.

Detta är användbart i fall där specifika modeller eller verktyg krävs för att slutföra en användares uppgift.

**Verktyg**

Verktyg kan definieras både när agenten definieras:

```python
def get_attractions( location: Annotated[str, Field(description="The location to get the top tourist attractions for")], ) -> str: """Get the top tourist attractions for a given location.""" return f"The top attractions for {location} are." 


# När du skapar en ChatAgent direkt

agent = ChatAgent( chat_client=OpenAIChatClient(), instructions="You are a helpful assistant", tools=[get_attractions]

```

och även vid körning av agenten:

```python

result1 = await agent.run( "What's the best place to visit in Seattle?", tools=[get_attractions] # Verktyg tillhandahållet endast för denna körning )
```

**Agenttrådar**

Agenttrådar används för att hantera konversationer med flera vändor. Trådar kan skapas antingen genom:

- Använda `get_new_thread()` vilket möjliggör att tråden sparas över tid
- Skapa en tråd automatiskt vid körning av en agent och bara ha tråden under aktuell körning.

För att skapa en tråd ser koden ut så här:

```python
# Skapa en ny tråd.
thread = agent.get_new_thread() # Kör agenten med tråden.
response = await agent.run("Hello, I am here to help you book travel. Where would you like to go?", thread=thread)

```

Du kan sedan serialisera tråden för att lagras för senare användning:

```python
# Skapa en ny tråd.
thread = agent.get_new_thread() 

# Kör agenten med tråden.

response = await agent.run("Hello, how are you?", thread=thread) 

# Serialisera tråden för lagring.

serialized_thread = await thread.serialize() 

# Deserialisera trådstatus efter inläsning från lagring.

resumed_thread = await agent.deserialize_thread(serialized_thread)
```

**Agent Middleware**

Agenter interagerar med verktyg och LLMs för att utföra användarens uppgifter. I vissa scenarier vill vi utföra eller följa upp mellan dessa interaktioner. Agent-middleware gör detta möjligt genom:

*Funktion Middleware*

Denna middleware låter oss utföra en åtgärd mellan agenten och en funktion/verktyg som den kommer att anropa. Ett exempel där detta kan användas är när du vill logga funktionsanropet.

I koden nedan definierar `next` om nästa middleware eller själva funktionen ska anropas.

```python
async def logging_function_middleware(
    context: FunctionInvocationContext,
    next: Callable[[FunctionInvocationContext], Awaitable[None]],
) -> None:
    """Function middleware that logs function execution."""
    # Förbearbetning: Logga före funktionskörning
    print(f"[Function] Calling {context.function.name}")

    # Fortsätt till nästa middleware eller funktionskörning
    await next(context)

    # Efterbearbetning: Logga efter funktionskörning
    print(f"[Function] {context.function.name} completed")
```

*Chat Middleware*

Denna middleware låter oss utföra eller logga en åtgärd mellan agenten och förfrågningarna mellan LLM.

Detta innehåller viktig information såsom de `messages` som skickas till AI-tjänsten.

```python
async def logging_chat_middleware(
    context: ChatContext,
    next: Callable[[ChatContext], Awaitable[None]],
) -> None:
    """Chat middleware that logs AI interactions."""
    # Förbehandling: Logga före AI-anrop
    print(f"[Chat] Sending {len(context.messages)} messages to AI")

    # Fortsätt till nästa middleware eller AI-tjänst
    await next(context)

    # Efterbearbetning: Logga efter AI-svar
    print("[Chat] AI response received")

```

**Agentminne**

Som täcktes i lektionen `Agentic Memory` är minnet ett viktigt element för att möjliggöra agentens arbete över olika kontexter. MAF erbjuder flera olika typer av minnen:

*I-minne lagring*

Detta är minne som lagras i trådar under applikationens körning.

```python
# Skapa en ny tråd.
thread = agent.get_new_thread() # Kör agenten med tråden.
response = await agent.run("Hello, I am here to help you book travel. Where would you like to go?", thread=thread)
```

*Persistenta meddelanden*

Detta minne används när konversationshistorik lagras över olika sessioner. Det definieras med `chat_message_store_factory`:

```python
from agent_framework import ChatMessageStore

# Skapa en anpassad meddelandelagring
def create_message_store():
    return ChatMessageStore()

agent = ChatAgent(
    chat_client=OpenAIChatClient(),
    instructions="You are a Travel assistant.",
    chat_message_store_factory=create_message_store
)

```

*Dynamiskt minne*

Detta minne läggs till i kontexten innan agenter körs. Dessa minnen kan lagras i externa tjänster såsom mem0:

```python
from agent_framework.mem0 import Mem0Provider

# Använder Mem0 för avancerade minnesfunktioner
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

**Agent-observerbarhet**

Observerbarhet är viktigt för att bygga pålitliga och underhållbara agentiska system. MAF integreras med OpenTelemetry för att tillhandahålla spårning och mätare för bättre observerbarhet.

```python
from agent_framework.observability import get_tracer, get_meter

tracer = get_tracer()
meter = get_meter()
with tracer.start_as_current_span("my_custom_span"):
    # gör något
    pass
counter = meter.create_counter("my_custom_counter")
counter.add(1, {"key": "value"})
```

### Arbetsflöden

MAF erbjuder arbetsflöden som är fördefinierade steg för att slutföra en uppgift och inkluderar AI-agenter som komponenter i dessa steg.

Arbetsflöden består av olika komponenter som möjliggör bättre kontrollflöde. Arbetsflöden möjliggör också **multi-agent orkestrering** och **checkpointing** för att spara arbetsflödets tillstånd.

Kärnkomponenterna i ett arbetsflöde är:

**Exekutörer**

Exekutörer tar emot indata-meddelanden, utför sina tilldelade uppgifter och producerar sedan ett utdata-meddelande. Detta för arbetsflödet framåt mot att slutföra den större uppgiften. Exekutörer kan vara antingen AI-agent eller kundlogik.

**Kanter**

Kanterna används för att definiera flödet av meddelanden i ett arbetsflöde. Dessa kan vara:

*Direkta kanter* - Enkla en-till-en kopplingar mellan exekutörer:

```python
from agent_framework import WorkflowBuilder

builder = WorkflowBuilder()
builder.add_edge(source_executor, target_executor)
builder.set_start_executor(source_executor)
workflow = builder.build()
```

*Villkorliga kanter* - Aktiveras efter att ett visst villkor är uppfyllt. Till exempel, när hotellrum inte är tillgängliga kan en exekutör föreslå andra alternativ.

*Switch-case kanter* - Leder meddelanden till olika exekutörer baserat på definierade villkor. Till exempel om en resenär har prioriterad åtkomst och deras uppgifter hanteras via ett annat arbetsflöde.

*Fan-out kanter* - Skickar ett meddelande till flera mål.

*Fan-in kanter* - Samlar flera meddelanden från olika exekutörer och skickar till ett mål.

**Händelser**

För att ge bättre observerbarhet i arbetsflöden erbjuder MAF inbyggda händelser för exekvering inklusive:

- `WorkflowStartedEvent`  - Arbetsflödesexekvering startar
- `WorkflowOutputEvent` - Arbetsflödet producerar ett utdata
- `WorkflowErrorEvent` - Arbetsflödet stöter på ett fel
- `ExecutorInvokeEvent`  - Exekutör startar behandlingen
- `ExecutorCompleteEvent`  -  Exekutör avslutar behandlingen
- `RequestInfoEvent` - En förfrågan utfärdas

## Avancerade MAF-mönster

Avsnitten ovan täcker nyckelkoncepten i Microsoft Agent Framework. När du bygger mer komplexa agenter, här är några avancerade mönster att överväga:

- **Middleware-komposition**: Kedja flera middleware-handlerare (loggning, autentisering, hastighetsbegränsning) med funktion- och chatmiddleware för finjusterad kontroll över agentens beteende.
- **Checkpointing av arbetsflöden**: Använd arbetsflödets händelser och serialisering för att spara och återuppta långvariga agentprocesser.
- **Dynamiskt verktygsval**: Kombinera RAG över verktygsbeskrivningar med MAF:s verktygsregistrering för att bara presentera relevanta verktyg per förfrågan.
- **Multi-agent överlämning**: Använd arbetsflödets kanter och villkorlig routning för att orkestrera överlämningar mellan specialiserade agenter.

## Kodexempel

Kodexempel för Microsoft Agent Framework finns i detta repository under filerna `xx-python-agent-framework` och `xx-dotnet-agent-framework`.

## Fler frågor om Microsoft Agent Framework?

Gå med i [Microsoft Foundry Discord](https://aka.ms/ai-agents/discord) för att träffa andra elever, delta i kontorstid och få svar på dina frågor om AI-agenter.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfriskrivning**:
Detta dokument har översatts med hjälp av AI-översättningstjänsten [Co-op Translator](https://github.com/Azure/co-op-translator). Trots att vi strävar efter noggrannhet bör du vara medveten om att automatiska översättningar kan innehålla fel eller brister. Det ursprungliga dokumentet på dess ursprungsspråk ska anses vara den auktoritativa källan. För kritisk information rekommenderas professionell mänsklig översättning. Vi ansvarar inte för några missförstånd eller feltolkningar som uppstår vid användning av denna översättning.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->