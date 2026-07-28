# परिवर्तन विवरण

**शुरुआतीहरूको लागि एआई एजेन्टहरू** कोर्सका सबै उल्लेखनीय परिवर्तनहरू यस फाइलमा दस्तावेज गरिएको छ।

## [रिलीज गरिएको] — 2026-07-14

यस रिलिजले कोर्सलाई दुई नयाँ रूपमा निकाला गरिएका मोडेलहरूबाट हटाएर बाँकी पाठ नोटबुकहरूलाई स्थिर Microsoft Agent Framework API मा माइग्रेट गर्दछ र Python नोटबुकहरूलाई प्रत्यक्ष Microsoft Foundry परिनियोजनसँग प्रमाणित गर्दछ।

### परिवर्तनहरू

- **निकाला गरिएका मोडेलहरूबाट हटाइयो (`gpt-4.1` / `gpt-4.1-mini` → `gpt-5-mini`)।** दुबै `gpt-4.1` र `gpt-4.1-mini` अहिले निकाला गरिएका छन् (प्रकाशित अवकाश मिति **14 अक्टोबर 2026**). कोर्सको हरेक सन्दर्भ (डकुमेन्टहरू, `.env.example`, Python/.NET नोटबुक र नमूनाहरू) लाई गैर-निकाला गरिएको `gpt-5-mini` सँग प्रतिस्थापन गरियो। पाठ १६ को मोडेल-राउटिंग उदाहरणले सानो/ठूलो अन्तर देखाउन `gpt-5-nano` (सानो) र `gpt-5-mini` (ठूलो) प्रयोग गरिराखेको छ। तेस्रो-पार्टी फाइलहरू ([15-browser-use/llms.txt](../../15-browser-use/llms.txt)), ऐतिहासिक GitHub मोडेलहरूका टेक्स्ट र `azure-openai-to-responses` कौशलको क्षमता नोटहरू जानाजानी परिवर्तन नगरिएका छन्।
- **पाठ १४ ह्यान्डअफ नोटबुक स्थिर API मा माइग्रेट भयो।** [14-handoff.ipynb](./14-microsoft-agent-framework/code-samples/14-handoff.ipynb) अब `agent_framework.orchestrations.HandoffBuilder` सँग `.with_start_agent(...)`, `HandoffAgentUserRequest.create_response(...)`, `event.type`-आधारित स्ट्रिमिङ, र `FoundryChatClient` प्रयोग गर्छ (पहिले हटाइएका pre-1.0 `HandoffBuilder`/`ChatMessage`/`RequestInfoEvent` प्रतीकहरू प्रतिस्थापन गर्दै)।
- **पाठ १४ मानव-इन-द-लूप नोटबुक स्थिर API मा माइग्रेट भयो।** [14-human-loop.ipynb](./14-microsoft-agent-framework/code-samples/14-human-loop.ipynb) अब `ctx.request_info(...)` + `@response_handler` मार्फत पज गर्दछ (हटाइएका `RequestInfoExecutor` / `RequestInfoMessage` / `RequestResponse` को स्थानमा), `WorkflowBuilder(start_executor=..., output_executors=[...])` सँग बनाइन्छ, `default_options={"response_format": ...}` मार्फत संरचित आउटपुट चलाउँछ, र स्क्रिप्ट गरिएको जवाफ प्रयोग गर्छ ताकि नोटबुक आफैं चल्न सकोस् (कुनै अवरोध गर्ने `input()` छैन)।
- **वातावरण कन्फिगरेसन** ([.env.example](../../.env.example)): मोडेल परिनियोजन नामहरू `gpt-5-mini` मा स्विच गरियो; `AZURE_AI_SMALL_MODEL` / `AZURE_AI_LARGE_MODEL` (पाठ १६ राउटिंग), र पहिलेदेखि अभाव भएको `AZURE_OPENAI_CHAT_DEPLOYMENT_NAME` (पाठ १५ ब्राउजर-उपयोग) थपियो।
- **निर्भरता** ([requirements.txt](../../requirements.txt)): `agent-framework`, `agent-framework-foundry`, र `agent-framework-openai` लाई `~=1.10.0` मा पिन गरियो ताकि स्व-संगत, प्रमाणित सेट मिलोस् (1.11.0 मा प्रयोग भएका उपकरणहरूमा प्रयोगात्मक ब्रेकिङ परिवर्तनहरू छन्)।

