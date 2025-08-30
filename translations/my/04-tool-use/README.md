<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "4a5ccc4ad1dba85fbc2087cf3b986544",
  "translation_date": "2025-08-30T09:36:45+00:00",
  "source_file": "04-tool-use/README.md",
  "language_code": "my"
}
-->
[![How to Design Good AI Agents](../../../translated_images/lesson-4-thumbnail.546162853cb3daffd64edd92014f274103f76360dfb39fc6e6ee399494da38fd.my.png)](https://youtu.be/vieRiPRx-gI?si=cEZ8ApnT6Sus9rhn)

> _(ဤပုံကိုနှိပ်ပြီးဤသင်ခန်းစာ၏ဗီဒီယိုကိုကြည့်ပါ)_

# Tool Use Design Pattern

Tools တွေက AI အေးဂျင့်တွေကို ပိုမိုကျယ်ပြန့်တဲ့စွမ်းရည်တွေကိုပေးနိုင်တဲ့အတွက် စိတ်ဝင်စားဖွယ်ကောင်းပါတယ်။ အေးဂျင့်တစ်ခုမှာ လုပ်ဆောင်နိုင်တဲ့ လှုပ်ရှားမှုအကန့်အသတ်ရှိတဲ့အစား tool တစ်ခုကို ထည့်သွင်းခြင်းအားဖြင့် အေးဂျင့်ဟာ လုပ်ဆောင်နိုင်တဲ့ လှုပ်ရှားမှုအမျိုးမျိုးကို လုပ်ဆောင်နိုင်ပါပြီ။ ဤအခန်းတွင် AI အေးဂျင့်များသည် သတ်မှတ်ထားသော ရည်မှန်းချက်များကို ရောက်ရှိရန် အထူး tools များကို အသုံးပြုနိုင်ပုံကို ဖော်ပြထားသော Tool Use Design Pattern ကို လေ့လာပါမည်။

## အကျဉ်းချုပ်

ဤသင်ခန်းစာတွင် ကျွန်ုပ်တို့သည် အောက်ပါမေးခွန်းများကို ဖြေရှင်းရန် ကြိုးစားနေပါသည်-

- Tool Use Design Pattern ဆိုတာဘာလဲ?
- ၎င်းကို အသုံးချနိုင်သော use cases များကဘာလဲ?
- Design Pattern ကို အကောင်အထည်ဖော်ရန် လိုအပ်သော အစိတ်အပိုင်းများ/အခြေခံအဆောက်အအုံများကဘာလဲ?
- ယုံကြည်စိတ်ချရသော AI အေးဂျင့်များကို တည်ဆောက်ရန် Tool Use Design Pattern ကို အသုံးပြုခြင်းအတွက် အထူးစဉ်းစားစရာများကဘာလဲ?

## သင်ယူရမည့်ရည်မှန်းချက်များ

ဤသင်ခန်းစာကိုပြီးမြောက်ပြီးနောက်တွင် သင်သည်-

- Tool Use Design Pattern နှင့် ၎င်း၏ ရည်ရွယ်ချက်ကို သတ်မှတ်နိုင်မည်။
- Tool Use Design Pattern ကို အသုံးချနိုင်သော use cases များကို ဖော်ထုတ်နိုင်မည်။
- Design Pattern ကို အကောင်အထည်ဖော်ရန် လိုအပ်သော အဓိကအစိတ်အပိုင်းများကို နားလည်နိုင်မည်။
- Tool Use Design Pattern ကို အသုံးပြုသော AI အေးဂျင့်များ၏ ယုံကြည်စိတ်ချရမှုကို သေချာစေရန် စဉ်းစားစရာများကို သိရှိနိုင်မည်။

## Tool Use Design Pattern ဆိုတာဘာလဲ?

**Tool Use Design Pattern** သည် LLMs များကို သတ်မှတ်ထားသော ရည်မှန်းချက်များကို ရောက်ရှိရန် အပြင်ပ tools များနှင့် အပြန်အလှန်ဆက်သွယ်နိုင်စွမ်းပေးခြင်းကို အဓိကထားသည်။ Tools များသည် အေးဂျင့်များက လှုပ်ရှားမှုများကို လုပ်ဆောင်ရန် အကောင်အထည်ဖော်နိုင်သော code ဖြစ်သည်။ Tool တစ်ခုသည် calculator ကဲ့သို့ ရိုးရှင်းသော function ဖြစ်နိုင်သလို၊ stock price lookup သို့မဟုတ် မိုးလေဝသခန့်မှန်းခြေကဲ့သို့သော third-party service ကို API call လုပ်ခြင်းဖြစ်နိုင်သည်။ AI အေးဂျင့်များ၏ အနက်တွင် tools များကို **model-generated function calls** အဖြစ် အေးဂျင့်များက လုပ်ဆောင်ရန် ရည်ရွယ်ထားသည်။

## ၎င်းကို အသုံးချနိုင်သော use cases များကဘာလဲ?

AI အေးဂျင့်များသည် tools များကို အသုံးပြု၍ ရှုပ်ထွေးသောအလုပ်များကို ပြီးမြောက်စေခြင်း၊ အချက်အလက်များကို ရယူခြင်း၊ သို့မဟုတ် ဆုံးဖြတ်ချက်များကို ချမှတ်ခြင်းတို့ကို လုပ်ဆောင်နိုင်သည်။ Tool Use Design Pattern ကို databases, web services, သို့မဟုတ် code interpreters ကဲ့သို့သော အပြင်ပစနစ်များနှင့် dynamic interaction လိုအပ်သော အခြေအနေများတွင် မကြာခဏအသုံးပြုသည်။ ၎င်းစွမ်းရည်သည် အောက်ပါ use cases များအတွက် အသုံးဝင်သည်-

- **Dynamic Information Retrieval:** Agents များသည် SQLite database ကို query လုပ်ခြင်း၊ stock prices သို့မဟုတ် မိုးလေဝသအချက်အလက်များကို ရယူခြင်းကဲ့သို့သော အချက်အလက်များကို ရယူရန် အပြင်ပ APIs သို့မဟုတ် databases များကို query လုပ်နိုင်သည်။
- **Code Execution and Interpretation:** Agents များသည် mathematical problems ကို ဖြေရှင်းရန်၊ report များကို ဖန်တီးရန် သို့မဟုတ် simulation များကို လုပ်ဆောင်ရန် code သို့မဟုတ် scripts များကို run လုပ်နိုင်သည်။
- **Workflow Automation:** Task schedulers, email services, သို့မဟုတ် data pipelines ကဲ့သို့သော tools များကို ပေါင်းစပ်ခြင်းအားဖြင့် ထပ်တလဲလဲ သို့မဟုတ် အဆင့်များစွာပါဝင်သော workflows များကို automate လုပ်ခြင်း။
- **Customer Support:** Agents များသည် CRM systems, ticketing platforms, သို့မဟုတ် knowledge bases များနှင့် ဆက်သွယ်ပြီး အသုံးပြုသူမေးခွန်းများကို ဖြေရှင်းနိုင်သည်။
- **Content Generation and Editing:** Grammar checkers, text summarizers, သို့မဟုတ် content safety evaluators ကဲ့သို့သော tools များကို အသုံးပြု၍ content ဖန်တီးမှုအလုပ်များကို ကူညီနိုင်သည်။

## Design Pattern ကို အကောင်အထည်ဖော်ရန် လိုအပ်သော အဓိကအစိတ်အပိုင်းများကဘာလဲ?

AI အေးဂျင့်များကို အလုပ်အမျိုးမျိုးကို လုပ်ဆောင်နိုင်စွမ်းပေးသော အစိတ်အပိုင်းများဖြစ်သည်။ Tool Use Design Pattern ကို အကောင်အထည်ဖော်ရန် လိုအပ်သော အဓိကအစိတ်အပိုင်းများကို ကြည့်ကြပါစို့-

- **Function/Tool Schemas**: အသုံးပြုနိုင်သော tools များ၏ အသေးစိတ်ဖော်ပြချက်များ၊ function name, ရည်ရွယ်ချက်, လိုအပ်သော parameters, နှင့် မျှော်မှန်းထားသော outputs အပါအဝင်။ ၎င်းသည် LLM ကို tools များရရှိနိုင်ပုံနှင့် တရားဝင်တောင်းဆိုမှုများကို ဖွဲ့စည်းပုံနားလည်စေသည်။
- **Function Execution Logic**: အသုံးပြုသူ၏ ရည်ရွယ်ချက်နှင့် စကားဝိုင်းအကြောင်းအရာအပေါ်မူတည်၍ tools များကို invoke လုပ်ပုံကို စီမံခန့်ခွဲသည်။ ၎င်းတွင် planner modules, routing mechanisms, သို့မဟုတ် tool usage ကို dynamic သတ်မှတ်ပေးသော conditional flows များပါဝင်နိုင်သည်။
- **Message Handling System**: အသုံးပြုသူ input, LLM response, tool calls, နှင့် tool outputs အကြား စကားဝိုင်းလှုပ်ရှားမှုကို စီမံခန့်ခွဲသော components များ။
- **Tool Integration Framework**: ရိုးရှင်းသော functions များဖြစ်စေ၊ ရှုပ်ထွေးသော အပြင်ပ services များဖြစ်စေ အေးဂျင့်ကို tools များနှင့် ချိတ်ဆက်ပေးသော infrastructure။
- **Error Handling & Validation**: Tool execution တွင်ဖြစ်ပေါ်သော fail များကို handle လုပ်ခြင်း၊ parameters များကို validate လုပ်ခြင်း၊ နှင့် မမျှော်လင့်ထားသော response များကို စီမံခန့်ခွဲခြင်း။
- **State Management**: စကားဝိုင်းအကြောင်းအရာ, ယခင် tool interactions, နှင့် multi-turn interactions များအတွက် တည်ငြိမ်သော data များကို track လုပ်ခြင်း။

## Function/Tool Calling

Function calling သည် Large Language Models (LLMs) များကို tools များနှင့် ဆက်သွယ်စေသော အဓိကနည်းလမ်းဖြစ်သည်။ 'Function' နှင့် 'Tool' ကို အပြန်အလှန်အသုံးပြုသောကြောင့် 'functions' (ပြန်လည်အသုံးပြုနိုင်သော code blocks) သည် အေးဂျင့်များအတွက် tasks များကို လုပ်ဆောင်ရန် အသုံးပြုသော 'tools' ဖြစ်သည်။ Function code ကို invoke လုပ်ရန်အတွက် LLM သည် အသုံးပြုသူ၏တောင်းဆိုမှုကို function description နှင့် နှိုင်းယှဉ်ရမည်။ Function description များပါဝင်သော schema ကို LLM သို့ ပေးပို့ပြီး LLM သည် task အတွက် အကောင်းဆုံး function ကို ရွေးချယ်ပြီး ၎င်း၏ name နှင့် arguments ကို ပြန်ပေးသည်။ ရွေးချယ်ထားသော function ကို invoke လုပ်ပြီး response ကို LLM သို့ ပြန်ပေးပြီး အသုံးပြုသူ၏တောင်းဆိုမှုကို ဖြေကြားရန် အသုံးပြုသည်။

Function calling ကို အေးဂျင့်များအတွက် အကောင်အထည်ဖော်ရန် developer များအတွက် လိုအပ်သောအရာများမှာ-

1. Function calling ကို support လုပ်သော LLM model
2. Function descriptions ပါဝင်သော schema
3. ဖော်ပြထားသော function တစ်ခုစီ၏ code

## Tool Use Examples with Agentic Frameworks

### Semantic Kernel

<a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Semantic Kernel</a> သည် Large Language Models (LLMs) နှင့်အလုပ်လုပ်သော .NET, Python, နှင့် Java developer များအတွက် open-source AI framework ဖြစ်သည်။ Function calling ကို အသုံးပြုခြင်းကို လွယ်ကူစေပြီး model သို့ function များနှင့် ၎င်း၏ parameters များကို automatic ဖော်ပြပေးသည်။

### Azure AI Agent Service

<a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Azure AI Agent Service</a> သည် developer များကို အရည်အသွေးမြင့် AI အေးဂျင့်များကို တည်ဆောက်ရန် အထောက်အကူပြုသော agentic framework ဖြစ်သည်။ ၎င်းသည် enterprise applications အတွက် အထူးအသုံးဝင်သည်။

## Tool Use Design Pattern ကို အသုံးပြုသော AI အေးဂျင့်များ၏ ယုံကြည်စိတ်ချရမှုကို သေချာစေရန် အထူးစဉ်းစားစရာများကဘာလဲ?

SQL ကို LLMs မှ dynamic ဖန်တီးခြင်းနှင့်ပတ်သက်သော စိုးရိမ်မှုများမှာ SQL injection သို့မဟုတ် malicious actions ကဲ့သို့သော security risk ဖြစ်သည်။ ၎င်းကို database access permissions များကို သင့်တော်စွာ configure လုပ်ခြင်းအားဖြင့် effectively ကာကွယ်နိုင်သည်။ Database များအတွက် read-only အဖြစ် configure လုပ်ခြင်းသည် အရေးကြီးသည်။

### Tool Use Design Pattern နှင့်ပတ်သက်သော မေးခွန်းများရှိပါသလား?
Azure AI Foundry Discord ကို [ဒီမှာ](https://aka.ms/ai-agents/discord) ဝင်ရောက်ပြီး အခြားသော သင်ယူသူများနှင့် တွေ့ဆုံပါ၊ အချိန်ချိန်းမေးမြန်းပွဲများတက်ရောက်ပါ၊ AI Agents အကြောင်းမေးမြန်းမှုများကို ဖြေရှင်းပါ။

## အပိုဆောင်း အရင်းအမြစ်များ

## ယခင် သင်ခန်းစာ

[Agentic Design Patterns ကို နားလည်ခြင်း](../03-agentic-design-patterns/README.md)

## နောက် သင်ခန်းစာ

[Agentic RAG](../05-agentic-rag/README.md)

---

**အကြောင်းကြားချက်**:  
ဤစာရွက်စာတမ်းကို AI ဘာသာပြန်ဝန်ဆောင်မှု [Co-op Translator](https://github.com/Azure/co-op-translator) ကို အသုံးပြု၍ ဘာသာပြန်ထားပါသည်။ ကျွန်ုပ်တို့သည် တိကျမှုအတွက် ကြိုးစားနေသော်လည်း၊ အလိုအလျောက် ဘာသာပြန်ခြင်းတွင် အမှားများ သို့မဟုတ် မတိကျမှုများ ပါရှိနိုင်သည်ကို သတိပြုပါ။ မူရင်းဘာသာစကားဖြင့် ရေးသားထားသော စာရွက်စာတမ်းကို အာဏာရှိသော ရင်းမြစ်အဖြစ် သတ်မှတ်သင့်ပါသည်။ အရေးကြီးသော အချက်အလက်များအတွက် လူ့ဘာသာပြန်ပညာရှင်များမှ ပရော်ဖက်ရှင်နယ် ဘာသာပြန်ခြင်းကို အကြံပြုပါသည်။ ဤဘာသာပြန်ကို အသုံးပြုခြင်းမှ ဖြစ်ပေါ်လာသော အလွဲအလွတ်များ သို့မဟုတ် အနားယူမှားမှုများအတွက် ကျွန်ုပ်တို့သည် တာဝန်မယူပါ။