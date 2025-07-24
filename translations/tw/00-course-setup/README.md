<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "c6a79c8f2b56a80370ff7e447765524f",
  "translation_date": "2025-07-24T07:52:25+00:00",
  "source_file": "00-course-setup/README.md",
  "language_code": "tw"
}
-->
# 課程設定

## 簡介

本課程將教您如何執行課程中的程式碼範例。

## 複製或分叉此存儲庫

首先，請複製或分叉 GitHub 存儲庫。這將建立您自己的課程材料版本，方便您執行、測試和調整程式碼！

您可以透過點擊以下連結完成操作：

![分叉存儲庫](../../../translated_images/forked-repo.33f27ca1901baa6a5e13ec3eb1f0ddd3a44d936d91cc8cfb19bfdb9688bd2c3d.tw.png)

## 執行程式碼

本課程提供一系列 Jupyter Notebook，讓您能夠親自操作並學習如何建立 AI Agents。

程式碼範例使用以下方式：

**需要 GitHub 帳戶 - 免費**：

1) Semantic Kernel Agent Framework + GitHub Models Marketplace，標記為 (semantic-kernel.ipynb)
2) AutoGen Framework + GitHub Models Marketplace，標記為 (autogen.ipynb)

**需要 Azure 訂閱**：
3) Azure AI Foundry + Azure AI Agent Service，標記為 (azureaiagent.ipynb)

我們鼓勵您嘗試所有三種範例，看看哪一種最適合您。

您選擇的範例將決定以下需要遵循的設定步驟：

## 系統需求

- Python 3.12+
  - **注意**：如果您尚未安裝 Python 3.12，請確保安裝它。然後使用 python3.12 建立虛擬環境 (venv)，以確保從 requirements.txt 文件中安裝正確的版本。
- GitHub 帳戶 - 用於存取 GitHub Models Marketplace
- Azure 訂閱 - 用於存取 Azure AI Foundry
- Azure AI Foundry 帳戶 - 用於存取 Azure AI Agent Service

我們在存儲庫的根目錄中包含了一個 `requirements.txt` 文件，其中列出了執行程式碼範例所需的所有 Python 套件。

您可以在終端機中於存儲庫根目錄執行以下命令來安裝它們：

```bash
pip install -r requirements.txt
```
我們建議建立 Python 虛擬環境以避免任何衝突和問題。

## 設定 VSCode
確保您在 VSCode 中使用正確版本的 Python。

