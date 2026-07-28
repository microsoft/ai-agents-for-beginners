# 疑難排解、風險表格與注意事項

## 疑難排解 400 錯誤

| 錯誤 | 修正方法 |
|-------|-----|
| `missing_required_parameter: tools[0].name` | 工具定義使用舊的 Chat Completions 嵌套格式 | 將 `{"type": "function", "function": {"name": ...}}` 攤平成 `{"type": "function", "name": ..., "parameters": ...}` — name、description、parameters 都放在頂層 |
| `unknown_parameter: input[N].tool_calls` | 多輪工具結果使用舊的 Chat Completions 格式 | 用 `response.output` 項目 + `{"type": "function_call_output", "call_id": ..., "output": ...}` 取代 `{"role": "assistant", "tool_calls": [...]}` + `{"role": "tool", ...}` |
| `invalid_function_parameters: 'required' is required` | 在 `strict: true` 工具中缺少 `required` 陣列 | 設定 `strict: true` 時，所有屬性必須列在 `required` 並且必須設定 `additionalProperties: false` |
| `invalid_function_parameters: 'additionalProperties' is required` | `strict: true` 工具缺少 `additionalProperties: false` | 在參數物件中加入 `"additionalProperties": false` |
| `invalid input[N].id: Expected an ID that begins with 'fc'` | 少量示例 function_call ID 使用了錯誤的前綴 | Function call ID 必須以 `fc_` 開頭（如 `fc_example1`），不可使用 `call_` |
| `missing_required_parameter: text.format.name` | 在格式字典中加入 `"name"` 鍵（例如 `"name": "Output"`） |
| `invalid_type: text.format` | 確保 `text.format` 是擁有 `type`、`name`、`strict`、`schema` 等鍵的字典，而非字串 |
| `invalid input content type` | 使用 `input_text` / `output_text` 類型內容代替 Chat 的 `text` |
| `invalid input content type` (影像) | 影像內容仍使用 `"type": "image_url"` | 改為 `"type": "input_image"` |
| 在 `image_url` 出現 `Expected object, got string` | `image_url` 仍是嵌套物件如 `{"url": "..."}` | 攤平成純字串，如 `"image_url": "https://..."` 或 `"image_url": "data:image/...;base64,..."` |
| `integer below minimum value`，針對 `max_output_tokens` | Azure OpenAI 最低值為 **16**。測試用建議使用 50 以上，生產環境建議 1000 以上。 |
| 串流時出現 `429 Too Many Requests` | 被速率限制。將串流包在 `try/except` 內，將錯誤 JSON 結果傳送到前端，並實作等待重試機制。 |
| 內容過濾錯誤時出現 `KeyError: 'innererror'` | Responses API 中內容過濾錯誤的結構已改變 | Chat Completions 使用 `error.body["innererror"]["content_filter_result"]`；Responses API 則使用 `error.body["content_filters"][0]["content_filter_results"]`（為複數且在陣列內）。請重新編寫所有 `innererror` 權杖存取。 |

---

## 遷移風險表

