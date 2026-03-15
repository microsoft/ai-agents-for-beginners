# Github MCP Server Example

## ဖော်ပြချက်

ဤသည်ကို Microsoft Reactor မှ ဧည့်ခံပွဲဖြစ်သည့် AI Agents Hackathon အတွက် ဖန်တီးထားသော ဒေမိုတစ်ခုဖြစ်သည်။

ဤကိရိယာများကို အသုံးပြုပြီး အသုံးပြုသူ၏ Github repos အပေါ် မူတည်၍ hackathon ပရောဂျက်များကို အကြံပြုရန် သုံးသည်။ ဤသည်ကို အောက်ပါအတိုင်း လုပ်ဆောင်သည်။

1. **Github Agent** - Github MCP Server ကို အသုံးပြုပြီး repos များနှင့် ထို repos များဆိုင်ရာ သတင်းအချက်အလက်များကို ရယူသည်။
2. **Hackathon Agent** - Github Agent မှ ပေးပို့သော ဒေတာကို ယူပြီး၊ အသုံးပြုသူ၏ project များ၊ အသုံးပြုသည့် ဘာသာစကားများနှင့် AI Agents hackathon အတွက် project track များကို အခြေခံ၍ ဖန်တီးမှုဆိုင်ရာ hackathon project အကြံအစည်များကို ထုတ်ပေးသည်။
3. **Events Agent** - Hackathon Agent ၏ အကြံပြုချက်များအပေါ် အခြေခံကာ Events Agent သည် AI Agent Hackathon စီးရီးမှ သက်ဆိုင်ရာ ပွဲများကို အကြံပြုပါမည်။

## ကုဒ်ကို လည်ပတ်ခြင်း

### ပတ်ဝန်းကျင် အပြင်အဆင် (Environment Variables)

ဒီ ဒေမိုတွင် Microsoft Agent Framework၊ Azure OpenAI Service၊ Github MCP Server နှင့် Azure AI Search များကို အသုံးပြုထားသည်။

ဤကိရိယာများကို အသုံးပြုရန် သင့်တွင် သင့်လျော်သော ပတ်ဝန်းကျင် အပြင်အဆင်များ သတ်မှတ်ထားသောကြောင်း အတည်ပြုပါ။

```python
AZURE_AI_PROJECT_ENDPOINT=""
AZURE_AI_MODEL_DEPLOYMENT_NAME=""
AZURE_SEARCH_SERVICE_ENDPOINT=""
AZURE_SEARCH_API_KEY=""
``` 

## Chainlit Server လည်ပတ်ခြင်း

MCP server ထံ ဆက်သွယ်ရန် ဤဒေမိုတွင် chat အင်တာဖေ့စ်အဖြစ် Chainlit ကို အသုံးပြုထားသည်။

server ကို လည်ပတ်ရန် terminal မှာ အောက်ပါ command ကို အသုံးပြုပါ။

```bash
chainlit run app.py -w
```

ဒါက သင့် Chainlit server ကို `localhost:8000` တွင် စတားပြီး သင့် Azure AI Search Index ကို `event-descriptions.md` အကြောင်းအရာဖြင့် ဖြည့်စွက်ပေးမည်ဖြစ်သည်။

## MCP Server ထံ ဆက်သွယ်ခြင်း

Github MCP Server သို့ ဆက်သွယ်ရန်၊ "plug" အိုင်ကွန်ကို "သင်၏မက်ဆေ့ခ််ကို ဤနေရာတွင် ရိုက်ထည့်ပါ.." ချက်ဘောက်အောက်မှ ရွေးပါ:

![MCP ချိတ်ဆက်ခြင်း](../../../../../translated_images/my/mcp-chainlit-1.7ed66d648e3cfb28.webp)

ယင်းနေရာမှ "MCP ချိတ်ဆက်ပါ" ကို နှိပ်၍ Github MCP Server သို့ ဆက်သွယ်ရန် command ကို ထည့်ပါ။

```bash
npx -y @modelcontextprotocol/server-github --env GITHUB_PERSONAL_ACCESS_TOKEN=[YOUR PERSONAL ACCESS TOKEN]
```

Replace "[YOUR PERSONAL ACCESS TOKEN]" with your actual Personal Access Token. 

ချိတ်ဆက်ပြီးနောက် plug အိုင်ကွန်အနီးတွင် (1) ကို မြင်ရမည်ဖြစ်ပြီး ၎င်းချိတ်ဆက်ပြီးဖြစ်ကြောင်း အတည်ပြုပါလိမ့်မည်။ မမြင်ရပါက `chainlit run app.py -w` ဖြင့် chainlit server ကို ပြန်စက်ထိန်းဖွင့်ကြည့်ပါ။

## ဒေမိုကို အသုံးပြုခြင်း

hackathon project များအကြံပြုရန် agent workflow ကို စတင်ရန်၊ အောက်ပါကဲ့သို့ မက်ဆေ့ခ်် တစ်ခု ရိုက်ထည့်နိုင်သည်။ 

"Github user koreyspace အတွက် hackathon project များ အကြံပြုပါ"

Router Agent သည် သင့်တောင်းဆိုချက်ကို ဖြတ်သန်းစစ်ဆေးပြီး သင့်တောင်းဆိုမှုကို ကိုင်တွယ်ရန် အထိရောက်ဆုံးသော agent တွေ (GitHub, Hackathon, နှင့် Events) ပေါင်းစပ်မှုကို ဆုံးဖြတ်ပေးမည်။ အဆိုပါ agent များသည် GitHub repository သုံးသပ်ချက်၊ project ဖန်တီးမှု အတွေးများနှင့် သက်ဆိုင်ရာ နည်းပညာပွဲများအပေါ် အခြေခံ၍ တိကျစုံလင်သော အကြံပြုချက်များကို ပံ့ပိုးပေးမည်။

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
သတိပေးချက်:
ဒီစာတမ်းကို AI ဘာသာပြန်ဝန်ဆောင်မှု [Co-op Translator](https://github.com/Azure/co-op-translator) ဖြင့် ဘာသာပြန်ထားပါသည်။ ကျွန်ုပ်တို့သည် တိကျမှန်ကန်မှုကို ကြိုးစားသော်လည်း အလိုအလျှောက် ပြုလုပ်သော ဘာသာပြန်ချက်များတွင် အမှားများ သို့မဟုတ် မှန်ကန်မှုချို့ယွင်းချက်များ ပါရှိနိုင်ကြောင်း သိရှိထားရပါသည်။ မူလစာတမ်းကို မူလဘာသာဖြင့်ရှိသော ခုခံအချက်အလက်အဖြစ် သတ်မှတ်၍ ကိုးကားသင့်ပါသည်။ အရေးကြီးသော အချက်အလက်များအတွက် လူ့ ပရော်ဖက်ရှင်နယ် ဘာသာပြန်ကို အသုံးပြုရန် အကြံပြုပါသည်။ ဤဘာသာပြန်ချက်ကို အသုံးပြုရာမှ ဖြစ်ပေါ်သည့် နားလည်မှုမှားယွင်းမှုများ သို့မဟုတ် အဓိပ္ပာယ်လွဲများအတွက် ကျွန်ုပ်တို့သည် တာဝန်မယူပါ။
<!-- CO-OP TRANSLATOR DISCLAIMER END -->