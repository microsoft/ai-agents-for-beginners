[![AI এজেন্ট ফ্রেমওয়ার্ক অন্বেষণ](../../../translated_images/bn/lesson-2-thumbnail.c65f44c93b8558df.webp)](https://youtu.be/ODwF-EZo_O8?si=1xoy_B9RNQfrYdF7)

> _(উপরের ছবিতে ক্লিক করে এই পাঠের ভিডিও দেখুন)_

# AI এজেন্ট ফ্রেমওয়ার্ক অন্বেষণ

AI এজেন্ট ফ্রেমওয়ার্কগুলো এমন সফটওয়্যার প্ল্যাটফর্ম যা AI এজেন্ট তৈরি, ডিপ্লয়মেন্ট এবং ব্যবস্থাপনা সহজ করে দেয়। এই ফ্রেমওয়ার্কগুলো ডেভেলপারদের প্রি-বিল্ট উপাদান, বিমূর্ততা, এবং টুল প্রদান করে যা জটিল AI সিস্টেমের উন্নয়নকে সরল করে তোলে।

এই ফ্রেমওয়ার্কগুলো ডেভেলপারদের তাদের অ্যাপ্লিকেশনগুলোর অনন্য দিকগুলোর উপর ফোকাস করতে সাহায্য করে, সাধারণ AI এজেন্ট উন্নয়নের চ্যালেঞ্জগুলোর জন্য মানক পদ্ধতি প্রদান করে। এগুলো স্কেলেবিলিটি, অ্যাক্সেসিবিলিটি, এবং দক্ষতা বাড়ায় AI সিস্টেম তৈরিতে।

## পরিচিতি 

এই পাঠে কভার করা হবে:

- AI এজেন্ট ফ্রেমওয়ার্কগুলি কী এবং এগুলো ডেভেলপারদের কী অর্জন করতে সক্ষম করে?
- দলগুলো কীভাবে এগুলো ব্যবহার করে দ্রুত প্রোটোটাইপ তৈরি, পুনরাবৃত্তি, এবং তাদের এজেন্টের সক্ষমতাগুলো উন্নত করতে পারে?
- Microsoft দ্বারা তৈরি ফ্রেমওয়ার্ক এবং টুলগুলোর মধ্যে পার্থক্যগুলো কী (<a href="https://aka.ms/ai-agents-beginners/ai-agent-service" target="_blank">Azure AI Agent Service</a> এবং <a href="https://learn.microsoft.com/azure/ai-services/openai/how-to/responses" target="_blank">Microsoft Agent Framework</a>)?
- আমি কি আমার বিদ্যমান Azure ইকোসিস্টেম টুলগুলো সরাসরি ইন্টিগ্রেট করতে পারি, নাকি আলাদা সলিউশন প্রয়োজন?
- Azure AI Agents service কী এবং এটি কীভাবে সাহায্য করছে?

## শেখার লক্ষ্যসমুহ

এই পাঠের লক্ষ্যগুলো হল আপনাকে বোঝানো:

- AI উন্নয়নে AI এজেন্ট ফ্রেমওয়ার্কগুলোর ভূমিকা।
- কীভাবে AI এজেন্ট ফ্রেমওয়ার্ক ব্যবহার করে জ্ঞানসম্পন্ন এজেন্ট তৈরি করা যায়।
- AI এজেন্ট ফ্রেমওয়ার্ক দ্বারা সক্রিয় করা মূল সক্ষমতাসমূহ।
- Microsoft Agent Framework এবং Azure AI Agent Service-এর মধ্যে পার্থক্য।

## AI এজেন্ট ফ্রেমওয়ার্কগুলো কী এবং এগুলো ডেভেলপারদের কী করতে সক্ষম করে?

পরম্পরাগত AI ফ্রেমওয়ার্কগুলো আপনার অ্যাপ্লিকেশনগুলোর সাথে AI একীভূত করতে এবং নিচের উপায়গুলোতে এগুলোকে আরও ভাল করতে সাহায্য করতে পারে:

- **ব্যক্তিগতকরণ**: AI ব্যবহারকারীর আচরণ এবং পছন্দ বিশ্লেষণ করে ব্যক্তিগতকৃত সুপারিশ, কন্টেন্ট, এবং অভিজ্ঞতা প্রদান করতে পারে।
উদাহরণ: Netflix-এর মতো স্ট্রিমিং সার্ভিসগুলো AI ব্যবহার করে দেখতে থাকা ইতিহাসের ওপর ভিত্তি করে সিনেমা ও শো প্রস্তাব করে, যা ব্যবহারকারীর অংশগ্রহণ এবং সন্তুষ্টি বাড়ায়।
- **স্বয়ংক্রিয়তা এবং দক্ষতা**: AI পুনরাবৃত্তিমূলক কাজগুলো স্বয়ংক্রিয় করতে, ওয়ার্কফ্লো সরল করতে, এবং অপারেশনাল দক্ষতা বাড়াতে পারে।
উদাহরণ: কাস্টমার সার্ভিস অ্যাপগুলো AI-চালিত চ্যাটবট ব্যবহার করে সাধারণ ইনকোয়েরিগুলো মোকাবেলা করে, প্রতিক্রিয়া সময় কমায় এবং জটিল সমস্যার জন্য মানব এজেন্টদের মুক্ত রাখে।
- **উন্নত ব্যবহারকারী অভিজ্ঞতা**: AI কণ্ঠ স্বীকৃতি, প্রাকৃতিক ভাষা প্রক্রিয়াকরণ, এবং প্রেডিকটিভ টেক্সটের মতো বুদ্ধিমান বৈশিষ্ট্য দিয়ে সার্বিক ব্যবহারকারী অভিজ্ঞতা উন্নত করতে পারে।
উদাহরণ: Siri এবং Google Assistant-এর মতো ভারচুয়াল সহকারীরা কণ্ঠ আদেশ বুঝতে এবং সাড়া দিতে AI ব্যবহার করে, যা ব্যবহারকারীদের ডিভাইসের সাথে ইন্টারঅ্যাকশন সহজ করে তোলে।

### সবকিছু চমৎকার শোনাচ্ছে, তাহলে কেন AI Agent Framework দরকার?

AI এজেন্ট ফ্রেমওয়ার্কগুলি কেবল AI ফ্রেমওয়ার্কের চেয়েও কিছু বেশি উপস্থাপন করে। এগুলো ইন্টেলিজেন্ট এজেন্ট তৈরির জন্য ডিজাইন করা হয়েছে যা ব্যবহারকারীর সাথে, অন্যান্য এজেন্টের সাথে এবং পরিবেশের সাথে ইন্টারঅ্যাক্ট করে নির্দিষ্ট লক্ষ্য অর্জন করতে পারে। এই এজেন্টগুলো স্বায়ত্তশাসিত আচরণ প্রদর্শন করতে পারে, সিদ্ধান্ত নিতে পারে, এবং পরিবর্তিত পরিস্থিতিতে অভিযোজিত হতে পারে। চলুন AI এজেন্ট ফ্রেমওয়ার্ক দ্বারা সক্ষম করা কিছু মূল সক্ষমতা দেখি:

- **এজেন্ট সহযোগিতা ও সমন্বয়**: একাধিক AI এজেন্ট তৈরি করার সক্ষমতা যা একসাথে কাজ করতে, যোগাযোগ করতে, এবং জটিল কাজ সমাধান করতে সমন্বয় করতে পারে।
- **টাস্ক অটোমেশন এবং ব্যবস্থাপনা**: বহু-ধাপ ওয়ার্কফ্লো স্বয়ংক্রিয় করা, টাস্ক ডেলিগেশন, এবং এজেন্টদের মধ্যে ডাইনামিক টাস্ক ব্যবস্থাপনার মেকানিজম প্রদান করে।
- **প্রাসঙ্গিক বোঝাপড়া এবং অভিযোজন**: এজেন্টদের প্রাসঙ্গিকতা বুঝতে, পরিবর্তিত পরিবেশে অভিযোজিত হতে, এবং রিয়েল-টাইম তথ্যের ভিত্তিতে সিদ্ধান্ত নিতে সক্ষম করে।

সংক্ষেপে, এজেন্টগুলো আপনাকে আরো বেশি করতে দেয়, অটোমেশনকে পরবর্তী স্তরে নেয়, এবং এমন বুদ্ধিমান সিস্টেম তৈরি করতে দেয় যা তাদের পরিবেশ থেকে অভিযোজিত এবং শিখতে পারে।

## কীভাবে দ্রুত প্রোটোটাইপ করা, পুনরাবৃত্তি করা, এবং এজেন্টের সক্ষমতাগুলো উন্নত করা যায়?

এটি একটি দ্রুত পরিবর্তনশীল ল্যান্ডস্কেপ, তবে বেশিরভাগ AI এজেন্ট ফ্রেমওয়ার্কে কিছু সাধারণ বিষয় আছে যা আপনাকে দ্রুত প্রোটোটাইপ এবং পুনরাবৃত্তি করতে সাহায্য করে যেমন মডিউলার কম্পোনেন্ট, সহযোগিতামূলক টুল, এবং রিয়েল-টাইম লার্নিং। চলুন এগুলোতে বিস্তারিত দেখি:

- **মডিউলার কম্পোনেন্ট ব্যবহার করুন**: AI SDK গুলো প্রি-বিল্ট উপাদান যেমন AI এবং মেমরি কানেক্টর, ন্যাচারাল ল্যাঙ্গুয়েজ বা কোড প্লাগইন ব্যবহার করে ফাংশন কল করা, প্রম্পট টেমপ্লেট ইত্যাদি প্রদান করে।
- **সহযোগিতামূলক টুলগুলো ব্যবহার করুন**: নির্দিষ্ট ভূমিকা ও টাস্ক সহ এজেন্ট ডিজাইন করুন, যাতে তারা সহযোগিতামূলক ওয়ার্কফ্লো পরীক্ষা ও পরিমার্জন করতে পারে।
- **রিয়েল-টাইমে শেখা**: এমন ফিডব্যাক লুপ বাস্তবায়ন করুন যেখানে এজেন্টরা ইন্টারঅ্যাকশনের মাধ্যমে শিখে এবং তাদের আচরণ ডাইনামিকভাবে সামঞ্জস্য করে।

### মডিউলার কম্পোনেন্ট ব্যবহার করুন

Microsoft Agent Framework-এর মতো SDK গুলো প্রি-বিল্ট কম্পোনেন্ট প্রদান করে যেমন AI কানেক্টর, টুল ডেফিনিশন, এবং এজেন্ট ম্যানেজমেন্ট।

**দলগুলো এটি কীভাবে ব্যবহার করতে পারে**: দলগুলো এই উপাদানগুলো দ্রুত একত্র করে একটি কার্যকরী প্রোটোটাইপ তৈরি করতে পারে बिना শূন্য থেকে শুরু করার, যা দ্রুত পরীক্ষণ এবং পুনরাবৃত্তির সুযোগ দেয়।

**বাস্তবে এটি কীভাবে কাজ করে**: আপনি ব্যবহারকারীর ইনপুট থেকে তথ্য বের করতে একটি প্রি-বিল্ট পার্সার ব্যবহার করতে পারেন, ডেটা সংরক্ষণ ও পুনরুদ্ধারের জন্য একটি মেমরি মডিউল ব্যবহার করতে পারেন, এবং ব্যবহারকারীর সাথে ইন্টারঅ্যাকশনের জন্য একটি প্রম্পট জেনারেটর ব্যবহার করতে পারেন, সবকিছুই শূন্য থেকে কম্পোনেন্ট তৈরি না করেই করা যায়।

**উদাহরণ কোড**. চলুন একটি উদাহরণ দেখি কিভাবে আপনি Microsoft Agent Framework `AzureAIProjectAgentProvider` ব্যবহার করে মডেলটিকে টুল কলিং সহ ব্যবহারকারীর ইনপুটে সাড়া দিতে পারেন:

``` python
# Microsoft Agent Framework পাইথন উদাহরণ

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
    # উদাহরণ আউটপুট: আপনার ১ জানুয়ারি, ২০২৫ তারিখের নিউ ইয়র্কের ফ্লাইট সফলভাবে বুক করা হয়েছে। নিরাপদ ভ্রমণ! ✈️🗽


if __name__ == "__main__":
    asyncio.run(main())
```

এই উদাহরণ থেকে আপনি দেখতে পারবেন কিভাবে একটি প্রি-বিল্ট পার্সার ব্যবহার করে ব্যবহারকারীর ইনপুট থেকে মূল তথ্য যেমন উত্স, গন্তব্য, এবং ফ্লাইট বুকিং অনুরোধের তারিখ বের করা যায়। এই মডিউলার পদ্ধতি আপনাকে উচ্চ-স্তরের লজিকের উপর ফোকাস করতে দেয়।

### সহযোগিতামূলক টুলগুলো ব্যবহার করুন

Microsoft Agent Framework-এর মতো ফ্রেমওয়ার্কগুলো একাধিক এজেন্ট তৈরি করতে সুবিধা করে দেয় যা একসাথে কাজ করতে পারে।

**দলগুলো এটি কীভাবে ব্যবহার করতে পারে**: দলগুলো নির্দিষ্ট ভূমিকা এবং টাস্ক সহ এজেন্ট ডিজাইন করতে পারে, যাতে তারা সহযোগিতামূলক ওয়ার্কফ্লো পরীক্ষা ও পরিমার্জন করতে পারে এবং সামগ্রিক সিস্টেম দক্ষতা উন্নত করতে পারে।

**বাস্তবে এটি কীভাবে কাজ করে**: আপনি এমন একটি এজেন্ট টিম তৈরি করতে পারেন যেখানে প্রতিটি এজেন্টের একটি বিশেষায়িত ফাংশন থাকে, যেমন ডাটা রিট্রিভাল, বিশ্লেষণ, বা সিদ্ধান্ত গ্রহণ। এই এজেন্টগুলো যোগাযোগ করে ও তথ্য শেয়ার করে একটি সাধারণ লক্ষ্য অর্জন করতে পারে, যেমন একটি ব্যবহারকারীর প্রশ্নের উত্তর দেওয়া বা একটি টাস্ক সম্পন্ন করা।

**উদাহরণ কোড (Microsoft Agent Framework)**:

```python
# মাইক্রোসফট এজেন্ট ফ্রেমওয়ার্ক ব্যবহার করে একাধিক এজেন্ট তৈরি করা যারা একসাথে কাজ করে

import os
from agent_framework.azure import AzureAIProjectAgentProvider
from azure.identity import AzureCliCredential

provider = AzureAIProjectAgentProvider(credential=AzureCliCredential())

# ডেটা উদ্ধার এজেন্ট
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

# একটি কাজের উপর এজেন্টগুলো ক্রমান্বয়ে চালানো
retrieval_result = await agent_retrieve.run("Retrieve sales data for Q4")
analysis_result = await agent_analyze.run(f"Analyze this data: {retrieval_result}")
print(analysis_result)
```

আগের কোডে আপনি দেখতে পাবেন কিভাবে আপনি একাধিক এজেন্টকে নিয়ে একটি টাস্ক তৈরি করতে পারেন যা ডেটা বিশ্লেষণে মিলিতভাবে কাজ করে। প্রতিটি এজেন্ট একটি নির্দিষ্ট ফাংশন সম্পাদন করে, এবং টাস্কটি এজেন্টদের সমন্বয়ের মাধ্যমে সম্পন্ন করা হয়। বিশেষায়িত ভূমিকা সহ ডেডিকেটেড এজেন্ট তৈরি করে আপনি টাস্ক দক্ষতা এবং কর্মদক্ষতা বৃদ্ধি করতে পারেন।

### রিয়েল-টাইমে শেখা

উন্নত ফ্রেমওয়ার্কগুলো রিয়েল-টাইম কনটেক্সট বোঝার এবং অভিযোজনের ক্ষমতা প্রদান করে।

**দলগুলো এটি কীভাবে ব্যবহার করতে পারে**: দলগুলো এমন ফিডব্যাক লুপ বাস্তবায়ন করতে পারে যেখানে এজেন্টরা ইন্টারঅ্যাকশনের থেকে শেখে এবং তাদের আচরণ ডাইনামিকভাবে সামঞ্জস্য করে, ফলে সক্ষমতার ধারাবাহিক উন্নতি এবং পরিমার্জন ঘটে।

**বাস্তবে এটি কীভাবে কাজ করে**: এজেন্টরা ব্যবহারকারীর প্রতিক্রিয়া, পরিবেশগত ডেটা, এবং টাস্ক ফলাফল বিশ্লেষণ করে তাদের নলেজ বেস আপডেট করতে পারে, সিদ্ধান্ত গ্রহণের অ্যালগরিদম সামঞ্জস্য করতে পারে, এবং সময়ের সঙ্গে পারফরম্যান্স উন্নত করতে পারে। এই পুনরাবৃত্তিমূলক শিখন প্রক্রিয়া এজেন্টদের পরিবর্তিত অবস্থার এবং ব্যবহারকারীর পছন্দের সাথে অভিযোজিত হতে সক্ষম করে, ফলে সামগ্রিক সিস্টেম কার্যকারিতা বাড়ে।

## Microsoft Agent Framework এবং Azure AI Agent Service-এর মধ্যে পার্থক্যগুলো কী?

এই পদ্ধতিগুলো তুলনা করার অনেক উপায় আছে, কিন্তু চলুন তাদের ডিজাইন, সক্ষমতা, এবং লক্ষ্য ব্যবহারকাণ্ডের দিক থেকে কিছু মূল পার্থক্য দেখি:

## Microsoft Agent Framework (MAF)

Microsoft Agent Framework একটি সরলীকৃত SDK প্রদান করে AI এজেন্ট তৈরির জন্য `AzureAIProjectAgentProvider` ব্যবহার করে। এটি ডেভেলপারদের এমন এজেন্ট তৈরি করতে সক্ষম করে যা Azure OpenAI মডেল ব্যবহার করে বিল্ট-ইন টুল কলিং, কনভারসেশন ম্যানেজমেন্ট, এবং Azure identity-এর মাধ্যমে এন্টারপ্রাইজ-গ্রেড সিকিউরিটি প্রদান করে।

**ব্যবহারকাণ্ড**: টুল ব্যবহার, বহু-ধাপ ওয়ার্কফ্লো, এবং এন্টারপ্রাইজ ইন্টিগ্রেশন সценারিও নিয়ে প্রোডাকশন-রেডি AI এজেন্ট নির্মাণ করা।

Microsoft Agent Framework-এর কিছু গুরুত্বপূর্ণ মূল ধারণা নীচে দেওয়া হলো:

- **Agents**. একটি এজেন্ট `AzureAIProjectAgentProvider` দিয়ে তৈরি হয় এবং একটি নাম, নির্দেশাবলী, এবং টুল দিয়ে কনফিগার করা হয়। এজেন্টสามารถ:
  - **ব্যবহারকারীর মেসেজ প্রক্রিয়াকরণ** এবং Azure OpenAI মডেল ব্যবহার করে সাড়া জেনারেট করতে পারে।
  - **টুল কল** স্বয়ংক্রিয়ভাবে বিবেচনার প্রাসঙ্গিকতার ওপর ভিত্তি করে করতে পারে।
  - **মাল্টিপল ইন্টারঅ্যাকশনের জুড়ে কনভারসেশন স্টেট বজায় রাখতে** পারে।

  এখানে একটি কোড স্নিপেট দেখানো হয়েছে কিভাবে একটি এজেন্ট তৈরি করা যায়:

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

- **Tools**. ফ্রেমওয়ার্কটি টুলগুলোকে Python ফাংশনের মতো ডেফাইন করার সমর্থন দেয় যা এজেন্ট স্বয়ংক্রিয়ভাবে কল করতে পারে। এজেন্ট তৈরির সময় টুলগুলো রেজিস্টার করা হয়:

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

- **মাল্টি-এজেন্ট সমন্বয়**. আপনি বিভিন্ন বিশেষায়নসহ একাধিক এজেন্ট তৈরি করতে পারেন এবং তাদের কাজ সমন্বয় করতে পারেন:

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

- **Azure Identity Integration**. ফ্রেমওয়ার্কটি `AzureCliCredential` (বা `DefaultAzureCredential`) ব্যবহার করে নিরাপদ, কীলেস অথেন্টিকেশন প্রদান করে, সরাসরি API কী ম্যানেজ করার প্রয়োজন দূর করে।

## Azure AI Agent Service

Azure AI Agent Service একটি সাম্প্রতিক সংযোজন, Microsoft Ignite 2024-এ পরিচিত করানো হয়েছে। এটি এজেন্টদের সাথে উন্নয়ন ও ডিপ্লয়মেন্টের জন্য আরও নমনীয় মডেলগুলোর সমর্থন দেয়, যেমন সরাসরি ওপেন-সোর্স LLMs যেমন Llama 3, Mistral, এবং Cohere কল করা।

Azure AI Agent Service শক্তিশালী এন্টারপ্রাইজ সিকিউরিটি মেকানিজম এবং ডেটা স্টোরেজ পদ্ধতি প্রদান করে, যা এটিকে এন্টারপ্রাইজ অ্যাপ্লিকেশনগুলোর জন্য উপযোগী করে তোলে।

এটি Microsoft Agent Framework-র সাথে আউট-অফ-দ্য-বক্স কাজ করে এজেন্ট তৈরি ও ডিপ্লয় করার জন্য।

এই সার্ভিসটি বর্তমানে Public Preview-তে রয়েছে এবং এজেন্ট বানানোর জন্য Python ও C# সমর্থন করে।

Azure AI Agent Service Python SDK ব্যবহার করে, আমরা একটি ব্যবহারকারী-নির্ধারিত টুল সহ একটি এজেন্ট তৈরি করতে পারি:

```python
import asyncio
from azure.identity import DefaultAzureCredential
from azure.ai.projects import AIProjectClient

# টুল ফাংশনগুলি নির্ধারণ করুন
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

### মূল ধারণাসমূহ

Azure AI Agent Service-এর নিম্নলিখিত মূল ধারণাসমূহ আছে:

- **Agent**. Azure AI Agent Service Microsoft Foundry-এর সাথে একীভূত। AI Foundry-র মধ্যে, একটি AI Agent একটি "স্মার্ট" মাইক্রোসার্ভিস হিসেবে কাজ করে যা প্রশ্নের উত্তর দিতে (RAG), কাজ সম্পন্ন করতে, বা পুরোপুরি ওয়ার্কফ্লো অটোমেট করতে ব্যবহার করা যায়। এটি জেনারেটিভ AI মডেলগুলোর ক্ষমতাকে টুলগুলোর সাথে মিলিয়ে বাস্তব-জগতের ডেটা সোর্সে অ্যাক্সেস এবং ইন্টারঅ্যাকশন সক্ষম করে। এখানে একটি এজেন্টের উদাহরণ:

    ```python
    agent = project_client.agents.create_agent(
        model="gpt-4o-mini",
        name="my-agent",
        instructions="You are helpful agent",
        tools=code_interpreter.definitions,
        tool_resources=code_interpreter.resources,
    )
    ```

    এই উদাহরণে, একটি এজেন্ট `gpt-4o-mini` মডেল দিয়ে তৈরি করা হয়েছে, একটি নাম `my-agent`, এবং নির্দেশাবলী `You are helpful agent`। এজেন্টটি কোড ইন্টারপ্রিটেশন টাস্কগুলি সম্পাদন করার জন্য টুল এবং রিসোর্স নিয়ে সজ্জিত করা হয়েছে।

- **Thread and messages**. থ্রেড একটি গুরুত্বপূর্ণ ধারণা। এটি একটি এজেন্ট এবং ব্যবহারকারীর মধ্যে একটি কথোপকথন বা ইন্টারঅ্যাকশনকে প্রতিনিধিত্ব করে। থ্রেডগুলো কথোপকথনের অগ্রগতি ট্র্যাক করতে, কনটেক্সট তথ্য সংরক্ষণ করতে, এবং ইন্টারঅ্যাকশনের স্টেট ম্যানেজ করতে ব্যবহার করা যেতে পারে। এখানে একটি থ্রেডের উদাহরণ:

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

    আগের কোডে, একটি থ্রেড তৈরি করা হয়েছে। এরপর, থ্রেডে একটি মেসেজ পাঠানো হয়েছে। `create_and_process_run` কল করে, এজেন্টকে থ্রেডে কাজ করতে বলা হয়েছে। শেষ পর্যন্ত, মেসেজগুলো ফেচ করে লগ করা হয়েছে যাতে এজেন্টের প্রতিক্রিয়া দেখা যায়। মেসেজগুলো কথোপকথনের অগ্রগতি নির্দেশ করে যা ব্যবহারকারী এবং এজেন্টের মধ্যে ঘটে। এটি বোঝাও গুরুত্বপূর্ণ যে মেসেজগুলো বিভিন্ন ধরনের হতে পারে যেমন টেক্সট, ছবি, বা ফাইল — অর্থাৎ এজেন্টের কাজের ফলাফল হিসেবে একটি ছবি বা টেক্সট প্রতিক্রিয়া হতে পারে। একজন ডেভেলপার হিসেবে, আপনি এগুলো ব্যবহার করে প্রতিক্রিয়াটি আরও প্রক্রিয়াজাত করতে বা ব্যবহারকারীর কাছে উপস্থাপন করতে পারেন।

- **Microsoft Agent Framework- এর সাথে ইন্টিগ্রেশন**. Azure AI Agent Service Microsoft Agent Framework-এর সাথে নির্বিঘ্নে কাজ করে, যার মানে আপনি `AzureAIProjectAgentProvider` ব্যবহার করে এজেন্ট তৈরি করতে পারেন এবং প্রোডাকশনের জন্য Agent Service-এ ডিপ্লয় করতে পারেন।

**ব্যবহারকাণ্ড**: Azure AI Agent Service এমন এন্টারপ্রাইজ অ্যাপ্লিকেশনগুলোর জন্য ডিজাইন করা হয়েছে যেগুলো নিরাপদ, স্কেলেবল, এবং নমনীয় AI এজেন্ট ডিপ্লয়মেন্টের প্রয়োজন।

## এই পদ্ধতিগুলোর মধ্যে পার্থক্য কী?
 
এটা মনে হতে পারে যে ওভারল্যাপ আছে, কিন্তু তাদের ডিজাইন, সক্ষমতা, এবং লক্ষ্য ব্যবহারকাণ্ডের দিক থেকে কিছু মূল পার্থক্য আছে:
 
- **Microsoft Agent Framework (MAF)**: এজেন্ট তৈরি করার জন্য একটি প্রোডাকশন-রেডি SDK। এটি টুল কলিং, কনভারসেশন ম্যানেজমেন্ট, এবং Azure identity ইন্টিগ্রেশনের জন্য একটি সরলীকৃত API প্রদান করে।
- **Azure AI Agent Service**: এটি Azure Foundry-তে একটি প্ল্যাটফর্ম এবং ডিপ্লয়মেন্ট সার্ভিস। এটি Azure OpenAI, Azure AI Search, Bing Search এবং কোড এক্সিকিউশনের মতো সার্ভিসগুলোর সাথে বিল্ট-ইন কানেক্টিভিটি প্রদান করে।
 
এখনো নিশ্চিত নন কোনটি বেছে নেবেন?

### ব্যবহারকাণ্ডসমূহ
 
চলুন কিছু সাধারণ ব্যবহারকাণ্ড দেখে আপনাকে সাহায্য করার চেষ্টা করি:
 
> Q: আমি প্রোডাকশন AI এজেন্ট অ্যাপ্লিকেশন নির্মাণ করছি এবং দ্রুত শুরু করতে চাই
>

>A: Microsoft Agent Framework একটি চমৎকার পছন্দ। এটি `AzureAIProjectAgentProvider`-এর মাধ্যমে একটি সহজ, Pythonic API প্রদান করে যা কয়েক লাইনে টুল এবং নির্দেশাবলী সহ এজেন্ট সংজ্ঞায়িত করতে দেয়।

>Q: আমি Azure-এর মতো ইন্টিগ্রেশন, যেমন Search এবং কোড এক্সিকিউশন সহ এন্টারপ্রাইজ-গ্রেড ডিপ্লয়মেন্ট চাই
>
> A: Azure AI Agent Service শ্রেষ্ঠ উপযুক্ত। এটি একটি প্ল্যাটফর্ম সার্ভিস যা বহু মডেল, Azure AI Search, Bing Search এবং Azure Functions-এর জন্য বিল্ট-ইন সক্ষমতা প্রদান করে। Foundry Portal-এ আপনার এজেন্টগুলি তৈরি করা এবং স্কেলে ডিপ্লয় করা সহজ করে তোলে।
 
> Q: আমি এখনও বিভ্রান্ত, কেবল একটি অপশন বলুন
>
> A: প্রথমে Microsoft Agent Framework দিয়ে আপনার এজেন্ট তৈরি শুরু করুন, এবং যখন প্রোডাকশনে ডিপ্লয় ও স্কেল করার প্রয়োজন হবে তখন Azure AI Agent Service ব্যবহার করুন। এই পদ্ধতি আপনাকে এজেন্ট লজিকে দ্রুত পুনরাবৃত্তি করার সুযোগ দেয় এবং এন্টারপ্রাইজ ডিপ্লয়মেন্টের জন্য একটি পরিষ্কার পথ প্রদান করে।
 
চলুন টেবিলটিতে মূল পার্থক্যগুলো সারসংক্ষেপ করি:

| Framework | Focus | Core Concepts | Use Cases |
| --- | --- | --- | --- |
| Microsoft Agent Framework | টুল কলিং সহ স্ট্রিমলাইন করা এজেন্ট SDK | Agents, Tools, Azure Identity | AI এজেন্ট নির্মাণ, টুল ব্যবহার, বহু-ধাপ ওয়ার্কফ্লো |
| Azure AI Agent Service | নমনীয় মডেল, এন্টারপ্রাইজ সিকিউরিটি, কোড জেনারেশন, টুল কলিং | Modularity, Collaboration, Process Orchestration | নিরাপদ, স্কেলযোগ্য, এবং নমনীয় AI এজেন্ট ডিপ্লয়মেন্ট |

## আমি কি আমার বিদ্যমান Azure ইকোসিস্টেম টুলগুলো সরাসরি ইন্টিগ্রেট করতে পারি, নাকি আলাদা সলিউশন প্রয়োজন?
উত্তর হলো হ্যাঁ — আপনি আপনার বিদ্যমান Azure ইকোসিস্টেম টুলগুলো সরাসরি Azure AI Agent Service-এ একীকরণ করতে পারেন, বিশেষত কারণ এটি অন্যান্য Azure পরিষেবার সাথে নির্বিঘ্নে কাজ করার জন্য তৈরি করা হয়েছে। উদাহরণস্বরূপ আপনি Bing, Azure AI Search, এবং Azure Functions একীভূত করতে পারেন। Microsoft Foundry-র সঙ্গেও গভীর একীকরণ রয়েছে।

The Microsoft Agent Framework also integrates with Azure services through `AzureAIProjectAgentProvider` and Azure identity, letting you call Azure services directly from your agent tools.

## নমুনা কোড

- Python: [এজেন্ট ফ্রেমওয়ার্ক](./code_samples/02-python-agent-framework.ipynb)
- .NET: [এজেন্ট ফ্রেমওয়ার্ক](./code_samples/02-dotnet-agent-framework.md)

## AI Agent Frameworks সম্পর্কে আরও প্রশ্ন আছে?

অন্যান্য শিক্ষার্থীদের সাথে দেখা করতে, অফিস আওয়ার-এ অংশ নিতে এবং আপনার AI Agents সম্পর্কিত প্রশ্নগুলোর উত্তর পেতে [Microsoft Foundry Discord](https://aka.ms/ai-agents/discord)-এ যোগ দিন।

## রেফারেন্স

- <a href="https://techcommunity.microsoft.com/blog/azure-ai-services-blog/introducing-azure-ai-agent-service/4298357" target="_blank">Azure এজেন্ট সার্ভিস</a>
- <a href="https://learn.microsoft.com/azure/ai-services/openai/how-to/responses" target="_blank">Microsoft Agent Framework - Azure OpenAI প্রতিক্রিয়াসমূহ</a>
- <a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Azure AI Agent সার্ভিস</a>

## পূর্ববর্তী পাঠ

[AI এজেন্ট এবং তাদের ব্যবহার-কেসের পরিচিতি](../01-intro-to-ai-agents/README.md)

## পরবর্তী পাঠ

[এজেন্টিক ডিজাইন প্যাটার্নগুলি বোঝা](../03-agentic-design-patterns/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
দায়-অস্বীকার:

এই দলিলটি AI অনুবাদ সেবা [Co-op Translator](https://github.com/Azure/co-op-translator) ব্যবহার করে অনুবাদ করা হয়েছে। যদিও আমরা যথার্থতার দিকে যত্নবান, স্বয়ংক্রিয় অনুবাদে ত্রুটি বা ভুল থাকতে পারে তা অনুগ্রহ করে মনে রাখুন। মূল নথি (তার নিজভাষায়) কে কর্তৃত্বশীল উৎস হিসেবে গণ্য করা উচিত। গুরুত্বপূর্ণ তথ্যের জন্য পেশাদার মানব অনুবাদের পরামর্শ দেওয়া হচ্ছে। এই অনুবাদ ব্যবহারের ফলে সৃষ্ট কোনো ভুল বোঝাবুঝি বা ভুল ব্যাখ্যার জন্য আমরা দায়ী নই।
<!-- CO-OP TRANSLATOR DISCLAIMER END -->