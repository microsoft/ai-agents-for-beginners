# ပြဿနာဖြေရှင်းခြင်း၊ အန္တရာယ်ဇယားနှင့် ထိခိုက်နိုင်သောအချက်များ

## 400 အမှားများ ပြဿနာဖြေရှင်းခြင်း

| အမှား | ပြင်ဆင်မှု |
|-------|-----|
| `missing_required_parameter: tools[0].name` | Tools သတ်မှတ်ချက်သည် အဟောင်း Chat Completions nested ပုံစံ အသုံးပြုသည် | `{"type": "function", "function": {"name": ...}}` မှ `{"type": "function", "name": ..., "parameters": ...}` သို့ ခြုံပုံပြင်ရန် — name၊ description၊ parameters များကို ထိပ်ဆုံးမှာထားရန် |
| `unknown_parameter: input[N].tool_calls` | Multi-turn tool نتیجه များသည် အဟောင်း Chat Completions ပုံစံအသုံးပြုသည် | `{"role": "assistant", "tool_calls": [...]}` + `{"role": "tool", ...}` ကို `response.output` အရာများနှင့် `{"type": "function_call_output", "call_id": ..., "output": ...}` ဖြင့်အစားထိုးရန် |
| `invalid_function_parameters: 'required' is required` | `strict: true` tools တွင် `required` array မပါရှိခြင်း | `strict: true` ဖြစ်သောအခါ properties များအားလုံးကို `required` တွင်စာရင်းပြုလုပ်ထားရမည်။ `additionalProperties: false` ကိုလည်းသတ်မှတ်ရမည် |
| `invalid_function_parameters: 'additionalProperties' is required` |  `strict: true` tools တွင် `additionalProperties: false` မပါရှိခြင်း | parameters object ထဲတွင် `"additionalProperties": false` ကို ထည့်သည် |
| `invalid input[N].id: Expected an ID that begins with 'fc'` | Few-shot function_call ID သည် prefix မှားနေခြင်း | Function call IDs သည် `fc_` (ဥပမာ `fc_example1`) ဖြင့်စတင်ရမည်၊ `call_` ဖြင့်မစတင်ရ။ |
| `missing_required_parameter: text.format.name` | format dict တွင် `"name"` key ထည့်ရန် (ဥပမာ `"name": "Output"`) |
| `invalid_type: text.format` | `text.format` သည် string မဟုတ်ပဲ dict ဖြစ်ရမည်၊ keys များမှာ `type`, `name`, `strict`, `schema` ဖြစ်ပါသည် |
| `invalid input content type` | Chat `text` မဟုတ်ဘဲ `input_text`/`output_text` content types အသုံးပြုရန် |
| `invalid input content type` (image) | အရုပ်အချက်အလက်တွင် `"type": "image_url"` ကို သုံးနေဆဲ | `"type": "input_image"` သို့ ပြောင်းရန် |
| `Expected object, got string` on `image_url` | `image_url` သည် နက် nested object `{"url": "..."}` ဖြစ်နေခြင်း | ဤ parameter ကို string ပုံစံသို့ ပြောင်းရန် - `"image_url": "https://..."` သို့မဟုတ် `"image_url": "data:image/...;base64,..."` |
| `integer below minimum value` for `max_output_tokens` | Azure OpenAI တွင် အနည်းဆုံး ၁၆ ဖြစ်ပါသည်။ စမ်းသပ်မှုများအတွက် ၅၀ ကျော်၊ ထုတ်လုပ်မှုအတွက် ၁၀၀၀ ကျော်ကိုသုံးပါ။ |
| `429 Too Many Requests` during streaming | Rate limit ဖြစ်နေသည်။ streaming ကို `try/except` ဖြင့် ဖုံးကွယ်၊ frontend သို့ error JSON ထုတ်ပေးပြီး backoff/retry ကို ကောင်းစွာ ပြုလုပ်ပါ။ |
| `KeyError: 'innererror'` on content filter error | Response API တွင် content filter error body ပုံစံ ပြောင်းလဲခြင်း | Chat Completions သည် `error.body["innererror"]["content_filter_result"]` သုံးသော်လည်း Responses API သည် `error.body["content_filters"][0]["content_filter_results"]` (plural နှင့် array ထဲ) သုံးသည်။ `innererror` လမ်းကြောင်းများအားလုံး ပြန်ရေးရန်။ |

