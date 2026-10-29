---
name: microsoft-docs
---
# Microsoft Docs

Microsoft ప్రौద్యోగికీ పరిసరానికి సంబంధించిన పరిశోధన నైపుణ్యం. learn.microsoft.com మరియు దీనికి బయట ఉండే డాక్యుమెంటేషన్ (VS కోడ్, GitHub, Aspire, Agent Framework రిపోజిటరీలు)ను కవర్ చేస్తుంది.

---

## డిఫాల్ట్: Microsoft Learn MCP

**learn.microsoft.com** పై ఉన్న గందరగోళమయిన అంశాలకు — Azure, .NET, M365, Power Platform, Agent Framework, Semantic Kernel, Windows మరియు మరిన్ని విషయాలకు ఈ టూల్స్ ఉపయోగించండి. మైక్రోసాఫ్ట్ డాక్యుమెంటేషన్ ప్రశ్నలకు ఇది ప్రధాన టూల్.

| టూల్ | ప్రయోజనం |
|------|---------|
| `microsoft_docs_search` | learn.microsoft.com లో సెర్చ్ చేయండి — కాన్సెప్ట్‌లు, గైడ్లు, ట్యుటోరియల్స్, కాన్ఫిగరేషన్ |
| `microsoft_code_sample_search` | Learn డాక్‌ల నుండి పని చేసే కోడ్ స్నిపెట్లు కనుగొనండి. ఉత్తమ ఫలితాల కోసం `language` (`python`, `csharp`, మొదలైనవి) పంపండి |
| `microsoft_docs_fetch` | సెర్చ్ ఎర్రిప్ట్స్ సరిపోకపోతే, నిర్దిష్ట URL నుండి పూర్తి పేజీ కంటెంట్ పొందండి |

సెర్చ్ తరువాత `microsoft_docs_fetch` ఉపయోగించండి, మీరు పూర్తి ట్యుటోరియల్స్, అన్ని కాన్ఫిగ్ ఆప్షన్లను కావాలంటే లేదా సెర్చ్ ఎర్రిప్ట్స్ చిన్నగా ఉన్నప్పుడు.

---

## మినహాయింపులు: ఇతర టూల్స్‌ని ఎప్పుడు ఉపయోగించాలి

ఈ క్రింది వర్గాలు **learn.microsoft.com** కు బయట ఉంటాయి. వాటి బదులు సూచించిన టూల్ ఉపయోగించండి.

### Aspire — Aspire MCP Server (ప్రాధాన్యం) లేదా Context7 ఉపయోగించండి

Aspire డాక్స్ **aspire.dev** పై ఉంటాయి, Learn వద్ద కాదు. ఉత్తమ టూల్ మీ Aspire CLI సంస్కరణ పై ఆధారపడుతుంది:

**CLI 13.2+** (సిఫార్సు చేయబడినది) — Aspire MCP సర్వర్ లో అంతర్నిర్మిత డాక్స్ సెర్చ్ టూల్స్ ఉంటాయి:

| MCP టూల్ | వివరణ |
|----------|-------------|
| `list_docs` | aspire.dev నుండి అందుబాటులో ఉన్న అన్ని డాక్యుమెంటేషన్ జాబితా |
| `search_docs` | aspire.dev కంటెంట్ పై వెయిటెడ్ లెక్సికల్ సెర్చ్ |
| `get_doc` | నిర్దిష్ట డాక్యుమెంట్‌ని స్లగ్ ద్వారా పొందండి |

