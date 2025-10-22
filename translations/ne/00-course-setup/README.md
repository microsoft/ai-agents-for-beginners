<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "96eb7f95375daa3e91778ca0295a55d9",
  "translation_date": "2025-10-15T08:35:13+00:00",
  "source_file": "00-course-setup/README.md",
  "language_code": "ne"
}
-->
# कोर्स सेटअप

## परिचय

यो पाठले यस कोर्सका कोड नमूनाहरू कसरी चलाउने भन्ने बारेमा चर्चा गर्नेछ।

## अन्य सिक्नेहरूमा सामेल हुनुहोस् र सहयोग प्राप्त गर्नुहोस्

तपाईंको रिपोजिटरी क्लोन गर्न सुरु गर्नु अघि, [AI Agents For Beginners Discord च्यानल](https://aka.ms/ai-agents/discord) मा सामेल हुनुहोस्। यहाँ तपाईं सेटअपमा सहयोग प्राप्त गर्न, कोर्सका बारेमा कुनै प्रश्न सोध्न, वा अन्य सिक्नेहरूसँग जडान गर्न सक्नुहुन्छ।

## यो रिपोजिटरी क्लोन वा फोर्क गर्नुहोस्

सुरु गर्नको लागि, कृपया GitHub रिपोजिटरी क्लोन वा फोर्क गर्नुहोस्। यसले तपाईंलाई कोर्स सामग्रीको आफ्नै संस्करण बनाउनेछ ताकि तपाईं कोड चलाउन, परीक्षण गर्न, र परिमार्जन गर्न सक्नुहुन्छ!

यो गर्नको लागि <a href="https://github.com/microsoft/ai-agents-for-beginners/fork" target="_blank">रिपोजिटरी फोर्क गर्नुहोस्</a> लिंकमा क्लिक गर्नुहोस्।

अब तपाईंको कोर्सको फोर्क गरिएको संस्करण निम्न लिंकमा उपलब्ध हुनेछ:

![Forked Repo](../../../translated_images/forked-repo.33f27ca1901baa6a5e13ec3eb1f0ddd3a44d936d91cc8cfb19bfdb9688bd2c3d.ne.png)

### शालो क्लोन (वर्कशप / Codespaces का लागि सिफारिस गरिएको)

  >पूर्ण रिपोजिटरी ठूलो (~3 GB) हुन सक्छ जब तपाईं सम्पूर्ण इतिहास र सबै फाइलहरू डाउनलोड गर्नुहुन्छ। यदि तपाईं केवल वर्कशपमा भाग लिँदै हुनुहुन्छ वा केवल केही पाठ फोल्डरहरू चाहिन्छ भने, शालो क्लोन (वा स्पार्स क्लोन) ले अधिकांश डाउनलोडलाई रोक्छ।

#### छिटो शालो क्लोन — न्यूनतम इतिहास, सबै फाइलहरू

तलका आदेशहरूमा `<your-username>` लाई तपाईंको फोर्क URL (वा अपस्ट्रीम URL यदि तपाईंलाई मनपर्छ भने) सँग बदल्नुहोस्।

केवल पछिल्लो कमिट इतिहास क्लोन गर्न (सानो डाउनलोड):

```bash|powershell
git clone --depth 1 https://github.com/<your-username>/ai-agents-for-beginners.git
```

विशिष्ट ब्रान्च क्लोन गर्न:

```bash|powershell
git clone --depth 1 --branch <branch-name> https://github.com/<your-username>/ai-agents-for-beginners.git
```

#### आंशिक (स्पार्स) क्लोन — न्यूनतम ब्लब्स + केवल चयनित फोल्डरहरू

यसले आंशिक क्लोन र स्पार्स-चेकआउट प्रयोग गर्दछ (Git 2.25+ र आंशिक क्लोन समर्थनको साथ आधुनिक Git सिफारिस गरिन्छ):

```bash|powershell
git clone --depth 1 --filter=blob:none --sparse https://github.com/<your-username>/ai-agents-for-beginners.git
```

रिपोजिटरी फोल्डरमा जानुहोस्:

bash का लागि:

```bash
cd ai-agents-for-beginners
```

Powershell का लागि:

```powershell
Set-Location ai-agents-for-beginners
```

त्यसपछि तपाईंले कुन फोल्डरहरू चाहिन्छ भनेर निर्दिष्ट गर्नुहोस् (तलको उदाहरणले दुई फोल्डरहरू देखाउँछ):

```bash|powershell
git sparse-checkout set 00-course-setup 01-intro-to-ai-agents
```

क्लोन र फाइलहरू प्रमाणित गरेपछि, यदि तपाईंलाई केवल फाइलहरू चाहिन्छ र ठाउँ खाली गर्न चाहनुहुन्छ भने (कुनै git इतिहास छैन), कृपया रिपोजिटरी मेटाडेटा मेटाउनुहोस् (💀अपरिवर्तनीय — तपाईं सबै Git कार्यक्षमता गुमाउनुहुनेछ: कुनै कमिट्स, पुल्स, पुशहरू, वा इतिहास पहुँच छैन)।

Linux/macOS का लागि:

```bash
rm -rf .git
```

Windows का लागि:

```powershell
Remove-Item -Recurse -Force .git
```

#### GitHub Codespaces प्रयोग गर्दै (स्थानीय ठूलो डाउनलोडहरू रोक्न सिफारिस गरिएको)

- [GitHub UI](https://github.com/codespaces) मार्फत यस रिपोजिटरीको लागि नयाँ Codespace सिर्जना गर्नुहोस्।  

- नयाँ सिर्जित Codespace को टर्मिनलमा, माथि उल्लेखित शालो/स्पार्स क्लोन आदेशहरू चलाउनुहोस् ताकि तपाईंलाई आवश्यक पाठ फोल्डरहरू Codespace कार्यक्षेत्रमा ल्याउन सक्नुहुन्छ।
- वैकल्पिक: Codespaces भित्र क्लोन गरेपछि, अतिरिक्त ठाउँ पुनः प्राप्त गर्न .git हटाउनुहोस् (मेटाउने आदेशहरू माथि हेर्नुहोस्)।
- नोट: यदि तपाईंलाई रिपोजिटरीलाई सीधा Codespaces मा खोल्न मनपर्छ भने (अतिरिक्त क्लोन बिना), ध्यान दिनुहोस् कि Codespaces ले devcontainer वातावरण निर्माण गर्नेछ र अझै पनि तपाईंलाई आवश्यक भन्दा बढी प्रावधान गर्न सक्छ। नयाँ Codespace भित्र शालो प्रतिलिपि क्लोन गर्नुले तपाईंलाई डिस्क प्रयोगमा बढी नियन्त्रण दिन्छ।

#### सुझावहरू

- यदि तपाईं सम्पादन/कमिट गर्न चाहनुहुन्छ भने सधैं क्लोन URL लाई तपाईंको फोर्कसँग बदल्नुहोस्।
- यदि तपाईंलाई पछि थप इतिहास वा फाइलहरू चाहिन्छ भने, तपाईं तिनीहरूलाई फेच गर्न वा स्पार्स-चेकआउट समायोजन गर्न सक्नुहुन्छ।

## कोड चलाउने

यो कोर्सले Jupyter Notebooks को एक श्रृंखला प्रदान गर्दछ जसले तपाईंलाई AI एजेन्टहरू निर्माण गर्न व्यावहारिक अनुभव प्राप्त गर्न अनुमति दिन्छ।

कोड नमूनाहरू निम्न प्रयोग गर्दछ:

**GitHub खाता आवश्यक - निःशुल्क**:

1) Semantic Kernel Agent Framework + GitHub Models Marketplace। (semantic-kernel.ipynb) लेबल गरिएको।
2) AutoGen Framework + GitHub Models Marketplace। (autogen.ipynb) लेबल गरिएको।

