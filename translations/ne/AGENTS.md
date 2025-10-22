<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a5f54aa3f419865e5d58bcfddb1d3198",
  "translation_date": "2025-10-03T15:34:55+00:00",
  "source_file": "AGENTS.md",
  "language_code": "ne"
}
-->
# AGENTS.md

## परियोजना अवलोकन

यो रिपोजिटरी "AI Agents for Beginners" समावेश गर्दछ - एक व्यापक शैक्षिक पाठ्यक्रम जसले AI एजेन्ट निर्माण गर्न आवश्यक सबै कुरा सिकाउँछ। पाठ्यक्रममा १५+ पाठहरू समावेश छन् जसले आधारभूत कुराहरू, डिजाइन ढाँचाहरू, फ्रेमवर्कहरू, र AI एजेन्टहरूको उत्पादन परिनियोजनलाई समेट्छ।

**मुख्य प्रविधिहरू:**
- Python 3.12+
- अन्तरक्रियात्मक सिकाइका लागि Jupyter Notebooks
- AI फ्रेमवर्कहरू: Semantic Kernel, AutoGen, Microsoft Agent Framework (MAF)
- Azure AI सेवाहरू: Azure AI Foundry, Azure AI Agent Service
- GitHub Models Marketplace (निःशुल्क स्तर उपलब्ध)

**आर्किटेक्चर:**
- पाठ-आधारित संरचना (00-15+ निर्देशिकाहरू)
- प्रत्येक पाठमा समावेश: README दस्तावेज, कोड नमूनाहरू (Jupyter notebooks), र छविहरू
- स्वचालित अनुवाद प्रणाली मार्फत बहुभाषी समर्थन
- प्रत्येक पाठमा बहु फ्रेमवर्क विकल्पहरू (Semantic Kernel, AutoGen, Azure AI Agent Service)

## सेटअप आदेशहरू

### आवश्यकताहरू
- Python 3.12 वा उच्च संस्करण
- GitHub खाता (GitHub Models - निःशुल्क स्तरको लागि)
- Azure सदस्यता (वैकल्पिक, Azure AI सेवाहरूको लागि)

### प्रारम्भिक सेटअप

1. **रिपोजिटरी क्लोन वा फोर्क गर्नुहोस्:**
   ```bash
   gh repo fork microsoft/ai-agents-for-beginners --clone
   # OR
   git clone https://github.com/microsoft/ai-agents-for-beginners.git
   cd ai-agents-for-beginners
   ```

2. **Python भर्चुअल वातावरण सिर्जना र सक्रिय गर्नुहोस्:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **आवश्यकताहरू स्थापना गर्नुहोस्:**
   ```bash
   pip install -r requirements.txt
   ```

4. **पर्यावरण चरहरू सेटअप गर्नुहोस्:**
   ```bash
   cp .env.example .env
   # Edit .env with your API keys and endpoints
   ```


### आवश्यक पर्यावरण चरहरू

**GitHub Models (निःशुल्क)** को लागि:
- `GITHUB_TOKEN` - GitHub बाट व्यक्तिगत पहुँच टोकन

**Azure AI सेवाहरू** (वैकल्पिक) को लागि:
- `PROJECT_ENDPOINT` - Azure AI Foundry परियोजना अन्त बिन्दु
- `AZURE_OPENAI_API_KEY` - Azure OpenAI API कुञ्जी
- `AZURE_OPENAI_ENDPOINT` - Azure OpenAI अन्त बिन्दु URL
- `AZURE_OPENAI_CHAT_DEPLOYMENT_NAME` - च्याट मोडेलको लागि परिनियोजन नाम
- `AZURE_OPENAI_EMBEDDING_DEPLOYMENT_NAME` - एम्बेडिङको लागि परिनियोजन नाम
- `.env.example` मा देखाइएको थप Azure कन्फिगरेसन

## विकास कार्यप्रवाह

### Jupyter Notebooks चलाउनुहोस्

प्रत्येक पाठमा विभिन्न फ्रेमवर्कहरूको लागि धेरै Jupyter notebooks समावेश छन्:

