# సమస్య పరిష్కారం, ప్రమాద పట్టిక & గోచర్స్

## 400ల సమస్య పరిష్కారం

| లోపం | పరిష్కారం |
|-------|-----|
| `missing_required_parameter: tools[0].name` | టూల్ నిర్వచనం పాత Chat Completions నెస్ట్ ఫార్మాట్ ఉపయోగిస్తుంది | `{"type": "function", "function": {"name": ...}}` నుండి `{"type": "function", "name": ..., "parameters": ...}` కి ఫ్లాటెన్ చేయండి — name, description, parameters శీర్షిక స్థాయిలో ఉండాలి |
| `unknown_parameter: input[N].tool_calls` | బహుళ-తిరుగు టూల్ ఫలితాలు పాత Chat Completions ఫార్మాట్ ఉపయోగిస్తాయి | `{"role": "assistant", "tool_calls": [...]}` + `{"role": "tool", ...}` ని `response.output` అంశాలతో + `{"type": "function_call_output", "call_id": ..., "output": ...}` తో భర్తీ చేయండి |
| `invalid_function_parameters: 'required' is required` | `strict: true` టూల్ వద్ద `required` అర్రే లేదు | `strict: true` ఉన్నప్పుడు, అన్ని లక్షణాలు `required` లో ఉండాలి మరియు `additionalProperties: false` సెట్ చేయాలి |
| `invalid_function_parameters: 'additionalProperties' is required` | `strict: true` టూల్ వద్ద `additionalProperties: false` లేదు | `"additionalProperties": false` ని పరామితుల ఆబ్జెక్టులో చేర్చండి |
| `invalid input[N].id: Expected an ID that begins with 'fc'` | Few-shot function_call ID తప్పు ఉపసర్గ ఉపయోగిస్తోంది | Function call IDs తప్పకుండా `fc_` తో మొదలవ్వాలి (ఉదా: `fc_example1`), `call_` కాదు |
| `missing_required_parameter: text.format.name` | ఫార్మాట్ డిక్ట్‌కి `"name"` కీ చేర్చండి (ఉదా: `"name": "Output"`) |
| `invalid_type: text.format` | `text.format` ఒక స్ట్రింగ్ కాకుండా dict కావాలి, అందులో `type`, `name`, `strict`, `schema` కీలు ఉండాలి |
| `invalid input content type` | చాట్‌లోని `text` స్థానంలో `input_text`/`output_text` కంటెంట్ టైప్స్ ఉపయోగించండి |
| `invalid input content type` (image) | ఇమేజ్ కంటెంట్ ఇంకా `"type": "image_url"` ఉపయోగిస్తుంది | దానిని `"type": "input_image"` కి మార్చండి |
| `Expected object, got string` on `image_url` | `image_url` ఇంకా నెస్ట్ ఆబ్జెక్ట్ `{"url": "..."}` గా ఉంది | దీనిని సాదా స్ట్రింగ్‌గా మార్చండి: `"image_url": "https://..."` లేదా `"image_url": "data:image/...;base64,..."` |
| `integer below minimum value` for `max_output_tokens` | Azure OpenAI వద్ద కనీసం **16** కావాలి. పరీక్షలకు 50+ మరియు ఉత్పత్తికి 1000+ వాడండి |
| `429 Too Many Requests` during streaming | రేటు పరిమితి వచ్చింది. స్ట్రీమింగ్‌ను `try/except` లో వుంచి, జావస్క్రిప్ట్ కి error JSON ఇవ్వండి, బ్యాక్‌ఆఫ్/రిటీ ప్రయోగించండి |
| `KeyError: 'innererror'` on content filter error | Responses API లో కంటెంట్ ఫిల్టర్ లోపం శరీరం నిర్మాణం మారింది | Chat Completions లో `error.body["innererror"]["content_filter_result"]` ఉపయోగించుతూ ఉండేవారు; Responses API ఇప్పుడు `error.body["content_filters"][0]["content_filter_results"]` (పంచురూపంలో, ఏర్రే లో). అన్ని `innererror` యాక్సెస్‌లను మళ్ళీ రాయండి |

---

## మార్పిడి ప్రమాద పట్టిక

