# Responses API 速查表 (Python + Azure OpenAI)

> 以下所有程式碼片段皆假設已初始化 `deployment = os.environ["AZURE_OPENAI_DEPLOYMENT"]` 與 `client`（請參閱客戶端設定）。

## 基本請求
```python
resp = client.responses.create(
    model=deployment,
    input="Hello",
    max_output_tokens=1000,
    store=False,
)
print(resp.output_text)
```

## 客戶端設定 — EntraID（推薦）
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

## 客戶端設定 — API 金鑰
```python
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ["AZURE_OPENAI_API_KEY"],
    base_url=f"{os.environ['AZURE_OPENAI_ENDPOINT'].rstrip('/')}/openai/v1/",
)
```

## 非同步客戶端設定 — EntraID
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

## 非同步客戶端設定 — EntraID，明確指定租戶（多租戶）

當 Azure OpenAI 資源位於與預設不同的<strong>租戶</strong>時，請明確將 `tenant_id` 傳入憑證。這在開發/測試場景很常見，因為開發者的主租戶與資源租戶不同。

```python
import os
from azure.identity.aio import (
    AzureDeveloperCliCredential,
    ChainedTokenCredential,
    ManagedIdentityCredential,
    get_bearer_token_provider,
)
from openai import AsyncOpenAI

# ManagedIdentityCredential for production (Azure Container Apps, App Service, etc.)
managed_identity_cred = ManagedIdentityCredential(
    client_id=os.getenv("AZURE_CLIENT_ID")  # user-assigned managed identity
)
# AzureDeveloperCliCredential for local dev — explicit tenant_id is critical
azd_cred = AzureDeveloperCliCredential(
    tenant_id=os.getenv("AZURE_TENANT_ID"),
    process_timeout=60,
)
# Chain: try managed identity first, fall back to azd CLI
azure_credential = ChainedTokenCredential(managed_identity_cred, azd_cred)

token_provider = get_bearer_token_provider(
    azure_credential, "https://cognitiveservices.azure.com/.default"
)

client = AsyncOpenAI(
    base_url=f"{os.environ['AZURE_OPENAI_ENDPOINT'].rstrip('/')}/openai/v1/",
    api_key=token_provider,
)
```

## 非同步客戶端遷移 — 前後對比

過時舊寫法：
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

新寫法：
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

## 完整同步遷移 — 前後對比

過時舊寫法（Azure OpenAI 聊天補全）：
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

新寫法（Responses API — Azure OpenAI v1 端點）：
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

## 串流（同步）
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
        print()  # newline at end
```

## 串流（非同步）
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

## 網頁應用串流 — 後端到前端結構

遷移串流 SSE/JSONL 至前端的網頁應用時，<strong>後端的序列化格式</strong>會改變。請設計後端輸出以維持前端現有的讀取邏輯，確保前端無需修改。

<strong>之前</strong> — Chat Completions 後端通常序列化每筆 `choices[0]` 字典：
```python
# Old: serialized full choice dict per chunk
async for chunk in response:
    if chunk.choices:
        yield json.dumps(chunk.choices[0].model_dump()) + "\n"
```
前端讀取：`response.delta.content`（深入讀取 choice 物件的路徑）。

<strong>之後</strong> — Responses API 後端輸出最小化結構，但保持相同的前端讀取路徑：
```python
# New: emit only what the frontend needs
async for event in await chat_coroutine:
    if event.type == "response.output_text.delta":
        yield json.dumps({"delta": {"content": event.delta}}) + "\n"
    elif event.type == "response.completed":
        yield json.dumps({"delta": {"content": None}, "finish_reason": "stop"}) + "\n"
