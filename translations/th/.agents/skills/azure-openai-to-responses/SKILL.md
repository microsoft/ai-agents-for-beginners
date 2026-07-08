---
name: azure-openai-to-responses
license: MIT
---
# ย้ายแอป Python จาก Azure OpenAI Chat Completions ไปยัง Responses API

> **คำแนะนำที่ชัดเจน — ปฏิบัติตามอย่างเคร่งครัด**
>
> ทักษะนี้ย้ายฐานโค้ด Python ที่ใช้ Azure OpenAI Chat Completions
> ไปยัง Responses API ที่รวมเป็นหนึ่งเดียว โปรดทำตามคำแนะนำเหล่านี้อย่างแม่นยำ
> อย่าดัดแปลงการแม็ประหว่างพารามิเตอร์หรือสร้างรูปแบบ API ใหม่

---

## ตัวกระตุ้น

เปิดใช้งานทักษะนี้เมื่อผู้ใช้ต้องการ:
- ย้ายแอป Python จาก Azure OpenAI Chat Completions ไปยัง Responses API
- อัปเกรดการใช้งาน Python OpenAI SDK เป็นรูปร่าง API ล่าสุดกับ Azure OpenAI
- เตรียมโค้ด Python สำหรับโมเดล GPT-5 หรือใหม่กว่าที่ต้องการ Responses บน Azure
- เปลี่ยนจาก `AzureOpenAI`/`AsyncAzureOpenAI` เป็นไคลเอนต์มาตรฐาน `OpenAI`/`AsyncOpenAI` ที่ใช้ endpoint v1
- แก้ไขคำเตือนการเลิกใช้ที่เกี่ยวข้องกับตัวสร้าง `AzureOpenAI` หรือ `api_version`

---

## ⚠️ ความเข้ากันได้ของโมเดล — ตรวจสอบก่อน

> **ก่อนย้าย โปรดตรวจสอบว่าโครงสร้างพื้นฐาน Azure OpenAI ของคุณรองรับ Responses API หรือไม่**

### 1. ทดสอบอย่างรวดเร็ว (เร็วที่สุด)

```python
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ["AZURE_OPENAI_API_KEY"],
    base_url=f"{os.environ['AZURE_OPENAI_ENDPOINT'].rstrip('/')}/openai/v1/",
)

try:
    resp = client.responses.create(
        model=os.environ["AZURE_OPENAI_DEPLOYMENT"],
        input="ping",
        max_output_tokens=50,
        store=False,
    )
    print(f"✅ Deployment supports Responses API: {resp.output_text}")
except Exception as e:
    print(f"❌ Deployment does NOT support Responses API: {e}")
```

> **หมายเหตุ**: `max_output_tokens` มี **ขั้นต่ำ 16** บน Azure OpenAI ค่าต่ำกว่า 16 จะส่งกลับข้อผิดพลาด 400 ใช้ค่า 50+ สำหรับการทดสอบอย่างรวดเร็ว

ถ้าส่งกลับ 404 หมายความว่าโครงสร้างพื้นฐานโมเดลนั้นยังไม่รองรับ Responses — ตรวจสอบเอกสารอ้างอิงด้านล่าง หรือสร้างโครงสร้างใหม่นำโมเดลที่รองรับมาใช้

### 2. ตรวจสอบโมเดลที่มีในภูมิภาคของคุณ (แนะนำ)

รันเครื่องมือความเข้ากันได้ของโมเดลที่มีให้ในตัวเพื่อตรวจสอบว่าโมเดลใดรองรับ Responses API ในภูมิภาคของคุณ:

```bash
python migrate.py models --subscription YOUR_SUB_ID --location YOUR_REGION
```

เครื่องมือนี้สอบถาม Azure ARM แบบสดและแสดงเมทริกซ์ความเข้ากันได้ — โมเดลไหนรองรับ Responses, output แบบมีโครงสร้าง, เครื่องมือ ฯลฯ ใช้ `--filter gpt-5.1,gpt-5.2` เพื่อลดผลลัพธ์ หรือ `--json` สำหรับการสคริปต์

### 3. เอกสารอ้างอิงการรองรับโมเดลทั้งหมด

