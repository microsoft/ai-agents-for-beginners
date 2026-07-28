# ใบช่วยจำ Responses API (Python + Azure OpenAI)

> ตัวอย่างทั้งหมดด้านล่างนี้สมมติว่า `deployment = os.environ["AZURE_OPENAI_DEPLOYMENT"]` และ `client` ได้ถูกกำหนดค่าไว้แล้ว (ดูการตั้งค่า client)

## คำขอพื้นฐาน
```python
resp = client.responses.create(
    model=deployment,
    input="Hello",
    max_output_tokens=1000,
    store=False,
)
print(resp.output_text)
```

## การตั้งค่า client — EntraID (แนะนำ)
```python
import os
from azure.identity import DefaultAzureCredential, get_bearer_token_provider
from openai import OpenAI

token_provider = get_bearer_token_provider(
    DefaultAzureCredential(),
    "https://cognitiveservices.azure.com/.default"
)

client = OpenAI(
    base_url=f"{os.environ['AZURE_OPENAI_ENDPOINT'].rstrip('/')}/openai/v1/",
    api_key=token_provider,
)
```

## การตั้งค่า client — คีย์ API
```python
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ["AZURE_OPENAI_API_KEY"],
    base_url=f"{os.environ['AZURE_OPENAI_ENDPOINT'].rstrip('/')}/openai/v1/",
)
```

## การตั้งค่า async client — EntraID
```python
import os
from azure.identity import DefaultAzureCredential, get_bearer_token_provider
from openai import AsyncOpenAI

token_provider = get_bearer_token_provider(
    DefaultAzureCredential(),
    "https://cognitiveservices.azure.com/.default"
)

client = AsyncOpenAI(
    base_url=f"{os.environ['AZURE_OPENAI_ENDPOINT'].rstrip('/')}/openai/v1/",
    api_key=token_provider,
)
```

## การตั้งค่า async client — EntraID พร้อม tenant เฉพาะ (หลาย tenant)

เมื่อ Azure OpenAI resource อยู่ใน **tenant ต่างจาก** ค่าเริ่มต้น ให้ส่ง `tenant_id` อย่างชัดเจนไปยัง credential สิ่งนี้มักเกิดในสถานการณ์ dev/test ที่ tenant บ้านของนักพัฒนาต่างจาก tenant ของ resource

```python
import os
from azure.identity.aio import (
    AzureDeveloperCliCredential,
    ChainedTokenCredential,
    ManagedIdentityCredential,
    get_bearer_token_provider,
)
from openai import AsyncOpenAI

# ManagedIdentityCredential สำหรับการผลิต (Azure Container Apps, App Service เป็นต้น)
managed_identity_cred = ManagedIdentityCredential(
    client_id=os.getenv("AZURE_CLIENT_ID")  # ตัวตนที่จัดการโดยผู้ใช้
)
# AzureDeveloperCliCredential สำหรับการพัฒนาในเครื่อง — tenant_id ที่ระบุชัดเจนมีความสำคัญ
azd_cred = AzureDeveloperCliCredential(
    tenant_id=os.getenv("AZURE_TENANT_ID"),
    process_timeout=60,
)
# เชน: ลองใช้ตัวตนที่จัดการก่อน จากนั้น fallback ไปที่ azd CLI
azure_credential = ChainedTokenCredential(managed_identity_cred, azd_cred)

token_provider = get_bearer_token_provider(
    azure_credential, "https://cognitiveservices.azure.com/.default"
)

client = AsyncOpenAI(
    base_url=f"{os.environ['AZURE_OPENAI_ENDPOINT'].rstrip('/')}/openai/v1/",
    api_key=token_provider,
)
```

## การย้าย async client — ก่อน/หลัง

ก่อนหน้า (เลิกใช้แล้ว):
```python
from openai import AsyncAzureOpenAI

client = AsyncAzureOpenAI(
    api_version=os.environ["AZURE_OPENAI_API_VERSION"],
    azure_endpoint=os.environ["AZURE_OPENAI_ENDPOINT"],
    azure_ad_token_provider=token_provider,
)

resp = await client.chat.completions.create(
    model="gpt-4.1",
    messages=[{"role": "user", "content": "Hello"}],
    max_tokens=500,
)
print(resp.choices[0].message.content)
```

