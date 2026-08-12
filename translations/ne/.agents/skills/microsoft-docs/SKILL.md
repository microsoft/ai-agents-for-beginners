---
name: microsoft-docs
description: आधिकारिक Microsoft दस्तावेजहरूमा सोधपुछ गरेर Azure, .NET, Agent Framework,
  Aspire, VS Code, GitHub र अन्य थुप्रै क्षेत्रमा लाग्ने अवधारणाहरू, ट्युटोरियलहरू
  र कोड उदाहरणहरू फेला पार्नुहोस्। डिफल्ट रूपमा Microsoft Learn MCP प्रयोग गरिन्छ,
  र learn.microsoft.com बाहिर रहेका सामग्रीका लागि Context7 र Aspire MCP प्रयोग गरिन्छ।
---
# Microsoft Docs

Microsoft प्रविधि इकोसिस्टमका लागि अनुसन्धान सिप। learn.microsoft.com र त्यसबाहिर बस्ने दस्तावेजहरू (VS Code, GitHub, Aspire, Agent Framework रिपोजिटरीहरू) समेट्छ।

---

## पूर्वनिर्धारित: Microsoft Learn MCP

यी उपकरणहरू प्रयोग गर्नुहोस् **learn.microsoft.com मा भएका सबै चीजहरूको** लागि — Azure, .NET, M365, Power Platform, Agent Framework, Semantic Kernel, Windows, र थप। यो Microsoft दस्तावेज क्वेरीहरूको ठूलो भागका लागि प्राथमिक उपकरण हो।

| उपकरण | उद्देश्य |
|------|---------|
| `microsoft_docs_search` | Search learn.microsoft.com — अवधारणाहरू, गाइडहरू, ट्युटोरियलहरू, कन्फिगरेसन |
| `microsoft_code_sample_search` | Learn डक्‍सबाट काम गर्ने कोड स्निपेटहरू फेला पार्नुहोस्। सर्वश्रेष्ठ नतिजाका लागि `language` (`python`, `csharp`, आदि) पास गर्नुहोस् |
| `microsoft_docs_fetch` | विशेष URL बाट पूर्ण पृष्ठ सामग्री प्राप्त गर्नुहोस् (जब खोज अंशहरू पर्याप्त हुँदैन) |

पूरा ट्युटोरियल, सबै कन्फिग विकल्पहरू, वा जब खोज अंशहरू काटिएका हुन्छन् त्यतिबेला खोजपछि `microsoft_docs_fetch` प्रयोग गर्नुहोस्।

---

## अपवादहरू: अन्य उपकरणहरू कहिले प्रयोग गर्ने

तलका वर्गहरू **learn.microsoft.com भन्दा बाहिर** बस्छन्। साटोमा निर्दिष्ट उपकरण प्रयोग गर्नुहोस्।

### .NET Aspire — Aspire MCP Server (सिफारिश गरिएको) वा Context7 प्रयोग गर्नुहोस्

Aspire दस्तावेजहरू **aspire.dev** मा बस्छन्, Learn मा होइन। उत्कृष्ट उपकरण तपाईंको Aspire CLI संस्करणमा निर्भर गर्दछ:

**CLI 13.2+** (सिफारिश) — Aspire MCP सर्वरमा बिल्ट-इन डक्‍स खोज उपकरणहरू समावेश छन्:

| MCP Tool | विवरण |
|----------|-------------|
| `list_docs` | aspire.dev बाट उपलब्ध सबै दस्तावेज सूचीबद्ध गर्दछ |
| `search_docs` | aspire.dev सामग्रीमा भारित लेक्सिकल खोज |
| `get_doc` | एक विशिष्ट कागजात slug द्वारा प्राप्त गर्दछ |

