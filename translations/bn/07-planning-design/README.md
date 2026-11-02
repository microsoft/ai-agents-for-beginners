[![Planning Design Pattern](../../../translated_images/bn/lesson-7-thumbnail.f7163ac557bea123.webp)](https://youtu.be/kPfJ2BrBCMY?si=9pYpPXp0sSbK91Dr)

> _(এই পাঠের ভিডিও দেখতে উপরের চিত্রটিতে ক্লিক করুন)_

# পরিকল্পনা ডিজাইন

## পরিচিতি

এই পাঠে আলোচনা করা হবে

* একটি পরিষ্কার সামগ্রিক লক্ষ্য নির্ধারণ করা এবং একটি জটিল কাজকে পরিচালনাযোগ্য কার্যসমূহে বিভক্ত করা।
* আরও নির্ভরযোগ্য এবং মেশিন-পঠনযোগ্য প্রতিক্রিয়ার জন্য কাঠামোবদ্ধ আউটপুট ব্যবহার করা।
* গতিশীল কাজ এবং অপ্রত্যাশিত ইনপুট পরিচালনার জন্য ইভেন্ট-চালিত পদ্ধতি প্রয়োগ করা।

## শেখার লক্ষ্যসমূহ

এই পাঠ শেষ করার পর, আপনি জানতে পারবেন:

* এআই এজেন্টের জন্য একটি সামগ্রিক লক্ষ্য চিহ্নিত এবং নির্ধারণ করা যাতে এজেন্ট স্পষ্টভাবে জানে কি অর্জন করতে হবে।
* একটি জটিল কাজকে ছোট ছোট অংশে বিভক্ত করা এবং সেগুলোকে যৌক্তিক ক্রমে সাজানো।
* এজেন্টদের প্রয়োজনীয় সরঞ্জাম (যেমন, অনুসন্ধান টুল বা ডেটা বিশ্লেষণ সরঞ্জাম) প্রদান করা, কখন এবং কীভাবে সেগুলো ব্যবহার করা হবে তা সিদ্ধান্ত নেওয়া, এবং অপ্রত্যাশিত পরিস্থিতি মোকাবেলা করা।
* উপ-কার্যগুলির ফলাফল মূল্যায়ন করা, কর্মদক্ষতা পরিমাপ করা, এবং চূড়ান্ত আউটপুট উন্নতির জন্য ক্রিয়াকলাপ পুনরাবৃত্তি করা।

## সামগ্রিক লক্ষ্য নির্ধারণ এবং একটি কাজকে বিভক্ত করা

![সাহায্যে লক্ষ্য ও কাজ নির্ধারণ](../../../translated_images/bn/defining-goals-tasks.d70439e19e37c47a.webp)

অধিকাংশ বাস্তব বিশ্বের কাজ একক পর্যায়ে মোকাবেলা করার জন্য অত্যন্ত জটিল। একটি এআই এজেন্টের জন্য একটি সংক্ষিপ্ত উদ্দেশ্য প্রয়োজন যা তার পরিকল্পনা এবং কর্ম পরিচালনা করবে। উদাহরণস্বরূপ লক্ষ্যটি বিবেচনা করুন:

    "৩ দিনের ভ্রমণসূচি তৈরি করুন।"

যদিও এটি প্রকাশ করতে সহজ, তবে এখনও এটি পরিশোধনের প্রয়োজন। লক্ষ্য যত স্পষ্ট হবে, এজেন্ট (এবং যেকোনো মানব সহযোগী) ততই সঠিক ফলাফল অর্জনে মনোনিবেশ করতে পারবে, যেমন একটি বিস্তৃত সূচি তৈরি করা যার মধ্যে থাকবে বিমান বিকল্প, হোটেল সুপারিশ এবং কার্যক্রম প্রস্তাবনা।

### কাজের বিভাজন

বড় বা জটিল কাজগুলো ছোট, লক্ষ্য নির্ধারিত উপকার্যে বিভক্ত করলে এগুলো পরিচালনাযোগ্য হয়।
ভ্রমণসূচির উদাহরণে, আপনি লক্ষ্যটি নিম্নরূপ ভাগ করতে পারেন:

* বিমান বুকিং
* হোটেল বুকিং
* গাড়ি ভাড়া
* ব্যক্তিগতকরণ

প্রতিটি উপকার্যকে সমর্পিত এজেন্ট বা প্রক্রিয়ার মাধ্যমে সম্পন্ন করা যায়। একজন এজেন্ট বিমান সেরা ডিল খুঁজে বের করায় বিশেষজ্ঞ হতে পারে, অন্যজন হোটেল বুকিং এ ফোকাস করতে পারে, ইত্যাদি। একটি সমন্বয়কারী বা "ডাউনস্ট্রিম" এজেন্ট শেষে একত্রিত itineray ব্যবহারকারীর কাছে প্রেরণ করতে পারে।

এই মডুলার পদ্ধতিটি ধাপে ধাপে উন্নতির সুবিধাও দেয়। উদাহরণস্বরূপ, আপনি খাদ্য এবং স্থানীয় কার্যক্রম প্রস্তাবনার জন্য বিশেষজ্ঞ এজেন্ট যোগ করতে পারেন এবং সময়ের সাথে সূচি উন্নত করতে পারেন।

### কাঠামোবদ্ধ আউটপুট

লার্জ ল্যাঙ্গুয়েজ মডেল (LLMs) কাঠামোবদ্ধ আউটপুট (যেমন JSON) তৈরি করতে পারে যা ডাউনস্ট্রিম এজেন্ট বা সেবাগুলোর জন্য সহজে পার্স এবং প্রক্রিয়াজাত করা যায়। বিশেষত একটি বহু-এজেন্ট ব্যবস্থায়, যেখানে পরিকল্পনা আউটপুট পাওয়ার পর আমরা এই কাজগুলো সম্পাদন করতে পারি।

নিম্নলিখিত পাইথন স্নিপেট একটি সহজ পরিকল্পনা এজেন্টকে লক্ষ্যকে উপকার্যে বিভক্ত করতে এবং একটি কাঠামোবদ্ধ পরিকল্পনা তৈরি করতে দেখায়:

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

# ট্রাভেল সাবটাস্ক মডেল
class TravelSubTask(BaseModel):
    task_details: str
    assigned_agent: AgentEnum  # আমরা এজেন্টকে কাজটি প্রদান করতে চাই

class TravelPlan(BaseModel):
    main_task: str
    subtasks: List[TravelSubTask]
    is_greeting: bool

provider = FoundryChatClient(
    project_endpoint=os.environ["AZURE_AI_PROJECT_ENDPOINT"],
    model=os.environ["AZURE_AI_MODEL_DEPLOYMENT_NAME"],
    credential=AzureCliCredential(),
)

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

### বহু-এজেন্ট সমন্বয়ের সঙ্গে পরিকল্পনা এজেন্ট

এই উদাহরণে, একটি সেম্যান্টিক রাউটার এজেন্ট ব্যবহারকারীর অনুরোধ গ্রহণ করে (যেমন, "আমার যাত্রার জন্য একটি হোটেল পরিকল্পনা দরকার।").

তারপর পরিকল্পনাকর্তা:

* হোটেল পরিকল্পনা গ্রহণ করে: ব্যবহারকারীর বার্তা গ্রহণ করে এবং সিস্টেম প্রম্পট (উপলব্ধ এজেন্টের বিশদসহ) ভিত্তিতে একটি কাঠামোবদ্ধ ভ্রমণ পরিকল্পনা তৈরি করে।
* এজেন্ট এবং তাদের টুলসের তালিকা দেয়: এজেন্ট রেজিস্ট্রিতে এজেন্টদের (যেমন বিমান, হোটেল, গাড়ি ভাড়া, এবং কার্যক্রম) তালিকা থাকে এবং তারা যেসব ফাংশন বা টুলস অফার করে তা থাকে।
* পরিকল্পনাটি সংশ্লিষ্ট এজেন্টদের কাছে প্রেরণ করে: উপকার্যের সংখ্যার উপর নির্ভর করে, পরিকল্পনাকর্তা বার্তাটি সরাসরি একক-কার্যের জন্য নির্দিষ্ট এজেন্টকে পাঠায় অথবা বহু-এজেন্ট সমন্বয়ের জন্য একটি গ্রুপ চ্যাট ম্যানেজারের মাধ্যমে সমন্বয় করে।
* ফলাফল সংক্ষেপ করে: অবশেষে, পরিকল্পনাকর্তা স্পষ্টতার জন্য তৈরি পরিকল্পনার সংক্ষিপ্তসার করে।
নিম্নলিখিত পাইথন কোড নমুনা এই ধাপগুলো প্রদর্শন করে:

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

# ট্রাভেল সাবটাস্ক মডেল

class TravelSubTask(BaseModel):
    task_details: str
    assigned_agent: AgentEnum # আমরা এজেন্টকে টাস্ক অর্পণ করতে চাই

class TravelPlan(BaseModel):
    main_task: str
    subtasks: List[TravelSubTask]
    is_greeting: bool
import json
import os
from typing import Optional

from agent_framework.foundry import FoundryChatClient
from azure.identity import AzureCliCredential

# ক্লায়েন্ট তৈরি করুন

provider = FoundryChatClient(
    project_endpoint=os.environ["AZURE_AI_PROJECT_ENDPOINT"],
    model=os.environ["AZURE_AI_MODEL_DEPLOYMENT_NAME"],
    credential=AzureCliCredential(),
)

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

# JSON হিসেবে লোড করার পর প্রতিক্রিয়া সামগ্রী মুদ্রণ করুন

pprint(json.loads(response_content))
```

আগের কোডের আউটপুট যা প্রদর্শিত হয়েছে এবং আপনি এরপর এই কাঠামোবদ্ধ আউটপুট ব্যবহার করে `assigned_agent` এ রুট করতে এবং ভ্রমণ পরিকল্পনা ব্যবহারকারীর কাছে সংক্ষেপ করতে পারেন।

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

আগের কোড নমুনার উদাহরণ নোটবুকটি এখানে পাওয়া যায় [এখানে](./code_samples/07-python-agent-framework.ipynb)।

### পুনরাবৃত্তিমূলক পরিকল্পনা

কিছু কাজ বারের পর বার বা পুনর্নির্মাণের প্রয়োজন হতে পারে, যেখানে একটি উপ-কার্যের ফলাফল পরবর্তী উপ-কার্যকে প্রভাবিত করে। উদাহরণস্বরূপ, যদি এজেন্ট বিমান বুকিং করার সময় অপ্রত্যাশিত ডেটা ফর্ম্যাট খুঁজে পায়, তবে হোটেল বুকিংয়ের আগে তার কৌশল পরিবর্তন করতে হতে পারে।

পাশাপাশি, ব্যবহারকারীর প্রতিক্রিয়া (যেমন, একজন মানুষ আগে উড়ানের পছন্দ করে) আংশিক পুনঃপরিকল্পনা প্রবর্তন করতে পারে। এই গতিশীল, পুনরাবৃত্তিমূলক পন্থাটি নিশ্চিত করে যে চূড়ান্ত সমাধান বাস্তব জগতের বাধ্যবাধকতা এবং পরিবর্তিত ব্যবহারকারী পছন্দের সাথে সামঞ্জস্যপূর্ণ।

যেমন কোডের উদাহরণ

```python
import os
from agent_framework.foundry import FoundryChatClient
from azure.identity import AzureCliCredential
#.. পূর্ববর্তী কোডের মতোই এবং ব্যবহারকারীর ইতিহাস, বর্তমান পরিকল্পনা প্রেরণ করুন

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
# .. পুনঃপরিকল্পনা করুন এবং সংশ্লিষ্ট এজেন্টদের কাছে কাজগুলি পাঠান
```

বৃহত্তর পরিকল্পনার জন্য দয়া করে Magnetic One <a href="https://www.microsoft.com/research/articles/magentic-one-a-generalist-multi-agent-system-for-solving-complex-tasks" target="_blank">ব্লগপোস্ট</a> দেখুন জটিল কাজগুলো সমাধানের জন্য।

## সারাংশ

এই আর্টিকেলটিতে আমরা দেখেছি কীভাবে একটি পরিকল্পনাকারী তৈরি করা যায় যা গতিশীলভাবে উপলব্ধ এজেন্ট নির্বাচন করতে পারে। পরিকল্পনাকারীর আউটপুট কাজগুলোকে উপকার্যে বিভক্ত করে এবং এজেন্টদের নিয়োগ দেয় যেন কাজগুলো সম্পাদিত হতে পারে। এজেন্টদের ধরে নেওয়া হয় যে তাদের কাজ সম্পাদনের জন্য প্রয়োজনীয় ফাংশন/সরঞ্জাম অ্যাক্সেস আছে। এজেন্টদের পাশাপাশি আপনি প্রতিফলন, সারাংশকারী, এবং রাউন্ড রবিন চ্যাটের মতো অন্যান্য প্যাটার্নও অন্তর্ভুক্ত করতে পারেন আরও কাস্টমাইজেশনের জন্য।

## অতিরিক্ত সম্পদ

Magnetic One - একটি সাধারণ উদ্দেশ্যের বহু-এজেন্ট সিস্টেম যা জটিল কাজ সমাধানে ব্যবহৃত হয় এবং বহু চ্যালেঞ্জিং এজেন্টিক বেঞ্চমার্কে চমৎকার ফলাফল অর্জন করেছে। রেফারেন্স: <a href="https://www.microsoft.com/research/articles/magentic-one-a-generalist-multi-agent-system-for-solving-complex-tasks" target="_blank">Magnetic One</a>. এই বাস্তবায়নে, অর্কেস্ট্রেটর নির্দিষ্ট কাজের পরিকল্পনা তৈরি করে এবং উপলব্ধ এজেন্টদের কাছে ঐ কাজগুলো বণ্টন করে। পরিকল্পনার পাশাপাশি অর্কেস্ট্রেটর একটি ট্র্যাকিং ব্যবস্থাও ব্যবহার করে কাজের অগ্রগতি নজরদারি এবং প্রয়োজনে পুনঃপরিকল্পনা করে।

### পরিকল্পনা ডিজাইন প্যাটার্ন সম্পর্কে আরও প্রশ্ন আছে?

[Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D) এ যোগ দিন অন্যান্য শিক্ষার্থীদের সাথে মেলামেশা করতে, অফিস নির্ধারিত সময়ে অংশগ্রহণ করতে এবং আপনার AI এজেন্ট সম্পর্কিত প্রশ্নের উত্তর পেতে।

## পূর্ববর্তী পাঠ

[বিশ্বাসযোগ্য AI এজেন্ট নির্মাণ](../06-building-trustworthy-agents/README.md)

## পরবর্তী পাঠ

[বহু-এজেন্ট ডিজাইন প্যাটার্ন](../08-multi-agent/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**অস্বীকৃতি**:
এই নথিটি AI অনুবাদ পরিষেবা [Co-op Translator](https://github.com/Azure/co-op-translator) ব্যবহার করে অনূদিত হয়েছে। যদিও আমরা শুদ্ধতার জন্য চেষ্টা করি, অনুগ্রহ করে মনে রাখবেন যে স্বয়ংক্রিয় অনুবাদে ত্রুটি বা অসঙ্গতি থাকতে পারে। মূল নথিটি তার স্বভাষায় কর্তৃত্বপূর্ণ উৎস হিসেবে বিবেচিত হওয়া উচিত। গুরুত্বপূর্ণ তথ্যের জন্য পেশাদার মানব অনুবাদ সুপারিশ করা হয়। এই অনুবাদের ব্যবহারে প্রয়োজনীয় ভুল বোঝাবুঝি বা ভুল ব্যাখ্যার জন্য আমরা দায়বদ্ধ নই।
<!-- CO-OP TRANSLATOR DISCLAIMER END -->