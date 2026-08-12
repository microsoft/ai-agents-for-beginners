# சோதனை வளமை மைக்ரேஷன்

Chat Completions இருந்து Responses APIக்கு கோட்பாகையை மயக்கும்போது, **சோதனைகள் கணிப்பிடத்தக்க வகையில் உடைமைகள் ஏற்படுகின்றன**. சரி செய்வது என்ன என்பதைக் காண இதுவே குறிப்பு.

---

## ஸ்ட்ரீமிங் பதில்களை மோக் செய்வது (Python pytest)

### முக்கிய மோக் வகுப்புகள்

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
            # வெற்று இடங்களை ஒழுங்குசெய்: முதல் வார்த்தையைத் தவிர அனைத்து வார்த்தைகளின் முன் இடம் சேர்க்கவும்
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

### செய்தி உள்ளடக்கத்தின் அடிப்படையில் மோக் பதில்களை வழிமாற்றுதல்

உண்மையான செயலிகள், கேள்விக்கட்டுப்பாட்டின் அடிப்படையில் வேறு பதில்களை வழங்குகின்றன. `input` (செய்திகள் அல்ல) மூலம் வழிமாற்றுக:

```python
async def mock_acreate(*args, **kwargs):
    # பதில்கள் API 'messages' இல்லை 'input' ஐ பயன்படுத்துகிறது
    last_message = kwargs.get("input", [])[-1]["content"]
    if last_message == "What is the capital of France?":
        return AsyncResponseIterator("The capital of France is Paris.")
    elif last_message == "What is the capital of Germany?":
        return AsyncResponseIterator("The capital of Germany is Berlin.")
    else:
        raise ValueError(f"Unexpected message: {last_message}")
```

### மான்கிப்பேச்சு பாதைகள்

| கிளையன்ட் வகை | மான்கிப்பேச்சு பாதை |
|-------------|------------------|
| `AsyncOpenAI` | `openai.resources.responses.AsyncResponses.create` |
| `OpenAI` (sync) | `openai.resources.responses.Responses.create` |

> **முன்னர்** (Chat Completions): `openai.resources.chat.AsyncCompletions.create`
> **பிறகு** (Responses): `openai.resources.responses.AsyncResponses.create`

### முழு கட்டமைப்பு உதாரணம்

```python
@pytest.fixture
def mock_openai_responses(monkeypatch):
    # ... இங்கு MockResponseEvent மற்றும் AsyncResponseIterator வகுப்புகள் ...

    async def mock_acreate(*args, **kwargs):
        last_message = kwargs.get("input", [])[-1]["content"]
        if last_message == "What is the capital of France?":
            return AsyncResponseIterator("The capital of France is Paris.")
        else:
            raise ValueError(f"Unexpected message: {last_message}")

    monkeypatch.setattr("openai.resources.responses.AsyncResponses.create", mock_acreate)
```

---

## 1. மோக் கட்டமைப்புகளை புதுப்பிக்கவும்

`ChatCompletionChunk` அடிப்படையிலான மோக்குகளை மேலுள்ள `MockResponseEvent` / `AsyncResponseIterator` மாதிரிக்கு மாற்றவும். முக்கிய மாற்றங்கள்:

| முன்னர் (Chat Completions மோக்) | பிறகு (Responses மோக்) |
|-------------------------------|------------------------|
| `openai.types.chat.ChatCompletionChunk(...)` | `MockResponseEvent(event_type, delta)` |
| `choices[0].delta.content` | `event.delta` |
| தொகுதியில் `finish_reason="stop"` | `event.type == "response.completed"` |
| Azure-சிறப்பான `prompt_filter_results` தொகுதி | முழுமையாக அகற்றவும் |
| Azure-சிறப்பான `content_filter_results` தேர்வுக்கு | முழுமையாக அகற்றவும் |
| மோக்கில் `kwargs.get("messages")` | மோக்கில் `kwargs.get("input")` |

---

## 2. ஸ்நாப்ஷாட் / கோல்டன் கோப்புகளை புதுப்பிக்கவும்

சோதனை தொகுதி ஸ்நாப்ஷாட் சோதனையை பயன்படுத்தினால் (எ.கா., `pytest-snapshot`, syrupy, அல்லது கைமுறையாக உருவாக்கிய JSONL ஸ்நாப்ஷாட்கள்), எதிர்பார்க்கப்படும் வெளியீட்டின் வடிவம் மாறும்:

**முன்னர்** (Chat Completions ஸ்ட்ரீமிங் JSONL):
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

புதிய வடிவம் மிகவும் எளிமையாகியுள்ளது — `function_call`, `refusal`, `role`, `tool_calls`, `index`, `logprobs`, அல்லது `content_filter_results` என்ற புலங்கள் எல்லாம் இல்லை. அனைத்து ஸ்நாப்ஷாட் கோப்புகளையும் புதுப்பிக்க அல்லது மறுவிதமாக உருவாக்கவும்.

> **டிப்**: மைக்ரேஷன் செய்த பிறகு சோதனைகளை `--snapshot-update` (pytest-snapshot) அல்லது `--update-snapshots` (syrupy) உடன் இயக்கி ஸ்நாப்ஷாட்டுகளை தானாக புதுப்பிக்கவும்.

---

## 3. சோதனை உறுதிப்பாடுகளை புதுப்பிக்கவும்

பொதுவான உறுதிப்பாட்டு உடைமைகள்:

| பழைய உறுதிப்பாடு | பிரச்சனை | புதிய உறுதிப்பாடு |
|--------------|---------|---------------|
| `client._azure_ad_token_provider is not None` | `AsyncOpenAI`க்கு `_azure_ad_token_provider` பண்பாடு இல்லை | `isinstance(client, AsyncOpenAI)` மற்றும் `"/openai/v1/" in str(client.base_url)` |
| `client.api_version == "2024-..."` | `OpenAI`/`AsyncOpenAI`க்கு `api_version` இல்லை | முழுமையாக அகற்று |
| `isinstance(client, AsyncAzureOpenAI)` | கிளையன்ட் வகை மாறியுள்ளது | `isinstance(client, AsyncOpenAI)` |

---

## 4. சோதனை கட்டமைப்புகளில் சுற்றுச்சூழல் மாறிலிகளை புதுப்பிக்கவும்

சோதனைகள் பெரும்பாலும் `monkeypatch.setenv` மூலம் env மாறிலிகளை அமைக்கும். இதைப் புதுப்பிக்கவும்:

| பழைய env மாறி | புதிய env மாறி | குறிப்பு |
|-------------|-------------|-------|
| `AZURE_OPENAI_CLIENT_ID` | `AZURE_CLIENT_ID` | பொதுவான Azure அடையாள SDK நடைமுறை |
| `AZURE_OPENAI_VERSION` | அகற்று | `api_version` தேவையில்லை |
| `AZURE_OPENAI_API_VERSION` | அகற்று | `api_version` தேவையில்லை |
| `AZURE_OPENAI_ENDPOINT` | `AZURE_OPENAI_ENDPOINT` | தொடர்ந்து வைத்திரு (`base_url`க்காக அவசியம்) |
| `AZURE_OPENAI_CHAT_DEPLOYMENT` | `AZURE_OPENAI_CHAT_DEPLOYMENT` | தொடர்ந்து வைத்திரு (`model` பாராம்க் பெயருக்காக) |

---

## 5. மைக்ரேஷன் தேவைப்படும் சோதனை குறியீட்டைக் கண்டுபிடிக்கவும்

```bash
# சோதனை-பிரத்தியேக பழைய படிகள்
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