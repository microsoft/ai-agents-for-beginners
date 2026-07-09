# பிழைதிருத்தல், அபாய அட்டவணை மற்றும் கவனிக்கக் கூடியவை

## 400 வழுவுகள் பிழைதிருத்தல்

| பிழை | சரிபார் |
|-------|-----|
| `missing_required_parameter: tools[0].name` | கருவி வரைவில் பழைய Chat Completions உட்பட வடிவமைப்பு பயன்படுத்தப்படுகிறது |  `{"type": "function", "function": {"name": ...}}` இருந்து `{"type": "function", "name": ..., "parameters": ...}` என்ற நிலைமையில் செல்லவும் — name, description, parameters மேல் நிலைமையில் செல்ல வேண்டும் |
| `unknown_parameter: input[N].tool_calls` | பன்முறை கருவி முடிவுகள் பழைய Chat Completions வடிவமைப்பு பயன்படுத்துகிறது | `{"role": "assistant", "tool_calls": [...]}` + `{"role": "tool", ...}` ஐ `response.output` உருப்படிகளுடன் + `{"type": "function_call_output", "call_id": ..., "output": ...}` என்று மாற்றவும் |
| `invalid_function_parameters: 'required' is required` | `strict: true` கருவி `required` வரிசை இன்றி உள்ளது | `strict: true` ஆக இருந்தால், எல்லா பண்புகளும் `required` இல் பட்டியலிடப்பட வேண்டும் மற்றும் `additionalProperties: false` அமைக்கப்பட வேண்டும் |
| `invalid_function_parameters: 'additionalProperties' is required` | `strict: true` கருவி `additionalProperties: false` இல்லாமல் உள்ளது | இடைமுக உட்பொருள் `parameters` மீது `"additionalProperties": false` சேர்க்கவும் |
| `invalid input[N].id: Expected an ID that begins with 'fc'` | Few-shot function_call ID தவறான முன்னொட்டு | Function call IDs `fc_` (எ.கா., `fc_example1`) என்று துவங்க வேண்டும், `call_` அல்ல |
| `missing_required_parameter: text.format.name` | வடிவமைப்பு அகராதிக்கு `"name"` விசை சேர்க்கவும் (எ.கா., `"name": "Output"`) |
| `invalid_type: text.format` | `text.format` என்பது குறியீடு அல்ல, ஒரு அகராதி ஆக மாற வேண்டும் (type, name, strict, schema விசைகள் கொண்டது) |
| `invalid input content type` | Chat `text` பதிலாக `input_text`/`output_text` உள்ளடக்க வகைகளை பயன்படுத்து |
| `invalid input content type` (படம்) | படம் உள்ளடக்கம் இன்னும் `"type": "image_url"` ஆக உள்ளது | `"type": "input_image"` ஆக மாற்றவும் |
| `Expected object, got string` on `image_url` | `image_url` இன்னும் `{"url": "..."}` என்ற உட்பட வடிவில் உள்ளது | ஒரு எளிய சரத்தைப் போல Flatten செய்யவும்: `"image_url": "https://..."` அல்லது `"image_url": "data:image/...;base64,..."` |
| `integer below minimum value` for `max_output_tokens` | Azure OpenAI இல் குறைந்தபட்சம் **16** ஆக இருக்க வேண்டும். சோதனைகளுக்கு 50+ மற்றும் நிர்வாகத்திற்கு 1000+ பயன்படுத்து |
| `429 Too Many Requests` streaming போது | விகித வரம்பளிக்கப்பட்டது. streaming ஐ `try/except` உள்ளே மூடு, பிழை JSON ஐ முன் முனையில் அனுப்பு, பின் முயற்சி/மீண்டும் முயற்சி செய் |
| `KeyError: 'innererror'` உள்ளடக்க வடிகட்டிப் பிழையில் | Responses API இல் உள்ளடக்க வடிகட்டு பிழை உடல் அமைப்பு மாற்றம் | Chat Completions இல் `error.body["innererror"]["content_filter_result"]` பயன்படுத்தப்பட்டது; Responses API இல் `error.body["content_filters"][0]["content_filter_results"]` (பன்மை, வரிசையின் உள்ளே) பயன்படுத்துகிறது. அனைத்து `innererror` அணுகலை மறுசரி செய். |

---

## இட плавtn இட Aயா அட்டவணை

