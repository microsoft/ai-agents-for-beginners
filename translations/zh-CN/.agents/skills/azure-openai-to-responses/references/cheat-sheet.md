# Responses API 备忘单（Python + Azure OpenAI）

> 以下所有代码片段均假设 `deployment = os.environ["AZURE_OPENAI_DEPLOYMENT"]` 且 `client` 已初始化（参见客户端设置）。

## 基本请求
```python
resp = client.responses.create(
    model=deployment,
    input="Hello",
    max_output_tokens=1000,
    store=False,
)
print(resp.output_text)
```

## 客户端设置 — EntraID（推荐）
```python
import os
from azure.identity import DefaultAzureCredential, get_bearer_token_provider
from openai import OpenAI

token_provider = get_bearer_token_provider(
    DefaultAzureCredential(),
    "https://cognitiveservices.azure.com/.default"
)

client = OpenAI(
    base_url=f"{os.environ['AZURE_OPENAI_ENDPOINT'].rstrip('/')}/openai/v1/",
    api_key=token_provider,
)
```

## 客户端设置 — API 密钥
```python
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ["AZURE_OPENAI_API_KEY"],
    base_url=f"{os.environ['AZURE_OPENAI_ENDPOINT'].rstrip('/')}/openai/v1/",
)
```

## 异步客户端设置 — EntraID
```python
import os
from azure.identity import DefaultAzureCredential, get_bearer_token_provider
from openai import AsyncOpenAI

token_provider = get_bearer_token_provider(
    DefaultAzureCredential(),
    "https://cognitiveservices.azure.com/.default"
)

client = AsyncOpenAI(
    base_url=f"{os.environ['AZURE_OPENAI_ENDPOINT'].rstrip('/')}/openai/v1/",
    api_key=token_provider,
)
```

## 异步客户端设置 — 带显式租户的 EntraID（多租户）

当 Azure OpenAI 资源所属的租户与默认租户不同，需显式传入 `tenant_id` 给凭据。这在开发/测试场景中很常见，开发者的主租户与资源租户不同。

```python
import os
from azure.identity.aio import (
    AzureDeveloperCliCredential,
    ChainedTokenCredential,
    ManagedIdentityCredential,
    get_bearer_token_provider,
)
from openai import AsyncOpenAI

# 用于生产环境的托管身份凭据（Azure 容器应用、应用服务等）
managed_identity_cred = ManagedIdentityCredential(
    client_id=os.getenv("AZURE_CLIENT_ID")  # 用户分配的托管身份
)
# 本地开发的 AzureDeveloperCliCredential — 明确的 tenant_id 至关重要
azd_cred = AzureDeveloperCliCredential(
    tenant_id=os.getenv("AZURE_TENANT_ID"),
    process_timeout=60,
)
# 链式认证：先尝试托管身份，失败后回退到 azd CLI
azure_credential = ChainedTokenCredential(managed_identity_cred, azd_cred)

token_provider = get_bearer_token_provider(
    azure_credential, "https://cognitiveservices.azure.com/.default"
)

client = AsyncOpenAI(
    base_url=f"{os.environ['AZURE_OPENAI_ENDPOINT'].rstrip('/')}/openai/v1/",
    api_key=token_provider,
)
```

## 异步客户端迁移 — 迁移前/迁移后

迁移前（已弃用）：
```python
from openai import AsyncAzureOpenAI

client = AsyncAzureOpenAI(
    api_version=os.environ["AZURE_OPENAI_API_VERSION"],
    azure_endpoint=os.environ["AZURE_OPENAI_ENDPOINT"],
    azure_ad_token_provider=token_provider,
)

resp = await client.chat.completions.create(
    model="gpt-4.1",
    messages=[{"role": "user", "content": "Hello"}],
    max_tokens=500,
)
print(resp.choices[0].message.content)
```

迁移后：
```python
from openai import AsyncOpenAI

deployment = os.environ["AZURE_OPENAI_DEPLOYMENT"]

client = AsyncOpenAI(
    base_url=f"{os.environ['AZURE_OPENAI_ENDPOINT'].rstrip('/')}/openai/v1/",
    api_key=token_provider,
)

resp = await client.responses.create(
    model=deployment,
    input="Hello",
    max_output_tokens=1000,
    store=False,
)
print(resp.output_text)
```

