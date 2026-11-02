# 疑難排解、風險表與陷阱

## 400 錯誤疑難排解

| 錯誤 | 解決方法 |
|-------|-----|
| `missing_required_parameter: tools[0].name` | 工具定義使用舊版聊天補全嵌套格式 | 將 `{"type": "function", "function": {"name": ...}}` 攤平為 `{"type": "function", "name": ..., "parameters": ...}` — name、description、parameters 應放在頂層 |
| `unknown_parameter: input[N].tool_calls` | 多回合工具結果用舊版聊天補全格式 | 將 `{"role": "assistant", "tool_calls": [...]}` + `{"role": "tool", ...}` 替換為 `response.output` 項目 + `{"type": "function_call_output", "call_id": ..., "output": ...}` |
| `invalid_function_parameters: 'required' is required` | `strict: true` 工具缺少 `required` 陣列 | 設定 `strict: true` 時，所有屬性必須列在 `required`，並設定 `additionalProperties: false` |
| `invalid_function_parameters: 'additionalProperties' is required` | `strict: true` 工具缺少 `additionalProperties: false` | 在參數物件中新增 `"additionalProperties": false` |
| `invalid input[N].id: Expected an ID that begins with 'fc'` | few-shot function_call ID 前綴錯誤 | function call ID 必須以 `fc_` 開頭 (例如 `fc_example1`)，而非 `call_` |
| `missing_required_parameter: text.format.name` | 在 format 字典新增 `"name"` 鍵 (例如 `"name": "Output"`) |
| `invalid_type: text.format` | 確保 `text.format` 是含有 `type`、`name`、`strict`、`schema` 鍵的字典 — 不可是字串 |
| `invalid input content type` | 使用 `input_text`/`output_text` 類型取代聊天的 `text` |
| `invalid input content type` (image) | 圖像類型仍為 `"type": "image_url"` | 改為 `"type": "input_image"` |
| `Expected object, got string` 在 `image_url` | `image_url` 仍為嵌套物件 `{"url": "..."}` | 攤平成純字串：`"image_url": "https://..."` 或 `"image_url": "data:image/...;base64,..."` |
| `integer below minimum value` 針對 `max_output_tokens` | Azure OpenAI 最小值為 **16**。測試時用 50+，正式環境用 1000+ 。 |
| 串流中出現 `429 Too Many Requests` | 請求率限制。將串流包在 `try/except` 中，向前端輸出錯誤 JSON，實施退避重試。 |
| Content filter 錯誤顯示 `KeyError: 'innererror'` | Responses API 中內容過濾器錯誤體結構變更 | 聊天補全使用 `error.body["innererror"]["content_filter_result"]`；Responses API 使用 `error.body["content_filters"][0]["content_filter_results"]`（複數形式，且在陣列中）。重寫所有 `innererror` 存取。 |

---

## 遷移風險表

