# 回應 API 速查表 (Python + Azure OpenAI)

> 以下所有程式碼片段均假設 `deployment = os.environ["AZURE_OPENAI_DEPLOYMENT"]` 和 `client` 已初始化（請參閱客戶端設定）。

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

## 非同步客戶端設定 — EntraID 與明確租戶（多租戶）

當 Azure OpenAI 資源位於與預設不同的 <strong>租戶</strong> 時，請明確將 `tenant_id` 傳入認證。此情況常見於開發/測試場景，其中開發者的主租戶與資源租戶不同。

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

## 非同步客戶端遷移 — 之前/之後

之前（棄用）：
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

之後：
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

## 完整同步遷移 — 之前/之後

之前（舊版 — Azure OpenAI 聊天完成功能）：
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

之後（回應 API — Azure OpenAI v1 端點）：
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

## 網頁應用串流 — 後端對前端資料形態

在遷移將 SSE/JSONL 串流至前端的網頁應用時，<strong>後端序列化格式</strong>會改變。請設計新的後端輸出以保留前端現有的存取模式，讓前端不需變更。

<strong>之前</strong> — 聊天完成功能後端通常序列化每個塊的 `choices[0]` 字典：
```python
# Old: serialized full choice dict per chunk
async for chunk in response:
    if chunk.choices:
        yield json.dumps(chunk.choices[0].model_dump()) + "\n"
```
前端讀取：`response.delta.content`（深層路徑至選項物件）。

<strong>之後</strong> — 回應 API 後端輸出最小化形態，保留相同的前端存取路徑：
```python
# New: emit only what the frontend needs
async for event in await chat_coroutine:
    if event.type == "response.output_text.delta":
        yield json.dumps({"delta": {"content": event.delta}}) + "\n"
    elif event.type == "response.completed":
        yield json.dumps({"delta": {"content": None}, "finish_reason": "stop"}) + "\n"
```
前端仍讀取 `response.delta.content` — <strong>無需變更前端</strong>。

> <strong>關鍵見解</strong>：回應 API 串流形態 (`event.type` + `event.delta`) 與聊天完成功能 (`chunk.choices[0].delta.content`) 本質不同。但您的後端對前端契約可由您定義。請塑造後端輸出以配合前端已有預期。

## 串流事件序列

當 `stream: true` 時，API 依此順序發出事件：
1. `response.created` – 回應物件初始化
2. `response.in_progress` – 開始生成
3. `response.output_item.added` – 輸出項目建立
4. `response.content_part.added` – 開始內容部分
5. `response.output_text.delta` – 文字區塊（多個，每個有 `delta: string`）
6. `response.output_text.done` – 文字生成完畢
7. `response.content_part.done` – 結束內容部分
8. `response.output_item.done` – 輸出項目完成
9. `response.completed` – 完整回應完成

對於基本文字串流，只需處理 `response.output_text.delta`（文字區塊）與 `response.completed`（結束）。

## 網頁應用中的串流錯誤處理

在網頁應用串流時，將非同步迭代包裹於 `try/except` 中，並以 JSON 形式傳出錯誤，以便前端可優雅顯示（如流量限制、暫時性失敗）：

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

> <strong>重要原因</strong>：Azure OpenAI 流量限制時會返回 `429 Too Many Requests`。若無 `try/except`，串流回應將悄然中止。若有，其則使前端收到 `{"error": "Too Many Requests"}` 並顯示重試提示。

## 串流事件類型（Python SDK）

- `ResponseTextDeltaEvent`：`type='response.output_text.delta'`，`delta: str`
- `ResponseCompletedEvent`：`type='response.completed'`，`response: Response`

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

錯誤主體結構已從聊天完成更改為回應 API。

之前（聊天完成）：
```python
except openai.APIError as error:
    if error.code == "content_filter":
        if error.body["innererror"]["content_filter_result"]["jailbreak"]["filtered"] is True:
            print("Jailbreak detected!")
```

之後（回應 API）：
```python
except openai.APIError as error:
    if error.code == "content_filter":
        if error.body["content_filters"][0]["content_filter_results"]["jailbreak"]["filtered"] is True:
            print("Jailbreak detected!")
```

