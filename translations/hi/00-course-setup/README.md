# पाठ्यक्रम सेटअप

## परिचय

इस पाठ में इस कोर्स के कोड नमूनों को चलाने का तरीका शामिल होगा।

## अन्य शिक्षार्थियों से जुड़ें और मदद प्राप्त करें

अपनी रिपॉज़िटरी क्लोन करना शुरू करने से पहले, सेटअप में किसी भी मदद, कोर्स के बारे में कोई भी प्रश्न, या अन्य शिक्षार्थियों से जुड़ने के लिए [AI Agents For Beginners Discord चैनल](https://aka.ms/ai-agents/discord) से जुड़ें।

## इस रिपॉज़िटरी को क्लोन या फोर्क करें

शुरू करने के लिए, कृपया GitHub रिपॉज़िटरी को क्लोन या फोर्क करें। यह आपके लिए कोर्स सामग्री का अपना संस्करण बनाएगा ताकि आप कोड चला, परीक्षण कर, और उसमें संशोधन कर सकें!

यह <a href="https://github.com/microsoft/ai-agents-for-beginners/fork" target="_blank">reop को फोर्क करने</a> के लिंक पर क्लिक करके किया जा सकता है

अब आपके पास इस कोर्स का अपना फोर्क किया हुआ संस्करण निम्नलिखित लिंक में होना चाहिए:

![Forked Repo](../../../translated_images/hi/forked-repo.33f27ca1901baa6a.webp)

### शैलो क्लोन (वर्कशॉप / कोडस्पेसेस के लिए अनुशंसित)

> जब आप पूरी इतिहास और सभी फ़ाइलें डाउनलोड करते हैं, तो पूरी रिपॉजिटरी बड़ी (~3 GB) हो सकती है। यदि आप केवल वर्कशॉप में भाग ले रहे हैं या केवल कुछ पाठ फ़ोल्डर चाहते हैं, तो एक शैलो क्लोन (या स्पार्स क्लोन) इतिहास को छोटा कर और/या ब्लॉब्स छोड़ कर अधिकांश डाउनलोड से बचता है।

#### त्वरित शैलो क्लोन — न्यूनतम इतिहास, सभी फ़ाइलें

नीचे दिए गए कमांड में `<your-username>` को अपनी फोर्क URL (या यदि आप चाहें तो अपस्ट्रीम URL) से बदलें।

केवल नवीनतम कमिट इतिहास को क्लोन करने के लिए (छोटा डाउनलोड):

```bash|powershell
git clone --depth 1 https://github.com/<your-username>/ai-agents-for-beginners.git
```

किसी विशेष शाखा को क्लोन करने के लिए:

```bash|powershell
git clone --depth 1 --branch <branch-name> https://github.com/<your-username>/ai-agents-for-beginners.git
```

#### आंशिक (स्पार्स) क्लोन — न्यूनतम ब्लॉब्स + केवल चयनित फ़ोल्डर

यह आंशिक क्लोन और स्पार्स-चेकआउट का उपयोग करता है (Git 2.25+ और आंशिक क्लोन समर्थन वाले आधुनिक Git की आवश्यकता है और अनुशंसित है):

```bash|powershell
git clone --depth 1 --filter=blob:none --sparse https://github.com/<your-username>/ai-agents-for-beginners.git
```

रिपॉजिटरी फ़ोल्डर में जाएँ:

```bash|powershell
cd ai-agents-for-beginners
```

फिर यह निर्दिष्ट करें कि आपको कौन से फ़ोल्डर चाहिए (नीचे उदाहरण दो फ़ोल्डरों को दिखाता है):

```bash|powershell
git sparse-checkout set 00-course-setup 01-intro-to-ai-agents
```

क्लोन करने और फ़ाइलों को सत्यापित करने के बाद, यदि आपको केवल फ़ाइलों की आवश्यकता है और आप स्थान मुक्त करना चाहते हैं (कोई git इतिहास नहीं), तो कृपया रिपॉजिटरी मेटाडेटा को हटा दें (💀अपरिवर्तनीय — आप सभी Git कार्यक्षमता खो देंगे: कोई कमिट्स, पुल, पुश या इतिहास एक्सेस नहीं)।

```bash
# जेडएसएच/बैश
rm -rf .git
```

```powershell
# पावरशेल
Remove-Item -Recurse -Force .git
```

#### GitHub Codespaces का उपयोग करना (स्थानीय बड़े डाउनलोड से बचने के लिए अनुशंसित)

- इस रिपो के लिए [GitHub UI](https://github.com/codespaces) के माध्यम से नया कोडस्पेस बनाएं।  

- नए बनाए गए कोडस्पेस के टर्मिनल में, ऊपर दिए गए शैलो/स्पार्स क्लोन कमांड में से एक चलाएँ ताकि केवल आवश्यक पाठ फ़ोल्डर कोडस्पेस वर्कस्पेस में लाए जा सकें।
- वैकल्पिक: Codespaces के अंदर क्लोनिंग के बाद, अतिरिक्त स्थान पुनः प्राप्त करने के लिए .git फ़ोल्डर को हटा दें (ऊपर हटाने के कमांड देखें)।
- नोट: यदि आप रिपोज़िटरी को सीधे Codespaces में खोलना पसंद करते हैं (अतिरिक्त क्लोन के बिना), तो ध्यान दें कि Codespaces डेवकंटेनर वातावरण बनाएगा और आप जितना उपयोग करेंगे उससे अधिक प्रोविजन कर सकता है। एक ताजा Codespace के अंदर एक शैलो कॉपी क्लोन करने से आपको डिस्क उपयोग पर अधिक नियंत्रण मिलता है।

#### सुझाव

- यदि आप संपादित/कमिट करना चाहते हैं, तो हमेशा क्लोन URL को अपनी फोर्क से बदलें।
- यदि बाद में आपको अधिक इतिहास या फ़ाइलों की आवश्यकता हो, तो आप उन्हें प्राप्त कर सकते हैं या अतिरिक्त फ़ोल्डरों को शामिल करने के लिए sparse-checkout समायोजित कर सकते हैं।

## कोड चलाना

यह कोर्स कुछ जुपिटर नोटबुक प्रदान करता है जिन्हें आप AI एजेंट बनाने का अनुभव प्राप्त करने के लिए चला सकते हैं।

कोड नमूने **Microsoft Agent Framework (MAF)** का उपयोग करते हैं जिसमें `FoundryChatClient` है, जो **Microsoft Foundry Agent Service V2** (Responses API) से **Microsoft Foundry** के माध्यम से जुड़ता है।

सभी पायथन नोटबुक को `*-python-agent-framework.ipynb` के रूप में लेबल किया गया है।

## आवश्यकताएँ

- Python 3.12+
  - **नोट:** यदि आपके पास Python3.12 स्थापित नहीं है, तो सुनिश्चित करें कि आप इसे स्थापित करें। फिर requirements.txt फ़ाइल से सही संस्करण स्थापित करने के लिए python3.12 का उपयोग करके अपना venv बनाएं।
  
    > उदाहरण

    Python venv डायरेक्टरी बनाएं:

    ```bash|powershell
    python -m venv venv
    ```

    फिर सक्रिय करें venv पर्यावरण:

    ```bash
    # zsh/bash
    source venv/bin/activate
    ```
  
    ```dos
    # Command Prompt for Windows
    venv\Scripts\activate
    ```

- .NET 10+: .NET का उपयोग करने वाले नमूना कोड के लिए, सुनिश्चित करें कि आप [.NET 10 SDK](https://dotnet.microsoft.com/download/dotnet/10.0) या उससे नया संस्करण स्थापित करें। फिर, अपने स्थापित .NET SDK संस्करण की जांच करें:

    ```bash|powershell
    dotnet --list-sdks
    ```

- **Azure CLI** — प्रमाणीकरण के लिए आवश्यक। [aka.ms/installazurecli](https://aka.ms/installazurecli) से इंस्टॉल करें।
- **Azure सदस्यता** — Microsoft Foundry और Microsoft Foundry Agent Service तक पहुँच के लिए।
- **Microsoft Foundry परियोजना** — एक परियोजना जिसमें तैनात मॉडल हो (जैसे, `gpt-5-mini`)। देखें [चरण 1](#चरण-1-एक-microsoft-foundry-प्रोजेक्ट-बनाएं)।

इस रिपॉजिटरी की रूट में `requirements.txt` फाइल शामिल है जिसमें कोड नमूने चलाने के लिए सभी आवश्यक पायथन पैकेज हैं।

आप इसे रिपॉजिटरी के रूट में अपने टर्मिनल में निम्नलिखित कमांड चलाकर इंस्टॉल कर सकते हैं:

```bash|powershell
pip install -r requirements.txt
```

हम किसी भी संघर्ष और समस्याओं से बचने के लिए पायथन वर्चुअल एनवायरनमेंट बनाने की सलाह देते हैं।

## VSCode सेटअप करें

सुनिश्चित करें कि आप VSCode में सही पायथन संस्करण का उपयोग कर रहे हैं।

![image](https://github.com/user-attachments/assets/a85e776c-2edb-4331-ae5b-6bfdfb98ee0e)

## Microsoft Foundry और Microsoft Foundry Agent Service सेटअप करें

### चरण 1: एक Microsoft Foundry प्रोजेक्ट बनाएं

आपको नोटबुक चलाने के लिए Microsoft Foundry का **hub** और एक तैनात मॉडल वाला **prject** चाहिए।

1. [ai.azure.com](https://ai.azure.com) पर जाएं और अपने Azure खाते से साइन इन करें।
2. एक **hub** बनाएं (या किसी मौजूदा का उपयोग करें)। देखें: [Hub resources overview](https://learn.microsoft.com/azure/ai-foundry/concepts/ai-resources)।
3. हब के अंदर एक **प्रोजेक्ट** बनाएं।
4. **Models + Endpoints** → **Deploy model** से एक मॉडल (जैसे `gpt-5-mini`) तैनात करें।

### चरण 2: अपने प्रोजेक्ट एंडपॉइंट और मॉडल तैनाती नाम प्राप्त करें

Microsoft Foundry पोर्टल में अपने प्रोजेक्ट से:

- **प्रोजेक्ट एंडपॉइंट** — **अवलोकन** पृष्ठ पर जाएं और एंडपॉइंट URL कॉपी करें।

![Project Connection String](../../../translated_images/hi/project-endpoint.8cf04c9975bbfbf1.webp)

- **मॉडल तैनाती नाम** — **Models + Endpoints** पर जाएं, अपने तैनात मॉडल का चयन करें, और **Deployment name** नोट करें (जैसे `gpt-5-mini`)।

### चरण 3: `az login` के साथ Azure में साइन इन करें

सभी नोटबुक प्रमाणीकरण के लिए **`AzureCliCredential`** का उपयोग करते हैं — कोई API कुंजी प्रबंधित करने की आवश्यकता नहीं। इसके लिए Azure CLI के माध्यम से साइन इन होना आवश्यक है।

1. यदि आपने पहले से Azure CLI इंस्टॉल नहीं किया है तो इसे इंस्टॉल करें: [aka.ms/installazurecli](https://aka.ms/installazurecli)

2. इसके बाद साइन इन करें:

    ```bash|powershell
    az login
    ```

    या यदि आप रिमोट/कोडस्पेस वातावरण में हैं जहाँ ब्राउज़र नहीं है:

    ```bash|powershell
    az login --use-device-code
    ```

3. यदि पूछा जाए तो अपनी सदस्यता चुनें — वह जिसमें आपका Foundry प्रोजेक्ट हो।

4. पुष्टि करें कि आप साइन इन हैं:

    ```bash|powershell
    az account show
    ```

> **`az login` क्यों?** नोटबुक `azure-identity` पैकेज से `AzureCliCredential` का उपयोग करके प्रमाणीकरण करते हैं। इसका मतलब है कि आपकी Azure CLI सत्र क्रेडेंशियल प्रदान करता है — आपकी `.env` फाइल में कोई API कुंजी या सीक्रेट्स नहीं। यह एक [सुरक्षा सर्वोत्तम प्रथा](https://learn.microsoft.com/azure/developer/ai/keyless-connections) है।

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

| वेरिएबल | कहाँ मिलेगा |
|----------|-----------------|
| `AZURE_AI_PROJECT_ENDPOINT` | Foundry पोर्टल → आपका प्रोजेक्ट → **अवलोकन** पृष्ठ |
| `AZURE_AI_MODEL_DEPLOYMENT_NAME` | Foundry पोर्टल → **Models + Endpoints** → आपके तैनात मॉडल का नाम |

अधिकांश पाठों के लिए बस इतना ही! नोटबुक `az login` सत्र के माध्यम से स्वचालित रूप से प्रमाणीकरण करेगा।

### चरण 5: पायथन निर्भरताएं इंस्टॉल करें

```bash|powershell
pip install -r requirements.txt
```

हम सुझाव देते हैं कि इसे आप पहले बनाए गए वर्चुअल एनवायरनमेंट के अंदर चलाएं।

## पाठ 5 (Agentic RAG) के लिए अतिरिक्त सेटअप

पाठ 5 में पुनः प्राप्ति-ऑगमेंटेड जेनरेशन के लिए **Azure AI Search** का उपयोग होता है। यदि आप वह पाठ चलाने की योजना बना रहे हैं, तो अपनी `.env` फाइल में ये वेरिएबल जोड़ें:

| वेरिएबल | कहाँ मिलेगा |
|----------|-----------------|
| `AZURE_SEARCH_SERVICE_ENDPOINT` | Azure पोर्टल → आपका **Azure AI Search** संसाधन → **अवलोकन** → URL |
| `AZURE_SEARCH_API_KEY` | Azure पोर्टल → आपका **Azure AI Search** संसाधन → **Settings** → **Keys** → प्राथमिक एडमिन कुंजी |

## पाठ जो Azure OpenAI को सीधे कॉल करते हैं उनके लिए अतिरिक्त सेटअप (पाठ 6 और 8)

पाठ 6 और 8 की कुछ नोटबुक सीधे **Azure OpenAI** ( **Responses API** का उपयोग करके) को कॉल करती हैं, बजाय किसी Microsoft Foundry प्रोजेक्ट के। ये नमूने पूर्व में GitHub Models का उपयोग करते थे, जो अब अप्रचलित है (जुलाई 2026 में समाप्त हो रहा है) और Responses API को समर्थन नहीं करता। यदि आप उन नमूनों को चलाने की योजना बना रहे हैं, तो अपनी `.env` फाइल में ये वेरिएबल जोड़ें:

| वेरिएबल | कहाँ मिलेगा |
|----------|-----------------|
| `AZURE_OPENAI_ENDPOINT` | Azure पोर्टल → आपका **Azure OpenAI** संसाधन → **Keys and Endpoint** → एंडपॉइंट (जैसे `https://<your-resource>.openai.azure.com`) |
| `AZURE_OPENAI_DEPLOYMENT` | आपके तैनात मॉडल का नाम (जैसे `gpt-5-mini`) जो Responses API का समर्थन करता हो |
| `AZURE_OPENAI_API_KEY` | वैकल्पिक — केवल यदि आप key-based प्रमाणीकरण का उपयोग करते हैं `az login` / Entra ID के बजाय |

> Responses API स्थिर `/openai/v1/` एंडपॉइंट का उपयोग करता है, इसलिए कोई `api-version` आवश्यक नहीं है। keyless Entra ID प्रमाणीकरण के लिए `az login` के साथ साइन इन करें।

## वैकल्पिक प्रदाता: MiniMax (OpenAI-संगत)

[MiniMax](https://platform.minimaxi.com/) बड़े संदर्भ मॉडल (204K टोकन तक) OpenAI-संगत API के माध्यम से प्रदान करता है। Microsoft Agent Framework का `OpenAIChatClient` किसी भी OpenAI-संगत एंडपॉइंट के साथ काम करता है, इसलिए आप Azure OpenAI या OpenAI के बजाय MiniMax का इस्तेमाल कर सकते हैं।

अपनी `.env` फाइल में ये वेरिएबल जोड़ें:

| वेरिएबल | कहाँ मिलेगा |
|----------|-----------------|
| `MINIMAX_API_KEY` | [MiniMax Platform](https://platform.minimaxi.com/) → API कुंजी |
| `MINIMAX_BASE_URL` | उपयोग करें `https://api.minimax.io/v1` (डिफ़ॉल्ट मान) |
| `MINIMAX_MODEL_ID` | उपयोग करने के लिए मॉडल का नाम (जैसे, `MiniMax-M3`) |

**उदाहरण मॉडल**: `MiniMax-M3` (अनुशंसित), `MiniMax-M2.7`, `MiniMax-M2.7-highspeed` (तेजी से प्रतिक्रियाएँ)। मॉडल नाम और उपलब्धता समय के साथ बदल सकती है, और किसी विशेष मॉडल का उपयोग आपके खाते या क्षेत्र पर निर्भर कर सकता है — वर्तमान सूची के लिए [MiniMax Platform](https://platform.minimaxi.com/) देखें। यदि `MiniMax-M3` आपके खाते के लिए उपलब्ध नहीं है, तो `MINIMAX_MODEL_ID` को उस मॉडल पर सेट करें जिसे आप उपयोग कर सकते हैं (जैसे `MiniMax-M2.7`)।

जो कोड नमूने `OpenAIChatClient` का उपयोग करते हैं (जैसे पाठ 14 होटल बुकिंग वर्कफ़्लो), वे स्वतः ही आपका MiniMax कॉन्फ़िगरेशन पहचान कर उपयोग करेंगे जब `MINIMAX_API_KEY` सेट होगा।

## वैकल्पिक प्रदाता: Foundry Local (डिवाइस पर मॉडल चलाएं)

[Foundry Local](https://foundrylocal.ai) एक हल्का रनटाइम है जो आपके अपने मशीन पर OpenAI-संगत API के माध्यम से भाषा मॉडल डाउनलोड, प्रबंधित और सेवा करता है — कोई क्लाउड, कोई Azure सदस्यता, और कोई API कुंजी नहीं। यह ऑफ़लाइन विकास, बिना क्लाउड लागत के प्रयोग, या डेटा डिवाइस पर रखने के लिए एक बढ़िया विकल्प है।

चूंकि Microsoft Agent Framework का `OpenAIChatClient` किसी भी OpenAI-संगत एंडपॉइंट के साथ काम करता है, Foundry Local Azure OpenAI के लिए एक स्थानीय विकल्प है।

**1. Foundry Local इंस्टॉल करें**

```bash
# विंडोज
winget install Microsoft.FoundryLocal

# मैकओएस
brew install foundrylocal
```

**2. एक मॉडल डाउनलोड करें और चलाएं** (यह लोकल सेवा भी शुरू करता है):

```bash
foundry model list          # उपलब्ध मॉडल देखें
foundry model run phi-4-mini
```

**3. Python SDK इंस्टॉल करें** जो लोकल एंडपॉइंट खोजता है:

```bash
pip install foundry-local-sdk
```

**4. Microsoft Agent Framework को अपने लोकल मॉडल पर इंगित करें:**

```python
from foundry_local import FoundryLocalManager
from agent_framework.openai import OpenAIChatClient

# मॉडल को डाउनलोड करता है (यदि आवश्यक हो) और स्थानीय रूप से सेवा प्रदान करता है, फिर एंडपॉइंट/पोर्ट का पता लगाता है।
manager = FoundryLocalManager("phi-4-mini")

chat_client = OpenAIChatClient(
    base_url=manager.endpoint,      # उदाहरण के लिए http://localhost:<port>/v1
    api_key=manager.api_key,        # Foundry Local के लिए हमेशा "not-required" होता है।
    model_id=manager.get_model_info("phi-4-mini").id,
)

agent = chat_client.as_agent(
    name="LocalAgent",
    instructions="You are a helpful assistant running fully on-device.",
)
```

> **नोट:** Foundry Local एक OpenAI-संगत **Chat Completions** एंडपॉइंट एक्सपोज़ करता है। इसका उपयोग स्थानीय विकास और ऑफलाइन परिदृश्यों के लिए करें। पूर्ण **Responses API** फीचर सेट (स्टेटफुल वार्तालाप, गहरा टूल ऑर्केस्ट्रेशन, एजेंट-शैली विकास) के लिए, पाठों में दिखाए अनुसार **Azure OpenAI** या **Microsoft Foundry** प्रोजेक्ट को लक्षित करें। वर्तमान मॉडल सूची और प्लेटफ़ॉर्म समर्थन के लिए [Foundry Local दस्तावेज़](https://foundrylocal.ai) देखें।

## पाठ 8 (Bing Grounding Workflow) के लिए अतिरिक्त सेटअप


पाठ 8 में स्थित शर्तीय वर्कफ़्लो नोटबुक Microsoft Foundry के माध्यम से **Bing ग्राउंडिंग** का उपयोग करता है। यदि आप उस नमूने को चलाने की योजना बना रहे हैं, तो इस चर को अपनी `.env` फ़ाइल में जोड़ें:

| चर | इसे कहां खोजें |
|----------|-----------------|
| `BING_CONNECTION_ID` | Microsoft Foundry पोर्टल → आपका प्रोजेक्ट → **प्रबंधन** → **कनेक्टेड संसाधन** → आपका Bing कनेक्शन → कनेक्शन ID कॉपी करें |

## समस्याओं का समाधान

### macOS पर SSL प्रमाणपत्र सत्यापन त्रुटियाँ

यदि आप macOS पर हैं और इस प्रकार की त्रुटि का सामना करते हैं:

```plaintext
ssl.SSLCertVerificationError: [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: self-signed certificate in certificate chain
```

यह macOS पर Python के साथ एक ज्ञात समस्या है जहां सिस्टम SSL प्रमाणपत्र स्वचालित रूप से विश्वसनीय नहीं होते। निम्नलिखित समाधान क्रमबद्ध रूप से आज़माएं:

**विकल्प 1: Python के Install Certificates स्क्रिप्ट को चलाएं (सिफारिश किया गया)**

```bash
# अपने इंस्टॉल किए गए पाइथन संस्करण (जैसे, 3.12 या 3.13) से 3.XX बदलें:
/Applications/Python\ 3.XX/Install\ Certificates.command
```

**विकल्प 2: अपनी नोटबुक में `connection_verify=False` का उपयोग करें (केवल GitHub Models नोटबुक के लिए)**

पाठ 6 की नोटबुक में (`06-building-trustworthy-agents/code_samples/06-system-message-framework.ipynb`), एक टिप्पणीबद्ध कार्यान्वयन पहले से शामिल है। क्लाइंट बनाते समय `connection_verify=False` की टिप्पणी हटा दें:

```python
client = ChatCompletionsClient(
    endpoint=endpoint,
    credential=AzureKeyCredential(token),
    connection_verify=False,  # यदि आपको प्रमाणपत्र त्रुटियां मिलती हैं तो SSL सत्यापन अक्षम करें
)
```

> **⚠️ चेतावनी:** SSL सत्यापन को अक्षम करना (`connection_verify=False`) सुरक्षा कम करता है क्योंकि यह प्रमाणपत्र सत्यापन को छोड़ देता है। इसे केवल विकासात्मक वातावरण में अस्थायी समाधान के रूप में ही उपयोग करें, उत्पादन में कभी नहीं।

**विकल्प 3: `truststore` इंस्टॉल करें और उपयोग करें**

```bash
pip install truststore
```

फिर अपने नोटबुक या स्क्रिप्ट के शीर्ष पर नेटवर्क कॉल करने से पहले निम्नलिखित जोड़ें:

```python
import truststore
truststore.inject_into_ssl()
```

## कहीं अटक गए हैं?

यदि इस सेटअप को चलाने में आपको कोई समस्या हो, तो हमारे <a href="https://discord.gg/kzRShWzttr" target="_blank">Azure AI Community Discord</a> में जुड़ें या <a href="https://github.com/microsoft/ai-agents-for-beginners/issues?WT.mc_id=academic-105485-koreyst" target="_blank">एक मुद्दा बनाएं</a>।

## अगला पाठ

आप अब इस पाठ्यक्रम के कोड को चलाने के लिए तैयार हैं। एआई एजेंट्स की दुनिया के बारे में और जानने के लिए शुभकामनाएँ!

[AI एजेंट्स और एजेंट उपयोग केस का परिचय](../01-intro-to-ai-agents/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**अस्वीकरण**:
इस दस्तावेज़ का अनुवाद AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) का उपयोग करके किया गया है। जबकि हम सटीकता के लिए प्रयास करते हैं, कृपया ध्यान दें कि स्वचालित अनुवादों में त्रुटियाँ या अशुद्धियाँ हो सकती हैं। मूल दस्तावेज़ अपनी मूल भाषा में ही प्रामाणिक स्रोत माना जाना चाहिए। महत्वपूर्ण जानकारी के लिए, पेशेवर मानव अनुवाद की सिफारिश की जाती है। इस अनुवाद के उपयोग से उत्पन्न किसी भी गलतफहमी या गलत व्याख्या के लिए हम उत्तरदायी नहीं हैं।
<!-- CO-OP TRANSLATOR DISCLAIMER END -->