หลังจาก:
```python
from openai import AsyncOpenAI

deployment = os.environ["AZURE_OPENAI_DEPLOYMENT"]

client = AsyncOpenAI(
    base_url=f"{os.environ['AZURE_OPENAI_ENDPOINT'].rstrip('/')}/openai/v1/",
    api_key=token_provider,
)

resp = await client.responses.create(
    model=deployment,
    input="Hello",
    max_output_tokens=1000,
    store=False,
)
print(resp.output_text)
```

## การย้าย sync เต็มรูปแบบ — ก่อน/หลัง

ก่อนหน้า (แบบเก่า — Azure OpenAI Chat Completions):
```python
from openai import AzureOpenAI
import os

client = AzureOpenAI(
    api_version=os.environ["AZURE_OPENAI_API_VERSION"],
    azure_endpoint=os.environ["AZURE_OPENAI_ENDPOINT"],
    api_key=os.environ["AZURE_OPENAI_API_KEY"],
)

resp = client.chat.completions.create(
    model="gpt-4.1",
    messages=[{"role": "user", "content": "Hello"}],
    max_tokens=500,
)
print(resp.choices[0].message.content)
```

หลังจาก (Responses API — จุดเชื่อมต่อ Azure OpenAI v1):
```python
from openai import OpenAI
import os

deployment = os.environ["AZURE_OPENAI_DEPLOYMENT"]

client = OpenAI(
    api_key=os.environ["AZURE_OPENAI_API_KEY"],
    base_url=f"{os.environ['AZURE_OPENAI_ENDPOINT'].rstrip('/')}/openai/v1/",
)

resp = client.responses.create(
    model=deployment,
    input="Hello",
    max_output_tokens=1000,
    store=False,
)
print(resp.output_text)
```

## การสตรีม (sync)
```python
stream = client.responses.create(
    model=deployment,
    input="Explain streaming in simple terms",
    max_output_tokens=1000,
    stream=True,
)
for event in stream:
    if event.type == "response.output_text.delta":
        print(event.delta, end="", flush=True)
    elif event.type == "response.completed":
        print()  # ขึ้นบรรทัดใหม่ที่ท้ายไฟล์
```

## การสตรีม (async)
```python
stream = await client.responses.create(
    model=deployment,
    input="Explain streaming in simple terms",
    max_output_tokens=1000,
    stream=True,
)
async for event in stream:
    if event.type == "response.output_text.delta":
        print(event.delta, end="", flush=True)
    elif event.type == "response.completed":
        print()
```

## การสตรีมแอปเว็บ — รูปแบบ backend-to-frontend

เมื่อย้ายแอปเว็บที่สตรีม SSE/JSONL ไปยัง frontend รูปแบบการอนุกรม backend **จะแตกต่างออกไป** ออกแบบเอาต์พุต backend ใหม่เพื่อรักษารูปแบบการเข้าถึงของ frontend ที่มีอยู่เดิมเพื่อให้ frontend ไม่ต้องเปลี่ยนแปลง

**ก่อนหน้า** — backend ของ Chat Completions โดยปกติจะอนุกรมแต่ละชิ้นของ `choices[0]` dict:
```python
# เก่า: ดิกชันนารีตัวเลือกเต็มแบบอนุกรมต่อชิ้นส่วน
async for chunk in response:
    if chunk.choices:
        yield json.dumps(chunk.choices[0].model_dump()) + "\n"
```
Frontend อ่าน: `response.delta.content` (เส้นทางลึกเข้าไปในอ็อบเจ็กต์ choice)

**หลังจาก** — backend ของ Responses API ส่งออกโครงสร้างที่เล็กลงรักษาเส้นทางการเข้าถึง frontend เดิมไว้:
```python
# ใหม่: ส่งออกเฉพาะสิ่งที่ frontend ต้องการเท่านั้น
async for event in await chat_coroutine:
    if event.type == "response.output_text.delta":
        yield json.dumps({"delta": {"content": event.delta}}) + "\n"
    elif event.type == "response.completed":
        yield json.dumps({"delta": {"content": None}, "finish_reason": "stop"}) + "\n"
```
Frontend ยังคงอ่าน `response.delta.content` — **ไม่ต้องเปลี่ยน frontend**

> **ข้อสังเกตสำคัญ**: รูปแบบการสตรีมของ Responses API (`event.type` + `event.delta`) แตกต่างโดยพื้นฐานจาก Chat Completions (`chunk.choices[0].delta.content`) แต่สัญญาของคุณระหว่าง backend กับ frontend กำหนดได้เอง ออกแบบเอาต์พุต backend ให้ตรงกับสิ่งที่ frontend คาดหวังไว้แล้ว

