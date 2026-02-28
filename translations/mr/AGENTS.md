# AGENTS.md

## प्रकल्पाचा आढावा

हा रेपॉझिटरी "AI Agents for Beginners" याचा समावेश करतो - AI एजंट्स तयार करण्यासाठी आवश्यक सर्वकाही शिकवणारे एक व्यापक शैक्षणिक कोर्स. हा कोर्स मूलभूत गोष्टी, डिझाइन पॅटर्न, फ्रेमवर्क आणि AI एजंट्सच्या उत्पादनात तैनात करण्याचा समावेश करणार्‍या 15+ धडांचा समावेश करतो.

**मुख्य तंत्रज्ञान:**
- Python 3.12+
- इंटरएक्टिव्ह शिक्षणासाठी Jupyter Notebooks
- AI Frameworks: Microsoft Agent Framework (MAF)
- Azure AI Services: Microsoft Foundry, Azure AI Foundry Agent Service V2

**आर्किटेक्चर:**
- धडा-आधारित संरचना (00-15+ निर्देशिका)
- प्रत्येक धड्यात असते: README दस्तऐवजीकरण, कोड उदाहरणे (Jupyter notebooks), आणि प्रतिमा
- स्वयंचलित अनुवाद प्रणालीद्वारे बहुभाषिक समर्थन
- प्रत्येक धड्यासाठी एक Python नोटबुक Microsoft Agent Framework वापरून

## सेटअप कमांड

### पूर्वअटी
- Python 3.12 किंवा त्याहून वर
- Azure subscription (Azure AI Foundry साठी)
- Azure CLI इन्स्टॉल केलेले आणि प्रमाणीकृत (`az login`)

### प्रारंभिक सेटअप

1. **रेपॉझिटरी क्लोन किंवा फोर्क करा:**
   ```bash
   gh repo fork microsoft/ai-agents-for-beginners --clone
   # किंवा
   git clone https://github.com/microsoft/ai-agents-for-beginners.git
   cd ai-agents-for-beginners
   ```

