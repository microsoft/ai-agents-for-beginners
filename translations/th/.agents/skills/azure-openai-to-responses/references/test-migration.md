# การย้ายโครงสร้างพื้นฐานสำหรับการทดสอบ

เมื่อย้ายฐานโค้ดจาก Chat Completions ไปยัง Responses API **การทดสอบจะล้มเหลวในรูปแบบที่คาดเดาได้** บทอ้างอิงนี้ครอบคลุมสิ่งที่ต้องแก้ไข

---

## การจำลองการสตรีมตอบกลับ (Python pytest)

### คลาสจำลองหลัก

```python
class MockResponseEvent:
    """Simulates a Responses API streaming event."""
    def __init__(self, event_type: str, delta: str | None = None):
        self.type = event_type
        self.delta = delta

class AsyncResponseIterator:
    """Async iterator that yields Responses API streaming events from a string answer."""
    def __init__(self, answer: str):
        self.event_index = 0
        self.events = []
        for i, word in enumerate(answer.split(" ")):
            # รักษาช่องว่าง: เพิ่มช่องว่างหน้าแต่ละคำยกเว้นคำแรก
            if i > 0:
                word = " " + word
            self.events.append(MockResponseEvent("response.output_text.delta", delta=word))
        self.events.append(MockResponseEvent("response.completed"))

    def __aiter__(self):
        return self

    async def __anext__(self):
        if self.event_index < len(self.events):
            event = self.events[self.event_index]
            self.event_index += 1
            return event
        raise StopAsyncIteration
```

### ส่งต่อการตอบกลับจำลองตามเนื้อหาข้อความ

แอปจริงให้คำตอบที่แตกต่างกันตามคำสั่ง ส่งต่อโดยใช้ `input` (ไม่ใช่ `messages`):

```python
async def mock_acreate(*args, **kwargs):
    # Responses API ใช้ 'input' ไม่ใช่ 'messages'
    last_message = kwargs.get("input", [])[-1]["content"]
    if last_message == "What is the capital of France?":
        return AsyncResponseIterator("The capital of France is Paris.")
    elif last_message == "What is the capital of Germany?":
        return AsyncResponseIterator("The capital of Germany is Berlin.")
    else:
        raise ValueError(f"Unexpected message: {last_message}")
```

### เส้นทาง Monkeypatch

| ประเภทไคลเอนต์ | เส้นทาง Monkeypatch |
|-------------|------------------|
| `AsyncOpenAI` | `openai.resources.responses.AsyncResponses.create` |
| `OpenAI` (ซิงค์) | `openai.resources.responses.Responses.create` |

> **ก่อนหน้า** (Chat Completions): `openai.resources.chat.AsyncCompletions.create`  
> **หลัง** (Responses): `openai.resources.responses.AsyncResponses.create`

### ตัวอย่าง fixture เต็ม

```python
@pytest.fixture
def mock_openai_responses(monkeypatch):
    # ... คลาส MockResponseEvent และ AsyncResponseIterator ที่นี่ ...

    async def mock_acreate(*args, **kwargs):
        last_message = kwargs.get("input", [])[-1]["content"]
        if last_message == "What is the capital of France?":
            return AsyncResponseIterator("The capital of France is Paris.")
        else:
            raise ValueError(f"Unexpected message: {last_message}")

    monkeypatch.setattr("openai.resources.responses.AsyncResponses.create", mock_acreate)
```

---

## 1. อัปเดต mock fixtures

แทนที่ mock ที่ใช้ `ChatCompletionChunk` ด้วยรูปแบบ `MockResponseEvent` / `AsyncResponseIterator` ข้างต้น การเปลี่ยนแปลงสำคัญ:

| ก่อนหน้า (mock Chat Completions) | หลัง (mock Responses) |
|-------------------------------|------------------------|
| `openai.types.chat.ChatCompletionChunk(...)` | `MockResponseEvent(event_type, delta)` |
| `choices[0].delta.content` | `event.delta` |
| `finish_reason="stop"` ใน chunk | `event.type == "response.completed"` |
| chunk `prompt_filter_results` เฉพาะ Azure | ลบออกทั้งหมด |
| `content_filter_results` ต่อ choice เฉพาะ Azure | ลบออกทั้งหมด |
| `kwargs.get("messages")` ใน mock | `kwargs.get("input")` ใน mock |

---

## 2. อัปเดต snapshot / ไฟล์ทอง

หากชุดทดสอบใช้ snapshot testing (เช่น `pytest-snapshot`, syrupy, หรือ snapshot JSONL แบบสร้างเอง) รูปแบบเอาต์พุตที่คาดหวังเปลี่ยนไป:

