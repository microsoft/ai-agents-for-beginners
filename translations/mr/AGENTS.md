# AGENTS.md

## प्रकल्पाचा आढावा

हे रिपॉझिटरी "AI Agents for Beginners" - एक व्यापक शैक्षणिक कोर्स आहे जो AI एजंट्स तयार करण्यासाठी आवश्यक असलेल्या सर्व गोष्टी शिकवतो. या कोर्समध्ये 15+ धडे आहेत ज्यामध्ये मूलभूत गोष्टी, डिझाइन पॅटर्न, फ्रेमवर्क्स आणि AI एजंट्सचे उत्पादन तैनाती समाविष्ट आहे.

**मुख्य तंत्रज्ञान:**
- Python 3.12+
- परस्पर शिकण्यासाठी Jupyter Notebooks
- AI फ्रेमवर्क्स: Semantic Kernel, AutoGen, Microsoft Agent Framework (MAF)
- Azure AI Services: Azure AI Foundry, Azure AI Agent Service
- GitHub Models Marketplace (फ्री टियर उपलब्ध)

**आर्किटेक्चर:**
- धड्यांवर आधारित रचना (00-15+ डिरेक्टरीज)
- प्रत्येक धड्यात: README दस्तऐवज, कोड नमुने (Jupyter notebooks), आणि प्रतिमा
- स्वयंचलित भाषांतर प्रणालीद्वारे बहुभाषिक समर्थन
- प्रत्येक धड्यासाठी एकाधिक फ्रेमवर्क पर्याय (Semantic Kernel, AutoGen, Azure AI Agent Service)

## सेटअप कमांड्स

### पूर्वतयारी
- Python 3.12 किंवा त्याहून अधिक
- GitHub खाते (GitHub Models - फ्री टियरसाठी)
- Azure सदस्यता (पर्यायी, Azure AI सेवांसाठी)

### प्रारंभिक सेटअप

1. **रिपॉझिटरी क्लोन किंवा फोर्क करा:**
   ```bash
   gh repo fork microsoft/ai-agents-for-beginners --clone
   # OR
   git clone https://github.com/microsoft/ai-agents-for-beginners.git
   cd ai-agents-for-beginners
   ```

2. **Python व्हर्च्युअल वातावरण तयार करा आणि सक्रिय करा:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **आवश्यकता स्थापित करा:**
   ```bash
   pip install -r requirements.txt
   ```

4. **पर्यावरणीय व्हेरिएबल्स सेट करा:**
   ```bash
   cp .env.example .env
   # Edit .env with your API keys and endpoints
   ```


### आवश्यक पर्यावरणीय व्हेरिएबल्स

**GitHub Models (फ्री) साठी:**
- `GITHUB_TOKEN` - GitHub वरून वैयक्तिक प्रवेश टोकन

**Azure AI Services** (पर्यायी) साठी:
- `PROJECT_ENDPOINT` - Azure AI Foundry प्रकल्पाचा एंडपॉइंट
- `AZURE_OPENAI_API_KEY` - Azure OpenAI API की
- `AZURE_OPENAI_ENDPOINT` - Azure OpenAI एंडपॉइंट URL
- `AZURE_OPENAI_CHAT_DEPLOYMENT_NAME` - चॅट मॉडेलसाठी डिप्लॉयमेंट नाव
- `AZURE_OPENAI_EMBEDDING_DEPLOYMENT_NAME` - एम्बेडिंगसाठी डिप्लॉयमेंट नाव
- `.env.example` मध्ये दाखवलेल्या अतिरिक्त Azure कॉन्फिगरेशन

## विकास कार्यप्रवाह

### Jupyter Notebooks चालवणे

प्रत्येक धड्यात विविध फ्रेमवर्कसाठी अनेक Jupyter notebooks आहेत:

1. **Jupyter सुरू करा:**
   ```bash
   jupyter notebook
   ```

2. **धड्याच्या डिरेक्टरीमध्ये जा** (उदा., `01-intro-to-ai-agents/code_samples/`)

3. **नोटबुक उघडा आणि चालवा:**
   - `*-semantic-kernel.ipynb` - Semantic Kernel फ्रेमवर्क वापरून
   - `*-autogen.ipynb` - AutoGen फ्रेमवर्क वापरून
   - `*-python-agent-framework.ipynb` - Microsoft Agent Framework (Python) वापरून
   - `*-dotnet-agent-framework.ipynb` - Microsoft Agent Framework (.NET) वापरून
   - `*-azureaiagent.ipynb` - Azure AI Agent Service वापरून

