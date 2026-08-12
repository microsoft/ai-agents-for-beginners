# সমস্যা সমাধান, ঝুঁকি টেবিল এবং সতর্কতা গুলো

## 400s সমস্যা সমাধান

| ত্রুটি | সমাধান |
|-------|-----|
| `missing_required_parameter: tools[0].name` | টুল সংজ্ঞায়ন পুরাতন Chat Completions নেস্টেড ফরম্যাট ব্যবহার করছে | `{"type": "function", "function": {"name": ...}}` থেকে ফ্ল্যাট করুন `{"type": "function", "name": ..., "parameters": ...}` — name, description, parameters উপরের স্তরে যাবে |
| `unknown_parameter: input[N].tool_calls` | Multi-turn টুল ফলাফলগুলি পুরাতন Chat Completions ফরম্যাট ব্যবহার করছে | `{"role": "assistant", "tool_calls": [...]}` + `{"role": "tool", ...}` এর পরিবর্তে `response.output` আইটেম + `{"type": "function_call_output", "call_id": ..., "output": ...}` ব্যবহার করুন |
| `invalid_function_parameters: 'required' is required` | `strict: true` টুলে `required` অ্যারে নেই | যখন `strict: true` থাকে, সব প্রপার্টি `required` অ্যারেতে তালিকাভুক্ত থাকতে হবে এবং `additionalProperties: false` সেট করতে হবে |
| `invalid_function_parameters: 'additionalProperties' is required` | `strict: true` টুলে `additionalProperties: false` নেই | প্যারামিটার অবজেক্টে `"additionalProperties": false` যোগ করুন |
| `invalid input[N].id: Expected an ID that begins with 'fc'` | Few-shot function_call আইডির প্রিফিক্স ভুল | ফাংশন কল আইডি অবশ্যই `fc_` দিয়ে শুরু হবে (যেমন, `fc_example1`), `call_` নয় |
| `missing_required_parameter: text.format.name` | ফরম্যাট ডিকশনারিতে `"name"` কী যুক্ত করুন (যেমন, `"name": "Output"`) |
| `invalid_type: text.format` | নিশ্চিত করুন যে `text.format` একটি ডিকশনারি যার মধ্যে `type`, `name`, `strict`, `schema` কী আছে — স্ট্রিং নয় |
| `invalid input content type` | Chat `text` এর পরিবর্তে `input_text`/`output_text` কন্টেন্ট টাইপ ব্যবহার করুন |
| `invalid input content type` (image) | ইমেজ কন্টেন্ট এখনও `"type": "image_url"` ব্যবহার করছে | পরিবর্তন করুন `"type": "input_image"` এ |
| `Expected object, got string` on `image_url` | `image_url` এখনও একটি নেস্টেড অবজেক্ট `{"url": "..."}` | এটিকে একটি সোজা স্ট্রিংয়ে ফ্ল্যাট করুন: `"image_url": "https://..."` অথবা `"image_url": "data:image/...;base64,..."` |
| `integer below minimum value` for `max_output_tokens` | Azure OpenAI এ ন্যূনতম মান **16** । টেস্টের জন্য ৫০+ এবং প্রোডাকশনের জন্য ১০০০+ ব্যবহার করুন। |
| `429 Too Many Requests` during streaming | রেট লিমিট হয়েছে। স্ট্রিমিংকে `try/except` ব্লকে রাখুন, ফ্রন্টেন্ডে ত্রুটির JSON পাঠান, ব্যাকঅফ/রিট্রাই প্রয়োগ করুন। |
| `KeyError: 'innererror'` on content filter error | Responses API তে কন্টেন্ট ফিল্টার ত্রুটি বডির কাঠামো পরিবর্তিত হয়েছে | Chat Completions এ `error.body["innererror"]["content_filter_result"]` ব্যবহৃত হত; Responses API তে এটি `error.body["content_filters"][0]["content_filter_results"]` (বহুবচন, একটি অ্যারের ভিতরে)। সব `innererror` অ্যাক্সেস পুনর্লিখন করুন। |

---

## মাইগ্রেশন ঝুঁকি টেবিল

