# การตั้งค่าคอร์ส

## บทนำ

บทเรียนนี้จะครอบคลุมวิธีการรันตัวอย่างโค้ดของคอร์สนี้

## เข้าร่วมกับผู้เรียนคนอื่นและรับความช่วยเหลือ

ก่อนที่คุณจะเริ่มโคลนรีโปของคุณ เข้าร่วม [AI Agents For Beginners Discord channel](https://aka.ms/ai-agents/discord) เพื่อรับความช่วยเหลือเกี่ยวกับการตั้งค่า คำถามเกี่ยวกับคอร์ส หรือเพื่อเชื่อมต่อกับผู้เรียนคนอื่น ๆ

## โคลนหรือฟอร์ครีโปนี้

เริ่มต้นโดยการโคลนหรือฟอร์คที่ GitHub Repository นี้ ซึ่งจะสร้างเวอร์ชันของตัวเองของเนื้อหาคอร์สเพื่อให้คุณสามารถรัน ทดสอบ และปรับแต่งโค้ดได้!

คุณสามารถทำได้โดยคลิกที่ลิงก์นี้ <a href="https://github.com/microsoft/ai-agents-for-beginners/fork" target="_blank">ฟอร์ครรีโป</a>

ตอนนี้คุณควรมีเวอร์ชันที่ฟอร์คของคอร์สนี้ในลิงก์ต่อไปนี้:

![Forked Repo](../../../translated_images/th/forked-repo.33f27ca1901baa6a.webp)

### โคลนแบบตื้น (แนะนำสำหรับเวิร์กช็อป / Codespaces)

> รีโปเต็มอาจมีขนาดใหญ่ (~3 GB) เมื่อคุณดาวน์โหลดประวัติและไฟล์ทั้งหมด หากคุณแค่เข้าร่วมเวิร์กช็อปหรือแค่ต้องการโฟลเดอร์บทเรียนบางส่วน โคลนแบบตื้น (หรือโคลนแบบห่าง) จะช่วยหลีกเลี่ยงการดาวน์โหลดส่วนใหญ่โดยตัดประวัติและ/หรือข้ามบาง blob

#### โคลนแบบตื้นอย่างรวดเร็ว — ประวัติน้อยที่สุด ไฟล์ครบถ้วน

แทนที่ `<your-username>` ในคำสั่งด้านล่างด้วย URL ฟอร์คของคุณ (หรือ URL ต้นทางถ้าคุณต้องการ)

เพื่อโคลนแค่ประวัติการคอมมิทล่าสุด (ดาวน์โหลดขนาดเล็ก):

```bash|powershell
git clone --depth 1 https://github.com/<your-username>/ai-agents-for-beginners.git
```

เพื่อโคลนสาขาเฉพาะ:

```bash|powershell
git clone --depth 1 --branch <branch-name> https://github.com/<your-username>/ai-agents-for-beginners.git
```

#### โคลนแบบบางส่วน (sparse) — blobs น้อยที่สุด + เฉพาะโฟลเดอร์ที่เลือก

วิธีนี้ใช้การโคลนแบบบางส่วนและ sparse-checkout (ต้องใช้ Git 2.25+ และแนะนำให้ใช้ Git รุ่นใหม่ที่รองรับโคลนแบบบางส่วน):

```bash|powershell
git clone --depth 1 --filter=blob:none --sparse https://github.com/<your-username>/ai-agents-for-beginners.git
```

เข้าไปในโฟลเดอร์รีโป:

```bash|powershell
cd ai-agents-for-beginners
```

จากนั้นระบุโฟลเดอร์ที่คุณต้องการ (ตัวอย่างด้านล่างแสดงสองโฟลเดอร์):

```bash|powershell
git sparse-checkout set 00-course-setup 01-intro-to-ai-agents
```

หลังจากโคลนและตรวจสอบไฟล์แล้ว หากคุณต้องการแค่ไฟล์และต้องการเคลียร์พื้นที่ (ไม่มีประวัติ git) กรุณาลบเมตาดาต้าของรีโป (💀ไม่สามารถย้อนกลับ — คุณจะสูญเสียฟังก์ชันทั้งหมดของ Git: ไม่มีคอมมิท, ดึง, ผลัก, หรือเข้าถึงประวัติ)

```bash
# zsh/bash
rm -rf .git
```

```powershell
# พาวเวอร์เชลล์
Remove-Item -Recurse -Force .git
```

#### การใช้ GitHub Codespaces (แนะนำเพื่อหลีกเลี่ยงการดาวน์โหลดขนาดใหญ่ในเครื่อง)

- สร้าง Codespace ใหม่สำหรับรีโปนี้ผ่าน [GitHub UI](https://github.com/codespaces)

- ในเทอร์มินัลของ Codespace ที่สร้างใหม่ รันคำสั่งโคลนแบบตื้น/บางส่วนด้านบนเพื่อดึงแค่โฟลเดอร์บทเรียนที่คุณต้องการเข้าไปใน workspace ของ Codespace
- เป็นทางเลือก: หลังจากโคลนใน Codespaces แล้ว ลบ .git เพื่อเรียกคืนพื้นที่เพิ่มเติม (ดูคำสั่งลบด้านบน)
- หมายเหตุ: หากคุณต้องการเปิดรีโปตรงใน Codespaces (โดยไม่ต้องโคลนเพิ่ม) โปรดทราบว่า Codespaces จะสร้างสภาพแวดล้อม devcontainer และอาจติดตั้งมากกว่าที่คุณต้องการ การโคลนแบบตื้นภายใน Codespace ใหม่ช่วยให้คุณควบคุมการใช้ดิสก์ได้มากกว่า

#### เคล็ดลับ

- แทนที่ URL โคลนด้วยฟอร์คของคุณเสมอถ้าคุณต้องการแก้ไข/คอมมิท
- หากคุณต้องการประวัติหรือไฟล์เพิ่มเติมในภายหลัง คุณสามารถดึงมาได้ หรือปรับ sparse-checkout เพื่อเพิ่มโฟลเดอร์เพิ่มเติม

## การรันโค้ด

คอร์สนี้มีชุด Jupyter Notebooks ที่คุณสามารถรันเพื่อฝึกปฏิบัติการสร้าง AI Agents

ตัวอย่างโค้ดใช้ **Microsoft Agent Framework (MAF)** กับ `FoundryChatClient` ที่เชื่อมต่อกับ **Microsoft Foundry Agent Service V2** (Responses API) ผ่าน **Microsoft Foundry**

โน้ตบุ๊ก Python ทั้งหมดจะติดป้ายชื่อ `*-python-agent-framework.ipynb`

## ความต้องการ

- Python 3.12+
  - **หมายเหตุ**: หากคุณยังไม่มี Python3.12 ติดตั้ง กรุณาติดตั้งก่อนแล้วสร้าง venv ของคุณโดยใช้ python3.12 เพื่อให้แน่ใจว่าติดตั้งเวอร์ชันที่ถูกต้องจากไฟล์ requirements.txt
  
    > ตัวอย่าง

    สร้างไดเรกทอรี Python venv:

    ```bash|powershell
    python -m venv venv
    ```

    จากนั้นเปิดใช้งานสภาพแวดล้อม venv สำหรับ:

    ```bash
    # zsh/bash
    source venv/bin/activate
    ```
  
    ```dos
    # Command Prompt for Windows
    venv\Scripts\activate
    ```

- .NET 10+: สำหรับโค้ดตัวอย่างที่ใช้ .NET ให้ติดตั้ง [.NET 10 SDK](https://dotnet.microsoft.com/download/dotnet/10.0) หรือเวอร์ชันใหม่กว่า จากนั้นตรวจสอบเวอร์ชัน .NET SDK ที่ติดตั้ง:

    ```bash|powershell
    dotnet --list-sdks
    ```

- **Azure CLI** — จำเป็นสำหรับการยืนยันตัวตน ติดตั้งจาก [aka.ms/installazurecli](https://aka.ms/installazurecli)
- **การสมัคร Azure** — เพื่อเข้าถึง Microsoft Foundry และ Microsoft Foundry Agent Service
- **โปรเจกต์ Microsoft Foundry** — โปรเจกต์ที่มีโมเดลปรับใช้แล้ว (เช่น `gpt-5-mini`) ดูเพิ่มเติมใน [ขั้นตอนที่ 1](#ขั้นตอนที่-1-สร้างโปรเจกต์-microsoft-foundry)

เราได้รวมไฟล์ `requirements.txt` ไว้ที่รูทของรีโปนี้ ซึ่งมีแพ็กเกจ Python ที่ต้องการทั้งหมดเพื่อรันตัวอย่างโค้ด

คุณสามารถติดตั้งโดยรันคำสั่งต่อไปนี้ในเทอร์มินัลที่รูทของรีโป:

```bash|powershell
pip install -r requirements.txt
```

เราแนะนำให้สร้างสภาพแวดล้อม Python แบบเสมือนเพื่อหลีกเลี่ยงความขัดแย้งและปัญหา

## ตั้งค่า VSCode

ตรวจสอบให้แน่ใจว่าคุณใช้เวอร์ชัน Python ที่ถูกต้องใน VSCode

![image](https://github.com/user-attachments/assets/a85e776c-2edb-4331-ae5b-6bfdfb98ee0e)

## ตั้งค่า Microsoft Foundry และ Microsoft Foundry Agent Service

### ขั้นตอนที่ 1: สร้างโปรเจกต์ Microsoft Foundry

คุณต้องมี Microsoft Foundry **hub** และ **โปรเจกต์** ที่มีโมเดลปรับใช้เพื่อรันโน้ตบุ๊ก

1. ไปที่ [ai.azure.com](https://ai.azure.com) และลงชื่อเข้าใช้ด้วยบัญชี Azure ของคุณ
2. สร้าง **hub** ใหม่ (หรือใช้ที่มีอยู่แล้ว) ดู: [ภาพรวมทรัพยากร Hub](https://learn.microsoft.com/azure/ai-foundry/concepts/ai-resources)
3. ภายใน hub ให้สร้าง **โปรเจกต์**
4. ปรับใช้โมเดล (เช่น `gpt-5-mini`) จาก **Models + Endpoints** → **Deploy model**

### ขั้นตอนที่ 2: ดึง Endpoint โปรเจกต์และชื่อการปรับใช้โมเดลของคุณ

จากโปรเจกต์ของคุณในพอร์ทัล Microsoft Foundry:

- **Project Endpoint** — ไปที่หน้า **Overview** และคัดลอก URL endpoint

![Project Connection String](../../../translated_images/th/project-endpoint.8cf04c9975bbfbf1.webp)

- **Model Deployment Name** — ไปที่ **Models + Endpoints** เลือกโมเดลที่คุณปรับใช้และจดชื่อ **Deployment name** (เช่น `gpt-5-mini`)

### ขั้นตอนที่ 3: ลงชื่อเข้าใช้ Azure ด้วย `az login`

โน้ตบุ๊กทั้งหมดใช้ **`AzureCliCredential`** สำหรับการยืนยันตัวตน — ไม่ต้องจัดการกับ API keys ซึ่งต้องเซ็นชื่อเข้าใช้ผ่าน Azure CLI

1. **ติดตั้ง Azure CLI** หากคุณยังไม่มี: [aka.ms/installazurecli](https://aka.ms/installazurecli)

2. **เซ็นชื่อเข้าใช้** โดยรันคำสั่ง:

    ```bash|powershell
    az login
    ```

    หรือถ้าคุณอยู่ในสภาพแวดล้อมระยะไกล/Codespace ที่ไม่มีเบราว์เซอร์:

    ```bash|powershell
    az login --use-device-code
    ```

3. **เลือกการสมัครของคุณ** ถ้ามี prompt — เลือกตัวที่มีโปรเจกต์ Foundry ของคุณ

4. **ตรวจสอบ** ว่าคุณลงชื่อเข้าใช้แล้ว:

    ```bash|powershell
    az account show
    ```

> **ทำไมต้องใช้ `az login`?** โน้ตบุ๊กยืนยันตัวตนด้วย `AzureCliCredential` จากแพ็กเกจ `azure-identity` ซึ่งหมายความว่าเซสชัน Azure CLI ของคุณจะเป็นตัวให้ข้อมูลรับรอง — ไม่มี API keys หรือความลับในไฟล์ `.env` ของคุณ นี่คือ [แนวทางปฏิบัติด้านความปลอดภัยที่ดีที่สุด](https://learn.microsoft.com/azure/developer/ai/keyless-connections)

### ขั้นตอนที่ 4: สร้างไฟล์ `.env` ของคุณ

คัดลอกไฟล์ตัวอย่าง:

```bash
# zsh/bash
cp .env.example .env
```

```powershell
# PowerShell
Copy-Item .env.example .env
```

เปิดไฟล์ `.env` แล้วกรอกค่าต่อไปนี้:

```env
AZURE_AI_PROJECT_ENDPOINT=https://<your-project>.services.ai.azure.com/api/projects/<your-project-id>
AZURE_AI_MODEL_DEPLOYMENT_NAME=gpt-5-mini
```

| ตัวแปร | ที่ที่หาได้ |
|----------|-----------------|
| `AZURE_AI_PROJECT_ENDPOINT` | พอร์ทัล Foundry → โปรเจกต์ของคุณ → หน้า **Overview** |
| `AZURE_AI_MODEL_DEPLOYMENT_NAME` | พอร์ทัล Foundry → **Models + Endpoints** → ชื่อโมเดลที่คุณปรับใช้ |

แค่นี้สำหรับบทเรียนส่วนใหญ่! โน้ตบุ๊กจะยืนยันตัวตนโดยอัตโนมัติผ่านเซสชัน `az login` ของคุณ

### ขั้นตอนที่ 5: ติดตั้ง dependencies ของ Python

```bash|powershell
pip install -r requirements.txt
```

แนะนำให้รันนี้ภายในสภาพแวดล้อมเสมือนที่คุณสร้างไว้ก่อนหน้า

## การตั้งค่าเพิ่มเติมสำหรับบทเรียนที่ 5 (Agentic RAG)

บทเรียนที่ 5 ใช้ **Azure AI Search** สำหรับการสร้างแบบเสริมที่ดึงข้อมูล หากคุณวางแผนจะรันบทเรียนนั้น ให้เพิ่มตัวแปรเหล่านี้ไปยังไฟล์ `.env` ของคุณ:

| ตัวแปร | ที่ที่หาได้ |
|----------|-----------------|
| `AZURE_SEARCH_SERVICE_ENDPOINT` | พอร์ทัล Azure → ทรัพยากร **Azure AI Search** ของคุณ → **Overview** → URL |
| `AZURE_SEARCH_API_KEY` | พอร์ทัล Azure → ทรัพยากร **Azure AI Search** ของคุณ → **Settings** → **Keys** → คีย์ผู้ดูแลระบบหลัก |

## การตั้งค่าเพิ่มเติมสำหรับบทเรียนที่เรียกใช้ Azure OpenAI โดยตรง (บทเรียน 6 และ 8)

โน้ตบุ๊กบางส่วนในบทเรียน 6 และ 8 เรียกใช้ **Azure OpenAI** โดยตรง (ใช้ **Responses API**) แทนการผ่านโปรเจกต์ Microsoft Foundry ตัวอย่างเหล่านี้เคยใช้ GitHub Models ซึ่งเลิกใช้แล้ว (จะหยุดใช้ในกรกฎาคม 2026) และไม่รองรับ Responses API หากคุณวางแผนจะรันตัวอย่างเหล่านั้น ให้เพิ่มตัวแปรเหล่านี้ไปยังไฟล์ `.env` ของคุณ:

| ตัวแปร | ที่ที่หาได้ |
|----------|-----------------|
| `AZURE_OPENAI_ENDPOINT` | พอร์ทัล Azure → ทรัพยากร **Azure OpenAI** ของคุณ → **Keys and Endpoint** → Endpoint (เช่น `https://<your-resource>.openai.azure.com`) |
| `AZURE_OPENAI_DEPLOYMENT` | ชื่อโมเดลที่คุณปรับใช้ (เช่น `gpt-5-mini`) ที่รองรับ Responses API |
| `AZURE_OPENAI_API_KEY` | ทางเลือก — เฉพาะถ้าคุณใช้การยืนยันตัวตนแบบคีย์แทน `az login` / Entra ID |

> Responses API ใช้ endpoint `/openai/v1/` ที่เสถียร จึงไม่จำเป็นต้องระบุ `api-version` เซ็นชื่อเข้าใช้ด้วย `az login` เพื่อใช้การยืนยันตัวตนแบบ Entra ID แบบไม่ต้องใช้คีย์

## ผู้ให้บริการทางเลือก: MiniMax (เข้ากันได้กับ OpenAI)

[MiniMax](https://platform.minimaxi.com/) มีโมเดลที่รองรับบริบทขนาดใหญ่ (สูงสุด 204K tokens) ผ่าน API ที่เข้ากันได้กับ OpenAI เนื่องจาก Microsoft Agent Framework's `OpenAIChatClient` ใช้กับ endpoint ที่รองรับ OpenAI-compatible ได้ คุณจึงสามารถใช้ MiniMax เป็นตัวเลือกแทน Azure OpenAI หรือ OpenAI ได้โดยตรง

เพิ่มตัวแปรเหล่านี้ไปยังไฟล์ `.env` ของคุณ:

| ตัวแปร | ที่ที่หาได้ |
|----------|-----------------|
| `MINIMAX_API_KEY` | [MiniMax Platform](https://platform.minimaxi.com/) → API Keys |
| `MINIMAX_BASE_URL` | ใช้ `https://api.minimax.io/v1` (ค่าปกติ) |
| `MINIMAX_MODEL_ID` | ชื่อโมเดลที่จะใช้ (เช่น `MiniMax-M3`) |

**ตัวอย่างโมเดล**: `MiniMax-M3` (แนะนำ), `MiniMax-M2.7`, `MiniMax-M2.7-highspeed` (ตอบสนองเร็วกว่า) ชื่อและความพร้อมใช้งานของโมเดลอาจเปลี่ยนแปลงตามเวลา และการเข้าถึงโมเดลขึ้นอยู่กับบัญชีหรือภูมิภาคของคุณ — ตรวจสอบที่ [MiniMax Platform](https://platform.minimaxi.com/) สำหรับรายการล่าสุด หาก `MiniMax-M3` ไม่พร้อมใช้งานสำหรับบัญชีของคุณ ให้ตั้งค่า `MINIMAX_MODEL_ID` เป็นโมเดลที่คุณเข้าถึงได้ (เช่น `MiniMax-M2.7`)

ตัวอย่างโค้ดที่ใช้ `OpenAIChatClient` (เช่น บทเรียน 14 workflow การจองโรงแรม) จะตรวจจับและใช้การตั้งค่า MiniMax ของคุณโดยอัตโนมัติเมื่อ `MINIMAX_API_KEY` ถูกตั้งค่า

## ผู้ให้บริการทางเลือก: Foundry Local (รันโมเดลบนอุปกรณ์ของคุณ)

[Foundry Local](https://foundrylocal.ai) คือรันไทม์น้ำหนักเบาที่ดาวน์โหลด จัดการ และให้บริการโมเดลภาษา **ทั้งหมดบนเครื่องของคุณเอง** ผ่าน API ที่เข้ากันได้กับ OpenAI — ไม่มีคลาวด์ ไม่มีการสมัคร Azure และไม่มี API keys เป็นตัวเลือกที่ยอดเยี่ยมสำหรับการพัฒนาออฟไลน์ ทดลองโดยไม่เสียค่าใช้จ่ายคลาวด์ หรือเก็บข้อมูลในเครื่อง

เนื่องจาก Microsoft Agent Framework's `OpenAIChatClient` ทำงานกับ endpoint ที่เข้ากันได้กับ OpenAI ได้ Foundry Local จึงเป็นตัวเลือกแทนแบบ local ที่ใช้งานได้แทน Azure OpenAI

**1. ติดตั้ง Foundry Local**

```bash
# วินโดวส์
winget install Microsoft.FoundryLocal

# แมคโอเอส
brew install foundrylocal
```

**2. ดาวน์โหลดและรันโมเดล** (นี่ยังเริ่มบริการ local ด้วย):

```bash
foundry model list          # ดูโมเดลที่มีอยู่
foundry model run phi-4-mini
```

**3. ติดตั้ง Python SDK** ที่ใช้ในการค้นหา endpoint local:

```bash
pip install foundry-local-sdk
```

**4. ชี้ Microsoft Agent Framework ไปยังโมเดล local ของคุณ:**

```python
from foundry_local import FoundryLocalManager
from agent_framework.openai import OpenAIChatClient

# ดาวน์โหลด (ถ้าจำเป็น) และให้บริการโมเดลในเครื่อง จากนั้นค้นหา endpoint/port
manager = FoundryLocalManager("phi-4-mini")

chat_client = OpenAIChatClient(
    base_url=manager.endpoint,      # เช่น http://localhost:<port>/v1
    api_key=manager.api_key,        # เสมอ "ไม่จำเป็น" สำหรับ Foundry Local
    model_id=manager.get_model_info("phi-4-mini").id,
)

agent = chat_client.as_agent(
    name="LocalAgent",
    instructions="You are a helpful assistant running fully on-device.",
)
```

> **หมายเหตุ:** Foundry Local เปิดเผย endpoint **Chat Completions** ที่เข้ากันได้กับ OpenAI ใช้สำหรับการพัฒนาท้องถิ่นและสถานการณ์ออฟไลน์ สำหรับชุดฟีเจอร์เต็มรูปแบบของ **Responses API** (สนทนาแบบรัฐ, การจัดการเครื่องมือที่ลึก, และการพัฒนาแบบ agent) ให้ใช้ **Azure OpenAI** หรือ **โปรเจกต์ Microsoft Foundry** ตามที่แสดงในบทเรียน ดู [เอกสาร Foundry Local](https://foundrylocal.ai) สำหรับแคตตาล็อกโมเดลและการสนับสนุนแพลตฟอร์มล่าสุด

## การตั้งค่าเพิ่มเติมสำหรับบทเรียนที่ 8 (Bing Grounding Workflow)


โน้ตบุ๊กเวิร์กโฟลว์มีเงื่อนไขในบทเรียนที่ 8 ใช้ **Bing grounding** ผ่าน Microsoft Foundry หากคุณวางแผนจะรันตัวอย่างนั้น ให้เพิ่มตัวแปรนี้ลงในไฟล์ `.env` ของคุณ:

| ตัวแปร | ที่หาได้จากที่ไหน |
|----------|-----------------|
| `BING_CONNECTION_ID` | พอร์ทัล Microsoft Foundry → โครงการของคุณ → **การจัดการ** → **ทรัพยากรที่เชื่อมต่อ** → การเชื่อมต่อ Bing ของคุณ → คัดลอกรหัสการเชื่อมต่อ |

## การแก้ไขปัญหา

### ข้อผิดพลาดการยืนยันใบรับรอง SSL บน macOS

หากคุณใช้ macOS และพบข้อผิดพลาดเช่น:

```plaintext
ssl.SSLCertVerificationError: [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: self-signed certificate in certificate chain
```

นี่เป็นปัญหาที่ทราบกันใน Python บน macOS ซึ่งใบรับรอง SSL ของระบบไม่ได้รับความไว้วางใจโดยอัตโนมัติ ลองแก้ไขตามวิธีด้านล่างนี้เป็นลำดับ:

**ตัวเลือกที่ 1: รันสคริปต์ติดตั้งใบรับรองของ Python (แนะนำ)**

```bash
# แทนที่ 3.XX ด้วยเวอร์ชัน Python ที่คุณติดตั้ง (เช่น 3.12 หรือ 3.13):
/Applications/Python\ 3.XX/Install\ Certificates.command
```

**ตัวเลือกที่ 2: ใช้ `connection_verify=False` ในโน้ตบุ๊กของคุณ (เฉพาะโน้ตบุ๊ก GitHub Models)**

ในโน้ตบุ๊กบทเรียนที่ 6 (`06-building-trustworthy-agents/code_samples/06-system-message-framework.ipynb`) มีวิธีแก้ไขที่ถูกคอมเมนต์ไว้แล้ว ยกเลิกการคอมเมนต์ `connection_verify=False` เมื่อสร้างไคลเอนต์:

```python
client = ChatCompletionsClient(
    endpoint=endpoint,
    credential=AzureKeyCredential(token),
    connection_verify=False,  # ปิดการตรวจสอบ SSL หากคุณพบข้อผิดพลาดของใบรับรอง
)
```

> **⚠️ คำเตือน:** การปิดการยืนยัน SSL (`connection_verify=False`) ลดระดับความปลอดภัยโดยข้ามการตรวจสอบใบรับรอง ใช้เฉพาะเป็นการแก้ไขชั่วคราวในสภาพแวดล้อมการพัฒนาเท่านั้น ห้ามใช้ในระบบจริง

**ตัวเลือกที่ 3: ติดตั้งและใช้ `truststore`**

```bash
pip install truststore
```

จากนั้นเพิ่มโค้ดต่อไปนี้ที่ด้านบนของโน้ตบุ๊กหรือสคริปต์ก่อนเรียกใช้งานเครือข่ายใดๆ:

```python
import truststore
truststore.inject_into_ssl()
```

## ติดขัดตรงไหนไหม?

หากคุณมีปัญหาในการรันการตั้งค่านี้ เข้าร่วมได้ที่ <a href="https://discord.gg/kzRShWzttr" target="_blank">Azure AI Community Discord</a> หรือ <a href="https://github.com/microsoft/ai-agents-for-beginners/issues?WT.mc_id=academic-105485-koreyst" target="_blank">สร้างรายงานปัญหา</a>.

## บทเรียนถัดไป

ตอนนี้คุณพร้อมที่จะรันโค้ดสำหรับหลักสูตรนี้แล้ว ขอให้มีความสุขกับการเรียนรู้เพิ่มเติมเกี่ยวกับโลกของ AI Agents!

[แนะนำ AI Agents และกรณีการใช้งาน Agent](../01-intro-to-ai-agents/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ปฏิเสธความรับผิดชอบ**:
เอกสารนี้ได้รับการแปลโดยใช้บริการแปลภาษา AI [Co-op Translator](https://github.com/Azure/co-op-translator) ขณะที่เราพยายามให้ความถูกต้อง โปรดทราบว่าการแปลโดยอัตโนมัติอาจมีข้อผิดพลาดหรือความไม่ถูกต้อง เอกสารต้นฉบับในภาษาต้นทางควรถูกพิจารณาเป็นแหล่งข้อมูลที่เชื่อถือได้ สำหรับข้อมูลที่สำคัญ แนะนำให้ใช้การแปลโดยมนุษย์มืออาชีพ เราไม่รับผิดชอบต่อความเข้าใจผิดหรือการตีความที่ผิดพลาดที่เกิดขึ้นจากการใช้การแปลนี้
<!-- CO-OP TRANSLATOR DISCLAIMER END -->