1. **Jupyter सुरु गर्नुहोस्:**
   ```bash
   jupyter notebook
   ```

2. **पाठ निर्देशिकामा जानुहोस्** (जस्तै, `01-intro-to-ai-agents/code_samples/`)

3. **नोटबुकहरू खोल्नुहोस् र चलाउनुहोस्:**
   - `*-semantic-kernel.ipynb` - Semantic Kernel फ्रेमवर्क प्रयोग गर्दै
   - `*-autogen.ipynb` - AutoGen फ्रेमवर्क प्रयोग गर्दै
   - `*-python-agent-framework.ipynb` - Microsoft Agent Framework (Python) प्रयोग गर्दै
   - `*-dotnet-agent-framework.ipynb` - Microsoft Agent Framework (.NET) प्रयोग गर्दै
   - `*-azureaiagent.ipynb` - Azure AI Agent Service प्रयोग गर्दै

### विभिन्न फ्रेमवर्कहरूसँग काम गर्नुहोस्

**Semantic Kernel + GitHub Models:**
- GitHub खाता संग निःशुल्क स्तर उपलब्ध
- सिकाइ र प्रयोगको लागि राम्रो
- फाइल ढाँचा: `*-semantic-kernel*.ipynb`

**AutoGen + GitHub Models:**
- GitHub खाता संग निःशुल्क स्तर उपलब्ध
- बहु-एजेन्ट समन्वय क्षमताहरू
- फाइल ढाँचा: `*-autogen.ipynb`

**Microsoft Agent Framework (MAF):**
- Microsoft बाट नवीनतम फ्रेमवर्क
- Python र .NET मा उपलब्ध
- फाइल ढाँचा: `*-agent-framework.ipynb`

**Azure AI Agent Service:**
- Azure सदस्यता आवश्यक
- उत्पादन-तयार सुविधाहरू
- फाइल ढाँचा: `*-azureaiagent.ipynb`

## परीक्षण निर्देशनहरू

यो शैक्षिक रिपोजिटरी हो जसमा उदाहरण कोड समावेश छ, उत्पादन कोडमा स्वचालित परीक्षणहरू छैनन्। आफ्नो सेटअप र परिवर्तनहरू प्रमाणित गर्न:

### म्यानुअल परीक्षण

1. **Python वातावरण परीक्षण गर्नुहोस्:**
   ```bash
   python --version  # Should be 3.12+
   pip list | grep -E "(autogen|semantic-kernel|azure-ai)"
   ```

2. **नोटबुक कार्यान्वयन परीक्षण गर्नुहोस्:**
   ```bash
   # Convert notebook to script and run (tests imports)
   jupyter nbconvert --to script <lesson-folder>/code_samples/<notebook>.ipynb --stdout | python
   ```

3. **पर्यावरण चरहरू प्रमाणित गर्नुहोस्:**
   ```bash
   python -c "import os; from dotenv import load_dotenv; load_dotenv(); print('✓ GITHUB_TOKEN' if os.getenv('GITHUB_TOKEN') else '✗ GITHUB_TOKEN missing')"
   ```


### व्यक्तिगत नोटबुकहरू चलाउनुहोस्

Jupyter मा नोटबुकहरू खोल्नुहोस् र कोशहरू क्रमिक रूपमा कार्यान्वयन गर्नुहोस्। प्रत्येक नोटबुक आत्म-समावेशी छ र समावेश गर्दछ:
- आयात कथनहरू
- कन्फिगरेसन लोड गर्दै
- उदाहरण एजेन्ट कार्यान्वयनहरू
- अपेक्षित आउटपुटहरू markdown कोशहरूमा

## कोड शैली

### Python परम्पराहरू

- **Python संस्करण**: 3.12+
- **कोड शैली**: मानक Python PEP 8 परम्पराहरू अनुसरण गर्नुहोस्
- **नोटबुकहरू**: अवधारणाहरू स्पष्ट गर्न markdown कोशहरू प्रयोग गर्नुहोस्
- **आयातहरू**: मानक पुस्तकालय, तेस्रो-पक्ष, स्थानीय आयातहरूद्वारा समूह गर्नुहोस्

