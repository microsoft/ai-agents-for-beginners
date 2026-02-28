---
name: microsoft-docs
description: అధికారిక Microsoft డాక్యుమెంటేషన్‌ను ప్రశ్నించి Azure, .NET, Agent Framework,
  Aspire, VS Code, GitHub మరియు మరెన్నో అంశాలపై కాన్సెప్ట్‌లు, ట్యుటోరియల్స్ మరియు
  కోడ్ ఉదాహరణలను కనుగొనండి. డిఫాల్ట్‌గా Microsoft Learn MCP ను ఉపయోగిస్తుంది; learn.microsoft.com
  వెలుపల ఉన్న కంటెంట్ కోసం Context7 మరియు Aspire MCP ను ఉపయోగిస్తుంది.
---
# Microsoft Docs

Microsoft సాంకేతిక పరిసరానికి సంబంధించి అన్వేషణ నైపుణ్యం. ఇది learn.microsoft.comని మరియు దీని బయట ఉన్న డాక్యుమెంటేషన్‌ను కవర్ చేస్తుంది (VS Code, GitHub, Aspire, Agent Framework రిపోస్).

---

## Default: Microsoft Learn MCP

ఈ టూల్స్‌ను **learn.microsoft.com** పైని ప్రతి విషయానికి ఉపయోగించండి — Azure, .NET, M365, Power Platform, Agent Framework, Semantic Kernel, Windows, మరియు ఇతరవి. మైక్రోసాఫ్ట్ డాక్యుమెంటేషన్ ప్రశ్నల పెద్ద భాగానికి ఇది ప్రధాన టూల్.

| Tool | Purpose |
|------|---------|
| `microsoft_docs_search` | Search learn.microsoft.com — సిద్ధాంతాలు, మార్గదర్శకాలు, పాఠాలు, కాన్ఫిగరేషన్ |
| `microsoft_code_sample_search` | Learn డాక్స్ నుండి పనిచేసే కోడ్ స్నిపెట్లు కనుగొనండి. ఉత్తమ ఫలితాల కోసం `language` (`python`, `csharp`, etc.) అందించండి |
| `microsoft_docs_fetch` | నిర్దిష్ట URL నుండి పేజీ యొక్క పూర్తి కంటెంట్ పొందండి (శోధన ఉద్ఘాటనలు పరిమితమైనప్పుడు) |

పూర్తి ట్యుటోరియల్స్, అన్ని కాన్ఫిగ్ ఆప్షన్లు అవసరమైతే లేదా శోధన ఉద్ఘాటనలు కట్ చేసేవిగా ఉంటే శోధన తర్వాత `microsoft_docs_fetch`ని ఉపయోగించండి.

---

## Exceptions: When to Use Other Tools

ఉద్దేశించిన వర్గాలు **learn.microsoft.com** బైటలో ఉంటాయి. ఆ ప్రాంతాలకు పక్కన పేర్కొన్న టూల్‌ను ఉపయోగించండి.

### .NET Aspire — Use Aspire MCP Server (preferred) or Context7

Aspire డాక్స్ **aspire.dev**పై ఉంటాయి, Learnలో కాదు. మీ Aspire CLI సంస్కరణపై ఉత్తమ టూల్ ఆధారపడుతుంది:

**CLI 13.2+** (recommended) — Aspire MCP సర్వర్‌లో బిల్ట్-ఇన్ డాక్స్ శోధన టూల్స్ ఉన్నాయి:

| MCP Tool | Description |
|----------|-------------|
| `list_docs` | aspire.dev నుండి అందుబాటులో ఉన్న అన్ని డాక్యుమెంటేషన్‌ను లిస్ట్ చేయి |
| `search_docs` | aspire.dev కంటెంట్ మీద వెయిటెడ్ లెక్సికల్ శోధన |
| `get_doc` | స్లెగ్ ద్వారా నిర్దిష్ట డాక్యూమెంట్‌ని పొందు |

