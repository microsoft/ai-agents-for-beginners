# 課程設置

## 簡介

這堂課將涵蓋如何運行本課程的程式碼範例。

## 加入其他學習者並獲得協助

在開始複製您的儲存庫之前，請加入 [AI Agents For Beginners Discord 頻道](https://aka.ms/ai-agents/discord) ，以便獲得任何設置上的協助、對課程的疑問，或與其他學習者連接。

## 複製或派生此儲存庫

要開始，請複製或派生這個 GitHub 儲存庫。這樣您就會有自己版本的課程教材，可以執行、測試和調整程式碼！

您可以點擊這個連結 <a href="https://github.com/microsoft/ai-agents-for-beginners/fork" target="_blank">派生儲存庫</a> 來完成。

您現在應該有這門課程的派生版本，連結如下：

![Forked Repo](../../../translated_images/zh-HK/forked-repo.33f27ca1901baa6a.webp)

### 淺層複製（推薦用於工作坊 / Codespaces）

  > 當下載完整歷史記錄和所有檔案時，完整儲存庫可能很大（約 3 GB）。如果您只參加工作坊或只需要幾個課程資料夾，淺層複製（或稀疏複製）會下載更少資料。

#### 快速淺層複製 — 極少歷史紀錄，所有檔案

將以下命令中的 `<your-username>` 替換為您的派生 URL（或上游 URL，視您喜好）。

若只想複製最新提交歷史（較小下載量）：

```bash
git clone --depth 1 https://github.com/<your-username>/ai-agents-for-beginners.git
```

若要複製特定分支：

```bash
git clone --depth 1 --branch <branch-name> https://github.com/<your-username>/ai-agents-for-beginners.git
```

#### 部分（稀疏）複製 — 最少 Blob + 只選擇特定資料夾

這使用部分複製和稀疏檢出 (需要 Git 2.25+ 並推薦使用支援部分複製的較新 Git)：

```bash
git clone --depth 1 --filter=blob:none --sparse https://github.com/<your-username>/ai-agents-for-beginners.git
```

進入儲存庫資料夾：

```bash
cd ai-agents-for-beginners
```

然後指定您想要的資料夾（以下範例顯示兩個資料夾）：

```bash
git sparse-checkout set 00-course-setup 01-intro-to-ai-agents
```

複製並確認檔案後，若您只需檔案且想釋放空間（無需 git 歷史），請刪除儲存庫元資料（💀不可復原 — 您將失去所有 Git 功能）：

```bash
# zsh/bash
rm -rf .git
```

```powershell
# PowerShell
Remove-Item -Recurse -Force .git
```

#### 使用 GitHub Codespaces（推薦以避免本機大型下載）

- 透過 [GitHub UI](https://github.com/codespaces) 為此儲存庫建立新的 Codespace。  

- 在新建的 codespace 終端機中，執行上述淺層/稀疏複製命令之一，僅將所需課程資料夾帶入 Codespace 工作區。
- 選擇性：在 Codespaces 裡複製後，刪除 .git 以回收額外空間（見上述刪除命令）。
- 注意：若您偏好直接在 Codespaces 打開儲存庫（不額外複製），請注意 Codespaces 會建構 devcontainer 環境，可能還是會配置超過您需要的內容。

#### 小技巧

- 如果您想編輯/提交，務必將複製 URL 換成您的派生版本。
- 若您之後需要更多歷史或檔案，可以擷取它們或調整稀疏檢出以包含更多資料夾。

## 運行程式碼

本課程提供一系列 Jupyter 筆記本，讓您實際操作並建立 AI 代理。

程式碼範例使用 **Microsoft Agent Framework (MAF)** 搭配 `FoundryChatClient`，通過 **Microsoft Foundry** 連線至 **Microsoft Foundry Agent Service V2**（回應 API）。

所有 Python 筆記本標註為 `*-python-agent-framework.ipynb`。

## 需求

- Python 3.12+
  - <strong>注意</strong>：如果您尚未安裝 Python 3.12，請務必安裝。然後用 python3.12 建立您的虛擬環境，確保從 requirements.txt 安裝正確版本。
  
    > 範例

    建立 Python 虛擬環境資料夾：

    ```bash
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

- .NET 10+：對於使用 .NET 的範例碼，請確保安裝 [.NET 10 SDK](https://dotnet.microsoft.com/download/dotnet/10.0) 或更新版本。檢查已安裝的 .NET SDK 版本：

    ```bash
    dotnet --list-sdks
    ```

- **Azure CLI** — 用於身份驗證。從 [aka.ms/installazurecli](https://aka.ms/installazurecli) 安裝。
- **Azure 訂閱** — 用於存取 Microsoft Foundry 和 Microsoft Foundry Agent Service。
- **Microsoft Foundry 專案** — 擁有已部署模型的專案（例如 `gpt-5-mini`）。請參見下方 [步驟 1](#步驟-1：建立-microsoft-foundry-專案)。

我們在此儲存庫根目錄附上 `requirements.txt`，包含執行程式範例所需所有 Python 套件。

您可以在儲存庫根目錄終端機執行以下指令安裝：

```bash
pip install -r requirements.txt
```

我們建議您建立 Python 虛擬環境，以避免衝突與問題。

## 設定 VSCode

確保您在 VSCode 使用正確的 Python 版本。

![image](https://github.com/user-attachments/assets/a85e776c-2edb-4331-ae5b-6bfdfb98ee0e)

## 設定 Microsoft Foundry 和 Microsoft Foundry Agent Service

### 步驟 1：建立 Microsoft Foundry 專案

您需要一個 Microsoft Foundry **hub** 和 <strong>專案</strong>，且該專案中必須部署模型，才能執行筆記本。

1. 前往 [ai.azure.com](https://ai.azure.com) 並使用您的 Azure 帳戶登入。
2. 建立一個 **hub**（或使用現有的）。參見：[Hub 資源概覽](https://learn.microsoft.com/azure/ai-foundry/concepts/ai-resources)。
3. 在 hub 裡建立一個 <strong>專案</strong>。
4. 從 **Models + Endpoints** → **Deploy model** 部署一個模型（如 `gpt-5-mini`）。

### 步驟 2：取得您的專案端點和模型部署名稱

從 Microsoft Foundry 門戶的專案中：

- <strong>專案端點</strong> — 前往 <strong>概覽</strong> 頁面，複製端點 URL。

![Project Connection String](../../../translated_images/zh-HK/project-endpoint.8cf04c9975bbfbf1.webp)

- <strong>模型部署名稱</strong> — 前往 **Models + Endpoints**，選擇已部署的模型，並紀錄 <strong>部署名稱</strong>（如 `gpt-5-mini`）。

### 步驟 3：使用 `az login` 登入 Azure

大多數筆記本透過您的 **Azure CLI 登入** 驗證 — 使用 `azure-identity` 套件中的 `AzureCliCredential` 或 `DefaultAzureCredential`（兩者皆可取得您的 `az login` 會話）— 因此不需 API 金鑰。部分課程和選用整合會用到 API 金鑰，請檢查各課程先決條件是否需額外環境變數。這需要您透過 Azure CLI 登入。

1. 若尚未安裝 **Azure CLI**，請安裝：[aka.ms/installazurecli](https://aka.ms/installazurecli)

2. 執行以下命令 <strong>登入</strong>：

    ```bash
    az login
    ```

    如果您在無瀏覽器的遠端/Codespace 環境中：

    ```bash
    az login --use-device-code
    ```

3. 如果系統提示，<strong>選擇您的訂閱</strong> — 選擇包含您的 Foundry 專案的訂閱。

4. <strong>確認</strong>您已登入：

    ```bash
    az account show
    ```

> **為什麼用 `az login`？** 筆記本使用 `azure-identity` 套件中的 `AzureCliCredential`（或同時支援的 `DefaultAzureCredential`），能取得您的 Azure CLI 登入狀態，這表示您透過 CLI 的會話提供認證，無需在 `.env` 放 API 金鑰或密鑰。這是 [安全最佳實踐](https://learn.microsoft.com/azure/developer/ai/keyless-connections)。

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

開啟 `.env` 並填寫以下兩個值：

```env
AZURE_AI_PROJECT_ENDPOINT=https://<your-project>.services.ai.azure.com/api/projects/<your-project-id>
AZURE_AI_MODEL_DEPLOYMENT_NAME=gpt-5-mini
```

| 變數 | 取得位置 |
|----------|-----------------|
| `AZURE_AI_PROJECT_ENDPOINT` | Foundry 入口網站 → 您的專案 → <strong>概覽</strong> 頁面 |
| `AZURE_AI_MODEL_DEPLOYMENT_NAME` | Foundry 入口網站 → **Models + Endpoints** → 您已部署模型名稱 |

大部分課程就這樣完成了！筆記本會自動透過您的 `az login` 會話驗證。

### 步驟 5：安裝 Python 相依套件

```bash
pip install -r requirements.txt
```

建議在您之前建立的虛擬環境中執行這個指令。

## 選用設定：Azure AI 搜尋（第 5 與第 16 課）

第 5 課（Agentic RAG）與第 16 課筆記本預設使用<strong>記憶體內知識庫</strong>— 無需額外 Azure 資源。如果您想用真實 **Azure AI Search** 索引做後援，請注意第 16 課本筆記本目前使用基於金鑰的驗證：當且僅當同時設定 `AZURE_SEARCH_SERVICE_ENDPOINT` <strong>及</strong> `AZURE_SEARCH_API_KEY` 時，才從記憶體內搜尋切換到 Azure AI Search，否則仍維持記憶體內搜尋 — 因此若想使用真實索引，您必須設定管理金鑰。無金鑰認證的 Microsoft Entra ID（RBAC）是您自有生產程式碼建議採用的方式，與本課程其他地方的 `az login` 流程一致。

下方 RBAC 步驟適用於此設置指引範例與您自有程式碼。它們不會使第 16 課筆記本支援無金鑰認證；第 16 課仍需同時設定端點與管理金鑰才使用 Azure AI Search。

1. 在您的搜尋服務上<strong>啟用角色基礎存取</strong>：

    ```bash
    az search service update --name <service-name> --resource-group <resource-group> --auth-options aadOrApiKey
    ```

2. <strong>指派必要角色給自己</strong>（建立/載入索引及查詢）：

    ```bash
    az role assignment create --assignee <your-user-or-principal-id> --role "Search Service Contributor" --scope $(az search service show -g <resource-group> -n <service-name> --query id -o tsv)
    az role assignment create --assignee <your-user-or-principal-id> --role "Search Index Data Contributor" --scope $(az search service show -g <resource-group> -n <service-name> --query id -o tsv)
    ```

3. **在 `.env` 加入端點設定**：

| 變數 | 取得位置 |
|----------|-----------------|
| `AZURE_SEARCH_SERVICE_ENDPOINT` | Azure 入口網站 → 您的 **Azure AI Search** 資源 → <strong>概覽</strong> → URL |
| `AZURE_SEARCH_API_KEY` | 第 16 課筆記本中啟用 Azure AI Search 所需（搭配端點使用）基於金鑰認證。Azure 入口網站 → <strong>設定</strong> → <strong>金鑰</strong> → 主要管理金鑰 |

> **為什麼要用無金鑰？** 管理金鑰賦予搜尋服務完整寫入權限，且可能洩漏於 `.env` 檔。使用 RBAC，則改用您的 `az login` 身份認證 — 與課程筆記本使用無金鑰 Entra ID 模式相同（透過 `AzureCliCredential` / `DefaultAzureCredential`）。詳見 [使用角色連接 Azure AI Search](https://learn.microsoft.com/azure/search/search-security-rbac)。

請參閱 [Azure AI Search 設定指南](./AzureSearch.md)，內含完整的 Python 與 .NET 建立索引範例。

## 針對直接呼叫 Azure OpenAI 的課程額外設定（第 6 與第 8 課）

第 6 與第 8 課某些筆記本直接呼叫 **Azure OpenAI**（使用 **Responses API**），未透過 Microsoft Foundry 專案。這些範例舊曾使用 GitHub Models，該服務已棄用且不支援 Responses API。請於 `.env` 新增以下變數：

| 變數 | 取得位置 |
|----------|-----------------|
| `AZURE_OPENAI_ENDPOINT` | Azure 入口網站 → 您的 **Azure OpenAI** 資源 → <strong>金鑰與端點</strong> → 端點（例如 `https://<your-resource>.openai.azure.com`） |
| `AZURE_OPENAI_DEPLOYMENT` | 您已部署並支援 Responses API 的模型名稱（例如 `gpt-5-mini`） |
| `AZURE_OPENAI_API_KEY` | 選用 — 只有當您使用基於金鑰的驗證，而非 `az login` / Entra ID 時需要 |

> Responses API 使用穩定的 `/openai/v1/` 端點，無需 `api-version`。請透過 `az login` 使用無金鑰 Entra ID 驗證。

## 替代供應商：MiniMax（OpenAI 相容）

[MiniMax](https://platform.minimaxi.com/) 提供大上下文模型（高達 204K 字元），並透過 OpenAI 相容 API。由於 Microsoft Agent Framework 的 `OpenAIChatClient` 能用於任何 OpenAI 相容端點，您可以將 MiniMax 用作使用 `OpenAIChatClient` 的課程範例中的替代方案。

請於 `.env` 檔新增以下變數：

| 變數 | 取得位置 |
|----------|-----------------|
| `MINIMAX_API_KEY` | [MiniMax 平台](https://platform.minimaxi.com/) → API 金鑰 |
| `MINIMAX_BASE_URL` | 使用 `https://api.minimax.io/v1`（預設值） |
| `MINIMAX_MODEL_ID` | 使用的模型名稱（例如 `MiniMax-M3`） |

<strong>範例模型</strong>：`MiniMax-M3`（推薦）、`MiniMax-M2.7`、`MiniMax-M2.7-highspeed`（回應較快）。模型名稱與可用度或會隨時間更動，且是否能使用特定模型取決於您的帳戶。

使用 `OpenAIChatClient` 的程式碼範例（例如第 14 課旅館訂房流程）在設定 `MINIMAX_API_KEY` 時，會自動偵測並使用您的 MiniMax 配置。


## 替代供應商：Novita AI（OpenAI 兼容）

[Novita AI](https://novita.ai/llm-api) 提供了用於開源及前沿大型語言模型（DeepSeek、Llama、Qwen 等）的 OpenAI 兼容 API。由於 Microsoft Agent Framework 的 `OpenAIChatClient` 可與任何 OpenAI 兼容的端點搭配使用，因此您可以使用 Novita AI 作為 Azure OpenAI 或 OpenAI 的即插即用替代方案。

將這些變量添加到您的 `.env` 文件：

| 變量 | 位置 |
|----------|-----------------|
| `NOVITA_API_KEY` | [Novita AI 控制台](https://novita.ai/settings/key-management) → API 密鑰 |
| `NOVITA_BASE_URL` | 使用 `https://api.novita.ai/openai/v1`（預設值） |
| `NOVITA_MODEL_ID` | 要使用的模型名稱（例如 `moonshotai/kimi-k3`） |

<strong>示例模型</strong>：`moonshotai/kimi-k3`、`zai-org/glm-5.2`、`deepseek/deepseek-v4-flash-0731`。Novita AI 同時也托管了許多其他開源模型系列（Llama、Qwen、GLM 等）—請查看 [Novita AI 模型庫](https://novita.ai/llm-api) 獲取當前可用模型列表及其模型 ID。

目前的範例不會自動使用 `NOVITA_*` 變量。要使用 Novita AI，請在您運行的範例中顯式傳入這些值以構建 `OpenAIChatClient`。

## 替代供應商：Foundry Local（本機運行模型）

[Foundry Local](https://foundrylocal.ai) 是一個輕量級運行時，能夠通過 OpenAI 兼容 API <strong>完全在您自己的機器上</strong>下載、管理和提供語言模型 — 無需雲端服務。

由於 Microsoft Agent Framework 的 `OpenAIChatClient` 可與任何 OpenAI 兼容端點搭配使用，Foundry Local 是 Azure OpenAI 的本地即插即用替代方案。

**1. 安裝 Foundry Local**

```bash
# Windows 視窗系統
winget install Microsoft.FoundryLocal

# macOS 蘋果作業系統
brew install foundrylocal
```

**2. 下載並運行模型**（同時啟動本地服務）：

```bash
foundry model list          # 查看可用模型
foundry model run phi-4-mini
```

**3. 安裝 Python SDK** 用於發現本地端點：

```bash
pip install foundry-local-sdk
```

**4. 指向 Microsoft Agent Framework 使用您的本地模型：**

```python
from foundry_local import FoundryLocalManager
from agent_framework.openai import OpenAIChatClient

# 下載（如果需要）並本地提供模型，然後發現端點/端口。
manager = FoundryLocalManager("phi-4-mini")

chat_client = OpenAIChatClient(
    base_url=manager.endpoint,      # 例如 http://localhost:<port>/v1
    api_key=manager.api_key,        # 對 Foundry Local 永遠是「不需要」
    model_id=manager.get_model_info("phi-4-mini").id,
)

agent = chat_client.as_agent(
    name="LocalAgent",
    instructions="You are a helpful assistant running fully on-device.",
)
```

> **注意：** Foundry Local 提供 OpenAI 兼容的 <strong>聊天補全</strong> 端點。用於本地開發和離線場景。要使用完整 **回應 API** 功能集（有狀態對話等），請使用 Azure OpenAI 或 Microsoft Foundry 專案。

## 第 8 課額外設置（Bing 地基工作流程）

第 8 課中的條件工作流程筆記本使用 Microsoft Foundry 提供的 **Bing 地基**。如果您打算運行該示例，請將此變量添加到您的 `.env` 文件：

| 變量 | 位置 |
|----------|-----------------|
| `BING_CONNECTION_ID` | Microsoft Foundry 控制台 → 您的專案 → <strong>管理</strong> → <strong>已連接資源</strong> → 您的 Bing 連接 → 複製連接 ID |

## 故障排除

### macOS 上的 SSL 證書驗證錯誤

如果您使用的是 macOS 且遇到類似錯誤：

```plaintext
ssl.SSLCertVerificationError: [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: self-signed certificate in certificate chain
```

這是 macOS 上 Python 的已知問題，系統 SSL 證書不會自動被信任。請按順序嘗試以下解決方案：

**選項 1：運行 Python 的安裝證書腳本（推薦）**

```bash
# 將 3.XX 替換為你安裝的 Python 版本（例如，3.12 或 3.13）：
/Applications/Python\ 3.XX/Install\ Certificates.command
```

**選項 2：在筆記本中使用 `connection_verify=False`（僅限 GitHub Models 筆記本）**

在第 6 課的筆記本（`06-building-trustworthy-agents/code_samples/06-system-message-framework.ipynb`）中，已包含一個已註解的可行變通方法。遇到證書錯誤時取消註解 `connection_verify=False`：

```python
client = ChatCompletionsClient(
    endpoint=endpoint,
    credential=AzureKeyCredential(token),
    connection_verify=False,  # 如果遇到證書錯誤，請禁用 SSL 驗證
)
```

> **⚠️ 警告：** 禁用 SSL 驗證（`connection_verify=False`）會降低安全性，因為會跳過證書驗證。僅在開發環境中作為臨時變通方法使用，切勿在生產環境中使用。

**選項 3：安裝並使用 `truststore`**

```bash
pip install truststore
```

然後在筆記本或腳本頂部，在進行任何網路請求之前添加如下代碼：

```python
import truststore
truststore.inject_into_ssl()
```

## 卡住了嗎？

若在執行此設置時有任何問題，歡迎加入我們的 <a href="https://discord.gg/kzRShWzttr" target="_blank">Azure AI 社群 Discord</a> 或 <a href="https://github.com/microsoft/ai-agents-for-beginners/issues?WT.mc_id=academic-105485-koreyst" target="_blank">創建 issue</a>。

## 下一課

現在您已準備好運行本課的程式碼。祝您學習 AI 代理世界愉快！

[AI代理簡介及代理使用案例](../01-intro-to-ai-agents/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責聲明**：
本文件由 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 翻譯而成。雖然我們致力於確保準確性，但請注意，機器自動翻譯可能包含錯誤或不準確之處。原始文件的母語版本應被視為權威來源。對於重要資訊，建議進行專業人工翻譯。我們不對因使用本翻譯而產生的任何誤解或誤釋承擔責任。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->