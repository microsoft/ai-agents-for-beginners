---
name: microsoft-docs
description: आधिकारिक Microsoft दस्तावेज़ों में क्वेरी करें ताकि Azure, .NET, Agent
  Framework, Aspire, VS Code, GitHub, और अन्य के बारे में अवधारणाएँ, ट्यूटोरियल और
  कोड उदाहरण मिल सकें। डिफ़ॉल्ट रूप से Microsoft Learn MCP का उपयोग करता है, और उन
  सामग्रियों के लिए जो learn.microsoft.com के बाहर रहती हैं Context7 और Aspire MCP
  का उपयोग करता है।
---
# Microsoft Docs

Microsoft टेक्नोलॉजी इकोसिस्टम के लिए रिसर्च स्किल। इसमें learn.microsoft.com और वह डॉक्यूमेंटेशन शामिल है जो इसके बाहर है (VS Code, GitHub, Aspire, Agent Framework रिपोज)।

---

## डिफ़ॉल्ट: Microsoft Learn MCP

इन टूल्स का उपयोग करें **everything on learn.microsoft.com** — Azure, .NET, M365, Power Platform, Agent Framework, Semantic Kernel, Windows, और भी बहुत कुछ। यह अधिकांश Microsoft डॉक्यूमेंटेशन क्वेरीज़ के लिए प्राथमिक टूल है।

| Tool | Purpose |
|------|---------|
| `microsoft_docs_search` | learn.microsoft.com — कॉन्सेप्ट्स, गाइड्स, ट्यूटोरियल्स, कॉन्फ़िगरेशन खोजें |
| `microsoft_code_sample_search` | Learn डॉक्स से काम करने वाले कोड स्निपेट खोजें। सबसे अच्छे परिणामों के लिए `language` (`python`, `csharp`, आदि) पास करें |
| `microsoft_docs_fetch` | किसी विशिष्ट URL से पूर्ण पेज सामग्री प्राप्त करें (जब search excerpts पर्याप्त न हों) |

जब आपको पूर्ण ट्यूटोरियल्स, सभी कॉन्फ़िग विकल्प, या जब search excerpts कटा हुआ हों, तो खोज के बाद `microsoft_docs_fetch` का उपयोग करें।

---

## अपवाद: कब अन्य टूल का उपयोग करें

निम्नलिखित श्रेणियाँ **outside** learn.microsoft.com पर रहती हैं। इसके बजाय निर्दिष्ट टूल का उपयोग करें।

### .NET Aspire — Aspire MCP Server (preferred) या Context7 का उपयोग करें

Aspire डॉक्यूमेंटेशन **aspire.dev** पर रहती है, Learn पर नहीं। सबसे अच्छा टूल आपके Aspire CLI वर्जन पर निर्भर करता है:

**CLI 13.2+** (अनुशंसित) — Aspire MCP सर्वर में बिल्ट-इन डॉक्स सर्च टूल शामिल हैं:

| MCP Tool | Description |
|----------|-------------|
| `list_docs` | aspire.dev से उपलब्ध सभी डॉक्यूमेंटेशन को सूचीबद्ध करता है |
| `search_docs` | aspire.dev सामग्री में वेटेड लेक्सिकल सर्च |
| `get_doc` | किसी विशिष्ट दस्तावेज़ को slug के माध्यम से पुनः प्राप्त करता है |

