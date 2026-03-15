# कोर्स सेटअप

## परिचय

हा धडा या कोर्समधील कोड सॅम्पल्स कसे चालवायचे हे सांगेल.

## इतर शिकणाऱ्यांशी जुळा आणि मदत मिळवा

आपल्या रेपो क्लोन करण्यापूर्वी, सेटअपसाठी मदत घेण्यासाठी, कोर्सबद्दल कोणतेही प्रश्न असल्यास किंवा इतर शिकणाऱ्यांशी संपर्क साधण्यासाठी [AI Agents For Beginners Discord channel](https://aka.ms/ai-agents/discord) मध्ये सामील व्हा.

## हा रेपो क्लोन किंवा फोर्क करा

सुरवात करण्यासाठी, कृपया GitHub रेपॉजिटरीचे क्लोन किंवा फोर्क करा. यामुळे आपल्याला कोर्स सामग्रीची स्वतःची आवृत्ती मिळेल जी आपण चालवू, तपासू आणि कोडमध्ये बदल करू शकता!

हे करण्यासाठी, <a href="https://github.com/microsoft/ai-agents-for-beginners/fork" target="_blank">रेपो फोर्क करण्यासाठी</a> लिंकवर क्लिक करा.

आपल्याकडे आता खालील लिंकवर या कोर्सची आपली फोर्क केलेली आवृत्ती असावी:

![Forked Repo](../../../translated_images/mr/forked-repo.33f27ca1901baa6a.webp)

### शॉलो क्लोन (कार्यशाळा / Codespaces साठी शिफारस)

  > पूर्ण रेपो डाउनलोड करताना संपूर्ण इतिहास आणि सर्व फाइल्स मोठ्या प्रमाणात (~3 GB) असू शकतात. आपण फक्त कार्यशाळेत सहभागी असाल किंवा फक्त काही धड्यांच्या फोल्डर्सची गरज असेल, तर शॉलो क्लोन (किंवा sparse clone) इतिहास कमी करून किंवा ब्लॉब्स वगळून त्यापैकी बहुसंख्य डाउनलोड टाळतो.

#### जलद शॉलो क्लोन — किमान इतिहास, सर्व फाइल्स

खालील कमांडमध्ये `<your-username>` ला आपल्या फोर्क URL ने बदला (किंवा अपस्ट्रीम URL वापरू इच्छित असल्यास).

फक्त नवीनतम कमिट इतिहास क्लोन करण्यासाठी (लहान डाउनलोड):

```bash|powershell
git clone --depth 1 https://github.com/<your-username>/ai-agents-for-beginners.git
```

विशिष्ट शाखा क्लोन करण्यासाठी:

```bash|powershell
git clone --depth 1 --branch <branch-name> https://github.com/<your-username>/ai-agents-for-beginners.git
```

#### आंशिक (स्पार्स) क्लोन — किमान ब्लॉब्स + निवडक फोल्डर्स

हे आंशिक क्लोन आणि sparse-checkout वापरते (Git 2.25+ आवश्यक आणि आंशिक क्लोन सपोर्टसह मॉडर्न Git शिफारसीत आहे):

```bash|powershell
git clone --depth 1 --filter=blob:none --sparse https://github.com/<your-username>/ai-agents-for-beginners.git
```

रेपो फोल्डरमध्ये जा:

```bash|powershell
cd ai-agents-for-beginners
```

नंतर तुम्हाला हव्या असलेल्या फोल्डर्स निर्दिष्ट करा (खालील उदाहरणात दोन फोल्डर्स दाखवले आहेत):

```bash|powershell
git sparse-checkout set 00-course-setup 01-intro-to-ai-agents
```

क्लोनिंग आणि फाइल्स तपासल्यानंतर, जर तुम्हाला फक्त फाइल्स पाहिजेत आणि जागा मोकळी करायची असेल (कोणतीही git historia आवश्यक नाही), तर कृपया रेपॉजिटरी मेटाडेटा काढून टाका (💀परत न येणारे — यामुळे सर्व Git कार्यक्षमता हरवेल: कमिट, पुल, पुश किंवा इतिहास प्रवेश नाही).

```bash
# zsh/bash
rm -rf .git
```

```powershell
# पॉवरशेल
Remove-Item -Recurse -Force .git
```

#### GitHub Codespaces वापरणे (स्थानिक मोठ्या डाउनलोड टाळण्यासाठी शिफारस केली आहे)

- या रेपोकरिता नवीन Codespace तयार करा [GitHub UI](https://github.com/codespaces) द्वारे.

- नव्याने तयार केलेल्या codespace च्या टर्मिनल मध्ये वर दिलेल्या शॉलो/स्पार्स क्लोन कमांडपैकी एक चालवा ज्यामुळे फक्त तुम्हाला हव्या असलेल्या धडा फोल्डर्स Codespace वर्कस्पेस मध्ये येतील.
- ऐच्छिक: Codespaces मध्ये क्लोन केल्यानंतर, अधिक जागा रिकामी करण्यासाठी .git काढून टाका (वरील काढण्याच्या कमांड्स पहा).
- टीप: जर तुम्हाला रेपो थेट Codespaces मध्ये उघडायचे असेल (अतिअधिक क्लोन शिवाय), तर लक्षात घ्या की Codespaces devcontainer पर्यावरण तयार करेल आणि कदाचित तुम्हाला हवे असल्यापेक्षा जास्त संसाधने वितरित करू शकतो. नवीन Codespace मध्ये शॉलो डाउनलोड क्लोन केल्याने डिस्क वापरावर अधिक नियंत्रण मिळते.

#### टीपा

- संपादित किंवा कमिट करण्यासाठी नेहमी क्लोन URL बदलून तुमच्या फोर्कचा URL वापरा.
- नंतर अधिक इतिहास किंवा फाइल्स पाहिजेत तर आपण त्यांना fetch करू शकता किंवा sparse-checkout अजस्ट करू शकता.

## कोड चालविणे

हा कोर्स तुम्हाला AI Agents तयार करण्याचा अनुभव देण्यासाठी अनेक Jupyter नोटबुक्स देतो, जे तुम्ही चालवू शकता.

कोड सॅम्पल्स **Microsoft Agent Framework (MAF)** वापरतात ज्यात `AzureAIProjectAgentProvider` असतो, जो **Azure AI Agent Service V2** (Responses API) शी **Microsoft Foundry** च्या माध्यमातून जोडतो.

सर्व Python नोटबुक्स `*-python-agent-framework.ipynb` असे लेबल केलेले आहेत.

## आवश्यकताः

- Python 3.12+
  - **टीप:** जर तुमच्याकडे Python 3.12 स्थापित नसेल, तर ते इंस्टॉल करा. नंतर python3.12 वापरून venv तयार करा, ज्यामुळे requirements.txt फाइलमधील योग्य आवृत्त्या स्थापित होतील.
  
    >उदाहरण

    Python venv निर्देशिका तयार करा:

    ```bash|powershell
    python -m venv venv
    ```

    नंतर venv पर्यावरण सक्रिय करा:

    ```bash
    # zsh/bash
    source venv/bin/activate
    ```
  
    ```dos
    # Command Prompt for Windows
    venv\Scripts\activate
    ```

- .NET 10+: .NET वापरून सॅम्पल कोड्ससाठी, [.NET 10 SDK](https://dotnet.microsoft.com/download/dotnet/10.0) किंवा त्यापुढील आवृत्ती स्थापित करा. नंतर, तुमची .NET SDK आवृत्ती तपासा:

    ```bash|powershell
    dotnet --list-sdks
    ```

- **Azure CLI** — प्रमाणीकरणासाठी आवश्यक. [aka.ms/installazurecli](https://aka.ms/installazurecli) वरून इंस्टॉल करा.
- **Azure Subscription** — Microsoft Foundry आणि Azure AI Agent Service च्या प्रवेशासाठी.
- **Microsoft Foundry प्रोजेक्ट** — एक प्रोजेक्ट ज्यात तैनात मॉडेल आहे (उदा. `gpt-4o`). खाली [Step 1](../../../00-course-setup) पहा.

या रेपॉजिटरीच्या मूळ फोल्डरमध्ये `requirements.txt` फाइल समाविष्ट करण्यात आली आहे, ज्यात कोड सॅम्पल्स चालविण्यासाठी आवश्यक असलेल्या सर्व Python पॅकेजेस आहेत.

तुम्ही ते टर्मिनल मधून खालील कमांड चालवून स्थापित करू शकता:

```bash|powershell
pip install -r requirements.txt
```

कोणत्याही संघर्ष किंवा अडचणी टाळण्यासाठी Python virtual environment तयार करण्याचा आम्ही सल्ला देतो.

## VSCode सेटअप करा

VSCode मध्ये योग्य Python आवृत्ती वापरत असल्याची खात्री करा.

![image](https://github.com/user-attachments/assets/a85e776c-2edb-4331-ae5b-6bfdfb98ee0e)

## Microsoft Foundry आणि Azure AI Agent Service चे सेटअप करा

### चरण 1: Microsoft Foundry प्रोजेक्ट तयार करा

तुम्हाला एखादा Azure AI Foundry **हब** आणि **प्रोजेक्ट** आवश्यक आहे ज्यात तैनात मॉडेल असेल, जेणेकरून नोटबुक्स चालवता येतील.

1. [ai.azure.com](https://ai.azure.com) वर जा आणि Azure खात्याने साइन इन करा.
2. एक **हब** तयार करा (किंवा विद्यमान हब वापरा). पहा: [Hub resources overview](https://learn.microsoft.com/azure/ai-foundry/concepts/ai-resources).
3. त्या हबमध्ये एक **प्रोजेक्ट** तयार करा.
4. **Models + Endpoints** → **Deploy model** कडे जाऊन एखादे मॉडेल (उदा. `gpt-4o`) तैनात करा.

### चरण 2: तुमचा प्रोजेक्ट एंडपॉइंट आणि मॉडेल डिप्लॉयमेंट नाव मिळवा

Microsoft Foundry पोर्टलमधील तुमच्या प्रोजेक्टमधून:

- **Project Endpoint** — **Overview** पृष्ठावर जा आणि एंडपॉइंट URL कॉपी करा.

![Project Connection String](../../../translated_images/mr/project-endpoint.8cf04c9975bbfbf1.webp)

- **Model Deployment Name** — **Models + Endpoints** मध्ये जा, तैनात केलेले मॉडेल निवडा, आणि **Deployment name** (उदा. `gpt-4o`) नोंद करा.

### चरण 3: `az login` वापरून Azure मध्ये साइन इन करा

सर्व नोटबुक्स प्रमाणीकरणासाठी **`AzureCliCredential`** वापरतात — API कीज व्यवस्थापित करण्याची गरज नाही. यासाठी Azure CLI द्वारे साइन इन केलेले असणे आवश्यक आहे.

1. **Azure CLI इंस्टॉल करा** जर आधीच स्थापित नसेल तर: [aka.ms/installazurecli](https://aka.ms/installazurecli)

2. **साइन इन करा** खालील आदेश चालवून:

    ```bash|powershell
    az login
    ```

    किंवा तुम्ही दूरस्थ/Codespace पर्यावरणात असाल आणि ब्राउझर नसेल तर:

    ```bash|powershell
    az login --use-device-code
    ```

3. **सदस्यता निवडा** जर विचारले गेले तर — त्यातील प्रोजेक्ट असलेल्या सदस्यता निवडा.

4. **सत्यापित करा** की साइन इन झालेले आहात:

    ```bash|powershell
    az account show
    ```

> **`az login` का?** नोटबुक्समध्ये `azure-identity` पॅकेजमधील `AzureCliCredential` वापरून प्रमाणीकरण होते. यामुळे तुमची Azure CLI सत्र क्रेडेन्शियल पुरवते — कोणतीही API कीज किंवा गुपिते `.env` फाइलमध्ये न ठेवता. हा एक [सुरक्षेचा उत्तम मार्ग](https://learn.microsoft.com/azure/developer/ai/keyless-connections) आहे.

### चरण 4: तुमची `.env` फाइल तयार करा

उदाहरण फाइल कॉपी करा:

```bash
# झश/बाश
cp .env.example .env
```

```powershell
# पॉवरशेल
Copy-Item .env.example .env
```

`.env` उघडा आणि खालील दोन मूल्ये भरा:

```env
AZURE_AI_PROJECT_ENDPOINT=https://<your-project>.services.ai.azure.com/api/projects/<your-project-id>
AZURE_AI_MODEL_DEPLOYMENT_NAME=gpt-4o
```

| व्हेरिएबल | कुठे शोधायचे |
|----------|-----------------|
| `AZURE_AI_PROJECT_ENDPOINT` | Foundry पोर्टल → तुमचा प्रोजेक्ट → **Overview** पृष्ठ |
| `AZURE_AI_MODEL_DEPLOYMENT_NAME` | Foundry पोर्टल → **Models + Endpoints** → तुमच्या तैनात मॉडेलचे नाव |

बहुतेक धड्यांसाठी एवढेच पुरेसे! नोटबुक्स तुमच्या `az login` सत्राद्वारे आपोआप प्रमाणीकरण करतील.

### चरण 5: Python अवलंबित्वे इंस्टॉल करा

```bash|powershell
pip install -r requirements.txt
```

आपण ही पूर्वी तयार केलेल्या virtual environment मध्ये चालविण्याचा सल्ला देतो.

## धडा 5 (Agentic RAG)साठी अतिरिक्त सेटअप

धडा 5 मध्ये **Azure AI Search** वापरल्या गेले आहे retrieval-augmented generation साठी. जर तो धडा चालवायचा असेल, तर हे व्हेरिएबल्स `.env` फाइलमध्ये जोडा:

| व्हेरिएबल | कुठे शोधायचे |
|----------|-----------------|
| `AZURE_SEARCH_SERVICE_ENDPOINT` | Azure पोर्टल → तुमचे **Azure AI Search** रिसोर्स → **Overview** → URL |
| `AZURE_SEARCH_API_KEY` | Azure पोर्टल → तुमचे **Azure AI Search** रिसोर्स → **Settings** → **Keys** → प्राथमिक अ‍ॅडमिन की |

## धडा 6 आणि धडा 8 (GitHub Models) साठी अतिरिक्त सेटअप

धडा 6 आणि 8 मधील काही नोटबुक्स **GitHub Models** वापरतात Azure AI Foundry ऐवजी. जर तो सॅम्पल्स चालवायचे असतील, तर हे व्हेरिएबल्स `.env` फाइल मध्ये जोडा:

| व्हेरिएबल | कुठे शोधायचे |
|----------|-----------------|
| `GITHUB_TOKEN` | GitHub → **Settings** → **Developer settings** → **Personal access tokens** |
| `GITHUB_ENDPOINT` | `https://models.inference.ai.azure.com` (मूळ किंमत) वापरा |
| `GITHUB_MODEL_ID` | वापरणारे मॉडेल नाव (उदा. `gpt-4o-mini`) |

## धडा 8 (Bing Grounding Workflow) साठी अतिरिक्त सेटअप

धडा 8 मधील conditional workflow नोटबुकमध्ये **Bing grounding** वापरले आहे Azure AI Foundry द्वारे. जर तो सॅम्पल चालवायचा असेल, तर `.env` फाइलमध्ये हा व्हेरिएबल जोडा:

| व्हेरिएबल | कुठे शोधायचे |
|----------|-----------------|
| `BING_CONNECTION_ID` | Azure AI Foundry पोर्टल → तुमचा प्रोजेक्ट → **Management** → **Connected resources** → तुमची Bing कनेक्शन → कनेक्शन ID कॉपी करा |

## समस्या निराकरण

### macOS वर SSL सर्टिफिकेट तपासणी त्रुटी

जर तुम्ही macOS वर असाल आणि खालीलप्रमाणे त्रुटी येत असेल:

```plaintext
ssl.SSLCertVerificationError: [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: self-signed certificate in certificate chain
```

हे Python च्या macOS आवृत्तीशी संबंधित एक ज्ञात समस्या आहे, जिथे सिस्टम SSL सर्टिफिकेट्स आपोआप विश्वासार्ह नाहीत. खालील उपाय क्रमाने वापरून पहा:

**पर्याय 1: Python चा Install Certificates स्क्रिप्ट चालवा (शिफारस केलेले)**

```bash
# 3.XX च्या जागी तुमची इंस्टॉल केलेली Python आवृत्ती ठेवा (उदा., 3.12 किंवा 3.13):
/Applications/Python\ 3.XX/Install\ Certificates.command
```

**पर्याय 2: नोटबुकमध्ये `connection_verify=False` वापरा (फक्त GitHub Models नोटबुक्ससाठी)**

धडा 6 नोटबुकमध्ये (`06-building-trustworthy-agents/code_samples/06-system-message-framework.ipynb`), एक टिप्पणीतून बाहेर काढलेले तोडगा आधीच आहे. क्लायंट तयार करताना `connection_verify=False` अनकॉमेंट करा:

```python
client = ChatCompletionsClient(
    endpoint=endpoint,
    credential=AzureKeyCredential(token),
    connection_verify=False,  # प्रमाणपत्र त्रुटी आढळल्यास SSL पडताळणी अक्षम करा
)
```

> **⚠️ सावधगिरी:** SSL तपासणी बंद केल्याने (`connection_verify=False`) सुरक्षा कमी होते कारण सर्टिफिकेट तपासणी टाळली जाते. फक्त विकास वातावरणात तात्पुरत्या उपाय म्हणून वापरा, उत्पादनात कधीही वापरू नका.

**पर्याय 3: `truststore` इंस्टॉल आणि वापरा**

```bash
pip install truststore
```

नंतर तुमच्या नोटबुक किंवा स्क्रिप्टच्या सुरुवातीला अर्थात नेटवर्क कॉल करण्यापूर्वी हे जोडा:

```python
import truststore
truststore.inject_into_ssl()
```

## कुठेतरी अडकले आहात?

जर तुम्हाला सेटअप चालवताना कोणतीही अडचण येत असेल, तर आमच्या <a href="https://discord.gg/kzRShWzttr" target="_blank">Azure AI Community Discord</a> मध्ये सामील व्हा किंवा <a href="https://github.com/microsoft/ai-agents-for-beginners/issues?WT.mc_id=academic-105485-koreyst" target="_blank">इश्यू तयार करा</a>.

## पुढचा धडा

आता तुम्ही या कोर्ससाठी कोड चालवायला तयार आहात. AI Agents च्या जगाबद्दल अधिक शिकण्यास आनंदी रहा!

[Introduction to AI Agents and Agent Use Cases](../01-intro-to-ai-agents/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**अस्वीकरण**:
हा दस्तऐवज एआय अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) चा वापर करून अनुवादित केला आहे. आम्ही अचूकतेसाठी प्रयत्न करत असलो तरी, कृपया लक्षात ठेवा की स्वयंचलित अनुवादांमध्ये त्रुटी किंवा चुकीची माहिती असू शकते. मूळ दस्तऐवज त्याच्या स्थानिक भाषेत अधिकृत स्रोत मानला जातो. महत्त्वाच्या माहिती साठी व्यावसायिक मानवी अनुवादाची शिफारस केली जाते. या अनुवादाचा वापर करून झालेल्या कोणत्याही गैरसमजुतींसाठी किंवा चुकांसाठी आम्ही जबाबदार नाही.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->