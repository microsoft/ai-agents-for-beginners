[![AI အေးဂျင့် ဖရေမ်ဝက်စ်များကို စူးစမ်းလေ့လာခြင်း](../../../translated_images/my/lesson-2-thumbnail.c65f44c93b8558df.webp)](https://youtu.be/ODwF-EZo_O8?si=1xoy_B9RNQfrYdF7)

> _(အပေါ်က ပုံကို နှိပ်ပြီး ဒီသင်ခန်းစာရဲ့ ဗီဒီယိုကို ကြည့်ရှုပါ)_

# AI အေးဂျင့် ဖရေမ်ဝက်စ်များကို စူးစမ်းလေ့လာခြင်း

AI agent ဖရေမ်ဝက်စ်များသည် AI အေးဂျင့်များကို ဖန်တီးခြင်း၊ မိတ်ဆက်ခြင်းနှင့် စီမံခန့်ခွဲခြင်းကို လွယ်ကူစေသော ဆော့ဖ်ဝဲ ပလက်ဖောင်းများဖြစ်သည်။ ဤဖရေမ်ဝက်စ်များသည် ဖန်တီးသူများအား ကြိုတင်တည်ဆောက်ထားသော ပါတ်စ်တီများ၊ အမြင်သရုပ်ဖော်မှုများနှင့် ကိရိယာများကို ပံ့ပိုးပေးကာ ရုပ်ပိုင်းဆိုင်ရာရင်းနှီးသော AI စနစ်များကို တိုးတက်စွာ ဖွံ့ဖြိုးစေရန် အလွယ်တကူ အသုံးပြုနိုင်စေသည်။

ဤဖရေမ်ဝက်စ်များကြောင့် ဖန်တီးသူများသည် သုံးစွဲသူထူးခြားချက်များသို့ ဦးတည်၍ ကိုယ်ပိုင်လျှောက်လွှာများ၏ ထူးခြားသည့် အပိုင်းများကို အာရုံစိုက်နိုင်ပြီး AI အေးဂျင့် ဖွံ့ဖြိုးတိုးတက်ရေးနယ်ပယ်ရှိ ပုံမှန်စိန်ခေါ်မှုများကို စံသတ်မှတ်ထားသော နည်းလမ်းများဖြင့် ဖြေရှင်းနိုင်သည်။ ၎င်းတို့သည် စမတ်စနစ်များ ဖန်တီးရာတွင် စကေးလ်ပြုနိုင်ခြင်း၊ ရောက်ရှိနိုင်မှုနှင့် လုပ်ဆောင်ချက်ထိရောက်မှုကို မြှင့်တင်ပေးသည်။

## မိတ်ဆက်

ဒီသင်ခန်းစာတွင် ဖော်ပြမည့် အကြောင်းအရာများမှာ -

- AI Agent Frameworks ဆိုတာဘာလဲ၊ ဖန်တီးသူများအား ဘာတွေ စွမ်းနိုင်လာစေသလဲ?
- အသင်းများသည် ဒီအရာများကို အသုံးပြုကာ မျှော်မှန်းချက်အရှိဆုံး prototype များကို ဘယ်လို အလျင်အမြန် ဖန်တီး၊ တိုးတက်စေ၊ မြှင့်တင်နိုင်သလဲ?
- Microsoft (<a href="https://aka.ms/ai-agents-beginners/ai-agent-service" target="_blank">Azure AI Agent Service</a> နှင့် <a href="https://learn.microsoft.com/azure/ai-services/openai/how-to/responses" target="_blank">Microsoft Agent Framework</a>) မှ ဖန်တီးထားသော ဖရေမ်ဝက်စ်များနှင့် ကိရိယာများ၏ ကွာခြားချက်များက ဘာလဲ?
- ကျွန်ုပ်၏ ရှိပြီးသား Azure ပတ်ဝန်းကျင် ကိရိယာများကို တိုက်ရိုက် ပေါင်းစည်းနိုင်မလား, သီးခြား ဖြေရှင်းချက်များ လိုအပ်သလား?
- Azure AI Agents service ဆိုတာ ဘာလဲ၊ ၎င်းက ကျွန်ုပ်ကို ဘယ်လို ကူညီပေးနေလဲ?

## သင်ယူရမည့် ရည်မှန်းချက်များ

ဒီသင်ခန်းစာ၏ ရည်မှန်းချက်များမှာ -

- AI ဖွံ့ဖြိုးရေးတွင် AI Agent Frameworks ၏ အခန်းကဏ္ဍကို နားလည်စေခြင်း။
- ဉာဏ်ပညာရှင် agent များ ဖန်တီးရန် AI Agent Frameworks ကို မည်သို့ အသုံးချရမည်ကို သင်ကြားပေးခြင်း။
- AI Agent Frameworks များက ပံ့ပိုးပေးသည့် အဓိက စွမ်းရည်များကို ဆွဲထုတ်ပြသခြင်း။
- Microsoft Agent Framework နှင့် Azure AI Agent Service တို့၏ ကွာခြားချက်များကို ရှင်းလင်းပြသခြင်း။

## AI Agent Frameworks ဆိုတာဘာလဲ၊ ဖန်တီးသူများကို ဘာတွေ လုပ်နိုင်အောင် ပြုလုပ်ပေးသလဲ?

ရိုးရိုး AI ဖရေမ်ဝက်စ်များက သင့်လျှောက်လွှာများထဲသို့ AI ကို ထည့်သွင်းရန်နှင့် အခြားသော အချက်အလက်များနှင့် ပေါင်းစည်းရန် အောက်ပါနည်းလမ်းများဖြင့် ကူညီပေးနိုင်သည်။

- **ပုဂ္ဂိုလိကထူးခြားအတွေ့အကြုံ (Personalization)**: AI သည် သုံးစွဲသူ အပြုအမူနှင့် ကြိုက်နှစ်သက်မှုများကို विश्लेषणကာ ကိုယ့်လိုလိုက်ကြောင်း အကြံပြုချက်များ၊ အကြောင်းအရာများနှင့် အတွေ့အကြုံများကို ပေးနိုင်သည်။ ဥပမာ - Netflix ကဲ့သို့ စတရိမင်း ဝန်ဆောင်မှုများသည် ကြည့်ရှုမှတ်တမ်းအပေါ်မူတည်၍ ရုပ်ရှင်များနှင့် ရုပ်သံ အစီအစဉ်များကို အကြံပြုကာ သုံးစွဲသူ စိတ်၀င်စားမှုနှင့် စိတ်ကျေနပ်မှုကို မြှင့်တင်ပေးသည်။
- **အလိုအလျောက်လုပ်ဆောင်ခြင်းနှင့် ထိရောက်မှု (Automation and Efficiency)**: AI သည် နာရက်ပြီးသော အလုပ်များကို အလိုအလျောက် ပြုလုပ်ပေးနိုင်ပြီး အလုပ်စဉ်များကို ရိုးရှင်းစေကာ လုပ်ငန်းဆောင်တာ ထိရောက်စေသည်။ ဥပမာ - ဖောက်သည်ဝန်ဆောင်မှု အက်ပ်များတွင် AI အားဖြင့် စွမ်းဆောင်သော chatbot များကို အသုံးပြု၍ ပုံမှန် မေးခွန်းများကို ကိုင်တွယ်ထားနိုင်သည်။ ၎င်းက တုံ့ပြန်ချိန်လျော့ပြီး လူဝန်ထမ်းများကို ပိုမိုရှုပ်ထွေးသော ကိစ္စများအတွက် အချိန်ပေးစေသည်။
- **အသုံးပြုသူအတွေ့အကြုံတိုးတက်ရေး (Enhanced User Experience)**: AI သည် အသံ မှတ်လက်ခံခြင်း၊ သဘာဝဘာသာစကား အ Verarbeitung နှင့် ခန့်မှန်းရေး စာသားများ ကဲ့သို့သော ဉာဏ်ရည်ဆိုင်ရာ လက္ခဏာများဖြင့် အသုံးပြုသူအတွေ့အကြုံကို တိုးတက်စေသည်။ ဥပမာ - Siri နှင့် Google Assistant ကဲ့သို့သော virtual assistant များသည် အသံအမိန့်များကို နားလည်၍ တုံ့ပြန်ကာ အသုံးပြုသူများအတွက် စက်ဘက်ဖြင့် ဆက်သွယ်ရသည့် လမ်းကို လွယ်ကူစေသည်။

### အားလုံးကောင်းပါတယ်၊ ဒါဆို AI Agent Framework လိုအပ်ရတဲ့ အကြောင်းကဘာလဲ?

AI Agent framework များသည် ရိုးရှင်းသော AI ဖရေမ်ဝက်စ်များထက် ပိုမိုကိုယ်ပိုင်သော အရာတစ်ခုကို ကိုယ်စားပြုသည်။ ၎င်းတို့ကို ဖန်တီးထားသော ရည်ရွယ်ချက်မှာ အသုံးပြုသူများ၊ အခြား agent များနှင့် ပတ်ဝန်းကျင်နှင့် မျေးဆက်ပြီး သတ်မှတ်ထားသော ရည်မှန်းချက်များကို ပြည့်မှီစေသည့် ဉာဏ်ရည်မြင့် agent များ ဖန်တီးရန်ဖြစ်သည်။ ၎င်း agent များသည် ကိုယ်ပိုင်အလိုအလျောက်ပြုမူနိုင်ပြီး ဆုံးဖြတ်ချက်ချနိုင်ကာ ပြောင်းလဲလျင်မြန်သော အခြေအနေများအပေါ် မုခင်းပြောင်းလဲနိုင်သည်။ AI Agent Frameworks များက ပံ့ပိုးပေးနိုင်သည့် အဓိက စွမ်းရည်များကို ကြည့်ကြပါစို့ -

- **Agent များအချင်းချင်း ပူးပေါင်းဆောင်ရွက်ခြင်းနှင့် ညှိနှိုင်းမှု**: အချင်းချင်း ဆက်သွယ်၍ ပူးပေါင်းဆောင်ရွက်နိုင်သည့် AI agent များ ဖန်တီးရန် အထောက်အကူပြုသည်။
- **အလုပ်တာဝန်အလိုအလျောက်ဆောင်ရွက်ခြင်းနှင့် စီမံခန့်ခွဲမှု**: များစွာသော အဆင့်မြင့် အလုပ်စဉ်များကို အလိုအလျောက်ထိန်းချုပ်ခြင်း၊ အလုပ်အပ်နှံခြင်းနှင့် agent များအကြား ဒိုင်းနမစ်စီမံခန့်ခွဲမှုများအတွက် မက်ကနစ်များ ပေးသည်။
- **အကြောင်းအရာနားလည်ခြင်းနှင့် ကိုက်ညီပြောင်းလဲမှု (Contextual Understanding and Adaptation)**: Agent များကို အခြေအနေကို နားလည်ရန်၊ ပတ်ဝန်းကျင်ပြောင်းလဲမှုများအပေါ် ကိုက်ညီရန်နှင့် အချိန်နှင့်တပြေးညီ အချက်အလက်များအပေါ် အခြေခံ၍ ဆုံးဖြတ်ချက်ချရန် စွမ်းရည်ပြုသည်။

အကျဥ်းချုပ်အားဖြင့် agent များက သင့်အား ပိုပြီးလုပ်ဆောင်နိုင်စေပြီး အလိုအလျောက်လုပ်ဆောင်မှုကို နောက်ထပ်အဆင့်မြှင့်တင်ပေးကာ ပတ်ဝန်းကျင်အပေါ်မှ သင်ယူ၍ ကိုက်ညီနိုင်သော ပိုမို ဉာဏ်ရည်မြင့် စနစ်များကို ဖန်တီးနိုင်စေသည်။

## အေးဂျင့်၏ စွမ်းရည်များကို အလျင်အမြန် prototype ဖန်တီး၊ ထပ်လည်တိုးတက်စေ၊ ချပြင်ရန် ဘယ်လိုလုပ်ရမလဲ?

ဤနယ်ပယ်သည် မြန်မြန်ပြောင်းလဲနေသော်လည်း အများအားဖြင့် AI Agent Frameworks များတွင် ပေါင်းစည်းအသုံးများသော အချက်များ ရှိပြီး ၎င်းတို့က သင့်အား အလျင်အမြန် prototype ဖန်တီးခြင်းနှင့် iteration လုပ်ခြင်းကို ကူညီပေးနိုင်သည်။ ၎င်းတို့မှာ module components, collaborative tools, နှင့် real-time learning တို့ ဖြစ်သည်။ ယနေ့က အချက်များကို အောက်ပါအတိုင်း ရှင်းပြပါမည် -

- **မော်ဂျူးလာပါက်ကွန် (Modular Components) ကို အသုံးပြုပါ**: AI SDK များတွင် AI နှင့် Memory connector များ၊ သဘာဝဘာသာစကား သို့မဟုတ် ကုဒ် plugin များဖြင့် function calling, prompt template များ အပါအဝင် ကြိုတင်တည်ဆောက်ထားသောပါတ်စ်များပါရှိသည်။
- **ပူးပေါင်းဆောင်ရွက်ရေး ကိရိယာများကို အသုံးချပါ**: ထူးခြားသော ဖြစ်စဉ်နှင့် တာဝန်များရှိသော agent များကို ဒီဇိုင်းဆွဲကာ ပူးပေါင်းဆောင်ရွက်မှု workflow များကို စမ်းသပ်၊ ပြုပြင်ချိန်ညှိနိုင်သည်။
- **အချိန်နဲ့တပြေးညီ သင်ယူပါ (Learn in Real-Time)**: Agent များသည် ဆက်သွယ်မှုများမှ သင်ယူကာ သူတို့၏ အပြုအမူကို ဒိုင်နမစ်စွာ ပြင်ဆင်နိုင်ရန် feedback loop များကို အကောင်အထည်ဖော်ပါ။

### မော်ဂျူးလာပါက်ကွန်များကို အသုံးပြုပါ

Microsoft Agent Framework ကဲ့သို့သော SDK များတွင် AI connector များ၊ tool သတ်မှတ်ချက်များနှင့် agent စီမံခန့်ခွဲမှုကဲ့သို့ ကြိုတင်တည်ဆောက်ထားသော ပါတ်စ်တီများ ပါဝင်သည်။

**အသင်းများ ဘယ်လို အသုံးချနိုင်သလဲ**: အသင်းများသည် ၎င်းတို့ကို အစကနေတည်ဆောက်ရန် မလိုဘဲ အရေးကြီးသော ပတ္တိများကို မြန်ဆန်စွာစုစည်းကာ လက်တွေ့အသုံးပြုနိုင်သည့် prototype ကို အလွယ်တကူ ဖန်တီးနိုင်ပြီး စမ်းသပ်မှုနှင့် iteration ကို မြန်ဆန်စေသည်။

**လက်တွေ့တွင် ဘယ်လို အလုပ်လုပ်သလဲ**: သင်သည် အသုံးပြုသူ၏ ငြိမ်းချမ်းမှုမှ ထိပ်တန်း အချက်အလက်များကို မျက်နှာချင်းဆိုင် ထုတ်ယူရန် ကြိုတင်တည်ဆောက်ထားသော parser တစ်ခုကို အသုံးပြုနိုင်သည်၊ အချက်အလက်ကို သိမ်းဆည်း၊ ပြန်လည်ယူရန် memory module တစ်ခုကို အသုံးပြုနိုင်သည်၊ နှင့် အသုံးပြုသူနှင့် ဆက်သွယ်ရန် prompt generator တစ်ခုကို အသုံးပြုနိုင်သည် — ဤအားလုံးကို စကတ်ချွတ်ကင်းစွာ တည်ဆောက်ရန် မလိုဘဲ အသုံးပြုနိုင်သည်။

**ဥပမာကုဒ်**။ ပေါင်းဖော်ပြရရင် Microsoft Agent Framework ကို `AzureAIProjectAgentProvider` နှင့် ပေါင်းစပ်ကာ model ကို tool calling ဖြင့် အသုံးပြုရန် ဤဥပမာကို ကြည့်ပါ။

``` python
# Microsoft Agent Framework Python နမူနာ

import asyncio
import os
from typing import Annotated

from agent_framework.azure import AzureAIProjectAgentProvider
from azure.identity import AzureCliCredential


# ခရီးသွားဘွတ်ကင်ချရန် နမူနာကိရိယာ စက်ရုပ်ရေးဆွဲပါ
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
    # နမူနာ အထွက်: ၂၀၂၅ ခုနှစ် ဇန်နဝါရီ ၁ ရက်နေ့တွင် နယူးယော့ခ်သို့ သင်၏ လေယာဉ်ခရီးစဉ်ကို အောင်မြင်စွာစာရင်းသွင်းပြီးဖြစ်သည်။ ခရီးသွားရာ အေးချမ်းစေပါစေ! ✈️🗽


if __name__ == "__main__":
    asyncio.run(main())
```

ဤဥပမာမှ သင်မြင်နိုင်သည်မှာ အသုံးပြုသူ၏ အစားထိုးထည့်သွင်းချက်မှ ကောက်ခြင်းဖြင့် origin, destination, နှင့် ရက်စွဲကဲ့သို့သော အချက်အလက်များကို ထုတ်ယူပေးသည့် ကြိုတင်တည်ဆောက်ထားသော parser ကို မည်သို့ အသုံးချနိုင်သည်ကို ဖြစ်ပါသည်။ ဤမော်ဂျူးလာနည်းပညာသည် သင်အား အဆင့်မြင့် လောဂျစ်များပေါ် အာရုံစိုက်ခွင့်ပြုသည်။

### ပူးပေါင်းဆောင်ရွက်ရေး ကိရိယာများကို အသုံးချပါ

Microsoft Agent Framework ကဲ့သို့ ဖရေမျော်စ်များသည် အချင်းချင်းပူးပေါင်းဆောင်ရွက်နိုင်သော agent များကို ဖန်တီးဖို့ အထောက်အကူပြုသည်။

**အသင်းများ ဘယ်လို အသုံးချနိုင်သလဲ**: အသင်းများသည် တာဝန်များနှင့် အခန်းကဏ္ဍ သတ်မှတ်ထားသော agent များကို ဒီဇိုင်းဆွဲနိုင်ပြီး ပူးပေါင်းလုပ်ဆောင်မှု workflow များကို စမ်းသပ်၊ မှန်ကန်အောင် ပြင်ဆင်နိုင်သည်။

**လက်တွေ့တွင် ဘယ်လို အလုပ်လုပ်သလဲ**: သင်သည် data retrieval, analysis, သို့မဟုတ် ဆုံးဖြတ်ချက်ချခြင်း ကဲ့သို့ အထူးပြု လုပ်ငန်းတာဝန်ရှိသည့် agent များကို တစ်စုချင်း ဖန်တီးနိုင်သည်။ ဤ agent များသည် ဆက်သွယ်မှုနှင့် အချက်အလက်မျှဝေမှုများဖြင့် ပူးပေါင်း၍ အသုံးပြုသူမေးခွန်းတစ်ခုကို ဖြေဆိုခြင်း သို့မဟုတ် တာဝန်တစ်ခုကို ပြီးမြောက်စေခြင်းကဲ့သို့ ရည်ရွယ်ချက်ပေါင်းတည်ချက်တူသော အလုံးစုံ အရေးယူမှုကို ရယူနိုင်သလို ဖြစ်စေသည်။

**ဥပမာကုဒ် (Microsoft Agent Framework)**:

```python
# Microsoft Agent Framework ကို အသုံးပြုပြီး အလုပ်လုပ်မည့် အေးဂျင့်များ များစွာ ဖန်တီးနေသည်

import os
from agent_framework.azure import AzureAIProjectAgentProvider
from azure.identity import AzureCliCredential

provider = AzureAIProjectAgentProvider(credential=AzureCliCredential())

# ဒေတာ ဆွဲယူခြင်း အေးဂျင့်
agent_retrieve = await provider.create_agent(
    name="dataretrieval",
    instructions="Retrieve relevant data using available tools.",
    tools=[retrieve_tool],
)

# ဒေတာ ခွဲခြမ်းစိတ်ဖြာမှု အေးဂျင့်
agent_analyze = await provider.create_agent(
    name="dataanalysis",
    instructions="Analyze the retrieved data and provide insights.",
    tools=[analyze_tool],
)

# တစ်စီအလိုက် အေးဂျင့်များကို အလုပ်လုပ်ဆောင်ရန် run ဟု ခေါ်သည်
retrieval_result = await agent_retrieve.run("Retrieve sales data for Q4")
analysis_result = await agent_analyze.run(f"Analyze this data: {retrieval_result}")
print(analysis_result)
```

မပြီးသောကုဒ်ပိုင်းတွင် သင်မြင်ရသောအတိုင်း အချက်အလက်များကို ခွဲခြမ်းစစ်ဆေးရန် အချို့သော agent များ ပူးပေါင်း၍ တာဝန်တစ်ခုကို ဆောင်ရွက်စေသည့် နည်းလမ်းကို တွေ့မြင်ရသည်။ Agent တစ်ဦးချင်းစီသည် အထူးပြု လုပ်ဆောင်ချက်တစ်ခုကို ပါဝင်ဆောင်ရွက်ပြီး တာဝန်ကို ရရှိရန် agent များကို ညှိနှိုင်းကာ လုပ်ဆောင်သည်။ အထူးပြု အခန်းကဏ္ဍများရှိ agent များကို ဖန်တီးခြင်းဖြင့် တာဝန်ထိထိရောက်ရောက်ဆောင်ရွက်နိုင်မှုကို တိုးတက်စေပါသည်။

### အချိန်နဲ့တပြေးညီ သင်ယူနိုင်စေရန်

တိုးတက်သော ဖရေမ်ဝက်စ်များသည် အချိန်နဲ့တပြေးညီ အကြောင်းအရာနားလည်မှုနှင့် ကိုက်ညီမှုအတွက် စွမ်းရည်များ ပံ့ပိုးပေးသည်။

**အသင်းများ ဘယ်လို အသုံးချနိုင်သလဲ**: အသင်းများသည် agent များကို ဆက်သွယ်မှုများမှ သင်ယူကာ ၎င်းတို့၏ အပြုအမူများကို ဒိုင်နမစ်စွာ ပြင်ဆင်စေနိုင်သည့် feedback loop များကို အကောင်အထည်ဖော်နိုင်သည်၊ ၎င်းက အဆက်မပြတ် တိုးတက်မှုနှင့် စွမ်းရည်များကို ပြုပြင်တိုးတက်စေသည်။

**လက်တွေ့တွင် ဘယ်လို အလုပ်လုပ်သလဲ**: Agent များသည် အသုံးပြုသူ feedback၊ ပတ်ဝန်းကျင်ဒေတာနှင့် တာဝန်အကောင်အထည်ဖော်မှုရလဒ်များကို ချွန်မြှင့်စစ်ဆေးကာ ၎င်းတို့၏ အသိပညာအစုံစု (knowledge base) ကို 업데이트လုပ်နိုင်သည်၊ ဆုံးဖြတ်ချက်ချနည်းလမ်းများကို ပြင်ဆင်နိုင်သည်၊ နှင့် မကြာခဏ ပိုမိုကောင်းမွန်လာစေရန် တိုးတက်စေသည်။ ၎င်း iteration ကျင့်စဉ်သည် agent များအား ပြောင်းလဲနေသော အခြေအနေများနှင့် အသုံးပြုသူ စိတ်ကြိုက်မှုများကို ကိုက်ညီစေနိုင်စေသည်။

## Microsoft Agent Framework နှင့် Azure AI Agent Service တို့၏ ကွာခြားချက်များက ဘာတွေလဲ?

ဤနည်းလမ်းများကို နှိုင်းယှဉ်ရန်နည်းလမ်းများ များပြားသော်လည်း ၎င်းတို့၏ ဒီဇိုင်း၊ စွမ်းရည်နှင့် ရည်ရွယ်သုံးစွဲမှုများအရ အောက်ပါ အဓိက ကွာခြားချက်များကို ကြည့်ကြမည်။

## Microsoft Agent Framework (MAF)

Microsoft Agent Framework သည် `AzureAIProjectAgentProvider` ကို အသုံးပြုပြီး AI agent များ တည်ဆောက်ရေးအတွက် စဉ်ဆက်မပြတ် SDK တစ်ခုကို ပံ့ပိုးပေးသည်။ ၎င်းက ဖန်တီးသူများအား Azure OpenAI မော်ဒယ်များကို အသုံးပြု၍ tool calling, conversation management နှင့် Azure identity ဖြင့် အချက်အလုံချဲ့ထားသော လုံခြုံရေး စနစ်များဖြင့် agent များကို ဖန်တီးနိုင်စေသည်။

**အသုံးပြုမှု ရောကြားမှုများ**: Tool အသုံးပြုခြင်း၊ များစွာသော အဆင့်ဆင့်လုပ်ငန်းစဉ်များနှင့် ဌာနဆက်သွယ်ရေးစနစ်များနှင့် ပေါင်းစည်းထားသည့် production-ready AI agent များ ဖန်တီးရန်။

Microsoft Agent Framework ၏ အရေးကြီးသော အခြေခံ အယူအဆများမှာ -

- **Agents**။ Agent တစ်ခုကို `AzureAIProjectAgentProvider` မှတစ်ဆင့် ဖန်တီးပြီး အမည်၊ ညွှန်ကြားချက်များနှင့် ကိရိယာများဖြင့် ဖွဲ့စည်းသည်။ Agent သည် -
  - **အသုံးပြုသူ မက်ဆေ့ချ်များကို ပrocess လုပ်ပြီး** Azure OpenAI မော်ဒယ်များကို အသုံးပြုကာ တုံ့ပြန်ချက်များ ဖန်တီးနိုင်သည်။
  - **Tool များကို အလိုအလျောက် ခေါ်ယူနိုင်**၍ ဆက်သွယ်မှု အခြေအနေအပေါ် မူတည်၍ အရေးပါတဲ့ လုပ်ဆောင်ချက်များကို ဆောင်ရွက်နိုင်သည်။
  - **စကားဝိုင်းအခြေအနေကို ပြန်လည် ထိန်းသိမ်းနိုင်**၍ များစွာသော အပြန်အလှန်ဆက်သွယ်မှုများအတွင်း conversation state ကို ဆက်လက် သိုလှောင်နိုင်သည်။

  Agent ဖန်တီးနည်းကို ပြသသည့် ကုဒ် အပိုင်းက ခုလောက်ပါ။

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

- **Tools**။ မျိုးစုံ အလုပ်များကို agent သည် အလိုအလျောက် ခေါ်ယူနိုင်သော Python function များအဖြစ် သတ်မှတ်နိုင်သည်။ Agent ဖန်တီးရာတွင် Tools များကို မှတ်ပုံတင်သည်။

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

- **Multi-Agent Coordination**။ ခွဲခြမ်းပေးမှုများရှိသော အမျိုးမျိုးသော အထူးပြု agent များကို ဖန်တီးကာ ၎င်းတို့၏ အလုပ်ကို ညှိနှိုင်းနိုင်သည်။

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

- **Azure Identity Integration**। Framework သည် `AzureCliCredential` (သို့မဟုတ် `DefaultAzureCredential`) ကို အသုံးပြု၍ လုံခြုံစိတ်ချရသော keyless authentication ကို ပံ့ပိုးပေးသည်၊ ထိုကာလတွင် API key များကို ကိုင်တွယ်ရန် မလိုအပ်တော့ပေ။

## Azure AI Agent Service

Azure AI Agent Service သည် Microsoft Ignite 2024 မှ တင်သွင်းခဲ့သော မိုဃ်းဆောင် အသစ်တစ်ခုဖြစ်သည်။ ၎င်းက Llama 3, Mistral, Cohere ကဲ့သို့သော open-source LLM များကို တိုက်ရိုက် ခေါ်ယူနိုင်သလို ပိုမို သေးငယ်နှင့် အလွယ်တကူ ချိန်ညှိနိုင်သည့် မော်ဒယ်များနှင့် ဖြန့်ချိနိုင်ရန် အဆင်ပြေစေသည်။

Azure AI Agent Service သည် စီးပွားရေးအဖွဲ့အစည်းများအတွက် လုံခြုံရေးစနစ်များနှင့် ဒေတာသိုလှောင်မှု နည်းလမ်းများကို မြင့်မားစွာ ပံ့ပိုးပေးသဖြင့် စီးပွားရေးအသုံးချမှုများအတွက် အထူးသင့်လျော်သည်။

၎င်းသည် Microsoft Agent Framework နှင့် အကောင်းဆုံးပေါင်းစည်းနိုင်ပြီး agent များ တည်ဆောက်ခြင်းနှင့် ဖြန့်ချိခြင်းအတွက် အထောက်အပံ့ ပေးနိုင်သည်။

ဤဝန်ဆောင်မှုကို ယခု Public Preview အနေဖြင့် ရရှိနိုင်ပြီး agent များကို ဖန်တီးရန် Python နှင့် C# ကို ပံ့ပိုးပေးထားသည်။

Azure AI Agent Service Python SDK ကို အသုံးပြုပြီး အသုံးပြုသူ သတ်မှတ်ထားသော tool တစ်ခုနှင့် agent တစ်ခုကို ဖန်တီးနည်း -

```python
import asyncio
from azure.identity import DefaultAzureCredential
from azure.ai.projects import AIProjectClient

# ကိရိယာလုပ်ဆောင်ချက်များကို သတ်မှတ်ပါ
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

### အခြေခံ အယူအဆများ

Azure AI Agent Service တွင် အောက်ပါ အခြေခံ အယူအဆများ ရှိသည် -

- **Agent**။ Azure AI Agent Service သည် Microsoft Foundry နှင့် ပေါင်းစည်းထားသည်။ AI Foundry အတွင်းတွင် AI Agent သည် အသိပညာရှိ "smarts" microservice တစ်ခုအဖြစ် တည်ရှိပြီး RAG ဖြင့် မေးခွန်းများကို ဖြေဆိုခြင်း၊ လုပ်ဆောင်ချက်များ ကိုင်တွယ်ခြင်း သို့မဟုတ် အလုံးစုံ Workflow များကို အလိုအလျောက် ဆောင်ရွက်နိုင်သည်။ ၎င်းသည် generative AI မော်ဒယ်များ၏ အာဏာနှင့် ရှေ့ကွက်များကို တိုက်ရိုက် ပေါင်းစည်းကာ အပြင်လောက ဒေတာအရင်းမြစ်များနှင့် အသုံးပြု၍ အပြန်အလှန် ဆက်သွယ်နိုင်သည့် tools များကို အသုံးပြုသည်။ Agent ၏ ဥပမာကို အောက်ပါအတိုင်း ပြထားသည်။

    ```python
    agent = project_client.agents.create_agent(
        model="gpt-4o-mini",
        name="my-agent",
        instructions="You are helpful agent",
        tools=code_interpreter.definitions,
        tool_resources=code_interpreter.resources,
    )
    ```

    ဤဥပမာတွင် agent တစ်ဦးကို `gpt-4o-mini` မော်ဒယ်ဖြင့် `my-agent` အမည်ဖြင့်၊ `You are helpful agent` ဟူသော ညွှန်ကြားချက်ဖြင့် ဖန်တီးထားသည်။ Agent သည် code interpretation လက်ရာများ ဆောင်ရွက်နိုင်ရန် tools နှင့် အရင်းအမြစ်များ ဖြင့် ပြည့်စုံသည်။

- **Thread နှင့် messages**။ Thread သည် အထူးထည့်ထားသည့် အယူအဆတစ်ခုဖြစ်သည်။ ၎င်းသည် agent နှင့် အသုံးပြုသူကြားရှိ စကားသံ သို့မဟုတ် ဆက်သွယ်မှုကို ကိုယ်စားပြုသည်။ Threads များကို စကားဝိုင်းတစ်ခု၏ တိုးတက်မှုကို သတင်းအချက်အလက် သိမ်းဆည်းရန်၊ context ကို မှတ်တမ်းတင်ရန်နှင့် အချိန်မီ အခြေအနေကို စီမံရန် အသုံးပြုနိုင်သည်။ Thread ၏ ဥပမာကို အောက်ပါအတိုင်း ပြထားသည်။

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

    အထက်ပါကုဒ်တွင် thread တစ်ခုကို ဖန်တီးထားသည်။ ထိုနောက် ဖောင်းစရာ message တစ်ခုကို thread သို့ ပို့ထားသည်။ `create_and_process_run` ကို ခေါ်ယူခြင်းဖြင့် agent ကို thread တွင် လုပ်ဆောင်ရန် တောင်းဆိုထားသည်။ နောက်ဆုံးတွင် messages များကို ဆွဲယူလော့ဂ်ထုတ်ခြင်းဖြင့် agent ၏ တုံ့ပြန်ချက်ကို ကြည့်ရှုနိုင်သည်။ မက်ဆေ့့များသည် စကား, ပုံ သို့မဟုတ် ဖိုင် ကဲ့သို့ အမျိုးအစား အမျိုးမျိုးရှိနိုင်သည် ဆိုသည်မှာ agent ၏ လုပ်ဆောင်ချက်ရလဒ်အနေဖြင့် ပုံတစ်ပုံ သို့မဟုတ် စာသားတစ်ပိုဒ်ဖြစ်လာနိုင်သည်။ ဖန်တီးသူတစ်ဦးအနေဖြင့် သင်သည် ဤအချက်အလက်ကို အသုံးပြုကာ တုံ့ပြန်ချက်ကို ထပ်မံလုပ်ဆောင်ရန် သို့မဟုတ် အသုံးပြုသူထံ မိတ်ဆက်ပေးနိုင်သည်။

- **Microsoft Agent Framework နှင့် ပေါင်းစည်းနိုင်ခြင်း**။ Azure AI Agent Service သည် Microsoft Agent Framework နှင့် အတူ လက်တွဲအလုပ်လုပ်နိုင်ပြီး၊ သင်သည် `AzureAIProjectAgentProvider` ကို အသုံးပြုကာ agent များ ဖန်တီးပြီး Agent Service မှတဆင့် production အတွက် ဖြန့်ချိနိုင်သည်။

**အသုံးပြုမှု ရောကြားမှုများ**: Azure AI Agent Service သည် လုံခြုံ, စကေးလ်ပြုနိုင်ပြီး အလွယ်တကူ ပြောင်းလဲနိုင်သော AI agent ဖြန့်ချိမှုကို လိုအပ်သည့် စီးပွားရေးအသုံးချမှုများအတွက် ရည်ရွယ်ထားသည်။

## ဤနည်းလမ်းများ၏ ကွာခြားချက်က ဘာလဲ?

บางครั้ง overlap ရှိသော်လည်း ၎င်းတို့၏ ဒီဇိုင်း၊ စွမ်းရည်နှင့် ရည်ညွှန်းသုံးစွဲမှုများအရ အောက်ပါ အရေးကြီး ကွာခြားချက်များ ရှိသည်။

- **Microsoft Agent Framework (MAF)**: Tool calling, conversation management နှင့် Azure identity ပေါင်းစပ်နိုင်သည့် agent များ ဖန်တီးရန် production-ready SDK တစ်ခုဖြစ်သည်။ Streamlined API တစ်ခုဖြင့် agent များကို ဖန်တီးရန် အဆင်ပြေသည်။
- **Azure AI Agent Service**: Agents များအတွက် Foundry အတွင်းရှိ platform နှင့် deployment ဝန်ဆောင်မှုဖြစ်သည်။ Azure OpenAI, Azure AI Search, Bing Search နှင့် code execution နှင့် အချင်းချင်း ချိတ်ဆက်မှုများကို ပေါင်းစည်းထားသည်။

ထိုနောက် သင် ဘယ်တစ်ခုကို ရွေးရမည်ကို မသေချာသေးလျှင် -

### အသုံးပြုမှု မျိုးစုံ

ကျွန်ုပ်တို့သည် အောက်ပါ ရိုးရှင်းသော ကိစ္စများမှတဆင့် မိတ်ဆက်ပေးလိုသည် -

> Q: production AI agent applications ဖန်တီးချင်ပြီး အစကို လျင်မြန်စတင်ချင်ပါတယ်
>

> A: Microsoft Agent Framework သည် အကောင်းဆုံးရွေးချယ်မှု ဖြစ်နိုင်သည်။ ၎င်းသည် `AzureAIProjectAgentProvider` မှတစ်ဆင့် ရိုးရှင်းသည့် Pythonic API ကို ပေးကာ tool များနှင့် ညွှန်ကြားချက်များဖြင့် agent များကို မကြာခဏ စာကြောင်းအနည်းငယ်ဖြင့် သတ်မှတ်နိုင်စေသည်။

> Q: Azure Search နှင့် code execution ကဲ့သို့ Azure ပေါင်းစည်းမှုများနှင့် အတူ စီးပွားရေးအဆင့် deployment လိုအပ်ပါတယ်
>
> A: Azure AI Agent Service သည် အကောင်းဆုံးသင့်လျော်ပါသည်။ ၎င်းသည် မော်ဒယ်များစွာ၊ Azure AI Search, Bing Search နှင့် Azure Functions များအတွက် built-in ချိတ်ဆက်မှုများပေးသည့် platform service တစ်ခုဖြစ်သည်။ Foundry Portal တွင် သင့် agent များကို အလွယ်တကူ တည်ဆောက်၍ ကျယ်ပြန့်စွာ ဖြန့်ချိနိုင်သည်။

> Q: ငါ မေးခွန်းရှုပ်နေဆဲ၊ တစ်ခုသာ ပေးပါ
>
> A: Microsoft Agent Framework ဖြင့် သင်၏ agent များကို စတင်ဖန်တီးပြီး ထို့နောက် production တွင် ဖြန့်ချိရန်နှင့် စကေးလ်ထိန်းရန် လိုအပ်သည့်အချိန် တွင် Azure AI Agent Service ကို အသုံးပြုပါ။ ဤနည်းလမ်းသည် သင့် agent logic အပေါ် မြန်ဆန်စွာ iteration လုပ်နိုင်စေပြီး စီးပွားရေး deployment သို့ ရောက်ရှိရန် သေချာသော လမ်းကြောင်းတစ်ခုကို ပေးသည်။

ကျွန်ုပ်တို့ အောက်ပါ အရေးကြီး ကွာခြားချက်များကို ဇယားတစ်ခုဖြင့် အကျဉ်းချုပ်ပေးလိုက်သည် -

| Framework | Focus | Core Concepts | Use Cases |
| --- | --- | --- | --- |
| Microsoft Agent Framework | Streamlined agent SDK with tool calling | Agents, Tools, Azure Identity | Building AI agents, tool use, multi-step workflows |
| Azure AI Agent Service | Flexible models, enterprise security, Code generation, Tool calling | Modularity, Collaboration, Process Orchestration | Secure, scalable, and flexible AI agent deployment |

## ကျွန်ုပ်၏ ရှိပြီးသား Azure ပတ်ဝန်းကျင် ကိရိယာများကို တိုက်ရိုက် ပေါင်းစည်းနိုင်မလား၊ သီးခြား ဖြေရှင်းချက်များ လိုအပ်သလား?
The answer is yes, you can integrate your existing Azure ecosystem tools directly with Azure AI Agent Service especially, as it has been built to work seamlessly with other Azure services. You could for example integrate Bing, Azure AI Search, and Azure Functions. There's also deep integration with Microsoft Foundry.

The Microsoft Agent Framework also integrates with Azure services through `AzureAIProjectAgentProvider` and Azure identity, letting you call Azure services directly from your agent tools.

## နမူနာကုဒ်များ

- Python: [Agent Framework](./code_samples/02-python-agent-framework.ipynb)
- .NET: [Agent Framework](./code_samples/02-dotnet-agent-framework.md)

## AI Agent Frameworks အကြောင်း ပိုမေးစရာများ ရှိသလား?

Join the [Microsoft Foundry Discord](https://aka.ms/ai-agents/discord) to meet with other learners, attend office hours and get your AI Agents questions answered.

## ကိုးကားချက်များ

- <a href="https://techcommunity.microsoft.com/blog/azure-ai-services-blog/introducing-azure-ai-agent-service/4298357" target="_blank">Azure Agent Service</a>
- <a href="https://learn.microsoft.com/azure/ai-services/openai/how-to/responses" target="_blank">Microsoft Agent Framework - Azure OpenAI Responses</a>
- <a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Azure AI Agent service</a>

## ယခင် သင်ခန်းစာ

[AI Agents မိတ်ဆက်နှင့် သုံးစွဲမှုများ](../01-intro-to-ai-agents/README.md)

## နောက်ထပ် သင်ခန်းစာ

[Agentic Design Patterns ကို နားလည်ခြင်း](../03-agentic-design-patterns/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
သတိပေးချက်:
ဤစာရွက်ကို AI ဘာသာပြန်ဝန်ဆောင်မှု [Co-op Translator](https://github.com/Azure/co-op-translator) ဖြင့် ဘာသာပြန်ထားပါသည်။ ကျွန်ုပ်တို့သည် တိကျမှုအတွက် ကြိုးစားပါသော်လည်း၊ အလိုအလျောက်ပြန်ဆိုခြင်းများတွင် အမှားများ သို့မဟုတ် မှားယွင်းချက်များ ပါရှိနိုင်သည်ကို ကျေးဇူးပြု၍ ထိုးထားပါ။ မူလစာရွက်ကို မူလဘာသာဖြင့်သာ သက်ဆိုင်ရာ တရားဝင် အရင်းအမြစ်အဖြစ် ယူဆသင့်ပါသည်။ အရေးကြီးသော အချက်အလက်များအတွက် လူ့ပရော်ဖက်ရှင်နယ် ဘာသာပြန်သူကို အသုံးပြုရန် အကြံပြုပါသည်။ ဤဘာသာပြန်ချက်ကို အသုံးပြုမှုကြောင့် ဖြစ်ပေါ်နိုင်သည့် နားမလည်မှုများ သို့မဟုတ် မှားယွင်းချက်များအတွက် ကျွန်ုပ်တို့အနေဖြင့် တာဝန်မခံပါ။
<!-- CO-OP TRANSLATOR DISCLAIMER END -->