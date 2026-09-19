# कोर्स सेटअप

## परिचय

इस पाठ में इस कोर्स के कोड नमूनों को चलाने के बारे में बताया जाएगा।

## अन्य शिक्षार्थियों से जुड़ें और सहायता प्राप्त करें

अपनी रिपॉज़िटरी क्लोन करने से पहले, सेटअप में किसी भी सहायता के लिए, कोर्स से संबंधित किसी भी प्रश्न के लिए, या अन्य शिक्षार्थियों से जुड़ने के लिए [AI Agents For Beginners Discord चैनल](https://aka.ms/ai-agents/discord) से जुड़ें।

## इस रिपॉजिटरी को क्लोन या फोर्क करें

शुरू करने के लिए, कृपया GitHub रिपॉजिटरी को क्लोन या फोर्क करें। यह आपको कोर्स सामग्री का अपना स्वयं का संस्करण बनाने देगा ताकि आप कोड चला, परीक्षण और संशोधित कर सकें!

इसे <a href="https://github.com/microsoft/ai-agents-for-beginners/fork" target="_blank">रिपॉजिटरी फोर्क करने</a> के लिंक पर क्लिक करके किया जा सकता है

अब आपके पास इस कोर्स का अपना फोर्क किया हुआ संस्करण निम्न लिंक में होना चाहिए:

![Forked Repo](../../../translated_images/hi/forked-repo.33f27ca1901baa6a.webp)

### शैलो क्लोन (कार्यशाला / Codespaces के लिए अनुशंसित)

  >पूर्ण रिपॉजिटरी का आकार बड़ा हो सकता है (~3 GB) जब आप पूरी इतिहास और सभी फाइलें डाउनलोड करते हैं। यदि आप केवल कार्यशाला में भाग ले रहे हैं या केवल कुछ पाठ फ़ोल्डर चाहिए, तो शैलो क्लोन (या sparse क्लोन) बहुत कम डाउनलोड करता है।

#### त्वरित शैलो क्लोन — न्यूनतम इतिहास, सभी फाइलें

नीचे दिए गए कमांड में `<your-username>` को अपने फोर्क URL (या यदि आप चाहें तो अपस्ट्रीम URL) से बदलें।

केवल नवीनतम कमिट इतिहास क्लोन करने के लिए (छोटा डाउनलोड):

```bash
git clone --depth 1 https://github.com/<your-username>/ai-agents-for-beginners.git
```

किसी विशिष्ट ब्रांच को क्लोन करने के लिए:

```bash
git clone --depth 1 --branch <branch-name> https://github.com/<your-username>/ai-agents-for-beginners.git
```

#### आंशिक (स्पार्स) क्लोन — न्यूनतम ब्लॉब + केवल चयनित फ़ोल्डर

यह आंशिक क्लोन और sparse-checkout का उपयोग करता है (Git 2.25+ और partial clone सपोर्ट के साथ आधुनिक Git की आवश्यकता है):

```bash
git clone --depth 1 --filter=blob:none --sparse https://github.com/<your-username>/ai-agents-for-beginners.git
```

रिपॉजिटरी फ़ोल्डर में जाएं:

```bash
cd ai-agents-for-beginners
```

फिर निर्धारित करें कि आप कौन से फ़ोल्डर चाहते हैं (नीचे उदाहरण में दो फ़ोल्डर दिखाए गए हैं):

```bash
git sparse-checkout set 00-course-setup 01-intro-to-ai-agents
```

क्लोन करने और फाइलें सत्यापित करने के बाद, यदि आप केवल फाइलें चाहते हैं और स्थान खाली करना चाहते हैं (कोई git इतिहास नहीं), तो कृपया रिपॉजिटरी मेटाडेटा हटा दें (💀अपरिवर्तनीय — आप सभी Git कार्यक्षमता खो देंगे):

```bash
# zsh/bash
rm -rf .git
```

```powershell
# पावरशेल
Remove-Item -Recurse -Force .git
```

#### GitHub Codespaces का उपयोग करना (स्थानीय बड़े डाउनलोड से बचने के लिए अनुशंसित)

- इस रिपॉजिटरी के लिए [GitHub UI](https://github.com/codespaces) के माध्यम से एक नया Codespace बनाएं।  

- नए बनाए गए Codespace की टर्मिनल में ऊपर दिए गए शैलो/स्पार्स क्लोन कमांड्स में से किसी एक को चलाएं ताकि केवल आपको आवश्यक पाठ फ़ोल्डर ही Codespace कार्यक्षेत्र में आएं।
- वैकल्पिक: Codespaces के अंदर क्लोन करने के बाद, अतिरिक्त स्थान रिक्लेम करने के लिए .git हटाएं (ऊपर हटाने के कमांड देखें)।
- ध्यान दें: यदि आप रिपॉजिटरी को सीधे Codespaces में खोलना पसंद करते हैं (अतिरिक्त क्लोन के बिना), तो ध्यान दें Codespaces devcontainer वातावरण बनाएगा और हो सकता है कि यह आप जितनी जरूरत है उससे अधिक संसाधन प्रदान करे।

#### सुझाव

- यदि आप संपादित/कमिट करना चाहते हैं तो हमेशा क्लोन URL को अपने फोर्क से बदलें।
- यदि बाद में आपको अधिक इतिहास या फाइलें चाहिए, तो आप उन्हें प्राप्त कर सकते हैं या sparse-checkout को अतिरिक्त फ़ोल्डरों को शामिल करने के लिए समायोजित कर सकते हैं।

## कोड चलाना

यह कोर्स Jupyter Notebooks की एक श्रृंखला प्रदान करता है जिन्हें आप AI Agents बनाने का व्यावहारिक अनुभव प्राप्त करने के लिए चला सकते हैं।

कोड नमूने **Microsoft Agent Framework (MAF)** का उपयोग करते हैं जिसमें `FoundryChatClient` है, जो **Microsoft Foundry Agent Service V2** (Responses API) से **Microsoft Foundry** के माध्यम से जुड़ता है।

सभी Python नोटबुक्स `*-python-agent-framework.ipynb` के रूप में लेबल किए गए हैं।

## आवश्यकताएं

- Python 3.12+
  - **नोट**: यदि आपके पास Python3.12 इंस्टॉल नहीं है, तो कृपया इसे इंस्टॉल करें। फिर अपनी venv बनाएँ python3.12 का उपयोग करके ताकि requirements.txt फ़ाइल से सही संस्करण इंस्टॉल हो।
  
    >उदाहरण

    Python venv डायरेक्टरी बनाएँ:

    ```bash
    python -m venv venv
    ```

    फिर इसके लिए venv पर्यावरण सक्रिय करें:

    ```bash
    # zsh/bash
    source venv/bin/activate
    ```
  
    ```dos
    # Command Prompt for Windows
    venv\Scripts\activate
    ```

- .NET 10+: .NET का उपयोग करने वाले नमूना कोड के लिए, सुनिश्चित करें कि आपने [.NET 10 SDK](https://dotnet.microsoft.com/download/dotnet/10.0) या उच्चतर संस्करण इंस्टॉल किया है। फिर, अपनी .NET SDK संस्करण जांचें:

    ```bash
    dotnet --list-sdks
    ```

- **Azure CLI** — प्रमाणिकरण के लिए आवश्यक। [aka.ms/installazurecli](https://aka.ms/installazurecli) से इंस्टॉल करें।
- **Azure Subscription** — Microsoft Foundry और Microsoft Foundry Agent Service तक पहुंच के लिए।
- **Microsoft Foundry Project** — एक ऐसा प्रोजेक्ट जिसमें मॉडल तैनात हो (जैसे, `gpt-5-mini`)। देखें [Step 1](#चरण-1-microsoft-foundry-प्रोजेक्ट-बनाएं) नीचे।

हमने इस रिपॉजिटरी की रूट में `requirements.txt` फ़ाइल शामिल की है जिसमें कोड नमूनों को चलाने के लिए आवश्यक सभी Python पैकेज हैं।

आप इन्हें रिपॉजिटरी की रूट में टर्मिनल में निम्न कमांड चलाकर इंस्टॉल कर सकते हैं:

```bash
pip install -r requirements.txt
```

हम अनुशंसा करते हैं कि किसी भी संघर्ष और मुद्दों से बचने के लिए Python वर्चुअल एनवायरनमेंट बनाएं।

## VSCode सेटअप करें

सुनिश्चित करें कि आप VSCode में सही संस्करण के Python का उपयोग कर रहे हैं।

![image](https://github.com/user-attachments/assets/a85e776c-2edb-4331-ae5b-6bfdfb98ee0e)

## Microsoft Foundry और Microsoft Foundry Agent Service सेटअप करें

### चरण 1: Microsoft Foundry प्रोजेक्ट बनाएं

आपको नोटबुक्स चलाने के लिए एक Microsoft Foundry **hub** और **project** चाहिए जिसमें डिप्लॉय किया गया मॉडल हो।

1. [ai.azure.com](https://ai.azure.com) पर जाएं और अपने Azure खाते से साइन इन करें।
2. एक **hub** बनाएं (या मौजूदा का उपयोग करें)। देखें: [Hub resources overview](https://learn.microsoft.com/azure/ai-foundry/concepts/ai-resources)।
3. हब के अंदर एक **प्रोजेक्ट** बनाएं।
4. **Models + Endpoints** → **Deploy model** से एक मॉडल (जैसे, `gpt-5-mini`) तैनात करें।

### चरण 2: अपना प्रोजेक्ट Endpoint और Model Deployment नाम प्राप्त करें

Microsoft Foundry पोर्टल में अपने प्रोजेक्ट से:

- **प्रोजेक्ट Endpoint** — **Overview** पेज पर जाएं और endpoint URL कॉपी करें।

![Project Connection String](../../../translated_images/hi/project-endpoint.8cf04c9975bbfbf1.webp)

- **Model Deployment नाम** — **Models + Endpoints** पर जाएं, अपने डिप्लॉय किए हुए मॉडल को चुनें, और **Deployment name** नोट करें (जैसे, `gpt-5-mini`)।

### चरण 3: Azure में `az login` के साथ साइन इन करें

अधिकांश नोटबुक्स आपके **Azure CLI साइन-इन** के माध्यम से प्रमाणीकृत होती हैं — `AzureCliCredential` या `DefaultAzureCredential` का उपयोग करते हुए (दोनों आपके `az login` सेशन को पकड़ते हैं) जो `azure-identity` पैकेज से है — इसलिए इन्हें API कुंजी की आवश्यकता नहीं होती। कुछ पाठ और वैकल्पिक इंटीग्रेशन API कुंजी का उपयोग करते हैं; प्रत्येक पाठ की आवश्यकताओं में किसी भी अतिरिक्त पर्यावरण चर की जांच करें। यह आवश्यक है कि आप Azure CLI के माध्यम से साइन इन हों।

1. यदि आपने Azure CLI इंस्टॉल नहीं किया है तो इसे इंस्टॉल करें: [aka.ms/installazurecli](https://aka.ms/installazurecli)

2. इसके बाद साइन इन करें:

    ```bash
    az login
    ```

    यदि आप किसी रिमोट/Codespace वातावरण में हैं जहाँ ब्राउज़र उपलब्ध नहीं है:

    ```bash
    az login --use-device-code
    ```

3. यदि पूछा जाए तो अपनी सब्सक्रिप्शन चुनें — वह जो आपके Foundry प्रोजेक्ट को शामिल करता है।

4. सुनिश्चित करें कि आप साइन इन हैं:

    ```bash
    az account show
    ```

> **क्यों `az login`?** नोटबुक्स `AzureCliCredential` (या `DefaultAzureCredential`, जो आपके Azure CLI लॉगिन को भी पकड़ता है) का उपयोग करके प्रमाणीकृत होती हैं जो `azure-identity` पैकेज से है। इसका मतलब है कि आपकी Azure CLI सेशन प्रमाणपत्र प्रदान करती है — आपके `.env` फाइल में कोई API कुंजी या सीक्रेट नहीं। यह [सुरक्षा की सर्वोत्तम प्रथा](https://learn.microsoft.com/azure/developer/ai/keyless-connections) है।

### चरण 4: अपनी `.env` फ़ाइल बनाएं

उदाहरण फ़ाइल कॉपी करें:

```bash
# zsh/bash
cp .env.example .env
```

```powershell
# पॉवरशेल
Copy-Item .env.example .env
```

`.env` खोलें और इन दो मानों को भरें:

```env
AZURE_AI_PROJECT_ENDPOINT=https://<your-project>.services.ai.azure.com/api/projects/<your-project-id>
AZURE_AI_MODEL_DEPLOYMENT_NAME=gpt-5-mini
```

| परिवर्तनशील | इसे कहां खोजें |
|----------|-----------------|
| `AZURE_AI_PROJECT_ENDPOINT` | Foundry पोर्टल → आपका प्रोजेक्ट → **Overview** पेज |
| `AZURE_AI_MODEL_DEPLOYMENT_NAME` | Foundry पोर्टल → **Models + Endpoints** → आपके डिप्लॉय किए गए मॉडल का नाम |

अधिकांश पाठों के लिए बस इतना ही! नोटबुक्स आपके `az login` सेशन के माध्यम से स्वचालित रूप से प्रमाणीकृत हो जाएंगी।

### चरण 5: Python निर्भरताएँ इंस्टॉल करें

```bash
pip install -r requirements.txt
```

हम अनुशंसा करते हैं कि आप इसे उस वर्चुअल एनवायरनमेंट में चलाएं जो आपने पहले बनाया था।

## वैकल्पिक सेटअप: Azure AI Search (पाठ 5 और 16)

पाठ 5 (Agentic RAG) और पाठ 16 नोटबुक्स बिना किसी अतिरिक्त Azure संसाधनों के **इन-मेमोरी नॉलेज बेस** के साथ तुरंत चलती हैं। यदि आप इन्हें एक वास्तविक **Azure AI Search** इंडेक्स के साथ बैक करना चाहते हैं, तो जान लें कि **पाठ 16 नोटबुक वर्तमान में कुंजी आधारित प्रमाणीकरण का उपयोग करता है**: यह इन-मेमोरी खोज से Azure AI Search पर केवल तब स्विच करता है जब **दोनों** `AZURE_SEARCH_SERVICE_ENDPOINT` **और** `AZURE_SEARCH_API_KEY` सेट हों, अन्यथा यह इन-मेमोरी खोज पर रहता है — इसलिए इसे वास्तविक इंडेक्स के खिलाफ चलाने के लिए आप एडमिन कुंजी भी सेट करें। कुंजी रहित प्रमाणीकरण Microsoft Entra ID (RBAC) के साथ अनुशंसित तरीका है, जो इस कोर्स में कहीं और उपयोग किया जाने वाला `az login` फ़्लो के अनुरूप है।

निम्न RBAC चरण सेटअप-गाइड नमूनों और आपके स्वयं के कोड पर लागू होते हैं। वे पाठ 16 नोटबुक में कुंजी रहित प्रमाणीकरण सक्षम नहीं करते; पाठ 16 अभी भी Azure AI Search का उपयोग करने के लिए दोनों एंडपॉइंट और एडमिन कुंजी मांगता है।

1. अपनी खोज सेवा पर **रोल-आधारित पहुँच सक्षम करें**:

    ```bash
    az search service update --name <service-name> --resource-group <resource-group> --auth-options aadOrApiKey
    ```

2. खुद को आवश्यक भूमिकाएँ असाइन करें (इंडेक्स बनाएं/लोड करें और क्वेरी करें):

    ```bash
    az role assignment create --assignee <your-user-or-principal-id> --role "Search Service Contributor" --scope $(az search service show -g <resource-group> -n <service-name> --query id -o tsv)
    az role assignment create --assignee <your-user-or-principal-id> --role "Search Index Data Contributor" --scope $(az search service show -g <resource-group> -n <service-name> --query id -o tsv)
    ```

3. अपनी `.env` फ़ाइल में एंडपॉइंट जोड़ें:

| परिवर्तनशील | इसे कहां खोजें |
|----------|-----------------|
| `AZURE_SEARCH_SERVICE_ENDPOINT` | Azure पोर्टल → आपकी **Azure AI Search** संसाधन → **Overview** → URL |
| `AZURE_SEARCH_API_KEY` | आवश्यक (एंडपॉइंट के साथ) ताकि पाठ 16 नोटबुक में Azure AI Search सक्षम हो सके, जो कुंजी आधारित प्रमाणीकरण का उपयोग करता है। Azure पोर्टल → **Settings** → **Keys** → प्राथमिक एडमिन कुंजी |

> **क्यों कुंजी रहित?** एडमिन कुंजी आपकी खोज सेवा को पूरी लिखने की अनुमति देती हैं और `.env` फ़ाइलों के माध्यम से लीक हो सकती हैं। RBAC के साथ, आपकी `az login` पहचान का उपयोग किया जाता है — वही कुंजी रहित Entra ID पैटर्न जो कोर्स के नोटबुक्स उपयोग करते हैं (`AzureCliCredential` / `DefaultAzureCredential` के माध्यम से)। देखें [Roles का उपयोग करते हुए Azure AI Search से कनेक्ट करें](https://learn.microsoft.com/azure/search/search-security-rbac)।

पूरे इंडेक्स निर्माण के नमूने पाइथन और .NET दोनों में देखने के लिए [Azure AI Search सेटअप गाइड](./AzureSearch.md) देखें।

## उन पाठों के लिए अतिरिक्त सेटअप जो सीधे Azure OpenAI कॉल करते हैं (पाठ 6 और 8)

कुछ नोटबुक्स पाठ 6 और 8 में **Responses API** के माध्यम से सीधे **Azure OpenAI** को कॉल करते हैं बजाय Microsoft Foundry प्रोजेक्ट के। ये नमूने पहले GitHub Models का उपयोग करते थे, जो अप्रचलित है और Responses API का समर्थन नहीं करता। इन परिवर्तनीयों को अपनी `.env` फ़ाइल में जोड़ें:

| परिवर्तनशील | इसे कहां खोजें |
|----------|-----------------|
| `AZURE_OPENAI_ENDPOINT` | Azure पोर्टल → आपकी **Azure OpenAI** संसाधन → **Keys and Endpoint** → Endpoint (जैसे `https://<your-resource>.openai.azure.com`) |
| `AZURE_OPENAI_DEPLOYMENT` | आपके डिप्लॉय किए गए मॉडल का नाम (जैसे `gpt-5-mini`) जो Responses API का समर्थन करता है |
| `AZURE_OPENAI_API_KEY` | वैकल्पिक — केवल यदि आप `az login` / Entra ID के बजाय कुंजी आधारित प्रमाणीकरण का उपयोग करते हैं |

> Responses API स्थिर `/openai/v1/` एंडपॉइंट का उपयोग करता है, इसलिए `api-version` आवश्यक नहीं है। keyless Entra ID प्रमाणीकरण के लिए `az login` से साइन इन करें।

## वैकल्पिक प्रदाता: MiniMax (OpenAI-अनुकूल)

[MiniMax](https://platform.minimaxi.com/) बड़े-कंटेक्स्ट मॉडल (204K टोकन तक) OpenAI-रूपांतरण API के माध्यम से प्रदान करता है। Microsoft Agent Framework का `OpenAIChatClient` किसी भी OpenAI-रूपांतरण एंडपॉइंट पर काम करता है, इसलिए आप MiniMax को उन पाठों के लिए एक विकल्प के रूप में उपयोग कर सकते हैं जो `OpenAIChatClient` का उपयोग करते हैं।

इन परिवर्तनीयों को अपनी `.env` फ़ाइल में जोड़ें:

| परिवर्तनशील | इसे कहां खोजें |
|----------|-----------------|
| `MINIMAX_API_KEY` | [MiniMax Platform](https://platform.minimaxi.com/) → API Keys |
| `MINIMAX_BASE_URL` | `https://api.minimax.io/v1` (डिफ़ॉल्ट मान) का उपयोग करें |
| `MINIMAX_MODEL_ID` | उपयोग करने के लिए मॉडल नाम (जैसे, `MiniMax-M3`) |

**उदाहरण मॉडल**: `MiniMax-M3` (अनुशंसित), `MiniMax-M2.7`, `MiniMax-M2.7-highspeed` (तेजी से प्रतिक्रियाएं)। मॉडल नाम और उपलब्धता समय के साथ बदल सकती है, और किसी विशिष्ट मॉडल तक आपकी पहुँच आपके खाते पर निर्भर हो सकती है।

कोड नमूने जो `OpenAIChatClient` का उपयोग करते हैं (जैसे, पाठ 14 होटल बुकिंग वर्कफ़्लो) आपके MiniMax कॉन्फ़िगरेशन का स्वचालित पता लगाएंगे और उपयोग करेंगे जब `MINIMAX_API_KEY` सेट हो।


## वैकल्पिक प्रदाता: Novita AI (OpenAI-अनुकूल)

[Novita AI](https://novita.ai/llm-api) ओपन-सोर्स और अग्रणी LLMs (DeepSeek, Llama, Qwen, और अधिक) के लिए OpenAI-अनुकूल API प्रदान करता है। चूंकि Microsoft Agent Framework का `OpenAIChatClient` किसी भी OpenAI-अनुकूल अंत बिंदु के साथ काम करता है, इसलिए आप Novita AI को Azure OpenAI या OpenAI के लिए ड्रॉप-इन विकल्प के रूप में उपयोग कर सकते हैं।

अपने `.env` फ़ाइल में ये वेरिएबल जोड़ें:

| वेरिएबल | इसे कहां खोजें |
|----------|-----------------|
| `NOVITA_API_KEY` | [Novita AI डैशबोर्ड](https://novita.ai/settings/key-management) → API कुंजी |
| `NOVITA_BASE_URL` | `https://api.novita.ai/openai/v1` का उपयोग करें (डिफ़ॉल्ट मान) |
| `NOVITA_MODEL_ID` | उपयोग करने के लिए मॉडल नाम (जैसे, `moonshotai/kimi-k3`) |

**उदाहरण मॉडल**: `moonshotai/kimi-k3`, `zai-org/glm-5.2`, `deepseek/deepseek-v4-flash-0731`। Novita AI कई अन्य ओपन-सोर्स मॉडल परिवार (Llama, Qwen, GLM, और अधिक) भी होस्ट करता है — वर्तमान उपलब्ध मॉडलों और उनके मॉडल IDs के लिए [Novita AI मॉडल लाइब्रेरी](https://novita.ai/llm-api) देखें।

वर्तमान नमूने `NOVITA_*` वेरिएबल्स को स्वचालित रूप से उपयोग नहीं करते। Novita AI का उपयोग करने के लिए, आप जिन नमूनों को चला रहे हैं उनमें `OpenAIChatClient` बनाते समय इन मानों को स्पष्ट रूप से पास करें।

## वैकल्पिक प्रदाता: Foundry Local (मॉडल ऑन-डिवाइस चलाएं)

[Foundry Local](https://foundrylocal.ai) एक हल्का रनटाइम है जो भाषा मॉडल को **पूरी तरह से आपके अपने कंप्यूटर पर** OpenAI-अनुकूल API के माध्यम से डाउनलोड, प्रबंधित और सर्व करता है — कोई क्लाउड आवश्यक नहीं।

क्योंकि Microsoft Agent Framework का `OpenAIChatClient` किसी भी OpenAI-अनुकूल अंत बिंदु के साथ काम करता है, Foundry Local Azure OpenAI के लिए एक स्थानीय ड्रॉप-इन विकल्प है।

**1. Foundry Local इंस्टॉल करें**

```bash
# विंडोज़
winget install Microsoft.FoundryLocal

# मैकओएस
brew install foundrylocal
```

**2. एक मॉडल डाउनलोड करें और चलाएं** (यह स्थानीय सेवा भी शुरू करता है):

```bash
foundry model list          # उपलब्ध मॉडल देखें
foundry model run phi-4-mini
```

**3. स्थानीय अंत बिंदु खोजने के लिए उपयोग किया जाने वाला Python SDK इंस्टॉल करें:**

```bash
pip install foundry-local-sdk
```

**4. Microsoft Agent Framework को अपने स्थानीय मॉडल की ओर निर्देशित करें:**

```python
from foundry_local import FoundryLocalManager
from agent_framework.openai import OpenAIChatClient

# मॉडल को डाउनलोड करता है (यदि आवश्यक हो) और स्थानीय रूप से सेवा प्रदान करता है, फिर एंडपॉइंट/पोर्ट खोजता है।
manager = FoundryLocalManager("phi-4-mini")

chat_client = OpenAIChatClient(
    base_url=manager.endpoint,      # उदाहरण के लिए http://localhost:<port>/v1
    api_key=manager.api_key,        # Foundry Local के लिए हमेशा "not-required"
    model_id=manager.get_model_info("phi-4-mini").id,
)

agent = chat_client.as_agent(
    name="LocalAgent",
    instructions="You are a helpful assistant running fully on-device.",
)
```

> **नोट:** Foundry Local एक OpenAI-अनुकूल **Chat Completions** अंत बिंदु प्रदान करता है। इसे स्थानीय विकास और ऑफ़लाइन परिदृश्यों के लिए उपयोग करें। पूर्ण **Responses API** फीचर सेट (स्थिति आधारित बातचीत, आदि) के लिए, Azure OpenAI या Microsoft Foundry प्रोजेक्ट का उपयोग करें।

## पाठ 8 के लिए अतिरिक्त सेटअप (Bing ग्राउंडिंग वर्कफ़्लो)

पाठ 8 में स्थितीय वर्कफ़्लो नोटबुक Microsoft Foundry के माध्यम से **Bing ग्राउंडिंग** का उपयोग करता है। यदि आप उस नमूने को चलाने की योजना बना रहे हैं, तो अपनी `.env` फ़ाइल में यह वेरिएबल जोड़ें:

| वेरिएबल | इसे कहां खोजें |
|----------|-----------------|
| `BING_CONNECTION_ID` | Microsoft Foundry पोर्टल → आपका प्रोजेक्ट → **Management** → **Connected resources** → आपकी Bing कनेक्शन → कनेक्शन ID कॉपी करें |

## समस्या निवारण

### macOS पर SSL सर्टिफिकेट सत्यापन त्रुटियाँ

यदि आप macOS पर हैं और इस प्रकार की त्रुटि आती है:

```plaintext
ssl.SSLCertVerificationError: [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: self-signed certificate in certificate chain
```

यह macOS पर Python की एक ज्ञात समस्या है जहाँ सिस्टम SSL सर्टिफिकेट स्वचालित रूप से भरोसेमंद नहीं होते। निम्नलिखित समाधान क्रम में आज़माएं:

**विकल्प 1: Python का Install Certificates स्क्रिप्ट चलाएं (अनुशंसित)**

```bash
# अपनी स्थापित Python संस्करण के साथ 3.XX को बदलें (जैसे, 3.12 या 3.13):
/Applications/Python\ 3.XX/Install\ Certificates.command
```

**विकल्प 2: अपने नोटबुक में `connection_verify=False` का उपयोग करें (केवल GitHub Models नोटबुक के लिए)**

पाठ 6 के नोटबुक (`06-building-trustworthy-agents/code_samples/06-system-message-framework.ipynb`) में, एक टिप्पणी किया गया समाधान पहले से शामिल है। जब आपको सर्टिफिकेट संबंधित त्रुटि हो, तो `connection_verify=False` को Uncomment करें:

```python
client = ChatCompletionsClient(
    endpoint=endpoint,
    credential=AzureKeyCredential(token),
    connection_verify=False,  # यदि आपको प्रमाणपत्र त्रुटियां मिलती हैं तो SSL सत्यापन असक्षम करें
)
```

> **⚠️ चेतावनी:** SSL सत्यापन अक्षम करना (`connection_verify=False`) सुरक्षा को कम करता है क्योंकि यह सर्टिफिकेट सत्यापन को स्किप कर देता है। इसे केवल विकास पर्यावरण में अस्थायी समाधान के रूप में उपयोग करें। इसे प्रोडक्शन में कभी भी उपयोग न करें।

**विकल्प 3: `truststore` इंस्टॉल करें और उपयोग करें**

```bash
pip install truststore
```

फिर अपने नोटबुक या स्क्रिप्ट की शुरुआत में नेटवर्क कॉल करने से पहले निम्नलिखित जोड़ें:

```python
import truststore
truststore.inject_into_ssl()
```

## कहीं फंसे हुए हैं?

यदि आपको इस सेटअप को चलाने में कोई समस्या आती है, तो हमारे <a href="https://discord.gg/kzRShWzttr" target="_blank">Azure AI Community Discord</a> में शामिल हों या <a href="https://github.com/microsoft/ai-agents-for-beginners/issues?WT.mc_id=academic-105485-koreyst" target="_blank">इश्यू बनाएं</a>.

## अगला पाठ

अब आप इस कोर्स के लिए कोड चलाने के लिए तैयार हैं। AI एजेंट्स की दुनिया के बारे में अधिक सीखने के लिए शुभकामनाएँ!

[AI एजेंट्स और एजेंट उपयोग मामलों का परिचय](../01-intro-to-ai-agents/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**अस्वीकरण**:
इस दस्तावेज़ का अनुवाद AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) का उपयोग करके किया गया है। जबकि हम सटीकता के लिए प्रयास करते हैं, कृपया ध्यान दें कि स्वचालित अनुवादों में त्रुटियाँ या अशुद्धियाँ हो सकती हैं। मूल दस्तावेज़ अपनी मूल भाषा में ही प्रामाणिक स्रोत माना जाना चाहिए। महत्वपूर्ण जानकारी के लिए, पेशेवर मानव अनुवाद की सिफारिश की जाती है। इस अनुवाद के उपयोग से उत्पन्न किसी भी गलतफहमी या गलत व्याख्या के लिए हम उत्तरदायी नहीं हैं।
<!-- CO-OP TRANSLATOR DISCLAIMER END -->