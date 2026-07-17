[![বিশ্বাসযোগ্য এআই এজেন্ট](../../../translated_images/bn/lesson-6-thumbnail.a58ab36c099038d4.webp)](https://youtu.be/iZKkMEGBCUQ?si=Q-kEbcyHUMPoHp8L)

> _(এই পাঠের ভিডিও দেখতে উপরের ছবি ক্লিক করুন)_

# বিশ্বাসযোগ্য এআই এজেন্ট তৈরি করা

## পরিচিতি

এই পাঠে আলোচনা করা হবে:

- কীভাবে নিরাপদ এবং কার্যকরী এআই এজেন্ট তৈরি এবং মোতায়েন করবেন
- এআই এজেন্ট উন্নয়নের সময় গুরুত্বপূর্ণ নিরাপত্তা বিবেচনা।
- এআই এজেন্ট উন্নয়নের সময় ডেটা এবং ব্যবহারকারীর গোপনীয়তা কীভাবে বজায় রাখা যায়।

## শেখার লক্ষ্য

এই পাঠ সম্পূর্ণ করার পর, আপনি জানতে পারবেন কীভাবে:

- এআই এজেন্ট তৈরি করার সময় ঝুঁকি সনাক্ত এবং প্রশমিত করবেন।
- ডেটা এবং অ্যাক্সেস সঠিকভাবে পরিচালিত হয় তা নিশ্চিত করার জন্য নিরাপত্তা ব্যবস্থা প্রয়োগ করবেন।
- ডেটা গোপনীয়তা বজায় রেখে এবং মানসম্পন্ন ব্যবহারকারীর অভিজ্ঞতা প্রদানকারী এআই এজেন্ট তৈরি করবেন।

## নিরাপত্তা

চলুন প্রথমে নিরাপদ এজেন্টিক অ্যাপ্লিকেশন তৈরি সম্পর্কে দেখি। নিরাপত্তা অর্থ হলো এআই এজেন্ট তার ডিজাইন অনুযায়ী কাজ করে। এজেন্টিক অ্যাপ্লিকেশন নির্মাতাদের জন্য আমাদের কাছে নিরাপত্তা সর্বাধিক করার পদ্ধতি ও টুলস রয়েছে:

### সিস্টেম মেসেজ ফ্রেমওয়ার্ক তৈরি করা

যদি আপনি কখনো বড় ভাষা মডেল (LLMs) ব্যবহার করে এআই অ্যাপ্লিকেশন তৈরি করে থাকেন, তাহলে আপনি জানেন একটি শক্তিশালী সিস্টেম প্রম্পট বা সিস্টেম মেসেজ ডিজাইন করার গুরুত্ব। এই প্রম্পটগুলো মেটা নিয়মাবলী, নির্দেশাবলী এবং নির্দেশিকা নির্ধারণ করে যা LLM ব্যবহারকারী এবং ডেটার সাথে কীভাবে যোগাযোগ করবে তা নিয়ন্ত্রণ করে।

এআই এজেন্টদের জন্য সিস্টেম প্রম্পট আরও বেশি গুরুত্বপূর্ণ কারণ এআই এজেন্টদের অত্যন্ত নির্দিষ্ট নির্দেশাবলী প্রয়োজন যাতে তারা আমাদের জন্য ডিজাইন করা টাস্কগুলি সম্পন্ন করতে পারে।

স্কেলযোগ্য সিস্টেম প্রম্পট তৈরি করতে, আমরা আমাদের অ্যাপ্লিকেশনে একটি বা একাধিক এজেন্ট তৈরি করার জন্য সিস্টেম মেসেজ ফ্রেমওয়ার্ক ব্যবহার করতে পারি:

![সিস্টেম মেসেজ ফ্রেমওয়ার্ক তৈরি](../../../translated_images/bn/system-message-framework.3a97368c92d11d68.webp)

#### ধাপ ১: একটি মেটা সিস্টেম মেসেজ তৈরি করুন

মেটা প্রম্পটটি একটি LLM ব্যবহার করে আমাদের তৈরি করা এজেন্টদের জন্য সিস্টেম প্রম্পট তৈরি করতে ব্যবহৃত হবে। আমরা এটি একটি টেমপ্লেট হিসেবে ডিজাইন করি যাতে প্রয়োজনে আমরা দক্ষভাবে একাধিক এজেন্ট তৈরি করতে পারি।

এখানে একটি উদাহরণ মেটা সিস্টেম মেসেজ যা আমরা LLM-কে দেব:

```plaintext
You are an expert at creating AI agent assistants. 
You will be provided a company name, role, responsibilities and other
information that you will use to provide a system prompt for.
To create the system prompt, be descriptive as possible and provide a structure that a system using an LLM can better understand the role and responsibilities of the AI assistant. 
```

#### ধাপ ২: একটি মৌলিক প্রম্পট তৈরি করুন

পরবর্তী ধাপ হলো এআই এজেন্ট বর্ণনা করার জন্য একটি মৌলিক প্রম্পট তৈরি করা। এতে এজেন্টের ভূমিকা, এজেন্ট সম্পন্ন করবে এমন কাজগুলি এবং এজেন্টের অন্যান্য দায়িত্ব অন্তর্ভুক্ত করা উচিত।

এখানে একটি উদাহরণ দেওয়া হলো:

```plaintext
You are a travel agent for Contoso Travel that is great at booking flights for customers. To help customers you can perform the following tasks: lookup available flights, book flights, ask for preferences in seating and times for flights, cancel any previously booked flights and alert customers on any delays or cancellations of flights.  
```

#### ধাপ ৩: মৌলিক সিস্টেম মেসেজ LLM-কে প্রদান করুন

এখন আমরা এই সিস্টেম মেসেজটিকে উন্নত করতে পারি মেটা সিস্টেম মেসেজ এবং আমাদের মৌলিক সিস্টেম মেসেজ উভয়ই সিস্টেম মেসেজ হিসেবে প্রদান করে।

এটি একটি সিস্টেম মেসেজ তৈরি করবে যা আমাদের এআই এজেন্টদের নির্দেশনা দেওয়ার জন্য আরও ভাল ডিজাইন করা হয়েছে:

```markdown
**Company Name:** Contoso Travel  
**Role:** Travel Agent Assistant

**Objective:**  
You are an AI-powered travel agent assistant for Contoso Travel, specializing in booking flights and providing exceptional customer service. Your main goal is to assist customers in finding, booking, and managing their flights, all while ensuring that their preferences and needs are met efficiently.

**Key Responsibilities:**

1. **Flight Lookup:**
    
    - Assist customers in searching for available flights based on their specified destination, dates, and any other relevant preferences.
    - Provide a list of options, including flight times, airlines, layovers, and pricing.
2. **Flight Booking:**
    
    - Facilitate the booking of flights for customers, ensuring that all details are correctly entered into the system.
    - Confirm bookings and provide customers with their itinerary, including confirmation numbers and any other pertinent information.
3. **Customer Preference Inquiry:**
    
    - Actively ask customers for their preferences regarding seating (e.g., aisle, window, extra legroom) and preferred times for flights (e.g., morning, afternoon, evening).
    - Record these preferences for future reference and tailor suggestions accordingly.
4. **Flight Cancellation:**
    
    - Assist customers in canceling previously booked flights if needed, following company policies and procedures.
    - Notify customers of any necessary refunds or additional steps that may be required for cancellations.
5. **Flight Monitoring:**
    
    - Monitor the status of booked flights and alert customers in real-time about any delays, cancellations, or changes to their flight schedule.
    - Provide updates through preferred communication channels (e.g., email, SMS) as needed.

**Tone and Style:**

- Maintain a friendly, professional, and approachable demeanor in all interactions with customers.
- Ensure that all communication is clear, informative, and tailored to the customer's specific needs and inquiries.

**User Interaction Instructions:**

- Respond to customer queries promptly and accurately.
- Use a conversational style while ensuring professionalism.
- Prioritize customer satisfaction by being attentive, empathetic, and proactive in all assistance provided.

**Additional Notes:**

- Stay updated on any changes to airline policies, travel restrictions, and other relevant information that could impact flight bookings and customer experience.
- Use clear and concise language to explain options and processes, avoiding jargon where possible for better customer understanding.

This AI assistant is designed to streamline the flight booking process for customers of Contoso Travel, ensuring that all their travel needs are met efficiently and effectively.

```

#### ধাপ ৪: পুনরাবৃত্তি এবং উন্নতি করুন

এই সিস্টেম মেসেজ ফ্রেমওয়ার্কের মূল্য হলো এটি একাধিক এজেন্ট থেকে সিস্টেম মেসেজ তৈরি করা সহজ করে তোলে এবং আপনার সিস্টেম মেসেজগুলি সময়ের সাথে সাথে উন্নত করতে সাহায্য করে। আপনার সম্পূর্ণ ব্যবহার কেসের জন্য প্রথমবারেই এমন একটি সিস্টেম মেসেজ থাকা খুবই বিরল। মৌলিক সিস্টেম মেসেজ পরিবর্তন করে এবং সেটিকে সিস্টেমের মাধ্যমে চালিয়ে ছোট ছোট সংশোধন এবং উন্নতি করা আপনাকে ফলাফল তুলনা ও মূল্যায়ন করতে সাহায্য করবে।

## হুমকি সমূহ বোঝা

বিশ্বাসযোগ্য এআই এজেন্ট তৈরি করতে, আপনার এআই এজেন্টের ঝুঁকি এবং হুমকিগুলি বুঝা এবং প্রশমিত করা গুরুত্বপূর্ণ। চলুন কিছু ভিন্ন ধরনের এআই এজেন্ট হুমকি এবং সেগুলোর জন্য কীভাবে ভালো পরিকল্পনা ও প্রস্তুতি নিতে হয় দেখি।

![হুমকিগুলো বোঝা](../../../translated_images/bn/understanding-threats.89edeada8a97fc0f.webp)

### টাস্ক এবং নির্দেশনা

**বর্ণনা:** আক্রমণকারীরা প্রম্পটিং বা ইনপুট পরিবর্তনের মাধ্যমে এআই এজেন্টের নির্দেশনা বা লক্ষ্য পরিবর্তন করার চেষ্টা করে।

**প্রশমন**: যথাযথ যাচাইকরণ পরীক্ষা এবং ইনপুট ফিল্টার প্রয়োগ করুন যাতে সম্ভাব্য বিপজ্জনক প্রম্পটগুলি এআই এজেন্ট প্রক্রিয়াজাত করার আগে সনাক্ত করা যায়। যেহেতু এই আক্রমণগুলি সাধারণত পুনরাবৃত্তি হয়, তাই কথোপকথনের প্রদত্ত সংখ্যাকে সীমাবদ্ধ করাও এই ধরনের আক্রমণ প্রতিহত করার একটি উপায়।

### গুরুত্বপূর্ণ সিস্টেমে অ্যাক্সেস

**বর্ণনা**: যদি একটি এআই এজেন্টের সেসব সিস্টেম এবং সার্ভিসে প্রবেশাধিকার থাকে যেখানে সংবেদনশীল তথ্য সংরক্ষিত থাকে, তবে আক্রমণকারীরা এজেন্ট এবং এই সার্ভিসগুলির মধ্যে যোগাযোগ বিকৃত করতে পারে। এগুলো সরাসরি আক্রমণ হতে পারে বা এজেন্টের মাধ্যমে এসব সিস্টেমের তথ্য আহরণের প্রচেষ্টা হতে পারে।

**প্রশমন**: এআই এজেন্টগুলিকে শুধুমাত্র প্রয়োজন অনুযায়ী সিস্টেমে অ্যাক্সেস দেওয়া উচিত এ ধরনের আক্রমণ প্রতিরোধে। এজেন্ট এবং সিস্টেমের মধ্যে যোগাযোগ অবশ্যই নিরাপদ হওয়া উচিত। প্রমাণীকরণ এবং অ্যাক্সেস নিয়ন্ত্রণ প্রয়োগ করাও তথ্য সুরক্ষার আরেকটি উপায়।

### রিসোর্স এবং সার্ভিস অতিরিক্ত চাপ

**বর্ণনা:** এআই এজেন্টরা টাস্ক সম্পাদনের জন্য বিভিন্ন টুলস এবং সার্ভিস ব্যবহার করতে পারে। আক্রমণকারী এই ক্ষমতাকে ব্যবহার করে এআই এজেন্টের মাধ্যমে সার্ভিসগুলিতে উচ্চমাত্রার অনুরোধ পাঠিয়ে সিস্টেম ব্যর্থতা বা বেশি খরচের কারণ হতে পারে।

**প্রশমন:** একটি সার্ভিসে কতগুলি অনুরোধ এআই এজেন্ট করতে পারে তা সীমাবদ্ধ করার জন্য নীতি প্রয়োগ করুন। কথোপকথনের রাউন্ড সংখ্যা ও অনুরোধ সীমাবদ্ধ করাও এই ধরনের আক্রমণ প্রতিরোধে সহায়ক।

### জ্ঞানভিত্তি দূষণ

**বর্ণনা:** এই ধরনের আক্রমণ সরাসরি এআই এজেন্টকেই লক্ষ্য করে না, বরং জ্ঞানভিত্তি এবং অন্যান্য সার্ভিসগুলোকে লক্ষ্য করে যা এআই এজেন্ট টাস্ক সম্পন্ন করতে ব্যবহার করবে। এতে ডেটা বা তথ্য দূষিত করা হতে পারে, যার ফলে পক্ষপাতদুষ্ট বা অপ্রত্যাশিত প্রতিক্রিয়া ব্যবহারকারীর কাছে পৌঁছতে পারে।

**প্রশমন:** এআই এজেন্টের ওয়ার্কফ্লোতে ব্যবহৃত ডেটার নিয়মিত যাচাইকরণ করুন। এই ডেটাতে প্রবেশাধিকার নিরাপদ রাখুন এবং কেবল বিশ্বাসযোগ্য ব্যক্তিরাই এটি পরিবর্তন করতে পারুক, এই ধরনের আক্রমণ এড়াতে।

### ধারাবাহিক ত্রুটি

**বর্ণনা:** এআই এজেন্ট বিভিন্ন টুলস এবং সার্ভিস ব্যবহার করে টাস্ক সম্পন্ন করে। আক্রমণকারীর কারণে সৃষ্ট ত্রুটি অন্য সিস্টেমের ব্যর্থতার কারণ হতে পারে, যা আক্রমণটিকে বিস্তৃত এবং সমস্যার সমাধান জটিল করে তোলে।

**প্রশমন**: এআই এজেন্টকে একটি সীমিত পরিবেশে চালানো যেমন, ডকার কনটেইনারে কাজ করানো যাতে সরাসরি সিস্টেম আক্রমণ ঠেকানো যায়। নির্দিষ্ট সিস্টেমে ত্রুটি এলে বিকল্প পদক্ষেপ এবং পুনরায় চেষ্টা করার লজিক তৈরি করাও বড় সিস্টেম ব্যর্থতা প্রতিরোধ করতে সহায়ক।

## মানব-সম্মিলিত

বিশ্বাসযোগ্য এআই এজেন্ট সিস্টেম তৈরির আরেকটি কার্যকর পদ্ধতি হলো মানব-সম্মিলিত পদ্ধতি। এতে এমন একটি প্রবাহ তৈরি হয় যেখানে ব্যবহারকারীরা চলাকালীন এজেন্টদের প্রতিক্রিয়া দিতে পারেন। ব্যবহারকারীরা একটি মাল্টি-এজেন্ট সিস্টেমে এজেন্টের ভূমিকা পালন করেন এবং চলমান প্রক্রিয়াটি অনুমোদন বা বন্ধ করার মাধ্যমে নিয়ন্ত্রণ রাখেন।

![মানব-সম্মিলিত](../../../translated_images/bn/human-in-the-loop.5f0068a678f62f4f.webp)

এখানে Microsoft Agent Framework ব্যবহার করে এই ধারণাটি কীভাবে বাস্তবায়িত হয় তার একটি কোড স্নিপেট:

```python
import os
from agent_framework.azure import AzureAIProjectAgentProvider
from azure.identity import AzureCliCredential

# মানব-ইন-দ্য-লুপ অনুমোদনের সাথে প্রদানকারী তৈরি করুন
provider = AzureAIProjectAgentProvider(
    credential=AzureCliCredential(),
)

# মানব অনুমোদন ধাপ সহ এজেন্ট তৈরি করুন
response = provider.create_response(
    input="Write a 4-line poem about the ocean.",
    instructions="You are a helpful assistant. Ask for user approval before finalizing.",
)

# ব্যবহারকারী উত্তর পর্যালোচনা এবং অনুমোদন করতে পারেন
print(response.output_text)
user_input = input("Do you approve? (APPROVE/REJECT): ")
if user_input == "APPROVE":
    print("Response approved.")
else:
    print("Response rejected. Revising...")
```

## উপসংহার

বিশ্বাসযোগ্য এআই এজেন্ট তৈরি করার জন্য দরকার সযত্ন ডিজাইন, শক্তিশালী নিরাপত্তা ব্যবস্থা, এবং নিয়মিত পুনরাবৃত্তি। কাঠামোবদ্ধ মেটা প্রম্পটিং সিস্টেম প্রয়োগ, সম্ভাব্য হুমকি বোঝা এবং প্রশমন কৌশল ব্যবহার করে ডেভেলপাররা নিরাপদ এবং কার্যকরী এআই এজেন্ট তৈরি করতে পারেন। এছাড়া, মানব-সম্মিলিত পদ্ধতি অন্তর্ভুক্ত করলে এআই এজেন্টরা ব্যবহারকারীর চাহিদার সাথে সঙ্গতিপূর্ণ থাকে এবং ঝুঁকি কমায়। এআই এর ক্রমবর্ধমান বিকাশের সঙ্গে, নিরাপত্তা, গোপনীয়তা এবং নৈতিক দিক বিবেচনায় সক্রিয় থাকা এআই চালিত সিস্টেমে বিশ্বাস ও নির্ভরযোগ্যতা বৃদ্ধিতে গুরুত্বপূর্ণ ভূমিকা রাখবে।

## কোড নমুনা

- [`code_samples/06-system-message-framework.ipynb`](code_samples/06-system-message-framework.ipynb): মেটা-প্রম্পট সিস্টেম-মেসেজ ফ্রেমওয়ার্কের ধাপে ধাপে প্রদর্শনী।
- [`code_samples/06-human-in-the-loop.ipynb`](code_samples/06-human-in-the-loop.ipynb): বিশ্বাসযোগ্য এজেন্টদের জন্য পূর্ব-কর্ম অনুমোদন গেট, ঝুঁকি স্তর বিভাজন, এবং অডিট লগিং।

### বিশ্বাসযোগ্য এআই এজেন্ট নির্মাণ সম্পর্কে আরও প্রশ্ন?

[Microsoft Foundry Discord](https://aka.ms/ai-agents/discord)-এ যোগ দিন অন্যান্য শিক্ষার্থীদের সাথে পরিচিত হতে, অফিস আওয়ার অংশগ্রহণ করতে এবং আপনার এআই এজেন্ট সম্পর্কিত প্রশ্নের উত্তর পেতে।

## অতিরিক্ত সম্পদ

- <a href="https://learn.microsoft.com/azure/ai-studio/responsible-use-of-ai-overview" target="_blank">দায়িত্বশীল এআই ওভারভিউ</a>
- <a href="https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai" target="_blank">জেনারেটিভ এআই মডেল এবং এআই অ্যাপ্লিকেশনের মূল্যায়ন</a>
- <a href="https://learn.microsoft.com/azure/ai-services/openai/concepts/system-message?context=%2Fazure%2Fai-studio%2Fcontext%2Fcontext&tabs=top-techniques" target="_blank">নিরাপত্তা সিস্টেম মেসেজ</a>
- <a href="https://blogs.microsoft.com/wp-content/uploads/prod/sites/5/2022/06/Microsoft-RAI-Impact-Assessment-Template.pdf?culture=en-us&country=us" target="_blank">ঝুঁকি মূল্যায়ন টেমপ্লেট</a>

## পূর্ববর্তী পাঠ

[Agentic RAG](../05-agentic-rag/README.md)

## পরবর্তী পাঠ

[পরিকল্পনা ডিজাইন প্যাটার্ন](../07-planning-design/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**অস্বীকৃতি**:
এই নথিটি AI অনুবাদ পরিষেবা [Co-op Translator](https://github.com/Azure/co-op-translator) ব্যবহার করে অনূদিত হয়েছে। যদিও আমরা শুদ্ধতার জন্য চেষ্টা করি, অনুগ্রহ করে মনে রাখবেন যে স্বয়ংক্রিয় অনুবাদে ত্রুটি বা অসঙ্গতি থাকতে পারে। মূল নথিটি তার স্বভাষায় কর্তৃত্বপূর্ণ উৎস হিসেবে বিবেচিত হওয়া উচিত। গুরুত্বপূর্ণ তথ্যের জন্য পেশাদার মানব অনুবাদ সুপারিশ করা হয়। এই অনুবাদের ব্যবহারে প্রয়োজনীয় ভুল বোঝাবুঝি বা ভুল ব্যাখ্যার জন্য আমরা দায়বদ্ধ নই।
<!-- CO-OP TRANSLATOR DISCLAIMER END -->