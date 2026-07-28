# 回應 API 速查表（Python + Azure OpenAI）

> 以下所有程式碼片段均假設 `deployment = os.environ["AZURE_OPENAI_DEPLOYMENT"]` 且 `client` 已初始化（請參閱客戶端設置）。

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

## 客戶端設置 — EntraID（推薦）
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

## 客戶端設置 — API 金鑰
```python
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ["AZURE_OPENAI_API_KEY"],
    base_url=f"{os.environ['AZURE_OPENAI_ENDPOINT'].rstrip('/')}/openai/v1/",
)
```

## 非同步客戶端設置 — EntraID
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

## 非同步客戶端設置 — 明確指定租戶的 EntraID（多租戶）

當 Azure OpenAI 資源位於與預設不同的 <strong>租戶</strong> 時，請明確將 `tenant_id` 傳入憑證。這在開發/測試場景中很常見，因為開發者的主租戶可能與資源租戶不同。

```python
import os
from azure.identity.aio import (
    AzureDeveloperCliCredential,
    ChainedTokenCredential,
    ManagedIdentityCredential,
    get_bearer_token_provider,
)
from openai import AsyncOpenAI

# 用於生產環境的 ManagedIdentityCredential（Azure 容器應用、應用服務等）
managed_identity_cred = ManagedIdentityCredential(
    client_id=os.getenv("AZURE_CLIENT_ID")  # 使用者指派的託管身份
)
# 用於本地開發的 AzureDeveloperCliCredential — 明確的 tenant_id 非常重要
azd_cred = AzureDeveloperCliCredential(
    tenant_id=os.getenv("AZURE_TENANT_ID"),
    process_timeout=60,
)
# 鏈：首先嘗試託管身份，如失敗則回退至 azd CLI
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

之前（已棄用）：
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

## 完全同步遷移 — 之前/之後

之前（舊版 — Azure OpenAI 聊天完成）：
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

## 流式傳輸（同步）
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
        print()  # 末尾有新行
```

## 流式傳輸（非同步）
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

## 網頁應用流式傳輸 — 後端至前端格式

在將流式 SSE/JSONL 的網頁應用遷移到前端時，<strong>後端序列化格式</strong>會變更。請設計新的後端輸出以保留前端現有的存取模式，讓前端無需更改。

<strong>之前</strong> — 聊天完成的後端通常序列化每個區塊的 `choices[0]` 字典：
```python
# 舊版：每個區塊序列化的完整選擇字典
async for chunk in response:
    if chunk.choices:
        yield json.dumps(chunk.choices[0].model_dump()) + "\n"
```
前端讀取：`response.delta.content`（深入選項物件的深層路徑）。

<strong>之後</strong> — 回應 API 的後端輸出為簡化形狀，保留相同的前端存取路徑：
```python
# 新增：只發送前端所需要的內容
async for event in await chat_coroutine:
    if event.type == "response.output_text.delta":
        yield json.dumps({"delta": {"content": event.delta}}) + "\n"
    elif event.type == "response.completed":
        yield json.dumps({"delta": {"content": None}, "finish_reason": "stop"}) + "\n"
```
前端仍然讀取 `response.delta.content` — <strong>無需更改前端</strong>。

> <strong>關鍵見解</strong>：回應 API 流式傳輸的形狀（`event.type` + `event.delta`）本質上不同於聊天完成（`chunk.choices[0].delta.content`）。但您的後端到前端協議由您定義。調整後端輸出以符合前端已有的需求。

## 流式傳輸事件序列

當 `stream: true` 時，API 會依序發出以下事件：
1. `response.created` – 已初始化回應物件
2. `response.in_progress` – 開始生成
3. `response.output_item.added` – 新增輸出項目
4. `response.content_part.added` – 開始內容部分
5. `response.output_text.delta` – 文字區塊（多個，每個都有 `delta: string`）
6. `response.output_text.done` – 完成文字生成
7. `response.content_part.done` – 內容部分完成
8. `response.output_item.done` – 輸出項目完成
9. `response.completed` – 回應完整

