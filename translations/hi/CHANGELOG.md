# परिवर्तन विवरण

**शुरुआत के लिए AI एजेंट्स** कोर्स में सभी महत्वपूर्ण बदलाव इस फ़ाइल में दर्ज किए गए हैं।

## [रिलीज़] — 2026-07-14

यह रिलीज़ कोर्स को दो हाल ही में अव्यवस्थित किए गए मॉडलों से हटाता है, बाकी लर्निंग नोटबुक्स को स्थिर Microsoft Agent Framework API में माइग्रेट करता है, और Python नोटबुक्स को Microsoft Foundry के लाइव डिप्लॉयमेंट के खिलाफ मान्य करता है।

### बदला गया

- **अव्यवस्थित मॉडलों से हटाया गया (`gpt-4.1` / `gpt-4.1-mini` → `gpt-5-mini`)।** दोनों `gpt-4.1` और `gpt-4.1-mini` अब अव्यवस्थित हैं (प्रकाशित सेवानिवृत्ति तिथि **14 अक्टूबर 2026**)। कोर्स के प्रत्येक संदर्भ (दस्तावेज़, `.env.example`, Python/.NET नोटबुक और उदाहरण) को अव्यवस्थित नहीं `gpt-5-mini` से बदला गया है। पाठ 16 के मॉडल-रूटिंग उदाहरण में छोटे/बड़े के लिए `gpt-5-nano` (छोटा) और `gpt-5-mini` (बड़ा) का उपयोग जारी है। थर्ड-पार्टी फ़ाइलें ([15-browser-use/llms.txt](../../15-browser-use/llms.txt)), ऐतिहासिक GitHub Models टेक्स्ट, और `azure-openai-to-responses` कौशल की क्षमता नोट्स जानबूझकर अपरिवर्तित छोड़े गए।
- **पाठ 14 हैंडऑफ नोटबुक को स्थिर API पर माइग्रेट किया गया।** [14-handoff.ipynb](./14-microsoft-agent-framework/code-samples/14-handoff.ipynb) अब `agent_framework.orchestrations.HandoffBuilder` का उपयोग करता है जिसमें `.with_start_agent(...)`, `HandoffAgentUserRequest.create_response(...)`, `event.type`-आधारित स्ट्रीमिंग, और `FoundryChatClient` शामिल हैं (पहले-1.0 `HandoffBuilder`/`ChatMessage`/`RequestInfoEvent` प्रतीकों को हटाते हुए)।
- **पाठ 14 ह्यूमन-इन-द-लूप नोटबुक को स्थिर API में माइग्रेट किया गया।** [14-human-loop.ipynb](./14-microsoft-agent-framework/code-samples/14-human-loop.ipynb) अब `ctx.request_info(...)` + `@response_handler` के माध्यम से पॉज करता है (हटाए गए `RequestInfoExecutor` / `RequestInfoMessage` / `RequestResponse` को बदलते हुए), `WorkflowBuilder(start_executor=..., output_executors=[...])` के साथ बनता है, संरचित आउटपुट `default_options={"response_format": ...}` द्वारा संचालित होता है, और एक स्क्रिप्टेड जवाब का उपयोग करता है ताकि नोटबुक बिना अवरुद्ध किए unattended चले (कोई `input()` ब्लॉक नहीं)।
- **पर्यावरण विन्यास** ([.env.example](../../.env.example)): मॉडल डिप्लॉयमेंट नामों को `gpt-5-mini` में बदला गया; `AZURE_AI_SMALL_MODEL` / `AZURE_AI_LARGE_MODEL` (पाठ 16 रूटिंग) और पहले से गायब `AZURE_OPENAI_CHAT_DEPLOYMENT_NAME` (पाठ 15 ब्राउज़र-उपयोग) जोड़े गए।
- **निर्भरता** ([requirements.txt](../../requirements.txt)): `agent-framework`, `agent-framework-foundry`, और `agent-framework-openai` को `~=1.10.0` पर पिन किया गया ताकि एक आत्म-संगत, वैधित सेट हो (1.11.0 में उन सतहों पर प्रायोगिक ब्रेकिंग परिवर्तन हैं जो ये पाठ उपयोग करते हैं)।

