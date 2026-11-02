# परीक्षण अवसंरचना माइग्रेशन

जब Chat Completions से Responses API में कोडबेस माइग्रेट किया जाता है, तो **परीक्षण पूर्वानुमानित तरीकों से टूट जाते हैं**। यह संदर्भ बताता है कि क्या ठीक करना है।

---

## स्ट्रीमिंग प्रतिक्रियाओं का मॉक करना (Python pytest)

### कोर मॉक क्लासेस

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
            # रिक्त स्थान बनाए रखें: पहले शब्द को छोड़कर सभी शब्दों के आगे एक स्थान लगाएं
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

### संदेश सामग्री द्वारा मॉक प्रतिक्रियाओं का रूटिंग

असली ऐप्स प्रम्प्ट के आधार पर अलग-अलग उत्तर देते हैं। `input` द्वारा रूट करें (ना कि `messages` द्वारा):

```python
async def mock_acreate(*args, **kwargs):
    # Responses API 'input' का उपयोग करता है, 'messages' नहीं।
    last_message = kwargs.get("input", [])[-1]["content"]
    if last_message == "What is the capital of France?":
        return AsyncResponseIterator("The capital of France is Paris.")
    elif last_message == "What is the capital of Germany?":
        return AsyncResponseIterator("The capital of Germany is Berlin.")
    else:
        raise ValueError(f"Unexpected message: {last_message}")
```

### मंकीपैच पाथ्स

| क्लाइंट प्रकार | मंकीपैच पाथ |
|-------------|------------------|
| `AsyncOpenAI` | `openai.resources.responses.AsyncResponses.create` |
| `OpenAI` (सिंक) | `openai.resources.responses.Responses.create` |

> **पहले** (Chat Completions): `openai.resources.chat.AsyncCompletions.create`
> **बाद में** (Responses): `openai.resources.responses.AsyncResponses.create`

### पूर्ण फिक्स्चर उदाहरण

```python
@pytest.fixture
def mock_openai_responses(monkeypatch):
    # ... MockResponseEvent और AsyncResponseIterator क्लासेस यहाँ ...

    async def mock_acreate(*args, **kwargs):
        last_message = kwargs.get("input", [])[-1]["content"]
        if last_message == "What is the capital of France?":
            return AsyncResponseIterator("The capital of France is Paris.")
        else:
            raise ValueError(f"Unexpected message: {last_message}")

    monkeypatch.setattr("openai.resources.responses.AsyncResponses.create", mock_acreate)
```

---

## 1. मॉक फिक्स्चर अपडेट करें

`ChatCompletionChunk`-आधारित मॉक को ऊपर दिए गए `MockResponseEvent` / `AsyncResponseIterator` पैटर्न से बदलें। मुख्य परिवर्तन:

| पहले (Chat Completions मॉक) | बाद में (Responses मॉक) |
|-------------------------------|------------------------|
| `openai.types.chat.ChatCompletionChunk(...)` | `MockResponseEvent(event_type, delta)` |
| `choices[0].delta.content` | `event.delta` |
| chunk में `finish_reason="stop"` | `event.type == "response.completed"` |
| Azure-विशिष्ट `prompt_filter_results` chunk | पूरी तरह से हटाएं |
| Azure-विशिष्ट `content_filter_results` प्रति विकल्प | पूरी तरह से हटाएं |
| मॉक में `kwargs.get("messages")` | मॉक में `kwargs.get("input")` |

---

## 2. स्नैपशॉट / गोल्डन फ़ाइलें अपडेट करें

यदि परीक्षण सूट स्नैपशॉट परीक्षण का उपयोग करता है (जैसे, `pytest-snapshot`, syrupy, या हैंड-रोल्ड JSONL स्नैपशॉट्स), तो अपेक्षित आउटपुट संरचना बदल जाती है:

**पहले** (Chat Completions स्ट्रीमिंग JSONL):
```jsonl
{"delta": {"content": null, "function_call": null, "refusal": null, "role": "assistant", "tool_calls": null}, "finish_reason": null, "index": 0, "logprobs": null, "content_filter_results": {}}
{"delta": {"content": "The", "function_call": null, "refusal": null, "role": null, "tool_calls": null}, "finish_reason": null, "index": 0, "logprobs": null, "content_filter_results": {"hate": {"filtered": false, "severity": "safe"}, ...}}
{"delta": {"content": null, ...}, "finish_reason": "stop", "index": 0, "logprobs": null, "content_filter_results": {}}
```

**बाद में** (Responses API स्ट्रीमिंग JSONL):
```jsonl
{"delta": {"content": "The"}}
{"delta": {"content": " capital"}}
{"delta": {"content": null}, "finish_reason": "stop"}
```

नई संरचना काफी सरल है — कोई `function_call`, `refusal`, `role`, `tool_calls`, `index`, `logprobs`, या `content_filter_results` फ़ील्ड नहीं। सभी स्नैपशॉट फ़ाइलों को अपडेट या पुनः उत्पन्न करें।

> **टिप**: माइग्रेट करने के बाद परीक्षणों को `--snapshot-update` (pytest-snapshot) या `--update-snapshots` (syrupy) के साथ चलाएं ताकि ऑटो-रिजनरेट हो सके।

---

## 3. परीक्षण कथनों को अपडेट करें

सामान्य अटकल टूटने के मामले:

| पुराना आश्वासन | समस्या | नया आश्वासन |
|--------------|---------|---------------|
| `client._azure_ad_token_provider is not None` | `AsyncOpenAI` के पास `_azure_ad_token_provider` विशेषता नहीं है | `isinstance(client, AsyncOpenAI)` और `"/openai/v1/" in str(client.base_url)` |
| `client.api_version == "2024-..."` | `OpenAI`/`AsyncOpenAI` पर कोई `api_version` नहीं | पूरी तरह से हटा दें |
| `isinstance(client, AsyncAzureOpenAI)` | क्लाइंट प्रकार बदल गया | `isinstance(client, AsyncOpenAI)` |

---

## 4. परीक्षण फिक्स्चर में पर्यावरण चर अपडेट करें

परीक्षण अक्सर `monkeypatch.setenv` के जरिए env vars सेट करते हैं। इन्हें अपडेट करें:

| पुराना env var | नया env var | नोट्स |
|-------------|-------------|-------|
| `AZURE_OPENAI_CLIENT_ID` | `AZURE_CLIENT_ID` | मानक Azure पहचान SDK कन्वेंशन |
| `AZURE_OPENAI_VERSION` | हटाएं | कोई `api_version` आवश्यक नहीं |
| `AZURE_OPENAI_API_VERSION` | हटाएं | कोई `api_version` आवश्यक नहीं |
| `AZURE_OPENAI_ENDPOINT` | `AZURE_OPENAI_ENDPOINT` | रखें (अभी भी `base_url` के लिए आवश्यक) |
| `AZURE_OPENAI_CHAT_DEPLOYMENT` | `AZURE_OPENAI_CHAT_DEPLOYMENT` | रखें (`model` पैरामीटर के लिए डिप्लॉयमेंट नाम) |

---

## 5. माइग्रेशन की आवश्यकता वाले परीक्षण कोड की खोज करें

```bash
# टेस्ट-विशिष्ट विरासत पैटर्न
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
इस दस्तावेज़ का अनुवाद AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) का उपयोग करके किया गया है। जबकि हम सटीकता के लिए प्रयास करते हैं, कृपया ध्यान दें कि स्वचालित अनुवादों में त्रुटियाँ या अशुद्धियाँ हो सकती हैं। मूल दस्तावेज़ अपनी मूल भाषा में ही प्रामाणिक स्रोत माना जाना चाहिए। महत्वपूर्ण जानकारी के लिए, पेशेवर मानव अनुवाद की सिफारिश की जाती है। इस अनुवाद के उपयोग से उत्पन्न किसी भी गलतफहमी या गलत व्याख्या के लिए हम उत्तरदायी नहीं हैं।
<!-- CO-OP TRANSLATOR DISCLAIMER END -->