## 完整同步迁移 — 迁移前/迁移后

迁移前（传统 — Azure OpenAI 聊天补全）：
```python
from openai import AzureOpenAI
import os

client = AzureOpenAI(
    api_version=os.environ["AZURE_OPENAI_API_VERSION"],
    azure_endpoint=os.environ["AZURE_OPENAI_ENDPOINT"],
    api_key=os.environ["AZURE_OPENAI_API_KEY"],
)

resp = client.chat.completions.create(
    model="gpt-4.1",
    messages=[{"role": "user", "content": "Hello"}],
    max_tokens=500,
)
print(resp.choices[0].message.content)
```

迁移后（Responses API — Azure OpenAI v1 端点）：
```python
from openai import OpenAI
import os

deployment = os.environ["AZURE_OPENAI_DEPLOYMENT"]

client = OpenAI(
    api_key=os.environ["AZURE_OPENAI_API_KEY"],
    base_url=f"{os.environ['AZURE_OPENAI_ENDPOINT'].rstrip('/')}/openai/v1/",
)

resp = client.responses.create(
    model=deployment,
    input="Hello",
    max_output_tokens=1000,
    store=False,
)
print(resp.output_text)
```

## 流式（同步）
```python
stream = client.responses.create(
    model=deployment,
    input="Explain streaming in simple terms",
    max_output_tokens=1000,
    stream=True,
)
for event in stream:
    if event.type == "response.output_text.delta":
        print(event.delta, end="", flush=True)
    elif event.type == "response.completed":
        print()  # 行尾换行
```

## 流式（异步）
```python
stream = await client.responses.create(
    model=deployment,
    input="Explain streaming in simple terms",
    max_output_tokens=1000,
    stream=True,
)
async for event in stream:
    if event.type == "response.output_text.delta":
        print(event.delta, end="", flush=True)
    elif event.type == "response.completed":
        print()
```

## Web 应用流式 — 后端到前端的数据格式

当迁移一个向前端流式 SSE/JSONL 的 Web 应用时，<strong>后端序列化格式</strong> 会发生变化。设计新的后端输出要保持前端现有的访问模式，这样前端无需做任何改动。

<strong>迁移前</strong> — 聊天补全后端通常序列化每个 chunk 的 `choices[0]` 字典：
```python
# 旧的：每块序列化的完整选择字典
async for chunk in response:
    if chunk.choices:
        yield json.dumps(chunk.choices[0].model_dump()) + "\n"
```
前端读取：`response.delta.content`（深入访问 choice 对象路径）。

<strong>迁移后</strong> — Responses API 后端发出最小形态，同时保持相同的前端访问路径：
```python
# 新：只发送前端需要的内容
async for event in await chat_coroutine:
    if event.type == "response.output_text.delta":
        yield json.dumps({"delta": {"content": event.delta}}) + "\n"
    elif event.type == "response.completed":
        yield json.dumps({"delta": {"content": None}, "finish_reason": "stop"}) + "\n"
```
前端仍然读取 `response.delta.content` — <strong>前端无需更改</strong>。

> <strong>关键见解</strong>：Responses API 的流式形态（`event.type` + `event.delta`）与聊天补全（`chunk.choices[0].delta.content`）本质不同。但后端到前端的协议由你定义。设计后端输出以匹配前端已有预期。

## 流式事件顺序

当 `stream: true`，API 会按顺序发送事件：
1. `response.created` – 响应对象初始化
2. `response.in_progress` – 开始生成
3. `response.output_item.added` – 输出项创建
4. `response.content_part.added` – 内容部分开始
5. `response.output_text.delta` – 文本块（多个，每个含 `delta: string`）
6. `response.output_text.done` – 文本生成完成
7. `response.content_part.done` – 内容部分完成
8. `response.output_item.done` – 输出项完成
9. `response.completed` – 完整响应完成