| 徵狀 | 可能的錯誤 | 修正方法 |
|---------|---------------|-----|
| `output_text` 為空或回應被截斷 | reasoning 模型的 `max_output_tokens` 設太低 | 將 `max_output_tokens` 設為 1000 或更高 — reasoning 會計入 Token 限制 |
| `400 invalid_type: text.format` | 使用了 `response_format` 字串而非 `text.format` 字典 | 使用 `text={"format": {"type": "json_schema", "name": "...", "strict": True, "schema": {...}}}` |
| `/openai/v1/responses` 出現 `404 Not Found` | `base_url` 設錯，少了 `/openai/v1/` 後綴 | 確保 `base_url=f"{endpoint}/openai/v1/"`（包含尾部斜線） |
| 切換到 `OpenAI()` 後收到 `401 Unauthorized` | `api_key` 未設定或令牌提供者未正確傳入 | 若為 EntraID，`api_key=token_provider` （可呼叫物件）。若為 API key，`api_key=os.environ["AZURE_OPENAI_API_KEY"]` |
| 模型回傳 `deployment not found` | `model` 參數與 Azure 部署名稱不符 | 使用 `model=os.environ["AZURE_OPENAI_DEPLOYMENT"]` — 這是部署名稱，不是模型名稱 |
| `json.loads(resp.output_text)` 引發 `JSONDecodeError` | 未強制執行 schema，或模型不支援嚴格 JSON | 確保 schema 中有 `"strict": True`，且確認模型支援結構化輸出 |
| 串流無 `delta` 事件 | 檢查了錯誤的事件類型 | 篩選條件請改為 `event.type == "response.output_text.delta"`，非 Chat 的 `chat.completion.chunk` |
| 遷移後影像輸入出現 `400` 錯誤 | 影像內容類型沒有更新 | 將 `"type": "image_url"` 改為 `"type": "input_image"`，並扁平化 `"image_url": {"url": "..."}` 改為 `"image_url": "..."` （純字串） |
| 工具呼叫無限迴圈 | 在後續輸入中缺少工具結果 | 執行工具後，將 `{"type": "function_call_output", "call_id": ..., "output": ...}` 項目附加到下一請求的 `input` 中 |
| GPT-5 或 o 系列出現 `temperature` 錯誤 | 指定了非 1 的明確 `temperature` 值 | 移除 `temperature` 或將其設為 `1`，適用於 GPT-5 及 o 系列模型（o1、o3-mini、o3、o4-mini） |
| o 系列模型出現 `top_p` 錯誤 | 不支援 `top_p` | 針對 o 系列模型時移除 `top_p` |
| `max_completion_tokens` 無法辨識 | 使用了 Azure 專屬參數 | 用 `max_output_tokens` 取代 `max_completion_tokens`。o 系列請設定高於 4096（reasoning token 會計入限制）。 |
| o 系列模型回傳空白或截斷結果 | `max_output_tokens` 設太低 | o 系列內部使用 reasoning tokens。將 `max_output_tokens` 設為 4096 或更高，而非 500–1000。 |
| `max_output_tokens` 收到 `400 integer_below_min_value` 錯誤 | 值低於 16 | Azure OpenAI 強制要求 `max_output_tokens >= 16`。測試用請用 50 以上，生產用 1000 以上。 |
| 串流中途出現 `429 Too Many Requests` | Azure OpenAI 速率限制 | 串流中斷時不會有錯誤提示。務必將 `async for event in await coroutine:` 包在 `try/except` 中，並向前端回傳 `{"error": str(e)}`。 |
| 使用 `AzureDeveloperCliCredential` 出現 `CredentialUnavailableError` | 租戶錯誤或未登入 | 明確傳入 `tenant_id=os.getenv("AZURE_TENANT_ID")`。本地執行 `azd auth login --tenant <租戶 ID>`。 |
| 使用 GitHub Models (`models.github.ai`) 出現 `404 Not Found` | GitHub Models 不支援 Responses API | 完全移除 GitHub Models 程式碼路徑。使用 Azure OpenAI、OpenAI，或相容且支持 Responses 的本地端點（例如 Ollama）。 |
| MAF 的 `OpenAIChatCompletionClient` 仍用 Chat Completions | 在 1.0.0+ 版本中仍使用舊 MAF 用戶端 | MAF 1.0.0+ 預設使用 Responses API 的 `OpenAIChatClient`。將 `OpenAIChatCompletionClient` 換成 `OpenAIChatClient`。若版本低於 1.0.0，請升級至 `agent-framework-openai>=1.0.0`。 |
| LangChain 代理在工具呼叫時回傳空或失敗 | `ChatOpenAI` 未使用 Responses API | 在 `ChatOpenAI(...)` 加上 `use_responses_api=True`。同時將回應訊息的 `.content` 改為 `.text`。 |
| 內容過濾錯誤處理中出現 `KeyError: 'innererror'` | Responses API 中錯誤內容結構變更 | 將 `error.body["innererror"]["content_filter_result"]["jailbreak"]` 改寫為 `error.body["content_filters"][0]["content_filter_results"]["jailbreak"]`。`innererror` 已消失；內容過濾細節改放在頂層 `content_filters` 陣列中，每個項目含有複數的 `content_filter_results`。 |
| 原始 HTTP 呼叫 `/openai/deployments/.../chat/completions` 回傳 404 | 使用了舊的 Chat Completions REST 端點 | 將網址改為 `/openai/v1/responses`。變更請求體中 `messages` → `input`，加入 `max_output_tokens` 和 `store: false`，移除 `api-version` 查詢參數。變更回應解析：`choices[0].message.content` → `output[0].content[0].text`（注意：`output_text` 是 SDK 的方便屬性，非原始 REST JSON 部分）。 |

