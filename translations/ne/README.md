# AI एजेन्टहरू सुरुवातीहरूका लागि - एक कोर्स

![सृजनात्मक AI सुरुवातीहरूका लागि](../../translated_images/ne/repo-thumbnailv2.06f4a48036fde647.webp)

## AI एजेन्टहरू निर्माण गर्न थाल्न आवश्यक सबै कुरा सिकाउने एक कोर्स

[![GitHub लाइसेन्स](https://img.shields.io/github/license/microsoft/ai-agents-for-beginners.svg)](https://github.com/microsoft/ai-agents-for-beginners/blob/master/LICENSE?WT.mc_id=academic-105485-koreyst)
[![GitHub योगदानकर्ता](https://img.shields.io/github/contributors/microsoft/ai-agents-for-beginners.svg)](https://GitHub.com/microsoft/ai-agents-for-beginners/graphs/contributors/?WT.mc_id=academic-105485-koreyst)
[![GitHub समस्याहरू](https://img.shields.io/github/issues/microsoft/ai-agents-for-beginners.svg)](https://GitHub.com/microsoft/ai-agents-for-beginners/issues/?WT.mc_id=academic-105485-koreyst)
[![GitHub पुल अनुरोधहरू](https://img.shields.io/github/issues-pr/microsoft/ai-agents-for-beginners.svg)](https://GitHub.com/microsoft/ai-agents-for-beginners/pulls/?WT.mc_id=academic-105485-koreyst)
[![PRs स्वागत छ](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com?WT.mc_id=academic-105485-koreyst)

### 🌐 बहुभाषिक समर्थन

#### GitHub Action मार्फत समर्थित (स्वचालित र सधैं अद्यावधिक)

<!-- CO-OP TRANSLATOR LANGUAGES TABLE START -->
[Arabic](../ar/README.md) | [Bengali](../bn/README.md) | [Bulgarian](../bg/README.md) | [Burmese (Myanmar)](../my/README.md) | [Chinese (Simplified)](../zh-CN/README.md) | [Chinese (Traditional, Hong Kong)](../zh-HK/README.md) | [Chinese (Traditional, Macau)](../zh-MO/README.md) | [Chinese (Traditional, Taiwan)](../zh-TW/README.md) | [Croatian](../hr/README.md) | [Czech](../cs/README.md) | [Danish](../da/README.md) | [Dutch](../nl/README.md) | [Estonian](../et/README.md) | [Finnish](../fi/README.md) | [French](../fr/README.md) | [German](../de/README.md) | [Greek](../el/README.md) | [Hebrew](../he/README.md) | [Hindi](../hi/README.md) | [Hungarian](../hu/README.md) | [Indonesian](../id/README.md) | [Italian](../it/README.md) | [Japanese](../ja/README.md) | [Kannada](../kn/README.md) | [Korean](../ko/README.md) | [Lithuanian](../lt/README.md) | [Malay](../ms/README.md) | [Malayalam](../ml/README.md) | [Marathi](../mr/README.md) | [Nepali](./README.md) | [Nigerian Pidgin](../pcm/README.md) | [Norwegian](../no/README.md) | [Persian (Farsi)](../fa/README.md) | [Polish](../pl/README.md) | [Portuguese (Brazil)](../pt-BR/README.md) | [Portuguese (Portugal)](../pt-PT/README.md) | [Punjabi (Gurmukhi)](../pa/README.md) | [Romanian](../ro/README.md) | [Russian](../ru/README.md) | [Serbian (Cyrillic)](../sr/README.md) | [Slovak](../sk/README.md) | [Slovenian](../sl/README.md) | [Spanish](../es/README.md) | [Swahili](../sw/README.md) | [Swedish](../sv/README.md) | [Tagalog (Filipino)](../tl/README.md) | [Tamil](../ta/README.md) | [Telugu](../te/README.md) | [Thai](../th/README.md) | [Turkish](../tr/README.md) | [Ukrainian](../uk/README.md) | [Urdu](../ur/README.md) | [Vietnamese](../vi/README.md)

> **स्थानीय रूपमा क्लोन गर्न चाहनुहुन्छ?**

> यो रिपोजिटरीमा ५०+ भाषा अनुवादहरू समावेश छन् जसले डाउनलोड आकार धेरै बढाउँछ। अनुवाद बिना क्लोन गर्न, sparse checkout प्रयोग गर्नुहोस्:
> ```bash
> git clone --filter=blob:none --sparse https://github.com/microsoft/ai-agents-for-beginners.git
> cd ai-agents-for-beginners
> git sparse-checkout set --no-cone '/*' '!translations' '!translated_images'
> ```
> यसले तपाईंलाई पाठ्यक्रम पूरा गर्न आवश्यक सबै कुरा धेरै छिटो डाउनलोड दिइन्छ।
<!-- CO-OP TRANSLATOR LANGUAGES TABLE END -->

**यदि तपाईंलाई अतिरिक्त अनुवाद भाषाहरू आवश्यक छ भने ती यहाँ सूचीबद्ध छन् [यहाँ](https://github.com/Azure/co-op-translator/blob/main/getting_started/supported-languages.md)**

[![GitHub हेर्नेहरू](https://img.shields.io/github/watchers/microsoft/ai-agents-for-beginners.svg?style=social&label=Watch)](https://GitHub.com/microsoft/ai-agents-for-beginners/watchers/?WT.mc_id=academic-105485-koreyst)
[![GitHub फोर्कहरू](https://img.shields.io/github/forks/microsoft/ai-agents-for-beginners.svg?style=social&label=Fork)](https://GitHub.com/microsoft/ai-agents-for-beginners/network/?WT.mc_id=academic-105485-koreyst)
[![GitHub तारा](https://img.shields.io/github/stars/microsoft/ai-agents-for-beginners.svg?style=social&label=Star)](https://GitHub.com/microsoft/ai-agents-for-beginners/stargazers/?WT.mc_id=academic-105485-koreyst)

[![Microsoft Foundry Discord](https://dcbadge.limes.pink/api/server/nTYy5BXMWG)](https://discord.gg/nTYy5BXMWG)


## 🌱 सुरु कसरी गर्ने

यस कोर्समा AI एजेन्टहरू निर्माण गर्ने आधारभूत कुराहरू समेटिएको छ। प्रत्येक पाठले आफ्नै विषय समेट्छ त्यसैले जहाँ मन लाग्छ त्यहाँबाट सुरु गर्न सक्नुहुन्छ!

यस कोर्सका लागि बहुभाषिक समर्थन उपलब्ध छ। हाम्रो [उपलब्ध भाषाहरू यहाँ](../..) हेर्नुहोस्।

यदि तपाईं पहिलो पटक Generative AI मोडेलहरूसँग निर्माण गर्दै हुनुहुन्छ भने, हाम्रो [सृजनात्मक AI सुरुवातीहरूका लागि](https://aka.ms/genai-beginners) कोर्स हेर्नुहोस्, जसले GenAI संग निर्माण गर्ने २१ पाठहरू समावेश गर्छ।

यो रिपोजिटरीलाई नबिर्सिइ [ताराको (🌟) साथ स्टार गर्नुहोस्](https://docs.github.com/en/get-started/exploring-projects-on-github/saving-repositories-with-stars?WT.mc_id=academic-105485-koreyst) र [फोर्क गर्नुहोस्](https://github.com/microsoft/ai-agents-for-beginners/fork) कोड चलाउन।

### अन्य सिक्नेहरूलाई भेट्नुहोस्, तपाईंका प्रश्नहरूको उत्तर पाउनुहोस्

यदि तपाईं अड्किनु भयो वा AI एजेन्टहरू निर्माणमा कुनै प्रश्न भए, हाम्रो विशेष डिस्कोर्ड च्यानलमा [Microsoft Foundry Discord](https://aka.ms/ai-agents/discord) मा सामेल हुनुहोस्।

### तपाईंलाई के चाहिन्छ

यस कोर्सका प्रत्येक पाठमा कोड उदाहरणहरू छन्, जुन code_samples फोल्डरमा फेला पार्न सकिन्छ। तपाईं आफ्नो कपि बनाउन [यो रिपो फोर्क गर्न सक्नुहुन्छ](https://github.com/microsoft/ai-agents-for-beginners/fork)।

यी अभ्यासहरूमा प्रयोग भएको कोड उदाहरणहरूले Azure AI Foundry र GitHub Model Catalogs उपयोग गर्दछ Language Models सँग अन्तरक्रिया गर्न:

- [Github Models](https://aka.ms/ai-agents-beginners/github-models) - निःशुल्क / सीमित
- [Azure AI Foundry](https://aka.ms/ai-agents-beginners/ai-foundry) - Azure खाता आवश्यक

यस कोर्सले Microsoft बाट यी AI Agent फ्रेमवर्क र सेवाहरू पनि प्रयोग गर्दछ:

- [Microsoft Agent Framework (MAF) - नयाँ!](https://aka.ms/ai-agents-beginners/agent-framewrok)
- [Azure AI Agent Service](https://aka.ms/ai-agents-beginners/ai-agent-service)
- [Semantic Kernel](https://aka.ms/ai-agents-beginners/semantic-kernel)
- [AutoGen](https://aka.ms/ai-agents/autogen)


यस कोर्सको कोड चलाउने थप जानकारीका लागि, [Course Setup](./00-course-setup/README.md) मा जानुहोस्।

## 🙏 सहयोग गर्न चाहनुहुन्छ?

यदि तपाईं सिफारिसहरू छ वा वर्तनी वा कोड त्रुटिहरू भेट्टाउनुभयो भने? [एक मुद्दा उठाउनुहोस्](https://github.com/microsoft/ai-agents-for-beginners/issues?WT.mc_id=academic-105485-koreyst) वा [पुल अनुरोध सिर्जना गर्नुहोस्](https://github.com/microsoft/ai-agents-for-beginners/pulls?WT.mc_id=academic-105485-koreyst)



## 📂 प्रत्येक पाठमा समावेश रहेका छन्

- README मा लेखिएको पाठ र एउटा छोटो भिडियो
- Python कोड नमूनाहरू जुन Azure AI Foundry र Github Models (निःशुल्क) समर्थन गर्छ
- तपाईंको सिकाइ जारी राख्न अतिरिक्त स्रोतहरूका लिंकहरू


## 🗃️ पाठहरू

| **पाठ**                                    | **पाठ र कोड**                                     | **भिडियो**                                                | **अतिरिक्त सिकाइ**                                                                         |
|--------------------------------------------|-------------------------------------------------|------------------------------------------------------------|------------------------------------------------------------------------------------------|
| AI एजेन्ट र एजेन्ट प्रयोग केसहरू परिचय     | [लिंक](./01-intro-to-ai-agents/README.md)         | [भिडियो](https://youtu.be/3zgm60bXmQk?si=z8QygFvYQv-9WtO1)  | [लिंक](https://aka.ms/ai-agents-beginners/collection?WT.mc_id=academic-105485-koreyst)    |
| AI एजेन्टिक फ्रेमवर्कहरूको अन्वेषण          | [लिंक](./02-explore-agentic-frameworks/README.md) | [भिडियो](https://youtu.be/ODwF-EZo_O8?si=Vawth4hzVaHv-u0H)  | [लिंक](https://aka.ms/ai-agents-beginners/collection?WT.mc_id=academic-105485-koreyst)    |
| AI एजेन्टिक डिजाइन ढाँचाहरू बुझ्न          | [लिंक](./03-agentic-design-patterns/README.md)    | [भिडियो](https://youtu.be/m9lM8qqoOEA?si=BIzHwzstTPL8o9GF)  | [लिंक](https://aka.ms/ai-agents-beginners/collection?WT.mc_id=academic-105485-koreyst)    |
| उपकरण प्रयोग डिजाइन ढाँचा                   | [लिंक](./04-tool-use/README.md)                   | [भिडियो](https://youtu.be/vieRiPRx-gI?si=2z6O2Xu2cu_Jz46N)  | [लिंक](https://aka.ms/ai-agents-beginners/collection?WT.mc_id=academic-105485-koreyst)    |
| एजेन्टिक RAG                               | [लिंक](./05-agentic-rag/README.md)                | [भिडियो](https://youtu.be/WcjAARvdL7I?si=gKPWsQpKiIlDH9A3)  | [लिंक](https://aka.ms/ai-agents-beginners/collection?WT.mc_id=academic-105485-koreyst)    |
| भरपर्दो AI एजेन्टहरू निर्माण गर्ने          | [लिंक](./06-building-trustworthy-agents/README.md) | [भिडियो](https://youtu.be/iZKkMEGBCUQ?si=jZjpiMnGFOE9L8OK ) | [लिंक](https://aka.ms/ai-agents-beginners/collection?WT.mc_id=academic-105485-koreyst)    |
| योजना डिजाइन ढाँचा                          | [लिंक](./07-planning-design/README.md)            | [भिडियो](https://youtu.be/kPfJ2BrBCMY?si=6SC_iv_E5-mzucnC)  | [लिंक](https://aka.ms/ai-agents-beginners/collection?WT.mc_id=academic-105485-koreyst)    |
| बहु-एजेन्ट डिजाइन ढाँचा                    | [लिंक](./08-multi-agent/README.md)                | [भिडियो](https://youtu.be/V6HpE9hZEx0?si=rMgDhEu7wXo2uo6g)  | [लिंक](https://aka.ms/ai-agents-beginners/collection?WT.mc_id=academic-105485-koreyst)    |
| Metacognition Design Pattern                 | [Link](./09-metacognition/README.md)               | [Video](https://youtu.be/His9R6gw6Ec?si=8gck6vvdSNCt6OcF)  | [Link](https://aka.ms/ai-agents-beginners/collection?WT.mc_id=academic-105485-koreyst) |
| AI Agents in Production                      | [Link](./10-ai-agents-production/README.md)        | [Video](https://youtu.be/l4TP6IyJxmQ?si=31dnhexRo6yLRJDl)  | [Link](https://aka.ms/ai-agents-beginners/collection?WT.mc_id=academic-105485-koreyst) |
| Using Agentic Protocols (MCP, A2A and NLWeb) | [Link](./11-agentic-protocols/README.md)           | [Video](https://youtu.be/X-Dh9R3Opn8)                                 | [Link](https://aka.ms/ai-agents-beginners/collection?WT.mc_id=academic-105485-koreyst) |
| Context Engineering for AI Agents            | [Link](./12-context-engineering/README.md)         | [Video](https://youtu.be/F5zqRV7gEag)                                 | [Link](https://aka.ms/ai-agents-beginners/collection?WT.mc_id=academic-105485-koreyst) |
| Managing Agentic Memory                      | [Link](./13-agent-memory/README.md)     |      [Video](https://youtu.be/QrYbHesIxpw?si=vZkVwKrQ4ieCcIPx)                                                      |                                                                                        |
| Exploring Microsoft Agent Framework                         | [Link](./14-microsoft-agent-framework/README.md)                            |                                                            |                                                                                        |
| Building Computer Use Agents (CUA)           | छिट्टै आइरहेको छ                            |                                                            |                                                                                        |
| Deploying Scalable Agents                    | छिट्टै आइरहेको छ                            |                                                            |                                                                                        |
| Creating Local AI Agents                     | छिट्टै आइरहेको छ                               |                                                            |                                                                                        |
| Securing AI Agents                           | छिट्टै आइरहेको छ                               |                                                            |                                                                                        |

## 🎒 अन्य कोर्सहरू

हाम्रो टोलीले अन्य कोर्सहरू पनि उत्पादन गर्छ! हेर्नुहोस्:

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
 
### Generative AI Series
[![Generative AI for Beginners](https://img.shields.io/badge/Generative%20AI%20for%20Beginners-8B5CF6?style=for-the-badge&labelColor=E5E7EB&color=8B5CF6)](https://github.com/microsoft/generative-ai-for-beginners?WT.mc_id=academic-105485-koreyst)
[![Generative AI (.NET)](https://img.shields.io/badge/Generative%20AI%20(.NET)-9333EA?style=for-the-badge&labelColor=E5E7EB&color=9333EA)](https://github.com/microsoft/Generative-AI-for-beginners-dotnet?WT.mc_id=academic-105485-koreyst)
[![Generative AI (Java)](https://img.shields.io/badge/Generative%20AI%20(Java)-C084FC?style=for-the-badge&labelColor=E5E7EB&color=C084FC)](https://github.com/microsoft/generative-ai-for-beginners-java?WT.mc_id=academic-105485-koreyst)
[![Generative AI (JavaScript)](https://img.shields.io/badge/Generative%20AI%20(JavaScript)-E879F9?style=for-the-badge&labelColor=E5E7EB&color=E879F9)](https://github.com/microsoft/generative-ai-with-javascript?WT.mc_id=academic-105485-koreyst)

---
 
### Core Learning
[![ML for Beginners](https://img.shields.io/badge/ML%20for%20Beginners-22C55E?style=for-the-badge&labelColor=E5E7EB&color=22C55E)](https://aka.ms/ml-beginners?WT.mc_id=academic-105485-koreyst)
[![Data Science for Beginners](https://img.shields.io/badge/Data%20Science%20for%20Beginners-84CC16?style=for-the-badge&labelColor=E5E7EB&color=84CC16)](https://aka.ms/datascience-beginners?WT.mc_id=academic-105485-koreyst)
[![AI for Beginners](https://img.shields.io/badge/AI%20for%20Beginners-A3E635?style=for-the-badge&labelColor=E5E7EB&color=A3E635)](https://aka.ms/ai-beginners?WT.mc_id=academic-105485-koreyst)
[![Cybersecurity for Beginners](https://img.shields.io/badge/Cybersecurity%20for%20Beginners-F97316?style=for-the-badge&labelColor=E5E7EB&color=F97316)](https://github.com/microsoft/Security-101?WT.mc_id=academic-96948-sayoung)
[![Web Dev for Beginners](https://img.shields.io/badge/Web%20Dev%20for%20Beginners-EC4899?style=for-the-badge&labelColor=E5E7EB&color=EC4899)](https://aka.ms/webdev-beginners?WT.mc_id=academic-105485-koreyst)
[![IoT for Beginners](https://img.shields.io/badge/IoT%20for%20Beginners-14B8A6?style=for-the-badge&labelColor=E5E7EB&color=14B8A6)](https://aka.ms/iot-beginners?WT.mc_id=academic-105485-koreyst)
[![XR Development for Beginners](https://img.shields.io/badge/XR%20Development%20for%20Beginners-38BDF8?style=for-the-badge&labelColor=E5E7EB&color=38BDF8)](https://github.com/microsoft/xr-development-for-beginners?WT.mc_id=academic-105485-koreyst)

---
 
### Copilot Series
[![Copilot for AI Paired Programming](https://img.shields.io/badge/Copilot%20for%20AI%20Paired%20Programming-FACC15?style=for-the-badge&labelColor=E5E7EB&color=FACC15)](https://aka.ms/GitHubCopilotAI?WT.mc_id=academic-105485-koreyst)
[![Copilot for C#/.NET](https://img.shields.io/badge/Copilot%20for%20C%23/.NET-FBBF24?style=for-the-badge&labelColor=E5E7EB&color=FBBF24)](https://github.com/microsoft/mastering-github-copilot-for-dotnet-csharp-developers?WT.mc_id=academic-105485-koreyst)
[![Copilot Adventure](https://img.shields.io/badge/Copilot%20Adventure-FDE68A?style=for-the-badge&labelColor=E5E7EB&color=FDE68A)](https://github.com/microsoft/CopilotAdventures?WT.mc_id=academic-105485-koreyst)
<!-- CO-OP TRANSLATOR OTHER COURSES END -->

## 🌟 समुदायलाई धन्यवाद

Agentic RAG देखाउँदै महत्वपूर्ण कोड नमूनाहरू योगदान गर्ने [Shivam Goyal](https://www.linkedin.com/in/shivam2003/) लाई धन्यवाद।

## योगदान

यो परियोजनाले योगदान र सुझावहरू स्वागत गर्दछ। अधिकांश योगदानका लागि तपाईँले Contributor License Agreement (CLA) मा सहमति जनाउन आवश्यक हुन्छ जसले तपाईँसँग योगदान प्रयोग गर्ने अधिकार छ भनी घोषणा गर्दछ। विवरणका लागि जानुहोस् <https://cla.opensource.microsoft.com>।

जब तपाईँ पुल अनुरोध पठाउनुहुन्छ, CLA बोटले स्वतः निर्णय गर्नेछ कि तपाईँलाई CLA प्रदान गर्न आवश्यक छ कि छैन र पुल अनुरोधमा उपयुक्त सजावट (जस्तै स्थिति जाँच, टिप्पणी) गर्नेछ। बोटले दिएको निर्देशनहरू पालना गर्नुहोस्। यसलाई सबै भंडारहरूमा एकपटक मात्र गर्नु पर्नेछ।

यस परियोजनाले [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/) अपनाएको छ। थप जानकारीका लागि [Code of Conduct FAQ](https://opensource.microsoft.com/codeofconduct/faq/) हेर्नुहोस् वा थप प्रश्नहरू वा सुझावका लागि [opencode@microsoft.com](mailto:opencode@microsoft.com) मा सम्पर्क गर्नुहोस्।

## ट्रेडमार्कहरू

यो परियोजनामा प्रोजेक्टहरू, उत्पादनहरू, वा सेवाहरूको ट्रेडमार्कहरू वा लोगोहरू हुन सक्छन्। Microsoft ट्रेडमार्क वा लोगोहरूको आधिकारिक प्रयोग Microsoft का ट्रेडमार्क र ब्रान्ड दिशानिर्देशहरू [Microsoft's Trademark & Brand Guidelines](https://www.microsoft.com/legal/intellectualproperty/trademarks/usage/general) अनुसार हुनुपर्छ। यस परियोजनाको संशोधित संस्करणमा Microsoft ट्रेडमार्क वा लोगोहरूको प्रयोगले भ्रम पैदा गर्नु वा Microsoft को प्रायोजन छ भनी इङ्गित गर्नु हुँदैन। तेस्रो-पक्ष ट्रेडमार्क वा लोगोहरूको कुनै पनि प्रयोग तिनका नीतिहरूमा आधारित हुनेछ।

## सहयोग प्राप्ति

यदि तपाईं अड्कनुहुन्छ वा AI अनुप्रयोगहरू निर्माण गर्दा कुनै प्रश्नहरू छन् भने, सहभागी हुनुहोस्:

[![Microsoft Foundry Discord](https://dcbadge.limes.pink/api/server/nTYy5BXMWG)](https://discord.gg/nTYy5BXMWG)

यदि तपाईंलाई उत्पादन प्रतिक्रिया वा निर्माण गर्दा त्रुटिहरू छन् भने जानुहोस्:

[![Microsoft Foundry Developer Forum](https://img.shields.io/badge/GitHub-Microsoft_Foundry_Developer_Forum-blue?style=for-the-badge&logo=github&color=000000&logoColor=fff)](https://aka.ms/foundry/forum)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**अस्वीकरण**:
यो दस्तावेज़ [Co-op Translator](https://github.com/Azure/co-op-translator) नामक एआई अनुवाद सेवा प्रयोग गरी अनुवाद गरिएको हो। हामी शुद्धताको लागि प्रयास गर्दछौं, तर कृपया ध्यान दिनुहोस् कि स्वचालित अनुवादहरूमा त्रुटि वा गलतफहमी हुन सक्छ। मूल दस्तावेज़लाई यसको मूल भाषामै आधिकारिक स्रोत मानिनु पर्दछ। महत्वपूर्ण सूचनाका लागि, व्यावसायिक मनुष्क अनुवाद सिफारिस गरिन्छ। यस अनुवादका प्रयोगबाट उत्पन्न कुनै पनि गलतफहमी वा भ्रामकताका लागि हामी जिम्मेवार छैनौं।
<!-- CO-OP TRANSLATOR DISCLAIMER END -->