对于基本文本流式处理，仅处理 `response.output_text.delta`（文本块）和 `response.completed`（结束）。

## Web 应用中的流式错误处理

在 Web 应用流式时，使用 `try/except` 包装异步迭代，将错误作为 JSON 产出，方便前端优雅显示错误（如限流、临时故障）：

```python
@stream_with_context
async def response_stream():
    chat_coroutine = client.responses.create(
        model=deployment,
        input=all_messages,
        max_output_tokens=1000,
        stream=True,
        store=False,
    )
    try:
        async for event in await chat_coroutine:
            if event.type == "response.output_text.delta":
                yield json.dumps({"delta": {"content": event.delta}}) + "\n"
            elif event.type == "response.completed":
                yield json.dumps({"delta": {"content": None}, "finish_reason": "stop"}) + "\n"
    except Exception as e:
        current_app.logger.error(e)
        yield json.dumps({"error": str(e)}) + "\n"
```


> <strong>为什么这很重要</strong>：Azure OpenAI 在速率限制期间会返回 `429 Too Many Requests`。没有 `try/except`，流式响应会静默失败。有了它，前端会接收到 `{"error": "Too Many Requests"}` 并可以显示重试提示。

## 流式事件类型（Python SDK）

- `ResponseTextDeltaEvent`：`type='response.output_text.delta'`，`delta: str`
- `ResponseCompletedEvent`：`type='response.completed'`，`response: Response`

## 会话格式
```python
# Responses API 支持通过输入数组的对话格式
response = client.responses.create(
    model=deployment,
    input=[
        {"role": "system", "content": "You are an Azure cloud architect."},
        {"role": "user", "content": "Design a scalable web application architecture."},
    ],
    max_output_tokens=1000,
)
print(response.output_text)
```

## 内容过滤错误处理

错误体结构已从 Chat Completions 改变为 Responses API。

之前（Chat Completions）：
```python
except openai.APIError as error:
    if error.code == "content_filter":
        if error.body["innererror"]["content_filter_result"]["jailbreak"]["filtered"] is True:
            print("Jailbreak detected!")
```

之后（Responses API）：
```python
except openai.APIError as error:
    if error.code == "content_filter":
        if error.body["content_filters"][0]["content_filter_results"]["jailbreak"]["filtered"] is True:
            print("Jailbreak detected!")
```

关键区别：
- `innererror` 包装已<strong>消失</strong> — 内容过滤详细信息现在位于 `error.body` 的顶层。
- `content_filter_result`（单数）→ `content_filters`（复数数组）包含每个条目中的 `content_filter_results`（复数）。
- `content_filters` 中的每个条目都包括 `blocked`，`source_type` 和带有按类别详情的 `content_filter_results`（`jailbreak`，`hate`，`sexual`，`violence`，`self_harm`）。

完整的 Responses API 内容过滤错误体形态：
```json
{
  "message": "The response was filtered...",
  "type": "invalid_request_error",
  "param": "prompt",
  "code": "content_filter",
  "content_filters": [
    {
      "blocked": true,
      "source_type": "prompt",
      "content_filter_results": {
        "jailbreak": { "detected": true, "filtered": true },
        "hate": { "filtered": false, "severity": "safe" },
        "sexual": { "filtered": false, "severity": "safe" },
        "violence": { "filtered": false, "severity": "safe" },
        "self_harm": { "filtered": false, "severity": "safe" }
      }
    }
  ]
}
```

## 原始 HTTP 迁移（requests/httpx）

如果应用直接调用 Azure OpenAI REST 而非使用 SDK：

之前（Chat Completions）：
```python
endpoint = f"{azure_endpoint}/openai/deployments/{deployment}/chat/completions?api-version=2024-03-01-preview"
data = {
    "messages": [{"role": "user", "content": query}],
    "model": model_name,
    "temperature": 0,
}
response = requests.post(endpoint, headers=headers, json=data)
message = response.json()["choices"][0]["message"]["content"]
```

