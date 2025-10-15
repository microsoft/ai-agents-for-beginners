<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "96eb7f95375daa3e91778ca0295a55d9",
  "translation_date": "2025-10-15T11:34:47+00:00",
  "source_file": "00-course-setup/README.md",
  "language_code": "en"
}
-->
# Course Setup

## Introduction

This lesson will explain how to run the code samples provided in this course.

## Connect with Other Learners and Get Support

Before cloning the repository, join the [AI Agents For Beginners Discord channel](https://aka.ms/ai-agents/discord) to get help with the setup, ask questions about the course, or connect with other learners.

## Clone or Fork this Repository

To get started, clone or fork the GitHub repository. This will create your own copy of the course materials, allowing you to run, test, and modify the code.

You can do this by clicking the link to <a href="https://github.com/microsoft/ai-agents-for-beginners/fork" target="_blank">fork the repository</a>.

Afterward, you will have your own forked version of the course available at the following link:

![Forked Repo](../../../translated_images/forked-repo.33f27ca1901baa6a5e13ec3eb1f0ddd3a44d936d91cc8cfb19bfdb9688bd2c3d.en.png)

### Shallow Clone (recommended for workshop / Codespaces)

  >The complete repository can be quite large (~3 GB) if you download the full history and all files. If you're only participating in the workshop or need access to specific lesson folders, a shallow clone (or sparse clone) can save time and storage by downloading only the essentials.

#### Quick shallow clone — minimal history, all files

Replace `<your-username>` in the commands below with your fork URL (or the upstream URL if preferred).

To clone only the latest commit history (smaller download):

```bash|powershell
git clone --depth 1 https://github.com/<your-username>/ai-agents-for-beginners.git
```

To clone a specific branch:

```bash|powershell
git clone --depth 1 --branch <branch-name> https://github.com/<your-username>/ai-agents-for-beginners.git
```

#### Partial (sparse) clone — minimal blobs + only selected folders

This method uses partial clone and sparse-checkout (requires Git 2.25+; modern Git versions with partial clone support are recommended):

```bash|powershell
git clone --depth 1 --filter=blob:none --sparse https://github.com/<your-username>/ai-agents-for-beginners.git
```

Navigate into the repository folder:

For bash:

```bash
cd ai-agents-for-beginners
```

For PowerShell:

```powershell
Set-Location ai-agents-for-beginners
```

Specify the folders you need (example below includes two folders):

```bash|powershell
git sparse-checkout set 00-course-setup 01-intro-to-ai-agents
```

After cloning and verifying the files, if you only need the files and want to free up space (no Git history), you can delete the repository metadata (💀irreversible — this will remove all Git functionality: no commits, pulls, pushes, or history access).

For Linux/macOS:

```bash
rm -rf .git
```

For Windows:

```powershell
Remove-Item -Recurse -Force .git
```

#### Using GitHub Codespaces (recommended to avoid large local downloads)

- Create a new Codespace for this repository via the [GitHub UI](https://github.com/codespaces).  

- In the terminal of the newly created Codespace, run one of the shallow/sparse clone commands above to bring only the lesson folders you need into the Codespace workspace.
- Optional: After cloning inside Codespaces, remove the `.git` folder to reclaim extra space (see removal commands above).
- Note: If you prefer to open the repository directly in Codespaces (without an additional clone), be aware that Codespaces will set up the development container environment and may still provision more than you need. Cloning a shallow copy inside a fresh Codespace gives you more control over disk usage.

#### Tips

- Always replace the clone URL with your fork if you plan to edit/commit.
- If you need more history or files later, you can fetch them or adjust sparse-checkout to include additional folders.

## Running the Code

This course includes a series of Jupyter Notebooks that you can use to gain hands-on experience in building AI Agents.

The code samples use one of the following:

**Requires GitHub Account - Free**:

1) Semantic Kernel Agent Framework + GitHub Models Marketplace. Labeled as (semantic-kernel.ipynb)
2) AutoGen Framework + GitHub Models Marketplace. Labeled as (autogen.ipynb)

