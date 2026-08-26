# การตั้งค่าหลักสูตร

## บทนำ

บทเรียนนี้จะครอบคลุมวิธีการรันตัวอย่างโค้ดในหลักสูตรนี้

## เข้าร่วมกับผู้เรียนคนอื่นและขอรับความช่วยเหลือ

ก่อนที่คุณจะเริ่มโคลนรีโพสของคุณ โปรดเข้าร่วม [ช่อง AI Agents For Beginners Discord](https://aka.ms/ai-agents/discord) เพื่อขอความช่วยเหลือเกี่ยวกับการตั้งค่า คำถามเกี่ยวกับหลักสูตร หรือเชื่อมต่อกับผู้เรียนคนอื่น ๆ

## โคลนหรือฟอร์กรีโพสนี้

เพื่อเริ่มต้น โปรดโคลนหรือฟอร์ก GitHub Repository นี้ ซึ่งจะสร้างเวอร์ชันของวัสดุหลักสูตรของคุณเองเพื่อให้คุณสามารถรัน ทดสอบ และปรับแต่งโค้ดได้!

คุณสามารถทำได้โดยคลิกที่ลิงก์เพื่อ <a href="https://github.com/microsoft/ai-agents-for-beginners/fork" target="_blank">ฟอร์กรีโพส</a>

ขณะนี้คุณควรมีรีโพสฟอร์กของหลักสูตรนี้ในลิงก์ต่อไปนี้:

![Forked Repo](../../../translated_images/th/forked-repo.33f27ca1901baa6a.webp)

### โคลนแบบตื้น (แนะนำสำหรับ workshop / Codespaces)

  > รีโพสเต็มอาจมีขนาดใหญ่มาก (~3 GB) เมื่อคุณดาวน์โหลดประวัติเต็มและไฟล์ทั้งหมด หากคุณเข้าร่วมแค่เวิร์กชอป หรือต้องการแค่โฟลเดอร์บทเรียนไม่กี่โฟลเดอร์ โคลนแบบตื้น (หรือโคลนแบบกระจาย) จะดาวน์โหลดข้อมูลน้อยกว่ามาก

#### โคลนแบบตื้นอย่างรวดเร็ว — ประวัติเล็กน้อย ไฟล์ทั้งหมด

เปลี่ยน `<your-username>` ในคำสั่งด้านล่างเป็น URL ฟอร์กของคุณ (หรือ URL แม่ข่ายถ้าคุณต้องการ)

เพื่อโคลนเฉพาะประวัติการคอมมิตล่าสุด (ดาวน์โหลดเล็ก):

```bash
git clone --depth 1 https://github.com/<your-username>/ai-agents-for-beginners.git
```

เพื่อโคลนสาขาที่ระบุ:

```bash
git clone --depth 1 --branch <branch-name> https://github.com/<your-username>/ai-agents-for-beginners.git
```

#### โคลนแบบบางส่วน (sparse) — บลอบเล็กน้อย + โฟลเดอร์เลือกเท่านั้น

ใช้โคลนแบบบางส่วนและ sparse-checkout (ต้องใช้ Git 2.25+ และแนะนำให้ใช้ Git รุ่นใหม่ที่รองรับ partial clone):

```bash
git clone --depth 1 --filter=blob:none --sparse https://github.com/<your-username>/ai-agents-for-beginners.git
```

เข้าไปยังโฟลเดอร์รีโพส:

```bash
cd ai-agents-for-beginners
```

จากนั้นระบุว่าโฟลเดอร์ไหนที่ต้องการ (ตัวอย่างด้านล่างแสดงสองโฟลเดอร์):

```bash
git sparse-checkout set 00-course-setup 01-intro-to-ai-agents
```

หลังจากโคลนและยืนยันไฟล์แล้ว หากคุณต้องการแค่ไฟล์และต้องการคืนพื้นที่ (ไม่ต้องการประวัติ git) โปรดลบเมทาดาทารีโพส (💀ไม่สามารถย้อนกลับ — คุณจะสูญเสียความสามารถทั้งหมดของ Git):

```bash
# zsh/bash
rm -rf .git
```

```powershell
# PowerShell
Remove-Item -Recurse -Force .git
```

#### การใช้ GitHub Codespaces (แนะนำเพื่อลดการดาวน์โหลดขนาดใหญ่บนเครื่อง)

- สร้าง Codespace ใหม่สำหรับรีโพสนี้ผ่าน [GitHub UI](https://github.com/codespaces)  

- ในเทอร์มินัลของ Codespace ที่สร้างใหม่ ให้รันคำสั่ง shallow/sparse clone ข้างต้นเพื่อดึงเฉพาะโฟลเดอร์บทเรียนที่คุณต้องการลงในพื้นที่งาน Codespace
- ตัวเลือก: หลังจากโคลนภายใน Codespaces ให้ลบ .git เพื่อคืนพื้นที่เพิ่ม (ดูคำสั่งลบด้านบน)
- หมายเหตุ: หากคุณต้องการเปิดรีโพสโดยตรงใน Codespaces (โดยไม่ต้องโคลนเพิ่ม) โปรดทราบว่า Codespaces จะสร้างสภาพแวดล้อม devcontainer และอาจยังตั้งค่าสิ่งที่มากกว่าที่คุณต้องการอยู่ดี

#### เคล็ดลับ

- แทนที่ URL โคลนด้วยฟอร์กของคุณเสมอถ้าคุณต้องการแก้ไข/คอมมิต
- ถ้าคุณต้องการประวัติหรือไฟล์เพิ่มในภายหลัง คุณสามารถ fetch หรือปรับ sparse-checkout ให้รวมโฟลเดอร์เพิ่มได้

## การรันโค้ด

หลักสูตรนี้มีชุด Jupyter Notebooks ที่คุณสามารถรันเพื่อเรียนรู้การสร้าง AI Agents ด้วยตนเอง

ตัวอย่างโค้ดใช้ **Microsoft Agent Framework (MAF)** กับ `FoundryChatClient` ซึ่งเชื่อมต่อกับ **Microsoft Foundry Agent Service V2** (Responses API) ผ่าน **Microsoft Foundry**

โน้ตบุ๊ก Python ทุกไฟล์จะถูกติดป้าย `*-python-agent-framework.ipynb`

## ความต้องการ

- Python 3.12+
  - **หมายเหตุ**: หากคุณยังไม่ได้ติดตั้ง Python3.12 ให้ติดตั้งก่อน จากนั้นสร้าง virtual environment ด้วย python3.12 เพื่อให้แน่ใจว่าเวอร์ชันถูกต้องตามไฟล์ requirements.txt
  
    >ตัวอย่าง

    สร้างไดเรกทอรี Python venv:

    ```bash
    python -m venv venv
    ```

    จากนั้นเปิดใช้สภาพแวดล้อม venv สำหรับ:

    ```bash
    # zsh/bash
    source venv/bin/activate
    ```
  
    ```dos
    # Command Prompt for Windows
    venv\Scripts\activate
    ```

- .NET 10+: สำหรับตัวอย่างโค้ดที่ใช้ .NET ให้ติดตั้ง [.NET 10 SDK](https://dotnet.microsoft.com/download/dotnet/10.0) หรือรุ่นที่ใหม่กว่า จากนั้นตรวจสอบเวอร์ชัน .NET SDK ที่ติดตั้ง:

    ```bash
    dotnet --list-sdks
    ```

- **Azure CLI** — จำเป็นสำหรับการตรวจสอบตัวตน ติดตั้งจาก [aka.ms/installazurecli](https://aka.ms/installazurecli)
- **Azure Subscription** — สำหรับการเข้าถึง Microsoft Foundry และ Microsoft Foundry Agent Service
- **โปรเจกต์ Microsoft Foundry** — โปรเจกต์ที่มีโมเดลที่ปรับใช้แล้ว (เช่น `gpt-5-mini`) ดู [ขั้นตอนที่ 1](#ขั้นตอนที่-1-สร้างโปรเจกต์-microsoft-foundry) ด้านล่าง

เราได้รวมไฟล์ `requirements.txt` ไว้ที่โฟลเดอร์รากของรีโพสนี้ ซึ่งมีแพ็กเกจ Python ที่จำเป็นทั้งหมดสำหรับการรันตัวอย่างโค้ด

คุณสามารถติดตั้งโดยรันคำสั่งต่อไปนี้ในเทอร์มินัลที่โฟลเดอร์รากของรีโพส

```bash
pip install -r requirements.txt
```

เราแนะนำให้สร้าง Python virtual environment เพื่อป้องกันความขัดแย้งและปัญหาต่าง ๆ

## ตั้งค่า VSCode

ตรวจสอบให้แน่ใจว่าคุณใช้เวอร์ชัน Python ที่ถูกต้องใน VSCode

![image](https://github.com/user-attachments/assets/a85e776c-2edb-4331-ae5b-6bfdfb98ee0e)

## ตั้งค่า Microsoft Foundry และ Microsoft Foundry Agent Service

### ขั้นตอนที่ 1: สร้างโปรเจกต์ Microsoft Foundry

คุณจะต้องมี **hub** และ **โปรเจกต์** ใน Microsoft Foundry พร้อมโมเดลที่ปรับใช้แล้วเพื่อรันโน้ตบุ๊ก

1. ไปที่ [ai.azure.com](https://ai.azure.com) และเข้าสู่ระบบด้วยบัญชี Azure ของคุณ
2. สร้าง **hub** (หรือใช้ที่มีอยู่แล้ว) ดูรายละเอียดได้ที่: [Hub resources overview](https://learn.microsoft.com/azure/ai-foundry/concepts/ai-resources)
3. ภายใน hub ให้สร้าง **โปรเจกต์**
4. ปรับใช้โมเดล (เช่น `gpt-5-mini`) จาก **Models + Endpoints** → **Deploy model**

### ขั้นตอนที่ 2: ดึง Endpoint โปรเจกต์และชื่อการปรับใช้โมเดลของคุณ

จากโปรเจกต์ของคุณในพอร์ทัล Microsoft Foundry:

- **Project Endpoint** — ไปที่หน้า **Overview** และคัดลอก URL endpoint

![Project Connection String](../../../translated_images/th/project-endpoint.8cf04c9975bbfbf1.webp)

- **Model Deployment Name** — ไปที่ **Models + Endpoints** เลือกโมเดลที่ปรับใช้ และจดชื่อ **Deployment name** (เช่น `gpt-5-mini`)

### ขั้นตอนที่ 3: ลงชื่อเข้าใช้ Azure ด้วยคำสั่ง `az login`

โน้ตบุ๊กส่วนใหญ่ตรวจสอบตัวตนผ่าน **การลงชื่อเข้าใช้ Azure CLI** — ใช้ `AzureCliCredential` หรือ `DefaultAzureCredential` (ซึ่งจะรับ session `az login` ของคุณ) จากแพ็กเกจ `azure-identity` — ดังนั้นจึงไม่ต้องใช้ API keys บางบทเรียนและการผสานรวมเสริมเลือกใช้ API keys; ตรวจสอบข้อกำหนดในแต่ละบทเรียนสำหรับตัวแปรสภาพแวดล้อมเพิ่มเติม ต้องลงชื่อเข้าใช้ผ่าน Azure CLI

1. **ติดตั้ง Azure CLI** หากยังไม่ได้ติดตั้ง: [aka.ms/installazurecli](https://aka.ms/installazurecli)

2. **ลงชื่อเข้าใช้** โดยการรัน:

    ```bash
    az login
    ```

    หรือถ้าคุณอยู่ในสภาพแวดล้อมระยะไกล/Codespace ที่ไม่มีเบราว์เซอร์:

    ```bash
    az login --use-device-code
    ```

3. **เลือกการสมัครสมาชิก** หากถูกถาม — เลือกอันที่มีโปรเจกต์ Foundry ของคุณ

4. **ตรวจสอบ** ว่าคุณได้เข้าสู่ระบบหรือยัง:

    ```bash
    az account show
    ```

> **ทำไมต้อง `az login`?** โน้ตบุ๊กใช้การตรวจสอบตัวตนผ่าน `AzureCliCredential` (หรือ `DefaultAzureCredential`) จากแพ็กเกจ `azure-identity` ซึ่งหมายความว่า session Azure CLI ของคุณคือตัวตน — ไม่ต้องใช้ API keys หรือความลับในไฟล์ `.env` นี่คือ [แนวปฏิบัติด้านความปลอดภัยที่ดีที่สุด](https://learn.microsoft.com/azure/developer/ai/keyless-connections)

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

เปิด `.env` และกรอกค่าดังนี้:

```env
AZURE_AI_PROJECT_ENDPOINT=https://<your-project>.services.ai.azure.com/api/projects/<your-project-id>
AZURE_AI_MODEL_DEPLOYMENT_NAME=gpt-5-mini
```

| ตัวแปร | ที่จะหาได้จาก |
|----------|-----------------|
| `AZURE_AI_PROJECT_ENDPOINT` | พอร์ทัล Foundry → โปรเจกต์ของคุณ → หน้า **Overview** |
| `AZURE_AI_MODEL_DEPLOYMENT_NAME` | พอร์ทัล Foundry → **Models + Endpoints** → ชื่อโมเดลที่ปรับใช้ของคุณ |

นั่นคือสำหรับบทเรียนส่วนใหญ่! โน้ตบุ๊กจะตรวจสอบตัวตนอัตโนมัติผ่าน session `az login` ของคุณ

### ขั้นตอนที่ 5: ติดตั้ง Dependencies ของ Python

```bash
pip install -r requirements.txt
```

เราแนะนำให้รันคำสั่งนี้ภายใน virtual environment ที่คุณสร้างไว้ก่อนหน้านี้

## การตั้งค่าเสริม: Azure AI Search (บทเรียน 5 และ 16)

โน้ตบุ๊กบทเรียน 5 (Agentic RAG) และบทเรียน 16 ทำงานได้ทันทีด้วย **ฐานความรู้ในหน่วยความจำ** — ไม่ต้องมีทรัพยากร Azure เพิ่ม หากคุณต้องการสนับสนุนด้วยดัชนี **Azure AI Search** จริง โปรดทราบว่า **โน้ตบุ๊กบทเรียน 16 ใช้วิธีตรวจสอบตัวตนด้วยคีย์**: จะสลับจากการค้นหาในหน่วยความจำเป็น Azure AI Search ก็ต่อเมื่อตั้งค่า `AZURE_SEARCH_SERVICE_ENDPOINT` **และ** `AZURE_SEARCH_API_KEY` ทั้งสองอย่าง มิฉะนั้นจะค้นหาในหน่วยความจำ — ดังนั้นเพื่อรันกับดัชนีจริงต้องตั้งค่าคีย์แอดมินด้วย วิธีตรวจสอบตัวตนแบบไม่มีคีย์ด้วย Microsoft Entra ID (RBAC) เป็นวิธีแนะนำสำหรับโค้ดโปรดักชันของคุณเอง สอดคล้องกับกระบวนการ `az login` ที่ใช้ในหลักสูตรนี้

ขั้นตอน RBAC ด้านล่างใช้สำหรับตัวอย่างคู่มือการตั้งค่าและโค้ดของคุณเอง ไม่ได้เปิดใช้งานการตรวจสอบตัวตนแบบไม่มีคีย์ในโน้ตบุ๊กบทเรียน 16; บทเรียน 16 ยังคงต้องใช้ endpoint และคีย์แอดมินในการใช้ Azure AI Search

1. **เปิดใช้งานการเข้าถึงแบบ role-based** บนบริการค้นหาของคุณ:

    ```bash
    az search service update --name <service-name> --resource-group <resource-group> --auth-options aadOrApiKey
    ```

2. **กำหนดบทบาทที่จำเป็นให้กับตัวคุณเอง** (สร้าง/โหลดดัชนีและสืบค้น):

    ```bash
    az role assignment create --assignee <your-user-or-principal-id> --role "Search Service Contributor" --scope $(az search service show -g <resource-group> -n <service-name> --query id -o tsv)
    az role assignment create --assignee <your-user-or-principal-id> --role "Search Index Data Contributor" --scope $(az search service show -g <resource-group> -n <service-name> --query id -o tsv)
    ```

3. **เพิ่ม endpoint** ลงในไฟล์ `.env` ของคุณ:

| ตัวแปร | ที่จะหาได้จาก |
|----------|-----------------|
| `AZURE_SEARCH_SERVICE_ENDPOINT` | พอร์ทัล Azure → ทรัพยากร **Azure AI Search** ของคุณ → **ภาพรวม** → URL |
| `AZURE_SEARCH_API_KEY` | จำเป็น (พร้อม endpoint) เพื่อเปิดใช้ Azure AI Search ในโน้ตบุ๊กบทเรียน 16 ซึ่งใช้การตรวจสอบตัวตนด้วยคีย์ พอร์ทัล Azure → **การตั้งค่า** → **คีย์** → คีย์แอดมินหลัก |

> **ทำไมต้องไม่มีคีย์?** คีย์แอดมินให้สิทธิ์เขียนเต็มที่กับบริการค้นหาของคุณและสามารถรั่วไหลจากไฟล์ `.env` ด้วย RBAC ตัวตนของคุณที่ลงชื่อเข้าใช้ `az login` จะถูกใช้แทน — รูปแบบ Entra ID แบบไม่มีคีย์เดียวกับที่โน้ตบุ๊กในหลักสูตรนี้ใช้ (ผ่าน `AzureCliCredential` / `DefaultAzureCredential`) ดูรายละเอียด [การเชื่อมต่อกับ Azure AI Search ด้วยบทบาท](https://learn.microsoft.com/azure/search/search-security-rbac)

ดูคู่มือการตั้งค่า [Azure AI Search](./AzureSearch.md) สำหรับตัวอย่างการสร้างดัชนีเต็มรูปแบบใน Python และ .NET

## การตั้งค่าเพิ่มเติมสำหรับบทเรียนที่เรียก Azure OpenAI โดยตรง (บทเรียน 6 และ 8)

โน้ตบุ๊กบางไฟล์ในบทเรียน 6 และ 8 เรียกใช้ **Azure OpenAI** โดยตรง (ใช้ **Responses API**) แทนการผ่านโปรเจกต์ Microsoft Foundry ตัวอย่างเหล่านี้เคยใช้ GitHub Models ซึ่งเลิกใช้แล้วและไม่รองรับ Responses API ให้เพิ่มตัวแปรเหล่านี้ลงในไฟล์ `.env` ของคุณ:

| ตัวแปร | ที่จะหาได้จาก |
|----------|-----------------|
| `AZURE_OPENAI_ENDPOINT` | พอร์ทัล Azure → ทรัพยากร **Azure OpenAI** ของคุณ → **Keys and Endpoint** → Endpoint (เช่น `https://<your-resource>.openai.azure.com`) |
| `AZURE_OPENAI_DEPLOYMENT` | ชื่อโมเดลที่ปรับใช้ของคุณ (เช่น `gpt-5-mini`) ที่รองรับ Responses API |
| `AZURE_OPENAI_API_KEY` | เป็นทางเลือก — เมื่อใช้การตรวจสอบตัวตนด้วยคีย์แทน `az login` / Entra ID |

> Responses API ใช้ endpoint ที่มั่นคง `/openai/v1/` ดังนั้นไม่ต้องใช้ `api-version` ลงชื่อเข้าใช้ด้วย `az login` เพื่อใช้การตรวจสอบตัวตนแบบไม่มีคีย์ Entra ID

## ผู้ให้บริการทางเลือก: MiniMax (เข้ากันได้กับ OpenAI)

[MiniMax](https://platform.minimaxi.com/) ให้บริการโมเดลบริบทขนาดใหญ่ (สูงสุด 204K tokens) ผ่าน API ที่เข้ากันได้กับ OpenAI เนื่องจาก Microsoft Agent Framework's `OpenAIChatClient` ทำงานกับ endpoint ที่เข้ากันได้กับ OpenAI ดังนั้นคุณสามารถใช้ MiniMax แทนสำหรับบทเรียนที่ใช้ `OpenAIChatClient`

เพิ่มตัวแปรเหล่านี้ในไฟล์ `.env` ของคุณ:

| ตัวแปร | ที่จะหาได้จาก |
|----------|-----------------|
| `MINIMAX_API_KEY` | [MiniMax Platform](https://platform.minimaxi.com/) → API Keys |
| `MINIMAX_BASE_URL` | ใช้ `https://api.minimax.io/v1` (ค่าพื้นฐาน) |
| `MINIMAX_MODEL_ID` | ชื่อโมเดลที่ใช้ (เช่น `MiniMax-M3`) |

**ตัวอย่างโมเดล**: `MiniMax-M3` (แนะนำ), `MiniMax-M2.7`, `MiniMax-M2.7-highspeed` (ตอบสนองเร็วขึ้น) ชื่อและความพร้อมใช้งานของโมเดลอาจเปลี่ยนแปลงตามเวลาและการเข้าถึงโมเดลขึ้นกับบัญชีของคุณ

ตัวอย่างโค้ดที่ใช้ `OpenAIChatClient` (เช่น ขั้นตอนการจองโรงแรมในบทเรียน 14) จะตรวจจับและใช้การตั้งค่า MiniMax ของคุณโดยอัตโนมัติเมื่อตั้งค่า `MINIMAX_API_KEY`


## ผู้ให้บริการทางเลือก: Foundry Local (รันโมเดลบนเครื่อง)

[Foundry Local](https://foundrylocal.ai) คือ runtime ขนาดเบาที่ดาวน์โหลด จัดการ และให้บริการโมเดลภาษา **ทั้งหมดบนเครื่องของคุณเอง** ผ่าน API ที่เข้ากันได้กับ OpenAI — ไม่ต้องใช้คลาวด์

เนื่องจาก Microsoft Agent Framework `OpenAIChatClient` ทำงานกับจุดเชื่อมต่อที่เข้ากันได้กับ OpenAI ใดๆ Foundry Local จึงเป็นทางเลือกแบบติดตั้งในเครื่องแทน Azure OpenAI ได้ทันที

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

**3. ติดตั้ง Python SDK** ที่ใช้ค้นหาจุดเชื่อมต่อในเครื่อง:

```bash
pip install foundry-local-sdk
```

**4. ชี้ Microsoft Agent Framework ให้ใช้โมเดลในเครื่องของคุณ:**

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

> **หมายเหตุ:** Foundry Local เปิดเผยจุดเชื่อมต่อ **Chat Completions** ที่เข้ากันได้กับ OpenAI ใช้สำหรับการพัฒนาท้องถิ่นและสถานการณ์ออฟไลน์ สำหรับชุดคุณสมบัติเต็มรูปแบบของ **Responses API** (การสนทนาแบบมีสถานะ ฯลฯ) ให้ใช้ Azure OpenAI หรือโครงการ Microsoft Foundry

## การตั้งค่าเพิ่มเติมสำหรับบทที่ 8 (กระบวนการทำงาน Bing Grounding)

โน้ตบุ๊กกระบวนการทำงานเงื่อนไขในบทที่ 8 ใช้ **Bing grounding** ผ่าน Microsoft Foundry หากคุณวางแผนจะรันตัวอย่างนั้น ให้เพิ่มตัวแปรนี้ในไฟล์ `.env` ของคุณ:

| ตัวแปร | หาได้จากที่ไหน |
|----------|-----------------|
| `BING_CONNECTION_ID` | พอร์ทัล Microsoft Foundry → โครงการของคุณ → **การจัดการ** → **ทรัพยากรที่เชื่อมต่อ** → การเชื่อมต่อ Bing ของคุณ → คัดลอก ID การเชื่อมต่อ |

## การแก้ไขปัญหา

### ข้อผิดพลาดการตรวจสอบใบรับรอง SSL บน macOS

หากคุณใช้ macOS และเจอข้อผิดพลาดเช่น:

```plaintext
ssl.SSLCertVerificationError: [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: self-signed certificate in certificate chain
```

นี่คือปัญหาที่รู้กันกับ Python บน macOS ซึ่งใบรับรอง SSL ของระบบจะไม่ได้รับการไว้วางใจอัตโนมัติ ลองแก้ไขตามนี้ตามลำดับ:

**ทางเลือกที่ 1: รันสคริปต์ติดตั้งใบรับรองของ Python (แนะนำ)**

```bash
# แทนที่ 3.XX ด้วยเวอร์ชัน Python ที่คุณติดตั้ง (เช่น 3.12 หรือ 3.13):
/Applications/Python\ 3.XX/Install\ Certificates.command
```

**ทางเลือกที่ 2: ใช้ `connection_verify=False` ในโน้ตบุ๊กของคุณ (สำหรับโน้ตบุ๊ก GitHub Models เท่านั้น)**

ในโน้ตบุ๊กบทที่ 6 (`06-building-trustworthy-agents/code_samples/06-system-message-framework.ipynb`) มีการแก้ปัญหาที่คอมเมนต์ไว้แล้ว ให้นำคอมเมนต์ `connection_verify=False` ออกเมื่อเจอข้อผิดพลาดใบรับรอง:

```python
client = ChatCompletionsClient(
    endpoint=endpoint,
    credential=AzureKeyCredential(token),
    connection_verify=False,  # ปิดการตรวจสอบ SSL หากคุณพบข้อผิดพลาดของใบรับรอง
)
```

> **⚠️ คำเตือน:** การปิดการตรวจสอบ SSL (`connection_verify=False`) จะลดความปลอดภัยโดยข้ามการยืนยันใบรับรอง ใช้เฉพาะเป็นทางแก้ชั่วคราวในสภาพแวดล้อมการพัฒนา อย่าใช้ในระบบจริงเด็ดขาด

**ทางเลือกที่ 3: ติดตั้งและใช้ `truststore`**

```bash
pip install truststore
```

จากนั้นเพิ่มบรรทัดดังต่อไปนี้ไว้บนสุดของโน้ตบุ๊กหรือสคริปต์ก่อนเรียกใช้งานเครือข่ายใดๆ:

```python
import truststore
truststore.inject_into_ssl()
```

## ติดปัญหาที่ไหน?

หากคุณมีปัญหาในการตั้งค่านี้ เข้าร่วมที่ <a href="https://discord.gg/kzRShWzttr" target="_blank">Azure AI Community Discord</a> หรือ <a href="https://github.com/microsoft/ai-agents-for-beginners/issues?WT.mc_id=academic-105485-koreyst" target="_blank">สร้าง issue</a> ได้เลย

## บทถัดไป

คุณพร้อมแล้วที่จะรันโค้ดสำหรับคอร์สนี้ ขอให้สนุกกับการเรียนรู้เพิ่มเติมเกี่ยวกับโลกของ AI Agents!

[Introduction to AI Agents and Agent Use Cases](../01-intro-to-ai-agents/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ปฏิเสธความรับผิดชอบ**:
เอกสารนี้ได้รับการแปลโดยใช้บริการแปลภาษา AI [Co-op Translator](https://github.com/Azure/co-op-translator) ขณะที่เราพยายามให้ความถูกต้อง โปรดทราบว่าการแปลโดยอัตโนมัติอาจมีข้อผิดพลาดหรือความไม่ถูกต้อง เอกสารต้นฉบับในภาษาต้นทางควรถูกพิจารณาเป็นแหล่งข้อมูลที่เชื่อถือได้ สำหรับข้อมูลที่สำคัญ แนะนำให้ใช้การแปลโดยมนุษย์มืออาชีพ เราไม่รับผิดชอบต่อความเข้าใจผิดหรือการตีความที่ผิดพลาดที่เกิดขึ้นจากการใช้การแปลนี้
<!-- CO-OP TRANSLATOR DISCLAIMER END -->