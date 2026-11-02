# Bảng tóm tắt API Responses (Python + Azure OpenAI)

> Tất cả các đoạn mã dưới đây giả định `deployment = os.environ["AZURE_OPENAI_DEPLOYMENT"]` và `client` đã được khởi tạo (xem phần thiết lập client).

## Yêu cầu cơ bản
```python
resp = client.responses.create(
    model=deployment,
    input="Hello",
    max_output_tokens=1000,
    store=False,
)
print(resp.output_text)
```

## Thiết lập client — EntraID (được khuyên dùng)
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

## Thiết lập client — API key
```python
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ["AZURE_OPENAI_API_KEY"],
    base_url=f"{os.environ['AZURE_OPENAI_ENDPOINT'].rstrip('/')}/openai/v1/",
)
```

## Thiết lập client bất đồng bộ — EntraID
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

## Thiết lập client bất đồng bộ — EntraID với tenant rõ ràng (đa tenant)

Khi tài nguyên Azure OpenAI nằm trong **tenant khác** với tenant mặc định, hãy truyền `tenant_id` rõ ràng vào credential. Điều này phổ biến trong các trường hợp dev/test, nơi tenant chính của nhà phát triển khác với tenant chứa tài nguyên.

```python
import os
from azure.identity.aio import (
    AzureDeveloperCliCredential,
    ChainedTokenCredential,
    ManagedIdentityCredential,
    get_bearer_token_provider,
)
from openai import AsyncOpenAI

# ManagedIdentityCredential cho môi trường sản xuất (Azure Container Apps, App Service, v.v.)
managed_identity_cred = ManagedIdentityCredential(
    client_id=os.getenv("AZURE_CLIENT_ID")  # định danh được quản lý do người dùng chỉ định
)
# AzureDeveloperCliCredential cho phát triển cục bộ — tenant_id rõ ràng là rất quan trọng
azd_cred = AzureDeveloperCliCredential(
    tenant_id=os.getenv("AZURE_TENANT_ID"),
    process_timeout=60,
)
# Chuỗi: thử định danh được quản lý trước, nếu không thì dùng azd CLI
azure_credential = ChainedTokenCredential(managed_identity_cred, azd_cred)

token_provider = get_bearer_token_provider(
    azure_credential, "https://cognitiveservices.azure.com/.default"
)

client = AsyncOpenAI(
    base_url=f"{os.environ['AZURE_OPENAI_ENDPOINT'].rstrip('/')}/openai/v1/",
    api_key=token_provider,
)
```

## Di chuyển client bất đồng bộ — trước/sau

Trước (không được khuyến khích):
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

Sau:
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

## Di chuyển đồng bộ đầy đủ — trước/sau

Trước (cũ — Azure OpenAI Chat Completions):
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

Sau (Responses API — điểm cuối Azure OpenAI v1):
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

## Streaming (đồng bộ)
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
        print()  # xuống dòng ở cuối
```

## Streaming (bất đồng bộ)
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

## Streaming app web — cấu trúc backend sang frontend

Khi di chuyển một app web phát trực tiếp SSE/JSONL tới frontend, **định dạng tuần tự hóa backend** thay đổi. Thiết kế đầu ra backend mới sao cho giữ nguyên các mẫu truy cập frontend hiện có để frontend không cần thay đổi.

**Trước** — Backend Chat Completions thường tuần tự hóa dict `choices[0]` của mỗi đoạn:
```python
# Cũ: từ điển lựa chọn đầy đủ được tuần tự hóa theo từng khối
async for chunk in response:
    if chunk.choices:
        yield json.dumps(chunk.choices[0].model_dump()) + "\n"
```
Frontend đọc: `response.delta.content` (đường sâu trong đối tượng choice).

**Sau** — Backend Responses API phát ra cấu trúc tối giản giữ nguyên đường truy cập frontend:
```python
# Mới: chỉ phát ra những gì frontend cần
async for event in await chat_coroutine:
    if event.type == "response.output_text.delta":
        yield json.dumps({"delta": {"content": event.delta}}) + "\n"
    elif event.type == "response.completed":
        yield json.dumps({"delta": {"content": None}, "finish_reason": "stop"}) + "\n"