### विविध फ्रेमवर्कसह काम करणे

**Semantic Kernel + GitHub Models:**
- GitHub खात्यासह फ्री टियर उपलब्ध
- शिकण्यासाठी आणि प्रयोगासाठी चांगले
- फाइल नमुना: `*-semantic-kernel*.ipynb`

**AutoGen + GitHub Models:**
- GitHub खात्यासह फ्री टियर उपलब्ध
- मल्टी-एजंट ऑर्केस्ट्रेशन क्षमता
- फाइल नमुना: `*-autogen.ipynb`

**Microsoft Agent Framework (MAF):**
- Microsoft कडून नवीनतम फ्रेमवर्क
- Python आणि .NET मध्ये उपलब्ध
- फाइल नमुना: `*-agent-framework.ipynb`

**Azure AI Agent Service:**
- Azure सदस्यता आवश्यक
- उत्पादनासाठी तयार वैशिष्ट्ये
- फाइल नमुना: `*-azureaiagent.ipynb`

## चाचणी सूचना

हे शैक्षणिक रिपॉझिटरी आहे ज्यामध्ये उदाहरण कोड आहे, उत्पादन कोडसह स्वयंचलित चाचण्या नाहीत. तुमची सेटअप आणि बदल सत्यापित करण्यासाठी:

### मॅन्युअल चाचणी

1. **Python वातावरणाची चाचणी करा:**
   ```bash
   python --version  # Should be 3.12+
   pip list | grep -E "(autogen|semantic-kernel|azure-ai)"
   ```

2. **नोटबुक कार्यान्वयनाची चाचणी करा:**
   ```bash
   # Convert notebook to script and run (tests imports)
   jupyter nbconvert --to script <lesson-folder>/code_samples/<notebook>.ipynb --stdout | python
   ```

3. **पर्यावरणीय व्हेरिएबल्स सत्यापित करा:**
   ```bash
   python -c "import os; from dotenv import load_dotenv; load_dotenv(); print('✓ GITHUB_TOKEN' if os.getenv('GITHUB_TOKEN') else '✗ GITHUB_TOKEN missing')"
   ```


### वैयक्तिक नोटबुक चालवणे

Jupyter मध्ये नोटबुक उघडा आणि अनुक्रमे सेल्स कार्यान्वित करा. प्रत्येक नोटबुक स्वतंत्र आहे आणि यामध्ये समाविष्ट आहे:
- आयात स्टेटमेंट्स
- कॉन्फिगरेशन लोडिंग
- उदाहरण एजंट अंमलबजावणी
- अपेक्षित आउटपुट्स markdown सेल्समध्ये

## कोड शैली

### Python परंपरा

- **Python आवृत्ती**: 3.12+
- **कोड शैली**: मानक Python PEP 8 परंपरा पाळा
- **नोटबुक्स**: संकल्पना स्पष्ट करण्यासाठी स्पष्ट markdown सेल्स वापरा
- **आयात**: मानक लायब्ररी, तृतीय-पक्ष, स्थानिक आयातानुसार गट करा

### Jupyter Notebook परंपरा

- कोड सेल्सच्या आधी वर्णनात्मक markdown सेल्स समाविष्ट करा
- संदर्भासाठी नोटबुक्समध्ये आउटपुट उदाहरणे जोडा
- धडाच्या संकल्पनांशी जुळणारी स्पष्ट व्हेरिएबल नावे वापरा
- नोटबुक कार्यान्वयन क्रम रेखीय ठेवा (सेल 1 → 2 → 3...)

### फाइल संघटना

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


## बांधणी आणि तैनाती

### दस्तऐवज तयार करणे

हे रिपॉझिटरी Markdown वापरते:
- प्रत्येक धडाच्या फोल्डरमध्ये README.md फाइल्स
- रिपॉझिटरीच्या मूळ ठिकाणी मुख्य README.md
- GitHub Actions द्वारे स्वयंचलित भाषांतर प्रणाली

### CI/CD पाइपलाइन

`.github/workflows/` मध्ये स्थित:

1. **co-op-translator.yml** - 50+ भाषांमध्ये स्वयंचलित भाषांतर
2. **welcome-issue.yml** - नवीन समस्या निर्मात्यांचे स्वागत करते
3. **welcome-pr.yml** - नवीन पुल विनंती योगदानकर्त्यांचे स्वागत करते

### तैनाती

हे शैक्षणिक रिपॉझिटरी आहे - कोणतीही तैनाती प्रक्रिया नाही. वापरकर्ते:
1. रिपॉझिटरी फोर्क किंवा क्लोन करा
2. नोटबुक्स स्थानिकपणे किंवा GitHub Codespaces मध्ये चालवा
3. उदाहरणे बदलून आणि प्रयोग करून शिका

