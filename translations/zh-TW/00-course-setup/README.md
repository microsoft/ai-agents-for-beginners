# 課程設定

## 簡介

本課程將介紹如何執行本課程的程式碼範例。

## 加入其他學習者並獲得協助

在您開始複製您的資料庫之前，請加入 [AI Agents For Beginners Discord 頻道](https://aka.ms/ai-agents/discord)，以獲取任何設定上的協助、課程相關問題或與其他學習者交流。

## 複製或分叉此資料庫

請先複製或分叉 GitHub 儲存庫。這將建立您自己的課程材料版本，使您能執行、測試及調整程式碼！

您可以點擊連結 <a href="https://github.com/microsoft/ai-agents-for-beginners/fork" target="_blank">分叉儲存庫</a> 來完成此動作

您現在應該擁有以下連結中的課程分叉版本：

![分叉儲存庫](../../../translated_images/zh-TW/forked-repo.33f27ca1901baa6a.webp)

### 淺層複製（建議用於工作坊 / Codespaces）

  > 如果您下載完整歷史紀錄和所有檔案，整個儲存庫可能會很大（約 3 GB）。若僅參加工作坊或只需部分課程資料夾，淺層複製（或稀疏複製）透過截斷歷史和/或跳過 blob，避免大部分下載量。

#### 快速淺層複製 — 最小歷史紀錄，所有檔案

請將下面指令中 `<your-username>` 替換成您的分叉 URL（或如果您願意，使用上游 URL）。

複製最新提交歷史紀錄（下載較小）：

```bash|powershell
git clone --depth 1 https://github.com/<your-username>/ai-agents-for-beginners.git
```

複製特定分支：

```bash|powershell
git clone --depth 1 --branch <branch-name> https://github.com/<your-username>/ai-agents-for-beginners.git
```

#### 部分（稀疏）複製 — 最小 blob + 只取指定資料夾

此方法使用部分複製與稀疏檢出（需要 Git 2.25+，建議使用支持部分複製的新版 Git）：

```bash|powershell
git clone --depth 1 --filter=blob:none --sparse https://github.com/<your-username>/ai-agents-for-beginners.git
```

進入儲存庫資料夾：

```bash|powershell
cd ai-agents-for-beginners
```

然後指定您想要的資料夾（下方範例示範兩個資料夾）：

```bash|powershell
git sparse-checkout set 00-course-setup 01-intro-to-ai-agents
```

複製並確認檔案後，如果您只需要檔案並想釋放空間（無須 git 歷史），請刪除儲存庫元資料（💀不可逆—將失去所有 Git 功能：無法提交、拉取、推送或存取歷史）。

```bash
# zsh/bash
rm -rf .git
```

```powershell
# PowerShell
Remove-Item -Recurse -Force .git
```

#### 使用 GitHub Codespaces（建議避免本機大下載）

- 透過 [GitHub 使用者介面](https://github.com/codespaces)為此儲存庫建立一個新的 Codespace。  

- 在新建立的 Codespace 終端機中，執行上述其中一個淺層/稀疏複製指令，將您需要的課程資料夾帶入 Codespace 工作空間。
- 選用：在 Codespaces 中複製後，刪除 .git 以回收更多空間（請參閱上述移除指令）。
- 注意：如果您偏好直接於 Codespaces 開啟儲存庫（無需額外複製），請注意 Codespaces 將構建 devcontainer 環境，且可能仍配置超過您所需資源。於新 Codespace 中複製淺層版本，能讓您更好控管磁碟使用。

#### 小技巧

- 若想編輯/提交，務必用您的分叉網址替換複製 URL。
- 若日後需要更多歷史或檔案，可以取得它們或調整稀疏檢出來包含其他資料夾。

## 執行程式碼

本課程提供一系列 Jupyter 筆記本，帶您動手實作 AI Agent 的建置。

程式碼範例使用 **Microsoft Agent Framework (MAF)** 與 `FoundryChatClient`，此用戶端透過 **Microsoft Foundry** 連接至 **Microsoft Foundry Agent Service V2**（即 Responses API）。

所有 Python 筆記本皆標註為 `*-python-agent-framework.ipynb`。

## 環境需求

- Python 3.12 以上
  - <strong>注意</strong>：如果尚未安裝 Python3.12，請務必安裝。接著使用 python3.12 建立虛擬環境，以確保安裝 requirements.txt 中的正確版本。
  
    > 範例

    建立 Python 虛擬環境資料夾：

    ```bash|powershell
    python -m venv venv
    ```

    然後啟用虛擬環境：

    ```bash
    # zsh/bash
    source venv/bin/activate
    ```
  
    ```dos
    # Command Prompt for Windows
    venv\Scripts\activate
    ```

- .NET 10 以上：使用 .NET 範例程式碼時，請安裝 [.NET 10 SDK](https://dotnet.microsoft.com/download/dotnet/10.0) 或更高版本。接著檢查已安裝的 SDK 版本：

    ```bash|powershell
    dotnet --list-sdks
    ```

- **Azure CLI** — 用於認證。請從 [aka.ms/installazurecli](https://aka.ms/installazurecli) 安裝。
- **Azure 訂閱** — 用於存取 Microsoft Foundry 和 Microsoft Foundry Agent Service。
- **Microsoft Foundry 專案** — 需有已部署模型的專案（如 `gpt-5-mini`）。詳見下方 [步驟 1](#步驟-1：建立-microsoft-foundry-專案)。

本儲存庫根目錄中包含 `requirements.txt`，列出了執行程式碼範例所需的所有 Python 套件。

您可於儲存庫根目錄的終端機執行下列指令安裝套件：

```bash|powershell
pip install -r requirements.txt
```

建議建立 Python 虛擬環境，以避免衝突和問題。

## 設定 VSCode

請確定 VSCode 使用正確的 Python 版本。

![image](https://github.com/user-attachments/assets/a85e776c-2edb-4331-ae5b-6bfdfb98ee0e)

## 設定 Microsoft Foundry 與 Microsoft Foundry Agent Service

### 步驟 1：建立 Microsoft Foundry 專案

您需要一個 Microsoft Foundry **hub** 與 <strong>專案</strong>，且專案內需部署模型，方能執行筆記本。

1. 前往 [ai.azure.com](https://ai.azure.com) 並用 Azure 帳戶登入。
2. 建立 **hub**（或使用現有 hub）。參閱：[Hub 資源概覽](https://learn.microsoft.com/azure/ai-foundry/concepts/ai-resources)。
3. 在 hub 中建立 <strong>專案</strong>。
4. 從 **Models + Endpoints** → **Deploy model** 部署模型（如 `gpt-5-mini`）。

### 步驟 2：取得專案端點與模型部署名稱

於 Microsoft Foundry 入口網站的專案中：

- <strong>專案端點</strong> — 前往 **Overview** 頁面並複製端點 URL。

![專案連接字串](../../../translated_images/zh-TW/project-endpoint.8cf04c9975bbfbf1.webp)

- <strong>模型部署名稱</strong> — 前往 **Models + Endpoints**，選擇您的已部署模型，並記下 **Deployment name**（如 `gpt-5-mini`）。

### 步驟 3：使用 `az login` 登入 Azure

所有筆記本均使用 **`AzureCliCredential`** 進行認證，無需管理 API 金鑰。此方式要求您透過 Azure CLI 登入。

1. 若尚未安裝 **Azure CLI**，請先安裝：[aka.ms/installazurecli](https://aka.ms/installazurecli)

2. 執行以下指令登入：

    ```bash|powershell
    az login
    ```

    若您使用遠端／Codespace 環境且無瀏覽器：

    ```bash|powershell
    az login --use-device-code
    ```

3. 如系統提示，選擇您的訂閱 — 選擇包含 Foundry 專案的訂閱。

4. 驗證您已登入：

    ```bash|powershell
    az account show
    ```

> **為何要使用 `az login`？** 筆記本使用 `azure-identity` 套件的 `AzureCliCredential` 進行認證，意即您的 Azure CLI 工作階段提供憑證 — 不需在 `.env` 檔案中放置 API 金鑰或密鑰。這是 [安全最佳實踐](https://learn.microsoft.com/azure/developer/ai/keyless-connections)。

### 步驟 4：建立你的 `.env` 檔案

複製範例檔：

```bash
# zsh/bash
cp .env.example .env
```

```powershell
# PowerShell
Copy-Item .env.example .env
```

打開 `.env`，填入以下兩個數值：

```env
AZURE_AI_PROJECT_ENDPOINT=https://<your-project>.services.ai.azure.com/api/projects/<your-project-id>
AZURE_AI_MODEL_DEPLOYMENT_NAME=gpt-5-mini
```

| 變數 | 位置 |
|----------|-----------------|
| `AZURE_AI_PROJECT_ENDPOINT` | Foundry 入口網站 → 您的專案 → **Overview** 頁面 |
| `AZURE_AI_MODEL_DEPLOYMENT_NAME` | Foundry 入口網站 → **Models + Endpoints** → 您已部署模型的名稱 |

大部分課程就這樣完成了！筆記本會自動透過您的 `az login` 工作階段認證。

### 步驟 5：安裝 Python 相依套件

```bash|powershell
pip install -r requirements.txt
```

建議於先前建立的虛擬環境中執行此作業。

## 第五課額外設定（Agentic RAG）

第五課使用 **Azure AI Search** 來進行檢索增強生成。如果您計劃執行該課程，請將以下變數加入 `.env` 檔案：

| 變數 | 位置 |
|----------|-----------------|
| `AZURE_SEARCH_SERVICE_ENDPOINT` | Azure 入口網站 → 您的 **Azure AI Search** 資源 → **Overview** → URL |
| `AZURE_SEARCH_API_KEY` | Azure 入口網站 → 您的 **Azure AI Search** 資源 → **Settings** → **Keys** → 主要管理金鑰 |

## 直接呼叫 Azure OpenAI 的課程額外設定（第 6 與 8 課）

部分第 6 與 8 課的筆記本直接呼叫 **Azure OpenAI**（使用 **Responses API**），而非透過 Microsoft Foundry 專案。這些範例之前使用 GitHub 模型，該服務已停用（將於 2026 年 7 月退休），且不支援 Responses API。如果您要執行這些範例，請將以下變數加入 `.env` 檔案：

| 變數 | 位置 |
|----------|-----------------|
| `AZURE_OPENAI_ENDPOINT` | Azure 入口網站 → 您的 **Azure OpenAI** 資源 → **Keys and Endpoint** → 端點（例如 `https://<your-resource>.openai.azure.com`） |
| `AZURE_OPENAI_DEPLOYMENT` | 您已部署，且支援 Responses API 的模型名稱（例如 `gpt-5-mini`） |
| `AZURE_OPENAI_API_KEY` | 選用 — 僅在您使用基於金鑰的認證，非 `az login` / Entra ID 時填寫 |

> Responses API 使用穩定的 `/openai/v1/` 端點，因此不需指定 `api-version`。請使用 `az login` 登入，以利用無金鑰的 Entra ID 認證。

## 替代提供者：MiniMax（OpenAI 相容）

[MiniMax](https://platform.minimaxi.com/) 提供支援最大 204K 代幣的長上下文模型，透過 OpenAI 相容 API。由於 Microsoft Agent Framework 的 `OpenAIChatClient` 可使用任何 OpenAI 相容端點，您可以將 MiniMax 作為 Azure OpenAI 或 OpenAI 的無縫替代方案。

請將以下變數加入 `.env` 檔案：

| 變數 | 位置 |
|----------|-----------------|
| `MINIMAX_API_KEY` | [MiniMax 平台](https://platform.minimaxi.com/) → API 金鑰 |
| `MINIMAX_BASE_URL` | 使用 `https://api.minimax.io/v1`（預設值） |
| `MINIMAX_MODEL_ID` | 要使用的模型名稱（例如 `MiniMax-M3`） |

<strong>範例模型</strong>：`MiniMax-M3`（推薦）、`MiniMax-M2.7`、`MiniMax-M2.7-highspeed`（較快回應）。模型名稱及可用性會隨時間變動，且特定模組的使用權限可能依您的帳戶或地區而異—請至 [MiniMax 平台](https://platform.minimaxi.com/) 查詢最新列表。若您的帳戶無法使用 `MiniMax-M3`，請將 `MINIMAX_MODEL_ID` 設為您可用的模型（例如 `MiniMax-M2.7`）。

使用 `OpenAIChatClient` 的程式碼範例（如第 14 課飯店訂房工作流程）會在設定了 `MINIMAX_API_KEY` 時，偵測並自動使用您的 MiniMax 配置。

## 替代提供者：Foundry Local（本機執行模型）

[Foundry Local](https://foundrylocal.ai) 是輕量級執行環境，可完全在您自己的機器上下載、管理與提供語言模型服務，透過 OpenAI 相容 API — 無需雲端、Azure 訂閱或 API 金鑰。適合離線開發、無雲成本實驗或需要資料本機存放的場合。

由於 Microsoft Agent Framework 的 `OpenAIChatClient` 可使用任意 OpenAI 相容端點，Foundry Local 正是 Azure OpenAI 的本機替代方案。

**1. 安裝 Foundry Local**

```bash
# Windows 作業系統
winget install Microsoft.FoundryLocal

# macOS 作業系統
brew install foundrylocal
```

**2. 下載並執行模型**（此步驟同時啟動本地服務）：

```bash
foundry model list          # 查看可用模型
foundry model run phi-4-mini
```

**3. 安裝用於偵測本地端點的 Python SDK：**

```bash
pip install foundry-local-sdk
```

**4. 指向 Microsoft Agent Framework 使用您的本地模型：**

```python
from foundry_local import FoundryLocalManager
from agent_framework.openai import OpenAIChatClient

# 下載（如有需要）並在本地提供模型，然後發現端點/埠口。
manager = FoundryLocalManager("phi-4-mini")

chat_client = OpenAIChatClient(
    base_url=manager.endpoint,      # 例如 http://localhost:<port>/v1
    api_key=manager.api_key,        # 對於 Foundry Local，總是「不需要」
    model_id=manager.get_model_info("phi-4-mini").id,
)

agent = chat_client.as_agent(
    name="LocalAgent",
    instructions="You are a helpful assistant running fully on-device.",
)
```

> **注意：** Foundry Local 提供 OpenAI 相容的 **Chat Completions** 端點，適合本機開發與離線使用。若需完整 **Responses API** 功能（有狀態對話、深入工具編排、代理式開發），請指向 **Azure OpenAI** 或 **Microsoft Foundry** 專案，如課程示範。詳情請參閱 [Foundry Local 文件](https://foundrylocal.ai) 以查看現行模型目錄及平台支援。

## 第八課額外設定（Bing Grounding 工作流程）


第 8 課中的條件工作流程筆記本使用透過 Microsoft Foundry 的 **Bing 根基**。如果您計劃執行該範例，請將此變數添加到您的 `.env` 檔案中：

| 變數 | 位置 |
|----------|-----------------|
| `BING_CONNECTION_ID` | Microsoft Foundry 入口網站 → 您的專案 → <strong>管理</strong> → <strong>已連接資源</strong> → 您的 Bing 連線 → 複製連線 ID |

## 疑難排解

### macOS 上的 SSL 憑證驗證錯誤

如果您在 macOS 上遇到類似以下錯誤：

```plaintext
ssl.SSLCertVerificationError: [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: self-signed certificate in certificate chain
```

這是在 macOS 上 Python 的已知問題，系統 SSL 憑證未自動信任。請依序嘗試以下解決方案：

**方案一：執行 Python 的 Install Certificates 腳本（推薦）**

```bash
# 將 3.XX 替換為您安裝的 Python 版本（例如，3.12 或 3.13）：
/Applications/Python\ 3.XX/Install\ Certificates.command
```

**方案二：在您的筆記本中使用 `connection_verify=False`（僅適用於 GitHub Models 筆記本）**

在第 6 課的筆記本 (`06-building-trustworthy-agents/code_samples/06-system-message-framework.ipynb`) 中，已包含註解掉的變通方法。建立 client 時解除註解 `connection_verify=False`：

```python
client = ChatCompletionsClient(
    endpoint=endpoint,
    credential=AzureKeyCredential(token),
    connection_verify=False,  # 如果遇到證書錯誤，請禁用 SSL 驗證
)
```

> **⚠️ 警告：** 禁用 SSL 驗證（`connection_verify=False`）會因跳過憑證驗證而降低安全性。僅在開發環境中作為臨時變通方法使用，切勿在生產環境中使用。

**方案三：安裝並使用 `truststore`**

```bash
pip install truststore
```

然後在筆記本或腳本的最上方（在進行任何網路呼叫之前）加入以下內容：

```python
import truststore
truststore.inject_into_ssl()
```

## 卡住了嗎？

如果您在執行設定時有任何問題，歡迎加入我們的 <a href="https://discord.gg/kzRShWzttr" target="_blank">Azure AI Community Discord</a> 或 <a href="https://github.com/microsoft/ai-agents-for-beginners/issues?WT.mc_id=academic-105485-koreyst" target="_blank">提出問題</a>。

## 下一課

您現在已準備好執行本課程的程式碼。祝您學習 AI 代理人的世界愉快！ 

[Introduction to AI Agents and Agent Use Cases](../01-intro-to-ai-agents/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責聲明**：
此文件已使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。雖然我們努力追求準確性，但請注意自動翻譯可能包含錯誤或不準確之處。原始文件的母語版本應視為權威來源。對於關鍵資訊，建議採用專業人工翻譯。我們不對因使用此翻譯所產生的任何誤解或誤譯承擔責任。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->