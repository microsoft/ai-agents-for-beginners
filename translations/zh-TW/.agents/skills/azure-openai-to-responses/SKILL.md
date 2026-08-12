---
name: azure-openai-to-responses
license: MIT
---
# 將 Python 應用程式從 Azure OpenAI Chat Completions 遷移到 Responses API

> **權威指南 — 請嚴格遵循**
>
> 本技能將使用 Azure OpenAI Chat Completions 的 Python 代碼庫
> 遷移到統一的 Responses API。請精確遵循這些指令。
> 不得自行即興映射參數或創建 API 形態。

---

## 觸發條件

當用戶想要：
- 將 Python 應用從 Azure OpenAI Chat Completions 遷移到 Responses API
- 升級 Python OpenAI SDK 使用方式，改用針對 Azure OpenAI 的最新 API 形態
- 為需要 Azure Responses 的 GPT-5 或更新模型準備 Python 代碼
- 從 `AzureOpenAI` / `AsyncAzureOpenAI` 切換到使用標準的 `OpenAI` / `AsyncOpenAI` 客戶端，搭配 v1 端點
- 修正與 `AzureOpenAI` 建構子或 `api_version` 相關的棄用警告

---

## ⚠️ 模型相容性 — 請先檢查

> **遷移前，請確認您的 Azure OpenAI 部署支援 Responses API。**

### 1. 快速測試您的部署（最快速）

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

> <strong>注意</strong>：Azure OpenAI 上 `max_output_tokens` 的<strong>最小值為 16</strong>。低於 16 的值會回傳 400 錯誤。用 50 以上進行快速測試。

如果回傳 404，表示該部署的模型尚不支援 Responses，請參考下方參考資料或用支援的模型重新部署。

### 2. 查詢區域內可用模型（建議）

執行內建模型相容性工具，查看您所在區域有哪些模型支援 Responses API：

```bash
python migrate.py models --subscription YOUR_SUB_ID --location YOUR_REGION
```

該指令會向 Azure ARM 實時查詢並顯示相容性矩陣 — 包含支援 Responses、結構化輸出、工具等的模型。可用 `--filter gpt-5.1,gpt-5.2` 篩選結果，或用 `--json` 做腳本化處理。

### 3. 完整模型支援參考

