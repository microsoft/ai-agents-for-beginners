# समस्या निवारण, जोखिम तालिका और सावधानियां

## 400 त्रुटियों की समस्या निवारण

| त्रुटि | सुधार |
|-------|-----|
| `missing_required_parameter: tools[0].name` | टूल परिभाषा पुरानी चैट पूर्णता नेस्टेड फ़ॉर्मेट का उपयोग करती है | इसे `{"type": "function", "function": {"name": ...}}` से `{"type": "function", "name": ..., "parameters": ...}` में फ्लैट करें — नाम, विवरण, पैरामीटर शीर्ष स्तर पर हों |
| `unknown_parameter: input[N].tool_calls` | मल्टी-टर्न टूल परिणाम पुरानी चैट पूर्णता फ़ॉर्मेट का उपयोग करते हैं | `{"role": "assistant", "tool_calls": [...]}` + `{"role": "tool", ...}` को `response.output` आइटम्स + `{"type": "function_call_output", "call_id": ..., "output": ...}` से बदलें |
| `invalid_function_parameters: 'required' is required` | `strict: true` टूल में `required` ऐरे नहीं है | जब `strict: true` हो, तो सभी गुण `required` में सूचीबद्ध होना चाहिए और `additionalProperties: false` सेट करना चाहिए |
| `invalid_function_parameters: 'additionalProperties' is required` | `strict: true` टूल में `additionalProperties: false` नहीं है | पैरामीटर ऑब्जेक्ट में `"additionalProperties": false` जोड़ें |
| `invalid input[N].id: Expected an ID that begins with 'fc'` | फ्यू-शॉट function_call ID का गलत उपसर्ग | फ़ंक्शन कॉल ID `fc_` से शुरू होना चाहिए (जैसे, `fc_example1`), न कि `call_` से |
| `missing_required_parameter: text.format.name` | फार्मेट डिक्ट में `"name"` कुंजी जोड़ें (जैसे, `"name": "Output"`) |
| `invalid_type: text.format` | सुनिश्चित करें कि `text.format` एक डिक्ट है जिसमें `type`, `name`, `strict`, `schema` कीज़ हों — स्ट्रिंग नहीं |
| `invalid input content type` | चैट `text` की बजाय `input_text`/`output_text` कंटेंट प्रकारों का उपयोग करें |
| `invalid input content type` (छवि) | इमेज कंटेंट अभी भी `"type": "image_url"` उपयोग करता है | इसे `"type": "input_image"` में बदलें |
| `Expected object, got string` on `image_url` | `image_url` अभी भी नेस्टेड ऑब्जेक्ट `{"url": "..."}` है | इसे सीधे स्ट्रिंग में फ्लैट करें: `"image_url": "https://..."` या `"image_url": "data:image/...;base64,..."` |
| `integer below minimum value` for `max_output_tokens` | Azure OpenAI पर न्यूनतम **16** है। टेस्ट के लिए 50+ और प्रोडक्शन के लिए 1000+ उपयोग करें। |
| `429 Too Many Requests` स्ट्रीमिंग के दौरान | दर-सीमा सीमित। स्ट्रीमिंग को `try/except` में लपेटें, त्रुटि JSON फ्रंटेंड को दें, बैकऑफ/रिट्राई लागू करें। |
| `KeyError: 'innererror'` कंटेंट फ़िल्टर त्रुटि पर | Responses API में कंटेंट फ़िल्टर त्रुटि बॉडी संरचना बदल गई | चैट पूर्णताओं में `error.body["innererror"]["content_filter_result"]`; Responses API में `error.body["content_filters"][0]["content_filter_results"]` (बहुवचन, एक ऐरे के अंदर) होता है। सभी `innererror` एक्सेस पुनः लिखें। |

---

## माइग्रेशन जोखिम तालिका