### नोट्स और ज्ञात सीमाएँ

- **लाइव Microsoft Foundry के साथ मान्य किया गया।** Python नोटबुक्स को `nbconvert` के साथ हेडलेस रूप से Microsoft Foundry प्रोजेक्ट के खिलाफ चलाया गया था जिसका उपयोग `gpt-5-mini` (और पाठ 16 रूटिंग के लिए `gpt-5-nano`) करता है। अपने स्वयं के प्रोजेक्ट में समान अव्यवस्थित नहीं मॉडलों को डिप्लॉय करें; नोटबुक्स डिप्लॉयमेंट नाम `AZURE_AI_MODEL_DEPLOYMENT_NAME` / `AZURE_OPENAI_DEPLOYMENT` से पढ़ती हैं।
- **कुछ पाठों के लिए अभी भी अतिरिक्त संसाधनों की आवश्यकता है।** पाठ 05 को Azure AI Search चाहिए; पाठ 08 Bing-ग्राउंडिंग वर्कफ़्लो (`04.python-agent-framework-workflow-aifoundry-condition.ipynb`) को Bing कनेक्शन और Microsoft Foundry Agent Service होस्टेड टूल्स की जरूरत होती है; पाठ 13 (Cognee) और पाठ 17 (Foundry Local) को अपने स्वयं के रनटाइम की आवश्यकता होती है।

## [रिलीज़] — 2026-07-13

यह रिलीज़ दो नए पाठ जोड़ता है जो डिप्लॉयमेंट चाप को पूरा करते हैं — एजेंट्स को Microsoft Foundry तक स्केल करना और एकल वर्कस्टेशन तक डाउन स्केल करना — साथ ही एक स्मोक-टेस्ट पाइपलाइन, ताज़ा कोर्स नेविगेशन, नए शिक्षार्थी कौशल, और अपडेट ब्रांडिंग।

### जोड़ा गया

