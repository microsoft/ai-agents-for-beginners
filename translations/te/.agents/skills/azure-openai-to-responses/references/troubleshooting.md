# సమస్యలను పరిష్కరించడం, ప్రమాద పట్టిక & గోచస్

## 400ల సమస్య పరిష్కారం

| లోపం | పరిష్కారం |
|-------|-----|
| `missing_required_parameter: tools[0].name` | టూల్ నిర్వచనం పాత చాట్ కంప్లిషన్స్ nested ఫార్మాట్ను ఉపయోగిస్తుంది | `{"type": "function", "function": {"name": ...}}` నుండి `{"type": "function", "name": ..., "parameters": ...}`గా మలచి - పేరు, వివరణ, పరామితులు టాప్ లెవల్ వద్ద ఉంచండి |
| `unknown_parameter: input[N].tool_calls` | మల్టీ-టర్న్ టూల్ ఫలితాలు పాత చాట్ కంప్లిషన్స్ ఫార్మాట్ ఉపయోగిస్తాయి | `{"role": "assistant", "tool_calls": [...]}` + `{"role": "tool", ...}` ను `response.output` అంశాలతో + `{"type": "function_call_output", "call_id": ..., "output": ...}`గా మార్చండి |
| `invalid_function_parameters: 'required' is required` | `strict: true` టూల్ లో `required` వరుస లేదు | `strict: true` ఉన్నపుడు అన్ని ప్రాపర్టీలను `required` లో చేర్చాలి మరియు `additionalProperties: false` కూడా అమలు చేయాలి |
| `invalid_function_parameters: 'additionalProperties' is required` | `strict: true` టూల్ లో `additionalProperties: false` లేకపోవడం | పరామితుల అంశానికి `"additionalProperties": false` జోడించండి |
| `invalid input[N].id: Expected an ID that begins with 'fc'` | Few-shot function_call ID prefix తప్పు | function call IDs `fc_`తో ప్రారంభం అవ్వాలి (ఉదా: `fc_example1`), `call_` కాదు |
| `missing_required_parameter: text.format.name` | ఫార్మాట్ డిక్ట్ కు `"name"` కీ జోడించండి (ఉదా: `"name": "Output"`) |
| `invalid_type: text.format` | `text.format` ఒక స్ట్రింగ్ కాకుండా `type`, `name`, `strict`, `schema` కలిగిన డిక్ట్ కాదని నిర్ధారించండి |
| `invalid input content type` | చాట్ `text` బదులుగా `input_text`/`output_text` కంటెంట్ టైప్స్ ఉపయోగించండి |
| `invalid input content type` (సేక్రితం) | ఇమేజ్ కంటెంట్ ఇంకా `"type": "image_url"` ఉపయోగిస్తుంది | `"type": "input_image"`గా మార్చండి |
| `Expected object, got string` on `image_url` | `image_url` nested ఆబ్జెక్ట్ గా ఉంది `{"url": "..."}` | సాధారణ స్ట్రింగ్ గా మార్చండి: `"image_url": "https://..."` లేదా `"image_url": "data:image/...;base64,..."` |
| `integer below minimum value` for `max_output_tokens` | Azure OpenAIలో కనీసం **16** కావాలి. టెస్టులకి 50+ మరియు ప్రొడక్షన్‌కి 1000+ ఉపయోగించండి. |
| `429 Too Many Requests` during streaming | రేట్ లిమిటెడ్. స్ట్రీమింగ్‌ను `try/except`లో చుట్టండి, error JSONను ఫ్రంట్‌ఎండ్‌కు ఇవ్వండి, బ్యాకాఫ్/రెట్రై అమలు చేయండి. |
| `KeyError: 'innererror'` on content filter error | Responses APIలో కంటెంట్ ఫిల్టర్ లోపం బాడీ స్ట్రక్చర్ మారింది | Chat Completions `error.body["innererror"]["content_filter_result"]` వాడింది; Responses API `error.body["content_filters"][0]["content_filter_results"]` (plural, array లో). అన్ని `innererror` యాక్సెస్‌లను రివ్రైటు చేయండి. |

---

## మైగ్రేషన్ ప్రమాద పట్టిక