## पुल विनंती मार्गदर्शक तत्त्वे

### सबमिट करण्यापूर्वी

1. **तुमचे बदल चाचणी करा:**
   - प्रभावित नोटबुक्स पूर्णपणे चालवा
   - सर्व सेल्स त्रुटीशिवाय कार्यान्वित होतात याची खात्री करा
   - आउटपुट योग्य आहेत याची तपासणी करा

2. **दस्तऐवज अद्यतन:**
   - नवीन संकल्पना जोडल्यास README.md अद्यतनित करा
   - जटिल कोडसाठी नोटबुक्समध्ये टिप्पण्या जोडा
   - markdown सेल्समध्ये उद्देश स्पष्ट करा

3. **फाइल बदल:**
   - `.env` फाइल्स कमिट करू नका (`.env.example` वापरा)
   - `venv/` किंवा `__pycache__/` डिरेक्टरीज कमिट करू नका
   - संकल्पना दाखवण्यासाठी नोटबुक आउटपुट ठेवा
   - तात्पुरत्या फाइल्स आणि बॅकअप नोटबुक्स (`*-backup.ipynb`) काढा

### PR शीर्षक स्वरूप

वर्णनात्मक शीर्षके वापरा:
- `[Lesson-XX] <संकल्पनेसाठी नवीन उदाहरण जोडा>`
- `[Fix] lesson-XX README मधील टायपो सुधारित करा`
- `[Update] lesson-XX मधील कोड नमुना सुधारित करा`
- `[Docs] सेटअप सूचना अद्यतनित करा`

### आवश्यक तपासण्या

- नोटबुक्स त्रुटीशिवाय कार्यान्वित होणे आवश्यक आहे
- README फाइल्स स्पष्ट आणि अचूक असाव्यात
- रिपॉझिटरीमधील विद्यमान कोड नमुन्यांचे अनुसरण करा
- इतर धडांशी सुसंगतता राखा

## अतिरिक्त टिप्पण्या

### सामान्य अडचणी

1. **Python आवृत्ती विसंगती:**
   - Python 3.12+ वापरला जात आहे याची खात्री करा
   - काही पॅकेजेस जुन्या आवृत्त्यांसह कार्य करत नाहीत
   - Python आवृत्ती स्पष्टपणे निर्दिष्ट करण्यासाठी `python3 -m venv` वापरा

2. **पर्यावरणीय व्हेरिएबल्स:**
   - नेहमी `.env.example` वरून `.env` तयार करा
   - `.env` फाइल कमिट करू नका (ती `.gitignore` मध्ये आहे)
   - GitHub टोकनला योग्य परवानग्या आवश्यक आहेत

3. **पॅकेज संघर्ष:**
   - नवीन व्हर्च्युअल वातावरण वापरा
   - वैयक्तिक पॅकेजेसऐवजी `requirements.txt` मधून स्थापित करा
   - काही नोटबुक्समध्ये त्यांच्या markdown सेल्समध्ये अतिरिक्त पॅकेजेस आवश्यक असू शकतात

4. **Azure सेवांसाठी:**
   - Azure AI सेवांसाठी सक्रिय सदस्यता आवश्यक आहे
   - काही वैशिष्ट्ये प्रदेश-विशिष्ट आहेत
   - GitHub Models साठी फ्री टियर मर्यादा लागू होतात

### शिकण्याचा मार्ग

धडांमधून अनुक्रमे प्रगती करण्याची शिफारस:
1. **00-course-setup** - वातावरण सेटअपसाठी येथे प्रारंभ करा
2. **01-intro-to-ai-agents** - AI एजंट्सची मूलभूत माहिती समजून घ्या
3. **02-explore-agentic-frameworks** - विविध फ्रेमवर्क्सबद्दल शिका
4. **03-agentic-design-patterns** - मुख्य डिझाइन पॅटर्न्स
5. क्रमांकित धडांद्वारे अनुक्रमे पुढे जा

### फ्रेमवर्क निवड

तुमच्या उद्दिष्टांनुसार फ्रेमवर्क निवडा:
- **शिकणे/प्रोटोटायपिंग**: Semantic Kernel + GitHub Models (फ्री)
- **मल्टी-एजंट सिस्टम्स**: AutoGen
- **नवीनतम वैशिष्ट्ये**: Microsoft Agent Framework (MAF)
- **उत्पादन तैनाती**: Azure AI Agent Service