主要差異：
- `innererror` 包裝器已 <strong>移除</strong> — 內容過濾細節現於 `error.body` 頂層。
- `content_filter_result` （單數）→ `content_filters` （複數陣列），每個條目中包含 `content_filter_results`（複數）。
- `content_filters` 中每個條目包含 `blocked`、`source_type`、及 `content_filter_results`，涵蓋各分類細節（`jailbreak`、`hate`、`sexual`、`violence`、`self_harm`）。

完整回應 API 內容過濾錯誤主體形態：
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

## 原始 HTTP 遷移（requests/httpx）

若應用直接呼叫 Azure OpenAI REST 而非使用 SDK：

之前（聊天完成）：
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

之後（回應 API）：
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

> <strong>備註</strong>：`output_text` 是 Python SDK 中 `Response` 物件上的便利屬性。原始 REST JSON 回應並無頂層 `output_text` 欄位 — 文字存於 `output[0].content[0].text`。

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

具內容類型的多輪（明確 `input_text`/`output_text`）：
```python
messages = [
    {"role": "system", "content": [{"type": "input_text", "text": "You are helpful."}]},
    {"role": "user", "content": [{"type": "input_text", "text": "Hi"}]},
    {"role": "assistant", "content": [{"type": "output_text", "text": "Hello!"}]},
    {"role": "user", "content": [{"type": "input_text", "text": "Tell me a joke"}]},
]
resp = client.responses.create(model=deployment, input=messages, store=False)
```

### 透過 `previous_response_id` 的多輪（替代方案）

您可以無需自行管理對話陣列，改用伺服器端串接 `previous_response_id` 的回應。API 會儲存每次回應並自動加上先前輪次。



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

**何時使用哪種方式：**

| 方法 | 優點 | 缺點 |
|---|---|---|
| `input` 陣列（手動） | 完全控制歷史；可修剪/摘要；不需要伺服器端儲存（`store=False`） | 程式碼較多；您需管理陣列 |
| `previous_response_id` | 程式碼更簡單；自動串接 | 需要 `store=True`（預設）；對話會儲存在伺服器端；無法修改回合間的歷史 |

> **遷移說明：** 大多數 Chat Completions 應用已自行管理訊息陣列，因此轉換為 `input` 陣列是一種更直接的 1:1 遷移。新程式碼或不需要操作對話歷史時使用 `previous_response_id`。

## O 系列推理模型（o1、o3-mini、o3、o4-mini）

O 系列模型在遷移到 Responses API 時有獨特的參數限制。

### o 系列的參數對應

| Chat Completions（o 系列） | Responses API | 注意事項 |
|---|---|---|
| `max_completion_tokens` | `max_output_tokens` | 設為高（4096+）—推理標記會計入限制 |
| `reasoning_effort` | `reasoning.effort` | 有該參數則保留（低/中/高） |
| `temperature` | 移除或設為 `1` | O 系列只接受 `1` |
| `top_p` | 移除 | O 系列不支援 |
| `seed` | 移除 | Responses API 不支援 |

### O 系列之前/之後

之前（Chat Completions 與 o 系列）：
```python
resp = client.chat.completions.create(
    model="o4-mini",
    messages=[{"role": "user", "content": "Solve this step by step: 2x + 5 = 13"}],
    max_completion_tokens=4096,
    reasoning_effort="medium",
)
print(resp.choices[0].message.content)
```

之後（Responses API）：
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

> <strong>注意</strong>：O 系列模型在推理期間可能會緩衝輸出才發送文字增量。串流仍然有效，但第一個 `response.output_text.delta` 事件可能比 GPT 模型延遲更長。

## 存取推理標記
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

> <strong>重要</strong>：請使用 `max_output_tokens=1000`（非 50–200）來涵蓋推理模型的內部推理過程。模型在產生最終輸出前會內部使用推理標記。

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

