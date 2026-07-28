# 故障排除、风险表及注意事项

## 400错误故障排除

| 错误 | 解决方法 |
|-------|-----|
| `missing_required_parameter: tools[0].name` | 工具定义使用了旧的聊天完成嵌套格式 | 将 `{"type": "function", "function": {"name": ...}}` 平铺为 `{"type": "function", "name": ..., "parameters": ...}` — name、description、parameters 放到顶层 |
| `unknown_parameter: input[N].tool_calls` | 多轮工具结果使用了旧的聊天完成格式 | 用 `response.output` 项和 `{"type": "function_call_output", "call_id": ..., "output": ...}` 替换 `{"role": "assistant", "tool_calls": [...]}` + `{"role": "tool", ...}` |
| `invalid_function_parameters: 'required' is required` | `strict: true` 的工具缺少 `required` 数组 | 当 `strict: true` 时，所有属性必须列在 `required` 中且必须设置 `additionalProperties: false` |
| `invalid_function_parameters: 'additionalProperties' is required` | `strict: true` 的工具缺少 `additionalProperties: false` | 在参数对象中添加 `"additionalProperties": false` |
| `invalid input[N].id: Expected an ID that begins with 'fc'` | 少样本 function_call ID 前缀错误 | function_call ID 必须以 `fc_` 开头（例如 `fc_example1`），而不是 `call_` |
| `missing_required_parameter: text.format.name` | 为格式字典添加 `"name"` 键（例如 `"name": "Output"`） |
| `invalid_type: text.format` | 确保 `text.format` 是包含 `type`、`name`、`strict`、`schema` 键的字典 — 而非字符串 |
| `invalid input content type` | 使用 `input_text`/`output_text` 内容类型代替聊天 `text` |
| `invalid input content type`（图片） | 图片内容仍使用 `"type": "image_url"` | 更改为 `"type": "input_image"` |
| `Expected object, got string` 在 `image_url` 上 | `image_url` 仍是嵌套对象 `{"url": "..."}` | 展平为纯字符串：`"image_url": "https://..."` 或 `"image_url": "data:image/...;base64,..."` |
| `integer below minimum value` 针对 `max_output_tokens` | Azure OpenAI 最小值为 **16**。测试中使用 50+，生产中使用 1000+。 |
| 流式传输时出现 `429 Too Many Requests` | 请求频率限制。将流式传输包裹在 `try/except`，向前端返回错误 JSON，实现重试/退避。 |
| 内容过滤错误时出现 `KeyError: 'innererror'` | 内容过滤错误体结构在 Responses API 中变更 | 聊天完成使用 `error.body["innererror"]["content_filter_result"]`；Responses API 使用 `error.body["content_filters"][0]["content_filter_results"]`（复数且在数组中）。重写所有 `innererror` 访问。 |

---

## 迁移风险表