| அறிகுறி | அந்தரங்க தவறு | சரிபார் |
|---------|---------------|-----|
| காலியான `output_text` / குறுக்கப்பட்ட பதில் | விவாத மாதிரிகளுக்கு `max_output_tokens` குறைவாக உள்ளது | `max_output_tokens=1000` அல்லது அதிகம் அமைக்கவும் — விவாத குறியீடுகள் வரம்புக்கு எதிரானவை |
| `400 invalid_type: text.format` | `text.format` அகராதி பதிலாக `response_format` ஸ்ட்ரிங் கடத்தப்பட்டது | `text={"format": {"type": "json_schema", "name": "...", "strict": True, "schema": {...}}}` பயன்படு |
| `/openai/v1/responses` மீது `404 Not Found` | தவறான `base_url` — `/openai/v1/` suffix இல்லாமல் உள்ளது | `base_url=f"{endpoint}/openai/v1/"` ( trailing slash உடன்) நிச்சயி |
| `401 Unauthorized`  `OpenAI()` மாற்றம் பிறகு | `api_key` அமைக்கப்படவில்லை அல்லது token வழங்குநர் சரியாக இல்லை | EntraID க்கு: `api_key=token_provider` (callable). API key க்குஇ: `api_key=os.environ["AZURE_OPENAI_API_KEY"]` |
| மாதிரி `deployment not found` திரும்புகிறது | `model` பரிமாணம் Azure அமைப்பு பெயருடன் பொருந்தவில்லை |  `model=os.environ["AZURE_OPENAI_DEPLOYMENT"]` பயன்படுத்தவும் — இது deployment பெயர், மாதிரி பெயர் அல்ல |
| `json.loads(resp.output_text)` `JSONDecodeError` எழுப்புகிறது | கட்டமைப்பு அமல் செய்யப்படவில்லை அல்லது மாதிரி கடுமையான JSON ஐ ஆதரிக்கவில்லை | கட்டமைப்பில் `"strict": True` இருக்கவும், கட்டமைக்கப்பட்ட வெளியீட்டினை ஆதரிக்க மாதிரியை சரிபார் |
| Streaming இல் எந்த `delta` நிகழ்வும் இல்லை | தவறான event வகையை சரிபார்க்கிறது | `event.type == "response.output_text.delta"` இல் வடிகட்டி, Chat இன் `chat.completion.chunk` அல்ல |
| மாற்றத்திற்குப் பிறகு படம் உள்ளீட்டில் `400` பிழை | படம் உள்ளடக்க வகை மாற்றப்படவில்லை | `"type": "image_url"` → `"type": "input_image"` மற்றும் `"image_url": {"url": "..."}` → `"image_url": "..."` (எளிய ஸ்ட்ரிங்) ஆக மாற்று |
| கருவி அழைப்புகள் முடிவற்றதாக loop செய்கின்றன | பிறகு வரும் `input` இல் கருவி முடிவு இல்லை | கருவி செயல்படுத்திய பிறகு, அடுத்த கோரிக்கையில் `input` க்கு `{"type": "function_call_output", "call_id": ..., "output": ...}` உருப்படியை சேர்க்கவும் |
| GPT-5 அல்லது o-series உடன் `temperature` பிழை | 1 தவிர்த்து வேறு `temperature` மதிப்பு | GPT-5 மற்றும் o-series மாதிரிகள் (o1, o3-mini, o3, o4-mini) க்கான `temperature` நீக்கவும் அல்லது 1 ஆக அமைக்கவும் |
| o-series உடன் `top_p` பிழை | `top_p` ஆதரிக்கப்படவில்லை | o-series மாதிரிகள் நோக்கி `top_p` ஐ நீக்கவும் |
| `max_completion_tokens` அங்கீகாரம் கிடைக்கவில்லை | Azure தனிப்பட்ட அளவுரு பயன்படுத்தப்படுகிறது | `max_completion_tokens` ஐ `max_output_tokens` ஆக மாற்றவும். o-series க்கான 4096+ ஆக அமைக்கவும் (விவாத குறியீடுகள் வரம்பில் கணக்கிடப்படும்). |
| o-series இருந்து காலியான/குறுக்கப்பட்ட output | `max_output_tokens` குறைவாக உள்ளது | o-series உள் இரயினிங் குறியீடுகளைப் பயன்படுத்துகிறது. `max_output_tokens=4096` அல்லது அதற்கு மேல் அமைக்கவும் — 500–1000 அல்ல. |
| `400 integer_below_min_value` `max_output_tokens` க்கான | மதிப்பு 16 க்குக் கீழ் உள்ளது | Azure OpenAI `max_output_tokens >= 16` கட்டாயம் உள்ளது. சோதனைகளுக்கு 50+ மற்றும் நிர்வாகத்திற்கு 1000+ பயன்படுத்தவும். |
| `429 Too Many Requests` மத்திய-ஸ்ட்ரீம் | Azure OpenAI மூலம் விகித வரம்பு | ஸ்ட்ரீம் எதையும் காணாமல் முறிவு ஆகும்போது பிழை கையாளல் இல்லை. எப்போதும் `async for event in await coroutine:` உடன் `try/except` மூடி, முன்னணி பகுதியுக்கு `{"error": str(e)}` அனுப்பவும். |
| `AzureDeveloperCliCredential` → `CredentialUnavailableError` | தவறான வாடிகையாளர் அல்லது உள்நுழையவில்லை | `tenant_id=os.getenv("AZURE_TENANT_ID")` துல்லியமாக கொடு. உள்ளூர் `azd auth login --tenant <tenant-id>` இயக்கவும். |
| GitHub Models (`models.github.ai`) பயன்படுத்தும்போது `404 Not Found` | GitHub Models Responses API ஐ ஆதரிக்காது | GitHub Models கோடு பாதையை முழுமையாக நீக்கு. Azure OpenAI, OpenAI அல்லது Responses ஆதரிக்கும் உள்ளூர் இடைமுகம் (எ.கா., Ollama) பயன்படுத்தவும். |
| MAF `OpenAIChatCompletionClient` இன்னும் Chat Completions பயன்படுத்துகிறது | 1.0.0+ இல் பழைய MAF கிளையண்ட் பயன்படுத்தப்படுகிறது | MAF 1.0.0+ இல் `OpenAIChatClient` இயல்பாக Responses API ஐ பயன்படுத்துகிறது. `OpenAIChatCompletionClient` ஐ `OpenAIChatClient` ஆக மாற்றவும். 1.0.0 முன் பதிப்புக்கு `agent-framework-openai>=1.0.0` க்கு மேம்படுத்தவும். |
| LangChain ஏஜென்ட் கருவி அழைப்புகளுடன் காலியான அல்லது தோல்வி | `ChatOpenAI` Responses API ஐப் பயன்படுத்தவில்லை | `ChatOpenAI(...)` இல் `use_responses_api=True` சேர்க்கவும். பதிலை `.content` இருந்து `.text` ஆக மாற்றவும். |
| Content filter பிழை காரியஸ்தியில் `KeyError: 'innererror'` | Responses API இல் பிழை உடல் அமைப்பு மாற்றம் | `error.body["innererror"]["content_filter_result"]["jailbreak"]` → `error.body["content_filters"][0]["content_filter_results"]["jailbreak"]` மாற்றவும். `innererror` wrapper இனி இல்லை; content filter விவரங்கள் முக்கிய `content_filters` வரிசையில் மற்றும் பன்மை `content_filter_results` உள்ளே இருக்கின்றன. |
| `/openai/deployments/.../chat/completions` க்கு நேரடி HTTP அழைப்பு 404 ஆகும் | பழைய Chat Completions REST Endpoint | URL ஐ `/openai/v1/responses` ஆக மாற்றவும். கோரிக்கை உடலை மாற்றவும்: `messages` → `input`, `max_output_tokens` + `store: false` சேர்க்கவும், `api-version` கேள்விப்பாராமை அகற்று. பதிலை மாற்றவும்: `choices[0].message.content` → `output[0].content[0].text` (குறிப்பு: `output_text` என்பது SDK வசதி, வடிவ REST JSON இல் இல்லை). |

