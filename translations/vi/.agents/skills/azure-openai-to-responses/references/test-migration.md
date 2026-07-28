# Di chuyển Cơ sở Hạ tầng Kiểm thử

Khi di chuyển codebase từ Chat Completions sang Responses API, **kiểm thử sẽ phá vỡ theo những cách có thể dự đoán được**. Tài liệu tham khảo này đề cập những gì cần sửa.

---

## Giả lập Streaming Responses (Python pytest)

### Các lớp mock cốt lõi

```python
class MockResponseEvent:
    """Simulates a Responses API streaming event."""
    def __init__(self, event_type: str, delta: str | None = None):
        self.type = event_type
        self.delta = delta

class AsyncResponseIterator:
    """Async iterator that yields Responses API streaming events from a string answer."""
    def __init__(self, answer: str):
        self.event_index = 0
        self.events = []
        for i, word in enumerate(answer.split(" ")):
            # Giữ khoảng trắng: thêm dấu cách vào tất cả các từ ngoại trừ từ đầu tiên
            if i > 0:
                word = " " + word
            self.events.append(MockResponseEvent("response.output_text.delta", delta=word))
        self.events.append(MockResponseEvent("response.completed"))

    def __aiter__(self):
        return self

    async def __anext__(self):
        if self.event_index < len(self.events):
            event = self.events[self.event_index]
            self.event_index += 1
            return event
        raise StopAsyncIteration
```

### Phân luồng câu trả lời giả lập theo nội dung tin nhắn

Các ứng dụng thực tế phục vụ câu trả lời khác nhau dựa trên lời nhắc. Phân luồng theo `input` (không phải `messages`):

```python
async def mock_acreate(*args, **kwargs):
    # API Responses sử dụng 'input' chứ không phải 'messages'
    last_message = kwargs.get("input", [])[-1]["content"]
    if last_message == "What is the capital of France?":
        return AsyncResponseIterator("The capital of France is Paris.")
    elif last_message == "What is the capital of Germany?":
        return AsyncResponseIterator("The capital of Germany is Berlin.")
    else:
        raise ValueError(f"Unexpected message: {last_message}")
```

### Đường dẫn monkeypatch

| Loại client | Đường dẫn monkeypatch |
|-------------|-----------------------|
| `AsyncOpenAI` | `openai.resources.responses.AsyncResponses.create` |
| `OpenAI` (đồng bộ) | `openai.resources.responses.Responses.create` |

> **Trước đây** (Chat Completions): `openai.resources.chat.AsyncCompletions.create`
> **Sau đây** (Responses): `openai.resources.responses.AsyncResponses.create`

### Ví dụ đầy đủ về fixture

```python
@pytest.fixture
def mock_openai_responses(monkeypatch):
    # ... Lớp MockResponseEvent và AsyncResponseIterator ở đây ...

    async def mock_acreate(*args, **kwargs):
        last_message = kwargs.get("input", [])[-1]["content"]
        if last_message == "What is the capital of France?":
            return AsyncResponseIterator("The capital of France is Paris.")
        else:
            raise ValueError(f"Unexpected message: {last_message}")

    monkeypatch.setattr("openai.resources.responses.AsyncResponses.create", mock_acreate)
```

---

## 1. Cập nhật fixture giả lập

Thay thế các mock dựa trên `ChatCompletionChunk` bằng kiểu mẫu `MockResponseEvent` / `AsyncResponseIterator` đã trình bày ở trên. Thay đổi chính:

| Trước đây (mock Chat Completions) | Sau đây (mock Responses) |
|-----------------------------------|-------------------------|
| `openai.types.chat.ChatCompletionChunk(...)` | `MockResponseEvent(event_type, delta)` |
| `choices[0].delta.content` | `event.delta` |
| `finish_reason="stop"` trong chunk | `event.type == "response.completed"` |
| chunk `prompt_filter_results` riêng cho Azure | Xóa hoàn toàn |
| `content_filter_results` riêng cho Azure trên mỗi lựa chọn | Xóa hoàn toàn |
| `kwargs.get("messages")` trong mock | `kwargs.get("input")` trong mock |

---

## 2. Cập nhật snapshot / file golden

Nếu bộ kiểm thử sử dụng kiểm thử snapshot (ví dụ: `pytest-snapshot`, syrupy, hoặc snapshot JSONL tự làm), hình dạng đầu ra mong đợi sẽ thay đổi:

**Trước đây** (Chat Completions streaming JSONL):
```jsonl
{"delta": {"content": null, "function_call": null, "refusal": null, "role": "assistant", "tool_calls": null}, "finish_reason": null, "index": 0, "logprobs": null, "content_filter_results": {}}
{"delta": {"content": "The", "function_call": null, "refusal": null, "role": null, "tool_calls": null}, "finish_reason": null, "index": 0, "logprobs": null, "content_filter_results": {"hate": {"filtered": false, "severity": "safe"}, ...}}
{"delta": {"content": null, ...}, "finish_reason": "stop", "index": 0, "logprobs": null, "content_filter_results": {}}
```

**Sau đây** (Responses API streaming JSONL):
```jsonl
{"delta": {"content": "The"}}
{"delta": {"content": " capital"}}
{"delta": {"content": null}, "finish_reason": "stop"}
```

Hình dạng mới đơn giản hơn rất nhiều — không có các trường `function_call`, `refusal`, `role`, `tool_calls`, `index`, `logprobs`, hoặc `content_filter_results`. Cập nhật hoặc tái tạo lại mọi file snapshot.

> **Mẹo**: Chạy kiểm thử với `--snapshot-update` (pytest-snapshot) hoặc `--update-snapshots` (syrupy) sau khi di chuyển để tự động tái tạo.

---

## 3. Cập nhật các khẳng định kiểm thử

Những lỗi phổ biến trong các khẳng định:

| Khẳng định cũ | Vấn đề | Khẳng định mới |
|--------------|---------|---------------|
| `client._azure_ad_token_provider is not None` | `AsyncOpenAI` không có thuộc tính `_azure_ad_token_provider` | `isinstance(client, AsyncOpenAI)` và `"/openai/v1/" in str(client.base_url)` |
| `client.api_version == "2024-..."` | Không có `api_version` trên `OpenAI`/`AsyncOpenAI` | Xóa hoàn toàn |
| `isinstance(client, AsyncAzureOpenAI)` | Loại client thay đổi | `isinstance(client, AsyncOpenAI)` |

---

## 4. Cập nhật biến môi trường trong fixture kiểm thử

Các kiểm thử thường thiết lập biến môi trường qua `monkeypatch.setenv`. Cập nhật chúng:

| Biến môi trường cũ | Biến môi trường mới | Ghi chú |
|--------------------|---------------------|---------|
| `AZURE_OPENAI_CLIENT_ID` | `AZURE_CLIENT_ID` | Quy ước chuẩn của Azure Identity SDK |
| `AZURE_OPENAI_VERSION` | Xóa | Không cần `api_version` |
| `AZURE_OPENAI_API_VERSION` | Xóa | Không cần `api_version` |
| `AZURE_OPENAI_ENDPOINT` | `AZURE_OPENAI_ENDPOINT` | Giữ lại (vẫn cần cho `base_url`) |
| `AZURE_OPENAI_CHAT_DEPLOYMENT` | `AZURE_OPENAI_CHAT_DEPLOYMENT` | Giữ lại (tên deployment cho tham số `model`) |

---

## 5. Tìm mã kiểm thử cần di chuyển

```bash
# Các mẫu kế thừa riêng cho kiểm thử
rg "ChatCompletionChunk" tests/
rg "AsyncCompletions\.create" tests/
rg "chat\.completions" tests/
rg "_azure_ad_token_provider" tests/
rg "prompt_filter_results" tests/
rg "content_filter_results" tests/
rg "AZURE_OPENAI_VERSION|AZURE_OPENAI_API_VERSION" tests/
rg "AZURE_OPENAI_CLIENT_ID" tests/
```

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Tuyên bố miễn trừ trách nhiệm**:
Tài liệu này đã được dịch bằng dịch vụ dịch thuật AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mặc dù chúng tôi cố gắng đảm bảo độ chính xác, xin lưu ý rằng bản dịch tự động có thể chứa lỗi hoặc sai sót. Tài liệu gốc bằng ngôn ngữ gốc nên được coi là nguồn tin chính thức. Đối với thông tin quan trọng, nên sử dụng dịch vụ dịch thuật chuyên nghiệp bởi con người. Chúng tôi không chịu trách nhiệm về bất kỳ hiểu lầm hoặc giải thích sai nào phát sinh từ việc sử dụng bản dịch này.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->