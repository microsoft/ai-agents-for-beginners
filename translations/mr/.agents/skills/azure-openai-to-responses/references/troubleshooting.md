# समस्या निवारण, जोखीम तक्ता आणि Gotchas

## 400s समस्या निवारण

| त्रुटी | निराकरण |
|-------|-----|
| `missing_required_parameter: tools[0].name` | टूल व्याख्या जुन्या Chat Completions नेस्टेड फॉरमॅटचा वापर करते | `{"type": "function", "function": {"name": ...}}` कडून `{"type": "function", "name": ..., "parameters": ...}` मध्ये फ्लॅटन करा — नाव, वर्णन, पॅरामीटर्स वरच्या स्तरावर असावेत |
| `unknown_parameter: input[N].tool_calls` | मल्टि-टर्न टूल परिणाम जुन्या Chat Completions फॉरमॅटचा वापर करतात | `{"role": "assistant", "tool_calls": [...]}` + `{"role": "tool", ...}` याऐवजी `response.output` आयटम + `{"type": "function_call_output", "call_id": ..., "output": ...}` वापरा |
| `invalid_function_parameters: 'required' is required` | `strict: true` टूलमध्ये `required` अ‍ॅरे गहाळ आहे | जेव्हा `strict: true` असते, तेव्हा सर्व प्रॉपर्टीज `required` मध्ये असाव्यात आणि `additionalProperties: false` सेट केले पाहिजे |
| `invalid_function_parameters: 'additionalProperties' is required` | `strict: true` टूलमध्ये `additionalProperties: false` गहाळ आहे | पॅरामीटर्स ऑब्जेक्टमध्ये `"additionalProperties": false` जोडा |
| `invalid input[N].id: Expected an ID that begins with 'fc'` | फ्यू-शॉट function_call आयडीचे प्रीफिक्स चुकीचे आहे | फंक्शन कॉल आयडी `fc_` ने सुरू होणे आवश्यक आहे (उदा. `fc_example1`), `call_` नव्हे |
| `missing_required_parameter: text.format.name` | फॉरमॅट डिक्टमध्ये `"name"` की जोडा (उदा., `"name": "Output"`) |
| `invalid_type: text.format` | `text.format` हे स्ट्रिंग न करता `type`, `name`, `strict`, `schema` या कीजसह डिक्शनरी असणे सुनिश्चित करा |
| `invalid input content type` | Chat `text` ऐवजी `input_text`/`output_text` कंटेंट प्रकार वापरा |
| `invalid input content type` (image) | इमेज कंटेंट अजूनही `"type": "image_url"` वापरतो | `"type": "input_image"` मध्ये बदला |
| `Expected object, got string` on `image_url` | `image_url` अजूनही नेस्टेड ऑब्जेक्ट `{"url": "..."}` आहे | साध्या स्ट्रिंगमध्ये फ्लॅटन करा: `"image_url": "https://..."` किंवा `"image_url": "data:image/...;base64,..."` |
| `integer below minimum value` for `max_output_tokens` | Azure OpenAI वर किमान 16 आहे. चाचणीसाठी 50+, उत्पादनासाठी 1000+ वापरा. |
| `429 Too Many Requests` स्ट्रीमिंग दरम्यान | रेट लिमिट लागले आहे. स्ट्रीमिंग `try/except` मध्ये लपेटा, चुका JSON फ्रंटेंडला द्या, बॅकऑफ/रिट्री लागू करा. |
| `KeyError: 'innererror'` कंटेंट फिल्टर त्रुटीवर | Responses API मध्ये कंटेंट फिल्टर त्रुटी शरीराची रचना बदलली आहे | Chat Completions मध्ये `error.body["innererror"]["content_filter_result"]`; Responses API मध्ये `error.body["content_filters"][0]["content_filter_results"]` (बहुवचन, अर्रेमध्ये) वापरा. सर्व `innererror` प्रवेश पुन्हा लिहा. |