- **पाठ 16 — Microsoft Foundry के साथ स्केलेबल एजेंट्स डिप्लॉय करना।** नया पाठ [16-deploying-scalable-agents/README.md](./16-deploying-scalable-agents/README.md) और चलने योग्य नोटबुक [16-python-agent-framework.ipynb](./16-deploying-scalable-agents/code_samples/16-python-agent-framework.ipynb) जो एक प्रोडक्शन कस्टमर-सपोर्ट एजेंट बनाता है (टूल्स, RAG, मेमोरी, मॉडल रूटिंग, प्रतिक्रिया कैशिंग, मानव अनुमोदन, एक मूल्यांकन गेट, और OpenTelemetry ट्रेसिंग) के साथ डेवलपमेंट/डिप्लॉयमेंट/रनटाइम मर्मेड आरेख, ज्ञान जांच, असाइनमेंट, और चुनौती।
- **पाठ 17 — Foundry Local और Qwen के साथ स्थानीय AI एजेंट बनाना।** नया पाठ [17-creating-local-ai-agents/README.md](./17-creating-local-ai-agents/README.md) और नोटबुक [17-local-agent-foundry-local.ipynb](./17-creating-local-ai-agents/code_samples/17-local-agent-foundry-local.ipynb) जो पूरी तरह से ऑन-डिवाइस इंजीनियरिंग असिस्टेंट बनाता है (Foundry Local के माध्यम से Qwen फ़ंक्शन कॉलिंग, सैंडबॉक्स्ड फ़ाइल टूल्स, Chroma के साथ स्थानीय RAG, वैकल्पिक स्थानीय MCP) के साथ केवल स्थानीय / स्थानीय-RAG / टूल-कॉलिंग आरेख, ज्ञान जांच, असाइनमेंट और चुनौती।
- **स्मोक-टेस्ट पाइपलाइन।** नया [AI Smoke Test](https://github.com/marketplace/actions/ai-smoke-test) वर्कफ़्लो [.github/workflows/smoke-test.yml](../../.github/workflows/smoke-test.yml) और प्रति-पाठ कैटलॉग [tests/](./tests/README.md) में डिप्लॉयबल एजेंट्स के लिए पाठ 01, 04, 05, और 16, प्रत्येक कैटलॉग को उसके पाठ और होस्टेड-एजेंट नाम के साथ मैप करता इंडेक्स README। पाठ 16 प्राप्त करता है "Validating a Deployed Agent with Smoke Tests" अनुभाग; पाठ 01/04/05 में वैकल्पिक स्मोक-टेस्ट पॉइंटर जोड़ता है।
- **शिक्षार्थी कौशल।** `.agents/skills/` के अंतर्गत नए एजेंट कौशल: [deploying-scalable-agents](./.agents/skills/deploying-scalable-agents/SKILL.md), [local-ai-agents](./.agents/skills/local-ai-agents/SKILL.md) (पाठ 16 और 17 मार्गदर्शन का पैकेज), और [testing-course-samples](./.agents/skills/testing-course-samples/SKILL.md) (कैसे नोटबुक नमूनों को लाइव Microsoft Foundry / Azure OpenAI सेटअप के खिलाफ वैधित करें)।
- **नोटबुक वैधता रनर।** नया [scripts/validate-notebooks.ps1](../../scripts/validate-notebooks.ps1) जो हर Python नोटबुक को `nbconvert` के साथ हेडलेस चलाता है और PASS/FAIL मैट्रिक्स (साथ ही `results.json`) प्रिंट करता है। यह स्वचालित रूप से रेपो रूट और Python का पता लगाता है, डिफ़ॉल्ट रूप से गैर-कोर्स नोटबुक्स (`.venv`, `site-packages`, `translations`, कौशल टेम्पलेट एसेट्स) और `.NET` नोटबुक्स को बाहर करता है, और `-Filter`, `-Timeout`, `-List`, `-IncludeDotnet`, और `-Python` का समर्थन करता है।
- **कोर्स नेविगेशन।** पाठ 11–15 के लिए पिछला/अगला पाठ लिंक जोड़े गए (पहले गायब थे) ताकि पूरा कोर्स दोनों दिशाओं में 00 → 18 तक जुड़ जाए।
- **नए थंबनेल।** पाठ 16 और 17 के लिए पाठ थंबनेल, साथ ही एक नई रिपॉजिटरी सोशल छवि [images/repo-thumbnailv3.png](./images/repo-thumbnailv3.png) (जो अब दो नए पाठों और `aka.ms/ai-agents-beginners` URL का प्रचार करती है)।
- **निर्भरता** ([requirements.txt](../../requirements.txt)): पाठ 17 के लिए `foundry-local-sdk` और `chromadb` जोड़े गए।

### बदला गया

- **मुख्य [README.md](./README.md)** पाठ तालिका: पाठ 16 और 17 अब उनके सामग्री से लिंक करते हैं (पहले "जल्द आ रहा है"); रिपॉजिटरी चित्र अपग्रेड होकर `repo-thumbnailv3.png` हुआ।
- **[STUDY_GUIDE.md](./STUDY_GUIDE.md)**: पाठ 16 और 17 को पाठ-दर-पाठ गाइड और सीखने के रास्तों में जोड़ा गया, और "Validating Deployed Agents with Smoke Tests" अनुभाग जोड़ा गया।
- **[AGENTS.md](./AGENTS.md)**: पाठ संख्या/विवरण (00–18) अपडेट किया गया, स्मोक-टेस्टिंग वेलिडेशन सेक्शन जोड़ा गया, और पाठ 16/17 नमूना नामकरण उदाहरण जोड़े गए।
- **[18-securing-ai-agents/README.md](./18-securing-ai-agents/README.md)**: "पिछला पाठ" अब पाठ 17 की ओर इशारा करता है (पहले पाठ 15 था), चेन बंद करता है।
- **अब गैर-अव्यवस्थित मॉडलों पर मानकीकृत मॉडल संदर्भ।** पूरे कोर्स के सभी `gpt-4o` / `gpt-4o-mini` संदर्भों (दस्तावेज़, `.env.example`, Python/.NET नोटबुक्स और नमूने) को `gpt-4.1-mini` से बदला गया — `gpt-4o` (सभी संस्करण) 2026 में सेवानिवृत्त हो रहा है। पाठ 16 के मॉडल-रूटिंग उदाहरण में छोटे/बड़े के लिए `gpt-4.1-mini` (छोटा) और `gpt-4.1` (बड़ा) का उपयोग जारी है। Python नोटबुक अब मॉडल को पर्यावरण चर (`AZURE_AI_MODEL_DEPLOYMENT_NAME` / `AZURE_OPENAI_DEPLOYMENT`) से चुनते हैं न कि हार्डकोडेड मॉडल नाम से।

### नोट्स और ज्ञात सीमाएँ

- **लाइव Azure के खिलाफ नहीं चलाया गया।** नए पाठों के नोटबुक शैक्षिक नमूने हैं; उन्हें अपने Microsoft Foundry / Foundry Local सेटअप के खिलाफ चलाएं और मान्य करें। स्मोक-टेस्ट वर्कफ़्लो के लिए आवश्यक है कि आप पाठ के एजेंट को डिप्लॉय करें और Azure OIDC गुप्त (`AZURE_CLIENT_ID`, `AZURE_TENANT_ID`, `AZURE_SUBSCRIPTION_ID`) को Foundry प्रोजेक्ट स्कोप में **Azure AI User** भूमिका के साथ कॉन्फ़िगर करें।
- **पाठ 17 केवल स्थानीय है।** इसका कोई Foundry Responses अंतबिंदु नहीं है, इसलिए स्मोक-टेस्ट कार्रवाई लागू नहीं होती; इसे अपने वर्कस्टेशन पर नोटबुक चलाकर मान्य करें।

## [रिलीज़] — 2026-07-06

यह रिलीज़ कोर्स को **Azure OpenAI Responses API** में माइग्रेट करता है, उत्पाद नामकरण को **Microsoft Foundry** और **Microsoft Agent Framework (MAF)** पर मानकीकृत करता है, GitHub Models को सेवानिवृत्त करता है, SDK संस्करण अपडेट करता है, और स्थानीय मॉडल्स और Foundry पर अन्य फ्रेमवर्क होस्टिंग पर नई सामग्री जोड़ता है।

### जोड़ा गया

- **माइग्रेशन कौशल** — `.agents/skills/` के अंतर्गत इंस्टॉल किया गया [`azure-openai-to-responses`](./.agents/skills/azure-openai-to-responses/SKILL.md) एजेंट स्किल (Azure-Samples/azure-openai-to-responses) सहित इसके संदर्भ और स्कैनर स्क्रिप्ट।
- **Foundry Local (डिवाइस पर मॉडल चलाएं)** — [00-course-setup/README.md](./00-course-setup/README.md) में नया "वैकल्पिक प्रदाता: Foundry Local" अनुभाग जिसमें इंस्टॉल (`winget` / `brew`), `foundry model run`, `foundry-local-sdk`, और Microsoft Agent Framework के साथ `FoundryLocalManager` को `OpenAIChatClient` के माध्यम से वायरिंग।
- **Microsoft Foundry पर LangChain / LangGraph एजेंट होस्टिंग** — [14-microsoft-agent-framework/README.md](./14-microsoft-agent-framework/README.md) में नया अनुभाग और चलने योग्य उदाहरण [14-langchain-hosted-agent.py](../../14-microsoft-agent-framework/code-samples/14-langchain-hosted-agent.py) जो `langchain-azure-ai[hosting]` और `ResponsesHostServer` ( `/responses` प्रोटोकॉल) का उपयोग करता है, Microsoft Learn पर आधारित ([Microsoft Learn](https://learn.microsoft.com/azure/foundry/how-to/develop/langchain-hosted-agents))।
- **Microsoft Project Opal** — [15-browser-use/README.md](./15-browser-use/README.md) में नया "वास्तविक दुनिया का उदाहरण: Microsoft Project Opal" अनुभाग जो Opal को एंटरप्राइज़ कंप्यूटर-उपयोग एजेंट के रूप में फ्रेम करता है और इसे कोर्स अवधारणाओं (ह्यूमन-इन-द-लूप, ट्रस्ट/सुरक्षा, योजना, कौशल) के साथ मैप करता है।
- **दूसरा पाठ 02 Python उदाहरण** — [02-python-agent-framework-azure-openai.ipynb](./02-explore-agentic-frameworks/code_samples/02-python-agent-framework-azure-openai.ipynb) जोड़ा गया (देखें "बदला गया" — पूर्व सेमैटिक कर्नेल नोटबुक से माइग्रेट किया गया) और इसे पाठ README में लिंक किया गया।
- [STUDY_GUIDE.md](./STUDY_GUIDE.md) में "मॉडल्स और प्रदाता" अनुभाग जोड़ा गया।

### बदला गया

- **Chat Completions → Responses API (Python)।** मॉडल को सीधे कॉल करने वाले नमूने Chat Completions से Responses API (`client.responses.create(input=..., store=False)`, `resp.output_text`) में माइग्रेट किए गए, `OpenAI` क्लाइंट के साथ स्थिर Azure OpenAI `/openai/v1/` एंडपॉइंट (कोई `api_version` नहीं) का उपयोग करते हुए। प्रभावित नमूनों में शामिल हैं:
  - [06-building-trustworthy-agents/code_samples/06-system-message-framework.ipynb](./06-building-trustworthy-agents/code_samples/06-system-message-framework.ipynb)
  - [06-building-trustworthy-agents/code_samples/06-human-in-the-loop.ipynb](./06-building-trustworthy-agents/code_samples/06-human-in-the-loop.ipynb)
  - [04-tool-use/README.md](./04-tool-use/README.md) — पूर्ण फ़ंक्शन-कॉलिंग वॉकथ्रू (टूल स्कीमा को Responses फॉर्मेट में समतल किया गया, टूल परिणाम `function_call_output`, `max_output_tokens`, आदि के रूप में लौटाए गए)।

- **GitHub मॉडल → Azure OpenAI।** GitHub मॉडल अब समाप्त हो रहे हैं (अगस्त 2026 में बंद) और Responses API का समर्थन नहीं करते। सभी GitHub मॉडल कोड पथ को Python और .NET नमूनों के पार Azure OpenAI / Microsoft Foundry में परिवर्तित किया गया है:
  - Python: Lesson 08 वर्कफ़्लो नोटबुक्स (`01`–`03`), Lesson 14 (`14-handoff`, `14-human-loop`, `hotel_booking_workflow_sample.py`)।
  - .NET: `01`–`04`, `07`, `08` `*-dotnet-agent-framework.cs` + सहयोगी `.md` दस्तावेज़, और Lesson 08 dotNET वर्कफ़्लो नोटबुक्स/`.md` (`01`–`03`) अब `AzureOpenAIClient(...).GetOpenAIResponseClient(deployment).CreateAIAgent(...)` का उपयोग करते हैं `AzureCliCredential` के साथ।
- **Semantic Kernel → Microsoft Agent Framework।** पूर्व `02-semantic-kernel.ipynb` को Microsoft Agent Framework के साथ Azure OpenAI (Responses API) का उपयोग करने के लिए पुनर्लिखित किया गया और इसे `02-python-agent-framework-azure-openai.ipynb` के नाम से पुनः नामित किया गया।
- **`FoundryChatClient` + `as_agent` पर मानकीकरण।** README और नोटबुक कोड जो `AzureAIProjectAgentProvider` को संदर्भित करता था, उसे Lesson 01 और फ्रेमवर्क के अपने नमूनों द्वारा उपयोग किए गए आधिकारिक पैटर्न पर मानकीकृत किया गया: `FoundryChatClient(project_endpoint=..., model=..., credential=AzureCliCredential())` के साथ `provider.as_agent(...)`। Lesson 02–14 के README और नोटबुक्स (जैसे Lesson 13 की मेमोरी, सभी Lesson 14 नोटबुक, `11-agentic-protocols/code_samples/github-mcp/app.py`) में अपडेट किया गया।
- **उत्पाद नामकरण।** अंग्रेज़ी सामग्री में पूरे नाम बदले गए:
  - "Azure AI Foundry" / "Azure AI Studio" → **Microsoft Foundry**
  - "Azure AI Agent Service" → **Microsoft Foundry Agent Service**
  - (बिना बदलाव: "Azure OpenAI", "Azure AI Search", "Azure AI Inference", और पर्यावरण-चर नाम।)
- **निर्भरता** ([requirements.txt](../../requirements.txt)):
  - फिक्स्ड `agent-framework>=1.10.0`, `agent-framework-foundry>=1.10.0`, `agent-framework-openai>=1.10.0`।
  - फिक्स्ड `openai>=1.108.1` (Responses API के लिए न्यूनतम)।
  - `azure-ai-inference` हटा दिया गया (केवल माइग्रेट किए गए GitHub मॉडलों के नमूनों द्वारा उपयोग किया जाता था)।
- **पर्यावरण कॉन्फ़िगरेशन** ([.env.example](../../.env.example)): GitHub मॉडल वेरिएबल्स (`GITHUB_TOKEN`, `GITHUB_ENDPOINT`, `GITHUB_MODEL_ID`) हटा दिए गए; `AZURE_OPENAI_ENDPOINT`, `AZURE_OPENAI_DEPLOYMENT`, और वैकल्पिक `AZURE_OPENAI_API_KEY` जोड़े गए; Microsoft Foundry के नामकरण को अपडेट किया गया।
- **दस्तावेज़** — ऊपर के लिए [00-course-setup/README.md](./00-course-setup/README.md), [AGENTS.md](./AGENTS.md), [README.md](./README.md), और [STUDY_GUIDE.md](./STUDY_GUIDE.md) को अपडेट किया (सेटअप env vars, सत्यापन स्निपेट, प्रदाता मार्गदर्शन, नामकरण)।

### हटाए गए

- GitHub मॉडल ऑनबोर्डिंग चरण और पर्यावरण चर सेटअप दस्तावेज़ों से (Azure OpenAI / Microsoft Foundry द्वारा प्रतिस्थापित)।

### सुरक्षा / गोपनीयता (सार्वजनिक साझा करने की सफाई)

- Jupyter नोटबुक निष्पादन आउटपुट साफ़ किए गए जिनमें एक असली **Azure सब्सक्रिप्शन ID**, संसाधन समूह / संसाधन नाम, और Bing कनेक्शन ID के साथ-साथ डेवलपर **स्थानीय फ़ाइल पथ और उपयोगकर्ता नाम** लीक हुए थे, इनमें:
  - `08-multi-agent/code_samples/workflows-agent-framework/dotNET/04.dotnet-agent-framework-workflow-aifoundry-condition.ipynb`
  - `08-multi-agent/code_samples/workflows-agent-framework/python/04.python-agent-framework-workflow-aifoundry-condition.ipynb`
  - `15-browser-use/15-browser-user.ipynb`
- सुनिश्चित किया गया कि ट्रैक किए गए अंग्रेजी सामग्री में कोई API कुंजी, टोकन, सदस्यता ID या व्यक्तिगत पथ नहीं रहे (जो शेष `GITHUB_TOKEN` संदर्भ हैं, वे GitHub Actions टोकन और GitHub MCP सर्वर PAT के लिए वैध हैं और GitHub मॉडल से संबंधित नहीं हैं)।

### नोट्स और ज्ञात सीमाएं

- **निष्पादित/कंपाइल नहीं किया गया।** ये शैक्षिक नमूने API/नामकरण सटीकता के लिए अपडेट किए गए हैं; इन्हें लाइव Azure संसाधनों पर नहीं चलाया गया, और .NET नमूने इस वातावरण में कंपाइल नहीं किए गए। अपनी Microsoft Foundry / Azure OpenAI तैनाती के विरुद्ध सत्यापित करें।
- **मॉडल तैनाती को Responses API का समर्थन करना चाहिए।** `gpt-4.1-mini`, `gpt-4.1`, या `gpt-5.x` मॉडल जैसे तैनाती का उपयोग करें। पुराने मॉडल मूल Responses कार्यक्षमता का समर्थन करते हैं लेकिन हर फीचर का नहीं।
- **एजेंट-फ्रेमवर्क संस्करण।** नमूने नवीनतम MAF (`>=1.10.0`) को लक्षित करते हैं। आधिकारिक एजेंट-निर्माण कॉल `client.as_agent(...)` है; APIs को फ्रेमवर्क के प्रकाशित दस्तावेज़ और एक स्थापित बिल्ड के विरुद्ध सत्यापित किया गया। यदि आप अलग संस्करण पिन करते हैं, तो विधि उपलब्धता की पुष्टि करें (`as_agent` बनाम `create_agent`)।
- **Lesson 08 वर्कफ़्लो नोटबुक 04** जानबूझकर `AzureAIAgentClient` (जो `agent-framework-azure-ai` से है) रखता है क्योंकि यह Microsoft Foundry Agent Service होस्टेड उपकरणों का उपयोग करता है (Bing grounding, कोड इंटरप्रिटर); यह पहले से ही Responses आधारित है।
- **.NET डिफ़ॉल्ट तैनाती।** दो Lesson 08 dotNET वर्कफ़्लो नमूने पूर्व में एक विशिष्ट मॉडल को हार्ड-कोड करते थे; अब वे डिफ़ॉल्ट रूप से `AZURE_OPENAI_DEPLOYMENT` (`gpt-4.1-mini`) का उपयोग करते हैं। यदि कोई नमूना मल्टीमोडल/विजन इनपुट पर निर्भर करता है, तो इसे उपयुक्त मॉडल पर सेट करें।
- **Foundry Local** एक OpenAI-अनुकूल **Chat Completions** एंडपॉइंट प्रदान करता है और स्थानीय विकास के लिए है; पूरे Responses API फीचर सेट के लिए Azure OpenAI / Microsoft Foundry का उपयोग करें।

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**अस्वीकरण**:
इस दस्तावेज़ का अनुवाद AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) का उपयोग करके किया गया है। जबकि हम सटीकता के लिए प्रयास करते हैं, कृपया ध्यान दें कि स्वचालित अनुवादों में त्रुटियाँ या अशुद्धियाँ हो सकती हैं। मूल दस्तावेज़ अपनी मूल भाषा में ही प्रामाणिक स्रोत माना जाना चाहिए। महत्वपूर्ण जानकारी के लिए, पेशेवर मानव अनुवाद की सिफारिश की जाती है। इस अनुवाद के उपयोग से उत्पन्न किसी भी गलतफहमी या गलत व्याख्या के लिए हम उत्तरदायी नहीं हैं।
<!-- CO-OP TRANSLATOR DISCLAIMER END -->