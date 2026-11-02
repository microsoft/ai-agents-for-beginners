# စမ်းသပ်မှုအခြေခံအဆောက်အဦး ပျmigrationိတ်ပြောင်းခြင်း  

Chat Completions မှ Responses API သို့ ကုဒ်ဘေ့စ်ကို ပြောင်းရွှေ့စဉ်တွင် **စမ်းသပ်မှုများသည် ခန့်မှန်းနိုင်သောနည်းလမ်းများဖြင့် ပြိုကွဲတတ်သည်**။ ၎င်းကို ဖြေရှင်းရန် အကြံပြုချက်ကို ဒီအညွှန်းတွင် ဖော်ပြထားသည်။  

---  

## Streaming Responses ကို စမ်းသပ်ရန် Mock ပြုလုပ်ခြင်း (Python pytest)  

### အခြေခံ mock အတန်းများ  

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
            # အလယ်အလတ်ကွာဟမှုကို ထိန်းသိမ်းပါ: ပထမ စကားလုံးအား မရောစဘဲ အခြား စကားလုံးအားလုံးရှေ့တွင် အာကာသ ထည့်ပါ
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
  
### မက်ဆေ့ခ်ျ အကြောင်းအရာအပေါ်အခြေခံ၍ mock responses များကို လမ်းညွှန်ခြင်း  

သက်ဆိုင်ရာ အက်ပ်များသည် prompt အပေါ်မူတည်ပြီး မတူညီသော အဖြေများပေးသည်။ `input` ကိုကြည့်၍ သွားရောက်ပေးပါ ( `messages` မဟုတ်)။  

```python
async def mock_acreate(*args, **kwargs):
    # Responses API သည် 'messages' မဟုတ်ပဲ 'input' ကို အသုံးပြုသည်။
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

> **မပြောင်းလွယ်ခင်** (Chat Completions): `openai.resources.chat.AsyncCompletions.create`  
> **ပြောင်းလဲပြီးနောက်** (Responses): `openai.resources.responses.AsyncResponses.create`  

### ပြည့်စုံသော fixture ဥပမာ  

```python
@pytest.fixture
def mock_openai_responses(monkeypatch):
    # ... ဒီမှာ MockResponseEvent နဲ့ AsyncResponseIterator အတန်းများ ...

    async def mock_acreate(*args, **kwargs):
        last_message = kwargs.get("input", [])[-1]["content"]
        if last_message == "What is the capital of France?":
            return AsyncResponseIterator("The capital of France is Paris.")
        else:
            raise ValueError(f"Unexpected message: {last_message}")

    monkeypatch.setattr("openai.resources.responses.AsyncResponses.create", mock_acreate)
