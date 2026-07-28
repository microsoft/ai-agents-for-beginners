---
name: azure-openai-to-responses
license: MIT
---
# 将 Python 应用从 Azure OpenAI 聊天补全迁移到 Responses API

> **权威指南 — 请严格遵循**
>
> 该技能将使用 Azure OpenAI 聊天补全的 Python 代码库
> 迁移到统一的 Responses API。请严格遵循这些说明。
> 不要即兴映射参数或发明 API 形态。

---

## 触发条件

当用户希望时启用此技能：
- 将 Python 应用从 Azure OpenAI 聊天补全迁移到 Responses API
- 升级 Python OpenAI SDK 的用法至针对 Azure OpenAI 的最新 API 形态
- 为需要 Azure 上 Responses 的 GPT-5 或更新模型准备 Python 代码
- 从 `AzureOpenAI`/`AsyncAzureOpenAI` 切换到带 v1 端点的标准 `OpenAI`/`AsyncOpenAI` 客户端
- 修复与 `AzureOpenAI` 构造函数或 `api_version` 相关的弃用警告

---

## ⚠️ 模型兼容性 — 先检查

> **迁移前，请验证您的 Azure OpenAI 部署支持 Responses API。**

### 1. 快速测试您的部署（最快）

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

> <strong>注意</strong>：在 Azure OpenAI 上，`max_output_tokens` 最小为 **16**。低于 16 会返回 400 错误。用于快速测试时请使用 50 以上。

如果返回 404，该部署的模型尚不支持 Responses — 请检查下面的参考资料或使用支持的模型重新部署。

### 2. 查看您所在区域可用模型（推荐）

运行内置的模型兼容性工具，查看在您所在的具体区域中支持 Responses API 的可用模型：

```bash
python migrate.py models --subscription YOUR_SUB_ID --location YOUR_REGION
```

该命令查询 Azure ARM 实时数据并显示兼容性矩阵——哪些模型支持 Responses、结构化输出、工具等。用 `--filter gpt-5.1,gpt-5.2` 缩小结果范围或用 `--json` 用于脚本处理。

### 3. 完整的模型支持参考

