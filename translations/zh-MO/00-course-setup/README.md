# 課程設置

## 介紹

本課程將涵蓋如何運行本課程的程式碼範例。

## 加入其他學習者並獲得幫助

在開始克隆你的代碼倉庫之前，請加入 [AI Agents For Beginners Discord 頻道](https://aka.ms/ai-agents/discord) 以獲得設置支援、課程相關問題的協助，或與其他學習者交流。

## 克隆或分叉此倉庫

首先，請克隆或分叉此 GitHub 倉庫。這將建立你自己的課程資料版本，方便你運行、測試及調整程式碼！

你可以點擊 <a href="https://github.com/microsoft/ai-agents-for-beginners/fork" target="_blank">fork the repo</a> 來分叉倉庫

現在你應該擁有本課程的分叉版本，以下是連結：

![Forked Repo](../../../translated_images/zh-MO/forked-repo.33f27ca1901baa6a.webp)

### Shallow Clone（推薦用於工作坊 / Codespaces）

  > 完整的倉庫包含完整歷史和所有檔案可能會很大（約3 GB）。如果你只參加工作坊或只需要部分課程資料夾，淺克隆（或稀疏克隆）可以截斷歷史和/或跳過 blobs，避免大部分下載。

#### 快速淺克隆 — 節省歷史，所有檔案

將以下命令中的 `<your-username>` 替換成你的分叉 URL（或上游 URL，如果你願意）。

只克隆最新提交歷史（小型下載）：

```bash|powershell
git clone --depth 1 https://github.com/<your-username>/ai-agents-for-beginners.git
```

克隆特定分支：

```bash|powershell
git clone --depth 1 --branch <branch-name> https://github.com/<your-username>/ai-agents-for-beginners.git
```

#### 部分（稀疏）克隆 — 節省 blobs 並且只選擇指定資料夾

使用部分克隆和稀疏檢出（requires Git 2.25+，建議使用支援部分克隆的現代 Git）：

```bash|powershell
git clone --depth 1 --filter=blob:none --sparse https://github.com/<your-username>/ai-agents-for-beginners.git
```

進入倉庫資料夾：

```bash|powershell
cd ai-agents-for-beginners
```

然後指定你需要的資料夾（下面範例展示兩個資料夾）：

```bash|powershell
git sparse-checkout set 00-course-setup 01-intro-to-ai-agents
```

完成克隆並驗證檔案後，如果只需要檔案並且想釋放空間（無 git 歷史），請刪除倉庫元資料（💀不可恢復 — 你將失去所有 Git 功能：不能提交、拉取、推送或查看歷史）。

```bash
# zsh/bash
rm -rf .git
```

```powershell
# PowerShell
Remove-Item -Recurse -Force .git
```

#### 使用 GitHub Codespaces（推薦，以避免本地大量下載）

- 透過 [GitHub UI](https://github.com/codespaces) 為此倉庫建立新的 Codespace。  

- 在新建的 codespace 終端機中，執行上述淺克隆/稀疏克隆命令，只將所需課程資料夾帶入 Codespace 工作區。
- 選擇性：在 Codespaces 裡克隆後，移除 .git 以回收空間（見上述移除命令）。
- 注意：若你喜歡直接在 Codespaces 打開倉庫（不另行克隆），請注意 Codespaces 會建立 devcontainer 環境，可能會配置超出需求的內容。 在新 Codespace 中淺克隆則讓你更好控制硬碟使用。

#### 小提示

- 如果你要編輯/提交，務必替換成你的分叉 clone URL。
- 若日後需要更多歷史或檔案，可以抓取或調整稀疏檢出以包含更多資料夾。

## 執行程式碼

本課程提供一系列 Jupyter 筆記本，你可以運行以獲得 AI 代理構建的實作經驗。

程式碼範例使用 **Microsoft Agent Framework (MAF)** 與 `FoundryChatClient`，它透過 **Microsoft Foundry** 連接到 **Microsoft Foundry Agent Service V2**（Responses API）。

所有 Python 筆記本均標記為 `*-python-agent-framework.ipynb`。

## 需求

- Python 3.12+
  - <strong>注意</strong>：如果你沒有安裝 Python 3.12，請確保安裝，然後使用 python3.12 建立虛擬環境以確保從 requirements.txt 安裝正確版本。
  
    >範例

    建立 Python 虛擬環境目錄：

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

- .NET 10+：對使用 .NET 的範例程式碼，請確保安裝 [.NET 10 SDK](https://dotnet.microsoft.com/download/dotnet/10.0) 或更新版本。然後檢查安裝的 .NET SDK 版本：

    ```bash|powershell
    dotnet --list-sdks
    ```

- **Azure CLI** — 需要進行身份驗證。請從 [aka.ms/installazurecli](https://aka.ms/installazurecli) 安裝。
- **Azure 訂閱** — 用於存取 Microsoft Foundry 和 Microsoft Foundry Agent Service。
- **Microsoft Foundry 專案** — 有已部署模型的專案（例如 `gpt-5-mini`）。見下方 [第1步](#第-1-步：建立-microsoft-foundry-項目)。

我們在此倉庫根目錄包含了 `requirements.txt` 檔案，裡面包含了執行程式碼範例所需的全部 Python 套件。

你可以在終端機於倉庫根目錄執行以下指令來安裝：

```bash|powershell
pip install -r requirements.txt
```

建議建立 Python 虛擬環境，避免衝突與問題。

## 設定 VSCode

確認在 VSCode 中使用正確版本的 Python。

![image](https://github.com/user-attachments/assets/a85e776c-2edb-4331-ae5b-6bfdfb98ee0e)

## 設定 Microsoft Foundry 和 Microsoft Foundry Agent Service

### 第 1 步：建立 Microsoft Foundry 項目

你需要一個 Microsoft Foundry **hub** 和帶有已部署模型的 **project** 來運行筆記本。

1. 訪問 [ai.azure.com](https://ai.azure.com) 並用 Azure 帳戶登入。
2. 建立一個 **hub**（或使用已有的）。參考：[Hub 資源概覽](https://learn.microsoft.com/azure/ai-foundry/concepts/ai-resources)。
3. 在 hub 裡建立一個 **project**。
4. 從 **Models + Endpoints** → **Deploy model** 部署模型（如 `gpt-5-mini`）。

### 第 2 步：取得你的專案端點和模型部署名稱

在 Microsoft Foundry 控制台你的專案頁面：

- <strong>專案端點</strong> — 移至 **Overview** 頁面複製端點 URL。

![Project Connection String](../../../translated_images/zh-MO/project-endpoint.8cf04c9975bbfbf1.webp)

- <strong>模型部署名稱</strong> — 在 **Models + Endpoints** 選擇你的部署模型，記下 **Deployment name**（如 `gpt-5-mini`）。

### 第 3 步：使用 `az login` 登入 Azure

所有筆記本都使用 **`AzureCliCredential`** 進行驗證 — 無需管理 API 金鑰。你必須透過 Azure CLI 登入。

1. 若尚未安裝 Azure CLI，請安裝：[aka.ms/installazurecli](https://aka.ms/installazurecli)

2. 透過以下指令登入：

    ```bash|powershell
    az login
    ```

    若在無瀏覽器的遠端/Codespace 環境：

    ```bash|powershell
    az login --use-device-code
    ```

3. 若被提示，<strong>選擇訂閱</strong> — 選擇包含你的 Foundry 專案的訂閱。

4. 驗證你已成功登入：

    ```bash|powershell
    az account show
    ```

> **為何使用 `az login`？** 筆記本透過 `azure-identity` 套件中的 `AzureCliCredential` 來認證。這表示 Azure CLI 的登入會話提供認證 — 你的 `.env` 不需要 API 金鑰或秘密。這是[安全最佳實踐](https://learn.microsoft.com/azure/developer/ai/keyless-connections)。

### 第 4 步：建立你的 `.env` 檔案

複製示例檔案：

```bash
# zsh/bash
cp .env.example .env
```

```powershell
# PowerShell
Copy-Item .env.example .env
```

打開 `.env` 檔案並填入以下兩個值：

```env
AZURE_AI_PROJECT_ENDPOINT=https://<your-project>.services.ai.azure.com/api/projects/<your-project-id>
AZURE_AI_MODEL_DEPLOYMENT_NAME=gpt-5-mini
```

| 變數 | 找尋位置 |
|----------|-----------------|
| `AZURE_AI_PROJECT_ENDPOINT` | Foundry 控制台 → 你的專案 → **Overview** 頁面 |
| `AZURE_AI_MODEL_DEPLOYMENT_NAME` | Foundry 控制台 → **Models + Endpoints** → 你的已部署模型名稱 |

大部分課程就此完成！筆記本會自動透過你的 `az login` 會話認證。

### 第 5 步：安裝 Python 依賴套件

```bash|powershell
pip install -r requirements.txt
```

建議在你先前建立的虛擬環境中執行。

## 第 5 課額外設置（Agentic RAG）

第 5 課使用 **Azure AI Search** 作檢索增強生成。如果你計劃運行該課程，請將變數加入 `.env` 檔案：

| 變數 | 找尋位置 |
|----------|-----------------|
| `AZURE_SEARCH_SERVICE_ENDPOINT` | Azure 控制台 → 你的 **Azure AI Search** 資源 → **Overview** → URL |
| `AZURE_SEARCH_API_KEY` | Azure 控制台 → 你的 **Azure AI Search** 資源 → **Settings** → **Keys** → 主管理金鑰 |

## 直接呼叫 Azure OpenAI 的課程額外設置（第 6 和 8 課）

部分第 6 和第 8 課的筆記本直接呼叫 **Azure OpenAI**（使用 **Responses API**），而非透過 Microsoft Foundry 專案。這些範例先前使用 GitHub Models，此方案已被棄用（2026 年 7 月退休），且不支援 Responses API。如果你打算運行這些範例，請加入以下變數到 `.env`：

| 變數 | 找尋位置 |
|----------|-----------------|
| `AZURE_OPENAI_ENDPOINT` | Azure 控制台 → 你的 **Azure OpenAI** 資源 → **Keys and Endpoint** → Endpoint（例如 `https://<your-resource>.openai.azure.com`） |
| `AZURE_OPENAI_DEPLOYMENT` | 你部署的模型名稱（例如 `gpt-5-mini`），支援 Responses API |
| `AZURE_OPENAI_API_KEY` | 選用 — 僅當你使用基於金鑰的認證取代 `az login` / Entra ID 時 |

> Responses API 使用穩定的 `/openai/v1/` 端點，無需 `api-version`。透過 `az login` 以無鑰 Entra ID 驗證方式登入。

## 替代提供者：MiniMax（兼容 OpenAI）

[MiniMax](https://platform.minimaxi.com/) 提供大型上下文模型（最多 204K 代幣），透過 OpenAI 兼容 API。由於 Microsoft Agent Framework 的 `OpenAIChatClient` 支援任何 OpenAI 兼容端點，因此你可以將 MiniMax 作為 Azure OpenAI 或 OpenAI 的替代方案。

將這些變數加入 `.env`：

| 變數 | 找尋位置 |
|----------|-----------------|
| `MINIMAX_API_KEY` | [MiniMax 平台](https://platform.minimaxi.com/) → API 金鑰 |
| `MINIMAX_BASE_URL` | 使用 `https://api.minimax.io/v1`（預設值） |
| `MINIMAX_MODEL_ID` | 你想使用的模型名稱（例如 `MiniMax-M3`） |

<strong>範例模型</strong>：`MiniMax-M3`（推薦）, `MiniMax-M2.7`, `MiniMax-M2.7-highspeed`（更快響應）。模型名稱與可用性會隨時間變更，且可用模型依帳號或地區而定 — 請查看 [MiniMax 平台](https://platform.minimaxi.com/) 以獲最新清單。如果 `MiniMax-M3` 你無法使用，請將 `MINIMAX_MODEL_ID` 設為你能使用的模型（如 `MiniMax-M2.7`）。

使用 `OpenAIChatClient` 的程式碼範例（如第 14 課旅館訂房工作流程）會在設定 `MINIMAX_API_KEY` 時自動偵測並使用你的 MiniMax 配置。

## 替代提供者：Foundry Local（在設備上執行模型）

[Foundry Local](https://foundrylocal.ai) 是輕量級執行環境，將語言模型<strong>完整下載、管理並在你的機器上提供服務</strong>，使用 OpenAI 兼容 API — 無需雲端、無需 Azure 訂閱，也無需 API 金鑰。非常適合離線開發、無雲端花費實驗，或讓資料保持在本地。

因為 Microsoft Agent Framework 的 `OpenAIChatClient` 支援任何 OpenAI 兼容端點，Foundry Local 是 Azure OpenAI 的本地替代方案。

**1. 安裝 Foundry Local**

```bash
# Windows 作業系統
winget install Microsoft.FoundryLocal

# macOS 作業系統
brew install foundrylocal
```

**2. 下載並運行模型**（同時啟動本地服務）：

```bash
foundry model list          # 查看可用型號
foundry model run phi-4-mini
```

**3. 安裝用於發現本地端點的 Python SDK：**

```bash
pip install foundry-local-sdk
```

**4. 指定 Microsoft Agent Framework 使用你的本地模型：**

```python
from foundry_local import FoundryLocalManager
from agent_framework.openai import OpenAIChatClient

# 下載（如有需要）並本地提供模型，然後偵測端點/端口。
manager = FoundryLocalManager("phi-4-mini")

chat_client = OpenAIChatClient(
    base_url=manager.endpoint,      # 例如 http://localhost:<port>/v1
    api_key=manager.api_key,        # 對於 Foundry Local 常為「不需要」。
    model_id=manager.get_model_info("phi-4-mini").id,
)

agent = chat_client.as_agent(
    name="LocalAgent",
    instructions="You are a helpful assistant running fully on-device.",
)
```

> **注意：** Foundry Local 暴露 OpenAI 兼容的<strong>聊天完成</strong>端點。適用於本地開發和離線場景。若需完整<strong>Responses API</strong>功能集（有狀態對話、深入工具編排、代理式開發），請選用 **Azure OpenAI** 或 **Microsoft Foundry** 專案（如課程所示）。詳情請參閱 [Foundry Local 文件](https://foundrylocal.ai) 了解當前模型目錄與平台支援。

## 第 8 課額外設置（Bing Grounding 工作流程）


課程 8 中的條件工作流程筆記本使用透過 Microsoft Foundry 的 **Bing 基座**。如果你計劃運行該範例，請將此變數添加到你的 `.env` 文件中：

| 變數 | 位置 |
|----------|-----------------|
| `BING_CONNECTION_ID` | Microsoft Foundry 入口網站 → 你的專案 → <strong>管理</strong> → <strong>已連接資源</strong> → 你的 Bing 連線 → 複製連線 ID |

## 疑難排解

### macOS 上的 SSL 憑證驗證錯誤

如果你使用 macOS 且遇到類似以下錯誤：

```plaintext
ssl.SSLCertVerificationError: [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: self-signed certificate in certificate chain
```

這是 macOS 上 Python 的已知問題，系統 SSL 憑證不會自動被信任。請依序嘗試以下解決方案：

**選項 1：執行 Python 的 Install Certificates 腳本（推薦）**

```bash
# 將 3.XX 替換成你已安裝的 Python 版本（例如，3.12 或 3.13）：
/Applications/Python\ 3.XX/Install\ Certificates.command
```

**選項 2：在你的筆記本中使用 `connection_verify=False`（僅限 GitHub Models 筆記本）**

在課程 6 筆記本（`06-building-trustworthy-agents/code_samples/06-system-message-framework.ipynb`）中，已包含註解的解決方案。建立客戶端時取消註解 `connection_verify=False`：

```python
client = ChatCompletionsClient(
    endpoint=endpoint,
    credential=AzureKeyCredential(token),
    connection_verify=False,  # 如果您遇到證書錯誤，請停用 SSL 驗證
)
```

> **⚠️ 警告：** 停用 SSL 驗證（`connection_verify=False`）會透過跳過憑證驗證降低安全性。請僅在開發環境中作為臨時解決方法使用，切勿用於生產環境。

**選項 3：安裝並使用 `truststore`**

```bash
pip install truststore
```

然後在你筆記本或腳本開頭、進行任何網絡呼叫之前加上以下代碼：

```python
import truststore
truststore.inject_into_ssl()
```

## 卡住了嗎？

如果你在執行此設定時有任何問題，歡迎加入我們的 <a href="https://discord.gg/kzRShWzttr" target="_blank">Azure AI 社群 Discord</a> 或 <a href="https://github.com/microsoft/ai-agents-for-beginners/issues?WT.mc_id=academic-105485-koreyst" target="_blank">提出問題</a>。

## 下一課

你現在已經準備好運行此課程的程式碼。祝你學習 AI Agent 世界愉快！

[AI Agent 與代理使用案例介紹](../01-intro-to-ai-agents/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責聲明**：
本文件使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。雖然我們力求準確，但請注意，自動翻譯可能包含錯誤或不準確之處。原始文件的母語版本應被視為權威來源。對於重要資訊，建議尋求專業人工翻譯。我們不對因使用本翻譯而引起的任何誤解或曲解承擔責任。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->