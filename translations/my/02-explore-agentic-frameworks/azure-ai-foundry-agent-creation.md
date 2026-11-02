# Microsoft Foundry Agent Service Development

ဒီလေ့ကျင့်မှုမှာ သင်က [Microsoft Foundry portal](https://ai.azure.com/?WT.mc_id=academic-105485-koreyst) ရဲ့ Microsoft Foundry Agent Service tools ကို အသုံးပြုပြီး Flight Booking အတွက် အေးဂျင့်တစ်ခု ဖန်တီးမှာဖြစ်ပါတယ်။ အဆိုပါ အေးဂျင့်က အသုံးပြုသူတွေနဲ့ ဆက်သွယ်ပြီး ဦးလာသောဂလုပ်နစ်အကြောင်း အချက်အလက်များ ပေးနိုင်ပါလိမ့်မယ်။

## မလိုအပ်သောအရာများ

ဒီလေ့ကျင့်မှုကိုအပြီးသတ်ရန် သင်လိုအပ်သည်။
၁။ စစ်ဆင်နေသည့် subscription ပါရှိသော Azure အကောင့်တစ်ခု။ [အခမဲ့အကောင့်ဖန်တီးရန်](https://azure.microsoft.com/free/?WT.mc_id=academic-105485-koreyst)။
၂။ Microsoft Foundry hub ဖန်တီးရန် ခွင့်ပြုချက်ရှိရမည်၊ သို့မဟုတ် သင်အတွက် ဖန်တီးပေးထားရမည်။
    - သင်၏ အခန်းကဏ္ဍသည် Contributor သို့မဟုတ် Owner ဖြစ်ပါက ဒီသင်ခန်းစာအတွင်း ဦးတည်ချက်များကို လိုက်နာနိုင်ပါသည်။

## Microsoft Foundry hub ဖန်တီးခြင်း

> **အရေးကြီး**: Microsoft Foundry ကို ယခင်က Azure AI Studio ဟု သိရှိခဲ့သည်။

၁။ Microsoft Foundry hub ဖန်တီးရန် [Microsoft Foundry](https://learn.microsoft.com/en-us/azure/ai-studio/?WT.mc_id=academic-105485-koreyst) ဘလော့ဂ်ပိုစ့်ထဲက ဥပမာလမ်းညွှန်ချက်များကိုလိုက်နာပါ။
၂။ သင်၏စီမံကိန်း ဖန်တီးပြီးပါက ပြသနေသော အကြံပေးချက်များကို ပိတ်ပြီး Microsoft Foundry portal ရဲ့ စီမံကိန်းစာမျက်နှာကို ပြန်လည်ဆန်းစစ်ပါ၊ အောက်ပါပုံ၏သဘောတူညီမှုအတိုင်းဖြစ်သင့်သည်။

    ![Microsoft Foundry Project](../../../translated_images/my/azure-ai-foundry.88d0c35298348c2f.webp)

## မော်ဒယ် တပ်ဆင်ခြင်း

၁။ သင်၏စီမံကိန်း အတွက် ဘယ်ဘက် panel တွင် **My assets** အပိုင်းရှိ **Models + endpoints** စာမျက်နှာကို ရွေးချယ်ပါ။
၂။ **Models + endpoints** စာမျက်နှာတွင် **Model deployments** တစ်ချပ်တွင် **+ Deploy model** မီနူးအောက်က **Deploy base model** ကို ရွေးပါ။
၃။ စာရင်းတွင် `gpt-5-mini` မော်ဒယ်ကို ရှာဖွေပြီး ရွေးချယ် အတည်ပြုပါ။

    > **အရေးကြီး**: TPM လျော့ချခြင်းသည် သင့် subscription တွင် ရရှိနိုင်သည့် quota ကို မကျော်လွန်စေရန်ကူညီသည်။

    ![Model Deployed](../../../translated_images/my/model-deployment.3749c53fb81e18fd.webp)

## အေးဂျင့်ဖန်တီးခြင်း

မော်ဒယ်တစ်ခု တပ်ဆင်ပြီးပါပြီ။ သင်အခု အေးဂျင့်တစ်ခုကို ဖန်တီးနိုင်ပြီ ဖြစ်သည်။ အေးဂျင့်ဆိုသည်မှာ အသုံးပြုသူများနှင့် ဆက်သွယ်ပေးနို်င်သည့် စကားပြော AI မော်ဒယ် ဖြစ်သည်။

၁။ သင်၏စီမံကိန်း အတွက် ဘယ်ဘက် panel တွင် **Build & Customize** အပိုင်းအောက်ရှိ **Agents** စာမျက်နှာကို ရွေးပါ။
၂။ **+ Create agent** ကို နှိပ်၍ အေးဂျင့်အသစ်တစ်ခု ဖန်တီးပါ။ **Agent Setup** dialog box အောက်ပါအတိုင်း။
    - အေးဂျင့်အတွက် အမည်တစ်ခု ထည့်ပါ၊ ဥပမာ `FlightAgent` ။
    - ရှေ့က ဖန်တီးထားသော `gpt-5-mini` မော်ဒယ်တပ်ဆင်မှု ရွေးချယ်ထားရမည်။
    - အေးဂျင့်လိုက်နာရမည့် **Instructions** ကို သင်လိုချင်သည့် prompt အတိုင်း သတ်မှတ်ပါ။ ဥပမာက如下။
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
> အသေးစိတ် prompt လုပ်စရာရှိပါက [ဒီ repository](https://github.com/ShivamGoyal03/RoamMind) မှာ ထပ်မံကြည့်ရှုနိုင်ပါသည်။
    
> ထို့အပြင် အေးဂျင့်၏ စွမ်းဆောင်ရည်များကို မြှင့်တင်ရန် **Knowledge Base** နှင့် **Actions** ထည့်သွင်းနိုင်ပြီး အသုံးပြုသူလိုအပ်ချက်များအပေါ် အလိုအလျောက်အလုပ်လုပ်နိုင်ပါသည်။ ဒီလေ့ကျင့်မှုအတွက် အဆိုပါအဆင့်များကို ကျော်လွှားနိုင်သည်။
    
![Agent Setup](../../../translated_images/my/agent-setup.9bbb8755bf5df672.webp)

၃။ multi-AI အေးဂျင့်အသစ်တစ်ခု ဖန်တီးရန် **New Agent** ကို ရိုက်နှိပ်ပါ။ ဖန်တီးပြီးသော အေးဂျင့်အသစ်သည် Agents စာမျက်နှာပေါ်တွင် ပြသမည်။


## အေးဂျင့်ကို စမ်းသပ်ခြင်း

အေးဂျင့်ကို ဖန်တီးပြီးနောက် Microsoft Foundry portal playground တွင် အသုံးပြုသူ မေးခွန်းများကို ဘယ်လိုပြန်လည်တုံ့ပြန်မှုရှိသည်ကို စမ်းသပ်နိုင်သည်။

၁။ သင့်အေးဂျင့်အတွက် **Setup** pane ထိပ်တွင် **Try in playground** ကို စိုက်ရွေးပါ။
၂။ **Playground** pane တွင် စကားပြောပြန်လည်ဆက်သွယ်မှုကို စမ်းသပ်နိုင်သည်။ ဥပမာအားဖြင့်၊ ၂၈ ရက်နေ့ Seattle ကနေ New York သို့ ဘယ်လေးပျံရံ့ချက်တွေရှိလဲဆိုတာ အေးဂျင့်ထံ မေးမြန်းနိုင်သည်။

    > **အရေးကြီး**: ဒီလေ့ကျင့်မှုတွင် အချိန်နှင့်တပြေးညီ ဒေတာ မသုံးတာကြောင့် အေးဂျင့်သည် တိကျသောအဖြေများ မပေးနိုင်ဘဲဖြစ်နိုင်သည်။ ရည်ရွယ်ချက်မှာ အသုံးပြုသူ မေးခွန်းများကို အေးဂျင့်၏ နားလည်မှုနှင့် ပြန်လည်တုံ့ပြန်မှု စွမ်းရည်ကို စမ်းသပ်ခြင်းဖြစ်သည်။

    ![Agent Playground](../../../translated_images/my/agent-playground.dc146586de715010.webp)

၃။ အေးဂျင့်စမ်းသပ်ပြီးနောက်၌ intents, training data နှင့် actions အသစ်များထပ်မံထည့်သွင်းကာ စွမ်းရည်များကို တိုးတက်အောင် ပြင်ဆင်နိုင်သည်။

## အရင်းမြစ်များကို ရှင်းလင်းခြင်း

အေးဂျင့် စမ်းသပ်ပြီးပါက ထပ်မံကုန်ကျစရိတ်မဖြစ်စေရန် ဖျက်ပစ်နိုင်သည်။
၁။ [Azure portal](https://portal.azure.com) ကို ဖွင့်ပြီး ဒီလေ့ကျင့်မှုတွင် အသုံးပြုထားသော hub အရင်းမြစ်များ ရှိ resource group အကြောင်းကြည့်ပါ။
၂။ toolbar တွင် **Delete resource group** ကို ရွေးချယ်ပါ။
၃။ resource group အမည်ကို ထည့်သွင်းပြီး ဖျက်လိုကြောင်း အတည်ပြုပါ။

## အရင်းအမြစ်များ

- [Microsoft Foundry documentation](https://learn.microsoft.com/en-us/azure/ai-studio/?WT.mc_id=academic-105485-koreyst)
- [Microsoft Foundry portal](https://ai.azure.com/?WT.mc_id=academic-105485-koreyst)
- [Getting Started with Microsoft Foundry](https://techcommunity.microsoft.com/blog/educatordeveloperblog/getting-started-with-azure-ai-studio/4095602?WT.mc_id=academic-105485-koreyst)
- [Fundamentals of AI agents on Azure](https://learn.microsoft.com/en-us/training/modules/ai-agent-fundamentals/?WT.mc_id=academic-105485-koreyst)
- [Azure AI Discord](https://aka.ms/AzureAI/Discord)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ပြောကြားချက်**
ဤစာတမ်းကို AI ဘာသာပြန်ဝန်ဆောင်မှု [Co-op Translator](https://github.com/Azure/co-op-translator) အသုံးပြု၍ ဘာသာပြန်ထားပါသည်။ ကျွန်ုပ်တို့သည် တိကျမှန်ကန်မှုအတွက် ကြိုးပမ်းနေသော်လည်း၊ စက်ကိရိယာဘာသာပြန်ခြင်းများတွင် အမှားများ သို့မဟုတ် မှားယွင်းချက်များ ပါဝင်နိုင်ကြောင်း သတိပြုပါရန် လိုအပ်ပါသည်။ မူလစာတမ်းကို မူရင်းဘာသာဖြင့်သာ ယုံကြည်စိတ်ချရသော အချက်အလက်အဖြစ် သတ်မှတ်သင့်သည်။ အရေးကြီးသည့် သတင်းအချက်အလက်များအတွက် ပရော်ဖက်ရှင်နယ် လူသားဘာသာပြန်သူဝန်ဆောင်မှုကို အကြံပြုပါသည်။ ဤဘာသာပြန်ချက်ကို အသုံးပြုခြင်းမှ ဖြစ်ပေါ်လာသော နားလည်မှုကွာခြားမှုများ သို့မဟုတ် မမှန်ကန်သော အသုံးပြုမှုများအတွက် ကျွန်ုပ်တို့ တာဝန်မခံပါ။
<!-- CO-OP TRANSLATOR DISCLAIMER END -->