- <strong>实时查询</strong>：`python migrate.py models`（见上文——特定区域，始终最新）
- <strong>可用浏览</strong>：[模型汇总表及区域可用性](https://learn.microsoft.com/en-us/azure/foundry/foundry-models/concepts/models-sold-directly-by-azure?tabs=global-standard-aoai%2Cglobal-standard&pivots=azure-openai#model-summary-table-and-region-availability)
- <strong>快速入门和指南</strong>：**https://aka.ms/openai/start**

### ⚠️ 较旧模型的限制

> <strong>警告</strong>：较旧模型（`gpt-4.1` 之前的）可能不完全支持所有 Responses API 功能。
>
> 已知的旧模型限制：
> - **`reasoning` 参数**：许多非推理模型不支持。仅当原代码已经存在 `reasoning` 时才迁移。
> - **`seed` 参数**：Responses API 完全不支持，需从所有请求中移除。
> - **通过 `text.format` 实现的结构化输出**：旧模型可能无法可靠强制执行 `strict: true` 的 JSON schema。
> - <strong>工具编排</strong>：GPT-5+ 作为内部推理部分协调工具调用。旧模型使用 Responses 仍能工作，但缺少深度集成。
> - <strong>温度限制</strong>：迁移到 `gpt-5` 时必须省略温度或设置为 `1`。旧模型没有此类限制。

### O 系推理模型（o1、o3-mini、o3、o4-mini）

O 系模型有独特的参数限制。迁移目标为 o 系模型的应用时：

- **`temperature`**：必须为 `1`（或省略）。O 系模型不接受其他值。
- **`max_completion_tokens` → `max_output_tokens`**：使用 Azure 专有的 `max_completion_tokens` 的应用必须切换到 `max_output_tokens`。设置较高值（4096+），因为推理用的标记计入限制。
- **`reasoning_effort`**：如果应用使用 `reasoning_effort`（低/中/高），请保留—Responses API 支持此参数用于 o 系模型。
- <strong>流式行为</strong>：O 系模型可能在推理完成前缓冲输出，然后再发出文本增量事件。流式仍然可用，但首个 `response.output_text.delta` 可能比 GPT 模型延迟更长。
- **`top_p`**：O 系不支持，存在则移除。
- <strong>工具使用</strong>：O 系模型通过 Responses API 支持工具，类似 GPT 模型，但工具调用编排质量依模型而异。

**措施 — 主动模型建议**：扫描阶段检查应用目标模型（部署名、环境变量、配置）。如果模型早于 `gpt-4.1`（不是 gpt-4.1+），主动告知用户：
- 当前模型下迁移支持基础文本、聊天、流式和工具。
- 新模型（`gpt-5.1`、`gpt-5.2`）在工具编排、结构化输出强制、推理和跨区域可用性方面表现更好。
- 用户应考虑在适当时升级部署 — 这不影响迁移本身。

不因模型版本阻止或拒绝迁移。该建议为信息性质。

### GitHub 模型不支持 Responses API

> **GitHub 模型（`models.github.ai`、`models.inference.ai.azure.com`）不支持 Responses API。**

如果代码库有 GitHub 模型的代码路径（检查 `base_url` 是否指向 `models.github.ai` 或 `models.inference.ai.azure.com`），<strong>迁移时请完全移除</strong>。Responses API 需要 Azure OpenAI、OpenAI 或兼容的本地端点（如支持 Responses 的 Ollama）。

扫描阶段操作：
- 标记所有 GitHub 模型代码路径以备删除。

---

## 框架迁移

许多应用使用 OpenAI 之上的高级框架。迁移它们时，需变更框架自身 API，而非仅底层 OpenAI 调用。

### Microsoft 代理框架 (MAF)

**先检查您的 MAF 版本** — 迁移依赖于您使用的是 MAF 1.0.0+ 还是 1.0.0 前的 beta/rc 版本。

#### MAF 1.0.0+ (agent-framework-openai >= 1.0.0)

`OpenAIChatClient` **已经使用 Responses API** — 无需迁移。如果代码库使用旧版 `OpenAIChatCompletionClient`（调用 `chat.completions.create`），请替换为 `OpenAIChatClient`。

| 之前 | 之后 |
|--------|-------|
| `from agent_framework.openai import OpenAIChatCompletionClient` | `from agent_framework.openai import OpenAIChatClient` |
| `OpenAIChatCompletionClient(...)` | `OpenAIChatClient(...)` |

查看版本：`python -c "import agent_framework_openai; print(agent_framework_openai.__version__)"`

#### MAF 1.0.0 前版本 (beta/rc 发布)

在 MAF 1.0.0 前，`OpenAIChatClient` 使用聊天补全。升级至 `agent-framework-openai>=1.0.0`，默认使用 Responses API。

其他接口不变 — `Agent` 和工具 API 保持一样。

### LangChain (`langchain-openai`)

在 `ChatOpenAI()` 中添加 `use_responses_api=True`。并将响应访问由 `.content` 改为 `.text`。

| 之前 | 之后 |
|--------|-------|
| `ChatOpenAI(model=..., base_url=..., api_key=...)` | `ChatOpenAI(model=..., base_url=..., api_key=..., use_responses_api=True)` |
| `result['messages'][-1].content` | `result['messages'][-1].text` |

详细的前后代码示例，参见 [cheat-sheet.md](./references/cheat-sheet.md)。

---

## 前端迁移指导

> **Responses API 是服务器端的 concern。** 迁移您的 Python 后端；前端的 HTTP 协议不应更改，除非后端仅是薄代理——在此情况下，考虑采用 Responses 请求形态以消除翻译层。如果前端使用客户端密钥直接调用 OpenAI，请先将这类调用移至后端。

### `@microsoft/ai-chat-protocol` 弃用

`@microsoft/ai-chat-protocol` npm 包已弃用，应替换为 [`ndjson-readablestream`](https://www.npmjs.com/package/ndjson-readablestream)。如在前端遇到：

1. 替换 CDN 脚本标签：
   ```html
   <!-- Before -->
   <script src="https://cdn.jsdelivr.net/npm/@microsoft/ai-chat-protocol@.../dist/iife/index.js"></script>
   <!-- After -->
   <script src="https://cdn.jsdelivr.net/npm/ndjson-readablestream@1.0.7/dist/ndjson-readablestream.umd.js"></script>
   ```
2. 移除 `AIChatProtocolClient` 实例化（`new ChatProtocol.AIChatProtocolClient("/chat")`）。
3. 将 `client.getStreamedCompletion(messages)` 替换为对后端流式端点的直接 `fetch()` 调用。
4. 将 `for await (const response of result)` 替换为 `for await (const chunk of readNDJSONStream(response.body))`。
5. 更新属性访问，由 `response.delta.content` / `response.error` 改为 `chunk.delta.content` / `chunk.error`。

---

## 目标

- 枚举所有使用 Chat Completions 或旧版 Completions 调用 Azure OpenAI 的 Python 代码位置。
- 提出 Python 代码库的迁移方案与步骤。
- 应用安全且最小化的编辑切换至 Responses API。
- 更新调用者以消费 Responses 输出模式；不使用向后兼容封装。
- 执行测试/静态检查；修复迁移带来的轻微破坏。
- 准备小型、易复审的变更集并提供最终带差异摘要（不提交）。

---

## 保护措施

- 仅修改 git 工作区内的文件，绝不向外写文件。
- 不保留向后兼容 shim；将代码迁移至新 API 形态。
- 不留墓碑/过渡注释或备份文件。
- 如先前使用流式，请保留流式语义；否则使用非流式。
- 审批模式下运行命令或网络请求前请求批准。
- 不运行 `git add`/`git commit`/`git push`；仅生成工作区编辑。

---

## 步骤 0：Azure OpenAI 客户端迁移（前提）

如果代码库使用 `AzureOpenAI` 或 `AsyncAzureOpenAI` 构造函数，先迁移到标准 `OpenAI` / `AsyncOpenAI` 构造函数。Azure 专用构造函数在 `openai>=1.108.1` 中已弃用。

### 为什么使用 v1 API 路径？

新的 `/openai/v1` 端点使用标准的 `OpenAI()` 客户端替代 `AzureOpenAI()`，无须 `api_version` 参数，且在 OpenAI 和 Azure OpenAI 上表现一致。相同客户端代码具备未来兼容性，无需版本管理。

### 关键变更

| 之前 | 之后 |
|--------|-------|
| `AzureOpenAI` | `OpenAI` |
| `AsyncAzureOpenAI` | `AsyncOpenAI` |
| `azure_endpoint` | `base_url` |
| `azure_ad_token_provider` | `api_key` |
| `api_version=...` | 完全移除 |

### 清理检查项

- 从客户端构造中移除 `api_version` 参数。
- 从 `.env`、应用设置和 Bicep/基础设施文件中移除 `AZURE_OPENAI_VERSION` / `AZURE_OPENAI_API_VERSION` 环境变量。
- 将 `.env`、应用设置、Bicep/基础设施及测试夹具中的 `AZURE_OPENAI_CLIENT_ID` 重命名为 `AZURE_CLIENT_ID`（遵守 Azure Identity SDK 标准惯例）。
- 确保 `requirements.txt` 或 `pyproject.toml` 中使用 `openai>=1.108.1`。

### 环境变量迁移

| 旧环境变量 | 操作 | 备注 |
|-------------|--------|-------|
| `AZURE_OPENAI_VERSION` | <strong>移除</strong> | v1 端点无需 `api_version` |
| `AZURE_OPENAI_API_VERSION` | <strong>移除</strong> | 同上 |
| `AZURE_OPENAI_CLIENT_ID` | <strong>重命名</strong> → `AZURE_CLIENT_ID` | Azure Identity SDK 标准，用于 `ManagedIdentityCredential(client_id=...)` |
| `AZURE_OPENAI_ENDPOINT` | <strong>保留</strong> | 仍用于构造 `base_url` |
| `AZURE_OPENAI_CHAT_DEPLOYMENT` | <strong>保留</strong> | 用作 `responses.create` 的 `model` 参数 |
| `AZURE_OPENAI_API_KEY` | <strong>保留</strong> | 用作基于密钥认证的 `api_key` |

客户端设置代码示例（同步、异步、EntraID、API 密钥、多租户）见 [cheat-sheet.md](./references/cheat-sheet.md)。

---

## 步骤 1：检测旧版调用点

运行 [detect_legacy.py](../../../../../.agents/skills/azure-openai-to-responses/scripts/detect_legacy.py) 脚本查找所有需迁移的调用点：

```bash
python skills/azure-openai-to-responses/scripts/detect_legacy.py .
```

或手动搜索——每个匹配都是迁移目标：

```bash
# 旧版API调用（必须重写）
rg "chat\.completions\.create"
rg "ChatCompletion\.create"
rg "Completion\.create"

# 已弃用的Azure客户端构造函数（必须替换）
rg "AzureOpenAI\("
rg "AsyncAzureOpenAI\("

# 响应结构访问模式（必须更新）
rg "choices\[0\]\.message\.content"
rg "choices\[0\]\.delta\.content"
rg "choices\[0\]\.message\.function_call"
rg "choices\[0\]\.message\.tool_calls"

# 旧嵌套格式的工具定义（必须扁平化）
rg '"function":\s*{\s*"name"'
rg "pydantic_function_tool"

# 旧格式的工具结果（必须转换为function_call_output）
rg '"role":\s*"tool"'
rg '"tool_call_id"'

# 已弃用的参数（必须删除或重命名）
rg "response_format"
rg "max_tokens\b"        # 重命名为max_output_tokens
rg "['\"]seed['\"]"      # remove entirely

# 已弃用的环境变量（清理）
rg "AZURE_OPENAI_API_VERSION|AZURE_OPENAI_VERSION"
rg "AZURE_OPENAI_CLIENT_ID"  # 应为AZURE_CLIENT_ID

# GitHub模型端点（必须删除 — 不支持Responses API）
rg "models\.github\.ai|models\.inference\.ai\.azure"

# 框架级旧模式（必须更新）
rg "OpenAIChatCompletionClient"  # MAF 1.0.0+：替换为OpenAIChatClient
rg "ChatOpenAI\(" | grep -v "use_responses_api"  # LangChain：需要use_responses_api=True

# 测试基础设施（必须更新）
rg "ChatCompletionChunk|AsyncCompletions\.create" tests/
rg "_azure_ad_token_provider" tests/
rg "prompt_filter_results|content_filter_results" tests/
rg "choices\[0\]" tests/

# 内容过滤器错误体访问（必须更新 — 结构已更改）
rg 'innererror.*content_filter_result|error\.body\["innererror"\]'
rg "content_filter_result\[" # 旧的单数形式 — 现在是content_filters数组内的content_filter_results（复数）

# 直接调用Chat Completions端点的原始HTTP请求（必须更新URL）
rg "/openai/deployments/.*/chat/completions"
rg "api-version="
```

### 规则（检测与重写）

- <strong>聊天补全客户端</strong>：`client.chat.completions.create` → `client.responses.create(...)`。

- **Azure 客户端构造函数**：`AzureOpenAI(...)` → `OpenAI(base_url=..., api_key=...)`。
- <strong>工具</strong>：将函数调用工具定义从嵌套格式（`{"type": "function", "function": {"name": ...}}`）转换为扁平的 Responses 格式（`{"type": "function", "name": ...}`）；使用 `tool_choice`；返回工具结果作为 `{"type": "function_call_output", "call_id": ..., "output": ...}` 项（而非 `{"role": "tool", ...}`）。
- <strong>工具往返</strong>：当模型返回函数调用时，将 `response.output` 项追加到对话中（而不是手动添加 `{"role": "assistant", "tool_calls": [...]}` 字典），然后为每个结果追加 `function_call_output` 项。
- <strong>少样本工具示例</strong>：如果对话中包含硬编码的工具调用示例，转换为 `{"type": "function_call", "id": "fc_...", "call_id": "fc_...", ...}` + `{"type": "function_call_output", ...}` 项。ID 必须以 `fc_` 开头。
- **`pydantic_function_tool()`<strong>：此辅助仍生成旧的嵌套格式，</strong>不兼容** `responses.create()`。请替换为手动工具定义或扁平化包装器。
- <strong>多轮</strong>：在应用中维护对话历史；通过 `input` 项传递之前的轮次。
- <strong>格式化</strong>：将 Chat 的顶层 `response_format` 替换为 Responses 的 `text.format`。规范形态：`text={"format": {"type": "json_schema", "name": "Output", "strict": True, "schema": {...}}}`。
- <strong>内容项</strong>：将 Chat 的 `content[].type: "text"` 替换为 Responses 的 `content[].type: "input_text"`，适用于用户/系统回合。
- <strong>图片内容项</strong>：将 Chat 的 `content[].type: "image_url"` 替换为 Responses 的 `content[].type: "input_image"`。`image_url` 字段由嵌套对象 `{"url": "..."}` 变为扁平字符串。详见备忘清单的前后示例。
- <strong>推理工作</strong>：**仅在原始代码中已存在 `reasoning` 时迁移**。
- <strong>内容过滤错误处理</strong>：错误体结构变化。Chat Completion 使用 `error.body["innererror"]["content_filter_result"]`（单数）；Responses API 使用 `error.body["content_filters"][0]["content_filter_results"]`（复数，数组内）。访问 `innererror` 的代码将引发 `KeyError`，需重写为新路径。
- **原始 HTTP 调用**：如果应用直接调用 Azure OpenAI REST API（通过 `requests`、`httpx` 等）使用 `/openai/deployments/{name}/chat/completions?api-version=...`，需重写为 `/openai/v1/responses`。请求体变化：`messages` → `input`，新增 `max_output_tokens` 和 `store: false`，移除 `api-version` 查询参数。响应体变化：`choices[0].message.content` → `output[0].content[0].text`（注意：`output_text` 是 SDK 便捷属性，原始 REST JSON 无）。

---

## 步骤 2：应用迁移

### 迁移说明（Chat Completions → Responses）

- <strong>为何迁移</strong>：Responses 是文本、工具和流式的统一接口；Chat Completions 属于遗留接口。使用 GPT-5 时，必须使用 Responses 以获得最佳性能。
- **HTTP**：Azure 端点从 `/openai/deployments/{name}/chat/completions` 变更为 `/openai/v1/responses`。
- <strong>字段</strong>：`messages` → `input`，`max_tokens` → `max_output_tokens`。`temperature` 不变。
- <strong>格式化</strong>：`response_format` → `text.format`（对象）。
- <strong>内容项</strong>：将 Chat 的 `content[].type: "text"` 替换为 Responses 的 `content[].type: "input_text"`，适用于系统/用户回合。
- <strong>图片内容项</strong>：将 Chat 的 `content[].type: "image_url"` 替换为 Responses 的 `content[].type: "input_image"`。`image_url` 字段由 `{"image_url": {"url": "..."}}` 扁平为 `{"image_url": "..."}`（纯字符串，https URL 或 `data:image/...;base64,...` 数据 URI）。

### 参数映射参考

| Chat Completions | Responses API |
|-----------------|---------------|
| `prompt` | `input` |
| `messages` | `input`（项数组） |
| `max_tokens` | `max_output_tokens` |
| `response_format` | `text.format`（对象） |
| `temperature` | `temperature`（不变） |
| `stop` | `stop`（不变） |
| `frequency_penalty` | `frequency_penalty`（不变） |
| `presence_penalty` | `presence_penalty`（不变） |
| `tools` / 函数调用 | `tools`（不变） |
| `seed` | <strong>移除</strong>（不支持） |
| `store` | `store`（设为 `false`） |
| `content[].type: "text"` | `content[].type: "input_text"` |
| `content[].type: "image_url"` | `content[].type: "input_image"` |
| `"image_url": {"url": "..."}` | `"image_url": "..."`（扁平字符串） |

完整的前后代码示例见 [cheat-sheet.md](./references/cheat-sheet.md)。

测试基础设施迁移（模拟、快照、断言）见 [test-migration.md](./references/test-migration.md)。

错误排查及注意事项见 [troubleshooting.md](./references/troubleshooting.md)。

---

## 数据保留与状态

- 对所有 Responses 请求设置 `store: false`。
- 不依赖先前消息 ID 或服务器存储的上下文；保持状态由客户端管理，且最小化元数据。

---

## 验收标准

### 代码级门控（全部通过）

- [ ] 已迁移文件中无 `rg "chat\.completions\.create|ChatCompletion\.create|Completion\.create"` 命中。
- [ ] 已迁移代码中无 `rg "AzureOpenAI\(|AsyncAzureOpenAI\("`，全部构造函数使用基于 v1 端点的 `OpenAI`/`AsyncOpenAI`。
- [ ] 已迁移代码中无 `rg "models\.github\.ai|models\.inference\.ai\.azure"`，GitHub 模型代码路径已移除。
- [ ] 已迁移代码中无 `rg "OpenAIChatCompletionClient"`，MAF 1.0.0+ 使用 `OpenAIChatClient`（采用 Responses API）。1.0.0 以前版本升级至 `agent-framework-openai>=1.0.0`。
- [ ] 所有 `ChatOpenAI(...)` 调用包含 `use_responses_api=True`。
- [ ] 无 `rg "choices\[0\]"` 命中，所有响应访问使用 `resp.output_text` 或 Responses 输出结构。
- [ ] 顶层没有 `response_format`，所有结构化输出使用 `text={"format": {...}}`。
- [ ] `requirements.txt` 或 `pyproject.toml` 中包含 `openai>=1.108.1` 和 `azure-identity`，依赖已重新安装。
- [ ] 所有 `responses.create` 调用设置了 `store=False`。
- [ ] 客户端构造无 `api_version`，环境文件和基础设施移除了 `AZURE_OPENAI_API_VERSION`。

### 测试基础设施门控（全部通过）

- [ ] 测试文件中无 `rg "ChatCompletionChunk|AsyncCompletions\.create|chat\.completions"` 命中。
- [ ] 测试文件中无 `rg "_azure_ad_token_provider"` 命中，断言更新为检查 `isinstance(client, AsyncOpenAI)` 或者 `base_url`。
- [ ] 测试文件中无 `rg "prompt_filter_results|content_filter_results"` 命中，移除 Azure 特定过滤模拟。
- [ ] 模拟夹具使用 `kwargs.get("input")` 替代 `kwargs.get("messages")`。
- [ ] 快照/黄金文件更新为 Responses 流式形态（无 `choices[0]`、`function_call`、`logprobs` 等）。
- [ ] 执行 `pytest` 后零失败。

### 行为门控（手动或测试框架验证）

- [ ] <strong>基础完成</strong>：非流式 `responses.create` 返回非空 `output_text`。
- [ ] <strong>流式一致性</strong>：若原代码使用流式，迁移代码流式返回且产出 `response.output_text.delta` 事件，且 delta 非空。
- [ ] <strong>结构化输出</strong>：若使用 `text.format` 的 `json_schema`，`json.loads(resp.output_text)` 成功且符合模式。
- [ ] <strong>工具调用循环</strong>：如果使用工具，模型发起工具调用，应用执行，后续请求返回最终 `output_text`（无无限循环）。
- [ ] <strong>异步一致性</strong>：若使用过 `AsyncAzureOpenAI`，则等效的 `AsyncOpenAI` 可正常使用 `await`。
- [ ] <strong>错误率</strong>：与迁移前基线比较，无新增 400/401/404 错误。

### 交付物

- 总结包括已编辑文件、老旧调用点的转换前后计数、以及后续步骤。
- 变更为工作区未提交编辑（无提交）。

---

## SDK 版本要求

| 包名 | 最低版本 |
|---------|----------------|
| `openai` | `>=1.108.1` |
| `azure-identity` | 最新版（用于 EntraID 认证） |

---

## 参考资料

- [备忘清单 — 所有代码片段](./references/cheat-sheet.md)
- [测试迁移 — 模拟、快照、断言](./references/test-migration.md)
- [故障排查 — 错误、风险表、注意事项](./references/troubleshooting.md)
- [detect_legacy.py — 自动扫描器](../../../../../.agents/skills/azure-openai-to-responses/scripts/detect_legacy.py)
- [Azure OpenAI 入门包](https://aka.ms/openai/start)
- [Azure OpenAI Responses API 文档](https://learn.microsoft.com/en-us/azure/ai-foundry/openai/how-to/responses)
- [Azure OpenAI API 版本生命周期](https://learn.microsoft.com/en-us/azure/ai-foundry/openai/api-version-lifecycle?view=foundry-classic&tabs=python#api-evolution)
- [OpenAI Responses API 参考](https://platform.openai.com/docs/api-reference/responses)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免责声明**：
本文件由 AI 翻译服务 [Co-op Translator](https://github.com/Azure/co-op-translator) 翻译完成。尽管我们力求准确，但请注意，自动翻译可能包含错误或不准确之处。原始语言版文件应视为权威来源。对于重要信息，建议使用专业人工翻译。我们对因使用本翻译而产生的任何误解或误释不承担责任。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->