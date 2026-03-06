# 課程設置

## 介紹

本課程將涵蓋如何運行本課程的代碼範例。

## 加入其他學習者並獲取幫助

在開始克隆您的倉庫之前，請加入 [AI Agents For Beginners Discord 頻道](https://aka.ms/ai-agents/discord)，以獲得任何設置幫助、課程相關問題，或與其他學習者交流。

## 克隆或派生此倉庫

首先，請克隆或派生 GitHub 倉庫。這會產生您自己的課程材料版本，您可以運行、測試和調整代碼！

您可以點擊鏈接 <a href="https://github.com/microsoft/ai-agents-for-beginners/fork" target="_blank">派生倉庫</a> 來完成此操作。

您現在應該擁有以下鏈接的自己派生版本：

![Forked Repo](../../../translated_images/zh-HK/forked-repo.33f27ca1901baa6a.webp)

### 淺層克隆（推薦用於研討會 / Codespaces）

  >當您下載完整歷史和所有文件時，完整的倉庫可能很大（約3GB）。如果您只是參加研討會或只需要幾個課程資料夾，淺層克隆（或稀疏克隆）則通過截斷歷史及/或跳過 blobs 來避免大部分下載。

#### 快速淺層克隆 — 最小歷史，所有文件

將下面命令裡的 `<your-username>` 替換為您的派生 URL（或者您喜歡的上游 URL）。

僅克隆最新提交歷史（下載小）：

```bash|powershell
git clone --depth 1 https://github.com/<your-username>/ai-agents-for-beginners.git
```

克隆指定分支：

```bash|powershell
git clone --depth 1 --branch <branch-name> https://github.com/<your-username>/ai-agents-for-beginners.git
```


#### 部分（稀疏）克隆 — 最小 blobs + 僅選定資料夾

這使用部分克隆和稀疏檢出（需要 Git 2.25+，並推薦使用支持部分克隆的現代 Git）：

```bash|powershell
git clone --depth 1 --filter=blob:none --sparse https://github.com/<your-username>/ai-agents-for-beginners.git
```

進入倉庫資料夾：

```bash|powershell
cd ai-agents-for-beginners
```

然後指定您想要的資料夾（以下示例顯示兩個資料夾）：

```bash|powershell
git sparse-checkout set 00-course-setup 01-intro-to-ai-agents
```

克隆並驗證文件後，如果您只需要文件且想釋放空間（無 git 歷史），請刪除倉庫元數據（💀不可逆 — 您將失去所有 Git 功能：無法提交、拉取、推送或訪問歷史）。

```bash
# zsh/bash
rm -rf .git
```

```powershell
# PowerShell
Remove-Item -Recurse -Force .git
```


#### 使用 GitHub Codespaces（推薦避免本地大型下載）

- 通過 [GitHub UI](https://github.com/codespaces) 為此倉庫創建新的 Codespace。

- 在新創建的 Codespace 終端中，運行上述淺層/稀疏克隆命令之一，只將您需要的課程資料夾帶入 Codespace 工作區。
- 選擇性：在 Codespaces 中克隆後，刪除 .git 以回收額外空間（參見上方刪除命令）。
- 注意：如果您想直接在 Codespaces 中打開倉庫（無需額外克隆），請注意 Codespaces 將構建 devcontainer 環境，可能仍會配置超出您需求的內容。在新 Codespace 內克隆淺層副本能讓您更好地控制磁盤使用。

#### 提示

- 如果您想編輯/提交，請務必將克隆 URL 替換為您的派生。
- 如果您日後需要更多歷史或文件，您可以獲取它們或調整稀疏檢出以包含其他資料夾。

## 運行代碼

本課程提供一系列 Jupyter 筆記本，您可以運行它們以獲得構建 AI Agent 的實踐經驗。

代碼範例使用 **Microsoft Agent Framework (MAF)** 和 `AzureAIProjectAgentProvider`，後者通過 **Microsoft Foundry** 連接到 **Azure AI Agent Service V2**（Responses API）。

所有 Python 筆記本標記為 `*-python-agent-framework.ipynb`。

## 要求

- Python 3.12+
  - **注意**：如果您尚未安裝 Python3.12，請務必先安裝。然後使用 python3.12 創建您的虛擬環境，確保從 requirements.txt 文件安裝正確版本。
  
    >示例

    創建 Python 虛擬環境目錄：

    ```bash|powershell
    python -m venv venv
    ```

    然後激活虛擬環境：

    ```bash
    # zsh/bash
    source venv/bin/activate
    ```
  
    ```dos
    # Command Prompt for Windows
    venv\Scripts\activate
    ```

- .NET 10+: 對於使用 .NET 的示例代碼，請確保安裝 [.NET 10 SDK](https://dotnet.microsoft.com/download/dotnet/10.0) 或以後版本。然後，檢查您安裝的 .NET SDK 版本：

    ```bash|powershell
    dotnet --list-sdks
    ```

- **Azure CLI** — 用於身份驗證。從 [aka.ms/installazurecli](https://aka.ms/installazurecli) 安裝。
- **Azure 訂閱** — 用於訪問 Microsoft Foundry 和 Azure AI Agent Service。
- **Microsoft Foundry 項目** — 需擁有一個部署了模型（例如 `gpt-4o`）的項目。請參見以下 [步驟 1](../../../00-course-setup)。

本倉庫根目錄中包含 `requirements.txt` 文件，包含運行代碼範例所需的所有 Python 套件。

您可以在倉庫根目錄的終端中運行以下命令安裝：

```bash|powershell
pip install -r requirements.txt
```

我們建議創建 Python 虛擬環境以避免任何衝突和問題。

## 設置 VSCode

確保您在 VSCode 中使用的是正確版本的 Python。

![image](https://github.com/user-attachments/assets/a85e776c-2edb-4331-ae5b-6bfdfb98ee0e)

## 設置 Microsoft Foundry 和 Azure AI Agent 服務

### 步驟 1：創建 Microsoft Foundry 項目

您需要一個 Azure AI Foundry **hub** 和 **項目**，且項目中需部署模型，以運行筆記本。

1. 訪問 [ai.azure.com](https://ai.azure.com) 並使用您的 Azure 帳戶登入。
2. 創建一個 **hub**（或使用現有的）。參見：[Hub 資源概述](https://learn.microsoft.com/azure/ai-foundry/concepts/ai-resources)。
3. 在 hub 中創建一個 **項目**。
4. 從 **Models + Endpoints** → **Deploy model** 部署一個模型（例如 `gpt-4o`）。

### 步驟 2：取得您的項目端點和模型部署名稱

在 Microsoft Foundry 入口網站中的項目：

- **項目端點** — 進入 **Overview** 頁面，複製端點 URL。

![Project Connection String](../../../translated_images/zh-HK/project-endpoint.8cf04c9975bbfbf1.webp)

- **模型部署名稱** — 前往 **Models + Endpoints**，選擇您的已部署模型，並記下 **Deployment name**（例如 `gpt-4o`）。

### 步驟 3：使用 `az login` 登入 Azure

所有筆記本均使用 **`AzureCliCredential`** 進行身份驗證——無需管理 API 金鑰。這需要您通過 Azure CLI 登入。

1. 如果尚未安裝 Azure CLI，請安裝：[aka.ms/installazurecli](https://aka.ms/installazurecli)

2. 登入：

    ```bash|powershell
    az login
    ```

    如果您在無瀏覽器的遠端/Codespace 環境中：

    ```bash|powershell
    az login --use-device-code
    ```

3. 如果被提示，選擇您的訂閱 — 請選含有您 Foundry 項目的那個。

4. 驗證您已登入：

    ```bash|powershell
    az account show
    ```

> **為何要用 `az login`？** 筆記本使用 `azure-identity` 套件的 `AzureCliCredential` 來認證。這表示您的 Azure CLI session 提供認證——無需將 API 金鑰或秘密放入 `.env` 文件。這是[安全最佳實踐](https://learn.microsoft.com/azure/developer/ai/keyless-connections)。

### 步驟 4：建立您的 `.env` 文件

複製範例文件：

```bash
# zsh/bash
cp .env.example .env
```

```powershell
# PowerShell
Copy-Item .env.example .env
```

打開 `.env` 並填入這兩個值：

```env
AZURE_AI_PROJECT_ENDPOINT=https://<your-project>.services.ai.azure.com/api/projects/<your-project-id>
AZURE_AI_MODEL_DEPLOYMENT_NAME=gpt-4o
```

| 變數 | 尋找位置 |
|----------|-----------------|
| `AZURE_AI_PROJECT_ENDPOINT` | Foundry 入口網站 → 您的項目 → **Overview** 頁面 |
| `AZURE_AI_MODEL_DEPLOYMENT_NAME` | Foundry 入口網站 → **Models + Endpoints** → 您部署的模型名稱 |

大部分課程就這樣完成了！筆記本將透過您的 `az login` 會話自動身份驗證。

### 步驟 5：安裝 Python 依賴項

```bash|powershell
pip install -r requirements.txt
```

我們建議您在之前創建的虛擬環境中運行這個命令。

## 額外設置：第 5 課（Agentic RAG）

第5課使用 **Azure AI Search** 進行檢索增強生成。如果您計劃運行該課程，請將以下變數添加到 `.env` 文件：

| 變數 | 尋找位置 |
|----------|-----------------|
| `AZURE_SEARCH_SERVICE_ENDPOINT` | Azure 入口網站 → 您的 **Azure AI Search** 資源 → **Overview** → URL |
| `AZURE_SEARCH_API_KEY` | Azure 入口網站 → 您的 **Azure AI Search** 資源 → **設定** → **金鑰** → 主要管理金鑰 |

## 額外設置：第 6 和第 8 課（GitHub Models）

第6及第8課中的 일부筆記本使用 **GitHub Models**，而非 Azure AI Foundry。如果您打算運行這些範例，請將以下變數添加至 `.env` 文件：

| 變數 | 尋找位置 |
|----------|-----------------|
| `GITHUB_TOKEN` | GitHub → **Settings** → **Developer settings** → **Personal access tokens** |
| `GITHUB_ENDPOINT` | 使用 `https://models.inference.ai.azure.com`（預設值） |
| `GITHUB_MODEL_ID` | 要使用的模型名稱（例如 `gpt-4o-mini`） |

## 額外設置：第 8 課（Bing Grounding Workflow）

第8課條件工作流筆記本使用透過 Azure AI Foundry 的 **Bing grounding**。如您計劃執行該樣本，請將此變數添加至 `.env` 文件：

| 變數 | 尋找位置 |
|----------|-----------------|
| `BING_CONNECTION_ID` | Azure AI Foundry 入口網站 → 您的項目 → **Management** → **Connected resources** → 您的 Bing 連線 → 複製連接 ID |

## 疑難排解

### macOS 上的 SSL 證書驗證錯誤

如果您在 macOS 遇到如下錯誤：

```plaintext
ssl.SSLCertVerificationError: [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: self-signed certificate in certificate chain
```

這是 macOS 上 Python 已知問題，系統 SSL 證書未自動被信任。請按順序嘗試以下解決方案：

**選項 1：執行 Python 的安裝證書腳本（推薦）**

```bash
# 將 3.XX 換成你已安裝嘅 Python 版本（例如，3.12 或 3.13）：
/Applications/Python\ 3.XX/Install\ Certificates.command
```

**選項 2：在筆記本中使用 `connection_verify=False`（僅限 GitHub Models 筆記本）**

在第 6 課筆記本 (`06-building-trustworthy-agents/code_samples/06-system-message-framework.ipynb`) 中，已包含註解掉的解決方式。創建客戶端時取消註解 `connection_verify=False`：

```python
client = ChatCompletionsClient(
    endpoint=endpoint,
    credential=AzureKeyCredential(token),
    connection_verify=False,  # 如果遇到證書錯誤，請禁用 SSL 驗證
)
```

> **⚠️ 警告：** 禁用 SSL 驗證 (`connection_verify=False`) 會降低安全性，因為跳過了證書驗證。僅在開發環境中作為臨時解決方案使用，切勿在生產環境使用。

**選項 3：安裝並使用 `truststore`**

```bash
pip install truststore
```

然後在筆記本或腳本頂部（進行任何網絡請求前）添加：

```python
import truststore
truststore.inject_into_ssl()
```


## 卡住了？

如您在設置過程中遇到任何問題，歡迎加入我們的 <a href="https://discord.gg/kzRShWzttr" target="_blank">Azure AI 社群 Discord</a> 或 <a href="https://github.com/microsoft/ai-agents-for-beginners/issues?WT.mc_id=academic-105485-koreyst" target="_blank">提出問題</a>。

## 下一課

您現在已準備好運行本課程的代碼。祝您在 AI Agents 世界中學習愉快！

[AI Agents 介紹及應用案例](../01-intro-to-ai-agents/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責聲明**：  
本文件由 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。儘管我們致力於精確翻譯，請注意自動翻譯結果可能包含錯誤或不準確之處。原始語言文件應被視為權威來源。對於重要資料，建議採用專業人工翻譯。我們不對因使用本翻譯而引起的任何誤解或誤譯承擔責任。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->