![image](https://github.com/user-attachments/assets/a85e776c-2edb-4331-ae5b-6bfdfb98ee0e)

## 使用 GitHub Models 的範例設定

### 步驟 1：取得您的 GitHub 個人存取權杖 (PAT)

本課程使用 GitHub Models Marketplace，提供免費存取大型語言模型 (LLMs)，您將使用它們來建立 AI Agents。

要使用 GitHub Models，您需要建立 [GitHub 個人存取權杖](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens)。

您可以在您的 GitHub 帳戶中完成此操作。

請遵循 [最小權限原則](https://docs.github.com/en/get-started/learning-to-code/storing-your-secrets-safely) 建立您的權杖。這意味著您應僅授予權杖執行本課程程式碼範例所需的權限。

1. 在螢幕左側選擇 `Fine-grained tokens` 選項。

    然後選擇 `Generate new token`。

    ![生成權杖](../../../translated_images/generate-new-token.8772e24e8e2e067f2e6742500eaf68bb5c5f8999537bd79a040d2ecc09c7fdcb.tw.png)

1. 為您的權杖輸入一個描述性名稱，反映其用途，方便日後識別。設定到期日期（建議：30 天；如果您希望更安全，可以選擇更短的期限，例如 7 天）。

    ![權杖名稱和到期日期](../../../translated_images/token-name-expiry-date.a095fb0de63868640a4c82d6b1bbc92b482930a663917a5983a3c7cd1ef86b77.tw.png)

1. 將權杖的範圍限制在您分叉的存儲庫。

    ![限制範圍至分叉存儲庫](../../../translated_images/select-fork-repository.4497f6bb05ccd6b474ed134493a815fc34f94f89db2b1630c494adff7b5b558a.tw.png)

1. 限制權杖的權限：在 **Permissions** 下，切換 **Account Permissions**，找到 **Models** 並僅啟用 GitHub Models 所需的讀取權限。

    ![帳戶權限](../../../translated_images/account-permissions.de1806fad33a72c6194d2688cf2c10f2adb9ff7a5c1041a2329cbef46bffbba0.tw.png)

    ![Models 讀取權限](../../../translated_images/models-read-access.c00bc44e28c40450a85542e19f8e8c68284c71861c076b7dbc078b4c7e51faa6.tw.png)

複製您剛剛建立的新權杖。接下來，您需要將此權杖添加到課程中包含的 `.env` 文件。

### 步驟 2：建立您的 `.env` 文件

要建立 `.env` 文件，請在終端機中執行以下命令：

```bash
cp .env.example .env
```

這將複製範例文件並在您的目錄中建立 `.env` 文件，您需要在其中填寫環境變數的值。

複製您的權杖後，使用您喜愛的文字編輯器打開 `.env` 文件，並將權杖貼到 `GITHUB_TOKEN` 欄位中。

現在，您應該能夠執行本課程的程式碼範例。

## 使用 Azure AI Foundry 和 Azure AI Agent Service 的範例設定

### 步驟 1：取得您的 Azure 專案端點

按照以下步驟在 Azure AI Foundry 中建立 Hub 和專案：[Hub 資源概述](https://learn.microsoft.com/en-us/azure/ai-foundry/concepts/ai-resources)

建立專案後，您需要取得專案的連接字串。

您可以在 Azure AI Foundry 入口網站的 **概述** 頁面找到此資訊。

![專案連接字串](../../../translated_images/project-endpoint.8cf04c9975bbfbf18f6447a599550edb052e52264fb7124d04a12e6175e330a5.tw.png)

### 步驟 2：建立您的 `.env` 文件

要建立 `.env` 文件，請在終端機中執行以下命令：

```bash
cp .env.example .env
```

這將複製範例文件並在您的目錄中建立 `.env` 文件，您需要在其中填寫環境變數的值。

複製您的權杖後，使用您喜愛的文字編輯器打開 `.env` 文件，並將權杖貼到 `PROJECT_ENDPOINT` 欄位中。

### 步驟 3：登入 Azure

作為安全性最佳實踐，我們將使用 [無密鑰驗證](https://learn.microsoft.com/azure/developer/ai/keyless-connections?tabs=csharp%2Cazure-cli?WT.mc_id=academic-105485-koreyst) 透過 Microsoft Entra ID 驗證至 Azure OpenAI。

接下來，打開終端機並執行 `az login --use-device-code` 登入您的 Azure 帳戶。

登入後，在終端機中選擇您的訂閱。

## 額外的環境變數 - Azure Search 和 Azure OpenAI

在 Agentic RAG 課程 - 第五課 - 中，有使用 Azure Search 和 Azure OpenAI 的範例。

如果您希望執行這些範例，您需要在 `.env` 文件中添加以下環境變數：

### 概述頁面（專案）

- `AZURE_SUBSCRIPTION_ID` - 在專案的 **概述** 頁面中檢查 **專案詳細資訊**。
- `AZURE_AI_PROJECT_NAME` - 在專案的 **概述** 頁面頂部查看專案名稱。
- `AZURE_OPENAI_SERVICE` - 在 **概述** 頁面的 **包含的功能** 標籤中找到 **Azure OpenAI Service**。

### 管理中心

- `AZURE_OPENAI_RESOURCE_GROUP` - 在 **管理中心** 的 **概述** 頁面中查看 **專案屬性**。
- `GLOBAL_LLM_SERVICE` - 在 **連接的資源** 下找到 **Azure AI Services** 連接名稱。如果未列出，請檢查 **Azure 入口網站** 中資源群組的 AI Services 資源名稱。

### 模型 + 端點頁面

- `AZURE_OPENAI_EMBEDDING_DEPLOYMENT_NAME` - 選擇您的嵌入模型（例如 `text-embedding-ada-002`），並記下模型詳細資訊中的 **部署名稱**。
- `AZURE_OPENAI_CHAT_DEPLOYMENT_NAME` - 選擇您的聊天模型（例如 `gpt-4o-mini`），並記下模型詳細資訊中的 **部署名稱**。

### Azure 入口網站

- `AZURE_OPENAI_ENDPOINT` - 找到 **Azure AI Services**，點擊它，然後進入 **資源管理**，選擇 **金鑰和端點**，向下滾動到 "Azure OpenAI endpoints"，複製標記為 "Language APIs" 的端點。
- `AZURE_OPENAI_API_KEY` - 在同一頁面中，複製 KEY 1 或 KEY 2。
- `AZURE_SEARCH_SERVICE_ENDPOINT` - 找到您的 **Azure AI Search** 資源，點擊它，然後查看 **概述**。
- `AZURE_SEARCH_API_KEY` - 然後進入 **設定**，選擇 **金鑰**，複製主要或次要管理金鑰。

### 外部網頁

- `AZURE_OPENAI_API_VERSION` - 訪問 [API 版本生命週期](https://learn.microsoft.com/en-us/azure/ai-services/openai/api-version-deprecation#latest-ga-api-release) 頁面，查看 **最新 GA API 發布**。

### 設定無密鑰驗證

為避免硬編碼您的憑證，我們將使用 Azure OpenAI 的無密鑰連接。為此，我們將導入 `DefaultAzureCredential`，稍後調用 `DefaultAzureCredential` 函數以獲取憑證。

```python
from azure.identity import DefaultAzureCredential, InteractiveBrowserCredential
```

## 遇到問題？

如果您在設定過程中遇到任何問題，請加入我們的

## 下一課

您現在已準備好執行本課程的程式碼。祝您在探索 AI Agents 的世界中學習愉快！

[AI Agents 簡介及應用案例](../01-intro-to-ai-agents/README.md)

**免責聲明**：  
本文件使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。我們致力於提供準確的翻譯，但請注意，自動翻譯可能包含錯誤或不準確之處。應以原始語言的文件作為權威來源。對於關鍵資訊，建議尋求專業人工翻譯。我們對因使用此翻譯而引起的任何誤解或誤讀概不負責。