# A Microsoft Agent Framework feltérképezése

![Agent Framework](../../../translated_images/hu/lesson-14-thumbnail.90df0065b9d234ee.webp)

### Bevezetés

Ez a lecke a következőket fogja lefedni:

- A Microsoft Agent Framework megértése: Főbb jellemzők és érték  
- A Microsoft Agent Framework kulcsfogalmainak feltárása
- Fejlett MAF minták: munkafolyamatok, middleware és memória

## Tanulási célok

A lecke elvégzése után tudni fogja, hogyan kell:

- Gyártásra kész MI ügynököket építeni a Microsoft Agent Framework használatával
- Alkalmazni a Microsoft Agent Framework alapvető funkcióit az ügynöki használati esetekhez
- Fejlett minták használata, beleértve a munkafolyamatokat, middleware-t és megfigyelhetőséget

## Kódminták 

A [Microsoft Agent Framework (MAF)](https://learn.microsoft.com/en-us/agent-framework/overview/?wt.mc_id=youtube_26688_organicsocial_reactor&pivots=programming-language-python) kódmintái megtalálhatók ebben a tárolóban az `xx-python-agent-framework` és `xx-dotnet-agent-framework` fájlok alatt.

## A Microsoft Agent Framework megértése

![Framework Intro](../../../translated_images/hu/framework-intro.077af16617cf130c.webp)

A [Microsoft Agent Framework (MAF)](https://learn.microsoft.com/en-us/agent-framework/overview/?wt.mc_id=youtube_26688_organicsocial_reactor&pivots=programming-language-python) a Microsoft egységes keretrendszere MI ügynökök építéséhez. Rugalmasságot kínál, hogy kezelje az ügynöki használati esetek széles körét, amelyek mind gyártási, mind kutatási környezetekben előfordulnak, beleértve:

- **Szekvenciális ügynök-orkesztrációt** olyan esetekben, ahol lépésről lépésre haladó munkafolyamatokra van szükség.
- **Párhuzamos orchesztrációt** olyan esetekben, ahol az ügynököknek egyszerre kell feladatokat elvégezniük.
- **Csoportos csevegés orkestrációt** olyan esetekben, ahol az ügynökök együttműködnek egy feladaton.
- **Átadás-orchesztrációt** olyan esetekben, ahol az ügynökök átadják egymásnak a feladatot, amint az alfeladatok kész vannak.
- **Mágneses orkestrációt** olyan esetekben, ahol egy menedzser ügynök hoz létre és módosít egy feladatlistát, és koordinálja az alügynököket a feladat elvégzéséhez.

Az MI ügynökök gyártásba juttatásához a MAF további funkciókat is tartalmaz:

- **Megfigyelhetőség** az OpenTelemetry használatával, ahol az MI Ügynök minden tevékenységét – beleértve az eszközhívásokat, orkésztrációs lépéseket, következtetési folyamatokat és teljesítményfigyelést a Microsoft Foundry műszerfalain keresztül – megfigyelhetjük.
- **Biztonság** az ügynökök natív hosztolásával a Microsoft Foundry-ban, amely tartalmazza a szerepalapú hozzáférés-vezérlést, a privát adatkezelést és a beépített tartalombiztonságot.
- **Tartósság** mivel az ügynök szálak és munkafolyamatok szüneteltethetők, folytathatók és hibákból helyreállíthatók, ami hosszabb futású folyamatokat tesz lehetővé.
- **Irányítás** emberi beavatkozás támogatása a munkafolyamatokban, ahol a feladatokat emberi jóváhagyáshoz kell megjelölni.

A Microsoft Agent Framework interoperábilitásra is fókuszál azáltal, hogy:

- **Fellegfüggetlen** - az ügynökök futtathatók konténerekben, helyben vagy több különböző felhőben.
- **Szolgáltatófüggetlen** - ügynökök létrehozhatók az általad preferált SDK-val, beleértve az Azure OpenAI-t és az OpenAI-t
- **Nyílt szabványok integrálása** - az ügynökök olyan protokollokat használhatnak, mint az Agent-to-Agent (A2A) és a Model Context Protocol (MCP), hogy felfedezzék és használják más ügynököket és eszközöket.
- **Bővítmények és kapcsolók** - kapcsolódhatnak adat- és memóriaszolgáltatásokhoz, például a Microsoft Fabric, SharePoint, Pinecone és Qdrant szolgáltatásokhoz.

Nézzük meg, hogy ezek a funkciók hogyan alkalmazhatók a Microsoft Agent Framework kulcsfogalmainál.

## A Microsoft Agent Framework kulcsfogalmai

### Ügynökök

![Agent Framework](../../../translated_images/hu/agent-components.410a06daf87b4fef.webp)

**Ügynökök létrehozása**

Az ügynök létrehozása úgy történik, hogy meghatározzuk az inferencia szolgáltatást (LLM szolgáltató), egy sor utasítást, amit az MI Ügynöknek követnie kell, valamint egy kijelölt `név`-et:


```python
agent = AzureOpenAIChatClient(credential=AzureCliCredential()).create_agent( instructions="You are good at recommending trips to customers based on their preferences.", name="TripRecommender" )
```

A fenti példa az `Azure OpenAI`-t használja, de ügynökök különféle szolgáltatásokkal is létrehozhatók, beleértve a `Microsoft Foundry Agent Service`-t:

```python
AzureAIAgentClient(async_credential=credential).create_agent( name="HelperAgent", instructions="You are a helpful assistant." ) as agent
```

OpenAI `Responses`, `ChatCompletion` API-k

```python
agent = OpenAIResponsesClient().create_agent( name="WeatherBot", instructions="You are a helpful weather assistant.", )
```

```python
agent = OpenAIChatClient().create_agent( name="HelpfulAssistant", instructions="You are a helpful assistant.", )
```

vagy a [MiniMax](https://platform.minimaxi.com/) használatával, amely OpenAI-kompatibilis API-t kínál nagy kontextusablakokkal (akár 204K tokenig):

```python
agent = OpenAIChatClient(base_url="https://api.minimax.io/v1", api_key=os.environ["MINIMAX_API_KEY"], model_id="MiniMax-M3").create_agent( name="HelpfulAssistant", instructions="You are a helpful assistant.", )
```

vagy távoli ügynökök az A2A protokoll segítségével:

```python
agent = A2AAgent( name=agent_card.name, description=agent_card.description, agent_card=agent_card, url="https://your-a2a-agent-host" )
```

**Ügynökök futtatása**

Az ügynökök a `.run` vagy `.run_stream` metódusokkal futtathatók, nem-streaming vagy streaming válaszokhoz.

```python
result = await agent.run("What are good places to visit in Amsterdam?")
print(result.text)
```

```python
async for update in agent.run_stream("What are the good places to visit in Amsterdam?"):
    if update.text:
        print(update.text, end="", flush=True)

```

Minden ügynök futtatásnak lehetnek olyan opciói is, amelyek testreszabják az olyan paramétereket, mint az ügynök által használt `max_tokens`, az általa hívható `eszközök`, vagy akár maga az ügynök által használt `modell`.

Ez hasznos olyan esetekben, amikor specifikus modellekre vagy eszközökre van szükség a felhasználó feladatának teljesítéséhez.

**Eszközök**

Az eszközök definiálhatók mind az ügynök definiálásakor:

```python
def get_attractions( location: Annotated[str, Field(description="The location to get the top tourist attractions for")], ) -> str: """Get the top tourist attractions for a given location.""" return f"The top attractions for {location} are." 


# Amikor közvetlenül ChatAgent-et hozunk létre

agent = ChatAgent( chat_client=OpenAIChatClient(), instructions="You are a helpful assistant", tools=[get_attractions]

```

valamint az ügynök futtatásakor is:

```python

result1 = await agent.run( "What's the best place to visit in Seattle?", tools=[get_attractions] # Ez az eszköz csak erre a futtatásra van biztosítva )
```

**Ügynök szálak**

Az ügynök szálak többfordulós beszélgetések kezelésére szolgálnak. Szálak létrehozhatók:

- a `get_new_thread()` használatával, amely lehetővé teszi a szál időbeli mentését
- vagy egy szál automatikus létrehozásával az ügynök futtatásakor, amely csak az aktuális futás idejére létezik.

Egy szál létrehozása így néz ki:

```python
# Hozzon létre egy új szálat.
thread = agent.get_new_thread() # Futtassa az ügynököt a szállal.
response = await agent.run("Hello, I am here to help you book travel. Where would you like to go?", thread=thread)

```

A szál későbbi használatra történő mentéséhez sorosítható:

```python
# Hozzon létre egy új szálat.
thread = agent.get_new_thread() 

# Futtassa az ügynököt a szállal.

response = await agent.run("Hello, how are you?", thread=thread) 

# Sorosítsa a szálat tároláshoz.

serialized_thread = await thread.serialize() 

# A szál állapotának deszerializálása a tárolásból való betöltés után.

resumed_thread = await agent.deserialize_thread(serialized_thread)
```

**Ügynök köztes réteg (Middleware)**

Az ügynökök eszközökkel és LLM-ekkel lépnek kapcsolatba a felhasználói feladatok elvégzéséhez. Bizonyos esetekben a két interakció között végre szeretnénk hajtani vagy nyomon követni tevékenységeket. Az ügynök köztes réteg ezt teszi lehetővé:

*Funkció Middleware*

Ez a middleware lehetővé teszi, hogy műveletet hajtsunk végre az ügynök és egy hívott funkció/eszköz között. Például, ha szeretnénk naplózni a funkcióhívást.

Az alábbi kódban a `next` határozza meg, hogy a következő middleware vagy maga a tényleges funkció legyen-e meghívva.

```python
async def logging_function_middleware(
    context: FunctionInvocationContext,
    next: Callable[[FunctionInvocationContext], Awaitable[None]],
) -> None:
    """Function middleware that logs function execution."""
    # Előfeldolgozás: Naplózás a függvény végrehajtása előtt
    print(f"[Function] Calling {context.function.name}")

    # Folytatás a következő middleware-rel vagy a függvény végrehajtásával
    await next(context)

    # Utófeldolgozás: Naplózás a függvény végrehajtása után
    print(f"[Function] {context.function.name} completed")
```

*Chat Middleware*

Ez a middleware lehetővé teszi, hogy végrehajtsunk vagy naplózzunk egy műveletet az ügynök és az LLM közötti kérés-válasz között.

Ez tartalmaz fontos információkat, például az AI szolgáltatásnak küldött `üzeneteket`.

```python
async def logging_chat_middleware(
    context: ChatContext,
    next: Callable[[ChatContext], Awaitable[None]],
) -> None:
    """Chat middleware that logs AI interactions."""
    # Előfeldolgozás: Naplózás az AI hívás előtt
    print(f"[Chat] Sending {len(context.messages)} messages to AI")

    # Folytatás a következő middleware vagy AI szolgáltatás felé
    await next(context)

    # Utófeldolgozás: Naplózás az AI válasz után
    print("[Chat] AI response received")

```

**Ügynök memória**

Ahogyan a `Agentic Memory` leckében tárgyaltuk, a memória fontos elem az ügynök működésének kontextusai feletti kezelése szempontjából. A MAF többféle memóriatípust kínál:

*Memória tárolás futás közben*

Ez a szálakon belüli memória, amely az alkalmazás futási ideje alatt tárolódik.

```python
# Hozz létre egy új szálat.
thread = agent.get_new_thread() # Futtasd az ügynököt a szállal.
response = await agent.run("Hello, I am here to help you book travel. Where would you like to go?", thread=thread)
```

*Állandó üzenetek*

Ez a memória a különböző munkamenetek közötti beszélgetési történelem tárolására szolgál. A `chat_message_store_factory` segítségével definiálható:

```python
from agent_framework import ChatMessageStore

# Egyéni üzenettár létrehozása
def create_message_store():
    return ChatMessageStore()

agent = ChatAgent(
    chat_client=OpenAIChatClient(),
    instructions="You are a Travel assistant.",
    chat_message_store_factory=create_message_store
)

```

*Dinamikus memória*

Ezt a memóriát a kontextushoz adjuk hozzá, mielőtt az ügynökök futnak. Ezek a memóriák külső szolgáltatásokban is tárolhatók, például mem0-ban:

```python
from agent_framework.mem0 import Mem0Provider

# Mem0 használata fejlett memória képességekhez
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

**Ügynök megfigyelhetősége**

A megfigyelhetőség fontos a megbízható és karbantartható ügynökrendszerek építéséhez. A MAF integrálódik az OpenTelemetry-vel, hogy jobb megfigyelhetőséget biztosítson nyomkövetéssel és mérőszámokkal.

```python
from agent_framework.observability import get_tracer, get_meter

tracer = get_tracer()
meter = get_meter()
with tracer.start_as_current_span("my_custom_span"):
    # csinálj valamit
    pass
counter = meter.create_counter("my_custom_counter")
counter.add(1, {"key": "value"})
```

### Munkafolyamatok

A MAF munkafolyamatokat kínál, amelyek előre definiált lépések egy feladat teljesítéséhez, és az MI ügynököket is bevonják komponensként ezekbe a lépésekbe.

A munkafolyamatok különböző összetevőkből állnak, amelyek jobb vezérlésfolyamot tesznek lehetővé. A munkafolyamatok támogatják a **több ügynökös orkestrációt** és az állapotmentést, azaz **checkpointolást** a munkafolyamat állapotainak mentésére.

Egy munkafolyamat főbb összetevői:

**Végrehajtók**

A végrehajtók input üzeneteket kapnak, elvégzik a feladataikat, majd output üzenetet generálnak. Ez előreviszi a munkafolyamatot a nagyobb feladat befejezése felé. A végrehajtók lehetnek MI ügynökök vagy egyéni logikák is.

**Élek**

Az élek határozzák meg az üzenetek áramlását egy munkafolyamatban. Ezek lehetnek:

*Direkt élek* - Egyszerű egy az egyhez kapcsolatok a végrehajtók között:

```python
from agent_framework import WorkflowBuilder

builder = WorkflowBuilder()
builder.add_edge(source_executor, target_executor)
builder.set_start_executor(source_executor)
workflow = builder.build()
```

*Feltételes élek* - Akkor aktiválódnak, ha bizonyos feltétel teljesül. Például, ha szállodai szobák nem elérhetők, egy végrehajtó alternatívákat javasolhat.

*Kapcsoló-eset élek* - Üzenetek irányítása különböző végrehajtókhoz meghatározott feltételek alapján. Például, ha egy utazó ügyfél prioritási hozzáféréssel rendelkezik, a feladatai egy másik munkafolyamaton keresztül kerülnek kezelésre.

*Sokirányú élek* - Egy üzenet több címzetthez küldése.

*Bejövő élek* - Több üzenet gyűjtése különböző végrehajtóktól és egy címzetthez továbbítása.

**Események**

A jobb megfigyelhetőség érdekében a MAF beépített eseményeket biztosít a végrehajtáshoz, többek között:

- `WorkflowStartedEvent`  - A munkafolyamat végrehajtásának kezdete
- `WorkflowOutputEvent` - A munkafolyamat kimenetet termel
- `WorkflowErrorEvent` - A munkafolyamat hibába ütközik
- `ExecutorInvokeEvent`  - A végrehajtó elkezdi a feldolgozást
- `ExecutorCompleteEvent`  -  A végrehajtó befejezi a feldolgozást
- `RequestInfoEvent` - Egy kérés elindul

## Fejlett MAF minták

A fentiek a Microsoft Agent Framework kulcsfogalmait fedik le. Ahogy bonyolultabb ügynököket épít, íme néhány fejlett minta, amit érdemes fontolóra venni:

- **Middleware összefűzés**: Több middleware kezelő láncolása (naplózás, hitelesítés, sebességkorlátozás) funkció- és chat-middleware használatával az ügynök viselkedésének finomhangolt kontrolljához.
- **Munkafolyamat állapotmentés**: Használja a munkafolyamat eseményeit és sorosítást a hosszabb futású ügynök folyamatok mentésére és folytatására.
- **Dinamikus eszközválasztás**: Kombinálja a RAG-et az eszközleírásokon az MAF eszközregisztrációjával, hogy csak a vonatkozó eszközöket jelenítse meg lekérdezésenként.
- **Több ügynök közötti átadás**: Használja a munkafolyamat éleket és feltételes útválasztást a specializált ügynökök közötti átadások orkestrálására.

## LangChain / LangGraph Ügynökök hosztolása Microsoft Foundry-n

A Microsoft Agent Framework **keretrendszer-interoperábilis** — nem kötött az MAF segítségével írt ügynökökhöz. Ha már van egy ügynöke, amit **LangChain** vagy **LangGraph** segítségével épített, futtathatja azt **Microsoft Foundry hosztolt ügynökként**, így a Foundry kezeli a futásidőt, munkameneteket, skálázást, azonosítást és protokoll végpontokat, míg az ügynök logikája a LangGraph-ban marad.

Ez a `langchain_azure_ai.agents.hosting` csomaggal valósítható meg, amely egy lefordított LangGraph gráfot tesz elérhetővé ugyanazokon a protokollokon, amelyeket a Foundry hosztolt ügynökök használnak.

**1. Telepítse a hosting kiegészítőt:**

```bash
pip install -U "langchain-azure-ai[hosting]>=1.2.4" azure-identity
```

A `hosting` kiegészítő telepíti a Foundry protokoll könyvtárait: az `azure-ai-agentserver-responses` (az OpenAI-kompatibilis `/responses` végpont) és az `azure-ai-agentserver-invocations` (a generikus `/invocations` végpont).

**2. Válasszon hosting protokollt:**

| Protokoll | Hoszt osztály | Végpont | Használat esete |
|----------|---------------|---------|-----------------|
| **Responses** | `ResponsesHostServer` | `/responses` | OpenAI-kompatibilis chat, streaming, válasz előzmények és beszélgetés szálazás támogatása – az ajánlott alapértelmezett konverzációs ügynökök számára. |
| **Invocations** | `InvocationsHostServer` | `/invocations` | Egyedi JSON formátum, webhook-szerű végpont vagy nem konverzációs feldolgozás szükséges. |

Mivel a **Responses API a Foundry-ban az elsődleges ügynök-fejlesztési API**, a legtöbb ügynöknél kezdje a `ResponsesHostServer`-rel.

**3. Konfigurálja a környezeti változókat** (`az login` lefuttatása előtte, hogy a `DefaultAzureCredential` tudjon hitelesíteni):

```bash
export FOUNDRY_PROJECT_ENDPOINT="https://<resource>.services.ai.azure.com/api/projects/<project>"
export FOUNDRY_MODEL_NAME="gpt-5-mini"
```

Amikor az ügynök később fut egy hosztolt ügynökként a Foundry-ban, a platform automatikusan injektálja a `FOUNDRY_PROJECT_ENDPOINT` változót.

**4. Tegye elérhetővé a LangGraph ügynököt a Responses protokollon keresztül:**

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

    # A ChatOpenAI itt a Foundry projekt OpenAI-kompatibilis (Responses) végpontját célozza meg.
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

Futtassa helyben a `python main.py` parancsal, majd küldjön egy Responses kérést a `http://localhost:8088/responses` címre.

**Kulcs viselkedések:**

- **Beszélgetések**: Az ügyfelek folytatják a beszélgetést `previous_response_id` vagy egy `conversation` azonosító átadásával. Ha a gráf LangGraph checkpointot használ, a Foundry a beszélgetési állapotot a checkpointhoz köti (gyártásban tartós checkpointot használjon; helyi tesztelésre a MemorySaver megfelelő).
- **Ember a hurkon belül**: Ha a gráf használja a LangGraph `interrupt()` funkcióját, a `ResponsesHostServer` a függőben lévő megszakítást válaszként (`function_call` / `mcp_approval_request`) jelzi, és az ügyfelek a hozzá illeszkedő `function_call_output` / `mcp_approval_response` válasszal folytathatják.
- **Kibocsátás a Foundry-ba**: Használja az Azure Developer CLI-t — `azd ext install azure.ai.agents`, `azd ai agent init -m <manifest>`, `azd ai agent run` (helyi, Docker szükséges), majd `azd provision` és `azd deploy`. A hosztolt ügynök telepítéséhez szükség van a **Foundry Project Manager** szerepre.

Ennek a példának futtatható verziója a [code-samples/14-langchain-hosted-agent.py](../../../14-microsoft-agent-framework/code-samples/14-langchain-hosted-agent.py) fájlban található. A teljes ismertetőért (Invocations protokoll, egyedi kérés sémák és hibajavítás) lásd a [Host LangGraph agents as Foundry hosted agents](https://learn.microsoft.com/azure/foundry/how-to/develop/langchain-hosted-agents) oldalt.

## Kódminták 

A Microsoft Agent Framework kódmintái megtalálhatók ebben a tárolóban az `xx-python-agent-framework` és `xx-dotnet-agent-framework` fájlok alatt.

## Több kérdésed van a Microsoft Agent Frameworkkel kapcsolatban?

Csatlakozz a [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D) közösséghez, hogy találkozz más tanulókkal, részt vegyél az irodai órákon, és választ kapj MI Ügynökökkel kapcsolatos kérdéseidre.
## Előző lecke

[Memória MI Ügynökök számára](../13-agent-memory/README.md)

## Következő lecke

[Számítógép-használati ügynökök építése (CUA)](../15-browser-use/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Jogi nyilatkozat**:
Ez a dokumentum az AI fordítási szolgáltatás, a [Co-op Translator](https://github.com/Azure/co-op-translator) segítségével készült. Bár az pontosságra törekszünk, kérjük, vegye figyelembe, hogy az automatikus fordítások hibákat vagy pontatlanságokat tartalmazhatnak. Az eredeti dokumentum az anyanyelvén tekintendő hiteles forrásnak. Fontos információk esetén professzionális emberi fordítást javasolunk. Nem vállalunk felelősséget semmilyen félreértésért vagy téves értelmezésért, amely ebből a fordításból ered.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->