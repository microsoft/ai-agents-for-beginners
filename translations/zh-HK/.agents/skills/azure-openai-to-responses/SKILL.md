---
name: azure-openai-to-responses
license: MIT
---
# 將 Python 應用程式從 Azure OpenAI Chat Completions 遷移至 Responses API

> **權威指南 — 請嚴格遵循**
>
> 本技能將使用 Azure OpenAI Chat Completions 的 Python 代碼庫
> 遷移至統一的 Responses API。請精確遵循這些指示。
> 不可隨意即興對應參數或發明 API 介面。

---

## 觸發條件

當使用者想要啟用本技能時：
- 將 Python 應用程式從 Azure OpenAI Chat Completions 遷移至 Responses API
- 將 Python OpenAI SDK 用法升級為最新的 Azure OpenAI API 格式
- 為 GPT-5 或更新版需要 Responses API 的模型準備 Python 程式碼
- 從 `AzureOpenAI` / `AsyncAzureOpenAI` 切換到帶 v1 端點的標準 `OpenAI` / `AsyncOpenAI` 用戶端
- 修正與 `AzureOpenAI` 構造函數或 `api_version` 相關的過時警告

---

## ⚠️ 模型相容性 — 請先檢查

> **遷移前，請確認你的 Azure OpenAI 部署支援 Responses API。**

### 1. 快速測試部署（最快）

```python
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ["AZURE_OPENAI_API_KEY"],
    base_url=f"{os.environ['AZURE_OPENAI_ENDPOINT'].rstrip('/')}/openai/v1/",
)

try:
    resp = client.responses.create(
        model=os.environ["AZURE_OPENAI_DEPLOYMENT"],
        input="ping",
        max_output_tokens=50,
        store=False,
    )
    print(f"✅ Deployment supports Responses API: {resp.output_text}")
except Exception as e:
    print(f"❌ Deployment does NOT support Responses API: {e}")
```

> <strong>注意</strong>：Azure OpenAI 中 `max_output_tokens` 最低為 16。低於 16 的值會回傳 400 錯誤。測試時請使用 50 以上。

如果此請求回傳 404，表示該部署的模型尚未支援 Responses。請參考下方文件或用支援的模型重新部署。

### 2. 檢查區域中的可用模型（推薦）

執行內建模型相容性工具，查看特定區域中有哪些模型支援 Responses API：

```bash
python migrate.py models --subscription YOUR_SUB_ID --location YOUR_REGION
```

該查詢即時連接 Azure ARM 並顯示相容性矩陣—哪些模型支援 Responses、結構化輸出、工具等。可用 `--filter gpt-5.1,gpt-5.2` 篩選結果，或 `--json` 用於腳本。

### 3. 完整模型支援參考

