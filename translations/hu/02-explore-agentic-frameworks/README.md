[![AI Ügynök Keretrendszerek Felfedezése](../../../translated_images/hu/lesson-2-thumbnail.c65f44c93b8558df.webp)](https://youtu.be/ODwF-EZo_O8?si=1xoy_B9RNQfrYdF7)

> _(Kattintson a fenti képre a lecke videójának megtekintéséhez)_

# AI Ügynök Keretrendszerek Felfedezése

Az AI ügynök keretrendszerek olyan szoftverplatformok, amelyeket az AI ügynökök létrehozásának, telepítésének és kezelésének egyszerűsítésére terveztek. Ezek a keretrendszerek előre elkészített komponenseket, absztrakciókat és eszközöket biztosítanak a fejlesztők számára, amelyek leegyszerűsítik a komplex AI rendszerek fejlesztését.

Ezek a keretrendszerek segítik a fejlesztőket abban, hogy az alkalmazások egyedi szempontjaira koncentrálhassanak, szabványosított megközelítéseket kínálva az AI ügynök fejlesztésében felmerülő általános kihívásokhoz. Növelik a skálázhatóságot, elérhetőséget és hatékonyságot az AI rendszerek építése során.

## Bevezetés

Ebben a leckében a következőkről lesz szó:

- Mik az AI Ügynök Keretrendszerek és mit tesznek lehetővé a fejlesztők számára?
- Hogyan használhatják a csapatok ezeket az ügynök képességeinek gyors prototípuskészítésére, iterálására és javítására?
- Milyen különbségek vannak a Microsoft által készített keretrendszerek és eszközök között (<a href="https://aka.ms/ai-agents-beginners/ai-agent-service" target="_blank">Azure AI Agent Service</a> és a <a href="https://learn.microsoft.com/azure/ai-services/openai/how-to/responses" target="_blank">Microsoft Agent Framework</a>)?
- Integrálhatom-e közvetlenül a meglévő Azure ökoszisztéma eszközeimet, vagy különálló megoldásokra van szükségem?
- Mi az az Azure AI Agents szolgáltatás, és hogyan segít nekem?

## Tanulási célok

Ennek a leckének a célja, hogy megértsd:

- Az AI Ügynök Keretrendszerek szerepét az AI fejlesztésében.
- Hogyan használhatók az AI Ügynök Keretrendszerek intelligens ügynökök építésére.
- Az AI Ügynök Keretrendszerek által lehetővé tett kulcsfontosságú képességek.
- A Microsoft Agent Framework és az Azure AI Agent Service közötti különbségek.

## Mik az AI Ügynök Keretrendszerek és mit tesznek lehetővé a fejlesztők számára?

A hagyományos AI keretrendszerek segítenek integrálni az AI-t az alkalmazásaidba, és az alkalmazásokat az alábbi módokon teszik jobbá:

- **Személyre szabás**: Az AI képes elemezni a felhasználói viselkedést és preferenciákat, hogy személyre szabott ajánlásokat, tartalmakat és élményeket nyújtson.
Példa: A Netflixhez hasonló streaming szolgáltatások AI-t használnak, hogy az előzmények alapján javasoljanak filmeket és műsorokat, növelve a felhasználók elköteleződését és elégedettségét.
- **Automatizálás és Hatékonyság**: Az AI automatizálhatja az ismétlődő feladatokat, egyszerűsíti a munkafolyamatokat, és javítja a működési hatékonyságot.
Példa: Az ügyfélszolgálati alkalmazások AI-alapú chatbotokat használnak az általános kérdések kezelésére, csökkentve a válaszadási időt és felszabadítva az emberi ügynököket a bonyolultabb ügyekhez.
- **Fejlesztett Felhasználói Élmény**: Az AI javítja az összesített felhasználói élményt intelligens funkciókkal, például hangfelismeréssel, természetes nyelvfeldolgozással és előrejelző szöveggel.
Példa: Az olyan virtuális asszisztensek, mint a Siri és a Google Assistant, AI segítségével értik meg és válaszolják meg a hangutasításokat, megkönnyítve ezzel a felhasználók eszközökkel való interakcióját.

### Ez mind szuper, de akkor miért van szükség az AI Ügynök Keretrendszerre?

Az AI ügynök keretrendszerek többet jelentenek, mint csupán AI keretrendszerek. Olyan intelligens ügynökök létrehozását teszik lehetővé, amelyek képesek felhasználókkal, más ügynökökkel és a környezettel interakcióba lépni meghatározott célok elérése érdekében. Ezek az ügynökök autonóm viselkedést tanúsíthatnak, döntéseket hozhatnak és alkalmazkodhatnak a változó körülményekhez. Nézzük néhány kulcsfontosságú képességüket, amelyeket az AI Ügynök Keretrendszerek tesznek lehetővé:

- **Ügynöki Együttműködés és Koordináció**: Lehetővé teszik több AI ügynök létrehozását, amelyek együtt tudnak dolgozni, kommunikálni és koordinálni a komplex feladatok megoldását.
- **Feladat Automatizálás és Menedzsment**: Mechanizmusokat kínálnak több lépésből álló munkafolyamatok automatizálására, feladat delegálásra és dinamikus feladatkezelésre az ügynökök között.
- **Kontekstusértés és Alkalmazkodás**: Felruházza az ügynököket azzal a képességgel, hogy megértsék a kontextust, alkalmazkodjanak a változó környezethez, és valós idejű információk alapján hozzanak döntéseket.

Összefoglalva, az ügynökök lehetővé teszik, hogy többet tegyél, az automatizálást magasabb szintre emeld, és intelligensebb rendszereket hozz létre, amelyek képesek alkalmazkodni és tanulni a környezetükből.

## Hogyan lehet gyorsan prototípust készíteni, iterálni és javítani az ügynök képességeit?

Ez egy gyorsan változó terület, de vannak olyan közös elemek a legtöbb AI Ügynök Keretrendszerben, amelyek segítenek a gyors prototípuskészítésben és iterációban, nevezetesen a moduláris komponensek, együttműködési eszközök és valós idejű tanulás. Nézzük meg ezeket:

- **Használj Moduláris Komponenseket**: Az AI SDK-k előre elkészített komponenseket kínálnak, például AI és memória csatlakozókat, természetes nyelv vagy kód plugineken keresztüli függvényhívásokat, üzenet sablonokat és még sok mást.
- **Használj Együttműködési Eszközöket**: Tervezzen ügynököket speciális szerepekkel és feladatokkal, lehetővé téve számukra, hogy teszteljék és finomítsák az együttműködési munkafolyamatokat.
- **Tanulj Valós Időben**: Valósíts meg olyan visszacsatolási köröket, ahol az ügynökök a kölcsönhatásokból tanulnak és dinamikusan módosítják a viselkedésüket.

### Használj Moduláris Komponenseket

Az olyan SDK-k, mint a Microsoft Agent Framework, előre elkészített komponenseket kínálnak, például AI csatlakozókat, eszközdefiníciókat és ügynökkezelést.

**Hogyan használhatják a csapatok**: A csapatok gyorsan összeállíthatják ezeket a komponenseket, hogy funkcionális prototípust hozzanak létre anélkül, hogy a nulláról kezdenének, lehetővé téve így a gyors kísérletezést és iterációt.

**Hogyan működik a gyakorlatban**: Használhatsz egy előre elkészített elemzőt az információk kinyerésére a felhasználói bemenetből, egy memória modult az adatok tárolására és visszakeresésére, valamint egy prompt generátort a felhasználókkal való interakcióhoz, mindezt anélkül, hogy ezeket a komponenseket a nulláról kellene felépíteni.

**Példa kód**. Nézzünk egy példát arra, hogyan használhatod a Microsoft Agent Framework-öt az `AzureAIProjectAgentProvider`-rel, hogy a modell eszközhívással válaszoljon a felhasználói bemenetekre:

``` python
# Microsoft Agent Framework Python példa

import asyncio
import os
from typing import Annotated

from agent_framework.azure import AzureAIProjectAgentProvider
from azure.identity import AzureCliCredential


# Definiáljon egy mintafüggvényt az utazás foglalásához
def book_flight(date: str, location: str) -> str:
    """Book travel given location and date."""
    return f"Travel was booked to {location} on {date}"


async def main():
    provider = AzureAIProjectAgentProvider(credential=AzureCliCredential())
    agent = await provider.create_agent(
        name="travel_agent",
        instructions="Help the user book travel. Use the book_flight tool when ready.",
        tools=[book_flight],
    )

    response = await agent.run("I'd like to go to New York on January 1, 2025")
    print(response)
    # Példa kimenet: Az Ön New Yorkba tartó járata 2025. január 1-jére sikeresen lefoglalva. Kellemes utazást! ✈️🗽


if __name__ == "__main__":
    asyncio.run(main())
```

Ebben a példában látható, hogyan használhatsz előre elkészített elemzőt a felhasználói bemenetből származó kulcsfontosságú információk, például az eredeti hely, célállomás és dátum kinyerésére egy repülőjegy foglalási kérésnél. Ez a moduláris megközelítés lehetővé teszi, hogy a magas szintű logikára koncentrálj.

### Használj Együttműködési Eszközöket

Az olyan keretrendszerek, mint a Microsoft Agent Framework, megkönnyítik több ügynök létrehozását, amelyek együtt tudnak dolgozni.

**Hogyan használhatják a csapatok**: A csapatok olyan ügynököket tervezhetnek, amelyek speciális szerepekkel és feladatokkal rendelkeznek, lehetővé téve számukra, hogy teszteljék és finomítsák az együttműködési munkafolyamatokat, valamint javítsák a rendszer hatékonyságát.

**Hogyan működik a gyakorlatban**: Létrehozhatsz egy ügynökcsapatot, ahol minden ügynök specializált funkciót lát el, például adatlekérést, elemzést vagy döntéshozatalt. Ezek az ügynökök kommunikálnak és megosztják az információkat egy közös cél elérése érdekében, például egy felhasználói kérdés megválaszolása vagy egy feladat elvégzése érdekében.

**Példa kód (Microsoft Agent Framework)**:

```python
# Több, együttműködő ügynök létrehozása a Microsoft Agent Framework használatával

import os
from agent_framework.azure import AzureAIProjectAgentProvider
from azure.identity import AzureCliCredential

provider = AzureAIProjectAgentProvider(credential=AzureCliCredential())

# Adatlekérő ügynök
agent_retrieve = await provider.create_agent(
    name="dataretrieval",
    instructions="Retrieve relevant data using available tools.",
    tools=[retrieve_tool],
)

# Adatelemző ügynök
agent_analyze = await provider.create_agent(
    name="dataanalysis",
    instructions="Analyze the retrieved data and provide insights.",
    tools=[analyze_tool],
)

# Futtassa az ügynököket egymás után egy feladaton
retrieval_result = await agent_retrieve.run("Retrieve sales data for Q4")
analysis_result = await agent_analyze.run(f"Analyze this data: {retrieval_result}")
print(analysis_result)
```

Az előző kódban azt látod, hogyan hozhatsz létre egy feladatot, amely több ügynök együttműködését igényli adat elemzésére. Minden ügynök speciális funkciót lát el, és a feladat végrehajtása az ügynökök koordinálásával történik a kívánt eredmény eléréséhez. Dedikált ügynökök létrehozásával és specializált szerepeik kiosztásával javíthatod a feladat hatékonyságát és teljesítményét.

### Tanulj Valós Időben

A fejlett keretrendszerek valós idejű kontextusértést és alkalmazkodást is biztosítanak.

**Hogyan használhatják a csapatok**: A csapatok visszacsatolási köröket valósíthatnak meg, ahol az ügynökök a kölcsönhatásokból tanulnak, és dinamikusan módosítják viselkedésüket, amely folyamatos fejlesztéshez és képesség finomításhoz vezet.

**Hogyan működik a gyakorlatban**: Az ügynökök elemezhetik a felhasználói visszajelzéseket, környezeti adatokat és a feladatok eredményeit, hogy frissítsék tudásbázisukat, módosítsák döntési algoritmusaikat és javítsák teljesítményüket az idő múlásával. Ez az iteratív tanulási folyamat lehetővé teszi, hogy az ügynökök alkalmazkodjanak a változó körülményekhez és a felhasználói igényekhez, növelve a rendszer hatékonyságát.

## Milyen különbségek vannak a Microsoft Agent Framework és az Azure AI Agent Service között?

Számos szempontból összehasonlíthatóak ezek a megközelítések, de nézzük meg néhány kulcsfontosságú különbséget a tervezés, képességek és célfelhasználás szempontjából:

## Microsoft Agent Framework (MAF)

A Microsoft Agent Framework egy egyszerűsített SDK-t biztosít AI ügynökök építéséhez az `AzureAIProjectAgentProvider` használatával. Lehetővé teszi a fejlesztők számára az Azure OpenAI modellek felhasználását eszközhívással, beszélgetés-kezeléssel és vállalati szintű biztonsággal az Azure identitáson keresztül.

**Felhasználási esetek**: Termelésre kész AI ügynökök építése eszközhasználattal, többlépéses munkafolyamatokkal és vállalati integrációs forgatókönyvekkel.

Néhány fontos alapfogalom a Microsoft Agent Framework-ben:

- **Ügynökök**. Egy ügynököt az `AzureAIProjectAgentProvider` hoz létre, beállítva névvel, utasításokkal és eszközökkel. Az ügynök:
  - **Feldolgozza a felhasználói üzeneteket** és válaszokat generál az Azure OpenAI modellekkel.
  - **Automatikusan hív eszközöket** a beszélgetés kontextusa alapján.
  - **Fenntartja a beszélgetés állapotát** több interakción keresztül.

  Íme egy kódrészlet, amely bemutatja egy ügynök létrehozását:

    ```python
    import os
    from agent_framework.azure import AzureAIProjectAgentProvider
    from azure.identity import AzureCliCredential

    provider = AzureAIProjectAgentProvider(credential=AzureCliCredential())
    agent = await provider.create_agent(
        name="my_agent",
        instructions="You are a helpful assistant.",
    )

    response = await agent.run("Hello, World!")
    print(response)
    ```

- **Eszközök**. A keretrendszer támogatja, hogy az eszközöket Python funkciókként definiáld, amelyeket az ügynök automatikusan meghívhat. Az eszközök regisztrálásra kerülnek az ügynök létrehozásakor:

    ```python
    def get_weather(location: str) -> str:
        """Get the current weather for a location."""
        return f"The weather in {location} is sunny, 72\u00b0F."

    agent = await provider.create_agent(
        name="weather_agent",
        instructions="Help users check the weather.",
        tools=[get_weather],
    )
    ```

- **Több Ügynök Koordinációja**. Több, különböző specializációval rendelkező ügynök hozható létre és koordinálható:

    ```python
    planner = await provider.create_agent(
        name="planner",
        instructions="Break down complex tasks into steps.",
    )

    executor = await provider.create_agent(
        name="executor",
        instructions="Execute the planned steps using available tools.",
        tools=[execute_tool],
    )

    plan = await planner.run("Plan a trip to Paris")
    result = await executor.run(f"Execute this plan: {plan}")
    ```

- **Azure Identitás Integráció**. A keretrendszer az `AzureCliCredential` (vagy `DefaultAzureCredential`) használatával biztonságos, kulcs nélküli hitelesítést biztosít, így nem szükséges API kulcsokat kezelni közvetlenül.

## Azure AI Agent Service

Az Azure AI Agent Service egy újabb szolgáltatás, amelyet a Microsoft Ignite 2024-en mutattak be. Lehetővé teszi AI ügynökök fejlesztését és telepítését rugalmasabb modellekkel, például közvetlenül hívható nyílt forráskódú LLM-ekkel, mint a Llama 3, Mistral és Cohere.

Az Azure AI Agent Service erősebb vállalati biztonsági mechanizmusokat és adattárolási módszereket kínál, így alkalmas vállalati alkalmazásokhoz.

Kész azonnal működésre a Microsoft Agent Framework-kel az ügynökök építéséhez és telepítéséhez.

Jelenleg nyilvános előzetes verzióban érhető el, és támogatja a Python és C# nyelveket az ügynökök építéséhez.

Az Azure AI Agent Service Python SDK használatával létrehozhatunk egy olyan ügynököt, amely felhasználó által definiált eszközt használ:

```python
import asyncio
from azure.identity import DefaultAzureCredential
from azure.ai.projects import AIProjectClient

# Eszközfüggvények definiálása
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
        model="gpt-4o-mini",
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

Az Azure AI Agent Service alapfogalmai:

- **Ügynök**. Az Azure AI Agent Service integrálódik a Microsoft Foundry-val. Az AI Foundry-n belül egy AI Ügynök "okos" mikroszolgáltatásként működik, amely képes kérdések megválaszolására (RAG), műveletek végrehajtására vagy teljes munkafolyamatok automatizálására. Ezt a generatív AI modellek és az eszközök kombinációjával éri el, amelyek lehetővé teszik számára, hogy valós adatforrásokat érjen el és kezeljen. Íme egy példa egy ügynökre:

    ```python
    agent = project_client.agents.create_agent(
        model="gpt-4o-mini",
        name="my-agent",
        instructions="You are helpful agent",
        tools=code_interpreter.definitions,
        tool_resources=code_interpreter.resources,
    )
    ```

    Ebben a példában egy „gpt-4o-mini” modellből, egy „my-agent” nevű és egy „You are helpful agent” utasításokkal rendelkező ügynök jön létre. Az ügynök eszközökkel és erőforrásokkal van felszerelve kódértelmezési feladatok végrehajtásához.

- **Szál és üzenetek**. A szál egy másik fontos fogalom. Egy beszélgetést vagy interakciót jelöl egy ügynök és egy felhasználó között. A szálak segítségével nyomon követhető a beszélgetés előrehaladása, tárolható a kontextus és kezelhető az interakció állapota. Íme egy példa egy szál létrehozására:

    ```python
    thread = project_client.agents.create_thread()
    message = project_client.agents.create_message(
        thread_id=thread.id,
        role="user",
        content="Could you please create a bar chart for the operating profit using the following data and provide the file to me? Company A: $1.2 million, Company B: $2.5 million, Company C: $3.0 million, Company D: $1.8 million",
    )
    
    # Ask the agent to perform work on the thread
    run = project_client.agents.create_and_process_run(thread_id=thread.id, agent_id=agent.id)
    
    # Fetch and log all messages to see the agent's response
    messages = project_client.agents.list_messages(thread_id=thread.id)
    print(f"Messages: {messages}")
    ```

    Az előző kódban létrejön egy szál. Ezt követően üzenetet küldenek a szálra. A `create_and_process_run` hívással az ügynöktől kérik a munkavégzést a szálon. Végül az üzenetek lekérése és naplózása történik az ügynök válaszának megtekintéséhez. Az üzenetek jelezhetik a beszélgetés előrehaladását a felhasználó és az ügynök között. Fontos megérteni, hogy az üzenetek különböző típusúak lehetnek, például szöveg, kép vagy fájl, vagyis az ügynök munkája eredményezhet például képet vagy szöveges választ. Fejlesztőként ezeket az információkat tovább feldolgozhatod vagy megjelenítheted a felhasználónak.

- **Integráció a Microsoft Agent Framework-kel**. Az Azure AI Agent Service zökkenőmentesen működik együtt a Microsoft Agent Framework-kel, ami azt jelenti, hogy az `AzureAIProjectAgentProvider` használatával építhetsz ügynököket, majd a Service-en keresztül telepítheted azokat termelési környezetben.

**Felhasználási esetek**: Az Azure AI Agent Service vállalati alkalmazásokra lett tervezve, amelyek biztonságos, skálázható és rugalmas AI ügynök telepítést igényelnek.

## Mi a különbség ezek között a megközelítések között?

Úgy tűnik, hogy van átfedés, de néhány kulcsfontosságú különbség van a tervezés, képességek és célfelhasználások terén:

- **Microsoft Agent Framework (MAF)**: Termelésre kész SDK AI ügynökök építésére. Egyszerű, eszközhívással, beszélgetés-kezeléssel és Azure identitás integrációval rendelkező API-t biztosít.
- **Azure AI Agent Service**: Platform és telepítési szolgáltatás az Azure Foundry-ban ügynökök számára. Beépített kapcsolódást kínál olyan szolgáltatásokhoz, mint az Azure OpenAI, Azure AI Search, Bing Search és kódvégrehajtás.

Még mindig nem vagy biztos, melyiket válaszd?

### Felhasználási esetek

Nézzük meg, hogyan segíthetünk néhány gyakori esettel:

> Kérdés: Termelésbe szánt AI ügynök alkalmazásokat építek, és gyorsan szeretnék kezdeni.
>

>Válasz: A Microsoft Agent Framework nagyszerű választás. Egyszerű, Pythonos API-t biztosít az `AzureAIProjectAgentProvider`-en keresztül, amely lehetővé teszi eszközökkel és utasításokkal rendelkező ügynökök definiálását néhány sor kódban.

>Kérdés: Vállalati szintű telepítésre van szükségem Azure integrációkkal, mint a Search és kódvégrehajtás.
>
> Válasz: Az Azure AI Agent Service a legjobb választás. Egy platform szolgáltatás, amely több modellhez, Azure AI Search-hoz, Bing Search-hoz és Azure Functions-hoz nyújt beépített képességeket. Könnyen létrehozhatod az ügynökeidet a Foundry Portálban, és skálázhatóan telepítheted azokat.
 
> Kérdés: Még mindig bizonytalan vagyok, csak mondd melyiket válasszam.
>
> Válasz: Kezdd a Microsoft Agent Framework-kel az ügynökök építését, majd használd az Azure AI Agent Service-t, amikor telepíteni és skálázni akarod őket termelésben. Ez a megközelítés lehetővé teszi, hogy gyorsan iterálj az ügynök logikáján, miközben világos utat ad a vállalati telepítéshez.
 
Összefoglalva a legfontosabb különbségek táblázatban:

| Keretrendszer | Fókusz | Alapfogalmak | Felhasználási esetek |
| --- | --- | --- | --- |
| Microsoft Agent Framework | Egyszerűsített ügynök SDK eszközhívással | Ügynökök, Eszközök, Azure identitás | AI ügynökök építése, eszközhasználat, többlépéses munkafolyamatok |
| Azure AI Agent Service | Rugalmas modellek, vállalati biztonság, kódgenerálás, eszközhívás | Modularitás, Együttműködés, Folyamat menedzsment | Biztonságos, skálázható és rugalmas AI ügynök telepítés |

## Integrálhatom-e közvetlenül a meglévő Azure ökoszisztéma eszközeimet, vagy különálló megoldásokra van szükségem?
A válasz igen, integrálhatja meglévő Azure ökoszisztéma eszközeit közvetlenül az Azure AI Agent Service-szel, különösen mivel az zökkenőmentes együttműködésre lett tervezve más Azure szolgáltatásokkal. Például integrálhatja a Binget, az Azure AI Search-t és az Azure Functions-t. Van továbbá mély integráció a Microsoft Foundry-val is.

A Microsoft Agent Framework szintén integrálódik az Azure szolgáltatásokkal az `AzureAIProjectAgentProvider` és az Azure identitás segítségével, lehetővé téve, hogy az Azure szolgáltatásokat közvetlenül az agent eszközeiből hívja meg.

## Példa kódok

- Python: [Agent Framework](./code_samples/02-python-agent-framework.ipynb)
- .NET: [Agent Framework](./code_samples/02-dotnet-agent-framework.md)

## További kérdése van az AI Agent Frameworkökkel kapcsolatban?

Csatlakozzon a [Microsoft Foundry Discord](https://aka.ms/ai-agents/discord) csatornához, hogy találkozzon más tanulókkal, részt vegyen irodai órákon, és választ kapjon AI Agent kérdéseire.

## Források

- <a href="https://techcommunity.microsoft.com/blog/azure-ai-services-blog/introducing-azure-ai-agent-service/4298357" target="_blank">Azure Agent Service</a>
- <a href="https://learn.microsoft.com/azure/ai-services/openai/how-to/responses" target="_blank">Microsoft Agent Framework - Azure OpenAI válaszok</a>
- <a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Azure AI Agent szolgáltatás</a>

## Korábbi lecke

[Bevezetés az AI Agentekbe és az Agent használati esetekbe](../01-intro-to-ai-agents/README.md)

## Következő lecke

[Agentikus tervezési minták megértése](../03-agentic-design-patterns/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Jogi Nyilatkozat**:  
Ez a dokumentum az AI fordító szolgáltatás [Co-op Translator](https://github.com/Azure/co-op-translator) segítségével készült. Bár a pontosságra törekszünk, kérjük, vegye figyelembe, hogy az automatikus fordítások hibákat vagy pontatlanságokat tartalmazhatnak. Az eredeti dokumentum az anyanyelvén tekintendő hiteles forrásnak. Fontos információk esetén szakmai, emberi fordítást javaslunk. Nem vállalunk felelősséget a fordítás használatából eredő félreértésekért vagy téves értelmezésekért.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->