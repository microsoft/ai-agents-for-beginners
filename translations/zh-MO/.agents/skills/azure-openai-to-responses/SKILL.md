---
name: azure-openai-to-responses
license: MIT
---
# 將 Python 應用程式從 Azure OpenAI Chat Completions 遷移到 Responses API

> **權威指南 — 請嚴格遵循**
>
> 本技能協助遷移使用 Azure OpenAI Chat Completions 的 Python 程式碼庫
> 至統一的 Responses API。請嚴格按照這些指示執行。
> 請勿即興映射參數或自行創建 API 結構。

---

## 啟動條件

當用戶希望執行下列操作時啟用此技能：
- 將 Python 應用程式從 Azure OpenAI Chat Completions 遷移至 Responses API
- 將 Python OpenAI SDK 用法升級至針對 Azure OpenAI 的最新 API 結構
- 為 GPT-5 或更新版本需要在 Azure 上使用 Responses 的模型準備 Python 程式碼
- 從 `AzureOpenAI`/`AsyncAzureOpenAI` 切換至使用標準的 `OpenAI`/`AsyncOpenAI` 客戶端及 v1 端點
- 修正與 `AzureOpenAI` 建構函式或 `api_version` 相關的棄用警告

---

## ⚠️ 模型相容性 — 請先確認

> **遷移前，請確認您的 Azure OpenAI 部署支援 Responses API。**

### 1. 簡易測試您的部署（最快速）

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

> <strong>注意</strong>：Azure OpenAI 上的 `max_output_tokens` 最小值為 **16**。小於 16 將返回 400 錯誤。簡易測試請使用 50 以上。

若此請求返回 404，表示該部署使用的模型尚未支援 Responses，請參考下面的參考資料或重新部署支援的模型。

### 2. 檢查您區域可用模型（推薦）

運行內建的模型相容性工具來查看您區域有哪些模型支援 Responses API：

```bash
python migrate.py models --subscription YOUR_SUB_ID --location YOUR_REGION
```

此命令會查詢 Azure ARM 實時狀態並展示相容性矩陣 — 哪些模型支援 Responses、結構化輸出、工具等。可用 `--filter gpt-5.1,gpt-5.2` 篩選結果，或用 `--json` 做腳本處理。

### 3. 完整模型相容參考

