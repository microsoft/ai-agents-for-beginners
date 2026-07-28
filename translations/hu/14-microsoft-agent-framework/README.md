# A Microsoft Agent Framework felfedezése

![Agent Framework](../../../translated_images/hu/lesson-14-thumbnail.90df0065b9d234ee.webp)

### Bevezetés

Ez a lecke a következőkről fog szólni:

- A Microsoft Agent Framework megértése: kulcsfontosságú jellemzők és érték
- A Microsoft Agent Framework kulcsfogalmainak feltárása
- Fejlett MAF minták: munkafolyamatok, middleware és memória

## Tanulási célok

A lecke elvégzése után tudni fogod, hogyan kell:

- Gyártásra kész AI ügynököket építeni a Microsoft Agent Framework segítségével
- Alkalmazni a Microsoft Agent Framework alapvető funkcióit az ügynöki használati esetekre
- Haladó mintákat használni, beleértve a munkafolyamatokat, middleware-t és megfigyelhetőséget

## Kódpéldák

A [Microsoft Agent Framework (MAF)](https://aka.ms/ai-agents-beginners/agent-framework) kódmintái megtalálhatók ebben a tárházban az `xx-python-agent-framework` és `xx-dotnet-agent-framework` fájlok alatt.

## A Microsoft Agent Framework megértése

![Framework Intro](../../../translated_images/hu/framework-intro.077af16617cf130c.webp)

A [Microsoft Agent Framework (MAF)](https://aka.ms/ai-agents-beginners/agent-framework) a Microsoft egységes keretrendszere AI ügynökök építésére. Rugalmasságot kínál, hogy kezelje az ügynökhasználati esetek széles skáláját mind produkciós, mind kutatási környezetekben, beleértve:

- **Szekvenciális ügynök-orkesztáció** olyan helyzetekben, ahol lépésről-lépésre történő munkafolyamatokra van szükség.
- **Párhuzamos orkesztáció** olyan helyzetekben, amikor az ügynököknek egyszerre kell feladatokat végrehajtaniuk.
- **Csoportos beszélgetés-orkesztáció** olyan helyzetekben, amikor az ügynökök együttműködhetnek egy feladaton.
- **Átadási orkesztáció** olyan helyzetekben, amikor az ügynökök átadják a feladatot egymásnak, amint az alfeladatok elkészültek.
- **Mágneses orkesztáció** olyan helyzetekben, ahol egy menedzserügynök létrehoz és módosít feladatlistákat, és kezeli az alügynökök koordinációját a feladat teljesítéséhez.

Az AI ügynökök produkcióban történő biztosításához a MAF a következő funkciókat is tartalmazza:

- **Megfigyelhetőség** az OpenTelemetry használatával, amely figyeli az AI ügynök minden tevékenységét, beleértve az eszközhasználatot, az orkesztációs lépéseket, az érvelési folyamatokat és a teljesítményfigyelést a Microsoft Foundry műszerfalakon keresztül.
- **Biztonság** azáltal, hogy az ügynökök natívan futnak a Microsoft Foundry-n, amely biztonsági vezérlőket tartalmaz, például szerepalapú hozzáférést, privát adatkezelést és beépített tartalombiztonságot.
- **Tartósság**, mivel az ügynök szálak és munkafolyamatok szüneteltethetők, folytathatók és hibákból felépülhetnek, ami lehetővé teszi a hosszabb futású folyamatokat.
- **Ellenőrzés**, mivel támogatottak az emberi beavatkozással működő munkafolyamatok, ahol a feladatok emberi jóváhagyást igényelnek.

A Microsoft Agent Framework interoperábilitásra is fókuszál:

- **Felhőfüggetlen** - Az ügynökök futhatnak konténerekben, helyszínen vagy többféle felhőn keresztül.
- **Szolgáltatófüggetlen** - Az ügynökök létrehozhatók a preferált SDK-val, beleértve az Azure OpenAI-t és az OpenAI-t.
- **Nyílt szabványok integrálása** - Az ügynökök használhatnak olyan protokollokat, mint az Agent-to-Agent (A2A) és a Model Context Protocol (MCP), hogy felfedezzék és használják más ügynököket és eszközöket.
- **Bővítmények és csatlakozók** - Csatlakozások létrehozhatók adat- és memória szolgáltatásokhoz, például Microsoft Fabric, SharePoint, Pinecone és Qdrant.

Nézzük meg, hogyan alkalmazzák ezeket a funkciókat a Microsoft Agent Framework néhány kulcsfogalmára.

## A Microsoft Agent Framework kulcsfogalmai

### Ügynökök

![Agent Framework](../../../translated_images/hu/agent-components.410a06daf87b4fef.webp)

**Ügynökök létrehozása**

Az ügynök létrehozása úgy történik, hogy meghatározzuk az inferencia szolgáltatást (LLM Szolgáltató), az AI ügynök által követendő utasításkészletet, és hozzárendeljük a `name` értéket:


```python
agent = AzureOpenAIChatClient(credential=AzureCliCredential()).create_agent( instructions="You are good at recommending trips to customers based on their preferences.", name="TripRecommender" )
```

Az előbbi példa az `Azure OpenAI`-t használja, de az ügynökök létrehozhatók különféle szolgáltatásokkal, beleértve a `Microsoft Foundry Agent Service`-t is:

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

vagy a [MiniMax](https://platform.minimaxi.com/) használatával, amely OpenAI-kompatibilis API-t kínál nagy kontextusablakkal (akár 204K tokenig):

```python
agent = OpenAIChatClient(base_url="https://api.minimax.io/v1", api_key=os.environ["MINIMAX_API_KEY"], model_id="MiniMax-M3").create_agent( name="HelpfulAssistant", instructions="You are a helpful assistant.", )
```

vagy távoli ügynökök az A2A protokollal:

```python
agent = A2AAgent( name=agent_card.name, description=agent_card.description, agent_card=agent_card, url="https://your-a2a-agent-host" )
```

**Ügynökök futtatása**

Az ügynökök `.run` vagy `.run_stream` metódusokkal futtathatók, nem-streaming vagy streaming válaszokkal.

```python
result = await agent.run("What are good places to visit in Amsterdam?")
print(result.text)
```

```python
async for update in agent.run_stream("What are the good places to visit in Amsterdam?"):
    if update.text:
        print(update.text, end="", flush=True)

```

Minden ügynök futtatásához lehetőség van olyan paraméterek testreszabására is, mint az ügynök által használt `max_tokens`, az ügynök által hívható `tools`, vagy akár magának az ügynök által használt `model`.

Ez hasznos olyan esetekben, amikor a felhasználói feladat elvégzéséhez specifikus modellek vagy eszközök szükségesek.

**Eszközök**

Az eszközök definiálhatók az ügynök definiálásakor:

```python
def get_attractions( location: Annotated[str, Field(description="The location to get the top tourist attractions for")], ) -> str: """Get the top tourist attractions for a given location.""" return f"The top attractions for {location} are." 


# Amikor közvetlenül ChatAgent-et hozunk létre

agent = ChatAgent( chat_client=OpenAIChatClient(), instructions="You are a helpful assistant", tools=[get_attractions]

```

és az ügynök futtatásakor is:

```python

result1 = await agent.run( "What's the best place to visit in Seattle?", tools=[get_attractions] # Az eszköz csak ehhez a futtatáshoz érhető el )
```

**Ügynök Szálak**

Az ügynök szálakat többszörös körös beszélgetések kezelésére használják. A szálak létrehozhatók:

- A `get_new_thread()` használatával, ami lehetővé teszi, hogy a szál idővel el legyen mentve
- Szálak automatikus létrehozásával az ügynök futtatásakor, ahol a szál csak az adott futtatásig él.

Egy szál létrehozásához a kód a következő:

```python
# Hozzon létre egy új szálat.
thread = agent.get_new_thread() # Futtassa az ügynököt a szállal.
response = await agent.run("Hello, I am here to help you book travel. Where would you like to go?", thread=thread)

```

Majd a szál sorosítható későbbi tárolásra:

```python
# Hozzon létre egy új szálat.
thread = agent.get_new_thread() 

# Futtassa az ügynököt a szállal.

response = await agent.run("Hello, how are you?", thread=thread) 

# Sorosítsa a szálat tároláshoz.

serialized_thread = await thread.serialize() 

# Deszerializálja a szál állapotát a tárolóból való betöltés után.

resumed_thread = await agent.deserialize_thread(serialized_thread)
```

**Ügynök Middleware**

Az ügynökök kölcsönhatásban állnak eszközökkel és LLM-ekkel a felhasználói feladatok teljesítéséhez. Bizonyos esetekben szeretnénk végrehajtani vagy követni az ezek közötti interakciókat. Az ügynök middleware ezt teszi lehetővé a következők révén:

*Funkció Middleware*

Ez a middleware lehetővé teszi, hogy egy lépést hajtsunk végre az ügynök és egy funkció/eszköz hívása között. Például hasznos lehet a funkcióhívások naplózása.

Az alábbi kódban a `next` határozza meg, hogy a következő middleware vagy a tényleges funkció hívódjon.

```python
async def logging_function_middleware(
    context: FunctionInvocationContext,
    next: Callable[[FunctionInvocationContext], Awaitable[None]],
) -> None:
    """Function middleware that logs function execution."""
    # Előfeldolgozás: Naplózás a függvény végrehajtása előtt
    print(f"[Function] Calling {context.function.name}")

    # Folytatás a következő middleware vagy függvény végrehajtásához
    await next(context)

    # Utófeldolgozás: Naplózás a függvény végrehajtása után
    print(f"[Function] {context.function.name} completed")
```

*Chat Middleware*

Ez a middleware lehetővé teszi egy akció végrehajtását vagy naplózását az ügynök és az LLM közötti üzenetváltás során.

Ez tartalmaz fontos információkat, például az AI szolgáltatásnak küldött `messages`-eket.

```python
async def logging_chat_middleware(
    context: ChatContext,
    next: Callable[[ChatContext], Awaitable[None]],
) -> None:
    """Chat middleware that logs AI interactions."""
    # Előfeldolgozás: Naplózás az MI hívás előtt
    print(f"[Chat] Sending {len(context.messages)} messages to AI")

    # Folytatás a következő middleware vagy MI szolgáltatáshoz
    await next(context)

    # Utófeldolgozás: Naplózás az MI válasz után
    print("[Chat] AI response received")

```

**Ügynök Memória**

Ahogy az `Agentic Memory` leckében szerepel, a memória fontos eleme annak, hogy az ügynök különböző kontextusokban tudjon működni. A MAF többféle memóriatípust kínál:

*Memória a memóriában (In-Memory Storage)*

Ez a memória az alkalmazás futása során a szálakban tárolódik.

```python
# Hozzon létre egy új szálat.
thread = agent.get_new_thread() # Futtassa az ügynököt a szállal.
response = await agent.run("Hello, I am here to help you book travel. Where would you like to go?", thread=thread)
```

*Tartós üzenetek*

Ezt a memóriát több munkamenet közötti beszélgetés előzményeinek tárolására használják. A `chat_message_store_factory` segítségével definiálható:

```python
from agent_framework import ChatMessageStore

# Egyedi üzenettár létrehozása
def create_message_store():
    return ChatMessageStore()

agent = ChatAgent(
    chat_client=OpenAIChatClient(),
    instructions="You are a Travel assistant.",
    chat_message_store_factory=create_message_store
)

```

*Dinamikus memória*

Ez a memória az ügynökök futtatása előtt kerül hozzáadásra a kontextushoz. Ezek a memóriák külső szolgáltatásokban is tárolhatók, például mem0-ban:

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

**Ügynök Megfigyelhetőség**

A megfigyelhetőség fontos a megbízható és karbantartható ügynökrendszerek építéséhez. A MAF integrálódik OpenTelemetry-vel a jobb követés és mérés érdekében.

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

A MAF előre definiált munkafolyamatokat kínál, amelyek lépéseket tartalmaznak a feladat elvégzésére, és AI ügynököket is beépít összetevőként ezekben a lépésekben.

A munkafolyamatok különböző komponensekből állnak, amelyek jobb vezérlést tesznek lehetővé. A munkafolyamatok támogatják a **több ügynökből álló orkesztációt** és a **mentési pontokat** a munkafolyamat állapotának megőrzésére.

A munkafolyamat alapvető összetevői:

**Végrehajtók**

A végrehajtók bemeneti üzeneteket kapnak, végrehajtják a kijelölt feladatokat, majd kimeneti üzenetet állítanak elő. Ez előreviszi a munkafolyamatot a nagyobb feladat teljesítése felé. A végrehajtók lehetnek AI ügynökök vagy egyéni logika.

**Élek**

Az élek definiálják az üzenetek áramlását a munkafolyamatban. Ezek lehetnek:

*Közvetlen élek* - Egyszerű egy az egyhez kapcsolat a végrehajtók között:

```python
from agent_framework import WorkflowBuilder

builder = WorkflowBuilder()
builder.add_edge(source_executor, target_executor)
builder.set_start_executor(source_executor)
workflow = builder.build()
```

*Feltételes élek* - Egy adott feltétel teljesülése után aktiválódnak. Például, ha a szállodai szobák nem elérhetők, a végrehajtó más lehetőségeket javasolhat.

*Switch-case élek* - Üzenetek irányítása különböző végrehajtókhoz meghatározott feltételek alapján. Például, ha egy utazási ügyfél prioritásos hozzáféréssel rendelkezik, a feladatait egy másik munkafolyamat kezeli.

*Fan-out élek* - Egy üzenet küldése több célpontra.

*Fan-in élek* - Több üzenet összegyűjtése különböző végrehajtóktól, majd egyetlen célpontnak való továbbítás.

**Események**

A jobb megfigyelhetőség érdekében a MAF beépített eseményeket kínál a végrehajtás során, többek között:

- `WorkflowStartedEvent`  - A munkafolyamat végrehajtása megkezdődik
- `WorkflowOutputEvent` - A munkafolyamat kimenetet állít elő
- `WorkflowErrorEvent` - A munkafolyamat hibát tapasztal
- `ExecutorInvokeEvent`  - A végrehajtó elindítja a feldolgozást
- `ExecutorCompleteEvent`  -  A végrehajtó befejezi a feldolgozást
- `RequestInfoEvent` - Kérés érkezik

## Fejlett MAF Minták

A fentiek a Microsoft Agent Framework kulcsfogalmait tárgyalják. Amint összetettebb ügynököket építesz, fontolj meg néhány fejlett mintát:

- **Middleware Kompozíció**: Több middleware kezelő láncolása (naplózás, hitelesítés, sebességkorlátozás) funkció- és chat middleware-rel az ügynök viselkedésének finomhangolt irányításához.
- **Munkafolyamat Mentési Pontok**: Munkafolyamat események és sorosítás használata a hosszú futású ügynök folyamatok mentésére és folytatására.
- **Dinamikus Eszközválasztás**: A RAG kombinálása az eszközleírások alapján a MAF eszközregisztrációjával, hogy lekérdezésenként csak releváns eszközöket jelenítsen meg.
- **Több Ügynök Közötti Átadás**: Munkafolyamat élek és feltételes irányítás használata a specializált ügynökök közötti átadások megszervezéséhez.

## LangChain / LangGraph Ügynökök tárolása Microsoft Foundry-n

A Microsoft Agent Framework **keretrendszer interoperábilis** — nem vagy korlátozva a MAF-val írt ügynökökre. Ha már rendelkezel egy **LangChain** vagy **LangGraph** ügynökkel, futtathatod azt, mint egy **Microsoft Foundry által tárolt ügynököt**, így a Foundry kezeli a futási időt, munkameneteket, méretezést, azonosítást és protokoll végpontokat, miközben az ügynök logikád a LangGraph-ban marad.

Ezt a `langchain_azure_ai.agents.hosting` csomaggal érik el, amely egy lefordított LangGraph gráfot tesz elérhetővé ugyanazokon a protokollokon keresztül, amelyeket a Foundry tárolt ügynökei használnak.

**1. Telepítsd a hosting extrát:**

```bash
pip install -U "langchain-azure-ai[hosting]>=1.2.4" azure-identity
```

A `hosting` extra telepíti a Foundry protokoll könyvtárakat: `azure-ai-agentserver-responses` (az OpenAI-kompatibilis `/responses` végpont) és `azure-ai-agentserver-invocations` (az általános `/invocations` végpont).

**2. Válassz egy hosting protokollt:**

| Protokoll | Host osztály | Végpont | Használat ideje |
|----------|-----------|----------|----------|
| **Responses** | `ResponsesHostServer` | `/responses` | Olyan ügynökök számára ajánlott alapértelmezett, akik OpenAI-kompatibilis chatet, streaminget, válasz előzményeket és beszélgetés szálazást szeretnének. |
| **Invocations** | `InvocationsHostServer` | `/invocations` | Ha egyedi JSON formátumra, webhook-stílusú végpontra vagy nem beszélgetés alapú feldolgozásra van szükséged. |

Mivel a **Responses API a fő API agent-stílusú fejlesztéshez a Foundry-ban**, a legtöbb ügynökhöz kezd a `ResponsesHostServer`-rel.

**3. Konfiguráld a környezeti változókat** (`az login` előtte, hogy a `DefaultAzureCredential` tudjon hitelesíteni):

```bash
export FOUNDRY_PROJECT_ENDPOINT="https://<resource>.services.ai.azure.com/api/projects/<project>"
export FOUNDRY_MODEL_NAME="gpt-5-mini"
```

Amikor az ügynök később tárolt ügynökként fut a Foundry-ban, a platform automatikusan kezeli a `FOUNDRY_PROJECT_ENDPOINT` változót.

**4. Tedd elérhetővé a LangGraph ügynököt a Responses protokollon keresztül:**

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

    # A ChatOpenAI itt a Foundry projekt OpenAI-kompatibilis (Válaszok) végpontját célozza meg.
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

Futtasd helyben a `python main.py` paranccsal, majd küldj egy Responses kérést a `http://localhost:8088/responses` címre.

**Fontos viselkedések:**

- **Beszélgetések**: Az ügyfelek egy beszélgetést folytatnak a `previous_response_id` vagy egy `conversation` azonosító továbbításával. Ha a gráfot LangGraph checkpoint-al fordították le, a Foundry a beszélgetés állapotát a checkpoint-hoz rendeli (használj tartós checkpointot produkcióban; a `MemorySaver` helyi teszteléshez megfelelő).
- **Emberi beavatkozás**: Ha a gráf használja a LangGraph `interrupt()` függvényt, a `ResponsesHostServer` megjeleníti a függőben lévő megszakítást mint Responses `function_call` / `mcp_approval_request` elemet, és az ügyfelek folytatják egy megfelelő `function_call_output` / `mcp_approval_response`-sal.
- **Foundry-ba telepítés**: Használd az Azure Developer CLI-t — `azd ext install azure.ai.agents`, `azd ai agent init -m <manifest>`, `azd ai agent run` (helyi, Docker szükséges), majd `azd provision` és `azd deploy`. A tárolt ügynök telepítéséhez szükséges a **Foundry Project Manager** szerepkör.

Ennek a példának egy futtatható változata megtalálható a [code-samples/14-langchain-hosted-agent.py](../../../14-microsoft-agent-framework/code-samples/14-langchain-hosted-agent.py) fájlban. A teljes bemutatóért (Invocations protokoll, egyedi kérés sémák és hibakeresés) lásd: [Host LangGraph agents as Foundry hosted agents](https://learn.microsoft.com/azure/foundry/how-to/develop/langchain-hosted-agents).

## Kódpéldák

A Microsoft Agent Framework-kel kapcsolatos kódminták megtalálhatóak a tárházban az `xx-python-agent-framework` és `xx-dotnet-agent-framework` fájlok alatt.

## További kérdéseid vannak a Microsoft Agent Framework-ről?

Csatlakozz a [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D) szerverhez, hogy találkozz más tanulókkal, részt vegyél hivatalos órákon és választ kapj AI ügynökökkel kapcsolatos kérdéseidre.
## Előző lecke

[Memória az AI ügynökök számára](../13-agent-memory/README.md)

## Következő lecke

[Számítógép-használati ügynökök építése (CUA)](../15-browser-use/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Jogi nyilatkozat**:
Ez a dokumentum az AI fordítási szolgáltatás, a [Co-op Translator](https://github.com/Azure/co-op-translator) segítségével készült. Bár az pontosságra törekszünk, kérjük, vegye figyelembe, hogy az automatikus fordítások hibákat vagy pontatlanságokat tartalmazhatnak. Az eredeti dokumentum az anyanyelvén tekintendő hiteles forrásnak. Fontos információk esetén professzionális emberi fordítást javasolunk. Nem vállalunk felelősséget semmilyen félreértésért vagy téves értelmezésért, amely ebből a fordításból ered.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->