---

## माइग्रेशन जोखीम तक्ता

| लक्षण | शक्य ती चूक | निराकरण |
|---------|---------------|-----|
| रिकामा `output_text` / त्रुटीपूर्ण प्रतिसाद | reasoning मॉडेलसाठी `max_output_tokens` खूप कमी | `max_output_tokens=1000` किंवा अधिक सेट करा — reasoning टोकन्स मर्यादेबाहेर गिनले जातात |
| `400 invalid_type: text.format` | `response_format` स्ट्रिंग पाठवली आहे, `text.format` डिक्ट नाही | `text={"format": {"type": "json_schema", "name": "...", "strict": True, "schema": {...}}}` वापरा |
| `/openai/v1/responses` वर `404 Not Found` | चुकीचा `base_url` — `/openai/v1/` सुफिक्स गहाळ आहे | सुनिश्चित करा `base_url=f"{endpoint}/openai/v1/"` (ट्रेलिंग स्लॅशसह) |
| `OpenAI()` वर स्विच करून `401 Unauthorized` | `api_key` सेट नाही किंवा टोकन पुरवठादार चुकीने पास केला आहे | EntraID साठी: `api_key=token_provider` (कॉलेबल). API कीसाठी: `api_key=os.environ["AZURE_OPENAI_API_KEY"]` |
| मॉडेल `deployment not found` परत देते | `model` पॅरामीटर तुमच्या Azure तैनाती नावाशी जुळत नाही | `model=os.environ["AZURE_OPENAI_DEPLOYMENT"]` वापरा — हे तैनाती नाव आहे, मॉडेल नाव नाही |
| `json.loads(resp.output_text)` मध्ये `JSONDecodeError` उगमित | Schema लागू नाही किंवा मॉडेल स्ट्रिक्ट JSON समर्थन करत नाही | स्कीमामध्ये `"strict": True` सुनिश्चित करा आणि मॉडेल स्ट्रक्चर्ड आउटपुटला सपोर्ट करते का तपासा |
| स्ट्रीमिंग `delta` इव्हेंट नाही मिळवत | चुकीचा इव्हेंट प्रकार तपासत आहे | Chat च्या `chat.completion.chunk` ऐवजी `event.type == "response.output_text.delta"` फिल्टर करा |
| माइग्रेशननंतर इमेज इनपुटवर `400` त्रुटी | इमेज कंटेंट प्रकार अद्यतनित नाही | `"type": "image_url"` → `"type": "input_image"` करा आणि `"image_url": {"url": "..."}` → `"image_url": "..."` (साधी स्ट्रिंग) करा |
| टूल कॉल अनंत वेळा लूप होते | फॉलो-अप `input` मध्ये टूल निकाल गहाळ आहे | टूल अंमलबजावणी नंतर, पुढील विनंतीमध्ये `input` मध्ये `{"type": "function_call_output", "call_id": ..., "output": ...}` आयटम जोडा |
| GPT-5 किंवा o-series सोबत `temperature` त्रुटी | स्पष्ट `temperature` मूल्य 1 शिवाय | GPT-5 आणि o-series मॉडेलसाठी (o1, o3-mini, o3, o4-mini) `temperature` काढा किंवा 1 सेट करा |
| o-series सोबत `top_p` त्रुटी | `top_p` समर्थित नाही | o-series मॉडेल्ससाठी `top_p` काढा |
| `max_completion_tokens` ओळखले जात नाही | Azure-स्पेशिफिक पॅरामीटर वापरला जातो | `max_completion_tokens` ऐवजी `max_output_tokens` वापरा. o-series साठी 4096+ सेट करा (reasoning टोकन्स मर्यादेबाहेर गिनले जातात). |
| o-series कडून रिकामा/त्रुटीपूर्ण आउटपुट | `max_output_tokens` खूप कमी | o-series अंतर्गत reasoning टोकन्स वापरतो. `max_output_tokens=4096` किंवा अधिक सेट करा — 500–1000 नव्हे. |
| `400 integer_below_min_value` for `max_output_tokens` | मूल्य 16 पेक्षा खाली | Azure OpenAI मध्ये `max_output_tokens >= 16` आवश्यक आहे. स्मोक टेस्टसाठी 50+, उत्पादनासाठी 1000+ वापरा. |
| स्ट्रीममध्ये मध्यभागी `429 Too Many Requests` | Azure OpenAI ने रेट लिमिट लावले आहे | स्ट्रीम त्रुटी हाताळणीशिवाय गुप्तपणे तुटतो. सदैव `async for event in await coroutine:` `try/except` मध्ये लपेटा आणि `{"error": str(e)}` फ्रंटेंडला द्या. |
| `AzureDeveloperCliCredential` → `CredentialUnavailableError` | चुकीचा टेनंट किंवा लॉगिन नाही | `tenant_id=os.getenv("AZURE_TENANT_ID")` स्पष्टपणे पास करा. स्थानिकरित्या `azd auth login --tenant <tenant-id>` चालवा. |
| GitHub Models (`models.github.ai`) वापरताना `404 Not Found` | GitHub Models Responses API समर्थन करत नाही | GitHub Models कोड मार्ग पूर्णपणे काढून टाका. Azure OpenAI, OpenAI किंवा अनुकूल स्थानिक एंडपॉइंट वापरा (उदा. Ollama with Responses support). |
| MAF `OpenAIChatCompletionClient` अजूनही Chat Completions वापरत आहे | 1.0.0+ मध्ये जुना MAF क्लायंट वापरला जातो | MAF 1.0.0+ मध्ये, `OpenAIChatClient` डिफॉल्टने Responses API वापरतो. `OpenAIChatCompletionClient` चे स्थान `OpenAIChatClient` ने भरा. प्री-1.0.0 साठी `agent-framework-openai>=1.0.0` वर अपग्रेड करा. |
| LangChain एजंट रिकामा परत करतो किंवा टूल कॉल्ससह अयशस्वी होतो | `ChatOpenAI` Responses API वापरत नाही | `ChatOpenAI(...)` मध्ये `use_responses_api=True` जोडा. तसेच प्रतिसाद संदेशांवर `.content` → `.text` बदला. |
| कंटेंट फिल्टर त्रुटी हँडलरमध्ये `KeyError: 'innererror'` | Responses API मध्ये त्रुटी बॉडी रचना बदलली | `error.body["innererror"]["content_filter_result"]["jailbreak"]` → `error.body["content_filters"][0]["content_filter_results"]["jailbreak"]` पुन्हा लिहा. `innererror` काढला गेला आहे; कंटेंट फिल्टर तपशील आता शीर्ष-स्तर `content_filters` अर्रे मध्ये आहेत जेथे `content_filter_results` (बहुवचन) प्रत्येक नोंदीत आहे. |
| `/openai/deployments/.../chat/completions` कडे थेट HTTP कॉल 404 परत करतो | जुना Chat Completions REST एंडपॉइंट | URL `/openai/v1/responses` मध्ये पुन्हा लिहा. विनंती बॉडी: `messages` → `input`, `max_output_tokens` + `store: false` जोडा, `api-version` क्वेरी पॅरामीटर काढा. प्रतिसाद पार्सिंग: `choices[0].message.content` → `output[0].content[0].text` बदला (टीप: `output_text` हा SDK सोयीसाठीचा प्रॉपर्टी आहे, थेट REST JSON मध्ये नाही). |

