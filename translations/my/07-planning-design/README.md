[![Planning Design Pattern](../../../translated_images/my/lesson-7-thumbnail.f7163ac557bea123.webp)](https://youtu.be/kPfJ2BrBCMY?si=9pYpPXp0sSbK91Dr)

> _(ဤသင်ခန်းစာ၏ ဗွီဒီယိုကို ကြည့်ရန် အပေါ်တွင်ရှိသည့် ပုံကို နှိပ်ပါ)_

# စီမံခန့်ခွဲမှု ဒီဇိုင်း

## မိတ်ဆက်

ဤသင်ခန်းစာတွင် ဖော်ပြမည့်အချက်များမှာ

* ပန်းတိုင်ရှင်းလင်းစွာ သတ်မှတ်ခြင်းနှင့် စိန်ခေါ်မည့် တာဝန်ရှုပ်ထွေးမှုကို စီမံခန့်ခွဲရန် အလုပ်အမှုခွဲခြင်း။
* ယုံကြည်စိတ်ချရပြီး စက်ကိရိယာဖတ်ရှုနိုင်သော ပြန်လည်ဖြေကြားမှုများအတွက် ဖွဲ့စည်းထားသော ထုတ်လွှင့်ချက်ကို အသုံးပြုခြင်း။
* ပရိုဂရမ်ပုံစံအရ လှုပ်ရှားမှုဖြစ်ရပ်နှင့် မမျှော်လင့်ထားသော input များကို ကိုင်တွယ်ရန် ဖြစ်ရပ်အခြေပြု နည်းလမ်းကို လျှောက်ထားခြင်း။

## သင်ယူရမည့် ရည်မှန်းချက်များ

ဤသင်ခန်းစာပြီးဆုံးသည့်အခါ၊ သင်သည်

* AI ကိုယ်စားလှယ်တစ်ဦးအတွက် ပန်းတိုင်အား သတ်မှတ်နိုင်ပြီး ထိုတွင် ရောက်ရှိရန် လိုအပ်သောအရာကို ရှင်းလင်းစွာ သိရှိနိုင်ရန်။
* ရှုပ်ထွေးသောတစ်ခုနဲ့တစ်ခု ဆက်စပ်ထားသော အလုပ်အမှုခွဲသေးစိတ်များကို ခွဲထုတ်ပြီး နည်းဖြင့် စီစဉ်နိုင်ရန်။
* ကိုယ်စားလှယ်များအား သင့်တော်သောကိရိယာများ (ဥပမာ၊ ရှာဖွေကိရိယာ သို့မဟုတ် ဒေတာ विश्लेषण ကိရိယာများ) ဖြင့် အချိန်နှင့် နည်းလမ်းကို ဆုံးဖြတ်ရန်၊ မမျှော်လင့်သော အခြေအနေများကို ကိုင်တွယ်နိုင်ရန်။
* လူမှုဆက်ဆံမှုအဖွဲ့အစည်းများအား သုံးသပ်ခြင်း၊ စွမ်းဆောင်ရည်တိုင်းတာခြင်းနှင့် အလုပ်လုပ်မှုများကို တိုးတက်အောင် ပြန်လှည့်ဆောင်ရွက်နိုင်ရန်။

## ပန်းတိုင် သတ်မှတ်ခြင်းနှင့် အလုပ်ခွဲဝေခြင်း

![Defining Goals and Tasks](../../../translated_images/my/defining-goals-tasks.d70439e19e37c47a.webp)

အများဆုံး အလုပ်များသည် တစ်ဆင့်တည်း ရှင်းလင်းစွာ ဖော်ဆောင်ရန် ခက်ခဲသည်။ AI ကိုယ်စားလှယ်သည် ၎င်း၏ စီမံချက်နှင့် လှုပ်ရှားမှုများကို ဦးတည်ရန် ရှင်းလင်းသော ရည်မှန်းချက် တစ်ခု လိုအပ်သည်။ ဥပမာဖြစ်သော ပန်းတိုင်မှာ

    "၃ ရက်ခရီးစဉ် စီမံချက် တစ်ခု ဖန်တီးရန်။"

ဤပန်းတိုင်သည် ရိုးရှင်းသော်လည်း ပြည့်စုံအောင် ရေးဆွဲရန် လိုအပ်သည်။ ပန်းတိုင် ပိုမိုရှင်းလင်းလျှင် ကိုယ်စားလှယ်နှင့် လူသားချိတ်ဆက်သူများသည် မှန်ကန်သော ထွက်ရှိမှုရရှိရန် အာရုံစိုက်နိုင်မှာ ဖြစ်ပြီး၊ စီးပွားရေး ခရီးစဉ်တွင် လေယာဥ်လက်မှတ်ရွေးချယ်မှု၊ ဟိုတယ် အကြံပြုချက်များနှင့် လှုပ်ရှားမှု အကြံပြုချက်များ ပါဝင်သော စုပေါင်းဆွဲဆုံးနိင်မှု ရရှိမည်ဖြစ်သည်။

### တာဝန်ခွဲခြမ်းခြင်း

ကြီးမားသည့် သို့မဟုတ် ရှုပ်ထွေးသော တာဝန်များကို သေးငယ်သော၊ ရည်မှန်းချက် ရှိသည့် အလုပ်ခွဲသေးစိတ်များခွဲပါက စီမံရန် လွယ်ကူသည်။
ခရီးစဉ် မူရင်းပန်းတိုင်သည်-

* လေယာဉ်လက်မှတ်ဘွတ်ကင်
* ဟိုတယ်ဘွတ်ကင်
* ကားငှားရမ်းခြင်း
* ကိုယ်ပိုင်စိတ်ကြိုက်မှု

တာဝန်တိုင်းသည် အထူးပြု ကိုယ်စားလှယ်များ သို့မဟုတ် လုပ်ငန်းစဉ်များမှ ဖြေရှင်းနိုင်သည်။ တစ်ဦးက အကောင်းဆုံး လေယာဉ်ပျံစျေးနှုန်းများ ရှာဖွေရာတွင် ကျွမ်းကျင်နိုင်သလောက်၊ တစ်ဦးက ဟိုတယ်ဘွတ်ကင်တွင် အာရုံစိုက်နိုင်သည်။ပြီးလျှင် “အောက်ခံ” ကိုယ်စားလှယ်တစ်ယောက်က ယင်းတို့ရလဒ်များကို စုပေါင်းပြီး သုံးစွဲသူအတွက် တစ်ခုတည်းသော ခရီးစဉ်အား တင်ပြနိုင်သည်။

ဤ ပုံစံသည် အဆင့်ဆင့် တိုးတက်မှုများကိုလည်း ခွင့်ပြုသည်။ ဥပမာအနေဖြင့် အစားအစာအကြံပြုချက်များ သို့မဟုတ် ဒေသဆိုင်ရာ လှုပ်ရှားမှုအကြံပြုချက်များအတွက် အထူးပြု ကိုယ်စားလှယ်များ ထည့်သွင်းပြီး ခရီးစဉ်ကို အချိန်နှင့်အမျှ တိုက်ရိုင်းမှီသောအတိုင်း ဖြည့်စွက်နိုင်သည်။

### ဖွဲ့စည်းရေး ထုတ်လွှင့်ချက်

ကြီးမားသော ဘာသာစကား မော်ဒယ်များ(LLMs) က JSON ကဲ့သို့ ဖွဲ့စည်းရေး ထုတ်လွှင့်ချက်ကို ထုတ်ပေးနိုင်ပြီး ၎င်းကို အောက်စွန်း အေးဂျင့်များ သို့မဟုတ် ဝန်ဆောင်မှုများက ပိုမို လွယ်ကူစွာ ဖတ်ရှုကြည့်ရှု နှင့် ချိန်ညှိနိုင်သည်။ ၎င်းသည် အများပြည်သူကိုယ်စားလှယ် ဂဏန်းများကို ရရှိပါက စီမံချက်ထုတ်လွှင့်ချက်ရရှိပြီးနောက် မှာ ဒီတာဝန်များကို တပ်ဆင်နိုင်သည်။

အောက်ပါ Python ကိုဒ် အပိုင်းက ရိုးရှင်းသော စီမံခန့်ခွဲသူ ကိုယ်စားလှယ်တစ်ယောက်က ပန်းတိုင်ကို တာဝန်ခွဲခြမ်းခြင်းနှင့် ဖွဲ့စည်းရေးရှိသော စီမံကိန်းထုတ်ပေးခြင်းကို ပြသသည်။

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

# ခရီးသွားခွဲခြမ်းအလုပ်မော်ဒယ်
class TravelSubTask(BaseModel):
    task_details: str
    assigned_agent: AgentEnum  # အလုပ်ကို အေးဂျင့်ထံ သတ်မှတ်လိုသည်

class TravelPlan(BaseModel):
    main_task: str
    subtasks: List[TravelSubTask]
    is_greeting: bool

provider = FoundryChatClient(
    project_endpoint=os.environ["AZURE_AI_PROJECT_ENDPOINT"],
    model=os.environ["AZURE_AI_MODEL_DEPLOYMENT_NAME"],
    credential=AzureCliCredential(),
)

# အသုံးပြုသူစာသားကို သတ်မှတ်ပါ
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

### မျိုးစုံ အေးဂျင့် စီမံချက် အတွင်း စီမံခန့်ခွဲသူ

ဤ ဥပမာတွင် Semantic Router Agent သည် အသုံးပြုသူ တောင်းဆိုချက်(ဥပမာ - "ကျွန်ုပ်၏ ခရီးနှင့်ပတ်သက်၍ ဟိုတယ် စီမံချက်တစ်ခု လိုအပ်သည်။") ရရှိသည်။

စီမံခန့်ခွဲသူသည်

* ဟိုတယ် စီမံချက် ရရှိသည် - စီမံခန့်ခွဲသူသည် အသုံးပြုသူ၏ စာတိုစာလုံးများကို လက်ခံပြီး၊ စနစ်ဒစ္‌တာဖြင့် (အရာရှိ အေးဂျင့် အချက်အလက်များပါဝင်သော) ဖွဲ့စည်းရေးရှိသော ခရီးစဉ်စီမံချက်ထုတ်ပေးသည်။
* ကိရိယာများနှင့် အေးဂျင့်များစာရင်း - အေးဂျင့် စာရင်းထဲတွင် လေယာဉ်၊ ဟိုတယ်၊ ကားငှားခြင်းနှင့် လှုပ်ရှားမှုတို့အတွက် အေးဂျင့်များစာရင်းနှင့် ၎င်းတို့ပေးသော အလုပ်ဆောင်မှုများ သို့မဟုတ် ကိရိယာများပါရှိသည်။
* စီမံချက်ကို သက်ဆိုင်ရာ အေးဂျင့်ဆီ ပို့သည် - တာဝန်ခွဲအရေအတွက်အပေါ်မူတည်၍ စီမံခန့်ခွဲသူသည် တစ်ဦးတည်းသော အေးဂျင့်သို့တိုက်ရိုက် အကြောင်းကြားရန် မဟုတ်လျှင် မျိုးစုံအေးဂျင့် ပဋိပက္ခအဖွဲ့မှ တစ်ဆင့် စီမံချက်ကို ပေးပို့သည်။
* ရလဒ်ကို အနှစ်ချုပ်တင်ပြသည် - နောက်ဆုံးတွင် စီမံခန့်ခွဲသူသည် ဖန်တီးထားသည့် စီမံချက်ကို တိကျလွယ်ကူစွာ တင်ပြပေးသည်။
အောက်ပါ Python ကုဒ် နမူနာသည် အဆင့်များကို ပြသသည်။

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

# ခရီးသွား အတူတကွလုပ်ငန်း မော်ဒယ်

class TravelSubTask(BaseModel):
    task_details: str
    assigned_agent: AgentEnum # ကျွန်တော်တို့ အလုပ်ကို ကိုယ်စားလှယ်ထံ ပေးလိုသည်

class TravelPlan(BaseModel):
    main_task: str
    subtasks: List[TravelSubTask]
    is_greeting: bool
import json
import os
from typing import Optional

from agent_framework.foundry import FoundryChatClient
from azure.identity import AzureCliCredential

# ဖောက်သည်ကို ဖန်တီးပါ

provider = FoundryChatClient(
    project_endpoint=os.environ["AZURE_AI_PROJECT_ENDPOINT"],
    model=os.environ["AZURE_AI_MODEL_DEPLOYMENT_NAME"],
    credential=AzureCliCredential(),
)

from pprint import pprint

# အသုံးပြုသူစာတိုက်ကို သတ်မှတ်ပါ

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

# JSON အဖြစ် ဖတ်ရှုပြီးနောက် တုံ့ပြန်မှုအကြောင်းအရာကို ထုတ်ပြပါ

pprint(json.loads(response_content))
```

ယခင်ကုဒ်မှ ထွက်ရှိသော output သည် `assigned_agent` သို့ လမ်းညွှန်ရန်နှင့် သုံးစွဲသူများအတွက် ခရီးစဉ်ကို စုစည်းတင်ပြရန် အသုံးပြုနိုင်ပါသည်။

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

ယခင်ကုဒ်နမူနာပါရှိသည့် notebook ကို [ဒီမှာ](./code_samples/07-python-agent-framework.ipynb) ရယူနိုင်ပါသည်။

### ပြန်လည်ဆန်းစစ်စီမံချက်

တာဝန်တချို့သည် နောက်ပြန်ပြန်ဆက်မှု သို့မဟုတ် ပြန်လည်စီမံချက်ချရန် လိုအပ်သည့် အလုပ်များ ဖြစ်လာနိုင်ပြီး၊ တစ်ခုတည်းသော တာဝန်ဖြေရှင်းမှု၏ ရလဒ်သည် နောက်တစ်ခုကို ထိခိုက်မှုရှိပါသည်။ ဥပမာ၊ လေယာဉ်လက်မှတ်ဘွတ်ကင်လုပ်သည့်အခါ မမျှော်လင့်ထားသော ဒေတာပုံစံတွေ့ရှိလျှင်၊ ဟိုတယ်ဘွတ်ကင်လုပ်ခြင်းသို့ ရောက်가기မတိုင်ခင် မူဝါဒကို အလျင်အမြန် အပြောင်းအလဲချရပါမည်။

ထို့အပြင် အသုံးပြုသူ၏ တုံ့ပြန်ချက် (ဥပမာ၊ လူတစ်ဦးက ပိုမိုလျင်မြန်သော လေယာဉ်တစ်စီးကို ကြိုက်နှစ်သက်သည်ဟု ဆုံးဖြတ်) သည် အပိုင်းတစ်စိတ်တစ်ပိုင်း ပြန်လည်စီမံမှုအား ဖြစ်ပေါ်စေသည်။ ဤအရာသည် နောက်ဆုံးဖြေရှင်းချက်သည် လက်တွေ့ကန့်သတ်ချက်များနှင့် အသုံးပြုသူ့ လိုအပ်ချက်များနှင့် ကိုက်ညီမှုရှိစေရန် အောင်မြင်သည်။

ဥပမာကုဒ်

```python
import os
from agent_framework.foundry import FoundryChatClient
from azure.identity import AzureCliCredential
#.. ယခင်ကုဒ်နှင့်တူပြီး အသုံးပြုသူသမိုင်း, လက်ရှိအစီအစဉ်ကိုဆက်လက်ထုတ်ပေးသည်

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
# .. ပြန်လည်အစီအစဉ်ချပြီး အလုပ်များကို သက်ဆိုင်ရာအေးဂျင့်များထံ ပို့ပေးသည်
```

ပိုမိုကျယ်ပြန့်သော စီမံခန့်ခွဲမှုအတွက် Magnet One <a href="https://www.microsoft.com/research/articles/magentic-one-a-generalist-multi-agent-system-for-solving-complex-tasks" target="_blank">Blogpost</a> ကို ကြည့်ရှုနိုင်ပါသည်။

## အကျဉ်းချုပ်

ဤဆောင်းပါးတွင် ကြည့်ရှုလိုက်သော နမူနာဖြစ်သော စီမံခန့်ခွဲသူသည် သတ်မှတ်ထားသောရရှိနိုင်သော ကိုယ်စားလှယ်များကို မျိုးစုံအကြား သဘောတူညီမှုပေါ် မှီ၍ ရွေးချယ်နိုင်သည်။ စီမံခန့်ခွဲသူ၏ ထုတ်လွှင့်ချက်သည် တာဝန်များကို ခွဲဝေပြီး ကိုယ်စားလှယ်များကို အပ်နှံသည်၊ ထို့ကြောင့် စီမံချက်များ ဆောင်ရွက်နိုင်သည်။ ကိုယ်စားလှယ်များသည် အလုပ်တစ်ခု ဆောင်ရွက်ရန် လိုအပ်သည့် လုပ်ငန်းစဉ်များ/ကိရိယာများကို အသုံးပြုရန် ဖြစ်သည်ဟု ထင်မှတ်ရမည်။ ကိုယ်စားလှယ်များအပြင် ပြန်လည်သုံးသပ်ခြင်း၊ အနှစ်ချုပ်ခြင်း၊ နှင့် လှည့်ပတ်ပေးသော စကားပြောချက်များကဲ့သို့ နောက်ထပ် ပုံစံများကိုလည်း ထည့်သွင်းနိုင်သည်။

## နောက်ထပ် ရင်းမြစ်များ

Magnet One - ရှုပ်ထွေးသော တာဝန်များကို ဖြေရှင်းနိုင်သည့် Generalist Multi-Agent System နှင့် အလေးပေးခြင်း ရရှိခဲ့ပြီး စိန်ခေါ်မှုများပြားသည့် အေးဂျင့်စနစ် များမှာ ထူးချွန်သော ရလဒ်များရရှိထားသည်။ ကိုးကားရန် - <a href="https://www.microsoft.com/research/articles/magentic-one-a-generalist-multi-agent-system-for-solving-complex-tasks" target="_blank">Magentic One</a> ။ဤစနစ်တွင် ဆောင်ရွက်သူသည် တာဝန်အတိအကျ သတ်မှတ်ထားသည့် စီမံချက်များကို ဖန်တီးပြီး တာဝန်များကို ရရှိနိုင်သော ကိုယ်စားလှယ်များထံ အပ်နှံသည်။ စီမံချက်လုပ်ခြင်းအပြင် ဆောင်ရွက်မှုတို့ အား ကြီးကြပ်မှုနှင့် လိုအပ်ပါက ပြန်လည်စီမံရန် စနစ်လည်း ပါရှိသည်။

### စီမံခန့်ခွဲမှု ဒီဇိုင်း ပုံစံအကြောင်း ပိုမိုမေးလေ့ရှိပါသလား?

အခြား သင်ယူသူများကို တွေ့ဆုံရန်၊ ရုံးချိန်များတက်ရောက်ရန်နှင့် သင့် AI ကိုယ်စားလှယ်မေးခွန်းများကို ဖြေရှင်းဖို့ [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D) တွင် ပါဝင်ဆွေးနွေးရအောင်။

## ယခင် သင်ခန်းစာ

[ယုံကြည်ရသော AI ကိုယ်စားလှယ်များ တည်ဆောက်ခြင်း](../06-building-trustworthy-agents/README.md)

## နောက်တစ်ခု သင်ခန်းစာ

[မျိုးစုံ အေးဂျင့် ဒီဇိုင်း ပုံစံ](../08-multi-agent/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ပြောကြားချက်**
ဤစာတမ်းကို AI ဘာသာပြန်ဝန်ဆောင်မှု [Co-op Translator](https://github.com/Azure/co-op-translator) အသုံးပြု၍ ဘာသာပြန်ထားပါသည်။ ကျွန်ုပ်တို့သည် တိကျမှန်ကန်မှုအတွက် ကြိုးပမ်းနေသော်လည်း၊ စက်ကိရိယာဘာသာပြန်ခြင်းများတွင် အမှားများ သို့မဟုတ် မှားယွင်းချက်များ ပါဝင်နိုင်ကြောင်း သတိပြုပါရန် လိုအပ်ပါသည်။ မူလစာတမ်းကို မူရင်းဘာသာဖြင့်သာ ယုံကြည်စိတ်ချရသော အချက်အလက်အဖြစ် သတ်မှတ်သင့်သည်။ အရေးကြီးသည့် သတင်းအချက်အလက်များအတွက် ပရော်ဖက်ရှင်နယ် လူသားဘာသာပြန်သူဝန်ဆောင်မှုကို အကြံပြုပါသည်။ ဤဘာသာပြန်ချက်ကို အသုံးပြုခြင်းမှ ဖြစ်ပေါ်လာသော နားလည်မှုကွာခြားမှုများ သို့မဟုတ် မမှန်ကန်သော အသုံးပြုမှုများအတွက် ကျွန်ုပ်တို့ တာဝန်မခံပါ။
<!-- CO-OP TRANSLATOR DISCLAIMER END -->