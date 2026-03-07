[![Planning Design Pattern](../../../translated_images/bn/lesson-7-thumbnail.f7163ac557bea123.webp)](https://youtu.be/kPfJ2BrBCMY?si=9pYpPXp0sSbK91Dr)

> _(এই পাঠের ভিডিও দেখতে উপরের ছবিটিতে ক্লিক করুন)_

# পরিকল্পনা নকশা

## পরিচিতি

এই পাঠে আলোচনা করা হবে

* একটি স্পষ্ট সামগ্রিক লক্ষ্য নির্ধারণ এবং একটি জটিল কাজকে পরিচালনাযোগ্য কাজগুলিতে বিভক্ত করা।
* আরও নির্ভরযোগ্য এবং মেশিন-পঠনযোগ্য প্রতিক্রিয়ার জন্য কাঠামোবদ্ধ আউটপুট ব্যবহার করা।
* গতিশীল কাজ এবং অপ্রত্যাশিত ইনপুট পরিচালনার জন্য একটি ইভেন্ট-চালিত পদ্ধতি প্রয়োগ করা।

## শেখার লক্ষ্য

এই পাঠ সম্পন্ন করার পরে, আপনি সম্পর্কে ধারণা পাবেন:

* একটি AI এজেন্টের জন্য একটি সামগ্রিক লক্ষ্য চিহ্নিত এবং নির্ধারণ করা, নিশ্চিত করা যে এটি স্পষ্টভাবে জানে কি অর্জন করতে হবে।
* একটি জটিল কাজকে পরিচালনাযোগ্য উপকাজে বিভাজন এবং সেগুলিকে যুক্তিসঙ্গত ক্রমে সংগঠিত করা।
* এজেন্টদের সঠিক সরঞ্জাম (যেমন অনুসন্ধান সরঞ্জাম বা ডেটা বিশ্লেষণ সরঞ্জাম) দিয়ে সজ্জিত করা, কখন এবং কীভাবে সেগুলি ব্যবহার করা হবে তা সিদ্ধান্ত নেওয়া, এবং উদ্ভূত অপ্রত্যাশিত পরিস্থিতি পরিচালনা করা।
* উপকাজের ফলাফল মূল্যায়ন, কর্মক্ষমতা পরিমাপ এবং চূড়ান্ত আউটপুট উন্নত করতে ক্রিয়াগুলির পুনরাবৃত্তি করা।

## সামগ্রিক লক্ষ্য নির্ধারণ এবং একটি কাজকে বিভক্ত করা

![Defining Goals and Tasks](../../../translated_images/bn/defining-goals-tasks.d70439e19e37c47a.webp)

অধিকাংশ বাস্তব বিশ্বের কাজ একক ধাপে মোকাবেলা করা 너무 জটিল। একটি AI এজেন্টের পরিকল্পনা ও কাজের নির্দেশনার জন্য একটি সংক্ষিপ্ত লক্ষ্য প্রয়োজন। উদাহরণস্বরূপ, নিম্নলিখিত লক্ষ্য বিবেচনা করুন:

    "৩ দিনের ভ্রমণ পরিকল্পনা তৈরি করুন।"

যদিও এটি সহজে বলা যায়, তবে এটি এখনও পরিমার্জনা প্রয়োজন। লক্ষ্য যত স্পষ্ট হবে, এজেন্ট (এবং যেকোনো মানব সহযোগী) তত ভালোভাবে সঠিক ফলাফল অর্জনে মনোযোগ দিতে পারবে, যেমন একটি বিস্তৃত পরিকল্পনা তৈরি করা যার মধ্যে বিমান বন্দর বিকল্প, হোটেল সুপারিশ এবং কার্যকলাপ পরামর্শ অন্তর্ভুক্ত থাকবে।

### কাজের বিভাজন

বড় বা জটিল কাজগুলি ছোট, লক্ষ্য-কেন্দ্রিক উপকাজে বিভক্ত করলে আরও সাশ্রয়ী হয়। ভ্রমণ পরিকল্পনার উদাহরণে, আপনি লক্ষ্যটি বিভক্ত করতে পারেন:

* বিমান টিকিট বুকিং
* হোটেল বুকিং
* গাড়ি ভাড়া
* ব্যক্তিগতকরণ

প্রতিটি উপকাজকে পরে নিবেদিত এজেন্ট বা প্রক্রিয়া দ্বারা মোকাবেলা করা যেতে পারে। এক এজেন্ট সেরা বিমান তালিকা খুঁজে পেতে বিশেষজ্ঞ হতে পারে, অন্য হোটেল বুকিং-এ মনোযোগ কেন্দ্রীভূত করতে পারে, ইত্যাদি। একটি সমন্বয়কারী বা "ডাউনস্ট্রিম" এজেন্ট পরে এই ফলাফলগুলি একত্রিত করে একসাথে একটি সামঞ্জস্যপূর্ণ পরিকল্পনা তৈরি করতে পারে।

এই মডুলার পদ্ধতি অগ্রগতি ও উন্নয়ন জন্য সুযোগ দেয়। উদাহরণস্বরূপ, আপনি খাদ্য সুপারিশ বা স্থানীয় কার্যকলাপ পরামর্শের জন্য বিশেষায়িত এজেন্ট যোগ করতে পারেন এবং সময়ের সাথে সাথে পরিকল্পনাটি পরিমার্জন করতে পারেন।

### কাঠামোবদ্ধ আউটপুট

বড় ভাষার মডেল (LLMs) কাঠামোবদ্ধ আউটপুট (যেমন JSON) তৈরি করতে পারে যা ডাউনস্ট্রিম এজেন্ট বা সেবাগুলির পক্ষে পার্স এবং প্রক্রিয়া করা সহজ। এটি বিশেষত বহু-এজেন্ট প্রসঙ্গে উপযুক্ত, যেখানে পরিকল্পনার আউটপুট প্রাপ্তির পরে এগুলি কার্যকর করা যায়।

নিম্নলিখিত পাইথন কোড একটি সাধারণ পরিকল্পনাকারী এজেন্ট প্রদর্শন করে যা একটি লক্ষ্যকে উপকাজে বিভক্ত করে এবং কাঠামোবদ্ধ পরিকল্পনা তৈরি করে:

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

# ভ্রমণ সাবটাস্ক মডেল
class TravelSubTask(BaseModel):
    task_details: str
    assigned_agent: AgentEnum  # আমরা অ্যাজেন্টকে টাস্ক বরাদ্দ করতে চাই

class TravelPlan(BaseModel):
    main_task: str
    subtasks: List[TravelSubTask]
    is_greeting: bool

provider = AzureAIProjectAgentProvider(credential=AzureCliCredential())

# ব্যবহারকারীর বার্তা সংজ্ঞায়িত করুন
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

### বহু-এজেন্ট সমন্বয়ের সঙ্গে পরিকল্পনাকারী এজেন্ট

এই উদাহরণে, একটি সেমান্টিক রাউটার এজেন্ট একটি ব্যবহারকারী অনুরোধ গ্রহণ করে (যেমন, "আমার ট্রিপের জন্য একটি হোটেল পরিকল্পনা দরকার।")।

পরিকল্পনাকারী তখন:

* হোটেল পরিকল্পনা গ্রহণ করে: পরিকল্পনাকারী ব্যবহারকারীর বার্তা গ্রহণ করে এবং একটি সিস্টেম প্রম্পট (প্রযোজ্য এজেন্ট বিবরণ সহ) এর ভিত্তিতে একটি কাঠামোবদ্ধ ট্রাভেল পরিকল্পনা তৈরি করে।
* এজেন্ট এবং তাদের সরঞ্জাম তালিকা করে: এজেন্ট রেজিষ্ট্রি এজেন্টদের তালিকা ধরে রাখে (যেমন বিমান, হোটেল, গাড়ি ভাড়া এবং কার্যকলাপের জন্য) সাথে তাদের প্রদান করা ফাংশন বা সরঞ্জাম।
* পরিকল্পনাটি সংশ্লিষ্ট এজেন্টদের কাছে পৌঁছে দেয়: উপকাজের সংখ্যার ওপর নির্ভর করে, পরিকল্পনাকারী বার্তাটি সরাসরি একটি নির্দিষ্ট এজেন্টকে পাঠায় (একক কাজ পরিস্থিতিতে) অথবা বহু-এজেন্ট সহযোগিতার জন্য একটি গ্রুপ চ্যাট ম্যানেজারের মাধ্যমে সমন্বয় করে।
* ফলাফল সারাংশ তৈরি করে: অবশেষে, পরিকল্পনাকারী পরিষ্কারতার জন্য তৈরি পরিকল্পনার সারাংশ তৈরি করে।

নিম্নলিখিত পাইথন কোড এই ধাপগুলি ব্যাখ্যা করে:

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

# ভ্রমণ সাবটাস্ক মডেল

class TravelSubTask(BaseModel):
    task_details: str
    assigned_agent: AgentEnum # আমরা এজেন্টকে কাজটি_assignment করতে চাই

class TravelPlan(BaseModel):
    main_task: str
    subtasks: List[TravelSubTask]
    is_greeting: bool
import json
import os
from typing import Optional

from agent_framework.azure import AzureAIProjectAgentProvider
from azure.identity import AzureCliCredential

# ক্লায়েন্ট তৈরি করুন

provider = AzureAIProjectAgentProvider(credential=AzureCliCredential())

from pprint import pprint

# ব্যবহারকারীর বার্তা নির্ধারণ করুন

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

# JSON হিসেবে লোড করার পরে প্রতিক্রিয়ার বিষয়বস্তু মুদ্রণ করুন

pprint(json.loads(response_content))
```

এর পরের আউটপুটটি পূর্বের কোডের ফলাফল এবং আপনি এই কাঠামোবদ্ধ আউটপুট ব্যবহার করে `assigned_agent` এ রুট করতে পারেন এবং পরিশেষে ব্যবহারকারীর কাছে ট্রাভেল পরিকল্পনার সারাংশ প্রদান করতে পারেন।

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

পূর্বের কোড নমুনা সহ একটি উদাহরণ নোটবুক এখানে পাওয়া যায় [here](07-python-agent-framework.ipynb).

### পুনরাবৃত্তিমূলক পরিকল্পনা

কিছু কাজ একটি পরস্পরণ এবং পুনঃপরিকল্পনার প্রয়োজন যেখানে একটি উপকাজের ফলাফল পরের উপকাজকে প্রভাবিত করে। উদাহরণস্বরূপ, যদি এজেন্ট বিমানের বুকিং করার সময় একটি অপ্রত্যাশিত ডেটা ফর্ম্যাট আবিষ্কার করে, তবে হয়তো সে তার কৌশল পরিবর্তন করতে হবে আগে হোটেল বুকিংয়ের জন্য এগিয়ে যাওয়ার আগে।

অতিরিক্তভাবে, ব্যবহারকারীর প্রতিক্রিয়া (যেমন একজন ব্যক্তি আরম্ভে একটি দ্রুত বিমান পছন্দ করেন) আংশিক পুনঃপরিকল্পনা চালু করতে পারে। এই গতিশীল, পুনরাবৃত্তিমূলক পদ্ধতি নিশ্চিত করে চূড়ান্ত সমাধান বাস্তব বিশ্ব পরিস্থিতি এবং পরিবর্তিত ব্যবহারকারীর পছন্দের সাথে সঙ্গতিপূর্ণ হয়।

উদাহরণস্বরূপ কোড

```python
from agent_framework.azure import AzureAIProjectAgentProvider
from azure.identity import AzureCliCredential
#.. আগের কোডের মতোই এবং ব্যবহারকারীর ইতিহাস, বর্তমান পরিকল্পনা প্রেরণ করুন

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
# .. পুনরায় পরিকল্পনা করুন এবং কাজগুলি সংশ্লিষ্ট এজেন্টদের পাঠান
```

অধিক ব্যাপক পরিকল্পনার জন্য Magnetic One এর <a href="https://www.microsoft.com/research/articles/magentic-one-a-generalist-multi-agent-system-for-solving-complex-tasks" target="_blank">ব্লগপোস্ট</a> দেখুন যা জটিল কাজ সমাধানে কাজ করে।

## সারাংশ

এই প্রবন্ধে আমরা দেখেছি কিভাবে একটি পরিকল্পনাকারী তৈরি করতে হয় যা প্রযোজ্য এজেন্টগুলি গতিশীলভাবে নির্বাচন করতে সক্ষম। পরিকল্পনাকারীর আউটপুট কাজগুলোকে বিভক্ত করে এবং এজেন্টদের নিয়োগ দেয় যাতে তারা সম্পাদন করতে পারে। ধারণা করা হয় যে এজেন্টদের কাছে কাজ সম্পাদন করতে প্রয়োজনীয় ফাংশন/সরঞ্জাম অ্যাক্সেস আছে। এজেন্টদের পাশাপাশি, আপনি প্রতিবিম্বন, সারসংক্ষেপকারী, এবং রাউন্ড রবিন চ্যাটের মতো অন্যান্য প্যাটার্ন যুক্ত করতে পারেন আরও কাস্টোমাইজেশনের জন্য।

## অতিরিক্ত সম্পদ

Magentic One - একটি সাধারণ মাল্টি-এজেন্ট সিস্টেম যা জটিল কাজ সমাধানে ব্যবহৃত হয় এবং বহু চ্যালেঞ্জিং এজেন্টিক বেঞ্চমার্কে চমৎকার ফলাফল অর্জন করেছে। রেফারেন্স: <a href="https://www.microsoft.com/research/articles/magentic-one-a-generalist-multi-agent-system-for-solving-complex-tasks" target="_blank">Magentic One</a>। এই বাস্তবায়নে, অর্কেস্ট্রেটর কাজ নির্দিষ্ট পরিকল্পনা তৈরি করে এবং উপলব্ধ এজেন্টদের কাছে কাজগুলিকে বিতরণ করে। পরিকল্পনার পাশাপাশি, অর্কেস্ট্রেটর একটি ট্র্যাকিং মেকানিজমও ব্যবহার করে কাজের অগ্রগতি পর্যবেক্ষণ করতে এবং প্রয়োজনে পুনঃপরিকল্পনা করতে।

### পরিকল্পনা নকশা প্যাটার্ন সম্পর্কে আরও প্রশ্ন আছে?

অন্য শিক্ষার্থীদের সাথে দেখা করতে, অফিস আওয়ার অংশ নিতে এবং আপনার AI এজেন্টের প্রশ্নের উত্তর পেতে [Microsoft Foundry Discord](https://aka.ms/ai-agents/discord) যোগ দিন।

## আগের পাঠ

[বিশ্বাসযোগ্য AI এজেন্ট তৈরি করা](../06-building-trustworthy-agents/README.md)

## পরের পাঠ

[বহু-এজেন্ট নকশা প্যাটার্ন](../08-multi-agent/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**অস্বীকৃতি**:  
এই নথিটি AI অনুবাদ সেবা [Co-op Translator](https://github.com/Azure/co-op-translator) ব্যবহার করে অনূদিত হয়েছে। আমরা যথাসাধ্য সঠিকতার চেষ্টা করি, তবুও স্বয়ংক্রিয় অনুবাদে ভুল বা অমিল থাকতে পারে। আদি নথির নিজ ভাষার সংস্করণকে কর্তৃত্বপূর্ণ উৎস হিসেবে বিবেচনা করা উচিত। গুরুত্বপূর্ণ তথ্যের জন্য পেশাদার মানব অনুবাদ গ্রহণ করার পরামর্শ দেওয়া হয়। এই অনুবাদ ব্যবহারে কোনো ভুলবোঝাবুঝি বা ভুল ব্যাখ্যার জন্য আমরা দায়ী নই।
<!-- CO-OP TRANSLATOR DISCLAIMER END -->