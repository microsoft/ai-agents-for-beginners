# মাইক্রোসফ্ট ফাউন্ড্রি এজেন্ট সার্ভিস ডেভেলপমেন্ট

এই অনুশীলনে, আপনি মাইক্রোসফ্ট ফাউন্ড্রি এজেন্ট সার্ভিস টুলগুলি [Microsoft Foundry portal](https://ai.azure.com/?WT.mc_id=academic-105485-koreyst)-এ ব্যবহার করে ফ্লাইট বুকিংয়ের জন্য একটি এজেন্ট তৈরি করবেন। এজেন্টটি ব্যবহারকারীদের সাথে ইন্টার‌্যাক্ট করতে এবং ফ্লাইট সম্পর্কে তথ্য প্রদান করতে সক্ষম হবে।

## পূর্বপ্রয়োজনীয়তা

এই অনুশীলন সম্পূর্ণ করার জন্য, আপনাকে নিম্নলিখিতগুলির প্রয়োজন:
১. একটি সক্রিয় সাবস্ক্রিপশনসহ Azure অ্যাকাউন্ট। [বিনামূল্যে একটি অ্যাকাউন্ট তৈরি করুন](https://azure.microsoft.com/free/?WT.mc_id=academic-105485-koreyst)।
২. আপনার মাইক্রোসফ্ট ফাউন্ড্রি হাব তৈরি করার অনুমতি থাকতে হবে অথবা কেউ আপনার জন্য একটি তৈরি করবে।
    - যদি আপনার ভূমিকা Contributor বা Owner হয়, তবে আপনি এই টিউটোরিয়ালের ধাপগুলি অনুসরণ করতে পারেন।

## একটি মাইক্রোসফ্ট ফাউন্ড্রি হাব তৈরি করুন

> **নোট:** মাইক্রোসফ্ট ফাউন্ড্রি পূর্বে Azure AI Studio নামে পরিচিত ছিল।

১. মাইক্রোসফ্ট ফাউন্ড্রি ব্লগ পোস্ট থেকে [Microsoft Foundry](https://learn.microsoft.com/en-us/azure/ai-studio/?WT.mc_id=academic-105485-koreyst) হাব তৈরির নির্দেশিকা অনুসরণ করুন।
২. যখন আপনার প্রকল্প তৈরি হয়ে যাবে, প্রদর্শিত যেকোনো টিপস বন্ধ করে Microsoft Foundry পোর্টালের প্রকল্প পৃষ্ঠা পর্যালোচনা করুন, এটি নিম্নলিখিত ছবির মতো দেখতে হবে:

    ![Microsoft Foundry Project](../../../translated_images/bn/azure-ai-foundry.88d0c35298348c2f.webp)

## একটি মডেল স্থাপন করুন

১. আপনার প্রকল্পের বামদিকের প্যানেলে, **My assets** বিভাগে **Models + endpoints** পৃষ্ঠা নির্বাচন করুন।
২. **Models + endpoints** পৃষ্ঠায়, **Model deployments** ট্যাবে, **+ Deploy model** মেনু থেকে **Deploy base model** নির্বাচন করুন।
৩. তালিকায় `gpt-5-mini` মডেলটি খুঁজুন, তারপর সেটি নির্বাচন করে নিশ্চিত করুন।

    > **নোট**: TPM কমানো সাবস্ক্রিপশনে উপলব্ধ কোটা অতিরিক্ত ব্যবহারের থেকে রক্ষা করে।

    ![Model Deployed](../../../translated_images/bn/model-deployment.3749c53fb81e18fd.webp)

## একটি এজেন্ট তৈরি করুন

এখন যেহেতু আপনি একটি মডেল স্থাপন করেছেন, আপনি একটি এজেন্ট তৈরি করতে পারেন। এজেন্ট হল একটি কথোপকথনমূলক AI মডেল যা ব্যবহারকারীদের সাথে যোগাযোগ করতে পারে।

১. আপনার প্রকল্পের বামদিকের প্যানেলে, **Build & Customize** বিভাগে **Agents** পৃষ্ঠা নির্বাচন করুন।
২. নতুন এজেন্ট তৈরি করতে **+ Create agent** তে ক্লিক করুন। **Agent Setup** ডায়ালগ বাক্সের নিচে:
    - এজেন্টের জন্য একটি নাম দিন, যেমন `FlightAgent`।
    - নিশ্চিত করুন যে আপনি পূর্বে তৈরি করা `gpt-5-mini` মডেল ডিপ্লয়মেন্ট নির্বাচন করেছেন
    - এজেন্টকে অনুসরণ করার জন্য ইনস্ট্রাকশান সেট করুন। এখানে একটি উদাহরণ:
    ```
    You are FlightAgent, a virtual assistant specialized in handling flight-related queries. Your role includes assisting users with searching for flights, retrieving flight details, checking seat availability, and providing real-time flight status. Follow the instructions below to ensure clarity and effectiveness in your responses:

    ### Task Instructions:
    1. **Recognizing Intent**:
       - Identify the user's intent based on their request, focusing on one of the following categories:
         - Searching for flights
         - Retrieving flight details using a flight ID
         - Checking seat availability for a specified flight
         - Providing real-time flight status using a flight number
       - If the intent is unclear, politely ask users to clarify or provide more details.
        
    2. **Processing Requests**:
        - Depending on the identified intent, perform the required task:
        - For flight searches: Request details such as origin, destination, departure date, and optionally return date.
        - For flight details: Request a valid flight ID.
        - For seat availability: Request the flight ID and date and validate inputs.
        - For flight status: Request a valid flight number.
        - Perform validations on provided data (e.g., formats of dates, flight numbers, or IDs). If the information is incomplete or invalid, return a friendly request for clarification.

    3. **Generating Responses**:
    - Use a tone that is friendly, concise, and supportive.
    - Provide clear and actionable suggestions based on the output of each task.
    - If no data is found or an error occurs, explain it to the user gently and offer alternative actions (e.g., refine search, try another query).
    
    ```
> [!NOTE]
> বিস্তারিত প্রাম্পটের জন্য, আপনি আরও তথ্যের জন্য [এই রেপোজিটরি](https://github.com/ShivamGoyal03/RoamMind) দেখতে পারেন।
    
> এছাড়াও, আপনি এজেন্টের ক্ষমতা বাড়াতে **Knowledge Base** এবং **Actions** যুক্ত করতে পারেন যাতে ব্যবহারকারীর অনুরোধ অনুসারে আরও তথ্য প্রদান এবং স্বয়ংক্রিয় কাজগুলি সম্পন্ন করা যায়। এই অনুশীলনের জন্য, আপনি এই ধাপগুলি বাদ দিতে পারেন।
    
![Agent Setup](../../../translated_images/bn/agent-setup.9bbb8755bf5df672.webp)

৩. নতুন একটি মাল্টি-AI এজেন্ট তৈরি করতে, কেবলমাত্র **New Agent** তে ক্লিক করুন। নতুন তৈরি এজেন্টটি Agents পৃষ্ঠায় প্রদর্শিত হবে।


## এজেন্ট পরীক্ষা করুন

এজেন্ট তৈরি করার পর, আপনি Microsoft Foundry পোর্টালের প্লেগ্রাউন্ডে ব্যবহারকারীর প্রশ্নের বিরুদ্ধে এটি কীভাবে সাড়া দেয় তা পরীক্ষা করতে পারেন।

১. আপনার এজেন্টের **Setup** প্যানেলের উপরের অংশে **Try in playground** নির্বাচন করুন।
২. **Playground** প্যানেলে, আপনি চ্যাট উইন্ডোতে প্রশ্ন টাইপ করে এজেন্টের সাথে ইন্টার‌্যাক্ট করতে পারেন। উদাহরণস্বরূপ, এজেন্টকে জিজ্ঞাসা করতে পারেন ২৮ তারিখে সিয়াটল থেকে নিউ ইয়র্ক-এর ফ্লাইট খোঁজার জন্য।

    > **নোট**: এই অনুশীলনে কোনো রিয়েল-টাইম ডেটা ব্যবহার করা হচ্ছে না, তাই এজেন্ট সঠিক উত্তর নাও দিতে পারে। উদ্দেশ্য হল এজেন্টের ব্যবহারকারীর প্রশ্ন বোঝার এবং প্রদত্ত নির্দেশাবলীর ভিত্তিতে সাড়া দেওয়ার ক্ষমতা পরীক্ষা করা।

    ![Agent Playground](../../../translated_images/bn/agent-playground.dc146586de715010.webp)

৩. এজেন্ট পরীক্ষা করার পর, আপনি এর সক্ষমতা বাড়াতে আরো intents, প্রশিক্ষণ ডেটা এবং actions যোগ করে এটি আরও কাস্টমাইজ করতে পারেন।

## সংস্থান পরিষ্কার করুন

পরীক্ষার কাজ শেষ হলে, অতিরিক্ত খরচ এড়াতে এজেন্টটি মুছে ফেলতে পারেন।
১. [Azure portal](https://portal.azure.com) খুলুন এবং সেই রিসোর্স গ্রুপের বিষয়বস্তু দেখুন যেখানে আপনি এই অনুশীলনের জন্য ব্যবহৃত হাব রিসোর্স স্থাপন করেছেন।
২. টুলবারে **Delete resource group** নির্বাচন করুন।
৩. রিসোর্স গ্রুপের নাম লিখে এটি মুছে ফেলার নিশ্চিত করুন।

## সংস্থানসমূহ

- [মাইক্রোসফ্ট ফাউন্ড্রি ডকুমেন্টেশন](https://learn.microsoft.com/en-us/azure/ai-studio/?WT.mc_id=academic-105485-koreyst)
- [মাইক্রোসফ্ট ফাউন্ড্রি পোর্টাল](https://ai.azure.com/?WT.mc_id=academic-105485-koreyst)
- [মাইক্রোসফ্ট ফাউন্ড্রি নিয়ে শুরু করা](https://techcommunity.microsoft.com/blog/educatordeveloperblog/getting-started-with-azure-ai-studio/4095602?WT.mc_id=academic-105485-koreyst)
- [Azure তে AI এজেন্টের মৌলিক বিষয়](https://learn.microsoft.com/en-us/training/modules/ai-agent-fundamentals/?WT.mc_id=academic-105485-koreyst)
- [Azure AI Discord](https://aka.ms/AzureAI/Discord)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**অস্বীকৃতি**:
এই নথিটি AI অনুবাদ পরিষেবা [Co-op Translator](https://github.com/Azure/co-op-translator) ব্যবহার করে অনূদিত হয়েছে। যদিও আমরা শুদ্ধতার জন্য চেষ্টা করি, অনুগ্রহ করে মনে রাখবেন যে স্বয়ংক্রিয় অনুবাদে ত্রুটি বা অসঙ্গতি থাকতে পারে। মূল নথিটি তার স্বভাষায় কর্তৃত্বপূর্ণ উৎস হিসেবে বিবেচিত হওয়া উচিত। গুরুত্বপূর্ণ তথ্যের জন্য পেশাদার মানব অনুবাদ সুপারিশ করা হয়। এই অনুবাদের ব্যবহারে প্রয়োজনীয় ভুল বোঝাবুঝি বা ভুল ব্যাখ্যার জন্য আমরা দায়বদ্ধ নই।
<!-- CO-OP TRANSLATOR DISCLAIMER END -->