# चेंजलॉग

**AI Agents for Beginners** कोर्समधील सर्व लक्षणीय बदल ह्या फाईलमध्ये नोंदवले आहेत.

## [जारी] — 2026-07-14

हा प्रकाशन कोर्स दोन नव्या-निषिद्ध मॉडेल्सवरून हलवतो, उर्वरित लेसन नोटबुक्सला स्थिर Microsoft Agent Framework API कडे स्थलांतरित करतो, आणि Python नोटबुक्सला Microsoft Foundry च्या प्रत्यक्ष डिप्लॉयमेंटवर पडताळणी करतो.

### बदलले

- **निषिद्ध मॉडेल्सवरून हलवले (`gpt-4.1` / `gpt-4.1-mini` → `gpt-5-mini`).** `gpt-4.1` आणि `gpt-4.1-mini` आता निषिद्ध आहेत (प्रकाशित निवृत्तीची तारीख **14 ऑक्टोबर 2026**). प्रत्येक कोर्स संदर्भ (डॉक्स, `.env.example`, Python/.NET नोटबुक्स आणि नमुने) यांना निषिद्ध नसलेल्या `gpt-5-mini` ने बदलेले आहे. लेसन 16 च्या मॉडेल-रूटिंग उदाहरणात `gpt-5-nano` (लहान) आणि `gpt-5-mini` (मोठ्या) वापरून लहान/मोठा विरोध ठेवले आहे. विकत घेतलेली तृतीय-पक्ष फायली ([15-browser-use/llms.txt](../../15-browser-use/llms.txt)), ऐतिहासिक GitHub Models मजकूर, आणि `azure-openai-to-responses` कौशल्याच्या कार्यक्षमतेच्या टिपा जानबूझून न बदलता ठेवल्या आहेत.
- **लेसन 14 हँडऑफ नोटबुक स्थिर API कडे स्थलांतरित.** [14-handoff.ipynb](./14-microsoft-agent-framework/code-samples/14-handoff.ipynb) आता `agent_framework.orchestrations.HandoffBuilder` वापरतो `.with_start_agent(...)`, `HandoffAgentUserRequest.create_response(...)`, `event.type`-आधारित स्ट्रीमिंग, आणि `FoundryChatClient` सह (काढण्यात आलेले प्री-1.0 `HandoffBuilder`/`ChatMessage`/`RequestInfoEvent` चिन्हे याऐवजी).
- **लेसन 14 मानव-इन-द-लूप नोटबुक स्थिर API कडे स्थलांतरित.** [14-human-loop.ipynb](./14-microsoft-agent-framework/code-samples/14-human-loop.ipynb) आता `ctx.request_info(...)` + `@response_handler` वापरून विराम देतो (काढण्यात आलेले `RequestInfoExecutor` / `RequestInfoMessage` / `RequestResponse` याऐवजी), `WorkflowBuilder(start_executor=..., output_executors=[...])` सह तयार करतो, संरचित आउटपुट `default_options={"response_format": ...}` मार्फत चालवतो, आणि स्क्रिप्ट केलेले उत्तर वापरतो ज्यामुळे नोटबुक स्वतःहून चालतो (कोणतेही `input()` ब्लॉकिंग नाही).
- **पर्यावरण संरचना** ([.env.example](../../.env.example)): मॉडेल डिप्लॉयमेंट नावे `gpt-5-mini` मध्ये बदली; `AZURE_AI_SMALL_MODEL` / `AZURE_AI_LARGE_MODEL` (लेसन 16 रूटिंग) आणि आधी नसलेले `AZURE_OPENAI_CHAT_DEPLOYMENT_NAME` (लेसन 15 ब्राउझर-उपयोग) जोडले.
- **डिपेंडन्सीज** ([requirements.txt](../../requirements.txt)): `agent-framework`, `agent-framework-foundry`, आणि `agent-framework-openai` यांच्या आवृत्ती `~=1.10.0` वर फिक्स केल्या; एकसंध, पडताळणी केलेला संच (1.11.0 मध्ये या लेसन्स वापरणाऱ्या API मध्ये तुटणारे बदल आहेत).