```
前端仍讀取 `response.delta.content` — <strong>不需變更前端</strong>。

> <strong>核心見解</strong>：Responses API 串流的結構 (`event.type` + `event.delta`) 和 Chat Completions (`chunk.choices[0].delta.content`) 本質不同，但您定義後端與前端間的契約。請將後端輸出形狀調整為符合前端預期。

## 串流事件序列

在 `stream: true` 時，API 依序送出事件：
1. `response.created` — 回應物件初始化
2. `response.in_progress` — 生成開始
3. `response.output_item.added` — 輸出項建立
4. `response.content_part.added` — 內容片段開始
5. `response.output_text.delta` — 文字區塊（多個，每個含 `delta: string`）
6. `response.output_text.done` — 文字生成完成
7. `response.content_part.done` — 內容片段完成
8. `response.output_item.done` — 輸出項完成
9. `response.completed` — 完整回應完成

對於基本文字串流，僅需處理 `response.output_text.delta`（文字區塊）和 `response.completed`（結束）。

## 網頁應用串流錯誤處理

在網頁應用串流時，將非同步迭代包裹在 `try/except`，並以 JSON 格式回傳錯誤訊息，讓前端能優雅顯示錯誤（例如速率限制、臨時故障）：

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

> <strong>為何此法重要</strong>：Azure OpenAI 在速率限制時會返回 `429 Too Many Requests`。若未使用 `try/except`，串流回應會默默終止。有了它，前端能接收 `{"error": "Too Many Requests"}` 並呈現重試提示。

## 串流事件類型（Python SDK）

- `ResponseTextDeltaEvent`：`type='response.output_text.delta'`、`delta: str`
- `ResponseCompletedEvent`：`type='response.completed'`、`response: Response`

## 對話格式
```python
# The Responses API supports conversation format via input array
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

## 內容過濾錯誤處理

錯誤體系從 Chat Completions 轉換到 Responses API 時有變更。

過去（Chat Completions）：
```python
except openai.APIError as error:
    if error.code == "content_filter":
        if error.body["innererror"]["content_filter_result"]["jailbreak"]["filtered"] is True:
            print("Jailbreak detected!")
```

現在（Responses API）：
```python
except openai.APIError as error:
    if error.code == "content_filter":
        if error.body["content_filters"][0]["content_filter_results"]["jailbreak"]["filtered"] is True:
            print("Jailbreak detected!")
```

主要差異：
- `innererror` 包覆層 <strong>消失</strong> — 內容過濾細節現在在 `error.body` 頂層。
- `content_filter_result`（單數）→ `content_filters`（複數陣列），每條目內有複數 `content_filter_results`。
- `content_filters` 中每項包含 `blocked`、`source_type`、`content_filter_results`，並針對各類別細節（`jailbreak`、`hate`、`sexual`、`violence`、`self_harm`）。

完整 Responses API 內容過濾錯誤體系：
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

## 原生 HTTP 遷移（requests/httpx）

若應用直接呼叫 Azure OpenAI REST 端點，而非使用 SDK：

過去（Chat Completions）：
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

現在（Responses API）：
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

> <strong>注意</strong>：`output_text` 是 Python SDK 的 `Response` 物件上便利的屬性。原生 REST JSON 回應沒有頂層 `output_text` 欄位 — 文字位於 `output[0].content[0].text`。

## 多輪對話
```python
# Build a conversation with Responses API
messages = [
    {"role": "system", "content": "You are a helpful coding assistant."},
    {"role": "user", "content": "Write a Python function to calculate factorial"},
]

response = client.responses.create(
    model=deployment,
    input=messages,
    max_output_tokens=400,
)

# Add assistant's response to conversation
messages.append({"role": "assistant", "content": response.output_text})

# Continue the conversation
messages.append({"role": "user", "content": "Now optimize it with memoization"})

response2 = client.responses.create(
    model=deployment,
    input=messages,
    max_output_tokens=400,
)
print(response2.output_text)
```

內容類型多輪（明確指定 `input_text` / `output_text`）：
```python
messages = [
    {"role": "system", "content": [{"type": "input_text", "text": "You are helpful."}]},
    {"role": "user", "content": [{"type": "input_text", "text": "Hi"}]},
    {"role": "assistant", "content": [{"type": "output_text", "text": "Hello!"}]},
    {"role": "user", "content": [{"type": "input_text", "text": "Tell me a joke"}]},
]
resp = client.responses.create(model=deployment, input=messages, store=False)
```

### 透過 `previous_response_id` 實現多輪（替代方案）

不用自己管理對話陣列，而是伺服器端用 `previous_response_id` 串聯回應。API 會存每則回應，自動加上先前輪次。

