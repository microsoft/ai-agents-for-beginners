[![Planeerimise disainimuster](../../../translated_images/et/lesson-7-thumbnail.f7163ac557bea123.webp)](https://youtu.be/kPfJ2BrBCMY?si=9pYpPXp0sSbK91Dr)

> _(Klõpsa ülaloleval pildil, et vaadata selle õppetundi videot)_

# Planeerimise disainimuster

## Sissejuhatus

Selles õppetükis käsitletakse

* Selge üldeesmärgi määratlemist ja keeruka ülesande jagamist hallatavateks osadeks.
* Struktureeritud väljundi kasutamist usaldusväärsemate ja masinloetavamate vastuste saamiseks.
* Sündmuspõhise lähenemise rakendamist dünaamiliste ülesannete ja ootamatute sisendite käsitlemiseks.

## Õpieesmärgid

Pärast selle õppetüki lõpetamist mõistate järgmisi punkte:

* Määratleda ja seada AI-agendi üldeesmärk, tagades, et see teab selgelt, mida tuleb saavutada.
* Jaotada keerukas ülesanne hallatavateks alatöödeks ja organiseerida need loogiliseks jada.
* Varustada agendid õigete tööriistadega (nt otsingutööriistad või andmeanalüüsi tööriistad), otsustada, millal ja kuidas neid kasutada, ning käsitleda tekkivaid ootamatuid olukordi.
* Hinnata alatööde tulemusi, mõõta jõudlust ja iteratiivselt tegutseda lõpptulemuse parandamiseks.

## Üldeesmärgi määratlemine ja ülesande jagamine

![Eesmärkide ja ülesannete määratlemine](../../../translated_images/et/defining-goals-tasks.d70439e19e37c47a.webp)

Enamik reaalmaailma ülesandeid on liiga keerulised, et neid ühe sammuna lahendada. AI-agendil peab olema lühike eesmärk, mis juhib selle planeerimist ja tegevusi. Näiteks vaadake eesmärki:

    "Genereeri 3-päevane reisiplaan."

Kuigi seda on lihtne sõnastada, vajab see siiski täpsustamist. Mida selgem on eesmärk, seda paremini saab agent (ja kõik inimkaasautorid) keskenduda õige tulemuse saavutamisele, näiteks põhjaliku reisiplaani loomisele lennuvalikute, hotelli soovituste ja tegevuste ettepanekutega.

### Ülesande dekompositsioon

Suured või keerukad ülesanded muutuvad hallatavamaks, kui need jagada väiksemateks, eesmärgipõhiseks alatöödeks.
Reisiplaani näite puhul võiks eesmärgi jagada järgmistesse alatöödesse:

* Lennukate broneerimine
* Hotelli broneerimine
* Autorenti
* Personaliseerimine

Iga alatööga saab tegeleda pühendatud agendid või protsessid. Üks agent võib spetsialiseeruda parimate lennipakkumiste otsimisele, teine keskenduda hotellibroneeringutele jne. Koordineeriv või „järgmine“ agent saab seejärel need tulemused kokku panna üheks sidusaks reisiplaaniks lõppkasutajale.

See modulaarne lähenemine võimaldab ka järkjärgulisi täiustusi. Näiteks võite lisada spetsialiseerunud agente toidusoovituste või kohalike tegevuste ettepanekute jaoks ja täiustada reisiplaani aja jooksul.

### Struktureeritud väljund

Suurkeelemudelid (LLM-id) saavad genereerida struktureeritud väljundeid (nt JSON), mida on lihtsam edasiste agentide või teenuste jaoks töödelda. See on eriti kasulik mitmeagendilises kontekstis, kus pärast planeerimise väljundi saamist saab neid ülesandeid ellu viia.

Järgmine Python'i näide demonstreerib lihtsat planeerimisagenti, mis jagab eesmärgi alatöödeks ja genereerib struktureeritud plaani:

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

# Reisi alamülesande mudel
class TravelSubTask(BaseModel):
    task_details: str
    assigned_agent: AgentEnum  # Soovime ülesande agendile määrata

class TravelPlan(BaseModel):
    main_task: str
    subtasks: List[TravelSubTask]
    is_greeting: bool

provider = AzureAIProjectAgentProvider(credential=AzureCliCredential())

# Määratle kasutaja sõnum
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

### Planeerimisagent mitmeagendilise orkestreerimisega

Selles näites võtab semantiline marsruudiagent kasutaja päringu (nt "Vajan oma reisile hotelliplaani.").

Planeerija teeb seejärel:

* Saab Hotelliplaani: Planeerija võtab kasutaja sõnumi ja, tuginedes süsteemi promptile (sh saadaval olevate agentide detailidele), genereerib struktureeritud reisiplaani.
* Loetleb agentid ja nende tööriistad: Agendiregister sisaldab agentide loendit (nt lennu, hotelli, autorendi ja tegevuste jaoks) koos funktsioonide või tööriistadega, mida nad pakuvad.
* Suunab plaani vastavatele agentidele: Olenevalt alatööde arvust saadab planeerija sõnumi kas otse pühendatud agendile (ühe ülesandega stsenaariumide puhul) või koordineerib mitmeagendilist koostööd grupivestluse halduri kaudu.
* Kokkuvõtab tulemuse: Lõpuks võtab planeerija genereeritud plaani kokku selguse jaoks.
Järgmine Python'i koodinäide illustreerib neid samme:

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

# Reisi alamülesande mudel

class TravelSubTask(BaseModel):
    task_details: str
    assigned_agent: AgentEnum # me tahame ülesande agendile määrata

class TravelPlan(BaseModel):
    main_task: str
    subtasks: List[TravelSubTask]
    is_greeting: bool
import json
import os
from typing import Optional

from agent_framework.azure import AzureAIProjectAgentProvider
from azure.identity import AzureCliCredential

# Loo klient

provider = AzureAIProjectAgentProvider(credential=AzureCliCredential())

from pprint import pprint

# Määra kasutaja sõnum

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

# Trüki vastuse sisu pärast selle laadimist JSON-ina

pprint(json.loads(response_content))
```

Mis järgneb, on väljund eelmisest koodist ja seda struktureeritud väljundit saate seejärel kasutada suunamaks `assigned_agent`-ile ja reisiplaani kokkuvõtmiseks lõppkasutajale.

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

Näide märkmikust eelneva koodinäitega on saadaval [siin](07-python-agent-framework.ipynb).

### Iteratiivne planeerimine

Mõned ülesanded nõuavad edasi-tagasi või ümberplaneerimist, kus ühe alatöö tulemus mõjutab järgmist. Näiteks kui agent avastab lennu broneerimisel ootamatu andmevormingut, võib ta enne hotellibroneeringute juurde liikumist oma strateegiat kohandada.

Lisaks võib kasutaja tagasiside (nt inimene otsustab, et eelistab varasemat lendu) käivitada osalise ümberplaneerimise. See dünaamiline, iteratiivne lähenemine tagab, et lõplik lahendus vastab reaalse maailma piirangutele ja muutuvale kasutaja eelistustele.

Näiteks kood

```python
from agent_framework.azure import AzureAIProjectAgentProvider
from azure.identity import AzureCliCredential
#.. sama mis eelmine kood ja edasta kasutaja ajalugu ning praegune plaan

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
# .. planeeri uuesti ja saada ülesanded vastavatele agentidele
```

Põhjalikuma planeerimise jaoks vaata Magnetic One <a href="https://www.microsoft.com/research/articles/magentic-one-a-generalist-multi-agent-system-for-solving-complex-tasks" target="_blank">Blogipostitus</a>, mis käsitleb keerukate ülesannete lahendamist.

## Kokkuvõte

Selles artiklis vaatasime näidet, kuidas luua planeerija, mis suudab dünaamiliselt valida määratletud saadavalolevad agendid. Planeerija väljund dekomponeerib ülesanded ja määrab agentidele, nii et neid saab täita. Eeldatakse, et agentidel on juurdepääs funktsioonidele/tööriistadele, mis on vajalikud ülesande täitmiseks. Lisaks agentidele võite lisada ka teisi mustreid, nagu refleksioon, kokkuvõtja ja ringikäik-vestlus (round robin), et veelgi kohandada.

## Lisamaterjalid

Magentic One - üldine mitmeagendiline süsteem keerukate ülesannete lahendamiseks, mis on saavutanud muljetavaldavaid tulemusi mitmetel keerukatel agendiväljakutsetel. Viide: <a href="https://www.microsoft.com/research/articles/magentic-one-a-generalist-multi-agent-system-for-solving-complex-tasks" target="_blank">Magentic One</a>. Selles rakenduses loob orkestreerija ülesandespetsiifilised plaanid ja delegeerib need olemasolevatele agentidele. Lisaks planeerimisele kasutab orkestreerija ka jälgimismehhanismi, et monitorida ülesande edenemist ja vajadusel ümberplaneerida.

### On veel küsimusi planeerimise disainimustri kohta?

Liitu [Microsoft Foundry Discord](https://aka.ms/ai-agents/discord), et kohtuda teiste õppuritega, osaleda arstiabides (office hours) ja saada vastused oma AI-agentidega seotud küsimustele.

## Eelmine õppetund

[Usaldusväärsete AI-agentide loomine](../06-building-trustworthy-agents/README.md)

## Järgmine õppetund

[Mitmeagendi disainimuster](../08-multi-agent/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
Lahtiütlus:
See dokument on tõlgitud tehisintellekti tõlketeenuse [Co-op Translator](https://github.com/Azure/co-op-translator) abil. Kuigi püüame tagada täpsuse, palun pange tähele, et automatiseeritud tõlked võivad sisaldada vigu või ebatäpsusi. Originaaldokument selle emakeeles tuleks pidada autoriteetseks allikaks. Kriitilise teabe puhul soovitatakse kasutada professionaalset inimtõlget. Me ei vastuta mis tahes arusaamatuste või valesti tõlgenduste eest, mis võivad tuleneda selle tõlke kasutamisest.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->