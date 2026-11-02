[![AI এজেন্ট ফ্রেমওয়ার্ক অনুসন্ধান](../../../translated_images/bn/lesson-2-thumbnail.c65f44c93b8558df.webp)](https://youtu.be/ODwF-EZo_O8?si=1xoy_B9RNQfrYdF7)

> _(এই পাঠের ভিডিও দেখতে উপরের ছবিতে ক্লিক করুন)_

# AI এজেন্ট ফ্রেমওয়ার্ক অনুসন্ধান

AI এজেন্ট ফ্রেমওয়ার্কগুলি সফটওয়্যার প্ল্যাটফর্ম যা AI এজেন্ট তৈরির, স্থাপনের এবং পরিচালনার প্রক্রিয়া সহজ করতে ডিজাইন করা হয়েছে। এই ফ্রেমওয়ার্কগুলি বিকাশকারীদের জন্য আগেই তৈরি উপাদান, বিমূর্ততা এবং সরঞ্জাম প্রদান করে যা জটিল AI সিস্টেমের উন্নয়নকে সরল করে তোলে।

এই ফ্রেমওয়ার্কগুলি বিকাশকারীদের তাদের অ্যাপ্লিকেশনগুলোর অনন্য দিকগুলোতে মনোযোগ দেওয়ার সুযোগ দেয় কারণ তারা AI এজেন্ট উন্নয়নের সাধারণ চ্যালেঞ্জগুলোর জন্য মানকীকৃত পদ্ধতি প্রদান করে। এগুলো স্কেলেবিলিটি, প্রবেশযোগ্যতা এবং দক্ষতা বৃদ্ধি করে AI সিস্টেম তৈরিতে।

## পরিচিতি 

এই পাঠে আলোচনা করা হবে:

- AI এজেন্ট ফ্রেমওয়ার্ক কি এবং এগুলো বিকাশকারীদের কী অর্জন করতে সাহায্য করে?
- দলগুলি কিভাবে এগুলো ব্যবহার করে দ্রুত প্রোটোটাইপ তৈরি, পুনর্বিবেচনা এবং এজেন্টের সক্ষমতা উন্নত করতে পারে?
- Microsoft এর নির্মিত ফ্রেমওয়ার্ক ও সরঞ্জামসমূহের পার্থক্য কি (<a href="https://aka.ms/ai-agents-beginners/ai-agent-service" target="_blank">Microsoft Foundry Agent Service</a> এবং <a href="https://learn.microsoft.com/azure/ai-services/openai/how-to/responses" target="_blank">Microsoft Agent Framework</a>)?
- আমি কি আমার বিদ্যমান Azure ইকোসিস্টেম সরঞ্জামগুলি সরাসরি ইন্টিগ্রেট করতে পারি, নাকি স্বতন্ত্র সমাধানের প্রয়োজন?
- Microsoft Foundry Agent Service কি এবং এটি কীভাবে আমাকে সাহায্য করছে?

## শিক্ষা লক্ষ্য

এই পাঠের লক্ষ্য হল আপনাকে সাহায্য করা:

- AI Agent ফ্রেমওয়ার্কের AI উন্নয়নে ভূমিকা বুঝতে।
- কীভাবে AI এজেন্ট ফ্রেমওয়ার্ক ব্যবহার করে বুদ্ধিমান এজেন্ট তৈরি করা যায়।
- AI এজেন্ট ফ্রেমওয়ার্কের মাধ্যমে সক্ষমতা।
- Microsoft Agent Framework এবং Microsoft Foundry Agent Service এর পার্থক্য।

## AI Agent ফ্রেমওয়ার্ক কি এবং এগুলো বিকাশকারীদের কী করতে দেয়?

প্রচলিত AI Frameworks আপনাকে আপনার অ্যাপ্লিকেশনে AI সংযোজন করে নিম্নলিখিতভাবে এপগুলিকে উন্নত করতে সাহায্য করে:

- **ব্যক্তিগতকরণ**: AI ব্যবহারকারীর আচরণ ও পছন্দ বিশ্লেষণ করে ব্যক্তিগতকৃত সুপারিশ, বিষয়বস্তু এবং অভিজ্ঞতা প্রদান করে।
উদাহরণ: Netflix-এর মত স্ট্রিমিং সেবা AI ব্যবহার করে দর্শন ইতিহাসের ভিত্তিতে সিনেমা ও শো সুপারিশ করে, যা ব্যবহারকারীর আকর্ষণ এবং সন্তুষ্টি বাড়ায়।
- **স্বয়ংক্রিয়তা এবং দক্ষতা**: AI পুনরাবৃত্তিমূলক কাজ স্বয়ংক্রিয়করণ, কর্মপ্রবাহ রূপান্তর এবং অপারেশন দক্ষতা উন্নত করে।
উদাহরণ: গ্রাহক পরিষেবা অ্যাপে AI চালিত চ্যাটবট সাধারণ প্রশ্নের উত্তর দেয়, সাড়া দেওয়ার সময় কমায় এবং জটিল বিষয়ের জন্য মানব এজেন্টদের অবাধ করে।
- **উন্নত ব্যবহারকারীর অভিজ্ঞতা**: AI কণ্ঠস্বর স্বীকৃতি, প্রাকৃতিক ভাষা প্রক্রিয়াকরণ এবং পূর্বাভাসমূলক টেক্সটের মত বুদ্ধিমান বৈশিষ্ট্য সরবরাহ করে সার্বিক ব্যবহারকারীর অভিজ্ঞতা উন্নত করে।
উদাহরণ: Siri ও Google Assistant-এর মত ভার্চুয়াল সহায়ক AI ব্যবহার করে কণ্ঠ কমান্ড বুঝে এবং সাড়া দেয়, ব্যবহারকারীদের ডিভাইসগুলির সাথে সহজ ইন্টারঅ্যাকশন করার সুযোগ দেয়।

### এসব তো ভালো শুনাচ্ছে, তাহলে কেন আমাদের AI Agent Frameworkের প্রয়োজন?

AI Agent ফ্রেমওয়ার্কগুলি কেবল AI ফ্রেমওয়ার্কের চেয়ে বেশি কিছু। এগুলো তৈরি হয়েছে বুদ্ধিমান এজেন্ট তৈরির জন্য যা ব্যবহারকারী, অন্যান্য এজেন্ট এবং পরিবেশের সাথে ইন্টারঅ্যাক্ট করে নির্দিষ্ট লক্ষ্য অর্জন করতে পারে। এই এজেন্টগুলি স্বয়ংক্রিয় আচরণ দেখাতে পারে, সিদ্ধান্ত নিতে পারে এবং পরিবর্তিত পরিস্থিতিতে খাপ খাইয়ে নিতে পারে। আসুন AI Agent ফ্রেমওয়ার্কের দ্বারা সক্রিয় কিছু মূল সক্ষমতা দেখি:

- **এজেন্ট সহযোগিতা ও সমন্বয়**: একাধিক AI এজেন্ট তৈরির সুযোগ দেয় যারা একসাথে কাজ, যোগাযোগ এবং সমন্বয় করে জটিল কাজ সমাধান করতে পারে।
- **কাজ স্বয়ংক্রিয়করণ ও ব্যবস্থাপনা**: বহু ধাপের কর্মপ্রবাহ স্বয়ংক্রিয়করণ, কাজ বরাদ্দ এবং গতিশীল কাজ ব্যবস্থাপনার জন্য পদ্ধতি সরবরাহ করে।
- **প্রাসঙ্গিক বোঝাপড়া এবং খাপ খাওয়ানো**: পরিবেশ বুঝতে, পরিবর্তিত পরিবেশে খাপ খাইয়ে নিতে এবং বাস্তব-সময়ের তথ্য অনুযায়ী সিদ্ধান্ত নিতে সক্ষম করে।

সংক্ষেপে, এজেন্টরা আপনাকে আরো করতে দেয়, স্বয়ংক্রিয়তা উন্নত করতে দেয়, পরিবেশ থেকে খাপ খাইয়ে শিখতে সক্ষম বুদ্ধিমান সিস্টেম তৈরিতে সহায়তা করে।

## কিভাবে দ্রুত প্রোটোটাইপ তৈরি, পুনর্বিবেচনা এবং এজেন্টের সক্ষমতা উন্নত করবেন?

এটি দ্রুত পরিবর্তনশীল ক্ষেত্র, তবে বেশিরভাগ AI Agent ফ্রেমওয়ার্কে কিছু সাধারণ বৈশিষ্ট্য আছে যেমন মডিউলার উপাদান, সহযোগিতামূলক সরঞ্জাম এবং বাস্তব-সময় শিক্ষা যা আপনাকে দ্রুত প্রোটোটাইপ এবং পুনর্বিবেচনা করতে সাহায্য করবে। আসুন এগুলো দেখি:

- **মডিউলার উপাদান ব্যবহার করুন**: AI SDK প্রাক-তৈরি উপাদান যেমন AI ও মেমোরি কানেক্টর, স্বাভাবিক ভাষায় বা কোড প্লাগইন দিয়ে ফাংশন কলিং, প্রম্পট টেমপ্লেট প্রভৃতি সরবরাহ করে।
- **সহযোগিতামূলক সরঞ্জাম নিন**: নির্দিষ্ট ভূমিকা ও কাজ সহ এজেন্ট ডিজাইন করুন, যাতে তারা সহযোগিতামূলক কর্মপ্রবাহ পরীক্ষা ও পরিমার্জন করতে পারে।
- **বাস্তব-সময়ে শিখুন**: এজেন্টদের ইন্টারঅ্যাকশনের মধ্য দিয়ে শেখার এবং গতিশীলভাবে আচরণ সামঞ্জস্য করার জন্য ফিডব্যাক লুপ তৈরি করুন।

### মডিউলার উপাদান ব্যবহার করুন

Microsoft Agent Framework এর মত SDK প্রাক-তৈরি উপাদান যেমন AI কানেক্টর, সরঞ্জাম সংজ্ঞা এবং এজেন্ট ব্যবস্থাপনা দেয়।

**দলগুলি কিভাবে এটি ব্যবহার করতে পারে**: দলগুলো দ্রুত এই উপাদানগুলো একত্রিত করে কার্যকর প্রোটোটাইপ তৈরি করতে পারে, যা দ্রুত পরীক্ষা-নিরীক্ষা এবং পুনর্বিবেচনার সুযোগ দেয়।

**প্রকৃত প্রয়োগে কিভাবে কাজ করে**: আপনি ব্যবহারকারীর ইনপুট থেকে তথ্য বের করতে একটি প্রাক-তৈরি পার্সার, ডেটা সংরক্ষণ ও আহরণের জন্য একটি মেমোরি মডিউল, এবং ব্যবহারকারীর সাথে আলাপচারিতার জন্য একটি প্রম্পট জেনারেটর ব্যবহার করতে পারেন, কোনোটিই নিজে থেকে তৈরি না করেই।

**উদাহরণ কোড**: আসুন দেখি Microsoft Agent Framework কিভাবে `FoundryChatClient` ব্যবহার করে টুল কলিং সহ মডেলকে ব্যবহারকারীর ইনপুটে সাড়া দিতে দেয়:

``` python
# মাইক্রোসফট এজেন্ট ফ্রেমওয়ার্ক পাইথন উদাহরণ

import asyncio
import os

from agent_framework import tool
from agent_framework.foundry import FoundryChatClient
from azure.identity import AzureCliCredential


# ভ্রমণ বুক করার জন্য একটি নমুনা টুল ফাংশন নির্ধারণ করুন
@tool(approval_mode="never_require")
def book_flight(date: str, location: str) -> str:
    """Book travel given location and date."""
    return f"Travel was booked to {location} on {date}"


async def main():
    provider = FoundryChatClient(
        project_endpoint=os.environ["AZURE_AI_PROJECT_ENDPOINT"],
        model=os.environ["AZURE_AI_MODEL_DEPLOYMENT_NAME"],
        credential=AzureCliCredential(),
    )
    agent = provider.as_agent(
        name="travel_agent",
        instructions="Help the user book travel. Use the book_flight tool when ready.",
        tools=[book_flight],
    )

    response = await agent.run("I'd like to go to New York on January 1, 2025")
    print(response)
    # উদাহরণ আউটপুট: ১ জানুয়ারী, ২০২৫ তারিখে আপনার নিউ ইয়র্কের ফ্লাইট সফলভাবে বুক করা হয়েছে। নিরাপদ ভ্রমণ করুন! ✈️🗽


if __name__ == "__main__":
    asyncio.run(main())
```

এই উদাহরণ থেকে আপনি দেখতে পাচ্ছেন কিভাবে একটি প্রাক-তৈরি পার্সার ব্যবহারকারীর ইনপুট থেকে মূল তথ্য যেমন উড়ানের উৎস, গন্তব্য এবং তারিখ বের করার জন্য ব্যবহার করা যায়। এই মডিউলার পদ্ধতি আপনাকে উচ্চ-স্তরের লজিকের উপর ফোকাস করতে সাহায্য করে।

### সহযোগিতামূলক সরঞ্জাম ব্যবহার করুন

Microsoft Agent Framework এর মত ফ্রেমওয়ার্কগুলি একাধিক এজেন্টের সমন্বয়ে কাজ করার সুযোগ দেয়।

**দলগুলি কিভাবে এরা ব্যবহার করতে পারে**: দলগুলো নির্দিষ্ট ভূমিকা ও কাজের সাথে এজেন্ট ডিজাইন করে সহযোগিতামূলক কর্মপ্রবাহ পরীক্ষা ও পরিমার্জন করে সামগ্রিক দক্ষতা উন্নত করতে পারে।

**প্রকৃত প্রয়োগে কিভাবে কাজ করে**: আপনি এমন এক দলের সৃষ্টি করতে পারেন যেখানে প্রতিটি এজেন্টের বিশেষ কার্য থাকে, যেমন তথ্য আহরণ, বিশ্লেষণ বা সিদ্ধান্ত গ্রহণ। এই এজেন্টরা একসাথে যোগাযোগ এবং তথ্য শেয়ার করে একটি সাধারণ লক্ষ্য যেমন ব্যবহারকারীর প্রশ্নের উত্তর দেওয়া বা কাজ সম্পাদন করে।

**উদাহরণ কোড (Microsoft Agent Framework)**:

```python
# মাইক্রোসফট এজেন্ট ফ্রেমওয়ার্ক ব্যবহার করে একাধিক এজেন্ট তৈরি করা যা একসাথে কাজ করে

import os
from agent_framework.foundry import FoundryChatClient
from azure.identity import AzureCliCredential

provider = FoundryChatClient(
    project_endpoint=os.environ["AZURE_AI_PROJECT_ENDPOINT"],
    model=os.environ["AZURE_AI_MODEL_DEPLOYMENT_NAME"],
    credential=AzureCliCredential(),
)

# ডাটা রিট্রিভাল এজেন্ট
agent_retrieve = provider.as_agent(
    name="dataretrieval",
    instructions="Retrieve relevant data using available tools.",
    tools=[retrieve_tool],
)

# ডাটা বিশ্লেষণ এজেন্ট
agent_analyze = provider.as_agent(
    name="dataanalysis",
    instructions="Analyze the retrieved data and provide insights.",
    tools=[analyze_tool],
)

# একটি কাজের উপর এজেন্টগুলি ধারাবাহিকভাবে চালানো
retrieval_result = await agent_retrieve.run("Retrieve sales data for Q4")
analysis_result = await agent_analyze.run(f"Analyze this data: {retrieval_result}")
print(analysis_result)
```

আগের কোডে আপনি দেখতে পাচ্ছেন কিভাবে একাধিক এজেন্টকে নিয়ে কাজ করা একটি কাজ তৈরি করা হয় তথ্য বিশ্লেষণের জন্য। প্রতিটি এজেন্ট একটি নির্দিষ্ট ফাংশন সম্পাদন করে এবং কাজটি সমন্বয়ের মাধ্যমে সম্পন্ন হয়। বিশেষায়িত ভূমিকাসম্পন্ন এজেন্ট তৈরির মাধ্যমে কাজের দক্ষতা ও কর্মক্ষমতা উন্নত হয়।

### বাস্তব-সময়ে শিখুন

উন্নত ফ্রেমওয়ার্কগুলি বাস্তব-সময়ের প্রসঙ্গ বুঝপড়া এবং খাপ খাওয়ানোর ক্ষমতা প্রদান করে।

**দলগুলি কিভাবে এটা ব্যবহার করতে পারে**: দলগুলো ফিডব্যাক লুপ প্রয়োগ করতে পারে যেখানে এজেন্টরা ইন্টারঅ্যাকশন থেকে শেখে এবং গতিশীলভাবে তাদের আচরণ সামঞ্জস্য করে, ধারাবাহিক উন্নতি ও সক্ষমতা পরিমার্জন করে।

**প্রকৃত প্রয়োগে কিভাবে কাজ করে**: এজেন্টরা ব্যবহারকারীর প্রতিক্রিয়া, পরিবেশগত ডেটা এবং কাজের ফলাফল বিশ্লেষণ করে তাদের জ্ঞানভিত্তি হালনাগাদ করে, সিদ্ধান্ত নেবার অ্যালগরিদম সামঞ্জস্য করে এবং সময়ের সাথে পারফরম্যান্স উন্নত করে। এই পুনরাবৃত্তি শেখার প্রক্রিয়া এজেন্টদের পরিবর্তনশীল পরিস্থিতি এবং ব্যবহারকারীর পছন্দ অনুযায়ী খাপ খাইয়ে নিতে সাহায্য করে, সামগ্রিক ব্যবস্থার কার্যকারিতা বাড়ায়।

## Microsoft Agent Framework এবং Microsoft Foundry Agent Service এর পার্থক্য কী?

এই পন্থাগুলোর তুলনা করার অনেক উপায় আছে, কিন্তু আসুন তাদের ডিজাইন, সক্ষমতা এবং লক্ষ্য ব্যবহার কেসের আলোকে কিছু মূল পার্থক্য দেখি:

## Microsoft Agent Framework (MAF)

Microsoft Agent Framework একটি সুসংহত SDK সরবরাহ করে `FoundryChatClient` ব্যবহার করে AI এজেন্ট তৈরি করার জন্য। এটি Azure OpenAI মডেল ব্যবহার করে এজেন্ট তৈরির সুযোগ দেয় যাদের অনুগত টুল কলিং, আলাপচারিতা ব্যবস্থাপনা এবং Azure পরিচয়ের মাধ্যমে এন্টারপ্রাইজ-গ্রেড সুরক্ষা দেয়।

**ব্যবহার ক্ষেত্র**: টুল ব্যবহারের সঙ্গে উৎপাদন-পর্যায়ের AI এজেন্ট তৈরি, বহু-ধাপ কর্মপ্রবাহ এবং এন্টারপ্রাইজ ইন্টিগ্রেশন সিচুয়েশন।

এখানে Microsoft Agent Framework এর কিছু গুরুত্বপূর্ণ মূল ধারণা:

- **এজেন্টস**। একটি এজেন্ট `FoundryChatClient` এর মাধ্যমে তৈরি এবং নাম, নির্দেশনা এবং সরঞ্জাম দ্বারা কনফিগার করা হয়। এজেন্ট করতে পারে:
  - **ব্যবহারকারীর বার্তাগুলো প্রক্রিয়াকরণ** এবং Azure OpenAI মডেল ব্যবহার করে উত্তর তৈরি।
  - **আলাপচারিতার প্রাসঙ্গিক টুল কল** স্বয়ংক্রিয়ভাবে করা।
  - **একাধিক ইন্টারঅ্যাকশনের মধ্য দিয়ে আলাপচারিতা অবস্থা বজায় রাখা**।

  এখানে একটি কোড স্নিপেটে দেখানো হয়েছে কিভাবে এজেন্ট তৈরি করবেন:

    ```python
    import os
    from agent_framework.foundry import FoundryChatClient
    from azure.identity import AzureCliCredential

    provider = FoundryChatClient(
        project_endpoint=os.environ["AZURE_AI_PROJECT_ENDPOINT"],
        model=os.environ["AZURE_AI_MODEL_DEPLOYMENT_NAME"],
        credential=AzureCliCredential(),
    )
    agent = provider.as_agent(
        name="my_agent",
        instructions="You are a helpful assistant.",
    )

    response = await agent.run("Hello, World!")
    print(response)
    ```

- **টুলস**। ফ্রেমওয়ার্ক পায়থনের ফাংশন হিসেবে টুল সংজ্ঞায়িত করার অনুমতি দেয় যা এজেন্ট স্বয়ংক্রিয়ভাবে কল করতে পারে। টুলগুলি এজেন্ট তৈরির সময় নিবন্ধিত হয়:

    ```python
    def get_weather(location: str) -> str:
        """Get the current weather for a location."""
        return f"The weather in {location} is sunny, 72\u00b0F."

    agent = provider.as_agent(
        name="weather_agent",
        instructions="Help users check the weather.",
        tools=[get_weather],
    )
    ```

- **বহু-এজেন্ট সমন্বয়**। আপনি বিভিন্ন দক্ষতাসম্পন্ন একাধিক এজেন্ট তৈরি করে তাদের কাজ সমন্বয় করতে পারেন:

    ```python
    planner = provider.as_agent(
        name="planner",
        instructions="Break down complex tasks into steps.",
    )

    executor = provider.as_agent(
        name="executor",
        instructions="Execute the planned steps using available tools.",
        tools=[execute_tool],
    )

    plan = await planner.run("Plan a trip to Paris")
    result = await executor.run(f"Execute this plan: {plan}")
    ```

- **Azure পরিচয় ইন্টিগ্রেশন**। ফ্রেমওয়ার্ক `AzureCliCredential` (বা `DefaultAzureCredential`) ব্যবহার করে নিরাপদ, কী-রহিত প্রমাণীকরণ, যা API কী পরিচালনার প্রয়োজন দূর করে।

## Microsoft Foundry Agent Service

Microsoft Foundry Agent Service হলো সাম্প্রতিক একটি সেবা, Microsoft Ignite 2024 এ পরিচয় করানো হয়েছে। এটি AI এজেন্ট তৈরি ও স্থাপনের জন্য আরও নমনীয় মডেল প্রদান করে, যেমন Llama 3, Mistral এবং Cohere মত ওপেন-সোর্স LLM সরাসরি কল করার সুযোগ।

Microsoft Foundry Agent Service শক্তিশালী এন্টারপ্রাইজ সুরক্ষা ব্যবস্থা এবং ডেটা সংরক্ষণ পদ্ধতি প্রদান করে, যা এটিকে এন্টারপ্রাইজ অ্যাপ্লিকেশনের জন্য উপযুক্ত করে তোলে। 

এটি Microsoft Agent Framework এর সাথে তৎক্ষণাৎ কাজ করে এজেন্ট তৈরি ও স্থাপনে সাহায্য করে।

এই সেবা বর্তমানে পাবলিক প্রিভিউতে রয়েছে এবং Python ও C# ভাষায় এজেন্ট তৈরি সমর্থন করে।

Microsoft Foundry Agent Service Python SDK ব্যবহার করে আমরা কাস্টম টুলসহ একটি এজেন্ট তৈরি করতে পারি:

```python
import asyncio
from azure.identity import DefaultAzureCredential
from azure.ai.projects import AIProjectClient

# টুল ফাংশনগুলি সংজ্ঞায়িত করুন
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
        model="gpt-5-mini",
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

Microsoft Foundry Agent Service এর মূল ধারণাগুলো:

- **এজেন্ট**। Microsoft Foundry Agent Service Microsoft Foundry এর সাথে ইন্টিগ্রেটেড। Microsoft Foundry-এ AI Agent একটি "স্মার্ট" মাইক্রোসার্ভিস হিসেবে কাজ করে যা প্রশ্নের উত্তর দেয় (RAG), ক্রিয়া করে বা সম্পূর্ণ ورکফ্লো স্বয়ংক্রিয় করে। এটি জেনারেটিভ AI মডেলের শক্তি এবং টুল সমন্বয় করে বাস্তব-জগতের ডেটা সোর্সের সাথে যোগাযোগ করে। এখানে একটি এজেন্টের উদাহরণ:

    ```python
    agent = project_client.agents.create_agent(
        model="gpt-5-mini",
        name="my-agent",
        instructions="You are helpful agent",
        tools=code_interpreter.definitions,
        tool_resources=code_interpreter.resources,
    )
    ```

   এই উদাহরণে, একটি এজেন্ট তৈরি হয়েছে মডেল `gpt-5-mini` দিয়ে, নাম `my-agent` এবং নির্দেশনা `You are helpful agent`। এজেন্টটি কোড ব্যাখ্যার কাজ করার জন্য টুল এবং রিসোর্সসহ সজ্জিত।

- **থ্রেড এবং বার্তা**। থ্রেড আরেকটি গুরুত্বপূর্ণ ধারণা। এটি একটি এজেন্ট ও ব্যবহারকারীর মধ্যে কথোপকথন বা ইন্টারঅ্যাকশন বোঝায়। থ্রেড কথোপকথনের অগ্রগতি ট্র্যাক করা, প্রসঙ্গ তথ্য সংরক্ষণ এবং ইন্টারঅ্যাকশনের অবস্থা পরিচালনার জন্য ব্যবহৃত হয়। এখানে একটি থ্রেডের উদাহরণ:

    ```python
    thread = project_client.agents.create_thread()
    message = project_client.agents.create_message(
        thread_id=thread.id,
        role="user",
        content="Could you please create a bar chart for the operating profit using the following data and provide the file to me? Company A: $1.2 million, Company B: $2.5 million, Company C: $3.0 million, Company D: $1.8 million",
    )
    
    # এজেন্টকে থ্রেডে কাজ করার জন্য বলুন
    run = project_client.agents.create_and_process_run(thread_id=thread.id, agent_id=agent.id)
    
    # এজেন্টের প্রতিক্রিয়া দেখতে সমস্ত বার্তা আনুন এবং লগ করুন
    messages = project_client.agents.list_messages(thread_id=thread.id)
    print(f"Messages: {messages}")
    ```

   আগের কোডে একটি থ্রেড তৈরি করা হয়েছে। এরপর থ্রেডে একটি বার্তা পাঠানো হয়েছে। `create_and_process_run` কল করে এজেন্টকে থ্রেডে কাজ করতে বলা হয়েছে। শেষে বার্তাগুলো নিয়ে লগ করা হয়েছে এজেন্টের প্রতিক্রিয়া দেখতে। বার্তাগুলো নির্দেশ করে কথোপকথনের অগ্রগতি ব্যবহারকারী ও এজেন্টের মধ্যে। এছাড়াও বার্তাগুলো বিভিন্ন ধরনের হতে পারে যেমন টেক্সট, ছবি বা ফাইল, অর্থাৎ এজেন্টের কাজের ফলাফল। একজন বিকাশকারী হিসেবে আপনি এই তথ্য ব্যবহার করে আরও প্রক্রিয়া বা ব্যবহারকারীর কাছে প্রদর্শন করতে পারেন।

- **Microsoft Agent Framework এর সাথে ইন্টিগ্রেটেড**। Microsoft Foundry Agent Service Microsoft Agent Framework এর সাথে নির্বিঘ্নে কাজ করে, অর্থাৎ আপনি `FoundryChatClient` ব্যবহার করে এজেন্ট তৈরি ও Agent Service এর মাধ্যমে উৎপাদনে স্থাপন করতে পারেন।

**ব্যবহার ক্ষেত্র**: Microsoft Foundry Agent Service এমন এন্টারপ্রাইজ অ্যাপ্লিকেশনের জন্য ডিজাইন করা হয়েছে যেখানে নিরাপদ, স্কেলেবল এবং নমনীয় AI এজেন্ট স্থাপনের প্রয়োজন।

## এই পন্থাগুলোর মধ্যে পার্থক্য কী?
 
কিছুটা ওভারল্যাপ থাকলেও, এগুলোর ডিজাইন, সক্ষমতা এবং লক্ষ্য ব্যবহারে কিছু মূল পার্থক্য আছে:
 
- **Microsoft Agent Framework (MAF)**: এটি একটি উৎপাদন-সক্ষম SDK যা AI এজেন্ট তৈরির জন্য। এটি একটি সরল API প্রদান করে এজেন্ট তৈরির জন্য যা টুল কল, আলাপচারিতা ব্যবস্থাপনা এবং Azure পরিচয় সমন্বয় করে।
- **Microsoft Foundry Agent Service**: এটি Microsoft Foundry এর একটি প্ল্যাটফর্ম ও স্থাপনা সেবা। এতে Azure OpenAI, Azure AI Search, Bing Search এবং কোড এক্সিকিউশনের মতো সেবাগুলোর সংযোজন অন্তর্ভুক্ত।
 
এখনও নিশ্চিত নন কোনটি বেছে নেবেন?

### ব্যবহারের ক্ষেত্র
 
চলুন কিছু সাধারণ ব্যবহারের ক্ষেত্রে দেখে নিই যা হয়তো আপনার সাহায্য করবে:
 
> প্রশ্ন: আমি উৎপাদন AI এজেন্ট অ্যাপ্লিকেশন তৈরি করছি এবং দ্রুত শুরু করতে চাই
>

>উত্তর: Microsoft Agent Framework একটি চমৎকার অপশন। এটি সরল, পাইথনভিত্তিক API প্রদান করে `FoundryChatClient` এর মাধ্যমে যা কয়েক লাইনে এজেন্ট টুল ও নির্দেশনা সংজ্ঞায়িত করতে দেয়।

>প্রশ্ন: আমার এন্টারপ্রাইজ-গ্রেড স্থাপনা প্রয়োজন Azure ইন্টিগ্রেশন সহ যেমন সার্চ এবং কোড এক্সিকিউশন
>
>উত্তর: Microsoft Foundry Agent Service সবচেয়ে উপযুক্ত। এটি একটি প্ল্যাটফর্ম সেবা যা বহু মডেল, Azure AI Search, Bing Search এবং Azure Functions এর বিল্ট-ইন সমর্থন দেয়। এটি Foundry Portal এ এজেন্ট তৈরি ও ব্যাপকভাবে স্থাপন সহজ করে।
 
> প্রশ্ন: আমি এখনও বিভ্রান্ত, শুধু একটি অপশন দিন
>
>উত্তর: প্রথমে Microsoft Agent Framework দিয়ে এজেন্ট তৈরি শুরু করুন, এবং যখন উৎপাদনে স্থাপন ও স্কেল করতে হবে তখন Microsoft Foundry Agent Service ব্যবহার করুন। এই পন্থা দ্রুত লজিক পুনর্বিবেচনার সুবিধা দেয় সাথে স্পষ্ট পথে এন্টারপ্রাইজ স্থাপনার জন্য।
 
আসুন মূল পার্থক্য টেবিল আকারে সারাংশ করি:

| ফ্রেমওয়ার্ক | ফোকাস | মূল ধারণা | ব্যবহারের ক্ষেত্র |
| --- | --- | --- | --- |
| Microsoft Agent Framework | সরল এজেন্ট SDK ও টুল কলিং | এজেন্ট, টুলস, Azure পরিচয় | AI এজেন্ট নির্মাণ, টুল ব্যবহারে, বহু-ধাপ কর্মপ্রবাহ |
| Microsoft Foundry Agent Service | নমনীয় মডেল, এন্টারপ্রাইজ সুরক্ষা, কোড জেনারেশন, টুল কলিং | মডুলারিটি, সহযোগিতা, প্রক্রিয়া সমন্বয় | নিরাপদ, স্কেলেবল ও নমনীয় AI এজেন্ট স্থাপনা |

## আমি কি আমার বিদ্যমান Azure ইকোসিস্টেম সরঞ্জাম সরাসরি ইন্টিগ্রেট করতে পারি, নাকি স্বতন্ত্র সমাধানের প্রয়োজন?


উত্তরটি হ্যাঁ, আপনি আপনার বিদ্যমান Azure ইকোসিস্টেম সরঞ্জামগুলি সরাসরি Microsoft Foundry Agent Service এর সাথে একীভূত করতে পারেন, বিশেষ করে এটি অন্যান্য Azure পরিষেবার সাথে নির্বিঘ্নে কাজ করার জন্য তৈরি হয়েছে। উদাহরণস্বরূপ, আপনি Bing, Azure AI Search, এবং Azure Functions একীভূত করতে পারেন। Microsoft Foundry এর সঙ্গেও গভীর একীভূতকরণ রয়েছে।

Microsoft Agent Framework এছাড়াও `FoundryChatClient` এবং Azure পরিচয়ের মাধ্যমে Azure পরিষেবার সাথে একীভূত হয়, যা আপনাকে আপনার এজেন্ট সরঞ্জাম থেকে সরাসরি Azure পরিষেবাগুলি কল করতে দেয়।

## নমুনা কোডসমূহ

- Python: [Agent Framework (Microsoft Foundry)](./code_samples/02-python-agent-framework.ipynb)
- Python: [Agent Framework (Azure OpenAI Responses API)](./code_samples/02-python-agent-framework-azure-openai.ipynb)
- .NET: [Agent Framework](./code_samples/02-dotnet-agent-framework.md)

## AI Agent Framework সম্পর্কে আরও প্রশ্ন আছে?

[Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D) এ যোগ দিন অন্যান্য শিক্ষার্থীদের সাথে দেখা করার জন্য, অফিস আওয়ারসে অংশগ্রহণ করতে এবং আপনার AI এজেন্ট প্রশ্নগুলোর উত্তর পেতে।

## রেফারেন্সসমূহ

- <a href="https://techcommunity.microsoft.com/blog/azure-ai-services-blog/introducing-azure-ai-agent-service/4298357" target="_blank">Azure Agent Service</a>
- <a href="https://learn.microsoft.com/azure/ai-services/openai/how-to/responses" target="_blank">Microsoft Agent Framework - Azure OpenAI Responses</a>
- <a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Microsoft Foundry Agent Service</a>

## আগের পাঠ

[Introduction to AI Agents and Agent Use Cases](../01-intro-to-ai-agents/README.md)

## পরবর্তী পাঠ

[Understanding Agentic Design Patterns](../03-agentic-design-patterns/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**অস্বীকৃতি**:
এই নথিটি AI অনুবাদ পরিষেবা [Co-op Translator](https://github.com/Azure/co-op-translator) ব্যবহার করে অনূদিত হয়েছে। যদিও আমরা শুদ্ধতার জন্য চেষ্টা করি, অনুগ্রহ করে মনে রাখবেন যে স্বয়ংক্রিয় অনুবাদে ত্রুটি বা অসঙ্গতি থাকতে পারে। মূল নথিটি তার স্বভাষায় কর্তৃত্বপূর্ণ উৎস হিসেবে বিবেচিত হওয়া উচিত। গুরুত্বপূর্ণ তথ্যের জন্য পেশাদার মানব অনুবাদ সুপারিশ করা হয়। এই অনুবাদের ব্যবহারে প্রয়োজনীয় ভুল বোঝাবুঝি বা ভুল ব্যাখ্যার জন্য আমরা দায়বদ্ধ নই।
<!-- CO-OP TRANSLATOR DISCLAIMER END -->