2. **Python वर्च्युअल इन्स्टन्स तयार करा आणि सक्रिय करा:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # Windows वर: venv\Scripts\activate
   ```

3. **आवश्यक पॅकेजेस इंस्टॉल करा:**
   ```bash
   pip install -r requirements.txt
   ```

4. **पर्यावरण वेरिएबल सेट करा:**
   ```bash
   cp .env.example .env
   # .env मध्ये आपली API की आणि एंडपॉइंट्स संपादित करा
   ```

### आवश्यक पर्यावरण वेरिएबल

For **Azure AI Foundry** (Required):
- `AZURE_AI_PROJECT_ENDPOINT` - Azure AI Foundry project endpoint
- `AZURE_AI_MODEL_DEPLOYMENT_NAME` - Model deployment name (e.g., gpt-4o)

For **Azure AI Search** (Lesson 05 - RAG):
- `AZURE_SEARCH_SERVICE_ENDPOINT` - Azure AI Search endpoint
- `AZURE_SEARCH_API_KEY` - Azure AI Search API key

प्रमाणीकरण: नोटबुक चालवण्यापूर्वी `az login` चालवा (हे `AzureCliCredential` वापरते).

## विकास कार्यप्रवाह

### Jupyter नोटबुक चालवणे

प्रत्येक धड्यात विविध फ्रेमवर्कसाठी अनेक Jupyter नोटबुक्स असतात:

1. **Jupyter सुरू करा:**
   ```bash
   jupyter notebook
   ```

2. **धडा निर्देशिकेत जा** (उदा., `01-intro-to-ai-agents/code_samples/`)

3. **नोटबुक उघडा आणि चालवा:**
   - `*-python-agent-framework.ipynb` - Microsoft Agent Framework (Python) वापरून
   - `*-dotnet-agent-framework.ipynb` - Microsoft Agent Framework (.NET) वापरून

### Microsoft Agent Framework सह काम करणे

**Microsoft Agent Framework + Azure AI Foundry:**
- Azure सदस्यत्व आवश्यक आहे
- Agent Service V2 साठी `AzureAIProjectAgentProvider` वापरते (Foundry पोर्टलमध्ये एजंट दिसतात)
- बिल्ट-इन वेधक्षमता (observability) सह उत्पादन-तयार
- फाइल नमुना: `*-python-agent-framework.ipynb`

## चाचणी सूचना

हे एक शैक्षणिक रेपॉझिटरी आहे ज्यात उत्पादन-स्तराचे स्वयंचलित चाचणी कोड नाहीत, परंतु उदाहरणात्मक कोड आहे. आपले सेटअप आणि बदल सत्यापित करण्यासाठी:

### मॅन्युअल चाचणी

1. **Python वातावरण तपासा:**
   ```bash
   python --version  # 3.12+ असले पाहिजे
   pip list | grep -E "(agent-framework|azure-ai|azure-identity)"
   ```

2. **नोटबुक एक्सिक्युशन तपासा:**
   ```bash
   # नोटबुक स्क्रिप्टमध्ये रूपांतर करा आणि चालवा (इम्पोर्ट्सची चाचणी)
   jupyter nbconvert --to script <lesson-folder>/code_samples/<notebook>.ipynb --stdout | python
   ```

3. **पर्यावरण व्हेरिएबल तपासा:**
   ```bash
   python -c "import os; from dotenv import load_dotenv; load_dotenv(); print('✓ GITHUB_TOKEN' if os.getenv('GITHUB_TOKEN') else '✗ GITHUB_TOKEN missing')"
   ```

### स्वतंत्र नोटबुक चालवणे

Jupyter मध्ये नोटबुक उघडा आणि सेल्स क्रमाने चालवा. प्रत्येक नोटबुक स्वयंपूर्ण असतो आणि यात समाविष्ट असते:
- इम्पोर्ट स्टेटमेंट्स
- कॉन्फिगरेशन लोड करणे
- उदाहरण एजंट अंमलबजावण्या
- markdown सेल्समधील अपेक्षित आउटपुट

## कोड शैली

### Python नियम

- **Python आवृत्ती**: 3.12+
- **कोड शैली**: मानक Python PEP 8 कन्व्हेन्शन्सचे पालन करा
- **नोटबुक्स**: संकल्पना समजावण्यासाठी स्पष्ट markdown सेल्स वापरा
- **इम्पोर्ट्स**: स्टँडर्ड लायब्ररी, तृतीय-पक्ष, स्थानिक इम्पोर्ट्स नुसार गटबद्ध करा

### Jupyter नोटबुक पद्धती

- कोड सेल्सपूर्वी वर्णनात्मक markdown सेल्स समाविष्ट करा
- संदर्भासाठी नोटबुक्समध्ये आउटपुट उदाहरणे जोडा
- धडा संकल्पनांना जुळणारी स्पष्ट व्हेरिएबल नावे वापरा
- नोटबुकचा एक्झिक्युशन क्रम रेषीय ठेवा (सेल 1 → 2 → 3...)

### फाइल संघटन

```
<lesson-number>-<lesson-name>/
├── README.md                     # Lesson documentation
├── code_samples/
│   ├── <number>-python-agent-framework.ipynb
│   └── <number>-dotnet-agent-framework.ipynb  (optional)
└── images/
    └── *.png