| लक्षण | संभावित गलती | सुधार |
|---------|---------------|-----|
| खाली `output_text` / कटौती किया गया उत्तर | reasoning मॉडल के लिए `max_output_tokens` बहुत कम है | `max_output_tokens=1000` या अधिक सेट करें — reasoning टोकन लिमिट में गिने जाते हैं |
| `400 invalid_type: text.format` | `text.format` डिक्ट के बजाय `response_format` स्ट्रिंग पास किया गया | `text={"format": {"type": "json_schema", "name": "...", "strict": True, "schema": {...}}}` का उपयोग करें |
| `/openai/v1/responses` पर `404 Not Found` | गलत `base_url` — `/openai/v1/` उपसर्ग गायब है | सुनिश्चित करें `base_url=f"{endpoint}/openai/v1/"` (ट्रेलिंग स्लैश के साथ) |
| `OpenAI()` में स्विच करने पर `401 Unauthorized` | `api_key` सेट नहीं है या टोकन प्रदाता सही तरीके से पास नहीं किया गया | EntraID के लिए: `api_key=token_provider` (callable). API की के लिए: `api_key=os.environ["AZURE_OPENAI_API_KEY"]` |
| मॉडल `deployment not found` लौटाता है | `model` पैरामीटर Azure डिप्लॉयमेंट नाम से मेल नहीं खाता | `model=os.environ["AZURE_OPENAI_DEPLOYMENT"]` का उपयोग करें — यह मॉडल नाम नहीं, डिप्लॉयमेंट नाम है |
| `json.loads(resp.output_text)` `JSONDecodeError` फेंकता है | स्कीमा लागू नहीं है या मॉडल स्ट्रिक्ट JSON समर्थित नहीं है | स्कीमा में `"strict": True` सुनिश्चित करें, और जांचें कि मॉडल संरचित आउटपुट समर्थित है |
| स्ट्रीमिंग कोई `delta` इवेंट नहीं देता | गलत इवेंट प्रकार जांच रहे हैं | `event.type == "response.output_text.delta"` पर फ़िल्टर करें, न कि चैट के `chat.completion.chunk` पर |
| माइग्रेशन के बाद इमेज इनपुट पर `400` त्रुटि | इमेज कंटेंट टाइप अपडेट नहीं किया गया | `"type": "image_url"` → `"type": "input_image"` में बदलें और `"image_url": {"url": "..."}` → `"image_url": "..."` (साधारण स्ट्रिंग) फ्लैट करें |
| टूल कॉल अनंत लूप में फंसा हुआ | फॉलो-अप `input` में टूल परिणाम गायब है | टूल चलाने के बाद, अगले रिक्वेस्ट के `input` में `{"type": "function_call_output", "call_id": ..., "output": ...}` आइटम जोड़ें |
| GPT-5 या o-सीरीज के साथ `temperature` त्रुटि | 1 के अलावा कोई स्पष्ट `temperature` मान | GPT-5 और o-सीरीज मॉडल (o1, o3-mini, o3, o4-mini) के लिए `temperature` हटाएं या इसे `1` पर सेट करें |
| o-सीरीज के साथ `top_p` त्रुटि | `top_p` समर्थित नहीं है | o-सीरीज मॉडल लक्ष्यित करते समय `top_p` हटाएं |
| `max_completion_tokens` मान्यता प्राप्त नहीं | Azure-विशिष्ट पैरामीटर उपयोग किया गया | `max_completion_tokens` को `max_output_tokens` से बदलें। o-सीरीज के लिए इसे 4096+ पर सेट करें (reasoning टोकन लिमिट में गिने जाते हैं)। |
| o-सीरीज से खाली/कटे हुए आउटपुट | `max_output_tokens` बहुत कम है | o-सीरीज आंतरिक रूप से reasoning टोकन उपयोग करता है। `max_output_tokens=4096` या उससे अधिक सेट करें — 500–1000 नहीं। |
| `400 integer_below_min_value` `max_output_tokens` के लिए | मान 16 से कम है | Azure OpenAI `max_output_tokens >= 16` लागू करता है। स्मोक टेस्ट के लिए 50+ और उत्पादन के लिए 1000+ का उपयोग करें। |
| स्ट्रीम के बीच में `429 Too Many Requests` | Azure OpenAI द्वारा दर-सीमा सीमित | स्ट्रीम चुपचाप टूट जाता है बिना त्रुटि हैंडलिंग के। हमेशा `async for event in await coroutine:` को `try/except` में लपेटें और फ्रंटेंड को `{"error": str(e)}` दें। |
| `AzureDeveloperCliCredential` → `CredentialUnavailableError` | गलत टेनेंट या लॉगिन नहीं है | `tenant_id=os.getenv("AZURE_TENANT_ID")` स्पष्ट रूप से पास करें। लोकली `azd auth login --tenant <tenant-id>` चलाएं। |
| GitHub मॉडल (`models.github.ai`) उपयोग करते समय `404 Not Found` | GitHub मॉडल Responses API का समर्थन नहीं करते | GitHub मॉडल कोड पथ पूरी तरह हटा दें। Azure OpenAI, OpenAI, या संगत लोकल एंडपॉइंट (जैसे Ollama with Responses support) का उपयोग करें। |
| MAF `OpenAIChatCompletionClient` अभी भी Chat Completions उपयोग कर रहा है | 1.0.0+ में लेगेसी MAF क्लाइंट का उपयोग | MAF 1.0.0+ में, `OpenAIChatClient` डिफ़ॉल्ट रूप से Responses API उपयोग करता है। `OpenAIChatCompletionClient` को `OpenAIChatClient` से बदलें। 1.0.0 से पहले के लिए, एजेंट-फ्रेमवर्क को अपग्रेड करें: `agent-framework-openai>=1.0.0`। |
| LangChain एजेंट टूल कॉल के साथ खाली या विफल होता है | `ChatOpenAI` Responses API का उपयोग नहीं कर रहा | `ChatOpenAI(...)` में `use_responses_api=True` जोड़ें। साथ ही, प्रतिक्रिया संदेशों में `.content` → `.text` करें। |
| कंटेंट फ़िल्टर त्रुटि हैंडलर में `KeyError: 'innererror'` | Responses API में त्रुटि बॉडी संरचना बदल गई | `error.body["innererror"]["content_filter_result"]["jailbreak"]` को बदलकर `error.body["content_filters"][0]["content_filter_results"]["jailbreak"]` करें। `innererror` रैपर हट चुका है; कंटेंट फ़िल्टर विवरण अब शीर्ष-स्तरीय `content_filters` ऐरे में हैं, जिसमें प्रत्येक प्रविष्टि के अंदर `content_filter_results` (बहुवचन) हैं। |
| `/openai/deployments/.../chat/completions` पर रॉ HTTP कॉल 404 लौटाता है | पुराना चैट पूर्णता REST एंडपॉइंट | URL को `/openai/v1/responses` में पुनः लिखें। रिक्वेस्ट बॉडी बदलें: `messages` → `input`, `max_output_tokens` + `store: false` जोड़ें, `api-version` क्वेरी पैरामीटर हटा दें। प्रतिक्रिया पार्सिंग बदलें: `choices[0].message.content` → `output[0].content[0].text` (ध्यान दें: `output_text` SDK सुविधा संपत्ति है, कच्चे REST JSON में नहीं)। |

