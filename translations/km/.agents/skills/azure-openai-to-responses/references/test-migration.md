# ការផ្លាស់ប្តូររចនាសម្ព័ន្ធតេស្ត

នៅពេលផ្លាស់ប្តូរមូលដ្ឋានកូដពី Chat Completions ទៅ Responses API, **តេស្តឆ្អែតដោយរបៀបដែលអាចទាយបាន**។ ឯកសារដែលយោងនេះគ្របដណ្តប់អ្វីដែលត្រូវជួសជុល។

---

## ការបង្កើត Mock Streaming Responses (Python pytest)

### ថ្នាក់ mock សំខាន់ៗ

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
            # រក្សាទុកចន្លោះ: បន្ថែមចន្លោះទៅជាការប្រកួតទាំងអស់លើកលែងតែពាក្យដំបូង
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

### ការបង្វិល mock responses ដោយអាស្រ័យលើមាតិកាសារ

ពφαρកម្មពិតបម្រើចម្លើយខុសគ្នាពីមូលដ្ឋានលើ prompt។ បង្វិលដោយ `input` (មិនមែន `messages`)៖

```python
async def mock_acreate(*args, **kwargs):
    # Responses API ប្រើ 'input' មិនមែន 'messages' នោះទេ
    last_message = kwargs.get("input", [])[-1]["content"]
    if last_message == "What is the capital of France?":
        return AsyncResponseIterator("The capital of France is Paris.")
    elif last_message == "What is the capital of Germany?":
        return AsyncResponseIterator("The capital of Germany is Berlin.")
    else:
        raise ValueError(f"Unexpected message: {last_message}")
```

### ផ្លូវ Monkeypatch

| ប្រភេទអតិថិជន | ផ្លូវ Monkeypatch |
|-------------|------------------|
| `AsyncOpenAI` | `openai.resources.responses.AsyncResponses.create` |
| `OpenAI` (sync) | `openai.resources.responses.Responses.create` |

> **មុន** (Chat Completions): `openai.resources.chat.AsyncCompletions.create`
> **បន្ទាប់** (Responses): `openai.resources.responses.AsyncResponses.create`

### ឧទាហរណ៍ fixture ពេញលេញ

```python
@pytest.fixture
def mock_openai_responses(monkeypatch):
    # ... ក្លាស MockResponseEvent និង AsyncResponseIterator នៅទីនេះ ...

    async def mock_acreate(*args, **kwargs):
        last_message = kwargs.get("input", [])[-1]["content"]
        if last_message == "What is the capital of France?":
            return AsyncResponseIterator("The capital of France is Paris.")
        else:
            raise ValueError(f"Unexpected message: {last_message}")

    monkeypatch.setattr("openai.resources.responses.AsyncResponses.create", mock_acreate)
```

---

## 1. បន្ទាន់សម័យ mock fixtures

ជំនួស mocks រៀបចំបែប `ChatCompletionChunk` ដោយរចនាបែប `MockResponseEvent` / `AsyncResponseIterator` ខាងលើ។ ជំនួសសំខាន់ៗ៖

| មុន (Chat Completions mock) | បន្ទាប់ (Responses mock) |
|-------------------------------|------------------------|
| `openai.types.chat.ChatCompletionChunk(...)` | `MockResponseEvent(event_type, delta)` |
| `choices[0].delta.content` | `event.delta` |
| `finish_reason="stop"` ក្នុង chunk | `event.type == "response.completed"` |
| chunk ជាក់លាក់ Azure `prompt_filter_results` | លុបចោលទាំងស្រុង |
| ជ្រើសរើសជាក់លាក់ Azure `content_filter_results` | លុបចោលទាំងស្រុង |
| `kwargs.get("messages")` ក្នុង mock | `kwargs.get("input")` ក្នុង mock |

---

## 2. បន្ទាន់សម័យ snapshot / ឯកសារសំឡេងមាស

ប្រសិនបើសំណុំតេស្តប្រើតេស្ត snapshot (ដូចជា `pytest-snapshot`, syrupy, ឬ snapshot JSONL ដោយដៃ), រចនាប័ទ្មលទ្ធផលដែលរំពឹងទុកបានផ្លាស់ប្តូរ៖

**មុន** (Chat Completions streaming JSONL):
```jsonl
{"delta": {"content": null, "function_call": null, "refusal": null, "role": "assistant", "tool_calls": null}, "finish_reason": null, "index": 0, "logprobs": null, "content_filter_results": {}}
{"delta": {"content": "The", "function_call": null, "refusal": null, "role": null, "tool_calls": null}, "finish_reason": null, "index": 0, "logprobs": null, "content_filter_results": {"hate": {"filtered": false, "severity": "safe"}, ...}}
{"delta": {"content": null, ...}, "finish_reason": "stop", "index": 0, "logprobs": null, "content_filter_results": {}}
```

