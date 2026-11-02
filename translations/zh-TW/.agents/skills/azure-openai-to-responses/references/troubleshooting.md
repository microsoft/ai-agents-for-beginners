# 故障排除、風險表格與注意事項

## 400 錯誤故障排除

| 錯誤 | 修正方法 |
|-------|-----|
| `missing_required_parameter: tools[0].name` | 工具定義使用舊的 Chat Completions 巢狀格式 | 從 `{"type": "function", "function": {"name": ...}}` 扁平化為 `{"type": "function", "name": ..., "parameters": ...}` — name、description、parameters 放在頂層 |
| `unknown_parameter: input[N].tool_calls` | 多回合工具結果使用舊的 Chat Completions 格式 | 將 `{"role": "assistant", "tool_calls": [...]}` + `{"role": "tool", ...}` 替換成 `response.output` 項目 + `{"type": "function_call_output", "call_id": ..., "output": ...}` |
| `invalid_function_parameters: 'required' is required` | `strict: true` 的工具缺少 `required` 陣列 | 當 `strict: true` 時，所有屬性必須列在 `required` 中，且必須設定 `additionalProperties: false` |
| `invalid_function_parameters: 'additionalProperties' is required` | `strict: true` 工具缺少 `additionalProperties: false` | 在參數物件中加入 `"additionalProperties": false` |
| `invalid input[N].id: Expected an ID that begins with 'fc'` | Few-shot function_call 的 ID 前綴錯誤 | 函數調用 ID 必須以 `fc_` 開頭（例如 `fc_example1`），不能是 `call_` |
| `missing_required_parameter: text.format.name` | 在 format 字典中加入 `"name"` 鍵（例如 `"name": "Output"`） |
| `invalid_type: text.format` | 確保 `text.format` 是含有 `type`、`name`、`strict`、`schema` 鍵的字典，而非字串 |
| `invalid input content type` | 使用 `input_text`/`output_text` 內容類型，替代 Chat 的 `text` |
| `invalid input content type`（圖片） | 圖片內容仍使用 `"type": "image_url"` | 改為 `"type": "input_image"` |
| `Expected object, got string` 在 `image_url` | `image_url` 仍是巢狀物件 `{"url": "..."}` | 扁平為純字串：`"image_url": "https://..."` 或 `"image_url": "data:image/...;base64,..."` |
| `integer below minimum value` 對 `max_output_tokens` | Azure OpenAI 最小值是 **16**。測試用建議用 50+，正式環境用 1000+。 |
| 串流時出現 `429 Too Many Requests` | 速率限制。將串流包在 `try/except` 中，向前端產生錯誤 JSON，實作退避/重試機制。 |
| 內容過濾錯誤時發生 `KeyError: 'innererror'` | Responses API 內容過濾錯誤回應體結構改變 | Chat Completions 用 `error.body["innererror"]["content_filter_result"]`；Responses API 改為 `error.body["content_filters"][0]["content_filter_results"]`（複數，包在陣列內）。重新撰寫所有 `innererror` 存取。 |

---

## 遷移風險表

