<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "49fa13c21a816ffcc7740ab17ba024a9",
  "translation_date": "2025-05-20T07:56:44+00:00",
  "source_file": "00-course-setup/README.md",
  "language_code": "ja"
}
-->
# コース設定

## 導入

このレッスンでは、このコースのコード サンプルを実行する方法について説明します。

## このリポジトリをクローンまたはフォークする

まず、GitHubリポジトリをクローンまたはフォークしてください。これにより、コース教材の自分用バージョンが作成され、コードを実行、テスト、調整できるようになります。

リンクをクリックすると、<a href="https://github.com/microsoft/ai-agents-for-beginners/fork" target="_blank">fork the repo</a>

これで、次のリンクにこのコースの独自のフォーク バージョンが作成されます。

![Forked Repo](../../../translated_images/forked-repo.eea246a73044cc984a1e462349e36e7336204f00785e3187b7399905feeada07.ja.png)

## コードを実行する

このコースでは、AI エージェントの構築を実際に体験するために実行できる一連の Jupyter Notebook を提供します。

コード サンプルでは、​​次のいずれかを使用します。

**GitHub アカウントが必要です - 無料**:

1) Semantic Kernel Agent Framework + GitHub Models Marketplace. Labelled as (semantic-kernel.ipynb)
2) AutoGen Framework + GitHub Models Marketplace. Labeled as (autogen.ipynb)

**Azure サブスクリプションが必要です**:
3) Azure AI Foundry + Azure AI Agent Service. Labelled as (azureaiagent.ipynb)

3 種類の例をすべて試してみて、どれが最適か確認することをお勧めします。

## 要件

- Python 3.12+
- GitHub アカウント - GitHub Models Marketplace へのアクセス用
- Azure サブスクリプション - Azure AI Foundry へのアクセス用
- Azure AI Foundry アカウント - Azure AI Agent サービスへのアクセス用

このリポジトリのルートには、コード サンプルを実行するために必要なすべての Python パッケージが含まれる `requirements.txt` ファイルが含まれています。

リポジトリのルートでターミナルで次のコマンドを実行するとインストールできます。

```bash
pip install -r requirements.txt
```
競合や問題を回避するために、Python 仮想環境を作成することをお勧めします。

## GitHub モデルを使用したサンプルのセットアップ

### ステップ1：GitHubパーソナルアクセストークン（PAT）を取得する

現在、このコースでは、GitHub モデル マーケットプレイスを使用して、AI エージェントの作成に使用される大規模言語モデル (LLM) への無料アクセスを提供しています。

このサービスにアクセスするには、GitHub 個人アクセス トークンを作成する必要があります。

これは、GitHub アカウントの <a href="https://github.com/settings/personal-access-tokens" target="_blank">Personal Access Tokens settings</a> に移動することで実行できます。

画面の左側にある `Fine-grained tokens` オプションを選択します。

Then select `Generate new token`.

![Generate Token](../../../translated_images/generate-token.361ec40abe59b84ac68d63c23e2b6854d6fad82bd4e41feb98fc0e6f030e8ef7.ja.png)

You will be prompted to enter a name for your token, select the expiration date (Recommended: 30 Days), and select the scopes for your token (Public Repositories).

Copy your new token that you have just created. You will now add this to your `.env` file included in this course. 


### Step 2: Create Your `.env` File

To create your `.env`ファイルに対して、ターミナルで次のコマンドを実行してください。

```bash
cp .env.example .env
```

これにより、サンプルファイルがコピーされ、`.env` in your directory and where you fill in the values for the environment variables.

With your token copied, open the `.env` file in your favorite text editor and paste your token into the `GITHUB_TOKEN` field.

You should now be able to run the code samples of this course.

## Set Up for Samples using Azure AI Foundry and Azure AI Agent Service

### Step 1: Retrieve Your Azure Project Connection String

Follow the steps to creating a project and agent in Azure AI Foundry found here: [Create a project in Azure AI Foundry](https://learn.microsoft.com/en-us/azure/ai-services/agents/quickstart?pivots=ai-foundry-portal?WT.mc_id=academic-105485-koreyst)

Once you have created your project, you will need to retrieve the connection string for your project.

This can be done by going to the **Overview** page of your project in the Azure AI Foundry portal.

![Project Connection String](../../../translated_images/project-connection-string.8a2c7c804a33d53df14011e583d0c3fe0f79d9eb52b72e3c7d7d2f68f828c8aa.ja.png)

### Step 2: Create Your `.env` File

To create your `.env`ファイルが作成されます。ターミナルで次のコマンドを実行してください。

```bash
cp .env.example .env
```

これにより、サンプルファイルがコピーされ、`.env` in your directory and where you fill in the values for the environment variables.

With your token copied, open the `.env` file in your favorite text editor and paste your token into the `PROJECT_CONNECTION_STRING` field.

### Step 3: Sign in to Azure

As a security best practice, we'll use [keyless authentication](https://learn.microsoft.com/azure/developer/ai/keyless-connections?tabs=csharp%2Cazure-cli?WT.mc_id=academic-105485-koreyst) to authenticate to Azure OpenAI with Microsoft Entra ID. Before you can do so, you'll first need to install the **Azure CLI** per the [installation instructions](https://learn.microsoft.com/cli/azure/install-azure-cli?WT.mc_id=academic-105485-koreyst) for your operating system.

Next, open a terminal and run `az login --use-device-code` to sign in to your Azure account.

Once you've logged in, select your subscription in the terminal.


## Additional Envionment Variables - Azure Search and Azure OpenAI 

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

Rather than hardcode your credentials, we'll use a keyless connection with Azure OpenAI. To do so, we'll import `DefaultAzureCredential` and later call the `DefaultAzureCredential`関数を使って資格情報を取得してください。

```python
from azure.identity import DefaultAzureCredential, InteractiveBrowserCredential
```

## どこかで詰まったら？

セットアップで問題があれば、ぜひ私たちの

または

に参加してください。

## 次のレッスン

これでこのコースのコードを実行する準備が整いました。AIエージェントの世界についてさらに学ぶことを楽しんでください！

[AIエージェントとエージェントのユースケース入門](../01-intro-to-ai-agents/README.md)

**免責事項**:  
本書類はAI翻訳サービス「[Co-op Translator](https://github.com/Azure/co-op-translator)」を使用して翻訳されています。正確性を期しておりますが、自動翻訳には誤りや不正確な部分が含まれる可能性があることをご了承ください。原文の言語によるオリジナル文書が正式な情報源とみなされるべきです。重要な情報については、専門の人間による翻訳を推奨します。本翻訳の利用により生じた誤解や誤訳について、一切の責任を負いかねます。
