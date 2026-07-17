# பிழைதிருத்தல், அபாய அட்டவணை மற்றும் கவனிக்க வேண்டியவை

## 400 பிழைகளை திருத்துதல்

| பிழை | பராமரிப்பு |
|-------|-----|
| `missing_required_parameter: tools[0].name` | கருவி வரையறை பழைய Chat Completions கொண்டுள்ள வடிவமைப்பைப் பயன்படுத்துகிறது | `{"type": "function", "function": {"name": ...}}` இல் இருந்து `{"type": "function", "name": ..., "parameters": ...}` என இணைத்தல் — name, description, parameters மேல் நிலை பெற்றுக்கொள்ள வேண்டும் |
| `unknown_parameter: input[N].tool_calls` | பன்முறை முறை கருவி முடிவுகள் பழைய Chat Completions வடிவத்தைக் கொண்டுள்ளது | `{"role": "assistant", "tool_calls": [...]}` + `{"role": "tool", ...}` ஐ `response.output` பொருட்களை + `{"type": "function_call_output", "call_id": ..., "output": ...}` என்று மாற்றவும் |
| `invalid_function_parameters: 'required' is required` | `strict: true` கருவியில் `required` வரிசை இல்லை | `strict: true` என்பதின்போது எல்லா பண்புகளும் `required` இல் பட்டியலிடப்பட்டிருக்க வேண்டும் மற்றும் `additionalProperties: false` அமைக்கப்பட வேண்டும் |
| `invalid_function_parameters: 'additionalProperties' is required` | `strict: true` கருவியில் `additionalProperties: false` இல்லை | பண்புகளின் பொருளுக்கு `"additionalProperties": false` சேர்க்கவும் |
| `invalid input[N].id: Expected an ID that begins with 'fc'` | சிறிது தாக்கல் function_call ID தவறான முன்னுறுப்பைக் கொண்டுள்ளது | Function call IDs `fc_` (எ.கா., `fc_example1`) கொண்டதாக இருக்க வேண்டும், `call_` அல்ல |
| `missing_required_parameter: text.format.name` | வடிவ dict-க்கு `"name"` முக்கியத்தை சேர்க்கவும் (எ.கா., `"name": "Output"`) |
| `invalid_type: text.format` | `text.format` ஒரு dict ஆக இருக்க வேண்டும், `type`, `name`, `strict`, `schema` என்ற முக்கியங்களுடன் — சராம்சம் அல்ல |
| `invalid input content type` | Chat `text` மாற்றாக `input_text`/`output_text` உள்ளடக்க வகைகளைப் பயன்படுத்தவும் |
| `invalid input content type` (படம்) | பட உள்ளடக்கம் இன்னும் `"type": "image_url"` பயன்படுத்துகிறது | `"type": "input_image"` என்று மாற்றவும் |
| `Expected object, got string` on `image_url` | `image_url` இன்னும் `{"url": "..."}` போன்ற ஓர் கூடிய பொருளாக உள்ளது | சாதாரண குறியைப் போல மாற்றவும்: `"image_url": "https://..."` அல்லது `"image_url": "data:image/...;base64,..."` |
| `integer below minimum value` for `max_output_tokens` | Azure OpenAI இல் குறைந்தபட்சம் **16** ஆகும். சோதனைகளுக்குப் 50+ மற்றும் உற்பத்திக்கு 1000+ ஐ பயன்படுத்தவும். |
| `429 Too Many Requests` திணறலின் போது | விகிதமிடல் தடை பட்டது. ஸ்ட்ரீமிங்கை `try/except` இல் மூடி, பிழை JSON ஐ முன் முனையிற்கு வழங்கவும், மீண்டும் முயற்சிக்கவும். |
| `KeyError: 'innererror'` உள்ளடக்கு வடிகட்டியில் பிழை | பதில்கள் API இல் உள்ளடக்கு வடிகட்டல் பிழை உடலை மாற்றியுள்ளது | Chat Completions இல் `error.body["innererror"]["content_filter_result"]` பயன்படுத்தப்பட்டது; Responses API இல் `error.body["content_filters"][0]["content_filter_results"]` (பன்மை, வரிசையிலுள்ள) பயன்படுத்தப்படுகிறது. அனைத்து `innererror` அணுகல்களையும் மறுசரிபார்க்கவும். |