| 徵狀 | 可能錯誤 | 解決方法 |
|---------|---------------|-----|
| `output_text` 為空或回應被截斷 | `max_output_tokens` 對推理模型太低 | 設定 `max_output_tokens=1000` 或更高 — 推理的字元計算在限制中 |
| `400 invalid_type: text.format` | 傳入 `response_format` 字串而非 `text.format` 字典 | 使用 `text={"format": {"type": "json_schema", "name": "...", "strict": True, "schema": {...}}}` |
| `/openai/v1/responses` 出現 `404 Not Found` | `base_url` 錯誤 — 缺少 `/openai/v1/` 後綴 | 確保 `base_url=f"{endpoint}/openai/v1/"`（帶斜線結尾） |
| 換用 `OpenAI()` 後出現 `401 Unauthorized` | 未設定 `api_key` 或未正確傳入 token provider | EntraID 使用：`api_key=token_provider`（callable）。API key 使用：`api_key=os.environ["AZURE_OPENAI_API_KEY"]` |
| 模型回傳 `deployment not found` | `model` 參數與 Azure 部署名稱不符 | 使用 `model=os.environ["AZURE_OPENAI_DEPLOYMENT"]` — 這是部署名稱，不是模型名稱 |
| `json.loads(resp.output_text)` 拋出 `JSONDecodeError` | 架構未強制執行或模型不支援嚴格 JSON | 確認 schema 中 `"strict": True`，並驗證模型支持結構化輸出 |
| 串流無 `delta` 事件 | 檢查錯誤的事件類型 | 過濾條件用 `event.type == "response.output_text.delta"`，而非聊天的 `chat.completion.chunk` |
| 遷移後影像輸入引發 `400` 錯誤 | 未更新影像內容類型 | 將 `"type": "image_url"` 改為 `"type": "input_image"`，並將 `"image_url": {"url": "..."}` 攤平成 `"image_url": "..."`（純字串） |
| 工具呼叫陷入無限迴圈 | 後續 `input` 缺少工具結果 | 執行工具後，於下一次請求的 `input` 新增 `{"type": "function_call_output", "call_id": ..., "output": ...}` 項目 |
| GPT-5 或 o 系列出現 `temperature` 錯誤 | 明確設定 `temperature` 值非 1 | 刪除 `temperature` 或設定為 `1`，適用 GPT-5 與 o 系列模型 (o1, o3-mini, o3, o4-mini) |
| o 系列出現 `top_p` 錯誤 | 不支援 `top_p` | 使用 o 系列模型時移除 `top_p` |
| `max_completion_tokens` 不被識別 | 使用 Azure 專屬參數 | 改用 `max_output_tokens`。 o 系列設定為 4096+（推理字元計在限制內）。 |
| o 系列表現出空白或截斷輸出 | `max_output_tokens` 設太低 | o 系列內部使用推理字元。設定 `max_output_tokens=4096` 或更高 — 不是 500–1000。 |
| `max_output_tokens` 出現 `400 integer_below_min_value` | 數值低於 16 | Azure OpenAI 強制 `max_output_tokens >= 16`。冒煙測試用 50+，正式環境用 1000+。 |
| 串流中斷出現 `429 Too Many Requests` | Azure OpenAI 限流 | 串流會默默斷開且無錯誤。請始終將 `async for event in await coroutine:` 包在 `try/except`，並向前端輸出 `{"error": str(e)}`。 |
| `AzureDeveloperCliCredential` 出現 `CredentialUnavailableError` | 租戶錯誤或未登入 | 明確傳入 `tenant_id=os.getenv("AZURE_TENANT_ID")`。本地運行 `azd auth login --tenant <tenant-id>`。 |
| 使用 GitHub 模型 (`models.github.ai`) 出現 `404 Not Found` | GitHub 模型不支援 Responses API | 完全移除 GitHub 模型代碼路徑。使用 Azure OpenAI、OpenAI 或相容的本地端點 (如 Ollama 支援 Responses)。 |
| MAF `OpenAIChatCompletionClient` 仍使用聊天補全 | MAF 1.0.0+ 使用舊版客戶端 | MAF 1.0.0+ 預設使用 `OpenAIChatClient`（Responses API）。用 `OpenAIChatClient` 替換 `OpenAIChatCompletionClient`。前 1.0.0 請升級至 `agent-framework-openai>=1.0.0`。 |
| LangChain 智能代理空回或工具呼叫失敗 | `ChatOpenAI` 未用 Responses API | 加入 `use_responses_api=True` 於 `ChatOpenAI(...)`。回應訊息使用 `.text` 取代 `.content`。 |
| Content filter 錯誤處理拋出 `KeyError: 'innererror'` | Responses API 中錯誤體結構變更 | 將 `error.body["innererror"]["content_filter_result"]["jailbreak"]` 改為 `error.body["content_filters"][0]["content_filter_results"]["jailbreak"]`。`innererror` 層已消失；內容過濾詳細資料移至頂級 `content_filters` 陣列中，每項含複數 `content_filter_results`。 |
| 原始 HTTP 呼叫 `/openai/deployments/.../chat/completions` 回傳 404 | 舊版聊天補全 REST 端點 | 改寫 URL 為 `/openai/v1/responses`。請求體 `messages` 改用 `input`，加上 `max_output_tokens` + `store: false`，移除 `api-version` 查詢參數。回應解析改為：`choices[0].message.content` → `output[0].content[0].text`（注意：`output_text` 為 SDK 方便性屬性，非原始 REST JSON）。 |

