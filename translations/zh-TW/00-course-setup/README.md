# 課程設定

## 簡介

本課將介紹如何執行本課程的程式範例。

## 與其他學習者交流並獲得協助

在開始複製你的 repo 之前，請先加入 [AI Agents For Beginners Discord channel](https://aka.ms/ai-agents/discord) 以獲得設定協助、課程相關問題的回答，或與其他學習者交流。

## 複製或 Fork 此儲存庫

開始之前，請複製或 fork GitHub 儲存庫。這會建立課程教材的個人版本，讓你可以執行、測試並調整程式碼！

This can be done by clicking the link to <a href="https://github.com/microsoft/ai-agents-for-beginners/fork" target="_blank">Fork 此儲存庫</a>

你現在應該在以下連結中擁有此課程的 fork 版本：

![已 fork 的儲存庫](../../../translated_images/zh-TW/forked-repo.33f27ca1901baa6a.webp)

### 淺層複製（建議用於工作坊 / Codespaces）

  >完整的儲存庫在下載完整歷史記錄與所有檔案時可能會很大（約 ~3 GB）。如果你只參加工作坊或只需要幾個課程資料夾，淺層複製（或稀疏複製）可以透過截斷歷史記錄和/或跳過 blobs 來避免大多數下載。

#### 快速淺層複製 — 最少歷史，但包含所有檔案

將下列指令中的 `<your-username>` 替換為你的 fork URL（或你偏好的 upstream URL）。

如果只想複製最近的提交歷史（下載量小）：

```bash|powershell
git clone --depth 1 https://github.com/<your-username>/ai-agents-for-beginners.git
```

複製特定分支：

```bash|powershell
git clone --depth 1 --branch <branch-name> https://github.com/<your-username>/ai-agents-for-beginners.git
```

#### 部分（sparse）複製 — 最少二進位檔案 + 僅選取的資料夾

這會使用 partial clone 與 sparse-checkout（需要 Git 2.25+，建議使用支援 partial clone 的現代 Git）：

```bash|powershell
git clone --depth 1 --filter=blob:none --sparse https://github.com/<your-username>/ai-agents-for-beginners.git
```

進入儲存庫資料夾：

```bash|powershell
cd ai-agents-for-beginners
```

然後指定你需要的資料夾（下面範例顯示兩個資料夾）：

```bash|powershell
git sparse-checkout set 00-course-setup 01-intro-to-ai-agents
```

複製並確認檔案後，如果你只需要檔案並想釋放空間（不保留 git 歷史），請刪除儲存庫的 metadata（💀不可逆 — 你將失去所有 Git 功能：無法提交、拉取、推送或存取歷史紀錄）。

```bash
# zsh/bash
rm -rf .git
```

```powershell
# PowerShell
Remove-Item -Recurse -Force .git
```

#### 使用 GitHub Codespaces（建議以避免本機大量下載）

- 透過 [GitHub UI](https://github.com/codespaces) 為此儲存庫建立新的 Codespace。  

- 在新建立的 Codespace 終端機中，執行上述其中一個淺層/稀疏複製指令，將你需要的課程資料夾帶入 Codespace 工作區。
- 選用：在 Codespaces 中複製後，移除 .git 以回收額外空間（參見上述刪除命令）。
- 注意：如果你偏好直接在 Codespaces 中開啟儲存庫（不另外複製），請注意 Codespaces 會建構 devcontainer 環境，可能仍會配置超出你需求的內容。在新的 Codespace 中先複製淺層副本，可以讓你更好地控制磁碟使用量。

#### 小提示

- 若要編輯/提交，務必將複製 URL 換成你的 fork。
- 若之後需要更多歷史或檔案，可透過 fetch 或調整 sparse-checkout 來包含其他資料夾。

## 執行程式碼

本課程提供一系列 Jupyter Notebook，可供你執行以獲得建立 AI Agents 的實作經驗。

程式範例使用 **Microsoft Agent Framework (MAF)** 與 `AzureAIProjectAgentProvider`，透過 **Microsoft Foundry** 連線到 **Azure AI Agent Service V2**（Responses API）。

所有 Python notebook 標示為 `*-python-agent-framework.ipynb`。

## 系統需求

- Python 3.12+
  - **注意**：如果你沒有安裝 Python3.12，請務必安裝。然後使用 python3.12 建立你的 venv，以確保從 requirements.txt 安裝到正確的版本。
  
    >範例

    建立 Python venv 目錄：

    ```bash|powershell
    python -m venv venv
    ```

    然後啟動 venv 環境：

    ```bash
    # zsh/bash
    source venv/bin/activate
    ```
  
    ```dos
    # Command Prompt for Windows
    venv\Scripts\activate
    ```

- .NET 10+: 若要執行使用 .NET 的範例程式，請安裝 [.NET 10 SDK](https://dotnet.microsoft.com/download/dotnet/10.0) 或更新版本。接著檢查你安裝的 .NET SDK 版本：

    ```bash|powershell
    dotnet --list-sdks
    ```

- **Azure CLI** — 用於認證。請從 [aka.ms/installazurecli](https://aka.ms/installazurecli) 安裝。
- **Azure 訂閱** — 用於存取 Microsoft Foundry 與 Azure AI Agent Service。
- **Microsoft Foundry 專案** — 需要一個已部署模型的專案（例如 `gpt-4o`）。請參閱下方的 [步驟 1](../../../00-course-setup)。

我們在此儲存庫根目錄包含了一個 `requirements.txt` 檔案，內含執行程式範例所需的所有 Python 套件。

你可以在儲存庫根目錄的終端機執行下列命令以安裝它們：

```bash|powershell
pip install -r requirements.txt
```

我們建議建立 Python 虛擬環境以避免衝突與問題。

## 設定 VSCode

確保在 VSCode 中使用正確的 Python 版本。

![圖片](https://github.com/user-attachments/assets/a85e776c-2edb-4331-ae5b-6bfdfb98ee0e)

## 設定 Microsoft Foundry 與 Azure AI Agent Service

### 步驟 1：建立 Microsoft Foundry 專案

你需要一個 Azure AI Foundry 的 **hub** 和 **project**，並部署模型，才能執行 notebook。

1. 前往 [ai.azure.com](https://ai.azure.com) 並使用你的 Azure 帳戶登入。
2. 建立一個 **hub**（或使用既有的）。參見：[Hub resources overview](https://learn.microsoft.com/azure/ai-foundry/concepts/ai-resources)。
3. 在 hub 裡建立一個 **project**。
4. 從 **Models + Endpoints** → **Deploy model** 部署模型（例如 `gpt-4o`）。

### 步驟 2：取得你的專案端點與模型部署名稱

在 Microsoft Foundry 入口網站的專案中：

- **Project Endpoint** — 前往 **Overview** 頁面並複製端點 URL。

![專案連線字串](../../../translated_images/zh-TW/project-endpoint.8cf04c9975bbfbf1.webp)

- **Model Deployment Name** — 前往 **Models + Endpoints**，選取你已部署的模型，並記下 **Deployment name**（例如 `gpt-4o`）。

### 步驟 3：使用 `az login` 登入 Azure

所有 notebook 都使用 **`AzureCliCredential`** 進行驗證 — 無需管理 API 金鑰。這需要你透過 Azure CLI 登入。

1. **安裝 Azure CLI**（如尚未安裝）：[aka.ms/installazurecli](https://aka.ms/installazurecli)

2. **登入**，執行下列命令：

    ```bash|powershell
    az login
    ```

    或者如果你在遠端/Codespace 環境且沒有瀏覽器：

    ```bash|powershell
    az login --use-device-code
    ```

3. 如有提示，**選擇你的訂閱** — 選擇包含你 Foundry 專案的訂閱。

4. **確認** 已登入：

    ```bash|powershell
    az account show
    ```

> **為何使用 `az login`？** Notebook 使用 azure-identity 套件的 `AzureCliCredential` 進行驗證。這代表你的 Azure CLI 工作階段會提供憑證 — 不需要在 `.env` 檔案中放置 API 金鑰或祕密。這是一項[安全最佳實務](https://learn.microsoft.com/azure/developer/ai/keyless-connections)。

### 步驟 4：建立你的 `.env` 檔案

複製範例檔案：

```bash
# zsh/bash
cp .env.example .env
```

```powershell
# PowerShell
Copy-Item .env.example .env
```

開啟 `.env` 並填入以下兩個數值：

```env
AZURE_AI_PROJECT_ENDPOINT=https://<your-project>.services.ai.azure.com/api/projects/<your-project-id>
AZURE_AI_MODEL_DEPLOYMENT_NAME=gpt-4o
```

| 變數 | 在哪裡找到 |
|----------|-----------------|
| `AZURE_AI_PROJECT_ENDPOINT` | Foundry 入口網站 → 你的專案 → **Overview** 頁面 |
| `AZURE_AI_MODEL_DEPLOYMENT_NAME` | Foundry 入口網站 → **Models + Endpoints** → 你已部署模型的名稱 |

大多數課程就是這樣！Notebook 會自動透過你的 `az login` 工作階段進行驗證。

### 步驟 5：安裝 Python 相依套件

```bash|powershell
pip install -r requirements.txt
```

我們建議在先前建立的虛擬環境中執行此步驟。

## 第 5 課的額外設定（Agentic RAG）

第 5 課使用 **Azure AI Search** 進行檢索增強生成。如果你打算執行該課程，請將這些變數加入你的 `.env` 檔案：

| 變數 | 在哪裡找到 |
|----------|-----------------|
| `AZURE_SEARCH_SERVICE_ENDPOINT` | Azure 入口網站 → 你的 **Azure AI Search** 資源 → **Overview** → URL |
| `AZURE_SEARCH_API_KEY` | Azure 入口網站 → 你的 **Azure AI Search** 資源 → **Settings** → **Keys** → 主要管理金鑰 |

## 第 6 與第 8 課的額外設定（GitHub Models）

第 6 與第 8 課的部分 notebook 使用 **GitHub Models**（而非 Azure AI Foundry）。如果你打算執行那些範例，請將下列變數加入你的 `.env` 檔案：

| 變數 | 在哪裡找到 |
|----------|-----------------|
| `GITHUB_TOKEN` | GitHub → **Settings** → **Developer settings** → **Personal access tokens** |
| `GITHUB_ENDPOINT` | 使用 `https://models.inference.ai.azure.com`（預設值） |
| `GITHUB_MODEL_ID` | 要使用的模型名稱（例如 `gpt-4o-mini`） |

## 第 8 課的額外設定（Bing Grounding 工作流程）

第 8 課的條件工作流程 notebook 使用透過 Azure AI Foundry 的 **Bing grounding**。若你打算執行該範例，請將此變數加入你的 `.env` 檔案：

| 變數 | 在哪裡找到 |
|----------|-----------------|
| `BING_CONNECTION_ID` | Azure AI Foundry 入口網站 → 你的專案 → **Management** → **Connected resources** → 你的 Bing 連線 → 複製 connection ID |

## 疑難排解

### macOS 上的 SSL 憑證驗證錯誤

如果你在 macOS 上遇到類似錯誤：

```plaintext
ssl.SSLCertVerificationError: [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: self-signed certificate in certificate chain
```

這是 Python 在 macOS 上已知的問題，系統 SSL 憑證未自動被信任。請按順序嘗試下列解決方法：

**選項 1：執行 Python 的 Install Certificates 腳本（建議）**

```bash
# 將 3.XX 替換為您已安裝的 Python 版本（例如 3.12 或 3.13）：
/Applications/Python\ 3.XX/Install\ Certificates.command
```

**選項 2：在 notebook 中使用 `connection_verify=False`（僅適用於 GitHub Models 的 notebook）**

在第 6 課的 notebook（`06-building-trustworthy-agents/code_samples/06-system-message-framework.ipynb`）中已包含註解掉的解法。建立 client 時取消註解 `connection_verify=False`：

```python
client = ChatCompletionsClient(
    endpoint=endpoint,
    credential=AzureKeyCredential(token),
    connection_verify=False,  # 如遇到憑證錯誤，請停用 SSL 驗證
)
```

> **⚠️ 警告：** 停用 SSL 驗證（`connection_verify=False`）會透過跳過憑證驗證來降低安全性。僅於開發環境中作為臨時解法使用，切勿在生產環境中使用。

**選項 3：安裝並使用 `truststore`**

```bash
pip install truststore
```

然後在 notebook 或腳本的最上方（在任何網路呼叫之前）加入下列內容：

```python
import truststore
truststore.inject_into_ssl()
```

## 卡在某處？

如果你在設定上遇到任何問題，請加入我們的 <a href="https://discord.gg/kzRShWzttr" target="_blank">Azure AI 社群 Discord</a> 或 <a href="https://github.com/microsoft/ai-agents-for-beginners/issues?WT.mc_id=academic-105485-koreyst" target="_blank">建立 issue</a>。

## 下一課

你現在已準備好執行本課程的程式碼。祝你在 AI Agents 的世界裡學習愉快！

[AI Agents 與代理使用案例簡介](../01-intro-to-ai-agents/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
免責聲明：
本文件已使用 AI 翻譯服務「Co-op Translator」（https://github.com/Azure/co-op-translator）進行翻譯。雖然我們力求準確，但請注意自動化翻譯可能包含錯誤或不準確之處。原始文件的母語版本應被視為具權威性的來源。對於重要資訊，建議採用專業人工翻譯。我們不對因使用本翻譯而產生的任何誤解或誤釋負責。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->