## ลำดับเหตุการณ์สตรีมมิ่ง

เมื่อ `stream: true` API จะส่งเหตุการณ์ตามลำดับนี้:
1. `response.created` – สร้างอ็อบเจ็กต์ response เริ่มต้น
2. `response.in_progress` – เริ่มการสร้าง
3. `response.output_item.added` – สร้างรายการผลลัพธ์
4. `response.content_part.added` – เริ่มส่วนเนื้อหา
5. `response.output_text.delta` – ชิ้นข้อความ (หลายชิ้น แต่ละอันมี `delta: string`)
6. `response.output_text.done` – การสร้างข้อความเสร็จสิ้น
7. `response.content_part.done` – ส่วนเนื้อหาสิ้นสุด
8. `response.output_item.done` – รายการผลลัพธ์เสร็จ
9. `response.completed` – ตอบกลับเต็มรูปแบบเสร็จสมบูรณ์

สำหรับการสตรีมข้อความพื้นฐาน ให้จัดการเฉพาะ `response.output_text.delta` (สำหรับชิ้นข้อความ) และ `response.completed` (สำหรับการสิ้นสุด)

## การจัดการข้อผิดพลาดสตรีมมิ่งในแอปเว็บ

เมื่อสตรีมในแอปเว็บ ให้ห่อหุ้มการวนลูป async ด้วย `try/except` และส่งข้อผิดพลาดเป็น JSON เพื่อให้ frontend แสดงผลได้อย่างสวยงาม (เช่น ขีดจำกัดอัตรา, ความล้มเหลวชั่วคราว):

```python
@stream_with_context
async def response_stream():
    chat_coroutine = client.responses.create(
        model=deployment,
        input=all_messages,
        max_output_tokens=1000,
        stream=True,
        store=False,
    )
    try:
        async for event in await chat_coroutine:
            if event.type == "response.output_text.delta":
                yield json.dumps({"delta": {"content": event.delta}}) + "\n"
            elif event.type == "response.completed":
                yield json.dumps({"delta": {"content": None}, "finish_reason": "stop"}) + "\n"
    except Exception as e:
        current_app.logger.error(e)
        yield json.dumps({"error": str(e)}) + "\n"
```


> **ทำไมเรื่องนี้จึงสำคัญ**: Azure OpenAI จะส่งกลับ `429 Too Many Requests` เมื่อถูกจำกัดอัตราการร้องขอ หากไม่มี `try/except` การตอบกลับแบบสตรีมจะดับไปโดยเงียบๆ แต่ถ้ามี จะทำให้ frontend ได้รับ `{"error": "Too Many Requests"}` และสามารถแสดงคำสั่งให้ลองใหม่ได้

## ประเภทเหตุการณ์สตรีม (Python SDK)

- `ResponseTextDeltaEvent`: `type='response.output_text.delta'`, `delta: str`
- `ResponseCompletedEvent`: `type='response.completed'`, `response: Response`

## รูปแบบการสนทนา
```python
# Responses API รองรับรูปแบบการสนทนาผ่านอาเรย์อินพุต
response = client.responses.create(
    model=deployment,
    input=[
        {"role": "system", "content": "You are an Azure cloud architect."},
        {"role": "user", "content": "Design a scalable web application architecture."},
    ],
    max_output_tokens=1000,
)
print(response.output_text)
```

## การจัดการข้อผิดพลาดตัวกรองเนื้อหา

โครงสร้างร่างข้อผิดพลาดเปลี่ยนจาก Chat Completions เป็น Responses API

ก่อนหน้านี้ (Chat Completions):
```python
except openai.APIError as error:
    if error.code == "content_filter":
        if error.body["innererror"]["content_filter_result"]["jailbreak"]["filtered"] is True:
            print("Jailbreak detected!")
```

หลังจากนี้ (Responses API):
```python
except openai.APIError as error:
    if error.code == "content_filter":
        if error.body["content_filters"][0]["content_filter_results"]["jailbreak"]["filtered"] is True:
            print("Jailbreak detected!")
```

ความแตกต่างหลัก:
- ตัวครอบ `innererror` **หายไป** — รายละเอียดตัวกรองเนื้อหาไปอยู่ชั้นบนสุดของ `error.body`
- `content_filter_result` (เอกพจน์) → `content_filters` (พหูพจน์เป็นอาร์เรย์) ซึ่งแต่ละรายการบรรจุ `content_filter_results` (พหูพจน์) อยู่ข้างใน
- แต่ละรายการใน `content_filters` รวมถึง `blocked`, `source_type` และ `content_filter_results` ที่มีรายละเอียดตามแต่ละหมวดหมู่ (`jailbreak`, `hate`, `sexual`, `violence`, `self_harm`)