- <strong>即時查詢</strong>：`python migrate.py models`（參見上方 — 區域特定，且始終保持最新）
- <strong>檢視供應</strong>：[模型摘要表及區域可用性](https://learn.microsoft.com/en-us/azure/foundry/foundry-models/concepts/models-sold-directly-by-azure?tabs=global-standard-aoai%2Cglobal-standard&pivots=azure-openai#model-summary-table-and-region-availability)
- <strong>快速入門與指引</strong>：**https://aka.ms/openai/start**

### ⚠️ 舊版模型限制

> <strong>警告</strong>：早期模型（`gpt-4.1` 之前的版本）可能無法完整支援所有 Responses API 功能。
>
> 已知的舊版模型限制：
> - **`reasoning` 參數**：許多非推理模型不支援。如原始程式碼未使用，勿遷移 `reasoning`。
> - **`seed` 參數**：Responses API 完全不支援，請從所有請求中移除。
> - **透過 `text.format` 使用結構化輸出**：舊版模型可能無法可靠執行 `strict: true` 的 JSON schema 驗證。
> - <strong>工具協調</strong>：GPT-5+ 將工具呼叫整合於推理過程中，舊模型的 Responses 支援仍有效，但缺乏深度整合。
> - <strong>溫度限制</strong>：遷移到 `gpt-5` 時，溫度參數必須省略或設定為 `1`。舊模型沒有此限制。

### O 系列推理模型（o1、o3-mini、o3、o4-mini）

O 系列模型有獨特的參數限制。當遷移針對 O 系列模型的應用時：

- **`temperature`**：必須是 `1`（或省略）。O 系列模型不接受其他值。
- **`max_completion_tokens` → `max_output_tokens`**：使用 Azure 特定的 `max_completion_tokens` 的應用需改用 `max_output_tokens`。設定較大值（4096 以上），因為推理令牌會計入限制。
- **`reasoning_effort`**：若應用使用 `reasoning_effort`（low/medium/high），請保留 — Responses API 支援此參數於 O 系列模型。
- <strong>串流行為</strong>：O 系列模型可能先緩衝輸出，待推理完成後才發出文字差異事件。串流依然可用，但第一個 `response.output_text.delta` 可能比 GPT 模型出現得晚。
- **`top_p`**：O 系列不支援，若出現請移除。
- <strong>工具使用</strong>：O 系列模型透過 Responses API 支援工具，與 GPT 類似，但工具呼叫協調品質因模型而異。

**行動 — 前瞻性模型建議**：掃描階段檢查應用目標模型（部署名稱、環境變數、配置）。若模型早於 `gpt-4.1`（非 gpt-4.1+），請主動告知用戶：
- 遷移能在其當前模型上順利運作基礎文字、聊天、串流及工具功能。
- 較新模型（`gpt-5.1`、`gpt-5.2`）提供更完善的工具協調、結構化輸出強制、推理與跨區域可用性。
- 用戶應考慮準備好時升級部署 — 但此步驟不會阻擋遷移。

不應依模型版本阻擋或拒絕執行遷移，此建議僅供參考資訊。

### GitHub Models 不支援 Responses API

> **GitHub Models (`models.github.ai`, `models.inference.ai.azure.com`) 不支援 Responses API。**

若代碼庫含有 GitHub Models 程式碼路徑（尋找 `base_url` 指向 `models.github.ai` 或 `models.inference.ai.azure.com`），遷移時<strong>必須完全移除</strong>。Responses API 需 Azure OpenAI、OpenAI 或相容本機端點（如支持 Responses 的 Ollama）。

掃描階段行動：
- 標記所有 GitHub Models 程式碼路徑以便移除。

---

## 框架遷移

許多應用使用 OpenAI 之上高階框架。遷移這些時，框架的 API 也會改變 — 不僅是底層的 OpenAI 調用。

### Microsoft Agent Framework (MAF)

**先檢查您的 MAF 版本** — 遷移作業依賴您使用的是 MAF 1.0.0+ 還是 1.0.0 以前的 beta/rc 版。

#### MAF 1.0.0+ (agent-framework-openai >= 1.0.0)

`OpenAIChatClient` **已使用 Responses API** — 無需遷移。若代碼使用舊版 `OpenAIChatCompletionClient`（呼叫 `chat.completions.create`），請替換為 `OpenAIChatClient`。

| 遷移前 | 遷移後 |
|--------|-------|
| `from agent_framework.openai import OpenAIChatCompletionClient` | `from agent_framework.openai import OpenAIChatClient` |
| `OpenAIChatCompletionClient(...)` | `OpenAIChatClient(...)` |

確認版本：`python -c "import agent_framework_openai; print(agent_framework_openai.__version__)"`

#### MAF 1.0.0 以前版本（beta/rc 發行版）

1.0.0 以前的 MAF 中，`OpenAIChatClient` 仍使用 Chat Completions。請升級至 `agent-framework-openai>=1.0.0`，改用預設的 Responses API。

無需其他變更 — `Agent` 與工具 API 保持不變。

### LangChain (`langchain-openai`)

在 `ChatOpenAI()` 加上 `use_responses_api=True`。同時將回應存取由 `.content` 改成 `.text`。

| 遷移前 | 遷移後 |
|--------|-------|
| `ChatOpenAI(model=..., base_url=..., api_key=...)` | `ChatOpenAI(model=..., base_url=..., api_key=..., use_responses_api=True)` |
| `result['messages'][-1].content` | `result['messages'][-1].text` |

完整遷移前後程式碼範例，請參閱 [cheat-sheet.md](./references/cheat-sheet.md)。

---

## 前端遷移指引

> **Responses API 是伺服器端功能。** 請遷移 Python 後端；前端的 HTTP 合約應保持不變，除非您的後端很薄透 — 此時可考慮直接採用 Responses 請求格式以消除轉換層。若前端直接用客戶端金鑰調用 OpenAI，請先移至後端。

### `@microsoft/ai-chat-protocol` 棄用

`@microsoft/ai-chat-protocol` npm 套件已棄用，應改用 [`ndjson-readablestream`](https://www.npmjs.com/package/ndjson-readablestream)。前端若遇到：

1. 替換 CDN script 標籤：
   ```html
   <!-- Before -->
   <script src="https://cdn.jsdelivr.net/npm/@microsoft/ai-chat-protocol@.../dist/iife/index.js"></script>
   <!-- After -->
   <script src="https://cdn.jsdelivr.net/npm/ndjson-readablestream@1.0.7/dist/ndjson-readablestream.umd.js"></script>
   ```
2. 移除 `AIChatProtocolClient` 實例化（`new ChatProtocol.AIChatProtocolClient("/chat")`）。
3. 將 `client.getStreamedCompletion(messages)` 替換成直接對後端串流端點的 `fetch()` 呼叫。
4. 將 `for await (const response of result)` 替換成 `for await (const chunk of readNDJSONStream(response.body))`。
5. 將屬性存取由 `response.delta.content` / `response.error` 改成 `chunk.delta.content` / `chunk.error`。

---

## 目標

- 列出所有使用 Chat Completions 或舊版 Completions 針對 Azure OpenAI 的 Python 呼叫處。
- 提出適用於 Python 代碼庫的遷移計畫與執行順序。
- 進行安全且最小的修改以切換至 Responses API。
- 更新呼叫端來使用 Responses 輸出格式；不保留向後相容包裝。
- 執行測試與程式檢查，修正遷移後產生的輕微錯誤。
- 準備小而可檢閱的變更集並提供最終包含差異的摘要（不提交代碼）。

---

## 保護措施

- 僅修改 git 工作區內的檔案。禁止寫出工作目錄之外的位置。
- 不保留向後相容的 shim；將代碼改為新 API 形態。
- 不留過渡註解或備份檔案。
- 若先前使用串流，保留串流語義；否則改用非串流。
- 若處於審核模式，非經批准前不執行命令或網絡呼叫。
- 不執行 `git add` / `git commit` / `git push`；僅產生工作樹修改。

---

## 步驟 0：Azure OpenAI 客戶端遷移（前置作業）

若代碼庫使用 `AzureOpenAI` 或 `AsyncAzureOpenAI` 建構子，請先遷移到標準 `OpenAI` / `AsyncOpenAI` 建構子。Azure 專用建構子在 `openai>=1.108.1` 已棄用。

### 為什麼改用 v1 API 路徑？

新的 `/openai/v1` 端點使用標準的 `OpenAI()` 客戶端，非 `AzureOpenAI()`，無需 `api_version` 參數，且在 OpenAI 與 Azure OpenAI 上行為一致。相同的客戶端代碼具備未來兼容性 — 無需版本管理。

### 主要改變

| 遷移前 | 遷移後 |
|--------|-------|
| `AzureOpenAI` | `OpenAI` |
| `AsyncAzureOpenAI` | `AsyncOpenAI` |
| `azure_endpoint` | `base_url` |
| `azure_ad_token_provider` | `api_key` |
| `api_version=...` | 完全移除 |

### 清理事項清單

- 移除客戶端建構時的 `api_version` 引數。
- 從 `.env`、應用設定、Bicep/基礎架構檔案中移除 `AZURE_OPENAI_VERSION` / `AZURE_OPENAI_API_VERSION` 環境變數。
- 將 `.env`、應用設定、Bicep/基礎架構及測試配置中的 `AZURE_OPENAI_CLIENT_ID` 改名為 `AZURE_CLIENT_ID`（符合標準 Azure Identity SDK 慣例）。
- 確保 `requirements.txt` 或 `pyproject.toml` 中的 `openai` 版本為 `>=1.108.1`。

### 環境變數遷移

| 舊環境變數 | 措施 | 備註 |
|-------------|--------|-------|
| `AZURE_OPENAI_VERSION` | <strong>移除</strong> | v1 端點不需 `api_version` |
| `AZURE_OPENAI_API_VERSION` | <strong>移除</strong> | 同上 |
| `AZURE_OPENAI_CLIENT_ID` | <strong>改名</strong> → `AZURE_CLIENT_ID` | 用於 `ManagedIdentityCredential(client_id=...)`，符合 Azure Identity SDK 慣例 |
| `AZURE_OPENAI_ENDPOINT` | <strong>保留</strong> | 用於建構 `base_url` |
| `AZURE_OPENAI_CHAT_DEPLOYMENT` | <strong>保留</strong> | 用於 `responses.create` 的 `model` 參數 |
| `AZURE_OPENAI_API_KEY` | <strong>保留</strong> | 用於基於金鑰的認證 `api_key` |

更多客戶端設定代碼範例（同步、非同步、EntraID、API 金鑰、多租戶），請參閱 [cheat-sheet.md](./references/cheat-sheet.md)。

---

## 步驟 1：偵測舊版呼叫處

執行 [detect_legacy.py](../../../../../.agents/skills/azure-openai-to-responses/scripts/detect_legacy.py) 腳本以找到所有需遷移的呼叫處：

```bash
python skills/azure-openai-to-responses/scripts/detect_legacy.py .
```

或手動執行以下關鍵字搜尋 — 每個符合項目均為遷移對象：

```bash
# 傳統 API 調用（必須重寫）
rg "chat\.completions\.create"
rg "ChatCompletion\.create"
rg "Completion\.create"

# 已棄用的 Azure 用戶端建構函式（必須替換）
rg "AzureOpenAI\("
rg "AsyncAzureOpenAI\("

# 回應結構存取模式（必須更新）
rg "choices\[0\]\.message\.content"
rg "choices\[0\]\.delta\.content"
rg "choices\[0\]\.message\.function_call"
rg "choices\[0\]\.message\.tool_calls"

# 舊的巢狀格式工具定義（必須扁平化）
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

# GitHub Models 端點（必須移除 — Responses API 不支持）
rg "models\.github\.ai|models\.inference\.ai\.azure"

# 框架層級傳統模式（必須更新）
rg "OpenAIChatCompletionClient"  # MAF 1.0.0+：替換為 OpenAIChatClient
rg "ChatOpenAI\(" | grep -v "use_responses_api"  # LangChain：需要 use_responses_api=True

# 測試基礎設施（必須更新）
rg "ChatCompletionChunk|AsyncCompletions\.create" tests/
rg "_azure_ad_token_provider" tests/
rg "prompt_filter_results|content_filter_results" tests/
rg "choices\[0\]" tests/

# 內容過濾錯誤主體存取（必須更新 — 結構改變）
rg 'innererror.*content_filter_result|error\.body\["innererror"\]'
rg "content_filter_result\[" # 舊的單數形式 — 現在是 content_filters 陣列中的 content_filter_results（複數）

# 對 Chat Completions 端點的原始 HTTP 調用（必須更新 URL）
rg "/openai/deployments/.*/chat/completions"
rg "api-version="
```

### 偵測與重寫原則

- **Chat Completions 用戶端**：`client.chat.completions.create` → `client.responses.create(...)`。

- **Azure 用戶端建構子**：`AzureOpenAI(...)` → `OpenAI(base_url=..., api_key=...)`。
- <strong>工具</strong>：將函式呼叫工具定義從巢狀格式（`{"type": "function", "function": {"name": ...}}`）轉換為平鋪的 Responses 格式（`{"type": "function", "name": ...}`）；使用 `tool_choice`；回傳工具結果為 `{"type": "function_call_output", "call_id": ..., "output": ...}` 項目（而非 `{"role": "tool", ...}`）。
- <strong>工具回合</strong>：當模型回傳函式呼叫時，將 `response.output` 項目附加到對話中（而非手動的 `{"role": "assistant", "tool_calls": [...]}` dict），接著為每個結果附加 `function_call_output` 項目。
- <strong>少量示範工具範例</strong>：如果對話中包含硬編碼的工具呼叫範例，轉換它們為 `{"type": "function_call", "id": "fc_...", "call_id": "fc_...", ...}` + `{"type": "function_call_output", ...}` 項目。ID 必須以 `fc_` 開頭。
- **`pydantic_function_tool()`<strong>：此幫助函式仍產生舊的巢狀格式，且</strong>不相容**於 `responses.create()`。請改用手動工具定義或平鋪的包裝器替代。
- <strong>多輪對話</strong>：在應用程式維護對話歷史；透過 `input` 項目傳遞先前回合。
- <strong>格式</strong>：將 Chat 的頂層 `response_format` 替換成 Responses 的 `text.format`。標準格式為：`text={"format": {"type": "json_schema", "name": "Output", "strict": True, "schema": {...}}}`。
- <strong>內容項目</strong>：將 Chat `content[].type: "text"` 替換為 Responses `content[].type: "input_text"`（適用於用戶/系統回合）。
- <strong>圖片內容項目</strong>：將 Chat `content[].type: "image_url"` 替換為 Responses `content[].type: "input_image"`。`image_url` 欄位由巢狀物件 `{"url": "..."}` 改為平面字串。請參考備忘單了解前後範例。
- <strong>推理內容</strong>：**僅在原始程式碼存在 `reasoning` 時才遷移**。
- <strong>內容過濾錯誤處理</strong>：錯誤主體結構變動。Chat Completions 使用 `error.body["innererror"]["content_filter_result"]`（單數）；Responses API 使用 `error.body["content_filters"][0]["content_filter_results"]`（複數且在陣列中）。存取 `innererror` 的程式碼會引發 `KeyError`，需改寫為新路徑。
- **原始 HTTP 呼叫**：如果應用程式直接呼叫 Azure OpenAI REST API（透過 `requests`, `httpx` 等使用 `/openai/deployments/{name}/chat/completions?api-version=...`），請改寫成 `/openai/v1/responses`。請求主體變更：`messages` → `input`，新增 `max_output_tokens` 及 `store: false`，移除 `api-version` 查詢參數。回應主體變更：`choices[0].message.content` → `output[0].content[0].text`（注意：`output_text` 為 SDK 方便屬性，原始 REST JSON 不存在）。

---

## 第 2 步：套用遷移

### 遷移注意事項（Chat Completions → Responses）

- <strong>為什麼遷移</strong>：Responses 是文字、工具與串流的統一 API；Chat Completions 為舊版。GPT-5 後，Responses 為最佳效能所需。
- **HTTP**：Azure 端點從 `/openai/deployments/{name}/chat/completions` 換到 `/openai/v1/responses`。
- <strong>欄位</strong>：`messages` → `input`，`max_tokens` → `max_output_tokens`。`temperature` 保持不變。
- <strong>格式</strong>：`response_format` → 用正確物件的 `text.format`。
- <strong>內容項目</strong>：系統/用戶回合將 Chat 的 `content[].type: "text"` 替換為 Responses 的 `content[].type: "input_text"`。
- <strong>圖片內容項目</strong>：將 Chat 的 `content[].type: "image_url"` 替換為 Responses 的 `content[].type: "input_image"`。將 `image_url` 欄位從 `{"image_url": {"url": "..."}}` 攤平成 `{"image_url": "..."}`（純字串，可能是 HTTPS URL 或 `data:image/...;base64,...` 資料 URI）。

### 參數映射參考

| Chat Completions | Responses API |
|-----------------|---------------|
| `prompt` | `input` |
| `messages` | `input`（陣列） |
| `max_tokens` | `max_output_tokens` |
| `response_format` | `text.format`（物件） |
| `temperature` | `temperature`（不變） |
| `stop` | `stop`（不變） |
| `frequency_penalty` | `frequency_penalty`（不變） |
| `presence_penalty` | `presence_penalty`（不變） |
| `tools` / 函式呼叫 | `tools`（不變） |
| `seed` | <strong>移除</strong>（不支援） |
| `store` | `store`（設為 `false`） |
| `content[].type: "text"` | `content[].type: "input_text"` |
| `content[].type: "image_url"` | `content[].type: "input_image"` |
| `"image_url": {"url": "..."}` | `"image_url": "..."`（平面字串） |

詳細前後程式碼範例，請見 [cheat-sheet.md](./references/cheat-sheet.md)。

測試基礎建設遷移（模擬、快照、斷言），請參考 [test-migration.md](./references/test-migration.md)。

錯誤排除與注意事項，請參考 [troubleshooting.md](./references/troubleshooting.md)。

---

## 資料留存與狀態

- 在所有 Responses 請求上設定 `store: false`。
- 不依賴之前的訊息 ID 或伺服器端儲存的上下文；狀態由客戶端管理，並最小化元資料。

---

## 驗收標準

### 程式碼層級門檻（全部需通過）

- [ ] 遷移後檔案中無法用 `rg "chat\.completions\.create|ChatCompletion\.create|Completion\.create"` 搜尋到任何匹配。
- [ ] 無 `rg "AzureOpenAI\(|AsyncAzureOpenAI\("` 匹配 — 所有建構子皆使用帶 v1 端點的 `OpenAI`/`AsyncOpenAI`。
- [ ] 無 `rg "models\.github\.ai|models\.inference\.ai\.azure"` 匹配 — GitHub Models 相關程式碼路徑已移除。
- [ ] 無 `rg "OpenAIChatCompletionClient"` 匹配 — MAF 1.0.0+ 程式碼使用 `OpenAIChatClient`（使用 Responses API）；1.0.0 以前版本需升級到 `agent-framework-openai>=1.0.0`。
- [ ] 所有 `ChatOpenAI(...)` 呼叫均包含 `use_responses_api=True`。
- [ ] 無 `rg "choices\[0\]"` 匹配 — 所有回應存取使用 `resp.output_text` 或 Responses 輸出結構。
- [ ] 頂層無 `response_format`；所有結構化輸出使用 `text={"format": {...}}`。
- [ ] `requirements.txt` 或 `pyproject.toml` 中含 `openai>=1.108.1` 及 `azure-identity`；依賴重裝。
- [ ] 每次呼叫 `responses.create` 都設定 `store=False`。
- [ ] 用戶端建構無 `api_version`；環境設定檔及基礎結構中刪除 `AZURE_OPENAI_API_VERSION`。

### 測試基礎建設門檻（全部需通過）

- [ ] 測試目錄中無 `rg "ChatCompletionChunk|AsyncCompletions\.create|chat\.completions"` 匹配。
- [ ] 測試目錄中無 `rg "_azure_ad_token_provider"` 匹配 — 斷言改為檢查 `isinstance(client, AsyncOpenAI)` 或 `base_url`。
- [ ] 測試目錄中無 `rg "prompt_filter_results|content_filter_results"` 匹配 — 移除 Azure 特定過濾模擬。
- [ ] 模擬裝置使用 `kwargs.get("input")` 而非 `kwargs.get("messages")`。
- [ ] 快照 / golden 檔案已更新為 Responses 串流格式（無 `choices[0]`、`function_call`、`logprobs` 等）。
- [ ] 完成所有測試更新後，`pytest` 輸出零失敗。

### 行為門檻（手動或透過測試框架驗證）

- [ ] <strong>基本完成</strong>：非串流的 `responses.create` 回傳非空 `output_text`。
- [ ] <strong>串流一致性</strong>：若原程式使用串流，遷移後仍串流並產生含非空 delta 的 `response.output_text.delta` 事件。
- [ ] <strong>結構化輸出</strong>：若使用帶 `json_schema` 的 `text.format`，`json.loads(resp.output_text)` 成功且符合 schema。
- [ ] <strong>工具呼叫迴圈</strong>：若使用工具，模型發出工具呼叫、應用執行，隨後請求回傳最終 `output_text`（無無限迴圈）。
- [ ] <strong>非同步一致性</strong>：若原使用 `AsyncAzureOpenAI`，遷移後 `AsyncOpenAI` 等效且可用 `await`。
- [ ] <strong>錯誤率</strong>：與遷移前基線比較，無新增 400/401/404 錯誤。

### 交付項目

- 摘要列出編輯的檔案、舊版呼叫點的前後數量及後續步驟。
- 變更只限工作目錄編輯（不含提交）。

---

## SDK 版本需求

| 套件 | 最低版本 |
|---------|----------------|
| `openai` | `>=1.108.1` |
| `azure-identity` | 最新版（用於 EntraID 認證） |

---

## 參考資料

- [備忘單 — 全部程式碼片段](./references/cheat-sheet.md)
- [測試遷移 — 模擬、快照、斷言](./references/test-migration.md)
- [疑難排解 — 錯誤、風險表、注意事項](./references/troubleshooting.md)
- [detect_legacy.py — 自動掃描程式](../../../../../.agents/skills/azure-openai-to-responses/scripts/detect_legacy.py)
- [Azure OpenAI 入門套件](https://aka.ms/openai/start)
- [Azure OpenAI Responses API 文件](https://learn.microsoft.com/en-us/azure/ai-foundry/openai/how-to/responses)
- [Azure OpenAI API 版本生命週期](https://learn.microsoft.com/en-us/azure/ai-foundry/openai/api-version-lifecycle?view=foundry-classic&tabs=python#api-evolution)
- [OpenAI Responses API 參考](https://platform.openai.com/docs/api-reference/responses)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責聲明**：
此文件已使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。雖然我們努力追求準確性，但請注意自動翻譯可能包含錯誤或不準確之處。原始文件的母語版本應視為權威來源。對於關鍵資訊，建議採用專業人工翻譯。我們不對因使用此翻譯所產生的任何誤解或誤譯承擔責任。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->