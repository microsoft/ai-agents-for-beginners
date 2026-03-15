# Prozkoumání Microsoft Agent Framework

![Agent Framework](../../../translated_images/cs/lesson-14-thumbnail.90df0065b9d234ee.webp)

### Úvod

Tato lekce pokryje:

- Pochopení Microsoft Agent Framework: Klíčové funkce a hodnota  
- Prozkoumání klíčových konceptů Microsoft Agent Framework
- Pokročilé vzory MAF: Workflowy, Middleware a Paměť

## Cíle učení

Po dokončení této lekce budete vědět, jak:

- Vytvářet produkčně připravené AI agenty pomocí Microsoft Agent Framework
- Aplikovat základní funkce Microsoft Agent Framework na vaše agenty určené použití
- Používat pokročilé vzory zahrnující workflowy, middleware a observabilitu

## Vzory kódu 

Vzory kódu pro [Microsoft Agent Framework (MAF)](https://aka.ms/ai-agents-beginners/agent-framewrok) najdete v tomto repozitáři v souborech `xx-python-agent-framework` a `xx-dotnet-agent-framework`.

## Pochopení Microsoft Agent Framework

![Framework Intro](../../../translated_images/cs/framework-intro.077af16617cf130c.webp)

[Microsoft Agent Framework (MAF)](https://aka.ms/ai-agents-beginners/agent-framewrok) je jednotný framework společnosti Microsoft pro tvorbu AI agentů. Nabízí flexibilitu k pokrytí široké škály použití agentů, která jsou vidět jak v produkčním, tak výzkumném prostředí, včetně:

- **Sekvenční orchestrace agentů** ve scénářích, kde jsou potřeba postupné workflowy.
- **Současná orchestrace** ve scénářích, kde agenti musí plnit úkoly současně.
- **Orchestrace skupinové konverzace** ve scénářích, kdy agenti spolupracují na jednom úkolu.
- **Předávací orchestrace** ve scénářích, kde si agenti předávají úkol, jakmile jsou dílčí úkoly dokončeny.
- **Magnetická orchestrace** ve scénářích, kdy manažerský agent vytváří a modifikuje seznam úkolů a řídí koordinaci subagentů k dokončení úkolu.

Pro doručení AI agentů v produkci obsahuje MAF také funkce jako:

- **Observabilita** pomocí OpenTelemetry, kde je zaznamenána každá akce AI agenta včetně volání nástrojů, kroků orchestrace, toků rozumování a monitorování výkonu přes Microsoft Foundry dashboardy.
- **Bezpečnost** díky hostování agentů nativně na Microsoft Foundry, které zahrnuje bezpečnostní kontroly jako role-based access, správu soukromých dat a vestavěnou bezpečnost obsahu.
- **Odolnost** protože vlákna agentů a workflowy mohou být pozastavena, obnovena a zotavena z chyb, což umožňuje delší běhy procesů.
- **Kontrola** prostřednictvím podporovaných workflowů s lidským dohledem, kde jsou úkoly označeny jako vyžadující lidské schválení.

Microsoft Agent Framework je také zaměřen na interoperabilitu tím, že:

- **Je nezávislý na cloudu** - Agenti mohou běžet v kontejnerech, on-premise i napříč různými cloudy.
- **Je nezávislý na poskytovateli** - Agenti mohou být vytvořeni pomocí vámi preferovaného SDK, včetně Azure OpenAI a OpenAI.
- **Integruje otevřené standardy** - Agenti mohou využívat protokoly jako Agent-to-Agent (A2A) a Model Context Protocol (MCP) k objevování a používání jiných agentů a nástrojů.
- **Pluginy a konektory** - Lze navazovat spojení na datové a paměťové služby jako Microsoft Fabric, SharePoint, Pinecone a Qdrant.

Podíváme se, jak jsou tyto funkce aplikovány na některé klíčové koncepty Microsoft Agent Framework.

## Klíčové koncepty Microsoft Agent Framework

### Agenti

![Agent Framework](../../../translated_images/cs/agent-components.410a06daf87b4fef.webp)

**Vytváření agentů**

Vytváření agentů se provádí definováním inference služby (poskytovatele LLM), sadu instrukcí, které má AI agent dodržovat, a přiděleným `name`:

```python
agent = AzureOpenAIChatClient(credential=AzureCliCredential()).create_agent( instructions="You are good at recommending trips to customers based on their preferences.", name="TripRecommender" )
```

Výše uvedený příklad používá `Azure OpenAI`, ale agenti mohou být vytvořeni pomocí různých služeb včetně `Microsoft Foundry Agent Service`:

```python
AzureAIAgentClient(async_credential=credential).create_agent( name="HelperAgent", instructions="You are a helpful assistant." ) as agent
```

OpenAI API `Responses`, `ChatCompletion`

```python
agent = OpenAIResponsesClient().create_agent( name="WeatherBot", instructions="You are a helpful weather assistant.", )
```

```python
agent = OpenAIChatClient().create_agent( name="HelpfulAssistant", instructions="You are a helpful assistant.", )
```

nebo vzdálených agentů pomocí protokolu A2A:

```python
agent = A2AAgent( name=agent_card.name, description=agent_card.description, agent_card=agent_card, url="https://your-a2a-agent-host" )
```

**Spouštění agentů**

Agenti se spouští pomocí metod `.run` nebo `.run_stream` pro ne-streamingové nebo streamovací odpovědi.

```python
result = await agent.run("What are good places to visit in Amsterdam?")
print(result.text)
```

```python
async for update in agent.run_stream("What are the good places to visit in Amsterdam?"):
    if update.text:
        print(update.text, end="", flush=True)

```

Každé spuštění agenta může mít také možnosti pro přizpůsobení parametrů jako `max_tokens` použitých agentem, `tools`, které může agent volat, a dokonce i samotný `model`, který agent používá.

To je užitečné v případech, kdy jsou pro dokončení uživatelského úkolu vyžadovány specifické modely nebo nástroje.

**Nástroje**

Nástroje mohou být definovány jak při definování agenta:

```python
def get_attractions( location: Annotated[str, Field(description="The location to get the top tourist attractions for")], ) -> str: """Get the top tourist attractions for a given location.""" return f"The top attractions for {location} are." 


# Při přímém vytváření ChatAgenta

agent = ChatAgent( chat_client=OpenAIChatClient(), instructions="You are a helpful assistant", tools=[get_attractions]

```

tak i při spouštění agenta:

```python

result1 = await agent.run( "What's the best place to visit in Seattle?", tools=[get_attractions] # Nástroj poskytnutý pouze pro tento běh )
```

**Vlákna agentů**

Vlákna agentů slouží k zpracování vícetahových konverzací. Vlákna lze vytvořit buď:

- Pomocí `get_new_thread()`, které umožňuje vlákno ukládat v průběhu času
- Automatickým vytvořením vlákna při spuštění agenta, přičemž vlákno existuje pouze během aktuálního spuštění.

Kód pro vytvoření vlákna vypadá takto:

```python
# Vytvořte nový vlákno.
thread = agent.get_new_thread() # Spusťte agenta s vláknem.
response = await agent.run("Hello, I am here to help you book travel. Where would you like to go?", thread=thread)

```

Poté můžete vlákno serializovat a uložit pro pozdější použití:

```python
# Vytvořit nový vlákno.
thread = agent.get_new_thread() 

# Spustit agenta s vláknem.

response = await agent.run("Hello, how are you?", thread=thread) 

# Serializovat vlákno pro uložení.

serialized_thread = await thread.serialize() 

# Deserializovat stav vlákna po načtení z úložiště.

resumed_thread = await agent.deserialize_thread(serialized_thread)
```

**Agent Middleware**

Agenti komunikují s nástroji a LLM, aby dokončili uživatelské úkoly. V některých scénářích chceme mezi těmito interakcemi něco vykonat nebo sledovat. Agent middleware nám to umožňuje prostřednictvím:

*Middleware funkcí*

Tento middleware nám umožňuje vykonat akci mezi agentem a funkcí/nástrojem, který volá. Příklad použití je, když chcete zaznamenat volání funkce do logu.

V kódu níže `next` určuje, zda má být volán další middleware nebo skutečná funkce.

```python
async def logging_function_middleware(
    context: FunctionInvocationContext,
    next: Callable[[FunctionInvocationContext], Awaitable[None]],
) -> None:
    """Function middleware that logs function execution."""
    # Předzpracování: Záznam před vykonáním funkce
    print(f"[Function] Calling {context.function.name}")

    # Pokračovat k další middleware nebo vykonání funkce
    await next(context)

    # Pozpracování: Záznam po vykonání funkce
    print(f"[Function] {context.function.name} completed")
```

*Chat Middleware*

Tento middleware nám umožňuje vykonat nebo zaznamenat akci mezi agentem a požadavky na LLM.

Obsahuje důležité informace jako `messages`, které jsou posílány AI službě.

```python
async def logging_chat_middleware(
    context: ChatContext,
    next: Callable[[ChatContext], Awaitable[None]],
) -> None:
    """Chat middleware that logs AI interactions."""
    # Předzpracování: Logovat před voláním AI
    print(f"[Chat] Sending {len(context.messages)} messages to AI")

    # Pokračovat k dalšímu middleware nebo AI službě
    await next(context)

    # Pozpracování: Logovat po odpovědi AI
    print("[Chat] AI response received")

```

**Paměť agenta**

Jak bylo pokryto v lekci `Agentic Memory`, paměť je důležitým prvkem umožňujícím agentovi pracovat v různých kontextech. MAF nabízí několik typů pamětí:

*Paměť v rámci aplikace (In-Memory Storage)*

Toto je paměť uložená ve vláknech během běhu aplikace.

```python
# Vytvořit nový vlákno.
thread = agent.get_new_thread() # Spustit agenta ve vlákně.
response = await agent.run("Hello, I am here to help you book travel. Where would you like to go?", thread=thread)
```

*Trvalé zprávy*

Tato paměť se používá pro ukládání historie konverzací napříč různými relacemi. Definuje se pomocí `chat_message_store_factory`:

```python
from agent_framework import ChatMessageStore

# Vytvořit vlastní úložiště zpráv
def create_message_store():
    return ChatMessageStore()

agent = ChatAgent(
    chat_client=OpenAIChatClient(),
    instructions="You are a Travel assistant.",
    chat_message_store_factory=create_message_store
)

```

*Dynamická paměť*

Tato paměť je přidána do kontextu před spuštěním agentů. Tyto paměti mohou být uloženy v externích službách jako mem0:

```python
from agent_framework.mem0 import Mem0Provider

# Použití Mem0 pro pokročilé paměťové schopnosti
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

**Observabilita agenta**

Observabilita je důležitá pro tvorbu spolehlivých a udržitelných agentických systémů. MAF integruje OpenTelemetry pro poskytování sledování a měření pro lepší observabilitu.

```python
from agent_framework.observability import get_tracer, get_meter

tracer = get_tracer()
meter = get_meter()
with tracer.start_as_current_span("my_custom_span"):
    # udělej něco
    pass
counter = meter.create_counter("my_custom_counter")
counter.add(1, {"key": "value"})
```

### Workflowy

MAF nabízí workflowy, což jsou předem definované kroky k dokončení úkolu, které zahrnují AI agenty jako komponenty v těchto krocích.

Workflowy se skládají z různých komponent, které umožňují lepší řízení toku. Workflowy také podporují **multi-agent orchestrace** a **checkpointing** pro ukládání stavů workflow.

Základními komponentami workflow jsou:

**Executors**

Executors přijímají vstupní zprávy, provádějí přidělené úkoly a produkují výstupní zprávu. To posouvá workflow vpřed k dokončení většího úkolu. Executors mohou být buď AI agenti nebo vlastní logika.

**Hrany (Edges)**

Hrany se používají k definování toku zpráv ve workflow. Tyto mohou být:

*Přímé hrany* - Jednoduché přímé spojení mezi executory:

```python
from agent_framework import WorkflowBuilder

builder = WorkflowBuilder()
builder.add_edge(source_executor, target_executor)
builder.set_start_executor(source_executor)
workflow = builder.build()
```

*Podmíněné hrany* - Aktivují se po splnění určité podmínky. Například pokud nejsou k dispozici hotelové pokoje, executor může navrhnout jiné možnosti.

*Switch-case hrany* - Směrují zprávy k různým executorům na základě definovaných podmínek. Například pokud má zákazník cestování prioritní přístup a jeho úkoly budou řešeny jiným workflow.

*Fan-out hrany* - Posílají jednu zprávu více cílům.

*Fan-in hrany* - Sbírají více zpráv z různých executorů a posílají je jednomu cíli.

**Události (Events)**

Pro lepší observabilitu workflow, MAF nabízí vestavěné události pro vykonávání včetně:

- `WorkflowStartedEvent`  - Zahájení vykonávání workflow
- `WorkflowOutputEvent` - Workflow vytvoří výstup
- `WorkflowErrorEvent` - Workflow narazí na chybu
- `ExecutorInvokeEvent`  - Executor začne zpracování
- `ExecutorCompleteEvent`  -  Executor dokončí zpracování
- `RequestInfoEvent` - Odeslán požadavek

## Pokročilé vzory MAF

Výše uvedené sekce pokrývají klíčové koncepty Microsoft Agent Framework. Jak vytváříte složitější agenty, zde jsou některé pokročilé vzory k zvážení:

- **Skládání middleware**: Řetězení více handlerů middleware (logování, autentizace, omezení rychlosti) používáním funkčního a chat middleware pro jemné ovládání chování agenta.
- **Checkpointing workflowu**: Použití událostí workflow a serializace k ukládání a obnově dlouho běžících procesů agentů.
- **Dynamický výběr nástrojů**: Kombinování RAG přes popisy nástrojů s registrací nástrojů v MAF k prezentaci relevantních nástrojů pro konkrétní dotaz.
- **Předávání mezi více agenty**: Použití hran workflow a podmíněného směrování k orchestraci předávání mezi specializovanými agenty.

## Vzory kódu 

Vzory kódu pro Microsoft Agent Framework najdete v tomto repozitáři v souborech `xx-python-agent-framework` a `xx-dotnet-agent-framework`.

## Máte další otázky ohledně Microsoft Agent Framework?

Připojte se na [Microsoft Foundry Discord](https://aka.ms/ai-agents/discord), kde se můžete setkat s dalšími studenty, navštěvovat konzultační hodiny a mít zodpovězené otázky o AI agentech.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Prohlášení o vyloučení odpovědnosti**:
Tento dokument byl přeložen pomocí AI překladatelské služby [Co-op Translator](https://github.com/Azure/co-op-translator). Přestože usilujeme o přesnost, mějte prosím na paměti, že automatizované překlady mohou obsahovat chyby nebo nepřesnosti. Původní dokument v jeho rodném jazyce by měl být považován za závazný zdroj. Pro kritické informace se doporučuje profesionální lidský překlad. Nejsme odpovědní za jakékoliv nedorozumění nebo mylné výklady vyplývající z použití tohoto překladu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->