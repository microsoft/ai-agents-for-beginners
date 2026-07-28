# कोर्स सेटअप

## प्रस्तावना

हा धडा या कोर्सचे कोड नमुने कसे चालवायचे ते कव्हर करेल.

## इतर शिकणाऱ्यांशी सामील व्हा आणि मदत मिळवा

तुमचे रेपो क्लोन करण्यापूर्वी, सेटअपसाठी कोणतीही मदत, कोर्सच्या संदर्भातील प्रश्न किंवा इतर शिकणाऱ्यांशी जोडण्यासाठी [AI Agents For Beginners Discord channel](https://aka.ms/ai-agents/discord) मध्ये सामील व्हा.

## हे रेपो क्लोन किंवा फोर्क करा

सुरुवात करण्यासाठी, कृपया GitHub रिपॉजिटरी क्लोन किंवा फोर्क करा. यामुळे तुम्हाला कोर्सच्या सामग्रीची स्वतःची आवृत्ती तयार करता येईल ज्यामुळे तुम्ही कोड चालवू, तपासू आणि बदल करू शकता!

हे करण्यासाठी <a href="https://github.com/microsoft/ai-agents-for-beginners/fork" target="_blank">रेपो फोर्क करा</a> या लिंकवर क्लिक करा

तुम्हाला आता खालील लिंकवर तुमच्या स्वतःच्या फोर्क केलेल्या कोर्सची आवृत्ती मिळाली पाहिजे:

![Forked Repo](../../../translated_images/mr/forked-repo.33f27ca1901baa6a.webp)

### शॅलो क्लोन (वर्कशॉप / कोडस्पेसेससाठी शिफारस केलेले)

> संपूर्ण रिपॉजिटरी मोठी (~3 GB) असू शकते जेव्हा तुम्ही पूर्ण इतिहास आणि सर्व फाइल्स डाउनलोड करता. जर तुम्ही फक्त वर्कशॉपला हजर असाल किंवा केवळ काही धडे फोल्डर लागत असतील, तर शॅलो क्लोन (किंवा sparse clone) इतिहास कमी करून आणि/किंवा ब्लॉब्स वगळून बहुतेक डाउनलोड टाळतो.

#### जलद शॅलो क्लोन — किमान इतिहास, सर्व फाइल्स

खालील कमांड्समध्ये `<your-username>` या जागी तुमचा फोर्क URL (किंवा वरचा मूळ URL) टाका.

केवळ नवीनतम कमिट इतिहास क्लोन करण्यासाठी (लहान डाउनलोड):

```bash|powershell
git clone --depth 1 https://github.com/<your-username>/ai-agents-for-beginners.git
```

विशिष्ट शाखा क्लोन करण्यासाठी:

```bash|powershell
git clone --depth 1 --branch <branch-name> https://github.com/<your-username>/ai-agents-for-beginners.git
```

#### आंशिक (sparse) क्लोन — किमान ब्लॉब्स + निवडलेले फोल्डर्स फक्त

हे आंशिक क्लोन आणि sparse-checkout वापरते (Git 2.25+ आवश्यक आणि आंशिक क्लोनसाठी आधुनिक Git शिफारस करतो):

```bash|powershell
git clone --depth 1 --filter=blob:none --sparse https://github.com/<your-username>/ai-agents-for-beginners.git
```

रेपो फोल्डरमध्ये जा:

```bash|powershell
cd ai-agents-for-beginners
```

नंतर तुम्हाला हवे असलेले फोल्डर्स निर्दिष्ट करा (खालील उदाहरण दोन फोल्डर्स दाखवते):

```bash|powershell
git sparse-checkout set 00-course-setup 01-intro-to-ai-agents
```

क्लोन करून फाइल्स तपासल्यानंतर, जर तुम्हाला फक्त फाईली पाहिजे असतील आणि जागा मोकळी करायची असेल (कोणताही git इतिहास नको असेल), तर कृपया रेपो मेटाडेटा हटवा (💀परत न येणारे — तुम्ही सर्व Git कार्यक्षमता गमावाल: कमिट, पुल, पुश किंवा इतिहास पाहणे नाही).

```bash
# झश/बॅश
rm -rf .git
```

```powershell
# पॉवरशेल
Remove-Item -Recurse -Force .git
```

#### GitHub Codespaces वापरणे (स्थानिक मोठे डाउनलोड टाळण्यासाठी शिफारसीय)

- या रिपॉसाठी [GitHub UI](https://github.com/codespaces) द्वारे नवीन Codespace तयार करा.  

- नव्या तयार Codespace च्या टर्मिनलमध्ये, वरील शॅलो/सपार्स क्लोन कमांड्सपैकी एक वापरा जेणेकरून फक्त तुम्हाला हवेलेले धडा फोल्डर्स Codespace कार्यक्षेत्रात येतील.
- ऐच्छिक: Codespaces मध्ये क्लोन केल्यावर, .git काढून अतिरिक्त जागा परत मिळवा (वरील काढण्याच्या कमांड्स पहा).
- लक्षात ठेवा: जर तुम्हाला रिपो थेट Codespaces मध्ये उघडायचा असेल (अतिरिक्त क्लोनशिवाय), तर Codespaces devcontainer वातावरण तयार करतो आणि कदाचित हवेपेक्षा अधिक प्रोव्हिजन करू शकतो. नवीन Codespace मध्ये शॅलो कॉपी क्लोन करणे तुम्हाला डिस्क वापरावर अधिक नियंत्रण देते.

#### टिप्स

- जर तुम्हाला एडिट/कमिट करायचे असेल तर क्लोन URL नेहमी तुमच्या फोर्कने बदला.
- नंतर अधिक इतिहास किंवा फाइल्स लागल्यास, तुम्ही ते फetch करू शकता किंवा sparse-checkout सुधारू शकता ज्या फोल्डर्समध्ये समावेश हवे.

## कोड चालवणे

हा कोर्स तुम्हाला AI एजंट्स बनवण्याचा प्रत्यक्ष अनुभव देणाऱ्या अनेक Jupyter नोटबुक्स प्रदान करतो.

कोड नमुने **Microsoft Agent Framework (MAF)** वापरतात `FoundryChatClient` सोबत, जे **Microsoft Foundry Agent Service V2** (Responses API) द्वारे **Microsoft Foundry** शी जोडते.

सर्व Python नोटबुक्स `*-python-agent-framework.ipynb` असे चिन्हांकित आहेत.

## आवश्यकताः

- Python 3.12+
  - **टीप:** जर Python3.12 स्थापित नसेल तर ते याची खात्री करून स्थापित करा. नंतर तुमचा venv python3.12 वापरून तयार करा जेणेकरून requirements.txt फाइलमधील योग्य आवृत्त्या स्थापित होतील.
  
    >उदाहरण

    Python venv डिरेक्टरी तयार करा:

    ```bash|powershell
    python -m venv venv
    ```

    नंतर खालीलप्रमाणे venv वातावरण सक्रिय करा:

    ```bash
    # झश/बाश
    source venv/bin/activate
    ```
  
    ```dos
    # Command Prompt for Windows
    venv\Scripts\activate
    ```

- .NET 10+: .NET वापरणाऱ्या नमुना कोडसाठी, [.NET 10 SDK](https://dotnet.microsoft.com/download/dotnet/10.0) किंवा त्यानंतरची आवृत्ती स्थापित करा. नंतर तुमची स्थापित .NET SDK आवृत्ती तपासा:

    ```bash|powershell
    dotnet --list-sdks
    ```

- **Azure CLI** — प्रमाणीकरणासाठी आवश्यक. [aka.ms/installazurecli](https://aka.ms/installazurecli) वरून स्थापित करा.
- **Azure Subscription** — Microsoft Foundry आणि Microsoft Foundry Agent Service मध्ये प्रवेशासाठी.
- **Microsoft Foundry Project** — लागू शकलेला मॉडेल असलेला प्रोजेक्ट (उदाहरणार्थ, `gpt-5-mini`). [Step 1](#पायरी-1-microsoft-foundry-प्रोजेक्ट-तयार-करा) पहा.

आम्ही या रिपॉजिटरीच्या रूटमध्ये `requirements.txt` फाइल दिली आहे ज्यात कोड नमुने चालवण्यासाठी आवश्यक सर्व Python पॅकेजेस आहेत.

तुम्ही ती टर्मिनल मध्ये खालील कमांड चालवून स्थापित करू शकता:

```bash|powershell
pip install -r requirements.txt
```

कोणत्याही संघर्ष आणि समस्या टाळण्यासाठी Python व्हर्च्युअल वातावरण तयार करण्याची आम्ही शिफारस करतो.

## VSCode सेटअप करा

VSCode मध्ये योग्य Python आवृत्ती वापरत आहात याची खात्री करा.

![image](https://github.com/user-attachments/assets/a85e776c-2edb-4331-ae5b-6bfdfb98ee0e)

## Microsoft Foundry आणि Microsoft Foundry Agent Service सेटअप करा

### पायरी 1: Microsoft Foundry प्रोजेक्ट तयार करा

तुम्हाला Microsoft Foundry **hub** आणि **project** लागेल ज्यात लागू शकलेला मॉडेल असेल, ज्यामुळे नोटबुक्स चालवता येतील.

1. [ai.azure.com](https://ai.azure.com) वर जा आणि तुमच्या Azure खात्याने साइन इन करा.
2. एक **hub** तयार करा (किंवा आधीच असलेला वापरा). पहा: [Hub resources overview](https://learn.microsoft.com/azure/ai-foundry/concepts/ai-resources).
3. हबच्या आत एक **project** तयार करा.
4. **Models + Endpoints** → **Deploy model** मधून एखादा मॉडेल (उदा., `gpt-5-mini`) लागू करा.

### पायरी 2: तुमचा प्रोजेक्ट एंडपॉइंट आणि मॉडेल डिप्लॉयमेंट नाव मिळवा

Microsoft Foundry पोर्टलमधील तुमच्या प्रोजेक्टमधून:

- **Project Endpoint** — **Overview** पृष्ठावर जा आणि एंडपॉइंट URL कॉपी करा.

![Project Connection String](../../../translated_images/mr/project-endpoint.8cf04c9975bbfbf1.webp)

- **Model Deployment Name** — **Models + Endpoints** मध्ये जाऊन लागू केलेला मॉडेल निवडा आणि **Deployment name** (उदा., `gpt-5-mini`) नोंद करा.

### पायरी 3: `az login` वापरून Azure मध्ये साइन इन करा

सर्व नोटबुक्स प्रमाणीकरणासाठी **`AzureCliCredential`** वापरतात — API की व्यवस्थापित करण्याची गरज नाही. यासाठी Azure CLI द्वारे साइन इन असणे आवश्यक आहे.

1. **Azure CLI स्थापित करा** जर आधी स्थापित नसेल तर: [aka.ms/installazurecli](https://aka.ms/installazurecli)

2. **साइन इन** करा:

    ```bash|powershell
    az login
    ```

    किंवा तुम्ही रिमोट/Codespace वातावरणात असल्यास ज्यात ब्राउझर नाही:

    ```bash|powershell
    az login --use-device-code
    ```

3. **तुमचा सबस्क्रिप्शन निवडा** (जर विचारले गेले) — जो Foundry प्रोजेक्टचा समावेश करतो.

4. **तुम्ही साइन इन आहात का ते तपासा**:

    ```bash|powershell
    az account show
    ```

> **`az login` का?** नोटबुक्स `azure-identity` पॅकेजमधील `AzureCliCredential` वापरून प्रमाणीकरण करतात. याचा म्हणजे तुमच्या Azure CLI सत्राने क्रेडेन्शियल्स पुरवले जातात — `.env` फाइलमध्ये API की किंवा रहस्य नाहीत. ही एक [सुरक्षा उत्तम पद्धत](https://learn.microsoft.com/azure/developer/ai/keyless-connections) आहे.

### पायरी 4: तुमच्या `.env` फाइल तयार करा

खालील उदाहरण फाइल कॉपी करा:

```bash
# zsh/bash
cp .env.example .env
```

```powershell
# पॉवरशेल
Copy-Item .env.example .env
```

`.env` उघडा आणि या दोन मूल्ये भरा:

```env
AZURE_AI_PROJECT_ENDPOINT=https://<your-project>.services.ai.azure.com/api/projects/<your-project-id>
AZURE_AI_MODEL_DEPLOYMENT_NAME=gpt-5-mini
```

| व्हेरिएबल | कुठे शोधायचे |
|----------|-----------------|
| `AZURE_AI_PROJECT_ENDPOINT` | Foundry पोर्टल → तुमचा प्रोजेक्ट → **Overview** पृष्ठ |
| `AZURE_AI_MODEL_DEPLOYMENT_NAME` | Foundry पोर्टल → **Models + Endpoints** → लागू केलेला मॉडेल नाव |

बर्‍याच धड्यांसाठी एवढेच! नोटबुक्स तुमच्या `az login` सत्राद्वारे आपोआप प्रमाणीकरण करतील.

### पायरी 5: Python अवलंबित्वे स्थापित करा

```bash|powershell
pip install -r requirements.txt
```

आम्ही शिफारस करतो की हे तुम्ही आधी तयार केलेल्या व्हर्च्युअल वातावरणात चालवा.

## धडा 5 साठी अतिरिक्त सेटअप (Agentic RAG)

धडा 5 मध्ये **Azure AI Search** वापरले जाते retrieval-augmented generation साठी. जर तुम्ही तो धडा चालवणार असाल, तर `.env` फाइलमध्ये हे व्हेरिएबल्स जोडा:

| व्हेरिएबल | कुठे शोधायचे |
|----------|-----------------|
| `AZURE_SEARCH_SERVICE_ENDPOINT` | Azure पोर्टल → तुमचा **Azure AI Search** रिसोर्स → **Overview** → URL |
| `AZURE_SEARCH_API_KEY` | Azure पोर्टल → तुमचा **Azure AI Search** रिसोर्स → **Settings** → **Keys** → प्राथमिक अॅडमिन की |

## धडे जे Azure OpenAI थेट कॉल करतात त्यासाठी अतिरिक्त सेटअप (धडे 6 आणि 8)

धडे 6 आणि 8 मधील काही नोटबुक्स थेट **Azure OpenAI** कॉल करतात (Responses API चा वापर करून) Microsoft Foundry प्रोजेक्टच्या माध्यमातून न जाऊन. हे नमुने पूर्वी GitHub Models वापरत होते, जे आता वापरात नाही (जुलै 2026 ला सेवानिवृत्त होत आहे) आणि Responses API ला समर्थन देत नाही. जर तुम्ही हे नमुने चालवणार असाल, तर `.env` फाईलमध्ये खालील व्हेरिएबल्स जोडा:

| व्हेरिएबल | कुठे शोधायचे |
|----------|-----------------|
| `AZURE_OPENAI_ENDPOINT` | Azure पोर्टल → तुमचा **Azure OpenAI** रिसोर्स → **Keys and Endpoint** → Endpoint (उदा., `https://<your-resource>.openai.azure.com`) |
| `AZURE_OPENAI_DEPLOYMENT` | तुमच्या लागू केलेल्या मॉडेल चे नाव (उदा., `gpt-5-mini`) जे Responses API समर्थित आहे |
| `AZURE_OPENAI_API_KEY` | ऐच्छिक — जर तुम्ही `az login` / Entra ID ऐवजी की-आधारित प्रमाणीकरण वापरत असाल तर |

> Responses API स्थिर `/openai/v1/` एंडपॉइंट वापरते, त्यामुळे `api-version` आवश्यक नाही. कीलेस Entra ID प्रमाणीकरणासाठी `az login` वापरा.

## पर्यायी प्रदाता: MiniMax (OpenAI-समर्थित)

[MiniMax](https://platform.minimaxi.com/) मोठ्या संदर्भातील मॉडेल्स (204K टोकनपर्यंत) OpenAI-समर्थित API द्वारे प्रदान करते. Microsoft Agent Framework चा `OpenAIChatClient` कोणत्याही OpenAI-समर्थित एंडपॉइंटसह काम करतो, त्यामुळे MiniMax तुमच्या `.env` फाइलमध्ये सेट करून Azure OpenAI किंवा OpenAI च्या पर्यायी म्हणून वापरू शकता.

या व्हेरिएबल्स `.env` मध्ये जोडा:

| व्हेरिएबल | कुठे शोधायचे |
|----------|-----------------|
| `MINIMAX_API_KEY` | [MiniMax Platform](https://platform.minimaxi.com/) → API Keys |
| `MINIMAX_BASE_URL` | वापरा `https://api.minimax.io/v1` (डिफॉल्ट मूल्य) |
| `MINIMAX_MODEL_ID` | वापरायचे मॉडेल नाव (उदा., `MiniMax-M3`) |

**उदाहरण मॉडेल्स:** `MiniMax-M3` (शिफारसीय), `MiniMax-M2.7`, `MiniMax-M2.7-highspeed` (जलद प्रतिसाद). मॉडेल नावे आणि उपलब्धता काळानुसार बदलू शकते, आणि मॉडेल उपलब्धता तुमच्या खात्यावर किंवा प्रदेशावर अवलंबून असू शकते — [MiniMax Platform](https://platform.minimaxi.com/) येथे सध्याची यादी तपासा. जर `MiniMax-M3` तुमच्या खात्याला उपलब्ध नसेल, तर `MINIMAX_MODEL_ID` मध्ये तुम्हाला मिळणारा मॉडेल नाव सेट करा (उदा., `MiniMax-M2.7`).

`OpenAIChatClient` वापरणारे कोड नमुने (उदा., धडा 14 हॉटेल बुकिंग वर्कफ्लो) `MINIMAX_API_KEY` सेट केल्यावर तुमच्या MiniMax कॉन्फिगरेशनचा आपोआप शोध घेतील आणि वापरतील.

## पर्यायी प्रदाता: Foundry Local (डिव्हाइसवर मॉडेल चालवा)

[Foundry Local](https://foundrylocal.ai) ही एक हलकी रनटाइम आहे जी भाषा मॉडेल्स डाउनलोड, व्यवस्थापित करते आणि OpenAI-समर्थित API द्वारे **फक्त तुमच्या संगणकावरच** सेवा करते — कोणतेही क्लाउड, Azure सबस्क्रिप्शन किंवा API की नाहीत. ऑफलाइन विकास, क्लाउड खर्चांशिवाय प्रयोग करण्यासाठी किंवा डिव्हाइसवर डेटा ठेवण्यासाठी ही एक उत्तम पर्याय आहे.

Microsoft Agent Framework चा `OpenAIChatClient` कोणत्याही OpenAI-समर्थित एंडपॉइंटसह काम करतो, त्यामुळे Foundry Local Azure OpenAI साठी स्थानिक पर्याय आहे.

**1. Foundry Local स्थापित करा**

```bash
# विंडोज
winget install Microsoft.FoundryLocal

# मॅकओएस
brew install foundrylocal
```

**2. एक मॉडेल डाउनलोड करा आणि चालवा** (हे स्थानिक सेवा देखील सुरू करेल):

```bash
foundry model list          # उपलब्ध मॉडेल्स पहा
foundry model run phi-4-mini
```

**3. Python SDK स्थापित करा** जे स्थानिक एंडपॉइंट शोधण्यासाठी वापरले जाते:

```bash
pip install foundry-local-sdk
```

**4. Microsoft Agent Framework ला तुमच्या स्थानिक मॉडेलकडे निर्देशित करा:**

```python
from foundry_local import FoundryLocalManager
from agent_framework.openai import OpenAIChatClient

# आवश्यक असल्यास डाउनलोड करतो आणि मॉडेल स्थानिकपणे सेवा देतो, नंतर एंडपॉइंट/पोर्ट शोधतो.
manager = FoundryLocalManager("phi-4-mini")

chat_client = OpenAIChatClient(
    base_url=manager.endpoint,      # उदाहरणार्थ http://localhost:<port>/v1
    api_key=manager.api_key,        # फाउंड्री लोकलसाठी नेहमी "not-required"
    model_id=manager.get_model_info("phi-4-mini").id,
)

agent = chat_client.as_agent(
    name="LocalAgent",
    instructions="You are a helpful assistant running fully on-device.",
)
```

> **टीप:** Foundry Local OpenAI-समर्थित **Chat Completions** एंडपॉइंट उघडते. स्थानिक विकास आणि ऑफलाइन परिस्थितीसाठी याचा वापर करा. संपूर्ण **Responses API** वैशिष्ट्यांसाठी (स्थितीपूर्ण संभाषणे, सखोल टूल ऑर्केस्ट्रेशन, आणि एजंट-शैली विकास), धड्यात दाखवलेल्या प्रमाणे Azure OpenAI किंवा **Microsoft Foundry** प्रोजेक्ट वापरा. सध्याच्या मॉडेल सूची आणि प्लॅटफॉर्म सपोर्टसाठी [Foundry Local दस्तऐवज](https://foundrylocal.ai) पहा.

## धडा 8 साठी अतिरिक्त सेटअप (Bing ग्राउंडिंग वर्कफ्लो)


धडे 8 मधील अटीवर आधारित कार्यप्रवाह नोटबुक Microsoft Foundry द्वारे **Bing ग्राउंडिंग** वापरते. आपण तो नमुना चालवण्याचा विचार करत असल्यास, आपल्या `.env` फाईलमध्ये हा बदलनीय जोडा:

| बदलनीय | कुठे सापडेल |
|----------|-----------------|
| `BING_CONNECTION_ID` | Microsoft Foundry पोर्टल → तुमचा प्रकल्प → **Management** → **Connected resources** → तुमचा Bing कनेक्शन → कनेक्शन आयडी कॉपी करा |

## समस्या निवारण

### macOS वर SSL प्रमाणपत्र पडताळणी त्रुटी

जर तुम्ही macOS वर असून अशा त्रुटीचा सामना करत असाल:

```plaintext
ssl.SSLCertVerificationError: [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: self-signed certificate in certificate chain
```

हे macOS वर Python चे एक ज्ञात गतिरोध आहे जिथे सिस्टम SSL प्रमाणपत्रे आपोआप विश्वासार्ह मानली जात नाहीत. खालील उपाय क्रमाने प्रयत्न करा:

**पर्याय 1: Python च्या Install Certificates स्क्रिप्ट चालवा (शिफारस केलेले)**

```bash
# 3.XX च्या जागी आपली स्थापित केलेली Python आवृत्ती बदला (उदा. 3.12 किंवा 3.13):
/Applications/Python\ 3.XX/Install\ Certificates.command
```

**पर्याय 2: तुमच्या नोटबुकमध्ये `connection_verify=False` वापरा (GitHub Models नोटबुकसाठीच)**

धडा 6 नोटबुकमध्ये (`06-building-trustworthy-agents/code_samples/06-system-message-framework.ipynb`), एका टिप्पणीकृत पर्यायाचा आधीच समावेश आहे. क्लायंट तयार करताना `connection_verify=False` अनकमेंट करा:

```python
client = ChatCompletionsClient(
    endpoint=endpoint,
    credential=AzureKeyCredential(token),
    connection_verify=False,  # प्रमाणपत्र त्रुटी आल्यास SSL पडताळणी अक्षम करा
)
```

> **⚠️ इशारा:** SSL पडताळणी अक्षम करणे (`connection_verify=False`) प्रमाणपत्र पडताळणी वगळल्यामुळे सुरक्षा कमी करते. विकास वातावरणात तात्पुरता उपाय म्हणून याचा वापर करा, उत्पादनात कधीही नाही.

**पर्याय 3: `truststore` इन्स्टॉल करून वापरा**

```bash
pip install truststore
```

त्यानंतर तुमच्या नोटबुक किंवा स्क्रिप्टच्या सुरुवातीला, कोणतेही नेटवर्क कॉल करण्यापूर्वी खालील कोड जोडा:

```python
import truststore
truststore.inject_into_ssl()
```

## कुठे अडकले आहात?

जर तुम्हाला या सेटअपला चालवताना कोणतीही अडचण येत असेल, तर आमच्या <a href="https://discord.gg/kzRShWzttr" target="_blank">Azure AI Community Discord</a> मध्ये सामील व्हा किंवा <a href="https://github.com/microsoft/ai-agents-for-beginners/issues?WT.mc_id=academic-105485-koreyst" target="_blank">इश्यू तयार करा</a>.

## पुढील धडा

तुम्ही आता या अभ्यासक्रमाचा कोड चालवायला तयार आहात. AI एजंट्सच्या जगाबद्दल अधिक शिकण्याचा आनंद घ्या!

[Introduction to AI Agents and Agent Use Cases](../01-intro-to-ai-agents/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**अस्वीकरण**:
हा दस्तऐवज AI भाषांतर सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) चा वापर करून अनुवादित केला आहे. जरी आम्ही अचूकतेसाठी प्रयत्न करतो, तरी कृपया लक्षात घ्या की स्वयंचलित भाषांतरांमध्ये त्रुटी किंवा अचूकतेची कमतरता असू शकते. मूळ दस्तऐवज त्याच्या मूळ भाषेत अधिकृत स्रोत मानला पाहिजे. महत्त्वाची माहिती असल्यास, व्यावसायिक मानवी भाषांतराची शिफारस केली जाते. या भाषांतराच्या वापरामुळे उद्भवणाऱ्या कोणत्याही गैरसमज किंवा चुकीच्या अर्थलावणीसाठी आम्ही जबाबदार नाही.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->