```

## बिल्ड आणि डिप्लॉयमेंट

### दस्तऐवजीकरण तयार करणे

हे रेपॉझिटरी दस्तऐवजीकरणासाठी Markdown वापरते:
- प्रत्येक धडा फोल्डरमध्ये README.md फाइल्स
- रेपॉझिटरी रूटवर मुख्य README.md
- GitHub Actions द्वारे स्वयंचलित अनुवाद प्रणाली

### CI/CD पाइपलाइन

ठिकाण: `.github/workflows/`:

1. **co-op-translator.yml** - 50+ भाषांमध्ये स्वयंचलित अनुवाद
2. **welcome-issue.yml** - नवीन इश्यू निर्मात्यांचे स्वागत करते
3. **welcome-pr.yml** - नवीन पुल रिक्वेस्ट योगदानकर्त्यांचे स्वागत करते

### डिप्लॉयमेंट

हे एक शैक्षणिक रेपॉझिटरी आहे - कोणतीही डिप्लॉयमेंट प्रक्रिया नाही. वापरकर्ते:
1. रेपॉझिटरी फोर्क किंवा क्लोन करा
2. नोटबुक स्थानिकपणे किंवा GitHub Codespaces मध्ये चालवा
3. उदाहरणे बदलून आणि प्रयोग करून शिका

## पुल रिक्वेस्ट मार्गदर्शक तत्त्वे

### सबमिट करण्यापूर्वी

1. **आपले बदल चाचणी करा:**
   - प्रभावित नोटबुक पूर्णपणे चालवा
   - सर्व सेल्स त्रुटीशिवाय चालत असल्याची खात्री करा
   - आउटपुट योग्य आहेत का ते तपासा

2. **दस्तऐवजीकरण अद्यतने:**
   - नवीन संकल्पना जोडत असाल तर README.md अद्यतनित करा
   - क्लिष्ट कोडसाठी नोटबुकमध्ये टिप्पणी जोडा
   - markdown सेल्स उद्देश समजावून देतात याची खात्री करा

3. **फाइल बदल:**
   - `.env` फाइल्स कमिट करण्याचे टाळा ( `.env.example` वापरा)
   - `venv/` किंवा `__pycache__/` निर्देशिका कमिट करू नका
   - संकल्पना दाखवणाऱ्या नोटबुक आउटपुट ठेवा
   - तात्पुरत्या फाइल्स आणि बॅकअप नोटबुक (`*-backup.ipynb`) काढा

### PR Title Format

वर्णनात्मक शीर्षके वापरा:
- `[Lesson-XX] Add new example for <concept>`
- `[Fix] Correct typo in lesson-XX README`
- `[Update] Improve code sample in lesson-XX`
- `[Docs] Update setup instructions`

### आवश्यक तपासण्या

- नोटबुक्स त्रुटीशिवाय चालाव्यात
- README फाईल्स स्पष्ट आणि अचूक असाव्यात
- रेपॉझिटरीमधील विद्यमान कोड पॅटर्नचे पालन करा
- इतर धडांशी सुसंगतता राखा

## अतिरिक्त सूचना

### सामान्य समस्या

1. **Python आवृत्ती जुळत नाही:**
   - Python 3.12+ वापरण्याची खात्री करा
   - काही पॅकेजेस जुन्या आवृत्त्यांवर काम करणार नाहीत
   - Python आवृत्ती स्पष्ट करण्यासाठी `python3 -m venv` वापरा

2. **पर्यावरण व्हेरिएबल्स:**
   - नेहमी `.env.example` वरून `.env` तयार करा
   - `.env` फाईल कमिट करू नका (`.gitignore` मध्ये आहे)
   - GitHub टोकनला योग्य परवानग्या आवश्यक आहेत

3. **पॅकेज संघर्ष:**
   - नवीन वर्च्युअल एन्व्हायर्नमेंट वापरा
   - स्वतंत्र पॅकेजेस ऐवजी `requirements.txt` मधून इन्स्टॉल करा
   - काही नोटबुकला त्यांच्या markdown सेल्समध्ये नमूद अतिरिक्त पॅकेजेस लागतील

4. **Azure सेवांशी संबंधित:**
   - Azure AI सेवा सक्रिय सदस्यत्व आवश्यक आहे
   - काही वैशिष्ट्ये विशिष्ट प्रदेशांसाठी असतात
   - GitHub Models साठी मोफत टियर मर्यादा लागू होतात

### शिक्षण मार्ग

शिफारस केलेली प्रगती क्रमाने धडे:
1. **00-course-setup** - पर्यावरण सेटअपसाठी येथे प्रारंभ करा
2. **01-intro-to-ai-agents** - AI एजंट्सची मूलभूत समज मिळवा
3. **02-explore-agentic-frameworks** - विविध फ्रेमवर्कबद्दल शिका
4. **03-agentic-design-patterns** - मुख्य डिझाइन पॅटर्न
5. क्रमांकवार धडे सलगपणे पुढे चालवा

### फ्रेमवर्क निवड

आपले उद्दिष्टानुसार फ्रेमवर्क निवडा:
- **All lessons**: Microsoft Agent Framework (MAF) with `AzureAIProjectAgentProvider`
- **Agents register server-side** in Azure AI Foundry Agent Service V2 and are visible in the Foundry portal

### मदत मिळवणे

- या [Microsoft Foundry Community Discord](https://aka.ms/ai-agents/discord) मध्ये सहभागी व्हा
- विशिष्ट मार्गदर्शनासाठी धड्यांचे README फाईल्स तपासा
- कोर्स आढाव्यासाठी मुख्य [README.md](./README.md) तपासा
- सविस्तर सेटअप सूचनांसाठी [Course Setup](./00-course-setup/README.md) पहा

### योगदान

हे एक खुले शैक्षणिक प्रकल्प आहे. योगदान स्वागत आहे:
- कोड उदाहरणे सुधारित करा
- टायपो किंवा चुका दुरुस्त करा
- स्पष्ट करण्यासाठी टिप्पणी जोडा
- नवीन धडा विषय सुचवा
- अतिरिक्त भाषांमध्ये अनुवाद करा

सध्याच्या गरजांसाठी [GitHub Issues](https://github.com/microsoft/ai-agents-for-beginners/issues) पहा.

## प्रकल्प-विशिष्ट संदर्भ

### बहुभाषिक समर्थन

हे रेपॉझिटरी स्वयंचलित अनुवाद प्रणाली वापरते:
- 50+ भाषांसाठी समर्थन
- अनुवाद `/translations/<lang-code>/` निर्देशिकांमध्ये असतात
- GitHub Actions वर्कफ्लो अनुवाद अद्यतन हाताळते
- स्रोत फाईल्स रेपॉझिटरीच्या रूटवर इंग्रजीत आहेत

### धडा रचना

प्रत्येक धडा सातत्यपूर्ण पॅटर्नचे पालन करतो:
1. लिंकसह व्हिडिओ थंबनेल
2. लेखी धडा सामग्री (README.md)
3. विविध फ्रेमवर्कमधील कोड नमुने
4. शिक्षण उद्दिष्टे आणि पूर्वअटी
5. अतिरिक्त शिक्षण संसाधने लिंक केलेली

### कोड नमुना नामकरण

Format: `<lesson-number>-python-agent-framework.ipynb`
- `01-python-agent-framework.ipynb` - Lesson 1, MAF Python
- `14-sequential.ipynb` - Lesson 14, MAF advanced patterns

### विशेष निर्देशिका

- `translated_images/` - अनुवादांसाठी स्थानिकृत प्रतिमा
- `images/` - इंग्रजी सामग्रीसाठी मूळ प्रतिमा
- `.devcontainer/` - VS Code विकास कंटेनर कॉन्फिगरेशन
- `.github/` - GitHub Actions वर्कफ्लोज़ आणि टेम्पलेट्स

### अवलंबित्व

प्रमुख पॅकेजेस `requirements.txt` मधून:
- `agent-framework` - Microsoft Agent Framework
- `a2a-sdk` - Agent-to-Agent protocol support
- `azure-ai-inference`, `azure-ai-projects` - Azure AI services
- `azure-identity` - Azure authentication (AzureCliCredential)
- `azure-search-documents` - Azure AI Search integration
- `mcp[cli]` - Model Context Protocol support

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
अस्वीकरण:
हा दस्तऐवज AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) वापरून अनुवादित करण्यात आला आहे. आम्ही अचूकतेसाठी प्रयत्न करतो, परंतु कृपया लक्षात ठेवा की स्वयंचलित अनुवादांमध्ये चुका किंवा अचूकतेच्या त्रुटी असू शकतात. मूळ दस्तऐवज त्याच्या मूळ भाषेत अधिकृत स्रोत मानले जावे. महत्त्वाच्या माहितीसाठी व्यावसायिक मानवी अनुवादाची शिफारस केली जाते. या अनुवादाच्या वापरामुळे उद्भवणाऱ्या कोणत्याही गैरसमजांबद्दल किंवा चुकीच्या अर्थलावबद्दल आम्ही जबाबदार नाही.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->