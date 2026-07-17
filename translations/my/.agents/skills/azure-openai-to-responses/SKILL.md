---
name: azure-openai-to-responses
license: MIT
---
# Python အက်ပ်များကို Azure OpenAI Chat Completions မှ Responses API သို့ ပြောင်းရွှေ့ခြင်း

> **အတည်ပြုလမ်းညွှန်ချက် — တိကျမှန်ကန်စွာလိုက်နာပါ**
>
> ဤကျွမ်းကျင်မှုသည် Python ကုဒ်ဘေ့စ်များကို Azure OpenAI Chat Completions မှ
> တည်ဆောက်ထားပြီး Responses API ကိုပြောင်းရွှေ့ခြင်းဖြစ်သည်။ ဤညွှန်ကြားချက်များကို တိကျမှန်ကန်စွာလိုက်နာပါ။
> မတော်တဆ parameter mapping များလုပ်ခြင်းသို့မဟုတ် API ပုံစံအသစ်များတီထွင်ခြင်း မပြုပါနှင့်။

---

## စတင်လုပ်ဆောင်ရန်အချက်များ

အသုံးပြုသူသည် အောက်ပါအချက်များကို လုပ်ဆောင်လိုသောအခါ ဤကျွမ်းကျင်မှုကို စတင်ပါ။
- Python အက်ပ်ကို Azure OpenAI Chat Completions မှ Responses API သို့ ပြောင်းရွှေ့ရန်
- Python OpenAI SDK အသုံးပြုမှုကို Azure OpenAI အတွက် နောက်ဆုံး API ပုံစံသို့ တိုးမြှင့်ရန်
- Responses များအတွက် ပြင်ဆင်ထားရန် GPT-5 သို့မဟုတ်ပိုမိုသစ်သော မော်ဒယ်များအတွက် Python ကုဒ်ပြင်ဆင်ရန်
- `AzureOpenAI`/`AsyncAzureOpenAI` မှ ပြောင်းလဲ၍ `OpenAI`/`AsyncOpenAI` စံနမူနာ client ကို v1 endpoint နှင့်အသုံးပြုရန်
- `AzureOpenAI` constructor များသို့မဟုတ် `api_version` သက်ဆိုင်သော ဖျက်သိမ်းခြင်း သတိပေးချက်များကို ပြင်ဆင်ရန်

---

## ⚠️ မော်ဒယ်သင့်တော်မှု — စစ်ဆေးပါ

> **ပြောင်းရွှေ့ခြင်းမပြုမီ၊ သင့် Azure OpenAI deployment သည် Responses API ကို ပံ့ပိုးထားမထားစစ်ဆေးပါ။**

### ၁။ သင့် deployment ကို Smoke-test ဆောင်ရွက်ခြင်း (အမြန်ဆုံး)

```python
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ["AZURE_OPENAI_API_KEY"],
    base_url=f"{os.environ['AZURE_OPENAI_ENDPOINT'].rstrip('/')}/openai/v1/",
)

try:
    resp = client.responses.create(
        model=os.environ["AZURE_OPENAI_DEPLOYMENT"],
        input="ping",
        max_output_tokens=50,
        store=False,
    )
    print(f"✅ Deployment supports Responses API: {resp.output_text}")
except Exception as e:
    print(f"❌ Deployment does NOT support Responses API: {e}")
```

> **မှတ်ချက်**: Azure OpenAI တွင် `max_output_tokens` ၏အနည်းဆုံးတန်ဖိုးမှာ **၁၆** ဖြစ်သည်။ ၁၆ ထက်နည်းပါက 400 error ပြန်ထုတ်ပါလိမ့်မယ်။ Smoke-test အတွက် ၅၀+ ကိုအသုံးပြုပါ။

ဤကိစ္စသည် 404 ပြန်လည်ရရှိပါက၊ ထို deployment ၏ မော်ဒယ်သည် Responses ကိုမပံ့ပိုးသေးပါ — အောက်ပါ ကိုးကားချက်ကိုစစ်ဆေးပါ သို့မဟုတ် ပံ့ပိုးသော မော်ဒယ်ဖြင့် ပြန်လည် deploy ပြုလုပ်ပါ။

### ၂။ သင့်ဒေသရှိ လွှမ်းမိုးသော မော်ဒယ်များကို စစ်ဆေးခြင်း (အကြံပြု)

သင့်ဒေသတွင် Responses API ပံ့ပိုးမှုရှိသည့် မော်ဒယ်များအား ကြည့်ရှုရန် မော်ဒယ်သင့်တော်မှု ကိရိယာကို အသုံးပြုပါ။

```bash
python migrate.py models --subscription YOUR_SUB_ID --location YOUR_REGION
```

ဤသည်သည် Azure ARM ကို တိုက်ရိုက်မေးမြန်းကာ မော်ဒယ်များက Responses, စနစ်တကျထွက်ရှိမှု၊ ကိရိယာများကဲ့သို့ ပံ့ပိုးမှုရှိ/မရှိ၊ စသည်တို့ကို ပြမြောက်သည်။ `--filter gpt-5.1,gpt-5.2` ဖြင့် ရလဒ်ကို ကန့်သတ်နိုင်ပြီး `--json` ဖြင့် စီမံရေးသားနိုင်သည်။

### ၃။ မော်ဒယ်ပံ့ပိုးမှု အပြည့်အစုံ ကိုးကားချက်

