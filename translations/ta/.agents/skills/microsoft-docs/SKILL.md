---
name: microsoft-docs
description: Azure, .NET, Agent Framework, Aspire, VS Code, GitHub மற்றும் பலவற்றைக்குழுவாகக்
  கொண்ட அதிகாரப்பூர்வ Microsoft ஆவணங்களைக் கேள்வி செய்து கொள்கின்றது. பொதுவாக Microsoft
  Learn MCP ஐ பயன்படுத்துகிறது, மேலும் learn.microsoft.com வெளியே வசிக்கும் உள்ளடக்கத்திற்காக
  Context7 மற்றும் Aspire MCP ஐ பயன்படுத்துகிறது.
---
# Microsoft Docs

Microsoft தொழில்நுட்ப சுற்றுச்சூழலுக்கான ஆராய்ச்சி திறன். learn.microsoft.com மற்றும் அதற்கு வெளியே இருக்கும் டாக்குமென்டேஷன் (VS Code, GitHub, Aspire, Agent Framework பதிவுகள்) ஆகியவற்றை உள்ளடக்குகிறது.

---

## இயல்புநிலை: Microsoft Learn MCP

**learn.microsoft.com இல் உள்ள அனைத்துக்கும்** இவற்றை பயன்படுத்துங்கள் — Azure, .NET, M365, Power Platform, Agent Framework, Semantic Kernel, Windows மற்றும் பல. இது பெருமட்டான Microsoft டாக்குமென்டேஷன் விசாரணைகளுக்கான பிரதான கருவி ஆகும்.

| கருவி | பயன்பாடு |
|------|---------|
| `microsoft_docs_search` | learn.microsoft.com இல் தேடல் — கருத்துகள், வழிகாட்டிகள், படிப்பறைகள், கட்டமைப்பு |
| `microsoft_code_sample_search` | Learn டாக்குமென்ட்களில் இருந்து செயல்படுத்தும் குறியீட்டு துணுக்குகள் கண்டுபிடி. சிறந்த முடிவுகளுக்கு `language` (`python`, `csharp`, போன்றவை) பயன்படுத்தவும் |
| `microsoft_docs_fetch` | குறிப்பிட்ட URL இல் இருந்து முழு பக்கம் உள்ளடக்கத்தை பெற (தேடல் துணுக்குகள் போதவில்லை என்றால்) |

தேவைப்பட்டால் முழுமையான படிப்பறைகள், அனைத்து கட்டமைப்பு விருப்பங்கள் அல்லது தேடல் துணுக்குகள் குறைக்கப்பட்டால் தேடலைத் தொடர்ந்து `microsoft_docs_fetch` பயன்படுத்தவும்.

---

## விதிவிலக்குகள்: பிற கருவிகளை எப்போது பயன்படுத்துவது

கீழ்க்காணும் வகைகள் **learn.microsoft.com க்குக் வெளியே** உள்ளன. பதிலுக்கு குறிப்பிடப்பட்ட கருவியை பயன்படுத்துங்கள்.

### Aspire — Aspire MCP Server (விருப்பமானது) அல்லது Context7 பயன்படுத்தவும்

Aspire டாக்குமென்ட்கள் **aspire.dev** இல் உள்ளன, Learn இல் அல்ல. சிறந்த கருவி உங்கள் Aspire CLI பதிப்பின் அடிப்படையில் இருக்கும்:

**CLI 13.2+** (பரிந்துரைக்கப்படுகிறது) — Aspire MCP சேவையகம் உள்ளடக்கிய டாக்குமென்ட் தேடல் கருவிகளை கொண்டுள்ளது:

| MCP கருவி | விளக்கம் |
|----------|-------------|
| `list_docs` | aspire.dev இல் உள்ள அனைத்து கிடைக்கும் டாக்குமென்டேஷனையும் பட்டியலிடுகிறது |
| `search_docs` | aspire.dev உள்ளடக்கத்தில் பண்புக்கு உட்பட்ட சொற்பொழிவுத் தேடல் |
| `get_doc` | சிறப்பு ஆவணத்தை slug மூலம் பெறுகிறது |

