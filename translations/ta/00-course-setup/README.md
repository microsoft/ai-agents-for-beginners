<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "96eb7f95375daa3e91778ca0295a55d9",
  "translation_date": "2025-10-15T08:51:54+00:00",
  "source_file": "00-course-setup/README.md",
  "language_code": "ta"
}
-->
# பாடநெறி அமைப்பு

## அறிமுகம்

இந்த பாடத்தில், இந்த பாடநெறியின் குறியீட்டு மாதிரிகளை எவ்வாறு இயக்குவது என்பதைப் பற்றி கற்றுக்கொள்வீர்கள்.

## மற்ற கற்றலாளர்களுடன் இணைந்து உதவி பெறுங்கள்

உங்கள் ரெப்போவை கிளோன் செய்யத் தொடங்குவதற்கு முன், [AI Agents For Beginners Discord channel](https://aka.ms/ai-agents/discord) இல் இணைந்து அமைப்புக்கு உதவி பெறவும், பாடநெறி தொடர்பான கேள்விகளை கேட்கவும் அல்லது மற்ற கற்றலாளர்களுடன் தொடர்பு கொள்ளவும்.

## இந்த ரெப்போவை கிளோன் செய்யவும் அல்லது ஃபோர்க் செய்யவும்

தொடங்க, தயவுசெய்து GitHub Repository ஐ கிளோன் செய்யவும் அல்லது ஃபோர்க் செய்யவும். இது உங்களுக்கான பாடநெறி பொருளின் தனிப்பட்ட பதிப்பை உருவாக்கும், இதனால் நீங்கள் குறியீட்டை இயக்க, சோதிக்க மற்றும் மாற்றலாம்!

இதைச் செய்ய, <a href="https://github.com/microsoft/ai-agents-for-beginners/fork" target="_blank">ரெப்போவை ஃபோர்க் செய்ய</a> இணைப்பைக் கிளிக் செய்யவும்.

இப்போது, இந்த பாடநெறியின் ஃபோர்க் செய்யப்பட்ட பதிப்பு கீழே உள்ள இணைப்பில் இருக்கும்:

![Forked Repo](../../../translated_images/forked-repo.33f27ca1901baa6a5e13ec3eb1f0ddd3a44d936d91cc8cfb19bfdb9688bd2c3d.ta.png)

### சுருக்கமான கிளோன் (வார்ப்படம் / Codespaces க்கு பரிந்துரைக்கப்படுகிறது)

  >முழு ரெப்போசிடரி பெரியதாக இருக்கலாம் (~3 GB) முழு வரலாற்றையும் அனைத்து கோப்புகளையும் பதிவிறக்கும்போது. நீங்கள் வெறும் வார்ப்படத்தில் கலந்துகொள்வதற்காக அல்லது சில பாடநெறி கோப்புறைகளை மட்டுமே தேவைப்படும் போது, ​​சுருக்கமான கிளோன் (அல்லது ஒரு சுருக்கமான கிளோன்) பெரும்பாலான பதிவிறக்கத்தை தவிர்க்கிறது.

#### விரைவான சுருக்கமான கிளோன் — குறைந்த வரலாறு, அனைத்து கோப்புகளும்

கீழே உள்ள கட்டளைகளில் `<your-username>` ஐ உங்கள் ஃபோர்க் URL (அல்லது உங்களுக்கு விருப்பமானது என்றால் மேலோட்ட URL) உடன் மாற்றவும்.

சமீபத்திய கமிட் வரலாற்றை மட்டுமே கிளோன் செய்ய:

```bash|powershell
git clone --depth 1 https://github.com/<your-username>/ai-agents-for-beginners.git
```

குறிப்பிட்ட கிளையை கிளோன் செய்ய:

```bash|powershell
git clone --depth 1 --branch <branch-name> https://github.com/<your-username>/ai-agents-for-beginners.git
```

#### பகுதி (சுருக்கமான) கிளோன் — குறைந்த ப்ளாப்ஸ் + தேர்ந்தெடுக்கப்பட்ட கோப்புறைகள் மட்டுமே

இது பகுதி கிளோன் மற்றும் சுருக்கமான-சேமிப்பு (Git 2.25+ மற்றும் பகுதி கிளோன் ஆதரவு கொண்ட நவீன Git பரிந்துரைக்கப்படுகிறது) பயன்படுத்துகிறது:

```bash|powershell
git clone --depth 1 --filter=blob:none --sparse https://github.com/<your-username>/ai-agents-for-beginners.git
```

ரெப்போ கோப்புறைக்கு செல்லவும்:

bash க்கு:

```bash
cd ai-agents-for-beginners
```

Powershell க்கு:

```powershell
Set-Location ai-agents-for-beginners
```

பின்னர் நீங்கள் எந்த கோப்புறைகளை விரும்புகிறீர்கள் என்பதை குறிப்பிடவும் (கீழே உள்ள உதாரணம் இரண்டு கோப்புறைகளை காட்டுகிறது):

```bash|powershell
git sparse-checkout set 00-course-setup 01-intro-to-ai-agents
```

கிளோன் செய்து கோப்புகளை சரிபார்த்த பிறகு, நீங்கள் கோப்புகளை மட்டுமே தேவைப்படும் போது மற்றும் இடத்தை விடுவிக்க (git வரலாறு இல்லை), ரெப்போசிடரி மெட்டாடேட்டாவை நீக்கவும் (💀மீளமுடியாதது — நீங்கள் அனைத்து Git செயல்பாடுகளையும் இழக்கிறீர்கள்: கமிட்கள், புல்கள், புஷ்கள் அல்லது வரலாற்று அணுகல்).

Linux/macOS க்கு:

```bash
rm -rf .git
```

Windows க்கு:

```powershell
Remove-Item -Recurse -Force .git
```

#### GitHub Codespaces பயன்படுத்துதல் (உள்ளூர் பெரிய பதிவிறக்கங்களைத் தவிர்க்க பரிந்துரைக்கப்படுகிறது)

- [GitHub UI](https://github.com/codespaces) மூலம் இந்த ரெப்போவுக்கு புதிய Codespace ஒன்றை உருவாக்கவும்.  

- புதிதாக உருவாக்கப்பட்ட Codespace இன் டெர்மினலில், Codespace வேலைப்பகுதியில் உங்களுக்கு தேவையான பாடநெறி கோப்புறைகளை மட்டுமே கொண்டு வர, மேலே உள்ள சுருக்கமான/சுருக்கமான கிளோன் கட்டளைகளில் ஒன்றை இயக்கவும்.
- விருப்பத்தேர்வு: Codespaces உள்ளே கிளோன் செய்த பிறகு, .git ஐ நீக்கி கூடுதல் இடத்தை மீட்டெடுக்கவும் (மேலே உள்ள நீக்கல் கட்டளைகளைப் பார்க்கவும்).
- குறிப்பு: நீங்கள் ரெப்போவை நேரடியாக Codespaces இல் திறக்க விரும்பினால் (கூடுதல் கிளோன் இல்லாமல்), Codespaces devcontainer சூழலை உருவாக்கும் மற்றும் உங்களுக்கு தேவையானதை விட இன்னும் அதிகமாக வழங்கலாம். புதிய Codespace உள்ளே சுருக்கமான நகலை கிளோன் செய்வது டிஸ்க் பயன்பாட்டில் அதிக கட்டுப்பாட்டை உங்களுக்கு வழங்குகிறது.

#### குறிப்புகள்

- நீங்கள் திருத்த/கமிட் செய்ய விரும்பினால், உங்கள் ஃபோர்க் URL ஐ மாற்றவும்.
- பின்னர் மேலும் வரலாறு அல்லது கோப்புகளை தேவைப்படும் போது, ​​அவற்றை பெறலாம் அல்லது சுருக்கமான-சேமிப்பைச் சரிசெய்து கூடுதல் கோப்புறைகளைச் சேர்க்கலாம்.

## குறியீட்டை இயக்குதல்

இந்த பாடநெறி, AI Agents உருவாக்குவதற்கான அனுபவத்தைப் பெறுவதற்கான Jupyter Notebooks தொடர் வழங்குகிறது.

குறியீட்டு மாதிரிகள் கீழே உள்ளவற்றில் ஏதாவது ஒன்றைப் பயன்படுத்துகின்றன:

**GitHub கணக்கு தேவை - இலவசம்**:

1) Semantic Kernel Agent Framework + GitHub Models Marketplace. (semantic-kernel.ipynb) என லேபிள் செய்யப்பட்டுள்ளது.
2) AutoGen Framework + GitHub Models Marketplace. (autogen.ipynb) என லேபிள் செய்யப்பட்டுள்ளது.

