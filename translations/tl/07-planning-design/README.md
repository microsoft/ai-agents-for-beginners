[![Planning Design Pattern](../../../translated_images/tl/lesson-7-thumbnail.f7163ac557bea123.webp)](https://youtu.be/kPfJ2BrBCMY?si=9pYpPXp0sSbK91Dr)

> _(I-click ang larawan sa itaas upang mapanood ang video ng araling ito)_

# Planning Design

## Panimula

Tatalakayin ng araling ito

* Pagbibigay ng malinaw na pangkalahatang layunin at paghahati ng isang masalimuot na gawain sa mga madaling pamahalaang gawain.
* Paggamit ng estrukturadong output para sa mas maaasahan at makinang mabasang tugon.
* Paglalapat ng event-driven na pamamaraan upang hawakan ang mga dinamikong gawain at hindi inaasahang mga input.

## Mga Layunin sa Pagkatuto

Pagkatapos makumpleto ang araling ito, mauunawaan mo ang tungkol sa:

* Tukuyin at itakda ang isang pangkalahatang layunin para sa AI agent, na tinitiyak na malinaw nitong alam kung ano ang kailangang makamit.
* Hatiin ang isang masalimuot na gawain sa mga pamahalaang subtask at ayusin ito sa isang lohikal na pagkakasunod-sunod.
* Bigyan ang mga agent ng tamang mga kasangkapan (hal., mga search tool o data analytics tools), magpasya kung kailan at paano ito gagamitin, at harapin ang mga hindi inaasahang sitwasyon na lumilitaw.
* Suriin ang mga resulta ng subtask, sukatin ang pagganap, at ulitin ang mga aksyon upang mapabuti ang panghuling output.

## Pagbibigay Kahulugan sa Pangkalahatang Layunin at Paghahati ng Gawain

![Defining Goals and Tasks](../../../translated_images/tl/defining-goals-tasks.d70439e19e37c47a.webp)

Karamihan sa mga totoong gawain ay masyadong kumplikado upang tugunan sa isang hakbang lamang. Nangangailangan ang AI agent ng isang maikling layunin upang gabayan ang kanyang pagpaplano at mga aksyon. Halimbawa, isaalang-alang ang layunin:

    "Gumawa ng 3-araw na itineraryo ng paglalakbay."

Bagaman simple itong sabihin, kailangan pa rin itong linawin. Mas malinaw ang layunin, mas maganda ang pagtuon ng ahente (at ng mga katuwang na tao) sa pag-abot ng tamang kinalabasan, tulad ng paggawa ng komprehensibong itineraryo na may mga opsyon sa flight, rekomendasyon sa hotel, at mga suhestiyon sa gawain.

### Paghahati ng Gawain

Ang mga malalaki o masalimuot na gawain ay nagiging mas madaling pamahalaan kapag hinati sa mas maliliit, layuning-pokus na mga subtask.
Para sa halimbawa ng itineraryo ng paglalakbay, maaari mong hatiin ang layunin sa:

* Pag-book ng Flight
* Pag-book ng Hotel
* Pag-upa ng Sasakyan
* Personalization

Ang bawat subtask ay maaaring gawin ng mga dedikadong agent o proseso. Isang ahente ang maaaring dalubhasa sa paghahanap ng pinakamahusay na flight deals, isa naman sa hotel bookings, at iba pa. Ang isang coordinating o “downstream” agent ang maaaring mag-ipon ng mga resultang ito sa isang magkakaugnay na itineraryo para sa end user.

Pinapayagan din ng modular na pamamaraang ito ang paunti-unting pagpapahusay. Halimbawa, maaari kang magdagdag ng mga specialized agent para sa Mga Rekomendasyon sa Pagkain o Mga Suhestiyon sa Lokal na Gawain at pinuhin ang itineraryo sa paglipas ng panahon.

### Estrukturadong Output

Makakalikha ang Large Language Models (LLMs) ng estrukturadong output (hal., JSON) na mas madali para sa downstream agents o serbisyo na i-parse at iproseso. Ito ay lalo na kapaki-pakinabang sa konteksto ng multi-agent, kung saan maaari nating isagawa ang mga gawain pagkatapos matanggap ang output ng pagpaplano.

Ang sumusunod na snippet ng Python ay nagpapakita ng isang simpleng planning agent na naghahati ng layunin sa mga subtask at gumagawa ng estrukturadong plano:

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

# Modelo ng SubTask sa Paglalakbay
class TravelSubTask(BaseModel):
    task_details: str
    assigned_agent: AgentEnum  # nais naming i-assign ang gawain sa ahente

class TravelPlan(BaseModel):
    main_task: str
    subtasks: List[TravelSubTask]
    is_greeting: bool

provider = FoundryChatClient(
    project_endpoint=os.environ["AZURE_AI_PROJECT_ENDPOINT"],
    model=os.environ["AZURE_AI_MODEL_DEPLOYMENT_NAME"],
    credential=AzureCliCredential(),
)

# Ibigay ang mensahe ng user
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

Sa halimbawang ito, tumatanggap ang Semantic Router Agent ng kahilingan ng user (hal., "Kailangan ko ng hotel plan para sa aking biyahe.").

Ang planner ay:

* Tumatanggap ng Hotel Plan: Kinukuha ng planner ang mensahe ng user at, batay sa system prompt (kasama ang detalye ng mga available na agent), gumagawa ng estrukturadong plano sa paglalakbay.
* Ipinapakita ang Listahan ng mga Agent at Kanilang Mga Kasangkapan: Ang agent registry ay may listahan ng mga agent (hal., para sa flight, hotel, pag-upa ng sasakyan, at mga aktibidad) kasama ang mga function o tools na inaalok nila.
* Ipinapasa ang Plano sa Mga Kaukulang Agent: Depende sa dami ng mga subtask, ang planner ay nagpadala ng mensahe nang direkta sa dedikadong agent (para sa mga scenario na may iisang gawain) o kinokoordina sa pamamagitan ng group chat manager para sa multi-agent na kolaborasyon.
* Nilalagom ang Kinalabasan: Sa wakas, nilalagom ng planner ang nagawang plano para sa kalinawan.
Ang sumusunod na halimbawa ng code sa Python ay nagpapakita ng mga hakbang na ito:

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

# Modelo ng Maliit na Gawain sa Paglalakbay

class TravelSubTask(BaseModel):
    task_details: str
    assigned_agent: AgentEnum # Nais naming i-assign ang gawain sa ahente

class TravelPlan(BaseModel):
    main_task: str
    subtasks: List[TravelSubTask]
    is_greeting: bool
import json
import os
from typing import Optional

from agent_framework.foundry import FoundryChatClient
from azure.identity import AzureCliCredential

# Gumawa ng kliyente

provider = FoundryChatClient(
    project_endpoint=os.environ["AZURE_AI_PROJECT_ENDPOINT"],
    model=os.environ["AZURE_AI_MODEL_DEPLOYMENT_NAME"],
    credential=AzureCliCredential(),
)

from pprint import pprint

# Tukuyin ang mensahe ng gumagamit

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

# I-print ang nilalaman ng sagot pagkatapos itong i-load bilang JSON

pprint(json.loads(response_content))
```

Ang sumusunod ay output mula sa naunang code at maaari mong gamitin ang estrukturadong output na ito upang ipasa sa `assigned_agent` at ilahad nang buo ang plano ng paglalakbay sa end user.

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

May available na halimbawa ng notebook na may naunang code sample [dito](./code_samples/07-python-agent-framework.ipynb).

### Paulit-ulit na Pagpaplano

Ang ilang mga gawain ay nangangailangan ng palitan o muling pagpaplano, kung saan ang resulta ng isang subtask ay nakakaapekto sa susunod. Halimbawa, kung ang agent ay makakita ng isang hindi inaasahang data format habang nagbubook ng mga flight, maaaring kailanganin nitong ayusin ang estratehiya bago magpatuloy sa pag-book ng hotel.

Bukod dito, ang feedback ng user (hal., isang tao na nagpapasya na mas gusto nila ang mas maagang flight) ay maaaring mag-trigger ng partial re-plan. Ang dinamikong pamamaraang ito ng paulit-ulit na pagpaplano ay nagsisiguro na ang panghuling solusyon ay tumutugon sa totoong mga limitasyon at patuloy na nagbabagong mga kagustuhan ng user.

halimbawa ng sample na code

```python
import os
from agent_framework.foundry import FoundryChatClient
from azure.identity import AzureCliCredential
#.. pareho ng naunang code at ipasa ang kasaysayan ng user, kasalukuyang plano

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
# .. muling magplano at ipadala ang mga gawain sa mga kaukulang ahente
```

Para sa mas kumprehensibong pagpaplano, tingnan ang Magnetic One <a href="https://www.microsoft.com/research/articles/magentic-one-a-generalist-multi-agent-system-for-solving-complex-tasks" target="_blank">Blogpost</a> para sa paglutas ng mga masalimuot na gawain.

## Buod

Sa artikulong ito ay tiningnan natin ang halimbawa kung paano gumawa ng planner na maaaring dinamiko na pumili ng mga available na agent na nakalatag. Ang output ng Planner ay naghahati ng mga gawain at nagtatalaga ng mga agent upang maisagawa ang mga ito. Ipinapalagay na ang mga agent ay may access sa mga function/tools na kinakailangan upang magampanan ang gawain. Bukod sa mga agent, maaari kang magdagdag ng iba pang mga pattern tulad ng reflection, summarizer, at round robin chat para sa karagdagang pag-customize.

## Karagdagang Mga Mapagkukunan

Magnetic One - Isang Generalist multi-agent system para sa paglutas ng masalimuot na mga gawain at nakamit ang kapansin-pansing resulta sa maraming mahihirap na agentic benchmark. Sanggunian: <a href="https://www.microsoft.com/research/articles/magentic-one-a-generalist-multi-agent-system-for-solving-complex-tasks" target="_blank">Magnetic One</a>. Sa implementasyong ito, ang orchestrator ay gumagawa ng mga task-specific na plano at nagtatalaga ng mga gawain sa mga available na agent. Bukod sa pagpaplano, gumagamit din ang orchestrator ng mekanismo sa pagsubaybay upang bantayan ang progreso ng gawain at mag-replan kapag kinakailangan.

### May Mga Karagdagang Tanong Tungkol sa Planning Design Pattern?

Sumali sa [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D) upang makipagkita sa ibang mga nag-aaral, dumalo sa office hours, at sagutin ang iyong mga tanong tungkol sa AI Agents.

## Nakaraang Aralin

[Building Trustworthy AI Agents](../06-building-trustworthy-agents/README.md)

## Susunod na Aralin

[Multi-Agent Design Pattern](../08-multi-agent/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Pagtatanggi**:
Ang dokumentong ito ay isinalin gamit ang serbisyo ng AI translation na [Co-op Translator](https://github.com/Azure/co-op-translator). Bagama't nagsusumikap kami para sa katumpakan, pakatandaan na ang awtomatikong pagsasalin ay maaaring maglaman ng mga pagkakamali o hindi pagkakatugma. Ang orihinal na dokumento sa orihinal nitong wika ang dapat ituring na pangunahing sanggunian. Para sa mahahalagang impormasyon, inirerekomenda ang propesyonal na pagsasalin ng tao. Hindi kami mananagot sa anumang maling pagkakaintindi o maling interpretasyon na nagmula sa paggamit ng pagsasaling ito.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->