### Jupyter Notebook परम्पराहरू

- कोड कोशहरू अघि वर्णनात्मक markdown कोशहरू समावेश गर्नुहोस्
- सन्दर्भको लागि नोटबुकहरूमा आउटपुट उदाहरणहरू थप्नुहोस्
- पाठ अवधारणाहरू मिल्ने स्पष्ट भेरिएबल नामहरू प्रयोग गर्नुहोस्
- नोटबुक कार्यान्वयन क्रम रेखीय राख्नुहोस् (कोश 1 → 2 → 3...)

### फाइल संगठन

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


## निर्माण र परिनियोजन

### दस्तावेज निर्माण

यो रिपोजिटरीले दस्तावेजको लागि Markdown प्रयोग गर्दछ:
- प्रत्येक पाठ फोल्डरमा README.md फाइलहरू
- रिपोजिटरीको मूलमा मुख्य README.md
- GitHub Actions मार्फत स्वचालित अनुवाद प्रणाली

### CI/CD पाइपलाइन

`.github/workflows/` मा अवस्थित:

1. **co-op-translator.yml** - ५०+ भाषामा स्वचालित अनुवाद
2. **welcome-issue.yml** - नयाँ मुद्दा सिर्जनाकर्ताहरूलाई स्वागत गर्दछ
3. **welcome-pr.yml** - नयाँ पुल अनुरोध योगदानकर्ताहरूलाई स्वागत गर्दछ

### परिनियोजन

यो शैक्षिक रिपोजिटरी हो - कुनै परिनियोजन प्रक्रिया छैन। प्रयोगकर्ताहरू:
1. रिपोजिटरी फोर्क वा क्लोन गर्नुहोस्
2. नोटबुकहरू स्थानीय रूपमा वा GitHub Codespaces मा चलाउनुहोस्
3. उदाहरणहरू संशोधन र प्रयोग गरेर सिक्नुहोस्

## पुल अनुरोध दिशानिर्देश

### पेश गर्नु अघि

1. **आफ्नो परिवर्तनहरू परीक्षण गर्नुहोस्:**
   - प्रभावित नोटबुकहरू पूर्ण रूपमा चलाउनुहोस्
   - सुनिश्चित गर्नुहोस् कि सबै कोशहरू त्रुटि बिना कार्यान्वित हुन्छन्
   - आउटपुटहरू उपयुक्त छन् भनी जाँच गर्नुहोस्

2. **दस्तावेज अपडेटहरू:**
   - नयाँ अवधारणाहरू थप्दा README.md अपडेट गर्नुहोस्
   - जटिल कोडको लागि नोटबुकहरूमा टिप्पणीहरू थप्नुहोस्
   - markdown कोशहरूले उद्देश्य स्पष्ट पार्छन् भनी सुनिश्चित गर्नुहोस्

3. **फाइल परिवर्तनहरू:**
   - `.env` फाइलहरू प्रतिबद्ध नगर्नुहोस् (`.env.example` प्रयोग गर्नुहोस्)
   - `venv/` वा `__pycache__/` निर्देशिकाहरू प्रतिबद्ध नगर्नुहोस्
   - अवधारणाहरू प्रदर्शन गर्दा नोटबुक आउटपुटहरू राख्नुहोस्
   - अस्थायी फाइलहरू र ब्याकअप नोटबुकहरू (`*-backup.ipynb`) हटाउनुहोस्

### PR शीर्षक ढाँचा

वर्णनात्मक शीर्षकहरू प्रयोग गर्नुहोस्:
- `[Lesson-XX] <अवधारणा> को लागि नयाँ उदाहरण थप्नुहोस्`
- `[Fix] पाठ-XX README मा टाइपो सुधार गर्नुहोस्`
- `[Update] पाठ-XX मा कोड नमूना सुधार गर्नुहोस्`
- `[Docs] सेटअप निर्देशनहरू अपडेट गर्नुहोस्`