```
  
---  

## ၁။ mock fixtures များ ပြင်ဆင်ခြင်း  

`ChatCompletionChunk` အခြေခံMocks များကို အထက်ပါ `MockResponseEvent` / `AsyncResponseIterator` ပုံစံဖြင့် အစားထိုးပေးပါ။ အဓိက ပြောင်းလဲမှုများမှာ -  

| မပြောင်းလဲခင် (Chat Completions mock) | ပြောင်းလဲပြီးနောက် (Responses mock) |  
|-------------------------------|------------------------|  
| `openai.types.chat.ChatCompletionChunk(...)` | `MockResponseEvent(event_type, delta)` |  
| `choices[0].delta.content` | `event.delta` |  
| chunk တွင် `finish_reason="stop"` | `event.type == "response.completed"` |  
| Azure အချို့အတွက် သီးသန့် `prompt_filter_results` chunk | အကုန် ဖယ်ရှားပေးရန် |  
| Azure အချို့အတွက် သီးသန့် `content_filter_results` per choice | အကုန် ဖယ်ရှားပေးရန် |  
| mock တွင် `kwargs.get("messages")` | mock တွင် `kwargs.get("input")` |  

---  

## ၂။ snapshot / golden ဖိုင်များကို ပြင်ဆင်ခြင်း  

စမ်းသပ်မှုစနစ်တွင် snapshot testing ကို အသုံးပြုပါက (ဥပမာ - `pytest-snapshot`, syrupy, သို့မဟုတ် လက်လုပ် JSONL snapshot များ)၊ မျှော်မှန်းထားသော output ဖွဲ့စည်းပုံ ပြောင်းလဲသည်။  

**မပြောင်းလဲခင်** (Chat Completions streaming JSONL):  
```jsonl
{"delta": {"content": null, "function_call": null, "refusal": null, "role": "assistant", "tool_calls": null}, "finish_reason": null, "index": 0, "logprobs": null, "content_filter_results": {}}
{"delta": {"content": "The", "function_call": null, "refusal": null, "role": null, "tool_calls": null}, "finish_reason": null, "index": 0, "logprobs": null, "content_filter_results": {"hate": {"filtered": false, "severity": "safe"}, ...}}
{"delta": {"content": null, ...}, "finish_reason": "stop", "index": 0, "logprobs": null, "content_filter_results": {}}
```
  
**ပြောင်းလဲပြီးနောက်** (Responses API streaming JSONL):  
```jsonl
{"delta": {"content": "The"}}
{"delta": {"content": " capital"}}
{"delta": {"content": null}, "finish_reason": "stop"}
```
  
အသစ်ထွက်ရှိသော ဖွဲ့စည်းပုံသည် အလွန်ရိုးရှင်းသည် — `function_call`, `refusal`, `role`, `tool_calls`, `index`, `logprobs`, နှင့် `content_filter_results` ကွင်းများ မရှိတော့ပါ။ snapshot ဖိုင်အားလုံးကို အပ်ဒိတ်လုပ် သို့မဟုတ် မကြာခဏ ပြန်လည် ပြုလုပ်ရမည်။  

> **အကြံပြုချက်**: ပြောင်းရွှေ့ပြီးနောက် `--snapshot-update` (pytest-snapshot) သို့မဟုတ် `--update-snapshots` (syrupy) ဖြင့် စမ်းသပ်မှုများကို သွားပြေးစေသည်။  

---  

## ၃။ စမ်းသပ်မှုတည်မှတ်ချက်များ ပြင်ဆင်ခြင်း  

ယေဘုယျအားဖြင့် assertion ချိုးဖောက်မှုများ -  

| အဟောင်း assertion | ပြဿနာ | အသစ် assertion |  
|--------------|---------|---------------|  
| `client._azure_ad_token_provider is not None` | `AsyncOpenAI` တွင် `_azure_ad_token_provider` attribute မရှိတော့ခြင်း | `isinstance(client, AsyncOpenAI)` နှင့် `"/openai/v1/" in str(client.base_url)` |  
| `client.api_version == "2024-..."` | `OpenAI` / `AsyncOpenAI` တွင် `api_version` မရှိတော့ခြင်း | အကုန် ဖယ်ရှားပေးရန် |  
| `isinstance(client, AsyncAzureOpenAI)` | Client အမျိုးအစား ပြောင်းလဲခြင်း | `isinstance(client, AsyncOpenAI)` |  

---  

## ၄။ စမ်းသပ်မှု fixture များအတွက် ပတ်ဝန်းကျင်အပြောင်းအလဲများ ပြင်ဆင်ခြင်း  

စမ်းသပ်မှုများသည် မကြာခဏ `monkeypatch.setenv` ဖြင့် env var များကို သတ်မှတ်သည်။ ၎င်းအတိုင်း ပြင်ဆင်ရမည် -  

| အဟောင်း env var | အသစ် env var | မှတ်ချက်များ |  
|-------------|-------------|-------|  
| `AZURE_OPENAI_CLIENT_ID` | `AZURE_CLIENT_ID` | Azure Identity SDK ၏ စံနှုန်းအညွှန်းချက် |  
| `AZURE_OPENAI_VERSION` | ဖယ်ရှားရန် | `api_version` မလိုအပ်တော့ခြင်း |  
| `AZURE_OPENAI_API_VERSION` | ဖယ်ရှားရန် | `api_version` မလိုအပ်တော့ခြင်း |  
| `AZURE_OPENAI_ENDPOINT` | `AZURE_OPENAI_ENDPOINT` | ထားရှိရန် ( `base_url` အတွက် လိုအပ်သည်) |  
| `AZURE_OPENAI_CHAT_DEPLOYMENT` | `AZURE_OPENAI_CHAT_DEPLOYMENT` | ထားရှိရန် ( `model` ပါရာမီတာအတွက် deployment name) |  

---  

## ၅။ ပြောင်းရွှေ့ရမည့် စမ်းသပ်တဲ့ကုဒ်ကို ရှာတွေ့ပါ  

```bash
# စမ်းသပ်မှုအထူးအမွေဟောင်းပုံစံများ
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