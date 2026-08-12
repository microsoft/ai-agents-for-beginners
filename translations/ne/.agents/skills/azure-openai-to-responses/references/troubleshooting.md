# समस्या समाधान, जोखिम तालिका र समस्या हुने कुराहरू

## 400 त्रुटिहरू समस्या समाधान

| त्रुटि | समाधान |
|-------|-----|
| `missing_required_parameter: tools[0].name` | उपकरण परिभाषा पुरानो Chat Completions नेस्ट गरिएको प्रारूप प्रयोग गर्छ | `{"type": "function", "function": {"name": ...}}` बाट `{"type": "function", "name": ..., "parameters": ...}` मा समतल गर्नुहोस् — नाम, वर्णन, प्यारेमेटरहरू शीर्ष स्तरमा जान्छन् |
| `unknown_parameter: input[N].tool_calls` | मल्टि-टर्न उपकरण परिणामहरू पुरानो Chat Completions प्रारूप प्रयोग गर्छन् | `{"role": "assistant", "tool_calls": [...]}` + `{"role": "tool", ...}` सँग प्रतिस्थापन गर्नुहोस् `response.output` आइटमहरू + `{"type": "function_call_output", "call_id": ..., "output": ...}` |
| `invalid_function_parameters: 'required' is required` | `strict: true` उपकरणले `required` array गुमायो | जब `strict: true` हुन्छ, सबै सम्पत्तिहरू `required` मा सूचीबद्ध हुनुपर्छ र `additionalProperties: false` सेट गर्नुपर्छ |
| `invalid_function_parameters: 'additionalProperties' is required` | `strict: true` उपकरणले `additionalProperties: false` हरायो | प्यारेमेटर वस्तुमा `"additionalProperties": false` थप्नुहोस् |
| `invalid input[N].id: Expected an ID that begins with 'fc'` | Few-shot function_call ID सँग गलत उपसर्ग छ | Function call ID ले `fc_` बाट शुरू हुनुपर्छ (जस्तै, `fc_example1`), `call_` होइन |
| `missing_required_parameter: text.format.name` | स्वरूप dict मा `"name"` कुञ्जी थप्नुहोस् (जस्तै, `"name": "Output"`) |
| `invalid_type: text.format` | सुनिश्चित गर्नुहोस् `text.format` dict हो जसमा `type`, `name`, `strict`, `schema` कुञ्जीहरू छन् — स्ट्रिङ होइन |
| `invalid input content type` | Chat `text` सट्टा `input_text` / `output_text` सामग्री प्रकारहरू प्रयोग गर्नुहोस् |
| `invalid input content type` (तस्बिर) | तस्बिर सामग्री अझै `"type": "image_url"` प्रयोग गर्दैछ | `"type": "input_image"` मा परिवर्तन गर्नुहोस् |
| `Expected object, got string` on `image_url` | `image_url` अझै नेस्ट गरिएको वस्तु छ `{"url": "..."}` | यो सामान्य स्ट्रिङमा समतल गर्नुहोस्: `"image_url": "https://..."` वा `"image_url": "data:image/...;base64,..."` |
| `integer below minimum value` for `max_output_tokens` | Azure OpenAI मा न्यूनतम **16** छ। परीक्षणका लागि 50+ र उत्पादनका लागि 1000+ प्रयोग गर्नुहोस्। |
| `429 Too Many Requests` स्ट्रिमिङको बेला | दर सीमित गरियो। स्ट्रिमिङलाई `try/except` मा राख्नुहोस्, त्रुटि JSON फ्रन्टएण्डमा पठाउनुहोस्, ब्याकअफ/पुनः प्रयास लागू गर्नुहोस्। |
| `KeyError: 'innererror'` सामग्री फिल्टर त्रुटिमा | सामग्री फिल्टर त्रुटि शरीर संरचना Responses API मा परिवर्तन भयो | Chat Completionsले `error.body["innererror"]["content_filter_result"]` प्रयोग गर्‍यो; Responses API ले `error.body["content_filters"][0]["content_filter_results"]` (बहुवचन, array भित्र) प्रयोग गर्छ। सबै `innererror` पहुँचहरू पुनर्लेखन गर्नुहोस्। |

---

## माइग्रेशन जोखिम तालिका