| লক্ষণ | সম্ভাব্য ভুল | সমাধান |
|---------|---------------|-----|
| খালি `output_text` / সংক্ষিপ্ত উত্তর | রিজনিং মডেলের জন্য `max_output_tokens` খুব কম | `max_output_tokens=1000` বা তার বেশি সেট করুন — রিজনিং টোকেন গুলো সীমার বিরুদ্ধে গণনা হয় |
| `400 invalid_type: text.format` | `response_format` স্ট্রিং পাঠানো হয়েছে, `text.format` ডিকশনারির বদলে | `text={"format": {"type": "json_schema", "name": "...", "strict": True, "schema": {...}}}` ব্যবহার করুন |
| `/openai/v1/responses` এ `404 Not Found` | ভুল `base_url` — শেষে `/openai/v1/` নেই | নিশ্চিত করুন `base_url=f"{endpoint}/openai/v1/"` (ট্রেইলিং স্ল্যাশ সহ) |
| `401 Unauthorized` যখন `OpenAI()` এ সুইচ করেছেন | `api_key` সেট করা হয়নি বা টোকেন প্রোভাইডার সঠিকভাবে পাঠানো হয়নি | EntraID এর জন্য: `api_key=token_provider` (কল করার যোগ্য)। API কী এর জন্য: `api_key=os.environ["AZURE_OPENAI_API_KEY"]` |
| মডেল দেয় `deployment not found` | `model` প্যারামিটার আপনার Azure ডিপ্লয়মেন্ট নামের সাথে মেলে না | `model=os.environ["AZURE_OPENAI_DEPLOYMENT"]` ব্যবহার করুন — এটি ডিপ্লয়মেন্টের নাম, মডেলের নাম নয় |
| `json.loads(resp.output_text)` এ `JSONDecodeError` | স্কিমা প্রয়োগ হয়েছে না বা মডেল কঠিন JSON সমর্থন করে না | স্কিমায় `"strict": True` নিশ্চিত করুন, এবং মডেল স্ট্রাকচার্ড আউটপুট সমর্থন করে কিনা যাচাই করুন |
| স্ট্রিমিং কোনও `delta` ইভেন্ট দেয় না | ভুল ইভেন্ট টাইপ যাচাই করছেন | `event.type == "response.output_text.delta"` অনুযায়ী ফিল্টার করুন, না যে Chat এর `chat.completion.chunk` |
| মাইগ্রেশনের পর ছবি ইনপুটে `400` ত্রুটি | ইমেজ কন্টেন্ট টাইপ আপডেট হয়নি | `"type": "image_url"` → `"type": "input_image"` এবং `"image_url": {"url": "..."}` → `"image_url": "..."` (প্লেইন স্ট্রিং) পরিবর্তন করুন |
| টুল কল অবিরাম লুপ করছে | ফলো-আপ `input` এ টুল ফলাফল অনুপস্থিত | একটি টুল চালানোর পর, পরবর্তী অনুরোধে `input` এ `{"type": "function_call_output", "call_id": ..., "output": ...}` আইটেম যোগ করুন |
| GPT-5 বা o-series এ `temperature` ত্রুটি | 1 ব্যতীত স্পষ্ট `temperature` মান | GPT-5 এবং o-series মডেলের জন্য `temperature` সরান অথবা ১ সেট করুন (o1, o3-mini, o3, o4-mini) |
| o-series তে `top_p` ত্রুটি | `top_p` সমর্থিত নয় | o-series মডেল টার্গেট করলে `top_p` সরান |
| `max_completion_tokens` চিনে নেয় না | Azure-সুনির্দিষ্ট প্যারামিটার ব্যবহার | `max_completion_tokens` এর বদলে `max_output_tokens` ব্যবহার করুন। o-series এর জন্য 4096+ সেট করুন (রিজনিং টোকেন গুলো সীমার বিরুদ্ধে গণনা হয়)। |
| o-series থেকে খালি/সংক্ষিপ্ত আউটপুট | `max_output_tokens` খুব কম | o-series ভিতরে রিজনিং টোকেন ব্যবহার করে। `max_output_tokens=4096` বা তার বেশি দিন — ৫০০–১০০০ নয়। |
| `400 integer_below_min_value` `max_output_tokens` এর জন্য | ১৬ এর নিচে মান | Azure OpenAI প্রয়োগ করে `max_output_tokens >= 16`। স্মোক টেস্টের জন্য ৫০+, প্রোডাকশনের জন্য ১০০০+ ব্যবহার করুন। |
| স্ট্রিম মাঝপথে `429 Too Many Requests` | Azure OpenAI দ্বারা রেট লিমিট | স্ট্রিম ছিন্ন হয় নীরবে, ত্রুটি হ্যান্ডলিং ছাড়া। সর্বদা `async for event in await coroutine:` স্ট্রিমিং লুপ `try/except` দিয়ে আবৃত করুন এবং ফ্রন্টেন্ডে `{"error": str(e)}` পাঠান। |
| `AzureDeveloperCliCredential` → `CredentialUnavailableError` | ভুল টেন্যান্ট অথবা লগইন করা হয়নি | স্পষ্টভাবে `tenant_id=os.getenv("AZURE_TENANT_ID")` দিন। লোকালি `azd auth login --tenant <tenant-id>` চালান। |
| গিটহাব মডেলস ( `models.github.ai` ) ব্যবহার করলে `404 Not Found` | গিটহাব মডেলস Responses API সমর্থন করে না | গিটহাব মডেলস কোড সম্পূর্ণ সরিয়ে ফেলুন। Azure OpenAI, OpenAI, বা সামঞ্জস্যপূর্ণ লোকাল এন্ডপয়েন্ট (যেমন Ollama যার Responses সমর্থন রয়েছে) ব্যবহার করুন। |
| MAF `OpenAIChatCompletionClient` এখনও Chat Completions ব্যবহার করছে | 1.0.0+ তে পুরাতন MAF ক্লায়েন্ট ব্যবহার করছেন | MAF 1.0.0+ এ `OpenAIChatClient` ডিফল্ট রূপে Responses API ব্যবহার করে। `OpenAIChatCompletionClient` বদলে `OpenAIChatClient` ব্যবহার করুন। 1.0.0 এর আগে থাকলে `agent-framework-openai>=1.0.0` এ আপগ্রেড করুন। |
| LangChain এজেন্ট টুল কলের সাথে ফাঁকা রিটার্ন করে বা ব্যর্থ হয় | `ChatOpenAI` Responses API ব্যবহার করছে না | `ChatOpenAI(...)` তে `use_responses_api=True` যোগ করুন। রেসপন্স মেসেজের `.content` কে `.text` করুন। |
| কন্টেন্ট ফিল্টার ত্রুটি হ্যান্ডলারে `KeyError: 'innererror'` | Responses API তে ত্রুটি বডির কাঠামো পরিবর্তন | `error.body["innererror"]["content_filter_result"]["jailbreak"]` → `error.body["content_filters"][0]["content_filter_results"]["jailbreak"]` এ পুনর্লিখন করুন। `innererror` মোড়ক চলে গেছে; কন্টেন্ট ফিল্টার ডিটেইলস এখন উপরের স্তরের `content_filters` অ্যারে, যার প্রতিটি এন্ট্রিতে `content_filter_results` (বহুবচন) থাকে। |
| `/openai/deployments/.../chat/completions` র কাঁচা HTTP কল 404 দেয় | পুরাতন Chat Completions REST এন্ডপয়েন্ট | URL `/openai/v1/responses` এ পরিবর্তন করুন। রিকোয়েস্ট বডি: `messages` → `input`, `max_output_tokens` + `store: false` যোগ করুন, `api-version` কুয়েরি প্যারামিটার সরান। রেসপন্স পার্সিং পরিবর্তন: `choices[0].message.content` → `output[0].content[0].text` (দ্রষ্টব্য: `output_text` একটি SDK সুবিধা, কাঁচা REST JSON এ নেই)। |