### नोंदी व ज्ञात मर्यादा

- **प्रत्यक्ष Microsoft Foundry वर पडताळले.** Python नोटबुक्स `nbconvert` सह हेडलेस पद्धतीने चालवल्या गेल्या ज्या Microsoft Foundry प्रकल्पासाठी `gpt-5-mini` (आणि लेसन 16 रूटिंगसाठी `gpt-5-nano`) वापरत होत्या. स्वता:च्या प्रकल्पात समतुल्य निषिद्ध नसलेले मॉडेल डिप्लॉय करा; नोटबुक्स `AZURE_AI_MODEL_DEPLOYMENT_NAME` / `AZURE_OPENAI_DEPLOYMENT` मधून डिप्लॉयमेंट नाव वाचतात.
- **काही लेसनसाठी अजूनही अतिरिक्त स्रोतांची आवश्यकता.** लेसन 05 ला Azure AI Search ची गरज आहे; लेसन 08 बिंग-ग्राउंडिंग वर्कफ्लो (`04.python-agent-framework-workflow-aifoundry-condition.ipynb`) ला Bing कनेक्शन आणि Microsoft Foundry Agent Service होस्ट केलेल्या साधनांची गरज आहे; लेसन 13 (Cognee) आणि लेसन 17 (Foundry Local) ला त्यांचे स्वतःचे रनटाइम आवश्यक आहेत.

## [जारी] — 2026-07-13

हा प्रकाशन दोन नवीन लेसन जोडतो जे डिप्लॉयमेंट आर्क पूर्ण करतात — Microsoft Foundry पर्यंत एजंट वाढवणे आणि एका कार्यस्थानापर्यंत कमी करणे — तसेच स्मोक-टेस्ट पाइपलाइन, नवीन नेव्हिगेशन, नवीन शिकणाऱ्याच्या कौशल्यांचा समावेश करतो, आणि अद्ययावत ब्रँडिंग.

### जोडले