---

## Gotchas

1. जर तुम्ही पूर्वी Chat Completions संभाषण स्थितीसाठी वापरला असेल, तर Responses सह स्वतःची स्थिती स्पष्टपणे व्यवस्थापित करा.
2. पारंपरिक `max_tokens` च्या ऐवजी `max_output_tokens` प्राधान्य द्या.
3. `gpt-5` कडे माइग्रेट करताना, `temperature` निर्दिष्ट नसणे किंवा `1` वर सेट असणे सुनिश्चित करा.
4. Chat चे `content[].type: "text"` वापरून Responses चे `content[].type: "input_text"` करा, वापरकर्ता/सिस्टम इनपुटसाठी.
5. `text.format` साठी योग्य डिक्शनरी पुरवा (उदा. `{"type": "json_schema", "name": "Output", "schema": ..., "strict": True}`), साधी स्ट्रिंग नाही.
6. Responses मध्ये `seed` पॅरामीटर समर्थित नाही; विनंत्यांमधून काढा.
7. **Reasoning**: केवळ जर मूळ कोडने आधी वापरले असेल तरच `reasoning` समाविष्ट करा. ज्यांच्याकडे reasoning नाही, अशा API कॉल्समध्ये `reasoning` जोडू नका — बरेच reasoning नसलेले मॉडेल हे पॅरामीटर समर्थन करत नाहीत.
8. **`max_output_tokens` मोजणी**: reasoning मॉडेल्स (GPT-5-mini, GPT-5, o-series) साठी `max_output_tokens=4096` किंवा अधिक वापरा — 50–1000 नव्हे. मॉडेल आधी अंतर्गत reasoning टोकन्स वापरतो तर दिसणारा आउटपुट तयार करते; खूप कमी मर्यादा म्हणजे त्रुटीपूर्ण किंवा रिकामा प्रतिसाद.
9. **O-series `max_completion_tokens`**: जर मूळ कोडने `max_completion_tokens` (o-series साठी Azure-विशेष) वापरले असेल तर `max_output_tokens` याने बदला. Responses API `max_completion_tokens` स्वीकारत नाही.
10. **O-series `reasoning_effort`**: जर मूळ कोड `reasoning_effort` (लो/मध्यम/उच्च) वापरत असेल तर ते Responses API कॉलमध्ये `reasoning={"effort": "<value>"}` मध्ये माइग्रेट करा.
11. **O-series स्ट्रीमिंग विलंब**: O-series मॉडेल्स आउटपुट तयार करण्यापूर्वी अंतर्गत reasoning करतात. स्ट्रीमिंग करताना, पहिल्या `response.output_text.delta` इव्हेंटसाठी अधिक विलंब अपेक्षित आहे. हे सामान्य आहे — मॉडेल reasoning करीत आहे, अडकलेले नाही.
9. **`_azure_ad_token_provider` गेला आहे**: `AsyncOpenAI` / `OpenAI` मध्ये `_azure_ad_token_provider` अ‍ॅट्रीब्युट नाही. चाचणी किंवा कोड जे या अ‍ॅट्रीब्युटवर प्रवेश करतात ते `AttributeError` देईल. टोकन पुरवठादार `api_key` म्हणून पास केला जातो आणि क्लायंट ऑब्जेक्टवर तपासता येत नाही.
10. **Snapshot / गोल्डन फाइल्स**: जर चाचणी सूटमध्ये स्नॅपशॉट चाचणी वापरली तर Chat Completions स्ट्रीमिंग आकार (`choices[0]`, `content_filter_results`, `function_call` वगैरे) असलेली **सर्व** स्नॅपशॉट फाइल्स नवीन Responses आकृतीसाठी अपडेट करा. हे चुकून राहू शकते आणि स्नॅपशॉट आशय सुनिश्चिती अपयश होतात.
11. **मॉक मंकीपॅच मार्ग**: मंकीपॅच लक्ष्य `openai.resources.chat.AsyncCompletions.create` → `openai.resources.responses.AsyncResponses.create` (किंवा सिंक्रोनससाठी `Responses.create`) मध्ये बदलले आहे. जुना मार्ग वापरला तर काहीच होत नाही — मॉक इंटरसेप्ट होणार नाही आणि चाचण्या वास्तविक API ला जातील किंवा अयशस्वी होतील.
12. **`input`, `messages` नाही**: मॉक फंक्शन्सना `kwargs.get("input")` वाचावे लागेल, `kwargs.get("messages")` नाही. Responses API संभाषण इतिहासासाठी `input` वापरतो.
13. **पर्यावरण चल नाव**: Azure Identity SDK `ManagedIdentityCredential(client_id=...)` साठी `AZURE_CLIENT_ID` वापरतो (`AZURE_OPENAI_CLIENT_ID` नाही). चाचण्या, `.env` फाइल्स, अ‍ॅप सेटिंग्स, Bicep/इन्फ्रात नाव बदला.
14. **`max_output_tokens` किमान 16 आहे**: Azure OpenAI 16 पेक्षा कमी मूल्ये `400 integer_below_min_value` सह नाकारतो. स्मोक टेस्टसाठी `50`, उत्पादनासाठी `1000+` वापरा. जुन्या `max_tokens` कडे अशी किमान मर्यादा नव्हती.
15. **`AzureDeveloperCliCredential` साठी `tenant_id`**: जेव्हा Azure OpenAI संसाधन वेगळ्या टेनंटमध्ये आहे, तेव्हा तुम्हाला **`tenant_id` स्पष्टपणे पास करणे आवश्यक आहे** — `AzureDeveloperCliCredential(tenant_id=os.getenv("AZURE_TENANT_ID"))`. न झाल्यास, क्रेडेन्शियल चुकीचा टेनंट वापरते आणि `401` देते.
16. **रेट लिमिट्स स्ट्रीमिंगमध्ये वेगळ्या प्रकारे दिसतात**: Chat Completions सह, 429 सहसा स्ट्रीम सुरू होण्यापासून थांबवते. Responses API स्ट्रीमिंगसह, 429 **मिड-स्ट्रीम** होऊ शकते — असिंक इटरेटर अपवाद फेकतो. स्ट्रीमिंग लूप नेहमी `try/except` मध्ये लपेटा आणि फ्रंटेंडकडे त्रुटी JSON ओळी पाठवा म्हणजे ते सौम्यपणे हाताळू शकते.