ఇవి Aspire CLI 13.2 ([PR #14028](https://github.com/microsoft/aspire/pull/14028)) లో వస్తాయి. అప్‌డేట్ చేయడానికి: `aspire update --self --channel daily`.

**CLI 13.1** — MCP సర్వర్ ఇన్టిగ్రేషన్ లుకప్ (`list_integrations`, `get_integration_docs`) ఇస్తుంది కానీ డాక్స్ సెర్చ్ అందదు. Context7 కిFallback అవ్వండి:

| లైబ్రరీ ID | ఉపయోగం |
|---|---|
| `/microsoft/aspire.dev` | ప్రాథమికం — గైడ్లు, ఇన్టిగ్రేషన్స్, CLI సూచిక, డిప్లాయ్‌మెంట్ |
| `/microsoft/aspire` | రన్‌టైమ్ మూలం — API లోపలివివరాలు, అమలు వివరాలు |
| `/communitytoolkit/aspire` | కమ్యూనిటీ ఇన్టిగ్రేషన్స్ — Go, Java, Node.js, Ollama |

### VS కోడ్ — Context7 ఉపయోగించండి

VS కోడ్ డాక్స్ **code.visualstudio.com** పై ఉంటాయి, Learn దగ్గరకు కాదు.

| లైబ్రరీ ID | ఉపయోగం |
|---|---|
| `/websites/code_visualstudio` | వాడుకరి డాక్స్ — సెట్టింగ్స్, ఫీచర్స్, డీబగ్గింగ్, రిమోట్ డెవ్ |
| `/websites/code_visualstudio_api` | ఎక్స్టెన్షన్ API — వెబ్‌వ్యూస్, TreeViews, క‌మాండ్లు, కాంట్రిబ్యూషన్ పాయింట్లు |

### GitHub — Context7 ఉపయోగించండి

GitHub డాక్స్ **docs.github.com** మరియు **cli.github.com** పైన ఉంటాయి.

| లైబ్రరీ ID | ఉపయోగం |
|---|---|
| `/websites/github_en` | యాక్షన్లు, API, రిపోజిటరీలు, సెక్యూరిటీ, అడ్మిన్, Copilot |
| `/websites/cli_github` | GitHub CLI (`gh`) క‌మాండ్లు మరియు ఫ్లాగ్స్ |

### Agent Framework — Learn MCP + Context7 ఉపయోగించండి

Agent Framework ట్యుటోరియల్స్ learn.microsoft.com(లో ఉంటాయి (`microsoft_docs_search` ఉపయోగించండి), కానీ **GitHub రిపో**లో డాక్స్ కంటే ముందుగానే API స్థాయి వివరాలు ఉంటాయి — ప్రత్యేకంగా DevUI REST API సూచిక, CLI ఎంపికలు, మరియు .NET ఇన్టిగ్రేషన్.

| లైబ్రరీ ID | ఉపయోగం |
|---|---|
| `/websites/learn_microsoft_en-us_agent-framework` | ట్యుటోరియల్స్ — DevUI గైడ్లు, ట్రేసింగ్, వర్క్‌ఫ్లో ఆర్కెస్ట్రేషన్ |
| `/microsoft/agent-framework` | API వివరాలు — DevUI REST ఎండ్‌పాయింట్లు, CLI ఫ్లాగ్స్, ఆథ్, .NET `AddDevUI`/`MapDevUI` |

**DevUI సూచన:** ఉపయోగించే విధాన గైడ్ల కోసం Learn వెబ్‌సైట్ సోర్స్‌ని ప్రశ్నించండి, తరువాత API స్థాయి వివరాలకు రిపో సోర్స్ (ఎండ్‌పాయింట్ స్కీమాలు, ప్రాక్సీ కాన్ఫిగర్, ఆథ్ టోకెన్లు) చూడండి.

---

## Context7 సెట్‌అప్

ఏ Context7 ప్రశ్న కోసం, ముందుగా లైబ్రరీ ID పరిష్కరించండి (ప్రతి సెషన్ కి ఒకసారి):

1. టెక్నాలజీ పేరు తో `mcp_context7_resolve-library-id` పిలవండి
2. రాబోయే లైబ్రరీ ID తో మరియు నిర్దిష్ట ప్రశ్న తో `mcp_context7_query-docs` పిలవండి

---

## సమర్థవంతమైన ప్రశ్నలు రాయడం

స్పష్టంగా ఉండండి — సంస్కరణ, ఉద్దేశ్యం, మరియు భాషను చేర్చండి:

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

సందర్భాన్ని చేర్చండి:
- **సంస్కరణ** అవసరమైతే (`.NET 8`, `Aspire 13`, `VS Code 1.96`)
- **పని ఉద్దేశ్యం** (`quickstart`, `tutorial`, `overview`, `limits`, `API reference`)
- **భాష** బహుభాషా డాక్స్ కోసం (`Python`, `TypeScript`, `C#`)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**అస్వీకరణ**:
ఈ పత్రం AI అనువాద సేవ [Co-op Translator](https://github.com/Azure/co-op-translator) ఉపయోగించి అనువదించబడింది. మేము ఖచ్చితత్వానికి ప్రయత్నిస్తున్నప్పటికీ, ఆటోమేటెడ్ అనువాదాలు తప్పులు లేదా అసమగ్రతలను కలిగి ఉండవచ్చు. దాని స్వదేశ భాషలో ఉన్న అసలు పత్రాన్ని అధికారం కలిగిన మూలంగా పరిగణించాలి. కీలకమైన సమాచారం కోసం, ప్రొఫెషనల్ మానవ అనువాదాన్ని సిఫారసు చేస్తాము. ఈ అనువాదం ఉపయోగం వల్ల కలిగే ఏవైనా అపార్థాలు లేదా తప్పుదారులు కోసం మేము బాధ్యత వహించము.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->