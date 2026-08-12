[![AI Ügynök Keretrendszerek felfedezése](../../../translated_images/hu/lesson-2-thumbnail.c65f44c93b8558df.webp)](https://youtu.be/ODwF-EZo_O8?si=1xoy_B9RNQfrYdF7)

> _(Kattints a fenti képre az óra videójának megtekintéséhez)_

# AI Ügynök Keretrendszerek Felfedezése

Az AI ügynök keretrendszerek olyan szoftverplatformok, amelyeket az AI ügynökök egyszerűbb létrehozására, telepítésére és kezelésére terveztek. Ezek a keretrendszerek előre elkészített komponenseket, absztrakciókat és eszközöket biztosítanak a fejlesztőknek, amelyek megkönnyítik a bonyolult AI rendszerek fejlesztését.

Ezek a keretrendszerek segítik a fejlesztőket, hogy az alkalmazásaik egyedi aspektusaira koncentrálhassanak, szabványosított megközelítéseket nyújtva az AI ügynök fejlesztés általános kihívásaira. Növelik a skálázhatóságot, elérhetőséget és hatékonyságot az AI rendszerek építése során.

## Bevezetés

Ez az óra a következőkről szól:

- Mik azok az AI Ügynök Keretrendszerek és mit tesznek lehetővé a fejlesztők számára?
- Hogyan használhatják a csapatok ezeket az ügynökök képességeinek gyors prototípus készítésére, iterálására és fejlesztésére?
- Milyen különbségek vannak a Microsoft által létrehozott keretrendszerek és eszközök között (<a href="https://aka.ms/ai-agents-beginners/ai-agent-service" target="_blank">Microsoft Foundry Agent Service</a> és a <a href="https://learn.microsoft.com/azure/ai-services/openai/how-to/responses" target="_blank">Microsoft Agent Framework</a>)?
- Integrálhatom-e közvetlenül a meglévő Azure ökoszisztéma eszközeimet, vagy különálló megoldásokra van szükség?
- Mi az a Microsoft Foundry Agent Service, és hogyan segít nekem?

## Tanulási célok

Ennek az órának a célja, hogy segítsen megérteni:

- Az AI Ügynök Keretrendszerek szerepét az AI fejlesztésben.
- Hogyan lehet az AI Ügynök Keretrendszereket használni intelligens ügynökök építésére.
- Az AI Ügynök Keretrendszerek által engedélyezett kulcsfontosságú képességeket.
- A Microsoft Agent Framework és a Microsoft Foundry Agent Service közötti különbségeket.

## Mik azok az AI Ügynök Keretrendszerek, és mit tehetnek a fejlesztők?

A hagyományos AI keretrendszerek segíthetnek az AI integrálásában az alkalmazásokba, és az alábbi módokon javíthatják ezeket az alkalmazásokat:

- **Személyre szabás**: Az AI képes elemezni a felhasználói viselkedést és preferenciákat, hogy személyre szabott ajánlásokat, tartalmat és élményeket nyújtson.
Példa: Olyan streaming szolgáltatások, mint a Netflix, AI-t használnak filmek és műsorok ajánlására a megtekintési előzmények alapján, növelve a felhasználói elköteleződést és elégedettséget.
- **Automatizálás és Hatékonyság**: Az AI képes automatizálni az ismétlődő feladatokat, optimalizálni a munkafolyamatokat és javítani az üzemi hatékonyságot.
Példa: Az ügyfélszolgálati alkalmazások AI-alapú csevegőbotokat használnak az általános kérdések kezelésére, csökkentve a válaszadási időt és felszabadítva az emberi ügynököket a bonyolultabb problémákra.
- **Fokozott felhasználói élmény**: Az AI javíthatja az általános felhasználói élményt intelligens funkciók biztosításával, például hangfelismerés, természetes nyelvfeldolgozás és prediktív szöveg segítségével.
Példa: Virtuális asszisztensek, mint Siri és Google Assistant AI-t használnak hangparancsok megértésére és válaszadására, megkönnyítve a felhasználók eszközeikkel való interakcióját.

### Ez mind remekül hangzik, de miért van szükségünk AI Ügynök Keretrendszerre?

Az AI Ügynök keretrendszerek többek egyszerű AI keretrendszereknél. Olyan intelligens ügynökök létrehozását teszik lehetővé, amelyek képesek felhasználókkal, más ügynökökkel és a környezettel kommunikálni, hogy elérjék konkrét céljaikat. Ezek az ügynökök autonóm viselkedést mutathatnak, döntéseket hozhatnak, és alkalmazkodhatnak a változó körülményekhez. Nézzük meg néhány kulcsfontosságú képességet, amelyeket az AI Ügynök Keretrendszerek támogatnak:

- **Ügynökök együttműködése és koordinációja**: Több AI ügynök létrehozását teszi lehetővé, amelyek képesek együtt dolgozni, kommunikálni és koordinálni a komplex feladatok megoldását.
- **Feladat automatizálás és menedzsment**: Mechanizmusokat biztosít a több lépésből álló munkafolyamatok automatizálására, feladat delegálására és dinamikus feladatkezelésre az ügynökök között.
- **Kontextuális megértés és alkalmazkodás**: Az ügynökök képessé tétele a kontextus megértésére, a változó környezethez való alkalmazkodásra és a valós idejű információk alapján történő döntéshozatalra.

Összefoglalva, az ügynökök lehetővé teszik, hogy többet tegyél, az automatizálást magasabb szintre emeld, intelligensebb rendszereket hozz létre, amelyek képesek alkalmazkodni és tanulni a környezetükből.

## Hogyan lehet gyorsan prototípust készíteni, iterálni és fejleszteni az ügynök képességeit?

Ez egy gyorsan változó terület, de vannak olyan elemek, amelyek a legtöbb AI Ügynök Keretrendszerben közösek, és segítenek gyors prototípust készíteni és iterálni, ilyenek a moduláris komponensek, együttműködő eszközök és a valós idejű tanulás. Merüljünk el ezekben:

- **Használj Moduláris Komponenseket**: Az AI SDK-k előre elkészített komponenseket kínálnak, például AI és memória csatlakozókat, funkcióhívást természetes nyelven vagy kódbővítményeken keresztül, prompt sablonokat és egyebeket.
- **Használj Együttműködő Eszközöket**: Tervezd meg az ügynököket konkrét szerepekkel és feladatokkal, lehetővé téve az együttműködési munkafolyamatok tesztelését és finomítását.
- **Tanulj Valós Időben**: Alkalmazz visszacsatolási hurkokat, ahol az ügynökök a kölcsönhatásokból tanulnak, és dinamikusan igazítják viselkedésüket.

### Használj Moduláris Komponenseket

Az olyan SDK-k, mint a Microsoft Agent Framework, előre elkészített komponenseket kínálnak, mint AI csatlakozók, eszközdefiníciók és ügynök menedzsment.

**Hogyan használhatják ezeket a csapatok**: A csapatok gyorsan összeállíthatják ezeket a komponenseket működő prototípus létrehozásához anélkül, hogy teljesen nulláról kellene kezdeniük, lehetővé téve a gyors kísérletezést és iterálást.

**Hogyan működik ez a gyakorlatban**: Használhatsz egy előre elkészített elemzőt az információk kinyerésére a felhasználói bemenetből, egy memória modult adatok tárolására és lekérésére, és egy prompt generátort a felhasználókkal való interakcióhoz, mindezt anélkül, hogy ezeket a komponenseket nulláról kellene megírni.

**Példa kód**. Nézzünk egy példát arra, hogyan használhatod a Microsoft Agent Frameworköt a `FoundryChatClient` segítségével, hogy a modell eszközhívásokkal válaszoljon a felhasználói bemenetekre:

``` python
# Microsoft Agent Framework Python példa

import asyncio
import os

from agent_framework import tool
from agent_framework.foundry import FoundryChatClient
from azure.identity import AzureCliCredential


# Definiáljunk egy mintafeladatot az utazás lefoglalására
@tool(approval_mode="never_require")
def book_flight(date: str, location: str) -> str:
    """Book travel given location and date."""
    return f"Travel was booked to {location} on {date}"


async def main():
    provider = FoundryChatClient(
        project_endpoint=os.environ["AZURE_AI_PROJECT_ENDPOINT"],
        model=os.environ["AZURE_AI_MODEL_DEPLOYMENT_NAME"],
        credential=AzureCliCredential(),
    )
    agent = provider.as_agent(
        name="travel_agent",
        instructions="Help the user book travel. Use the book_flight tool when ready.",
        tools=[book_flight],
    )

    response = await agent.run("I'd like to go to New York on January 1, 2025")
    print(response)
    # Példa kimenet: Az Ön január 1-jei, 2025-ös New Yorkba tartó repülőjegye sikeresen lefoglalva. Kellemes utazást! ✈️🗽


if __name__ == "__main__":
    asyncio.run(main())
```

Ebből a példából láthatod, hogyan használhatsz előre elkészített elemzőt a felhasználói bemenet kulcsfontosságú adatainak, például az indulási hely, célállomás és időpont kinyerésére egy repülőjegyfoglalási kérés esetén. Ez a moduláris megközelítés lehetővé teszi, hogy a magas szintű logikára koncentrálj.

### Használj Együttműködő Eszközöket

Olyan keretrendszerek, mint a Microsoft Agent Framework, megkönnyítik több ügynök létrehozását, amelyek együtt tudnak dolgozni.

**Hogyan használhatják ezt a csapatok**: A csapatok tervezhetnek olyan ügynököket, akiknek speciális szerepük és feladataik vannak, lehetővé téve számukra az együttműködő munkafolyamatok tesztelését és finomítását, valamint az általános rendszer hatékonyságának javítását.

**Hogyan működik ez a gyakorlatban**: Létrehozhatsz egy ügynök csapatot, ahol minden ügynök egy speciális funkciót lát el, például adatlekérés, elemzés vagy döntéshozatal. Ezek az ügynökök kommunikálhatnak és megoszthatnak információkat egy közös cél érdekében, például egy felhasználói kérdés megválaszolására vagy egy feladat elvégzésére.

**Példa kód (Microsoft Agent Framework)**:

```python
# Több ügynök létrehozása, amelyek együttműködnek a Microsoft Agent Framework használatával

import os
from agent_framework.foundry import FoundryChatClient
from azure.identity import AzureCliCredential

provider = FoundryChatClient(
    project_endpoint=os.environ["AZURE_AI_PROJECT_ENDPOINT"],
    model=os.environ["AZURE_AI_MODEL_DEPLOYMENT_NAME"],
    credential=AzureCliCredential(),
)

# Adatlekérési ügynök
agent_retrieve = provider.as_agent(
    name="dataretrieval",
    instructions="Retrieve relevant data using available tools.",
    tools=[retrieve_tool],
)

# Adatelemzési ügynök
agent_analyze = provider.as_agent(
    name="dataanalysis",
    instructions="Analyze the retrieved data and provide insights.",
    tools=[analyze_tool],
)

# Ügynökök egymás utáni futtatása egy feladaton
retrieval_result = await agent_retrieve.run("Retrieve sales data for Q4")
analysis_result = await agent_analyze.run(f"Analyze this data: {retrieval_result}")
print(analysis_result)
```

Az előző kódban azt láthatod, hogyan hozhatsz létre egy olyan feladatot, amelyben több ügynök együtt dolgozik adat elemzésén. Minden ügynök egy adott feladatot végez, és a feladat a koordinált munkájuk eredményeként valósul meg. Dedikált, speciális szerepkörű ügynökök létrehozásával javíthatod a feladat hatékonyságát és teljesítményét.

### Tanulj Valós Időben

Fejlett keretrendszerek kínálnak képességeket valós idejű kontextusmegértésre és alkalmazkodásra.

**Hogyan használhatják ezt a csapatok**: Csapatok visszacsatolási hurkokat alkalmazhatnak, ahol az ügynökök a kölcsönhatásokból tanulnak és dinamikusan módosítják viselkedésüket, folyamatos fejlesztést és finomítást eredményezve.

**Hogyan működik ez a gyakorlatban**: Az ügynökök elemezhetik a felhasználói visszajelzéseket, környezeti adatokat és a feladatok eredményeit, hogy frissítsék tudásbázisukat, módosítsák döntési algoritmusaikat és idővel javítsák teljesítményüket. Ez az ismétlődő tanulási folyamat lehetővé teszi az ügynökök számára, hogy alkalmazkodjanak a változó feltételekhez és felhasználói preferenciákhoz, ezáltal növelve az egész rendszer hatékonyságát.

## Milyen különbségek vannak a Microsoft Agent Framework és a Microsoft Foundry Agent Service között?

Sokféleképpen össze lehet hasonlítani ezeket a megközelítéseket, de nézzük meg néhány kulcsfontosságú különbséget a tervezésük, képességeik és célfelhasználási eseteik szempontjából:

## Microsoft Agent Framework (MAF)

A Microsoft Agent Framework egy egyszerűsített SDK, amely az AI ügynökök építését teszi lehetővé `FoundryChatClient` használatával. Lehetővé teszi az ügynökök létrehozását, amelyek az Azure OpenAI modellekre építenek beépített eszközhívással, beszélgetéskezeléssel és vállalati szintű biztonsággal, az Azure azonosításon keresztül.

**Használati esetek**: Termelésre kész AI ügynökök létrehozása eszközhasználattal, több lépésből álló munkafolyamatokkal és vállalati integrációs szcenáriókkal.

Íme néhány fontos alapfogalom a Microsoft Agent Frameworkből:

- **Ügynökök**. Egy ügynököt a `FoundryChatClient`-tel hoznak létre, amely konfigurálható névvel, utasításokkal és eszközökkel. Az ügynök képes:
  - **Feldolgozni a felhasználói üzeneteket** és válaszokat generálni Azure OpenAI modellek segítségével.
  - **Automatikusan eszközöket hívni** a beszélgetés kontextusa alapján.
  - **Fenntartani a beszélgetési állapotot** több interakció során.

  Íme egy kódrészlet arról, hogyan lehet egy ügynököt létrehozni:

    ```python
    import os
    from agent_framework.foundry import FoundryChatClient
    from azure.identity import AzureCliCredential

    provider = FoundryChatClient(
        project_endpoint=os.environ["AZURE_AI_PROJECT_ENDPOINT"],
        model=os.environ["AZURE_AI_MODEL_DEPLOYMENT_NAME"],
        credential=AzureCliCredential(),
    )
    agent = provider.as_agent(
        name="my_agent",
        instructions="You are a helpful assistant.",
    )

    response = await agent.run("Hello, World!")
    print(response)
    ```

- **Eszközök**. A keretrendszer támogatja az eszközök Python függvényekként történő definiálását, amelyeket az ügynök automatikusan hívhat meg. Az eszközök regisztrálása az ügynök létrehozásakor történik:

    ```python
    def get_weather(location: str) -> str:
        """Get the current weather for a location."""
        return f"The weather in {location} is sunny, 72\u00b0F."

    agent = provider.as_agent(
        name="weather_agent",
        instructions="Help users check the weather.",
        tools=[get_weather],
    )
    ```

- **Több Ügynök Koordinációja**. Több különböző specializációjú ügynök is létrehozható, és koordinálhatják a munkájukat:

    ```python
    planner = provider.as_agent(
        name="planner",
        instructions="Break down complex tasks into steps.",
    )

    executor = provider.as_agent(
        name="executor",
        instructions="Execute the planned steps using available tools.",
        tools=[execute_tool],
    )

    plan = await planner.run("Plan a trip to Paris")
    result = await executor.run(f"Execute this plan: {plan}")
    ```

- **Azure Azonosítás Integráció**. A keretrendszer az `AzureCliCredential`-t (vagy a `DefaultAzureCredential`-t) használja biztonságos, kulcs nélküli hitelesítésre, így nincs szükség API kulcsok kezelésére.

## Microsoft Foundry Agent Service

A Microsoft Foundry Agent Service egy újabb szolgáltatás, amelyet a Microsoft Ignite 2024-en mutattak be. Lehetővé teszi AI ügynökök fejlesztését és telepítését rugalmasabb modellekkel, például közvetlenül nyílt forráskódú LLM-ek hívásával, mint a Llama 3, Mistral és Cohere.

A Microsoft Foundry Agent Service erősebb vállalati biztonsági mechanizmusokat és adattárolási módokat kínál, így alkalmas vállalati alkalmazásokhoz.

Alapértelmezetten együttműködik a Microsoft Agent Frameworkkel ügynökök építéséhez és telepítéséhez.

Jelenleg nyilvánosan előzetes verzióban érhető el, és támogatja a Python és C# alapú ügynökfejlesztést.

A Microsoft Foundry Agent Service Python SDK segítségével létrehozhatunk egy ügynököt felhasználói definiált eszközzel:

```python
import asyncio
from azure.identity import DefaultAzureCredential
from azure.ai.projects import AIProjectClient

# Eszközfunkciók meghatározása
def get_specials() -> str:
    """Provides a list of specials from the menu."""
    return """
    Special Soup: Clam Chowder
    Special Salad: Cobb Salad
    Special Drink: Chai Tea
    """

def get_item_price(menu_item: str) -> str:
    """Provides the price of the requested menu item."""
    return "$9.99"


async def main() -> None:
    credential = DefaultAzureCredential()
    project_client = AIProjectClient.from_connection_string(
        credential=credential,
        conn_str="your-connection-string",
    )

    agent = project_client.agents.create_agent(
        model="gpt-5-mini",
        name="Host",
        instructions="Answer questions about the menu.",
        tools=[get_specials, get_item_price],
    )

    thread = project_client.agents.create_thread()

    user_inputs = [
        "Hello",
        "What is the special soup?",
        "How much does that cost?",
        "Thank you",
    ]

    for user_input in user_inputs:
        print(f"# User: '{user_input}'")
        message = project_client.agents.create_message(
            thread_id=thread.id,
            role="user",
            content=user_input,
        )
        run = project_client.agents.create_and_process_run(
            thread_id=thread.id, agent_id=agent.id
        )
        messages = project_client.agents.list_messages(thread_id=thread.id)
        print(f"# Agent: {messages.data[0].content[0].text.value}")


if __name__ == "__main__":
    asyncio.run(main())
```

### Alapfogalmak

A Microsoft Foundry Agent Service az alábbi alapfogalmakkal rendelkezik:

- **Ügynök**. A Microsoft Foundry Agent Service integrálódik a Microsoft Foundry platformmal. A Microsoft Foundry-ban egy AI ügynök "okos" mikroszolgáltatásként működik, amely kérdések megválaszolására (RAG), műveletek végrehajtására vagy teljes munkafolyamatok automatizálására használható. Ezt úgy éri el, hogy egyesíti a generatív AI modellek erejét olyan eszközökkel, amelyek lehetővé teszik számára a valós adatok elérését és azokkal való interakciót. Íme egy példa egy ügynökre:

    ```python
    agent = project_client.agents.create_agent(
        model="gpt-5-mini",
        name="my-agent",
        instructions="You are helpful agent",
        tools=code_interpreter.definitions,
        tool_resources=code_interpreter.resources,
    )
    ```

    Ebben a példában egy ügynököt hozunk létre `gpt-5-mini` modellel, `my-agent` névvel és az utasítás `You are helpful agent`. Az ügynök eszközökkel és erőforrásokkal van felszerelve kódértelmezési feladatok végrehajtásához.

- **Szálak és üzenetek**. A szál szintén egy fontos fogalom. Egy szál egy beszélgetést vagy interakciót jelent az ügynök és a felhasználó között. A szálakat arra használják, hogy nyomon kövessék egy beszélgetés előrehaladását, tárolják a kontextusadatokat és kezeljék az interakció állapotát. Íme egy példa egy szálra:

    ```python
    thread = project_client.agents.create_thread()
    message = project_client.agents.create_message(
        thread_id=thread.id,
        role="user",
        content="Could you please create a bar chart for the operating profit using the following data and provide the file to me? Company A: $1.2 million, Company B: $2.5 million, Company C: $3.0 million, Company D: $1.8 million",
    )
    
    # Kérje meg az ügynököt, hogy végezzen munkát a szálon
    run = project_client.agents.create_and_process_run(thread_id=thread.id, agent_id=agent.id)
    
    # Szerezze be és naplózza az összes üzenetet az ügynök válaszának megtekintéséhez
    messages = project_client.agents.list_messages(thread_id=thread.id)
    print(f"Messages: {messages}")
    ```

    Az előző kódban egy szálat hoztunk létre. Ezután egy üzenetet küldtünk a szálnak. A `create_and_process_run` hívásával az ügynököt felkértük, hogy dolgozzon a szálon. Végül az üzeneteket lekértük és naplóztuk az ügynök válaszának megtekintéséhez. Az üzenetek jelzik a beszélgetés előrehaladását a felhasználó és az ügynök között. Fontos megérteni azt is, hogy az üzenetek típusa eltérő lehet, például szöveg, kép vagy fájl, azaz az ügynök munkája lehet például kép vagy szöveges válasz is. Fejlesztőként ezeket az információkat felhasználhatod a válasz további feldolgozására vagy a felhasználó számára történő megjelenítésre.

- **Integráció a Microsoft Agent Frameworkkel**. A Microsoft Foundry Agent Service zökkenőmentesen működik együtt a Microsoft Agent Frameworkkel, tehát az ügynököket a `FoundryChatClient` használatával építheted és az Agent Service-en keresztül telepítheted éles környezetben.

**Használati esetek**: A Microsoft Foundry Agent Service vállalati alkalmazásokra van tervezve, ahol biztonságos, skálázható és rugalmas AI ügynök telepítés szükséges.

## Mi a különbség ezek között a megközelítések között?
 
Úgy hangzik, mintha lenne átfedés, de vannak kulcsfontosságú különbségek a tervezés, képességek és célfelhasználások tekintetében:
 
- **Microsoft Agent Framework (MAF)**: Egy termelésre kész SDK AI ügynökök építéséhez. Egyszerűsített API-t biztosít ügynökök létrehozásához eszközhívással, beszélgetéskezeléssel és Azure azonosítás integrációval.
- **Microsoft Foundry Agent Service**: Egy platform és telepítési szolgáltatás a Microsoft Foundry-ban ügynökök számára. Beépített kapcsolatot biztosít olyan szolgáltatásokhoz, mint az Azure OpenAI, Azure AI Search, Bing Search és kód végrehajtás.
 
Még mindig bizonytalan, melyiket válaszd?

### Használati esetek
 
Nézzük meg, tudunk-e segíteni néhány gyakori alkalmazási eseten keresztül:
 
> K: Termelésre kész AI ügynök alkalmazásokat fejlesztek, és gyorsan szeretnék indulni
>

> V: A Microsoft Agent Framework nagyszerű választás. Egyszerű, Pythonos API-t kínál a `FoundryChatClient` segítségével, amellyel néhány sor kódban definiálhatsz eszközökkel és utasításokkal rendelkező ügynököket.

> K: Vállalati szintű telepítésre van szükségem Azure integrációval, mint a Search és a kód végrehajtás.
>
> V: A Microsoft Foundry Agent Service a legjobb választás. Ez egy platform szolgáltatás, amely több modellre, Azure AI Searchre, Bing Searchre és Azure Functions-re épülő beépített képességeket kínál. Egyszerűvé teszi ügynökeid építését a Foundry Portálon és azok skálázható telepítését.
 
> K: Még mindig bizonytalan vagyok, csak adj egy lehetőséget.
>
> V: Kezdd a Microsoft Agent Frameworkkel az ügynökök építését, majd használd a Microsoft Foundry Agent Service-t, amikor el kell őket telepíteni és skálázni éles környezetben. Ez a megközelítés gyors iterációt tesz lehetővé az ügynök logikáján, miközben egyértelmű utat kínál a vállalati szintű telepítéshez.
 
Foglaljuk össze a kulcsfontosságú különbségeket egy táblázatban:

| Keretrendszer | Fókusz | Alapfogalmak | Használati esetek |
| --- | --- | --- | --- |
| Microsoft Agent Framework | Egyszerűsített ügynök SDK eszközhívással | Ügynökök, Eszközök, Azure Azonosítás | AI ügynökök építése, eszközhasználat, többlépéses munkafolyamatok |
| Microsoft Foundry Agent Service | Rugalmas modellek, vállalati biztonság, kódgenerálás, eszközhívás | Moduláris felépítés, Együttműködés, Folyamatok koordinációja | Biztonságos, skálázható és rugalmas AI ügynök telepítés |

## Integrálhatom közvetlenül a meglévő Azure eszközeimet, vagy szükségem van különálló megoldásokra?


A válasz igen, közvetlenül integrálhatja meglévő Azure ökoszisztéma eszközeit a Microsoft Foundry Agent Service-szel, különösen, mivel az zökkenőmentes együttműködésre lett tervezve más Azure szolgáltatásokkal. Például integrálhatja a Binget, az Azure AI Search-t és az Azure Functions-t. Emellett mély integráció van a Microsoft Foundry-val.

A Microsoft Agent Framework az Azure szolgáltatásokkal is integrálódik a `FoundryChatClient` és az Azure azonosítás révén, lehetővé téve, hogy az Azure szolgáltatásokat közvetlenül az ügynök eszközeiből hívja meg.

## Minta kódok

- Python: [Agent Framework (Microsoft Foundry)](./code_samples/02-python-agent-framework.ipynb)
- Python: [Agent Framework (Azure OpenAI Responses API)](./code_samples/02-python-agent-framework-azure-openai.ipynb)
- .NET: [Agent Framework](./code_samples/02-dotnet-agent-framework.md)

## Van még kérdése az AI Agent Frameworkökkel kapcsolatban?

Csatlakozzon a [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D) csoporthoz, hogy találkozzon más tanulókkal, részt vehessen az irodai órákon, és választ kapjon AI ügynökeihez kapcsolódó kérdéseire.

## Hivatkozások

- <a href="https://techcommunity.microsoft.com/blog/azure-ai-services-blog/introducing-azure-ai-agent-service/4298357" target="_blank">Azure Agent Service</a>
- <a href="https://learn.microsoft.com/azure/ai-services/openai/how-to/responses" target="_blank">Microsoft Agent Framework - Azure OpenAI Responses</a>
- <a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Microsoft Foundry Agent Service</a>

## Előző lecke

[Bevezetés az AI ügynökökbe és azok felhasználási eseteibe](../01-intro-to-ai-agents/README.md)

## Következő lecke

[Az ügynöki tervezési minták megértése](../03-agentic-design-patterns/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Jogi nyilatkozat**:
Ez a dokumentum az AI fordítási szolgáltatás, a [Co-op Translator](https://github.com/Azure/co-op-translator) segítségével készült. Bár az pontosságra törekszünk, kérjük, vegye figyelembe, hogy az automatikus fordítások hibákat vagy pontatlanságokat tartalmazhatnak. Az eredeti dokumentum az anyanyelvén tekintendő hiteles forrásnak. Fontos információk esetén professzionális emberi fordítást javasolunk. Nem vállalunk felelősséget semmilyen félreértésért vagy téves értelmezésért, amely ebből a fordításból ered.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->