---

## सावधानियां

1. यदि आपने पहले चैट पूर्णताओं का उपयोग किया था, तो बातचीत की स्थिति का प्रबंधन स्पष्ट रूप से Responses के साथ करें।
2. पुरानी `max_tokens` के बजाय `max_output_tokens` पसंद करें।
3. `gpt-5` पर माइग्रेट करते समय सुनिश्चित करें कि `temperature` निर्दिष्ट न हो या `1` पर सेट हो।
4. चैट `content[].type: "text"` को Responses में `content[].type: "input_text"` से बदलें (उपयोगकर्ता/सिस्टम इनपुट के लिए)।
5. `text.format` के लिए एक उचित डिक्ट दें (जैसे, `{"type": "json_schema", "name": "Output", "schema": ..., "strict": True}`), साधारण स्ट्रिंग नहीं।
6. Responses में `seed` पैरामीटर समर्थित नहीं है; इसे रिक्वेस्ट से हटा दें।
7. **Reasoning**: केवल तब reasoning शामिल करें जब मूल कोड पहले से इसका उपयोग करता हो। उन API कॉल्स में reasoning न जोड़ें जिनमें यह नहीं था — कई गैर-reasoning मॉडल इस पैरामीटर का समर्थन नहीं करते।
8. **`max_output_tokens` आकार**: reasoning मॉडल (GPT-5-mini, GPT-5, o-सीरीज) के लिए `max_output_tokens=4096` या अधिक उपयोग करें — 50–1000 नहीं। मॉडल दृश्यमान आउटपुट उत्पन्न करने से पहले आंतरिक रूप से reasoning टोकन का उपयोग करता है; बहुत कम लिमिट कटे या खाली उत्तर देती है।
9. **O-सीरीज `max_completion_tokens`**: यदि मूल कोड ने `max_completion_tokens` (o-सीरीज के लिए Azure-विशिष्ट) उपयोग किया, तो इसे `max_output_tokens` से बदलें। Responses API `max_completion_tokens` स्वीकार नहीं करता।
10. **O-सीरीज `reasoning_effort`**: यदि मूल कोड `reasoning_effort` (low/medium/high) उपयोग करता है, तो इसे Responses API कॉल में `reasoning={"effort": "<value>"}` में माइग्रेट करें।
11. **O-सीरीज स्ट्रीमिंग देरी**: O-सीरीज मॉडल आउटपुट उत्पन्न करने से पहले आंतरिक reasoning करता है। स्ट्रीमिंग के समय, पहले `response.output_text.delta` इवेंट से पहले लंबी देरी की उम्मीद करें। यह सामान्य है — मॉडल reasoning कर रहा है, फंस नहीं गया है।
9. **`_azure_ad_token_provider` अब नहीं है**: `AsyncOpenAI` / `OpenAI` में `_azure_ad_token_provider` गुण नहीं है। इस गुण को एक्सेस करने वाले टेस्ट या कोड `AttributeError` फेंकेंगे। टोकन प्रदाता `api_key` के रूप में पास किया जाता है और क्लाइंट ऑब्जेक्ट पर निरीक्षणीय नहीं है।
10. **Snapshot / गोल्डन फ़ाइलें**: यदि टेस्ट सूट स्नैपशॉट टेस्टिंग का उपयोग करता है, तो सभी स्नैपशॉट फ़ाइलें जो चैट पूर्णताओं स्ट्रीमिंग शेप्स (`choices[0]`, `content_filter_results`, `function_call`, आदि) शामिल करती हैं, उन्हें नए Responses शेप के साथ अपडेट किया जाना चाहिए। यह मिस करना आसान है और स्नैपशॉट असर्शन विफलताओं का कारण बनता है।
11. **मॉक मंकीपैच पाथ**: मंकीपैच लक्ष्य `openai.resources.chat.AsyncCompletions.create` से बदलकर `openai.resources.responses.AsyncResponses.create` (या सिंक के लिए `Responses.create`) हो गया है। पुराने पाथ का उपयोग चुपचाप कुछ नहीं करता — मॉक इंटरसेप्ट नहीं करेगा, और टेस्ट असली API का उपयोग करेंगे या विफल होंगे।
12. **`input` न कि `messages`**: मॉक फ़ंक्शन्स को `kwargs.get("input")` पढ़ना चाहिए, न कि `kwargs.get("messages")`। Responses API बातचीत इतिहास के लिए `input` उपयोग करता है।
13. **पर्यावरण वेरिएबल नामकरण**: Azure Identity SDK `ManagedIdentityCredential(client_id=...)` के लिए `AZURE_CLIENT_ID` (न कि `AZURE_OPENAI_CLIENT_ID`) उपयोग करता है। टेस्ट, `.env` फ़ाइलें, ऐप सेटिंग्स, और बाइसेप/इन्फ्रा में नाम बदलें।
14. **`max_output_tokens` न्यूनतम 16 है**: Azure OpenAI 16 से कम मानों को `400 integer_below_min_value` के साथ अस्वीकृत करता है। स्मोक टेस्ट के लिए `50` और प्रोडक्शन के लिए 1000+ का उपयोग करें। पुराने `max_tokens` में ऐसी न्यूनतम सीमा नहीं थी।
15. **`AzureDeveloperCliCredential` के लिए `tenant_id`**: जब Azure OpenAI रिसोर्स अलग टेनेंट में हो, तो `tenant_id` स्पष्ट रूप से पास करना **जरूरी** है — `AzureDeveloperCliCredential(tenant_id=os.getenv("AZURE_TENANT_ID"))`। इसके बिना, क्रेडेंशियल चुपचाप गलत टेनेंट का उपयोग करता है और `401` लौटाता है।
16. **स्ट्रीमिंग में दर-सीमा अलग-अलग रूप में आती है**: चैट पूर्णताओं के साथ, 429 आमतौर पर स्ट्रीम शुरू होने से रोकता था। Responses API स्ट्रीमिंग के साथ, 429 **मध्य स्ट्रीम** हो सकता है — असिंक इटरेटर एक अपवाद उठाएगा। हमेशा स्ट्रीमिंग लूप को `try/except` में लपेटें और त्रुटि JSON लाइन फ्रंटेंड को लौटाएं ताकि वह इसे आसानी से संभाल सके।

