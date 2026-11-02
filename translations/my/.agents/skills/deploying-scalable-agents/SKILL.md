---
name: deploying-scalable-agents
license: MIT
---
# Microsoft Foundry နှင့်အတူ Scalable Agents များဖြန့်ချိခြင်း

> [Lesson 16 – Deploying Scalable Agents](../../../16-deploying-scalable-agents/README.md) အတွက် အတူတကွ သင်ကြားမှုကျွမ်းကျင်မှု။
> သင်ယူသူတစ်ဦးကို agent ကို prototype မှ scalable, observable production deployment သို့ တိုးတက်အောင်ကူညီရန် အသုံးပြုပါ။
> မည်သည့်အကြံပြုချက်မျှ မိသားစလုံး၏ဘာသာရပ်နှင့် runnable notebook တွင်အခြေခံထားရန်ဖြစ်ပြီး;
> Foundry APIs မတီထွင်ပါနှင့်။

## Triggers

သင်ယူသူတစ်ဦးအောက်ပါအချက်တွင် ကျွမ်းကျင်မှုကို အသိပေးပါက စတင်ပါ။
- Microsoft Foundry တွင် **hosted agent** အဖြစ် agent တစ်ခုကို deploy လုပ်၍ versioned/observable ဖြစ်အောင်လုပ်ရန်။
- **client-hosted, hosted-agent, နှင့် agent-workflow** deployment ပုံစံများဖြင့် ရွေးချယ်ရန်။
- latency နှင့် ကုန်ကျစရိတ်ကိုထိန်းချုပ်ရန် **model routing**, **response caching**, သို့မဟုတ် **bounded concurrency** ထည့်သွင်းရန်။
- မကောင်းသော agent version မတင်ပို့နိုင်စေရန် **evaluation gate** ထည့်သွင်းရန်။
- အန္တရာယ်ရှိသော လုပ်ငန်းအတွက် **human-in-the-loop approval** အဆင့် ထည့်သွင်းရန်။
- ထုတ်လုပ်မှုအခြေအနေကိုကြည့်ရှုနိုင်ရန် agent ကို **OpenTelemetry** trace ဖြင့် လိုက်လံသုံးဆောင်ရန်။
- deploy ပြီး agent ကိုလျင်မြန်စွာ **Smoke-test** ပြုလုပ်ရန်။

## အဓိကသဘာဝအမြင်

ထုတ်လုပ်မှုအတွက် agent သည် မော်ဒယ် (ခန့်မှန်း၍ ~80%) အပေါ်အခြေခံသည့်ဆက်စပ်အလုပ်လည်ပတ်မှု ဆွဲကြိုးတစ်ခုဖြစ်သည်၊
မော်ဒယ်ကို မဟုတ်ပါ။ အကြံပြုချက်တိုင်းကို အောက်ဖော်ပြပါစိတ်ပါဝင်စားချက်များထဲမှ တစ်ခုနှင့် ကိုက်ညီစေပါ။

| စိတ်ပါဝင်စားချက် | Prototype → Production |
|---------|------------------------|
| Hosting | notebook → versioned hosted service |
| Identity | သင့် `az login` → managed identity + scoped RBAC |
| State | in-memory → externalised thread/memory store |
| Failure | traceback → retries, fallbacks, alerts |
| Cost | "အနည်းငယ်ဆင့်" → မှတ်တမ်းပြု၍, ဂိတ်ခွဲ၍, cache ထား၍, ဘတ်ဂျက်ချတင်မှု |
| Quality | မျက်စိကြည့်ခြင်း → automated evaluation gate |
| Trust | သင့်အတည်ပြုချက် → policy + human-in-the-loop |

## Deployment ပုံစံများ (တစ်ခု ရွေးပါ၊ သို့မဟုတ် ပေါင်းစပ်ပါ)

