# စမ်းသပ်မှု အင်ဖရာစက်တပ် ပြောင်းရွှေ့ခြင်း

Chat Completions မှ Responses API သို့ ကုဒ်အခြေခံကို ပြောင်းရွှေ့စဉ်တွင်၊ **စမ်းသပ်မှုများသည် ကြိုတင်ခန့်မှန်းနိုင်သည့် နည်းလမ်းဖြင့် ချိုးဖျက်သွားသည်။** ယခု ရည်ညွှန်းချက်တွင် ပြင်ဆင်ရမည့်အရာများ ပါဝင်သည်။

---

## စတရီမင်း အဖြေ Mock ပြုလုပ်ခြင်း (Python pytest)

### အခြေခံ mock ကလားစ

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
            # သရုတန်းကိုသေချာထားပါ - ပထမဆုံး စကားလုံးအားသာ အခြားဆိုက် စကားလုံးအားလုံးကို အကြို ဖြည့်ပါ။
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

### စနစ်အတိုင်း စာတိုက်အကြောင်းအရ mock အဖြေများ ရွေးချယ်ပါ

အမှန်တကယ် အက်ပ်များသည် prompt များအပေါ်မူတည်၍ မတူညီသည့် အဖြေများကို ပေးသည်။ `input` (messages မဟုတ်ပါ) ဖြင့် လမ်းညွှန်ပါ။

```python
async def mock_acreate(*args, **kwargs):
    # Responses API သည် 'messages' မဟုတ်ဘဲ 'input' ကို အသုံးပြုပါသည်
    last_message = kwargs.get("input", [])[-1]["content"]
    if last_message == "What is the capital of France?":
        return AsyncResponseIterator("The capital of France is Paris.")
    elif last_message == "What is the capital of Germany?":
        return AsyncResponseIterator("The capital of Germany is Berlin.")
    else:
        raise ValueError(f"Unexpected message: {last_message}")
```

### Monkeypatch လမ်းကြောင်းများ

| Client အမျိုးအစား | Monkeypatch လမ်းကြောင်း |
|-------------|------------------|
| `AsyncOpenAI` | `openai.resources.responses.AsyncResponses.create` |
| `OpenAI` (sync) | `openai.resources.responses.Responses.create` |

> **မပြောင်းမီ** (Chat Completions): `openai.resources.chat.AsyncCompletions.create`
> **ပြောင်းလဲပြီး** (Responses): `openai.resources.responses.AsyncResponses.create`

### ပြည့်စုံသော fixture နမူနာ

```python
@pytest.fixture
def mock_openai_responses(monkeypatch):
    # ... MockResponseEvent နှင့် AsyncResponseIterator အတန်းများကို ဒီမှာ ...

    async def mock_acreate(*args, **kwargs):
        last_message = kwargs.get("input", [])[-1]["content"]
        if last_message == "What is the capital of France?":
            return AsyncResponseIterator("The capital of France is Paris.")
        else:
            raise ValueError(f"Unexpected message: {last_message}")

    monkeypatch.setattr("openai.resources.responses.AsyncResponses.create", mock_acreate)
```

---

## ၁။ mock fixtures အသစ်ပြောင်းရွှေ့ခြင်း

`ChatCompletionChunk` အခြေခံ mock များကို `MockResponseEvent` / `AsyncResponseIterator` ပုံစံ အသစ်ဖြင့် အစားထိုးပါ။ အဓိကပြောင်းလဲမှုများမှာ-

| မပြောင်းမီ (Chat Completions mock) | ပြောင်းလဲပြီး (Responses mock) |
|-------------------------------|------------------------|
| `openai.types.chat.ChatCompletionChunk(...)` | `MockResponseEvent(event_type, delta)` |
| `choices[0].delta.content` | `event.delta` |
| chunk တွင် `finish_reason="stop"` | `event.type == "response.completed"` |
| Azure အထူး `prompt_filter_results` chunk | အပြီးအစီး ဖယ်ရှားပါ |
| Azure အထူး `content_filter_results` choice တစ်ခုစီ | အပြီးအစီး ဖယ်ရှားပါ |
| mock တွင် `kwargs.get("messages")` | mock တွင် `kwargs.get("input")` |

---

## ၂။ snapshot / golden ဖိုင်များ ပြင်ဆင်ခြင်း

စမ်းသပ်မှု စုစည်းမှုတွင် snapshot စမ်းသပ်မှု (ဥပမာ `pytest-snapshot`, syrupy, သို့မဟုတ် JSONL snapshots ကို ကိုင်တွယ်ခြင်း) ကို အသုံးပြုလျှင်၊ ထွက်ရှိချက် ပုံသဏ္ဍာန် ပြောင်းလဲသွားသည်။

**မပြောင်းမီ** (Chat Completions streaming JSONL):
```jsonl
{"delta": {"content": null, "function_call": null, "refusal": null, "role": "assistant", "tool_calls": null}, "finish_reason": null, "index": 0, "logprobs": null, "content_filter_results": {}}
{"delta": {"content": "The", "function_call": null, "refusal": null, "role": null, "tool_calls": null}, "finish_reason": null, "index": 0, "logprobs": null, "content_filter_results": {"hate": {"filtered": false, "severity": "safe"}, ...}}
{"delta": {"content": null, ...}, "finish_reason": "stop", "index": 0, "logprobs": null, "content_filter_results": {}}
```