**Azure சந்தா தேவை**:
3) Azure AI Foundry + Azure AI Agent Service. (azureaiagent.ipynb) என லேபிள் செய்யப்பட்டுள்ளது.

இந்த மூன்று வகையான உதாரணங்களை முயற்சிக்குமாறு உங்களை ஊக்குவிக்கிறோம், எது உங்களுக்கு சிறந்தது என்பதைப் பார்க்க.

நீங்கள் எந்த விருப்பத்தைத் தேர்ந்தெடுத்தாலும், கீழே உள்ள அமைப்பு படிகளை நீங்கள் பின்பற்ற வேண்டும்:

## தேவைகள்

- Python 3.12+
  - **குறிப்பு**: Python3.12 நிறுவப்படவில்லை என்றால், அதை நிறுவவும். பின்னர் requirements.txt கோப்பிலிருந்து சரியான பதிப்புகள் நிறுவப்படுவதை உறுதிப்படுத்த python3.12 ஐப் பயன்படுத்தி உங்கள் venv ஐ உருவாக்கவும்.
  
    >உதாரணம்

    Python venv கோப்புறை உருவாக்கவும்:

    ``` bash
    python3 -m venv venv
    ```

    பின்னர் venv சூழலை செயல்படுத்தவும்:

    macOS மற்றும் Linux

    ```bash
    source venv/bin/activate
    ```
  
    Windows

    ```bash
    venv\Scripts\activate
    ```

