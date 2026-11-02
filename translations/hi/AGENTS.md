# AGENTS.md

## परियोजना अवलोकन

यह रिपॉजिटरी "शुरुआती के लिए AI एजेंट्स" - एक व्यापक शैक्षिक कोर्स प्रदान करता है जो AI एजेंट्स बनाने के लिए आवश्यक सभी चीजें सिखाता है। कोर्स में 18 पाठ शामिल हैं (संख्या 00-18) जिनमें मूल बातें, डिजाइन पैटर्न, फ्रेमवर्क, उत्पादन तैनाती, स्थानीय/डिवाइस एजेंट्स, और AI एजेंट्स की सुरक्षा शामिल है।

**मुख्य तकनीकें:**
- Python 3.12+
- इंटरैक्टिव सीखने के लिए Jupyter नोटबुक्स
- AI फ्रेमवर्क्स: Microsoft Agent Framework (MAF)
- Azure AI सेवाएं: Microsoft Foundry, Microsoft Foundry Agent Service V2

**आर्किटेक्चर:**
- पाठ-आधारित संरचना (00-18 निर्देशिकाएँ)
- प्रत्येक पाठ में शामिल हैं: README दस्तावेज़, कोड नमूने (Jupyter नोटबुक्स), और छवियाँ
- स्वचालित अनुवाद प्रणाली के माध्यम से बहुभाषी समर्थन
- प्रत्येक पाठ के लिए एक Python नोटबुक जिसका उपयोग Microsoft Agent Framework करता है

## सेटअप कमांड्स

### आवश्यकताएँ
- Python 3.12 या उच्चतर
- Azure सदस्यता (Microsoft Foundry के लिए)
- Azure CLI स्थापित और प्रमाणीकृत (`az login`)

### प्रारंभिक सेटअप

1. **रिपॉजिटरी क्लोन या फोर्क करें:**
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

3. **निर्भरता स्थापित करें:**
   ```bash
   pip install -r requirements.txt
   ```

4. **पर्यावरण चर सेट करें:**
   ```bash
   cp .env.example .env
   # Edit .env with your API keys and endpoints
   ```

### आवश्यक पर्यावरण चर

**Microsoft Foundry** के लिए (ज़रूरी):
- `AZURE_AI_PROJECT_ENDPOINT` - Microsoft Foundry परियोजना एंडपॉइंट
- `AZURE_AI_MODEL_DEPLOYMENT_NAME` - मॉडल तैनाती का नाम (जैसे gpt-5-mini)

**Azure AI Search** के लिए (पाठ 05 - RAG):
- `AZURE_SEARCH_SERVICE_ENDPOINT` - Azure AI Search एंडपॉइंट
- `AZURE_SEARCH_API_KEY` - Azure AI Search API कुंजी

प्रमाणीकरण: नोटबुक्स चलाने से पहले `az login` चलाएँ (जो `AzureCliCredential` का उपयोग करता है)।

## विकास कार्यप्रवाह

### Jupyter नोटबुक्स चलाना

प्रत्येक पाठ में विभिन्न फ्रेमवर्क्स के लिए कई Jupyter नोटबुक्स होती हैं:

1. **Jupyter शुरू करें:**
   ```bash
   jupyter notebook
   ```

2. **किसी पाठ निर्देशिका पर जाएँ** (जैसे `01-intro-to-ai-agents/code_samples/`)

3. **नोटबुक्स खोलें और चलाएँ:**
   - `*-python-agent-framework.ipynb` - Microsoft Agent Framework का उपयोग करते हुए (Python)
   - `*-dotnet-agent-framework.ipynb` - Microsoft Agent Framework का उपयोग करते हुए (.NET)

### Microsoft Agent Framework के साथ काम करना

**Microsoft Agent Framework + Microsoft Foundry:**
- Azure सदस्यता आवश्यक
- एजेंट सेवा V2 के लिए `FoundryChatClient` का उपयोग करता है (एजेंट Foundry पोर्टल में दिखाई देते हैं)
- अंतर्निहित अवलोकनशीलता के साथ उत्पादन-तैयार
- फ़ाइल पैटर्न: `*-python-agent-framework.ipynb`

## परीक्षण निर्देश

यह एक शैक्षिक रिपॉजिटरी है जिसमें उदाहरण कोड है, न कि उत्पादन कोड जिसमें स्वचालित परीक्षण हैं। अपनी सेटअप और परिवर्तनों को सत्यापित करने के लिए:

### मैन्युअल परीक्षण

