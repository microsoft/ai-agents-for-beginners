---
name: microsoft-docs
---
# Microsoft Docs

Microsoft तकनीकी इकोसिस्टम के लिए अनुसंधान कौशल। इसमें learn.microsoft.com और उससे बाहर की डाक्यूमेंटेशन शामिल है (VS Code, GitHub, Aspire, Agent Framework रिपोज़)।

---

## डिफ़ॉल्ट: Microsoft Learn MCP

इन उपकरणों का उपयोग **learn.microsoft.com पर सब कुछ** के लिए करें — Azure, .NET, M365, Power Platform, Agent Framework, Semantic Kernel, Windows, और बहुत कुछ। यह अधिकांश Microsoft डाक्यूमेंटेशन प्रश्नों के लिए प्राथमिक उपकरण है।

| उपकरण | उद्देश्य |
|------|---------|
| `microsoft_docs_search` | learn.microsoft.com पर खोजें — अवधारणाएं, मार्गदर्शिकाएं, ट्यूटोरियल, कॉन्फ़िगरेशन |
| `microsoft_code_sample_search` | Learn डॉक्स से काम करने वाले कोड स्निपेट्स खोजें। सर्वोत्तम परिणाम के लिए `language` (`python`, `csharp`, आदि) पास करें |
| `microsoft_docs_fetch` | एक विशिष्ट URL से पूर्ण पृष्ठ सामग्री प्राप्त करें (जब खोज अंश पर्याप्त न हों) |

जब आपको पूर्ण ट्यूटोरियल, सभी कॉन्फ़िग विकल्पों की आवश्यकता हो, या जब खोज अंश काटे गए हों तब खोज के बाद `microsoft_docs_fetch` का उपयोग करें।

---

## अपवाद: अन्य उपकरण कब उपयोग करें

निम्नलिखित श्रेणियाँ **learn.microsoft.com के बाहर** रहती हैं। इसके बजाय निर्दिष्ट उपकरण का उपयोग करें।

### Aspire — Aspire MCP सर्वर (प्राथमिक) या Context7 का उपयोग करें

Aspire डॉक्स **aspire.dev** पर रहते हैं, न कि Learn पर। सर्वोत्तम उपकरण आपके Aspire CLI संस्करण पर निर्भर करता है:

**CLI 13.2+** (सिफारिश की गई) — Aspire MCP सर्वर में अंतर्निहित डॉक्स खोज उपकरण शामिल हैं:

| MCP उपकरण | विवरण |
|----------|-------------|
| `list_docs` | aspire.dev से सभी उपलब्ध डाक्यूमेंटेशन सूचीबद्ध करता है |
| `search_docs` | aspire.dev सामग्री के पार वेटेड लेक्सिकल खोज |
| `get_doc` | स्लग द्वारा एक विशिष्ट दस्तावेज़ प्राप्त करता है |