### नोट र ज्ञात सीमाहरू

- **प्रत्यक्ष Microsoft Foundry मा प्रमाणित।** Python नोटबुकहरू `nbconvert` मार्फत हेडलेस रूपमा Microsoft Foundry प्रोजेक्टमा `gpt-5-mini` (र पाठ १६ राउटिंगका लागि `gpt-5-nano`) सँग चलाइएको थियो। आफ्नै प्रोजेक्टमा बराबर गैर-निकाला मोडेलहरू परिनियोजन गर्नुहोस्; नोटबुकहरूले परिनियोजन नाम `AZURE_AI_MODEL_DEPLOYMENT_NAME` / `AZURE_OPENAI_DEPLOYMENT` बाट पढ्छन्।
- **अझै केही पाठहरूका लागि अतिरिक्त स्रोतहरू आवश्यक।** पाठ ०५ लाई Azure AI Search चाहिन्छ; पाठ ०८ को Bing-ग्राउन्डिङ् कार्यप्रवाह (`04.python-agent-framework-workflow-aifoundry-condition.ipynb`) लाई Bing कनेक्शन र Microsoft Foundry Agent Service होस्ट गरिएका उपकरणहरू चाहिन्छ; पाठ १३ (Cognee) र पाठ १७ (Foundry Local) लाई आफ्नै रनटाइमहरू आवश्यक छन्।

## [रिलीज गरिएको] — 2026-07-13

यस रिलिजले दुई नयाँ पाठहरू थप्छ जुन परिनियोजन चक्र पूरा गर्छन् — Microsoft Foundry सम्म एजेन्टहरू विस्तार गर्ने र एकल वर्कस्टेशनमा घटाउने — साथै स्मोक-टेस्ट पाइपलाइन, नवीनीकृत कोर्स नेभिगेसन, नयाँ सिक्ने कौशलहरू, र अद्यावधिक ब्रान्डिङ्ग।

### थपिएका

