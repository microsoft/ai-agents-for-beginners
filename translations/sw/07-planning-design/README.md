[![Mpangilio wa Muundo wa Mipangilio](../../../translated_images/sw/lesson-7-thumbnail.f7163ac557bea123.webp)](https://youtu.be/kPfJ2BrBCMY?si=9pYpPXp0sSbK91Dr)

> _(Bonyeza juu ya picha kuona video ya somo hili)_

# Mpangilio wa Muundo

## Utangulizi

Somo hili litashughulikia

* Kufafanua lengo kuu wazi na kugawanya kazi tata kuwa kazi ndogo ndogo zinazoweza kudhibitiwa.
* Kutumia matokeo yaliyo pangwa kwa mwonekano wa kuaminika na unaoeleweka na mashine.
* Kutumia mbinu inayotegemea matukio kushughulikia kazi zinazobadilika na ingizo zisizotarajiwa.

## Malengo ya Kujifunza

Baada ya kumaliza somo hili, utakuwa na uelewa kuhusu:

* Kubaini na kuweka lengo kuu kwa wakala wa AI, kuhakikisha anajua wazi kinachotakiwa kufanikishwa.
* Kugawanya kazi tata kuwa kazi ndogo ndogo zinazoweza kudhibitiwa na kuzipanga kwa mpangilio wa mantiki.
* Kuwapa mawakala zana sahihi (mfano, zana za utafutaji au zana za uchambuzi wa data), kuamua lini na jinsi zitakavyotumika, na kushughulikia hali zisizotarajiwa zinazojitokeza.
* Kutathmini matokeo ya kazi ndogo, kupima utendaji, na kurudia hatua ili kuboresha matokeo ya mwisho.

## Kufafanua Lengo Kuu na Kugawanya Kazi

![Kufafanua Malengo na Kazi](../../../translated_images/sw/defining-goals-tasks.d70439e19e37c47a.webp)

Kazi nyingi za dunia halisi ni ngumu sana kushughulikia kwa hatua moja. Wakala wa AI anahitaji lengo fupi la kuongoza mipangilio na hatua zake. Kwa mfano, fikiria lengo:

    "Tengeneza ratiba ya usafiri ya siku 3."

Ingawa ni rahisi kusema, bado inahitaji uboreshaji. Kadri lengo linavyokuwa wazi zaidi, ndivyo wakala (na washirikiano wowote wa binadamu) wanaweza kuzingatia kufanikisha matokeo sahihi, kama vile kutengeneza ratiba kamili yenye chaguo za ndege, mapendekezo ya hoteli, na mapendekezo ya shughuli.

### Kugawanya Kazi

Kazi kubwa au tata huwa rahisi kusimamia wakati zina gawiwa kuwa kazi ndogo ndogo zenye lengo.
Kwa mfano wa ratiba ya usafiri, unaweza kugawanya lengo kuwa:

* Kuweka Tiketi za Ndege
* Kuweka Hoteli
* Kukodisha Gari
* Urekebishaji Binafsi

Kila kazi ndogo inaweza kushughulikiwa na mawakala au michakato maalum. Wakala mmoja anaweza kuangazia kutafuta ofa bora za ndege, mwingine akazingatia kuweka hoteli, na kadhalika. Wakala wa kuratibu au "wa chini ya mto" anaweza kusanya matokeo haya kuwa ratiba moja inayoshirikiana kwa mtumiaji wa mwisho.

Njia hii ya moduli pia huruhusu maboresho hatua kwa hatua. Kwa mfano, unaweza kuongeza mawakala maalum kwa Mapendekezo ya Chakula au Mapendekezo ya Shughuli za Mtaa na kuboresha ratiba kadri muda unavyoenda.

### Matokeo Yaliyo Pangwa

Models za Lugha Kubwa (LLMs) zinaweza kuzalisha matokeo yaliyo pangwa (mfano JSON) ambayo ni rahisi kwa mawakala au huduma za chini ya mto kuyasoma na kuyashughulikia. Hii ni muhimu hasa katika muktadha wa mawakala wengi, ambapo tunaweza kutekeleza kazi hizi baada ya kupokea matokeo ya mpangilio.

Kipande kifuatacho cha Python kinaonyesha wakala wa mpangilio akigawanya lengo kuwa kazi ndogo na kutengeneza mpango uliopangwa:

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

# Mtindo wa Kazi Ndogo ya Safari
class TravelSubTask(BaseModel):
    task_details: str
    assigned_agent: AgentEnum  # tunataka kumteua wakala kwa kazi hiyo

class TravelPlan(BaseModel):
    main_task: str
    subtasks: List[TravelSubTask]
    is_greeting: bool

provider = FoundryChatClient(
    project_endpoint=os.environ["AZURE_AI_PROJECT_ENDPOINT"],
    model=os.environ["AZURE_AI_MODEL_DEPLOYMENT_NAME"],
    credential=AzureCliCredential(),
)

# Eleza ujumbe wa mtumiaji
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

### Wakala wa Mpangilio kwa Ushirikiano wa Mawakala Wengi

Katika mfano huu, Wakala wa Kutuma Semantic anapokea ombi la mtumiaji (mfano, "Nahitaji mpango wa hoteli kwa safari yangu.").

Kisha mpangiliaji:

* Anapokea Mpango wa Hoteli: Mpangiliaji huchukua ujumbe wa mtumiaji na, kulingana na kiito cha mfumo (pamoja na maelezo ya mawakala waliopo), hutengeneza mpango wa kusafiri uliopangwa.
* Anataja Mawakala na Zana Zao: rejista ya mawakala ina orodha ya mawakala (mfano, kwa ndege, hoteli, kukodisha gari, na shughuli) pamoja na kazi au zana wanazotoa.
* Anapeleka Mpango kwa Mawakala Husika: Kulingana na idadi ya kazi ndogo, mpangiliaji hutuma ujumbe moja kwa moja kwa wakala maalum (kwa hali ya kazi moja) au kuandaa kupitia meneja wa mazungumzo wa kundi kwa ushirikiano wa mawakala wengi.
* Anahitimisha Matokeo: Mwisho, mpangiliaji hutoa muhtasari wa mpango ulio tengenezwa kwa uwazi.
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

# Mfano wa Kazi Ndogo ya Safari

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

from agent_framework.foundry import FoundryChatClient
from azure.identity import AzureCliCredential

# Unda mteja

provider = FoundryChatClient(
    project_endpoint=os.environ["AZURE_AI_PROJECT_ENDPOINT"],
    model=os.environ["AZURE_AI_MODEL_DEPLOYMENT_NAME"],
    credential=AzureCliCredential(),
)

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

# Chapisha maudhui ya majibu baada ya kuipakia kama JSON

pprint(json.loads(response_content))
```

Kinachofuata ni matokeo ya msimbo ulio hapo awali na unaweza kisha kutumia matokeo haya yaliyo pangwa kwenda kwa `assigned_agent` na kuhitimisha mpango wa safari kwa mtumiaji wa mwisho.

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

Mfano wa daftari lenye mfano wa msimbo uliopita upo [hapa](./code_samples/07-python-agent-framework.ipynb).

### Mpangilio wa Kurudia

Baadhi ya kazi zinahitaji mwingiliano wa kurudiana au mipango tena, ambapo matokeo ya kazi ndogo yanaathiri kazi ifuatayo. Kwa mfano, ikiwa wakala atagundua muundo wa data usiotarajiwa wakati wa kuweka tiketi za ndege, anaweza kuhitaji kubadilisha mkakati wake kabla ya kuendelea na kuweka hoteli.

Zaidi ya hayo, mrejesho wa mtumiaji (mfano, binadamu anapochagua kwenda na ndege mapema zaidi) unaweza kuanzisha mipango ya sehemu tena. Njia hii ya mabadiliko ya mara kwa mara inahakikisha suluhisho la mwisho linaendana na vizingiti halisi vya dunia na upendeleo zinazo badilishana za mtumiaji.

mfano wa msimbo

```python
import os
from agent_framework.foundry import FoundryChatClient
from azure.identity import AzureCliCredential
#.. sawa na msimbo wa awali na pitia historia ya mtumiaji, mpango wa sasa

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

Kwa mipangilio kamili zaidi angalia Magnetic One <a href="https://www.microsoft.com/research/articles/magentic-one-a-generalist-multi-agent-system-for-solving-complex-tasks" target="_blank">Blogpost</a> kwa kutatua kazi tata.

## Muhtasari

Katika makala haya tumetazama mfano wa jinsi tunavyoweza kuunda mpangiliaji ambaye anaweza kuchagua kwa nguvu mawakala waliopo waliotajwa. Matokeo ya Mpangiliaji hugawanya kazi na kugawa mawakala ili zileteke. Inadhaniwa mawakala wana upatikanaji wa kazi/zana zinazohitajika kutekeleza kazi husika. Zaidi ya mawakala, unaweza kuongeza mifumo mingine kama vile tafakari, muhtasari, na mazungumzo ya mzunguko kwa kuboresha zaidi.

## Rasilimali Zaidi

Magnetic One - Mfumo wa mawakala wengi wa mtaalam wa jumla kwa kutatua kazi kubwa na umefikia matokeo mazuri katika majukwaa changamano ya mawakala. Marejeleo: <a href="https://www.microsoft.com/research/articles/magentic-one-a-generalist-multi-agent-system-for-solving-complex-tasks" target="_blank">Magnetic One</a>. Katika utekelezaji huu mpangilio huunda mipango maalum ya kazi na kuwasilisha kazi hizo kwa mawakala waliopo. Zaidi ya kupanga mpangilio, mpangilio pia hutumia mfumo wa kufuatilia maendeleo ya kazi na kuripanga tena kama inahitajika.

### Una Maswali Zaidi Kuhusu Muundo wa Mpangilio?

Jiunge na [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D) kukutana na wanaojifunza wengine, kuhudhuria saa za ofisi na kupata majibu ya maswali yako kuhusu AI Agents.

## Somo lililopita

[Kujenga Mawakala wa AI wa Kuaminika](../06-building-trustworthy-agents/README.md)

## Somo linalofuata

[Muundo wa Mawakala Wengi](../08-multi-agent/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Kionyozo**:
Hati hii imetafsiriwa kwa kutumia huduma ya tafsiri ya AI [Co-op Translator](https://github.com/Azure/co-op-translator). Ingawa tunajitahidi kupata usahihi, tafadhali fahamu kwamba tafsiri za kiotomatiki zinaweza kuwa na makosa au upungufu wa usahihi. Hati ya asili katika lugha yake halisi inapaswa kuchukuliwa kama chanzo cha mamlaka. Kwa taarifa muhimu, tafsiri ya kitaalamu inayofanywa na binadamu inapendekezwa. Hatutojibu kwa kuelewa vibaya au tafsiri potofu zinazotokea kutokana na matumizi ya tafsiri hii.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->