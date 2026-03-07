[![Tervezés – tervezési minta](../../../translated_images/hu/lesson-7-thumbnail.f7163ac557bea123.webp)](https://youtu.be/kPfJ2BrBCMY?si=9pYpPXp0sSbK91Dr)

> _(Kattints a fenti képre a lecke videójának megtekintéséhez)_

# Tervezési minta

## Bevezetés

Ez a lecke a következőket foglalja magában:

* Egy világos, átfogó cél meghatározása és egy összetett feladat kisebb, kezelhető részekre bontása.
* Strukturált kimenet kihasználása a megbízhatóbb és géppel olvasható válaszok érdekében.
* Eseményvezérelt megközelítés alkalmazása dinamikus feladatok és váratlan bemenetek kezelésére.

## Tanulási célok

A lecke elvégzése után a következőket fogod érteni:

* Az AI-ügynök számára egy átfogó cél azonosítása és beállítása, hogy világosan tudja, mit kell elérnie.
* Egy összetett feladat lebontása kezelhető alfeladatokra és ezek logikus sorrendbe rendezése.
* A megfelelő eszközökkel való ellátás (pl. keresőeszközök vagy adatelemzési eszközök), ezek használatának eldöntése és a felmerülő váratlan helyzetek kezelése.
* Az alfeladatok eredményeinek értékelése, a teljesítmény mérése és a műveletek iterálása a végső kimenet javítása érdekében.

## Az általános cél meghatározása és a feladat felbontása

![Célok és feladatok meghatározása](../../../translated_images/hu/defining-goals-tasks.d70439e19e37c47a.webp)

A legtöbb valós feladat túl összetett ahhoz, hogy egyetlen lépésben oldjuk meg. Egy AI-ügynöknek rövid, tömör célt kell adni, amely irányítja a tervezését és műveleteit. Például, tekintsük a célt:

    "Készíts egy 3 napos utazási útitervet."

Bár ez egyszerűen megfogalmazható, további pontosításra szorul. Minél világosabb a cél, annál inkább tud az ügynök (és az esetleges emberi közreműködők) a megfelelő eredmény elérésére koncentrálni, például átfogó útiterv készítésére járatopciókkal, szállásajánlásokkal és programjavaslatokkal.

### Feladatok felbontása

A nagy vagy bonyolult feladatok kezelhetőbbé válnak, ha kisebb, célorientált alfeladatokra bontjuk őket.
Az utazási útiterv példájánál a célt a következőkre lehet bontani:

* Repülőjegy-foglalás
* Szállásfoglalás
* Autóbérlés
* Személyre szabás

Minden alfeladatot külön ügynökök vagy folyamatok kezelhetnek. Egy ügynök specializálódhat a legjobb repülőjegy-ajánlatok keresésére, egy másik a szállásfoglalásokra, és így tovább. Egy koordináló vagy "downstream" ügynök ezután összeállíthatja ezeket az eredményeket egy koherens útitervbe a végfelhasználó számára.

Ez a moduláris megközelítés lehetővé teszi az inkrementális fejlesztéseket is. Például hozzáadhatsz specializált ügynököket ételajánlásokhoz vagy helyi programjavaslatokhoz, és az útitervet idővel tovább finomíthatod.

### Strukturált kimenet

A Nagy nyelvi modellek (LLM-ek) strukturált kimenetet (pl. JSON) tudnak generálni, amelyet könnyebb feldolgozni a downstream ügynökök vagy szolgáltatások számára. Ez különösen hasznos többügynökös környezetben, ahol a tervezési kimenet kézhezvétele után végrehajthatóak a feladatok.

A következő Python részlet egy egyszerű tervező ügynököt mutat be, amely egy célt bont fel alfeladatokra és strukturált tervet generál:

```python
from pydantic import BaseModel
from enum import Enum
from typing import List, Optional, Union
import json
import os
from typing import Optional
from pprint import pprint
from agent_framework.azure import AzureAIProjectAgentProvider
from azure.identity import AzureCliCredential

class AgentEnum(str, Enum):
    FlightBooking = "flight_booking"
    HotelBooking = "hotel_booking"
    CarRental = "car_rental"
    ActivitiesBooking = "activities_booking"
    DestinationInfo = "destination_info"
    DefaultAgent = "default_agent"
    GroupChatManager = "group_chat_manager"

# Utazási részfeladat modell
class TravelSubTask(BaseModel):
    task_details: str
    assigned_agent: AgentEnum  # a feladatot az ügynöknek szeretnénk kiosztani

class TravelPlan(BaseModel):
    main_task: str
    subtasks: List[TravelSubTask]
    is_greeting: bool

provider = AzureAIProjectAgentProvider(credential=AzureCliCredential())

# Határozza meg a felhasználói üzenetet
system_prompt = """You are a planner agent.
    Your job is to decide which agents to run based on the user's request.
    Provide your response in JSON format with the following structure:
{'main_task': 'Plan a family trip from Singapore to Melbourne.',
 'subtasks': [{'assigned_agent': 'flight_booking',
               'task_details': 'Book round-trip flights from Singapore to '
                               'Melbourne.'}
    Below are the available agents specialised in different tasks:
    - FlightBooking: For booking flights and providing flight information
    - HotelBooking: For booking hotels and providing hotel information
    - CarRental: For booking cars and providing car rental information
    - ActivitiesBooking: For booking activities and providing activity information
    - DestinationInfo: For providing information about destinations
    - DefaultAgent: For handling general requests"""

user_message = "Create a travel plan for a family of 2 kids from Singapore to Melbourne"

response = client.create_response(input=user_message, instructions=system_prompt)

response_content = response.output_text
pprint(json.loads(response_content))
```

### Tervező ügynök többügynökös összehangolással

Ebben a példában egy Semantic Router Agent fogad egy felhasználói kérést (pl. "Szükségem van egy szállástervre az utazásomhoz.").

A tervező ezután:

* Megkapja a szállástervet: A tervező felhasználói üzenet alapján, egy rendszer-prompt (beleértve az elérhető ügynök részleteit) segítségével strukturált utazási tervet generál.
* Felsorolja az ügynököket és eszközeiket: Az ügynök-regiszter tartalmazza az ügynökök listáját (pl. repülő, szállás, autóbérlés és aktivitások) és az általuk kínált funkciókat vagy eszközöket.
* A terv útirányozása a megfelelő ügynökökhöz: Az alfeladatok számától függően a tervező vagy közvetlenül egy dedikált ügynöknek küldi az üzenetet (egytaskszcenáriók esetén), vagy csoportos együttműködéshez csevegéskezelőn keresztül koordinál.
* Az eredmény összefoglalása: Végül a tervező összefoglalja a generált tervet az érthetőség kedvéért.
A következő Python kódrészlet illusztrálja ezeket a lépéseket:

```python

from pydantic import BaseModel

from enum import Enum
from typing import List, Optional, Union

class AgentEnum(str, Enum):
    FlightBooking = "flight_booking"
    HotelBooking = "hotel_booking"
    CarRental = "car_rental"
    ActivitiesBooking = "activities_booking"
    DestinationInfo = "destination_info"
    DefaultAgent = "default_agent"
    GroupChatManager = "group_chat_manager"

# Utazási alfeladat modell

class TravelSubTask(BaseModel):
    task_details: str
    assigned_agent: AgentEnum # a feladatot az ügynöknek szeretnénk kiosztani

class TravelPlan(BaseModel):
    main_task: str
    subtasks: List[TravelSubTask]
    is_greeting: bool
import json
import os
from typing import Optional

from agent_framework.azure import AzureAIProjectAgentProvider
from azure.identity import AzureCliCredential

# Hozza létre a klienst

provider = AzureAIProjectAgentProvider(credential=AzureCliCredential())

from pprint import pprint

# Határozza meg a felhasználói üzenetet

system_prompt = """You are a planner agent.
    Your job is to decide which agents to run based on the user's request.
    Below are the available agents specialized in different tasks:
    - FlightBooking: For booking flights and providing flight information
    - HotelBooking: For booking hotels and providing hotel information
    - CarRental: For booking cars and providing car rental information
    - ActivitiesBooking: For booking activities and providing activity information
    - DestinationInfo: For providing information about destinations
    - DefaultAgent: For handling general requests"""

user_message = "Create a travel plan for a family of 2 kids from Singapore to Melbourne"

response = client.create_response(input=user_message, instructions=system_prompt)

response_content = response.output_text

# Írja ki a válasz tartalmát miután JSON-ként betöltötte

pprint(json.loads(response_content))
```

A következő az előző kód kimenete, és ezt a strukturált kimenetet felhasználhatod az `assigned_agent`-hez irányításhoz és az utazási terv összefoglalásához a végfelhasználó számára.

```json
{
    "is_greeting": "False",
    "main_task": "Plan a family trip from Singapore to Melbourne.",
    "subtasks": [
        {
            "assigned_agent": "flight_booking",
            "task_details": "Book round-trip flights from Singapore to Melbourne."
        },
        {
            "assigned_agent": "hotel_booking",
            "task_details": "Find family-friendly hotels in Melbourne."
        },
        {
            "assigned_agent": "car_rental",
            "task_details": "Arrange a car rental suitable for a family of four in Melbourne."
        },
        {
            "assigned_agent": "activities_booking",
            "task_details": "List family-friendly activities in Melbourne."
        },
        {
            "assigned_agent": "destination_info",
            "task_details": "Provide information about Melbourne as a travel destination."
        }
    ]
}
```

A fent említett kódrészletet tartalmazó példafüzet elérhető [itt](07-python-agent-framework.ipynb).

### Iteratív tervezés

Néhány feladat visszacsatolást vagy újratervezést igényel, ahol egy alfeladat eredménye befolyásolja a következőt. Például, ha az ügynök váratlan adatformátumot talál a repülőjegyfoglalás során, módosítania kell a stratégiáját, mielőtt a szállásfoglalásokra továbblépne.

Ezenkívül a felhasználói visszajelzés (pl. egy ember döntése, hogy egy korábbi járatot preferál) részleges újratervezést indíthat el. Ez a dinamikus, iteratív megközelítés biztosítja, hogy a végső megoldás igazodjon a valós világ korlátaihoz és a változó felhasználói preferenciákhoz.

példa kód

```python
from agent_framework.azure import AzureAIProjectAgentProvider
from azure.identity import AzureCliCredential
#.. ugyanaz, mint az előző kód, és továbbadni a felhasználói előzményeket és a jelenlegi tervet

system_prompt = """You are a planner agent to optimize the
    Your job is to decide which agents to run based on the user's request.
    Below are the available agents specialized in different tasks:
    - FlightBooking: For booking flights and providing flight information
    - HotelBooking: For booking hotels and providing hotel information
    - CarRental: For booking cars and providing car rental information
    - ActivitiesBooking: For booking activities and providing activity information
    - DestinationInfo: For providing information about destinations
    - DefaultAgent: For handling general requests"""

user_message = "Create a travel plan for a family of 2 kids from Singapore to Melbourne"

response = client.create_response(
    input=user_message,
    instructions=system_prompt,
    context=f"Previous travel plan - {TravelPlan}",
)
# .. újratervezni és elküldeni a feladatokat a megfelelő ügynököknek
```

Átfogóbb tervezéshez nézd meg a Magnetic One <a href="https://www.microsoft.com/research/articles/magentic-one-a-generalist-multi-agent-system-for-solving-complex-tasks" target="_blank">Blogbejegyzés</a>, amely a komplex feladatok megoldására szolgál.

## Összefoglalás

Ebben a cikkben megnéztünk egy példát arra, hogyan hozhatunk létre egy olyan tervezőt, amely dinamikusan kiválasztja a definiált, elérhető ügynököket. A tervező kimenete felbontja a feladatokat és hozzárendeli az ügynököket, hogy azok végre tudják hajtani azokat. Feltételezzük, hogy az ügynökök hozzáférnek azokhoz a funkciókhoz/eszközökhöz, amelyek a feladat elvégzéséhez szükségesek. Az ügynökök mellett további mintákat is beilleszthetsz, például reflexiót, összegzőt és körkörös csevegést a további testreszabáshoz.

## További források

Magentic One - A Generalist multi-agent system for solving complex tasks és kiváló eredményeket ért el több kihívást jelentő ügynöki benchmarkon. Referencia: <a href="https://www.microsoft.com/research/articles/magentic-one-a-generalist-multi-agent-system-for-solving-complex-tasks" target="_blank">Magentic One</a>. Ebben a megvalósításban az összehangoló feladat-specifikus terveket hoz létre és átadja ezeket az elérhető ügynököknek. A tervezés mellett az összehangoló nyomonkövetési mechanizmust is alkalmaz a feladat előrehaladásának figyelésére és szükség esetén újratervezésre.

### Van még kérdésed a tervezési mintáról?

Csatlakozz a [Microsoft Foundry Discord](https://aka.ms/ai-agents/discord), hogy találkozhass más tanulókkal, részt vehess konzultációs órákon és választ kapj az AI-ügynökökkel kapcsolatos kérdéseidre.

## Előző lecke

[Megbízható AI-ügynökök építése](../06-building-trustworthy-agents/README.md)

## Következő lecke

[Többügynökös tervezési minta](../08-multi-agent/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
Felelősségkizárás:
Ezt a dokumentumot az [Co-op Translator](https://github.com/Azure/co-op-translator) nevű mesterséges intelligencia-alapú fordítószolgáltatással fordítottuk. Bár törekszünk a pontosságra, kérjük, vegye figyelembe, hogy az automatikus fordítások hibákat vagy pontatlanságokat tartalmazhatnak. Az eredeti, forrásnyelvű dokumentum tekintendő a hiteles forrásnak. Kritikus fontosságú információk esetén hivatásos, emberi fordítást javasolunk. Nem vállalunk felelősséget a fordítás használatából eredő félreértésekért vagy téves értelmezésekért.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->