---

## கவனிக்க வேண்டியவை

1. முன்பு Chat Completions உரையாடல் நிலை பயன்பட்டிருந்தால், Responses உடன் தனிப்பட்ட நிலையை தெளிவாக பராமரி.
2. பழைய `max_tokens` இடம் `max_output_tokens` ஐ அதிக மதிப்பீடு செய்.
3. `gpt-5` க்கு மாற்றும்போது, `temperature` குறிப்பிடப்படாதிருக்க அல்லது `1` ஆக அமைக்கப்பட்டிருப்பதை உறுதி செய்.
4. Chat இன் `content[].type: "text"` ஐ Responses இல் `content[].type: "input_text"` ஆக மாற்று — பயனர்/கணினி உள்ளீடுகளுக்கு.
5. `text.format` க்கு உரிய அகராதி கொடு (எ.கா., `{"type": "json_schema", "name": "Output", "schema": ..., "strict": True}`), ஒரு சாதாரண ஸ்ட்ரிங் அல்ல.
6. Responses இல் `seed` பரிமாணம் ஆதரிக்கப்படவில்லை; கோரிக்கைகளில் இருந்து நீக்கு.
7. **விவாதம்**: அசல் குறியீடு ஏற்கனவே பயன்படுத்தியிருந்தால் மட்டுமே `reasoning` சேர்க்கவும். இல்லாவிட்டால் API அழைப்புகளில் `reasoning` சேர்க்காதீர்கள் — பல மாதிரிகள் (எ.கா., gpt-4o-mini) இந்த பரிமாணத்தை ஆதரிக்காது.
8. **`max_output_tokens` பருமன்**: விவாத மாதிரிகளுக்கு (GPT-5-mini, GPT-5, o-series), `max_output_tokens=4096` அல்லது அதிகமாகவும் — 50-1000 அல்ல. மாதிரி வெளிப்படையான வெளியீட்டுக்கு முன்பு உள் விவாத குறியீடுகளை பயன்படுத்துகிறது; குறைந்த வரம்புகள் குறுக்கப்பட்ட அல்லது காலியான பதில்களை உண்டாக்கும்.
9. **O-series `max_completion_tokens`**: அசல் குறியீடு `max_completion_tokens` (o-series க்கு Azure சிறப்பானது) பயன்படுத்தியிருந்தால், அதை `max_output_tokens` ஆக மாற்றவும். Responses API `max_completion_tokens` ஐப்பற்றாவதும்.
10. **O-series `reasoning_effort`**: அசல் குறியீடு `reasoning_effort` (குறைவான/நடுத்தர/உயர்) பயன்படுத்தியிருந்தால், Responses API அழைப்பில் `reasoning={"effort": "<value>"}` ஆக மாற்றுக.
11. **O-series streaming தாமதம்**: O-series மாதிரிகள் வெளியீடு முன்னர் உள்ளக விவாதம் செய்கின்றன. Streaming போது முதல் `response.output_text.delta` நிகழ்வுக்கு நீண்ட தாமதம் இருக்கும். இது சாதாரணம் — மாதிரி விவாதித்திருக்கிறது, பிழைபடவில்லை.
9. **`_azure_ad_token_provider` இல் இல்லை**: `AsyncOpenAI` / `OpenAI` க்கு `_azure_ad_token_provider` பண்பு இல்லை. இந்த பண்பை அணுகும் சோதனைகள் அல்லது குறியீடுகள் `AttributeError` ஏற்படும். டோக்கன் வழங்குபவர் `api_key` ஆக அனுப்பப்படுகிறது மற்றும் கிளையண்ட் பொருளில் பரிசோதிக்க முடியாது.
10. **Snapshot / பொன்கூறுகள் கோப்புகள்**: சோதனை தொகுப்பு snapshot சோதனையை பயன்படுத்துமானால், Chat Completions streaming வடிவங்கள் (`choices[0]`, `content_filter_results`, `function_call` முதலியன) உடைய **எல்லா** snapshot கோப்புகளும் புதிய Responses வடிவத்திற்கு புதுப்பிக்கப்பட வேண்டும். இது எளிதில் தவறிக்கொள்ளப்படுகிறது மற்றும் snapshot உறுதிப்படுத்தல் தோல்விகளுக்கு காரணமாகிறது.
11. **Mock monkeypatch பாதை**: monkeypatch இலக்கு `openai.resources.chat.AsyncCompletions.create` → `openai.resources.responses.AsyncResponses.create` (அல்லது sync க்காக `Responses.create`) ஆக மாற்றப்பட்டுள்ளது. பழைய பாதையை பயன்படுத்தினால் எந்த இடையூறும் செய்யாது — mock நுழையாது, சோதனைகள் உண்மையான API ஐ அணுகி தோல்வியடையும்.
12. **`input` μην `messages`**: Mock செயல்பாடுகள் `kwargs.get("input")` ஐ படிக்க வேண்டும், `kwargs.get("messages")` அல்ல. Responses API உரையாடல் வரலாற்றுக்கு `input` ஐ பயன்படுத்துகிறது.
13. **Environ மாறி பெயரை மாற்று**: Azure அடையாள SDK `AZURE_CLIENT_ID` (இல்லை `AZURE_OPENAI_CLIENT_ID`) ஐ `ManagedIdentityCredential(client_id=...)` க்கு பயன்படுத்துகிறது. சோதனைகள், `.env` கோப்புகள், செயலிகளின் அமைப்புகள் மற்றும் Bicep/இணைப்பு கோப்புகளில் பெயரை மாற்றவும்.
14. **`max_output_tokens` குறைந்தபட்சம் 16**: Azure OpenAI 16 க்கும் கீழான மதிப்புகளை `400 integer_below_min_value` என்று நிராகரிக்கிறது. சோதனைகளுக்கு 50, நிர்வாகத்திற்கு 1000+ பயன்படுத்துக. பழைய `max_tokens` க்கு இத்தகைய குறைந்தபட்சம் இல்லை.
15. **`tenant_id` `AzureDeveloperCliCredential` க்கு**: Azure OpenAI வளம் வேறு வாடிகையாளர் இல்லையில் இருந்தால், நீங்கள் **துல்லியமாக** `tenant_id` கொடுக்க வேண்டும் — `AzureDeveloperCliCredential(tenant_id=os.getenv("AZURE_TENANT_ID"))`. இல்லையெனில், நிரல் தவறான வாடிகையாளரை அமைத்து `401` திருப்பும்.
16. **Rate வரம்புகள் ஸ்ட்ரீமிங்கில் வேறுபடுகின்றன**: Chat Completions உடன் 429 சிக்கல் ஸ்ட்ரீம் துவக்கம் தடுக்கும். Responses API ஸ்ட்ரீமிங் உடன் 429 **ஸ்ட்ரீமின் நடுவில்** ஏற்படலாம் — ஏசிங்க் இட்டரேட்டர் பிழையை எழுப்பும். எப்போதும் ஸ்ட்ரீமிங் சுற்றி `try/except` மூடி, பிழை JSON வரி முன்னணி பகுதியுக்கு அனுப்பு, அதனை அரவணைக்க frontend அனுமதிக்கவும்.