- **คิวรีสด**: `python migrate.py models` (ดูด้านบน — เฉพาะภูมิภาค, อัปเดตเสมอ)
- **ดูความพร้อมใช้งาน**: [ตารางสรุปโมเดลและความพร้อมใช้งานภูมิภาค](https://learn.microsoft.com/en-us/azure/foundry/foundry-models/concepts/models-sold-directly-by-azure?tabs=global-standard-aoai%2Cglobal-standard&pivots=azure-openai#model-summary-table-and-region-availability)
- **เริ่มต้นเร็ว & คำแนะนำ**: **https://aka.ms/openai/start**

### ⚠️ ข้อจำกัดของโมเดลเก่า

> **คำเตือน**: โมเดลเก่า (เช่น `gpt-4o`, `gpt-4`) อาจยังไม่รองรับฟีเจอร์ Responses API ทั้งหมดอย่างเต็มที่
>
> ข้อจำกัดที่ทราบกับโมเดลเก่า:
> - **พารามิเตอร์ `reasoning`**: ไม่รองรับบน `gpt-4o-mini`, `gpt-4o` และโมเดลที่ไม่รองรับ reasoning หลายรุ่น ย้ายเฉพาะ `reasoning` ถ้ามีในโค้ดต้นฉบับเท่านั้น
> - **พารามิเตอร์ `seed`**: ไม่รองรับใน Responses API เลย — ให้ลบออกจากทุกคำขอ
> - **เอาต์พุตแบบมีโครงสร้างผ่าน `text.format`**: โมเดลเก่าอาจไม่บังคับใช้ JSON schemas แบบ `strict: true` อย่างน่าเชื่อถือ
> - **การประสานงานเครื่องมือ**: GPT-5+ ประสานงานการเรียกใช้เครื่องมือเป็นส่วนหนึ่งของ reasoning ภายใน โมเดลเก่าบน Responses ยังทำงานได้แต่ไม่มีการผนวกลึกเช่นนี้
> - **ข้อจำกัดอุณหภูมิ**: เมื่อต้องย้ายไป `gpt-5` อุณหภูมิต้องไม่กำหนดหรือกำหนดเป็น `1` โมเดลเก่าไม่มีกฎนี้

### โมเดล reasoning ชุด O-series (o1, o3-mini, o3, o4-mini)

โมเดลชุด O-series มีข้อจำกัดพารามิเตอร์เฉพาะ เมื่อย้ายแอปที่ใช้โมเดล O-series:

- **`temperature`**: ต้องเป็น `1` (หรือไม่กำหนด) โมเดล O-series ไม่รับค่าต่าง
- **`max_completion_tokens` → `max_output_tokens`**: แอปที่ใช้ `max_completion_tokens` แบบ Azure ต้องเปลี่ยนไปใช้ `max_output_tokens` ตั้งค่าสูง (4096+) เพราะโทเค็น reasoning ใช้นับในขีดจำกัด
- **`reasoning_effort`**: ถ้าแอปใช้ `reasoning_effort` (ต่ำ/กลาง/สูง) ให้เก็บไว้ — Responses API รองรับพารามิเตอร์นี้สำหรับโมเดล O-series
- **พฤติกรรมสตรีม**: โมเดล O-series อาจเก็บผลลัพธ์จนกว่า reasoning จะเสร็จก่อนส่ง event delta ข้อความ สตรีมมิ่งยังทำงานได้แต่ `response.output_text.delta` แรกอาจช้ากว่า GPT
- **`top_p`**: ไม่รองรับบน O-series — ให้ลบถ้ามี
- **การใช้เครื่องมือ**: โมเดล O-series รองรับเครื่องมือผ่าน Responses API เช่นเดียวกับ GPT แต่คุณภาพการประสานงานแตกต่างตามรุ่น

**คำแนะนำแบบรุก**: ระหว่างสแกน ให้ตรวจสอบว่าแอปเป้าหมายโมเดลใด (ชื่อ deployment, env vars, config) ถ้าเป็น `gpt-4o` หรือต่ำกว่า (ไม่ใช่ gpt-4.1+) แจ้งผู้ใช้ล่วงหน้า:
- การย้ายจะทำงานได้สำหรับข้อความพื้นฐาน, แชท, สตรีม และเครื่องมือบนโมเดลปัจจุบัน
- โมเดลใหม่กว่า (`gpt-5.1`, `gpt-5.2`) มีการประสานงานเครื่องมือที่ดีขึ้น, บังคับใช้ output แบบมีโครงสร้าง, reasoning, และพร้อมให้ใช้งานข้ามภูมิภาค
- ควรพิจารณาอัปเกรด deployment เมื่อพร้อม — ไม่ใช่อุปสรรคในการย้าย

อย่าบล็อกหรือปฏิเสธการย้ายตามเวอร์ชันโมเดล คำแนะนำเป็นข้อมูลเท่านั้น

### GitHub Models ไม่รองรับ Responses API

> **GitHub Models (`models.github.ai`, `models.inference.ai.azure.com`) ไม่รองรับ Responses API**

ถ้าฐานโค้ดมีเส้นทางโค้ดของ GitHub Models (ดูที่ `base_url` ชี้ไปยัง `models.github.ai` หรือ `models.inference.ai.azure.com`) ให้ **ลบออกทั้งหมด** เมื่อย้าย Responses API ต้องใช้ Azure OpenAI, OpenAI หรือ endpoint ท้องถิ่นที่เข้ากันได้ เช่น Ollama ที่รองรับ Responses

การดำเนินการในระหว่างการสแกน:
- แจ้งเตือนการลบเส้นทางโค้ดของ GitHub Models

---

## การย้าย Framework

แอปหลายตัวใช้เฟรมเวิร์กระดับสูงบน OpenAI เมื่อย้ายเฟรมเวิร์กเหล่านี้ API ของเฟรมเวิร์กเองจะเปลี่ยน — ไม่ใช่แค่การเรียก OpenAI เบื้องหลัง

### Microsoft Agent Framework (MAF)

**ตรวจสอบเวอร์ชัน MAF ก่อน** — การย้ายขึ้นกับว่าใช้ MAF 1.0.0+ หรือเบต้า/RC ก่อน 1.0.0

#### MAF 1.0.0+ (agent-framework-openai >= 1.0.0)

`OpenAIChatClient` **ใช้ Responses API อยู่แล้ว** — ไม่ต้องย้าย ถ้าฐานโค้ดใช้ `OpenAIChatCompletionClient` เดิม (ใช้ `chat.completions.create`) ให้แทนที่ด้วย `OpenAIChatClient`

| ก่อน  | หลัง  |
|-------|-------|
| `from agent_framework.openai import OpenAIChatCompletionClient` | `from agent_framework.openai import OpenAIChatClient` |
| `OpenAIChatCompletionClient(...)` | `OpenAIChatClient(...)` |

ตรวจสอบเวอร์ชัน: `python -c "import agent_framework_openai; print(agent_framework_openai.__version__)"`

#### MAF ก่อน 1.0.0 (เบต้า/RC)

ใน MAF ก่อน 1.0.0, `OpenAIChatClient` ใช้ Chat Completions อัปเกรดเป็น `agent-framework-openai>=1.0.0` ที่ `OpenAIChatClient` ใช้ Responses API เป็นค่าเริ่มต้น

ไม่ต้องเปลี่ยนแปลงอื่น — API ของ `Agent` และเครื่องมือยังเหมือนเดิม

### LangChain (`langchain-openai`)

เพิ่ม `use_responses_api=True` ใน `ChatOpenAI()` และอัปเดตการเข้าถึง response จาก `.content` เป็น `.text`

| ก่อน  | หลัง  |
|-------|-------|
| `ChatOpenAI(model=..., base_url=..., api_key=...)` | `ChatOpenAI(model=..., base_url=..., api_key=..., use_responses_api=True)` |
| `result['messages'][-1].content` | `result['messages'][-1].text` |

ตัวอย่างโค้ดก่อน/หลังครบถ้วนดูได้ที่ [cheat-sheet.md](./references/cheat-sheet.md)

---

## คำแนะนำการย้าย Frontend

> **Responses API เป็นเรื่องของฝั่งเซิร์ฟเวอร์** ย้าย backend Python ของคุณ; สัญญา HTTP ของ frontend ควรไม่เปลี่ยนเว้นแต่ backend เป็นตัวผ่านบางๆ — กรณีนั้นควรพิจารณาใช้รูปแบบคำขอ Responses เพื่อลดชั้นแปล หาก frontend เรียก OpenAI โดยตรงด้วยคีย์ฝั่งไคลเอนต์ ให้ย้ายการเรียกเหล่านั้นไปยัง backend ก่อน

### การเลิกใช้ `@microsoft/ai-chat-protocol`

แพ็กเกจ npm `@microsoft/ai-chat-protocol` ถูกเลิกใช้ ควรแทนที่ด้วย [`ndjson-readablestream`](https://www.npmjs.com/package/ndjson-readablestream) หากพบใน frontend:

1. แท็กสคริปต์ CDN:
   ```html
   <!-- Before -->
   <script src="https://cdn.jsdelivr.net/npm/@microsoft/ai-chat-protocol@.../dist/iife/index.js"></script>
   <!-- After -->
   <script src="https://cdn.jsdelivr.net/npm/ndjson-readablestream@1.0.7/dist/ndjson-readablestream.umd.js"></script>
   ```
2. ลบการสร้าง `AIChatProtocolClient` (`new ChatProtocol.AIChatProtocolClient("/chat")`)
3. แทนที่ `client.getStreamedCompletion(messages)` ด้วยการเรียก `fetch()` ตรงไปยัง endpoint สตรีมของ backend
4. แทนที่ `for await (const response of result)` ด้วย `for await (const chunk of readNDJSONStream(response.body))`
5. ปรับการเข้าถึงคุณสมบัติจาก `response.delta.content` / `response.error` เป็น `chunk.delta.content` / `chunk.error`

---

## เป้าหมาย

- ระบุจุดเรียกใน Python ทุกจุดที่ใช้ Chat Completions หรือ Completions แบบเก่ากับ Azure OpenAI
- เสนอแผนและลำดับการย้ายสำหรับฐานโค้ด Python
- แก้ไขอย่างปลอดภัยและน้อยที่สุดเพื่อสลับไป Responses API
- ปรับปรุงผู้เรียกให้ใช้ schema เอาต์พุต Responses โดยตรง; ไม่มี wrapper แบบ backcompat
- รันเทส/ลินท์; แก้ไขบั๊กเล็กน้อยที่เกิดจากการย้าย
- เตรียมชุดเปลี่ยนแปลงขนาดเล็ก, สามารถตรวจสอบได้ และสรุปผลตอนท้ายพร้อม diff (ไม่ต้องคอมมิต)

---

## ข้อจำกัด

- แก้ไขเฉพาะไฟล์ภายใน workspace git เท่านั้น ห้ามเขียนนอกพื้นที่
- ไม่ต้องรักษา shim compatibility ย้อนหลัง; ย้ายโค้ดไป API รูปร่างใหม่
- ไม่ทิ้งคอมเมนต์แปลงผ่านหรือไฟล์สำรอง
- รักษาเซมานติกการสตรีมถ้าเคยใช้มาก่อน หากไม่ใช้ให้ใช้แบบไม่สตรีม
- ขออนุมัติก่อนรันคำสั่งหรือเรียกเครือข่าย หากอยู่ในโหมดอนุมัติ
- ไม่ต้องรันคำสั่ง `git add`/`git commit`/`git push`; สร้างการแก้ไขใน working-tree เท่านั้น

---

## ขั้นตอน 0: ย้าย Azure OpenAI Client (ข้อกำหนดเบื้องต้น)

ถ้าฐานโค้ดใช้ตัวสร้าง `AzureOpenAI` หรือ `AsyncAzureOpenAI` ให้ย้ายไปใช้ `OpenAI` / `AsyncOpenAI` ปกติก่อน ตัวสร้างเฉพาะ Azure นี้ถูกเลิกใช้ใน `openai>=1.108.1`

### ทำไมต้องใช้เส้นทาง API v1?

endpoint ใหม่ `/openai/v1` ใช้ไคลเอนต์มาตรฐาน `OpenAI()` แทน `AzureOpenAI()` ไม่ต้องมีพารามิเตอร์ `api_version` และทำงานเหมือนกันทั้ง OpenAI และ Azure OpenAI โค้ดลูกค้าชุดเดียวรองรับอนาคต — ไม่ต้องจัดการเวอร์ชัน

### การเปลี่ยนแปลงสำคัญ

| ก่อน  | หลัง  |
|-------|-------|
| `AzureOpenAI` | `OpenAI` |
| `AsyncAzureOpenAI` | `AsyncOpenAI` |
| `azure_endpoint` | `base_url` |
| `azure_ad_token_provider` | `api_key` |
| `api_version=...` | ลบออกทั้งหมด |

### รายการทำความสะอาด

- ลบอาร์กิวเมนต์ `api_version` จากการสร้างไคลเอนต์
- ลบตัวแปรแวดล้อม `AZURE_OPENAI_VERSION` / `AZURE_OPENAI_API_VERSION` จาก `.env`, การตั้งค่าแอป, และไฟล์ Bicep/infra
- เปลี่ยนชื่อ `AZURE_OPENAI_CLIENT_ID` → `AZURE_CLIENT_ID` ใน `.env`, การตั้งค่าแอป, Bicep/infra และทดสอบ (ตาม convention ของ Azure Identity SDK)
- ตรวจสอบให้แน่ใจว่ามี `openai>=1.108.1` ใน `requirements.txt` หรือ `pyproject.toml`

### การย้ายตัวแปรแวดล้อม

| ตัวแปรแวดล้อมเก่า | การดำเนินการ | หมายเหตุ |
|---------------------|--------------|----------|
| `AZURE_OPENAI_VERSION` | **ลบออก** | ไม่ต้องใช้ `api_version` กับ endpoint v1 |
| `AZURE_OPENAI_API_VERSION` | **ลบออก** | เช่นเดียวกับด้านบน |
| `AZURE_OPENAI_CLIENT_ID` | **เปลี่ยนชื่อ** → `AZURE_CLIENT_ID` | convention มาตรฐานสำหรับ `ManagedIdentityCredential(client_id=...)` |
| `AZURE_OPENAI_ENDPOINT` | **เก็บไว้** | ยังคงใช้ในการสร้าง `base_url` |
| `AZURE_OPENAI_CHAT_DEPLOYMENT` | **เก็บไว้** | ใช้เป็นพารามิเตอร์ `model` ใน `responses.create` |
| `AZURE_OPENAI_API_KEY` | **เก็บไว้** | ใช้เป็น `api_key` สำหรับการรับรองความถูกต้องด้วยคีย์ |

สำหรับตัวอย่างการตั้งค่าไคลเอนต์ (ซิงค์, แอซิงค์, EntraID, API key, multi-tenant) ดูที่ [cheat-sheet.md](./references/cheat-sheet.md)

---

## ขั้นตอน 1: ตรวจหาจุดเรียกแบบเก่า

รันสคริปต์ [detect_legacy.py](../../../../../.agents/skills/azure-openai-to-responses/scripts/detect_legacy.py) เพื่อตรวจหาจุดเรียกที่ต้องย้ายทั้งหมด:

```bash
python skills/azure-openai-to-responses/scripts/detect_legacy.py .
```

หรือค้นหาแบบแมนนวล — ทุกผลจับคู่ถือเป็นเป้าหมายการย้าย:

```bash
# การเรียกใช้ API แบบเก่า (ต้องเขียนใหม่)
rg "chat\.completions\.create"
rg "ChatCompletion\.create"
rg "Completion\.create"

# ตัวสร้างลูกค้า Azure ที่ถูกยกเลิกการใช้งาน (ต้องเปลี่ยน)
rg "AzureOpenAI\("
rg "AsyncAzureOpenAI\("

# รูปแบบการเข้าถึงข้อมูลตอบกลับ (ต้องอัปเดต)
rg "choices\[0\]\.message\.content"
rg "choices\[0\]\.delta\.content"
rg "choices\[0\]\.message\.function_call"
rg "choices\[0\]\.message\.tool_calls"

# คำนิยามเครื่องมือในรูปแบบซ้อนเก่า (ต้องปรับให้เรียบ)
rg '"function":\s*{\s*"name"'
rg "pydantic_function_tool"

# ผลลัพธ์เครื่องมือในรูปแบบเก่า (ต้องแปลงเป็น function_call_output)
rg '"role":\s*"tool"'
rg '"tool_call_id"'

# พารามิเตอร์ที่ถูกยกเลิก (ต้องลบหรือเปลี่ยนชื่อ)
rg "response_format"
rg "max_tokens\b"        # เปลี่ยนชื่อเป็น max_output_tokens
rg "['\"]seed['\"]"      # remove entirely

# ตัวแปรสภาพแวดล้อมที่ถูกยกเลิก (ล้างข้อมูล)
rg "AZURE_OPENAI_API_VERSION|AZURE_OPENAI_VERSION"
rg "AZURE_OPENAI_CLIENT_ID"  # ควรเป็น AZURE_CLIENT_ID

# จุดสิ้นสุดโมเดล GitHub (ต้องลบ — ไม่รองรับ Responses API)
rg "models\.github\.ai|models\.inference\.ai\.azure"

# รูปแบบเก่าระดับเฟรมเวิร์ก (ต้องอัปเดต)
rg "OpenAIChatCompletionClient"  # MAF 1.0.0+: แทนที่ด้วย OpenAIChatClient
rg "ChatOpenAI\(" | grep -v "use_responses_api"  # LangChain: ต้องใช้ use_responses_api=True

# โครงสร้างการทดสอบ (ต้องอัปเดต)
rg "ChatCompletionChunk|AsyncCompletions\.create" tests/
rg "_azure_ad_token_provider" tests/
rg "prompt_filter_results|content_filter_results" tests/
rg "choices\[0\]" tests/

# การเข้าถึงเนื้อหาข้อผิดพลาดของตัวกรองเนื้อหา (ต้องอัปเดต — โครงสร้างเปลี่ยนแปลง)
rg 'innererror.*content_filter_result|error\.body\["innererror"\]'
rg "content_filter_result\[" # รูปแบบเอกพจน์เก่า — ตอนนี้เป็น content_filter_results (พหูพจน์) ภายในอาร์เรย์ content_filters

# การเรียก HTTP ดิบไปยังจุดสิ้นสุด Chat Completions (ต้องอัปเดต URL)
rg "/openai/deployments/.*/chat/completions"
rg "api-version="
```

### เฮอร์ริสติกส์ (ตรวจหาและเขียนใหม่)

- **Chat Completions client**: `client.chat.completions.create` → `client.responses.create(...)`.
- **ตัวสร้างไคลเอนต์ Azure**: `AzureOpenAI(...)` → `OpenAI(base_url=..., api_key=...)`.
- **เครื่องมือ**: แปลงคำจำกัดความเครื่องมือเรียกใช้ฟังก์ชันจากรูปแบบซ้อน (`{"type": "function", "function": {"name": ...}}`) เป็นรูปแบบ Responses แบบแบน (`{"type": "function", "name": ...}`); ใช้ `tool_choice`; ส่งผลลัพธ์เครื่องมือเป็นรายการ `{"type": "function_call_output", "call_id": ..., "output": ...}` (ไม่ใช่ `{"role": "tool", ...}`).
- **การเดินทางรอบเครื่องมือ**: เมื่อโมเดลส่งคืนการเรียกใช้ฟังก์ชัน ให้ต่อรายการ `response.output` เข้ากับบทสนทนา (ไม่ใช่ dict ด้วยตนเอง `{"role": "assistant", "tool_calls": [...]}`) แล้วต่อรายการ `function_call_output` สำหรับแต่ละผลลัพธ์.
- **ตัวอย่างเครื่องมือแบบ Few-shot**: หากบทสนทนารวมตัวอย่างการเรียกเครื่องมือที่กำหนดค่าคงที่ ให้แปลงเป็นรายการ `{"type": "function_call", "id": "fc_...", "call_id": "fc_...", ...}` + `{"type": "function_call_output", ...}` รหัสต้องขึ้นต้นด้วย `fc_`.
- **`pydantic_function_tool()`**: ตัวช่วยนี้ยังคงสร้างรูปแบบซ้อนแบบเก่าและ **ไม่เข้ากัน** กับ `responses.create()` แทนที่ด้วยคำจำกัดความเครื่องมือด้วยตนเองหรือ wrapper สำหรับแปลงเป็นรูปแบบแบน.
- **มัลติเทิร์น**: เก็บประวัติการสนทนาในแอป; ส่งผ่านเทิร์นก่อนหน้าผ่าน `input`.
- **การจัดรูปแบบ**: แทนที่ `response_format` ระดับหัวข้อของ Chat ด้วย `text.format` ใน Responses รูปแบบมาตรฐาน: `text={"format": {"type": "json_schema", "name": "Output", "strict": True, "schema": {...}}}`.
- **รายการเนื้อหา**: แทนที่ Chat `content[].type: "text"` ด้วย Responses `content[].type: "input_text"` สำหรับเทิร์นของผู้ใช้/ระบบ.
- **รายการเนื้อหารูปภาพ**: แทนที่ Chat `content[].type: "image_url"` ด้วย Responses `content[].type: "input_image"`. ฟิลด์ `image_url` เปลี่ยนจากวัตถุซ้อน `{"url": "..."}` เป็นสตริงแบน ดูชีทสำหรับตัวอย่างก่อน/หลัง.
- **ความพยายามในการให้เหตุผล**: **ย้ายเฉพาะ `reasoning` หากมีอยู่ในโค้ดต้นฉบับเท่านั้น**.
- **การจัดการข้อผิดพลาดกรองเนื้อหา**: โครงสร้างตัวเนื้อหาของข้อผิดพลาดเปลี่ยนไป Chat Completions ใช้ `error.body["innererror"]["content_filter_result"]` (รูปเดียว); Responses API ใช้ `error.body["content_filters"][0]["content_filter_results"]` (รูปพหูพจน์ ในอาเรย์). โค้ดที่เข้าถึง `innererror` จะเกิด `KeyError` ให้เขียนใหม่เป็นเส้นทางใหม่.
- **การเรียก HTTP ดิบ**: หากแอปเรียก Azure OpenAI REST API โดยตรง (ผ่าน `requests`, `httpx` ฯลฯ) ใช้ `/openai/deployments/{name}/chat/completions?api-version=...` ให้เขียนใหม่เป็น `/openai/v1/responses`. ร่างคำขอเปลี่ยน: `messages` → `input`, เพิ่ม `max_output_tokens` และ `store: false`, ลบพารามิเตอร์ query `api-version`. ตัวเนื้อหาคำตอบเปลี่ยน: `choices[0].message.content` → `output[0].content[0].text` (หมายเหตุ: `output_text` เป็นสมบัติ SDK ช่วยเหลือไม่มีใน JSON REST ดิบ). 

---

## ขั้นตอนที่ 2: ใช้การโยกย้าย

### หมายเหตุการโยกย้าย (Chat Completions → Responses)

- **ทำไมต้องโยกย้าย**: Responses เป็น API ที่รวมกันสำหรับข้อความ เครื่องมือ และสตรีมมิง; Chat Completions เป็นของเก่า ด้วย GPT-5 Responses เป็นสิ่งจำเป็นสำหรับประสิทธิภาพสูงสุด.
- **HTTP**: จุดสิ้นสุด Azure เปลี่ยนจาก `/openai/deployments/{name}/chat/completions` เป็น `/openai/v1/responses`.
- **ฟิลด์**: `messages` → `input`, `max_tokens` → `max_output_tokens`. `temperature` เหมือนเดิม.
- **การจัดรูปแบบ**: `response_format` → `text.format` เป็นวัตถุที่ถูกต้อง.
- **รายการเนื้อหา**: แทนที่ Chat `content[].type: "text"` ด้วย Responses `content[].type: "input_text"` สำหรับเทิร์นของระบบ/ผู้ใช้.
- **รายการเนื้อหารูปภาพ**: แทนที่ Chat `content[].type: "image_url"` ด้วย Responses `content[].type: "input_image"`. แบนฟิลด์ `image_url` จาก `{"image_url": {"url": "..."}}` เป็น `{"image_url": "..."}` (สตริงธรรมดา — อาจเป็น URL HTTPS หรือ data URI `data:image/...;base64,...`).

### การแมปพารามิเตอร์อ้างอิง

| Chat Completions | Responses API |
|-----------------|---------------|
| `prompt` | `input` |
| `messages` | `input` (อาเรย์ของรายการ) |
| `max_tokens` | `max_output_tokens` |
| `response_format` | `text.format` (วัตถุ) |
| `temperature` | `temperature` (ไม่เปลี่ยน) |
| `stop` | `stop` (ไม่เปลี่ยน) |
| `frequency_penalty` | `frequency_penalty` (ไม่เปลี่ยน) |
| `presence_penalty` | `presence_penalty` (ไม่เปลี่ยน) |
| `tools` / function-calling | `tools` (ไม่เปลี่ยน) |
| `seed` | **ลบ** (ไม่รองรับ) |
| `store` | `store` (ตั้งค่าเป็น `false`) |
| `content[].type: "text"` | `content[].type: "input_text"` |
| `content[].type: "image_url"` | `content[].type: "input_image"` |
| `"image_url": {"url": "..."}` | `"image_url": "..."` (สตริงแบน) |

สำหรับตัวอย่างโค้ดก่อน/หลังแบบเต็ม ดูได้ที่ [cheat-sheet.md](./references/cheat-sheet.md).

สำหรับการโยกย้ายโครงสร้างทดสอบ (mocks, snapshots, assertions) ดู [test-migration.md](./references/test-migration.md).

สำหรับแก้ไขปัญหาและข้อควรระวัง ดู [troubleshooting.md](./references/troubleshooting.md).

---

## การเก็บข้อมูล & สถานะ

- ตั้งค่า `store: false` ในทุกคำขอ Responses.
- อย่าพึ่งพา ID ข้อความก่อนหน้าหรือบริบทที่เก็บในเซิร์ฟเวอร์ ให้เก็บสถานะในฝั่งไคลเอนต์และลดเมตาดาต้าให้น้อยที่สุด.

---

## เกณฑ์การยอมรับ

### ประตูระดับโค้ด (ทั้งหมดต้องผ่าน)

- [ ] ไม่มีการพบ `rg "chat\.completions\.create|ChatCompletion\.create|Completion\.create"` ในไฟล์ที่โยกย้ายแล้ว.
- [ ] ไม่มีการพบ `rg "AzureOpenAI\(|AsyncAzureOpenAI\("` — ตัวสร้างทั้งหมดใช้ `OpenAI`/`AsyncOpenAI` กับจุดสิ้นสุด v1.
- [ ] ไม่มีการพบ `rg "models\.github\.ai|models\.inference\.ai\.azure"` — ลบเส้นทางโค้ด GitHub Models แล้ว.
- [ ] ไม่มีการพบ `rg "OpenAIChatCompletionClient"` — โค้ด MAF 1.0.0+ ใช้ `OpenAIChatClient` (ซึ่งใช้ Responses API). ในเวอร์ชันก่อน 1.0.0 ให้อัปเกรดเป็น `agent-framework-openai>=1.0.0`.
- [ ] เรียกใช้ `ChatOpenAI(...)` ทุกครั้งต้องรวม `use_responses_api=True`.
- [ ] ไม่มีการพบ `rg "choices\[0\]"` — การเข้าถึงคำตอบทั้งหมดใช้ `resp.output_text` หรือโครงสร้างเอาต์พุต Responses.
- [ ] ไม่มี `response_format` ที่ระดับบน; การส่งออกที่มีโครงสร้างทั้งหมดใช้ `text={"format": {...}}`.
- [ ] `openai>=1.108.1` และ `azure-identity` ใน `requirements.txt` หรือ `pyproject.toml`; ติดตั้งไลบรารีใหม่แล้ว.
- [ ] ตั้งค่า `store=False` ในทุกการเรียก `responses.create`.
- [ ] ไม่มี `api_version` ในการสร้างไคลเอนต์; ลบ `AZURE_OPENAI_API_VERSION` จากไฟล์ env และโครงสร้างพื้นฐาน.

### ประตูโครงสร้างทดสอบ (ทั้งหมดต้องผ่าน)

- [ ] ไม่มีการพบ `rg "ChatCompletionChunk|AsyncCompletions\.create|chat\.completions" tests/`.
- [ ] ไม่มีการพบ `rg "_azure_ad_token_provider" tests/` — assertion ปรับปรุงตรวจสอบ `isinstance(client, AsyncOpenAI)` หรือ `base_url`.
- [ ] ไม่มีการพบ `rg "prompt_filter_results|content_filter_results" tests/` — ลบ mocks ตัวกรองเฉพาะ Azure แล้ว.
- [ ] fixture mock ใช้ `kwargs.get("input")` ไม่ใช่ `kwargs.get("messages")`.
- [ ] Snapshot / golden files ปรับปรุงรูปแบบ Responses สตรีมมิง (ไม่มี `choices[0]`, `function_call`, `logprobs` เป็นต้น).
- [ ] `pytest` ผ่านโดยไม่มีล้มเหลวหลังปรับทุกการทดสอบ.

### ประตูพฤติกรรม (ตรวจสอบด้วยตนเองหรือผ่าน test harness)

- [ ] **การเติมเต็มพื้นฐาน**: `responses.create` แบบไม่สตรีมออกผล `output_text` ที่ไม่ว่าง.
- [ ] **ความเท่าเทียมสตรีม**: หากโค้ดเดิมใช้สตรีม โค้ดที่โยกย้ายจะสตรีมและยกเหตุการณ์ `response.output_text.delta` ที่ผลต่างไม่ว่าง.
- [ ] **เอาต์พุตแบบมีโครงสร้าง**: หากใช้ `text.format` พร้อม `json_schema`, `json.loads(resp.output_text)` ต้องสำเร็จและตรงกับสคีมา.
- [ ] **ลูปเรียกเครื่องมือ**: หากใช้เครื่องมือ โมเดลจะสร้างคำสั่งเรียกเครื่องมือ แอปจะทำงาน และคำขอต่อไปจะส่งคืน `output_text` สุดท้าย (ไม่มีลูปไม่สิ้นสุด).
- [ ] **ความเท่าเทียมแบบ Async**: หากใช้ `AsyncAzureOpenAI` แบบเดิม `AsyncOpenAI` แบบใหม่ต้องทำงานด้วย `await` ได้.
- [ ] **อัตราข้อผิดพลาด**: ไม่มีข้อผิดพลาด 400/401/404 ใหม่เมื่อเทียบกับฐานก่อนโยกย้าย.

### ผลลัพธ์ส่งมอบ

- สรุปรวมไฟล์ที่แก้ไข จำนวนก่อน/หลังการเรียกใช้งานแบบเก่า และขั้นตอนถัดไป.
- เปลี่ยนแปลงเป็นการแก้ไขใน working-tree เท่านั้น (ไม่มี commit).

---

## ความต้องการเวอร์ชัน SDK

| แพ็กเกจ | เวอร์ชันขั้นต่ำ |
|---------|----------------|
| `openai` | `>=1.108.1` |
| `azure-identity` | ล่าสุด (สำหรับการยืนยันตัวตน EntraID) |

---

## เอกสารอ้างอิง

- [ชีทช่วยจำ — ตัวอย่างโค้ดทั้งหมด](./references/cheat-sheet.md)
- [โยกย้ายการทดสอบ — mocks, snapshots, assertions](./references/test-migration.md)
- [แก้ไขปัญหา — ข้อผิดพลาด, ตารางความเสี่ยง, ข้อควรระวัง](./references/troubleshooting.md)
- [detect_legacy.py — ตัวสแกนอัตโนมัติ](../../../../../.agents/skills/azure-openai-to-responses/scripts/detect_legacy.py)
- [Azure OpenAI Starter Kit](https://aka.ms/openai/start)
- [เอกสาร API Azure OpenAI Responses](https://learn.microsoft.com/en-us/azure/ai-foundry/openai/how-to/responses)
- [วงจรชีวิตของเวอร์ชัน API Azure OpenAI](https://learn.microsoft.com/en-us/azure/ai-foundry/openai/api-version-lifecycle?view=foundry-classic&tabs=python#api-evolution)
- [เอกสารอ้างอิง OpenAI Responses API](https://platform.openai.com/docs/api-reference/responses)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ปฏิเสธความรับผิดชอบ**:
เอกสารนี้ได้รับการแปลโดยใช้บริการแปลภาษา AI [Co-op Translator](https://github.com/Azure/co-op-translator) ขณะที่เราพยายามให้ความถูกต้อง โปรดทราบว่าการแปลโดยอัตโนมัติอาจมีข้อผิดพลาดหรือความไม่ถูกต้อง เอกสารต้นฉบับในภาษาต้นทางควรถูกพิจารณาเป็นแหล่งข้อมูลที่เชื่อถือได้ สำหรับข้อมูลที่สำคัญ แนะนำให้ใช้การแปลโดยมนุษย์มืออาชีพ เราไม่รับผิดชอบต่อความเข้าใจผิดหรือการตีความที่ผิดพลาดที่เกิดขึ้นจากการใช้การแปลนี้
<!-- CO-OP TRANSLATOR DISCLAIMER END -->