---

## 陷阱

1. 先前使用聊天補全管理對話狀態，改用 Responses 面需自行明確管理狀態。
2. 優先使用 `max_output_tokens`，取代舊有的 `max_tokens`。
3. 遷移至 `gpt-5` 時，確保未指定 `temperature` 或將其設為 `1`。
4. 將聊天的 `content[].type: "text"` 替換為 Responses 的 `content[].type: "input_text"`，用於用戶或系統輸入。
5. `text.format` 應供給適當字典 (例如 `{"type": "json_schema", "name": "Output", "schema": ..., "strict": True}`)，而非單純字串。
6. Responses 不支援 `seed` 參數，請從請求中移除。
7. **推理(Reasoning)**：僅在原始程式碼已使用推理時包含它。不要在未使用推理的 API 呼叫中新增此參數 — 許多非推理模型不支援。
8. **`max_output_tokens` 大小設定**：推理模型 (GPT-5-mini、GPT-5、o 系列) 使用 `max_output_tokens=4096` 或更高 — 非 50–1000。模型內部計算推理字元後才產出可見輸出；限制過低會導致截斷或空白回應。
9. **o 系列 `max_completion_tokens`**：原始代碼使用 o 系列 Azure 專屬參數 `max_completion_tokens`，請改用 `max_output_tokens`。Responses API 不接受 `max_completion_tokens`。
10. **o 系列 `reasoning_effort`**：原始代碼使用 `reasoning_effort`（low/medium/high），請改為在 Responses API 呼叫中使用 `reasoning={"effort": "<value>"}`。
11. **o 系列串流延遲**：o 系列模型在產出輸出前會先進行內部推理。串流時，第一個 `response.output_text.delta` 事件會有較長延遲。這是正常現象 — 模型正在推理，非卡死。
9. **`_azure_ad_token_provider` 已移除**：`AsyncOpenAI` / `OpenAI` 不再有 `_azure_ad_token_provider` 屬性。測試或程式碼中存取此屬性將引發 `AttributeError`。token provider 以 `api_key` 形式傳入，無法透過客戶端物件存取。
10. **快照/金典檔案**：若測試套件使用快照測試，所有含聊天補全串流形狀（`choices[0]`、`content_filter_results`、`function_call` 等）之快照檔案<strong>必須</strong>更新為新的 Responses 形狀。此處容易遺漏，會導致快照斷言失敗。
11. <strong>模擬猴子補丁路徑</strong>：猴子補丁目標由 `openai.resources.chat.AsyncCompletions.create` 改為 `openai.resources.responses.AsyncResponses.create`（同步使用 `Responses.create`）。舊路徑不會生效 — 模擬無法攔截，測試會呼叫真實 API 或失敗。
12. **使用 `input` 取代 `messages`**：模擬函式須讀取 `kwargs.get("input")`，而非 `kwargs.get("messages")`。Responses API 使用 `input` 儲存對話歷史。
13. <strong>環境變量命名</strong>：Azure Identity SDK 使用 `AZURE_CLIENT_ID`（非 `AZURE_OPENAI_CLIENT_ID`）做為 `ManagedIdentityCredential(client_id=...)`。請在測試、`.env`、應用設定及 Bicep/基礎建設中更新名稱。
14. **`max_output_tokens` 最小值為 16**：Azure OpenAI 拒絕值低於16並回傳 `400 integer_below_min_value`。冒煙測試用 50，正式環境用 1000+。舊參數 `max_tokens` 無此限制。
15. **`AzureDeveloperCliCredential` 的 `tenant_id`**：當 Azure OpenAI 資源不在同一租戶，必須明確傳入 `tenant_id` — `AzureDeveloperCliCredential(tenant_id=os.getenv("AZURE_TENANT_ID"))`。否則憑證會默默使用錯誤租戶並回傳 `401`。
16. <strong>限流行為於串流中呈現差異</strong>：聊天補全時，429 錯誤通常阻止串流開啟。使用 Responses API 串流時，429 錯誤可能於<strong>串流中間</strong>發生 — 非同步迭代器會丟出例外。請始終將串流迴圈包在 `try/except`，並輸出錯誤 JSON 行讓前端能優雅處理。