| లక్షణం | సాధ్యమైన పొరపాటు | పరిష్కారం |
|---------|---------------|-----|
| ఖాళీ `output_text` / కట్ అయిన ప్రతిస్పందన | reasoning మోడల్స్ కోసం `max_output_tokens` తక్కువగా ఉంది | `max_output_tokens=1000` లేదా ఎక్కువగా సెట్ చేయండి — reasoning టోకెన్లు లిమిట్‌ను తగ్గిస్తాయి |
| `400 invalid_type: text.format` | `text.format` డిక్ట్ బదులుగా `response_format` స్ట్రింగ్ ఇచ్చారు | `text={"format": {"type": "json_schema", "name": "...", "strict": True, "schema": {...}}}` ఉపయోగించండి |
| `/openai/v1/responses`పై `404 Not Found` | తప్పు `base_url` - `/openai/v1/` లేదు | `base_url=f"{endpoint}/openai/v1/"` (ట్రైలింగ్ స్లాష్ తో) ఉండాలి |
| `401 Unauthorized` `OpenAI()`కు మార్చిన తర్వాత | `api_key` సెట్ చేయకపోవడం లేదా టోకన్ ప్రొవైడర్ సరైన విధంగా ఇవ్వకపోవడం | ఎంట్రా ID కోసం: `api_key=token_provider` (콜బుల్). API కీ కోసం: `api_key=os.environ["AZURE_OPENAI_API_KEY"]` |
| మోడల్ `deployment not found` తిరిగి ఇస్తోంది | `model` పారామితి మీ Azure డిప్లాయిమెంట్ పేరు కాకపోవడం | `model=os.environ["AZURE_OPENAI_DEPLOYMENT"]` వాడండి - ఇది deployment పేరు, మోడల్ పేరు కాదు |
| `json.loads(resp.output_text)`లో `JSONDecodeError` వస్తోంది | స్కీమా అమలు కాలేదన్న లేదా మోడల్ స్ట్రిక్ట్ JSON మద్దతు ఇవ్వలేదు | స్కీమాలో `"strict": True` ఉన్నదని నిర్ధారించండి, మోడల్ స్ట్రక్చర్డ్ అవుట్పుట్ మద్దతు ఇస్తుందో ఖచ్చితంగా చూడండి |
| స్ట్రీమింగ్ లో ఎలాంటి `delta` ఈవెంట్లు లేవు | తప్పు ఈవెంట్ టైపు చెక్ చేస్తున్నారు | `event.type == "response.output_text.delta"` ఫిల్టర్ చేయండి, చాట్‌లో ఉన్న `chat.completion.chunk` కాదు |
| మైగ్రేషన్ తరువాత ఇమేజ్ ఇన్‌పుట్ లో `400` లోపం | ఇమేజ్ కంటెంట్ టైపు అప్డేట్ కాలేదు | `"type": "image_url"` → `"type": "input_image"`గా మార్చండి మరియు `"image_url": {"url": "..."}` → `"image_url": "..."` (సాధారణ స్ట్రింగ్)గా ఫ్లాటెన్ చేయండి |
| టూల్ కాల్స్ అనంతం జరిగిపోతున్నాయి | ఫాలో-అప్ `input`లో టూల్ ఫలితం లేదు | టూల్ అమలు చేసిన తర్వాత, తదుపరి రిక్వెస్ట్‌లో `input`కి `{"type": "function_call_output", "call_id": ..., "output": ...}` అంశాన్ని జత చేయండి |
| GPT-5 లేదా o-series లో `temperature` లోపం | 1 కాకుండా ఇతర స్పష్టమైన `temperature` విలువ | GPT-5 మరియు o-series మోడల్స్ (o1, o3-mini, o3, o4-mini)కి `temperature` తీసివెయ్యండి లేదా `1`కి సెట్ చేయండి |
| o-series లో `top_p` లోపం | `top_p` మద్దతు లేదు | o-series మోడల్స్‌కి when `top_p` తొలగించండి |
| `max_completion_tokens` గుర్తించబడలేదు | Azure ప్రత్యేక పారామితి వాడుతున్నారు | `max_completion_tokens` బదులుగా `max_output_tokens` వాడండి. o-series కి 4096+ సెట్ చేయండి (reasoning టోకెన్లు లిమిట్‌ను తగ్గిస్తాయి). |
| o-series నుంచి ఖాళీ/కట్ అయిన అవుట్పుట్ | `max_output_tokens` తక్కువగా ఉంది | o-series లో reasoning టోకెన్లు ఇంటర్నల్‌గా వాడుతాయి. `max_output_tokens=4096` లేదా ఎక్కువగా సెట్ చేయండి — 500–1000 కాదు. |
| `400 integer_below_min_value` `max_output_tokens` కోసం | విలువ 16 కంటే తక్కువ | Azure OpenAI `max_output_tokens >= 16` తప్పనిసరి. టెస్టులకు 50+ మరియు ప్రొడక్షన్‌కి 1000+ వాడండి. |
| స్ట్రీమింగ్ మధ్యలో `429 Too Many Requests` | Azure OpenAI ద్వారా రేట్ లిమిటెడ్ | స్ట్రీమ్ ఎర్రర్ హ్యాండ్లింగ్ లేకుండా మౌనంగా బ్రేకు అవుతుంది. ఎల్లప్పుడూ `async for event in await coroutine:` లూప్‌ను `try/except`లో చుట్టండి మరియు ఫ్రంట్‌ఎండ్‌కి `{"error": str(e)}` ఇవ్వండి. |
| `AzureDeveloperCliCredential` → `CredentialUnavailableError` | తప్పు టెనంట్ లేదా లాగిన్ కాదు | `tenant_id=os.getenv("AZURE_TENANT_ID")` స్పష్టంగా అందించండి. లాకల్‌గా `azd auth login --tenant <tenant-id>` నడపండి. |
| GitHub Models (`models.github.ai`) వాడుతున్నప్పుడు `404 Not Found` | GitHub Models Responses API మద్దతు ఇవ్వదు | GitHub Models కోడ్ పాథ్‌ను పూర్తిగా తొలగించండి. Azure OpenAI, OpenAI లేదా Responses మద్దతు ఉన్న స్థానిక ఎండ్‌పాయింట్ (ఉదా: Ollama) ఉపయోగించండి. |
| MAF `OpenAIChatCompletionClient` ఇంకా Chat Completions వాడుతుంది | 1.0.0+ లో పాత MAF క్లయింట్ ఉపయోగిస్తున్నారు | MAF 1.0.0+ లో `OpenAIChatClient` మౌలికంగా Responses API వాడుతుంది. `OpenAIChatCompletionClient`కి బదులుగా `OpenAIChatClient` వాడండి. 1.0.0కు ముందు వర్షన్ అయితే `agent-framework-openai>=1.0.0` కి అప్‌గ్రేడ్ చేయండి. |
| LangChain ఏజెంట్ టూల్ కాల్స్ తో ఖాళీగా లేదా విఫలమవుతుంది | `ChatOpenAI` Responses API వాడడం లేదు | `ChatOpenAI(...)`లో `use_responses_api=True` చేర్చండి. జవాబుల్లో `.content` ను `.text`గా మార్చండి. |
| కంటెంట్ ఫిల్టర్ లోపం హ్యాండ్లర్‌లో `KeyError: 'innererror'` | Responses API లో లోపం బాడీ స్ట్రక్చర్ మారింది | `error.body["innererror"]["content_filter_result"]["jailbreak"]` ను `error.body["content_filters"][0]["content_filter_results"]["jailbreak"]` గా మార్చండి. `innererror` ఆవరణ తొలగింది; కంటెంట్ ఫిల్టర్ వివరాలు ఇప్పుడు టాప్-లెవల్ `content_filters` array లో ఉంటాయి, ప్రతి ఎంట్రీలో `content_filter_results` (plural) ఉంటుంది. |
| `/openai/deployments/.../chat/completions` కు రా HTTP కాల్ `404` ఇస్తుంది | పాత Chat Completions REST ఎండ్‌పాయింట్ | URL ను `/openai/v1/responses`గా మార్చండి. అభ్యర్థన బాడీ: `messages` → `input`, `max_output_tokens` + `store: false` జతచేయండి, `api-version` క్యువరీ పారామ్ తీసివేయండి. స్పందన పార్సింగ్: `choices[0].message.content` → `output[0].content[0].text` (గమనిక: `output_text` అనేది SDK సౌలభ్య ప్రాపర్టీ, రా REST JSON లో లేదు). |