| लक्षण | सम्भावित गल्ती | समाधान |
|---------|---------------|-----|
| खाली `output_text` / कटा प्रतिक्रिया | तर्क मोडेलहरूका लागि `max_output_tokens` धेरै कम छ | `max_output_tokens=1000` वा माथि सेट गर्नुहोस् — तर्क टोकनहरूले सिमा बिरुद्ध गन्ती गर्छन् |
| `400 invalid_type: text.format` | `text.format` dict सट्टा `response_format` स्ट्रिङ पास गरिएको छ | प्रयोग गर्नुहोस् `text={"format": {"type": "json_schema", "name": "...", "strict": True, "schema": {...}}}` |
| `/openai/v1/responses` मा `404 Not Found` | गलत `base_url` — `/openai/v1/` suffix हरायो | पक्का गर्नुहोस् `base_url=f"{endpoint}/openai/v1/"` (ट्रेलिङ स्ल्यास सहित) |
| `401 Unauthorized` `OpenAI()` मा स्विच गरेपछि | `api_key` सेट नभएको वा टोकन प्रदायक ठीकसँग पास नगरिएको | EntraID का लागि: `api_key=token_provider` (कलेबल)। API कुञ्जीका लागि: `api_key=os.environ["AZURE_OPENAI_API_KEY"]` |
| मोडेलले `deployment not found` फर्कायो | `model` प्याराम तपाइँको Azure डिप्लोइमेन्ट नामसँग मेल खाँदैन | प्रयोग गर्नुहोस् `model=os.environ["AZURE_OPENAI_DEPLOYMENT"]` — यो डिप्लोइमेन्ट नाम हो, मोडेल नाम होइन |
| `json.loads(resp.output_text)` ले `JSONDecodeError` फ्याँक्छ | स्किमा लागू गरिएको छैन वा मोडेलले कडा JSON समर्थन गर्दैन | पक्का गर्नुहोस् स्किमामा `"strict": True` छ, र मोडेल संरचित आउटपुट समर्थन गर्दछ |
| स्ट्रिमिङले कुनै `delta` इभेन्ट दिएन | गलत इभेन्ट प्रकार जाँच्दै | `event.type == "response.output_text.delta"` मा फिल्टर गर्नुहोस्, Chat को `chat.completion.chunk` होइन |
| माइग्रेशन पछि तस्बिर इनपुटमा `400` त्रुटि | तस्बिर सामग्री प्रकार अपडेट भएको छैन | `"type": "image_url"` → `"type": "input_image"` मा बदल्नुहोस् र `"image_url": {"url": "..."}` → `"image_url": "..."` (साधारण स्ट्रिङ) मा समतल गर्नुहोस् |
| उपकरण कलहरू अनन्त लूपमा जान्छन् | पछिल्लोपटक `input` मा उपकरण परिणाम हरायो | उपकरण सञ्चालन पछि अर्को अनुरोधमा `input` मा `{"type": "function_call_output", "call_id": ..., "output": ...}` आइटम थप्नुहोस् |
| GPT-5 वा o-series सँग `temperature` त्रुटि | 1 बाहेक स्पष्ट `temperature` मान | GPT-5 र o-series मोडेलहरूको लागि `temperature` हटाउनुहोस् वा `1` मा सेट गर्नुहोस् (o1, o3-mini, o3, o4-mini) |
| o-series सँग `top_p` त्रुटि | `top_p` समर्थित छैन | o-series मोडेलहरूको लक्ष्य गर्दा `top_p` हटाउनुहोस् |
| `max_completion_tokens` मान्यता पाएको छैन | Azure-विशिष्ट प्याराम प्रयोग गर्दै | `max_completion_tokens` लाई `max_output_tokens` सँग परिवर्तन गर्नुहोस्। o-series का लागि 4096+ मा सेट गर्नुहोस् (तर्क टोकनहरू सिमा बिरुद्ध गन्ती गर्छन्)। |
| o-series बाट खाली/कटिएको आउटपुट | `max_output_tokens` धेरै कम छ | o-series भित्रै तर्क टोकनहरू प्रयोग गर्छ। `max_output_tokens=4096` वा माथि सेट गर्नुहोस् — 500–1000 होइन। |
| `400 integer_below_min_value` for `max_output_tokens` | मान 16 भन्दा कम छ | Azure OpenAI ले `max_output_tokens >= 16` लागू गर्छ। स्मोक टेस्टका लागि 50+ र उत्पादनका लागि 1000+ प्रयोग गर्नुहोस्। |
| स्ट्रिमका बीचमा `429 Too Many Requests` | Azure OpenAI द्वारा दर सीमित | स्ट्रिम बिनाकुनै त्रुटि ह्यान्डलिङ बिना चुपचाप टुट्छ। सधैं `async for event in await coroutine:` लाई `try/except` मा राख्नुहोस् र फ्रन्टएण्डमा `{"error": str(e)}` पठाउनुहोस्। |
| `AzureDeveloperCliCredential` → `CredentialUnavailableError` | गलत टेनन्ट वा लगइन गरिएको छैन | स्पष्ट रूपमा `tenant_id=os.getenv("AZURE_TENANT_ID")` पास गर्नुहोस्। स्थानीय रूपमा `azd auth login --tenant <tenant-id>` चलाउनुहोस्। |
| GitHub मोडेलहरू प्रयोग गर्दा `404 Not Found` (`models.github.ai`) | GitHub मोडेलले Responses API समर्थन गर्दैन | GitHub मोडेलको कोड पथ पूर्ण रूपमा हटाउनुहोस्। Azure OpenAI, OpenAI वा अनुकूल स्थानीय एन्डपोइन्ट प्रयोग गर्नुहोस् (जस्तै, प्रतिक्रिया समर्थनसहितको Ollama)। |
| MAF `OpenAIChatCompletionClient` अझै Chat Completions प्रयोग गर्दैछ | MAF 1.0.0+ मा पुरानो क्लाइन्ट प्रयोग गर्दै | MAF 1.0.0+ मा `OpenAIChatClient` डिफल्ट रूपमा Responses API प्रयोग गर्छ। `OpenAIChatCompletionClient` लाई `OpenAIChatClient` सँग प्रतिस्थापन गर्नुहोस्। 1.0.0 भन्दा अघि, `agent-framework-openai>=1.0.0` मा अपग्रेड गर्नुहोस्। |
| LangChain एजेन्टले खाली परिणाम दिन्छ वा उपकरण कलसँग असफल हुन्छ | `ChatOpenAI` Responses API प्रयोग गरिरहेको छैन | `ChatOpenAI(...)` मा `use_responses_api=True` थप्नुहोस्। साथै प्रतिक्रिया सन्देशहरूमा `.content` लाई `.text` मा परिवर्तन गर्नुहोस्। |
| सामग्री फिल्टर त्रुटि ह्यान्डलरमा `KeyError: 'innererror'` | Responses API मा त्रुटि शरीर संरचना परिवर्तन भयो | `error.body["innererror"]["content_filter_result"]["jailbreak"]` → `error.body["content_filters"][0]["content_filter_results"]["jailbreak"]` पुनर्लेखन गर्नुहोस्। `innererror` रैपर हटेको छ; सामग्री फिल्टर विवरणहरू अहिले शीर्ष स्तरको `content_filters` array भित्र छन् र हरेक entry भित्र `content_filter_results` (बहुवचन) छ। |
| `/openai/deployments/.../chat/completions` लाई रॉ HTTP कलले 404 दिन्छ | पुरानो Chat Completions REST एन्डपोइन्ट | URL लाई `/openai/v1/responses` मा पुनर्लेखन गर्नुहोस्। अनुरोध शरीर: `messages` → `input` मा परिवर्तन गर्नुहोस्, `max_output_tokens` + `store: false` थप्नुहोस्, `api-version` क्वेरी प्याराम हटाउनुहोस्। प्रतिक्रिया पार्सिङ परिवर्तन गर्नुहोस्: `choices[0].message.content` → `output[0].content[0].text` (ध्यान दिनुहोस्: `output_text` SDK सुविधा हो, कच्चा REST JSON मा छैन)। |

