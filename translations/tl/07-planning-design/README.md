[![Planning Design Pattern](../../../translated_images/tl/lesson-7-thumbnail.f7163ac557bea123.webp)](https://youtu.be/kPfJ2BrBCMY?si=9pYpPXp0sSbK91Dr)

> _(I-click ang larawan sa itaas upang panoorin ang video ng leksyong ito)_

# Planning Design

## Panimula

Saklawin ng leksyong ito ang

* Paglilinaw ng isang malinaw na pangkalahatang layunin at paghahati ng isang kumplikadong gawain sa mga magagawang pamamahalang gawain.
* Paggamit ng istrukturadong output para sa mas maaasahan at makina-nababasang mga tugon.
* Pagpapatupad ng isang event-driven na pamamaraan upang hawakan ang mga dinamikong gawain at hindi inaasahang mga input.

## Mga Layunin ng Pagkatuto

Pagkatapos makumpleto ang leksyong ito, magkakaroon ka ng pang-unawa sa:

* Tukuyin at itakda ang isang pangkalahatang layunin para sa isang AI agent, tinitiyak na malinaw nitong alam kung ano ang kailangang makamit.
* Hatiin ang isang kumplikadong gawain sa mga pamamahalaang subtasks at ayusin ang mga ito sa isang lohikal na pagkakasunod-sunod.
* Bigyan ang mga ahente ng tamang mga kasangkapan (hal., mga search tool o data analytics tool), magpasya kung kailan at paano sila gagamitin, at harapin ang mga hindi inaasahang sitwasyon na lumitaw.
* Suriin ang mga kinalabasan ng subtask, sukatin ang pagganap, at ulitin ang mga aksyon upang mapabuti ang panghuling output.

## Paglilinaw ng Pangkalahatang Layunin at Paghahati ng Gawain

![Defining Goals and Tasks](../../../translated_images/tl/defining-goals-tasks.d70439e19e37c47a.webp)

Karamihan sa mga gawain sa totoong mundo ay masyadong kumplikado upang harapin sa isang hakbang lamang. Nangangailangan ang AI agent ng maikling layunin upang gabayan ang kanyang pagpaplano at mga aksyon. Halimbawa, isaalang-alang ang layunin:

    "Gumawa ng 3-araw na itineraryo sa paglalakbay."

Bagaman ito ay simple sabihin, kailangan pa rin itong linawin. Mas malinaw ang layunin, mas maganda ang pokus ng agent (at ng mga taong kasama nito) sa pag-abot ng tamang resulta, tulad ng paggawa ng komprehensibong itineraryo na may mga opsyon sa flight, mga rekomendasyon sa hotel, at mga suhestiyon sa gawain.

### Pagbabahagi ng Gawain

Ang malalaki o masalimuot na mga gawain ay nagiging mas madaling pamahalaan kapag hinati sa mga mas maliliit, layuning nakatuon na subtasks.
Para sa halimbawa ng itineraryo sa paglalakbay, maaari mong hatiin ang layunin sa:

* Pag-book ng Flight
* Pag-book ng Hotel
* Pag-renta ng Sasakyan
* Personalization

Bawat subtask ay maaaring harapin ng mga espesyal na ahente o proseso. Ang isang ahente ay maaaring espesyalisado sa paghahanap ng pinakamagandang flight deals, ang isa naman ay sa pag-book ng hotel, at iba pa. Ang isang tagapag-ugnay o “downstream” na ahente ay maaaring pagsamahin ang mga resultang ito sa isang magkakaugnay na itineraryo para sa end user.

Pinapahintulutan din ng modular na metodong ito ang mga incremental na pagpapahusay. Halimbawa, maaari kang magdagdag ng mga espesyal na ahente para sa Mga Rekomendasyon sa Pagkain o Mga Lokal na Suhestiyon ng Aktibidad at pinuhin ang itineraryo sa paglipas ng panahon.

### Istrukturadong output

Ang mga Large Language Models (LLMs) ay maaaring gumawa ng istrukturadong output (hal., JSON) na mas madali para sa mga downstream agent o serbisyo na iparse at iproseso. Ito ay lalong kapaki-pakinabang sa konteksto ng multi-agent, kung saan maaari nating isagawa ang mga gawain pagkatapos matanggap ang output ng plano.

Ang sumusunod na snippet ng Python ay nagpapakita ng isang simpleng planning agent na naghahati ng layunin sa mga subtasks at lumilikha ng istrukturadong plano:

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

# Modelo ng Travel SubTask
class TravelSubTask(BaseModel):
    task_details: str
    assigned_agent: AgentEnum  # nais naming i-assign ang task sa ahente

class TravelPlan(BaseModel):
    main_task: str
    subtasks: List[TravelSubTask]
    is_greeting: bool

provider = AzureAIProjectAgentProvider(credential=AzureCliCredential())

# Tukuyin ang mensahe ng user
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

### Planning Agent na may Multi-Agent Orchestration

Sa halimbawang ito, isang Semantic Router Agent ang tumatanggap ng kahilingan ng user (hal., "Kailangan ko ng hotel plan para sa aking biyahe.").

Ang planner ay:

* Tumanggap ng Hotel Plan: Kinuha ng planner ang mensahe ng user at, batay sa isang system prompt (kabilang ang detalye ng mga magagamit na agent), nilikha ang isang istrukturadong plano sa paglalakbay.
* Naglista ng Mga Ahente at Kanilang mga Kasangkapan: Ang agent registry ay naglalaman ng listahan ng mga ahente (hal., para sa flight, hotel, pag-renta ng sasakyan, at mga aktibidad) kasama ang mga function o kasangkapang inaalok nila.
* Ipinapadala ang Plano sa Mga Tiyak na Ahente: Depende sa bilang ng mga subtasks, ang planner ay direktang nagpapadala ng mensahe sa dedikadong ahente (para sa mga single-task na sitwasyon) o nakikipag-coordinate sa pamamagitan ng group chat manager para sa multi-agent na kolaborasyon.
* Ipinapaliwanag ang Kinalabasan: Sa huli, pinagsasama ng planner ang ulat ng nilikhang plano para sa kalinawan.
Ang sumusunod na sample ng code sa Python ay nagpapakita ng mga hakbang na ito:

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

# Modelo ng Travel SubTask

class TravelSubTask(BaseModel):
    task_details: str
    assigned_agent: AgentEnum # nais naming i-assign ang task sa ahente

class TravelPlan(BaseModel):
    main_task: str
    subtasks: List[TravelSubTask]
    is_greeting: bool
import json
import os
from typing import Optional

from agent_framework.azure import AzureAIProjectAgentProvider
from azure.identity import AzureCliCredential

# Gumawa ng kliyente

provider = AzureAIProjectAgentProvider(credential=AzureCliCredential())

from pprint import pprint

# Tukuyin ang mensahe ng user

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

# I-print ang nilalaman ng tugon pagkatapos itong i-load bilang JSON

pprint(json.loads(response_content))
```

Ang sumusunod ay output mula sa naunang code at maaari mong gamitin ang istrukturadong output na ito upang i-route sa `assigned_agent` at ibuod ang plano ng paglalakbay para sa end user.

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

May isang halimbawa ng notebook gamit ang naunang sample na code na makikita [dito](07-python-agent-framework.ipynb).

### Iterative Planning

Ang ilang mga gawain ay nangangailangan ng pasulput-sulpot o muling pagpaplano, kung saan ang resulta ng isang subtask ay nakakaapekto sa susunod. Halimbawa, kung ang ahente ay makakakita ng isang hindi inaasahang format ng data habang nagbu-book ng mga flight, maaaring kailanganin nitong baguhin ang estratehiya bago magpatuloy sa pag-book ng hotel.

Bukod dito, ang feedback ng user (hal., kapag pinili ng tao na mas gusto nila ang mas maagang flight) ay maaaring mag-trigger ng partial na muling pagpaplano. Ang dinamikong, iterative na metodong ito ay nagsisigurong ang panghuling solusyon ay naaayon sa mga totoong limitasyon at nagbabagong kagustuhan ng user.

halimbawa ng code

```python
from agent_framework.azure import AzureAIProjectAgentProvider
from azure.identity import AzureCliCredential
#.. pareho sa naunang code at ipasa ang kasaysayan ng gumagamit, kasalukuyang plano

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
# .. muling planuhin at ipadala ang mga gawain sa mga kaukulang ahente
```

Para sa mas komprehensibong pagpaplano, tingnan ang Magnetic One <a href="https://www.microsoft.com/research/articles/magentic-one-a-generalist-multi-agent-system-for-solving-complex-tasks" target="_blank">Blogpost</a> para sa paglutas ng mga kumplikadong gawain.

## Buod

Sa artikulong ito, tiningnan natin ang isang halimbawa kung paano tayo maaaring gumawa ng isang planner na maaaring dinamiko na pumili ng mga magagamit na agent na nakasaad. Ang output ng Planner ay naghahati sa mga gawain at nagtatalaga sa mga ahente upang maisagawa ang mga ito. Inaasahan na may access ang mga ahente sa mga kinakailangang function/casangkapan para isagawa ang gawain. Bilang karagdagan sa mga ahente, maaari mong isama ang iba pang mga pattern tulad ng reflection, summarizer, at round robin chat para sa karagdagang pag-customize.

## Karagdagang Mga Mapagkukunan

Magentic One - Isang Generalist multi-agent system para sa paglutas ng mga kumplikadong gawain at nakakamit ng kahanga-hangang mga resulta sa maraming mahihirap na agentic benchmarks. Sanggunian: <a href="https://www.microsoft.com/research/articles/magentic-one-a-generalist-multi-agent-system-for-solving-complex-tasks" target="_blank">Magentic One</a>. Sa implementasyong ito, ang orchestrator ay lumilikha ng mga task-specific na plano at itinalaga ang mga gawaing ito sa mga magagamit na ahente. Bukod sa pagpaplano, gumagamit din ang orchestrator ng mekanismo ng pagsubaybay upang bantayan ang progreso ng gawain at muling magplano kung kinakailangan.

### May Mga Karagdagang Tanong tungkol sa Planning Design Pattern?

Sumali sa [Microsoft Foundry Discord](https://aka.ms/ai-agents/discord) upang makipagkita sa ibang mga nag-aaral, dumalo sa office hours, at masagot ang iyong mga tanong tungkol sa AI Agents.

## Nakaraang Aralin

[Building Trustworthy AI Agents](../06-building-trustworthy-agents/README.md)

## Susunod na Aralin

[Multi-Agent Design Pattern](../08-multi-agent/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Pahayag ng Paunawa**:
Ang dokumentong ito ay isinalin gamit ang serbisyong AI na pagsasalin na [Co-op Translator](https://github.com/Azure/co-op-translator). Bagamat nagsisikap kami na maging tumpak, pakatandaan na ang awtomatikong pagsasalin ay maaaring maglaman ng mga pagkakamali o kamalian. Ang orihinal na dokumento sa likas nitong wika ang dapat ituring na pangunahing sanggunian. Para sa mahahalagang impormasyon, ipinapayo ang propesyonal na pagsasaling pantao. Hindi kami mananagot sa anumang hindi pagkakaunawaan o maling interpretasyon na maaaring magmula sa paggamit ng pagsasaling ito.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->