17. **वेब अॅपसाठी स्ट्रीमिंग त्रुटी हाताळणी अनिवार्य आहे**: नमुना `try: async for event in await coroutine: ... except Exception as e: yield json.dumps({"error": str(e)})` महत्त्वाचा आहे. याशिवाय, SSE/JSONL स्ट्रीम कोणत्याही सर्व्हर-साइड त्रुटीवर शांतपणे संपते आणि फ्रंटेंड अडखळते.
18. **टूल व्याख्या फ्लॅट स्वरूपात वापराव्यात**: Responses API ला `{"type": "function", "name": ..., "parameters": ...}` अपेक्षित आहे — Chat Completions च्या नेस्टेड `{"type": "function", "function": {"name": ..., "parameters": ...}}` स्वरूपात नाही. हे फंक्शन-कॉलिंग कोडसाठी सर्वसाधारण स्थलांतर त्रुटी आहे.
19. **`pydantic_function_tool()` अप्रतिबंधित आहे**: `openai.pydantic_function_tool()` सहाय्यक अद्याप जुना नेस्टेड स्वरूप तयार करतो. ते `responses.create()` सह वापरू नये. टूल स्कीमा मॅन्युअली परिभाषित करा किंवा आउटपुट फ्लॅटन करा.
20. **टूल परिणामांसाठी `function_call_output` वापरा, `role: tool` नाही**: टूल चालविल्यानंतर, `{"type": "function_call_output", "call_id": ..., "output": ...}` जोडा — `{"role": "tool", "tool_call_id": ..., "content": ...}` नाही. असिस्टंटच्या टूल विनंतीसाठी, `messages.extend(response.output)` वापरा — मॅन्युअल `{"role": "assistant", "tool_calls": [...]}` डिक्शनरी नाही.
21. **`strict: true` वापरताना `required` + `additionalProperties: false` आवश्यक**: टूलवर `strict: true` वापरल्यास, प्रत्येक मालमत्ता `required` अ‍ॅरे मध्ये असावी आणि `additionalProperties` `false` असावी. यापैकी कोणतीही चुकल्यास 400 त्रुटी येते.
22. **फंक्शन कॉल आयडींना विशिष्ट उपसर्ग असले पाहिजे**: `input` मध्ये फ्यू-शॉट `function_call` आयटम देतानाचा `id` फील्ड `fc_` ने सुरू होणे आवश्यक आहे आणि `call_id` फील्ड `call_` ने सुरू होणे आवश्यक आहे (उदा. `"id": "fc_example1", "call_id": "call_example1"`). जुना Chat Completions `call_` उपसर्ग `id` साठी वापरल्यास नाकारले जाईल.
23. **GitHub Models Responses API समर्थित नाही**: जर अॅपमध्ये GitHub Models कोड मार्ग (`base_url` `models.github.ai` किंवा `models.inference.ai.azure.com` कडे निर्देशीत) असेल, तर तो पूर्णपणे काढून टाका. कोणताही स्थलांतर मार्ग नाही — Azure OpenAI, OpenAI किंवा सुसंगत स्थानिक एपीआयवर जा.
24. **कंटेंट फिल्टर त्रुटी शरीर रचना बदलली**: Chat Completions त्रुटी `error.body["innererror"]["content_filter_result"]` (एकवचनी) वापरत होत्या. Responses API त्रुटी `error.body["content_filters"][0]["content_filter_results"]` (बहुवचनी, अॅरे मध्ये) वापरतात. `innererror` की आता अस्तित्वात नाही. थेट `innererror` प्रवेश करणारा कोड रनटाइमवर `KeyError` उडवेल — स्थलांतरात हे सहज चुकू शकते कारण ते फक्त कंटेंट फिल्टर खरंच ट्रिगर झाल्यावर दिसते. स्थलांतर करताना नेहमी `innererror` साठी शोधा.
25. **रॉ HTTP कॉलसाठी URL + बॉडी पुनर्लेखन आवश्यक**: Azure OpenAI REST थेट कॉल करणाऱ्या अॅप्सना (जसे `requests`, `httpx`, `aiohttp` वापरून) `/openai/deployments/{name}/chat/completions?api-version=...` ऐवजी `/openai/v1/responses` वर स्विच करणे आवश्यक आहे. रिक्वेस्ट बॉडीत `messages` ऐवजी `input` वापरतात, `max_output_tokens` आणि `store` आवश्यक आहेत, आणि `api-version` क्वेरी पॅरामीटर काढला जातो. प्रतिसाद बॉडी टेक्स्ट `output[0].content[0].text` येथे आहे — **नाही:** `output_text`, जे SDK सोपेपणा आहे आणि रॉ REST JSON मध्ये नाही.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**अस्वीकरण**:
हा दस्तऐवज AI भाषांतर सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) चा वापर करून अनुवादित केला आहे. जरी आम्ही अचूकतेसाठी प्रयत्न करतो, तरी कृपया लक्षात घ्या की स्वयंचलित भाषांतरांमध्ये त्रुटी किंवा अचूकतेची कमतरता असू शकते. मूळ दस्तऐवज त्याच्या मूळ भाषेत अधिकृत स्रोत मानला पाहिजे. महत्त्वाची माहिती असल्यास, व्यावसायिक मानवी भाषांतराची शिफारस केली जाते. या भाषांतराच्या वापरामुळे उद्भवणाऱ्या कोणत्याही गैरसमज किंवा चुकीच्या अर्थलावणीसाठी आम्ही जबाबदार नाही.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->