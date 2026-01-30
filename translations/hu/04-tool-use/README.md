[![Hogyan tervezzünk jó AI ügynököket](../../../translated_images/hu/lesson-4-thumbnail.546162853cb3daff.webp)](https://youtu.be/vieRiPRx-gI?si=cEZ8ApnT6Sus9rhn)

> _(Kattints a fenti képre a lecke videójának megtekintéséhez)_

# Eszközhasználat tervezési minta

Az eszközök érdekessége, hogy lehetővé teszik az AI ügynökök számára a képességek szélesebb skáláját. Ahelyett, hogy az ügynöknek egy korlátozott műveletkészlete lenne, egy eszköz hozzáadásával az ügynök már szélesebb körű műveleteket képes végrehajtani. Ebben a fejezetben megvizsgáljuk az Eszközhasználat tervezési mintát, amely leírja, hogyan használhatják az AI ügynökök a specifikus eszközöket céljaik eléréséhez.

## Bevezetés

Ebben a leckében a következő kérdésekre keressük a választ:

- Mi az eszközhasználat tervezési minta?
- Milyen felhasználási esetekre alkalmazható?
- Mely elemek/építőelemek szükségesek a minta megvalósításához?
- Milyen különös szempontokat kell figyelembe venni az Eszközhasználat tervezési minta megbízható AI ügynökök építéséhez?

## Tanulási célok

A lecke elvégzése után képes leszel:

- Meghatározni az Eszközhasználat tervezési mintát és annak célját.
- Azonosítani azokat a felhasználási eseteket, ahol ez a minta alkalmazható.
- Megérteni a minta megvalósításához szükséges kulcselemeket.
- Felismerni a megbízhatóság biztosításának szempontjait az AI ügynökök esetében, amelyek ezt a mintát használják.

## Mi az Eszközhasználat tervezési minta?

Az **Eszközhasználat tervezési minta** arra összpontosít, hogy a nagy nyelvi modellek (LLM-ek) képesek legyenek külső eszközökkel együttműködni meghatározott célok elérése érdekében. Az eszközök olyan kódok, amelyeket az ügynök végrehajthat bizonyos műveletek elvégzésére. Egy eszköz lehet egyszerű függvény, például egy számológép, vagy egy harmadik fél szolgáltatásának API hívása, például árfolyam vagy időjárás lekérdezése. AI ügynökök kontextusában az eszközöket úgy tervezik, hogy az ügynökök modell által generált függvényhívások válaszaként hajtsák végre.

## Milyen felhasználási esetekre alkalmazható?

Az AI ügynökök eszközöket használhatnak bonyolult feladatok elvégzésére, információk lekérésére, vagy döntéshozatalra. Az eszközhasználati tervezési mintát gyakran alkalmazzák olyan forgatókönyvekben, ahol dinamikus interakció szükséges külső rendszerekkel, mint adatbázisok, webszolgáltatások vagy kódértelmezők. Ez a képesség számos különböző felhasználási esetben hasznos, például:

- **Dinamikus információlekérés:** Az ügynökök lekérdezhetnek külső API-kat vagy adatbázisokat friss adatértékekért (például SQLite adatbázis lekérdezés adat elemzéshez, árfolyam vagy időjárás információk lekérése).
- **Kódvégrehajtás és értelmezés:** Az ügynökök kódot vagy scriptet hajthatnak végre matematikai problémák megoldásához, jelentések készítéséhez vagy szimulációk lebonyolításához.
- **Munkafolyamat automatizálás:** Ismétlődő vagy többlépéses munkafolyamatok automatizálása eszközök integrálásával, például feladatütemezők, e-mail szolgáltatások vagy adatcsővezetékek használatával.
- **Ügyféltámogatás:** Az ügynökök kapcsolatba léphetnek CRM rendszerekkel, jegykezelő platformokkal vagy tudásbázisokkal, hogy megválaszolják a felhasználói kérdéseket.
- **Tartalomgenerálás és szerkesztés:** Az ügynökök eszközöket használhatnak, mint például nyelvtani ellenőrzők, szövegösszefoglalók vagy tartalombiztonsági értékelők, hogy segítsék a tartalomkészítést.

## Mely elemek/építőelemek szükségesek az eszközhasználat tervezési minta megvalósításához?

Ezek az építőelemek teszik lehetővé az AI ügynök számára, hogy széles körű feladatokat hajtson végre. Nézzük meg a kulcsfontosságú elemeket az Eszközhasználat tervezési minta megvalósításához:

- **Függvény/Eszköz sémák**: Részletes definíciók az elérhető eszközökről, beleértve a függvény nevét, célját, szükséges paramétereket és a várt kimeneteket. Ezek a sémák lehetővé teszik az LLM számára, hogy megértse, mely eszközök állnak rendelkezésre és hogyan kell érvényes kéréseket összeállítani.

- **Függvény-végrehajtási logika**: Szabályozza, hogy mikor és hogyan hívják meg az eszközöket a felhasználó szándéka és a beszélgetés kontextusa alapján. Ez tartalmazhat tervező modulokat, útválasztó mechanizmusokat vagy feltételes folyamatokat, amelyek dinamikusan határozzák meg az eszközhasználatot.

- **Üzenetkezelő rendszer**: Olyan komponensek, amelyek kezelik a beszélgetési folyamatot a felhasználói bemenetek, LLM válaszok, eszközhívások és eszközválaszok között.

- **Eszközintegrációs keretrendszer**: Infrastruktúra, amely összekapcsolja az ügynököt különféle eszközökkel, legyenek azok egyszerű függvények vagy összetett külső szolgáltatások.

- **Hibakezelés és érvényesítés**: Mechanizmusok az eszközvégrehajtási hibák kezelésére, paraméterek érvényesítésére és váratlan válaszok kezelésére.

- **Állapotkezelés**: Követi a beszélgetés kontextusát, a korábbi eszközös interakciókat és tartós adatokat a többfordulós interakciók konzisztenciájának biztosításához.

Most nézzük meg részletesebben a Függvény/Eszköz hívást.

### Függvény/Eszköz hívás

A függvényhívás az elsődleges módja annak, hogy a Nagy Nyelvi Modelleket (LLM-eket) eszközökkel együttműködve használjuk. Gyakran látjuk a „Függvény” és „Eszköz” kifejezéseket felcserélhetően, mert a „függvények” (újrahasználható kódrészek) az „eszközök”, amelyeket az ügynökök használnak a feladatok végrehajtására. Ahhoz, hogy egy függvény kódját meghívják, az LLM-nek össze kell hasonlítania a felhasználó kérését a függvény leírásával. Ehhez egy olyan séma kerül elküldésre az LLM-nek, amely tartalmazza az összes elérhető függvény leírását. Az LLM kiválasztja a legmegfelelőbb függvényt a feladathoz, és visszaküldi a nevét és az argumentumait. A kiválasztott függvényt meghívják, a válasza visszakerül az LLM-hez, amely az információk alapján válaszol a felhasználó kérésére.

A fejlesztőknek, akik függvényhívást akarnak megvalósítani ügynökök számára, szükségük lesz:

1. Egy olyan LLM modellre, amely támogatja a függvényhívást
2. Egy sémára, amely tartalmazza a függvények leírásait
3. A leírt függvények kódjára

Vegyük az aktuális idő lekérésének példáját egy városban a szemléltetéshez:

1. **Indítsunk el egy LLM-et, amely támogatja a függvényhívást:**

    Nem minden modell támogatja a függvényhívást, ezért fontos ellenőrizni, hogy a használt LLM igen. Az <a href="https://learn.microsoft.com/azure/ai-services/openai/how-to/function-calling" target="_blank">Azure OpenAI</a> támogatja a függvényhívást. Kezdhetünk az Azure OpenAI kliens inicializálásával.

    ```python
    # Inicializálja az Azure OpenAI klienset
    client = AzureOpenAI(
        azure_endpoint = os.getenv("AZURE_OPENAI_ENDPOINT"), 
        api_key=os.getenv("AZURE_OPENAI_API_KEY"),  
        api_version="2024-05-01-preview"
    )
    ```

1. **Hozzunk létre egy függvénysémát**:

    Ezután definiálunk egy JSON sémát, amely tartalmazza a függvény nevét, a függvény leírását és a paraméterek nevét, leírását.
    Ezt a sémát aztán átadjuk a korábban létrehozott kliensnek, együtt a felhasználói kéréssel, miszerint San Francisco aktuális idejére kíváncsiak vagyunk. Fontos megjegyezni, hogy ez egy **eszköz hívás** eredménye, **nem** a végső válasz a kérdésre. Amint korábban említettük, az LLM visszaküldi a feladathoz kiválasztott függvény nevét és az argumentumokat.

    ```python
    # Függvényleírás a modell számára olvasásra
    tools = [
        {
            "type": "function",
            "function": {
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
        }
    ]
    ```
   
    ```python
  
    # Kezdeti felhasználói üzenet
    messages = [{"role": "user", "content": "What's the current time in San Francisco"}] 
  
    # Első API hívás: Kérje meg a modellt, hogy használja a függvényt
      response = client.chat.completions.create(
          model=deployment_name,
          messages=messages,
          tools=tools,
          tool_choice="auto",
      )
  
      # Feldolgozza a modell válaszát
      response_message = response.choices[0].message
      messages.append(response_message)
  
      print("Model's response:")  

      print(response_message)
  
    ```

    ```bash
    Model's response:
    ChatCompletionMessage(content=None, role='assistant', function_call=None, tool_calls=[ChatCompletionMessageToolCall(id='call_pOsKdUlqvdyttYB67MOj434b', function=Function(arguments='{"location":"San Francisco"}', name='get_current_time'), type='function')])
    ```
  
1. **A feladat végrehajtásához szükséges függvénykód:**

    Miután az LLM kiválasztotta, hogy melyik függvényt kell futtatni, a végrehajtó kódot meg kell valósítani és futtatni kell.
    Pythonban megvalósíthatjuk az aktuális idő lekéréséhez szükséges kódot. Emellett szükséges lesz a válaszüzenetből kinyerni a függvény nevét és argumentumait a végső eredményhez.

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
      if response_message.tool_calls:
          for tool_call in response_message.tool_calls:
              if tool_call.function.name == "get_current_time":
     
                  function_args = json.loads(tool_call.function.arguments)
     
                  time_response = get_current_time(
                      location=function_args.get("location")
                  )
     
                  messages.append({
                      "tool_call_id": tool_call.id,
                      "role": "tool",
                      "name": "get_current_time",
                      "content": time_response,
                  })
      else:
          print("No tool calls were made by the model.")  
  
      # Második API hívás: A modell végső válaszának lekérése
      final_response = client.chat.completions.create(
          model=deployment_name,
          messages=messages,
      )
  
      return final_response.choices[0].message.content
     ```

     ```bash
      get_current_time called with location: San Francisco
      Timezone found for san francisco
      The current time in San Francisco is 09:24 AM.
     ```

A függvényhívás a legtöbb, ha nem az összes ügynökös eszközhasználati minta központi eleme, azonban a kézi megvalósítása néha kihívást jelenthet.
Ahogy a [2. leckében](../../../02-explore-agentic-frameworks) tanultuk, az ügynökös keretrendszerek előre elkészített építőelemeket kínálnak az eszközhasználat megvalósításához.
 
## Példák eszközhasználatra ügynökös keretrendszerekkel

Íme néhány példa arra, hogyan valósítható meg az Eszközhasználat tervezési minta különféle ügynökös keretrendszerek használatával:

### Semantic Kernel

<a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">A Semantic Kernel</a> egy nyílt forráskódú AI keretrendszer .NET, Python és Java fejlesztők számára, akik nagy nyelvi modellekkel dolgoznak. Egyszerűsíti a függvényhívás folyamatát azáltal, hogy automatikusan leírja a függvényeidet és azok paramétereit a modellnek egy <a href="https://learn.microsoft.com/semantic-kernel/concepts/ai-services/chat-completion/function-calling/?pivots=programming-language-python#1-serializing-the-functions" target="_blank">szerializálás</a> nevű folyamaton keresztül. Kezeli továbbá a kommunikáció oda-vissza menetét a modell és a kód között. Egy további előnye annak, hogy Semantic Kernel ügynökös keretrendszert használunk, hogy előre elkészített eszközökhöz férhetünk hozzá, mint például a <a href="https://github.com/microsoft/semantic-kernel/blob/main/python/samples/getting_started_with_agents/openai_assistant/step4_assistant_tool_file_search.py" target="_blank">Fájlkereső</a> és <a href="https://github.com/microsoft/semantic-kernel/blob/main/python/samples/getting_started_with_agents/openai_assistant/step3_assistant_tool_code_interpreter.py" target="_blank">Kódértelmező</a>.

A következő ábra szemlélteti a függvényhívás folyamatát a Semantic Kernel használatával:

![function calling](../../../translated_images/hu/functioncalling-diagram.a84006fc287f6014.webp)

A Semantic Kernelben a függvényeket/eszközöket <a href="https://learn.microsoft.com/semantic-kernel/concepts/plugins/?pivots=programming-language-python" target="_blank">bővítményeknek</a> hívják. Az előbb látott `get_current_time` függvényt egy osztállyá alakíthatjuk, amely tartalmazza a függvényt, és ebből bővítményt készítünk. Importálhatjuk a `kernel_function` dekorátort is, amely a függvény leírását fogadja be. Amikor létrehozunk egy kernelet a GetCurrentTimePlugin-nel, az automatikusan szerializálja a függvényt és paramétereit, így létrehozva a sémát, amelyet a modellnek továbbítunk.

```python
from semantic_kernel.functions import kernel_function

class GetCurrentTimePlugin:
    async def __init__(self, location):
        self.location = location

    @kernel_function(
        description="Get the current time for a given location"
    )
    def get_current_time(location: str = ""):
        ...

```

```python 
from semantic_kernel import Kernel

# Hozd létre a magot
kernel = Kernel()

# Hozd létre a bővítményt
get_current_time_plugin = GetCurrentTimePlugin(location)

# Add hozzá a bővítményt a maghoz
kernel.add_plugin(get_current_time_plugin)
```
  
### Azure AI Agent Service

<a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Az Azure AI Agent Service</a> egy újabb ügynökös keretrendszer, amely arra szolgál, hogy a fejlesztők biztonságosan, könnyen fejleszthessenek, telepíthessenek és méretezzenek magas színvonalú, bővíthető AI ügynököket anélkül, hogy az alapvető számítási és tárhely erőforrásokat kezelniük kellene. Különösen hasznos vállalati alkalmazások esetén, mivel egy teljesen menedzselt szolgáltatás és vállalati szintű biztonságot nyújt.

Az LLM API közvetlen használatához képest az Azure AI Agent Service a következő előnyöket kínálja:

- Automatikus eszközhívás – nem kell maga parse-olni az eszköz hívást, meghívni az eszközt és kezelni a választ; mindez a szerver oldalon történik
- Biztonságosan kezelt adatok – ahelyett, hogy saját beszélgetési állapotot kezelne, a szálakra támaszkodhat az összes szükséges információ tárolásához
- Használatra kész eszközök – eszközök, amelyekkel adatforrásokkal léphetünk kapcsolatba, mint például Bing, Azure AI Search és Azure Functions.

Az Azure AI Agent Service-ben elérhető eszközök két kategóriába sorolhatók:

1. Tudás Eszközök:
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/bing-grounding?tabs=python&pivots=overview" target="_blank">Grounding a Bing Keresővel</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/file-search?tabs=python&pivots=overview" target="_blank">Fájlkereső</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-ai-search?tabs=azurecli%2Cpython&pivots=overview-azure-ai-search" target="_blank">Azure AI Search</a>

2. Műveleti Eszközök:
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/function-calling?tabs=python&pivots=overview" target="_blank">Függvényhívás</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/code-interpreter?tabs=python&pivots=overview" target="_blank">Kódértelmező</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/openapi-spec?tabs=python&pivots=overview" target="_blank">OpenAPI által definiált eszközök</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-functions?pivots=overview" target="_blank">Azure Functions</a>

Az Agent Service lehetővé teszi ezek együttes használatát, mint `eszközkészlet` (toolset). Emellett `szálakat` is használ, amelyek nyomon követik az adott beszélgetés üzenet előzményeit.

Képzeld el, hogy egy Contoso nevű cég értékesítési ügynöke vagy. Beszélgető ügynököt szeretnél fejleszteni, amely képes válaszolni az értékesítési adataiddal kapcsolatos kérdésekre.

A következő kép szemlélteti, hogyan lehet az Azure AI Agent Service-t használni az értékesítési adatok elemzésére:

![Agentic Service In Action](../../../translated_images/hu/agent-service-in-action.34fb465c9a84659e.webp)

Az eszközök használatához a szolgáltatással létrehozhatunk egy klienst és definiálhatunk egy eszközt vagy eszközkészletet. Ennek gyakorlati megvalósítására az alábbi Python kód használható. Az LLM megvizsgálja az eszközkészletet, és eldönti, hogy használja-e a felhasználó által létrehozott `fetch_sales_data_using_sqlite_query` függvényt vagy az előre elkészített Kódértelmezőt a felhasználói kérés alapján.

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
code_interpreter = code_interpreter = CodeInterpreterTool()
toolset.add(code_interpreter)

agent = project_client.agents.create_agent(
    model="gpt-4o-mini", name="my-agent", instructions="You are helpful agent", 
    toolset=toolset
)
```

## Milyen különleges szempontokat kell figyelembe venni az Eszközhasználat tervezési minta alkalmazásánál megbízható AI ügynökök építéséhez?

Az LLM-ek által dinamikusan generált SQL-lel kapcsolatban gyakori aggodalom a biztonság, különösen az SQL injekció vagy rosszindulatú műveletek, mint az adatbázis törlése vagy manipulálása. Bár ezek az aggodalmak jogosak, hatékonyan mérsékelhetők az adatbázishoz való hozzáférési engedélyek megfelelő konfigurálásával. A legtöbb adatbázis esetén ez az adatbázis csak olvasható (read-only) beállítását jelenti. Olyan adatbázis szolgáltatásoknál mint a PostgreSQL vagy az Azure SQL, az alkalmazásnak olvasási (SELECT) szerepkört kell kapnia.
Az alkalmazás futtatása biztonságos környezetben további védelmet nyújt. Vállalati környezetekben az adatok jellemzően az operatív rendszerekből vannak kinyerve és átalakítva egy csak olvasható adatbázisba vagy adattárházba, amely felhasználóbarát sémával rendelkezik. Ez a megközelítés biztosítja, hogy az adatok biztonságosak, teljesítmény és hozzáférhetőség szempontjából optimalizáltak, valamint az alkalmazás korlátozott, csak olvasható hozzáféréssel rendelkezik.

## Mintakódok

- Python: [Agent Framework](./code_samples/04-python-agent-framework.ipynb)
- .NET: [Agent Framework](./code_samples/04-dotnet-agent-framework.md)

## További kérdése van az eszközhasználati tervezési mintákkal kapcsolatban?

Csatlakozzon az [Azure AI Foundry Discord](https://aka.ms/ai-agents/discord) szerveréhez, hogy találkozhasson más tanulókkal, részt vegyen ügyfélszolgálati órákon és megválaszoltassa AI Agentekkel kapcsolatos kérdéseit.

## További források

- <a href="https://microsoft.github.io/build-your-first-agent-with-azure-ai-agent-service-workshop/" target="_blank">Azure AI Agents Service Workshop</a>
- <a href="https://github.com/Azure-Samples/contoso-creative-writer/tree/main/docs/workshop" target="_blank">Contoso Creative Writer Multi-Agent Workshop</a>
- <a href="https://learn.microsoft.com/semantic-kernel/concepts/ai-services/chat-completion/function-calling/?pivots=programming-language-python#1-serializing-the-functions" target="_blank">Semantic Kernel Function Calling Tutorial</a>
- <a href="https://github.com/microsoft/semantic-kernel/blob/main/python/samples/getting_started_with_agents/openai_assistant/step3_assistant_tool_code_interpreter.py" target="_blank">Semantic Kernel Kódértelmező</a>
- <a href="https://microsoft.github.io/autogen/dev/user-guide/core-user-guide/components/tools.html" target="_blank">Autogen Eszközök</a>

## Előző lecke

[Agentikus tervezési minták megértése](../03-agentic-design-patterns/README.md)

## Következő lecke

[Agentikus RAG](../05-agentic-rag/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Nyilatkozat**:
Ez a dokumentum az AI fordító szolgáltatás, a [Co-op Translator](https://github.com/Azure/co-op-translator) segítségével készült. Bár a pontosságra törekszünk, kérjük, vegye figyelembe, hogy az automatikus fordítás hibákat vagy pontatlanságokat tartalmazhat. Az eredeti dokumentum az adott nyelven tekintendő hiteles forrásnak. Kritikus információk esetén szakmai emberi fordítást javaslunk. Nem vállalunk felelősséget a fordítás használatából eredő félreértésekért vagy helytelen értelmezésekért.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->