| 症状 | 可能错误 | 解决方案 |
|---------|---------------|-----|
| 空的 `output_text` / 响应被截断 | 对推理模型 `max_output_tokens` 过低 | 设置 `max_output_tokens=1000` 或更高 — 推理令牌计入限制 |
| `400 invalid_type: text.format` | 传入了 `response_format` 字符串而非 `text.format` 字典 | 使用 `text={"format": {"type": "json_schema", "name": "...", "strict": True, "schema": {...}}}` |
| `/openai/v1/responses` 返回 `404 Not Found` | 错误的 `base_url` — 缺少 `/openai/v1/` 后缀 | 确保 `base_url=f"{endpoint}/openai/v1/"`（包括尾部斜杠） |
| 切换到 `OpenAI()` 后出现 `401 Unauthorized` | `api_key` 未设置或令牌提供者传递不正确 | 对于 EntraID：`api_key=token_provider`（可调用）。对 API 密钥：`api_key=os.environ["AZURE_OPENAI_API_KEY"]` |
| 模型返回 `deployment not found` | `model` 参数与 Azure 部署名称不符 | 使用 `model=os.environ["AZURE_OPENAI_DEPLOYMENT"]` — 它是部署名称，不是模型名称 |
| `json.loads(resp.output_text)` 抛出 `JSONDecodeError` | 未强制执行 schema 或模型不支持严格 JSON | 确保 schema 中有 `"strict": True`，并确认模型支持结构化输出 |
| 流式传输无 `delta` 事件 | 检查了错误的事件类型 | 过滤条件应为 `event.type == "response.output_text.delta"`，而非聊天的 `chat.completion.chunk` |
| 迁移后图片输入出现 `400` 错误 | 图片内容类型未更新 | 将 `"type": "image_url"` 改为 `"type": "input_image"`，并将 `"image_url": {"url": "..."}` 展平为 `"image_url": "..."`（纯字符串） |
| 工具调用无限循环 | 后续 `input` 缺少工具结果 | 执行完工具后，在下一次请求的 `input` 中追加 `{"type": "function_call_output", "call_id": ..., "output": ...}` 项 |
| GPT-5 或 o 系列出现 `temperature` 错误 | 明确指定了非 1 的 `temperature` 值 | 移除 `temperature` 或设为 `1`，适用于 GPT-5 和 o 系列模型（o1、o3-mini、o3、o4-mini） |
| o 系列出现 `top_p` 错误 | 不支持 `top_p` | 针对 o 系列模型移除 `top_p` |
| 不识别 `max_completion_tokens` | 使用了 Azure 特有参数 | 用 `max_output_tokens` 替代。对 o 系列设置为 4096+（推理令牌计入限制）。 |
| o 系列输出为空或被截断 | `max_output_tokens` 过低 | o 系列内部使用推理令牌。设置 `max_output_tokens=4096` 或更高，避免 500–1000。 |
| `400 integer_below_min_value` 针对 `max_output_tokens` | 值低于 16 | Azure OpenAI 强制 `max_output_tokens >= 16`。烟雾测试用 50+，生产用 1000+。 |
| 流程中出现 `429 Too Many Requests` | 被 Azure OpenAI 限速 | 流被无声中断且不报错。始终将 `async for event in await coroutine:` 包裹在 `try/except` 中，向前端返回 `{"error": str(e)}`。 |
| `AzureDeveloperCliCredential` 报 `CredentialUnavailableError` | 租户错误或未登录 | 明确传递 `tenant_id=os.getenv("AZURE_TENANT_ID")`。本地运行 `azd auth login --tenant <tenant-id>`。 |
| 使用 GitHub 模型（`models.github.ai`）时出现 `404 Not Found` | GitHub 模型不支持 Responses API | 完全移除 GitHub 模型代码路径。使用 Azure OpenAI、OpenAI 或兼容的本地端点（例如支持 Responses 的 Ollama）。 |
| MAF `OpenAIChatCompletionClient` 仍使用聊天完成 | 1.0.0 及以上版本使用遗留 MAF 客户端 | 在 MAF 1.0.0+ 中，`OpenAIChatClient` 默认使用 Responses API。用 `OpenAIChatClient` 替换 `OpenAIChatCompletionClient`。1.0.0 之前版本，升级 `agent-framework-openai>=1.0.0`。 |
| LangChain 代理工具调用返回空或失败 | `ChatOpenAI` 未使用 Responses API | 在 `ChatOpenAI(...)` 中添加 `use_responses_api=True`。响应消息 `.content` 改 `.text`。 |
| 内容过滤错误处理器中出现 `KeyError: 'innererror'` | Responses API 中错误体结构变更 | 重写 `error.body["innererror"]["content_filter_result"]["jailbreak"]` 为 `error.body["content_filters"][0]["content_filter_results"]["jailbreak"]`。`innererror` 包装已去除，内容过滤详情现分布于顶层 `content_filters` 数组内的复数 `content_filter_results`。 |
| 直接调用 `/openai/deployments/.../chat/completions` 返回 404 | 旧聊天完成 REST 端点 | 重写 URL 为 `/openai/v1/responses`。请求体改为：`messages` → `input`，添加 `max_output_tokens` + `store: false`，去除 `api-version` 查询参数。响应解析改为：`choices[0].message.content` → `output[0].content[0].text`（注意：`output_text` 是 SDK 便利属性，不在原始 REST JSON 中）。 |