**Requires Azure Subscription**:
3) Azure AI Foundry + Azure AI Agent Service. Labeled as (azureaiagent.ipynb)

We recommend trying all three types of examples to determine which works best for you.

Your choice will determine the setup steps you need to follow below:

## Requirements

- Python 3.12+
  - **NOTE**: If Python 3.12 is not installed, make sure to install it. Then create your virtual environment using Python 3.12 to ensure the correct versions are installed from the `requirements.txt` file.
  
    >Example

    Create a Python virtual environment directory:

    ``` bash
    python3 -m venv venv
    ```

    Then activate the virtual environment:

    macOS and Linux

    ```bash
    source venv/bin/activate
    ```
  
    Windows

    ```bash
    venv\Scripts\activate
    ```

- A GitHub Account - For access to the GitHub Models Marketplace
- Azure Subscription - For access to Azure AI Foundry
- Azure AI Foundry Account - For access to the Azure AI Agent Service

A `requirements.txt` file is included in the root of this repository, containing all the necessary Python packages to run the code samples.

Install them by running the following command in your terminal at the root of the repository:

```bash
pip install -r requirements.txt
```

We recommend creating a Python virtual environment to avoid conflicts and issues.

## Setup VSCode
Ensure you are using the correct version of Python in VSCode.

![image](https://github.com/user-attachments/assets/a85e776c-2edb-4331-ae5b-6bfdfb98ee0e)

## Set Up for Samples using GitHub Models 

### Step 1: Retrieve Your GitHub Personal Access Token (PAT)

This course uses the GitHub Models Marketplace, which provides free access to Large Language Models (LLMs) for building AI Agents.

To use the GitHub Models, you need to create a [GitHub Personal Access Token](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens).

You can create this token by visiting your <a href="https://github.com/settings/personal-access-tokens" target="_blank">Personal Access Tokens settings</a> in your GitHub account.

Follow the [Principle of Least Privilege](https://docs.github.com/en/get-started/learning-to-code/storing-your-secrets-safely) when creating your token. Only grant the permissions necessary to run the code samples in this course.

1. Select the `Fine-grained tokens` option on the left side of your screen under **Developer settings**.
   ![](../../../translated_images/profile_developer_settings.410a859fe749c755c859d414294c5908e307222b2c61819c3203bbeed4470e25.en.png)

    Then click `Generate new token`.

    ![Generate Token](../../../translated_images/fga_new_token.1c1a234afe202ab37483944a291ee80c1868e1e78082fd6bd4180fea5d5a15b4.en.png)

2. Provide a descriptive name for your token that reflects its purpose, making it easier to identify later.

    🔐 Token Duration Recommendation

    Recommended duration: 30 days  
    For better security, you can choose a shorter period—such as 7 days 🛡️.  
    This is a great way to set a personal goal and complete the course while maintaining your learning momentum 🚀.

    ![Token Name and Expiration](../../../translated_images/token-name-expiry-date.a095fb0de63868640a4c82d6b1bbc92b482930a663917a5983a3c7cd1ef86b77.en.png)

3. Restrict the token's scope to your fork of this repository.

    ![Limit scope to fork repository](../../../translated_images/token_repository_limit.924ade5e11d9d8bb6cd21293987e4579dea860e2ba66d607fb46e49524d53644.en.png)

4. Limit the token's permissions: Under **Permissions**, click the **Account** tab, then click the "+ Add permissions" button. A dropdown will appear. Search for **Models** and check the box for it.
    ![Add Models Permission](../../../translated_images/add_models_permissions.c0c44ed8b40fc143dc87792da9097d715b7de938354e8f771d65416ecc7816b8.en.png)

5. Verify the required permissions before generating the token. ![Verify Permissions](../../../translated_images/verify_permissions.06bd9e43987a8b219f171bbcf519e45ababae35b844f5e9757e10afcb619b936.en.png)

6. Before generating the token, ensure you are ready to store it securely, such as in a password manager vault, as it will not be displayed again after creation. ![Store Token Securely](../../../translated_images/store_token_securely.08ee2274c6ad6caf3482f1cd1bad7ca3fdca1ce737bc485bfa6499c84297c789.en.png)

Copy the newly created token. You will now add this to your `.env` file included in this course.

### Step 2: Create Your `.env` File

To create your `.env` file, run the following command in your terminal:

```bash
cp .env.example .env
```

This will copy the example file and create a `.env` file in your directory, where you can fill in the values for the environment variables.

Paste your copied token into the `GITHUB_TOKEN` field in the `.env` file using your preferred text editor.
![GitHub Token Field](../../../translated_images/github_token_field.20491ed3224b5f4ab24d10ced7a68c4aba2948fe8999cfc8675edaa16f5e5681.en.png)

You should now be ready to run the code samples provided in this course.

## Set Up for Samples using Azure AI Foundry and Azure AI Agent Service

### Step 1: Retrieve Your Azure Project Endpoint

Follow the steps to create a hub and project in Azure AI Foundry as described here: [Hub resources overview](https://learn.microsoft.com/en-us/azure/ai-foundry/concepts/ai-resources).

Once your project is created, retrieve the connection string for your project.

You can find this on the **Overview** page of your project in the Azure AI Foundry portal.

![Project Connection String](../../../translated_images/project-endpoint.8cf04c9975bbfbf18f6447a599550edb052e52264fb7124d04a12e6175e330a5.en.png)

### Step 2: Create Your `.env` File

To create your `.env` file, run the following command in your terminal:

```bash
cp .env.example .env
```

This will copy the example file and create a `.env` file in your directory, where you can fill in the values for the environment variables.

Paste your copied token into the `PROJECT_ENDPOINT` field in the `.env` file using your preferred text editor.

### Step 3: Sign in to Azure

As a security best practice, use [keyless authentication](https://learn.microsoft.com/azure/developer/ai/keyless-connections?tabs=csharp%2Cazure-cli?WT.mc_id=academic-105485-koreyst) to authenticate to Azure OpenAI with Microsoft Entra ID.

Open a terminal and run `az login --use-device-code` to sign in to your Azure account.

After logging in, select your subscription in the terminal.

## Additional Environment Variables - Azure Search and Azure OpenAI 

For the Agentic RAG Lesson (Lesson 5), some samples use Azure Search and Azure OpenAI.

To run these samples, add the following environment variables to your `.env` file:

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

Instead of hardcoding your credentials, use a keyless connection with Azure OpenAI. Import `DefaultAzureCredential` and call the `DefaultAzureCredential` function to obtain the credential.

```python
from azure.identity import DefaultAzureCredential, InteractiveBrowserCredential
```

## Need Help?
If you encounter any problems while setting up, feel free to join our <a href="https://discord.gg/kzRShWzttr" target="_blank">Azure AI Community Discord</a> or <a href="https://github.com/microsoft/ai-agents-for-beginners/issues?WT.mc_id=academic-105485-koreyst" target="_blank">submit an issue</a>.

## Next Lesson

You're now ready to execute the code for this course. Enjoy exploring the fascinating world of AI Agents!

[Introduction to AI Agents and Agent Use Cases](../01-intro-to-ai-agents/README.md)

---

**Disclaimer**:  
This document has been translated using the AI translation service [Co-op Translator](https://github.com/Azure/co-op-translator). While we aim for accuracy, please note that automated translations may include errors or inaccuracies. The original document in its native language should be regarded as the authoritative source. For critical information, professional human translation is advised. We are not responsible for any misunderstandings or misinterpretations resulting from the use of this translation.