---

## 注意事項

1. 如果以往用 Chat Completions 管理對話狀態，現在用 Responses 請明確自行管理狀態。
2. 建議使用 `max_output_tokens`，不要使用舊有的 `max_tokens`。
3. 遷移到 `gpt-5` 時，確保未指定 `temperature` 或明確設定為 `1`。
4. 把 Chat 的 `content[].type: "text"` 替換為 Responses 的 `content[].type: "input_text"` 用於使用者/系統輸入。
5. `text.format` 請提供正確字典格式（例：`{"type": "json_schema", "name": "Output", "schema": ..., "strict": True}`），不可用純字串。
6. Responses 不支援 `seed` 參數，請從請求中移除。
7. **Reasoning**：僅當原程式碼已使用 `reasoning` 時才包含，不要新加到未使用 reasoning 之 API 呼叫 — 許多非 reasoning 模型不支援此參數。
8. **`max_output_tokens` 設定大小**：針對 reasoning 模型（GPT-5-mini、GPT-5、o 系列），請設為 4096 或更高 — 不要使用 50–1000。模型內部先用 reasoning tokens 進行推理，限制太低會導致回應截斷或空白。
9. **o 系列的 `max_completion_tokens`**：若程式碼原使用 `max_completion_tokens`（Azure 專屬 o 系列參數），請改用 `max_output_tokens`。Responses API 不接受 `max_completion_tokens`。
10. **o 系列的 `reasoning_effort`**：若原程式使用 `reasoning_effort`（low/medium/high），請改為 Responses API 呼叫中 `reasoning={"effort": "<value>"}`。
11. **o 系列串流延遲**：o 系列模型在產生輸出前會先進行內部推理。串流時首個 `response.output_text.delta` 事件會延遲。這是正常現象，表示模型在推理，非故障。
9. **`_azure_ad_token_provider` 不見了**：`AsyncOpenAI` / `OpenAI` 不再有 `_azure_ad_token_provider` 屬性。測試或程式碼若存取此屬性會拋 `AttributeError`。token 提供者已改用 `api_key` 傳入，且無法從用戶端物件檢視。
10. **快照檔 / golden files**：若測試套件用快照測試，所有包含 Chat Completions 串流格式（`choices[0]`、`content_filter_results`、`function_call` 等）的快照檔必須更新為新的 Responses 形態。這很容易遺漏，且會導致快照斷言失敗。
11. **Mock 打補丁路徑**：打補丁目標改從 `openai.resources.chat.AsyncCompletions.create` → `openai.resources.responses.AsyncResponses.create`（同步為 `Responses.create`）。舊路徑不會產生錯誤，但補丁不會生效，測試會打到真實 API 或失敗。
12. **使用 `input` 不是 `messages`**：Mock 函式必須讀取 `kwargs.get("input")`，非 `kwargs.get("messages")`。Responses API 用 `input` 表示對話歷史。
13. <strong>環境變數命名</strong>：Azure Identity SDK 使用 `AZURE_CLIENT_ID`（非 `AZURE_OPENAI_CLIENT_ID`）對應 `ManagedIdentityCredential(client_id=...)`。請在測試、`.env` 文件、應用設定和 Bicep/基礎架構中重新命名。
14. **`max_output_tokens` 最低為 16**：Azure OpenAI 拒絕低於 16 的值，錯誤為 `400 integer_below_min_value`。測試用請用 50，生產用 1000 以上。舊的 `max_tokens` 沒有此限制。
15. **`AzureDeveloperCliCredential` 的 `tenant_id`**：當 Azure OpenAI 資源在不同租戶時，必須明確傳入 `tenant_id` — 如 `AzureDeveloperCliCredential(tenant_id=os.getenv("AZURE_TENANT_ID"))`。省略則憑證會無聲地用錯租戶並回 `401`。
16. <strong>速率限制在串流中呈現方式不同</strong>：Chat Completions 中，429 通常阻止串流啟動。Responses API 串流中，429 可在 <strong>串流中途</strong> 發生 — 非同步迭代器將拋出例外。請務必將串流迴圈包在 `try/except`，並回傳錯誤 JSON 行，讓前端能優雅處理。