| 症狀 | 可能錯誤 | 修正方法 |
|---------|---------------|-----|
| 空白的 `output_text` / 回應被截斷 | 推理模型的 `max_output_tokens` 設定太低 | 設定 `max_output_tokens=1000` 或更高 — 推理令牌會佔用額度 |
| `400 invalid_type: text.format` | 傳入 `response_format` 字串而非 `text.format` 字典 | 使用 `text={"format": {"type": "json_schema", "name": "...", "strict": True, "schema": {...}}}` |
| 在 `/openai/v1/responses` 出現 `404 Not Found` | `base_url` 錯誤 — 缺少 `/openai/v1/` 後綴 | 確保 `base_url=f"{endpoint}/openai/v1/"`（包含尾斜線） |
| 切換至 `OpenAI()` 後出現 `401 Unauthorized` | `api_key` 未設或 token provider 傳遞錯誤 | EntraID：`api_key=token_provider`（可呼叫物件）。API 金鑰：`api_key=os.environ["AZURE_OPENAI_API_KEY"]` |
| 模型回覆 `deployment not found` | `model` 參數與 Azure 部署名稱不符 | 使用 `model=os.environ["AZURE_OPENAI_DEPLOYMENT"]` — 這是部署名稱，不是模型名稱 |
| `json.loads(resp.output_text)` 報 `JSONDecodeError` | 未嚴格執行 schema 或模型不支援嚴格 JSON | 確認 schema 中 `"strict": True`，並驗證模型支援結構化輸出 |
| 串流沒有產生 `delta` 事件 | 檢查錯誤的事件類型 | 篩選條件為 `event.type == "response.output_text.delta"`，不是 Chat 的 `chat.completion.chunk` |
| 遷移後影像輸入出現 `400` 錯誤 | 圖片內容類型未更新 | 將 `"type": "image_url"` 改成 `"type": "input_image"` 並扁平 `"image_url": {"url": "..."}` 改為 `"image_url": "..."`（純字串） |
| 工具呼叫無限循環 | 下一次 `input` 中缺少工具結果 | 執行工具後，在下一個請求的 `input` 中加入 `{"type": "function_call_output", "call_id": ..., "output": ...}` 項目 |
| GPT-5 或 o 系列模型出現 `temperature` 錯誤 | 明確指定非 1 的 `temperature` | 移除 `temperature` 或設為 `1`，適用 GPT-5 和 o 系列模型（o1、o3-mini、o3、o4-mini） |
| o 系列模型報 `top_p` 錯誤 | 不支援 `top_p` | 針對 o 系列模型移除 `top_p` |
| `max_completion_tokens` 無法識別 | 使用 Azure 特定參數 | 將 `max_completion_tokens` 換成 `max_output_tokens`。o 系列設定 4096+（推理令牌佔用額度）。 |
| o 系列模型輸出空白或被截斷 | `max_output_tokens` 設定太低 | o 系列內部使用推理令牌。設定 `max_output_tokens=4096` 或更高 — 不要設成 500–1000。 |
| `max_output_tokens` 出現 `400 integer_below_min_value` | 數值小於 16 | Azure OpenAI 強制 `max_output_tokens >= 16`。煙霧測試使用 50+，正式環境使用 1000+。 |
| 串流中途出現 `429 Too Many Requests` | Azure OpenAI 被速率限制 | 串流會在沒有錯誤提示的情況下斷掉。務必將 `async for event in await coroutine:` 包在 `try/except`，並將 `{"error": str(e)}` 傳給前端。 |
| 使用 `AzureDeveloperCliCredential` 發生 `CredentialUnavailableError` | 租戶錯誤或未登入 | 明確傳遞 `tenant_id=os.getenv("AZURE_TENANT_ID")`。本機執行 `azd auth login --tenant <tenant-id>`。 |
| 使用 GitHub 模型 (`models.github.ai`) 回傳 `404 Not Found` | GitHub 模型不支援 Responses API | 徹底移除 GitHub 模型程式碼路徑。請使用 Azure OpenAI、OpenAI 或相容的本地端點（例如支援 Responses 的 Ollama）。 |
| MAF `OpenAIChatCompletionClient` 仍使用 Chat Completions | MAF 版本 1.0.0 以上使用舊版客戶端 | 在 MAF 1.0.0 以上版本中，`OpenAIChatClient` 預設改用 Responses API。將 `OpenAIChatCompletionClient` 替換為 `OpenAIChatClient`。若版本早於 1.0.0，請更新至 `agent-framework-openai>=1.0.0`。 |
| LangChain 代理呼叫工具時回傳空白或失敗 | `ChatOpenAI` 未使用 Responses API | 在 `ChatOpenAI(...)` 新增 `use_responses_api=True`。回應訊息屬性 `.content` 改用 `.text`。 |
| 內容過濾錯誤處理時發生 `KeyError: 'innererror'` | Responses API 的錯誤體結構改變 | 將 `error.body["innererror"]["content_filter_result"]["jailbreak"]` 改為 `error.body["content_filters"][0]["content_filter_results"]["jailbreak"]`。`innererror` 包裝層已移除；內容過濾詳情現存於頂層 `content_filters` 陣列中，陣列項目包含複數的 `content_filter_results`。 |
| 使用原始 HTTP 呼叫 `/openai/deployments/.../chat/completions` 回傳 404 | 舊的 Chat Completions REST 端點 | 將 URL 改寫為 `/openai/v1/responses`。請求體 `messages` 改為 `input`，新增 `max_output_tokens` 與 `store: false`，移除 `api-version` 查詢參數。解析回應時，從 `choices[0].message.content` 改為 `output[0].content[0].text`（註：`output_text` 是 SDK 的便利屬性，原始 REST JSON 中無此欄位）。 |