- 在 `tools` 中定義函式，採用 **平面 Responses API 格式** — `name`、`description` 與 `parameters` 為頂層（非巢狀於 `function` 下）。
- 模型請求呼叫工具時，在您的應用中執行工具，並將工具結果作為 `function_call_output` 項目放入下一次請求的 `input` 中。
- 保持 schema 精簡；執行前驗證輸入。
- 使用 `strict: true` 時，所有屬性必須列在 `required`，且 `additionalProperties: false` 為必填。

> **⚠️ `pydantic_function_tool()` 不相容**：`openai.pydantic_function_tool()` 輔助工具仍舊產生舊 Chat Completions 巢狀格式（`{"type": "function", "function": {"name": ...}}`）。請勿與 `responses.create()` 一起使用。請手動定義工具 schema 或寫包裝器以平整輸出。

### 工具定義格式

Responses API 使用 <strong>平面</strong> 工具格式 — `name`、`description`、`parameters` 為頂層鍵（非巢狀於 `function` 下）。

**之前（Chat Completions — 巢狀格式）：**
```python
tools = [{"type": "function", "function": {"name": "lookup_weather", "parameters": {...}}}]
```

**之後（Responses API — 平面格式）：**
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

使用 `strict: true`（schema 強制執行）：
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

### 工具呼叫往返（執行並回傳結果）

模型請求工具呼叫時，使用 `response.output` 項目 + `function_call_output` — <strong>非</strong> Chat Completions 的 `role: assistant` + `role: tool` 模式。

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

### 少量範例的工具呼叫示例

在 `input` 中提供少量工具呼叫範例時，使用 `function_call` 與 `function_call_output` 項目。ID 必須以 `fc_` 開頭。

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

## 影像輸入

影像內容項目型態從 `image_url` 轉為 `input_image`，URL 從巢狀物件變成平面字串。

### 影像輸入 — 之前（Chat Completions）
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

### 影像輸入 — 之後（Responses API，URL）
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

### 影像輸入 — 之後（Responses API，base64）
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

> <strong>主要變更</strong>：(1) `"type": "image_url"` → `"type": "input_image"`，(2) `"image_url": {"url": "..."}`（巢狀物件）→ `"image_url": "..."`（平面字串 — HTTPS URL 或 `data:image/...;base64,...` 資料 URI），(3) `"type": "text"` → `"type": "input_text"`。

## Microsoft Agent Framework (MAF) 遷移

**請先確認您的 MAF 版本** — 遷移方式取決於您使用的是 MAF 1.0.0+ 還是 1.0.0 前的 beta/rc 版本。

查詢方式：`python -c "import agent_framework_openai; print(agent_framework_openai.__version__)"`

### MAF 1.0.0+ （agent-framework-openai >= 1.0.0）

在 MAF 1.0.0+ 中，`OpenAIChatClient` **已經使用 Responses API** — 無需遷移。

若程式碼使用舊版的 `OpenAIChatCompletionClient`（使用 `chat.completions.create`），請替換為 `OpenAIChatClient`：

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

之後：
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

### MAF 1.0.0 前版本（beta/rc 版本）

在 1.0.0 前版本的 MAF 中，`OpenAIChatClient` 使用 Chat Completions。請升級至 `agent-framework-openai>=1.0.0`，其中 `OpenAIChatClient` 預設使用 Responses API。

> <strong>注意</strong>：`Agent`、`MCPStreamableHTTPTool` 與其他 MAF API 不變 — 只有客戶端類別匯入及實例化方式改變。

## LangChain (`langchain-openai`) 遷移

將 `use_responses_api=True` 新增到 `ChatOpenAI()`。同時將訊息內容存取從 `.content` 更新為 `.text`。

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

> <strong>主要變更</strong>：(1) 建構函式中的 `use_responses_api=True`，(2) 回應訊息中的 `.content` → `.text`。

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責聲明**：
此文件已使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。雖然我們努力追求準確性，但請注意自動翻譯可能包含錯誤或不準確之處。原始文件的母語版本應視為權威來源。對於關鍵資訊，建議採用專業人工翻譯。我們不對因使用此翻譯所產生的任何誤解或誤譯承擔責任。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->