ये Aspire CLI 13.2 में आते हैं ([PR #14028](https://github.com/dotnet/aspire/pull/14028)). अपडेट करने के लिए: `aspire update --self --channel daily`. संदर्भ: https://davidpine.dev/posts/aspire-docs-mcp-tools/

**CLI 13.1** — MCP सर्वर इंटीग्रेशन लुकअप (`list_integrations`, `get_integration_docs`) प्रदान करता है लेकिन डॉक्स सर्च **नहीं**। Context7 पर लौटें:

| Library ID | Use for |
|---|---|
| `/microsoft/aspire.dev` | प्राथमिक — गाइड्स, इंटीग्रेशन, CLI संदर्भ, डिप्लॉयमेंट |
| `/dotnet/aspire` | रनटाइम स्रोत — API इंटरनल्स, इम्प्लीमेंटेशन विवरण |
| `/communitytoolkit/aspire` | कम्युनिटी इंटीग्रेशन — Go, Java, Node.js, Ollama |

### VS Code — Context7 का उपयोग करें

VS Code डॉक्स **code.visualstudio.com** पर रहती हैं, Learn पर नहीं।

| Library ID | Use for |
|---|---|
| `/websites/code_visualstudio` | यूज़र डॉक्स — सेटिंग्स, फीचर्स, डिबगिंग, रिमोट डेव |
| `/websites/code_visualstudio_api` | एक्सटेंशन API — वेबव्यूज़, TreeViews, कमांड्स, योगदान बिंदु |

### GitHub — Context7 का उपयोग करें

GitHub डॉक्स **docs.github.com** और **cli.github.com** पर रहती हैं।

| Library ID | Use for |
|---|---|
| `/websites/github_en` | Actions, API, रिपोज, सुरक्षा, एडमिन, Copilot |
| `/websites/cli_github` | GitHub CLI (`gh`) कमांड्स और फ़्लैग्स |

### Agent Framework — Learn MCP + Context7 का उपयोग करें

Agent Framework ट्यूटोरियल्स learn.microsoft.com पर हैं (use `microsoft_docs_search`), लेकिन **GitHub repo** में API-स्तरीय विवरण अक्सर प्रकाशित डॉक्स से आगे होता है — विशेष रूप से DevUI REST API संदर्भ, CLI विकल्प, और .NET इंटीग्रेशन।

| Library ID | Use for |
|---|---|
| `/websites/learn_microsoft_en-us_agent-framework` | ट्यूटोरियल्स — DevUI गाइड्स, ट्रेसिंग, वर्कफ़्लो ऑर्केस्ट्रेशन |
| `/microsoft/agent-framework` | API विवरण — DevUI REST endpoints, CLI फ़्लैग्स, ऑथ, .NET `AddDevUI`/`MapDevUI` |

**DevUI टिप:** how-to गाइड्स के लिए Learn वेबसाइट स्रोत को क्वेरी करें, फिर API-स्तरीय विशिष्टताओं (endpoint schemas, proxy config, auth tokens) के लिए repo स्रोत देखें।

---

## Context7 सेटअप

किसी भी Context7 क्वेरी के लिए, पहले library ID को सुलझाएँ (एक सत्र में एक बार):

1. तकनीक के नाम के साथ `mcp_context7_resolve-library-id` कॉल करें
2. वापस मिले library ID और एक विशिष्ट क्वेरी के साथ `mcp_context7_query-docs` कॉल करें

---

## प्रभावी क्वेरीज लिखना

विशिष्ट रहें — संस्करण, उद्देश्य, और भाषा शामिल करें:

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
- **संस्करण** जब प्रासंगिक हो (`.NET 8`, `Aspire 13`, `VS Code 1.96`)
- **कार्य का उद्देश्य** (`quickstart`, `tutorial`, `overview`, `limits`, `API reference`)
- **भाषा** बहुभाषी डॉक्स के लिए (`Python`, `TypeScript`, `C#`)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
अस्वीकरण:
यह दस्तावेज़ एआई अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) का उपयोग करके अनूदित किया गया है। हम सटीकता के लिए प्रयासरत हैं, फिर भी कृपया ध्यान दें कि स्वचालित अनुवादों में त्रुटियाँ या असंगतियाँ हो सकती हैं। मूल दस्तावेज़ को उसकी मूल भाषा में आधिकारिक स्रोत माना जाना चाहिए। महत्वपूर्ण जानकारी के लिए पेशेवर मानव अनुवाद की सलाह दी जाती है। इस अनुवाद के उपयोग से उत्पन्न किसी भी गलतफहमी या गलत व्याख्या के लिए हम उत्तरदायी नहीं हैं।
<!-- CO-OP TRANSLATOR DISCLAIMER END -->