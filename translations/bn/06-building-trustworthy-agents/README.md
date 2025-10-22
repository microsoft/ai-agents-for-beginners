<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "498802b4c3c3cc486b86f27a12cebb34",
  "translation_date": "2025-08-29T12:13:02+00:00",
  "source_file": "06-building-trustworthy-agents/README.md",
  "language_code": "bn"
}
-->
[![Trustworthy AI Agents](../../../translated_images/lesson-6-thumbnail.a58ab36c099038d4f786c2b0d5d6e89f41f4c2ecc05ab10b67bced2695eeb218.bn.png)](https://youtu.be/iZKkMEGBCUQ?si=Q-kEbcyHUMPoHp8L)

> _(উপরের ছবিতে ক্লিক করে এই পাঠের ভিডিও দেখুন)_

# বিশ্বাসযোগ্য AI এজেন্ট তৈরি করা

## ভূমিকা

এই পাঠে আলোচনা করা হবে:

- কীভাবে নিরাপদ এবং কার্যকরী AI এজেন্ট তৈরি ও স্থাপন করা যায়।
- AI এজেন্ট তৈরি করার সময় গুরুত্বপূর্ণ নিরাপত্তা বিষয়গুলো।
- AI এজেন্ট তৈরি করার সময় ডেটা এবং ব্যবহারকারীর গোপনীয়তা কীভাবে বজায় রাখা যায়।

## শেখার লক্ষ্য

এই পাঠ সম্পন্ন করার পর, আপনি জানতে পারবেন:

- AI এজেন্ট তৈরি করার সময় ঝুঁকি চিহ্নিত করা এবং তা কমানোর উপায়।
- ডেটা এবং অ্যাক্সেস সঠিকভাবে পরিচালনা করার জন্য নিরাপত্তা ব্যবস্থা প্রয়োগ করা।
- AI এজেন্ট তৈরি করা যা ডেটার গোপনীয়তা বজায় রাখে এবং ব্যবহারকারীর জন্য মানসম্মত অভিজ্ঞতা প্রদান করে।

## নিরাপত্তা

চলুন প্রথমে নিরাপদ এজেন্টিক অ্যাপ্লিকেশন তৈরি করার দিকে নজর দিই। নিরাপত্তা মানে হলো AI এজেন্ট তার নির্ধারিত কাজ সঠিকভাবে সম্পন্ন করে। এজেন্টিক অ্যাপ্লিকেশন নির্মাতা হিসেবে, আমাদের কাছে নিরাপত্তা সর্বাধিক করার জন্য পদ্ধতি এবং সরঞ্জাম রয়েছে:

### সিস্টেম মেসেজ ফ্রেমওয়ার্ক তৈরি করা

যদি আপনি কখনও বড় ভাষার মডেল (LLM) ব্যবহার করে AI অ্যাপ্লিকেশন তৈরি করে থাকেন, তাহলে আপনি জানেন যে একটি শক্তিশালী সিস্টেম প্রম্পট বা সিস্টেম মেসেজ ডিজাইন করার গুরুত্ব কতটা। এই প্রম্পটগুলো LLM কীভাবে ব্যবহারকারী এবং ডেটার সাথে যোগাযোগ করবে তার নিয়ম, নির্দেশনা এবং নির্দেশিকা স্থাপন করে।

AI এজেন্টের ক্ষেত্রে, সিস্টেম প্রম্পট আরও বেশি গুরুত্বপূর্ণ কারণ AI এজেন্টকে নির্দিষ্ট কাজ সম্পন্ন করার জন্য অত্যন্ত সুনির্দিষ্ট নির্দেশনা প্রয়োজন।

স্কেলযোগ্য সিস্টেম প্রম্পট তৈরি করতে, আমরা আমাদের অ্যাপ্লিকেশনে এক বা একাধিক এজেন্ট তৈরি করার জন্য একটি সিস্টেম মেসেজ ফ্রেমওয়ার্ক ব্যবহার করতে পারি:

![Building a System Message Framework](../../../translated_images/system-message-framework.3a97368c92d11d6814577b03cd128ec8c71a5fd1e26f341835cfa5df59ae87ae.bn.png)

#### ধাপ ১: একটি মেটা সিস্টেম মেসেজ তৈরি করুন

মেটা প্রম্পটটি LLM দ্বারা ব্যবহৃত হবে আমাদের তৈরি করা এজেন্টগুলোর জন্য সিস্টেম প্রম্পট তৈরি করতে। আমরা এটি একটি টেমপ্লেট হিসেবে ডিজাইন করি যাতে প্রয়োজন হলে একাধিক এজেন্ট সহজে তৈরি করা যায়।

এখানে একটি মেটা সিস্টেম মেসেজের উদাহরণ দেওয়া হলো যা আমরা LLM-কে দেব:

```plaintext
You are an expert at creating AI agent assistants. 
You will be provided a company name, role, responsibilities and other
information that you will use to provide a system prompt for.
To create the system prompt, be descriptive as possible and provide a structure that a system using an LLM can better understand the role and responsibilities of the AI assistant. 
```

#### ধাপ ২: একটি বেসিক প্রম্পট তৈরি করুন

পরবর্তী ধাপে একটি বেসিক প্রম্পট তৈরি করতে হবে যা AI এজেন্টকে বর্ণনা করবে। এখানে এজেন্টের ভূমিকা, এজেন্ট যে কাজগুলো সম্পন্ন করবে এবং এজেন্টের অন্যান্য দায়িত্বগুলো অন্তর্ভুক্ত করা উচিত।

এখানে একটি উদাহরণ দেওয়া হলো:

```plaintext
You are a travel agent for Contoso Travel that is great at booking flights for customers. To help customers you can perform the following tasks: lookup available flights, book flights, ask for preferences in seating and times for flights, cancel any previously booked flights and alert customers on any delays or cancellations of flights.  
```

#### ধাপ ৩: LLM-কে বেসিক সিস্টেম মেসেজ প্রদান করুন

এখন আমরা মেটা সিস্টেম মেসেজকে সিস্টেম মেসেজ হিসেবে এবং আমাদের বেসিক সিস্টেম মেসেজকে প্রদান করে এই সিস্টেম মেসেজটি অপ্টিমাইজ করতে পারি।

এটি আমাদের AI এজেন্টকে নির্দেশনা দেওয়ার জন্য আরও ভালোভাবে ডিজাইন করা একটি সিস্টেম মেসেজ তৈরি করবে:

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

এই সিস্টেম মেসেজ ফ্রেমওয়ার্কের মূল্য হলো একাধিক এজেন্টের জন্য সিস্টেম মেসেজ তৈরি করা সহজতর করা এবং সময়ের সাথে আপনার সিস্টেম মেসেজ উন্নত করা। আপনার সম্পূর্ণ ব্যবহারের ক্ষেত্রে প্রথমবারেই একটি কার্যকরী সিস্টেম মেসেজ পাওয়া বিরল। বেসিক সিস্টেম মেসেজে ছোট পরিবর্তন এবং উন্নতি করে এবং সিস্টেমের মাধ্যমে এটি চালিয়ে তুলনা ও মূল্যায়ন করার মাধ্যমে আপনি ফলাফল উন্নত করতে পারবেন।

## হুমকি বোঝা

বিশ্বাসযোগ্য AI এজেন্ট তৈরি করতে হলে, আপনার AI এজেন্টের ঝুঁকি এবং হুমকি বোঝা এবং তা কমানোর উপায় জানা গুরুত্বপূর্ণ। চলুন AI এজেন্টের কিছু ভিন্ন হুমকি এবং সেগুলো মোকাবিলার পরিকল্পনা ও প্রস্তুতির উপায় দেখি।

![Understanding Threats](../../../translated_images/understanding-threats.89edeada8a97fc0f7053558567d5dd27c0c333b74e47fffdde490fa6777a4c17.bn.png)

### কাজ এবং নির্দেশনা

**বর্ণনা:** আক্রমণকারীরা প্রম্পট বা ইনপুট পরিবর্তন করে AI এজেন্টের নির্দেশনা বা লক্ষ্য পরিবর্তন করার চেষ্টা করে।

**প্রতিরোধ:** AI এজেন্টের প্রক্রিয়ায় যাওয়ার আগে সম্ভাব্য বিপজ্জনক প্রম্পট শনাক্ত করতে যাচাই চেক এবং ইনপুট ফিল্টার প্রয়োগ করুন। যেহেতু এই ধরনের আক্রমণ সাধারণত এজেন্টের সাথে ঘন ঘন যোগাযোগের প্রয়োজন হয়, কথোপকথনের টার্ন সংখ্যা সীমিত করাও এই ধরনের আক্রমণ প্রতিরোধের একটি উপায়।

### গুরুত্বপূর্ণ সিস্টেমে অ্যাক্সেস

**বর্ণনা:** যদি AI এজেন্টের কাছে সংবেদনশীল ডেটা সংরক্ষণকারী সিস্টেম এবং পরিষেবাগুলোর অ্যাক্সেস থাকে, তাহলে আক্রমণকারীরা এজেন্ট এবং এই পরিষেবাগুলোর মধ্যে যোগাযোগকে বিপর্যস্ত করতে পারে। এটি সরাসরি আক্রমণ বা এজেন্টের মাধ্যমে এই সিস্টেম সম্পর্কে তথ্য পাওয়ার প্রচেষ্টা হতে পারে।

**প্রতিরোধ:** AI এজেন্টকে শুধুমাত্র প্রয়োজনীয় ভিত্তিতে সিস্টেমে অ্যাক্সেস দেওয়া উচিত যাতে এই ধরনের আক্রমণ প্রতিরোধ করা যায়। এজেন্ট এবং সিস্টেমের মধ্যে যোগাযোগও নিরাপদ হওয়া উচিত। প্রমাণীকরণ এবং অ্যাক্সেস নিয়ন্ত্রণ প্রয়োগ করাও এই তথ্য রক্ষার একটি উপায়।

### রিসোর্স এবং পরিষেবা অতিরিক্ত ব্যবহার

**বর্ণনা:** AI এজেন্ট বিভিন্ন টুল এবং পরিষেবায় অ্যাক্সেস করতে পারে কাজ সম্পন্ন করার জন্য। আক্রমণকারীরা এই ক্ষমতা ব্যবহার করে AI এজেন্টের মাধ্যমে উচ্চ সংখ্যক অনুরোধ পাঠিয়ে এই পরিষেবাগুলোতে আক্রমণ করতে পারে, যা সিস্টেম ব্যর্থতা বা উচ্চ খরচের কারণ হতে পারে।

**প্রতিরোধ:** AI এজেন্ট একটি পরিষেবায় কতটি অনুরোধ করতে পারে তার সীমা নির্ধারণের নীতি প্রয়োগ করুন। কথোপকথনের টার্ন সংখ্যা এবং AI এজেন্টের অনুরোধ সীমিত করাও এই ধরনের আক্রমণ প্রতিরোধের একটি উপায়।

### জ্ঞানভাণ্ডার বিষক্রিয়া

**বর্ণনা:** এই ধরনের আক্রমণ সরাসরি AI এজেন্টকে লক্ষ্য করে না বরং জ্ঞানভাণ্ডার এবং অন্যান্য পরিষেবাগুলোকে লক্ষ্য করে যা AI এজেন্ট ব্যবহার করবে। এটি এমন ডেটা বা তথ্যকে দূষিত করতে পারে যা AI এজেন্ট কাজ সম্পন্ন করতে ব্যবহার করবে, যা ব্যবহারকারীর কাছে পক্ষপাতদুষ্ট বা অনাকাঙ্ক্ষিত প্রতিক্রিয়া সৃষ্টি করতে পারে।

**প্রতিরোধ:** AI এজেন্ট তার কার্যপ্রবাহে যে ডেটা ব্যবহার করবে তার নিয়মিত যাচাই করুন। এই ডেটায় অ্যাক্সেস নিরাপদ করুন এবং শুধুমাত্র বিশ্বস্ত ব্যক্তিদের দ্বারা পরিবর্তন নিশ্চিত করুন যাতে এই ধরনের আক্রমণ এড়ানো যায়।

### ক্রমবর্ধমান ত্রুটি

**বর্ণনা:** AI এজেন্ট বিভিন্ন টুল এবং পরিষেবায় অ্যাক্সেস করে কাজ সম্পন্ন করে। আক্রমণকারীদের দ্বারা সৃষ্ট ত্রুটি অন্যান্য সিস্টেমের ব্যর্থতার কারণ হতে পারে, যা AI এজেন্টের সাথে সংযুক্ত থাকে। এর ফলে আক্রমণ আরও বিস্তৃত এবং সমাধান করা কঠিন হয়ে যেতে পারে।

**প্রতিরোধ:** এটি এড়ানোর একটি পদ্ধতি হলো AI এজেন্টকে একটি সীমিত পরিবেশে পরিচালনা করা, যেমন ডকার কন্টেইনারে কাজ সম্পন্ন করা, যাতে সরাসরি সিস্টেম আক্রমণ প্রতিরোধ করা যায়। নির্দিষ্ট সিস্টেম ত্রুটির প্রতিক্রিয়ায় ব্যাকআপ ব্যবস্থা এবং পুনরায় চেষ্টা করার লজিক তৈরি করাও বড় সিস্টেম ব্যর্থতা প্রতিরোধের একটি উপায়।

## মানব-নিয়ন্ত্রিত প্রক্রিয়া

বিশ্বাসযোগ্য AI এজেন্ট সিস্টেম তৈরি করার আরেকটি কার্যকর উপায় হলো মানব-নিয়ন্ত্রিত প্রক্রিয়া ব্যবহার করা। এটি এমন একটি প্রবাহ তৈরি করে যেখানে ব্যবহারকারীরা এজেন্টের কার্যক্রম চলাকালীন প্রতিক্রিয়া প্রদান করতে পারে। ব্যবহারকারীরা মূলত একটি বহু-এজেন্ট সিস্টেমে এজেন্ট হিসেবে কাজ করে এবং চলমান প্রক্রিয়ার অনুমোদন বা বন্ধ করার ক্ষমতা রাখে।

![Human in The Loop](../../../translated_images/human-in-the-loop.5f0068a678f62f4fc8373d5b78c4c22f35d9e4da35c93f66c3b634c1774eff34.bn.png)

এখানে AutoGen ব্যবহার করে এই ধারণা বাস্তবায়নের একটি কোড স্নিপেট দেওয়া হলো:

```python

# Create the agents.
model_client = OpenAIChatCompletionClient(model="gpt-4o-mini")
assistant = AssistantAgent("assistant", model_client=model_client)
user_proxy = UserProxyAgent("user_proxy", input_func=input)  # Use input() to get user input from console.

# Create the termination condition which will end the conversation when the user says "APPROVE".
termination = TextMentionTermination("APPROVE")

# Create the team.
team = RoundRobinGroupChat([assistant, user_proxy], termination_condition=termination)

# Run the conversation and stream to the console.
stream = team.run_stream(task="Write a 4-line poem about the ocean.")
# Use asyncio.run(...) when running in a script.
await Console(stream)

```

## উপসংহার

বিশ্বাসযোগ্য AI এজেন্ট তৈরি করতে হলে যত্নশীল ডিজাইন, শক্তিশালী নিরাপত্তা ব্যবস্থা এবং ধারাবাহিক পুনরাবৃত্তি প্রয়োজন। গঠনমূলক মেটা প্রম্পটিং সিস্টেম প্রয়োগ করে, সম্ভাব্য হুমকি বোঝা এবং প্রতিরোধ কৌশল প্রয়োগ করে, ডেভেলপাররা নিরাপদ এবং কার্যকরী AI এজেন্ট তৈরি করতে পারে। এছাড়াও, মানব-নিয়ন্ত্রিত প্রক্রিয়া অন্তর্ভুক্ত করা নিশ্চিত করে যে AI এজেন্ট ব্যবহারকারীর প্রয়োজনের সাথে সামঞ্জস্যপূর্ণ থাকে এবং ঝুঁকি কমায়। AI ক্রমাগত উন্নত হওয়ার সাথে সাথে নিরাপত্তা, গোপনীয়তা এবং নৈতিক বিষয়গুলোতে সক্রিয় মনোভাব বজায় রাখা AI-চালিত সিস্টেমে বিশ্বাস এবং নির্ভরযোগ্যতা গড়ে তোলার চাবিকাঠি হবে।

### বিশ্বাসযোগ্য AI এজেন্ট তৈরির বিষয়ে আরও প্রশ্ন আছে?

[Azure AI Foundry Discord](https://aka.ms/ai-agents/discord)-এ যোগ দিন, অন্যান্য শিক্ষার্থীদের সাথে যোগাযোগ করুন, অফিস আওয়ারে অংশগ্রহণ করুন এবং আপনার AI এজেন্ট সম্পর্কিত প্রশ্নের উত্তর পান।

## অতিরিক্ত সম্পদ

- <a href="https://learn.microsoft.com/azure/ai-studio/responsible-use-of-ai-overview" target="_blank">Responsible AI overview</a>
- <a href="https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai" target="_blank">Evaluation of generative AI models and AI applications</a>
- <a href="https://learn.microsoft.com/azure/ai-services/openai/concepts/system-message?context=%2Fazure%2Fai-studio%2Fcontext%2Fcontext&tabs=top-techniques" target="_blank">Safety system messages</a>
- <a href="https://blogs.microsoft.com/wp-content/uploads/prod/sites/5/2022/06/Microsoft-RAI-Impact-Assessment-Template.pdf?culture=en-us&country=us" target="_blank">Risk Assessment Template</a>

## পূর্ববর্তী পাঠ

[Agentic RAG](../05-agentic-rag/README.md)

## পরবর্তী পাঠ

[Planning Design Pattern](../07-planning-design/README.md)

---

**অস্বীকৃতি**:  
এই নথিটি AI অনুবাদ পরিষেবা [Co-op Translator](https://github.com/Azure/co-op-translator) ব্যবহার করে অনুবাদ করা হয়েছে। আমরা যথাসম্ভব সঠিক অনুবাদের চেষ্টা করি, তবে অনুগ্রহ করে মনে রাখবেন যে স্বয়ংক্রিয় অনুবাদে ত্রুটি বা অসঙ্গতি থাকতে পারে। নথিটির মূল ভাষায় রচিত সংস্করণটিকেই প্রামাণিক উৎস হিসেবে বিবেচনা করা উচিত। গুরুত্বপূর্ণ তথ্যের জন্য পেশাদার মানব অনুবাদ ব্যবহার করার পরামর্শ দেওয়া হচ্ছে। এই অনুবাদ ব্যবহারের ফলে সৃষ্ট কোনো ভুল বোঝাবুঝি বা ভুল ব্যাখ্যার জন্য আমরা দায়ী নই।