對於基本的文字流式傳輸，只需處理 `response.output_text.delta`（文字區塊）和 `response.completed`（結束）。

## 網頁應用中的流式錯誤處理

在網頁應用中流式傳輸時，請將非同步迭代包裹在 `try/except` 中，並以 JSON 方式產生錯誤，讓前端能優雅顯示（例如速率限制、臨時失敗）：

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


> <strong>為何這很重要</strong>：Azure OpenAI 在速率限制時會返回 `429 Too Many Requests`。如果沒有 `try/except`，串流回應會靜默失效。加上它後，前端會收到 `{"error": "Too Many Requests"}`，並可顯示重試提示。

## 串流事件類型（Python SDK）

- `ResponseTextDeltaEvent`：`type='response.output_text.delta'`，`delta: str`
- `ResponseCompletedEvent`：`type='response.completed'`，`response: Response`

## 對話格式
```python
# Responses API 支援透過輸入陣列的對話格式
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

錯誤主體結構從 Chat Completions 變更為 Responses API。

之前（Chat Completions）：
```python
except openai.APIError as error:
    if error.code == "content_filter":
        if error.body["innererror"]["content_filter_result"]["jailbreak"]["filtered"] is True:
            print("Jailbreak detected!")
```

之後（Responses API）：
```python
except openai.APIError as error:
    if error.code == "content_filter":
        if error.body["content_filters"][0]["content_filter_results"]["jailbreak"]["filtered"] is True:
            print("Jailbreak detected!")
```

主要差異：
- `innererror` 包裝已<strong>移除</strong> — 內容過濾詳情現在位於 `error.body` 的頂層。
- `content_filter_result`（單數）→ `content_filters`（複數陣列），包含每項的 `content_filter_results`（複數）。
- `content_filters` 中的每個條目都包括 `blocked`、`source_type` 以及帶有各類別細節（`jailbreak`、`hate`、`sexual`、`violence`、`self_harm`）的 `content_filter_results`。

完整 Responses API 內容過濾錯誤主體格式：
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

如果應用程式直接呼叫 Azure OpenAI REST 而非使用 SDK：

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

之後（Responses API）：
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

> <strong>注意</strong>：`output_text` 是 Python SDK 中 `Response` 物件的便利屬性。原始 REST JSON 回應並沒有頂層 `output_text` 欄位 — 該文本位於 `output[0].content[0].text`。

## 多輪對話
```python
# 使用 Responses API 建立對話
messages = [
    {"role": "system", "content": "You are a helpful coding assistant."},
    {"role": "user", "content": "Write a Python function to calculate factorial"},
]

response = client.responses.create(
    model=deployment,
    input=messages,
    max_output_tokens=400,
)

# 將助理的回應加入對話
messages.append({"role": "assistant", "content": response.output_text})

# 繼續對話
messages.append({"role": "user", "content": "Now optimize it with memoization"})

response2 = client.responses.create(
    model=deployment,
    input=messages,
    max_output_tokens=400,
)
print(response2.output_text)
```

內容型多輪（明確 `input_text`/`output_text`）：
```python
messages = [
    {"role": "system", "content": [{"type": "input_text", "text": "You are helpful."}]},
    {"role": "user", "content": [{"type": "input_text", "text": "Hi"}]},
    {"role": "assistant", "content": [{"type": "output_text", "text": "Hello!"}]},
    {"role": "user", "content": [{"type": "input_text", "text": "Tell me a joke"}]},
]
resp = client.responses.create(model=deployment, input=messages, store=False)
```

### 透過 `previous_response_id` 進行多輪（替代方法）

你可以使用 `previous_response_id` 在伺服器端串接回應，而非自己管理對話陣列。API 會儲存每個回應並自動加上先前回合。



```python
# 第一次回合
response = client.responses.create(
    model=deployment,
    input=[{"role": "user", "content": "Write a Python function to calculate factorial"}],
)
print(response.output_text)