### आवश्यक जाँचहरू

- नोटबुकहरू त्रुटि बिना कार्यान्वित हुनुपर्छ
- README फाइलहरू स्पष्ट र सटीक हुनुपर्छ
- रिपोजिटरीमा अवस्थित कोड ढाँचाहरू अनुसरण गर्नुहोस्
- अन्य पाठहरूसँग स्थिरता कायम गर्नुहोस्

## थप नोटहरू

### सामान्य समस्याहरू

1. **Python संस्करण असंगति:**
   - Python 3.12+ प्रयोग गर्नुहोस् भनी सुनिश्चित गर्नुहोस्
   - केही प्याकेजहरू पुराना संस्करणहरूसँग काम नगर्न सक्छन्
   - Python संस्करण स्पष्ट रूपमा निर्दिष्ट गर्न `python3 -m venv` प्रयोग गर्नुहोस्

2. **पर्यावरण चरहरू:**
   - सधैं `.env.example` बाट `.env` सिर्जना गर्नुहोस्
   - `.env` फाइल प्रतिबद्ध नगर्नुहोस् (यो `.gitignore` मा छ)
   - GitHub टोकनलाई उपयुक्त अनुमति आवश्यक छ

3. **प्याकेज असंगति:**
   - नयाँ भर्चुअल वातावरण प्रयोग गर्नुहोस्
   - व्यक्तिगत प्याकेजहरू भन्दा `requirements.txt` बाट स्थापना गर्नुहोस्
   - केही नोटबुकहरूले markdown कोशहरूमा उल्लेख गरिएका थप प्याकेजहरू आवश्यक हुन सक्छ

4. **Azure सेवाहरू:**
   - Azure AI सेवाहरू सक्रिय सदस्यता आवश्यक छ
   - केही सुविधाहरू क्षेत्र-विशिष्ट छन्
   - GitHub Models को निःशुल्क स्तर सीमाहरू लागू हुन्छन्

### सिकाइ मार्ग

पाठहरू मार्फत अनुशंसित प्रगति:
1. **00-course-setup** - वातावरण सेटअपको लागि यहाँ सुरु गर्नुहोस्
2. **01-intro-to-ai-agents** - AI एजेन्टको आधारभूत कुरा बुझ्नुहोस्
3. **02-explore-agentic-frameworks** - विभिन्न फ्रेमवर्कहरूको बारेमा जान्नुहोस्
4. **03-agentic-design-patterns** - कोर डिजाइन ढाँचाहरू
5. क्रमबद्ध पाठहरू क्रमिक रूपमा जारी राख्नुहोस्

### फ्रेमवर्क चयन

आफ्नो लक्ष्यको आधारमा फ्रेमवर्क चयन गर्नुहोस्:
- **सिकाइ/प्रोटोटाइपिङ**: Semantic Kernel + GitHub Models (निःशुल्क)
- **बहु-एजेन्ट प्रणालीहरू**: AutoGen
- **नवीनतम सुविधाहरू**: Microsoft Agent Framework (MAF)
- **उत्पादन परिनियोजन**: Azure AI Agent Service

### सहयोग प्राप्त गर्नुहोस्