- GitHub கணக்கு - GitHub Models Marketplace ஐ அணுக
- Azure சந்தா - Azure AI Foundry ஐ அணுக
- Azure AI Foundry கணக்கு - Azure AI Agent Service ஐ அணுக

இந்த ரெப்போசிடரியின் மூலத்தில் உள்ள `requirements.txt` கோப்பில், குறியீட்டு மாதிரிகளை இயக்க தேவையான அனைத்து Python தொகுதிகளும் உள்ளன.

நீங்கள் அதை ரெப்போசிடரியின் மூலத்தில் உங்கள் டெர்மினலில் கீழே உள்ள கட்டளையை இயக்குவதன் மூலம் நிறுவலாம்:

```bash
pip install -r requirements.txt
```
Python மெய்நிகர் சூழலை உருவாக்க பரிந்துரைக்கிறோம், எந்த முரண்பாடுகள் மற்றும் சிக்கல்களையும் தவிர்க்க.

## VSCode அமைப்பு
VSCode இல் சரியான Python பதிப்பைப் பயன்படுத்துகிறீர்கள் என்பதை உறுதிப்படுத்தவும்.

![image](https://github.com/user-attachments/assets/a85e776c-2edb-4331-ae5b-6bfdfb98ee0e)

## GitHub Models ஐப் பயன்படுத்தி மாதிரிகளை அமைக்கவும் 

### படி 1: உங்கள் GitHub தனிப்பட்ட அணுகல் டோக்கனை (PAT) பெறவும்

இந்த பாடநெறி GitHub Models Marketplace ஐ பயன்படுத்துகிறது, இது உங்களுக்கு AI Agents உருவாக்க பயன்படுத்தப்படும் பெரிய மொழி மாதிரிகளை (LLMs) இலவசமாக அணுக அனுமதிக்கிறது.

GitHub Models ஐப் பயன்படுத்த, நீங்கள் [GitHub Personal Access Token](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens) ஐ உருவாக்க வேண்டும்.

இது உங்கள் GitHub கணக்கில் உள்ள <a href="https://github.com/settings/personal-access-tokens" target="_blank">Personal Access Tokens settings</a> க்கு சென்று செய்யலாம்.

உங்கள் டோக்கனை உருவாக்கும்போது [Principle of Least Privilege](https://docs.github.com/en/get-started/learning-to-code/storing-your-secrets-safely) ஐ பின்பற்றவும். இது இந்த பாடநெறியில் குறியீட்டு மாதிரிகளை இயக்க டோக்கனுக்கு தேவையான அனுமதிகளை மட்டுமே வழங்க வேண்டும் என்பதைக் குறிக்கிறது.

1. **Developer settings** க்கு சென்று உங்கள் திரையின் இடது பக்கத்தில் உள்ள `Fine-grained tokens` விருப்பத்தைத் தேர்ந்தெடுக்கவும்.
   ![](../../../translated_images/profile_developer_settings.410a859fe749c755c859d414294c5908e307222b2c61819c3203bbeed4470e25.ta.png)

    பின்னர் `Generate new token` ஐத் தேர்ந்தெடுக்கவும்.

    ![Generate Token](../../../translated_images/fga_new_token.1c1a234afe202ab37483944a291ee80c1868e1e78082fd6bd4180fea5d5a15b4.ta.png)

2. உங்கள் டோக்கனின் நோக்கத்தை பிரதிபலிக்கும் ஒரு விளக்கமான பெயரை உள்ளீடு செய்யவும், பின்னர் அதை எளிதாக அடையாளம் காணலாம்.


    🔐 டோக்கன் காலாவதியான பரிந்துரை

    பரிந்துரைக்கப்பட்ட காலம்: 30 நாட்கள்
    மேலும் பாதுகாப்பான நிலைப்பாட்டிற்காக, குறுகிய காலத்தைத் தேர்ந்தெடுக்கலாம்—7 நாட்கள் 🛡️ போன்றவை
    இது ஒரு தனிப்பட்ட இலக்கை அமைத்து, உங்கள் கற்றல் வேகத்தை அதிகரிக்கும் போது பாடநெறியை முடிக்க ஒரு சிறந்த வழி 🚀.

    ![Token Name and Expiration](../../../translated_images/token-name-expiry-date.a095fb0de63868640a4c82d6b1bbc92b482930a663917a5983a3c7cd1ef86b77.ta.png)

3. இந்த ரெப்போசிடரியின் ஃபோர்க் வரைபடத்திற்கு டோக்கனின் அளவை வரையறுக்கவும்.

    ![Limit scope to fork repository](../../../translated_images/token_repository_limit.924ade5e11d9d8bb6cd21293987e4579dea860e2ba66d607fb46e49524d53644.ta.png)

4. டோக்கனின் அனுமதிகளை வரையறுக்கவும்: **Permissions** கீழ், **Account** தாவலை கிளிக் செய்து, "+ Add permissions" பொத்தானை கிளிக் செய்யவும். ஒரு டிராப்டவுன் தோன்றும். தயவுசெய்து **Models** ஐ தேடி, அதற்கான பெட்டியைச் சரிபார்க்கவும்.
    ![Add Models Permission](../../../translated_images/add_models_permissions.c0c44ed8b40fc143dc87792da9097d715b7de938354e8f771d65416ecc7816b8.ta.png)

5. டோக்கனை உருவாக்குவதற்கு முன், தேவையான அனுமதிகளை சரிபார்க்கவும். ![Verify Permissions](../../../translated_images/verify_permissions.06bd9e43987a8b219f171bbcf519e45ababae35b844f5e9757e10afcb619b936.ta.png)

6. டோக்கனை உருவாக்குவதற்கு முன், நீங்கள் அதை ஒரு பாதுகாப்பான இடத்தில், பாஸ்வேர்ட் மேலாளர் வால்ட் போன்றவற்றில் சேமிக்க தயாராக இருக்க வேண்டும், ஏனெனில் நீங்கள் அதை உருவாக்கிய பிறகு மீண்டும் காண முடியாது. ![Store Token Securely](../../../translated_images/store_token_securely.08ee2274c6ad6caf3482f1cd1bad7ca3fdca1ce737bc485bfa6499c84297c789.ta.png)

நீங்கள் தற்போது உருவாக்கிய புதிய டோக்கனை நகலெடுக்கவும். இந்த பாடநெறியில் உள்ள `.env` கோப்பில் இதைச் சேர்க்க வேண்டும்.


### படி 2: உங்கள் `.env` கோப்பை உருவாக்கவும்

உங்கள் டெர்மினலில் கீழே உள்ள கட்டளையை இயக்கி உங்கள் `.env` கோப்பை உருவாக்கவும்.

```bash
cp .env.example .env
```

இது உதாரண கோப்பை நகலெடுத்து, உங்கள் கோப்புறையில் `.env` ஐ உருவாக்கும், மேலும் நீங்கள் சுற்றுச்சூழல் மாறிகள் மதிப்புகளை நிரப்ப வேண்டும்.

உங்கள் டோக்கனை நகலெடுத்து, உங்கள் விருப்பமான உரை திருத்தியில் `.env` கோப்பைத் திறந்து, உங்கள் டோக்கனை `GITHUB_TOKEN` புலத்தில் ஒட்டவும்.
![GitHub Token Field](../../../translated_images/github_token_field.20491ed3224b5f4ab24d10ced7a68c4aba2948fe8999cfc8675edaa16f5e5681.ta.png)


இப்போது நீங்கள் இந்த பாடநெறியின் குறியீட்டு மாதிரிகளை இயக்க முடியும்.

## Azure AI Foundry மற்றும் Azure AI Agent Service ஐப் பயன்படுத்தி மாதிரிகளை அமைக்கவும்

### படி 1: உங்கள் Azure திட்ட இறுதிப்புள்ளியைப் பெறவும்


Azure AI Foundry இல் ஒரு ஹப் மற்றும் திட்டத்தை உருவாக்குவதற்கான படிகளை பின்பற்றவும்: [Hub resources overview](https://learn.microsoft.com/en-us/azure/ai-foundry/concepts/ai-resources)


திட்டத்தை உருவாக்கிய பிறகு, உங்கள் திட்டத்திற்கான இணைப்பு சரத்தைப் பெற வேண்டும்.

இது Azure AI Foundry போர்டலின் **Overview** பக்கத்திற்கு சென்று செய்யலாம்.

![Project Connection String](../../../translated_images/project-endpoint.8cf04c9975bbfbf18f6447a599550edb052e52264fb7124d04a12e6175e330a5.ta.png)

### படி 2: உங்கள் `.env` கோப்பை உருவாக்கவும்

உங்கள் டெர்மினலில் கீழே உள்ள கட்டளையை இயக்கி உங்கள் `.env` கோப்பை உருவாக்கவும்.

```bash
cp .env.example .env
```

இது உதாரண கோப்பை நகலெடுத்து, உங்கள் கோப்புறையில் `.env` ஐ உருவாக்கும், மேலும் நீங்கள் சுற்றுச்சூழல் மாறிகள் மதிப்புகளை நிரப்ப வேண்டும்.

உங்கள் டோக்கனை நகலெடுத்து, உங்கள் விருப்பமான உரை திருத்தியில் `.env` கோப்பைத் திறந்து, உங்கள் டோக்கனை `PROJECT_ENDPOINT` புலத்தில் ஒட்டவும்.

### படி 3: Azure இல் உள்நுழையவும்

ஒரு பாதுகாப்பு சிறந்த நடைமுறையாக, Microsoft Entra ID உடன் Azure OpenAI க்கு அங்கீகாரம் செய்ய [keyless authentication](https://learn.microsoft.com/azure/developer/ai/keyless-connections?tabs=csharp%2Cazure-cli?WT.mc_id=academic-105485-koreyst) ஐப் பயன்படுத்துவோம். 

அடுத்ததாக, ஒரு டெர்மினலைத் திறந்து `az login --use-device-code` ஐ இயக்கி உங்கள் Azure கணக்கில் உள்நுழைக.

நீங்கள் உள்நுழைந்த பிறகு, டெர்மினலில் உங்கள் சந்தாவைத் தேர்ந்தெடுக்கவும்.


## கூடுதல் சுற்றுச்சூழல் மாறிகள் - Azure Search மற்றும் Azure OpenAI 

Agentic RAG பாடம் - பாடம் 5 - Azure Search மற்றும் Azure OpenAI ஐப் பயன்படுத்தும் மாதிரிகளை உள்ளடக்கியது.

இந்த மாதிரிகளை இயக்க விரும்பினால், உங்கள் `.env` கோப்பில் பின்வரும் சுற்றுச்சூழல் மாறிகளைச் சேர்க்க வேண்டும்:

### மேற்பார்வை பக்கம் (திட்டம்)

- `AZURE_SUBSCRIPTION_ID` - உங்கள் திட்டத்தின் **Overview** பக்கத்தில் **Project details** ஐ சரிபார்க்கவும்.

- `AZURE_AI_PROJECT_NAME` - உங்கள் திட்டத்தின் **Overview** பக்கத்தின் மேல் பார்க்கவும்.

- `AZURE_OPENAI_SERVICE` - **Overview** பக்கத்தில் **Azure OpenAI Service** க்கான **Included capabilities** தாவலில் இதைத் தேடவும்.

### மேலாண்மை மையம்

- `AZURE_OPENAI_RESOURCE_GROUP` - **Management Center** இன் **Overview** பக்கத்தில் **Project properties** க்கு செல்லவும்.

- `GLOBAL_LLM_SERVICE` - **Connected resources** கீழ், **Azure AI Services** இணைப்பு பெயரைத் தேடவும். பட்டியலில் இல்லை என்றால், உங்கள் ரிசோர்ஸ் குழுவின் **Azure portal** இல் AI Services resource name ஐ சரிபார்க்கவும்.

### மாதிரிகள் + இறுதிப்புள்ளிகள் பக்கம்

- `AZURE_OPENAI_EMBEDDING_DEPLOYMENT_NAME` - உங்கள் embedding மாதிரியைத் தேர்ந்தெடுக்கவும் (எ.கா., `text-embedding-ada-002`) மற்றும் மாதிரி விவரங்களில் இருந்து **Deployment name** ஐ கவனிக்கவும்.

- `AZURE_OPENAI_CHAT_DEPLOYMENT_NAME` - உங்கள் chat மாதிரியைத் தேர்ந்தெடுக்கவும் (எ.கா., `gpt-4o-mini`) மற்றும் மாதிரி விவரங்களில் இருந்து **Deployment name** ஐ கவனிக்கவும்.

### Azure Portal

- `AZURE_OPENAI_ENDPOINT` - **Azure AI services** ஐ தேடவும், அதை கிளிக் செய்யவும், பின்னர் **Resource Management**, **Keys and Endpoint** க்கு செல்லவும், "Azure OpenAI endpoints" வரை கீழே ஸ்க்ரோல் செய்து, "Language APIs" என்று கூறும் ஒன்றை நகலெடுக்கவும்.

- `AZURE_OPENAI_API_KEY` - அதே திரையில் இருந்து, KEY 1 அல்லது KEY 2 ஐ நகலெடுக்கவும்.

- `AZURE_SEARCH_SERVICE_ENDPOINT` - உங்கள் **Azure AI Search** வளத்தைத் தேடவும், அதை கிளிக் செய்யவும், **Overview** ஐப் பார்க்கவும்.

- `AZURE_SEARCH_API_KEY` - பின்னர் **Settings** க்கு சென்று **Keys** க்கு சென்று முதன்மை அல்லது துணை நிர்வாக விசையை நகலெடுக்கவும்.

### வெளிப்புற வலைப்பக்கம்

- `AZURE_OPENAI_API_VERSION` - [API version lifecycle](https://learn.microsoft.com/en-us/azure/ai-services/openai/api-version-deprecation#latest-ga-api-release) பக்கத்தை **Latest GA API release** கீழ் பார்வையிடவும்.

### Keyless authentication அமைக்கவும்

உங்கள் சான்றுகளை கடினமாக்காமல், Azure OpenAI உடன் keyless இணைப்பைப் பயன்படுத்துவோம். இதற்காக, `DefaultAzureCredential` ஐ இறக்குமதி செய்து, பின்னர் `DefaultAzureCredential` செயல்பாட்டை அழைத்து சான்றை பெறுவோம்.

```python
from azure.identity import DefaultAzureCredential, InteractiveBrowserCredential
```

## ஏதேனும் இடத்தில் சிக்கியுள்ளீர்களா?
இந்த அமைப்பை இயக்குவதில் ஏதேனும் சிக்கல்கள் இருந்தால், எங்கள் <a href="https://discord.gg/kzRShWzttr" target="_blank">Azure AI Community Discord</a> அல்லது <a href="https://github.com/microsoft/ai-agents-for-beginners/issues?WT.mc_id=academic-105485-koreyst" target="_blank">ஒரு பிரச்சினையை உருவாக்கவும்</a>.

## அடுத்த பாடம்

இந்த பாடத்திற்கான குறியீட்டை இயக்க தயாராக உள்ளீர்கள். AI முகவர்களின் உலகத்தை மேலும் அறிந்து மகிழுங்கள்!

[AI முகவர்கள் மற்றும் முகவர் பயன்பாட்டு வழக்குகள் அறிமுகம்](../01-intro-to-ai-agents/README.md)

---

**குறிப்பு**:  
இந்த ஆவணம் AI மொழிபெயர்ப்பு சேவை [Co-op Translator](https://github.com/Azure/co-op-translator) பயன்படுத்தி மொழிபெயர்க்கப்பட்டுள்ளது. நாங்கள் துல்லியத்திற்காக முயற்சிக்கிறோம், ஆனால் தானியங்கி மொழிபெயர்ப்புகளில் பிழைகள் அல்லது தவறுகள் இருக்கக்கூடும் என்பதை கவனத்தில் கொள்ளவும். அதன் தாய்மொழியில் உள்ள மூல ஆவணம் அதிகாரப்பூர்வ ஆதாரமாக கருதப்பட வேண்டும். முக்கியமான தகவல்களுக்கு, தொழில்முறை மனித மொழிபெயர்ப்பு பரிந்துரைக்கப்படுகிறது. இந்த மொழிபெயர்ப்பைப் பயன்படுத்துவதால் ஏற்படும் எந்த தவறான புரிதல்கள் அல்லது தவறான விளக்கங்களுக்கு நாங்கள் பொறுப்பல்ல.