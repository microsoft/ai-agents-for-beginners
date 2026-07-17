[![AI နည်းပညာကို စူးစမ်းလေ့လာခြင်း](../../../translated_images/my/lesson-2-thumbnail.c65f44c93b8558df.webp)](https://youtu.be/ODwF-EZo_O8?si=1xoy_B9RNQfrYdF7)

> _(ဓာတ်ပုံကိုနှိပ်၍ ဤသင်ခန်းစာ၏ ဗီဒီယိုကိုကြည့်ရှုနိုင်သည်)_

# AI Agent Framework များကို စူးစမ်းလေ့လာခြင်း

AI agent frameworks များမှာ AI agents များကို ဖန်တီးခြင်း၊ ထုတ်လုပ်ခြင်းနှင့် စီမံခန့်ခွဲခြင်းများကို လွယ်ကူစေဖို့ လည်ပတ်ပလက်ဖောင်းများဖြစ်သည်။ ဤ framework များက developer များအား အဆင့်မြင့် AI စနစ်များ ဖန်တီးရာတွင် ကြိုတင်ပြင်ဆင်ထားသော ကောက်နှုတ်ပစ္စည်းများ၊ abstraction များနှင့် ကိရိယာများကို တစ်နေရာတည်းမှ ဖော်ပြကူညီပေးသည်။

ဤ framework များသည် developer များကို AI agent ဖန်တီးခြင်း၌အထူးပြု သဘောတစ်ခုကို အာရုံစိုက်နိုင်ရန် ရောင်စုံသော စံတော်ချိန် များဖြင့် ပုံမှန် ပြဿနာ များကို ဖြေရှင်းနိုင်စေသည်။ ၎င်းတို့သည် AI စနစ် တည်ဆောက်ရေး၌ အတိုင်းအတာချဲ့ချဲ့မှု၊ ချိတ်ဆက်မှု နှင့် ထိရောက်မှုကို မြှင့်တင်ပေးပါသည်။

## နိဒါန်း 

ဤသင်ခန်းစာတွင် လေ့လာသွားမည့်အချက်များမှာ-

- AI Agent Framework များဆိုသည်မှာ ဘာလဲ၊ developer များကို ဘာသို့ အောင်မြင်စေလဲ။
- အဖွဲ့များသည် အကောင်းဆုံးပုံဖော်၊ ပြန်လည်သုံးသပ်ခြင်းနှင့် ၎င်းတို့၏ agent များ၏ စွမ်းရည်မြှင့်တင်ရေးကို မည်သို့ အသုံးချနိုင်သနည်း။
- Microsoft (<a href="https://aka.ms/ai-agents-beginners/ai-agent-service" target="_blank">Microsoft Foundry Agent Service</a> နှင့် <a href="https://learn.microsoft.com/azure/ai-services/openai/how-to/responses" target="_blank">Microsoft Agent Framework</a>) ဖန်တီးထားသည့် framework နှင့် ကိရိယာများအကြား မတူကွဲပြားမှုများ ရှိပါသလား။
- အကြံပေးခြင်းများ၊ အဖွဲ့အစည်းများ သုံးနေသည့် Azure စနစ်ကိရိယာများကိုတိုက်ရိုက် ပေါင်းစည်းနိုင်သလား၊ သီးသန့် ဖြေရှင်းနည်း များလိုအပ်သလား။
- Microsoft Foundry Agent Service ဆိုသည်မှာ ဘာလဲ၊ ဤသည်က ကျွန်ုပ်များအတွက် ဘယ်လို အကူအညီ ပေးပါသလဲ။

## လေ့လာရန် ရည်ရွယ်ချက်များ

ဤသင်ခန်းစာအားဖြင့် နားလည်စေလိုသည်မှာ-

- AI Agent Framework များ၏ AI ဖွံ့ဖြိုး တိုးတက်ရေး၌ အခန်းကဏ္ဍ။
- AI Agent Framework ကို အသုံးပြု၍ အတတ်ပညာရှိသော agents များ ဖန်တီးခြင်း။
- AI Agent Framework များက ပံ့ပိုးပေးသော အဓိက စွမ်းရည်များ။
- Microsoft Agent Framework နှင့် Microsoft Foundry Agent Service တို့၏ မတူကွဲပြားချက်များ။

## AI Agent Framework များဆိုသည်မှာ ဘာလဲ၊ developer များကို ဘာလုပ်ခွင့်ရစေသနည်း။

ရိုးရာ AI Framework များက သင်၏ application များတွင် AI ကို ပေါင်းစည်းကာ အောက်ပါအတိုင်း ကောင်းမွန်စေသော နည်းလမ်းများ ရှိသည်။

- **ကိုယ်ပိုင်စိတ်တိုင်းကျထောက်ပံ့မှု**: AI က အသုံးပြုသူ၏ကိုယ်ရေး အပြုအမူ နှင့် စိတ်ကြိုက်မှုများ ကို ချက်ချင်း ခွဲခြားခန့်မှန်းပြီး ကိုယ်ပိုင် အကြံဉာဏ်၊ အကြောင်းအရာနှင့် အတွေ့အကြုံများ ပေးဆောင်နိုင်သည်။
ဥပမာ - Netflix ကဲ့သို့ Video streaming ဝန်ဆောင်မှုများ သည် ကြည့်ရှုမှတ်တမ်းအပေါ် အခြေခံ၍ ရုပ်ရှင်များ သို့မဟုတ် အစီအစဉ်များကို အကြံပြုနိုင်၍ အသုံးပြုသူ စိတ်ဝင်စားမှု နှင့် အကျေနပ်မှုများ ပိုမိုတိုးတက်စေပါသည်။
- **အလိုအလျောက် စနစ်နှင့် ထိရောက်မှု**: AI က လုပ်ဆောင်ရူရာ စနစ်တစ်ခုလုံးတွင် တိုးတက်စေမည့် အလိုအလျောက် လုပ်ငန်းစဉ်များ၊ အလုပ်စဉ်များကို လျင်မြန်ထိရောက်စွာ စီမံခန့်ခွဲနိုင်ပါသည်။
ဥပမာ - Customer service application များမှာ AI အား အသုံးပြုပြီး chatbot များအား သုံးစွဲသူများမေးခွန်းများကို ဖြေရှင်းပေးကာ ဖြေကြားချိန်ကို လျှော့နည်းစေပြီး လူ့ အရာရှိများအား ပိုမိုခက်ခဲသည့် ပြဿနာများအတွက် အာရုံစိုက်ရန် ခွင့်ပြုပါသည်။
- **အသုံးပြုသူ အတွေ့အကြုံ မြှင့်တင်ခြင်း**: AI က အသံဖမ်းယူခြင်း၊ သဘာဝဘာသာစကား ဖြင့် ဆက်သွယ်နိုင်ခြင်းနှင့် ခန့်မှန်းရေးသားခြင်းစသည့် ဉာဏ်ကြီး features များထည့်သွင်းကာ အသုံးပြုသူအတွေ့အကြုံ တိုးတက်စေပါသည်။
ဥပမာ - Siri နှင့် Google Assistant ကဲ့သို့ အဓိကအသံဖမ်းယူပြီး ထိတွေ့ဆက်သွယ်မှု များလုပ်နိုင်စေသည်။

### အားလုံးကောင်းမွန်သလို AI Agent Framework အကြောင်း ဘာကြောင့် လိုအပ်သလဲ?

AI Agent framework များသည် AI framework ပုံမှန်ထက် ပိုမိုကြီးမားသော အရာတစ်ခုကို ကိုယ်စားပြုသည်။ ၎င်းများသည် အသုံးပြုသူ၊ အခြား agents များနှင့် ပတ်ဝန်းကျင်တို့အား ကျယ်ပြန့်စွာ ဆက်သွယ်နိုင်သော အသိဉာဏ် agent များ ဖန်တီးရန် အထောက်အကူပြုသည်။ ၎င်းတို့တွင် ကိုယ်ပိုင် ဆုံးဖြတ်ချက်များ ချနိုင်ခြင်း၊ ဖွဲ့စည်းမှု ပြောင်းလဲမှု အလိုက် ကိုက်ညီနိုင်ခြင်း အပါအဝင် autonomous လုပ်ဆောင်မှုများ ရှိသည်။

- **Agent များ၏ ပူးပေါင်းဆောင်ရွက်ခြင်း နှင့် ညှိနှိုင်းမှု**: အချက်အလက်များကို ချိတ်ဆက်မှုဖြင့် အတူတကွ လုပ်နိုင်စေခြင်း။
- **တာဝန်များအလိုက် အလုပ်ခွဲဝေရေး နှင့် စီမံခန့်ခွဲမှု**: လုပ်ငန်းစဉ်များကို မျက်မှောက်ဆုံးဖြတ်ပြီး အလုပ်ခွဲဝေရေးနှင့် dynamic စီမံခန့်ခွဲမှု ဖြစ်စေခြင်း။
- **ပတ်ဝန်းကျင် နားလည်မှု နှင့် ကျေနပ်မှု**: အချိန်နှင့်တပြေးညီ သတင်းအချက်အလက်များ အသိနားလည်ပြီး ဆုံးဖြတ်ချက်များ ချနိုင်မှု။

တိုတို ထုတ်ဖော်ရမည့်အချက်မှာ agent များက မည်သည့် automation တွေလည်းဆို စနစ်များ ပိုမိုအသိဉာဏ်ရှိစေရန် အကျိုးရှိစေသည်။

## Agent ၏ စွမ်းရည်အား မြန်မြန်ဆန်ဆန် prototype ပြုလုပ်၊ ပြန်လည်ကောက်နုတ် နေရာချမှု ဘာတွေ လုပ်လို့ရသလဲ?

AI Agent Framework များတွင် အများအားဖြင့် module components, ပူးပေါင်းဆောင်ရွက်မှုကိရိယာများ၊ နှင့် real-time learning ပိုင်းများ ပါဝင်ပြီး prototype လုပ်ရန် အထောက်အကူ ဖြစ်စေသည်။ ဤအချက်များကို လေ့လာကြမည်။

- **Module Components အသုံးပြုခြင်း**: AI SDK များတွင် AI နှင့် Memory connectors၊ function call များကို သဘာဝဘာသာဖြင့် သို့မဟုတ် code plugins ဖြင့် အသုံးပြုနိုင်သော ကိရိယာများ၊ prompt templates များ ကြိုတင်အသင့်ရှိသည်။
- **ပူးပေါင်းဆောင်ရွက်မှု ကိရိယာများ အသုံးပြုခြင်း**: agents များကို တိကျသော ဘာသာရပ် နှင့် တာဝန်များဖြင့် ဒီဇိုင်းလုပ်ကာ ပူးပေါင်းဆောင်ရွက်မှု ကို စမ်းသပ်ပြုပြင်နိုင်သည်။
- **တက်ကြွသော Real-Time သင်ယူမှု**: agents များသည် ဆက်သွယ်မှုများမှ သင်ယူပြီး တုံ့ပြန်မှုများ ပြောင်းလဲခြင်းများ ပြုလုပ်ပါသည်။

### Module Components အသုံးပြုခြင်း

Microsoft Agent Framework ကဲ့သို့သော SDK များတွင် AI connectors၊ tool definition များနှင့် agent စီမံခန့်ခွဲမှု ကြိုတင်ထည့်သွင်းထားသော components များ ပါဝင်သည်။

**အဖွဲ့များအသုံးချပုံ**: အဖွဲ့များသည် အစမှ စတင်မလုပ်ဘဲသာ components များကို မြန်မြန် ပေါင်းစည်းကာ functional prototype တည်ဆောက်နိုင်သည်။

**လေ့ကျင့်သုံးစွဲပုံ**: အသုံးပြုသူထဲက input ပေါ်မှ အချက်အလက် ထုတ်ယူရန် parser အသုံးပြုခြင်း၊ ဒေတာ သိမ်းဆည်းရန် memory module ကို သုံးခြင်း၊ အသုံးပြုသူနှင့် ဆက်သွယ်ရန် prompt generator ကို အသုံးပြုခြင်း စသည်ဖြင့် components များကို တည်ဆောက်မှုမလိုဘဲ အသုံးပြုနိုင်သည်။

**ဥပမာကုဒ်**: Microsoft Agent Framework နဲ့ `FoundryChatClient` အသုံးပြုပြီး အသုံးပြုသူ input အပေါ် တုံ့ပြန်မှု tool calling ဖြင့် ဆောင်ရွက်ပုံကို ကြည့်ပါ။

``` python
# Microsoft Agent Framework Python နမူနာ

import asyncio
import os

from agent_framework import tool
from agent_framework.foundry import FoundryChatClient
from azure.identity import AzureCliCredential


# ခရီးသွားဘောက်ချ ခြင်းအတွက် နမူနာကိရိယာအလုပ်လုပ်ငန်းဖန်တီးပါ
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
    # နမူနာထွက်ရှိခြင်း: ၂၀၂၅ ခုနှစ်၊ ဇန်နဝါရီ ၁ ရက်နေ့မှာ သင်ရဲ့ New York သို့ မောင်းနှင်မည့် လေယာဉ်လက်မှတ်ကို အောင်မြင်စွာဘောက်ချပြီး ဖြစ်ပါပြီ။ ခရီးသွားရာလမ်းမှာ ဘေးကင်းစေပါစေ! ✈️🗽


if __name__ == "__main__":
    asyncio.run(main())
```

ဤဥပမာတွင် အသုံးပြုသူ input မှ တစ်ခုတည်းသော flight booking request အချက်အလက်များ (မူလတည်နေရာ၊ သွားမည့်နေရာ၊ ရက်စွဲ) အပါအဝင် အချက်အလက် အဓိကများကို parser ဖြင့် ထုတ်ယူနိုင်မှု အတွက် ဒီ modular နည်းလမ်းကို အသုံးပြုပါသည်။

### ပူးပေါင်းဆောင်ရွက်မှု ကိရိယာများ အသုံးပြုခြင်း

Microsoft Agent Framework ကဲ့သို့ framework များသည် ပူးပေါင်းဆောင်ရွက်နိုင်သော အများ agent များ ဖန်တီးရန် ကူညီပေးသည်။

**အဖွဲ့များ အသုံးပြုနည်း**: agent များတချက်တည်းကျ အကြောင်းအရာ သတ်မှတ် တာဝန်များပေး၍ workflow များကို စမ်းသပ်ပြင်ဆင်နိုင်သည်။

**အသုံးအဆောင်ပုံ**: အဖွဲ့တစ်ခုမှာ data retrieval, သုံးသပ်ခြင်း နှင့် ဆုံးဖြတ်မှုများ ဆောင်ရွက်သည့် specialized agent များ ပါဝင်ခြင်း။ သူတို့ဟာ တစ်ဦးနှင့် တစ်ဦး ဆက်သွယ်၍ တစ်နိုင်ငံလုံးအတွက် ရည်မှန်းချက်တစ်ခု အောင်မြင်ရန် အလုပ်လုပြုသည်။

**ဥပမာကုဒ် (Microsoft Agent Framework)**:

```python
# Microsoft Agent Framework ကို အသုံးပြု၍ အတူတကွ လုပ်ဆောင်သောအေးဂျင့်များ များစွာ ဖန်တီးခြင်း

import os
from agent_framework.foundry import FoundryChatClient
from azure.identity import AzureCliCredential

provider = FoundryChatClient(
    project_endpoint=os.environ["AZURE_AI_PROJECT_ENDPOINT"],
    model=os.environ["AZURE_AI_MODEL_DEPLOYMENT_NAME"],
    credential=AzureCliCredential(),
)

# ဒေတာ ရယူရေး အေးဂျင့်
agent_retrieve = provider.as_agent(
    name="dataretrieval",
    instructions="Retrieve relevant data using available tools.",
    tools=[retrieve_tool],
)

# ဒေတာ ခွဲခြမ်းစိတ်ဖြာရေး အေးဂျင့်
agent_analyze = provider.as_agent(
    name="dataanalysis",
    instructions="Analyze the retrieved data and provide insights.",
    tools=[analyze_tool],
)

# တစ်ခုချင်း စဉ်လိုက် အေးဂျင့်များကို တာဝန်တစ်ခု၌ ပြေးဆွဲခြင်း
retrieval_result = await agent_retrieve.run("Retrieve sales data for Q4")
analysis_result = await agent_analyze.run(f"Analyze this data: {retrieval_result}")
print(analysis_result)
```

နောက်ဆုံးကုဒ်တွင် မျက်မှောက် multiple agent များကို data ကို သုံးသပ်ရန် တာဝန် ဖန်တီးပုံကို ကြည့်နိုင်သည်။ ဒေသအလိုက် agent တစ်ဦးချင်းစီသည် အထူးတောက်လျှောက် တာဝန်ယူပြီး၊ အဖွဲ့အစည်းပေါင်းစည်းမှုဖြင့် စီမံကိန်းများပြီးစီးသည်။ ဤကြောင်း agents များကို သတ်မှတ်ပြီးစိတ်ကြိုက်တာဝန်များတွက် စောင့်ရှောက်မှု မြင့်တက်သည်။

### Real-Time သင်ယူမှု

အဆင့်မြင့် framework များသည် real-time context နားလည်မှု နှင့် လိုက်လျောညီထွေမှု စွမ်းရည်များ ပံ့ပိုးပေးသည်။

**အဖွဲ့များ အသုံးချပုံ**: agents များသည် အပြန်အလှန် ဆက်သွယ်မှုမှ သင်ယူကာ လုပ်ဆောင်မှု ချိန်ညှိမှုများ ပြုလုပ်နိုင်သည်၊ ၎င်းတို့၏စွမ်းရည် သာမန် မပြေလည်မှု များတိုးတက်စေရန်။

**အသုံးအဆောင်ပုံ**: agents များသည် အသုံးပြုသူတုံ့ပြန်ချက်၊ ပတ်ဝန်းကျင် ဒေတာနှင့် တာဝန်ရလဒ်များကို စိစစ်ကာ ဗဟုသုတ ပြုပြင်။ ဆုံးဖြတ်ချက် ချမှု အယ်လ်ဂိုရစ်သမ်များ ပြုပြင်တိုးတက်စေနိုင်ပြီး စနစ်ချဲ့ထွင်မှု မြင့်တက်စေသည်။

## Microsoft Agent Framework နှင့် Microsoft Foundry Agent Service တို့ အကြား မတူကွဲပြားချက်များ ဘာတွေလဲ?

အထူးသဖြင့် ဒီ design, စွမ်းရည်များနှင့် ရည်မှန်းထားသော အသုံးပြုမှုများအရ သုံးသပ်လို့ရသည့် အချက်အလက်အချို့က如下:

## Microsoft Agent Framework (MAF)

Microsoft Agent Framework သည် `FoundryChatClient` အသုံးပြု၍ AI agents ဖန်တီးရန် အပစ်အခတ် လုံလောက်သည့် SDK ဖြစ်သည်။ Azure OpenAI မော်ဒယ်များအား အစွမ်းထက် tool calling, စကားဝိုင်း စီမံခန့်ခွဲမှု နှင့် လုံခြုံရေး စနစ်များဖြင့် ထောက်ပံ့သည်။

**အသုံးပြုမှု များ**: tool အသုံးပြုခြင်း၊ multi-step workflow များနှင့် လုပ်ငန်း အဖွဲ့ချုပ်မြင့်စနစ်များ ဖန်တီးရာတွင် သာယာလှပသည်။

Microsoft Agent Framework ၏ အဓိက အယူအဆများမှာ:

- **Agents**. `FoundryChatClient` ဖြင့် ဖန်တီးပြီး အမည်၊ အညွှန်း၊ tool များဖြင့် ပြင်ဆင်ထားသည်။ agent တွင်-
  - **အသုံးပြုသူ မက်ဆေ့ချ်များ နှင့် Azure OpenAI မှ တုံ့ပြန်မှု ထုတ်ပေးခြင်း**။
  - **စကားဝိုင်း context အတိုင်း အလိုအလျောက် tool များကိုခေါ်ယူခြင်း**။
  - **စကားဝိုင်းအခြေအနေကို နှစ်ချက်နှစ်ကြိမ် ထိန်းသိမ်းခြင်း**။

  ထိုကဲ့သို့ agent ဖန်တီးခုံတုရန် ကုဒ်နမူနာ:

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

- **Tools**. framework က agent သတ်မှတ်ရာတွင် Python function အဖြစ် tool များကို ထည့်သွင်းအသုံးပြု လို၍ မှတ်ပုံတင်နိုင်သည်။

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

- **Multi-Agent Coordination**. နယ်ပယ်အလိုက် မတူသော agent များကိုဖန်တီးပြီး ဆက်ဆံနိုင်သည်။

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

- **Azure Identity Integration**. `AzureCliCredential` (သို့) `DefaultAzureCredential` ကို အသုံးပြုကာ API key မလိုတော့ဘဲ လုံခြုံစိတ်ချစေသည်။

## Microsoft Foundry Agent Service

Microsoft Foundry Agent Service သည် Microsoft Ignite 2024 တွင် မကြာမီ မိတ်ဆက်ခဲ့ပြီး AI agents ဖန်တီးခြင်း၊ ထုတ်လုပ်ခြင်းနှင့် open-source LLM များ (Llama 3, Mistral, Cohere) ကို တိုက်ရိုက် ခေါ်ဆောင်လို့ရသည့် ပလက်ဖောင်းဖြစ်သည်။

Microsoft Foundry Agent Service သည် လုံခြုံရေးနှင့် ဒေတာသိမ်းဆည်းမှု နည်းလမ်းများ တိုးတက်ကောင်းမွန်ပြီး လုပ်ငန်းသုံး အပလီကေးရှင်းများအတွက် သင့်တော်သည်။

Microsoft Agent Framework နှင့် ပေါင်း၍ agent များကို တည်ဆောက်ခြင်းနှင့် ထုတ်လုပ်ခြင်း လုပ်ငန်းများကို အလွယ်တကူ လုပ်ဆောင်နိုင်သည်။

ဤ၀န်ဆောင်မှုသည် အခုအချိန်တွင် Public Preview အဆင့်တွင် ရှိပြီး Python နှင့် C# ဖြင့် agent ဖန်တီးနိုင်သည်။

Microsoft Foundry Agent Service Python SDK အသုံးပြုပြီး user သတ်မှတ် tool ပါဝင်သော agent ဖန်တီးခြင်း-

```python
import asyncio
from azure.identity import DefaultAzureCredential
from azure.ai.projects import AIProjectClient

# ကိရိယာလုပ်ဆောင်ချက်များကို သတ်မှတ်ပါ။
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
        model="gpt-4.1-mini",
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

### အဓိက အယူအဆများ

Microsoft Foundry Agent Service ၏ အဓိက အယူအဆများမှာ-

- **Agent**. Microsoft Foundry Agent Service သည် Microsoft Foundry နှင့်ပေါင်းစည်းပြီး AI Agent များကို "smart" microservice အဖြစ် အသုံးပြု၍ မေးခွန်းများ ဖြေဆိုခြင်း (RAG), လုပ်ဆောင်ချက်များ ဆောင်ရွက်ခြင်း သို့မဟုတ် workflows များ အလိုအလျောက် ပြုလုပ်ခြင်းတို့ အတွက် အသုံးပြုသည်။ ၎င်းသည် မော်ဒယ် AI ဝိုင်းတွဲ စွမ်းအားနှင့် real-world ဒေတာရင်းမြစ်များကို ချိတ်ဆက် ခံစားသုံးနိုင်စေသော ကိရိယာများကို ပေါင်းစည်းထားသည်။ agent ပုံစံ တစ်ခု တွေ့ရစေပါသည်။

    ```python
    agent = project_client.agents.create_agent(
        model="gpt-4.1-mini",
        name="my-agent",
        instructions="You are helpful agent",
        tools=code_interpreter.definitions,
        tool_resources=code_interpreter.resources,
    )
    ```

    ဤဥပမာတွင် `gpt-4.1-mini` မော်ဒယ်ဖြင့် agent တစ်ခုဖန်တီးပြီး၊ အမည် `my-agent` နှင့် သင်ကြားချက် `You are helpful agent` ပါရှိသည်။ agent သည် code interpret task များ ပြုလုပ်ရန် tool များ နှင့် အရင်းအမြစ်များ ဖြင့် စွမ်းဆောင်ရည်ထောက်ပံ့ထားသည်။

- **Thread နှင့် messages**. Thread ဆိုသည်မှာ agent နှင့် အသုံးပြုသူ တို့ ပတ်သတ်သည့် စကားဝိုင်း သို့မဟုတ် ဆက်သွယ်မှု ဖြစ်သည်။ Thread များတွင် စကားဝိုင်း တိုးတက်မှုကို ထိန်းသိမ်းရန် context သိမ်းဆည်းမှုနှင့် interaction အခြေအနေစီမံခန့်ခွဲမှုများ ပြုလုပ်နိုင်သည်။ thread ၏ ဥပမာ-

    ```python
    thread = project_client.agents.create_thread()
    message = project_client.agents.create_message(
        thread_id=thread.id,
        role="user",
        content="Could you please create a bar chart for the operating profit using the following data and provide the file to me? Company A: $1.2 million, Company B: $2.5 million, Company C: $3.0 million, Company D: $1.8 million",
    )
    
    # တစ်ခုချင်းစီအတွက် အေဂျင့်ကို လုပ်ငန်းစဉ်များပြုလုပ်ရန် တောင်းဆိုပါ
    run = project_client.agents.create_and_process_run(thread_id=thread.id, agent_id=agent.id)
    
    # အေဂျင့်၏တုံ့ပြန်ချက်တွေကို ကြည့်ရှုနိုင်ရန် မက်ဆေ့ခ်ျအားလုံးကို ရယူပြီး မှတ်တမ်းတင်ပါ
    messages = project_client.agents.list_messages(thread_id=thread.id)
    print(f"Messages: {messages}")
    ```

    ယခင်ကုဒ်တွင် thread တစ်ခု ဖန်တီးပြီး message တစ်ခု ကို thread ထဲသို့ ပို့သည်။ `create_and_process_run` ကို ခေါ်၍ agent ကို အလုပ်လုပ်အပ်သည်။ နောက်ဆုံးတွင် messages များကို ရယူ၍ သင်ကြားချက် ထုတ်ပြပုံတွင် agent ၏ တုံ့ပြန်မှုများအား မှတ်တမ်းတင်သည်။ messages များတွင် စာသား၊ ဓာတ်ပုံ သို့မဟုတ် ဖိုင် အမျိုးအစားရှိနိုင်ပြီး developer က ၎င်းတို့ကို ထပ်မံ လုပ်ဆောင်ရန် သုံးနိုင်သည်။

- **Microsoft Agent Framework နှင့် ပေါင်းစည်းမှု**. Microsoft Foundry Agent Service သည် Microsoft Agent Framework နှင့် လက်တွဲ၍ `FoundryChatClient` ကို အသုံးပြုပြီး agent များကို တည်ဆောက်ပြီး ထုတ်လုပ်နိုင်သည်။

**အသုံးပြုမှု များ**: လုံခြုံ၍ ကျယ်ပြန့် ချဲ့ထွင်နိုင်ချင်သည့် လုပ်ငန်းသုံး AI agent တည်ဆောက်ခြင်း၌ သင့်တော်သည်။

## ဤနည်းလမ်းများ အကြား မတူကွဲပြားချက်များ မည်သို့ရှိသနည်း?
 
တူညီချက်များ ရှိသော်လည်း၊ design, စွမ်းရည်များ နှင့် ရည်ရွယ်ချက် အသုံးပြုမှုများအရ အဓိကမတူကွဲပြားပါသည်။
 
- **Microsoft Agent Framework (MAF)**: AI agent ဖန်တီးရန် အသုံးချရလွယ်ကူပြီး ထုတ်လုပ်မှုပြည့်စုံသော SDK ဖြစ်သည်။ tool calling, စကားဝိုင်း စီမံခန့်ခွဲမှုနှင့် Azure identity ပေါင်းစပ် API ပေးသည်။
- **Microsoft Foundry Agent Service**: Microsoft Foundry ၏ ပလက်ဖောင်းနှင့် ထုတ်လုပ်မှု ဝန်ဆောင်မှုဖြစ်ပြီး Azure OpenAI, Azure AI Search, Bing Search နှင့် code execution အား built-in ချိတ်ဆက်မှုများ ပံ့ပိုးပေးသည်။
 
ရွေးချယ်ရန် မသေချာသေးလျှင်?

### အသုံးပြုမှုများ
 
အောက်တွင် လူကြိုက်များသော အသုံးများကို စာမျက်နှာတစ်ခုဆွဲကြည့်ကြမယ်-
 
> Q: ကျွန်ုပ်သည် ထုတ်လုပ်မှု AI agent အက်ပလီကေးရှင်းများ တည်ဆောက်လိုပြီး လျင်မြန်စတင်လိုသည်
>

>A: Microsoft Agent Framework သည် အလွန်သင့်တော်သောရွေးချယ်မှုတစ်ခုဖြစ်သည်။ `FoundryChatClient` အလွယ်တကူအသုံးပြုနိုင်ပြီး tools နှင့် များသော သတ်မှတ်ချက်များ ပါဝင်သည်။

>Q: Azure Search, code execution ကဲ့သို့ လုပ်ငန်းအသုံးပြုသော လုံခြုံစိတ်ချစေရန် deployment လိုသည်
>
> A: Microsoft Foundry Agent Service သည် ကောင်းမွန်သောရွေးချယ်မှုဖြစ်သည်။ platform ဝန်ဆောင်မှုဖြစ်ပြီး multiple model များ၊ Azure AI Search, Bing Search, Azure Functions များ built-in ပါဝင်ကာ Foundry Portal မှ တွဲဖက် ဖန်တီး နှင့် ထုတ်လုပ်နိုင်သည်။
 
> Q: နားမလည်သေးပါ၊ တစ်ခုသာရွေးပေးပါ
>
> A: အရင်ဆုံး Microsoft Agent Framework ဖြင့် agent များ ဖန်တီးပြီး ထို့နောက် Microsoft Foundry Agent Service ကို အသုံးပြုပြီး ထုတ်လုပ်မှု မွေးမြူပါ။ ဒါက logic ကိုလျင်မြန်စွာ ပြုပြင်နိုင်ပြီး enterprise deployment အဆင့်သို့ ရောက်ခွင့်ပေးပါသည်။
 
အဓိက မတူကွဲပြားချက်များကို အောက်ကဇယားတွင် တင်ပြထားသည်-

| Framework | အခြေစိုက်ရာ | အဓိက အယူအဆ | အသုံးပြုမှုများ |
| --- | --- | --- | --- |
| Microsoft Agent Framework | tool calling ပါဝင်သော streamlined agent SDK | Agents, Tools, Azure Identity | AI agent ဖန်တီးခြင်း၊ tool အသုံးပြုမှု၊ multi-step workflow များ |
| Microsoft Foundry Agent Service | အဆင်ပြေသော မော်ဒယ်များ၊ လုပ်ငန်းလုံခြုံမှု၊ code generate, tool calling | Modularity, Collaboration, Process Orchestration | လုံခြုံကာ ကျယ်ပြန့်စွာ AI agent ထုတ်လုပ်ခြင်း |

## ကျွန်ုပ်၏ရှိပြီးသား Azure စနစ်ကိရိယာများကို တိုက်ရိုက် ပေါင်းစည်းနိုင်သလား ဘယ်လိုဖြေရှင်းမှုလိုအပ်သလဲ?


ဟုတ်ကဲ့၊ သင်၏ ရှိပြီးသား Azure ecosystem ကိရိယာများကို Microsoft Foundry Agent Service နှင့် တိုက်ရိုက်ပေါင်းစည်းနိုင်ပါတယ်၊ အထူးသဖြင့် အခြား Azure ဝန်ဆောင်မှုများနှင့် မဖြစ်မနေ ပေါင်းစည်းနိုင်ရန်အတွက် တည်ဆောက်ထားသောကြောင့်ပါ။ ဥပမာအားဖြင့် Bing, Azure AI Search နှင့် Azure Functions ကို ပေါင်းစည်းနိုင်ပါတယ်။ Microsoft Foundry နှင့်လည်း အနက်ရှိုင်းဆုံးပေါင်းစည်းမှုရှိပါတယ်။

Microsoft Agent Framework သည် `FoundryChatClient` နှင့် Azure အတည်ပြုခြင်းအားဖြင့် Azure ဝန်ဆောင်မှုများနှင့် ပေါင်းစည်းပြီး သင်၏ agent ကိရိယာများမှ Azure ဝန်ဆောင်မှုများကို တိုက်ရိုက်ခေါ်သုံးစွဲနိုင်စေပါတယ်။

## နမူနာကုဒ်များ

- Python: [Agent Framework (Microsoft Foundry)](./code_samples/02-python-agent-framework.ipynb)
- Python: [Agent Framework (Azure OpenAI Responses API)](./code_samples/02-python-agent-framework-azure-openai.ipynb)
- .NET: [Agent Framework](./code_samples/02-dotnet-agent-framework.md)

## AI Agent Frameworks သက်ဆိုင်သော အသေးစိတ် မေးမြန်းလိုပါသလား?

[Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D) တွင်ပူးပေါင်းပြီး သင်တန်းသားများနှင့် တွေ့ဆုံဆွေးနွေးရန်၊ နေ့လယ်စာရင်းမိတ်ဆက်ပေးဆွေးနွေးရန်နှင့် သင့် AI Agents မေးခွန်းများကို ဖြေပေးနိုင်သည်။

## ကိုးကားချက်များ

- <a href="https://techcommunity.microsoft.com/blog/azure-ai-services-blog/introducing-azure-ai-agent-service/4298357" target="_blank">Azure Agent Service</a>
- <a href="https://learn.microsoft.com/azure/ai-services/openai/how-to/responses" target="_blank">Microsoft Agent Framework - Azure OpenAI Responses</a>
- <a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Microsoft Foundry Agent Service</a>

## ယခင်သင်ခန်းစာ

[Introduction to AI Agents and Agent Use Cases](../01-intro-to-ai-agents/README.md)

## နောက်တစ်ခန်း သင်ခန်းစာ

[Understanding Agentic Design Patterns](../03-agentic-design-patterns/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ပြောကြားချက်**
ဤစာတမ်းကို AI ဘာသာပြန်ဝန်ဆောင်မှု [Co-op Translator](https://github.com/Azure/co-op-translator) အသုံးပြု၍ ဘာသာပြန်ထားပါသည်။ ကျွန်ုပ်တို့သည် တိကျမှန်ကန်မှုအတွက် ကြိုးပမ်းနေသော်လည်း၊ စက်ကိရိယာဘာသာပြန်ခြင်းများတွင် အမှားများ သို့မဟုတ် မှားယွင်းချက်များ ပါဝင်နိုင်ကြောင်း သတိပြုပါရန် လိုအပ်ပါသည်။ မူလစာတမ်းကို မူရင်းဘာသာဖြင့်သာ ယုံကြည်စိတ်ချရသော အချက်အလက်အဖြစ် သတ်မှတ်သင့်သည်။ အရေးကြီးသည့် သတင်းအချက်အလက်များအတွက် ပရော်ဖက်ရှင်နယ် လူသားဘာသာပြန်သူဝန်ဆောင်မှုကို အကြံပြုပါသည်။ ဤဘာသာပြန်ချက်ကို အသုံးပြုခြင်းမှ ဖြစ်ပေါ်လာသော နားလည်မှုကွာခြားမှုများ သို့မဟုတ် မမှန်ကန်သော အသုံးပြုမှုများအတွက် ကျွန်ုပ်တို့ တာဝန်မခံပါ။
<!-- CO-OP TRANSLATOR DISCLAIMER END -->