---

## இடம்பெயர்வு அபாய அட்டவணை

| அறிகுறி | சாத்தியமான பிழை | பராமரிப்பு |
|---------|---------------|-----|
| காலியான `output_text` / குறுக்கப்பட்ட பதில் | கருத்து விளக்க மாடல்களுக்கு `max_output_tokens` குறைவாக இருத்தல் | `max_output_tokens=1000` அல்லது அதற்கு மேல் அமைக்கவும் — கருத்துக் கணக்கீடு குறியீடுகள் கட்டுப்பாட்டுக்குள் சேர்க்கப்படுகின்றன |
| `400 invalid_type: text.format` | `text.format` dict க்கு பதிலாக `response_format` رشته வழங்கப்பட்டது | `text={"format": {"type": "json_schema", "name": "...", "strict": True, "schema": {...}}}` பயன்படுத்தவும் |
| `/openai/v1/responses` இல் `404 Not Found` | தவறான `base_url` — `/openai/v1/` இறுதியின்றி உள்ளது | `base_url=f"{endpoint}/openai/v1/"` (இறுதியில் ஸ்லாஷ் கொண்டதாக) உறுதிப் படுத்தவும் |
| `OpenAI()` க்கு மாற்றிய பின்னர் `401 Unauthorized` | `api_key` ஏற்கனவே அமைக்கப்படவில்லை அல்லது டோக்கன் வழங்குபவர் சரியாக வழங்கப்படவில்லை | EntraID க்காக: `api_key=token_provider` (கால் செய்யக்கூடியது). API விசைக்காக: `api_key=os.environ["AZURE_OPENAI_API_KEY"]` |
| மாடல் `deployment not found` என பதிலளிக்கிறது | `model` அளவுரு உங்கள் Azure பகிர்தல் பெயருடன் பொருந்தவில்லை | `model=os.environ["AZURE_OPENAI_DEPLOYMENT"]` பயன்படுத்தவும் — இது பகிர்தல் பெயர், மாடல் பெயர் அல்ல |
| `json.loads(resp.output_text)` `JSONDecodeError` எழுப்புகிறது | திட்டம் கடுமையாக JSON ஐ அமல்படுத்தவில்லை அல்லது மாடல் கட்டமைக்கப்பட்ட வெளியீட்டை ஆதரிக்கவில்லை | திட்டத்தில் `"strict": True` என உறுதிப்படுத்தவும் மற்றும் மாடல் கட்டமைப்பான வெளியீட்டை கையாள்கிறது என்பதை சரிபார்க்கவும் |
| ஸ்ட்ரீமிங் எந்த `delta` நிகழ்வுகளையும் வழங்கவில்லை | தவறான நிகழ்வு வகை பார்க்கப்படுகிறது | `event.type == "response.output_text.delta"` என்பதை வடிகட்டவும், Chat இன் `chat.completion.chunk` அல்ல |
| இடம்பெயர்க்கப்பட்ட பிறகு படம் உள்ளீட்டில் `400` பிழை | படம் உள்ளடக்கு வகை புதுப்பிக்கப்படவில்லை | `"type": "image_url"` → `"type": "input_image"` மாற்றவும் மற்றும் `"image_url": {"url": "..."}` → `"image_url": "..."` (சாதாரண குறி) ஆம் மாற்றவும் |
| கருவி அழைப்புக்கள் முடிவில்லாமல் சுற்றிவளைக்கிறது | தொடர்ந்து உள்ளீட்டில் கருவி முடிவுகள் இல்லாதது | ஒரு கருவி செயல்படுத்திய பின் அடுத்த கோரிக்கையில் `input`க்கு `{"type": "function_call_output", "call_id": ..., "output": ...}` உருப்படியை சேர்க்கவும் |
| GPT-5 அல்லது o-series உடன் `temperature` பிழை | 1 தவிர வேறொரு `temperature` மதிப்பு குறிப்பிட்டல் | GPT-5 மற்றும் o-series மாடல்களுக்கு `temperature` நீக்கவும் அல்லது 1 ஆக மாற்றவும் (o1, o3-mini, o3, o4-mini) |
| o-series உடன் `top_p` பிழை | `top_p` ஆதரிக்கப்படவில்லை | o-series மாடல்களை இலக்கு வைக்கும் போது `top_p` நீக்கவும் |
| `max_completion_tokens` பறைசெய்யப்படவில்லை | Azure-நிர்வஹிக்கப்பட்ட அளவுருவை பயன்படுத்துதல் | `max_completion_tokens` இனை `max_output_tokens` என மாற்றவும். o-series க்கு 4096+ அமைக்கவும் (கருத்துக் குறியீடுகள் கட்டுப்பாட்டின்கீழ்). |
| o-series இருந்து காலியான / குறுக்கப்பட்ட வெளியீடு | `max_output_tokens` மிகவும் குறைவு | O-series உள்ளகமாக கருத்துக் குறியீடுகளை பயன்படுத்துகிறது. `max_output_tokens=4096` அல்லது அதற்கு மேல் அமைக்கவும் — 500–1000 அல்ல. |
| `400 integer_below_min_value` `max_output_tokens`க்கு | மதிப்பு 16க்குக் குறைவாக உள்ளது | Azure OpenAI `max_output_tokens >= 16` என்பதை கட்டாயப்படுத்துகிறது. புகை சோதனைகளுக்கு 50+ மற்றும் உற்பத்திக்கு 1000+ பயன்படுத்தவும். |
| ஸ்ட்ரீமிங் நடுவே `429 Too Many Requests` | Azure OpenAI மூலம் விகிதமிடல் தடைபட்டது | ஸ்ட்ரீம் பிழை கையாளுதல் இல்லாமல் அமைதி உடைத்து விடுகிறது. எப்போதும் `async for event in await coroutine:` ஐ `try/except` இல் மூடி `{ "error": str(e) }` ஐ முன் முனையிற்கு வழங்கவும். |
| `AzureDeveloperCliCredential` → `CredentialUnavailableError` | தவறான வாடகையாளர் அல்லது உள்நுழையவில்லை | `tenant_id=os.getenv("AZURE_TENANT_ID")` ஐ தெளிவாக வழங்கவும். உள்ளூர் `azd auth login --tenant <tenant-id>` ஓட்டவும். |
| GitHub மாடல்கள் (`models.github.ai`) பயன்படுத்திய போது `404 Not Found` | GitHub மாடல்கள் Responses API ஐ ஆதரிக்காது | GitHub மாடல்கள் கோடை பாதையை முழுமையாக அகற்றவும். Azure OpenAI, OpenAI அல்லது ஒத்துசேர்க்கக்கூடிய உள்ளூர் இடைமுகம் (எ.கா., Ollama Responses ஆதரவு) பயன்படுத்தவும். |
| MAF `OpenAIChatCompletionClient` இன்னும் Chat Completions பயன்படுகிறது | 1.0.0+ பதிப்பில் பழைய MAF கிளையண்ட் பயன்படுத்தப்பட்டுள்ளது | MAF 1.0.0+ இல், `OpenAIChatClient` இயல்பாக Responses API ஐ பயன்படுத்துகிறது. `OpenAIChatCompletionClient` ஐ `OpenAIChatClient` க்கு மாற்றவும். 1.0.0 க்கும் முன் பதிப்புகளுக்கு `agent-framework-openai>=1.0.0` என மேம்படுத்தவும். |
| LangChain முகவர் கால்களைக் கொண்டு கால்கள் காலியாக அல்லது தோல்வி அடைகிறது | `ChatOpenAI` Responses API ஐ பயன்படுத்தவில்லை | `ChatOpenAI(...)` இல் `use_responses_api=True` சேர்க்கவும். نیز பதில் செய்திகள் `.content` → `.text` ஆக மாற்றவும். |
| உள்ளடக்கு வடிகட்டல் பிழை ஹேண்டலரில் `KeyError: 'innererror'` | Responses API இல் பிழை உடல் அமைப்பு மாற்றப்பட்டது | `error.body["innererror"]["content_filter_result"]["jailbreak"]` → `error.body["content_filters"][0]["content_filter_results"]["jailbreak"]` என மறுசரிபார்க்கவும். `innererror` பொதி இல்லாமல் போயுள்ளது; உள்ளடக்கு வடிகட்டல் விவரங்கள் இப்போது மேல் நிலை `content_filters` வரிசையில் மற்றும் ஒவ்வொரு உள்ளீட்டிலும் `content_filter_results` (பன்மை) உள்ளது. |
| `/openai/deployments/.../chat/completions` க்கு நேரடி HTTP அழைப்பு 404 ஐ வழங்குகிறது | பழைய Chat Completions REST இடைமுகம் | URL ஐ `/openai/v1/responses` என மாற்றவும். கோரிக்கை உடலை மாற்றவும்: `messages` → `input`, `max_output_tokens` + `store: false` சேர்க்கவும், `api-version` கேள்வி அர் நீக்கவும். பதில் பாகுபாடு: `choices[0].message.content` → `output[0].content[0].text` (குறிப்பு: `output_text` என்பது SDK வசதி சொத்து, மூல REST JSON இல் இல்லை). |