之后（Responses API）：
```python
endpoint = f"{azure_endpoint}/openai/v1/responses"
data = {
    "model": deployment,
    "input": [{"role": "user", "content": query}],
    "temperature": 0,
    "max_output_tokens": 1000,
    "store": False,
}
response = requests.post(endpoint, headers=headers, json=data)
output_text = response.json()["output"][0]["content"][0]["text"]
```

> <strong>注意</strong>：`output_text` 是 Python SDK `Response` 对象的一个方便属性。原始 REST JSON 响应没有顶层 `output_text` 字段 — 文本位于 `output[0].content[0].text`。

## 多轮会话
```python
# 使用Responses API构建对话
messages = [
    {"role": "system", "content": "You are a helpful coding assistant."},
    {"role": "user", "content": "Write a Python function to calculate factorial"},
]

response = client.responses.create(
    model=deployment,
    input=messages,
    max_output_tokens=400,
)

# 将助手的回复添加到对话中
messages.append({"role": "assistant", "content": response.output_text})

# 继续对话
messages.append({"role": "user", "content": "Now optimize it with memoization"})

response2 = client.responses.create(
    model=deployment,
    input=messages,
    max_output_tokens=400,
)
print(response2.output_text)
```

内容类型的多轮（显式 `input_text`/`output_text`）：
```python
messages = [
    {"role": "system", "content": [{"type": "input_text", "text": "You are helpful."}]},
    {"role": "user", "content": [{"type": "input_text", "text": "Hi"}]},
    {"role": "assistant", "content": [{"type": "output_text", "text": "Hello!"}]},
    {"role": "user", "content": [{"type": "input_text", "text": "Tell me a joke"}]},
]
resp = client.responses.create(model=deployment, input=messages, store=False)
```

### 通过 `previous_response_id` 的多轮（替代方案）

你可以不用自己管理会话数组，而是使用 `previous_response_id` 链接服务器端的响应。API 会存储每条响应并自动在前面加上之前的回合。



```python
# 第一次对话
response = client.responses.create(
    model=deployment,
    input=[{"role": "user", "content": "Write a Python function to calculate factorial"}],
)
print(response.output_text)

# 后续对话 — 只需传递新的用户消息 + 上一次的响应ID
response2 = client.responses.create(
    model=deployment,
    input=[{"role": "user", "content": "Now optimize it with memoization"}],
    previous_response_id=response.id,
)
print(response2.output_text)
```

**何时使用哪种方式：**

| 方式 | 优点 | 缺点 |
|---|---|---|
| `input` 数组（手动） | 对历史有完整控制；可以剪裁/总结；无需服务器端存储（`store=False`） | 代码更多；你要管理数组 |
| `previous_response_id` | 代码更简单；自动链接 | 需要 `store=True`（默认）；会话存储在服务器端；无法修改回合间历史 |

> **迁移提示：** 大多数 Chat Completions 应用已经管理自己的消息数组，转换为 `input` 数组是更直接的 1:1 迁移。对新代码或不需要操作会话历史的情况，使用 `previous_response_id`。

## O 系列推理模型（o1、o3-mini、o3、o4-mini）

O 系列模型迁移到 Responses API 时有独特的参数限制。

### O 系列参数映射

| Chat Completions（o 系列） | Responses API | 备注 |
|---|---|---|

| `max_completion_tokens` | `max_output_tokens` | 设置高值（4096+）—推理令牌计入限制 |
| `reasoning_effort` | `reasoning.effort` | 若存在，保持不变（low/medium/high） |
| `temperature` | 删除或设置为 `1` | O系列只接受 `1` |
| `top_p` | 删除 | O系列不支持 |
| `seed` | 删除 | Responses API 不支持 |

### O系列之前/之后

之前（使用 o 系列的聊天补全）：
```python
resp = client.chat.completions.create(
    model="o4-mini",
    messages=[{"role": "user", "content": "Solve this step by step: 2x + 5 = 13"}],
    max_completion_tokens=4096,
    reasoning_effort="medium",
)
print(resp.choices[0].message.content)
```

