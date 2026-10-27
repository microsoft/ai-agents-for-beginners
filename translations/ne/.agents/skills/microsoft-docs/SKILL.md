---
name: microsoft-docs
description: आधिकारिक Microsoft कागजातहरूमा खोजी गर्नुहोस् ताकि Azure, .NET, Agent
  Framework, Aspire, VS Code, GitHub, र थप कुराहरू सम्बन्धित अवधारणा, ट्यूटोरियलहरू,
  र कोड उदाहरणहरू फेला पार्न सकियोस्। डिफल्ट रूपमा Microsoft Learn MCP प्रयोग गर्दछ,
  साथै learn.microsoft.com बाहिरको सामग्रीको लागि Context7 र Aspire MCP प्रयोग गर्छ।
---
# माइक्रोसफ्ट डोक्स

माइक्रोसफ्ट प्रविधि इकोसिस्टमका लागि अनुसन्धान कौशल। learn.microsoft.com र त्यस भन्दा बाहिरको डोकुमेन्टेसन (VS Code, GitHub, Aspire, Agent Framework रेकपोहरू) समेट्छ।

---

## पूर्वनिर्धारित: माइक्रोसफ्ट लर्न MCP

यी उपकरणहरू प्रयोग गर्नुहोस् **learn.microsoft.com मा सबै कुराको लागि** — Azure, .NET, M365, Power Platform, Agent Framework, Semantic Kernel, Windows, र थप। यो Microsoft डोकुमेन्टेसन प्रश्नहरूको विशाल बहुमतका लागि मुख्य उपकरण हो।

| उपकरण | उद्देश्य |
|------|---------|
| `microsoft_docs_search` | learn.microsoft.com खोज्नुहोस् — अवधारणाहरू, मार्गदर्शनहरू, ट्युटोरियलहरू, कन्फिगरेसन |
| `microsoft_code_sample_search` | लर्न डकुमेन्ट्सबाट कार्यरत कोड उदाहरणहरू पत्ता लगाउनुहोस्। सबैभन्दा राम्रो नतिजा लागि `language` (`python`, `csharp`, आदि) प्रदान गर्नुहोस् |
| `microsoft_docs_fetch` | विशेष URL बाट पूर्ण पृष्ठ सामग्री पाउनुहोस् (जब खोज अंशहरू पर्याप्त नभए) |

खोज पछि `microsoft_docs_fetch` प्रयोग गर्नुहोस् जब तपाईंलाई पूर्ण ट्युटोरियलहरू, सबै कन्फिग विकल्पहरू आवश्यक पर्दछन्, वा जब खोज अंशहरू छोट्याइएका हुन्छन्।

---

## अपवादहरू: अन्य उपकरणहरू कहिले प्रयोग गर्ने

तलका वर्गीकरणहरू **learn.microsoft.com बाहिर** छन्। निर्दिष्ट उपकरणहरू प्रयोग गर्नुहोस्।

### Aspire — Aspire MCP सर्भर (प्राथमिक) वा Context7 प्रयोग गर्नुहोस्

Aspire डोक्सहरू **aspire.dev** मा हुन्छन्, Learn मा होइन। उत्तम उपकरण तपाईंको Aspire CLI संस्करणमा निर्भर गर्दछ:

**CLI 13.2+** (सिफारिस गरिएको) — Aspire MCP सर्भरमा निर्मित डोक्स खोज उपकरणहरू छन्:

| MCP उपकरण | विवरण |
|----------|-------------|
| `list_docs` | aspire.dev बाट सबै उपलब्ध डोकुमेन्टेसन सूचीबद्ध गर्दछ |
| `search_docs` | aspire.dev सामग्रीमा भारी शब्द खोज |
| `get_doc` | स्लग द्वारा विशेष कागजात प्राप्त गर्दछ |