รูปร่างร่างข้อผิดพลาดตัวกรองเนื้อหาเต็มรูปแบบของ Responses API:
```json
{
  "message": "The response was filtered...",
  "type": "invalid_request_error",
  "param": "prompt",
  "code": "content_filter",
  "content_filters": [
    {
      "blocked": true,
      "source_type": "prompt",
      "content_filter_results": {
        "jailbreak": { "detected": true, "filtered": true },
        "hate": { "filtered": false, "severity": "safe" },
        "sexual": { "filtered": false, "severity": "safe" },
        "violence": { "filtered": false, "severity": "safe" },
        "self_harm": { "filtered": false, "severity": "safe" }
      }
    }
  ]
}
```

## การย้ายข้อมูล HTTP ดิบ (requests/httpx)

หากแอพเรียก Azure OpenAI REST โดยตรงแทนการใช้ SDK:

ก่อนหน้านี้ (Chat Completions):
```python
endpoint = f"{azure_endpoint}/openai/deployments/{deployment}/chat/completions?api-version=2024-03-01-preview"
data = {
    "messages": [{"role": "user", "content": query}],
    "model": model_name,
    "temperature": 0,
}
response = requests.post(endpoint, headers=headers, json=data)
message = response.json()["choices"][0]["message"]["content"]
```

หลังจากนี้ (Responses API):
```python
endpoint = f"{azure_endpoint}/openai/v1/responses"
data = {
    "model": deployment,
    "input": [{"role": "user", "content": query}],
    "temperature": 0,
    "max_output_tokens": 1000,
    "store": False,
}
response = requests.post(endpoint, headers=headers, json=data)
output_text = response.json()["output"][0]["content"][0]["text"]
```

> **หมายเหตุ**: `output_text` เป็นคุณสมบัติที่สะดวกในอ็อบเจ็กต์ `Response` ของ Python SDK การตอบกลับ JSON ของ REST ดิบไม่มีฟิลด์ `output_text` ชั้นสูงสุด — ข้อความอยู่ที่ `output[0].content[0].text`

## การสนทนาแบบหลายรอบ
```python
# สร้างบทสนทนาด้วย Responses API
messages = [
    {"role": "system", "content": "You are a helpful coding assistant."},
    {"role": "user", "content": "Write a Python function to calculate factorial"},
]

response = client.responses.create(
    model=deployment,
    input=messages,
    max_output_tokens=400,
)

# เพิ่มการตอบกลับของผู้ช่วยในบทสนทนา
messages.append({"role": "assistant", "content": response.output_text})

# ดำเนินบทสนทนาต่อไป
messages.append({"role": "user", "content": "Now optimize it with memoization"})

response2 = client.responses.create(
    model=deployment,
    input=messages,
    max_output_tokens=400,
)
print(response2.output_text)
```

การสนทนาหลายรอบแบบมีประเภทเนื้อหา (กำหนด `input_text`/`output_text` ชัดเจน):
```python
messages = [
    {"role": "system", "content": [{"type": "input_text", "text": "You are helpful."}]},
    {"role": "user", "content": [{"type": "input_text", "text": "Hi"}]},
    {"role": "assistant", "content": [{"type": "output_text", "text": "Hello!"}]},
    {"role": "user", "content": [{"type": "input_text", "text": "Tell me a joke"}]},
]
resp = client.responses.create(model=deployment, input=messages, store=False)
```

### การสนทนาหลายรอบผ่าน `previous_response_id` (ทางเลือก)

แทนที่จะจัดการอาร์เรย์การสนทนาด้วยตัวเอง คุณสามารถเชื่อมโยงการตอบกลับ
ด้านเซิร์ฟเวอร์โดยใช้ `previous_response_id` API จะเก็บแต่ละการตอบกลับและ
ต่อด้วยรอบก่อนหน้าที่อัตโนมัติ

```python
# ตาคืนแรก
response = client.responses.create(
    model=deployment,
    input=[{"role": "user", "content": "Write a Python function to calculate factorial"}],
)
print(response.output_text)

# ตาต่อไป — เพียงส่งข้อความผู้ใช้ใหม่ + ID การตอบกลับก่อนหน้า
response2 = client.responses.create(
    model=deployment,
    input=[{"role": "user", "content": "Now optimize it with memoization"}],
    previous_response_id=response.id,
)
print(response2.output_text)
```

