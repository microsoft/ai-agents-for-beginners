---
name: microsoft-docs
description: Azure, .NET, Agent Framework, Aspire, VS Code, GitHub နှင့် အခြားများအပါအဝင်
  တရားဝင် Microsoft အထောက်အထားများကို မေးမြန်း၍ အယူအဆများ၊ သင်ခန်းစာများနှင့် ကုဒ်
  ဥပမာများကို ရှာဖွေပါ။ Microsoft Learn MCP ကို ပုံမှန် အဖြစ် အသုံးပြု၍ learn.microsoft.com
  ပြင်ပတွင် တည်ရှိသော အကြောင်းအရာများအတွက် Context7 နှင့် Aspire MCP ကို အသုံးပြုသည်။
---
# Microsoft Docs

Microsoft နည်းပညာ ပတ်ဝန်းကျင်အတွက် သုတေသန ကျွမ်းကျင်မှု။ learn.microsoft.com နှင့် အဲဒီမှာ မပါသော စာတမ်းများ (VS Code, GitHub, Aspire, Agent Framework repos) ကို ဖုံးလွှမ်းပါသည်။

---

## ပုံမှန်: Microsoft Learn MCP

learn.microsoft.com ပေါ်ရှိ အရာအားလုံးအတွက် ဤကိရိယာများကို အသုံးပြုပါ — Azure, .NET, M365, Power Platform, Agent Framework, Semantic Kernel, Windows နှင့် အခြားများ။ ၎င်းသည် Microsoft စာတမ်းများ မေးခွန်းများအတွက် အဓိက ကိရိယာဖြစ်သည်။

| ကိရိယာ | ရည်ရွယ်ချက် |
|------|---------|
| `microsoft_docs_search` | learn.microsoft.com တွင် ရှာဖွေမည် — အယူအဆများ၊ လမ်းညွှန်များ၊ သင်ခန်းစာများ၊ ဆက်တင်များ |
| `microsoft_code_sample_search` | Learn စာတမ်းများမှ အလုပ်လုပ်နိုင်သော ကုဒ် သရုပ်ပြများကို ရှာဖွေပါ။ အကောင်းဆုံးရလဒ်အတွက် `language` (`python`, `csharp`, etc.) ကို ပေးပါ |
| `microsoft_docs_fetch` | စာမျက်နှာတစ်ခုလျှင် အပြည့်အစုံကို URL တိတိမှ ရယူပါ (search မှ ပြုတ်ကျမှုများ မလုံလောက်သောအခါ) |

search အပြီးမှာ သင်အပြည့်အစုံ သင်ခန်းစာများ၊ ဆက်တင်ရွေးချယ်စရာအားလုံး သို့မဟုတ် search မှ ရှောင်ကြဉ်ထားသော အစိတ်အပိုင်းများ လိုအပ်သည့်အခါ `microsoft_docs_fetch` ကို အသုံးပြုပါ။

---

## ထူးခြားချက်များ: အခြား ကိရိယာများကို ဘယ်အချိန် အသုံးပြုမည်နည်း

အောက်ပါ အမျိုးအစားများသည် learn.microsoft.com အပြင်တွင် ရှိသည်။ အစားထိုးထားသော ကိရိယာကို အသုံးပြုပါ။

### .NET Aspire — Aspire MCP Server (အကြိုက်ဆုံး) သို့မဟုတ် Context7 ကို အသုံးပြုပါ

Aspire စာတမ်းများသည် Learn တွင်မဟုတ်ဘဲ **aspire.dev** ပေါ်တွင် ရှိသည်။ အကောင်းဆုံး ကိရိယာမှာ သင့် Aspire CLI ဗားရှင်းပေါ် မူတည်ပါသည်။

**CLI 13.2+** (အကြံပြု) — Aspire MCP server သည် အတွင်းပိုင်း docs ရှာဖွေရေး ကိရိယာများကို ထည့်သွင်းပေးထားသည်။

| MCP Tool | Description |
|----------|-------------|
| `list_docs` | aspire.dev မှ ရရှိနိုင်သည့် စာတမ်းများအားလုံးကို စာရင်းပြမည် |
| `search_docs` | aspire.dev အကြောင်းအရာများအနှံ့ အလေးချိန်ထားသော စကားလုံးအခြေခံ ရှာဖွေမှု |
| `get_doc` | slug ဖြင့် သတ်မှတ်ထားသော စာတမ်းကို ရယူမည် |

