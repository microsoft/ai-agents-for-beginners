---
name: microsoft-docs
---
# Microsoft Docs

Microsoft နည်းပညာ ecosystem အတွက် သုတေသန ကျွမ်းကျင်မှု။ learn.microsoft.com နှင့် အဲဒီထဲမှာမဟုတ်တဲ့ စာတမ်းများ (VS Code, GitHub, Aspire, Agent Framework repos) ကို ဖုံးကွယ်ပါသည်။

---

## ပုံမှန်: Microsoft Learn MCP

learn.microsoft.com အတွက် **အရာအားလုံးကို** ဒီကိရိယာများကို အသုံးပြုပါ — Azure, .NET, M365, Power Platform, Agent Framework, Semantic Kernel, Windows နှင့် အခြားများ။ ဒါက Microsoft စာတမ်းများ မေးခွန်းများ အများအပြားအတွက် အဓိက ကိရိယာဖြစ်သည်။

| ကိရိယာ | ရည်ရွယ်ချက် |
|------|---------|
| `microsoft_docs_search` | learn.microsoft.com မှ ပညာရပ်များ၊ လမ်းညွှန်များ၊ သင်ခန်းစာများ၊ ဆက်တင်များကို ရှာဖွေခြင်း |
| `microsoft_code_sample_search` | Learn စာတမ်းများမှ စမ်းသပ်ထားသော ကုဒ်နမူနာများ ရှာဖွေခြင်း။ ထိရောက်ဆုံးရလဒ်အတွက် `language` (`python`, `csharp`, စသည်) ကို ဖြတ်သန်းပါ |
| `microsoft_docs_fetch` | ရှာဖွေမှု ဖော်ပြချက်များမလုံလောက်လျှင် ထူးချွန် URL မှ အပြည့်အစုံစာမျက်နှာအကြောင်းအရာ ရယူခြင်း |

ရှာဖွေပြီးနောက် `microsoft_docs_fetch` ကို အသုံးပြုပါ သင့်လျော်သော သင်ခန်းစာများ၊ ဆက်တင်ရွေးချယ်စရာများ အပြည့်အဝလိုအပ်ပါက သို့မဟုတ် ရှာဖွေမှုဖော်ပြချက်များကို truncated ဖြစ်လျှင်။

---

## ကွဲပြားချက်များ: အခြား ကိရိယာများ သုံးရန်အချိန်

အောက်ပါအမျိုးအစားများသည် learn.microsoft.com မှ **ပြင်ပမှာ** ရှိသည်။ သတ်မှတ်ထားသော ကိရိယာကို အစားထိုး အသုံးပြုပါ။

### Aspire — Aspire MCP Server (preferrred) သို့မဟုတ် Context7 ကို အသုံးပြုပါ

Aspire စာတမ်းများသည် **aspire.dev** တွင်ရှိပြီး Learn တွင်မဟုတ်ပါ။ အကောင်းဆုံး ကိရိယာသည် Aspire CLI ဗားရှင်းပေါ် မူတည်သည်။

**CLI 13.2+** (အကြံပြု) — Aspire MCP server တွင် စာတမ်းရှာဖွေရေးကိရိယာများ ပါဝင်သည်။

| MCP ကိရိယာ | ဖော်ပြချက် |
|----------|-------------|
| `list_docs` | aspire.dev တင်သည့် စာတမ်းအားလုံး စာရင်းပြုစုချက် |
| `search_docs` | aspire.dev အကြောင်းအရာများ ပေါ်တွင် အလေးပေး စာလုံးရှာဖွေရေး |
| `get_doc` | slug ဖြင့် တိကျသော စာတမ်း ရယူခြင်း |

