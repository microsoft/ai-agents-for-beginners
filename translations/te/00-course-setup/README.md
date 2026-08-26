# కోర్సు సెटప్

## పరిచయం

ఈ పాఠం ఈ కోర్సు యొక్క కోడ్ నమూనాలను నడిపే విధానాన్ని వివరిస్తుంది.

## ఇతర విద్యార్థులతో చేరి సహాయం పొందండి

మీ రీపోను క్లోన్ చేయడానికి ముందే, సెటప్ గురించి సహాయం, కోర్సు విషయాల పై ఏవైనా ప్రశ్నలు లేదా ఇతర విద్యార్థులతో కనెక్ట్ కావడానికి [AI Agents For Beginners Discord చానల్](https://aka.ms/ai-agents/discord) జాయిన్ అవ్వండి.

## ఈ రీపోను క్లోన్ లేదా ఫోర్క్ చేయండి

ప్రారంభించడానికి, దయచేసి గిట్హబ్ రిపోజిటరీని క్లోన్ లేదా ఫోర్క్ చేయండి. ఇది మీకు కోర్సు మెటీరియల్ యొక్క మీ స్వంత ప్రతిని తయారుచేస్తుంది, తద్వారా మీరు కోడ్ నడపగలరు, పరీక్షించగలరు మరియు సవరించగలరు!

మీరు దీన్ని చేయడానికి <a href="https://github.com/microsoft/ai-agents-for-beginners/fork" target="_blank">ఫోర్క్ చేయడానికి ఈ లింక్</a>పై క్లిక్ చేయండి

ఇప్పుడు మీకు ఈ కోర్సు యొక్క మీ స్వంత ఫోర్క్ వెర్షన్ ఈ లింక్లో ఉండాలి:

![Forked Repo](../../../translated_images/te/forked-repo.33f27ca1901baa6a.webp)

### శాలో క్లోన్ (వరక workshop / Codespaces కోసం సిఫార్సు)

  > పూర్తిగా రిపోజిటరీ డౌన్లోడ్ చేస్తే (~3 GB) పెద్దదై ఉంటుంది, ఈతర చరిత్ర మరియు ఫైళ్ళతో. మీరు కేవలం వర్క్‌షాప్‌కు హాజరవుతున్నప్పుడు లేదా కొంత పాఠ్య ఫోల్డర్లు మాత్రమే కావలసినపుడు, శాలో క్లోన్ (లేదా స్పార్స్ క్లోన్) చాలా తక్కువ డౌన్లోడ్ చేస్తుంది.

#### క్విక్ శాలో క్లోన్ — కనీస చరిత్ర, అన్ని ఫైళ్లు

క్రింద మీరు `<your-username>` స్థానంలో మీ ఫోర్క్ URL లేదా మీరు ఇష్టపడితే అప్‌స్ట్రీమ్ URLను ఉంచండి.

మీకు తాజా కమిట్ చరిత్రను మాత్రమే డౌన్లోడ్ చేయాలంటే:

```bash
git clone --depth 1 https://github.com/<your-username>/ai-agents-for-beginners.git
```

ప్రత్యేక బ్రాంచ్‌ను క్లోన్ చేయడానికి:

```bash
git clone --depth 1 --branch <branch-name> https://github.com/<your-username>/ai-agents-for-beginners.git
```

#### పార్టీషియల్ (స్పార్స్) క్లోన్ — కనీస బ్లాబ్స్ + ఎంచుకున్న ఫోల్డర్లే

ఇది పార్టీయల్ క్లోన్ మరియు స్పార్స్-చెకౌట్ ఉపయోగిస్తుంటుంది (Git 2.25+ అవసరం మరియు పార్టీయల్ క్లోన్ మద్దతు ఉన్న ఆధునిక Git సిఫార్సు).

```bash
git clone --depth 1 --filter=blob:none --sparse https://github.com/<your-username>/ai-agents-for-beginners.git
```

రిపో ఫోల్డర్ లో ప్రవేశించండి:

```bash
cd ai-agents-for-beginners
```

మీరు కావాల్సిన ఫోల్డర్లను స్పష్టంచేయండి (కింద ఉదాహరణలో రెండు ఫోల్డర్లు చూపబడినవి):

```bash
git sparse-checkout set 00-course-setup 01-intro-to-ai-agents
```

క్లోన్ చేసి ఫైల్స్ ను ధృవీకరించిన తర్వాత, మీకు ఫైళ్లు మాత్రమే కావాలి, గిట్ చరిత్ర అవసరం లేకపోతే (అదే, డిస్క్ స్పేస్ ఉంచడానికి) రిపోజిటరీ మెటాడేటాను తవ్వండి (💀ఇది తిరిగి రాకపోవచ్చు — మీరు అన్ని Git ఫంక్షనాలిటీని కోల్పోతారు):

```bash
# జెడ్ఎస్ఎచ్/బాష్
rm -rf .git
```

```powershell
# పవర్‌షెల్
Remove-Item -Recurse -Force .git
```

#### GitHub Codespaces ఉపయోగించడం (తక్కువ లోకల్ పెద్ద డౌన్లోడ్లకు సిఫార్సు)

- ఈ రిపోకు కొత్త Codespace సృష్టించండి [GitHub UI](https://github.com/codespaces) ద్వారా.  

- సరికొత్త Codespace టెర్మినల్లో పైన ఉన్న శాలో/స్పార్స్ క్లోన్ కమాండ్లలో ఒకదాన్ని రన్ చేసి మీకు కావాల్సిన పాఠ్య ఫోల్డర్లను మాత్రమే Codespace వర్క్‌స్పేస్‌కి తీసుకురండి.
- ఐచ్ఛికం: Codespaces లోక్లోన్ చేసిన తర్వాత, అదనపు స్థానం కోసం .git నీ తీసివేయవచ్చు (పై తొలగింపు కమాండ్లను చూడండి).
- గమనిక: మీరు రిపోను నేరుగా Codespaces లో తెరవాలని ఇష్టపడితే (అదనపు క్లోన్ లేకుండానే), Codespaces డెవ్‌కంటైనర్ వాతావరణాన్ని నిర్మిస్తుంది మరియు కావాల్సినది కన్నా ఎక్కువ రిసోర్సుల్ని అమర్చవచ్చు.

#### సూచనలు

- ఎడిట్/కమిట్ చేయాలనుకుంటే, అసలు క్లోన్ URLను మీ ఫోర్క్ URLతో మార్చండి.
- తర్వాత చరిత్ర లేదా ఫైల్స్ కావాలంటే, వాటిని తీసుకోండి లేదా స్పార్స్-చెకౌట్ ద్వారా అదనపు ఫోల్డర్లను చేర్చండి.

## కోడ్ నడపడం

ఈ కోర్సు AI ఏజెంట్లను నిర్మించడంలో హ్యాండ్-ఆన్ అనుభవం పొందేందుకు జ్యుపిటర్ నోట్బుక్స్ సిరీస్‌ను అందిస్తుంది.

కోడ్ నమూనాలు **Microsoft Agent Framework (MAF)** ఉపయోగిస్తాయి, దీనిలో `FoundryChatClient` ఉంది, ఇది **Microsoft Foundry Agent Service V2** (Responses API)కి **Microsoft Foundry** ద్వారా కనెక్ట్ అవుతుంది.

అన్ని Python నోట్బుక్స్ `*-python-agent-framework.ipynb` గా లేబుల్ చేయబడ్డాయి.

## అవసరాలు

- Python 3.12+
  - **గమనిక**: మీరు Python3.12 ఇన్స్టాల్ చేయకపోతే, దయచేసి ఇన్స్టాల్ చేయండి. తరువాత, అనుకున్న వర్షన్‌లను సరైన రీతిలో ఇన్స్టాల్ చేయటానికి python3.12 ఉపయోగించి వర్చువల్ ఎన్‌విరాన్‌మెంట్ (venv) సృష్టించండి.
  
    >ఉదాహరణ

    Python వర్చువల్ ఎన్‌విరాన్‌మెంట్ డైరెక్టరీ సృష్టించండి:

    ```bash
    python -m venv venv
    ```

    తర్వాత వర్చువల్ ఎన్‌విరాన్‌మెంట్‌ను ఆక్సివ్ చేయండి:

    ```bash
    # జెడ్ఎస్ఎచ్/బ్యాష్
    source venv/bin/activate
    ```
  
    ```dos
    # Command Prompt for Windows
    venv\Scripts\activate
    ```

- .NET 10+: .NET ఉపయోగించే నమూనా కోడ్‌ల కోసం, దయచేసి [.NET 10 SDK](https://dotnet.microsoft.com/download/dotnet/10.0) లేదా కొత్త వర్షన్ ఇన్స్టాల్ చేయండి. తరువాత, మీ ఇన్స్టాల్ అయిన .NET SDK వర్షన్‌ను చెక్ చేయండి:

    ```bash
    dotnet --list-sdks
    ```

- **Azure CLI** — ఆథెంటికేషన్ కోసం అవసరం. [aka.ms/installazurecli](https://aka.ms/installazurecli) నుండి ఇన్స్టాల్ చేసుకోండి.
- **Azure Subscription** — Microsoft Foundry మరియు Microsoft Foundry Agent Service యాక్సెస్ కోసం.
- **Microsoft Foundry Project** — డిప్లాయ్ చేసిన మోడల్ కలిగిన ప్రాజెక్ట్ (ఉదా: `gpt-5-mini`). [సందర్శన 1](#స్టెప్-1-microsoft-foundry-ప్రాజెక్ట్-సృష్టించండి) చూడండి.

ఈ రిపోజిటరీ రూట్‌లో ఉన్న `requirements.txt` ఫైల్ కొడ్ నమూనాలు నడుపడానికి అవసరమైన అన్ని Python ప్యాకేజీలను కలిగి ఉంది.

మీరు రిపోజిటరీ రూట్ వద్ద కింది కమాండ్ నడుపడం ద్వారా అవి ఇన్స్టాల్ చేయవచ్చు:

```bash
pip install -r requirements.txt
```

కంప్లికేషన్‌లు మరియు గందరగోళాలు నివారించడానికి Python వర్చువల్ ఎన్‌విరాన్‌మెంట్ సృష్టించడం మేము薦సుకుంటున్నాము.

## VSCode సెటప్

VSCodeలో సరైన Python వర్షన్ ఉపయోగిస్తున్నట్లు నిర్ధారించుకోండి.

![image](https://github.com/user-attachments/assets/a85e776c-2edb-4331-ae5b-6bfdfb98ee0e)

## Microsoft Foundry మరియు Microsoft Foundry Agent Service ను సెటప్ చేయండి

### స్టెప్ 1: Microsoft Foundry ప్రాజెక్ట్ సృష్టించండి

మీరు జూపిటర్ నోట్బుక్స్ నడపడానికి ఒక Microsoft Foundry **హబ్** మరియు **ప్రాజెక్ట్** అవసరం, ఒక డిప్లాయ్ చేసిన మోడల్‌తో.

1. [ai.azure.com](https://ai.azure.com) కి వెళ్లి మీ Azure అకౌంట్ తో సైన్ ఇన్ అవ్వండి.
2. ఒక **హబ్** సృష్టించండి (లేదా యున్న ఒకటి ఉపయోగించండి). చూడండి: [హబ్ వనరుల అవగాహన](https://learn.microsoft.com/azure/ai-foundry/concepts/ai-resources).
3. హబ్ లో ఒక **ప్రాజెక్ట్** సృష్టించండి.
4. **మోడల్స్ + ఎండ్ పాయింట్లు** → **మోడల్ డిప్లాయ్ చేయండి** నుండి ఒక మోడల్ (ఉదా: `gpt-5-mini`) డిప్లాయ్ చేయండి.

### స్టెప్ 2: ప్రాజెక్ట్ ఎండ్‌పాయింట్ మరియు మోడల్ డిప్లాయ్‌మెంట్ పేరును పొందండి

Microsoft Foundry పోర్టల్ లో మీ ప్రాజెక్ట్ నుండి:

- **ప్రాజెక్ట్ ఎండ్‌పాయింట్** — **Overview** పేజీకి వెళ్లి ఎండ్పాయింట్ URL ను కాపీ చేయండి.

![Project Connection String](../../../translated_images/te/project-endpoint.8cf04c9975bbfbf1.webp)

- **మోడల్ డిప్లాయ్‌మెంట్ పేరు** — **మోడల్స్ + ఎండ్‌పాయింట్లు** లోకి వెళ్లి, డిప్లాయ్ చేసిన మోడల్ ఎంచుకొని, **డిప్లాయ్‌మెంట్ పేరు** గమనించండి (ఉదా: `gpt-5-mini`).

### స్టెప్ 3: `az login` తో Azure లో సైన్ ఇన్ అవ్వండి

ఎక్కువ భాగం నోట్బుక్స్ మీరు **Azure CLI సైన్-ఇన్** ద్వారా ఆథెంటికేట్ అవుతాయి — `azure-identity` ప్యాకేజీలోని `AzureCliCredential` లేదా `DefaultAzureCredential` (ఇవి మీ `az login` సెషన్‌ను స్వీకరిస్తాయి) ఉపయోగించి — అందువల్ల API కీలు అవసరం ఉండవు. కొన్ని పాఠ్యాలు మరియు ఐచ్చిక ఇంటిగ్రేషన్లు API కీలు ఉపయోగిస్తాయి; ఆ పాఠ్యాల ముందస్తు అవసరాలు చెక్ చేయండి. దీని కోసం మీరు Azure CLI ద్వారా సైన్ ఇన్ అయి ఉండాలి.

1. **Azure CLI ఇన్స్టాల్ చేయండి**: [aka.ms/installazurecli](https://aka.ms/installazurecli)

2. **సైన్ ఇన్** చేయడానికి ఈ కమాండ్ నడపండి:

    ```bash
    az login
    ```

    లేదా, మీరు రిమోట్/Codespace వాతావరణంలో బ్రౌజర్ లేకపోతే:

    ```bash
    az login --use-device-code
    ```

3. మీరు ప్రాంప్ట్ అయితే మీ సబ్‌స్క్రిప్షన్ ఎంచుకోండి — మీ Foundry ప్రాజెక్ట్ ఉన్నదాన్ని ఎంచుకోండి.

4. మీ సైన్ ఇన్ అయినది ధృవీకరించండి:

    ```bash
    az account show
    ```

> **`az login` ఎందుకు?** నోట్బుక్స్ `azure-identity`లోని `AzureCliCredential` (లేదా `DefaultAzureCredential`) ద్వారా ఆథెంటికేట్ అవుతాయి, ఇవి మీ Azure CLI సైన్ ఇన్‌ను ఉపయోగిస్తాయి. అర్థం మీరు API కీలు లేకుండా `.env` ఫైల్లో ఏ కీలు లేకుండానే ప్రవేశించవచ్చు. ఇది ఒక [భద్రత ఉత్తమ అభ్యాసం](https://learn.microsoft.com/azure/developer/ai/keyless-connections).

### స్టెప్ 4: మీ `.env` ఫైల్ సృష్టించండి

ఉదాహరణ ఫైల్‌ను కాపీ చేయండి:

```bash
# zsh/bash
cp .env.example .env
```

```powershell
# పవర్‌షెల్
Copy-Item .env.example .env
```

`.env` తెరిచి ఈ రెండు విలువలను నింపండి:

```env
AZURE_AI_PROJECT_ENDPOINT=https://<your-project>.services.ai.azure.com/api/projects/<your-project-id>
AZURE_AI_MODEL_DEPLOYMENT_NAME=gpt-5-mini
```

| వేరియబుల్ | ఎక్కడి నుంచి పొందాలి |
|----------|-----------------|
| `AZURE_AI_PROJECT_ENDPOINT` | Foundry పోర్టల్ → మీ ప్రాజెక్ట్ → **Overview** పేజీ |
| `AZURE_AI_MODEL_DEPLOYMENT_NAME` | Foundry పోర్టల్ → **Models + Endpoints** → మీ డిప్లాయ్ చేసిన మోడల్ పేరు |

ఎక్కువ భాగం పాఠాల కోసం ఇది చాలు! నోట్బుక్స్ మీ `az login` సెషన్ ద్వారా ఆటోమేటిక్‌గా ఆథెంటికేట్ అవుతాయి.

### స్టెప్ 5: Python డిపెండెన్సీలు ఇన్స్టాల్ చేయండి

```bash
pip install -r requirements.txt
```

మేము మీరు ముందుగానే సృష్టించిన వర్చువల్ ఎన్‌విరాన్‌మెంట్ లో ఇది నడపాలని సిఫార్సు చేస్తున్నాము.

## ఐచ్ఛిక సెటప్: Azure AI Search (పాఠాలు 5 మరియు 16)

పాఠం 5 (Agentic RAG) మరియు పాఠం 16 నోట్బుక్స్ డిఫాల్ట్ గా **ఇన్-మెమరీ నాలెడ్జ్ బేస్**తో నడుస్తుంది — అదనపు Azure వనరులు అవసరం లేదు. మీరు వాటిని నిజమైన **Azure AI Search** సూచికతో బ్యాక్ చేయాలనుకుంటే గమనించండి: పాఠం 16 నోట్బుక్ ప్రస్తుతానికి కీలును ఆధారపడిన ఆథెంటికేషన్ ను ఉపయోగిస్తుంది: ఇది `AZURE_SEARCH_SERVICE_ENDPOINT` మరియు `AZURE_SEARCH_API_KEY` రెండూ సెట్ చేయబడితే మాత్రమే ఇన్-మెమరీ నుండి Azure AI Search కి మారుతుంది; లేకపోతే ఇన్-మెమరీ సెలక్షన్ ఉంటుంది — కాబట్టి నిజమైన సూచికకు ఇది నడపాలంటే అడ్మిన్ కీ కూడా ఇవ్వాలి. Microsoft Entra ID (RBAC) తో కీలుకల ఆథెంటికేషన్ మీ స్వంత ప్రొడక్షన్ కోడ్ కోసం సిఫార్సు చేయబడింది, ఇది కోర్సులోని అన్ని ప్రాంతాల్లో `az login` ఫ్లోని అనుసరిస్తుంది.

క్రింద RBAC స్టెప్పులు సెటప్-గైడ్ నమూనాలకి మరియు మీ స్వంత కోడ్ కి వర్తిస్తాయి. అవి పాఠం 16 నోట్బుక్లో కీలుకల ఆథెంటికేషన్‌ను యాక్టివేట్ చేయవు; పాఠం 16 కి అందుబాటులో ఉండాలంటే ఎండ్‌పాయింట్ మరియు అడ్మిన్ కీ రెండూ అవసరం.

1. మీ సెర్చ్ సర్వీస్‌పై **రోల్ ఆధారిత యాక్సెస్** ఎనేబుల్ చేయండి:

    ```bash
    az search service update --name <service-name> --resource-group <resource-group> --auth-options aadOrApiKey
    ```

2. అవసరమైన పాత్రలను మీకు స్వయంగా అప్పగించండి (ఇండెక్స్ సృష్టించడానికి/లోడ్ చేయడానికి మరియు క్వెరీ చేయడానికి):

    ```bash
    az role assignment create --assignee <your-user-or-principal-id> --role "Search Service Contributor" --scope $(az search service show -g <resource-group> -n <service-name> --query id -o tsv)
    az role assignment create --assignee <your-user-or-principal-id> --role "Search Index Data Contributor" --scope $(az search service show -g <resource-group> -n <service-name> --query id -o tsv)
    ```

3. మీ `.env` ఫైల్కి ఎండ్‌పాయింట్ జోడించండి:

| వేరియబుల్ | ఎక్కడి నుంచి పొందాలి |
|----------|-----------------|
| `AZURE_SEARCH_SERVICE_ENDPOINT` | Azure పోర్టల్ → మీ **Azure AI Search** వనరు → **Overview** → URL |
| `AZURE_SEARCH_API_KEY` | పాఠం 16 నోట్బుక్ లో Azure AI Search కీ ఆధారిత ఆథెంటికేషన్ కోసం అవసరం. Azure పోర్టల్ → **Settings** → **Keys** → ప్రాథమిక అడ్మిన్ కీ |

> **ఎందుకు కీలుకల?** అడ్మిన్ కీలు మీ సెర్చ్ సర్వీస్ కు పూర్తి వ్రాత యాక్సెస్ ఇస్తాయి మరియు `.env` ఫైళ్ల ద్వారా లీక్ అవ్వొచ్చు. RBAC తో, మీ `az login` ఐడెంటిటీ ఉపయోగిస్తారు — ఇదే కీలుకల Entra ID శైలీ కోర్సు నోట్బుక్స్ ఉపయోగించే విధానం (via `AzureCliCredential` / `DefaultAzureCredential`). చూడండి [Connect to Azure AI Search using roles](https://learn.microsoft.com/azure/search/search-security-rbac).

పూర్తి ఇండెక్స్ సృష్టింపు నమూనాల కోసం [Azure AI Search సెటప్ గైడ్](./AzureSearch.md) చూడండి Python మరియు .NET లో.

## మరింత సెటప్ అవసరం Azure OpenAI నేరుగా పిలవు పాఠాలకి (పాఠాలు 6 మరియు 8)

పాఠాలు 6 మరియు 8 లోని కొన్ని నోట్బుక్స్ **Azure OpenAI** ని నేరుగా (Responses API ఉపయోగించి) పిలుస్తాయి, ఇది Microsoft Foundry ప్రాజెక్ట్ ద్వారా కాదు. ఈ నమూనాలు ముందు GitHub మోడల్స్ ని ఉపయోగించాయి, అవి డిప్రికేటెడ్ అయింది మరియు Responses API కి మద్దతు ఇవ్వవు. ఈ వేరియబుల్స్ ను `.env` ఫైల్ లో చేర్చండి:

| వేరియబుల్ | ఎక్కడి నుంచి పొందాలి |
|----------|-----------------|
| `AZURE_OPENAI_ENDPOINT` | Azure పోర్టల్ → మీ **Azure OpenAI** వనరు → **Keys and Endpoint** → ఎండ్‌పాయింట్ (ఉదా: `https://<your-resource>.openai.azure.com`) |
| `AZURE_OPENAI_DEPLOYMENT` | Responses API మద్దతు ఉన్న మీ డిప్లాయ్ చేసిన మోడల్ పేరు (ఉదా: `gpt-5-mini`) |
| `AZURE_OPENAI_API_KEY` | ఐచ్చికం — మీరు `az login` / Entra ID స్థానంలో కీ ఆధారిత ఆథెంటికేషన్ ఉపయోగిస్తే మాత్రమే |

> Responses API స్థిరమైన `/openai/v1/` ఎండ్‌పాయింట్ ఉపయోగిస్తుంది, కాబట్టి `api-version` అవసరం లేదు. కర్‌లెస్ Entra ID ఆథెంటికేషన్ కోసం `az login` తో సైన్ ఇన్ అవ్వండి.

## ప్రత్యామ్నాయ ప్రొవైడర్: MiniMax (OpenAI-అనుకూలమైన)

[MiniMax](https://platform.minimaxi.com/) పెద్ద కాంటెక్స్ట్ మోడల్స్ (204K టోకెన్లు వరకు) OpenAI-సమ్మత API ద్వారా అందిస్తుంది. Microsoft Agent Framework యొక్క `OpenAIChatClient` ఏ OpenAI-సమ్మత ఎండ్‌పాయింట్ తోనైనా పని చేస్తుంది, కాబట్టి `OpenAIChatClient` ఉపయోగించే పాఠాల కోసం MiniMax ఒక ప్రత్యామ్నాయం.

ఈ వేరియబుల్స్ ను `.env` ఫైల్ లో చేర్చండి:

| వేరియబుల్ | ఎక్కడి నుంచి పొందాలి |
|----------|-----------------|
| `MINIMAX_API_KEY` | [MiniMax Platform](https://platform.minimaxi.com/) → API కీలు |
| `MINIMAX_BASE_URL` | `https://api.minimax.io/v1` (పూర్తి విలువ) ఉపయోగించండి |
| `MINIMAX_MODEL_ID` | ఉపయోగించాల్సిన మోడల్ పేరు (ఉదా: `MiniMax-M3`) |

**ఉదాహరణ మోడల్స్**: `MiniMax-M3` (సిఫార్సు చేయబడింది), `MiniMax-M2.7`, `MiniMax-M2.7-highspeed` (వేగవంతమైన ప్రతిస్పందనలు). మోడల్ పేర్లు మరియు అందుబాటు కాలం ఆధారంగా మారవచ్చు, మరియు ఖాతాపై ఆధారపడి ఉండవచ్చు.

`OpenAIChatClient` ఉపయోగించే కోడ్ నమూనాలు (ఉదా: పాఠం 14 హోటల్ బుకింగ్ వర్క్‌ఫ్లో) `MINIMAX_API_KEY` సెట్ చేసినప్పుడు మీ MiniMax కాన్ఫిగరేషన్ ని ఆటోమేటిక్ గా గుర్తించి ఉపయోగిస్తాయి.


## ప్రత్యామ్నాయ ప్రొవైడర్: Foundry Local (పరికరంపై మోడల్స్ నడపండి)

[Foundry Local](https://foundrylocal.ai) అనేది ఒక తేలికపాటి రన్‌టైమ్, ఇది భాషా మోడల్స్‌ను **మిమ్మల్ని మీరు ఉన్న యంత్రం మీదే పూర్తిగా** డౌన్‌లోడ్ చేసి, నిర్వహించి, OpenAI-తో అనుకూలమైన API ద్వారా సర్వ్ చేస్తుంది — క్లౌడ్ అవసరం లేదు.

Microsoft Agent Framework యొక్క `OpenAIChatClient` ఎలాంటి OpenAI-తో అనుకూలమైన ఎండ్‌పాయింట్‌తో పని చేస్తుంది కాబట్టి, Foundry Local అనేది Azure OpenAIకు స్థానిక ప్రత్యామ్నాయం.

**1. Foundry Local ని ఇన్‌స్టాల్ చేయండి**

```bash
# విండోస్
winget install Microsoft.FoundryLocal

# మాక్‌ఓఎస్
brew install foundrylocal
```

**2. ఒక మోడల్ డౌన్‌లోడ్ చేసి నడిపించండి** (ఇది స్థానిక సేవను కూడా ప్రారంభిస్తుంది):

```bash
foundry model list          # అందుబాటులో ఉన్న నమూనాలను చూడండి
foundry model run phi-4-mini
```

**3. స్థానిక ఎండ్‌పాయింట్‌ను కనుగొనడానికి Python SDKని ఇన్‌స్టాల్ చేయండి:**

```bash
pip install foundry-local-sdk
```

**4. Microsoft Agent Frameworkను మీ స్థానిక మోడల్ వైపు సూచించండి:**

```python
from foundry_local import FoundryLocalManager
from agent_framework.openai import OpenAIChatClient

# మోడల్‌ను లోకల్‌గా డౌన్లోడ్ (అవసరమైతే) చేసి, అందజేస్తుంది, తదుపరి ఎండ్‌పాయింట్/పోర్ట్‌ను కనుగొనేందుకు.
manager = FoundryLocalManager("phi-4-mini")

chat_client = OpenAIChatClient(
    base_url=manager.endpoint,      # ఉదా: http://localhost:<port>/v1
    api_key=manager.api_key,        # ఫౌండ్రీ లోకల్ కోసం ఎల్లప్పుడూ "అవసరం లేదు"
    model_id=manager.get_model_info("phi-4-mini").id,
)

agent = chat_client.as_agent(
    name="LocalAgent",
    instructions="You are a helpful assistant running fully on-device.",
)
```

> **గమనిక:** Foundry Local ఒక OpenAI-తో అనుకూలమైన **Chat Completions** ఎండ్‌పాయింట్‌ని అందిస్తుంది. దీన్ని స్థానిక అభివృద్ధి మరియు ఆఫ్‌లైన్ పరిస్థితుల కోసం ఉపయోగించండి. పూర్తి **Responses API** ఫీచర్ సెట్ (స్థితిగత సంభాషణలు, మొదలైనవి) కోసం Azure OpenAI లేదా Microsoft Foundry ప్రాజెక్ట్‌ను ఉపయోగించండి.

## పాఠం 8 కొరకు అదనపు సెటప్ (Bing గ్రౌండింగ్ వర్క్‌ఫ్లో)

పాఠం 8లో ఉన్న షరతుపడిన వర్క్‌ఫ్లో నోట్‌బుక్ Microsoft Foundry ద్వారా **Bing గ్రౌండింగ్**ను ఉపయోగిస్తుంది. ఆ నమూనాను నడపాలని ఉంటే, ఈ వేరియబుల్‌ను మీ `.env` ఫైల్‌లో చేర్చండి:

| వేరియబుల్ | ఎక్కడ దొరుకుతుంది |
|----------|-----------------|
| `BING_CONNECTION_ID` | Microsoft Foundry పోర్టల్ → మీ ప్రాజెక్టు → **Management** → **Connected resources** → మీ Bing కనెక్షన్ → కనెక్షన్ ID ని కాపీ చేయండి |

## సమస్య పరిష్కారం

### macOS మీద SSL సర్టిఫికేట్ ధృవీకరణ లోపాలు

మీకు macOS మీద క్రింది రకమైన లోపం వస్తున్నట్లయితే:

```plaintext
ssl.SSLCertVerificationError: [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: self-signed certificate in certificate chain
```

ఇది macOS లో Pythonతో ఒక పరిచిత సమస్య, అక్కడ సిస్టమ్ SSL సర్టిఫికేట్‌లు ఆటోమేటిక్గా విశ్వసించబడవు. కింది పరిష్కారాలు వరుసగా ప్రయత్నించండి:

**వికల్పం 1: Python యొక్క Install Certificates స్క్రిప్ట్‌ను నడపండి (సిఫార్సు చేయబడింది)**

```bash
# మీ ఇన్‌స్టాల్ చేసిన Python సంస్కరణతో 3.XX ని మార్చండి (ఉదాహరణకు, 3.12 లేదా 3.13):
/Applications/Python\ 3.XX/Install\ Certificates.command
```

**వికల్పం 2: మీ నోట్‌బుక్‌లో `connection_verify=False` ఉపయోగించండి (GitHub Models నోట్‌బుక్స్ కోసం మాత్రమే)**

పాఠం 6 నోట్‌బుక్‌లో (`06-building-trustworthy-agents/code_samples/06-system-message-framework.ipynb`), ఒక వ్యాఖ్య లేని పనితీరు ఇప్పటికే ఉన్నది. సర్టిఫికేట్ లోపాలు వస్తే `connection_verify=False`ని వ్యాఖ్యల నుంచి తీసివేయండి:

```python
client = ChatCompletionsClient(
    endpoint=endpoint,
    credential=AzureKeyCredential(token),
    connection_verify=False,  # సర్టిఫికెట్ లోపాలు ఎదురైతే SSL ధృవీకరణను నిలిపివేయండి
)
```

> **⚠️ హెచ్చరిక:** SSL ధృవీకరణను నిలిపివేయడం (`connection_verify=False`) సర్టిఫికేట్ ప్రమాణీకరణను తప్పించే ద్వారా భద్రతను తగ్గించుతుంది. అభివృద్ధి వాతావరణంలో తాత్కాలిక పరిష్కారంగా మాత్రమే దీన్ని ఉపయోగించండి. ఉత్పత్తిలో ఉపయోగించవద్దు.

**వికల్పం 3: `truststore`ని ఇన్‌స్టాల్ చేసి ఉపయోగించండి**

```bash
pip install truststore
```

ఆపై మీ నోట్‌బుక్ లేదా స్క్రిప్ట్‌లో ఎటువంటి నెట్‌వర్క్ కాల్‌లు చేయక ముందు పైన ఈ కోడ్‌ను జోడించండి:

```python
import truststore
truststore.inject_into_ssl()
```

## ఎక్కడైనా చిక్కుకున్నారా?

ఈ సెటప్ నడపడంలో ఎలాంటి సమస్యలు ఉంటే, మా <a href="https://discord.gg/kzRShWzttr" target="_blank">Azure AI Community Discord</a> లో చేరండి లేదా <a href="https://github.com/microsoft/ai-agents-for-beginners/issues?WT.mc_id=academic-105485-koreyst" target="_blank">ఇష్యూ సృష్టించండి</a>.

## తదుపరి పాఠం

ఈ కోర్సు కోసం కోడ్ నడపడానికి మీరు ప్రస్తుతులను అయిపోతున్నారు. AI ఏజెంట్ల ప్రపంచం గురించి మరింత నేర్చుకోవడం సంతోషంగా ఉండాలి!

[Introduction to AI Agents and Agent Use Cases](../01-intro-to-ai-agents/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**అస్వీకరణ**:
ఈ పత్రం AI అనువాద సేవ [Co-op Translator](https://github.com/Azure/co-op-translator) ఉపయోగించి అనువదించబడింది. మేము ఖచ్చితత్వానికి ప్రయత్నిస్తున్నప్పటికీ, ఆటోమేటెడ్ అనువాదాలు తప్పులు లేదా అసమగ్రతలను కలిగి ఉండవచ్చు. దాని స్వదేశ భాషలో ఉన్న అసలు పత్రాన్ని అధికారం కలిగిన మూలంగా పరిగణించాలి. కీలకమైన సమాచారం కోసం, ప్రొఫెషనల్ మానవ అనువాదాన్ని సిఫారసు చేస్తాము. ఈ అనువాదం ఉపయోగం వల్ల కలిగే ఏవైనా అపార్థాలు లేదా తప్పుదారులు కోసం మేము బాధ్యత వహించము.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->