```python
# First turn
response = client.responses.create(
    model=deployment,
    input=[{"role": "user", "content": "Write a Python function to calculate factorial"}],
)
print(response.output_text)

# Subsequent turns — just pass the new user message + previous response ID
response2 = client.responses.create(
    model=deployment,
    input=[{"role": "user", "content": "Now optimize it with memoization"}],
    previous_response_id=response.id,
)
print(response2.output_text)
```



| 方法 | 優點 | 缺點 |

| `input` 陣列（手動） | 完全控制歷史；可修剪/摘要；無需伺服器端存儲（`store=False`） | 需寫更多程式碼；自行管理陣列 |
| `previous_response_id` | 程式碼更簡單；自動串連 | 需要 `store=True`（預設）；聊天紀錄存伺服器；無法修改中間歷史 |

> **遷移提示：** 大多數 Chat Completions 應用已自行管理訊息陣列，切換到 `input` 陣列為更直接的 1:1 遷移。若為新程式碼或不需操作對話歷史，建議用 `previous_response_id`。

## O 系推理模型 (o1, o3-mini, o3, o4-mini)

O 系模型在遷移至 Responses API 時有特別參數限制。

### O 系參數映射

| Chat Completions（o 系） | Responses API | 備註 |

| `max_completion_tokens` | `max_output_tokens` | 設得高些（4096 以上）— 推理 tokens 計入限制 |
| `reasoning_effort` | `reasoning.effort` | 若有則照原設置（low/medium/high） |
| `temperature` | 移除或設為 `1` | O 系模型只接受 `1` |
| `top_p` | 移除 | O 系不支援 |
| `seed` | 移除 | Responses API 不支援 |

### O 系前後對比

過去（Chat Completions 使用 o 系）：

之前（使用 o 系列的聊天補全）：
```python
resp = client.chat.completions.create(
    model="o4-mini",
    messages=[{"role": "user", "content": "Solve this step by step: 2x + 5 = 13"}],
    max_completion_tokens=4096,
    reasoning_effort="medium",
)
print(resp.choices[0].message.content)
```

在 (Responses API) 之後：
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

> <strong>注意</strong>：O 系列模型在推理過程中可能會緩衝輸出，再發送文字增量。串流仍然可用，但第一個 `response.output_text.delta` 事件可能比 GPT 模型延遲更長時間才到達。

## 存取推理 Token
```python
# Reasoning models use internal reasoning — you can see how many reasoning tokens were used
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

> <strong>重要</strong>：使用 `max_output_tokens=1000`（而非 50–200）來考量推理模型的內部推理過程。模型在生成最終輸出前會在內部使用推理 Tokens。

## 結構化輸出 — JSON Schema
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

- 在 `tools` 中定義函式，使用 **平面 Responses API 格式** — `name`、`description` 和 `parameters` 為頂層鍵（不嵌套在 `function` 下）。
- 當模型請求執行工具時，在你的應用程式中執行它，並將工具結果作為 `function_call_output` 項目放在下一次請求的 `input` 中。
- 保持 Schema 簡潔；在執行前驗證輸入。
- 使用 `strict: true` 時，所有屬性必須列在 `required` 中，且 `additionalProperties: false` 是強制性的。

> **⚠️ `pydantic_function_tool()` 不相容**：`openai.pydantic_function_tool()` 輔助工具仍產生舊的 Chat Completions 嵌套格式（`{"type": "function", "function": {"name": ...}}`）。勿與 `responses.create()` 同時使用。請手動定義工具 Schema 或撰寫包裝函式以展平輸出。

### 工具定義格式

Responses API 使用 <strong>平面</strong> 工具格式 — `name`、`description`、`parameters` 為頂層鍵（不嵌套在 `function` 下）。

**之前 (Chat Completions — 嵌套格式)：**
```python
tools = [{"type": "function", "function": {"name": "lookup_weather", "parameters": {...}}}]
```

**之後 (Responses API — 平面格式)：**
```python
tools = [{"type": "function", "name": "lookup_weather", "parameters": {...}}]
```

完整範例：
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

使用 `strict: true`（Schema 強制）：
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
            "required": ["city_name"],       # All properties MUST be listed
            "additionalProperties": False,   # Required for strict mode
        },
    }
]
```