---

## 注意事项

1. 如果你之前用聊天完成管理会话状态，改用 Responses 时需显式管理你自己的状态。
2. 建议使用 `max_output_tokens` 代替遗留的 `max_tokens`。
3. 迁移至 `gpt-5` 时，确保未指定 `temperature` 或值为 `1`。
4. 将聊天的 `content[].type: "text"` 替换为 Responses 的 `content[].type: "input_text"`，适用于用户/系统输入。
5. 对 `text.format`，提供正确的字典（例如 `{"type": "json_schema", "name": "Output", "schema": ..., "strict": True}`），而非纯字符串。
6. Responses 不支持 `seed` 参数；从请求中移除它。
7. <strong>推理</strong>：仅在原代码已使用推理时包含 `reasoning`。不要对未使用推理的 API 调用添加 `reasoning` — 许多非推理模型不支持此参数。
8. **`max_output_tokens` 大小**：针对推理模型（GPT-5-mini、GPT-5、o 系列），使用 `max_output_tokens=4096` 或更高 — 非 50–1000。模型在生成可见输出前使用推理令牌；限制过低会导致响应被截断或为空。
9. **o 系列 `max_completion_tokens`**：如果原代码使用了 o 系列特有的 `max_completion_tokens`，请替换为 `max_output_tokens`。Responses API 不接受 `max_completion_tokens`。
10. **o 系列 `reasoning_effort`**：若原代码使用了 `reasoning_effort`（low/medium/high），迁移时在 Responses API 调用中用 `reasoning={"effort": "<value>"}` 表示。
11. **o 系列流式延迟**：o 系列模型在生成输出前进行内部推理。流式时，首次出现 `response.output_text.delta` 事件前会有较长延迟。这是正常现象——模型在推理，而非卡死。
9. **`_azure_ad_token_provider` 已移除**：`AsyncOpenAI` / `OpenAI` 不再有 `_azure_ad_token_provider` 属性。测试或代码访问该属性会报 `AttributeError`。令牌提供者作为 `api_key` 传入，且客户端对象不可检查此属性。
10. **快照/金丝雀文件**：若测试套件使用快照测试，<strong>所有</strong>包含聊天完成流式模式（`choices[0]`、`content_filter_results`、`function_call` 等）的快照文件必须更新为新的 Responses 形态。这点容易遗漏，且会导致快照断言失败。
11. **Mock monkeypatch 路径**：monkeypatch 目标从 `openai.resources.chat.AsyncCompletions.create` 改为 `openai.resources.responses.AsyncResponses.create`（同步为 `Responses.create`）。使用旧路径不会报错但无效 —— mock 不生效，测试调用真实 API 或失败。
12. **`input` 非 `messages`**：Mock 函数必须读取 `kwargs.get("input")`，而非 `kwargs.get("messages")`。Responses API 使用 `input` 表示会话历史。
13. <strong>环境变量命名</strong>：Azure 身份 SDK 使用 `AZURE_CLIENT_ID`（非 `AZURE_OPENAI_CLIENT_ID`）作为 `ManagedIdentityCredential(client_id=...)`。测试、`.env` 文件、应用设置和 Bicep/基础设施中请做好调整。
14. **`max_output_tokens` 最小值为 16**：Azure OpenAI 拒绝小于 16 的值，报 `400 integer_below_min_value`。烟雾测试使用 50，生产使用 1000+。旧的 `max_tokens` 没有此限制。
15. **`AzureDeveloperCliCredential` 的 `tenant_id`<strong>：当 Azure OpenAI 资源位于不同租户时，</strong>必须**显式传入 `tenant_id` — `AzureDeveloperCliCredential(tenant_id=os.getenv("AZURE_TENANT_ID"))`。否则该凭据会默认错误租户，返回 `401`。
16. <strong>流式中速率限制表现不同</strong>：聊天完成时，429 通常阻止流开始。Responses API 流式，429 可发生在<strong>流中途</strong> — 异步迭代器抛出异常。务必将流循环包裹在 `try/except`，向前端返回错误 JSON 行，方便优雅处理。

