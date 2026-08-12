# การแก้ไขปัญหา ตารางความเสี่ยง และข้อควรระวัง

## การแก้ไขปัญหา 400s

| ข้อผิดพลาด | การแก้ไข |
|-------|-----|
| `missing_required_parameter: tools[0].name` | นิยามเครื่องมือใช้รูปแบบซ้อน Chat Completions แบบเก่า | แบนฟอร์แมตจาก `{"type": "function", "function": {"name": ...}}` เป็น `{"type": "function", "name": ..., "parameters": ...}` — name, description, parameters อยู่ที่ระดับบน |
| `unknown_parameter: input[N].tool_calls` | ผลลัพธ์เครื่องมือแบบหลายเทิร์นใช้รูปแบบ Chat Completions แบบเก่า | แทนที่ `{"role": "assistant", "tool_calls": [...]}` + `{"role": "tool", ...}` ด้วยรายการ `response.output` + `{"type": "function_call_output", "call_id": ..., "output": ...}` |
| `invalid_function_parameters: 'required' is required` | เครื่องมือ `strict: true` ขาด array `required` | เมื่อใช้ `strict: true` คุณสมบัติทั้งหมดต้องระบุใน `required` และต้องตั้งค่า `additionalProperties: false` |
| `invalid_function_parameters: 'additionalProperties' is required` | เครื่องมือ `strict: true` ขาด `additionalProperties: false` | เพิ่ม `"additionalProperties": false` ในอ็อบเจ็กต์พารามิเตอร์ |
| `invalid input[N].id: Expected an ID that begins with 'fc'` | รหัสฟังก์ชันคอลล์ few-shot มีคำนำหน้าผิด | รหัสฟังก์ชันคอลล์ต้องขึ้นต้นด้วย `fc_` (เช่น `fc_example1`), ไม่ใช่ `call_` |
| `missing_required_parameter: text.format.name` | เพิ่มคีย์ `"name"` ให้กับ dict รูปแบบ (เช่น `"name": "Output"`) |
| `invalid_type: text.format` | ตรวจสอบว่า `text.format` เป็น dict ที่มีคีย์ `type`, `name`, `strict`, `schema` — ไม่ใช่สตริง |
| `invalid input content type` | ใช้ชนิดเนื้อหา `input_text`/`output_text` แทน Chat `text` |
| `invalid input content type` (image) | ชนิดเนื้อหารูปภาพยังใช้ `"type": "image_url"` | เปลี่ยนเป็น `"type": "input_image"` |
| `Expected object, got string` บน `image_url` | `image_url` ยังคงเป็นอ็อบเจ็กต์ซ้อน `{"url": "..."}` | แบนฟอร์แมตเป็นสตริงธรรมดา: `"image_url": "https://..."` หรือ `"image_url": "data:image/...;base64,..."` |
| `integer below minimum value` สำหรับ `max_output_tokens` | ค่าขั้นต่ำคือ **16** บน Azure OpenAI ใช้ 50+ สำหรับการทดสอบ, 1000+ สำหรับใช้งานจริง |
| `429 Too Many Requests` ระหว่างสตรีมมิ่ง | ถูกจำกัดอัตรา ใช้ `try/except` ครอบการสตรีมมิ่ง, ส่ง JSON ข้อผิดพลาดไป frontend, ใช้กลไกหน่วง/ลองใหม่ |
| `KeyError: 'innererror'` บนข้อผิดพลาดตัวกรองเนื้อหา | โครงสร้างเนื้อหาข้อผิดพลาดใน API Responses เปลี่ยนแปลง | Chat Completions ใช้ `error.body["innererror"]["content_filter_result"]`; Responses API ใช้ `error.body["content_filters"][0]["content_filter_results"]` (พหูพจน์, อยู่ในอาร์เรย์). แก้ไขการเข้าถึง `innererror` ทั้งหมด. |

---

## ตารางความเสี่ยงการย้ายระบบ

