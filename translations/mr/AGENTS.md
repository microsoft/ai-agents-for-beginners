# AGENTS.md

## प्रकल्पाचा आढावा

या रिपॉझिटरीमध्ये "सोप्या लोकांसाठी AI एजंट्स" - AI एजंट्स तयार करण्यासाठी आवश्यक सर्वकाही शिकवणारा एक व्यापक शैक्षणिक कोर्स समाविष्ट आहे. या कोर्समध्ये 18 धडे (क्रमांक 00-18) आहेत जे मूलतत्त्वे, डिझाइन पॅटर्न, फ्रेमवर्क, उत्पादन तैनाती, स्थानिक/डिव्हाइसवर चालणारे एजंट्स, आणि AI एजंट्सची सुरक्षितता यांचा समावेश करतात.

**महत्त्वाच्या तंत्रज्ञान:**
- Python 3.12+
- संवादात्मक शिक्षणासाठी Jupyter नोटबुक्स
- AI फ्रेमवर्क्स: Microsoft Agent Framework (MAF)
- Azure AI सेवाः Microsoft Foundry, Microsoft Foundry Agent Service V2

**आर्किटेक्चर:**
- धडा आधारित रचना (00-18 डिरेक्टरीज)
- प्रत्येक धड्यामध्ये: README दस्तऐवज, कोड सॅम्पल्स (Jupyter नोटबुक्स), आणि प्रतिमा असतात
- स्वयंचलित अनुवाद प्रणालीद्वारे बहुभाषिक समर्थन
- Microsoft Agent Framework वापरून प्रत्येक धड्यासाठी एक Python नोटबुक

## सेटअप कमांड्स

### पूर्वपरिस्तिथी
- Python 3.12 किंवा त्याहून अधिक
- Azure सदस्यता (Microsoft Foundry साठी)
- Azure CLI इन्स्टॉल आणि प्रमाणित केलेले (`az login`)

### पहिला सेटअप

1. **रिपॉझिटरी क्लोन करा किंवा फोर्क करा:**
   ```bash
   gh repo fork microsoft/ai-agents-for-beginners --clone
   # OR
   git clone https://github.com/microsoft/ai-agents-for-beginners.git
   cd ai-agents-for-beginners
   ```

2. **Python वर्चुअल एन्व्हायर्नमेंट तयार करा आणि सक्रिय करा:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **अधिकारिका इन्स्टॉल करा:**
   ```bash
   pip install -r requirements.txt
   ```

4. **एन्व्हायर्नमेंट व्हेरिएबल्स सेट करा:**
   ```bash
   cp .env.example .env
   # Edit .env with your API keys and endpoints
   ```

### आवश्यक पर्यावरणीय चल (Environment Variables)

**Microsoft Foundry** साठी (आवश्यक):
- `AZURE_AI_PROJECT_ENDPOINT` - Microsoft Foundry प्रोजेक्ट एंडपॉईंट
- `AZURE_AI_MODEL_DEPLOYMENT_NAME` - मॉडेल तैनातीचे नाव (उदा. gpt-5-mini)

**Azure AI Search** साठी (धडा 05 - RAG):
- `AZURE_SEARCH_SERVICE_ENDPOINT` - Azure AI Search एंडपॉईंट
- `AZURE_SEARCH_API_KEY` - Azure AI Search API की

प्रमाणिकरण: नोटबुक्स चालवण्यापूर्वी `az login` चालवा (यामध्ये `AzureCliCredential` वापरले जाते).

## विकास कार्यप्रवाह

### Jupyter नोटबुक्स चालवणे

प्रत्येक धड्यात वेगवेगळ्या फ्रेमवर्कसाठी अनेक Jupyter नोटबुक्स असतात:

1. **Jupyter सुरू करा:**
   ```bash
   jupyter notebook
   ```

2. **धडा डिरेक्टरीकडे जा** (उदा. `01-intro-to-ai-agents/code_samples/`)

3. **नोटबुक उघडा आणि चालवा:**
   - `*-python-agent-framework.ipynb` - Microsoft Agent Framework वापरून (Python)
   - `*-dotnet-agent-framework.ipynb` - Microsoft Agent Framework वापरून (.NET)

### Microsoft Agent Framework सह काम करणे

**Microsoft Agent Framework + Microsoft Foundry:**
- Azure सदस्यता आवश्यक आहे
- Agent Service V2 साठी `FoundryChatClient` वापरतो (Foundry पोर्टलमध्ये एजंट दिसतात)
- अंगभूत निरीक्षणासह उत्पादनासाठी तयार
- फाईल नमुना: `*-python-agent-framework.ipynb`

## परीक्षण सूचना

