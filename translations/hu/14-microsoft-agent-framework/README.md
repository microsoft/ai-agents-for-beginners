# A Microsoft Agent Framework felfedezése

![Agent Framework](../../../translated_images/hu/lesson-14-thumbnail.90df0065b9d234ee.webp)

### Bevezetés

Ez a lecke a következőket tárgyalja:

- A Microsoft Agent Framework megértése: fő jellemzők és érték  
- A Microsoft Agent Framework kulcsfogalmainak felfedezése
- Fejlett MAF minták: munkafolyamatok, köztes szoftverek és memória

## Tanulási célok

A lecke elvégzése után tudni fogod, hogyan:

- Éles környezetbe alkalmas AI ügynököket építs a Microsoft Agent Framework segítségével
- Alkalmazd a Microsoft Agent Framework alapvető funkcióit az ügynöki felhasználási eseteidre
- Használj fejlett mintákat, beleértve a munkafolyamatokat, köztes szoftvereket és megfigyelhetőséget

## Kódminták 

A [Microsoft Agent Framework (MAF)](https://aka.ms/ai-agents-beginners/agent-framewrok) kódmintái megtalálhatók ebben a tárolóban az `xx-python-agent-framework` és az `xx-dotnet-agent-framework` fájlok alatt.

## A Microsoft Agent Framework megértése

![Framework Intro](../../../translated_images/hu/framework-intro.077af16617cf130c.webp)

[Microsoft Agent Framework (MAF)](https://aka.ms/ai-agents-beginners/agent-framewrok) a Microsoft egységes keretrendszere AI ügynökök építéséhez. Rugalmasságot kínál a különféle ügynöki felhasználási esetek kezelésére, amelyek mind a termelési, mind a kutatási környezetekben előfordulnak, többek között:

- **Szekvenciális ügynök-orchestration** olyan forgatókönyvekben, ahol lépésről lépésre történő munkafolyamatokra van szükség.
- **Párhuzamos orchestration** olyan esetekben, ahol az ügynököknek egyszerre kell feladatokat elvégezniük.
- **Csoportos csevegés orchestration** olyan helyzetekben, ahol az ügynökök egy feladaton együttműködhetnek.
- **Átadás orchestration** olyan forgatókönyvekben, ahol az ügynökök a részfeladatok elvégzése után adják át a feladatot egymásnak.
- **Mágneses orchestration** olyan esetekben, ahol egy menedzser ügynök feladatlistát hoz létre és módosít, és kezeli az alügynökök koordinációját a feladat elvégzéséhez.

Az AI ügynökök termelési bevezetéséhez a MAF a következő funkciókat is tartalmazza:

- **Megfigyelhetőség** OpenTelemetry használatával, ahol az AI ügynök minden egyes művelete, beleértve az eszközhívásokat, az orchestration lépéseket, az érvelési folyamatokat és a teljesítményfigyelést a Microsoft Foundry műszerfalakon, nyomon követhető.
- **Biztonság** az ügynökök natív hostolásával a Microsoft Foundry-n, amely biztonsági vezérlőket tartalmaz, például szerepalapú hozzáférést, privát adatok kezelését és beépített tartalombiztonságot.
- **Tartósság** mert az ügynök szálak és munkafolyamatok szüneteltethetők, folytathatók és hiba esetén helyreállíthatók, ami hosszabb futásidejű folyamatokat tesz lehetővé.
- **Ellenőrzés** emberi beavatkozást igénylő munkafolyamatok támogatása, ahol a feladatok emberi jóváhagyást igénylőként vannak megjelölve.

A Microsoft Agent Framework interoperabilitásra is törekszik az alábbi módokon:

- **Fellegfüggetlen** - Az ügynökök futtathatók konténerekben, helyben és több különböző felhőn keresztül.
- **Szolgáltatófüggetlen** - Az ügynökök létrehozhatók a preferált SDK-don keresztül, beleértve az Azure OpenAI-t és az OpenAI-t
- **Nyílt szabványok integrálása** - Az ügynökök használhatnak olyan protokollokat, mint az Agent-to-Agent (A2A) és a Model Context Protocol (MCP), hogy felfedezzék és használják más ügynököket és eszközöket.
- **Bővítmények és csatlakozók** - Kapcsolatok hozhatók létre adat- és memória szolgáltatásokhoz, mint a Microsoft Fabric, SharePoint, Pinecone és Qdrant.

Nézzük meg, hogyan alkalmazzák ezeket a funkciókat a Microsoft Agent Framework néhány alapvető koncepciójánál.

## A Microsoft Agent Framework kulcsfogalmai

### Ügynökök

![Agent Framework](../../../translated_images/hu/agent-components.410a06daf87b4fef.webp)

**Ügynökök létrehozása**

Az ügynök létrehozása úgy történik, hogy definiáljuk az inferencia szolgáltatást (LLM szolgáltató), egy sor utasítást, amelyet az AI ügynök követ, és egy hozzárendelt `name`-et:

```python
agent = AzureOpenAIChatClient(credential=AzureCliCredential()).create_agent( instructions="You are good at recommending trips to customers based on their preferences.", name="TripRecommender" )
```

A fenti példa `Azure OpenAI` használatával készült, de az ügynökök különféle szolgáltatásokkal is létrehozhatók, beleértve a `Microsoft Foundry Agent Service`-t:

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

vagy távoli ügynökök az A2A protokollt használva:

```python
agent = A2AAgent( name=agent_card.name, description=agent_card.description, agent_card=agent_card, url="https://your-a2a-agent-host" )
```

**Ügynökök futtatása**

Az ügynökök a nem-sugárzó vagy sugárzó válaszokhoz a `.run` vagy `.run_stream` metódusokkal futtathatók.

```python
result = await agent.run("What are good places to visit in Amsterdam?")
print(result.text)
```

```python
async for update in agent.run_stream("What are the good places to visit in Amsterdam?"):
    if update.text:
        print(update.text, end="", flush=True)

```

Minden ügynök futtatáshoz opciók is megadhatók a paraméterek testreszabásához, mint például az ügynök által használt `max_tokens`, azok a `tools`, amelyeket az ügynök hívhat, és maga a `model`, amely az ügynök számára használatos.

Ez hasznos olyan esetekben, amikor egy felhasználói feladat elvégzéséhez bizonyos modellekre vagy eszközökre van szükség.

**Eszközök**

Eszközök definiálhatók mind az ügynök definiálásakor:

```python
def get_attractions( location: Annotated[str, Field(description="The location to get the top tourist attractions for")], ) -> str: """Get the top tourist attractions for a given location.""" return f"The top attractions for {location} are." 


# Amikor közvetlenül hozunk létre egy ChatAgentet

agent = ChatAgent( chat_client=OpenAIChatClient(), instructions="You are a helpful assistant", tools=[get_attractions]

```

mind az ügynök futtatásakor is:

```python

result1 = await agent.run( "What's the best place to visit in Seattle?", tools=[get_attractions] # Ez az eszköz csak erre a futtatásra van biztosítva )
```

**Ügynök szálak**

Az ügynök szálakat többszörös fordulós beszélgetések kezelésére használják. A szálak létrehozhatók az alábbi módok valamelyikével:

- A `get_new_thread()` használatával, ami lehetővé teszi a szál idővel történő mentését
- Szál automatikus létrehozásával az ügynök futtatásakor, amikor a szálnak csak az aktuális futás során van élettartama.

A szál létrehozásához a kód így néz ki:

```python
# Hozzon létre egy új szálat.
thread = agent.get_new_thread() # Futtassa az ügynököt a szállal.
response = await agent.run("Hello, I am here to help you book travel. Where would you like to go?", thread=thread)

```

A szálat ezután sorosíthatod (serialize) későbbi felhasználás céljából:

```python
# Hozzon létre egy új szálat.
thread = agent.get_new_thread() 

# Futtassa az ügynököt a szállal.

response = await agent.run("Hello, how are you?", thread=thread) 

# Szerializálja a szálat tároláshoz.

serialized_thread = await thread.serialize() 

# Deszerializálja a szál állapotát a tárolóból való betöltés után.

resumed_thread = await agent.deserialize_thread(serialized_thread)
```

**Ügynök köztes szoftver (Middleware)**

Az ügynökök eszközökkel és LLM-ekkel lépnek kölcsönhatásba a felhasználói feladatok elvégzése érdekében. Bizonyos forgatókönyvekben közbe szeretnénk lépni vagy nyomon követni ezeket a kölcsönhatásokat. Az ügynök middleware lehetővé teszi számunkra ezt a következők révén:

*Funkció middleware*

Ez a middleware lehetővé teszi egy művelet végrehajtását az ügynök és egy általa hívott függvény/eszköz között. Ennek tipikus példája, amikor a függvényhívást szeretnéd naplózni.

A lenti kódban a `next` határozza meg, hogy a következő middleware-t vagy a tényleges függvényt kell-e meghívni.

```python
async def logging_function_middleware(
    context: FunctionInvocationContext,
    next: Callable[[FunctionInvocationContext], Awaitable[None]],
) -> None:
    """Function middleware that logs function execution."""
    # Előfeldolgozás: Naplózás a függvény végrehajtása előtt
    print(f"[Function] Calling {context.function.name}")

    # Tovább a következő middleware-hez vagy a függvény végrehajtásához
    await next(context)

    # Utófeldolgozás: Naplózás a függvény végrehajtása után
    print(f"[Function] {context.function.name} completed")
```

*Chat middleware*

Ez a middleware lehetővé teszi egy művelet végrehajtását vagy naplózását az ügynök és az LLM közötti kérések között.

Ez olyan fontos információkat tartalmaz, mint azok a `messages`, amelyeket az AI szolgáltatásnak küldenek.

```python
async def logging_chat_middleware(
    context: ChatContext,
    next: Callable[[ChatContext], Awaitable[None]],
) -> None:
    """Chat middleware that logs AI interactions."""
    # Előfeldolgozás: Naplózás az MI hívása előtt
    print(f"[Chat] Sending {len(context.messages)} messages to AI")

    # Tovább a következő köztes réteghez vagy MI-szolgáltatáshoz
    await next(context)

    # Utófeldolgozás: Naplózás az MI válasza után
    print("[Chat] AI response received")

```

**Ügynök memória**

Ahogy az `Agentic Memory` leckében tárgyaltuk, a memória fontos eleme annak, hogy az ügynök különböző kontextusokban működhessen. A MAF többféle memóriatípust kínál:

*Memória a memóriában (In-Memory Storage)*

Ez az alkalmazás futása során a szálakban tárolt memória.

```python
# Hozzon létre egy új szálat.
thread = agent.get_new_thread() # Futtassa az ügynököt a szálon.
response = await agent.run("Hello, I am here to help you book travel. Where would you like to go?", thread=thread)
```

*Perzisztens üzenetek (Persistent Messages)*

Ezt a memóriát a beszélgetési előzmények különböző munkamenetek közötti tárolására használják. A `chat_message_store_factory` segítségével definiálható:

```python
from agent_framework import ChatMessageStore

# Hozzon létre egy egyéni üzenettárolót
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

A megfigyelhetőség fontos a megbízható és karbantartható ügynöki rendszerek építéséhez. A MAF integrálja az OpenTelemetry-t, hogy jobb nyomkövetést és mérőszámokat biztosítson.

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

A MAF munkafolyamatokat kínál, amelyek előre definiált lépések egy feladat végrehajtásához, és ezekben a lépésekben AI ügynökök is szerepelhetnek.

A munkafolyamatok különböző összetevőkből állnak, amelyek jobb vezérlési folyamatot tesznek lehetővé. A munkafolyamatok emellett lehetővé teszik a **többügynökös orchestrationt** és a **pontmentést (checkpointing)** a munkafolyamat állapotainak mentéséhez.

Egy munkafolyamat magját az alábbi összetevők képezik:

**Végrehajtók (Executors)**

A végrehajtók bemeneti üzeneteket kapnak, elvégzik a nekik kiosztott feladatokat, majd kimeneti üzenetet állítanak elő. Ez előreviszi a munkafolyamatot a nagyobb feladat teljesítése felé. A végrehajtók lehetnek AI ügynökök vagy egyedi logikák.

**Élek (Edges)**

Az élek határozzák meg az üzenetek áramlását egy munkafolyamatban. Ezek lehetnek:

*Direkt élek* - Egyszerű egy-az-egy kapcsolatok a végrehajtók között:

```python
from agent_framework import WorkflowBuilder

builder = WorkflowBuilder()
builder.add_edge(source_executor, target_executor)
builder.set_start_executor(source_executor)
workflow = builder.build()
```

*Feltételes élek* - Akkor aktiválódnak, amikor egy meghatározott feltétel teljesül. Például, ha a szállodai szobák nem elérhetők, egy végrehajtó más lehetőségeket javasolhat.

*Switch-case élek* - Az üzeneteket különböző végrehajtókhoz irányítják meghatározott feltételek alapján. Például ha egy utazó ügyfélnek prioritási hozzáférése van, akkor a feladatait egy másik munkafolyamaton keresztül kezelik.

*Fan-out élek* - Egy üzenetet több célhoz küldenek.

*Fan-in élek* - Több üzenetet gyűjtenek össze különböző végrehajtóktól és egyetlen célhoz továbbítanak.

**Események**

A munkafolyamatok jobb megfigyelhetőségének biztosításához a MAF beépített eseményeket kínál a végrehajtás számára, többek között:

- `WorkflowStartedEvent`  - A munkafolyamat végrehajtása elkezdődik
- `WorkflowOutputEvent` - A munkafolyamat kimenetet hoz létre
- `WorkflowErrorEvent` - A munkafolyamat hibába ütközik
- `ExecutorInvokeEvent`  - A végrehajtó megkezdi a feldolgozást
- `ExecutorCompleteEvent`  -  A végrehajtó befejezi a feldolgozást
- `RequestInfoEvent` - Egy kérés kerül kiadásra

## Fejlett MAF minták

A fenti részek lefedik a Microsoft Agent Framework kulcsfogalmait. Ahogy egyre összetettebb ügynököket építesz, érdemes megfontolni az alábbi fejlett mintákat:

- **Middleware összefűzés**: Több middleware kezelő (naplózás, hitelesítés, rate-limiting) láncolása funkció- és chat-middleware használatával a finomhangolt vezérlés érdekében az ügynök viselkedésén.
- **Munkafolyamat pontmentés**: Munkafolyamat események és sorosítás használata hosszú futású ügynöki folyamatok mentésére és folytatására.
- **Dinamikus eszközválasztás**: RAG kombinálása az eszközleírásokon alapuló kereséssel a MAF eszközregisztrációjával, hogy lekérdezésenként csak a releváns eszközök jelenjenek meg.
- **Többügynökös átadás**: Munkafolyamat élek és feltételes irányítás használata a speciális ügynökök közötti átadások orchestration-jához.

## Kódminták 

A Microsoft Agent Framework kódmintái megtalálhatók ebben a tárolóban az `xx-python-agent-framework` és az `xx-dotnet-agent-framework` fájlok alatt.

## Van további kérdésed a Microsoft Agent Framework-kel kapcsolatban?

Csatlakozz a [Microsoft Foundry Discord](https://aka.ms/ai-agents/discord)-hoz, hogy találkozhass más tanulókkal, részt vehess office hour-okon és választ kapj az AI ügynökökkel kapcsolatos kérdéseidre.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
Felelősségkizárás:
Ezt a dokumentumot az AI fordítószolgáltatás, a [Co-op Translator](https://github.com/Azure/co-op-translator) használatával fordították. Bár törekszünk a pontosságra, kérjük, vegye figyelembe, hogy az automatikus fordítások hibákat vagy pontatlanságokat tartalmazhatnak. Az eredeti dokumentum anyanyelvű változatát tekintse hivatalos forrásnak. Fontos információk esetén professzionális, emberi fordítást javaslunk. Nem vállalunk felelősséget az e fordítás használatából eredő félreértésekért vagy helytelen értelmezésekért.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->