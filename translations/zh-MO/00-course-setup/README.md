# 課程設定

## 簡介

本課程將涵蓋如何運行本課程的程式碼範例。

## 加入其他學習者並獲取幫助

在開始複製您的代碼庫之前，請加入 [AI Agents For Beginners Discord 頻道](https://aka.ms/ai-agents/discord)，以獲取設定幫助、課程相關問題，或與其他學習者互動。

## 複製或 Fork 此代碼庫

請先複製或 Fork GitHub 儲存庫。這樣您將擁有課程材料的個人版本，可以運行、測試和調整程式碼！

您可以點擊連結<a href="https://github.com/microsoft/ai-agents-for-beginners/fork" target="_blank">fork 此儲存庫</a>來完成這個動作。

您現在應該擁有本課程的 Fork 版本，位於以下連結：

![Forked Repo](../../../translated_images/zh-MO/forked-repo.33f27ca1901baa6a.webp)

### Shallow Clone（建議用於工作坊 / Codespaces）

  >當您下載完整的歷史紀錄和所有檔案時，完整儲存庫可能很大（約 3 GB）。如果您只參加工作坊或只需要幾個課程資料夾，淺層複製（或部分複製）會下載更少內容。

#### 快速淺層複製 — 最少歷史紀錄，下載所有檔案

請用您的 Fork URL（或您偏好的上游 URL）取代下方命令中的 `<your-username>`。

若只想複製最新的提交歷史（下載較小）：

```bash
git clone --depth 1 https://github.com/<your-username>/ai-agents-for-beginners.git
```

若想複製特定分支：

```bash
git clone --depth 1 --branch <branch-name> https://github.com/<your-username>/ai-agents-for-beginners.git
```

#### 部分（稀疏）複製 — 最少 blob 且只下載選定資料夾

使用部分複製和稀疏檢出（需要 Git 2.25+，且建議使用支援部分複製的現代 Git）：

```bash
git clone --depth 1 --filter=blob:none --sparse https://github.com/<your-username>/ai-agents-for-beginners.git
```

進入儲存庫資料夾：

```bash
cd ai-agents-for-beginners
```

然後指定您想要的資料夾（以下範例示範兩個資料夾）：

```bash
git sparse-checkout set 00-course-setup 01-intro-to-ai-agents
```

複製並驗證檔案之後，如果您只需要檔案且想釋放空間（沒有 git 歷史），請刪除儲存庫元資料（💀不可逆 — 會失去所有 Git 功能）：

```bash
# zsh/bash
rm -rf .git
```

```powershell
# PowerShell
Remove-Item -Recurse -Force .git
```

#### 使用 GitHub Codespaces（建議避免本地大型下載）

- 透過 [GitHub UI](https://github.com/codespaces) 為此儲存庫建立新的 Codespace。  

- 在新建 Codespace 的終端機中，執行上述淺層/稀疏複製命令之一，只帶入您需要的課程資料夾到 Codespace 工作區。
- 選用：在 Codespaces 內部複製後，移除 .git 以回收額外空間（參見上述移除指令）。
- 注意：若偏好直接在 Codespaces 開啟儲存庫（不另作複製），Codespaces 會建立 devcontainer 環境，可能仍會佔用超出需求的資源。

#### 小提示

- 如有意修改/提交，請務必用您的 Fork URL 替換複製連結。
- 後續若需更多歷史或檔案，您可以 fetch 它們或調整稀疏檢出以包含額外資料夾。

## 運行程式碼

本課程提供一系列的 Jupyter 筆記本，您可以用來實際動手體驗打造 AI Agents。

程式碼範例使用 **Microsoft Agent Framework (MAF)** 及 `FoundryChatClient`，連接到 **Microsoft Foundry Agent Service V2**（即 Responses API）透過 **Microsoft Foundry**。

所有 Python 筆記本均標示為 `*-python-agent-framework.ipynb`。

## 需求

- Python 3.12+
  - <strong>注意</strong>：如果尚未安裝 Python3.12，請先安裝。接著使用 python3.12 建立虛擬環境，以確保安裝 requirements.txt 中的正確版本。
  
    >範例

    建立 Python 虛擬環境資料夾：

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

- .NET 10+: 對於使用 .NET 的範例程式碼，請確保安裝 [.NET 10 SDK](https://dotnet.microsoft.com/download/dotnet/10.0) 或更高版本。然後檢查已安裝的 .NET SDK 版本：

    ```bash
    dotnet --list-sdks
    ```

- **Azure CLI** — 用於認證。請從 [aka.ms/installazurecli](https://aka.ms/installazurecli) 安裝。
- **Azure 訂閱** — 用於存取 Microsoft Foundry 與 Microsoft Foundry Agent Service。
- **Microsoft Foundry 專案** — 部署好模型的專案（例如 `gpt-5-mini`）。請參閱下方 [步驟 1](#步驟-1：建立-microsoft-foundry-專案)。

本儲存庫根目錄包含 `requirements.txt`，其中列出執行程式碼範例所需的所有 Python 套件。

您可以在終端機中，儲存庫根目錄下執行以下命令安裝：

```bash
pip install -r requirements.txt
```

建議使用 Python 虛擬環境以避免衝突及問題。

## 設定 VSCode

確認您在 VSCode 中使用正確的 Python 版本。

![image](https://github.com/user-attachments/assets/a85e776c-2edb-4331-ae5b-6bfdfb98ee0e)

## 設定 Microsoft Foundry 與 Microsoft Foundry Agent Service

### 步驟 1：建立 Microsoft Foundry 專案

您需要一個 Microsoft Foundry **hub** 和 **project**，並有已部署的模型才能運行筆記本。

1. 前往 [ai.azure.com](https://ai.azure.com) 並用您的 Azure 帳戶登入。
2. 建立一個 **hub**（或使用現有的）。詳見：[Hub 資源概覽](https://learn.microsoft.com/azure/ai-foundry/concepts/ai-resources)。
3. 在 hub 裡建立一個 **project**。
4. 從 **Models + Endpoints** → **Deploy model** 部署一個模型（例如 `gpt-5-mini`）。

### 步驟 2：取得專案端點及模型部署名稱

在 Microsoft Foundry 入口網站的您的專案中：

- <strong>專案端點</strong> — 進入 **Overview** 頁面並複製端點 URL。

![Project Connection String](../../../translated_images/zh-MO/project-endpoint.8cf04c9975bbfbf1.webp)

- <strong>模型部署名稱</strong> — 前往 **Models + Endpoints**，選擇您的已部署模型，並記下 <strong>部署名稱</strong>（例如 `gpt-5-mini`）。

### 步驟 3：使用 `az login` 登入 Azure

大部分筆記本透過您的 **Azure CLI 登入狀態** 認證 — 使用 `azure-identity` 套件中的 `AzureCliCredential` 或 `DefaultAzureCredential`（兩者均會接收您的 `az login` 會話）— 因此不需 API 金鑰。少數課程和選用整合會用到 API 金鑰；請檢查各課程先決條件是否有額外的環境變數。這需要您透過 Azure CLI 登入。

1. 若尚未安裝，請安裝 Azure CLI：[aka.ms/installazurecli](https://aka.ms/installazurecli)

2. 執行以下命令登入：

    ```bash
    az login
    ```

    若您在無瀏覽器的遠端/Codespace 環境中：

    ```bash
    az login --use-device-code
    ```

3. 系統提示時，<strong>選擇您的訂閱</strong> — 請選包含 Foundry 專案的訂閱。

4. 驗證您已登入：

    ```bash
    az account show
    ```

> **為何使用 `az login`？** 筆記本使用 `azure-identity` 套件中的 `AzureCliCredential`（或同時接收 Azure CLI 登入的 `DefaultAzureCredential`）進行認證。這表示您的 Azure CLI 會話提供憑證 — 不需在 `.env` 檔案中包含 API 金鑰或密鑰。這是[安全最佳實踐](https://learn.microsoft.com/azure/developer/ai/keyless-connections)。

### 步驟 4：建立您的 `.env` 檔案

複製範例檔案：

```bash
# zsh/bash
cp .env.example .env
```

```powershell
# PowerShell
Copy-Item .env.example .env
```

開啟 `.env` 填寫這兩個值：

```env
AZURE_AI_PROJECT_ENDPOINT=https://<your-project>.services.ai.azure.com/api/projects/<your-project-id>
AZURE_AI_MODEL_DEPLOYMENT_NAME=gpt-5-mini
```

| 變數 | 取得位置 |
|----------|-----------------|
| `AZURE_AI_PROJECT_ENDPOINT` | Foundry 入口網站 → 您的專案 → **Overview** 頁面 |
| `AZURE_AI_MODEL_DEPLOYMENT_NAME` | Foundry 入口網站 → **Models + Endpoints** → 您已部署模型的名稱 |

大多數課程就這樣！筆記本會自動透過您的 `az login` 會話完成認證。

### 步驟 5：安裝 Python 相依套件

```bash
pip install -r requirements.txt
```

建議在您先前建立的虛擬環境內執行此命令。

## 選用設定：Azure AI 搜尋（第 5 與第 16 課）

第 5 課（Agentic RAG）與第 16 課筆記本可直接使用 <strong>記憶體內知識庫</strong> — 無需額外 Azure 資源。若想支援真實的 **Azure AI 搜尋** 索引，請注意第 16 課筆記本目前使用基於金鑰的認證：僅當同時設定 `AZURE_SEARCH_SERVICE_ENDPOINT` <strong>且</strong> `AZURE_SEARCH_API_KEY` 時才會從記憶體搜尋轉換到 Azure AI 搜尋；否則會維持記憶體搜尋。要對真實索引操作，您必須同時設定管理金鑰。對您自己的正式生產程式碼，建議使用無金鑰的 Microsoft Entra ID （RBAC）認證，與本課程中各處使用的 `az login` 流程一致。

以下 RBAC 步驟適用於本設定指南範例與您自訂程式碼。它們無法授權第 16 課筆記本的無金鑰認證；第 16 課仍需同時設定端點和管理金鑰以使用 Azure AI 搜尋。

1. <strong>在您的搜尋服務上啟用角色基礎存取控制</strong>：

    ```bash
    az search service update --name <service-name> --resource-group <resource-group> --auth-options aadOrApiKey
    ```

2. <strong>為自己指派必要的角色</strong>（建立/讀取索引及查詢）：

    ```bash
    az role assignment create --assignee <your-user-or-principal-id> --role "Search Service Contributor" --scope $(az search service show -g <resource-group> -n <service-name> --query id -o tsv)
    az role assignment create --assignee <your-user-or-principal-id> --role "Search Index Data Contributor" --scope $(az search service show -g <resource-group> -n <service-name> --query id -o tsv)
    ```

3. **將端點新增到您的 `.env` 檔案**：

| 變數 | 取得位置 |
|----------|-----------------|
| `AZURE_SEARCH_SERVICE_ENDPOINT` | Azure 入口網站 → 您的 **Azure AI 搜尋** 資源 → **Overview** → URL |
| `AZURE_SEARCH_API_KEY` | 必要（與端點並用）以啟用第 16 課筆記本中的 Azure AI 搜尋（金鑰認證）。Azure 入口網站 → **Settings** → **Keys** → 主要管理金鑰 |

> **為何推薦無金鑰？** 管理金鑰授予搜索服務完整寫入權限，且可能透過 `.env` 檔案外洩。透過 RBAC，則使用您藉由 `az login` 登入的身份 — 與課程筆記本使用的無金鑰 Entra ID 模式相同（透過 `AzureCliCredential` / `DefaultAzureCredential`）。詳見 [使用角色連接 Azure AI 搜尋](https://learn.microsoft.com/azure/search/search-security-rbac)。

請參閱 [Azure AI 搜尋設定指南](./AzureSearch.md)，了解完整的 Python 與 .NET 索引建立範例。

## 直接呼叫 Azure OpenAI 的課程附加設定（第 6 與第 8 課）

第 6 與第 8 課的部分筆記本直接調用 **Azure OpenAI**（使用 **Responses API**），而非透過 Microsoft Foundry 專案。這些範例先前使用 GitHub Models，但該服務已過時，且不支援 Responses API。請將以下變數加入您的 `.env` 檔案：

| 變數 | 取得位置 |
|----------|-----------------|
| `AZURE_OPENAI_ENDPOINT` | Azure 入口網站 → 您的 **Azure OpenAI** 資源 → **Keys and Endpoint** → 端點（如 `https://<your-resource>.openai.azure.com`）|
| `AZURE_OPENAI_DEPLOYMENT` | 您所部署支持 Responses API 的模型名稱（如 `gpt-5-mini`） |
| `AZURE_OPENAI_API_KEY` | 選用 — 僅在您使用基於金鑰認證而非 `az login` / Entra ID 時需要 |

> Responses API 使用穩定的 `/openai/v1/` 端點，因此不需 `api-version`。請透過 `az login` 進行無金鑰 Entra ID 認證。

## 替代供應商：MiniMax (OpenAI 兼容)

[MiniMax](https://platform.minimaxi.com/) 提供可處理大上下文（最多 204K 代幣）的模型，透過與 OpenAI 兼容的 API。由於 Microsoft Agent Framework 的 `OpenAIChatClient` 可與任何 OpenAI 相容端點配合，因此您可用 MiniMax 作為使用 `OpenAIChatClient` 課程的替代方案。

請將以下變數新增至您的 `.env` 檔案：

| 變數 | 取得位置 |
|----------|-----------------|
| `MINIMAX_API_KEY` | [MiniMax 平台](https://platform.minimaxi.com/) → API 金鑰 |
| `MINIMAX_BASE_URL` | 使用 `https://api.minimax.io/v1`（預設值） |
| `MINIMAX_MODEL_ID` | 要使用的模型名稱（例如 `MiniMax-M3`） |

<strong>示例模型</strong>：`MiniMax-M3`（推薦）、`MiniMax-M2.7`、`MiniMax-M2.7-highspeed`（較快回應）。模型名稱及可用性可能會變動，且對特定模型的存取權依您的帳戶而定。

使用 `OpenAIChatClient` 的程式碼範例（例如第 14 課飯店預訂流程）當設定了 `MINIMAX_API_KEY` 時，將自動偵測並使用您的 MiniMax 設定。


## 替代提供者：Novita AI（兼容 OpenAI）

[Novita AI](https://novita.ai/llm-api) 提供一個兼容 OpenAI 的 API，用於開源和前沿大型語言模型（DeepSeek、Llama、Qwen 等）。由於 Microsoft Agent Framework 的 `OpenAIChatClient` 支援任何兼容 OpenAI 的端點，您可以使用 Novita AI 作為 Azure OpenAI 或 OpenAI 的直接替代方案。

把這些變量添加到您的 `.env` 文件中：

| 變量 | 位置 |
|----------|-----------------|
| `NOVITA_API_KEY` | [Novita AI Dashboard](https://novita.ai/settings/key-management) → API 金鑰 |
| `NOVITA_BASE_URL` | 使用 `https://api.novita.ai/openai/v1`（預設值） |
| `NOVITA_MODEL_ID` | 使用的模型名稱（例如 `moonshotai/kimi-k3`） |

<strong>範例模型</strong>：`moonshotai/kimi-k3`、`zai-org/glm-5.2`、`deepseek/deepseek-v4-flash-0731`。Novita AI 還托管許多其他開源模型系列（Llama、Qwen、GLM 等）— 請查看 [Novita AI 模型庫](https://novita.ai/llm-api) 了解當前可用模型及其模型 ID。

當前範例代碼不會自動使用 `NOVITA_*` 變量。要使用 Novita AI，請在您運行的示例中構建 `OpenAIChatClient` 時明確傳遞這些值。

## 替代提供者：Foundry Local（在設備上運行模型）

[Foundry Local](https://foundrylocal.ai) 是一款輕量級運行時，可下載、管理並通過兼容 OpenAI 的 API <strong>完全在您自己的機器上</strong>提供語言模型服務 — 無需雲端。

由於 Microsoft Agent Framework 的 `OpenAIChatClient` 適用於任何兼容 OpenAI 的端點，Foundry Local 是 Azure OpenAI 的即插即用本地替代方案。

**1. 安裝 Foundry Local**

```bash
# Windows 作業系統
winget install Microsoft.FoundryLocal

# macOS 作業系統
brew install foundrylocal
```

**2. 下載並運行模型**（這也會啟動本地服務）：

```bash
foundry model list          # 查看可用模型
foundry model run phi-4-mini
```

**3. 安裝用於發現本地端點的 Python SDK：**

```bash
pip install foundry-local-sdk
```

**4. 指向 Microsoft Agent Framework 至您的本地模型：**

```python
from foundry_local import FoundryLocalManager
from agent_framework.openai import OpenAIChatClient

# 下載（如有需要）並在本地提供模型，然後發現端點/端口。
manager = FoundryLocalManager("phi-4-mini")

chat_client = OpenAIChatClient(
    base_url=manager.endpoint,      # 例如 http://localhost:<port>/v1
    api_key=manager.api_key,        # 對於 Foundry Local 始終為「不需要」。
    model_id=manager.get_model_info("phi-4-mini").id,
)

agent = chat_client.as_agent(
    name="LocalAgent",
    instructions="You are a helpful assistant running fully on-device.",
)
```

> **注意:** Foundry Local 提供一個兼容 OpenAI 的 <strong>聊天補全</strong> 端點。請用於本地開發及離線場景。要完整使用 **Responses API** 功能集（如有狀態對話等），請使用 Azure OpenAI 或 Microsoft Foundry 項目。

## 第八課額外設置（Bing 定向工作流）

第八課的條件工作流筆記本使用 Microsoft Foundry 通過 **Bing 定向**。如果打算執行該範例，請將此變量添加到您的 `.env` 文件中：

| 變量 | 位置 |
|----------|-----------------|
| `BING_CONNECTION_ID` | Microsoft Foundry 入口 → 您的項目 → <strong>管理</strong> → <strong>已連接資源</strong> → 您的 Bing 連接 → 複製連接 ID |

## 疑難排解

### macOS 上的 SSL 證書驗證錯誤

如果您使用 macOS 並遇到如下錯誤：

```plaintext
ssl.SSLCertVerificationError: [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: self-signed certificate in certificate chain
```

這是 macOS 上 Python 的已知問題，系統 SSL 證書不會自動被信任。請按順序嘗試以下解決方案：

**選項 1：運行 Python 安裝證書腳本（推薦）**

```bash
# 將 3.XX 換成您已安裝的 Python 版本（例如：3.12 或 3.13）：
/Applications/Python\ 3.XX/Install\ Certificates.command
```

**選項 2：在您的筆記本中使用 `connection_verify=False`（僅限 GitHub Models 筆記本）**

在第六課筆記本 (`06-building-trustworthy-agents/code_samples/06-system-message-framework.ipynb`) 中，已包含注釋掉的解決方案。遇到證書錯誤時，請取消註解 `connection_verify=False`：

```python
client = ChatCompletionsClient(
    endpoint=endpoint,
    credential=AzureKeyCredential(token),
    connection_verify=False,  # 如果遇到證書錯誤，請禁用 SSL 驗證
)
```

> **⚠️ 警告：** 禁用 SSL 驗證（`connection_verify=False`）會降低安全性，因為跳過了證書驗證。請僅作為開發環境中的臨時解決方案使用，切勿在生產環境中使用。

**選項 3：安裝並使用 `truststore`**

```bash
pip install truststore
```

然後在您的筆記本或腳本頂部添加以下內容，並且在進行任何網絡調用前執行：

```python
import truststore
truststore.inject_into_ssl()
```

## 遇到問題？

如果您在這個設置過程中遇到任何問題，歡迎加入我們的<a href="https://discord.gg/kzRShWzttr" target="_blank">Azure AI 社區 Discord</a>或<a href="https://github.com/microsoft/ai-agents-for-beginners/issues?WT.mc_id=academic-105485-koreyst" target="_blank">提交問題</a>。

## 下一課

您現在已準備好運行本課程的代碼。祝您學習 AI Agents 的世界愉快！

[AI Agents介紹及應用案例](../01-intro-to-ai-agents/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責聲明**：
本文件使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。雖然我們力求準確，但請注意，自動翻譯可能包含錯誤或不準確之處。原始文件的母語版本應被視為權威來源。對於重要資訊，建議尋求專業人工翻譯。我們不對因使用本翻譯而引起的任何誤解或曲解承擔責任。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->