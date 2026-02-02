# AGENTS.md

## परियोजना का अवलोकन

यह रिपॉजिटरी "AI Agents for Beginners" नामक एक व्यापक शैक्षिक पाठ्यक्रम प्रदान करती है, जो AI एजेंट्स बनाने के लिए आवश्यक सभी चीजें सिखाती है। इस पाठ्यक्रम में 15+ पाठ शामिल हैं, जो मूलभूत बातें, डिज़ाइन पैटर्न, फ्रेमवर्क और AI एजेंट्स के उत्पादन परिनियोजन को कवर करते हैं।

**मुख्य तकनीकें:**
- Python 3.12+
- इंटरैक्टिव लर्निंग के लिए Jupyter Notebooks
- AI फ्रेमवर्क: Semantic Kernel, AutoGen, Microsoft Agent Framework (MAF)
- Azure AI सेवाएं: Azure AI Foundry, Azure AI Agent Service
- GitHub Models Marketplace (मुफ्त टियर उपलब्ध)

**आर्किटेक्चर:**
- पाठ आधारित संरचना (00-15+ डायरेक्टरी)
- प्रत्येक पाठ में शामिल हैं: README दस्तावेज़, कोड नमूने (Jupyter नोटबुक), और चित्र
- स्वचालित अनुवाद प्रणाली के माध्यम से बहु-भाषा समर्थन
- प्रत्येक पाठ के लिए कई फ्रेमवर्क विकल्प (Semantic Kernel, AutoGen, Azure AI Agent Service)

## सेटअप कमांड्स

### आवश्यकताएँ
- Python 3.12 या उच्चतर
- GitHub खाता (GitHub Models - मुफ्त टियर के लिए)
- Azure सदस्यता (वैकल्पिक, Azure AI सेवाओं के लिए)

### प्रारंभिक सेटअप

1. **रिपॉजिटरी को क्लोन या फोर्क करें:**
   ```bash
   gh repo fork microsoft/ai-agents-for-beginners --clone
   # OR
   git clone https://github.com/microsoft/ai-agents-for-beginners.git
   cd ai-agents-for-beginners
   ```

2. **Python वर्चुअल एनवायरनमेंट बनाएं और सक्रिय करें:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **डिपेंडेंसी इंस्टॉल करें:**
   ```bash
   pip install -r requirements.txt
   ```

4. **एनवायरनमेंट वेरिएबल सेट करें:**
   ```bash
   cp .env.example .env
   # Edit .env with your API keys and endpoints
   ```


### आवश्यक एनवायरनमेंट वेरिएबल्स

**GitHub Models (मुफ्त) के लिए:**
- `GITHUB_TOKEN` - GitHub से व्यक्तिगत एक्सेस टोकन

**Azure AI सेवाओं के लिए** (वैकल्पिक):
- `PROJECT_ENDPOINT` - Azure AI Foundry प्रोजेक्ट का एंडपॉइंट
- `AZURE_OPENAI_API_KEY` - Azure OpenAI API कुंजी
- `AZURE_OPENAI_ENDPOINT` - Azure OpenAI का एंडपॉइंट URL
- `AZURE_OPENAI_CHAT_DEPLOYMENT_NAME` - चैट मॉडल के लिए परिनियोजन नाम
- `AZURE_OPENAI_EMBEDDING_DEPLOYMENT_NAME` - एम्बेडिंग के लिए परिनियोजन नाम
- `.env.example` में दिखाए गए अतिरिक्त Azure कॉन्फ़िगरेशन

## विकास कार्यप्रवाह

### Jupyter Notebooks चलाना

प्रत्येक पाठ में विभिन्न फ्रेमवर्क के लिए कई Jupyter नोटबुक शामिल हैं:

1. **Jupyter शुरू करें:**
   ```bash
   jupyter notebook
   ```

2. **किसी पाठ की डायरेक्टरी पर जाएं** (जैसे, `01-intro-to-ai-agents/code_samples/`)

3. **नोटबुक खोलें और चलाएं:**
   - `*-semantic-kernel.ipynb` - Semantic Kernel फ्रेमवर्क का उपयोग करते हुए
   - `*-autogen.ipynb` - AutoGen फ्रेमवर्क का उपयोग करते हुए
   - `*-python-agent-framework.ipynb` - Microsoft Agent Framework (Python) का उपयोग करते हुए
   - `*-dotnet-agent-framework.ipynb` - Microsoft Agent Framework (.NET) का उपयोग करते हुए
   - `*-azureaiagent.ipynb` - Azure AI Agent Service का उपयोग करते हुए

### विभिन्न फ्रेमवर्क के साथ काम करना

