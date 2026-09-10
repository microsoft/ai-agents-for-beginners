---
name: microsoft-docs
description: Azure, .NET, Agent Framework, Aspire, VS Code, GitHub आणि इतर यंत्रणांमधील
  संकल्पना, ट्यूटोरियल आणि कोड उदाहरणे शोधण्यासाठी अधिकृत Microsoft दस्तऐवजीकरण क्वेरी
  करा. डिफॉल्ट म्हणून Microsoft Learn MCP वापरते, तर learn.microsoft.com च्या बाहेरील
  सामग्रीसाठी Context7 आणि Aspire MCP वापरले जातात.
---
# Microsoft Docs

Microsoft तंत्रज्ञान इकोसिस्टमसाठी संशोधन कौशल्य. हे learn.microsoft.com आणि त्याबाहेर असलेले दस्तऐवजीकरण कव्हर करते (VS Code, GitHub, Aspire, Agent Framework रिपॉझिटरीज).

---

## डिफॉल्ट: Microsoft Learn MCP

हे साधने **learn.microsoft.com वरील सर्व काही** साठी वापरा — Azure, .NET, M365, Power Platform, Agent Framework, Semantic Kernel, Windows, आणि अधिक. हे बहुतेक Microsoft दस्तऐवजीकरण प्रश्नांसाठी प्राथमिक साधन आहे.

| Tool | Purpose |
|------|---------|
| `microsoft_docs_search` | learn.microsoft.com शोधा — संकल्पना, मार्गदर्शक, ट्यूटोरियल्स, कॉन्फिगरेशन |
| `microsoft_code_sample_search` | Learn दस्तऐवजांमधील चालणारे कोड स्निपेट शोधा. सर्वोत्तम परिणामांसाठी `language` (`python`, `csharp`, इत्यादी) द्या |
| `microsoft_docs_fetch` | विशिष्ट URL कडून पूर्ण पान सामग्री मिळवा (जेव्हा शोधातील अंश पुरेसे नसतात तेव्हा) |

शोध केल्यानंतर पूर्ण ट्यूटोरियल्स, सर्व कॉन्फिग पर्याय किंवा जेव्हा शोधातील अंश कापलेले असतात तेव्हा `microsoft_docs_fetch` वापरा.

---

## अपवाद: इतर साधने कधी वापरावीत

खालील वर्गीकरणे **learn.microsoft.com च्या बाहेर** आहेत. त्याऐवजी निर्दिष्ट केलेले साधन वापरा.

### .NET Aspire — Aspire MCP Server (प्राधान्य) किंवा Context7 वापरा

Aspire दस्तऐवजीकरणे **aspire.dev** वर आहेत, Learn वर नाहीत. सर्वोत्तम साधन तुमच्या Aspire CLI आवृत्तीवर अवलंबून आहे:

**CLI 13.2+** (शिफारसीय) — Aspire MCP सर्व्हरमध्ये अंतर्भूत docs शोध साधने आहेत:

| MCP Tool | Description |
|----------|-------------|
| `list_docs` | aspire.dev वरून सर्व उपलब्ध दस्तऐवजीकरणांची यादी दाखवते |
| `search_docs` | aspire.dev सामग्रीवर वजनदार लेक्सिकल शोध |
| `get_doc` | slug ने एखादे विशिष्ट दस्तऐवज प्राप्त करते |

