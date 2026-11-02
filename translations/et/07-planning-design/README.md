[![Planeerimisdisaini muster](../../../translated_images/et/lesson-7-thumbnail.f7163ac557bea123.webp)](https://youtu.be/kPfJ2BrBCMY?si=9pYpPXp0sSbK91Dr)

> _(Vajutage ülalolevale pildile video vaatamiseks)_

# Planeerimisdisain

## Sissejuhatus

Selles õppetükis käsitleme

* Selge üldeesmärgi määratlemist ja keeruka ülesande jaotamist hallatavateks osadeks.
* Struktureeritud väljundi kasutamist usaldusväärsemate ja masinloetavate vastuste jaoks.
* Sündmuspõhise lähenemise rakendamist dünaamiliste ülesannete ja ootamatute sisendite käsitlemiseks.

## Õpieesmärgid

Pärast selle õppetüki läbimist saate aru:

* Kuidas kindlaks teha ja seada AI-agendi üldeesmärk, tagades, et see teab selgelt, mida tuleb saavutada.
* Kuidas keerukat ülesannet jagada hallatavateks alamosadeks ja organiseerida need loogilisse järjekorda.
* Kuidas varustada agente õigete tööriistadega (nt otsingutööriistad või andmeanalüütika tööriistad), otsustada, millal ja kuidas neid kasutatakse, ning käsitleda tekkivaid ootamatuid olukordi.
* Kuidas hinnata alamosade tulemusi, mõõta tulemuslikkust ja parendada lõplikku väljundit tegevuste iteratiivse täiendamise kaudu.

## Üldeesmärgi määratlemine ja ülesande jagamine

![Eesmärkide ja ülesannete määratlemine](../../../translated_images/et/defining-goals-tasks.d70439e19e37c47a.webp)

Enamik päriselu ülesandeid on liiga keerukad, et neid lahendada ühe sammuna. AI-agent vajab planeerimise ja tegevuste juhtimiseks kokkuvõtlikku eesmärki. Näiteks võib eesmärk olla:

    "Koostada 3-päevane reisikava."

Kuigi see on lihtne väide, vajab see siiski täpsustamist. Mida selgem on eesmärk, seda paremini saab agent (ja ka kõik inimkaaslased) keskenduda õige tulemuse saavutamisele, näiteks põhjaliku reisikava loomisele, mis sisaldab lennuvõimalusi, hotellisoovitusi ja tegevuste ideid.

### Ülesande jaotamine

Suured või keerukad ülesanded muutuvad väiksemateks, eesmärgipõhisteks alamosadeks jagades paremini hallatavaks.
Näiteks reisikava puhul võiksite eesmärgi jagada järgmiseks:

* Lennupiletite broneerimine
* Hotelli broneerimine
* Autorendi korraldamine
* Isikupärastamine

Iga alamosa saab seejärel eraldi agentide või protsesside poolt käsitlemist. Üks agent võib spetsialiseeruda parimate lennupakkumiste otsimisele, teine hotellide broneerimisele jne. Koordineeriv või "järgneva astme" agent saab seejärel need tulemused üheks terviklikuks reisikavaks kasutajale kokku panna.

See moodulipõhine lähenemine võimaldab ka järkjärgulisi täiustusi. Näiteks võiksite lisada spetsialiseerunud agente toidusoovituste või kohalike tegevuste soovituste jaoks ning ajapikku reisikava täpsustada.

### Struktureeritud väljund

Suured keelemudelid (LLM-id) suudavad genereerida struktureeritud väljundit (nt JSON), mida on lihtsam allagentidel või teenustel töödelda ja analüüsida. See on eriti kasulik mitmeagendi kontekstis, kus saab tegevusi teostada pärast planeerimise väljundi saamist.

Järgmine Python-i näidis demonstreerib lihtsat planeerimisagenti, kes lagundab eesmärgi alamosadeks ja loob struktureeritud plaani:

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

# Reisialamudeli ülesanne
class TravelSubTask(BaseModel):
    task_details: str
    assigned_agent: AgentEnum  # soovime ülesande agendile määrata

class TravelPlan(BaseModel):
    main_task: str
    subtasks: List[TravelSubTask]
    is_greeting: bool

provider = FoundryChatClient(
    project_endpoint=os.environ["AZURE_AI_PROJECT_ENDPOINT"],
    model=os.environ["AZURE_AI_MODEL_DEPLOYMENT_NAME"],
    credential=AzureCliCredential(),
)

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

### Planeerimisagent mitmeagendi korraldusega

Selles näites saab semantiline marsruutija agent kasutaja päringu (nt "Mul on vaja hotellikava oma reisiks.").

Seejärel teeb planeerija:

* Saab hotellikava: planeerija võtab kasutaja sõnumi ja süsteemi sisendi alusel (sealhulgas olemasolevate agentide info) genereerib struktureeritud reisiplaani.
* Loetleb agentide ja nende tööriistad: agendi registris on nimekiri agentidest (nt lennundus, hotell, autorent ja tegevused) koos nende funktsioonide või tööriistadega.
* Suunab plaani vastavatele agentidele: vastavalt alamosade arvule saadab planeerija sõnumi kas otse pühendatud agendile (ülesande puhul) või koordineerib rühmateenuse halduriga mitmeagentide koostöö puhul.
* Võtab tulemuse kokku: lõpuks teeb planeerija genereeritud plaanist kokkuvõtte selguse huvides.
Järgmine Python-i koodinäide illustreerib neid samme:

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
    assigned_agent: AgentEnum # me tahame määrata ülesande agendile

class TravelPlan(BaseModel):
    main_task: str
    subtasks: List[TravelSubTask]
    is_greeting: bool
import json
import os
from typing import Optional

from agent_framework.foundry import FoundryChatClient
from azure.identity import AzureCliCredential

# Loo klient

provider = FoundryChatClient(
    project_endpoint=os.environ["AZURE_AI_PROJECT_ENDPOINT"],
    model=os.environ["AZURE_AI_MODEL_DEPLOYMENT_NAME"],
    credential=AzureCliCredential(),
)

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

Järgmine on eelneva koodi väljund ja saate seda struktureeritud väljundit kasutada, et suunata see `assigned_agent`-ile ja esitada kasutajale reisikava kokkuvõte.

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

Näide eelneva koodiga sülearvutist on saadaval [siin](./code_samples/07-python-agent-framework.ipynb).

### Iteratiivne planeerimine

Mõned ülesanded vajavad edasi-tagasi suhtlust või ümberplaneerimist, kus ühe alamosa tulemus mõjutab järgmist sammu. Näiteks, kui agent leiab lennupiletite broneerimise ajal ootamatu andmeformaadi, võib ta enne hotellibroneeringute juurde liikumist oma strateegiat kohandada.

Samuti võib kasutaja tagasiside (nt inimene otsustab, et eelistab varasemat lendu) käivitada osalise ümberplaneerimise. See dünaamiline ja iteratiivne lähenemine tagab, et lõplik lahendus vastab pärismaailma piirangutele ning kasutaja eelistuste muutumisele.

nt näidis kood

```python
import os
from agent_framework.foundry import FoundryChatClient
from azure.identity import AzureCliCredential
#.. sama mis eelnevas koodis ja edasta kasutaja ajalugu, praegune plaan

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
# .. tee uuesti plaan ja saada ülesanded vastavatele esindajatele
```

Üksikasjalikuma planeerimise jaoks vaadake Magnetic One <a href="https://www.microsoft.com/research/articles/magentic-one-a-generalist-multi-agent-system-for-solving-complex-tasks" target="_blank">Blogipostitus</a> keerukate ülesannete lahendamiseks.

## Kokkuvõte

Selles artiklis vaatasime näidet, kuidas luua planeerijat, mis suudab dünaamiliselt valida määratletud olemasolevad agendid. Planeerija väljund lagundab ülesanded ja määrab agendid, et ülesanded täita. Eeldatakse, et agentidel on juurdepääs vajadusel ülesande täitmiseks vajalikele funktsioonidele/tööriistadele. Agendilistele saab lisada ka muid mustreid nagu reflekteerija, kokkuvõtte tegija ja ringikõne vestlus, et veelgi kohandada.

## Täiendavad ressursid

Magnetic One – generalistlik mitmeagentide süsteem keerukate ülesannete lahendamiseks, mis on saavutanud muljetavaldavaid tulemusi mitmetel keerukatel agentuursetel võrdlusülesannetel. Viide: <a href="https://www.microsoft.com/research/articles/magentic-one-a-generalist-multi-agent-system-for-solving-complex-tasks" target="_blank">Magnetic One</a>. Selles rakenduses loob korraldaja ülesandepõhised plaanid ja delegeerib need olemasolevatele agentidele. Lisaks planeerimisele kasutab korraldaja ka jälgimismehhanismi ülesande edenemise jälgimiseks ja vajadusel ümberplaneerimiseks.

### Kas teil on planeerimisdisaini mustri kohta rohkem küsimusi?

Liituge [Microsoft Foundry Discordiga](https://discord.com/invite/ATgtXmAS5D), et kohtuda teiste õppijatega, osaleda kontoritundides ja saada vastused oma AI-agentide küsimustele.

## Eelmine õppetükk

[Usaldusväärsete AI-agentide loomine](../06-building-trustworthy-agents/README.md)

## Järgmine õppetükk

[Mitmeagendi disainimuster](../08-multi-agent/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Lahtiütlus**:
See dokument on tõlgitud kasutades AI tõlketeenust [Co-op Translator](https://github.com/Azure/co-op-translator). Kuigi me püüdleme täpsuse poole, palun pange tähele, et automatiseeritud tõlgetes võib esineda vigu või ebatäpsusi. Originaaldokument selle emakeeles tuleks pidada autoriteetseks allikaks. Olulise teabe puhul soovitatakse kasutada professionaalset inimtõlget. Me ei vastuta selle tõlkega seotud eksimustest või valesti mõistmistest.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->