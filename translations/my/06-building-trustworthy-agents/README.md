<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "498802b4c3c3cc486b86f27a12cebb34",
  "translation_date": "2025-08-29T23:57:36+00:00",
  "source_file": "06-building-trustworthy-agents/README.md",
  "language_code": "my"
}
-->
[![Trustworthy AI Agents](../../../translated_images/lesson-6-thumbnail.a58ab36c099038d4f786c2b0d5d6e89f41f4c2ecc05ab10b67bced2695eeb218.my.png)](https://youtu.be/iZKkMEGBCUQ?si=Q-kEbcyHUMPoHp8L)

> _(အထက်ပါပုံကိုနှိပ်ပြီး ဒီသင်ခန်းစာရဲ့ ဗီဒီယိုကို ကြည့်ပါ)_

# ယုံကြည်စိတ်ချရသော AI အေးဂျင့်များ တည်ဆောက်ခြင်း

## မိတ်ဆက်

ဒီသင်ခန်းစာမှာ အောက်ပါအကြောင်းအရာများကို လေ့လာပါမည်-

- ဘယ်လိုအကောင်းဆုံးနှင့် လုံခြုံသော AI အေးဂျင့်များကို တည်ဆောက်ပြီး အသုံးချရမည်။
- AI အေးဂျင့်များ ဖွံ့ဖြိုးတိုးတက်စဉ်တွင် လုံခြုံရေးအရေးပါချက်များ။
- AI အေးဂျင့်များ ဖွံ့ဖြိုးတိုးတက်စဉ်တွင် ဒေတာနှင့် အသုံးပြုသူ၏ ကိုယ်ရေးအချက်အလက် လုံခြုံရေးကို ဘယ်လိုထိန်းသိမ်းရမည်။

## သင်ယူရမည့်ရည်မှန်းချက်များ

ဒီသင်ခန်းစာပြီးဆုံးပြီးနောက်မှာ-

- AI အေးဂျင့်များ ဖန်တီးရာတွင် ဖြစ်နိုင်သော အန္တရာယ်များကို သတ်မှတ်ပြီး လျှော့ချနိုင်မည်။
- ဒေတာနှင့် ဝင်ရောက်ခွင့်ကို သေချာစွာ စီမံခန့်ခွဲရန် လုံခြုံရေးအတိုင်းအတာများကို အကောင်အထည်ဖော်နိုင်မည်။
- ဒေတာလုံခြုံရေးကို ထိန်းသိမ်းပြီး အသုံးပြုသူအတွေ့အကြုံကောင်းများ ပေးစွမ်းနိုင်သော AI အေးဂျင့်များ ဖန်တီးနိုင်မည်။

## လုံခြုံရေး

အေးဂျင့်အခြေပြု အက်ပ်လီကေးရှင်းများကို လုံခြုံစွာ တည်ဆောက်ခြင်းကို စတင်လေ့လာကြမည်။ လုံခြုံရေးဆိုသည်မှာ AI အေးဂျင့်သည် ရည်ရွယ်ထားသည့်အတိုင်း လုပ်ဆောင်နိုင်ခြင်းကို ဆိုလိုသည်။ အေးဂျင့်အခြေပြု အက်ပ်လီကေးရှင်းများ ဖန်တီးသူများအနေဖြင့် လုံခြုံရေးကို အများဆုံးမြှင့်တင်ရန် နည်းလမ်းများနှင့် ကိရိယာများ ရှိသည်-

### စနစ်မက်ဆေ့ချ် ဖွဲ့စည်းမှု တည်ဆောက်ခြင်း

သင်သည် Large Language Models (LLMs) ကို အသုံးပြု၍ AI အက်ပ်တစ်ခုကို တည်ဆောက်ဖူးလျှင် စနစ်မက်ဆေ့ချ် (system prompt) သို့မဟုတ် စနစ်မက်ဆေ့ချ်ကို ခိုင်မာစွာ ဒီဇိုင်းဆွဲရန် အရေးကြီးကြောင်း သိလိမ့်မည်။ ဒီမက်ဆေ့ချ်များသည် LLM သည် အသုံးပြုသူနှင့် ဒေတာကို ဘယ်လိုအပြန်အလှန်လုပ်ဆောင်မည်ကို သတ်မှတ်ပေးသော meta စည်းမျဉ်းများ၊ လမ်းညွှန်ချက်များနှင့် လိုက်နာရမည့်အချက်များကို ဖွဲ့စည်းပေးသည်။

AI အေးဂျင့်များအတွက် စနစ်မက်ဆေ့ချ်သည် ပိုမိုအရေးကြီးသည်။ အေးဂျင့်များသည် ကျွန်ုပ်တို့ဒီဇိုင်းဆွဲထားသော တာဝန်များကို ပြည့်စုံစွာ လုပ်ဆောင်ရန် အလွန်သေချာသော လမ်းညွှန်ချက်များလိုအပ်သည်။

စနစ်မက်ဆေ့ချ်များကို အကျိုးရှိစွာ တည်ဆောက်ရန်အတွက် ကျွန်ုပ်တို့သည် အက်ပ်လီကေးရှင်းတွင် အေးဂျင့်များ တစ်ခု သို့မဟုတ် အများအပြားကို တည်ဆောက်ရန် စနစ်မက်ဆေ့ချ် ဖွဲ့စည်းမှုကို အသုံးပြုနိုင်သည်-

![Building a System Message Framework](../../../translated_images/system-message-framework.3a97368c92d11d6814577b03cd128ec8c71a5fd1e26f341835cfa5df59ae87ae.my.png)

#### အဆင့် ၁- Meta စနစ်မက်ဆေ့ချ် တစ်ခု ဖန်တီးပါ

Meta prompt ကို LLM သုံးပြီး ကျွန်ုပ်တို့ဖန်တီးလိုသော အေးဂျင့်များအတွက် စနစ်မက်ဆေ့ချ်များကို ဖန်တီးရန် အသုံးပြုမည်။ ကျွန်ုပ်တို့သည် template အဖြစ် ဒီဇိုင်းဆွဲထားပြီး လိုအပ်ပါက အေးဂျင့်များ အများအပြားကို အကျိုးရှိစွာ ဖန်တီးနိုင်သည်။

ဤသည်မှာ LLM ကို ပေးမည့် meta စနစ်မက်ဆေ့ချ်၏ ဥပမာဖြစ်သည်-

```plaintext
You are an expert at creating AI agent assistants. 
You will be provided a company name, role, responsibilities and other
information that you will use to provide a system prompt for.
To create the system prompt, be descriptive as possible and provide a structure that a system using an LLM can better understand the role and responsibilities of the AI assistant. 
```

#### အဆင့် ၂- အခြေခံ prompt တစ်ခု ဖန်တီးပါ

နောက်တစ်ဆင့်မှာ AI အေးဂျင့်ကို ဖော်ပြရန် အခြေခံ prompt တစ်ခု ဖန်တီးခြင်းဖြစ်သည်။ အေးဂျင့်၏ အခန်းကဏ္ဍ၊ အေးဂျင့်၏ လုပ်ဆောင်မည့် တာဝန်များနှင့် အေးဂျင့်၏ တာဝန်ဝတ္တရားများကို ထည့်သွင်းဖော်ပြရမည်။

ဤသည်မှာ ဥပမာတစ်ခုဖြစ်သည်-

```plaintext
You are a travel agent for Contoso Travel that is great at booking flights for customers. To help customers you can perform the following tasks: lookup available flights, book flights, ask for preferences in seating and times for flights, cancel any previously booked flights and alert customers on any delays or cancellations of flights.  
```

#### အဆင့် ၃- LLM ကို အခြေခံစနစ်မက်ဆေ့ချ် ပေးပါ

ယခု meta စနစ်မက်ဆေ့ချ်ကို စနစ်မက်ဆေ့ချ်အဖြစ်ပေးပြီး ကျွန်ုပ်တို့၏ အခြေခံစနစ်မက်ဆေ့ချ်ကို ထည့်သွင်းခြင်းဖြင့် ဒီစနစ်မက်ဆေ့ချ်ကို အကောင်းဆုံး optimize လုပ်နိုင်သည်။

ဤသည်မှာ AI အေးဂျင့်များကို လမ်းညွှန်ရန် ပိုမိုကောင်းမွန်သော စနစ်မက်ဆေ့ချ်ကို ဖန်တီးပေးမည်-

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

#### အဆင့် ၄- Iteration နှင့် တိုးတက်မှု

ဒီစနစ်မက်ဆေ့ချ် ဖွဲ့စည်းမှု၏ အကျိုးကျေးဇူးမှာ အေးဂျင့်များ အများအပြားကို အလွယ်တကူ ဖန်တီးနိုင်ရန်နှင့် စနစ်မက်ဆေ့ချ်များကို အချိန်ကြာမြင့်စွာ တိုးတက်အောင် လုပ်ဆောင်နိုင်ရန် ဖြစ်သည်။ သင့်ရဲ့ လိုအပ်ချက်များအတွက် ပထမဆုံးစနစ်မက်ဆေ့ချ်သည် အပြည့်အဝအလုပ်လုပ်မည်ဟု မျှော်လင့်ရခက်သည်။ အခြေခံစနစ်မက်ဆေ့ချ်ကို ပြောင်းလဲခြင်းနှင့် စနစ်ကို ပြန်လည်လုပ်ဆောင်ခြင်းဖြင့် ရလဒ်များကို နှိုင်းယှဉ်ပြီး အကဲဖြတ်နိုင်သည်။

## အန္တရာယ်များကို နားလည်ခြင်း

ယုံကြည်စိတ်ချရသော AI အေးဂျင့်များကို တည်ဆောက်ရန် အေးဂျင့်၏ အန္တရာယ်များနှင့် ခြိမ်းခြောက်မှုများကို နားလည်ပြီး လျှော့ချရန် လိုအပ်သည်။ အေးဂျင့်များကို ပိုမိုကောင်းမွန်စွာ စီမံဆောင်ရွက်နိုင်ရန် အန္တရာယ်များအချို့ကို လေ့လာကြမည်-

![Understanding Threats](../../../translated_images/understanding-threats.89edeada8a97fc0f7053558567d5dd27c0c333b74e47fffdde490fa6777a4c17.my.png)

### တာဝန်နှင့် လမ်းညွှန်ချက်

**ဖော်ပြချက်:** တိုက်ခိုက်သူများသည် AI အေးဂျင့်၏ လမ်းညွှန်ချက်များ သို့မဟုတ် ရည်မှန်းချက်များကို prompt သို့မဟုတ် input များကို ပြောင်းလဲခြင်းဖြင့် ပြောင်းလဲရန် ကြိုးစားသည်။

**လျှော့ချနည်းလမ်း:** AI အေးဂျင့်မှ အဆောင်ရွက်မပြုမီ အန္တရာယ်ရှိနိုင်သော prompt များကို ရှာဖွေဖော်ထုတ်ရန် validation checks နှင့် input filters ကို အသုံးပြုပါ။ ဒီတိုက်ခိုက်မှုများသည် အေးဂျင့်နှင့် မကြာခဏ အပြန်အလှန်လုပ်ဆောင်ရန် လိုအပ်သောကြောင့် စကားဝိုင်းတွင် ပြောဆိုမှုအကြိမ်ရေကို ကန့်သတ်ခြင်းသည် ဒီတိုက်ခိုက်မှုများကို ကာကွယ်ရန် နည်းလမ်းတစ်ခုဖြစ်သည်။

### အရေးပါသော စနစ်များသို့ ဝင်ရောက်ခွင့်

**ဖော်ပြချက်:** AI အေးဂျင့်သည် အရေးပါသော ဒေတာကို သိမ်းဆည်းထားသော စနစ်များနှင့် ဝန်ဆောင်မှုများသို့ ဝင်ရောက်ခွင့်ရှိပါက တိုက်ခိုက်သူများသည် အေးဂျင့်နှင့် ဒီဝန်ဆောင်မှုများအကြား ဆက်သွယ်မှုကို ချိုးဖောက်နိုင်သည်။ ဒါဟာ တိုက်ရိုက်တိုက်ခိုက်မှုများ သို့မဟုတ် အေးဂျင့်မှ ဒီစနစ်များအကြောင်း အချက်အလက်ရယူရန် ကြိုးစားမှုများ ဖြစ်နိုင်သည်။

**လျှော့ချနည်းလမ်း:** AI အေးဂျင့်များသည် ဒီတိုက်ခိုက်မှုများကို ကာကွယ်ရန် လိုအပ်သောအခါမှသာ စနစ်များသို့ ဝင်ရောက်ခွင့်ရှိရမည်။ အေးဂျင့်နှင့် စနစ်အကြား ဆက်သွယ်မှုကို လုံခြုံစွာ ဆောင်ရွက်ရမည်။ Authentication နှင့် access control ကို အကောင်အထည်ဖော်ခြင်းသည် ဒီအချက်အလက်ကို ကာကွယ်ရန် နည်းလမ်းတစ်ခုဖြစ်သည်။

### အရင်းအမြစ်နှင့် ဝန်ဆောင်မှုများ အလွန်အကျွံအသုံးပြုခြင်း

**ဖော်ပြချက်:** AI အေးဂျင့်များသည် တာဝန်များကို ပြည့်စုံစွာ လုပ်ဆောင်ရန် ကိရိယာများနှင့် ဝန်ဆောင်မှုများကို ဝင်ရောက်အသုံးပြုနိုင်သည်။ တိုက်ခိုက်သူများသည် AI အေးဂျင့်မှ တဆင့် ဒီဝန်ဆောင်မှုများကို တိုက်ခိုက်ရန် အလွန်အကျွံတောင်းဆိုမှုများ ပေးပို့နိုင်ပြီး စနစ်ချို့ယွင်းမှုများ သို့မဟုတ် ကုန်ကျစရိတ်များ မြင့်မားစေနိုင်သည်။

**လျှော့ချနည်းလမ်း:** AI အေးဂျင့်သည် ဝန်ဆောင်မှုတစ်ခုသို့ တောင်းဆိုမှုအရေအတွက်ကို ကန့်သတ်ရန် မူဝါဒများကို အကောင်အထည်ဖော်ပါ။ AI အေးဂျင့်နှင့် စကားဝိုင်းတွင် ပြောဆိုမှုအကြိမ်ရေကို ကန့်သတ်ခြင်းသည် ဒီတိုက်ခိုက်မှုများကို ကာကွယ်ရန် နည်းလမ်းတစ်ခုဖြစ်သည်။

### Knowledge Base Poisoning

**ဖော်ပြချက်:** ဒီတိုက်ခိုက်မှုသည် AI အေးဂျင့်ကို တိုက်ရိုက်မပစ်မှတ်ထားပါဘဲ AI အေးဂျင့်မှ အသုံးပြုမည့် knowledge base နှင့် အခြားဝန်ဆောင်မှုများကို ပစ်မှတ်ထားသည်။ ဒါဟာ AI အေးဂျင့်မှ တာဝန်တစ်ခုကို ပြည့်စုံစွာ လုပ်ဆောင်ရန် အသုံးပြုမည့် ဒေတာ သို့မဟုတ် အချက်အလက်ကို ချို့ယွင်းစေခြင်းဖြစ်ပြီး အသုံးပြုသူအတွက် bias ဖြစ်စေခြင်း သို့မဟုတ် မရည်ရွယ်ထားသော အဖြေများကို ဖြစ်စေသည်။

**လျှော့ချနည်းလမ်း:** AI အေးဂျင့်မှ workflows တွင် အသုံးပြုမည့် ဒေတာကို အကြိမ်ကြိမ် အတည်ပြုပါ။ ဒီဒေတာကို လုံခြုံစွာ ထိန်းသိမ်းပြီး ယုံကြည်ရသောပုဂ္ဂိုလ်များမှသာ ပြောင်းလဲနိုင်ရန် သေချာပါ။

### Cascading Errors

**ဖော်ပြချက်:** AI အေးဂျင့်များသည် တာဝန်များကို ပြည့်စုံစွာ လုပ်ဆောင်ရန် ကိရိယာများနှင့် ဝန်ဆောင်မှုများကို ဝင်ရောက်အသုံးပြုနိုင်သည်။ တိုက်ခိုက်သူများကြောင့် ဖြစ်ပေါ်သော အမှားများသည် AI အေးဂျင့်နှင့် ဆက်စပ်သော အခြားစနစ်များကို ချို့ယွင်းစေပြီး တိုက်ခိုက်မှုသည် ပိုမိုကျယ်ပြန့်လာပြီး troubleshooting ခက်ခဲစေသည်။

**လျှော့ချနည်းလမ်း:** AI အေးဂျင့်ကို Docker container ကဲ့သို့သော ကန့်သတ်ထားသော ပတ်ဝန်းကျင်တွင် တာဝန်များကို လုပ်ဆောင်ရန် ချမှတ်ခြင်းသည် တိုက်ရိုက်စနစ်တိုက်ခိုက်မှုများကို ကာကွယ်ရန် နည်းလမ်းတစ်ခုဖြစ်သည်။ အချို့သောစနစ်များမှ error ဖြင့် တုံ့ပြန်သောအခါ fallback mechanisms နှင့် retry logic ကို ဖန်တီးခြင်းသည် စနစ်ချို့ယွင်းမှုများကို ကာကွယ်ရန် နည်းလမ်းတစ်ခုဖြစ်သည်။

## Human-in-the-Loop

ယုံကြည်စိတ်ချရသော AI အေးဂျင့်စနစ်များကို တည်ဆောက်ရန် ထိရောက်သော နည်းလမ်းတစ်ခုမှာ Human-in-the-loop ကို အသုံးပြုခြင်းဖြစ်သည်။ ဒီနည်းလမ်းသည် အသုံးပြုသူများကို အေးဂျင့်များ၏ လုပ်ဆောင်မှုအတွင်း feedback ပေးနိုင်ရန် လမ်းကြောင်းတစ်ခု ဖန်တီးပေးသည်။ အသုံးပြုသူများသည် multi-agent system တွင် အေးဂျင့်များအဖြစ် လုပ်ဆောင်ပြီး လုပ်ဆောင်မှုကို အတည်ပြုခြင်း သို့မဟုတ် ရပ်တန့်ခြင်းကို ဆောင်ရွက်နိုင်သည်။

![Human in The Loop](../../../translated_images/human-in-the-loop.5f0068a678f62f4fc8373d5b78c4c22f35d9e4da35c93f66c3b634c1774eff34.my.png)

AutoGen ကို အသုံးပြု၍ ဒီအယူအဆကို အကောင်အထည်ဖော်ထားသော code snippet ဤနေရာတွင် ဖော်ပြထားသည်-

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

## နိဂုံး

ယုံကြည်စိတ်ချရသော AI အေးဂျင့်များကို တည်ဆောက်ရန် သေချာသော ဒီဇိုင်း၊ ခိုင်မာသော လုံခြုံရေးအတိုင်းအတာများနှင့် ဆက်လက်တိုးတက်မှုများ လိုအပ်သည်။ Structured meta prompting systems ကို အကောင်အထည်ဖော်ခြင်း၊ ဖြစ်နိုင်သော ခြိမ်းခြောက်မှုများကို နားလည်ခြင်းနှင့် လျှော့ချရန် နည်းလမ်းများကို အသုံးပြုခြင်းဖြင့် လုံခြုံပြီး ထိရောက်သော AI အေးဂျင့်များကို ဖန်တီးနိုင်သည်။ ထို့အပြင် Human-in-the-loop ကို ထည့်သွင်းခြင်းသည် AI အေးဂျင့်များကို အသုံးပြုသူ၏ လိုအပ်ချက်များနှင့် ကိုက်ညီစေရန်အတွက် အကျိုးရှိစေပြီး အန္တရာယ်များကို လျှော့ချနိုင်သည်။ AI သည် ဆက်လက်တိုးတက်နေသည့်အခါ လုံခြုံရေး၊ ကိုယ်ရေးအချက်အလက်နှင့် စိတ်ပိုင်းဆိုင်ရာအချက်များကို အရေးပါစွာ ထိန်းသိမ်းထားခြင်းသည် AI အခြေပြုစနစ်များတွင် ယုံကြည်မှုနှင့် ယုံကြည်စိတ်ချမှုကို မြှင့်တင်ရန် အရေးပါမည်။

### ယုံကြည်စိတ်ချရသော AI အေးဂျင့်များ တည်ဆောက်ခြင်းနှင့် ပတ်သက်သော မေးခွန်းများ ရှိပါသလား?

[Azure AI Foundry Discord](https://aka.ms/ai-agents/discord) ကို ဝင်ရောက်ပြီး အခြားလေ့လာသူများနှင့် တွေ့ဆုံပါ၊ office hours တွင် ပါဝင်ပါ၊ AI အေးဂျင့်များနှင့် ပတ်သက်သော မေးခွန်းများကို ဖြေရှင်းပါ။

## ထပ်မံသော အရင်းအမြစ်များ

- <a href="https://learn.microsoft.com/azure/ai-studio/responsible-use-of-ai-overview" target="_blank">AI ကို တာဝန်ရှိစွာ အသုံးပြုခြင်းအကြောင်းအရာ</a>
- <a href="https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai" target="_blank">Generative AI မော်ဒယ်များနှင့် AI အက်ပ်များကို အကဲဖြတ်ခြင်း</a>
- <a href="https://learn.microsoft.com/azure/ai-services/openai/concepts/system-message?context=%2Fazure%2Fai-studio%2Fcontext%2Fcontext&tabs=top-techniques" target="_blank">လုံခြုံရေး စနစ်မက်ဆေ့ချ်များ</a>
- <a href="https://blogs.microsoft.com/wp-content/uploads/prod/sites

---

**အကြောင်းကြားချက်**:  
ဤစာရွက်စာတမ်းကို AI ဘာသာပြန်ဝန်ဆောင်မှု [Co-op Translator](https://github.com/Azure/co-op-translator) ကို အသုံးပြု၍ ဘာသာပြန်ထားပါသည်။ ကျွန်ုပ်တို့သည် တိကျမှုအတွက် ကြိုးစားနေပါသော်လည်း၊ အလိုအလျောက် ဘာသာပြန်ခြင်းတွင် အမှားများ သို့မဟုတ် မတိကျမှုများ ပါဝင်နိုင်သည်ကို သတိပြုပါ။ မူရင်းဘာသာစကားဖြင့် ရေးသားထားသော စာရွက်စာတမ်းကို အာဏာရှိသော ရင်းမြစ်အဖြစ် သတ်မှတ်သင့်ပါသည်။ အရေးကြီးသော အချက်အလက်များအတွက် လူ့ဘာသာပြန်ပညာရှင်များမှ ပရော်ဖက်ရှင်နယ် ဘာသာပြန်ခြင်းကို အကြံပြုပါသည်။ ဤဘာသာပြန်ကို အသုံးပြုခြင်းမှ ဖြစ်ပေါ်လာသော အလွဲအမှားများ သို့မဟုတ် အနားယူမှုများအတွက် ကျွန်ုပ်တို့သည် တာဝန်မယူပါ။