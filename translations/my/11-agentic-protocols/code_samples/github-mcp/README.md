# Github MCP Server Example

## ဖော်ပြချက်

ဤသည်ကို Microsoft Reactor မှ ကျင်းပသော AI Agents Hackathon အတွက် ဖန်တီးထားသည့် ဒေမို (demo) တစ်ခု ဖြစ်သည်။

ဤကိရိယာကို အသုံးပြု၍ အသုံးပြုသူ၏ Github repos များအပေါ် အခြေခံပြီး hackathon ပရောဂျက်များကို အကြံပြုနိုင်သည်။
၎င်းကို အောက်ပါအတိုင်း ဆောင်ရွက်သည်။

1. **Github Agent** - Github MCP Server ကို အသုံးပြုပြီး repo များနှင့် ၎င်း repo များဆိုင်ရာ သတင်းအချက်အလက်များကို ရယူသည်။
2. **Hackathon Agent** - Github Agent မှ ယူထားသည့် ဒေတာများကို အသုံးပြုပြီး အသုံးပြုသူ၏ project များ၊ သုံးထားသော ဘာသာစကားများနှင့် AI Agents hackathon အတွက် project tracks များအပေါ် အခြေခံ၍ ဖန်တီးသော hackathon project အတွေးများကို ထုတ်ပေးသည်။
3. **Events Agent** - Hackathon Agent ၏ အကြံပြုချက်အပေါ် အခြေခံ၍ Events Agent သည် AI Agent Hackathon စီးရီးမှ သက်ဆိုင်ရာ event များကို အကြံပြုပေးမည်။

## ကုဒ်ကို လည်ပတ်ခြင်း

### Environment Variables

ဤဒေမိုတွင် Microsoft Agent Framework, Azure OpenAI Service, Github MCP Server နှင့် Azure AI Search ကို အသုံးပြုထားပါသည်။

ဤကိရိယာများကို အသုံးပြုရန် လိုအပ်သော environment variables များကို သတ်မှတ်ထားကြောင်း သေချာပါ။

```python
AZURE_AI_PROJECT_ENDPOINT=""
AZURE_AI_MODEL_DEPLOYMENT_NAME=""
AZURE_SEARCH_SERVICE_ENDPOINT=""
AZURE_SEARCH_API_KEY=""
``` 

## Chainlit Server လည်ပတ်ခြင်း

MCP server နှင့် ဆက်သွယ်ရန် ဤဒေမိုတွင် chat အင်တာဖေ့စ်အဖြစ် Chainlit ကို အသုံးပြုထားသည်။

Server ကို ပြေးစေရန် သင်၏ terminal တွင် အောက်ပါ command ကို အသုံးပြုပါ။

```bash
chainlit run app.py -w
```

ဤသည်က သင့် Chainlit server ကို `localhost:8000` တွင် စတင်လည်ပတ်စေပြီး သင့် Azure AI Search Index ကို `event-descriptions.md` အကြောင်းအရာဖြင့် ဖြည့်စွက်ပေးမည်။

## MCP Server နှင့် ဆက်သွယ်ခြင်း

Github MCP Server သို့ ဆက်ရန်၊ chat box အောက်ဘက်ရှိ "Type your message here.." ဟု ပြထားသော နေရာအောက်ရှိ "plug" အိုင်ကွန်ကို ရွေးပါ:

![MCP ချိတ်ဆက်](../../../../../translated_images/my/mcp-chainlit-1.7ed66d648e3cfb28.webp)

အဲဒီနေရာမှ "Connect an MCP" ကို နှိပ်၍ Github MCP Server သို့ ဆက်ရန် command ကို ထည့်ပါ:

```bash
npx -y @modelcontextprotocol/server-github --env GITHUB_PERSONAL_ACCESS_TOKEN=[YOUR PERSONAL ACCESS TOKEN]
```

"[YOUR PERSONAL ACCESS TOKEN]" ကို သင့်၏ လက်ရှိ Personal Access Token ဖြင့် အစားထိုးပါ။

ဆက်သွယ်ပြီးနောက် plug အိုင်ကွန်အနီး၌ (1) ဟု ပြနေမည်ဖြစ်ပြီး ဆက်သွယ်ထားကြောင်း အတည်ပြုမည်။ မတွေ့ပါက `chainlit run app.py -w` ဖြင့် chainlit server ကို ပြန်စတင်ကြည့်ပါ။

## ဒေမိုကို အသုံးပြုခြင်း

hackathon project များအတွက် အကြံပြုရန် agent workflow ကို စတင်ရန် အောက်ပါမက်ဆေ့ချ်တစ်ခုကို ရိုက်ထည့်နိုင်သည်။

"Recommend hackathon projects for the Github user koreyspace"

Router Agent သည် သင့်တောင်းဆိုချက်ကို ခွဲခြမ်းစိတ်ဖြာပြီး သင့်မေးခွန်းကို ဖြေရှင်းရန်အတွက် ဘယ် agent ပေါင်းစပ်မှု (GitHub, Hackathon, နှင့် Events) များက သင့်တော်ဆုံးဖြစ်မည်ကို ဆုံးဖြတ်ပါလိမ့်မည်။ agents များသည် GitHub repository ခွဲခြမ်းစစ်ဆေးမှု၊ project အတွေးပေါ်ထွက်မှုနှင့် သက်ဆိုင်ရာ နည်းပညာအဖြစ်အပျက်များကို အခြေခံ၍ စုံလင်အကြံပြုချက်များ ပေးရန် ပူးပေါင်းလှုပ်ရှားကြသည်။

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
ရှင်းလင်းချက်:
ယခုစာရွက်စာတမ်းကို AI ဘာသာပြန်ဝန်ဆောင်မှု [Co-op Translator](https://github.com/Azure/co-op-translator) ဖြင့် ဘာသာပြန်ထားပါသည်။ ကျွန်ုပ်တို့သည် တိကျမှုအတွက် ကြိုးစားသော်လည်း အလိုအလျောက်ပြုလုပ်ထားသော ဘာသာပြန်ချက်များတွင် အမှားများ သို့မဟုတ် တိကျမှုနည်းပါးမှုများ ပါဝင်နိုင်သည်ကို ကျေးဇူးပြု၍ သတိပြုပါ။ မူလစာရွက်စာတမ်းကို မူလဘာသာဖြင့်သာ တရားဝင် အချက်အလက်အဖြစ် ယူဆသင့်သည်။ အရေးကြီးသော အချက်အလက်များအတွက် ပရော်ဖက်ရှင်နယ် လူဘာသာပြန်ကို အသုံးပြုရန် အကြံပြုပါသည်။ ဤဘာသာပြန်ချက်ကို အသုံးပြုမှုကြောင့် ဖြစ်ပေါ်နိုင်သည့် နားမလည်မှုများ သို့မဟုတ် မှားယွင်းစွာ နားလည်မှုများအတွက် ကျွန်ုပ်တို့ တာဝန်မယူပါ။
<!-- CO-OP TRANSLATOR DISCLAIMER END -->