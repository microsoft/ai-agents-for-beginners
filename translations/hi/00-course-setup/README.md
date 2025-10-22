<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "96eb7f95375daa3e91778ca0295a55d9",
  "translation_date": "2025-10-15T08:33:44+00:00",
  "source_file": "00-course-setup/README.md",
  "language_code": "hi"
}
-->
# कोर्स सेटअप

## परिचय

इस पाठ में इस कोर्स के कोड नमूनों को कैसे चलाना है, इसके बारे में चर्चा की जाएगी।

## अन्य शिक्षार्थियों से जुड़ें और मदद प्राप्त करें

अपने रिपॉजिटरी को क्लोन करने से पहले, [AI Agents For Beginners Discord चैनल](https://aka.ms/ai-agents/discord) से जुड़ें ताकि सेटअप में मदद, कोर्स से संबंधित सवाल पूछ सकें, या अन्य शिक्षार्थियों से जुड़ सकें।

## इस रिपॉजिटरी को क्लोन या फोर्क करें

शुरू करने के लिए, कृपया GitHub रिपॉजिटरी को क्लोन या फोर्क करें। इससे आपके पास कोर्स सामग्री का अपना संस्करण होगा, जिसे आप चला सकते हैं, परीक्षण कर सकते हैं और कोड में बदलाव कर सकते हैं!

यह <a href="https://github.com/microsoft/ai-agents-for-beginners/fork" target="_blank">रिपॉजिटरी को फोर्क करें</a> लिंक पर क्लिक करके किया जा सकता है।

अब आपके पास इस कोर्स का अपना फोर्क किया हुआ संस्करण निम्नलिखित लिंक पर होगा:

![Forked Repo](../../../translated_images/forked-repo.33f27ca1901baa6a5e13ec3eb1f0ddd3a44d936d91cc8cfb19bfdb9688bd2c3d.hi.png)

### शैलो क्लोन (वर्कशॉप / कोडस्पेस के लिए अनुशंसित)

  > जब आप पूरी रिपॉजिटरी डाउनलोड करते हैं तो यह बहुत बड़ी (~3 GB) हो सकती है। यदि आप केवल वर्कशॉप में भाग ले रहे हैं या केवल कुछ पाठ फ़ोल्डर की आवश्यकता है, तो शैलो क्लोन (या स्पार्स क्लोन) इतिहास को छोटा करके और/या ब्लॉब्स को छोड़कर अधिकांश डाउनलोड से बचने में मदद करता है।

#### त्वरित शैलो क्लोन — न्यूनतम इतिहास, सभी फाइलें

नीचे दिए गए कमांड में `<your-username>` को अपने फोर्क URL (या यदि आप चाहें तो अपस्ट्रीम URL) से बदलें।

केवल नवीनतम कमिट इतिहास को क्लोन करने के लिए (छोटा डाउनलोड):

```bash|powershell
git clone --depth 1 https://github.com/<your-username>/ai-agents-for-beginners.git
```

किसी विशेष ब्रांच को क्लोन करने के लिए:

```bash|powershell
git clone --depth 1 --branch <branch-name> https://github.com/<your-username>/ai-agents-for-beginners.git
```

#### आंशिक (स्पार्स) क्लोन — न्यूनतम ब्लॉब्स + केवल चयनित फ़ोल्डर

यह आंशिक क्लोन और स्पार्स-चेकआउट का उपयोग करता है (Git 2.25+ की आवश्यकता है और आंशिक क्लोन समर्थन के साथ आधुनिक Git अनुशंसित है):

```bash|powershell
git clone --depth 1 --filter=blob:none --sparse https://github.com/<your-username>/ai-agents-for-beginners.git
```

रिपॉजिटरी फ़ोल्डर में जाएं:

bash के लिए:

```bash
cd ai-agents-for-beginners
```

Powershell के लिए:

```powershell
Set-Location ai-agents-for-beginners
```

फिर उन फ़ोल्डरों को निर्दिष्ट करें जिनकी आपको आवश्यकता है (नीचे उदाहरण में दो फ़ोल्डर दिखाए गए हैं):

```bash|powershell
git sparse-checkout set 00-course-setup 01-intro-to-ai-agents
```

क्लोन और फाइलों को सत्यापित करने के बाद, यदि आपको केवल फाइलों की आवश्यकता है और स्थान खाली करना चाहते हैं (कोई git इतिहास नहीं), तो कृपया रिपॉजिटरी मेटाडेटा को हटा दें (💀अपरिवर्तनीय — आप सभी Git कार्यक्षमता खो देंगे: कोई कमिट्स, पुल्स, पुशेस, या इतिहास एक्सेस नहीं)।

Linux/macOS के लिए:

```bash
rm -rf .git
```

Windows के लिए:

```powershell
Remove-Item -Recurse -Force .git
```

#### GitHub Codespaces का उपयोग करना (स्थानीय बड़े डाउनलोड से बचने के लिए अनुशंसित)

- [GitHub UI](https://github.com/codespaces) के माध्यम से इस रिपॉजिटरी के लिए एक नया Codespace बनाएं।  

- नए बनाए गए कोडस्पेस के टर्मिनल में, ऊपर दिए गए शैलो/स्पार्स क्लोन कमांड में से एक चलाएं ताकि केवल आवश्यक पाठ फ़ोल्डर को कोडस्पेस वर्कस्पेस में लाया जा सके।
- वैकल्पिक: कोडस्पेस में क्लोनिंग के बाद, अतिरिक्त स्थान पुनः प्राप्त करने के लिए .git को हटा दें (ऊपर दिए गए हटाने के कमांड देखें)।
- नोट: यदि आप कोडस्पेस में सीधे रिपॉजिटरी खोलना पसंद करते हैं (बिना अतिरिक्त क्लोन के), तो ध्यान दें कि कोडस्पेस डेवलपर कंटेनर वातावरण का निर्माण करेगा और संभवतः आपकी आवश्यकता से अधिक प्रावधान करेगा। एक ताजा कोडस्पेस के अंदर एक शैलो कॉपी क्लोन करना आपको डिस्क उपयोग पर अधिक नियंत्रण देता है।

#### सुझाव

- यदि आप संपादन/कमिट करना चाहते हैं, तो हमेशा क्लोन URL को अपने फोर्क से बदलें।
- यदि बाद में आपको अधिक इतिहास या फाइलों की आवश्यकता हो, तो आप उन्हें प्राप्त कर सकते हैं या स्पार्स-चेकआउट को समायोजित कर सकते हैं ताकि अतिरिक्त फ़ोल्डर शामिल किए जा सकें।

## कोड चलाना

यह कोर्स Jupyter Notebooks की एक श्रृंखला प्रदान करता है जिसे आप AI Agents बनाने का व्यावहारिक अनुभव प्राप्त करने के लिए चला सकते हैं।

कोड नमूने निम्नलिखित का उपयोग करते हैं:

**GitHub अकाउंट आवश्यक - मुफ्त**:

1) Semantic Kernel Agent Framework + GitHub Models Marketplace। लेबल किया गया (semantic-kernel.ipynb)
2) AutoGen Framework + GitHub Models Marketplace। लेबल किया गया (autogen.ipynb)