**เมื่อใดควรใช้แบบใด:**

| วิธีการ | ข้อดี | ข้อเสีย |
|---|---|---|
| อาร์เรย์ `input` (จัดการเอง) | ควบคุมประวัติเต็มที่; สามารถตัด/สรุป; ไม่ต้องเก็บฝั่งเซิร์ฟเวอร์ (`store=False`) | โค้ดยุ่งยากกว่า; คุณต้องจัดการอาร์เรย์เอง |
| `previous_response_id` | โค้ดง่ายกว่า; ต่อเนื่องอัตโนมัติ | ต้องใช้ `store=True` (ค่าปริยาย); การสนทนาเก็บฝั่งเซิร์ฟเวอร์; ไม่แก้ไขประวัติระหว่างรอบได้ |

> **หมายเหตุการย้าย:** แอพ Chat Completions ส่วนใหญ่จัดการอาร์เรย์ข้อความเองอยู่แล้ว การเปลี่ยนเป็นอาร์เรย์ `input` จึงเป็นการย้ายตรง 1:1 ที่ง่ายกว่า ใช้ `previous_response_id` สำหรับโค้ดใหม่หรือเมื่อไม่ต้องการแก้ไขประวัติการสนทนา

## โมเดลเหตุผลแบบชุด O-series (o1, o3-mini, o3, o4-mini)

โมเดลชุด O-series มีข้อจำกัดพารามิเตอร์เฉพาะเมื่อย้ายไป Responses API

### การแมปพารามิเตอร์สำหรับ o-series

| Chat Completions (o-series) | Responses API | หมายเหตุ |
|---|---|---|

| `max_completion_tokens` | `max_output_tokens` | ตั้งค่าสูง (4096+) — โทเคนการให้เหตุผลถูกนับรวมในการจำกัด |
| `reasoning_effort` | `reasoning.effort` | เก็บไว้ตามเดิมถ้ามี (ต่ำ/กลาง/สูง) |
| `temperature` | ลบหรือกำหนดเป็น `1` | O-series รองรับเฉพาะ `1` |
| `top_p` | ลบ | ไม่รองรับใน o-series |
| `seed` | ลบ | ไม่รองรับใน Responses API |

### O-series ก่อน/หลัง

ก่อน (Chat Completions กับ o-series):
```python
resp = client.chat.completions.create(
    model="o4-mini",
    messages=[{"role": "user", "content": "Solve this step by step: 2x + 5 = 13"}],
    max_completion_tokens=4096,
    reasoning_effort="medium",
)
print(resp.choices[0].message.content)
```

หลัง (Responses API):
```python
resp = client.responses.create(
    model=deployment,
    input="Solve this step by step: 2x + 5 = 13",
    max_output_tokens=4096,
    reasoning={"effort": "medium"},
    store=False,
)
print(resp.output_text)
```

> **หมายเหตุ**: โมเดล O-series อาจเก็บบัฟเฟอร์ผลลัพธ์ระหว่างการให้เหตุผลก่อนที่จะส่ง delta ของข้อความ การสตรีมยังคงทำงานได้แต่เหตุการณ์ `response.output_text.delta` ครั้งแรกอาจมาช้ากว่ากับโมเดล GPT

## การเข้าถึงโทเคนการให้เหตุผล
```python
# โมเดลการให้เหตุผลใช้การให้เหตุผลภายใน — คุณสามารถดูได้ว่ามีการใช้โทเค็นการให้เหตุผลกี่ตัว
response = client.responses.create(
    model=deployment,
    input="Explain quantum computing in simple terms",
    max_output_tokens=1000,
)
print(response.output_text)
print(f"Status: {response.status}")
print(f"Reasoning tokens: {response.usage.output_tokens_details.reasoning_tokens}")
print(f"Output tokens: {response.usage.output_tokens}")
```

> **สำคัญ**: ใช้ `max_output_tokens=1000` (ไม่ใช่ 50–200) เพื่อรองรับกระบวนการให้เหตุผลภายในของโมเดล โมเดลจะใช้โทเคนการให้เหตุผลภายในก่อนสร้างผลลัพธ์สุดท้าย

