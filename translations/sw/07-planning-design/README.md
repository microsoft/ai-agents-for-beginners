[![Mpangilio wa Muundo wa Mipango](../../../translated_images/sw/lesson-7-thumbnail.f7163ac557bea123.webp)](https://youtu.be/kPfJ2BrBCMY?si=9pYpPXp0sSbK91Dr)

> _(Bonyeza picha juu ili kutazama video ya somo hili)_

# Mpangilio wa Muundo

## Utangulizi

Somo hili litashughulikia

* Kufafanua lengo kuu wazi na kugawanya kazi ngumu kuwa kazi ndogo ndogo zinazoweza kudhibitiwa.
* Kutumia matokeo yaliyo na muundo kwa majibu yenye kuaminika zaidi na yanayosomwa na mashine.
* Kutumia mbinu inayotegemea matukio kushughulikia kazi zinazoleta mabadiliko na pembejeo zisizotarajiwa.

## Malengo ya Kujifunza

Baada ya kumaliza somo hili, utakuwa na uelewa kuhusu:

* Kubaini na kuweka lengo kuu kwa wakala wa AI, kuhakikisha anajua wazi kinachotakiwa kufanikishwa.
* Kugawanya kazi ngumu kuwa kazi ndogo ndogo zinazolenga malengo na kuzipanga kwa mpangilio wa mantiki.
* Kuwapa mawakala zana sahihi (mfano, zana za utafutaji au zana za uchambuzi wa data), kuamua lini na jinsi zinavyotumika, na kushughulikia hali zisizotarajiwa zinazojitokeza.
* Kutathmini matokeo ya kazi ndogo, kupima utendaji, na kurudia hatua za kuboresha matokeo ya mwisho.

## Kufafanua Lengo Kuu na Kugawanya Kazi

![Kufafanua Malengo na Kazi](../../../translated_images/sw/defining-goals-tasks.d70439e19e37c47a.webp)

Kazi nyingi halisi ni ngumu mno kushughulikia kwa hatua moja tu. Wakala wa AI anahitaji lengo fupi la kuelekeza mipango na vitendo vyake. Kwa mfano, fikiria lengo:

    "Tengeneza ratiba ya kusafiri ya siku 3."

Ingawa ni rahisi kusema, bado linahitaji kusahihishwa. Kadri lengo linavyokuwa wazi zaidi, ndivyo wakala (na washirikishi wowote wa binadamu) wanavyoweza kuzingatia kufanikisha matokeo sahihi, kama vile kuunda ratiba kamili yenye chaguzi za ndege, mapendekezo ya hoteli, na mapendekezo ya shughuli.

### Kugawanya Kazi

Kazi kubwa au tata zinaweza kudhibitiwa vizuri zaidi zinapogawanywa kuwa kazi ndogo ndogo zenye lengo maalum.
Kwa mfano wa ratiba ya kusafiri, unaweza kugawanya lengo kuwa:

* Uwekaji wa Tiketi za Ndege
* Uwekaji wa Hoteli
* Kukodisha Gari
* Ubinafsishaji

Kila kazi ndogo inaweza kushughulikiwa na mawakala maalum au michakato. Wakala mmoja anaweza kushughulikia utafutaji wa ofa bora za ndege, mwingine anazingatia uwekaji wa hoteli, na kadhalika. Wakala wa kuratibu au "wa chini" anaweza kisha kukusanya matokeo haya kuunda ratiba moja iliyo kamili kwa mtumiaji wa mwisho.

Mbinu hii ya moduli pia inaruhusu maboresho ya awamu kwa awamu. Kwa mfano, unaweza kuongeza mawakala maalum kwa Mapendekezo ya Chakula au Mapendekezo ya Shughuli za Kijiji na kuboresha ratiba kwa muda.

### Matokeo yenye Muundo

Modeli Kubwa za Lugha (LLMs) zinaweza kuzalisha matokeo yenye muundo (mfano JSON) ambayo ni rahisi kwa mawakala wa chini au huduma kuchambua na kusindika. Hii ni muhimu hasa katika muktadha wa mawakala wengi, ambapo tunaweza kuchukua hatua kwenye kazi hizi baada ya kupokea matokeo ya mipango.

Fuatayo ni kipande cha Python kinachoonyesha wakala wa mipango akigawanya lengo kuwa kazi ndogo ndogo na kuzalisha mpango wenye muundo:

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

# Mfano wa Kazi Ndogo ya Safari
class TravelSubTask(BaseModel):
    task_details: str
    assigned_agent: AgentEnum  # tunataka kugawa kazi kwa wakala

class TravelPlan(BaseModel):
    main_task: str
    subtasks: List[TravelSubTask]
    is_greeting: bool

provider = AzureAIProjectAgentProvider(credential=AzureCliCredential())

# Bainisha ujumbe wa mtumiaji
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

### Wakala wa Mpangilio na Usimamizi wa Mawakala Wengi

Katika mfano huu, Wakala wa Mzunguko wa Semantiki anapokea ombi la mtumiaji (mfano, "Nahitaji mpango wa hoteli kwa safari yangu.").

Mpangaji kisha:

* Anapokea Mpango wa Hoteli: Mpangaji huchukua ujumbe wa mtumiaji na, kulingana na mfumo wa mfumo (ukiongozwa na maelezo ya mawakala waliopo), huzalisha mpango wa kusafiri wenye muundo.
* Anataja Majina ya Mawakala na Zana zao: Rejista ya wakala ina orodha ya mawakala (mfano, kwa ndege, hoteli, kodi ya gari, na shughuli) pamoja na kazi au zana wanazotoa.
* Anapeleka Mpango kwa Mawakala Husika: Kutegemea na idadi ya kazi ndogo, mpangaji hutuma ujumbe moja kwa moja kwa wakala maalum (kwa hali ya kazi moja) au kuratibu kupitia meneja wa mazungumzo ya kikundi kwa ushirikiano wa mawakala wengi.
* Anafupisha Matokeo: Mwisho, mpangaji hufupisha mpango uliotengenezwa kwa uwazi.
Mfano wa msimbo wa Python unaonyesha hatua hizi:

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

# Mfano wa Dhamira Ndogo ya Safari

class TravelSubTask(BaseModel):
    task_details: str
    assigned_agent: AgentEnum # tunataka kugawa kazi kwa wakala

class TravelPlan(BaseModel):
    main_task: str
    subtasks: List[TravelSubTask]
    is_greeting: bool
import json
import os
from typing import Optional

from agent_framework.azure import AzureAIProjectAgentProvider
from azure.identity import AzureCliCredential

# Unda mteja

provider = AzureAIProjectAgentProvider(credential=AzureCliCredential())

from pprint import pprint

# Eleza ujumbe wa mtumiaji

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

# Chapisha maudhui ya majibu baada ya kuyapakia kama JSON

pprint(json.loads(response_content))
```

Kinachofuata ni matokeo ya msimbo uliotangulia na unaweza kutumia matokeo haya yenye muundo kuitumia `assigned_agent` na kufupisha mpango wa kusafiri kwa mtumiaji wa mwisho.

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

Mfano wa daftari lenye msimbo uliotangulia upo [hapa](07-python-agent-framework.ipynb).

### Mipango ya Kikirudisho

Baadhi ya kazi zinahitaji kurudia mchakato wa mipango, ambapo matokeo ya kazi ndogo yanaathiri ile inayofuata. Kwa mfano, ikiwa wakala atagundua muundo usiotarajiwa wa data wakati wa kuweka tiketi za ndege, anaweza kuhitaji kubadilisha mkakati wake kabla ya kuendelea na kuweka hoteli.

Zaidi ya hayo, maoni ya mtumiaji (mfano, binadamu kuamua wanapendelea ndege ya mapema) yanaweza kusababisha upangaji wa sehemu ya kazi upya. Mbinu hii ya mzunguko, ya mabadiliko, inahakikisha suluhisho la mwisho linaendana na vizingiti halisi vya dunia na mabadiliko ya mapendeleo ya mtumiaji.

mfano wa msimbo

```python
from agent_framework.azure import AzureAIProjectAgentProvider
from azure.identity import AzureCliCredential
#.. sawa na msimbo wa awali na pita kwenye historia ya mtumiaji, mpango wa sasa

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
# .. panga upya na tuma kazi kwa mawakala husika
```

Kwa mipango ya kina zaidi tazama makala ya Magnetic One <a href="https://www.microsoft.com/research/articles/magentic-one-a-generalist-multi-agent-system-for-solving-complex-tasks" target="_blank">Blogpost</a> kwa kutatua kazi ngumu.

## Muhtasari

Katika makala haya tumeangalia mfano wa jinsi tunavyoweza kuunda mpangaji anayeweza kuchagua kwa nguvu mawakala waliopo waliotajwa. Matokeo ya Mpangaji hugawanya kazi na kugawa mawakala ili ziweze kutekelezwa. Inachukuliwa kuwa mawakala wana upatikanaji wa kazi/zaidi ya zana zinazohitajika kufanya kazi. Mbali na mawakala unaweza kujumuisha mifumo mingine kama tafakari, mfupishaji, na mazungumzo ya mzunguko wa mduara ili kuboresha zaidi.

## Rasilimali Zaidi

Magentic One - Mfumo wa mawakala wengi wa jumla kwa kutatua kazi nyeti na umefikia mafanikio makubwa katika vipimo vingi vigumu vya mawakala. Marejeleo: <a href="https://www.microsoft.com/research/articles/magentic-one-a-generalist-multi-agent-system-for-solving-complex-tasks" target="_blank">Magentic One</a>. Katika utekelezaji huu mwandamizi huunda mipango maalum ya kazi na kugawa kazi hizi kwa mawakala waliopo. Mbali na kupanga, mwandamizi pia hutumia mfumo wa ufuatiliaji wa maendeleo ya kazi na kurudia mipango inapohitajika.

### Una Maswali Zaidi kuhusu Muundo wa Mipango?

Jiunge na [Microsoft Foundry Discord](https://aka.ms/ai-agents/discord) kukutana na wanafunzi wengine, kuhudhuria vipindi vya maswali, na kupata majibu kwa maswali yako ya Wakala wa AI.

## Somo lililotangulia

[Kuunda Wakala wa AI Wanaoaminika](../06-building-trustworthy-agents/README.md)

## Somo lijalo

[Muundo wa Mawakala Wengi](../08-multi-agent/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Tangazo la Kukana**:  
Hati hii imetafsiriwa kwa kutumia huduma ya utafsiri ya AI [Co-op Translator](https://github.com/Azure/co-op-translator). Ingawa tunajitahidi kwa usahihi, tafadhali fahamu kwamba tafsiri za kiotomatiki zinaweza kuwa na makosa au upungufu wa usahihi. Hati ya asili kwa lugha yake ya mzaliwa inapaswa kuzingatiwa kama chanzo chenye mamlaka. Kwa taarifa muhimu, inashauriwa kutumia utafsiri wa kitaalamu wa binadamu. Hatuna wajibu wowote kwa kutokuelewana au tafsiri potovu zinazotokana na matumizi ya tafsiri hii.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->