**ก่อนหน้า** (JSONL สตรีมมิ่ง Chat Completions):  
```jsonl
{"delta": {"content": null, "function_call": null, "refusal": null, "role": "assistant", "tool_calls": null}, "finish_reason": null, "index": 0, "logprobs": null, "content_filter_results": {}}
{"delta": {"content": "The", "function_call": null, "refusal": null, "role": null, "tool_calls": null}, "finish_reason": null, "index": 0, "logprobs": null, "content_filter_results": {"hate": {"filtered": false, "severity": "safe"}, ...}}
{"delta": {"content": null, ...}, "finish_reason": "stop", "index": 0, "logprobs": null, "content_filter_results": {}}
```
  
**หลัง** (JSONL สตรีมมิ่ง Responses API):  
```jsonl
{"delta": {"content": "The"}}
{"delta": {"content": " capital"}}
{"delta": {"content": null}, "finish_reason": "stop"}
```
  
รูปแบบใหม่เรียบง่ายมาก — ไม่มีฟิลด์ `function_call`, `refusal`, `role`, `tool_calls`, `index`, `logprobs`, หรือ `content_filter_results` อัปเดตหรือสร้างใหม่ไฟล์ snapshot ทั้งหมด

> **เคล็ดลับ**: รันการทดสอบพร้อม `--snapshot-update` (pytest-snapshot) หรือ `--update-snapshots` (syrupy) หลังย้ายเพื่อสร้างไฟล์ snapshot อัตโนมัติใหม่

---

## 3. อัปเดตการตรวจสอบผลการทดสอบ

การตรวจสอบผลที่พบบ่อยว่าล้มเหลว:

| การตรวจสอบเก่า | ปัญหา | การตรวจสอบใหม่ |
|--------------|---------|---------------|
| `client._azure_ad_token_provider is not None` | `AsyncOpenAI` ไม่มีแอตทริบิวต์ `_azure_ad_token_provider` | `isinstance(client, AsyncOpenAI)` และ `"/openai/v1/" in str(client.base_url)` |
| `client.api_version == "2024-..."` | ไม่มี `api_version` บน `OpenAI`/`AsyncOpenAI` | ลบออกทั้งหมด |
| `isinstance(client, AsyncAzureOpenAI)` | ประเภทไคลเอนต์เปลี่ยน | `isinstance(client, AsyncOpenAI)` |

---

## 4. อัปเดตตัวแปรสิ่งแวดล้อมใน test fixtures

การทดสอบมักตั้งค่า env vars ผ่าน `monkeypatch.setenv` อัปเดตดังนี้:

| ตัวแปร env เก่า | ตัวแปร env ใหม่ | หมายเหตุ |
|-------------|-------------|-------|
| `AZURE_OPENAI_CLIENT_ID` | `AZURE_CLIENT_ID` | ตามคอนเวนชันของ Azure Identity SDK |
| `AZURE_OPENAI_VERSION` | ลบออก | ไม่ต้องการ `api_version` |
| `AZURE_OPENAI_API_VERSION` | ลบออก | ไม่ต้องการ `api_version` |
| `AZURE_OPENAI_ENDPOINT` | `AZURE_OPENAI_ENDPOINT` | เก็บไว้ (ยังคงต้องใช้สำหรับ `base_url`) |
| `AZURE_OPENAI_CHAT_DEPLOYMENT` | `AZURE_OPENAI_CHAT_DEPLOYMENT` | เก็บไว้ (ชื่อ deployment สำหรับพารามิเตอร์ `model`) |

---

## 5. ค้นหาซอร์สโค้ดการทดสอบที่ต้องย้าย

```bash
# แบบแผนเก่าที่เฉพาะเจาะจงสำหรับการทดสอบ
rg "ChatCompletionChunk" tests/
rg "AsyncCompletions\.create" tests/
rg "chat\.completions" tests/
rg "_azure_ad_token_provider" tests/
rg "prompt_filter_results" tests/
rg "content_filter_results" tests/
rg "AZURE_OPENAI_VERSION|AZURE_OPENAI_API_VERSION" tests/
rg "AZURE_OPENAI_CLIENT_ID" tests/
```

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ปฏิเสธความรับผิดชอบ**:
เอกสารนี้ได้รับการแปลโดยใช้บริการแปลภาษา AI [Co-op Translator](https://github.com/Azure/co-op-translator) ขณะที่เราพยายามให้ความถูกต้อง โปรดทราบว่าการแปลโดยอัตโนมัติอาจมีข้อผิดพลาดหรือความไม่ถูกต้อง เอกสารต้นฉบับในภาษาต้นทางควรถูกพิจารณาเป็นแหล่งข้อมูลที่เชื่อถือได้ สำหรับข้อมูลที่สำคัญ แนะนำให้ใช้การแปลโดยมนุษย์มืออาชีพ เราไม่รับผิดชอบต่อความเข้าใจผิดหรือการตีความที่ผิดพลาดที่เกิดขึ้นจากการใช้การแปลนี้
<!-- CO-OP TRANSLATOR DISCLAIMER END -->