---

## समस्याहरू हुने कुराहरू

1. यदि पहिले तपाइँले कुराकानी अवस्थाका लागि Chat Completions प्रयोग गर्नु भयो भने, अब आफ्नै अवस्था स्पष्ट रूपमा Responses सँग व्यवस्थापन गर्नुहोस्।
2. पुरानो `max_tokens` भन्दा `max_output_tokens` प्राथमिकता दिनुहोस्।
3. `gpt-5` मा माइग्रेट गर्दा, सुनिश्चित गर्नुहोस् `temperature` निर्दिष्ट गरिएको छैन वा `1` मा सेट गरिएको छ।
4. Chat को `content[].type: "text"` लाई Responses को `content[].type: "input_text"` सँग प्रतिस्थापन गर्नुहोस् प्रयोगकर्ता/प्रणाली इनपुटहरूको लागि।
5. `text.format` का लागि उपयुक्त dict (जस्तै, `{"type": "json_schema", "name": "Output", "schema": ..., "strict": True}`) उपलब्ध गराउनुहोस्, सरल स्ट्रिङ होइन।
6. Responses मा `seed` प्यारामेटर समर्थित छैन; अनुरोधबाट यसलाई हटाउनुहोस्।
7. **तर्क**: केवल तर्क पहिले नै प्रयोग गरेको कोडमा समावेश गर्नुहोस्। जसले तर्क प्रयोग गरेको छैन त्यहाँ API कलमा तर्क थप्नुहोस् नदिनुहोस् — धेरै गैर-तर्क मोडेलहरूले यस प्यारामेटरलाई समर्थन गर्दैनन्।
8. **`max_output_tokens` आकार**: तर्क मोडेलहरू (GPT-5-mini, GPT-5, o-series) का लागि `max_output_tokens=4096` वा माथि प्रयोग गर्नुहोस् — 50–1000 होइन। मोडेलले आउटपुट उत्पन्न गर्नु अघि भित्री तर्क टोकनहरू प्रयोग गर्छ; धेरै कम सिमा खाली वा कटिएको प्रतिक्रिया ल्याउँछ।
9. **O-series `max_completion_tokens`**: यदि मूल कोडले `max_completion_tokens` (o-series का लागि Azure-विशिष्ट) प्रयोग गरेको छ भने, `max_output_tokens` सँग प्रतिस्थापन गर्नुहोस्। Responses API ले `max_completion_tokens` स्वीकार्दैन।
10. **O-series `reasoning_effort`**: यदि मूल कोडले `reasoning_effort` (कम/मध्यम/उच्‍च) प्रयोग गरेको छ भने, यसलाई Responses API कलमा `reasoning={"effort": "<value>"}` मा माइग्रेट गर्नुहोस्।
11. **O-series स्ट्रिमिङ ढिलाइ**: O-series मोडेलहरूले आउटपुट उत्पन्न गर्नु अघि भित्री तर्क गर्छन्। स्ट्रिमिङ गर्दा, पहिलो `response.output_text.delta` इभेन्ट सम्म लामो ढिलाइ अपेक्षा गर्नुहोस्। यो सामान्य हो — मोडेल तर्क गर्दैछ, फसेको होइन।
9. **`_azure_ad_token_provider` हरायो**: `AsyncOpenAI` / `OpenAI` मा `_azure_ad_token_provider` एट्रिब्युट छैन। परीक्षण वा कोड जुन यस एट्रिब्युटलाई पहुँच गर्छ, `AttributeError` ल्याउँछ। टोकन प्रदायक `api_key` को रूपमा पास गरिन्छ र क्लाइन्ट वस्तुमा निरीक्षण गर्न सकिंदैन।
10. **स्न्यापशट / गोल्डेन फाइलहरू**: यदि टेस्ट सूटले स्न्यापशट परीक्षण प्रयोग गर्छ, **सबै** स्न्यापशट फाइलहरू जसमा Chat Completions स्ट्रिमिङ आकृतिहरू (`choices[0]`, `content_filter_results`, `function_call`, आदि) छन्, तिनीहरूलाई नयाँ Responses आकृतिमा अपडेट गर्नुपर्छ। यो सजिलै छुट्न सक्छ र स्न्यापशट परीक्षण विफलतातर्फ लैजान्छ।
11. **मक मंकीप्याच पथ**: मंकीप्याच लक्ष `openai.resources.chat.AsyncCompletions.create` → `openai.resources.responses.AsyncResponses.create` (वा सिंक्रोनसका लागि `Responses.create`) मा परिवर्तन भएको छ। पुरानो पथ प्रयोग गर्दा चुपचाप केही हुँदैन — मॉकले इन्टरसेप्ट गर्दैन र परीक्षणले वास्तविक API मा जान्छ वा असफल हुन्छ।
12. **`input` न कि `messages`**: मॉक फङ्सनहरूले `kwargs.get("input")` पढ्नुपर्नेछ, `kwargs.get("messages")` होइन। Responses API ले कुराकानी इतिहासका लागि `input` प्रयोग गर्छ।
13. **Env var नामाकरण**: Azure Identity SDK ले `ManagedIdentityCredential(client_id=...)` का लागि `AZURE_CLIENT_ID` (नकि `AZURE_OPENAI_CLIENT_ID`) प्रयोग गर्छ। परीक्षणहरू, `.env` फाइलहरू, एप सेटिङ्स र Bicep/इन्फ्रामा यसलाई पुनर्नामाकरण गर्नुहोस्।
14. **`max_output_tokens` न्यूनतम 16 हो**: Azure OpenAI ले 16 भन्दा कम मानलाई `400 integer_below_min_value` सँग अस्वीकार गर्छ। स्मोक टेस्टका लागि 50 र उत्पादनका लागि 1000+ प्रयोग गर्नुहोस्। पुरानो `max_tokens` मा यस्तो न्यूनतम थिएन।
15. **`AzureDeveloperCliCredential` का लागि `tenant_id`**: जब Azure OpenAI स्रोत फरक टेनन्टमा छ भने, तपाइँले `tenant_id` स्पष्ट रूपमा पास गर्नुपर्छ — `AzureDeveloperCliCredential(tenant_id=os.getenv("AZURE_TENANT_ID"))`। यो बिना, क्रेडेन्सियलले चुपचाप गलत टेनन्ट प्रयोग गर्छ र `401` फर्काउँछ।
16. **स्ट्रिमिङमा दर सिमाहरू फरक देखिन्छन्**: Chat Completions सँग 429 प्रायः स्ट्रिम सुरु हुनबाट रोक्थ्यो। Responses API स्ट्रिमिङ सँग, 429 **स्ट्रिमको बीचमै** हुन सक्छ — एसिंक्रोनस इटरेटरले अपवाद फ्याँक्छ। सधैं स्ट्रिमिङ लूपलाई `try/except` मा राख्नुहोस् र त्रुटि JSON लाइन ल्याउनुहोस् ताकि फ्रन्टएण्डले यसलाई सहजै ह्यान्डल गर्न सकोस्।

