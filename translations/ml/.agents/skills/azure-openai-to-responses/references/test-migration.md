# ടെസ്റ്റ് ഇൻഫ്രാസ്ട്രക്ചർ മൈഗ്രേഷൻ

ചാറ്റ് കോംപ്ലീഷൻസിൽ നിന്നു پاسخപ്രവർത്തന API യിലേക്ക് കോഡ്‌ബേസ് മൈഗ്രേറ്റ് ചെയ്യുമ്പോൾ, **ടെസ്റ്റുകൾ പ്രവചിക്കാവുന്ന രീതികളിൽ തകരാറ് വരുന്നു**. പരിഹാരങ്ങൾ എന്തെന്താണെന്ന് ഈ റഫറൻസ് വിശദീകരിക്കുന്നു.

---

## സ്റ്റ്രീമിംഗ്_RESPONSES_ മൊക്കിംഗ് (Python pytest)

### കോർ മൊക്ക് ക്ലാസ്സുകൾ

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
            # ശൂന്യസ്ഥാനം സംരക്ഷിക്കുക: ആദ്യ വാക്കിന് മുന്നിൽ ഒഴികെയുള്ള എല്ലാ വാക്കുകൾക്കും ഇടം ചേർക്കുക
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

### സന്ദേശ ഉള്ളടകത്തിന്റെ അടിസ്ഥാനത്തിൽ മൊക്ക് RESPONSES റൂട്ടിംഗ്

യാഥാർത്ഥ്യ ആപ്പുകൾ പ്രംപ്റ്റ് അടിസ്ഥാനത്തിൽ വ്യത്യസ്ത ഉത്തരം നൽകുന്നു. `input` പ്രകാരം റൂട്ടുചെയ്യുക (`messages` അല്ല):

```python
async def mock_acreate(*args, **kwargs):
    # Responses API 'messages' അല്ല 'input' ഉപയോഗിക്കുന്നു
    last_message = kwargs.get("input", [])[-1]["content"]
    if last_message == "What is the capital of France?":
        return AsyncResponseIterator("The capital of France is Paris.")
    elif last_message == "What is the capital of Germany?":
        return AsyncResponseIterator("The capital of Germany is Berlin.")
    else:
        raise ValueError(f"Unexpected message: {last_message}")
```

### മണിപാച്ച് പാതകൾ

| ക്ലയന്റ് തരം | മണിപാച്ച് പാത്ത് |
|-------------|------------------|
| `AsyncOpenAI` | `openai.resources.responses.AsyncResponses.create` |
| `OpenAI` (sync) | `openai.resources.responses.Responses.create` |

> **മുമ്പ്** (ചാറ്റ് കോംപ്ലീഷൻസ്): `openai.resources.chat.AsyncCompletions.create`
> **ശേഷം** (RESPONSES): `openai.resources.responses.AsyncResponses.create`

### സമ്പൂർണ്ണ ഫിക്സ്ചർ ഉദാഹരണം

```python
@pytest.fixture
def mock_openai_responses(monkeypatch):
    # ... MockResponseEvent ഉം AsyncResponseIterator ക്ലാസ്സുകളും ഇവിടെ ...

    async def mock_acreate(*args, **kwargs):
        last_message = kwargs.get("input", [])[-1]["content"]
        if last_message == "What is the capital of France?":
            return AsyncResponseIterator("The capital of France is Paris.")
        else:
            raise ValueError(f"Unexpected message: {last_message}")

    monkeypatch.setattr("openai.resources.responses.AsyncResponses.create", mock_acreate)
```

---

## 1. മൊക്ക് ഫിക്സ്ചറുകൾ അപ്ഡേറ്റ് ചെയ്യുക

മുകളിലുള്ള `ChatCompletionChunk` അടിസ്ഥാനമാക്കിയ മൊക്കുകൾ `MockResponseEvent` / `AsyncResponseIterator` പാറ്റേൺ ഉപയോഗിച്ച് മാറ്റുക. പ്രധാന മാറ്റങ്ങൾ:

| മുമ്പ് (ചാറ്റ് കോംപ്ലീഷൻ മൊക്ക്) |ശേഷം (RESPONSES മൊക്ക്) |
|-------------------------------|------------------------|
| `openai.types.chat.ChatCompletionChunk(...)` | `MockResponseEvent(event_type, delta)` |
| `choices[0].delta.content` | `event.delta` |
| ചുറ്റുള്ള `finish_reason="stop"` | `event.type == "response.completed"` |
| ആസ്യൂർ-സ്വഭാവമുള്ള `prompt_filter_results` ചങ്ക് | പൂർണ്ണമായും നീക്കം ചെയ്യുക |
| ആസ്യൂർ-സ്വഭാവമുള്ള ഓരോ തിരഞ്ഞെടുപ്പിനും `content_filter_results` | പൂർണ്ണമായും നീക്കം ചെയ്യുക |
| മൊക്കിൽ `kwargs.get("messages")` | മൊക്കിൽ `kwargs.get("input")` |

---

## 2. സ്നാപ്ഷോട്ട് / ഗോൾഡൻ ഫയലുകൾ അപ്ഡേറ്റ് ചെയ്യുക