ही शैक्षणिक रिपॉझिटरी आहे ज्यामध्ये उत्पादनासाठी कोड नाही पण उदाहरणार्थ कोड आहे. तुमचा सेटअप आणि बदलांची तपासणी करण्यासाठी:

### मॅन्युअल टेस्टिंग

1. **Python वातावरणाची परीक्षा करा:**
   ```bash
   python --version  # Should be 3.12+
   pip list | grep -E "(agent-framework|azure-ai|azure-identity)"
   ```

2. **नोटबुक अंमलबजावणीची चाचणी करा:**
   ```bash
   # Convert notebook to script and run (tests imports)
   jupyter nbconvert --to script <lesson-folder>/code_samples/<notebook>.ipynb --stdout | python
   ```

3. **एन्व्हायर्नमेंट व्हेरिएबल्सची तपासणी करा:**
   ```bash
   python -c "import os; from dotenv import load_dotenv; load_dotenv(); print('✓ AZURE_AI_PROJECT_ENDPOINT' if os.getenv('AZURE_AI_PROJECT_ENDPOINT') else '✗ AZURE_AI_PROJECT_ENDPOINT missing')"
   ```

### स्वतंत्र नोटबुक्स चालवणे

Jupyter मध्ये नोटबुक उघडा आणि क्रमाने सेल्स चालवा. प्रत्येक नोटबुक स्वतंत्र असून त्यात समाविष्ट आहे:
- आयात स्टेटमेंट्स
- कॉन्फिगरेशन लोडिंग
- उदाहरण एजंट अंमलबजावण्या
- markdown सेल्स मध्ये अपेक्षित आउटपुट्स

### तैनात एजंट्सचे स्मोक-टेस्टिंग