17. **Web 应用必须进行流错误处理**：模式 `try: async for event in await coroutine: ... except Exception as e: yield json.dumps({"error": str(e)})` 至关重要。若无此处理，SSE/JSONL 流在任何服务器端错误时会静默终止，前端将卡死。
18. <strong>工具定义必须使用扁平格式</strong>：Responses API 期待的是 `{"type": "function", "name": ..., "parameters": ...}` — 不接受 Chat Completions 嵌套格式 `{"type": "function", "function": {"name": ..., "parameters": ...}}`。这是函数调用代码迁移中最常见的错误。
19. **`pydantic_function_tool()` 不兼容**：`openai.pydantic_function_tool()` 辅助方法仍然生成旧的嵌套格式。不要将其与 `responses.create()` 一起使用。应手动定义工具架构或扁平化输出。
20. **工具结果使用 `function_call_output`，而非 `role: tool`**：执行工具后，应附加 `{"type": "function_call_output", "call_id": ..., "output": ...}` — 而不是 `{"role": "tool", "tool_call_id": ..., "content": ...}`。对于助理的工具请求，用 `messages.extend(response.output)` — 不要手动使用 `{"role": "assistant", "tool_calls": [...]}` 字典。
21. **`strict: true` 需要 `required` + `additionalProperties: false`**：当在工具上使用 `strict: true` 时，每个属性必须列在 `required` 数组中，并且 `additionalProperties` 必须为 `false`。缺少任意一项都会导致 400 错误。
22. **函数调用 ID 需特定前缀**：当在 `input` 中提供少量 `function_call` 项时，`id` 字段必须以 `fc_` 开头，`call_id` 字段必须以 `call_` 开头（例如 `"id": "fc_example1", "call_id": "call_example1"`）。旧的 Chat Completions 使用 `call_` 作为 `id` 前缀会被拒绝。
23. **GitHub Models 不支持 Responses API**：如果应用有 GitHub Models 代码路径（`base_url` 指向 `models.github.ai` 或 `models.inference.ai.azure.com`），请完全移除。没有迁移路径 — 请切换到 Azure OpenAI、OpenAI 或兼容的本地端点。
24. <strong>内容过滤错误体结构有变</strong>：Chat Completions 错误使用 `error.body["innererror"]["content_filter_result"]`（单数）。Responses API 错误使用 `error.body["content_filters"][0]["content_filter_results"]`（复数，并在数组内）。`innererror` 键已不存在。直接访问 `innererror` 的代码迁移时会在运行时触发 `KeyError` — 这很容易被忽视，因为只有当内容过滤真正触发时才会出现。迁移时务必 grep 查找 `innererror`。
25. **原始 HTTP 调用需改写 URL + 请求体**：直接调用 Azure OpenAI REST（通过 `requests`、`httpx`、`aiohttp`）且使用 `/openai/deployments/{name}/chat/completions?api-version=...` 的应用，必须切换至 `/openai/v1/responses`。请求体使用 `input` 替代 `messages`，且需要 `max_output_tokens` 和 `store`，并且移除 `api-version` 查询参数。响应体文本位于 `output[0].content[0].text` — <strong>不是</strong> `output_text`，后者是 SDK 的便利属性，不存在于原始 REST JSON 中。

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免责声明**：
本文件由 AI 翻译服务 [Co-op Translator](https://github.com/Azure/co-op-translator) 翻译完成。尽管我们力求准确，但请注意，自动翻译可能包含错误或不准确之处。原始语言版文件应视为权威来源。对于重要信息，建议使用专业人工翻译。我们对因使用本翻译而产生的任何误解或误释不承担责任。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->