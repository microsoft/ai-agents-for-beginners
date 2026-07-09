# ការផ្លាស់ប្តូរនៅក្នុងហេដ្ឋារចនាសម្ព័ន្ធសាកល្បង

នៅពេលផ្ទេរកូដពី Chat Completions ទៅ Responses API, **ការសាកល្បងខូចដោយវិធីដែលអាចទាយទុកជាមុន**។ ការបញ្ជាក់នេះគ្របដណ្តប់អំពីអ្វីដែលត្រូវជួសជុល។

---

## ការដាក់តំណរមកប្រាប់ស្វាគមន៍បញ្ជូនចរន្ត (Python pytest)

### ថ្នាក់មុខងារមុខប្រាប់ស្វាគមន៍

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
            # រក្សាទុកប្រវែងសត្ថៈ៖ បន្ថែមចន្លោះមួយចំនួនមុខពាក្យទាំងអស់ក្រៅតែមុខមួយប៉ុណ្ណោះ
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

### ការបញ្ជូនពេលដើម្បីចែកចាយតបស្នាក់លើមាតិកាសារ

កម្មវិធីពិតប្រាកដផ្តល់ចម្លើយខុសគ្នាតាមការបញ្ចូល។ ចែកចាយដោយ `input` (មិនមែន `messages`)៖

```python
async def mock_acreate(*args, **kwargs):
    # Responses API ប្រើ 'input' មិនមែន 'messages'
    last_message = kwargs.get("input", [])[-1]["content"]
    if last_message == "What is the capital of France?":
        return AsyncResponseIterator("The capital of France is Paris.")
    elif last_message == "What is the capital of Germany?":
        return AsyncResponseIterator("The capital of Germany is Berlin.")
    else:
        raise ValueError(f"Unexpected message: {last_message}")
```

### រួមបញ្ចូលផ្លូវ Monkeypatch

| ប្រភេទអតិថិជន | ផ្លូវ Monkeypatch |
|-------------|------------------|
| `AsyncOpenAI` | `openai.resources.responses.AsyncResponses.create` |
| `OpenAI` (sync) | `openai.resources.responses.Responses.create` |

> **មុន** (Chat Completions): `openai.resources.chat.AsyncCompletions.create`
> **បន្ទាប់** (Responses): `openai.resources.responses.AsyncResponses.create`

### ឧទាហរណ៍​គ្រឿងបន្លាស់ពេញលេញ

```python
@pytest.fixture
def mock_openai_responses(monkeypatch):
    # ... ជំពូក MockResponseEvent និង AsyncResponseIterator នៅទីនេះ ...

    async def mock_acreate(*args, **kwargs):
        last_message = kwargs.get("input", [])[-1]["content"]
        if last_message == "What is the capital of France?":
            return AsyncResponseIterator("The capital of France is Paris.")
        else:
            raise ValueError(f"Unexpected message: {last_message}")

    monkeypatch.setattr("openai.resources.responses.AsyncResponses.create", mock_acreate)
```

---

## 1. អាប់ដេតឧបករណ៍ mock

ជំនួស mocks ដែលផ្អែកលើ `ChatCompletionChunk` ជាមួយបម្លែង `MockResponseEvent` / `AsyncResponseIterator` ខាងលើ។ ការផ្លាស់ប្តូរចម្បងៈ

| មុន (mock Chat Completions) | បន្ទាប់ (mock Responses) |
|-------------------------------|------------------------|
| `openai.types.chat.ChatCompletionChunk(...)` | `MockResponseEvent(event_type, delta)` |
| `choices[0].delta.content` | `event.delta` |
| `finish_reason="stop"` នៅក្នុង chunk | `event.type == "response.completed"` |
| chunk `prompt_filter_results` ជាពិសេស Azure | ដកចេញទាំងស្រុង |
| `content_filter_results` តាមជម្រើសជាពិសេស Azure | ដកចេញទាំងស្រុង |
| `kwargs.get("messages")` នៅ mock | `kwargs.get("input")` នៅ mock |

---

## 2. អាប់ដេតឯកសារសម្លុក / ផ្កាយមាស

ប្រសិនបើយោងទៅតេស្តស្នូលមានការប្រើប្រាស់សម្លុក(ដូចជា `pytest-snapshot`, syrupy, ឬសម្លុក JSONL ដែលផលិតដោយដៃ), ទ្រង់ទ្រាយលទ្ធផលដែលរំពឹងទុកផ្លាស់ប្តូរ ៖

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

ទ្រង់ទ្រាយថ្មីមានភាពសាមញ្ញយ៉ាងខ្លាំង — គ្មានវាល `function_call`, `refusal`, `role`, `tool_calls`, `index`, `logprobs`, ឬ `content_filter_results` ទៀត។ អាប់ដេតឬបង្កើតឡើងវិញឯកសារសម្លុកទាំងអស់។

> **រូបិយប័ណ្ណ**: ជួញដូរតេស្តជាមួយ `--snapshot-update` (pytest-snapshot) ឬ `--update-snapshots` (syrupy) បន្ទាប់ពីផ្លាស់ប្តូរដើម្បីផលិតឡើងវិញដោយស្វ័យប្រវត្តិ។

---

## 3. អាប់ដេតការត្រួតពិនិត្យតេស្ត

ការខូចខាតធម្មតាក្នុងការត្រួតពិនិត្យ:

| ពិនិត្យចាស់ | បញ្ហា | ពិនិត្យថ្មី |
|--------------|---------|---------------|
| `client._azure_ad_token_provider is not None` | `AsyncOpenAI` គ្មានគុណលក្ខណៈ `_azure_ad_token_provider` | `isinstance(client, AsyncOpenAI)` និង `"/openai/v1/" in str(client.base_url)` |
| `client.api_version == "2024-..."` | គ្មាន `api_version` នៅលើ `OpenAI`/`AsyncOpenAI` | ដកចេញទាំងស្រុង |
| `isinstance(client, AsyncAzureOpenAI)` | ប្រភេទអតិថិជនផ្លាស់ប្ដូរ | `isinstance(client, AsyncOpenAI)` |

---

## 4. អាប់ដេតអរិយធម៌បរិយាកាសនៅក្នុងឧបករណ៍សាកល្បង

ការសាកល្បងជារឿយៗកំណត់បម្លាស់ប្តូរបរិយាកាសតាម `monkeypatch.setenv`។ អាប់ដេតពួកនេះ៖

| បរិយាកាសចាស់ | បរិយាកាសថ្មី | កំណត់សម្គាល់ |
|-------------|-------------|-------|
| `AZURE_OPENAI_CLIENT_ID` | `AZURE_CLIENT_ID` | គោលក្នុង SDK អត្តសញ្ញាណ Azure ទៀងទាត់ |
| `AZURE_OPENAI_VERSION` | ដកចេញ | គ្មាន `api_version` ត្រូវការ |
| `AZURE_OPENAI_API_VERSION` | ដកចេញ | គ្មាន `api_version` ត្រូវការ |
| `AZURE_OPENAI_ENDPOINT` | `AZURE_OPENAI_ENDPOINT` | រក្សាទុក (នៅតែត្រូវការសម្រាប់ `base_url`) |
| `AZURE_OPENAI_CHAT_DEPLOYMENT` | `AZURE_OPENAI_CHAT_DEPLOYMENT` | រក្សាទុក (ឈ្មោះដាក់សំរាប់ `model` param) |

---

## 5. ស្វែងរកកូដសាកល្បងដែលត្រូវការផ្លាស់ប្តូរ

```bash
# លំនាំចាស់ពិសេសសម្រាប់ការប្រឡង
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