---

## ပြောင်းရွှေ့မှု အန္တရာယ်ဇယား

| ရောဂါလက္ခဏာ | ဖြစ်နိုင်သော အမှား | ပြင်ဆင်မှု |
|---------|---------------|-----|
| output_text စာသားဖျက်ကွက် / ဖြတ်တောက်ထားသော တုံ့ပြန်ချက် | `max_output_tokens` သည် reasoning မော်ဒယ်များအတွက် အနည်းငယ်过于သေးသည် | `max_output_tokens=1000` သို့ပို၍ တန်ဖိုးထားရန် — reasoning tokens များသည် ကန့်သတ်ချက်တွင်ပါဝင်သည် |
| `400 invalid_type: text.format` | `text.format` dict မဟုတ်ပဲ `response_format` string ဖြင့်ပေးထားခြင်း | `text={"format": {"type": "json_schema", "name": "...", "strict": True, "schema": {...}}}` ကိုအသုံးပြုရန် |
| `404 Not Found` on `/openai/v1/responses` | `base_url` မှားနေခြင်း — `/openai/v1/` suffix မပါရှိခြင်း | `base_url=f"{endpoint}/openai/v1/"` (slash နဲ့လိုက်) ဖြစ်ရန် သေချာစေပါ။ |
| `401 Unauthorized` after switching to `OpenAI()` | `api_key` မထည့်ထားဘဲ သို့မဟုတ် token provider မမှန်ကန်စွာ မပေးခြင်း | EntraID အတွက်: `api_key=token_provider` (callable ဖြစ်သည်။) API key အတွက်: `api_key=os.environ["AZURE_OPENAI_API_KEY"]` |
| Model returns `deployment not found` | `model` parameter သည် Azure deployment နာမည်နှင့် မကိုက်ညီခြင်း | `model=os.environ["AZURE_OPENAI_DEPLOYMENT"]` များကိုသုံးပါ — deployment နာမည်ဖြစ်သည်၊ model နာမည် မဟုတ်ပါ။ |
| `json.loads(resp.output_text)` သည် `JSONDecodeError` ပေးသည် | schema မအားသတ်မတ်ထားခြင်း သို့မဟုတ် model သည် strict JSON ကို မထောက်ပံ့ခြင်း | schema တွင် `"strict": True` သေချာထားပြီး model သည် ဖွဲ့စည်းထားသော ပြန်လည်ထုတ်ဝေမှုကို ထောက်ပံ့သည်ဟု အတည်ပြုရန် |
| Streaming မှာ `delta` event မပေးပဲဖြုတ်တယ် | event type မှားစစ်နေခြင်း | Chat ၏ `chat.completion.chunk` မဟုတ်ဘဲ `event.type == "response.output_text.delta"` ကို စစ်ဆေးရန် |
| ပြောင်းရွှေ့ပြီးနောက် image input တွင် `400` အမှားများ | Image content type မပြောင်းလဲထားခြင်း | `"type": "image_url"` → `"type": "input_image"` နှင့် `"image_url": {"url": "..."}` → `"image_url": "..."` (string ပုံစံ) ပြောင်းပါ။ |
| Tool calls က အချိန်မကုန် အလွှာမတတ်ပဲကွင်းဆက်ပြန်လုပ်နေသည် | follow-up `input` တွင် tool result မပါရှိခြင်း | tool ကို 실행ပြီးနောက် `{"type": "function_call_output", "call_id": ..., "output": ...}` item ကို နောက်တစ်ကြိမ် request ထဲ input တွင် ထည့်ပါ။ |
| GPT-5 သို့မဟုတ် o-series မော်ဒယ်များတွင် `temperature` error ဖြစ်ခြင်း | `temperature` တွင် ၁ မဟုတ်သော တန်ဖိုးထည့်ထားခြင်း | GPT-5 နှင့် o-series မော်ဒယ်များ (o1, o3-mini, o3, o4-mini) အတွက် `temperature` ကိုဖယ်ရှားပါ သို့မဟုတ် `1` အဖြစ် သတ်မှတ်ပါ။ |
| o-series တွင် `top_p` error ဖြစ်ခြင်း | `top_p` သည် မထောက်ပံ့ခြင်း | o-series မော်ဒယ်များတွင် `top_p` ကို ဖယ်ရှားပါ။ |
| `max_completion_tokens` ကို ရှာမတွေ့ | Azure အထူး parameter ကို သုံးခြင်း | `max_completion_tokens` ကို `max_output_tokens` ဖြင့် အစားထိုးပါ။ o-series အတွက် 4096+ သတ်မှတ်ရန် (reasoning tokens က ကန့်သတ်ချက်ထဲတွင် ပါဝင်သည်)။ |
| o-series မှ ထွက်ရှိသော output စာသားသည် အလွတ် သို့မဟုတ် ဖြတ်တောက်ခံထားသည် | `max_output_tokens` သေးလွန်းခြင်း | o-series သည် reasoning tokens ကို အတွင်းပိုင်း အသုံးပြုသည်။ `max_output_tokens=4096` သို့မဟုတ် ပိုစီတန်ဖိုးထားပေးပါ၊ ၅၀၀ – ၁၀၀၀ မဟုတ်ပါ။ |
| `400 integer_below_min_value` for `max_output_tokens` | တန်ဖိုးသည် ၁၆ အောက် | Azure OpenAI သည် `max_output_tokens >= 16` ကို တင်းကျပ်စွာလိုအပ်သည်။ စမ်းသပ်မှုများအတွက် ၅၀ ကျော်၊ ထုတ်လုပ်မှုအတွက် ၁၀၀၀ ကျော် သတ်မှတ်ပါ။ |
| `429 Too Many Requests` mid-stream ဖြစ်ခြင်း | Azure OpenAI မှ rate limit ခံထားခြင်း | Stream သည် error handling မပါဘဲ တိတ်ဆိတ်တောက်သွားနိုင်သည်။ `async for event in await coroutine:` ကို အသုံးပြုသည့် streaming loop ကို အမြဲ try/except ဖြင့် ဖုံးကွယ်ပြီး `{"error": str(e)}` ကို frontend ထံ ထုတ်ပေးပါ။ |
| `AzureDeveloperCliCredential` → `CredentialUnavailableError` ဖြစ်ခြင်း | tenant မှားနေခြင်း သို့မဟုတ် log in မလုပ်ထားခြင်း | `tenant_id=os.getenv("AZURE_TENANT_ID")` ကို ထိပ်မိန့်သတ်ပေးပါ။ ဒေသတွင်း `azd auth login --tenant <tenant-id>` ကို ပြုလုပ်ပါ။ |
| GitHub Models (`models.github.ai`) အသုံးပြုချိန် `404 Not Found` ဖြစ်ခြင်း | GitHub Models မှ Responses API ကို မထောက်ပံ့ခြင်း | GitHub Models code path ကို လုံးဝ ဖယ်ရှားပြီး Azure OpenAI၊ OpenAI သို့ ယခုသုံးနိုင်သည့် local endpoint (ဥပမာ Ollama with Responses support) ကို သုံးပါ။ |
| MAF `OpenAIChatCompletionClient` သည် Chat Completions ကို အသုံးပြုနေဆဲ | MAF 1.0.0+ တွင် အဟောင်း client အသုံးပြုနေခြင်း | MAF 1.0.0+ မှာ `OpenAIChatClient` သည် ပုံမှန်အားဖြင့် Responses API ကို အသုံးပြုသည်။ `OpenAIChatCompletionClient` ကို `OpenAIChatClient` ဖြင့် ပြောင်းလဲပါ။ pre-1.0.0 ဝေထုတ်မှုများအတွက် `agent-framework-openai>=1.0.0` သို့ တိုးမြှင့်ပါ။ |
| LangChain agent တွင် tool calls တွင် မျက်မှောက်မရှိ သို့မဟုတ် မအောင်မြင်ခြင်း | `ChatOpenAI` သည် Responses API ကို မသုံးခြင်း | `ChatOpenAI(...)` တွင် `use_responses_api=True` ထည့်လိုက်ပါ။ `.content` ကို `.text` သို့ ပြောင်းပါ။ |
| content filter error handler တွင် `KeyError: 'innererror'` ဖြစ်ခြင်း | Responses API တွင် error body ပုံစံ ပြောင်းလဲခြင်း | `error.body["innererror"]["content_filter_result"]["jailbreak"]` ကို `error.body["content_filters"][0]["content_filter_results"]["jailbreak"]` သို့ ပြန်ရေးရန်။ `innererror` wrapper မရှိတော့ဘဲ content filter အချက်အလက်များသည် အပေါ်ဆုံး `content_filters` array ထဲရှိပြီး entry တစ်ခုစီတွင် `content_filter_results` (plural) ပါရှိသည်။ |
| Raw HTTP call `/openai/deployments/.../chat/completions` မှာ 404 ပြန်လာသည် | အဟောင်း Chat Completions REST endpoint ကို သုံးနေခြင်း | URL ကို `/openai/v1/responses` သို့ ပြောင်းပြီး request body တွင် `messages` → `input`၊ `max_output_tokens` + `store: false` ထည့်၊ `api-version` query parameter ကို ဖယ်ရှားပါ။ response parsing ကို `choices[0].message.content` → `output[0].content[0].text` (မှတ်ချက်: `output_text` သည် SDK အတွက် အဆင်ပြေစေရေး property ဖြစ်သည်၊ raw REST JSON တွင် မပါ။) ဖြစ်အောင် ပြောင်းပါ။ |