ဤများသည် Aspire CLI 13.2 တွင် ပါဝင်သည် ([PR #14028](https://github.com/dotnet/aspire/pull/14028))။ အပ်ဒိတ်လုပ်ရန်: `aspire update --self --channel daily`။ Ref: https://davidpine.dev/posts/aspire-docs-mcp-tools/

**CLI 13.1** — MCP server သည် integration lookup (`list_integrations`, `get_integration_docs`) ကို ပံ့ပိုးပေးသော်လည်း docs ရှာဖွေမှုကို မပံ့ပိုးပါ။ Context7 သို့ ပြန်လှည့်ပါ။

| Library ID | အသုံးပြုရန် |
|---|---|
| `/microsoft/aspire.dev` | Primary — လမ်းညွှန်များ၊ integrations, CLI ကိုးကားချက်, deployment |
| `/dotnet/aspire` | Runtime source — API အတွင်းပိုင်း၊ အကောင်အထည်ဖော်ချက် အသေးစိတ်များ |
| `/communitytoolkit/aspire` | Community integrations — Go, Java, Node.js, Ollama |

### VS Code — Context7 ကို အသုံးပြုပါ

VS Code စာတမ်းများသည် Learn တွင်မဟုတ်ဘဲ **code.visualstudio.com** ပေါ်တွင် ရှိသည်။

| Library ID | အသုံးပြုရန် |
|---|---|
| `/websites/code_visualstudio` | အသုံးပြုသူ စာတမ်း — ဆက်တင်များ၊ အင်္ဂါရပ်များ၊ ဒေဘတ်ဂ်လုပ်ခြင်း၊ အဝေးမှ ဖွံ့ဖြိုးရေး |
| `/websites/code_visualstudio_api` | Extension API — webviews, TreeViews, commands, contribution points |

### GitHub — Context7 ကို အသုံးပြုပါ

GitHub စာတမ်းများသည် **docs.github.com** နှင့် **cli.github.com** ပေါ်တွင် ရှိသည်။

| Library ID | အသုံးပြုရန် |
|---|---|
| `/websites/github_en` | Actions, API, repos, security, admin, Copilot |
| `/websites/cli_github` | GitHub CLI (`gh`) အမိန့်များ နှင့် ဖလက်များ |

### Agent Framework — Learn MCP + Context7 ကို အသုံးပြုပါ

Agent Framework သင်ခန်းစာများသည် learn.microsoft.com တွင် ရှိသည် (အသုံးပြုပါ `microsoft_docs_search`), သို့သော် **GitHub repo** တွင် API အဆင့် အသေးစိတ်များရှိပြီး အများအားဖြင့် ထုတ်ပြန်ထားသော စာတမ်းများထက် မြန်ဆန်တတ်သည် — အထူးသဖြင့် DevUI REST API ကိုးကားချက်၊ CLI ရွေးချယ်စရာများ၊ နှင့် .NET ပေါင်းစည်းမှု။

| Library ID | အသုံးပြုရန် |
|---|---|
| `/websites/learn_microsoft_en-us_agent-framework` | Tutorials — DevUI လမ်းညွှန်များ၊ tracing၊ workflow စီမံခန့်ခွဲမှု |
| `/microsoft/agent-framework` | API detail — DevUI REST endpoints, CLI flags, auth, .NET `AddDevUI`/`MapDevUI` |

**DevUI tip:** Learn website source ကနေ how-to လမ်းညွှန်များကို ရှာဖွေပြီး၊ API-အဆင့် အသေးစိတ်များ (endpoint schemas, proxy config, auth tokens) အတွက် repo source ကို ရှာပါ။

---

## Context7 တပ်ဆင်မှု

Context7 မေးခွန်းများအတွက် library ID ကို ပထမဦးစွာ ဖြေရှင်းပါ (session တစ်ခုလျှင် တစ်ကြိမ်):

1. နည်းပညာ အမည်ဖြင့် `mcp_context7_resolve-library-id` ကို ခေါ်ပါ
2. ပြန်လာသော library ID နှင့် အထူးမေးခွန်းတစ်ခုဖြင့် `mcp_context7_query-docs` ကို ခေါ်ပါ

---

## ထိရောက်သော မေးခွန်းရေးသားနည်း

တိကျစွာ ရေးပါ — ဗားရှင်း၊ ရည်ရွယ်ချက်၊ နှင့် ဘာသာစကားကို ထည့်ပါ။

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

အကြောင်းအရာ ထည့်သွင်းပါ:
- **ဗားရှင်း** သက်ဆိုင်သောအခါ (`.NET 8`, `Aspire 13`, `VS Code 1.96`)
- **လုပ်ငန်း ရည်ရွယ်ချက်** (`quickstart`, `tutorial`, `overview`, `limits`, `API reference`)
- **ဘာသာစကား** အတွက် polyglot စာတမ်းများ (`Python`, `TypeScript`, `C#`)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
မှတ်ချက် (Disclaimer):

ဤစာရွက်စာတမ်းကို AI ဘာသာပြန်ဝန်ဆောင်မှုဖြစ်သည့် [Co-op Translator](https://github.com/Azure/co-op-translator) ကို အသုံးပြု၍ ဘာသာပြန်ထားပါသည်။ ကျွန်ုပ်တို့သည် တိကျမှန်ကန်စေရန် ကြိုးပမ်းသော်လည်း အလိုအလျောက် ဘာသာပြန်ချက်များတွင် အမှားများ သို့မဟုတ် တိကျမှုမရှိမှုများ ပါဝင်နိုင်ကြောင်း သတိပြုပါ။ မူလစာတမ်းကို မူလဘာသာဖြင့်သာ အာမခံရင်းမြစ် (authoritative source) အဖြစ် ယူဆသင့်ပါသည်။ အရေးပါသော အချက်အလက်များအတွက် ပရော်ဖက်ရှင်နယ် လူ့ဘာသာပြန်ကို အသုံးပြုရန် အကြံပြုပါသည်။ ဤဘာသာပြန်ချက်ကို အသုံးပြုခြင်းကြောင့် ဖြစ်ပေါ်လာသော နားလည်မှားခြင်းများ သို့မဟုတ် မှားယွင်းသော အဓိပ္ပာယ်ဖော်ပြချက်များအတွက် ကျွန်ုပ်တို့မှာ တာဝန်မရှိပါ။
<!-- CO-OP TRANSLATOR DISCLAIMER END -->