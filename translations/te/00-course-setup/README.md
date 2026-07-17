# కోర్సు సెటప్

## పరిచయం

ఈ పాఠం ఈ కోర్సు యొక్క కోడ్ నమూనాలను ఎలా চালించాలో కవర్ చేస్తుంది.

## ఇతర శిక్షణార్థులతో చేరండి మరియు సహాయం పొందండి

మీ రిపోని క్లోన్ చేసుకోవడానికి ముందే, సెటప్‌కు సహాయం పొందడానికి, కోర్సు గురించి ఏవైనా ప్రశ్నలు అడగడానికి లేదా ఇతర శిక్షణార్థులతో కనెక్ట్ కావడానికి [AI Agents For Beginners Discord channel](https://aka.ms/ai-agents/discord) లో చేరండి.

## ఈ రిపోను క్లోన్ చేయండి లేదా ఫోర్క్ చేయండి

ప్రారంభించడానికి, GitHub రిపాజిటరీని క్లోన్ చేయండి లేదా ఫోర్క్ చేయండి. ఇది మీకు కోర్సు మెటీరియల్ యొక్క మీ స్వంత వెర్షన్ అందిస్తుంది, తద్వారా మీరు కోడ్‌ను నడిపించవచ్చు, పరీక్షించవచ్చు మరియు సవరించవచ్చు!

ఇది <a href="https://github.com/microsoft/ai-agents-for-beginners/fork" target="_blank">ఫోర్క్ చేయడానికి లింక్‌ను క్లిక్ చేయడం ద్వారా చేయవచ్చు</a>

ఇప్పుడు మీరు ఈ కోర్సు యొక్క మీ స్వంత ఫోర్క్ చేసిన వెర్షన్ క్రింది లింకులో కలిగి ఉండాలి:

![Forked Repo](../../../translated_images/te/forked-repo.33f27ca1901baa6a.webp)

### షాలో క్లోన్ (వర్క్‌షాప్ / కోడ్‌స్పేస్‌ల కోసం సిఫార్సు చేయబడింది)

  >పూర్తి రిపాజిటరీ పెద్దవిగా ఉండొచ్చు (~3 GB) మీరు పూర్తి చరిత్ర మరియు అన్ని ఫైళ్ళను డౌన్‌లోడ్ చేస్తే. మీరు వర్క్‌షాప్‌లో మాత్రమె పాల్గొంటున్నట్లయితే లేదా కొద్దిపాటి పాఠాల ఫోల్డర్‌లు మాత్రమే అవసరమైతే, షాలో క్లోన్ (లేదా స్పార్స్ క్లోన్) చరిత్రను తగ్గించడం ద్వారా మరియు/లేదా బ్లాబ్స్ ని తప్పించి ఆ డౌన్‌లోడ్‌ను ఎక్కువగా నివారిస్తుంది.

#### త్వరణ షాలో క్లోన్ — కనిష్ట చరిత్ర, అన్ని ఫైళ్లు

క్రింది కమాండ్లలో `<your-username>` ని మీ ఫోర్క్ URL తో (లేదా మీకు ఇష్టమైతే అప్‌స్ట్రీమ్ URL తో) మార్చండి.

లేటెస్ట్ కమిట్ చరిత్ర మాత్రమే క్లోన్ చేయడానికి (చిన్న డౌన్‌లోడ్):

```bash|powershell
git clone --depth 1 https://github.com/<your-username>/ai-agents-for-beginners.git
```

ఒక నిర్దిష్ట బ్రాంచ్ ని క్లోన్ చేయడానికి:

```bash|powershell
git clone --depth 1 --branch <branch-name> https://github.com/<your-username>/ai-agents-for-beginners.git
```

#### భాగస్వామ్య (స్పార్స్) క్లోన్ — కనిష్ట బ్లాబ్స్ + ఎంచుకున్న ఫోల్డర్‌లు మాత్రమే

ఇది పార్టియల్ క్లోన్ మరియు స్పార్స్-చెక్‌ఔట్‌ను ఉపయోగిస్తుంది (Git 2.25+ అవసరం మరియు పార్టియల్ క్లోన్ మద్దతు ఉన్న ఆధునిక Git కోసం సిఫార్సు చేయబడింది):

```bash|powershell
git clone --depth 1 --filter=blob:none --sparse https://github.com/<your-username>/ai-agents-for-beginners.git
```

రిపో ఫోల్డర్ లోకి వెళ్ళండి:

```bash|powershell
cd ai-agents-for-beginners
```

ఆ తరువాత మీరు కావలసిన ఫోల్డర్లను పేర్కొనండి (క్రింద ఉదాహరణ రెండు ఫోల్డర్లను చూపిస్తుంది):

```bash|powershell
git sparse-checkout set 00-course-setup 01-intro-to-ai-agents
```

క్లోన్ చేసి ఫైళ్లు ధృవీకరించిన తర్వాత, మీరు కేవలం ఫైళ్ళు మాత్రమే కావాలనుకుంటే మరియు స్థలాన్ని విడుదల చేయాలనుకుంటే (గిట్ చరిత్ర లేదు), దయచేసి రిపాజిటరీ మెటాడేటాను తొలగించండి (💀మరల తీసుకోలేని చర్య — మీరు గిట్ది కార్యాచరణలను కోల్పోతారు: ఎలాంటి కమిట్లు, పుల్లు, పుష్లు, లేదా చరిత్ర నిలువదలవు).

```bash
# zsh/bash
rm -rf .git
```

```powershell
# పవర్‌షెల్
Remove-Item -Recurse -Force .git
```

#### GitHub Codespaces ఉపయోగించడం (స్థానిక పెద్ద డౌన్లోడ్లను నివారించడానికి సిఫార్సు చేయబడింది)

- ఈ రిపో కోసం [GitHub UI](https://github.com/codespaces) ద్వారా కొత్త Codespace సృష్టించండి.  

- కొత్తగా సృష్టించిన codespace టెర్మినల్‌లో, మీకు అవసరమైన పాఠాల ఫోల్డర్లను మాత్రమే Codespace వర్క్‌స్పేస్‌లో తీసుకురావడానికి పై యున్న షాలో/స్పార్స్ క్లోన్ కమాండ్లలో ఒకదాన్ని నడిపించండి.
- ఐచ్ఛికం: Codespaces లో క్లోన్ చేసే సమయానిమ్మీద .git ని తొలగించి అదనపు స్థలం తిరిగి పొందండి (క్రింద ఉన్న తొలగింపు కమాండ్లను చూడండి).
- గమనిక: మీరు రిపోను Codespaces లో నేరుగా తెరవాలని ఇష్టపడితే (కాగా అదనపు క్లోన్ లేకుండా), Codespaces డెవ్‌కంటైనర్ వాతావరణాన్ని సృష్టిస్తుంది మరియు మీరు అవసరమయ్యే కంటే ఎక్కువ ప్రావిజన్ చేయవచ్చు. తాజాది Codespace లో షాలో కాపీని క్లోన్ చేయడం ద్వారా మీరు డిస్క్ వనరులపై ఎక్కువ నియంత్రణ పొందవచ్చు.

#### సూచనలు

- ఎడిట్/కమిట్ చేయాలనుకుంటే కాపీ URL ను మీ ఫోర్క్ URL తో ఎప్పుడూ మార్చండి.
- తర్వాత చరిత్ర లేదా ఫైళ్లకు అవసరం ఉంటే, వాటిని ఫెట్ చేయవచ్చు లేదా స్పార్స్-చెక్‌ఔట్‌ను సవరించి అదనపు ఫోల్డర్లను చేర్చవచ్చు.

## కోడ్ నడుపడం

ఈ కోర్సు మీరు AI ఏజెంట్లు నిర్మించడంలో ప్రాక్టికల్ అనుభవం పొందటానికి నడిపించగల Jupyter Notebooks సీరీజ్ ని అందిస్తుంది.

కోడ్ నమూనాలు **Microsoft Agent Framework (MAF)** ను `FoundryChatClient` తో ఉపయోగిస్తున్నాయి, ఇది **Microsoft Foundry Agent Service V2** (Responses API) ద్వారా **Microsoft Foundry** కి కనెక్ట్ అవుతుంది.

అన్ని Python నోట్‌బుక్స్ `*-python-agent-framework.ipynb` గా లేబుల్ చేయబడ్డాయి.

## అవసరాలు

- Python 3.12+
  - **గమనిక**: Python3.12 ఇన్‌స్టాల్ చేయని వారు దాన్ని తప్పక ఇన్‌స్టాల్ చేసుకోండి. తర్వాత మీరు సరిగా అవసరమైన వెర్షన్లు requirements.txt ఫైల్ నుంచి ఇన్‌స్టాల్ చేయబడేలా python3.12 ఉపయోగించి మీ వర్చువల్ ఎన్విరాన్‌మెంట్ ను (venv) క్రియేట్ చేయండి.
  
    >ఉదాహరణ

    Python venv డైరెక్టరీని సృష్టించండి:

    ```bash|powershell
    python -m venv venv
    ```

    తరువాత క్రింది విధంగా venv ఎన్విరాన్‌మెంట్ ని యాక్టివేట్ చేయండి:

    ```bash
    # zsh/bash
    source venv/bin/activate
    ```
  
    ```dos
    # Command Prompt for Windows
    venv\Scripts\activate
    ```

- .NET 10+: .NET ఉపయోగించే కోడ్‌ల కోసం, [.NET 10 SDK](https://dotnet.microsoft.com/download/dotnet/10.0) లేక దానికంటే కొత్త వెర్షన్ ఇన్‌స్టాల్ చేసుకోండి. ఆపై ఇన్‌స్టాల్ చేసిన .NET SDK వెర్షన్‌ని తనిఖీ చేయండి:

    ```bash|powershell
    dotnet --list-sdks
    ```

- **Azure CLI** — ధృవీకరణ కొరకు అవసరం. [aka.ms/installazurecli](https://aka.ms/installazurecli) నుండి ఇన్‌స్టాల్ చేయండి.
- **Azure Subscription** — Microsoft Foundry మరియు Microsoft Foundry Agent Service యాక్సెస్ కొరకు.
- **Microsoft Foundry ప్రాజెక్ట్** — డిప్లాయ్ చేయబడిన మోడల్ (ఉదా: `gpt-4.1-mini`) ఉన్న ప్రాజెక్ట్. [డబ్బా 1](#1వ-దశ-microsoft-foundry-ప్రాజెక్ట్-సృష్టించండి) చూడండి.

ఈ రిపాజిటరీ రూట్ లో `requirements.txt` ఫైల్ అందించబడి ఉంది, ఇందులో కోడ్ నమూనాలను నడిపించడానికి అవసరమైన అన్ని Python ప్యాకేజీలు ఉన్నాయి.

మీరు ఈ క్రింది కమాండ్‌ని రి‌పోజిటరీ రూట్‌లో టెర్మినల్‌లో నడిపించి వాటిని ఇన్‌స్టాల్ చేసుకోవచ్చు:

```bash|powershell
pip install -r requirements.txt
```

ఏవైనా ఘర్షణలు మరియు సమస్యలను నివారించేందుకు Python వర్చువల్ ఎన్విరాన్‌మెంట్ సృష్టించడం మేము సిఫార్సు చేస్తున్నాము.

## VSCode సెటప్ చేయండి

మీరు VSCodeలో సరైన Python వెర్షన్ ఉపయోగిస్తున్నారో లేదో నిర్ధారించుకోండి.

![image](https://github.com/user-attachments/assets/a85e776c-2edb-4331-ae5b-6bfdfb98ee0e)

## Microsoft Foundry మరియు Microsoft Foundry Agent Service సెటప్ చేయండి

### 1వ దశ: Microsoft Foundry ప్రాజెక్ట్ సృష్టించండి

నోట్‌బుక్స్ నడిపించేందుకు మిమ్మల్ని Microsoft Foundry **హబ్** మరియు **ప్రాజెక్ట్** అవసరం ఉంటుంది, దీని లో మోడల్ డిప్లాయ్ చేయబడింది.

1. [ai.azure.com](https://ai.azure.com) కు వెళ్లి మీ Azure ఖాతా తో సైన్ ఇన్ అవ్వండి.
2. ఒక **హబ్** సృష్టించండి (లేదా ఇప్పటికే ఉన్న దానిని ఉపయోగించండి). వీక్షించండి: [Hub resources overview](https://learn.microsoft.com/azure/ai-foundry/concepts/ai-resources).
3. హబ్ లో ఒక **ప్రాజెక్ట్** సృష్టించండి.
4. **మోడల్స్ + ఎండ్‌పాయింట్స్** → **మోడల్ డిప్లాయ్ చేయండి** నుండి మోడల్ (ఉదా: `gpt-4.1-mini`) డిప్లాయ్ చేయండి.

### 2వ దశ: మీ ప్రాజెక్ట్ ఎండ్‌పాయింట్ మరియు మోడల్ డిప్లాయ్‌మెంట్ పేరు పొందండి

Microsoft Foundry పోర్టల్లో మీ ప్రాజెక్ట్ నుండి:

- **ప్రాజెక్ట్ ఎండ్‌పాయింట్** — **అవలోకనం** పేజీకి వెళ్లి ఎండ్‌పాయింట్ URL ని కాపీ చేసుకోండి.

![Project Connection String](../../../translated_images/te/project-endpoint.8cf04c9975bbfbf1.webp)

- **మోడల్ డిప్లాయ్‌మెంట్ పేరు** — **మోడల్స్ + ఎండ్‌పాయింట్స్**కి వెళ్లి, మీ డిప్లాయ్ చేసిన మోడల్ ఎంచుకుని, **డిప్లాయ్‌మెంట్ పేరు** (ఉదా: `gpt-4.1-mini`) గుర్తుంచుకోండి.

### 3వ దశ: `az login` తో Azure కి సైన్ ఇన్ అవ్వండి

అన్ని నోట్‌బుక్స్ **`AzureCliCredential`** ఉపయోగించి ధృవీకరిస్తాయి — ఏ API కీలు మేనేజ్ చేయాల్సిన అవసరం లేదు. దానికి Azure CLI ద్వారా సైన్ ఇన్ కావాలి.

1. మీరు ఇప్పటికీ Azure CLI ఇన్‌స్టాల్ చేయకపోతే: [aka.ms/installazurecli](https://aka.ms/installazurecli) నుండి ఇన్‌స్టాల్ చేయండి

2. సైన్ ఇన్ కావడానికి క్రింది కమాండ్ నడపండి:

    ```bash|powershell
    az login
    ```

    లేదా మీరు బ్రౌజర్ లేని రిమోట్/Codespace వాతావరణంలో ఉంటే:

    ```bash|powershell
    az login --use-device-code
    ```

3. మీరు అడిగితే మీ సబ్‌స్క్రిప్షన్ ని ఎంచుకోండి — ఇందులో మీ Foundry ప్రాజెక్టు ఉంది.

4. మీరు సైన్ ఇన్ అయినారని నిర్ధారించుకోండి:

    ```bash|powershell
    az account show
    ```

> **`az login` ఎందుకు?** నోట్‌బుక్స్ `azure-identity` ప్యాకేజీ నుండి `AzureCliCredential` ని ఉపయోగించి ధృవీకరిస్తాయి. అంటే, మీ Azure CLI సెషన్ క్రెడెన్షియల్స్ ని అందిస్తుంది — మీ `.env` ఫైల్‌లో API కీలు లేదా సీక్రెట్ల అవసరం లేదు. ఇది ఒక [భద్రత ఉత్తమ ప్రయోగం](https://learn.microsoft.com/azure/developer/ai/keyless-connections).

### 4వ దశ: మీ `.env` ఫైల్ సృష్టించండి

ఉదాహరణ ఫైలు కాపీ చేసుకోండి:

```bash
# జెడ్‌ఎస్‌హెచ్/బాష్
cp .env.example .env
```

```powershell
# పవర్‌షెల్
Copy-Item .env.example .env
```

`.env` తెరవండి మరియు ఈ రెండు విలువలను నింపండి:

```env
AZURE_AI_PROJECT_ENDPOINT=https://<your-project>.services.ai.azure.com/api/projects/<your-project-id>
AZURE_AI_MODEL_DEPLOYMENT_NAME=gpt-4.1-mini
```

| వేరియబుల్ | ఎక్కడ నుండి పొందాలి |
|----------|-----------------|
| `AZURE_AI_PROJECT_ENDPOINT` | Foundry పోర్టల్ → మీ ప్రాజెక్ట్ → **అవలోకనం** పేజీ |
| `AZURE_AI_MODEL_DEPLOYMENT_NAME` | Foundry పోర్టల్ → **మోడల్స్ + ఎండ్‌పాయింట్స్** → మీరు డిప్లాయ్ చేసిన మోడల్ పేరు |

చాలా పాఠాల కోసం ఇదే కావాలి! నోట్‌బుక్స్‌లు మీ `az login` సెషన్ ద్వారా ఆటోమేటిగ్గా ధృవీకరిస్తాయి.

### 5వ దశ: Python డిపెండెన్సీలు ఇన్‌స్టాల్ చేయండి

```bash|powershell
pip install -r requirements.txt
```

మేము సిఫార్సు చేస్తున్నది మీరు ముందుగా సృష్టించిన వర్చువల్ ఎన్విరాన్‌మెంట్ లో దీన్ని నడిపించండి.

## పాఠం 5 కోసం అదనపు సెటప్ (ఏజెంటిక్ RAG)

పాఠం 5 రిట్రీవల్-ఆగ్మెంటెడ్ జనరేషన్ కోసం **Azure AI Search** ఉపయోగిస్తుంది. మీరు ఆ పాఠం నడపాలని యోచిస్తే, ఈ వేరియబుల్స్‌ను మీ `.env` ఫైల్ లో చేర్చండి:

| వేరియబుల్ | ఎక్కడ ఖ‌త‌మ‌వుతుంది |
|----------|-----------------|
| `AZURE_SEARCH_SERVICE_ENDPOINT` | Azure పోర్టల్ → మీ **Azure AI Search** వనరు → **అవలోకనం** → URL |
| `AZURE_SEARCH_API_KEY` | Azure పోర్టల్ → మీ **Azure AI Search** వనరు → **సెట్టింగ్స్** → **కీలు** → ప్రాథమిక అడ్మిన్ కీ |

## Azure OpenAIని నేరుగా పిలిచే పాఠాల కోసం అదనపు సెటప్ (పాఠాలు 6 మరియు 8)

కొన్నిమంది పాఠాలు 6 మరియు 8 లోని నోట్‌బుక్స్ **Azure OpenAI** ని నేరుగా పిలుస్తాయి (మరియు **Responses API** ఉపయోగిస్తాయి), ఇది Microsoft Foundry ప్రాజెక్ట్ ద్వారా కాదు. ఈ నమూనాలు ముందుగా GitHub Models ఉపయోగించేవి, ఇవి వాయిదా పడినవి (2026 జూలైలో రిటైర్ అవుతాయి) మరియు Responses API మద్దతు ఇవ్వవు. మీరు ఆ నమూనాలు పరుగెత్తించాలనుకుంటే, ఈ వేరియబుల్స్ ను మీ `.env` ఫైల్ లో చేర్చండి:

| వేరియబుల్ | ఎక్కడ నుంచి పొందాలి |
|----------|-----------------|
| `AZURE_OPENAI_ENDPOINT` | Azure పోర్టల్ → మీ **Azure OpenAI** వనరు → **కీలు మరియు ఎండ్‌పాయింట్** → ఎండ్‌పాయింట్ (ఉదా: `https://<your-resource>.openai.azure.com`) |
| `AZURE_OPENAI_DEPLOYMENT` | మీ డిప్లాయ్ చేసిన మోడల్ పేరు (ఉదా: `gpt-4.1-mini`), ఇది Responses APIకి మద్దతు ఇస్తుంది |
| `AZURE_OPENAI_API_KEY` | ఐచ్ఛికం — మీరు `az login` / Entra ID బదులుగా కీ-ఆధారిత ధృవీకరణ ఉపయోగిస్తే మాత్రమే |

> Responses API స్థిరమైన `/openai/v1/` ఎండ్‌పాయింట్ ఉపయోగిస్తుంది, అందుకే ఎటువంటి `api-version` అవసరం లేదు. కీలు లేని Entra ID ధృవీకరణకు `az login` తో సైన్ ఇన్ అవ్వండి.

## ప్రత్యామ్నాయ ప్రొవైడర్: MiniMax (OpenAI-అనుకూలం)

[MiniMax](https://platform.minimaxi.com/) పెద్ద సాన్నిహిత్య మోడల్స్ (204K టోకెన్ల వరకు) ను OpenAI-అనుకూల API ద్వారా అందిస్తుంది. Microsoft Agent Framework యొక్క `OpenAIChatClient` ఏ OpenAI-అనుకూల ఎండ్‌పాయింట్‌తోనైనా పనిచేసినందున, మీరు MiniMaxని Azure OpenAI లేదా OpenAI కి ప్రత్యామ్నాయంగా ఉపయోగించవచ్చు.

ఈ వేరియబుల్స్‌ను మీ `.env` ఫైల్ లో చేర్చండి:

| వేరియబుల్ | ఎక్కడ నుండి పొందాలి |
|----------|-----------------|
| `MINIMAX_API_KEY` | [MiniMax Platform](https://platform.minimaxi.com/) → API కీలు |
| `MINIMAX_BASE_URL` | `https://api.minimax.io/v1` ఉపయోగించండి (డిఫాల్ట్ విలువ) |
| `MINIMAX_MODEL_ID` | ఉపయోగించే మోడల్ పేరు (ఉదా: `MiniMax-M3`) |

**ఉదాహరణ మోడల్స్**: `MiniMax-M3` (సిఫార్సు చేయబడింది), `MiniMax-M2.7`, `MiniMax-M2.7-highspeed` (వేగంగా స్పందిస్తుంది). మోడల్ పేర్లు మరియు లభ్యత కాలానుగుణంగా మారవచ్చు మరియు ఒక నిర్దిష్ట మోడల్ కు యాక్సెస్ మీ ఖాతా లేదా ప్రాంతంపై ఆధారపడి ఉంటుంది — [MiniMax Platform](https://platform.minimaxi.com/) లో ప్రస్తుత జాబితాను పరీక్షించండి. మీరు `MiniMax-M3` అందుబాటులో లేకపోతే, మీకు అందుబాటులో ఉన్న మోడల్ ను `MINIMAX_MODEL_ID` గా సెట్ చేయండి (ఉదా: `MiniMax-M2.7`).

`OpenAIChatClient` ఉపయోగించే కోడ్ నమూనాలు (ఉదా: పాఠం 14 హోటల్ బుకింగ్ వర్క్‌ఫ్లో) `MINIMAX_API_KEY` సెట్ చేస్తే మీ MiniMax కాన్ఫిగరేషన్‌ని ఆటోమేటిగ్గా గుర్తించి ఉపయోగిస్తాయి.

## ప్రత్యామ్నాయ ప్రొవైడర్: Foundry Local (మోడల్స్‌ను డివైస్ మీద నడపండి)

[Foundry Local](https://foundrylocal.ai) ఒక తేలికపాటి రంటైమ్, ఇది భాష మోడల్స్‌ను **మీ స్వంత యంత్రంపై పూర్తిగా** OpenAI-అనుకూల API ద్వారా డౌన్లోడ్ చేసి నిర్వహించగలదు — క్లౌడ్ లేదు, Azure సబ్‌స్క్రిప్షన్ లేదు, API కీలు లేవు. ఇది ఆఫ్‌లైన్ డెవలప్మెంట్, క్లౌడ్ ఖర్చులు లేకుండా పరీక్షించడం, లేదా డేటాను డివైస్‌లో ఉంచడం కోసం చాలా గొప్ప ఎంపిక.

Microsoft Agent Framework యొక్క `OpenAIChatClient` ఏ OpenAI-అనుకూల ఎండ్‌పాయింట్ తోనైనా పనిచేసినందున, Foundry Local Azure OpenAI కి స్థానిక ప్రత్యామ్నాయం.

**1. Foundry Local ను ఇన్‌స్టాల్ చేయండి**

```bash
# విండోస్
winget install Microsoft.FoundryLocal

# మాక్‌ఓఎస్
brew install foundrylocal
```

**2. ఒక మోడల్ డౌన్లోడ్ చేసి నడపండి** (ఇది స్థానిక సేవను కూడా ప్రారంభిస్తుంది):

```bash
foundry model list          # అందుబాటులో ఉన్న మోడల్స్ చూడండి
foundry model run phi-4-mini
```

**3. స్థానిక ఎండ్‌పాయింట్ కనుగొనే Python SDK ను ఇన్‌స్టాల్ చేయండి:**

```bash
pip install foundry-local-sdk
```

**4. Microsoft Agent Framework ని మీ స్థానిక మోడల్ వైపు సూచించండి:**

```python
from foundry_local import FoundryLocalManager
from agent_framework.openai import OpenAIChatClient

# అవసరమైతే డౌన్‌లోడ్ చేసి మోడల్‌ను స్థానికంగా సర్వ్ చేస్తుంది, ఆ తర్వాత ఎండ్పాయింట్/పోర్ట్ ని కనుగొంటుంది.
manager = FoundryLocalManager("phi-4-mini")

chat_client = OpenAIChatClient(
    base_url=manager.endpoint,      # ఉదా. http://localhost:<port>/v1
    api_key=manager.api_key,        # Foundry Local కోసం ఎప్పుడూ "అవసరం లేదు"
    model_id=manager.get_model_info("phi-4-mini").id,
)

agent = chat_client.as_agent(
    name="LocalAgent",
    instructions="You are a helpful assistant running fully on-device.",
)
```

> **గమనిక:** Foundry Local OpenAI-అనుకూల **చాట్ కంప్లీషన్స్** ఎండ్‌పాయింట్‌ను అందిస్తుంది. స్థానిక అభివృద్ధి మరియు ఆఫ్‌లైన్ పరిస్థితేల కోసం దీన్ని ఉపయోగించండి. పూర్తి **Responses API** ఫీచర్ సెట్ (స్టేట్‌ఫుల్ సంభాషణలు, లోతైన టూల్ ఆర్కిస్ట్రేషన్, ఏజెంట్-శైలీలో అభివృద్ధి) కోసం, పాఠాలలో చూపినట్లుగా **Azure OpenAI** లేదా **Microsoft Foundry** ప్రాజెక్ట్‌ను లక్ష్యంగా నొక్కండి. ప్రస్తుత మోడల్ కేటలాగ్ మరియు ప్లాట్‌ఫాం మద్దతు కోసం [Foundry Local డాక్యుమెంటేషన్](https://foundrylocal.ai) చూడండి.


## పాఠం 8 కోసం అదనపు సెటప్ (బింగ్ గ్రౌండింగ్ వర్క్ఫ్లో)

పాఠం 8లో ఉన్న కండిషనల్ వర్క్‌ఫ్లో నోట్‌బుక్ Microsoft Foundry ద్వారా **బింగ్ గ్రౌండింగ్** ఉపయోగిస్తుంది. మీరు ఆ నమూనాను నిర్వహించాలనుకుంటే, ఈ వేరియబుల్‌ను మీ `.env` ఫైల్‌లో జోడించండి:

| వేరియబుల్ | ఎక్కడ కనుగొనాలి |
|----------|-----------------|
| `BING_CONNECTION_ID` | Microsoft Foundry పోర్టల్ → మీ ప్రాజెక్ట్ → **Management** → **Connected resources** → మీ Bing కనెక్షన్ → కనెక్షన్ ID కాపీ చేయండి |

## సమస్య పరిష్కారం

### macOSపై SSL సర్టిఫికెట్ తనిఖీ పొరపాట్లు

మీరు macOSపై ఉంటే మరియు క్రింది త్రుటి వస్తే:

```plaintext
ssl.SSLCertVerificationError: [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: self-signed certificate in certificate chain
```

ఇది macOSపై Pythonకి తెలిసిన ఒక సమస్య, ఎక్కడ సిస్టమ్ SSL సర్టిఫికెట్లను స్వయంచాలకంగా విశ్వసించదూ. కింది పరిష్కారాలను క్రమంగా ప్రయత్నించండి:

**ఎంపిక 1: Python యొక్క Install Certificates స్క్రిప్ట్ నడపండి (సిఫారసు చేయబడింది)**

```bash
# మీరు ఇన్స్టాల్ చేసిన Python సంస్కరణతో 3.XX ను మార్చండి (ఉదాహరణకు, 3.12 లేదా 3.13):
/Applications/Python\ 3.XX/Install\ Certificates.command
```

**ఎంపిక 2: మీ నోట్‌బుక్‌లో `connection_verify=False` ఉపయోగించండి (GitHub మోడల్స్ నోట్‌బుక్స్ కొరకు మాత్రమే)**

పాఠం 6 నోట్‌బుక్‌లో (`06-building-trustworthy-agents/code_samples/06-system-message-framework.ipynb`), ఒక వ్యాఖ్యానించబడిన పద్దతి ఇప్పటికే ఇవ్వబడింది. క్లయింట్ సృష్టించినప్పుడు `connection_verify=False` ను వ్యాఖ్యను తొలగించి ఉపయోగించండి:

```python
client = ChatCompletionsClient(
    endpoint=endpoint,
    credential=AzureKeyCredential(token),
    connection_verify=False,  # సర్టిఫికేట్ పొరపాట్లు ఎదురైతే SSL నిర్ధారణను నిలిపివేయండి
)
```

> **⚠️ హెచ్చరిక:** SSL తనిఖీని నిలిపివేస్తే (`connection_verify=False`), సర్టిఫికెట్ ధృవీకరణను దాటవేయడం వల్ల భద్రత తగ్గుతుంది. దీన్ని అభివృద్ది వాతావరణాల్లో తాత్కాలిక పరిష్కారం మాత్రమే ఉపయోగించండి, ఉత్పత్తిలో ఎప్పుడూ ఉపయోగించకండి.

**ఎంపిక 3: `truststore`ని ఇన్స్తాల్ చేసి ఉపయోగించండి**

```bash
pip install truststore
```

తరువాత, మీ నోట్‌బుక్ లేదా స్క్రిప్ట్ పైభాగంలో ఈ క్రింది కోడును జోడించండి, ఏనెట్‌వర్క్ కాల్స్ మొద‌లుపెట్టేముందు:

```python
import truststore
truststore.inject_into_ssl()
```

## ఏదైనా ఇబ్బంది?

ఈ సెటప్ నిర్వహించడంలో ఎలాంటి సమస్యలు ఉంటే, మా <a href="https://discord.gg/kzRShWzttr" target="_blank">Azure AI Community Discord</a> లోకి చేరండి లేదా <a href="https://github.com/microsoft/ai-agents-for-beginners/issues?WT.mc_id=academic-105485-koreyst" target="_blank">ఇష్యూ సృష్టించండి</a>.

## తదుపరి పాఠం

మీరు ఈ కోర్సు కోడ్ నడపడానికి సిద్ధంగా ఉన్నారు. AI ఏజెంట్ల ప్రపంచం గురించి మరింత తెలుసుకోవడంలో సంతోషంగా ఉండండి!

[AI ఏజెంట్లకు పరిచయం మరియు ఏజెంట్ ఉపయోగ కేసులు](../01-intro-to-ai-agents/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**అస్వీకరణ**:
ఈ పత్రం AI అనువాద సేవ [Co-op Translator](https://github.com/Azure/co-op-translator) ఉపయోగించి అనువదించబడింది. మేము ఖచ్చితత్వానికి ప్రయత్నిస్తున్నప్పటికీ, ఆటోమేటెడ్ అనువాదాలు తప్పులు లేదా అసమగ్రతలను కలిగి ఉండవచ్చు. దాని స్వదేశ భాషలో ఉన్న అసలు పత్రాన్ని అధికారం కలిగిన మూలంగా పరిగణించాలి. కీలకమైన సమాచారం కోసం, ప్రొఫెషనల్ మానవ అనువాదాన్ని సిఫారసు చేస్తాము. ఈ అనువాదం ఉపయోగం వల్ల కలిగే ఏవైనా అపార్థాలు లేదా తప్పుదారులు కోసం మేము బాధ్యత వహించము.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->