# Responses API Cheat Sheet (Python + Azure OpenAI)

> ตัวอย่างโค้ดทั้งหมดด้านล่างสมมติว่า `deployment = os.environ["AZURE_OPENAI_DEPLOYMENT"]` และ `client` ถูกสร้างไว้แล้ว (ดูการตั้งค่า client)

## Basic request
```python
resp = client.responses.create(
    model=deployment,
    input="Hello",
    max_output_tokens=1000,
    store=False,
)
print(resp.output_text)
```

## ตั้งค่า Client — EntraID (แนะนำ)
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

## ตั้งค่า Client — API key
```python
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ["AZURE_OPENAI_API_KEY"],
    base_url=f"{os.environ['AZURE_OPENAI_ENDPOINT'].rstrip('/')}/openai/v1/",
)
```

## ตั้งค่า Async client — EntraID
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

## ตั้งค่า Async client — EntraID พร้อม tenant ระบุ (multi-tenant)

เมื่แหล่ง Azure OpenAI อยู่ใน **tenant ที่ต่างจากค่าเริ่มต้น** ให้ส่ง `tenant_id` อย่างชัดเจนไปยัง credentials ซึ่งเป็นสถานการณ์ที่พบได้บ่อยใน dev/test ที่ tenant บ้านของนักพัฒนาต่างจาก tenant ของทรัพยากร

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
    client_id=os.getenv("AZURE_CLIENT_ID")  # การระบุตัวตนแบบ Managed ที่กำหนดให้ผู้ใช้
)
# AzureDeveloperCliCredential สำหรับการพัฒนาท้องถิ่น — การระบุ tenant_id อย่างชัดเจนเป็นสิ่งสำคัญ
azd_cred = AzureDeveloperCliCredential(
    tenant_id=os.getenv("AZURE_TENANT_ID"),
    process_timeout=60,
)
# Chain: ลองใช้ managed identity ก่อน จากนั้นถ้าล้มเหลวใช้ azd CLI
azure_credential = ChainedTokenCredential(managed_identity_cred, azd_cred)

token_provider = get_bearer_token_provider(
    azure_credential, "https://cognitiveservices.azure.com/.default"
)

client = AsyncOpenAI(
    base_url=f"{os.environ['AZURE_OPENAI_ENDPOINT'].rstrip('/')}/openai/v1/",
    api_key=token_provider,
)
```

## ย้าย Async client — ก่อน/หลัง

ก่อนหน้า (เลิกใช้แล้ว):
```python
from openai import AsyncAzureOpenAI

client = AsyncAzureOpenAI(
    api_version=os.environ["AZURE_OPENAI_API_VERSION"],
    azure_endpoint=os.environ["AZURE_OPENAI_ENDPOINT"],
    azure_ad_token_provider=token_provider,
)

