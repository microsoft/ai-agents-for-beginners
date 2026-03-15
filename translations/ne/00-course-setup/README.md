# Course Setup

## Introduction

यस पाठले यस कोर्सका कोड नमूनाहरू कसरी चलाउने भन्ने कुरालाई कभर गर्नेछ।

## Join Other Learners and Get Help

तपाईंले तपाईंको repo क्लोन गर्नुअघि, सेटअपमा सहयोग, कोर्स सम्बन्धि कुनै प्रश्न, वा अन्य सिक्नेहरूसँग जडान हुन [AI Agents For Beginners Discord channel](https://aka.ms/ai-agents/discord) मा सामेल हुनुस्।

## Clone or Fork this Repo

सुरू गर्न, कृपया GitHub Repository क्लोन वा फोर्क गर्नुहोस्। यसले कोर्स सामग्रीको तपाईंको आफ्नै संस्करण बनाउँछ जसले गर्दा तपाईंले कोड चलाउन, परीक्षण गर्न, र समायोजन गर्न सक्नुहुन्छ!

यो गर्न सकिन्छ <a href="https://github.com/microsoft/ai-agents-for-beginners/fork" target="_blank">repo फोर्क गर्न</a> लिंकमा क्लिक गरेर

तपाईंले अब निम्न लिंकमा यो कोर्सको आफ्नो फोर्क गरिएको संस्करण पाउनु भएको हुनुपर्छ:

![फोर्क गरिएको Repo](../../../translated_images/ne/forked-repo.33f27ca1901baa6a.webp)

### Shallow Clone (recommended for workshop / Codespaces)

  >पूर्ण रेपोजिटरी जब तपाईं पूर्ण इतिहास र सबै फाइलहरू डाउनलोड गर्नुहुन्छ ठूलो (~3 GB) हुन सक्छ। यदि तपाईं केवल कार्यशाला मा सहभागी हुनुहुन्छ वा केवल केही पाठ फोल्डरहरू चाहिन्छ भने, एक शल्लो क्लोन (वा स्पार्स क्लोन) ले इतिहास संक्षेप गरेर र/वा ब्लबहरू स्किप गरेर अधिकांश डाउनलोडबाट बचाउछ।

#### Quick shallow clone — minimal history, all files

तलका आदेशहरूमा `<your-username>` लाई तपाईंको फोर्क URL (वा तपाईं प्राथमिकता दिनुहुने भए अपस्ट्रीम URL) सँग प्रतिस्थापित गर्नुहोस्।

अन्तिम commit इतिहास मात्र क्लोन गर्न (सानो डाउनलोड):

```bash|powershell
git clone --depth 1 https://github.com/<your-username>/ai-agents-for-beginners.git
```

विशेष शाखा क्लोन गर्न:

```bash|powershell
git clone --depth 1 --branch <branch-name> https://github.com/<your-username>/ai-agents-for-beginners.git
```

#### Partial (sparse) clone — minimal blobs + only selected folders

यसले partial clone र sparse-checkout प्रयोग गर्दछ (आवश्यक Git 2.25+ र partial clone समर्थन भएको आधुनिक Git सिफारिस गरिन्छ):

```bash|powershell
git clone --depth 1 --filter=blob:none --sparse https://github.com/<your-username>/ai-agents-for-beginners.git
```

रेपो फोल्डरमा जानुहोस्:

```bash|powershell
cd ai-agents-for-beginners
```

पछि कुन फोल्डरहरू चाहनुहुन्छ निर्दिष्ट गर्नुहोस् (तलको उदाहरणले दुई फोल्डर देखाउँछ):

```bash|powershell
git sparse-checkout set 00-course-setup 01-intro-to-ai-agents
```

क्लोन र फाइलहरू जाँच गर्ने पछि, यदि तपाईंलाई केवल फाइलहरू चाहिन्छ र स्थान फ्री गर्न चाहनुहुन्छ (git इतिहास चाहिँदैन), कृपया रेपो मेटाडाटा हटाउनुहोस् (💀अपरिवर्तनीय — तपाईंले सबै Git कार्यक्षमता गुमाउनु हुनेछ: कुनै commits, pulls, pushes, वा इतिहास पहुँच हुनेछैन)।

```bash
# zsh/bash
rm -rf .git
```

```powershell
# पावरशेल
Remove-Item -Recurse -Force .git
```

#### Using GitHub Codespaces (recommended to avoid local large downloads)

- यस रेपोको लागि [GitHub UI](https://github.com/codespaces) मार्फत नयाँ Codespace सिर्जना गर्नुहोस्।  

- नयाँ सिर्जना गरिएको codespace को टर्मिनलमा माथिका शल्लो/स्पार्स क्लोन आदेशहरू मध्ये एक चलाउनुहोस् ताकि तपाईंलाई चाहिने मात्र पाठ फोल्डरहरू Codespace कार्यक्षेत्रमा ल्याउन सकियोस्।
- वैकल्पिक: Codespaces भित्र क्लोन गरेपछि, थप स्थान रिकभर गर्न .git हटाउनुस् (माथिका हटाउने आदेशहरू हेर्नुहोस्)।
- नोट: यदि तपाईं रेपो सिधै Codespaces मा खोल्न चाहनुहुन्छ (अतिरिक्त क्लोन बिना), जानकार हुनुहोस् कि Codespaces ले devcontainer वातावरण निर्माण गर्नेछ र अझै पनि तपाईंलाई आवश्यक भन्दा बढी संसाधन प्रावधान गर्न सक्छ। नयाँ Codespace भित्र शल्लो प्रतिलिपि क्लोन गर्दा डिस्क प्रयोगमा थप नियन्त्रण प्राप्त हुन्छ।

#### Tips

- यदि तपाईंले सम्पादन/कमिट गर्न चाहनुहुन्छ भने सधैं क्लोन URL लाई तपाईंको फोर्कसँग प्रतिस्थापित गर्नुहोस्।
- पछि तपाईंलाई थप इतिहास वा फाइलहरू चाहियो भने, तपाईं तिनीहरू फेच गर्न सक्नुहुन्छ वा sparse-checkout समायोजित गरेर अतिरिक्त फोल्डरहरू समावेश गर्न सक्नुहुन्छ।

## Running the Code

यस कोर्सले Jupyter Notebooks को श्रृंखला प्रस्ताव गर्छ जुन तपाईंले चलाएर AI Agents निर्माणमा व्यावहारिक अनुभव प्राप्त गर्न सक्नुहुन्छ।

कोड नमूनाहरूले Microsoft Agent Framework (MAF) प्रयोग गर्छन् र `AzureAIProjectAgentProvider` सँग जडित हुन्छ, जुन Microsoft Foundry मार्फत Azure AI Agent Service V2 (Responses API) सँग जडान गर्छ।

सबै Python नोटबुकहरू `*-python-agent-framework.ipynb` भनेर लेबल गरिएको छन्।

## Requirements

- Python 3.12+
  - **NOTE**: यदि तपाईंंसँग Python3.12 इन्स्टल छैन भने, सुनिश्चित गर्नुहोस् कि तपाईंले यसलाई इन्स्टल गर्नु भएको छ। तब requirements.txt फाइलबाट सही संस्करणहरू इन्स्टल गर्न python3.12 प्रयोग गरी आफ्नो venv सिर्जना गर्नुहोस्।
  
    >उदाहरण

    Python venv डाइरेक्टरी बनाउनुहोस्:

    ```bash|powershell
    python -m venv venv
    ```

    त्यसपछि venv वातावरण सक्रिय गर्नुहोस्:

    ```bash
    # zsh/bash
    source venv/bin/activate
    ```
  
    ```dos
    # Command Prompt for Windows
    venv\Scripts\activate
    ```

- .NET 10+: .NET प्रयोग गर्ने नमूना कोडहरूको लागि, कृपया [.NET 10 SDK](https://dotnet.microsoft.com/download/dotnet/10.0) वा पछि को संस्करण इन्स्टल गर्नुहोस्। त्यसपछि, इन्स्टल गरिएको .NET SDK संस्करण जाँच्नुहोस्:

    ```bash|powershell
    dotnet --list-sdks
    ```

- **Azure CLI** — प्रमाणीकरणको लागि आवश्यक। यहाँबाट इन्स्टल गर्नुहोस्: [aka.ms/installazurecli](https://aka.ms/installazurecli).
- **Azure Subscription** — Microsoft Foundry र Azure AI Agent Service पहुँचका लागि।
- **Microsoft Foundry Project** — डिप्लोय गरिएको मोडल भएको परियोजना (जस्तै, `gpt-4o`) चलाउनका लागि। हेर्नुहोस् [Step 1](../../../00-course-setup) तल।

हामीले यस रेपोको मूलमा `requirements.txt` फाइल समावेश गरेका छौं जसले कोड नमूनाहरू चलाउन आवश्यक सबै Python प्याकेजहरू समावेश गर्दछ।

तपाईंले तीहरू इन्स्टल गर्न रेपोको रुटमा आफ्नो टर्मिनलमा तलको आदेश चलाउन सक्नुहुन्छ:

```bash|powershell
pip install -r requirements.txt
```

हामी सिफारिस गर्छौं कि कुनै द्वन्द्व र समस्याबाट बच्न Python भर्चुअल वातावरण सिर्जना गर्नुहोस्।

## Setup VSCode

VSCode मा तपाईंले सही Python संस्करण प्रयोग गरिरहनु भएको छ भन्ने कुरा सुनिश्चित गर्नुहोस्।

![छवि](https://github.com/user-attachments/assets/a85e776c-2edb-4331-ae5b-6bfdfb98ee0e)

## Set Up Microsoft Foundry and Azure AI Agent Service

### Step 1: Create a Microsoft Foundry Project

नोटबुकहरू चलाउनको लागि तपाईंलाई Azure AI Foundry **hub** र **project** आवश्यक छ जसमा डिप्लोय गरिएको मोडल छ।

1. तपाईंको Azure खातामा साइन इन गर्न [ai.azure.com](https://ai.azure.com) मा जानुहोस्।
2. एक **hub** सिर्जना गर्नुहोस् (वा अवस्थित मध्ये प्रयोग गर्नुहोस्)। हेर्नुहोस्: [Hub resources overview](https://learn.microsoft.com/azure/ai-foundry/concepts/ai-resources).
3. हब भित्र एउटा **project** सिर्जना गर्नुहोस्।
4. **Models + Endpoints** → **Deploy model** बाट मोडल (उदा., `gpt-4o`) डिप्लोय गर्नुहोस्।

### Step 2: Retrieve Your Project Endpoint and Model Deployment Name

Microsoft Foundry पोर्टलमा तपाईंको परियोजनाबाट:

- **Project Endpoint** — **Overview** पृष्ठमा जानुहोस् र endpoint URL प्रतिलिपि गर्नुहोस्।

![Project Connection String](../../../translated_images/ne/project-endpoint.8cf04c9975bbfbf1.webp)

- **Model Deployment Name** — **Models + Endpoints** मा जानुहोस्, तपाईंले डिप्लोय गरेको मोडल चयन गर्नुहोस्, र **Deployment name** नोट गर्नुहोस् (उदा., `gpt-4o`)।

### Step 3: Sign in to Azure with `az login`

सबै नोटबुकहरूले प्रमाणीकरणका लागि **`AzureCliCredential`** प्रयोग गर्छन् — प्रबन्ध गर्न कुनै API कुञ्जीहरू आवश्यक छैन। यसको लागि तपाईंले Azure CLI मार्फत साइन इन हुनुपर्छ।

1. यदि तपाईंले अझै Azure CLI इन्स्टल गर्नुभएको छैन भने इन्स्टल गर्नुहोस्: [aka.ms/installazurecli](https://aka.ms/installazurecli)

2. निम्न चलाएर **साइन इन** गर्नुहोस्:

    ```bash|powershell
    az login
    ```

    वा यदि तपाईं रिमोट/Codespace वातावरणमा ब्राउजर बिना हुनुहुन्छ भने:

    ```bash|powershell
    az login --use-device-code
    ```

3. आवश्यक परेमा **तपाईंको subscription छान्नुहोस्** — Foundry परियोजना भएको सन्दर्भमा त्यो चयन गर्नुहोस्।

4. **पुष्टि** गर्नुहोस् कि तपाईं साइन इन हुनुहुन्छ:

    ```bash|powershell
    az account show
    ```

> **किन `az login`?** नोटबुकहरूले `azure-identity` प्याकेजबाट `AzureCliCredential` प्रयोग गरेर प्रमाणिकरण गर्दछन्। यसको अर्थ तपाईंको Azure CLI सेसनले प्रमाणपत्रहरू प्रदान गर्छ — तपाईंको `.env` फाइलमा कुनै API कुञ्जी वा गोप्य जानकारी राख्नु पर्दैन। यो एक [सुरक्षा उत्तम अभ्यास](https://learn.microsoft.com/azure/developer/ai/keyless-connections) हो।

### Step 4: Create Your `.env` File

उदाहरण फाइल प्रतिलिपि गर्नुहोस्:

```bash
# zsh/bash
cp .env.example .env
```

```powershell
# पावरशेल
Copy-Item .env.example .env
```

`.env` खोल्नुहोस् र यी दुई मानहरू भर्नुहोस्:

```env
AZURE_AI_PROJECT_ENDPOINT=https://<your-project>.services.ai.azure.com/api/projects/<your-project-id>
AZURE_AI_MODEL_DEPLOYMENT_NAME=gpt-4o
```

| Variable | Where to find it |
|----------|-----------------|
| `AZURE_AI_PROJECT_ENDPOINT` | Foundry पोर्टल → your project → **Overview** पृष्ठ |
| `AZURE_AI_MODEL_DEPLOYMENT_NAME` | Foundry पोर्टल → **Models + Endpoints** → तपाईंले डिप्लोय गरेको मोडलको नाम |

यतिमै धेरै पाठहरूका लागि पर्याप्त छ! नोटबुकहरूले तपाईंको `az login` सेसन मार्फत स्वतः प्रमाणिकरण गर्नेछन्।

### Step 5: Install Python Dependencies

```bash|powershell
pip install -r requirements.txt
```

हामी सिफारिस गर्छौं कि तपाईंले यो पहिले सिर्जना गरेको भर्चुअल वातावरण भित्र चलाउनुहोस्।

## Additional Setup for Lesson 5 (Agentic RAG)

पाठ 5 ले retrieval-augmented generation का लागि **Azure AI Search** प्रयोग गर्छ। यदि तपाईं त्यो पाठ चलाउन योजना गर्दै हुनुहुन्छ भने, यी भेरियेबलहरू तपाईंको `.env` फाइलमा जोड्नुहोस्:

| Variable | Where to find it |
|----------|-----------------|
| `AZURE_SEARCH_SERVICE_ENDPOINT` | Azure पोर्टल → तपाईंको **Azure AI Search** रिसोर्स → **Overview** → URL |
| `AZURE_SEARCH_API_KEY` | Azure पोर्टल → तपाईंको **Azure AI Search** रिसोर्स → **Settings** → **Keys** → primary admin key |

## Additional Setup for Lesson 6 and Lesson 8 (GitHub Models)

पाठ 6 र 8 का केही नोटबुकहरूले Azure AI Foundry को सट्टा **GitHub Models** प्रयोग गर्छन्। यदि तपाईं ती नमूनाहरू चलाउन योजना गर्दै हुनुहुन्छ भने, यी भेरियेबलहरू तपाईंको `.env` फाइलमा थप्नुहोस्:

| Variable | Where to find it |
|----------|-----------------|
| `GITHUB_TOKEN` | GitHub → **Settings** → **Developer settings** → **Personal access tokens** |
| `GITHUB_ENDPOINT` | Use `https://models.inference.ai.azure.com` (default value) |
| `GITHUB_MODEL_ID` | प्रयोग गर्नुपर्ने मोडल नाम (जस्तै `gpt-4o-mini`) |

## Additional Setup for Lesson 8 (Bing Grounding Workflow)

पाठ 8 मा रहेको conditional workflow नोटबुकले Azure AI Foundry मार्फत **Bing grounding** प्रयोग गर्छ। यदि तपाईं त्यो नमूना चलाउन योजना गर्दै हुनुहुन्छ भने, यो भेरियेबल तपाईंको `.env` फाइलमा थप्नुस्:

| Variable | Where to find it |
|----------|-----------------|
| `BING_CONNECTION_ID` | Azure AI Foundry पोर्टल → your project → **Management** → **Connected resources** → तपाईंको Bing connection → connection ID प्रतिलिपि गर्नुहोस् |

## Troubleshooting

### SSL Certificate Verification Errors on macOS

यदि तपाईं macOS मा हुनुहुन्छ र तल जस्तो त्रुटि आउँछ भने:

```plaintext
ssl.SSLCertVerificationError: [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: self-signed certificate in certificate chain
```

यो Python मा macOS को साथ एक ज्ञात समस्या हो जहाँ सिस्टम SSL प्रमाणपत्रहरू स्वतः विश्वास गरिँदैन। तलका समाधानहरू क्रमिक रूपमा प्रयास गर्नुहोस्:

**Option 1: Run Python's Install Certificates script (recommended)**

```bash
# 3.XX लाई तपाईंले इन्स्टल गरेको Python संस्करण (उदाहरणका लागि, 3.12 वा 3.13) सँग बदल्नुहोस्:
/Applications/Python\ 3.XX/Install\ Certificates.command
```

**Option 2: Use `connection_verify=False` in your notebook (for GitHub Models notebooks only)**

Lesson 6 नोटबुक (`06-building-trustworthy-agents/code_samples/06-system-message-framework.ipynb`) मा, एउटा टिप्पणी गरिएको वर्कअराउन्ड पहिले नै समावेश गरिएको छ। क्लाइन्ट बनाउँदा `connection_verify=False` अनकमेेन्ट गर्नुहोस्:

```python
client = ChatCompletionsClient(
    endpoint=endpoint,
    credential=AzureKeyCredential(token),
    connection_verify=False,  # प्रमाणपत्र त्रुटि आएमा SSL सत्यापन अक्षम गर्नुहोस्
)
```

> **⚠️ Warning:** SSL प्रमाणीकरण (`connection_verify=False`) अक्षम गर्नुले सुरक्षा घटाउँछ किनकि प्रमाणपत्र मान्यकरण स्किप हुन्छ। विकास वातावरणमा अस्थायी समाधानको रूपमा मात्र प्रयोग गर्नुहोस्, कहिल्यै उत्पादनमा प्रयोग नगर्नुहोस्।

**Option 3: Install and use `truststore`**

```bash
pip install truststore
```

तब आफ्नो नोटबुक वा स्क्रिप्टको माथि नेटवर्क कलहरू गर्नु अघि निम्न थप्नुहोस्:

```python
import truststore
truststore.inject_into_ssl()
```

## Stuck Somewhere?

यदि तपाईं यो सेटअप चलाउन कुनै समस्या हुनुहुन्छ भने, हाम्रो <a href="https://discord.gg/kzRShWzttr" target="_blank">Azure AI Community Discord</a> मा जानुहोस् वा <a href="https://github.com/microsoft/ai-agents-for-beginners/issues?WT.mc_id=academic-105485-koreyst" target="_blank">एक issue सिर्जना गर्नुहोस्</a>।

## Next Lesson

तपाईं अब यो कोर्सका लागि कोड चलाउन तयार हुनुहुन्छ। AI Agents को संसारबारे थप सिकाइमा सफल रहनुहोस्! 

[Introduction to AI Agents and Agent Use Cases](../01-intro-to-ai-agents/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
अस्वीकरण:
यो दस्तावेज AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) प्रयोग गरी अनुवाद गरिएको हो। हामी शुद्धताको लागि प्रयास गर्छौं, तर कृपया जानकार रहनुहोस् कि स्वचालित अनुवादमा त्रुटि वा अशुद्धता हुन सक्छ। मूल दस्तावेजलाई यसको मूल भाषामा नै प्रमाणिक स्रोत मानिनु पर्छ। महत्वपूर्ण जानकारीको लागि पेशेवर मानवीय अनुवाद सिफारिस गरिन्छ। यस अनुवादको प्रयोगबाट उत्पन्न हुने कुनै पनि गलतफहमी वा गलत व्याख्याका लागि हामी जिम्मेवार हुने छैनौं।
<!-- CO-OP TRANSLATOR DISCLAIMER END -->