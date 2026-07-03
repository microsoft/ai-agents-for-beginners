[![Planning Design Pattern](../../../translated_images/hr/lesson-7-thumbnail.f7163ac557bea123.webp)](https://youtu.be/kPfJ2BrBCMY?si=9pYpPXp0sSbK91Dr)

> _(Kliknite na gornju sliku za prikaz videa ove lekcije)_

# Dizajn planiranja

## Uvod

Ova lekcija će obuhvatiti

* Definiranje jasnog ukupnog cilja i razlaganje složenog zadatka na upravljive zadatke.
* Korištenje strukturiranog izlaza za pouzdanije i strojno čitljive odgovore.
* Primjenu pristupa vođenog događajima za rukovanje dinamičkim zadacima i neočekivanim unosima.

## Ciljevi učenja

Nakon završetka ove lekcije, razumjet ćete:

* Prepoznati i postaviti ukupni cilj za AI agenta, osiguravajući da jasno zna što treba postići.
* Razložiti složen zadatak na upravljive podzadatke i organizirati ih u logički slijed.
* Opremljivati agente pravim alatima (npr. alati za pretraživanje ili alati za analizu podataka), odlučiti kada i kako se koriste te upravljati neočekivanim situacijama koje nastanu.
* Procijeniti rezultate podzadatka, mjeriti izvedbu i ponavljati akcije radi poboljšanja konačnog rezultata.

## Definiranje ukupnog cilja i razlaganje zadatka

![Definiranje ciljeva i zadataka](../../../translated_images/hr/defining-goals-tasks.d70439e19e37c47a.webp)

Većina zadataka u stvarnom svijetu je previše složena da bi se riješila u jednom koraku. AI agent treba sažet cilj koji vodi njegovo planiranje i radnje. Primjerice, razmotrite cilj:

    "Generiraj trodnevni plan putovanja."

Iako je jednostavan za izreći, još treba doradu. Što je cilj jasniji, to bolje agent (i svi uključeni ljudi) mogu usmjeriti svoje napore na postizanje pravog ishoda, poput izrade sveobuhvatnog itinerara s opcijama leta, preporukama hotela i prijedlozima aktivnosti.

### Razlaganje zadatka

Veliki ili složeni zadaci postaju upravljiviji kada se podijele na manje, ciljno orijentirane podzadatke.  
Za primjer itinerara putovanja možete razložiti cilj na:

* Rezervacija leta
* Rezervacija hotela
* Najam automobila
* Personalizacija

Svaki podzadatak može onda biti obrađen od strane specijaliziranih agenata ili procesa. Jedan agent mogao bi se specijalizirati za pretraživanje najboljih letova, drugi za rezervacije hotela itd. Koordinirajući ili „downstream“ agent tada može objediniti ove rezultate u jedan koherentan itinerar za krajnjeg korisnika.

Ovaj modularni pristup također omogućuje postupna poboljšanja. Na primjer, možete dodati specijalizirane agente za Preporuke hrane ili Lokalnih aktivnosti i kroz vrijeme doraditi plan putovanja.

### Strukturirani izlaz

Veliki jezični modeli (LLM) mogu generirati strukturirani izlaz (npr. JSON) koji je lakše za izvozne agente ili usluge za parsiranje i obradu. To je posebno korisno u kontekstu više agenata, gdje možemo izvršavati zadatke nakon primitka planerskog izlaza.

Sljedeći Python isječak prikazuje jednostavnog planerskog agenta kako razlaže cilj na podzadatke i generira strukturirani plan:

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

# Model putnog podzadatka
class TravelSubTask(BaseModel):
    task_details: str
    assigned_agent: AgentEnum  # želimo dodijeliti zadatak agentu

class TravelPlan(BaseModel):
    main_task: str
    subtasks: List[TravelSubTask]
    is_greeting: bool

provider = AzureAIProjectAgentProvider(credential=AzureCliCredential())

# Definiraj korisničku poruku
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
  
### Planerski agent s višeagentnom orkestracijom

U ovom primjeru, Semantički usmjerivački agent prima korisnički zahtjev (npr. "Trebam plan hotela za svoje putovanje.").

Planer tada:

* Prima plan hotela: Planer preuzima korisnikovu poruku i na temelju sistemske upute (uključujući podatke o dostupnim agentima) generira strukturirani plan putovanja.
* Prikazuje agente i njihove alate: Registar agenata drži popis agenata (npr. za letove, hotele, najam automobila i aktivnosti) zajedno s funkcijama ili alatima koje nude.
* Usmjerava plan odgovarajućim agentima: Ovisno o broju podzadatka, planer ili šalje poruku izravno namjenskom agentu (za zadatke jedan po jedan) ili koordinira putem upravitelja grupnog chata za suradnju više agenata.
* Sažima ishod: Na kraju, planer sažima generirani plan radi jasnoće.  
Sljedeći Python kod ilustrira ove korake:

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

# Model podsloženog putovanja

class TravelSubTask(BaseModel):
    task_details: str
    assigned_agent: AgentEnum # želimo dodijeliti zadatak agentu

class TravelPlan(BaseModel):
    main_task: str
    subtasks: List[TravelSubTask]
    is_greeting: bool
import json
import os
from typing import Optional

from agent_framework.azure import AzureAIProjectAgentProvider
from azure.identity import AzureCliCredential

# Kreiraj klijenta

provider = AzureAIProjectAgentProvider(credential=AzureCliCredential())

from pprint import pprint

# Definiraj korisničku poruku

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

# Ispiši sadržaj odgovora nakon učitavanja kao JSON

pprint(json.loads(response_content))
```
  
Što slijedi je izlaz prethodnog koda i nakon toga možete koristiti ovaj strukturirani izlaz za usmjeravanje prema `assigned_agent` i sažeti plan putovanja krajnjem korisniku.

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
  
Primjer bilježnice s prethodnim kodom dostupan je [ovdje](07-python-agent-framework.ipynb).

### Iterativno planiranje

Neki zadaci zahtijevaju povratnu komunikaciju ili ponovno planiranje, gdje ishod jednog podzadatka utječe na sljedeći. Na primjer, ako agent otkrije neočekivani format podataka tijekom rezervacije leta, možda će morati prilagoditi svoju strategiju prije nego što nastavi s rezervacijom hotela.

Dodatno, povratne informacije korisnika (npr. da čovjek odluči da želi raniji let) mogu pokrenuti djelomično ponovno planiranje. Ovaj dinamični, iterativni pristup osigurava da konačno rješenje bude usklađeno s realnim ograničenjima i izmjenjivim željama korisnika.

npr. primjerni kod

```python
from agent_framework.azure import AzureAIProjectAgentProvider
from azure.identity import AzureCliCredential
#.. isto kao i prethodni kod i proslijedi povijest korisnika, trenutni plan

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
# .. ponovno planiraj i pošalji zadatke odgovarajućim agentima
```
  
Za sveobuhvatnije planiranje pogledajte Magnetic One <a href="https://www.microsoft.com/research/articles/magentic-one-a-generalist-multi-agent-system-for-solving-complex-tasks" target="_blank">Blogpost</a> za rješavanje složenih zadataka.

## Sažetak

U ovom članku pogledali smo primjer kako možemo stvoriti planer koji dinamički odabire definirane dostupne agente. Izlaz Planera razlaže zadatke i dodjeljuje agente kako bi se mogli izvršiti. Pretpostavlja se da agenti imaju pristup funkcijama/alatima potrebnim za izvršenje zadatka. Osim agenata, možete uključiti i druge obrasce poput refleksije, sažimača i round robin chata za dodatnu prilagodbu.

## Dodatni resursi

Magentic One - Generalistički višestruki agentski sustav za rješavanje složenih zadataka koji je postigao impresivne rezultate na više zahtjevnih agentskih benchmarka. Referenca: <a href="https://www.microsoft.com/research/articles/magentic-one-a-generalist-multi-agent-system-for-solving-complex-tasks" target="_blank">Magentic One</a>. U ovoj implementaciji, orkestrator izrađuje zadatkovne planove i delegira zadatke dostupnim agentima. Osim planiranja, orkestrator koristi mehanizam za praćenje napretka zadatka i po potrebi ponovno planira.

### Imate li dodatnih pitanja o obrascu dizajna planiranja?

Pridružite se [Microsoft Foundry Discordu](https://discord.com/invite/ATgtXmAS5D) kako biste se povezali s drugim učenicima, sudjelovali na konzultacijama i dobili odgovore na svoja pitanja o AI agentima.

## Prethodna lekcija

[Izgradnja pouzdanih AI agenata](../06-building-trustworthy-agents/README.md)

## Sljedeća lekcija

[Višeagentni dizajn uzorak](../08-multi-agent/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Napomena**:
Ovaj dokument je preveden korištenjem AI prevoditeljskog servisa [Co-op Translator](https://github.com/Azure/co-op-translator). Iako težimo točnosti, imajte na umu da automatski prijevodi mogu sadržavati greške ili netočnosti. Izvorni dokument na izvornom jeziku treba smatrati autoritativnim izvorom. Za važne informacije preporuča se profesionalni ljudski prijevod. Nismo odgovorni za bilo kakva nesporazumevanja ili pogrešne interpretacije koje proizlaze iz korištenja ovog prijevoda.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->