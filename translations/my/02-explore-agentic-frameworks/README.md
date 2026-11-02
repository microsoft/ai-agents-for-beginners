[![AI Agent Frameworks များကို လေ့လာခြင်း](../../../translated_images/my/lesson-2-thumbnail.c65f44c93b8558df.webp)](https://youtu.be/ODwF-EZo_O8?si=1xoy_B9RNQfrYdF7)

> _(ဤသင်ခန်းစာ၏ ဗီဒီယိုကို ကြည့်ရှုရန် အပေါ်ပါ ပုံကို နှိပ်ပါ)_

# AI Agent Frameworks များကို လေ့လာပါ

AI agent frameworks များသည် AI agents များကို ဖန်တီးခြင်း၊ တပ်ဆင်ခြင်းနှင့် စီမံခန့်ခွဲခြင်းကို လွယ်ကူစေရန် ဒီဇိုင်း ထားသော စက်မှုကြမ်းတမ်းပလက်ဖောင်းများဖြစ်သည်။ ဒီ frameworks များသည် developer များအတွက် မှီခိုနိုင်သော ပစ္စည်းအစိတ်အပိုင်းများ၊ abstraction များ နှင့် ကိရိယာများကို ပေးဆောင်ကာ ကောင်းစွာ စီမံရန် မြှင့်တင်ပေးသည်။

ဒီ frameworks များသည် developer များကို AI agent ဖန်တီးမှုတွင် ရှိသော ပုံမှန် စိန်ခေါ်မှုများအတွက် စံပြနည်းလမ်းများဖြင့် ထောက်ပံ့ပေးကာ သူတို့၏ application များ၏ ထူးခြားချက်များကို ပိုမို ဂရုပြုနိုင်စေသည်။ ၎င်းသည် AI စနစ်များ ဖန်တီးရာတွင် မြှင့်တင်နိုင်စွမ်း၊ လွယ်ကူစေရေးနှင့် ထိရောက်မှု အများစွာ တိုးတက်စေသည်။

## နိဒါန်း

ဤသင်ခန်းစာတွင် ပါဝင်စေမည့် အကြောင်းအရာများမှာ -

- AI Agent Frameworks ဆိုတာ ဘာလဲ၊ developer များ အသုံးပြု၍ ဘာတွေ ပြုလုပ်နိုင်သလဲ?
- အသင်းများသည် ၎င်းတို့၏ agent ၏ စွမ်းရည်များကို အလျင်အမြန် prototype ပြုလုပ်၍ လည်ပတ်ချက်ပြန်လည်တိုးတက်ကောင်းမွန်စေရန် မည်သို့ အသုံးပြုနိုင်သနည်း?
- Microsoft (<a href="https://aka.ms/ai-agents-beginners/ai-agent-service" target="_blank">Microsoft Foundry Agent Service</a> နှင့် <a href="https://learn.microsoft.com/azure/ai-services/openai/how-to/responses" target="_blank">Microsoft Agent Framework</a>) ဖန်တီးထားသော framework များနှင့် tool များအကြား တစ်ခုချင်းစီ ရှိ ကွာခြားချက်များက ဘာတွေလဲ?
- အသုံးပြုလျက်ရှိသော Azure ecosystem tools များကို တိုက်ရိုက် ပေါင်းစည်းအသုံးပြုနိုင်မလား၊ ဒါမှမဟုတ် သီးခြားဖြေရှင်းမှုများ လိုအပ်ပါသလား?
- Microsoft Foundry Agent Service ဆိုတာ ဘာလဲ၊ ၎င်းက သင့်ကို မည်ကဲ့သို့ ကူညီပေးလဲ?

## သင်ယူရမည့် ကြိုးစားမှုများ

ဤသင်ခန်းစာ၏ ရည်ရွယ်ချက်မှာ သင်တွေ့ရမည့်အချက်များ:

- AI Agent Frameworks ၏ အရေးပါမှု။
- AI Agent Frameworks ကို အသုံးပြု၍ ပညာရပ်များပါ  agent များ တည်ဆောက်နည်း။
- AI Agent Frameworks ပေးသော အရေးကြီးသော စွမ်းဆောင်ရည်များ။
- Microsoft Agent Framework နှင့် Microsoft Foundry Agent Service တို့၏ ကွာခြားချက်များ။

## AI Agent Frameworks များ ဆိုတာဘာလဲ၊ developer များ ဘာတွေ ပြုလုပ်နိုင်သနည်း?

ရိုးရာ AI Frameworks များသည် သင်၏ app များထဲ AI ကို ပေါင်းစည်းရာတွင် ကူညီပေးနိုင်ပြီး ဤ app များကို အောက်ပါနည်းဖြင့် ပိုမိုကောင်းမွန်စေသည် -

- **ပုဂ္ဂိုလိကလုပ်ဆောင်ချက်ပြုခြင်း**: AI သည် အသုံးပြုသူ လေ့လာမှုများနှင့် သဘောထားများကို စူးစမ်းထားပြီး ပုဂ္ဂိုလိက အကြံပြုချက်များ၊ အကြောင်းအရာများနှင့် အတွေ့အကြုံများ ပေးစွမ်းနိုင်သည်။
ဥပမာ - Netflix ကဲ့သို့သော streaming ဝန်ဆောင်မှုများသည် AI ကို အသုံးပြု၍ ပြေးသည့် ဇာတ်ကားများနှင့် ရုပ်မြင်သံကြားအစီအစဉ်များကို လိုက်လံအကြံပြုခြင်းဖြင့် အသုံးပြုသူ စိတ်ဝင်စားမှုနှင့်ကျေနပ်မှုကို တိုးမြှင့်သည်။
- **အော်တိုမိတ်နှင့် ထိရောက်မှု**: AI သည် အလုပ်များကို အလိုအလျောက် ပြုလုပ်နိုင်ပြီး စဉ်ဆက်မပြတ်လုပ်ငန်းစဉ်များကို လွယ်ကူစွာ စီမံနိုင်သည်။
ဥပမာ - Customer service အက်ပလီကေးရှင်းများသည် AI အား ထောက်ပံ့သော chatbot များဖြင့် အများပြော မေးခွန်းများကို ပြန်လည်ဖြေရှင်းခြင်းဖြင့် အာရုံစိုက်မှုနှင့် လူအဖွဲ့အတွက် များစွာ စွန့်ပစ်နိုင်သည်။
- **အသုံးပြုသူအတွေ့အကြုံ မြှင့်တင်ခြင်း**: AI သည် အသံသိခြင်း၊ သဘာဝဘာသာစကား စီမံခန့်ခွဲခြင်း၊ မျှော်မှန်းချက်အရ စာသားရေးသားမှုကဲ့သို့သော အသုံးများသော features များဖြင့် အသုံးပြုသူအတွေ့အကြုံ တိုးတက်စေသည်။
ဥပမာ - Siri နှင့် Google Assistant ကဲ့သို့သော virtual assistant များသည် AI ကို အသုံးပြု၍ အသံမိန့်များကို နားလည်မှုနှင့် ပြန်ကြားမှု ပြုလုပ်ကာ အသုံးပြုသူများ၏ စက်ပစ္စည်းများနှင့် လွယ်ကူစွာ ဆက်သွယ်နိုင်စေသည်။

### ကောင်းတယ်နော်၊ ဒါပေမယ့် AI Agent Framework ကို ဘာကြောင့် လိုအပ်တာလဲ?

AI Agent Framework များသည် AI frameworks ပုံမှန်များထက် ပို၍ တိုးတက်မှုရှိသည်။ ၎င်းတို့သည် အသုံးပြုသူများနှင့် အခြား agent များနှင့် ပတ်ဝန်းကျင်ကြား ဆက်သွယ်နိုင်ပြီး ဆောင်ရွက်ချက်အတိအကျရရှိစေရန် ပညာရှိသော agent များ ဖန်တီးနိုင်စေရန် ဒီဇိုင်းထုတ်လိုက်သည်။ ၎င်းတို့သည် ကောင်းမွန်သော ကိုယ်သက်ရောက်မှု၊ ဆုံးဖြတ်ချက်ချခြင်းနှင့် ပတ်ဝန်းကျင် ပြောင်းလဲမှုအပေါ် မူတည်၍ ကိုက်ညီမှု ပြုလုပ်နိုင်သည်။ AI Agent Framework များထောက်ပံ့ပေးသော အရေးကြီးသော စွမ်းဆောင်ရည် အချို့မှာ -

- **Agent များ ပူးပေါင်းဆောင်ရွက်ခြင်းနှင့် ညှိနှိုင်းခြင်း**: Agnet တစ်ချို့သည် တူညီသော လုပ်ငန်းများကို အတူတကွ ပြုပြင်နိုင်ရန် ဆက်ဆံ ရောနှောပြီး လုပ်ငန်းရှုထောင့်များကို ရှာဖွေနိုင်စေသည်။
- **အလုပ်များ ကို အလိုအလျောက် ပြုလုပ်ခြင်းနှင့် စီမံခန့်ခွဲမှု**: လုပ်ငန်းစဉ်ကြီးများကို အလိုအလျောက် စီမံရန်၊ အလုပ်များ ခွဲဝေကမ်းလှမ်းခြင်းနှင့် ယခုအချိန်အခြေအနေ အရ စီမံခန့်ခွဲမှုများလုပ်နိုင်စေသည်။
- **အခြေအနေကို နားလည်ပြီး ကိုက်ညီမှု ပြုလုပ်ခြင်း**: Agent များသည် အခြေအနေများကို နားလည်ကာ ပတ်ဝန်းကျင် ပြောင်းလဲမှုများကို ကိုက်ညီစွာ ဖြေရှင်းနိုင်ပြီး လူကြီးမင်းတို အခုပင် ရရှိနောက်ခံပုံစံအရ ဆုံးဖြတ်ချက်များ ချနိုင်သည်။

အကျဉ်းချုပ်အားဖြင့် agent များသည် ပိုမိုအားကောင်းလာစေခြင်း၊ automation ကိုမျှသာအဆင့်မြှင့်တင်ခြင်း၊ ပိုမို သိမြင်စွမ်းနိုင်သော AI စနစ်များ ဖန်တီးပေးခြင်းအားဖြင့် ပတ်ဝန်းကျင်မှ သင်ယူယူဆောင် နိုင်စေသည်။

## Agent ၏ စွမ်းဆောင်ရည်များကို အမြန် prototype ပြုလုပ်ခြင်း၊ များပြားပြောင်းလဲတိုးတက်စေခြင်း မည်သို့လုပ်ရမည်နည်း?

ဤကဏ္ဍမှာ တိုးတက်မှုမြန်ဆန်သော နေရာဖြစ်ပါသည်၊ သို့သော် AI Agent Framework များအများစုတွင် အဖွဲ့လိုက် တည်ဆောက်နိုင်သည့် module components များ၊ ပူးပေါင်းဆောင်ရွက်မှု ကိရိယာများနှင့် အချိန်နှင့် တပြေးညီ လေ့လာမှု စနစ်များ အပေါ် အခြေခံ၍ အမြန် prototype နှင့် iteration ပြုလုပ်နိုင်ပါသည်။ အောက်တွင် အသေးစိတ်ဖော်ပြပါသည် -

- **Module Components များ အသုံးပြုပါ**: AI SDK များသည် AI နှင့် Memory connectors, function calling ကို သဘာဝဘာသာစကား သို့မဟုတ် ကုဒ် plugin များဖြင့် အသုံးပြုခြင်း၊ prompt templates များ စသဖြင့် ပြင်ဆင်ပြီးသား component များ ပေးအပ်သည်။
- **ပူးပေါင်းဆောင်ရွက်မှု ကိရိယာများကို အသုံးပြုပါ**: agent များအား အထူးသတ်မှတ်ထားသော အခန်းကဏ္ဍများနှင့် ရည်ရွယ်ချက်များ ဖြင့် ဒီဇိုင်းဆွဲ၍ ပူးပေါင်းမှု workflow များစမ်းသပ် ချပြန်ပြုပြင်နိုင်စေသည်။
- **အချိန်နှင့် တပြေးညီ လေ့လာမှုဆောင်ရွက်ပါ**: agents များသည် ဆက်သွယ်မှုများမှ ယုံကြည်ချက် ရယူကာ သက်ဆိုင်ရာ လုပ်ဆောင်ချက်များကို အချိန်နှင့်တပြေးညီ ပြန်လည် တည့်တောက်နိုင်စေနိုင်ရန်

### Module Components များ အသုံးပြုခြင်း

Microsoft Agent Framework ကဲ့သို့သော SDK များသည် AI connectors, tool definitions, agent management စတာတွေ ပြင်ဆင်ထားသော component များ ပေးသည်။

**အဖွဲ့များ အသုံးပြုနည်း**: အဖွဲ့များသည် ဒီ component များကို လျင်မြန်စွာ တွဲဖက် စုပေါင်းကာ သူတို့၏ prototype အသစ်ကို ရင်းမြစ် ထည့်စရာမလိုပဲ စမ်းသပ် ကြည့်နိုင်သည်။

**လက်တွေ့ အသုံးပြုနည်း**: အသုံးပြုသူ input မှ သတင်းအချက်အလက် ခွဲထုတ်ရန် ပြင်ဆင်ထားသော parser ကို အသုံးပြုနိုင်ပြီး၊ data များ သိမ်းဆည်းဖို့ memory module, အသုံးပြုသူကို လက်ခံဆက်သွယ်ရန် prompt generator တို့ ပါဝင်သည်။

**ဥပမာကုဒ်**: Microsoft Agent Framework ကို `FoundryChatClient` နှင့် အသုံးပြုပြီး tool calling ဖြင့် အသုံးပြုသူ input ကို ဘယ်လို ပြန်ကြားမယ်ဆိုတာ ဥပမာ ကြည့်ကြရအောင်။

``` python
# Microsoft Agent Framework Python ဥပမာ

import asyncio
import os

from agent_framework import tool
from agent_framework.foundry import FoundryChatClient
from azure.identity import AzureCliCredential


# ခရီးသွားစာရင်းစာရင်းမှတ်ရန် နမူနာကိရိယာ လုပ်ဆောင်ချက်ကို သတ်မှတ်ပါ
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
    # ဥပမာ အထွက်: သင်၏ ၂၀၂၅ ခုနှစ်၊ ဇန်နဝါရီလ ၁ ရက်နေ့တွင် နယူးယောက်သို့ သင်၏ လေယာဉ်ခရီးစဉ်ကို အောင်မြင်စွာ မှတ်ပုံတင်ပြီးဖြစ်ပါသည်။ ခရီးသွားရာတွင် ဘေးကင်းပါစေ! ✈️🗽


if __name__ == "__main__":
    asyncio.run(main())
```

ဤဥပမာမှ ကြည့်ရမှာက အသုံးပြုသူ input မှ အရေးပါတဲ့ ပစ္စည်းများကို (လေယာဉ်လက်မှတ်ရယူမှု အစရှိသည့် နေရာ၊ သွားမည့်နေရာနှင့် ရက်စွဲ) parser ဖြင့် ခွဲထုတ်နိင်ခြင်း ဖြစ်သည်။ ဒီ module ပုံစံက သင့်ကို အဆင့်မြင့် နည်းလမ်းများအပေါ် ဦးတည်မှုလုပ်နိုင်စေသည်။

### ပူးပေါင်းဆောင်ရွက်မှု ကိရိယာများအသုံးပြုခြင်း

Microsoft Agent Framework ကဲ့သို့သော frameworks သည် agent အများစုကို အတူတကွ ဆောင်ရွက်ရန် အကြောင်းအရာကို ပံ့ပိုးပေးသည်။

**အသုံးပြုနည်း**: အသင်းများသည် လုပ်ငန်းများအလိုက် အထူးပြု agent များဒီဇိုင်း ဆွဲကာ ပူးပေါင်းမှု workflow များ စမ်းသပ် ပြန်လည် တိုးတက်အောင် ဆောင်ရွက်နိုင်သည်။

**လက်တွေ့ အသုံးပြုနည်း**: အဖွဲ့၊ agent တစ်စုကို ဖန်တီးပါ၊ တစ်ဦးချင်းစီသည် ဒေတာရှာဖွေရေး၊ သုံးသပ်ခြင်း သို့မဟုတ် ဆုံးဖြတ်ချက်ချခြင်း စတာတွင် အထူးပြုလုပ်သည်။ ဤ agent များသည် အတူတကွ ဆက်သွယ်ကာ စီးပွားရေး စိန်ခေါ်မှုများကို ဖြေရှင်းကာ နောက်ဆုံး ရည်မှန်းချက်အောင်မြင်စေသည်။

**ဥပမာကုဒ် (Microsoft Agent Framework)**:

```python
# Microsoft Agent Framework ကို အသုံးပြု၍ အပြန်အလှန် အတူတကွ လုပ်ဆောင်နိုင်သော အေးဂျင့်များစွာ ဖန်တီးခြင်း

import os
from agent_framework.foundry import FoundryChatClient
from azure.identity import AzureCliCredential

provider = FoundryChatClient(
    project_endpoint=os.environ["AZURE_AI_PROJECT_ENDPOINT"],
    model=os.environ["AZURE_AI_MODEL_DEPLOYMENT_NAME"],
    credential=AzureCliCredential(),
)

# ဒေတာ ရယူခြင်း အေးဂျင့်
agent_retrieve = provider.as_agent(
    name="dataretrieval",
    instructions="Retrieve relevant data using available tools.",
    tools=[retrieve_tool],
)

# ဒေတာ ခွဲခြမ်းစိတ်ဖြာခြင်း အေးဂျင့်
agent_analyze = provider.as_agent(
    name="dataanalysis",
    instructions="Analyze the retrieved data and provide insights.",
    tools=[analyze_tool],
)

# တာဝန်တစ်ခုတွင် အေးဂျင့်များကို အဆက်မပြတ် လည်ပတ်ခြင်း
retrieval_result = await agent_retrieve.run("Retrieve sales data for Q4")
analysis_result = await agent_analyze.run(f"Analyze this data: {retrieval_result}")
print(analysis_result)
```

အဆိုပါကုဒ်တွင် ကြည့်ရသောအရာမှာ agent အများကြီးပူးပေါင်းလုပ်ဆောင်ခြင်းဖြင့် ဒေတာများကို အကဲဖြတ်ဆောင်ရွက်ရန် တာဝန်ထားသော task တစ်ခု ဖန်တီးခြင်း ဖြစ်သည်။ တစ်ဦးချင်း agent များသည် အထူးပြုလုပ်ငန်းများဆောင်ရွက်ကာ တာ၀န်ကို ရည်မှန်းထားသလို တကွ လုပ်ဆောင်သော ဖြေရှင်းမှုကို ရရှိစေသည်။ အထူးပြု agent များ ဖန်တီးခြင်းဖြင့် စွမ်းဆောင်ရည် နှင့် ထိရောက်မှု တိုးတက်စေသည်။

### အချိန်နှင့် တပြေးညီ လေ့လာခြင်း

Advanced frameworks များသည် အချိန်နှင့်တပြေးညီ အခြေအနေနားလည်ခြင်းနှင့် ကိုက်ညီမှု ပြုလုပ်ခြင်း စွမ်းဆောင်ရည်ရှိသည်။

**အသုံးပြုနည်း**: အဖွဲ့များသည် interactions များမှ သင်ယူကာ သက်ဆိုင်ရာ လုပ်ဆောင်မှုများကို သက်ဆိုင်ရာအခါမီ ပြင်ဆင်နိုင်သည့် feedback loop များ ထည့်သွင်းကာ စွမ်းရည်တိုးတက်မှုကို ဆက်လက်ပြုလုပ်နိုင်သည်။

**လက်တွေ့အသုံးပြုနည်း**: agent များသည် အသုံးပြုသူပြန်လည်တုံ့ပြန်မှု၊ ပတ်ဝန်းကျင်ဒေတာများနှင့် အလုပ်လုပ်ဆောင်မှု အပြောင်းအလဲများကို စူးစမ်းသုံးသပ်ပြီး သိမွတ်မှုအချက်အလက်များ update ပြုလုပ်ကာ ဆုံးဖြတ်ချက်ချမှု algorithm များမှန်ကန်စေရန် ဆက်လက်တိုးတက်မှုများ ပြုလုပ်ပါသည်။ ဤ iterative လေ့လာမှုက agent များအား ပတ်ဝန်းကျင် ပြောင်းလဲမှုအပေါ် မျှလင့်နိုင်စွမ်း ပြုလုပ်ပေးကာ User preference များနှင့် ကိုက်ညီမှုမြှင့်တင်ရန် ကူညီသည်။

## Microsoft Agent Framework နှင့် Microsoft Foundry Agent Service တို့အကြား ကွာခြားချက်များက ဘာတွေလဲ?

၎င်းတို့ ၏ ဒီဇိုင်း၊ စွမ်းဆောင်ရည် နှင့် ရည်ရွယ်ချက် အသုံးပြုမှု အရ မတူကြောင်းများစွာရှိသော်လည်း အဓိက ကြီးမားသော ကွာခြားချက်အချို့ကို အောက်တွင် ကြည့်ကြပါစို့ -

## Microsoft Agent Framework (MAF)

Microsoft Agent Framework သည် `FoundryChatClient` ကို အသုံးပြု၍ AI agent များ တည်ဆောက်ရာအတွက် တစ်နေရာထဲပြုထားသော SDK ဖြစ်သည်။ ဒီ Framework သည် Azure OpenAI မော်ဒယ်များကို အသုံးပြုကာ tool calling, စကားပြော စီမံခန့်ခွဲခြင်းနှင့် Azure Identity ဖြင့် စက်မှုအဆင့် ဘေးကင်းမှုကာကွယ်မှု ပံ့ပိုးပေးသည်။

**အသုံးပြုမှုများ**: tool အသုံးပြုခြင်း၊ multi-step လုပ်ငန်းစဉ်များနှင့် စက်မှုလက်မှတ်အတွင်းပေါင်းစည်းခြင်း များပါဝင်သော ထုတ်လုပ်ရေးရန် AI agent များ တည်ဆောက်ခြင်း။

Microsoft Agent Framework ၏ အရေးကြီးသော အတွေးအခေါ် အချို့မှာ -

- **Agents**. `FoundryChatClient` ဖြင့် agent ကို ဖန်တီးပြီး အမည်၊ညွှန်ကြားချက်များနှင့် tool များဖြင့် ကနေဖော်ပြခွင့် ရှိသည်။ Agent သည်-
  - အသုံးပြုသူ စကားများကို ဖြေကြားမှု အဖြစ် Azure OpenAI မော်ဒယ်ဖြင့် ပြန်လည် ဖြေဆိုနိုင်သည်။
  - စကားပြောအခြေအနေ အပေါ် မူတည်ပြီး အလိုအလျောက် tool call လုပ်နိုင်သည်။
  - စကားပြော အခြေအနေကို interaction များကြား ထိန်းသိမ်းထားနိုင်သည်။

အောက်ပါ ကုဒ် ဥပမာသည် agent တစ်ခု ဖန်တီးနည်းကို ပြသပါသည်။

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

- **Tools**. Framework သည် Python function များအဖြစ် tool များသတ်မှတ်ခြင်းကို ပံ့ပိုးသည်။ tool များကို agent ဖန်တီးစဉ် မှတ်ပုံတင်သည်။

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

- **Multi-Agent Coordination**. အထူးပြုလုပ်ငန်း ကွဲပြားသော agent များအများကြီးဖန်တီး၍ ၎င်းတို့၏ လုပ်ဆောင်မှုများကို ညှိနှိုင်းနိုင်သည်။

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

- **Azure Identity Integration**. Framework သည် `AzureCliCredential` သို့မဟုတ် `DefaultAzureCredential` ကို သုံး၍ API key မလိုအပ်ဘဲ လုံခြုံစိတ်ချစွာ အတည်ပြုနိုင်သည်။

## Microsoft Foundry Agent Service

Microsoft Foundry Agent Service သည် Microsoft Ignite 2024 တွင် မကြာသေးမီမှာ မိတ်ဆက် ပေးခဲ့ပြီး ပိုမိုလွယ်ကူသော မော်ဒယ်များဖြစ်သည့် Llama 3, Mistral, Cohere ကဲ့သို့သော open-source LLM များကို တိုက်ရိုက် ဖိတ်ခေါ်ကာ AI agent များ ဖန်တီး၊ တပ်ဆင်နိုင်သည်။

Microsoft Foundry Agent Service သည် စက်မှုအဆင့် လုံခြုံမှုစနစ်များနှင့် ဒေတာသိုလှောင်မှုနည်းလမ်းများ ပိုမိုကြီးမားစွာ ဖြည့်ဆည်းထားသည်၊ ၎င်းအား စက်မှုအသုံးပြုမှုများအတွက် သင့်လျော်ခြင်း ဖြစ်သည်။

Microsoft Agent Framework နှင့် ပေါင်းစပ်အသုံးပြုနိုင်၍ Agent များကို ဖန်တီး၊ တပ်ဆင် လုပ်ဆောင်ရာတွင် အထောက်အကူဖြစ်စေသည်။

ယခုအခါ Public Preview အဆင့်ရှိပြီး Python နှင့် C# ဖြင့် agent များ ဖန်တီးနိုင်သည်။

Microsoft Foundry Agent Service Python SDK ကို အသုံးပြု၍ user သတ်မှတ်ထားသော tool ပါရှိသော agent တစ်ခု ဖန်တီးနိုင်သည် -

```python
import asyncio
from azure.identity import DefaultAzureCredential
from azure.ai.projects import AIProjectClient

# ကိရိယာလုပ်ဆောင်ချက်များကိုသတ်မှတ်ပါ။
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

### အဓိကအတွေးအခေါ်များ

Microsoft Foundry Agent Service တွင် အဓိက အတွေးအခေါ်များမှာ -

- **Agent**. Microsoft Foundry Agent Service သည် Microsoft Foundry နှင့် ပေါင်းစပ်ထားသည်။ Microsoft Foundry အတွင်း AI Agent သည် "smart" microservice အဖြစ် လုပ်ဆောင်နိုင်ပြီး မေးခွန်းဖြေခြင်း (RAG), အရေးယူမှု ဆောင်ရွက်ခြင်း သို့မဟုတ် လုပ်ငန်းစဉ် အလိုအလျောက်ဖြေရှင်းမှုများ ပြုလုပ်နိုင်သည်။ ၎င်းသည် generative AI မော်ဒယ်များ ဖြင့် tool များ ပေါင်းစပ်ကာ အမြင်သာသော ဒေတာ အရင်းမြစ်များ ကို ချိတ်ဆက် ဆောင်ရွက်နိုင်စေသည်။ ဤမှာ agent ၏ ဥပမာ တစ်ခုဖြစ်သည် -

    ```python
    agent = project_client.agents.create_agent(
        model="gpt-5-mini",
        name="my-agent",
        instructions="You are helpful agent",
        tools=code_interpreter.definitions,
        tool_resources=code_interpreter.resources,
    )
    ```

    ဤဥပမာတွင် agent တစ်ခုကို `gpt-5-mini` မော်ဒယ်ဖြင့်၊ အမည် `my-agent` နှင့် ညွှန်ကြားချက် `You are helpful agent` ဖြင့် ဖန်တီးထားသည်။ Agent သည် code interpret လုပ်ငန်းများ ဆောင်ရွက်နိုင်ရန် tool နှင့် အရင်းအမြစ်များပါရှိသည်။

- **Thread နှင့် messages**. Thread သည် agent နှင့် အသုံးပြုသူ ကြား ဆက်သွယ်မှု ဒါမှမဟုတ် ပြောဆိုမှု ဖြစ်သည်။ Threads များဖြင့် ဆက်သွယ်မှု တိုးတက်မှုကို တွေ့ရှိ ထိန်းသိမ်းထားနိုင်ပြီး context အချက်အလက်များ သိမ်းဆည်း၍ interaction ၏ အခြေအနေကို စီမံနိုင်သည်။ ဤအောက်တွင် thread ၏ ဥပမာ တစ်ခုရှိသည် -

    ```python
    thread = project_client.agents.create_thread()
    message = project_client.agents.create_message(
        thread_id=thread.id,
        role="user",
        content="Could you please create a bar chart for the operating profit using the following data and provide the file to me? Company A: $1.2 million, Company B: $2.5 million, Company C: $3.0 million, Company D: $1.8 million",
    )
    
    # ကိုယ်စားလှယ်အား နွယ်တွဲပေါ်တွင် အလုပ်လုပ်ရန် တောင်းဆိုပါ
    run = project_client.agents.create_and_process_run(thread_id=thread.id, agent_id=agent.id)
    
    # ကိုယ်စားလှယ်၏ တုံ့ပြန်ချက်ကိုကြည့်ရှုရန် စာတိုက်များအားလုံးနဲ့ မှတ်တမ်းတင်ပါ
    messages = project_client.agents.list_messages(thread_id=thread.id)
    print(f"Messages: {messages}")
    ```

    အောက်ပါကုဒ်တွင် thread တစ်ခု ဖန်တီးပြီး message တစ်ခု ပို့ဆောင်သည်။ `create_and_process_run` ဟူသော function ကို ခေါ်ဆိုကာ agent ကို thread အပေါ် ဆောင်ရွက်ရန် တောင်းဆိုသည်။ နောက်ဆုံး messages များကို ရယူလို့ agent ၏ အဖြေကို မှတ်တမ်းတင်သည်။ messages များသည် စကားလုံး၊ ပုံ၊ ဖိုင် စသည့် အမျိုးအစား ခွဲခြားနိုင်သည်။ Developer များအနေဖြင့် response ကို နောက်ထပ် လက်ခံလုပ်ဆောင်ရန် သို့မဟုတ် အသုံးပြုသူသို့ တင်ပြရန် အသုံးတည့်သည်။

- **Microsoft Agent Framework နှင့် ပေါင်းစပ် အသုံးပြုမှု**. Microsoft Foundry Agent Service သည် Microsoft Agent Framework နှင့် ချိတ်ဆက်ပြီး ရောင်းအားဟောင်း agent များကို `FoundryChatClient` ဖြင့် ဖန်တီးကာ Agent Service မှတဆင့် ထုတ်လုပ်မှု အတွက် တပ်ဆင်နိုင်သည်။

**အသုံးပြုမှုများ**: Microsoft Foundry Agent Service သည် လုံခြုံမှုမြင့်မားပြီး၊ တိုးတက်နိုင်သော၊ ကြီးမားသော စက်မှု AI agent တပ်ဆင်မှုများအတွက် အထူးသင့်တော်သည်။

## ဒီနည်းလမ်းတွေ အကြားကွာခြားချက်ကဘာလဲ?
 
တချို့နေရာမှာတူညီမှု ရှိသော်လည်း ၎င်းတို့၏ ဒီဇိုင်း၊ စွမ်းဆောင်ရည် နှင့် ရည်ရွယ်ချက်အသုံးပြုမှုအရ အဓိက ကွာခြားချက်များ များသည် -
 
- **Microsoft Agent Framework (MAF)**: AI agents များ တည်ဆောက်ရန် ထုတ်လုပ်မှု အသင့် SDK ဖြစ်သည်။ tool calling, conversation management နှင့် Azure identity ပေါင်းစပ်မှုဖြင့် API ကို ရိုးရှင်းစွာ ပေးသည်။
- **Microsoft Foundry Agent Service**: Microsoft Foundry တွင် agents အတွက် ပလက်ဖောင်းနှင့် တပ်ဆင်မှု ဝန်ဆောင်မှုဖြစ်သည်။ Azure OpenAI, Azure AI Search, Bing Search နှင့် ကုဒ် ဆောင်ရွက်မှုတို့နှင့် Built-in ချိတ်ဆက်မှု ရှိသည်။
 
သင် အဘယ်ကို ရွေးချယ်ရမှာ မသေချာသေးပါလား?

### အသုံးပြုမှု ဥပမာများ
 
ဖြစ်နိုင်ခြေ အချို့ကို လေ့လာကြည့် လိုက်ကြရအောင် -
 
> Q: ထုတ်လုပ်ရေး AI agent applications များအတွက် အလျင်အမြန် ဆောင်ရွက်လိုသည်
>

>A: Microsoft Agent Framework သည် ကောင်းမွန်သော ရွေးချယ်မှုဖြစ်သည်။ `FoundryChatClient` မှတဆင့် tool နှင့် သတ်မှတ်ချက်များဖြင့် agent များကို ရိုးရှင်းသော Python API ဖြင့် အချုပ်အခြား ရေးသားနိုင်သည်။

>Q: Azure တွင် Search နှင့် code execution တိုက်ရိုက် ပေါင်းစည်းရန္ လုပ်ငန်းစဉ်အဆင့်စက်မှုအဆင့် တပ်ဆင်ဖို့လိုအပ်သည်
>
>A: Microsoft Foundry Agent Service သည် အကောင်းဆုံးဖြစ်သည်။ ပလက်ဖောင်း ဝန်ဆောင်မှုအနေဖြင့် မော်ဒယ်အမျိုးမျိုး၊ Azure AI Search, Bing Search နှင့် Azure Functions ပါဝင်မှုဖြင့် agent များ သက်သာစွာ ဖန်တီးကာ Foundry Portal မှတဆင့် ကြီးမားစွာ တပ်ဆင်နိုင်သည်။
 
> Q: အတိအကျ မသေချာသေးဘူး၊ ရွေးချယ်စရာ တစ်ခုပေးပါ
>
> A: Microsoft Agent Framework ဖြင့် agent များ ဖန်တီးပြီး နောက်ပိုင်းမှာ ထုတ်လုပ်မှုအတွက် Microsoft Foundry Agent Service ကို အသုံးပြု၍ တပ်ဆင်ချင်သလို ကြီးမားမှု ချဲ့ထွင်နိုင်သည်။ ဤနည်းလမ်းဖြင့် agent logic ကို အမြန် iterate လုပ်နိုင်ပြီး စက်မှုအဆင့် တပ်ဆင်မှုကို ရိုးရှင်းစွာ ပြုလုပ်နိုင်သည်။
 
အဓိက ကွာခြားချက်များကိုဇယား အတိုင်း စုစည်းကြည့်ပါ -

| Framework | အာရုံစိုက်ချက် | အဓိက အတွေးအခေါ်များ | အသုံးပြုမှုများ |
| --- | --- | --- | --- |
| Microsoft Agent Framework | Tool calling ပါရှိသော streamlined agent SDK | Agents, Tools, Azure Identity | AI agent များ တည်ဆောက်ခြင်း၊ tool အသုံးပြုခြင်း၊ multi-step workflows |
| Microsoft Foundry Agent Service | မော်ဒယ်ဖလွယ်ကူမှု၊ စက်မှု လုံခြုံမှု၊ Code generation၊ Tool calling | Modularity, Collaboration, Process Orchestration | လုံခြုံစိတ်ချရပြီး တိုးတက် ချဲ့ထွင်နိုင်သော AI agent တပ်ဆင်မှု |

## အသုံးပြုနေသော Azure ecosystem tools များကို တိုက်ရိုက် ပေါင်းစည်းနိုင်ပါသလား၊ သီးခြားဖြေရှင်းမှုလိုပါသလား?


ဟုတ်ကဲ့၊ သင်ရဲ့ ရှိပြီးသား Azure စနစ်ထဲကကိရိယာတွေကို Microsoft Foundry Agent Service နဲ့ တိုက်ရိုက် ပေါင်းစည်းနိုင်ပါတယ်၊ အထူးသဖြင့် အဲဒါဟာ အခြား Azure ဝန်ဆောင်မှုတွေနဲ့ ပေါင်းစည်းဖို့အတွက် အဆင်ပြေရေးနဲ့ တည်ဆောက်ထားတာဖြစ်ပါတယ်။ ဥပဒ်တစ်ရပ်အနေနဲ့ Bing၊ Azure AI Search နဲ့ Azure Functions တွေကို ပေါင်းစည်းနိုင်ပါတယ်။ Microsoft Foundry နဲ့ပါ အနက်ကပ်ပေါင်းသင်းမှုရှိပါတယ်။

Microsoft Agent Framework ကလည်း `FoundryChatClient` နဲ့ Azure ကိုယ်ပိုင်အမှတ်တံဆိပ်ဖြင့် Azure ဝန်ဆောင်မှုများနဲ့ ပေါင်းစည်းပြီး သင့်ရဲ့ agent ကိရိယာတွေထဲကနေ တိုက်ရိုက် Azure ဝန်ဆောင်မှုများကို ခေါ်ယူနိုင်ပါတယ်။

## နမူနာကုဒ်များ

- Python: [Agent Framework (Microsoft Foundry)](./code_samples/02-python-agent-framework.ipynb)
- Python: [Agent Framework (Azure OpenAI Responses API)](./code_samples/02-python-agent-framework-azure-openai.ipynb)
- .NET: [Agent Framework](./code_samples/02-dotnet-agent-framework.md)

## AI Agent Frameworks အကြောင်း မေးစရာများရှိပါသလား?

အခြား သင်ယူသူတွေနဲ့ တွေ့ဆုံ၊ အလုပ်ချိန်များတက်ရောက်ပြီး သင့်ရဲ့ AI Agents မှ မေးခွန်းများကို ဖြေရှင်းနိုင်ရန် [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D) ကို ဝင်ရောက်ပါ။

## ကိုးကားရင်းမြစ်များ

- <a href="https://techcommunity.microsoft.com/blog/azure-ai-services-blog/introducing-azure-ai-agent-service/4298357" target="_blank">Azure Agent Service</a>
- <a href="https://learn.microsoft.com/azure/ai-services/openai/how-to/responses" target="_blank">Microsoft Agent Framework - Azure OpenAI Responses</a>
- <a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Microsoft Foundry Agent Service</a>

## မကြာသေးမီက သင်ခန်းစာ

[AI Agent မိတ်ဆက်ခြင်းနှင့် Agent အသုံးချမှုလမ်းကြောင်းများ](../01-intro-to-ai-agents/README.md)

## နောက်တန်း သင်ခန်းစာ

[Agentic ဒီဇိုင်းပုံစံများနားလည်ခြင်း](../03-agentic-design-patterns/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ပြောကြားချက်**
ဤစာတမ်းကို AI ဘာသာပြန်ဝန်ဆောင်မှု [Co-op Translator](https://github.com/Azure/co-op-translator) အသုံးပြု၍ ဘာသာပြန်ထားပါသည်။ ကျွန်ုပ်တို့သည် တိကျမှန်ကန်မှုအတွက် ကြိုးပမ်းနေသော်လည်း၊ စက်ကိရိယာဘာသာပြန်ခြင်းများတွင် အမှားများ သို့မဟုတ် မှားယွင်းချက်များ ပါဝင်နိုင်ကြောင်း သတိပြုပါရန် လိုအပ်ပါသည်။ မူလစာတမ်းကို မူရင်းဘာသာဖြင့်သာ ယုံကြည်စိတ်ချရသော အချက်အလက်အဖြစ် သတ်မှတ်သင့်သည်။ အရေးကြီးသည့် သတင်းအချက်အလက်များအတွက် ပရော်ဖက်ရှင်နယ် လူသားဘာသာပြန်သူဝန်ဆောင်မှုကို အကြံပြုပါသည်။ ဤဘာသာပြန်ချက်ကို အသုံးပြုခြင်းမှ ဖြစ်ပေါ်လာသော နားလည်မှုကွာခြားမှုများ သို့မဟုတ် မမှန်ကန်သော အသုံးပြုမှုများအတွက် ကျွန်ုပ်တို့ တာဝန်မခံပါ။
<!-- CO-OP TRANSLATOR DISCLAIMER END -->