**Semantic Kernel + GitHub Models:**
- GitHub खाता के साथ मुफ्त टियर उपलब्ध
- सीखने और प्रयोग के लिए अच्छा
- फ़ाइल पैटर्न: `*-semantic-kernel*.ipynb`

**AutoGen + GitHub Models:**
- GitHub खाता के साथ मुफ्त टियर उपलब्ध
- मल्टी-एजेंट ऑर्केस्ट्रेशन क्षमताएं
- फ़ाइल पैटर्न: `*-autogen.ipynb`

**Microsoft Agent Framework (MAF):**
- Microsoft का नवीनतम फ्रेमवर्क
- Python और .NET में उपलब्ध
- फ़ाइल पैटर्न: `*-agent-framework.ipynb`

**Azure AI Agent Service:**
- Azure सदस्यता की आवश्यकता
- उत्पादन-तैयार सुविधाएं
- फ़ाइल पैटर्न: `*-azureaiagent.ipynb`

## परीक्षण निर्देश

यह एक शैक्षिक रिपॉजिटरी है जिसमें उदाहरण कोड है, न कि उत्पादन कोड जिसमें स्वचालित परीक्षण हों। अपनी सेटअप और परिवर्तनों को सत्यापित करने के लिए:

### मैनुअल परीक्षण

1. **Python एनवायरनमेंट का परीक्षण करें:**
   ```bash
   python --version  # Should be 3.12+
   pip list | grep -E "(autogen|semantic-kernel|azure-ai)"
   ```

2. **नोटबुक निष्पादन का परीक्षण करें:**
   ```bash
   # Convert notebook to script and run (tests imports)
   jupyter nbconvert --to script <lesson-folder>/code_samples/<notebook>.ipynb --stdout | python
   ```

3. **एनवायरनमेंट वेरिएबल्स सत्यापित करें:**
   ```bash
   python -c "import os; from dotenv import load_dotenv; load_dotenv(); print('✓ GITHUB_TOKEN' if os.getenv('GITHUB_TOKEN') else '✗ GITHUB_TOKEN missing')"
   ```


### व्यक्तिगत नोटबुक चलाना

Jupyter में नोटबुक खोलें और कोशिकाओं को क्रमिक रूप से निष्पादित करें। प्रत्येक नोटबुक आत्म-निहित है और इसमें शामिल हैं:
- आयात कथन
- कॉन्फ़िगरेशन लोडिंग
- एजेंट कार्यान्वयन के उदाहरण
- अपेक्षित आउटपुट markdown कोशिकाओं में

## कोड शैली

### Python कन्वेंशन

- **Python संस्करण**: 3.12+
- **कोड शैली**: मानक Python PEP 8 कन्वेंशन का पालन करें
- **नोटबुक्स**: अवधारणाओं को समझाने के लिए स्पष्ट markdown कोशिकाओं का उपयोग करें
- **आयात**: मानक लाइब्रेरी, तृतीय-पक्ष, स्थानीय आयात द्वारा समूह बनाएं

### Jupyter Notebook कन्वेंशन

- कोड कोशिकाओं से पहले वर्णनात्मक markdown कोशिकाएं शामिल करें
- संदर्भ के लिए नोटबुक्स में आउटपुट उदाहरण जोड़ें
- पाठ अवधारणाओं से मेल खाने वाले स्पष्ट वेरिएबल नामों का उपयोग करें
- नोटबुक निष्पादन क्रम रैखिक रखें (कोशिका 1 → 2 → 3...)

### फ़ाइल संगठन

```
<lesson-number>-<lesson-name>/
├── README.md                     # Lesson documentation
├── code_samples/
│   ├── <number>-semantic-kernel.ipynb
│   ├── <number>-autogen.ipynb
│   ├── <number>-python-agent-framework.ipynb
│   └── <number>-azureaiagent.ipynb
└── images/
    └── *.png
```


## निर्माण और परिनियोजन

### दस्तावेज़ निर्माण

यह रिपॉजिटरी दस्तावेज़ीकरण के लिए Markdown का उपयोग करती है:
- प्रत्येक पाठ फ़ोल्डर में README.md फ़ाइलें
- रिपॉजिटरी रूट पर मुख्य README.md
- GitHub Actions के माध्यम से स्वचालित अनुवाद प्रणाली

### CI/CD पाइपलाइन

`.github/workflows/` में स्थित:

1. **co-op-translator.yml** - 50+ भाषाओं में स्वचालित अनुवाद
2. **welcome-issue.yml** - नए मुद्दा निर्माताओं का स्वागत करता है
3. **welcome-pr.yml** - नए पुल अनुरोध योगदानकर्ताओं का स्वागत करता है

