# பாட வகுப்பு அமைத்தல்

## அறிமுகம்

இந்த பாடத்தில், இந்த பாடத்திட்டத்தின் கோட் உதாரணங்களை எப்படி இயக்குவது என்பதைக் காண்போம்.

## மற்ற கற்றலாளர்களுடன் இணைந்து உதவி பெறுங்கள்

உங்கள் ரெபோவை க்ளோன் செய்ய துவங்கும் முன்பு, அமைப்புக்கு உதவ அல்லது பாடத்திட்டம் பற்றிய கேள்விகள் வருமானால் அல்லது பிற கற்றலாளர்களுடன் இணைப்பதற்காக [AI Agents For Beginners Discord channel](https://aka.ms/ai-agents/discord) இணையதளத்தில் சேரவும்.

## இந்த ரெபோவை க்ளோன் அல்லது ஃபோர்க் செய்யவும்

துவங்க, தயவுசெய்து GitHub ரெபோசிடரியை கிளோன் அல்லது ஃபோர்க் செய்யவும். இது உங்களுக்கு கோட் செயல்படுத்துவதற்கு, சோதனை செய்ய மற்றும் மாற்றங்களை செய்ய உங்களது சொந்த பதிப்பாக பாடப்பொருளை உருவாக்கும்!

இதை செய்ய, <a href="https://github.com/microsoft/ai-agents-for-beginners/fork" target="_blank">ரெபோவை ஃபோர்க் செய்ய</a> உள்ள தொடுப்பை க்ளிக் செய்யலாம்

இப்போது உங்களுக்கு இந்த பாடத்திட்டத்தின் சொந்த ஃபோர்க் பதிப்பு கீழ்காணும் தொடுப்பில் கிடைக்கும்:

![Forked Repo](../../../translated_images/ta/forked-repo.33f27ca1901baa6a.webp)

### மேல் பரிந்துரைக்கப்படுகிறது: லேசான க்ளோன் (workshop / Codespaces க்கு)

  >இணையக தொகுப்பு முழுமையாகப் பதிவிறக்கம் செய்தால் பெரியதாக (~3 GB) இருக்கலாம். நீங்கள் வெறும் வொர்க்ஷாப் பார்வையோ அல்லது சில பாடம் கோப்புக்களை மட்டும் தேவையோ என்றால், லேசான க்ளோன் (அல்லது சில பகுதிகளை மட்டுமே) வரலாறு மற்றும்/அல்லது பிளாப்களை குறைத்து பெரும்பாலான பதிவிறக்கங்களை தவிர்க்கும்.

#### விரைவான லேசான க்ளோன் — குறைந்த வரலாறு, அனைத்து கோப்புகளும்

கீழுள்ள கட்டளைகளில் `<your-username>` என்பதனை உங்கள் ஃபோர்க் URL (அல்லது முன்னணி URL) மூலம் மாற்றவும்.

சமீபத்திய கமிட் வரலாற்றை மட்டும் க்ளோன் செய்ய (சிறிய பதிவிறக்கம்):

```bash|powershell
git clone --depth 1 https://github.com/<your-username>/ai-agents-for-beginners.git
```

குறிப்பிட்ட கிளையை மட்டும் க்ளோன் செய்ய:

```bash|powershell
git clone --depth 1 --branch <branch-name> https://github.com/<your-username>/ai-agents-for-beginners.git
```

#### பகுதி (sparse) க்ளோன் — குறைந்த பிளாப்கள் + தேர்ந்தெடுக்கப்பட்ட கோப்புறைகள் மட்டும்

இது பகுதி க்ளோன் மற்றும் sparse-checkout (Git 2.25+ வேண்டிய மற்றும் பகுதி க்ளோன் ஆதரவுடன் பரிந்துரைக்கப்படுகிறது) பயன்படுத்துகிறது:

```bash|powershell
git clone --depth 1 --filter=blob:none --sparse https://github.com/<your-username>/ai-agents-for-beginners.git
```

ரெபோ கோப்புறையில் செல்:

```bash|powershell
cd ai-agents-for-beginners
```

பிறகு நீங்கள் விரும்பும் கோப்புறைகளை குறிப்பிடவும் (கீழே இரு கோப்புறைகள் காட்டப்பட்டுள்ளன):

```bash|powershell
git sparse-checkout set 00-course-setup 01-intro-to-ai-agents
```

க்ளோன் செய்து கோப்புக்களை உறுதிப்படுத்தியபின், நீங்கள் கோப்புக்களை மட்டும் தேவையில்லையெனில் மற்றும் வசதிக்காக அதிக இடத்தை விடஒதுக்க, ரெபோ மதிப்புரை (metadata) அழிக்கவும் (💀மீண்டும் பெற முடியாதது – இது அனைத்து Git செயல்பாடுகளையும் இழக்கும்: கமிட்கள், புல், புஷ், வரலாறு அணுகல்).

```bash
# zsh/bash
rm -rf .git
```

```powershell
# பவர் ஷெல்
Remove-Item -Recurse -Force .git
```

#### GitHub Codespaces பயன்படுத்துதல் (உள்ளூர் பெரிய பதிவிறக்கத்தைக் தவிர்க்க பரிந்துரைக்கப்படுகிறது)

- இந்த ரெபோவுக்கான புதிய Codespace ஐ [GitHub UI](https://github.com/codespaces) மூலம் உருவாக்கவும்.  

- புதிய Codespace இன் டெர்மினலில், க்கு மேற்கண்ட லேசான/குறைந்தது பகுதிகளை உள்ளடக்கிய க்ளோன் கட்டளைகளில் ஒன்றைப் பயன்படுத்தி தேவையான பாட கோப்புறைகளை மட்டும் Codespace வேலைப்பகுதியில் கொண்டு வரவும்.
- வேண்டுமானால்: Codespaces இல் க்ளோன் செய்தபின் .git ஐ நீக்கி கூடுதல் இடத்தை மீட்டெடுக்கவும் (மேலே உள்ள நீக்க கட்டளைகளை பார்க்கவும்).
- குறிப்பு: Codespaces இல் நேரடியாக ரெபோவை திறக்க விரும்பினால் (க்ளோன் இல்லாமல்), Codespaces devcontainer சூழலை உருவாக்கும் மற்றும் உங்களுக்கு தேவையானதைவிட கூடுதல் அமைப்புகளையும் ஏற்படுத்தும். புதிய Codespace இல் லேசான இணைப்பான க்ளோனிங் உங்களுக்கு டிஸ்க் பயன்பாட்டில் அதிகக் கட்டுப்பாட்டை வழங்கும்.

#### குறிப்புகள்

- எப்போதும் நீங்கள் திருத்த/கமிட் செய்ய விரும்பினால், க்ளோன் URL ஐ உங்கள் ஃபோர்க் URL ஆக மாற்றவும்.
- பிறகு நீங்கள் வரலாறு அல்லது கோப்புகள் அதிகமாக வேண்டுமானால், அவற்றைப் பெறலாம் அல்லது sparse-checkout ஐ மாற்றி கூடுதல் கோப்புறைகளைச் சேர்க்கலாம்.

## கோட் இயக்கல்

இந்த பாடப் பட்டியலில், AI முகவர்களை கட்டுவதற்கான கைபயிற்சி அனுபவம் பெற Jupyter Notebooks தொகுப்பு வழங்கப்படுகின்றன.

கோட் உதாரணங்கள் **Microsoft Agent Framework (MAF)** மற்றும் `FoundryChatClient` பயன்படுத்துகின்றன, இது **Microsoft Foundry Agent Service V2** (Responses API) மூலம் **Microsoft Foundry** என இணைக்கிறது.

அனைத்து Python நோட்புக்குகளும் `*-python-agent-framework.ipynb` என அடையாளம் காணப்படுகின்றன.

## தேவைகள்

- Python 3.12+
  - **குறிப்பு**: உங்களிடம் Python3.12 இல்லையெனில், அதை நிறுவவும். பின்னர் requirements.txt கோப்பில் சேர்க்கப்பட்ட சரியான பதிப்புகளை நிறுவ python3.12 பயன்படுத்தி venv உருவாகவும்.
  
    >உதாரணம்

    Python venv கோப்புறையை உருவாக்கவும்:

    ```bash|powershell
    python -m venv venv
    ```

    பிறகு venv சூழலை இயக்கவும்:

    ```bash
    # zsh/bash
    source venv/bin/activate
    ```
  
    ```dos
    # Command Prompt for Windows
    venv\Scripts\activate
    ```

- .NET 10+: .NET பயன்படுத்தும் மாதிரி கோடுகளுக்காக [.NET 10 SDK](https://dotnet.microsoft.com/download/dotnet/10.0) அல்லது மேல் பதிப்பை நிறுவவும். பின்னர் நிறுவப்பட்ட .NET SDK பதிப்பை சரிபார்க்கவும்:

    ```bash|powershell
    dotnet --list-sdks
    ```

- **Azure CLI** — அங்கீகாரத்திற்கு தேவை. [aka.ms/installazurecli](https://aka.ms/installazurecli) இலிருந்து நிறுவவும்.
- **Azure சந்தா** — Microsoft Foundry மற்றும் Microsoft Foundry Agent Service அணுகுவதற்கு.
- **Microsoft Foundry திட்டம்** — பயன்படுத்த deploy செய்யப்பட்ட மாடலுடன் (உதாரணம்: `gpt-5-mini`). கீழே [படி 1](#படி-1-microsoft-foundry-திட்டம்-உருவாக்கவும்) பார்க.

இந்த ரெபோவை ஜேனரல் ரூட்டில் `requirements.txt` கோப்பை இணைத்திருக்கிறோம், இது கோட் உதாரணங்களை இயக்க தேவையான Python பக்கேஜ்கள் அனைத்தையும் கொண்டுள்ளது.

அதனை நிரலில் கீழ்க்காணும் கட்டளை மூலம் நிறுவலாம்:

```bash|powershell
pip install -r requirements.txt
```

எந்தவொரு முரண்பாடு மற்றும் பிரச்சனைகளைக் தவிர்க்க Python virtual environment உருவாக்க பரிந்துரைக்கப்படுகிறது.

## VSCode அமைக்கவும்

VSCode இல் சரியான Python பதிப்பை நீங்கள் பயன்படுத்துகிறீர்கள் என்பதை உறுதிப்படுத்தவும்.

![image](https://github.com/user-attachments/assets/a85e776c-2edb-4331-ae5b-6bfdfb98ee0e)

## Microsoft Foundry மற்றும் Microsoft Foundry Agent Service அமைத்தல்

### படி 1: Microsoft Foundry திட்டம் உருவாக்கவும்

நோட்புக்குகளை இயக்க, Microsoft Foundry **hub** மற்றும் **project** ஒன்றும் deploy செய்யப்பட்ட மாதிரியுடன் தேவை.

1. [ai.azure.com](https://ai.azure.com) சென்று Azure கணக்குடன் உள்நுழைக.
2. புதிய **hub** உருவாக்கவும் (அல்லது ஏற்கனவே உள்ளதைப் பயன்படுத்தவும்). கண்டு: [Hub resources overview](https://learn.microsoft.com/azure/ai-foundry/concepts/ai-resources).
3. hubக்கு உள், புதிய **project** உருவாக்கவும்.
4. **Models + Endpoints** → **Deploy model** மூலம் ஒரு மாதிரியை (எ.கா., `gpt-5-mini`) உருவாக்கவும்.

### படி 2: உங்கள் திட்ட அம்சத்தையும் மாதிரி பெயரையும் பெறவும்

Microsoft Foundry போர்டலில் உங்கள் திட்டத்திலிருந்து:

- **திட்ட அம்சம்** — **Overview** பக்கத்திற்குச் சென்று அம்ச URLஐ நகலெடுக்கவும்.

![Project Connection String](../../../translated_images/ta/project-endpoint.8cf04c9975bbfbf1.webp)

- **மாதிரி பெயர்** — **Models + Endpoints** இல் deploy செய்யப்பட்ட மாதிரியைத் தேர்ந்தெடுத்து, **Deployment name** (எ.கா., `gpt-5-mini`) குறிப்பு பெறவும்.

### படி 3: `az login` மூலம் Azure ஆக உள்நுழையவும்

அனைத்து நோட்புக்குகளும் **`AzureCliCredential`** மூலம் அங்கீகாரம் பெறும் — எந்த API விசைகளும் தேவையில்லை. இதற்கு Azure CLI வழியாக உள்நுழைய வேண்டும்.

1. **Azure CLI** நிறுவிக்கொள்ளாதிருந்தால்: [aka.ms/installazurecli](https://aka.ms/installazurecli)

2. உள்நுழைய கீழ்காணும் கட்டளையை இயக்கவும்:

    ```bash|powershell
    az login
    ```

    அல்லது, உலாவி இல்லாத தொலை/கோட்ஸ்பேஸ் சூழலில்:

    ```bash|powershell
    az login --use-device-code
    ```

3. உங்களுக்கு கேட்கப்பட்டால் உங்கள் சந்தாவைத் தேர்ந்தெடுக்கவும் — உங்கள் Foundry திட்டம் உள்ள சந்தா தேர்ந்தெடுக்க வேண்டும்.

4. உள்நுழைந்திருப்பதை உறுதிப்படுத்தவும்:

    ```bash|powershell
    az account show
    ```

> **`az login` ஏன்?** நோட்புக்குகள் `azure-identity` தொகுப்பின் `AzureCliCredential` பயன்படுத்தி அங்கீகாரம் பெறுகின்றன. இதனால், உங்கள் Azure CLI அமர்வு அங்கீகாரக் குறியீடுகளை வழங்கும் — உங்கள் `.env` கோப்பில் எந்த API விசைகளோ ரகசியங்களோ தேவையில்லை. இது ஒரு [பாதுகாப்பு சிறந்த நடைமுறை](https://learn.microsoft.com/azure/developer/ai/keyless-connections).

### படி 4: `.env` கோப்பை உருவாக்கவும்

உதாரணக் கோப்பை நகலெடுக்கவும்:

```bash
# zsh/bash
cp .env.example .env
```

```powershell
# பவர் ஷெல்
Copy-Item .env.example .env
```

`.env` திறந்து கீழ்காணும் இரண்டு மதிப்புகளை நிரப்பவும்:

```env
AZURE_AI_PROJECT_ENDPOINT=https://<your-project>.services.ai.azure.com/api/projects/<your-project-id>
AZURE_AI_MODEL_DEPLOYMENT_NAME=gpt-5-mini
```

| மாறி | எங்கே கண்டுபிடிப்பது |
|----------|-----------------|
| `AZURE_AI_PROJECT_ENDPOINT` | Foundry போர்டல் → உங்கள் திட்டம் → **Overview** பக்கம் |
| `AZURE_AI_MODEL_DEPLOYMENT_NAME` | Foundry போர்டல் → **Models + Endpoints** → deploy செய்யப்பட்ட மாதிரியின் பெயர் |

பெரும்பாலான பாடங்களுக்காக இதுவே போதும்! நோட்புக்குகள் உங்கள் `az login` அமர்வின் மூலம் தானாக அங்கீகரிக்கும்.

### படி 5: Python சார்ந்த பகுதிகளைக் நிறுவவும்

```bash|powershell
pip install -r requirements.txt
```

இதை நீங்கள் முன்பு உருவாக்கிய virtual environment இல் இயக்க பரிந்துரைக்கப்படுகிறது.

## பாடம் 5 (Agentic RAG)க்கு கூடுதல் அமைப்புகள்

பாடம் 5, **Azure AI Search** பயன்படுத்துகிறது retrieval-augmented generation க்காக. அந்தபாடத்தை இயக்க திட்டமிட்டால், `.env` கோப்பில் கீழ்காணும் மாறிகளை சேர்க்கவும்:

| மாறி | எங்கே கண்டுபிடிப்பது |
|----------|-----------------|
| `AZURE_SEARCH_SERVICE_ENDPOINT` | Azure போர்டல் → உங்கள் **Azure AI Search** வளம் → **Overview** → URL |
| `AZURE_SEARCH_API_KEY` | Azure போர்டல் → உங்கள் **Azure AI Search** வளம் → **Settings** → **Keys** → பிரதான நிர்வாக விசை |

## நேரடியாக Azure OpenAI ஐ அழைக்கும் பாடங்களுக்கான கூடுதல் அமைப்புகள் (பாடங்கள் 6 மற்றும் 8)

பாடங்கள் 6 மற்றும் 8 இல் சில நோட்புக்குகள் **Responses API** பயன்படுத்தி நேரடியாக **Azure OpenAI** ஐ அழைக்கின்றன, Microsoft Foundry திட்டத்தைக் பயன்படுத்தாது. இந்த உதாரணங்கள் முன்பாக GitHub Models பயன்படுத்தியிருந்தன, இது ஓருவருடத்திற்குப் பிறகு (ஜூலை 2026) நிறுத்தப்படவுள்ளதாகும் மற்றும் Responses API க்கு ஆதரவாகில்லை. அவை இயக்க முயற்சி செய்வதெனில், `.env` கோப்பில் கீழ்காணும் மாறிகளை சேர்க்கவும்:

| மாறி | எங்கே கண்டுபிடிப்பது |
|----------|-----------------|
| `AZURE_OPENAI_ENDPOINT` | Azure போர்டல் → உங்கள் **Azure OpenAI** வளம் → **Keys and Endpoint** → Endpoint (எ.கா., `https://<your-resource>.openai.azure.com`) |
| `AZURE_OPENAI_DEPLOYMENT` | Responses API க்கு ஆதரவான deploy செய்யப்பட்ட மாதிரியின் பெயர் (எ.கா., `gpt-5-mini`) |
| `AZURE_OPENAI_API_KEY` | விருப்பம் — `az login` அல்லது Entra ID அங்கீகாரம் பதிலாக விசை அடிப்படையால் பயன்படுத்தின் மட்டும் |

> Responses API நிலையான `/openai/v1/` endpoint பயன்படுத்துகிறது, ஆகவே `api-version` தேவை இல்லை. விசை இல்லா Entra ID அங்கீகாரம் க்காக `az login` மூலம் உள்நுழையவும்.

## மாற்று வழங்குனர்: MiniMax (OpenAI-போன்ற)

[MiniMax](https://platform.minimaxi.com/) பெரிய சந்தைகளுக்கு (204K குறியீடுகள் வரை) OpenAI-போன்ற API மூலம் சேவை அளிக்கிறது. Microsoft Agent Framework இன் `OpenAIChatClient` எந்த OpenAI-போன்ற endpoint உடனும் வேலை செய்கிறது, ஆகவே Azure OpenAI அல்லது OpenAIக்கு பதிலாக MiniMax ஐ பயன்படுத்தலாம்.

`.env` கோப்பில் இவ்வாறான மாறிகளை சேர்க்கவும்:

| மாறி | எங்கே கண்டுபிடிப்பது |
|----------|-----------------|
| `MINIMAX_API_KEY` | [MiniMax Platform](https://platform.minimaxi.com/) → API விசைகள் |
| `MINIMAX_BASE_URL` | `https://api.minimax.io/v1` (எய்திக்கூடிய மதிப்பு) பயன்படுத்தவும் |
| `MINIMAX_MODEL_ID` | பயன்படுத்தும் மாதிரி பெயர் (எ.கா., `MiniMax-M3`) |

**உதாரண மாதிரிகள்**: `MiniMax-M3` (பரிந்துரைக்கப்படுகிறது), `MiniMax-M2.7`, `MiniMax-M2.7-highspeed` (வேகமான பதில்கள்). மாதிரி பெயர்கள் மற்றும் கிடைக்கும் வசதி காலத்துடன் மாறலாம், மற்றும் உங்கள் கணக்கு அல்லது பகுதியை பொறுத்தது — தற்போதைய பட்டியலின்காக [MiniMax Platform](https://platform.minimaxi.com/) சரிபார்க்கவும். `MiniMax-M3` உங்கள் கணக்கிற்கு கிடைக்காவிட்டால், நீங்கள் அணுகக்கூடிய மற்ற மாதிரியை (எ.கா., `MiniMax-M2.7`) `MINIMAX_MODEL_ID` ஆக அமைக்கவும்.

`OpenAIChatClient` பயன்படுத்தும் கோட் உதாரணங்கள் (எ.கா., பாடம் 14 ஹோட்டல் முன்பதிவு வேலைநடை) `MINIMAX_API_KEY` அமைக்கப்பட்டால் தானாகவே MiniMax கட்டமைப்பை கண்டறிந்து பயன்படுத்தும்.

## மாற்று வழங்குநர்: Foundry Local (மோழி மாதிரிகளை சாதனத்தில் இயக்கு)

[Foundry Local](https://foundrylocal.ai) உள்ளகமாக உங்கள் இயந்திரத்தில் முழுமையாக மொழி மாதிரிகளை பதிவிறக்கம் செய்து, பராமரித்து, OpenAI-போன்ற API வாயிலாக வழங்கும் எளிய இயக்க சூழல் — மேகமோ, Azure சந்தாவோ, API விசைகளோ தேவையில்லை. இணையம் இல்லாமல் வளர்ச்சி, மேக செலவில்லாமல் முயற்சி அல்லது தரவுகளை சாதனத்தில் வைத்திருக்க இதை பயன்படுத்தலாம்.

Microsoft Agent Framework இன் `OpenAIChatClient` எந்த OpenAI-போன்ற endpoint உடனும் வேலை செய்கிறது என்பதால் Foundry Local Azure OpenAIக்கு உள்ளூர் மாற்றாக இருக்கலாம்.

**1. Foundry Local ஐ நிறுவவும்**

```bash
# விண்டோஸ்
winget install Microsoft.FoundryLocal

# மேக் ஓஎஸ்
brew install foundrylocal
```

**2. மாதிரி பதிவிறக்கம் செய்து இயக்கவும்** (இது உள்ளக சேவையையும் துவக்கும்):

```bash
foundry model list          # கிடைக்கும் மாதிரிகளைப் பார்க்கவும்
foundry model run phi-4-mini
```

**3. உள்ளக அம்சத்தை கண்டறிய Python SDK ஐ நிறுவவும்:**

```bash
pip install foundry-local-sdk
```

**4. Microsoft Agent Framework க்கு உங்கள் உள்ளக மாதிரியை குறிப்பிடவும்:**

```python
from foundry_local import FoundryLocalManager
from agent_framework.openai import OpenAIChatClient

# வடிவமைப்பை உள்ளூரில் பதிவிறக்கம் செய்கிறது (தாங்கள் தேவைப்பட்டால்) மற்றும் சேவை செய்கிறது, பிறகு இணைவரையறை/பೋரை கண்டறிகிறது.
manager = FoundryLocalManager("phi-4-mini")

chat_client = OpenAIChatClient(
    base_url=manager.endpoint,      # உதாரணமாக http://localhost:<port>/v1
    api_key=manager.api_key,        # Foundry உள்ளூருக்கான போது எப்பொழுதும் "தேவைப்படாது"
    model_id=manager.get_model_info("phi-4-mini").id,
)

agent = chat_client.as_agent(
    name="LocalAgent",
    instructions="You are a helpful assistant running fully on-device.",
)
```

> **குறிப்பு:** Foundry Local OpenAI-போன்ற **Chat Completions** endpoint ஒன்றை வெளிப்படுத்துகிறது. உள்ளக வளர்ச்சி மற்றும் இணையம் இல்லாத சூழல்களுக்கு அதை பயன்படுத்தவும். முழு **Responses API** அம்சங்களுக்காக (அமைப்புள்ள உரையாடல்கள், ஆழமான கருவி ஒருங்கிணைப்பு, முகவரி-பாணி வளர்ச்சி), பாடங்களில் காட்டப்பட்டுள்ளபோல் **Azure OpenAI** அல்லது **Microsoft Foundry** திட்டங்களை பயன்படுத்தவும். தற்போதைய மாதிரி பட்டியல் மற்றும் தள ஆதரவுக்காக [Foundry Local ஆவணங்கள்](https://foundrylocal.ai) பார்க்கவும்.

## பாடம் 8 (Bing Grounding Workflow)க்கு கூடுதல் அமைப்புகள்


பாடம் 8ல் உள்ள நிபந்தனையுடன் கூடிய வேலைப்ப 흐ிவு நோட்புக் Microsoft Foundry மூலம் **Bing அடிப்படையை** பயன்படுத்துகிறது. அந்த மாதிரியை இயக்க திட்டமிட்டிருந்தால், உங்கள் `.env` கோப்பில் இந்த மாறிலியை சேர்க்கவும்:

| மாறிலி | எங்கு காணலாம் |
|----------|-----------------|
| `BING_CONNECTION_ID` | Microsoft Foundry போர்டல் → உங்கள் திட்டம் → **Management** → **Connected resources** → உங்கள் Bing இணைப்பு → இணைப்பு ஐடியை நகலெடு |

## பிரச்சனைகள் தீர்ப்பு

### macOS இல் SSL சான்றிதழ் சரிபார்ப்பு பிழைகள்

நீங்கள் macOS இல் இருந்தால், கீழ்காணும் பிழை போன்றதை சந்திக்கலாம்:

```plaintext
ssl.SSLCertVerificationError: [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: self-signed certificate in certificate chain
```

இது macOS இல் Python உடன் அறியப்பட்ட பிரச்சனை, எப்போது சிஸ்டம் SSL சான்றிதழ்களை தானாக நம்பவில்லை. பின்வரும் தீர்வுகளை வரிசைப்படுத்திக் கொண்டு முயற்சிக்கவும்:

**விருப்பம் 1: Python உடன் உள்ள Install Certificates ஸ்கிரிப்டை இயக்கவும் (பரிந்துரைக்கப்படுகிறது)**

```bash
# உங்கள் நிறுவிய Python பதிப்பை 3.XX உடன் மாற்றவும் (உதாரணமாக, 3.12 அல்லது 3.13):
/Applications/Python\ 3.XX/Install\ Certificates.command
```

**விருப்பம் 2: உங்கள் நோட்புக் இல் `connection_verify=False` பயன்படுத்தவும் (GitHub Models நோட்பூக்களுக்கு மட்டும்)**

பாடம் 6 நோட்புக் (`06-building-trustworthy-agents/code_samples/06-system-message-framework.ipynb`) இல், ஒரு கருத்திட்ட வேலைபாட்டை ஏற்கனவே உள்ளடக்கியுள்ளனர். கிளையன்ட் உருவாக்கும்போது `connection_verify=False`-ஐ கருத்தை அகற்றி பயன்படுத்தவும்:

```python
client = ChatCompletionsClient(
    endpoint=endpoint,
    credential=AzureKeyCredential(token),
    connection_verify=False,  # சான்றிதழ் பிழைகள் ஏற்படும் போது SSL சரிபார்ப்பை முடக்கு
)
```

> **⚠️ எச்சரிக்கை:** SSL சரிபார்ப்பை முடக்குவது (`connection_verify=False`) சான்றிதழ் சரிபார்ப்பை தாண்டிசொல்லி பாதுகாப்பை குறைக்கும். இது வளர்ச்சி சூழல்களில் தற்காலிக மாற்றாக மட்டுமே பயன்படுத்தவும், உற்பத்தியில் எப்போதும் பயன்படுத்த வேண்டாம்.

**விருப்பம் 3: `truststore` ஐ நிறுவி பயன்படுத்தவும்**

```bash
pip install truststore
```

பின்னர் உங்கள் நோட்புக் அல்லது ஸ்கிரிப்ட் தலைப்பில் பின்வரும் வரியை எந்த நெட்வொர்க் கால் செய்யும் முன்பும் சேர்க்கவும்:

```python
import truststore
truststore.inject_into_ssl()
```

## எங்கேயோ சிக்கியுள்ளீர்களா?

இந்த அமைப்பை இயக்குவதில் ஏதேனும் பிரச்சனை இருந்தால், எங்கள் <a href="https://discord.gg/kzRShWzttr" target="_blank">Azure AI Community Discord</a> இல் சேர்ந்துகொள் அல்லது <a href="https://github.com/microsoft/ai-agents-for-beginners/issues?WT.mc_id=academic-105485-koreyst" target="_blank">ஒரு பிரச்சனை பதிவு செய்</a>.

## அடுத்த பாடம்

இப்போது நீங்கள் இந்த பாடத்திட்டத்தின் குறியீட்டை இயக்க தயாராக உள்ளீர்கள். AI முகவர்களின் உலகத்தைப் பற்றி மேலும் கற்றுக்கொள்ள சந்தோஷமாக இருக்கவும்!

[AI முகவர்கள் அறிமுகம் மற்றும் முகவர் பயன்பாட்டு வழக்குகள்](../01-intro-to-ai-agents/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**மறுப்பு**:
இந்த ஆவணம் AI மொழிபெயர்ப்பு சேவை [Co-op Translator](https://github.com/Azure/co-op-translator) பயன்படுத்தி மொழிபெயர்க்கப்பட்டுள்ளது. நாங்கள் துல்லியத்திற்காக முயற்சி செய்துள்ளோம், ஆனால் தானாக செய்யப்படும் மொழிபெயர்ப்புகளில் பிழைகள் அல்லது தவறுகள் இருக்கலாம் என்பதை கவனத்தில் கொள்ளவும். அசல் ஆவணம் அதன் தாய்மொழியில் அதிகாரப்பூர்வ ஆதாரமாக கருதப்பட வேண்டும். முக்கியமான தகவல்களுக்கு, தொழில்நுட்பமான மனித மொழிபெயர்ப்பு பரிந்துரைக்கப்படுகிறது. இந்த மொழிபெயர்ப்பைப் பயன்படுத்துவதால் ஏற்படும் எந்த தவறான புரிதல்கள் அல்லது தவறான விளக்கத்திற்கும் நாங்கள் பொறுப்பில்வில்லை.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->