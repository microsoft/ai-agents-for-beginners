# AGENTS.md

## ప్రాజెక్ట్ అవలోకనం

ఈ రిపోజిటరీ "AI Agents for Beginners" - AI ఏజెంట్‌లను నిర్మించడానికి అవసరమైన ప్రతిదీ బోధించే సమగ్ర విద్యా కోర్సును కలిగి ఉంది. కోర్స్ AI ఏజెంట్‌ల ప్రాథమిక విషయాలు, డిజైన్ నమూనాలు, ఫ్రేమ్‌వర్క్‌లు మరియు ఉత్పత్తి విస్తరణను కవర్ చేసే 15+ పాఠాలను కలిగి ఉంది.

**కీ సాంకేతికతలు:**
- Python 3.12+
- ఇంటరాక్టివ్ అభ్యాసం కోసం Jupyter Notebooks
- AI ఫ్రేమ్‌వర్క్‌లు: Semantic Kernel, AutoGen, Microsoft Agent Framework (MAF)
- Azure AI సేవలు: Azure AI Foundry, Azure AI Agent Service
- GitHub Models Marketplace (ఉచిత టైర్ అందుబాటులో ఉంది)

**నిర్మాణం:**
- పాఠం-ఆధారిత నిర్మాణం (00-15+ డైరెక్టరీలు)
- ప్రతి పాఠంలో ఉన్నవి: README డాక్యుమెంటేషన్, కోడ్ నమూనాలు (Jupyter notebooks), మరియు చిత్రాలు
- ఆటోమేటెడ్ అనువాద వ్యవస్థ ద్వారా బహుళ-భాషా మద్దతు
- ప్రతి పాఠానికి బహుళ ఫ్రేమ్‌వర్క్ ఎంపికలు (Semantic Kernel, AutoGen, Azure AI Agent Service)

## సెటప్ ఆదేశాలు

### ముందస్తు అవసరాలు
- Python 3.12 లేదా అంతకంటే ఎక్కువ
- GitHub ఖాతా (GitHub Models కోసం - ఉచిత టైర్)
- Azure సబ్‌స్క్రిప్షన్ (ఐచ్ఛికం, Azure AI సేవల కోసం)

### ప్రారంభ సెటప్

1. **రిపోజిటరీని క్లోన్ లేదా ఫోర్క్ చేయండి:**
   ```bash
   gh repo fork microsoft/ai-agents-for-beginners --clone
   # లేదా
   git clone https://github.com/microsoft/ai-agents-for-beginners.git
   cd ai-agents-for-beginners
   ```

2. **Python వర్చువల్ ఎన్విరాన్‌మెంట్ సృష్టించండి మరియు యాక్టివేట్ చేయండి:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # Windows లో: venv\Scripts\activate
   ```

3. **డిపెండెన్సీలను ఇన్‌స్టాల్ చేయండి:**
   ```bash
   pip install -r requirements.txt
   ```

4. **ఎన్విరాన్‌మెంట్ వేరియబుల్స్ సెటప్ చేయండి:**
   ```bash
   cp .env.example .env
   # మీ API కీలు మరియు ఎండ్‌పాయింట్‌లతో .env ని ఎడిట్ చేయండి
   ```

### అవసరమైన ఎన్విరాన్‌మెంట్ వేరియబుల్స్

**GitHub Models (ఉచితం)** కోసం:
- `GITHUB_TOKEN` - GitHub నుండి వ్యక్తిగత యాక్సెస్ టోకెన్

**Azure AI సేవలు** (ఐచ్ఛికం) కోసం:
- `PROJECT_ENDPOINT` - Azure AI Foundry ప్రాజెక్ట్ ఎండ్‌పాయింట్
- `AZURE_OPENAI_API_KEY` - Azure OpenAI API కీ
- `AZURE_OPENAI_ENDPOINT` - Azure OpenAI ఎండ్‌పాయింట్ URL
- `AZURE_OPENAI_CHAT_DEPLOYMENT_NAME` - చాట్ మోడల్ కోసం డిప్లాయ్‌మెంట్ పేరు
- `AZURE_OPENAI_EMBEDDING_DEPLOYMENT_NAME` - ఎంబెడింగ్స్ కోసం డిప్లాయ్‌మెంట్ పేరు
- `.env.example`లో చూపిన అదనపు Azure కాన్ఫిగరేషన్

## అభివృద్ధి వర్క్‌ఫ్లో

### Jupyter Notebooks అమలు చేయడం

ప్రతి పాఠం వివిధ ఫ్రేమ్‌వర్క్‌ల కోసం బహుళ Jupyter notebooks కలిగి ఉంటుంది:

1. **Jupyter ప్రారంభించండి:**
   ```bash
   jupyter notebook
   ```

2. **పాఠ డైరెక్టరీకి నావిగేట్ చేయండి** (ఉదా., `01-intro-to-ai-agents/code_samples/`)

3. **notebooks తెరిచి అమలు చేయండి:**
   - `*-semantic-kernel.ipynb` - Semantic Kernel ఫ్రేమ్‌వర్క్ ఉపయోగించడం
   - `*-autogen.ipynb` - AutoGen ఫ్రేమ్‌వర్క్ ఉపయోగించడం
   - `*-python-agent-framework.ipynb` - Microsoft Agent Framework (Python) ఉపయోగించడం
   - `*-dotnet-agent-framework.ipynb` - Microsoft Agent Framework (.NET) ఉపయోగించడం
   - `*-azureaiagent.ipynb` - Azure AI Agent Service ఉపయోగించడం

## టెస్టింగ్ సూచనలు

ఇది ఉత్పత్తి కోడ్ కంటే ఉదాహరణ కోడ్‌తో విద్యా రిపోజిటరీ. మీ సెటప్ మరియు మార్పులను ధృవీకరించడానికి:

### మాన్యువల్ టెస్టింగ్

1. **Python ఎన్విరాన్‌మెంట్ పరీక్షించండి:**
   ```bash
   python --version  # 3.12+ అయి ఉండాలి
   pip list | grep -E "(autogen|semantic-kernel|azure-ai)"
   ```

2. **Notebook అమలును పరీక్షించండి:**
   ```bash
   # Notebook ని స్క్రిప్ట్‌గా మార్చండి మరియు అమలు చేయండి (imports పరీక్షించడానికి)
   jupyter nbconvert --to script <notebook-file>.ipynb
   python <notebook-file>.py
   ```

ఈ కోర్స్ గురించి మరింత సమాచారం కోసం, [Course Setup](../../00-course-setup/README.md)ని చూడండి.