---

## கவனிக்க வேண்டியவை

1. நீங்கள் முன்பு உரையாடல் நிலைக்கு Chat Completions பயன்படுத்தி இருந்தால், Responses உடன் உங்கள் நிலையை தெளிவாக நிர்வகிக்கவும்.
2. பழைய `max_tokens` இடம்கொண்ட `max_output_tokens` ஐ முன்னுரிமை கொடுங்கள்.
3. `gpt-5` க்கு இடம்பெயரும்போது, `temperature` குறிப்பிடப்படாமல் இருத்தல் அல்லது `1` ஆக அமைக்கப்பட வேண்டும்.
4. Chat `content[].type: "text"` ஐ Responses இல் `content[].type: "input_text"` ஆக மாற்றவும் பயனர்/சிஸ்டம் உள்ளீடுகளுக்கு.
5. `text.format` க்கு சரியான dict (எ.கா., `{"type": "json_schema", "name": "Output", "schema": ..., "strict": True}`) கொடுக்கவும், சாதாரண சரம் அல்ல.
6. Responses இல் `seed` அளவுரு ஆதரிக்கப்படவில்லை; கோரிக்கைகளில் இருந்து அகற்றவும்.
7. **கருத்து விளக்கல்**: அசல் குறியீடு இதைப் பயன்படுத்தியிருந்தால் மட்டுமே `reasoning` உள்ளிடவும். இதை இல்லை என்ற API அழைப்புகளில் சேர்க்க வேண்டாம் — பல மாடல்கள் இதை ஆதரிக்காது.
8. **`max_output_tokens` அளவீடு**: கருத்து விளக்க மாடல்களுக்கு (GPT-5-mini, GPT-5, o-series), `max_output_tokens=4096` அல்லது அதற்கு மேல் பயன்படுத்தவும் — 50–1000 அல்ல. மாடல் வெளிப்படையாக உரையை உருவாக்குவதற்கு முன்னர் கருத்துக் குறியீடுகளை உள் பாகமாக பயன்படுத்துகிறது; குறைவான வரம்புகள் குறுக்கப்பட்ட அல்லது காலியான பதில்களை உண்டாக்கும்.
9. **O-series `max_completion_tokens`**: அசல் குறியீடு `max_completion_tokens` (o-series க்கான Azure-விசேடம்) பயன்படுத்தினால், அதை `max_output_tokens` ஆக மாற்றவும். Responses API `max_completion_tokens` ஏற்காது.
10. **O-series `reasoning_effort`**: அசல் குறியீடு `reasoning_effort` (குறைவான/மத்திய/உயர்) பயன்படுத்தினால், Responses API அழைப்பில் அதை `reasoning={"effort": "<value>"}` ஆக மாற்றவும்.
11. **O-series ஸ்ட்ரீமிங் தாமதம்**: O-series மாடல்கள் வெளியீட்டை உருவாக்குவதற்கு முன் உள்ளக கருத்து விளக்கத்தை செய்கின்றன. ஸ்ட்ரீமிங் போது முதல் `response.output_text.delta` நிகழ்வு வருவதற்கு நீண்ட தாமதம் ஏற்படலாம். இது சாதாரணம் — மாடல் கருத்து விளக்கத்தில் உள்ளது, அவilan இல்லை.
9. **`_azure_ad_token_provider` இல்லை**: `AsyncOpenAI` / `OpenAI` இல் `_azure_ad_token_provider` பண்பு இல்லை. அதன்மீது அணுகும் சோதனைகள் அல்லது குறியீடுகள் `AttributeError` ஏற்படுத்தும். டோக்கன் வழங்குபவர் `api_key` என வழங்கப்படுகிறது மற்றும் கிளையண்ட் பொருளில் பரிசோதிக்க முடியாது.
10. **ஸ்நாப்ஷாட் / பொற்கோப்புகள்**: சோதனை தொகுப்பு ஸ்நாப்ஷாட் சோதனை பயன்படுத்தினால், Chat Completions ஸ்ட்ரீமிங் வடிவங்களைக் கொண்ட அனைத்து ஸ்நாப்ஷாட் கோப்புகளும் Responses புதிய வடிவத்தில் மேம்படுத்தப்பட வேண்டும். இது தவறவிட எளிது மற்றும் ஸ்நாப்ஷாட் உறுதிப்படுத்தல் தோல்விகளை உண்டாக்கும்.
11. **மோக் மங்கிப்பாட்ச் பாதை**: மங்கிப்பாட்ச் இலக்கு `openai.resources.chat.AsyncCompletions.create` → `openai.resources.responses.AsyncResponses.create` (அல்லது ஒத்திருக்கையில் `Responses.create`) ஆக மாறியுள்ளது. பழைய பாதை அமைதியாகச் செயல்படாது — மங் கை இடையிலான இடைமுகத்தைத் தடுத்து நிறுத்தாது மற்றும் சோதனைகள் உண்மையான API ஐச் சந்திக்கும் அல்லது தோல்வி அடையும்.
12. **`input`, `messages` அல்ல**: மோக் செயலிகள் `kwargs.get("input")` ஐப் படிக்க வேண்டும், `kwargs.get("messages")` அல்ல. Responses API உரையாடல் வரலாற்றுக்கு `input`-ஐப் பயன்படுத்துகிறது.
13. **சூழல் மாறி பெயரிடல்**: Azure Identity SDK `ManagedIdentityCredential(client_id=...)` க்காக `AZURE_CLIENT_ID` (ஏனெனில் `AZURE_OPENAI_CLIENT_ID` அல்ல) பயன்படுத்துகிறது. சோதனைகள், `.env` கோப்புகள், பயன்பாட்டு அமைப்புகள் மற்றும் Bicep/ஈஸ்வரின் பெயர் மாற்றவும்.
14. **`max_output_tokens` குறைந்தபட்சம் 16 ஆகும்**: Azure OpenAI 16 க்கும் கீழான மதிப்புகளை `400 integer_below_min_value` உடன் நிராகரிக்கிறது. புகை சோதனைகளுக்கு 50 மற்றும் உற்பத்திக்கு 1000+ பயன்படுத்தவும். பழைய `max_tokens` க்கு இது குறைந்தபட்சம் இல்லை.
15. **`AzureDeveloperCliCredential` க்கு `tenant_id`**: Azure OpenAI வளம் வேறு வாடகையாளரிலுள்ளது என்றால், நீங்கள் **தெளிவாக** `tenant_id` ஐ வழங்க வேண்டும் — `AzureDeveloperCliCredential(tenant_id=os.getenv("AZURE_TENANT_ID"))`. இல்லையெனில், உரிமம் அமைதி கணினி தவறான வாடகையாளரைப் பயன்படுத்தி `401` திருப்பும்.
16. **ஸ்ட்ரீமிங்கில் விகிதமிடல் தடைகள் வேறுபடும்**: Chat Completions உடன், 429 பொதுவாக ஸ்ட்ரீம் துவங்குவதைத் தடுக்கிறது. Responses API ஸ்ட்ரீமிங்குடன், 429 ஸ்ட்ரீமின் நடுவே நிகழலாம் — அசிங்க் இடைமுகம் தவறை எழுப்பும். ஸ்ட்ரீமிங் லூப்பை எப்போதும் `try/except` இல் மூடி பிழை JSON வரியை முன் முனையிற்கு வழங்கி, மென்மையாக கையாளத்தக்கவாறு செய்க.