- <strong>即時查詢</strong>：`python migrate.py models`（如上述所示 — 依區域不同，資料永遠最新）
- <strong>瀏覽可用性</strong>：[模型摘要表及區域可用性](https://learn.microsoft.com/en-us/azure/foundry/foundry-models/concepts/models-sold-directly-by-azure?tabs=global-standard-aoai%2Cglobal-standard&pivots=azure-openai#model-summary-table-and-region-availability)
- <strong>快速入門與指南</strong>：**https://aka.ms/openai/start**

### ⚠️ 舊版模型限制

> <strong>警告</strong>：舊版模型（`gpt-4.1` 之前的）可能無法完全支援所有 Responses API 功能。
>
> 舊版模型已知限制：
> - **`reasoning` 參數**：許多非推理模型不支援。只有原本代碼使用過才遷移此參數。
> - **`seed` 參數**：Responses API 完全不支援，務必移除。
> - **透過 `text.format` 的結構化輸出**：舊版模型可能無法穩定強制 `strict: true` 的 JSON 架構。
> - <strong>工具編排</strong>：GPT-5+ 在推理中整合工具呼叫。舊版模型仍運作，但缺乏此深入整合。
> - <strong>溫度限制</strong>：遷移至 `gpt-5` 時，溫度需省略或設定為 `1`。舊版模型無此限制。

### O 系列推理模型 (o1, o3-mini, o3, o4-mini)

O 系列模型有特別的參數限制。遷移針對 O 系列模型的應用程式時：

- **`temperature`**：必須是 `1`（或省略）。O 系列不接受其他值。
- **`max_completion_tokens` → `max_output_tokens`**：使用 Azure 專屬的 `max_completion_tokens` 的應用需切換至 `max_output_tokens`。由於推理會消耗 Token，設定較高值（4096 以上）。
- **`reasoning_effort`**：若使用 `reasoning_effort`（low/medium/high），保留即可 — Responses API 支援 O 系列模型這參數。
- <strong>串流行為</strong>：O 系列模型可能會緩衝輸出直到推理完成才發出文字差異事件。串流仍可用，但第一個 `response.output_text.delta` 可能較 GPT 模型延遲較久才送達。
- **`top_p`**：O 系列不支援此參數 — 若存在請移除。
- <strong>工具使用</strong>：O 系列模型透過 Responses API 支援工具，與 GPT 模型相同，但工具呼叫編排品質因模型不同而異。

**措施 — 主動模型諮詢**：掃描階段檢查應用程式目標模型（部署名稱、環境變數、設定）。若模型為 `gpt-4.1` 之前版本，主動告知用戶：
- 對其目前模型，遷移可支援基本文字、聊天、串流及工具功能。
- 較新模型（`gpt-5.1`、`gpt-5.2`）提供更好的工具編排、結構化輸出強制、推理和跨區域可用性。
- 建議用戶在準備好時考慮升級部署 — 並非遷移阻礙。

不要以模型版本為由阻止或拒絕遷移。此諮詢為資訊性提示。

### GitHub Models 不支援 Responses API

> **GitHub Models (`models.github.ai`, `models.inference.ai.azure.com`) 不支援 Responses API。**

若程式碼中有 GitHub Models 路徑（例如 `base_url` 指向 `models.github.ai` 或 `models.inference.ai.azure.com`），<strong>請在遷移時完全移除</strong>。Responses API 需使用 Azure OpenAI、OpenAI 或相容的本地端點（例如支援 Responses 的 Ollama）。

掃描時應採取的措施：
- 標示任何 GitHub Models 路徑以便移除。

---

## 框架遷移

許多應用程式使用封裝 OpenAI 的高階框架。遷移這些框架時，不僅底層 OpenAI 呼叫改變，框架自身的 API 也會變更。

### Microsoft Agent Framework (MAF)

**首先檢查您的 MAF 版本** — 遷移將依您使用的是 MAF 1.0.0+ 還是 1.0.0 之前的 beta/rc 版本而異。

#### MAF 1.0.0+ (agent-framework-openai >= 1.0.0)

`OpenAIChatClient` **已經使用 Responses API** — 無需遷移。若程式碼使用舊版 `OpenAIChatCompletionClient`（基於 `chat.completions.create`），請改用 `OpenAIChatClient`。

| 之前 | 之後 |
|--------|-------|
| `from agent_framework.openai import OpenAIChatCompletionClient` | `from agent_framework.openai import OpenAIChatClient` |
| `OpenAIChatCompletionClient(...)` | `OpenAIChatClient(...)` |

查看版本：`python -c "import agent_framework_openai; print(agent_framework_openai.__version__)"` 

#### MAF 1.0.0 之前版本（beta/rc）

在 MAF 1.0.0 之前版本中，`OpenAIChatClient` 使用 Chat Completions。請升級到 `agent-framework-openai>=1.0.0`，它會預設使用 Responses API 的 `OpenAIChatClient`。

其他 API（如 `Agent` 和工具）不變。

### LangChain (`langchain-openai`)

在 `ChatOpenAI()` 中新增 `use_responses_api=True`。並更新響應訪問方式，從 `.content` 改為 `.text`。

| 之前 | 之後 |
|--------|-------|
| `ChatOpenAI(model=..., base_url=..., api_key=...)` | `ChatOpenAI(model=..., base_url=..., api_key=..., use_responses_api=True)` |
| `result['messages'][-1].content` | `result['messages'][-1].text` |

完整前後代碼範例，請參考 [cheat-sheet.md](./references/cheat-sheet.md)。

---

## 前端遷移指導

> **Responses API 是後端處理。** 請遷移您的 Python 後端；前端的 HTTP 合約應保持不變，除非您的後端只是個簡單轉送層 — 在那種情況下，考慮採用 Responses 請求結構以消除翻譯層。若前端使用客戶端密鑰直接呼叫 OpenAI，請先將這些呼叫移至後端。

### `@microsoft/ai-chat-protocol` 棄用

`@microsoft/ai-chat-protocol` npm 包已棄用，應改用 [`ndjson-readablestream`](https://www.npmjs.com/package/ndjson-readablestream)。若前端遇到此包：

1. 替換 CDN 腳本標籤：
   ```html
   <!-- Before -->
   <script src="https://cdn.jsdelivr.net/npm/@microsoft/ai-chat-protocol@.../dist/iife/index.js"></script>
   <!-- After -->
   <script src="https://cdn.jsdelivr.net/npm/ndjson-readablestream@1.0.7/dist/ndjson-readablestream.umd.js"></script>
   ```
2. 移除 `AIChatProtocolClient` 實例化（`new ChatProtocol.AIChatProtocolClient("/chat")`）。
3. 將 `client.getStreamedCompletion(messages)` 改成直接 `fetch()` 後端串流端點。
4. 將 `for await (const response of result)` 改為 `for await (const chunk of readNDJSONStream(response.body))`。
5. 更新屬性訪問方式，從 `response.delta.content` / `response.error` 改為 `chunk.delta.content` / `chunk.error`。

---

## 目標

- 枚舉所有使用 Chat Completions 或舊版 Completions 呼叫 Azure OpenAI 的 Python 呼叫點。
- 擬定 Python 程式碼庫的遷移計畫與順序。
- 採用安全且最小修改方式切換至 Responses API。
- 更新呼叫端以消費 Responses 輸出結構；不使用任何向後相容包裝。
- 執行測試與靜態檢查；修正遷移導致的小錯誤。
- 準備小且可審核的變更集，並提供最終摘要及差異 (不執行 commit)。

---

## 防護措施

- 僅修改 Git 工作區內的檔案，禁止對工作區外寫入。
- 不保留向後相容性 shim；直接遷移至新 API 結構。
- 不留存銘碑註解或備份檔案。
- 若先前使用串流，務必保留串流語意；否則可改為非串流。
- 若為審批模式，操作命令或網絡呼叫前請先取得批准。
- 不執行 `git add`/`git commit`/`git push`；僅產生工作樹修改。

---

## 第 0 步：Azure OpenAI 客戶端遷移（先決條件）

若程式碼庫使用 `AzureOpenAI` 或 `AsyncAzureOpenAI` 建構子，請先遷移到標準的 `OpenAI` / `AsyncOpenAI` 建構子。Azure 專屬建構子在 `openai>=1.108.1` 中已棄用。

### 為何使用 v1 API 路徑？

新的 `/openai/v1` 端點使用標準的 `OpenAI()` 客戶端替代 `AzureOpenAI()`，無需 `api_version` 參數，在 OpenAI 和 Azure OpenAI 間行為一致。相同的客戶端代碼具有未來相容性 — 無需版本管理。

### 關鍵改變

| 之前 | 之後 |
|--------|-------|
| `AzureOpenAI` | `OpenAI` |
| `AsyncAzureOpenAI` | `AsyncOpenAI` |
| `azure_endpoint` | `base_url` |
| `azure_ad_token_provider` | `api_key` |
| `api_version=...` | 完全移除 |

### 清理清單

- 移除建構客戶端時的 `api_version` 參數。
- 從 `.env`、應用設置及 Bicep/基礎架構檔移除 `AZURE_OPENAI_VERSION` / `AZURE_OPENAI_API_VERSION` 環境變數。
- 將 `.env`、應用設置、Bicep/基礎架構及測試 fixture 中的 `AZURE_OPENAI_CLIENT_ID` 改名為 `AZURE_CLIENT_ID`（符合 Azure 身分識別 SDK 標準慣例）。
- 確保在 `requirements.txt` 或 `pyproject.toml` 中使用 `openai>=1.108.1`。

### 環境變數遷移

| 舊環境變數 | 措施 | 備註 |
|-------------|--------|-------|
| `AZURE_OPENAI_VERSION` | <strong>移除</strong> | v1 端點不需 `api_version` |
| `AZURE_OPENAI_API_VERSION` | <strong>移除</strong> | 同上 |
| `AZURE_OPENAI_CLIENT_ID` | <strong>改名</strong> → `AZURE_CLIENT_ID` | Azure 身分識別 SDK 的標準 `ManagedIdentityCredential(client_id=...)` 慣例 |
| `AZURE_OPENAI_ENDPOINT` | <strong>保留</strong> | 仍用於 `base_url` 建構 |
| `AZURE_OPENAI_CHAT_DEPLOYMENT` | <strong>保留</strong> | 用作 `responses.create` 的 `model` 參數 |
| `AZURE_OPENAI_API_KEY` | <strong>保留</strong> | 用於基於金鑰的認證 `api_key` |

有關客戶端設置代碼範例（同步、非同步、EntraID、API 金鑰、多租戶）請參考 [cheat-sheet.md](./references/cheat-sheet.md)。

---

## 第 1 步：偵測舊版呼叫點

執行 [detect_legacy.py](../../../../../.agents/skills/azure-openai-to-responses/scripts/detect_legacy.py) 腳本以找到所有需要遷移的呼叫點：

```bash
python skills/azure-openai-to-responses/scripts/detect_legacy.py .
```

或手動執行此類搜尋 — 每個匹配即為遷移目標：

```bash
# 傳統 API 調用（必須重寫）
rg "chat\.completions\.create"
rg "ChatCompletion\.create"
rg "Completion\.create"

# 已棄用的 Azure 客戶端建構子（必須替換）
rg "AzureOpenAI\("
rg "AsyncAzureOpenAI\("

# 回應結構存取模式（必須更新）
rg "choices\[0\]\.message\.content"
rg "choices\[0\]\.delta\.content"
rg "choices\[0\]\.message\.function_call"
rg "choices\[0\]\.message\.tool_calls"

# 舊巢狀格式的工具定義（必須扁平化）
rg '"function":\s*{\s*"name"'
rg "pydantic_function_tool"

# 舊格式的工具結果（必須轉換為 function_call_output）
rg '"role":\s*"tool"'
rg '"tool_call_id"'

# 已棄用的參數（必須刪除或重新命名）
rg "response_format"
rg "max_tokens\b"        # 重新命名為 max_output_tokens
rg "['\"]seed['\"]"      # remove entirely

# 已棄用的環境變量（清理）
rg "AZURE_OPENAI_API_VERSION|AZURE_OPENAI_VERSION"
rg "AZURE_OPENAI_CLIENT_ID"  # 應該是 AZURE_CLIENT_ID

# GitHub 模型端點（必須移除 — 不支援 Responses API）
rg "models\.github\.ai|models\.inference\.ai\.azure"

# 框架層級的傳統模式（必須更新）
rg "OpenAIChatCompletionClient"  # MAF 1.0.0+：替換成 OpenAIChatClient
rg "ChatOpenAI\(" | grep -v "use_responses_api"  # LangChain：需要 use_responses_api=True

# 測試基礎設施（必須更新）
rg "ChatCompletionChunk|AsyncCompletions\.create" tests/
rg "_azure_ad_token_provider" tests/
rg "prompt_filter_results|content_filter_results" tests/
rg "choices\[0\]" tests/

# 內容過濾錯誤主體存取（必須更新 — 結構已更改）
rg 'innererror.*content_filter_result|error\.body\["innererror"\]'
rg "content_filter_result\[" # 舊單數形式 — 現在是 content_filters 陣列內的 content_filter_results（複數）

# 對 Chat Completions 端點的原始 HTTP 調用（必須更新 URL）
rg "/openai/deployments/.*/chat/completions"
rg "api-version="
```

### 偵測與重寫的啟發式

- **Chat Completions 客戶端**：從 `client.chat.completions.create` → `client.responses.create(...)`。

- **Azure 用戶端建構子**：`AzureOpenAI(...)` → `OpenAI(base_url=..., api_key=...)`。
- <strong>工具</strong>：將函式呼叫工具定義從巢狀格式 (`{"type": "function", "function": {"name": ...}}`) 轉換成平坦的 Responses 格式 (`{"type": "function", "name": ...}`)；使用 `tool_choice`；返回工具結果為 `{"type": "function_call_output", "call_id": ..., "output": ...}` 項目（而非 `{"role": "tool", ...}`）。
- <strong>工具迴圈往返</strong>：當模型返回函式呼叫時，將 `response.output` 項目追加到對話中（非手動的 `{"role": "assistant", "tool_calls": [...]}` 字典），然後為每個結果追加 `function_call_output` 項目。
- <strong>少量範例工具呼叫</strong>：若對話包括硬編碼的工具呼叫範例，將它們轉換成 `{"type": "function_call", "id": "fc_...", "call_id": "fc_...", ...}` + `{"type": "function_call_output", ...}` 項目。ID 必須以 `fc_` 開頭。
- **`pydantic_function_tool()`<strong>：此輔助函式仍會產生舊有的巢狀格式，</strong>不相容**於 `responses.create()`。請改用手動工具定義或扁平化包裝器。
- <strong>多輪互動</strong>：在應用中維護對話歷史；傳遞先前回合透過 `input` 項目。
- <strong>格式</strong>：以 Responses 取代 Chat 的頂層 `response_format`，改為使用 `text.format`。規範格式：`text={"format": {"type": "json_schema", "name": "Output", "strict": True, "schema": {...}}}`。
- <strong>內容項目</strong>：將 Chat 的 `content[].type: "text"` 替換為 Responses 的 `content[].type: "input_text"`（用戶／系統回合）。
- <strong>圖像內容項目</strong>：將 Chat 的 `content[].type: "image_url"` 替換為 Responses 的 `content[].type: "input_image"`。`image_url` 欄位從巢狀物件 `{"url": "..."}` 變成扁平字串。詳見速查表前後範例。
- <strong>推理努力</strong>：**僅在原始程式已有 `reasoning` 字段時遷移**。
- <strong>內容過濾錯誤處理</strong>：錯誤主體結構變更。Chat Completions 使用 `error.body["innererror"]["content_filter_result"]`（單數）；Responses API 使用 `error.body["content_filters"][0]["content_filter_results"]`（複數，陣列中）。存取 `innererror` 的程式將引發 `KeyError`。請改用新路徑。
- **原始 HTTP 呼叫**：若應用直接呼叫 Azure OpenAI REST API（透過 `requests`、`httpx` 等）使用 `/openai/deployments/{name}/chat/completions?api-version=...`，請改寫為 `/openai/v1/responses`。請求主體變更：`messages` → `input`、新增 `max_output_tokens` 和 `store: false`、移除 `api-version` 查詢參數。回應主體變更：`choices[0].message.content` → `output[0].content[0].text`（註：`output_text` 為 SDK 方便屬性，原生 REST JSON 中無）。

---

## 步驟 2：應用遷移

### 遷移注意事項 (Chat Completions → Responses)

- <strong>為何要遷移</strong>：Responses 是文字、工具及串流統一 API；Chat Completions 為舊版。搭配 GPT-5，必須使用 Responses 以達最佳效能。
- **HTTP**：Azure 端點從 `/openai/deployments/{name}/chat/completions` 轉至 `/openai/v1/responses`。
- <strong>欄位</strong>：`messages` → `input`，`max_tokens` → `max_output_tokens`。`temperature` 不變。
- <strong>格式</strong>：`response_format` → `text.format`（物件格式）。
- <strong>內容項目</strong>：替換 Chat 的 `content[].type: "text"` 為 Responses 的 `content[].type: "input_text"`，適用於系統／使用者回合。
- <strong>圖像內容項目</strong>：替換 Chat 的 `content[].type: "image_url"` 為 Responses 的 `content[].type: "input_image"`。將 `image_url` 欄位從 `{"image_url": {"url": "..."}}` 扁平化為 `{"image_url": "..."}`（純字串—HTTPS URL 或 `data:image/...;base64,...` 資料 URI）。

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
| `tools` / 函式呼叫 | `tools`（不變） |
| `seed` | <strong>移除</strong>（不支援） |
| `store` | `store`（設定為 `false`） |
| `content[].type: "text"` | `content[].type: "input_text"` |
| `content[].type: "image_url"` | `content[].type: "input_image"` |
| `"image_url": {"url": "..."}` | `"image_url": "..."`（扁平字串） |

完整前後範例程式碼請參見 [cheat-sheet.md](./references/cheat-sheet.md)。

考量測試基礎設施遷移（mocks、快照、斷言），請見 [test-migration.md](./references/test-migration.md)。

如需錯誤診斷及注意事項，請見 [troubleshooting.md](./references/troubleshooting.md)。

---

## 資料保留與狀態

- 所有 Responses 請求設定 `store: false`。
- 不依賴先前訊息 ID 或伺服器保存的上下文；狀態由用戶端管理並盡量減少元資料。

---

## 驗收標準

### 程式碼層級門檻（全部通過）

- [ ] 在遷移後檔案中，搜尋 `rg "chat\.completions\.create|ChatCompletion\.create|Completion\.create"`，應為零結果。
- [ ] 搜尋 `rg "AzureOpenAI\(|AsyncAzureOpenAI\("`，全部建構子改用帶 v1 端點的 `OpenAI`/`AsyncOpenAI`。
- [ ] 搜尋 `rg "models\.github\.ai|models\.inference\.ai\.azure"`，GitHub Models 相關程式路徑已移除。
- [ ] 搜尋 `rg "OpenAIChatCompletionClient"`，MAF 1.0.0+ 程式碼使用 `OpenAIChatClient`（搭配 Responses API）。1.0.0 以前請升級至 `agent-framework-openai>=1.0.0`。
- [ ] 所有 `ChatOpenAI(...)` 呼叫含 `use_responses_api=True`。
- [ ] 搜尋 `rg "choices\[0\]"`，所有存取回應皆使用 `resp.output_text` 或 Responses 輸出結構。
- [ ] 頂層不出現 `response_format`；所有結構化輸出使用 `text={"format": {...}}`。
- [ ] `requirements.txt` 或 `pyproject.toml` 中有 `openai>=1.108.1` 與 `azure-identity`；依賴重新安裝完畢。
- [ ] 每個 `responses.create` 呼叫設定 `store=False`。
- [ ] 用戶端建構時不包含 `api_version`；環境變數及基礎設施中移除 `AZURE_OPENAI_API_VERSION`。

### 測試基礎設施門檻（全部通過）

- [ ] 在 `tests/` 中搜尋 `rg "ChatCompletionChunk|AsyncCompletions\.create|chat\.completions"`，應為零結果。
- [ ] 在 `tests/` 中搜尋 `rg "_azure_ad_token_provider"`，斷言更新為檢查 `isinstance(client, AsyncOpenAI)` 或 `base_url`。
- [ ] 在 `tests/` 中搜尋 `rg "prompt_filter_results|content_filter_results"`，移除 Azure 特有過濾器 mocks。
- [ ] mock fixtures 使用 `kwargs.get("input")`，而非 `kwargs.get("messages")`。
- [ ] 快照與 golden 檔案更新為 Responses 串流格式（無 `choices[0]`、`function_call`、`logprobs` 等）。
- [ ] 所有測試更新後 `pytest` 通過且無失敗。

### 行為門檻（手動或透過測試套件驗證）

- [ ] <strong>基本完成測試</strong>：非串流 `responses.create` 返回非空字串 `output_text`。
- [ ] <strong>串流一致性</strong>：原程式有使用串流，則遷移後程式也串流並產生包含非空增量的 `response.output_text.delta` 事件。
- [ ] <strong>結構化輸出</strong>：使用 `text.format` 加上 `json_schema` 時，`json.loads(resp.output_text)` 可成功解析且符合架構。
- [ ] <strong>工具呼叫迴圈</strong>：若有使用工具，模型發出工具呼叫、應用執行呼叫，後續請求回傳最終 `output_text`（無無限迴圈）。
- [ ] <strong>非同步一致性</strong>：若使用 `AsyncAzureOpenAI`，其對應的 `AsyncOpenAI` 可配合 `await` 正常運作。
- [ ] <strong>錯誤率</strong>：相較遷移前基線，無新增 400/401/404 錯誤。

### 交付項目

- 摘要包含已編輯檔案、舊版調用數前後對比、下一步。
- 變更僅限工作樹編輯（無提交）。

---

## SDK 版本需求

| 套件 | 最低版本 |
|---------|----------------|
| `openai` | `>=1.108.1` |
| `azure-identity` | 最新版（用於 EntraID 認證） |

---

## 參考資源

- [速查表 — 所有程式碼片段](./references/cheat-sheet.md)
- [測試遷移 — mocks、快照、斷言](./references/test-migration.md)
- [故障排除 — 錯誤、風險表、注意事項](./references/troubleshooting.md)
- [detect_legacy.py — 自動掃描器](../../../../../.agents/skills/azure-openai-to-responses/scripts/detect_legacy.py)
- [Azure OpenAI 入門套件](https://aka.ms/openai/start)
- [Azure OpenAI Responses API 文件](https://learn.microsoft.com/en-us/azure/ai-foundry/openai/how-to/responses)
- [Azure OpenAI API 版本生命週期](https://learn.microsoft.com/en-us/azure/ai-foundry/openai/api-version-lifecycle?view=foundry-classic&tabs=python#api-evolution)
- [OpenAI Responses API 參考](https://platform.openai.com/docs/api-reference/responses)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責聲明**：
本文件使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。雖然我們力求準確，但請注意，自動翻譯可能包含錯誤或不準確之處。原始文件的母語版本應被視為權威來源。對於重要資訊，建議尋求專業人工翻譯。我們不對因使用本翻譯而引起的任何誤解或曲解承擔責任。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->