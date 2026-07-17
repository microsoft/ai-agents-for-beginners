# ပြဿနာဖြေရှင်းခြင်း၊ အန္တရာယ်ဇယားနှင့် သတိထားရန်အချက်များ

## 400 များ ပြဿနာဖြေရှင်းခြင်း

| အမှား | ဖြေရှင်းနည်း |
|-------|-----|
| `missing_required_parameter: tools[0].name` | ကိရိယာဖော်ပြချက်မှာ အဟောင်း Chat Completions nested ပုံစံကို အသုံးပြုထားသည် | `{"type": "function", "function": {"name": ...}}` မှ `{"type": "function", "name": ..., "parameters": ...}` သို့ အလွှာချနိုင်စေရန် — name, description, parameters များကို အထက်လွှာတွင်ထားရန် |
| `unknown_parameter: input[N].tool_calls` | Multi-turn tool ရလဒ်များမှာ အဟောင်း Chat Completions ပုံစံကို အသုံးပြုသည် | `{"role": "assistant", "tool_calls": [...]}` + `{"role": "tool", ...}` ကို `response.output` အချက်များနှင့် + `{"type": "function_call_output", "call_id": ..., "output": ...}` ဖြင့် အစားထိုးပါ |
| `invalid_function_parameters: 'required' is required` | `strict: true` ကိရိယာတွင် `required` array မပါဝင်ခြင်း | `strict: true` ဖြစ်သောအခါ property များအားလုံးကို `required` တွင် စာရင်းပြုစုထားရမည်နှင့် `additionalProperties: false` ကို သတ်မှတ်ရမည် |
| `invalid_function_parameters: 'additionalProperties' is required` | `strict: true` ကိရိယာတွင် `additionalProperties: false` မပါဝင်ခြင်း | parameters object တွင် `"additionalProperties": false` ကို ထည့်သွင်းပါ |
| `invalid input[N].id: Expected an ID that begins with 'fc'` | Few-shot function_call ID ရဲ့ prefix မှားနေခြင်း | Function call ID များသည် `fc_` (ဥပမာ `fc_example1`) ဖြင့် စတင်ရမည်၊ `call_` မဟုတ်နိုင်ပါ |
| `missing_required_parameter: text.format.name` | format dict တွင် `"name"` key ကို ထည့်သွင်းပါ (ဥပမာ `"name": "Output"`) |
| `invalid_type: text.format` | `text.format` သည် string မဟုတ်ဘဲ `type`, `name`, `strict`, `schema` key များပါရှိသော dict ဖြစ်ရန် သေချာပါစေ |
| `invalid input content type` | Chat `text` ထက် `input_text` / `output_text` content types များကို အသုံးပြုပါ |
| `invalid input content type` (image) | Image content သည် `"type": "image_url"` ကို အသုံးပြုနေဆဲ | `"type": "input_image"` သို့ ပြောင်းပါ |
| `Expected object, got string` on `image_url` | `image_url` သည် nested object `{"url": "..."}` အနေဖြင့် ရှိနေဆဲ | `"image_url": "https://..."` သို့ `"image_url": "data:image/...;base64,..."` အဖြစ် ရိုးရှင်းသော string အဖြစ် ပြောင်းပါ |
| `integer below minimum value` for `max_output_tokens` | Azure OpenAI တွင် အနည်းဆုံး ၁၆ ဖြစ်သည်။ စမ်းသပ်မှုအတွက် ၅၀ ကျော်၊ ထုတ်လုပ်မှုအတွက် ၁၀၀၀ ကျော် အသုံးပြုပါ |
| `429 Too Many Requests` during streaming | Rate limit ဖြစ်သည်။ streaming ကို `try/except` ဖြင့် ဝိုင်းကပ်ပြီး အမှား JSON ကို frontend သို့ ပို့ပါ၊ backoff/retry ကို တပ်ဆင်ပါ |
| `KeyError: 'innererror'` on content filter error | Responses API တွင် content filter error body structure ပြောင်းလဲမှု | Chat Completions တွင် `error.body["innererror"]["content_filter_result"]` ကို အသုံးပြုခဲ့သည့်အစား Responses API သည် `error.body["content_filters"][0]["content_filter_results"]` (plural, array အတွင်း) ကို အသုံးပြုသည်။ `innererror` အဆင့်အားလုံးပြင်ရန်လိုသည် |

---

