[![Planning Design Pattern](../../../translated_images/pa/lesson-7-thumbnail.f7163ac557bea123.webp)](https://youtu.be/kPfJ2BrBCMY?si=9pYpPXp0sSbK91Dr)

> _(ਇਸ ਪਾਠ ਦੀ ਵੀਡੀਓ ਵੇਖਣ ਲਈ ਉੱਪਰ ਦੀ ਚਿੱਤਰ 'ਤੇ ਕਲਿੱਕ ਕਰੋ)_

# ਯੋਜਨਾ ਬਣਾਉਣ ਦਾ ਡਿਜ਼ਾਈਨ

## ਪਰਿਚਯ

ਇਹ ਪਾਠ ਕਵਰ ਕਰੇਗਾ

* ਇੱਕ ਸਪੱਸ਼ਟ ਕੁੱਲ ਲਕੜੀ ਨਿਰਧਾਰਿਤ ਕਰਨਾ ਅਤੇ ਇੱਕ ਜਟਿਲ ਕਾਰਜ ਨੂੰ ਪ੍ਰਬੰਧਨਯੋਗ ਕਾਰਜਾਂ ਵਿੱਚ ਵੰਡਣਾ।
* ਵਿਵਸਥਿਤ ਆਉਟਪੁੱਟ ਦਾ ਲਾਭ ਉਠਾਉਣਾ ਤਾਂ ਜੋ ਜ਼ਿਆਦਾ ਭਰੋਸੇਯੋਗ ਅਤੇ ਮਸ਼ੀਨ-ਪਠਨਯੋਗ ਪ੍ਰਤੀਕਿਰਿਆਵਾਂ ਮਿਲ ਸਕਣ।
* ਗਤੀਸ਼ੀਲ ਕਾਰਜਾਂ ਅਤੇ ਅਣਪਛਾਤੇ ਇਨਪੁੱਟਾਂ ਨੂੰ ਸੰਭਾਲਣ ਲਈ ਇਕ ਘਟਨਾ-ਚਾਲਿਤ ਪਹੁੰਚ ਲਾਗੂ ਕਰਨਾ।

## ਸਿੱਖਣ ਦੇ ਲਕੜੀ

ਇਸ ਪਾਠ ਨੂੰ ਪੂਰਾ ਕਰਨ ਤੋਂ ਬਾਅਦ, ਤੁਹਾਨੂੰ ਇਹ ਸਮਝ ਆ ਜਾਵੇਗੀ:

* ਇੱਕ AI ਏਜੰਟ ਲਈ ਕੁੱਲ ਮਕਸਦ ਦੀ ਪਛਾਣ ਕਰੋ ਅਤੇ ਇਹ ਸੈੱਟ ਕਰੋ ਕਿ ਇਹ ਸਪੱਸ਼ਟ ਤੌਰ 'ਤੇ ਜਾਣਦਾ ਹੈ ਕਿ ਕੀ ਪ੍ਰਾਪਤ ਕਰਨਾ ਹੈ।
* ਇੱਕ ਜਟਿਲ ਕਾਰਜ ਨੂੰ ਪ੍ਰਬੰਧਨਯੋਗ ਉਪ-ਕਾਰਜਾਂ ਵਿੱਚ ਵੰਡੋ ਅਤੇ ਉਨ੍ਹਾਂ ਨੂੰ ਤਰਕਸੰਗਤ ਕ੍ਰਮ ਵਿੱਚ ਵਿਵਸਥਿਤ ਕਰੋ।
* ਏਜੰਟ ਨੂੰ ਸਹੀ ਸੰਦਾਂ (ਜਿਵੇਂ ਖੋਜ ਸੰਦ ਜਾਂ ਡਾਟਾ ਵਿਸ਼ਲੇਸ਼ਣ ਸੰਦ) ਨਾਲ ਸਜਾਓ, ਇਹ ਫੈਸਲਾ ਕਰੋ ਕਿ ਕਦੋਂ ਅਤੇ ਕਿਵੇਂ ਇਹਨਾਂ ਦੀ ਵਰਤੋਂ ਕਰਨੀ ਹੈ, ਅਤੇ ਉੱਥੇ ਉੱਠਣ ਵਾਲੀਆਂ ਅਣਪਛਾਤੀਆਂ ਸਥਿਤੀਆਂ ਨੂੰ ਸੰਭਾਲੋ।
* ਉਪ-ਕਾਰਜਾਂ ਦੇ ਨਤੀਜਿਆਂ ਦਾ ਮੁਲਾਂਕਣ ਕਰੋ, ਪ੍ਰਦਰਸ਼ਨ ਮਾਪੋ, ਅਤੇ ਆਖ਼ਰੀ ਆਉਟਪੁੱਟ ਨੂੰ ਸੁਧਾਰਨ ਲਈ ਕਰਵਾਈ ਵਿਚ ਸੁਧਾਰ ਕਰੋ।

## ਕੁੱਲ ਮਕਸਦ ਨਿਰਧਾਰਿਤ ਕਰਨਾ ਅਤੇ ਕਾਰਜ ਵੰਡਣਾ

![Defining Goals and Tasks](../../../translated_images/pa/defining-goals-tasks.d70439e19e37c47a.webp)

ਜ਼ਿਆਦਾਤਰ ਅਸਲੀ ਦੁਨੀਆ ਦੇ ਕਾਰਜ ਇੱਕ ਕਦਮ ਵਿੱਚ ਕਰਨ ਲਈ ਬਹੁਤ ਜਟਿਲ ਹੁੰਦੇ ਹਨ। ਇਕ AI ਏਜੰਟ ਨੂੰ ਆਪਣੀ ਯੋਜਨਾ ਅਤੇ ਕਾਰਵਾਈ ਲਈ ਇੱਕ ਸੰਖੇਪ ਉਦੇਸ਼ ਦੀ ਲੋੜ ਹੁੰਦੀ ਹੈ। ਉਦਾਹਰਨ ਵਜੋਂ, ਇੱਥੇ ਲਕੜੀ ਹੈ:

    "3-ਦਿਨ ਦਾ ਯਾਤਰਾ ਯੋਜਨਾ ਤਿਆਰ ਕਰੋ।"

ਜੇਕਰچہ ਇਹ ਸਧਾਰਣ ਹੈ, ਇਹ ਨੂੰ ਫਿਰ ਵੀ ਸੁਧਾਰ ਦੇਣ ਦੀ ਲੋੜ ਹੈ। ਜਿੰਨਾ ਜ਼ਿਆਦਾ ਸਪੱਠ ਲਕੜੀ ਹੋਵੇਗਾ, ਏਜੰਟ (ਅਤੇ ਕੋਈ ਵੀ ਮਨੁੱਖੀ ਸਹਿਯੋਗੀ) ਬੇਹਤਰ ਤਰੀਕੇ ਨਾਲ ਸਹੀ ਨਤੀਜਾ ਪ੍ਰਾਪਤ ਕਰਨ 'ਤੇ ਧਿਆਨ ਕੇਂਦ੍ਰਿਤ ਕਰ ਸਕਦੇ ਹਨ, ਜਿਵੇਂ ਕਿ ਫਲਾਈਟ ਵਿਕਲਪ, ਹੋਟਲ ਸਿਫਾਰਸ਼ਾਂ, ਅਤੇ ਕਿਰਿਆਸ਼ੀਲ ਸੁਝਾਵਾਂ ਦੇ ਨਾਲ ਇੱਕ ਵਿਸਥਾਰਪੂਰਕ ਯਾਤਰਾ ਦਸਤਾਵੇਜ਼ ਬਣਾਉਣਾ।

### ਕਾਰਜ ਵੰਡ

ਵੱਡੇ ਜਾਂ ਜਟਿਲ ਕਾਰਜ ਛੋਟੇ, ਲਕੜੀ-ਕੇਂਦਰਿਤ ਉਪ-ਕਾਰਜਾਂ ਵਿੱਚ ਵੰਡੇ ਜਾਣ 'ਤੇ ਜ਼ਿਆਦਾ ਮੈਨਠੇ ਜਾਂਦੇ ਹਨ।  
ਯਾਤਰਾ ਯੋਜਨਾ ਦੇ ਉਦਾਹਰਨ ਲਈ, ਤੁਸੀਂ ਲਕੜੀ ਨੂੰ ਵੰਡ ਸਕਦੇ ਹੋ:

* ਫਲਾਈਟ ਬੁਕਿੰਗ  
* ਹੋਟਲ ਬੁਕਿੰਗ  
* ਕਾਰ ਕਿਰਾਏ 'ਤੇ ਲੈਣਾ  
* ਨਿੱਜੀਕਰਨ

ਹਰ ਉਪ-ਕਾਰਜ ਨੂੰ ਸਮਰਪਿਤ ਏਜੰਟਾਂ ਜਾਂ ਪ੍ਰਕਿਰਿਆਵਾਂ ਵੱਲੋਂ ਸਾਂਭਿਆ ਜਾ ਸਕਦਾ ਹੈ। ਇੱਕ ਏਜੰਟ ਸਭ ਤੋਂ ਵਧੀਆ ਫਲਾਈਟ ਦਾਮ ਖੋਜਣ ਵਿੱਚ ਮੁਹਾਰਤ ਰੱਖ ਸਕਦਾ ਹੈ, ਦੂਜਾ ਹੋਟਲ ਬੁਕਿੰਗ 'ਤੇ ਧਿਆਨ ਕੇਂਦ੍ਰਿਤ ਕਰਦਾ ਹੈ, ਆਦਿ। ਇੱਕ ਕੋਆਰਡੀਨੇਟਿੰਗ ਜਾਂ "ਡਾਊਨਸਟਰਿਮ" ਏਜੰਟ ਫਿਰ ਇਹ ਨਤੀਜੇ ਇੱਕ ਮਨਮੁਹਾਂਦੇ ਯਾਤਰਾ ਦਸਤਾਵੇਜ਼ ਵਿੱਚ ਇਕੱਠੇ ਕਰ ਸਕਦਾ ਹੈ ਜਿਹੜਾ ਅੰਤ ਮੂਲ ਉਪਭੋਗਤਾ ਲਈ ਹੁੰਦਾ ਹੈ।  

ਇਹ ਮਾਡਿਊਲਰ ਪਹੁੰਚ ਵੀ ਵਾਧੂ ਸੁਧਾਰਾਂ ਦੀ ਆਗਿਆ ਦਿੰਦੀ ਹੈ। ਉਦਾਹਰਨ ਲਈ, ਤੁਸੀਂ ਖ਼ਾਣ-ਪੀਣ ਦੀਆਂ ਸਿਫ਼ਾਰਸ਼ਾਂ ਜਾਂ ਸਥਾਨਕ ਗਤੀਵਿਧੀਆਂ ਦੀਆਂ ਸੁਝਾਵਾਂ ਲਈ ਵਿਸ਼ੇਸ਼ ਏਜੰਟ ਜੋੜ ਸਕਦੇ ਹੋ ਅਤੇ ਸਮੇਂ-ਸਮੇਂ 'ਤੇ ਯਾਤਰਾ ਦਸਤਾਵੇਜ਼ ਨੂੰ ਸੁਧਾਰ ਸਕਦੇ ਹੋ।

### ਵਿਵਸਥਿਤ ਆਉਟਪੁੱਟ

ਵੱਡੇ ਭਾਸ਼ਾ ਮਾਡਲ (LLMs) ਵਿਵਸਥਿਤ ਆਉਟਪੁੱਟ (ਜਿਵੇਂ JSON) ਤਿਆਰ ਕਰ ਸਕਦੇ ਹਨ ਜੋ ਡਾਊਨਸਟਰਿਮ ਏਜੰਟ ਜਾਂ ਸੇਵਾਵਾਂ ਲਈ ਅਸਾਨੀ ਨਾਲ ਪਾਰਸ ਅਤੇ ਪ੍ਰਕਿਰਿਆਗਤ ਹੋ ਜਾਂਦਾ ਹੈ। ਇਹ ਖ਼ਾਸ ਤੌਰ 'ਤੇ ਬਹੁ-ਏਜੰਟ ਸੰਦਰਭ ਵਿੱਚ ਲਾਭਕਾਰੀ ਹੈ, ਜਿੱਥੇ ਅਸੀਂ ਇਹ ਕਾਰਜ ਯੋਜਨਾ ਬਣਾਉਣ ਦੇ ਆਉਟਪੁੱਟ ਮਿਲਣ ਤੋਂ ਬਾਅਦ ਕਰ ਸਕਦੇ ਹਾਂ।  

ਹੇਠਾਂ ਦਿੱਤਾ ਪਾਇਥਨ ਸਨਿੱਪੇਟ ਇੱਕ ਸਧਾਰਣ ਯੋਜਨਾ ਬਣਾਉਣ ਵਾਲੇ ਏਜੰਟ ਨੂੰ ਕਿਵੇਂ ਇੱਕ ਲਕੜੀ ਨੂੰ ਉਪ-ਕਾਰਜਾਂ ਵਿੱਚ ਵੰਡਦਾ ਹੈ ਅਤੇ ਇੱਕ ਵਿਵਸਥਿਤ ਯੋਜਨਾ ਤਿਆਰ ਕਰਦਾ ਹੈ ਦਿਖਾਉਂਦਾ ਹੈ:

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

# ਯਾਤਰਾ ਸਬਟਾਸਕ ਮਾਡਲ
class TravelSubTask(BaseModel):
    task_details: str
    assigned_agent: AgentEnum  # ਅਸੀਂ ਕਾਰਜ ਏਜੰਟ ਨੂੰ ਸੌਂਪਣਾ ਚਾਹੁੰਦੇ ਹਾਂ

class TravelPlan(BaseModel):
    main_task: str
    subtasks: List[TravelSubTask]
    is_greeting: bool

provider = AzureAIProjectAgentProvider(credential=AzureCliCredential())

# ਯੂਜ਼ਰ ਸੁਨੇਹਾ ਪਰਿਭਾਸ਼ਿਤ ਕਰੋ
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
  
### ਬਹੁ-ਏਜੰਟ ਸਮਨ્વਣ ਵਾਲਾ ਯੋਜਨਾ ਬਣਾਉਣ ਵਾਲਾ ਏਜੰਟ  

ਇਸ ਉਦਾਹਰਨ ਵਿੱਚ, ਇੱਕ ਸੈਮਾਂਟਿਕ ਰਾਊਟਰ ਏਜੰਟ ਇੱਕ ਉਪਭੋਗਤਾ ਦੀ ਬੇਨਤੀ ਪ੍ਰਾਪਤ ਕਰਦਾ ਹੈ (ਜਿਵੇਂ "ਮੈਨੂੰ ਆਪਣੀ ਯਾਤਰਾ ਲਈ ਹੋਟਲ ਯੋਜਨਾ ਦੀ ਲੋੜ ਹੈ।")।

ਫਿਰ ਯੋਜਨਾਕਾਰ:

* ਹੋਟਲ ਯੋਜਨਾ ਪ੍ਰਾਪਤ ਕਰਦਾ ਹੈ: ਯੋਜਨਾਕਾਰ ਉਪਭੋਗਤਾ ਦਾ ਸੁਨੇਹਾ ਲੈਂਦਾ ਹੈ ਅਤੇ ਸਿਸਟਮ ਪ੍ਰਾਂਪਟ (ਉਪਲੱਬਧ ਏਜੰਟ ਵੇਰਿਆਂ ਸਮੇਤ) ਦੇ ਆਧਾਰ 'ਤੇ ਇੱਕ ਵਿਵਸਥਿਤ ਯਾਤਰਾ ਯੋਜਨਾ ਤਿਆਰ ਕਰਦਾ ਹੈ।  
* ਏਜੰਟ ਅਤੇ ਉਨ੍ਹਾਂ ਦੇ ਸੰਦਾਂ ਦੀ ਸੂਚੀ ਬਣਾਉਂਦਾ ਹੈ: ਏਜੰਟ ਰਜਿਸਟਰੀ ਵਿੱਚ ਏਜੰਟਾਂ ਦੀ ਸੂਚੀ ਹੁੰਦੀ ਹੈ (ਉਦਾਹਰਣ ਵਜੋਂ ਫਲਾਈਟ, ਹੋਟਲ, ਕਾਰ ਕਿਰਾਏ, ਅਤੇ ਗਤੀਵਿਧੀ ਲਈ) ਅਤੇ ਉਹਨਾਂ ਵੱਲੋਂ ਪੇਸ਼ ਕੀਤੇ ਫੰਕਸ਼ਨ ਜਾਂ ਸੰਦ।  
* ਯੋਜਨਾ ਨੂੰ ਸੰਬੰਧਤ ਏਜੰਟਾਂ ਤੱਕ ਭੇਜਦਾ ਹੈ: ਉਪ-ਕਾਰਜਾਂ ਦੀ ਗਿਣਤੀ ਦੇ ਮੱਦੇਨਜ਼ਰ ਯੋਜਨਾਕਾਰ ਸੁਨੇਹਾ ਸੀਧਾ ਕਿਸੇ ਸਮਰਪਿਤ ਏਜੰਟ ਨੂੰ ਭੇਜਦਾ ਹੈ (ਇੱਕ ਕਾਰਜ ਵਾਲੀਆਂ ਸਥਿਤੀਆਂ ਲਈ) ਜਾਂ ਬਹੁ-ਏਜੰਟ ਸਹਿਯੋਗ ਲਈ ਗਰੁੱਪ ਚੈਟ ਮੈਨੇਜਰ ਰਾਹੀਂ ਕੋਆਰਡੀਨੇਟ ਕਰਦਾ ਹੈ।  
* ਨਤੀਜਾ ਸੰਖੇਪ ਕਰਦਾ ਹੈ: ਆਖ਼ਰਕਾਰ, ਯੋਜਨਾਕਾਰ ਸਪਸ਼ਟਤਾ ਲਈ ਤਿਆਰ ਕੀਤੀ ਯੋਜਨਾ ਦਾ ਸੰਖੇਪ ਕਰਦਾ ਹੈ।  
ਹੇਠਾਂ ਦਿੱਤਾ ਪਾਇਥਨ ਕੋਡ ਨਮੂਨਾ ਇਹ ਕਦਮ ਦਰਸਾਉਂਦਾ ਹੈ:  

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

# ਯਾਤਰਾ ਸਬਟਾਸਕ ਮਾਡਲ

class TravelSubTask(BaseModel):
    task_details: str
    assigned_agent: AgentEnum # ਅਸੀਂ ਟਾਸਕ ਨੂੰ ਏਜੰਟ ਨੂੰ ਸੌਂਪਣਾ ਚਾਹੁੰਦੇ ਹਾਂ

class TravelPlan(BaseModel):
    main_task: str
    subtasks: List[TravelSubTask]
    is_greeting: bool
import json
import os
from typing import Optional

from agent_framework.azure import AzureAIProjectAgentProvider
from azure.identity import AzureCliCredential

# ਕਲਾਇੰਟ ਬਣਾਓ

provider = AzureAIProjectAgentProvider(credential=AzureCliCredential())

from pprint import pprint

# ਯੂਜ਼ਰ ਮੈਸਜ ਨੂੰ ਪਰਿਭਾਸ਼ਿਤ ਕਰੋ

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

# ਇਸਨੂੰ JSON ਵਜੋਂ ਲੋਡ ਕਰਨ ਤੋਂ ਬਾਅਦ ਜਵਾਬ ਸਮੱਗਰੀ ਪ੍ਰਿੰਟ ਕਰੋ

pprint(json.loads(response_content))
```
  
ਹੇਠਾਂ ਦਿੱਤਾ ਗਿਆ ਕੋਡ ਔਟਪੁੱਟ ਪਿਛਲੇ ਕੋਡ ਦੇ ਨਤੀਜੇ ਨੂੰ ਦਰਸਾਉਂਦਾ ਹੈ ਅਤੇ ਤੁਸੀਂ ਇਸ ਵਿਵਸਥਿਤ ਆਉਟਪੁੱਟ ਨੂੰ `assigned_agent` ਵੱਲ ਭੇਜਣ ਅਤੇ ਯਾਤਰਾ ਯੋਜਨਾ ਨੂੰ ਅੰਤਮ ਉਪਭੋਗਤਾ ਲਈ ਸੰਖੇਪ ਕਰਨ ਲਈ ਵਰਤ ਸਕਦੇ ਹੋ।

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
  
ਪਿਛਲੇ ਕੋਡ ਨਮੂਨੇ ਵਾਲਾ ਇੱਕ ਉਦਾਹਰਨ ਨੋਟਬੁੱਕ [ਇਥੇ](07-python-agent-framework.ipynb) ਉਪਲਬਧ ਹੈ।

### ਦੁਹਰਾਉਂਦੀ ਯੋਜਨਾ ਬਣਾਉਣਾ

ਕੁਝ ਕਾਰਜਾਂ ਲਈ ਅੱਗੇ-ਪਿੱਛੇ ਜਾਂ ਦੁਬਾਰਾ ਯੋਜਨਾਬੰਦੀ ਦੀ ਲੋੜ ਹੁੰਦੀ ਹੈ, ਜਿੱਥੇ ਇੱਕ ਉਪ-ਕਾਰਜ ਦਾ ਨਤੀਜਾ ਅਗਲੇ ਉਪ-ਕਾਰਜ 'ਤੇ ਪ੍ਰਭਾਵ ਪਾਂਦਾ ਹੈ। ਉਦਾਹਰਨ ਵਜੋਂ, ਜੇਕਰ ਏਜੰਟ ਫਲਾਈਟ ਬੁਕਿੰਗ ਦੌਰਾਨ ਅਣਪਛਾਤੇ ਡਾਟਾ ਫਾਰਮੈਟ ਦਾ ਪਤਾ ਲਗਾਉਂਦਾ ਹੈ, ਤਾਂ ਇਸ ਨੂੰ ਹੋਟਲ ਬੁਕਿੰਗ ਦੀ ਯੋਜਨਾ ਸ਼ੁਰੂ ਕਰਨ ਤੋਂ ਪਹਿਲਾਂ ਆਪਣੀ ਯੋਜਨਾਬੰਦੀ ਨੂੰ ਢਾਲਣਾ ਪੈ ਸਕਦਾ ਹੈ।  

ਇਸ ਤੋਂ ਇਲਾਵਾ, ਉਪਭੋਗਤਾ ਦੀ ਰਾਏ (ਜਿਵੇਂ ਕੋਈ ਮਨੁੱਖ ਪਹਿਲੀ ਫਲਾਈਟ ਨੂੰ ਤਰਜੀਹ ਦੇਵੇ) ਇੱਕ ਹਿੱਸੇਵਾਰੀ ਦੁਬਾਰਾ ਯੋਜਨਾ ਨੂੰ ਚਾਲੂ ਕਰ ਸਕਦੀ ਹੈ। ਇਹ ਤਰਤੀਬ ਵਾਲੀ, ਦੁਹਰਾਉਣ ਵਾਲੀ ਪਹੁੰਚ ਇਹ ਯਕੀਨੀ ਬਣਾਉਂਦੀ ਹੈ ਕਿ ਆਖਰੀ ਹੱਲ ਅਸਲੀ ਦੁਨੀਆ ਦੀਆਂ ਪਾਬੰਦੀਆਂ ਅਤੇ ਬਦਲਦੀਆਂ ਉਪਭੋਗਤਾ ਪਸੰਦਾਂ ਨਾਲ ਮੇਲ ਖਾਂਦਾ ਹੈ।  

ਉਦਾਹਰਨ ਕੋਡ

```python
from agent_framework.azure import AzureAIProjectAgentProvider
from azure.identity import AzureCliCredential
#.. ਪਿਛਲੇ ਕੋਡ ਵਾਂਗ ਹੀ ਅਤੇ ਯੂਜ਼ਰ ਇਤਿਹਾਸ, ਮੌਜੂਦਾ ਯੋਜਨਾ ਨੂੰ ਅੱਗੇ ਵਧਾਓ

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
# .. ਮੁੜ ਯੋਜਨਾ ਬਣਾਓ ਅਤੇ ਕੰਮਾਂ ਨੂੰ ਸੰਬੰਧਿਤ ਏਜੰਟਾਂ ਨੂੰ ਭੇਜੋ
```
  
ਜਿਆਦਾ ਵਿਸਥਾਰਪੂਰਕ ਯੋਜਨਾ ਬਣਾਉਣ ਲਈ ਮੈਗਨੇਟਿਕ ਵਨ ਦੇ <a href="https://www.microsoft.com/research/articles/magentic-one-a-generalist-multi-agent-system-for-solving-complex-tasks" target="_blank">ਬਲੌਗਪੋਸਟ</a> ਨੂੰ ਦੇਖੋ ਜੋ ਕਿ ਜਟਿਲ ਕਾਰਜਾਂ ਹੱਲ ਕਰਨ ਲਈ ਹੈ।

## ਸੰਖੇਪ

ਇਸ ਲੇਖ ਵਿੱਚ ਅਸੀਂ ਦੇਖਿਆ ਕਿ ਕਿਵੇਂ ਇੱਕ ਯੋਜਨਾਕਾਰ ਬਣਾਇਆ ਜਾ ਸਕਦਾ ਹੈ ਜੋ ਉਪਲਬਧ ਏਜੰਟਾਂ ਦੀ ਡਾਇਨਾਮਿਕ ਚੋਣ ਕਰਦਾ ਹੈ। ਯੋਜਨਾਕਾਰ ਦਾ ਆਉਟਪੁੱਟ ਕਾਰਜਾਂ ਨੂੰ ਵੰਡਦਾ ਹੈ ਅਤੇ ਉਹਨਾਂ ਨੂੰ ਐਜੰਟਾਂ ਨੂੰ ਸੌਂਪਦਾ ਹੈ ਤਾਂ ਜੋ ਉਹ ਲਾਗੂ ਹੋ ਸਕਣ। ਇਹ ਮੰਨਿਆ ਜਾਂਦਾ ਹੈ ਕਿ ਏਜੰਟਾਂ ਕੋਲ ਉਹ ਫੰਕਸ਼ਨ/ਸੰਦ ਹਨ ਜੋ ਕਾਰਜ ਕਰਨ ਲਈ ਜਰੂਰੀ ਹਨ। ਏਜੰਟਾਂ ਦੇ ਇਲਾਵਾ ਤੁਸੀਂ ਹੋਰ ਪੈਟਰਨਾਂ ਜਿਵੇਂ ਰਿਫਲੈਕਸ਼ਨ, ਸੰਖੇਪਕ, ਅਤੇ ਰਾਊਂਡ ਰੋਬਿਨ ਚੈਟ ਵੱਧ ਸਕਦੇ ਹੋ ਤਾਂ ਜੋ ਹੋਰ ਵਿਅਕਤੀਗਤਕਰਨ ਕੀਤਾ ਜਾ ਸਕੇ।

## ਵਾਧੂ ਸਰੋਤ

Magentic One - ਜਟਿਲ ਕਾਰਜਾਂ ਹੱਲ ਕਰਨ ਲਈ ਇੱਕ ਜਨਰਲਿਸਟ ਬਹੁ-ਏਜੰਟ ਸਿਸਟਮ ਹੈ ਅਤੇ ਇਹ ਬਹੁਤ ਸਾਰੇ ਚੁਣੌਤੀਪੂਰਕ ਏਜੰਟਿਕ ਮਾਪਦੰਡਾਂ ‘ਤੇ ਸ਼ਾਨਦਾਰ ਨਤੀਜੇ ਪ੍ਰਾਪਤ ਕਰ ਚੁੱਕਾ ਹੈ। ਹਵਾਲਾ: <a href="https://www.microsoft.com/research/articles/magentic-one-a-generalist-multi-agent-system-for-solving-complex-tasks" target="_blank">Magentic One</a>। ਇਸ ਅਮਲ ਵਿੱਚ, ਅੰਤਰਰਾਸ਼ਟਰਕਾਰਕ ਕਾਰਜ ਵਿਸ਼ੇਸ਼ ਯੋਜਨਾਵਾਂ ਬਣਾਉਂਦਾ ਹੈ ਅਤੇ ਇਹ ਕਾਰਜ ਉਪਲਬਧ ਏਜੰਟਾਂ ਨੂੰ ਸੁਪਰਵਾਈਜ਼ ਕਰਦਾ ਹੈ। ਯੋਜਨਾਂ ਦੇ ਇਲਾਵਾ, ਅੰਤਰਰਾਸ਼ਟਰਕਾਰਕ ਇੱਕ ਟ੍ਰੈਕਿੰਗ ਵਿਧੀ ਵੀ ਵਰਤਦਾ ਹੈ ਜੋ ਕਾਰਜ ਦੀ ਪ੍ਰਗਤੀ ਨੂੰ ਨਿਗਰਾਨੀ ਕਰਦਾ ਹੈ ਅਤੇ ਜਰੂਰਤ ਮੁਤਾਬਕ ਦੁਬਾਰਾ ਯੋਜਨਾ ਬਣਾਉਂਦਾ ਹੈ।

### ਯੋਜਨਾ ਬਣਾਉਣ ਦੇ ਡਿਜ਼ਾਈਨ ਪੈਟਰਨ ਬਾਰੇ ਹੋਰ ਸਵਾਲ ਹਨ?

ਦੂਜੇ ਸਿੱਖਣ ਵਾਲਿਆਂ ਨਾਲ ਮਿਲਣ, ਦਫ਼ਤਰ ਵਾਰੀਏਂਸ਼ ਵਿੱਚ ਸ਼ਾਮਲ ਹੋਣ ਅਤੇ ਆਪਣੇ AI ਏਜੰਟਸ ਸਬੰਧੀ ਸਵਾਲ ਪੁੱਛਣ ਲਈ [Microsoft Foundry Discord](https://aka.ms/ai-agents/discord) ਵਿੱਚ ਸ਼ਾਮਲ ਹੋਵੋ।

## ਪਿਛਲਾ ਪਾਠ

[ਯਕੀਨੀ ਯੋਗ AI ਏਜੰਟ ਬਣਾਉਣਾ](../06-building-trustworthy-agents/README.md)

## ਅਗਲਾ ਪਾਠ

[ਬਹੁ-ਏਜੰਟ ਡਿਜ਼ਾਈਨ ਪੈਟਰਨ](../08-multi-agent/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ਡਿਸਕਲੇਮਰ**:
ਇਹ ਦਸਤਾਵੇਜ਼ AI ਅਨੁਵਾਦ ਸੇਵਾ [Co-op Translator](https://github.com/Azure/co-op-translator) ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਅਨੁਵਾਦਿਤ ਕੀਤਾ ਗਿਆ ਹੈ। ਜਦੋਂ ਕਿ ਅਸੀਂ ਸਹੀਅਤ ਲਈ ਕੋਸ਼ਿਸ਼ ਕਰਦੇ ਹਾਂ, ਕਿਰਪਾ ਕਰਕੇ ਜਾਣੂ ਹੋਵੋ ਕਿ ਸਵੈਚਾਲਿਤ ਅਨੁਵਾਦਾਂ ਵਿੱਚ ਗਲਤੀਆਂ ਜਾਂ ਅਸੂਚਨਾਵਾਂ ਹੋ ਸਕਦੀਆਂ ਹਨ। ਮੂਲ ਦਸਤਾਵੇਜ਼ ਉਸ ਦੀ ਮੂਲ ਭਾਸ਼ਾ ਵਿੱਚ ਹੀ ਪ੍ਰਮਾਣਿਕ ਸ੍ਰੋਤ ਮੰਨਿਆ ਜਾਣਾ ਚਾਹੀਦਾ ਹੈ। ਮਹੱਤਵਪੂਰਨ ਜਾਣਕਾਰੀ ਲਈ, ਪ੍ਰੋਫੈਸ਼ਨਲ ਮਨੁੱਖੀ ਅਨੁਵਾਦ ਦੀ ਸਿਫਾਰਿਸ਼ ਕੀਤੀ ਜਾਂਦੀ ਹੈ। ਅਸੀਂ ਇਸ ਅਨੁਵਾਦ ਦੀ ਵਰਤੋਂ ਕਾਰਨ ਹੋਣ ਵਾਲੀਆਂ ਕਿਸੇ ਵੀ ਗਲਤਫਹਿਮੀਆਂ ਜਾਂ ਗਲਤ ਅਰਥ ਲਗਾਉਣ ਲਈ ਜ਼ਿੰਮੇਵਾਰ ਨਹੀਂ ਹਾਂ।
<!-- CO-OP TRANSLATOR DISCLAIMER END -->