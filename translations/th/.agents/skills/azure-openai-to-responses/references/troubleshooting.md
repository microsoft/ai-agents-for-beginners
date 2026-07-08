# การแก้ไขปัญหา, ตารางความเสี่ยง & ข้อควรระวัง

## การแก้ไขปัญหา 400s

| ข้อผิดพลาด | การแก้ไข |
|-------|-----|
| `missing_required_parameter: tools[0].name` | นิยามเครื่องมือใช้รูปแบบซ้อน Chat Completions แบบเก่า | เปลี่ยนจาก `{"type": "function", "function": {"name": ...}}` เป็น `{"type": "function", "name": ..., "parameters": ...}` — ชื่อ, คำอธิบาย, พารามิเตอร์ย้ายไปที่ระดับบนสุด |
| `unknown_parameter: input[N].tool_calls` | ผลลัพธ์เครื่องมือแบบหลายรอบใช้รูปแบบ Chat Completions แบบเก่า | แทนที่ `{"role": "assistant", "tool_calls": [...]}` + `{"role": "tool", ...}` ด้วย รายการ `response.output` + `{"type": "function_call_output", "call_id": ..., "output": ...}` |
| `invalid_function_parameters: 'required' is required` | เครื่องมือที่ `strict: true` ขาดอาร์เรย์ `required` | เมื่อ `strict: true` คุณสมบัติทั้งหมดต้องถูกระบุใน `required` และต้องตั้งค่า `additionalProperties: false` |
| `invalid_function_parameters: 'additionalProperties' is required` | เครื่องมือที่ `strict: true` ขาด `additionalProperties: false` | เพิ่ม `"additionalProperties": false` ในอ็อบเจ็กต์พารามิเตอร์ |
| `invalid input[N].id: Expected an ID that begins with 'fc'` | ID ฟังก์ชัน call แบบ few-shot ใช้ prefix ผิด | ID ของฟังก์ชัน call ต้องขึ้นต้นด้วย `fc_` (เช่น `fc_example1`) ไม่ใช่ `call_` |
| `missing_required_parameter: text.format.name` | เพิ่มคีย์ `"name"` ให้กับ dict รูปแบบ (เช่น `"name": "Output"`) |
| `invalid_type: text.format` | ตรวจสอบให้แน่ใจว่า `text.format` เป็น dict ที่มีคีย์ `type`, `name`, `strict`, `schema` — ไม่ใช่สตริง |
| `invalid input content type` | ใช้ชนิดเนื้อหา `input_text`/`output_text` แทน Chat `text` |
| `invalid input content type` (image) | เนื้อหาภาพยังใช้ `"type": "image_url"` | เปลี่ยนเป็น `"type": "input_image"` |
| `Expected object, got string` บน `image_url` | `image_url` ยังเป็นอ็อบเจ็กต์ซ้อน `{"url": "..."}` | เปลี่ยนเป็นสตริงธรรมดา: `"image_url": "https://..."` หรือ `"image_url": "data:image/...;base64,..."` |
| `integer below minimum value` สำหรับ `max_output_tokens` | ค่าต่ำสุดคือ **16** บน Azure OpenAI ใช้ 50+ สำหรับทดสอบ, 1000+ สำหรับใช้งานจริง |
| `429 Too Many Requests` ระหว่างสตรีมมิ่ง | ถูกจำกัดอัตรา ให้ใช้ `try/except` ครอบการสตรีมมิ่ง, ส่งคืน JSON ข้อผิดพลาดไปยัง frontend, ใช้ backoff/retry |
| `KeyError: 'innererror'` เมื่อเกิดข้อผิดพลาดตัวกรองเนื้อหา | โครงสร้างร่างข้อผิดพลาดตัวกรองเนื้อหาเปลี่ยนใน Responses API | Chat Completions ใช้ `error.body["innererror"]["content_filter_result"]`; Responses API ใช้ `error.body["content_filters"][0]["content_filter_results"]` (พหูพจน์, อยู่ในอาร์เรย์) ปรับโค้ดที่เข้าถึง `innererror` ทั้งหมด |