हे Aspire CLI 13.2 मध्ये डिलिव्हर होतात ([PR #14028](https://github.com/dotnet/aspire/pull/14028)). अपडेट करण्यासाठी: `aspire update --self --channel daily`. संदर्भ: https://davidpine.dev/posts/aspire-docs-mcp-tools/

**CLI 13.1** — MCP सर्व्हर इंटीग्रेशन लुकअप (`list_integrations`, `get_integration_docs`) प्रदान करते परंतु **docs शोध** नाही. या प्रकरणात Context7 वापरा:

| Library ID | Use for |
|---|---|
| `/microsoft/aspire.dev` | प्राथमिक — मार्गदर्शक, इंटीग्रेशन्स, CLI संदर्भ, डिप्लॉयमेंट |
| `/dotnet/aspire` | रनटाइम स्रोत — API अंतर्गत रचना, अंमलबजावणी तपशील |
| `/communitytoolkit/aspire` | सामुदायिक इंटीग्रेशन्स — Go, Java, Node.js, Ollama |

### VS Code — Context7 वापरा

VS Code दस्तऐवजीकरणे **code.visualstudio.com** वर आहेत, Learn वर नाहीत.

| Library ID | Use for |
|---|---|
| `/websites/code_visualstudio` | वापरकर्ता दस्तऐवजीकरण — सेटिंग्ज, वैशिष्ट्ये, डिबगिंग, रिमोट डेव्हलपमेंट |
| `/websites/code_visualstudio_api` | एक्स्टेंशन API — webviews, TreeViews, commands, contribution points |

### GitHub — Context7 वापरा

GitHub दस्तऐवजीकरणे **docs.github.com** आणि **cli.github.com** वर आहेत.

| Library ID | Use for |
|---|---|
| `/websites/github_en` | Actions, API, रेपॉजिटरीज, सुरक्षा, प्रशासक, Copilot |
| `/websites/cli_github` | GitHub CLI (`gh`) चे कमांड आणि फ्लॅग |

### Agent Framework — Learn MCP + Context7 वापरा

Agent Framework ट्यूटोरियल्स learn.microsoft.com वर आहेत (`microsoft_docs_search` वापरा), परंतु **GitHub repo** मध्ये API-स्तरीय तपशील असतात जे बर्‍याचदा प्रकाशित दस्तऐवजीकरणापेक्षा पुढे असतात — विशेषतः DevUI REST API संदर्भ, CLI पर्याय, आणि .NET एकत्रीकरण.

| Library ID | Use for |
|---|---|
| `/websites/learn_microsoft_en-us_agent-framework` | ट्यूटोरियल्स — DevUI मार्गदर्शक, ट्रेसिंग, वर्कफ्लो ऑर्केस्ट्रेशन |
| `/microsoft/agent-framework` | API तपशील — DevUI REST endpoints, CLI फ्लॅग, auth, .NET `AddDevUI`/`MapDevUI` |

**DevUI टिप:** How-to मार्गदर्शकांसाठी Learn वेबसाइटचा स्रोत चौकशी करा, नंतर API-स्तरीय विशिष्टांसाठी रेपो स्रोत तपासा (endpoint schemas, proxy config, auth tokens).

---

## Context7 सेटअप

कोणत्याही Context7 क्वेरीसाठी, प्रथम लायब्ररी ID निश्चित करा (सत्रासाठी एकदाच):

1. तंत्रज्ञानाच्या नावासह `mcp_context7_resolve-library-id` कॉल करा
2. परत आलेल्या लायब्ररी ID आणि विशिष्ट क्वेरीसह `mcp_context7_query-docs` कॉल करा

---

## प्रभावी क्वेरीज लिहिणे

विशिष्ट रहा — आवृत्ती, हेतू, आणि भाषा समाविष्ट करा:

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

संदर्भ समाविष्ट करा:
- **आवृत्ती** जेव्हा संबंधित (`.NET 8`, `Aspire 13`, `VS Code 1.96`)
- **कामाचा हेतू** (`quickstart`, `tutorial`, `overview`, `limits`, `API reference`)
- **भाषा** बहुभाषिक दस्तऐवजांसाठी (`Python`, `TypeScript`, `C#`)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
अस्वीकरण:
हा दस्तऐवज AI अनुवाद सेवा Co‑op Translator (https://github.com/Azure/co-op-translator) वापरून अनुवादित करण्यात आला आहे. जरी आम्ही अचूकतेसाठी प्रयत्न करतो, तरी कृपया लक्षात घ्या की स्वयंचलित अनुवादांमध्ये चुका किंवा अचूकतेच्या त्रुटी असू शकतात. मूळ दस्तऐवज त्याच्या मूळ भाषेत अधिकृत स्रोत मानला जावा. महत्त्वाची माहिती असल्यास व्यावसायिक मानवी अनुवाद करण्याची शिफारस केली जाते. या अनुवादाच्या वापरामुळे उद्भवणाऱ्या कोणत्याही गैरसमजुती किंवा चुकीच्या अर्थनिर्देशासाठी आम्ही जबाबदार नाहीत.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->