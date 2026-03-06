[![Načrtovalni vzorec](../../../translated_images/sl/lesson-7-thumbnail.f7163ac557bea123.webp)](https://youtu.be/kPfJ2BrBCMY?si=9pYpPXp0sSbK91Dr)

> _(Kliknite na zgornjo sliko za ogled videa te lekcije)_

# Načrtovanje zasnove

## Uvod

Ta lekcija bo zajemala

* Določitev jasnega splošnega cilja in razčlenitev zahtevne naloge na obvladljive podnaloge.
* Izrabo strukturiranega izhoda za bolj zanesljive in z računalnikom berljive odgovore.
* Uporabo pristopa, ki temelji na dogodkih za obravnavo dinamičnih nalog in nepričakovanih vhodov.

## Cilji učenja

Po zaključku te lekcije boste razumeli:

* Kako prepoznati in določiti splošni cilj za AI agenta, da bo jasno vedel, kaj je treba doseči.
* Kako razčleniti zahtevno nalogo na obvladljive podnaloge in jih organizirati v logični zaporedju.
* Kako opremiti agente z ustreznimi orodji (npr. iskalna orodja ali orodja za analitiko podatkov), kdaj in kako jih uporabljati ter kako se spopadati z nepričakovanimi situacijami.
* Kako oceniti rezultate podnalog, meriti učinkovitost in ponavljati dejavnosti za izboljšanje končnega izhoda.

## Določitev splošnega cilja in razčlenitev naloge

![Določitev ciljev in nalog](../../../translated_images/sl/defining-goals-tasks.d70439e19e37c47a.webp)

Večina nalog v resničnem svetu je preveč zapletena, da bi jih rešili v enem samem koraku. AI agent potrebuje jedrnat cilj, ki ga vodi pri načrtovanju in dejanjih. Na primer, razmislite o cilju:

    "Ustvari tridnevni potovalni načrt."

Čeprav je enostaven za izražanje, ga je še vedno treba natančneje opredeliti. Bolj ko je cilj jasen, bolje se agent (in morebitni človeški sodelavci) lahko osredotoči na dosego pravilnega izida, kot je ustvarjanje celovitega načrta z možnostmi letov, priporočili za hotele in predlogi aktivnosti.

### Razčlenitev naloge

Velike ali zapletene naloge postanejo obvladljivejše, ko jih razdelimo na manjše, ciljno usmerjene podnaloge.
Za primer potovalnega načrta bi lahko cilj razčlenili na:

* Rezervacija leta
* Rezervacija hotela
* Najem avtomobila
* Prilagajanje

Vsako podnalogo lahko nato obravnavajo namenski agenti ali procesi. Eden od agentov se morda specializira za iskanje najboljših ponudb letov, drugi se osredotoča na rezervacije hotelov itd. Koordinacijski ali »spodnji« agent lahko nato združi te rezultate v enoten načrt za končnega uporabnika.

Ta modularni pristop omogoča tudi postopne izboljšave. Na primer, lahko dodate specializirane agente za priporočila hrane ali predloge lokalnih aktivnosti ter skozi čas natančneje prilagajate načrt.

### Strukturiran izhod

Veliki jezikovni modeli (LLM) lahko generirajo strukturiran izhod (npr. JSON), ki ga je lažje razbrati in obdelati za spodnje agente ali storitve. To je še posebej uporabno v kontekstu več agentov, kjer lahko izvajamo te naloge po prejemu načrta.

Naslednji fragment kode v Pythonu prikazuje preprost načrtovalni agent, ki razčleni cilj v podnaloge in generira strukturiran načrt:

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

# Model podnaloge za potovanje
class TravelSubTask(BaseModel):
    task_details: str
    assigned_agent: AgentEnum  # želimo dodeliti nalogo agentu

class TravelPlan(BaseModel):
    main_task: str
    subtasks: List[TravelSubTask]
    is_greeting: bool

provider = AzureAIProjectAgentProvider(credential=AzureCliCredential())

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

V tem primeru Semantic Router Agent prejme zahtevo uporabnika (npr. "Potrebujem načrt hotela za svoje potovanje.").

Načrtovalec nato:

* Prejme načrt hotela: Načrtovalec vzame uporabnikovo sporočilo in na podlagi sistemskega poziva (vključno s podatki o razpoložljivih agentih) generira strukturiran potovalni načrt.
* Navedbe agentov in njihovih orodij: Registar agentov vsebuje seznam agentov (npr. za let, hotel, najem avtomobila in aktivnosti) skupaj z funkcijami ali orodji, ki jih ponujajo.
* Usmeri načrt pripadajočim agentom: Glede na število podnalog načrtovalec bodisi neposredno pošlje sporočilo namenskemu agentu (za enojne naloge) ali pa koordinira preko upravljalca skupinskega klepeta za sodelovanje več agentov.
* Povzame izid: Nazadnje načrtovalec povzame ustvarjeni načrt za jasnost.
Naslednji primer kode v Pythonu prikazuje te korake:

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

from agent_framework.azure import AzureAIProjectAgentProvider
from azure.identity import AzureCliCredential

# Ustvari odjemalca

provider = AzureAIProjectAgentProvider(credential=AzureCliCredential())

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

# Izpiši vsebino odgovora po nalaganju kot JSON

pprint(json.loads(response_content))
```

Kar sledi, je izhod iz prejšnje kode, ki ga lahko nato uporabite za usmerjanje k `assigned_agent` in povzemanje potovalnega načrta za končnega uporabnika.

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

Primer zvezka s prej omenjeno kodo je na voljo [tukaj](07-python-agent-framework.ipynb).

### Iterativno načrtovanje

Nekatere naloge zahtevajo izmenjavo ali ponovni načrt, kjer izid ene podnaloge vpliva na naslednjo. Na primer, če agent med rezervacijo letov odkrije nepričakovan format podatkov, bo morda moral prilagoditi svojo strategijo, preden nadaljuje z rezervacijami hotelov.

Poleg tega lahko povratne informacije uporabnika (npr. če človek odloči, da bolj želi zgodnejši let) sprožijo delni ponovni načrt. Ta dinamični, iterativni pristop zagotavlja, da se končna rešitev uskladi z omejitvami resničnega sveta in spreminjajočimi se uporabniškimi preferencami.

npr. vzorčna koda

```python
from agent_framework.azure import AzureAIProjectAgentProvider
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

Za bolj celovito načrtovanje si oglejte Magnetic One <a href="https://www.microsoft.com/research/articles/magentic-one-a-generalist-multi-agent-system-for-solving-complex-tasks" target="_blank">Blogpost</a> za reševanje zapletenih nalog.

## Povzetek

V tem prispevku smo si ogledali primer, kako lahko ustvarimo načrtovalca, ki lahko dinamično izbere razpoložljive agente. Izhod načrtovalca razčleni naloge in dodeli agente, da jih lahko izvedejo. Predpostavlja se, da imajo agenti dostop do funkcij/orodij, potrebnih za opravljanje naloge. Poleg agentov lahko vključite še druge vzorce, kot so refleksija, povzetek in rotacijski klepet, za nadaljnjo prilagoditev.

## Dodatni viri

Magentic One - Generalni večagentni sistem za reševanje zapletenih nalog, ki je dosegel impresivne rezultate na več zahtevnih agentnih preverjanjih. Reference: <a href="https://www.microsoft.com/research/articles/magentic-one-a-generalist-multi-agent-system-for-solving-complex-tasks" target="_blank">Magentic One</a>. V tej implementaciji orkestrator ustvarja nalogam specifične načrte in te naloge delegira razpoložljivim agentom. Poleg načrtovanja orkestrator uporablja tudi mehanizem sledenja za spremljanje napredka naloge in ob potrebi ponovno načrtuje.

### Imate več vprašanj o načrtovalnem vzorcu?

Pridružite se [Microsoft Foundry Discord](https://aka.ms/ai-agents/discord), da se srečate z drugimi učenci, udeležite ur uradne podpore in dobite odgovore na vaša vprašanja o AI agentih.

## Prejšnja lekcija

[Gradnja zanesljivih AI agentov](../06-building-trustworthy-agents/README.md)

## Naslednja lekcija

[Večagentni vzorec](../08-multi-agent/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Omejitev odgovornosti**:
Ta dokument je bil preveden z uporabo AI prevajalske storitve [Co-op Translator](https://github.com/Azure/co-op-translator). Čeprav si prizadevamo za natančnost, vas prosimo, da upoštevate, da lahko avtomatski prevodi vsebujejo napake ali netočnosti. Izvirni dokument v njegovem izvirnem jeziku se šteje za uradni vir. Za pomembne informacije priporočamo strokovni človeški prevod. Nismo odgovorni za morebitna nesporazuma ali napačne interpretacije, ki izhajajo iz uporabe tega prevoda.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->