### परिनियोजन

यह एक शैक्षिक रिपॉजिटरी है - कोई परिनियोजन प्रक्रिया नहीं। उपयोगकर्ता:
1. रिपॉजिटरी को फोर्क या क्लोन करें
2. नोटबुक्स को स्थानीय रूप से या GitHub Codespaces में चलाएं
3. उदाहरणों को संशोधित और प्रयोग करके सीखें

## पुल अनुरोध दिशानिर्देश

### सबमिट करने से पहले

1. **अपने परिवर्तनों का परीक्षण करें:**
   - प्रभावित नोटबुक्स को पूरी तरह से चलाएं
   - सुनिश्चित करें कि सभी कोशिकाएं त्रुटियों के बिना निष्पादित होती हैं
   - आउटपुट उपयुक्त हैं यह जांचें

2. **दस्तावेज़ीकरण अपडेट:**
   - यदि नए अवधारणाएं जोड़ रहे हैं तो README.md अपडेट करें
   - जटिल कोड के लिए नोटबुक्स में टिप्पणियां जोड़ें
   - सुनिश्चित करें कि markdown कोशिकाएं उद्देश्य को समझाती हैं

3. **फ़ाइल परिवर्तन:**
   - `.env` फ़ाइलों को कमिट करने से बचें (`.env.example` का उपयोग करें)
   - `venv/` या `__pycache__/` डायरेक्टरीज़ को कमिट न करें
   - जब वे अवधारणाओं को प्रदर्शित करते हैं तो नोटबुक आउटपुट रखें
   - अस्थायी फ़ाइलें और बैकअप नोटबुक्स (`*-backup.ipynb`) हटाएं

### PR शीर्षक प्रारूप

वर्णनात्मक शीर्षक का उपयोग करें:
- `[Lesson-XX] <अवधारणा> के लिए नया उदाहरण जोड़ें`
- `[Fix] पाठ-XX README में टाइपो सुधारें`
- `[Update] पाठ-XX में कोड नमूना सुधारें`
- `[Docs] सेटअप निर्देश अपडेट करें`

### आवश्यक जांच

- नोटबुक्स त्रुटियों के बिना निष्पादित होनी चाहिए
- README फाइलें स्पष्ट और सटीक होनी चाहिए
- रिपॉजिटरी में मौजूदा कोड पैटर्न का पालन करें
- अन्य पाठों के साथ संगति बनाए रखें

## अतिरिक्त नोट्स

### सामान्य समस्याएं

1. **Python संस्करण का मेल न होना:**
   - सुनिश्चित करें कि Python 3.12+ का उपयोग किया गया है
   - कुछ पैकेज पुराने संस्करणों के साथ काम नहीं कर सकते
   - Python संस्करण को स्पष्ट रूप से निर्दिष्ट करने के लिए `python3 -m venv` का उपयोग करें

2. **एनवायरनमेंट वेरिएबल्स:**
   - हमेशा `.env.example` से `.env` बनाएं
   - `.env` फ़ाइल को कमिट न करें (यह `.gitignore` में है)
   - GitHub टोकन को उचित अनुमतियों की आवश्यकता है

3. **पैकेज संघर्ष:**
   - एक नया वर्चुअल एनवायरनमेंट का उपयोग करें
   - व्यक्तिगत पैकेजों के बजाय `requirements.txt` से इंस्टॉल करें
   - कुछ नोटबुक्स में उनके markdown कोशिकाओं में उल्लिखित अतिरिक्त पैकेजों की आवश्यकता हो सकती है

4. **Azure सेवाएं:**
   - Azure AI सेवाओं को सक्रिय सदस्यता की आवश्यकता होती है
   - कुछ सुविधाएं क्षेत्र-विशिष्ट हैं
   - GitHub Models पर मुफ्त टियर सीमाएं लागू होती हैं

### सीखने का मार्ग

पाठों के माध्यम से अनुशंसित प्रगति:
1. **00-course-setup** - पर्यावरण सेटअप के लिए यहां से शुरू करें
2. **01-intro-to-ai-agents** - AI एजेंट्स की मूलभूत बातें समझें
3. **02-explore-agentic-frameworks** - विभिन्न फ्रेमवर्क के बारे में जानें
4. **03-agentic-design-patterns** - मुख्य डिज़ाइन पैटर्न
5. क्रमांकित पाठों के माध्यम से क्रमिक रूप से जारी रखें

### फ्रेमवर्क चयन