17. <strong>網頁應用必須處理串流錯誤</strong>：`try: async for event in await coroutine: ... except Exception as e: yield json.dumps({"error": str(e)})` 這個模式非常重要。若沒有它，SSE/JSONL 串流在任何伺服器端錯誤時會悄悄停止，前端則會卡住。
18. <strong>工具定義必須使用扁平格式</strong>：Responses API 預期 `{"type": "function", "name": ..., "parameters": ...}` — 而不是 Chat Completions 的巢狀格式 `{"type": "function", "function": {"name": ..., "parameters": ...}}`。這是函式呼叫代碼遷移中最常見的錯誤。
19. **`pydantic_function_tool()` 不相容**：`openai.pydantic_function_tool()` 助手仍然產生舊的巢狀格式。不要與 `responses.create()` 一起使用。請手動定義工具架構或扁平化輸出。
20. **工具結果應使用 `function_call_output`，非 `role: tool`**：執行工具後，應附加 `{"type": "function_call_output", "call_id": ..., "output": ...}` — 而非 `{"role": "tool", "tool_call_id": ..., "content": ...}`。對助理的工具呼叫，使用 `messages.extend(response.output)` — 而非手動建立 `{"role": "assistant", "tool_calls": [...]}` 字典。
21. **`strict: true` 需要 `required` + `additionalProperties: false`**：當對工具設置 `strict: true` 時，每個屬性必須列在 `required` 陣列中，且 `additionalProperties` 必須為 `false`。缺少其中任一項都會導致 400 錯誤。
22. **函式呼叫 ID 有特定前綴**：在 `input` 中提供少量 `function_call` 項目時，`id` 欄位必須以 `fc_` 開頭，而 `call_id` 欄位必須以 `call_` 開頭（例如 `"id": "fc_example1", "call_id": "call_example1"`）。使用舊 Chat Completions 的 `call_` 前綴作為 `id` 會被拒絕。
23. **GitHub Models 不支援 Responses API**：若應用程式有 GitHub Models 代碼路徑（`base_url` 指向 `models.github.ai` 或 `models.inference.ai.azure.com`），請完全移除。此無遷移途徑 — 請切換至 Azure OpenAI、OpenAI 或相容的本地端點。
24. <strong>內容過濾錯誤主體結構變更</strong>：Chat Completions 錯誤使用 `error.body["innererror"]["content_filter_result"]`（單數）。Responses API 錯誤改用 `error.body["content_filters"][0]["content_filter_results"]`（複數且在陣列中）。已不再有 `innererror` 鍵。直接存取 `innererror` 的程式碼在執行時會引發 `KeyError` — 這在遷移時容易錯過，因為只有在內容過濾觸發時才會浮現。遷移時一定要 grep `innererror`。
25. **直接 HTTP 呼叫需重寫 URL + 主體**：應用程式透過 `/openai/deployments/{name}/chat/completions?api-version=...` 使用 `requests`、`httpx`、`aiohttp` 直接呼叫 Azure OpenAI REST，必須改為 `/openai/v1/responses`。請求主體改用 `input` 取代 `messages`，並要求 `max_output_tokens` 和 `store`，且移除 `api-version` 查詢參數。回應主體文字在 `output[0].content[0].text` — <strong>非</strong> `output_text`，後者是 SDK 的便利屬性，原生 REST JSON 中不存在。

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責聲明**：
本文件使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。雖然我們力求準確，但請注意，自動翻譯可能包含錯誤或不準確之處。原始文件的母語版本應被視為權威來源。對於重要資訊，建議尋求專業人工翻譯。我們不對因使用本翻譯而引起的任何誤解或曲解承擔責任。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->