---

## ตารางความเสี่ยงในการย้ายระบบ

| อาการ | ความผิดพลาดที่น่าจะเกิดขึ้น | การแก้ไข |
|---------|---------------|-----|
| `output_text` ว่างเปล่า / ตอบกลับถูกตัด | `max_output_tokens` ต่ำเกินไปสำหรับโมเดล reasoning | ตั้งค่า `max_output_tokens=1000` ขึ้นไป — โทเค็น reasoning ถูกนับรวมในขีดจำกัด |
| `400 invalid_type: text.format` | ส่ง `response_format` เป็นสตริงแทนการเป็น dict `text.format` | ใช้ `text={"format": {"type": "json_schema", "name": "...", "strict": True, "schema": {...}}}` |
| `404 Not Found` บน `/openai/v1/responses` | `base_url` ผิดพลาด — ขาด `/openai/v1/` ที่ท้าย | ตรวจสอบว่า `base_url=f"{endpoint}/openai/v1/"` (มี / ท้าย) |
| `401 Unauthorized` หลังเปลี่ยนไปใช้ `OpenAI()` | `api_key` ไม่ถูกตั้งหรือส่ง token provider ไม่ถูกต้อง | สำหรับ EntraID: `api_key=token_provider` (เป็น callable) สำหรับ API key: `api_key=os.environ["AZURE_OPENAI_API_KEY"]` |
| โมเดลส่งกลับ `deployment not found` | พารามิเตอร์ `model` ไม่ตรงกับชื่อ deployment Azure ของคุณ | ใช้ `model=os.environ["AZURE_OPENAI_DEPLOYMENT"]` — ชื่อนี้คือชื่อ deployment ไม่ใช่ชื่อโมเดล |
| `json.loads(resp.output_text)` เกิดข้อผิดพลาด `JSONDecodeError` | ไม่บังคับ schema หรือโมเดลไม่รองรับ JSON ที่เข้มงวด | ตรวจสอบให้แน่ใจว่า `"strict": True` อยู่ใน schema และโมเดลรองรับ structured output |
| ไม่มีเหตุการณ์ `delta` เมื่อสตรีมมิ่ง | ตรวจสอบประเภทเหตุการณ์ผิด | กรองโดย `event.type == "response.output_text.delta"` ไม่ใช่ `chat.completion.chunk` ของ Chat |
| `400` เมื่อป้อนภาพหลังจากย้ายระบบ | ชนิดเนื้อหาภาพไม่อัปเดต | เปลี่ยน `"type": "image_url"` → `"type": "input_image"` และแปลง `"image_url": {"url": "..."}` → `"image_url": "..."` (สตริงธรรมดา) |
| เครื่องมือเรียกวนลูปไม่สิ้นสุด | ขาดผลลัพธ์ของเครื่องมือใน `input` ต่อไป | หลังเรียกใช้เครื่องมือ ให้เพิ่มรายการ `{"type": "function_call_output", "call_id": ..., "output": ...}` เข้าไปใน `input` ในคำร้องขอถัดไป |
| ข้อผิดพลาด `temperature` กับ GPT-5 หรือ o-series | ค่า `temperature` กำหนดชัดเจนไม่ใช่ 1 | ลบ `temperature` หรือกำหนดเป็น `1` สำหรับ GPT-5 และ o-series (o1, o3-mini, o3, o4-mini) |
| ข้อผิดพลาด `top_p` กับ o-series | `top_p` ไม่รองรับ | ลบ `top_p` เมื่อใช้โมเดล o-series |
| `max_completion_tokens` ไม่ถูกจดจำ | ใช้พารามิเตอร์เฉพาะ Azure | แทนที่ด้วย `max_output_tokens` ตั้งเป็น 4096+ สำหรับ o-series (โทเค็น reasoning ถูกนับรวม) |
| ผลลัพธ์ว่างเปล่า/ถูกตัดจาก o-series | `max_output_tokens` ต่ำเกินไป | o-series ใช้โทเค็น reasoning ภายใน ตั้ง `max_output_tokens=4096` หรือสูงกว่า — ไม่ใช่ 500–1000 |
| `400 integer_below_min_value` สำหรับ `max_output_tokens` | ค่าต่ำกว่า 16 | Azure OpenAI บังคับ `max_output_tokens >= 16` ใช้ 50+ สำหรับทดสอบเป็นเบื้องต้น, 1000+ สำหรับใช้งานจริง |
| `429 Too Many Requests` กลางสตรีม | ถูกจำกัดโดย Azure OpenAI | สตรีมขาดโดยไม่มีการแจ้งข้อผิดพลาดเสมอ ห่อรอบ `async for event in await coroutine:` ด้วย `try/except` และส่ง `{"error": str(e)}` ไปยัง frontend |
| `AzureDeveloperCliCredential` → `CredentialUnavailableError` | เทนแนนต์ผิดหรือไม่ได้ล็อกอิน | ใส่ `tenant_id=os.getenv("AZURE_TENANT_ID")` อย่างชัดเจน รัน `azd auth login --tenant <tenant-id>` ในเครื่อง |
| `404 Not Found` ใช้ GitHub Models (`models.github.ai`) | GitHub Models ไม่รองรับ Responses API | ลบเส้นทางโค้ด GitHub Models ใช้ Azure OpenAI, OpenAI หรือ endpoint ในเครื่องที่เข้ากันได้ (เช่น Ollama ที่รองรับ Responses) |
| MAF `OpenAIChatCompletionClient` ยังใช้ Chat Completions | ใช้ไคลเอนต์ MAF รุ่นเก่าใน 1.0.0+ | ใน MAF 1.0.0+ `OpenAIChatClient` ใช้ Responses API ตามค่าเริ่มต้น แทนที่ `OpenAIChatCompletionClient` ด้วย `OpenAIChatClient` สำหรับรุ่นก่อน 1.0.0 ให้อัปเกรดเป็น `agent-framework-openai>=1.0.0` |
| ตัวแทน LangChain คืนค่าว่างหรือล้มเหลวกับการเรียกเครื่องมือ | `ChatOpenAI` ไม่ใช้ Responses API | เพิ่ม `use_responses_api=True` ใน `ChatOpenAI(...)` และเปลี่ยน `.content` เป็น `.text` บนข้อความตอบกลับ |
| `KeyError: 'innererror'` ในตัวจัดการข้อผิดพลาดตัวกรองเนื้อหา | โครงสร้างร่างข้อผิดพลาดเปลี่ยนใน Responses API | เขียนใหม่จาก `error.body["innererror"]["content_filter_result"]["jailbreak"]` เป็น `error.body["content_filters"][0]["content_filter_results"]["jailbreak"]` ตัวห่อ `innererror` หายไป รายละเอียดตัวกรองเนื้อหาอยู่ในอาร์เรย์ top-level `content_filters` พร้อม `content_filter_results` (พหูพจน์) ภายในแต่ละรายการ |
| เรียก HTTP ดิบไปที่ `/openai/deployments/.../chat/completions` คืน 404 | ใช้ REST endpoint Chat Completions แบบเก่า | เปลี่ยน URL เป็น `/openai/v1/responses` เปลี่ยน body คำขอ: `messages` → `input`, เพิ่ม `max_output_tokens` + `store: false`, ลบ query param `api-version` เปลี่ยนการแยกวิเคราะห์คำตอบ: `choices[0].message.content` → `output[0].content[0].text` (หมายเหตุ: `output_text` เป็น property สะดวกของ SDK ไม่อยู่ใน JSON REST ดิบ) |