之后（Responses API）：
```python
resp = client.responses.create(
    model=deployment,
    input="Solve this step by step: 2x + 5 = 13",
    max_output_tokens=4096,
    reasoning={"effort": "medium"},
    store=False,
)
print(resp.output_text)
```

> <strong>注意</strong>：O 系列模型在推理时可能会缓冲输出，然后再发出文本增量。流式传输仍然有效，但首个 `response.output_text.delta` 事件可能会比 GPT 模型延迟更长时间到达。

## 访问推理令牌
```python
# 推理模型使用内部推理——你可以看到使用了多少推理标记
response = client.responses.create(
    model=deployment,
    input="Explain quantum computing in simple terms",
    max_output_tokens=1000,
)
print(response.output_text)
print(f"Status: {response.status}")
print(f"Reasoning tokens: {response.usage.output_tokens_details.reasoning_tokens}")
print(f"Output tokens: {response.usage.output_tokens}")
```

> <strong>重要</strong>：使用 `max_output_tokens=1000`（不是 50–200）以适应推理模型的内部推理过程。模型在生成最终输出前会内部使用推理令牌。

## 结构化输出 — JSON Schema
```python
resp = client.responses.create(
    model=deployment,
    input="What is the capital of France?",
    max_output_tokens=500,
    text={
        "format": {
            "type": "json_schema",
            "name": "Output",
            "strict": True,
            "schema": {
                "type": "object",
                "properties": {"answer": {"type": "string"}},
                "required": ["answer"],
                "additionalProperties": False,
            },
        }
    },
    store=False,
)
import json
data = json.loads(resp.output_text)
print(data["answer"])
```

## 工具使用

- 使用 **扁平 Responses API 格式** 在 `tools` 中定义函数 — 顶层包含 `name`、`description` 和 `parameters`（不嵌套在 `function` 下）。
- 当模型请求调用工具时，在你的应用中执行该工具，并在下一次请求的 `input` 内以 `function_call_output` 项包含该工具结果。
- 保持模式简洁；执行前验证输入。
- 使用 `strict: true` 时，所有属性必须列在 `required` 中，且必须设置 `additionalProperties: false`。

> **⚠️ `pydantic_function_tool()` 不兼容**：`openai.pydantic_function_tool()` 辅助工具仍然生成旧的聊天补全嵌套格式（`{"type": "function", "function": {"name": ...}}`）。请勿与 `responses.create()` 一起使用。请手动定义工具模式或编写包装器来扁平化输出。

### 工具定义格式

Responses API 使用 <strong>扁平</strong> 工具格式 — `name`、`description`、`parameters` 是顶层键（不嵌套在 `function` 下）。

**之前（聊天补全 — 嵌套格式）：**
```python
tools = [{"type": "function", "function": {"name": "lookup_weather", "parameters": {...}}}]
```

**之后（Responses API — 扁平格式）：**
```python
tools = [{"type": "function", "name": "lookup_weather", "parameters": {...}}]
```

完整示例：
```python
tools = [
    {
        "type": "function",
        "name": "lookup_weather",
        "description": "Lookup the weather for a given city name.",
        "parameters": {
            "type": "object",
            "properties": {
                "city_name": {"type": "string", "description": "The city name"},
            },
            "required": ["city_name"],
            "additionalProperties": False,
        },
    }
]

response = client.responses.create(
    model=deployment,
    input=[
        {"role": "system", "content": "You are a weather chatbot."},
        {"role": "user", "content": "What's the weather in Berkeley?"},
    ],
    tools=tools,
    tool_choice="auto",
    store=False,
)
```

使用 `strict: true`（模式强制）：
```python
tools = [
    {
        "type": "function",
        "name": "lookup_weather",
        "description": "Lookup the weather for a given city name.",
        "strict": True,
        "parameters": {
            "type": "object",
            "properties": {
                "city_name": {"type": "string", "description": "The city name"},
            },
            "required": ["city_name"],       # 所有属性必须列出
            "additionalProperties": False,   # 严格模式下必需
        },
    }
]
```

### 工具调用回传（执行并返回结果）

