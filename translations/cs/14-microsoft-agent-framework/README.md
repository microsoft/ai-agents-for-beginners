# Prozkoumání Microsoft Agent Framework

![Agent Framework](../../../translated_images/cs/lesson-14-thumbnail.90df0065b9d234ee.webp)

### Úvod

Tato lekce pokryje:

- Pochopení Microsoft Agent Framework: Klíčové funkce a hodnota  
- Prozkoumání klíčových konceptů Microsoft Agent Framework
- Pokročilé vzory MAF: Pracovní postupy, middleware a paměť

## Cíle učení

Po dokončení této lekce budete vědět, jak:

- Vytvořit produkčně připravené AI agenty pomocí Microsoft Agent Framework
- Aplikovat hlavní funkce Microsoft Agent Framework na vaše případové použití agentů
- Používat pokročilé vzory včetně pracovních postupů, middleware a pozorovatelnosti

## Ukázky kódu 

Ukázky kódu pro [Microsoft Agent Framework (MAF)](https://aka.ms/ai-agents-beginners/agent-framework) naleznete v tomto repozitáři v souborech `xx-python-agent-framework` a `xx-dotnet-agent-framework`.

## Pochopení Microsoft Agent Framework

![Framework Intro](../../../translated_images/cs/framework-intro.077af16617cf130c.webp)

[Microsoft Agent Framework (MAF)](https://aka.ms/ai-agents-beginners/agent-framework) je sjednocený framework Microsoftu pro tvorbu AI agentů. Nabízí flexibilitu k pokrytí široké škály případů použití agentů, jak v produkčních, tak výzkumných prostředích, včetně:

- **Sekvenční orchestraci agentů** v situacích, kde jsou potřeba krokové pracovní postupy.
- **Současnou orchestraci** v situacích, kdy agenti musí úkoly dokončit současně.
- **Orchestraci skupinového chatu** v situacích, kdy agenti mohou spolupracovat na jednom úkolu.
- **Předávání úkolu** v situacích, kdy si agenti předávají úkol, jak jsou dílčí úkoly dokončovány.
- **Magnetickou orchestraci** v situacích, kdy manažerský agent vytváří a upravuje seznam úkolů a řídí koordinaci subagentů k dokončení úkolu.

Pro nasazení AI agentů v produkci MAF také obsahuje funkce pro:

- **Pozorovatelnost** pomocí OpenTelemetry, kde je sledována každá akce AI agenta včetně volání nástrojů, kroků orchestrací, logických toků a monitorování výkonu přes dashboardy Microsoft Foundry.
- **Bezpečnost** hostováním agentů nativně na Microsoft Foundry, což zahrnuje bezpečnostní řízení jako přístup založený na rolích, zpracování soukromých dat a integrovanou ochranu obsahu.
- **Trvanlivost** díky možnosti pozastavení, obnovení a zotavení agentních vláken a pracovních postupů, což umožňuje dlouhodobější procesy.
- **Kontrolu** podporou pracovních postupů s lidským zásahem, kde jsou úkoly označeny jako vyžadující lidské schválení.

Microsoft Agent Framework se také zaměřuje na interoperabilitu prostřednictvím:

- **Nezávislosti na cloudu** - Agent může běžet v kontejnerech, on-premise a napříč různými cloudy.
- **Nezávislosti na poskytovateli** - Agenti mohou být vytvářeni pomocí preferovaného SDK včetně Azure OpenAI a OpenAI
- **Integrace otevřených standardů** - Agenti mohou využívat protokoly jako Agent-to-Agent(A2A) a Model Context Protocol (MCP) k vyhledávání a používání jiných agentů a nástrojů.
- **Pluginy a konektory** - Mohou být navázány spojení na datové a paměťové služby jako Microsoft Fabric, SharePoint, Pinecone a Qdrant.

Podívejme se, jak se tyto funkce aplikují na některé klíčové koncepty Microsoft Agent Framework.

## Klíčové koncepty Microsoft Agent Framework

### Agenti

![Agent Framework](../../../translated_images/cs/agent-components.410a06daf87b4fef.webp)

**Vytváření agentů**

Vytváření agenta se provádí definováním inferenční služby (poskytovatele LLM),  
sady pokynů, které má AI agent následovat, a přiřazeným `name`:

```python
agent = AzureOpenAIChatClient(credential=AzureCliCredential()).create_agent( instructions="You are good at recommending trips to customers based on their preferences.", name="TripRecommender" )
```

Výše uvedené používá `Azure OpenAI`, ale agenti mohou být vytvářeni pomocí různých služeb, včetně `Microsoft Foundry Agent Service`:

```python
AzureAIAgentClient(async_credential=credential).create_agent( name="HelperAgent", instructions="You are a helpful assistant." ) as agent
```

OpenAI `Responses`, `ChatCompletion` API

```python
agent = OpenAIResponsesClient().create_agent( name="WeatherBot", instructions="You are a helpful weather assistant.", )
```

```python
agent = OpenAIChatClient().create_agent( name="HelpfulAssistant", instructions="You are a helpful assistant.", )
```

nebo [MiniMax](https://platform.minimaxi.com/), poskytující API kompatibilní s OpenAI s velkými kontextovými okny (až 204K tokenů):

```python
agent = OpenAIChatClient(base_url="https://api.minimax.io/v1", api_key=os.environ["MINIMAX_API_KEY"], model_id="MiniMax-M3").create_agent( name="HelpfulAssistant", instructions="You are a helpful assistant.", )
```

nebo vzdálené agenty používající protokol A2A:

```python
agent = A2AAgent( name=agent_card.name, description=agent_card.description, agent_card=agent_card, url="https://your-a2a-agent-host" )
```

**Spuštění agentů**

Agenti se spouštějí pomocí metod `.run` nebo `.run_stream` pro ne-streamované nebo streamované odpovědi.

```python
result = await agent.run("What are good places to visit in Amsterdam?")
print(result.text)
```

```python
async for update in agent.run_stream("What are the good places to visit in Amsterdam?"):
    if update.text:
        print(update.text, end="", flush=True)

```

Každé spuštění agenta může také obsahovat možnosti přizpůsobení parametrů, jako například `max_tokens` používaný agentem, `tools`, které agent může volat, a dokonce i samotný `model` použitý agentem.

To je užitečné v situacích, kdy jsou pro splnění uživatelova úkolu potřebné specifické modely nebo nástroje.

**Nástroje**

Nástroje lze definovat jak při definování agenta:

```python
def get_attractions( location: Annotated[str, Field(description="The location to get the top tourist attractions for")], ) -> str: """Get the top tourist attractions for a given location.""" return f"The top attractions for {location} are." 


# Při přímém vytváření ChatAgenta

agent = ChatAgent( chat_client=OpenAIChatClient(), instructions="You are a helpful assistant", tools=[get_attractions]

```

tak i při spouštění agenta:

```python

result1 = await agent.run( "What's the best place to visit in Seattle?", tools=[get_attractions] # Nástroj poskytovaný pouze pro tento běh )
```

**Vlákna agentů**

Vlákna agentů slouží k řízení konverzací s vícenásobnými koly. Vlákna mohou být vytvořena buď:

- Pomocí `get_new_thread()`, což umožňuje vlákno ukládat v průběhu času
- Automatickým vytvořením vlákna při spuštění agenta, které trvá pouze během aktuálního běhu.

K vytvoření vlákna vypadá kód takto:

```python
# Vytvořit nový vlákno.
thread = agent.get_new_thread() # Spustit agenta pomocí vlákna.
response = await agent.run("Hello, I am here to help you book travel. Where would you like to go?", thread=thread)

```

Vlákno můžete poté serializovat pro pozdější uložení:

```python
# Vytvořte nový vlákno.
thread = agent.get_new_thread() 

# Spusťte agenta s vláknem.

response = await agent.run("Hello, how are you?", thread=thread) 

# Serializujte vlákno pro uložení.

serialized_thread = await thread.serialize() 

# Deserializujte stav vlákna po načtení z úložiště.

resumed_thread = await agent.deserialize_thread(serialized_thread)
```

**Middleware agenta**

Agenti komunikují s nástroji a LLM, aby splnili úkoly uživatele. V určitých scénářích chceme vykonat nebo sledovat akce mezi těmito interakcemi. Middleware agenta nám to umožňuje prostřednictvím:

*Middleware funkcí*

Tento middleware nám dovoluje vykonat akci mezi agentem a funkcí/nástrojem, který volá. Příklad použití je, když chcete zaznamenávat volání funkce.

V kódu níže `next` určuje, zda má být volán další middleware nebo samotná funkce.

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

    # Povězpracování: Záznam po vykonání funkce
    print(f"[Function] {context.function.name} completed")
```

*Middleware chatu*

Tento middleware nám umožňuje vykonat nebo zaznamenat akci mezi agentem a požadavky mezi LLM.

Obsahuje důležité informace, jako jsou `messages` odesílané AI službě.

```python
async def logging_chat_middleware(
    context: ChatContext,
    next: Callable[[ChatContext], Awaitable[None]],
) -> None:
    """Chat middleware that logs AI interactions."""
    # Předzpracování: Zaznamenat před voláním AI
    print(f"[Chat] Sending {len(context.messages)} messages to AI")

    # Pokračovat na další middleware nebo AI službu
    await next(context)

    # Pozpracování: Zaznamenat po odpovědi AI
    print("[Chat] AI response received")

```

**Paměť agenta**

Jak bylo pokryto v lekci `Agentic Memory`, paměť je důležitým prvkem pro umožnění agentovi operovat přes různé kontexty. MAF nabízí několik různých typů pamětí:

*Paměť v rámci aplikace*

Jedná se o paměť uloženou ve vláknech během běhu aplikace.

```python
# Vytvořit nový vlákno.
thread = agent.get_new_thread() # Spustit agenta s vláknem.
response = await agent.run("Hello, I am here to help you book travel. Where would you like to go?", thread=thread)
```

*Perzistentní zprávy*

Tato paměť se používá pro uchovávání historie konverzace přes různé relace. Definuje se pomocí `chat_message_store_factory`:

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

*Dynamická paměť*

Tato paměť se přidává do kontextu před spuštěním agentů. Tyto paměti mohou být ukládány v externích službách jako mem0:

```python
from agent_framework.mem0 import Mem0Provider

# Použití Mem0 pro pokročilé paměťové funkce
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

**Pozorovatelnost agenta**

Pozorovatelnost je důležitá pro tvorbu spolehlivých a udržitelných agentních systémů. MAF integruje OpenTelemetry pro poskytování sledování a metrík pro lepší pozorovatelnost.

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

MAF nabízí pracovní postupy, což jsou předdefinované kroky k dokončení úkolu, které zahrnují AI agenty jako součást těchto kroků.

Pracovní postupy jsou složeny z různých komponent, které umožňují lepší řízení toku řízení. Pracovní postupy také umožňují **multi-agent orchestraci** a **checkpointing** pro ukládání stavů pracovních postupů.

Hlavní komponenty pracovního postupu jsou:

**Spouštěče (Executors)**

Spouštěče přijímají vstupní zprávy, vykonávají své přiřazené úkoly a poté generují výstupní zprávu. To posouvá pracovní postup vpřed k dokončení většího úkolu. Spouštěče mohou být AI agenti nebo vlastní logika.

**Hrany (Edges)**

Hrany slouží k definování toku zpráv v pracovním postupu. Mohou být:

*Přímé hrany* - Jednoduchá spojení jeden-na-jeden mezi spouštěči:

```python
from agent_framework import WorkflowBuilder

builder = WorkflowBuilder()
builder.add_edge(source_executor, target_executor)
builder.set_start_executor(source_executor)
workflow = builder.build()
```

*Podmíněné hrany* - Aktivovány po splnění určité podmínky. Například pokud nejsou k dispozici hotelové pokoje, spouštěč může navrhnout jiné možnosti.

*Switch-case hrany* - Směrují zprávy k různým spouštěčům na základě definovaných podmínek. Například pokud má cestující prioritní přístup, jeho úkoly budou zpracovány jiným pracovním postupem.

*Rozvětvovací hrany* - Odesílají jednu zprávu na více cílů.

*Sběrné hrany* - Sbírají více zpráv od různých spouštěčů a odesílají je jednomu cíli.

**Události (Events)**

Pro lepší pozorovatelnost pracovních postupů MAF nabízí vestavěné události pro vykonávání, včetně:

- `WorkflowStartedEvent`  - Spuštění pracovního postupu
- `WorkflowOutputEvent` - Pracovní postup generuje výstup
- `WorkflowErrorEvent` - Pracovní postup narazí na chybu
- `ExecutorInvokeEvent`  - Spouštěč začíná zpracovávat
- `ExecutorCompleteEvent`  - Spouštěč dokončil zpracování
- `RequestInfoEvent` - Požadavek byl odeslán

## Pokročilé vzory MAF

Výše uvedené části pokrývají klíčové koncepty Microsoft Agent Framework. Jak stavíte složitější agenty, zde jsou některé pokročilé vzory k zvážení:

- **Skládání middleware**: Řetězení více middleware handlerů (logování, autorizace, omezení rychlosti) pomocí funkčního a chat middleware pro jemné řízení chování agenta.
- **Checkpointing pracovních postupů**: Použití událostí pracovních postupů a serializace k ukládání a obnovení dlouhotrvajících procesů agentů.
- **Dynamický výběr nástrojů**: Kombinace RAG přes popisy nástrojů s registrací nástrojů MAF k zobrazení pouze relevantních nástrojů pro dotaz.
- **Předávání mezi více agenty**: Použití hran pracovních postupů a podmíněného směrování k orchestraci předávání mezi specializovanými agenty.

## Hostování LangChain / LangGraph agentů na Microsoft Foundry

Microsoft Agent Framework je **frameworkově interoperabilní** — nejste omezeni na agenty napsané pouze v MAF. Pokud už máte agenta vytvořeného pomocí **LangChain** nebo **LangGraph**, můžete jej spustit jako **hostovaného agenta Microsoft Foundry**, takže Foundry spravuje runtime, relace, škálování, identitu a protokolové koncové body za vás, zatímco vaše logika agenta zůstává v LangGraph.

To se provádí pomocí balíčku `langchain_azure_ai.agents.hosting`, který zpřístupňuje zkompilovaný LangGraph graf přes stejné protokoly, které používají hostovaní agenti Foundry.

**1. Nainstalujte hosting extra:**

```bash
pip install -U "langchain-azure-ai[hosting]>=1.2.4" azure-identity
```

Balíček `hosting` nainstaluje protokolové knihovny Foundry: `azure-ai-agentserver-responses` (OpenAI-kompatibilní endpoint `/responses`) a `azure-ai-agentserver-invocations` (obecný endpoint `/invocations`).

**2. Vyberte hostingový protokol:**

| Protokol | Hostitelská třída | Endpoint | Použití |
|----------|-----------|----------|----------|
| **Responses** | `ResponsesHostServer` | `/responses` | Chcete OpenAI-kompatibilní chat, streamování, historii odpovědí a vláken konverzace — doporučený výchozí režim pro konverzační agenty. |
| **Invocations** | `InvocationsHostServer` | `/invocations` | Potřebujete vlastní strukturu JSON, webhookový endpoint nebo ne-konverzační zpracování. |

Protože **Responses API je primární API pro vývoj agentů ve Foundry**, začněte s `ResponsesHostServer` pro většinu agentů.

**3. Konfigurujte proměnné prostředí** (`az login` nejdříve, aby `DefaultAzureCredential` mohl autentizovat):

```bash
export FOUNDRY_PROJECT_ENDPOINT="https://<resource>.services.ai.azure.com/api/projects/<project>"
export FOUNDRY_MODEL_NAME="gpt-5-mini"
```

Když agent později poběží jako hostovaný agent ve Foundry, platforma automaticky nastavení `FOUNDRY_PROJECT_ENDPOINT`.

**4. Zpřístupněte LangGraph agenta přes protokol Responses:**

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

    # ChatOpenAI zde cílí na endpoint kompatibilní s OpenAI (Responses) v projektu Foundry.
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

Spusťte lokálně pomocí `python main.py`, poté pošlete požadavek na `http://localhost:8088/responses`.

**Klíčové chování:**

- **Konverzace**: Klienti pokračují v konverzaci předáním `previous_response_id` nebo `conversation` ID. Pokud je graf zkompilován s LangGraph checkpointem, Foundry propojuje stav konverzace s checkpointem (v produkci používejte trvalý checkpoint; `MemorySaver` je vhodný pro lokální testování).
- **Lidský zásah**: Pokud váš graf používá LangGraph `interrupt()`, `ResponsesHostServer` zvýrazní čekající přerušení jako položku Responses `function_call` / `mcp_approval_request` a klienti pokračují s odpovídajícím `function_call_output` / `mcp_approval_response`.
- **Nasazení do Foundry**: Použijte Azure Developer CLI — `azd ext install azure.ai.agents`, `azd ai agent init -m <manifest>`, `azd ai agent run` (lokálně, vyžaduje Docker), poté `azd provision` a `azd deploy`. Nasazení hostovaného agenta vyžaduje roli **Foundry Project Manager**.

Spustitelná verze tohoto příkladu je v [code-samples/14-langchain-hosted-agent.py](../../../14-microsoft-agent-framework/code-samples/14-langchain-hosted-agent.py). Pro kompletní průchod (protokol Invocations, vlastní schémata požadavků a řešení problémů) viz [Host LangGraph agents as Foundry hosted agents](https://learn.microsoft.com/azure/foundry/how-to/develop/langchain-hosted-agents).

## Ukázky kódu 

Ukázky kódu pro Microsoft Agent Framework naleznete v tomto repozitáři v souborech `xx-python-agent-framework` a `xx-dotnet-agent-framework`.

## Máte další otázky ohledně Microsoft Agent Framework?

Připojte se k [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D) a setkejte se s ostatními studenty, zúčastněte se konzultačních hodin a získejte odpovědi na své otázky ohledně AI agentů.
## Předchozí lekce

[Paměť pro AI agenty](../13-agent-memory/README.md)

## Další lekce

[Vytváření agentů pro používání počítače (CUA)](../15-browser-use/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Prohlášení o omezení odpovědnosti**:
Tento dokument byl přeložen pomocí AI překladatelské služby [Co-op Translator](https://github.com/Azure/co-op-translator). Přestože usilujeme o co největší přesnost, mějte prosím na paměti, že automatizované překlady mohou obsahovat chyby nebo nepřesnosti. Originální dokument v jeho mateřském jazyce by měl být považován za autoritativní zdroj. Pro kritické informace se doporučuje profesionální lidský překlad. Nejsme odpovědní za jakékoli nedorozumění nebo nesprávné interpretace vzniklé použitím tohoto překladu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->