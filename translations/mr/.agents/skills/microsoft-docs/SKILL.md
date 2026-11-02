---
name: microsoft-docs
description: अधिकृत Microsoft दस्तऐवजांची चौकशी करा जेणेकरून Azure, .NET, Agent Framework,
  Aspire, VS Code, GitHub, आणि बरेच काही यांसारख्या विषयांवरील संकल्पना, प्रशिक्षण
  आणि कोड उदाहरणे मिळतील. Microsoft Learn MCP हे डीफॉल्ट म्हणून वापरले जाते, आणि learn.microsoft.com
  बाहेर असलेल्या सामग्रीसाठी Context7 आणि Aspire MCP वापरले जातात.
---
# Microsoft Docs

मायक्रोसॉफ्ट तंत्रज्ञान परिसंस्थेसाठी संशोधन कौशल्य. learn.microsoft.com आणि त्याबाहेरचे दस्तऐवजीकरण (VS कोड, GitHub, Aspire, Agent Framework रेपॉजिटरीज) यावर आधारित आहे.

---

## डीफॉल्ट: Microsoft Learn MCP

learn.microsoft.com वर **सर्व काही** साठी खालील साधने वापरा — Azure, .NET, M365, Power Platform, Agent Framework, Semantic Kernel, Windows इत्यादी. ही मायक्रोसॉफ्ट दस्तऐवजीकरण क्वेरीजसाठी मुख्य साधन आहे.

| टूल | उद्दिष्ट |
|------|---------|
| `microsoft_docs_search` | learn.microsoft.com सर्च करा — संकल्पना, मार्गदर्शक, ट्युटोरियल्स, कॉन्फिगरेशन |
| `microsoft_code_sample_search` | Learn दस्तऐवजांमधून काम करणारा कोड स्निपेट सापडा. सर्वोत्तम निकालांसाठी `language` (`python`, `csharp`, इ.) वापरा |
| `microsoft_docs_fetch` | विशिष्ट URL कडून पूर्ण पृष्ठ सामग्री मिळवा (जेव्हा सर्च एक्सर्सट्स पुरेसे नसतात) |

सर्चनंतर संपूर्ण ट्युटोरियल्स, सर्व कॉन्फिग पर्याय किंवा जेव्हा सर्च एक्सर्सट्स वाक्यांश मर्यादित असतात तेव्हा `microsoft_docs_fetch` वापरा.

---

## अपवाद: कधी इतर साधने वापरावीत

खालील वर्ग learn.microsoft.com च्या **बाहेर** असतात. यासाठी निर्दिष्ट टूल वापरा.

### Aspire — Aspire MCP Server (प्राधान्यक्रम) किंवा Context7 वापरा

Aspire दस्तऐवज **aspire.dev** वर आहेत, Learn वर नाहीत. उत्तम टूल तुमच्या Aspire CLI आवृत्तीवर अवलंबून आहे:

**CLI 13.2+** (शिफारस केलेले) — Aspire MCP सर्वरमध्ये अंगभूत दस्तऐवज सर्च साधने आहेत:

| MCP टूल | वर्णन |
|----------|-------------|
| `list_docs` | aspire.dev मधील सर्व उपलब्ध दस्तऐवजांची यादी देते |
| `search_docs` | aspire.dev सामग्रीमध्ये वजन दिलेला लॅक्सिकल सर्च |
| `get_doc` | स्लगद्वारे विशिष्ट दस्तऐवज मिळवा |