## ผลลัพธ์แบบมีโครงสร้าง — JSON Schema
```python
resp = client.responses.create(
    model=deployment,
    input="What is the capital of France?",
    max_output_tokens=500,
    text={
        "format": {
            "type": "json_schema",
            "name": "Output",
            "strict": True,
            "schema": {
                "type": "object",
                "properties": {"answer": {"type": "string"}},
                "required": ["answer"],
                "additionalProperties": False,
            },
        }
    },
    store=False,
)
import json
data = json.loads(resp.output_text)
print(data["answer"])
```

## การใช้เครื่องมือ

- กำหนดฟังก์ชันใน `tools` ด้วยรูปแบบ Responses API แบบ **แบน** — `name`, `description`, และ `parameters` อยู่ระดับบนสุด (ไม่ซ้อนใน `function`)
- เมื่อโมเดลขอเรียกใช้เครื่องมือ ให้ดำเนินการในแอปของคุณและรวมผลลัพธ์ของเครื่องมือในคำขอต่อไปเป็นรายการ `function_call_output` ภายใต้ `input`
- รักษา schema ให้เรียบง่าย; ตรวจสอบความถูกต้องของอินพุตก่อนดำเนินการ
- เมื่อใช้ `strict: true` คุณสมบัติทั้งหมดต้องถูกระบุใน `required` และ `additionalProperties: false` จำเป็นต้องใช้

> **⚠️ `pydantic_function_tool()` ไม่เข้ากัน**: ตัวช่วย `openai.pydantic_function_tool()` ยังคงสร้างรูปแบบแชทรุ่นเก่าแบบซ้อน (`{"type": "function", "function": {"name": ...}}`) หลีกเลี่ยงการใช้กับ `responses.create()` ให้กำหนด schema เครื่องมือด้วยตนเองหรือเขียนตัวห่อเพื่อแปลงออกมาเป็นรูปแบบแบน

### รูปแบบการกำหนดเครื่องมือ

Responses API ใช้รูปแบบเครื่องมือแบบ **แบน** — `name`, `description`, `parameters` เป็นคีย์ระดับบนสุด (ไม่ซ้อนใน `function`)

**ก่อน (Chat Completions — ซ้อน):**
```python
tools = [{"type": "function", "function": {"name": "lookup_weather", "parameters": {...}}}]
```

**หลัง (Responses API — แบน):**
```python
tools = [{"type": "function", "name": "lookup_weather", "parameters": {...}}]
```

ตัวอย่างเต็ม:
```python
tools = [
    {
        "type": "function",
        "name": "lookup_weather",
        "description": "Lookup the weather for a given city name.",
        "parameters": {
            "type": "object",
            "properties": {
                "city_name": {"type": "string", "description": "The city name"},
            },
            "required": ["city_name"],
            "additionalProperties": False,
        },
    }
]

response = client.responses.create(
    model=deployment,
    input=[
        {"role": "system", "content": "You are a weather chatbot."},
        {"role": "user", "content": "What's the weather in Berkeley?"},
    ],
    tools=tools,
    tool_choice="auto",
    store=False,
)
```

พร้อม `strict: true` (บังคับใช้ schema):
```python
tools = [
    {
        "type": "function",
        "name": "lookup_weather",
        "description": "Lookup the weather for a given city name.",
        "strict": True,
        "parameters": {
            "type": "object",
            "properties": {
                "city_name": {"type": "string", "description": "The city name"},
            },
            "required": ["city_name"],       # ต้องระบุคุณสมบัติทั้งหมด
            "additionalProperties": False,   # จำเป็นสำหรับโหมดเข้มงวด
        },
    }
]
```

### การเรียกเครื่องมือแบบรอบเดินทาง (รันและส่งผลลัพธ์คืน)

เมื่อโมเดลร้องขอการเรียกเครื่องมือ ให้ใช้รายการ `response.output` + `function_call_output` — **ไม่ใช่** รูปแบบ `role: assistant` + `role: tool` ของ Chat Completions

```python
import json

messages = [
    {"role": "system", "content": "You are a weather chatbot."},
    {"role": "user", "content": "Is it sunny in Berkeley?"},
]

response = client.responses.create(
    model=deployment, input=messages, tools=tools, store=False,
)

tool_calls = [item for item in response.output if item.type == "function_call"]
if tool_calls:
    # เพิ่มรายการ function_call ของแบบจำลองลงในการสนทนา
    messages.extend(response.output)

    # ดำเนินการแต่ละเครื่องมือและเพิ่มผลลัพธ์
    for tc in tool_calls:
        result = execute_tool(tc.name, json.loads(tc.arguments))
        messages.append({
            "type": "function_call_output",
            "call_id": tc.call_id,
            "output": json.dumps(result),
        })

    # รับการตอบกลับสุดท้ายพร้อมผลลัพธ์ของเครื่องมือ
    response = client.responses.create(
        model=deployment, input=messages, tools=tools, store=False,
    )
    print(response.output_text)
```