17. **வெப் செயலிகளுக்கு ஸ்ட்ரீமிங் பிழை கையாளல் கட்டாயமாகும்**: `try: async for event in await coroutine: ... except Exception as e: yield json.dumps({"error": str(e)})` என்ற மாதிரி அவசியமானது. இதில்லாமல், SSE/JSONL ஸ்ட்ரீம் எந்தவொரு சர்வர் பக்கம் பிழையிலும் மௌனமாக முடிவடையும் மற்றும் முன்னணி பொருத்தி தொங்கும்.
18. **கருவி வரையறைகள் ஒரு ரேகை வடிவத்தை பயன்படுத்த வேண்டும்**: Responses API `{"type": "function", "name": ..., "parameters": ...}` என்று எதிர்பார்கிறது — Chat Completions இன் நெஸ்டட் `{"type": "function", "function": {"name": ..., "parameters": ...}}` அல்ல. இது செயல்பாட்டு அழைப்புக் குறியீட்டில் பொதுவான இடம்பெயர்வு பிழை ஆகும்.
19. **`pydantic_function_tool()` பொருந்தாது**: `openai.pydantic_function_tool()` உதவியாளர் இன்னும் பழைய நெஸ்டட் வடிவத்தை உருவாக்குகிறது. இதை `responses.create()` உடன் பயன்படுத்தவேண்டாம். கருவி திட்டங்களை கைமுறை வகைப்படுத்தவும் அல்லது வெளியீட்டை ஒரு ரேகையாக மாற்றவும்.
20. **கருவி முடிவுகள் `function_call_output` ஐ பயன்படுத்த வேண்டும், `role: tool` இல்லை**: ஒரு கருவி இயக்கப்பட்ட பிறகு, `{"type": "function_call_output", "call_id": ..., "output": ...}` சேர்க்கவும் — `{"role": "tool", "tool_call_id": ..., "content": ...}` அல்ல. உதவியாளரின் கருவி கோரிக்கைக்காக, `messages.extend(response.output)` பயன்படுத்தவும் — கைமுறையாக `{"role": "assistant", "tool_calls": [...]}` அகராதி அல்ல.
21. **`strict: true` என்றால் `required` + `additionalProperties: false` அவசியம்**: கருவியில் `strict: true` பயன்படுத்தும்போது, எல்லா பண்புகளுமே `required` வரிசையில் பட்டியலிடப்பட வேண்டும் மற்றும் `additionalProperties` `false` ஆக இருக்க வேண்டும். இது இரண்டையும் தவறவிட்டால் 400 பிழை ஏற்படும்.
22. **செயல்பாட்டு அழைப்பு அடையாளங்கள் குறிப்பிட்ட முன் அடையாளங்கள் உடையவை**: குறைந்த-முயற்சி `function_call` உருப்படிகளை `input` பயன்படுத்தும்போது, `id` புலம் `fc_` கொண்டு தொடங்க வேண்டும் மற்றும் `call_id` புலம் `call_` கொண்டு தொடங்க வேண்டும் (எ.கா., `"id": "fc_example1", "call_id": "call_example1"`). பழைய Chat Completions இன் `call_` முன்அடையாளம் `id` க்கு பயன்படுத்துவது மறுக்கப்படுகிறது.
23. **GitHub மாடல்கள் Responses API ஐ ஆதரிக்காது**: செயலியில் GitHub Models குறியீடு பாதை (`base_url` `models.github.ai` அல்லது `models.inference.ai.azure.com` க்கு உண்பதாக) இருந்தால் அது முழுமையாக அகற்ற வேண்டும். இடம்பெயர்வு பாதை இல்லை — Azure OpenAI, OpenAI அல்லது பொருந்தக்கூடிய உள்ளூர் முடிவிற்கு மாறவும்.
24. **உள்ளடக்க வடிகட்டி பிழை உடலை அமைப்பு மாறியுள்ளது**: Chat Completions பிழைகள் `error.body["innererror"]["content_filter_result"]` (ஒற்றை) பயன்படுத்தியது. Responses API பிழைகள் `error.body["content_filters"][0]["content_filter_results"]` (பலமடங்கு, ஒரு வரிசையில்) பயன்படுத்துகின்றன. `innererror` விசை இப்போது இல்லை. நேரடியாக `innererror` அணுகும் குறியீடு இயக்க நேரத்தில் `KeyError` எழுப்பும் — இது இடம்பெயர்வில் தவறவிட எளியது ஏனெனில் அது மட்டுமே உள்ளடக்க வடிகட்டி உண்மையில் செயல்பட்டு போது வெளிப்படும். இடம்பெயர்வில் எப்போதும் `innererror` க்காக தேடவும்.
25. **நேரடி HTTP அழைப்புகள் URL + உடல் மறுசீரமைப்பை தேவைப்படும்**: Azure OpenAI REST ஐ நேரடியாக அழைக்கும் செயலிகள் (/openai/deployments/{name}/chat/completions?api-version=...) பயன்படுத்தும் போது அது /openai/v1/responses என மாற்றப்பட வேண்டும். கோரிக்கை உடல் `messages` பதிலாக `input` பயன்படுத்தும், `max_output_tokens` மற்றும் `store` தேவைப்படும், மற்றும் `api-version` தனக்கே உரிய கேள்வி அளவுரு நீக்கப்படுகிறது. பதில் உடல் உரை `output[0].content[0].text` இல் இருக்கும் — **`output_text` அல்ல**, இது SDK வசதிக்காக உள்ள சொத்து மற்றும் வெற்றிடம் REST JSON இல் இல்லை.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**மறுப்பு**:
இந்த ஆவணம் AI மொழிபெயர்ப்பு சேவை [Co-op Translator](https://github.com/Azure/co-op-translator) பயன்படுத்தி மொழிபெயர்க்கப்பட்டுள்ளது. நாங்கள் துல்லியத்திற்காக முயற்சி செய்துள்ளோம், ஆனால் தானாக செய்யப்படும் மொழிபெயர்ப்புகளில் பிழைகள் அல்லது தவறுகள் இருக்கலாம் என்பதை கவனத்தில் கொள்ளவும். அசல் ஆவணம் அதன் தாய்மொழியில் அதிகாரப்பூர்வ ஆதாரமாக கருதப்பட வேண்டும். முக்கியமான தகவல்களுக்கு, தொழில்நுட்பமான மனித மொழிபெயர்ப்பு பரிந்துரைக்கப்படுகிறது. இந்த மொழிபெயர்ப்பைப் பயன்படுத்துவதால் ஏற்படும் எந்த தவறான புரிதல்கள் அல்லது தவறான விளக்கத்திற்கும் நாங்கள் பொறுப்பில்வில்லை.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->