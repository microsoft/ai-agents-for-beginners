# कोर्स सेटअप

## परिचय

हा धडा या कोर्सच्या कोड नमुन्यांना कसे चालवायचे यावर प्रकाश टाकेल.

## इतर शिकणाऱ्यांशी जोडा आणि मदत मिळवा

आपला रेपो क्लोन करण्यापूर्वी, कोणतीही सेटअपशी संबंधित मदत, कोर्स संदर्भातील प्रश्न किंवा इतर शिकणाऱ्यांशी संपर्क साधण्यासाठी [AI Agents For Beginners Discord channel](https://aka.ms/ai-agents/discord) मध्ये सामील व्हा.

## या रेपोला क्लोन किंवा फोर्क करा

सुरु करण्यासाठी, कृपया GitHub Repository क्लोन किंवा फोर्क करा. यामुळे तुम्हाला कोर्स सामग्रीची तुमची स्वतःची आवृत्ती मिळेल ज्यामुळे तुम्ही कोड चालवू, तपासू आणि सुधारणा करू शकता!

हे करण्या साठी <a href="https://github.com/microsoft/ai-agents-for-beginners/fork" target="_blank">रेपो फोर्क करा</a> या लिंकवर क्लिक करा

आता तुमच्याकडे या कोर्सचा तुमचा स्वतःचा फोर्क केलेला आवृत्ती खालील लिंकवर असावा:

![Forked Repo](../../../translated_images/mr/forked-repo.33f27ca1901baa6a.webp)

### शॅलो क्लोन (वर्कशॉप / Codespaces साठी शिफारसीय)

  > पूर्ण रेपॉजिटरी पूर्ण इतिहास आणि सर्व फाइल्ससहित डाउनलोड केल्यावर मोठी (~3 GB) असू शकते. जर तुम्ही फक्त वर्कशॉपमध्ये सहभागी होत असाल किंवा केवळ काही धडा फोल्डर्स लागतील, तर शॅलो क्लोन (किंवा sparse clone) खूप कमी डाउनलोड करते.

#### क्विक शॅलो क्लोन—किमान इतिहास, सर्व फाइल्स

खालील कमांड्समधील `<your-username>` तुमच्या फोर्क URL ने (किंवा जर तुम्हाला प्राधान्य असेल तर अपस्ट्रीम URL ने) बदला.

फक्त नवीनतम कमिट इतिहास क्लोन करण्यासाठी (किंचित डाउनलोड):

```bash
git clone --depth 1 https://github.com/<your-username>/ai-agents-for-beginners.git
```

विशिष्ट शाखा क्लोन करण्यासाठी:

```bash
git clone --depth 1 --branch <branch-name> https://github.com/<your-username>/ai-agents-for-beginners.git
```

#### आंशिक (sparse) क्लोन – किमान blob + फक्त निवडलेल्या फोल्डर्स

हे आंशिक क्लोन आणि sparse-checkout वापरते (Git 2.25+ आवश्यक आणि आंशिक क्लोन समर्थन असणाऱ्या आधुनिक Git साठी शिफारसीय):

```bash
git clone --depth 1 --filter=blob:none --sparse https://github.com/<your-username>/ai-agents-for-beginners.git
```

रेपो फोल्डरमध्ये जा:

```bash
cd ai-agents-for-beginners
```

नंतर तुम्हाला हवे असलेले फोल्डर्स निर्दिष्ट करा (खालील उदाहरण दोन फोल्डर्स दाखवते):

```bash
git sparse-checkout set 00-course-setup 01-intro-to-ai-agents
```

क्लोन केल्यानंतर आणि फाइल्स तपासल्यानंतर, जर तुम्हाला केवळ फाइल्स लागतील आणि जागा मोकळी करायची असेल (कोणताही git इतिहास नको असेल), तर कृपया रेपो मेटाडेटा डिलीट करा (💀परत येऊ नये - तुम्हाला सर्व Git कार्यक्षमता गमवावी लागेल):

```bash
# झेडएसएच/बॅश
rm -rf .git
```

```powershell
# पॉवरशेल
Remove-Item -Recurse -Force .git
```

#### GitHub Codespaces वापरुन (स्थानिक मोठ्या डाउनलोड टाळण्यासाठी शिफारसीय)

- या रेपो साठी [GitHub UI](https://github.com/codespaces) द्वारे नवीन Codespace तयार करा.  

- नव्या बनलेल्या Codespace च्या टर्मिनलमध्ये, शॅलो/स्पार्स क्लोन कमांड्सपैकी एक चालवा ज्यामुळे केवळ हवे असलेले धडा फोल्डर्स Codespace कार्यक्षेत्रात येतील.
- ऐच्छिक: Codespaces मध्ये क्लोन केल्यावर, अतिरिक्त जागा मोकळी करण्यासाठी .git काढा (वरील काढण्याच्या कमांड्स पहा).
- लक्षात ठेवा: तुम्हाला जर पुढील क्लोन न करता थेट Codespaces मध्ये रेपो उघडायचा असेल, तर Codespaces devcontainer पर्यावरण तयार करेल आणि कदाचित तुमच्या गरजेपेक्षा अधिक पर्याय पुरवू शकते.

#### टिपा

- तुमचा बदल करण्यासाठी/कमिट करण्यासाठी क्लोन URL नेहमीच तुमच्या फोर्कने बदला.
- नंतर अधिक इतिहास किंवा फाइल्स लागत असल्यास, तुम्ही त्यांना fetch करू शकता किंवा sparse-checkout मध्ये अतिरिक्त फोल्डर्स समाविष्ट करू शकता.

## कोड चालविणे

हा कोर्स AI एजंट्स बनविण्याचा हॅण्ड्स-ऑन अनुभव मिळवण्यासाठी Jupyter नोटबुक्सची मालिका ऑफर करतो.

कोड नमुने **Microsoft Agent Framework (MAF)** वापरतात आणि `FoundryChatClient` जो **Microsoft Foundry Agent Service V2** (Responses API) शी **Microsoft Foundry** मधून जोडतो.

सर्व Python नोटबुक्स `*-python-agent-framework.ipynb` नावाने लेबेल केलेले आहेत.

## आवश्यकता

- Python 3.12+
  - **टीप**: जर तुमच्याकडे Python3.12 इंस्टॉल नसेल, तर ते नक्की इंस्टॉल करा. नंतर requirements.txt फाइलमधील योग्य आवृत्त्या इंस्टॉल करण्यासाठी python3.12 वापरून तुमचे venv तयार करा.
  
    >उदाहरण

    Python venv निर्देशिका तयार करा:

    ```bash
    python -m venv venv
    ```

    मग पुढील साठी venv environment सक्रिय करा:

    ```bash
    # झश/बॅश
    source venv/bin/activate
    ```
  
    ```dos
    # Command Prompt for Windows
    venv\Scripts\activate
    ```

- .NET 10+: .NET वापरून नमुना कोडसाठी, [.NET 10 SDK](https://dotnet.microsoft.com/download/dotnet/10.0) किंवा नंतरची आवृत्ती इंस्टॉल करा. नंतर, तुमच्या इंस्टॉल केलेल्या .NET SDK चा अवलंब तपासा:

    ```bash
    dotnet --list-sdks
    ```

- **Azure CLI** — प्रमाणीकरणासाठी आवश्यक. [aka.ms/installazurecli](https://aka.ms/installazurecli) कडून इंस्टॉल करा.
- **Azure Subscription** — Microsoft Foundry आणि Microsoft Foundry Agent Service साठी प्रवेश.
- **Microsoft Foundry Project** — एखादा प्रोजेक्ट ज्यात तैनात मॉडेल आहे (उदा., `gpt-5-mini`). खाली [Step 1](#पाऊल-1-microsoft-foundry-प्रोजेक्ट-तयार-करा) पहा.

आम्ही या रिपॉझिटरीच्या मूळामध्ये `requirements.txt` फाइल दिली आहे ज्यामध्ये कोड नमुने चालवण्यासाठी लागणारे सर्व Python पॅकेज आहेत.

तुम्ही ती रिपॉझिटरीच्या मूळ निर्देशिकेत तुमच्या टर्मिनलमध्ये खालील कमांड चालवून इन्स्टॉल करू शकता:

```bash
pip install -r requirements.txt
```

कोणतीही संघर्ष आणि समस्या टाळण्यासाठी Python व्हर्चुअल एन्व्हायर्नमेंट तयार करण्याची आम्ही शिफारस करतो.

## VSCode Setup

VSCode मध्ये तुम्ही योग्य Python आवृत्ती वापरत असल्याची खात्री करा.

![image](https://github.com/user-attachments/assets/a85e776c-2edb-4331-ae5b-6bfdfb98ee0e)

## Microsoft Foundry आणि Microsoft Foundry Agent Service सेटअप करा

### पाऊल 1: Microsoft Foundry प्रोजेक्ट तयार करा

तुम्हाला Microsoft Foundry **हब** आणि **प्रोजेक्ट** आवश्यक आहे ज्यात तैनात मॉडेल असेल जेणेकरून नोटबुक्स चालवता येतील.

1. [ai.azure.com](https://ai.azure.com) ला जा आणि तुमच्या Azure खात्याने लॉगिन करा.
2. **हब** तयार करा (किंवा आधीचा वापरा). पहा: [Hub resources overview](https://learn.microsoft.com/azure/ai-foundry/concepts/ai-resources).
3. हब मध्ये **प्रोजेक्ट** तयार करा.
4. **Models + Endpoints** → **Deploy model** मध्ये जाऊन मॉडेल (उदा., `gpt-5-mini`) तैनात करा.

### पाऊल 2: तुमचा प्रोजेक्ट एंडपॉइंट आणि मॉडेल तैनाती नाव मिळवा

Microsoft Foundry पोर्टलमधील तुमच्या प्रोजेक्टमधून:

- **Project Endpoint** — **Overview** पृष्ठावर जा आणि एंडपॉइंट URL कॉपी करा.

![Project Connection String](../../../translated_images/mr/project-endpoint.8cf04c9975bbfbf1.webp)

- **Model Deployment Name** — **Models + Endpoints** वर जा, तुमचा तैनात केलेला मॉडेल निवडा आणि **Deployment name** (उदा., `gpt-5-mini`) नोंद करा.

### पाऊल 3: `az login` ने Azure मध्ये साइन इन करा

बर्‍याच नोटबुक्स तुमच्या **Azure CLI साइन-इन** द्वारा प्रमाणीकरण करतात — `azure-identity` पॅकेजमधील `AzureCliCredential` किंवा `DefaultAzureCredential` वापरून (जे तुमचा `az login` सत्र घेते) — त्यामुळे API कीसाठी गरज नाही. काही धडे आणि ऐच्छिक इंटिग्रेशन्स API की वापरतात; प्रत्येक धड्याच्या पूर्ववत अटी तपासा. यासाठी तुम्हाला Azure CLI द्वारे साइन इन केलेले असणे आवश्यक आहे.

1. **Azure CLI स्थापित करा** जर आधीपासून नसेल: [aka.ms/installazurecli](https://aka.ms/installazurecli)

2. **साइन इन** करा:

    ```bash
    az login
    ```

    किंवा जर तुम्ही रिमोट/कोडस्पेस वातावरणामध्ये आहात आणि ब्राउझर नाही:

    ```bash
    az login --use-device-code
    ```

3. **तुमची सबस्क्रिप्शन निवडा** जर ते विचारले तर — ज्यामध्ये तुमचा Foundry प्रोजेक्ट आहे तो निवडा.

4. **तुम्ही साइन इन केलेले आहात का ते तपासा**:

    ```bash
    az account show
    ```

> **`az login` का?** नोटबुक्स `azure-identity` पॅकेजमधील `AzureCliCredential` (किंवा `DefaultAzureCredential`, जे तुमचा Azure CLI साइन-इन देखील घेतो) वापरून प्रमाणीकरण करतात. म्हणजे तुमचा Azure CLI सत्र क्रेडेन्शियल पुरवतो — API कीस किंवा गुपिते `.env` फाइलमध्ये नाहीत. हा एक [सुरक्षा चांगला सराव](https://learn.microsoft.com/azure/developer/ai/keyless-connections) आहे.

### पाऊल 4: तुमची `.env` फाइल तयार करा

उदाहरण फाइल कॉपी करा:

```bash
# zsh/bash
cp .env.example .env
```

```powershell
# पॉवरशेल
Copy-Item .env.example .env
```

`.env` उघडा आणि हे दोन मूल्ये भरा:

```env
AZURE_AI_PROJECT_ENDPOINT=https://<your-project>.services.ai.azure.com/api/projects/<your-project-id>
AZURE_AI_MODEL_DEPLOYMENT_NAME=gpt-5-mini
```

| चल (Variable) | कुठे शोधायचे |
|----------|-----------------|
| `AZURE_AI_PROJECT_ENDPOINT` | Foundry पोर्टल → तुमचा प्रोजेक्ट → **Overview** पृष्ठ |
| `AZURE_AI_MODEL_DEPLOYMENT_NAME` | Foundry पोर्टल → **Models + Endpoints** → तुमचा तैनात केलेला मॉडेल नाव |

बर्‍याच धड्यांसाठी इतक्यातच काम झाले! नोटबुक्स तुमच्या `az login` सत्राद्वारे स्वयंचलितपणे प्रमाणीकरण करतात.

### पाऊल 5: Python Dependencies इंस्टॉल करा

```bash
pip install -r requirements.txt
```

आम्ही शिफारस करतो की हा कमांड तुम्ही आधी तयार केलेल्या वर्च्युअल एन्व्हायर्नमेंटमध्ये चालवा.

## ऐच्छिक सेटअप: Azure AI Search (धडे 5 आणि 16)

धडा 5 (Agentic RAG) आणि धडा 16 नोटबुक्स बिनधास्त **in-memory knowledge base** वापरतात — कोणत्याही अतिरिक्त Azure साधनांची गरज नाही. जर तुम्हाला त्यांना खऱ्या **Azure AI Search** निर्देशांकासह वापरायचे असेल तर लक्षात ठेवा की धडा 16 नोटबुक सध्या **की-आधारित प्रमाणीकरण वापरतो**: तो in-memory शोधापासून Azure AI Search वर स्विच करतो जेव्हा **दोन्ही** `AZURE_SEARCH_SERVICE_ENDPOINT` **आणि** `AZURE_SEARCH_API_KEY` सेट केलेले असतात, अन्यथा in-memory शोधावरच राहतो — त्यामुळे खऱ्या निर्देशांकासोबत चालवण्यासाठी तुम्हाला प्रशासन की देखील सेट करावी लागते. Microsoft Entra ID (RBAC) सह कीलेस प्रमाणीकरण हे तुमच्या स्वतःच्या उत्पादन कोडसाठी शिफारसीय पद्धत आहे, जी या कोर्समधील `az login` प्रवाहाशी सुसंगत आहे.

खालील RBAC पावल्‍या सेटअप-गाइड नमुन्‍यांवर आणि तुमच्या स्वतःच्या कोडवर लागू होतात. त्या धडा 16 नोटबुकमध्ये कीलेस प्रमाणीकरण सक्षम करत नाहीत; धडा 16 मध्ये अजूनही दोन्ही एंडपॉइंट आणि प्रशासकीय की वापरली जाते Azure AI Search साठी.

1. **तुमच्या शोध सेवेमध्ये रोल-आधारित प्रवेश सक्षम करा**:

    ```bash
    az search service update --name <service-name> --resource-group <resource-group> --auth-options aadOrApiKey
    ```

2. **आवश्यक भूमिका स्वतःस सौंपा** (निर्देशांक तयार/लोड आणि चौकशी करण्यासाठी):

    ```bash
    az role assignment create --assignee <your-user-or-principal-id> --role "Search Service Contributor" --scope $(az search service show -g <resource-group> -n <service-name> --query id -o tsv)
    az role assignment create --assignee <your-user-or-principal-id> --role "Search Index Data Contributor" --scope $(az search service show -g <resource-group> -n <service-name> --query id -o tsv)
    ```

3. तुमच्या `.env` फाइलमध्ये एंडपॉइंट जोडा:

| चल (Variable) | कुठे शोधायचे |
|----------|-----------------|
| `AZURE_SEARCH_SERVICE_ENDPOINT` | Azure पोर्टल → तुमच्या **Azure AI Search** स्रोत → **Overview** → URL |
| `AZURE_SEARCH_API_KEY` | आवश्यक (एंडपॉइंटसह) धडा 16 नोटबुकमध्ये Azure AI Search सक्षम करण्यासाठी, जो की-आधारित प्रमाणीकरण वापरतो. Azure पोर्टल → **Settings** → **Keys** → प्राथमिक प्रशासकीय की |

> **कीलेस का?** प्रशासकीय की तुमच्या शोध सेवेवर पूर्ण लेखन प्रवेश देते आणि `.env` फाइल्समधून बाहेर पडू शकते. RBAC वापरून तुमचा `az login` ओळख वापरला जातो — तोच कीलेस Entra ID नमुना जो कोर्स नोटबुक्स वापरतात (मार्फत `AzureCliCredential` / `DefaultAzureCredential`). पाहा [Connect to Azure AI Search using roles](https://learn.microsoft.com/azure/search/search-security-rbac).

विस्ताराने निर्देशांक-निर्मिती नमुन्यांसाठी [Azure AI Search setup guide](./AzureSearch.md) पहा Python व .NET मध्ये.

## अतिरिक्त सेटअप धडे ज्यात Azure OpenAI थेट कॉल करतात (धडे 6 आणि 8)

काही नोटबुक्स धडे 6 आणि 8 मध्ये थेट **Azure OpenAI** कॉल करतात (**Responses API** वापरून) Microsoft Foundry प्रोजेक्टशिवाय. हे नमुने पूर्वी GitHub Models वापरत होते, जे बंद झाले आहे आणि Responses API ला समर्थन देत नाही. तुमच्या `.env` फाइलमध्ये हे चल जोडा:

| चल (Variable) | कुठे शोधायचे |
|----------|-----------------|
| `AZURE_OPENAI_ENDPOINT` | Azure पोर्टल → तुमचा **Azure OpenAI** स्रोत → **Keys and Endpoint** → EndPoint (उदा. `https://<your-resource>.openai.azure.com`) |
| `AZURE_OPENAI_DEPLOYMENT` | तुमच्या तैनात केलेल्या मॉडेलचे नाव (उदा., `gpt-5-mini`) जे Responses API ला समर्थन देते |
| `AZURE_OPENAI_API_KEY` | ऐच्छिक — केवळ की-आधारित प्रमाणीकरण वापरत असल्यास `az login` / Entra ID ऐवजी |

> Responses API स्थिर `/openai/v1/` एंडपॉइंट वापरतो, त्यामुळे `api-version` आवश्यक नाही. कीलेस Entra ID प्रमाणीकरणासाठी `az login` वापरा.

## पर्यायी प्रदाता: MiniMax (OpenAI-सुसंगत)

[MiniMax](https://platform.minimaxi.com/) मोठ्या संदर्भाच्या मॉडेल्स (जास्तीत जास्त 204K टोकन्स) OpenAI-सुसंगत API द्वारे उपलब्ध करतो. Microsoft Agent Framework चा `OpenAIChatClient` कोणत्याही OpenAI-सुसंगत एंडपॉइंटसह कार्य करतो, त्यामुळे तुम्ही MiniMax ला `OpenAIChatClient` वापरल्या जाणाऱ्या धड्यांसाठी थेट पर्यायी म्हणून वापरू शकता.

हे चल तुमच्या `.env` फाइलमध्ये जोडा:

| चल (Variable) | कुठे शोधायचे |
|----------|-----------------|
| `MINIMAX_API_KEY` | [MiniMax Platform](https://platform.minimaxi.com/) → API Keys |
| `MINIMAX_BASE_URL` | `https://api.minimax.io/v1` वापरा (डिफॉल्ट मूल्य) |
| `MINIMAX_MODEL_ID` | वापरण्याचे मॉडेल नाव (उदा., `MiniMax-M3`) |

**उदाहरण मॉडेल्स**: `MiniMax-M3` (शिफारसीय), `MiniMax-M2.7`, `MiniMax-M2.7-highspeed` (वेगवान प्रतिसाद). मॉडेल नावे आणि उपलब्धता वेळोवेळी बदलू शकते, आणि एका विशिष्ट मॉडेलसाठी प्रवेश तुमच्या खात्यावर अवलंबून असू शकतो.

`OpenAIChatClient` वापरणारे कोड नमुने (उदा., धडा 14 हॉटेल बुकिंग वर्कफ्लो) स्वयंचलितपणे तुमचा MiniMax कॉन्फिगरेशन वापरतील जेव्हा `MINIMAX_API_KEY` सेट केलेले असेल.


## पर्यायी प्रदाता: Novita AI (OpenAI-संगत)

[Novita AI](https://novita.ai/llm-api) मुक्त स्रोत आणि सीमारेषा LLMs (DeepSeek, Llama, Qwen, इत्यादी) साठी OpenAI-संगत API प्रदान करतो. Microsoft Agent Framework चा `OpenAIChatClient` कोणत्याही OpenAI-संगत एन्डपॉइंटसह कार्य करतो, त्यामुळे आपण Novita AI ला Azure OpenAI किंवा OpenAI चा पर्यायी ड्रोप-इन म्हणून वापरू शकता.

आपल्या `.env` फाइलमध्ये हे व्हेरिएबल्स जोडा:

| व्हेरिएबल | कुठे शोधायचे |
|----------|---------------|
| `NOVITA_API_KEY` | [Novita AI Dashboard](https://novita.ai/settings/key-management) → API Keys |
| `NOVITA_BASE_URL` | वापरा `https://api.novita.ai/openai/v1` (पूर्वनिर्धारित मूल्य) |
| `NOVITA_MODEL_ID` | वापरण्याचा मॉडेल नाव (उदा., `moonshotai/kimi-k3`) |

**उदाहरण मॉडेल्स**: `moonshotai/kimi-k3`, `zai-org/glm-5.2`, `deepseek/deepseek-v4-flash-0731`. Novita AI अजून बरेच मुक्त स्रोत मॉडेल कुटुंबे (Llama, Qwen, GLM, इत्यादी) होस्ट करते — उपलब्ध मॉडेल्स आणि त्यांच्या मॉडेल IDs साठी [Novita AI मॉडेल लायब्ररी](https://novita.ai/llm-api) तपासा.

सध्याच्या सॅंपल मध्ये `NOVITA_*` व्हेरिएबल्स आपोआप वापरले जात नाहीत. Novita AI वापरण्यासाठी, आपण चालवत असलेल्या सॅंपलमध्ये `OpenAIChatClient` तयार करताना हे मूल्ये स्पष्टपणे द्या.

## पर्यायी प्रदाता: Foundry Local (मॉडेल्स आपल्या डिव्हाइसवर चालवा)

[Foundry Local](https://foundrylocal.ai) हा एक हलका रनटाइम आहे जो भाषा मॉडेल्स **पूर्णपणे आपल्या मशीनवर** डाउनलोड, व्यवस्थापित आणि सेवा पुरवतो OpenAI-संगत API द्वारे — कोणतेही क्लाउड आवश्यक नाही.

कारण Microsoft Agent Framework चा `OpenAIChatClient` कोणत्याही OpenAI-संगत एन्डपॉइंटसह कार्य करतो, Foundry Local हा Azure OpenAI चा स्थानिक पर्यायी म्हणून वापरू शकतो.

**1. Foundry Local स्थापित करा**

```bash
# विंडोज
winget install Microsoft.FoundryLocal

# मॅकओएस
brew install foundrylocal
```

**2. एक मॉडेल डाउनलोड करा आणि चालवा** (हे स्थानिक सेवा देखील सुरू करते):

```bash
foundry model list          # उपलब्ध मॉडेल पहा
foundry model run phi-4-mini
```

**3. Python SDK स्थापित करा** ज्याचा वापर स्थानिक एन्डपॉइंट शोधण्यासाठी होतो:

```bash
pip install foundry-local-sdk
```

**4. Microsoft Agent Framework ला तुमच्या स्थानिक मॉडेलशी जोडा:**

```python
from foundry_local import FoundryLocalManager
from agent_framework.openai import OpenAIChatClient

# मॉडेल डाउनलोड करतो (जर आवश्यक असेल तर) आणि स्थानिकरीतीने सेवा पुरवतो, नंतर एंडपॉइंट/पोर्ट शोधतो.
manager = FoundryLocalManager("phi-4-mini")

chat_client = OpenAIChatClient(
    base_url=manager.endpoint,      # उदा. http://localhost:<port>/v1
    api_key=manager.api_key,        # नेहमीच "not-required" फाऊंड्री लोकलसाठी
    model_id=manager.get_model_info("phi-4-mini").id,
)

agent = chat_client.as_agent(
    name="LocalAgent",
    instructions="You are a helpful assistant running fully on-device.",
)
```

> **टीप:** Foundry Local एक OpenAI-संगत **चॅट पूर्णता** एन्डपॉइंट उघडतो. स्थानिक विकास आणि ऑफलाइन परिस्थितीसाठी वापरा. पूर्ण **Responses API** वैशिष्ट्यांसाठी (स्थितिजन्य संवाद इत्यादी), Azure OpenAI किंवा Microsoft Foundry प्रोजेक्ट वापरा.

## आठवडा 8 साठी अतिरिक्त सेटअप (Bing ग्राउंडिंग वर्कफ्लो)

आठवडा 8 मधील सशर्त वर्कफ्लो नोटबुक Microsoft Foundry द्वारे **Bing ग्राउंडिंग** वापरतो. आपण तो सॅंपल चालवणार असल्यास, आपल्या `.env` फाइलमध्ये हा व्हेरिएबल जोडा:

| व्हेरिएबल | कुठून शोधायचे |
|----------|---------------|
| `BING_CONNECTION_ID` | Microsoft Foundry पोर्टल → आपला प्रोजेक्ट → **Management** → **Connected resources** → आपला Bing कनेक्शन → कनेक्शन ID कॉपी करा |

## समस्या निवारण

### macOS वर SSL प्रमाणपत्र पडताळणी त्रुटी

आपण macOS वापरत असल्यास आणि खालीलप्रमाणे त्रुटी येत असेल:

```plaintext
ssl.SSLCertVerificationError: [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: self-signed certificate in certificate chain
```

Python चे macOS वर हे एक ज्ञात प्रश्न आहे जेथे प्रणाली SSL प्रमाणपत्रे आपोआप विश्वासार्ह ठरवली जात नाहीत. खालील सोल्यूशन्स क्रमाने वापरून पहा:

**पर्याय 1: Python चे Install Certificates स्क्रिप्ट चालवा (शिफारस केलेले)**

```bash
# आपला स्थापित केलेला Python आवृत्ती (उदा. 3.12 किंवा 3.13) वापरून 3.XX बदला:
/Applications/Python\ 3.XX/Install\ Certificates.command
```

**पर्याय 2: आपल्या नोटबुकमध्ये `connection_verify=False` वापरा (GitHub Models नोटबुकसाठीच)**

आठवडा 6 नोटबुकमध्ये (`06-building-trustworthy-agents/code_samples/06-system-message-framework.ipynb`), एक कमेंट केलेले उपाय आधीच समाविष्ट आहे. प्रमाणपत्र त्रुटी आल्यावर `connection_verify=False` अनकमेंट करा:

```python
client = ChatCompletionsClient(
    endpoint=endpoint,
    credential=AzureKeyCredential(token),
    connection_verify=False,  # जर तुम्हाला प्रमाणपत्र त्रुटी आढळल्यास SSL पडताळणी अक्षम करा
)
```

> **⚠️ इशारा:** SSL पडताळणी बंद करणे (`connection_verify=False`) सुरक्षा कमी करते कारण प्रमाणपत्र तपासणी टाळते. हे फक्त विकास वातावरणासाठी तात्पुरते उपाय म्हणून वापरा. उत्पादनात कधीही वापरू नका.

**पर्याय 3: `truststore` स्थापित करा आणि वापरा**

```bash
pip install truststore
```

मग आपल्या नोटबुक किंवा स्क्रिप्टच्या वर नेटवर्क कॉल करण्यापूर्वी खालील जोडाः

```python
import truststore
truststore.inject_into_ssl()
```

## कुठेतरी अडकलात का?

या सेटअपसह काही समस्या असल्यास, आमच्या <a href="https://discord.gg/kzRShWzttr" target="_blank">Azure AI Community Discord</a> मध्ये सामील व्हा किंवा <a href="https://github.com/microsoft/ai-agents-for-beginners/issues?WT.mc_id=academic-105485-koreyst" target="_blank">एक इश्यू तयार करा</a>.

## पुढील धडा

आपण आता या अभ्यासक्रमाचा कोड चालवायला तयार आहात. AI एजंट्सच्या जगाबद्दल अधिक शिकताना आनंद घ्या! 

[AI एजंट्स आणि एजंट वापर प्रकरणांची ओळख](../01-intro-to-ai-agents/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**अस्वीकरण**:
हा दस्तऐवज AI भाषांतर सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) चा वापर करून अनुवादित केला आहे. जरी आम्ही अचूकतेसाठी प्रयत्न करतो, तरी कृपया लक्षात घ्या की स्वयंचलित भाषांतरांमध्ये त्रुटी किंवा अचूकतेची कमतरता असू शकते. मूळ दस्तऐवज त्याच्या मूळ भाषेत अधिकृत स्रोत मानला पाहिजे. महत्त्वाची माहिती असल्यास, व्यावसायिक मानवी भाषांतराची शिफारस केली जाते. या भाषांतराच्या वापरामुळे उद्भवणाऱ्या कोणत्याही गैरसमज किंवा चुकीच्या अर्थलावणीसाठी आम्ही जबाबदार नाही.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->