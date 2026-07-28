---
name: azure-openai-to-responses
license: MIT
---
# ย้ายแอป Python จาก Azure OpenAI Chat Completions ไปยัง Responses API

> **คำแนะนำอย่างเป็นทางการ — ทำตามอย่างเคร่งครัด**
>
> ทักษะนี้จะย้ายฐานโค้ด Python ที่ใช้ Azure OpenAI Chat Completions
> ไปยัง Responses API แบบรวมศูนย์ โปรดทำตามคำแนะนำเหล่านี้อย่างแม่นยำ
> หลีกเลี่ยงการปรับแม็ปพารามิเตอร์เองหรือคิดค้นรูปแบบ API ใหม่

---

## ตัวจุดเริ่มต้น

เปิดใช้งานทักษะนี้เมื่อผู้ใช้ต้องการ:
- ย้ายแอป Python จาก Azure OpenAI Chat Completions ไปยัง Responses API
- อัพเกรดการใช้งาน Python OpenAI SDK ไปยังรูปแบบ API ล่าสุดกับ Azure OpenAI
- เตรียมโค้ด Python สำหรับโมเดล GPT-5 หรือใหม่กว่าที่ต้องการ Responses บน Azure
- เปลี่ยนจากไคลเอนต์ `AzureOpenAI`/`AsyncAzureOpenAI` เป็น `OpenAI`/`AsyncOpenAI` แบบมาตรฐานที่ใช้ปลายทาง v1
- แก้ไขคำเตือนการเลิกใช้ที่เกี่ยวกับตัวสร้าง `AzureOpenAI` หรือ `api_version`

---

## ⚠️ ความเข้ากันได้ของโมเดล — ตรวจสอบก่อน

> **ก่อนย้าย ตรวจสอบให้แน่ใจว่า deployment Azure OpenAI ของคุณรองรับ Responses API**

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

> **หมายเหตุ**: บน Azure OpenAI `max_output_tokens` มีค่าขั้นต่ำ **16** ค่าที่ต่ำกว่า 16 จะส่งคืนข้อผิดพลาด 400 ใช้ค่า 50+ สำหรับการทดสอบแบบรวดเร็ว

หากส่งคืน 404 โมเดลใน deployment นี้ยังไม่รองรับ Responses — ตรวจสอบข้อมูลอ้างอิงด้านล่างหรือเปิดใช้งานใหม่ด้วยโมเดลที่รองรับ

### 2. ตรวจสอบโมเดลที่มีในภูมิภาคของคุณ (แนะนำ)

ใช้เครื่องมือรองรับโมเดลในตัวเพื่อดูว่ามีอะไรพร้อมใช้งานกับ Responses API ในภูมิภาคของคุณ:

```bash
python migrate.py models --subscription YOUR_SUB_ID --location YOUR_REGION
```

เครื่องมือนี้เรียก Azure ARM สดและแสดงแมทริกซ์ความเข้ากันได้ — โมเดลใดรองรับ Responses, การส่งออกแบบมีโครงสร้าง, เครื่องมือ ฯลฯ ใช้ `--filter gpt-5.1,gpt-5.2` เพื่อลดผลลัพธ์หรือ `--json` สำหรับสคริปต์

### 3. อ้างอิงการรองรับโมเดลเต็มรูปแบบ

