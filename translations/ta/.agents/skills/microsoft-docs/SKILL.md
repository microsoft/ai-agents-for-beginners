---
name: microsoft-docs
description: Azure, .NET, Agent Framework, Aspire, VS Code, GitHub மற்றும் மேலும்
  பலவற்றை சார்ந்த கருத்துகள், பயிற்சிகள் மற்றும் குறியீட்டு எடுத்துக்காட்டுகளை கண்டறிய
  அதிகாரப்பூர்வ Microsoft ஆவணங்களை விசாரணை செய்க. இயல்புநிலையாக Microsoft Learn MCP-ஐ
  பயன்படுத்துகிறது; learn.microsoft.com-க்கு வெளியிலுள்ள உள்ளடக்கத்திற்காக Context7
  மற்றும் Aspire MCP-ஐப் பயன்படுத்துகிறது.
---
# Microsoft ஆவணங்கள்

Microsoft தொழில்நுட்ப சூழலுக்கான ஆய்வு திறன். learn.microsoft.com மற்றும் அதற்குப் புறம் இருக்கும் ஆவணங்களை (VS Code, GitHub, Aspire, Agent Framework репோஸ்) カவரும்.

---

## இயல்புநிலை: Microsoft Learn MCP

**learn.microsoft.com இல் உள்ள அனைத்திற்கும்** இந்த கருவிகளை பயன்படுத்துக — Azure, .NET, M365, Power Platform, Agent Framework, Semantic Kernel, Windows மற்றும் மேலும் பல. இது பெரும்பாலான Microsoft ஆவணக் கேள்விகளுக்கான முதன்மையான கருவியாகும்.

| Tool | Purpose |
|------|---------|
| `microsoft_docs_search` | learn.microsoft.com ஐத் தேடுக — கருத்துகள், வழிகாட்டிகள், பாடநெறிகள், கட்டமைப்பு |
| `microsoft_code_sample_search` | Learn ஆவணங்களில் இருந்து செயல்படும் குறியீடு குறும்பகுதிகளை கண்டுபிடிக்கவும். சிறந்த முடிவுகளுக்காக `language` (`python`, `csharp`, etc.) கொடுக்கவும் |
| `microsoft_docs_fetch` | ஒரு குறிப்பிட்ட URL-இலிருந்து முழு பக்க உள்ளடக்கத்தைப் பெறுக (தேடல் சுருக்கங்கள் போதுமானதாக இல்லையெனில்) |

முழுமையான பாடநெறிகள், அனைத்து கட்டமைப்பு விருப்பங்கள் அல்லது தேடல் சுருக்கங்கள் வெட்டப்பட்டுள்ள போது தேடலுக்குப் பிறகு `microsoft_docs_fetch` ஐ பயன்படுத்தவும்.

---

## விதிவிலக்குகள்: வேறு கருவிகள் எப்போது பயன்படுத்துவது

பின்வரும் பிரிவுகள் **learn.microsoft.com இற்கு வெளியே** உள்ளன. பதிலுக்கு குறிப்பிடப்பட்ட கருவியைப் பயன்படுத்தவும்.

### .NET Aspire — Aspire MCP Server (முன்னுரிமை) அல்லது Context7 ஐ பயன்படுத்தவும்

Aspire ஆவணங்கள் **aspire.dev** இல் பிரசுரிக்கப்படுகின்றன, Learn இல் அல்ல. சிறந்த கருவி உங்கள் Aspire CLI பதிப்பின் மீது பொருந்தும்:

**CLI 13.2+** ( பரிந்துரைக்கப்படுகிறது ) — Aspire MCP சேவையகம் கட்டமைக்கப்பட்ட docs தேடல் கருவிகளை உள்ளடக்குகிறது:

| MCP Tool | Description |
|----------|-------------|
| `list_docs` | aspire.dev இல் உள்ள அனைத்து கிடைக்கும் ஆவணங்களையும் பட்டியலிடுகிறது |
| `search_docs` | aspire.dev உள்ளடக்கத்தின் முழுவதும் எடைப்பட்ட எழுத்துத் தேடலைச் செய்கிறது |
| `get_doc` | ஒரு குறிப்பிட்ட ஆவணத்தை slug மூலம் பெறுகிறது |

