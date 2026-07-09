---
name: azure-openai-to-responses
license: MIT
---
# Azure OpenAI Chat Completions မှ Responses API သို့ Python အက်ပ်များ ကို ရွှေ့ပြောင်းခြင်း

> **အတည်ပြုထားသော လမ်းညွှန်ချက်များ — တိတိကျကျ လိုက်နာပါ**
>
> ဒီစွမ်းရည်က Azure OpenAI Chat Completions ကို အသုံးပြုနေသော Python ကုဒ်များကို
> တစ်ခုတည်းသော Responses API သို့ ရွှေ့ပြောင်းပေးပါသည်။ ဤညွှန်ကြားချက်များကို တိတိကျကျ လိုက်နာပါ။
> parameter mapping များကို တိုက်ရိုက်ထပ်တိုးခြင်း သို့မဟုတ် API ပုံစံ အသစ်ဖန်တီးခြင်း မပြုပါနှင့်။

---

## လှုံ့ thúcမှုများ

အသုံးပြုသူသည် အောက်ပါအရာများ လုပ်လိုသောအချိန်တွင် ဒီစွမ်းရည်ကို ဖွင့်ပါ။
- Azure OpenAI Chat Completions မှ Responses API သို့ Python app တစ်ခုကို ရွှေ့ပြောင်းလိုသည်။
- Azure OpenAI အဆင့်အတန်းသို့ Python OpenAI SDK အသုံးပြုမှုကို နောက်ဆုံး API ပုံစံသို့ အဆင့်မြှင့်လိုသည်။
- Azure မှ Responses လိုအပ်သည့် GPT-5 သို့မဟုတ် အသစ်တိုးမြှင့်ထားသော မော်ဒယ်များအတွက် Python ကုဒ်ကို ပြင်ဆင်လိုသည်။
- `AzureOpenAI`/`AsyncAzureOpenAI` မှ စံသတ် OpenAI/AsyncOpenAI ဖောက်သည်နှင့် v1 endpoint သို့ ပြောင်းလိုခြင်း။
- `AzureOpenAI` constructor များ သို့မဟုတ် `api_version` နှင့်ဆက်စပ်သော ရှေးကွယ်ခြင်း သတိပေးချက်များကို ပြင်ဆင်လိုသည်။

---

## ⚠️ မော်ဒယ် ကိုက်ညီမှု — ပထမဦးဆုံး စစ်ဆေးပါ

> **ရွှေ့ပြောင်းမပြုလုပ်ခင် သင့် Azure OpenAI တပ်ဆင်မှုသည် Responses API ကို ထောက်ပံ့မှုရှိကြောင်း အတည်ပြုပါ။**

### 1. သင့်တပ်ဆင်မှုကို Smoke-test လုပ်ပါ (အမြန်ဆုံး)

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

> **မှတ်ချက်**: `max_output_tokens` သည် Azure OpenAI တွင် **အနည်းဆုံး 16** ရှိရမည်။ 16 အောက် တန်ဖိုးများ သည် 400 အမှား ပြန်လည်ပေးသွားသည်။ Smoke test များအတွက် 50+ ကို အသုံးပြုပါ။

၎င်းသည် 404 ပြန်လာပါက၊ အဆိုပါတပ်ဆင်မှု၏ မော်ဒယ်သည် Responses ကို ထောက်ပံ့မှု မရှိသေးပါ — အောက်တွင် ရှုမြင်ချက်စစ်ဆေးရန် သို့မဟုတ် ထောက်ပံ့သော မော်ဒယ်နဲ့ ပြန်တပ်ဆင်ပါ။

### 2. သင့်ဒေသရှိ မော်ဒယ်များကို စစ်ဆေးပါ (အကြံပြုသည်)

သင့်ဒေသအထူးသဖြင့် Responses API ထောက်ပံ့မှုရှိမိုင် မော်ဒယ်များကို ကြည့်ရန် အချုပ်စည်းစနစ် အမြဲရှိသော မော်ဒယ် ကိုက်ညီမှုကိရိယာကို စစ်ဆေးပါ။

```bash
python migrate.py models --subscription YOUR_SUB_ID --location YOUR_REGION
```

ဤကိရိယာသည် Azure ARM ကို တိုက်ရိုက် တောင်းဆိုပြီး မော်ဒယ်များသည် Responses၊ ဖွဲ့စည်းတည်ဆောက် output၊ ကိရိယာများ စသဖြင့် မဘာသာ ရှိကြောင်းကို ပြသသည် — `--filter gpt-5.1,gpt-5.2` ဖြင့် ရလဒ်များကို ကန့်သတ်နိုင်သည် သို့မဟုတ် စာတိုက် ရေးသားမှုအတွက် `--json` အသုံးပြုနိုင်သည်။

### 3. မော်ဒယ်များ၏ အပြည့်အစုံ ထောက်ပံ့မှု ရှုမြင်ချက်

