<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "9bf0395cbc541ce8db2a9699c8678dfc",
  "translation_date": "2025-08-30T10:30:08+00:00",
  "source_file": "11-agentic-protocols/code_samples/github-mcp/README.md",
  "language_code": "my"
}
-->
# Github MCP Server Example

## ဖော်ပြချက်

ဒီဟာ Microsoft Reactor မှာကျင်းပတဲ့ AI Agents Hackathon အတွက် ဖန်တီးထားတဲ့ နမူနာတစ်ခုဖြစ်ပါတယ်။

ဒီ tools ကို အသုံးပြုသူရဲ့ Github repos အပေါ်အခြေခံပြီး Hackathon project recommendation ပေးဖို့ အသုံးပြုပါတယ်။ ဒီဟာကို အောက်ပါအတိုင်းလုပ်ဆောင်ပါတယ်-

1. **Github Agent** - Github MCP Server ကို အသုံးပြုပြီး repos နဲ့ repos အကြောင်းအရာတွေကို ရယူပါတယ်။
2. **Hackathon Agent** - Github Agent ရဲ့ data ကို အသုံးပြုပြီး အသုံးပြုသူရဲ့ project တွေ၊ အသုံးပြုထားတဲ့ programming languages နဲ့ AI Agents Hackathon ရဲ့ project tracks အပေါ်အခြေခံပြီး ဖန်တီးမှုရှိတဲ့ Hackathon project idea တွေကို ဖန်တီးပေးပါတယ်။
3. **Events Agent** - Hackathon Agent ရဲ့ အကြံပေးချက်အပေါ်အခြေခံပြီး AI Agent Hackathon series မှာ သက်ဆိုင်တဲ့ event recommendation တွေကို ပေးပါတယ်။

## Code ကို run လုပ်ခြင်း

### Environment Variables

ဒီ demo မှာ Azure Open AI Service, Semantic Kernel, Github MCP Server နဲ့ Azure AI Search ကို အသုံးပြုပါတယ်။

ဒီ tools တွေကို အသုံးပြုနိုင်ဖို့ အောက်ပါ environment variables တွေကို သေချာစွာ set လုပ်ထားပါ:

```python
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME=""
AZURE_OPENAI_EMBEDDING_DEPLOYMENT_NAME=""
AZURE_OPENAI_ENDPOINT=""
AZURE_OPENAI_API_KEY=""
AZURE_OPENAI_API_VERSION=""
AZURE_SEARCH_SERVICE_ENDPOINT=""
AZURE_SEARCH_API_KEY=""
``` 

## Chainlit Server ကို run လုပ်ခြင်း

MCP server ကို ချိတ်ဆက်ဖို့ ဒီ demo မှာ Chainlit ကို chat interface အနေနဲ့ အသုံးပြုပါတယ်။

Server ကို run လုပ်ဖို့ terminal မှာ အောက်ပါ command ကို အသုံးပြုပါ:

```bash
chainlit run app.py -w
```

ဒီဟာက `localhost:8000` မှာ Chainlit server ကို စတင်ပြီး `event-descriptions.md` content ကို Azure AI Search Index မှာ ထည့်သွင်းပေးပါလိမ့်မယ်။

## MCP Server ကို ချိတ်ဆက်ခြင်း

Github MCP Server ကို ချိတ်ဆက်ဖို့ "Type your message here.." chat box အောက်မှာရှိတဲ့ "plug" icon ကို ရွေးချယ်ပါ:

![MCP Connect](../../../../../translated_images/mcp-chainlit-1.7ed66d648e3cfb28f1ea5f320b91e4404df4a24a0f236ce3de999666621f1cfc.my.png)

ဒီနေရာကနေ Github MCP Server ကို ချိတ်ဆက်ဖို့ command ကို ထည့်သွင်းနိုင်တဲ့ "Connect an MCP" ကို click လုပ်ပါ:

```bash
npx -y @modelcontextprotocol/server-github --env GITHUB_PERSONAL_ACCESS_TOKEN=[YOUR PERSONAL ACCESS TOKEN]
```

"[YOUR PERSONAL ACCESS TOKEN]" ကို သင့်ရဲ့ Personal Access Token နဲ့ အစားထိုးပါ။

ချိတ်ဆက်ပြီးရင် plug icon ရဲ့ အနားမှာ (1) ဆိုတဲ့ အမှတ်ကို တွေ့ရပါလိမ့်မယ်။ မတွေ့ရင် `chainlit run app.py -w` နဲ့ chainlit server ကို ပြန်စတင်ကြည့်ပါ။

## Demo ကို အသုံးပြုခြင်း

Hackathon project recommendation workflow ကို စတင်ဖို့ "Recommend hackathon projects for the Github user koreyspace" လို့ message ရိုက်ထည့်နိုင်ပါတယ်။

Router Agent က သင့်ရဲ့ request ကို ချက်ချင်းခွဲခြားပြီး အကောင်းဆုံးဖြေရှင်းနိုင်တဲ့ agents (GitHub, Hackathon, နဲ့ Events) တွေကို ရွေးချယ်ပေးပါလိမ့်မယ်။ ဒီ agents တွေက Github repository analysis, project idea ဖန်တီးခြင်းနဲ့ သက်ဆိုင်တဲ့ tech events recommendation တွေကို ပေါင်းစပ်ပြီး comprehensive recommendation တွေကို ပေးပါလိမ့်မယ်။

---

**အကြောင်းကြားချက်**:  
ဤစာရွက်စာတမ်းကို AI ဘာသာပြန်ဝန်ဆောင်မှု [Co-op Translator](https://github.com/Azure/co-op-translator) ကို အသုံးပြု၍ ဘာသာပြန်ထားပါသည်။ ကျွန်ုပ်တို့သည် တိကျမှုအတွက် ကြိုးစားနေသော်လည်း၊ အလိုအလျောက် ဘာသာပြန်မှုများတွင် အမှားများ သို့မဟုတ် မတိကျမှုများ ပါဝင်နိုင်သည်ကို သတိပြုပါ။ မူရင်းစာရွက်စာတမ်းကို ၎င်း၏ မူရင်းဘာသာစကားဖြင့် အာဏာတရားရှိသော အရင်းအမြစ်အဖြစ် သတ်မှတ်သင့်ပါသည်။ အရေးကြီးသော အချက်အလက်များအတွက် လူက ဘာသာပြန်မှု ဝန်ဆောင်မှုကို အသုံးပြုရန် အကြံပြုပါသည်။ ဤဘာသာပြန်မှုကို အသုံးပြုခြင်းမှ ဖြစ်ပေါ်လာသော အလွဲအလွန်များ သို့မဟုတ် အနားလွဲမှုများအတွက် ကျွန်ုပ်တို့သည် တာဝန်မယူပါ။