### मदत मिळवणे

- [Azure AI Foundry Community Discord](https://aka.ms/ai-agents/discord) मध्ये सामील व्हा
- विशिष्ट मार्गदर्शनासाठी धड README फाइल्स पुनरावलोकन करा
- कोर्सचा आढावा घेण्यासाठी मुख्य [README.md](./README.md) तपासा
- तपशीलवार सेटअप सूचनांसाठी [Course Setup](./00-course-setup/README.md) पहा

### योगदान

हे एक खुले शैक्षणिक प्रकल्प आहे. योगदान स्वागतार्ह:
- कोड उदाहरणे सुधारित करा
- टायपो किंवा त्रुटी सुधारित करा
- स्पष्ट करणाऱ्या टिप्पण्या जोडा
- नवीन धड विषय सुचवा
- अतिरिक्त भाषांमध्ये भाषांतर करा

[GitHub Issues](https://github.com/microsoft/ai-agents-for-beginners/issues) मध्ये विद्यमान गरजा पहा.

## प्रकल्प-विशिष्ट संदर्भ

### बहुभाषिक समर्थन

हे रिपॉझिटरी स्वयंचलित भाषांतर प्रणाली वापरते:
- 50+ भाषांचे समर्थन
- `/translations/<lang-code>/` डिरेक्टरीजमध्ये भाषांतरे
- GitHub Actions कार्यप्रवाह भाषांतर अद्यतन हाताळतो
- मूळ फाइल्स इंग्रजीमध्ये रिपॉझिटरीच्या मूळ ठिकाणी आहेत

### धड रचना

प्रत्येक धड एकसारखा नमुना अनुसरण करतो:
1. व्हिडिओ थंबनेलसह लिंक
2. लेखी धड सामग्री (README.md)
3. अनेक फ्रेमवर्क्समधील कोड नमुने
4. शिकण्याची उद्दिष्टे आणि पूर्वतयारी
5. अतिरिक्त शिकण्याचे संसाधने लिंक केलेली

### कोड नमुना नामकरण

नमुना: `<lesson-number>-<framework-name>.ipynb`
- `04-semantic-kernel.ipynb` - धडा 4, Semantic Kernel
- `07-autogen.ipynb` - धडा 7, AutoGen
- `14-python-agent-framework.ipynb` - धडा 14, MAF Python
- `14-dotnet-agent-framework.ipynb` - धडा 14, MAF .NET

### विशेष डिरेक्टरीज

- `translated_images/` - भाषांतरांसाठी स्थानिक प्रतिमा
- `images/` - इंग्रजी सामग्रीसाठी मूळ प्रतिमा
- `.devcontainer/` - VS Code विकास कंटेनर कॉन्फिगरेशन
- `.github/` - GitHub Actions कार्यप्रवाह आणि टेम्पलेट्स

### आवश्यकताः

`requirements.txt` मधील मुख्य पॅकेजेस:
- `autogen-agentchat`, `autogen-core`, `autogen-ext` - AutoGen फ्रेमवर्क
- `semantic-kernel` - Semantic Kernel फ्रेमवर्क
- `agent-framework` - Microsoft Agent Framework
- `azure-ai-inference`, `azure-ai-projects` - Azure AI सेवांसाठी
- `azure-search-documents` - Azure AI Search एकत्रीकरण
- `chromadb` - RAG उदाहरणांसाठी व्हेक्टर डेटाबेस
- `chainlit` - चॅट UI फ्रेमवर्क
- `browser_use` - एजंट्ससाठी ब्राउझर ऑटोमेशन
- `mcp[cli]` - मॉडेल कॉन्टेक्स्ट प्रोटोकॉल समर्थन
- `mem0ai` - एजंट्ससाठी मेमरी व्यवस्थापन

---

**अस्वीकरण**:  
हा दस्तऐवज AI भाषांतर सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) वापरून भाषांतरित करण्यात आला आहे. आम्ही अचूकतेसाठी प्रयत्नशील असलो तरी, कृपया लक्षात ठेवा की स्वयंचलित भाषांतरांमध्ये त्रुटी किंवा अचूकतेचा अभाव असू शकतो. मूळ भाषेतील दस्तऐवज हा अधिकृत स्रोत मानला जावा. महत्त्वाच्या माहितीसाठी, व्यावसायिक मानवी भाषांतराची शिफारस केली जाते. या भाषांतराचा वापर करून उद्भवलेल्या कोणत्याही गैरसमज किंवा चुकीच्या अर्थासाठी आम्ही जबाबदार राहणार नाही.