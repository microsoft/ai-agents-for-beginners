# Bảng tóm tắt Responses API (Python + Azure OpenAI)

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

## Thiết lập client — EntraID (được khuyến nghị)
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

Khi tài nguyên Azure OpenAI nằm trong **tenant khác** với tenant mặc định, hãy truyền `tenant_id` rõ ràng vào thông tin đăng nhập. Điều này thường gặp trong các kịch bản phát triển/kiểm thử khi tenant chính của nhà phát triển khác với tenant tài nguyên.

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
    client_id=os.getenv("AZURE_CLIENT_ID")  # Managed identity được gán cho người dùng
)
# AzureDeveloperCliCredential cho phát triển cục bộ — tenant_id rõ ràng là rất quan trọng
azd_cred = AzureDeveloperCliCredential(
    tenant_id=os.getenv("AZURE_TENANT_ID"),
    process_timeout=60,
)
# Chuỗi: thử managed identity trước, nếu không thành công thì chuyển sang azd CLI
azure_credential = ChainedTokenCredential(managed_identity_cred, azd_cred)

token_provider = get_bearer_token_provider(
    azure_credential, "https://cognitiveservices.azure.com/.default"
)

client = AsyncOpenAI(
    base_url=f"{os.environ['AZURE_OPENAI_ENDPOINT'].rstrip('/')}/openai/v1/",
    api_key=token_provider,
)
```

## Di trú client bất đồng bộ — trước/sau

Trước (không còn dùng nữa):
```python
from openai import AsyncAzureOpenAI

client = AsyncAzureOpenAI(
    api_version=os.environ["AZURE_OPENAI_API_VERSION"],
    azure_endpoint=os.environ["AZURE_OPENAI_ENDPOINT"],
    azure_ad_token_provider=token_provider,
)

