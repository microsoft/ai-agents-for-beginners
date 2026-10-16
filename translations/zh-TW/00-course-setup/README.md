# 課程設定

## 介紹

本課程將介紹如何執行本課程的程式碼範例。

## 加入其他學習者並取得協助

在開始複製您的儲存庫之前，請加入 [AI Agents For Beginners Discord 頻道](https://aka.ms/ai-agents/discord)，以便獲得設定方面的協助、課程相關問題，或與其他學習者交流。

## 複製或分叉此儲存庫

開始之前，請複製或分叉 GitHub 儲存庫。這會建立屬於您自己的課程材料版本，讓您能執行、測試並調整程式碼！

您可以點擊此連結 <a href="https://github.com/microsoft/ai-agents-for-beginners/fork" target="_blank">分叉此儲存庫</a>

您現在應該擁有此課程的分叉版本，連結如下：

![Forked Repo](../../../translated_images/zh-TW/forked-repo.33f27ca1901baa6a.webp)

### 淺層複製（推薦用於工作坊 / Codespaces）

  > 下載完整歷史與所有檔案時，完整儲存庫可能非常大（約 3 GB）。如果您只參加工作坊或僅需要少數課程資料夾，淺層複製（或稀疏複製）將大幅減少下載量。

#### 快速淺層複製 — 最少歷史、所有檔案

請將下列指令中的 `<your-username>` 替換為您的分叉 URL（或您選擇的上游 URL）。

僅複製最新提交歷史（下載較小）：

```bash
git clone --depth 1 https://github.com/<your-username>/ai-agents-for-beginners.git
```

複製特定分支：

```bash
git clone --depth 1 --branch <branch-name> https://github.com/<your-username>/ai-agents-for-beginners.git
```

#### 部分（稀疏）複製 — 最少 blob + 僅選擇資料夾

使用部分複製與稀疏檢出（需 Git 2.25+，推薦使用支援部分複製的新版 Git）：

```bash
git clone --depth 1 --filter=blob:none --sparse https://github.com/<your-username>/ai-agents-for-beginners.git
```

進入儲存庫資料夾：

```bash
cd ai-agents-for-beginners
```

指定您需要的資料夾（下面範例顯示兩個資料夾）：

```bash
git sparse-checkout set 00-course-setup 01-intro-to-ai-agents
```

複製並驗證檔案後，如果您只需要檔案且想釋放空間（無 Git 歷史），請刪除儲存庫元資料（💀不可復原 — 您將失去所有 Git 功能）：

```bash
# zsh/bash
rm -rf .git
```

```powershell
# PowerShell
Remove-Item -Recurse -Force .git
```

#### 使用 GitHub Codespaces（推薦避免本機大量下載）

- 透過 [GitHub UI](https://github.com/codespaces) 為此儲存庫建立新的 Codespace。  

- 在新建立的 Codespace 終端機中，執行上方任一淺層/稀疏複製指令，將您需要的課程資料夾帶入 Codespace 工作區。
- 選用：在 Codespaces 中複製後，可移除 .git 以回收額外空間（請參考上述移除指令）。
- 注意：如果您選擇直接在 Codespaces 中開啟儲存庫（無需額外複製），Codespaces 將建立 devcontainer 環境，且可能仍會配置超出您所需的內容。

#### 小技巧

- 若要編輯/提交，請務必把複製 URL 替換為您的分叉版本。
- 若您日後需要更多歷史或檔案，可從遠端下載或調整稀疏檢出設定，加入其他資料夾。

## 執行程式碼

課程提供一系列 Jupyter 筆記本，您可以操作這些筆記本，實際體驗建立 AI Agents。

程式範例使用 **Microsoft Agent Framework (MAF)** 搭配 `FoundryChatClient`，透過 **Microsoft Foundry** 連線至 **Microsoft Foundry Agent Service V2**（也稱為 Responses API）。

所有 Python 筆記本皆標示為 `*-python-agent-framework.ipynb`。

## 系統需求

- Python 3.12+
  - <strong>注意</strong>：若尚未安裝 Python3.12，請先安裝。接著使用 python3.12 建立虛擬環境，確保依照 requirements.txt 安裝正確版本的套件。
  
    >範例

    建立 Python 虛擬環境目錄：

    ```bash
    python -m venv venv
    ```

    接著啟動虛擬環境：

    ```bash
    # zsh/bash
    source venv/bin/activate
    ```
  
    ```dos
    # Command Prompt for Windows
    venv\Scripts\activate
    ```

- .NET 10+：若程式碼範例使用 .NET，請安裝 [.NET 10 SDK](https://dotnet.microsoft.com/download/dotnet/10.0) 或更新版本。然後查看已安裝的 .NET SDK 版本：

    ```bash
    dotnet --list-sdks
    ```

- **Azure CLI** — 必須安裝以執行認證。請從 [aka.ms/installazurecli](https://aka.ms/installazurecli) 安裝。
- **Azure 訂閱** — 用於存取 Microsoft Foundry 及 Microsoft Foundry Agent Service。
- **Microsoft Foundry 專案** — 需要有部署模型的專案（例如 `gpt-5-mini`）。詳見下方 [步驟 1](#第一步：建立-microsoft-foundry-專案)。

此儲存庫根目錄已有 `requirements.txt` 檔案，其中列出執行程式碼所需的所有 Python 套件。

您可在儲存庫根目錄的終端機執行以下指令安裝：

```bash
pip install -r requirements.txt
```

建議建立 Python 虛擬環境，以免發生衝突與問題。

## 設定 VSCode

請確保您在 VSCode 使用正確版本的 Python。

![image](https://github.com/user-attachments/assets/a85e776c-2edb-4331-ae5b-6bfdfb98ee0e)

## 設定 Microsoft Foundry 與 Microsoft Foundry Agent Service

### 第一步：建立 Microsoft Foundry 專案

要執行筆記本，您需要具備已部署模型的 Microsoft Foundry **hub** 與 <strong>專案</strong>。

1. 前往 [ai.azure.com](https://ai.azure.com) 並使用您的 Azure 帳號登入。
2. 建立一個 **hub**（或使用既有的）。參考：[Hub 資源概覽](https://learn.microsoft.com/azure/ai-foundry/concepts/ai-resources)。
3. 在 hub 中建立一個 <strong>專案</strong>。
4. 從 **Models + Endpoints** → **Deploy model** 部署一個模型（例如 `gpt-5-mini`）。

### 第二步：取得專案端點與模型部署名稱

在您 Microsoft Foundry 頁面專案中：

- <strong>專案端點</strong> — 前往 **Overview** 頁面並複製端點 URL。

![Project Connection String](../../../translated_images/zh-TW/project-endpoint.8cf04c9975bbfbf1.webp)

- <strong>模型部署名稱</strong> — 前往 **Models + Endpoints**，選擇已部署的模型，並紀錄 **Deployment name**（如 `gpt-5-mini`）。

### 第三步：使用 `az login` 登入 Azure

大多數筆記本通過您的 **Azure CLI 登入** 認證 — 使用來自 `azure-identity` 套件的 `AzureCliCredential` 或 `DefaultAzureCredential`（兩者都會挑選您的 `az login` 會話） — 因此不需要 API 金鑰。有部分課程及選用的整合部分會使用 API 金鑰；請查看每堂課前置條件，以確認是否需要額外環境變數。這需要您先登入 Azure CLI。

1. 若您尚未安裝 Azure CLI，請參考 [aka.ms/installazurecli](https://aka.ms/installazurecli)

2. 執行以下命令登入：

    ```bash
    az login
    ```

    若您處於沒有瀏覽器的遠端或 Codespace 環境：

    ```bash
    az login --use-device-code
    ```

3. 出現提示時選擇您的訂閱 — 請選擇包含您的 Foundry 專案的訂閱。

4. 確認您已登入：

    ```bash
    az account show
    ```

> **為什麼使用 `az login`？** 筆記本使用 `azure-identity` 套件的 `AzureCliCredential`（或同樣會挑選您的 Azure CLI 登入的 `DefaultAzureCredential`）進行認證。這代表 Azure CLI 會話提供憑證 — 您的 `.env` 檔案中不需 API 金鑰或密鑰。這是[安全最佳實踐](https://learn.microsoft.com/azure/developer/ai/keyless-connections)。

### 第四步：建立您的 `.env` 檔案

複製範例檔案：

```bash
# zsh/bash
cp .env.example .env
```

```powershell
# PowerShell
Copy-Item .env.example .env
```

開啟 `.env`，並填入以下兩個數值：

```env
AZURE_AI_PROJECT_ENDPOINT=https://<your-project>.services.ai.azure.com/api/projects/<your-project-id>
AZURE_AI_MODEL_DEPLOYMENT_NAME=gpt-5-mini
```

| 變數名稱 | 取得位置 |
|----------|-----------------|
| `AZURE_AI_PROJECT_ENDPOINT` | Foundry 入口網站 → 您的專案 → **Overview** 頁面 |
| `AZURE_AI_MODEL_DEPLOYMENT_NAME` | Foundry 入口網站 → **Models + Endpoints** → 您部署模型的名稱 |

大多數課程就這樣完成！筆記本可自動透過您的 `az login` 會話進行認證。

### 第五步：安裝 Python 依賴

```bash
pip install -r requirements.txt
```

建議在先前建立的虛擬環境中執行此命令。

## 選用設定：Azure AI 搜尋（第 5 和 16 課）

第 5 課（Agentic RAG）和第 16 課筆記本預設使用<strong>記憶體內知識庫</strong>即可執行 — 無需額外 Azure 資源。若您想使用真實的 **Azure AI 搜尋** 索引，請注意第 16 課筆記本目前使用基於金鑰的認證：僅當同時設定 `AZURE_SEARCH_SERVICE_ENDPOINT` <strong>和</strong> `AZURE_SEARCH_API_KEY` 時，才會從記憶體搜尋切換到 Azure AI 搜尋；否則將保持記憶體搜尋；因此，要針對真實索引執行，必須同時設定管理者金鑰。針對您自己的產品程式碼，建議使用 Microsoft Entra ID (RBAC) 的無金鑰認證，與本課程其他地方使用的 `az login` 流程一致。

以下 RBAC 步驟適用於設定指引範例及您自己的程式碼。它們不會啟用第 16 課筆記本的無金鑰認證；第 16 課仍需同時設定端點及管理者金鑰才能使用 Azure AI 搜尋。

1. <strong>啟用搜尋服務的角色存取控制</strong>：

    ```bash
    az search service update --name <service-name> --resource-group <resource-group> --auth-options aadOrApiKey
    ```

2. <strong>指派您自己所需的角色</strong>（用於建立/載入索引及查詢）：

    ```bash
    az role assignment create --assignee <your-user-or-principal-id> --role "Search Service Contributor" --scope $(az search service show -g <resource-group> -n <service-name> --query id -o tsv)
    az role assignment create --assignee <your-user-or-principal-id> --role "Search Index Data Contributor" --scope $(az search service show -g <resource-group> -n <service-name> --query id -o tsv)
    ```

3. **在 `.env` 檔裡新增端點**：

| 變數名稱 | 取得位置 |
|----------|-----------------|
| `AZURE_SEARCH_SERVICE_ENDPOINT` | Azure 入口網站 → 您的 **Azure AI 搜尋** 資源 → **Overview** → URL |
| `AZURE_SEARCH_API_KEY` | 必須（和端點一起使用）以在第 16 課筆記本啟用 Azure AI 搜尋，該筆記本使用基於金鑰的認證。Azure 入口網站 → **Settings** → **Keys** → 主要管理金鑰 |

> **為什麼要使用無金鑰認證？** 管理金鑰授予搜尋服務完全寫入權限，且可能透過 `.env` 檔外洩。使用 RBAC 時，會用您的 `az login` 身份 — 與課程中筆記本採用的 Keyless Entra ID 模式相同（透過 `AzureCliCredential` / `DefaultAzureCredential`）。詳見 [使用角色存取連接 Azure AI 搜尋](https://learn.microsoft.com/azure/search/search-security-rbac)。

請參閱 [Azure AI 搜尋設定指南](./AzureSearch.md)，以取得 Python 與 .NET 的完整索引建立範例。

## 需要額外設定、會直接呼叫 Azure OpenAI 的課程（第 6 及 8 課）

第 6 及 8 課的部分筆記本會直接利用 **Azure OpenAI**（使用 **Responses API**），而非透過 Microsoft Foundry 專案執行。這些範例先前使用 GitHub Models（已停用且不支援 Responses API）。請在 `.env` 檔案增加下列變數：

| 變數名稱 | 取得位置 |
|----------|-----------------|
| `AZURE_OPENAI_ENDPOINT` | Azure 入口網站 → 您的 **Azure OpenAI** 資源 → **Keys and Endpoint** → Endpoint（例如 `https://<your-resource>.openai.azure.com`） |
| `AZURE_OPENAI_DEPLOYMENT` | 您部署支援 Responses API 模型的名稱（例如 `gpt-5-mini`） |
| `AZURE_OPENAI_API_KEY` | 選用 — 僅於使用基於金鑰的認證而非 `az login` / Entra ID 時需設定 |

> Responses API 使用穩定的 `/openai/v1/` 端點，因此不需要 `api-version`。請用 `az login` 登入以使用無金鑰 Entra ID 認證。

## 替代供應商：MiniMax（OpenAI 相容）

[MiniMax](https://platform.minimaxi.com/) 透過 OpenAI 相容 API 提供長上下文模型（最高支援 204K 代幣）。由於 Microsoft Agent Framework 的 `OpenAIChatClient` 可與任何 OpenAI 相容端點搭配使用，您可以針對使用 `OpenAIChatClient` 的課程，使用 MiniMax 作為可替代的即插即用方案。

在 `.env` 檔案新增以下變數：

| 變數名稱 | 取得位置 |
|----------|-----------------|
| `MINIMAX_API_KEY` | [MiniMax 平台](https://platform.minimaxi.com/) → API 金鑰 |
| `MINIMAX_BASE_URL` | 使用 `https://api.minimax.io/v1` （預設值） |
| `MINIMAX_MODEL_ID` | 要使用的模型名稱（例如 `MiniMax-M3`） |

<strong>範例模型</strong>：`MiniMax-M3`（推薦）、`MiniMax-M2.7`、`MiniMax-M2.7-highspeed`（反應更快）。模型名稱和可用性可能隨時間變動，且某些模型的存取權可能取決於您的帳號。

使用 `OpenAIChatClient` 的程式範例（如第 14 課飯店訂房流程）在設定了 `MINIMAX_API_KEY` 後，會自動偵測並使用您的 MiniMax 設定。


## 替代提供者：Novita AI（OpenAI 相容）

[Novita AI](https://novita.ai/llm-api) 提供一個 OpenAI 相容的 API，支援開放原始碼和前沿 LLM（DeepSeek、Llama、Qwen 等）。由於 Microsoft Agent Framework 的 `OpenAIChatClient` 可以與任何 OpenAI 相容的端點合作，因此你可以使用 Novita AI 作為 Azure OpenAI 或 OpenAI 的直接替代方案。

將這些變數加入你的 `.env` 檔案：

| 變數 | 來源 |
|----------|-----------------|
| `NOVITA_API_KEY` | [Novita AI 控制台](https://novita.ai/settings/key-management) → API 金鑰 |
| `NOVITA_BASE_URL` | 使用 `https://api.novita.ai/openai/v1`（預設值） |
| `NOVITA_MODEL_ID` | 要使用的模型名稱（例如 `moonshotai/kimi-k3`） |

<strong>範例模型</strong>：`moonshotai/kimi-k3`、`zai-org/glm-5.2`、`deepseek/deepseek-v4-flash-0731`。Novita AI 也托管許多其他開放原始碼模型家族（Llama、Qwen、GLM 等）——請參考 [Novita AI 模型庫](https://novita.ai/llm-api) 了解目前可供使用的模型及其模型 ID。

目前的範例不會自動使用 `NOVITA_*` 變數。要使用 Novita AI，請在執行的範例中建構 `OpenAIChatClient` 時明確傳入這些值。

## 替代提供者：Foundry Local（本機運行模型）

[Foundry Local](https://foundrylocal.ai) 是一個輕量的執行環境，可下載、管理並提供語言模型，<strong>完全在你的本機電腦上執行</strong>，透過 OpenAI 相容的 API —— 不需要雲端。

由於 Microsoft Agent Framework 的 `OpenAIChatClient` 能配合任何 OpenAI 相容端點，Foundry Local 是 Azure OpenAI 的本機替代方案。

**1. 安裝 Foundry Local**

```bash
# Windows 作業系統
winget install Microsoft.FoundryLocal

# macOS 作業系統
brew install foundrylocal
```

**2. 下載並執行模型**（這也會啟動本機服務）：

```bash
foundry model list          # 查看可用模型
foundry model run phi-4-mini
```

**3. 安裝 Python SDK**，用於偵測本機端點：

```bash
pip install foundry-local-sdk
```

**4. 將 Microsoft Agent Framework 指向本機模型：**

```python
from foundry_local import FoundryLocalManager
from agent_framework.openai import OpenAIChatClient

# 下載（如有需要）並在本地提供模型，然後發現端點/埠口。
manager = FoundryLocalManager("phi-4-mini")

chat_client = OpenAIChatClient(
    base_url=manager.endpoint,      # 例如 http://localhost:<port>/v1
    api_key=manager.api_key,        # Foundry Local 永遠是「不需要」
    model_id=manager.get_model_info("phi-4-mini").id,
)

agent = chat_client.as_agent(
    name="LocalAgent",
    instructions="You are a helpful assistant running fully on-device.",
)
```

> **注意：** Foundry Local 開放 OpenAI 相容的 **Chat Completions** 端點。用於本地開發及離線場景。欲使用完整的 **Responses API** 功能集（如有狀態的對話等），請使用 Azure OpenAI 或 Microsoft Foundry 專案。

## 第 8 課額外設定（Bing 固定流程）

第 8 課的條件式流程筆記本使用 Microsoft Foundry 的 **Bing 固定** 功能。如果你打算執行該範例，請在你的 `.env` 檔案中新增此變數：

| 變數 | 來源 |
|----------|-----------------|
| `BING_CONNECTION_ID` | Microsoft Foundry 入口網站 → 你的專案 → <strong>管理</strong> → <strong>已連接資源</strong> → 你的 Bing 連線 → 複製連線 ID |

## 疑難排解

### macOS 上的 SSL 證書驗證錯誤

如果你在 macOS 遇到如下錯誤：

```plaintext
ssl.SSLCertVerificationError: [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: self-signed certificate in certificate chain
```

這是 Python 在 macOS 上已知的問題，系統 SSL 證書不會自動被信任。請按順序嘗試以下解決方案：

**選項 1：執行 Python 的安裝證書腳本（建議）**

```bash
# 將 3.XX 替換為你安裝的 Python 版本（例如，3.12 或 3.13）：
/Applications/Python\ 3.XX/Install\ Certificates.command
```

**選項 2：在筆記本中使用 `connection_verify=False`（僅限 GitHub Models 筆記本）**

在第 6 課的筆記本（`06-building-trustworthy-agents/code_samples/06-system-message-framework.ipynb`）中，已含括一個被註解掉的解決方法。當你遇到證書錯誤時，取消註解 `connection_verify=False`：

```python
client = ChatCompletionsClient(
    endpoint=endpoint,
    credential=AzureKeyCredential(token),
    connection_verify=False,  # 如果遇到憑證錯誤，請停用 SSL 驗證
)
```

> **⚠️ 警告：** 停用 SSL 驗證（`connection_verify=False`）會跳過證書檢查，降低安全性。僅在開發環境中作為暫時的解決方案使用，請勿在生產環境中使用。

**選項 3：安裝並使用 `truststore`**

```bash
pip install truststore
```

接著在你的筆記本或腳本的頂端、進行任何網路呼叫之前加入以下程式碼：

```python
import truststore
truststore.inject_into_ssl()
```

## 卡住了嗎？

如果你在執行此設定過程中有任何問題，歡迎加入我們的 <a href="https://discord.gg/kzRShWzttr" target="_blank">Azure AI 社群 Discord</a> 或 <a href="https://github.com/microsoft/ai-agents-for-beginners/issues?WT.mc_id=academic-105485-koreyst" target="_blank">提出 issue</a>。

## 下一課

你現在準備好執行本課程的程式碼。祝你在 AI Agents 的世界裡學習愉快！

[AI Agents 介紹與代理案例](../01-intro-to-ai-agents/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責聲明**：
此文件已使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。雖然我們努力追求準確性，但請注意自動翻譯可能包含錯誤或不準確之處。原始文件的母語版本應視為權威來源。對於關鍵資訊，建議採用專業人工翻譯。我們不對因使用此翻譯所產生的任何誤解或誤譯承擔責任。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->