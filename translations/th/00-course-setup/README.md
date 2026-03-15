# การตั้งค่าหลักสูตร

## บทนำ

บทเรียนนี้จะครอบคลุมวิธีการรันตัวอย่างโค้ดของหลักสูตรนี้

## เข้าร่วมกับผู้เรียนอื่นและขอความช่วยเหลือ

ก่อนที่คุณจะเริ่มโคลนรีโปของคุณ เข้าร่วมที่ [ช่อง Discord AI Agents For Beginners](https://aka.ms/ai-agents/discord) เพื่อขอความช่วยเหลือในการตั้งค่า คำถามเกี่ยวกับหลักสูตร หรือเชื่อมต่อกับผู้เรียนคนอื่น ๆ

## โคลนหรือโฟร์กรูปรีโปนี้

เพื่อเริ่มต้น กรุณาโคลนหรือโฟร์กรูป GitHub Repository นี้ ซึ่งจะช่วยให้คุณมีเวอร์ชันของวัสดุหลักสูตรที่คุณสามารถรัน ทดสอบ และปรับแต่งโค้ดได้เอง!

คุณสามารถทำได้โดยคลิกที่ลิงก์ <a href="https://github.com/microsoft/ai-agents-for-beginners/fork" target="_blank">โฟร์กรูปรีโป</a>

ตอนนี้คุณควรมีเวอร์ชันโฟร์กของหลักสูตรนี้ในลิงก์ดังต่อไปนี้:

![Forked Repo](../../../translated_images/th/forked-repo.33f27ca1901baa6a.webp)

### โคลนแบบตื้น (แนะนำสำหรับเวิร์คช็อป / Codespaces)

  > รีโปเต็มสามารถมีขนาดใหญ่ (~3 GB) เมื่อคุณดาวน์โหลดประวัติทั้งหมดและไฟล์ทั้งหมด หากคุณเข้าร่วมแค่เวิร์คช็อปหรือแค่ต้องการโฟลเดอร์บทเรียนบางส่วน โคลนแบบตื้น (หรือโคลนแบบบางส่วน) จะช่วยหลีกเลี่ยงการดาวน์โหลดส่วนใหญ่นั้นโดยลดขนาดประวัติและ/หรือข้ามบล็อบบางส่วน

#### โคลนแบบตื้นอย่างรวดเร็ว — ประวัติน้อยที่สุด ไฟล์ทั้งหมด

แทนที่ `<your-username>` ในคำสั่งด้านล่างด้วย URL ของโฟร์กของคุณ (หรือ URL แหล่งต้นทางหากคุณต้องการ)

เพื่อโคลนประวัติการคอมมิตล่าสุดเท่านั้น (ดาวน์โหลดขนาดเล็ก):

```bash|powershell
git clone --depth 1 https://github.com/<your-username>/ai-agents-for-beginners.git
```

เพื่อโคลนเฉพาะสาขาที่ระบุ:

```bash|powershell
git clone --depth 1 --branch <branch-name> https://github.com/<your-username>/ai-agents-for-beginners.git
```

#### โคลนแบบบางส่วน (sparse) — บล็อบน้อยที่สุด + โฟลเดอร์ที่เลือกเท่านั้น

ใช้การโคลนแบบบางส่วนและ sparse-checkout (ต้องใช้ Git 2.25+ และแนะนำให้ใช้ Git รุ่นใหม่ที่รองรับการโคลนแบบบางส่วน):

```bash|powershell
git clone --depth 1 --filter=blob:none --sparse https://github.com/<your-username>/ai-agents-for-beginners.git
```

เข้าสู่โฟลเดอร์รีโป:

```bash|powershell
cd ai-agents-for-beginners
```

จากนั้นระบุโฟลเดอร์ที่คุณต้องการ (ตัวอย่างด้านล่างแสดงสองโฟลเดอร์):

```bash|powershell
git sparse-checkout set 00-course-setup 01-intro-to-ai-agents
```

หลังโคลนและยืนยันไฟล์แล้ว หากคุณต้องการเฉพาะไฟล์และต้องการเพิ่มพื้นที่ว่าง (ไม่มีประวัติ git) กรุณาลบเมตาดาต้ารีโป (💀ไม่สามารถย้อนกลับ — คุณจะสูญเสียการใช้งาน Git ทั้งหมด: ไม่มีคอมมิต, ดึง, ส่ง, หรือเข้าถึงประวัติ)

```bash
# zsh/bash
rm -rf .git
```

```powershell
# PowerShell
Remove-Item -Recurse -Force .git
```

#### การใช้ GitHub Codespaces (แนะนำเพื่อหลีกเลี่ยงการดาวน์โหลดขนาดใหญ่ในเครื่อง)

- สร้าง Codespace ใหม่สำหรับรีโปนี้ผ่าน [GitHub UI](https://github.com/codespaces).  

- ในเทอร์มินัลของ Codespace ที่สร้างขึ้นใหม่ ให้รันคำสั่งโคลนแบบตื้น/แบบบางส่วนที่กล่าวข้างต้นเพื่อนำเฉพาะโฟลเดอร์บทเรียนที่คุณต้องการเข้าสู่พื้นที่ทำงานของ Codespace.
- ตัวเลือก: หลังโคลนใน Codespaces ให้ลบ .git เพื่อเรียกคืนพื้นที่เพิ่มเติม (ดูคำสั่งลบด้านบน).
- หมายเหตุ: หากคุณต้องการเปิดรีโปโดยตรงใน Codespaces (โดยไม่โคลนเพิ่ม) โปรดทราบว่า Codespaces จะสร้างสภาพแวดล้อม devcontainer และอาจเตรียมชุดมากกว่าที่คุณต้องการ การโคลนสำเนาแบบตื้นภายใน Codespace ใหม่จะให้คุณควบคุมการใช้พื้นที่ดิสก์ได้มากขึ้น

#### เคล็ดลับ

- แทนที่ URL โคลนด้วยโฟร์กของคุณเสมอหากต้องการแก้ไข/คอมมิต
- หากคุณต้องการประวัติหรือไฟล์เพิ่มภายหลัง คุณสามารถดึงหรือปรับ sparse-checkout เพื่อรวมโฟลเดอร์เพิ่มเติมได้

## การรันโค้ด

หลักสูตรนี้มีชุด Jupyter Notebooks ที่คุณสามารถรันเพื่อประสบการณ์การสร้าง AI Agents ด้วยตัวเอง

ตัวอย่างโค้ดใช้ **Microsoft Agent Framework (MAF)** กับ `AzureAIProjectAgentProvider` ซึ่งเชื่อมต่อกับ **Azure AI Agent Service V2** (API ตอบกลับ) ผ่าน **Microsoft Foundry**

โน้ตบุ๊ค Python ทั้งหมดจะมีป้ายชื่อ `*-python-agent-framework.ipynb`

## ความต้องการ

- Python 3.12+
  - **หมายเหตุ**: หากคุณยังไม่มี Python3.12 ติดตั้ง ให้ติดตั้งก่อน แล้วสร้าง venv ด้วย python3.12 เพื่อให้แน่ใจว่าจะติดตั้งเวอร์ชันที่ถูกต้องจากไฟล์ requirements.txt
  
    >ตัวอย่าง

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

- .NET 10+: สำหรับโค้ดตัวอย่างที่ใช้ .NET ให้ติดตั้ง [.NET 10 SDK](https://dotnet.microsoft.com/download/dotnet/10.0) หรือเวอร์ชันที่ใหม่กว่า แล้วตรวจสอบเวอร์ชัน SDK ที่ติดตั้ง:

    ```bash|powershell
    dotnet --list-sdks
    ```

- **Azure CLI** — จำเป็นสำหรับการยืนยันตัวตน ติดตั้งจาก [aka.ms/installazurecli](https://aka.ms/installazurecli)
- **Azure Subscription** — เพื่อเข้าถึง Microsoft Foundry และ Azure AI Agent Service
- **โครงการ Microsoft Foundry** — โครงการที่มีโมเดลเผยแพร่ (เช่น `gpt-4o`) ดู [ขั้นตอนที่ 1](../../../00-course-setup) ด้านล่าง

เราได้รวมไฟล์ `requirements.txt` ไว้ในโฟลเดอร์รูทของรีโปนี้ ซึ่งมีแพ็คเกจ Python ที่จำเป็นทั้งหมดสำหรับรันตัวอย่างโค้ด

คุณสามารถติดตั้งโดยรันคำสั่งต่อไปนี้ในเทอร์มินัลที่รูทรีโป:

```bash|powershell
pip install -r requirements.txt
```

เราแนะนำให้สร้างสภาพแวดล้อมเสมือน Python เพื่อป้องกันข้อขัดแย้งและปัญหา

## ตั้งค่า VSCode

ตรวจสอบให้แน่ใจว่าคุณใช้เวอร์ชัน Python ที่ถูกต้องใน VSCode

![image](https://github.com/user-attachments/assets/a85e776c-2edb-4331-ae5b-6bfdfb98ee0e)

## การตั้งค่า Microsoft Foundry และ Azure AI Agent Service

### ขั้นตอนที่ 1: สร้างโครงการ Microsoft Foundry

คุณจำเป็นต้องมี Azure AI Foundry **hub** และ **project** พร้อมโมเดลที่เผยแพร่ เพื่อรันโน้ตบุ๊ค

1. ไปที่ [ai.azure.com](https://ai.azure.com) และเข้าสู่ระบบด้วยบัญชี Azure ของคุณ
2. สร้าง **hub** (หรือใช้ที่มีอยู่แล้ว) ดูที่: [ภาพรวมทรัพยากร Hub](https://learn.microsoft.com/azure/ai-foundry/concepts/ai-resources)
3. ใน hub สร้าง **project**
4. เผยแพร่โมเดล (เช่น `gpt-4o`) จาก **Models + Endpoints** → **Deploy model**

### ขั้นตอนที่ 2: ดึง Endpoint โครงการและชื่อการเผยแพร่โมเดล

จากโครงการในพอร์ทัล Microsoft Foundry:

- **Project Endpoint** — ไปที่หน้า **Overview** และคัดลอก URL endpoint

![Project Connection String](../../../translated_images/th/project-endpoint.8cf04c9975bbfbf1.webp)

- **Model Deployment Name** — ไปที่ **Models + Endpoints**, เลือกโมเดลที่เผยแพร่ และบันทึก **Deployment name** (เช่น `gpt-4o`)

### ขั้นตอนที่ 3: ลงชื่อเข้าใช้ Azure ด้วย `az login`

โน้ตบุ๊คทุกตัวใช้ **`AzureCliCredential`** สำหรับการยืนยันตัวตน — ไม่มีการจัดการกับ API keys แต่อย่างใด ซึ่งคุณจำเป็นต้องลงชื่อเข้าใช้ผ่าน Azure CLI

1. **ติดตั้ง Azure CLI** หากคุณยังไม่มี: [aka.ms/installazurecli](https://aka.ms/installazurecli)

2. **ลงชื่อเข้าใช้** โดยรันคำสั่ง:

    ```bash|powershell
    az login
    ```

    หรือถ้าคุณอยู่ในสภาพแวดล้อมระยะไกล / Codespace ที่ไม่มีเบราว์เซอร์:

    ```bash|powershell
    az login --use-device-code
    ```

3. **เลือก subscription** หากถาม — เลือกตัวที่มีโครงการ Foundry ของคุณ

4. **ตรวจสอบ** การเข้าสู่ระบบของคุณ:

    ```bash|powershell
    az account show
    ```

> **ทำไมต้องใช้ `az login`?** โน้ตบุ๊คยืนยันตัวตนด้วย `AzureCliCredential` จากแพ็คเกจ `azure-identity` ซึ่งหมายความว่าเซสชัน Azure CLI ของคุณจะเป็นตัวให้สิทธิ์ — ไม่ต้องใช้ API keys หรือความลับในไฟล์ `.env` นี่คือ [แนวปฏิบัติด้านความปลอดภัยที่ดีที่สุด](https://learn.microsoft.com/azure/developer/ai/keyless-connections)

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

เปิดไฟล์ `.env` และกรอกสองค่าต่อไปนี้:

```env
AZURE_AI_PROJECT_ENDPOINT=https://<your-project>.services.ai.azure.com/api/projects/<your-project-id>
AZURE_AI_MODEL_DEPLOYMENT_NAME=gpt-4o
```

| ตัวแปร | ที่หาค่าได้ |
|----------|-----------------|
| `AZURE_AI_PROJECT_ENDPOINT` | พอร์ทัล Foundry → โครงการของคุณ → หน้า **Overview** |
| `AZURE_AI_MODEL_DEPLOYMENT_NAME` | พอร์ทัล Foundry → **Models + Endpoints** → ชื่อการเผยแพร่โมเดลของคุณ |

เท่านี้สำหรับหลายบทเรียน! โน้ตบุ๊คจะยืนยันตัวตนโดยอัตโนมัติผ่านเซสชัน `az login` ของคุณ

### ขั้นตอนที่ 5: ติดตั้ง Dependencies ของ Python

```bash|powershell
pip install -r requirements.txt
```

เราแนะนำให้รันคำสั่งนี้ภายในสภาพแวดล้อมเสมือนที่คุณสร้างไว้ก่อนหน้านี้

## การตั้งค่าเพิ่มเติมสำหรับบทเรียนที่ 5 (Agentic RAG)

บทเรียน 5 ใช้ **Azure AI Search** สำหรับการสร้างแบบมีการเสริมการค้นคืน หากคุณตั้งใจจะรันบทเรียนนั้น ให้เพิ่มตัวแปรเหล่านี้ในไฟล์ `.env` ของคุณ:

| ตัวแปร | ที่หาค่าได้ |
|----------|-----------------|
| `AZURE_SEARCH_SERVICE_ENDPOINT` | พอร์ทัล Azure → แหล่งทรัพยากร **Azure AI Search** ของคุณ → **Overview** → URL |
| `AZURE_SEARCH_API_KEY` | พอร์ทัล Azure → แหล่งทรัพยากร **Azure AI Search** ของคุณ → **Settings** → **Keys** → คีย์แอดมินหลัก |

## การตั้งค่าเพิ่มเติมสำหรับบทเรียนที่ 6 และ 8 (GitHub Models)

โน้ตบุ๊คบางส่วนในบทเรียนที่ 6 และ 8 ใช้ **GitHub Models** แทน Azure AI Foundry หากคุณตั้งใจจะรันตัวอย่างเหล่านั้น ให้เพิ่มตัวแปรเหล่านี้ในไฟล์ `.env` ของคุณ:

| ตัวแปร | ที่หาค่าได้ |
|----------|-----------------|
| `GITHUB_TOKEN` | GitHub → **Settings** → **Developer settings** → **Personal access tokens** |
| `GITHUB_ENDPOINT` | ใช้ `https://models.inference.ai.azure.com` (ค่าปริยาย) |
| `GITHUB_MODEL_ID` | ชื่อโมเดลที่ใช้ (เช่น `gpt-4o-mini`) |

## การตั้งค่าเพิ่มเติมสำหรับบทเรียนที่ 8 (Bing Grounding Workflow)

โน้ตบุ๊คเวิร์กโฟลว์เงื่อนไขในบทเรียนที่ 8 ใช้ **Bing grounding** ผ่าน Azure AI Foundry หากคุณตั้งใจจะรันตัวอย่างนี้ ให้เพิ่มตัวแปรนี้ในไฟล์ `.env` ของคุณ:

| ตัวแปร | ที่หาค่าได้ |
|----------|-----------------|
| `BING_CONNECTION_ID` | พอร์ทัล Azure AI Foundry → โครงการของคุณ → **Management** → **Connected resources** → การเชื่อมต่อ Bing ของคุณ → คัดลอก ID การเชื่อมต่อ |

## การแก้ไขปัญหา

### ข้อผิดพลาดการตรวจสอบใบรับรอง SSL บน macOS

ถ้าคุณใช้ macOS แล้วพบข้อผิดพลาดแบบนี้:

```plaintext
ssl.SSLCertVerificationError: [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: self-signed certificate in certificate chain
```

นี่คือปัญหาที่ทราบของ Python บน macOS ที่ใบรับรอง SSL ของระบบไม่ถูกไว้วางใจโดยอัตโนมัติ ลองวิธีแก้ไขต่อไปนี้ตามลำดับ:

**ตัวเลือก 1: รันสคริปต์ติดตั้งใบรับรองของ Python (แนะนำ)**

```bash
# แทนที่ 3.XX ด้วยเวอร์ชัน Python ที่คุณติดตั้ง (เช่น 3.12 หรือ 3.13):
/Applications/Python\ 3.XX/Install\ Certificates.command
```

**ตัวเลือก 2: ใช้ `connection_verify=False` ในโน้ตบุ๊คของคุณ (ใช้เฉพาะกับโน้ตบุ๊ค GitHub Models เท่านั้น)**

ในโน้ตบุ๊คบทเรียน 6 (`06-building-trustworthy-agents/code_samples/06-system-message-framework.ipynb`) มีวิธีแก้ไขที่คอมเมนต์ไว้แล้ว เพียงเอาคอมเมนต์ออกที่ `connection_verify=False` เมื่อสร้างไคลเอนต์:

```python
client = ChatCompletionsClient(
    endpoint=endpoint,
    credential=AzureKeyCredential(token),
    connection_verify=False,  # ปิดการตรวจสอบ SSL หากคุณพบข้อผิดพลาดของใบรับรอง
)
```

> **⚠️ คำเตือน:** การปิดใช้งานการตรวจสอบ SSL (`connection_verify=False`) จะลดความปลอดภัยโดยการข้ามการตรวจสอบใบรับรอง ใช้วิธีนี้เฉพาะในสภาพแวดล้อมการพัฒนาชั่วคราวเท่านั้น ห้ามใช้ในระบบโปรดัคชัน

**ตัวเลือก 3: ติดตั้งและใช้ `truststore`**

```bash
pip install truststore
```

จากนั้นเพิ่มบรรทัดนี้ไว้บนสุดของโน้ตบุ๊คหรือสคริปต์ของคุณก่อนเรียกการเชื่อมต่อเครือข่ายใด ๆ:

```python
import truststore
truststore.inject_into_ssl()
```

## ติดขัดที่ไหน?

ถ้าคุณมีปัญหาในการรันการตั้งค่านี้ เข้าร่วมใน <a href="https://discord.gg/kzRShWzttr" target="_blank">Azure AI Community Discord</a> หรือ <a href="https://github.com/microsoft/ai-agents-for-beginners/issues?WT.mc_id=academic-105485-koreyst" target="_blank">สร้างปัญหา</a>

## บทเรียนถัดไป

ตอนนี้คุณพร้อมที่จะรันโค้ดสำหรับหลักสูตรนี้แล้ว ขอให้สนุกกับการเรียนรู้เพิ่มเติมเกี่ยวกับโลกของ AI Agents!

[บทนำสู่ AI Agents และกรณีการใช้งาน Agent](../01-intro-to-ai-agents/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ข้อจำกัดความรับผิดชอบ**:  
เอกสารนี้ได้รับการแปลโดยใช้บริการแปลภาษาอัตโนมัติ [Co-op Translator](https://github.com/Azure/co-op-translator) แม้ว่าเราจะพยายามให้การแปลมีความถูกต้อง โปรดทราบว่าการแปลโดยอัตโนมัติอาจมีข้อผิดพลาดหรือความคลาดเคลื่อน เอกสารต้นฉบับในภาษาดั้งเดิมควรถือเป็นแหล่งข้อมูลที่เชื่อถือได้ สำหรับข้อมูลที่มีความสำคัญ แนะนำให้ใช้บริการแปลโดยมืออาชีพ เราไม่รับผิดชอบต่อความเข้าใจผิดหรือการตีความที่ผิดพลาดที่เกิดจากการใช้การแปลนี้
<!-- CO-OP TRANSLATOR DISCLAIMER END -->