**បន្ទាប់** (Responses API streaming JSONL):
```jsonl
{"delta": {"content": "The"}}
{"delta": {"content": " capital"}}
{"delta": {"content": null}, "finish_reason": "stop"}
```

ទម្រង់ថ្មីសាមញ្ញជាងគេ — គ្មានវាល `function_call`, `refusal`, `role`, `tool_calls`, `index`, `logprobs`, ឬ `content_filter_results` ទៀត។ បន្ទាន់សម័យ ឬ បង្កើតឡើងវិញឯកសារ snapshot ទាំងអស់។

> **គន្លឹះ**៖ រត់តេស្តជាមួយ `--snapshot-update` (pytest-snapshot) ឬ `--update-snapshots` (syrupy) បន្ទាប់ពីផ្លាស់ប្ដូរដើម្បីបង្កើតឡើងវិញអូតូម៉ាទិក។

---

## 3. បន្ទាន់សម័យការបញ្ជាក់តេស្ត

ការបែកបាក់នៃការបញ្ជាក់ដែលមានន័យសាកលវិទ្យា៖

| ការបញ្ជាក់ចាស់ | បញ្ហា | ការបញ្ជាក់ថ្មី |
|--------------|---------|---------------|
| `client._azure_ad_token_provider is not None` | `AsyncOpenAI` មិនមានគុណលក្ខណៈ `_azure_ad_token_provider` | `isinstance(client, AsyncOpenAI)` និង `"/openai/v1/" នៅក្នុង str(client.base_url)` |
| `client.api_version == "2024-..."` | គ្មាន `api_version` លើ `OpenAI`/`AsyncOpenAI` | លុបចោលទាំងស្រុង |
| `isinstance(client, AsyncAzureOpenAI)` | ប្រភេទអតិថិជនផ្លាស់ប្តូរ | `isinstance(client, AsyncOpenAI)` |

---

## 4. បន្ទាន់សម័យអថេរស្ថានបរិដ្ឋានក្នុង fixture តេស្ត

តេស្តស្ថិតនៅជាច្រើនកំណត់អថេរស្ថានបរិដ្ឋានតាមរយៈ `monkeypatch.setenv`។ បន្ទាន់សម័យទាំងនេះ៖

| អថេរស្ថានបរិដ្ឋានចាស់ | អថេរស្ថានបរិដ្ឋានថ្មី | កំណត់ខ្លឹមសារ |
|-------------|-------------|-------|
| `AZURE_OPENAI_CLIENT_ID` | `AZURE_CLIENT_ID` | ប្រពៃណី SDK មូលដ្ឋានអត្តសញ្ញាណ Azure ផ្លូវការជាមួយ |
| `AZURE_OPENAI_VERSION` | លុប | មិនត្រូវការចំពោះ `api_version` |
| `AZURE_OPENAI_API_VERSION` | លុប | មិនត្រូវការចំពោះ `api_version` |
| `AZURE_OPENAI_ENDPOINT` | `AZURE_OPENAI_ENDPOINT` | រក្សាទុក (ត្រូវការសម្រាប់ `base_url`) |
| `AZURE_OPENAI_CHAT_DEPLOYMENT` | `AZURE_OPENAI_CHAT_DEPLOYMENT` | រក្សាទុក (ឈ្មោះ deployment សម្រាប់ប៉ារ៉ាម៉ែត្រ `model`) |

---

## 5. ស្វែងរកកូដតេស្តដែលត្រូវផ្លាស់ប្តូរ

```bash
# លំនាំបុរាណជាក់លាក់សម្រាប់ការប្រឡង
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
**ការបដិសេធ**:
ឯកសារនេះត្រូវបានបម្លែងភាសា ដោយប្រើសេវាបម្លែងភាសា AI [Co-op Translator](https://github.com/Azure/co-op-translator)។ ទោះយើងខ្ញុំមានក្តីប្រាថ្នាឱ្យបានច្បាស់លាស់ តែសូមយល់ដឹងថាការបម្លែងដោយស្វ័យប្រវត្តិក៏អាចមានកំហុសឬភាពមិនត្រឹមត្រូវ។ ឯកសារដើមជាភាសាទីតាំងគួរត្រូវបានគេប្រើជាប្រភពច្បាស់លាស់។ សម្រាប់ព័ត៌មានសំខាន់ៗ សូមណែនាំឱ្យប្រើប្រាស់ការប្រែដោយមនុស្សជំនាញ។ យើងខ្ញុំមិនទទួលខុសត្រូវចំពោះការយល់ច្រឡំ ឬការបកស្រាយខុសបន្ទាប់ពីការប្រើប្រាស់ការបម្លែងនេះនោះទេ។
<!-- CO-OP TRANSLATOR DISCLAIMER END -->