| లక్షణం | సాధ్యమైన పొరపాటు | పరిష్కారం |
|---------|---------------|-----|
| ఖాళీ `output_text` / కత్తిరించిన స్పందన | `max_output_tokens` తక్కువగా ఉంది, reasoning మోడల్స్ కోసం | `max_output_tokens=1000` లేదా ఎక్కువగా సెట్ చేయండి — reasoning టోకెన్లు పరిమితి మీద ప్రభావం కలిగిస్తాయి |
| `400 invalid_type: text.format` | `text.format` dict కాకుండా `response_format` స్ట్రింగ్ ఇచ్చారు | `text={"format": {"type": "json_schema", "name": "...", "strict": True, "schema": {...}}}` ఉపయోగించండి |
| `/openai/v1/responses` పై `404 Not Found` | base_url తప్పు — `/openai/v1/` పూర్తి లేదు | `base_url=f"{endpoint}/openai/v1/"` (ట్రైలింగ్ స్లాష్ తో) నిర్ధారించుకోండి |
| `OpenAI()` కు మారిన తర్వాత `401 Unauthorized` | `api_key` సెట్ కాని లేదా token provider సరైనవిగా పాస్ కాని | EntraID కోసం: `api_key=token_provider` (అంటే callable). API key కోసం: `api_key=os.environ["AZURE_OPENAI_API_KEY"]` |
| మోడల్ `deployment not found` ఇస్తోంది | `model` పరామితి మీ Azure deployment పేరుతో సరిపోలడం లేదు | `model=os.environ["AZURE_OPENAI_DEPLOYMENT"]` వాడండి — ఇది deployment పేరు, model పేరు కాదు |
| `json.loads(resp.output_text)` లో `JSONDecodeError` | స్కీమా అమలులో లేదు లేదా మోడల్ కఠిన JSON మద్దతు ఇవ్వదు | స్కీమాలో `"strict": True` ఉండాలని మరియు మోడల్ స్ట్రక్చర్డ్ అవుట్‌పుట్ మద్దతు ఇవ్వడాన్ని నిర్ధారించండి |
| స్ట్రీమింగ్‌లో `delta` ఈవెంట్స్ లేవు | తప్పు ఈవెంట్ మాటరీం తనిఖీ చేస్తున్నారు | `event.type == "response.output_text.delta"` పై ఫిల్టర్ పెట్టండి, Chat లోని `chat.completion.chunk` కాదు |
| మార్పిడి తర్వాత ఇమేజ్ ఇన్‌పుట్ పై `400` లోపం | ఇమేజ్ కంటెంట్ టైపు అప్‌డేట్ కాలేదు | `"type": "image_url"` → `"type": "input_image"` గా మార్చండి, `"image_url": {"url": "..."}` → `"image_url": "..."` (సాదాసీదా స్ట్రింగ్) గా ఫ్లాటెన్ చేయండి |
| టూల్ కాల్స్ అనంతంగా తిరుగుతాయి | ఫాలో-అప్ `input` లో టూల్ ఫలితం లేదు | టూల్ నెరవేర్చిన తర్వాత, తదుపరి అభ్యర్థనలో `input`కి `{"type": "function_call_output", "call_id": ..., "output": ...}` అంశాన్ని జోడించండి |
| GPT-5 లేదా o-series తో `temperature` లోపం | స్పష్టమైన `temperature` విలువ 1 కాకుండా ఉంది | GPT-5 మరియు o-series మోడల్స్ (o1, o3-mini, o3, o4-mini) కోసం `temperature` తీసేయండి లేదా 1 గా సెట్ చేయండి |
| o-series తో `top_p` లోపం | `top_p` మద్దతు లేదు | o-series మోడల్స్ టార్గెట్ చేసినప్పుడు `top_p` తీసేయండి |
| `max_completion_tokens` గుర్తించబడలేదు | Azure ప్రత్యేక పరామితి వాడుతున్నారు | `max_completion_tokens` ని `max_output_tokens` తో మార్చండి. o-series కోసం 4096+ సెట్ చేయండి (reasoning టోకెన్లు పరిమితికి వ్యతిరేకం) |
| o-series నుండి ఖాళీ/కత్తిరించిన అవుట్‌పుట్ | `max_output_tokens` తక్కువగా సెట్ చేశారు | o-series లో reasoning టోకెన్లు అంతర్గతంగా వాడుతాయి. `max_output_tokens=4096` లేదా ఎక్కువగా సెట్ చేయండి — 500–1000 కాదు |
| `400 integer_below_min_value` `max_output_tokens` కోసం | విలువు 16 కంటే తక్కువ | Azure OpenAI లో `max_output_tokens >= 16` తప్పనిసరి. స్మోక్ టెస్టులకు 50+, ఉత్పత్తికి 1000+ వాడండి |
| స్ట్రీమ్ మధ్యలో `429 Too Many Requests` | Azure OpenAI రేటు పరిమితి | స్ట్రీమ్ ఎరర్స్ లేకుండా మధ్యలో విరిగిపోతుంది. ఎప్పుడూ `async for event in await coroutine:` ను `try/except` తో కప్పండి మరియు `{"error": str(e)}` ఫ్రంట్ ఎండ్ కు ఇవ్వండి |
| `AzureDeveloperCliCredential` → `CredentialUnavailableError` | తప్పు టెనంట్ లేదా లాగిన్ కాలేదు | `tenant_id=os.getenv("AZURE_TENANT_ID")` ను స్పష్టంగా పాస్ చేయండి. స్థానికంగా `azd auth login --tenant <tenant-id>` నడిపించండి |
| GitHub Models (`models.github.ai`) ఉపయోగించి `404 Not Found` | GitHub Models Responses API మద్దతు ఇవ్వడం లేదు | GitHub Models కోడ్ మార్గం పూర్తిగా తీసేయండి. Azure OpenAI, OpenAI, లేదా Ollama వంటి Responses మద్దతును కలిగిన లోకల్ ఎండ్పాయింట్ వాడండి |
| MAF `OpenAIChatCompletionClient` ఇంతకుముందు Chat Completions వాడుతోంది | 1.0.0+ లో పాత MAF క్లయింట్ వాడుతున్నాయి | MAF 1.0.0+ లో, `OpenAIChatClient` డిఫాల్ట్ గా Responses API వాడుతుంది. `OpenAIChatCompletionClient` ని `OpenAIChatClient` గా మార్చండి. 1.0.0 పూర్వంగా ఉన్నవారు `agent-framework-openai>=1.0.0`కి అప్‌గ్రేడ్ అవ్వండి |
| LangChain ఏజెంట్ ఖాళీగా ఉంటుంది లేదా టూల్ కాల్స్ తో ఫెయిలవుతుంది | `ChatOpenAI` Responses API ఉపయోగించడం లేదు | `ChatOpenAI(...)`లో `use_responses_api=True` చేర్చండి. స్పందన సందేశాలలో `.content` ను `.text` గా మార్చండి |
| కంటెంట్ ఫిల్టర్ లోపం హ్యాండ్లర్ లో `KeyError: 'innererror'` | Responses API లో తప్పిద శరీరం నిర్మాణం మారింది | `error.body["innererror"]["content_filter_result"]["jailbreak"]` ని `error.body["content_filters"][0]["content_filter_results"]["jailbreak"]` గా మార్చండి. `innererror` ముట్టుబడి లేదు; కంటెంట్ ఫిల్టర్ వివరాలు ఇప్పుడు టాప్-లెవెల్ `content_filters` ఏర్రే లో, ప్రతి అంశంలో `content_filter_results` ఉన్నవి |
| `/openai/deployments/.../chat/completions` కు రా HTTP కాల్ 404 ఇస్తోంది | పాత Chat Completions REST ఎండ్పాయింట్ | URL ని `/openai/v1/responses` గా మార్చండి. రిక్వెస్ట్ బాడీ: `messages` → `input`, `max_output_tokens` + `store: false` చేర్చండి, `api-version` క్వేరిం పారామితి తీసేయండి. స్పందన పర్‌సింగ్: `choices[0].message.content` → `output[0].content[0].text` (గమనిక: `output_text` ఒక SDK సౌకర్యం, రా REST JSON లో లేదు) |