---

## గోచస్

1. మీరు మునుపటి చాట్ కంప్లిషన్స్ వినియోగించి కవర్స్ చేయబడిన సంభాషణ స్థితిని నిర్వహించారంటే, Responses తో మీ స్వంత స్థితిని స్పష్టంగా నిర్వహించండి.
2. పాత `max_tokens`కు బదులుగా `max_output_tokens` వాడటం మెరుగైనది.
3. `gpt-5` కి మారుతున్నప్పుడు, `temperature` స్పష్టంగా ఇవ్వకూడదు లేకపోతే `1`గానే ఉండాలి.
4. చాట్ `content[].type: "text"` ను Responses `content[].type: "input_text"`గా మార్చండి, వినియోగదారు లేదా సిస్టమ్ ఇన్‌పుట్లకు.
5. `text.format` కోసం సరైన డిక్ట్ ఇవ్వండి (ఉదా: `{"type": "json_schema", "name": "Output", "schema": ..., "strict": True}`), సాధారణ స్ట్రింగ్ కాదు.
6. Responses లో `seed` పారామితి మద్దతు లేదు; దానిని అభ్యర్థనల నుండి తీసివేయండి.
7. **Reasoning**: అసలు కోడ్ ఇప్పటికే `reasoning` వాడితేనే దాన్ని చేరిపెట్టండి. లేకపోతే API కాల్స్ కు reasoning జోడించకండి — చాలా మోడల్స్ (ఉదా: gpt-4o-mini) దీనిని మద్దతు ఇవ్వవు.
8. **`max_output_tokens` పరిమాణం**: reasoning మోడల్స్ (GPT-5-mini, GPT-5, o-series) కోసం `max_output_tokens=4096` లేదా ఎక్కువగా వాడండి — 50–1000 కాదు. మోడల్ అవుట్పుట్ ఇవ్వడానికి ముందు reasoning టోకెన్లు లోపల వాడుతుంది; తక్కువ పరిమితులు కార్చ్ కారణంగా అవుట్పుట్ కట్ లేదా ఖాళీ అవుతుంది.
9. **O-series `max_completion_tokens`**: అసలు కోడ్ `max_completion_tokens` (Azure ప్రత్యేకమైనది o-series కి) వాడితే, దానిని `max_output_tokens`తో మార్చండి. Responses API `max_completion_tokens` తీసుకోదు.
10. **O-series `reasoning_effort`**: అసలు కోడ్ `reasoning_effort` (తక్కువ/మధ్యస్థ/అధిక) వాడితే, దీన్ని Responses API కాల్‌లో `reasoning={"effort": "<value>"}`గా మార్చండి.
11. **O-series స్ట్రీమింగ్ ఆలస్యం**: O-series మోడల్స్ అవుట్పుట్ ఇవ్వడానికి ఇంటర్నల్ reasoning చేస్తాయి. స్ట్రీమింగ్‌లో మొదటి `response.output_text.delta` ఈవెంట్‌కు ముందుగా ఎక్కువ ఆలస్యం ఉంటుందని భావించండి. ఇది సర్వసాధారణం — మోడల్ reasoningలో ఉంది, ఫ్రీజ్ కాలేదు.
9. **`_azure_ad_token_provider` ఇక లేదు**: `AsyncOpenAI` / `OpenAI` లో `_azure_ad_token_provider` అట్రిబ్యూట్ ఉండదు. టెస్ట్‌లు లేదా కోడ్ ఆ అట్రిబ్యూట్కు యాక్సెస్ అయితే `AttributeError` తప్పును ఇస్తుంది. టోకెన్ ప్రొవైడర్ `api_key`గా ఇవ్వబడుతుంది మరియు క్లయింట్ ఆబ్జెక్టులో చూడటానికి లేదు.
10. **స్నాప్‌షాట్ / గోల్డెన్ ఫైళ్ళు**: టెస్ట్ సూట్ స్నాప్‌షాట్ టెస్టింగ్ ఉపయోగిస్తుంటే, చాట్ కంప్లిషన్స్ స్ట్రీమింగ్ ఆకృతులు (`choices[0]`, `content_filter_results`, `function_call`, మొదలైనవి) ఉన్న అన్ని స్నాప్‌షాట్ ఫైళ్ళను కొత్త Responses ఆకృతికి సరిచేయాలి. ఇది మిస్ అవ్వడం సులభం, స్నాప్‌షాట్ అసెర్షన్ ఫెయిల్యూర్‌లకు కారణమవుతుంది.
11. **మాక్ మంకీపాచ్ మార్గం**: మంకీపాచ్ లక్ష్యం `openai.resources.chat.AsyncCompletions.create` నుండి `openai.resources.responses.AsyncResponses.create` (లేదా సమకాల సమయానికి `Responses.create`) కు మారింది. పాత మార్గం వాడడం శూన్యం చేస్తుంది - మాక్ ఎఫెక్ట్ చూపదు, టెస్ట్‌లు అసలైన APIని తాకతాయి లేదా విఫలమవుతాయి.
12. **`input` కాదు `messages`**: మాక్ ఫంక్షన్లు `kwargs.get("input")` చదవాలి, `kwargs.get("messages")` కాదు. Responses APIకి సంభాషణ చరిత్ర `input`గా ఉంటుంది.
13. **వాతావరణ వేరియబుల్ పేర్లు**: Azure Identity SDK `ManagedIdentityCredential(client_id=...)` కోసం `AZURE_OPENAI_CLIENT_ID` కాదు, `AZURE_CLIENT_ID` వాడుతుంది. టెస్ట్‌లు, `.env` ఫైళ్లు, యాప్ సెట్టింగ్స్, Bicep/ఇన్ఫ్రాలో పేరు మార్చండి.
14. **`max_output_tokens` కనిష్ఠం 16**: Azure OpenAI 16కి తక్కువ విలువలను `400 integer_below_min_value` తో తిరస్కరిస్తుంది. టెస్ట్‌లకు 50, ప్రొడక్షన్‌కు 1000+ వాడండి. పాత `max_tokens` కి ఇలాంటి కనిష్ఠం లేదు.
15. **`AzureDeveloperCliCredential` కోసం `tenant_id`**: Azure OpenAI రిసోర్స్ బేరే టెనంట్‌లో ఉన్నప్పుడు, తప్పకుండా `tenant_id` స్పష్టంగా ఇవ్వాలి — `AzureDeveloperCliCredential(tenant_id=os.getenv("AZURE_TENANT_ID"))`. లేకపోతే క్రెడెన్షియల్ తప్పు టెనంట్ వాడి మౌనంగా `401` ఇస్తుంది.
16. **స్ట్రీమింగ్‌లో రేట్ లిమిట్లు వేరు విధంగా వస్తాయి**: చాట్ కంప్లిషన్స్‌లో 429 సాధారణంగా స్ట్రీమ్ ప్రారంభించకుండా నిరోధించేది. Responses API స్ట్రీమింగ్‌లో 429 స్ట్రీమ్ మధ్యలో రావచ్చు — async iterator ఒక Exception తీయగలదు. ఎల్లప్పుడూ స్ట్రీమింగ్ లూప్‌ను `try/except`లో ఉంచి, error JSON లైన్‌ పంపి ఫ్రంట్‌ఎండ్ దీన్ని సులభంగా నిర్వహించేందుకు సహాయం చేయండి.