## ရွှေ့ပြောင်းဆဲအန္တရာယ်ဇယား

| လက္ခဏာ | ခန့်မှန်းလွယ်ကူသော အမှား | ဖြေရှင်းနည်း |
|---------|---------------|-----|
| အလွယ်တကူ ဖြတ်တောက်သော `output_text` / အဖြေတစ်စိတ်တစ်ပိုင်း | reasoning မော်ဒယ်များအတွက် `max_output_tokens` နည်းပါးခြင်း | `max_output_tokens=1000` သို့မဟုတ် ပိုမြင့်ရန် သတ်မှတ်ပါ — reasoning token များသည် ကန့်သတ်ချက်အတွင်း ပါဝင်သည် |
| `400 invalid_type: text.format` | `text.format` dict မဟုတ်ဘဲ `response_format` string ဖြတ်ပို့ခြင်း | `text={"format": {"type": "json_schema", "name": "...", "strict": True, "schema": {...}}}` ကို အသုံးပြုပါ |
| `/openai/v1/responses` တွင် `404 Not Found` ဖြစ်ခြင်း | `base_url` မှားနေခြင်း — `/openai/v1/` suffix မပါဝင်ခြင်း | `base_url=f"{endpoint}/openai/v1/"` (slash ပါသင့်) ဖြစ်စေရန် သေချာစေပါ |
| `401 Unauthorized` ဖြစ်ခြင်း `OpenAI()` သို့ ပြောင်းပြောင်းလဲလဲမှုအောက်မှာ | `api_key` မသတ်မှတ်ခြင်း သို့မဟုတ် token provider မမှန်ကန်စွာမပေးခြင်း | EntraID အတွက် `api_key=token_provider` (callable) ဖြစ်ရမည်။ API key အတွက် `api_key=os.environ["AZURE_OPENAI_API_KEY"]` ဖြစ်ရမည် |
| Model က `deployment not found` ပြန်လာခြင်း | `model` param သည် Azure deployment နာမည်နှင့် ကိုက်ညီမှုမရှိခြင်း | `model=os.environ["AZURE_OPENAI_DEPLOYMENT"]` ကို အသုံးပြုပါ — ဒီသည် deployment နာမည်ဖြစ်ပြီး model နာမည်မဟုတ်ပါ |
| `json.loads(resp.output_text)` မှ `JSONDecodeError` ထွက်ခြင်း | Schema မအားတင်းစွာ သတ်မှတ်ခြင်း မရှိခြင်း သို့မဟုတ် model မှ strict JSON မပံ့ပိုးခြင်း | schema တွင် `"strict": True` သတ်မှတ်ပြီး၊ model သည် ဖွဲ့စည်းထားသော output ကို ပံ့ပိုးကြောင်း သေချာစေပါ |
| Streaming တွင် `delta` event မထွက်ခြင်း | မှားယွင်းသော event type ကို စစ်ဆေးခြင်း | Chat ၏ `chat.completion.chunk` မဟုတ်ဘဲ `event.type == "response.output_text.delta"` ကို စစ်ဆေးပါ |
| ရွှေ့ပြောင်းပြီးနောက် image input တွင် `400` error ဖြစ်ခြင်း | Image content type မပြောင်းလဲခြင်း | `"type": "image_url"` ကို `"type": "input_image"` သို့ ပြောင်းပြီး `"image_url": {"url": "..."}` ကို `"image_url": "..."` (string ရိုးရှင်း) သို့ ပြောင်းပါ |
| Tool calls သည် အဆုံးမရှိလည်ပတ်ခြင်း | follow-up `input` ထဲမှာ tool result ပျောက်နေခြင်း | tool ပြီးနောက် `{"type": "function_call_output", "call_id": ..., "output": ...}` item ကို နောက်တစ်ကြိမ် request ၏ `input` ထဲ ထည့်ပါ |
| GPT-5 သို့မဟုတ် o-series နဲ့ `temperature` error ဖြစ်ခြင်း | ၁ မဟုတ်သော `temperature` တန်ဖိုး သတ်မှတ်ခြင်း | GPT-5 နှင့် o-series (o1, o3-mini, o3, o4-mini) မော်ဒယ်များအတွက် `temperature` ကို ဖျက်ပါ သို့မဟုတ် `1` သတ်မှတ်ပါ |
| o-series နှင့် `top_p` error ဖြစ်ခြင်း | `top_p` မပံ့ပိုးပါ | o-series မော်ဒယ်များအား ရည်ရွယ်၍ `top_p` ကို ဖျက်ပါ |
| `max_completion_tokens` ကို အလိုအလျောက် မသိရှိခြင်း | Azure ပိုင်းအသုံးပြု parameter ဖြစ်ခြင်း | `max_completion_tokens` ကို `max_output_tokens` ဖြင့်အစားထိုးပါ။ o-series အတွက် ၄၀၉၆+ သတ်မှတ်ပါ (reasoning token များသည် ကန့်သတ်ချက်တွင် ပါဝင်သည်) |
| o-series မှ အလုံအလောက်မရှိသော အဖြေ သို့မဟုတ် ဖြတ်တောက်သော output ဖြစ်ခြင်း | `max_output_tokens` နည်းပါးခြင်း | o-series သည် reasoning token များကို အတွင်းပိုင်းတွင် သုံးသည်။ `max_output_tokens=4096` သို့မဟုတ် ပိုမြင့်သောတန်ဖိုး သတ်မှတ်ပါ — ၅၀–၁၀၀၀ မဟုတ်ပါ |
| `400 integer_below_min_value` for `max_output_tokens` | တန်ဖိုး ၁၆ အောက် ဖြစ်ခြင်း | Azure OpenAI မှ `max_output_tokens >= 16` ကို တင်းကြပ်စွာ ကျင့်သုံးသည်။ smoke test များအတွက် ၅၀ ကျော်၊ ထုတ်လုပ်မှုအတွက် ၁၀၀၀ ကျော် အသုံးပြုပါ |
| `429 Too Many Requests` mid-stream ဖြစ်ခြင်း | Azure OpenAI ဖြင့် rate limit ဖြစ်နေခြင်း | Stream များသည် error handling မရှိလျှင် ထပ်တလဲလဲဖြတ်တောက်သွားသည်။ `async for event in await coroutine:` ကို အမြဲ `try/except` ဖြင့် ဝိုင်းကပ်ကာ frontend သို့ `{"error": str(e)}` ကို ပေးပို့ပါ |
| `AzureDeveloperCliCredential` → `CredentialUnavailableError` ဖြစ်ခြင်း | tenant မှားနေခြင်း သို့မဟုတ် login မပြုလုပ်ခြင်း | `tenant_id=os.getenv("AZURE_TENANT_ID")` ကို အတိအကျ ပေးပို့ပါ။ ဒေသတွင်းတွင် `azd auth login --tenant <tenant-id>` ကို ပြုလုပ်ပါ |
| GitHub Models (`models.github.ai`) အသုံးပြု၍ `404 Not Found` ဖြစ်ခြင်း | GitHub Models သည် Responses API ကို မပံ့ပိုးပါ | GitHub Models ကုဒ်လမ်းကြောင်းအား လုံးဝ ဖယ်ရှားပါ။ Azure OpenAI, OpenAI သို့မဟုတ် Responses ကို ပံ့ပိုးသည့် ကိုက်ညီသော local endpoint (ဥပမာ Ollama) ကို သီးသန့် အသုံးပြုပါ |
| MAF `OpenAIChatCompletionClient` သည် Chat Completions ကို ဆက်လက် အသုံးပြုနေခြင်း | MAF ဆန်းသစ် client ကို 1.0.0+ မှ အသုံးမပြုခြင်း | MAF 1.0.0+ တွင် `OpenAIChatClient` သည် default ဖြင့် Responses API ကို သုံးပါသည်။ `OpenAIChatCompletionClient` ကို `OpenAIChatClient` ဖြင့် အစားထိုးပါ။ 1.0.0 မတိုင်မီ version တွင် `agent-framework-openai>=1.0.0` သို့ အဆင့်မြှင့်ပါ |
| LangChain agent မှ tool calls ဖြင့် အလွတ် သို့မဟုတ် မအောင်မြင်ခြင်း | `ChatOpenAI` မှ Responses API သုံးမထားခြင်း | `ChatOpenAI(...)` တွင် `use_responses_api=True` ထည့်သွင်းပါ။ response messages တွင် `.content` ကို `.text` သို့ အသစ်ပြောင်းပါ |
| Content filter error handler တွင် `KeyError: 'innererror'` ဖြစ်ခြင်း | Responses API တွင် error body structure ပြောင်းလဲမှု | `error.body["innererror"]["content_filter_result"]["jailbreak"]` ကို `error.body["content_filters"][0]["content_filter_results"]["jailbreak"]` ဖြင့် ပြုလုပ်ပါ။ `innererror` wrapper မရှိတော့ပါ။ content filter အသေးစိတ်များသည် `content_filters` array ထဲရှိပြီး၊ entry တစ်ခုစီတွင် `content_filter_results` (ပေါင်းစည်း) ပါဝင်သည် |
| Raw HTTP call `/openai/deployments/.../chat/completions` မှ 404 ပြန်လာခြင်း | အဟောင်း Chat Completions REST endpoint ဖြစ်ခြင်း | URL ကို `/openai/v1/responses` ချိန်ညှိပါ။ request body တွင် `messages` → `input` ပြောင်းပြီး `max_output_tokens` နှင့် `store: false` ထည့်ခြင်း၊ `api-version` query param ကို ဖယ်ရှားခြင်း။ response ကို parsing လုပ်ရာတွင် `choices[0].message.content` → `output[0].content[0].text` အဖြစ် ပြောင်းပါ (မှတ်ချက်: `output_text` သည် SDK အဆင်ပြေမှု property ဖြစ်ပြီး raw REST JSON တွင် မပါ) |

