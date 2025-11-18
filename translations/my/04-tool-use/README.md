<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "d7c3b7bd1b3528074d8b6a7c5ad33b6f",
  "translation_date": "2025-11-18T18:32:11+00:00",
  "source_file": "04-tool-use/README.md",
  "language_code": "my"
}
-->
[![How to Design Good AI Agents](../../../translated_images/lesson-4-thumbnail.546162853cb3daffd64edd92014f274103f76360dfb39fc6e6ee399494da38fd.my.png)](https://youtu.be/vieRiPRx-gI?si=cEZ8ApnT6Sus9rhn)

> _(ဤသင်ခန်းစာ၏ဗီဒီယိုကိုကြည့်ရန် အထက်ပါပုံကိုနှိပ်ပါ)_

# Tool Use Design Pattern

Tools တွေက စိတ်ဝင်စားစရာကောင်းပါတယ်၊ အကြောင်းကတော့ AI အေးဂျင့်တွေကို ပိုမိုကျယ်ပြန့်တဲ့စွမ်းရည်တွေ ပေးနိုင်လို့ပါ။ အေးဂျင့်တစ်ခုဟာ လုပ်ဆောင်နိုင်တဲ့ လုပ်ဆောင်ချက်တွေအနည်းငယ်သာရှိနေတဲ့အစား Tool တစ်ခုထည့်သွင်းလိုက်တာနဲ့ အေးဂျင့်ဟာ လုပ်ဆောင်ချက်အမျိုးမျိုးကို လုပ်ဆောင်နိုင်ပါပြီ။ ဒီအခန်းမှာတော့ AI အေးဂျင့်တွေက သူတို့ရဲ့ရည်မှန်းချက်တွေကို ရောက်ရှိအောင် Tool တွေကို ဘယ်လိုအသုံးပြုနိုင်မလဲဆိုတာ ဖော်ပြထားတဲ့ Tool Use Design Pattern ကို လေ့လာသွားမှာဖြစ်ပါတယ်။

## အကျဉ်းချုပ်

ဒီသင်ခန်းစာမှာ ကျွန်တော်တို့ အောက်ပါမေးခွန်းတွေကို ဖြေရှင်းဖို့ ကြိုးစားသွားမှာဖြစ်ပါတယ်-

- Tool Use Design Pattern ဆိုတာဘာလဲ?
- ဘယ်လိုအခြေအနေတွေမှာ အသုံးပြုနိုင်မလဲ?
- ဒီ Design Pattern ကို အကောင်အထည်ဖော်ဖို့လိုအပ်တဲ့ အစိတ်အပိုင်း/အခြေခံအဆောက်အအုံတွေကဘာလဲ?
- Tool Use Design Pattern ကို အသုံးပြုပြီး ယုံကြည်ရတဲ့ AI အေးဂျင့်တွေကို တည်ဆောက်ဖို့အတွက် အထူးစဉ်းစားရမယ့်အချက်တွေကဘာလဲ?

## သင်ယူရမယ့်ရည်မှန်းချက်များ

ဒီသင်ခန်းစာပြီးဆုံးတဲ့အခါမှာ သင်တစ်ဦးက-

- Tool Use Design Pattern ကို အဓိပ္ပါယ်ဖွင့်ဆိုနိုင်ပြီး ရည်ရွယ်ချက်ကို နားလည်နိုင်မယ်။
- Tool Use Design Pattern ကို အသုံးပြုနိုင်တဲ့ အခြေအနေတွေကို ဖော်ထုတ်နိုင်မယ်။
- ဒီ Design Pattern ကို အကောင်အထည်ဖော်ဖို့လိုအပ်တဲ့ အဓိကအစိတ်အပိုင်းတွေကို နားလည်နိုင်မယ်။
- ဒီ Design Pattern ကို အသုံးပြုတဲ့ AI အေးဂျင့်တွေမှာ ယုံကြည်မှုရှိစေရန် စဉ်းစားရမယ့်အချက်တွေကို သိရှိနိုင်မယ်။

## Tool Use Design Pattern ဆိုတာဘာလဲ?

**Tool Use Design Pattern** ဟာ LLMs တွေကို အပြင်ပ Tools တွေနဲ့ အပြန်အလှန်ဆက်သွယ်နိုင်စွမ်းပေးပြီး ရည်မှန်းချက်တွေကို ရောက်ရှိအောင်လုပ်ဆောင်နိုင်စေတဲ့ အဓိကအချက်ကို အခြေခံထားပါတယ်။ Tools တွေဟာ အေးဂျင့်တစ်ခုက လုပ်ဆောင်ချက်တွေကို အကောင်အထည်ဖော်ဖို့ အသုံးပြုနိုင်တဲ့ ကုဒ်တွေဖြစ်ပါတယ်။ Tool တစ်ခုဟာ ကိန်းဂဏန်းတွက်ချက်တဲ့ Function တစ်ခုလို ရိုးရှင်းတဲ့ Function ဖြစ်နိုင်သလို၊ အခြားသူရဲ့ API ကို ခေါ်ယူပြီး ရှယ်ယာဈေးနှုန်း သို့မဟုတ် မိုးလေဝသခန့်မှန်းချက်ကို ရယူတဲ့ Function တစ်ခုလည်း ဖြစ်နိုင်ပါတယ်။ AI အေးဂျင့်တွေရဲ့အနေနဲ့ Tools တွေကို **model-generated function calls** အဖြစ် အကောင်အထည်ဖော်ဖို့ ဒီဇိုင်းဆွဲထားပါတယ်။

## ဘယ်လိုအခြေအနေတွေမှာ အသုံးပြုနိုင်မလဲ?

AI အေးဂျင့်တွေဟာ Tools တွေကို အသုံးပြုပြီး အလုပ်ရှုပ်တဲ့တာဝန်တွေကို ပြီးမြောက်စေခြင်း၊ အချက်အလက်တွေကို ရယူခြင်း၊ သို့မဟုတ် ဆုံးဖြတ်ချက်ချခြင်းတွေကို လုပ်ဆောင်နိုင်ပါတယ်။ Tool Use Design Pattern ကို အပြင်ပစနစ်တွေ (Databases, Web Services, Code Interpreters) နဲ့ အပြန်အလှန်ဆက်သွယ်ဖို့လိုအပ်တဲ့ အခြေအနေတွေမှာ အသုံးပြုလေ့ရှိပါတယ်။ ဒီစွမ်းရည်ဟာ အောက်ပါအခြေအနေမျိုးစုံမှာ အသုံးဝင်ပါတယ်-

- **Dynamic Information Retrieval:** Agents တွေဟာ အပြင်ပ APIs သို့မဟုတ် Databases တွေကို Query လုပ်ပြီး နောက်ဆုံးရရှိတဲ့ အချက်အလက်တွေကို ရယူနိုင်ပါတယ် (ဥပမာ- SQLite Database ကို Query လုပ်ပြီး ဒေတာခွဲခြမ်းစိတ်ဖြာခြင်း၊ ရှယ်ယာဈေးနှုန်း သို့မဟုတ် မိုးလေဝသအချက်အလက် ရယူခြင်း)။
- **Code Execution and Interpretation:** Agents တွေဟာ ကိန်းဂဏန်းပြဿနာတွေကို ဖြေရှင်းခြင်း၊ အစီရင်ခံစာတွေကို ဖန်တီးခြင်း၊ သို့မဟုတ် Simulation တွေကို လုပ်ဆောင်ဖို့ Code သို့မဟုတ် Scripts တွေကို အကောင်အထည်ဖော်နိုင်ပါတယ်။
- **Workflow Automation:** Task Scheduler, Email Services, Data Pipelines လို Tools တွေကို ပေါင်းစပ်ပြီး အလုပ်တစ်ခုလုံးကို အလိုအလျောက်လုပ်ဆောင်နိုင်ပါတယ်။
- **Customer Support:** CRM Systems, Ticketing Platforms, Knowledge Bases တွေနဲ့ ဆက်သွယ်ပြီး အသုံးပြုသူရဲ့မေးခွန်းတွေကို ဖြေရှင်းနိုင်ပါတယ်။
- **Content Generation and Editing:** Grammar Checkers, Text Summarizers, Content Safety Evaluators လို Tools တွေကို အသုံးပြုပြီး Content ဖန်တီးခြင်းလုပ်ငန်းတွေကို ကူညီနိုင်ပါတယ်။

## Tool Use Design Pattern ကို အကောင်အထည်ဖော်ဖို့လိုအပ်တဲ့ အစိတ်အပိုင်း/အခြေခံအဆောက်အအုံတွေကဘာလဲ?

AI အေးဂျင့်တွေကို အလုပ်အမျိုးမျိုးလုပ်ဆောင်နိုင်စေဖို့ ဒီအစိတ်အပိုင်းတွေက အရေးကြီးပါတယ်။ Tool Use Design Pattern ကို အကောင်အထည်ဖော်ဖို့လိုအပ်တဲ့ အဓိကအစိတ်အပိုင်းတွေကို ကြည့်ကြရအောင်-

- **Function/Tool Schemas**: အသုံးပြုနိုင်တဲ့ Tools တွေရဲ့ Function Name, ရည်ရွယ်ချက်, လိုအပ်တဲ့ Parameters, မျှော်လင့်ရတဲ့ Outputs စတဲ့ အသေးစိတ်ဖော်ပြချက်တွေပါဝင်တဲ့ Schema တွေ။ ဒီ Schema တွေက LLM ကို Tools တွေကို ဘယ်လိုအသုံးပြုရမလဲဆိုတာ နားလည်စေပါတယ်။
- **Function Execution Logic**: အသုံးပြုသူရဲ့ရည်ရွယ်ချက်နဲ့ စကားဝိုင်းအကြောင်းအရာအပေါ်မူတည်ပြီး Tools တွေကို ဘယ်အချိန်မှာ Invoke လုပ်မလဲဆိုတာ စီမံခန့်ခွဲတဲ့ Logic တွေ။
- **Message Handling System**: အသုံးပြုသူရဲ့ Input, LLM ရဲ့ Response, Tool Calls, Tool Outputs တွေကို စီမံခန့်ခွဲတဲ့ Components တွေ။
- **Tool Integration Framework**: ရိုးရှင်းတဲ့ Function တွေဖြစ်စေ၊ အပြင်ပ Services တွေဖြစ်စေ Tools တွေနဲ့ အေးဂျင့်ကို ချိတ်ဆက်ပေးတဲ့ Infrastructure။
- **Error Handling & Validation**: Tool Execution မှာ Failures တွေကို Handle လုပ်ခြင်း၊ Parameters တွေကို Validate လုပ်ခြင်း၊ မမျှော်လင့်ထားတဲ့ Responses တွေကို စီမံခြင်း Mechanisms တွေ။
- **State Management**: စကားဝိုင်းအကြောင်းအရာ၊ အရင် Tool Interaction တွေ၊ Multi-turn Interaction တွေမှာ တိကျမှုရှိစေရန် Persistent Data တွေကို ထိန်းသိမ်းခြင်း။

## Function/Tool Calling

Function Calling ဟာ LLMs တွေကို Tools တွေနဲ့ ဆက်သွယ်စေဖို့ အဓိကနည်းလမ်းဖြစ်ပါတယ်။ 'Function' နဲ့ 'Tool' ဆိုတာ အတူတူအသုံးပြုလေ့ရှိပါတယ်၊ အကြောင်းကတော့ 'Functions' (ပြန်အသုံးပြုနိုင်တဲ့ Code Blocks) တွေဟာ အေးဂျင့်တွေ Task တွေကို လုပ်ဆောင်ဖို့ အသုံးပြုတဲ့ 'Tools' တွေဖြစ်လို့ပါ။ Function Code ကို Invoke လုပ်ဖို့ LLM ဟာ အသုံးပြုသူရဲ့တောင်းဆိုချက်ကို Function Description နဲ့ နှိုင်းယှဉ်ရပါမယ်။ Function Description တွေပါဝင်တဲ့ Schema ကို LLM ကို ပေးပို့ပြီး LLM ဟာ Task အတွက် အကောင်းဆုံး Function ကို ရွေးချယ်ပြီး Function Name နဲ့ Arguments ကို ပြန်ပေးပို့ပါတယ်။ ရွေးချယ်ထားတဲ့ Function ကို Invoke လုပ်ပြီး Response ကို LLM ကို ပြန်ပေးပို့ပြီး အသုံးပြုသူရဲ့တောင်းဆိုချက်ကို ဖြေရှင်းပေးပါတယ်။

## Tool Use Examples with Agentic Frameworks

### Semantic Kernel

<a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Semantic Kernel</a> ဟာ .NET, Python, Java Developer တွေအတွက် LLMs တွေနဲ့ အလုပ်လုပ်ဖို့ အဆင်ပြေစေတဲ့ Open-source AI Framework ဖြစ်ပါတယ်။ Function Calling ကို ပိုမိုလွယ်ကူစေဖို့ Functions တွေကို အလိုအလျောက် Description ပေးပြီး Model ကို ပေးပို့တဲ့ Serialization လုပ်ငန်းစဉ်ကို အသုံးပြုပါတယ်။

### Azure AI Agent Service

<a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Azure AI Agent Service</a> ဟာ Developer တွေကို Compute နဲ့ Storage Resources တွေကို စီမံခန့်ခွဲစရာမလိုဘဲ AI Agents တွေကို တည်ဆောက်၊ Deploy, Scale လုပ်နိုင်စေတဲ့ Framework ဖြစ်ပါတယ်။

## Tool Use Design Pattern ကို ယုံကြည်ရတဲ့ AI အေးဂျင့်တွေကို တည်ဆောက်ဖို့အတွက် အထူးစဉ်းစားရမယ့်အချက်တွေကဘာလဲ?

SQL ကို LLMs တွေက Dynamically Generate လုပ်တဲ့အခါမှာ Security ပိုင်းမှာ စိုးရိမ်ရတဲ့အချက်တွေရှိပါတယ်၊ အထူးသဖြင့် SQL Injection သို့မဟုတ် Database ကို ပျက်စီးစေတဲ့ လှုပ်ရှားမှုတွေပါ။ ဒီစိုးရိမ်ရတဲ့အချက်တွေကို Database Access Permissions တွေကို သေချာစွာ Configure လုပ်ခြင်းအားဖြင့် အကျိုးသက်သာရှိစေပါတယ်။ Database အများစုအတွက် Read-only အဖြစ် Configure လုပ်ရပါမယ်။ PostgreSQL သို့မဟုတ် Azure SQL လို Database Services တွေအတွက် App ကို Read-only (SELECT) Role ပေးရပါမယ်။
အက်ဥ်းချုပ် - အက်ပ်ကို လုံခြုံသောပတ်ဝန်းကျင်တွင် အလုပ်လုပ်ခြင်းသည် ကာကွယ်မှုကို ပိုမိုတိုးတက်စေပါသည်။ စီးပွားရေးလုပ်ငန်းများတွင် ဒေတာများကို လုပ်ငန်းစဉ်များမှ ထုတ်ယူပြီး အသုံးပြုရလွယ်ကူသော schema ပါရှိသော ဖတ်ရှုနိုင်သော database သို့မဟုတ် data warehouse သို့ ပြောင်းလဲထားသည်။ ဒီနည်းလမ်းက ဒေတာကို လုံခြုံစေပြီး၊ စွမ်းဆောင်ရည်နှင့် အသုံးပြုနိုင်မှုအတွက် အကောင်းဆုံးဖြစ်စေပြီး၊ အက်ပ်ကို ဖတ်ရှုနိုင်သော အခွင့်အာဏာသာပေးထားသည်။

## နမူနာ ကုဒ်များ

- Python: [Agent Framework](./code_samples/04-python-agent-framework.ipynb)
- .NET: [Agent Framework](./code_samples/04-dotnet-agent-framework.md)

## Tool Use Design Patterns အကြောင်း ပိုမိုမေးမြန်းလိုပါသလား?

အခြားလေ့လာသူများနှင့် တွေ့ဆုံရန်၊ office hours တွင် ပါဝင်ရန်နှင့် AI Agents အကြောင်း မေးမြန်းရန် [Azure AI Foundry Discord](https://aka.ms/ai-agents/discord) ကို ဝင်ရောက်ပါ။

## ထပ်ဆောင်း အရင်းအမြစ်များ

- <a href="https://microsoft.github.io/build-your-first-agent-with-azure-ai-agent-service-workshop/" target="_blank">Azure AI Agents Service Workshop</a>
- <a href="https://github.com/Azure-Samples/contoso-creative-writer/tree/main/docs/workshop" target="_blank">Contoso Creative Writer Multi-Agent Workshop</a>
- <a href="https://learn.microsoft.com/semantic-kernel/concepts/ai-services/chat-completion/function-calling/?pivots=programming-language-python#1-serializing-the-functions" target="_blank">Semantic Kernel Function Calling Tutorial</a>
- <a href="https://github.com/microsoft/semantic-kernel/blob/main/python/samples/getting_started_with_agents/openai_assistant/step3_assistant_tool_code_interpreter.py" target="_blank">Semantic Kernel Code Interpreter</a>
- <a href="https://microsoft.github.io/autogen/dev/user-guide/core-user-guide/components/tools.html" target="_blank">Autogen Tools</a>

## ယခင် သင်ခန်းစာ

[Understanding Agentic Design Patterns](../03-agentic-design-patterns/README.md)

## နောက်သင်ခန်းစာ

[Agentic RAG](../05-agentic-rag/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ဝန်ခံချက်**:  
ဤစာရွက်စာတမ်းကို AI ဘာသာပြန်ဝန်ဆောင်မှု [Co-op Translator](https://github.com/Azure/co-op-translator) ကို အသုံးပြု၍ ဘာသာပြန်ထားပါသည်။ ကျွန်ုပ်တို့သည် တိကျမှန်ကန်မှုအတွက် ကြိုးစားနေသော်လည်း၊ အလိုအလျောက်ဘာသာပြန်ခြင်းတွင် အမှားများ သို့မဟုတ် မမှန်ကန်မှုများ ပါဝင်နိုင်သည်ကို သတိပြုပါ။ မူလဘာသာစကားဖြင့် ရေးသားထားသော စာရွက်စာတမ်းကို အာဏာတည်သောရင်းမြစ်အဖြစ် သတ်မှတ်သင့်ပါသည်။ အရေးကြီးသော အချက်အလက်များအတွက် လူ့ဘာသာပြန်ပညာရှင်များကို အသုံးပြုရန် အကြံပြုပါသည်။ ဤဘာသာပြန်ကို အသုံးပြုခြင်းမှ ဖြစ်ပေါ်လာသော နားလည်မှုမှားများ သို့မဟုတ် အဓိပ္ပာယ်မှားများအတွက် ကျွန်ုပ်တို့သည် တာဝန်မယူပါ။
<!-- CO-OP TRANSLATOR DISCLAIMER END -->