- **पाठ १६ — Microsoft Foundry सँग स्केलेबल एजेन्टहरू परिनियोजन गर्दै।** नयाँ पाठ [16-deploying-scalable-agents/README.md](./16-deploying-scalable-agents/README.md) र चलाउन मिल्ने नोटबुक [16-python-agent-framework.ipynb](./16-deploying-scalable-agents/code_samples/16-python-agent-framework.ipynb) जसले उत्पादन ग्राहक-सहायता एजेन्ट निर्माण गर्छ (उपकरणहरू, RAG, मेमोरी, मोडेल राउटिंग, प्रतिक्रिया क्यासिङ्, मानव अनुमोदन, मूल्याङ्कन गेट, र OpenTelemetry ट्रेसिङ), विकास/परिनियोजन/रनटाइम Mermaid चित्रहरू, ज्ञान जाँच, असाइनमेन्ट, र चुनौतीसहित।
- **पाठ १७ — Foundry Local र Qwen सँग स्थानीय AI एजेन्टहरू सिर्जना गर्दै।** नयाँ पाठ [17-creating-local-ai-agents/README.md](./17-creating-local-ai-agents/README.md) र नोटबुक [17-local-agent-foundry-local.ipynb](./17-creating-local-ai-agents/code_samples/17-local-agent-foundry-local.ipynb) जसले पूर्ण रूपमा उपकरणमाथि आधारित इञ्जिनियरिङ सहायक निर्माण गर्छ (Qwen कार्य कलिङ् Foundry Local मार्फत, स्यान्डबक्स गरिएको फाइल उपकरणहरू, स्थानीय RAG Chroma सँग, वैकल्पिक स्थानीय MCP), स्थानीय मात्र / स्थानीय-RAG / उपकरण-कलिङ चित्रहरू, ज्ञान जाँच, असाइनमेन्ट, र चुनौतीसहित।
- **स्मोक-टेस्ट पाइपलाइन।** नयाँ [AI Smoke Test](https://github.com/marketplace/actions/ai-smoke-test) कार्यप्रवाह [.github/workflows/smoke-test.yml](../../.github/workflows/smoke-test.yml) र पाठहरू ०१, ०४, ०५, र १६ मा परिनियोज्य एजेन्टहरूको लागि [tests/](./tests/README.md) अन्तर्गत क्याटलगहरू, प्रत्येक क्याटलगलाई सम्बन्धित पाठ र होस्ट गरिएको एजेन्ट नामसँग जोड्ने इन्डेक्स README सहित। पाठ १६ मा "परिनियोजित एजेन्टलाई स्मोक टेस्टहरूसँग प्रमाणित गर्दै" शीर्षक थपियो; पाठहरू ०१/०४/०५ मा वैकल्पिक स्मोक-टेस्ट संकेतक थपियो।
- **सिक्ने कौशलहरू।** `.agents/skills/` मा नयाँ एजेन्ट कौशलहरू: [deploying-scalable-agents](./.agents/skills/deploying-scalable-agents/SKILL.md), [local-ai-agents](./.agents/skills/local-ai-agents/SKILL.md) (पाठ १६ र १७ मार्गदर्शन प्याकेजिङ), र [testing-course-samples](./.agents/skills/testing-course-samples/SKILL.md) (नोटबुक नमूना प्रमाणन कसरी गर्ने प्रत्यक्ष Microsoft Foundry / Azure OpenAI सेटअपसँग)।
- **नोटबुक प्रमाणन रनर।** नयाँ [scripts/validate-notebooks.ps1](../../scripts/validate-notebooks.ps1) जुन प्रत्येक Python नोटबुकलाई `nbconvert` सँग हेडलेस चलाउने र PASS/FAIL म्याट्रिक्स प्रिन्ट गर्ने (साथै `results.json`) गर्दछ। यो रिपो रूट र Python आफैं पत्ता लगाउँछ, गैर-कोर्स नोटबुकहरू (`.venv`, `site-packages`, `translations`, कौशल टेम्प्लेट एसेटहरू) र `.NET` नोटबुकहरूलाई पूर्वनिर्धारित रूपमा बाहिर राख्छ, र `-Filter`, `-Timeout`, `-List`, `-IncludeDotnet`, र `-Python` लाई समर्थन गर्दछ।
- **कोर्स नेभिगेसन।** पाठहरू ११–१५ मा पहिले अभाव रहेको पुरानो/अर्को पाठको लिङ्क थपियो ताकि पुरा कोर्स ०० → १८ दुवै दिशामा श्रृंखलाबद्ध होस्।
- **नयाँ थम्बनेलहरू।** पाठ १६ र १७ का थम्बनेलहरू, साथै नवीनीकृत रिपोजिटरी सामाजिक छवि [images/repo-thumbnailv3.png](./images/repo-thumbnailv3.png) जसले दुई नयाँ पाठहरू र `aka.ms/ai-agents-beginners` URL प्रचार गर्दछ।
- **निर्भरता** ([requirements.txt](../../requirements.txt)): पाठ १७ का लागि `foundry-local-sdk` र `chromadb` थपियो।

### परिवर्तनहरू

- **मुख्य [README.md](./README.md)** पाठ तालिका: पाठ १६ र १७ अब तिनका सामग्रीमा लिङ्क हुन्छन् (पहिले "शीघ्र आउँदै"); रिपोजिटरी छवि `repo-thumbnailv3.png` मा बढाइयो।
- **[STUDY_GUIDE.md](./STUDY_GUIDE.md)**: पाठ-द्वारा-पाठ मार्गदर्शक र सिकाइ पथहरूमा पाठ १६ र १७ थपियो, साथै "स्मोक टेस्टहरूसँग परिनियोजित एजेन्टहरू प्रमाणित गर्दै" शीर्षक थपियो।
- **[AGENTS.md](./AGENTS.md)**: पाठ संख्या/वर्णन अपडेट गरियो (००–१८), स्मोक-टेस्टिङ प्रमाणन खण्ड थपियो, र पाठ १६/१७ नमुना नामकरण उदाहरणहरू थपियो।
- **[18-securing-ai-agents/README.md](./18-securing-ai-agents/README.md)**: "अघिल्लो पाठ" अब पाठ १७ लाई सूचित गर्छ (पहिले पाठ १५ थियो), श्रृंखला बन्द गर्दै।
- **गैर-निकाला मोडेलहरूमा मापदण्डित मोडेल सन्दर्भहरू।** समूला `gpt-4o` / `gpt-4o-mini` सन्दर्भहरू पाठभरि (डकुमेन्ट, `.env.example`, Python/.NET नोटबुक र नमूनाहरू) `gpt-4.1-mini` सँग प्रतिस्थापन गरियो — `gpt-4o` (सबै संस्करणहरू) सन् २०२६ मा अवकाश हुँदैछ। पाठ १६ को मोडेल-राउटिंग उदाहरणले सानो/ठूलो अन्तर देखाउन `gpt-4.1-mini` (सानो) र `gpt-4.1` (ठूलो) प्रयोग गरिरहेका छन्। Python नोटबुकहरूले अब मोडेल वातावरण चरहरूबाट चयन गर्छन् (`AZURE_AI_MODEL_DEPLOYMENT_NAME` / `AZURE_OPENAI_DEPLOYMENT`) सट्टा हाड-कोडिङ मोडेल नाम।

### नोट र ज्ञात सीमाहरू

- **प्रत्यक्ष Azure सँग चलाइएको छैन।** नयाँ पाठहरूका नोटबुकहरू शिक्षण नमूना हुन्; तिनीहरूलाई आफ्नै Microsoft Foundry / Foundry Local सेटअपसँग चलाउनुहोस् र प्रमाणित गर्नुहोस्। स्मोक-टेस्ट कार्यप्रवाहले पाठको एजेन्ट परिनियोजन र Azure OIDC गुप्तचरहरू (`AZURE_CLIENT_ID`, `AZURE_TENANT_ID`, `AZURE_SUBSCRIPTION_ID`) Foundry प्रोजेक्ट स्कोपमा **Azure AI User** भूमिकासहित कन्फिगर गर्न आवश्यक छ।
- **पाठ १७ स्थानीय मात्र हो।** यसको Foundry Responses अन्तबिन्दु छैन, त्यसैले स्मोक-टेस्ट क्रिया लागू हुँदैन; नोटबुक आफ्नो वर्कस्टेशनमा चलाएर प्रमाणित गर्नुहोस्।

## [रिलीज गरिएको] — 2026-07-06

यस रिलिजले कोर्सलाई **Azure OpenAI Responses API** मा माइग्रेट गर्दछ, उत्पादन नामाकरण Microsoft Foundry र Microsoft Agent Framework (MAF) मा मानकीकृत गर्दछ, GitHub मोडेलहरू अवकाश गर्दछ, SDK संस्करणहरू अपडेट गर्दछ, र स्थानीय मोडेलहरू र Foundry मा अन्य फ्रेमवर्कहरू होस्ट गर्ने नयाँ सामग्री थप्दछ।

### थपिएका

- **माइग्रेशन कौशल** — [`azure-openai-to-responses`](./.agents/skills/azure-openai-to-responses/SKILL.md) एजेन्ट कौशल स्थापना गरिएको (Azure-Samples/azure-openai-to-responses बाट) `.agents/skills/` अन्तर्गत, यसको सन्दर्भहरू र स्क्यानर स्क्रिप्ट सहित।
- **Foundry Local (मोडेलहरू उपकरणमै चलाउनुहोस्)** — [00-course-setup/README.md](./00-course-setup/README.md) मा नयाँ "वैकल्पिक प्रदायक: Foundry Local" खण्ड जसमा स्थापना (`winget` / `brew`), `foundry model run`, `foundry-local-sdk`, र Microsoft Agent Framework जडानका लागि `FoundryLocalManager` र `OpenAIChatClient` समेटिएका छन्।
- **Microsoft Foundry मा LangChain / LangGraph एजेन्टहरू होस्ट गर्दै** — [14-microsoft-agent-framework/README.md](./14-microsoft-agent-framework/README.md) मा नयाँ खण्ड, साथै `langchain-azure-ai[hosting]` र `ResponsesHostServer` (`/responses` प्रोटोकल) प्रयोग गर्ने चलाउन मिल्ने नमूना [14-langchain-hosted-agent.py](../../14-microsoft-agent-framework/code-samples/14-langchain-hosted-agent.py), Microsoft Learn मा आधारित [https://learn.microsoft.com/azure/foundry/how-to/develop/langchain-hosted-agents](https://learn.microsoft.com/azure/foundry/how-to/develop/langchain-hosted-agents) ।
- **Microsoft Project Opal** — [15-browser-use/README.md](./15-browser-use/README.md) मा नयाँ "वास्तविक विश्व उदाहरण: Microsoft Project Opal" खण्ड, जसले Opal लाई उद्यम कम्प्युटर-प्रयोग एजेन्टको रूपमा चित्रण गर्दछ र कोर्स अवधारणाहरूमा मिलाउँछ (मानव-इन-द-लूप, ट्रस्ट/सुरक्षा, योजना, कौशल)।
- **दोश्रो पाठ ०२ Python नमूना** — [02-python-agent-framework-azure-openai.ipynb](./02-explore-agentic-frameworks/code_samples/02-python-agent-framework-azure-openai.ipynb) थपियो ("परिवर्तन" हेर्नुहोस् — पुरानो Semantic Kernel नोटबुकबाट माइग्रेट गरिएको) र यसलाई पाठ README मा लिंक गरियो।
- **मोडेल र प्रदायकहरू** खण्ड [STUDY_GUIDE.md](./STUDY_GUIDE.md) मा थपियो।

### परिवर्तनहरू

- **च्याट कम्प्लेसन्स → Responses API (Python)।** मोडेललाई सिधै बोलाउने नमूनाहरू Chat Completions बाट Responses API (`client.responses.create(input=..., store=False)`, `resp.output_text`) मा माइग्रेट गरियो, स्थिर Azure OpenAI `/openai/v1/` अन्तबिन्दु (`api_version` बिना) सँग `OpenAI` क्लाइन्ट प्रयोग गरेर। प्रभावित नमूनाहरूमा समावेश छन्:
  - [06-building-trustworthy-agents/code_samples/06-system-message-framework.ipynb](./06-building-trustworthy-agents/code_samples/06-system-message-framework.ipynb)
  - [06-building-trustworthy-agents/code_samples/06-human-in-the-loop.ipynb](./06-building-trustworthy-agents/code_samples/06-human-in-the-loop.ipynb)
  - [04-tool-use/README.md](./04-tool-use/README.md) — पूर्ण फंक्शन-कलिङ वाकथ्रु (उपकरण स्किमालाई Responses ढाँचामा समतल पार्दै, उपकरण नतिजा `function_call_output`, `max_output_tokens`, आदि रूपमा फर्काउने)।

- **GitHub मोडेलहरू → Azure OpenAI।** GitHub मोडेलहरू अब प्रयोगमा छैनन् (जुलाई २०२६ मा बन्द हुँदैछ) र Responses API समर्थन गर्दैन। सबै GitHub मोडेल कोड पथहरू Python र .NET नमूनाहरूमा Azure OpenAI / Microsoft Foundry मा रूपान्तरण गरियो:
  - Python: Lesson 08 workflow नोटबुकहरू (`01`–`03`), Lesson 14 (`14-handoff`, `14-human-loop`, `hotel_booking_workflow_sample.py`)।
  - .NET: `01`–`04`, `07`, `08` `*-dotnet-agent-framework.cs` + सहायक `.md` कागजातहरू, र Lesson 08 dotNET workflow नोटबुकहरू/`.md` (`01`–`03`) अब `AzureOpenAIClient(...).GetOpenAIResponseClient(deployment).CreateAIAgent(...)` प्रयोग गर्छन् `AzureCliCredential` संग।
- **Semantic Kernel → Microsoft Agent Framework।** पहिलेको `02-semantic-kernel.ipynb` Microsoft Agent Framework संग Azure OpenAI (Responses API) प्रयोग गर्न पुनःलेखित गरियो र `02-python-agent-framework-azure-openai.ipynb` नामकरण गरियो।
- **`FoundryChatClient` + `as_agent` मा मानकीकरण गरियो।** README र नोटबुक कोड जसले `AzureAIProjectAgentProvider` लाई सन्दर्भित गर्थ्यो, यसलाई Lesson 01 र फ्रेमवर्कका आफ्नै नमूनाहरूले प्रयोग गरेको मानक ढाँचामा मानकीकरण गरियो: `FoundryChatClient(project_endpoint=..., model=..., credential=AzureCliCredential())` `provider.as_agent(...)` संग। Lesson 02–14 का README र नोटबुकहरूमा अपडेट गरियो (जस्तै, Lesson 13 मेमोरी, सबै Lesson 14 नोटबुकहरू, `11-agentic-protocols/code_samples/github-mcp/app.py`)।
- **उत्पादन नामकरण।** अंग्रेजी सामग्रीमा सम्पूर्ण नाम परिवर्तनहरू:
  - "Azure AI Foundry" / "Azure AI Studio" → **Microsoft Foundry**
  - "Azure AI Agent Service" → **Microsoft Foundry Agent Service**
  - (परिवर्तन नभएको: "Azure OpenAI", "Azure AI Search", "Azure AI Inference", र environment-variable नामहरू।)
- **निर्भरता** ([requirements.txt](../../requirements.txt)):
  - `agent-framework>=1.10.0`, `agent-framework-foundry>=1.10.0`, `agent-framework-openai>=1.10.0` हेरिएको छ।
  - Responses API को लागि न्यूनतम `openai>=1.108.1` पिन गरिएको छ।
  - `azure-ai-inference` हटाइयो (माइग्रेट गरिएको GitHub Models नमूनाहरूमा मात्र प्रयोग भएको थियो)।
- **पर्यावरण कन्फिगरेसन** ([.env.example](../../.env.example)): GitHub Models भेरिएबलहरू (`GITHUB_TOKEN`, `GITHUB_ENDPOINT`, `GITHUB_MODEL_ID`) हटाइयो; `AZURE_OPENAI_ENDPOINT`, `AZURE_OPENAI_DEPLOYMENT`, र वैकल्पिक `AZURE_OPENAI_API_KEY` थपियो; Microsoft Foundry नाममा अद्यावधिक गरियो।
- **डोकुमेन्टहरू** — माथिको लागि अद्यावधिक गरियो [00-course-setup/README.md](./00-course-setup/README.md), [AGENTS.md](./AGENTS.md), [README.md](./README.md), र [STUDY_GUIDE.md](./STUDY_GUIDE.md) (सेटअप env var हरू, जाँच स्निपेट, प्रदायक मार्गदर्शन, नामकरण)।

### हटाइयो

- GitHub Models अनबोर्डिङ चरणहरू र पर्यावरण भेरिएबलहरू सेटअप डोकुमेन्टहरूबाट हटाइयो (Azure OpenAI / Microsoft Foundry द्वारा प्रतिस्थापित)।

### सुरक्षा / गोपनीयता (सार्वजनिक सेयर सफाइ)

- Jupyter नोटबुक एक्सिक्युशन आउटपुटहरू जुन वास्तविक **Azure सदस्यता ID**, रिसोर्स-ग्रुप / रिसोर्स नामहरू, र Bing कनेक्सन ID, साथै विकासकर्ता **स्थानीय फाइल पथ र प्रयोगकर्तानामहरू** लिक गरेका थिए, मेटाइयो:
  - `08-multi-agent/code_samples/workflows-agent-framework/dotNET/04.dotnet-agent-framework-workflow-aifoundry-condition.ipynb`
  - `08-multi-agent/code_samples/workflows-agent-framework/python/04.python-agent-framework-workflow-aifoundry-condition.ipynb`
  - `15-browser-use/15-browser-user.ipynb`
- API कुञ्जीहरू, टोकनहरू, सदस्यता IDहरू, वा व्यक्तिगत मार्गहरू ट्र्याक गरिएको अंग्रेजी सामग्रीमा अड्किएका छैनन् भनी पुष्टि गरियो (`GITHUB_TOKEN` सन्दर्भहरू भने GitHub Actions टोकनहरू हुन् कार्यप्रवाहहरूमा र GitHub MCP सर्भर PAT Lesson 11 सेटअपमा — दुबै वैध र GitHub Models सँग सम्बन्धित छैनन्)।

### नोट्स र ज्ञात सीमितताहरू

- **चलाइएको / कम्पाइल नगरिएको।** यी शैक्षिक नमूनाहरू API/नामकरण शुद्धताका लागि अद्यावधिक गरिएका छन्; तिनीहरूलाई प्रत्यक्ष Azure स्रोतहरूसँग चलाइएको छैन, र .NET नमूनाहरू यस वातावरणमा कम्पाइल गरिएका छैनन्। आफ्नो Microsoft Foundry / Azure OpenAI डिप्लोयमेन्टमा प्रमाणित गर्नुहोस्।
- **मोडेल डिप्लोयमेन्टले Responses API समर्थन गर्नुपर्छ।** `gpt-4.1-mini`, `gpt-4.1`, वा `gpt-5.x` मोडेल जस्ता डिप्लोयमेन्ट प्रयोग गर्नुहोस्। पुराना मोडेलहरूले Responses को मूल कार्यक्षमता समर्थन गर्छन् तर सबै सुविधाहरू होइनन्।
- **Agent-framework संस्करण।** नमूनाहरू नवीनतम MAF (`>=1.10.0`) लक्षित गर्छन्। केनोनिकल एजेन्ट सिर्जना कल `client.as_agent(...)` हो; एपीआईहरू फ्रेमवर्कका प्रकाशित डकुमेन्टहरू र स्थापनाको विरुद्धमा परीक्षण गरियो। यदि फरक संस्करण पिन गर्नु भयो भने, मेथड उपलब्धता पुष्टि गर्नुहोस् (`as_agent` बनाम `create_agent`)।
- **Lesson 08 workflow नोटबुक 04** जानाजानी `AzureAIAgentClient` (from `agent-framework-azure-ai`) राखिएको छ किन भने यसले Microsoft Foundry Agent Service होस्ट गरिएको उपकरणहरू (Bing grounding, कोड इन्टरप्रेटर) प्रयोग गर्दछ; यो पहिले नै Responses-आधारित हो।
- **.NET पूर्वनिर्धारित डिप्लोयमेन्ट।** दुईवटा Lesson 08 dotNET workflow नमूनाहरूले पहिले निश्चित मोडेल हार्ड-कोड गरेको थिए; अब तिनीहरूले डिफल्ट रूपमा `AZURE_OPENAI_DEPLOYMENT` (`gpt-4.1-mini`) प्रयोग गर्छन्। यदि नमूना मल्टिमोडल/दृष्टि इनपुटमा भर पर्छ भने, `AZURE_OPENAI_DEPLOYMENT` उपयुक्त मोडेलमा सेट गर्नुहोस्।
- **Foundry Local** ले OpenAI-अनुकूल **Chat Completions** अन्त्यबिन्दु प्रदान गर्दछ र स्थानीय विकासका लागि लक्षित छ; पूर्ण Responses API सुविधाका लागि Azure OpenAI / Microsoft Foundry प्रयोग गर्नुहोस्।

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**अस्वीकरण**:
यो दस्तावेज़ AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) प्रयोग गरेर अनुवाद गरिएको हो। हामी सही हुन प्रयास गर्छौं, तर कृपया जानकार हुनुस् कि स्वचालित अनुवादमा त्रुटिहरू वा अशुद्धताहरू हुन सक्छन्। मूल दस्तावेज़ यसको मूल भाषामा आधिकारिक स्रोत मानिनुपर्छ। महत्वपूर्ण जानकारीका लागि व्यावसायिक मानव अनुवाद सिफारिस गरिन्छ। यस अनुवादको प्रयोगबाट उत्पन्न कुनै पनि गलत बुझाइ वा त्रुटिको लागि हामी जिम्मेवार छैनौं।
<!-- CO-OP TRANSLATOR DISCLAIMER END -->