### ตัวอย่างการเรียกเครื่องมือแบบ few-shot

เมื่อให้ตัวอย่างการเรียกเครื่องมือแบบ few-shot ใน `input` ให้ใช้รายการ `function_call` และ `function_call_output` รหัสต้องขึ้นต้นด้วย `fc_`

```python
messages = [
    {"role": "system", "content": "You are a product search assistant."},
    {"role": "user", "content": "Find climbing gear for outdoors"},
    {
        "type": "function_call",
        "id": "fc_example1",
        "call_id": "call_example1",
        "name": "search_database",
        "arguments": '{"search_query": "climbing gear outdoor"}',
    },
    {
        "type": "function_call_output",
        "call_id": "call_example1",
        "output": "Results: ...",
    },
    {"role": "user", "content": "Now find shoes under $50"},
]
```

```python
# ตัวอย่างการค้นหาเว็บในตัว
resp = client.responses.create(
    model=deployment,
    tools=[{"type": "web_search_preview"}],
    input="What was a positive news story from today?",
    store=False,
)
print(resp.output_text)
```

## อินพุตภาพ

รายการเนื้อหาภาพจะเปลี่ยนประเภทจาก `image_url` เป็น `input_image` และ URL จะเปลี่ยนจากวัตถุซ้อนเป็นสตริงแบน

### อินพุตภาพ — ก่อนหน้า (Chat Completions)
```python
resp = client.chat.completions.create(
    model=deployment,
    messages=[
        {
            "role": "user",
            "content": [
                {"type": "text", "text": "What's in this image?"},
                {
                    "type": "image_url",
                    "image_url": {"url": "https://example.com/image.jpg"},
                },
            ],
        }
    ],
    max_tokens=500,
)
print(resp.choices[0].message.content)
```

### อินพุตภาพ — หลัง (Responses API, URL)
```python
resp = client.responses.create(
    model=deployment,
    input=[
        {
            "role": "user",
            "content": [
                {"type": "input_text", "text": "What's in this image?"},
                {
                    "type": "input_image",
                    "image_url": "https://example.com/image.jpg",
                },
            ],
        }
    ],
    max_output_tokens=500,
    store=False,
)
print(resp.output_text)
```

### อินพุตภาพ — หลัง (Responses API, base64)
```python
import base64

def encode_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode("utf-8")

base64_image = encode_image("path_to_your_image.jpg")

resp = client.responses.create(
    model=deployment,
    input=[
        {
            "role": "user",
            "content": [
                {"type": "input_text", "text": "What's in this image?"},
                {
                    "type": "input_image",
                    "image_url": f"data:image/jpeg;base64,{base64_image}",
                },
            ],
        }
    ],
    max_output_tokens=500,
    store=False,
)
print(resp.output_text)
```

> **การเปลี่ยนแปลงหลัก**: (1) `"type": "image_url"` → `"type": "input_image"`, (2) `"image_url": {"url": "..."}` (วัตถุซ้อน) → `"image_url": "..."` (สตริงแบน — เป็น URL HTTPS หรือ data URI ชนิด `data:image/...;base64,...`), (3) `"type": "text"` → `"type": "input_text"`

## การย้าย Microsoft Agent Framework (MAF)

**ตรวจสอบเวอร์ชัน MAF ของคุณก่อน** — การย้ายขึ้นอยู่กับว่าคุณใช้ MAF 1.0.0 ขึ้นไป หรือเวอร์ชันเบต้า/rc ก่อน 1.0.0

ตรวจสอบได้โดย: `python -c "import agent_framework_openai; print(agent_framework_openai.__version__)"`

### MAF 1.0.0+ (agent-framework-openai >= 1.0.0)

ใน MAF 1.0.0+ `OpenAIChatClient` **ใช้ Responses API แล้ว** — ไม่ต้องย้ายข้อมูล

หากฐานโค้ดใช้ `OpenAIChatCompletionClient` รุ่นเก่า (ซึ่งใช้ `chat.completions.create`) ให้แทนที่ด้วย `OpenAIChatClient`:

