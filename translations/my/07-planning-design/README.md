<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "43069833a0412210ad5c3cc93d9c2146",
  "translation_date": "2025-09-18T15:52:18+00:00",
  "source_file": "07-planning-design/README.md",
  "language_code": "my"
}
-->
[![Planning Design Pattern](../../../translated_images/lesson-7-thumbnail.f7163ac557bea1236242cc86b178c3f1bbf5eb07b87f9cd7c256b366e32bcbb6.my.png)](https://youtu.be/kPfJ2BrBCMY?si=9pYpPXp0sSbK91Dr)

> _(အထက်ပါပုံကိုနှိပ်ပြီး ဒီသင်ခန်းစာရဲ့ ဗီဒီယိုကို ကြည့်ပါ)_

# အကြံအစီအစဉ် ဒီဇိုင်း

## မိတ်ဆက်

ဒီသင်ခန်းစာမှာ အောက်ပါအကြောင်းအရာများကို လေ့လာပါမည်-

* ရှင်းလင်းသော အထွေထွေရည်မှန်းချက်ကို သတ်မှတ်ပြီး ရှုပ်ထွေးသောအလုပ်ကို စီမံနိုင်သောအလုပ်များအဖြစ် ခွဲခြားခြင်း။
* ယုံကြည်စိတ်ချရပြီး စက်များဖတ်ရှုနိုင်သော အဖြေများအတွက် ဖွဲ့စည်းထားသော output ကို အသုံးချခြင်း။
* အကျိုးအမြတ်ရှိသော အဖြေများနှင့် မမျှော်လင့်ထားသော input များကို ကိုင်တွယ်ရန် အဖြစ်အပျက်အခြေခံနည်းလမ်းကို အသုံးပြုခြင်း။

## သင်ယူရမည့်ရည်မှန်းချက်များ

ဒီသင်ခန်းစာကို ပြီးဆုံးပြီးနောက်မှာ-

* AI agent အတွက် ရည်မှန်းချက်တစ်ခုကို သတ်မှတ်ပြီး၊ ဘာကို ရောက်ရှိရမည်ဆိုတာ ရှင်းလင်းစွာ သိရှိစေခြင်း။
* ရှုပ်ထွေးသောအလုပ်ကို စီမံနိုင်သော subtask များအဖြစ် ခွဲခြားပြီး၊ အဆင့်လိုက်စဉ်လိုက်စီစဉ်ခြင်း။
* Agent များကို သင့်တော်သော tools (ဥပမာ- ရှာဖွေမှု tools သို့မဟုတ် ဒေတာခွဲခြမ်းစိတ်ဖြာ tools) ဖြင့် ပြင်ဆင်ပေးပြီး၊ ဘယ်အချိန်မှာ ဘယ်လိုအသုံးပြုရမည်ဆိုတာ ဆုံးဖြတ်ခြင်းနှင့် မမျှော်လင့်ထားသောအခြေအနေများကို ကိုင်တွယ်ခြင်း။
* Subtask အဖြေများကို အကဲဖြတ်ပြီး၊ လုပ်ဆောင်မှုကို တိုးတက်အောင် ပြန်လည်ပြင်ဆင်ခြင်း။

## ရည်မှန်းချက်ကို သတ်မှတ်ခြင်းနှင့် အလုပ်ကို ခွဲခြားခြင်း

![ရည်မှန်းချက်များနှင့် အလုပ်များကို သတ်မှတ်ခြင်း](../../../translated_images/defining-goals-tasks.d70439e19e37c47ac76c48b209a4eb515bea5b8a5207f6b2e7b5e597f09ccf6a.my.png)

အများစုသော အမှန်တကယ်လုပ်ငန်းများသည် တစ်ဆင့်တည်းဖြင့် ဖြေရှင်းရန် အလွန်ရှုပ်ထွေးနေတတ်သည်။ AI agent တစ်ခုသည် ၎င်း၏ စီမံချက်နှင့် လုပ်ဆောင်မှုများကို လမ်းညွှန်ရန် ရှင်းလင်းသော ရည်မှန်းချက်တစ်ခုလိုအပ်သည်။ ဥပမာအားဖြင့်-

    "၃ ရက်ခရီးစဉ် itinerary တစ်ခုကို ဖန်တီးပါ။"

ရည်မှန်းချက်ကို ရှင်းလင်းစွာ ဖော်ပြနိုင်သော်လည်း၊ ၎င်းကို ထပ်မံတိုးတက်အောင် ပြင်ဆင်ရန် လိုအပ်သည်။ ရည်မှန်းချက်ကို ပိုမိုရှင်းလင်းစွာ သတ်မှတ်နိုင်လျှင်၊ agent (နှင့် လူသားပူးပေါင်းလုပ်ကိုင်သူများ) သည် flight ရွေးချယ်မှုများ၊ ဟိုတယ်အကြံပြုချက်များနှင့် လှုပ်ရှားမှုအကြံပြုချက်များပါဝင်သော itinerary တစ်ခုကို ဖန်တီးရန် ပိုမိုအာရုံစိုက်နိုင်မည်ဖြစ်သည်။

### အလုပ်ခွဲခြားခြင်း

ကြီးမားသော သို့မဟုတ် ရှုပ်ထွေးသောအလုပ်များကို သေးငယ်သော ရည်မှန်းချက်အခြေခံ subtask များအဖြစ် ခွဲခြားခြင်းဖြင့် ပိုမိုစီမံနိုင်စေသည်။
ခရီးစဉ် itinerary ဥပမာအတွက်၊ ရည်မှန်းချက်ကို အောက်ပါအတိုင်း ခွဲခြားနိုင်သည်-

* Flight Booking
* Hotel Booking
* Car Rental
* Personalization

subtask တစ်ခုစီကို အထူးပြု agent များ သို့မဟုတ် လုပ်ငန်းစဉ်များဖြင့် ကိုင်တွယ်နိုင်သည်။ Agent တစ်ခုသည် အကောင်းဆုံး flight deal များကို ရှာဖွေရာတွင် အထူးပြုနိုင်ပြီး၊ တစ်ခုသည် ဟိုတယ် booking များကို အာရုံစိုက်နိုင်သည်။ “downstream” agent သို့မဟုတ် စီမံခန့်ခွဲသူတစ်ခုသည် ၎င်းတို့၏ရလဒ်များကို စုပေါင်းပြီး အဆုံးသုံးစွဲသူအတွက် itinerary တစ်ခုအဖြစ် ဖော်ပြနိုင်သည်။

ဒီ modular နည်းလမ်းသည် တိုးတက်မှုများကို တဖြည်းဖြည်း ပြုလုပ်နိုင်စေသည်။ ဥပမာအားဖြင့်၊ Food Recommendations သို့မဟုတ် Local Activity Suggestions အတွက် အထူးပြု agent များကို ထည့်သွင်းပြီး itinerary ကို အချိန်ကြာလာသည်နှင့်အမျှ ပိုမိုပြည့်စုံအောင် ပြင်ဆင်နိုင်သည်။

### ဖွဲ့စည်းထားသော output

Large Language Models (LLMs) သည် structured output (ဥပမာ- JSON) ကို ဖန်တီးနိုင်ပြီး၊ ၎င်းသည် downstream agent များ သို့မဟုတ် ဝန်ဆောင်မှုများအတွက် ပိုမိုလွယ်ကူစွာ ဖတ်ရှုနိုင်သည်။ ၎င်းသည် multi-agent အခြေအနေတွင် အထူးအသုံးဝင်ပြီး၊ planning output ရရှိပြီးနောက် အလုပ်များကို လုပ်ဆောင်နိုင်သည်။ 

အမြန်လမ်းညွှန်အတွက် ```python
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

# Travel SubTask Model
class TravelSubTask(BaseModel):
    task_details: str
    assigned_agent: AgentEnum  # we want to assign the task to the agent

class TravelPlan(BaseModel):
    main_task: str
    subtasks: List[TravelSubTask]
    is_greeting: bool

client = AzureAIChatCompletionClient(
    model="gpt-4o-mini",
    endpoint="https://models.inference.ai.azure.com",
    # To authenticate with the model you will need to generate a personal access token (PAT) in your GitHub settings.
    # Create your PAT token by following instructions here: https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens
    credential=AzureKeyCredential(os.environ["GITHUB_TOKEN"]),
    model_info={
        "json_output": False,
        "function_calling": True,
        "vision": True,
        "family": "unknown",
    },
)

# Define the user message
messages = [
    SystemMessage(content="""You are an planner agent.
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
    - DefaultAgent: For handling general requests""", source="system"),
    UserMessage(
        content="Create a travel plan for a family of 2 kids from Singapore to Melboune", source="user"),
]

response = await client.create(messages=messages, extra_create_args={"response_format": 'json_object'})

response_content: Optional[str] = response.content if isinstance(
    response.content, str) else None
if response_content is None:
    raise ValueError("Response content is not a valid JSON string" )

pprint(json.loads(response_content))

# # Ensure the response content is a valid JSON string before loading it
# response_content: Optional[str] = response.content if isinstance(
#     response.content, str) else None
# if response_content is None:
#     raise ValueError("Response content is not a valid JSON string")

# # Print the response content after loading it as JSON
# pprint(json.loads(response_content))

# Validate the response content with the MathReasoning model
# TravelPlan.model_validate(json.loads(response_content))
``` ကို ကြည့်ပါ။

### Multi-Agent Orchestration ဖြင့် Planning Agent

ဒီဥပမာမှာ Semantic Router Agent တစ်ခုသည် အသုံးပြုသူ၏တောင်းဆိုမှု (ဥပမာ- "ကျွန်တော့်ခရီးစဉ်အတွက် ဟိုတယ်အစီအစဉ်လိုအပ်ပါတယ်။") ကို လက်ခံသည်။

planner သည်-

* Hotel Plan ကို လက်ခံခြင်း- planner သည် အသုံးပြုသူ၏ message ကို လက်ခံပြီး၊ system prompt (ရရှိနိုင်သော agent အချက်အလက်များပါဝင်သည်) အပေါ်အခြေခံ၍ structured travel plan တစ်ခုကို ဖန်တီးသည်။
* Agent များနှင့် ၎င်းတို့၏ Tools ကို စာရင်းပြုစုခြင်း- agent registry သည် agent များ (ဥပမာ- flight, hotel, car rental, activities) နှင့် ၎င်းတို့၏ လုပ်ဆောင်နိုင်သော function များ/tools များကို စာရင်းပြုစုထားသည်။
* Plan ကို သက်ဆိုင်ရာ Agent များထံ ပို့ခြင်း- subtask များအရေအတွက်ပေါ်မူတည်၍၊ planner သည် message ကို တစ်ခုတည်းသော task အခြေအနေများအတွက် အထူးပြု agent ထံတိုက်ရိုက်ပို့ခြင်း သို့မဟုတ် multi-agent ပူးပေါင်းဆောင်ရွက်မှုအတွက် group chat manager မှတစ်ဆင့် စီမံခန့်ခွဲခြင်း။
* ရလဒ်ကို အကျဉ်းချုပ်ခြင်း- planner သည် ဖန်တီးထားသော plan ကို ရှင်းလင်းစွာ အကျဉ်းချုပ်ပေးသည်။

အောက်ပါ Python code sample သည် ဒီအဆင့်များကို ဖော်ပြသည်-

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

# Travel SubTask Model

class TravelSubTask(BaseModel):
    task_details: str
    assigned_agent: AgentEnum # we want to assign the task to the agent

class TravelPlan(BaseModel):
    main_task: str
    subtasks: List[TravelSubTask]
    is_greeting: bool
import json
import os
from typing import Optional

from autogen_core.models import UserMessage, SystemMessage, AssistantMessage
from autogen_ext.models.openai import AzureOpenAIChatCompletionClient

# Create the client with type-checked environment variables

client = AzureOpenAIChatCompletionClient(
    azure_deployment=os.getenv("AZURE_OPENAI_DEPLOYMENT_NAME"),
    model=os.getenv("AZURE_OPENAI_DEPLOYMENT_NAME"),
    api_version=os.getenv("AZURE_OPENAI_API_VERSION"),
    azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"),
    api_key=os.getenv("AZURE_OPENAI_API_KEY"),
)

from pprint import pprint

# Define the user message

messages = [
    SystemMessage(content="""You are an planner agent.
    Your job is to decide which agents to run based on the user's request.
    Below are the available agents specialized in different tasks:
    - FlightBooking: For booking flights and providing flight information
    - HotelBooking: For booking hotels and providing hotel information
    - CarRental: For booking cars and providing car rental information
    - ActivitiesBooking: For booking activities and providing activity information
    - DestinationInfo: For providing information about destinations
    - DefaultAgent: For handling general requests""", source="system"),
    UserMessage(content="Create a travel plan for a family of 2 kids from Singapore to Melbourne", source="user"),
]

response = await client.create(messages=messages, extra_create_args={"response_format": TravelPlan})

# Ensure the response content is a valid JSON string before loading it

response_content: Optional[str] = response.content if isinstance(response.content, str) else None
if response_content is None:
    raise ValueError("Response content is not a valid JSON string")

# Print the response content after loading it as JSON

pprint(json.loads(response_content))
```

အထက်ပါ code ရဲ့ output ကို ```json
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
``` မှာ ကြည့်နိုင်ပြီး၊ structured output ကို `assigned_agent` ထံ ပို့ပြီး travel plan ကို အဆုံးသုံးစွဲသူအတွက် အကျဉ်းချုပ်ပေးနိုင်သည်။

ဥပမာ notebook ကို [ဒီမှာ](07-autogen.ipynb) ရရှိနိုင်ပါသည်။

### Iterative Planning

အချို့သောအလုပ်များသည် အပြန်အလှန် သို့မဟုတ် ပြန်လည်စီမံခြင်းကို လိုအပ်ပြီး၊ subtask တစ်ခုရဲ့ရလဒ်သည် နောက်တစ်ခုကို သက်ရောက်စေသည်။ ဥပမာအားဖြင့်၊ agent သည် flight booking လုပ်စဉ်တွင် မမျှော်လင့်ထားသော data format ကို ရှာဖွေတွေ့ရှိပါက၊ ဟိုတယ် booking မလုပ်မီ ၎င်း၏နည်းလမ်းကို ပြောင်းလဲရန် လိုအပ်နိုင်သည်။

ထို့အပြင်၊ အသုံးပြုသူ feedback (ဥပမာ- လူသားတစ်ဦးသည် အစောဆုံး flight ကို သဘောကျသည်ဟု ဆုံးဖြတ်ခြင်း) သည် အစိတ်အပိုင်းပြန်လည်စီမံခြင်းကို ဖြစ်စေနိုင်သည်။ ဒီ dynamic, iterative နည်းလမ်းသည် အဆုံးသတ်ဖြေရှင်းချက်သည် အမှန်တကယ်အခြေအနေများနှင့် အသုံးပြုသူ၏ အဆင့်မြှင့်လိုအပ်ချက်များနှင့် ကိုက်ညီစေသည်။

ဥပမာ code-

```python
from autogen_core.models import UserMessage, SystemMessage, AssistantMessage
#.. same as previous code and pass on the user history, current plan
messages = [
    SystemMessage(content="""You are a planner agent to optimize the
    Your job is to decide which agents to run based on the user's request.
    Below are the available agents specialized in different tasks:
    - FlightBooking: For booking flights and providing flight information
    - HotelBooking: For booking hotels and providing hotel information
    - CarRental: For booking cars and providing car rental information
    - ActivitiesBooking: For booking activities and providing activity information
    - DestinationInfo: For providing information about destinations
    - DefaultAgent: For handling general requests""", source="system"),
    UserMessage(content="Create a travel plan for a family of 2 kids from Singapore to Melbourne", source="user"),
    AssistantMessage(content=f"Previous travel plan - {TravelPlan}", source="assistant")
]
# .. re-plan and send the tasks to respective agents
```

ရှုပ်ထွေးသောအလုပ်များကို စီမံရန် ပိုမိုကျယ်ကျယ်ပြန့်ပြန့်သော planning ကို Magnetic One မှာ ကြည့်ပါ။

## အကျဉ်းချုပ်

ဒီဆောင်းပါးမှာ ရရှိနိုင်သော agent များကို သတ်မှတ်ပြီး၊ အလုပ်များကို ခွဲခြားပြီး agent များထံ ပေးအပ်နိုင်သော planner တစ်ခုကို ဖန်တီးနည်းကို ကြည့်ရှုခဲ့ပါသည်။ Planner ရဲ့ output သည် အလုပ်များကို ခွဲခြားပြီး agent များကို ပေးအပ်နိုင်သည်။ Agent များသည် လိုအပ်သော function/tools များကို အသုံးပြုနိုင်သည်ဟု ယူဆထားသည်။ Agent များအပြင် reflection, summarizer, နှင့် round robin chat ကဲ့သို့သော pattern များကို ထည့်သွင်းပြီး ပိုမိုစိတ်ကြိုက်ပြုလုပ်နိုင်သည်။

## ထပ်မံလေ့လာရန် အရင်းအမြစ်များ

AutoGen Magnetic One - ရှုပ်ထွေးသောအလုပ်များကို ဖြေရှင်းရန် Generalist multi-agent system တစ်ခုဖြစ်ပြီး၊ agentic benchmark များစွာတွင် ထူးချွန်သောရလဒ်များရရှိထားသည်။ Reference:

ဒီ implementation မှာ orchestrator သည် task-specific plan ကို ဖန်တီးပြီး၊ အလုပ်များကို ရရှိနိုင်သော agent များထံ ပေးအပ်သည်။ Planning အပြင် orchestrator သည် အလုပ်ရဲ့ တိုးတက်မှုကို စောင့်ကြည့်ပြီး လိုအပ်သလို ပြန်လည်စီမံခြင်းကို လုပ်ဆောင်သည်။

### Planning Design Pattern အကြောင်း မေးခွန်းများရှိပါသလား?

[Azure AI Foundry Discord](https://aka.ms/ai-agents/discord) ကို Join လုပ်ပြီး အခြားသော သင်ယူသူများနှင့် တွေ့ဆုံပါ၊ office hours တွင် ပါဝင်ပြီး AI Agents အကြောင်း မေးခွန်းများကို ဖြေရှင်းပါ။

## ယခင်သင်ခန်းစာ

[ယုံကြည်စိတ်ချရသော AI Agents ဖန်တီးခြင်း](../06-building-trustworthy-agents/README.md)

## နောက်သင်ခန်းစာ

[Multi-Agent Design Pattern](../08-multi-agent/README.md)

---

**အကြောင်းကြားချက်**:  
ဤစာရွက်စာတမ်းကို AI ဘာသာပြန်ဝန်ဆောင်မှု [Co-op Translator](https://github.com/Azure/co-op-translator) ကို အသုံးပြု၍ ဘာသာပြန်ထားပါသည်။ ကျွန်ုပ်တို့သည် တိကျမှုအတွက် ကြိုးစားနေသော်လည်း၊ အလိုအလျောက် ဘာသာပြန်မှုများတွင် အမှားများ သို့မဟုတ် မတိကျမှုများ ပါဝင်နိုင်သည်ကို သတိပြုပါ။ မူရင်းစာရွက်စာတမ်းကို ၎င်း၏ မူရင်းဘာသာစကားဖြင့် အာဏာတရားရှိသော အရင်းအမြစ်အဖြစ် သတ်မှတ်သင့်ပါသည်။ အရေးကြီးသော အချက်အလက်များအတွက် လူက ဘာသာပြန်မှုကို အသုံးပြုရန် အကြံပြုပါသည်။ ဤဘာသာပြန်မှုကို အသုံးပြုခြင်းမှ ဖြစ်ပေါ်လာသော အလွဲအလွဲအချော်များ သို့မဟုတ် အနားလွဲမှုများအတွက် ကျွန်ုပ်တို့သည် တာဝန်မယူပါ။