当模型请求调用工具时，使用 `response.output` 项 + `function_call_output` — <strong>而非</strong> 聊天补全中的 `role: assistant` + `role: tool` 模式。

```python
import json

messages = [
    {"role": "system", "content": "You are a weather chatbot."},
    {"role": "user", "content": "Is it sunny in Berkeley?"},
]

response = client.responses.create(
    model=deployment, input=messages, tools=tools, store=False,
)

tool_calls = [item for item in response.output if item.type == "function_call"]
if tool_calls:
    # 将模型的 function_call 项添加到对话中
    messages.extend(response.output)

    # 执行每个工具并添加结果
    for tc in tool_calls:
        result = execute_tool(tc.name, json.loads(tc.arguments))
        messages.append({
            "type": "function_call_output",
            "call_id": tc.call_id,
            "output": json.dumps(result),
        })

    # 使用工具结果获取最终响应
    response = client.responses.create(
        model=deployment, input=messages, tools=tools, store=False,
    )
    print(response.output_text)
```

### 少量示例的工具调用

在 `input` 中提供少量工具调用示例时，使用 `function_call` 和 `function_call_output` 项。ID 必须以 `fc_` 开头。

```python
messages = [
    {"role": "system", "content": "You are a product search assistant."},
    {"role": "user", "content": "Find climbing gear for outdoors"},
    {
        "type": "function_call",
        "id": "fc_example1",
        "call_id": "call_example1",
        "name": "search_database",
        "arguments": '{"search_query": "climbing gear outdoor"}',
    },
    {
        "type": "function_call_output",
        "call_id": "call_example1",
        "output": "Results: ...",
    },
    {"role": "user", "content": "Now find shoes under $50"},
]
```

```python
# 内置网页搜索示例
resp = client.responses.create(
    model=deployment,
    tools=[{"type": "web_search_preview"}],
    input="What was a positive news story from today?",
    store=False,
)
print(resp.output_text)
```

## 图像输入

图像内容项的类型从 `image_url` 变为 `input_image`，URL 从嵌套对象变为扁平字符串。

### 图像输入 — 之前（聊天补全）
```python
resp = client.chat.completions.create(
    model=deployment,
    messages=[
        {
            "role": "user",
            "content": [
                {"type": "text", "text": "What's in this image?"},
                {
                    "type": "image_url",
                    "image_url": {"url": "https://example.com/image.jpg"},
                },
            ],
        }
    ],
    max_tokens=500,
)
print(resp.choices[0].message.content)
```

### 图像输入 — 之后（Responses API，URL形式）
```python
resp = client.responses.create(
    model=deployment,
    input=[
        {
            "role": "user",
            "content": [
                {"type": "input_text", "text": "What's in this image?"},
                {
                    "type": "input_image",
                    "image_url": "https://example.com/image.jpg",
                },
            ],
        }
    ],
    max_output_tokens=500,
    store=False,
)
print(resp.output_text)
```

### 图像输入 — 之后（Responses API，base64形式）
```python
import base64

def encode_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode("utf-8")

base64_image = encode_image("path_to_your_image.jpg")

resp = client.responses.create(
    model=deployment,
    input=[
        {
            "role": "user",
            "content": [
                {"type": "input_text", "text": "What's in this image?"},
                {
                    "type": "input_image",
                    "image_url": f"data:image/jpeg;base64,{base64_image}",
                },
            ],
        }
    ],
    max_output_tokens=500,
    store=False,
)
print(resp.output_text)
```

> <strong>关键变化</strong>：（1）`"type": "image_url"` → `"type": "input_image"`，（2）`"image_url": {"url": "..."}`（嵌套对象）→ `"image_url": "..."`（扁平字符串 — HTTPS URL 或 `data:image/...;base64,...` 数据 URI），（3）`"type": "text"` → `"type": "input_text"`。

## Microsoft Agent Framework (MAF) 迁移

**先检查你的 MAF 版本** — 迁移取决于你是使用 MAF 1.0.0+ 还是 1.0.0 以下的 beta/rc 版本。

检查方法：`python -c "import agent_framework_openai; print(agent_framework_openai.__version__)"`