ज्या धड्यामध्ये एजंट Microsoft Foundry होस्टेड एजंट म्हणून तैनात आहे (01, 04, 05, 16), त्या रिपॉझिटरीमध्ये `tests/` अंतर्गत स्मोक-टेस्ट कॅटलॉग्स आहेत जे `.github/workflows/smoke-test.yml` कार्यप्रवाहाद्वारे [AI Smoke Test](https://github.com/marketplace/actions/ai-smoke-test) क्रिया वापरून चालवली जातात. हे हलक्या वजनाचे पोस्ट-डिप्लॉय गेट म्हणून कार्य करतात (एजंट पोहोचण्यायोग्य आहे का आणि मूलभूत प्रॉम्प्ट अपेक्षा पूर्ण करत आहे का?), जे धडा 10 आणि 16 मधील मूल्यमापन पाईपलाइनला पूरक आहे. कॅटलॉग-टू-लेसन-टू-एजंट मॅपिंगसाठी [tests/README.md](./tests/README.md) पहा. धडा 17 स्थानिक Foundry Local सह लोकल चालवतो आणि त्याचा होस्टेड एंडपॉईंट नाही, त्यामुळे तो त्याचा नोटबुक थेट चालवून सत्यापित केला जातो.

## कोड शैली

### Python नियम

- **Python आवृत्ती**: 3.12+
- **कोड शैली**: मानक Python PEP 8 नियम पाळा
- **नोटबुक्स**: कल्पना स्पष्ट करण्यासाठी स्पष्ट markdown सेल वापरा
- **आयात**: मानक लायब्ररी, तृतीय-पक्ष, स्थानिक आयात यानुसार गट करा

### Jupyter नोटबुक नियम

- कोड सेल्सपूर्वी वर्णनात्मक markdown सेल्स समाविष्ट करा
- संदर्भासाठी नोटबुकमध्ये आउटपुट उदाहरणे जोडा
- धडाच्या संकल्पनांशी जुळणारी स्पष्ट वेरिएबल नावे वापरा
- नोटबुक अंमलबजावणीची क्रमानुसार linear ठेवाः सेल 1 → 2 → 3...

### फाईल संघटना

```
<lesson-number>-<lesson-name>/
├── README.md                     # Lesson documentation
├── code_samples/
│   ├── <number>-python-agent-framework.ipynb
│   └── <number>-dotnet-agent-framework.ipynb  (optional)
└── images/
    └── *.png
```

## बांधणी आणि तैनाती

### दस्तऐवज तयार करणे

ही रिपॉझिटरी दस्तऐवजासाठी Markdown वापरते:
- प्रत्येक धडा फोल्डरमध्ये README.md फाईल्स
- मुख्य README.md रिपॉझिटरीच्या मूळ स्थानी
- GitHub Actions द्वारे स्वयंचलित अनुवाद प्रणाली

### CI/CD पाईपलाइन

स्थिती: `.github/workflows/`:

1. **co-op-translator.yml** - ५०+ भाषांमध्ये स्वयंचलित अनुवाद
2. **welcome-issue.yml** - नवीन इश्यू निर्मात्यांचे स्वागत
3. **welcome-pr.yml** - नवीन पुल विनंती योगदानकर्त्यांचे स्वागत

### तैनाती

ही शैक्षणिक रिपॉझिटरी आहे - कोणतीही तैनाती प्रक्रिया नाही. वापरकर्ते:
1. रिपॉझिटरी फोर्क किंवा क्लोन करा
2. नोटबुक स्थानिक किंवा GitHub Codespaces मध्ये चालवा
3. उदाहरणांमध्ये बदल करून आणि प्रयोग करून शिका

## पुल विनंती मार्गदर्शक तत्त्वे

### सबमिट करण्यापूर्वी

1. **तुमचे बदल तपासा:**
   - प्रभावित नोटबुक्स पूर्णपणे चालवा
   - सर्व सेल्स त्रुटीशिवाय चालतात का ते तपासा
   - आउटपुट्स योग्य आहेत का ते तपासा

2. **दस्तऐवज अपडेट्स:**
   - नवीन संकल्पना जोडत असल्यास README.md अद्यतनित करा
   - क्लिष्ट कोडसाठी नोटबुक्समध्ये टिप्पण्या जोडा
   - markdown सेल्स मध्ये उद्दिष्ट स्पष्ट करा

3. **फाईल बदल:**
   - `.env` फाईल्स कमिट करू नका (तुम्ही `.env.example` वापरा)
   - `venv/` किंवा `__pycache__/` डिरेक्टरीज कमिट करू नका
   - नोटबुक आउटपुट्स ठेवा जेव्हा ते संकल्पना स्पष्ट करतात
   - तात्पुरत्या फाईल्स आणि बॅकअप नोटबुक्स काढा (`*-backup.ipynb`)

### PR शीर्षक फॉर्मॅट

वर्णनात्मक शीर्षके वापरा:
- `[Lesson-XX] Add new example for <concept>`
- `[Fix] Correct typo in lesson-XX README`
- `[Update] Improve code sample in lesson-XX`
- `[Docs] Update setup instructions`

### आवश्यक तपासण्या

- नोटबुक्स त्रुटीशिवाय चालणे आवश्यक आहे
- README फाईल्स स्पष्ट आणि अचूक असाव्यात
- रिपॉझिटरीतील विद्यमान कोड नमुना पाळा
- इतर धडांशी सुसंगतता राखा

## अतिरिक्त नोंदी

### सामान्य चुका

1. **Python आवृत्तीचा विसंगतता:**
   - Python 3.12+ वापरण्याची खात्री करा
   - काही पॅकेजेस जुन्या आवृत्त्यांसह काम करणार नाहीत
   - Python आवृत्ती स्पष्ट करण्यासाठी `python3 -m venv` वापरा

2. **एन्व्हायर्नमेंट व्हेरिएबल्स:**
   - प्रत्येक वेळेस `.env` पासून `.env.example` तयार करा
   - `.env` फाईल कमिट करू नका (ती `.gitignore` मध्ये आहे)
   - Entra ID चे कीलेस प्रमाणीकरणसाठी `az login` वापरा

3. **पॅकेज संघर्ष:**
   - नवीन वर्चुअल एन्व्हायर्नमेंट वापरा
   - वेगळ्या पॅकेजेसऐवजी `requirements.txt` मधून इन्स्टॉल करा
   - काही नोटबुकसाठी त्यांच्या markdown सेल्समध्ये नमूद केलेले अतिरिक्त पॅकेज आवश्यक असू शकतात

4. **Azure सेवा:**
   - Azure AI सेवा सक्रिय सदस्यता आवश्यक आहे
   - काही वैशिष्ट्ये क्षेत्र-विशिष्ट असू शकतात
   - तुमच्या Azure OpenAI मॉडेल तैनातीने Responses API समर्थन करत असल्याची खात्री करा

### शिकण्याचा मार्ग

धडे अनुक्रमे पुढीलप्रमाणे पुढे जाण्याची शिफारस केली आहे:
1. **00-course-setup** - येथे पर्यावरण सेटअपसाठी सुरुवात करा
2. **01-intro-to-ai-agents** - AI एजंट मूलतत्त्वे समजून घ्या
3. **02-explore-agentic-frameworks** - विविध फ्रेमवर्क्सबद्दल शिका
4. **03-agentic-design-patterns** - मुख्य डिझाइन पॅटर्न्स
5. क्रमांकाने दिलेले पुढील धडे पूर्ण करा

### फ्रेमवर्क निवड

तुमच्या उद्दिष्टांनुसार फ्रेमवर्क निवडा:
- **सर्व धडे**: Microsoft Agent Framework (MAF) सह `FoundryChatClient`
- एजंट Microsoft Foundry Agent Service V2 मध्ये सर्व्हर साईडवर नोंदणी करतात आणि Foundry पोर्टलमध्ये दिसतात

### मदत मिळवा

- [Microsoft Foundry Community Discord](https://aka.ms/ai-agents/discord) मध्ये सामील व्हा
- विशिष्ट मार्गदर्शनासाठी धड्यांच्या README फाइल तपासा
- कोर्स आढाव्यासाठी मुख्य [README.md](./README.md) पहा
- सविस्तर सेटअप सूचना साठी [Course Setup](./00-course-setup/README.md) पहा

### योगदान

हा एक खुला शैक्षणिक प्रकल्प आहे. योगदान स्वागतार्ह:
- कोड उदाहरणे सुधारित करा
- टायपो किंवा त्रुटी दुरुस्त करा
- समज स्पष्ट करणाऱ्या टिप्पण्या जोडा
- नवीन धडा विषय सुचवा
- अधिक भाषांमध्ये अनुवाद करा

सध्याच्या गरजांसाठी [GitHub Issues](https://github.com/microsoft/ai-agents-for-beginners/issues) पहा.

## प्रकल्प-विशिष्ट संदर्भ

### बहुभाषिक समर्थन

ही रिपॉझिटरी स्वयंचलित अनुवाद प्रणाली वापरते:
- ५०+ भाषा समर्थित
- अनुवाद `/translations/<lang-code>/` डिरेक्टरीज मध्ये आहेत
- GitHub Actions कार्यप्रवाह अनुवाद अद्यतने हाताळतो
- स्रोत फाईल्स इंग्रजीमध्ये रिपॉझिटरीच्या मूळ स्थानी आहेत

### धडा संरचना

प्रत्येक धडा एकसारखा नमुना अनुसरतो:
1. व्हिडिओ थंबनेलसह लिंक
2. लिखित धडा सामग्री (README.md)
3. अनेक फ्रेमवर्कमध्ये कोड सॅम्पल्स
4. शिका उद्दिष्टे आणि पूर्वअट
5. अतिरिक्त शिकण्याचे स्रोत लिंक केलेले

### कोड सॅम्पल नावकरण

स्वरूप: `<lesson-number>-python-agent-framework.ipynb`
- `01-python-agent-framework.ipynb` - धडा 1, MAF Python
- `14-sequential.ipynb` - धडा 14, MAF प्रगत पॅटर्न
- `16-python-agent-framework.ipynb` - धडा 16, उत्पादन ग्राहक-समर्थन एजंट
- `17-local-agent-foundry-local.ipynb` - धडा 17, स्थानिक एजंट Foundry Local + Qwen सह

### विशेष फोल्डर्स

- `translated_images/` - अनुवादांसाठी स्थानिकीकृत प्रतिमा
- `images/` - इंग्रजी सामग्रीसाठी मूळ प्रतिमा
- `.devcontainer/` - VS Code विकास कंटेनर विन्यास
- `.github/` - GitHub Actions कार्यप्रवाह आणि साचे

### अवलंबित्व

महत्त्वाचे पॅकेजेस `requirements.txt` मधून:
- `agent-framework` - Microsoft Agent Framework
- `a2a-sdk` - एजंट-टू-एजंट प्रोटोकॉल समर्थन
- `azure-ai-inference`, `azure-ai-projects` - Azure AI सेवा
- `azure-identity` - Azure प्रमाणीकरण (AzureCliCredential)
- `azure-search-documents` - Azure AI Search एकत्रीकरण
- `mcp[cli]` - मॉडेल कॉन्टेक्स्ट प्रोटोकॉल समर्थन

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**अस्वीकरण**:
हा दस्तऐवज AI भाषांतर सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) चा वापर करून अनुवादित केला आहे. जरी आम्ही अचूकतेसाठी प्रयत्न करतो, तरी कृपया लक्षात घ्या की स्वयंचलित भाषांतरांमध्ये त्रुटी किंवा अचूकतेची कमतरता असू शकते. मूळ दस्तऐवज त्याच्या मूळ भाषेत अधिकृत स्रोत मानला पाहिजे. महत्त्वाची माहिती असल्यास, व्यावसायिक मानवी भाषांतराची शिफारस केली जाते. या भाषांतराच्या वापरामुळे उद्भवणाऱ्या कोणत्याही गैरसमज किंवा चुकीच्या अर्थलावणीसाठी आम्ही जबाबदार नाही.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->