हे Aspire CLI 13.2 ([PR #14028](https://github.com/microsoft/aspire/pull/14028)) मध्ये समाविष्ट आहे. अपडेट करण्यासाठी: `aspire update --self --channel daily` वापरा.

**CLI 13.1** — MCP सर्वर इंटिग्रेशन लुकअप (`list_integrations`, `get_integration_docs`) प्रदान करतो पण दस्तऐवज सर्च **नाही** करतो. Context7 वापरा:

| लायब्ररी आयडी | वापरासाठी |
|---|---|
| `/microsoft/aspire.dev` | मुख्य — मार्गदर्शक, इंटिग्रेशन्स, CLI संदर्भ, डिप्लॉयमेंट |
| `/microsoft/aspire` | रनटाइम स्रोत — API अंतर्गत तपशील, अमलबजावणी तपशील |
| `/communitytoolkit/aspire` | कम्युनिटी इंटिग्रेशन्स — Go, Java, Node.js, Ollama |

### VS Code — Context7 वापरा

VS Code दस्तऐवज **code.visualstudio.com** वर आहेत, Learn वर नाहीत.

| लायब्ररी आयडी | वापरासाठी |
|---|---|
| `/websites/code_visualstudio` | वापरकर्ता दस्तऐवज — सेटिंग्ज, फिचर्स, डीबगिंग, रिमोट डेव्ह |
| `/websites/code_visualstudio_api` | एक्सटेंशन API — वेबव्ह्यूज, ट्रीव्ह्यूज, आज्ञा, योगदान पॉइंट्स |

### GitHub — Context7 वापरा

GitHub दस्तऐवज **docs.github.com** आणि **cli.github.com** वर आहेत.

| लायब्ररी आयडी | वापरासाठी |
|---|---|
| `/websites/github_en` | अॅक्शन्स, API, रेपो, सुरक्षा, अॅडमिन, कॉपायलट |
| `/websites/cli_github` | GitHub CLI (`gh`) आज्ञा आणि फ्लॅग्स |

### Agent Framework — Learn MCP + Context7 वापरा

Agent Framework ट्युटोरियल्स learn.microsoft.com वर आहेत (`microsoft_docs_search` वापरा), पण **GitHub रेपो** मध्ये API-स्तरीय तपशील आहे जो अनेकदा प्रकाशित दस्तऐवजांपेक्षा पुढे आहे — विशेषतः DevUI REST API संदर्भ, CLI पर्याय, आणि .NET इंटिग्रेशन.

| लायब्ररी आयडी | वापरासाठी |
|---|---|
| `/websites/learn_microsoft_en-us_agent-framework` | ट्युटोरियल्स — DevUI मार्गदर्शक, ट्रेसिंग, वर्कफ्लो ऑर्केस्ट्रेशन |
| `/microsoft/agent-framework` | API तपशील — DevUI REST एंडपॉइंट्स, CLI फ्लॅग्स, प्रमाणीकरण, .NET `AddDevUI`/`MapDevUI` |

**DevUI टीप:** Learn वेबसाइट स्त्रोतावर हाऊ-टू मार्गदर्शक शोधा, नंतर रेपो स्त्रोतावर API-स्तरीय तपशील मिळवा (एंडपॉइंट स्कीमास, प्रॉक्सी कॉन्फिग, प्रमाणीकरण टोकन).

---

## Context7 सेटअप

कोणत्याही Context7 क्वेरीसाठी, प्रथम लायब्ररी आयडी ठरवा (प्रत्येक सत्रासाठी एकदाच):

1. तंत्रज्ञान नावासह `mcp_context7_resolve-library-id` कॉल करा
2. परत आलेल्या लायब्ररी आयडीसह आणि विशिष्ट क्वेरीसह `mcp_context7_query-docs` कॉल करा

---

## प्रभावी क्वेरीज लिहिणे

विशिष्ट रहा — आवृत्ती, हेतू, आणि भाषा यांचा समावेश करा:

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

संदर्भ जोडा:
- संबंधित वेळेस **आवृत्ती** (`.NET 8`, `Aspire 13`, `VS Code 1.96`)
- **कार्य हेतू** (`quickstart`, `tutorial`, `overview`, `limits`, `API reference`)
- बहुभाषिक दस्तऐवजासाठी **भाषा** (`Python`, `TypeScript`, `C#`)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**अस्वीकरण**:
हा दस्तऐवज AI भाषांतर सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) चा वापर करून अनुवादित केला आहे. जरी आम्ही अचूकतेसाठी प्रयत्न करतो, तरी कृपया लक्षात घ्या की स्वयंचलित भाषांतरांमध्ये त्रुटी किंवा अचूकतेची कमतरता असू शकते. मूळ दस्तऐवज त्याच्या मूळ भाषेत अधिकृत स्रोत मानला पाहिजे. महत्त्वाची माहिती असल्यास, व्यावसायिक मानवी भाषांतराची शिफारस केली जाते. या भाषांतराच्या वापरामुळे उद्भवणाऱ्या कोणत्याही गैरसमज किंवा चुकीच्या अर्थलावणीसाठी आम्ही जबाबदार नाही.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->