17. **వెబ్ యాప్స్ కోసం స్ట్రీమింగ్ లోపాలను నిర్వహించడం తప్పనిసరి**: `try: async for event in await coroutine: ... except Exception as e: yield json.dumps({"error": str(e)})` నమూనా చాలా ముఖ్యం. దీనిలేని పరిస్తితుల్లో, SSE/JSONL స్ట్రీమ్ సర్వర్-పక్కలో ఏదైనా లోపం జరిగితే నిశ్శబ్దంగా ఆగిపోతుంది మరియు ఫ్రంట్ ఎండ్ హ్యాంగ్ అవుతుంది.
18. **టూల్ నిర్వచనాలు ఫ్లాట్ ఫార్మాట్‌లో ఉండాలి**: రెస్పాన్‌సెస్ API `{"type": "function", "name": ..., "parameters": ...}` ని ఆశిస్తుంది — Chat Completions లోని నెస్టెడ్ `{"type": "function", "function": {"name": ..., "parameters": ...}}` కాదు. ఇది ఫంక్షన్-కాల్ కోడ్ కోసం సాధారణ మైగ్రేషన్ లోపం.
19. **`pydantic_function_tool()` అనుకూలంగా లేదు**: `openai.pydantic_function_tool()` హెల్పర్ ఇంకా పాత నెస్టెడ్ ఫార్మాట్‌ను సృష్టిస్తుంది. దీన్ని `responses.create()` తో ఉపయోగించవద్దు. టూల్ స్కీమాను మానవీయంగా నిర్వచించండి లేదా అవుట్పుట్‌ను ఫ్లాట్ చేయండి.
20. **టూల్ ఫలితాలు `function_call_output` ఉపయోగించాలి, `role: tool` కాదు**: ఒక టూల్ నెరవేర్చిన తర్వాత, `{"type": "function_call_output", "call_id": ..., "output": ...}` జతచేయాలి — `{"role": "tool", "tool_call_id": ..., "content": ...}` కాదు. అసిస్టెంట్ యొక్క టూల్ అభ్యర్ధన కోసం, `messages.extend(response.output)` ఉపయోగించండి — మాన్యువల్ గా `{"role": "assistant", "tool_calls": [...]}` డిక్ట్ కాదు.
21. **`strict: true` కి `required` మరియు `additionalProperties: false` అవసరం**: ఒక టూల్‌పై `strict: true` ఉపయోగించినప్పుడు, ప్రతి ప్రాపర్టీ `required` అర్రేలో ఉండాలి మరియు `additionalProperties` `false` గా ఉండాలి. ఏదైనా లేకపోతే 400 లోపం వస్తుంది.
22. **ఫంక్షన్ కాల్ IDలకు నిర్దిష్ట ప్రిఫిక్స్ ఉంటాయి**: Few-shot `function_call` అంశాలు `input` లో ఇవ్వబడినప్పుడు, `id` ఫీల్డ్ `fc_` తో ప్రారంభమయ్యి, `call_id` ఫీల్డ్ `call_` తో ప్రారంభమవాలి (ఉదా: `"id": "fc_example1", "call_id": "call_example1"`). పాత Chat Completions లో `id` కి `call_` ప్రిఫిక్స్ ఉపయోగించడం తిరస్కరించబడుతుంది.
23. **GitHub Models రెస్పాన్స్ API ని మద్దతు ఇవ్వదు**: యాప్ లో GitHub Models కోడ్ పాథ్ (`base_url` `models.github.ai` లేదా `models.inference.ai.azure.com`కు పాయింట్ చేసిన) ఉంటే, దాన్ని పూర్తిగా తొలగించండి. మైగ్రేషన్ మార్గం లేదు — Azure OpenAI, OpenAI లేదా అనుకూలమైన లోకల్ ఎండ్‌పాయింట్‌కు మారండి.
24. **కంటెంట్ ఫిల్టర్ లోపం శరీర నిర్మాణం మార్చబడింది**: Chat Completions లోపాలు `error.body["innererror"]["content_filter_result"]` (ఏక వైభవం) ఉపయోగించేవి. రెస్పాన్స్ API లోపాలు `error.body["content_filters"][0]["content_filter_results"]` (బహువచనమ్, అర్రేలో) ఉపయోగిస్తాయి. `innererror` కీ ఇక లేదంటే. నేరుగా `innererror` యాక్సెస్ చేసే కోడ్ రన్‌టైమ్‌లో `KeyError` ని సృష్టిస్తుంది — ఇది మైగ్రేషన్ సమయానికే కనపడకపోవచ్చు, ఎందుకంటే కంటెంట్ ఫిల్టర్ వాస్తవానికి ట్రిగ్గర్ అయినప్పుడు మాత్రమే తెలుస్తుంది. మైగ్రేషన్ సమయంలో ఎల్లప్పుడూ `innererror` కోసం గ్రేప్ చేయండి.
25. **నేరుగా HTTP కాల్స్ కి URL + బాడీ పునఃరచన అవసరం**: Azure OpenAI RESTని నేరుగా (`requests`, `httpx`, `aiohttp` ద్వారా) `/openai/deployments/{name}/chat/completions?api-version=...` ఉపయోగించి కాల్ చేసే యాప్స్ `/openai/v1/responses` కి మారాలి. రిక్వెస్ట్ బాడీ `messages` బదులుగా `input`ను ఉపయోగిస్తుంది, `max_output_tokens` మరియు `store` అవసరం, మరియు `api-version` క్యూరీ పారామీటర్ పడుతుంది. రిస్పాన్స్ బాడీ టెక్స్ట్ `output[0].content[0].text` వద్ద ఉంటుంది — **కాదు** `output_text`, ఇది SDK సౌకర్యమైన ప్రాపర్టీ మాత్రమే, రా REST JSONలో లేదు.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**అస్వీకరణ**:
ఈ పత్రం AI అనువాద సేవ [Co-op Translator](https://github.com/Azure/co-op-translator) ఉపయోగించి అనువదించబడింది. మేము ఖచ్చితత్వానికి ప్రయత్నిస్తున్నప్పటికీ, ఆటోమేటెడ్ అనువాదాలు తప్పులు లేదా అసమగ్రతలను కలిగి ఉండవచ్చు. దాని స్వదేశ భాషలో ఉన్న అసలు పత్రాన్ని అధికారం కలిగిన మూలంగా పరిగణించాలి. కీలకమైన సమాచారం కోసం, ప్రొఫెషనల్ మానవ అనువాదాన్ని సిఫారసు చేస్తాము. ఈ అనువాదం ఉపయోగం వల్ల కలిగే ఏవైనా అపార్థాలు లేదా తప్పుదారులు కోసం మేము బాధ్యత వహించము.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->