# 後續回合 — 只需傳送新的用戶訊息 + 之前的回應編號
response2 = client.responses.create(
    model=deployment,
    input=[{"role": "user", "content": "Now optimize it with memoization"}],
    previous_response_id=response.id,
)
print(response2.output_text)
```

**何時使用何者：**

| 方法 | 優點 | 缺點 |
|---|---|---|
| `input` 陣列（手動） | 完全控制歷史；可裁剪/摘要；不需伺服器端儲存（`store=False`） | 代碼較多；需自行管理陣列 |
| `previous_response_id` | 代碼較簡單；自動串接 | 需要 `store=True`（預設）；對話儲存在伺服器端；回合間無法修改歷史 |

> **遷移說明：** 大多數 Chat Completions 應用已自己管理訊息陣列，故轉為 `input` 陣列為最直接的 1:1 遷移。新代碼或無需操作對話歷史時使用 `previous_response_id`。

## O 系列推理模型（o1, o3-mini, o3, o4-mini）

O 系列模型在遷移至 Responses API 時有獨特的參數限制。

### o 系列參數對應

| Chat Completions（o 系列） | Responses API | 備註 |
|---|---|---|

| `max_completion_tokens` | `max_output_tokens` | 設置高（4096+）— 推理令牌計入限制 |
| `reasoning_effort` | `reasoning.effort` | 若存在則保持不變（低/中/高） |
| `temperature` | 移除或設置為 `1` | O 系列僅接受 `1` |
| `top_p` | 移除 | O 系列不支持 |
| `seed` | 移除 | Responses API 不支持 |

### O 系列前後差異

前（使用 Chat Completions 和 o 系列）：
```python
resp = client.chat.completions.create(
    model="o4-mini",
    messages=[{"role": "user", "content": "Solve this step by step: 2x + 5 = 13"}],
    max_completion_tokens=4096,
    reasoning_effort="medium",
)
print(resp.choices[0].message.content)
```

後（Responses API）：
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

> <strong>注意</strong>：O 系列模型在推理過程中可能會緩衝輸出，然後才發出文本增量。串流仍然有效，但第一個 `response.output_text.delta` 事件可能會比 GPT 模型晚些到達。

## 訪問推理令牌
```python
# 推理模型使用內部推理 — 你可以看到使用了多少推理代幣
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

> <strong>重要</strong>：請使用 `max_output_tokens=1000`（而非 50–200）以考慮推理模型的內部推理過程。模型在生成最終輸出前會在內部使用推理令牌。

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

- 在 `tools` 中定義函數要採用 **flat Responses API 格式** — `name`、`description` 和 `parameters` 位於頂層（不嵌套在 `function` 下面）。
- 當模型要求調用工具時，在您的應用中執行該工具，並將工具結果作為 `function_call_output` 項目放入下一次請求的 `input` 中。
- 保持 schema 最簡；執行前先驗證輸入。
- 使用 `strict: true` 時，所有屬性必須列在 `required` 中，且必須設置 `additionalProperties: false`。

> **⚠️ `pydantic_function_tool()` 不兼容**：`openai.pydantic_function_tool()` 助手仍會生成舊的 Chat Completions 嵌套格式（`{"type": "function", "function": {"name": ...}}`）。不要與 `responses.create()` 一起使用。請手動定義工具 schema 或寫個包裝器將輸出平坦化。

### 工具定義格式

Responses API 使用 <strong>扁平</strong> 工具格式 — `name`、`description`、`parameters` 位於頂層鍵（不嵌套在 `function` 下）。

**之前（Chat Completions — 嵌套）：**
```python
tools = [{"type": "function", "function": {"name": "lookup_weather", "parameters": {...}}}]
```

**之後（Responses API — 扁平）：**
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

