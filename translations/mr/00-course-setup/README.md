<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "96eb7f95375daa3e91778ca0295a55d9",
  "translation_date": "2025-10-15T11:42:40+00:00",
  "source_file": "00-course-setup/README.md",
  "language_code": "mr"
}
-->
# कोर्स सेटअप

## परिचय

या धड्यात आपण या कोर्सचे कोड नमुने कसे चालवायचे ते शिकणार आहोत.

## इतर शिकणाऱ्यांमध्ये सामील व्हा आणि मदत मिळवा

तुमचा रेपो क्लोन करण्यापूर्वी, [AI Agents For Beginners Discord channel](https://aka.ms/ai-agents/discord) मध्ये सामील व्हा. तुम्हाला सेटअपसाठी मदत, कोर्सबद्दल प्रश्न विचारायचे असतील किंवा इतर शिकणाऱ्यांशी संपर्क साधायचा असेल तर येथे मदत मिळेल.

## हा रेपो क्लोन किंवा फोर्क करा

सुरुवात करण्यासाठी, कृपया GitHub Repository क्लोन किंवा फोर्क करा. यामुळे तुम्हाला कोर्स मटेरियलची स्वतःची आवृत्ती मिळेल ज्यामुळे तुम्ही कोड चालवू, चाचणी करू आणि बदल करू शकाल!

हे करण्यासाठी <a href="https://github.com/microsoft/ai-agents-for-beginners/fork" target="_blank">रेपो फोर्क करण्यासाठी</a> लिंकवर क्लिक करा.

आता तुम्हाला या कोर्सची स्वतःची फोर्क केलेली आवृत्ती खालील लिंकवर मिळेल:

![Forked Repo](../../../translated_images/forked-repo.33f27ca1901baa6a5e13ec3eb1f0ddd3a44d936d91cc8cfb19bfdb9688bd2c3d.mr.png)

### शॅलो क्लोन (वर्कशॉप / कोडस्पेससाठी शिफारस केलेले)

  > संपूर्ण रेपो मोठा (~3 GB) असू शकतो जेव्हा तुम्ही संपूर्ण इतिहास आणि सर्व फाइल्स डाउनलोड करता. जर तुम्ही फक्त वर्कशॉपमध्ये सहभागी होत असाल किंवा तुम्हाला फक्त काही धड्यांच्या फोल्डर्सची आवश्यकता असेल, तर शॅलो क्लोन (किंवा स्पार्स क्लोन) बहुतेक डाउनलोड टाळतो.

#### जलद शॅलो क्लोन — किमान इतिहास, सर्व फाइल्स

खालील कमांड्समध्ये `<your-username>` ला तुमच्या फोर्क URL ने बदला (किंवा तुम्हाला हवे असल्यास अपस्ट्रीम URL).

फक्त नवीनतम कमिट इतिहास क्लोन करण्यासाठी (लहान डाउनलोड):

```bash|powershell
git clone --depth 1 https://github.com/<your-username>/ai-agents-for-beginners.git
```

विशिष्ट ब्रँच क्लोन करण्यासाठी:

```bash|powershell
git clone --depth 1 --branch <branch-name> https://github.com/<your-username>/ai-agents-for-beginners.git
```

#### अंशतः (स्पार्स) क्लोन — किमान ब्लॉब्स + फक्त निवडलेले फोल्डर्स

हे अंशतः क्लोन आणि स्पार्स-चेकआउट वापरते (Git 2.25+ आवश्यक आहे आणि अंशतः क्लोन समर्थनासह आधुनिक Git शिफारस केली जाते):

```bash|powershell
git clone --depth 1 --filter=blob:none --sparse https://github.com/<your-username>/ai-agents-for-beginners.git
```

रेपो फोल्डरमध्ये जा:

बॅशसाठी:

```bash
cd ai-agents-for-beginners
```

पॉवरशेलसाठी:

```powershell
Set-Location ai-agents-for-beginners
```

त्यानंतर तुम्हाला हवे असलेले फोल्डर्स निर्दिष्ट करा (खालील उदाहरण दोन फोल्डर्स दर्शवते):

```bash|powershell
git sparse-checkout set 00-course-setup 01-intro-to-ai-agents
```

फाइल्स क्लोन आणि सत्यापित केल्यानंतर, जर तुम्हाला फक्त फाइल्सची आवश्यकता असेल आणि जागा मोकळी करायची असेल (कोणताही git इतिहास नाही), तर कृपया रेपो मेटाडेटा हटवा (💀अपरिवर्तनीय — तुम्ही सर्व Git कार्यक्षमता गमवाल: कोणतेही कमिट्स, पुल्स, पुशेस किंवा इतिहास प्रवेश).

Linux/macOS साठी:

```bash
rm -rf .git
```

Windows साठी:

```powershell
Remove-Item -Recurse -Force .git
```

#### GitHub Codespaces वापरणे (स्थानिक मोठ्या डाउनलोड्स टाळण्यासाठी शिफारस केलेले)

- [GitHub UI](https://github.com/codespaces) द्वारे या रेपोसाठी नवीन Codespace तयार करा.  

- नवीन तयार केलेल्या कोडस्पेसच्या टर्मिनलमध्ये, वर दिलेल्या शॅलो/स्पार्स क्लोन कमांड्स चालवा जेणेकरून तुम्हाला फक्त आवश्यक धड्यांचे फोल्डर्स कोडस्पेस वर्कस्पेसमध्ये मिळतील.
- पर्यायी: कोडस्पेसमध्ये क्लोन केल्यानंतर, अतिरिक्त जागा रिकामी करण्यासाठी .git काढा (वरील काढण्याच्या कमांड्स पहा).
- टीप: जर तुम्हाला रेपो थेट कोडस्पेसमध्ये उघडायचा असेल (अतिरिक्त क्लोनशिवाय), लक्षात ठेवा कोडस्पेस डेव्हकंटेनर वातावरण तयार करेल आणि कदाचित तुम्हाला आवश्यकतेपेक्षा अधिक प्रोव्हिजन करू शकते. नवीन कोडस्पेसमध्ये शॅलो कॉपी क्लोन करणे तुम्हाला डिस्क वापरावर अधिक नियंत्रण देते.

#### टिप्स

- जर तुम्हाला संपादित/कमिट करायचे असेल तर नेहमी क्लोन URL तुमच्या फोर्कने बदला.
- जर तुम्हाला नंतर अधिक इतिहास किंवा फाइल्सची आवश्यकता असेल, तर तुम्ही त्यांना फेच करू शकता किंवा स्पार्स-चेकआउट समायोजित करून अतिरिक्त फोल्डर्स समाविष्ट करू शकता.

## कोड चालवणे

हा कोर्स Jupyter Notebooks ची मालिका ऑफर करतो ज्याद्वारे तुम्ही AI Agents तयार करण्याचा प्रत्यक्ष अनुभव घेऊ शकता.

कोड नमुने खालीलप्रमाणे वापरतात:

**GitHub खाते आवश्यक - मोफत**:

1) Semantic Kernel Agent Framework + GitHub Models Marketplace. (semantic-kernel.ipynb) म्हणून लेबल केलेले
2) AutoGen Framework + GitHub Models Marketplace. (autogen.ipynb) म्हणून लेबल केलेले