17. <strong>網頁應用程序必須進行串流錯誤處理</strong>：模式 `try: async for event in await coroutine: ... except Exception as e: yield json.dumps({"error": str(e)})` 是關鍵。若缺少此處理，SSE/JSONL 串流會在任何伺服器端錯誤時悄無聲息地停止，前端則會當機。
18. <strong>工具定義必須使用扁平格式</strong>：Responses API 預期 `{"type": "function", "name": ..., "parameters": ...}` — 而非 Chat Completions 的巢狀格式 `{"type": "function", "function": {"name": ..., "parameters": ...}}`。這是函數呼叫程式碼轉換最常見的錯誤。
19. **`pydantic_function_tool()` 不相容**：`openai.pydantic_function_tool()` 助手仍生成舊的巢狀格式。請勿和 `responses.create()` 一起使用。請手動定義工具模式或將輸出扁平化。
20. **工具結果使用 `function_call_output`，不是 `role: tool`**：執行工具後，請附加 `{"type": "function_call_output", "call_id": ..., "output": ...}` — 而非 `{"role": "tool", "tool_call_id": ..., "content": ...}`。而助理的工具請求，使用 `messages.extend(response.output)` — 不用手動加 `{"role": "assistant", "tool_calls": [...]}` 字典。
21. **`strict: true` 需要 `required` + `additionalProperties: false`**：在工具使用 `strict: true` 時，每個屬性都必須列於 `required` 陣列中，且 `additionalProperties` 必須是 `false`。缺一會導致 400 錯誤。
22. **函數呼叫 ID 有特定前綴**：於 `input` 中提供 few-shot `function_call` 項目時，`id` 欄位必須以 `fc_` 開頭，`call_id` 欄位必須以 `call_` 開頭（例如 `"id": "fc_example1", "call_id": "call_example1"`）。舊 Chat Completions 的 `call_` 作為 `id` 前綴已被拒絕。
23. **GitHub Models 不支援 Responses API**：若應用包含 GitHub Models 路徑（`base_url` 指向 `models.github.ai` 或 `models.inference.ai.azure.com`），請完全移除。沒有轉移路徑——請切換至 Azure OpenAI、OpenAI 或相容之本地端點。
24. <strong>內容過濾器錯誤的回應結構已變更</strong>：Chat Completions 錯誤使用 `error.body["innererror"]["content_filter_result"]`（單數）。Responses API 錯誤改為使用 `error.body["content_filters"][0]["content_filter_results"]`（複數，於陣列中）。`innererror` 鍵已不存在。直接存取 `innererror` 的程式碼執行時會觸發 `KeyError` — 這在轉換時容易忽略，因為僅在內容過濾器實際觸發時才會顯現。轉換期間必須 grep `innererror`。
25. **直接呼叫原生 HTTP 需改寫 URL + 請求體**：若應用直接呼叫 Azure OpenAI REST（經 `requests`、`httpx`、`aiohttp`）且使用 `/openai/deployments/{name}/chat/completions?api-version=...`，必須切換至 `/openai/v1/responses`。請求體使用 `input` 替代 `messages`，且必需 `max_output_tokens` 與 `store`，`api-version` 查詢參數也會被移除。回應體文字位於 `output[0].content[0].text` — <strong>不是</strong> `output_text`，後者是 SDK 的便利屬性，原生 REST JSON 中無此欄位。

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責聲明**：
本文件由 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 翻譯而成。雖然我們致力於確保準確性，但請注意，機器自動翻譯可能包含錯誤或不準確之處。原始文件的母語版本應被視為權威來源。對於重要資訊，建議進行專業人工翻譯。我們不對因使用本翻譯而產生的任何誤解或誤釋承擔責任。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->