---

## သတိထားရန်အချက်များ

1. ယခင်တွင် Chat Completions ကို စကားပြောစတိတ်တာအတြက္ အသုံးပြုခဲ့သည်ဆိုပါက Responses နှင့်အတူ သင်၏ စတိတ်ကို ကိုယ်တိုင် စီမံခန့်ခွဲပါ။
2. အဟောင်း `max_tokens` ထက် `max_output_tokens` ကို ဦးစားပေး အသုံးပြုပါ။
3. `gpt-5` သို့ ရွှေ့ပြောင်းသည့်အခါ `temperature` ကို မသတ်မှတ်ရသေးပါက သတ်မှတ်ရာတွင် `1` ဖြစ်စေရန် သေချာစေပါ။
4. Chat ၏ `content[].type: "text"` ကို Responses ၏ `content[].type: "input_text"` ဖြင့် အစားထိုးပါ၊ သုံးစွဲသူ/စနစ် input များအတွက်ဖြစ်သည်။
5. `text.format` အတွက် သင့်တော်သော dict (ဥပမာ `{"type": "json_schema", "name": "Output", "schema": ..., "strict": True}`) ကို ပေးပါ၊ ရိုးရှင်း string မဟုတ်ပါ။
6. Responses တွင် `seed` parameter မပံ့ပိုးတော့ပါ; request များမှ ဖယ်ရှားပါ။
7. **Reasoning**: မူရင်းကုဒ်တွင် သုံးထားခဲ့မှသာပါဝင်စေရန် `reasoning` ကိုသာ ထည့်ပါ။  မပါခဲ့သော API call များတွင် `reasoning` ထည့်မပါနှင့် — reasoning မဟုတ်သော မော်ဒယ်များတွင် ၎င်း parameter ကို မပံ့ပိုးပါ။
8. **`max_output_tokens` အရွယ်အစား**: reasoning မော်ဒယ်များ (GPT-5-mini, GPT-5, o-series) အတွက် `max_output_tokens=4096` သို့မဟုတ် ပိုမြင့်သောတန်ဖိုး သတ်မှတ်ပါ — ၅၀–၁၀၀၀ မဟုတ်ပါ။ မော်ဒယ်သည် မမြင်သာသော output ထုတ်မပေးမီ reasoning token များကို အတွင်းပိုင်းတွင် အသုံးပြုသည်; နည်းလွန်းသောကန့်သတ်ချက်သည် တစ်စိတ်တစ်ပိုင်းဖြတ်တောက်ခြင်း သို့မဟုတ် အလွတ်ဖြေများ ဖြစ်စေသည်။
9. **O-series `max_completion_tokens`**: မူရင်းကုဒ်တွင် `max_completion_tokens` (o-series အတွက် Azure ကွဲပြားသော parameter) ကို သုံးခဲ့ပါက `max_output_tokens` ဖြင့် အစားထိုးပါ။ Responses API တွင် `max_completion_tokens` ကို လက်ခံမည် မဟုတ်ပါ။
10. **O-series `reasoning_effort`**: မူရင်းကုဒ်တွင် `reasoning_effort` (low/medium/high) ကို သုံးပါက Responses API call တွင် `reasoning={"effort": "<value>"}` သို့ ရွှေ့ပြောင်းပါ။
11. **O-series streaming အနား မပေးရာ**: O-series မော်ဒယ်များသည် output ထုတ်လိုသည်မတိုင်မီ အတွင်းပိုင်း reasoning ကို လုပ်ဆောင်သည်။ streaming နှင့်အတူ ပထမဆုံး `response.output_text.delta` အဖြစ်ဖြစ်သော event မထွက်မီ ကြာမြင့်ချိန် ကြီးနေရမည်။ ၎င်းသည် သာမန်ဖြစ်ပါသည် — မော်ဒယ်သည် reasoning လုပ်နေသည်၊ ခြိမ်းခြောက်ခြင်း မဟုတ်ပါ။
9. **`_azure_ad_token_provider` ပျောက်ကွဲသွားပြီ**: `AsyncOpenAI` / `OpenAI` တွင် `_azure_ad_token_provider` attribute မရှိတော့ပါ။ ၎င်း attribute ကို ဝင်ရောက်သုံးသည့် စမ်းသပ်မှု သို့မဟုတ် ကုဒ်များသည် `AttributeError` နှင့် ပျက်သိမ်းမည်။ token provider ကို `api_key` အဖြစ် ပေးပြီး client object တွင် စစ်ဆေး၍ မရပါ။
10. **Snapshot / golden ဖိုင်များ**: စမ်းသပ်မှု suite သည် snapshot test များ အသုံးပြုပါက Chat Completions streaming shape (`choices[0]`, `content_filter_results`, `function_call` စသည့်) ပါဝင်သည့် snapshot ဖိုင်များအားလုံးကို များသည် Responses shape အသစ်ဖြင့် ပြောင်းလဲရမည်။ ၎င်းသည် လွယ်ကူစွာ ပျက်ကွက်မှု ဖြစ်ပေါ်စေသည်။
11. **Mock monkeypatch လမ်းကြောင်း**: monkeypatch target သည် `openai.resources.chat.AsyncCompletions.create` မှ `openai.resources.responses.AsyncResponses.create` (သို့မဟုတ် sync အတွက် `Responses.create`) သို့ ပြောင်းသွားသည်။ အဟောင်းလမ်းကြောင်းကို အသုံးပြုလျှင် မည်သည့် result မမျှ မဖြစ်ပေါ်ဘဲ mock လက်မခံတော့ပါ၊ စမ်းသပ်မှုများသည် တကယ် API ကို ထိတွေ့ရမည်၊ မအောင်မြင်ရပါ။
12. **`input` မဟုတ် `messages`**: Mock function များသည် `kwargs.get("input")` ကို ဖတ်ရမည်၊ `kwargs.get("messages")` မဟုတ်ပါ။ Responses API သည် စကားပြောသမိုင်းအတွက် `input` ကို အသုံးပြုသည်။
13. **Env var နာမည်ပေးခြင်း**: Azure Identity SDK သည် ManagedIdentityCredential(client_id=...) အတွက် `AZURE_OPENAI_CLIENT_ID` မဟုတ်ဘဲ `AZURE_CLIENT_ID` ကို အသုံးပြုသည်။ စမ်းသပ်မှုများ၊ `.env` ဖိုင်များ၊ app settings နှင့် Bicep/infra များတွင် ပြန်ပြင်ပါ။
14. **`max_output_tokens` အနည်းဆုံး သတ်မှတ်ချက် ၁၆ ဖြစ်သည်**: Azure OpenAI သည် ၁၆ အောက်တန်ဖိုးကို `400 integer_below_min_value` ဖြင့် ငြင်းဆန်သည်။ smoke test များအတွက် ၅၀ အသုံးပြုပါ၊ ထုတ်လုပ်မှုအတွက် ၁၀၀၀+ ကို အသုံးပြုပါ။ အဟောင်း `max_tokens` တွင် ဤအနည်းဆုံး သတ်မှတ်ချက် မရှိပါ။
15. **`AzureDeveloperCliCredential` အတွက် `tenant_id`**: Azure OpenAI resource သည် အခြား tenant တွင် ရှိပါက `tenant_id` ကို ဖြည့်စွက်ပေးရမည် — `AzureDeveloperCliCredential(tenant_id=os.getenv("AZURE_TENANT_ID"))`။ မပါလျှင် credential သည် အမှားသော tenant ကို တမ်းညှိပြီး `401` ပြန်လည်ပေးမည်။
16. **Rate limits သည် streaming တွင် ကွဲပြားစွာ မြင်သာစေသည်**: Chat Completions ၌ ၄၂၉ သည် စတင်ခြင်းကို တားဆီးခဲ့သည်။ Responses API streaming ၌ ၄၂၉ သည် **stream မဖြတ်မီ** ဖြစ်နိုင်ပြီး async iterator တွင် exception ဖြစ်ပေါ်စေသည်။ streaming loop ကို အမြဲ `try/except` ဖြင့် ဝိုင်းကပ်ပြီး error JSON line တစ်ကြောင်း frontend သို့ ပေးပို့၍ လုံခြုံစွာ ပြုပြင်နိုင်စေရန် လုပ်ဆောင်ပါ။