---

## ထိခိုက်နိုင်သော အချက်များ

1. ယခင်က Chat Completions ကို စကားပြောအခြေအနေများ အတွက် သုံးခဲ့ပါက Responses နှင့်အတူ သင်၏အခြေအနေကို ထိန်းချုပ်ပါ။
2. အဟောင်း `max_tokens` ထက် `max_output_tokens` ကို ဦးစားပေး သုံးပါ။
3. `gpt-5` သို့ ပြောင်းရွှေ့တိုင်း `temperature` ကို မထည့်ပါနှင့် သို့မဟုတ် `1` အဖြစ်သတ်မှတ်ထားပါ။
4. Chat ၏ `content[].type: "text"` ကို Responses ၏ `content[].type: "input_text"` သို့ ပြောင်းပါ (အသုံးပြုသူ/စနစ် input များအတွက်)။
5. `text.format` တွင် string မဟုတ်ဘဲ သင့်တော်သော dict ကို ပေးပါ (ဥပမာ `{"type": "json_schema", "name": "Output", "schema": ..., "strict": True}`)။
6. Responses တွင် `seed` parameter ကို မထောက်ပံ့ပါ၊ requests များမှ ဖယ်ရှားပါ။
7. **Reasoning**: မူလကုဒ်တွင် မှာရှိပြီး ပါကသာ `reasoning` ထည့်ပါ။ မဟုတ်ပါက API ခေါ်ဆိုမှုများတွင် မထည့်ရ။ မော်ဒယ်အများစု (ဥပမာ gpt-4o-mini) သည် parameter ကို မထောက်ပံ့ပါ။
8. **`max_output_tokens` မမာဖက်ခြင်း**: reasoning မော်ဒယ်များ (GPT-5-mini, GPT-5, o-series) အတွက် `max_output_tokens=4096` သို့ ဦးစားပေး သတ်မှတ်ပါ — ၅၀ – ၁၀၀၀ မဟုတ်ပါ။ မော်ဒယ်သည် reasoning tokens ကို အတွင်းပိုင်းအသုံးပြု၍ မြင်သာသော output ထုတ်ရန် မတိုင်ခင်ဖြစ်သည်။ အနိမ့်တန်ဖိုးများကြောင့် output မလုံလောက်ခြင်း သို့မဟုတ် စာမဲ့ output ဖြစ်ပေါ်နိုင်သည်။
9. **O-series `max_completion_tokens`**: မူလကုဒ်တွင် `max_completion_tokens` (o-series အတွက် Azure-အထူး) ကို သုံးနေပါက `max_output_tokens` ဖြင့် အစားထိုးပါ။ Responses API သည် `max_completion_tokens` ကို မလက်ခံပါ။
10. **O-series `reasoning_effort`**: မူလကုဒ်တွင် `reasoning_effort` (low/medium/high) ကို သုံးပါက Responses API ခေါ်ဆိုမှုတွင် `reasoning={"effort": "<value>"}` သို့ ပြောင်းပါ။
11. **O-series streaming ဆန့်ကျင်မှု**: O-series မော်ဒယ်သည် output ထုတ်မီ အတွင်းပိုင်း reasoning ပြုလုပ်သည့်အတွက် streaming တွင် ပထမ `response.output_text.delta` event မထွက်မီ အချိန်ရှည်ကြာနိုင်သည်။ ၎င်းသည် သာမန်ဖြစ်ပြီး မော်ဒယ်သည် reasoning ပြုလုပ်နေသည်၊ ပိတ်မထားပါ။
9. **`_azure_ad_token_provider` မရှိတော့ပါ**: `AsyncOpenAI` / `OpenAI` တွင် `_azure_ad_token_provider` attribute မပါတော့ပါ။ attribute ကို သုံးသော test များ သို့မဟုတ် code များသည် `AttributeError` ဖြစ်လိမ့်မည်။ token provider ကို `api_key` အဖြစ်ပေးပြီး client object တွင် ကြည့်ရှု၍ မရပါ။
10. **Snapshot / golden ဖိုင်များ**: Test suite တွင် snapshot testing သုံးပါက Chat Completions streaming shape များပါဝင်သော snapshot ဖိုင်များအားလုံးကို Responses shape အသစ်များ ဖြင့် အပ်ဒိတ်လုပ်ရမည်။ ၎င်းကို မမြင်မကွင်းလွှတ်မိခြင်းကြောင့် snapshot assertion မအောင်မြင်မှု ဖြစ်ပေါ်နိုင်သည်။
11. **Mock monkeypatch လမ်းကြောင်းပြောင်းခြင်း**: Monkeypatch target သည် `openai.resources.chat.AsyncCompletions.create` မှ `openai.resources.responses.AsyncResponses.create` (သို့မဟုတ် sync ကိစ္စတွင် `Responses.create`) သို့ ပြောင်းလဲသည်။ အဟောင်း လမ်းကြောင်းသည် မဟန့်တားနိုင်ပါ၊ test များသည် တကယ့် API သို့ ချိတ်ဆက်ခြင်း သို့မဟုတ် fail ဖြစ်စေပါသည်။
12. **`input` သုံးရန်၊ `messages` မဟုတ်ပါ**: Mock ပုံဖော် functions များသည် `kwargs.get("input")` ကိုဖတ်ရမည်၊ `kwargs.get("messages")` မဟုတ်လိုက်ပါ။ Responses API သည် စကားပြောသမိုင်းအတွက် `input` ကို သုံးသည်။
13. **Environment variable နာမည်ပြောင်းမှု**: Azure Identity SDK သည် `AZURE_CLIENT_ID` ကို (မဟုတ်သော `AZURE_OPENAI_CLIENT_ID`) `ManagedIdentityCredential(client_id=...)` အတွက် သုံးသည်။ Test များ၊ .env ဖိုင်များ၊ app settings နှင့် Bicep/infra တွင် အမည်ပြောင်းရန်လိုသည်။
14. **`max_output_tokens` ၏ အနည်းဆုံး တန်ဖိုးမှာ ၁၆ ဖြစ်သည်**: Azure OpenAI သည် ၁၆ အောက်တန်ဖိုးများကို `400 integer_below_min_value` ဖြင့် ငြင်းဆန်သည်။ Smoke tests အတွက် ၅၀၊ ထုတ်လုပ်မှုအတွက် ၁၀၀၀+ သုံးပါ။ မူရင်း `max_tokens` တွင် ဤအနည်းဆုံး မရှိပါ။
15. **`AzureDeveloperCliCredential` အတွက် `tenant_id` ပြသရန်**: Azure OpenAI resource သည် အခြား tenant တွင်ရှိလျှင် `tenant_id` ကို ပေးရန် တာဝန်ရှိသည် — `AzureDeveloperCliCredential(tenant_id=os.getenv("AZURE_TENANT_ID"))` ။ မပေးပါက credential သည် လျှို့ဝှက်စွတ်ကမ်း မှားသော tenant ကို သုံးသည်နှင့် `401` ပြန်လာသည်။
16. **Streaming တွင် rate limits များသည် ကွဲပြားစွာ လုပ်ဆောင်မှုရှိသည်**: Chat Completions တွင် 429 သည် streaming စတင်ခြင်းမဖြစ်စေရန်။ Responses API streaming တွင် 429 သည် streaming အတွင်းတစ်လျှောက် ဖြစ်နိုင်သည် — async iterator သည် exception ဖြုတ်ပေးမည်။ streaming loop ကို အမြဲ `try/except` ဖြင့် ဖုံးကွယ်ပြီး error JSON line ထုတ်ပေး၍ frontend အရမ်းအဆင်ပြေစေရန် ပြုလုပ်ပါ။ 