- **การเรียกดูสด**: `python migrate.py models` (ดูด้านบน — เฉพาะภูมิภาค, อัปเดตเสมอ)
- **เรียกดูความพร้อมใช้งาน**: [ตารางสรุปโมเดลและความพร้อมใช้งานในภูมิภาค](https://learn.microsoft.com/en-us/azure/foundry/foundry-models/concepts/models-sold-directly-by-azure?tabs=global-standard-aoai%2Cglobal-standard&pivots=azure-openai#model-summary-table-and-region-availability)
- **เริ่มต้นใช้งานและคำแนะนำ**: **https://aka.ms/openai/start**

### ⚠️ ข้อจำกัดของโมเดลเก่า

> **คำเตือน**: โมเดลเก่า (ก่อน `gpt-4.1`) อาจไม่รองรับฟีเจอร์ Responses API ทุกอย่างอย่างเต็มที่
>
> จำกัดการใช้งานที่ทราบกับโมเดลเก่า:
> - **พารามิเตอร์ `reasoning`**: ไม่รองรับในหลายโมเดลที่ไม่มี reasoning หากจะย้ายให้ย้ายเฉพาะกรณีที่มี `reasoning` อยู่แล้วในโค้ดต้นทาง
> - **พารามิเตอร์ `seed`**: ไม่รองรับใน Responses API เลย — ลบออกจากคำขอทั้งหมด
> - **ผลลัพธ์แบบมีโครงสร้างผ่าน `text.format`**: โมเดลเก่าอาจไม่บังคับใช้สคีมา JSON แบบ `strict: true` ได้อย่างน่าเชื่อถือ
> - **การประสานเครื่องมือ**: GPT-5+ จัดการการเรียกเครื่องมือเป็นส่วนหนึ่งของ reasoning ภายใน โมเดลเก่าบน Responses ยังใช้งานได้แต่ไม่มีการรวมลึกนี้
> - **ข้อจำกัดอุณหภูมิ**: เมื่อย้ายไป `gpt-5` อุณหภูมิต้องไม่กำหนดหรือกำหนดเป็น `1` โมเดลเก่าไม่มีข้อจำกัดนี้

### โมเดล reasoning ซีรีส์ O (o1, o3-mini, o3, o4-mini)

โมเดลซีรีส์ O มีข้อจำกัดพารามิเตอร์เฉพาะตัว เมื่อย้ายแอปที่มุ่งเป้าไปยังโมเดลซีรีส์ O:

- **`temperature`**: ต้องเป็น `1` (หรือละเว้น) โมเดลซีรีส์ O ไม่รับค่าที่ต่างจากนี้
- **`max_completion_tokens` → `max_output_tokens`**: แอปที่ใช้ `max_completion_tokens` เฉพาะ Azure ต้องเปลี่ยนเป็น `max_output_tokens` ตั้งค่าสูง (4096+) เพราะโทเค็น reasoning นับในขีดจำกัดนี้
- **`reasoning_effort`**: หากแอปใช้ `reasoning_effort` (ต่ำ/กลาง/สูง) ให้เก็บไว้ — Responses API รองรับพารามิเตอร์นี้สำหรับโมเดลซีรีส์ O
- **พฤติกรรมการสตรีม**: โมเดลซีรีส์ O อาจเก็บบัฟเฟอร์ผลลัพธ์จน reasoning เสร็จก่อนส่งเหตุการณ์ delta ข้อความ การสตรีมยังทำงาน แต่ delta แรกอาจช้ากว่าโมเดล GPT
- **`top_p`**: ไม่รองรับในซีรีส์ O — ให้ลบออกหากมี
- **การใช้เครื่องมือ**: โมเดลซีรีส์ O รองรับเครื่องมือผ่าน Responses API เช่นเดียวกับโมเดล GPT แต่คุณภาพการประสานการเรียกเครื่องมือขึ้นกับแต่ละโมเดล

**คำแนะนำเชิงรุก — ระหว่างสแกน**: ตรวจสอบว่าแอปใช้โมเดลใด (ชื่อ deployment, ตัวแปรสภาพแวดล้อม, การตั้งค่า) หากเป็นโมเดลก่อน `gpt-4.1` (ไม่ใช่ gpt-4.1+) แจ้งผู้ใช้ล่วงหน้า:
- การย้ายจะทำงานกับข้อความพื้นฐาน แชท การสตรีม และเครื่องมือบนโมเดลปัจจุบันได้
- โมเดลใหม่กว่า (`gpt-5.1`, `gpt-5.2`) ให้การประสานเครื่องมือที่ดีกว่า การบังคับใช้ผลลัพธ์แบบมีโครงสร้าง reasoning และความพร้อมใช้งานข้ามภูมิภาค
- ควรพิจารณาอัปเกรด deployment เมื่อพร้อม — ไม่มีผลขัดขวางการย้ายตอนนี้

หลีกเลี่ยงการบล็อกหรือปฏิเสธให้ย้ายตามเวอร์ชันโมเดล คำแนะนำนี้เป็นข้อมูลเท่านั้น

### GitHub Models ไม่รองรับ Responses API

> **GitHub Models (`models.github.ai`, `models.inference.ai.azure.com`) ไม่รองรับ Responses API**

หากฐานโค้ดมีเส้นทางโค้ด GitHub Models (ดูที่ `base_url` ชี้ไปยัง `models.github.ai` หรือ `models.inference.ai.azure.com`) **ให้ลบออกทั้งหมด** ในการย้าย Responses API ต้องใช้ Azure OpenAI, OpenAI หรือปลายทางในเครื่องที่เข้ากันได้ (เช่น Ollama ที่รองรับ Responses)

การดำเนินการระหว่างสแกน:
- ให้ติดธงเส้นทางโค้ด GitHub Models เพื่อการลบ

---

## การย้ายเฟรมเวิร์ก

แอปหลายแอปใช้เฟรมเวิร์กระดับสูงบน OpenAI เมื่อย้ายเฟรมเวิร์กเหล่านี้ จะมีการเปลี่ยนแปลง API เฟรมเวิร์กเอง — ไม่ใช่แค่การเรียก OpenAI ขั้นต่ำ

### Microsoft Agent Framework (MAF)

**ตรวจสอบเวอร์ชัน MAF ของคุณก่อน** — การย้ายขึ้นกับว่าคุณใช้ MAF 1.0.0+ หรือเบต้า/rc ก่อน 1.0.0

#### MAF 1.0.0+ (agent-framework-openai >= 1.0.0)

`OpenAIChatClient` **ใช้ Responses API แล้ว** — ไม่ต้องย้าย หากฐานโค้ดยังใช้ `OpenAIChatCompletionClient` แบบเก่า (ที่ใช้ `chat.completions.create`) ให้เปลี่ยนเป็น `OpenAIChatClient`

| ก่อน | หลัง |
|--------|-------|
| `from agent_framework.openai import OpenAIChatCompletionClient` | `from agent_framework.openai import OpenAIChatClient` |
| `OpenAIChatCompletionClient(...)` | `OpenAIChatClient(...)` |

ตรวจสอบเวอร์ชันของคุณด้วย: `python -c "import agent_framework_openai; print(agent_framework_openai.__version__)"`

#### MAF ก่อน 1.0.0 (รุ่นเบต้า/rc)

ใน MAF ก่อน 1.0.0 `OpenAIChatClient` ใช้ Chat Completions อัพเกรดเป็น `agent-framework-openai>=1.0.0` ซึ่ง `OpenAIChatClient` ใช้ Responses API โดยดีฟอลต์

ไม่มีการเปลี่ยนแปลงอื่น — API ของ `Agent` และเครื่องมือเหมือนเดิม

### LangChain (`langchain-openai`)

เพิ่ม `use_responses_api=True` ให้กับ `ChatOpenAI()` และอัพเดตการเข้าถึงผลลัพธ์จาก `.content` เป็น `.text`

| ก่อน | หลัง |
|--------|-------|
| `ChatOpenAI(model=..., base_url=..., api_key=...)` | `ChatOpenAI(model=..., base_url=..., api_key=..., use_responses_api=True)` |
| `result['messages'][-1].content` | `result['messages'][-1].text` |

ดูตัวอย่างโค้ดทั้งก่อนและหลังใน [cheat-sheet.md](./references/cheat-sheet.md)

---

## คำแนะนำการย้ายส่วนหน้า

> **Responses API เป็นเรื่องฝั่งเซิร์ฟเวอร์** ย้าย backend Python ของคุณ ส่วนหน้า (frontend) ควรยังคงตามสัญญา HTTP เดิมเว้นแต่ว่า backend เป็นเพียงชั้นผ่านบาง ๆ — กรณีนั้นให้พิจารณาใช้รูปแบบคำขอ Responses เพื่อกำจัดชั้นแปลง หาก frontend เรียก OpenAI โดยตรงด้วยคีย์ฝั่งไคลเอนต์ ให้ย้ายการเรียกเหล่านั้นไป backend ก่อน

### การเลิกใช้งาน `@microsoft/ai-chat-protocol`

แพ็กเกจ npm `@microsoft/ai-chat-protocol` ถูกเลิกใช้และควรเปลี่ยนเป็น [`ndjson-readablestream`](https://www.npmjs.com/package/ndjson-readablestream) หากพบในส่วนหน้า:

1. แก้แท็กสคริปต์ CDN:
   ```html
   <!-- Before -->
   <script src="https://cdn.jsdelivr.net/npm/@microsoft/ai-chat-protocol@.../dist/iife/index.js"></script>
   <!-- After -->
   <script src="https://cdn.jsdelivr.net/npm/ndjson-readablestream@1.0.7/dist/ndjson-readablestream.umd.js"></script>
   ```
2. ลบการสร้างอินสแตนซ์ `AIChatProtocolClient` (`new ChatProtocol.AIChatProtocolClient("/chat")`)
3. เปลี่ยน `client.getStreamedCompletion(messages)` เป็นเรียก `fetch()` ตรงไปยังจุดสตรีมของ backend
4. เปลี่ยน `for await (const response of result)` เป็น `for await (const chunk of readNDJSONStream(response.body))`
5. ปรับเปลี่ยนการเข้าถึงคุณสมบัติจาก `response.delta.content` / `response.error` เป็น `chunk.delta.content` / `chunk.error`

---

## เป้าหมาย

- ระบุทุกจุดเรียก Python ที่ใช้ Chat Completions หรือ Completions แบบเก่าที่เรียกกับ Azure OpenAI
- เสนอแผนการย้ายและลำดับขั้นสำหรับฐานโค้ด Python
- ใช้การแก้ไขอย่างปลอดภัยและน้อยที่สุดเพื่อสลับไป Responses API
- อัปเดตผู้เรียกเพื่อใช้สคีมาผลลัพธ์ของ Responses; ไม่มีหุ้มหลังความเข้ากันได้
- รันการทดสอบ/ตรวจสอบ; แก้ไขปัญหาเล็กน้อยที่เกิดจากการย้าย
- เตรียมชุดการเปลี่ยนแปลงที่เล็กและตรวจสอบได้ พร้อมสรุปสุดท้ายพร้อมการเปรียบเทียบ (ไม่ต้อง commit)

---

## กฎข้อบังคับ

- แก้ไขเฉพาะไฟล์ในพื้นที่ git เท่านั้น ห้ามเขียนนอกพื้นที่นี้
- ไม่ต้องเก็บไว้ในช่องทางหลังความเข้ากันได้; ย้ายโค้ดไปยังรูปแบบ API ใหม่
- หลีกเลี่ยงการทิ้งคอมเมนต์รอยตาย/เปลี่ยนผ่านหรือไฟล์สำรอง
- รักษาลักษณะการสตรีมหากเคยใช้; มิฉะนั้นใช้แบบไม่สตรีม
- ขออนุมัติก่อนรันคำสั่งหรือเรียกเครือข่ายถ้าอยู่ในโหมดอนุมัติ
- หลีกเลี่ยงการรัน `git add`/`git commit`/`git push`; ผลลัพธ์ต้องเป็นใน working-tree เท่านั้น

---

## ขั้นตอนที่ 0: ย้ายไคลเอนต์ Azure OpenAI (เงื่อนไขเบื้องต้น)

หากฐานโค้ดใช้ตัวสร้าง `AzureOpenAI` หรือ `AsyncAzureOpenAI` ให้ย้ายไปใช้ตัวสร้าง `OpenAI` / `AsyncOpenAI` แบบมาตรฐานก่อน ตัวสร้างเฉพาะ Azure ถูกเลิกใช้ใน `openai>=1.108.1`

### ทำไมต้องใช้ปลายทาง v1 API?

ปลายทางใหม่ `/openai/v1` ใช้ไคลเอนต์ `OpenAI()` แบบมาตรฐานแทน `AzureOpenAI()` ไม่ต้องใช้พารามิเตอร์ `api_version` และทำงานเหมือนกันทั้ง OpenAI และ Azure OpenAI โค้ดไคลเอนต์เดียวกันนี้รองรับอนาคต — ไม่ต้องจัดการเวอร์ชัน

### การเปลี่ยนแปลงสำคัญ

| ก่อน | หลัง |
|--------|-------|
| `AzureOpenAI` | `OpenAI` |
| `AsyncAzureOpenAI` | `AsyncOpenAI` |
| `azure_endpoint` | `base_url` |
| `azure_ad_token_provider` | `api_key` |
| `api_version=...` | ลบทิ้งทั้งหมด |

### รายการล้างข้อมูล

- ลบอาร์กิวเมนต์ `api_version` จากการสร้างไคลเอนต์
- ลบตัวแปรสภาพแวดล้อม `AZURE_OPENAI_VERSION` / `AZURE_OPENAI_API_VERSION` จาก `.env`, การตั้งค่าแอป และไฟล์ Bicep/โครงสร้างพื้นฐาน
- เปลี่ยนชื่อ `AZURE_OPENAI_CLIENT_ID` → `AZURE_CLIENT_ID` ใน `.env`, การตั้งค่าแอป, Bicep/โครงสร้างพื้นฐาน และไฟล์ตัวอย่างทดสอบ (ตามแนวทางมาตรฐาน Azure Identity SDK)
- แน่ใจว่า `openai>=1.108.1` ใน `requirements.txt` หรือ `pyproject.toml`

### ย้ายตัวแปรสภาพแวดล้อม

| ตัวแปรสภาพแวดล้อมเดิม | การดำเนินการ | หมายเหตุ |
|-------------|--------|-------|
| `AZURE_OPENAI_VERSION` | **ลบ** | ไม่ต้องใช้ `api_version` กับปลายทาง v1 |
| `AZURE_OPENAI_API_VERSION` | **ลบ** | เหมือนกันกับด้านบน |
| `AZURE_OPENAI_CLIENT_ID` | **เปลี่ยนชื่อ** → `AZURE_CLIENT_ID` | ตามมาตรฐาน Azure Identity SDK สำหรับ `ManagedIdentityCredential(client_id=...)` |
| `AZURE_OPENAI_ENDPOINT` | **เก็บไว้** | ยังคงต้องใช้สำหรับสร้าง `base_url` |
| `AZURE_OPENAI_CHAT_DEPLOYMENT` | **เก็บไว้** | ใช้เป็นพารามิเตอร์ `model` ใน `responses.create` |
| `AZURE_OPENAI_API_KEY` | **เก็บไว้** | ใช้เป็น `api_key` สำหรับการยืนยันตัวตนด้วยคีย์ |

ตัวอย่างการตั้งค่าไคลเอนต์ (ซิงค์, อะซิงค์, EntraID, คีย์ API, หลาย tenant) ดูใน [cheat-sheet.md](./references/cheat-sheet.md)

---

## ขั้นตอนที่ 1: ตรวจจับจุดเรียกใช้งานแบบเก่า

รันสคริปต์ [detect_legacy.py](../../../../../.agents/skills/azure-openai-to-responses/scripts/detect_legacy.py) เพื่อค้นหาจุดเรียกใช้งานทั้งหมดที่ต้องย้าย:

```bash
python skills/azure-openai-to-responses/scripts/detect_legacy.py .
```

หรือรันการค้นหาเหล่านี้ด้วยตนเอง — ทุกคำที่ตรงเป็นเป้าหมายการย้าย:

```bash
# การเรียก API รุ่นเก่า (ต้องเขียนใหม่)
rg "chat\.completions\.create"
rg "ChatCompletion\.create"
rg "Completion\.create"

# ตัวสร้างไคลเอ็นต์ Azure ที่เลิกใช้แล้ว (ต้องเปลี่ยนใหม่)
rg "AzureOpenAI\("
rg "AsyncAzureOpenAI\("

# รูปแบบการเข้าถึงโครงสร้างการตอบกลับ (ต้องอัปเดต)
rg "choices\[0\]\.message\.content"
rg "choices\[0\]\.delta\.content"
rg "choices\[0\]\.message\.function_call"
rg "choices\[0\]\.message\.tool_calls"

# นิยามเครื่องมือในรูปแบบซ้อนเก่า (ต้องปรับเป็นโครงสร้างแบน)
rg '"function":\s*{\s*"name"'
rg "pydantic_function_tool"

# ผลลัพธ์เครื่องมือในรูปแบบเก่า (ต้องแปลงเป็น function_call_output)
rg '"role":\s*"tool"'
rg '"tool_call_id"'

# พารามิเตอร์ที่เลิกใช้แล้ว (ต้องลบหรือเปลี่ยนชื่อ)
rg "response_format"
rg "max_tokens\b"        # เปลี่ยนชื่อเป็น max_output_tokens
rg "['\"]seed['\"]"      # remove entirely

# ตัวแปรสภาพแวดล้อมที่เลิกใช้แล้ว (ต้องทำความสะอาด)
rg "AZURE_OPENAI_API_VERSION|AZURE_OPENAI_VERSION"
rg "AZURE_OPENAI_CLIENT_ID"  # ควรเป็น AZURE_CLIENT_ID

# จุดเชื่อมต่อโมเดล GitHub (ต้องลบ — API ตอบกลับไม่ได้รับการสนับสนุน)
rg "models\.github\.ai|models\.inference\.ai\.azure"

# รูปแบบเก่าของเฟรมเวิร์กระดับสูง (ต้องอัปเดต)
rg "OpenAIChatCompletionClient"  # MAF 1.0.0+: เปลี่ยนเป็น OpenAIChatClient
rg "ChatOpenAI\(" | grep -v "use_responses_api"  # LangChain: ต้องใช้ use_responses_api=True

# โครงสร้างพื้นฐานการทดสอบ (ต้องอัปเดต)
rg "ChatCompletionChunk|AsyncCompletions\.create" tests/
rg "_azure_ad_token_provider" tests/
rg "prompt_filter_results|content_filter_results" tests/
rg "choices\[0\]" tests/

# การเข้าถึงข้อมูลข้อผิดพลาดตัวกรองเนื้อหา (ต้องอัปเดต — โครงสร้างเปลี่ยนแปลง)
rg 'innererror.*content_filter_result|error\.body\["innererror"\]'
rg "content_filter_result\[" # รูปแบบเอกพจน์เก่า — ตอนนี้เป็น content_filter_results (พหูพจน์) ภายในอาร์เรย์ content_filters

# การเรียก HTTP ดิบไปยังจุดสิ้นสุด Chat Completions (ต้องอัปเดต URL)
rg "/openai/deployments/.*/chat/completions"
rg "api-version="
```

### การประมาณ (ตรวจจับและเขียนใหม่)

- **ไคลเอนต์ Chat Completions**: `client.chat.completions.create` → `client.responses.create(...)`.

- **ตัวสร้างลูกค้า Azure**: `AzureOpenAI(...)` → `OpenAI(base_url=..., api_key=...)`.
- **เครื่องมือ**: แปลงคำจำกัดความเครื่องมือเรียกฟังก์ชันจากรูปแบบซ้อนกัน (`{"type": "function", "function": {"name": ...}}`) เป็นรูปแบบแบนของ Responses (`{"type": "function", "name": ...}`); ใช้ `tool_choice`; ส่งคืนผลลัพธ์ของเครื่องมือเป็นรายการ `{"type": "function_call_output", "call_id": ..., "output": ...}` (ไม่ใช่ `{"role": "tool", ...}`).
- **รอบเครื่องมือ**: เมื่อโมเดลส่งคืนการเรียกฟังก์ชัน ให้แนบรายการ `response.output` ลงในการสนทนา (ไม่ใช่ dict แบบแมนนวล `{"role": "assistant", "tool_calls": [...]}`) จากนั้นแนบรายการ `function_call_output` สำหรับแต่ละผลลัพธ์.
- **ตัวอย่างเครื่องมือแบบ few-shot**: หากการสนทนารวมตัวอย่างการเรียกเครื่องมือแบบกำหนดไว้ล่วงหน้า ให้แปลงเป็นรายการ `{"type": "function_call", "id": "fc_...", "call_id": "fc_...", ...}` + `{"type": "function_call_output", ...}` ต้องให้ ID เริ่มต้นด้วย `fc_`.
- **`pydantic_function_tool()`**: ตัวช่วยนี้ยังคงสร้างรูปแบบซ้อนแบบเก่าและ **ไม่เข้ากันได้** กับ `responses.create()` ให้แทนที่ด้วยคำจำกัดความเครื่องมือแบบแมนนวลหรือใช้ตัวห่อแปลงรูปแบบแบน.
- **หลายรอบ**: รักษาประวัติการสนทนาในแอป; ส่งผ่านรอบก่อนหน้าผ่านรายการ `input`.
- **การจัดรูปแบบ**: แทนที่ `response_format` บนระดับบนสุดของ Chat ด้วย `text.format` ใน Responses รูปแบบมาตรฐาน: `text={"format": {"type": "json_schema", "name": "Output", "strict": True, "schema": {...}}}`.
- **รายการเนื้อหา**: แทนที่ Chat `content[].type: "text"` ด้วย Responses `content[].type: "input_text"` สำหรับรอบของผู้ใช้/ระบบ.
- **รายการเนื้อหารูปภาพ**: แทนที่ Chat `content[].type: "image_url"` ด้วย Responses `content[].type: "input_image"` ฟิลด์ `image_url` เปลี่ยนจากออบเจ็กต์ซ้อน `{"url": "..."}` เป็นสตริงแบน ดูตารางสรุปสำหรับตัวอย่างก่อน/หลัง.
- **ความพยายามในการให้เหตุผล**: **ย้ายเฉพาะ `reasoning` หากมีอยู่แล้วในโค้ดเดิม**.
- **การจัดการข้อผิดพลาดตัวกรองเนื้อหา**: โครงสร้าง body ของข้อผิดพลาดเปลี่ยนจากเดิม Chat Completions ใช้ `error.body["innererror"]["content_filter_result"]` (เอกพจน์); Responses API ใช้ `error.body["content_filters"][0]["content_filter_results"]` (พหูพจน์ อยู่ในอาเรย์) โค้ดที่เข้าถึง `innererror` จะเกิด `KeyError` ให้เขียนใหม่ใช้เส้นทางใหม่.
- **การเรียก HTTP แบบดิบ**: หากแอปเรียก REST API ของ Azure OpenAI โดยตรง (ผ่าน `requests`, `httpx` ฯลฯ) ใช้ `/openai/deployments/{name}/chat/completions?api-version=...` ให้เขียนใหม่เป็น `/openai/v1/responses` ร่างคำขอเปลี่ยน: `messages` → `input` เพิ่ม `max_output_tokens` และ `store: false` ลบพารามิเตอร์ query `api-version` ร่างการตอบกลับเปลี่ยน: `choices[0].message.content` → `output[0].content[0].text` (หมายเหตุ: `output_text` เป็นคุณสมบัติสะดวกของ SDK ซึ่งไม่มีใน REST JSON ต้นฉบับ).

---

## ขั้นตอนที่ 2: ใช้การย้ายข้อมูล

### หมายเหตุการย้ายข้อมูล (Chat Completions → Responses)

- **ทำไมต้องย้าย**: Responses คือ API รวมสำหรับข้อความ, เครื่องมือ, และการสตรีม; Chat Completions เป็นของเดิม กับ GPT-5 จำเป็นต้องใช้ Responses เพื่อประสิทธิภาพดีที่สุด.
- **HTTP**: จุดสิ้นสุด Azure เปลี่ยนจาก `/openai/deployments/{name}/chat/completions` เป็น `/openai/v1/responses`.
- **ฟิลด์**: `messages` → `input`, `max_tokens` → `max_output_tokens` อุณหภูมิยังคงเหมือนเดิม.
- **การจัดรูปแบบ**: `response_format` → `text.format` โดยใช้วัตถุที่ถูกต้อง.
- **รายการเนื้อหา**: แทนที่ Chat `content[].type: "text"` ด้วย Responses `content[].type: "input_text"` สำหรับรอบระบบ/ผู้ใช้.
- **รายการเนื้อหารูปภาพ**: แทนที่ Chat `content[].type: "image_url"` ด้วย Responses `content[].type: "input_image"` แบนฟิลด์ `image_url` จาก `{"image_url": {"url": "..."}}` เป็น `{"image_url": "..."}` (เป็นสตริงธรรมดา — อาจเป็น URL HTTPS หรือ data URI ประเภท `data:image/...;base64,...`).

### แผนที่พารามิเตอร์อ้างอิง

| Chat Completions | Responses API |
|-----------------|---------------|
| `prompt` | `input` |
| `messages` | `input` (อาเรย์ของรายการ) |
| `max_tokens` | `max_output_tokens` |
| `response_format` | `text.format` (วัตถุ) |
| `temperature` | `temperature` (ไม่เปลี่ยนแปลง) |
| `stop` | `stop` (ไม่เปลี่ยนแปลง) |
| `frequency_penalty` | `frequency_penalty` (ไม่เปลี่ยนแปลง) |
| `presence_penalty` | `presence_penalty` (ไม่เปลี่ยนแปลง) |
| `tools` / function-calling | `tools` (ไม่เปลี่ยนแปลง) |
| `seed` | **ลบ** (ไม่รองรับ) |
| `store` | `store` (ตั้งเป็น `false`) |
| `content[].type: "text"` | `content[].type: "input_text"` |
| `content[].type: "image_url"` | `content[].type: "input_image"` |
| `"image_url": {"url": "..."}` | `"image_url": "..."` (สตริงแบน) |

สำหรับตัวอย่างโค้ดก่อน/หลังแบบสมบูรณ์ ดูที่ [cheat-sheet.md](./references/cheat-sheet.md).

สำหรับการย้ายโครงสร้างทดสอบ (mocks, snapshots, assertions) ดูที่ [test-migration.md](./references/test-migration.md).

สำหรับการแก้ไขปัญหาข้อผิดพลาดและปัญหาต่าง ๆ ดูที่ [troubleshooting.md](./references/troubleshooting.md).

---

## การเก็บรักษาข้อมูล & สถานะ

- ตั้งค่า `store: false` ในคำขอ Responses ทั้งหมด.
- อย่าพึ่งพา ID ข้อความก่อนหน้าหรือบริบทที่เก็บไว้ในเซิร์ฟเวอร์; เก็บสถานะแบบจัดการโดยไคลเอนต์และลดเมตาดาต้าให้น้อยที่สุด.

---

## เกณฑ์การยอมรับ

### ด่านระดับโค้ด (ต้องผ่านทั้งหมด)

- [ ] ไม่มีการจับคู่สำหรับ `rg "chat\.completions\.create|ChatCompletion\.create|Completion\.create"` ในไฟล์ที่ย้ายแล้ว.
- [ ] ไม่มีการจับคู่สำหรับ `rg "AzureOpenAI\(|AsyncAzureOpenAI\("` — ตัวสร้างทั้งหมดใช้ `OpenAI`/`AsyncOpenAI` กับจุดสิ้นสุด v1.
- [ ] ไม่มีการจับคู่สำหรับ `rg "models\.github\.ai|models\.inference\.ai\.azure"` — ลบเส้นทางโค้ด GitHub Models.
- [ ] ไม่มีการจับคู่สำหรับ `rg "OpenAIChatCompletionClient"` — โค้ด MAF 1.0.0+ ใช้ `OpenAIChatClient` (ซึ่งใช้ Responses API) ในเวอร์ชันก่อน 1.0.0 ให้ปรับเป็น `agent-framework-openai>=1.0.0`.
- [ ] ทุกการเรียก `ChatOpenAI(...)` รวม `use_responses_api=True`.
- [ ] ไม่มีการจับคู่สำหรับ `rg "choices\[0\]"` — ทุกการเข้าถึงผลลัพธ์ใช้ `resp.output_text` หรือสคีม่าเอาต์พุต Responses.
- [ ] ไม่มี `response_format` บนระดับบนสุด; ทุกผลลัพธ์มีโครงสร้างใช้ `text={"format": {...}}`.
- [ ] ใน `requirements.txt` หรือ `pyproject.toml` มี `openai>=1.108.1` และ `azure-identity`; ติดตั้ง dependencies ใหม่แล้ว.
- [ ] ตั้งค่า `store=False` ในทุกการเรียก `responses.create`.
- [ ] ไม่มี `api_version` ในการสร้างไคลเอนต์; ลบ `AZURE_OPENAI_API_VERSION` ออกจากไฟล์ env และโครงสร้างพื้นฐาน.

### ด่านโครงสร้างทดสอบ (ต้องผ่านทั้งหมด)

- [ ] ไม่มีการจับคู่สำหรับ `rg "ChatCompletionChunk|AsyncCompletions\.create|chat\.completions" tests/`.
- [ ] ไม่มีการจับคู่สำหรับ `rg "_azure_ad_token_provider" tests/` — ปรับปรุง assertions ให้ตรวจสอบ `isinstance(client, AsyncOpenAI)` หรือ `base_url`.
- [ ] ไม่มีการจับคู่สำหรับ `rg "prompt_filter_results|content_filter_results" tests/` — ลบ mocks ตัวกรองเฉพาะ Azure.
- [ ] ใช้ fixture mocks `kwargs.get("input")` แทน `kwargs.get("messages")`.
- [ ] ปรับปรุงไฟล์ snapshot / golden เป็นรูปแบบสตรีมของ Responses (ไม่มี `choices[0]`, `function_call`, `logprobs` ฯลฯ).
- [ ] `pytest` ผ่านโดยไม่มีข้อผิดพลาดหลังจากแก้ไขการทดสอบทั้งหมด.

### ด่านพฤติกรรม (ตรวจสอบด้วยตนเองหรือผ่านชุดทดสอบ)

- [ ] **การคอมพลีตพื้นฐาน**: `responses.create` แบบไม่สตรีมส่งคืน `output_text` ที่ไม่ว่าง.
- [ ] **ความเท่าเทียมแบบสตรีม**: หากโค้ดเดิมใช้การสตรีม โค้ดที่ย้ายจะสตรีมและให้เหตุการณ์ `response.output_text.delta` ที่มีเดลต้าไม่ว่าง.
- [ ] **เอาต์พุตโครงสร้าง**: หากใช้ `text.format` กับ `json_schema` `json.loads(resp.output_text)` ผ่านและตรงกับสคีม่า.
- [ ] **ลูปเรียกเครื่องมือ**: หากใช้เครื่องมือ โมเดลจะส่งคำสั่งเรียกเครื่องมือ, แอปจะประมวลผล, และคำขอต่อไปจะส่งคืน `output_text` สุดท้าย (ไม่มีลูปไม่สิ้นสุด).
- [ ] **ความเท่าเทียมแบบ Async**: หากใช้ `AsyncAzureOpenAI`, การใช้ `AsyncOpenAI` แบบเทียบเท่าทำงานด้วย `await`.
- [ ] **อัตราข้อผิดพลาด**: ไม่มีข้อผิดพลาด 400/401/404 ใหม่เมื่อเทียบกับเส้นฐานก่อนย้าย.

### ผลงานที่ส่งมอบ

- สรุปรายการไฟล์ที่แก้ไข, จำนวนจุดเรียกใช้เดิมและใหม่, และขั้นตอนถัดไป.
- การเปลี่ยนแปลงเป็นการแก้ไขใน working-tree เท่านั้น (ไม่มี commit).

---

## เวอร์ชันที่ต้องใช้ของ SDK

| แพ็กเกจ | เวอร์ชันขั้นต่ำ |
|---------|----------------|
| `openai` | `>=1.108.1` |
| `azure-identity` | ล่าสุด (สำหรับการรับรองความถูกต้อง EntraID) |

---

## แหล่งอ้างอิง

- [ใบสรุปการโกง — ตัวอย่างโค้ดทั้งหมด](./references/cheat-sheet.md)
- [การย้ายทดสอบ — mocks, snapshots, assertions](./references/test-migration.md)
- [แก้ไขปัญหา — ข้อผิดพลาด, ตารางความเสี่ยง, ปัญหาที่พบบ่อย](./references/troubleshooting.md)
- [detect_legacy.py — ตัวสแกนอัตโนมัติ](../../../../../.agents/skills/azure-openai-to-responses/scripts/detect_legacy.py)
- [ชุดเริ่มต้น Azure OpenAI](https://aka.ms/openai/start)
- [เอกสาร Azure OpenAI Responses API](https://learn.microsoft.com/en-us/azure/ai-foundry/openai/how-to/responses)
- [วงจรชีวิตเวอร์ชัน Azure OpenAI API](https://learn.microsoft.com/en-us/azure/ai-foundry/openai/api-version-lifecycle?view=foundry-classic&tabs=python#api-evolution)
- [เอกสารอ้างอิง OpenAI Responses API](https://platform.openai.com/docs/api-reference/responses)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ปฏิเสธความรับผิดชอบ**:
เอกสารนี้ได้รับการแปลโดยใช้บริการแปลภาษา AI [Co-op Translator](https://github.com/Azure/co-op-translator) ขณะที่เราพยายามให้ความถูกต้อง โปรดทราบว่าการแปลโดยอัตโนมัติอาจมีข้อผิดพลาดหรือความไม่ถูกต้อง เอกสารต้นฉบับในภาษาต้นทางควรถูกพิจารณาเป็นแหล่งข้อมูลที่เชื่อถือได้ สำหรับข้อมูลที่สำคัญ แนะนำให้ใช้การแปลโดยมนุษย์มืออาชีพ เราไม่รับผิดชอบต่อความเข้าใจผิดหรือการตีความที่ผิดพลาดที่เกิดขึ้นจากการใช้การแปลนี้
<!-- CO-OP TRANSLATOR DISCLAIMER END -->