இது Aspire CLI 13.2 இல் மையமாக உள்ளது ([PR #14028](https://github.com/microsoft/aspire/pull/14028)). புதுப்பிக்க: `aspire update --self --channel daily`.

**CLI 13.1** — MCP சேவையகம் ஒருங்கிணைப்பு தேடலை வழங்குகிறது (`list_integrations`, `get_integration_docs`) ஆனால் **டாக்குமென்ட் தேடலை வழங்கவில்லை**. Context7 ஐ fallback ஆக பயன்படுத்தவும்:

| நூலக ID | பயன்பாடு |
|---|---|
| `/microsoft/aspire.dev` | முதன்மை — வழிகாட்டிகள், ஒருங்கிணைப்புகள், CLI குறிக்கோள், பிணைக்கல் |
| `/microsoft/aspire` | இயக்க நேர மூலக்கோடு — API உள் விவரங்கள், அமல்படுத்தும் விவரங்கள் |
| `/communitytoolkit/aspire` | சமூக ஒருங்கிணைப்புகள் — Go, Java, Node.js, Ollama |

### VS Code — Context7 பயன்படுத்தவும்

VS Code டாக்குமென்ட்கள் **code.visualstudio.com** இல் உள்ளன, Learn இல் அல்ல.

| நூலக ID | பயன்பாடு |
|---|---|
| `/websites/code_visualstudio` | பயனர் டாக்குமென்ட் — அமைப்புகள், அம்சங்கள், பிழைத்திருத்தம், தொலைநிலை dev |
| `/websites/code_visualstudio_api` | விரிவாக்க API — இணைய காட்சிகள், TreeViews, கட்டளைகள், பங்களிப்பு புள்ளிகள் |

### GitHub — Context7 பயன்படுத்தவும்

GitHub டாக்குமென்ட் **docs.github.com** மற்றும் **cli.github.com** இல் உள்ளது.

| நூலக ID | பயன்பாடு |
|---|---|
| `/websites/github_en` | செயலிகள், API, பதிப்புகள், பாதுகாப்பு, நிர்வாகம், Copilot |
| `/websites/cli_github` | GitHub CLI (`gh`) கட்டளைகள் மற்றும் கொடி முடிச்சுகள் |

### Agent Framework — Learn MCP + Context7 பயன்படுத்தவும்

Agent Framework படிப்பறைகள் learn.microsoft.com இல் உள்ளன ( `microsoft_docs_search` பயன்படுத்தவும்), ஆனால் **GitHub பதிவகம்** பொதுவாக வெளியிடப்பட்ட டாக்குமென்ட்களை விட API நிலை விவரங்களை, குறிப்பாக DevUI REST API குறிப்பு, CLI விருப்பங்கள் மற்றும் .NET ஒருங்கிணைப்பு முன்னோக்கி வழங்குகிறது.

| நூலக ID | பயன்பாடு |
|---|---|
| `/websites/learn_microsoft_en-us_agent-framework` | படிப்பறைகள் — DevUI வழிகாட்டிகள், கண்காணித்தல், பணிச் செயல் ஒழுங்கமைப்பு |
| `/microsoft/agent-framework` | API விவரம் — DevUI REST காட்சிகள், CLI கொடிகள், அங்கீகாரம், .NET `AddDevUI`/`MapDevUI` |

**DevUI குறிப்பு:** எப்படி செய்வது வழிகாட்டிகளுக்காக Learn வலைத்தள மூலத்தை வினவவும், பிறகு API நிலை விவரங்களுக்கு (எնդ்பாயிண்ட் திட்டங்கள், பிரதிநிதித்துவ கட்டமைப்பு, அங்கீகார டோக்கன்கள்) பதிவகம் மூலத்தைப் பயன்படுத்தவும்.

---

## Context7 அமைப்பு

எந்த Context7 விசாரணைக்கும், முதலில் நூலக ID ஐ தீர்மானிக்கவும் (ஒன்று குறிப்பாக ஒவ்வொரு அமர்வுக்கும்):

1. தொழில்நுட்ப பெயரை கொண்டு `mcp_context7_resolve-library-id` ஐ அழைக்கவும்
2. கிடைத்த நூலக ID மற்றும் குறிப்பிட்ட விசாரணையுடன் `mcp_context7_query-docs` ஐ அழைக்கவும்

---

## திறமையான விசாரணைகள் எழுதுதல்

குறிப்பாக இருங்கள் — பதிப்பு, நோக்கம் மற்றும் மொழியைச் சேர்க்கவும்:

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

குறிக்கோள் சேர்க்கவும்:
- பொருத்தமான போது **பதிப்பு** (`.NET 8`, `Aspire 13`, `VS Code 1.96`)
- **பணி நோக்கம்** (`quickstart`, `tutorial`, `overview`, `limits`, `API reference`)
- பலமொழி டாக்குமென்டுகளுக்கான **மொழி** (`Python`, `TypeScript`, `C#`)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**மறுப்பு**:
இந்த ஆவணம் AI மொழிபெயர்ப்பு சேவை [Co-op Translator](https://github.com/Azure/co-op-translator) பயன்படுத்தி மொழிபெயர்க்கப்பட்டுள்ளது. நாங்கள் துல்லியத்திற்காக முயற்சி செய்துள்ளோம், ஆனால் தானாக செய்யப்படும் மொழிபெயர்ப்புகளில் பிழைகள் அல்லது தவறுகள் இருக்கலாம் என்பதை கவனத்தில் கொள்ளவும். அசல் ஆவணம் அதன் தாய்மொழியில் அதிகாரப்பூர்வ ஆதாரமாக கருதப்பட வேண்டும். முக்கியமான தகவல்களுக்கு, தொழில்நுட்பமான மனித மொழிபெயர்ப்பு பரிந்துரைக்கப்படுகிறது. இந்த மொழிபெயர்ப்பைப் பயன்படுத்துவதால் ஏற்படும் எந்த தவறான புரிதல்கள் அல்லது தவறான விளக்கத்திற்கும் நாங்கள் பொறுப்பில்வில்லை.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->