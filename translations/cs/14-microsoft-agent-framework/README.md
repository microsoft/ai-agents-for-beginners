# Prozkoumávání Microsoft Agent Framework

![Agent Framework](../../../translated_images/cs/lesson-14-thumbnail.90df0065b9d234ee.webp)

### Úvod

Tato lekce pokryje:

- Pochopení Microsoft Agent Framework: Klíčové vlastnosti a přínos  
- Prozkoumání klíčových konceptů Microsoft Agent Framework
- Pokročilé MAF vzory: Workflows, middleware a paměť

## Cíle učení

Po dokončení této lekce budete vědět, jak:

- Vytvářet produkčně připravené AI agenty pomocí Microsoft Agent Framework
- Aplikovat základní vlastnosti Microsoft Agent Framework na vaše agentní scénáře
- Používat pokročilé vzory včetně workflow, middleware a sledovatelnosti

## Ukázky kódu 

Ukázky kódu pro [Microsoft Agent Framework (MAF)](https://aka.ms/ai-agents-beginners/agent-framework) najdete v tomto repozitáři pod soubory `xx-python-agent-framework` a `xx-dotnet-agent-framework`.

## Pochopení Microsoft Agent Framework

![Framework Intro](../../../translated_images/cs/framework-intro.077af16617cf130c.webp)

[Microsoft Agent Framework (MAF)](https://aka.ms/ai-agents-beginners/agent-framework) je sjednocený rámec Microsoftu pro vytváření AI agentů. Nabízí flexibilitu pro řešení široké škály agentních scénářů viděných jak v produkčním, tak výzkumném prostředí, včetně:

- **Sekvenční orchestraci agentů** v situacích, kde jsou potřeba postupné workflow.
- **Současnou orchestraci** v situacích, kdy agenti potřebují dokončit úkoly současně.
- **Orchestrace skupinového chatu**, kde agenti mohou spolupracovat na jednom úkolu.
- **Orchestrace předání úkolu**, kdy agenti předávají úkoly jeden druhému jak se podúkoly dokončují.
- **Magnetickou orchestraci**, kdy manažerský agent vytváří a modifikuje seznam úkolů a koordinuje pod-agenty k dokončení úkolu.

Pro produkční nasazení AI agentů má MAF také tyto vlastnosti:

- **Sledovatelnost** pomocí OpenTelemetry, kdy každá akce AI agenta včetně vyvolání nástroje, kroků orchestrace, toku rozumu a výkonového monitoringu přes Microsoft Foundry dashboardy je zaznamenána.
- **Bezpečnost** díky nativnímu hostování agentů v Microsoft Foundry, které zahrnuje bezpečnostní kontroly jako řízení přístupu na základě rolí, zpracování soukromých dat a zabudovanou ochranu obsahu.
- **Odolnost** – Vlákna a workflow agentů mohou být pozastavena, obnovena a zotavena z chyb, což umožňuje dlouhodobé běhy procesů.
- **Řízení** – Podporována jsou workflow s člověkem v cyklu, kde jsou úkoly označeny jako vyžadující lidské schválení.

Microsoft Agent Framework je také zaměřen na interoperabilitu tím, že:

- **Je nezávislý na cloudu** – Agenti mohou běžet v kontejnerech, on-premises i napříč různými cloudy.
- **Je nezávislý na poskytovateli** – Agenti mohou být vytvářeni pomocí preferovaného SDK včetně Azure OpenAI a OpenAI.
- **Integruje otevřené standardy** – Agenti mohou využívat protokoly jako Agent-to-Agent (A2A) a Model Context Protocol (MCP) k objevování a využívání jiných agentů a nástrojů.
- **Pluginy a konektory** – Může být provedeno propojení na datové a paměťové služby jako Microsoft Fabric, SharePoint, Pinecone a Qdrant.

Podívejme se, jak jsou tyto vlastnosti aplikovány na některé základní koncepty Microsoft Agent Framework.

## Klíčové koncepty Microsoft Agent Framework

### Agenti

![Agent Framework](../../../translated_images/cs/agent-components.410a06daf87b4fef.webp)

**Vytváření agentů**

Vytvoření agenta se provádí definováním inference služby (poskytovatele LLM),  
sady instrukcí, které má AI agent následovat, a přiřazeným `name`:

```python
agent = AzureOpenAIChatClient(credential=AzureCliCredential()).create_agent( instructions="You are good at recommending trips to customers based on their preferences.", name="TripRecommender" )
```

Výše je používaný `Azure OpenAI`, ale agenti mohou být vytvořeni pomocí různých služeb včetně `Microsoft Foundry Agent Service`:

```python
AzureAIAgentClient(async_credential=credential).create_agent( name="HelperAgent", instructions="You are a helpful assistant." ) as agent
```

OpenAI `Responses`, API `ChatCompletion`

```python
agent = OpenAIResponsesClient().create_agent( name="WeatherBot", instructions="You are a helpful weather assistant.", )
```

```python
agent = OpenAIChatClient().create_agent( name="HelpfulAssistant", instructions="You are a helpful assistant.", )
```

nebo [MiniMax](https://platform.minimaxi.com/), který poskytuje API kompatibilní s OpenAI a velké kontextové okna (až 204K tokenů):

```python
agent = OpenAIChatClient(base_url="https://api.minimax.io/v1", api_key=os.environ["MINIMAX_API_KEY"], model_id="MiniMax-M3").create_agent( name="HelpfulAssistant", instructions="You are a helpful assistant.", )
```

nebo vzdálené agenty pomocí protokolu A2A:

```python
agent = A2AAgent( name=agent_card.name, description=agent_card.description, agent_card=agent_card, url="https://your-a2a-agent-host" )
```

**Spouštění agentů**

Agenti jsou spuštěni pomocí metod `.run` nebo `.run_stream` pro odpovědi bez streamingu nebo s streamingem.

```python
result = await agent.run("What are good places to visit in Amsterdam?")
print(result.text)
```

```python
async for update in agent.run_stream("What are the good places to visit in Amsterdam?"):
    if update.text:
        print(update.text, end="", flush=True)

```

Každé spuštění agenta může mít také možnosti pro přizpůsobení parametrů jako `max_tokens` použitých agentem, `tools`, které agent může volat, a dokonce samotný `model` používaný agentem.

To je užitečné v případech, kdy jsou pro splnění uživatelského úkolu vyžadovány specifické modely nebo nástroje.

**Nástroje**

Nástroje mohou být definovány jak při definici agenta:

```python
def get_attractions( location: Annotated[str, Field(description="The location to get the top tourist attractions for")], ) -> str: """Get the top tourist attractions for a given location.""" return f"The top attractions for {location} are." 


# Při přímém vytváření ChatAgenta

agent = ChatAgent( chat_client=OpenAIChatClient(), instructions="You are a helpful assistant", tools=[get_attractions]

```

a také při spouštění agenta:

```python

result1 = await agent.run( "What's the best place to visit in Seattle?", tools=[get_attractions] # Nástroj poskytnut pouze pro tento běh )
```

**Vlákna agentů**

Vlákna agentů se používají k řešení vícekolových konverzací. Vlákna mohou být vytvořena buď:

- Použitím `get_new_thread()`, což umožňuje vlákno uložit v čase
- Automatickým vytvořením vlákna při spuštění agenta, přičemž vlákno trvá pouze během aktuálního spuštění.

Pro vytvoření vlákna vypadá kód takto:

```python
# Vytvořit nový vlákno.
thread = agent.get_new_thread() # Spusťte agenta s vlákem.
response = await agent.run("Hello, I am here to help you book travel. Where would you like to go?", thread=thread)

```

Poté můžete vlákno serializovat pro pozdější použití:

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

**Agent Middleware**

Agenti interagují s nástroji a LLM pro dokončení úkolů uživatele. V určitých scénářích chceme provádět nebo sledovat akce mezi těmito interakcemi. Agent middleware nám to umožňuje prostřednictvím:

*Middleware funkcí*

Tento middleware nám umožňuje vykonat akci mezi agentem a funkcí/nástrojem, který agent volá. Příklad použití je, když chcete zaznamenávat volání funkce.

V kódu níže `next` definuje, zda se má zavolat další middleware nebo skutečná funkce.

```python
async def logging_function_middleware(
    context: FunctionInvocationContext,
    next: Callable[[FunctionInvocationContext], Awaitable[None]],
) -> None:
    """Function middleware that logs function execution."""
    # Předzpracování: Zaznamenejte před spuštěním funkce
    print(f"[Function] Calling {context.function.name}")

    # Pokračujte na další middleware nebo spuštění funkce
    await next(context)

    # Post-processing: Zaznamenejte po spuštění funkce
    print(f"[Function] {context.function.name} completed")
```

*Middleware chatu*

Tento middleware nám umožňuje vykonání nebo záznam akce mezi agentem a požadavky mezi LLM.

Obsahuje důležité informace jako `messages`, které jsou odesílány AI službě.

```python
async def logging_chat_middleware(
    context: ChatContext,
    next: Callable[[ChatContext], Awaitable[None]],
) -> None:
    """Chat middleware that logs AI interactions."""
    # Předzpracování: Záznam před voláním AI
    print(f"[Chat] Sending {len(context.messages)} messages to AI")

    # Pokračovat na další middleware nebo AI službu
    await next(context)

    # Pozpracování: Záznam po odpovědi AI
    print("[Chat] AI response received")

```

**Paměť agenta**

Jak bylo popsáno v lekci `Agentic Memory`, paměť je důležitý prvek umožňující agentovi pracovat přes různé kontexty. MAF nabízí několik typů paměti:

*Paměť v paměti (In-Memory Storage)*

Toto je paměť uložená ve vláknech během běhu aplikace.

```python
# Vytvořit nové vlákno.
thread = agent.get_new_thread() # Spustit agenta s vláknem.
response = await agent.run("Hello, I am here to help you book travel. Where would you like to go?", thread=thread)
```

*Trvalé zprávy (Persistent Messages)*

Tato paměť se používá pro uchování historie konverzace přes různé sessiony. Je definována pomocí `chat_message_store_factory`:

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

*Dynamická paměť (Dynamic Memory)*

Tato paměť se přidává do kontextu před spuštěním agentů. Tyto paměti mohou být uložené v externích službách jako mem0:

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

**Sledovatelnost agenta (Agent Observability)**

Sledovatelnost je důležitá pro vytváření spolehlivých a udržitelných agentních systémů. MAF integruje OpenTelemetry pro poskytování trasování a metrik pro lepší sledovatelnost.

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

### Workflow

MAF nabízí workflow, což jsou předem definované kroky ke splnění úkolu, zahrnující AI agenty jako komponenty těchto kroků.

Workflow jsou složena z různých komponent, které umožňují lepší řízení toku. Workflow také umožňují **víceagentní orchestraci** a **checkpointing** pro ukládání stavů workflow.

Základní komponenty workflow jsou:

**Prováděcí komponenty (Executors)**

Executory přijímají vstupní zprávy, vykonávají své přiřazené úkoly a poté generují výstupní zprávu. Posouvají workflow směrem k dokončení většího úkolu. Executory mohou být AI agent nebo vlastní logika.

**Hrany (Edges)**

Hrany definují tok zpráv v workflow. Mohou být:

*Přímé hrany* – Jednoduchá jednota-jedna spojení mezi executory:

```python
from agent_framework import WorkflowBuilder

builder = WorkflowBuilder()
builder.add_edge(source_executor, target_executor)
builder.set_start_executor(source_executor)
workflow = builder.build()
```

*Podmíněné hrany* – Aktivují se po splnění určité podmínky. Například když nejsou dostupné hotelové pokoje, executor může navrhnout jiné možnosti.

*Přepínačové (switch-case) hrany* – Směrují zprávy k různým executorům na základě definovaných podmínek. Například pokud má zákazník prioritní přístup, jeho úkoly budou řešeny přes jiné workflow.

*Fan-out hrany* – Posílají jednu zprávu na více cílů.

*Fan-in hrany* – Sbírají více zpráv z různých executorů a posílají na jeden cíl.

**Události (Events)**

Pro lepší sledovatelnost workflow nabízí MAF vestavěné události pro vykonávání, včetně:

- `WorkflowStartedEvent`  - Začátek vykonávání workflow
- `WorkflowOutputEvent` - Workflow vydá výstup
- `WorkflowErrorEvent` - Workflow narazí na chybu
- `ExecutorInvokeEvent`  - Executor zahájí zpracování
- `ExecutorCompleteEvent`  -  Executor dokončí zpracování
- `RequestInfoEvent` - Je vydán požadavek

## Pokročilé MAF vzory

Výše uvedené části pokrývají základní koncepty Microsoft Agent Framework. Při vytváření složitějších agentů uvážíte následující pokročilé vzory:

- **Skládání middleware**: Řetězit několik middleware handlerů (logování, autentizace, omezení rychlosti) pomocí middleware funkcí a chatu pro jemné řízení chování agenta.
- **Checkpointing workflow**: Používat workflow události a serializaci k ukládání a obnovení dlouhotrvajících agentních procesů.
- **Dynamický výběr nástrojů**: Kombinovat RAG nad popisy nástrojů s registrací nástrojů MAF k prezentaci pouze relevantních nástrojů podle dotazu.
- **Víceagentní předávání úkolu**: Používat hrany workflow a podmíněné směrování k orchestraci předávání mezi specializovanými agenty.

## Hostování LangChain / LangGraph agentů na Microsoft Foundry

Microsoft Agent Framework je **interoperabilní mezi rámci** — nejste omezeni na agenty napsané s MAF. Pokud už máte agenta vytvořeného s **LangChain** nebo **LangGraph**, můžete ho spustit jako **hostovaného agenta Microsoft Foundry**, kde Foundry spravuje runtime, sessiony, škálování, identitu a koncové body protokolů, zatímco vaše agentní logika zůstává v LangGraph.

To se dělá pomocí balíčku `langchain_azure_ai.agents.hosting`, který vystavuje zkompilovaný LangGraph graf přes stejné protokoly, které používají hostovaní agenti Foundry.

**1. Nainstalujte doplněk hosting:**

```bash
pip install -U "langchain-azure-ai[hosting]>=1.2.4" azure-identity
```

Doplněk `hosting` instaluje Foundry protokolové knihovny: `azure-ai-agentserver-responses` (OpenAI kompatibilní endpoint `/responses`) a `azure-ai-agentserver-invocations` (generický endpoint `/invocations`).

**2. Vyberte protokol hostování:**

| Protokol | Host třída | Endpoint | Použijte když |
|----------|-----------|----------|----------|
| **Responses** | `ResponsesHostServer` | `/responses` | Chcete OpenAI kompatibilní chat, streaming, historii odpovědí a vlákna konverzace — doporučený výchozí protokol pro konverzační agenty. |
| **Invocations** | `InvocationsHostServer` | `/invocations` | Potřebujete vlastní JSON strukturu, endpoint ve stylu webhook nebo ne-konverzační zpracování. |

Protože **Responses API je primární API pro vývoj agentů v Foundry**, začněte s `ResponsesHostServer` pro většinu agentů.

**3. Nastavte proměnné prostředí** (`az login` nejdříve, aby `DefaultAzureCredential` mohl autentizovat):

```bash
export FOUNDRY_PROJECT_ENDPOINT="https://<resource>.services.ai.azure.com/api/projects/<project>"
export FOUNDRY_MODEL_NAME="gpt-4.1"
```

Když agent později poběží jako hostovaný agent ve Foundry, platforma automaticky injektuje `FOUNDRY_PROJECT_ENDPOINT`.

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
    deployment = os.environ.get("FOUNDRY_MODEL_NAME", "gpt-4.1")
    credential = DefaultAzureCredential()
    project = AIProjectClient(endpoint=project_endpoint, credential=credential)
    openai_client = project.get_openai_client()
    token_provider = get_bearer_token_provider(credential, _AZURE_AI_SCOPE)

    # ChatOpenAI zde cílí na OpenAI-kompatibilní (Responses) endpoint projektu Foundry.
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

Spusťte ho lokálně s `python main.py`, poté odešlete požadavek Responses na `http://localhost:8088/responses`.

**Klíčová chování:**

- **Konverzace**: Klienti pokračují v konverzaci předáním `previous_response_id` nebo `conversation` ID. Pokud je váš graf kompilován s LangGraph checkpointerem, Foundry ukládá stav konverzace k checkpointu (v produkci používejte trvalý checkpointer; `MemorySaver` je vhodný pro lokální testování).
- **Člověk v cyklu**: Pokud váš graf používá LangGraph `interrupt()`, `ResponsesHostServer` zobrazí čekající přerušení jako položku `function_call` / `mcp_approval_request`, a klienti pokračují s odpovídajícím `function_call_output` / `mcp_approval_response`.
- **Nasazení do Foundry**: Použijte Azure Developer CLI — `azd ext install azure.ai.agents`, `azd ai agent init -m <manifest>`, `azd ai agent run` (lokálně, vyžaduje Docker), poté `azd provision` a `azd deploy`. Nasazení hostovaného agenta vyžaduje roli **Foundry Project Manager**.

Spustitelná verze tohoto příkladu je v [code-samples/14-langchain-hosted-agent.py](../../../14-microsoft-agent-framework/code-samples/14-langchain-hosted-agent.py). Kompletní průvodce (protoko lInvocations, vlastní požadavkové schémata a řešení problémů) naleznete v [Host LangGraph agents as Foundry hosted agents](https://learn.microsoft.com/azure/foundry/how-to/develop/langchain-hosted-agents).

## Ukázky kódu 

Ukázky kódu pro Microsoft Agent Framework najdete v tomto repozitáři pod soubory `xx-python-agent-framework` a `xx-dotnet-agent-framework`.

## Máte Více Otázek o Microsoft Agent Framework?

Připojte se k [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D) a setkejte se s dalšími studenty, zúčastněte se konzultačních hodin a získejte odpovědi na vaše otázky ohledně AI agentů.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Prohlášení o omezení odpovědnosti**:
Tento dokument byl přeložen pomocí AI překladatelské služby [Co-op Translator](https://github.com/Azure/co-op-translator). Přestože usilujeme o co největší přesnost, mějte prosím na paměti, že automatizované překlady mohou obsahovat chyby nebo nepřesnosti. Originální dokument v jeho mateřském jazyce by měl být považován za autoritativní zdroj. Pro kritické informace se doporučuje profesionální lidský překlad. Nejsme odpovědní za jakékoli nedorozumění nebo nesprávné interpretace vzniklé použitím tohoto překladu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->