- **တိုက်ရိုက် တောင်းဆိုမှု**: `python migrate.py models` (အထက်ဖော်ပြထားသည် — ဒေသအလိုက် အမြဲအသစ်)
- **ရနိုင်မှု ကြည့်ရန်**: [Model summary table and region availability](https://learn.microsoft.com/en-us/azure/foundry/foundry-models/concepts/models-sold-directly-by-azure?tabs=global-standard-aoai%2Cglobal-standard&pivots=azure-openai#model-summary-table-and-region-availability)
- **Quickstart နှင့် လမ်းညွှန်ချက်**: **https://aka.ms/openai/start**

### ⚠️ အဟောင်း မော်ဒယ် သတ်မှတ်ချက်များ

> **သတိပေးချက်**: အဟောင်း မော်ဒယ်များ (ဥပမာ `gpt-4o`, `gpt-4`) သည် Responses API ၏ လုံလောက်စွာသော လုပ်ဆောင်ချက်များအားလုံး မထောက်ပံ့နိုင်ပါ။
>
> အဟောင်း မော်ဒယ်များနှင့် တွေ့ရှိခဲ့သော ကန့်သတ်ချက်များ:
> - **`reasoning` parameter**: `gpt-4o-mini`, `gpt-4o` နှင့် reasoning မပါသော မော်ဒယ်များတွင် မထောက်ပံ့ပါ။ မူရင်းကုဒ်တွင် ရှိပြီးသားမျှသာ reasoning ကို ရွှေ့ပြောင်းပါ။
> - **`seed` parameter**: Responses API တွင် မထောက်ပံ့သေးသည် — အားလုံးမှ ဖယ်ရှားပါ။
> - **`text.format` ဖြင့် ဖွဲ့စည်းထားသော output**: အဟောင်း မော်ဒယ်များသည် `strict: true` JSON schema များကို မကြာခဏ စစ်ဆေးပေးခြင်း မရှိပါ။
> - **Tool ထိန်းချုပ်မှု**: GPT-5+ သည် internal reasoning ၏ အစိတ်အပိုင်းအဖြစ် tool ဖုန်းခေါ်မှုများ ကို စီမံခန့်ခွဲသည်။ Responses အပေါ် အဟောင်း မော်ဒယ်များ အလုပ်လုပ်သော်လည်း အဓိက ဆက်လက်မပေါင်းစည်းမှုရှိပါသည်။
> - **ထိပ်တန်းအပူချိန် သတ်မှတ်ချက်များ**: `gpt-5` သို့ ရွှေ့ပြောင်းတဲ့အခါ temperature ကို ဖယ်ရှားပါ သို့မဟုတ် `1` သို့ သတ်မှတ်ပါ။ အဟောင်း မော်ဒယ်များတွင် ဤကန့်သတ်ချက် မရှိပါ။

### O-series reasoning မော်ဒယ်များ (o1, o3-mini, o3, o4-mini)

O-series မော်ဒယ်များတွင် အထူး parameter ကန့်သတ်ချက်များ ရှိသည်။ O-series မော်ဒယ်များ အခြေခံထားပြီး app များကို ရွှေ့ပြောင်းသောအခါ:

- **`temperature`**: `1` ဖြစ်ရမည် (သို့မဟုတ် ဖယ်ရှားရမည်)။ O-series မော်ဒယ်များသည် အခြားတန်ဖိုးများကို လက်ခံမရပါ။
- **`max_completion_tokens` → `max_output_tokens`**: Azure ထူးခြားသော `max_completion_tokens` ကို အသုံးပြုသော app များသည် `max_output_tokens` သို့ ပြောင်းရန် လိုအပ်သည်။ အမြင့်တန်ဖိုးများ (4096+) သတ်မှတ်ပါ၊ reasoning token များသည် ကန့်သတ်ချက်ထဲ မှ ထည့်သွင်းတွက်ချက်ပါသည်။
- **`reasoning_effort`**: app သည် `reasoning_effort` (low/medium/high) ကို အသုံးပြုပါက တာဝန်ခံပါ — Responses API သည် o-series မော်ဒယ်များအတွက် ဤ parameter ကို ထောက်ပံ့သည်။
- **Streaming လုပ်ဆောင်မှု**: O-series မော်ဒယ်များသည် reasoning ပြီးဆုံးသည်အထိ output ကို buffer ထားသည်။ Streaming အလုပ်လည်း မြန်ဆန်သော်လည်း ပထမဆုံး `response.output_text.delta`သည် GPT မော်ဒယ်များထက် ပိုကြာမြင့်စွာ ရောက်ရှိနိုင်သည်။
- **`top_p`**: O-series အတွက် အထောက်အပံ့ မရှိပါ — ရှိလျှင် ဖယ်ရှားပါ။
- **Tool အသုံးပြုမှု**: O-series မော်ဒယ်များသည် GPT မော်ဒယ်အသုံးပြုသည့် Responses API ကဲ့သို့ ကိရိယာများကို ထောက်ပံ့သည်၊ သို့သော် tool ခေါ်ဆိုမှု စီမံခန့်ခွဲမှုအရည်အသွေး မော်ဒယ်အလိုက် ကွဲပြားပါသည်။

**လုပ်ဆောင်မှု — မော်ဒယ် အကြံပြုချက်အဖွင့်**: စကင်လုပ်ရာတွင် app သည် မည်သည့် မော်ဒယ်ကို ရည်ညွှန်းသည်ကို စစ်ဆေးပါ (deployment အမည်များ၊ ပတ်ဝန်းကျင် အလိုက် အမျိုးအစားများ၊ config)။ မော်ဒယ်သည် `gpt-4o` သို့မဟုတ် အဟောင်း (gpt-4.1+ မဟုတ်) ဖြစ်ပါက အသုံးပြုသူ ကို အကြံပြုသောစာပို့ပါ။
- ပထမဦးစွာ ရှိနေသော မော်ဒယ်တွင် မူရင်း စာသား၊ chat, streaming နှင့် ကိရိယာ အသုံးပြုမှုများအတွက် ရွေ့ပြောင်းခြင်း အလုပ်လုပ်မည်။
- အသစ်တိုးမြှင့်ထားသော မော်ဒယ်များ (`gpt-5.1`, `gpt-5.2`) သည် ကိရိယာ ခေါ်ဆိုမှု စီမံခန့်ခွဲမှု ပိုမိုကောင်းမွန်မှု၊ ဖွဲ့စည်းတည်ဆောက် output ပေါ်လစီထားခြင်း၊ reasoning နှင့် ဒေသတစွာ ရရှိနိုင်မှုများ ပေးစွမ်းသည်။
- အသင့်ရှိသည့်အချိန်တွင် deployment ကို တိုးတက်စေရန် စဉ်းစားသင့်သည် — သို့သော် ရွှေ့ပြောင်းမှုတချို့ မပိတ်ပင်ပါ။

မော်ဒယ် ဗားရှင်းအရ ရွှေ့ပြောင်းရမှ မရမှ အကန့်အသတ် မထားပါနှင့်။ အကြံပြုချက်သာ ဖြစ်သည်။

### GitHub Models သည် Responses API မထောက်ပံ့ပါ

> **GitHub Models (`models.github.ai`, `models.inference.ai.azure.com`) သည် Responses API ကို ထောက်ပံ့မှု မရှိပါ။**

ကုဒ်ဘေ့စ်တွင် GitHub Models ကိုယ်ပိုင် လမ်းကြောင်း (path) များရှိပါက (`base_url` သည် `models.github.ai` သို့မဟုတ် `models.inference.ai.azure.com` ကို ဦးတည်ခြင်းရှာဖွေပါ)၊ **ရွှေ့ပြောင်းမှုအတွင်း ပြီးပြည့်စုံ ဖယ်ရှားပါ**။ Responses API သည် Azure OpenAI, OpenAI သို့မဟုတ် Ollama ကဲ့သို့ compatible local endpoint တစ်ခုကို တောင်းဆိုပါသည်။

စကင်လုပ်စဉ် လုပ်ဆောင်ချက်များ:
- GitHub Models လမ်းကြောင်းများအား ဖယ်ရှားရန် အမှတ်အသား ပြုပါ။

---

## Framework ရွှေ့ပြောင်းခြင်း

အက်ပ်များစွာသည် OpenAI အပေါ်၌ မြင့်မားသော အဆင့် Framework များကို အသုံးပြုသည်။ ဤ Framework များ ရွှေ့ပြောင်းခြင်းသည် မူရင်း OpenAI ခေါ်ဆိုမှုများသာမက Framework အမှုဆောင် API များတွင်ပါ ပါဝင်သည်။

### Microsoft Agent Framework (MAF)

**သင့် MAF ဗားရှင်းကို ပထမဦးဆုံး စစ်ဆေးပါ** — ရွှေ့ပြောင်းခြင်းသည် သင့်သည် MAF 1.0.0+ သို့မဟုတ် pre-1.0.0 beta/rc ပေါ် မူတည်ပါသည်။

#### MAF 1.0.0+ (agent-framework-openai >= 1.0.0)

`OpenAIChatClient` **ပြီးသား Responses API ကို အသုံးပြုသည်** — ရွှေ့ပြောင်းတစ်စုံတစ်ရာ မလိုအပ်ပါ။ တကယ်လျှင် legacy `OpenAIChatCompletionClient` (`chat.completions.create` ကို သုံးသည့်)ကို သုံးနေပါက `OpenAIChatClient` ဖြင့် အစားထိုးပါ။

| မတိုင်မီ | ပြီးနောက် |
|--------|-------|
| `from agent_framework.openai import OpenAIChatCompletionClient` | `from agent_framework.openai import OpenAIChatClient` |
| `OpenAIChatCompletionClient(...)` | `OpenAIChatClient(...)` |

သင့်ဗားရှင်းကို စစ်ဆေးရန် - `python -c "import agent_framework_openai; print(agent_framework_openai.__version__)"` ကို အသုံးပြုပါ။

#### MAF pre-1.0.0 (beta/rc releases)

pre-1.0.0 MAF တွင် `OpenAIChatClient` သည် Chat Completions ကို အသုံးပြုသည်။ `agent-framework-openai>=1.0.0` သို့ အဆင့်မြှင့်၍ `OpenAIChatClient` သည် Responses API ကို default အဖြစ် အသုံးပြုသည်။

အခြား ပြင်ဆင်မှု မလိုအပ်ပါ — `Agent` နှင့် ကိရိယာ API များသည် သူ့အတိုင်း ဖြစ်နေပါသည်။

### LangChain (`langchain-openai`)

`ChatOpenAI()` တွင် `use_responses_api=True` ကို ထည့်သွင်းပါ။ ပြန်လည်ရရှိမှုကို `.content` မှ `.text` သို့ ပြောင်းပါ။

| မတိုင်မီ | ပြီးနောက် |
|--------|-------|
| `ChatOpenAI(model=..., base_url=..., api_key=...)` | `ChatOpenAI(model=..., base_url=..., api_key=..., use_responses_api=True)` |
| `result['messages'][-1].content` | `result['messages'][-1].text` |

အပြည့်အစုံ မူလနှင့် ပြောင်းလဲပြီးသော ကုဒ် နမူနာများအတွက် [cheat-sheet.md](./references/cheat-sheet.md) ကို ကြည့်ပါ။

---

## Frontend ရွှေ့ပြောင်းခြင်း လမ်းညွှန်ချက်

> **Responses API သည် server-side ဆိုင်ရာဖြစ်သည်။** သင့် Python backend ကို ရွှေ့ပြောင်းပါ; frontend ၏ HTTP သဘောတူစာချုပ်ကို ပြောင်းလဲရန် မလိုအပ်ပါ (backend သာ တိကျသော pass-through ဖြစ်ပါက Response request shape ကို အသုံးပြုရန် စဉ်းစားပါ)။ frontend ကျွန်ုပ် OpenAI ကို client-side key ဖြင့် တိုက်ရိုက် ခေါ်ဆိုပါက calling များကို ပထမဦးဆုံး backend သို့ ပြောင်းရွှေ့ပါ။

### `@microsoft/ai-chat-protocol` package ရှိ ပျက်ကွက်မှု

`@microsoft/ai-chat-protocol` npm package ကို ရှင်းလင်းပြီး [`ndjson-readablestream`](https://www.npmjs.com/package/ndjson-readablestream) ဖြင့် အစားထိုးသင့်သည်။ သင့် frontend တွင် တွေ့ပါက-

1. CDN script tag ကို အစားထိုးပါ။
   ```html
   <!-- Before -->
   <script src="https://cdn.jsdelivr.net/npm/@microsoft/ai-chat-protocol@.../dist/iife/index.js"></script>
   <!-- After -->
   <script src="https://cdn.jsdelivr.net/npm/ndjson-readablestream@1.0.7/dist/ndjson-readablestream.umd.js"></script>
   ```
2. `AIChatProtocolClient` အများသုံး အဓိက `new ChatProtocol.AIChatProtocolClient("/chat")` ကို ဖယ်ရှားပါ။
3. `client.getStreamedCompletion(messages)` ကို backend streaming endpoint သို့ တိုက်ရိုက် `fetch()` ခေါ်သို့ ပြောင်းပါ။
4. `for await (const response of result)` ကို `for await (const chunk of readNDJSONStream(response.body))` သို့ ပြောင်းပါ။
5. `response.delta.content` / `response.error` ကို `chunk.delta.content` / `chunk.error` သို့ update ပြုလုပ်ပါ။

---

## ရည်မှန်းချက်များ

- Azure OpenAI ကို တိုက်ရိုက် အသုံးပြုသည့် Python call site များအားလုံး အသေးစိတ် စာရင်းပြုစုပါ။
- Python ကုဒ်ဘေ့စ်အတွက် ရွှေ့ပြောင်းရေး စီမံချက်နှင့် အဆင့်တန်းကို အကြံပြုပါ။
- Responses API သို့ ပြောင်းရွှေ့ရာတွင် အန္တရာယ်ကင်းပြီး အနည်းဆုံးပြင်ဆင်ချက်များသာ ဆောင်ရွက်ပါ။
- Responses output schema ကို အသုံးပြုအောင် caller များ ပြင်ဆင်ပါ; backward compatibility wrappers မလိုအပ်ပါ။
- စမ်းသပ်ခြင်း / lint ပေါင်းစပ်ပြီး ရိုးရှင်းသော ပြဿနာများကို ပြင်ဆင်ပါ။
- Review လုပ်လွယ်သော ပြင်ဆင်မှုအသေးစား ပေါင်းစပ်ပြီး နောက်ဆုံး सारအစ ချုပ်ပါတိ်းသည်းအပြည့်အစုံ လာပါတယ် (commit မလုပ်ပါနှင့်)။

---

## ကာကွယ်ခြင်းများ

- git workspace အတွင်းရှိ ဖိုင်များကိုသာ ပြင်ဆင်ပါ။ အပြင်မှာ မရေးပါနှင့်။
- backward compatibility shims မထိန်းသိမ်းပါနှင့်; ကုဒ်ကို API ပုံစံအသစ်သို့ ရွှေ့ပြောင်းပါ။
- tombstone/transition မှတ်ချက်များ သို့မဟုတ် backup ဖိုင်များ မတွယ်ကျန်ပါနှင့်။
- ရှိနေပါက streaming semantics ကို ထိန်းသိမ်းပါ; မရှိပါက non-streaming ကို အသုံးပြုပါ။
- approval mode တွင် command များ သို့မဟုတ် network ခေါ်ဆိုမှု မလုပ်မီ အတည်ပြုချက် တောင်းပါ။
- `git add`/`git commit`/`git push` မလုပ်ပါနှင့်; working-tree ပြင်ဆင်မှုများသာ ထုတ်လုပ်ပါ။

---

## အဆင့် 0: Azure OpenAI Client ရွှေ့ပြောင်းခြင်း (လိုအပ်ချက်)

ကုဒ်ဘေ့စ်တွင် `AzureOpenAI` သို့မဟုတ် `AsyncAzureOpenAI` constructor များ အသုံးပြုပါက စတင်၍ စံပြ `OpenAI` / `AsyncOpenAI` ကို အသုံးပြု ရွှေ့ပြောင်းပါ။ Azure ထူးခြား constructor များသည် `openai>=1.108.1` တွင် ရှေးကွယ်သွားပါပြီ။

### v1 API လမ်းကြောင်းရဲ့ အကြောင်းရင်း

အသစ် `/openai/v1` endpoint သည် `AzureOpenAI()` မဟုတ်ဘဲ စံပြ `OpenAI()` client ကို သုံးပြီး `api_version` parameter မလိုအပ်ဘဲ OpenAI နှင့် Azure OpenAI တို့တွင် တူညီစွာ အလုပ်လုပ်သည်။ ၎င်း client ကုဒ်သည် အနာဂတ်ခံနိုင်ပြီး ဗားရှင်းစီမံမှု မလိုအပ်ပါ။

### အဓိက ပြောင်းလဲမှုများ

| မတိုင်မီ | ပြီးနောက် |
|--------|-------|
| `AzureOpenAI` | `OpenAI` |
| `AsyncAzureOpenAI` | `AsyncOpenAI` |
| `azure_endpoint` | `base_url` |
| `azure_ad_token_provider` | `api_key` |
| `api_version=...` | အပြည့်စုံ ဖယ်ရှားပါ |

### စစ်ဆေးရန်စာရင်း

- client ဖန်တီးရာတွင် `api_version` argument ကို ဖယ်ရှားပါ။
- `.env`, app settings, Bicep/infra ဖိုင်များမှ `AZURE_OPENAI_VERSION` / `AZURE_OPENAI_API_VERSION` ပတ်ဝန်းကျင် အပြောင်းအလဲ မရှိစေရန် ဖယ်ရှားပါ။
- `.env`, app settings, Bicep/infra နှင့် စမ်းသပ်မှု ဖိုင်များတွင် `AZURE_OPENAI_CLIENT_ID` ကို `AZURE_CLIENT_ID` သို့ အမည်ပြောင်းပါ (standard Azure Identity SDK သဘောထားအတိုင်း)။
- `requirements.txt` သို့မဟုတ် `pyproject.toml` တွင် `openai>=1.108.1` ရှိခြင်း အာမခံပါ။

### ပတ်ဝန်းကျင် အပြောင်းအလဲများ

| အဟောင်း env var | လုပ်ဆောင်ချက် | မှတ်ချက် |
|-------------|--------|-------|
| `AZURE_OPENAI_VERSION` | **ဖယ်ရှားပါ** | v1 endpoint တွင် `api_version` မလိုအပ်ပါ |
| `AZURE_OPENAI_API_VERSION` | **ဖယ်ရှားပါ** | အထက်ပါလိုပဲ |
| `AZURE_OPENAI_CLIENT_ID` | **အမည်ပြောင်းပါ** → `AZURE_CLIENT_ID` | `ManagedIdentityCredential(client_id=...)`  အတွက် စံ Azure Identity SDK convention |
| `AZURE_OPENAI_ENDPOINT` | **ထိန်းသိမ်းပါ** | `base_url` ဖန်တီးရာတွင် လိုအပ်သေးသည် |
| `AZURE_OPENAI_CHAT_DEPLOYMENT` | **ထိန်းသိမ်းပါ** | `responses.create` ပြည့်စုံမှုအတွက် `model` parameter အဖြစ် အသုံးပြုသည် |
| `AZURE_OPENAI_API_KEY` | **ထိန်းသိမ်းပါ** | key-based အတည်ပြုမှုအတွက် `api_key` ထားရှိသည် |

client setup အတွက် နမူနာကုဒ်များ (sync, async, EntraID, API key, multi-tenant) အတွက် [cheat-sheet.md](./references/cheat-sheet.md) ကို ကြည့်ပါ။

---

## အဆင့် 1: Legacy Call Sites ရှာဖွေခြင်း

ရွှေ့ပြောင်းရန် လိုအပ်သော call site များအားလုံး ကို တွေ့ရှိရန် [detect_legacy.py](../../../../../.agents/skills/azure-openai-to-responses/scripts/detect_legacy.py) script ကို ပြေးပါ။

```bash
python skills/azure-openai-to-responses/scripts/detect_legacy.py .
```

သို့မဟုတ် manual search များ ပြုလုပ်ပါ — မတူညီသော အစိတ်အပိုင်းတိုင်းသည် ရွှေ့ပြောင်းရန် ရည်ရွယ်ချက် ဖြစ်သည်။

```bash
# အတိတ် API ခေါ်ဆိုမှုများ (ပြန်ရေးရန်လိုအပ်သည်)
rg "chat\.completions\.create"
rg "ChatCompletion\.create"
rg "Completion\.create"

# ရုပ်သိမ်းပြီးသော Azure client အဆောက်အစည်းများ (အစားထိုးရန်လိုအပ်သည်)
rg "AzureOpenAI\("
rg "AsyncAzureOpenAI\("

# တုံ့ပြန်မှုပုံစံဝင်ရိုးလမ်းညွှန်များ (တိုးတက်စေရန်လိုအပ်သည်)
rg "choices\[0\]\.message\.content"
rg "choices\[0\]\.delta\.content"
rg "choices\[0\]\.message\.function_call"
rg "choices\[0\]\.message\.tool_calls"

# ဟောင်းနှင့်အတွင်းစပ်ဖော်ပြချက်ဖြစ်သောကိရိယာသတ်မှတ်ချက်များ (ပြေးဆွဲပုံသဏ္ဍာန်ပြောင်းရန်)
rg '"function":\s*{\s*"name"'
rg "pydantic_function_tool"

# ဟောင်းနည်းဖြင့်ဖြေရှင်းချက်များ (function_call_output သို့ပြောင်းရန်)
rg '"role":\s*"tool"'
rg '"tool_call_id"'

# ရုပ်သိမ်းပြီးသောပါရာမီတာများ (ဖယ်ရှားရန် သို့မဟုတ် နာမည်ပြောင်းရန်)
rg "response_format"
rg "max_tokens\b"        # max_output_tokens သို့နာမည်ပြောင်းရန်
rg "['\"]seed['\"]"      # remove entirely

# ရုပ်သိမ်းပြီးသောပတ်ဝန်းကျင်အပြောင်းအလဲများ (သန့်ရှင်းရေး)
rg "AZURE_OPENAI_API_VERSION|AZURE_OPENAI_VERSION"
rg "AZURE_OPENAI_CLIENT_ID"  # AZURE_CLIENT_ID ဖြစ်သင့်သည်

# GitHub မော်ဒယ် endpoint များ (ဖယ်ရှားရန် — Responses API ကိုမထောက်ပံ့)
rg "models\.github\.ai|models\.inference\.ai\.azure"

# အခြေခံဘက် legacy ပုံစံများ (တိုးတက်စေရန်)
rg "OpenAIChatCompletionClient"  # MAF 1.0.0+ : OpenAIChatClient ဖြင့်အစားထိုးပါ
rg "ChatOpenAI\(" | grep -v "use_responses_api"  # LangChain : use_responses_api=True လိုအပ်သည်

# စမ်းသပ်နည်းပညာပစ္စည်း (တိုးတက်စေရန်)
rg "ChatCompletionChunk|AsyncCompletions\.create" tests/
rg "_azure_ad_token_provider" tests/
rg "prompt_filter_results|content_filter_results" tests/
rg "choices\[0\]" tests/

# အကြောင်းအရာစစ်ထုတ်မှုအမှားခန္ဓာကိုယ်ဝင်ရိုး (တိုးတက်စေရန် — ဖွဲ့စည်းမှုပြောင်းလဲပြီ)
rg 'innererror.*content_filter_result|error\.body\["innererror"\]'
rg "content_filter_result\[" # ဟောင်း singular ပုံစံ — ယခု content_filters အတွင်းရှိ content_filter_results (နာမ်ပေါင်း)

# Chat Completions endpoint သို့ လတ်တလော HTTP ခေါ်ဆိုမှုများ (URL ကိုတိုးတက်စေရန်)
rg "/openai/deployments/.*/chat/completions"
rg "api-version="
```

### heuristic များ (ရှာဖွေနှင့် ပြန်လည်ရေးသားမှု)

- **Chat Completions client**: `client.chat.completions.create` → `client.responses.create(...)`။

- **Azure client constructors**: `AzureOpenAI(...)` → `OpenAI(base_url=..., api_key=...)`။
- **Tools**: function-calling tool သတ်မှတ်ချက်များကို nested ဖော်မတ် (`{"type": "function", "function": {"name": ...}}`) မှ flat Responses ဖော်မတ် (`{"type": "function", "name": ...}`) သို့ပြောင်းလဲပါ။ `tool_choice` ကိုအသုံးပြုပါ။ tool ရလဒ်များကို `{"type": "function_call_output", "call_id": ..., "output": ...}` အဖြစ် return ပြန်ပေးပါ ( `{"role": "tool", ...}` မဟုတ်ပါ)။
- **Tool round-trips**: မော်ဒယ်မှ function calls ကိုပြန်လာသောအခါ `response.output` items များကို ဆက်သွယ်မှုထဲထည့်ပါ (manual `{"role": "assistant", "tool_calls": [...]}` dict မဟုတ်ပါ)၊ နောက်မှ result တစ်ခုစီအတွက် `function_call_output` items များကိုထည့်ပါ။
- **Few-shot tool examples**: ဆက်သွယ်မှုတွင် hardcoded tool call အကြောင်းအရာများပါရှိလျှင်၊ `{"type": "function_call", "id": "fc_...", "call_id": "fc_...", ...}` + `{"type": "function_call_output", ...}` items အဖြစ်ပြောင်းပါ။ IDs များသည် `fc_` ဖြင့်စတင်ရမည်။
- **`pydantic_function_tool()`**: ဒီ helper သည်ဟောင်းသော nested ဖော်မတ်ကို generate လုပ်ပြီး `responses.create()` နှင့် **သဟဇာတမရှိပါ**။ ဝင်ရောက်အသုံးပြုရာတွင် manual tool သတ်မှတ်ချက်များ သို့မဟုတ် flattening wrapper ကိုအသုံးပြုပါ။
- **Multi-turn**: ဆက်သွယ်မှုမှတ်တမ်းကို app တွင်ထိန်းသိမ်းပါ။ ယခင် turn များကို `input` items မှတဆင့် ပေးပို့ပါ။
- **Formatting**: Chat ၏အထက်ဆုံးအဆင့် `response_format` ကို Responses မှာ `text.format` ဖြင့်အစားထိုးပါ။ တိကျသည့်ပုံစံမှာ `text={"format": {"type": "json_schema", "name": "Output", "strict": True, "schema": {...}}}` ဖြစ်သည်။
- **Content items**: Chat ထဲရှိ `content[].type: "text"` ကို Responses ၏ `content[].type: "input_text"` အဖြစ်လဲပါ။
- **Image content items**: Chat ထဲရှိ `content[].type: "image_url"` ကို Responses ၏ `content[].type: "input_image"` အဖြစ်ပြောင်းပါ။ `image_url` လဲ nested object `{"url": "..."}` မှာ flat string ျဖစ္သွားပါသည်။ ရှေ့နောက်နမူနာများအတွက် cheat sheet ကိုကြည့်ပါ။
- **Reasoning effort**: မူလကုဒ်တွင် ရှိပြီးသားဖြစ်လျှင်သာ `reasoning` ကို ပြောင်းရွှေ့ပါ။
- **Content filter error handling**: error body ဖွဲ့စည်းမှုပြောင်းလဲသည်။ Chat Completions သည် `error.body["innererror"]["content_filter_result"]` (တစ်ခုရဲ့) ကို သုံးခဲ့ပြီး Responses API သည် `error.body["content_filters"][0]["content_filter_results"]` (array အတွင်း ဖော်ပြချက်များ) ကိုအသုံးပြုသည်။ `innererror` ကိုအသုံးပြုသော code များသည် `KeyError` ဖြစ်စေမည်။ အသစ်သောလမ်းကြောင်းကို အသုံးပြုရန် ပြင်ဆင်ပါ။
- **Raw HTTP calls**: app သည် Azure OpenAI REST API ကိုတိုက်ရိုက်ခေါ်ယူသောအခါ (requests, httpx တို့မှတဆင့်) `/openai/deployments/{name}/chat/completions?api-version=...` မှ `/openai/v1/responses` သို့ ပြောင်းလဲပါ။ request body မှာ `messages` → `input` ဖြစ်သည်၊ `max_output_tokens` နှင့် `store: false` ကိုထည့်ပါ၊ `api-version` query param ကိုဖယ်ရှားပါ။ response body ကို `choices[0].message.content` မှ `output[0].content[0].text` သို့ပြောင်းပါ (မှတ်ချက်: `output_text` သည် SDK ၏အဆင်ပြေရေး property ဖြစ်ပြီး raw REST JSON တွင်မရှိပါ)။

---

## အဆင့် ၂: ပျက်ကွက်မှုမှအလွယ်တကူ ပြောင်းရွှေ့ခြင်း

### ပျက်ကွက်မှုမှတ်စုများ (Chat Completions → Responses)

- **ဘာကြောင့် ပြောင်းလဲရသလဲ**: Responses သည် စာသား၊ tools နှင့် streaming များအတွက် ပေါင်းစပ်တစ်ခု API ဖြစ်သည်။ Chat Completions သည် အဟောင်းဖြစ်သည်။ GPT-5 နှင့်အတူ Responses သည် အကောင်းဆုံး လည်ပတ်မှုအတွက် လိုအပ်သည်။
- **HTTP**: Azure endpoint ကို `/openai/deployments/{name}/chat/completions` မှ `/openai/v1/responses` သို့ပြောင်းသည်။
- **Fields**: `messages` → `input`၊ `max_tokens` → `max_output_tokens` ဖြစ်သည်။ `temperature` သည် မပြောင်းလဲပါ။
- **Formatting**: `response_format` ကို အမှန်တကယ် object ဖြင့် `text.format` သို့ပြောင်းပါ။
- **Content items**: Chat ၏ `content[].type: "text"` ကို Responses ၏ `content[].type: "input_text"` ဖြင့်အစားထိုးပါ။
- **Image content items**: Chat ၏ `content[].type: "image_url"` ကို Responses ၏ `content[].type: "input_image"` ဖြင့် အစားထိုးပါ။ `image_url` ကို `{"image_url": {"url": "..."}}` မှ `{"image_url": "..."}` သို့ (string သာ) flatten ပြောင်းပါ (HTTPS URL သို့မဟုတ် `data:image/...;base64,...` data URI ဖြစ်နိုင်သည်)။

### ပါရာမီတာ များပြောင်းလဲရက်

| Chat Completions | Responses API |
|-----------------|---------------|
| `prompt` | `input` |
| `messages` | `input` (array of items) |
| `max_tokens` | `max_output_tokens` |
| `response_format` | `text.format` (object) |
| `temperature` | `temperature` (မပြောင်းလဲ) |
| `stop` | `stop` (မပြောင်းလဲ) |
| `frequency_penalty` | `frequency_penalty` (မပြောင်းလဲ) |
| `presence_penalty` | `presence_penalty` (မပြောင်းလဲ) |
| `tools` / function-calling | `tools` (မပြောင်းလဲ) |
| `seed` | **ဖယ်ရှားရန်** (မထောက်ခံ) |
| `store` | `store` (false သတ်မှတ်ထား) |
| `content[].type: "text"` | `content[].type: "input_text"` |
| `content[].type: "image_url"` | `content[].type: "input_image"` |
| `"image_url": {"url": "..."}` | `"image_url": "..."` (flat string) |

ပြည့်စုံသော ရှေ့နောက် ကိုးကားနမူနာများအတွက် [cheat-sheet.md](./references/cheat-sheet.md) ကိုကြည့်ပါ။

စမ်းသပ်မှု အဆောက်အအုံ ပျက်ကွက်မှု (mock, snapshot, assertion) အတွက် [test-migration.md](./references/test-migration.md) ကိုကြည့်ပါ။

အဆင်မပြေတာများနှင့် ရှောင်ရှားရန်အချက်များအတွက် [troubleshooting.md](./references/troubleshooting.md) ကိုကြည့်ပါ။

---

## ဒေတာသိမ်းဆည်းမှုနှင့် အခြေအနေ

- Responses ၏ request များအားလုံးတွင် `store: false` သတ်မှတ်ထားပါ။
- ယခင် message ID များသို့မဟုတ် server ထိန်းသိမ်းထားသည့် context များအား မယုံကြည်ပါနှင့်။ state ကို client-Managed ဖြစ်အောင် ထိန်းသိမ်းပြီး metadata ကို လျော့ပါ။

---

## လက်ခံရန် ရည်မှန်းချက်များ

### ကုဒ်-အဆင့် ဂိတ်များ (အားလုံးဖြတ်သန်းရမည်)

- [ ] ပြောင်းလဲပြီးဖိုင်များတွင် `rg "chat\.completions\.create|ChatCompletion\.create|Completion\.create"` မရှိရ။
- [ ] `rg "AzureOpenAI\(|AsyncAzureOpenAI\("` ကိုမတွေ့ရ၊ constructors များအားလုံးသည် `OpenAI`/`AsyncOpenAI` ကို v1 endpoint နှင့်အသုံးပြုထားရမည်။
- [ ] `rg "models\.github\.ai|models\.inference\.ai\.azure"` မတွေ့ရ၊ GitHub Models နှင့် ဆက်စပ် code များ ဖယ်ရှားထားသည်။
- [ ] `rg "OpenAIChatCompletionClient"` မတွေ့ရ၊ MAF 1.0.0+ တွင် `OpenAIChatClient` ကို အသုံးပြုသည် (Responses API ကိုအသုံးပြုသည်)။ 1.0.0 မတိုင်မီတွင် `agent-framework-openai>=1.0.0` သို့မြှင့်တင်ပါ။
- [ ] အားလုံး `ChatOpenAI(...)` ခေါ်သုံးမှုများတွင် `use_responses_api=True` ပါဝင်စေရန်။
- [ ] `rg "choices\[0\]"` မရှိရ၊ တုံ့ပြန်ချက်များအားလုံးသည် `resp.output_text` သို့မဟုတ် Responses output schema ကိုအသုံးပြုထားသည်။
- [ ] အထက်တန်း `response_format` မပါ၊ ဖွဲ့စည်းထားသော output အားလုံးမှာ `text={"format": {...}}` ကိုအသုံးပြုပါ။
- [ ] `openai>=1.108.1` နှင့် `azure-identity` ကို `requirements.txt` သို့ `pyproject.toml` တွင်ပါရှိပြီး dependency များအား ပြန်လည်တပ်ဆင်ထားသည်။
- [ ] မှန်ကန်စွာ `store=False` ကို `responses.create` ခေါ်သုံးမှုတိုင်းတွင် သတ်မှတ်ထားသည်။
- [ ] client constructor တွင် `api_version` မပါ၊ `AZURE_OPENAI_API_VERSION` ကို environment files နှင့် infrastructure မှ ဖယ်ရှားထားသည်။

### စမ်းသပ်မှုဆိုင်ရာ ဂိတ်များ (အားလုံးဖြတ်သန်းရမည်)

- [ ] `rg "ChatCompletionChunk|AsyncCompletions\.create|chat\.completions" tests/` မတွေ့ရ။
- [ ] `rg "_azure_ad_token_provider" tests/` မတွေ့ရ၊ assertion များကို `isinstance(client, AsyncOpenAI)` သို့ `base_url` ကိုစစ်ဆေးပြီး update လုပ်ထားသည်။
- [ ] `rg "prompt_filter_results|content_filter_results" tests/` မတွေ့ရ၊ Azure-specific filter mock များ ဖယ်ရှားထားသည်။
- [ ] mock fixtures များသည် `kwargs.get("input")` ကိုအသုံးပြု၊ `kwargs.get("messages")` မဟုတ်ပါ။
- [ ] snapshot / golden files များကို Responses streaming ပုံစံ ( `choices[0]`, `function_call`, `logprobs` မဟုတ်သော) သို့ update ပြုလုပ်ထားသည်။
- [ ] `pytest` များသည် မတည့်မှုများမရှိဘဲ ဖြတ်သန်းနိုင်သည်။

### အပြုအမူ ဆိုင်ရာ ဂိတ်များ (ကိုယ့်အတိုင်သက်သေတမ်း သို့မဟုတ် စမ်းသပ်မှုမှ ကြည့်ရှုရန်)

- [ ] **အခြေခံဖြည့်စွက်မှု**: non-streaming `responses.create` သည် အလွတ်သလောက် `output_text` ပြန်ပေးသည်။
- [ ] **Stream တူညီမှု**: မူရင်းကုဒ်သည် streaming ကိုအသုံးပြုခဲ့လျှင်၊ ပြောင်းလဲပြီးကုဒ်သည် streaming ပြီး `response.output_text.delta` event များဖြင့် non-empty delta များထုတ်ပေးသည်။
- [ ] **ဖွဲ့စည်းထားသော output**: `text.format` တွင် `json_schema` အသုံးပြုလျှင် `json.loads(resp.output_text)` သည်  အောင်မြင်ပြီး schema နှင့်ကိုက်ညီသည်။
- [ ] **Tool-call လုပ်ငန်းစဉ်**: tool များကိုအသုံးပြုလျှင်၊ မော်ဒယ်သည် tool call များ ထုတ်ပေးကာ App သည် အကောင်အထည်ဖော်၊ နောက်တုံ့ပြန်ချက်တွင် နောက်ဆုံး `output_text` ပြန်ရှိသည် (အဆုံးမပျက်သော loop မရှိ)။
- [ ] **Async တူညီမှု**: `AsyncAzureOpenAI` ကိုအသုံးပြုခဲ့လျှင် `AsyncOpenAI` equivalent သည် `await` ဖြင့် ရိုးရိုးလည်ပတ်နိုင်သည်။
- [ ] **Error အလားအလာ**: ရှိပြီးသား baseline နှင့်နှိုင်းလျှင် 400/401/404 error အသစ် မရှိရ။

### လက်ခံသင့်သည့် deliverables များ

- အကျဉ်းချုပ်တွင် ပြင်ဆင်ပြီးဖိုင်များ၊ legacy call sites များ၏ မတည့်မှုအရေအတွက်(ရှေ့/နောက်) နှင့် နောက်ဆက်တွဲအဆင့်များ ပါဝင်ရမည်။
- ပြင်ဆင်ထားမှုများသည် working-tree edits များသာဖြစ်ပြီး commit မထည့်ပါ။

---

## SDK ဗားရှင်း လိုအပ်ချက်များ

| package | အနည်းဆုံးဗားရှင်း |
|---------|----------------|
| `openai` | `>=1.108.1` |
| `azure-identity` | နောက်ဆုံးဗားရှင်း (EntraID authentication အတွက်) |

---

## ကိုးကားချက်များ

- [Cheat Sheet — အားလုံးသော Code Snippets](./references/cheat-sheet.md)
- [Test Migration — mocks, snapshots, assertions](./references/test-migration.md)
- [Troubleshooting — အမှားများ၊ စိုးရိမ်ရသောအချက်များ၊ အသိပေးချက်များ](./references/troubleshooting.md)
- [detect_legacy.py — automated scanner](../../../../../.agents/skills/azure-openai-to-responses/scripts/detect_legacy.py)
- [Azure OpenAI Starter Kit](https://aka.ms/openai/start)
- [Azure OpenAI Responses API စာတမ်းများ](https://learn.microsoft.com/en-us/azure/ai-foundry/openai/how-to/responses)
- [Azure OpenAI API version lifecycle](https://learn.microsoft.com/en-us/azure/ai-foundry/openai/api-version-lifecycle?view=foundry-classic&tabs=python#api-evolution)
- [OpenAI Responses API ကိုးကားချက်](https://platform.openai.com/docs/api-reference/responses)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ပြောကြားချက်**
ဤစာတမ်းကို AI ဘာသာပြန်ဝန်ဆောင်မှု [Co-op Translator](https://github.com/Azure/co-op-translator) အသုံးပြု၍ ဘာသာပြန်ထားပါသည်။ ကျွန်ုပ်တို့သည် တိကျမှန်ကန်မှုအတွက် ကြိုးပမ်းနေသော်လည်း၊ စက်ကိရိယာဘာသာပြန်ခြင်းများတွင် အမှားများ သို့မဟုတ် မှားယွင်းချက်များ ပါဝင်နိုင်ကြောင်း သတိပြုပါရန် လိုအပ်ပါသည်။ မူလစာတမ်းကို မူရင်းဘာသာဖြင့်သာ ယုံကြည်စိတ်ချရသော အချက်အလက်အဖြစ် သတ်မှတ်သင့်သည်။ အရေးကြီးသည့် သတင်းအချက်အလက်များအတွက် ပရော်ဖက်ရှင်နယ် လူသားဘာသာပြန်သူဝန်ဆောင်မှုကို အကြံပြုပါသည်။ ဤဘာသာပြန်ချက်ကို အသုံးပြုခြင်းမှ ဖြစ်ပေါ်လာသော နားလည်မှုကွာခြားမှုများ သို့မဟုတ် မမှန်ကန်သော အသုံးပြုမှုများအတွက် ကျွန်ုပ်တို့ တာဝန်မခံပါ။
<!-- CO-OP TRANSLATOR DISCLAIMER END -->