अपने लक्ष्यों के आधार पर फ्रेमवर्क चुनें:
- **सीखना/प्रोटोटाइप बनाना**: Semantic Kernel + GitHub Models (मुफ्त)
- **मल्टी-एजेंट सिस्टम्स**: AutoGen
- **नवीनतम सुविधाएं**: Microsoft Agent Framework (MAF)
- **उत्पादन परिनियोजन**: Azure AI Agent Service

### सहायता प्राप्त करना

- [Azure AI Foundry Community Discord](https://aka.ms/ai-agents/discord) में शामिल हों
- विशिष्ट मार्गदर्शन के लिए पाठ README फाइलें देखें
- पाठ्यक्रम अवलोकन के लिए मुख्य [README.md](./README.md) देखें
- विस्तृत सेटअप निर्देशों के लिए [Course Setup](./00-course-setup/README.md) देखें

### योगदान

यह एक खुला शैक्षिक प्रोजेक्ट है। योगदान का स्वागत है:
- कोड उदाहरण सुधारें
- टाइपो या त्रुटियां ठीक करें
- स्पष्ट टिप्पणियां जोड़ें
- नए पाठ विषय सुझाएं
- अतिरिक्त भाषाओं में अनुवाद करें

[GitHub Issues](https://github.com/microsoft/ai-agents-for-beginners/issues) में वर्तमान आवश्यकताओं को देखें।

## परियोजना-विशिष्ट संदर्भ

### बहु-भाषा समर्थन

यह रिपॉजिटरी स्वचालित अनुवाद प्रणाली का उपयोग करती है:
- 50+ भाषाओं का समर्थन
- `/translations/<lang-code>/` डायरेक्टरीज़ में अनुवाद
- GitHub Actions वर्कफ़्लो अनुवाद अपडेट को संभालता है
- स्रोत फाइलें रिपॉजिटरी रूट पर अंग्रेजी में हैं

### पाठ संरचना

प्रत्येक पाठ एक सुसंगत पैटर्न का अनुसरण करता है:
1. वीडियो थंबनेल के साथ लिंक
2. लिखित पाठ सामग्री (README.md)
3. कई फ्रेमवर्क में कोड नमूने
4. सीखने के उद्देश्य और आवश्यकताएं
5. अतिरिक्त सीखने के संसाधन लिंक किए गए

### कोड नमूना नामकरण

प्रारूप: `<lesson-number>-<framework-name>.ipynb`
- `04-semantic-kernel.ipynb` - पाठ 4, Semantic Kernel
- `07-autogen.ipynb` - पाठ 7, AutoGen
- `14-python-agent-framework.ipynb` - पाठ 14, MAF Python
- `14-dotnet-agent-framework.ipynb` - पाठ 14, MAF .NET

### विशेष डायरेक्टरीज़

- `translated_images/` - अनुवादों के लिए स्थानीयकृत चित्र
- `images/` - अंग्रेजी सामग्री के लिए मूल चित्र
- `.devcontainer/` - VS Code विकास कंटेनर कॉन्फ़िगरेशन
- `.github/` - GitHub Actions वर्कफ़्लो और टेम्पलेट्स

### डिपेंडेंसीज़

`requirements.txt` से मुख्य पैकेज:
- `autogen-agentchat`, `autogen-core`, `autogen-ext` - AutoGen फ्रेमवर्क
- `semantic-kernel` - Semantic Kernel फ्रेमवर्क
- `agent-framework` - Microsoft Agent Framework
- `azure-ai-inference`, `azure-ai-projects` - Azure AI सेवाएं
- `azure-search-documents` - Azure AI Search एकीकरण
- `chromadb` - RAG उदाहरणों के लिए वेक्टर डेटाबेस
- `chainlit` - चैट UI फ्रेमवर्क
- `browser_use` - एजेंट्स के लिए ब्राउज़र ऑटोमेशन
- `mcp[cli]` - मॉडल कॉन्टेक्स्ट प्रोटोकॉल समर्थन
- `mem0ai` - एजेंट्स के लिए मेमोरी प्रबंधन

---

**अस्वीकरण**:  
यह दस्तावेज़ AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) का उपयोग करके अनुवादित किया गया है। जबकि हम सटीकता के लिए प्रयास करते हैं, कृपया ध्यान दें कि स्वचालित अनुवाद में त्रुटियां या अशुद्धियां हो सकती हैं। मूल भाषा में उपलब्ध मूल दस्तावेज़ को आधिकारिक स्रोत माना जाना चाहिए। महत्वपूर्ण जानकारी के लिए, पेशेवर मानव अनुवाद की सिफारिश की जाती है। इस अनुवाद के उपयोग से उत्पन्न किसी भी गलतफहमी या गलत व्याख्या के लिए हम उत्तरदायी नहीं हैं।