- [Azure AI Foundry Community Discord](https://aka.ms/ai-agents/discord) मा सामेल हुनुहोस्
- विशिष्ट मार्गदर्शनको लागि पाठ README फाइलहरू समीक्षा गर्नुहोस्
- मुख्य [README.md](./README.md) मा पाठ्यक्रम अवलोकन जाँच गर्नुहोस्
- विस्तृत सेटअप निर्देशनहरूको लागि [Course Setup](./00-course-setup/README.md) हेर्नुहोस्

### योगदान

यो एक खुला शैक्षिक परियोजना हो। योगदान स्वागत छ:
- कोड उदाहरणहरू सुधार गर्नुहोस्
- टाइपो वा त्रुटिहरू सुधार गर्नुहोस्
- स्पष्ट टिप्पणीहरू थप्नुहोस्
- नयाँ पाठ विषयहरू सुझाव गर्नुहोस्
- थप भाषाहरूमा अनुवाद गर्नुहोस्

[GitHub Issues](https://github.com/microsoft/ai-agents-for-beginners/issues) मा वर्तमान आवश्यकताहरू हेर्नुहोस्।

## परियोजना-विशिष्ट सन्दर्भ

### बहुभाषी समर्थन

यो रिपोजिटरीले स्वचालित अनुवाद प्रणाली प्रयोग गर्दछ:
- ५०+ भाषाहरू समर्थित
- अनुवादहरू `/translations/<lang-code>/` निर्देशिकाहरूमा
- GitHub Actions कार्यप्रवाहले अनुवाद अपडेटहरू ह्यान्डल गर्दछ
- स्रोत फाइलहरू रिपोजिटरीको मूलमा अंग्रेजीमा छन्

### पाठ संरचना

प्रत्येक पाठले एक सुसंगत ढाँचा अनुसरण गर्दछ:
1. भिडियो थम्बनेल लिंक सहित
2. लिखित पाठ सामग्री (README.md)
3. विभिन्न फ्रेमवर्कहरूमा कोड नमूनाहरू
4. सिकाइ उद्देश्यहरू र आवश्यकताहरू
5. अतिरिक्त सिकाइ स्रोतहरू लिंक गरिएको

### कोड नमूना नामकरण

ढाँचा: `<lesson-number>-<framework-name>.ipynb`
- `04-semantic-kernel.ipynb` - पाठ ४, Semantic Kernel
- `07-autogen.ipynb` - पाठ ७, AutoGen
- `14-python-agent-framework.ipynb` - पाठ १४, MAF Python
- `14-dotnet-agent-framework.ipynb` - पाठ १४, MAF .NET

### विशेष निर्देशिकाहरू

- `translated_images/` - अनुवादहरूको लागि स्थानीयकृत छविहरू
- `images/` - अंग्रेजी सामग्रीको लागि मूल छविहरू
- `.devcontainer/` - VS Code विकास कन्टेनर कन्फिगरेसन
- `.github/` - GitHub Actions कार्यप्रवाहहरू र टेम्पलेटहरू

### निर्भरताहरू

`requirements.txt` बाट मुख्य प्याकेजहरू:
- `autogen-agentchat`, `autogen-core`, `autogen-ext` - AutoGen फ्रेमवर्क
- `semantic-kernel` - Semantic Kernel फ्रेमवर्क
- `agent-framework` - Microsoft Agent Framework
- `azure-ai-inference`, `azure-ai-projects` - Azure AI सेवाहरू
- `azure-search-documents` - Azure AI Search एकीकरण
- `chromadb` - RAG उदाहरणहरूको लागि भेक्टर डाटाबेस
- `chainlit` - च्याट UI फ्रेमवर्क
- `browser_use` - एजेन्टहरूको लागि ब्राउजर स्वचालन
- `mcp[cli]` - मोडेल सन्दर्भ प्रोटोकल समर्थन
- `mem0ai` - एजेन्टहरूको लागि मेमोरी व्यवस्थापन

---

**अस्वीकरण**:  
यो दस्तावेज़ AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) प्रयोग गरेर अनुवाद गरिएको हो। हामी यथासम्भव शुद्धता सुनिश्चित गर्न प्रयास गर्छौं, तर कृपया ध्यान दिनुहोस् कि स्वचालित अनुवादमा त्रुटिहरू वा अशुद्धताहरू हुन सक्छ। मूल दस्तावेजलाई यसको मातृभाषामा आधिकारिक स्रोत मानिनुपर्छ। महत्वपूर्ण जानकारीको लागि, व्यावसायिक मानव अनुवाद सिफारिस गरिन्छ। यस अनुवादको प्रयोगबाट उत्पन्न हुने कुनै पनि गलतफहमी वा गलत व्याख्याको लागि हामी जिम्मेवार हुने छैनौं।