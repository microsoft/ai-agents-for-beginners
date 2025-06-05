<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "c729f7442eb5afd55b5522e3ad65c822",
  "translation_date": "2025-06-05T14:53:32+00:00",
  "source_file": "00-course-setup/README.md",
  "language_code": "hi"
}
-->
आपके पास अब इस कोर्स का अपना फोर्क किया हुआ संस्करण निम्न लिंक में होना चाहिए:

![Forked Repo](../../../00-course-setup/images/forked-repo.png)

## कोड चलाना

यह कोर्स एक श्रृंखला प्रदान करता है Jupyter Notebooks की, जिन्हें आप चलाकर AI एजेंट बनाने का व्यावहारिक अनुभव प्राप्त कर सकते हैं।

कोड नमूने निम्न में से किसी एक का उपयोग करते हैं:

**GitHub अकाउंट आवश्यक - मुफ्त**:

1) Semantic Kernel Agent Framework + GitHub Models Marketplace। इसे (semantic-kernel.ipynb) के रूप में लेबल किया गया है।
2) AutoGen Framework + GitHub Models Marketplace। इसे (autogen.ipynb) के रूप में लेबल किया गया है।

**Azure सब्सक्रिप्शन आवश्यक**:
3) Azure AI Foundry + Azure AI Agent Service। इसे (azureaiagent.ipynb) के रूप में लेबल किया गया है।

हम आपको तीनों प्रकार के उदाहरणों को आज़माने के लिए प्रोत्साहित करते हैं ताकि आप देख सकें कि कौन सा आपके लिए सबसे अच्छा काम करता है।

जो भी विकल्प आप चुनें, वह निर्धारित करेगा कि आपको नीचे दिए गए कौन से सेटअप चरणों का पालन करना है:

## आवश्यकताएँ

- Python 3.12+
- GitHub अकाउंट - GitHub Models Marketplace तक पहुंच के लिए
- Azure सब्सक्रिप्शन - Azure AI Foundry तक पहुंच के लिए
- Azure AI Foundry अकाउंट - Azure AI Agent Service तक पहुंच के लिए

हमने इस रिपॉजिटरी की रूट डायरेक्टरी में एक `requirements.txt` फ़ाइल शामिल की है जिसमें कोड नमूनों को चलाने के लिए आवश्यक सभी Python पैकेज हैं।

आप इन्हें रिपॉजिटरी की रूट में अपने टर्मिनल में निम्न कमांड चलाकर इंस्टॉल कर सकते हैं:

```bash
pip install -r requirements.txt
```
किसी भी टकराव और समस्याओं से बचने के लिए हम Python वर्चुअल एन्वायरनमेंट बनाने की सलाह देते हैं।

## GitHub Models का उपयोग करने वाले नमूनों के लिए सेटअप

### चरण 1: अपना GitHub Personal Access Token (PAT) प्राप्त करें

वर्तमान में, यह कोर्स GitHub Models Marketplace का उपयोग करता है ताकि Large Language Models (LLMs) तक मुफ्त पहुंच प्रदान की जा सके, जिनका उपयोग AI एजेंट बनाने में किया जाएगा।

इस सेवा तक पहुंचने के लिए, आपको GitHub Personal Access Token बनाना होगा।

यह आपके GitHub अकाउंट में जाकर किया जा सकता है।

`Fine-grained tokens` option on the left side of your screen.

Then select `Generate new token`.

![Generate Token](../../../00-course-setup/images/generate-token.png)

You will be prompted to enter a name for your token, select the expiration date (Recommended: 30 Days), and select the scopes for your token (Public Repositories).

It's also necessary to edit the permissions of this token: Permissions -> Models -> Allows access to GitHub Models

Copy your new token that you have just created. You will now add this to your `.env` file included in this course. 


### Step 2: Create Your `.env` File

To create your `.env` फ़ाइल में अपने टर्मिनल में निम्न कमांड चलाएं।

```bash
cp .env.example .env
```

यह उदाहरण फ़ाइल की कॉपी बनाएगा और `.env` in your directory and where you fill in the values for the environment variables.

With your token copied, open the `.env` file in your favorite text editor and paste your token into the `GITHUB_TOKEN` field.

You should now be able to run the code samples of this course.

## Set Up for Samples using Azure AI Foundry and Azure AI Agent Service

### Step 1: Retrieve Your Azure Project Connection String