---

## 注意事項

1. 如果先前使用 Chat Completions 管理對話狀態，請改用 Responses 明確管理自己的狀態。
2. 優先使用 `max_output_tokens`，取代舊有的 `max_tokens`。
3. 遷移到 `gpt-5` 時，確保未指定 `temperature` 或將其設為 `1`。
4. 對於使用者與系統輸入，將 Chat 的 `content[].type: "text"` 替換為 Responses 的 `content[].type: "input_text"`。
5. 對於 `text.format`，提供正確的字典（例如 `{"type": "json_schema", "name": "Output", "schema": ..., "strict": True}`），而非純字串。
6. `seed` 參數在 Responses 中不支援，請自請求中移除。
7. **推理（reasoning）**：只有當原始程式已使用此功能時，才加入 `reasoning`。不要對未使用推理的模型調用額外加入此參數，因為多數非推理模型不支援。
8. **`max_output_tokens` 大小設定**：針對推理模型（GPT-5-mini、GPT-5、o 系列），使用 `max_output_tokens=4096` 或更高，不可使用 50–1000。模型內部會使用推理令牌於輸出前，設定太低會導致回應被截斷或空白。
9. **o 系列的 `max_completion_tokens`**：若原程式使用 Azure 特定參數 `max_completion_tokens`，請替換成 `max_output_tokens`。Responses API 不接受 `max_completion_tokens`。
10. **o 系列的 `reasoning_effort`**：若原程式使用 `reasoning_effort`（low/medium/high），請轉換為 Responses API 的 `reasoning={"effort": "<值>"}`。
11. **o 系列串流延遲**：o 系列模型會先執行內部推理再輸出結果。串流時首個 `response.output_text.delta` 事件會較晚出現，此為正常，表示模型正在推理而非當機。
9. **`_azure_ad_token_provider` 已移除**：`AsyncOpenAI` / `OpenAI` 已無 `_azure_ad_token_provider` 屬性。測試或程式碼若存取此屬性，會產生 `AttributeError`。token provider 改以 `api_key` 傳入，且客戶端物件無法觀察此屬性。
10. **快照 / golden 檔案**：若測試套件用快照測試，<strong>所有</strong>含有 Chat Completions 串流結構（`choices[0]`、`content_filter_results`、`function_call` 等）的快照檔案都必須更新為新的 Responses 結構。這常被忽略且會引起快照斷言失敗。
11. **模擬（mock）套件路徑變動**：模擬目標從 `openai.resources.chat.AsyncCompletions.create` 改成 `openai.resources.responses.AsyncResponses.create`（同步為 `Responses.create`）。使用舊路徑不會生效，模擬無法攔截請求，導致實際呼叫API或測試失敗。
12. **`input` 非 `messages`**：模擬函式必須讀取 `kwargs.get("input")`，非 `kwargs.get("messages")`。Responses API 使用 `input` 作為對話歷史參數。
13. <strong>環境變數命名</strong>：Azure 身分驗證 SDK 使用 `AZURE_CLIENT_ID`（非 `AZURE_OPENAI_CLIENT_ID`）作為 `ManagedIdentityCredential(client_id=...)` 的參數。請在測試、`.env` 檔案、應用設定及 Bicep/基礎建設中改名。
14. **`max_output_tokens` 最小值為 16**：Azure OpenAI 會對小於 16 的數值以 `400 integer_below_min_value` 拒絕。測試用建議使用 50，正式環境使用 1000 以上。舊有的 `max_tokens` 沒有此限制。
15. **針對 `AzureDeveloperCliCredential` 的 `tenant_id`<strong>：Azure OpenAI 資源位於不同租戶時，</strong>必須**明確傳入 `tenant_id` — `AzureDeveloperCliCredential(tenant_id=os.getenv("AZURE_TENANT_ID"))`。若缺少，認證會默認錯誤租戶，回傳 `401`。
16. <strong>速率限制串流時行為不同</strong>：Chat Completions 常見 429 錯誤會阻止串流啟動。使用 Responses API 串流時，429 可能在串流中途發生，非同步迭代器會拋出例外。務必將串流迴圈包在 `try/except` 中，並傳出錯誤 JSON，前端才能優雅處理。

