# การตั้งค่าหลักสูตร

## บทนำ

บทเรียนนี้จะครอบคลุมวิธีการรันตัวอย่างโค้ดของหลักสูตรนี้

## เข้าร่วมกับผู้เรียนคนอื่นๆ และขอรับความช่วยเหลือ

ก่อนที่คุณจะเริ่มโคลนรีโปของคุณ ให้เข้าร่วมกับ [ช่อง Discord AI Agents For Beginners](https://aka.ms/ai-agents/discord) เพื่อขอความช่วยเหลือเกี่ยวกับการตั้งค่า ถามคำถามเกี่ยวกับหลักสูตร หรือเชื่อมต่อกับผู้เรียนอื่นๆ

## โคลน หรือ ฟอร์ก รีโปนี้

เพื่อเริ่มต้น กรุณาโคลนหรือฟอร์ก GitHub Repository นี้ ซึ่งจะทำให้คุณมีเวอร์ชันของวัสดุหลักสูตรเป็นของตัวเองเพื่อให้คุณสามารถรัน ทดสอบ และปรับแต่งโค้ดได้!

คุณสามารถทำได้โดยคลิกที่ลิงก์ <a href="https://github.com/microsoft/ai-agents-for-beginners/fork" target="_blank">เพื่อฟอร์กรีโป</a>

ตอนนี้คุณควรมีเวอร์ชันฟอร์กของหลักสูตรนี้ในลิงก์ต่อไปนี้:

![Forked Repo](../../../translated_images/th/forked-repo.33f27ca1901baa6a.webp)

### โคลนแบบตื้น (แนะนำสำหรับเวิร์กช็อป / Codespaces)

  >รีโปเต็มสามารถมีขนาดใหญ่ (~3 GB) เมื่อคุณดาวน์โหลดประวัติทั้งหมดและไฟล์ทั้งหมด หากคุณเข้าร่วมเฉพาะเวิร์กช็อปหรือต้องการเพียงโฟลเดอร์บทเรียนไม่กี่โฟลเดอร์ โคลนแบบตื้น (หรือโคลนแบบห่างๆ) จะดาวน์โหลดน้อยกว่ามาก

#### โคลนแบบตื้นอย่างรวดเร็ว — ประวัติน้อยที่สุด, ไฟล์ทั้งหมด

แทนที่ `<your-username>` ในคำสั่งด้านล่างด้วย URL ฟอร์กของคุณ (หรือ URL upstream หากคุณต้องการ)

เพื่อโคลนเฉพาะประวัติ commit ล่าสุด (ดาวน์โหลดขนาดเล็ก):

```bash
git clone --depth 1 https://github.com/<your-username>/ai-agents-for-beginners.git
```

เพื่อโคลนสาขาที่ระบุ:

```bash
git clone --depth 1 --branch <branch-name> https://github.com/<your-username>/ai-agents-for-beginners.git
```

#### โคลนแบบบางส่วน (sparse) — บลอบน้อยที่สุด + โฟลเดอร์ที่เลือกเท่านั้น

วิธีนี้ใช้ partial clone และ sparse-checkout (ต้องใช้ Git 2.25+ และแนะนำให้ใช้ Git รุ่นใหม่ที่รองรับ partial clone):

```bash
git clone --depth 1 --filter=blob:none --sparse https://github.com/<your-username>/ai-agents-for-beginners.git
```

เข้าไปในโฟลเดอร์รีโป:

```bash
cd ai-agents-for-beginners
```

แล้วระบุว่าโฟลเดอร์ใดที่คุณต้องการ (ตัวอย่างด้านล่างแสดงสองโฟลเดอร์):

```bash
git sparse-checkout set 00-course-setup 01-intro-to-ai-agents
```

หลังจากโคลนและตรวจสอบไฟล์แล้ว หากคุณต้องการเฉพาะไฟล์และต้องการปลดปล่อยพื้นที่ (ไม่เก็บประวัติ git) กรุณาลบ metadata ของรีโป (💀 ไม่สามารถย้อนกลับได้ — คุณจะสูญเสียฟังก์ชันการทำงาน Git ทั้งหมด):

```bash
# zsh/bash
rm -rf .git
```

```powershell
# PowerShell
Remove-Item -Recurse -Force .git
```

#### การใช้ GitHub Codespaces (แนะนำเพื่อหลีกเลี่ยงการดาวน์โหลดขนาดใหญ่ในเครื่อง)

- สร้าง Codespace ใหม่สำหรับรีโปนี้ผ่าน [GitHub UI](https://github.com/codespaces)  

- ในเทอร์มินัลของ Codespace ที่สร้างใหม่ ให้รันคำสั่ง shallow/sparse clone ข้างต้นเพื่อดึงเฉพาะโฟลเดอร์บทเรียนที่คุณต้องการมาไว้ในพื้นที่ทำงานของ Codespace
- ตัวเลือก: หลังโคลนภายใน Codespaces ให้ลบ .git เพื่อคืนพื้นที่ว่างเพิ่มเติม (ดูคำสั่งลบด้านบน)
- หมายเหตุ: หากคุณต้องการเปิดรีโปโดยตรงใน Codespaces (โดยไม่ต้องโคลนเพิ่ม) ให้ทราบว่า Codespaces จะสร้างสภาพแวดล้อม devcontainer และอาจจัดเตรียมมากกว่าที่คุณต้องการ

#### เคล็ดลับ

- ให้แทนที่ URL โคลนด้วยฟอร์กของคุณเสมอหากคุณต้องการแก้ไข/commit
- หากคุณต้องการประวัติหรือไฟล์เพิ่มเติมในภายหลัง คุณสามารถ fetch หรือปรับ sparse-checkout เพื่อรวมโฟลเดอร์เพิ่มเติมได้

## การรันโค้ด

หลักสูตรนี้มีชุด Jupyter Notebooks ที่คุณสามารถรันเพื่อรับประสบการณ์จริงในการสร้าง AI Agents

ตัวอย่างโค้ดใช้ **Microsoft Agent Framework (MAF)** กับ `FoundryChatClient` ซึ่งเชื่อมต่อกับ **Microsoft Foundry Agent Service V2** (Responses API) ผ่าน **Microsoft Foundry**

ไฟล์โน้ตบุ๊ก Python ทั้งหมดจะถูกตั้งชื่อว่า `*-python-agent-framework.ipynb`

## ข้อกำหนด

- Python 3.12+
  - **หมายเหตุ**: หากคุณยังไม่มี Python3.12 ให้ติดตั้งก่อน จากนั้นสร้าง venv โดยใช้ python3.12 เพื่อให้แน่ใจว่าติดตั้งเวอร์ชันที่ถูกต้องจากไฟล์ requirements.txt
  
    >ตัวอย่าง

    สร้างไดเรกทอรี Python venv:

    ```bash
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

- .NET 10+: สำหรับโค้ดตัวอย่างที่ใช้ .NET ให้ติดตั้ง [.NET 10 SDK](https://dotnet.microsoft.com/download/dotnet/10.0) หรือตัวใหม่กว่าก่อน จากนั้นตรวจสอบเวอร์ชัน .NET SDK ที่ติดตั้ง:

    ```bash
    dotnet --list-sdks
    ```

- **Azure CLI** — จำเป็นสำหรับการพิสูจน์ตัวตน ติดตั้งได้จาก [aka.ms/installazurecli](https://aka.ms/installazurecli)
- **Azure Subscription** — สำหรับการเข้าถึง Microsoft Foundry และ Microsoft Foundry Agent Service
- **Microsoft Foundry Project** — โครงการที่มีโมเดลที่ติดตั้งอยู่ (เช่น `gpt-5-mini`) ดู [ขั้นตอนที่ 1](#ขั้นตอนที่-1-สร้างโปรเจกต์-microsoft-foundry) ด้านล่าง

เราได้รวมไฟล์ `requirements.txt` ไว้ในโฟลเดอร์รากของรีโปนี้ ซึ่งบรรจุแพ็กเกจ Python ที่จำเป็นทั้งหมดสำหรับการรันตัวอย่างโค้ด

คุณสามารถติดตั้งโดยรันคำสั่งต่อไปนี้ในเทอร์มินัลที่โฟลเดอร์รากของรีโป:

```bash
pip install -r requirements.txt
```

เราแนะนำให้สร้างสภาพแวดล้อม Python เสมือนเพื่อหลีกเลี่ยงความขัดแย้งและปัญหาใดๆ

## ตั้งค่า VSCode

ตรวจสอบให้แน่ใจว่าคุณใช้เวอร์ชัน Python ที่ถูกต้องใน VSCode

![image](https://github.com/user-attachments/assets/a85e776c-2edb-4331-ae5b-6bfdfb98ee0e)

## การตั้งค่า Microsoft Foundry และ Microsoft Foundry Agent Service

### ขั้นตอนที่ 1: สร้างโปรเจกต์ Microsoft Foundry

คุณต้องมี **hub** และ **project** ใน Microsoft Foundry พร้อมโมเดลที่ติดตั้งเพื่อรันโน้ตบุ๊ก

1. ไปที่ [ai.azure.com](https://ai.azure.com) และเข้าสู่ระบบด้วยบัญชี Azure ของคุณ
2. สร้าง **hub** ใหม่ (หรือใช้ของที่มีอยู่แล้ว) ดู: [Hub resources overview](https://learn.microsoft.com/azure/ai-foundry/concepts/ai-resources)
3. ภายใน hub สร้าง **project**
4. ติดตั้งโมเดล (เช่น `gpt-5-mini`) จาก **Models + Endpoints** → **Deploy model**

### ขั้นตอนที่ 2: ดึงปลายทางโปรเจกต์และชื่อการติดตั้งโมเดลของคุณ

จากโปรเจกต์ของคุณในพอร์ทัล Microsoft Foundry:

- **Project Endpoint** — ไปที่หน้ากรุอัปเดตภาพรวม (**Overview**) และคัดลอก URL ปลายทาง

![Project Connection String](../../../translated_images/th/project-endpoint.8cf04c9975bbfbf1.webp)

- **Model Deployment Name** — ไปที่ **Models + Endpoints** เลือกโมเดลที่ติดตั้ง แล้วจดชื่อ **Deployment name** (เช่น `gpt-5-mini`)

### ขั้นตอนที่ 3: เข้าสู่ระบบ Azure ด้วย `az login`

โน้ตบุ๊กส่วนใหญ่จะพิสูจน์ตัวตนผ่าน **การเข้าสู่ระบบ Azure CLI** ของคุณ — โดยใช้ `AzureCliCredential` หรือ `DefaultAzureCredential` (ซึ่งดึงข้อมูลจากเซสชัน `az login` ของคุณ) จากแพ็กเกจ `azure-identity` — ดังนั้นไม่ต้องใช้คีย์ API บางบทเรียนและการรวมระบบเพิ่มเติมตามความสมัครใจจะใช้คีย์ API; โปรดตรวจสอบเงื่อนไขเบื้องต้นของบทเรียนแต่ละบทสำหรับตัวแปรสภาพแวดล้อมเพิ่มเติมซึ่งจำเป็นต้องเข้าสู่ระบบผ่าน Azure CLI

1. **ติดตั้ง Azure CLI** หากยังไม่ได้ติดตั้ง: [aka.ms/installazurecli](https://aka.ms/installazurecli)

2. **เข้าสู่ระบบ** โดยรัน:

    ```bash
    az login
    ```

    หรือถ้าคุณอยู่ในสภาพแวดล้อมระยะไกล/Codespace ที่ไม่มีเบราว์เซอร์:

    ```bash
    az login --use-device-code
    ```

3. **เลือกการสมัครใช้งานของคุณ** หากมีการแจ้งเตือน — เลือกอันที่มีโปรเจกต์ Foundry ของคุณอยู่

4. **ตรวจสอบ** ว่าคุณได้เข้าสู่ระบบแล้ว:

    ```bash
    az account show
    ```

> **ทำไมต้องใช้ `az login`?** โน้ตบุ๊กพิสูจน์ตัวตนผ่าน `AzureCliCredential` (หรือ `DefaultAzureCredential` ซึ่งดึงจากเซสชัน Azure CLI ของคุณ) จากแพ็กเกจ `azure-identity` ซึ่งหมายความว่าเซสชัน Azure CLI ของคุณจะให้ข้อมูลรับรอง — ไม่มีคีย์ API หรือความลับในไฟล์ `.env` ของคุณ นี่เป็น [แนวทางปฏิบัติด้านความปลอดภัยที่ดีที่สุด](https://learn.microsoft.com/azure/developer/ai/keyless-connections)

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

เปิด `.env` และกรอกค่าเหล่านี้:

```env
AZURE_AI_PROJECT_ENDPOINT=https://<your-project>.services.ai.azure.com/api/projects/<your-project-id>
AZURE_AI_MODEL_DEPLOYMENT_NAME=gpt-5-mini
```

| ตัวแปร | ที่หาเจอ |
|----------|-----------------|
| `AZURE_AI_PROJECT_ENDPOINT` | พอร์ทัล Foundry → โปรเจกต์ของคุณ → หน้า **Overview** |
| `AZURE_AI_MODEL_DEPLOYMENT_NAME` | พอร์ทัล Foundry → **Models + Endpoints** → ชื่อโมเดลที่ติดตั้งของคุณ |

นั่นแหละสำหรับบทเรียนส่วนใหญ่! โน้ตบุ๊กจะพิสูจน์ตัวตนอัตโนมัติผ่านเซสชัน `az login` ของคุณ

### ขั้นตอนที่ 5: ติดตั้ง Dependencies ของ Python

```bash
pip install -r requirements.txt
```

เราแนะนำให้รันภายในสภาพแวดล้อมเสมือนที่คุณสร้างไว้ก่อนหน้านี้

## การตั้งค่าเสริม: Azure AI Search (บทเรียนที่ 5 และ 16)

โน้ตบุ๊กบทเรียนที่ 5 (Agentic RAG) และบทเรียนที่ 16 รันได้ทันทีด้วยฐานความรู้ในหน่วยความจำ — ไม่ต้องใช้ทรัพยากร Azure เพิ่มเติม หากคุณต้องการเชื่อมต่อกับดัชนีของ **Azure AI Search** จริง โปรดทราบว่า **โน้ตบุ๊กบทเรียนที่ 16 ใช้การพิสูจน์ตัวตนแบบใช้คีย์**: มันจะสลับจากการค้นหาในหน่วยความจำไปยัง Azure AI Search เฉพาะเมื่อ **ทั้ง** `AZURE_SEARCH_SERVICE_ENDPOINT` **และ** `AZURE_SEARCH_API_KEY` ถูกตั้งค่า และจะอยู่ที่การค้นหาในหน่วยความจำหากไม่ได้ตั้งค่า ดังนั้นถ้าจะรันกับดัชนีจริง คุณต้องตั้งค่าคีย์แอดมินด้วย การพิสูจน์ตัวตนแบบไร้คีย์ด้วย Microsoft Entra ID (RBAC) เป็นวิธีที่แนะนำสำหรับโค้ดการผลิตของคุณเอง สอดคล้องกับการไหลของ `az login` ที่ใช้ในส่วนอื่นๆ ของหลักสูตรนี้

ขั้นตอน RBAC ด้านล่างใช้กับตัวอย่างในคู่มือการตั้งค่าและโค้ดของคุณเอง ไม่ได้เปิดใช้การพิสูจน์ตัวตนแบบไร้คีย์ในโน้ตบุ๊กบทเรียนที่ 16; บทเรียนที่ 16 ยังคงต้องการทั้ง endpoint และคีย์แอดมินสำหรับใช้ Azure AI Search

1. **เปิดใช้งานการเข้าถึงตามบทบาท (RBAC)** บนบริการค้นหาของคุณ:

    ```bash
    az search service update --name <service-name> --resource-group <resource-group> --auth-options aadOrApiKey
    ```

2. **มอบหมายบทบาทที่จำเป็นให้กับตัวคุณเอง** (สร้าง/โหลดดัชนี และคิวรี):

    ```bash
    az role assignment create --assignee <your-user-or-principal-id> --role "Search Service Contributor" --scope $(az search service show -g <resource-group> -n <service-name> --query id -o tsv)
    az role assignment create --assignee <your-user-or-principal-id> --role "Search Index Data Contributor" --scope $(az search service show -g <resource-group> -n <service-name> --query id -o tsv)
    ```

3. **เพิ่ม endpoint** ลงในไฟล์ `.env` ของคุณ:

| ตัวแปร | ที่หาเจอ |
|----------|-----------------|
| `AZURE_SEARCH_SERVICE_ENDPOINT` | พอร์ทัล Azure → ทรัพยากร **Azure AI Search** ของคุณ → **Overview** → URL |
| `AZURE_SEARCH_API_KEY` | จำเป็น (พร้อมกับ endpoint) เพื่อเปิดใช้งาน Azure AI Search ในโน้ตบุ๊กบทเรียนที่ 16 ซึ่งใช้การพิสูจน์ตัวตนด้วยคีย์ พอร์ทัล Azure → **Settings** → **Keys** → คีย์แอดมินหลัก |

> **ทำไมต้องไร้คีย์?** คีย์แอดมินให้สิทธิเขียนเต็มรูปแบบกับบริการค้นหาของคุณและอาจรั่วไหลผ่านไฟล์ `.env` ด้วย RBAC ตัวตน `az login` ของคุณจะถูกใช้แทน — ซึ่งเป็นรูปแบบการพิสูจน์ตัวตนแบบไร้คีย์ของ Entra ID ที่โน้ตบุ๊กของหลักสูตรใช้ (ผ่าน `AzureCliCredential` / `DefaultAzureCredential`) ดูเพิ่มเติม [เชื่อมต่อไปยัง Azure AI Search โดยใช้บทบาท](https://learn.microsoft.com/azure/search/search-security-rbac)

ดูคู่มือการตั้งค่า [Azure AI Search setup guide](./AzureSearch.md) สำหรับตัวอย่างเต็มของการสร้างดัชนีด้วย Python และ .NET

## การตั้งค่าเพิ่มเติมสำหรับบทเรียนที่เรียกใช้ Azure OpenAI โดยตรง (บทเรียนที่ 6 และ 8)

โน้ตบุ๊กบางตัวในบทเรียนที่ 6 และ 8 เรียกใช้ **Azure OpenAI** โดยตรง (โดยใช้ **Responses API**) แทนการผ่านโปรเจกต์ Microsoft Foundry ตัวอย่างเหล่านี้เคยใช้ GitHub Models ซึ่งเลิกใช้แล้วและไม่รองรับ Responses API โปรดเพิ่มตัวแปรเหล่านี้ในไฟล์ `.env` ของคุณ:

| ตัวแปร | ที่หาเจอ |
|----------|-----------------|
| `AZURE_OPENAI_ENDPOINT` | พอร์ทัล Azure → ทรัพยากร **Azure OpenAI** ของคุณ → **Keys and Endpoint** → Endpoint (เช่น `https://<your-resource>.openai.azure.com`) |
| `AZURE_OPENAI_DEPLOYMENT` | ชื่อของโมเดลที่ติดตั้งของคุณ (เช่น `gpt-5-mini`) ซึ่งรองรับ Responses API |
| `AZURE_OPENAI_API_KEY` | ตัวเลือก — เฉพาะถ้าคุณใช้การพิสูจน์ตัวตนด้วยคีย์แทน `az login` / Entra ID |

> Responses API ใช้ endpoint เสถียร `/openai/v1/` ดังนั้นไม่ต้องระบุ `api-version` เข้าสู่ระบบด้วย `az login` เพื่อใช้การพิสูจน์ตัวตนแบบไร้คีย์ Entra ID

## ผู้ให้บริการทางเลือก: MiniMax (รองรับ OpenAI)

[MiniMax](https://platform.minimaxi.com/) ให้บริการโมเดลขนาดใหญ่บริบท (สูงสุด 204K tokens) ผ่าน API ที่เข้ากันได้กับ OpenAI เนื่องจาก Microsoft Agent Framework's `OpenAIChatClient` ทำงานได้กับ endpoint ที่เข้ากันได้กับ OpenAI ใดๆ คุณสามารถใช้ MiniMax เป็นตัวเลือกแทนสำหรับบทเรียนที่ใช้ `OpenAIChatClient`

เพิ่มตัวแปรเหล่านี้ในไฟล์ `.env` ของคุณ:

| ตัวแปร | ที่หาเจอ |
|----------|-----------------|
| `MINIMAX_API_KEY` | [MiniMax Platform](https://platform.minimaxi.com/) → API Keys |
| `MINIMAX_BASE_URL` | ใช้ `https://api.minimax.io/v1` (ค่าเริ่มต้น)|
| `MINIMAX_MODEL_ID` | ชื่อโมเดลที่ใช้ (เช่น `MiniMax-M3`) |

**โมเดลตัวอย่าง**: `MiniMax-M3` (แนะนำ), `MiniMax-M2.7`, `MiniMax-M2.7-highspeed` (ตอบสนองเร็วกว่า) ชื่อและการเข้าถึงโมเดลอาจเปลี่ยนแปลงได้ตามเวลาที่ใช้และขึ้นอยู่กับบัญชีของคุณ

ตัวอย่างโค้ดที่ใช้ `OpenAIChatClient` (เช่น โฟลว์การจองในบทเรียนที่ 14) จะตรวจจับและใช้การตั้งค่า MiniMax ของคุณโดยอัตโนมัติเมื่อมีการตั้งค่า `MINIMAX_API_KEY`


## ผู้ให้บริการทางเลือก: Novita AI (รองรับ OpenAI)

[Novita AI](https://novita.ai/llm-api) ให้บริการ API ที่รองรับ OpenAI สำหรับโมเดลภาษาที่เป็นโอเพ่นซอร์สและก้าวหน้า (DeepSeek, Llama, Qwen และอื่น ๆ) เนื่องจาก `OpenAIChatClient` ของ Microsoft Agent Framework ทำงานร่วมกับจุดสิ้นสุดที่รองรับ OpenAI ใด ๆ ได้ คุณจึงสามารถใช้ Novita AI เป็นทางเลือกแทน Azure OpenAI หรือ OpenAI ได้โดยตรง

เพิ่มตัวแปรเหล่านี้ลงในไฟล์ `.env` ของคุณ:

| ตัวแปร | ที่หามันได้ที่ไหน |
|----------|-----------------|
| `NOVITA_API_KEY` | [แผงควบคุม Novita AI](https://novita.ai/settings/key-management) → API Keys |
| `NOVITA_BASE_URL` | ใช้ `https://api.novita.ai/openai/v1` (ค่าปริยาย) |
| `NOVITA_MODEL_ID` | ชื่อโมเดลที่จะใช้ (เช่น `moonshotai/kimi-k3`) |

**ตัวอย่างโมเดล**: `moonshotai/kimi-k3`, `zai-org/glm-5.2`, `deepseek/deepseek-v4-flash-0731` Novita AI ยังโฮสต์โมเดลโอเพ่นซอร์สแบบครอบครัวอื่น ๆ อีกมากมาย (Llama, Qwen, GLM และอื่น ๆ) — ตรวจสอบ [คลังโมเดล Novita AI](https://novita.ai/llm-api) เพื่อดูรายชื่อโมเดลและรหัสโมเดลที่มีอยู่ในขณะนี้

ตัวอย่างปัจจุบันไม่ใช้ตัวแปร `NOVITA_*` โดยอัตโนมัติ หากต้องการใช้ Novita AI ให้ส่งค่าตัวแปรเหล่านี้เมื่อสร้าง `OpenAIChatClient` ในตัวอย่างที่คุณกำลังรันอย่างชัดเจน

## ผู้ให้บริการทางเลือก: Foundry Local (รันโมเดลบนอุปกรณ์)

[Foundry Local](https://foundrylocal.ai) คือการรันไทม์น้ำหนักเบาที่ดาวน์โหลด จัดการ และให้บริการโมเดลภาษา **ทั้งหมดบนเครื่องของคุณเอง** ผ่าน API ที่รองรับ OpenAI — ไม่ต้องใช้คลาวด์

เนื่องจาก `OpenAIChatClient` ของ Microsoft Agent Framework ทำงานร่วมกับจุดสิ้นสุดที่รองรับ OpenAI ใด ๆ ได้ Foundry Local จึงเป็นทางเลือกในเครื่องที่แทนที่ Azure OpenAI ได้โดยตรง

**1. ติดตั้ง Foundry Local**

```bash
# วินโดวส์
winget install Microsoft.FoundryLocal

# แมคโอเอส
brew install foundrylocal
```

**2. ดาวน์โหลดและรันโมเดล** (ซึ่งจะเริ่มบริการในเครื่องด้วย):

```bash
foundry model list          # ดูรุ่นที่มีอยู่
foundry model run phi-4-mini
```

**3. ติดตั้ง Python SDK** ที่ใช้ในการค้นหาจุดสิ้นสุดในเครื่อง:

```bash
pip install foundry-local-sdk
```

**4. ชี้ Microsoft Agent Framework ถึงโมเดลในเครื่องของคุณ:**

```python
from foundry_local import FoundryLocalManager
from agent_framework.openai import OpenAIChatClient

# ดาวน์โหลด (ถ้าจำเป็น) และให้บริการโมเดลในเครื่อง จากนั้นค้นหาจุดเชื่อมต่อ/พอร์ต
manager = FoundryLocalManager("phi-4-mini")

chat_client = OpenAIChatClient(
    base_url=manager.endpoint,      # เช่น http://localhost:<port>/v1
    api_key=manager.api_key,        # เสมอเป็น "ไม่จำเป็น" สำหรับ Foundry Local
    model_id=manager.get_model_info("phi-4-mini").id,
)

agent = chat_client.as_agent(
    name="LocalAgent",
    instructions="You are a helpful assistant running fully on-device.",
)
```

> **หมายเหตุ:** Foundry Local ให้บริการจุดสิ้นสุด **Chat Completions** ที่รองรับ OpenAI ใช้สำหรับการพัฒนาในเครื่องและกรณีออฟไลน์ สำหรับคุณสมบัติเต็มรูปแบบของ **Responses API** (บทสนทนาที่มีสถานะ ฯลฯ) ให้ใช้ Azure OpenAI หรือโครงการ Microsoft Foundry

## การตั้งค่าเพิ่มเติมสำหรับบทเรียนที่ 8 (กระบวนการทำงานการอิง Bing)

โน้ตบุ๊กกระบวนการทำงานแบบมีเงื่อนไขในบทเรียนที่ 8 ใช้ **การอิง Bing** ผ่าน Microsoft Foundry หากคุณวางแผนจะรันตัวอย่างนี้ ให้เพิ่มตัวแปรนี้ลงในไฟล์ `.env` ของคุณ:

| ตัวแปร | ที่หามันได้ที่ไหน |
|----------|-----------------|
| `BING_CONNECTION_ID` | พอร์ทัล Microsoft Foundry → โครงการของคุณ → **การจัดการ** → **ทรัพยากรที่เชื่อมต่อ** → การเชื่อมต่อ Bing ของคุณ → คัดลอก ID การเชื่อมต่อ |

## การแก้ไขปัญหา

### ข้อผิดพลาดการตรวจสอบใบรับรอง SSL บน macOS

หากคุณใช้ macOS และพบข้อผิดพลาดเช่น:

```plaintext
ssl.SSLCertVerificationError: [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: self-signed certificate in certificate chain
```

นี่เป็นปัญหาที่ทราบใน Python บน macOS ที่ใบรับรอง SSL ของระบบไม่ได้รับความไว้วางใจโดยอัตโนมัติ ลองแก้ไขตามลำดับดังนี้:

**ตัวเลือก 1: รันสคริปต์ Install Certificates ของ Python (แนะนำ)**

```bash
# แทนที่ 3.XX ด้วยเวอร์ชัน Python ที่คุณติดตั้ง (เช่น 3.12 หรือ 3.13):
/Applications/Python\ 3.XX/Install\ Certificates.command
```

**ตัวเลือก 2: ใช้ `connection_verify=False` ในโน้ตบุ๊กของคุณ (สำหรับโน้ตบุ๊ก GitHub Models เท่านั้น)**

ในโน้ตบุ๊กบทเรียนที่ 6 (`06-building-trustworthy-agents/code_samples/06-system-message-framework.ipynb`) มีวิธีแก้ที่ถูกคอมเมนต์ไว้แล้ว ให้ยกเลิกคอมเมนต์ `connection_verify=False` เมื่อเจอข้อผิดพลาดใบรับรอง:

```python
client = ChatCompletionsClient(
    endpoint=endpoint,
    credential=AzureKeyCredential(token),
    connection_verify=False,  # ปิดการตรวจสอบ SSL หากคุณพบข้อผิดพลาดของใบรับรอง
)
```

> **⚠️ คำเตือน:** การปิดใช้งานการตรวจสอบ SSL (`connection_verify=False`) จะลดความปลอดภัยโดยข้ามการตรวจสอบใบรับรอง ใช้เฉพาะเป็นวิธีแก้ชั่วคราวในสภาพแวดล้อมการพัฒนาเท่านั้น ห้ามใช้ในงานผลิต

**ตัวเลือก 3: ติดตั้งและใช้ `truststore`**

```bash
pip install truststore
```

จากนั้นเพิ่มบรรทัดต่อไปนี้ที่ด้านบนของโน้ตบุ๊กหรือสคริปต์ของคุณก่อนทำการเรียกเครือข่ายใด ๆ:

```python
import truststore
truststore.inject_into_ssl()
```

## ติดขัดที่ไหนไหม?

หากคุณมีปัญหาใด ๆ ในการรันการตั้งค่านี้ เข้าร่วมใน <a href="https://discord.gg/kzRShWzttr" target="_blank">Discord ชุมชน Azure AI</a> ของเราหรือ <a href="https://github.com/microsoft/ai-agents-for-beginners/issues?WT.mc_id=academic-105485-koreyst" target="_blank">สร้างข้อผิดพลาด</a>

## บทเรียนถัดไป

ตอนนี้คุณพร้อมที่จะรันโค้ดบทเรียนนี้แล้ว เรียนรู้อย่างสนุกกับโลกของ AI Agents! 

[บทนำสู่ AI Agents และกรณีการใช้งาน Agent](../01-intro-to-ai-agents/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ปฏิเสธความรับผิดชอบ**:
เอกสารนี้ได้รับการแปลโดยใช้บริการแปลภาษา AI [Co-op Translator](https://github.com/Azure/co-op-translator) ขณะที่เราพยายามให้ความถูกต้อง โปรดทราบว่าการแปลโดยอัตโนมัติอาจมีข้อผิดพลาดหรือความไม่ถูกต้อง เอกสารต้นฉบับในภาษาต้นทางควรถูกพิจารณาเป็นแหล่งข้อมูลที่เชื่อถือได้ สำหรับข้อมูลที่สำคัญ แนะนำให้ใช้การแปลโดยมนุษย์มืออาชีพ เราไม่รับผิดชอบต่อความเข้าใจผิดหรือการตีความที่ผิดพลาดที่เกิดขึ้นจากการใช้การแปลนี้
<!-- CO-OP TRANSLATOR DISCLAIMER END -->