ก่อน:
```python
from agent_framework.openai import OpenAIChatCompletionClient
from azure.identity.aio import DefaultAzureCredential, get_bearer_token_provider

async_credential = DefaultAzureCredential()
token_provider = get_bearer_token_provider(async_credential, "https://cognitiveservices.azure.com/.default")

client = OpenAIChatCompletionClient(
    base_url=f"{os.environ['AZURE_OPENAI_ENDPOINT']}/openai/v1/",
    api_key=token_provider,
    model=os.environ["AZURE_OPENAI_CHAT_DEPLOYMENT"],
)
```

หลัง:
```python
from agent_framework.openai import OpenAIChatClient
from azure.identity.aio import DefaultAzureCredential, get_bearer_token_provider

async_credential = DefaultAzureCredential()
token_provider = get_bearer_token_provider(async_credential, "https://cognitiveservices.azure.com/.default")

client = OpenAIChatClient(
    base_url=f"{os.environ['AZURE_OPENAI_ENDPOINT']}/openai/v1/",
    api_key=token_provider,
    model=os.environ["AZURE_OPENAI_CHAT_DEPLOYMENT"],
)
```

### MAF ก่อน 1.0.0 (เบต้า/rc)

ใน MAF ก่อน 1.0.0 `OpenAIChatClient` ใช้ Chat Completions ให้เลื่อนรุ่นเป็น `agent-framework-openai>=1.0.0` ที่ `OpenAIChatClient` ใช้ Responses API โดยค่าเริ่มต้น

> **หมายเหตุ**: `Agent`, `MCPStreamableHTTPTool` และ API ของ MAF อื่น ๆ ไม่เปลี่ยนแปลง — มีเพียงการนำเข้าและการสร้างอินสแตนซ์ของคลายเอ็นต์เท่านั้นที่เปลี่ยน

## การย้าย LangChain (`langchain-openai`)

เพิ่ม `use_responses_api=True` ใน `ChatOpenAI()` และอัปเดตการเข้าถึงเนื้อหาข้อความจาก `.content` เป็น `.text`

ก่อน:
```python
import azure.identity
from langchain_openai import ChatOpenAI
from pydantic import SecretStr

token_provider = azure.identity.get_bearer_token_provider(
    azure.identity.DefaultAzureCredential(),
    "https://cognitiveservices.azure.com/.default",
)
model = ChatOpenAI(
    model=os.environ.get("AZURE_OPENAI_CHAT_DEPLOYMENT"),
    base_url=os.environ["AZURE_OPENAI_ENDPOINT"] + "/openai/v1/",
    api_key=token_provider,
)

# ... การเรียกใช้งานตัวแทน ...
result = await agent.ainvoke({"messages": [HumanMessage(content=query)]})
print(result['messages'][-1].content)
```

หลัง:
```python
import azure.identity
from langchain_openai import ChatOpenAI
from pydantic import SecretStr

token_provider = azure.identity.get_bearer_token_provider(
    azure.identity.DefaultAzureCredential(),
    "https://cognitiveservices.azure.com/.default",
)
model = ChatOpenAI(
    model=os.environ.get("AZURE_OPENAI_CHAT_DEPLOYMENT"),
    base_url=os.environ["AZURE_OPENAI_ENDPOINT"] + "/openai/v1/",
    api_key=token_provider,
    use_responses_api=True,
)

# ... การเรียกใช้งานตัวแทน ...
result = await agent.ainvoke({"messages": [HumanMessage(content=query)]})
print(result['messages'][-1].text)
```

> **การเปลี่ยนแปลงหลัก**: (1) `use_responses_api=True` ในตัวสร้าง, (2) `.content` → `.text` ในข้อความตอบกลับ

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ปฏิเสธความรับผิดชอบ**:
เอกสารนี้ได้รับการแปลโดยใช้บริการแปลภาษา AI [Co-op Translator](https://github.com/Azure/co-op-translator) ขณะที่เราพยายามให้ความถูกต้อง โปรดทราบว่าการแปลโดยอัตโนมัติอาจมีข้อผิดพลาดหรือความไม่ถูกต้อง เอกสารต้นฉบับในภาษาต้นทางควรถูกพิจารณาเป็นแหล่งข้อมูลที่เชื่อถือได้ สำหรับข้อมูลที่สำคัญ แนะนำให้ใช้การแปลโดยมนุษย์มืออาชีพ เราไม่รับผิดชอบต่อความเข้าใจผิดหรือการตีความที่ผิดพลาดที่เกิดขึ้นจากการใช้การแปลนี้
<!-- CO-OP TRANSLATOR DISCLAIMER END -->