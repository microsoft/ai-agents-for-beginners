[![Tervezési Minta](../../../translated_images/hu/lesson-7-thumbnail.f7163ac557bea123.webp)](https://youtu.be/kPfJ2BrBCMY?si=9pYpPXp0sSbK91Dr)

> _(Kattintson fent a képre a lecke videójának megtekintéséhez)_

# Tervezési minták

## Bevezetés

Ez a lecke a következőket fogja tárgyalni

* Egy világos, átfogó cél meghatározását és egy összetett feladat kezelhetőbb részekre bontását.
* Strukturált kimenet kihasználását megbízhatóbb és gép által olvasható válaszokhoz.
* Egy eseményvezérelt megközelítés alkalmazását a dinamikus feladatok és váratlan bemenetek kezelésére.

## Tanulási célok

A lecke elvégzése után a következőket fogja érteni:

* Azonosítani és meghatározni egy átfogó célt egy AI ügynök számára, biztosítva, hogy világosan tudja, mi a követendő cél.
* Összetett feladatot lebontani kezelhető részekre és logikus sorrendbe rendezni azokat.
* Felszerelni az ügynököket a megfelelő eszközökkel (pl. keresőeszközök vagy adat-analitikai eszközök), eldönteni mikor és hogyan használják őket, és kezelni a felmerülő váratlan helyzeteket.
* Értékelni az alfeladatok eredményeit, mérni a teljesítményt, és iterálni a lépéseken a végső kimenet javítása érdekében.

## Az átfogó cél meghatározása és a feladat lebontása

![Célok és feladatok meghatározása](../../../translated_images/hu/defining-goals-tasks.d70439e19e37c47a.webp)

A legtöbb valós feladat túl összetett ahhoz, hogy egyetlen lépésben lehessen megoldani. Egy AI ügynöknek tömör célkitűzésre van szüksége, hogy irányítsa a tervezést és a követendő lépéseket. Például vegyük a célt:

    "Készíts egy 3 napos utazási tervet."

Bár egyszerűen megfogalmazható, finomításra van szükség. Minél világosabb a cél, annál jobban fókuszálhat az ügynök (és az esetleges emberi közreműködők) a kívánt eredmény elérésére, például egy átfogó útiterv létrehozására, benne repülőjárat-opciókkal, szállásajánlásokkal és programjavaslatokkal.

### Feladat lebontása

Nagy vagy összetett feladatok kezelhetőbbekké válnak, ha kisebb, célorientált alfeladatokra bontjuk őket.
Az utazási terv példájánál a célt a következőkre bonthatjuk:

* Repülőjegy foglalás
* Szállás foglalás
* Autókölcsönzés
* Személyre szabás

Minden alfeladattal külön ügynökök vagy folyamatok foglalkozhatnak. Egy ügynök specializálódhat a legjobb repülőjegy ajánlatok keresésére, egy másik a szállásfoglalásra stb. Egy koordináló vagy „leszármazott” ügynök pedig összeállíthatja ezeket az eredményeket egy egységes útitervbe a végfelhasználó számára.

Ez a moduláris megközelítés lehetővé teszi az inkrementális fejlesztést is. Például hozzáadhatunk specializált ügynököket ételajánlásokra vagy helyi programjavaslatokra, és idővel finomíthatjuk az útitervet.

### Strukturált kimenet

A Nagy Nyelvi Modellek (LLM-ek) képesek strukturált kimenetet (pl. JSON) generálni, amely könnyebben feldolgozható a leszármazott ügynökök vagy szolgáltatások számára. Ez különösen hasznos többügynökös környezetben, ahol ezeket a feladatokat a tervezési kimenet fogadása után lehet végrehajtani.

A következő Python kódrészlet bemutat egy egyszerű tervező ügynököt, amely lebont egy célt alfeladatokra és strukturált tervet generál:

```python
from pydantic import BaseModel
from enum import Enum
from typing import List, Optional, Union
import json
import os
from typing import Optional
from pprint import pprint
from agent_framework.foundry import FoundryChatClient
from azure.identity import AzureCliCredential

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
    assigned_agent: AgentEnum  # hozzá akarjuk rendelni a feladatot az ügynökhöz

class TravelPlan(BaseModel):
    main_task: str
    subtasks: List[TravelSubTask]
    is_greeting: bool

provider = FoundryChatClient(
    project_endpoint=os.environ["AZURE_AI_PROJECT_ENDPOINT"],
    model=os.environ["AZURE_AI_MODEL_DEPLOYMENT_NAME"],
    credential=AzureCliCredential(),
)

# Definiáld a felhasználói üzenetet
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

Ebben a példában egy Szemantikus Router ügynök fogadja a felhasználói kérését (pl. "Szállás tervet kérek az utazásomhoz.").

A tervező ezután:

* Fogadja a Szállás Tervet: A tervező veszi a felhasználó üzenetét, és a rendszer prompt alapján (amely tartalmazza az elérhető ügynökök részleteit) strukturált utazási tervet generál.
* Felsorolja az Ügynököket és Eszközeiket: Az ügynökregiszter tartalmaz egy listát az ügynökökről (pl. repülő, szállás, autókölcsönzés, programok) és az általuk kínált funkciókról vagy eszközökről.
* Eljuttatja a Tervet a megfelelő ügynökökhöz: Az alfeladatok számától függően a tervező közvetlenül elküldi az üzenetet egy dedikált ügynöknek (egyetlen feladat esetén), vagy koordinál a csoportchat menedzserrel többügynökös együttműködés esetén.
* Összegzi az Eredményt: Végül a tervező összefoglalja a generált tervet az átláthatóság érdekében.
A következő Python kódminta bemutatja ezeket a lépéseket:

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
    assigned_agent: AgentEnum # hozzá akarjuk rendelni a feladatot az ügynökhöz

class TravelPlan(BaseModel):
    main_task: str
    subtasks: List[TravelSubTask]
    is_greeting: bool
import json
import os
from typing import Optional

from agent_framework.foundry import FoundryChatClient
from azure.identity import AzureCliCredential

# Létrehozni az ügyfelet

provider = FoundryChatClient(
    project_endpoint=os.environ["AZURE_AI_PROJECT_ENDPOINT"],
    model=os.environ["AZURE_AI_MODEL_DEPLOYMENT_NAME"],
    credential=AzureCliCredential(),
)

from pprint import pprint

# Meghatározni a felhasználói üzenetet

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

# Kiírni a választartalmat JSON-ként való betöltés után

pprint(json.loads(response_content))
```

A következő kimenet az előző kód eredménye, ezt a strukturált kimenetet aztán az `assigned_agent` felé irányíthatjuk és összefoglalhatjuk az utazási tervet a végfelhasználónak.

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

Egy példafüzet a fenti kóddal elérhető [itt](./code_samples/07-python-agent-framework.ipynb).

### Iteratív tervezés

Egyes feladatok visszacsatolást vagy újratervezést igényelnek, ahol egy alfeladat eredménye befolyásolja a következőt. Például, ha az ügynök váratlan adatformátummal találkozik repülőjegy foglalás közben, alkalmazkodnia kell stratégiájához mielőtt tovább lép a szállásfoglalásra.

Ezen felül a felhasználói visszajelzés (pl. ha egy ember korábbi járatot részesít előnyben) részleges újratervezést indíthat el. Ez a dinamikus, iteratív megközelítés biztosítja, hogy a végső megoldás megfeleljen a valós korlátoknak és a változó felhasználói igényeknek.

pl. kódminta

```python
import os
from agent_framework.foundry import FoundryChatClient
from azure.identity import AzureCliCredential
#.. ugyanaz, mint az előző kódban, és továbbítja a felhasználó előzményeit, aktuális tervét

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
# .. újratervez és elküldi a feladatokat a megfelelő ügynököknek
```

A komplexebb tervezéshez érdemes megnézni a Magnetic One <a href="https://www.microsoft.com/research/articles/magentic-one-a-generalist-multi-agent-system-for-solving-complex-tasks" target="_blank">blogbejegyzést</a>, amely összetett feladatok megoldására szolgál.

## Összefoglalás

Ebben a cikkben megnéztünk egy példát arra, hogyan hozhatunk létre tervezőt, amely dinamikusan választja ki az elérhető, definiált ügynököket. A tervező kimenete lebontja a feladatokat és hozzárendeli az ügynököket, hogy azok végrehajthatók legyenek. Feltételezzük, hogy az ügynökök hozzáférnek az adott feladat végrehajtásához szükséges funkciókhoz/eszközökhöz. Az ügynökök mellett további mintákat is beemelhetünk, mint reflexió, összefoglaló vagy körkörös chat, hogy testreszabottabbá tegyük a működést.

## További források

Magnetic One - Egy generalista többügynökös rendszer összetett feladatok megoldására, amely számos kihívást jelentő ügynöki benchmarkon kiváló eredményeket ért el. Referencia: <a href="https://www.microsoft.com/research/articles/magentic-one-a-generalist-multi-agent-system-for-solving-complex-tasks" target="_blank">Magnetic One</a>. Ebben a megvalósításban az összehangoló specifikus tervezési terveket hoz létre és delegálja ezeket az elérhető ügynökök számára. A tervezés mellett az összehangoló követési mechanizmust is alkalmaz a feladat előrehaladásának nyomon követésére és szükség szerinti újratervezésére.

### Kérdése van a Tervezési mintákkal kapcsolatban?

Csatlakozzon a [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D) közösséghez, hogy más tanulókkal találkozzon, részt vegyen az irodai órákon és választ kapjon AI ügynökökkel kapcsolatos kérdéseire.

## Előző lecke

[Megbízható AI ügynökök építése](../06-building-trustworthy-agents/README.md)

## Következő lecke

[Többügynökös tervezési minta](../08-multi-agent/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Jogi nyilatkozat**:
Ez a dokumentum az AI fordítási szolgáltatás, a [Co-op Translator](https://github.com/Azure/co-op-translator) segítségével készült. Bár az pontosságra törekszünk, kérjük, vegye figyelembe, hogy az automatikus fordítások hibákat vagy pontatlanságokat tartalmazhatnak. Az eredeti dokumentum az anyanyelvén tekintendő hiteles forrásnak. Fontos információk esetén professzionális emberi fordítást javasolunk. Nem vállalunk felelősséget semmilyen félreértésért vagy téves értelmezésért, amely ebből a fordításból ered.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->