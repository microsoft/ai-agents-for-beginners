[![বিশ্বস্ত AI এজেন্ট](../../../translated_images/bn/lesson-6-thumbnail.a58ab36c099038d4.webp)](https://youtu.be/iZKkMEGBCUQ?si=Q-kEbcyHUMPoHp8L)

> _(এই পাঠের ভিডিও দেখতে উপরের ছবিটিতে ক্লিক করুন)_

# বিশ্বস্ত AI এজেন্ট তৈরী

## পরিচিতি

এই পাঠে আলোচনা করা হবে:

- কীভাবে নিরাপদ এবং কার্যকর AI এজেন্ট তৈরি ও স্থাপন করবেন
- AI এজেন্ট বিকাশের সময় গুরুত্বপূর্ণ সিকিউরিটি বিবেচনা
- AI এজেন্ট তৈরি করার সময় ডেটা এবং ব্যবহারকারীর গোপনীয়তা রক্ষা করার পদ্ধতি

## শেখার লক্ষ্য

এই পাঠ শেষ করার পর আপনি জানতে পারবেন:

- AI এজেন্ট তৈরির সময় ঝুঁকি শনাক্ত ও প্রশমনের পদ্ধতি
- ডেটা এবং অ্যাক্সেস সঠিকভাবে ব্যবস্থাপনার জন্য সিকিউরিটি ব্যবস্থা প্রয়োগ করা
- ডেটা গোপনীয়তা রক্ষা এবং উচ্চমানের ব্যবহারকারীর অভিজ্ঞতা নিশ্চিত করার জন্য AI এজেন্ট তৈরি

## নিরাপত্তা

চলুন প্রথমে নিরাপদ এজেন্টিক অ্যাপ্লিকেশন তৈরির দিকে নজর দেওয়া যাক। নিরাপত্তার অর্থ AI এজেন্ট ডিজাইন অনুযায়ী কাজ করছে। এজেন্টিক অ্যাপ্লিকেশন নির্মাতারা হিসেবে, আমরা নিরাপত্তা সর্বাধিক করার জন্য কিছু পদ্ধতি ও টুলস ব্যবহার করি:

### একটি সিস্টেম মেসেজ ফ্রেমওয়ার্ক নির্মাণ

যদি আপনি আগে কখনও বড় ভাষা মডেল (LLMs) ব্যবহার করে AI অ্যাপ্লিকেশন তৈরি করে থাকেন, তবে আপনি জানেন একটি দৃঢ় সিস্টেম প্রম্পট বা সিস্টেম মেসেজ ডিজাইনের গুরুত্ব। এই প্রম্পটগুলো মেটা নিয়ম, নির্দেশনা এবং গাইডলাইন স্থাপন করে যে কিভাবে LLM ব্যবহারকারী ও ডেটার সাথে ইন্টারঅ্যাক্ট করবে।

AI এজেন্টের ক্ষেত্রে, সিস্টেম প্রম্পট আরও গুরুত্বপূর্ণ কারণ AI এজেন্টদের আমাদের ডিজাইন করা কাজগুলো সম্পন্ন করার জন্য অত্যন্ত নির্দিষ্ট নির্দেশনা প্রয়োজন।

স্কেলযোগ্য সিস্টেম প্রম্পট তৈরি করতে, আমরা আমাদের অ্যাপ্লিকেশনের এক বা একাধিক এজেন্ট তৈরির জন্য একটি সিস্টেম মেসেজ ফ্রেমওয়ার্ক ব্যবহার করতে পারি:

![সিস্টেম মেসেজ ফ্রেমওয়ার্ক নির্মাণ](../../../translated_images/bn/system-message-framework.3a97368c92d11d68.webp)

#### ধাপ ১: একটি মেটা সিস্টেম মেসেজ তৈরি করুন

এই মেটা প্রম্পটটি LLM ব্যবহার করে আমরা তৈরি করব, যা এজেন্টদের জন্য সিস্টেম প্রম্পট জেনারেট করবে। আমরা এটি একটি টেমপ্লেট হিসেবে ডিজাইন করি যাতে প্রয়োজনে অনেকগুলো এজেন্ট সহজে তৈরি করা যায়।

এখানে একটি মেটা সিস্টেম মেসেজের উদাহরণ যা আমরা LLM-কে দেব:

```plaintext
You are an expert at creating AI agent assistants. 
You will be provided a company name, role, responsibilities and other
information that you will use to provide a system prompt for.
To create the system prompt, be descriptive as possible and provide a structure that a system using an LLM can better understand the role and responsibilities of the AI assistant. 
```

#### ধাপ ২: একটি মৌলিক প্রম্পট তৈরি করুন

পরবর্তী ধাপ হল AI এজেন্টের বর্ণনা দেওয়ার জন্য একটি মৌলিক প্রম্পট তৈরি করা। এতে আপনি এজেন্টের ভূমিকা, এজেন্ট সম্পন্ন করার কাজগুলো এবং এজেন্টের অন্যান্য দায়িত্ব অন্তর্ভুক্ত করবেন।

এখানে একটি উদাহরণ:

```plaintext
You are a travel agent for Contoso Travel that is great at booking flights for customers. To help customers you can perform the following tasks: lookup available flights, book flights, ask for preferences in seating and times for flights, cancel any previously booked flights and alert customers on any delays or cancellations of flights.  
```

#### ধাপ ৩: মৌলিক সিস্টেম মেসেজ LLM-কে প্রদান করুন

এখন আমরা সিস্টেম মেসেজকে আরও উন্নত করতে পারি মেটা সিস্টেম মেসেজ এবং আমাদের মৌলিক সিস্টেম মেসেজ উভয়কে সিস্টেম মেসেজ হিসেবে প্রদান করে।

এটি একটি উন্নত সিস্টেম মেসেজ তৈরি করবে যা আমাদের AI এজেন্টদের পরিচালনায় সহায়ক:

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

#### ধাপ ৪: পুনরাবৃত্তি ও উন্নতি করুন

এই সিস্টেম মেসেজ ফ্রেমওয়ার্কের মূল্য হল সহজেই একাধিক এজেন্টদের জন্য সিস্টেম মেসেজ তৈরি করা এবং সময়ের সাথে আপনার সিস্টেম মেসেজ উন্নত করা। সাধারনত প্রথমবারেই আপনার পুরো ব্যবহারের ক্ষেত্রে সিস্টেম মেসেজ কাজ করবে এমনটি হওয়া দুর্লভ। মৌলিক সিস্টেম মেসেজ পরিবর্তন করে ছোটখাটো সমন্বয় ও উন্নতি করা এবং সিস্টেম দিয়ে সেটি চালিয়ে ফলাফল তুলনা ও মূল্যায়ন করার সুযোগ থাকবে।

## হুমকি বোঝা

বিশ্বস্ত AI এজেন্ট তৈরির জন্য, আপনার AI এজেন্টের ঝুঁকি এবং হুমকি বোঝা ও প্রশমন করা গুরুত্বপূর্ণ। আসুন AI এজেন্টদের বিভিন্ন হুমকির মধ্যে কিছুকে দেখে নেই এবং কীভাবে আপনি এগুলোর জন্য ভাল পরিকল্পনা ও প্রস্তুতি নিতে পারেন।

![হুমকি বোঝা](../../../translated_images/bn/understanding-threats.89edeada8a97fc0f.webp)

### কাজ এবং নির্দেশনা

**বর্ণনা:** আক্রমণকারীরা AI এজেন্টের নির্দেশ বা লক্ষ্য পরিবর্তনের চেষ্টা করে প্রম্পটিং বা ইনপুট ম্যানিপুলেশনের মাধ্যমে।

**প্রতিরোধ:** প্রক্রিয়াকরণের আগে বিপজ্জনক প্রম্পট সনাক্তের জন্য যাচাই পরীক্ষা এবং ইনপুট ফিল্টার কার্যকর করুন। যেহেতু এই ধরনের আক্রমণ প্রায়ই এজেন্টের সাথে ঘনিষ্ট যোগাযোগের মাধ্যমে হয়, কথোপকথনের টার্ন সীমাবদ্ধ করাও এই আক্রমণ রোধের একটি উপায়।

### গুরুত্বপূর্ণ সিস্টেমে অ্যাক্সেস

**বর্ণনা:** যদি AI এজেন্ট সংবেদনশীল ডেটা সংরক্ষণকারী সিস্টেম ও সার্ভিসে অ্যাক্সেস পায়, আক্রমণকারীরা এজেন্ট এবং সার্ভিসের মধ্যে যোগাযোগে হস্তক্ষেপ করতে পারে। এটি সরাসরি আক্রমণ হতে পারে বা এজেন্টের মাধ্যমে তথ্য আহরণের চেষ্টা।

**প্রতিরোধ:** AI এজেন্টকে প্রয়োজনীয় মাত্রায় সিস্টেমে অ্যাক্সেস দিন যাতে এই ধরনের আক্রমণ ঠেকানো যায়। এজেন্ট ও সিস্টেমের মধ্যে যোগাযোগও সুরক্ষিত হতে হবে। প্রমাণীকরণ এবং অ্যাক্সেস নিয়ন্ত্রণ প্রয়োগও গুরুত্বপূর্ণ।

### রিসোর্স ও সার্ভিস অতিরঞ্জন

**বর্ণনা:** AI এজেন্ট বিভিন্ন টুল ও সার্ভিস ব্যবহার করে কাজ সম্পন্ন করতে পারে। আক্রমণকারীরা এই ক্ষমতা ব্যবহার করে AI এজেন্টের মাধ্যমে উচ্চ পরিমাণ অনুরোধ পাঠিয়ে সার্ভিসগুলোতে আঘাত হানতে পারে, যা সিস্টেম ব্যর্থতা বা অতিরিক্ত খরচের কারণ হতে পারে।

**প্রতিরোধ:** একটি সার্ভিসে AI এজেন্ট কতগুলি অনুরোধ করতে পারবে তা সীমাবদ্ধ করার নীতিমালা গ্রহণ করুন। কথোপকথনের টার্ন ও অনুরোধের সংখ্যা সীমিত করা এই ধরনের আক্রমণ প্রতিরোধের আরও একটি পদ্ধতি।

### জ্ঞানভিত্তি দূষণ

**বর্ণনা:** এই ধরনের আক্রমণ সরাসরি AI এজেন্টকে নয়, বরং জ্ঞানভিত্তি এবং অন্যান্য সার্ভিসগুলোকে লক্ষ্য করে যা AI এজেন্ট কাজের জন্য ব্যবহার করবে। এতে ডেটা বা তথ্য দুর্নীতিগ্রস্ত হতে পারে, যার ফলে পক্ষপাতমূলক বা অনিচ্ছাকৃত প্রতিক্রিয়া আসতে পারে।

**প্রতিরোধ:** নিয়মিত যাচাই-বাছাই করুন AI এজেন্টের ওয়ার্কফ্লোর জন্য ব্যবহৃত ডেটা। শুধুমাত্র বিশ্বস্ত ব্যক্তিরা এই ডেটা পরিবর্তন করতে পারে তা নিশ্চিত করুন যাতে এই ধরনের আক্রমণ প্রতিহত হয়।

### ক্রমান্বয়ে ত্রুটি

**বর্ণনা:** AI এজেন্ট বিভিন্ন টুল ও সার্ভিস ব্যবহার করে কাজ শেষ করে। আক্রমণকারীদের কারণে সৃষ্ট ত্রুটিগুলো অন্যান্য সংযুক্ত সিস্টেমে ব্যর্থতা ঘটাতে পারে, ফলে আক্রমণ ব্যাপক ও ভাষ্য নির্ণয়ে কঠিন হয়ে ওঠে।

**প্রতিরোধ:** এর উত্তরণ এড়াতে AI এজেন্টকে সীমিত পরিবেশে চলতে দিন, যেমন Docker কন্টেইনারে কাজ করা, যাতে সরাসরি সিস্টেম আক্রমণ ঠেকানো যায়। নির্দিষ্ট সিস্টেম ত্রুটি দিলে ব্যাকআপ ব্যবস্থার ব্যবস্থা রাখা এবং পুনরায় চেষ্টা করার যুক্তি তৈরি করাও বড় সিস্টেম ব্যর্থতা প্রতিরোধ করবে।

## মানব-ইন-দ্য-লুপ

আরেকটি কার্যকর উপায় হল বিশ্বস্ত AI এজেন্ট ব্যবস্থা তৈরিতে মানব-ইন-দ্য-লুপ ব্যবহার। এতে একটি প্রবাহ তৈরি হয় যেখানে ব্যবহারকারীরা চলাকালীন এজেন্টদের ফিডব্যাক দিতে পারে। ব্যবহারকারীরা কার্যত মাল্টি-এজেন্ট সিস্টেমের এজেন্ট হিসেবে আচরণ করেন এবং চলমান প্রক্রিয়া অনুমোদন বা সমাপ্তি দিতে পারেন।

![মানব ইন দ্য লুপ](../../../translated_images/bn/human-in-the-loop.5f0068a678f62f4f.webp)

এটি কিভাবে বাস্তবায়িত হয় তা দেখাতে Microsoft Agent Framework ব্যবহার করে কোডের একটি অংশ এখানে দেওয়া হলো:

```python
import os
from agent_framework.azure import AzureAIProjectAgentProvider
from azure.identity import AzureCliCredential

# হিউম্যান-ইন-দ্য-লুপ অনুমোদনের সাথে প্রদানকারী তৈরি করুন
provider = AzureAIProjectAgentProvider(
    credential=AzureCliCredential(),
)

# হিউম্যান অনুমোদন ধাপ সহ এজেন্ট তৈরি করুন
response = provider.create_response(
    input="Write a 4-line poem about the ocean.",
    instructions="You are a helpful assistant. Ask for user approval before finalizing.",
)

# ব্যবহারকারী প্রতিক্রিয়া পর্যালোচনা এবং অনুমোদন করতে পারেন
print(response.output_text)
user_input = input("Do you approve? (APPROVE/REJECT): ")
if user_input == "APPROVE":
    print("Response approved.")
else:
    print("Response rejected. Revising...")
```

## উপসংহার

বিশ্বস্ত AI এজেন্ট তৈরির জন্য সাবধানতার সাথে ডিজাইন, দৃঢ় সিকিউরিটি ব্যবস্থা ও অবিচ্ছিন্ন পুনরাবৃত্তি প্রয়োজন। সংগঠিত মেটা প্রম্পটিং সিস্টেম প্রয়োগ, সম্ভাব্য হুমকি বোঝা এবং প্রশমন কৌশল প্রয়োগ করে বিকাশকারীরা নিরাপদ ও কার্যকর AI এজেন্ট তৈরি করতে পারেন। এছাড়াও, মানব-ইন-দ্য-লুপ পদ্ধতি AI এজেন্টদের ব্যবহারকারীর চাহিদার সাথে সামঞ্জস্য বজায় রাখতে ও ঝুঁকি কমাতে সহায়ক। AI এর অগ্রগতির সাথে নিরাপত্তা, গোপনীয়তা এবং নৈতিক দিকগুলোতে সক্রিয় মনোভাব রাখা বিশ্বস্ততা ও নির্ভরযোগ্যতা বৃদ্ধিতে গুরুত্বপূর্ণ।

### বিশ্বস্ত AI এজেন্ট নির্মাণ বিষয়ে আরো প্রশ্ন আছে?

[Microsoft Foundry Discord](https://aka.ms/ai-agents/discord) -এ যোগ দিন অন্যান্য শিক্ষার্থীদের সাথে দেখা করতে, অফিস আওয়ার এ অংশ নিতে এবং আপনার AI এজেন্ট সম্পর্কিত প্রশ্নের উত্তর পেতে।

## অতিরিক্ত সম্পদ

- <a href="https://learn.microsoft.com/azure/ai-studio/responsible-use-of-ai-overview" target="_blank">দায়িত্বশীল AI ওভারভিউ</a>
- <a href="https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai" target="_blank">জেনারেটিভ AI মডেল এবং AI অ্যাপ্লিকেশন মূল্যায়ন</a>
- <a href="https://learn.microsoft.com/azure/ai-services/openai/concepts/system-message?context=%2Fazure%2Fai-studio%2Fcontext%2Fcontext&tabs=top-techniques" target="_blank">নিরাপত্তা সিস্টেম মেসেজ</a>
- <a href="https://blogs.microsoft.com/wp-content/uploads/prod/sites/5/2022/06/Microsoft-RAI-Impact-Assessment-Template.pdf?culture=en-us&country=us" target="_blank">ঝুঁকি মূল্যায়ন টেমপ্লেট</a>

## পূর্ববর্তী পাঠ

[Agentic RAG](../05-agentic-rag/README.md)

## পরবর্তী পাঠ

[Planning Design Pattern](../07-planning-design/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**দায়িত্বরোধ**:
এই নথিটি AI অনুবাদ সেবা [Co-op Translator](https://github.com/Azure/co-op-translator) ব্যবহার করে অনূদিত হয়েছে। আমরা যথাসম্ভব সঠিকতার চেষ্টা করি, তবে স্বয়ংক্রিয় অনুবাদে ত্রুটি বা অসঙ্গতি থাকতে পারে। মূল ভাষায় থাকা নথিটিকেই নির্ভরযোগ্য উৎস হিসেবে বিবেচনা করা উচিত। গুরুত্বপূর্ণ তথ্যের ক্ষেত্রে পেশাদার মানব অনুবাদ সুপারিশ করা হয়। এই অনুবাদের ব্যবহারে সৃষ্ট কোনো ভুল বোঝাবুঝি বা অসঙ্গতির জন্য আমরা দায়বদ্ধ নই।
<!-- CO-OP TRANSLATOR DISCLAIMER END -->