---

## ข้อควรระวัง

1. ถ้าเคยใช้ Chat Completions เพื่อสถานะการสนทนา ให้จัดการสถานะของคุณเองอย่างชัดเจนด้วย Responses
2. ใช้ `max_output_tokens` แทน `max_tokens` แบบเก่า
3. เมื่อย้ายไปใช้ `gpt-5` ตรวจสอบว่าไม่ได้ระบุหรือกำหนด `temperature` เป็น `1`
4. แทนที่ Chat `content[].type: "text"` ด้วย Responses `content[].type: "input_text"` สำหรับข้อมูลผู้ใช้/ระบบ
5. สำหรับ `text.format` ให้ส่ง dict ที่ถูกต้อง (เช่น `{"type": "json_schema", "name": "Output", "schema": ..., "strict": True}`) ไม่ใช่สตริงธรรมดา
6. พารามิเตอร์ `seed` ไม่รองรับใน Responses ให้ลบออกจากคำขอ
7. **Reasoning**: ใส่ `reasoning` ก็ต่อเมื่อโค้ดเดิมมีใช้งานเท่านั้น อย่าเพิ่ม `reasoning` ในการเรียก API ที่ไม่เคยมี เนื่องจากโมเดลหลายตัว (เช่น gpt-4o-mini) ไม่รองรับพารามิเตอร์นี้
8. **ขนาดของ `max_output_tokens`**: สำหรับโมเดล reasoning (GPT-5-mini, GPT-5, o-series) ใช้ `max_output_tokens=4096` หรือสูงกว่า — ไม่ใช่ 50–1000 โมเดลใช้โทเค็น reasoning ภายในก่อนสร้างผลลัพธ์ที่มองเห็นได้ ขีดจำกัดต่ำเกินไปจะทำให้ตอบกลับถูกตัดหรือว่างเปล่า
9. **`max_completion_tokens` สำหรับ o-series**: ถ้าโค้ดเดิมใช้ `max_completion_tokens` (เฉพาะ Azure สำหรับ o-series) ให้แทนที่ด้วย `max_output_tokens` Responses API ไม่รับ `max_completion_tokens`
10. **`reasoning_effort` สำหรับ o-series**: ถ้าโค้ดเดิมใช้ `reasoning_effort` (ต่ำ/กลาง/สูง) ให้ย้ายเป็น `reasoning={"effort": "<value>"}` ในการเรียก Responses API
11. **ความหน่วงเวลาสตรีมมิ่งของ o-series**: โมเดล o-series ทำ reasoning ภายในก่อนสร้างผลลัพธ์ เมื่อสตรีมมิ่ง คาดว่าจะหน่วงเวลานานก่อนเหตุการณ์ `response.output_text.delta` แรก นี่เป็นเรื่องปกติ — โมเดลกำลัง reasoning ไม่ได้หยุดทำงาน
9. **`_azure_ad_token_provider` ถูกถอดออกแล้ว**: `AsyncOpenAI` / `OpenAI` ไม่มีแอตทริบิวต์ `_azure_ad_token_provider` การทดสอบหรือโค้ดที่เข้าถึงแอตทริบิวต์นี้จะล้มเหลวด้วย `AttributeError` โทเค็น provider จะถูกส่งผ่านเป็น `api_key` และไม่สามารถตรวจสอบได้จากไคลเอนต์
10. **ไฟล์ Snapshot / golden**: ถ้าชุดทดสอบใช้ snapshot testing **ทุก** ไฟล์ snapshot ที่มีรูปแบบ streaming ของ Chat Completions (`choices[0]`, `content_filter_results`, `function_call` ฯลฯ) ต้องอัปเดตให้เป็นรูปแบบ Responses ใหม่ ซึ่งง่ายที่จะพลาดและทำให้ Assertion ของ snapshot ผิดพลาด
11. **เส้นทาง monkeypatch สำหรับ mock**: เส้นทางเปลี่ยนจาก `openai.resources.chat.AsyncCompletions.create` → `openai.resources.responses.AsyncResponses.create` (หรือ `Responses.create` สำหรับซิงค์) ใช้เส้นทางเก่าจะไม่ทำงานอย่างเงียบ ๆ — mock จะไม่จับ และการทดสอบจะใช้ API จริงหรือล้มเหลว
12. **`input` ไม่ใช่ `messages`**: ฟังก์ชัน mock ต้องอ่าน `kwargs.get("input")` ไม่ใช่ `kwargs.get("messages")` Responses API ใช้ `input` สำหรับประวัติการสนทนา
13. **การตั้งชื่อตัวแปรแวดล้อม**: Azure Identity SDK ใช้ `AZURE_CLIENT_ID` (ไม่ใช่ `AZURE_OPENAI_CLIENT_ID`) สำหรับ `ManagedIdentityCredential(client_id=...)` ให้เปลี่ยนชื่อในทดสอบ, ไฟล์ `.env`, การตั้งค่าแอป และ Bicep/โครงสร้างพื้นฐาน
14. **ค่าต่ำสุดของ `max_output_tokens` คือ 16**: Azure OpenAI ปฏิเสธค่าน้อยกว่า 16 ด้วย `400 integer_below_min_value` ใช้ 50 สำหรับทดสอบเบื้องต้น, 1000+ สำหรับใช้งานจริง `max_tokens` แบบเก่าไม่มีขั้นต่ำนี้
15. **`tenant_id` สำหรับ `AzureDeveloperCliCredential`**: เมื่อทรัพยากร Azure OpenAI อยู่ในเทนแนนต์ต่าง ให้ต้องส่ง `tenant_id` อย่างชัดเจน — `AzureDeveloperCliCredential(tenant_id=os.getenv("AZURE_TENANT_ID"))` หากไม่ใส่ จะใช้เทนแนนต์ผิดโดยเงียบ ๆ และส่งกลับ `401`
16. **อัตราจำกัดปรากฏต่างกันในสตรีมมิ่ง**: กับ Chat Completions รหัส 429 จะป้องกันไม่ให้สตรีมเริ่มต้นได้ แต่กับ Responses API สตรีมมิ่ง รหัส 429 อาจเกิดขึ้น **กลางสตรีม** — ตัววนซ้ำแบบ async จะโยนข้อผิดพลาดเสมอ ให้ห่อวงวนสตรีมมิ่งด้วย `try/except` และส่งบรรทัด JSON แสดงข้อผิดพลาดเพื่อให้ frontend จัดการได้อย่างเหมาะสม
17. **การจัดการข้อผิดพลาดแบบสตรีมมิงเป็นสิ่งจำเป็นสำหรับเว็บแอป**: รูปแบบ `try: async for event in await coroutine: ... except Exception as e: yield json.dumps({"error": str(e)})` มีความสำคัญอย่างยิ่ง หากไม่มีรูปแบบนี้ สตรีม SSE/JSONL จะหยุดทำงานอย่างเงียบๆ เมื่อเกิดข้อผิดพลาดฝั่งเซิร์ฟเวอร์ และหน้าเว็บจะค้าง
18. **คำจำกัดความของเครื่องมือจะต้องใช้รูปแบบแบน**: Responses API คาดหวัง `{"type": "function", "name": ..., "parameters": ...}` — ไม่ใช่ `{"type": "function", "function": {"name": ..., "parameters": ...}}` ซึ่งเป็นรูปแบบซ้อนกันของ Chat Completions นี่เป็นข้อผิดพลาดการย้ายที่พบบ่อยที่สุดสำหรับโค้ดการเรียกฟังก์ชัน
19. **`pydantic_function_tool()` ไม่เข้ากัน**: ตัวช่วย `openai.pydantic_function_tool()` ยังคงสร้างรูปแบบเก่าที่ซ้อนกัน ห้ามใช้กับ `responses.create()` ให้กำหนดสคีมาของเครื่องมือด้วยตัวเองหรือแปลงผลลัพธ์ให้เป็นแบบแบน
20. **ผลลัพธ์ของเครื่องมือใช้ `function_call_output` ไม่ใช่ `role: tool`**: หลังจากเรียกใช้เครื่องมือ ให้เพิ่ม `{"type": "function_call_output", "call_id": ..., "output": ...}` — ไม่ใช่ `{"role": "tool", "tool_call_id": ..., "content": ...}` สำหรับการร้องขอเครื่องมือของผู้ช่วย ให้ใช้ `messages.extend(response.output)` — ไม่ใช่ดิกชันนารีแบบแมนนวล `{"role": "assistant", "tool_calls": [...]}`  
21. **`strict: true` ต้องใช้ `required` + `additionalProperties: false`**: เมื่อใช้ `strict: true` กับเครื่องมือ ทุกคุณสมบัติต้องถูกระบุในอาร์เรย์ `required` และ `additionalProperties` ต้องเป็น `false` หากขาดอย่างใดอย่างหนึ่ง จะทำให้เกิดข้อผิดพลาด 400
22. **ID การเรียกฟังก์ชันมีคำนำหน้าที่เฉพาะเจาะจง**: เมื่อให้รายการ `function_call` แบบ few-shot ใน `input` ฟิลด์ `id` ต้องขึ้นต้นด้วย `fc_` และฟิลด์ `call_id` ต้องขึ้นต้นด้วย `call_` (เช่น `"id": "fc_example1", "call_id": "call_example1"`) การใช้คำนำหน้า `call_` ที่เก่าของ Chat Completions สำหรับ `id` จะไม่ได้รับการยอมรับ
23. **GitHub Models ไม่รองรับ Responses API**: หากแอปมีเส้นทางโค้ด GitHub Models (`base_url` ชี้ไปที่ `models.github.ai` หรือ `models.inference.ai.azure.com`) ให้ลบออกทั้งหมด ไม่มีเส้นทางการย้ายข้อมูล — ให้เปลี่ยนไปใช้ Azure OpenAI, OpenAI หรือ endpoint ในเครื่องที่เข้ากันได้
24. **โครงสร้างร่างเนื้อหาของข้อผิดพลาดตัวกรองเนื้อหาเปลี่ยนไป**: ข้อผิดพลาดของ Chat Completions ใช้ `error.body["innererror"]["content_filter_result"]` (พหูพจน์) ข้อผิดพลาด Responses API ใช้ `error.body["content_filters"][0]["content_filter_results"]` (พหูพจน์ อยู่ในอาร์เรย์) ไม่มีคีย์ `innererror` อีกต่อไป โค้ดที่เข้าถึง `innererror` ตรงๆ จะทำให้เกิด `KeyError` ในเวลารัน — ซึ่งสังเกตได้ยากขณะย้ายข้อมูลเพราะปรากฏเฉพาะเมื่อฟิลเตอร์เนื้อหาทำงานจริง ให้ค้นหา `innererror` เสมอในระหว่างการย้ายข้อมูล
25. **การเรียก HTTP ดิบต้องแก้ไข URL + ร่างคำขอ**: แอปที่เรียก Azure OpenAI REST โดยตรง (ผ่าน `requests`, `httpx`, `aiohttp`) ใช้ `/openai/deployments/{name}/chat/completions?api-version=...` ต้องเปลี่ยนไปใช้ `/openai/v1/responses` ร่างคำขอใช้ `input` แทน `messages` ต้องมี `max_output_tokens` และ `store` และไม่ต้องใช้พารามิเตอร์ query `api-version` ข้อความในร่างคำตอบอยู่ที่ `output[0].content[0].text` — **ไม่ใช่** `output_text` ซึ่งเป็นสมบัติความสะดวกของ SDK ที่ไม่มีใน JSON REST ดิบ

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ปฏิเสธความรับผิดชอบ**:
เอกสารนี้ได้รับการแปลโดยใช้บริการแปลภาษา AI [Co-op Translator](https://github.com/Azure/co-op-translator) ขณะที่เราพยายามให้ความถูกต้อง โปรดทราบว่าการแปลโดยอัตโนมัติอาจมีข้อผิดพลาดหรือความไม่ถูกต้อง เอกสารต้นฉบับในภาษาต้นทางควรถูกพิจารณาเป็นแหล่งข้อมูลที่เชื่อถือได้ สำหรับข้อมูลที่สำคัญ แนะนำให้ใช้การแปลโดยมนุษย์มืออาชีพ เราไม่รับผิดชอบต่อความเข้าใจผิดหรือการตีความที่ผิดพลาดที่เกิดขึ้นจากการใช้การแปลนี้
<!-- CO-OP TRANSLATOR DISCLAIMER END -->