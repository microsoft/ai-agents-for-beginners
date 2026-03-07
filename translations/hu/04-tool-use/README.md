[![Hogyan tervezzünk jó AI-ügynököket](../../../translated_images/hu/lesson-4-thumbnail.546162853cb3daff.webp)](https://youtu.be/vieRiPRx-gI?si=cEZ8ApnT6Sus9rhn)

> _(Kattintson a fenti képre a lecke videójának megtekintéséhez)_

# Eszközhasználati tervezési minta

Az eszközök azért érdekesek, mert lehetővé teszik, hogy az AI-ügynökök szélesebb körű képességekkel rendelkezzenek. Ahelyett, hogy az ügynöknek korlátozott készletű műveletei lennének, egy eszköz hozzáadásával az ügynök most már sokféle műveletet képes végrehajtani. Ebben a fejezetben az Eszközhasználati tervezési mintát vizsgáljuk, amely leírja, hogyan használhatnak az AI-ügynökök konkrét eszközöket céljaik eléréséhez.

## Bevezetés

Ebben a leckében a következő kérdésekre keressük a választ:

- Mi az eszközhasználati tervezési minta?
- Milyen használati esetekre alkalmazható?
- Mely elemek/építőkockák szükségesek a minta megvalósításához?
- Milyen különleges megfontolások szükségesek az Eszközhasználati tervezési minta alkalmazásához megbízható AI-ügynökök építésekor?

## Tanulási célok

A lecke elvégzése után képes lesz:

- Definiálni az Eszközhasználati tervezési mintát és annak célját.
- Azonosítani azokat a használati eseteket, ahol az Eszközhasználati tervezési minta alkalmazható.
- Megérteni a minta megvalósításához szükséges kulcselemeket.
- Felismerni a megbízhatóság biztosításához szükséges megfontolásokat olyan AI-ügynökök esetén, amelyek ezt a mintát használják.

## Mi az eszközhasználati tervezési minta?

A **Eszközhasználati tervezési minta** az LLM-eknek az a képessége, hogy külső eszközökkel lépjenek interakcióba konkrét célok elérése érdekében. Az eszközök olyan kódok, amelyeket egy ügynök végrehajthat műveletek elvégzésére. Egy eszköz lehet egy egyszerű függvény, például egy számológép, vagy egy harmadik féltől származó szolgáltatás API-hívása, például részvényár-keresés vagy időjárás-előrejelzés. Az AI-ügynökök kontextusában az eszközöket úgy tervezték, hogy ügynökök hajtsák végre őket válaszként a **model által generált függvényhívásokra**.

## Milyen használati esetekre alkalmazható?

Az AI-ügynökök eszközöket használhatnak összetett feladatok elvégzésére, információk lekérésére vagy döntéshozatalra. Az eszközhasználati tervezési mintát gyakran olyan forgatókönyvekben alkalmazzák, amelyek dinamikus interakciót igényelnek külső rendszerekkel, például adatbázisokkal, webszolgáltatásokkal vagy kódfuttatókkal. Ez a képesség számos különböző használati esetben hasznos, többek között:

- **Dinamikus információlekérés:** Az ügynökök külső API-kat vagy adatbázisokat kérdezhetnek le a naprakész adatokért (például SQLite adatbázis lekérdezése adatelemzéshez, részvényárak vagy időjárási információk lekérése).
- **Kódvégrehajtás és értelmezés:** Az ügynökök kódot vagy szkripteket futtathatnak matematikai problémák megoldásához, jelentések generálásához vagy szimulációk végrehajtásához.
- **Munkafolyamat-automatizálás:** Ismétlődő vagy többlépéses munkafolyamatok automatizálása olyan eszközök integrálásával, mint ütemezők, e-mail szolgáltatások vagy adatcsatornák.
- **Ügyféltámogatás:** Az ügynökök CRM rendszerekkel, jegykezelő platformokkal vagy tudásbázisokkal léphetnek kapcsolatba a felhasználói kérdések megoldására.
- **Tartalomkészítés és szerkesztés:** Az ügynökök olyan eszközöket használhatnak, mint helyesírás- és nyelvtani ellenőrzők, szövegösszefoglalók vagy tartalombiztonsági értékelők, hogy segítsenek a tartalom létrehozásában.

## Mely elemek/építőkockák szükségesek az eszközhasználati tervezési minta megvalósításához?

Ezek az építőkockák lehetővé teszik az AI-ügynök számára, hogy széles körű feladatokat végezzen el. Nézzük meg a kulcselemeket, amelyek szükségesek az Eszközhasználati tervezési minta megvalósításához:

- **Funkció/Eszköz sémák**: Részletes meghatározások az elérhető eszközökről, beleértve a függvény nevét, célját, a szükséges paramétereket és a várható kimeneteket. Ezek a sémák lehetővé teszik az LLM számára, hogy megértse, milyen eszközök állnak rendelkezésre és hogyan kell érvényes kéréseket összeállítani.
- **Funkcióvégrehajtási logika**: Szabályozza, hogyan és mikor hívják meg az eszközöket a felhasználó szándéka és a beszélgetés kontextusa alapján. Ez tartalmazhat tervező modulokat, útválasztási mechanizmusokat vagy feltételes folyamatokat, amelyek dinamikusan határozzák meg az eszközhasználatot.
- **Üzenetkezelő rendszer**: Olyan komponensek, amelyek kezelik a beszélgetési folyamatot a felhasználói bemenetek, LLM-válaszok, eszközhívások és eszközkimenetek között.
- **Eszközintegrációs keretrendszer**: Infrastruktúra, amely összeköti az ügynököt különböző eszközökkel, legyenek azok egyszerű függvények vagy összetett külső szolgáltatások.
- **Hiba kezelés és validálás**: Mechanizmusok az eszközvégrehajtás hibáinak kezelésére, a paraméterek érvényesítésére és a váratlan válaszok kezelésére.
- **Állapotkezelés**: Nyomon követi a beszélgetés kontextusát, a korábbi eszközinterakciókat és a tartós adatokat annak érdekében, hogy konzisztenciát biztosítson a többfordulós interakciók során.

Ezután nézzük meg részletesebben a Funkció/Eszköz hívást.

### Funkció/Eszköz hívás

A funkcióhívás az elsődleges módja annak, hogy az LLM-eket eszközökkel történő interakcióra képessé tegyük. Gyakran látni fogja, hogy a 'Funkció' és az 'Eszköz' kifejezést felcserélhetően használják, mert a 'funkciók' (újrahasznosítható kódbetétek) azok az 'eszközök', amelyeket az ügynökök a feladatok végrehajtására használnak. Ahhoz, hogy egy függvény kódját meghívják, az LLM-nek össze kell hasonlítania a felhasználó kérését a függvény leírásával. Ennek érdekében egy sémát, amely tartalmazza az összes elérhető függvény leírását, elküldünk az LLM-nek. Az LLM ezután kiválasztja a feladathoz legmegfelelőbb függvényt és visszaadja annak nevét és argumentumait. A kiválasztott függvényt meghívják, a válasza visszakerül az LLM-hez, amely ezt az információt felhasználva adja meg a felhasználó számára a választ.

Ahhoz, hogy a fejlesztők megvalósítsák a funkcióhívást az ügynökök számára, szükség lesz:

1. Egy LLM modellre, amely támogatja a funkcióhívást
2. Egy sémára, amely tartalmazza a függvényleírásokat
3. Az egyes leírt függvények kódjára

Vegyük a példát, amikor egy város aktuális idejét szeretnénk lekérdezni:

1. **Inicializáljunk egy funkcióhívást támogató LLM-et:**

    Nem minden modell támogatja a funkcióhívást, ezért fontos ellenőrizni, hogy az általad használt LLM támogatja-e.     <a href="https://learn.microsoft.com/azure/ai-services/openai/how-to/function-calling" target="_blank">Azure OpenAI</a> támogatja a funkcióhívást. Elkezdhetjük az Azure OpenAI kliens inicializálásával. 

    ```python
    # Inicializálja az Azure OpenAI klienst
    client = AzureOpenAI(
        azure_endpoint = os.getenv("AZURE_AI_PROJECT_ENDPOINT"), 
        api_key=os.getenv("AZURE_OPENAI_API_KEY"),  
        api_version="2024-05-01-preview"
    )
    ```

1. **Hozzuk létre a funkció sémát**:

    Ezután definiálunk egy JSON sémát, amely tartalmazza a függvény nevét, a függvény által végzett művelet leírását, valamint a függvény paramétereinek nevét és leírását.
    Ezt a sémát elküldjük az előzőleg létrehozott kliensnek, együtt a felhasználó San Francisco-i időpont lekérésére irányuló kérésével. Fontos megjegyezni, hogy egy **eszközhívás** az, ami visszatér, **nem** a végső válasz a kérdésre. Amint korábban említettük, az LLM visszaadja a feladathoz kiválasztott függvény nevét és az átadandó argumentumokat.

    ```python
    # A modell számára olvasandó függvény leírása
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
  
    # Első API-hívás: Kérd meg a modellt, hogy használja a függvényt
      response = client.chat.completions.create(
          model=deployment_name,
          messages=messages,
          tools=tools,
          tool_choice="auto",
      )
  
      # Feldolgozd a modell válaszát
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

    Most, hogy az LLM kiválasztotta, melyik függvényt kell futtatni, a feladatot végrehajtó kódot meg kell valósítani és futtatni kell.
    Pythonban megvalósíthatjuk az aktuális idő lekérését. Emellett szükség lesz kódra is annak kinyerésére, hogy a response_message-ből hogyan szedjük ki a nevet és az argumentumokat a végső eredmény megszerzéséhez.

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
  
      # Második API-hívás: A modell végső válaszának lekérése
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

A Funkcióhívás a legtöbb, ha nem az összes ügynök eszközhasználati tervezésének központi eleme, azonban a nulla alapú megvalósítás néha kihívást jelenthet.
Ahogy a [Lesson 2](../../../02-explore-agentic-frameworks) leckében megtanultuk, az agentikus keretrendszerek előre elkészített építőkockákat biztosítanak az eszközhasználat megvalósításához.
 
## Eszközhasználati példák agentikus keretrendszerekkel

Íme néhány példa arra, hogyan valósítható meg az Eszközhasználati tervezési minta különböző agentikus keretrendszerek használatával:

### Microsoft Agent Framework

<a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Microsoft Agent Framework</a> egy nyílt forráskódú AI keretrendszer AI-ügynökök építéséhez. Egyszerűsíti a funkcióhívás folyamatát azzal, hogy lehetővé teszi az eszközök Python függvényekként való definiálását a `@tool` dekorátorral. A keretrendszer kezeli a modell és a kód közötti oda-vissza kommunikációt. Emellett hozzáférést biztosít előre elkészített eszközökhöz, például File Search és Code Interpreter a `AzureAIProjectAgentProvider` segítségével.

A következő ábra szemlélteti a funkcióhívás folyamatát a Microsoft Agent Framework használatával:

![Funkcióhívás](../../../translated_images/hu/functioncalling-diagram.a84006fc287f6014.webp)

A Microsoft Agent Frameworkben az eszközök dekorált függvényekként vannak definiálva. A korábban látott `get_current_time` függvényt eszközzé alakíthatjuk a `@tool` dekorátor használatával. A keretrendszer automatikusan szerializálja a függvényt és annak paramétereit, létrehozva a sémát, amelyet az LLM-nek küldünk.

```python
from agent_framework import tool
from agent_framework.azure import AzureAIProjectAgentProvider
from azure.identity import AzureCliCredential

@tool
def get_current_time(location: str) -> str:
    """Get the current time for a given location"""
    ...

# Hozd létre a klienst
provider = AzureAIProjectAgentProvider(credential=AzureCliCredential())

# Hozz létre egy ügynököt és futtasd az eszközzel
agent = await provider.create_agent(name="TimeAgent", instructions="Use available tools to answer questions.", tools=get_current_time)
response = await agent.run("What time is it?")
```
  
### Azure AI Agent Service

<a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Azure AI Agent Service</a> egy újabb agentikus keretrendszer, amelyet arra terveztek, hogy lehetővé tegye a fejlesztők számára biztonságosan magas színvonalú, kiterjeszthető AI-ügynökök építését, telepítését és skálázását anélkül, hogy a mögöttes számítási és tárolási erőforrásokat kellene kezelniük. Különösen hasznos vállalati alkalmazásokhoz, mivel teljesen felügyelt szolgáltatás vállalati szintű biztonsággal.

Az LLM API közvetlen használatához képest az Azure AI Agent Service néhány előnyt kínál, többek között:

- Automatikus eszközhívás – nincs szükség eszközhívás feldolgozására, az eszköz meghívására és a válasz kezelésére; mindez most szerveroldalon történik
- Biztonságosan kezelt adatok – a saját beszélgetési állapot kezelése helyett a threads használatára támaszkodhat, hogy minden szükséges információt tároljon
- Készenléti eszközök – olyan eszközök, amelyekkel az adatforrásaival léphet kapcsolatba, például Bing, Azure AI Search és Azure Functions.

Az Azure AI Agent Service-ben elérhető eszközök két kategóriába sorolhatók:

1. Tudáseszközök:
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/bing-grounding?tabs=python&pivots=overview" target="_blank">Grounding with Bing Search</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/file-search?tabs=python&pivots=overview" target="_blank">File Search</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-ai-search?tabs=azurecli%2Cpython&pivots=overview-azure-ai-search" target="_blank">Azure AI Search</a>

2. Műveleti eszközök:
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/function-calling?tabs=python&pivots=overview" target="_blank">Function Calling</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/code-interpreter?tabs=python&pivots=overview" target="_blank">Code Interpreter</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/openapi-spec?tabs=python&pivots=overview" target="_blank">OpenAPI defined tools</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-functions?pivots=overview" target="_blank">Azure Functions</a>

Az Agent Service lehetővé teszi, hogy ezeket az eszközöket egy `toolset`-ként használjuk együtt. Emellett `threads`-eket használ, amelyek nyomon követik egy adott beszélgetés üzenettörténetét.

Képzelje el, hogy egy Contoso nevű vállalat értékesítési ügynöke. Egy olyan beszélgető ügynököt szeretne fejleszteni, amely képes válaszolni az értékesítési adataira vonatkozó kérdésekre.

A következő kép szemlélteti, hogyan használhatná az Azure AI Agent Service-t az értékesítési adatok elemzésére:

![Agent Service működés közben](../../../translated_images/hu/agent-service-in-action.34fb465c9a84659e.webp)

Bármelyik eszköz használatához a szolgáltatással létrehozhatunk egy klienset és definiálhatunk egy eszközt vagy eszközkészletet. Gyakorlati megvalósításhoz a következő Python kódot használhatjuk. Az LLM képes lesz megnézni az eszközkészletet és eldönteni, hogy a felhasználó által létrehozott függvényt, a `fetch_sales_data_using_sqlite_query`-t használja-e, vagy a beépített Code Interpreter-t a felhasználói kérés alapján.

```python 
import os
from azure.ai.projects import AIProjectClient
from azure.identity import DefaultAzureCredential
from fetch_sales_data_functions import fetch_sales_data_using_sqlite_query # A fetch_sales_data_using_sqlite_query függvény, amely megtalálható a fetch_sales_data_functions.py fájlban.
from azure.ai.projects.models import ToolSet, FunctionTool, CodeInterpreterTool

project_client = AIProjectClient.from_connection_string(
    credential=DefaultAzureCredential(),
    conn_str=os.environ["PROJECT_CONNECTION_STRING"],
)

# Eszközkészlet inicializálása
toolset = ToolSet()

# Függvényhívó ügynök inicializálása a fetch_sales_data_using_sqlite_query függvénnyel, és hozzáadása az eszközkészlethez
fetch_data_function = FunctionTool(fetch_sales_data_using_sqlite_query)
toolset.add(fetch_data_function)

# A Code Interpreter eszköz inicializálása és hozzáadása az eszközkészlethez.
code_interpreter = code_interpreter = CodeInterpreterTool()
toolset.add(code_interpreter)

agent = project_client.agents.create_agent(
    model="gpt-4o-mini", name="my-agent", instructions="You are helpful agent", 
    toolset=toolset
)
```

## Milyen különleges megfontolások szükségesek az Eszközhasználati tervezési minta alkalmazásához megbízható AI-ügynökök építésekor?

Az LLM-ek által dinamikusan generált SQL-lel kapcsolatban gyakori aggodalom a biztonság, különösen az SQL injekció vagy rosszindulatú műveletek kockázata, például adatbázis törlése vagy manipulálása. Bár ezek az aggodalmak jogosak, hatékonyan mérsékelhetők az adatbázis-hozzáférési jogosultságok megfelelő konfigurálásával. A legtöbb adatbázis esetében ez azt jelenti, hogy az adatbázist csak olvashatóként kell konfigurálni. Olyan adatbázis-szolgáltatásoknál, mint a PostgreSQL vagy az Azure SQL, az alkalmazásnak olvasható (SELECT) szerepkört kell kapnia.

Az alkalmazás biztonságos környezetben való futtatása tovább növeli a védelmet. Vállalati forgatókönyvekben az adatok általában kinyerésre és átalakításra kerülnek az operációs rendszerekből egy olvasható adatbázisba vagy adattárházba, amely felhasználóbarát sémával rendelkezik. Ez a megközelítés biztosítja, hogy az adatok biztonságosak, teljesítmény és hozzáférhetőség szempontjából optimalizáltak, és hogy az alkalmazás korlátozott, csak olvasható hozzáféréssel rendelkezik.

## Mintakódok

- Python: [Agent Framework](./code_samples/04-python-agent-framework.ipynb)
- .NET: [Agent Framework](./code_samples/04-dotnet-agent-framework.md)

## Van még kérdése az Eszközhasználati tervezési mintákkal kapcsolatban?

Csatlakozzon a [Microsoft Foundry Discord](https://aka.ms/ai-agents/discord) szerverhez, hogy találkozzon más tanulókkal, részt vegyen konzultációkon és választ kapjon AI-ügynökökkel kapcsolatos kérdéseire.

## További források

- <a href="https://microsoft.github.io/build-your-first-agent-with-azure-ai-agent-service-workshop/" target="_blank">Azure AI Agents Service Workshop</a>
- <a href="https://github.com/Azure-Samples/contoso-creative-writer/tree/main/docs/workshop" target="_blank">Contoso Creative Writer Multi-Agent Workshop</a>
- <a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Microsoft Agent Framework Overview</a>

## Előző lecke

[Az agentikus tervezési minták megértése](../03-agentic-design-patterns/README.md)

## Következő lecke
[Ügynöki RAG](../05-agentic-rag/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
Felelősségkizárás:
Ezt a dokumentumot a mesterséges intelligencián alapuló fordítószolgáltatás, a Co-op Translator (https://github.com/Azure/co-op-translator) segítségével fordították. Bár igyekszünk a pontosságra, kérjük, vegye figyelembe, hogy az automatikus fordítások hibákat vagy pontatlanságokat tartalmazhatnak. Az eredeti, anyanyelvi változat tekintendő hiteles forrásnak. Fontos információk esetén professzionális, emberi fordítást javasolunk. Nem vállalunk felelősséget az e fordítás használatából eredő bármilyen félreértésért vagy téves értelmezésért.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->