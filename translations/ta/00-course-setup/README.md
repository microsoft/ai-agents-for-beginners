# பாடநெறி அமைப்பு

## அறிமுகம்

இந்த பாடம் இந்த பாடநெறியின் குறியீடு உதாரணங்களை எவ்வாறு இயக்குவது என்பதை கற்பிக்கும்.

## பிற பயிலாளர்களுடன் இணைந்து உதவி பெறுங்கள்

உங்கள் ரெப்போவை கிளோன் செய்ய தொடங்குவதற்கு முன், அமைப்பில் உதவி பெற, பாடத்திற்கான கேள்விகளை கேட்க்க, அல்லது பிற பயிலாளர்களுடன் தொடர்பு கொள்ள [AI Agents For Beginners Discord சேனலை](https://aka.ms/ai-agents/discord) இணையுங்கள்.

## இந்த ரெப்போவை கிளோன் அல்லது ஃபோர்க் செய்யவும்

தொடங்க, GitHub ரெப்பொசிடரியை கிளோன் அல்லது ஃபோர்க் செய்யவும். இதனால் நீங்கள் பாடநெறி உள்ளடக்கத்தின் உங்கள் சொந்த பிரதியை பெற்று குறியீட்டை இயக்கு, சோதனை செய் மற்றும் திருத்தம் செய்ய முடியும்!

This can be done by clicking the link to <a href="https://github.com/microsoft/ai-agents-for-beginners/fork" target="_blank">ரெப்போவை ஃபோர்க் செய்ய</a>

You should now have your own forked version of this course in the following link:

![ஃபோர்க் செய்யப்பட்ட ரெப்போ](../../../translated_images/ta/forked-repo.33f27ca1901baa6a.webp)

### குறுகிய கிளோன் (workshop / Codespaces க்காக பரிந்துரைக்கப்படுகிறது)

  >பூரண ரெப்பொசிடரி முழு வரலாறும் மற்றும் அனைத்து கோப்புகளும் பதிவிறக்கப்பட்டால் பெரியதாக (~3 GB) இருக்கலாம். நீங்கள் வெறும் workshop இற்கு வரப்போகிறீர்கள் அல்லது சில பாடப்பொடிகள் மட்டும் தேவையானால், ஒரு குறுகிய கிளோன் (அல்லது ஒரு sparse clone) வரலாற்றை சுருக்குவதாலும் மற்றும்/அல்லது blobsஐ தவிர்ப்பதால் பெரும்பாலும் அந்த பதிவிறக்கத்தை தவிர்க்க உதவும்.

#### விரைவான குறுகிய கிளோன் — குறைந்த வரலாறு, அனைத்து கோப்புகளும்

Below கட்டளைகளில் உள்ள `<your-username>` ஐ உங்கள் ஃபோர்க் URL(அல்லது விருப்பமிருந்தால் upstream URL) உடன் மாற்றவும்.

கடைசிக் commit வரலாற்றை மட்டுமே கிளோன் செய்ய (சிறிய பதிவிறக்கம்):

```bash|powershell
git clone --depth 1 https://github.com/<your-username>/ai-agents-for-beginners.git
```

தற்குறிப்பாக ஒரு கிளையை கிளோன் செய்ய:

```bash|powershell
git clone --depth 1 --branch <branch-name> https://github.com/<your-username>/ai-agents-for-beginners.git
```

#### பகுதி (sparse) கிளோன் — குறைந்த blobs + தேர்ந்தெடுக்கப்பட்ட கோப்பolders மட்டுமே

இது partial clone மற்றும் sparse-checkout ஐ பயன்படுத்துகிறது (Git 2.25+ தேவைப்படும் மற்றும் partial clone ஆதரவு கொண்ட நவீன Git பரிந்துரைக்கப்படுகிறது):

```bash|powershell
git clone --depth 1 --filter=blob:none --sparse https://github.com/<your-username>/ai-agents-for-beginners.git
```

ரெப்போ கோப்புறையில் செல்லவும்:

```bash|powershell
cd ai-agents-for-beginners
```

பின்னர் நீங்கள் வேண்டுமென்றால் எந்த கோப்புறைகளை எடுப்பதென்பதை குறிப்பிடுங்கள் (தொகுப்பு கீழே இரண்டு கோப்புறைகளை காட்டுகிறது):

```bash|powershell
git sparse-checkout set 00-course-setup 01-intro-to-ai-agents
```

கிளோனிங் மற்றும் கோப்புகளை சரிபாரித்த பிறகு, நீங்கள் வெறுமனே கோப்புகள் மட்டும் வேண்டும் மற்றும் இடத்தை விட சுத்தம் செய்ய நினைத்தால் (git வரலாறு இல்லை), தயவுசெய்து ரெப்பொசிடரி மெட்டாடேட்டாவை நீக்கவும் (💀மீள்தி அமைய முடியாதது — இதில் நீங்கள் அனைத்து Git செயல்பாடுகளையும் இழக்கப்பெறுவீர்கள்: commits, pulls, pushes, அல்லது வரலாறு அணுகல்).

```bash
# zsh/bash
rm -rf .git
```

```powershell
# பவர்ஷெல்
Remove-Item -Recurse -Force .git
```

#### GitHub Codespaces ஐ பயன்படுத்துதல் (உள்ளூர் பெரிய பதிவிறக்கங்களை தவிர்க்க பரிந்துரைக்கப்படுகிறது)

- இந்த ரெப்போவிற்கான புதிய Codespace ஒன்றை [GitHub UI](https://github.com/codespaces) மூலம் உருவாக்குங்கள்.  

- புதிதாக உருவாக்கப்பட்ட codespace இன் டெர்மினலில், மேலே உள்ள shallow/sparse clone கட்டளைகளில் ஒன்றை இயக்கி உங்களுக்கு தேவைப்படும் பாடப்பொடிகளை மட்டுமே Codespace வேலைப்பகுதியில் கொண்டு வாருங்கள்.
- விருப்பமா: Codespaces இல் உள்ளே கிளோன் செய்த பிறகு, கூடுதல் இடத்தை மீட்டெடுக்க .git ஐ நீக்கவும் (மேலே கொடுக்கப்பட்ட நீக்கக் கட்டளைகளைப் பார்க்கவும்).
- குறிப்பு: உங்கள் ரெப்போவை Codespaces இல் நேரடியாக திறக்க (கூடுதல் கிளோன் இல்லாமல்) விரும்பினால், Codespaces devcontainer சூழலை கட்டமைக்கும் மற்றும் இது இன்னும் தேவையிலதானவை தானாகவே வழங்கக்கூடும். ஒரு புதிய Codespace உள்ளே ஒரு குறுகிய பிரதி கிளோன் செய்தால் கோப்புச் சேமிப்பு மேலாண்மையில் நீங்கள் அதிக கட்டுப்பாட்டை பெறுவீர்கள்.

#### குறிப்புகள்

- தொகுக்க/கமிட்ட் செய்ய விரும்பினால், எப்போதும் கிளோன் URLஐ உங்கள் ஃபோர்க்கு மாற்றவும்.
- பின்னர் மேலும் வரலாறு அல்லது கோப்புகள் தேவைப்பட்டால், அவைகளை fetch செய்து சேர்க்கலாம் அல்லது sparse-checkout ஐ மாற்றி கூடுதல் கோப்புறைகளை உள்ளடக்கலாம்.

## குறியீட்டை இயக்குவது

இந்த பாடநெறி கையேட்டில் சில Jupyter நோட்புக்குகள் உள்ளன, அவைகளை இயக்கி AI ஏஜென்டுகள் உருவாக்குவதில் கைமுறை அனுபவம் பெறலாம்.

குறியீடு மாதிரிகள் **Microsoft Agent Framework (MAF)** ஐ பயன்படுத்துகிறது மற்றும் `AzureAIProjectAgentProvider` மூலம் **Microsoft Foundry** மூலமாக **Azure AI Agent Service V2** (Responses API) உடன் இணைக்கின்றது.

அனைத்து Python நோட்புக்குகளும் `*-python-agent-framework.ipynb` என அடையாளம் வைப்ட்டுள்ளன.

## தேவைகள்

- Python 3.12+
  - **குறிப்பு**: உங்கள் கணினியில் Python3.12 நிறுவப்படவில்லையெனில், அதை நிறுவிக்கொண்டிருங்கள். அதன் பின் requirements.txt கோப்பில் குறிப்பிடப்பட்ட சரியான பதிப்புகளை நிறுவுவதற்காக python3.12 கொண்டு venv உருவாக்குங்கள்.
  
    >உதாரணம்

    Python venv கோப்புறையை உருவாக்கவும்:

    ```bash|powershell
    python -m venv venv
    ```

    பின்னர் venv சூழலை செயல்படுத்த:

    ```bash
    # zsh/பாஷ்
    source venv/bin/activate
    ```
  
    ```dos
    # Command Prompt for Windows
    venv\Scripts\activate
    ```

- .NET 10+: .NET பயன்படுத்திய மாதிரிகளுக்காக, [ .NET 10 SDK](https://dotnet.microsoft.com/download/dotnet/10.0) அல்லது அதற்கும் மேல் பதிப்பை 설치 செய்து கொள்ளுங்கள். பிறகு உங்கள் நிறுவப்பட்ட .NET SDK பதிப்பை சரிபார்க்கவும்:

    ```bash|powershell
    dotnet --list-sdks
    ```

- **Azure CLI** — அங்கீகாரத்திற்கு தேவை. [aka.ms/installazurecli](https://aka.ms/installazurecli) இருந்து நிறுவுக.
- **Azure Subscription** — Microsoft Foundry மற்றும் Azure AI Agent Service அணுகலுக்கு.
- **Microsoft Foundry Project** — உரையாடலுக்கு அமைக்கப்பட்ட ஒரு மாதிரியை கொண்ட ஒரு திட்டம் (உதா., `gpt-4o`). கீழே [Step 1](../../../00-course-setup) ஐப் பார்க்கவும்.

இந்த ரெப்பொசிடரியின் ரூட்டில் `requirements.txt` கோப்பு சேர்க்கப்பட்டுள்ளது, இது குறியீடு மாதிரிகளை இயக்க பணிபுரியும் எல்லா தேவையான Python பேக்கேஜ்களையும் கொண்டுள்ளது.

உங்கள் டெர்மினலில் ரெப்பொசிடரியின் ரூட்டில் கீழ்காணும் கட்டளையை இயக்கி அவை அனைத்தையும் நிறுவலாம்:

```bash|powershell
pip install -r requirements.txt
```

பகுப்பு மோதல்களையும் பிரச்சனைகளையும் தவிர்க்க Python virtual environment உருவாக்க பரிந்துரைக்கப்படுகிறது.

## VSCode அமைப்பு

VSCode இல் நீங்கள் சரியான Python பதிப்பை பயன்படுத்துகிறீர்களா என்பதை உறுதிப்படுத்துங்கள்.

![படம்](https://github.com/user-attachments/assets/a85e776c-2edb-4331-ae5b-6bfdfb98ee0e)

## Microsoft Foundry மற்றும் Azure AI Agent Service அமைத்தல்

### படி 1: Microsoft Foundry திட்டம் உருவாக்கவும்

நோட்பூக்களை இயக்க இந்த செயற்பாட்டிற்கு ஒரு Azure AI Foundry **hub** மற்றும் **project** மற்றும் அதில் பயன்பாட்டுக்கான ஒரு deploy செய்யப்பட்ட மாதிரி தேவை.

1. [ai.azure.com](https://ai.azure.com) இன் பக்கத்திற்கு சென்று உங்கள் Azure கணக்கில் சைன் இன் செய்யுங்கள்.
2. ஒரு **hub** உருவாக்கவும் (அல்லது ஏற்கனவே உள்ளதையொன்றை பயன்படுத்தவும்). பார்க்கவும்: [Hub resources overview](https://learn.microsoft.com/azure/ai-foundry/concepts/ai-resources).
3. hub இல் உள்ளே ஒரு **project** உருவாக்கவும்.
4. **Models + Endpoints** → **Deploy model** இல் இருந்து ஒரு மாதிரியை deploy செய்யவும் (உதா., `gpt-4o`).

### படி 2: உங்கள் திட்ட எண்ட்பாயிண்ட் மற்றும் மாதிரி டெப்லாய் பெயரை பெறுதல்

Microsoft Foundry போர்டலில் உங்கள் திட்டத்தில் இருந்து:

- **Project Endpoint** — **Overview** பக்கத்திற்கு சென்று endpoint URLஐ நகலெடுக்கவும்.

![திட்ட இணைப்பு சரம்](../../../translated_images/ta/project-endpoint.8cf04c9975bbfbf1.webp)

- **Model Deployment Name** — **Models + Endpoints** இன் கீழ் உங்கள் deploy செய்த மாதிரியைத் தேர்ந்தெடுத்து **Deployment name** ஐ குறித்துக் கொள்ளுங்கள் (உதா., `gpt-4o`).

### படி 3: `az login` கொண்டு Azure இல் சைன் இன் செய்யவும்

அனைத்து நோட்புக்குகள் அங்கீகாரத்திற்கு **`AzureCliCredential`** ஐப் பயன்படுத்துகின்றன — நிர்வகிக்க வேண்டிய API விசைகள் இல்லை. இதற்கு நீங்கள் Azure CLI மூலம் சைன் இன் செய்யப்பட்டிருக்க வேண்டும்.

1. **Azure CLI ஐ நிறுவ**்ிக்கவில்லை என்றால் நிறுவவும்: [aka.ms/installazurecli](https://aka.ms/installazurecli)

2. **சைன் இன் செய்ய** கீழ்காணும் கட்டளையை இயக்கவும்:

    ```bash|powershell
    az login
    ```

    அல்லது உங்களுக்கு browser இல்லாத remote/Codespace சூழல் இருந்தால்:

    ```bash|powershell
    az login --use-device-code
    ```

3. **உங்கள் subscription ஐ தேர்வு செய்க** (கேட்கப்பட்டால்) — உங்கள் Foundry திட்டத்தை கொண்ட subscriptionஐத் தேர்ந்தெடுக்கவும்.

4. **சரிபார்க்கவும்** நீங்கள் சைன் இன் செய்துள்ளீர்களா:

    ```bash|powershell
    az account show
    ```

> **ஏன் `az login`?** நோட்புக்குகள் `azure-identity` பேக்கேஜின் `AzureCliCredential` ஐப் பயன்படுத்தி அங்கீகாரம் செய்கின்றன. இதன் பொருள் உங்கள் Azure CLI அமர்வு (session) தான் கடவுச்சொற்களைக் கொடுக்கிறது — `.env` கோப்பில் API விசைகள் அல்லது ரகசியங்கள் தேவைப்படும். இது ஒரு [பாதுகாப்பு சிறந்த நடைமுறை](https://learn.microsoft.com/azure/developer/ai/keyless-connections).

### படி 4: உங்கள் `.env` கோப்பை உருவாக்கவும்

உதாரணக் கோப்பைப் நகலெடுக்கவும்:

```bash
# zsh/bash
cp .env.example .env
```

```powershell
# பவர் ஷெல்
Copy-Item .env.example .env
```

`.env` ஐத் திறந்து கீழ்காணும் இரண்டு பெறுமதிகளை நிரப்பவும்:

```env
AZURE_AI_PROJECT_ENDPOINT=https://<your-project>.services.ai.azure.com/api/projects/<your-project-id>
AZURE_AI_MODEL_DEPLOYMENT_NAME=gpt-4o
```

| Variable | Where to find it |
|----------|-----------------|
| `AZURE_AI_PROJECT_ENDPOINT` | Foundry portal → your project → **Overview** page |
| `AZURE_AI_MODEL_DEPLOYMENT_NAME` | Foundry portal → **Models + Endpoints** → your deployed model's name |

இதுவுவே பெரும்பாலான பாடங்களுக்கு போதியும்! நோட்புக்குகள் உங்கள் `az login` அமர்வு மூலம் தானாக அங்கீகரிக்கப்படும்.

### படி 5: Python சார்ந்த சார்பு பொருட்களை நிறுவவும்

```bash|powershell
pip install -r requirements.txt
```

உங்களுக்கு முன்னதாக உருவாக்கிய virtual environment இன் உள்ளே இதை இயக்குமாறு பரிந்துரைக்கப்படுகிறது.

## பாடம் 5 க்கான கூடுதல் அமைப்பு (Agentic RAG)

பாடம் 5 இல் **Azure AI Search** ஐ retrieval-augmented generation க்காக பயன்படுத்துகிறது. அந்த பாடத்தை இயக்க திட்டமிட்டால், உங்கள் `.env` கோப்பில் கீழ்காணும் மாறில்களை சேர்க்கவும்:

| Variable | Where to find it |
|----------|-----------------|
| `AZURE_SEARCH_SERVICE_ENDPOINT` | Azure portal → your **Azure AI Search** resource → **Overview** → URL |
| `AZURE_SEARCH_API_KEY` | Azure portal → your **Azure AI Search** resource → **Settings** → **Keys** → primary admin key |

## பாடம் 6 மற்றும் பாடம் 8 க்கான கூடுதல் அமைப்பு (GitHub Models)

பாடங்கள் 6 மற்றும் 8 இன் சில நோட்புக்குகள் Microsoft Foundry ஐ தவிர **GitHub Models** ஐ பயன்படுத்துகின்றன. அந்த மாதிரிகளை இயக்க திட்டமிட்டால், உங்கள் `.env` கோப்பில் இந்த மாறில்களை சேர்த்திடுங்கள்:

| Variable | Where to find it |
|----------|-----------------|
| `GITHUB_TOKEN` | GitHub → **Settings** → **Developer settings** → **Personal access tokens** |
| `GITHUB_ENDPOINT` | Use `https://models.inference.ai.azure.com` (default value) |
| `GITHUB_MODEL_ID` | Model name to use (e.g. `gpt-4o-mini`) |

## பாடம் 8 க்கான கூடுதல் அமைப்பு (Bing Grounding Workflow)

பாடம் 8 இல் உள்ள conditional workflow நோட்புக் Azure AI Foundry மூலம் **Bing grounding** ஐ பயன்படுத்துகிறது. அந்த மாதிரியை இயக்க திட்டமிட்டால், உங்கள் `.env` கோப்பில் இந்த மாறியை சேர்க்கவும்:

| Variable | Where to find it |
|----------|-----------------|
| `BING_CONNECTION_ID` | Azure AI Foundry portal → your project → **Management** → **Connected resources** → your Bing connection → copy the connection ID |

## சிக்கல்கள் தீர்க்குதல்

### macOS இல் SSL சான்றிதழ் சரிபார்ப்பு பிழைகள்

macOS இல் நீங்கள் இۈرுவான பிழையானால்:

```plaintext
ssl.SSLCertVerificationError: [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: self-signed certificate in certificate chain
```

இது macOS இல் Python உடன் பரிச்சயமான பிரச்சனை — சிஸ்டம் SSL சான்றிதழ்கள் தானாகவே நம்பப்படுவதில்லை. கீழ்க்காணும் தீர்வுகளைக் குறிசொல்லப்படியலில் முயற்சிக்கவும்:

**விருப்பம் 1: Python இன் Install Certificates ஸ்கிரிப்ட்டை இயக்கவும் (பரிந்துரைக்கப்பட்டது)**

```bash
# 3.XX-ஐ உங்கள் நிறுவிய Python பதிப்பால் (உதா., 3.12 அல்லது 3.13) மாற்றவும்:
/Applications/Python\ 3.XX/Install\ Certificates.command
```

**விருப்பம் 2: உங்கள் நோட்புக்கில் `connection_verify=False` பயன்படுத்தவும் (GitHub Models நோட்புக்குகளுக்கே மட்டும்)**

Lesson 6 நோட்புக் (`06-building-trustworthy-agents/code_samples/06-system-message-framework.ipynb`) இல் ஒரு கமென்ட் செய்யப்பட்ட workaround ஏற்கனவே உள்ளதாக உள்ளது. client உருவாக்கும் போது `connection_verify=False` ஐ uncomment செய்து பயன்படுத்தவும்:

```python
client = ChatCompletionsClient(
    endpoint=endpoint,
    credential=AzureKeyCredential(token),
    connection_verify=False,  # சான்றிதழ் பிழைகள் ஏற்பட்டால் SSL சரிபார்ப்பை முடக்கவும்
)
```

> **⚠️ எச்சரிக்கை:** SSL சரிபார்ப்பை முடக்குவது (`connection_verify=False`) சான்றிதழ் சரிபார்ப்பை தவிர்க்குவதின் மூலம் பாதுகாப்பை குறைக்கிறது. அதை தற்காலிக workaround ஆகவும் development சூழலில் மட்டுமே பயன்படுத்தவும், production இல் தேர்ந்தெடுக்கக்கூடாது.

**விருப்பம் 3: `truststore` ஐ நிறுவி பயன்படுத்தவும்**

```bash
pip install truststore
```

பின்னர் உங்கள் நோட்புக் அல்லது ஸ்கிரிப்டின் மேற்பகுதியில் எந்தவொரு நெட்வொர்க் அழைப்புகளையும் செய்யும் முன் இதை சேர்க்கவும்:

```python
import truststore
truststore.inject_into_ssl()
```

## எங்காவது சிக்கியிருக்கிறீர்களா?

இந்த அமைப்பை இயக்குவதில் ஏதேனும் பிரச்சினைகள் இருந்தால், எங்கள் <a href="https://discord.gg/kzRShWzttr" target="_blank">Azure AI Community Discord</a> இல் சென்று உதவி பெறவும் அல்லது <a href="https://github.com/microsoft/ai-agents-for-beginners/issues?WT.mc_id=academic-105485-koreyst" target="_blank">ஒரு issue உருவாக்கவும்</a>.

## அடுத்த பாடம்

இப்பொழுது நீங்கள் இந்த பாடநெறிக்கான குறியீட்டை இயக்கு தயாராக இருக்கிறீர்கள். AI ஏஜென்டுகளின் உலகத்தைப் பற்றி மேலும் மகிழ்ச்சியாகக் கற்பீர்கள்!

[AI ஏஜென்டுகளிற்கான அறிமுகம் மற்றும் ஏஜென்ட் பயன்பாட்டு வழக்குகள்](../01-intro-to-ai-agents/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
மறுப்புரை:
இந்த ஆவணம் AI மொழிபெயர்ப்பு சேவை [Co-op Translator](https://github.com/Azure/co-op-translator) மூலம் மொழிபெயர்க்கப்பட்டுள்ளது. நாங்கள் துல்லியத்திற்காக முயற்சியினும், தானியங்கி மொழிபெயர்ப்புகளில் பிழைகள் அல்லது தவறுகள் இருக்கக்கூடும் என்பதை கவனத்தில் கொள்ளவும். மூல ஆவணம் அதன் தாய்மொழியில் அதிகாரப்பூர்வ ஆதாரமாக கருதப்பட வேண்டும். முக்கிய மற்றும் நேர்மறையான தகவல்களுக்கு, தொழில்முறை மனித மொழிபெயர்ப்பை பரிந்துரைக்கின்றோம். இந்த மொழிபெயர்ப்பைப் பயன்படுத்துவதால் ஏற்பட்ட எந்தணும் தவறான புரிதல் அல்லது தவறான விளக்கத்திற்கும் நாங்கள் பொறுப்பேற்கமாட்டோம்.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->