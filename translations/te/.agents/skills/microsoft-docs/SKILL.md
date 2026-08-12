---
name: microsoft-docs
description: Microsoft యొక్క అధికారిక డాక్యుమెంటేషన్‌ను పరిశీలించి Azure, .NET, Agent
  Framework, Aspire, VS Code, GitHub మరియు మరెన్నో అంశాలకు సంబంధించిన కాన్సెప్ట్స్,
  ట్యుటోరియల్స్ మరియు కోడ్ ఉదాహరణలను కనుగొనండి. డిఫాల్ట్‌గా Microsoft Learn MCP ను
  ఉపయోగిస్తుంది, learn.microsoft.com వెలుపల ఉన్న కంటెంట్ కోసం Context7 మరియు Aspire
  MCP ను ఉపయోగిస్తుంది.
---
# Microsoft డాక్స్

Microsoft టెక్నాలజీ ఎకోసిస్టమ్ కోసం శోధన నైపుణ్యం. ఇది learn.microsoft.com మరియు దానిపై కాకుండా ఉన్న డాక్యుమెంటేషన్ (VS Code, GitHub, Aspire, Agent Framework రిపోజిటరీలు) ను కవర్ చేస్తుంది.

---

## డిఫాల్ట్: Microsoft Learn MCP

ఈ టూల్స్‌ను **learn.microsoft.comలో ఉన్న అన్నిటికీ** ఉపయోగించండి — Azure, .NET, M365, Power Platform, Agent Framework, Semantic Kernel, Windows, మరియు ఇతరవి. ఇది మైక్రోసాఫ్ట్ డాక్యుమెంటేషన్ ప్రశ్నల కోసం ప్రధాన టూల్.

| Tool | Purpose |
|------|---------|
| `microsoft_docs_search` | learn.microsoft.com ని శోధించండి — భావనలు, గైడ్లు, ట్యుటోరియల్స్, కాన్ఫిగరేషన్ |
| `microsoft_code_sample_search` | Learn డాక్స్ నుంచి పనిచేసే కోడ్ స్నిపెట్లు కనుగొనండి. ఉత్తమ ఫలితాల కోసం `language` (`python`, `csharp`, మొదలైనవి) ఇవ్వండి |
| `microsoft_docs_fetch` | ఒక నిర్దిష్ట URL నుండి పూర్తి పేజీ కంటెంట్ పొందండి (శోధన సంక్షిప్తాలు చాలనప్పుడు) |

పూర్తి ట్యుటోరియల్స్, అన్ని కాన్ఫిగ్ ఎంపికలు కావాలంటే లేదా శోధన సంక్షిప్తాలు తిడకబడ్డప్పుడు `microsoft_docs_fetch` ను శోధన తర్వాత ఉపయోగించండి.

---

## ఎంపికలు: ఇతర టూల్స్ ఎప్పుడు ఉపయోగించాలి

క్రింది వర్గాలు **learn.microsoft.comకి బయట** ఉన్నాయి. బదులుగా పేర్కొన్న టూల్‌ను ఉపయోగించండి.

### .NET Aspire — Aspire MCP Server (పసందైనది) లేదా Context7 ఉపయోగించండి

Aspire డాక్స్ **aspire.dev** పై ఉంటాయి, Learn పై కాదు. ఉత్తమ టూల్ మీ Aspire CLI వెర్షన్‌పై ఆధారపడుతుంది:

**CLI 13.2+** (సిఫార్సు) — Aspire MCP సర్వర్ బిల్ట్-ఇన్ డాక్స్ శోధన టూల్స్‌ను కలిగి ఉంటుంది:

| MCP Tool | Description |
|----------|-------------|
| `list_docs` | aspire.dev నుండి అందుబాటులో ఉన్న అన్ని డాక్యుమెంటేషన్లను జాబితా చేస్తుంది |
| `search_docs` | aspire.dev కంటెంట్‌పై బరువు-ఆధారిత లెక్సికల్ శోధన |
| `get_doc` | స్లగ్ ద్వారా ఒక నిర్దిష్ట డాక్యుమెంట్‌ను పొందుతుంది |