### 工具呼叫往返流程（執行與回傳結果）

當模型請求呼叫工具時，使用 `response.output` 項目加上 `function_call_output` — <strong>不要</strong>使用 Chat Completions 的 `role: assistant` 加 `role: tool` 模式。

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
    # Add the model's function_call items to conversation
    messages.extend(response.output)

    # Execute each tool and add results
    for tc in tool_calls:
        result = execute_tool(tc.name, json.loads(tc.arguments))
        messages.append({
            "type": "function_call_output",
            "call_id": tc.call_id,
            "output": json.dumps(result),
        })

    # Get final response with tool results
    response = client.responses.create(
        model=deployment, input=messages, tools=tools, store=False,
    )
    print(response.output_text)
```

### 少量示例的工具呼叫範例

提供少量工具呼叫示例時，在 `input` 中使用 `function_call` 和 `function_call_output` 項目。IDs 必須以 `fc_` 開頭。

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
# Built-in web search example
resp = client.responses.create(
    model=deployment,
    tools=[{"type": "web_search_preview"}],
    input="What was a positive news story from today?",
    store=False,
)
print(resp.output_text)
```

## 圖片輸入

圖片內容項目的類型從 `image_url` 變更為 `input_image`，URL 從嵌套物件變成平面字串。

### 圖片輸入 — 之前 (Chat Completions)
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

### 圖片輸入 — 之後 (Responses API，URL 格式)
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

### 圖片輸入 — 之後 (Responses API，base64 格式)
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

> <strong>主要變更</strong>：（1）`"type": "image_url"` → `"type": "input_image"`，（2）`"image_url": {"url": "..."}`（嵌套物件）→ `"image_url": "..."`（平面字串 — HTTPS URL 或 `data:image/...;base64,...` 資料 URI），（3）`"type": "text"` → `"type": "input_text"`。

## 微軟代理框架（Microsoft Agent Framework，MAF）遷移

**先檢查你的 MAF 版本** — 遷移取決於你是使用 MAF 1.0.0+ 還是 1.0.0 之前的 beta/rc。

檢查方法：`python -c "import agent_framework_openai; print(agent_framework_openai.__version__)"`

### MAF 1.0.0+ (agent-framework-openai >= 1.0.0)

在 MAF 1.0.0+ 中，`OpenAIChatClient` **已經使用 Responses API** — 無需遷移。

如果程式碼使用舊版 `OpenAIChatCompletionClient`（使用 `chat.completions.create`），請替換成 `OpenAIChatClient`：

前：
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

後：
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

### MAF 1.0.0 之前版本（beta/rc 版本）

在 1.0.0 之前的 MAF 中，`OpenAIChatClient` 使用 Chat Completions。建議升級到 `agent-framework-openai>=1.0.0`，此版本預設 `OpenAIChatClient` 使用 Responses API。

> <strong>注意</strong>：`Agent`、`MCPStreamableHTTPTool` 及其他 MAF API 保持不變 — 只有客戶端類別的引入和實例化改變。

## LangChain (`langchain-openai`) 遷移

將 `use_responses_api=True` 加到 `ChatOpenAI()`，同時更新訊息內容存取方式，從 `.content` 改為 `.text`。

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

# ... agent invocation ...
result = await agent.ainvoke({"messages": [HumanMessage(content=query)]})
print(result['messages'][-1].content)
```

之後：
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

# ... agent invocation ...
result = await agent.ainvoke({"messages": [HumanMessage(content=query)]})
print(result['messages'][-1].text)
```

> <strong>主要變更</strong>：（1）建構子中的 `use_responses_api=True`，（2）回應訊息中 `.content` → `.text`。

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責聲明**：
本文件由 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 翻譯而成。雖然我們致力於確保準確性，但請注意，機器自動翻譯可能包含錯誤或不準確之處。原始文件的母語版本應被視為權威來源。對於重要資訊，建議進行專業人工翻譯。我們不對因使用本翻譯而產生的任何誤解或誤釋承擔責任。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->