| อาการ | ความผิดพลาดที่น่าจะเป็น | การแก้ไข |
|---------|---------------|-----|
| `output_text` ว่าง/ผลตอบกลับถูกตัด | `max_output_tokens` ต่ำเกินไปสำหรับโมเดล reasoning | ตั้งค่า `max_output_tokens=1000` หรือสูงกว่า — token reasoning นับรวมในขีดจำกัด |
| `400 invalid_type: text.format` | ส่ง `response_format` เป็นสตริงแทนที่จะเป็น dict `text.format` | ใช้ `text={"format": {"type": "json_schema", "name": "...", "strict": True, "schema": {...}}}` |
| `404 Not Found` บน `/openai/v1/responses` | `base_url` ผิด — ขาดส่วนต่อท้าย `/openai/v1/` | ตรวจสอบให้แน่ใจว่า `base_url=f"{endpoint}/openai/v1/"` (มี / ท้าย) |
| `401 Unauthorized` หลังเปลี่ยนเป็น `OpenAI()` | ไม่ตั้งค่า `api_key` หรือส่ง token provider ไม่ถูกต้อง | สำหรับ EntraID: `api_key=token_provider` (callable). สำหรับ API key: `api_key=os.environ["AZURE_OPENAI_API_KEY"]` |
| โมเดลส่ง `deployment not found` | พารามิเตอร์ `model` ไม่ตรงกับชื่อ deployment ของ Azure | ใช้ `model=os.environ["AZURE_OPENAI_DEPLOYMENT"]` — นี่คืชื่อ deployment ไม่ใช่ชื่อโมเดล |
| `json.loads(resp.output_text)` เกิด `JSONDecodeError` | ไม่มีการบังคับใช้ schema หรือโมเดลไม่รองรับ JSON เข้มงวด | ตั้งค่า `"strict": True` ใน schema และตรวจสอบว่าโมเดลรองรับ output แบบมีโครงสร้าง |
| สตรีมมิ่งไม่มี `delta` events | ตรวจสอบประเภท event ผิด | กรองด้วย `event.type == "response.output_text.delta"`, ไม่ใช่ `chat.completion.chunk` ของ Chat |
| ข้อผิดพลาด 400 บนภาพอินพุตหลังย้ายระบบ | ชนิดเนื้อหารูปภาพไม่อัปเดต | เปลี่ยน `"type": "image_url"` → `"type": "input_image"` และแบนฟอร์แมต `"image_url": {"url": "..."}` → `"image_url": "..."` (สตริงธรรมดา) |
| เครื่องมือเรียกวนลูปไม่สิ้นสุด | ขาดผลลัพธ์เครื่องมือในอินพุตคำขอถัดไป | หลังเรียกเครื่องมือ เพิ่มรายการ `{"type": "function_call_output", "call_id": ..., "output": ...}` ลงใน `input` ของคำขอถัดไป |
| ข้อผิดพลาด `temperature` กับ GPT-5 หรือ o-series | ค่า `temperature` ระบุชัดเจนไม่ใช่ 1 | ลบ `temperature` หรือกำหนดเป็น `1` สำหรับโมเดล GPT-5 และ o-series (o1, o3-mini, o3, o4-mini) |
| ข้อผิดพลาด `top_p` กับ o-series | `top_p` ไม่รองรับ | ลบ `top_p` เมื่อใช้โมเดล o-series |
| `max_completion_tokens` ไม่รู้จัก | ใช้พารามิเตอร์เฉพาะ Azure | แทนที่ `max_completion_tokens` ด้วย `max_output_tokens`. ตั้งค่าเป็น 4096+ สำหรับ o-series (token reasoning นับรวมในขีดจำกัด) |
| ผลลัพธ์ว่าง/ถูกตัดจาก o-series | `max_output_tokens` ต่ำเกินไป | o-series ใช้ token reasoning ภายใน ตั้งค่า `max_output_tokens=4096` หรือสูงกว่า — ไม่ใช่ 500–1000 |
| ข้อผิดพลาด 400 `integer_below_min_value` สำหรับ `max_output_tokens` | ค่าต่ำกว่า 16 | Azure OpenAI บังคับให้ `max_output_tokens >= 16`. ใช้ 50+ สำหรับทดสอบ, 1000+ สำหรับการใช้งานจริง |
| `429 Too Many Requests` กลางสตรีม | ถูกจำกัดอัตราโดย Azure OpenAI | สตรีมขาดอย่างเงียบๆ ไม่มีการจัดการข้อผิดพลาด ห่อ `async for event in await coroutine:` ด้วย `try/except` แล้วส่ง `{"error": str(e)}` ไป frontend |
| `AzureDeveloperCliCredential` → `CredentialUnavailableError` | ใช้ tenant ผิดหรือไม่ได้ล็อกอิน | ส่ง `tenant_id=os.getenv("AZURE_TENANT_ID")` ชัดเจน เรียก `azd auth login --tenant <tenant-id>` ในเครื่อง |
| `404 Not Found` เมื่อใช้ GitHub Models (`models.github.ai`) | GitHub Models ไม่รองรับ Responses API | ลบโค้ด GitHub Models ออก ใช้ Azure OpenAI, OpenAI, หรือ endpoint ท้องถิ่นที่รองรับ Responses (เช่น Ollama) |
| MAF `OpenAIChatCompletionClient` ยังใช้ Chat Completions | ใช้ไคลเอนต์ MAF แบบเก่าบน 1.0.0+ | ใน MAF 1.0.0+ `OpenAIChatClient` ใช้ Responses API โดยดีฟอลต์ แทนที่ `OpenAIChatCompletionClient` ด้วย `OpenAIChatClient`. สำหรับก่อน 1.0.0 ให้อัปเกรดเป็น `agent-framework-openai>=1.0.0` |
| ตัวแทน LangChain ส่งคืนว่างหรือผิดพลาดกับการเรียกเครื่องมือ | `ChatOpenAI` ไม่ใช้ Responses API | เพิ่ม `use_responses_api=True` ใน `ChatOpenAI(...)` และเปลี่ยน `.content` → `.text` ในข้อความตอบกลับ |
| `KeyError: 'innererror'` ในตัวจัดการข้อผิดพลาดตัวกรองเนื้อหา | โครงสร้างข้อผิดพลาดเปลี่ยนใน Responses API | แก้ไข `error.body["innererror"]["content_filter_result"]["jailbreak"]` → `error.body["content_filters"][0]["content_filter_results"]["jailbreak"]`. ตัวหุ้ม `innererror` หายไป; รายละเอียดตัวกรองเนื้อหาอยู่ในอาร์เรย์ท็อประดับ `content_filters` โดยมี `content_filter_results` (พหูพจน์) ในแต่ละรายการ |
| การเรียก HTTP ดิบที่ `/openai/deployments/.../chat/completions` คืน 404 | จุดสิ้นสุด REST Chat Completions แบบเก่า | แก้ไข URL เป็น `/openai/v1/responses`. เปลี่ยน body คำขอ: `messages` → `input`, เพิ่ม `max_output_tokens` + `store: false`, ลบพารามิเตอร์ query `api-version`. เปลี่ยนวิธีอ่านผลตอบกลับ: `choices[0].message.content` → `output[0].content[0].text` (หมายเหตุ: `output_text` เป็น convenience property ของ SDK, ไม่มีใน JSON ดิบ REST) |