यी Aspire CLI 13.2 मा समावेश छन् ([PR #14028](https://github.com/dotnet/aspire/pull/14028)). अपडेट गर्न: `aspire update --self --channel daily`. सन्दर्भ: https://davidpine.dev/posts/aspire-docs-mcp-tools/

**CLI 13.1** — MCP सर्वरले integration lookup (`list_integrations`, `get_integration_docs`) प्रदान गर्छ तर **not** docs search। Context7 मा फर्किनुहोस्:

| Library ID | Use for |
|---|---|
| `/microsoft/aspire.dev` | Primary — guides, integrations, CLI reference, deployment |
| `/dotnet/aspire` | Runtime source — API internals, implementation details |
| `/communitytoolkit/aspire` | Community integrations — Go, Java, Node.js, Ollama |

### VS Code — Context7 प्रयोग गर्नुहोस्

VS Code दस्तावेजहरू **code.visualstudio.com** मा बस्छन्, Learn मा होइन।

| Library ID | Use for |
|---|---|
| `/websites/code_visualstudio` | User docs — settings, features, debugging, remote dev |
| `/websites/code_visualstudio_api` | Extension API — webviews, TreeViews, commands, contribution points |

### GitHub — Context7 प्रयोग गर्नुहोस्

GitHub दस्तावेजहरू **docs.github.com** र **cli.github.com** मा बस्छन्।

| Library ID | Use for |
|---|---|
| `/websites/github_en` | Actions, API, रिपोजिटरीहरू, सुरक्षा, प्रशासन, Copilot |
| `/websites/cli_github` | GitHub CLI (`gh`) commands and flags |

### Agent Framework — Learn MCP + Context7 प्रयोग गर्नुहोस्

Agent Framework ट्युटोरियलहरू learn.microsoft.com मा छन् ( `microsoft_docs_search` प्रयोग गर्नुहोस्), तर **GitHub रिपो** मा API-स्तरीय विवरण हुन्छ जुन प्राय: प्रकाशित डकुमेन्टहरू भन्दा अगाडि हुन्छ — विशेष गरी DevUI REST API सन्दर्भ, CLI विकल्पहरू, र .NET एकीकरण।

| Library ID | Use for |
|---|---|
| `/websites/learn_microsoft_en-us_agent-framework` | Tutorials — DevUI guides, tracing, workflow orchestration |
| `/microsoft/agent-framework` | API detail — DevUI REST endpoints, CLI flags, auth, .NET `AddDevUI`/`MapDevUI` |

**DevUI सुझाव:** कसरी-गर्न गाइडहरूको लागि Learn वेबसाइट स्रोत सोध्नुहोस्, त्यसपछि API-स्तरीय विशिष्टताहरू (endpoint schemas, proxy config, auth tokens) का लागि रिपो स्रोत हेर्नुहोस्।

---

## Context7 सेटअप

कुनै पनि Context7 क्वेरीको लागि, पहिले library ID समाधान गर्नुहोस् (प्रति सत्र एक पटक):

1. प्रविधि नामसँग `mcp_context7_resolve-library-id` कल गर्नुहोस्
2. फर्किएको library ID र एउटा विशिष्ट क्वेरीसँग `mcp_context7_query-docs` कल गर्नुहोस्

---

## प्रभावकारी क्वेरी लेख्ने तरिका

विशिष्ट हुनुहोस् — संस्करण, उद्देश्य, र भाषा समावेश गर्नुहोस्:

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
- **संस्करण** when relevant (`.NET 8`, `Aspire 13`, `VS Code 1.96`)
- **कार्य उद्देश्य** (`quickstart`, `tutorial`, `overview`, `limits`, `API reference`)
- **भाषा** for polyglot docs (`Python`, `TypeScript`, `C#`)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
अस्वीकरण:
यो दस्तावेज AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) प्रयोग गरेर अनुवाद गरिएको हो। हामी सटीकताको प्रयास गर्छौं, तर कृपया ध्यान दिनुहोस् कि स्वचालित अनुवादमा त्रुटि वा अशुद्धि हुन सक्छ। मूल दस्तावेजलाई यसको मूल भाषामा नै अधिकारिक स्रोत मानिनु पर्छ। महत्वपूर्ण जानकारीको लागि पेशेवर मानव अनुवाद सिफारिश गरिन्छ। यस अनुवादको प्रयोगबाट उत्पन्न हुने कुनै पनि गलतफहमी वा दुरव्याख्याका लागि हामी उत्तरदायी छैनौं।
<!-- CO-OP TRANSLATOR DISCLAIMER END -->