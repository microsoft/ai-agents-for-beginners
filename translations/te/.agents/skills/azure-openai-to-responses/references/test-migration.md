# టెస్ట్ ఇన్‌ఫ్రాస్ట్రక్చర్ తరలింపు

Chat Completions నుండి Responses API కి కోడ్‌బేస్ తరలిస్తున్నప్పుడు, **టెస్టులు ఊహించదగిన విధంగా విరిగిపోతాయి**. ఏం సరిచేయాలో ఈ సూచిక కవర్ చేస్తుంది.

---

## స్ట్రీమింగ్ ప్రతిస్పందనలను మాక్ చేయడం (Python pytest)

### ప్రధాన మాక్ తరగతులు

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
            # శూన్యతను రక్షించండి: మొదటి పదాన్ని తప్ప అన్ని పదాల ముందు ఖాళీ వ్రాయండి
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

### సందేశం విషయానికి అనుగుణంగా మాక్ ప్రతిస్పందనలను రూట్ చేయడం

వాస్తవ యాప్స్ ప్రాంప్ట్ ఆధారంగా వేరే జవాబులు ఇస్తాయి. `messages` కాకుండా `input` ద్వారా రూట్ చేయండి:

```python
async def mock_acreate(*args, **kwargs):
    # స్పందనల API 'input' ను ఉపయోగిస్తుంది, 'messages' కాదు
    last_message = kwargs.get("input", [])[-1]["content"]
    if last_message == "What is the capital of France?":
        return AsyncResponseIterator("The capital of France is Paris.")
    elif last_message == "What is the capital of Germany?":
        return AsyncResponseIterator("The capital of Germany is Berlin.")
    else:
        raise ValueError(f"Unexpected message: {last_message}")
```

### మంకీప్యాచ్ మార్గాలు

| క్లయింట్ రకం | మంకీప్యాచ్ మార్గం |
|-------------|------------------|
| `AsyncOpenAI` | `openai.resources.responses.AsyncResponses.create` |
| `OpenAI` (సింక్) | `openai.resources.responses.Responses.create` |

> **మునుపటి** (Chat Completions): `openai.resources.chat.AsyncCompletions.create`
> **తరతరాలు** (Responses): `openai.resources.responses.AsyncResponses.create`

### పూర్తి ఫిక్స్చర్ ఉదాహరణ

```python
@pytest.fixture
def mock_openai_responses(monkeypatch):
    # ... ఇక్కడ MockResponseEvent మరియు AsyncResponseIterator తరగతులు ...

    async def mock_acreate(*args, **kwargs):
        last_message = kwargs.get("input", [])[-1]["content"]
        if last_message == "What is the capital of France?":
            return AsyncResponseIterator("The capital of France is Paris.")
        else:
            raise ValueError(f"Unexpected message: {last_message}")

    monkeypatch.setattr("openai.resources.responses.AsyncResponses.create", mock_acreate)
```

---

## 1. మాక్ ఫిక్స్చర్లను అప్డేట్ చేయండి

`ChatCompletionChunk` ఆధారిత మాక్‌లను పై `MockResponseEvent` / `AsyncResponseIterator` ప్యాటర్న్‌తో మార్చండి. ప్రధాన మార్పులు:

| ముందు (Chat Completions మాక్) | తర్వాత (Responses మాక్) |
|-------------------------------|------------------------|
| `openai.types.chat.ChatCompletionChunk(...)` | `MockResponseEvent(event_type, delta)` |
| `choices[0].delta.content` | `event.delta` |
| చంక్‌లో `finish_reason="stop"` | `event.type == "response.completed"` |
| Azure-స్పెసిఫిక్ `prompt_filter_results` చంక్ | పూర్తిగా తొలగించండి |
| Azure-స్పెసిఫిక్ `content_filter_results` ప్రతి ఎంపికకి | పూర్తిగా తొలగించండి |
| మాక్‌లో `kwargs.get("messages")` | మాక్‌లో `kwargs.get("input")` |

---

## 2. స్నాప్షాట్ / గోల్డెన్ ఫైల్స్‌ను అప్డేట్ చేయండి

టెస్ట్ సూట్ స్నాప్షాట్ టెస్టింగ్ (ఉదా: `pytest-snapshot`, syrupy, లేదా హ్యాండ్-రోల్ JSONL స్నాప్షాట్లు) ఉపయోగిస్తే, ఎదురుచూసే అవుట్పుట్ ఆకారం మారుతుంది:

