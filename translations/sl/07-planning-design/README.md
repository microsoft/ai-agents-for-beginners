[![Načrtovanje oblikovalskega vzorca](../../../translated_images/sl/lesson-7-thumbnail.f7163ac557bea123.webp)](https://youtu.be/kPfJ2BrBCMY?si=9pYpPXp0sSbK91Dr)

> _(Kliknite na zgornjo sliko za ogled videa tega učnega gradiva)_

# Načrtovanje oblikovalskega vzorca

## Uvod

V tej lekciji bomo obravnavali

* Določitev jasnega splošnega cilja in razdelitev kompleksne naloge na obvladljive podnaloge.
* Izrabo strukturiranega izhoda za bolj zanesljive in strojno berljive odzive.
* Uporabo dogodkovno vodenega pristopa za obravnavo dinamičnih nalog in nepričakovanih vhodov.

## Cilji učenja

Po končani lekciji boste razumeli:

* Kako prepoznati in določiti splošni cilj za AI agenta, da jasno ve, kaj je treba doseči.
* Kako razstaviti kompleksno nalogo na obvladljive podnaloge in jih organizirati v logičen zaporedje.
* Opremljanje agentov s pravimi orodji (npr. orodji za iskanje ali orodji za analitiko podatkov), odločanje, kdaj in kako jih uporabiti, ter obvladovanje nepričakovanih situacij, ki se pojavijo.
* Oceno rezultatov podnalog, merjenje uspešnosti ter ponavljanje akcij za izboljšanje končnega izida.

## Določanje splošnega cilja in razčlenitev naloge

![Določanje ciljev in nalog](../../../translated_images/sl/defining-goals-tasks.d70439e19e37c47a.webp)

Večina nalog v resničnem svetu je preveč kompleksna, da bi jih rešili v enem koraku. AI agent potrebuje jedrnat cilj, ki usmerja njegovo načrtovanje in dejanja. Na primer, razmislimo o cilju:

    "Ustvari tridnevni potovalni načrt."

Čeprav je preprost za izražanje, potrebuje še dopolnitev. Bolj jasen ko je cilj, bolje se lahko agent (in vsi sodelujoči ljudje) osredotočijo na doseganje pravilnega izida, na primer izdelavo celovitega itinerarja z možnostmi letov, priporočili za hotele in predlogi aktivnosti.

### Razčlenitev naloge

Velike ali zapletene naloge postanejo bolj obvladljive, ko jih razdelimo na manjše, ciljno usmerjene podnaloge.
Za primer potovalnega načrta lahko cilj razčlenite na:

* Rezervacija leta
* Rezervacija hotela
* Najem avtomobila
* Personalizacija

Vsako podnalogo lahko obravnavajo namenski agenti ali procesi. En agent se lahko specializira za iskanje najboljših letalskih ponudb, drugi za rezervacije hotelov in tako naprej. Koordinacijski ali »spodnji« agent lahko nato združi te rezultate v enoten načrt za končnega uporabnika.

Ta modularni pristop omogoča tudi postopne izboljšave. Na primer, lahko dodate specializirane agente za priporočila hrane ali lokalne aktivnosti in postopoma izpopolnite načrt.

### Strukturiran izhod

Veliki jezikovni modeli (LLM) lahko ustvarijo strukturiran izhod (npr. JSON), ki ga je lažje razčleniti in obdelati za spodnje agente ali storitve. To je še posebej uporabno v kontekstu več agentov, kjer lahko te naloge izvedemo po prejemu izhoda načrtovanja.

Naslednji Python izsek prikazuje preprost načrtovalni agent, ki razčleni cilj na podnaloge in ustvari strukturiran načrt:

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

# Model potovalne podnaloge
class TravelSubTask(BaseModel):
    task_details: str
    assigned_agent: AgentEnum  # želimo dodeliti nalogo agentu

class TravelPlan(BaseModel):
    main_task: str
    subtasks: List[TravelSubTask]
    is_greeting: bool

provider = FoundryChatClient(
    project_endpoint=os.environ["AZURE_AI_PROJECT_ENDPOINT"],
    model=os.environ["AZURE_AI_MODEL_DEPLOYMENT_NAME"],
    credential=AzureCliCredential(),
)

# Določite sporočilo uporabnika
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

### Načrtovalni agent z večagentno orkestracijo

V tem primeru Semantic Router Agent prejme uporabniški zahtevek (npr. "Potrebujem načrt hotela za svoje potovanje.").

Nato načrtovalec:

* Prejme načrt hotela: Načrtovalec vzame uporabniško sporočilo in na podlagi sistemskega poziva (vključno s podatki o razpoložljivih agentih) ustvari strukturiran potovalni načrt.
* Našteje agente in njihova orodja: Register agentov vsebuje seznam agentov (npr. za letalske prevoze, hotele, najem avtomobila in aktivnosti) skupaj s funkcijami ali orodji, ki jih ponujajo.
* Pošlje načrt pripadajočim agentom: Glede na število podnalog načrtovalec ali neposredno pošlje sporočilo namenskem agentu (za enonamenske scenarije) ali koordinira prek upravljavca skupinskega klepeta za sodelovanje več agentov.
* Povzame izid: Na koncu načrtovalec povzame ustvarjeni načrt za jasnost.
Naslednji primerek kode v Pythonu prikazuje te korake:

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

# Model poti podnaloge

class TravelSubTask(BaseModel):
    task_details: str
    assigned_agent: AgentEnum # Želimo dodeliti nalogo agentu

class TravelPlan(BaseModel):
    main_task: str
    subtasks: List[TravelSubTask]
    is_greeting: bool
import json
import os
from typing import Optional

from agent_framework.foundry import FoundryChatClient
from azure.identity import AzureCliCredential

# Ustvari odjemalca

provider = FoundryChatClient(
    project_endpoint=os.environ["AZURE_AI_PROJECT_ENDPOINT"],
    model=os.environ["AZURE_AI_MODEL_DEPLOYMENT_NAME"],
    credential=AzureCliCredential(),
)

from pprint import pprint

# Določi uporabnikovo sporočilo

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

# Natisni vsebino odgovora po nalaganju v JSON

pprint(json.loads(response_content))
```

Sledi izhod prejšnje kode, ki ga nato lahko uporabite za usmerjanje na `assigned_agent` in povzetek potovalnega načrta za končnega uporabnika.

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

Primer zvezka s prejšnjim primerom kode je na voljo [tukaj](./code_samples/07-python-agent-framework.ipynb).

### Iterativno načrtovanje

Nekatere naloge zahtevajo naprej-nazaj ali ponovni načrt, kjer izid ene podnaloge vpliva na naslednjo. Na primer, če agent med rezervacijo letov odkrije nepričakovano obliko podatkov, se mora morda prilagoditi, preden nadaljuje z rezervacijo hotela.

Poleg tega lahko povratne informacije uporabnika (npr. človek, ki se odloči za zgodnejši let) sprožijo delno ponovni načrt. Ta dinamični, iterativni pristop zagotavlja, da končna rešitev ustreza resničnim omejitvam in spreminjajočim se uporabniškim željam.

npr. vzorčna koda

```python
import os
from agent_framework.foundry import FoundryChatClient
from azure.identity import AzureCliCredential
#.. enako kot prejšnja koda in posreduj zgodovino uporabnika, trenutni načrt

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
# .. ponovno načrtuj in pošlji naloge ustreznim agentom
```

Za bolj celovito načrtovanje si oglejte Magnetic One <a href="https://www.microsoft.com/research/articles/magentic-one-a-generalist-multi-agent-system-for-solving-complex-tasks" target="_blank">Blogpost</a> za reševanje kompleksnih nalog.

## Povzetek

V tem članku smo si ogledali primer, kako lahko ustvarimo načrtovalca, ki lahko dinamično izbere razpoložljive agente. Izhod načrtovalca razčleni naloge in dodeli agente, da jih izvedejo. Predpostavlja se, da imajo agenti dostop do funkcij/orodij, potrebnih za izvedbo naloge. Poleg agentov lahko vključite tudi druge vzorce, kot so refleksija, povzemalnik in krožna komunikacija za nadaljnjo prilagoditev.

## Dodatni viri

Magnetic One - generalni multi-agentni sistem za reševanje kompleksnih nalog, ki je dosegel impresivne rezultate na več zahtevnih agentskih merilih. Referenca: <a href="https://www.microsoft.com/research/articles/magentic-one-a-generalist-multi-agent-system-for-solving-complex-tasks" target="_blank">Magnetic One</a>. V tej implementaciji orkestrator ustvarja načrte za specifične naloge in dodeljuje te naloge razpoložljivim agentom. Poleg načrtovanja orkestrator uporablja tudi mehanizem za sledenje napredku naloge in po potrebi ponovno načrtuje.

### Imate več vprašanj o načrtovanju oblikovalskega vzorca?

Pridružite se [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D), da se povežete z drugimi učenci, se udeležite pisarnkih ur in dobite odgovore na vaša vprašanja o AI agentih.

## Prejšnja lekcija

[Gradnja zaupanja vrednih AI agentov](../06-building-trustworthy-agents/README.md)

## Naslednja lekcija

[Večagentni oblikovalski vzorec](../08-multi-agent/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Omejitev odgovornosti**:
Ta dokument je bil preveden z uporabo AI prevajalske storitve [Co-op Translator](https://github.com/Azure/co-op-translator). Čeprav si prizadevamo za natančnost, vas prosimo, da upoštevate, da avtomatizirani prevodi lahko vsebujejo napake ali netočnosti. Izvirni dokument v njegovem izvirnem jeziku je treba obravnavati kot avtoritativni vir. Za kritične informacije je priporočljiv strokovni človeški prevod. Ne odgovarjamo za morebitna nesporazume ali napačne interpretacije, ki izhajajo iz uporabe tega prevoda.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->