- **တိုက်ရိုက်မေးမြန်းခြင်း**: `python migrate.py models` (အထက်က အတိုင်း — ဒေသအလိုက်၊ အမြဲတမ်းအပ်ဒိတ်)
- **ရရှိနိုင်မှုကြည့်ရှုမှု**: [မော်ဒယ်အကျဉ်းချုပ်စာရင်းနှင့် ဒေသရရှိနိုင်မှု](https://learn.microsoft.com/en-us/azure/foundry/foundry-models/concepts/models-sold-directly-by-azure?tabs=global-standard-aoai%2Cglobal-standard&pivots=azure-openai#model-summary-table-and-region-availability)
- **စတင်အသုံးပြုခြင်းနှင့် လမ်းညွှန်ချက်**: **https://aka.ms/openai/start**

### ⚠️ ဝေးကျော်သုံး မော်ဒယ်အကန့်အသတ်များ

> **သတိပေးချက်**: `gpt-4.1` မတိုင်မီ မော်ဒယ်များသည် Responses API ၏ အင်္ဂါရပ်များအားလုံးကို ပြည့်ဝစွာမပံ့ပိုးနိုင်ပါ။
>
> အသိအမှတ်ပြုသော ဝေးကျော်သုံး မော်ဒယ်အကန့်အသတ်များမှာ -
> - **`reasoning` parameter**: ထိုမော်ဒယ်များအတွက် မပံ့ပိုးပါ။ အရင်ကကုဒ်တွင် ရှိခဲ့လျှင်သာ ပြောင်းရွှေ့ပါ။
> - **`seed` parameter**: Responses API တွင် မပံ့ပိုးပါ — အားလုံးမှ ဖယ်ရှားပစ်ပါ။
> - **`text.format` မှ စနစ်တကျ ထွက်ရှိမှု**: ဝေးကျော်သုံး မော်ဒယ်များတွင် `strict: true` JSON စံသတ်မှတ်ချက်များ မတိကျစွာ အကောင်အထည်ဖော်နိုင်ပါ။
> - **ကိရိယာ စီမံခန့်ခွဲမှု**: GPT-5+ သည် ချဉ်းကပ်မှုအတွင်း ကိရိယာခေါ်ဆိုမှုများ ကို ပြုလုပ်သည်။ ဝေးကျော်သုံး မော်ဒယ်များတွင် အလွှာထပ်ခွဲခြင်းမရှိပေ။
> - **အပူချိန် ကန့်သတ်ချက်များ**: `gpt-5` သို့ ပြောင်းရာတွင် temperature ကို ဖယ်ရှားရန် သို့မဟုတ် `1` သတ်မှတ်ရမည်။ ဝေးကျော်သုံး မော်ဒယ်များတွင် ကန့်သတ်ချက် မရှိပါ။

### O-series reasoning မော်ဒယ်များ (o1, o3-mini, o3, o4-mini)

O-series မော်ဒယ်များတွင် parameter ကန့်သတ်ချက် ထူးခြားသည်။ ဤမော်ဒယ်များသို့ ပစ်မှတ်ထားသော အက်ပ်များ ပြောင်းရွှေ့သည့်အခါ -

- **`temperature`**: `1` ဖြစ်ရမည် (သို့မဟုတ် ဖယ်ရှားထားရမည်)။ အခြားတန်ဖိုး မလက်ခံပါ။
- **`max_completion_tokens` → `max_output_tokens`**: Azure အထူး `max_completion_tokens`  အသုံးပြုသော အက်ပ်များသည် `max_output_tokens` သို့ ပြောင်းရန်။ လက်လှမ်းမီသည့် တန်ဖိုးများ (4096+) သတ်မှတ်ပါ၊ reasoning tokens သည် ကန့်သတ်ချက်ထဲ တက်ရှိသည်။
- **`reasoning_effort`**: အက်ပ်မှ `reasoning_effort` (နည်း/အလယ်/မြင့်) အသုံးပြုလျှင် ထိန်းသိမ်းပါ၊ Responses API သည် o-series မော်ဒယ်များအတွက် အထောက်အပံ့ပေးပါသည်။
- **စတီးမင်း့ ဖွင့်လှစ်ခြင်း**: O-series မော်ဒယ်များသည် reasoning ပြီးဆုံးမှ text delta events များ ထုတ်လွှင့်နိုင်ရန် output ကို buffer ထားသည်။ စတီးမင်း့င်သည် ထုံးစံအတိုင်း လုပ်ဆောင်နိုင်သော်လည်း ပထမအကြိမ် `response.output_text.delta` သည် GPT မော်ဒယ်များထက် နာရီကြာစောင့်ရနိုင်ပါသည်။
- **`top_p`**: O-series တွင် မပံ့ပိုးပါ — ရှိပါက ဖယ်ရှားပါ။
- **ကိရိယာအသုံးပြုမှု**: O-series မော်ဒယ်များသည် Responses API မှတဆင့် GPT မော်ဒယ်များလို ကိရိယာများကို ပံ့ပိုးသည်၊ သို့သော် ကိရိယာ ခေါ်ဆိုမှု စီမံခန့်ခွဲမှု အရည်အသွေး မရွေးပါ။

**လှုပ်ရှားမှု — မော်ဒယ် အကြံပြုချက် အသိပေးမှု**: စကင်အဆင့်တွင် အက်ပ်သည် မည်သည့် မော်ဒယ်ကို ပစ်မှတ်ထားသည်ကို (deployment အမည်များ၊ env vars၊ config) စစ်ဆေးပါ။ မော်ဒယ်သည် `gpt-4.1` မမီပါက (gpt-4.1+ မဟုတ်ပါ) အသုံးပြုသူအား အောက်ပါအချက်များ ပြောကြားပေးပါ -
- အဆိုပါပြောင်းရွှေ့ခြင်းသည် ပထမဦးဆုံး စာသား၊ စကားပြော၊ စတီးမင်း့င် နှင့် ကိရိယာများ အတွက် လုပ်ဆောင်နိုင်ပါလိမ့်မယ်။
- နောက်ဆုံးမော်ဒယ်များ (`gpt-5.1`, `gpt-5.2`) သည် ကိရိယာ စီမံခန့်ခွဲမှုပိုမိုကောင်းမွန်မှု၊ စနစ်တကျ output enforcement, reasoning နှင့် ဒေသပေါ်မူတည်သောရရှိနိုင်မှု ပိုမိုကောင်းတယ်။
- သင့်အနေနဲ့ deployment ကို ပြင်ဆင်ပြီးသာ မြှင့်တင်စဉ်းစားသင့်သည် — ပြောင်းရွှေ့ခြင်းကို အတားအဆီးမဖြစ်ပါ။

မော်ဒယ် ဗားရှင်းအပေါ် မူတည်၍ ပြောင်းရွှေ့မှုကို တားမြစ်ခြင်း သို့မဟုတ် ငြင်းဆန်ခြင်း မပြုပါနှင့်။ အကြံပြုချက်ဖြစ်သည်။

### GitHub Models သည် Responses API ကို မပံ့ပိုးပါ

> **GitHub Models (`models.github.ai`, `models.inference.ai.azure.com`) သည် Responses API ကို မပံ့ပိုးပါ။**

ကုဒ်ဘေ့စ်တွင် GitHub Models ၏ ကုဒ်လမ်းကြောင်းရှိလျှင် ( `base_url` ကို `models.github.ai` သို့မဟုတ် `models.inference.ai.azure.com` သို့ညွှန်ပြသည်ဟု ရှာပါ)၊ **ပြောင်းရွှေ့မှုအတွက် အလုံးစုံ ဖယ်ရှားပစ်ပါ**။ Responses API သည် Azure OpenAI, OpenAI သို့မဟုတ် Ollama ကဲ့သို့ Responses ပံ့ပိုးသော ကိုက်ညီသော ဒေသတွင်း endpoint ကိုသာ လိုအပ်သည်။

စကင်အချိန်၌ လုပ်ဆောင်ရန် -
- GitHub Models ၏ ကုဒ်လမ်းကြောင်းများကို ဖယ်ရှားရန် မှတ်သားပါ။

---

## ဖရိမ်ဝွတ်ပြောင်းရွှေ့ခြင်း

အများအပြားသော အက်ပ်များသည် OpenAI ပေါ်တွင် အဆင့်မြင့် ဖရိမ်ဝွတ်များ အသုံးပြုကြသည်။ ဤမျိုးကို ပြောင်းရွှေ့သည့်အခါ ဖရိမ်ဝွတ်၏ ကိုယ်ပိုင် API ပြောင်းလဲမှုများ၊ အောက်ခံ OpenAI ခေါ်ဆိုမှုများသာမကပါ။

### Microsoft Agent Framework (MAF)

**ပထမဆုံး သင့် MAF ဗားရှင်းကို စစ်ဆေးပါ** — ပြောင်းရွှေ့မှုသည် သင်၏ MAF 1.0.0+ သို့မဟုတ် pre-1.0.0 beta/rc ပေါ် မူတည်သည်။

#### MAF 1.0.0+ (agent-framework-openai >= 1.0.0)

`OpenAIChatClient` သည် **ရေ့ပုံ Responses API ကို အသုံးပြုနေပြီး** — ပြောင်းရွှေ့ရန် မလိုပါ။ legacy `OpenAIChatCompletionClient` ( `chat.completions.create` ကို သုံးသည်) ကို အသုံးပြုနေပါက `OpenAIChatClient` ဖြင့်အစားထိုးပါ။

| မတိုင်မီ | ပြီးနောက် |
|--------|-------|
| `from agent_framework.openai import OpenAIChatCompletionClient` | `from agent_framework.openai import OpenAIChatClient` |
| `OpenAIChatCompletionClient(...)` | `OpenAIChatClient(...)` |

သင့်ဗားရှင်းကို စစ်ဆေးရန်: `python -c "import agent_framework_openai; print(agent_framework_openai.__version__)"`

#### MAF pre-1.0.0 (beta/rc ထုတ်လုပ်ချက်များ)

pre-1.0.0 MAF တွင် `OpenAIChatClient` သည် Chat Completions ကို အသုံးပြုခဲ့သည်။ `agent-framework-openai>=1.0.0` သို့ မြှင့်တင်ပါ၊ ဤတွင် `OpenAIChatClient` သည် Responses API ကို ပုံမှန်အသုံးပြုသည်။

အခြားပြောင်းလဲမှု မလိုပါ — `Agent` နှင့် ကိရိယာ API များသည် အတူတူဖြစ်နေသည်။

### LangChain (`langchain-openai`)

`ChatOpenAI()` သို့ `use_responses_api=True` ကို ထည့်ပါ။ ပြီးတော့ response ၏ `.content` ကို `.text` သို့ ပြောင်းပါ။

| မတိုင်မီ | ပြီးနောက် |
|--------|-------|
| `ChatOpenAI(model=..., base_url=..., api_key=...)` | `ChatOpenAI(model=..., base_url=..., api_key=..., use_responses_api=True)` |
| `result['messages'][-1].content` | `result['messages'][-1].text` |

အပြည့်အစုံ မျှဝေမှုများအတွက် [cheat-sheet.md](./references/cheat-sheet.md) ကို ကြည့်ရှုနိုင်ပါသည်။

---

## Frontend ပြောင်းရွှေ့ခြင်း လမ်းညွှန်ချက်

> **Responses API သည် server-side ဆိုင်ရာဖြစ်သည်။** သင်၏ Python backend ကိုပြောင်းရွှေ့ပါ; frontend ၏ HTTP သဘောတူညီချက်သည် မပြောင်းလဲသင့်ပါ (backend သည် thin pass-through ဖြစ်လျှင်သာ) — ဤအခြေအနေ၌ Responses request ပုံစံကို လက်ခံရန် ထည့်စဉ်းစားပါ။ Frontend က client-side အချက်အလက်ဖြင့် OpenAI ကိုတိုက်ရိုက်ခေါ်လျှင်၊ ဒီခေါ်ဆိုမှုများကို မူလ backend သို့ငြိမ့်ရွှေ့ပါ။

### `@microsoft/ai-chat-protocol` ဖျက်သိမ်းခြင်း

`@microsoft/ai-chat-protocol` npm package ကို အသုံးမပြုတော့ဘဲ [`ndjson-readablestream`](https://www.npmjs.com/package/ndjson-readablestream) ဖြင့် အစားထိုးသင့်သည်။ Frontend တွင် စတင်တွေ့ပါက -

၁။ CDN script tag ကို အစားထိုးပါ:
   ```html
   <!-- Before -->
   <script src="https://cdn.jsdelivr.net/npm/@microsoft/ai-chat-protocol@.../dist/iife/index.js"></script>
   <!-- After -->
   <script src="https://cdn.jsdelivr.net/npm/ndjson-readablestream@1.0.7/dist/ndjson-readablestream.umd.js"></script>
   ```
၂။ `AIChatProtocolClient` instantiation ကို ဖယ်ရှားပါ (`new ChatProtocol.AIChatProtocolClient("/chat")`)။
၃။ `client.getStreamedCompletion(messages)` ကို fetch() ကိုနောက်ခံ streaming endpoint သို့ တိုက်ရိုက်ခေါ်ဆိုပါ။
၄။ `for await (const response of result)` ကို `for await (const chunk of readNDJSONStream(response.body))` ဖြင့် ပြောင်းပါ။
၅။ `response.delta.content` / `response.error` မှ `chunk.delta.content` / `chunk.error` သို့ property access ပြောင်းပါ။

---

## ရည်ရွယ်ချက်များ

- Azure OpenAI အတွက် Chat Completions သို့မဟုတ် legacy Completions ကို အသုံးပြုနေသော Python ခေါ်ဆိုမှုပိုင်းအားလုံး စာရင်းပြုစုပါ။
- Python ကုဒ်ဘေ့စ်အတွက် ပြောင်းရွှေ့ခြင်းအစီအစဉ်နှင့် စဉ်လိုက် အချိန်ဇယားကို သတ်မှတ်ပါ။
- Responses API သို့ လုံခြုံပြီး အနည်းဆုံး ပြောင်းလဲမှုများ လုပ်ဆောင်ပါ။
- Responses ထွက်ရှိမှု schema ကို အသုံးပြုရန် ခေါ်ဆိုသူများကို တိုးတက်သိသာစေပါ; အကျိုးသက်ရောက်မှုအတွက် wrappers မလိုအပ်ပါ။
- စမ်းသပ်မှုများ/ lint များ ပြုလုပ်ပြီး ပြောင်းလဲမှုကြောင့် ဖြစ်ပေါ်သော သိသာခြင်းမရှိသေးသော ပြဿနာများ ဖြေရှင်းပါ။
- သေးငယ်၍ သုံးသပ်နိုင်သော ပြောင်းလဲမှုစုစည်းမှုများ ပြုစုပြီး နောက်ဆုံးအကျဉ်းချုပ်အဖြစ် diff များနှင့် ပေးပို့ပါ (commit မလုပ်ပါနှင့်)။

---

## ကာကွယ်စောင့်ကြည့်မှု

- git workspace အတွင်းရှိ ဖိုင်များသာ ပြင်ဆင်ပါ။ အပြင်ဘက်ကို မရေးသားပါနှင့်။
- အနောက်မှ အားနည်းမှုသိုလှောင်ထားခြင်းများ တစ်စုံတစ်ရာ ထိန်းသိမ်းထားခြင်းမပြုပါ။ ကုဒ်ကို API ပုံစံအသစ်သို့ ပြောင်းရွှေ့ပါ။
- သားမွေးတင်တိုက်ရှာမှု မက်ဆေ့ခ်ျ/ အကူအညီ စာများ သို့မဟုတ် အထောက်အထားဖိုင်များ မထားပါနှင့်။
- ယခင်တွင် streaming ကို အသုံးပြုခဲ့လျှင် ထိန်းသိမ်းပါ; မဟုတ်ပါက non-streaming ကို အသုံးပြုပါ။
- မှတ်ချက်မိန့်ခွန်း (approval mode) တွင် အမိန့်များ သို့မဟုတ် ကွန်ယက်ခေါ်ဆိုမှုများ လုပ်မည့်အခါ အတည်ပြုချက် မေးပါ။
- `git add`/`git commit`/`git push` မလုပ်ပါနှင့်; working-tree ပြင်ဆင်ခြင်းများသာ ဖန်တီးပါ။

---

## အဆင့် ၀: Azure OpenAI Client ပြောင်းရွှေ့ခြင်း (လိုအပ်ချက်)

ကုဒ်ဘေ့စ်တွင် `AzureOpenAI` သို့မဟုတ် `AsyncAzureOpenAI` constructor များကို အသုံးပြုထားပါက စုစုပေါင်း `OpenAI` / `AsyncOpenAI` constructor များသို့ ယခင်ဆုံး ပြောင်းရွှေ့ပါ။ Azure အထူး constructor များသည် `openai>=1.108.1` တွင် ဖျက်သိမ်းထားသည်။

### v1 API လမ်းကြောင်း ဘာကြောင့်?

အသစ် `/openai/v1` endpoint သည် `AzureOpenAI()` မှ မဟုတ်ဘဲ `OpenAI()` client စံနမူနာကို သုံးသည်၊ `api_version` parameter မလိုအပ်၊ OpenAI နှင့် Azure OpenAI တို့တွင် ထပ်တူတူ လုပ်ဆောင်သည်။ client ကုဒ်တစ်ခုဖြင့် အနာဂတ်ကိုကြိုတင်ကာကွယ်ထားသည် — ဗားရှင်း စီမံခန့်ခွဲမှု မလိုအပ်ပါ။

### အဓိကပြောင်းလဲမှုများ

| မတိုင်မီ | ပြီးနောက် |
|--------|-------|
| `AzureOpenAI` | `OpenAI` |
| `AsyncAzureOpenAI` | `AsyncOpenAI` |
| `azure_endpoint` | `base_url` |
| `azure_ad_token_provider` | `api_key` |
| `api_version=...` | အပြီးအစီး ဖယ်ရှားပါ |

### ရှင်းလင်းအတတ်ပညာ စစ်ဆေးစရာစာရင်း

- client constructor မှ `api_version` argument ကို ဖယ်ရှားပါ။
- `.env`, app setting များနှင့် Bicep/infra ဖိုင်များမှ `AZURE_OPENAI_VERSION` / `AZURE_OPENAI_API_VERSION` environment variables များကို ဖယ်ရှားပါ။
- `.env`, app setting များနှင့် Bicep/infra ၊ test fixture များတွင် `AZURE_OPENAI_CLIENT_ID` ကို `AZURE_CLIENT_ID` ဟု ပြောင်းပါ (Azure Identity SDK ရိုးရာစည်းမျဉ်း)။
- `requirements.txt` သို့မဟုတ် `pyproject.toml` တွင် `openai>=1.108.1` ဖြစ်ကြောင်း သေချာပါစေ။

### environment variable ပြောင်းရွှေ့မှု

| အဟောင်း env var | လုပ်ဆောင်မှု | မှတ်ချက်များ |
|-------------|--------|-------|
| `AZURE_OPENAI_VERSION` | **ဖယ်ရှားပါ** | v1 endpoint တွင် `api_version` မလိုအပ်ပါ |
| `AZURE_OPENAI_API_VERSION` | **ဖယ်ရှားပါ** | အထက်ပါအတိုင်း |
| `AZURE_OPENAI_CLIENT_ID` | **အမည်ပြောင်းပါ** → `AZURE_CLIENT_ID` | `ManagedIdentityCredential(client_id=...)` အတွက် Azure Identity SDK ရိုးရာစည်းမျဉ်း |
| `AZURE_OPENAI_ENDPOINT` | **ထိန်းသိမ်းပါ** | `base_url` ဖန်တီးရာတွင် မလိုလျော့နိုင်ပါ |
| `AZURE_OPENAI_CHAT_DEPLOYMENT` | **ထိန်းသိမ်းပါ** | `responses.create` ၏ `model` parameter အဖြစ် အသုံးပြုသည် |
| `AZURE_OPENAI_API_KEY` | **ထိန်းသိမ်းပါ** | key-based authentication အတွက် `api_key` အဖြစ် အသုံးပြုသည် |

client setup ကုဒ် နမူနာများ (sync, async, EntraID, API key, multi-tenant) အတွက် [cheat-sheet.md](./references/cheat-sheet.md) ကိုကြည့်ပါ။

---

## အဆင့် ၁: Legacy ခေါ်ဆိုမှုများ ရှာဖွေခြင်း

ပြောင်းရွှေ့ရန်လိုအပ်သော ခေါ်ဆိုမှုများအားလုံးကို တွေ့ဖို့ [detect_legacy.py](../../../../../.agents/skills/azure-openai-to-responses/scripts/detect_legacy.py) စကရစ်ပ်ကို အသုံးပြုပါ။

```bash
python skills/azure-openai-to-responses/scripts/detect_legacy.py .
```

သို့မဟုတ် လက်ဖြင့် ရှာဖွေရန်—ကိုက်ညီမှုတိုင်းဟာ ပြောင်းရွှေ့ရန် ဂိုဏ်းတစ်ခုဖြစ်သည်။

```bash
# အရင် API ကော်လ်များ (ပြန်ရေးရေးရန်လိုအပ်သည်)
rg "chat\.completions\.create"
rg "ChatCompletion\.create"
rg "Completion\.create"

# ရှေးမသုံးတော့သော Azure client constructor များ (အစားထိုးရန်လိုအပ်သည်)
rg "AzureOpenAI\("
rg "AsyncAzureOpenAI\("

# တုံ့ပြန်ပုံစံ ဝင်ရောက်ခြင်း များ (နောက်ဆုံးပေါ် ပြင်ဆင်ရန်လိုအပ်သည်)
rg "choices\[0\]\.message\.content"
rg "choices\[0\]\.delta\.content"
rg "choices\[0\]\.message\.function_call"
rg "choices\[0\]\.message\.tool_calls"

# သုံးစွဲ工具 တိုင်ကြိုးသေးသောပုံစံ (တင်ချဲ့ရန်လိုအပ်သည်)
rg '"function":\s*{\s*"name"'
rg "pydantic_function_tool"

# သုံးစွဲ工具 ရလဒ်များဟောင်းပုံစံ (function_call_output သို့ပြောင်းရန်လိုအပ်သည်)
rg '"role":\s*"tool"'
rg '"tool_call_id"'

# ရှေးခေတ် параметр များ (ဖယ်ရှားရန် သို့မဟုတ် အမည်ပြောင်းရန်လိုအပ်သည်)
rg "response_format"
rg "max_tokens\b"        # max_output_tokens အဖြစ် အမည်ပြောင်းပါ
rg "['\"]seed['\"]"      # remove entirely

# ရှေးခေတ် περιβάλλον μεταβλητές များ (သန့်ရှင်းရေးလုပ်ရန်)
rg "AZURE_OPENAI_API_VERSION|AZURE_OPENAI_VERSION"
rg "AZURE_OPENAI_CLIENT_ID"  # AZURE_CLIENT_ID ဖြစ်သင့်သည်

# GitHub Models endpoint များ (ဖယ်ရှားရန် — Responses API မထောက်ပံ့)
rg "models\.github\.ai|models\.inference\.ai\.azure"

# Framework- အဆင့် ရှေးရိုးစနစ်များ (နောက်ဆုံးပေါ် ပြင်ဆင်ရန်လိုအပ်သည်)
rg "OpenAIChatCompletionClient"  # MAF 1.0.0+ : OpenAIChatClient ဖြင့် အစားထိုးပါ
rg "ChatOpenAI\(" | grep -v "use_responses_api"  # LangChain: use_responses_api=True လိုအပ်သည်

# စမ်းသပ်ရေး အဆောက်အအုံ (နောက်ဆုံးပေါ် ပြင်ဆင်ရန်လိုအပ်သည်)
rg "ChatCompletionChunk|AsyncCompletions\.create" tests/
rg "_azure_ad_token_provider" tests/
rg "prompt_filter_results|content_filter_results" tests/
rg "choices\[0\]" tests/

# အကြောင်း ဖန်တီးမှု အမှား ကိုယ်ထည် ဝင်ရောက်ခြင်း (ပြင်ဆင်ရန် — အဖွဲ့အစည်း ပြောင်းလဲသည်)
rg 'innererror.*content_filter_result|error\.body\["innererror"\]'
rg "content_filter_result\[" # ဟောင်းသော ဂဏန်းတစ်ခုစွန်းပုံစံ — ယခု content_filter_results (အများ) သည် content_filters array အတွင်းရှိသည်

# Chat Completions endpoint တွင် သဘာဝ HTTP ကော်လ်များ (URL ကိုနောက်ဆုံးပေါ် ပြင်ဆင်ရန်လိုအပ်သည်)
rg "/openai/deployments/.*/chat/completions"
rg "api-version="
```

### လမ်းညွှန်ချက်များ (သိရှိ၊ ပြန်ရေးခြင်း)

- **Chat Completions client**: `client.chat.completions.create` → `client.responses.create(...)`။

- **Azure client constructors**: `AzureOpenAI(...)` → `OpenAI(base_url=..., api_key=...)`။
- **Tools**: function-calling tool သတ်မှတ်ချက်များကို nested ဖော်စပ်မှုမှ (`{"type": "function", "function": {"name": ...}}`) flat Responses ဖော်မတ်သို့ (`{"type": "function", "name": ...}`) ပြောင်းပြင်ပါ။ `tool_choice` ကို အသုံးပြုပါ။ tool ရလဒ်များကို `{"type": "function_call_output", "call_id": ..., "output": ...}` အမျိုးအစား (မဟုတ်သော `{"role": "tool", ...}`) အဖြစ် ပြန်ပေးပါ။
- **Tool round-trips**: model သည် function calls ပြန်လည်ပေးသည့်အခါ `response.output` items များကို စကားပြောပွဲတွင် ထည့်သွင်းပါ (manual `{"role": "assistant", "tool_calls": [...]}` dict မဟုတ်)။ ထို့နောက် ရလဒ်တစ်ခုချင်းစီအတွက် `function_call_output` items များ ထည့်သွင်းပါ။
- **Few-shot tool examples**: စကားပြောပွဲတွင် hardcoded tool call နမူနာများပါဝင်လျှင်၊ `{"type": "function_call", "id": "fc_...", "call_id": "fc_...", ...}` + `{"type": "function_call_output", ...}` items များသို့ ပြောင်းပါ။ IDs များသည် `fc_` ဖြင့် စတင်ရမည်။
- **`pydantic_function_tool()`**: ဤ helper သည် ဆက်လက်ပင် အဟောင်း nested ဖော်စပ်မှုကို ထုတ်လုပ်ပြီး `responses.create()` နှင့် **မကိုက်ညီပါ**။ manual tool သတ်မှတ်ချက်များ သို့မဟုတ် flattening wrapper ဖြင့် အစားထိုးပါ။
- **Multi-turn**: စကားပြောဖော်ပြမှုမှတ်တမ်းကို app တွင် ထိန်းသိမ်းထားပါ။ ယခင် လှည့်များကို `input` items ဖြင့် ပေးပို့ပါ။
- **Formatting**: Chat ၏ top-level `response_format` ကို Responses တွင် `text.format` ဖြင့် အစားထိုးပါ။ canonical ဖော်စပ်ချက်မှာ `text={"format": {"type": "json_schema", "name": "Output", "strict": True, "schema": {...}}}` ဖြစ်သည်။
- **Content items**: Chat ၏ `content[].type: "text"` ကို Responses ၏ `content[].type: "input_text"` သို့ အစားထိုးပါ။ အသုံးပြုသူ/စနစ် လှည့်များအတွက်ဖြစ်သည်။
- **Image content items**: Chat ၏ `content[].type: "image_url"` ကို Responses ၏ `content[].type: "input_image"` သို့ အစားထိုးပါ။ `image_url` ကွင်းကို nested object `{"url": "..."}` မှ flat string သို့ ပြောင်းလဲသည်။ cheat sheet တွင် အရင်/နောက် နမူနာများကို ကြည့်ပါ။
- **Reasoning effort**: **ကုဒ်တွင် မပြင်ဆင်မီ၊ `reasoning` ရှိမှသာ လှည့်ပြောင်းပါ။**
- **Content filter error handling**: error body ဖွဲ့စည်းမှု ပြောင်းလဲသည်။ Chat Completions သည် `error.body["innererror"]["content_filter_result"]`(singular) ကို သုံးပြီး Responses API သည် `error.body["content_filters"][0]["content_filter_results"]`(plural, array ထဲ) ကို သုံးသည်။ `innererror` သို့ 접근ရာ၌ `KeyError` တက်မည်။ အသစ်သောလမ်းကြောင်းကို ပြန်ရေးပါ။
- **Raw HTTP calls**: app သည် Azure OpenAI REST API ကိုတိုက်ရိုက် သုံးသည်ဆိုပါက (`requests`, `httpx` စသည်ဖြင့်) `/openai/deployments/{name}/chat/completions?api-version=...` မှ `/openai/v1/responses` သို့ ပြောင်းပါ။ requests body မှ `messages` → `input` ပြောင်းပြီး `max_output_tokens`, `store: false` ထည့်ပါ၊ `api-version` query param ကို ဖယ်ရှားပါ။ response body မှ `choices[0].message.content` → `output[0].content[0].text` (မှတ်ချက်- `output_text` သည် SDK မှ အဆင်ပြေမှုအတွက် မူလ raw REST JSON တွင် မပါဝင်ပါ) ဖြစ်သည်။

---

## အဆင့် ၂: လှည့်ပြောင်းမှု အကောင်အထည်ဖော်ခြင်း

### လှည့်ပြောင်းမှု မှတ်ချက်များ (Chat Completions → Responses)

- **လှည့်ပြောင်းရခြင်း အကြောင်း**: Responses သည် စာသား၊ tools နှင့် streaming အတွက် ဆက်စပ် API ဖြစ်ပြီး Chat Completions သည် အရင်က API ဖြစ်သည်။ GPT-5 အသုံးပြုမှုတွင် Responses API ကို ဦးစားပေးသုံးရန်လိုအပ်သည်။
- **HTTP**: Azure endpoint ကို `/openai/deployments/{name}/chat/completions` မှ `/openai/v1/responses` သို့ ပြောင်းသည်။
- **Field များ**: `messages` → `input`, `max_tokens` → `max_output_tokens`။ `temperature` ပြောင်းရွှေ့မှု မရှိ။
- **Formatting**: `response_format` → `text.format` (object ဖြင့်) ဖြစ်သည်။
- **Content items**: Chat ၏ `content[].type: "text"` ကို Responses ၏ `content[].type: "input_text"` သို့ အစားထိုးပါ။ စနစ်/အသုံးပြုသူ လှည့်များများအတွက် ဖြစ်သည်။
- **Image content items**: Chat ၏ `content[].type: "image_url"` ကို Responses ၏ `content[].type: "input_image"` သို့ အစားထိုးပါ။ `image_url` ကွင်းသည် `{"image_url": {"url": "..."}}` မှ `{"image_url": "..."}` (စက်ကွင်း မဖြစ်သော string - HTTPS URL သို့မဟုတ် `data:image/...;base64,...` data URI) သို့ ပြောင်းလဲသည်။

### ပါရာမီတာ အသေးစိတ် တွဲဖက်ညွှန်ကြားချက်

| Chat Completions | Responses API |
|-----------------|---------------|
| `prompt` | `input` |
| `messages` | `input` (items များ Array ဖြစ်သည်) |
| `max_tokens` | `max_output_tokens` |
| `response_format` | `text.format` (object) |
| `temperature` | `temperature` (မပြောင်းလဲ) |
| `stop` | `stop` (မပြောင်းလဲ) |
| `frequency_penalty` | `frequency_penalty` (မပြောင်းလဲ) |
| `presence_penalty` | `presence_penalty` (မပြောင်းလဲ) |
| `tools` / function-calling | `tools` (မပြောင်းလဲ) |
| `seed` | **ဖယ်ရှားပါ** (မထောက်ပံ့ပါ) |
| `store` | `store` (`false` အဖြစ် သတ်မှတ်ရမည်) |
| `content[].type: "text"` | `content[].type: "input_text"` |
| `content[].type: "image_url"` | `content[].type: "input_image"` |
| `"image_url": {"url": "..."}` | `"image_url": "..."` (flat string) |

အပြည့်အစုံနမူနာများအတွက် [cheat-sheet.md](./references/cheat-sheet.md) ကို ကြည့်ပါ။

စမ်းသပ်မှု တည်ဆောက်ရေး လှည့်ပြောင်းမှု (mocks, snapshots, assertions) များအတွက် [test-migration.md](./references/test-migration.md) ကို ကြည့်ပါ။

အမှားများနှင့် လုပ်ဆောင်ရာ၌ ဖြစ်ပေါ်နိုင်စရာပြဿနာများအတွက် [troubleshooting.md](./references/troubleshooting.md) ကို ကြည့်ပါ။

---

## ဒေတာ သိမ်းဆည်းမှုနှင့် အခြေအနေ

- Responses ၏ တောင်းဆိုမှုအားလုံးတွင် `store: false` ကို သတ်မှတ်ပါ။
- ယခင် message ID များ သို့မဟုတ် server များတွင် သိမ်းဆည်းထားသော context များကို မူတည်စေမည် မဟုတ်ပါ။ စနစ်အခြေအနေကို client မှ ထိန်းသိမ်းပါ၊ metadata ကိုလည်း အနည်းငယ်သာ အသုံးပြုပါ။

---

## လက်ခံမည့် စံချိန်နှုန်းများ

### ကုဒ်အဆင့် ကြီးကြပ်မှု (အားလုံး ဖြတ်သန်းရမည်)

- [ ] `rg "chat\.completions\.create|ChatCompletion\.create|Completion\.create"` မရှိပါ။
- [ ] `rg "AzureOpenAI\(|AsyncAzureOpenAI\("` မရှိပါ — အားလုံး constructor များသည် `OpenAI`/`AsyncOpenAI` နှင့် v1 endpoint အသုံးပြုထားသည်။
- [ ] `rg "models\.github\.ai|models\.inference\.ai\.azure"` မရှိပါ — GitHub Models ကုဒ်လမ်းကြောင်း ဖယ်ရှားထားသည်။
- [ ] `rg "OpenAIChatCompletionClient"` မရှိပါ — MAF 1.0.0+ ကုဒ်သည် `OpenAIChatClient` (Responses API သုံး) ကို အသုံးပြုသည်။ 1.0.0 မရောက်ခင် version တွင် `agent-framework-openai>=1.0.0` သို့ အဆင့်မြှင့်ထားပါ။
- [ ] `ChatOpenAI(...)` အားလုံးတွင် `use_responses_api=True` ပါဝင်သည်။
- [ ] `rg "choices\[0\]"` မရှိပါ — ရလဒ်များအားလုံးသည် `resp.output_text` သို့မဟုတ် Responses output schema အသုံးပြုသည်။
- [ ] top level တွင် `response_format` မရှိရန်၊ အားလုံး structured output သည် `text={"format": {...}}` အသုံးပြုသည်။
- [ ] `openai>=1.108.1` နှင့် `azure-identity` ကို `requirements.txt` သို့မဟုတ် `pyproject.toml` တွင် ပါဝင်ပြီး dependency များ ပြန်တပ်ဆင်ထားသည်။
- [ ] `store=False` ကို `responses.create` အားလုံးတွင် သတ်မှတ်ထားသည်။
- [ ] client constructor တွင် `api_version` မပါရှိ၊ `AZURE_OPENAI_API_VERSION` ကို env ဖိုင်များနှင့် အခြား အခြေအနေများမှ ဖယ်ရှားပြီးဖြစ်သည်။

### စမ်းသပ်မှု တည်ဆောက်ရေး ကြီးကြပ်မှု (အားလုံး ဖြတ်သန်းရမည်)

- [ ] `rg "ChatCompletionChunk|AsyncCompletions\.create|chat\.completions" tests/` မရှိပါ။
- [ ] `rg "_azure_ad_token_provider" tests/` မရှိပါ — assertion များမှာ `isinstance(client, AsyncOpenAI)` သို့မဟုတ် `base_url` သဘောထား သပ်သပ်လျှောက်ထားပါ။
- [ ] `rg "prompt_filter_results|content_filter_results" tests/` မရှိပါ — Azure-specific filter mocks များ ဖယ်ရှားထားသည်။
- [ ] mock fixtures များတွင် `kwargs.get("input")` ကိုသာ အသုံးပြုသည်၊ `kwargs.get("messages")` မဟုတ်ပါ။
- [ ] snapshot / golden ဖိုင်များ ကို Responses streaming schema (no `choices[0]`, `function_call`, `logprobs`, etc.) ဖြင့် ပြင်ဆင်ထားသည်။
- [ ] `pytest` စမ်းသပ်မှု အောင်မြင်ပြီး ဘေးတွင် အမှားမရှိပါ။

### အပြုအမူ ကြီးကြပ်မှု (ကိုယ်တိုင် သို့မဟုတ် စမ်းသပ်မှု ဖွင့်ရန်)

- [ ] **အခြေခံ အကောင်အထည်ဖော်မှု**: non-streaming `responses.create` သည် ရလဒ် မအားလုံး မလွတ်ပါ။
- [ ] **Stream parity**: မူလကုဒ်တွင် streaming အသုံးပြုထားလျှင်၊ လှည့်ပြောင်းပြီးကုဒ်သည် stream လုပ်ပြီး non-empty ကွဲပြားချက် delta များ ဖြန့်ဝေသည်။
- [ ] **Structured output**: `text.format` နှင့် `json_schema` အသုံးပြုပြီး `json.loads(resp.output_text)` ဖြင့် အောင်မြင်စွာ ဖတ်ရှုနိုင်ပြီး schema နှင့် ကိုက်ညီသည်။
- [ ] **Tool-call loop**: tools များကိုအသုံးပြုပြီး၊ model သည် tool calls ထုတ်ပြန်သည်၊ အက်ပ် သည် ထိုအချက်များကို ဆောင်ရွက်ပြီး နောက်တောင်းဆိုမှုတွင် နောက်ဆုံး `output_text` ကို ပြန်လည်ထုတ်ပေးသည် (ကာကွယ်မဲ့ infinite loop မရှိ)။
- [ ] **Async parity**: `AsyncAzureOpenAI` ကိုအသုံးပြုပြီးလျှင် `AsyncOpenAI` နှင့် `await` ဖြင့် လုပ်ဆောင်နိုင်သည်။
- [ ] **Error rate**: လှည့်ပြောင်းမပြုမီ baseline နှင့် နှိုင်းယှဉ်၍ 400/401/404 error များ မပြန်လည်တက်ပါ။

### ပို့ဆောင်ရန် အရာများ

- ပြင်ဆင်ခဲ့သည့် ဖိုင်များ၊ legacy call site များ၏ အရေအတွက် မတူညီမှု (အရင်/နောက်) နှင့် နောက်ဆုံးအဆင့်များကို အကျဉ်းချုပ်ပါ။
- ပြောင်းလဲမှုများသည် working-tree edits အဖြစ်သာ (commit မလုပ်သေး) ဖြစ်သည်။

---

## SDK ဗားရှင်း လိုအပ်ချက်များ

| package | အနည်းဆုံး ဗားရှင်း |
|---------|----------------|
| `openai` | `>=1.108.1` |
| `azure-identity` | နောက်ဆုံးဗားရှင်း (EntraID auth အတွက်) |

---

## လမ်းညွှန်ချက်များ

- [Cheat Sheet — အားလုံးသော ကုဒ်အပိုင်းများ](./references/cheat-sheet.md)
- [Test Migration — mocks, snapshots, assertions](./references/test-migration.md)
- [Troubleshooting — မှားချက်များ, အန္တရာယ်ဇယား, ပေါ်တတ်သောပြဿနာများ](./references/troubleshooting.md)
- [detect_legacy.py — automated scanner](../../../../../.agents/skills/azure-openai-to-responses/scripts/detect_legacy.py)
- [Azure OpenAI Starter Kit](https://aka.ms/openai/start)
- [Azure OpenAI Responses API သောတ်တမ်းများ](https://learn.microsoft.com/en-us/azure/ai-foundry/openai/how-to/responses)
- [Azure OpenAI API ဗားရှင်း အသက်တာဇယား](https://learn.microsoft.com/en-us/azure/ai-foundry/openai/api-version-lifecycle?view=foundry-classic&tabs=python#api-evolution)
- [OpenAI Responses API ကိုးကားချက်](https://platform.openai.com/docs/api-reference/responses)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ပြောကြားချက်**
ဤစာတမ်းကို AI ဘာသာပြန်ဝန်ဆောင်မှု [Co-op Translator](https://github.com/Azure/co-op-translator) အသုံးပြု၍ ဘာသာပြန်ထားပါသည်။ ကျွန်ုပ်တို့သည် တိကျမှန်ကန်မှုအတွက် ကြိုးပမ်းနေသော်လည်း၊ စက်ကိရိယာဘာသာပြန်ခြင်းများတွင် အမှားများ သို့မဟုတ် မှားယွင်းချက်များ ပါဝင်နိုင်ကြောင်း သတိပြုပါရန် လိုအပ်ပါသည်။ မူလစာတမ်းကို မူရင်းဘာသာဖြင့်သာ ယုံကြည်စိတ်ချရသော အချက်အလက်အဖြစ် သတ်မှတ်သင့်သည်။ အရေးကြီးသည့် သတင်းအချက်အလက်များအတွက် ပရော်ဖက်ရှင်နယ် လူသားဘာသာပြန်သူဝန်ဆောင်မှုကို အကြံပြုပါသည်။ ဤဘာသာပြန်ချက်ကို အသုံးပြုခြင်းမှ ဖြစ်ပေါ်လာသော နားလည်မှုကွာခြားမှုများ သို့မဟုတ် မမှန်ကန်သော အသုံးပြုမှုများအတွက် ကျွန်ုပ်တို့ တာဝန်မခံပါ။
<!-- CO-OP TRANSLATOR DISCLAIMER END -->