### MAF 1.0.0+（agent-framework-openai >= 1.0.0）

在 MAF 1.0.0+ 中，`OpenAIChatClient` **已经使用 Responses API** — 无需迁移。

如果代码库中使用遗留的 `OpenAIChatCompletionClient`（使用 `chat.completions.create`），请替换为 `OpenAIChatClient`：

之前：
```python
from agent_framework.openai import OpenAIChatCompletionClient
from azure.identity.aio import DefaultAzureCredential, get_bearer_token_provider

async_credential = DefaultAzureCredential()
token_provider = get_bearer_token_provider(async_credential, "https://cognitiveservices.azure.com/.default")

client = OpenAIChatCompletionClient(
    base_url=f"{os.environ['AZURE_OPENAI_ENDPOINT']}/openai/v1/",
    api_key=token_provider,
    model=os.environ["AZURE_OPENAI_CHAT_DEPLOYMENT"],
)
```

之后：
```python
from agent_framework.openai import OpenAIChatClient
from azure.identity.aio import DefaultAzureCredential, get_bearer_token_provider

async_credential = DefaultAzureCredential()
token_provider = get_bearer_token_provider(async_credential, "https://cognitiveservices.azure.com/.default")

client = OpenAIChatClient(
    base_url=f"{os.environ['AZURE_OPENAI_ENDPOINT']}/openai/v1/",
    api_key=token_provider,
    model=os.environ["AZURE_OPENAI_CHAT_DEPLOYMENT"],
)
```

### MAF 1.0.0 以下（beta/rc 版本）

在 1.0.0 以下版本的 MAF 中，`OpenAIChatClient` 使用聊天补全。升级到 `agent-framework-openai>=1.0.0` 后，`OpenAIChatClient` 默认使用 Responses API。

> <strong>注意</strong>：`Agent`、`MCPStreamableHTTPTool` 等 MAF API 保持不变 — 仅客户端类的导入和实例化发生改变。

## LangChain (`langchain-openai`) 迁移

在 `ChatOpenAI()` 中添加 `use_responses_api=True`。并且将消息内容访问由 `.content` 改为 `.text`。

之前：
```python
import azure.identity
from langchain_openai import ChatOpenAI
from pydantic import SecretStr

token_provider = azure.identity.get_bearer_token_provider(
    azure.identity.DefaultAzureCredential(),
    "https://cognitiveservices.azure.com/.default",
)
model = ChatOpenAI(
    model=os.environ.get("AZURE_OPENAI_CHAT_DEPLOYMENT"),
    base_url=os.environ["AZURE_OPENAI_ENDPOINT"] + "/openai/v1/",
    api_key=token_provider,
)

# ... 代理调用 ...
result = await agent.ainvoke({"messages": [HumanMessage(content=query)]})
print(result['messages'][-1].content)
```

之后：
```python
import azure.identity
from langchain_openai import ChatOpenAI
from pydantic import SecretStr

token_provider = azure.identity.get_bearer_token_provider(
    azure.identity.DefaultAzureCredential(),
    "https://cognitiveservices.azure.com/.default",
)
model = ChatOpenAI(
    model=os.environ.get("AZURE_OPENAI_CHAT_DEPLOYMENT"),
    base_url=os.environ["AZURE_OPENAI_ENDPOINT"] + "/openai/v1/",
    api_key=token_provider,
    use_responses_api=True,
)

# ... 代理调用 ...
result = await agent.ainvoke({"messages": [HumanMessage(content=query)]})
print(result['messages'][-1].text)
```

> <strong>关键变化</strong>：（1）构造函数中 `use_responses_api=True`，（2）响应消息中 `.content` → `.text`。

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免责声明**：
本文件由 AI 翻译服务 [Co-op Translator](https://github.com/Azure/co-op-translator) 翻译完成。尽管我们力求准确，但请注意，自动翻译可能包含错误或不准确之处。原始语言版文件应视为权威来源。对于重要信息，建议使用专业人工翻译。我们对因使用本翻译而产生的任何误解或误释不承担责任。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->