```
Frontend vẫn đọc `response.delta.content` — **không cần thay đổi frontend**.

> **Điều quan trọng**: Cấu trúc streaming của Responses API (`event.type` + `event.delta`) hoàn toàn khác với Chat Completions (`chunk.choices[0].delta.content`). Nhưng hợp đồng backend đến frontend là do bạn định nghĩa. Hãy tạo đầu ra backend phù hợp với mong đợi hiện tại của frontend.

## Chuỗi sự kiện streaming

Khi `stream: true`, API phát các sự kiện theo thứ tự này:
1. `response.created` – đối tượng response được khởi tạo
2. `response.in_progress` – bắt đầu tạo kết quả
3. `response.output_item.added` – mục output được tạo
4. `response.content_part.added` – bắt đầu phần nội dung
5. `response.output_text.delta` – các đoạn text (nhiều đoạn, mỗi đoạn có `delta: string`)
6. `response.output_text.done` – kết thúc tạo text
7. `response.content_part.done` – phần nội dung kết thúc
8. `response.output_item.done` – mục output kết thúc
9. `response.completed` – hoàn thành toàn bộ response

Đối với streaming văn bản cơ bản, chỉ cần xử lý `response.output_text.delta` (các đoạn text) và `response.completed` (kết thúc).

## Xử lý lỗi streaming trong các app web

Khi streaming trong app web, bọc vòng lặp async trong khối `try/except` và trả về lỗi dạng JSON để frontend có thể hiện thông báo đẹp mắt (ví dụ lỗi giới hạn tốc độ, lỗi tạm thời):

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

> **Tại sao quan trọng**: Azure OpenAI trả về `429 Too Many Requests` khi giới hạn tốc độ. Nếu không có `try/except`, streaming sẽ kết thúc im lặng. Với nó, frontend nhận được `{"error": "Too Many Requests"}` và có thể hiển thị yêu cầu thử lại.

## Các loại sự kiện streaming (Python SDK)

- `ResponseTextDeltaEvent`: `type='response.output_text.delta'`, `delta: str`
- `ResponseCompletedEvent`: `type='response.completed'`, `response: Response`

## Định dạng hội thoại
```python
# API Phản hồi hỗ trợ định dạng hội thoại thông qua mảng đầu vào
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

## Xử lý lỗi bộ lọc nội dung

Cấu trúc lỗi thay đổi từ Chat Completions sang Responses API.

Trước (Chat Completions):
```python
except openai.APIError as error:
    if error.code == "content_filter":
        if error.body["innererror"]["content_filter_result"]["jailbreak"]["filtered"] is True:
            print("Jailbreak detected!")
```

Sau (Responses API):
```python
except openai.APIError as error:
    if error.code == "content_filter":
        if error.body["content_filters"][0]["content_filter_results"]["jailbreak"]["filtered"] is True:
            print("Jailbreak detected!")
```

Khác biệt chính:
- Bao bọc `innererror` **không còn nữa** — chi tiết lọc nội dung giờ nằm ở cấp trên cùng của `error.body`.
- `content_filter_result` (số ít) → `content_filters` (mảng số nhiều) chứa `content_filter_results` (số nhiều) bên trong từng phần tử.
- Mỗi phần tử trong `content_filters` bao gồm `blocked`, `source_type`, và `content_filter_results` với chi tiết theo từng loại (`jailbreak`, `hate`, `sexual`, `violence`, `self_harm`).

Cấu trúc đầy đủ của lỗi bộ lọc nội dung Responses API:
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

## Di chuyển raw HTTP (requests/httpx)

Nếu app gọi trực tiếp REST Azure OpenAI thay vì dùng SDK:

Trước (Chat Completions):
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

Sau (Responses API):
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

> **Lưu ý**: `output_text` là thuộc tính tiện lợi trong đối tượng `Response` của Python SDK. Phản hồi JSON REST thô không có trường `output_text` cấp cao — văn bản nằm ở `output[0].content[0].text`.

## Hội thoại nhiều vòng
```python
# Xây dựng một cuộc trò chuyện với Responses API
messages = [
    {"role": "system", "content": "You are a helpful coding assistant."},
    {"role": "user", "content": "Write a Python function to calculate factorial"},
]

response = client.responses.create(
    model=deployment,
    input=messages,
    max_output_tokens=400,
)

# Thêm phản hồi của trợ lý vào cuộc trò chuyện
messages.append({"role": "assistant", "content": response.output_text})

# Tiếp tục cuộc trò chuyện
messages.append({"role": "user", "content": "Now optimize it with memoization"})

response2 = client.responses.create(
    model=deployment,
    input=messages,
    max_output_tokens=400,
)
print(response2.output_text)
```

Hội thoại nhiều vòng theo kiểu gán loại nội dung (explicit `input_text`/`output_text`):
```python
messages = [
    {"role": "system", "content": [{"type": "input_text", "text": "You are helpful."}]},
    {"role": "user", "content": [{"type": "input_text", "text": "Hi"}]},
    {"role": "assistant", "content": [{"type": "output_text", "text": "Hello!"}]},
    {"role": "user", "content": [{"type": "input_text", "text": "Tell me a joke"}]},
]
resp = client.responses.create(model=deployment, input=messages, store=False)
```

### Nhiều vòng qua `previous_response_id` (cách khác)

Thay vì tự quản lý mảng hội thoại, bạn có thể xâu chuỗi các phản hồi
phía server bằng `previous_response_id`. API lưu trữ từng phản hồi và
tự động thêm các vòng trước vào.

```python
# Lượt đầu tiên
response = client.responses.create(
    model=deployment,
    input=[{"role": "user", "content": "Write a Python function to calculate factorial"}],
)
print(response.output_text)

# Các lượt tiếp theo — chỉ cần gửi tin nhắn người dùng mới + ID phản hồi trước đó
response2 = client.responses.create(
    model=deployment,
    input=[{"role": "user", "content": "Now optimize it with memoization"}],
    previous_response_id=response.id,
)
print(response2.output_text)
```

**Khi nào dùng cách nào:**

| Phương pháp | Ưu điểm | Nhược điểm |
|---|---|---|
| Mảng `input` (thủ công) | Kiểm soát đầy đủ lịch sử; có thể cắt/ngắn/gom tóm tắt; không cần lưu server (`store=False`) | Mã phức tạp hơn; bạn tự quản lý mảng |
| `previous_response_id` | Mã đơn giản hơn; tự động nối chuỗi | Cần `store=True` (mặc định); hội thoại lưu server; không thể sửa lịch sử giữa các vòng |

> **Lưu ý di chuyển:** Hầu hết app Chat Completions hiện tại quản lý mảng tin nhắn riêng, nên chuyển sang mảng `input` là di chuyển trực tiếp 1:1. Dùng `previous_response_id` cho code mới hoặc khi không cần thao tác lịch sử hội thoại.

## Các mô hình reasoning dòng O (o1, o3-mini, o3, o4-mini)

Mô hình dòng O có các giới hạn tham số đặc biệt khi di chuyển sang Responses API.

### Ánh xạ tham số cho dòng o

| Chat Completions (dòng o) | Responses API | Ghi chú |
|---|---|---|
| `max_completion_tokens` | `max_output_tokens` | Đặt cao (4096+) — token reasoning tính vào giới hạn |
| `reasoning_effort` | `reasoning.effort` | Giữ nguyên nếu có (low/medium/high) |
| `temperature` | Loại bỏ hoặc đặt `1` | Dòng o chỉ chấp nhận `1` |
| `top_p` | Loại bỏ | Không hỗ trợ trên dòng o |
| `seed` | Loại bỏ | Không hỗ trợ trong Responses API |

