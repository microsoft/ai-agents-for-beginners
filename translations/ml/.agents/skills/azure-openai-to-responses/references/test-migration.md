# ടെസ്റ്റ് ഇൻഫ്രാസ്ട്രക്ചർ മൈഗ്രേഷൻ

കോഡ്‌ബേസ് ചാറ്റ് കോംപ്ലീഷൻസിൽ നിന്ന് റെസ്പോൺസസ് API-ിലേക്കു മൈഗ്രേറ്റ് ചെയ്യുമ്പോൾ, **ടെസ്റ്റുകൾ പ്രവചനീയമായ രീതിയിൽ തകരാറിലാകുന്നു**. ഇത് പരിഹരിക്കാനുള്ള സ്രോതസ്സാണ് ഈ റഫറൻസ്.

---

## സ്റ്റ്രീമിങ് റെസ്പോൺസുകൾ മോക്ക് ചെയ്യൽ (Python pytest)

### കോർ മോക് ക്ലാസുകൾ

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
            # ശൂന്യമേഖല സംരക്ഷിക്കുക: ആദ്യപരാമർശം ഒഴികെയുള്ള എല്ലാ വാക്കുകൾക്കും മുൻപിൽ സ്പേസ് ചേർക്കുക
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

### സന്ദേശ உள்ளടക്കത്തിനനുസരിച്ച് മോക് റെസ്പോൺസുകൾ റൂട്ടിംഗ്

യഥാർത്ഥ ആപ്പുകൾ പ്രോംപ്റ്റ് അടിസ്ഥാനത്തിൽ വ്യത്യസ്ത ഉത്തരങ്ങൾ നൽകുന്നു. `input` (മാറ്റം: `messages` അല്ല) അനുസരിച്ചു റൂട്ടിംഗ് ചെയ്യുക:

```python
async def mock_acreate(*args, **kwargs):
    # റിസ്പോൺസസ് API 'messages' അല്ല 'input' ഉപയോഗിക്കുന്നു
    last_message = kwargs.get("input", [])[-1]["content"]
    if last_message == "What is the capital of France?":
        return AsyncResponseIterator("The capital of France is Paris.")
    elif last_message == "What is the capital of Germany?":
        return AsyncResponseIterator("The capital of Germany is Berlin.")
    else:
        raise ValueError(f"Unexpected message: {last_message}")
```

### മങ്കിപാച്ച് പാതകൾ

| ക്ലയന്റ് തരം | മങ്കിപാച്ച് പാത |
|-------------|------------------|
| `AsyncOpenAI` | `openai.resources.responses.AsyncResponses.create` |
| `OpenAI` (സിങ്ക്) | `openai.resources.responses.Responses.create` |

> **മുൻപ്** (Chat Completions): `openai.resources.chat.AsyncCompletions.create`
> **ശേഷം** (Responses): `openai.resources.responses.AsyncResponses.create`

### പൂർണ്ണ ഫിക്‌സ്‌ചർ ഉദാഹരണം

```python
@pytest.fixture
def mock_openai_responses(monkeypatch):
    # ... MockResponseEvent සහ AsyncResponseIterator ക്ലാസ്സുകൾ ഇവിടെ ...

    async def mock_acreate(*args, **kwargs):
        last_message = kwargs.get("input", [])[-1]["content"]
        if last_message == "What is the capital of France?":
            return AsyncResponseIterator("The capital of France is Paris.")
        else:
            raise ValueError(f"Unexpected message: {last_message}")

    monkeypatch.setattr("openai.resources.responses.AsyncResponses.create", mock_acreate)
```

---

## 1. മോക് ഫിക്‌സ്‌ച്ചറുകൾ അപ്‌ഡേറ്റ് ചെയ്യുക

സ്റ്റ്രീമിങ് APIയ്ക്ക് ഉചിതമായ `MockResponseEvent` / `AsyncResponseIterator` പാറ്റേൺ ഉപയോഗിച്ച് `ChatCompletionChunk` അടിസ്ഥാനപരമായ മോക്സ് മാറ്റുക. പ്രധാന മാറ്റങ്ങൾ:

| മുൻപ് (Chat Completions മോക്) | പിന്നാലെ (Responses മോക്) |
|-------------------------------|------------------------|
| `openai.types.chat.ChatCompletionChunk(...)` | `MockResponseEvent(event_type, delta)` |
| `choices[0].delta.content` | `event.delta` |
| ചെങ്ക്-ൽ `finish_reason="stop"` | `event.type == "response.completed"` |
| ആസൂർ-സ്പെസിഫിക് `prompt_filter_results` ചെങ്ക് | പൂർണ്ണമായും നീക്കം ചെയ്യുക |
| ആസൂർ-സ്പെസിഫിക് `content_filter_results` ഓരോ തിരഞ്ഞെടുപ്പിലും | പൂർണ്ണമായും നീക്കം ചെയ്യുക |
| മോകിൽ `kwargs.get("messages")` | മോകിൽ `kwargs.get("input")` |

---

## 2. സ്നാപ്ഷോട്ട് / ഗോൾഡൻ ഫയലുകൾ അപ്ഡേറ്റ് ചെയ്യുക

ടെസ്റ്റ് സ്വിറ്റ് സ്നാപ്ഷോട്ട് ടെസ്റ്റിങ് ഉപയോഗിച്ചാൽ (ഉദാഹരണത്തിന്, `pytest-snapshot`, syrupy, അല്ലെങ്കിൽ JSONL സ്വയം തയ്യാറാക്കിയ സ്നാപ്ഷോട്ടുകൾ), പ്രതീക്ഷിക്കപ്പെടുന്ന ഔട്ട്‌പുട്ട് ആകൃതി മാറുന്നു:

**മുൻപ്** (Chat Completions സ്റ്റ്രീമിങ് JSONL):
```jsonl
{"delta": {"content": null, "function_call": null, "refusal": null, "role": "assistant", "tool_calls": null}, "finish_reason": null, "index": 0, "logprobs": null, "content_filter_results": {}}
{"delta": {"content": "The", "function_call": null, "refusal": null, "role": null, "tool_calls": null}, "finish_reason": null, "index": 0, "logprobs": null, "content_filter_results": {"hate": {"filtered": false, "severity": "safe"}, ...}}
{"delta": {"content": null, ...}, "finish_reason": "stop", "index": 0, "logprobs": null, "content_filter_results": {}}
```

**ശേഷം** (Responses API സ്റ്റ്രീമിങ് JSONL):
```jsonl
{"delta": {"content": "The"}}
{"delta": {"content": " capital"}}
{"delta": {"content": null}, "finish_reason": "stop"}
```

ഈ പുതിയ ആകൃതി വളരെ ലളിതമാണ് — `function_call`, `refusal`, `role`, `tool_calls`, `index`, `logprobs`, അല്ലെങ്കിൽ `content_filter_results` ഫീൽഡുകൾ ഇല്ല. എല്ലാ സ്നാപ്ഷട്ട് ഫയലുകളും അപ്ഡേറ്റ് ചെയ്യുകയോ പുനഃസൃഷ്ടിക്കുകയോ ചെയ്യുക.

> **ടിപ്പ്**: മൈഗ്രേറ്റ് ചെയ്തു കഴിഞ്ഞ് `--snapshot-update` (pytest-snapshot) അല്ലെങ്കിൽ `--update-snapshots` (syrupy) ഓപ്ഷനുകൾ ഉപയോഗിച്ച് ടെസ്റ്റുകൾ റൺ ചെയ്യുകയും സ്നാപ്ഷോട്ടുകൾ സ്വയം പുതുക്കുകയും ചെയ്യുക.

---

## 3. ടെസ്റ്റ് അസ്സേർഷനുകൾ അപ്ഡേറ്റ് ചെയ്യുക

സാധാരണമായി ഉള്ള അസ്സേർഷൻ തകരാറുകൾ:

| പഴയ അസ്സേർഷൻ | പ്രശ്നം | പുതിയ അസ്സേർഷൻ |
|--------------|---------|---------------|
| `client._azure_ad_token_provider is not None` | `AsyncOpenAI`-ക്ക് `_azure_ad_token_provider` ആട്രിബ്യൂട്ട് ഇല്ല | `isinstance(client, AsyncOpenAI)` കൂടാതെ `"/openai/v1/" in str(client.base_url)` |
| `client.api_version == "2024-..."` | `OpenAI`/`AsyncOpenAI`-യിൽ `api_version` ഇല്ല | പൂർണ്ണമായും നീക്കം ചെയ്യുക |
| `isinstance(client, AsyncAzureOpenAI)` | ക്ലയന്റ് തരം മാറി | `isinstance(client, AsyncOpenAI)` |

---

## 4. ടെസ്റ്റ് ഫിക്‌സ്‌ചറുകളിലെ എൻവയൺമെന്റ് വേരിയബിളുകൾ അപ്ഡേറ്റ് ചെയ്യുക

ടെസ്റ്റുകൾ സാധാരണയായി `monkeypatch.setenv` മുഖേന എൻവയർമെന്റ് വേരിയബിളുകൾ സജ്ജീകരിക്കുന്നു. ഇവ അപ്ഡേറ്റ് ചെയ്യുക:

| പഴയ എൻവയർമെന്റ് വേരി | പുതിയ എൻവയർമെന്റ് വേരി | കുറിപ്പുകൾ |
|-------------|-------------|-------|
| `AZURE_OPENAI_CLIENT_ID` | `AZURE_CLIENT_ID` | സ്റ്റാൻഡേർഡ് ആസൂർ ഐഡന്റിറ്റി SDK മാർഗനിർദേശം |
| `AZURE_OPENAI_VERSION` | നീക്കം ചെയ്യുക | `api_version` ആവശ്യമില്ല |
| `AZURE_OPENAI_API_VERSION` | നീക്കം ചെയ്യുക | `api_version` ആവശ്യമില്ല |
| `AZURE_OPENAI_ENDPOINT` | `AZURE_OPENAI_ENDPOINT` | നിലനിർത്തുക (`base_url`-യ്ക്ക് ആവശ്യമാണ്) |
| `AZURE_OPENAI_CHAT_DEPLOYMENT` | `AZURE_OPENAI_CHAT_DEPLOYMENT` | നിലനിർത്തുക (ഡിപ്ലോയ്മെന്റ് പേരു `model` പാരാമീറ്ററിനായി) |

---

## 5. മൈഗ്രേഷൻ ആവശ്യമുള്ള ടെസ്റ്റ് കോഡ് കണ്ടെത്തുക

```bash
# ടെസ്റ്റ്-വിശിഷ്ട പാരമ്പര്യ മാതൃകകൾ
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
**അറിയിപ്പ്**:
ഈ രേഖ AI പരിഭാഷാ സേവനം [Co-op Translator](https://github.com/Azure/co-op-translator) ഉപയോഗിച്ച് പരിഭാഷപ്പെടുത്തിയതാണ്. ഞങ്ങൾ കൃത്യതയ്ക്കായി ശ്രമിക്കുന്നുവെങ്കിലും, ഓട്ടോമേറ്റഡ് പരിഭാഷകളിൽ പിഴവുകൾ അല്ലെങ്കിൽ തെറ്റായ വിവരങ്ങൾ ഉണ്ടാകാൻ സാധ്യതയുണ്ട്. അതിന്റെ സ്വാഭാവിക ഭാഷയിലുള്ള അസൽ രേഖയാണ് പ്രാമാണികമായ ഉറവിടമായി പരിഗണിക്കേണ്ടത്. നിർണായകമായ വിവരങ്ങൾക്ക്, പ്രൊഫഷണൽ മനുഷ്യ പരിഭാഷ ശുപാർശ ചെയ്യുന്നു. ഈ പരിഭാഷ ഉപയോഗിച്ച് ഉണ്ടാകുന്ന തെറ്റിദ്ധാരണകൾ അല്ലെങ്കിൽ തെറ്റായ വ്യാഖ്യാനങ്ങൾക്കായി ഞങ്ങൾ ഉത്തരവാദികളല്ല.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->