1. **Python पर्यावरण का परीक्षण करें:**
   ```bash
   python --version  # Should be 3.12+
   pip list | grep -E "(agent-framework|azure-ai|azure-identity)"
   ```

2. **नोटबुक निष्पादन का परीक्षण करें:**
   ```bash
   # Convert notebook to script and run (tests imports)
   jupyter nbconvert --to script <lesson-folder>/code_samples/<notebook>.ipynb --stdout | python
   ```

3. **पर्यावरण चर सत्यापित करें:**
   ```bash
   python -c "import os; from dotenv import load_dotenv; load_dotenv(); print('✓ AZURE_AI_PROJECT_ENDPOINT' if os.getenv('AZURE_AI_PROJECT_ENDPOINT') else '✗ AZURE_AI_PROJECT_ENDPOINT missing')"
   ```

### व्यक्तिगत नोटबुक्स चलाना

Jupyter में नोटबुक खोलें और कोशिकाओं को क्रमबद्ध रूप से निष्पादित करें। प्रत्येक नोटबुक स्वायत्त है और इसमें शामिल हैं:
- आयात कथन
- कॉन्फ़िगरेशन लोडिंग
- उदाहरण एजेंट कार्यान्वयन
- मार्कडाउन कोशिकाओं में अपेक्षित आउटपुट

### तैनात एजेंट्स का स्मोक-टेस्टिंग

