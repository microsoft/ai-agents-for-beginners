[![Hogyan tervezzünk jó mesterséges intelligencia ügynököket](../../../translated_images/hu/lesson-4-thumbnail.546162853cb3daff.webp)](https://youtu.be/vieRiPRx-gI?si=cEZ8ApnT6Sus9rhn)

> _(Kattintson a fenti képre a leckéhez tartozó videó megtekintéséhez)_

# Eszközhasználati Tervezési Minta

Az eszközök érdekesek, mert lehetővé teszik, hogy az MI-ügynökök szélesebb körű képességekkel rendelkezzenek. Az ügynöknek nem kell korlátozott cselekvéseket végrehajtania, hanem eszköz hozzáadásával az ügynök most már számos különböző műveletet képes végrehajtani. Ebben a fejezetben az Eszközhasználati Tervezési Mintát vizsgáljuk meg, amely leírja, hogyan használhatják az MI-ügynökök a specifikus eszközöket céljaik eléréséhez.

## Bevezetés

Ebben a leckében a következő kérdésekre keressük a választ:

- Mi az eszközhasználati tervezési minta?
- Milyen esetekben alkalmazható?
- Mely elemekre/építőelemekre van szükség a minta implementálásához?
- Milyen különleges szempontok vannak az Eszközhasználati Tervezési Minta megbízható MI-ügynökök építéséhez?

## Tanulási célok

A lecke elvégzése után képes lesz:

- Meghatározni az Eszközhasználati Tervezési Mintát és célját.
- Azonosítani azokat az eseteket, ahol az Eszközhasználati Tervezési Minta alkalmazható.
- Megérteni a minta implementálásához szükséges kulcselemeket.
- Felismerni a megbízhatóság biztosításához szükséges szempontokat MI-ügynököknél, akik ezt a mintát használják.

## Mi az Eszközhasználati Tervezési Minta?

Az **Eszközhasználati Tervezési Minta** arra fókuszál, hogy az LLM-ek képessé váljanak külső eszközökkel interakcióba lépni bizonyos célok elérése érdekében. Az eszközök olyan kódok, amelyeket az ügynök végrehajthat műveletek elvégzésére. Egy eszköz lehet egyszerű függvény, mint például egy számológép, vagy egy harmadik fél szolgáltatásának API hívása, mint az árfolyam lekérdezés vagy időjárás előrejelzés. Az MI-ügynökök kontextusában az eszközöket úgy tervezték, hogy az ügynökök modellek által generált függvényhívásokra reagálva hajtsák végre őket.

## Milyen esetekben alkalmazható?

Az MI-ügynökök eszközöket használhatnak összetett feladatok teljesítésére, információk lekérésére vagy döntések meghozatalára. Az eszközhasználati tervezési minta gyakran olyan helyzetekben használatos, ahol dinamikus interakció szükséges külső rendszerekkel, mint adatbázisok, webszolgáltatások vagy kódértelmezők. Ez a képesség számos különböző felhasználási esetben hasznos, például:

- **Dinamikus információ lekérés:** Az ügynökök külső API-kon vagy adatbázisokon keresztül tudnak aktuális adatokat lekérdezni (pl. SQLite adatbázis lekérdezése adatelemzéshez, részvényárfolyam vagy időjárási adatok lekérése).
- **Kód végrehajtás és értelmezés:** Az ügynökök képesek kódot vagy szkripteket futtatni matematikai problémák megoldására, jelentések generálására vagy szimulációk végrehajtására.
- **Munkafolyamat automatizálás:** Ismétlődő vagy többlépéses munkafolyamatok automatizálása olyan eszközökkel, mint feladatütemezők, e-mail szolgáltatások vagy adatcsövek.
- **Ügyféltámogatás:** Az ügynökök képesek CRM rendszerekkel, jegykezelő platformokkal vagy tudásbázisokkal interakcióba lépni a felhasználói kérdések megoldására.
- **Tartalom generálás és szerkesztés:** Az ügynökök eszközöket használhatnak, mint helyesírás ellenőrzők, szövegösszefoglalók vagy tartalombiztonsági értékelők a tartalomkészítés támogatására.

## Mely elemekre/építőelemekre van szükség az eszközhasználati tervezési minta megvalósításához?

Ezek az építőelemek teszik lehetővé, hogy az MI ügynök sokféle feladatot elvégezzen. Nézzük meg a kulcsfontosságú elemeket az Eszközhasználati Tervezési Minta implementálásához:

- **Függvény/Eszköz séma:** Részletes meghatározások az elérhető eszközökről, ideértve a függvény nevét, célját, szükséges paramétereket és a várt kimenetet. Ezek a sémák lehetővé teszik az LLM számára, hogy megértse, milyen eszközök állnak rendelkezésre és hogyan kell érvényes kéréseket összeállítani.

- **Függvényvégrehajtási logika:** Szabályozza, hogy mikor és hogyan hívják meg az eszközöket a felhasználó szándéka és a beszélgetés kontextusa alapján. Ez tartalmazhat tervező modulokat, irányítási mechanizmusokat vagy feltételes áramlásokat, amelyek dinamikusan határozzák meg az eszközhasználatot.

- **Üzenetkezelő rendszer:** A komponensek irányítják a beszélgetési folyamatot a felhasználói bemenetek, LLM válaszok, eszközhívások és eszközkimenetek között.

- **Eszközintegrációs keretrendszer:** Infrastrukturális elem, amely az ügynököt különféle eszközökhöz csatlakoztatja, legyenek azok egyszerű függvények vagy bonyolult külső szolgáltatások.

- **Hibakezelés és érvényesítés:** Mechanizmusok az eszközvégrehajtás hibáinak kezelésére, paraméterek érvényesítésére és váratlan válaszok menedzselésére.

- **Állapotkezelés:** Nyomon követi a beszélgetés kontextusát, korábbi eszközinterakciókat és tartós adatokat, hogy több lépéses interakcióknál is biztosítsa a konzisztenciát.

Most nézzük meg részletesebben a Függvény/Eszközhívást.

### Függvény/Eszközhívás

A függvényhívás a fő módszer, amellyel a Nagynyelvű Modellek (LLM-ek) eszközökkel lépnek kapcsolatba. Gyakran használják felcserélhetően a 'Függvény' és 'Eszköz' szavakat, mert a 'függvények' (újrahasználható kódblokkok) azok az 'eszközök', amelyeket az ügynökök a feladatok elvégzéséhez használnak. Ahhoz, hogy egy függvény kódját meghívják, az LLM-nek össze kell vetnie a felhasználó kérését a függvény leírásával. Ehhez egy sémát küldenek az LLM-nek, amely tartalmazza az összes elérhető függvény leírását. Az LLM kiválasztja az adott feladathoz legmegfelelőbb függvényt, majd visszaadja annak nevét és argumentumait. A kiválasztott függvényt meghívják, a válaszát visszaküldik az LLM-nek, ami az információ alapján válaszol a felhasználói kérésre.

Fejlesztők számára, hogy megvalósítsák a függvényhívást ügynökök számára, szükség van:

1. Egy LLM modellre, amely támogatja a függvényhívást
2. Egy séma, amely tartalmazza a függvények leírásait
3. A leírt függvények kódjára

Vegyük példának egy város aktuális idejének lekérését:

1. **Indítsunk el egy olyan LLM-et, amely támogatja a függvényhívást:**

    Nem minden modell támogatja a függvényhívást, ezért fontos ellenőrizni, hogy az Ön által használt LLM tudja-e ezt. Az <a href="https://learn.microsoft.com/azure/ai-services/openai/how-to/function-calling" target="_blank">Azure OpenAI</a> támogatja a függvényhívást. Kezdjük az Azure OpenAI kliens inicializálásával.

    ```python
    # Inicializálja az Azure OpenAI kliensét
    client = AzureOpenAI(
        azure_endpoint = os.getenv("AZURE_AI_PROJECT_ENDPOINT"), 
        api_key=os.getenv("AZURE_OPENAI_API_KEY"),  
        api_version="2024-05-01-preview"
    )
    ```

1. **Hozzunk létre egy függvény sémát:**

    Definiálunk egy JSON sémát, amely tartalmazza a függvény nevét, a funkcionalitás leírását, valamint a paraméterek neveit és leírását.
    Ezután ezt a sémát elküldjük a korábban létrehozott kliensnek, mellékelve a felhasználó kérését, amely San Francisco aktuális idejére vonatkozik. Fontos megjegyezni, hogy a visszakapott válasz egy **eszközhívás**, **nem** a kérdés végleges válasza. Ahogy korábban említettük, az LLM visszaadja a feladathoz kiválasztott függvény nevét és argumentumait.

    ```python
    # A modell számára olvasható funkcióleírás
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
  
      # A modell válaszának feldolgozása
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

    Most, hogy az LLM kiválasztotta a végrehajtandó függvényt, implementálni és futtatni kell a feladatot végrehajtó kódot.
    Python nyelven megvalósíthatjuk az aktuális idő lekérését. Írni kell kódot az is, hogy a response_message-ből kinyerjük a függvény nevét és argumentumait a végső eredményhez.

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

A függvényhívás az eszközhasználati tervezés alapját képezi az ügynököknél, de megvalósítása nulláról néha kihívást jelenthet.
Ahogy a [2. leckében](../../../02-explore-agentic-frameworks) láttuk, az ügynök keretrendszerek előre elkészített építőelemeket biztosítanak az eszközhasználat megvalósításához.

## Eszközhasználati példák ügynök keretrendszerekkel

Íme néhány példa arra, hogyan lehet megvalósítani az Eszközhasználati Tervezési Mintát különböző ügynök keretrendszerekkel:

### Microsoft Agent Framework

A <a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Microsoft Agent Framework</a> egy nyílt forráskódú MI keretrendszer MI-ügynökök építéséhez. Egyszerűsíti a függvényhívást, mivel lehetővé teszi az eszközök Python függvényekként való definiálását az `@tool` dekorátor használatával. A keretrendszer kezeli a kommunikációt a modell és a kód között. Emellett előre elkészített eszközökhöz is hozzáférést biztosít, mint például Fájlkereső és Kódértelmező az `AzureAIProjectAgentProvider`-en keresztül.

Az alábbi diagram illusztrálja a függvényhívás folyamatát a Microsoft Agent Frameworkkel:

![function calling](../../../translated_images/hu/functioncalling-diagram.a84006fc287f6014.webp)

A Microsoft Agent Framework-ben az eszközök dekorált függvényekként vannak definiálva. Az előzőleg látott get_current_time függvényt eszközzé alakíthatjuk az `@tool` dekorátorral. A keretrendszer automatikusan sorosítja a függvényt és paramétereit, létrehozva a sémát, amelyet az LLM-nek küldünk.

```python
from agent_framework import tool
from agent_framework.azure import AzureAIProjectAgentProvider
from azure.identity import AzureCliCredential

@tool
def get_current_time(location: str) -> str:
    """Get the current time for a given location"""
    ...

# Hozd létre az ügyfelet
provider = AzureAIProjectAgentProvider(credential=AzureCliCredential())

# Hozz létre egy ügynököt és futtasd az eszközzel
agent = await provider.create_agent(name="TimeAgent", instructions="Use available tools to answer questions.", tools=get_current_time)
response = await agent.run("What time is it?")
```
  
### Azure AI Agent Service

Az <a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Azure AI Agent Service</a> egy újabb ügynök keretrendszer, amely lehetővé teszi fejlesztők számára, hogy biztonságosan építsenek, telepítsenek és skálázzanak magas minőségű, kiterjeszthető MI-ügynököket anélkül, hogy az alapul szolgáló számítási és tárolási erőforrásokat menedzselniük kellene. Különösen hasznos vállalati alkalmazások esetén, mivel teljesen felügyelt szolgáltatás vállalati szintű biztonsággal.

Az LLM API közvetlen fejlesztésével szemben, az Azure AI Agent Service több előnyt kínál, többek között:

- Automatikus eszközhívás – nincs szükség a hívás elemzésére, az eszköz meghívására vagy a válasz kezelésére, mindez a szerveroldalon történik
- Biztonságosan kezelt adatok – a saját beszélgetési állapot kezelés helyett a szálak tárolják az összes szükséges információt
- Kész eszközök – eszközök, amelyekkel adatforrásokkal lehet interakcióba lépni, mint Bing, Azure AI Search és Azure Functions

Az Azure AI Agent Service-ben rendelkezésre álló eszközök két kategóriába sorolhatók:

1. Tudás eszközök:
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/bing-grounding?tabs=python&pivots=overview" target="_blank">Bing Keresés alapozás</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/file-search?tabs=python&pivots=overview" target="_blank">Fájlkereső</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-ai-search?tabs=azurecli%2Cpython&pivots=overview-azure-ai-search" target="_blank">Azure AI Search</a>

2. Művelet eszközök:
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/function-calling?tabs=python&pivots=overview" target="_blank">Függvényhívás</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/code-interpreter?tabs=python&pivots=overview" target="_blank">Kódértelmező</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/openapi-spec?tabs=python&pivots=overview" target="_blank">OpenAPI által definiált eszközök</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-functions?pivots=overview" target="_blank">Azure Functions</a>

Az Agent Service lehetővé teszi számunkra ezeknek az eszközöknek az együttes használatát, mint egy `toolset` (eszközkészlet). Emellett használja a `szálakat` (threads), amelyek nyomon követik egy adott beszélgetés üzenettörténetét.

Képzeljük el, hogy Ön egy értékesítési ügynök a Contoso nevű vállalatnál. Egy beszélgető ügynököt szeretne fejleszteni, amely válaszolni tud az Ön értékesítési adataira vonatkozó kérdésekre.

Az alábbi kép bemutatja, hogyan használhatja az Azure AI Agent Service-t értékesítési adatainak elemzésére:

![Agentic Service In Action](../../../translated_images/hu/agent-service-in-action.34fb465c9a84659e.webp)

Bármelyik eszközt használhatjuk a szolgáltatással, ha létrehozunk egy klienst és definiálunk egy eszközt vagy eszközkészletet. Gyakorlatilag az alábbi Python kódot használhatjuk. Az LLM meg tudja nézni az eszközkészletet, és eldöntheti, hogy a felhasználói kérés alapján a felhasználó által létrehozott `fetch_sales_data_using_sqlite_query` függvényt vagy az előre elkészített Kódértelmezőt használja-e.

```python 
import os
from azure.ai.projects import AIProjectClient
from azure.identity import DefaultAzureCredential
from fetch_sales_data_functions import fetch_sales_data_using_sqlite_query # fetch_sales_data_using_sqlite_query függvény, amely a fetch_sales_data_functions.py fájlban található.
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
    model="gpt-4o-mini", name="my-agent", instructions="You are helpful agent", 
    toolset=toolset
)
```

## Milyen különleges szempontok vannak az Eszközhasználati Tervezési Minta megbízható MI-ügynökök építéséhez?

Az LLM-ek által dinamikusan generált SQL-lel kapcsolatban gyakori aggodalom a biztonság, különösen az SQL befecskendezés vagy rosszindulatú műveletek kockázata, mint például az adatbázis törlése vagy manipulálása. Bár ezek az aggodalmak jogosak, hatékonyan mérsékelhetők az adatbázis-hozzáférési jogosultságok megfelelő beállításával. A legtöbb adatbázis esetében ez az adatbázis csak olvashatóvá konfigurálását jelenti. Olyan adatbázis szolgáltatásoknál, mint a PostgreSQL vagy Azure SQL, az alkalmazásnak olvasható (SELECT) szerepkörrel kell rendelkeznie.

Az alkalmazás biztonságos környezetben való futtatása növeli a védelmet. Vállalati szcenáriókban az adatokat általában kinyerik és átalakítják az operatív rendszerekből egy olvasható adatbázisba vagy adattárházba, felhasználóbarát sémával. Ez a megközelítés biztosítja, hogy az adatok biztonságosak, optimalizáltak a teljesítmény és a hozzáférhetőség szempontjából, és az alkalmazás korlátozott, csak olvasási hozzáféréssel rendelkezzen.

## Példakódok

- Python: [Agent Framework](./code_samples/04-python-agent-framework.ipynb)
- .NET: [Agent Framework](./code_samples/04-dotnet-agent-framework.md)

## Több kérdése van az Eszközhasználati Tervezési Mintákkal kapcsolatban?

Csatlakozzon a [Microsoft Foundry Discord](https://aka.ms/ai-agents/discord) közösségéhez, hogy találkozzon más tanulókkal, részt vegyen konzultációkon és választ kapjon MI-ügynökökkel kapcsolatos kérdéseire.

## További források

- <a href="https://microsoft.github.io/build-your-first-agent-with-azure-ai-agent-service-workshop/" target="_blank">Azure AI Agents Service Workshop</a>
- <a href="https://github.com/Azure-Samples/contoso-creative-writer/tree/main/docs/workshop" target="_blank">Contoso Creative Writer Multi-Agent Workshop</a>
- <a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Microsoft Agent Framework áttekintés</a>

## Előző lecke

[Agentikus tervezési minták megértése](../03-agentic-design-patterns/README.md)

## Következő lecke
[Agentikus RAG](../05-agentic-rag/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Jogi nyilatkozat**:
Ez a dokumentum az AI fordítási szolgáltatás, a [Co-op Translator](https://github.com/Azure/co-op-translator) segítségével készült. Bár az pontosságra törekszünk, kérjük, vegye figyelembe, hogy az automatikus fordítások hibákat vagy pontatlanságokat tartalmazhatnak. Az eredeti dokumentum az anyanyelvén tekintendő hiteles forrásnak. Fontos információk esetén professzionális emberi fordítást javasolunk. Nem vállalunk felelősséget semmilyen félreértésért vagy téves értelmezésért, amely ebből a fordításból ered.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->