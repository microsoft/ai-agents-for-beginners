# కోర్సు సెటప్

## పరిచయం

ఈ పాఠం ఈ కోర్సు యొక్క కోడ్ ఉదాహరణలను ఎలా నడపాలో వివరించబోతుంది.

## ఇతర విద్యార్థులతో కలసి సహాయం పొందండి

మీ రిపొను క్లోన్ చేయడం ప్రారంభించే ముందు, సెటప్ కోసం ఏదైనా సహాయం లేదా కోర్సు గురించి ప్రశ్నలు లేదా ఇతర విద్యార్థులతో కలవడానికి [AI Agents For Beginners Discord ఛానెల్](https://aka.ms/ai-agents/discord) లో చేరండి.

## ఈ రిపోను క్లోన్ లేదా ఫోర్క్ చేయండి

ప్రారంభించడానికి, GitHub రిపోజిటరీని క్లోన్ లేదా ఫోర్క్ చేయండి. అలా చేయడం ద్వారా మీరు కోర్సు మెటీరియల్ యొక్క మీ స్వంత కాపీని సృష్టించి, కోడ్‌ను నడపడం, పరీక్షించడం మరియు సవరించుకోవచ్చు!

ఇది <a href="https://github.com/microsoft/ai-agents-for-beginners/fork" target="_blank">రిపోను ఫోర్క్ చేయడానికి</a> లింక్‌పై క్లిక్ చేసి చేయవచ్చు

ఇప్పుడు ఈ కోర్సు యొక్క మీ స్వంత ఫోర్క్ వర్షన్ ఈ క్రింది లింకులో ఉందని మీరు చూసుకోగలరు:

![Forked Repo](../../../translated_images/te/forked-repo.33f27ca1901baa6a.webp)

### శాలో క్లోన్ (వర్క్‌షాప్ / కోడ్స్‌పేస్‌ల కోసం సిఫార్సు చేయబడింది)

  >పూర్తి రిపోజిటరీ పెద్దదిగా ఉండవచ్చు (~3 GB) అన్ని ఫైళ్ల పూర్తి చరిత్రను డౌన్‌లోడ్ చేస్తే. మీరు వర్క్‌షాప్ అటెండ్ చేస్తుంటే లేదా కొన్ని పాఠాల ఫోల్డర్లే కావాలంటే, శలో క్లోన్ (లేదా స్పార్‌సు క్లోన్) చాలా తక్కువ డౌన్‌లోడ్ చేస్తుంది.

#### త్వరిత శాలో క్లోన్ — కనిష్ట చరిత్ర, అన్ని ఫైళ్లతో

దిగువ ఆజ್ಞలన్లో `<your-username>` ను మీ ఫోర్క్ URL తో (లేదా మీరు ఇష్టపడ్డ upstream URL తో) మార్చండి.

కేవలం తాజా కమిట్ చరిత్రను క్లోన్ చేయడానికి (సన్నని డౌన్‌లోడ్):

```bash
git clone --depth 1 https://github.com/<your-username>/ai-agents-for-beginners.git
```

ఒక నిర్దిష్ట బ్రాంచ్‌ను క్లోన్ చేయడానికి:

```bash
git clone --depth 1 --branch <branch-name> https://github.com/<your-username>/ai-agents-for-beginners.git
```

#### భాగశః (స sparse) క్లోన్ — కనిష్ట బ్లాబ్స్ + ఎంపిక చేయబడిన ఫోల్డర్లు మాత్రమే

ఇది పార్టియల్ క్లోన్ మరియు స్పార్స్-చెకౌట్ ఉపయోగిస్తుంది (Git 2.25+ అవసరం మరియు పార్టియల్ క్లోన్ మద్దతు ఉన్న ఆధునిక Git సిఫార్సు చేయబడింది):

```bash
git clone --depth 1 --filter=blob:none --sparse https://github.com/<your-username>/ai-agents-for-beginners.git
```

రిపో ఫోల్డర్‌లో ప్రవేశించండి:

```bash
cd ai-agents-for-beginners
```

అప్పుడు మీరు కావలసిన ఫోల్డర్లను పేర్కొనండి (కింది ఉదాహరణ రెండు ఫోల్డర్లను చూపిస్తుంది):

```bash
git sparse-checkout set 00-course-setup 01-intro-to-ai-agents
```

క్లోన్ చేసి ఫైళ్లను ధృవీకరించిన తర్వాత, మీరు కేవలం ఫైళ్లే కావాలనుకుంటే మరియు స్థలాన్ని ఖాళీ చేయాలనుకుంటే (ఏ git చరిత్ర అవసరం లేదు) దయచేసి రిపోజిటరీ మెటాడేటాను తొలగించండి (💀 తిరిగి రానిది — మీరు అన్ని Git ఫంక్షనాలిటీని కోల్పోతారు):

```bash
# జెడ్‌ఎస్‌ఎష్/బాష్
rm -rf .git
```

```powershell
# పవర్‌షెల్
Remove-Item -Recurse -Force .git
```

#### GitHub Codespaces ఉపయోగించడం (స్థానిక పెద్ద డౌన్లోడ్లను నివారించడానికి సిఫార్సు చేయబడింది)

- ఈ రిపో కోసం [GitHub UI](https://github.com/codespaces) ద్వారా కొత్త Codespace సృష్టించండి.  

- కొత్తగా సృష్టించిన codespace టెర్మినల్ లో, పై శాలో/స sparse క్లోన్ ఆజ్ఞలను నడిపి మీరు కావలసిన పాఠాల ఫోల్డర్లు మాత్రమే Codespace వర్క్‌స్పేస్‌కి తెరవండి.
- ఆప్షనల్: Codespacesలో క్లోన్ చేసిన తర్వాత, అదనపు స్థలాన్ని పొందడానికి .git ను తొలగించండి (మీరూ పై తొలగింపు ఆజ్ఞలను చూడండి).
- గమనిక: మీరు రిపోను నేరుగా Codespacesలో తెరవాలని ఇష్టపడితే (మరొక క్లోన్ లేకుండానే), Codespaces devcontainer వాతావరణాన్ని నిర్మిస్తుంది మరియు మీరు అవసరం కంటే ఎక్కువ ప్రొవిజనింగ్ చేయవచ్చు.

#### సూచనలు

- ఎడిట్ / కమిట్ చేయదలచినా క్లోన్ URL ను మీ ఫోర్క్ URL తో ఎప్పుడూ మార్చండి.
- తర్వాత మీరు ఎక్కువ చరిత్ర లేదా ఫైళ్లు కావాలనుకుంటే, వాటిని fetch చేయవచ్చు లేదా స్పార్స్-చెకౌట్ సెట్ చేసి అదనపు ఫోల్డర్లను చేర్చవచ్చు.

## కోడ్ నడపడం

ఈ కోర్సు Jupyter Notebooks సిరీస్‌ని అందిస్తుంది, వాటితో మీరు AI ఏజెంట్లను నిర్మించడంలో ప్రాక్టికల్ అనుభవం పొందవచ్చు.

కోడ్ ఉదాహరణలు **Microsoft Agent Framework (MAF)** ను ఉపయోగిస్తాయి `FoundryChatClient` తో, ఇది **Microsoft Foundry Agent Service V2** (Responses API) తో **Microsoft Foundry** ద్వారా కనెక్ట్ అవుతుంది.

అన్ని Python notebooks `*-python-agent-framework.ipynb` అని లేబులై ఉంటాయి.

## అవసరాలు

- Python 3.12+
  - **గమనిక**: మీరు Python3.12 ఇన్‌స్టాల్ చేయకపోతే, దాన్ని ఖచ్చితంగా ఇన్‌స్టాల్ చేయండి. తరువాత python3.12 ఉపయోగించి venv సృష్టించండి, తద్వారా requirements.txt ఫైల్ నుండి సరైన వెర్షన్లు ఇన్‌స్టాల్ అవుతాయి.
  
    >ఉదాహరణ

    Python వర్చువల్ ఎన్విరాన్‌మెంట్ డైరక్టరీ సృష్టించండి:

    ```bash
    python -m venv venv
    ```

    తర్వాత venv ఎన్విరాన్‌మెంట్ ను యాక్టివేట్ చేయండి:

    ```bash
    # zsh/bash
    source venv/bin/activate
    ```
  
    ```dos
    # Command Prompt for Windows
    venv\Scripts\activate
    ```

- .NET 10+: .NET ఉపయోగించే నమూనా కోడ్‌లకు, [.NET 10 SDK](https://dotnet.microsoft.com/download/dotnet/10.0) లేదా తరువాతి వెర్షన్‌ను ఇన్‌స్టాల్ చేయండి. తర్వాత మీ ఇన్‌స్టాల్ చేసిన .NET SDK వెర్షన్‌ను తనిఖీ చేయండి:

    ```bash
    dotnet --list-sdks
    ```

- **Azure CLI** — ప్రామాణీకరణకు అవసరం. [aka.ms/installazurecli](https://aka.ms/installazurecli) నుండి ఇన్‌స్టాల్ చేయండి.
- **Azure సభ్యత్వం** — Microsoft Foundry మరియు Microsoft Foundry Agent Service కి ప్రాప్యత కోసం.
- **Microsoft Foundry ప్రాజెక్ట్** — ఒక ప్రాజెక్ట్ డిప్లాయ్ చేసిన మోడల్ తో (ఉదా: `gpt-5-mini`). క్రింది [Step 1](#దశ-1-microsoft-foundry-ప్రాజెక్ట్-సృష్టించండి) చూడండి.

ఈ రిపోజిటరీ రూట్‌లో కోడ్ ఉదాహరణలు నడిపేందుకు అవసరమైన అన్ని Python ప్యాకేజీలను కలిగిన `requirements.txt` ఫైలు చేర్చబడింది.

వాటిని ఇన్‌స్టాల్ చేయడానికి ఈ క్రింది ఆజ్ఞను రిపొ రూట్ లో మీ టెర్మినల్ లో నడిపండి:

```bash
pip install -r requirements.txt
```

ఇలాంటి పోటీ సమస్యలు మరియు సమస్యలను నివారించడానికి Python వర్చువల్ ఎన్విరాన్‌మెంట్ సృష్టించాలని మేము సిఫార్సు చేస్తాము.

## VSCode సెటప్

మీరు VSCodeలో సరైన Python వెర్షన్ ఉపయోగిస్తున్నదాని నిర్ధారణ చేయండి.

![image](https://github.com/user-attachments/assets/a85e776c-2edb-4331-ae5b-6bfdfb98ee0e)

## Microsoft Foundry మరియు Microsoft Foundry Agent Service సెటప్ చేయండి

### దశ 1: Microsoft Foundry ప్రాజెక్ట్ సృష్టించండి

మీరు నోట్బుక్స్ నడపడానికి మోడల్ డిప్లాయ్ చేసిన Microsoft Foundry **హబ్** మరియు **ప్రాజెక్ట్** అవసరం.

1. [ai.azure.com](https://ai.azure.com) కు వెళ్లి మీ Azure ఖాతాతో సైన్ ఇన్ అవండి.
2. ఒక **హబ్** సృష్టించండి (లేదా ఉన్నదానిని ఉపయోగించండి). చూడండి: [Hub resources overview](https://learn.microsoft.com/azure/ai-foundry/concepts/ai-resources).
3. హబ్ లో **ప్రాజెక్ట్** సృష్టించండి.
4. **Models + Endpoints** → **Deploy model** నుండి ఒక మోడల్ (ఉదా: `gpt-5-mini`) ను డిప్లాయ్ చేయండి.

### దశ 2: మీ ప్రాజెక్ట్ ఎండ్‌పాయింట్ మరియు మోడల్ డిప్లాయ్‌మెంట్ పేరు పొందండి

Microsoft Foundry పోర్టల్ లో మీ ప్రాజెక్ట్ నుంచి:

- **Project Endpoint** — **Overview** పేజీకి వెళ్లి ఎండ్‌పాయింట్ URL ను కాపీ చేసుకోండి.

![Project Connection String](../../../translated_images/te/project-endpoint.8cf04c9975bbfbf1.webp)

- **Model Deployment Name** — **Models + Endpoints**కి వెళ్లి మీరు డిప్లాయ్ చేసిన మోడల్ ఎంచుకుని, **Deployment name** గమనించుకోండి (ఉదా: `gpt-5-mini`).

### దశ 3: `az login` తో Azureలో సైన్ ఇన్ అవ్వండి

చాలా నోట్బుక్స్ **Azure CLI సైన్ ఇన్** ద్వారా ప్రామాణీకరించబడతాయి — `azure-identity` ప్యాకేజీ నుండి `AzureCliCredential` లేదా `DefaultAzureCredential` (రెండూ మీ `az login` సెషన్‌ను ఉపయోగిస్తాయి) ఉపయోగించి — అందువల్ల API కీలు అవసరం ఉండవు. కొన్ని పాఠాలు మరియు ఐచ్ఛిక ఇంటిగ్రేషన్లు API కీలు ఉపయోగిస్తాయి; ప్రతి పాఠం ఆవశ్యకతలను తనిఖీ చేయండి. దీనికి మీరు Azure CLI ద్వారా సైన్ ఇన్ అయి ఉండాలి.

1. మీరు ఇంకా ఇన్‌స్టాల్ చేయకపోతే **Azure CLI ఇన్‌స్టాల్ చేయండి**: [aka.ms/installazurecli](https://aka.ms/installazurecli)

2. **సైన్ ఇన్** చేయడానికి ఈ ఆజ్ఞను నడిపండి:

    ```bash
    az login
    ```

    లేదా మీరు రిమోట్/కోడ్స్‌పేస్ ఎదుర్గల వాతావరణంలో ఉంటే బ్రౌజర్ లేకుండా:

    ```bash
    az login --use-device-code
    ```

3. **మీ సభ్యత్వం ఎంచుకోండి** (అవసరమనిపిస్తే) — మీ Foundry ప్రాజెక్ట్ ఉన్నదాన్ని ఎంచుకోండి.

4. మీరు సైన్ ఇన్ అయి ఉందో లేదో ధృవీకరించండి:

    ```bash
    az account show
    ```

> **ఎందుకు `az login`?** నోట్బుక్స్ `AzureCliCredential` (లేదా `DefaultAzureCredential`, మీ Azure CLI సైన్ ఇన్ తీసుకునే) ను ఉపయోగించి ప్రామాణీకరణ చేస్తాయి. అంటే, మీ Azure CLI సెషన్ క్రెడెన్షియల్స్ అందిస్తుంది — మీ `.env` ఫైల్‌లో API కీలు లేదా సీక్రెట్స్ అవసరం లేవు. ఇది ఒక [భద్రతా ఉత్తమ ప్రవర్తన](https://learn.microsoft.com/azure/developer/ai/keyless-connections).

### దశ 4: మీ `.env` ఫైల్ సృష్టించండి

నమూనా ఫైల్‌ను కాపీ చేయండి:

```bash
# జెడ్‌ష్/బాష్
cp .env.example .env
```

```powershell
# పవర్‌షెల్
Copy-Item .env.example .env
```

`.env` ఫైల్ ను తెరవండి మరియు ఈ రెండు విలువలు నింపండి:

```env
AZURE_AI_PROJECT_ENDPOINT=https://<your-project>.services.ai.azure.com/api/projects/<your-project-id>
AZURE_AI_MODEL_DEPLOYMENT_NAME=gpt-5-mini
```

| వేరియబుల్ | ఎక్కడ దొరుకుతుంది |
|----------|-----------------|
| `AZURE_AI_PROJECT_ENDPOINT` | Foundry పోర్టల్ → మీ ప్రాజెక్ట్ → **Overview** పేజీ |
| `AZURE_AI_MODEL_DEPLOYMENT_NAME` | Foundry పోర్టల్ → **Models + Endpoints** → మీ డిప్లాయ్ చేసిన మోడల్ పేరు |

బాకీ బహుళ పాఠాల కోసం ఇదే సరిపోతుంది! నోట్బుక్స్ మీ `az login` సెషన్ ద్వారా ఆటోమేటిక్ ప్రామాణీకరణ చేస్తాయి.

### దశ 5: Python ఆధారాలను ఇన్‌స్టాల్ చేయండి

```bash
pip install -r requirements.txt
```

మీరు దీన్ని ముందుగా సృష్టించిన వర్చువల్ ఎన్విరాన్‌మెంట్‌లో నడపాలని మేము సిఫార్సు చేస్తాము.

## ఐచ్ఛిక సెటప్: Azure AI Search (పాఠాలు 5 మరియు 16)

పాఠం 5 (Agentic RAG) మరియు పాఠం 16 నోట్బుక్స్ డిఫాల్ట్ గా **ఇన్-మెమరీ నాలెడ్జ్ బేస్** తో నడుస్తాయి — అదనపు Azure వనరులు అవసరం లేవు. మీరు వాటిని నిజమైన **Azure AI Search** ఇండెక్స్ తో బ్యాక్ చేయాలనుకుంటే, గమనించండి పాఠం 16 నోట్బుక్ ప్రస్తుతానికి కీల ఆధారిత ప్రామాణీకరణను ఉపయోగిస్తుంది: ఇది ఇన్-మెమరీ సెర్చ్ నుండి Azure AI Search కి మారుతుంది అప్పుడే, మీరు రెండు `AZURE_SEARCH_SERVICE_ENDPOINT` మరియు `AZURE_SEARCH_API_KEY` సెట్ చేసినపుడు మాత్రమే, లేకపోతే ఇన్-మెమరీ సెర్చ్ చేతిరిగిపోదు — కాబట్టి నిజమైన ఇండెక్స్ పై నడిపించాలంటే అడ్మిన్ కీ కూడా సెట్ చేయాలి. కీ రహిత ప్రామాణీకరణ Microsoft Entra ID (RBAC) ఉపయోగించే దారిది, ఇది ఈ కోర్సులోని అన్ని ఇతర చోట్ల ఉపయోగించే `az login` ఫ్లోకి అనుగుణంగా ఉంది.

క్రింద ఉన్న RBAC దశలు సెటప్-గైడ్ نمూనాలకు మరియు మీ స్వంత కోడ్ కి వర్తిస్తాయి. అవి పాఠం 16 నోట్బుక్ లో కీల లేని ప్రామాణీకరణను ఎనేబుల్ చేయవు; పాఠం 16 లో Azure AI Search ఉపయోగించడానికి ఎండ్‌పాయింట్ మరియు అడ్మిన్ కీ రెండూ అవసరం.

1. మీ సెర్చ్ సర్వీస్ పై **రోల్-ఆధారిత యాక్సెస్ ఎనేబుల్ చేయండి**:

    ```bash
    az search service update --name <service-name> --resource-group <resource-group> --auth-options aadOrApiKey
    ```

2. మీకు కావలసిన రోల్స్ అపాయింట్ చేయండి (ఇండెక్స్ సృష్టించడం/లోడ్ చేయడం మరియు క్వెరీ చేయడం):

    ```bash
    az role assignment create --assignee <your-user-or-principal-id> --role "Search Service Contributor" --scope $(az search service show -g <resource-group> -n <service-name> --query id -o tsv)
    az role assignment create --assignee <your-user-or-principal-id> --role "Search Index Data Contributor" --scope $(az search service show -g <resource-group> -n <service-name> --query id -o tsv)
    ```

3. మీ `.env` ఫైల్ లో ఎండ్‌పాయింట్ ని జోడించండి:

| వేరియబుల్ | ఎక్కడ దొరుకుతుంది |
|----------|-----------------|
| `AZURE_SEARCH_SERVICE_ENDPOINT` | Azure పోర్టల్ → మీ **Azure AI Search** వనరు → **Overview** → URL |
| `AZURE_SEARCH_API_KEY` | పాఠం 16 నోట్బుక్ లో Azure AI Search కీ ఆధారిత ప్రామాణీకరణ కోసం అవసరం (ఎండ్‌పాయింట్ తో పాటు). Azure పోర్టల్ → **Settings** → **Keys** → ప్రాథమిక అడ్మిన్ కీ |

> **ఎందుకు కీరहित?** అడ్మిన్ కీలు మీ సెర్చ్ సేవకు పూర్తి రైటు యాక్సెస్ ఇస్తాయి మరియు `.env` ఫైళ్ల ద్వారా లీక్ చెందవచ్చు. RBAC తో, మీ `az login` ఐడెంటిటీ ఉపయోగిస్తారు — అదే కీరहित Entra ID నమూనా ఈ కోర్సు నోట్బుక్స్ ఉపయోగిస్తున్నది (`AzureCliCredential` / `DefaultAzureCredential` ద్వారా). చూడండి [Connect to Azure AI Search using roles](https://learn.microsoft.com/azure/search/search-security-rbac).

పూర్తి ఇండెక్స్-సృష్టి నమూనాల కోసం [Azure AI Search సెటప్ గైడ్](./AzureSearch.md) చూడండి Python మరియు .NET లలో.

## ఏజెంట్స్ 6 మరియు 8 నేరుగా Azure OpenAI కి కాల్ చేసే పాఠాల కోసం అదనపు సెటప్

పాఠాల 6 మరియు 8 లో కొన్ని నోట్బుక్స్ Microsoft Foundry ప్రాజెక్ట్ ద్వారా కాకుండా నేరుగా **Azure OpenAI** (Responses API) ని ఉపయోగిస్తాయి. ఈ నమూనాలు గతంలో GitHub Models ఉపయోగించేవి, అది అంత మాట్లాడుతూ Responses API ని మద్దతు ఇవ్వదు మరియు ఇది డిప్రికేటెడ్. ఈ వేరియబుల్స్‌ని మీ `.env` ఫైల్ లో జోడించండి:

| వేరియబుల్ | ఎక్కడ దొరుకుతుంది |
|----------|-----------------|
| `AZURE_OPENAI_ENDPOINT` | Azure పోర్టల్ → మీ **Azure OpenAI** వనరు → **Keys and Endpoint** → ఎండ్‌పాయింట్ (ఉదా: `https://<your-resource>.openai.azure.com`) |
| `AZURE_OPENAI_DEPLOYMENT` | మీరు డిప్లాయ్ చేసిన మోడల్ పేరు (ఉదా: `gpt-5-mini`) ఇది Responses API ని మద్దతు ఇవ్వాలి |
| `AZURE_OPENAI_API_KEY` | ఐచ్ఛికం — మీరు `az login` / Entra ID కంటే కీ ఆధారిత ప్రామాణీకరణ ఉపయోగిస్తే మాత్రమే |

> Responses API స్థిరమైన `/openai/v1/` ఎండ్‌పాయింట్ ఉపయోగిస్తుంది, కాబట్టి `api-version` అవసరం లేదు. `az login` తో సైన్ ఇన్ అయి కీరలేని Entra ID ప్రామాణీకరణ ఉపయోగించండి.

## ప్రత్యామ్నాయ ప్రొవైడర్: MiniMax (OpenAI-కంపాటిబుల్)

[MiniMax](https://platform.minimaxi.com/) పెద్ద కాంటెక్స్ట్ మోడల్స్ ( 최대 204K tokens) ను OpenAI-కంపాటిబుల్ API ద్వారా అందిస్తుంది. Microsoft Agent Framework లోని `OpenAIChatClient` OpenAI-కంపాటిబుల్ ఎండ్‌పాయింట్ తో పని చేస్తుంది కాబట్టి, మీరు `OpenAIChatClient` ఉపయోగించే పాఠాలకు MiniMax ని ప్రత్యామ్నాయంగా ఉపయోగించవచ్చు.

ఈ వేరియబుల్స్‌ను మీ `.env` ఫైల్ లో జోడించండి:

| వేరియబుల్ | ఎక్కడ దొరుకుతుంది |
|----------|-----------------|
| `MINIMAX_API_KEY` | [MiniMax Platform](https://platform.minimaxi.com/) → API కీలు |
| `MINIMAX_BASE_URL` | `https://api.minimax.io/v1` (డిఫాల్ట్ విలువ) ఉపయోగించండి |
| `MINIMAX_MODEL_ID` | వాడదలచిన మోడల్ పేరు (ఉదా: `MiniMax-M3`) |

**ఉదాహరణ మోడళ్ళు**: `MiniMax-M3` (సిఫార్సు చేసినది), `MiniMax-M2.7`, `MiniMax-M2.7-highspeed` (వేగంగా స్పందనలు). మోడల్ పేర్లు మరియు లభ్యత కాలానుగుణంగా మారవచ్చు, మరియు ప్రతి మోడల్ యాక్సెస్ మీ ఖాతాపై ఆధారపడుతుంది.

`OpenAIChatClient` ఉపయోగించే కోడ్ ఉదాహరణలు (ఉదా: పాఠం 14 హోటల్ బుకింగ్ వర్క్‌ఫ్లో) `MINIMAX_API_KEY` సెట్ అయినపుడు మీ MiniMax కాన్ఫిగరేషన్ ను స్వయంచాలకంగా గుర్తించి ఉపయోగిస్తాయి.


## ప్రత్యామ్నాయ ప్రొవైడర్: Novita AI (OpenAI-అనుకూలం)

[Novita AI](https://novita.ai/llm-api) ఓపెన్-సోర్స్ మరియు ఫ్రంటియర్ LLMs (DeepSeek, Llama, Qwen, మరియు మరిన్ని) కోసం OpenAI-అనుకూల APIని అందిస్తుంది. Microsoft Agent Framework యొక్క `OpenAIChatClient` ఏ OpenAI-అనుకూల ఎండ్పాయింట్‌తో పని చేస్తుంది కాబట్టి, మీరు Novita AIని Azure OpenAI లేదా OpenAIకి ప్రత్యామ్నాయంగా ఉపయోగించవచ్చు.

ఈ వేరియబుల్స్‌ను మీ `.env` ఫైల్‌లో చేర్చండి:

| వేరియబుల్ | ఎక్కడ కనుగొనాలి |
|----------|-----------------|
| `NOVITA_API_KEY` | [Novita AI డాష్‌బోర్డు](https://novita.ai/settings/key-management) → API కీలు |
| `NOVITA_BASE_URL` | `https://api.novita.ai/openai/v1` ఉపయోగించండి (డిఫాల్ట్ విలువు) |
| `NOVITA_MODEL_ID` | ఉపయోగించవలసిన మోడల్ పేరు (ఉదాహరణకు, `moonshotai/kimi-k3`) |

**ఉదాహరణ మోడల్స్**: `moonshotai/kimi-k3`, `zai-org/glm-5.2`, `deepseek/deepseek-v4-flash-0731`. Novita AI మరెన్నో ఓపెన్-సోర్స్ మోడల్ కుటుంబాలను (Llama, Qwen, GLM, మరియు మరిన్ని) కూడా ఆతిథ్యం ఇస్తుంది — ప్రస్తుతం అందుబాటులో ఉన్న మోడల్స్ మరియు వారి మోడల్ IDs కోసం [Novita AI మోడల్ లైబ్రరీ](https://novita.ai/llm-api)ను చూడండి.

ప్రస్తుత సాంపిళ్లు ఆటోమాటిక్‌గా `NOVITA_*` వేరియబుల్స్‌ని ఉపయోగించవు. Novita AI ఉపయోగించాలంటే మీరు పాసు చేస్తున్న `OpenAIChatClient`లో ఈ విలువలను స్పష్టంగా అందించాలి.

## ప్రత్యామ్నాయ ప్రొవైడర్: Foundry Local (డివైస్ పై మోడల్స్ నడుపండి)

[Foundry Local](https://foundrylocal.ai) ఒక లైట్‌వెయిట్ రన్‌టైమ్, ఇది భాషా మోడల్స్‌ని **మీ స్వంత యంత్రంలో పూర్తి స్థాయిలో** డౌన్లోడ్ చేసి, నిర్వహించి, OpenAI-అనుకూల API ద్వారా అందిస్తుంది — క్లౌడ్ అవసరం లేదు.

Microsoft Agent Framework యొక్క `OpenAIChatClient` ఏ OpenAI-అనుకూల ఎండ్పాయింట్‌తో పని చేయగలుగుతుందని, Foundry Local Azure OpenAIకి స్థానిక ప్రత్యామ్నాయం.

**1. Foundry Localని ఇన్‌స్టాల్ చేయండి**

```bash
# విండోస్
winget install Microsoft.FoundryLocal

# మాక్OS
brew install foundrylocal
```

**2. ఒక మోడల్ డౌన్లోడ్ చేసి నడపండి** (ఇది స్థానిక సర్వీసును కూడా ప్రారంభిస్తుంది):

```bash
foundry model list          # అందుబాటులో ఉన్న మోడల్స్‌ను చూడండి
foundry model run phi-4-mini
```

**3. స్థానిక ఎండ్పాయింట్ కనుగొనడానికి ఉపయోగించే Python SDKని ఇన్‌స్టాల్ చేయండి:**

```bash
pip install foundry-local-sdk
```

**4. Microsoft Agent Frameworkని మీ స్థానిక మోడల్ పై చూపించండి:**

```python
from foundry_local import FoundryLocalManager
from agent_framework.openai import OpenAIChatClient

# మోడల్‌ను లోకల్గా డౌన్లోడ్ చేసి (అవసరమైతే) సేవ్ చేస్తుంది, ఆ తర్వాత ఎండ్‌పాయింట్/పోర్ట్‌ను కనుగొంటుంది.
manager = FoundryLocalManager("phi-4-mini")

chat_client = OpenAIChatClient(
    base_url=manager.endpoint,      # ఉదాహరణకు http://localhost:<port>/v1
    api_key=manager.api_key,        # Foundry Local కోసం ఎప్పుడూ "not-required"
    model_id=manager.get_model_info("phi-4-mini").id,
)

agent = chat_client.as_agent(
    name="LocalAgent",
    instructions="You are a helpful assistant running fully on-device.",
)
```

> **గమనిక:** Foundry Local OpenAI-అనుకూల **చాట్ కంప్లీషన్స్** ఎండ్పాయింట్‌ను అందిస్తుంది. స్థానిక అభివృద్ధికి మరియు ఆఫ్‌లైన్ సందర్భాల కోసం దీనిని ఉపయోగించండి. పూర్తి **ప్రతిస్పందనలు API** ఫీచర్ సెట్టు (స్థితిగత సంభాషణలు, మొదలైనవి) కోసం Azure OpenAI లేదా Microsoft Foundry ప్రాజెక్ట్ ఉపయోగించండి.

## పాఠం 8 కోసం అదనపు సెట్-అప్ (బింగ్ గ్రౌండింగ్ వర్క్‌ఫ్లో)

పాఠం 8 లో కల్గించిన షితల్ వర్క్‌ఫ్లో Microsoft Foundry ద్వారా **బింగ్ గ్రౌండింగ్** ఉపయోగిస్తుంది. ఆ సాంపిల్‌ను నడపాలనుకుంటే, ఈ వేరియబుల్‌ను మీ `.env` ఫైల్ లో చేర్చండి:

| వేరియబుల్ | ఎక్కడ కనుగొనాలి |
|----------|-----------------|
| `BING_CONNECTION_ID` | Microsoft Foundry పోర్టల్ → మీ ప్రాజెక్ట్ → **Management** → **Connected resources** → మీ Bing కనెక్షన్ → కనెక్షన్ ID ను కాపీ చేసుకోండి |

## సమస్యలు పరిష్కరణ

### macOSపై SSL సర్టిఫికెట్ ధృవీకరణ లోపాలు

మీరు macOS పై ఉంటే మరియు దీంట్లాంటి లోపం వస్తే:

```plaintext
ssl.SSLCertVerificationError: [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: self-signed certificate in certificate chain
```

ఇది macOS పై Pythonతో తెలిసిన సమస్య, అదేవిధంగా సిస్టమ్ SSL సర్టిఫికెట్లు ఆటోమాటిక్ గా నమ్మకమైనవి కావు. ఈ క్రింది పరిష్కారాలను వరుసలో ప్రయత్నించండి:

**ఎంపిక 1: Python యొక్క Install Certificates స్క్రిప్ట్ నడపండి (పరామర్శించబడింది)**

```bash
# మీ ఇన్‌స్టాల్ చేసిన Python సంస్కరణతో 3.XX ని మార్చండి (ఉదా., 3.12 లేదా 3.13):
/Applications/Python\ 3.XX/Install\ Certificates.command
```

**ఎంపిక 2: మీ నోట్‌బుక్‌లో `connection_verify=False` ఉపయోగించండి (GitHub Models నోట్‌బుక్స్‌కి మాత్రమె)**

పాఠం 6 నోట్‌బుక్ (`06-building-trustworthy-agents/code_samples/06-system-message-framework.ipynb`)లో, కామెంట్ చేయబడిన వర్క్ ఎరౌండ్ ఇప్పటికే ఉన్నాయి. సర్టిఫికెట్ లోపాలు ఎదురైనప్పుడు `connection_verify=False` ను అన్‌కామెంట్ చేయండి:

```python
client = ChatCompletionsClient(
    endpoint=endpoint,
    credential=AzureKeyCredential(token),
    connection_verify=False,  # మీరు సర్టిఫికెట్ లోపాలను ఎదుర్కుంటే SSL నిర్ధారణను ఆక్రియ చేయండి
)
```

> **⚠️ హెచ్చరిక:** SSL ధృవీకరణని ఆపివేత (`connection_verify=False`) సర్టిఫికేట్ సరైనతను ఎక్కవుగా తక్కువ చేస్తుంది. ఇది అభివృద్ధి వాతావరణాల్లో తాత్కాలిక పరిష్కారంగా మాత్రమే ఉపయోగించండి. ఉత్పత్తిలో అసలు ఉపయోగించవద్దు.

**ఎంపిక 3: `truststore`ని ఇన్‌స్టాల్ చేసి ఉపయోగించండి**

```bash
pip install truststore
```

ఆపై మీ నోట్‌బుక్ లేదా స్క్రిప్ట్ ప్రారంభంలో ఏదైనా నెట్‌వర్క్ కాల్స్ చేయకముందు క్రింది కోడ్ చేర్చండి:

```python
import truststore
truststore.inject_into_ssl()
```

## ఎక్కడో నిలిచిపోయారా?

మీరు ఈ సెటప్ నడుపుతుండగా ఏదైనా సమస్యలు ఎదురైతే, మా <a href="https://discord.gg/kzRShWzttr" target="_blank">Azure AI Community Discord</a>లో చేరండి లేదా <a href="https://github.com/microsoft/ai-agents-for-beginners/issues?WT.mc_id=academic-105485-koreyst" target="_blank">ఇష్యూ సృష్టించండి</a>.

## తదుపరి పాఠం

మీరు ఇప్పుడు ఈ కోర్సుకు అవసరమైన కోడ్ నడపడానికి సిద్ధంగా ఉన్నారు. AI ఏజెంట్ల ప్రపంచంలో మరిన్ని నేర్చుకోవడానికి సంతోషంగా ఉండండి!

[AI ఏజెంట్లకు పరిచయం మరియు ఏజెంట్ వినియోగ కేసులు](../01-intro-to-ai-agents/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**అస్వీకరణ**:
ఈ పత్రం AI అనువాద సేవ [Co-op Translator](https://github.com/Azure/co-op-translator) ఉపయోగించి అనువదించబడింది. మేము ఖచ్చితత్వానికి ప్రయత్నిస్తున్నప్పటికీ, ఆటోమేటెడ్ అనువాదాలు తప్పులు లేదా అసమగ్రతలను కలిగి ఉండవచ్చు. దాని స్వదేశ భాషలో ఉన్న అసలు పత్రాన్ని అధికారం కలిగిన మూలంగా పరిగణించాలి. కీలకమైన సమాచారం కోసం, ప్రొఫెషనల్ మానవ అనువాదాన్ని సిఫారసు చేస్తాము. ఈ అనువాదం ఉపయోగం వల్ల కలిగే ఏవైనా అపార్థాలు లేదా తప్పుదారులు కోసం మేము బాధ్యత వహించము.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->