उन पाठों के लिए जहां एजेंट Microsoft Foundry होस्टेड एजेंट के रूप में तैनात है (01, 04, 05, 16), रिपॉजिटरी `tests/` के अंतर्गत स्मोक-टेस्ट कैटलॉग भेजता है जो `.github/workflows/smoke-test.yml` कार्यप्रवाह के द्वारा [AI स्मोक टेस्ट](https://github.com/marketplace/actions/ai-smoke-test) क्रिया के माध्यम से चलाए जाते हैं। ये एक हल्का-पोस्ट-डिप्लॉय गेट हैं (क्या एजेंट पहुँच योग्य है और बुनियादी प्रांप्ट अपेक्षाओं का पालन कर रहा है?), जो पाठ 10 और 16 में मूल्यांकन पाइपलाइन के पूरक हैं। कैटलॉग-से-पाठ-से-एजेंट मैपिंग के लिए [tests/README.md](./tests/README.md) देखें। पाठ 17 स्थानीय रूप से Foundry Local के साथ चलता है और इसका कोई होस्टेड एंडपॉइंट नहीं है, इसलिए इसका सत्यापन सीधे इसकी नोटबुक चलाकर किया जाता है।

## कोड शैली

### Python कन्वेंशंस

- **Python संस्करण**: 3.12+
- **कोड शैली**: मानक Python PEP 8 कन्वेंशंस का पालन करें
- **नोटबुक्स**: अवधारणाओं को समझाने के लिए स्पष्ट मार्कडाउन कोशिकाएँ उपयोग करें
- **आयात**: मानक लाइब्रेरी, तीसरे पक्ष, स्थानीय आयातों के अनुसार समूह बनाएं

### Jupyter नोटबुक कन्वेंशंस

- कोड कोशिकाओं से पहले वर्णनात्मक मार्कडाउन कोशिकाएँ शामिल करें
- संदर्भ के लिए नोटबुक्स में आउटपुट के उदाहरण जोड़ें
- पाठ अवधारणाओं से मेल खाने वाले स्पष्ट चर नामों का उपयोग करें
- नोटबुक निष्पादन क्रम को रैखिक बनाए रखें (कोशिका 1 → 2 → 3...)

### फ़ाइल संगठन

```
<lesson-number>-<lesson-name>/
├── README.md                     # Lesson documentation
├── code_samples/
│   ├── <number>-python-agent-framework.ipynb
│   └── <number>-dotnet-agent-framework.ipynb  (optional)
└── images/
    └── *.png
```

## निर्माण और तैनाती

### दस्तावेज़ निर्माण

यह रिपॉजिटरी दस्तावेज़ के लिए मार्कडाउन का उपयोग करती है:
- प्रत्येक पाठ फ़ोल्डर में README.md फ़ाइलें
- रिपॉजिटरी रूट पर मुख्य README.md
- GitHub Actions के माध्यम से स्वचालित अनुवाद प्रणाली

### CI/CD पाइपलाइन

स्थित है `.github/workflows/`:

1. **co-op-translator.yml** - 50+ भाषाओं में स्वचालित अनुवाद
2. **welcome-issue.yml** - नए issue निर्माताओं का स्वागत करता है
3. **welcome-pr.yml** - नए pull request योगदानकर्ताओं का स्वागत करता है

### तैनाती

यह एक शैक्षिक रिपॉजिटरी है - कोई तैनाती प्रक्रिया नहीं है। उपयोगकर्ता:
1. रिपॉजिटरी को फोर्क या क्लोन करें
2. नोटबुक्स को स्थानीय रूप से या GitHub Codespaces में चलाएँ
3. उदाहरण संशोधित करके और प्रयोग करके सीखें

## पुल अनुरोध दिशानिर्देश

### सबमिट करने से पहले

1. **अपने परिवर्तनों का परीक्षण करें:**
   - प्रभावित नोटबुक्स को पूरी तरह चलाएँ
   - सुनिश्चित करें कि सभी कोशिकाएँ बिना त्रुटि के चलती हैं
   - जांचें कि आउटपुट उपयुक्त हैं

2. **दस्तावेज़ अपडेट करें:**
   - नया विषय जोड़ने पर README.md अपडेट करें
   - जटिल कोड के लिए नोटबुक्स में टिप्पणियाँ जोड़ें
   - सुनिश्चित करें कि मार्कडाउन कोशिकाएँ उद्देश्य समझाती हैं

3. **फ़ाइल परिवर्तनों:**
   - `.env` फ़ाइलें कमिट करने से बचें (`.env.example` का उपयोग करें)
   - `venv/` या `__pycache__/` निर्देशिकाओं को कमिट न करें
   - जब वे अवधारणाएं दिखाते हैं तो नोटबुक आउटपुट रखें
   - अस्थायी फ़ाइलें और बैकअप नोटबुक हटाएँ (`*-backup.ipynb`)

### PR टाइटल प्रारूप

विवरणात्मक शीर्षक उपयोग करें:
- `[Lesson-XX] Add new example for <concept>`
- `[Fix] Correct typo in lesson-XX README`
- `[Update] Improve code sample in lesson-XX`
- `[Docs] Update setup instructions`

### आवश्यक जांचें

- नोटबुक्स बिना त्रुटि के चलनी चाहिए
- README फ़ाइलें स्पष्ट और सटीक होनी चाहिए
- रिपॉजिटरी में मौजूदा कोड पैटर्न का पालन करें
- अन्य पाठों के साथ संगति बनाए रखें

## अतिरिक्त नोट्स

### सामान्य सावधानियाँ

1. **Python संस्करण मेल नहीं खाना:**
   - सुनिश्चित करें कि Python 3.12+ उपयोग हो रहा है
   - कुछ पैकेज पुराने संस्करणों के साथ काम नहीं कर सकते
   - स्पष्ट रूप से Python संस्करण निर्दिष्ट करने के लिए `python3 -m venv` का उपयोग करें

2. **पर्यावरण चर:**
   - हमेशा `.env` को `.env.example` से बनाएं
   - `.env` फाइल कमिट न करें (यह `.gitignore` में है)
   - keyless Entra ID प्रमाणीकरण के लिए `az login` के साथ साइन इन करें

3. **पैकेज संघर्ष:**
   - नया वर्चुअल एनवायरनमेंट उपयोग करें
   - व्यक्तिगत पैकेजों के बजाय `requirements.txt` से इंस्टॉल करें
   - कुछ नोटबुक्स को उनके मार्कडाउन कोशिकाओं में उल्लेखित अतिरिक्त पैकेजों की आवश्यकता हो सकती है

4. **Azure सेवाएं:**
   - Azure AI सेवाओं के लिए सक्रिय सदस्यता आवश्यक है
   - कुछ सुविधाएँ क्षेत्र-विशिष्ट हो सकती हैं
   - सुनिश्चित करें कि आपकी Azure OpenAI मॉडल तैनाती Responses API का समर्थन करती है

### सीखने का मार्ग

अनुशंसित क्रम:
1. **00-course-setup** - पर्यावरण सेटअप के लिए प्रारंभ करें
2. **01-intro-to-ai-agents** - AI एजेंट मूल बातें समझें
3. **02-explore-agentic-frameworks** - विभिन्न फ्रेमवर्क्स के बारे में जानें
4. **03-agentic-design-patterns** - मुख्य डिजाइन पैटर्न्स
5. क्रमिक रूप से क्रमांकित पाठों के माध्यम से जारी रखें

### फ्रेमवर्क चयन

अपने उद्देश्यों के आधार पर फ्रेमवर्क चुनें:
- **सभी पाठ**: Microsoft Agent Framework (MAF) `FoundryChatClient` के साथ
- एजेंट Microsoft Foundry Agent Service V2 में सर्वर-साइड पंजीकृत होते हैं और Foundry पोर्टल में दिखाई देते हैं

### सहायता प्राप्त करना

- [Microsoft Foundry Community Discord](https://aka.ms/ai-agents/discord) में शामिल हों
- विशिष्ट मार्गदर्शन के लिए पाठ README फ़ाइलें देखें
- कोर्स अवलोकन के लिए मुख्य [README.md](./README.md) जांचें
- विस्तृत सेटअप निर्देशों के लिए [Course Setup](./00-course-setup/README.md) देखें

### योगदान देना

यह एक खुला शैक्षिक प्रोजेक्ट है। योगदान स्वागत योग्य हैं:
- कोड उदाहरण सुधारें
- टाइपो या त्रुटियाँ ठीक करें
- स्पष्ट टिप्पणियाँ जोड़ें
- नए पाठ विषय सुझाएँ
- अतिरिक्त भाषाओं में अनुवाद करें

वर्तमान आवश्यकताओं के लिए [GitHub Issues](https://github.com/microsoft/ai-agents-for-beginners/issues) देखें।

## प्रोजेक्ट-विशिष्ट संदर्भ

### बहुभाषी समर्थन

यह रिपॉजिटरी स्वचालित अनुवाद प्रणाली का उपयोग करती है:
- 50+ भाषाएँ समर्थित
- अनुवाद `/translations/<lang-code>/` निर्देशिकाओं में हैं
- अनुवाद अपडेट को संभालने के लिए GitHub Actions कार्यप्रवाह
- स्रोत फ़ाइलें अंग्रेजी में रिपॉजिटरी रूट पर

### पाठ संरचना

प्रत्येक पाठ एक सुसंगत पैटर्न का पालन करता है:
1. लिंक के साथ वीडियो थम्बनेल
2. लिखित पाठ सामग्री (README.md)
3. कई फ्रेमवर्क्स में कोड नमूने
4. सीखने के उद्देश्य और पूर्वापेक्षाएँ
5. अतिरिक्त सीखने के संसाधन जुड़े हुए

### कोड नमूने का नामकरण

फॉर्मेट: `<lesson-number>-python-agent-framework.ipynb`
- `01-python-agent-framework.ipynb` - पाठ 1, MAF Python
- `14-sequential.ipynb` - पाठ 14, MAF उन्नत पैटर्न
- `16-python-agent-framework.ipynb` - पाठ 16, उत्पादन ग्राहक-समर्थन एजेंट
- `17-local-agent-foundry-local.ipynb` - पाठ 17, स्थानीय एजेंट Foundry Local + Qwen के साथ

### विशेष निर्देशिकाएँ

- `translated_images/` - अनुवादों के लिए स्थानीयकृत छवियाँ
- `images/` - अंग्रेज़ी सामग्री के लिए मूल छवियाँ
- `.devcontainer/` - VS Code विकास कंटेनर कॉन्फ़िगरेशन
- `.github/` - GitHub Actions कार्यप्रवाह और टेम्पलेट्स

### निर्भरता

प्रमुख पैकेज्स `requirements.txt` से:
- `agent-framework` - Microsoft Agent Framework
- `a2a-sdk` - एजेंट-से-एजेंट प्रोटोकॉल समर्थन
- `azure-ai-inference`, `azure-ai-projects` - Azure AI सेवाएं
- `azure-identity` - Azure प्रमाणीकरण (AzureCliCredential)
- `azure-search-documents` - Azure AI Search एकीकरण
- `mcp[cli]` - मॉडल संदर्भ प्रोटोकॉल समर्थन

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**अस्वीकरण**:
इस दस्तावेज़ का अनुवाद AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) का उपयोग करके किया गया है। जबकि हम सटीकता के लिए प्रयास करते हैं, कृपया ध्यान दें कि स्वचालित अनुवादों में त्रुटियाँ या अशुद्धियाँ हो सकती हैं। मूल दस्तावेज़ अपनी मूल भाषा में ही प्रामाणिक स्रोत माना जाना चाहिए। महत्वपूर्ण जानकारी के लिए, पेशेवर मानव अनुवाद की सिफारिश की जाती है। इस अनुवाद के उपयोग से उत्पन्न किसी भी गलतफहमी या गलत व्याख्या के लिए हम उत्तरदायी नहीं हैं।
<!-- CO-OP TRANSLATOR DISCLAIMER END -->