**Azure सदस्यता आवश्यक**:
3) Azure AI Foundry + Azure AI Agent Service. (azureaiagent.ipynb) म्हणून लेबल केलेले

आम्ही तुम्हाला तीन प्रकारचे उदाहरणे वापरून पाहण्याची शिफारस करतो जेणेकरून तुमच्यासाठी कोणता सर्वोत्तम कार्य करतो ते पाहता येईल.

तुम्ही कोणताही पर्याय निवडला तरी, खाली दिलेल्या सेटअप चरणांचे अनुसरण करणे आवश्यक आहे:

## आवश्यकताः

- Python 3.12+
  - **टीप**: जर तुमच्याकडे Python3.12 स्थापित नसेल, तर ते स्थापित करा. नंतर requirements.txt फाइलमधून योग्य आवृत्त्या स्थापित करण्यासाठी python3.12 वापरून तुमचा venv तयार करा.
  
    >उदाहरण

    Python venv डिरेक्टरी तयार करा:

    ``` bash
    python3 -m venv venv
    ```

    नंतर venv वातावरण सक्रिय करा:

    macOS आणि Linux साठी

    ```bash
    source venv/bin/activate
    ```
  
    Windows साठी

    ```bash
    venv\Scripts\activate
    ```

- GitHub खाते - GitHub Models Marketplace मध्ये प्रवेशासाठी
- Azure सदस्यता - Azure AI Foundry मध्ये प्रवेशासाठी
- Azure AI Foundry खाते - Azure AI Agent Service मध्ये प्रवेशासाठी