१७. **वेब अनुप्रयोगहरूको लागि स्ट्रिमिङ त्रुटि ह्यान्डलिङ अनिवार्य छ**: `try: async for event in await coroutine: ... except Exception as e: yield json.dumps({"error": str(e)})` ढाँचा अत्यन्त महत्वपूर्ण छ। यसबिना, SSE/JSONL स्ट्रिमले कुनै पनि सर्भर-साइड त्रुटिमा चुपचाप समाप्त हुन्छ र फ्रन्टएन्ड अड्कन्छ।
१८. **उपकरण परिभाषाहरूले फ्ल्याट ढाँचा प्रयोग गर्नुपर्छ**: Responses API ले `{"type": "function", "name": ..., "parameters": ...}` अपेक्षा गर्दछ — Chat Completions को नेस्टेड `{"type": "function", "function": {"name": ..., "parameters": ...}}` होइन। यो फन्क्सन-कलिङ कोडका लागि सबैभन्दा सामान्य माइग्रेशन त्रुटि हो।
१९. **`pydantic_function_tool()` असंगत छ**: `openai.pydantic_function_tool()` सहायकले अझै पुरानो नेस्टेड ढाँचा उत्पादन गर्दछ। यसलाई `responses.create()` सँग प्रयोग नगर्नुहोस्। उपकरण स्किमाहरू हस्तनिर्मित रूपमा परिभाषित गर्नुहोस् वा आउटपुटलाई फ्ल्याट गर्नुहोस्।
२०. **उपकरण परिणामहरू `function_call_output` प्रयोग गर्छन्, `role: tool` होइन**: उपकरण सञ्चालन गरेपछि `{"type": "function_call_output", "call_id": ..., "output": ...}` थप्नुहोस् — `{"role": "tool", "tool_call_id": ..., "content": ...}` होइन। सहायकको उपकरण अनुरोधको लागि, `messages.extend(response.output)` प्रयोग गर्नुहोस् — म्यानुअल `{"role": "assistant", "tool_calls": [...]}` डिक्सनरी होइन।
२१. **`strict: true` लाई `required` + `additionalProperties: false` चाहिन्छ**: उपकरणमा `strict: true` प्रयोग गर्दा, हरेक गुण `required` एर्रेमा सूचीबद्घ हुनुपर्छ र `additionalProperties` लाई `false` हुनुपर्छ। एउटासमेत हराएमा ४०० त्रुटि आउँछ।
२२. **फन्क्सन कल ID हरूलाई निश्चित उपसर्गहरू हुन्छन्**: `input` मा केही शटका `function_call` वस्तुहरू उपलब्ध गराउँदा, `id` फिल्ड `fc_` बाट सुरु हुनुपर्छ र `call_id` फिल्ड `call_` बाट सुरु हुनुपर्छ (जस्तै, `"id": "fc_example1", "call_id": "call_example1"`). पुरानो Chat Completions को `id` मा `call_` उपसर्ग प्रयोग गर्न अस्वीकृत हुन्छ।
२३. **GitHub मोडेलहरूले Responses API समर्थन गर्दैनन्**: अनुप्रयोगमा GitHub Models कोड पथ (`base_url` जसले `models.github.ai` वा `models.inference.ai.azure.com` तर्फ संकेत गर्दछ) भएमा, यसलाई पूर्ण रूपमा हटाउनुपर्छ। कुनै माइग्रेशन पथ छैन — Azure OpenAI, OpenAI, वा उपयुक्त स्थानीय अन्तबिन्दुमा स्विच गर्नुहोस्।
२४. **सामग्री फिल्टर त्रुटिको बडी संरचनामा परिवर्तन भयो**: Chat Completions त्रुटिहरूले `error.body["innererror"]["content_filter_result"]` (एकवचन) प्रयोग गर्थे। Responses API त्रुटिहरूले `error.body["content_filters"][0]["content_filter_results"]` (बहुवचन, एर्रे भित्र) उपयोग गर्छ। `innererror` कुञ्जी अब छैन। जुन कोडले सिधै `innererror` पहुँच गर्छ, Runtime मा `KeyError` ल्याउँछ — यो माइग्रेशनमा सजिलै छुट्न सक्छ किनकि यो मात्र तब देखा पर्छ जब सामग्री फिल्टर साँच्चै सक्रिय हुन्छ। माइग्रेशन गर्दा सधैं `innererror` का लागि grep गर्नुहोस्।
२५. **कच्चा HTTP कलहरूलाई URL + बडी पुनर्लेखन आवश्यक छ**: Azure OpenAI REST सिधै कल गर्ने अनुप्रयोगहरूले (जस्तै `requests`, `httpx`, `aiohttp` बाट) `/openai/deployments/{name}/chat/completions?api-version=...` बाट `/openai/v1/responses` मा स्विच गर्नुपर्छ। अनुरोध बडीले `messages` को सट्टा `input` प्रयोग गर्दछ, `max_output_tokens` र `store` आवश्यक छ, र `api-version` क्वेरी प्यारामिटर हटाइन्छ। प्रतिक्रिया बडी टेक्स्ट `output[0].content[0].text` मा छ — **`output_text` होइन**, जुन SDK सुविधा हो र कच्चा REST JSON मा उपलब्ध छैन।

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**अस्वीकरण**:
यो दस्तावेज़ AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) प्रयोग गरेर अनुवाद गरिएको हो। हामी सही हुन प्रयास गर्छौं, तर कृपया जानकार हुनुस् कि स्वचालित अनुवादमा त्रुटिहरू वा अशुद्धताहरू हुन सक्छन्। मूल दस्तावेज़ यसको मूल भाषामा आधिकारिक स्रोत मानिनुपर्छ। महत्वपूर्ण जानकारीका लागि व्यावसायिक मानव अनुवाद सिफारिस गरिन्छ। यस अनुवादको प्रयोगबाट उत्पन्न कुनै पनि गलत बुझाइ वा त्रुटिको लागि हामी जिम्मेवार छैनौं।
<!-- CO-OP TRANSLATOR DISCLAIMER END -->