### Dòng O trước/sau

Trước (Chat Completions với dòng o):
```python
resp = client.chat.completions.create(
    model="o4-mini",
    messages=[{"role": "user", "content": "Solve this step by step: 2x + 5 = 13"}],
    max_completion_tokens=4096,
    reasoning_effort="medium",
)
print(resp.choices[0].message.content)
```

Sau (Responses API):
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

> **Lưu ý**: Mô hình dòng o có thể đệm đầu ra trong quá trình reasoning trước khi phát các delta text. Streaming vẫn hoạt động nhưng sự kiện `response.output_text.delta` đầu tiên có thể đến sau độ trễ dài hơn so với mô hình GPT.

## Truy cập token reasoning
```python
# Các mô hình lý luận sử dụng lý luận nội bộ — bạn có thể thấy được có bao nhiêu token lý luận đã được sử dụng
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

> **Quan trọng**: Sử dụng `max_output_tokens=1000` (không phải 50–200) để tính đến quá trình reasoning nội bộ của mô hình. Mô hình sử dụng token reasoning nội bộ trước khi sinh đầu ra cuối cùng.

## Đầu ra có cấu trúc — JSON Schema
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

## Sử dụng công cụ

- Định nghĩa hàm trong `tools` theo **định dạng Responses API phẳng** — `name`, `description`, và `parameters` ở cấp cao (không lồng dưới `function`).
- Khi mô hình yêu cầu gọi công cụ, thực thi trong app của bạn và bao gồm kết quả công cụ trong yêu cầu tiếp theo dưới dạng mục `function_call_output` trong `input`.
- Giữ schema tối giản; kiểm tra đầu vào trước khi thực thi.
- Khi dùng `strict: true`, tất cả các thuộc tính phải liệt kê trong `required` và `additionalProperties: false` là bắt buộc.

> **⚠️ `pydantic_function_tool()` không tương thích**: Hàm trợ giúp `openai.pydantic_function_tool()` vẫn tạo định dạng lồng cũ của Chat Completions (`{"type": "function", "function": {"name": ...}}`). Không dùng với `responses.create()`. Định nghĩa schema công cụ thủ công hoặc viết wrapper để làm phẳng đầu ra.

### Định dạng định nghĩa công cụ

Responses API sử dụng định dạng công cụ **phẳng** — `name`, `description`, `parameters` là các khóa cấp cao (không lồng dưới `function`).

**Trước (Chat Completions — lồng nhau):**
```python
tools = [{"type": "function", "function": {"name": "lookup_weather", "parameters": {...}}}]
```

**Sau (Responses API — phẳng):**
```python
tools = [{"type": "function", "name": "lookup_weather", "parameters": {...}}]
```

Ví dụ đầy đủ:
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

Với `strict: true` (bắt buộc schema):
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
            "required": ["city_name"],       # Tất cả các thuộc tính PHẢI được liệt kê
            "additionalProperties": False,   # Bắt buộc đối với chế độ nghiêm ngặt
        },
    }
]
```

### Vòng gọi công cụ (thực thi và trả kết quả)

Khi mô hình yêu cầu gọi công cụ, sử dụng các mục `response.output` + `function_call_output` — **không** sử dụng mẫu `role: assistant` + `role: tool` của Chat Completions.

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
    # Thêm các mục function_call của mô hình vào cuộc trò chuyện
    messages.extend(response.output)

    # Thực thi từng công cụ và thêm kết quả
    for tc in tool_calls:
        result = execute_tool(tc.name, json.loads(tc.arguments))
        messages.append({
            "type": "function_call_output",
            "call_id": tc.call_id,
            "output": json.dumps(result),
        })

    # Lấy phản hồi cuối cùng với kết quả công cụ
    response = client.responses.create(
        model=deployment, input=messages, tools=tools, store=False,
    )
    print(response.output_text)
