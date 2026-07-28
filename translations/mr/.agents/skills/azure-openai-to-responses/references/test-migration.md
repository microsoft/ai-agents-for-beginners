# चाचणी पायाभूत सुविधा स्थलांतर

जेव्हा Chat Completions वरून Responses API कडे कोडबेस स्थलांतरित केले जाते, तेव्हा **चाचण्या ठराविक मार्गांनी तुटतात**. काय दुरुस्त करायचे ते यामध्ये दर्शविले आहे.

---

## स्ट्रीमिंग प्रतिसादांची मॉकिंग (Python pytest)

### मुख्य मॉक वर्ग

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
            # रिक्त जागा जतन करा: पहिल्या शब्दाशिवाय सर्व शब्दांच्या पुढे रिक्त जागा जोडा
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

### संदेशांच्या सामग्रीनुसार मॉक प्रतिसादांची राऊटिंग

वास्तविक अॅप्स प्रॉम्प्ट नुसार विविध उत्तर देतात. `input` द्वारे राऊट करा (संदेशांवर नव्हे):

```python
async def mock_acreate(*args, **kwargs):
    # Responses API 'input' वापरते, 'messages' नाही
    last_message = kwargs.get("input", [])[-1]["content"]
    if last_message == "What is the capital of France?":
        return AsyncResponseIterator("The capital of France is Paris.")
    elif last_message == "What is the capital of Germany?":
        return AsyncResponseIterator("The capital of Germany is Berlin.")
    else:
        raise ValueError(f"Unexpected message: {last_message}")
```

### मंकीपॅच पथ

| क्लायंट प्रकार | मंकीपॅच पथ |
|-------------|------------------|
| `AsyncOpenAI` | `openai.resources.responses.AsyncResponses.create` |
| `OpenAI` (synchronous) | `openai.resources.responses.Responses.create` |

> **आधीचे** (Chat Completions): `openai.resources.chat.AsyncCompletions.create`
> **नंतरचे** (Responses): `openai.resources.responses.AsyncResponses.create`

### पूर्ण फिक्स्चर उदाहरण

```python
@pytest.fixture
def mock_openai_responses(monkeypatch):
    # ... MockResponseEvent आणि AsyncResponseIterator क्लास येथे ...

    async def mock_acreate(*args, **kwargs):
        last_message = kwargs.get("input", [])[-1]["content"]
        if last_message == "What is the capital of France?":
            return AsyncResponseIterator("The capital of France is Paris.")
        else:
            raise ValueError(f"Unexpected message: {last_message}")

    monkeypatch.setattr("openai.resources.responses.AsyncResponses.create", mock_acreate)
```

---

## 1. मॉक फिक्स्चर अपडेट करा

वर सांगितलेल्या `MockResponseEvent` / `AsyncResponseIterator` पॅटर्नसह `ChatCompletionChunk`-आधारित मॉक बदलून टाका. महत्त्वाचे बदल:

| आधीचे (Chat Completions मॉक) | नंतरचे (Responses मॉक) |
|-------------------------------|------------------------|
| `openai.types.chat.ChatCompletionChunk(...)` | `MockResponseEvent(event_type, delta)` |
| `choices[0].delta.content` | `event.delta` |
| चंकमध्ये `finish_reason="stop"` | `event.type == "response.completed"` |
| Azure-विशिष्ट `prompt_filter_results` चंक | पूर्णपणे काढा |
| Azure-विशिष्ट निवडीसाठी `content_filter_results` | पूर्णपणे काढा |
| मॉकमध्ये `kwargs.get("messages")` | मॉकमध्ये `kwargs.get("input")` |

---

## 2. स्नॅपशॉट / गोल्डन फायली अपडेट करा

जर चाचणी संच स्नॅपशॉट चाचणी वापरत असेल (उदा., `pytest-snapshot`, syrupy, किंवा हँड-रोल्ड JSONL स्नॅपशॉट्स), तर अपेक्षित आउटपुटची रचना बदलते:

**आधीचे** (Chat Completions स्ट्रीमिंग JSONL):
```jsonl
{"delta": {"content": null, "function_call": null, "refusal": null, "role": "assistant", "tool_calls": null}, "finish_reason": null, "index": 0, "logprobs": null, "content_filter_results": {}}
{"delta": {"content": "The", "function_call": null, "refusal": null, "role": null, "tool_calls": null}, "finish_reason": null, "index": 0, "logprobs": null, "content_filter_results": {"hate": {"filtered": false, "severity": "safe"}, ...}}
{"delta": {"content": null, ...}, "finish_reason": "stop", "index": 0, "logprobs": null, "content_filter_results": {}}
```

**नंतरचे** (Responses API स्ट्रीमिंग JSONL):
```jsonl
{"delta": {"content": "The"}}
{"delta": {"content": " capital"}}
{"delta": {"content": null}, "finish_reason": "stop"}
```

नवी रचना फार सोपी आहे — `function_call`, `refusal`, `role`, `tool_calls`, `index`, `logprobs`, किंवा `content_filter_results` फील्ड्स नाहीत. सर्व स्नॅपशॉट फायली अद्यतनित करा किंवा पुनःनिर्मित करा.

> **सूचना**: स्थलांतरित केल्यानंतर `--snapshot-update` (pytest-snapshot) किंवा `--update-snapshots` (syrupy) सह चाचण्या चालवा जेणेकरून ऑटोमॅटिक पुनःनिर्मिती होईल.

---

## 3. चाचणी दावे अपडेट करा

सामान्य दाव्यांचे तुटणे:

| जुना दावा | समस्या | नवीन दावा |
|--------------|---------|---------------|
| `client._azure_ad_token_provider is not None` | `AsyncOpenAI` मध्ये `_azure_ad_token_provider` वैशिष्ट्य नाही | `isinstance(client, AsyncOpenAI)` आणि `"/openai/v1/" str(client.base_url)` मध्ये आहे |
| `client.api_version == "2024-..."` | `OpenAI`/`AsyncOpenAI` वर `api_version` नाही | पूर्णपणे काढा |
| `isinstance(client, AsyncAzureOpenAI)` | क्लायंट प्रकार बदलला आहे | `isinstance(client, AsyncOpenAI)` |

---

## 4. चाचणी फिक्स्चरमधील पर्यावरण बदलफेर अद्यतनित करा

चाचण्या सामान्यतः `monkeypatch.setenv` द्वारे पर्यावरण बदल सेट करतात. यांचे अद्यतन करा:

| जुना पर्यावरण बदल | नवीन पर्यावरण बदल | टीपा |
|-------------|-------------|-------|
| `AZURE_OPENAI_CLIENT_ID` | `AZURE_CLIENT_ID` | मानक Azure ओळख SDK परंपरा |
| `AZURE_OPENAI_VERSION` | काढा | `api_version` आवश्यक नाही |
| `AZURE_OPENAI_API_VERSION` | काढा | `api_version` आवश्यक नाही |
| `AZURE_OPENAI_ENDPOINT` | `AZURE_OPENAI_ENDPOINT` | ठेवा (अद्याप `base_url` साठी आवश्यक) |
| `AZURE_OPENAI_CHAT_DEPLOYMENT` | `AZURE_OPENAI_CHAT_DEPLOYMENT` | ठेवा (`model` पॅरामीटरसाठी डिप्लॉयमेंट नाव) |

---

## 5. स्थलांतराची गरज असलेला चाचणी कोड शोधा

```bash
# चाचणी-विशिष्ट वारसा नमुने
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
**अस्वीकरण**:
हा दस्तऐवज AI भाषांतर सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) चा वापर करून अनुवादित केला आहे. जरी आम्ही अचूकतेसाठी प्रयत्न करतो, तरी कृपया लक्षात घ्या की स्वयंचलित भाषांतरांमध्ये त्रुटी किंवा अचूकतेची कमतरता असू शकते. मूळ दस्तऐवज त्याच्या मूळ भाषेत अधिकृत स्रोत मानला पाहिजे. महत्त्वाची माहिती असल्यास, व्यावसायिक मानवी भाषांतराची शिफारस केली जाते. या भाषांतराच्या वापरामुळे उद्भवणाऱ्या कोणत्याही गैरसमज किंवा चुकीच्या अर्थलावणीसाठी आम्ही जबाबदार नाही.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->