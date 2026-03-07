# शुरुवातीहरूका लागि AI एजेन्टहरू - एक पाठ्यक्रम

![सृजनात्मक AI शुरुवातीहरूका लागि](../../translated_images/ne/repo-thumbnailv2.06f4a48036fde647.webp)

## AI एजेन्टहरू निर्माण गर्न सुरु गर्न आवश्यक सबै कुरा सिकाउने एक पाठ्यक्रम

[![GitHub लाइसेन्स](https://img.shields.io/github/license/microsoft/ai-agents-for-beginners.svg)](https://github.com/microsoft/ai-agents-for-beginners/blob/master/LICENSE?WT.mc_id=academic-105485-koreyst)
[![GitHub योगदानकर्ताहरू](https://img.shields.io/github/contributors/microsoft/ai-agents-for-beginners.svg)](https://GitHub.com/microsoft/ai-agents-for-beginners/graphs/contributors/?WT.mc_id=academic-105485-koreyst)
[![GitHub समस्याहरू](https://img.shields.io/github/issues/microsoft/ai-agents-for-beginners.svg)](https://GitHub.com/microsoft/ai-agents-for-beginners/issues/?WT.mc_id=academic-105485-koreyst)
[![GitHub पुल-रिक्वेस्टहरू](https://img.shields.io/github/issues-pr/microsoft/ai-agents-for-beginners.svg)](https://GitHub.com/microsoft/ai-agents-for-beginners/pulls/?WT.mc_id=academic-105485-koreyst)
[![PRs स्वागत छन्](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com?WT.mc_id=academic-105485-koreyst)

### 🌐 बहुभाषी समर्थन

#### GitHub Action मार्फत समर्थित (स्वचालित र सधैं अद्यावधिक)

<!-- CO-OP TRANSLATOR LANGUAGES TABLE START -->
[अराबी](../ar/README.md) | [बंगाली](../bn/README.md) | [बुल्गेरियन](../bg/README.md) | [बर्मी (म्यानमार)](../my/README.md) | [चिनियाँ (सरलीकृत)](../zh-CN/README.md) | [चिनियाँ (परम्परागत, हङकङ)](../zh-HK/README.md) | [चिनियाँ (परम्परागत, मकाओ)](../zh-MO/README.md) | [चिनियाँ (परम्परागत, ताइवान)](../zh-TW/README.md) | [क्रोएशियन](../hr/README.md) | [चेचक](../cs/README.md) | [डेनिश](../da/README.md) | [डच](../nl/README.md) | [एसटोनीयन](../et/README.md) | [फिनिश](../fi/README.md) | [फ्रेन्च](../fr/README.md) | [जर्मन](../de/README.md) | [ग्रीक](../el/README.md) | [हिब्रू](../he/README.md) | [हिन्दी](../hi/README.md) | [हंगेरीयन](../hu/README.md) | [इन्डोनेसियन](../id/README.md) | [इटालियन](../it/README.md) | [जापानी](../ja/README.md) | [कन्नडा](../kn/README.md) | [कोरियन](../ko/README.md) | [लिथुआनियन](../lt/README.md) | [मले](../ms/README.md) | [मलयालम](../ml/README.md) | [मराठी](../mr/README.md) | [नेपाली](./README.md) | [नाइजेरीयन पिजिन](../pcm/README.md) | [नर्वेजियन](../no/README.md) | [पारसी (फारसी)](../fa/README.md) | [पोलिश](../pl/README.md) | [पोर्चुगिज (ब्राजिल)](../pt-BR/README.md) | [पोर्चुगिज (पोर्चुगल)](../pt-PT/README.md) | [पन्जाबी (गुरुमुखी)](../pa/README.md) | [रोमानियन](../ro/README.md) | [रशियन](../ru/README.md) | [सर्बियाली (सिरिलिक)](../sr/README.md) | [स्लोवाक](../sk/README.md) | [स्लोभेनियन](../sl/README.md) | [स्पेनी](../es/README.md) | [स्वाहिली](../sw/README.md) | [स्विडिश](../sv/README.md) | [ट्यागालोग (फिलिपिनो)](../tl/README.md) | [तमिल](../ta/README.md) | [तेलुगु](../te/README.md) | [थाई](../th/README.md) | [टर्किश](../tr/README.md) | [यूक्रेनीयन](../uk/README.md) | [उर्दू](../ur/README.md) | [भिएतनामिज](../vi/README.md)

> **स्थानीय रूपमा क्लोन गर्न प्राथमिकता दिनुहुन्छ?**
> 
> यस रिपोजिटरीले ५० भन्दा बढी भाषा अनुवादहरू समावेश गर्दछ जसले डाउनलोड आकार धेरै बढाउँछ। अनुवादहरू बिना क्लोन गर्न, sparse checkout प्रयोग गर्नुहोस्:
> 
> **Bash / macOS / Linux:**
> ```bash
> git clone --filter=blob:none --sparse https://github.com/microsoft/ai-agents-for-beginners.git
> cd ai-agents-for-beginners
> git sparse-checkout set --no-cone '/*' '!translations' '!translated_images'
> ```
>
> **CMD (Windows):**
> ```cmd
> git clone --filter=blob:none --sparse https://github.com/microsoft/ai-agents-for-beginners.git
> cd ai-agents-for-beginners
> git sparse-checkout set --no-cone "/*" "!translations" "!translated_images"
> ```
>
> यसले तपाईंलाई कोर्स पूरा गर्न आवश्यक सबै कुरा छिटो डाउनलोड गराउँछ।
<!-- CO-OP TRANSLATOR LANGUAGES TABLE END -->

**अतिरिक्त अनुवाद भाषाहरूको लागि जुन समर्थित छन्, सूची यहाँ छ [यहाँ](https://github.com/Azure/co-op-translator/blob/main/getting_started/supported-languages.md)**

[![GitHub वाचर्स](https://img.shields.io/github/watchers/microsoft/ai-agents-for-beginners.svg?style=social&label=Watch)](https://GitHub.com/microsoft/ai-agents-for-beginners/watchers/?WT.mc_id=academic-105485-koreyst)
[![GitHub फोर्क्स](https://img.shields.io/github/forks/microsoft/ai-agents-for-beginners.svg?style=social&label=Fork)](https://GitHub.com/microsoft/ai-agents-for-beginners/network/?WT.mc_id=academic-105485-koreyst)
[![GitHub स्टारहरू](https://img.shields.io/github/stars/microsoft/ai-agents-for-beginners.svg?style=social&label=Star)](https://GitHub.com/microsoft/ai-agents-for-beginners/stargazers/?WT.mc_id=academic-105485-koreyst)

[![Microsoft Foundry Discord](https://dcbadge.limes.pink/api/server/nTYy5BXMWG)](https://discord.gg/nTYy5BXMWG)


## 🌱 शुरुवात

यो पाठ्यक्रमले AI एजेन्टहरू बनाउनका आधारभूत सिद्धान्तहरू समेट्ने पाठहरू समावेश गर्दछ। प्रत्येक पाठले आफ्नै विषय समेट्छ, त्यसैले जहाँ सुरु गर्न चाहनुहुन्छ त्यहाँबाट प्रारम्भ गर्नुहोस्!

यो पाठ्यक्रमको लागि बहुभाषी समर्थन छ। हाम्रा [उपलब्ध भाषाहरू यहाँ हेर्नुहोस्](../..)।

यदि तपाईं पहिलो पटक सृजनात्मक AI मोडेलहरूसँग निर्माण गर्दै हुनुहुन्छ भने, हाम्रो [सृजनात्मक AI शुरुवातीहरूका लागि](https://aka.ms/genai-beginners) पाठ्यक्रममा हेर्नुहोस्, जसमा GenAI सँग निर्माण गर्ने २१ पाठहरू छन्।

यस रिपोमा [तारा (🌟) लगाउन](https://docs.github.com/en/get-started/exploring-projects-on-github/saving-repositories-with-stars?WT.mc_id=academic-105485-koreyst) नबिर्सनुहोस् र [फोर्क](https://github.com/microsoft/ai-agents-for-beginners/fork) गरेपछि कोड चलाउन सक्नुहुन्छ।

### अन्य सिक्नेहरूसँग भेट्नुहोस्, प्रश्नहरूको उत्तर पाउनुहोस्

यदि तपाईं अड्किनुभयो वा AI एजेन्टहरू बनाउन कुनै प्रश्न छ भने, हाम्रो समर्पित Discord च्यानल [Microsoft Foundry Discord](https://aka.ms/ai-agents/discord) मा सहभागी हुनुहोस्।

### के चाहिन्छ 

यस पाठ्यक्रमका प्रत्येक पाठमा कोड उदाहरणहरू समावेश छन्, जुन code_samples फोल्डरमा पाइन्छ। तपाईं [यस रिपो फोर्क](https://github.com/microsoft/ai-agents-for-beginners/fork) गरेर आफ्नो प्रतिलिपि बनाउन सक्नुहुन्छ।

यी व्यायाममा रहेको कोड उदाहरणहरूले Microsoft Agent Framework सँग Azure AI Foundry Agent Service V2 प्रयोग गर्दछ:

- [Microsoft Foundry](https://aka.ms/ai-agents-beginners/ai-foundry) - Azure खाता आवश्यक

यस पाठ्यक्रमले Microsoft बाट निम्न AI एजेन्ट फ्रेमवर्क र सेवाहरू प्रयोग गर्दछ:

- [Microsoft Agent Framework (MAF)](https://aka.ms/ai-agents-beginners/agent-framewrok)
- [Azure AI Foundry Agent Service V2](https://aka.ms/ai-agents-beginners/ai-agent-service)

यस पाठ्यक्रमको कोड चलाउने बारे थप जानकारीका लागि, [Course Setup](./00-course-setup/README.md) मा जानुहोस्।

## 🙏 मद्दत गर्न चाहनुहुन्छ?

तपाईं सल्लाह दिन चाहनुहुन्छ वा हिज्जे या कोड त्रुटि फेला पार्नुभएको छ भने? [समस्या उठाउनुहोस्](https://github.com/microsoft/ai-agents-for-beginners/issues?WT.mc_id=academic-105485-koreyst) वा [पुल रेक्वेस्ट बनाउनुहोस्](https://github.com/microsoft/ai-agents-for-beginners/pulls?WT.mc_id=academic-105485-koreyst)


## 📂 प्रत्येक पाठमा समावेश छ

- README मा रहेको लेखिएको पाठ र एक छोटो भिडियो
- Microsoft Agent Framework सँग Azure AI Foundry प्रयोग गरिएको Python कोड उदाहरणहरू
- अध्ययन जारी राख्न थप स्रोतहरूको लिंकहरू


## 🗃️ पाठहरू

| **पाठ**                                     | **पाठ र कोड**                                            | **भिडियो**                                                  | **थप अध्ययन**                                                                   |
|----------------------------------------------|----------------------------------------------------------|--------------------------------------------------------------|----------------------------------------------------------------------------------|
| AI एजेन्टहरू र एजेन्ट प्रयोगका परिचय        | [लिंक](./01-intro-to-ai-agents/README.md)                 | [भिडियो](https://youtu.be/3zgm60bXmQk?si=z8QygFvYQv-9WtO1)   | [लिंक](https://aka.ms/ai-agents-beginners/collection?WT.mc_id=academic-105485-koreyst) |
| AI एजेन्टिक फ्रेमवर्कहरूको अन्वेषण            | [लिंक](./02-explore-agentic-frameworks/README.md)         | [भिडियो](https://youtu.be/ODwF-EZo_O8?si=Vawth4hzVaHv-u0H)   | [लिंक](https://aka.ms/ai-agents-beginners/collection?WT.mc_id=academic-105485-koreyst) |
| AI एजेन्टिक डिजाइन ढाँचा बुझ्ने               | [लिंक](./03-agentic-design-patterns/README.md)            | [भिडियो](https://youtu.be/m9lM8qqoOEA?si=BIzHwzstTPL8o9GF)   | [लिंक](https://aka.ms/ai-agents-beginners/collection?WT.mc_id=academic-105485-koreyst) |
| उपकरण उपयोग डिजाइन ढाँचा                      | [लिंक](./04-tool-use/README.md)                            | [भिडियो](https://youtu.be/vieRiPRx-gI?si=2z6O2Xu2cu_Jz46N)   | [लिंक](https://aka.ms/ai-agents-beginners/collection?WT.mc_id=academic-105485-koreyst) |
| एजेन्टिक RAG                                  | [लिंक](./05-agentic-rag/README.md)                         | [भिडियो](https://youtu.be/WcjAARvdL7I?si=gKPWsQpKiIlDH9A3)   | [लिंक](https://aka.ms/ai-agents-beginners/collection?WT.mc_id=academic-105485-koreyst) |
| विश्वसनीय AI एजेन्टहरू निर्माण                | [लिंक](./06-building-trustworthy-agents/README.md)         | [भिडियो](https://youtu.be/iZKkMEGBCUQ?si=jZjpiMnGFOE9L8OK)    | [लिंक](https://aka.ms/ai-agents-beginners/collection?WT.mc_id=academic-105485-koreyst) |
| योजना बनाउने डिजाइन ढाँचा                      | [लिंक](./07-planning-design/README.md)                     | [भिडियो](https://youtu.be/kPfJ2BrBCMY?si=6SC_iv_E5-mzucnC)   | [लिंक](https://aka.ms/ai-agents-beginners/collection?WT.mc_id=academic-105485-koreyst) |
| बहु-एजेन्ट डिजाइन ढाँचा                       | [लिंक](./08-multi-agent/README.md)                         | [भिडियो](https://youtu.be/V6HpE9hZEx0?si=rMgDhEu7wXo2uo6g)   | [लिंक](https://aka.ms/ai-agents-beginners/collection?WT.mc_id=academic-105485-koreyst) |
| मेटाकग्निशन डिजाइन ढाँचा                      | [लिंक](./09-metacognition/README.md)                       | [भिडियो](https://youtu.be/His9R6gw6Ec?si=8gck6vvdSNCt6OcF)   | [लिंक](https://aka.ms/ai-agents-beginners/collection?WT.mc_id=academic-105485-koreyst) |
| उत्पादनमा AI एजेन्टहरू                      | [Link](./10-ai-agents-production/README.md)        | [Video](https://youtu.be/l4TP6IyJxmQ?si=31dnhexRo6yLRJDl)  | [Link](https://aka.ms/ai-agents-beginners/collection?WT.mc_id=academic-105485-koreyst) |
| एजेन्टिक प्रोटोकलहरू प्रयोग गर्दै (MCP, A2A र NLWeb) | [Link](./11-agentic-protocols/README.md)           | [Video](https://youtu.be/X-Dh9R3Opn8)                                 | [Link](https://aka.ms/ai-agents-beginners/collection?WT.mc_id=academic-105485-koreyst) |
| AI एजेन्टहरूको सन्दर्भ इन्जिनियरिङ           | [Link](./12-context-engineering/README.md)         | [Video](https://youtu.be/F5zqRV7gEag)                                 | [Link](https://aka.ms/ai-agents-beginners/collection?WT.mc_id=academic-105485-koreyst) |
| एजेन्टिक स्मरण व्यवस्थापन                      | [Link](./13-agent-memory/README.md)     |      [Video](https://youtu.be/QrYbHesIxpw?si=vZkVwKrQ4ieCcIPx)                                                      |                                                                                        |
| माइक्रोसफ्ट एजेन्ट फ्रेमवर्क अन्वेषण गर्दै                         | [Link](./14-microsoft-agent-framework/README.md)                            |                                                            |                                                                                        |
| कम्प्युटर प्रयोग एजेन्टहरू (CUA) निर्माण गर्दै           | चाँडै आउने                        |                                                            |                                                                                        |
| स्केलेबल एजेन्टहरू परिचालन गर्दै                    | चाँडै आउने                        |                                                            |                                                                                        |
| स्थानीय AI एजेन्टहरू सिर्जना गर्दै                     | चाँडै आउने                               |                                                            |                                                                                        |
| AI एजेन्टहरूको सुरक्षा गर्दै                           | चाँडै आउने                               |                                                            |                                                                                        |

## 🎒 अन्य पाठ्यक्रमहरू

हाम्रो टोलीले अन्य पाठ्यक्रमहरू उत्पादन गर्छ! जाँच गर्नुहोस्:

<!-- CO-OP TRANSLATOR OTHER COURSES START -->
### LangChain
[![LangChain4j for Beginners](https://img.shields.io/badge/LangChain4j%20for%20Beginners-22C55E?style=for-the-badge&&labelColor=E5E7EB&color=0553D6)](https://aka.ms/langchain4j-for-beginners)
[![LangChain.js for Beginners](https://img.shields.io/badge/LangChain.js%20for%20Beginners-22C55E?style=for-the-badge&labelColor=E5E7EB&color=0553D6)](https://aka.ms/langchainjs-for-beginners?WT.mc_id=m365-94501-dwahlin)
[![LangChain for Beginners](https://img.shields.io/badge/LangChain%20for%20Beginners-22C55E?style=for-the-badge&labelColor=E5E7EB&color=0553D6)](https://github.com/microsoft/langchain-for-beginners?WT.mc_id=m365-94501-dwahlin)
---

### Azure / Edge / MCP / Agents
[![AZD for Beginners](https://img.shields.io/badge/AZD%20for%20Beginners-0078D4?style=for-the-badge&labelColor=E5E7EB&color=0078D4)](https://github.com/microsoft/AZD-for-beginners?WT.mc_id=academic-105485-koreyst)
[![Edge AI for Beginners](https://img.shields.io/badge/Edge%20AI%20for%20Beginners-00B8E4?style=for-the-badge&labelColor=E5E7EB&color=00B8E4)](https://github.com/microsoft/edgeai-for-beginners?WT.mc_id=academic-105485-koreyst)
[![MCP for Beginners](https://img.shields.io/badge/MCP%20for%20Beginners-009688?style=for-the-badge&labelColor=E5E7EB&color=009688)](https://github.com/microsoft/mcp-for-beginners?WT.mc_id=academic-105485-koreyst)
[![AI Agents for Beginners](https://img.shields.io/badge/AI%20Agents%20for%20Beginners-00C49A?style=for-the-badge&labelColor=E5E7EB&color=00C49A)](https://github.com/microsoft/ai-agents-for-beginners?WT.mc_id=academic-105485-koreyst)

---
 
### जेनेरेटिभ AI सिरिज
[![Generative AI for Beginners](https://img.shields.io/badge/Generative%20AI%20for%20Beginners-8B5CF6?style=for-the-badge&labelColor=E5E7EB&color=8B5CF6)](https://github.com/microsoft/generative-ai-for-beginners?WT.mc_id=academic-105485-koreyst)
[![Generative AI (.NET)](https://img.shields.io/badge/Generative%20AI%20(.NET)-9333EA?style=for-the-badge&labelColor=E5E7EB&color=9333EA)](https://github.com/microsoft/Generative-AI-for-beginners-dotnet?WT.mc_id=academic-105485-koreyst)
[![Generative AI (Java)](https://img.shields.io/badge/Generative%20AI%20(Java)-C084FC?style=for-the-badge&labelColor=E5E7EB&color=C084FC)](https://github.com/microsoft/generative-ai-for-beginners-java?WT.mc_id=academic-105485-koreyst)
[![Generative AI (JavaScript)](https://img.shields.io/badge/Generative%20AI%20(JavaScript)-E879F9?style=for-the-badge&labelColor=E5E7EB&color=E879F9)](https://github.com/microsoft/generative-ai-with-javascript?WT.mc_id=academic-105485-koreyst)

---
 
### मूल सिकाइ
[![ML for Beginners](https://img.shields.io/badge/ML%20for%20Beginners-22C55E?style=for-the-badge&labelColor=E5E7EB&color=22C55E)](https://aka.ms/ml-beginners?WT.mc_id=academic-105485-koreyst)
[![Data Science for Beginners](https://img.shields.io/badge/Data%20Science%20for%20Beginners-84CC16?style=for-the-badge&labelColor=E5E7EB&color=84CC16)](https://aka.ms/datascience-beginners?WT.mc_id=academic-105485-koreyst)
[![AI for Beginners](https://img.shields.io/badge/AI%20for%20Beginners-A3E635?style=for-the-badge&labelColor=E5E7EB&color=A3E635)](https://aka.ms/ai-beginners?WT.mc_id=academic-105485-koreyst)
[![Cybersecurity for Beginners](https://img.shields.io/badge/Cybersecurity%20for%20Beginners-F97316?style=for-the-badge&labelColor=E5E7EB&color=F97316)](https://github.com/microsoft/Security-101?WT.mc_id=academic-96948-sayoung)
[![Web Dev for Beginners](https://img.shields.io/badge/Web%20Dev%20for%20Beginners-EC4899?style=for-the-badge&labelColor=E5E7EB&color=EC4899)](https://aka.ms/webdev-beginners?WT.mc_id=academic-105485-koreyst)
[![IoT for Beginners](https://img.shields.io/badge/IoT%20for%20Beginners-14B8A6?style=for-the-badge&labelColor=E5E7EB&color=14B8A6)](https://aka.ms/iot-beginners?WT.mc_id=academic-105485-koreyst)
[![XR Development for Beginners](https://img.shields.io/badge/XR%20Development%20for%20Beginners-38BDF8?style=for-the-badge&labelColor=E5E7EB&color=38BDF8)](https://github.com/microsoft/xr-development-for-beginners?WT.mc_id=academic-105485-koreyst)

---
 
### कोपाइ़लट सिरिज
[![Copilot for AI Paired Programming](https://img.shields.io/badge/Copilot%20for%20AI%20Paired%20Programming-FACC15?style=for-the-badge&labelColor=E5E7EB&color=FACC15)](https://aka.ms/GitHubCopilotAI?WT.mc_id=academic-105485-koreyst)
[![Copilot for C#/.NET](https://img.shields.io/badge/Copilot%20for%20C%23/.NET-FBBF24?style=for-the-badge&labelColor=E5E7EB&color=FBBF24)](https://github.com/microsoft/mastering-github-copilot-for-dotnet-csharp-developers?WT.mc_id=academic-105485-koreyst)
[![Copilot Adventure](https://img.shields.io/badge/Copilot%20Adventure-FDE68A?style=for-the-badge&labelColor=E5E7EB&color=FDE68A)](https://github.com/microsoft/CopilotAdventures?WT.mc_id=academic-105485-koreyst)
<!-- CO-OP TRANSLATOR OTHER COURSES END -->

## 🌟 समुदायलाई धन्यवाद

महत्वपूर्ण कोड नमूनाहरू प्रदर्शन गर्ने एजेन्टिक RAG मा योगदानका लागि [Shivam Goyal](https://www.linkedin.com/in/shivam2003/) लाई धन्यवाद।

## योगदान

यस परियोजनाले योगदान र सुझावहरूलाई स्वागत गर्दछ। धेरै योगदानहरूमा तपाईँले Contributor License Agreement (CLA) मा सहमति जनाउनु आवश्यक छ जसले तपाईंलाई तपाईंको योगदान प्रयोग गर्ने अधिकार छ भनी घोषणा गर्दछ। थप विवरणका लागि, <https://cla.opensource.microsoft.com> हेर्नुहोस्।

जब तपाईं पुल अनुरोध पेश गर्नुहुन्छ, CLA बोटले स्वचालित रूपमा निर्धारण गर्नेछ कि तपाईंले CLA प्रदान गर्नु आवश्यक छ कि छैन र PR उपयुक्त रूपमा सजावट गर्नेछ (जस्तै, स्थिति जाँच, टिप्पणी)। बोटद्वारा प्रदान गरिएका निर्देशनहरू पालना गर्नुहोस्। तपाईंलाई यी सबै रिपोजहरूमा केवल एकपटक यो गर्नु पर्नेछ।

यस परियोजनाले [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/) अपनाएको छ। थप जानकारीका लागि [Code of Conduct FAQ](https://opensource.microsoft.com/codeofconduct/faq/) हेर्नुहोस् वा कुनै अतिरिक्त प्रश्न वा टिप्पणीका लागि [opencode@microsoft.com](mailto:opencode@microsoft.com) मा सम्पर्क गर्नुहोस्।

## ट्रेडमार्कहरू

यस परियोजनामा परियोजनाहरू, उत्पादनहरू, वा सेवाहरूका ट्रेडमार्कहरू वा लोगोहरू हुन सक्छन्। माइक्रोसफ्ट ट्रेडमार्कहरू वा लोगोहरूको अधिकृत प्रयोग Microsoft को [ट्रेडमार्क र ब्रान्ड मार्गनिर्देशनहरू](https://www.microsoft.com/legal/intellectualproperty/trademarks/usage/general) अनुसार हुनुपर्छ। संशोधित संस्करणहरूमा माइक्रोसफ्ट ट्रेडमार्क वा लोगोहरूको प्रयोगले भ्रम सिर्जना गर्नु हुँदैन वा माइक्रोसफ्ट प्रायोजन दर्शाउनु हुँदैन। तेस्रो पक्षका ट्रेडमार्क वा लोगोहरूको प्रयोग तिनीहरूको सम्बन्धित नीतिहरूमा अधीनमा हुनेछ।

## सहायता प्राप्त गर्न

यदि तपाईं अलमलमा हुनुहुन्छ वा AI अनुप्रयोगहरू बनाउन सन्दर्भमा कुनै प्रश्नहरू छन् भने, सामेल हुनुहोस्:

[![Microsoft Foundry Discord](https://img.shields.io/badge/Discord-Azure_AI_Foundry_Community_Discord-blue?style=for-the-badge&logo=discord&color=5865f2&logoColor=fff)](https://aka.ms/foundry/discord)

यदि तपाईंलाई उत्पादन प्रतिक्रिया वा निर्माण गर्दा त्रुटिहरू छन् भने भेट्नुहोस्:

[![Microsoft Foundry Developer Forum](https://img.shields.io/badge/GitHub-Azure_AI_Foundry_Developer_Forum-blue?style=for-the-badge&logo=github&color=000000&logoColor=fff)](https://aka.ms/foundry/forum)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**अस्वीकरण**:
यो दस्तावेज़ AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) को प्रयोग गरेर अनुवाद गरिएको हो। हामी शुद्धताको प्रयास गर्छौं, तर कृपया बुझ्नुहोस् कि स्वचालित अनुवादहरूमा त्रुटि वा अशुद्धता हुन सक्दछन्। मूल भाषा मा रहेको दस्तावेज़लाई आधिकारिक स्रोतका रूपमा मान्नु पर्छ। महत्वपूर्ण जानकारीको लागि, पेशेवर मानवीय अनुवाद सिफारिस गरिन्छ। यस अनुवादको प्रयोगबाट हुने कुनै पनि गलतफहमी वा गलत व्याख्याको लागि हामी जिम्मेवार हुँदैनौं।
<!-- CO-OP TRANSLATOR DISCLAIMER END -->