[![বিশ্বস্ত AI এজেন্টগুলি](../../../translated_images/bn/lesson-6-thumbnail.a58ab36c099038d4.webp)](https://youtu.be/iZKkMEGBCUQ?si=Q-kEbcyHUMPoHp8L)

> _(এই পাঠের ভিডিও দেখতে উপরের ছবিতে ক্লিক করুন)_

# বিশ্বস্ত AI এজেন্ট নির্মাণ

## পরিচিতি

এই পাঠে আলোচনা করা হবে:

- কিভাবে নিরাপদ ও কার্যকরী AI এজেন্ট তৈরি ও ডিপ্লয় করবেন
- AI এজেন্ট তৈরি করার সময় গুরুত্বপূর্ণ সুরক্ষা বিবেচনা।
- AI এজেন্ট তৈরি করার সময় ডেটা ও ব্যবহারকারীর গোপনীয়তা বজায় রাখা।

## শেখার লক্ষ্যসমূহ

এই পাঠ শেষ করার পর, আপনি জানতে পারবেন কিভাবে:

- AI এজেন্ট তৈরির সময় ঝুঁকি চিহ্নিত করা ও কমানো।
- নিশ্চিত করা যে ডেটা ও অ্যাক্সেস সঠিকভাবে পরিচালিত হয় সেদিকে নিরাপত্তা ব্যবস্থা প্রয়োগ।
- এমন AI এজেন্ট তৈরি করা যা ডেটা গোপনীয়তা বজায় রেখে ভালো ব্যবহারকারীর অভিজ্ঞতা দেয়।

## নিরাপত্তা

প্রথমে আসুন নিরাপদ এজেন্টিক অ্যাপ্লিকেশন নির্মাণ করি। নিরাপত্তা মানে AI এজেন্ট পরিকল্পিতভাবে কাজ করবে। এজেন্টিক অ্যাপ্লিকেশনের নির্মাতা হিসাবে, আমাদের কাছে নিরাপত্তা সর্বোচ্চ করার পদ্ধতি ও সরঞ্জাম রয়েছে:

### একটি সিস্টেম মেসেজ ফ্রেমওয়ার্ক তৈরি করা

যদি আপনি কখনো বড় ভাষা মডেল (LLMs) ব্যবহার করে AI অ্যাপ্লিকেশন তৈরি করে থাকেন, তবে আপনি জানেন একটি শক্তিশালী সিস্টেম প্রম্পট বা সিস্টেম মেসেজ ডিজাইনের গুরুত্ব। এই প্রম্পটগুলো মেটা নিয়ম, নির্দেশনা এবং গাইডলাইন স্থাপন করে কিভাবে LLM ব্যবহারকারী ও ডেটার সাথে ইন্টারঅ্যাক্ট করবে।

AI এজেন্টদের জন্য সিস্টেম প্রম্পট আরও গুরুত্বপূর্ণ কারণ AI এজেন্টদের আমাদের ডিজাইন করা কাজগুলো সম্পন্ন করার জন্য অত্যন্ত সুনির্দিষ্ট নির্দেশনা প্রয়োজন।

স্কেলযোগ্য সিস্টেম প্রম্পট তৈরির জন্য আমরা আমাদের অ্যাপ্লিকেশনে এক বা একাধিক এজেন্ট তৈরির জন্য একটি সিস্টেম মেসেজ ফ্রেমওয়ার্ক ব্যবহার করতে পারি:

![সিস্টেম মেসেজ ফ্রেমওয়ার্ক তৈরি](../../../translated_images/bn/system-message-framework.3a97368c92d11d68.webp)

#### ধাপ 1: একটি মেটা সিস্টেম মেসেজ তৈরি করুন

মেটা প্রম্পটটি LLM দ্বারা এজেন্টদের জন্য সিস্টেম প্রম্পট তৈরি করতে ব্যবহার করা হবে। আমরা এটিকে একটি টেমপ্লেট হিসেবে ডিজাইন করি যাতে প্রয়োজনে সহজে একাধিক এজেন্ট তৈরি করা যায়।

এখানে একটি উদাহরণ মেটা সিস্টেম মেসেজ যা আমরা LLM কে দিতে পারি:

```plaintext
You are an expert at creating AI agent assistants. 
You will be provided a company name, role, responsibilities and other
information that you will use to provide a system prompt for.
To create the system prompt, be descriptive as possible and provide a structure that a system using an LLM can better understand the role and responsibilities of the AI assistant. 
```

#### ধাপ 2: একটি বেসিক প্রম্পট তৈরি করুন

পরবর্তী ধাপ হলো AI এজেন্টের বর্ণনা দিতে একটি বেসিক প্রম্পট তৈরি করা। এর মধ্যে এজেন্টের ভূমিকা, কাজগুলো যা এজেন্ট সম্পন্ন করবে, এবং এজেন্টের অন্য যে কোনো দায়িত্ব অন্তর্ভুক্ত করা উচিত।

এখানে একটি উদাহরণ:

```plaintext
You are a travel agent for Contoso Travel that is great at booking flights for customers. To help customers you can perform the following tasks: lookup available flights, book flights, ask for preferences in seating and times for flights, cancel any previously booked flights and alert customers on any delays or cancellations of flights.  
```

#### ধাপ 3: বেসিক সিস্টেম মেসেজ LLM-কে প্রদান করুন

এখন আমরা এই সিস্টেম মেসেজটিকে অপ্টিমাইজ করতে পারি মেটা সিস্টেম মেসেজকে সিস্টেম মেসেজ হিসেবে ও আমাদের বেসিক সিস্টেম মেসেজ হিসেবে প্রদান করে।

এটি এমন একটি সিস্টেম মেসেজ তৈরি করবে যা আমাদের AI এজেন্টদের গাইড করার জন্য আরও ভালো ডিজাইন করা:

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

#### ধাপ 4: পুনরাবৃত্তি করুন এবং উন্নত করুন

এই সিস্টেম মেসেজ ফ্রেমওয়ার্কের মূল উদ্দেশ্য হল একাধিক এজেন্ট থেকে সিস্টেম মেসেজ তৈরি করা সহজ করা এবং সময়ের সাথে সিস্টেম মেসেজ উন্নত করা। এটি বিরল যে আপনার প্রথমবারের সিস্টেম মেসেজ সম্পূর্ণ কাজ করবে। ছোটখাটো পরিবর্তন এবং উন্নতি করে প্রতিদ্বন্দ্বিতা করতে পারবেন যদি আপনি বেসিক সিস্টেম মেসেজ পরিবর্তন করে সিস্টেমের মধ্যে চালান এবং ফলাফল তুলনা করুন।

## হুমকি বোঝা

বিশ্বস্ত AI এজেন্ট তৈরি করতে, এজেন্টের ঝুঁকি ও হুমকিগুলো বোঝা এবং কমানো গুরুত্বপূর্ণ। আসুন কিছু AI এজেন্টের হুমকির দিকে নজর দিই এবং কিভাবে আপনি এগুলো পরিকল্পনা ও প্রতিরোধ করতে পারেন।

![হুমকি বোঝা](../../../translated_images/bn/understanding-threats.89edeada8a97fc0f.webp)

### কাজ এবং নির্দেশনা

**বর্ণনা:** আক্রমণকারী প্রম্পটিং বা ইনপুট ম্যানিপুলেশনের মাধ্যমে AI এজেন্টের নির্দেশনা বা লক্ষ্য পরিবর্তন করার চেষ্টা করে।

**প্রতিরোধ:** সম্ভাব্য বিপজ্জনক প্রম্পট সনাক্তের জন্য বৈধতা পরীক্ষা এবং ইনপুট ফিল্টারগুলি কার্যকর করুন, যাতে এগুলো AI এজেন্ট প্রক্রিয়াকরণের আগে ধরা পড়ে। যেহেতু এই আক্রমণকারীগণ সাধারণত এজেন্টের সাথে নিয়মিত যোগাযোগ করে, কথোপকথনের সংখ্যা সীমাবদ্ধ করাও এই আক্রমণ রোধ করার উপায়।

### গুরুত্বপূর্ণ সিস্টেম অ্যাক্সেস

**বর্ণনা:** যদি AI এজেন্ট সিস্টেম ও পরিষেবাগুলিতে অ্যাক্সেস পায় যেখানে সংবেদনশীল তথ্য সঞ্চিত থাকে, আক্রমণকারীরা এজেন্ট ও পরিষেবার মধ্যে যোগাযোগের নিরাপত্তা ভঙ্গ করতে পারে। এগুলো সরাসরি আক্রমণ বা এজেন্টের মাধ্যমে তথ্য প্রাপ্তির চেষ্টা হতে পারে।

**প্রতিরোধ:** এই ধরনের আক্রমণ রোধে AI এজেন্টকে প্রয়োজন অনুযায়ী সিস্টেমে সীমিত অ্যাক্সেস দিন। এজেন্ট ও সিস্টেমের যোগাযোগ অবশ্যই নিরাপদ হওয়া উচিত। প্রমাণীকরণ এবং প্রবেশ নিয়ন্ত্রণ ব্যবস্থা বাস্তবায়ন এর আরেকটি উপায়।

### সম্পদ ও পরিষেবা অতিরিক্ত লোডিং

**বর্ণনা:** AI এজেন্ট বিভিন্ন টুল ও পরিষেবায় কাজ সম্পন্ন করার জন্য অ্যাক্সেস পায়। আক্রমণকারীরা এই ক্ষমতা ব্যবহার করে এজেন্টের মাধ্যমে পরিষেবাগুলিতে উচ্চ পরিমাণ অনুরোধ পাঠিয়ে সিস্টেমের ব্যর্থতা বা অতিরিক্ত খরচ সৃষ্টি করতে পারে।

**প্রতিরোধ:** পরিষেবায় এজেন্ট কতবার অনুরোধ করতে পারে তা সীমাবদ্ধ করার জন্য নীতি প্রয়োগ করুন। কথোপকথনের সংখ্যা কমানো এবং AI এজেন্টকে অনুরোধের সংখ্যা সীমাবদ্ধ করাও এই আক্রমণ প্রতিরোধের উপায়।

### জ্ঞানভাণ্ডার বিষাক্ততা

**বর্ণনা:** এই ধরনের আক্রমণ সরাসরি AI এজেন্টকে লক্ষ্য করে না, বরং সেই জ্ঞানভাণ্ডার এবং অন্যান্য পরিষেবাগুলিকে লক্ষ্য করে যা AI এজেন্ট কাজে লাগাবে। এতে তথ্য দূষিত করে বা বিকৃত করে ব্যবহারকারীকে পক্ষপাতমূলক বা অনাকাঙ্ক্ষিত প্রতিক্রিয়া প্রদান করা হয়।

**প্রতিরোধ:** AI এজেন্টের ওয়ার্কফ্লোতে ব্যবহৃত তথ্য নিয়মিত যাচাই করুন। এই তথ্যের অ্যাক্সেস নিরাপদ রাখুন এবং শুধুমাত্র বিশ্বাসযোগ্য ব্যক্তির দ্বারা পরিবর্তন করার ব্যবস্থা নিশ্চিত করুন।

### ক্রমাগত ত্রুটি

**বর্ণনা:** AI এজেন্ট বিভিন্ন টুল ও পরিষেবায় কাজ সম্পন্ন করতে অ্যাক্সেস পায়। আক্রমণকারীর সৃষ্ট ত্রুটিগুলো অন্য সিস্টেমের ব্যর্থতা সৃষ্টি করতে পারে, যার ফলে আক্রমণ বিস্তৃত ও সমস্যার সমাধান কঠিন হয়।

**প্রতিরোধ:** এজেন্টকে সিমিত পরিবেশে চালান, যেমন Docker কন্টেইনারের মধ্যে কাজ করানো, যাতে সরাসরি সিস্টেম আক্রমণ থেকে নিরাপদ থাকে। নির্দিষ্ট সিস্টেমের ত্রুটির জবাবে ফallback ও retry পদ্ধতি তৈরি করাও বড় সিস্টেম ব্যর্থতা রোধ করতে সাহায্য করে।

## মানব-ইন-দ্য-লুপ

বিশ্বস্ত AI এজেন্ট সিস্টেম তৈরি করার আরেকটি কার্যকর পদ্ধতি হলো মানব-ইন-দ্য-লুপ ব্যবহার করা। এতে এমন একটি প্রবাহ তৈরি হয় যেখানে ব্যবহারকারীরা চলাকালীন এজেন্টকে প্রতিক্রিয়া দিতে পারে। ব্যবহারকারীরা একধরনের মাল্টি-এজেন্ট সিস্টেমের এজেন্ট হিসেবে কাজ করে এবং চলমান প্রক্রিয়ার অনুমোদন বা সমাপ্তি দেয়।

![মানব ইন দ্য লুপ](../../../translated_images/bn/human-in-the-loop.5f0068a678f62f4f.webp)

এই ধারণাটি বাস্তবায়নের জন্য Microsoft Agent Framework ব্যবহার করে একটি কোড স্নিপেট এখানে দেওয়া হলো:

```python
import os
from agent_framework.foundry import FoundryChatClient
from azure.identity import AzureCliCredential

# মানব-ইন-দ্য-লুপ অনুমোদন সহ প্রদানকারী তৈরি করুন
provider = FoundryChatClient(
    project_endpoint=os.environ["AZURE_AI_PROJECT_ENDPOINT"],
    model=os.environ["AZURE_AI_MODEL_DEPLOYMENT_NAME"],
    credential=AzureCliCredential(),
)

# একটি মানব অনুমোদন ধাপ সহ এজেন্ট তৈরি করুন
response = provider.create_response(
    input="Write a 4-line poem about the ocean.",
    instructions="You are a helpful assistant. Ask for user approval before finalizing.",
)

# ব্যবহারকারী প্রতিক্রিয়া পর্যালোচনা এবং অনুমোদন করতে পারে
print(response.output_text)
user_input = input("Do you approve? (APPROVE/REJECT): ")
if user_input == "APPROVE":
    print("Response approved.")
else:
    print("Response rejected. Revising...")
```

## উপসংহার

বিশ্বস্ত AI এজেন্ট নির্মাণে সাবধান ডিজাইন, শক্তিশালী নিরাপত্তা ব্যবস্থা এবং ধারাবাহিক পুনরাবৃত্তি প্রয়োজন। কাঠামোবদ্ধ মেটা প্রম্পটিং সিস্টেম বাস্তবায়ন, সম্ভাব্য হুমকি বোঝা এবং প্রতিরোধ কৌশল প্রয়োগ করে ডেভেলপাররা নিরাপদ ও কার্যকরী AI এজেন্ট তৈরি করতে পারবেন। পাশাপাশি মানব-ইন-দ্য-লুপ পদ্ধতি অন্তর্ভুক্ত করে ব্যবহারকারীর প্রয়োজনের সাথে সংযুক্তি বজায় রাখা এবং ঝুঁকি হ্রাস করা সম্ভব। AI প্রযুক্তি উন্নতির সাথে নিরাপত্তা, গোপনীয়তা এবং নৈতিক বিষয়গুলিতে প্রোঅ্যাকটিভ মনোভাব বজায় রাখা বিশ্বস্ত ও নির্ভরযোগ্য AI-চালিত সিস্টেমের জন্য গুরুত্বপূর্ণ।

## কোড নমুনা

- [`code_samples/06-system-message-framework.ipynb`](code_samples/06-system-message-framework.ipynb): মেটা-প্রম্পট সিস্টেম-মেসেজ ফ্রেমওয়ার্কের ধাপে ধাপে প্রদর্শনী।
- [`code_samples/06-human-in-the-loop.ipynb`](code_samples/06-human-in-the-loop.ipynb): বিশ্বস্ত এজেন্টের জন্য প্রাক-কর্ম অনুমোদন গেট, ঝুঁকি শ্রেণিবিন্যাস, এবং অডিট লগিং।

### বিশ্বস্ত AI এজেন্ট নির্মাণ নিয়ে আরও প্রশ্ন আছে?

[Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D)-এ যোগ দিন অন্যান্য শিক্ষার্থীদের সাথে মেলামেশা করতে, অফিস আওয়ার অংশ নিতে এবং আপনার AI এজেন্টের প্রশ্নের উত্তর পেতে।

## অতিরিক্ত সম্পদ

- <a href="https://learn.microsoft.com/azure/ai-studio/responsible-use-of-ai-overview" target="_blank">দায়িত্বশীল AI ওভারভিউ</a>
- <a href="https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai" target="_blank">জেনারেটিভ AI মডেল এবং AI অ্যাপ্লিকেশনের মূল্যায়ন</a>
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