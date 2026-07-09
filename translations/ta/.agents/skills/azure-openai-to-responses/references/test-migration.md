# சோதனை பணியாளர் இடமாற்றம்

Chat Completions இல் இருந்து Responses API க்கு குறியீட்டை மாற்றும் போது, **சோதனைகள் கணிக்கக்கூடிய முறைகளில் உடைந்து விடுகின்றன**. எதை சரிசெய்ய வேண்டும் என்பதைக் குறிப்பிடுகிறது இந்த குறிப்பு.

---

## ஸ்ட்ரீமிங் பதில்களை முற்போக்கு பதிப்பிக்கல் (Python pytest)

### மூல mock வகுப்புகள்

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
            # வெற்றிடத்தை பாதுகாக்கவும்: முதல் வார்த்தையை தவிர அனைத்து வார்த்தைகளுக்கும் முன் வெற்றிடம் சேர்க்கவும்
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

### செய்தி உள்ளடக்கத்தின் அடிப்படையில் mock பதில்களை வழிமாற்றல்

உண்மையான பயன்பாடுகள் கோரிக்கையின் அடிப்படையில் வெவ்வேறு பதில்களை வழங்குகின்றன. `input` அலகின் அடிப்படையில் வழிகாட்டவும் (messages அல்ல):

```python
async def mock_acreate(*args, **kwargs):
    # பதில்கள் API 'input' ஐ பயன்படுத்துகிறது 'messages' அல்ல
    last_message = kwargs.get("input", [])[-1]["content"]
    if last_message == "What is the capital of France?":
        return AsyncResponseIterator("The capital of France is Paris.")
    elif last_message == "What is the capital of Germany?":
        return AsyncResponseIterator("The capital of Germany is Berlin.")
    else:
        raise ValueError(f"Unexpected message: {last_message}")
```

### Monkeypatch பாதைகள்

| கிளையன்ட் வகை | Monkeypatch பாதை |
|-------------|------------------|
| `AsyncOpenAI` | `openai.resources.responses.AsyncResponses.create` |
| `OpenAI` (sync) | `openai.resources.responses.Responses.create` |

> **முன்** (Chat Completions): `openai.resources.chat.AsyncCompletions.create`
> **பிறகு** (Responses): `openai.resources.responses.AsyncResponses.create`

### முழுமையான உதாரணம்

```python
@pytest.fixture
def mock_openai_responses(monkeypatch):
    # ... MockResponseEvent மற்றும் AsyncResponseIterator வகுப்புகள் இங்கே ...

    async def mock_acreate(*args, **kwargs):
        last_message = kwargs.get("input", [])[-1]["content"]
        if last_message == "What is the capital of France?":
            return AsyncResponseIterator("The capital of France is Paris.")
        else:
            raise ValueError(f"Unexpected message: {last_message}")

    monkeypatch.setattr("openai.resources.responses.AsyncResponses.create", mock_acreate)
```

---

## 1. mock உதவிகள் புதுப்பிக்கவும்

`ChatCompletionChunk` அடிப்படையிலான mock களை மேலே உள்ள `MockResponseEvent` / `AsyncResponseIterator` முறையில் மாற்றவும். முக்கிய மாற்றங்கள்:

| முன்பு (Chat Completions mock) | பிறகு (Responses mock) |
|-------------------------------|------------------------|
| `openai.types.chat.ChatCompletionChunk(...)` | `MockResponseEvent(event_type, delta)` |
| `choices[0].delta.content` | `event.delta` |
| `finish_reason="stop"` என்ற chunk | `event.type == "response.completed"` |
| Azure-க்கு தனிச்சிறப்பான `prompt_filter_results` chunk | முழுமையாக அகற்று |
| Azure-க்கு தனிச்சிறப்பான `content_filter_results` தேர்வுக்கு | முழுமையாக அகற்று |
| mock இல் `kwargs.get("messages")` | mock இல் `kwargs.get("input")` |

---

## 2. ஸ்நாப்ஷாட் / கோல்டன் கோப்புகளை புதுப்பிக்கவும்

சோதனை தொகுப்பு snapshot சோதனையை (எ.கா., `pytest-snapshot`, syrupy, அல்லது கையால் உருவாக்கிய JSONL snapshots) பயன்படுத்தினால், எதிர்பார்த்த வெளியீட்டின் வடிவம் மாறும்:

**முன்** (Chat Completions ஸ்ட்ரீமிங் JSONL):
```jsonl
{"delta": {"content": null, "function_call": null, "refusal": null, "role": "assistant", "tool_calls": null}, "finish_reason": null, "index": 0, "logprobs": null, "content_filter_results": {}}
{"delta": {"content": "The", "function_call": null, "refusal": null, "role": null, "tool_calls": null}, "finish_reason": null, "index": 0, "logprobs": null, "content_filter_results": {"hate": {"filtered": false, "severity": "safe"}, ...}}
{"delta": {"content": null, ...}, "finish_reason": "stop", "index": 0, "logprobs": null, "content_filter_results": {}}
```