17. <strong>網頁應用必須強制處理串流錯誤</strong>：模式 `try: async for event in await coroutine: ... except Exception as e: yield json.dumps({"error": str(e)})` 非常關鍵。若沒有此機制，SSE/JSONL 串流將在任何伺服器端錯誤時無聲終止，前端會掛起。
18. <strong>工具定義必須使用扁平格式</strong>：Responses API 預期格式為 `{"type": "function", "name": ..., "parameters": ...}` — 不是 Chat Completions 嵌套的 `{"type": "function", "function": {"name": ..., "parameters": ...}}`。這是函數呼叫程式碼遷移中最常見的錯誤。
19. **`pydantic_function_tool()` 不相容**：`openai.pydantic_function_tool()` 輔助函數仍會產生舊式的嵌套格式，請勿與 `responses.create()` 一起使用。請手動定義工具 schema 或將輸出扁平化。
20. **工具結果需使用 `function_call_output`，而非 `role: tool`**：執行工具後，附加 `{"type": "function_call_output", "call_id": ..., "output": ...}` — 而非 `{"role": "tool", "tool_call_id": ..., "content": ...}`。助理的工具請求，使用 `messages.extend(response.output)` — 而非手動建立 `{"role": "assistant", "tool_calls": [...]}` 字典。
21. **`strict: true` 需 `required` + `additionalProperties: false`**：在工具上使用 `strict: true` 時，每個屬性都必須列在 `required` 陣列中，且 `additionalProperties` 必須設為 `false`。任一缺失都會造成 400 錯誤。
22. **函數呼叫 ID 有特定前綴**：在 `input` 中提供少量範例 `function_call` 項目時，`id` 欄位必須以 `fc_` 開頭，`call_id` 欄位必須以 `call_` 開頭（例如 `"id": "fc_example1", "call_id": "call_example1"`）。舊版 Chat Completions 的 `call_` 前綴用於 `id` 會被拒絕。
23. **GitHub Models 不支援 Responses API**：若應用包含 GitHub Models 的程式碼路徑（`base_url` 指向 `models.github.ai` 或 `models.inference.ai.azure.com`），請完全移除。此無遷移路徑 — 請切換至 Azure OpenAI、OpenAI 或相容的本地端點。
24. <strong>內容過濾錯誤主體結構變更</strong>：Chat Completions 的錯誤使用 `error.body["innererror"]["content_filter_result"]`（單數）。Responses API 錯誤使用 `error.body["content_filters"][0]["content_filter_results"]`（複數，且在陣列內）。`innererror` 鍵已不存在。直接存取 `innererror` 的程式碼執行時會拋出 `KeyError` — 這在遷移時很容易被忽略，因為只有當內容過濾觸發時才會發生。遷移期間務必搜尋 `innererror`。
25. **原始 HTTP 呼叫需重寫 URL + 主體**：直接呼叫 Azure OpenAI REST（透過 `requests`、`httpx`、`aiohttp`）用 `/openai/deployments/{name}/chat/completions?api-version=...` 的應用必須改用 `/openai/v1/responses`。請求主體使用 `input` 取代 `messages`，並需 `max_output_tokens` 及 `store`，且移除 `api-version` 查詢參數。回應主體文字位於 `output[0].content[0].text` — <strong>非</strong> `output_text`，後者為 SDK 的便利屬性，原始 REST JSON 中無此欄位。

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責聲明**：
此文件已使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。雖然我們努力追求準確性，但請注意自動翻譯可能包含錯誤或不準確之處。原始文件的母語版本應視為權威來源。對於關鍵資訊，建議採用專業人工翻譯。我們不對因使用此翻譯所產生的任何誤解或誤譯承擔責任。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->