- **लेसन 16 — Microsoft Foundry सह स्केलेबल एजंट डिप्लॉय करणे.** नवीन लेसन [16-deploying-scalable-agents/README.md](./16-deploying-scalable-agents/README.md) आणि चालवण्याजोगा नोटबुक [16-python-agent-framework.ipynb](./16-deploying-scalable-agents/code_samples/16-python-agent-framework.ipynb) जे ग्राहक-समर्थन एजंट तयार करतो (साधने, RAG, मेमरी, मॉडेल रूटिंग, प्रतिसाद कॅशिंग, मानवी मंजुरी, मूल्यमापन द्वार, आणि OpenTelemetry ट्रेसिंग), विकास/डिप्लॉयमेंट/रनटाइम Mermaid आरेखनांसह, ज्ञान तपासणी, असाइनमेंट, आणि आव्हान.
- **लेसन 17 — Foundry Local आणि Qwen सह स्थानिक AI एजंट तयार करणे.** नवीन लेसन [17-creating-local-ai-agents/README.md](./17-creating-local-ai-agents/README.md) आणि नोटबुक [17-local-agent-foundry-local.ipynb](./17-creating-local-ai-agents/code_samples/17-local-agent-foundry-local.ipynb) पूर्णपणे डिव्हाइसवर चालणारा अभियंता सहायक तयार करतो (Qwen फंक्शन कॉलिंग Foundry Local द्वारे, सँडबॉक्स फाईल साधने, स्थानिक RAG सह Chroma, पर्यायी स्थानिक MCP), स्थानिक-फक्त / स्थानिक-RAG / साधन कॉलिंग आरेखनांसह, ज्ञान तपासणी, असाइनमेंट, आणि आव्हान.
- **स्मोक-टेस्ट पाइपलाइन.** नवीन [AI Smoke Test](https://github.com/marketplace/actions/ai-smoke-test) वर्कफ्लो [.github/workflows/smoke-test.yml](../../.github/workflows/smoke-test.yml) आणि प्रत्येक लेसन बद्दल केटलॉग [tests/](./tests/README.md) मध्ये जे एजंट डिप्लॉय करता येतात (लेसन 01, 04, 05, आणि 16), प्रत्येक केटलॉगला त्याच्या लेसन आणि होस्टेड एजंट नावाशी जुळणार्‍या README सह. लेसन 16 ला "डिप्लॉय केलेला एजंट स्मोक टेस्टसह पडताळणी" विभाग मिळाला; लेसन 01/04/05 ला पर्यायी स्मोक-टेस्ट पॉइंटर.
- **शिकणाऱ्याची कौशल्ये.** नवीन एजंट कौशल्ये `.agents/skills/` अंतर्गत: [deploying-scalable-agents](./.agents/skills/deploying-scalable-agents/SKILL.md), [local-ai-agents](./.agents/skills/local-ai-agents/SKILL.md) (लेसन 16 आणि 17 चे मार्गदर्शन), आणि [testing-course-samples](./.agents/skills/testing-course-samples/SKILL.md) (नोटबुक नमुन्यांची प्रत्यक्ष Microsoft Foundry / Azure OpenAI सेटअपवर पडताळणी कशी करायची).
- **नोटबुक पडताळणी रनर.** नवीन [scripts/validate-notebooks.ps1](../../scripts/validate-notebooks.ps1) जे प्रत्येक Python नोटबुक `nbconvert` सह हेडलेस पद्धतीने चालवते आणि PASS/FAIL मॅट्रिक्स (आणि `results.json`) छापते. हे स्वयं-ओळख करते रेपो मूळ आणि Python, कोर्सच्या बाहेरचे नोटबुक वगळते (`.venv`, `site-packages`, `translations`, कौशल्य टेम्प्लेट सामग्री) आणि `.NET` नोटबुक्स डीफॉल्टने, आणि `-Filter`, `-Timeout`, `-List`, `-IncludeDotnet`, आणि `-Python` सपोर्ट करते.
- **कोर्स नेव्हिगेशन.** लेसन 11–15 साठी आधी नसलेले मागील/पुढील लेसन दुवे जोडले जेणेकरून संपूर्ण कोर्स 00 → 18 उभ्या आणि आडव्या दोन्ही दिशांनी लिंक होतो.
- **नवीन थंबनेल्स.** लेसन 16 आणि 17 साठी थंबनेल्स, तसेच अद्ययावत रेपो सोशल चित्र [images/repo-thumbnailv3.png](./images/repo-thumbnailv3.png) (आता दोन नवीन लेसन आणि `aka.ms/ai-agents-beginners` URL जाहिरात करते).
- **डिपेंडन्सीज** ([requirements.txt](../../requirements.txt)): लेसन 17 साठी `foundry-local-sdk` आणि `chromadb` जोडले.

### बदलले

- **मुख्य [README.md](./README.md)** लेसन टेबल: लेसन 16 आणि 17 आता त्यांच्याशी संबंधित सामग्रीकडे दुवे करतात (पूर्वी "लवकर येत आहे"); रेपोचे चित्र `repo-thumbnailv3.png` मध्ये बदलले.
- **[STUDY_GUIDE.md](./STUDY_GUIDE.md)**: लेसन-निहाय मार्गदर्शिका आणि शिक्षण मार्गांमध्ये लेसन 16 आणि 17 जोडले, आणि "स्मोक टेस्टसह डिप्लॉय केलेल्या एजंटची पडताळणी" विभाग.
- **[AGENTS.md](./AGENTS.md)**: लेसनची संख्या/वर्णन (00–18) अद्ययावत केली, स्मोक टेस्टिंग पडताळणी विभाग जोडला, आणि लेसन 16/17 नमुना नावकरण उदाहरणे जोडली.
- **[18-securing-ai-agents/README.md](./18-securing-ai-agents/README.md)**: "मागील लेसन" आता लेसन 17 कडे निर्देश करते (पूर्वी लेसन 15), साखळी पूर्ण करते.
- **निषिद्ध नसलेल्या मॉडेल्ससाठी प्रमाणित मॉडेल संदर्भ.** संपूर्ण कोर्समध्ये `gpt-4o` / `gpt-4o-mini` संदर्भ `gpt-4.1-mini` ने बदले (डॉक्स, `.env.example`, Python/.NET नोटबुक्स आणि नमुने) — `gpt-4o` (सर्व आवृत्त्या) 2026 मध्ये निवृत्त होत आहे. लेसन 16 च्या मॉडेल-रूटिंग उदाहरणात `gpt-4.1-mini` (लहान) आणि `gpt-4.1` (मोठा) वापरून लहान/मोठ्या अभिव्यक्ती ठेवली आहे. Python नोटबुक आता वातावरणीय चलांमधून मॉडेल निवडतो (`AZURE_AI_MODEL_DEPLOYMENT_NAME` / `AZURE_OPENAI_DEPLOYMENT`) हार्ड-कोड केलेल्या नावाऐवजी.

### नोंदी व ज्ञात मर्यादा

- **प्रत्यक्ष Azure वर चालवले नाही.** नवीन लेसनचे नोटबुक शैक्षणिक नमुने आहेत; स्वतःच्या Microsoft Foundry / Foundry Local सेटअपवर चालवा आणि पडताळणी करा. स्मोक-टेस्ट वर्कफ्लो साठी आपल्याला लेसनचा एजंट डिप्लॉय करावा लागतो आणि Azure OIDC रहस्ये (`AZURE_CLIENT_ID`, `AZURE_TENANT_ID`, `AZURE_SUBSCRIPTION_ID`) Foundry प्रकल्प श्रेणीवर **Azure AI User** भूमिका सह कॉन्फिगर करावी लागते.
- **लेसन 17 हा फक्त स्थानिक आहे.** याचा Foundry Responses endpoint नाही, त्यामुळे स्मोक-टेस्ट क्रिया लागू होत नाही; नोटबुक आपल्या कार्यस्थानावर चालवून पडताळणी करा.

## [जारी] — 2026-07-06

हा प्रकाशन कोर्सला **Azure OpenAI Responses API** वर स्थलांतरित करतो, उत्पादन नावे **Microsoft Foundry** आणि **Microsoft Agent Framework (MAF)** वर प्रमाणित करतो, GitHub Models निवृत्त करतो, SDK आवृत्त्या अद्ययावत करतो, आणि स्थानिक मॉडेल आणि Foundry वर इतर फ्रेमवर्क होस्टिंग वर नवीन सामग्री जोडतो.

### जोडले

- **स्थानांतरण कौशल्य** — [azure-openai-to-responses](./.agents/skills/azure-openai-to-responses/SKILL.md) एजंट कौशल्य (Azure-Samples/azure-openai-to-responses वरून) `.agents/skills/` अंतर्गत स्थापित केले, ज्यात त्याचे संदर्भ आणि स्कॅनर स्क्रिप्ट आहे.
- **Foundry Local (डिव्हाइसवर मॉडेल्स चालवा)** — [00-course-setup/README.md](./00-course-setup/README.md) मध्ये नवीन "पर्यायी प्रदाता: Foundry Local" विभाग, ज्यात इंस्टॉलेशन (`winget` / `brew`), `foundry model run`, `foundry-local-sdk`, आणि Microsoft Agent Framework ला `OpenAIChatClient` मार्फत वायर्ड करणे समाविष्ट आहे.
- **Microsoft Foundry वर LangChain / LangGraph एजंट होस्टिंग** — [14-microsoft-agent-framework/README.md](./14-microsoft-agent-framework/README.md) मध्ये नवीन विभाग आणि चालवण्याजोगा नमुना [14-langchain-hosted-agent.py](../../14-microsoft-agent-framework/code-samples/14-langchain-hosted-agent.py) जे `langchain-azure-ai[hosting]` आणि `ResponsesHostServer` ( `/responses` प्रोटोकॉल) वापरतो, Microsoft Learn https://learn.microsoft.com/azure/foundry/how-to/develop/langchain-hosted-agents वर आधारित.
- **Microsoft Project Opal** — [15-browser-use/README.md](./15-browser-use/README.md) मध्ये नवीन "प्रत्यक्ष जगाचे उदाहरण: Microsoft Project Opal" विभाग, जे Opal ला उद्योग संगणक-उपयोग एजंट म्हणून फ्रेम करतो आणि कोर्स संकल्पनांना जुळवतो (human-in-the-loop, विश्वास/सुरक्षा, नियोजन, कौशल्ये).
- **दुसरा लेसन 02 Python नमुना** — [02-python-agent-framework-azure-openai.ipynb](./02-explore-agentic-frameworks/code_samples/02-python-agent-framework-azure-openai.ipynb) जोडले (बघा "बदलले" — पूर्वीच्या Semantic Kernel नोटबुकमधून स्थलांतरित) आणि लेसन README मध्ये लिंक केले.
- **मॉडेल्स आणि प्रदाते** विभाग [STUDY_GUIDE.md](./STUDY_GUIDE.md) मध्ये जोडला.

### बदलले

- **चॅट पूर्णता → प्रतिसाद API (Python).** थेट मॉडेल कॉल करणाऱ्या नमुन्यांना चॅट पूर्णता API वरून प्रतिसाद API (`client.responses.create(input=..., store=False)`, `resp.output_text`) कडे स्थलांतरित केले, `OpenAI` क्लायंट वापरून स्थिर Azure OpenAI `/openai/v1/` एंडपॉईंट येथे (कोणताही `api_version` नाही). प्रभावित नमुने खालील प्रमाणे:
  - [06-building-trustworthy-agents/code_samples/06-system-message-framework.ipynb](./06-building-trustworthy-agents/code_samples/06-system-message-framework.ipynb)
  - [06-building-trustworthy-agents/code_samples/06-human-in-the-loop.ipynb](./06-building-trustworthy-agents/code_samples/06-human-in-the-loop.ipynb)
  - [04-tool-use/README.md](./04-tool-use/README.md) — पूर्ण फंक्शन-कॉलिंग वॉकथ्रू (टूल स्कीमा प्रतिसाद स्वरूपात समतल केले, साधन परिणाम `function_call_output`, `max_output_tokens`, इत्यादी म्हणून परतले).

- **GitHub मॉडेल्स → Azure OpenAI.** GitHub मॉडेल्स बंद होत आहेत (जुलै 2026 मध्ये) आणि ते Responses API ला समर्थन देत नाहीत. सर्व GitHub मॉडेल्स कोड मार्ग Python आणि .NET नमुन्यांमध्ये Azure OpenAI / Microsoft Foundry मध्ये रूपांतरित करण्यात आले आहेत:
  - Python: लेसन 08 वर्कफ्लो नोटबुक्स (`01`–`03`), लेसन 14 (`14-handoff`, `14-human-loop`, `hotel_booking_workflow_sample.py`).
  - .NET: `01`–`04`, `07`, `08` `*-dotnet-agent-framework.cs` + संबंधित `.md` दस्तऐवज आणि लेसन 08 dotNET वर्कफ्लो नोटबुक्स/`.md` (`01`–`03`) आता `AzureOpenAIClient(...).GetOpenAIResponseClient(deployment).CreateAIAgent(...)` सह `AzureCliCredential` वापरतात.
- **Semantic Kernel → Microsoft Agent Framework.** पूर्वीचे `02-semantic-kernel.ipynb` पुन्हा लिहिले गेले आणि Microsoft Agent Framework सह Azure OpenAI (Responses API) वापरण्यासाठी नावांतर केले गेले, आता त्याचे नाव `02-python-agent-framework-azure-openai.ipynb` आहे.
- **`FoundryChatClient` + `as_agent` वर एकसंधीकरण.** README आणि नोटबुक कोड ज्यात `AzureAIProjectAgentProvider` संदर्भित केले गेले होते, ते Lesson 01 आणि फ्रेमवर्कच्या स्वत:च्या नमुन्यांमध्ये वापरल्या जाणाऱ्या नियमांवर एकसंध केले गेले आहेत: `FoundryChatClient(project_endpoint=..., model=..., credential=AzureCliCredential())` सह `provider.as_agent(...)`. हे Lesson 02–14 च्या README आणि नोटबुक्समध्ये अद्ययावत केले गेले (उदा., लेसन 13 मेमरी, सर्व लेसन 14 नोटबुक्स, `11-agentic-protocols/code_samples/github-mcp/app.py`).
- **उत्पादन नावे.** इंग्रजी मजकूरात संपूर्ण नावांतर झाले:
  - "Azure AI Foundry" / "Azure AI Studio" → **Microsoft Foundry**
  - "Azure AI Agent Service" → **Microsoft Foundry Agent Service**
  - (बदल नाही: "Azure OpenAI", "Azure AI Search", "Azure AI Inference", आणि पर्यावरण-वेरिएबल नावे.)
- **आश्रितता** ([requirements.txt](../../requirements.txt)):
  - पिन केले `agent-framework>=1.10.0`, `agent-framework-foundry>=1.10.0`, `agent-framework-openai>=1.10.0`.
  - पिन केले `openai>=1.108.1` (Responses API साठी किमान).
  - काढले `azure-ai-inference` (हे फक्त GitHub मॉडेल्स नमुन्यांमध्ये वापरले जात होते जे स्थलांतरित केले गेले).
- **पर्यावरण संरचना** ([.env.example](../../.env.example)): GitHub मॉडेल्स वेरिएबल्स (`GITHUB_TOKEN`, `GITHUB_ENDPOINT`, `GITHUB_MODEL_ID`) काढले; जोडले `AZURE_OPENAI_ENDPOINT`, `AZURE_OPENAI_DEPLOYMENT`, आणि ऐच्छिक `AZURE_OPENAI_API_KEY`; Microsoft Foundry नावांच्या अद्यतनांसह.
- **दस्तऐवज** — वर उल्लेखलेल्या बाबीसाठी [00-course-setup/README.md](./00-course-setup/README.md), [AGENTS.md](./AGENTS.md), [README.md](./README.md), आणि [STUDY_GUIDE.md](./STUDY_GUIDE.md) अद्यतनित केले (सेटअप env वेरिएबल्स, पडताळणी स्निपेट, प्रदाता मार्गदर्शन, नामकरण).

### काढले गेले

- GitHub मॉडेल्स ऑनबोर्डिंग पायऱ्या आणि पर्यावरण वेरिएबल्स सेटअप दस्तऐवजांमधून (Azure OpenAI / Microsoft Foundry ने बदललेले).

### सुरक्षा / गोपनीयता (सार्वजनिक-साहित्य स्वच्छता)

- जुपिटर नोटबुकची अमलात आणलेली आउटपुट साफ केली जिथे प्रत्यक्ष **Azure सदस्यता आयडी**, संसाधन गट / संसाधन नावे, आणि Bing कनेक्शन आयडी लीक झाले होते, तसेच विकसकांची **स्थानिक फाइल मार्ग आणि वापरकर्तानावे**, यामध्ये:
  - `08-multi-agent/code_samples/workflows-agent-framework/dotNET/04.dotnet-agent-framework-workflow-aifoundry-condition.ipynb`
  - `08-multi-agent/code_samples/workflows-agent-framework/python/04.python-agent-framework-workflow-aifoundry-condition.ipynb`
  - `15-browser-use/15-browser-user.ipynb`
- सत्यापित केले की API कीज, टोकन्स, सदस्यता आयडी, किंवा वैयक्तिक मार्ग इंग्रजी सामग्रीमध्ये उरलेले नाहीत (जी `GITHUB_TOKEN` संदर्भ उरलेले आहेत ते GitHub Actions टोकन वर्कफ्लो मध्ये आणि GitHub MCP सर्व्हर PAT लेसन 11 सेटप मध्ये — दोन्ही कायदेशीर आणि GitHub मॉडेल्सशी संबंधित नाहीत).

### नोट्स आणि ज्ञात मर्यादा

- **अमलात आणलेले / संकलित नाहीत.** हे शैक्षणिक नमुने API / नामकरण योग्यतेसाठी अद्ययावत केले गेले आहेत; ते थेट Azure संसाधनांवर रन केले गेले नाही, आणि .NET नमुने या वातावरणात संकलित केले गेले नाहीत. आपल्या स्वत:च्या Microsoft Foundry / Azure OpenAI तैनातीसोबत पडताळणी करा.
- **मॉडेल तैनातीने Responses API ला समर्थन दिले पाहिजे.** `gpt-4.1-mini`, `gpt-4.1`, किंवा `gpt-5.x` मॉडेलसारख्या तैनातीचा वापर करा. जुने मॉडेल्स Responses चे मुख्य कार्यक्षमतेला समर्थन देतात पण प्रत्येक वैशिष्ट्याला नाही.
- **एजंट-फ्रेमवर्क आवृत्ती.** नमुने नवीनतम MAF (`>=1.10.0`) वर लक्ष केंद्रित करतात. मुख्य एजंट-निर्मिती कॉल `client.as_agent(...)` आहे; API फ्रेमवर्कच्या प्रसिद्ध दस्तऐवजांशी आणि स्थापित बिल्डशी पडताळणी करण्यात आले आहे. आपण वेगळी आवृत्ती वापरत असल्यास, पद्धतीची उपलब्धता तपासा (`as_agent` विरुद्ध `create_agent`).
- **लेसन 08 वर्कफ्लो नोटबुक 04** हेतुपुरस्सर `AzureAIAgentClient` (जो `agent-framework-azure-ai` कडून आहे) ठेवतो कारण तो Microsoft Foundry Agent Service होस्ट केलेले टूल्स (Bing ग्राउंडिंग, कोड इंटरप्रिटर) वापरतो; तो आधीच Responses-आधारित आहे.
- **.NET डीफॉल्ट तैनात.** दोन लेसन 08 dotNET वर्कफ्लो नमुने आधी विशिष्ट मॉडेल हार्ड-कॉड केलेले होते; ते आता `AZURE_OPENAI_DEPLOYMENT` (`gpt-4.1-mini`) वर डीफॉल्ट आहेत. जर एखादा नमुना मल्टीमॉडाल/दृष्य इनपुटवर अवलंबून असेल तर `AZURE_OPENAI_DEPLOYMENT` ला योग्य मॉडेल सेट करा.
- **Foundry Local** OpenAI-सुसंगत **Chat Completions** एंडपॉइंट प्रदान करतो आणि स्थानिक विकासासाठी उद्दिष्ट आहे; पूर्ण Responses API वैशिष्ट्यांसाठी Azure OpenAI / Microsoft Foundry वापरा.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**अस्वीकरण**:
हा दस्तऐवज AI भाषांतर सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) चा वापर करून अनुवादित केला आहे. जरी आम्ही अचूकतेसाठी प्रयत्न करतो, तरी कृपया लक्षात घ्या की स्वयंचलित भाषांतरांमध्ये त्रुटी किंवा अचूकतेची कमतरता असू शकते. मूळ दस्तऐवज त्याच्या मूळ भाषेत अधिकृत स्रोत मानला पाहिजे. महत्त्वाची माहिती असल्यास, व्यावसायिक मानवी भाषांतराची शिफारस केली जाते. या भाषांतराच्या वापरामुळे उद्भवणाऱ्या कोणत्याही गैरसमज किंवा चुकीच्या अर्थलावणीसाठी आम्ही जबाबदार नाही.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->