resp = await client.chat.completions.create(
    model="gpt-4o",
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

## Di trú đồng bộ đầy đủ — trước/sau

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
    model="gpt-4o",
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

## Truyền phát (đồng bộ)
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

## Truyền phát (bất đồng bộ)
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

## Truyền phát ứng dụng web — hình thức backend tới frontend

Khi di trú một ứng dụng web truyền SSE/JSONL tới frontend, **định dạng tuần tự của backend** thay đổi. Hãy thiết kế đầu ra backend mới để giữ nguyên mẫu truy cập hiện có của frontend nhằm frontend không cần thay đổi.

**Trước** — Backend Chat Completions thường tuần tự hóa dict `choices[0]` của mỗi chunk:
```python
# Cũ: từ điển lựa chọn đầy đủ được tuần tự hóa cho mỗi phần nhỏ
async for chunk in response:
    if chunk.choices:
        yield json.dumps(chunk.choices[0].model_dump()) + "\n"
```
Frontend đọc: `response.delta.content` (đường sâu vào đối tượng choice).

**Sau** — Backend Responses API phát ra một hình thức tối giản bảo toàn con đường truy cập frontend hiện có:
```python
# Mới: chỉ phát ra những gì frontend cần
async for event in await chat_coroutine:
    if event.type == "response.output_text.delta":
        yield json.dumps({"delta": {"content": event.delta}}) + "\n"
    elif event.type == "response.completed":
        yield json.dumps({"delta": {"content": None}, "finish_reason": "stop"}) + "\n"
```
Frontend vẫn đọc `response.delta.content` — **không cần thay đổi frontend**.

> **Điều quan trọng**: Hình thức truyền phát của Responses API (`event.type` + `event.delta`) căn bản khác so với Chat Completions (`chunk.choices[0].delta.content`). Nhưng hợp đồng backend tới frontend do bạn định nghĩa. Hãy tạo hình đầu ra backend khớp với điều frontend đã mong đợi.

## Chuỗi sự kiện truyền phát

Khi `stream: true`, API phát các sự kiện theo thứ tự:
1. `response.created` – đối tượng response được khởi tạo
2. `response.in_progress` – quá trình sinh bắt đầu
3. `response.output_item.added` – tạo mục đầu ra
4. `response.content_part.added` – bắt đầu phần nội dung
5. `response.output_text.delta` – các đoạn văn bản (nhiều đoạn, mỗi đoạn có `delta: string`)
6. `response.output_text.done` – kết thúc sinh văn bản
7. `response.content_part.done` – kết thúc phần nội dung
8. `response.output_item.done` – kết thúc mục đầu ra
9. `response.completed` – hoàn tất phản hồi

Với truyền phát văn bản cơ bản, chỉ xử lý `response.output_text.delta` (để nhận các đoạn văn bản) và `response.completed` (kết thúc).

## Xử lý lỗi truyền phát trong ứng dụng web

Khi truyền phát trong ứng dụng web, hãy dùng vòng lặp async trong khối `try/except` và phát lỗi dưới dạng JSON để frontend có thể hiển thị một cách đẹp mắt (ví dụ: giới hạn tỷ lệ, lỗi tạm thời):

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

> **Tại sao điều này quan trọng**: Azure OpenAI trả về `429 Too Many Requests` khi giới hạn tần suất gọi. Nếu không có `try/except`, phản hồi truyền phát sẽ kết thúc âm thầm. Với nó, frontend nhận được `{"error": "Too Many Requests"}` và có thể hiển thị gợi ý thử lại.

## Các loại sự kiện truyền phát (Python SDK)

- `ResponseTextDeltaEvent`: `type='response.output_text.delta'`, `delta: str`
- `ResponseCompletedEvent`: `type='response.completed'`, `response: Response`

## Định dạng cuộc hội thoại
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

Cấu trúc lỗi đã thay đổi từ Chat Completions sang Responses API.

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

Các điểm khác biệt chính:
- bọc `innererror` **đã biến mất** — chi tiết bộ lọc nội dung giờ ở ngay cấp cao của `error.body`.
- `content_filter_result` (số ít) → `content_filters` (mảng số nhiều) chứa các `content_filter_results` (số nhiều) bên trong mỗi mục.
- Mỗi mục trong `content_filters` bao gồm `blocked`, `source_type`, và `content_filter_results` với chi tiết theo từng loại (`jailbreak`, `hate`, `sexual`, `violence`, `self_harm`).

Cấu trúc đầy đủ của phần lỗi bộ lọc nội dung Responses API:
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

## Di trú HTTP thô (requests/httpx)

Nếu ứng dụng gọi trực tiếp REST Azure OpenAI thay vì dùng SDK:

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

> **Lưu ý**: `output_text` là thuộc tính tiện lợi của đối tượng `Response` trong Python SDK. Phản hồi JSON REST thô không có trường cấp cao `output_text` — văn bản nằm trong `output[0].content[0].text`.

## Cuộc hội thoại đa lượt
```python
# Xây dựng cuộc trò chuyện với API Responses
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

Cuộc hội thoại đa lượt có định kiểu nội dung (rõ ràng `input_text`/`output_text`):
```python
messages = [
    {"role": "system", "content": [{"type": "input_text", "text": "You are helpful."}]},
    {"role": "user", "content": [{"type": "input_text", "text": "Hi"}]},
    {"role": "assistant", "content": [{"type": "output_text", "text": "Hello!"}]},
    {"role": "user", "content": [{"type": "input_text", "text": "Tell me a joke"}]},
]
resp = client.responses.create(model=deployment, input=messages, store=False)
```

### Đa lượt qua `previous_response_id` (cách thay thế)

Thay vì tự quản lý mảng cuộc hội thoại, bạn có thể xâu chuỗi các phản hồi phía máy chủ
bằng `previous_response_id`. API lưu trữ từng phản hồi và
tự động thêm các lượt trước.

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

| Cách tiếp cận | Ưu điểm | Nhược điểm |
|---|---|---|
| Mảng `input` (thủ công) | Toàn quyền kiểm soát lịch sử; có thể cắt/gộp tóm tắt; không cần lưu máy chủ (`store=False`) | Mã phức tạp hơn; bạn phải quản lý mảng |
| `previous_response_id` | Mã đơn giản; xâu chuỗi tự động | Yêu cầu `store=True` (mặc định); cuộc hội thoại lưu trên máy chủ; không thể sửa lịch sử giữa các lượt |

> **Lưu ý di trú:** Hầu hết ứng dụng Chat Completions đã tự quản lý mảng tin nhắn, nên chuyển sang mảng `input` là di trú trực tiếp 1:1 hơn. Dùng `previous_response_id` cho mã mới hoặc khi không cần thao tác lịch sử hội thoại.

## Mô hình suy luận dòng O (o1, o3-mini, o3, o4-mini)

Các mô hình dòng O có ràng buộc tham số riêng khi di trú sang Responses API.

### Bản đồ tham số cho dòng O

| Chat Completions (dòng O) | Responses API | Ghi chú |
|---|---|---|
| `max_completion_tokens` | `max_output_tokens` | Để cao (4096+) — token suy luận tính vào giới hạn |
| `reasoning_effort` | `reasoning.effort` | Giữ nguyên nếu có (thấp/trung bình/cao) |
| `temperature` | Xóa hoặc đặt thành `1` | Dòng O chỉ chấp nhận `1` |
| `top_p` | Xóa | Không hỗ trợ trên dòng O |
| `seed` | Xóa | Không hỗ trợ trong Responses API |

### Dòng O trước/sau

Trước (Chat Completions với dòng O):
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

> **Lưu ý**: Các mô hình dòng O có thể đệm đầu ra trong quá trình suy luận trước khi phát các delta văn bản. Truyền phát vẫn hoạt động nhưng sự kiện đầu tiên `response.output_text.delta` có thể đến muộn hơn so với mô hình GPT.

## Truy cập token suy luận
```python
# Mô hình suy luận sử dụng suy luận nội bộ — bạn có thể thấy có bao nhiêu token suy luận đã được sử dụng
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

> **Quan trọng**: Dùng `max_output_tokens=1000` (không phải 50–200) để tính đến quá trình suy luận nội bộ của mô hình suy luận. Mô hình sử dụng token suy luận bên trong trước khi sinh ra đầu ra cuối cùng.

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

- Định nghĩa các hàm trong `tools` với **định dạng Responses API phẳng** — `name`, `description`, và `parameters` ở cấp trên (không lồng trong `function`).
- Khi mô hình yêu cầu gọi công cụ, thực thi nó trong ứng dụng của bạn và bao gồm kết quả công cụ trong yêu cầu kế tiếp dưới dạng mục `function_call_output` trong `input`.
- Giữ schema đơn giản; xác thực đầu vào trước khi thực thi.
- Khi dùng `strict: true`, tất cả thuộc tính phải liệt kê trong `required` và `additionalProperties: false` là bắt buộc.

> **⚠️ `pydantic_function_tool()` không tương thích**: Helper `openai.pydantic_function_tool()` vẫn tạo định dạng lồng Chat Completions cũ (`{"type": "function", "function": {"name": ...}}`). Không dùng nó với `responses.create()`. Định nghĩa schema công cụ thủ công hoặc viết wrapper để phẳng hóa đầu ra.

### Định dạng định nghĩa công cụ

Responses API dùng định dạng công cụ **phẳng** — `name`, `description`, `parameters` là khóa cấp trên (không lồng trong `function`).

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
            "additionalProperties": False,   # Bắt buộc cho chế độ nghiêm ngặt
        },
    }
]
```

### Vòng gọi công cụ (thực thi và trả kết quả)

Khi mô hình yêu cầu gọi công cụ, dùng các mục `response.output` + `function_call_output` — **không dùng** mô hình Chat Completions với pattern `role: assistant` + `role: tool`.

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

### Ví dụ gọi công cụ ít mẫu

Khi cung cấp ví dụ gọi công cụ ít mẫu trong `input`, dùng mục `function_call` và `function_call_output`. ID phải bắt đầu bằng `fc_`.

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

Mục nội dung hình ảnh thay đổi loại từ `image_url` thành `input_image`, và URL thay đổi từ đối tượng lồng vào chuỗi phẳng.

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

> **Thay đổi quan trọng**: (1) `"type": "image_url"` → `"type": "input_image"`, (2) `"image_url": {"url": "..."}` (đối tượng lồng) → `"image_url": "..."` (chuỗi phẳng — hoặc URL HTTPS hoặc URI dữ liệu `data:image/...;base64,...`), (3) `"type": "text"` → `"type": "input_text"`.

## Di trú Microsoft Agent Framework (MAF)

**Kiểm tra phiên bản MAF trước** — việc di trú phụ thuộc bạn đang dùng MAF 1.0.0+ hay beta/rc pre-1.0.0.

Để kiểm tra: `python -c "import agent_framework_openai; print(agent_framework_openai.__version__)"`

### MAF 1.0.0+ (agent-framework-openai >= 1.0.0)

Trong MAF 1.0.0+, `OpenAIChatClient` **đã dùng Responses API** — không cần di trú.

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

### MAF pre-1.0.0 (bản beta/rc)

Trong pre-1.0.0 MAF, `OpenAIChatClient` dùng Chat Completions. Nâng cấp lên `agent-framework-openai>=1.0.0` khi `OpenAIChatClient` mặc định dùng Responses API.

> **Lưu ý**: Các API `Agent`, `MCPStreamableHTTPTool`, và các API MAF khác không đổi — chỉ thay nhập khẩu và khởi tạo client.

## Di trú LangChain (`langchain-openai`)

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

# ... gọi đại lý ...
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

# ... gọi tác nhân ...
result = await agent.ainvoke({"messages": [HumanMessage(content=query)]})
print(result['messages'][-1].text)
```

> **Thay đổi quan trọng**: (1) `use_responses_api=True` trong hàm tạo, (2) `.content` → `.text` trên tin nhắn phản hồi.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Tuyên bố miễn trừ trách nhiệm**:
Tài liệu này đã được dịch bằng dịch vụ dịch thuật AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mặc dù chúng tôi cố gắng đảm bảo độ chính xác, xin lưu ý rằng bản dịch tự động có thể chứa lỗi hoặc sai sót. Tài liệu gốc bằng ngôn ngữ gốc nên được coi là nguồn tin chính thức. Đối với thông tin quan trọng, nên sử dụng dịch vụ dịch thuật chuyên nghiệp bởi con người. Chúng tôi không chịu trách nhiệm về bất kỳ hiểu lầm hoặc giải thích sai nào phát sinh từ việc sử dụng bản dịch này.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->