**ပြောင်းလဲပြီး** (Responses API streaming JSONL):
```jsonl
{"delta": {"content": "The"}}
{"delta": {"content": " capital"}}
{"delta": {"content": null}, "finish_reason": "stop"}
```

ပုံသဏ္ဍာန်အသစ်သည် လျင်မြန်ပြီး လွယ်ကူသည် — `function_call`, `refusal`, `role`, `tool_calls`, `index`, `logprobs`, သို့မဟုတ် `content_filter_results` လို အကွက်များ မပါဝင်ကြပါ။ snapshot ဖိုင်များအားလုံးကို update ရှေ့သစ်ပါ။

> **အကြံပြုချက်**: ပြောင်းရွှေ့ပြီးနောက် `--snapshot-update` (pytest-snapshot) သို့မဟုတ် `--update-snapshots` (syrupy) ဖြင့် စမ်းသပ်မှုများပြုလုပ်ပါက အလိုအလျောက် ပြောင်းလဲသွားပါမည်။

---

## ၃။ စမ်းသပ်မှု အာမခံချက်များ ပြင်ဆင်ခြင်း

ရိုးရာ အာမခံချက်ချိုးဖျက်မှုများ:

| ခုနှစ် အာမခံချက် | ပြဿနာ | အသစ် အာမခံချက် |
|--------------|---------|---------------|
| `client._azure_ad_token_provider is not None` | `AsyncOpenAI` တွင် `_azure_ad_token_provider` attribute မရှိပါ | `isinstance(client, AsyncOpenAI)` နှင့် `"/openai/v1/" in str(client.base_url)` |
| `client.api_version == "2024-..."` | `OpenAI`/`AsyncOpenAI` တွင် `api_version` မရှိပါ | အပြီးအစီး ဖယ်ရှားပါ |
| `isinstance(client, AsyncAzureOpenAI)` | Client အမျိုးအစား ပြောင်းလဲသွားသည် | `isinstance(client, AsyncOpenAI)` |

---

## ၄။ စမ်းသပ်မှု fixtures တွင် ပတ်ဝန်းကျင် ရောနှောသည့် 변수를 ပြင်ဆင်ပါ

စမ်းသပ်မှုများတွင် အကြိမ်ကြိမ် `monkeypatch.setenv` ဖြင့် env var များ သတ်မှတ်သည်။ ၎င်းများကို update လုပ်ပါ။

| နန်းမူ env var | အသစ် env var | မှတ်ချက်များ |
|-------------|-------------|-------|
| `AZURE_OPENAI_CLIENT_ID` | `AZURE_CLIENT_ID` | ယဉ်ကျေးသော Azure Identity SDK စံနှုန်း |
| `AZURE_OPENAI_VERSION` | ဖယ်ရှားပါ | api_version မလိုအပ်ပါ |
| `AZURE_OPENAI_API_VERSION` | ဖယ်ရှားပါ | api_version မလိုအပ်ပါ |
| `AZURE_OPENAI_ENDPOINT` | `AZURE_OPENAI_ENDPOINT` | ထားပါ (base_url အတွက် မထွက်ရှိသေး) |
| `AZURE_OPENAI_CHAT_DEPLOYMENT` | `AZURE_OPENAI_CHAT_DEPLOYMENT` | ထားပါ (model parameter အတွက် deployment နာမည်) |

---

## ၅။ ပြောင်းရွှေ့ရမည့် စမ်းသပ်မှုကုဒ်ကို ရှာဖွေပါ

```bash
# စမ်းသပ်မှု-ထူးချွန်နည်းပညာအမွေအနှစ်ပုံစံများ
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
**ပြောကြားချက်**
ဤစာတမ်းကို AI ဘာသာပြန်ဝန်ဆောင်မှု [Co-op Translator](https://github.com/Azure/co-op-translator) အသုံးပြု၍ ဘာသာပြန်ထားပါသည်။ ကျွန်ုပ်တို့သည် တိကျမှန်ကန်မှုအတွက် ကြိုးပမ်းနေသော်လည်း၊ စက်ကိရိယာဘာသာပြန်ခြင်းများတွင် အမှားများ သို့မဟုတ် မှားယွင်းချက်များ ပါဝင်နိုင်ကြောင်း သတိပြုပါရန် လိုအပ်ပါသည်။ မူလစာတမ်းကို မူရင်းဘာသာဖြင့်သာ ယုံကြည်စိတ်ချရသော အချက်အလက်အဖြစ် သတ်မှတ်သင့်သည်။ အရေးကြီးသည့် သတင်းအချက်အလက်များအတွက် ပရော်ဖက်ရှင်နယ် လူသားဘာသာပြန်သူဝန်ဆောင်မှုကို အကြံပြုပါသည်။ ဤဘာသာပြန်ချက်ကို အသုံးပြုခြင်းမှ ဖြစ်ပေါ်လာသော နားလည်မှုကွာခြားမှုများ သို့မဟုတ် မမှန်ကန်သော အသုံးပြုမှုများအတွက် ကျွန်ုပ်တို့ တာဝန်မခံပါ။
<!-- CO-OP TRANSLATOR DISCLAIMER END -->