---

## గోచర్స్

1. మీరు ముందుగా Chat Completions ను సంభాషణ స్థితి కోసం వాడితే, Responses తో మీ స్వంత స్థితిని స్పష్టంగా నిర్వహించండి.
2. పాత `max_tokens` కంటే `max_output_tokens` మను సూచించండి.
3. `gpt-5` కి మారుతున్నప్పుడు, `temperature` ఉంచకూడదు లేదా `1` గా సెట్ చేయండి.
4. చాట్ లోని `content[].type: "text"` ను Responses లో `content[].type: "input_text"` తో మార్చండి, ఇది వినియోగదారు/సిస్టమ్ ఇన్‌పుట్లకు.
5. `text.format` కోసం సరైన డిక్ట్ ఇవ్వండి (ఉదా: `{"type": "json_schema", "name": "Output", "schema": ..., "strict": True}`), సాధారణ స్ట్రింగ్ కాదు.
6. Responses లో `seed` పరామితి మద్దతు లేదు; దాన్ని అభ్యర్థనల నుండి తీసేయండి.
7. **Reasoning**: అసలు కోడ్‌లో ఇదే వాడితేనే `reasoning` చేర్చండి. ఇది లేని API కాల్స్ కి `reasoning` జోడించకండి — ఎక్కువ నాన్-రీజనింగ్ మోడల్స్ ఈ పరామితిని మద్దతు ఇవ్వవు.
8. **`max_output_tokens` పరిమాణం**: reasoning మోడల్స్ కు (GPT-5-mini, GPT-5, o-series), `max_output_tokens=4096` లేదా ఎక్కువ వాడండి — 50–1000 కాదు. మోడల్ అవుట్‌పుట్ ముందు reasoning టోకెన్లను అంతర్గతంగా ఉపయోగిస్తుంది; తక్కువ పరిమితులు truncate చేయబడిన లేదా ఖాళీ స్పందనలు కలిగిస్తాయి.
9. **O-series `max_completion_tokens`**: అసలు కోడ్ లో `max_completion_tokens` (o-series-కాఖ్యాత Azure స్పెసిఫిక్) వాడితే, దానిని `max_output_tokens` తో మార్చండి. Responses API `max_completion_tokens` తీసుకోదు.
10. **O-series `reasoning_effort`**: అసలు కోడ్ లో `reasoning_effort` (కిమి/మధ్యస్థ/అధిక) వాడితే, దీనిని Responses API కాల్ లో `reasoning={"effort": "<value>"}` గా మార్చండి.
11. **O-series స్ట్రీమింగ్ ఆలస్యం**: O-series మోడల్స్ అవుట్‌పుట్ తయారీ ముందు అంతర్గత reasoning చేస్తాయి. స్ట్రీమింగ్ చేస్తుంటే మొదటి `response.output_text.delta` ఈవెంట్ ముందు ఎక్కువ ఆలస్యం సాధారణం — మోడల్ reasoning చేస్తున్నതാണ്, ఆగబில்லை.
9. **`_azure_ad_token_provider` పోయింది**: `AsyncOpenAI` / `OpenAI` వద్ద `_azure_ad_token_provider` అట్రిబ్యూట్ పిలవబడదు. ఆ అట్రిబ్యూట్ యాక్సెస్ చేసే టెస్టులు లేదా కోడ్ `AttributeError` ఇస్తుంది. టోకెన్ ప్రొవైడర్ `api_key` గా పాస్ అవుతుంది మరియు క్లయింట్ ఆబ్జెక్ట్ నుంచి పర్యవేక్షించలేరు.
10. **స్నాప్‌షాట్ / గోల్డెన్ ఫైల్స్**: టెస్ట్ సూట్ స్నాప్‌షాట్ టెస్టింగ్ చేస్తే, **అన్ని** స్నాప్‌షాట్ ఫైళ్ళు Chat Completions స్ట్రీమింగ్ ఆకృతి (`choices[0]`, `content_filter_results`, `function_call`, మొదలైనవి) నుండి కొత్త Responses ఆకృతికి అప్‌డేట్ అయ్యి ఉండాలి. ఇది మిస్ అయితే స్నాప్‌షాట్ అసర్ట్ విఫలమవుతుంది.
11. **మాక్ మంకీపాచ్ పాథ్**: మంకీపాచ్ లక్ష్యం మారింది: `openai.resources.chat.AsyncCompletions.create` → `openai.resources.responses.AsyncResponses.create` (లేదా సమకాల Sync కోసం `Responses.create`). పాత పాథ్ వాడితే మంకీచేస్తుంది కాదు — మాక్ ఇన్టర్సెప్ట్ చేయదు, టెస్టులు నిజమైన API ను కలుస్తాయి లేదా విఫలమవుతాయి.
12. **`input` కాదు `messages`**: మాక్ ఫంక్షన్లు `kwargs.get("input")` చదవాలి, `kwargs.get("messages")` కాదు. Responses API సంభాషణ చరిత్రకి `input` వాడుతుంది.
13. **పర్యావరణ చారాల పేరు**: Azure Identity SDK `ManagedIdentityCredential(client_id=...)` కోసం `AZURE_CLIENT_ID` (కాదు `AZURE_OPENAI_CLIENT_ID`) వాడుతుంది. టెస్టులు, `.env` ఫైల్స్, యాప్ సెట్టింగ్స్, Bicep/ఇన్‌ఫ్రాలో పేరు మార్చండి.
14. **`max_output_tokens` కనీసం 16**: Azure OpenAI 16 కంటే తక్కువ విలువలకు `400 integer_below_min_value` ఇస్తుంది. స్మోక్ టెస్టులకు 50, ఉత్పత్తికి 1000+ వాడండి. పాత `max_tokens` కి ఇలాంటి కనీసం లేదు.
15. **`AzureDeveloperCliCredential`కి `tenant_id`**: Azure OpenAI వనరు వేరే టెనంట్‌లో ఉంటే `tenant_id` తప్పనిసరి గా పాస్ చేయాలి — `AzureDeveloperCliCredential(tenant_id=os.getenv("AZURE_TENANT_ID"))`. లేకుంటే క్రెడెన్షియల్ తప్పు టెనంట్ వాడి `401` ఇస్తుంది.
16. **స్ట్రీమింగ్‌లో రేటు పరిమితుల ప్రదర్శన వేరేలా ఉంటుంది**: Chat Completions కు 429 సాధారణంగా స్ట్రీమ్ ప్రారంభం ఆపేది. Responses API స్ట్రీమింగ్ లో, 429 **మధ్యలో** వచ్చేయచ్చు — అసింక్ యిటరేటర్ ఎక్స్‌సెప్షన్ వేస్తుంది. ఎప్పుడూ స్ట్రీమింగ్ లూప్ ను `try/except` లో ఉంచి, error JSON లైన్ ఇవ్వండి, ఫ్రంట్ ఎండ్ సజావుగా హ్యాండిల్ చేయగలుగుతుంది.