यी Aspire CLI 13.2 मा सामेल छन् ([PR #14028](https://github.com/microsoft/aspire/pull/14028))। अपडेट गर्न: `aspire update --self --channel daily` प्रयोग गर्नुहोस्।

**CLI 13.1** — MCP सर्भर इंटिग्रेशन लुकअप (`list_integrations`, `get_integration_docs`) दिन्छ तर डोक्स खोज **दिंदैन**। Context7 मा फर्कनुहोस्:

| लाइब्रेरी ID | प्रयोग गर्ने उद्देश्य |
|---|---|
| `/microsoft/aspire.dev` | मुख्य — मार्गदर्शनहरू, इंटिग्रेशनहरू, CLI संदर्भ, डिप्लोयमेन्ट |
| `/microsoft/aspire` | रनटाइम स्रोत — API भित्री कुरा, कार्यान्वयन विवरणहरू |
| `/communitytoolkit/aspire` | समुदाय इंटिग्रेशनहरू — Go, Java, Node.js, Ollama |

### VS Code — Context7 प्रयोग गर्नुहोस्

VS Code डोक्सहरू **code.visualstudio.com** मा छन्, Learn मा होइन।

| लाइब्रेरी ID | प्रयोग गर्ने उद्देश्य |
|---|---|
| `/websites/code_visualstudio` | प्रयोगकर्ता डोक्स — सेटिङहरू, सुविधाहरू, डिबगिङ, रिमोट विकास |
| `/websites/code_visualstudio_api` | एक्सटेन्सन API — वेबव्यूहरू, ट्रीभ्यूहरू, कमाण्डहरू, योगदान बिन्दुहरू |

### GitHub — Context7 प्रयोग गर्नुहोस्

GitHub डोक्सहरू **docs.github.com** र **cli.github.com** मा छन्।

| लाइब्रेरी ID | प्रयोग गर्ने उद्देश्य |
|---|---|
| `/websites/github_en` | एक्टन्स, API, रिपोज, सुरक्षा, प्रशासक, Copilot |
| `/websites/cli_github` | GitHub CLI (`gh`) कमाण्ड र फ्ल्यागहरू |

### Agent Framework — Learn MCP + Context7 प्रयोग गर्नुहोस्

Agent Framework ट्युटोरियलहरू learn.microsoft.com मा छन् (`microsoft_docs_search` प्रयोग गर्नुहोस्), तर GitHub रेकपोमा API-स्तरको विवरण हुन्छ जुन प्रायः प्रकाशित डोक्सभन्दा अघि हुन्छ — विशेष गरी DevUI REST API सन्दर्भ, CLI विकल्पहरू, र .NET इंटिग्रेशन।

| लाइब्रेरी ID | उपयोगका लागि |
|---|---|
| `/websites/learn_microsoft_en-us_agent-framework` | ट्युटोरियलहरू — DevUI मार्गदर्शनहरू, ट्रेसिङ, वर्कफ्लो अोरकेस्ट्रेशन |
| `/microsoft/agent-framework` | API विवरण — DevUI REST endpoints, CLI फ्ल्यागहरू, प्रमाणीकरण, .NET `AddDevUI`/`MapDevUI` |

**DevUI सुझाव:** Learn वेबसाइट स्रोतबाट हाउ-टु गाइडहरूको लागि खोज गर्नुहोस्, त्यसपछि API-स्तर विशिष्टताका लागि रेकपो स्रोत (एन्डपोइन्ट स्किमाहरू, प्रोक्सी कन्फिग, प्रमाणीकरण टोकनहरू) खोज्नुहोस्।

---

## Context7 सेटअप

कुनै पनि Context7 क्वेरीको लागि, पहिले लाइब्रेरी ID निर्णय गर्नुहोस् (प्रत्येक सत्रका लागि एकपटक मात्र):

1. प्राविधिक नामसँग `mcp_context7_resolve-library-id` कल गर्नुहोस्
2. फिर्ता गरिएको लाइब्रेरी ID र विशेष क्वेरीसँग `mcp_context7_query-docs` कल गर्नुहोस्

---

## प्रभावकारी क्वेरी लेख्ने तरिका

स्पष्ट हुनुहोस् — संस्करण, उद्देश्य, र भाषा समावेश गर्नुहोस्:

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

सन्दर्भ समावेश गर्नुहोस्:
- **सही अवस्थाको संस्करण** (`.NET 8`, `Aspire 13`, `VS Code 1.96`)
- **कार्य उद्देश्य** (`quickstart`, `tutorial`, `overview`, `limits`, `API reference`)
- **भाषा** बहुभाषिक डकुमेन्टहरूका लागि (`Python`, `TypeScript`, `C#`)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**अस्वीकरण**:
यो दस्तावेज़ AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) प्रयोग गरेर अनुवाद गरिएको हो। हामी सही हुन प्रयास गर्छौं, तर कृपया जानकार हुनुस् कि स्वचालित अनुवादमा त्रुटिहरू वा अशुद्धताहरू हुन सक्छन्। मूल दस्तावेज़ यसको मूल भाषामा आधिकारिक स्रोत मानिनुपर्छ। महत्वपूर्ण जानकारीका लागि व्यावसायिक मानव अनुवाद सिफारिस गरिन्छ। यस अनुवादको प्रयोगबाट उत्पन्न कुनै पनि गलत बुझाइ वा त्रुटिको लागि हामी जिम्मेवार छैनौं।
<!-- CO-OP TRANSLATOR DISCLAIMER END -->