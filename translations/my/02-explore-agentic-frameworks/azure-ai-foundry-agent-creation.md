# Microsoft Foundry Agent Service ဖန်တီးခြင်းနှင့် တိုးတက်မှု

ဒီလေ့ကျင့်မှုမှာ၊ သင်သည် [Microsoft Foundry portal](https://ai.azure.com/?WT.mc_id=academic-105485-koreyst) တွင် Microsoft Foundry Agent Service ကိရိယာများကို အသုံးပြု၍ Flight Booking အတွက် agent တစ်ခု ဖန်တီးမှာဖြစ်သည်။ ဤ agent သည် အသုံးပြုသူများနှင့် ဆက်သွယ်နိုင်ပြီး ပျံသန်းခရီးစဉ်အကြောင်းအရာများကို ပေးအပ်နိုင်ပါမည်။

## လိုအပ်ချက်များ

ဒီလေ့ကျင့်မှုကို ပြီးစီးရန် အောက်ပါအရာများလိုအပ်ပါသည်။
1. စွမ်းဆောင်မှုရှိသော subscription ပါရှိသည့် Azure အကောင့်တစ်ခု။ [အကောင့်ကို အခမဲ့ဖန်တီးရန်](https://azure.microsoft.com/free/?WT.mc_id=academic-105485-koreyst)။
2. Microsoft Foundry hub ဖန်တီးခွင့်ရှိရမည် သို့မဟုတ် သင့်အတွက် ဖန်တီးထားရမည်။
    - သင့်အခန်းကဏ္ဍမှာ Contributor သို့မဟုတ် Owner ဖြစ်ပါက ဒီလုပ်ဆောင်ရန်လမ်းညွှန်ကိုလိုက်နာနိုင်ပါသည်။

## Microsoft Foundry hub တစ်ခု ဖန်တီးပါ

> **မှတ်ချက်**: Microsoft Foundry သည် ယခင်က Azure AI Studio ဟူ၍ အမည်ပေးခဲ့သည်။

1. Microsoft Foundry hub ဖန်တီးရန်အတွက် [Microsoft Foundry](https://learn.microsoft.com/en-us/azure/ai-studio/?WT.mc_id=academic-105485-koreyst) ဘလော့ဂ်ဆောင်းပါးမှ လမ်းညွှန်ချက်များကို လိုက်နာပါ။
2. သင့်ပရောဂျက် ပြီးမြောက်သည့်အခါ၊ ပြသထားသည့် အကြံပေးချက်များကို ပိတ်ပြီး Microsoft Foundry portal တွင် ပရောဂျက်စာမျက်နှာကို ပြန်လည်သုံးသပ်ပါ၊ အောက်ပါပုံနှင့် ဆင်တူသည်။

    ![Microsoft Foundry Project](../../../translated_images/my/azure-ai-foundry.88d0c35298348c2f.webp)

## မော်ဒယ်တင်ဆက်ခြင်း

1. သရဲပရောဂျက်အတွက် ဘယ်ဘက်က ပလိတ်ဖောင်းတွင်၊ **My assets** အပိုင်းက **Models + endpoints** စာမျက်နှာကို ရွေးချယ်ပါ။
2. **Models + endpoints** စာမျက်နှာတွင် **Model deployments** တက်ဘ်အောက်၊ **+ Deploy model** မီယူတွင် **Deploy base model** ကို ရွေးချယ်ပါ။
3. စာရင်းအတွင်း `gpt-4.1-mini` မော်ဒယ်ကို ရှာဖွေပြီး၊ ရွေးချယ်ကာ အတည်ပြုပါ။

    > **မှတ်ချက်**: TPM ကို လျော့ချခြင်းသည် သင့်အသုံးပြုနေသော subscription ၏ ကန့်သတ်မှုကို ကျော်လွန်မှုမှ ရှောင်ရှားစေရန် ကူညီပေးသည်။

    ![Model Deployed](../../../translated_images/my/model-deployment.3749c53fb81e18fd.webp)

## Agent တစ်ခု ဖန်တီးပါ

မော်ဒယ်တင်ဆက်ပြီးနောက်၊ သင်သည် agent တစ်ခု ဖန်တီးနိုင်ပါပြီ။ Agent သည် အသုံးပြုသူများနှင့် ဆက်သွယ်နိုင်သည့် စကားပြော AI မော်ဒယ်ဖြစ်သည်။

1. သရဲပရောဂျက်အတွက် ဘယ်ဘက်ပလိတ်ဖောင်းတွင် **Build & Customize** အပိုင်းအောက်မှာ **Agents** စာမျက်နှာကို ရွေးချယ်ပါ။
2. အသစ် agent ဖန်တီးရန် **+ Create agent** ကို နှိပ်ပါ။ **Agent Setup** ဒိုင်ယလုပ်ဘောက်စ်အောက်တွင်-
    - `FlightAgent` ကဲ့သို့ အေးဂျင့်အမည် တစ်ခု ထည့်ပါ။
    - မိမိ ပြင်ဆင်ထားသော `gpt-4.1-mini` မော်ဒယ်တင်ဆက်မှု ရွေးချယ်ထားပါစေ။
    - အေးဂျင့်ကို လိုက်နာစေမည့် **ညွှန်ကြားချက်များ** ကို သင်ယူဆောင်ရွက်လိုသည့် အတိုင်း သတ်မှတ်ပါ။ ဥပမာအဖြစ် -
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
> အပြည့်အစုံပုံစံငြိမ်းထားရာအတွက် [ဒီ repository](https://github.com/ShivamGoyal03/RoamMind) တွင် ပိုမိုသိရှိနိုင်ပါသည်။
    
> ထို့အတူ၊ အေးဂျင့်၏ စွမ်းဆောင်ရည်များ ထပ်မံတိုးတက်အောင် **Knowledge Base** နှင့် **Actions** များကို ထည့်သွင်းနိုင်ပြီး၊ အသုံးပြုသူ လိုအပ်ချက်များအရ အချက်အလက် ပိုမိုပေးနိုင်သော နှင့် အလိုအလျောက်လုပ်ဆောင်ချက်များ ပြုလုပ်နိုင်ပါသည်။ ဒီလေ့ကျင့်မှုအတွက် ထိုအဆင့်များကို ကျော်ဖြတ်နိုင်ပါသည်။
    
![Agent Setup](../../../translated_images/my/agent-setup.9bbb8755bf5df672.webp)

3. multi-AI agent အသစ် တစ်ခု ဖန်တီးရန် **New Agent** ကိုသာ နိပ်ပါ။ အသစ်ဖန်တီးလိုက်သည့် agent ကို Agents စာမျက်နှာတွင် ပြသပါလိမ့်မည်။


## Agent ကို စမ်းသပ်ကြည့်ပါ

Agent ဖန်တီးပြီးနောက်၊ Microsoft Foundry portal playground တွင် အသုံးပြုသူ မေးခွန်းများကို agent က ဘယ်လိုတုံ့ပြန်သနည်း စမ်းသပ်နိုင်ပါသည်။

1. Agent အတွက် **Setup** pane အပေါ်ထပ်တွင် **Try in playground** ကို ရွေးချယ်ပါ။
2. **Playground** pane တွင် စကားပြောပြန်လည်မှုကွင်းတွင် မေးခွန်းများရိုက်ထည့်၍ agent နှင့် မေးမြန်းဆက်သွယ်နိုင်ပါသည်။ ဥပမာ၊ သင်သည် ၂၈ ရက်နေ့တွင် Seattle မှ New York သို့ ပျံသန်းခရီးစဉ်များကို agent ကို ဖော်ပြရန် တောင်းနိုင်ပါသည်။

    > **မှတ်ချက်**: ဒီလေ့ကျင့်မှုတွင် အချိန်နှင့်တပြေးညီဒေတာ မသုံးရာကြောင့် agent ၏ တုံ့ပြန်ချက်များသည် စနစ်တကျဖြစ်နိုင်ခြေ မရှိပါ၊ လူကြိုက်များသော မေးခွန်းများကို နားလည်ပြီးတုံ့ပြန်နိုင်မှုကို စမ်းသပ်ခြင်းဖြစ်သည်။

    ![Agent Playground](../../../translated_images/my/agent-playground.dc146586de715010.webp)

3. Agent ကို စမ်းသပ်ပြီးနောက်၊ ၎င်း၏ စွမ်းဆောင်ရည်များ တိုးတက်အောင် များစွာသော အယူစေချင်ချက်များ၊ သင်ကြားမှုဒေတာများနှင့် လုပ်ဆောင်ချက်များ ထည့်သွင်း၍ ပိုမိုကောင်းမွန်အောင် ပြုပြင်နိုင်ပါသည်။

## အရင်းအမြစ်များ ရှင်းလင်းခွင့်ပြုခြင်း

စမ်းသပ်ပြီးနောက် agent ကိုဖျက်လိုက်ခြင်းဖြင့် ထပ်ဆောင်းကုန်ကျစရိတ်များမှ ကာကွယ်နိုင်ပါသည်။
1. [Azure portal](https://portal.azure.com) ကိုဖွင့်ပြီး ဒီလေ့ကျင့်မှုတွင် အသုံးပြုထားသည့် hub resource များတည်ရှိရာ resource group များကို ကြည့်ရှုပါ။
2. အကူအညီပြားဖက်မှာ **Delete resource group** ကို ရွေးချယ်ပါ။
3. resource group အမည် ထည့်ပြီး ဖျက်ပစ်လိုသည်ဆိုမှုကို အတည်ပြုပါ။

## အရင်းအမြစ်များ

- [Microsoft Foundry စာတမ်းအကြောင်းအရာ](https://learn.microsoft.com/en-us/azure/ai-studio/?WT.mc_id=academic-105485-koreyst)
- [Microsoft Foundry portal](https://ai.azure.com/?WT.mc_id=academic-105485-koreyst)
- [Microsoft Foundry နဲ့ စတင်ကျင့်ပြုခြင်း](https://techcommunity.microsoft.com/blog/educatordeveloperblog/getting-started-with-azure-ai-studio/4095602?WT.mc_id=academic-105485-koreyst)
- [Azure ပေါ်ရှိ AI agent များ၏ အခြေခံသဘောတရားများ](https://learn.microsoft.com/en-us/training/modules/ai-agent-fundamentals/?WT.mc_id=academic-105485-koreyst)
- [Azure AI Discord](https://aka.ms/AzureAI/Discord)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ပြောကြားချက်**
ဤစာတမ်းကို AI ဘာသာပြန်ဝန်ဆောင်မှု [Co-op Translator](https://github.com/Azure/co-op-translator) အသုံးပြု၍ ဘာသာပြန်ထားပါသည်။ ကျွန်ုပ်တို့သည် တိကျမှန်ကန်မှုအတွက် ကြိုးပမ်းနေသော်လည်း၊ စက်ကိရိယာဘာသာပြန်ခြင်းများတွင် အမှားများ သို့မဟုတ် မှားယွင်းချက်များ ပါဝင်နိုင်ကြောင်း သတိပြုပါရန် လိုအပ်ပါသည်။ မူလစာတမ်းကို မူရင်းဘာသာဖြင့်သာ ယုံကြည်စိတ်ချရသော အချက်အလက်အဖြစ် သတ်မှတ်သင့်သည်။ အရေးကြီးသည့် သတင်းအချက်အလက်များအတွက် ပရော်ဖက်ရှင်နယ် လူသားဘာသာပြန်သူဝန်ဆောင်မှုကို အကြံပြုပါသည်။ ဤဘာသာပြန်ချက်ကို အသုံးပြုခြင်းမှ ဖြစ်ပေါ်လာသော နားလည်မှုကွာခြားမှုများ သို့မဟုတ် မမှန်ကန်သော အသုံးပြုမှုများအတွက် ကျွန်ုပ်တို့ တာဝန်မခံပါ။
<!-- CO-OP TRANSLATOR DISCLAIMER END -->