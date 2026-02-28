[![AI এজেন্ট ফ্রেমওয়ার্ক অন্বেষণ](../../../translated_images/bn/lesson-2-thumbnail.c65f44c93b8558df.webp)](https://youtu.be/ODwF-EZo_O8?si=1xoy_B9RNQfrYdF7)

> _(উপরের ছবিতে ক্লিক করে এই পাঠের ভিডিও দেখুন)_

# AI এজেন্ট ফ্রেমওয়ার্ক অন্বেষণ

AI agent frameworks হল সফটওয়্যার প্ল্যাটফর্মগুলো যা AI এজেন্ট তৈরি, ডিপ্লয়মেন্ট, এবং ব্যবস্থাপনাকে সহজ করার জন্য ডিজাইন করা। এই ফ্রেমওয়ার্কগুলো ডেভেলপারদেরকে প্রি-বিল্ট কম্পোনেন্ট, অ্যাবস্ট্রাকশন, এবং টুল সরবরাহ করে যা জটিল AI সিস্টেমগুলোর উন্নয়নকে ত্বরান্বিত করে।

এই ফ্রেমওয়ার্কগুলো ডেভেলপারদেরকে তাদের অ্যাপ্লিকেশনের অনন্য দিকগুলোর ওপর মনোনিবেশ করতে সহায়তা করে; কারণ এগুলো AI এজেন্ট ডেভেলপমেন্টের সাধারণ চ্যালেঞ্জগুলোর জন্য স্ট্যান্ডার্ডাইজড পদ্ধতি প্রদান করে। এগুলো স্কেলেবিলিটি, অ্যাক্সেসিবিলিটি, এবং কার্যকারিতা উন্নত করে AI সিস্টেম নির্মাণে।

## পরিচিতি 

এই পাঠে আলোচনা করা হবে:

- AI এজেন্ট ফ্রেমওয়ার্ক কী এবং এগুলো ডেভেলপারদেরকে কী অর্জন করতে সহায়তা করে?
- দলগুলো কীভাবে এগুলো ব্যবহার করে দ্রুত প্রোটোটাইপ তৈরি, পুনরাবৃত্তি, এবং তাদের এজেন্টের সক্ষমতা উন্নত করতে পারে?
- Microsoft (<a href="https://aka.ms/ai-agents-beginners/ai-agent-service" target="_blank">Azure AI Agent Service</a> and the <a href="https://learn.microsoft.com/azure/ai-services/openai/how-to/responses" target="_blank">Microsoft Agent Framework</a>) দ্বারা নির্মিত ফ্রেমওয়ার্ক এবং টুলগুলোর মধ্যে পার্থক্য কী?
- আমি কি আমার বিদ্যমান Azure একোসিস্টেম টুলগুলো সরাসরি ইন্টিগ্রেট করতে পারি, নাকি আলাদা স্ট্যান্ডঅ্যালোন সলিউশনের প্রয়োজন?
- Azure AI Agents service কী এবং এটি কীভাবে আমাকে সাহায্য করছে?

## শেখার লক্ষ্য

এই পাঠের লক্ষ্যগুলো আপনাকে সাহায্য করবে বুঝতে:

- AI ডেভেলপমেন্টে AI এজেন্ট ফ্রেমওয়ার্কগুলোর ভূমিকা।
- বুদ্ধিমান এজেন্ট তৈরির জন্য AI এজেন্ট ফ্রেমওয়ার্কগুলো কীভাবে ব্যবহার করবেন।
- AI এজেন্ট ফ্রেমওয়ার্কগুলো দ্বারা সক্রিয় প্রধান ক্ষমতাসমূহ।
- Microsoft Agent Framework এবং Azure AI Agent Service এর মধ্যে পার্থক্যগুলি।

## AI এজেন্ট ফ্রেমওয়ার্ক কী এবং এগুলো ডেভেলপারদের কী করতে সক্ষম করে?

প্রচলিত AI ফ্রেমওয়ার্কগুলো আপনাকে আপনার অ্যাপগুলিতে AI একত্রিত করতে এবং এগুলোকে নিম্নলিখিত উপায়ে উন্নত করতে সাহায্য করতে পারে:

- **ব্যক্তিগতকরণ**: AI ব্যবহারকারীর আচরণ এবং পছন্দ বিশ্লেষণ করে ব্যক্তিগত সুপারিশ, কনটেন্ট এবং অভিজ্ঞতা প্রদান করতে পারে।
উদাহরণ: Netflix-এর মতো স্ট্রিমিং সার্ভিসগুলো দর্শনের ইতিহাসের উপর ভিত্তি করে সিনেমা ও শো সুপারিশ করতে AI ব্যবহার করে, যা ব্যবহারকারীর এনগেজমেন্ট এবং সন্তুষ্টি বাড়ায়।
- **স্বয়ংক্রিয়করণ ও দক্ষতা**: AI পুনরাবৃত্তিমূলক কাজগুলো স্বয়ংক্রিয় করতে, ওয়ার্কফ্লোকে সুষম করতে, এবং অপারেশনাল দক্ষতা উন্নত করতে পারে।
উদাহরণ: কাস্টমার সার্ভিস অ্যাপগুলো সাধারণ জিজ্ঞাসাগুলো পরিচালনা করতে AI-চালিত চ্যাটবট ব্যবহার করে, জবাব সময় হ্রাস করে এবং জটিল বিষয়গুলোর জন্য মানব এজেন্টদের মুক্ত করে।
- **উন্নত ব্যবহারকারীর অভিজ্ঞতা**: AI ভয়েস রিকগনিশন, ন্যাচারাল ল্যাঙ্গুয়েজ প্রসেসিং, এবং প্রেডিক্টিভ টেক্সটের মতো বুদ্ধিমান ফিচার প্রদান করে সামগ্রিক ব্যবহারকারী অভিজ্ঞতা উন্নত করতে পারে।
উদাহরণ: Siri এবং Google Assistant-এর মতো ভার্চুয়াল অ্যাসিস্ট্যান্টগুলো ভয়েস কমান্ড বুঝতে এবং সাড়া দিতে AI ব্যবহার করে, যা ব্যবহারকারীদের ডিভাইসের সাথে যোগাযোগকে সহজ করে।

### সবই দুর্দান্ত শোনাচ্ছে, তাহলে AI Agent Framework-এর ضرورت কেন?

AI Agent ফ্রেমওয়ার্কগুলো শুধু AI ফ্রেমওয়ার্কের চেয়েও বেশি কিছু উপস্থাপন করে। এগুলো এমন বুদ্ধিমান এজেন্ট তৈরির জন্য ডিজাইন করা যাতে ব্যবহারকারী, অন্যান্য এজেন্ট, এবং পরিবেশের সাথে ইন্টারঅ্যাক্ট করে নির্দিষ্ট লক্ষ্য অর্জন করতে পারে। এই এজেন্টগুলো স্বয়ংক্রিয় আচরণ প্রদর্শন করতে পারে, সিদ্ধান্ত নিতে পারে, এবং পরিবর্তনশীল উদ্বেগে অভিযোজিত হতে পারে। AI Agent Framework দ্বারা সক্রিয় কয়েকটি মূল সক্ষমতা দেখি:

- **এজেন্ট সহযোগিতা ও সমন্বয়**: একাধিক AI এজেন্ট তৈরি করতে সক্ষম করে যা একসাথে কাজ করতে, যোগাযোগ করতে, এবং সমন্বয় করে জটিল কাজ সমাধান করতে পারে।
- **টাস্ক স্বয়ংক্রিয়করণ ও ব্যবস্থাপনা**: বহু-ধাপের ওয়ার্কফ্লো স্বয়ংক্রিয়করণ, টাস্ক ডেলিগেশন, এবং এজেন্টদের মধ্যে ডাইনামিক টাস্ক ম্যানেজমেন্টের জন্য মেকানিজম সরবরাহ করে।
- **প্রাসঙ্গিক বোঝাপড়া ও অভিযোজন**: এজেন্টদের প্রাসঙ্গিকতা বোঝার, পরিবেশের পরিবর্তনের সাথে মানিয়ে নেওয়ার, এবং রিয়েল-টাইম তথ্যের ভিত্তিতে সিদ্ধান্ত নেবার ক্ষমতা প্রদান করে।

সারমর্মে, এজেন্টগুলো আপনাকে আরও কিছু করতে দেয় — স্বয়ংক্রিয়করণকে পরবর্তী মাত্রায় নেওয়া, এমন বুদ্ধিমান সিস্টেম তৈরি করা যা পরিবেশ থেকে শেখে এবং অভিযোজিত হতে পারে।

## কীভাবে দ্রুত প্রোটোটাইপ তৈরি, পুনরাবৃত্তি, এবং এজেন্টের সক্ষমতা উন্নত করবেন?

এটাকি দ্রুত পরিবর্তনশীল ক্ষেত্র, কিন্তু বেশিরভাগ AI Agent ফ্রেমওয়ার্কে কিছু সাধারণ ব্যাপার আছে যা আপনাকে দ্রুত প্রোটোটাইপ ও পুনরাবৃত্তি করতে সাহায্য করবে যেমন মডিউলার কম্পোনেন্ট, সহযোগী টুল, এবং রিয়েল-টাইম লার্নিং। এগুলো বিস্তারিত দেখি:

- **মডুলার উপাদান ব্যবহার করুন**: AI SDK গুলো প্রি-বিল্ট কম্পোনেন্ট যেমন AI এবং Memory কনেক্টর, ন্যাচারাল ল্যাঙ্গুয়েজ বা কোড প্লাগইন ব্যবহার করে ফাংশন কলিং, প্রম্পট টেমপ্লেট, এবং আরও অনেক কিছু অফার করে।
- **সহযোগী টুল ব্যবহার করুন**: নির্দিষ্ট ভূমিকা ও টাস্কসহ এজেন্ট ডিজাইন করুন, যাতে তারা সহযোগী ওয়ার্কফ্লো টেস্ট করে উন্নত করতে পারে।
- **রিয়েল-টাইমে শেখা**: এমন ফিডব্যাক লুপ বাস্তবায়ন করুন যেখানে এজেন্টগুলো ইন্টারঅ্যাকশন থেকে শেখে এবং তাদের আচরণ ডাইনামিকভাবে সামঞ্জস্য করে।

### মডুলার উপাদান ব্যবহার করুন

Microsoft Agent Framework-এর মতো SDK গুলো প্রি-বিল্ট কম্পোনেন্ট যেমন AI কনেক্টর, টুল ডেফিনিশন, এবং এজেন্ট ম্যানেজমেন্ট অফার করে।

**দলগুলি এগুলো কীভাবে ব্যবহার করতে পারে**: দলগুলো শূন্য থেকে শুরু না করে দ্রুত এগুলো একত্রিত করে একটি কার্যকরী প্রোটোটাইপ তৈরি করতে পারে, যা দ্রুত পরীক্ষণ এবং পুনরাবৃত্তি সম্ভব করে।

**কিভাবে এটি বাস্তবে কাজ করে**: আপনি ব্যবহারকারী ইনপুট থেকে তথ্য বের করার জন্য একটি প্রি-বিল্ট পার্সার ব্যবহার করতে পারেন, ডেটা সংরক্ষণ ও পুনরুদ্ধারের জন্য একটি মেমোরি মডিউল, এবং ব্যবহারকারীর সাথে ইন্টারঅ্যাক্ট করার জন্য একটি প্রম্পট জেনারেটর—all without having to build these components from scratch. (Note: preserved English fragment as original concept)

**উদাহরণ কোড**. Let's look at an example of how you can use the Microsoft Agent Framework with `AzureAIProjectAgentProvider` to have the model respond to user input with tool calling:

``` python
# মাইক্রোসফ্ট এজেন্ট ফ্রেমওয়ার্ক পাইথন উদাহরণ

import asyncio
import os
from typing import Annotated

from agent_framework.azure import AzureAIProjectAgentProvider
from azure.identity import AzureCliCredential


# ভ্রমণ বুক করার জন্য একটি নমুনা টুল ফাংশন সংজ্ঞায়িত করুন
def book_flight(date: str, location: str) -> str:
    """Book travel given location and date."""
    return f"Travel was booked to {location} on {date}"


async def main():
    provider = AzureAIProjectAgentProvider(credential=AzureCliCredential())
    agent = await provider.create_agent(
        name="travel_agent",
        instructions="Help the user book travel. Use the book_flight tool when ready.",
        tools=[book_flight],
    )

    response = await agent.run("I'd like to go to New York on January 1, 2025")
    print(response)
    # উদাহরণ আউটপুট: ২০২৫ সালের ১ জানুয়ারি নিউ ইয়র্কে আপনার ফ্লাইট সফলভাবে বুক করা হয়েছে। নিরাপদ ভ্রমণ! ✈️🗽


if __name__ == "__main__":
    asyncio.run(main())
```

What you can see from this example is how you can leverage a pre-built parser to extract key information from user input, such as the origin, destination, and date of a flight booking request. This modular approach allows you to focus on the high-level logic.

### সহযোগী টুল ব্যবহার করুন

Microsoft Agent Framework-এর মতো ফ্রেমওয়ার্কগুলো একত্রে কাজ করতে পারে এমন একাধিক এজেন্ট তৈরিতে সুবিধা দেয়।

**দলগুলি এগুলো কীভাবে ব্যবহার করতে পারে**: দলগুলো নির্দিষ্ট ভূমিকা ও টাস্ক সহ এজেন্ট ডিজাইন করতে পারে, যা তাদের সহযোগী ওয়ার্কফ্লো টেস্ট এবং পরিশোধন করতে এবং সামগ্রিক সিস্টেম দক্ষতা উন্নত করতে সক্ষম করে।

**কিভাবে এটি বাস্তবে কাজ করে**: আপনি এমন একটি এজেন্ট টিম তৈরি করতে পারেন যেখানে প্রতিটি এজেন্টের একটি বিশেষায়িত কার্য আছে, যেমন ডেটা পুনরুদ্ধার, বিশ্লেষণ, বা সিদ্ধান্ত গ্রহণ। এই এজেন্টগুলো যোগাযোগ এবং তথ্য ভাগ করে একটি সাধারণ লক্ষ্য অর্জন করতে পারে, যেমন ব্যবহারকারীর প্রশ্নের উত্তর দেয়া বা একটি টাস্ক সম্পন্ন করা।

**উদাহরণ কোড (Microsoft Agent Framework)**:

```python
# মাইক্রোসফট এজেন্ট ফ্রেমওয়ার্ক ব্যবহার করে একাধিক এজেন্ট তৈরি করা যারা একসাথে কাজ করে

import os
from agent_framework.azure import AzureAIProjectAgentProvider
from azure.identity import AzureCliCredential

provider = AzureAIProjectAgentProvider(credential=AzureCliCredential())

# ডেটা পুনরুদ্ধার এজেন্ট
agent_retrieve = await provider.create_agent(
    name="dataretrieval",
    instructions="Retrieve relevant data using available tools.",
    tools=[retrieve_tool],
)

# ডেটা বিশ্লেষণ এজেন্ট
agent_analyze = await provider.create_agent(
    name="dataanalysis",
    instructions="Analyze the retrieved data and provide insights.",
    tools=[analyze_tool],
)

# একটি টাস্কে ধারাবাহিকভাবে এজেন্ট চালানো
retrieval_result = await agent_retrieve.run("Retrieve sales data for Q4")
analysis_result = await agent_analyze.run(f"Analyze this data: {retrieval_result}")
print(analysis_result)
```

What you see in the previous code is how you can create a task that involves multiple agents working together to analyze data. Each agent performs a specific function, and the task is executed by coordinating the agents to achieve the desired outcome. By creating dedicated agents with specialized roles, you can improve task efficiency and performance.

### রিয়েল-টাইমে শেখা

উন্নত ফ্রেমওয়ার্কগুলো রিয়েল-টাইম প্রাসঙ্গিক বোঝাপড়া এবং অভিযোজনের ক্ষমতা প্রদান করে।

**দলগুলি এগুলো কীভাবে ব্যবহার করতে পারে**: দলগুলো এমন ফিডব্যাক লুপ বাস্তবায়ন করতে পারে যেখানে এজেন্টগুলো ইন্টারঅ্যাকশন থেকে শেখে এবং তাদের আচরণ ডাইনামিকভাবে সামঞ্জস্য করে, যার ফলে সক্ষমতার ধারাবাহিক উন্নতি ও পরিশোধন ঘটে।

**কিভাবে এটি বাস্তবে কাজ করে**: এজেন্টগুলো ব্যবহারকারীর ফিডব্যাক, পরিবেশগত ডেটা, এবং টাস্ক আউটকাম বিশ্লেষণ করে তাদের নলেজ বেস আপডেট করতে পারে, সিদ্ধান্ত-গ্রহণ অ্যালগরিদম সামঞ্জস্য করতে পারে, এবং সময়ের সাথে পারফরম্যান্স উন্নত করতে পারে। এই পুনরাবৃত্তিমূলক শেখার প্রক্রিয়া এজেন্টগুলোকে পরিবর্তিত শর্ত এবং ব্যবহারকারীর পছন্দের সাথে খাপ খাইয়ে নিতে সক্ষম করে, ফলে সামগ্রিক সিস্টেম কার্যকারিতা বৃদ্ধি পায়।

## Microsoft Agent Framework এবং Azure AI Agent Service-এর মধ্যে পার্থক্য কী?

এই পদ্ধতিগুলো তুলনা করার অনেক উপায় আছে, কিন্তু চলুন তাদের ডিজাইন, সক্ষমতা, এবং লক্ষ্য ব্যবহারের ক্ষেত্রে কিছু প্রধান পার্থক্যের দিকে তাকাই:

## Microsoft Agent Framework (MAF)

Microsoft Agent Framework একটি স্ট্রীমলাইনড SDK প্রদান করে `AzureAIProjectAgentProvider` ব্যবহার করে AI এজেন্ট নির্মাণের জন্য। এটি ডেভেলপারদেরকে এমন এজেন্ট তৈরি করতে সক্ষম করে যা Azure OpenAI মডেলগুলোর সাথে বিল্ট-ইন টুল কলিং, কথোপকথন পরিচালনা, এবং Azure identity-এর মাধ্যমে এন্টারপ্রাইজ-গ্রেড সিকিউরিটি উপকারিতা ব্যবহার করে।

**ব্যবহার কেস**: টুল ব্যবহার, বহু-ধাপের ওয়ার্কফ্লো, এবং এন্টারপ্রাইজ ইন্টিগ্রেশন সিনারিও সহ প্রোডাকশন-রেডি AI এজেন্ট নির্মাণ।

Microsoft Agent Framework-এর কিছু গুরুত্বপূর্ণ মূল ধারণা হল:

- **এজেন্টসমূহ**. একটি এজেন্ট `AzureAIProjectAgentProvider` দিয়ে তৈরি করা হয় এবং একটি নাম, নির্দেশাবলী, এবং টুল দিয়ে কনফিগার করা হয়। এজেন্ট করতে পারে:
  - **ব্যবহারকারীর বার্তা প্রক্রিয়াকরণ** এবং Azure OpenAI মডেল ব্যবহার করে সাড়া জেনারেট করা।
  - **টুল কল করা** স্বয়ংক্রিয়ভাবে কথোপকথন প্রসঙ্গের ভিত্তিতে।
  - **কথোপকথনের অবস্থা বজায় রাখা** বহু ইন্টারঅ্যাকশনের জুড়ে।

  Here is a code snippet showing how to create an agent:

    ```python
    import os
    from agent_framework.azure import AzureAIProjectAgentProvider
    from azure.identity import AzureCliCredential

    provider = AzureAIProjectAgentProvider(credential=AzureCliCredential())
    agent = await provider.create_agent(
        name="my_agent",
        instructions="You are a helpful assistant.",
    )

    response = await agent.run("Hello, World!")
    print(response)
    ```

- **টুলসমূহ**. ফ্রেমওয়ার্কটি টুলগুলোকে Python ফাংশন হিসেবে ডেফাইন করার সমর্থন করে যেগুলো এজেন্ট স্বয়ংক্রিয়ভাবে ইনভোক করতে পারে। এজেন্ট তৈরি করার সময় টুলগুলো রেজিস্টার করা হয়:

    ```python
    def get_weather(location: str) -> str:
        """Get the current weather for a location."""
        return f"The weather in {location} is sunny, 72\u00b0F."

    agent = await provider.create_agent(
        name="weather_agent",
        instructions="Help users check the weather.",
        tools=[get_weather],
    )
    ```

- **মাল্টি-এজেন্ট সমন্বয়**. আপনি বিভিন্ন বিশেষজ্ঞতার সাথে একাধিক এজেন্ট তৈরি করে তাদের কাজ সমন্বয় করতে পারেন:

    ```python
    planner = await provider.create_agent(
        name="planner",
        instructions="Break down complex tasks into steps.",
    )

    executor = await provider.create_agent(
        name="executor",
        instructions="Execute the planned steps using available tools.",
        tools=[execute_tool],
    )

    plan = await planner.run("Plan a trip to Paris")
    result = await executor.run(f"Execute this plan: {plan}")
    ```

- **Azure Identity ইন্টিগ্রেশন**. ফ্রেমওয়ার্কটি নিরাপদ, কী-লেস অথেন্টিকেশনের জন্য `AzureCliCredential` (বা `DefaultAzureCredential`) ব্যবহার করে, সরাসরি API কী ব্যবস্থাপনার প্রয়োজনীয়তা বিলোপ করে।

## Azure AI Agent Service

Azure AI Agent Service হলো একটি তুলনামূলক আরও πρόσφα নিবিষ্ট সংযোজন, Microsoft Ignite 2024-এ পরিচয় করানো হয়েছে। এটি আরও নমনীয় মডেলগুলোর সাথে AI এজেন্ট ভাগ ও ডিপ্লয় করার সুবিধা দেয়, যেমন সরাসরি ওপেন-সোর্স LLMs যেমন Llama 3, Mistral, এবং Cohere কল করতে পারা।

Azure AI Agent Service শক্তিশালী এন্টারপ্রাইজ সিকিউরিটি মেকানিজম এবং ডেটা স্টোরেজ পদ্ধতি প্রদান করে, যা এটিকে এন্টারপ্রাইজ অ্যাপ্লিকেশনের জন্য উপযুক্ত করে তোলে।

এটি Microsoft Agent Framework-এর সাথে আউট-অফ-দ্যা-বক্স কাজ করে এজেন্ট নির্মাণ ও ডিপ্লয় করার জন্য।

এই সার্ভিসটি বর্তমানে Public Preview-তে আছে এবং এজেন্ট নির্মাণের জন্য Python এবং C# সাপোর্ট করে।

Using the Azure AI Agent Service Python SDK, we can create an agent with a user-defined tool:

```python
import asyncio
from azure.identity import DefaultAzureCredential
from azure.ai.projects import AIProjectClient

# টুল ফাংশন সংজ্ঞায়িত করুন
def get_specials() -> str:
    """Provides a list of specials from the menu."""
    return """
    Special Soup: Clam Chowder
    Special Salad: Cobb Salad
    Special Drink: Chai Tea
    """

def get_item_price(menu_item: str) -> str:
    """Provides the price of the requested menu item."""
    return "$9.99"


async def main() -> None:
    credential = DefaultAzureCredential()
    project_client = AIProjectClient.from_connection_string(
        credential=credential,
        conn_str="your-connection-string",
    )

    agent = project_client.agents.create_agent(
        model="gpt-4o-mini",
        name="Host",
        instructions="Answer questions about the menu.",
        tools=[get_specials, get_item_price],
    )

    thread = project_client.agents.create_thread()

    user_inputs = [
        "Hello",
        "What is the special soup?",
        "How much does that cost?",
        "Thank you",
    ]

    for user_input in user_inputs:
        print(f"# User: '{user_input}'")
        message = project_client.agents.create_message(
            thread_id=thread.id,
            role="user",
            content=user_input,
        )
        run = project_client.agents.create_and_process_run(
            thread_id=thread.id, agent_id=agent.id
        )
        messages = project_client.agents.list_messages(thread_id=thread.id)
        print(f"# Agent: {messages.data[0].content[0].text.value}")


if __name__ == "__main__":
    asyncio.run(main())
```

### মূল ধারণা

Azure AI Agent Service-এর নিম্নলিখিত মূল ধারণাগুলো আছে:

- **Agent**. Azure AI Agent Service Microsoft Foundry-এর সাথে ইন্টিগ্রেট করে। AI Foundry-র মধ্যে, একটি AI Agent একটি "smart" মাইক্রোসার্ভিস হিসেবে কাজ করে যা প্রশ্নের উত্তর দিতে (RAG), কর্ম সম্পাদন করতে, বা সম্পূর্ণভাবে ওয়ার্কফ্লো স্বয়ংক্রিয় করতে ব্যবহার করা যেতে পারে। এটি জেনারেটিভ AI মডেলগুলির শক্তিকে টুলগুলোর সঙ্গে সংযুক্ত করে বাস্তব-জগতের ডেটা সোর্সে অ্যাক্সেস ও ইন্টারঅ্যাক্ট করার সক্ষমতা দেয়। এখানে একটি এজেন্টের উদাহরণ:

    ```python
    agent = project_client.agents.create_agent(
        model="gpt-4o-mini",
        name="my-agent",
        instructions="You are helpful agent",
        tools=code_interpreter.definitions,
        tool_resources=code_interpreter.resources,
    )
    ```

    In this example, an agent is created with the model `gpt-4o-mini`, a name `my-agent`, and instructions `You are helpful agent`. The agent is equipped with tools and resources to perform code interpretation tasks.

- **থ্রেড এবং বার্তা**. থ্রেড আরেকটি গুরুত্বপূর্ণ ধারণা। এটি একটি এজেন্ট এবং একটি ব্যবহারকারীর মধ্যে কথোপকথন বা ইন্টারঅ্যাকশনকে প্রতিনিধিত্ব করে। থ্রেডগুলো কথোপকথনের অগ্রগতি ট্র্যাক করতে, প্রসঙ্গ তথ্য সংরক্ষণ করতে, এবং ইন্টারঅ্যাকশনের অবস্থা পরিচালনা করতে ব্যবহার করা যায়। এখানে একটি থ্রেডের উদাহরণ:

    ```python
    thread = project_client.agents.create_thread()
    message = project_client.agents.create_message(
        thread_id=thread.id,
        role="user",
        content="Could you please create a bar chart for the operating profit using the following data and provide the file to me? Company A: $1.2 million, Company B: $2.5 million, Company C: $3.0 million, Company D: $1.8 million",
    )
    
    # Ask the agent to perform work on the thread
    run = project_client.agents.create_and_process_run(thread_id=thread.id, agent_id=agent.id)
    
    # Fetch and log all messages to see the agent's response
    messages = project_client.agents.list_messages(thread_id=thread.id)
    print(f"Messages: {messages}")
    ```

    In the previous code, a thread is created. Thereafter, a message is sent to the thread. By calling `create_and_process_run`, the agent is asked to perform work on the thread. Finally, the messages are fetched and logged to see the agent's response. The messages indicate the progress of the conversation between the user and the agent. It's also important to understand that the messages can be of different types such as text, image, or file, that is the agents work has resulted in for example an image or a text response for example. As a developer, you can then use this information to further process the response or present it to the user.

- **Microsoft Agent Framework-এর সাথে ইন্টিগ্রেট করে**. Azure AI Agent Service Microsoft Agent Framework-এর সাথে নির্বিঘ্নে কাজ করে, যার মানে আপনি `AzureAIProjectAgentProvider` ব্যবহার করে এজেন্ট তৈরি করে Agent Service-এর মাধ্যমে প্রোডাকশনে ডিপ্লয় করতে পারেন।

**ব্যবহার কেস**: Azure AI Agent Service এমন এন্টারপ্রাইজ অ্যাপ্লিকেশনের জন্য ডিজাইন করা যেখানে সিকিউর, স্কেলেবল, এবং নমনীয় AI এজেন্ট ডিপ্লয়মেন্ট প্রয়োজন।

## এই পদ্ধতিগুলোর মধ্যে পার্থক্য কী?
 
এগুলোতে ওভারল্যাপ আছে বলে মনে হতে পারে, কিন্তু তাদের ডিজাইন, সক্ষমতা, এবং লক্ষ্য ব্যবহারের দিক থেকে কিছু মূল পার্থক্য আছে:
 
- **Microsoft Agent Framework (MAF)**: AI এজেন্ট তৈরির জন্য একটি প্রোডাকশন-রেডি SDK। এটি টুল কলিং, কথোপকথন ম্যানেজমেন্ট, এবং Azure identity ইন্টিগ্রেশনের সাথে এজেন্ট তৈরির জন্য একটি স্ট্রীমলাইনড API প্রদান করে।
- **Azure AI Agent Service**: Agents-এর জন্য Azure Foundry-তে একটি প্ল্যাটফর্ম এবং ডিপ্লয়মেন্ট সার্ভিস। এটি Azure OpenAI, Azure AI Search, Bing Search এবং কোড এক্সিকিউশনের মতো সার্ভিসগুলোর জন্য বিল্ট-ইন কানেকটিভিটি দেয়।
 
এখনো নিশ্চিত না কোনটি বেছে নেবেন?

### ব্যবহারের ক্ষেত্র
 
চলুন কিছু সাধারণ ব্যবহারের কেস দেখে আমরা আপনাকে সাহায্য করতে পারি কিনা দেখি:
 
> Q: আমি প্রোডাকশন AI এজেন্ট অ্যাপ্লিকেশন তৈরি করছি এবং দ্রুত শুরু করতে চাই
>
>
>A: Microsoft Agent Framework একটি চমৎকার পছন্দ। এটি `AzureAIProjectAgentProvider` এর মাধ্যমে একটি সরল, Pythonic API প্রদান করে যা আপনাকে কয়েক লাইনের কোডে টুল এবং নির্দেশনা সহ এজেন্ট নির্ধারণ করতে দেয়।

>Q: আমি এমন একটি এন্টারপ্রাইজ-গ্রেড ডিপ্লয়মেন্ট প্রয়োজন যেখানে Azure ইন্টিগ্রেশন যেমন Search এবং কোড এক্সিকিউশন আছে
>
> A: Azure AI Agent Service সবচেয়ে উপযুক্ত। এটি একটি প্ল্যাটফর্ম সার্ভিস যা একাধিক মডেল, Azure AI Search, Bing Search এবং Azure Functions-এর জন্য বিল্ট-ইন ক্ষমতা প্রদান করে। এটি Foundry Portal-এ আপনার এজেন্ট তৈরি করা এবং স্কেলে ডিপ্লয় করা সহজ করে তোলে।
 
> Q: আমি এখনো বিভ্রান্ত, শুধু একটি অপশন বলুন
>
> A: প্রথমে Microsoft Agent Framework দিয়ে আপনার এজেন্ট তৈরি করা শুরু করুন, এবং যখন প্রোডাকশনে ডিপ্লয় ও স্কেল করতে হবে তখন Azure AI Agent Service ব্যবহার করুন। এই পদ্ধতি আপনাকে দ্রুত এজেন্ট লজিকে পুনরাবৃত্তি করতে দেয় পাশাপাশি এন্টারপ্রাইজ ডিপ্লয়মেন্টের জন্য একটি স্পষ্ট পথ দেয়।
 
চলুন মূল পার্থক্যগুলো একটি টেবিলে সারসংক্ষেপ করি:

| ফ্রেমওয়ার্ক | ফোকাস | মূল ধারণা | ব্যবহারের ক্ষেত্র |
| --- | --- | --- | --- |
| Microsoft Agent Framework | টুল কলিং সহ স্ট্রীমলাইনড এজেন্ট SDK | Agents, Tools, Azure Identity | AI এজেন্ট নির্মাণ, টুল ব্যবহার, বহু-ধাপ ওয়ার্কফ্লো |
| Azure AI Agent Service | নমনীয় মডেল, এন্টারপ্রাইজ সিকিউরিটি, কোড জেনারেশন, টুল কলিং | মডুলারিটি, সহযোগিতা, প্রসেস অর্কেস্ট্রেশন | সিকিউর, স্কেলেবল, এবং নমনীয় AI এজেন্ট ডিপ্লয়মেন্ট |

## আমি কি আমার বিদ্যমান Azure একোসিস্টেম টুলগুলো সরাসরি ইন্টিগ্রেট করতে পারি, নাকি আলাদা স্ট্যান্ডঅ্যালোন সলিউশনের প্রয়োজন?
উত্তর হ্যাঁ — আপনি আপনার বিদ্যমান Azure ইকোসিস্টেমের সরঞ্জামগুলো সরাসরি Azure AI Agent Service-এর সাথে একত্রিত করতে পারেন, বিশেষ করে কারণ এটি অন্যান্য Azure পরিষেবার সাথে নির্বিঘ্নভাবে কাজ করার জন্য তৈরি করা হয়েছে। উদাহরণস্বরূপ, আপনি Bing, Azure AI Search, এবং Azure Functions একত্রিত করতে পারেন। Microsoft Foundry-র সঙ্গেও এর গভীর একত্রীকরণ রয়েছে।

Microsoft Agent Framework এছাড়াও `AzureAIProjectAgentProvider` এবং Azure identity-এর মাধ্যমে Azure পরিষেবার সাথে একত্রীকরণ করে, যাতে আপনার agent টুলগুলো থেকে সরাসরি Azure পরিষেবা কল করতে পারেন।

## নমুনা কোড

- Python: [এজেন্ট ফ্রেমওয়ার্ক](./code_samples/02-python-agent-framework.ipynb)
- .NET: [এজেন্ট ফ্রেমওয়ার্ক](./code_samples/02-dotnet-agent-framework.md)

## AI এজেন্ট ফ্রেমওয়ার্ক সম্পর্কে আরও প্রশ্ন আছে?

যোগ দিন [Microsoft Foundry Discord](https://aka.ms/ai-agents/discord) যাতে আপনি অন্যান্য শিক্ষার্থীদের সাথে দেখা করতে পারেন, অফিস আওয়ারগুলোতে অংশগ্রহণ করতে পারেন এবং আপনার AI এজেন্ট সম্পর্কিত প্রশ্নগুলোর উত্তর পেতে পারেন।

## রেফারেন্স

- <a href="https://techcommunity.microsoft.com/blog/azure-ai-services-blog/introducing-azure-ai-agent-service/4298357" target="_blank">Azure এজেন্ট সার্ভিস</a>
- <a href="https://learn.microsoft.com/azure/ai-services/openai/how-to/responses" target="_blank">Microsoft Agent Framework - Azure OpenAI উত্তরসমূহ</a>
- <a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Azure AI Agent সার্ভিস</a>

## পূর্বের পাঠ

[AI এজেন্ট এবং এজেন্ট ব্যবহারের কেসের পরিচিতি](../01-intro-to-ai-agents/README.md)

## পরবর্তী পাঠ

[এজেন্টিক ডিজাইন প্যাটার্নসমূহ বোঝা](../03-agentic-design-patterns/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
ডিসক্লেইমার:
এই নথিটি এআই অনুবাদ সেবা Co-op Translator (https://github.com/Azure/co-op-translator) ব্যবহার করে অনুবাদ করা হয়েছে। আমরা যতটা সম্ভব সঠিকতা বজায় রাখার চেষ্টা করে থাকি, তবুও অনুগ্রহ করে জেনে রাখুন যে স্বয়ংক্রিয় অনুবাদে ত্রুটি বা বিভ্রান্তি থাকতে পারে। মূল নথিটি তার নিজ ভাষায় প্রামাণিক উৎস হিসেবে বিবেচিত হওয়া উচিত। গুরুত্বপূর্ণ তথ্যের জন্য পেশাদার মানব অনুবাদ গ্রহণ করার পরামর্শ দেওয়া হয়। এই অনুবাদ ব্যবহারের ফলে উদ্ভূত কোনো ভুল বোঝাবুঝি বা ভ্রান্ত ব্যাখ্যার জন্য আমরা দায়ী থাকব না।
<!-- CO-OP TRANSLATOR DISCLAIMER END -->