**Azure सदस्यता आवश्यक**:
3) Azure AI Foundry + Azure AI Agent Service। लेबल किया गया (azureaiagent.ipynb)

हम आपको तीनों प्रकार के उदाहरणों को आज़माने के लिए प्रोत्साहित करते हैं ताकि आप देख सकें कि आपके लिए कौन सा सबसे अच्छा काम करता है।

आप जो भी विकल्प चुनते हैं, वह नीचे दिए गए सेटअप चरणों को निर्धारित करेगा:

## आवश्यकताएँ

- Python 3.12+
  - **NOTE**: यदि आपके पास Python3.12 स्थापित नहीं है, तो सुनिश्चित करें कि आप इसे स्थापित करें। फिर requirements.txt फ़ाइल से सही संस्करण स्थापित करने के लिए python3.12 का उपयोग करके अपना venv बनाएं।
  
    >उदाहरण

    Python venv डायरेक्टरी बनाएं:

    ``` bash
    python3 -m venv venv
    ```

    फिर venv वातावरण को सक्रिय करें:

    macOS और Linux के लिए

    ```bash
    source venv/bin/activate
    ```
  
    Windows के लिए

    ```bash
    venv\Scripts\activate
    ```

- एक GitHub अकाउंट - GitHub Models Marketplace तक पहुंच के लिए
- Azure सदस्यता - Azure AI Foundry तक पहुंच के लिए
- Azure AI Foundry अकाउंट - Azure AI Agent Service तक पहुंच के लिए

हमने इस रिपॉजिटरी की रूट में एक `requirements.txt` फ़ाइल शामिल की है जिसमें कोड नमूनों को चलाने के लिए आवश्यक सभी Python पैकेज शामिल हैं।