resp = await client.chat.completions.create(
    model="gpt-4o",
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

## ย้าย sync เต็มรูปแบบ — ก่อน/หลัง

ก่อนหน้า (เก่า — Azure OpenAI Chat Completions):
```python
from openai import AzureOpenAI
import os

client = AzureOpenAI(
    api_version=os.environ["AZURE_OPENAI_API_VERSION"],
    azure_endpoint=os.environ["AZURE_OPENAI_ENDPOINT"],
    api_key=os.environ["AZURE_OPENAI_API_KEY"],
)

resp = client.chat.completions.create(
    model="gpt-4o",
    messages=[{"role": "user", "content": "Hello"}],
    max_tokens=500,
)
print(resp.choices[0].message.content)
```

หลังจาก (Responses API — endpoint v1 ของ Azure OpenAI):
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

## การสตรีม (ซิงค์)
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
        print()  # ขึ้นบรรทัดใหม่ที่ส่วนท้าย
```

## การสตรีม (แอสิงค์)
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

## การสตรีมเว็บแอป — โครงสร้าง backend ไป frontend

เมื่อย้ายเว็บแอปที่ส่งสตรีม SSE/JSONL ไปยัง frontend **รูปแบบ serialization ของ backend** จะเปลี่ยนไป ให้ออกแบบผลลัพธ์ backend ใหม่เพื่อรักษารูปแบบการเข้าถึงฝั่ง frontend เดิมไว้เพื่อไม่ต้องแก้ไข frontend

**ก่อนหน้า** — Chat Completions backend โดยปกติจะทำ serialization เป็น dict ของ `choices[0]` ของแต่ละชิ้น:
```python
# เก่า: พจนานุกรมตัวเลือกเต็มที่เรียงลำดับแล้วต่อชิ้นส่วน
async for chunk in response:
    if chunk.choices:
        yield json.dumps(chunk.choices[0].model_dump()) + "\n"
```

การอ่านของ frontend: `response.delta.content` (เส้นทางลึกในวัตถุ choice)

**หลังจาก** — Responses API backend ส่งออกเป็นรูปแบบกะทัดรัดที่ยังคงเส้นทางเข้าถึง frontend เดิมไว้:
```python
# ใหม่: ส่งออกเฉพาะสิ่งที่ส่วนหน้าต้องการเท่านั้น
async for event in await chat_coroutine:
    if event.type == "response.output_text.delta":
        yield json.dumps({"delta": {"content": event.delta}}) + "\n"
    elif event.type == "response.completed":
        yield json.dumps({"delta": {"content": None}, "finish_reason": "stop"}) + "\n"
```

frontend ยังคงอ่าน `response.delta.content` — **ไม่ต้องแก้ไข frontend**

> **ข้อสังเกตหลัก**: รูปแบบสตรีมของ Responses API (`event.type` + `event.delta`) แตกต่างจาก Chat Completions (`chunk.choices[0].delta.content`) โดยพื้นฐาน แต่การตกลงระหว่าง backend กับ frontend เป็นของคุณ กำหนดรูป backend ให้ออกตรงกับสิ่งที่ frontend คาดหวังไว้แล้ว

## ลำดับเหตุการณ์สตรีม

เมื่อ `stream: true` API จะส่งเหตุการณ์ตามลำดับนี้:
1. `response.created` – สร้างวัตถุ response
2. `response.in_progress` – เริ่มการสร้างข้อความ
3. `response.output_item.added` – สร้าง output item
4. `response.content_part.added` – เริ่มส่วนเนื้อหา
5. `response.output_text.delta` – ชุดข้อความ (หลายชุด โดยแต่ละชุดมี `delta: string`)
6. `response.output_text.done` – เสร็จสิ้นการสร้างข้อความ
7. `response.content_part.done` – ส่วนเนื้อหาเสร็จสิ้น
8. `response.output_item.done` – output item เสร็จสิ้น
9. `response.completed` – ตอบกลับสมบูรณ์

สำหรับการสตรีมข้อความพื้นฐาน ให้จัดการแค่ `response.output_text.delta` (ข้อความชุด) และ `response.completed` (จบการทำงาน)

## การจัดการข้อผิดพลาดจากสตรีมในเว็บแอป

เมื่อทำสตรีมในเว็บแอป ให้ห่อหุ้มการ iterate แบบ async ด้วย `try/except` และส่งออกข้อผิดพลาดเป็น JSON เพื่อให้ frontend แสดงผลอย่างเหมาะสม (เช่น จำกัดอัตรา, ความล้มเหลวชั่วคราว):

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

> **เหตุผลที่สำคัญ**: Azure OpenAI จะคืนค่า `429 Too Many Requests` เมื่อถูกจำกัดอัตรา ถ้าไม่มี `try/except` การสตรีมจะหยุดทำงานโดยเงียบๆ แต่ถ้ามี จะส่ง `{"error": "Too Many Requests"}` ไปยัง frontend เพื่อแสดงข้อความให้ลองใหม่

## ชนิดเหตุการณ์สตรีม (Python SDK)

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

ก่อน (Chat Completions):
```python
except openai.APIError as error:
    if error.code == "content_filter":
        if error.body["innererror"]["content_filter_result"]["jailbreak"]["filtered"] is True:
            print("Jailbreak detected!")
```

หลัง (Responses API):
```python
except openai.APIError as error:
    if error.code == "content_filter":
        if error.body["content_filters"][0]["content_filter_results"]["jailbreak"]["filtered"] is True:
            print("Jailbreak detected!")
```

ความแตกต่างสำคัญ:
- ไม่ใช้ wrapper `innererror` อีกต่อไป — รายละเอียดตัวกรองเนื้อหาอยู่บนระดับบนสุดของ `error.body`
- `content_filter_result` (เอกพจน์) เปลี่ยนเป็น `content_filters` (พหูพจน์เป็นอาร์เรย์) ที่มี `content_filter_results` (พหูพจน์) แต่ละรายการ
- แต่ละรายการใน `content_filters` มีค่า `blocked`, `source_type`, และ `content_filter_results` ที่แสดงรายละเอียดตามหมวดหมู่ (`jailbreak`, `hate`, `sexual`, `violence`, `self_harm`)

โครงสร้างข้อผิดพลาดตัวกรองเนื้อหา Responses API แบบเต็ม:
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

## ย้ายแบบ HTTP ดิบ (requests/httpx)

ถ้าแอปเรียก REST ของ Azure OpenAI โดยตรงแทนใช้ SDK:

ก่อน (Chat Completions):
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

หลัง (Responses API):
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

> **หมายเหตุ**: `output_text` เป็น property สะดวกใน Python SDK `Response` เท่านั้น ส่วน raw REST JSON ไม่มีฟิลด์ `output_text` อยู่บนระดับบน — ข้อความอยู่ใน `output[0].content[0].text`

## การสนทนาหลายตา (multi-turn)
```python
# สร้างการสนทนาด้วย Responses API
messages = [
    {"role": "system", "content": "You are a helpful coding assistant."},
    {"role": "user", "content": "Write a Python function to calculate factorial"},
]

response = client.responses.create(
    model=deployment,
    input=messages,
    max_output_tokens=400,
)

# เพิ่มการตอบกลับของผู้ช่วยลงในการสนทนา
messages.append({"role": "assistant", "content": response.output_text})

# ดำเนินการสนทนาต่อ
messages.append({"role": "user", "content": "Now optimize it with memoization"})

response2 = client.responses.create(
    model=deployment,
    input=messages,
    max_output_tokens=400,
)
print(response2.output_text)
```

หลายตาที่แยกประเภทเนื้อหา (กำหนด `input_text`/`output_text` ชัดเจน):
```python
messages = [
    {"role": "system", "content": [{"type": "input_text", "text": "You are helpful."}]},
    {"role": "user", "content": [{"type": "input_text", "text": "Hi"}]},
    {"role": "assistant", "content": [{"type": "output_text", "text": "Hello!"}]},
    {"role": "user", "content": [{"type": "input_text", "text": "Tell me a joke"}]},
]
resp = client.responses.create(model=deployment, input=messages, store=False)
```

### หลายตาผ่าน `previous_response_id` (ทางเลือก)

แทนที่จะจัดการอาเรย์สนทนาเอง สามารถต่อเชื่อม response จากฝั่งเซิร์ฟเวอร์โดยใช้ `previous_response_id` ซึ่ง API จะเก็บทุก response และต่อข้อความก่อนหน้าให้อัตโนมัติ

```python
# ครั้งแรก
response = client.responses.create(
    model=deployment,
    input=[{"role": "user", "content": "Write a Python function to calculate factorial"}],
)
print(response.output_text)

# รอบถัดไป — เพียงส่งข้อความผู้ใช้ใหม่ + ID การตอบกลับก่อนหน้า
response2 = client.responses.create(
    model=deployment,
    input=[{"role": "user", "content": "Now optimize it with memoization"}],
    previous_response_id=response.id,
)
print(response2.output_text)
```

**เมื่อใดใช้แบบไหน:**

| วิธี | ข้อดี | ข้อเสีย |
|---|---|---|
| อาเรย์ `input` (จัดเอง) | ควบคุมประวัติทั้งหมด; ตัดทอน/สรุปได้; ไม่ต้องเก็บฝั่งเซิร์ฟเวอร์ (`store=False`) | เขียนโค้ดเยอะ ต้องจัดการอาร์เรย์เอง |
| `previous_response_id` | โค้ดง่ายขึ้น; ต่อเชื่อมอัตโนมัติ | ต้องใช้ `store=True` (ค่าเริ่มต้น); เก็บประวัติฝั่งเซิร์ฟเวอร์; แก้ไขประวัติกลางคันไม่ได้ |

> **หมายเหตุการย้าย:** แอปส่วนใหญ่ที่ใช้ Chat Completions จัดการอาเรย์ข้อความเองอยู่แล้ว จึงแปลงเป็นอาเรย์ `input` ได้ง่ายกว่า 1:1 ใช้ `previous_response_id` กับโค้ดใหม่หรือถ้าไม่ต้องแก้ไขประวัติสนทนา

## โมเดล O-series (o1, o3-mini, o3, o4-mini)

โมเดล O-series มีข้อจำกัดพารามิเตอร์เฉพาะเมื่อย้ายมาที่ Responses API

### แมปพารามิเตอร์สำหรับ o-series

| Chat Completions (o-series) | Responses API | หมายเหตุ |
|---|---|---|
| `max_completion_tokens` | `max_output_tokens` | ตั้งค่าสูง (4096+) — token ที่ใช้เหตุผลคิดรวมในขีดจำกัด |
| `reasoning_effort` | `reasoning.effort` | เก็บค่าเดิมถ้ามี (low/medium/high) |
| `temperature` | ลบหรือกำหนดเป็น `1` | O-series รับค่าแค่ `1` |
| `top_p` | ลบ | ไม่รองรับบน o-series |
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

> **หมายเหตุ**: โมเดล O-series อาจบัฟเฟอร์ข้อมูลก่อนออกข้อความ delta จริง การสตรีมยังทำงานได้ แต่ event `response.output_text.delta` ครั้งแรกอาจมาช้ากว่า GPT

## การเข้าถึง token ของ reasoning
```python
# โมเดลการให้เหตุผลใช้การให้เหตุผลภายใน — คุณสามารถเห็นจำนวนโทเค็นการให้เหตุผลที่ถูกใช้
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

> **สำคัญ**: ใช้ `max_output_tokens=1000` (ไม่ใช่ 50–200) เพื่อเผื่อ token เหตุผลภายใน โมเดลจะใช้ token เหตุผลก่อนสร้างผลลัพธ์สุดท้าย

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

## การใช้เครื่องมือ (Tool use)

- กำหนดฟังก์ชันใน `tools` แบบ **รูปแบบ Responses API แบนเรียบ** — `name`, `description`, และ `parameters` อยู่ระดับบนสุด (ไม่ซ้อนใน `function`)
- เมื่อโมเดลขอเรียกเครื่องมือ ให้รันมันในแอปฯ และใส่ผลลัพธ์เครื่องมือในคำขอต่อไปเป็น `function_call_output` ภายใน `input`
- ทำ schema ให้น้อยที่สุด ตรวจสอบ input ก่อนเรียกใช้งาน
- ใช้ `strict: true` ต้องระบุทุก property ใน `required` และ `additionalProperties: false` ต้องบังคับใช้

> **⚠️ `pydantic_function_tool()` ไม่เข้ากัน**: ตัวช่วย `openai.pydantic_function_tool()` ยังสร้างรูปแบบแบบเก่าซ้อน (`{"type": "function", "function": {"name": ...}}`) อย่าใช้กับ `responses.create()` ให้กำหนด schema เครื่องมือเองหรือเขียน wrapper เพื่อเรียบแบนผลลัพธ์

### รูปแบบการนิยามเครื่องมือ

Responses API ใช้รูปแบบเครื่องมือแบบ **แบน** — `name`, `description`, `parameters` เป็น key ระดับบนสุด (ไม่ซ้อนใน `function`)

**ก่อนหน้า (Chat Completions — ซ้อน):**
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

ใช้ `strict: true` (บังคับ schema):
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

### การเรียกเครื่องมือ (execute และคืนผล)

เมื่อโมเดลขอเรียกเครื่องมือ ใช้ `response.output` + `function_call_output` — **ไม่ใช่** รูปแบบ Chat Completions `role: assistant` + `role: tool`

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
    # เพิ่มรายการ function_call ของโมเดลลงในการสนทนา
    messages.extend(response.output)

    # ดำเนินการแต่ละเครื่องมือและเพิ่มผลลัพธ์
    for tc in tool_calls:
        result = execute_tool(tc.name, json.loads(tc.arguments))
        messages.append({
            "type": "function_call_output",
            "call_id": tc.call_id,
            "output": json.dumps(result),
        })

    # รับคำตอบสุดท้ายพร้อมผลลัพธ์จากเครื่องมือ
    response = client.responses.create(
        model=deployment, input=messages, tools=tools, store=False,
    )
    print(response.output_text)
```

### ตัวอย่างเรียกเครื่องมือแบบ few-shot

เมื่อใส่ตัวอย่างเรียกเครื่องมือใน `input` ให้ใส่ไอเท็ม `function_call` และ `function_call_output` รหัสต้องขึ้นต้นด้วย `fc_`

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

## การป้อนภาพ (Image input)

รายการเนื้อหาภาพเปลี่ยนชนิดจาก `image_url` เป็น `input_image` และ URL เปลี่ยนจากอ็อบเจ็กต์ซ้อนเป็นสตริงแบบแบน

### Image input — ก่อน (Chat Completions)
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

### Image input — หลัง (Responses API, URL)
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

### Image input — หลัง (Responses API, base64)
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

> **การเปลี่ยนแปลงสำคัญ**: (1) `"type": "image_url"` → `"type": "input_image"`, (2) `"image_url": {"url": "..."}` (อ็อบเจ็กต์ซ้อน) → `"image_url": "..."` (สตริงแบน — เป็น HTTPS URL หรือ `data:image/...;base64,...`), (3) `"type": "text"` → `"type": "input_text"`

## การย้าย Microsoft Agent Framework (MAF)

**ตรวจสอบเวอร์ชัน MAF ของคุณก่อน** — การย้ายขึ้นกับว่าคุณใช้ MAF 1.0.0+ หรือเวอร์ชันก่อนหน้า beta/rc

ตรวจเช็ค: `python -c "import agent_framework_openai; print(agent_framework_openai.__version__)"`

### MAF 1.0.0+ (agent-framework-openai >= 1.0.0)

ใน MAF 1.0.0+ `OpenAIChatClient` **ใช้ Responses API เรียบร้อยแล้ว** — ไม่ต้องย้าย

ถ้าฐานโค้ดใช้ตัวเก่า `OpenAIChatCompletionClient` (ที่ใช้ `chat.completions.create`) ให้เปลี่ยนเป็น `OpenAIChatClient`:

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

### MAF ก่อน 1.0.0 (beta/rc)

ใน MAF ก่อน 1.0.0 `OpenAIChatClient` ใช้ Chat Completions ให้ปรับเป็น `agent-framework-openai>=1.0.0` ซึ่ง `OpenAIChatClient` ใช้ Responses API เป็นค่าเริ่มต้น

> **หมายเหตุ**: API เช่น `Agent`, `MCPStreamableHTTPTool` และ MAF ตัวอื่นยังเหมือนเดิม — แค่เปลี่ยนการ import และสร้าง instance ของ client เท่านั้น

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

> **การเปลี่ยนแปลงสำคัญ**: (1) ใส่ `use_responses_api=True` ใน constructor, (2) เปลี่ยนจาก `.content` เป็น `.text` ในข้อความตอบกลับ

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ปฏิเสธความรับผิดชอบ**:
เอกสารนี้ได้รับการแปลโดยใช้บริการแปลภาษา AI [Co-op Translator](https://github.com/Azure/co-op-translator) ขณะที่เราพยายามให้ความถูกต้อง โปรดทราบว่าการแปลโดยอัตโนมัติอาจมีข้อผิดพลาดหรือความไม่ถูกต้อง เอกสารต้นฉบับในภาษาต้นทางควรถูกพิจารณาเป็นแหล่งข้อมูลที่เชื่อถือได้ สำหรับข้อมูลที่สำคัญ แนะนำให้ใช้การแปลโดยมนุษย์มืออาชีพ เราไม่รับผิดชอบต่อความเข้าใจผิดหรือการตีความที่ผิดพลาดที่เกิดขึ้นจากการใช้การแปลนี้
<!-- CO-OP TRANSLATOR DISCLAIMER END -->