---

## সতর্কতা

1. আগের মতো Chat Completions ব্যবহার করলে, ইচ্ছাকৃতভাবে আপনার নিজস্ব স্টেট Responses-সহ ম্যানেজ করুন।
2. পুরাতন `max_tokens` এর বদলে `max_output_tokens` প্রাধান্য দিন।
3. `gpt-5` এ মাইগ্রেট করার সময় নিশ্চিত করুন `temperature` নির্দিষ্ট নয় অথবা ১ সেট করা আছে।
4. Chat এর `content[].type: "text"` কে Responses এর `content[].type: "input_text"` দিয়ে বদলান, বিশেষত ব্যবহারকারী/সিস্টেম ইনপুটে।
5. `text.format` এর জন্য সঠিক ডিকশনারি দিন (যেমন `{"type": "json_schema", "name": "Output", "schema": ..., "strict": True}`), সোজা স্ট্রিং নয়।
6. Responses এ `seed` প্যারামিটার সমর্থিত নয়; অনুরোধ থেকে সরিয়ে ফেলুন।
7. **রিজনিং:** মূল কোডে রিজনিং ব্যবহার থাকলে শুধু তাই অন্তর্ভুক্ত করুন। যেসব API কলের মধ্যে ছিল না সেখানে রিজনিং যোগ করবেন না — অনেক গে রিজনিং মডেল এই প্যারামিটার সমর্থন করে না।
8. **`max_output_tokens` সাইজ:** রিজনিং মডেল (GPT-5-mini, GPT-5, o-series) এর জন্য `max_output_tokens=4096` বা তার বেশি ব্যবহার করুন — ৫০–১০০০ নয়। মডেল আউটপুটের আগে ভিতরে রিজনিং টোকেন ব্যবহার করে; খুব কম মানে ট্রাঙ্কেট বা খালি রেসপন্স হবে।
9. **o-series `max_completion_tokens`:** যদি মূল কোডে `max_completion_tokens` (o-series এর Azure-সুনির্দিষ্ট) ব্যবহার হয়, তাহলে `max_output_tokens` দিয়ে বদলান। Responses API `max_completion_tokens` গ্রহণ করে না।
10. **o-series `reasoning_effort`:** যদি মূল কোডে `reasoning_effort` (low/medium/high) ব্যবহার হয়, তাহলে Responses API কলের মধ্যে `reasoning={"effort": "<value>"}` এ মাইগ্রেট করুন।
11. **o-series স্ট্রিমিং দেরি:** o-series মডেল ভিতরে রিজনিং করার পর আউটপুট তৈরি করে। স্ট্রিমিং এর প্রথম `response.output_text.delta` ইভেন্টের আগে দীর্ঘ দেরি আশা করুন। এটি স্বাভাবিক — মডেল রিজনিং করছে, আটকে নেই।
9. **`_azure_ad_token_provider` নেই:** `AsyncOpenAI` / `OpenAI` এর মধ্যে `_azure_ad_token_provider` অ্যাট্রিবিউট নেই। যদি টেস্ট বা কোড এই অ্যাট্রিবিউটে প্রবেশ করার চেষ্টা করে তবে `AttributeError` হবে। টোকেন প্রোভাইডার `api_key` হিসেবে পাঠানো হয় এবং ক্লায়েন্ট অবজেক্টে দেখা যায় না।
10. **স্ন্যাপশট / গোল্ডেন ফাইল:** যদি টেস্ট সুট স্ন্যাপশট টেস্টিং ব্যবহার করে, তাহলে **সব** স্ন্যাপশট ফাইল যেগুলো Chat Completions স্ট্রিমিং শেপ (যেমন `choices[0]`, `content_filter_results`, `function_call` ইত্যাদি) রয়েছে, সেগুলো নতুন Responses শেপে আপডেট করতে হবে। এড়িয়ে গেলে স্ন্যাপশট অ্যাসারশন ব্যর্থ হবে।
11. **মক মনকিপ্যাচ পাথ:** মনকিপ্যাচ লক্ষ্য `openai.resources.chat.AsyncCompletions.create` থেকে পরিবর্তিত হয়ে `openai.resources.responses.AsyncResponses.create` (অথবা সিঙ্কের জন্য `Responses.create`) হয়ে গেছে। পুরাতন পাথ ব্যবহার করলে মক কোনো কার্যকর হবেনা — মক ইন্টারসেপ্ট করবে না, টেস্ট বাস্তব API স্পর্শ করবে বা ব্যর্থ হবে।
12. **`input`, `messages` নয়:** মক ফাংশনগুলোকে `kwargs.get("input")` পড়তে হবে, `kwargs.get("messages")` নয়। Responses API কথোপকথনের ইতিহাসে `input` ব্যবহার করে।
13. **এনভায়রনমেন্ট ভ্যারিয়েবল নামকরণ:** Azure Identity SDK `ManagedIdentityCredential(client_id=...)` এর জন্য `AZURE_CLIENT_ID` (না যে `AZURE_OPENAI_CLIENT_ID`) ব্যবহার করে। টেস্ট, `.env` ফাইল, অ্যাপ সেটিংস, এবং Bicep/ইনফ্রাতে নাম পরিবর্তন করুন।
14. **`max_output_tokens` ন্যূনতম ১৬:** Azure OpenAI ১৬ এর নিচের মান `400 integer_below_min_value` ত্রুটি দেবে। স্মোক টেস্টে ৫০ ব্যবহার করুন, প্রোডাকশনে ১০০০+। পুরাতন `max_tokens` এর এমন কোনো ন্যূনতম সীমা ছিল না।
15. **`AzureDeveloperCliCredential` এর জন্য `tenant_id`:** যখন Azure OpenAI রিসোর্স ভিন্ন টেন্যান্টে থাকে, আপনি অবশ্যই স্পষ্টভাবে `tenant_id` পাঠাতে হবে — `AzureDeveloperCliCredential(tenant_id=os.getenv("AZURE_TENANT_ID"))`। তা না হলে ক্রেডেনশিয়াল ভুল টেন্যান্ট ব্যবহার করে চলে যাবে এবং `401` রিটার্ন করবে।
16. **স্ট্রিমিং-এ রেট লিমিট ভিন্নভাবে হয়:** Chat Completions এ 429 সাধারনত স্ট্রিম শুরু থেকে আটকাত। Responses API স্ট্রিমিং এ 429 **মাঝপথে** ঘটতে পারে — অ্যাসিঙ্ক ইটারেটর একটি ব্যতিক্রম ছুড়ে দেয়। সর্বদা স্ট্রিমিং লুপ `try/except` দিয়ে আবৃত করুন এবং একটি ত্রুটি JSON লাইন পাঠান যাতে ফ্রন্টেন্ড সেটি সুন্দরভাবে হ্যান্ডেল করতে পারে।

