[![ယုံကြည်စိတ်ချရသော AI အေးဂျင့်များ](../../../translated_images/my/lesson-6-thumbnail.a58ab36c099038d4.webp)](https://youtu.be/iZKkMEGBCUQ?si=Q-kEbcyHUMPoHp8L)

> _(ဒီသင်ခန်းစာရဲ့ ဗီဒီယိုကို ကြည့်ရန် အပေါ်ကပုံကို နှိပ်ပါ)_

# ယုံကြည်စိတ်ချရသော AI အေးဂျင့်များ တည်ဆောက်ခြင်း

## နိဒါန်း

ဒီသင်ခန်းစာမှာ ဖော်ပြမှာကတော့ -

- ဘယ်လိုလုံခြုံပြီး ထိရောက်တဲ့ AI အေးဂျင့်များကို တည်ဆောက်ပြီး စတင်အသုံးပြုမလဲ
- AI အေးဂျင့်များ ဖန်တီးရာတွင် အရေးကြီးသော လုံခြုံရေး မှတ်ချက်များ
- AI အေးဂျင့်များ ဖန်တီးရာတွင် ဒေတာနှင့် အသုံးပြုသူ စိစစ်မှုကို မည်သို့ထိန်းသိမ်းမလဲ

## သင်ယူရမည့်ရည်မှန်းချက်များ

ဒီသင်ခန်းစာပြီးဆုံးပြီးနောက် သင်သည် -

- AI အေးဂျင့်များ တည်ဆောက်ရာတွင် ဖြစ်နိုင်သော အန္တရာယ်ကို ရှာဖွေပြီး ကာကွယ်နိုင်ပါမည်။
- ဒေတာနှင့် လက်လှမ်းမီမှုကို မှန်ကန်စွာ စီမံခန့်ခွဲရန် လုံခြုံရေး များကို အသုံးပြုနိုင်ပါမည်။
- ဒေတာစိစစ်မှု ထိန်းသိမ်းပြီး တကယ်အသုံးပြုသူအတွေ့အကြုံကောင်းမွန်သော AI အေးဂျင့်များ ဖန်တီးနိုင်ပါမည်။

## လုံခြုံမှု

ရောင့်ရဲသော AI အေးဂျင့်အက်ပလီကေးရှင်းများ တည်ဆောက်ခြင်းကို ပထမဦးဆုံး ကြည့်ကြရအောင်။ လုံခြုံမှုဆိုသည်မှာ AI အေးဂျင့်သည် တာဝန်ကျေစွာ ဆောင်ရွက်ခြင်းကိုဆိုလိုသည်။ AI အေးဂျင့်များကို ဖန်တီးသူများအနေနှင့် လုံခြုံမှုအမြင့်ဆုံးထားရန် နည်းလမ်းနှင့် ကိရိယာများ ရှိသည်။

### စနစ်စာတမ်း Framework တည်ဆောက်ခြင်း

သင် LLM (အကြီးစား ဘာသာစကား မော်ဒယ်) အသုံးပြု၍ AI အက်ပလီကေးရှင်းတစ်ခုဖန်တီးဖူးပါက system prompt သို့မဟုတ် system message ကို ပြုစုပြင်ဆင်ရန် အရေးပါကြောင်း သိရှိပါပြီ။ ဤ prompt များမှာ LLM ကို အသုံးပြုသူ နှင့် ဒေတာတို့နှင့် မည်သည့်နည်းဖြင့် ဆက်သွယ်မည်ဟု meta စည်းမျဉ်း၊ လမ်းညွှန်ချက်များတည်ဆောက်ပါသည်။

AI အေးဂျင့်များအတွက် system prompt သည် ပိုမိုအရေးပါသည်။ သူတို့တွင် တာဝန်ထမ်းဆောင်ရန် အတိအကျ ညွှန်ကြားချက်များလိုအပ်မည်ဖြစ်ပါသည်။

စနစ်တကျ ဖြစ်အောင် စနစ်စာတမ်းထုတ်လုပ်ဖို့ system message framework ကို အသုံးပြုနိုင်ပါသည်။ ဒါက သင်၏ အက်ပလီကေးရှင်းမှာ agent တစ်ခု သို့မဟုတ် များစွာဖန်တီးရာတွင် အထောက်အကူဖြစ်ပါလိမ့်မည်-

![Building a System Message Framework](../../../translated_images/my/system-message-framework.3a97368c92d11d68.webp)

#### အဆင့် ၁: Meta System Message တစ်ခု ဖန်တီးပါ

Meta prompt ကို LLM က system prompt များ ဖန်တီးရန် အသုံးပြုမည်ဖြစ်သည်။ ကျွန်ုပ်တို့သည် template အဖြစ် ဒီ meta prompt ကို ဒီဇိုင်းဆွဲကြပါသည်၊ ထို့ကြောင့် လိုအပ်ပါက agent များစွာကို ထိရောက်စွာ ဖန်တီးနိုင်ပါသည်။

LLM ကို ပေးမည့် meta system message ကို ဥပမာ -

```plaintext
You are an expert at creating AI agent assistants. 
You will be provided a company name, role, responsibilities and other
information that you will use to provide a system prompt for.
To create the system prompt, be descriptive as possible and provide a structure that a system using an LLM can better understand the role and responsibilities of the AI assistant. 
```

#### အဆင့် ၂: အခြေခံ prompt တစ်ခု ဖန်တီးပါ

နောက်တစ်ဆင့်မှာ AI အေးဂျင့်ကို ဖော်ပြရန် အခြေခံ prompt တစ်ခု ဖန်တီးရန် ဖြစ်သည်။ အေးဂျင့်၏ တာဝန်၊ ဆောင်ရွက်မည့်တာဝန်များနှင့် အခြားတာဝန်များ ပါဝင်သင့်သည်။

ဥပမာဖြစ်သော prompt -

```plaintext
You are a travel agent for Contoso Travel that is great at booking flights for customers. To help customers you can perform the following tasks: lookup available flights, book flights, ask for preferences in seating and times for flights, cancel any previously booked flights and alert customers on any delays or cancellations of flights.  
```

#### အဆင့် ၃: အခြေခံ system message ကို LLM ထံ ပေးပါ

ယခုတော့ နည်းလမ်းကို အကောင်းဆုံးလုပ်ရန် meta system message ကို system message အဖြစ်သုံးပြီး အခြေခံ system message နှင့် ပေါင်းထည့်ပေးပါ။

ဒီလိုလုပ်ခြင်းအားဖြင့် AI အေးဂျင့်များကို ဦးတည်ညွှန်ကြားရန် ပိုမိုမှန်ကန်သော system message ရရှိမည်ဖြစ်သည်။

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

#### အဆင့် ၄: ပြန်လည်ပြင်ဆင်၍ တိုးတက်အောင်လုပ်ပါ

ဒီ system message framework ၏ အရေးပါမှုမှာ agent များစွာမှ system message များကို ပိုမိုလွယ်ကူစွာ ဖန်တီးနိုင်ခြင်းနှင့် နေ့စဉ်တိုးတက်မှုအတွက် ဖြစ်သည်။ ပထမဆုံးကြိမ်မှာ စနစ်တကျ အလုပ်လုပ်မည့် system message ရှိခြင်း မကြာခဏ မတွေ့ရပါ။ ဒါကြောင့် အခြေခံ system message ကို ပြင်ဆင်၍ system မှတဆင့် ပြန်လည်ဗဟိုပြုနိုင်မှု၊ တိုးတက်အောင်လုပ်နိုင်မှုကောင်းမွန်သည်။

## အန္တရာယ်များနားလည်ခြင်း

ယုံကြည်စိတ်ချရသော AI အေးဂျင့်များ ဖန်တီးရန်အတွက် AI agent ကို ဖြစ်နိုင်သော အန္တရာယ်များနှင့် တိုက်ရိုက်သက်ရောက်မှုများကိုနားလည်ပြီး ကာကွယ်ရန် အရေးပါသည်။ AI အေးဂျင့်များကို ထိခိုက်မှု အမျိုးမျိုးရှိပြီး အောက်တွင် တချို့သာဖော်ပြထားသည်၊ မည်သို့ကောင်းစွာ စီမံကိန်းဆွဲပြီး ပြင်ဆင်နိုင်မလဲကြည့်လိုက်ပါစို့။

![Understanding Threats](../../../translated_images/my/understanding-threats.89edeada8a97fc0f.webp)

### တာဝန်နှင့် ညွှန်ကြားချက်

**ဖော်ပြချက်**: တိုက်ခိုက်သူများသည် prompt သို့မဟုတ် input များကို ချိန်ဆ ပြင်ဆင်ခြင်းဖြင့် AI အေးဂျင့်၏ လုပ်ဆောင်ရမည့် တာဝန်များ သို့မဟုတ် ရည်မှန်းချက်များ ပြောင်းလဲရန် ကြိုးပမ်းသည်။

**ကာကွယ်မှု**: AI အေးဂျင့် အလုပ်မစတင်မီ အန္တရာယ်ရှိနိုင်သည့် prompt များကို စစ်ဆေးဖော်ထုတ်ရန် နဲ့ input filter များ ပြုလုပ်ပါ။ ဤတိုက်ခိုက်မှုများသည် conversation turns များများမလုပ်နိုင်ပဲ ရပ်တန့်ရန် conversation တွင် turns အရေအတွက်ကန့်သတ်ခြင်းပြုနိုင်သည်။

### အရေးကြီးစနစ်များထဲ ဝင်ရောက်ခြင်း

**ဖော်ပြချက်**: AI အေးဂျင့်သည် စနစ်နှင့် ဝန်ဆောင်မှုများတွင် ဝင်ရောက်ခွင့်ရှိပြီး ဤနေရာတွင် အရေးကြီး ဒေတာများ သိမ်းဆည်းထားပါက၊ တိုက်ခိုက်သူများသည် agent နှင့် service များအကြား ဆက်သွယ်မှုကို ထိန်းချုပ်နိုင်သည်။ ၎င်းမှာ တိုက်ရိုက်တိုက်ခိုက်မှု သို့မဟုတ် system များအားဖြင့် အသေးစိတ် အချက်အလက် ရယူရန် ကြိုးပမ်းမှုဖြစ်နိုင်သည်။

**ကာကွယ်မှု**: AI agents များကို လိုအပ်သည့် စနစ်များအတွက်သာ ဝင်ရောက်ခွင့်ပေးရန်၊ agent နှင့် စနစ်အကြား ဆက်သွယ်မှုလည်း လုံခြုံစေဖို့ ခွင့်ပြုပါ။ အတည်ပြုမှုနှင့် ဝင်ရောက်ခွင့်ထိန်းချုပ်မှုများ ထည့်သွင်းဆောင်ရွက်ရန်။

### အရင်းအမြစ်နှင့် ဝန်ဆောင်မှုများ အလေးချိန်ကျန်မြန်

**ဖော်ပြချက်**: AI အေးဂျင့်များသည် သတ်မှတ်အရာလုပ်ရန် ကိရိယာများနှင့် ဝန်ဆောင်မှုများ အသုံးပြုနိုင်ပါသည်။ တိုက်ခိုက်သူများသည် AI အေးဂျင့်မှတဆင့် တောင်းဆိုမှုများ အများအပြားပေးပို့ကာ ဝန်ဆောင်မှုများကို အလေးချိန်လုပ်စေရာ ဖြစ်စေသည်။ ဒေသခံစနစ် မတည်မြဲခြင်း သို့မဟုတ် အနှုန်းအများကြီး ဖြစ်စေသည်။

**ကာကွယ်မှု**: AI အေးဂျင့်မှ ဝန်ဆောင်မှုထံ တောင်းဆိုခြင်း အရေအတွက် ကန့်သတ်ရန် မူဝါဒများ ထည့်သွင်းပါ။ AI အေးဂျင့်အား conversation turn နှင့် တောင်းဆိုမှုအရေအတွက်ကို ကန့်သတ်ခြင်းဖြင့် ဒီအမျိုးအစားတိုက်ခိုက်မှုများကို ကာကွယ်နိုင်သည်။

### သိပ္ပံအခြေခံ ဒေတာ ပျက်စီးမှု

**ဖော်ပြချက်**: ဒီအမျိုးအစား တိုက်ခိုက်မှုသည် AI agent ကိုတိုက်ရိုက်တိုက်ခိုက်ခြင်း မဟုတ်ဘဲ၊ AI agent အသုံးပြုမည့် သိပ္ပံအခြေခံ ဒေတာ နှင့် အခြားဝန်ဆောင်မှုများကို ပစ်မှတ်ထားသည်။ ၎င်းသည် ဒေတာကိုပျက်စီးစေခြင်းမှစ၍ AI အေးဂျင့်၏ တုံ့ပြန်ချက်အား ကြီးထွားသော ဖွဲ့စည်းခြင်း မမှန်ကန်မှုများ ဖန်တီးစေနိုင်သည်။

**ကာကွယ်မှု**: AI အေးဂျင့်workflow တွင်အသုံးပြုမည့် ဒေတာကို ပုံမှန်စစ်ဆေးအတည်ပြုပါ။ ဒေတာအား ဝင်ရောက်ပြောင်းလဲခြင်းကို ယုံကြည်စိတ်ချရပြီး တရားဝင်သူများကသာ လုပ်နိုင်ရန် လုံခြုံမှုထားရှိပါ။

### တဆင့်ဆင့် ပြဿနာများဖြစ်ပွားမှု

**ဖော်ပြချက်**: AI အေးဂျင့်သည် ကိရိယာများနှင့် ဝန်ဆောင်မှုများကို အသုံးပြုကာ တာဝန်ထမ်းဆောင်သည်။ တိုက်ခိုက်သူများမှ ဖြစ်စေသော အမှားများကြောင့် AI agent အဆက်အသွယ်ရှိ စနစ်များ ကျရောက်ပြီး ပြဿနာများပိုမိုဖြစ်ပွားဖို့ ဖြစ်စေသည်။

**ကာကွယ်မှု**: AI agent ကို ကန့်သတ်ထားသည့် ပတ်ဝန်းကျင်တွင် အလုပ်လုပ်စေခြင်း (ဥပမာ - Docker container ထဲတွင် ရှိခြင်း) ဖြင့် တိုက်ရိုက်စနစ်တိုက်ခိုက်မှုကာကွယ်နိုင်သည်။ နောက်ပြန်ပြင်ဆင်ခြင်းနှင့် ပြန်လည် ကြိုးစားမည့် အလိုအလျောက်လုပ်ဆောင်မှု ထည့်သွင်းခြင်းကလည်း စနစ်ကျရောက်မှုများကြီးမားစေခြင်းမှ ကာကွယ်နိုင်သည်။

## လူကို အတူထည့်သွင်းခြင်း

ယုံကြည်စိတ်ချရသော AI agent စနစ်များတည်ဆောက်ရာတွင် လူကို အတူထည့်သွင်းခြင်း (Human-in-the-loop) ကို သုံးခြင်းလည်း ထိရောက်သော နည်းလမ်းတစ်ခုဖြစ်သည်။ ဤနည်းလမ်းတွင် အသုံးပြုသူများသည် အေးဂျင့်များကို feedback ပေးနိုင်ပြီး အေးဂျင့်များ အလုပ်လုပ်နေစဉ် အတည်ပြုခြင်း သို့မဟုတ် ရပ်ဆိုင်းပေးနိုင်သည်။

![Human in The Loop](../../../translated_images/my/human-in-the-loop.5f0068a678f62f4f.webp)

ဤအယူအဆကို Microsoft Agent Framework ဖြင့် ကုဒ်အပိုင်းအရှည် မှတ်သားထားသော နမူနာ -

```python
import os
from agent_framework.azure import AzureAIProjectAgentProvider
from azure.identity import AzureCliCredential

# လူတစ်ဦး၏ အတည်ပြုချက်ဖြင့် provider ကို ဖန်တီးပါ
provider = AzureAIProjectAgentProvider(
    credential=AzureCliCredential(),
)

# လူတစ်ဦး၏ အတည်ပြုခြင်း အဆင့်ပါ agent ကို ဖန်တီးပါ
response = provider.create_response(
    input="Write a 4-line poem about the ocean.",
    instructions="You are a helpful assistant. Ask for user approval before finalizing.",
)

# အသုံးပြုသူသည် တုံ့ပြန်ချက်ကို ပြန်လည်ဆန်းစစ်၍ အတည်ပြုနိုင်သည်
print(response.output_text)
user_input = input("Do you approve? (APPROVE/REJECT): ")
if user_input == "APPROVE":
    print("Response approved.")
else:
    print("Response rejected. Revising...")
```

## နိဂုံးချုပ်

ယုံကြည်စိတ်ချရသော AI အေးဂျင့်များ တည်ဆောက်ရန် သေချာစွာ ဒီဇိုင်းဆွဲသည့် နည်းလမ်းများ၊ ခိုင်မာသော လုံခြုံရေးစနစ်များနှင့် ဆက်လက်တိုးတက်အောင် ပြုပြင်ရန် လိုအပ်သည်။ ဆက်စပ် meta prompting စနစ်များ အသုံးပြုခြင်း၊ ဖြစ်နိုင်သော အန္တရာယ်များကို နားလည်ခြင်းနှင့် ကာကွယ်နိုင်မှု မူဝါဒများ အသုံးပြုခြင်းအားဖြင့် လုံခြုံပြီး ထိရောက်သော AI အေးဂျင့်များ ဖန်တီးနိုင်သည်။ ထို့ပြင် လူကို အတူထည့်သွင်းခြင်းဖြင့် AI အေးဂျင့်များ အသုံးပြုသူတို့လိုအပ်ချက်နှင့် ညီညွတ်နေစေပြီး အန္တရာယ်များကို သက်သာစေနိုင်သည်။ AI နည်းပညာ တိုးတက်လာသည့်အခါ ဆက်လက်လုံခြုံမှု၊ ကိုယ်ရေးအချက်အလက်၊ နှင့် မူဝါဒကျင့်ဝတ် ဆိုင်ရာ အချက်များကို အလေးထားဆောင်ရွက်ရမည်ဖြစ်သည်။

## ကုဒ်နမူနာများ

- [`code_samples/06-system-message-framework.ipynb`](code_samples/06-system-message-framework.ipynb): meta-prompt system-message framework ဖြင့် အဆင့်မြှင့် ပြသချက်။
- [`code_samples/06-human-in-the-loop.ipynb`](code_samples/06-human-in-the-loop.ipynb): ယုံကြည်စိတ်ချရသော agent များအတွက် လုပ်ဆောင်မှုပြုလုပ်မည့် လက်ခံမှု၊ အန္တရာယ်အဆင့်သတ်မှတ်ခြင်း၊ နှင့် စစ်ဆေးမှတ်တမ်း။

### ယုံကြည်စိတ်ချရသော AI အေးဂျင့်များ တည်ဆောက်ခြင်းဆိုင်ရာ အခြားမေးခွန်းများ ရှိပါသလား?

[Microsoft Foundry Discord](https://aka.ms/ai-agents/discord) တွင် ပေါင်းစည်းပြီး အခြားကျောင်းသားများနှင့် တွေ့ဆုံ၊ ရုံးချိန်များ တက်ရောက်ပြီး သင်၏ AI အေးဂျင့် မေးခွန်းများကို ဖြေကြားပါ။

## အပိုဆောင်း အရင်းအမြစ်များ

- <a href="https://learn.microsoft.com/azure/ai-studio/responsible-use-of-ai-overview" target="_blank">တာဝတ်ယူအကောင်အထည်ဖော်သည့် AI များ အကြောင်းအရာ</a>
- <a href="https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai" target="_blank">ဇီဝ AI မော်ဒယ်များနှင့် AI အက်ပလီကေးရှင်းများ အကဲဖြတ်ချက်</a>
- <a href="https://learn.microsoft.com/azure/ai-services/openai/concepts/system-message?context=%2Fazure%2Fai-studio%2Fcontext%2Fcontext&tabs=top-techniques" target="_blank">လုံခြုံရေး စနစ်စာတမ်းများ</a>
- <a href="https://blogs.microsoft.com/wp-content/uploads/prod/sites/5/2022/06/Microsoft-RAI-Impact-Assessment-Template.pdf?culture=en-us&country=us" target="_blank">အန္တရာယ် သတ်မှတ်စာရွက်ပုံစံ</a>

## ယခင် သင်ခန်းစာ

[Agentic RAG](../05-agentic-rag/README.md)

## နောက်ထပ် သင်ခန်းစာ

[Planning Design Pattern](../07-planning-design/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ပြောကြားချက်**
ဤစာတမ်းကို AI ဘာသာပြန်ဝန်ဆောင်မှု [Co-op Translator](https://github.com/Azure/co-op-translator) အသုံးပြု၍ ဘာသာပြန်ထားပါသည်။ ကျွန်ုပ်တို့သည် တိကျမှန်ကန်မှုအတွက် ကြိုးပမ်းနေသော်လည်း၊ စက်ကိရိယာဘာသာပြန်ခြင်းများတွင် အမှားများ သို့မဟုတ် မှားယွင်းချက်များ ပါဝင်နိုင်ကြောင်း သတိပြုပါရန် လိုအပ်ပါသည်။ မူလစာတမ်းကို မူရင်းဘာသာဖြင့်သာ ယုံကြည်စိတ်ချရသော အချက်အလက်အဖြစ် သတ်မှတ်သင့်သည်။ အရေးကြီးသည့် သတင်းအချက်အလက်များအတွက် ပရော်ဖက်ရှင်နယ် လူသားဘာသာပြန်သူဝန်ဆောင်မှုကို အကြံပြုပါသည်။ ဤဘာသာပြန်ချက်ကို အသုံးပြုခြင်းမှ ဖြစ်ပေါ်လာသော နားလည်မှုကွာခြားမှုများ သို့မဟုတ် မမှန်ကန်သော အသုံးပြုမှုများအတွက် ကျွန်ုပ်တို့ တာဝန်မခံပါ။
<!-- CO-OP TRANSLATOR DISCLAIMER END -->