आम्ही या रेपोच्या मूळ फोल्डरमध्ये एक `requirements.txt` फाइल समाविष्ट केली आहे ज्यामध्ये कोड नमुने चालवण्यासाठी आवश्यक असलेल्या सर्व Python पॅकेजेस आहेत.

तुम्ही ती फाइल रेपोच्या मूळ फोल्डरमध्ये खालील कमांड चालवून स्थापित करू शकता:

```bash
pip install -r requirements.txt
```

आम्ही कोणत्याही संघर्ष आणि समस्यांपासून बचाव करण्यासाठी Python व्हर्च्युअल वातावरण तयार करण्याची शिफारस करतो.

## VSCode सेटअप
VSCode मध्ये योग्य Python आवृत्ती वापरत असल्याची खात्री करा.

![image](https://github.com/user-attachments/assets/a85e776c-2edb-4331-ae5b-6bfdfb98ee0e)

## GitHub Models वापरून नमुन्यांसाठी सेटअप 

### चरण 1: तुमचा GitHub Personal Access Token (PAT) मिळवा

हा कोर्स GitHub Models Marketplace चा उपयोग करतो, ज्यामुळे तुम्हाला Large Language Models (LLMs) चा विनामूल्य प्रवेश मिळतो, ज्याचा उपयोग तुम्ही AI Agents तयार करण्यासाठी करू शकता.

GitHub Models वापरण्यासाठी, तुम्हाला [GitHub Personal Access Token](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens) तयार करावा लागेल.

हे तुमच्या GitHub खात्यातील <a href="https://github.com/settings/personal-access-tokens" target="_blank">Personal Access Tokens settings</a> वर जाऊन करता येईल.

कृपया तुमचा टोकन तयार करताना [Principle of Least Privilege](https://docs.github.com/en/get-started/learning-to-code/storing-your-secrets-safely) चे अनुसरण करा. याचा अर्थ असा की तुम्ही टोकनला फक्त कोर्समधील कोड नमुने चालवण्यासाठी आवश्यक असलेले परवानग्या द्याव्यात.

1. **Developer settings** मध्ये जाऊन डाव्या बाजूला `Fine-grained tokens` पर्याय निवडा.
   ![](../../../translated_images/profile_developer_settings.410a859fe749c755c859d414294c5908e307222b2c61819c3203bbeed4470e25.mr.png)

    नंतर `Generate new token` निवडा.

    ![Generate Token](../../../translated_images/fga_new_token.1c1a234afe202ab37483944a291ee80c1868e1e78082fd6bd4180fea5d5a15b4.mr.png)

2. टोकनसाठी त्याच्या उद्देशाचे प्रतिबिंबित करणारे वर्णनात्मक नाव प्रविष्ट करा, जे नंतर ओळखणे सोपे होईल.


    🔐 टोकन कालावधी शिफारस

    शिफारस केलेला कालावधी: 30 दिवस
    अधिक सुरक्षितता ठेवण्यासाठी, तुम्ही कमी कालावधी निवडू शकता—उदाहरणार्थ, 7 दिवस 🛡️
    हे वैयक्तिक लक्ष्य सेट करण्याचा आणि तुमच्या शिकण्याच्या गतीसह कोर्स पूर्ण करण्याचा एक उत्तम मार्ग आहे 🚀.

    ![Token Name and Expiration](../../../translated_images/token-name-expiry-date.a095fb0de63868640a4c82d6b1bbc92b482930a663917a5983a3c7cd1ef86b77.mr.png)

3. टोकनचा स्कोप तुमच्या रेपोच्या फोर्कपुरता मर्यादित ठेवा.

    ![Limit scope to fork repository](../../../translated_images/token_repository_limit.924ade5e11d9d8bb6cd21293987e4579dea860e2ba66d607fb46e49524d53644.mr.png)

4. टोकनच्या परवानग्या मर्यादित करा: **Permissions** अंतर्गत, **Account** टॅबवर क्लिक करा आणि "+ Add permissions" बटणावर क्लिक करा. एक ड्रॉपडाउन दिसेल. कृपया **Models** शोधा आणि त्यासाठी बॉक्स तपासा.
    ![Add Models Permission](../../../translated_images/add_models_permissions.c0c44ed8b40fc143dc87792da9097d715b7de938354e8f771d65416ecc7816b8.mr.png)

5. टोकन तयार करण्यापूर्वी आवश्यक परवानग्या सत्यापित करा. ![Verify Permissions](../../../translated_images/verify_permissions.06bd9e43987a8b219f171bbcf519e45ababae35b844f5e9757e10afcb619b936.mr.png)

6. टोकन तयार करण्यापूर्वी, तुम्ही टोकन सुरक्षित ठिकाणी जसे की पासवर्ड मॅनेजर वॉल्टमध्ये संग्रहित करण्यास तयार आहात याची खात्री करा, कारण ते तयार केल्यानंतर पुन्हा दर्शवले जाणार नाही. ![Store Token Securely](../../../translated_images/store_token_securely.08ee2274c6ad6caf3482f1cd1bad7ca3fdca1ce737bc485bfa6499c84297c789.mr.png)

तुम्ही नुकतेच तयार केलेले नवीन टोकन कॉपी करा. आता तुम्ही ते या कोर्समध्ये समाविष्ट केलेल्या `.env` फाइलमध्ये जोडाल.


### चरण 2: तुमची `.env` फाइल तयार करा

तुमची `.env` फाइल तयार करण्यासाठी तुमच्या टर्मिनलमध्ये खालील कमांड चालवा.

```bash
cp .env.example .env
```

हे उदाहरण फाइल कॉपी करेल आणि तुमच्या डिरेक्टरीमध्ये `.env` तयार करेल जिथे तुम्ही पर्यावरणीय व्हेरिएबल्ससाठी मूल्ये भरा.

तुमचा टोकन कॉपी करून, तुमच्या आवडत्या टेक्स्ट एडिटरमध्ये `.env` फाइल उघडा आणि तुमचा टोकन `GITHUB_TOKEN` फील्डमध्ये पेस्ट करा.
![GitHub Token Field](../../../translated_images/github_token_field.20491ed3224b5f4ab24d10ced7a68c4aba2948fe8999cfc8675edaa16f5e5681.mr.png)


आता तुम्ही या कोर्सचे कोड नमुने चालवू शकता.

## Azure AI Foundry आणि Azure AI Agent Service वापरून नमुन्यांसाठी सेटअप

### चरण 1: तुमचा Azure प्रोजेक्ट एंडपॉइंट मिळवा


Azure AI Foundry मध्ये हब आणि प्रोजेक्ट तयार करण्यासाठी चरणांचे अनुसरण करा: [Hub resources overview](https://learn.microsoft.com/en-us/azure/ai-foundry/concepts/ai-resources)


तुमचा प्रोजेक्ट तयार केल्यानंतर, तुम्हाला तुमच्या प्रोजेक्टसाठी कनेक्शन स्ट्रिंग मिळवणे आवश्यक आहे.

हे Azure AI Foundry पोर्टलमधील तुमच्या प्रोजेक्टच्या **Overview** पेजवर जाऊन करता येईल.

![Project Connection String](../../../translated_images/project-endpoint.8cf04c9975bbfbf18f6447a599550edb052e52264fb7124d04a12e6175e330a5.mr.png)

### चरण 2: तुमची `.env` फाइल तयार करा

तुमची `.env` फाइल तयार करण्यासाठी तुमच्या टर्मिनलमध्ये खालील कमांड चालवा.

```bash
cp .env.example .env
```

हे उदाहरण फाइल कॉपी करेल आणि तुमच्या डिरेक्टरीमध्ये `.env` तयार करेल जिथे तुम्ही पर्यावरणीय व्हेरिएबल्ससाठी मूल्ये भरा.

तुमचा टोकन कॉपी करून, तुमच्या आवडत्या टेक्स्ट एडिटरमध्ये `.env` फाइल उघडा आणि तुमचा टोकन `PROJECT_ENDPOINT` फील्डमध्ये पेस्ट करा.

### चरण 3: Azure मध्ये साइन इन करा

सुरक्षिततेच्या सर्वोत्तम पद्धती म्हणून, आपण Microsoft Entra ID सह Azure OpenAI मध्ये [keyless authentication](https://learn.microsoft.com/azure/developer/ai/keyless-connections?tabs=csharp%2Cazure-cli?WT.mc_id=academic-105485-koreyst) वापरू.

पुढे, टर्मिनल उघडा आणि `az login --use-device-code` चालवून तुमच्या Azure खात्यात साइन इन करा.

तुम्ही लॉग इन केल्यानंतर, टर्मिनलमध्ये तुमची सदस्यता निवडा.


## अतिरिक्त पर्यावरणीय व्हेरिएबल्स - Azure Search आणि Azure OpenAI 

Agentic RAG Lesson - Lesson 5 साठी - काही नमुने आहेत जे Azure Search आणि Azure OpenAI वापरतात.

जर तुम्हाला हे नमुने चालवायचे असतील, तर तुम्हाला तुमच्या `.env` फाइलमध्ये खालील पर्यावरणीय व्हेरिएबल्स जोडणे आवश्यक आहे:

### प्रोजेक्टचा आढावा पृष्ठ

- `AZURE_SUBSCRIPTION_ID` - तुमच्या प्रोजेक्टच्या **Overview** पृष्ठावरील **Project details** तपासा.

- `AZURE_AI_PROJECT_NAME` - तुमच्या प्रोजेक्टच्या **Overview** पृष्ठाच्या शीर्षस्थानी पहा.

- `AZURE_OPENAI_SERVICE` - **Overview** पृष्ठावरील **Azure OpenAI Service** साठी **Included capabilities** टॅबमध्ये हे शोधा.

### व्यवस्थापन केंद्र

- `AZURE_OPENAI_RESOURCE_GROUP` - **Management Center** च्या **Overview** पृष्ठावरील **Project properties** वर जा.

- `GLOBAL_LLM_SERVICE` - **Connected resources** अंतर्गत, **Azure AI Services** कनेक्शन नाव शोधा. जर सूचीबद्ध नसेल, तर **Azure portal** मध्ये तुमच्या रिसोर्स ग्रुप अंतर्गत AI Services रिसोर्स नाव तपासा.

### मॉडेल्स + एंडपॉइंट्स पृष्ठ

- `AZURE_OPENAI_EMBEDDING_DEPLOYMENT_NAME` - तुमचा एम्बेडिंग मॉडेल निवडा (उदा., `text-embedding-ada-002`) आणि मॉडेल तपशीलांमधून **Deployment name** लक्षात ठेवा.

- `AZURE_OPENAI_CHAT_DEPLOYMENT_NAME` - तुमचा चॅट मॉडेल निवडा (उदा., `gpt-4o-mini`) आणि मॉडेल तपशीलांमधून **Deployment name** लक्षात ठेवा.

### Azure पोर्टल

- `AZURE_OPENAI_ENDPOINT` - **Azure AI services** शोधा, त्यावर क्लिक करा, नंतर **Resource Management**, **Keys and Endpoint** वर जा, "Azure OpenAI endpoints" पर्यंत स्क्रोल करा आणि "Language APIs" म्हणणारा कॉपी करा.

- `AZURE_OPENAI_API_KEY` - त्याच स्क्रीनवरून, KEY 1 किंवा KEY 2 कॉपी करा.

- `AZURE_SEARCH_SERVICE_ENDPOINT` - तुमचा **Azure AI Search** रिसोर्स शोधा, त्यावर क्लिक करा आणि **Overview** पहा.

- `AZURE_SEARCH_API_KEY` - नंतर **Settings** वर जा आणि **Keys** वर जाऊन प्राथमिक किंवा दुय्यम प्रशासकीय की कॉपी करा.

### बाह्य वेबपृष्ठ

- `AZURE_OPENAI_API_VERSION` - [API version lifecycle](https://learn.microsoft.com/en-us/azure/ai-services/openai/api-version-deprecation#latest-ga-api-release) पृष्ठावर **Latest GA API release** अंतर्गत भेट द्या.

### Keyless Authentication सेटअप

तुमच्या क्रेडेन्शियल्स हार्डकोड करण्याऐवजी, आपण Azure OpenAI सह keyless कनेक्शन वापरू. असे करण्यासाठी, आपण `DefaultAzureCredential` आयात करू आणि नंतर `DefaultAzureCredential` फंक्शन कॉल करून क्रेडेन्शियल मिळवू.

```python
from azure.identity import DefaultAzureCredential, InteractiveBrowserCredential
```

## कुठे अडले आहात?
जर तुम्हाला हे सेटअप चालवताना काही समस्या आल्या, तर आमच्या <a href="https://discord.gg/kzRShWzttr" target="_blank">Azure AI Community Discord</a> मध्ये सामील व्हा किंवा <a href="https://github.com/microsoft/ai-agents-for-beginners/issues?WT.mc_id=academic-105485-koreyst" target="_blank">समस्या नोंदवा</a>.

## पुढचा धडा

आता तुम्ही या कोर्ससाठी कोड चालवण्यासाठी तयार आहात. AI एजंट्सच्या जगाबद्दल अधिक शिकण्याचा आनंद घ्या!

[AI एजंट्स आणि एजंट वापर प्रकरणांची ओळख](../01-intro-to-ai-agents/README.md)

---

**अस्वीकरण**:  
हा दस्तऐवज AI भाषांतर सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) वापरून भाषांतरित करण्यात आला आहे. आम्ही अचूकतेसाठी प्रयत्नशील असलो तरी, कृपयास लक्षात ठेवा की स्वयंचलित भाषांतरे त्रुटी किंवा अचूकतेच्या अभावाने युक्त असू शकतात. मूळ भाषेतील दस्तऐवज हा अधिकृत स्रोत मानला जावा. महत्त्वाच्या माहितीसाठी, व्यावसायिक मानवी भाषांतराची शिफारस केली जाते. या भाषांतराचा वापर करून उद्भवलेल्या कोणत्याही गैरसमज किंवा चुकीच्या अर्थासाठी आम्ही जबाबदार राहणार नाही.