---

## ข้อควรระวัง

1. ถ้าเคยใช้ Chat Completions สำหรับสถานะการสนทนา ให้จัดการสถานะของคุณเองอย่างชัดเจนด้วย Responses
2. ใช้ `max_output_tokens` แทน `max_tokens` แบบเดิม
3. เมื่อย้ายไป `gpt-5` ตรวจสอบว่าไม่ระบุหรือกำหนด `temperature` เป็น `1`
4. แทนที่ Chat `content[].type: "text"` ด้วย Responses `content[].type: "input_text"` สำหรับอินพุตผู้ใช้/ระบบ
5. สำหรับ `text.format`, ต้องให้ dict ที่ถูกต้อง (เช่น `{"type": "json_schema", "name": "Output", "schema": ..., "strict": True}`) ไม่ใช่สตริงธรรมดา
6. พารามิเตอร์ `seed` ไม่รองรับใน Responses; ลบออกจากคำขอ
7. **Reasoning**: รวม `reasoning` เฉพาะเมื่อโค้ดเดิมใช้เท่านั้น อย่าเพิ่ม `reasoning` ใน API ที่ไม่ได้ใช้ — โมเดลจำนวนมากที่ไม่ใช้ reasoning ไม่รองรับพารามิเตอร์นี้
8. **ขนาด `max_output_tokens`**: สำหรับโมเดล reasoning (GPT-5-mini, GPT-5, o-series), ใช้ `max_output_tokens=4096` หรือสูงกว่า — ไม่ใช่ 50–1000 โมเดลใช้ reasoning tokens ภายในก่อนสร้างผลลัพธ์ที่มองเห็น ขีดจำกัดต่ำเกินไปทำให้ผลลัพธ์ถูกตัดหรือว่างเปล่า
9. **o-series `max_completion_tokens`**: หากโค้ดเดิมใช้ `max_completion_tokens` (เฉพาะ Azure สำหรับ o-series), แทนที่ด้วย `max_output_tokens` Responses API ไม่ยอมรับ `max_completion_tokens`
10. **o-series `reasoning_effort`**: ถ้าโค้ดเดิมใช้ `reasoning_effort` (ต่ำ/กลาง/สูง), ย้ายไปใช้ `reasoning={"effort": "<value>"}` ในการเรียก Responses API
11. **ความล่าช้าสตรีมมิ่ง o-series**: โมเดล o-series ทำ reasoning ภายในก่อนสร้างผลลัพธ์ เมื่อสตรีมมิ่ง, คาดว่ามีความล่าช้านานขึ้นก่อน event แรก `response.output_text.delta` เป็นเรื่องปกติ — โมเดลกำลังทำ reasoning, ไม่ได้ค้าง
9. **`_azure_ad_token_provider` หายไป**: `AsyncOpenAI` / `OpenAI` ไม่มีแอตทริบิวต์ `_azure_ad_token_provider` การทดสอบหรือโค้ดที่เข้าถึงแอตทริบิวต์นี้จะล้มเหลวด้วย `AttributeError` ตัวจัดหาทoken ถูกส่งเป็น `api_key` และไม่สามารถตรวจสอบจากอ็อบเจ็กต์ไคลเอนต์ได้
10. **ไฟล์ Snapshot / golden**: ถ้าชุดทดสอบใช้ snapshot testing, **ไฟล์ snapshot ทั้งหมด** ที่มีรูปแบบสตรีมมิ่ง Chat Completions (`choices[0]`, `content_filter_results`, `function_call`, ฯลฯ) ต้องอัปเดตเป็นรูปแบบ Responses ใหม่ ง่ายที่จะพลาดและทำให้ทดสอบไม่ผ่าน
11. **เส้นทาง mock monkeypatch**: เปลี่ยนเป้าหมาย monkeypatch จาก `openai.resources.chat.AsyncCompletions.create` เป็น `openai.resources.responses.AsyncResponses.create` (หรือ `Responses.create` สำหรับ sync) การใช้เส้นทางเก่าเงียบ ๆ จะไม่ทำงาน — mock จะไม่ถูกดักจับ และทดสอบจะติดต่อ API จริงหรือผิดพลาด
12. **`input` ไม่ใช่ `messages`**: ฟังก์ชัน mock ต้องอ่าน `kwargs.get("input")` ไม่ใช่ `kwargs.get("messages")` Responses API ใช้ `input` สำหรับประวัติสนทนา
13. **ชื่อ environment variable**: Azure Identity SDK ใช้ `AZURE_CLIENT_ID` (ไม่ใช่ `AZURE_OPENAI_CLIENT_ID`) สำหรับ `ManagedIdentityCredential(client_id=...)` เปลี่ยนชื่อในทดสอบ, ไฟล์ `.env`, การตั้งค่าแอป และ Bicep/โครงสร้างพื้นฐาน
14. **ขั้นต่ำ `max_output_tokens` คือ 16**: Azure OpenAI ปฏิเสธค่าต่ำกว่า 16 ด้วยข้อผิดพลาด `400 integer_below_min_value` ใช้ 50 สำหรับทดสอบเบื้องต้น, 1000+ สำหรับใช้งานจริง `max_tokens` แบบเก่าไม่มีขั้นต่ำนี้
15. **`tenant_id` สำหรับ `AzureDeveloperCliCredential`**: เมื่อทรัพยากร Azure OpenAI อยู่ใน tenant อื่น, ต้องส่ง `tenant_id` ชัดเจน — `AzureDeveloperCliCredential(tenant_id=os.getenv("AZURE_TENANT_ID"))` หากไม่ส่ง ตัวรับรองจะใช้ tenant ผิดและคืน `401`
16. **ข้อจำกัดความเร็วแสดงผลต่างกันในสตรีมมิ่ง**: กับ Chat Completions, 429 มักจะทำให้ไม่เริ่มสตรีม กับ Responses API สตรีมมิ่ง, 429 อาจเกิด **กลางสตรีม** — ตัววนซ้ำ async จะโยนข้อผิดพลาด ห่อวงวนสตรีมด้วย `try/except` แล้วส่งบรรทัด JSON ข้อผิดพลาดเพื่อให้ frontend จัดการอย่างเหมาะสม

