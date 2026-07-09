[![Načrtovanje oblikovalskega vzorca](../../../translated_images/sl/lesson-7-thumbnail.f7163ac557bea123.webp)](https://youtu.be/kPfJ2BrBCMY?si=9pYpPXp0sSbK91Dr)

> _(Kliknite na zgornjo sliko za ogled videa tega poglavja)_

# Načrtovanje oblikovanja

## Uvod

To poglavje bo zajemalo

* Določitev jasnega celostnega cilja in razbitje kompleksne naloge na obvladljive naloge.
* Izrabo strukturiranega izhoda za bolj zanesljive in strojno berljive odgovore.
* Uporabo dogodkovno vodene metode za obravnavo dinamičnih nalog in nepričakovanih vnosov.

## Cilji učenja

Po zaključenem poglavju boste razumeli:

* Prepoznati in določiti celostni cilj za AI agenta, da bo jasno vedel, kaj je treba doseči.
* Razčleniti zahtevno nalogo na obvladljive podnaloge in jih organizirati v logičen zaporedje.
* Opremljati agente z ustreznimi orodji (npr. orodja za iskanje ali analitiko podatkov), odločati, kdaj in kako jih uporabiti ter obravnavati nepričakovane situacije, ki se pojavijo.
* Ocenjevati rezultate podnalog, meriti učinkovitost in ponavljati dejanja za izboljšanje končnega izhoda.

## Določitev celostnega cilja in razbitje naloge

![Določanje ciljev in nalog](../../../translated_images/sl/defining-goals-tasks.d70439e19e37c47a.webp)

Večina nalog iz resničnega sveta je preveč kompleksna, da bi jo obravnavali v enem samem koraku. AI agent potrebuje jedrnat cilj, ki vodi njegovo načrtovanje in dejanja. Na primer, razmislite o cilju:

    "Ustvarite 3-dnevni potovalni načrt."

Čeprav je preprosto izreči, še vedno zahteva rafiniranje. Bolj jasen kot je cilj, bolje se agent (in kateri koli sodelujoči človek) lahko osredotoči na dosego pravilnega izida, kot je ustvarjanje obsežnega načrta s možnostmi letov, priporočili za hotele in predlogi za dejavnosti.

### Razčlenitev naloge

Velike ali zapletene naloge so bolj obvladljive, če jih razdelimo na manjše, ciljno usmerjene podnaloge.
Za primer potovalnega načrta lahko cilj razčlenite na:

* Rezervacija letov
* Rezervacija hotela
* Najem avtomobila
* Personalizacija

Vsako podnalogo lahko nato obravnavajo namenski agenti ali procesi. Eden od agentov se lahko specializira za iskanje najboljših ponudb za lete, drugi se osredotoči na hotelske rezervacije itd. Koordinacijski ali „spodnji“ agent lahko nato združi te rezultate v eno kohezivno potovalno načrtovanje za končnega uporabnika.

Ta modularni pristop omogoča tudi postopne izboljšave. Na primer, lahko dodate specializirane agente za priporočila hrane ali predloge lokalnih dejavnosti in skozi čas izpopolnite načrt.

### Strukturiran izhod

Veliki jezikovni modeli (LLM) lahko ustvarijo strukturiran izhod (npr. JSON), ki ga je lažje razčleniti in obdelati za spodnje agente ali storitve. To je posebej uporabno v večagentnem kontekstu, kjer lahko po prejemu načrta izvedemo te naloge.

Naslednji python primer prikazuje preprost agenta za načrtovanje, ki razčleni cilj na podnaloge in ustvari strukturiran načrt:

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

# Določi uporabnikovo sporočilo
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

### Agent za načrtovanje z večagentno orkestracijo

V tem primeru agent Semantični usmerjevalnik prejme uporabniško zahtevo (npr. "Potrebujem načrt hotela za svoje potovanje.").

Načrtovalec nato:

* Prejme načrt hotela: Načrtovalec vzame sporočilo uporabnika in na podlagi sistemskega poziva (vključno s podatki o razpoložljivih agentih) ustvari strukturiran potovalni načrt.
* Našteje agente in njihova orodja: Register agentov vsebuje seznam agentov (npr. za lete, hotele, najem avtomobila in dejavnosti) skupaj s funkcijami ali orodji, ki jih nudijo.
* Usmeri načrt do ustreznih agentov: Glede na število podnalog načrtovalec ali pošlje sporočilo neposredno namenskim agentom (za enonaložne primere) ali usklajuje prek upravljavca skupinskega klepeta za sodelovanje več agentov.
* Povzame rezultat: Na koncu načrtovalec za jasnost povzame ustvarjeni načrt.
Naslednji python primer kode prikazuje te korake:

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

# Model potovalne podnaloge

class TravelSubTask(BaseModel):
    task_details: str
    assigned_agent: AgentEnum # želimo dodeliti nalogo agentu

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

# Določi sporočilo uporabnika

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

# Natisni vsebino odgovora po nalaganju kot JSON

pprint(json.loads(response_content))
```

Spodaj je izhod prejšnje kode, ki jo nato lahko uporabite kot strukturiran izhod za usmerjanje do `assigned_agent` in povzema potovalni načrt končnemu uporabniku.

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

Primer prenosnika s prejšnjo kodo je na voljo [tukaj](./code_samples/07-python-agent-framework.ipynb).

### Iterativno načrtovanje

Nekatere naloge zahtevajo izmenjavo ali ponovno načrtovanje, kjer rezultat ene podnaloge vpliva na naslednjo. Na primer, če agent odkrije nepričakovano obliko podatkov pri rezervaciji letov, se bo morda moral prilagoditi, preden nadaljuje z rezervacijo hotela.

Poleg tega lahko povratne informacije uporabnika (npr. človek, ki se odloči za zgodnejši let) sprožijo delno ponovno načrtovanje. Ta dinamičen, iterativen pristop zagotavlja, da končna rešitev ustreza realnim omejitvam in spreminjajočim se uporabniških željam.

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
# .. načrtuj znova in pošlji naloge ustreznim agentom
```

Za bolj celovito načrtovanje si oglejte Magnetic One <a href="https://www.microsoft.com/research/articles/magentic-one-a-generalist-multi-agent-system-for-solving-complex-tasks" target="_blank">Blogpost</a> za reševanje kompleksnih nalog.

## Povzetek

V tem članku smo si ogledali primer, kako ustvariti načrtovalca, ki lahko dinamično izbere razpoložljive agente. Izhod načrtovalca razčleni naloge in dodeli agente za izvedbo. Predvideva se, da imajo agenti dostop do funkcij/orodij, potrebnih za opravljanje naloge. Poleg agentov lahko vključite tudi druge vzorce, kot so refleksija, povzemalec in round robin klepet za nadaljnjo prilagoditev.

## Dodatni viri

Magnetic One - Splošen večagentni sistem za reševanje kompleksnih nalog, ki je dosegel impresivne rezultate na več zahtevnih agenčnih merilih. Referenca: <a href="https://www.microsoft.com/research/articles/magentic-one-a-generalist-multi-agent-system-for-solving-complex-tasks" target="_blank">Magnetic One</a>. V tej implementaciji orkestrator ustvarja nalogam specifične načrte in delegira te naloge razpoložljivim agentom. Poleg načrtovanja orkestrator uporablja tudi mehanizem sledenja za spremljanje napredka naloge in po potrebi ponovno načrtuje.

### Imate več vprašanj o vzorcu načrtovanja?

Pridružite se [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D), da spoznate druge učence, se udeležite ur uradnega svetovanja in dobite odgovore na svoja vprašanja o AI agentih.

## Prejšnje poglavje

[Gradnja zanesljivih AI agentov](../06-building-trustworthy-agents/README.md)

## Naslednje poglavje

[Večagentni oblikovalski vzorec](../08-multi-agent/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Omejitev odgovornosti**:
Ta dokument je bil preveden z uporabo AI prevajalske storitve [Co-op Translator](https://github.com/Azure/co-op-translator). Čeprav si prizadevamo za natančnost, vas prosimo, da upoštevate, da avtomatizirani prevodi lahko vsebujejo napake ali netočnosti. Izvirni dokument v njegovem izvirnem jeziku je treba obravnavati kot avtoritativni vir. Za kritične informacije je priporočljiv strokovni človeški prevod. Ne odgovarjamo za morebitna nesporazume ali napačne interpretacije, ki izhajajo iz uporabe tega prevoda.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->