17. **వెబ్ యాప్‌ల కోసం స్ట్రీమింగ్ లోపం నిర్వహణ తప్పనిసరి**: `try: async for event in await coroutine: ... except Exception as e: yield json.dumps({"error": str(e)})` అనే ప్యాటర్న్ కీలకం. ఈ విధానం లేకుంటే, SSE/JSONL స్ట్రీమ్ ఏదైనా సర్వర్-సైడ్ లోపం వచ్చినప్పుడు నిశ్శబ్దంగా ముగుస్తుంది మరియు ఫ్రంట్‌ఎండ్ హ్యాంగ్ అవుతుంది.
18. **టూల్ నిర్వచనాలు ఫ్లాట్ ఫార్మాట్ ఉపయోగించాలి**: Responses API `{"type": "function", "name": ..., "parameters": ...}` ఆకృతిని ఆశిస్తుంది — Chat Completions లోని నెస్టెడ్ `{"type": "function", "function": {"name": ..., "parameters": ...}}` కాదు. ఇది function-calling కోడ్ కోసం అత్యంత సాధారణమైన మైగ్రేషన్ లోపం.
19. **`pydantic_function_tool()` అనుకూలంగాని కాదు**: `openai.pydantic_function_tool()` సహాయకుడు ఇప్పటికీ పాత నెస్టెడ్ ఫార్మాట్‌ను ఉత్పత్తి చేస్తుంది. దీన్ని `responses.create()` తో ఉపయోగించవద్దు. టూల్ స్కీమాలను మాన్యువల్‌గా నిర్వచించండి లేదా అవుట్పుట్‌ను ఫ్లాటెన్ చేయండి.
20. **టూల్ ఫలితాలు `function_call_output` ఉపయోగిస్తాయి, `role: tool` కాదు**: ఒకటోసారి టూల్ అమలు చేసిన తర్వాత `{"type": "function_call_output", "call_id": ..., "output": ...}`ను జోడించండి — `{"role": "tool", "tool_call_id": ..., "content": ...}` కాదు. అసిస్టెంట్ టూల్ అభ్యర్థన కోసం `messages.extend(response.output)` ఉపయోగించండి — మాన్యువల్ `{"role": "assistant", "tool_calls": [...]}` డిక్ట్ కాకూడదు.
21. **`strict: true` కోసం `required` + `additionalProperties: false` అవసరం**: టూల్‌కి `strict: true` ఉపయోగించే సమయంలో, ప్రతి ప్రాపర్టీ `required` అర్రేలో ఉంచాలి మరియు `additionalProperties` ని `false` గా సెట్ చేయాలి. ఏదయినా కోల్పోతే 400 లోపం వస్తుంది.
22. **ఫంక్షన్ కాల్ IDs కి నిర్దিষ্ট ప్రిఫిక్సులు ఉంటాయి**: Few-shot `function_call` అంశాలు `input` లో ఇవ్వబడుతున్నప్పుడు, `id` ఫీల్డ్ `fc_` తో, `call_id` ఫీల్డ్ `call_` తో మొదలవ్వాలి (ఉదాహరణకు, `"id": "fc_example1", "call_id": "call_example1"`). పాత Chat Completions లోని `call_` ప్రిఫిక్సు `id` కోసం ఉపయోగించడం తిరస్కరించబడుతుంది.
23. **GitHub Models Responses API ను మద్దతు ఇవ్వదు**: యాప్ GitHub Models కోడ్ పాత్ (`base_url` `models.github.ai` లేదా `models.inference.ai.azure.com`కి సూచన) ఉంటే దానిని పూర్తిగా తీసివేయండి. మైగ్రేషన్ మార్గం లేదు — Azure OpenAI, OpenAI లేదా అనుకూల స్థానిక ఎండ్పాయింట్ కు మారండి.
24. **కంటెంట్ ఫిల్టర్ లోపం బాడీ ساخت౦ మారింది**: Chat Completions లోపాలు `error.body["innererror"]["content_filter_result"]` (ఏకవచనం) ఉపయోగించేవి. Responses API లోపాలు `error.body["content_filters"][0]["content_filter_results"]` (బహువచనం, అర్రేలో) ఉపయోగిస్తాయి. `innererror` కీ ఇక లేరు. `innererror` ని నేరుగా యాక్సెస్ చేసే కోడ్-runtime లో `KeyError` ను పుట్టిస్తుంది — ఇది migration లో దాదాపు కనిపించదు ఎందుకంటే కంటెంట్ ఫిల్టర్ నిజంగా trigger అవుతుండғанда మాత్రమే కనిపిస్తుంది. మైగ్రేషన్ సమయంలో ఎప్పుడూ `innererror` కోసం grep చేయండి.
25. **రా HTTP కాల్స్ కి URL + బాడీ రీక్రైట్ అవసరం**: /openai/deployments/{name}/chat/completions?api-version=... URL తో Azure OpenAI RESTను నేరుగా పిలువడం (requests, httpx, aiohttp ద్వారా) చేస్తే, అది /openai/v1/responses కి మారాలి. అభ్యర్థన బాడీ `messages` కు బదులుగా `input` ఉపయోగిస్తుంది, `max_output_tokens` మరియు `store` అవసరం మరియు `api-version` క్వెరీ పరామీటర్ తీసివేయబడింది. ప్రతిస్పందన బాడీ టెక్స్ట్ `output[0].content[0].text` లో ఉంటుంది — **కాదు** `output_text`, ఇది SDK సౌకర్యపు ప్రాపర్టీ; రా REST JSONలో లేరు.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**అస్వీకరణ**:
ఈ పత్రం AI అనువాద సేవ [Co-op Translator](https://github.com/Azure/co-op-translator) ఉపయోగించి అనువదించబడింది. మేము ఖచ్చితత్వానికి ప్రయత్నిస్తున్నప్పటికీ, ఆటోమేటెడ్ అనువాదాలు తప్పులు లేదా అసమగ్రతలను కలిగి ఉండవచ్చు. దాని స్వదేశ భాషలో ఉన్న అసలు పత్రాన్ని అధికారం కలిగిన మూలంగా పరిగణించాలి. కీలకమైన సమాచారం కోసం, ప్రొఫెషనల్ మానవ అనువాదాన్ని సిఫారసు చేస్తాము. ఈ అనువాదం ఉపయోగం వల్ల కలిగే ఏవైనా అపార్థాలు లేదా తప్పుదారులు కోసం మేము బాధ్యత వహించము.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->