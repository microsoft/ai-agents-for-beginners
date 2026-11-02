# A Microsoft Agent Framework felfedezése

![Agent Framework](../../../translated_images/hu/lesson-14-thumbnail.90df0065b9d234ee.webp)

### Bevezetés

Ez az óra a következőket fogja lefedni:

- A Microsoft Agent Framework megértése: kulcsfontosságú jellemzők és előnyök  
- A Microsoft Agent Framework kulcsfontosságú fogalmainak feltárása
- Fejlett MAF minták: munkafolyamatok, köztes szoftver és memória

## Tanulási célok

A lecke befejezése után tudni fogod, hogyan kell:

- Gyártásra kész MI ügynököket építeni a Microsoft Agent Framework használatával
- Alkalmazni a Microsoft Agent Framework alapvető jellemzőit az ügynökös felhasználási esetekre
- Haladó mintákat alkalmazni, beleértve a munkafolyamatokat, köztes szoftvert és megfigyelhetőséget

## Kódminták

A [Microsoft Agent Framework (MAF)](https://learn.microsoft.com/en-us/agent-framework/overview/?wt.mc_id=youtube_26688_organicsocial_reactor&pivots=programming-language-python) kódmintái elérhetőek ebben a tárházban az `xx-python-agent-framework` és `xx-dotnet-agent-framework` fájlok alatt.

## A Microsoft Agent Framework megértése

![Framework Intro](../../../translated_images/hu/framework-intro.077af16617cf130c.webp)

A [Microsoft Agent Framework (MAF)](https://learn.microsoft.com/en-us/agent-framework/overview/?wt.mc_id=youtube_26688_organicsocial_reactor&pivots=programming-language-python) a Microsoft egységes keretrendszere MI ügynökök építéséhez. Rugalmasságot kínál az ügynökös felhasználási esetek sokféleségének kezelésére mind gyártási, mind kutatási környezetben, beleértve:

- **Szekvenciális ügynökközvetítést** olyan esetekben, amikor lépésenkénti munkafolyamatokra van szükség.
- **Párhuzamos közvetítést** olyan esetekben, amikor az ügynököknek egyszerre kell feladatokat elvégezniük.
- **Csoportos csevegés-közvetítést** olyan esetekben, amikor az ügynökök egy feladaton együttműködve dolgoznak.
- **Átadás-közvetítést** olyan esetekben, amikor az ügynökök átadják egymásnak a feladatot, amint az alfeladatok elkészülnek.
- **Mágneses közvetítést** olyan esetekben, amikor egy felügyelő ügynök létrehoz és módosít egy feladatlistát, és kezeli az alügynökök koordinációját a feladat végrehajtásához.

Az MI ügynökök gyártási szintű kiszállításához a MAF tartalmazza továbbá a következő jellemzőket:

- **Megfigyelhetőség** az OpenTelemetry használatával, ahol az MI ügynök minden műveletét, beleértve az eszköz-hívásokat, közvetítési lépéseket, érvelési folyamatokat és teljesítmény-ellenőrzést a Microsoft Foundry műszerfalain keresztül rögzítjük.
- **Biztonság** azzal, hogy az ügynökök natívan a Microsoft Foundry-n futnak, amely tartalmaz biztonsági vezérlőket, mint például szerepalapú hozzáférés, privát adatok kezelése és beépített tartalombiztonság.
- **Tartósság** mivel az ügynök szálak és munkafolyamatok szüneteltethetők, folytathatók és hiba esetén helyreállíthatók, ami lehetővé teszi a hosszabb folyamatos működést.
- **Ellenőrzés** olyan emberi részvételt támogató munkafolyamatokkal, ahol a feladatokat emberi jóváhagyás szükségességével jelölik.

A Microsoft Agent Framework az interoperabilitásra is fókuszál a következők által:

- **Felhőfüggetlenség** - Az ügynökök futhatnak konténerekben, helyszínen és több különböző felhőn keresztül.
- **Szolgáltatófüggetlenség** - Az ügynökök létrehozhatók a kedvenc SDK-d használatával, beleértve az Azure OpenAI és OpenAI-t.
- **Nyílt szabványok integrálása** - Az ügynökök használhatnak olyan protokollokat, mint az Agent-to-Agent (A2A) és a Model Context Protocol (MCP), hogy felfedezzék és használják más ügynököket és eszközöket.
- **Bővítmények és csatlakozók** - Kapcsolódások hozhatók létre adat- és memória szolgáltatásokhoz, mint a Microsoft Fabric, SharePoint, Pinecone és Qdrant.

Nézzük meg, hogyan alkalmazzák ezeket a jellemzőket a Microsoft Agent Framework néhány alapvető fogalmára.

## A Microsoft Agent Framework kulcsfogalmai

### Ügynökök

![Agent Framework](../../../translated_images/hu/agent-components.410a06daf87b4fef.webp)

**Ügynökök létrehozása**

Az ügynök létrehozása az inferencia szolgáltatás (LLM szolgáltató), az AI ügynök számára követendő utasítások és egy hozzárendelt `name` megadásával történik:


```python
agent = AzureOpenAIChatClient(credential=AzureCliCredential()).create_agent( instructions="You are good at recommending trips to customers based on their preferences.", name="TripRecommender" )
```

A fenti példa az `Azure OpenAI`-t használja, de az ügynökök létrehozhatók különféle szolgáltatásokkal, beleértve a `Microsoft Foundry Agent Service`-t is:

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

vagy a [MiniMax](https://platform.minimaxi.com/) használatával, amely OpenAI-kompatibilis API-t biztosít nagyméretű kontextusablakokkal (akár 204K tokenig):

```python
agent = OpenAIChatClient(base_url="https://api.minimax.io/v1", api_key=os.environ["MINIMAX_API_KEY"], model_id="MiniMax-M3").create_agent( name="HelpfulAssistant", instructions="You are a helpful assistant.", )
```

vagy távoli ügynökökkel az A2A protokoll használatával:

```python
agent = A2AAgent( name=agent_card.name, description=agent_card.description, agent_card=agent_card, url="https://your-a2a-agent-host" )
```

**Ügynökök futtatása**

Az ügynökök a `.run` vagy `.run_stream` metódusokkal futtathatók nem folyamatos vagy folyamatos válaszok esetén.

```python
result = await agent.run("What are good places to visit in Amsterdam?")
print(result.text)
```

```python
async for update in agent.run_stream("What are the good places to visit in Amsterdam?"):
    if update.text:
        print(update.text, end="", flush=True)

```

Minden ügynök futtatásához opcionálisan megadhatók paraméterek, mint például az ügynök által használt `max_tokens`, a hívható `tools` és maga az ügynök által használt `model`.

Ez hasznos olyan esetekben, amikor specifikus modellekre vagy eszközökre van szükség a felhasználói feladat elvégzéséhez.

**Eszközök**

Az eszközök definiálhatók az ügynök definiálásakor:

```python
def get_attractions( location: Annotated[str, Field(description="The location to get the top tourist attractions for")], ) -> str: """Get the top tourist attractions for a given location.""" return f"The top attractions for {location} are." 


# Amikor közvetlenül egy ChatAgent-et hozunk létre

agent = ChatAgent( chat_client=OpenAIChatClient(), instructions="You are a helpful assistant", tools=[get_attractions]

```

és az ügynök futtatásakor is:

```python

result1 = await agent.run( "What's the best place to visit in Seattle?", tools=[get_attractions] # Csak erre a futtatásra biztosított eszköz )
```

**Ügynök szálak**

Az ügynök szálak többmenetes beszélgetések kezelésére szolgálnak. Szálakat lehet létrehozni a következő módokon:

- A `get_new_thread()` használatával, ami lehetővé teszi a szál időbeni mentését
- Egy szál automatikus létrehozásával az ügynök futtatásakor, ahol a szál csak az aktuális futás ideje alatt létezik.

Egy szál létrehozásának kódja így néz ki:

```python
# Hozzon létre egy új szálat.
thread = agent.get_new_thread() # Futtassa az ügynököt a szállal.
response = await agent.run("Hello, I am here to help you book travel. Where would you like to go?", thread=thread)

```

A szál sorosítható, hogy később tárolható legyen:

```python
# Hozzon létre egy új szálat.
thread = agent.get_new_thread() 

# Futtassa az ügynököt a szálal.

response = await agent.run("Hello, how are you?", thread=thread) 

# Szerializálja a szálat tároláshoz.

serialized_thread = await thread.serialize() 

# Deszerializálja a szál állapotát betöltés után a tárolóból.

resumed_thread = await agent.deserialize_thread(serialized_thread)
```

**Ügynök köztes szoftver**

Az ügynökök eszközökkel és LLM-ekkel lépnek interakcióba a felhasználói feladatok elvégzéséhez. Bizonyos esetekben szeretnénk köztes műveleteket végrehajtani vagy nyomon követni ezeket az interakciókat. Az ügynök köztes szoftver lehetővé teszi ezt:

*Funkció köztes szoftver*

Ez a köztes szoftver lehetővé teszi, hogy egy műveletet hajtsunk végre az ügynök és a hívott funkció/eszköz között. Például naplózást végezhetünk a funkcióhíváson.

A következő kódban a `next` határozza meg, hogy a következő köztes szoftver vagy a tényleges funkció hívódjon meg.

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

*Chat köztes szoftver*

Ez a köztes szoftver lehetővé teszi, hogy műveleteket hajtsunk végre vagy naplózzunk az ügynök és a LLM közötti kérések között.

Ez tartalmaz fontos információkat, például az AI szolgáltatásnak küldött `messages`.

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

Ahogy az `Agentic Memory` leckében áttekintettük, a memória fontos elem az ügynök számára, hogy különböző kontextusokban tudjon működni. A MAF több memória típust kínál:

*Memória a futásidő alatt (In-Memory Storage)*

Ez a memória a szálakban kerül tárolásra az alkalmazás futásideje alatt.

```python
# Hozzon létre egy új szálat.
thread = agent.get_new_thread() # Futtassa az ügynököt a szállal.
response = await agent.run("Hello, I am here to help you book travel. Where would you like to go?", thread=thread)
```

*Tartós üzenetek (Persistent Messages)*

Ez a memória a beszélgetés előzményeinek tárolására szolgál különböző munkamenetek között. A `chat_message_store_factory` használatával definiáljuk:

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

*Dinamikus memória (Dynamic Memory)*

Ez a memória az ügynökök futtatása előtt kerül hozzáadásra a kontextushoz. Ezeket mem0-szerű külső szolgáltatásokban lehet tárolni:

```python
from agent_framework.mem0 import Mem0Provider

# Mem0 használata fejlett memóriafunkciókhoz
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

**Ügynök megfigyelhetőség**

A megfigyelhetőség fontos a megbízható és karbantartható ügynökrendszerek építéséhez. A MAF integrál az OpenTelemetry-vel, hogy jobb megfigyelhetőséget biztosítson követés és mérőszámok formájában.

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

A MAF előre definiált munkafolyamatokat kínál, amelyek lépéseket tartalmaznak egy feladat végrehajtásához, és MI ügynököket építenek be az egyes lépések összetevőjeként.

A munkafolyamatok különböző komponensekből állnak, amelyek jobb vezérlési áramlást tesznek lehetővé. A munkafolyamatok támogatják a **több ügynökös közvetítést** és a **mentési pontokat (checkpointing)** a munkafolyamat állapotainak megőrzéséhez.

A munkafolyamat kulcskomponensei:

**Végrehajtók (Executors)**

A végrehajtók bemeneti üzeneteket kapnak, végrehajtják a kijelölt feladatokat, majd kimeneti üzenetet állítanak elő. Ez továbbviszi a munkafolyamatot a nagyobb feladat véghezvitele felé. A végrehajtók AI ügynökök vagy egyedi logika lehet.

**Élek (Edges)**

Az élek a munkafolyamat üzenetáramlását határozzák meg. Ezek lehetnek:

*Közvetlen élek* - Egyszerű egy az egyhez kapcsolatok a végrehajtók között:

```python
from agent_framework import WorkflowBuilder

builder = WorkflowBuilder()
builder.add_edge(source_executor, target_executor)
builder.set_start_executor(source_executor)
workflow = builder.build()
```

*Feltételes élek* - Akkor aktiválódnak, amikor egy adott feltétel teljesül. Például, ha nincs elérhető szállodai szoba, a végrehajtó más lehetőségeket javasolhat.

*Váltó-élek (Switch-case Edges)* - Az üzeneteket különböző végrehajtókhoz irányítják előre meghatározott feltételek alapján. Például, ha az utazó vásárló prioritással rendelkezik, a feladatait egy másik munkafolyamat kezeli.

*Fan-out élek* - Egy üzenetet több célhoz küld.

*Fan-in élek* - Több üzenetet gyűjtenek össze különböző végrehajtóktól és egy célhoz küldenek.

**Események**

A jobb megfigyelhetőség érdekében a MAF beépített futtatási eseményeket kínál, például:

- `WorkflowStartedEvent`  - Munkafolyamat futtatás kezdete
- `WorkflowOutputEvent` - Munkafolyamat kimenet készül
- `WorkflowErrorEvent` - Hiba történik a munkafolyamatban
- `ExecutorInvokeEvent`  - Végrehajtó elindul
- `ExecutorCompleteEvent`  - Végrehajtó befejezte a futtatást
- `RequestInfoEvent` - Kérés történt

## Haladó MAF minták

A fentiekben a Microsoft Agent Framework kulcsfogalmait vettük át. Ahogy összetettebb ügynököket építesz, íme néhány haladó minta, amit érdemes figyelembe venni:

- **Köztes szoftver kompozíció**: Több köztes szoftver kezelőt láncolhatsz össze (naplózás, autentikáció, sebességkorlátozás) funkció és chat köztes szoftverrel az ügynök viselkedés finomhangolásához.
- **Munkafolyamat mentési pontok**: Használj munkafolyamat eseményeket és sorosítást a hosszú futású ügynök folyamatok mentésére és folytatására.
- **Dinamikus eszközválasztás**: Kombináld az eszközleírások RAG-ját a MAF eszközregisztrációval, hogy csak a lekérdezésnek megfelelő eszközöket mutassa.
- **Több ügynök átadása**: Használj munkafolyamat éleket és feltételes irányítást a specializált ügynökök közti átadások koordinálásához.

## LangChain / LangGraph ügynökök hosztolása Microsoft Foundry-n

A Microsoft Agent Framework **keretrendszer-interoperábilis** — nem vagy korlátozva csak MAF-fel írt ügynökökre. Ha már van egy ügynököd, ami **LangChain**-nel vagy **LangGraph**-gal készült, futtathatod azt **Microsoft Foundry hosztolt ügynökként**, így Foundry kezeli a futtatókörnyezetet, munkameneteket, méretezést, identitást és protokoll végpontokat, miközben az ügynök logikád LangGraph-ban marad.

Ez a `langchain_azure_ai.agents.hosting` csomag segítségével valósítható meg, amely egy LangGraph gráfot hoz létre ugyanazokon a protokollokon keresztül, amelyeket a Foundry hosztolt ügynökök használnak.

**1. Telepítsd a hosting extrát:**

```bash
pip install -U "langchain-azure-ai[hosting]>=1.2.4" azure-identity
```

A `hosting` extra telepíti a Foundry protokoll könyvtárakat: `azure-ai-agentserver-responses` (az OpenAI-kompatibilis `/responses` végpont) és `azure-ai-agentserver-invocations` (az általános `/invocations` végpont).

**2. Válassz egy hosting protokollt:**

| Protokoll | Hoszt osztály | Végpont | Használat esetén |
|----------|---------------|---------|-----------------|
| **Responses** | `ResponsesHostServer` | `/responses` | Ha OpenAI-kompatibilis chat, streaming, válaszelőzmények és beszélgetés szálazás szükséges — ez az ajánlott alapértelmezett konverzációs ügynökökhöz. |
| **Invocations** | `InvocationsHostServer` | `/invocations` | Ha egyedi JSON formára, webhook-stílusú végpontra vagy nem-konverzációs feldolgozásra van szükség. |

Mivel a **Responses API a fő API az ügynök-stílusú fejlesztéshez Foundry-ban**, a legtöbb ügynöknél a `ResponsesHostServer`-rel kezdjük.

**3. Konfiguráld a környezeti változókat** (`az login` előtte, hogy a `DefaultAzureCredential` tudjon hitelesíteni):

```bash
export FOUNDRY_PROJECT_ENDPOINT="https://<resource>.services.ai.azure.com/api/projects/<project>"
export FOUNDRY_MODEL_NAME="gpt-5-mini"
```

Amikor az ügynök később Foundry hosztolt ügynökként fut, a platform automatikusan befecskendezi a `FOUNDRY_PROJECT_ENDPOINT` értéket.

**4. Tegyél elérhetővé egy LangGraph ügynököt a Responses protokollon keresztül:**

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

Futtasd helyileg a `python main.py` parancsal, majd küldj egy Responses kérést a `http://localhost:8088/responses` címre.

**Kulcsfontosságú viselkedések:**

- **Beszélgetések**: A kliensek folytatják a beszélgetést úgy, hogy megadják a `previous_response_id`-t vagy egy `conversation` azonosítót. Ha a gráf LangGraph mentővel van összeállítva, Foundry a beszélgetés állapotát a mentési ponthoz köti (gyártásban tartós mentőt használj, helyi teszteléshez a `MemorySaver` megfelel).
- **Emberi beavatkozás (Human-in-the-loop)**: Ha a gráf LangGraph `interrupt()`-ot használ, a `ResponsesHostServer` a függőben lévő megszakítást egy Responses `function_call` / `mcp_approval_request` elemként jeleníti meg, és a kliensek folytatják egy megfeleltetett `function_call_output` / `mcp_approval_response`-szal.
- **Kiadás Foundry-ra**: Használd az Azure Developer CLI-t — `azd ext install azure.ai.agents`, `azd ai agent init -m <manifest>`, `azd ai agent run` (helyi, Docker kell hozzá), majd `azd provision` és `azd deploy`. A hosztolt ügynökök telepítéséhez a **Foundry Project Manager** szerepkör szükséges.

Egy futtatható verziója ennek a példának itt található: [code-samples/14-langchain-hosted-agent.py](../../../14-microsoft-agent-framework/code-samples/14-langchain-hosted-agent.py). A teljes útmutató (Invocations protokoll, egyedi kérelemsémák és hibakeresés) elérhető a [Host LangGraph agents as Foundry hosted agents](https://learn.microsoft.com/azure/foundry/how-to/develop/langchain-hosted-agents) oldalon.

## Kódminták

A Microsoft Agent Framework kódmintái megtalálhatók ebben a tárházban az `xx-python-agent-framework` és `xx-dotnet-agent-framework` fájlok alatt.

## Van több kérdésed a Microsoft Agent Frameworkről?

Csatlakozz a [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D) közösséghez, hogy találkozz más tanulókkal, részt vegyél az ügyfélfogadó órákon és választ kapj az MI ügynökök kérdéseidre.
## Előző lecke

[Memória MI ügynökök számára](../13-agent-memory/README.md)

## Következő lecke

[Számítógép-használó Ügynökök építése (CUA)](../15-browser-use/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Jogi nyilatkozat**:
Ez a dokumentum az AI fordítási szolgáltatás, a [Co-op Translator](https://github.com/Azure/co-op-translator) segítségével készült. Bár az pontosságra törekszünk, kérjük, vegye figyelembe, hogy az automatikus fordítások hibákat vagy pontatlanságokat tartalmazhatnak. Az eredeti dokumentum az anyanyelvén tekintendő hiteles forrásnak. Fontos információk esetén professzionális emberi fordítást javasolunk. Nem vállalunk felelősséget semmilyen félreértésért vagy téves értelmezésért, amely ebből a fordításból ered.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->