இவை Aspire CLI 13.2 இல் அடங்கಿವೆ ([PR #14028](https://github.com/dotnet/aspire/pull/14028)). புதுப்பிக்க: `aspire update --self --channel daily`. Ref: https://davidpine.dev/posts/aspire-docs-mcp-tools/

**CLI 13.1** — MCP சேவையகம் ஒருங்கிணைப்பு தேடலை (`list_integrations`, `get_integration_docs`) வழங்குகிறது ஆனால் docs தேடலை வழங்காது. Context7க்கு மறு வழியாக செல்லவும்:

| Library ID | Use for |
|---|---|
| `/microsoft/aspire.dev` | முதன்மை — வழிகாட்டிகள், ஒருங்கிணைப்புகள், CLI குறிப்பு, நிறுவல் |
| `/dotnet/aspire` | ரன்டைம் மூலம் — API உள் அம்சங்கள், அமலாக்க விவரங்கள் |
| `/communitytoolkit/aspire` | சமூக ஒருங்கிணைப்புகள் — Go, Java, Node.js, Ollama |

### VS Code — Context7 பயன்படுத்தவும்

VS Code ஆவணங்கள் **code.visualstudio.com** இல் இருக்கும், Learn இல் அல்ல.

| Library ID | Use for |
|---|---|
| `/websites/code_visualstudio` | பயனர் ஆவணங்கள் — அமைப்புகள், அம்சங்கள், பிழைத் தேடல், தூர அபிவிருத்தி |
| `/websites/code_visualstudio_api` | நீட்டிப்பு API — webviews, TreeViews, commands, contribution points |

### GitHub — Context7 பயன்படுத்தவும்

GitHub ஆவணங்கள் **docs.github.com** மற்றும் **cli.github.com** இல் உள்ளன.

| Library ID | Use for |
|---|---|
| `/websites/github_en` | Actions, API, repos, பாதுகாப்பு, நிர்வாகம், Copilot |
| `/websites/cli_github` | GitHub CLI (`gh`) கட்டளைகள் மற்றும் கொடிகள் |

### Agent Framework — Learn MCP + Context7 ஐ பயன்படுத்தவும்

Agent Framework பாடநெறிகள் learn.microsoft.com இல் உள்ளது (பயன்படுத்த `microsoft_docs_search`), ஆனால் **GitHub repo** வெளியிடப்பட்ட ஆவணங்களைவிட பலமுறை முன்னேறிய API-நிலை விபரங்களை கொண்டுள்ளது — குறிப்பாக DevUI REST API குறிப்பு, CLI விருப்பங்கள் மற்றும் .NET ஒருங்கிணைவு.

| Library ID | Use for |
|---|---|
| `/websites/learn_microsoft_en-us_agent-framework` | பாடநெறிகள் — DevUI வழிகாட்டிகள், டிரேசிங், வேலை ஓட்ட ஒழுங்கமைப்பு |
| `/microsoft/agent-framework` | API விவரம் — DevUI REST இறுதிக்கருத்துகள், CLI கொடிகள், அங்கீகாரம், .NET `AddDevUI`/`MapDevUI` |

DevUI குறிப்பு: how-to வழிகாட்டிகளுக்கு Learn இணையதளத்தின் மூலத்தை வினவவும், பின்னர் API-நிலை குறிப்புகளுக்காக repo மூலத்தை வினவவும் (எண்ட்பாயிண்ட் ஸ்கீமாஸ், proxy கட்டமைப்பு, அங்கீகார டோக்கன்கள்).

---

## Context7 அமைப்பு

எந்த Context7 வினாவுக்கும், முதலில் library ID யை தீர்மானிக்கவும் (ஒரு அமர்வுக்கு ஒரு முறை):

1. Call `mcp_context7_resolve-library-id` with the technology name
2. Call `mcp_context7_query-docs` with the returned library ID and a specific query

---

## பயனுள்ள கேள்விகள் எழுதுதல்

குறிப்பாக இருங்கள் — பதிப்பு, நோக்கம் மற்றும் மொழியை உள்ளடக்குங்கள்:

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

Include context:
- **பதிப்பு** when relevant (`.NET 8`, `Aspire 13`, `VS Code 1.96`)
- **பணியின் நோக்கம்** (`quickstart`, `tutorial`, `overview`, `limits`, `API reference`)
- **மொழி** for polyglot docs (`Python`, `TypeScript`, `C#`)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
மறுப்பு:
இந்த ஆவணம் AI மொழிபெயர்ப்பு சேவையாகிய Co-op Translator (https://github.com/Azure/co-op-translator) மூலம் மொழிபெயர்க்கப்பட்டது. நாங்கள் துல்லியத்திற்காக முயற்சித்தாலும், தானியங்கி மொழிபெயர்ப்புகளில் பிழைகள் அல்லது தவறுகள் இருக்கலாம் என்பதை தயவுசெய்து கவனியுங்கள். அதன் சொந்த மொழியில் உள்ள மூல ஆவணத்தை அதிகாரபூர்வ ஆதாரமாக கருத வேண்டும். முக்கியமான தகவல்களுக்கு, தொழில்முறை மனித மொழிபெயர்ப்பை பரிந்துரைக்கின்றோம். இந்த மொழிபெயர்ப்பைப் பயன்படுத்தியதனால் ஏற்பட்ட எந்தவொரு தவறான புரிதல்களிற்கோ தவறான விளக்கங்களிற்கோ நாங்கள் பொறுப்பேற்கமாட்டோம்.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->