১৭। **ওয়েব অ্যাপসের জন্য স্ট্রিমিং ত্রুটি পরিচালনা বাধ্যতামূলক**: `try: async for event in await coroutine: ... except Exception as e: yield json.dumps({"error": str(e)})` প্যাটার্নটি অত্যন্ত গুরুত্বপূর্ণ। এটি ছাড়া, যেকোনো সার্ভার-সাইড ত্রুটিতে SSE/JSONL স্ট্রিম নিঃশব্দে শেষ হয়ে যায় এবং ফ্রন্টএন্ড হ্যাং হয়ে যায়।
১৮। **টুল ডেফিনিশনগুলো অবশ্যই ফ্ল্যাট ফরম্যাটে হতে হবে**: Responses API প্রত্যাশা করে `{"type": "function", "name": ..., "parameters": ...}` — Chat Completions এর নেস্টেড `{"type": "function", "function": {"name": ..., "parameters": ...}}` নয়। ফাংশন-কলিং কোডের জন্য এই সবচেয়ে সাধারণ মাইগ্রেশন ত্রুটি।
১৯। **`pydantic_function_tool()` অসামঞ্জস্যপূর্ণ**: `openai.pydantic_function_tool()` হেল্পার এখনও পুরনো নেস্টেড ফরম্যাট তৈরি করে। এটি `responses.create()` এর সাথে ব্যবহার করবেন না। সরঞ্জাম স্কিমাগুলো ম্যানুয়ালি ডিফাইন করুন বা আউটপুট ফ্ল্যাট করুন।
২০। **টুল ফলাফলগুলো `function_call_output` ব্যবহার করে, `role: tool` নয়**: টুল এক্সিকিউট করার পর, `{"type": "function_call_output", "call_id": ..., "output": ...}` যুক্ত করুন — `{"role": "tool", "tool_call_id": ..., "content": ...}` নয়। সহকারীর টুল অনুরোধের জন্য, `messages.extend(response.output)` ব্যবহার করুন — ম্যানুয়াল `{"role": "assistant", "tool_calls": [...]}` ডিক্ট নয়।
২১। **`strict: true` এর জন্য `required` + `additionalProperties: false` প্রয়োজন**: টুলে `strict: true` ব্যবহার করলে প্রতিটি প্রপার্টি অবশ্যই `required` অ্যারেতে থাকতে হবে এবং `additionalProperties` অবশ্যই `false` হতে হবে। এর কোনোটাই বাদ দিলে ৪০০ ত্রুটি হয়।
২২। **ফাংশন কল আইডির নির্দিষ্ট প্রিফিক্স আছে**: যখন few-shot `function_call` আইটেম `input` এ দেওয়া হয়, তখন `id` ফিল্ড `fc_` দিয়ে শুরু হবে এবং `call_id` ফিল্ড `call_` দিয়ে শুরু হবে (যেমন, `"id": "fc_example1", "call_id": "call_example1"`)। পুরনো Chat Completions এর `call_` প্রিফিক্স `id` এর জন্য ব্যবহার করলে অগ্রহণযোগ্য।
২৩। **GitHub Models Responses API সমর্থন করে না**: যদি অ্যাপে GitHub Models কোড পাথ থাকে (`base_url` যা `models.github.ai` বা `models.inference.ai.azure.com` নির্দেশ করে), তাহলে এটিকে সম্পূর্ণরূপে সরিয়ে ফেলুন। কোনো মাইগ্রেশন পথ নেই — Azure OpenAI, OpenAI, বা একটি সামঞ্জস্যপূর্ণ লোকাল এন্ডপয়েন্টে স্যুইচ করুন।
২৪। **কন্টেন্ট ফিল্টার ত্রুটির বডির কাঠামো পরিবর্তিত হয়েছে**: Chat Completions ত্রুটিতে `error.body["innererror"]["content_filter_result"]` (একবচন) ব্যবহার হতো। Responses API ত্রুটিতে `error.body["content_filters"][0]["content_filter_results"]` (বহুবচন, একটি অ্যারের ভিতরে) ব্যবহার হয়। `innererror` কী আর নেই। সরাসরি `innererror` অ্যাক্সেস করলে রানটাইমে `KeyError` উঠবে — মাইগ্রেশনে এটা সহজে মিস হতে পারে কারণ এটি কেবলমাত্র কন্টেন্ট ফিল্টার আসলেই ট্রিগার হলে প্রকাশ পায়। মাইগ্রেশনের সময় সর্বদা `innererror` grep করুন।
২৫। **রাউ HTTP কলগুলোতে URL + বডি পুনর্লিখন প্রয়োজন**: Azure OpenAI REST সরাসরি কল করা অ্যাপগুলো (যেমন `requests`, `httpx`, `aiohttp`) `/openai/deployments/{name}/chat/completions?api-version=...` থেকে অবশ্যই `/openai/v1/responses` এ স্যুইচ করবে। রিকোয়েস্ট বডিতে `messages` নয়, `input` ব্যবহার হবে, এবং `max_output_tokens` ও `store` প্রয়োজন, এবং `api-version` কোয়েরি প্যারামিটার বাদ দেয়া হবে। রেসপন্স বডির টেক্সট `output[0].content[0].text` এ থাকে — **না** `output_text` এ, যা SDK এর একটি সুবিধাজনক প্রপার্টি এবং রাউ REST JSON এ নেই।

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**অস্বীকৃতি**:
এই নথিটি AI অনুবাদ পরিষেবা [Co-op Translator](https://github.com/Azure/co-op-translator) ব্যবহার করে অনূদিত হয়েছে। যদিও আমরা শুদ্ধতার জন্য চেষ্টা করি, অনুগ্রহ করে মনে রাখবেন যে স্বয়ংক্রিয় অনুবাদে ত্রুটি বা অসঙ্গতি থাকতে পারে। মূল নথিটি তার স্বভাষায় কর্তৃত্বপূর্ণ উৎস হিসেবে বিবেচিত হওয়া উচিত। গুরুত্বপূর্ণ তথ্যের জন্য পেশাদার মানব অনুবাদ সুপারিশ করা হয়। এই অনুবাদের ব্যবহারে প্রয়োজনীয় ভুল বোঝাবুঝি বা ভুল ব্যাখ্যার জন্য আমরা দায়বদ্ধ নই।
<!-- CO-OP TRANSLATOR DISCLAIMER END -->