使用 `strict: true`（schema 強制）：
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
            "required": ["city_name"],       # 所有屬性必須列出
            "additionalProperties": False,   # 嚴格模式下必須要求
        },
    }
]
```

### 工具調用來回（執行並返回結果）

當模型請求調用工具時，使用 `response.output` 項目 + `function_call_output` — <strong>不要</strong>使用 Chat Completions 的 `role: assistant` + `role: tool` 模式。

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
    # 將模型的 function_call 項目加入對話
    messages.extend(response.output)

    # 執行每個工具並加入結果
    for tc in tool_calls:
        result = execute_tool(tc.name, json.loads(tc.arguments))
        messages.append({
            "type": "function_call_output",
            "call_id": tc.call_id,
            "output": json.dumps(result),
        })

    # 使用工具結果取得最終回應
    response = client.responses.create(
        model=deployment, input=messages, tools=tools, store=False,
    )
    print(response.output_text)
```

### 少量示例工具調用

在 `input` 中提供少量示例的工具調用時，使用 `function_call` 和 `function_call_output` 項目。ID 必須以 `fc_` 開頭。

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
# 內置網頁搜索示例
resp = client.responses.create(
    model=deployment,
    tools=[{"type": "web_search_preview"}],
    input="What was a positive news story from today?",
    store=False,
)
print(resp.output_text)
```

## 圖像輸入

圖像內容項目類型由 `image_url` 改為 `input_image`，且 URL 從嵌套對象變為扁平字符串。

### 圖像輸入 — 之前（Chat Completions）
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

### 圖像輸入 — 之後（Responses API，URL）
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

### 圖像輸入 — 之後（Responses API，base64）
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

> <strong>關鍵改動</strong>： (1) `"type": "image_url"` → `"type": "input_image"`，(2) `"image_url": {"url": "..."}`（嵌套對象）→ `"image_url": "..."`（扁平字符串—HTTPS URL 或 `data:image/...;base64,...` 資料 URI），(3) `"type": "text"` → `"type": "input_text"`。

## Microsoft Agent Framework (MAF) 遷移

**先檢查您的 MAF 版本** — 遷移取決於您使用的是 MAF 1.0.0+ 還是之前的 beta/rc 版本。

查詢方式：`python -c "import agent_framework_openai; print(agent_framework_openai.__version__)"`

### MAF 1.0.0+ (agent-framework-openai >= 1.0.0)

在 MAF 1.0.0+ 中，`OpenAIChatClient` **已經使用 Responses API** — 不需要遷移。

如果程式碼庫使用的是舊的 `OpenAIChatCompletionClient`（使用 `chat.completions.create`），請替換為 `OpenAIChatClient`：

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

### MAF 1.0.0 之前（beta/rc 版本）

在 1.0.0 之前的 MAF 中，`OpenAIChatClient` 使用了 Chat Completions。請升級至 `agent-framework-openai>=1.0.0`，該版本中 `OpenAIChatClient` 預設使用 Responses API。

> <strong>注意</strong>：`Agent`、`MCPStreamableHTTPTool` 以及其他 MAF API 保持不變 — 只有客戶端類的導入和實例化方式改變。

## LangChain (`langchain-openai`) 遷移

在 `ChatOpenAI()` 中新增 `use_responses_api=True`。同時將訊息內容的存取從 `.content` 改為 `.text`。

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

# ... 代理調用 ...
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

# ... 代理調用 ...
result = await agent.ainvoke({"messages": [HumanMessage(content=query)]})
print(result['messages'][-1].text)
```

> <strong>關鍵改動</strong>： (1) 建構子中加入 `use_responses_api=True`，(2) 對回應訊息使用 `.text` 取代 `.content`。

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責聲明**：
本文件使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。雖然我們力求準確，但請注意，自動翻譯可能包含錯誤或不準確之處。原始文件的母語版本應被視為權威來源。對於重要資訊，建議尋求專業人工翻譯。我們不對因使用本翻譯而引起的任何誤解或曲解承擔責任。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->