**Azure सदस्यता आवश्यक**:
3) Azure AI Foundry + Azure AI Agent Service। (azureaiagent.ipynb) लेबल गरिएको।

हामी तपाईंलाई तीन प्रकारका उदाहरणहरू प्रयास गर्न प्रोत्साहित गर्दछौं ताकि कुन तपाईंको लागि उत्तम काम गर्दछ भनेर थाहा पाउन सक्नुहुन्छ।

तपाईंले जुन विकल्प चयन गर्नुहुन्छ, त्यसले तलका सेटअप चरणहरू निर्धारण गर्नेछ:

## आवश्यकताहरू

- Python 3.12+
  - **NOTE**: यदि तपाईंले Python3.12 स्थापना गर्नुभएको छैन भने, सुनिश्चित गर्नुहोस् कि तपाईंले यसलाई स्थापना गर्नुभएको छ। त्यसपछि requirements.txt फाइलबाट सही संस्करणहरू स्थापना गर्न python3.12 प्रयोग गरेर आफ्नो venv सिर्जना गर्नुहोस्।
  
    >उदाहरण

    Python venv डाइरेक्टरी सिर्जना गर्नुहोस्:

    ``` bash
    python3 -m venv venv
    ```

    त्यसपछि venv वातावरण सक्रिय गर्नुहोस्:

    macOS र Linux का लागि

    ```bash
    source venv/bin/activate
    ```
  
    Windows का लागि

    ```bash
    venv\Scripts\activate
    ```