```

### Ví dụ gọi công cụ theo vài lần thử

Khi cung cấp ví dụ gọi công cụ trong `input`, sử dụng các mục `function_call` và `function_call_output`. ID phải bắt đầu bằng `fc_`.

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
# Ví dụ tìm kiếm web tích hợp sẵn
resp = client.responses.create(
    model=deployment,
    tools=[{"type": "web_search_preview"}],
    input="What was a positive news story from today?",
    store=False,
)
print(resp.output_text)
```

## Đầu vào hình ảnh

Các mục nội dung hình ảnh đổi type từ `image_url` sang `input_image`, và URL chuyển từ đối tượng lồng sang chuỗi phẳng.

### Đầu vào hình ảnh — trước (Chat Completions)
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

### Đầu vào hình ảnh — sau (Responses API, URL)
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

### Đầu vào hình ảnh — sau (Responses API, base64)
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

> **Thay đổi chính**: (1) `"type": "image_url"` → `"type": "input_image"`, (2) `"image_url": {"url": "..."}` (đối tượng lồng) → `"image_url": "..."` (chuỗi phẳng — hoặc URL HTTPS hoặc URI dữ liệu base64 `data:image/...;base64,...`), (3) `"type": "text"` → `"type": "input_text"`.

## Di chuyển Microsoft Agent Framework (MAF)

**Kiểm tra phiên bản MAF của bạn trước** — di chuyển phụ thuộc vào việc bạn dùng MAF 1.0.0+ hay beta/rc trước 1.0.0.

Để kiểm tra: `python -c "import agent_framework_openai; print(agent_framework_openai.__version__)"`

### MAF 1.0.0+ (agent-framework-openai >= 1.0.0)

Trong MAF 1.0.0+, `OpenAIChatClient` **đã dùng Responses API** — không cần di chuyển.

Nếu codebase dùng `OpenAIChatCompletionClient` cũ (dùng `chat.completions.create`), thay bằng `OpenAIChatClient`:

Trước:
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

Sau:
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

### MAF trước 1.0.0 (phiên bản beta/rc)

Trong MAF trước 1.0.0, `OpenAIChatClient` dùng Chat Completions. Nâng cấp lên `agent-framework-openai>=1.0.0` để `OpenAIChatClient` mặc định dùng Responses API.

> **Lưu ý**: Các API `Agent`, `MCPStreamableHTTPTool` và các API MAF khác không đổi — chỉ import và khởi tạo lớp client thay đổi.

## Di chuyển LangChain (`langchain-openai`)

Thêm `use_responses_api=True` vào `ChatOpenAI()`. Cập nhật truy cập nội dung tin nhắn từ `.content` sang `.text`.

Trước:
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

# ... gọi tác nhân ...
result = await agent.ainvoke({"messages": [HumanMessage(content=query)]})
print(result['messages'][-1].content)
```

Sau:
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

# ... gọi agent ...
result = await agent.ainvoke({"messages": [HumanMessage(content=query)]})
print(result['messages'][-1].text)
```

> **Thay đổi chính**: (1) `use_responses_api=True` trong hàm tạo, (2) `.content` → `.text` trên các tin nhắn phản hồi.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Tuyên bố miễn trừ trách nhiệm**:
Tài liệu này đã được dịch bằng dịch vụ dịch thuật AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mặc dù chúng tôi cố gắng đảm bảo độ chính xác, xin lưu ý rằng bản dịch tự động có thể chứa lỗi hoặc sai sót. Tài liệu gốc bằng ngôn ngữ gốc nên được coi là nguồn tin chính thức. Đối với thông tin quan trọng, nên sử dụng dịch vụ dịch thuật chuyên nghiệp bởi con người. Chúng tôi không chịu trách nhiệm về bất kỳ hiểu lầm hoặc giải thích sai nào phát sinh từ việc sử dụng bản dịch này.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->