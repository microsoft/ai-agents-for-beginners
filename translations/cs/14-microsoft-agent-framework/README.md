# Prozkoumání Microsoft Agent Framework

![Agent Framework](../../../translated_images/cs/lesson-14-thumbnail.90df0065b9d234ee.webp)

### Úvod

Tato lekce pokryje:

- Pochopení Microsoft Agent Framework: Klíčové vlastnosti a hodnota  
- Prozkoumání klíčových konceptů Microsoft Agent Framework
- Pokročilé vzory MAF: Pracovní postupy, middleware a paměť

## Vzdělávací cíle

Po dokončení této lekce budete vědět, jak:

- Vytvořit produkčně připravené AI agenty pomocí Microsoft Agent Framework
- Aplikovat základní funkce Microsoft Agent Framework ve vašich agentních použitích
- Používat pokročilé vzory zahrnující pracovní postupy, middleware a pozorovatelnost

## Ukázky kódu 

Ukázky kódu pro [Microsoft Agent Framework (MAF)](https://learn.microsoft.com/en-us/agent-framework/overview/?wt.mc_id=youtube_26688_organicsocial_reactor&pivots=programming-language-python) naleznete v tomto repozitáři v souborech `xx-python-agent-framework` a `xx-dotnet-agent-framework`.

## Pochopení Microsoft Agent Framework

![Framework Intro](../../../translated_images/cs/framework-intro.077af16617cf130c.webp)

[Microsoft Agent Framework (MAF)](https://learn.microsoft.com/en-us/agent-framework/overview/?wt.mc_id=youtube_26688_organicsocial_reactor&pivots=programming-language-python) je jednotný rámec Microsoftu pro vytváření AI agentů. Nabízí flexibilitu pro řešení široké škály agentních případů použití jak v produkčních, tak výzkumných prostředích, včetně:

- **Sekvenční orchestrace agentů** ve scénářích, kde jsou potřeba postupné pracovní postupy.
- **Současná orchestrace** ve scénářích, kde agenti potřebují dokončit úkoly současně.
- **Orchestrace skupinových chatů** ve scénářích, kde agenti spolupracují na jednom úkolu.
- **Orchestrace předávání úkolů** ve scénářích, kde si agenti předávají úkoly, jakmile jsou dílčí úkoly dokončeny.
- **Magnetická orchestrace** ve scénářích, kde manažerský agent vytváří a upravuje seznam úkolů a koordinuje podagenty k dokončení úkolu.

Pro nasazení AI Agentů v produkci má MAF také zahrnuté funkce pro:

- **Pozorovatelnost** pomocí OpenTelemetry, kde každá akce AI Agenta včetně vyvolání nástroje, orchestrací kroků, toků uvažování a monitorování výkonu přes dashboardy Microsoft Foundry.
- **Bezpečnost** díky hostování agentů nativně na Microsoft Foundry, které zahrnuje bezpečnostní kontroly jako přístup založený na rolích, nakládání s privátními daty a vestavěnou obsahovou bezpečnost.
- **Odolnost** protože vlákna a pracovní postupy agentů mohou být pauzovány, obnoveny a zotaveny z chyb, což umožňuje dlouhodobě běžící procesy.
- **Kontrola** protože jsou podporovány pracovní postupy s lidským dohledem, kde jsou úkoly označeny jako vyžadující lidské schválení.

Microsoft Agent Framework se také zaměřuje na interoperabilitu tím, že:

- **Je nezávislý na cloudu** - Agenti mohou běžet v kontejnerech, on-premises a přes různé cloudové platformy.
- **Je nezávislý na poskytovateli** - Agenti mohou být tvořeni pomocí vašeho preferovaného SDK včetně Azure OpenAI a OpenAI.
- **Integruje otevřené standardy** - Agenti mohou využívat protokoly jako Agent-to-Agent (A2A) a Model Context Protocol (MCP) k propojování a používání jiných agentů a nástrojů.
- **Pluginy a konektory** - Spojení mohou být vytvořena se službami pro data a paměť, jako jsou Microsoft Fabric, SharePoint, Pinecone a Qdrant.

Podívejme se, jak se tyto funkce aplikují na některé základní koncepty Microsoft Agent Framework.

## Klíčové koncepty Microsoft Agent Framework

### Agenti

![Agent Framework](../../../translated_images/cs/agent-components.410a06daf87b4fef.webp)

**Tvorba agentů**

Tvorba agentů se provádí definováním inference služby (poskytovatel LLM), 
sady instrukcí, které má AI Agent následovat, a přiřazeného `name` (jména):

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

nebo [MiniMax](https://platform.minimaxi.com/), který poskytuje OpenAI-kompatibilní API s velkými kontextovými okny (až 204K tokenů):

```python
agent = OpenAIChatClient(base_url="https://api.minimax.io/v1", api_key=os.environ["MINIMAX_API_KEY"], model_id="MiniMax-M3").create_agent( name="HelpfulAssistant", instructions="You are a helpful assistant.", )
```

nebo vzdálené agenty používající protokol A2A:

```python
agent = A2AAgent( name=agent_card.name, description=agent_card.description, agent_card=agent_card, url="https://your-a2a-agent-host" )
```

**Spouštění agentů**

Agenti jsou spouštěni pomocí metod `.run` nebo `.run_stream` pro nereálné nebo streamované odpovědi.

```python
result = await agent.run("What are good places to visit in Amsterdam?")
print(result.text)
```

```python
async for update in agent.run_stream("What are the good places to visit in Amsterdam?"):
    if update.text:
        print(update.text, end="", flush=True)

```

Každý běh agenta také může mít volby pro přizpůsobení parametrů jako `max_tokens`, které agent využívá, `tools`, které může agent vyvolávat, a dokonce i samotný `model` použitý agentem.

To je užitečné v případech, kdy jsou pro dokončení uživatelského úkolu požadovány specifické modely nebo nástroje.

**Nástroje**

Nástroje mohou být definovány jak během definice agenta:

```python
def get_attractions( location: Annotated[str, Field(description="The location to get the top tourist attractions for")], ) -> str: """Get the top tourist attractions for a given location.""" return f"The top attractions for {location} are." 


# Při přímém vytváření ChatAgenta

agent = ChatAgent( chat_client=OpenAIChatClient(), instructions="You are a helpful assistant", tools=[get_attractions]

```

a také při spuštění agenta:

```python

result1 = await agent.run( "What's the best place to visit in Seattle?", tools=[get_attractions] # Nástroj poskytnutý pouze pro tento běh )
```

**Vlákna agentů**

Vlákna agentů se používají pro vícetahové konverzace. Vlákna mohou být vytvořena buď:

- Použitím `get_new_thread()`, což umožňuje vlákno ukládat v průběhu času
- Automatickým vytvořením vlákna při spuštění agenta, které trvá pouze během aktuálního běhu.

K vytvoření vlákna vypadá kód takto:

```python
# Vytvořit nový vlákno.
thread = agent.get_new_thread() # Spusťte agenta s vláknem.
response = await agent.run("Hello, I am here to help you book travel. Where would you like to go?", thread=thread)

```

Pak můžete vlákno serializovat pro pozdější uložení:

```python
# Vytvořit nový vlákno.
thread = agent.get_new_thread() 

# Spustit agenta s vláknem.

response = await agent.run("Hello, how are you?", thread=thread) 

# Serializovat vlákno pro ukládání.

serialized_thread = await thread.serialize() 

# Deserializovat stav vlákna po načtení z úložiště.

resumed_thread = await agent.deserialize_thread(serialized_thread)
```

**Agent Middleware**

Agenti interagují s nástroji a LLM k dokončení úkolů uživatelů. V určitých scénářích chceme mezi těmito interakcemi provádět nebo sledovat akce. Middleware agentů nám to umožňuje prostřednictvím:

*Funkční Middleware*

Tento middleware nám umožňuje vykonat akci mezi agentem a funkcí/nástrojem, který bude volat. Příkladem použití je, když chcete zaznamenávat volání funkce.

V kódu níže `next` určuje, zda má být zavolán další middleware nebo skutečná funkce.

```python
async def logging_function_middleware(
    context: FunctionInvocationContext,
    next: Callable[[FunctionInvocationContext], Awaitable[None]],
) -> None:
    """Function middleware that logs function execution."""
    # Předzpracování: Záznam před vykonáním funkce
    print(f"[Function] Calling {context.function.name}")

    # Pokračovat k dalšímu middleware nebo vykonání funkce
    await next(context)

    # Pozpracování: Záznam po vykonání funkce
    print(f"[Function] {context.function.name} completed")
```

*Chat Middleware*

Tento middleware nám umožňuje vykonat nebo zaznamenat akci mezi agentem a požadavky mezi LLM.

Obsahuje důležité informace jako `messages`, které jsou posílány AI službě.

```python
async def logging_chat_middleware(
    context: ChatContext,
    next: Callable[[ChatContext], Awaitable[None]],
) -> None:
    """Chat middleware that logs AI interactions."""
    # Předzpracování: Protokolovat před voláním AI
    print(f"[Chat] Sending {len(context.messages)} messages to AI")

    # Pokračovat k dalšímu middleware nebo AI službě
    await next(context)

    # Post-processing: Protokolovat po odpovědi AI
    print("[Chat] AI response received")

```

**Paměť agentů**

Jak bylo uvedeno v lekci `Agentic Memory`, paměť je důležitým prvkem umožňujícím agentovi pracovat v různých kontextech. MAF nabízí několik různých typů pamětí:

*Paměť v rámci aplikace (In-Memory Storage)*

Tato paměť je uchovávána ve vláknech během běhu aplikace.

```python
# Vytvořit nové vlákno.
thread = agent.get_new_thread() # Spustit agenta s vlákna.
response = await agent.run("Hello, I am here to help you book travel. Where would you like to go?", thread=thread)
```

*Trvalé zprávy (Persistent Messages)*

Tato paměť se používá pro uchovávání historie konverzací mezi různými relacemi. Definuje se pomocí `chat_message_store_factory`:

```python
from agent_framework import ChatMessageStore

# Vytvořte vlastní úložiště zpráv
def create_message_store():
    return ChatMessageStore()

agent = ChatAgent(
    chat_client=OpenAIChatClient(),
    instructions="You are a Travel assistant.",
    chat_message_store_factory=create_message_store
)

```

*Dynamická paměť (Dynamic Memory)*

Tato paměť je přidána do kontextu před spuštěním agentů. Paměti mohou být uloženy ve vnějších službách, například mem0:

```python
from agent_framework.mem0 import Mem0Provider

# Používání Mem0 pro pokročilé paměťové schopnosti
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

**Pozorovatelnost agentů**

Pozorovatelnost je důležitá pro budování spolehlivých a udržitelných agentních systémů. MAF se integruje s OpenTelemetry pro zpětné sledování a měření pro lepší pozorovatelnost.

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

### Pracovní postupy

MAF nabízí pracovní postupy, což jsou předdefinované kroky k dokončení úkolu a zahrnují AI agenty jako součásti těchto kroků.

Pracovní postupy se skládají z různých komponent, které umožňují lepší řízení toku. Pracovní postupy také umožňují **multi-agent orchestrace** a **checkpointing** pro ukládání stavů pracovních postupů.

Hlavní komponenty pracovního postupu jsou:

**Vykonavatelé (Executors)**

Vykonavatelé přijímají vstupní zprávy, provádějí své přidělené úkoly a poté produkují výstupní zprávu. Posouvají pracovní postup kupředu směrem k dokončení většího úkolu. Vykonavatelé mohou být AI agentem nebo vlastní logikou.

**Hrany (Edges)**

Hrany se používají k definování toku zpráv v pracovním postupu. Mohou být:

*Přímé hrany* - Jednoduchá spojení jeden-na-jeden mezi vykonavateli:

```python
from agent_framework import WorkflowBuilder

builder = WorkflowBuilder()
builder.add_edge(source_executor, target_executor)
builder.set_start_executor(source_executor)
workflow = builder.build()
```

*Podmíněné hrany* - Aktivují se po splnění určité podmínky. Například když nejsou dostupné hotelové pokoje, vykonavatel může navrhnout jiné možnosti.

*Hrany typu switch-case* - Posílají zprávy různým vykonavatelům na základě definovaných podmínek. Například pokud má zákazník prioritní přístup, jeho úkoly budou řešeny jiným pracovním postupem.

*Rozvětvující hrany (Fan-out Edges)* - Odesílají jednu zprávu více cílům.

*Sběrné hrany (Fan-in Edges)* - Sbírají více zpráv od různých vykonavatelů a posílají je jednomu cíli.

**Události (Events)**

Pro lepší pozorovatelnost pracovních postupů nabízí MAF vestavěné události vykonávání, včetně:

- `WorkflowStartedEvent`  - Začátek vykonávání pracovního postupu
- `WorkflowOutputEvent` - Pracovní postup produkoval výstup
- `WorkflowErrorEvent` - Pracovní postup narazil na chybu
- `ExecutorInvokeEvent`  - Vykonavatel začal zpracovávat
- `ExecutorCompleteEvent`  -  Vykonavatel dokončil zpracování
- `RequestInfoEvent` - Požadavek byl vydán

## Pokročilé vzory MAF

Výše uvedené části pokrývají klíčové koncepty Microsoft Agent Framework. Jak vytváříte složitější agenty, zde jsou některé pokročilé vzory k úvaze:

- **Skládání middleware**: Řetězení více middleware handlerů (logování, autentizace, omezení rychlosti) pomocí funkčního a chat middleware pro jemnou kontrolu chování agenta.
- **Checkpointing pracovních postupů**: Použití událostí pracovních postupů a serializace k ukládání a obnovení dlouhých agentních procesů.
- **Dynamický výběr nástrojů**: Kombinujte RAG nad popisy nástrojů s registrací nástrojů MAF k prezentaci pouze relevantních nástrojů pro dotaz.
- **Předávání mezi více agenty**: Použijte hrany pracovních postupů a podmíněné přesměrování k orchestraci předávání mezi specializovanými agenty.

## Hostování LangChain / LangGraph agentů na Microsoft Foundry

Microsoft Agent Framework je **rámcově interoperabilní** — nejste omezeni pouze na agenty napsané s MAF. Pokud už máte agenta vytvořeného pomocí **LangChain** nebo **LangGraph**, můžete jej spustit jako **hostovaného agenta Microsoft Foundry**, takže Foundry spravuje runtime, relace, škálování, identitu a protokolové koncové body za vás, zatímco vaše agentní logika zůstává v LangGraph.

To se provádí pomocí balíčku `langchain_azure_ai.agents.hosting`, který vystavuje zkompilovaný LangGraph graf přes stejné protokoly, které používají hostovaní agenti Foundry.

**1. Nainstalujte hosting extra:**

```bash
pip install -U "langchain-azure-ai[hosting]>=1.2.4" azure-identity
```

Extra `hosting` instaluje Foundry protokolové knihovny: `azure-ai-agentserver-responses` (OpenAI-kompatibilní koncový bod `/responses`) a `azure-ai-agentserver-invocations` (obecný koncový bod `/invocations`).

**2. Vyberte hostingový protokol:**

| Protokol | Hostitelská třída | Koncový bod | Použití kdy |
|----------|-----------|----------|----------|
| **Responses** | `ResponsesHostServer` | `/responses` | Chcete OpenAI-kompatibilní chat, streamování, historii odpovědí a vlákna konverzace — doporučený výchozí režim pro konverzační agenty. |
| **Invocations** | `InvocationsHostServer` | `/invocations` | Potřebujete vlastní JSON tvar, webhookový endpoint nebo ne-konverzační zpracování. |

Protože **Responses API je primární API pro vývoj agentů ve Foundry**, začněte s `ResponsesHostServer` pro většinu agentů.

**3. Nakonfigurujte proměnné prostředí** (`az login` nejprve, aby se mohl ověřit `DefaultAzureCredential`):

```bash
export FOUNDRY_PROJECT_ENDPOINT="https://<resource>.services.ai.azure.com/api/projects/<project>"
export FOUNDRY_MODEL_NAME="gpt-5-mini"
```

Když agent později poběží jako hostovaný agent ve Foundry, platforma automaticky injektuje `FOUNDRY_PROJECT_ENDPOINT`.

**4. Vystavte LangGraph agenta přes protokol Responses:**

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

    # ChatOpenAI zde cílí na OpenAI-kompatibilní (Responses) koncový bod v projektu Foundry.
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

Spusťte jej lokálně pomocí `python main.py`, poté pošlete požadavek Responses na `http://localhost:8088/responses`.

**Klíčové chování:**

- **Konverzace**: Klienti pokračují v konverzaci předáváním `previous_response_id` nebo ID `conversation`. Pokud je váš graf zkompilován s LangGraph checkpointem, Foundry mapuje stav konverzace k checkpointu (v produkci použijte odolný checkpointer; `MemorySaver` je vhodný pro lokální testování).
- **Lidský zásah**: Pokud váš graf používá LangGraph `interrupt()`, `ResponsesHostServer` zobrazuje čekající přerušení jako předmět `function_call` / `mcp_approval_request` a klienti pokračují s odpovídajícím `function_call_output` / `mcp_approval_response`.
- **Nasazení do Foundry**: Použijte Azure Developer CLI — `azd ext install azure.ai.agents`, `azd ai agent init -m <manifest>`, `azd ai agent run` (lokálně, vyžaduje Docker), pak `azd provision` a `azd deploy`. Pro nasazení hostovaných agentů máte potřebu role **Foundry Project Manager**.

Spustitelná verze tohoto příkladu je k dispozici v [code-samples/14-langchain-hosted-agent.py](../../../14-microsoft-agent-framework/code-samples/14-langchain-hosted-agent.py). Pro úplný postup (protokol Invocations, vlastní schémata požadavků a řešení problémů) viz [Host LangGraph agents as Foundry hosted agents](https://learn.microsoft.com/azure/foundry/how-to/develop/langchain-hosted-agents).

## Ukázky kódu 

Ukázky kódu pro Microsoft Agent Framework lze najít v tomto repozitáři v souborech `xx-python-agent-framework` a `xx-dotnet-agent-framework`.

## Máte další otázky ohledně Microsoft Agent Framework?

Připojte se k [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D), kde se můžete setkat s ostatními studenty, navštívit kancelářské hodiny a získat odpovědi na své dotazy ohledně AI Agentů.
## Předchozí lekce

[Paměť pro AI Agenty](../13-agent-memory/README.md)

## Následující lekce

[Vytváření agentů pro použití počítače (CUA)](../15-browser-use/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Prohlášení o omezení odpovědnosti**:
Tento dokument byl přeložen pomocí AI překladatelské služby [Co-op Translator](https://github.com/Azure/co-op-translator). Přestože usilujeme o co největší přesnost, mějte prosím na paměti, že automatizované překlady mohou obsahovat chyby nebo nepřesnosti. Originální dokument v jeho mateřském jazyce by měl být považován za autoritativní zdroj. Pro kritické informace se doporučuje profesionální lidský překlad. Nejsme odpovědní za jakékoli nedorozumění nebo nesprávné interpretace vzniklé použitím tohoto překladu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->