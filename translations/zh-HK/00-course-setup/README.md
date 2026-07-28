# 課程設定

## 介紹

本課程將介紹如何執行本課程的程式碼範例。

## 加入其他學習者並獲得協助

在開始克隆您的儲存庫之前，請加入[AI Agents For Beginners Discord 頻道](https://aka.ms/ai-agents/discord)，以獲得任何設定上的協助、課程問題，或與其他學習者交流。

## 克隆或分支此儲存庫

首先，請克隆或分支 GitHub 儲存庫。這會建立您自己的課程材料版本，讓您能執行、測試和調整程式碼！

您可以點擊連結<a href="https://github.com/microsoft/ai-agents-for-beginners/fork" target="_blank">分支此儲存庫</a>來完成此操作

您現在應該擁有此課程的分支版本，連結如下：

![Forked Repo](../../../translated_images/zh-HK/forked-repo.33f27ca1901baa6a.webp)

### 淺層克隆（推薦用於工作坊 / Codespaces）

  >下載完整歷史和所有檔案時，完整儲存庫可能很大（約 3 GB）。如果您僅參加工作坊或只需要部分課程資料夾，淺層克隆（或稀疏克隆）透過截斷歷史記錄和/或跳過 blobs，避免大部分下載。

#### 快速淺層克隆 — 最少歷史，全檔案

將下列指令中的 `<your-username>` 替換為您的分支 URL（或上游 URL，如果您偏好）。

若只克隆最新的提交歷史（下載量小）：

```bash|powershell
git clone --depth 1 https://github.com/<your-username>/ai-agents-for-beginners.git
```

若要克隆特定分支：

```bash|powershell
git clone --depth 1 --branch <branch-name> https://github.com/<your-username>/ai-agents-for-beginners.git
```

#### 部分（稀疏）克隆 — 最少 blobs + 只選定的資料夾

此方法使用部分克隆和 sparse-checkout（需要 Git 2.25+ 且建議使用支援部分克隆的現代 Git）：

```bash|powershell
git clone --depth 1 --filter=blob:none --sparse https://github.com/<your-username>/ai-agents-for-beginners.git
```

進入儲存庫資料夾：

```bash|powershell
cd ai-agents-for-beginners
```

然後指定您需要的資料夾（範例展示兩個資料夾）：

```bash|powershell
git sparse-checkout set 00-course-setup 01-intro-to-ai-agents
```

克隆並檢查檔案後，若您只需要檔案且想釋放空間（無需 git 歷史），請刪除儲存庫元資料（💀不可逆 — 您將失去所有 Git 功能：無法提交、拉取、推送或存取歷史）。

```bash
# zsh/bash
rm -rf .git
```

```powershell
# PowerShell
Remove-Item -Recurse -Force .git
```

#### 使用 GitHub Codespaces（推薦以避免本地大型下載）

- 透過[GitHub UI](https://github.com/codespaces)為此儲存庫建立新的 Codespace。  

- 在新建立的 Codespace 終端機中，執行上述淺層/稀疏克隆指令，將您需要的課程資料夾帶入 Codespace 工作區。
- 選用：Clone 後在 Codespaces 裡移除 .git 以回收額外空間（參見上述移除指令）。
- 注意：若您偏好直接用 Codespaces 開啟儲存庫（不另 Clone），請知悉 Codespaces 會構建 devcontainer 環境，可能仍會配置超出您需求。於新的 Codespace 內 Clone 淺層副本，能讓您更掌控磁碟使用。

#### 小技巧

- 如需編輯/提交，請務必替換克隆 URL 為您的分支。
- 若後續需要更多歷史或檔案，您可以拉取或調整 sparse-checkout 以加入更多資料夾。

## 執行程式碼

本課程提供一系列 Jupyter 筆記本，讓您實作體驗建置 AI Agents。

範例程式使用 **Microsoft Agent Framework (MAF)** 的 `FoundryChatClient`，透過 **Microsoft Foundry** 連接至 **Microsoft Foundry Agent Service V2**（Responses API）。

所有 Python 筆記本皆標註以 `*-python-agent-framework.ipynb`。

## 需求

- Python 3.12+
  - <strong>注意</strong>：若尚未安裝 Python3.12，請先安裝。建立虛擬環境時務必使用 python3.12，確保從 requirements.txt 安裝正確版本。
  
    >範例

    建立 Python 虛擬環境資料夾：

    ```bash|powershell
    python -m venv venv
    ```

    然後啟動虛擬環境：

    ```bash
    # zsh/bash
    source venv/bin/activate
    ```
  
    ```dos
    # Command Prompt for Windows
    venv\Scripts\activate
    ```

- .NET 10+：使用範例程式碼需安裝 [.NET 10 SDK](https://dotnet.microsoft.com/download/dotnet/10.0) 或更新版本。檢查已安裝的 .NET SDK 版本：

    ```bash|powershell
    dotnet --list-sdks
    ```

- **Azure CLI** — 認證必備，請從 [aka.ms/installazurecli](https://aka.ms/installazurecli) 安裝。
- **Azure 訂閱** — 以用於存取 Microsoft Foundry 和 Microsoft Foundry Agent Service。
- **Microsoft Foundry 專案** — 需有部署模型（例如 `gpt-5-mini`）。請參考下方[步驟 1](#步驟-1：建立-microsoft-foundry-專案)。

本儲存庫根目錄已包含 `requirements.txt`，列出執行程式碼範例所需的所有 Python 套件。

您可於儲存庫根目錄終端機執行以下指令安裝：

```bash|powershell
pip install -r requirements.txt
```

建議建立 Python 虛擬環境以避免衝突與問題。

## 設定 VSCode

請確保在 VSCode 中使用正確版本的 Python。

![image](https://github.com/user-attachments/assets/a85e776c-2edb-4331-ae5b-6bfdfb98ee0e)

## 設定 Microsoft Foundry 和 Microsoft Foundry Agent Service

### 步驟 1：建立 Microsoft Foundry 專案

您需一個 Microsoft Foundry **hub** 和包含已部署模型的 <strong>專案</strong>，才能執行筆記本。

1. 前往 [ai.azure.com](https://ai.azure.com)，並用您的 Azure 帳戶登入。
2. 建立一個 **hub**（或使用現有者）。參閱：[Hub 資源概述](https://learn.microsoft.com/azure/ai-foundry/concepts/ai-resources)。
3. 在 hub 內建立一個 <strong>專案</strong>。
4. 從 **Models + Endpoints** → **Deploy model** 部署模型（例如 `gpt-5-mini`）。

### 步驟 2：取得專案端點和模型部署名稱

在 Microsoft Foundry 入口網站的專案中：

- <strong>專案端點</strong> — 前往 **Overview** 頁面並複製端點 URL。

![Project Connection String](../../../translated_images/zh-HK/project-endpoint.8cf04c9975bbfbf1.webp)

- <strong>模型部署名稱</strong> — 至 **Models + Endpoints**，選擇您部署的模型，記下 **Deployment name**（例如 `gpt-5-mini`）。

### 步驟 3：使用 `az login` 登入 Azure

所有筆記本皆使用 **`AzureCliCredential`** 認證，無需管理 API 金鑰。這要求您透過 Azure CLI 登入。

1. 若尚未安裝，先安裝 **Azure CLI**：[aka.ms/installazurecli](https://aka.ms/installazurecli)

2. 執行登入指令：

    ```bash|powershell
    az login
    ```

    若在無瀏覽器的遠端/Codespace 環境：

    ```bash|powershell
    az login --use-device-code
    ```

3. 若系統提示，<strong>選擇訂閱</strong> — 選擇含您的 Foundry 專案的訂閱。

4. 確認您已成功登入：

    ```bash|powershell
    az account show
    ```

> **為什麼要用 `az login`？** 筆記本透過 `azure-identity` 套件的 `AzureCliCredential` 進行認證，您的 Azure CLI 會話即提供認證，無需在 `.env` 檔案存放 API 金鑰或秘密。這是[安全最佳實務](https://learn.microsoft.com/azure/developer/ai/keyless-connections)。

### 步驟 4：建立您的 `.env` 檔案

複製範本檔案：

```bash
# zsh/bash
cp .env.example .env
```

```powershell
# PowerShell
Copy-Item .env.example .env
```

開啟 `.env`，填寫這兩個變數：

```env
AZURE_AI_PROJECT_ENDPOINT=https://<your-project>.services.ai.azure.com/api/projects/<your-project-id>
AZURE_AI_MODEL_DEPLOYMENT_NAME=gpt-5-mini
```

| 變數 | 取得位置 |
|----------|-----------------|
| `AZURE_AI_PROJECT_ENDPOINT` | Foundry 入口網站 → 您的專案 → **Overview** 頁面 |
| `AZURE_AI_MODEL_DEPLOYMENT_NAME` | Foundry 入口網站 → **Models + Endpoints** → 您部署模型的名稱 |

大多數課程就到此完成！筆記本會透過您的 `az login` 會話自動認證。

### 步驟 5：安裝 Python 依賴套件

```bash|powershell
pip install -r requirements.txt
```

建議在您先前建立的虛擬環境中執行此指令。

## 課程 5（Agentic RAG）額外設定

課程 5 使用 **Azure AI Search** 來實現檢索增強生成。若您計劃執行該課程，請在 `.env` 中加入以下變數：

| 變數 | 取得位置 |
|----------|-----------------|
| `AZURE_SEARCH_SERVICE_ENDPOINT` | Azure 入口網站 → 您的 **Azure AI Search** 資源 → **Overview** → URL |
| `AZURE_SEARCH_API_KEY` | Azure 入口網站 → 您的 **Azure AI Search** 資源 → **Settings** → **Keys** → 主要管理金鑰 |

## 直接調用 Azure OpenAI 的課程（課程 6 和 8）額外設定

部分課程 6 和 8 的筆記本直接調用 **Azure OpenAI**（使用 **Responses API**），而非透過 Microsoft Foundry 專案。這些範例以前使用 GitHub Models，該服務已棄用（2026 年 7 月退休）且不支援 Responses API。如您欲執行這些範例，請在 `.env` 中加入下列變數：

| 變數 | 取得位置 |
|----------|-----------------|
| `AZURE_OPENAI_ENDPOINT` | Azure 入口網站 → 您的 **Azure OpenAI** 資源 → **Keys and Endpoint** → Endpoint（例如 `https://<your-resource>.openai.azure.com`） |
| `AZURE_OPENAI_DEPLOYMENT` | 支援 Responses API 的部署模型名稱（例如 `gpt-5-mini`） |
| `AZURE_OPENAI_API_KEY` | 選用 — 僅當您使用基於金鑰的認證而非 `az login` / Entra ID 時 |

> Responses API 使用穩定的 `/openai/v1/` 端點，因此不需指定 `api-version`。透過 `az login` 進行無金鑰 Entra ID 認證。

## 替代提供者：MiniMax（相容 OpenAI）

[MiniMax](https://platform.minimaxi.com/) 提供大上下文模型（最高支援 204K 字元）透過相容 OpenAI 的 API。由於 Microsoft Agent Framework 的 `OpenAIChatClient` 可與任何相容 OpenAI 的端點協作，MiniMax 可作為 Azure OpenAI 或 OpenAI 的替代方案無縫使用。

請將以下變數加入您的 `.env` 檔案：

| 變數 | 取得位置 |
|----------|-----------------|
| `MINIMAX_API_KEY` | [MiniMax 平台](https://platform.minimaxi.com/) → API 金鑰 |
| `MINIMAX_BASE_URL` | 使用 `https://api.minimax.io/v1`（預設值） |
| `MINIMAX_MODEL_ID` | 要使用的模型名稱（例如 `MiniMax-M3`） |

<strong>範例模型</strong>：`MiniMax-M3`（推薦）、`MiniMax-M2.7`、`MiniMax-M2.7-highspeed`（響應更快）。模型名稱及可用性會隨時間變化，且存取可能依您的帳戶或區域不同而異 — 請查閱 [MiniMax 平台](https://platform.minimaxi.com/) 以獲得最新清單。若您的帳戶無法使用 `MiniMax-M3`，請將 `MINIMAX_MODEL_ID` 設為您能使用的模型（例：`MiniMax-M2.7`）。

使用 `OpenAIChatClient` 的程式碼範例（例如第 14 課旅館預訂流程）在設定了 `MINIMAX_API_KEY` 後，會自動偵測並使用您的 MiniMax 配置。

## 替代提供者：Foundry Local（本機執行模型）

[Foundry Local](https://foundrylocal.ai) 是輕量級執行環境，可完全在您的設備上下載、管理及提供語言模型，並經由相容 OpenAI 的 API 使用 — 不需雲端、Azure 訂閱或 API 金鑰。非常適合離線開發、無需產生雲端費用的實驗，或是希望資料留在本機的場景。

由於 Microsoft Agent Framework 的 `OpenAIChatClient` 能配合任一相容 OpenAI 的端點，Foundry Local 是 Azure OpenAI 的本機替代方案。

**1. 安裝 Foundry Local**

```bash
# Windows 作業系統
winget install Microsoft.FoundryLocal

# macOS 作業系統
brew install foundrylocal
```

**2. 下載並執行模型**（同時啟動本機服務）：

```bash
foundry model list          # 查看可用模型
foundry model run phi-4-mini
```

**3. 安裝用於發現本機端點的 Python SDK**：

```bash
pip install foundry-local-sdk
```

**4. 指向 Microsoft Agent Framework 使用您的本機模型：**

```python
from foundry_local import FoundryLocalManager
from agent_framework.openai import OpenAIChatClient

# 下載（如有需要）並在本地提供模型，然後發現端點/端口。
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

> **注意：** Foundry Local 暴露相容 OpenAI 的 **Chat Completions** 端點，用於本機開發和離線情境。若需完整的 **Responses API** 功能集（有狀態對話、深入工具協同和代理式開發），請導向 **Azure OpenAI** 或課程範例中的 **Microsoft Foundry** 專案。詳見 [Foundry Local 文件](https://foundrylocal.ai) 以瞭解最新模型目錄與平台支援。

## 課程 8（Bing Grounding Workflow）額外設定


課程 8 中的條件工作流程筆記本使用透過 Microsoft Foundry 的 **Bing grounding**。如果你計劃運行該範例，請將此變數添加到你的 `.env` 文件中：

| 變數 | 位置 |
|----------|-----------------|
| `BING_CONNECTION_ID` | Microsoft Foundry 入口網站 → 你的專案 → <strong>管理</strong> → <strong>已連接資源</strong> → 你的 Bing 連接 → 複製連接 ID |

## 疑難排解

### macOS 上的 SSL 證書驗證錯誤

如果你在 macOS 上遇到如下錯誤：

```plaintext
ssl.SSLCertVerificationError: [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: self-signed certificate in certificate chain
```

這是 macOS 上 Python 的已知問題，系統 SSL 證書不會自動被信任。請依序嘗試以下解決方案：

**選項 1：執行 Python 的 Install Certificates 腳本（推薦）**

```bash
# 將 3.XX 替換為你安裝嘅 Python 版本（例如 3.12 或 3.13）：
/Applications/Python\ 3.XX/Install\ Certificates.command
```

**選項 2：在你的筆記本中使用 `connection_verify=False`（僅適用於 GitHub Models 筆記本）**

在第 6 課筆記本（`06-building-trustworthy-agents/code_samples/06-system-message-framework.ipynb`）中，已包含註解掉的解決方法。建立客戶端時取消註解 `connection_verify=False`：

```python
client = ChatCompletionsClient(
    endpoint=endpoint,
    credential=AzureKeyCredential(token),
    connection_verify=False,  # 如果遇到憑證錯誤，請停用 SSL 驗證
)
```

> **⚠️ 警告：** 停用 SSL 驗證 (`connection_verify=False`) 會繞過證書驗證，降低安全性。僅在開發環境作為臨時解決方案使用，切勿用於生產環境。

**選項 3：安裝並使用 `truststore`**

```bash
pip install truststore
```

然後在筆記本或腳本中，進行任何網路呼叫前於頂部添加以下內容：

```python
import truststore
truststore.inject_into_ssl()
```

## 卡住了嗎？

如果運行本設置時遇到任何問題，歡迎加入我們的 <a href="https://discord.gg/kzRShWzttr" target="_blank">Azure AI 社群 Discord</a> 或 <a href="https://github.com/microsoft/ai-agents-for-beginners/issues?WT.mc_id=academic-105485-koreyst" target="_blank">提出問題</a>。

## 下一課

你現在已準備好運行本課程的程式碼。祝你學習 AI 代理的世界愉快！

[AI 代理及代理使用案例入門](../01-intro-to-ai-agents/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責聲明**：
本文件由 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 翻譯而成。雖然我們致力於確保準確性，但請注意，機器自動翻譯可能包含錯誤或不準確之處。原始文件的母語版本應被視為權威來源。對於重要資訊，建議進行專業人工翻譯。我們不對因使用本翻譯而產生的任何誤解或誤釋承擔責任。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->