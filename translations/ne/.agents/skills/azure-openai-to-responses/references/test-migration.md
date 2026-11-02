# परीक्षण पूर्वधार संरचना स्थानान्तरण

जब Chat Completions बाट Responses API मा कोडबेस स्थानान्तरण गरिन्छ, **परीक्षणहरू पूर्वानुमेय तरिकाले भंग हुन्छन्**। यो सन्दर्भले के सुधार गर्ने हो त्यसभने चर्चा गर्छ।

---

## स्ट्रीमिंग प्रतिक्रिया नक्कली बनाउने (Python pytest)

### मुख्य मोक वर्गहरू

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
            # रिक्त स्थान सुरक्षित गर्नुहोस्: पहिलोबाहेक सबै शब्दहरूको अगाडि खाली ठाउँ थप्नुहोस्
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

### सन्देश सामग्री अनुसार मोक प्रतिक्रियाहरू रुट गर्ने

वास्तविक एपहरूले प्रॉम्प्ट आधारमा फरक उत्तरहरू सेवा गर्छन्। `input` द्वारा रुट गर्नुहोस् (`messages` होइन):

```python
async def mock_acreate(*args, **kwargs):
    # प्रतिक्रियाहरू API ले 'input' प्रयोग गर्छ, 'messages' होइन
    last_message = kwargs.get("input", [])[-1]["content"]
    if last_message == "What is the capital of France?":
        return AsyncResponseIterator("The capital of France is Paris.")
    elif last_message == "What is the capital of Germany?":
        return AsyncResponseIterator("The capital of Germany is Berlin.")
    else:
        raise ValueError(f"Unexpected message: {last_message}")
```

### मङ्कीप्याच मार्गहरू

| क्लाइन्ट प्रकार | मङ्कीप्याच मार्ग |
|-------------|------------------|
| `AsyncOpenAI` | `openai.resources.responses.AsyncResponses.create` |
| `OpenAI` (सिंक) | `openai.resources.responses.Responses.create` |

> **अघिल्लो** (Chat Completions): `openai.resources.chat.AsyncCompletions.create`
> **पछिल्लो** (Responses): `openai.resources.responses.AsyncResponses.create`

### पूर्ण फिक्स्चर उदाहरण

```python
@pytest.fixture
def mock_openai_responses(monkeypatch):
    # ... MockResponseEvent र AsyncResponseIterator कक्षाहरू यहाँ ...

    async def mock_acreate(*args, **kwargs):
        last_message = kwargs.get("input", [])[-1]["content"]
        if last_message == "What is the capital of France?":
            return AsyncResponseIterator("The capital of France is Paris.")
        else:
            raise ValueError(f"Unexpected message: {last_message}")

    monkeypatch.setattr("openai.resources.responses.AsyncResponses.create", mock_acreate)
```

---

## 1. मोक फिक्स्चरहरू अपडेट गर्नुहोस्

`ChatCompletionChunk`-आधारित मोकहरूलाई माथि दिइएको `MockResponseEvent` / `AsyncResponseIterator` ढाँचामा प्रतिस्थापन गर्नुहोस्। महत्वपूर्ण परिवर्तनहरू:

| अघिल्लो (Chat Completions मोक) | पछिल्लो (Responses मोक) |
|-------------------------------|------------------------|
| `openai.types.chat.ChatCompletionChunk(...)` | `MockResponseEvent(event_type, delta)` |
| `choices[0].delta.content` | `event.delta` |
| टुक्रामा `finish_reason="stop"` | `event.type == "response.completed"` |
| Azure-विशेष `prompt_filter_results` टुक्रा | पुरा हटाउनुहोस् |
| Azure-विशेष `content_filter_results` प्रति विकल्प | पुरा हटाउनुहोस् |
| मोकमा `kwargs.get("messages")` | मोकमा `kwargs.get("input")` |

---

## 2. स्न्यापशट / गोल्डेन फाइलहरू अपडेट गर्नुहोस्

यदि परीक्षण सूटले स्न्यापशट परीक्षण प्रयोग गर्छ (जस्तै, `pytest-snapshot`, syrupy, वा हातले बनाएको JSONL स्न्यापशटहरू), अपेक्षित आउटपुट आकार परिवर्तन हुन्छ:

**अघिल्लो** (Chat Completions स्ट्रीमिंग JSONL):
```jsonl
{"delta": {"content": null, "function_call": null, "refusal": null, "role": "assistant", "tool_calls": null}, "finish_reason": null, "index": 0, "logprobs": null, "content_filter_results": {}}
{"delta": {"content": "The", "function_call": null, "refusal": null, "role": null, "tool_calls": null}, "finish_reason": null, "index": 0, "logprobs": null, "content_filter_results": {"hate": {"filtered": false, "severity": "safe"}, ...}}
{"delta": {"content": null, ...}, "finish_reason": "stop", "index": 0, "logprobs": null, "content_filter_results": {}}
```

**पछिल्लो** (Responses API स्ट्रीमिंग JSONL):
```jsonl
{"delta": {"content": "The"}}
{"delta": {"content": " capital"}}
{"delta": {"content": null}, "finish_reason": "stop"}
```

नयाँ आकार अत्यन्त सरल छ — कुनै `function_call`, `refusal`, `role`, `tool_calls`, `index`, `logprobs`, वा `content_filter_results` क्षेत्रहरू छैनन्। सबै स्न्यापशट फाइलहरू अपडेट वा पुनःउत्पादन गर्नुहोस्।

> **सुझाव**: स्थानान्तरण पछि स्वत: पुनःउत्पादन गर्न `--snapshot-update` (pytest-snapshot) वा `--update-snapshots` (syrupy) सँग परीक्षणहरू चलाउनुहोस्।

---

## 3. परीक्षण परीक्षणहरू अपडेट गर्नुहोस्

सामान्य परीक्षण भंगहरू:

| पुरानो परीक्षण | समस्या | नयाँ परीक्षण |
|--------------|---------|---------------|
| `client._azure_ad_token_provider is not None` | `AsyncOpenAI` मा `_azure_ad_token_provider` एट्रिब्युट छैन | `isinstance(client, AsyncOpenAI)` र `"/openai/v1/"` `str(client.base_url)` मा छ |
| `client.api_version == "2024-..."` | `OpenAI`/`AsyncOpenAI` मा `api_version` छैन | पुरा हटाउनुहोस् |
| `isinstance(client, AsyncAzureOpenAI)` | क्लाइन्ट प्रकार परिवर्तन भयो | `isinstance(client, AsyncOpenAI)` |

---

## 4. परीक्षण फिक्स्चरमा वातावरण चरहरू अपडेट गर्नुहोस्

परीक्षणहरूले प्रायः `monkeypatch.setenv` द्वारा वातावरण चरहरू सेट गर्छन्। यी अपडेट गर्नुहोस्:

| पुरानो वातावरण चर | नयाँ वातावरण चर | नोटहरू |
|-------------|-------------|-------|
| `AZURE_OPENAI_CLIENT_ID` | `AZURE_CLIENT_ID` | मानक Azure आइडेन्टिटी SDK परम्परा |
| `AZURE_OPENAI_VERSION` | हटाउनुहोस् | कुनै `api_version` आवश्यक छैन |
| `AZURE_OPENAI_API_VERSION` | हटाउनुहोस् | कुनै `api_version` आवश्यक छैन |
| `AZURE_OPENAI_ENDPOINT` | `AZURE_OPENAI_ENDPOINT` | राख्नुहोस् (अझै पनि `base_url` का लागि आवश्यक) |
| `AZURE_OPENAI_CHAT_DEPLOYMENT` | `AZURE_OPENAI_CHAT_DEPLOYMENT` | राख्नुहोस् (`model` पारामिटरको लागि डिप्लोयमेन्ट नाम) |

---

## 5. स्थानान्तरण आवश्यक परीक्षण कोडको खोजी गर्नुहोस्

```bash
# परीक्षण-विशेष पुरानो ढाँचाहरू
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
यो दस्तावेज़ AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) प्रयोग गरेर अनुवाद गरिएको हो। हामी सही हुन प्रयास गर्छौं, तर कृपया जानकार हुनुस् कि स्वचालित अनुवादमा त्रुटिहरू वा अशुद्धताहरू हुन सक्छन्। मूल दस्तावेज़ यसको मूल भाषामा आधिकारिक स्रोत मानिनुपर्छ। महत्वपूर्ण जानकारीका लागि व्यावसायिक मानव अनुवाद सिफारिस गरिन्छ। यस अनुवादको प्रयोगबाट उत्पन्न कुनै पनि गलत बुझाइ वा त्रुटिको लागि हामी जिम्मेवार छैनौं।
<!-- CO-OP TRANSLATOR DISCLAIMER END -->