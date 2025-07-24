<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "c6a79c8f2b56a80370ff7e447765524f",
  "translation_date": "2025-07-24T07:58:36+00:00",
  "source_file": "00-course-setup/README.md",
  "language_code": "hi"
}
-->
# कोर्स सेटअप

## परिचय

इस पाठ में आप सीखेंगे कि इस कोर्स के कोड सैंपल्स को कैसे चलाना है।

## इस रिपॉजिटरी को क्लोन या फोर्क करें

शुरू करने के लिए, कृपया GitHub रिपॉजिटरी को क्लोन या फोर्क करें। इससे आपके पास कोर्स सामग्री का अपना संस्करण होगा, जिसे आप चला सकते हैं, टेस्ट कर सकते हैं और संशोधित कर सकते हैं!

यह लिंक पर क्लिक करके किया जा सकता है:

आपके पास अब इस कोर्स का अपना फोर्क किया हुआ संस्करण निम्नलिखित लिंक में होना चाहिए:

![Forked Repo](../../../translated_images/forked-repo.33f27ca1901baa6a5e13ec3eb1f0ddd3a44d936d91cc8cfb19bfdb9688bd2c3d.hi.png)

## कोड चलाना

यह कोर्स Jupyter Notebooks की एक श्रृंखला प्रदान करता है, जिन्हें चलाकर आप AI एजेंट्स बनाने का व्यावहारिक अनुभव प्राप्त कर सकते हैं।

कोड सैंपल्स निम्नलिखित का उपयोग करते हैं:

**GitHub अकाउंट आवश्यक - मुफ्त**:

1) Semantic Kernel Agent Framework + GitHub Models Marketplace। इसे (semantic-kernel.ipynb) के रूप में लेबल किया गया है।
2) AutoGen Framework + GitHub Models Marketplace। इसे (autogen.ipynb) के रूप में लेबल किया गया है।

**Azure सब्सक्रिप्शन आवश्यक**:
3) Azure AI Foundry + Azure AI Agent Service। इसे (azureaiagent.ipynb) के रूप में लेबल किया गया है।

हम आपको तीनों प्रकार के उदाहरण आज़माने की सलाह देते हैं ताकि आप देख सकें कि आपके लिए कौन सा सबसे अच्छा काम करता है।

आप जो भी विकल्प चुनें, वह नीचे दिए गए सेटअप चरणों को निर्धारित करेगा:

## आवश्यकताएँ

- Python 3.12+
  - **NOTE**: यदि आपके पास Python 3.12 इंस्टॉल नहीं है, तो सुनिश्चित करें कि आप इसे इंस्टॉल करें। फिर `python3.12` का उपयोग करके अपना वर्चुअल एनवायरनमेंट बनाएं ताकि `requirements.txt` फ़ाइल से सही संस्करण इंस्टॉल हो सकें।
- GitHub अकाउंट - GitHub Models Marketplace तक पहुंच के लिए
- Azure सब्सक्रिप्शन - Azure AI Foundry तक पहुंच के लिए
- Azure AI Foundry अकाउंट - Azure AI Agent Service तक पहुंच के लिए

हमने इस रिपॉजिटरी की रूट डायरेक्टरी में एक `requirements.txt` फ़ाइल शामिल की है, जिसमें कोड सैंपल्स को चलाने के लिए आवश्यक सभी Python पैकेज शामिल हैं।

आप इसे निम्नलिखित कमांड को अपनी टर्मिनल में रूट डायरेक्टरी पर चलाकर इंस्टॉल कर सकते हैं:

```bash
pip install -r requirements.txt
```
हम किसी भी संघर्ष और समस्याओं से बचने के लिए एक Python वर्चुअल एनवायरनमेंट बनाने की सिफारिश करते हैं।

## VSCode सेटअप करें
सुनिश्चित करें कि आप VSCode में सही Python संस्करण का उपयोग कर रहे हैं।

