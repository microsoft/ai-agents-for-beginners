# Course Setup

## Introduction

ఈ పాఠం ఈ కోర్సు యొక్క కోడ్ నమూనాలను ఎలా నడిపించుకోవాలో వివరించుతుంది.

## Join Other Learners and Get Help

మీరు మీ రిపోను క్లోన్ చేయడం మొదలుపెట్టే ముందు, సెటప్ సహాయం కోసం, కోర్సు గురించి ఏవైనా ప్రశ్నలు కోసం లేదా ఇతర అభ్యసకులతో ಸಂಪರ್ಕానికి [AI Agents For Beginners Discord channel](https://aka.ms/ai-agents/discord)‌లో చేరండి.

## Clone or Fork this Repo

ప్రారంభించడానికి, దయచేసి GitHub Repositoryని క్లోన్ లేదా ఫోర్క్ చేయండి. ఇది కోర్సు పదార్థాల మీ సొంత వెర్షన్‌ను సృష్టిస్తుంది, తద్వారా మీరు కోడ్‌ను నడిపించవచ్చు, పరీక్షించవచ్చు, మరియు సర్దుబాటు చేయవచ్చు!

ఇది చేయడానికి <a href="https://github.com/microsoft/ai-agents-for-beginners/fork" target="_blank">fork the repo</a> లింక్‌ను క్లిక్ చేయండి

మీకు ఇప్పుడు ఈ కోర్సు యొక్క మీ సొంత ఫోర్క్ చేయబడిన వెర్షన్ ఈ క్రింది లింక్‌లో ఉంటుంది:

![క్లోన్ చేసిన రిపో](../../../translated_images/te/forked-repo.33f27ca1901baa6a.webp)

### Shallow Clone (recommended for workshop / Codespaces)

  >పూర్తి రిపాజిటరీ పూర్తి ఇతిహాసం మరియు అన్ని ఫైళ్ళను డౌన్లోడ్ చేస్తే పెద్దది (~3 GB) కావచ్చు. మీరు వర్క్‌షాప్‌కు మాత్రమే హాజరైతే లేదా కొన్ని పాఠాల ఫోల్డర్లే అవసరమైతే, షాలో క్లోన్ (లేదా స్పార్స్ క్లోన్) ఇతిహాసాన్ని త్రంక్ చేయడం ద్వారా మరియు/లేదా బ్లోబ్స్‌ను స్కిప్ చేయడం ద్వారా ఆ పెద్ద డౌన్లోడ్‌ను నివారిస్తుంది.

#### Quick shallow clone — minimal history, all files

క్రింది కమాండ్లలో `<your-username>`ని మీ ఫోర్క్ URL (లేదా అవసరమైతే అప్‌స్ట్రీమ్ URL)తో మార్చండి.

తాజా కమిట్ ఇతిహాసం మాత్రమే క్లోన్ చేయడానికి (చిన్న డౌన్లోడ్):

```bash|powershell
git clone --depth 1 https://github.com/<your-username>/ai-agents-for-beginners.git
```

ఒక నిర్దిష్ట బ్రాంచి క్లోన్ చేయడానికి:

```bash|powershell
git clone --depth 1 --branch <branch-name> https://github.com/<your-username>/ai-agents-for-beginners.git
```

#### Partial (sparse) clone — minimal blobs + only selected folders

ఇది partial clone మరియు sparse-checkout ఉపయోగిస్తుంది (Git 2.25+ అవసరం మరియు partial clone మద్దతుతో ఆధునిక Git సిఫార్సు చేయబడుతుంది):

```bash|powershell
git clone --depth 1 --filter=blob:none --sparse https://github.com/<your-username>/ai-agents-for-beginners.git
```

రిపో ఫోల్డర్‌లోకి వెళ్ళండి:

```bash|powershell
cd ai-agents-for-beginners
```

తర్వాత మీరు కావలసిన ఫోల్డర్లను నిర్దేశించండి (కింది ఉదాహరణలో రెండు ఫోల్డర్లు చూపించబడ్డాయి):

```bash|powershell
git sparse-checkout set 00-course-setup 01-intro-to-ai-agents
```

క్లోనింగ్ మరియు ఫైళ్ళను ధృవీకరించిన తర్వాత, మీరు కేవలం ఫైళ్ళే కావాలని మరియు స్థలం విముక్తి చేయాలనుకుంటే (గిట్ ఇతిహాసం అవసరం వద్దు), దయచేసి రిపాజిటరీ మెటాడేటాను తొలగించండి (💀శాశ్వతమైనది — మీరు అన్ని Git ఫంక్షనాలిటీని పోగొట్టుకుంటారు: ఏ కమిట్లు, పుల్స్, పుష్‌లు లేదా ఇతిహాసం యాక్సెస్ లేదు).

```bash
# zsh/bash
rm -rf .git
```

```powershell
# పవర్‌షెల్
Remove-Item -Recurse -Force .git
```

#### Using GitHub Codespaces (recommended to avoid local large downloads)

- ఈ రిపో కోసం కొత్త Codespace సృష్టించడానికి [GitHub UI](https://github.com/codespaces)ను ఉపయోగించండి।  

- కొత్తగా సృష్టించిన codespace టెర్మినల్‌లో, మీరు అవసరమయ్యే పాఠాల ఫోల్డర్లను మాత్రమే Codespace వర్క్‌స్పేస్‌లోకి తీసుకొనుటకు పై షాలో/స్పార్స్ క్లోన్ కమాండ్లలో ఒకదాన్ని నడపండి.
- ఐచ్ఛికం: Codespaces లో క్లోన్ చేసిన తర్వాత, అదనపు స్థలం ఉపసంహరించడానికి .git ను తొలగించండి (పైన సూచించిన తొలగింపు కమాండ్లను చూడండి).
- గమనిక: మీరు రిపోను Diretly Codespacesలో (అదనపు క్లోన్ లేకుండా) తెరవాలని ఇష్టపడితే, Codespaces devcontainer వాతావరణాన్ని నిర్మిస్తుంది మరియు మీరు అవసరమైనదినికంటే ఎక్కువను ప్రొవిజన్ చేయవచ్చు. తాజా Codespace లో షాలో కాపీని క్లోన్ చేయడం మీకు డిస్క్ వినియోగంపై మరింత నియంత్రణ ఇస్తుంది.

#### Tips

- ఎప్పుడు క్లోన్ URL ను మీ ఫోర్క్ తో మార్చడం మర్చిపోకండి, మీరు సవరించాలనుకుంటే/కమిట్ చేయాలనుకుంటే.
- తరువాత మరింత ఇతిహాసం లేదా ఫైళ్ళు అవసరమైతే, మీరు వాటిని FETCH చేయవచ్చు లేదా sparse-checkout ని సర్దుబాటు చేసి అదనపు ఫోల్డర్లను చేర్చవచ్చు.

## Running the Code

ఈ కోర్సులో మీరు చేతితో అనుభవం పొందడానికి నడిపించగల సీరీస్ Jupyter Notebooks ఉన్నాయి.

కోడ్ నమూనాలు **Microsoft Agent Framework (MAF)**ని `AzureAIProjectAgentProvider`తో ఉపయోగిస్తాయి, ఇది **Microsoft Foundry** ద్వారా **Azure AI Agent Service V2** (the Responses API)కి కనెక్ట్ చేస్తుంది.

అన్ని Python నవ్‌బుక్స్ `*-python-agent-framework.ipynb`గా పేరుబడినవి.

## Requirements

- Python 3.12+
  - **గమనిక**: మీకు Python3.12 ఇన్‌స్టాల్ చేయబడని ఉంటే, దయచేసి దాన్ని ఇన్‌స్టాల్ చేయండి. అప్పుడు requirements.txt ఫైల్ నుండి సరైన వెర్షన్లు ఇన్‌స్టాల్ అయ్యేలా python3.12 ఉపయోగించి మీ venv ను క్రియేట్ చేయండి.
  
    >ఉదాహరణ

    Python venv డైరెక్టరీ క్రియేట్ చేయండి:

    ```bash|powershell
    python -m venv venv
    ```

    అప్పుడు venv ఎన్విరాన్‌మెంట్‌ను యాక్టివేట్ చేయండి:

    ```bash
    # zsh/bash
    source venv/bin/activate
    ```
  
    ```dos
    # Command Prompt for Windows
    venv\Scripts\activate
    ```

- .NET 10+: .NET ఉపయోగించే సాంపిల్ కోడ్‌ల కోసం, దయచేసి [.NET 10 SDK](https://dotnet.microsoft.com/download/dotnet/10.0) లేదా తాజా వెర్షన్‌ను ఇన్‌స్టాల్ చేయండి. అప్పుడు, మీ ఇన్‌స్టాల్ చేసిన .NET SDK వెర్షన్‌ను నిర్ధారించండి:

    ```bash|powershell
    dotnet --list-sdks
    ```

- **Azure CLI** — ప్రామాణీకరణ కోసం అవసరం. [aka.ms/installazurecli](https://aka.ms/installazurecli) నుండి ఇన్‌స్టాల్ చేయండి.
- **Azure Subscription** — Microsoft Foundry మరియు Azure AI Agent Service కి యాక్సెస్ కోసం.
- **Microsoft Foundry Project** — నోట్‌బుక్స్ నడిపించడానికి deployed మోడల్ ఉన్న ప్రాజెక్ట్ (ఉదాహరణకు `gpt-4o`) కావాలి. దిగువ [Step 1](../../../00-course-setup) చూడండి.

మేము ఈ రిపో యొక్క రూట్‌లో `requirements.txt` ఫైల్‌ను చేర్చాం, ఇది కోడ్ నమూనాలను నడపడేందుకు అవసరమైన అన్ని Python ప్యాకేజీలను కలిగి ఉంది.

మీరు రిపో యొక్క రూట్‌లోని టెర్మినల్‌లో క్రింది కమాండ్ నడిపి వాటిని ఇన్‌స్టాల్ చేయవచ్చు:

```bash|powershell
pip install -r requirements.txt
```

ఎటువంటి తార్కికతలు మరియు సమస్యలను నివారించడానికి Python వర్చువల్ ఎన్విరాన్‌మెంట్ సృష్టించడం మేము సిఫార్సు చేస్తాము.

## Setup VSCode

VSCodeలో మీరు సరైన Python వెర్షన్‌ను ఉపయోగిస్తున్నారని నిర్ధారించుకోండి.

![చిత్రం](https://github.com/user-attachments/assets/a85e776c-2edb-4331-ae5b-6bfdfb98ee0e)

## Set Up Microsoft Foundry and Azure AI Agent Service

### దశ 1: Microsoft Foundry ప్రాజెక్ట్ సృష్టించండి

నోట్‌బుక్స్ నడపడానికి మీరు deployed మోడల్ ఉన్న Azure AI Foundry **hub** మరియు **project** అవసరం.

1. మీ Azure ఖాతాతో సైన్ ఇన్ చేయడానికి [ai.azure.com](https://ai.azure.com) కు వెళ్లండి.
2. ఒక **hub** సృష్టించండి (లేదా ప్రారంభంలో ఉన్నదాని ఉపయోగించండి). చూడండి: [Hub resources overview](https://learn.microsoft.com/azure/ai-foundry/concepts/ai-resources).
3. హబ్ లోపల, ఒక **project** సృష్టించండి.
4. **Models + Endpoints** → **Deploy model** నుండి ఒక మోడల్ (ఉదాహరణకు `gpt-4o`) ను డిప్లాయ్ చేయండి.

### దశ 2: మీ ప్రాజెక్ట్ ఎండ్‌పాయింట్ మరియు మోడల్ డిప్లాయ్‌మెంట్ పేరును పొందండి

Microsoft Foundry పోర్టల్‌లోని మీ ప్రాజెక్ట్ నుండి:

- **Project Endpoint** — **Overview** పేజీకి వెళ్లి ఎండ్‌పాయింట్ URL ను కాపీ చేయండి.

![Project Connection String](../../../translated_images/te/project-endpoint.8cf04c9975bbfbf1.webp)

- **Model Deployment Name** — **Models + Endpoints**కి వెళ్లి, మీ డిప్లాయ్ చేసిన మోడల్‌ను ఎంచుకుని **Deployment name** (ఉదాహరణకు `gpt-4o`) గమనించండి.

### దశ 3: `az login` తో Azure లో సైన్ ఇన్ అవ్వండి

అన్ని నోట్‌బుక్స్ ప్రామాణీకరణ కోసం **`AzureCliCredential`** ఉపయోగిస్తాయి — నిర్వహించవలసిన ఏ API కీలు లేవు. దీనికి Azure CLI ద్వారా మీరు సైన్ ఇన్ అయ్యి ఉండాలి.

1. మీరు ఇప్పటికీ ఇన్‌స్టాల్ చేయకపోతే **Azure CLI** ను ఇన్‌స్టాల్ చేయండి: [aka.ms/installazurecli](https://aka.ms/installazurecli)

2. సైన్ ఇన్ చేయడానికి ఈ కమాండ్ నడపండి:

    ```bash|powershell
    az login
    ```

    లేదా మీరు బ్రౌజర్ లేని రిమోట్/Codespace వాతావరణంలో ఉన్నట్లయితే:

    ```bash|powershell
    az login --use-device-code
    ```

3. ప్రాంప్ట్ అయిన బాటులో మీ సబ్‌స్క్రిప్షన్‌ను ఎంచుకోండి — మీ Foundry ప్రాజెక్ట్ ఉన్నదానిని ఎంచుకోండి.

4. మీరు సైన్ ఇన్ అయినట్లు నిర్ధారించుకోండి:

    ```bash|powershell
    az account show
    ```

> **ఎందుకు `az login`?** నోట్‌బుక్స్ `azure-identity` ప్యాకేజీ నుండి `AzureCliCredential`ని ఉపయోగించి ప్రామాణీకరిస్తాయి. అంటే మీ Azure CLI సెషన్ క్రెడెంటియల్స్‌ను అందిస్తుంది — మీ `.env` ఫైలులో ఏ API కీలు లేదా రహస్యాలు అవసరం ఉండవు. ఇది ఒక [సెక్యురిటీ ఉత్తమ ఆచారం](https://learn.microsoft.com/azure/developer/ai/keyless-connections).

### దశ 4: మీ `.env` ఫైల్ సృష్టించండి

ఉదాహరణ ఫైల్‌ను కాపీ చేయండి:

```bash
# zsh/bash
cp .env.example .env
```

```powershell
# పవర్‌షెల్
Copy-Item .env.example .env
```

`.env` ను ఓపెన్ చేసి ఈ రెండు విలువలను పూర్ణ చేయండి:

```env
AZURE_AI_PROJECT_ENDPOINT=https://<your-project>.services.ai.azure.com/api/projects/<your-project-id>
AZURE_AI_MODEL_DEPLOYMENT_NAME=gpt-4o
```

| Variable | Where to find it |
|----------|-----------------|
| `AZURE_AI_PROJECT_ENDPOINT` | Foundry portal → your project → **Overview** page |
| `AZURE_AI_MODEL_DEPLOYMENT_NAME` | Foundry portal → **Models + Endpoints** → your deployed model's name |

ఇంతే చాలా పాఠాల కోసం అవసరం! నోట్‌బుక్స్ మీ `az login` సెషన్ ద్వారా ఆటోమేటిక్‌గా ప్రామాణీకరించబడతాయి.

### దశ 5: Python Dependencies ను ఇన్‌స్టాల్ చేయండి

```bash|powershell
pip install -r requirements.txt
```

మేము మీరు ముందుగా సృష్టించిన వర్చువల్ ఎన్విరాన్‌మెంట్‌లో దీన్ని నడపాలని సిఫార్సు చేస్తాము.

## Additional Setup for Lesson 5 (Agentic RAG)

పాఠం 5 రెట్రీవల్-అగ్మెంటెడ్ జనరేషన్ కోసం **Azure AI Search** ఉపయోగిస్తుంది. మీరు ఆ పాఠం నడపాలని ఉద్దేశిస్తే, మీ `.env` ఫైల్‌లో ఈ వేరియబుల్‌లను జత చేయండి:

| Variable | Where to find it |
|----------|-----------------|
| `AZURE_SEARCH_SERVICE_ENDPOINT` | Azure portal → your **Azure AI Search** resource → **Overview** → URL |
| `AZURE_SEARCH_API_KEY` | Azure portal → your **Azure AI Search** resource → **Settings** → **Keys** → primary admin key |

## Additional Setup for Lesson 6 and Lesson 8 (GitHub Models)

పాఠం 6 మరియు 8 లోని కొన్ని నోట్‌బుక్స్ Azure AI Foundry స్థానానికి బదులుగా **GitHub Models** ఉపయోగిస్తాయి. మీరు ఆ నమూనాలను నడిపించాలనుకుంటే, మీ `.env` ఫైల్‌లో ఈ వేరియబుల్‌లను జత చేయండి:

| Variable | Where to find it |
|----------|-----------------|
| `GITHUB_TOKEN` | GitHub → **Settings** → **Developer settings** → **Personal access tokens** |
| `GITHUB_ENDPOINT` | Use `https://models.inference.ai.azure.com` (default value) |
| `GITHUB_MODEL_ID` | Model name to use (e.g. `gpt-4o-mini`) |

## Additional Setup for Lesson 8 (Bing Grounding Workflow)

పాఠం 8 లో ఉన్న conditional workflow నోట్‌బుక్ Azure AI Foundry ద్వారా **Bing grounding** ఉపయోగిస్తుంది. మీరు ఆ నమూనాను నడిపించాలనుకుంటే, మీ `.env` ఫైల్‌లో ఈ వేరియబుల్‌ను జత చేయండి:

| Variable | Where to find it |
|----------|-----------------|
| `BING_CONNECTION_ID` | Azure AI Foundry portal → your project → **Management** → **Connected resources** → your Bing connection → copy the connection ID |

## Troubleshooting

### SSL Certificate Verification Errors on macOS

 మీరు macOSపై ఉంటే మరియు క్రిందట్లుగా ఒక ఎర్రర్ చూపిస్తే:

```plaintext
ssl.SSLCertVerificationError: [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: self-signed certificate in certificate chain
```

ఇది macOSపై Pythonతో పండుగా తెలిసిన సమస్య, ఇక్కడ సిస్టమ్ SSL సర్టిఫికేట్లు ఆటోమేటిక్ గా ట్రస్ట్ చేయబడవు. కింది పరిష్కారాలను క్ర‌మంగా ప్రయత్నించండి:

**వికల్పం 1: Python యొక్క Install Certificates స్క్రిప్ట్ను నడపండి (శిఫార్సు చేయబడింది)**

```bash
# 3.XX ను మీ ఇన్‌స్టాల్ చేసిన Python సంస్కరణతో మార్చండి (ఉదాహరణకి, 3.12 లేదా 3.13):
/Applications/Python\ 3.XX/Install\ Certificates.command
```

**వికల్పం 2: మీ నోట్‌బుక్‌లో `connection_verify=False` ఉపయోగించండి (GitHub Models నోట్‌బుక్స్‌కి మాత్రమే)**

Lesson 6 నోట్‌బుక్ (`06-building-trustworthy-agents/code_samples/06-system-message-framework.ipynb`)లో, కామెంట్ చేయబడిన వర్క్ అరౌండ్ ఇప్పటికే చేరుస్తారు. క్లయింట్ సృష్టించే సమయంలో `connection_verify=False`ని uncomment చేయండి:

```python
client = ChatCompletionsClient(
    endpoint=endpoint,
    credential=AzureKeyCredential(token),
    connection_verify=False,  # సర్టిఫికెట్ లోపాలు ఎదురైనట్లయితే SSL ధృవీకరణను నిలిపివేయండి
)
```

> **⚠️ హెచ్చరిక:** SSL ధృవీకరణను నిష్క్రియం చేయడం (`connection_verify=False`) సర్టిఫికేట్ ధృవీకరణను జారవిడుచుకోవడం ద్వారా భద్రతను తగ్గిస్తుంది. ఇది అభివృద్ధి వాతావరణాల్లో తాత్కాలిక వర్క్ అరౌండ్ గా మాత్రమే ఉపయోగించండి, ప్రొడక్షన్‌లో ఎప్పుడూ ఉపయోగించకండి.

**వికల్పం 3: `truststore` ను ఇన్‌స్టాల్ చేసి ఉపయోగించండి**

```bash
pip install truststore
```

ఆ తరువాత నెట్‌వర్క్ కాల్స్ చేయక ముందే మీ నోట్‌బుక్ లేదా స్క్రిప్ట్ టాప్‌లో క్రింది‌ని జోడించండి:

```python
import truststore
truststore.inject_into_ssl()
```

## Stuck Somewhere?

ఈ సెటప్ నడపడంలో మీకు ఏవైనా సమస్యలు ఉంటే, మా <a href="https://discord.gg/kzRShWzttr" target="_blank">Azure AI Community Discord</a>లోకి రండి లేదా <a href="https://github.com/microsoft/ai-agents-for-beginners/issues?WT.mc_id=academic-105485-koreyst" target="_blank">create an issue</a> చేయండి.

## Next Lesson

మీరు ఇప్పుడు ఈ కోర్సు కోసం కోడ్ నడిపేలా సిద్ధంగా ఉన్నారు. AI Agents ప్రపంచాన్ని గురించి మరింత నేర్చుకోవడంలో సంతోషకరంగా ఉండండి!

[Introduction to AI Agents and Agent Use Cases](../01-intro-to-ai-agents/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
బాధ్యత నిరాకరణ:

ఈ పత్రాన్ని AI అనువాద సేవ [Co-op Translator](https://github.com/Azure/co-op-translator) ద్వారా అనువదించబడ్డది. మేము ఖచ్చితత్వానికి ప్రయత్నించినప్పటికీ, ఆటోమేటెడ్ అనువాదాలు తప్పులు లేదా అపనిర్దిష్టతలు కలిగి ఉండవచ్చు అని దయచేసి గమనించండి. మూల భాషలో ఉన్న అసలు పత్రాన్ని అధికారిక మూలంగా పరిగణించాలి. అత్యంత కీలకమైన సమాచారం కోసం వృత్తిపరమైన మానవ అనुवాదకుడి సేవలను ఉపయోగించటం మంచి ఆచారం. ఈ అనువాదం వినియోగం వల్ల జరిగే ఏవైనా అపవిత్రతలు లేదా తప్పుగా అర్థం చేసుకోవడాలపై మేము బాధ్యత వహించము.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->