17. **การจัดการข้อผิดพลาดของการสตรีมเป็นสิ่งจำเป็นสำหรับเว็บแอป**: รูปแบบ `try: async for event in await coroutine: ... except Exception as e: yield json.dumps({"error": str(e)})` สำคัญมาก หากไม่มีรูปแบบนี้ สตรีม SSE/JSONL จะหยุดทำงานโดยเงียบ ๆ เมื่อเกิดข้อผิดพลาดที่ฝั่งเซิร์ฟเวอร์และหน้าฟรอนต์เอนด์จะค้าง
18. **นิยามเครื่องมือจะต้องใช้รูปแบบแบน**: Responses API คาดหวังรูปแบบ `{"type": "function", "name": ..., "parameters": ...}` — ไม่ใช่รูปแบบซ้อนของ Chat Completions ที่เป็น `{"type": "function", "function": {"name": ..., "parameters": ...}}` นี่คือข้อผิดพลาดที่พบบ่อยสุดเมื่อย้ายโค้ดฟังก์ชันเรียกใช้
19. **`pydantic_function_tool()` ไม่เข้ากัน**: helper `openai.pydantic_function_tool()` ยังคงสร้างรูปแบบซ้อนเดิมอยู่ อย่าใช้กับ `responses.create()` ให้กำหนดสกีมาเครื่องมือด้วยตนเองหรือแปลงผลลัพธ์ให้เป็นแบบแบน
20. **ผลลัพธ์ของเครื่องมือใช้ `function_call_output` ไม่ใช่ `role: tool`**: หลังเรียกใช้เครื่องมือ ให้เพิ่มข้อมูลเป็น `{"type": "function_call_output", "call_id": ..., "output": ...}` — ไม่ใช่ `{"role": "tool", "tool_call_id": ..., "content": ...}` สำหรับคำขอเครื่องมือของผู้ช่วย ใช้ `messages.extend(response.output)` — ไม่ใช่ dict แบบแมนนวล `{"role": "assistant", "tool_calls": [...]}` 
21. **`strict: true` ต้องใช้ `required` + `additionalProperties: false`**: เมื่อใช้ `strict: true` กับเครื่องมือ ทุกสมบัติต้องถูกระบุในอาร์เรย์ `required` และ `additionalProperties` ต้องตั้งค่าเป็น `false` หากขาดอย่างใดอย่างหนึ่งจะเกิดข้อผิดพลาด 400
22. **ID ของการเรียกฟังก์ชันมีคำนำหน้าที่เจาะจง**: เมื่อให้รายการ `function_call` แบบ few-shot ใน `input` ฟิลด์ `id` ต้องขึ้นต้นด้วย `fc_` และฟิลด์ `call_id` ต้องขึ้นต้นด้วย `call_` (เช่น `"id": "fc_example1", "call_id": "call_example1"`) การใช้คำนำหน้า `call_` ของ Chat Completions เดิมสำหรับ `id` จะถูกปฏิเสธ
23. **GitHub Models ไม่รองรับ Responses API**: หากแอปมีเส้นทางโค้ด GitHub Models (`base_url` ชี้ไปที่ `models.github.ai` หรือ `models.inference.ai.azure.com`) ให้ลบออกทั้งหมด ไม่มีเส้นทางย้ายข้อมูล — ให้เปลี่ยนไปใช้ Azure OpenAI, OpenAI หรือ endpoint ภายในที่เข้ากันได้แทน
24. **โครงสร้างเนื้อหาร่างข้อผิดพลาดตัวกรองเนื้อหาเปลี่ยนไป**: ข้อผิดพลาดของ Chat Completions ใช้ `error.body["innererror"]["content_filter_result"]` (เอกพจน์) ข้อผิดพลาด Responses API ใช้ `error.body["content_filters"][0]["content_filter_results"]` (พหูพจน์, อยู่ในอาร์เรย์) คีย์ `innererror` ไม่มีอยู่แล้ว โค้ดที่เข้าถึง `innererror` โดยตรงจะเกิด `KeyError` ในเวลารันไทม์ — ซึ่งง่ายต่อการพลาดตอนย้ายข้อมูลเพราะจะเกิดขึ้นเมื่อฟิลเตอร์ตัวกรองเนื้อหาทำงานเท่านั้น ให้ค้นหา `innererror` ในการย้ายข้อมูลเสมอ
25. **การเรียก HTTP ดิบต้องเขียน URL + body ใหม่**: แอปที่เรียก REST Azure OpenAI โดยตรง (ผ่าน `requests`, `httpx`, `aiohttp`) โดยใช้ `/openai/deployments/{name}/chat/completions?api-version=...` ต้องเปลี่ยนเป็น `/openai/v1/responses` ร่างคำขอใช้ `input` แทน `messages` ต้องส่ง `max_output_tokens` และ `store` และพารามิเตอร์ query `api-version` ถูกตัดออก ข้อความในร่างการตอบกลับอยู่ที่ `output[0].content[0].text` — **ไม่ใช่** `output_text` ซึ่งเป็น property สะดวกของ SDK ที่ไม่มีใน JSON REST ดิบ

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ปฏิเสธความรับผิดชอบ**:
เอกสารนี้ได้รับการแปลโดยใช้บริการแปลภาษา AI [Co-op Translator](https://github.com/Azure/co-op-translator) ขณะที่เราพยายามให้ความถูกต้อง โปรดทราบว่าการแปลโดยอัตโนมัติอาจมีข้อผิดพลาดหรือความไม่ถูกต้อง เอกสารต้นฉบับในภาษาต้นทางควรถูกพิจารณาเป็นแหล่งข้อมูลที่เชื่อถือได้ สำหรับข้อมูลที่สำคัญ แนะนำให้ใช้การแปลโดยมนุษย์มืออาชีพ เราไม่รับผิดชอบต่อความเข้าใจผิดหรือการตีความที่ผิดพลาดที่เกิดขึ้นจากการใช้การแปลนี้
<!-- CO-OP TRANSLATOR DISCLAIMER END -->