**మునుపటి** (Chat Completions స్ట్రీమింగ్ JSONL):
```jsonl
{"delta": {"content": null, "function_call": null, "refusal": null, "role": "assistant", "tool_calls": null}, "finish_reason": null, "index": 0, "logprobs": null, "content_filter_results": {}}
{"delta": {"content": "The", "function_call": null, "refusal": null, "role": null, "tool_calls": null}, "finish_reason": null, "index": 0, "logprobs": null, "content_filter_results": {"hate": {"filtered": false, "severity": "safe"}, ...}}
{"delta": {"content": null, ...}, "finish_reason": "stop", "index": 0, "logprobs": null, "content_filter_results": {}}
```

**తరతరాలు** (Responses API స్ట్రీమింగ్ JSONL):
```jsonl
{"delta": {"content": "The"}}
{"delta": {"content": " capital"}}
{"delta": {"content": null}, "finish_reason": "stop"}
```

కొత్త ఆకారం చాలా సరళమైనది — `function_call`, `refusal`, `role`, `tool_calls`, `index`, `logprobs`, లేదా `content_filter_results` ఫీల్డ్స్ ఉండవు. అన్ని స్నాప్షాట్ ఫైల్స్‌ను అప్డేట్ లేదా పునఃసృష్టించండి.

> **గుర్తు**: తరలింపు తర్వాత ఆటోరీజెనరేట్ చేయడానికి `--snapshot-update` (pytest-snapshot) లేదా `--update-snapshots` (syrupy) తో టెస్టులు నడపండి.

---

## 3. టెస్ట్ నిర్ధారణలను అప్డేట్ చేయండి

సాధారణ నిర్ధారణ విరామాలు:

| పాత నిర్ధారణ | సమస్య | కొత్త నిర్ధారణ |
|--------------|---------|---------------|
| `client._azure_ad_token_provider is not None` | `AsyncOpenAI` కు `_azure_ad_token_provider` అభిప్రాయం లేదు | `isinstance(client, AsyncOpenAI)` మరియు `"/openai/v1/" in str(client.base_url)` |
| `client.api_version == "2024-..."` | `OpenAI`/`AsyncOpenAI`పై ఏ `api_version` లేదు | పూర్తిగా తొలగించండి |
| `isinstance(client, AsyncAzureOpenAI)` | క్లయింట్ రకం మారింది | `isinstance(client, AsyncOpenAI)` |

---

## 4. టెస్ట్ ఫిక్స్చర్లలో పర్యావరణ చలామణీలను అప్డేట్ చేయండి

టెస్టులు తరచుగా `monkeypatch.setenv` ద్వారా env vars సెట్ చేస్తాయి. ఇవి అప్డేట్ చేయండి:

| పాత env var | కొత్త env var | గమనికలు |
|-------------|-------------|-------|
| `AZURE_OPENAI_CLIENT_ID` | `AZURE_CLIENT_ID` | స్టాండర్డ్ Azure Identity SDK ఆచారం |
| `AZURE_OPENAI_VERSION` | తొలగించు | ఏ api_version అవసరం లేదు |
| `AZURE_OPENAI_API_VERSION` | తొలగించు | ఏ api_version అవసరం లేదు |
| `AZURE_OPENAI_ENDPOINT` | `AZURE_OPENAI_ENDPOINT` | ఉంచండి (ఇంకా `base_url` కోసం అవసరం) |
| `AZURE_OPENAI_CHAT_DEPLOYMENT` | `AZURE_OPENAI_CHAT_DEPLOYMENT` | ఉంచండి (`model` పారామీటర్ కోసం deployment పేరు) |

---

## 5. తరలింపుకు అవసరమైన టెస్ట్ కోడ్ కోసం శోధించండి

```bash
# పరీక్ష-దిశగా నిర్దిష్ట వెనుకబడిన నమూనాలు
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
**అస్వీకరణ**:
ఈ పత్రం AI అనువాద సేవ [Co-op Translator](https://github.com/Azure/co-op-translator) ఉపయోగించి అనువదించబడింది. మేము ఖచ్చితత్వానికి ప్రయత్నిస్తున్నప్పటికీ, ఆటోమేటెడ్ అనువాదాలు తప్పులు లేదా అసమగ్రతలను కలిగి ఉండవచ్చు. దాని స్వదేశ భాషలో ఉన్న అసలు పత్రాన్ని అధికారం కలిగిన మూలంగా పరిగణించాలి. కీలకమైన సమాచారం కోసం, ప్రొఫెషనల్ మానవ అనువాదాన్ని సిఫారసు చేస్తాము. ఈ అనువాదం ఉపయోగం వల్ల కలిగే ఏవైనా అపార్థాలు లేదా తప్పుదారులు కోసం మేము బాధ్యత వహించము.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->