17. **वेब ऐप्स के लिए स्ट्रीमिंग त्रुटि हैंडलिंग अनिवार्य है**: `try: async for event in await coroutine: ... except Exception as e: yield json.dumps({"error": str(e)})` पैटर्न महत्वपूर्ण है। इसके बिना, कोई भी सर्वर-साइड त्रुटि पर SSE/JSONL स्ट्रीम चुपचाप खत्म हो जाती है और फ्रंटेंड अटक जाता है।
18. **टूल परिभाषाओं को फ्लैट फॉर्मेट में उपयोग करना चाहिए**: Responses API अपेक्षा करता है `{"type": "function", "name": ..., "parameters": ...}` — न कि Chat Completions के नेस्टेड `{"type": "function", "function": {"name": ..., "parameters": ...}}`। यह फंक्शन-कॉलिंग कोड के लिए सबसे सामान्य माइग्रेशन त्रुटि है।
19. **`pydantic_function_tool()` असंगत है**: `openai.pydantic_function_tool()` हेल्पर अभी भी पुराना नेस्टेड फॉर्मेट उत्पन्न करता है। इसे `responses.create()` के साथ उपयोग न करें। टूल स्कीमाओं को मैनुअल रूप से परिभाषित करें या आउटपुट को फ्लैटन करें।
20. **टूल परिणाम `function_call_output` का उपयोग करते हैं, न कि `role: tool`**: टूल निष्पादित करने के बाद, `{"type": "function_call_output", "call_id": ..., "output": ...}` जोड़ें — न कि `{"role": "tool", "tool_call_id": ..., "content": ...}`। सहायक के टूल अनुरोध के लिए, `messages.extend(response.output)` का उपयोग करें — न कि मैनुअल `{"role": "assistant", "tool_calls": [...]}` डिक्ट।
21. **`strict: true` के लिए `required` + `additionalProperties: false` आवश्यक हैं**: जब टूल पर `strict: true` का उपयोग किया जाता है, तो हर प्रॉपर्टी को `required` एरे में सूचीबद्ध किया जाना चाहिए और `additionalProperties` `false` होना चाहिए। इनमें से कोई भी नहीं होने पर 400 त्रुटि होती है।
22. **फंक्शन कॉल आईडी के विशिष्ट उपसर्ग होते हैं**: जब `input` में फ्यू-शॉट `function_call` आइटम प्रदान किए जाते हैं, तो `id` फ़ील्ड को `fc_` से शुरू होना चाहिए और `call_id` फ़ील्ड को `call_` से (उदा., `"id": "fc_example1", "call_id": "call_example1"`). पुराने Chat Completions के लिए `id` में `call_` उपसर्ग अस्वीकृत किया जाता है।
23. **GitHub Models Responses API का समर्थन नहीं करता**: यदि ऐप में GitHub Models कोड पथ (`base_url` जो `models.github.ai` या `models.inference.ai.azure.com` की ओर इशारा करता है) है, तो इसे पूरी तरह से हटा दें। कोई माइग्रेशन पथ नहीं है — Azure OpenAI, OpenAI, या संगत स्थानीय एंडपॉइंट पर स्विच करें।
24. **सामग्री फ़िल्टर त्रुटि बॉडी संरचना बदल गई है**: Chat Completions त्रुटियां उपयोग करती थीं `error.body["innererror"]["content_filter_result"]` (एकवचन)। Responses API त्रुटियां उपयोग करती हैं `error.body["content_filters"][0]["content_filter_results"]` (बहुवचन, एक एरे के अंदर)। `innererror` कुंजी अब मौजूद नहीं है। जो भी कोड सीधे `innererror` एक्सेस करता है वह रनटाइम पर `KeyError` उठाएगा — यह माइग्रेशन में पकड़े जाने में आसान नहीं है क्योंकि यह केवल तभी सतह पर आता है जब सामग्री फ़िल्टर वास्तव में ट्रिगर होता है। माइग्रेशन के दौरान हमेशा `innererror` के लिए ग्रेप करें।
25. **रॉ HTTP कॉल के लिए URL + बॉडी पुनर्लेखन आवश्यक है**: Azure OpenAI REST को सीधे कॉल करने वाले ऐप्स (जैसे `requests`, `httpx`, `aiohttp` के माध्यम से) जो `/openai/deployments/{name}/chat/completions?api-version=...` का उपयोग करते हैं, उन्हें `/openai/v1/responses` पर स्विच करना होगा। रिक्वेस्ट बॉडी में `messages` के बजाय `input` उपयोग होता है, `max_output_tokens` और `store` आवश्यक हैं, और `api-version` क्वेरी पैरामीटर छोड़ दिया जाता है। प्रतिक्रिया बॉडी पाठ `output[0].content[0].text` पर होता है — **न कि** `output_text`, जो कि SDK की एक सुविधा संपत्ति है और कच्चे REST JSON में मौजूद नहीं है।

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**अस्वीकरण**:
इस दस्तावेज़ का अनुवाद AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) का उपयोग करके किया गया है। जबकि हम सटीकता के लिए प्रयास करते हैं, कृपया ध्यान दें कि स्वचालित अनुवादों में त्रुटियाँ या अशुद्धियाँ हो सकती हैं। मूल दस्तावेज़ अपनी मूल भाषा में ही प्रामाणिक स्रोत माना जाना चाहिए। महत्वपूर्ण जानकारी के लिए, पेशेवर मानव अनुवाद की सिफारिश की जाती है। इस अनुवाद के उपयोग से उत्पन्न किसी भी गलतफहमी या गलत व्याख्या के लिए हम उत्तरदायी नहीं हैं।
<!-- CO-OP TRANSLATOR DISCLAIMER END -->