၁၇။ **ဝက်ဘ်အက်ပ်များအတွက် Streaming အမှားကို ကိုင်တွယ်ခြင်းသည် မဖြစ်မနေနည်းပါ**- အနည်းဆုံး `try: async for event in await coroutine: ... except Exception as e: yield json.dumps({"error": str(e)})` အပုံစံကို အသုံးပြုရန်လိုသည်။ ယင်းမပါဘဲ SSE/JSONL stream သည် ဆာဗာဘက်မှ အမှားတစ်ခုဖြစ်သမျှတစ်ခုဖြစ်လျှင် တိတ်ဆိတ်ပျောက်ကွယ်သွားပြီး ဖရွန့်အင်ပိုင်းမှာ တောင့်တင်းနေပါသည်။
၁၈။ **Tool အကြောင်းအရာများကို flat format ဖြင့်သာ အသုံးပြုရမည်**- Responses API သည် `{"type": "function", "name": ..., "parameters": ...}` ကိုမျှော်လင့်သည် — Chat Completions မှ nested `{"type": "function", "function": {"name": ..., "parameters": ...}}` ကို မရရှိပါ။ ၎င်းသည် function-calling ကုဒ်များတွင် အများဆုံး ဖြစ်ပွားသော ပြောင်းရွှေ့မှု အမှားဖြစ်သည်။
၁၉။ **`pydantic_function_tool()` သည် လိုက်ဖက်မှုမရှိပါ**- `openai.pydantic_function_tool()` ဟူသည့် ကူညီဖန်တီးသူသည် ဟောင်းသော nested format ကို Generate လုပ်ဆောင်ထားဆဲဖြစ်သည်။ ၎င်းကို `responses.create()` နှင့် မပေါင်းသုံးရ။
၂၀။ **Tool ရလဒ်များအတွက် `function_call_output` ကို အသုံးပြုရပြီး `role: tool` မဟုတ်ပါ**- Tool တစ်ခုကို သုံးပြီးနောက် `{"type": "function_call_output", "call_id": ..., "output": ...}` ကို ထည့်ရန် လိုသည် — `{"role": "tool", "tool_call_id": ..., "content": ...}` မဟုတ်ပါ။ အကူအညီပေးသူ၏ Tool မှ တောင်းဆိုမှုအတွက် `messages.extend(response.output)` ကို သုံးသည် — လက်ဖြင့် `{"role": "assistant", "tool_calls": [...]}` dictionary မဟုတ်ပါ။
၂၁။ **`strict: true` သုံးရာတွင် `required` + `additionalProperties: false` လိုအပ်သည်**- Tool တွင် `strict: true` ကို သုံးလျှင် property တစ်ခုချင်းစီသည် `required` အတွင်းတွင် ရှိရမည်၊ `additionalProperties` သည် false ဖြစ်ရမည်။ မဖြစ်မျှနှင့် ၄၀၀ အမှား ဖြစ်ပေါ်ပါသည်။
၂၂။ **Function call IDs တွင် အထူးအတိုင်းအတာ prefix များရှိသည်**- Few-shot `function_call` အရာများကို `input` တွင် ပေးသည့်အခါ `id` field သည် `fc_` ဖြင့် စတင်ရမည်၊ `call_id` field သည် `call_` ဖြင့် စတင်ရမည် (ဥပမာ `"id": "fc_example1", "call_id": "call_example1"`)။ ဟောင်းသော Chat Completions `call_` prefix ကို `id` အတွက် သုံးခြင်းသည် ငြင်းဆိုခံရသည်။
၂၃။ **GitHub Models သည် Responses API ကို မထောက်ပံ့ပါ**- အက်ပ်တွင် GitHub Models code path ရှိပါက (`base_url` သည် `models.github.ai` သို့မဟုတ် `models.inference.ai.azure.com` ကို ညွှန်ပြနေပါက) ၎င်းကို အလိုလျှော့ဖျက်လိုက်ပါ။ ပြောင်းရွှေ့ရာတစ်ခုမရှိပါ — Azure OpenAI, OpenAI သို့မဟုတ် ကိုက်ညီသော ဒေသတွင်း Endpoint ကို အသုံးပြုရန် ပြောင်းပါ။
၂၄။ **Content filter error body ဖွဲ့စည်းမှု ပြောင်းလဲသွားပြီ**- Chat Completions အမှားများသည် `error.body["innererror"]["content_filter_result"]` (တစ်ခုတည်း) ကို အသုံးပြုသော်လည်း Responses API အမှားများသည် `error.body["content_filters"][0]["content_filter_results"]` (များစွာ၊ Array အတွင်း) ကို အသုံးပြုသည်။ `innererror` key သည် မရှိတော့ပါ။ `innererror` တန်းတိုက်အသုံးပြုသည့် ကုဒ်များသည် runtime တွင် `KeyError` ထွက်ပေါ်လိမ့်မည် — ၎င်းသည် content filter မှ ထိုးရိုက်ချိန်တွင်သာ တွေ့ရှိလို့ ချွေမှတ်ရန်ခက် စေသည်။ ပြောင်းရွှေ့မှုအတွင်း `innererror` ကို အမြဲဂရုပ်လုပ်ပါ။
၂၅။ **Raw HTTP ခေါ်ဆိုမှုတွေမှာ URL + body ပြင်ဆင်ရန်လိုသည်**- Azure OpenAI REST ကို တိုက်ရိုက် ခေါ်ဆိုနေသော အက်ပ်များ (`requests`, `httpx`, `aiohttp` အသုံးပြု၍ `/openai/deployments/{name}/chat/completions?api-version=...` ထဲမှ ခေါ်ဆိုခြင်း) သည် `/openai/v1/responses` သို့ ပြောင်းရန်လိုသည်။ Request body တွင် `messages` အစား `input` ကိုသုံးပြီး `max_output_tokens` နှင့် `store` ကို လိုအပ်သည်၊ `api-version` query parameter ကို ဖယ်ရှားသည်။ Response Body ဖော်ပြချက်သည် `output[0].content[0].text` တွင်ရှိသည် — **မဟုတ်ပါ** `output_text` ကို၊ ၎င်းသည် SDK အဆင်ပြေမှု property ဖြစ်ပြီး raw REST JSON တွင် မပါဝင်ပါ။

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ပြောကြားချက်**
ဤစာတမ်းကို AI ဘာသာပြန်ဝန်ဆောင်မှု [Co-op Translator](https://github.com/Azure/co-op-translator) အသုံးပြု၍ ဘာသာပြန်ထားပါသည်။ ကျွန်ုပ်တို့သည် တိကျမှန်ကန်မှုအတွက် ကြိုးပမ်းနေသော်လည်း၊ စက်ကိရိယာဘာသာပြန်ခြင်းများတွင် အမှားများ သို့မဟုတ် မှားယွင်းချက်များ ပါဝင်နိုင်ကြောင်း သတိပြုပါရန် လိုအပ်ပါသည်။ မူလစာတမ်းကို မူရင်းဘာသာဖြင့်သာ ယုံကြည်စိတ်ချရသော အချက်အလက်အဖြစ် သတ်မှတ်သင့်သည်။ အရေးကြီးသည့် သတင်းအချက်အလက်များအတွက် ပရော်ဖက်ရှင်နယ် လူသားဘာသာပြန်သူဝန်ဆောင်မှုကို အကြံပြုပါသည်။ ဤဘာသာပြန်ချက်ကို အသုံးပြုခြင်းမှ ဖြစ်ပေါ်လာသော နားလည်မှုကွာခြားမှုများ သို့မဟုတ် မမှန်ကန်သော အသုံးပြုမှုများအတွက် ကျွန်ုပ်တို့ တာဝန်မခံပါ။
<!-- CO-OP TRANSLATOR DISCLAIMER END -->