Aspire CLI 13.2 တွင် ပါလာသည် ([PR #14028](https://github.com/microsoft/aspire/pull/14028))။ Update ပြုလုပ်ရန်: `aspire update --self --channel daily`။

**CLI 13.1** — MCP server တွင် integration lookup (`list_integrations`, `get_integration_docs`) ပေးထားသော်လည်း **စာတမ်းရှာဖွေမှု မပါဝင်ပါ။** Context7 ကို ပြန်လည်အသုံးပြုပါ။

| စာကြည့်တိုက် ID | အသုံးပြုရန် |
|---|---|
| `/microsoft/aspire.dev` | အဓိက — လမ်းညွှန်များ၊ ပေါင်းစပ်မှုများ၊ CLI အညွှန်း၊ တပ်ဆင်ခြင်း |
| `/microsoft/aspire` | runtime အင်တာနယ်— API အတွင်းပိုင်း၊ အကောင်အထည်ဖော်ချက် အသေးစိတ် |
| `/communitytoolkit/aspire` | လူ့အသိုင်းအဝိုင်း ပေါင်းစပ်မှုများ — Go, Java, Node.js, Ollama |

### VS Code — Context7 ကို အသုံးပြုပါ

VS Code စာတမ်းများသည် **code.visualstudio.com** တွင် ရှိပြီး Learn တွင်မဟုတ်ပါ။

| စာကြည့်တိုက် ID | အသုံးပြုရန် |
|---|---|
| `/websites/code_visualstudio` | အသုံးပြုသူ စာတမ်း — တပ်ဆင်မှုများ၊ လုပ်ဆောင်ချက်များ၊ အမှားရှာခြင်း၊ အကွာအဝေး ဖွံ့ဖြိုးရေး |
| `/websites/code_visualstudio_api` | Extension API — webviews, TreeViews, commands, contribution points |

### GitHub — Context7 ကို အသုံးပြုပါ

GitHub စာတမ်းများသည် **docs.github.com** နှင့် **cli.github.com** တွင် ရှိသည်။

| စာကြည့်တိုက် ID | အသုံးပြုရန် |
|---|---|
| `/websites/github_en` | Actions, API, repos, security, admin, Copilot |
| `/websites/cli_github` | GitHub CLI (`gh`) commands နှင့် flags |

### Agent Framework — Learn MCP + Context7 ကို အသုံးပြုပါ

Agent Framework သင်ခန်းစာများသည် learn.microsoft.com တွင် ရှိသည် (`microsoft_docs_search` ကို အသုံးပြုပါ)၊ သို့သော် **GitHub repo** သည် API အဆင့်အသေးစိတ်ဖြစ်ပြီး မကြာခဏ ထုတ်ပြန်ထားသော စာတမ်းတွေထက် ရှေ့နေသည် — အထူးသဖြင့် DevUI REST API အညွှန်း၊ CLI ရွေးချယ်စရာများနှင့် .NET ပေါင်းစပ်မှု။

| စာကြည့်တိုက် ID | အသုံးပြုရန် |
|---|---|
| `/websites/learn_microsoft_en-us_agent-framework` | သင်ခန်းစာများ — DevUI လမ်းညွှန်များ၊ အသိအမှတ်ပြုခြင်း၊ workflow စီမံခန့်ခွဲမှု |
| `/microsoft/agent-framework` | API အသေးစိတ် — DevUI REST endpoints, CLI flags, authentication, .NET `AddDevUI`/`MapDevUI` |

**DevUI အကြံပြုချက်:** လုပ်ဆောင်နည်းလမ်းလမ်းညွှန်များအတွက် Learn ဝက်ဘ်ဆိုက် အရင်းအမြစ်ကို ခေါ်ဆိုပြီး၊ API အဆင့် အသေးစိတ်များ (endpoint schemas, proxy config, authentication tokens) အတွက် repo အရင်းအမြစ်ကို အကောက်ယူပါ။

---

## Context7 စီစဉ်ခြင်း

Context7 မေးခွန်းအတွက် library ID ကို အရင်ဆုံး ဖြေရှင်းပါ (session တစ်ခုလျှင် တစ်ကြိမ်သာ)။

1. နည်းပညာအမည်ဖြင့် `mcp_context7_resolve-library-id` ကို ခေါ်ဆိုပါ
2. ပြန်လည်ရရှိသော စာကြည့်တိုက် ID နှင့် သတ်မှတ်ထားသော မေးခွန်း ဖြင့် `mcp_context7_query-docs` ကို ခေါ်ဆိုပါ

---

## ထိရောက်သော မေးခွန်းများ ရေးသားခြင်း

တိကျသေချာစွာ ရေးပါ — ဗားရှင်း၊ ရည်ရွယ်ချက်နှင့် ဘာသာစကား ပါဝင်အောင်။

```
# ❌ Too broad
"Azure Functions"
"agent framework"

# ✅ Specific
"Azure Functions Python v2 programming model"
"Cosmos DB partition key design best practices"
"GitHub Actions workflow_dispatch inputs matrix strategy"
"Aspire AddUvicornApp Python FastAPI integration"
"DevUI serve agents tracing OpenTelemetry directory discovery"
"Agent Framework workflow conditional edges branching handoff"
```

context ပါဝင်အောင် - 
- **ဗားရှင်း** သက်ဆိုင်လျှင် (`.NET 8`, `Aspire 13`, `VS Code 1.96`)
- **အလုပ်ရည်ရွယ်ချက်** (`quickstart`, `tutorial`, `overview`, `limits`, `API reference`)
- **ဘာသာစကား** အများဘက်စာတမ်းများအတွက် (`Python`, `TypeScript`, `C#`)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ပြောကြားချက်**
ဤစာတမ်းကို AI ဘာသာပြန်ဝန်ဆောင်မှု [Co-op Translator](https://github.com/Azure/co-op-translator) အသုံးပြု၍ ဘာသာပြန်ထားပါသည်။ ကျွန်ုပ်တို့သည် တိကျမှန်ကန်မှုအတွက် ကြိုးပမ်းနေသော်လည်း၊ စက်ကိရိယာဘာသာပြန်ခြင်းများတွင် အမှားများ သို့မဟုတ် မှားယွင်းချက်များ ပါဝင်နိုင်ကြောင်း သတိပြုပါရန် လိုအပ်ပါသည်။ မူလစာတမ်းကို မူရင်းဘာသာဖြင့်သာ ယုံကြည်စိတ်ချရသော အချက်အလက်အဖြစ် သတ်မှတ်သင့်သည်။ အရေးကြီးသည့် သတင်းအချက်အလက်များအတွက် ပရော်ဖက်ရှင်နယ် လူသားဘာသာပြန်သူဝန်ဆောင်မှုကို အကြံပြုပါသည်။ ဤဘာသာပြန်ချက်ကို အသုံးပြုခြင်းမှ ဖြစ်ပေါ်လာသော နားလည်မှုကွာခြားမှုများ သို့မဟုတ် မမှန်ကန်သော အသုံးပြုမှုများအတွက် ကျွန်ုပ်တို့ တာဝန်မခံပါ။
<!-- CO-OP TRANSLATOR DISCLAIMER END -->