आप इसे रिपॉजिटरी की रूट में अपने टर्मिनल में निम्नलिखित कमांड चलाकर स्थापित कर सकते हैं:

```bash
pip install -r requirements.txt
```
हम किसी भी संघर्ष और समस्याओं से बचने के लिए Python वर्चुअल वातावरण बनाने की सिफारिश करते हैं।

## VSCode सेटअप
सुनिश्चित करें कि आप VSCode में सही संस्करण का Python उपयोग कर रहे हैं।

![image](https://github.com/user-attachments/assets/a85e776c-2edb-4331-ae5b-6bfdfb98ee0e)

## GitHub Models का उपयोग करके नमूनों के लिए सेटअप 

### चरण 1: अपना GitHub व्यक्तिगत एक्सेस टोकन (PAT) प्राप्त करें

यह कोर्स GitHub Models Marketplace का उपयोग करता है, जो आपको बड़े भाषा मॉडल (LLMs) तक मुफ्त पहुंच प्रदान करता है, जिसे आप AI Agents बनाने के लिए उपयोग करेंगे।

GitHub Models का उपयोग करने के लिए, आपको एक [GitHub Personal Access Token](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens) बनाना होगा।

यह आपके GitHub अकाउंट में <a href="https://github.com/settings/personal-access-tokens" target="_blank">Personal Access Tokens settings</a> पर जाकर किया जा सकता है।

कृपया टोकन बनाते समय [Principle of Least Privilege](https://docs.github.com/en/get-started/learning-to-code/storing-your-secrets-safely) का पालन करें। इसका मतलब है कि आपको केवल टोकन को इस कोर्स के कोड नमूनों को चलाने के लिए आवश्यक अनुमतियाँ देनी चाहिए।

1. **Developer settings** पर जाकर स्क्रीन के बाईं ओर `Fine-grained tokens` विकल्प चुनें।
   ![](../../../translated_images/profile_developer_settings.410a859fe749c755c859d414294c5908e307222b2c61819c3203bbeed4470e25.hi.png)

    फिर `Generate new token` चुनें।

    ![Generate Token](../../../translated_images/fga_new_token.1c1a234afe202ab37483944a291ee80c1868e1e78082fd6bd4180fea5d5a15b4.hi.png)

2. अपने टोकन के लिए एक वर्णनात्मक नाम दर्ज करें जो इसके उद्देश्य को दर्शाता हो, ताकि बाद में इसे पहचानना आसान हो।

    🔐 टोकन अवधि अनुशंसा

    अनुशंसित अवधि: 30 दिन
    अधिक सुरक्षित दृष्टिकोण के लिए, आप छोटी अवधि चुन सकते हैं—जैसे 7 दिन 🛡️
    यह एक व्यक्तिगत लक्ष्य निर्धारित करने और कोर्स को पूरा करने का एक शानदार तरीका है जब आपकी सीखने की गति उच्च हो 🚀।

    ![Token Name and Expiration](../../../translated_images/token-name-expiry-date.a095fb0de63868640a4c82d6b1bbc92b482930a663917a5983a3c7cd1ef86b77.hi.png)

3. टोकन के दायरे को इस रिपॉजिटरी के फोर्क तक सीमित करें।

    ![Limit scope to fork repository](../../../translated_images/token_repository_limit.924ade5e11d9d8bb6cd21293987e4579dea860e2ba66d607fb46e49524d53644.hi.png)

4. टोकन की अनुमतियों को प्रतिबंधित करें: **Permissions** के तहत, **Account** टैब पर क्लिक करें, और "+ Add permissions" बटन पर क्लिक करें। एक ड्रॉपडाउन दिखाई देगा। कृपया **Models** खोजें और इसके बॉक्स को चेक करें।
    ![Add Models Permission](../../../translated_images/add_models_permissions.c0c44ed8b40fc143dc87792da9097d715b7de938354e8f771d65416ecc7816b8.hi.png)

5. टोकन बनाने से पहले आवश्यक अनुमतियों को सत्यापित करें। ![Verify Permissions](../../../translated_images/verify_permissions.06bd9e43987a8b219f171bbcf519e45ababae35b844f5e9757e10afcb619b936.hi.png)

6. टोकन बनाने से पहले सुनिश्चित करें कि आप इसे सुरक्षित स्थान जैसे पासवर्ड मैनेजर वॉल्ट में संग्रहीत करने के लिए तैयार हैं, क्योंकि इसे बनाने के बाद फिर से नहीं दिखाया जाएगा। ![Store Token Securely](../../../translated_images/store_token_securely.08ee2274c6ad6caf3482f1cd1bad7ca3fdca1ce737bc485bfa6499c84297c789.hi.png)

अपने नए बनाए गए टोकन को कॉपी करें। अब आप इसे इस कोर्स में शामिल `.env` फ़ाइल में जोड़ेंगे।

### चरण 2: अपनी `.env` फ़ाइल बनाएं

अपनी `.env` फ़ाइल बनाने के लिए अपने टर्मिनल में निम्नलिखित कमांड चलाएं।

```bash
cp .env.example .env
```

यह उदाहरण फ़ाइल को कॉपी करेगा और आपकी डायरेक्टरी में एक `.env` बनाएगा, जहां आप पर्यावरण चर के लिए मान भर सकते हैं।

अपने टोकन को कॉपी करके, अपनी पसंदीदा टेक्स्ट एडिटर में `.env` फ़ाइल खोलें और अपने टोकन को `GITHUB_TOKEN` फ़ील्ड में पेस्ट करें।
![GitHub Token Field](../../../translated_images/github_token_field.20491ed3224b5f4ab24d10ced7a68c4aba2948fe8999cfc8675edaa16f5e5681.hi.png)

अब आप इस कोर्स के कोड नमूनों को चलाने में सक्षम होंगे।

## Azure AI Foundry और Azure AI Agent Service का उपयोग करके नमूनों के लिए सेटअप

### चरण 1: अपना Azure प्रोजेक्ट एंडपॉइंट प्राप्त करें

Azure AI Foundry में हब और प्रोजेक्ट बनाने के चरणों का पालन करें: [Hub resources overview](https://learn.microsoft.com/en-us/azure/ai-foundry/concepts/ai-resources)

एक बार जब आप अपना प्रोजेक्ट बना लेते हैं, तो आपको अपने प्रोजेक्ट के लिए कनेक्शन स्ट्रिंग प्राप्त करनी होगी।

यह Azure AI Foundry पोर्टल में अपने प्रोजेक्ट के **Overview** पेज पर जाकर किया जा सकता है।

![Project Connection String](../../../translated_images/project-endpoint.8cf04c9975bbfbf18f6447a599550edb052e52264fb7124d04a12e6175e330a5.hi.png)

### चरण 2: अपनी `.env` फ़ाइल बनाएं

अपनी `.env` फ़ाइल बनाने के लिए अपने टर्मिनल में निम्नलिखित कमांड चलाएं।

```bash
cp .env.example .env
```

यह उदाहरण फ़ाइल को कॉपी करेगा और आपकी डायरेक्टरी में एक `.env` बनाएगा, जहां आप पर्यावरण चर के लिए मान भर सकते हैं।

अपने टोकन को कॉपी करके, अपनी पसंदीदा टेक्स्ट एडिटर में `.env` फ़ाइल खोलें और अपने टोकन को `PROJECT_ENDPOINT` फ़ील्ड में पेस्ट करें।

### चरण 3: Azure में साइन इन करें

सुरक्षा के सर्वोत्तम अभ्यास के रूप में, हम [keyless authentication](https://learn.microsoft.com/azure/developer/ai/keyless-connections?tabs=csharp%2Cazure-cli?WT.mc_id=academic-105485-koreyst) का उपयोग करेंगे ताकि Microsoft Entra ID के साथ Azure OpenAI में प्रमाणित हो सकें।

इसके बाद, एक टर्मिनल खोलें और `az login --use-device-code` चलाकर अपने Azure अकाउंट में साइन इन करें।

एक बार जब आप लॉग इन कर लें, तो टर्मिनल में अपनी सदस्यता चुनें।

## अतिरिक्त पर्यावरण चर - Azure Search और Azure OpenAI 

Agentic RAG पाठ - पाठ 5 - के लिए कुछ नमूने हैं जो Azure Search और Azure OpenAI का उपयोग करते हैं।

यदि आप इन नमूनों को चलाना चाहते हैं, तो आपको अपनी `.env` फ़ाइल में निम्नलिखित पर्यावरण चर जोड़ने की आवश्यकता होगी:

### Overview Page (Project)

- `AZURE_SUBSCRIPTION_ID` - अपने प्रोजेक्ट के **Overview** पेज पर **Project details** देखें।

- `AZURE_AI_PROJECT_NAME` - अपने प्रोजेक्ट के **Overview** पेज के शीर्ष पर देखें।

- `AZURE_OPENAI_SERVICE` - **Overview** पेज पर **Azure OpenAI Service** के लिए **Included capabilities** टैब में इसे खोजें।

### Management Center

- `AZURE_OPENAI_RESOURCE_GROUP` - **Management Center** के **Overview** पेज पर **Project properties** पर जाएं।

- `GLOBAL_LLM_SERVICE` - **Connected resources** के तहत, **Azure AI Services** कनेक्शन नाम खोजें। यदि सूचीबद्ध नहीं है, तो अपने संसाधन समूह के तहत AI Services संसाधन नाम के लिए **Azure portal** की जांच करें।

### Models + Endpoints Page

- `AZURE_OPENAI_EMBEDDING_DEPLOYMENT_NAME` - अपना एम्बेडिंग मॉडल चुनें (जैसे, `text-embedding-ada-002`) और मॉडल विवरण से **Deployment name** नोट करें।

- `AZURE_OPENAI_CHAT_DEPLOYMENT_NAME` - अपना चैट मॉडल चुनें (जैसे, `gpt-4o-mini`) और मॉडल विवरण से **Deployment name** नोट करें।

### Azure Portal

- `AZURE_OPENAI_ENDPOINT` - **Azure AI services** देखें, उस पर क्लिक करें, फिर **Resource Management**, **Keys and Endpoint** पर जाएं, "Azure OpenAI endpoints" तक स्क्रॉल करें, और वह कॉपी करें जो "Language APIs" कहता है।

- `AZURE_OPENAI_API_KEY` - उसी स्क्रीन से, KEY 1 या KEY 2 कॉपी करें।

- `AZURE_SEARCH_SERVICE_ENDPOINT` - अपने **Azure AI Search** संसाधन को खोजें, उस पर क्लिक करें, और **Overview** देखें।

- `AZURE_SEARCH_API_KEY` - फिर **Settings** और **Keys** पर जाएं और प्राथमिक या द्वितीयक एडमिन कुंजी कॉपी करें।

### External Webpage

- `AZURE_OPENAI_API_VERSION` - [API version lifecycle](https://learn.microsoft.com/en-us/azure/ai-services/openai/api-version-deprecation#latest-ga-api-release) पेज पर **Latest GA API release** के तहत देखें।

### Keyless Authentication सेटअप

अपने क्रेडेंशियल्स को हार्डकोड करने के बजाय, हम Azure OpenAI के साथ keyless कनेक्शन का उपयोग करेंगे। ऐसा करने के लिए, हम `DefaultAzureCredential` को इम्पोर्ट करेंगे और बाद में `DefaultAzureCredential` फ़ंक्शन को कॉल करेंगे ताकि क्रेडेंशियल प्राप्त किया जा सके।

```python
from azure.identity import DefaultAzureCredential, InteractiveBrowserCredential
```

## कहीं अटक गए?


यदि आपको इस सेटअप को चलाने में कोई समस्या हो, तो हमारे <a href="https://discord.gg/kzRShWzttr" target="_blank">Azure AI Community Discord</a> में शामिल हों या <a href="https://github.com/microsoft/ai-agents-for-beginners/issues?WT.mc_id=academic-105485-koreyst" target="_blank">एक समस्या दर्ज करें</a>।

## अगला पाठ

अब आप इस पाठ्यक्रम के कोड को चलाने के लिए तैयार हैं। एआई एजेंट्स की दुनिया के बारे में और अधिक सीखने का आनंद लें!

[एआई एजेंट्स और उनके उपयोग मामलों का परिचय](../01-intro-to-ai-agents/README.md)

---

**अस्वीकरण**:  
यह दस्तावेज़ AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) का उपयोग करके अनुवादित किया गया है। जबकि हम सटीकता के लिए प्रयास करते हैं, कृपया ध्यान दें कि स्वचालित अनुवाद में त्रुटियां या अशुद्धियां हो सकती हैं। मूल भाषा में उपलब्ध मूल दस्तावेज़ को आधिकारिक स्रोत माना जाना चाहिए। महत्वपूर्ण जानकारी के लिए, पेशेवर मानव अनुवाद की सिफारिश की जाती है। इस अनुवाद के उपयोग से उत्पन्न किसी भी गलतफहमी या गलत व्याख्या के लिए हम उत्तरदायी नहीं हैं।