- GitHub खाता - GitHub Models Marketplace पहुँचको लागि
- Azure सदस्यता - Azure AI Foundry पहुँचको लागि
- Azure AI Foundry खाता - Azure AI Agent Service पहुँचको लागि

हामीले यस रिपोजिटरीको मूलमा `requirements.txt` फाइल समावेश गरेका छौं जसमा कोड नमूनाहरू चलाउन आवश्यक सबै Python प्याकेजहरू समावेश छन्।

तपाईं यसलाई निम्न आदेश चलाएर स्थापना गर्न सक्नुहुन्छ:

```bash
pip install -r requirements.txt
```

हामी कुनै पनि द्वन्द्व र समस्याहरूबाट बच्न Python भर्चुअल वातावरण सिर्जना गर्न सिफारिस गर्दछौं।

## VSCode सेटअप
सुनिश्चित गर्नुहोस् कि तपाईं VSCode मा सही संस्करणको Python प्रयोग गर्दै हुनुहुन्छ।

![image](https://github.com/user-attachments/assets/a85e776c-2edb-4331-ae5b-6bfdfb98ee0e)

## GitHub Models प्रयोग गरेर नमूनाहरूको सेटअप 

### चरण 1: तपाईंको GitHub व्यक्तिगत पहुँच टोकन (PAT) प्राप्त गर्नुहोस्

यो कोर्सले GitHub Models Marketplace प्रयोग गर्दछ, जसले तपाईंलाई AI एजेन्टहरू निर्माण गर्न प्रयोग गरिने Large Language Models (LLMs) को निःशुल्क पहुँच प्रदान गर्दछ।

GitHub Models प्रयोग गर्नको लागि, तपाईंले [GitHub Personal Access Token](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens) सिर्जना गर्न आवश्यक छ।

यो तपाईंको GitHub खाताको <a href="https://github.com/settings/personal-access-tokens" target="_blank">Personal Access Tokens settings</a> मा गएर गर्न सकिन्छ।

कृपया टोकन सिर्जना गर्दा [Principle of Least Privilege](https://docs.github.com/en/get-started/learning-to-code/storing-your-secrets-safely) पालना गर्नुहोस्। यसको मतलब तपाईंले टोकनलाई यस कोर्सका कोड नमूनाहरू चलाउन आवश्यक अनुमतिहरू मात्र दिनुपर्छ।

1. **Developer settings** मा गएर स्क्रिनको बायाँपट्टि रहेको `Fine-grained tokens` विकल्प चयन गर्नुहोस्।
   ![](../../../translated_images/profile_developer_settings.410a859fe749c755c859d414294c5908e307222b2c61819c3203bbeed4470e25.ne.png)

    त्यसपछि `Generate new token` चयन गर्नुहोस्।

    ![Generate Token](../../../translated_images/fga_new_token.1c1a234afe202ab37483944a291ee80c1868e1e78082fd6bd4180fea5d5a15b4.ne.png)

2. टोकनको उद्देश्यलाई प्रतिबिम्बित गर्ने वर्णनात्मक नाम प्रविष्ट गर्नुहोस् ताकि पछि सजिलै चिन्ह लगाउन सकियोस्।

    🔐 टोकन अवधि सिफारिस

    सिफारिस गरिएको अवधि: ३० दिन
    अधिक सुरक्षित स्थिति प्राप्त गर्न, तपाईं छोटो अवधि चयन गर्न सक्नुहुन्छ—जस्तै ७ दिन 🛡️
    यो व्यक्तिगत लक्ष्य सेट गर्न र कोर्स पूरा गर्नको लागि राम्रो तरिका हो जब तपाईंको सिक्ने गति उच्च छ 🚀।

    ![Token Name and Expiration](../../../translated_images/token-name-expiry-date.a095fb0de63868640a4c82d6b1bbc92b482930a663917a5983a3c7cd1ef86b77.ne.png)

3. टोकनको स्कोपलाई यस रिपोजिटरीको फोर्कमा सीमित गर्नुहोस्।

    ![Limit scope to fork repository](../../../translated_images/token_repository_limit.924ade5e11d9d8bb6cd21293987e4579dea860e2ba66d607fb46e49524d53644.ne.png)

4. टोकनको अनुमतिहरू सीमित गर्नुहोस्: **Permissions** अन्तर्गत, **Account** ट्याबमा क्लिक गर्नुहोस्, र "+ Add permissions" बटनमा क्लिक गर्नुहोस्। ड्रपडाउन देखा पर्नेछ। कृपया **Models** खोज्नुहोस् र त्यसको लागि बाकस जाँच गर्नुहोस्।
    ![Add Models Permission](../../../translated_images/add_models_permissions.c0c44ed8b40fc143dc87792da9097d715b7de938354e8f771d65416ecc7816b8.ne.png)

5. टोकन सिर्जना गर्नु अघि आवश्यक अनुमतिहरू प्रमाणित गर्नुहोस्। ![Verify Permissions](../../../translated_images/verify_permissions.06bd9e43987a8b219f171bbcf519e45ababae35b844f5e9757e10afcb619b936.ne.png)

6. टोकन सिर्जना गर्नु अघि, सुनिश्चित गर्नुहोस् कि तपाईं टोकनलाई पासवर्ड म्यानेजर भल्ट जस्तो सुरक्षित स्थानमा भण्डारण गर्न तयार हुनुहुन्छ, किनकि यो सिर्जना गरेपछि फेरि देखाइने छैन। ![Store Token Securely](../../../translated_images/store_token_securely.08ee2274c6ad6caf3482f1cd1bad7ca3fdca1ce737bc485bfa6499c84297c789.ne.png)

तपाईंले हालै सिर्जना गरेको नयाँ टोकन प्रतिलिपि गर्नुहोस्। अब तपाईंले यो टोकनलाई यस कोर्समा समावेश गरिएको `.env` फाइलमा थप्नु पर्नेछ।

### चरण 2: तपाईंको `.env` फाइल सिर्जना गर्नुहोस्

तपाईंको टर्मिनलमा निम्न आदेश चलाएर `.env` फाइल सिर्जना गर्नुहोस्।

```bash
cp .env.example .env
```

यसले उदाहरण फाइललाई प्रतिलिपि गर्नेछ र `.env` फाइल सिर्जना गर्नेछ जहाँ तपाईं वातावरण चरहरूको लागि मानहरू भर्न सक्नुहुन्छ।

तपाईंको टोकन प्रतिलिपि गरेर, तपाईंको मनपर्ने टेक्स्ट एडिटरमा `.env` फाइल खोल्नुहोस् र `GITHUB_TOKEN` फिल्डमा टोकन पेस्ट गर्नुहोस्।
![GitHub Token Field](../../../translated_images/github_token_field.20491ed3224b5f4ab24d10ced7a68c4aba2948fe8999cfc8675edaa16f5e5681.ne.png)

अब तपाईं यस कोर्सका कोड नमूनाहरू चलाउन सक्षम हुनुहुनेछ।

## Azure AI Foundry र Azure AI Agent Service प्रयोग गरेर नमूनाहरूको सेटअप

### चरण 1: तपाईंको Azure प्रोजेक्ट अन्त बिन्दु प्राप्त गर्नुहोस्

Azure AI Foundry मा हब र प्रोजेक्ट सिर्जना गर्ने चरणहरू यहाँ पालना गर्नुहोस्: [Hub resources overview](https://learn.microsoft.com/en-us/azure/ai-foundry/concepts/ai-resources)

एक पटक तपाईंले आफ्नो प्रोजेक्ट सिर्जना गरेपछि, तपाईंले आफ्नो प्रोजेक्टको लागि कनेक्शन स्ट्रिङ प्राप्त गर्न आवश्यक छ।

यो Azure AI Foundry पोर्टलमा तपाईंको प्रोजेक्टको **Overview** पृष्ठमा गएर गर्न सकिन्छ।

![Project Connection String](../../../translated_images/project-endpoint.8cf04c9975bbfbf18f6447a599550edb052e52264fb7124d04a12e6175e330a5.ne.png)

### चरण 2: तपाईंको `.env` फाइल सिर्जना गर्नुहोस्

तपाईंको टर्मिनलमा निम्न आदेश चलाएर `.env` फाइल सिर्जना गर्नुहोस्।

```bash
cp .env.example .env
```

यसले उदाहरण फाइललाई प्रतिलिपि गर्नेछ र `.env` फाइल सिर्जना गर्नेछ जहाँ तपाईं वातावरण चरहरूको लागि मानहरू भर्न सक्नुहुन्छ।

तपाईंको टोकन प्रतिलिपि गरेर, तपाईंको मनपर्ने टेक्स्ट एडिटरमा `.env` फाइल खोल्नुहोस् र `PROJECT_ENDPOINT` फिल्डमा टोकन पेस्ट गर्नुहोस्।

### चरण 3: Azure मा साइन इन गर्नुहोस्

सुरक्षाको उत्तम अभ्यासको रूपमा, हामी [keyless authentication](https://learn.microsoft.com/azure/developer/ai/keyless-connections?tabs=csharp%2Cazure-cli?WT.mc_id=academic-105485-koreyst) प्रयोग गर्नेछौं Microsoft Entra ID सँग Azure OpenAI मा प्रमाणित गर्न।

अर्को, टर्मिनल खोल्नुहोस् र `az login --use-device-code` चलाएर Azure खातामा साइन इन गर्नुहोस्।

एक पटक तपाईं साइन इन गरेपछि, टर्मिनलमा आफ्नो सदस्यता चयन गर्नुहोस्।

## अतिरिक्त वातावरण चरहरू - Azure Search र Azure OpenAI 

Agentic RAG पाठ - पाठ ५ - मा नमूनाहरू छन् जसले Azure Search र Azure OpenAI प्रयोग गर्दछ।

यदि तपाईं यी नमूनाहरू चलाउन चाहनुहुन्छ भने, तपाईंले आफ्नो `.env` फाइलमा निम्न वातावरण चरहरू थप्न आवश्यक छ:

### ओभरभ्यू पृष्ठ (प्रोजेक्ट)

- `AZURE_SUBSCRIPTION_ID` - तपाईंको प्रोजेक्टको **Overview** पृष्ठमा **Project details** जाँच गर्नुहोस्।

- `AZURE_AI_PROJECT_NAME` - तपाईंको प्रोजेक्टको **Overview** पृष्ठको शीर्षमा हेर्नुहोस्।

- `AZURE_OPENAI_SERVICE` - **Overview** पृष्ठको **Included capabilities** ट्याबमा **Azure OpenAI Service** को लागि हेर्नुहोस्।

### व्यवस्थापन केन्द्र

- `AZURE_OPENAI_RESOURCE_GROUP` - **Management Center** को **Overview** पृष्ठमा **Project properties** मा जानुहोस्।

- `GLOBAL_LLM_SERVICE` - **Connected resources** अन्तर्गत, **Azure AI Services** कनेक्शन नाम खोज्नुहोस्। यदि सूचीबद्ध छैन भने, **Azure portal** मा तपाईंको स्रोत समूह अन्तर्गत AI Services स्रोत नाम जाँच गर्नुहोस्।

### मोडेलहरू + अन्त बिन्दु पृष्ठ

- `AZURE_OPENAI_EMBEDDING_DEPLOYMENT_NAME` - तपाईंको embedding मोडेल चयन गर्नुहोस् (जस्तै, `text-embedding-ada-002`) र मोडेल विवरणबाट **Deployment name** नोट गर्नुहोस्।

- `AZURE_OPENAI_CHAT_DEPLOYMENT_NAME` - तपाईंको च्याट मोडेल चयन गर्नुहोस् (जस्तै, `gpt-4o-mini`) र मोडेल विवरणबाट **Deployment name** नोट गर्नुहोस्।

### Azure पोर्टल

- `AZURE_OPENAI_ENDPOINT` - **Azure AI services** खोज्नुहोस्, त्यसमा क्लिक गर्नुहोस्, त्यसपछि **Resource Management**, **Keys and Endpoint** मा जानुहोस्, "Azure OpenAI endpoints" मा स्क्रोल गर्नुहोस्, र "Language APIs" भन्ने एक प्रतिलिपि गर्नुहोस्।

- `AZURE_OPENAI_API_KEY` - त्यही स्क्रिनबाट, KEY 1 वा KEY 2 प्रतिलिपि गर्नुहोस्।

- `AZURE_SEARCH_SERVICE_ENDPOINT` - तपाईंको **Azure AI Search** स्रोत खोज्नुहोस्, त्यसमा क्लिक गर्नुहोस्, र **Overview** हेर्नुहोस्।

- `AZURE_SEARCH_API_KEY` - त्यसपछि **Settings** मा जानुहोस् र **Keys** मा गएर प्राथमिक वा द्वितीयक एडमिन कुञ्जी प्रतिलिपि गर्नुहोस्।

### बाह्य वेबपेज

- `AZURE_OPENAI_API_VERSION` - [API version lifecycle](https://learn.microsoft.com/en-us/azure/ai-services/openai/api-version-deprecation#latest-ga-api-release) पृष्ठमा **Latest GA API release** अन्तर्गत जानुहोस्।

### Keyless authentication सेटअप गर्नुहोस्

तपाईंको प्रमाणहरू हार्डकोड नगर्ने, हामी Azure OpenAI सँग keyless कनेक्शन प्रयोग गर्नेछौं। यसका लागि, हामी `DefaultAzureCredential` आयात गर्नेछौं र पछि `DefaultAzureCredential` फङ्सनलाई प्रमाण प्राप्त गर्न कल गर्नेछौं।

```python
from azure.identity import DefaultAzureCredential, InteractiveBrowserCredential
```

## कतै अड्किनुभयो?
यदि तपाईंलाई यो सेटअप चलाउन कुनै समस्या छ भने, हाम्रो <a href="https://discord.gg/kzRShWzttr" target="_blank">Azure AI Community Discord</a> मा सामेल हुनुहोस् वा <a href="https://github.com/microsoft/ai-agents-for-beginners/issues?WT.mc_id=academic-105485-koreyst" target="_blank">समस्या सिर्जना गर्नुहोस्</a>।

## अर्को पाठ

अब तपाईं यस पाठ्यक्रमको कोड चलाउन तयार हुनुहुन्छ। AI एजेन्टहरूको संसारबारे थप सिक्न शुभकामना!

[AI एजेन्टहरू र एजेन्ट प्रयोग केसहरूको परिचय](../01-intro-to-ai-agents/README.md)

---

**अस्वीकरण**:  
यो दस्तावेज़ AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) प्रयोग गरेर अनुवाद गरिएको छ। हामी शुद्धताको लागि प्रयास गर्छौं, तर कृपया ध्यान दिनुहोस् कि स्वचालित अनुवादहरूमा त्रुटिहरू वा अशुद्धताहरू हुन सक्छ। यसको मूल भाषा मा रहेको दस्तावेज़लाई आधिकारिक स्रोत मानिनुपर्छ। महत्वपूर्ण जानकारीको लागि, व्यावसायिक मानव अनुवाद सिफारिस गरिन्छ। यस अनुवादको प्रयोगबाट उत्पन्न हुने कुनै पनि गलतफहमी वा गलत व्याख्याको लागि हामी जिम्मेवार हुने छैनौं।