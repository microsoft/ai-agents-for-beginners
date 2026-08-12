[![Hogyan tervezzünk jó AI ügynököket](../../../translated_images/hu/lesson-4-thumbnail.546162853cb3daff.webp)](https://youtu.be/vieRiPRx-gI?si=cEZ8ApnT6Sus9rhn)

> _(A fenti képre kattintva megtekintheti a lecke videóját)_

# Eszközhasználati tervezési minta

Az eszközök érdekesek, mert lehetővé teszik az AI ügynökök számára, hogy szélesebb spektrumú képességekkel rendelkezzenek. Az ügynök ahelyett, hogy egy korlátozott cselekvéssorozatot hajtana végre, egy eszköz hozzáadásával különféle műveleteket tud végezni. Ebben a fejezetben megvizsgáljuk az Eszközhasználati tervezési mintát, amely leírja, hogyan használhatják az AI ügynökök a konkrét eszközöket céljaik elérésére.

## Bevezetés

Ebben a leckében a következő kérdésekre keressük a választ:

- Mi az eszközhasználati tervezési minta?
- Milyen alkalmazási területekre alkalmazható?
- Mely elemekre/építőkövekre van szükség a tervezési minta megvalósításához?
- Milyen különleges szempontokat kell figyelembe venni a megbízható AI ügynökök létrehozásához az eszközhasználati tervezési minta alkalmazásakor?

## Tanulási célok

A lecke elvégzése után képes lesz:

- Meghatározni az eszközhasználati tervezési mintát és célját.
- Azonosítani azokat az alkalmazási területeket, ahol a mintát alkalmazzák.
- Megérteni a tervezési minta megvalósításához szükséges kulcselemeket.
- Felismerni a megbízhatóság biztosításához szükséges megfontolásokat az AI ügynökök esetében ezen minta használatakor.

## Mi az eszközhasználati tervezési minta?

A **Tool Use Design Pattern** (eszközhasználati tervezési minta) arra fókuszál, hogy az LLM-ek képesek legyenek külső eszközökkel interakcióba lépni konkrét célok elérése érdekében. Az eszközök olyan kódok, amelyeket egy ügynök végrehajthat, hogy műveleteket hajtson végre. Egy eszköz lehet egyszerű függvény, például egy kalkulátor, vagy egy harmadik fél szolgáltatásának API hívása, például részvényárfolyam lekérdezése vagy időjárás-előrejelzés. Az AI ügynökök esetében az eszközöket úgy alakítják ki, hogy azokat az ügynökök **modell által generált függvényhívások** válaszaként tudják végrehajtani.

## Milyen alkalmazási területekre használható?

Az AI ügynökök eszközök segítségével képesek bonyolult feladatokat megoldani, információt lekérni vagy döntéseket hozni. Az eszközhasználati tervezési mintát jellemzően olyan helyzetekben alkalmazzák, ahol dinamikus interakció szükséges külső rendszerekkel, például adatbázisokkal, webszolgáltatásokkal vagy kódfordítókkal. Ez a képesség többféle esetben hasznos, például:

- **Dinamikus információ lekérés:** Az ügynökök külső API-kat vagy adatbázisokat kérdezhetnek le naprakész adatokért (pl. SQLite adatbázis lekérdezés adatelemzéshez, részvényárak vagy időjárási információk lekérése).
- **Kódvégrehajtás és értelmezés:** Az ügynökök kódot vagy szkripteket futtathatnak matematikai problémák megoldásához, jelentéskészítéshez vagy szimulációk végzéséhez.
- **Munkafolyamat automatizálás:** Ismétlődő vagy több lépéses munkafolyamatok automatizálása eszközök integrálásával, mint feladatütemezők, email szolgáltatások vagy adatok feldolgozási láncai.
- **Ügyfélszolgálat:** Az ügynökök CRM rendszerekkel, jegykezelő platformokkal vagy tudásbázisokkal interakcióba léphetnek a felhasználói kérdések megoldásához.
- **Tartalomkészítés és szerkesztés:** Az ügynökök olyan eszközöket használhatnak, mint a nyelvtani ellenőrzők, szövegösszefoglalók vagy tartalombiztonsági értékelők, hogy segítsenek a tartalomkészítésben.

## Mely elemekre/építőkövekre van szükség az eszközhasználati tervezési minta megvalósításához?

Ezek az építőelemek teszik lehetővé, hogy az AI ügynök széles feladatskálát végezzen el. Nézzük meg a Tool Use Design Pattern megvalósításához szükséges kulcselemeket:

- **Függvény/eszköz sémák**: A rendelkezésre álló eszközök részletes definíciói, beleértve a függvény nevét, célját, szükséges paramétereit és várható kimeneteit. Ezek a sémák segítik az LLM-et abban, hogy megértse, milyen eszközök elérhetők és hogyan kell érvényes kéréseket összeállítani.

- **Függvény végrehajtási logika**: Szabályozza, mikor és hogyan hívják meg az eszközöket a felhasználói szándék és a beszélgetési kontextus alapján. Ez tartalmazhat tervező modulokat, útválasztó mechanizmusokat vagy feltételes folyamatokat, amelyek dinamikusan döntenek az eszközhasználatról.

- **Üzenetkezelő rendszer**: Az alkotóelemek, amelyek felügyelik a beszélgetés menetét a felhasználói bemenetek, LLM válaszok, eszközhívások és azok kimenetei között.

- **Eszköz integrációs keretrendszer**: Infrastruktúra, amely összekapcsolja az ügynököt különféle eszközökkel, akár egyszerű függvényekről, akár összetett külső szolgáltatásokról legyen szó.

- **Hibakezelés és validáció**: Mechanizmusok az eszközvégrehajtás hibáinak kezelésére, a paraméterek érvényesítésére és váratlan válaszok kezelésére.

- **Állapotkezelés**: Követi a beszélgetési kontextust, korábbi eszközhasználatokat és tartós adatokat a konzisztencia érdekében többfordulós interakciók során.

Ezután nézzük meg részletesebben a függvény/eszköz hívást.
 
### Függvény/Eszköz hívás

A függvényhívás az elsődleges módja annak, hogy LLM-eket eszközökkel kapcsoljunk össze. Gyakran használjuk felváltva a „Function” és az „Tool” szavakat, mert a „függvények” (újrafelhasználható kódrészek) azok az eszközök, amelyeket az ügynökök feladatok elvégzéséhez használnak. Annak érdekében, hogy egy függvény kódját meghívhassuk, az LLM-nek össze kell vetnie a felhasználói kérést a függvény leírásával. Ehhez egy olyan sémát kell az LLM-nek elküldeni, amely tartalmazza az elérhető függvények leírásait. Az LLM kiválasztja a feladathoz legmegfelelőbb függvényt, majd visszaadja annak nevét és argumentumait. A kiválasztott függvényt meghívjuk, a válaszát visszaküldjük az LLM-nek, amely ezt felhasználva válaszol a felhasználó kérésére.

A fejlesztőknek, akik függvényhívást kívánnak megvalósítani ügynököknek, szükségük lesz:

1. Olyan LLM modellre, amely támogatja a függvényhívást
2. Egy sémára, amely tartalmazza a függvényleírásokat
3. Az egyes leírt függvények kódjára

Vegyük például az aktuális idő lekérését egy városban a következőképpen:

1. **Indítsunk el egy, a függvényhívást támogató LLM-et:**

    Nem minden modell támogatja a függvényhívást, így fontos ellenőrizni, hogy az Ön által használt LLM ezt tudja-e. Az <a href="https://learn.microsoft.com/azure/ai-services/openai/how-to/function-calling" target="_blank">Azure OpenAI</a> támogatja a függvényhívást. Kezdhetjük az OpenAI kliens inicializálásával az Azure OpenAI **Responses API**-jához (a stabil `/openai/v1/` végpont — nincs szükség `api_version`-re).

    ```python
    # Inicializálja az OpenAI klienst az Azure OpenAI (Responses API, v1 végpont) számára
    client = OpenAI(
        base_url=f"{os.environ['AZURE_OPENAI_ENDPOINT'].rstrip('/')}/openai/v1/",
        api_key=os.environ["AZURE_OPENAI_API_KEY"],
    )
    deployment_name = os.environ["AZURE_OPENAI_DEPLOYMENT"]
    ```

1. **Függvény séma létrehozása**:

    Ezután definiálunk egy JSON sémát, amely tartalmazza a függvény nevét, leírását, és a paraméterek nevét valamint azok leírását.
    Ezt a sémát átadjuk a korábban létrehozott kliensnek, amelyhez hozzáadjuk a felhasználói kérés, például a san franciscói idő lekérdezését. Fontos megjegyezni, hogy egy **eszközhívás** az, ami visszatér, **nem** a kérdés végleges válasza. Ahogyan korábban említettük, az LLM visszaadja a kiválasztott függvény nevét és a hozzá tartozó argumentumokat.

    ```python
    # A modell által olvasható függvényleírás (Responses API lapos eszközformátum)
    tools = [
        {
            "type": "function",
            "name": "get_current_time",
            "description": "Get the current time in a given location",
            "parameters": {
                "type": "object",
                "properties": {
                    "location": {
                        "type": "string",
                        "description": "The city name, e.g. San Francisco",
                    },
                },
                "required": ["location"],
            },
        }
    ]
    ```
   
    ```python
  
    # Kezdeti felhasználói üzenet
    messages = [{"role": "user", "content": "What's the current time in San Francisco"}]

    # Első API hívás: Kérd meg a modellt, hogy használja a függvényt
    response = client.responses.create(
        model=deployment_name,
        input=messages,
        tools=tools,
        tool_choice="auto",
        store=False,
    )

    # A Responses API a tool call-okat function_call elemekként adja vissza a response.output-ban.
    # Fűzd hozzá őket a beszélgetéshez, hogy a modell teljes kontextussal rendelkezzen a következő körben.
    messages += response.output

    print("Model's response:")
    print(response.output)
  
    ```

    ```bash
    Model's response:
    [ResponseFunctionToolCall(arguments='{"location":"San Francisco"}', call_id='call_pOsKdUlqvdyttYB67MOj434b', name='get_current_time', type='function_call')]
    ```
  
1. **A függvény kódja a feladat végrehajtásához:**

    Miután az LLM kiválasztotta, hogy melyik függvényt kell futtatni, a végrehajtó kódot meg kell írni és futtatni kell.
    Pythonban megvalósíthatjuk az aktuális idő lekérését. Szükséges lesz az is, hogy kódot írjunk az válaszüzenetből a név és argumentumok kinyeréséhez a végső eredményhez.

    ```python
      def get_current_time(location):
        """Get the current time for a given location"""
        print(f"get_current_time called with location: {location}")  
        location_lower = location.lower()
        
        for key, timezone in TIMEZONE_DATA.items():
            if key in location_lower:
                print(f"Timezone found for {key}")  
                current_time = datetime.now(ZoneInfo(timezone)).strftime("%I:%M %p")
                return json.dumps({
                    "location": location,
                    "current_time": current_time
                })
      
        print(f"No timezone data found for {location_lower}")  
        return json.dumps({"location": location, "current_time": "unknown"})
    ```

     ```python
    # Függvényhívások kezelése
    tool_calls = [item for item in response.output if item.type == "function_call"]
    if tool_calls:
        for tool_call in tool_calls:
            if tool_call.name == "get_current_time":

                function_args = json.loads(tool_call.arguments)

                time_response = get_current_time(
                    location=function_args.get("location")
                )

                # A művelet eredményét function_call_output elemként visszaadni
                messages.append({
                    "type": "function_call_output",
                    "call_id": tool_call.call_id,
                    "output": time_response,
                })
    else:
        print("No tool calls were made by the model.")

    # Második API hívás: A modell végső válaszának lekérése
    final_response = client.responses.create(
        model=deployment_name,
        input=messages,
        tools=tools,
        store=False,
    )

    return final_response.output_text
     ```

     ```bash
      get_current_time called with location: San Francisco
      Timezone found for san francisco
      The current time in San Francisco is 09:24 AM.
     ```

A függvényhívás áll a legtöbb, ha nem az összes ügynök eszközhasználati tervezési minta központjában, azonban a megvalósítása teljesen saját kezűleg néha kihívást jelenthet.
Ahogyan a [2. leckéből](../../../02-explore-agentic-frameworks) megtanultuk, az ügynök keretrendszerek előre elkészített építőelemekkel segítik az eszközhasználat megvalósítását.
 
## Eszközhasználat példák ügynök keretrendszerekkel

Íme néhány példa arra, hogyan valósítható meg az eszközhasználati tervezési minta különféle ügynök keretrendszerek segítségével:

### Microsoft Agent Framework

A <a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Microsoft Agent Framework</a> egy nyílt forráskódú AI keretrendszer AI ügynökök építéséhez. Egyszerűsíti a függvényhívás használatát, lehetővé téve, hogy eszközöket Python függvényként definiáljunk a `@tool` dekorátorral. A keretrendszer kezeli a modell és a kód közötti kommunikáció oda-vissza folyamatát. Emellett előre elkészített eszközökhöz biztosít hozzáférést, mint például a Fájlkutató és Kód-interpreter a `FoundryChatClient` segítségével.

A következő ábra szemlélteti a függvényhívás folyamatát a Microsoft Agent Framework használatával:

![függvényhívás](../../../translated_images/hu/functioncalling-diagram.a84006fc287f6014.webp)

A Microsoft Agent Frameworkben az eszközök dekorált függvényekként vannak definiálva. Az előzőleg látott `get_current_time` függvényt eszközzé alakíthatjuk a `@tool` dekorátor segítségével. A keretrendszer automatikusan szériázza a függvényt és paramétereit, így elkészíti a sémát, amit az LLM-nek küld.

```python
import os
from agent_framework import tool
from agent_framework.foundry import FoundryChatClient
from azure.identity import AzureCliCredential

@tool(approval_mode="never_require")
def get_current_time(location: str) -> str:
    """Get the current time for a given location"""
    ...

# Kliens létrehozása
provider = FoundryChatClient(
    project_endpoint=os.environ["AZURE_AI_PROJECT_ENDPOINT"],
    model=os.environ["AZURE_AI_MODEL_DEPLOYMENT_NAME"],
    credential=AzureCliCredential(),
)

# Agent létrehozása és futtatása az eszközzel
agent = provider.as_agent(name="TimeAgent", instructions="Use available tools to answer questions.", tools=get_current_time)
response = await agent.run("What time is it?")
```
  
### Microsoft Foundry Agent Service

A <a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Microsoft Foundry Agent Service</a> egy újabb ügynök keretrendszer, amelyet úgy terveztek, hogy a fejlesztők biztonságosan építhessenek, telepíthessenek és méretezzenek nagy teljesítményű, bővíthető AI ügynököket anélkül, hogy az alapvető számítási és tárhelyi erőforrásokat kezelniük kellene. Különösen hasznos vállalati alkalmazásokhoz, mivel teljesen felügyelt szolgáltatás vállalati szintű biztonsággal.

Ha összehasonlítjuk a közvetlen LLM API fejlesztéssel, a Microsoft Foundry Agent Service néhány előnyt kínál, többek között:

- Automatikus eszközhívás – nincs szükség arra, hogy az eszközhívást magunk dolgozzuk fel, meghívjuk az eszközt és kezeljük a választ; mindez most a szerveroldalon történik
- Biztonságos adatkezelés – ahelyett, hogy saját beszélgetési állapotot kezelne, a szálakra támaszkodhat, amelyek az összes szükséges információt tárolják
- Kész eszközök – Eszközök, amelyekkel adatforrásaival léphet interakcióba, például Bing, Azure AI Search és Azure Functions.

A Microsoft Foundry Agent Service-ben elérhető eszközök két kategóriába sorolhatók:

1. Tudás eszközök:
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/bing-grounding?tabs=python&pivots=overview" target="_blank">Bing kereséssel való horgonyzás</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/file-search?tabs=python&pivots=overview" target="_blank">Fájlkutató</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-ai-search?tabs=azurecli%2Cpython&pivots=overview-azure-ai-search" target="_blank">Azure AI Search</a>

2. Műveleti eszközök:
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/function-calling?tabs=python&pivots=overview" target="_blank">Függvényhívás</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/code-interpreter?tabs=python&pivots=overview" target="_blank">Kód értelmező</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/openapi-spec?tabs=python&pivots=overview" target="_blank">OpenAPI által definiált eszközök</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-functions?pivots=overview" target="_blank">Azure Functions</a>

Az Agent Service lehetővé teszi ezek az eszközök együttes, `toolset`-ként való használatát. Emellett használja a `szálakat`, amelyek nyomon követik egy adott beszélgetés üzenettörténetét.

Képzeljük el, hogy egy Contoso nevű cégnél értékesítési ügynök vagy. Olyan beszélgető ügynököt szeretnél fejleszteni, amely válaszolni tud értékesítési adatokról szóló kérdésekre.

A következő kép azt szemlélteti, hogyan használhatod a Microsoft Foundry Agent Service-t értékesítési adatok elemzésére:

![Agentic Service működés közben](../../../translated_images/hu/agent-service-in-action.34fb465c9a84659e.webp)

Ezek bármelyikének használatához az Agent Service-szel létrehozhatunk egy klienst, és definiálhatunk egy eszközt vagy eszközkészletet. Gyakorlati megvalósításhoz a következő Python kódot használhatjuk. Az LLM meg tudja nézni az eszközkészletet, és eldöntheti, hogy a felhasználó által létrehozott `fetch_sales_data_using_sqlite_query` függvényt vagy az előre elkészített Code Interpreter-t használja a felhasználói kérés alapján.

```python 
import os
from azure.ai.projects import AIProjectClient
from azure.identity import DefaultAzureCredential
from fetch_sales_data_functions import fetch_sales_data_using_sqlite_query # fetch_sales_data_using_sqlite_query függvény, amely megtalálható a fetch_sales_data_functions.py fájlban.
from azure.ai.projects.models import ToolSet, FunctionTool, CodeInterpreterTool

project_client = AIProjectClient.from_connection_string(
    credential=DefaultAzureCredential(),
    conn_str=os.environ["PROJECT_CONNECTION_STRING"],
)

# Eszközkészlet inicializálása
toolset = ToolSet()

# Függvényhívó ügynök inicializálása a fetch_sales_data_using_sqlite_query függvénnyel és hozzáadása az eszközkészlethez
fetch_data_function = FunctionTool(fetch_sales_data_using_sqlite_query)
toolset.add(fetch_data_function)

# Kódértelmező eszköz inicializálása és hozzáadása az eszközkészlethez.
code_interpreter = CodeInterpreterTool()toolset.add(code_interpreter)

agent = project_client.agents.create_agent(
    model="gpt-5-mini", name="my-agent", instructions="You are helpful agent", 
    toolset=toolset
)
```

## Milyen különleges megfontolások szükségesek az eszközhasználati tervezési minta megbízható AI ügynökök építéséhez?

Az LLM-ek által dinamikusan generált SQL esetében gyakori aggály a biztonság, különösen az SQL injekció vagy rosszindulatú műveletek kockázata, például az adatbázis törlése vagy manipulálása. Bár ezek az aggodalmak jogosak, hatékonyan mérsékelhetőek az adatbázis-hozzáférési jogosultságok megfelelő beállításával. A legtöbb adatbázis esetén ez azt jelenti, hogy az adatbázist csak olvasható módban konfiguráljuk. Olyan adatbázis szolgáltatásoknál, mint a PostgreSQL vagy Azure SQL, az alkalmazásnak olvasható (SELECT) jogosultságot kell kapnia.

Az alkalmazás biztonságos környezetben futtatása tovább növeli a védelmet. Vállalati helyzetekben az adatok rendszerint kivonásra és átalakításra kerülnek az operációs rendszerekből, egy olvasható adatbázisba vagy adattárházba egy felhasználóbarát sémával. Ez a megközelítés biztosítja az adatok biztonságát, a teljesítmény és hozzáférhetőség optimalizáltságát, valamint korlátozott, csak olvasható hozzáférést az alkalmazás számára.

## Kódemminta

- Python: [Agent Framework](./code_samples/04-python-agent-framework.ipynb)
- .NET: [Agent Framework](./code_samples/04-dotnet-agent-framework.md)

## Van még kérdése az eszközhasználati tervezési mintákról?

Csatlakozzon a [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D) szerverhez, hogy találkozzon más tanulókkal, vegyen részt nyílt órákon, és kérdéseit feltegye AI ügynökökkel kapcsolatban.

## További források

- <a href="https://microsoft.github.io/build-your-first-agent-with-azure-ai-agent-service-workshop/" target="_blank">Azure AI Agents Service Workshop</a>
- <a href="https://github.com/Azure-Samples/contoso-creative-writer/tree/main/docs/workshop" target="_blank">Contoso Creative Writer többügynökös Workshop</a>
- <a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Microsoft Agent Framework áttekintés</a>


## Az Ügynök Gyorsellenőrzése (Opcionális)

Miután megtanultad, hogyan telepíts ügynököket a [16. leckében](../16-deploying-scalable-agents/README.md), gyorsan tesztelheted ennek a leckének a `TravelToolAgent` ügynökét (még mindig hívja az eszközeit és válaszol?) a [`tests/lesson-04-smoke-tests.json`](../../../tests/lesson-04-smoke-tests.json) használatával. Lásd a [`tests/README.md`](../tests/README.md) fájlt a futtatás módjáról.

## Előző lecke

[Az Ügynöki Tervezési Minták Megértése](../03-agentic-design-patterns/README.md)

## Következő lecke

[Ügynöki RAG](../05-agentic-rag/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Jogi nyilatkozat**:
Ez a dokumentum az AI fordítási szolgáltatás, a [Co-op Translator](https://github.com/Azure/co-op-translator) segítségével készült. Bár az pontosságra törekszünk, kérjük, vegye figyelembe, hogy az automatikus fordítások hibákat vagy pontatlanságokat tartalmazhatnak. Az eredeti dokumentum az anyanyelvén tekintendő hiteles forrásnak. Fontos információk esetén professzionális emberi fordítást javasolunk. Nem vállalunk felelősséget semmilyen félreértésért vagy téves értelmezésért, amely ebből a fordításból ered.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->