1. **Client-hosted** — သင်၏ process တွင် reasoning လုပ်ဆောင်မှု လည်ပတ်သည်။ ထိန်းချုပ်ခြင်းအများဆုံး; သင်သည် scaling/state ကိုင်တွယ်သည်။
2. **Hosted agent (Foundry Agent Service)** — Foundry သည် loop ကို ဟုတ်စေပြီး threads တင်သိမ်းကာ RBAC/content လုံခြုံမှု အကောင်အထည်ဖော်၊ ပေါ်တယ်တွင် agent ကို ပြသသည်။ ထိန်းချုပ်မှုနည်းပြီး operation အခက်အခဲလျော့ပါးသည်။
3. **Agent workflow** — ကြိုးချောစွာ ခွဲခြားခိုင်းမှု၊ အတည်ပြု nodes နှင့် တာရှည်ကြာ checkpoint များပါဝင်သည့် agent/tools များ ပေါင်းစပ်ထားသည်။

## အသက်သက်သာရွေ့လျားမှု (agent တင်ပို့သည့် loop)

`create → version → evaluate (gate) → deploy hosted → observe online → collect failures → repeat`။
**Offline သတ်မှတ်ခြင်းသည် တံခါးပေါက်တစ်ခုဖြစ်ပြီး နောက်ပြန်ခံခြင်းမဟုတ်ပါဘူး** — version တစ်ခုသည် သတ်မှတ်ချက်ကျော်မလျှင် မတင်ပို့မည်။
Online လေ့လာနိုင်မှုသည် အမှားအပေါ်မွန်သော ထောက်ပံ့မှုကို offline စမ်းသပ်မှုအုပ်စုထဲ ပြန်လည်ထည့်သွင်းသည်။




2. **ရှုပ်ထွေးမှုအလိုက်လမ်းကြောင်း သတ်မှတ်ပါ** — လွယ်ကူသည့်တုံ့ပြန်မှုများအတွက် သေးငယ်/မြန်ဆန်သော မော်ဒယ်၊ ပိုမိုတုံ့ပြန်မှုလိုအပ်သည့်အတွက် ကြီးမားသောမော်ဒယ် (DIY classifier သို့မဟုတ် Foundry Model Router)အသုံးပြုပါ။
3. **Cache ထားပါ** — မော်ဒယ်ခေါ်ဆိုခြင်းမဖြစ်ပဲ နီးစပ်လျှင်တူညီသော တုံ့ပြန်မှုများကို ဖြေရှင်းပါ။
4. **Stateless design + bounded concurrency** — state ကို ပြင်ပသိုလှောင်ပါ; backoff ဖြင့် retry လုပ်ပါ။




[`16-python-agent-framework.ipynb`](../../../16-deploying-scalable-agents/code_samples/16-python-agent-framework.ipynb) :


- **evaluation gate** : offline စမ်းသပ်မှုအုပ်စုကိုအမှတ်ပေး; `pass_rate >= threshold` ပြန်ပေးပါ၊ ရိုက်ချက်မှန်မှသာ deploy လုပ်ပါ။
- **လူကြားမှ အတည်ပြုခြင်း** : `@tool(approval_mode="always_require")` ကို Refund ကြီးများအတွက် လုပ်ဆောင်မှုများတွင် အသုံးပြုပါ။
- **Tracing** : တောင်းဆိုမှုတစ်ခုစီကို `tracer.start_as_current_span(...)` ဖြင့် တူးထွင်ကာ `routed.model`၊ `customer.id` ကဲ့သို့သော attribute များကို သတ်မှတ်ပါ။