ये Aspire CLI 13.2 ([PR #14028](https://github.com/microsoft/aspire/pull/14028)) में आते हैं। अपडेट के लिए: `aspire update --self --channel daily`।

**CLI 13.1** — MCP सर्वर इंटीग्रेशन लुकअप (`list_integrations`, `get_integration_docs`) प्रदान करता है लेकिन **डॉक्स खोज नहीं**। इन पर वापस आने के लिए Context7 का उपयोग करें:

| लाइब्रेरी ID | उपयोग हेतु |
|---|---|
| `/microsoft/aspire.dev` | प्राथमिक — मार्गदर्शिकाएं, इंटीग्रेशन, CLI संदर्भ, डिप्लॉयमेंट |
| `/microsoft/aspire` | रनटाइम स्रोत — API आंतरिक, कार्यान्वयन विवरण |
| `/communitytoolkit/aspire` | कम्युनिटी इंटीग्रेशन — Go, Java, Node.js, Ollama |

### VS Code — Context7 का उपयोग करें

VS Code डॉक्स **code.visualstudio.com** पर रहते हैं, न कि Learn पर।

| लाइब्रेरी ID | उपयोग हेतु |
|---|---|
| `/websites/code_visualstudio` | उपयोगकर्ता डॉक्स — सेटिंग्स, फीचर्स, डिबगिंग, रिमोट डेव |
| `/websites/code_visualstudio_api` | एक्सटेंशन API — वेबव्यू, TreeViews, कमांड, योगदान बिंदु |

### GitHub — Context7 का उपयोग करें

GitHub डॉक्स **docs.github.com** और **cli.github.com** पर रहते हैं।

| लाइब्रेरी ID | उपयोग हेतु |
|---|---|
| `/websites/github_en` | एक्शन्स, API, रिपोज, सुरक्षा, एडमिन, Copilot |
| `/websites/cli_github` | GitHub CLI (`gh`) कमांड और फ्लैग्स |

### Agent Framework — Learn MCP + Context7 का उपयोग करें

Agent Framework ट्यूटोरियल learn.microsoft.com पर हैं (`microsoft_docs_search` का उपयोग करें), लेकिन **GitHub रिपोज** में API स्तर का विवरण होता है जो अक्सर प्रकाशित डॉक्स से आगे होता है — विशेष रूप से DevUI REST API संदर्भ, CLI विकल्प, और .NET इंटीग्रेशन।

| लाइब्रेरी ID | उपयोग हेतु |
|---|---|
| `/websites/learn_microsoft_en-us_agent-framework` | ट्यूटोरियल — DevUI गाइड, ट्रेसिंग, वर्कफ़्लो ऑर्केस्ट्रेशन |
| `/microsoft/agent-framework` | API विवरण — DevUI REST एंडपॉइंट, CLI फ्लैग्स, प्रमाणीकरण, .NET `AddDevUI`/`MapDevUI` |

**DevUI टिप:** पहले Learn वेबसाइट स्रोत से कैसे-गाइड पूछें, फिर API स्तर के विशेषताओं (एंडपॉइंट स्कीमा, प्रॉक्सी सेटिंग, प्रमाणीकरण टोकन) के लिए रिपोज स्रोत देखें।

---

## Context7 सेटअप

किसी भी Context7 प्रश्न के लिए, पहले लाइब्रेरी ID हल करें (सत्र में एक बार):

1. प्रौद्योगिकी नाम के साथ `mcp_context7_resolve-library-id` कॉल करें
2. प्राप्त लाइब्रेरी ID और विशिष्ट प्रश्न के साथ `mcp_context7_query-docs` कॉल करें

---

## प्रभावी प्रश्न लिखना

विशिष्ट बनें — संस्करण, उद्देश्य, और भाषा शामिल करें:

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

संदर्भ शामिल करें:
- जहां प्रासंगिक हो **संस्करण** (`.NET 8`, `Aspire 13`, `VS Code 1.96`)
- **कार्य उद्देश्य** (`quickstart`, `tutorial`, `overview`, `limits`, `API reference`)
- बहुभाषी डॉक्स के लिए **भाषा** (`Python`, `TypeScript`, `C#`)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**अस्वीकरण**:
इस दस्तावेज़ का अनुवाद AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) का उपयोग करके किया गया है। जबकि हम सटीकता के लिए प्रयास करते हैं, कृपया ध्यान दें कि स्वचालित अनुवादों में त्रुटियाँ या अशुद्धियाँ हो सकती हैं। मूल दस्तावेज़ अपनी मूल भाषा में ही प्रामाणिक स्रोत माना जाना चाहिए। महत्वपूर्ण जानकारी के लिए, पेशेवर मानव अनुवाद की सिफारिश की जाती है। इस अनुवाद के उपयोग से उत्पन्न किसी भी गलतफहमी या गलत व्याख्या के लिए हम उत्तरदायी नहीं हैं।
<!-- CO-OP TRANSLATOR DISCLAIMER END -->