17. **வெப் செயலிகளுக்கு ஸ்ட்ரீமிங் பிழை முகாமை கட்டாயம்**: `try: async for event in await coroutine: ... except Exception as e: yield json.dumps({"error": str(e)})` என்ற மாதிரி அவசியம். இத बिना, SSE/JSONL ஸ்ட்ரீம் சேவையக பக்க பிழை ஏற்படும்போது அமைதியாக நிற்கும் மற்றும் முன்னணி இடைமுகம் கமனம் ஆகும்.
18. **கருவி வரையறைகள் சீரான வடிவிலேயே இருக்க வேண்டும்**: Responses API `{"type": "function", "name": ..., "parameters": ...}` என்பதை எதிர்பார்க்கிறது — Chat Completions இல் உள்ள நெஸ்டட் `{"type": "function", "function": {"name": ..., "parameters": ...}}` அல்ல. இது செயல்பாடு அழைக்கும் குறியீட்டில் மிகவும் சந்தர்ப்பமான பிழை ஆகும்.
19. **`pydantic_function_tool()` பொருந்தாது**: `openai.pydantic_function_tool()` உதவியாளர் பழைய நெஸ்டட் வடிவை இன்னும் உருவாக்குகிறது. இதனை `responses.create()` உடன் பயன்படுத்த வேண்டாம். கருவி ஸ்கீமைகளை கையால் வரையறுக்க வேண்டும் அல்லது வெளியீட்டை சீரான வடிவில் மாற்ற வேண்டும்.
20. **கருவி முடிவுகள் `function_call_output` ஐப் பயன்படுத்த வேண்டும், `role: tool` அல்ல**: ஒரு கருவி செயல்படுத்திய பிறகு `{"type": "function_call_output", "call_id": ..., "output": ...}` சேர்க்கவும் — `{"role": "tool", "tool_call_id": ..., "content": ...}` அல்ல. உதவியாளரின் கருவி கோரிக்கைக்கு `messages.extend(response.output)` பயன்படுத்தவும் — கைமுறை `{"role": "assistant", "tool_calls": [...]}` அகராதி பயன்படுத்த வேண்டாம்.
21. **`strict: true` என்பதற்கு `required` + `additionalProperties: false` அவசியம்**: ஒரு கருவியில் `strict: true` பயன்படுத்தும் போது, ஒவ்வொரு சொத்தும் `required` வரிசையில் சேர்க்கப்பட வேண்டும் மற்றும் `additionalProperties` மதிப்பு `false` ஆக இருக்க வேண்டும். யாராவது இல்லாவிட்டால் 400 பிழை ஏற்படும்.
22. **செயல்பாடு அழைக்கும் ID களுக்கு குறிப்பிட்ட முன்னொட்டி இருக்க வேண்டும்**: `input` இல் சில செயல்பாடு அழைப்புகளை வழங்கும் போது, `id` புலம் `fc_` என்று துவங்க வேண்டும் மற்றும் `call_id` புலம் `call_` என்று துவங்க வேண்டும் (உதா: `"id": "fc_example1", "call_id": "call_example1"`). பழைய Chat Completions இல் `id`க்கு `call_` முன்னொட்டை பயன்படுத்துவது நிராகரிக்கப்படும்.
23. **GitHub Models Responses API ஐ ஆதரிக்காது**: செயலியில் GitHub Models குறியீட்டு பாதை (`base_url` `models.github.ai` அல்லது `models.inference.ai.azure.com` என்பதைக் குறிக்கும்) இருந்தால் முழுமையாக அகற்று. மாற்றம் செய்யலாமான பாதை இல்லை — Azure OpenAI, OpenAI அல்லது பொருந்தக்கூடிய உள்ளூர் முனையத்துக்கு மாற்றவும்.
24. **உள்ளடக்க வடிகட்டி பிழை உடல் அமைப்பு மாறியுள்ளது**: Chat Completions பிழைகள் `error.body["innererror"]["content_filter_result"]` (ஒற்றை) பயன்படுத்தின. Responses API பிழைகள் `error.body["content_filters"][0]["content_filter_results"]` (பல தொகுப்பாக, மட்டத்தில்) பயன்படுத்துகின்றன. `innererror` விசை இனி இல்லை. நேரடியாக `innererror` அணுகும் குறியீடு ஓட்டுநேரத்தில் `KeyError` ஏற்படுத்தும் — இது மாற்றத்தில் கவனிக்க பிரச்சனை சென்று, உள்ளடக்க வடிகட்டி உண்மையில் செயல்படும் போது மட்டுமே வெளிப்படும். மாற்றத்தின் போது எப்போதும் `innererror` க்கான தேடலைச் செய்ய வேண்டும்.
25. **நெருக்கடியான HTTP அழைப்புகளுக்கு URL + உடல் மறுசீரமைப்பு தேவை**: Azure OpenAI REST ஐ நேரடியாக ( `requests`, `httpx`, `aiohttp` மூலம்) `/openai/deployments/{name}/chat/completions?api-version=...` என்ற முகவரியில் அழைக்கும் செயலிகள் `/openai/v1/responses` க்கு மாற்ற வேண்டும். கோரிக்கை உடல் `messages` பதிலாக `input` பயன்படுத்தும், `max_output_tokens` மற்றும் `store` தேவை, மற்றும் `api-version` கேள்விப் பர் நீக்கப்படும். பதில் உடல் உரை `output[0].content[0].text` இல் இருக்கிறது — **இல்லை** `output_text`, இது SDK வசதி சொத்தாகும் மற்றும் மூல REST JSON இல் இல்லை.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**மறுப்பு**:
இந்த ஆவணம் AI மொழிபெயர்ப்பு சேவை [Co-op Translator](https://github.com/Azure/co-op-translator) பயன்படுத்தி மொழிபெயர்க்கப்பட்டுள்ளது. நாங்கள் துல்லியத்திற்காக முயற்சி செய்துள்ளோம், ஆனால் தானாக செய்யப்படும் மொழிபெயர்ப்புகளில் பிழைகள் அல்லது தவறுகள் இருக்கலாம் என்பதை கவனத்தில் கொள்ளவும். அசல் ஆவணம் அதன் தாய்மொழியில் அதிகாரப்பூர்வ ஆதாரமாக கருதப்பட வேண்டும். முக்கியமான தகவல்களுக்கு, தொழில்நுட்பமான மனித மொழிபெயர்ப்பு பரிந்துரைக்கப்படுகிறது. இந்த மொழிபெயர்ப்பைப் பயன்படுத்துவதால் ஏற்படும் எந்த தவறான புரிதல்கள் அல்லது தவறான விளக்கத்திற்கும் நாங்கள் பொறுப்பில்வில்லை.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->