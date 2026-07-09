# పరీక్షా మౌలసిద్ధాంతం మైగ్రేషన్

Chat Completions నుండి Responses API కి ఒక కోడ్‌బేస్‌ను మైగ్రేట్ చేసేప్పుడు, **పరీక్షలు నిర్దిష్టమైన ప్రతిపాదనలతో విరుచుకుంటాయి**. ఇది ఏమి సరిచేయాలో ఈ సూచికలో ఉంది.

---

## స్ట్రీమింగ్ ప్రతిక్రియలను మాక్ చేయడం (Python pytest)

### కోర్ మాక్ క్లాసులు

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
            # వైట్ స్పేస్ నిలుపుకోండి: మొదటి పదం మినహాయించి అన్ని పదాల ముందు ఖాళీని జోడించండి
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

### సందేశ కంటెంటు ఆధారంగా మాక్ ప్రతిక్రియలను రూట్ చేయడం

నిజమైన యాప్స్ ప్రాంప్ట్ ఆధారంగా వేర్వేరు జవాబులు అందిస్తాయి. `input` (మరియు `messages` కాదు) ఆధారంగా రూట్ చేయండి:

```python
async def mock_acreate(*args, **kwargs):
    # ప్రతిస్పందనలు API 'input' ను ఉపయోగిస్తుంది, 'messages' ను కాదు
    last_message = kwargs.get("input", [])[-1]["content"]
    if last_message == "What is the capital of France?":
        return AsyncResponseIterator("The capital of France is Paris.")
    elif last_message == "What is the capital of Germany?":
        return AsyncResponseIterator("The capital of Germany is Berlin.")
    else:
        raise ValueError(f"Unexpected message: {last_message}")
```

### మన్కీప్యాచ్ మార్గాలు

| క్లయింట్ రకం | మన్కీప్యాచ్ మార్గం |
|-------------|------------------|
| `AsyncOpenAI` | `openai.resources.responses.AsyncResponses.create` |
| `OpenAI` (సింక్) | `openai.resources.responses.Responses.create` |

> **ముందు** (Chat Completions): `openai.resources.chat.AsyncCompletions.create`
> **తరువాత** (Responses): `openai.resources.responses.AsyncResponses.create`

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

## 1. మాక్ ఫిక్స్చర్లను నవీకరించండి

`ChatCompletionChunk`-ఆధారిత మాక్‌లను `MockResponseEvent` / `AsyncResponseIterator` నమూనాతో మార్చండి. ప్రధాన మార్పులు:

| ముందు (Chat Completions మాక్) | తర్వాత (Responses మాక్) |
|-------------------------------|------------------------|
| `openai.types.chat.ChatCompletionChunk(...)` | `MockResponseEvent(event_type, delta)` |
| `choices[0].delta.content` | `event.delta` |
| `finish_reason="stop"` చంక్‌లో | `event.type == "response.completed"` |
| Azure-నిర్దిష్ట `prompt_filter_results` చంక్ | సంపూర్ణంగా తొలగించండి |
| Azure-నిర్దిష్ట `content_filter_results` ప్రతీ ఎంపికలో | పూర్తిగా తొలగించండి |
| మాక్‌లో `kwargs.get("messages")` | మాక్‌లో `kwargs.get("input")` |

---

## 2. స్నాప్షాట్ / గోల్డెన్ ఫైల్స్‌ను నవీకరించండి

పరీక్షా సూట్ స్నాప్షాట్ పరీక్షను (ఉదా., `pytest-snapshot`, syrupy, లేదా స్వయంగా తయారుచేసిన JSONL స్నాప్‌షాట్లు) ఉపయోగిస్తే, अपेक्षित అవుట్పుట్ ఆకారం మారుతుంది:

**ముందు** (Chat Completions స్ట్రీమింగ్ JSONL):
```jsonl
{"delta": {"content": null, "function_call": null, "refusal": null, "role": "assistant", "tool_calls": null}, "finish_reason": null, "index": 0, "logprobs": null, "content_filter_results": {}}
{"delta": {"content": "The", "function_call": null, "refusal": null, "role": null, "tool_calls": null}, "finish_reason": null, "index": 0, "logprobs": null, "content_filter_results": {"hate": {"filtered": false, "severity": "safe"}, ...}}
{"delta": {"content": null, ...}, "finish_reason": "stop", "index": 0, "logprobs": null, "content_filter_results": {}}
```

**తరువాత** (Responses API స్ట్రీమింగ్ JSONL):
```jsonl
{"delta": {"content": "The"}}
{"delta": {"content": " capital"}}
{"delta": {"content": null}, "finish_reason": "stop"}
```

కొత్త ఆకారం చాలా సులభం — `function_call`, `refusal`, `role`, `tool_calls`, `index`, `logprobs`, లేదా `content_filter_results` ఫీల్డులు లేవు. అన్ని స్నాఫ్ట్ ఫైల్స్ నవీకరించండి లేదా తిరిగి సృష్టించండి.

> **సూచన**: మైగ్రేట్ చేసాక పరీక్షలు `--snapshot-update` (pytest-snapshot) లేదా `--update-snapshots` (syrupy) తో నిర్వహించి ఆటోమేటిక్‌గా రీ جنరేట్ చేయండి.

---

## 3. పరీక్షా దృఢీకరణలను నవీకరించండి

సాధారణ దృఢీకరణ విరుచుకోవడాలు:

| పాత దృఢీకరణ | సమస్య | కొత్త దృఢీకరణ |
|--------------|---------|---------------|
| `client._azure_ad_token_provider is not None` | `AsyncOpenAI` వద్ద `_azure_ad_token_provider` గుణము లేదు | `isinstance(client, AsyncOpenAI)` మరియు `"/openai/v1/" in str(client.base_url)` |
| `client.api_version == "2024-..."` | `OpenAI` / `AsyncOpenAI` లో `api_version` లేదు | పూర్తిగా తొలగించండి |
| `isinstance(client, AsyncAzureOpenAI)` | క్లయింట్ రకం మారింది | `isinstance(client, AsyncOpenAI)` |

---

## 4. పరీక్షా ఫిక్స్చర్లలో వాతావరణ փոփոխనలు నవీకరించండి

పరీక్షలు వెర్షన్ వేరియబుల్స్ సాధారంగా `monkeypatch.setenv` ద్వారా సెట్ చేస్తాయి. వీటిని నవీకరించండి:

| పాత env వరియబుల్ | కొత్త env వరియబుల్ | గమనికలు |
|-------------|-------------|-------|
| `AZURE_OPENAI_CLIENT_ID` | `AZURE_CLIENT_ID` | ప్రామాణిక Azure Identity SDK సంప్రదాయం |
| `AZURE_OPENAI_VERSION` | తొలగించండి | `api_version` అవసరం లేదు |
| `AZURE_OPENAI_API_VERSION` | తొలగించండి | `api_version` అవసరం లేదు |
| `AZURE_OPENAI_ENDPOINT` | `AZURE_OPENAI_ENDPOINT` | ఉంచండి (ఇంకా `base_url` కోసం అవసరం) |
| `AZURE_OPENAI_CHAT_DEPLOYMENT` | `AZURE_OPENAI_CHAT_DEPLOYMENT` | ఉంచండి (`model` పరామితి కోసం deployment పేరు) |

---

## 5. మైగ్రేషన్ అవసరమయ్యే పరీక్ష కో드를 శోధించండి

```bash
# పరీక్ష-ప్రత్యేక పాత నమూనాలు
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