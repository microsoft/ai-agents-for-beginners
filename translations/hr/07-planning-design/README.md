[![Planning Design Pattern](../../../translated_images/hr/lesson-7-thumbnail.f7163ac557bea123.webp)](https://youtu.be/kPfJ2BrBCMY?si=9pYpPXp0sSbK91Dr)

> _(Kliknite na sliku iznad za pregled videa ove lekcije)_

# Dizajn planiranja

## Uvod

Ova lekcija će obuhvatiti

* Definiranje jasnog ukupnog cilja i razbijanje složenog zadatka u upravljive zadatke.
* Korištenje strukturiranog izlaza za pouzdanije i za stroj čitljive odgovore.
* Primjenu pristupa vođenog događajima za rukovanje dinamičkim zadacima i neočekivanim unosima.

## Ciljevi učenja

Nakon završetka ove lekcije, imat ćete razumijevanje o:

* Identifikaciji i postavljanju ukupnog cilja za AI agenta, osiguravajući da jasno zna što treba postići.
* Razlaganju složenog zadatka u upravljive podzadatke i organizaciji u logičan redoslijed.
* Opremljavanju agenata pravim alatima (npr. alati za pretraživanje ili alati za analizu podataka), odlučivanju kada i kako ih koristiti te rukovanju neočekivanim situacijama koje se pojave.
* Procjeni ishoda podzadatka, mjerenju izvedbe te iteraciji na radnjama za poboljšanje konačnog rezultata.

## Definiranje ukupnog cilja i razlaganje zadatka

![Definiranje ciljeva i zadataka](../../../translated_images/hr/defining-goals-tasks.d70439e19e37c47a.webp)

Većina stvarnih zadataka je previše složena da bi ih se riješilo u jednom koraku. AI agentu je potreban sažet cilj koji će usmjeravati njegovo planiranje i radnje. Na primjer, razmotrite cilj:

    "Generiraj trodnevni plan putovanja."

Iako je jednostavno navesti, još uvijek treba doradu. Što je cilj jasniji, to se agent (i svi ljudski suradnici) bolje mogu usredotočiti na postizanje pravog ishoda, poput stvaranja sveobuhvatnog plana s opcijama letova, preporukama hotela i prijedlozima aktivnosti.

### Razlaganje zadataka

Veliki ili složeni zadaci postaju upravljiviji kada se podijele na manje, ciljno orijentirane podzadatke.
Za primjer plana putovanja, cilj možete razložiti na:

* Rezervacija leta
* Rezervacija hotela
* Najam automobila
* Personalizacija

Svaki podzadatak zatim može biti riješen od strane posvećenih agenata ili procesa. Jedan agent može se specijalizirati za pronalaženje najboljih ponuda za letove, drugi se fokusira na rezervacije hotela, itd. Koordinirajući ili „donji“ agent može potom spojiti ove rezultate u jedan koherentan plan za krajnjeg korisnika.

Ovaj modularni pristup također omogućava postupna poboljšanja. Na primjer, možete dodati specijalizirane agente za preporuke hrane ili lokalne aktivnosti i s vremenom doraditi plan.

### Strukturirani izlaz

Veliki jezični modeli (LLM) mogu generirati strukturirani izlaz (npr. JSON) koji je lakše za daljnju obradu ili parsiranje od strane drugih agenata ili servisa. To je osobito korisno u kontekstu višestrukih agenata, gdje možemo pokretati zadatke nakon primitka izlaza planiranja.

Sljedeći Python primjer prikazuje jednostavnog planerskog agenta koji razlaže cilj na podzadatke i generira strukturirani plan:

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

# Model podzadatka putovanja
class TravelSubTask(BaseModel):
    task_details: str
    assigned_agent: AgentEnum  # želimo dodijeliti zadatak agentu

class TravelPlan(BaseModel):
    main_task: str
    subtasks: List[TravelSubTask]
    is_greeting: bool

provider = FoundryChatClient(
    project_endpoint=os.environ["AZURE_AI_PROJECT_ENDPOINT"],
    model=os.environ["AZURE_AI_MODEL_DEPLOYMENT_NAME"],
    credential=AzureCliCredential(),
)

# Definirajte poruku korisnika
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

### Planerski agent s orkestracijom više agenata

U ovom primjeru agent Semantičkog rutera prima korisnički zahtjev (npr. "Trebam plan hotela za svoje putovanje.").

Planer zatim:

* Prima plan hotela: Planer uzima korisničku poruku i, na temelju sistemske poruke (uključujući dostupne detalje o agentima), generira strukturirani plan putovanja.
* Navodi agente i njihove alate: Registar agenata sadrži popis agenata (npr. za letove, hotele, najam automobila i aktivnosti) zajedno s funkcijama ili alatima koje nude.
* Usmjerava plan odgovarajućim agentima: Ovisno o broju podzadatka, planer ili šalje poruku izravno posvećenom agentu (za scenarije s jednim zadatkom) ili koordinira putem upravitelja grupnog chata za suradnju više agenata.
* Sažima ishod: Na kraju, planer sažima generirani plan radi jasnoće.
Sljedeći Python kôd ilustrira ove korake:

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

# Model podzadatka putovanja

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

from agent_framework.foundry import FoundryChatClient
from azure.identity import AzureCliCredential

# Kreiraj klijenta

provider = FoundryChatClient(
    project_endpoint=os.environ["AZURE_AI_PROJECT_ENDPOINT"],
    model=os.environ["AZURE_AI_MODEL_DEPLOYMENT_NAME"],
    credential=AzureCliCredential(),
)

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

Ono što slijedi je izlaz prethodnog koda i zatim možete koristiti ovaj strukturirani izlaz za usmjeravanje ka `assigned_agent` i sažimanje plana putovanja za krajnjeg korisnika.

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

Primjer bilježnice s prethodnim uzorkom koda dostupan je [ovdje](./code_samples/07-python-agent-framework.ipynb).

### Iterativno planiranje

Neki zadaci zahtijevaju iteracije ili ponovno planiranje, gdje ishod jednog podzadatka utječe na sljedeći. Na primjer, ako agent otkrije neočekivani format podataka tijekom rezervacije leta, možda će trebati prilagoditi strategiju prije nego što nastavi s rezervacijom hotela.

Osim toga, korisnička povratna informacija (npr. čovjek odluči da preferira raniji let) može pokrenuti djelomično ponovno planiranje. Ovaj dinamični, iterativni pristup osigurava da konačno rješenje bude usklađeno sa stvarnim ograničenjima i promjenjivim korisničkim preferencijama.

npr. uzorak koda

```python
import os
from agent_framework.foundry import FoundryChatClient
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

U ovom članku smo pogledali primjer kako možemo stvoriti planer koji može dinamički odabrati dostupne agente. Izlaz planer razlaže zadatke i dodjeljuje agente tako da ih se može izvršiti. Pretpostavlja se da agenti imaju pristup funkcijama/alatima potrebnim za izvršenje zadatka. Osim agenata, možete uključiti i druge obrasce poput refleksije, sumarnog prikaza i kružnog chata za daljnju prilagodbu.

## Dodatni resursi

Magnetic One - Generalistički sustav s više agenata za rješavanje složenih zadataka koji je postigao impresivne rezultate na više zahtjevnih testova agenata. Referenca: <a href="https://www.microsoft.com/research/articles/magentic-one-a-generalist-multi-agent-system-for-solving-complex-tasks" target="_blank">Magnetic One</a>. U ovoj implementaciji orkestrator stvara zadatkovno specifične planove i delegira ih dostupnim agentima. Uz planiranje, orkestrator koristi mehanizam za praćenje napretka zadataka i ponovno planira po potrebi.

### Imate li dodatnih pitanja o obrascu dizajna planiranja?

Pridružite se [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D) zajednici kako biste se susreli s drugim učenicima, sudjelovali na konzultacijama i dobili odgovore na pitanja o AI agentima.

## Prethodna lekcija

[Izgradnja pouzdanih AI agenata](../06-building-trustworthy-agents/README.md)

## Sljedeća lekcija

[Obrazac dizajna višestrukih agenata](../08-multi-agent/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Napomena**:
Ovaj dokument je preveden korištenjem AI prevoditeljskog servisa [Co-op Translator](https://github.com/Azure/co-op-translator). Iako težimo točnosti, imajte na umu da automatski prijevodi mogu sadržavati greške ili netočnosti. Izvorni dokument na izvornom jeziku treba smatrati autoritativnim izvorom. Za važne informacije preporuča se profesionalni ljudski prijevod. Nismo odgovorni za bilo kakva nesporazumevanja ili pogrešne interpretacije koje proizlaze iz korištenja ovog prijevoda.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->