![image](https://github.com/user-attachments/assets/a85e776c-2edb-4331-ae5b-6bfdfb98ee0e)

## GitHub Models का उपयोग करने वाले सैंपल्स के लिए सेटअप

### चरण 1: अपना GitHub Personal Access Token (PAT) प्राप्त करें

यह कोर्स GitHub Models Marketplace का उपयोग करता है, जो आपको बड़े भाषा मॉडल्स (LLMs) तक मुफ्त पहुंच प्रदान करता है, जिनका उपयोग आप AI एजेंट्स बनाने के लिए करेंगे।

GitHub Models का उपयोग करने के लिए, आपको एक [GitHub Personal Access Token](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens) बनाना होगा।

यह आपके GitHub अकाउंट में जाकर किया जा सकता है।

कृपया [Principle of Least Privilege](https://docs.github.com/en/get-started/learning-to-code/storing-your-secrets-safely) का पालन करें जब आप अपना टोकन बनाएं। इसका मतलब है कि आपको केवल वही अनुमतियाँ देनी चाहिए जो इस कोर्स के कोड सैंपल्स को चलाने के लिए आवश्यक हैं।

1. अपनी स्क्रीन के बाईं ओर `Fine-grained tokens` विकल्प चुनें।

    फिर `Generate new token` चुनें।

    ![Generate Token](../../../translated_images/generate-new-token.8772e24e8e2e067f2e6742500eaf68bb5c5f8999537bd79a040d2ecc09c7fdcb.hi.png)

1. अपने टोकन के लिए एक वर्णनात्मक नाम दर्ज करें जो इसके उद्देश्य को दर्शाता हो, ताकि इसे बाद में पहचानना आसान हो। एक समाप्ति तिथि सेट करें (अनुशंसित: 30 दिन; आप चाहें तो अधिक सुरक्षित दृष्टिकोण के लिए 7 दिन जैसी छोटी अवधि चुन सकते हैं।)

    ![Token Name and Expiration](../../../translated_images/token-name-expiry-date.a095fb0de63868640a4c82d6b1bbc92b482930a663917a5983a3c7cd1ef86b77.hi.png)

1. टोकन के स्कोप को इस रिपॉजिटरी के फोर्क तक सीमित करें।

    ![Limit scope to fork repository](../../../translated_images/select-fork-repository.4497f6bb05ccd6b474ed134493a815fc34f94f89db2b1630c494adff7b5b558a.hi.png)

1. टोकन की अनुमतियों को सीमित करें: **Permissions** के तहत, **Account Permissions** पर जाएं, **Models** पर जाएं और केवल GitHub Models के लिए आवश्यक पढ़ने की अनुमति सक्षम करें।

    ![Account Permissions](../../../translated_images/account-permissions.de1806fad33a72c6194d2688cf2c10f2adb9ff7a5c1041a2329cbef46bffbba0.hi.png)

    ![Models Read Access](../../../translated_images/models-read-access.c00bc44e28c40450a85542e19f8e8c68284c71861c076b7dbc078b4c7e51faa6.hi.png)

अपने नए बनाए गए टोकन को कॉपी करें। अब आप इसे इस कोर्स में शामिल `.env` फ़ाइल में जोड़ेंगे।

### चरण 2: अपनी `.env` फ़ाइल बनाएं

अपनी `.env` फ़ाइल बनाने के लिए, अपनी टर्मिनल में निम्नलिखित कमांड चलाएं:

```bash
cp .env.example .env
```

यह उदाहरण फ़ाइल को कॉपी करेगा और आपकी डायरेक्टरी में एक `.env` बनाएगा, जहाँ आप पर्यावरण वेरिएबल्स के लिए मान भर सकते हैं।

अपने टोकन को कॉपी करके, अपनी पसंदीदा टेक्स्ट एडिटर में `.env` फ़ाइल खोलें और अपने टोकन को `GITHUB_TOKEN` फ़ील्ड में पेस्ट करें।

अब आप इस कोर्स के कोड सैंपल्स को चला सकते हैं।

## Azure AI Foundry और Azure AI Agent Service का उपयोग करने वाले सैंपल्स के लिए सेटअप

### चरण 1: अपना Azure प्रोजेक्ट एंडपॉइंट प्राप्त करें

Azure AI Foundry में एक हब और प्रोजेक्ट बनाने के चरणों का पालन करें: [Hub resources overview](https://learn.microsoft.com/en-us/azure/ai-foundry/concepts/ai-resources)

एक बार जब आप अपना प्रोजेक्ट बना लें, तो आपको अपने प्रोजेक्ट के लिए कनेक्शन स्ट्रिंग प्राप्त करनी होगी।

यह Azure AI Foundry पोर्टल में आपके प्रोजेक्ट के **Overview** पेज पर जाकर किया जा सकता है।

![Project Connection String](../../../translated_images/project-endpoint.8cf04c9975bbfbf18f6447a599550edb052e52264fb7124d04a12e6175e330a5.hi.png)

### चरण 2: अपनी `.env` फ़ाइल बनाएं

अपनी `.env` फ़ाइल बनाने के लिए, अपनी टर्मिनल में निम्नलिखित कमांड चलाएं:

```bash
cp .env.example .env
```

यह उदाहरण फ़ाइल को कॉपी करेगा और आपकी डायरेक्टरी में एक `.env` बनाएगा, जहाँ आप पर्यावरण वेरिएबल्स के लिए मान भर सकते हैं।

अपने टोकन को कॉपी करके, अपनी पसंदीदा टेक्स्ट एडिटर में `.env` फ़ाइल खोलें और अपने टोकन को `PROJECT_ENDPOINT` फ़ील्ड में पेस्ट करें।

### चरण 3: Azure में साइन इन करें

सुरक्षा के सर्वोत्तम अभ्यास के रूप में, हम [keyless authentication](https://learn.microsoft.com/azure/developer/ai/keyless-connections?tabs=csharp%2Cazure-cli?WT.mc_id=academic-105485-koreyst) का उपयोग करेंगे ताकि Microsoft Entra ID के साथ Azure OpenAI में प्रमाणित हो सकें।

इसके बाद, एक टर्मिनल खोलें और `az login --use-device-code` चलाकर अपने Azure अकाउंट में साइन इन करें।

साइन इन करने के बाद, टर्मिनल में अपनी सब्सक्रिप्शन चुनें।

## अतिरिक्त पर्यावरण वेरिएबल्स - Azure Search और Azure OpenAI

Agentic RAG पाठ - पाठ 5 - के लिए, कुछ सैंपल्स Azure Search और Azure OpenAI का उपयोग करते हैं।

यदि आप इन सैंपल्स को चलाना चाहते हैं, तो आपको अपनी `.env` फ़ाइल में निम्नलिखित पर्यावरण वेरिएबल्स जोड़ने होंगे:

### Overview Page (Project)

- `AZURE_SUBSCRIPTION_ID` - अपने प्रोजेक्ट के **Overview** पेज पर **Project details** देखें।

- `AZURE_AI_PROJECT_NAME` - अपने प्रोजेक्ट के **Overview** पेज के शीर्ष पर देखें।

- `AZURE_OPENAI_SERVICE` - **Overview** पेज पर **Included capabilities** टैब में **Azure OpenAI Service** देखें।

### Management Center

- `AZURE_OPENAI_RESOURCE_GROUP` - **Management Center** के **Overview** पेज पर **Project properties** पर जाएं।

- `GLOBAL_LLM_SERVICE` - **Connected resources** के तहत, **Azure AI Services** कनेक्शन नाम देखें। यदि सूचीबद्ध नहीं है, तो अपने संसाधन समूह के तहत Azure पोर्टल में AI Services संसाधन नाम देखें।

### Models + Endpoints Page

- `AZURE_OPENAI_EMBEDDING_DEPLOYMENT_NAME` - अपना एम्बेडिंग मॉडल चुनें (जैसे, `text-embedding-ada-002`) और मॉडल विवरण से **Deployment name** नोट करें।

- `AZURE_OPENAI_CHAT_DEPLOYMENT_NAME` - अपना चैट मॉडल चुनें (जैसे, `gpt-4o-mini`) और मॉडल विवरण से **Deployment name** नोट करें।

### Azure Portal

- `AZURE_OPENAI_ENDPOINT` - **Azure AI services** देखें, उस पर क्लिक करें, फिर **Resource Management**, **Keys and Endpoint** पर जाएं, "Azure OpenAI endpoints" तक स्क्रॉल करें, और "Language APIs" वाले को कॉपी करें।

- `AZURE_OPENAI_API_KEY` - उसी स्क्रीन से, KEY 1 या KEY 2 कॉपी करें।

- `AZURE_SEARCH_SERVICE_ENDPOINT` - अपने **Azure AI Search** संसाधन को खोजें, उस पर क्लिक करें, और **Overview** देखें।

- `AZURE_SEARCH_API_KEY` - फिर **Settings** और फिर **Keys** पर जाएं और प्राथमिक या द्वितीयक एडमिन कुंजी कॉपी करें।

### External Webpage

- `AZURE_OPENAI_API_VERSION` - [API version lifecycle](https://learn.microsoft.com/en-us/azure/ai-services/openai/api-version-deprecation#latest-ga-api-release) पेज पर **Latest GA API release** देखें।

### Keyless Authentication सेटअप करें

अपने क्रेडेंशियल्स को हार्डकोड करने के बजाय, हम Azure OpenAI के साथ एक keyless कनेक्शन का उपयोग करेंगे। ऐसा करने के लिए, हम `DefaultAzureCredential` को इंपोर्ट करेंगे और बाद में `DefaultAzureCredential` फ़ंक्शन को कॉल करेंगे ताकि क्रेडेंशियल प्राप्त हो सके।

```python
from azure.identity import DefaultAzureCredential, InteractiveBrowserCredential
```

## कहीं अटक गए?

यदि आपको इस सेटअप को चलाने में कोई समस्या हो रही है, तो हमारे 

## अगला पाठ

अब आप इस कोर्स के कोड को चलाने के लिए तैयार हैं। AI एजेंट्स की दुनिया के बारे में और अधिक सीखने का आनंद लें!

[AI एजेंट्स और उनके उपयोग के मामलों का परिचय](../01-intro-to-ai-agents/README.md)

**अस्वीकरण**:  
यह दस्तावेज़ AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) का उपयोग करके अनुवादित किया गया है। जबकि हम सटीकता सुनिश्चित करने का प्रयास करते हैं, कृपया ध्यान दें कि स्वचालित अनुवाद में त्रुटियां या अशुद्धियां हो सकती हैं। मूल भाषा में उपलब्ध मूल दस्तावेज़ को आधिकारिक स्रोत माना जाना चाहिए। महत्वपूर्ण जानकारी के लिए, पेशेवर मानव अनुवाद की सिफारिश की जाती है। इस अनुवाद के उपयोग से उत्पन्न किसी भी गलतफहमी या गलत व्याख्या के लिए हम उत्तरदायी नहीं हैं।