**பிறகு** (Responses API ஸ்ட்ரீமிங் JSONL):
```jsonl
{"delta": {"content": "The"}}
{"delta": {"content": " capital"}}
{"delta": {"content": null}, "finish_reason": "stop"}
```

புதிய வடிவம் மிகவும் எளிமையானது — `function_call`, `refusal`, `role`, `tool_calls`, `index`, `logprobs`, அல்லது `content_filter_results` என்ற புலங்கள் இல்லை. அனைத்து ஸ்நாப்ஷாட் கோப்புகளையும் புதுப்பிக்கவும் அல்லது மீண்டும் உருவாக்கவும்.

> **சூதை**: மாற்றபின் `--snapshot-update` (pytest-snapshot) அல்லது `--update-snapshots` (syrupy) என சோதனைகளை இயக்கி தானாக மீண்டும் உருவாக்கவும்.

---

## 3. சோதனை உறுதிப்படுத்தல்களை புதுப்பிக்கவும்

பொதுவான உறுதிப்படுத்தல் உடைப்புகள்:

| பழைய உறுதிப்படுத்தல் | சிக்கல் | புதிய உறுதிப்படுத்தல் |
|--------------|---------|---------------|
| `client._azure_ad_token_provider is not None` | `AsyncOpenAI` இல் `_azure_ad_token_provider` பண்பு இல்லை | `isinstance(client, AsyncOpenAI)` மற்றும் `"/openai/v1/" in str(client.base_url)` |
| `client.api_version == "2024-..."` | `OpenAI`/`AsyncOpenAI` இல் `api_version` இல்லை | முழுமையாக அகற்று |
| `isinstance(client, AsyncAzureOpenAI)` | கிளையன்ட் வகை மாற்றப்பட்டுள்ளது | `isinstance(client, AsyncOpenAI)` |

---

## 4. சோதனை உதவிகளில் சுற்றுப்புற மாறிலிகளை புதுப்பிக்கவும்

சோதனைகள் பொதுவாக `monkeypatch.setenv` மூலம் சுற்றுப்புற மாறிலிகளை அமைக்கின்றன. இதை புதுப்பிக்கவும்:

| பழைய சுற்றுப்புற மாறி | புதிய சுற்றுப்புற மாறி | குறிப்பு |
|-------------|-------------|-------|
| `AZURE_OPENAI_CLIENT_ID` | `AZURE_CLIENT_ID` | சாதாரண Azure அடையாள SDK ஒப்பந்தம் |
| `AZURE_OPENAI_VERSION` | அகற்று | எதுவும் `api_version` தேவையில்லை |
| `AZURE_OPENAI_API_VERSION` | அகற்று | எதுவும் `api_version` தேவையில்லை |
| `AZURE_OPENAI_ENDPOINT` | `AZURE_OPENAI_ENDPOINT` | வைத்திருக்கும் (`base_url` க்கு இன்னும் தேவை) |
| `AZURE_OPENAI_CHAT_DEPLOYMENT` | `AZURE_OPENAI_CHAT_DEPLOYMENT` | வைத்திருக்கும் (`model` அளவுருவுக்கான deployment பெயர்) |

---

## 5. மாற்றம் தேவையான சோதனை குறியீட்டை தேடு

```bash
# சோதனை-சார்ந்த பழைய வடிவங்கள்
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
**மறுப்பு**:
இந்த ஆவணம் AI மொழிபெயர்ப்பு சேவை [Co-op Translator](https://github.com/Azure/co-op-translator) பயன்படுத்தி மொழிபெயர்க்கப்பட்டுள்ளது. நாங்கள் துல்லியத்திற்காக முயற்சி செய்துள்ளோம், ஆனால் தானாக செய்யப்படும் மொழிபெயர்ப்புகளில் பிழைகள் அல்லது தவறுகள் இருக்கலாம் என்பதை கவனத்தில் கொள்ளவும். அசல் ஆவணம் அதன் தாய்மொழியில் அதிகாரப்பூர்வ ஆதாரமாக கருதப்பட வேண்டும். முக்கியமான தகவல்களுக்கு, தொழில்நுட்பமான மனித மொழிபெயர்ப்பு பரிந்துரைக்கப்படுகிறது. இந்த மொழிபெயர்ப்பைப் பயன்படுத்துவதால் ஏற்படும் எந்த தவறான புரிதல்கள் அல்லது தவறான விளக்கத்திற்கும் நாங்கள் பொறுப்பில்வில்லை.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->