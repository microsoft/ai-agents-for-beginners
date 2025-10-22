<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "9bf0395cbc541ce8db2a9699c8678dfc",
  "translation_date": "2025-08-30T00:19:36+00:00",
  "source_file": "11-agentic-protocols/code_samples/github-mcp/README.md",
  "language_code": "my"
}
-->
# Github MCP Server ဥပမာ

## ဖော်ပြချက်

ဒီဟာက Microsoft Reactor မှာ ကျင်းပတဲ့ AI Agents Hackathon အတွက် ဖန်တီးထားတဲ့ နမူနာတစ်ခုဖြစ်ပါတယ်။

ဒီ tool ကို အသုံးပြုပြီး အသုံးပြုသူရဲ့ Github repos အပေါ် အခြေခံပြီး hackathon project တွေကို အကြံပြုပေးနိုင်ပါတယ်။ ဒီလုပ်ငန်းစဉ်ကို အောက်ပါအတိုင်း ဆောင်ရွက်ပါတယ် -

1. **Github Agent** - Github MCP Server ကို အသုံးပြုပြီး repos နဲ့ အဲဒီ repos တွေကို ပတ်သက်တဲ့ အချက်အလက်တွေကို ရယူပါ။
2. **Hackathon Agent** - Github Agent က ရရှိတဲ့ အချက်အလက်တွေကို အသုံးပြုပြီး အသုံးပြုသူရဲ့ project တွေ၊ အသုံးပြုထားတဲ့ programming languages နဲ့ AI Agents Hackathon ရဲ့ project tracks တွေအပေါ် အခြေခံပြီး ဖန်တီးမှုရှိတဲ့ hackathon project အကြံပြုချက်တွေကို ထုတ်ပေးပါ။
3. **Events Agent** - Hackathon Agent ရဲ့ အကြံပြုချက်အပေါ် အခြေခံပြီး AI Agent Hackathon စီးရီးထဲက သက်ဆိုင်ရာ အခမ်းအနားတွေကို အကြံပြုပေးပါ။

## ကုဒ်ကို အလုပ်လုပ်စေခြင်း

### ပတ်ဝန်းကျင် အပြောင်းအလဲများ

ဒီနမူနာမှာ Azure Open AI Service, Semantic Kernel, Github MCP Server နဲ့ Azure AI Search ကို အသုံးပြုထားပါတယ်။

ဒီ tool တွေကို အသုံးပြုနိုင်ဖို့ အောက်ပါ ပတ်ဝန်းကျင် အပြောင်းအလဲတွေကို သေချာစွာ သတ်မှတ်ထားပါ -

```python
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME=""
AZURE_OPENAI_EMBEDDING_DEPLOYMENT_NAME=""
AZURE_OPENAI_ENDPOINT=""
AZURE_OPENAI_API_KEY=""
AZURE_OPENAI_API_VERSION=""
AZURE_SEARCH_SERVICE_ENDPOINT=""
AZURE_SEARCH_API_KEY=""
``` 

## Chainlit Server ကို အလုပ်လုပ်စေခြင်း

MCP server နဲ့ ချိတ်ဆက်ဖို့ ဒီနမူနာမှာ Chainlit ကို chat interface အနေနဲ့ အသုံးပြုထားပါတယ်။

Server ကို အလုပ်လုပ်စေဖို့ အောက်ပါ command ကို သင့် terminal မှာ အသုံးပြုပါ -

```bash
chainlit run app.py -w
```

ဒီဟာက သင့် Chainlit server ကို `localhost:8000` မှာ စတင်ပြီး Azure AI Search Index ကို `event-descriptions.md` content နဲ့ ဖြည့်စွက်ပေးပါလိမ့်မယ်။

## MCP Server နဲ့ ချိတ်ဆက်ခြင်း

Github MCP Server နဲ့ ချိတ်ဆက်ဖို့ "Type your message here.." chat box အောက်မှာရှိတဲ့ "plug" icon ကို ရွေးချယ်ပါ -

![MCP Connect](../../../../../translated_images/mcp-chainlit-1.7ed66d648e3cfb28f1ea5f320b91e4404df4a24a0f236ce3de999666621f1cfc.my.png)

အဲဒီနေရာကနေ "Connect an MCP" ကို နှိပ်ပြီး Github MCP Server နဲ့ ချိတ်ဆက်ဖို့ command ကို ထည့်သွင်းနိုင်ပါတယ် -

```bash
npx -y @modelcontextprotocol/server-github --env GITHUB_PERSONAL_ACCESS_TOKEN=[YOUR PERSONAL ACCESS TOKEN]
```

"[YOUR PERSONAL ACCESS TOKEN]" ကို သင့်ရဲ့ Personal Access Token နဲ့ အစားထိုးပါ။

ချိတ်ဆက်ပြီးရင် plug icon ရဲ့ ဘေးမှာ (1) ဆိုတဲ့ အမှတ်ကို မြင်ရပါလိမ့်မယ်။ မမြင်ရဘူးဆိုရင် `chainlit run app.py -w` နဲ့ chainlit server ကို ပြန်စတင်ကြည့်ပါ။

## နမူနာကို အသုံးပြုခြင်း

Hackathon project recommendation အတွက် agent workflow ကို စတင်ဖို့ အောက်ပါလိုမျိုး စာသားတစ်ခု ရိုက်ထည့်နိုင်ပါတယ် -

"Recommend hackathon projects for the Github user koreyspace"

Router Agent က သင့်ရဲ့ တောင်းဆိုချက်ကို ခွဲခြမ်းစိတ်ဖြာပြီး အကောင်းဆုံးဖြေရှင်းနိုင်မယ့် agents (GitHub, Hackathon, နဲ့ Events) တွေကို ရွေးချယ်ပေးပါလိမ့်မယ်။ အဲဒီ agents တွေက Github repository ကို ခွဲခြမ်းစိတ်ဖြာခြင်း၊ project idea ဖန်တီးခြင်း၊ နဲ့ သက်ဆိုင်ရာ နည်းပညာ အခမ်းအနားတွေကို အကြံပြုခြင်းတို့အတွက် ပေါင်းစပ်လုပ်ဆောင်ပေးပါလိမ့်မယ်။

---

**အကြောင်းကြားချက်**:  
ဤစာရွက်စာတမ်းကို AI ဘာသာပြန်ဝန်ဆောင်မှု [Co-op Translator](https://github.com/Azure/co-op-translator) ကို အသုံးပြု၍ ဘာသာပြန်ထားပါသည်။ ကျွန်ုပ်တို့သည် တိကျမှုအတွက် ကြိုးစားနေသော်လည်း၊ အလိုအလျောက် ဘာသာပြန်မှုများတွင် အမှားများ သို့မဟုတ် မတိကျမှုများ ပါရှိနိုင်သည်ကို သတိပြုပါ။ မူရင်းဘာသာစကားဖြင့် ရေးသားထားသော စာရွက်စာတမ်းကို အာဏာတရ အရင်းအမြစ်အဖြစ် သတ်မှတ်သင့်ပါသည်။ အရေးကြီးသော အချက်အလက်များအတွက် လူက ဘာသာပြန်မှု ဝန်ဆောင်မှုကို အသုံးပြုရန် အကြံပြုပါသည်။ ဤဘာသာပြန်မှုကို အသုံးပြုခြင်းမှ ဖြစ်ပေါ်လာသော အလွဲအလွန်များ သို့မဟုတ် အနားယူမှားမှုများအတွက် ကျွန်ုပ်တို့သည် တာဝန်မယူပါ။