ఇవి Aspire CLI 13.2లో షిప్ అయ్యాయి ([PR #14028](https://github.com/dotnet/aspire/pull/14028)). అప్‌డేట్ చేయడానికి: `aspire update --self --channel daily`. సూచన: https://davidpine.dev/posts/aspire-docs-mcp-tools/

**CLI 13.1** — MCP సర్వర్ ఇన్టిగ్రేషన్ లుక్‌ప్ (`list_integrations`, `get_integration_docs`) అందిస్తుంది కానీ డాక్స్ శోధన అందించదు. ఈ సందర్భాల్లో Context7కు వెనక్కి దిగండి:

| Library ID | Use for |
|---|---|
| `/microsoft/aspire.dev` | ప్రాథమిక — మార్గదర్శకాలు, ఇన్టిగ్రేషన్లు, CLI రిఫరెన్స్, డిప్లాయ్మెంట్ |
| `/dotnet/aspire` | రన్‌టైమ్ సోర్స్ — API అంతర్గతాలు, అమలు వివరాలు |
| `/communitytoolkit/aspire` | కమ్యూనిటీ ఇన్టిగ్రేషన్లు — Go, Java, Node.js, Ollama |

### VS Code — Use Context7

VS Code డాక్స్ **code.visualstudio.com** పై ఉంటాయి, Learnలో కాదు.

| Library ID | Use for |
|---|---|
| `/websites/code_visualstudio` | యూజర్ డాక్స్ — సెట్టింగ్స్, ఫీచర్స్, డీబగ్గింగ్, రిమోట్ డెవ్ |
| `/websites/code_visualstudio_api` | ఎక్స్‌టెన్షన్ API — webviews, TreeViews, commands, contribution points |

### GitHub — Use Context7

GitHub డాక్స్ **docs.github.com** మరియు **cli.github.com**పై ఉంటాయి.

| Library ID | Use for |
|---|---|
| `/websites/github_en` | Actions, API, రిపోస్, సెక్యూరిటీ, అడ్మిన్, Copilot |
| `/websites/cli_github` | GitHub CLI (`gh`) ఆదేశాలు మరియు ఫ్లాగ్‌లు |

### Agent Framework — Use Learn MCP + Context7

Agent Framework ట్యుటోరియల్స్ learn.microsoft.comలో ఉంటాయి (ఉపయోగించండి `microsoft_docs_search`), కానీ **GitHub రేపో** ప్రచురిత డాక్స్ కన్నా తరచుగా ముందస్తుగా ఉంటూ API-స్థాయి వివరణ కలిగి ఉంటుంది — ముఖ్యంగా DevUI REST API రిఫరెన్స్, CLI ఆప్షన్లు, మరియు .NET ఇంటిగ్రేషన్.

| Library ID | Use for |
|---|---|
| `/websites/learn_microsoft_en-us_agent-framework` | ట్యుటోరియల్స్ — DevUI గైడ్లు, ట్రేసింగ్, వర్క్‌ఫ్లో ఆర్కెస్ట్రేషన్ |
| `/microsoft/agent-framework` | API వివరాలు — DevUI REST ఎండ్‌పాయింట్లు, CLI ఫ్లాగ్‌లు, auth, .NET `AddDevUI`/`MapDevUI` |

DevUI సూచన: ఎలా చేయాలో గైడ్ల కోసం ముందుగా Learn వెబ్‌సైట్ మూలాన్ని ప్రశ్నించండి, ఆపై API-స్థాయి ప్రత్యేక వివరాల కోసం (ఎండ్‌పాయింట్ స్కీమాలు, ప్రాక్సీ కాన్ఫిగ్, ఆథ్ టోకెన్లు) రిపో మూలాన్ని చూడండి.

---

## Context7 Setup

ఏదైనా Context7 ప్రశ్న కోసం, సెషన్‌కు ఒకసారి లైబ్రరీ IDని పరిష్కరించండి:

1. టెక్నాలజీ పేరు తో `mcp_context7_resolve-library-id` ను కాల్ చేయండి
2. తిరిగొచ్చిన లైబ్రరీ IDతో మరియు నిర్దిష్ట ప్రశ్నతో `mcp_context7_query-docs` ను కాల్ చేయండి

---

## Writing Effective Queries

స్పష్టంగా ఉండండి — వెర్షన్, ఉద్దేశ్యం, మరియు భాషను చేర్చండి:

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
- **Version** when relevant (`.NET 8`, `Aspire 13`, `VS Code 1.96`)
- **Task intent** (`quickstart`, `tutorial`, `overview`, `limits`, `API reference`)
- **Language** for polyglot docs (`Python`, `TypeScript`, `C#`)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
నిరాకరణ:
ఈ పత్రాన్ని AI అనువాద సేవ (Co-op Translator) ఉపయోగించి అనువదించారు: https://github.com/Azure/co-op-translator. మేము ఖచ్చితత్వాన్ని కల్పించడానికి ప్రయత్నించినప్పటికీ, స్వయంచాలక అనువాదాల్లో పొరపాట్లు లేదా తప్పులు ఉండవచ్చు అని దయచేసి గమనించండి. మూల భాషలో ఉన్న అసలైన పత్రాన్ని అధికారం కలిగిన మూలంగా పరిగణించాలి. కీలకమైన సమాచారానికి వృత్తిపరులైన మానవ అనువాదాన్ని సూచిస్తాం. ఈ అనువాదాన్ని ఉపయోగించడంవల్ల ఏర్పడే ఏవైనా అపార్థాలు లేదా తప్పుగా అర్థం చేసుకోవడాలకు మేము బాధ్యత వహించము.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->