Follow the steps to creating a hub and project in Azure AI Foundry found here: [Hub resources overview](https://learn.microsoft.com/en-us/azure/ai-foundry/concepts/ai-resources)


Once you have created your project, you will need to retrieve the connection string for your project.

This can be done by going to the **Overview** page of your project in the Azure AI Foundry portal.

![Project Connection String](../../../00-course-setup/images/project-connection-string.png)

### Step 2: Create Your `.env` File

To create your `.env` फ़ाइल बनाएगा। अपने टर्मिनल में निम्न कमांड चलाएं।

```bash
cp .env.example .env
```

यह उदाहरण फ़ाइल की कॉपी बनाएगा और `.env` in your directory and where you fill in the values for the environment variables.

With your token copied, open the `.env` file in your favorite text editor and paste your token into the `PROJECT_CONNECTION_STRING` field.

### Step 3: Sign in to Azure

As a security best practice, we'll use [keyless authentication](https://learn.microsoft.com/azure/developer/ai/keyless-connections?tabs=csharp%2Cazure-cli?WT.mc_id=academic-105485-koreyst) to authenticate to Azure OpenAI with Microsoft Entra ID. Before you can do so, you'll first need to install the **Azure CLI** per the [installation instructions](https://learn.microsoft.com/cli/azure/install-azure-cli?WT.mc_id=academic-105485-koreyst) for your operating system.

Next, open a terminal and run `az login --use-device-code` to sign in to your Azure account.

Once you've logged in, select your subscription in the terminal.


## Additional Environment Variables - Azure Search and Azure OpenAI 

For the Agentic RAG Lesson - Lesson 5 - there are samples that use Azure Search and Azure OpenAI.

If you want to run these samples, you will need to add the following environment variables to your `.env` file:

### Overview Page (Project)

- `AZURE_SUBSCRIPTION_ID` - Check **Project details** on the **Overview** page of your project.

- `AZURE_AI_PROJECT_NAME` - Look at the top of the **Overview** page for your project.

- `AZURE_OPENAI_SERVICE` - Find this in the **Included capabilities** tab for **Azure OpenAI Service** on the **Overview** page.

### Management Center

- `AZURE_OPENAI_RESOURCE_GROUP` - Go to **Project properties** on the **Overview** page of the **Management Center**.

- `GLOBAL_LLM_SERVICE` - Under **Connected resources**, find the **Azure AI Services** connection name. If not listed, check the **Azure portal** under your resource group for the AI Services resource name.

### Models + Endpoints Page

- `AZURE_OPENAI_EMBEDDING_DEPLOYMENT_NAME` - Select your embedding model (e.g., `text-embedding-ada-002`) and note the **Deployment name** from the model details.

- `AZURE_OPENAI_CHAT_DEPLOYMENT_NAME` - Select your chat model (e.g., `gpt-4o-mini`) and note the **Deployment name** from the model details.

### Azure Portal

- `AZURE_OPENAI_ENDPOINT` - Look for **Azure AI services**, click on it, then go to **Resource Management**, **Keys and Endpoint**, scroll down to the "Azure OpenAI endpoints", and copy the one that says "Language APIs".

- `AZURE_OPENAI_API_KEY` - From the same screen, copy KEY 1 or KEY 2.

- `AZURE_SEARCH_SERVICE_ENDPOINT` - Find your **Azure AI Search** resource, click it, and see **Overview**.

- `AZURE_SEARCH_API_KEY` - Then go to **Settings** and then **Keys** to copy the primary or secondary admin key.

### External Webpage

- `AZURE_OPENAI_API_VERSION` - Visit the [API version lifecycle](https://learn.microsoft.com/en-us/azure/ai-services/openai/api-version-deprecation#latest-ga-api-release) page under **Latest GA API release**.

### Setup keyless authentication

Rather than hardcode your credentials, we'll use a keyless connection with Azure OpenAI. To do so, we'll import `DefaultAzureCredential` and later call the `DefaultAzureCredential` फ़ंक्शन का उपयोग करके क्रेडेंशियल प्राप्त करें।

```python
from azure.identity import DefaultAzureCredential, InteractiveBrowserCredential
```

## कहीं अटक गए?

यदि इस सेटअप को चलाने में आपको कोई समस्या हो, तो हमारे 

या 

में शामिल हों।

## अगला पाठ

अब आप इस कोर्स के लिए कोड चलाने के लिए तैयार हैं। AI एजेंट्स की दुनिया के बारे में और जानने के लिए शुभकामनाएं!

[Introduction to AI Agents and Agent Use Cases](../01-intro-to-ai-agents/README.md)

**अस्वीकरण**:  
इस दस्तावेज़ का अनुवाद AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) का उपयोग करके किया गया है। जबकि हम सटीकता के लिए प्रयासरत हैं, कृपया ध्यान दें कि स्वचालित अनुवादों में त्रुटियाँ या असंगतियाँ हो सकती हैं। मूल दस्तावेज़ अपनी मूल भाषा में ही अधिकारिक स्रोत माना जाना चाहिए। महत्वपूर्ण जानकारी के लिए, पेशेवर मानव अनुवाद की सलाह दी जाती है। इस अनुवाद के उपयोग से उत्पन्न किसी भी गलतफहमी या गलत व्याख्या के लिए हम जिम्मेदार नहीं हैं।