17. **ဝက်ဘ်အက်ပ်များအတွက် Streaming အမှားထိန်းချုပ်မှုသည် တရားဝင်ဖြစ်ရပါမည်** - ပုံစံ `try: async for event in await coroutine: ... except Exception as e: yield json.dumps({"error": str(e)})` သည် အရေးကြီးသည်။ ဤမရှိပါက SSE/JSONL စီးရီးသည် ဆာဗာဘက်အမှားတစ်ခုခုတွင်ထိုးထွင်းခြင်းမရှိဘဲ သေဆုံးပြီး ဖရန့်ဒ်အက်ပ်သည် တုန့်ပြန်မှု မရှိတော့ပါ။
18. **ကိရိယာသတ်မှတ်ချက်များသည် ပုံစံလေးချောင်းနည်းဖြင့်သာ အသုံးပြုရမည်** - Responses API သည် `{"type": "function", "name": ..., "parameters": ...}` ကိုမျှော်လင့်သည် - Chat Completions ၏ nested `{"type": "function", "function": {"name": ..., "parameters": ...}}` မဟုတ်ပါ။ ၎င်းသည် function-calling ကုဒ်အတွက် အများဆုံးဖြစ်ပေါ်သောအမှားဖြစ်သည်။
19. **`pydantic_function_tool()` သည် ညှို့ဆက်မရပါ** - `openai.pydantic_function_tool()` ကူညီရေးဆွဲမှုသည် ယခင် nested ပုံစံအသစ်ကို ဖန်တီးနေဆဲဖြစ်သည်။ `responses.create()` နှင့် အတူ မသုံးသင့်ပါ။ ကိရိယာ schema များကို လက်ဖြင့် သတ်မှတ်ပါ သို့မဟုတ် output ကို လေးချောင်းပြုပြင်ပါ။
20. **ကိရိယာရလဒ်များသည် `function_call_output` ကို အသုံးပြုပြီး `role: tool` မဟုတ်ရပါ** - ကိရိယာတစ်ခုကို ဆောင်ရွက်ပြီးနောက် `{"type": "function_call_output", "call_id": ..., "output": ...}` ကို ပေါင်းထည့်ပါ — `{"role": "tool", "tool_call_id": ..., "content": ...}` မဟုတ်ပါ။ အကူအညီပေးသူ၏ ကိရိယာတောင်းဆိုမှုအတွက် `messages.extend(response.output)` ကို သုံးရန်ရှိပြီး လက်ဖြင့် `{"role": "assistant", "tool_calls": [...]}` ဆိုသည့် dict မဟုတ်ပါ။
21. **`strict: true` သုံးသောအခါ `required` + `additionalProperties: false` လိုအပ်သည်** - ကိရိယာတစ်ခုတွင် `strict: true` သုံးစဉ်တွင် စုပေါင်း property များသည် `required` အဏ် array တွင် ပါရှိရမည်ဖြစ်ပြီး `additionalProperties` သည် `false` ဖြစ်ရမည်။ အချက်တစ်ခုခု လွတ်လပ်ပါက 400 အမှား ဖြစ်ပေါ်သည်။
22. **Function call ID များတွင် သတ်မှတ် prefix များ ရှိရမည်** - `input` တွင် few-shot `function_call` အပိုင်းများ ဆက်တိုက်ပေးသည့်အချိန် `id` ဂုဏ်သတ္တိသည် `fc_` ဖြင့် စတင်ရမည်။ `call_id` သည် `call_` ဖြင့် စတင်ရမည် (ဥပမာ `"id": "fc_example1", "call_id": "call_example1"` ဖြစ်သည်။) ယခင် Chat Completions ၏ `call_` prefix ကို `id` အတွက် သုံးမှုကို ဂရုမစိုက်ပြီး ခုခံသည်။
23. **GitHub မော်ဒယ်များသည် Responses API ကို မထောက်ပံ့ပါ** - အက်ပ်တွင် GitHub မော်ဒယ်ကုဒ်လမ်းကြောင်း (`base_url` သည် `models.github.ai` သို့မဟုတ် `models.inference.ai.azure.com` သို့ ဦးတည်ထားရှိပါက) များရှိပါက အပြည့်အစုံ ဖယ်ရှားရပါမည်။ ပြောင်းရွှေ့မည့်လမ်းကြောင်းမရှိပါ — Azure OpenAI၊ OpenAI သို့မဟုတ် သဟဇာတဒေသခံ endpoint သို့ သွားပါ။
24. **အကြောင်းအရာ စစ်ဆေးခြင်း အမှားပုံစံ ပွားပြောင်းသွားသည်** - Chat Completions အမှားများသည် `error.body["innererror"]["content_filter_result"]` (တစ်ခုတည်း) ကို အသုံးပြုပြီး Responses API အမှားများသည် `error.body["content_filters"][0]["content_filter_results"]` (တစ်ခုပေါင်းများစွာ၊ အတွင်း Array) ကို အသုံးပြုသည်။ `innererror` key သည်လည်းမရှိတော့ပါ။ မည်သည့်ကုဒ်တွင် `innererror` ကို တိုက်ရိုက်ဝင်ရောက်သုံးစွဲပါက runtime တွင် `KeyError` ဖြစ်စေနိုင်ပြီး၊ ပြောင်းရွှေ့ခြင်းအတွင်း အလွတ်မလွတ်လွတ်မခံယူနိုင်တော့ပါ။ ပြောင်းရွှေ့စဉ် အမြဲ `innererror` ကို ရှာဖွေပါ။
25. **Raw HTTP ခေါ်ဆိုမှုများတွင် URL နှင့် body ပြင်ဆင်ခြင်း လိုအပ်သည်** - Azure OpenAI REST ကို တိုက်ရိုက်ခေါ်ဆိုသည့် App များ (requests, httpx, aiohttp ဇာတိ) `/openai/deployments/{name}/chat/completions?api-version=...` သို့ လွှဲပြောင်းထားရမည်။ `/openai/v1/responses` ဖြစ်လာသည်။ မေးသည် body တွင် `messages` မဟုတ်ဘဲ `input` ကို အသုံးပြုထားပြီး `max_output_tokens` နှင့် `store` ပါဝင်ရမည်။ `api-version` query parameter ကို ဖယ်ရှားထားသည်။ ပြန်လာသော response body စာသားသည် `output[0].content[0].text` တွင်ရှိပြီး — SDK အဆင်ပြေမှု property ဖြစ်သော `output_text` မဟုတ်ပါ၊ သေရှင်းသော raw REST JSON တွင် မပါရှိပါ။

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ပြောကြားချက်**
ဤစာတမ်းကို AI ဘာသာပြန်ဝန်ဆောင်မှု [Co-op Translator](https://github.com/Azure/co-op-translator) အသုံးပြု၍ ဘာသာပြန်ထားပါသည်။ ကျွန်ုပ်တို့သည် တိကျမှန်ကန်မှုအတွက် ကြိုးပမ်းနေသော်လည်း၊ စက်ကိရိယာဘာသာပြန်ခြင်းများတွင် အမှားများ သို့မဟုတ် မှားယွင်းချက်များ ပါဝင်နိုင်ကြောင်း သတိပြုပါရန် လိုအပ်ပါသည်။ မူလစာတမ်းကို မူရင်းဘာသာဖြင့်သာ ယုံကြည်စိတ်ချရသော အချက်အလက်အဖြစ် သတ်မှတ်သင့်သည်။ အရေးကြီးသည့် သတင်းအချက်အလက်များအတွက် ပရော်ဖက်ရှင်နယ် လူသားဘာသာပြန်သူဝန်ဆောင်မှုကို အကြံပြုပါသည်။ ဤဘာသာပြန်ချက်ကို အသုံးပြုခြင်းမှ ဖြစ်ပေါ်လာသော နားလည်မှုကွာခြားမှုများ သို့မဟုတ် မမှန်ကန်သော အသုံးပြုမှုများအတွက် ကျွန်ုပ်တို့ တာဝန်မခံပါ။
<!-- CO-OP TRANSLATOR DISCLAIMER END -->