[![Multi-Agent Design](./images/lesson-8-thumbnail.png)](https://youtu.be/V6HpE9hZEx0?si=A7K44uMCqgvLQVCa)
> _(ဤသင်ခန်းစာ၏ ဗီဒီယိုကြည့်ရှုရန် အထက်ပါ ပုံပေါ်တွင် နှိပ်ပါ)_

# Planning Design Pattern (စီမံကိန်းဒီဇိုင်းပုံစံ)

## နိဒါန်း

ဤသင်ခန်းစာတွင် အောက်ပါအချက်များကို လေ့လာရမည်-

* ရှင်းလင်းသော ခြုံငုံရည်ရွယ်ချက်တစ်ခုကို သတ်မှတ်ခြင်းနှင့် ရှုပ်ထွေးသော လုပ်ငန်းတစ်ခုကို စီမံနိုင်သော အပိုင်းငယ်များအဖြစ် ခွဲခြားခြင်း
* ပိုမို ယုံကြည်စိတ်ချရပြီး စက်ဖတ်နိုင်သော တုံ့ပြန်မှုများအတွက် တည်ဆောက်ပုံအထွက်ကို အသုံးပြုခြင်း
* ပြောင်းလဲနိုင်သော လုပ်ငန်းများနှင့် မမျှော်လင့်သော အခြေအနေများကို ကိုင်တွယ်ရန် event-driven approach အား အသုံးချခြင်း

## သင်ယူမည့်ရည်မှန်းချက်များ

ဤသင်ခန်းစာပြီးဆုံးပါက အောက်ပါအချက်များအတွက် နားလည်မှုရရှိမည်-

* AI agent တစ်ခုအတွက် ခြုံငုံရည်ရွယ်ချက်ကို ခွဲခြားသတ်မှတ်ခြင်းနှင့် အောင်မြင်ရန်လိုအပ်သည့်အရာကို ရှင်းလင်းစွာ သိရှိအောင်ပြုလုပ်ခြင်း
* ရှုပ်ထွေးသော အလုပ်တစ်ခုကို စီမံနိုင်သော အခွဲငယ်များအဖြစ် ခွဲခြားပြီး ယုက္တိဆီလျော်သော အစီအစဉ်အတိုင်း စုစည်းခြင်း
* Agent များကို သင့်လျော်သော ကိရိယာများ (ဥပမာ- ရှာဖွေမှုကိရိယာများ သို့မဟုတ် ဒေတာခွဲခြမ်းစိတ်ဖြာရေးကိရိယာများ) ဖြင့် တပ်ဆင်ပေးခြင်း၊ ၎င်းတို့ကို မည်သည့်အချိန်နှင့် ဘယ်လိုအသုံးပြုရမည်ကို ဆုံးဖြတ်ခြင်းနှင့် မမျှော်လင့်သော အခြေအနေများကို ကိုင်တွယ်ခြင်း
* အခွဲငယ်လုပ်ငန်းများ၏ ရလဒ်များကို အကဲဖြတ်ခြင်း၊ စွမ်းဆောင်ရည်ကို တိုင်းတာခြင်းနှင့် နောက်ဆုံးရလဒ်ကို တိုးတက်စေရန် လုပ်ဆောင်ချက်များကို ထပ်မံပြုလုပ်ခြင်း

## ခြုံငုံရည်ရွယ်ချက်ကို သတ်မှတ်ခြင်းနှင့် လုပ်ငန်းကို ခွဲခြမ်းခြင်း

လက်တွေ့ကမ္ဘာတွင်ရှိသော လုပ်ငန်းအများစုသည် အဆင့်တစ်ဆင့်တည်းဖြင့် ကိုင်တွယ်ရန် အလွန်ရှုပ်ထွေးပါသည်။ AI agent တစ်ခုသည် ၎င်း၏ စီမံကိန်းနှင့် လုပ်ဆောင်ချက်များကို လမ်းညွှန်ရန် တိကျသော ရည်မှန်းချက်တစ်ခု လိုအပ်ပါသည်။ ဥပမာအားဖြင့်-

    "၃ ရက်ကြာ ခရီးစဉ်အစီအစဉ်တစ်ခု ပြုစုပါ"

ဤအရာသည် ရိုးရှင်းစွာ ဖော်ပြထားသော်လည်း နောက်ထပ် သေသေချာချာ ပြင်ဆင်ရန် လိုအပ်သေးသည်။ ရည်ရွယ်ချက် ပိုမို ရှင်းလင်းလေ၊ agent (နှင့် လူသားအလုပ်ဖော်များ) သည် လေယာဉ်ဖျင့်ရွေးချယ်မှုများ၊ ဟိုတယ်အကြံပြုချက်များနှင့် လှုပ်ရှားမှုအကြံပြုချက်များပါဝင်သော ပြည့်စုံသော ခရီးစဉ်အစီအစဉ်တစ်ခု ဖန်တီးခြင်းကဲ့သို့ မှန်ကန်သော ရလဒ်ကို အောင်မြင်စေရန် ပိုမို အာရုံစိုက်နိုင်လေ ဖြစ်သည်။

### လုပ်ငန်းခွဲခြမ်းခြင်း

ကြီးမားသော သို့မဟုတ် ရှုပ်ထွေးသော လုပ်ငန်းများသည် ပိုမိုသေးငယ်ပြီး ရည်မှန်းချက်ဗဟိုပြုသော အခွဲငယ်လုപ်ငန်းများအဖြစ် ခွဲခြားသောအခါ ပိုမို စီမံနိုင်လေ ဖြစ်ပါသည်။

ခရီးစဉ်အစီအစဉ်ဥပမာအတွက် ရည်ရွယ်ချက်ကို အောက်ပါအတိုင်း ခွဲခြားနိုင်သည်-

* လေယာဉ်ဖျင့်ကြိုတင်မှာထားခြင်း
* ဟိုတယ်ကြိုတင်မှာထားခြင်း
* ကားငှားရမ်းခြင်း
* ကိုယ်ရေးကိုယ်တာပြုစုခြင်း

အခွဲငယ်လုပ်ငန်းတစ်ခုစီကို အထူးပြု agent များ သို့မဟုတ် လုပ်ငန်းစဉ်များဖြင့် ကိုင်တွယ်နိုင်ပါသည်။ Agent တစ်ခုသည် အကောင်းဆုံး လေယာဉ်ဖျင့်အရောင်းအ၀ယ်များကို ရှာဖွေရာတွင် အထူးကျွမ်းကျင်နိုင်ပြီး၊ နောက်တစ်ခုသည် ဟိုတယ်ကြိုတင်မှာထားမှုများကို အဓိကထားနိုင်သည်၊ အခြားတစ်ခုသည် အစရှိသဖြင့်။ ပြီးတော့ ညှိနှိုင်းသော သို့မဟုတ် "downstream" agent တစ်ခုက ဤရလဒ်များကို စုစည်းပြီး အသုံးပြုသူကို ပေးရန် ညီညွတ်သော ခရီးစဉ်အစီအစဉ်တစ်ခုအဖြစ် ပြုလုပ်နိုင်သည်။

ဤ modular ချဉ်းကပ်မှုသည် တစ်ဆင့်ချင်း တိုးတက်မှုများကိုလည်း ခွင့်ပြုပါသည်။ ဥပမာအားဖြင့်၊ သင်သည် အစားအစာအကြံပြုချက်များ သို့မဟုတ် ဒေသတွင်းလှုပ်ရှားမှုအကြံပြုချက်များအတွက် အထူးပြု agent များကို ထည့်သွင်းနိုင်ပြီး အချိန်ကြာလာသည်နှင့်အမျှ ခရီးစဉ်အစီအစဉ်ကို သိုးသိုးမွေးမွေး ပြုပြင်နိုင်သည်။

### တည်ဆောက်ပုံအထွက်

Large Language Models (LLMs) များသည် downstream agent များ သို့မဟုတ် ဝန်ဆောင်မှုများအတွက် parse လုပ်ရန်နှင့် လုပ်ဆောင်ရန် ပိုမို လွယ်ကူသော တည်ဆောက်ပုံအထွက် (ဥပမာ- JSON) ကို ထုတ်လုပ်နိုင်ပါသည်။ ဤအချက်သည် multi-agent context တွင် အထူးအသုံးဝင်ပြီး၊ စီမံကိန်းအထွက်ရရှိပြီးနောက် ဤလုပ်ငန်းများကို လုပ်ဆောင်နိုင်ပါသည်။ လျင်မြန်သော အလုံးအရုံးအတွက် ဤ [blogpost](https://microsoft.github.io/autogen/stable/user-guide/core-user-guide/cookbook/structured-output-agent.html) ကို ကြည့်ရှုပါ။

အောက်ပါ Python code snippet သည် ရည်ရွယ်ချက်တစ်ခုကို အခွဲငယ်လုပ်ငန်းများအဖြစ် ခွဲခြားပြီး တည်ဆောက်ပုံအစီအစဉ်တစ်ခု ထုတ်လုပ်သော ရိုးရှင်းသော စီမံကိန်း agent တစ်ခုကို သရုပ်ပြပါသည်-

```python
from pydantic import BaseModel
from enum import Enum
from typing import List, Optional, Union
import json
import os
from typing import Optional
from pprint import pprint
from autogen_core.models import UserMessage, SystemMessage, AssistantMessage
from autogen_ext.models.azure import AzureAIChatCompletionClient
from azure.core.credentials import AzureKeyCredential

class AgentEnum(str, Enum):
    FlightBooking = "flight_booking"
    HotelBooking = "hotel_booking"
    CarRental = "car_rental"
    ActivitiesBooking = "activities_booking"
    DestinationInfo = "destination_info"
    DefaultAgent = "default_agent"
    GroupChatManager = "group_chat_manager"

# ခရီးစဉ်အခွဲငယ်လုပ်ငန်း Model
class TravelSubTask(BaseModel):
    task_details: str
    assigned_agent: AgentEnum  # လုပ်ငန်းကို agent ကို တာဝန်ပေးလိုသည်

class TravelPlan(BaseModel):
    main_task: str
    subtasks: List[TravelSubTask]
    is_greeting: bool

client = AzureAIChatCompletionClient(
    model="gpt-4o-mini",
    endpoint="https://models.inference.ai.azure.com",
    # Model နှင့် authenticate လုပ်ရန် သင့် GitHub settings တွင် personal access token (PAT) ဖန်တီးရန် လိုအပ်ပါသည်။
    # ဤနေရာတွင် လမ်းညွှန်ချက်များကို လိုက်နာ၍ PAT token ဖန်တီးပါ: https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens
    credential=AzureKeyCredential(os.environ["GITHUB_TOKEN"]),
    model_info={
        "json_output": False,
        "function_calling": True,
        "vision": True,
        "family": "unknown",
    },
)

# အသုံးပြုသူမက်ဆေ့ချ်ကို သတ်မှတ်ပါ
messages = [
    SystemMessage(content="""သင်သည် စီမံကိန်း agent တစ်ခုဖြစ်သည်။
    သင့်အလုပ်မှာ အသုံးပြုသူ၏တောင်းဆိုချက်အပေါ်အခြေခံ၍ မည်သည့် agent များကို လုပ်ဆောင်ရမည်ကို ဆုံးဖြတ်ရန်ဖြစ်သည်။
                      အောက်ပါ structure ဖြင့် JSON format ဖြင့် သင့်တုံ့ပြန်မှုကို ပေးပါ:
{'main_task': 'စင်ကာပူမှ မဲလ်ဘုန်းသို့ မိသားစုခရီးစဉ်ကို စီမံပါ။',
 'subtasks': [{'assigned_agent': 'flight_booking',
               'task_details': 'စင်ကာပူမှ မဲလ်ဘုန်းသို့ သွားလာလေယာဉ်ဖျင့်များကို ကြိုတင်မှာပါ။'}
    အောက်တွင် မတူညီသော လုပ်ငန်းများတွင် အထူးပြုသော ရရှိနိုင်သော agent များဖြစ်သည်:
    - FlightBooking: လေယာဉ်ဖျင့်ကြိုတင်မှာထားခြင်းနှင့် လေယာဉ်ဖျင့်အချက်အလက်များ ပေးခြင်းအတွက်
    - HotelBooking: ဟိုတယ်ကြိုတင်မှာထားခြင်းနှင့် ဟိုတယ်အချက်အလက်များ ပေးခြင်းအတွက်
    - CarRental: ကားငှားရမ်းခြင်းနှင့် ကားငှားရမ်းမှုအချက်အလက်များ ပေးခြင်းအတွက်
    - ActivitiesBooking: လှုပ်ရှားမှုများကြိုတင်မှာထားခြင်းနှင့် လှုပ်ရှားမှုအချက်အလက်များ ပေးခြင်းအတွက်
    - DestinationInfo: ခရီးစဉ်နေရာများအကြောင်း အချက်အလက်များ ပေးခြင်းအတွက်
    - DefaultAgent: ယေဘုယျတောင်းဆိုချက်များကို ကိုင်တွယ်ခြင်းအတွက်""", source="system"),
    UserMessage(
        content="စင်ကာပူမှ မဲလ်ဘုန်းသို့ ကလေး ၂ ယောက်ပါသော မိသားစုအတွက် ခရီးစဉ်အစီအစဉ်တစ်ခု ဖန်တီးပါ", source="user"),
]

response = await client.create(messages=messages, extra_create_args={"response_format": 'json_object'})

response_content: Optional[str] = response.content if isinstance(
    response.content, str) else None
if response_content is None:
    raise ValueError("တုံ့ပြန်မှုအကြောင်းအရာသည် မှန်ကန်သော JSON string မဟုတ်ပါ")

pprint(json.loads(response_content))
```

### Multi-Agent ညှိနှိုင်းမှုနှင့်အတူ စီမံကိန်း Agent

ဤဥပမာတွင် Semantic Router Agent တစ်ခုသည် အသုံးပြုသူ၏တောင်းဆိုချက် (ဥပမာ- "ကျွန်တော့်ခရီးစဉ်အတွက် ဟိုတယ်အစီအစဉ်တစ်ခု လိုအပ်ပါသည်။") ကို လက်ခံရရှိသည်။

ထို့နောက် planner သည်-

* ဟိုတယ်အစီအစဉ်ကို လက်ခံရရှိ: Planner သည် အသုံးပြုသူ၏မက်ဆေ့ချ်ကို လက်ခံပြီး system prompt (ရရှိနိုင်သော agent အသေးစိတ်များပါဝင်သော) အပေါ်အခြေခံ၍ တည်ဆောက်ပုံအပေါ် ခရီးစဉ်အစီအစဉ်တစ်ခုကို ထုတ်လုပ်သည်။
* Agent များနှင့် ၎င်းတို့၏ကိရိယာများကို စာရင်း: Agent registry သည် agent များ (ဥပမာ- လေယာဉ်ဖျင့်၊ ဟိုတယ်၊ ကားငှားရမ်းခြင်းနှင့် လှုပ်ရှားမှုများအတွက်) နှင့် ၎င်းတို့ကမ်းလှမ်းသော function များ သို့မဟုတ် ကိရိယာများပါသော စာရင်းတစ်ခုကို ကိုင်ဆောင်သည်။
* သက်ဆိုင်ရာ Agent များထံ အစီအစဉ်ကို လမ်းညွှန်: အခွဲငယ်လုပ်ငန်းများ အရေအတွက်အပေါ်မူတည်၍ planner သည် မက်ဆေ့ချ်ကို အထူးပြု agent တစ်ခုထံ တိုက်ရိုက်ပို့ (single-task scenarios အတွက်) သို့မဟုတ် multi-agent collaboration အတွက် group chat manager မှတစ်ဆင့် ညှိနှိုင်းသည်။
* ရလဒ်ကို အတိုချုပ်: နောက်ဆုံးတွင် planner သည် ရှင်းလင်းမှုအတွက် ထုတ်လုပ်ထားသော အစီအစဉ်ကို အတိုချုပ်ပြသည်။

အောက်ပါ Python code နမူနာသည် ဤအဆင့်များကို သရုပ်ပြပါသည်-

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

# ခရီးซဉ်အခွဲငယ်လုပ်ငန်း Model
class TravelSubTask(BaseModel):
    task_details: str
    assigned_agent: AgentEnum # လုပ်ငန်းကို agent ကို တာဝန်ပေးလိုသည်

class TravelPlan(BaseModel):
    main_task: str
    subtasks: List[TravelSubTask]
    is_greeting: bool

import json
import os
from typing import Optional
from autogen_core.models import UserMessage, SystemMessage, AssistantMessage
from autogen_ext.models.openai import AzureOpenAIChatCompletionClient

# Type-checked environment variables များဖြင့် client ကို ဖန်တီးပါ
client = AzureOpenAIChatCompletionClient(
    azure_deployment=os.getenv("AZURE_OPENAI_DEPLOYMENT_NAME"),
    model=os.getenv("AZURE_OPENAI_DEPLOYMENT_NAME"),
    api_version=os.getenv("AZURE_OPENAI_API_VERSION"),
    azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"),
    api_key=os.getenv("AZURE_OPENAI_API_KEY"),
)

from pprint import pprint

# အသုံးပြုသူမက်ဆေ့ချ်ကို သတ်မှတ်ပါ
messages = [
    SystemMessage(content="""သင်သည် စီမံကိန်း agent တစ်ခုဖြစ်သည်။
    သင့်အလုပ်မှာ အသုံးပြုသူ၏တောင်းဆိုချက်အပေါ်အခြေခံ၍ မည်သည့် agent များကို လုပ်ဆောင်ရမည်ကို ဆုံးဖြတ်ရန်ဖြစ်သည်။
    အောက်တွင် မတူညီသော လုပ်ငန်းများတွင် အထူးပြုသော ရရှိနိုင်သော agent များဖြစ်သည်:
    - FlightBooking: လေယာဉ်ဖျင့်ကြိုတင်မှာထားခြင်းနှင့် လေယာဉ်ဖျင့်အချက်အလက်များ ပေးခြင်းအတွက်
    - HotelBooking: ဟိုတယ်ကြိုတင်မှာထားခြင်းနှင့် ဟိုတယ်အချက်အလက်များ ပေးခြင်းအတွက်
    - CarRental: ကားငှားရမ်းခြင်းနှင့် ကားငှားရမ်းမှုအချက်အလက်များ ပေးခြင်းအတွက်
    - ActivitiesBooking: လှုပ်ရှားမှုများကြိုတင်မှာထားခြင်းနှင့် လှုပ်ရှားမှုအချက်အလက်များ ပေးခြင်းအတွက်
    - DestinationInfo: ခရီးစဉ်နေရာများအကြောင်း အချက်အလက်များ ပေးခြင်းအတွက်
    - DefaultAgent: ယေဘုယျတောင်းဆိုချက်များကို ကိုင်တွယ်ခြင်းအတွက်""", source="system"),
    UserMessage(content="စင်ကာပူမှ မဲလ်ဘုန်းသို့ ကလေး ၂ ယောက်ပါသော မိသားစုအတွက် ခရီးစဉ်အစီအစဉ်တစ်ခု ဖန်တီးပါ", source="user"),
]

response = await client.create(messages=messages, extra_create_args={"response_format": TravelPlan})

# JSON string အဖြစ် မှန်ကန်မှုကို သေချာစေပြီးမှ loading လုပ်ပါ
response_content: Optional[str] = response.content if isinstance(response.content, str) else None
if response_content is None:
    raise ValueError("တုံ့ပြန်မှုအကြောင်းအရာသည် မှန်ကန်သော JSON string မဟုတ်ပါ")

# JSON အဖြစ် loading လုပ်ပြီးနောက် တုံ့ပြန်မှုအကြောင်းအရာကို print လုပ်ပါ
pprint(json.loads(response_content))
```

အရင်က code မှ ရလဒ်မှာ အောက်ပါအတိုင်းဖြစ်ပြီး ထို့နောက် ဤတည်ဆောက်ပုံအထွက်ကို `assigned_agent` သို့ route လုပ်ရန်နှင့် အသုံးပြုသူကို ခရီးစဉ်အစီအစဉ်ကို အတိုချုပ်ရန် အသုံးပြုနိုင်ပါသည်-

```json
{
    "is_greeting": "False",
    "main_task": "စင်ကာပူမှ မဲလ်ဘုန်းသို့ မိသားစုခရီးစဉ်ကို စီမံပါ။",
    "subtasks": [
        {
            "assigned_agent": "flight_booking",
            "task_details": "စင်ကာပူမှ မဲလ်ဘုန်းသို့ သွားလာလေယာဉ်ဖျင့်များကို ကြိုတင်မှာပါ။"
        },
        {
            "assigned_agent": "hotel_booking",
            "task_details": "မဲလ်ဘုန်းတွင် မိသားစုနှင့်လိုက်ဖက်သော ဟိုတယ်များကို ရှာဖွေပါ။"
        },
        {
            "assigned_agent": "car_rental",
            "task_details": "မဲလ်ဘုန်းတွင် လေးယောက်ပါသော မိသားစုအတွက် သင့်လျော်သော ကားငှားရမ်းမှုကို စီစဉ်ပါ။"
        },
        {
            "assigned_agent": "activities_booking",
            "task_details": "မဲလ်ဘုန်းတွင် မိသားစုနှင့်လိုက်ဖက်သော လှုပ်ရှားမှုများကို စာရင်းပြုစုပါ။"
        },
        {
            "assigned_agent": "destination_info",
            "task_details": "မဲလ်ဘုန်းအကြောင်း ခရီးစဉ်နေရာတစ်ခုအဖြစ် အချက်အလက်များ ပေးပါ။"
        }
    ]
}
```

ရှေ့က code နမူနာပါသော နမူနာ notebook ကို [ဤနေရာ](07-autogen.ipynb) တွင် ရရှိနိုင်ပါသည်။

### ထပ်မံလုပ်ဆောင်သော စီမံကိန်းပြုလုပ်ခြင်း

အချို့သော လုပ်ငန်းများသည် နှစ်ဖက်ပြောဆိုမှု သို့မဟုတ် ပြန်လည်စီမံခြင်း လိုအပ်ပြီး အခွဲငယ်လုပ်ငန်းတစ်ခု၏ ရလဒ်သည် နောက်တစ်ခုကို လွှမ်းမိုးပါသည်။ ဥပမာအားဖြင့်၊ လေယာဉ်ဖျင့်ကြိုတင်မှာထားရာတွင် မမျှော်လင့်သော ဒေတာပုံစံကို agent က ရှာဖွေတွေ့ရှိပါက ဟိုတယ်ကြိုတင်မှာထားမှုများသို့ မသွားမီ ၎င်း၏ဗျူဟာကို လိုက်လျောညီထွေ လုပ်ရန် လိုအပ်နိုင်သည်။

ထို့အပြင်၊ အသုံးပြုသူ feedback (ဥပမာ- လူသားတစ်ယောက်က ပိုမို စောသော လေယာဉ်ဖျင့်ကို နှစ်သက်ကြောင်း ဆုံးဖြတ်ခြင်း) သည် တစ်စိတ်တစ်ပိုင်း ပြန်လည်စီမံခြင်းကို ဖြစ်ပေါ်စေနိုင်သည်။ ဤ dynamic၊ iterative ချဉ်းကပ်မှုသည် နောက်ဆုံးအဖြေသည် လက်တွေ့ကန့်သတ်ချက်များနှင့် ပြောင်းလဲနေသော အသုံးပြုသူ နှစ်သက်မှုများနှင့် ကိုက်ညီကြောင်း သေချာစေပါသည်။

ဥပမာ နမူနာ code

```python
from autogen_core.models import UserMessage, SystemMessage, AssistantMessage
#.. အရင်က code နှင့် အတူတူ၊ အသုံးပြုသူမှတ်တမ်း၊ လက်ရှိအစီအစဉ်ကို ပေးပို့ပါ
messages = [
    SystemMessage(content="""သင်သည် အကောင်းဆုံးဖြစ်အောင် စီမံကိန်း agent တစ်ခုဖြစ်သည်
    သင့်အလုပ်မှာ အသုံးပြုသူ၏တောင်းဆိုချက်အပေါ်အခြေခံ၍ မည်သည့် agent များကို လုပ်ဆောင်ရမည်ကို ဆုံးဖြတ်ရန်ဖြစ်သည်။
    အောက်တွင် မတူညီသော လုပ်ငန်းများတွင် အထူးပြုသော ရရှိနိုင်သော agent များဖြစ်သည်:
    - FlightBooking: လေယာဉ်ဖျင့်ကြိုတင်မှာထားခြင်းနှင့် လေယာဉ်ဖျင့်အချက်အလက်များ ပေးခြင်းအတွက်
    - HotelBooking: ဟိုတယ်ကြိုတင်မှာထားခြင်းနှင့် ဟိုတယ်အချက်အလက်များ ပေးခြင်းအတွက်
    - CarRental: ကားငှားရမ်းခြင်းနှင့် ကားငှားရမ်းမှုအချက်အလက်များ ပေးခြင်းအတွက်
    - ActivitiesBooking: လှုပ်ရှားမှုများကြိုတင်မှာထားခြင်းနှင့် လှုပ်ရှားမှုအချက်အလက်များ ပေးခြင်းအတွက်
    - DestinationInfo: ခရီးစဉ်နေရာများအကြောင်း အချက်အလက်များ ပေးခြင်းအတွက်
    - DefaultAgent: ယေဘုယျတောင်းဆိုချက်များကို ကိုင်တွယ်ခြင်းအတွက်""", source="system"),
    UserMessage(content="စင်ကာပူမှ မဲလ်ဘုန်းသို့ ကလေး ၂ ယောက်ပါသော မိသားစုအတွက် ခရီးစဉ်အစီအစဉ်တစ်ခု ဖန်တီးပါ", source="user"),
    AssistantMessage(content=f"ယခင်ခရီးစဉ်အစီအစဉ် - {TravelPlan}", source="assistant")
]
# .. ပြန်လည်စီမံပြီး သက်ဆိုင်ရာ agent များထံ လုပ်ငန်းများကို ပို့ပါ
```

ပိုမို ကျယ်ပြန့်သော စီမံကိန်းပြုလုပ်ခြင်းအတွက် ရှုပ်ထွေးသော လုပ်ငန်းများကို ဖြေရှင်းရန် Magnetic One [Blogpost](https://www.microsoft.com/research/articles/magentic-one-a-generalist-multi-agent-system-for-solving-complex-tasks) ကို ကြည့်ရှုပါ။

## အတိုချုပ်

ဤဆောင်းပါးတွင် ကျွန်ုပ်တို့သည် သတ်မှတ်ထားသော ရရှိနိုင်သော agent များကို dynamic ရွေးချယ်နိုင်သော planner တစ်ခုကို မည်သို့ဖန်တီးရမည်ကို ဥပမာတစ်ခုကြည့်ရှုခဲ့ပါသည်။ Planner ၏ အထွက်သည် လုပ်ငန်းများကို ခွဲခြားပြီး ၎င်းတို့ကို လုပ်ဆောင်နိုင်အောင် agent များကို တာဝန်ပေးအပ်သည်။ Agent များသည် လုပ်ငန်းကို လုပ်ဆောင်ရန် လိုအပ်သော function/tool များကို ရရှိနိုင်ကြောင်း ယူဆပါသည်။ Agent များအပြင် reflection၊ summarizer နှင့် round robin chat ကဲ့သို့သော အခြား pattern များကိုလည်း ပိုမို စိတ်ကြိုက်ပြုလုပ်ရန် ထည့်သွင်းနိုင်ပါသည်။

## နောက်ထပ် အရင်းအမြစ်များ

* AutoGen Magentic One - ရှုပ်ထွေးသော လုပ်ငန်းများကို ဖြေရှင်းရန်အတွက် Generalist multi-agent system တစ်ခုဖြစ်ပြီး စိန်ခေါ်မှုများစွာသော agentic benchmark များတွင် အံ့သြဖွယ်ရလဒ်များ အောင်မြင်ခဲ့သည်။ ကိုးကား: [autogen-magentic-one](https://github.com/microsoft/autogen/tree/main/python/packages/autogen-magentic-one)။ ဤ implementation တွင် orchestrator သည် လုပ်ငန်းအထူးပြု အစီအစဉ်ကို ဖန်တီးပြီး ဤလုပ်ငန်းများကို ရရှိနိုင်သော agent များထံ delegate လုပ်သည်။ စီမံကိန်းပြုလုပ်ခြင်းအပြင် orchestrator သည် လုပ်ငန်း၏တိုးတက်မှုကို စောင့်ကြည့်ရန်နှင့် လိုအပ်သလို ပြန်လည်စီမံရန် ခြေရာခံစနစ်တစ်ခုကိုလည်း အသုံးပြုသည်။

## ယခင်သင်ခန်းစာ

[ယုံကြည်စိတ်ချရသော AI Agent များ တည်ဆောက်ခြင်း](../06-building-trustworthy-agents/README.md)

## နောက်သင်ခန်းစာ

[Multi-Agent ဒီဇိုင်းပုံစံ](../08-multi-agent/README.md)