ടെസ്റ്റ് സ്യൂട്ട് സ്നാപ്ഷോട്ട് ടെസ്റ്റിംഗ് (ഉദാ: `pytest-snapshot`, syrupy, ഹാൻഡ്-റോൾഡ് JSONL സ്നാപ്ഷോട്ടുകൾ) ഉപയോഗിക്കുന്നുവെങ്കിൽ, പ്രതീക്ഷിച്ച ഔട്ട്പുട്ട് രൂപം മാറും:

**മുമ്പ്** (ചാറ്റ് കോംപ്ലീഷൻസ് സ്റ്റ്രീമിംഗ് JSONL):
```jsonl
{"delta": {"content": null, "function_call": null, "refusal": null, "role": "assistant", "tool_calls": null}, "finish_reason": null, "index": 0, "logprobs": null, "content_filter_results": {}}
{"delta": {"content": "The", "function_call": null, "refusal": null, "role": null, "tool_calls": null}, "finish_reason": null, "index": 0, "logprobs": null, "content_filter_results": {"hate": {"filtered": false, "severity": "safe"}, ...}}
{"delta": {"content": null, ...}, "finish_reason": "stop", "index": 0, "logprobs": null, "content_filter_results": {}}
```

**ശേഷം** (RESPONSES API സ്റ്റ്രീമിംഗ് JSONL):
```jsonl
{"delta": {"content": "The"}}
{"delta": {"content": " capital"}}
{"delta": {"content": null}, "finish_reason": "stop"}
```

പുതിയ രൂപം വളരെ ലളിതമാണ് — `function_call`, `refusal`, `role`, `tool_calls`, `index`, `logprobs`, അല്ലെങ്കിൽ `content_filter_results` ഫീൽഡുകൾ ഇല്ല. എല്ലാ സ്നാപ്ഷോട്ട് ഫയലുകളും അപ്ഡേറ്റ് ചെയ്യുക അല്ലെങ്കിൽ പുനഃസൃഷ്ടിക്കുക.

> **ടിപ്പ്**: മൈഗ്രേറ്റുചെയ്‌തതിന് ശേഷം ടെസ്റ്റുകൾ `--snapshot-update` (pytest-snapshot) അല്ലെങ്കിൽ `--update-snapshots` (syrupy) ഉപയോഗിച്ച് ഓട്ടോമാറ്റിക് പുനഃസൃഷ്ടിക്കാൻ രൺ ചെയ്യുക.

---

## 3. ടെസ്റ്റ് അസർഷനുകൾ അപ്ഡേറ്റ് ചെയ്യുക

സാധാരണ അസർഷൻ തകരാറുകൾ:

| പഴയ അസർഷൻ | പ്രശ്നം | പുതിയ അസർഷൻ |
|--------------|---------|---------------|
| `client._azure_ad_token_provider is not None` | `AsyncOpenAI`യിൽ `_azure_ad_token_provider` ആട്രിബ്യൂട്ട് ഇല്ല | `isinstance(client, AsyncOpenAI)` എന്നും `"/openai/v1/"` എന്നത് `str(client.base_url)` ൽ ഉൾപ്പെടുന്നതായിരിക്കണം |
| `client.api_version == "2024-..."` | `OpenAI`/`AsyncOpenAI`യിൽ `api_version` ഇല്ല | പൂർണ്ണമായും നീക്കം ചെയ്യുക |
| `isinstance(client, AsyncAzureOpenAI)` | ക്ലയന്റ് തരം മാറി | `isinstance(client, AsyncOpenAI)` |

---

## 4. ടസ്റ്റ് ഫിക്സ്ചറുകളിൽ പരിസ്ഥിതി വ്യത്യാസങ്ങൾ അപ്ഡേറ്റ് ചെയ്യുക

ടെസ്റ്റുകൾ സാധാരണയായി `monkeypatch.setenv` വഴിയാണ് എൺവ് വേരിയেবলുകൾ സെറ്റ് ചെയ്യുന്നത്. ഇവ അപ്ഡേറ്റ് ചെയ്യുക:

| പഴയ എൻവ് വാരിയബിൾ | പുതിയ എൻവ് വാരിയബിൾ | കുറിപ്പുകൾ |
|-------------|-------------|-------|
| `AZURE_OPENAI_CLIENT_ID` | `AZURE_CLIENT_ID` | സ്റ്റാൻഡേർഡ് ആസ്യൂർ ഐഡന്റിറ്റി SDK കൺവെൻഷൻ |
| `AZURE_OPENAI_VERSION` | നീക്കം ചെയ്യുക | `api_version` ആവശ്യമില്ല |
| `AZURE_OPENAI_API_VERSION` | നീക്കം ചെയ്യുക | `api_version` ആവശ്യമില്ല |
| `AZURE_OPENAI_ENDPOINT` | `AZURE_OPENAI_ENDPOINT` | ഇനിയും വേണം (`base_url` നു വേണ്ടി) |
| `AZURE_OPENAI_CHAT_DEPLOYMENT` | `AZURE_OPENAI_CHAT_DEPLOYMENT` | ഇനിയും വേണം (`model` പാരാമിനായി ഡിപ്ലോയ്‌മെന്റ് നാമം) |

---

## 5. മൈഗ്രേഷൻ ആവശ്യമുള്ള ടെസ്റ്റ് കോഡ് തിരയുക

```bash
# പരീക്ഷാസംബന്ധിയായ പാരമ്പര്യ ബെച്ചു മാതൃകകൾ
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