ఇవి Aspire CLI 13.2లో వస్తాయి ([PR #14028](https://github.com/dotnet/aspire/pull/14028)). అప్‌డేట్ చేయడానికి: `aspire update --self --channel daily`. సూచన: https://davidpine.dev/posts/aspire-docs-mcp-tools/

**CLI 13.1** — MCP సర్వర్ ఇంటిగ్రేషన్ లుకప్ (`list_integrations`, `get_integration_docs`) అందిస్తుంది కానీ డాక్స్ శోధన ఇవ్వదు. Context7కి fallback చేయండి:

| Library ID | Use for |
|---|---|
| `/microsoft/aspire.dev` | Primary — గైడ్లు, ఇంటిగ్రేషన్లు, CLI సూచిక, డిప్లాయ్మెంట్ |
| `/dotnet/aspire` | Runtime source — API అంతర్గతాలు, అమలు వివరాలు |
| `/communitytoolkit/aspire` | Community integrations — Go, Java, Node.js, Ollama |

### VS Code — Context7 ఉపయోగించండి

VS Code డాక్స్ **code.visualstudio.com** పై ఉంటాయి, Learn పై కాదు.

| Library ID | Use for |
|---|---|
| `/websites/code_visualstudio` | User docs — సెట్టింగ్స్, ఫీచర్లు, డీబగ్గింగ్, రిమోట్ డెవలప్‌మెంట్ |
| `/websites/code_visualstudio_api` | Extension API — webviews, TreeViews, కమాండ్లు, contribution points |

### GitHub — Context7 ఉపయోగించండి

GitHub డాక్స్ **docs.github.com** మరియు **cli.github.com** పై ఉంటాయి.

| Library ID | Use for |
|---|---|
| `/websites/github_en` | Actions, API, రిపోజిటరీలు, భద్రత, అడ్మిన్, Copilot |
| `/websites/cli_github` | GitHub CLI (`gh`) కమాండ్లు మరియు ఫ్లాగ్‌లు |

### Agent Framework — Learn MCP + Context7 ఉపయోగించండి

Agent Framework ట్యుటోరియల్స్ learn.microsoft.com పై ఉంటాయి (`microsoft_docs_search` ఉపయోగించండి), కానీ **GitHub repo** API-స్థాయి వివరాలు అందిస్తుంది, ఇవి తరచుగా ప్రచురించే డాక్స్ కంటే ముందుంటాయి — ముఖ్యంగా DevUI REST API reference, CLI ఎంపికలు, మరియు .NET ఇంటిగ్రేషన్.

| Library ID | Use for |
|---|---|
| `/websites/learn_microsoft_en-us_agent-framework` | Tutorials — DevUI గైడ్లు, ట్రేసింగ్, వర్క్‌ఫ్లో ఆర్కెస్ట్రేషన్ |
| `/microsoft/agent-framework` | API detail — DevUI REST ఎండ్పాయింట్లు, CLI ఫ్లాగ్‌లు, auth, .NET `AddDevUI`/`MapDevUI` |

**DevUI సూచన:** ఎలా చేయాలో గైడ్లు కోసం Learn వెబ్‌సైట్ సోర్స్‌ను கேయిర్చండి, తరువాత API-స్థాయి స్పెసిఫిక్స్ కోసం repo సోర్స్‌ని చూడండి (ఎండ్పాయింట్ స్కీమాలు, ప్రాక్సీ కాన్ఫిగ్, auth టోకెన్లు).

---

## Context7 సెటప్

ఏ Context7 ప్రశ్నకైనా, ముందుగా లైబ్రరీ IDని పరిష్కరించండి (సెషన్‌కు ఒక్కసారి):

1. టెక్నాలజీ పేరు తో `mcp_context7_resolve-library-id` ని కాల్ చేయండి
2. తిరిగి వచ్చిన లైబ్రరీ ID మరియు నిర్దిష్ట ప్రశ్నతో `mcp_context7_query-docs` ని కాల్ చేయండి

---

## ప్రభావవంతమైన ప్రశ్నలు రాయడం

స్పష్టంగా ఉండండి — వెర్షన్, ఉద్దేశ్యం, మరియు భాషని చేర్చండి:

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
- **వర్షన్** సంబంధితప్పుడు (`.NET 8`, `Aspire 13`, `VS Code 1.96`)
- **పని ఉద్దేశ్యం** (`quickstart`, `tutorial`, `overview`, `limits`, `API reference`)
- **భాష** బహుభాషా డాక్స్ కోసం (`Python`, `TypeScript`, `C#`)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
అస్వీకరణ:

ఈ పత్రాన్ని AI అనువాద సేవ అయిన Co-op Translator (https://github.com/Azure/co-op-translator) ద్వారా అనువదించబడింది. మేము ఖచ్చితత్వానికి ప్రయత్నించినప్పటికీ, స్వయంచాలిత అనువాదాల్లో పొరపాట్లు లేదా లోపాలు ఉండొచ్చు గనుక దయచేసి అర్థం చేసుకోండి. స్థానిక భాషలోని మూల పత్రాన్ని అధికారిక మూలంగా పరిగణించాలి. కీలకమైన సమాచారానికి వృత్తిపరమైన మానవ అనువాదాన్ని సూచిస్తాము. ఈ అనువాదం వాడకం వల్ల ఏర్పడే ఏవైనా అపసమజ్ఞతలు లేదా తప్పుగా అర్థం చేసుకోవడాలకు మేము బాధ్యులు కాదు.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->