- <strong>即時查詢</strong>：`python migrate.py models`（見上方 — 區域特定，持續更新）
- <strong>瀏覽可用性</strong>: [模型摘要表及區域可用性](https://learn.microsoft.com/en-us/azure/foundry/foundry-models/concepts/models-sold-directly-by-azure?tabs=global-standard-aoai%2Cglobal-standard&pivots=azure-openai#model-summary-table-and-region-availability)
- <strong>快速入門與指南</strong>：**https://aka.ms/openai/start**

### ⚠️ 較舊模型的限制

> <strong>警告</strong>：較舊模型（早於 `gpt-4.1` 的版本）可能無法完整支援所有 Responses API 功能。
>
> 已知較舊模型的限制：
> - **`reasoning` 參數**：許多非推理模型不支援此參數。只在原始代碼已有 `reasoning` 時才遷移。
> - **`seed` 參數**：Responses API 完全不支援，請從所有請求中移除。
> - **透過 `text.format` 的結構化輸出**：舊模型可能無法可靠強制執行 `strict: true` 的 JSON schema。
> - <strong>工具協調</strong>：GPT-5+ 模型將工具調用整合進內部推理，舊模型在 Responses API 仍可使用工具，但缺乏深入的整合。
> - <strong>溫度限制</strong>：遷移至 `gpt-5` 時，溫度參數必須省略或設為 `1`。舊模型無此限制。

### O 系列推理模型（o1、o3-mini、o3、o4-mini）

O 系列模型有其獨特的參數限制。遷移針對 O 系列模型的應用時：

- **`temperature`**：必須設成 `1`（或省略）。O 系列模型不接受其他數值。
- **`max_completion_tokens` → `max_output_tokens`**：使用 Azure 專有 `max_completion_tokens` 的應用必須改用 `max_output_tokens`，並設定較高數值（4096 以上），因為推理過程中使用的 tokens 也會占用限制。
- **`reasoning_effort`**：若應用使用 `reasoning_effort`（低/中/高），請保留；Responses API 對 O 系列模型支援此參數。
- <strong>串流行為</strong>：O 系列模型可能會在推理完成前緩衝輸出，延後發送文字增量事件。串流仍有效，但首次 `response.output_text.delta` 可能比 GPT 模型延遲更久。
- **`top_p`**：O 系列模型不支援此參數，若出現請移除。
- <strong>工具使用</strong>：O 系列模型通過 Responses API 支援工具功能，與 GPT 模型類似，但工具呼叫協調質量因模型而異。

**行動 — 主動模型建議**：掃描階段檢查應用所用模型（部署名稱、環境變數、配置）。若模型低於 `gpt-4.1`（非 gpt-4.1+），主動告知使用者：
- 遷移在其目前模型上可行，基本支援文字、聊天、串流和工具。
- 新型模型（`gpt-5.1`、`gpt-5.2`）在工具協調、結構化輸出強制、推理和跨區域可用性等方面擁有更佳表現。
- 使用者可視情況考慮升級部署，此非遷移阻礙。

不可基於模型版本阻擋或拒絕遷移。此建議僅供參考。

### GitHub Models 不支援 Responses API

> **GitHub Models (`models.github.ai`, `models.inference.ai.azure.com`) 不支援 Responses API。**

若代碼庫有 GitHub Models 代碼路徑（尋找 `base_url` 指向 `models.github.ai` 或 `models.inference.ai.azure.com`），遷移時<strong>應完全移除</strong>。Responses API 需要 Azure OpenAI、OpenAI 或相容的本地端點（例如支援 Responses 的 Ollama）。

掃描期間的行動：
- 標記任何 GitHub Models 代碼路徑，待移除。

---

## 框架遷移

許多應用在 OpenAI 之上使用高階框架。遷移時，不僅是底層 OpenAI 呼叫，框架本身的 API 也會改變。

### Microsoft Agent Framework (MAF)

**先檢查你的 MAF 版本** — 遷移依賴於你是否使用 MAF 1.0.0+，或先前的 1.0.0 前測試版/RC。

#### MAF 1.0.0+ (agent-framework-openai >= 1.0.0)

`OpenAIChatClient` **已使用 Responses API** — 無需遷移。如代碼使用舊有的 `OpenAIChatCompletionClient`（使用 `chat.completions.create`），請換成 `OpenAIChatClient`。

| 舊版 | 新版 |
|--------|-------|
| `from agent_framework.openai import OpenAIChatCompletionClient` | `from agent_framework.openai import OpenAIChatClient` |
| `OpenAIChatCompletionClient(...)` | `OpenAIChatClient(...)` |

查看版本：`python -c "import agent_framework_openai; print(agent_framework_openai.__version__)"`

#### MAF 1.0.0 前版本（beta/rc）

在 1.0.0 前版本中，`OpenAIChatClient` 使用 Chat Completions。請升級至 `agent-framework-openai>=1.0.0`，使 `OpenAIChatClient` 預設使用 Responses API。

其他 API 如 `Agent` 和工具 API 無需更改。

### LangChain (`langchain-openai`)

為 `ChatOpenAI()` 新增 `use_responses_api=True`。同時將回應存取從 `.content` 改為 `.text`。

| 舊版 | 新版 |
|--------|-------|
| `ChatOpenAI(model=..., base_url=..., api_key=...)` | `ChatOpenAI(model=..., base_url=..., api_key=..., use_responses_api=True)` |
| `result['messages'][-1].content` | `result['messages'][-1].text` |

完整前後代碼示例請參閱 [cheat-sheet.md](./references/cheat-sheet.md)。

---

## 前端遷移指南

> **Responses API 屬於伺服器端問題。** 請先遷移 Python 後端；前端的 HTTP 合約應保持不變，除非你的後端僅做薄轉發——在這種情況下，考慮採用 Responses 請求格式，消除翻譯層。若前端使用客戶端金鑰直接呼叫 OpenAI，請先轉移這部分呼叫到後端。

### `@microsoft/ai-chat-protocol` 已過時

`@microsoft/ai-chat-protocol` npm 套件已停用，應換用 [`ndjson-readablestream`](https://www.npmjs.com/package/ndjson-readablestream)。若在前端遇到：

1. 替換 CDN 腳本標籤：
   ```html
   <!-- Before -->
   <script src="https://cdn.jsdelivr.net/npm/@microsoft/ai-chat-protocol@.../dist/iife/index.js"></script>
   <!-- After -->
   <script src="https://cdn.jsdelivr.net/npm/ndjson-readablestream@1.0.7/dist/ndjson-readablestream.umd.js"></script>
   ```
2. 移除 `AIChatProtocolClient` 實例化（`new ChatProtocol.AIChatProtocolClient("/chat")`）。
3. 將 `client.getStreamedCompletion(messages)` 改成直接對後端串流端點的 `fetch()` 呼叫。
4. 將 `for await (const response of result)` 替換為 `for await (const chunk of readNDJSONStream(response.body))`。
5. 將屬性存取從 `response.delta.content` / `response.error` 改為 `chunk.delta.content` / `chunk.error`。

---

## 目標

- 列出所有在 Azure OpenAI 使用 Chat Completions 或舊版 Completions 的 Python 呼叫點。
- 提出 Python 代碼庫的遷移計劃及執行順序。
- 套用安全且最小的修改切換至 Responses API。
- 更新呼叫者以使用 Responses 輸出架構；不保留向後相容的封裝。
- 執行測試及碼風檢查；修正遷移導致的瑣碎錯誤。
- 準備小且可審查的變更集並提供最終摘要和差異（不提交）。

---

## 護欄規則

- 僅修改 git 工作區內的檔案，絕不寫出範圍外。
- 不保留舊版相容層；代碼直接遷移到新 API 格式。
- 不留下標記/過渡性註解或備份檔案。
- 若先前使用串流，則保留串流語意；否則使用非串流模式。
- 若處於審核模式，執行命令或網路呼叫前需請求批准。
- 不執行 `git add`/`git commit`/`git push`，只產生工作區修改。

---

## 第 0 步：Azure OpenAI 用戶端遷移（前置條件）

若代碼庫使用 `AzureOpenAI` 或 `AsyncAzureOpenAI` 建構函數，請先遷移至標準 `OpenAI` / `AsyncOpenAI` 建構函數。Azure 專用建構函數自 `openai>=1.108.1` 起已被棄用。

### 為什麼使用 v1 API 路徑？

新的 `/openai/v1` 端點使用標準 `OpenAI()` 用戶端替代 `AzureOpenAI()`，不需 `api_version` 參數，且在 OpenAI 與 Azure OpenAI 上行為完全相同。此用戶端程式碼具未來適應性，無需管理版本。

### 主要變更

| 舊版 | 新版 |
|--------|-------|
| `AzureOpenAI` | `OpenAI` |
| `AsyncAzureOpenAI` | `AsyncOpenAI` |
| `azure_endpoint` | `base_url` |
| `azure_ad_token_provider` | `api_key` |
| `api_version=...` | 完全移除 |

### 清理檢查清單

- 從用戶端建構移除 `api_version` 參數。
- 從 `.env`、應用設定、Bicep/基礎結構檔移除 `AZURE_OPENAI_VERSION` / `AZURE_OPENAI_API_VERSION` 環境變數。
- 將 `.env`、應用設定、Bicep/基礎結構及測試夾具中的 `AZURE_OPENAI_CLIENT_ID` 改名為 `AZURE_CLIENT_ID`（Azure Identity SDK 標準慣例）。
- 確保 `requirements.txt` 或 `pyproject.toml` 中 openai 版本為 `>=1.108.1`。

### 環境變數遷移

| 舊環境變數 | 行動 | 備註 |
|-------------|--------|-------|
| `AZURE_OPENAI_VERSION` | <strong>移除</strong> | v1 端點不需 `api_version` |
| `AZURE_OPENAI_API_VERSION` | <strong>移除</strong> | 同上 |
| `AZURE_OPENAI_CLIENT_ID` | <strong>改名為</strong> → `AZURE_CLIENT_ID` | 用於 `ManagedIdentityCredential(client_id=...)` 的標準 Azure Identity SDK 慣例 |
| `AZURE_OPENAI_ENDPOINT` | <strong>保留</strong> | 用於 `base_url` 建立 |
| `AZURE_OPENAI_CHAT_DEPLOYMENT` | <strong>保留</strong> | 用於 `responses.create` 的 `model` 參數 |
| `AZURE_OPENAI_API_KEY` | <strong>保留</strong> | 用於金鑰認證的 `api_key` |

用戶端設定代碼範例（同步、非同步、EntraID、API key、多租戶）請見 [cheat-sheet.md](./references/cheat-sheet.md)。

---

## 第 1 步：偵測舊版呼叫

執行 [detect_legacy.py](../../../../../.agents/skills/azure-openai-to-responses/scripts/detect_legacy.py) 腳本尋找所有需遷移的呼叫點：

```bash
python skills/azure-openai-to-responses/scripts/detect_legacy.py .
```

或手動執行以下搜尋，每個匹配點均為遷移目標：

```bash
# 舊有 API 調用（必須重寫）
rg "chat\.completions\.create"
rg "ChatCompletion\.create"
rg "Completion\.create"

# 已棄用的 Azure 用戶端建構子（必須替換）
rg "AzureOpenAI\("
rg "AsyncAzureOpenAI\("

# 回應結構存取模式（必須更新）
rg "choices\[0\]\.message\.content"
rg "choices\[0\]\.delta\.content"
rg "choices\[0\]\.message\.function_call"
rg "choices\[0\]\.message\.tool_calls"

# 舊有巢狀格式的工具定義（必須扁平化）
rg '"function":\s*{\s*"name"'
rg "pydantic_function_tool"

# 舊格式的工具結果（必須轉換為 function_call_output）
rg '"role":\s*"tool"'
rg '"tool_call_id"'

# 已棄用的參數（必須移除或重新命名）
rg "response_format"
rg "max_tokens\b"        # 重新命名為 max_output_tokens
rg "['\"]seed['\"]"      # remove entirely

# 已棄用的環境變數（清理）
rg "AZURE_OPENAI_API_VERSION|AZURE_OPENAI_VERSION"
rg "AZURE_OPENAI_CLIENT_ID"  # 應該是 AZURE_CLIENT_ID

# GitHub 模型端點（必須移除 — 不支援回應 API）
rg "models\.github\.ai|models\.inference\.ai\.azure"

# 框架層級的舊有模式（必須更新）
rg "OpenAIChatCompletionClient"  # MAF 1.0.0+：替換為 OpenAIChatClient
rg "ChatOpenAI\(" | grep -v "use_responses_api"  # LangChain：需要 use_responses_api=True

# 測試基礎設施（必須更新）
rg "ChatCompletionChunk|AsyncCompletions\.create" tests/
rg "_azure_ad_token_provider" tests/
rg "prompt_filter_results|content_filter_results" tests/
rg "choices\[0\]" tests/

# 內容篩選錯誤主體存取（必須更新 — 結構已更改）
rg 'innererror.*content_filter_result|error\.body\["innererror"\]'
rg "content_filter_result\[" # 舊的單數形式 — 現在在 content_filters 陣列內是 content_filter_results（複數）

# 直接呼叫 Chat Completions 端點的原始 HTTP（必須更新 URL）
rg "/openai/deployments/.*/chat/completions"
rg "api-version="
```

### 判斷準則（偵測與重寫）

- **Chat Completions 用戶端**：`client.chat.completions.create` → `client.responses.create(...)`。

- **Azure 用戶端建構子**：`AzureOpenAI(...)` → `OpenAI(base_url=..., api_key=...)`。
- **工具（Tools）**：將函數呼叫工具定義從巢狀格式 (`{"type": "function", "function": {"name": ...}}`) 轉換為平坦的 Responses 格式 (`{"type": "function", "name": ...}`)；使用 `tool_choice`；將工具結果以 `{"type": "function_call_output", "call_id": ..., "output": ...}` 項目返回（而非 `{"role": "tool", ...}`）。
- <strong>工具迴圈</strong>：當模型回傳函數呼叫時，將 `response.output` 項目附加到對話紀錄（而非手動建立的 `{"role": "assistant", "tool_calls": [...]}` 字典），接著為每個結果附加 `function_call_output` 項目。
- <strong>少量範例工具呼叫</strong>：若對話包含硬編碼的工具呼叫範例，則將它們轉換為 `{"type": "function_call", "id": "fc_...", "call_id": "fc_...", ...}` + `{"type": "function_call_output", ...}` 項目。ID 必須以 `fc_` 開頭。
- **`pydantic_function_tool()`<strong>：此輔助函數仍產生舊的巢狀格式且</strong>不相容**於 `responses.create()`。請改用手動工具定義或平坦包裝器。
- <strong>多輪對話</strong>：於應用中維護對話歷史；用 `input` 項目傳遞之前回合。
- <strong>格式化</strong>：將 Chat 的頂層 `response_format` 替換為 Responses 的 `text.format`。標準格式為：`text={"format": {"type": "json_schema", "name": "Output", "strict": True, "schema": {...}}}`。
- <strong>內容項目</strong>：將 Chat `content[].type: "text"` 替換為 Responses `content[].type: "input_text"` 用於使用者/系統回合。
- <strong>圖片內容項目</strong>：將 Chat `content[].type: "image_url"` 替換為 Responses `content[].type: "input_image"`。`image_url` 欄位從巢狀物件 `{"url": "..."}` 改為平坦字串。請參考備忘單了解前後範例。
- <strong>推理欄位</strong>：**只有在原始程式碼已有 `reasoning` 時才進行遷移**。
- <strong>內容過濾錯誤處理</strong>：錯誤主體結構改變。Chat Completions 使用 `error.body["innererror"]["content_filter_result"]`（單數）；Responses API 使用 `error.body["content_filters"][0]["content_filter_results"]`（複數，陣列內）。存取 `innererror` 的程式碼將引發 `KeyError`，請改寫為新路徑。
- **原生 HTTP 呼叫**：若應用直接呼叫 Azure OpenAI REST API（透過 `requests`、`httpx` 等），使用 `/openai/deployments/{name}/chat/completions?api-version=...`，請改寫為 `/openai/v1/responses`。請求主體變更：`messages` → `input`、新增 `max_output_tokens` 和 `store: false`，移除 `api-version` 查詢參數。回應主體變更：`choices[0].message.content` → `output[0].content[0].text`（注意：`output_text` 是 SDK 的便利屬性，原生 REST JSON 不存在）。

---

## 步驟 2：套用遷移

### 遷移說明（Chat Completions → Responses）

- <strong>為何要遷移</strong>：Responses 是文本、工具和串流的統一 API；Chat Completions 是舊版。使用 GPT-5 時，為取得最佳效能需使用 Responses。
- **HTTP**：Azure 端點由 `/openai/deployments/{name}/chat/completions` 變更為 `/openai/v1/responses`。
- <strong>欄位</strong>：`messages` → `input`，`max_tokens` → `max_output_tokens`。`temperature` 不變。
- <strong>格式化</strong>：`response_format` → `text.format`（物件）。
- <strong>內容項目</strong>：將 Chat `content[].type: "text"` 替換為 Responses `content[].type: "input_text"` 用於系統/使用者回合。
- <strong>圖片內容項目</strong>：將 Chat `content[].type: "image_url"` 替換為 Responses `content[].type: "input_image"`。將 `image_url` 欄位從 `{"image_url": {"url": "..."}}` 平坦為 `{"image_url": "..."}`（純字串，可為 HTTPS URL 或 `data:image/...;base64,...` 的資料 URI）。

### 參數對照參考

| Chat Completions | Responses API |
|-----------------|---------------|
| `prompt` | `input` |
| `messages` | `input`（項目陣列） |
| `max_tokens` | `max_output_tokens` |
| `response_format` | `text.format`（物件） |
| `temperature` | `temperature`（不變） |
| `stop` | `stop`（不變） |
| `frequency_penalty` | `frequency_penalty`（不變） |
| `presence_penalty` | `presence_penalty`（不變） |
| `tools` / 函數呼叫 | `tools`（不變） |
| `seed` | <strong>移除</strong>（不支援） |
| `store` | `store`（設定為 `false`） |
| `content[].type: "text"` | `content[].type: "input_text"` |
| `content[].type: "image_url"` | `content[].type: "input_image"` |
| `"image_url": {"url": "..."}` | `"image_url": "..."`（平坦字串） |

完整前後範例程式碼請參考 [cheat-sheet.md](./references/cheat-sheet.md)。

測試基礎建設遷移（mock、快照、斷言）請參考 [test-migration.md](./references/test-migration.md)。

錯誤排查與注意事項請參考 [troubleshooting.md](./references/troubleshooting.md)。

---

## 資料保留與狀態管理

- 全部 Responses 請求都設定 `store: false`。
- 不可依賴前訊息 ID 或伺服器儲存的上下文；請保持狀態由客戶端管理並最小化元資料。

---

## 驗收標準

### 程式碼層級門檻（全部必須通過）

- [ ] 在遷移後的檔案中，`rg "chat\.completions\.create|ChatCompletion\.create|Completion\.create"` 無任何匹配。
- [ ] `rg "AzureOpenAI\(|AsyncAzureOpenAI\("` 無任何匹配 — 所有建構子皆使用帶 v1 端點的 `OpenAI`/`AsyncOpenAI`。
- [ ] `rg "models\.github\.ai|models\.inference\.ai\.azure"` 無任何匹配 — 移除 GitHub Models 相關程式碼路徑。
- [ ] `rg "OpenAIChatCompletionClient"` 無任何匹配 — MAF 1.0.0+ 程式碼使用 `OpenAIChatClient`（採用 Responses API）。若為 1.0.0 之前版本，請升級至 `agent-framework-openai>=1.0.0`。
- [ ] 所有 `ChatOpenAI(...)` 調用皆包含 `use_responses_api=True`。
- [ ] `rg "choices\[0\]"` 無任何匹配 — 所有回應存取皆使用 `resp.output_text` 或 Responses 輸出結構。
- [ ] 頂層不再有 `response_format`；所有結構化輸出皆使用 `text={"format": {...}}`。
- [ ] `requirements.txt` 或 `pyproject.toml` 中包含 `openai>=1.108.1` 與 `azure-identity`；並已重新安裝相依套件。
- [ ] 每次呼叫 `responses.create` 均設置 `store=False`。
- [ ] 客戶端建構時無 `api_version`；`AZURE_OPENAI_API_VERSION` 已從環境檔與基礎架構移除。

### 測試基礎建設門檻（全部必須通過）

- [ ] `rg "ChatCompletionChunk|AsyncCompletions\.create|chat\.completions" tests/` 無任何匹配。
- [ ] `rg "_azure_ad_token_provider" tests/` 無任何匹配 — 斷言更新為檢查 `isinstance(client, AsyncOpenAI)` 或 `base_url`。
- [ ] `rg "prompt_filter_results|content_filter_results" tests/` 無任何匹配 — 移除 Azure 專屬過濾 mock。
- [ ] mock fixture 使用 `kwargs.get("input")` 非 `kwargs.get("messages")`。
- [ ] 快照 / golden 檔案更新為 Responses 串流結構（無 `choices[0]`、`function_call`、`logprobs` 等）。
- [ ] `pytest` 執行通過且無失敗。

### 行為驗證門檻（手動或透過測試架構驗證）

- [ ] <strong>基本完成</strong>：非串流的 `responses.create` 回傳非空 `output_text`。
- [ ] <strong>串流等價</strong>：原始程式若使用串流，遷移程式需串流並產出帶有非空 delta 的 `response.output_text.delta` 事件。
- [ ] <strong>結構化輸出</strong>：若使用 `text.format` 包含 `json_schema`，`json.loads(resp.output_text)` 成功且符合結構。
- [ ] <strong>工具呼叫迴圈</strong>：若使用工具，模型會呼叫工具，應用執行後，後續請求會回傳最終的 `output_text`（無無限迴圈）。
- [ ] <strong>非同步等價</strong>：若使用 `AsyncAzureOpenAI`，等價的 `AsyncOpenAI` 能以 `await` 呼叫。
- [ ] <strong>錯誤率</strong>：與遷移前基準相比，不增加 400/401/404 的錯誤。

### 交付項目

- 概要包含編輯的檔案、遷移前後的舊版調用數量差異及後續步驟。
- 變更為工作目錄層級的程式碼編輯（不包含提交）。

---

## SDK 版本需求

| 套件 | 最低版本 |
|---------|----------------|
| `openai` | `>=1.108.1` |
| `azure-identity` | 最新版（用於 EntraID 驗證） |

---

## 參考資料

- [備忘單 — 全部程式碼片段](./references/cheat-sheet.md)
- [測試遷移 — mock、快照、斷言](./references/test-migration.md)
- [疑難排解 — 錯誤、風險表、注意事項](./references/troubleshooting.md)
- [detect_legacy.py — 自動掃描器](../../../../../.agents/skills/azure-openai-to-responses/scripts/detect_legacy.py)
- [Azure OpenAI 新手套件](https://aka.ms/openai/start)
- [Azure OpenAI Responses API 文件](https://learn.microsoft.com/en-us/azure/ai-foundry/openai/how-to/responses)
- [Azure OpenAI API 版本生命週期](https://learn.microsoft.com/en-us/azure/ai-foundry/openai/api-version-lifecycle?view=foundry-classic&tabs=python#api-evolution)
- [OpenAI Responses API 參考](https://platform.openai.com/docs/api-reference/responses)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責聲明**：
本文件由 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 翻譯而成。雖然我們致力於確保準確性，但請注意，機器自動翻譯可能包含錯誤或不準確之處。原始文件的母語版本應被視為權威來源。對於重要資訊，建議進行專業人工翻譯。我們不對因使用本翻譯而產生的任何誤解或誤釋承擔責任。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->