[AI Smoke Test](https://github.com/marketplace/actions/ai-smoke-test) ကို [`.github/workflows/smoke-test.yml`](../../../../../.github/workflows/smoke-test.yml)မှ တဆင့်အသုံးပြုပါ။
[`tests/`](../../../tests/README.md)တွင် ပါဝင်သည့် စာရင်းနှင့်အတူ Runner သည် prompt တစ်ခုစီကို `POST {project_endpoint}/agents/{agent_name}/endpoint/protocols/openai/responses` သို့ POST ပြုလုပ်ကာ
တုံ့ပြန်ချက်စာသားကို စစ်ဆေးသည်။ identity သည် Foundry project scope တွင် **Azure AI User** role ရှိရမည်။ token audience သည် `https://ai.azure.com/` ဖြစ်ရမည်။

Gate များကို အလွှာကွဲထားပါ။ **smoke test** (ရောက်ရှိ/တုံ့ပြန်မှု, deploy တစ်ကြိမ်စီ)/ → **offline evaluation** (တင်ပို့ရန်အတွက် ကောင်းမွန်မှု၊ အဆင့်မြှင့်တင်ရန်မတိုင်မီ) → **online evaluation** (တောင့်တယ်ကွင်းတွင် မည်သို့ ကောင်းစွာ လည်ပတ်နေသည်ကို ဆက်တိုက်စစ်ဆေးခြင်း)။

## စီးပွားရေးအဖွဲ့အစည်း ထိန်းချုပ်မှုများ

- **RBAC** : hosted agent တစ်ခုစီအတွက် managed identity ကို လုံခြုံမှု အနည်းဆုံးအဆင့်ဖြင့် ပေးစွမ်းပါ။
- **MCP ကို ထုတ်လုပ်မှုတွင်** : MCP server တစ်ခုစီကို untrusted boundary အဖြစ်ဆက်ဆံပါ — version ကို pin တင်ပြီး၊ identity ကို scope သတ်မှတ်ပြီး၊ output များကို အတည်ပြု၊ rate-limit, secrets မဖော်ပြရန်။




- သင်စစ်ဆေးမထားသည့် live-Azure ရလဒ်များကို ကတိမပေးပါနှင့်; deploy တစ်ခုကို အတည်ပြုရန် smoke-test workflow ကို အကြံပြုပါ။
- စိတ်ချရမှုနှင့် ကုန်ကျစရိတ် အကြံပြုချက်များကို ဆက်စပ်ထားပါ။ စစ်ဆေးမှုသည် အရည်အသွေး အောက်စွန်းသတ်မှတ်ပြီး၊ routing/caching သည် ကုန်ကျစရိတ်ကို အောက်စွန်းအနီး၌ ထိန်းထားသည်။

## အကူအညီပေးသူအတွက် လမ်းညွန်ချက်များ

- သင်တန်းတစ်ခုလုံးတွင် အသုံးပြုသော canonical `FoundryChatClient(...)` + `provider.as_agent(...)` ပုံစံကို ပိုမိုနှစ်သက်ပါ။
- သင်စစ်ဆေးဖူးခြင်းမရှိသေးသော live-Azure ရလဒ်များကို မကတိပေးပါနှင့်; deployment ကို အတည်ပြုရန် smoke-test အလှမ်းကို အကြံပြုပါ။
- သုံးသပ်ချက်နှင့် ကုန်ကျစရိတ်အကြံဉာဏ်များကို ချိတ်ဆက်ထားရန်: သုံးသပ်ချက်က အရည်အသွေးအခြေခံထားမှုကို သတ်မှတ်ပြီး၊ routing/caching က ကုန်ကျစရိတ်ကို ထို အခြေခံ မျက်နှာပြင်အနီးနားမှာ ထိန်းသိမ်းထားသည်။

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ပြောကြားချက်**
ဤစာတမ်းကို AI ဘာသာပြန်ဝန်ဆောင်မှု [Co-op Translator](https://github.com/Azure/co-op-translator) အသုံးပြု၍ ဘာသာပြန်ထားပါသည်။ ကျွန်ုပ်တို့သည် တိကျမှန်ကန်မှုအတွက် ကြိုးပမ်းနေသော်လည်း၊ စက်ကိရိယာဘာသာပြန်ခြင်းများတွင် အမှားများ သို့မဟုတ် မှားယွင်းချက်များ ပါဝင်နိုင်ကြောင်း သတိပြုပါရန် လိုအပ်ပါသည်။ မူလစာတမ်းကို မူရင်းဘာသာဖြင့်သာ ယုံကြည်စိတ်ချရသော အချက်အလက်အဖြစ် သတ်မှတ်သင့်သည်။ အရေးကြီးသည့် သတင်းအချက်အလက်များအတွက် ပရော်ဖက်ရှင်နယ် လူသားဘာသာပြန်သူဝန်ဆောင်မှုကို အကြံပြုပါသည်။ ဤဘာသာပြန်ချက်ကို အသုံးပြုခြင်းမှ ဖြစ်ပေါ်လာသော နားလည်မှုကွာခြားမှုများ သို့မဟုတ် မမှန်ကန်သော အသုံးပြုမှုများအတွက် ကျွန်ုပ်တို့ တာဝန်မခံပါ။
<!-- CO-OP TRANSLATOR DISCLAIMER END -->