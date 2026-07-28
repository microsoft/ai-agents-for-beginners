# కోర్సు సెటప్

## పరిచయం

ఈ పాఠం ఈ కోర్సు యొక్క కోడ్ ఉదాహరణలు ఎలా నడుపాలో వివరిస్తుంది.

## ఇతర విద్యార్థులతో చేరండి మరియు సహాయం పొందండి

మీ రెపోను క్లోన్ చేయడం ప్రారంభించే ముందు, సెటప్‌కు ఏమైనా సహాయం, కోర్సుపై ప్రశ్నలు లేదా ఇతర విద్యార్థుల దగ్గర చేరడానికి [AI Agents For Beginners Discord channel](https://aka.ms/ai-agents/discord) లో చేరండి.

## ఈ రెపోను క్లోన్ లేదా ఫోర్క్ చేయండి

ప్రారంభించడానికి, గిట్హబ్ రిపాజిటరీని క్లోన్ లేదా ఫోర్క్ చేయండి. ఇది మీ సొంత వర్షన్‌ను సృష్టిస్తుంది, దీనితో మీరు కోడ్‌ను నడిపించవచ్చు, పరీక్షించవచ్చు మరియు మార్చవచ్చు!

ఇది <a href="https://github.com/microsoft/ai-agents-for-beginners/fork" target="_blank">ఫోర్క్ చేయడానికి</a> లింకును క్లిక్ చేయడం ద్వారా చేయవచ్చు

ఇప్పుడు మీకు ఈ కోర్సు యొక్క మీ స్వంత ఫోర్క్డ్ వెర్షన్ ఈ కింది లింకులో ఉండాలి:

![Forked Repo](../../../translated_images/te/forked-repo.33f27ca1901baa6a.webp)

### షాలో క్లోన్ (వర్క్‌షాప్ / కోడ్స్‌పేస్‌ల కోసం సూచించబడింది)

  >పూర్తి రిపాజిటరీ పూర్తి చరిత్ర మరియు అన్ని ఫైళ్లను డౌన్లోడ్ చేస్తే పెద్దది అయి (~3 GB) ఉంటుంది. మీరు కేవలం వర్క్‌షాప్‌కి మాత్రమే హాజరైతే లేదా కొద్దిగా పాఠాలు మాత్రమే అవసరమైతే, షాలో క్లోన్ లేదా స్పార్స్ క్లోన్ చరిత్రను కత్తిరించడం లేదా బ్లాబ్స్ స్కిప్ చేయడం ద్వారా ఎక్కువ భాగం డౌన్లోడ్‌ను నివారిస్తుంది.

#### త్వరిత షాలో క్లోన్ — కనీస చరిత్ర, అన్ని ఫైళ్లు

క్రింద ఉన్న కమాండ్లలో `<your-username>`ని మీ ఫోర్క్ URL (లేదా మీరు ఇష్టపడితే అపస్ట్రీమ్ URL) తో మార్చండి.

తాజా కమీట్ చరిత్రను మాత్రమే క్లోన్ చేయడానికి (చిన్న డౌన్లోడ్):

```bash|powershell
git clone --depth 1 https://github.com/<your-username>/ai-agents-for-beginners.git
```

ఒక నిర్దిష్ట బ్రాంచ్ క్లోన్ చేయడానికి:

```bash|powershell
git clone --depth 1 --branch <branch-name> https://github.com/<your-username>/ai-agents-for-beginners.git
```

#### ఆకుముపాలక (స్పార్స్) క్లోన్ — కనీస బ్లాబ్స్ + కొన్ని నిర్దిష్ట ఫోల్డర్లు మాత్రమే

ఇది partial clone మరియు sparse-checkout ఉపయోగిస్తుంది (Git 2.25+ అవసరం మరియు partial cloneకి మోడ్రన్ Git సూచించబడింది):

```bash|powershell
git clone --depth 1 --filter=blob:none --sparse https://github.com/<your-username>/ai-agents-for-beginners.git
```

రిపో ఫోల్డర్‌లోకి వెళ్లండి:

```bash|powershell
cd ai-agents-for-beginners
```

తర్వాత మీరు అవసరమైన ఫోల్డర్లను నిర్దారించండి (కింది ఉదాహరణ రెండు ఫోల్డర్లను చూపిస్తుంది):

```bash|powershell
git sparse-checkout set 00-course-setup 01-intro-to-ai-agents
```

క్లోన్ చేసి ఫైళ్లు పరిశీలించిన తర్వాత, మీరు కేవలం ఫైళ్లు కావాలని మరియు స్థలాన్ని తొలగించాలనుకుంటే (గిట్ చరిత్ర లేదు), దయచేసి రిపాజిటరీ మెటాడేటాను తొలగించండి (💀మార్చలేని — మీరు అన్ని Git కార్యకలాపాలను కోల్పోతారు: కమిట్లు, పుల్స్, పుష్లు లేదా చరిత్ర యాక్సెస్ లేవు).

```bash
# zsh/bash
rm -rf .git
```

```powershell
# పవర్ షెల్
Remove-Item -Recurse -Force .git
```

#### GitHub కోడ్స్‌పేస్‌లను ఉపయోగించడం (స్థానిక పెద్ద డౌన్లోడ్లను నివారించడానికి సూచించబడింది)

- ఈ రెపోకు కోసం [GitHub UI](https://github.com/codespaces) ద్వారా కొత్త కోడ్స్‌పేస్ సృష్టించండి.

- కొత్తగా సృష్టించిన కోడ్స్‌పేస్ టెర్మినల్లో, చేర్చిన పాఠాల ఫోల్డర్లను మాత్రమే కోడ్స్‌పేస్ వర్క్‌స్పేస్‌లో తెచ్చేందుకు పై షాలో/స్పార్స్ క్లోన్ కమాండ్లలో ఏదైనా నడిపించండి.
- అదనంగా: కోడ్స్‌పేస్ లో క్లోన్ చేసిన తర్వాత, అదనపు స్థలాన్ని తిరిగి పొందడానికి .git ను తీసివేయండి (పై తొలగింపు కమాండ్లను చూడండి).
- గమనిక: మీరు ఈ రెపోను నేరుగా కోడ్స్‌పేస్‌లలో (అదనపు క్లోన్ లేకుండానే) తెరవడానికి ఇష్టపడితే, కోడ్స్‌పేస్‌లు devcontainer వాతావరణాన్ని నిర్మిస్తాయి మరియు మీకు అవసరం కంటే ఎక్కువ వనరులు అప్పగించవచ్చు. కొత్త కోడ్స్‌పేస్ లో షాలో కాపీని క్లోన్ చేయడం ద్వారా డ్రైవ్ ఉపయోగాన్ని మెరుగ్గా నియంత్రించవచ్చు.

#### సూచనలు

- ఎప్పుడూ మీరు ఎడిట్/కమిట్ చేయాలనుకుంటే, క్లోన్ URL ను మీ ఫోర్క్ URL తో మార్చండి.
- తర్వాత చరిత్ర లేదా ఫైళ్లు కావాలంటే, వాటిని fetch చేయవచ్చు లేదా sparse-checkout మార్చి అదనపు ఫోల్డర్లను చేర్చవచ్చు.

## కోడ్ నడపడం

ఈ కోర్సు AI ఏజెంట్స్ నిర్మాణంలో అనుభవం పొందడానికి నడిపించదగిన జ్యూపిటర్ నోట్బుక్స్ ల సంకలనాన్ని అందిస్తుంది.

కోడ్ ఉదాహరణలు **Microsoft Agent Framework (MAF)** ను ఉపయోగిస్తూ ఉంటాయి, `FoundryChatClient` తో, ఇది **Microsoft Foundry** ద్వారా **Microsoft Foundry Agent Service V2** (Responses API) కు కనెక్ట్ అవుతుంది.

అన్ని పైనథాన్ నోట్బుక్స్ `*-python-agent-framework.ipynb` అనే లేబుల్ కలిగి ఉంటాయి.

## అవసరాలు

- Python 3.12+
  - **గమనిక**: మీకు Python3.12 ఇన్స్టాల్ లేకపోతే, దయచేసి ముందుగా దాన్ని ఇన్స్టాల్ చేయండి. తరువాత కొన్ని అవసరమైన వెర్షన్ల కోసం requirements.txt ఫైల్ నుండి సరైన ప్యాకేజీలు పొందడానికి python3.12 ఉపయోగించి మీ వర్చువల్ ఎన్‌విరాన్మెంట్ క్రియేట్ చేయండి.
  
    >ఉదాహరణ

    Python వర్చువల్-env డైరెక్టరీని సృష్టించండి:

    ```bash|powershell
    python -m venv venv
    ```

    తరువాత వర్చువల్-envని చురుకుచేయండి:

    ```bash
    # zsh/bash
    source venv/bin/activate
    ```
  
    ```dos
    # Command Prompt for Windows
    venv\Scripts\activate
    ```

- .NET 10+: .NET ఉపయోగించే సాంపిల్ల కోసం [.NET 10 SDK](https://dotnet.microsoft.com/download/dotnet/10.0) లేదా తర్వాతి వర్షన్ ఇన్స్టాల్ చేయండి. తర్వాత మీరు ఇన్స్టాల్ చేసిన .NET SDK వెర్షన్ పరిశీలించండి:

    ```bash|powershell
    dotnet --list-sdks
    ```

- **Azure CLI** — అథెంటికేషన్ కోసం అవసరం. [aka.ms/installazurecli](https://aka.ms/installazurecli) నుండి ఇన్స్టాల్ చేయండి.
- **Azure Subscription** — Microsoft Foundry మరియు Microsoft Foundry Agent Service కి యాక్సెస్ కోసం.
- **Microsoft Foundry Project** — మోడల్ డిప్లాయ్ చేసిన ప్రాజెక్ట్ (ఉదా: `gpt-5-mini`). కింది [Step 1](#దశ-1-microsoft-foundry-ప్రాజెక్ట్-సృష్టించండి) చూడండి.

ఈ రెపో యొక్క రూట్ లో అవసరమైన అన్ని Python ప్యాకేజీలతో కూడిన `requirements.txt` ఫైల్ ను చేర్చాము.

ఈ క్రింది ఆదేశాన్ని రూట్ డైరెక్టరీలో మీ టెర్మినల్ లో నడిపించాలి:

```bash|powershell
pip install -r requirements.txt
```

వివిధ సమస్యలు లేకుండా Python వర్చువల్ ఎన్విరాన్మెంట్ సృష్టించమని సూచించబడింది.

## VSCode సెటప్ చేయండి

మీరు VSCodeలో సరైన Python వెర్షన్ ఉపయోగిస్తున్నదో లేదో నిర్ధారించుకోండి.

![image](https://github.com/user-attachments/assets/a85e776c-2edb-4331-ae5b-6bfdfb98ee0e)

## Microsoft Foundry మరియు Microsoft Foundry Agent Service సెటప్ చేయండి

### దశ 1: Microsoft Foundry ప్రాజెక్ట్ సృష్టించండి

నోట్బుక్స్ నడపడానికి Microsoft Foundry **హబ్** మరియు డిప్లాయ్ అయిన మోడల్ ఉన్న **ప్రాజెక్ట్** అవసరం.

1. [ai.azure.com](https://ai.azure.com) కి వెళ్లి మీ Azure ఖాతాతో సైన్ ఇన్ అవ్వండి.
2. ఒక **హబ్** సృష్టించండి (లేదా ఇప్పటికే ఉన్నది వాడండి). చూడండి: [Hub resources overview](https://learn.microsoft.com/azure/ai-foundry/concepts/ai-resources).
3. ఆ హబ్ లో ఒక **ప్రాజెక్ట్** సృష్టించండి.
4. **Models + Endpoints** → **Deploy model** వద్ద ఒక మోడల్ (ఉదా: `gpt-5-mini`) ని డిప్లాయ్ చేయండి.

### దశ 2: మీ ప్రాజెక్ట్ ఎండ్‌పాయింట్ మరియు మోడల్ డిప్లాయ్‌మెంట్ పేరు పొందండి

మీ Microsoft Foundry పోర్టల్ లోని ప్రాజెక్ట్ నుండి:

- **Project Endpoint** — **Overview** పేజీకి వెళ్లి ఎండ్‌పాయింట్ URL కాపీ చేయండి.

![Project Connection String](../../../translated_images/te/project-endpoint.8cf04c9975bbfbf1.webp)

- **Model Deployment Name** — **Models + Endpoints** వద్ద మీ డిప్లాయ్ చేసిన మోడల్ ఎంచుకుని, **Deployment name** (ఉదా: `gpt-5-mini`) గుర్తించండి.

### దశ 3: `az login` తో Azure లో సైన్ ఇన్ అవ్వండి

అన్ని నోట్బుక్స్ **`AzureCliCredential`** ఉపయోగించి అథెంటికేట్ అవుతాయి — ఏ API కీలు అవసరం లేదు. ఇది Azure CLI ద్వారా సైన్ ఇన్ కావటం అవసరం.

1. **Azure CLI ఇన్స్టాల్ చేయండి** (మీరు ఇంతలాగే చేయకపోతే): [aka.ms/installazurecli](https://aka.ms/installazurecli)

2. **సైన్ ఇన్ అవ్వండి** ఈ విధంగా:

    ```bash|powershell
    az login
    ```

    లేదా మీరు రిమోట్/కోడ్స్‌పేస్ వాతావరణంలో బ్రౌజర్ లేకుండా ఉంటే:

    ```bash|powershell
    az login --use-device-code
    ```

3. **మీ సబ్‌స్క్రిప్షన్ ఎంచుకోండి** (ప్రాంప్ట్ వస్తే) — మీ Foundry ప్రాజెక్ట్ ఉన్నది ఎంచుకోండి.

4. మీరు సైన్ ఇన్ అయ్యారు అని ధృవీకరించుకోండి:

    ```bash|powershell
    az account show
    ```

> **ఎందుకు `az login`?** నోట్బుక్స్ `azure-identity` ప్యాకేజీ నుండి `AzureCliCredential` ఉపయోగించి అథెంటికేట్ చేస్తాయి. అంటే మీ Azure CLI సెషన్ క్రెడెన్షియల్స్ అందిస్తుంది — `.env` ఫైలులో API కీలు లేదా సీక్రెట్స్ అవసరం లేదు. ఇది [భద్రత ఉత్తమ అభ్యాసం](https://learn.microsoft.com/azure/developer/ai/keyless-connections).

### దశ 4: మీ `.env` ఫైల్ సృష్టించండి

ఉదాహరణ ఫైల్ ని కాపీ చేయండి:

```bash
# zsh/bash
cp .env.example .env
```

```powershell
# పవర్‌షెల్
Copy-Item .env.example .env
```

`.env` ని తెరవండి మరియు ఈ రెండు విలువలను నింపండి:

```env
AZURE_AI_PROJECT_ENDPOINT=https://<your-project>.services.ai.azure.com/api/projects/<your-project-id>
AZURE_AI_MODEL_DEPLOYMENT_NAME=gpt-5-mini
```

| వేరియబుల్ | దొరకడానికి స్థలం |
|----------|-----------------|
| `AZURE_AI_PROJECT_ENDPOINT` | Foundry పోర్టల్ → మీ ప్రాజెక్ట్ → **Overview** పేజీ |
| `AZURE_AI_MODEL_DEPLOYMENT_NAME` | Foundry పోర్టల్ → **Models + Endpoints** → మీ డిప్లాయ్ చేసిన మోడల్ పేరు |

ఎక్కువ వాడుతున్న పాఠాల కోసం అంతే! నోట్బుక్స్ మీ `az login` సెషన్ ద్వారా ఆటోమేటిక్ అథెంటికేట్ అవుతాయి.

### దశ 5: పython డిపెండెన్సీలు ఇన్స్టాల్ చేయండి

```bash|powershell
pip install -r requirements.txt
```

మీరు ముందుగా సృష్టించిన వర్చువల్ ఎన్విరాన్మెంట్ లో దీనిని నడపాలని సూచించబడింది.

## పాఠం 5 (Agentic RAG) కోసం అదనపు సెటప్

పాఠం 5 రిట్రీవల్-ఆగ్మెంటెడ్ జనరేషన్ కోసం **Azure AI Search** ఉపయోగిస్తుంది. మీరు ఆ పాఠం నడపాలనుకుంటే, ఈ వేరియబుల్స్ ను `.env` ఫైల్ లో చేర్చండి:

| వేరియబుల్ | దొరకడానికి స్థలం |
|----------|-----------------|
| `AZURE_SEARCH_SERVICE_ENDPOINT` | Azure పోర్టల్ → మీ **Azure AI Search** వనరు → **Overview** → URL |
| `AZURE_SEARCH_API_KEY` | Azure పోర్టల్ → మీ **Azure AI Search** వనరు → **Settings** → **Keys** → ప్రాధమిక అడ్మిన్ కీ |

## Azure OpenAIను నేరుగా పిలిచే పాఠాల సహాయంతో అదనపు సెటప్ (పాఠాలు 6 మరియు 8)

కొంతమంది పాఠాలు 6 మరియు 8 లో కాస్త నేరుగా **Azure OpenAI** (Responses API ద్వారా) పిలుస్తాయి, Microsoft Foundry ప్రాజెక్టు ద్వారా కాకుండా. ఈ నమూనాలు గతంలో GitHub Models ఉపయోగించాయి, ఇవి నిలిపివేయబడ్డాయి (2026 జూలైలో రిటైర్ అవుతాయి) మరియు Responses APIకి మద్దతు ఇవ్వవు. మీరు ఆ నమూనాలు నడపాలనుకుంటే, ఈ వేరియబుల్స్ `.env`లో చేర్చండి:

| వేరియబుల్ | దొరకడానికి స్థలం |
|----------|-----------------|
| `AZURE_OPENAI_ENDPOINT` | Azure పోర్టల్ → మీ **Azure OpenAI** వనరు → **Keys and Endpoint** → ఎండ్‌పాయింట్ (ఉదా: `https://<your-resource>.openai.azure.com`) |
| `AZURE_OPENAI_DEPLOYMENT` | మీరు డిప్లాయ్ చేసిన మోడల్ పేరు (ఉదా: `gpt-5-mini`) ఇది Responses APIకి మద్దతు ఇస్తుంది |
| `AZURE_OPENAI_API_KEY` | ఐచ్ఛికం — key-based auth ఉపయోగిస్తే మాత్రమే అవసరం, `az login` / Entra ID స్థానంలో |

> Responses API స్థిరమైన `/openai/v1/` ఎండ్‌పాయింట్ ఉపయోగిస్తుంది, అందువల్ల `api-version` అవసరం లేదు. కీ-లెస్ Entra ID అథెంటికేషన్ కోసం `az login` తో సైన్ ఇన్ అవ్వండి.

## ప్రత్యామ్నాయ ప్రొవైడర్: MiniMax (OpenAI-అనుకూలమైనది)

[MiniMax](https://platform.minimaxi.com/) పెద్ద కాన్టెక్స్ మోడల్స్ (204K టోకెన్ల వరకు) OpenAI అనుకూల API ద్వారా అందిస్తుంది. Microsoft Agent Frameworkలోని `OpenAIChatClient` ఏ OpenAI-అనుకూల ఎండ్‌పాయింట్తోనైనా పని చేయగలదు, కాబట్టి MiniMax ను Azure OpenAI లేదా OpenAI కు ప్రత్యామ్నాయం గా ఉపయోగించవచ్చు.

ఈ వేరియబుల్స్ ను `.env` ఫైల్ లో చేర్చండి:

| వేరియబుల్ | దొరకడానికి స్థలం |
|----------|-----------------|
| `MINIMAX_API_KEY` | [MiniMax Platform](https://platform.minimaxi.com/) → API కీలను పొందండి |
| `MINIMAX_BASE_URL` | `https://api.minimax.io/v1` (డిఫాల్ట్ విలువు) ఉపయోగించండి |
| `MINIMAX_MODEL_ID` | వాడదలచిన మోడల్ పేరు (ఉదా: `MiniMax-M3`) |

**ఉదాహరణ మోడల్స్**: `MiniMax-M3` (సూచించబడింది), `MiniMax-M2.7`, `MiniMax-M2.7-highspeed` (వేలిగా సమాధానాలు). మోడల్ పేర్లు మరియు అందుబాటు కాలం తో మారవచ్చు, మోడల్ యాక్సెస్ మీ అకౌంట్ లేదా ప్రాంతం ఆధారంగా ఉండవచ్చు — తాజా జాబితా కోసం [MiniMax Platform](https://platform.minimaxi.com/) చూసుకోండి. `MiniMax-M3` మీకు అందుబాటులో లేకుంటే, మీకు అందుబాటులో ఉన్న మోడల్ (ఉదా: `MiniMax-M2.7`)కి `MINIMAX_MODEL_ID` సెట్ చేయండి.

`OpenAIChatClient` ఉపయోగించే ఉదాహరణలు (ఉదా: పాఠం 14 హోటల్ బుకింగ్ వర్క్‌ఫ్లో) ఆటోమేటిగానే `MINIMAX_API_KEY` సెట్ అయితే మీ MiniMax సెట్టింగ్స్ ని గుర్తించి ఉపయోగిస్తాయి.

## ప్రత్యామ్నాయ ప్రొవైడర్: Foundry Local (మోడల్స్ ని డివైస్ పై నడిపించండి)

[Foundry Local](https://foundrylocal.ai) ఒక లైట్‌వెయిట్ రన్‌టైమ్, మీరు మీ కంప్యూటర్ మీద భాషా మోడల్స్‌ని డౌన్లోడ్ చేసి, నిర్వహించి, OpenAI-అనుకూల API ద్వారా సర్వ్ చేస్తుంది — క్లౌడ్ లేదూ, Azure సబ్‌స్క్రిప్షన్ లేదూ, API కీలు అవసరం లేకుండా. ఇది ఆఫ్‌లైన్ డెవలప్‌మెంట్, క్లౌడ్ ఖర్చులు లేకుండా ఎక్స్‌పెరిజ్ చేయడానికి, లేదా డేటాను డివైస్ లోనే ఉంచడానికి అద్భుతమైన ఆప్షన్.

Microsoft Agent Frameworkలోని `OpenAIChatClient` ఏ OpenAI అనుకూల ఎండ్‌పాయింట్తోనైనా పని చేయగలదు కాబట్టి, Foundry Local Azure OpenAIకి స్థానిక ప్రత్యామ్నాయం.

**1. Foundry Local ఇన్స్టాల్ చేయండి**

```bash
# విండోస్
winget install Microsoft.FoundryLocal

# మాక్OS
brew install foundrylocal
```

**2. ఒక మోడల్ డౌన్లోడ్ చేసి నడపండి** (ఇది స్థానిక సర్వీస్‌ను కూడా ప్రారంభిస్తుంది):

```bash
foundry model list          # అందుబాటులో ఉన్న మోడళ్లను చూడండి
foundry model run phi-4-mini
```

**3. స్థానిక ఎండ్‌పాయింట్ను కనుగొనేందుకు Python SDK ని ఇన్స్టాల్ చేయండి:**

```bash
pip install foundry-local-sdk
```

**4. Microsoft Agent Frameworkని మీ స్థానిక మోడల్ వైపు సూచించండి:**

```python
from foundry_local import FoundryLocalManager
from agent_framework.openai import OpenAIChatClient

# అవసరమైతే డౌన్‌లోడ్ చేసి, స్థానికంగా మోడల్‌ను అందిస్తుంది, తర్వాత ఎండ్‌పాయింట్/పోర్ట్‌ను కనుగొంటుంది.
manager = FoundryLocalManager("phi-4-mini")

chat_client = OpenAIChatClient(
    base_url=manager.endpoint,      # ఉదా: http://localhost:<port>/v1
    api_key=manager.api_key,        # Foundry Local కోసం ఎల్లప్పుడూ "అవసరం లేదు"
    model_id=manager.get_model_info("phi-4-mini").id,
)

agent = chat_client.as_agent(
    name="LocalAgent",
    instructions="You are a helpful assistant running fully on-device.",
)
```

> **గమనిక:** Foundry Local OpenAI అనుకూల **చాట్ కంప్లీషన్** ఎండ్‌పాయింట్‌ను ఎక్స్‌పోస్ చేస్తుంది. స్థానిక డెవలప్‌మెంట్ మరియు ఆఫ్‌లైన్ సన్నివేశాల కోసం దీనిని ఉపయోగించండి. పూర్తి **Responses API** ఫీచర్ సెట్ కోసం (స్థితిగత సంభాషణలు, లోతైన టూల్ ఆర్కెస్ట్రేషన్, ఏజెంట్-స్టైల్ డెవలప్‌మెంట్), పాఠాలలో చూపినట్లు **Azure OpenAI** లేదా **Microsoft Foundry** ప్రాజెక్ట్‌ను టార్గెట్ చేయండి. తాజా మోడల్ క్యాటలాగ్ మరియు ప్లాట్‌ఫారమ్ మద్దతు కోసం [Foundry Local డాక్యుమెంటేషన్](https://foundrylocal.ai) చూడండి.

## పాఠం 8 (Bing Grounding Workflow) కోసం అదనపు సెటప్


పాఠం 8 లోని షరతుల ప్రేరిత పని పుస్తకం Microsoft Foundry ద్వారా **Bing గ్రౌండింగ్** ను ఉపయోగిస్తుంది. మీరు ఆ నమూనాను నడపాలని ప్లాన్ చేస్తే, ఈ వేరియబుల్ ను మీ `.env` ఫైల్‌లో జోడించండి:

| వేరియబుల్ | ఎక్కడ కనుగొనాలి |
|----------|-----------------|
| `BING_CONNECTION_ID` | Microsoft Foundry పోర్టల్ → మీ ప్రాజెక్ట్ → **Management** → **Connected resources** → మీ Bing కనెక్షన్ → కనెక్షన్ IDని కాపీ చేయండి |

## సమస్య పరిష్కారం

### macOS పై SSL సర్టిఫికెట్ ధృవీకరణ లోపాలు

మీరు macOS పై ఉంటే మరియు క్రింది లాంటి లోపాన్ని ఎదుర్కుంటే:

```plaintext
ssl.SSLCertVerificationError: [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: self-signed certificate in certificate chain
```

ఇది macOSపై Pythonకి సంబంధించిన తెలిసిన సమస్య, ఎక్కడ సిస్టమ్ SSL సర్టిఫికెట్లను ఆటోమేటిక్‌గా నమ్మదు. కింది పరిష్కారాలను క్రమంగా ప్రయత్నించండి:

**వికల్పం 1: Python యొక్క Install Certificates స్క్రిప్ట్ ని నడపండి (సిఫారసు చేయబడింది)**

```bash
# మీ ఇన్‌స్టాల్ చేసిన Python వెర్షన్‌తో 3.XX ను మార్చండి (ఉదా., 3.12 లేదా 3.13):
/Applications/Python\ 3.XX/Install\ Certificates.command
```

**వికల్పం 2: మీ నోట్బుక్‌లో `connection_verify=False` ఉపయోగించండి (GitHub Models నోట్బుక్స్ కోసం మాత్రమే)**

పాఠం 6 నోట్బుక్ (`06-building-trustworthy-agents/code_samples/06-system-message-framework.ipynb`) లో, ఒక వ్యాఖ్యాన చేస్త ఉన్న వర్క్ అరౌండ్ ఇప్పటికే ఉంది. క్లయింట్ సృష్టిస్తున్నప్పుడు `connection_verify=False` ను వ్యాఖ్యా లేకుండా చేయండి:

```python
client = ChatCompletionsClient(
    endpoint=endpoint,
    credential=AzureKeyCredential(token),
    connection_verify=False,  # సర్టిఫికెట్ లోపాలు ఎదురైనప్పుడు SSL నిర్ధారణను డిసేబుల్ చేయండి
)
```

> **⚠️ హెచ్చరిక:** SSL ధృవీకరణను నిష్క్రియం చేయడం (`connection_verify=False`) సర్టిఫికెట్ చెల్లింపును ఎగవేసి భద్రతను తగ్గిస్తుంది. దీన్ని డెవలప్మెంట్ వాతావరణాల్లో తాత్కాలిక పరిష్కారంగా మాత్రమే ఉపయోగించండి, ఉత్పత్తి వాతావరణంలో ఎప్పుడూ కాదు.

**వికల్పం 3: `truststore` ని ఇన్‌స్టాల్ చేసి ఉపయోగించండి**

```bash
pip install truststore
```

ఆపై మీ నోట్బుక్ లేదా స్క్రిప్ట్ లో ఎటువంటి నెట్‌వర్క్ కాల్స్ జరగక ముందు క్రింద చెప్పినది జత చేయండి:

```python
import truststore
truststore.inject_into_ssl()
```

## ఏదైనా আটకిపోయారా?

ఈ సెటప్ నడ‌పడంలో మీకు ఏదైనా సమస్యలు ఉంటే, మా <a href="https://discord.gg/kzRShWzttr" target="_blank">Azure AI Community Discord</a> లో చేరండి లేదా <a href="https://github.com/microsoft/ai-agents-for-beginners/issues?WT.mc_id=academic-105485-koreyst" target="_blank">ఒక ఇష్యూ సృష్టించండి</a>.

## తదుపరి పాఠం

మీరు ఇప్పుడు ఈ కోర్సు కోసం కోడ్ నడపడానికి సిద్ధంగా ఉన్నారు. AI ఏజెంట్స్ ప్రపంచం గురించి మరింత నేర్చుకోవడానికి సంతోషంగా ఉండండి!

[AI ఏజెంట్స్ మరియు ఏజెంట్ ఉపయోగ సందర్భాలకి పరిచయం](../01-intro-to-ai-agents/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**అస్వీకరణ**:
ఈ పత్రం AI అనువాద సేవ [Co-op Translator](https://github.com/Azure/co-op-translator) ఉపయోగించి అనువదించబడింది. మేము ఖచ్చితత్వానికి ప్రయత్నిస్తున్నప్పటికీ, ఆటోమేటెడ్ అనువాదాలు తప్పులు లేదా అసమగ్రతలను కలిగి ఉండవచ్చు. దాని స్వదేశ భాషలో ఉన్న అసలు పత్రాన్ని అధికారం కలిగిన మూలంగా పరిగణించాలి. కీలకమైన సమాచారం కోసం, ప్రొఫెషనల్ మానవ అనువాదాన్ని సిఫారసు చేస్తాము. ఈ అనువాదం ఉపయోగం వల్ల కలిగే ఏవైనా అపార్థాలు లేదా తప్పుదారులు కోసం మేము బాధ్యత వహించము.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->