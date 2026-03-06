[![Obrazac dizajna planiranja](../../../translated_images/hr/lesson-7-thumbnail.f7163ac557bea123.webp)](https://youtu.be/kPfJ2BrBCMY?si=9pYpPXp0sSbK91Dr)

> _(Kliknite sliku iznad da pogledate video ove lekcije)_

# Dizajn planiranja

## Uvod

Ova lekcija će obuhvatiti

* Definiranje jasnog općeg cilja i razbijanje složenog zadatka na upravljive zadatke.
* Korištenje strukturiranog izlaza za pouzdanije i strojno čitljive odgovore.
* Primjena pristupa vođenog događajima za rukovanje dinamičnim zadacima i neočekivanim unosima.

## Ciljevi učenja

Nakon završetka ove lekcije razumjet ćete:

* Identificirati i postaviti opći cilj za AI agenta, osiguravajući da jasno zna što treba postići.
* Razložiti složen zadatak na upravljive podzadatke i organizirati ih u logičan slijed.
* Opremiti agente odgovarajućim alatima (npr. alati za pretraživanje ili alati za analizu podataka), odlučiti kada i kako se koriste te rukovati neočekivanim situacijama koje se pojave.
* Procijeniti rezultate podzadatka, mjeriti izvedbu i iterirati radnje kako bi se poboljšao konačni rezultat.

## Definiranje ukupnog cilja i razbijanje zadatka

![Definiranje ciljeva i zadataka](../../../translated_images/hr/defining-goals-tasks.d70439e19e37c47a.webp)

Većina zadataka u stvarnom svijetu previše je složena da bi se rješavala u jednom koraku. AI agentu je potreban sažet cilj koji će usmjeravati njegovo planiranje i radnje. Na primjer, razmotrite cilj:

    "Generirajte trodnevni plan putovanja."

Iako je jednostavno navesti, i dalje treba doradu. Što je cilj jasniji, to se agent (i svi ljudski suradnici) mogu bolje usredotočiti na postizanje pravog ishoda, poput stvaranja sveobuhvatnog itinerera s opcijama leta, preporukama hotela i prijedlozima aktivnosti.

### Dekompozicija zadatka

Veliki ili složeni zadaci postaju upravljiviji kada se podijele na manje, ciljno orijentirane podzadatke.
Za primjer itinerera putovanja, cilj možete razložiti na:

* Rezervacija leta
* Rezervacija hotela
* Najam automobila
* Personalizacija

Svaki podzadatak tada mogu rješavati specijalizirani agenti ili procesi. Jedan agent mogao bi se specijalizirati za pronalaženje najboljih ponuda letova, drugi se usredotočiti na rezervacije hotela itd. Koordinirajući ili "downstream" agent tada može sastaviti ove rezultate u jedan koherentan itinerer za krajnjeg korisnika.

Ovaj modularni pristup također omogućava postepena poboljšanja. Na primjer, možete dodati specijalizirane agente za preporuke hrane ili prijedloge lokalnih aktivnosti i s vremenom usavršavati itinerer.

### Strukturirani izlaz

Large Language Models (LLM-ovi) mogu generirati strukturirani izlaz (npr. JSON) koji je lakše parsirati i obraditi za downstream agente ili servise. To je posebno korisno u multi-agentnom kontekstu, gdje možemo pokrenuti ove zadatke nakon što se primi plan u strukturiranom obliku.

The following Python snippet demonstrates a simple planning agent decomposing a goal into subtasks and generating a structured plan:

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

# Model podzadatka putovanja
class TravelSubTask(BaseModel):
    task_details: str
    assigned_agent: AgentEnum  # želimo dodijeliti zadatak agentu

class TravelPlan(BaseModel):
    main_task: str
    subtasks: List[TravelSubTask]
    is_greeting: bool

provider = AzureAIProjectAgentProvider(credential=AzureCliCredential())

# Definirajte korisničku poruku
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

### Planer s orkestracijom više agenata

U ovom primjeru, Semantički usmjerivački agent prima korisnički zahtjev (npr. "Trebam plan hotela za moje putovanje.").

Planer zatim:

* Prima plan hotela: Planer uzima korisnikovu poruku i, na temelju sistemskog prompta (uključujući dostupne detalje agenata), generira strukturirani plan putovanja.
* Navodi agente i njihove alate: registar agenata sadrži popis agenata (npr. za letove, hotele, najam automobila i aktivnosti) zajedno s funkcijama ili alatima koje nude.
* Usmjerava plan odgovarajućim agentima: Ovisno o broju podzadatka, planer ili šalje poruku izravno posvećenom agentu (za scenarije s jednim zadatkom), ili koordinira putem upravitelja grupnog chata za suradnju više agenata.
* Sažima ishod: Na kraju, planer sažima generirani plan radi jasnoće.
Sljedeći Python primjer koda ilustrira ove korake:

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
    assigned_agent: AgentEnum # Želimo dodijeliti zadatak agentu

class TravelPlan(BaseModel):
    main_task: str
    subtasks: List[TravelSubTask]
    is_greeting: bool
import json
import os
from typing import Optional

from agent_framework.azure import AzureAIProjectAgentProvider
from azure.identity import AzureCliCredential

# Stvorite klijenta

provider = AzureAIProjectAgentProvider(credential=AzureCliCredential())

from pprint import pprint

# Definirajte korisničku poruku

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

# Ispišite sadržaj odgovora nakon učitavanja kao JSON

pprint(json.loads(response_content))
```

What follows is the output from the previous code and you can then use this structured output to route to `assigned_agent` and summarize the travel plan to the end user.

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

Primjer bilježnice s prethodnim primjerom koda dostupan je [ovdje](07-python-agent-framework.ipynb).

### Iterativno planiranje

Neki zadaci zahtijevaju međusobnu razmjenu ili ponovno planiranje, gdje ishod jednog podzadatka utječe na sljedeći. Na primjer, ako agent otkrije neočekivani format podataka pri rezervaciji letova, možda će trebati prilagoditi svoju strategiju prije prelaska na rezervacije hotela.

Osim toga, povratne informacije korisnika (npr. kada osoba odluči da preferira raniji let) mogu pokrenuti djelomično ponovno planiranje. Ovaj dinamični, iterativni pristup osigurava da konačno rješenje bude usklađeno sa stvarnim ograničenjima i mijenjajućim preferencijama korisnika.

npr. primjer koda

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

Za sveobuhvatnije planiranje pogledajte Magnetic One <a href="https://www.microsoft.com/research/articles/magentic-one-a-generalist-multi-agent-system-for-solving-complex-tasks" target="_blank">objavu na blogu</a> za rješavanje složenih zadataka.

## Sažetak

U ovom članku pogledali smo primjer kako možemo stvoriti planer koji može dinamički odabrati definirane dostupne agente. Izlaz planera razlaže zadatke i dodjeljuje agente tako da se mogu izvršiti. Pretpostavlja se da agenti imaju pristup funkcijama/alatima potrebnim za obavljanje zadatka. Osim agenata možete uključiti i druge obrasce poput refleksije, sažimača i round robin chata kako biste dodatno prilagodili sustav.

## Dodatni resursi

Magentic One - Generalistički multi-agentni sustav za rješavanje složenih zadataka koji je postigao impresivne rezultate na više zahtjevnih agentskih benchmarka. Referenca: <a href="https://www.microsoft.com/research/articles/magentic-one-a-generalist-multi-agent-system-for-solving-complex-tasks" target="_blank">Magentic One</a>. U ovoj implementaciji orkestrator stvara planove specifične za zadatke i delegira te zadatke dostupnim agentima. Osim planiranja, orkestrator također koristi mehanizam praćenja za nadzor napretka zadatka i ponovno planiranje po potrebi.

### Imate li još pitanja o obrascu dizajna planiranja?

Pridružite se [Microsoft Foundry Discord](https://aka.ms/ai-agents/discord) kako biste se susreli s drugim učenicima, sudjelovali na uredovnim satima i dobili odgovore na pitanja o svojim AI agentima.

## Prethodna lekcija

[Izgradnja pouzdanih AI agenata](../06-building-trustworthy-agents/README.md)

## Sljedeća lekcija

[Obrazac dizajna za više agenata](../08-multi-agent/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
Izjava o odricanju odgovornosti:
Ovaj je dokument preveden korištenjem AI prevoditeljskog servisa [Co-op Translator](https://github.com/Azure/co-op-translator). Iako nastojimo postići točnost, imajte na umu da automatski prijevodi mogu sadržavati pogreške ili netočnosti. Izvorni dokument na izvornom jeziku treba se smatrati mjerodavnim izvorom. Za kritične informacije preporučuje se profesionalni ljudski prijevod. Ne snosimo odgovornost za bilo kakve nesporazume ili pogrešna tumačenja koja proizlaze iz korištenja ovog prijevoda.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->