<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "96eb7f95375daa3e91778ca0295a55d9",
  "translation_date": "2025-10-15T11:47:42+00:00",
  "source_file": "00-course-setup/README.md",
  "language_code": "th"
}
-->
# การตั้งค่าคอร์ส

## บทนำ

บทเรียนนี้จะครอบคลุมวิธีการรันตัวอย่างโค้ดของคอร์สนี้

## เข้าร่วมกับผู้เรียนคนอื่นและขอความช่วยเหลือ

ก่อนที่คุณจะเริ่มต้นการโคลน repo ของคุณ เข้าร่วม [ช่อง Discord AI Agents For Beginners](https://aka.ms/ai-agents/discord) เพื่อขอความช่วยเหลือเกี่ยวกับการตั้งค่า ถามคำถามเกี่ยวกับคอร์ส หรือเชื่อมต่อกับผู้เรียนคนอื่น ๆ

## โคลนหรือ Fork Repo นี้

เพื่อเริ่มต้น กรุณาโคลนหรือ fork GitHub Repository นี้ เพื่อสร้างเวอร์ชันของคุณเองสำหรับเนื้อหาคอร์ส เพื่อให้คุณสามารถรัน ทดสอบ และปรับแต่งโค้ดได้!

คุณสามารถทำได้โดยคลิกลิงก์ <a href="https://github.com/microsoft/ai-agents-for-beginners/fork" target="_blank">fork repo</a>

ตอนนี้คุณควรมีเวอร์ชัน fork ของคอร์สนี้ในลิงก์ต่อไปนี้:

![Forked Repo](../../../translated_images/forked-repo.33f27ca1901baa6a5e13ec3eb1f0ddd3a44d936d91cc8cfb19bfdb9688bd2c3d.th.png)

### โคลนแบบตื้น (แนะนำสำหรับ workshop / Codespaces)

  > Repository ทั้งหมดอาจมีขนาดใหญ่ (~3 GB) เมื่อคุณดาวน์โหลดประวัติและไฟล์ทั้งหมด หากคุณเข้าร่วม workshop หรือเพียงต้องการโฟลเดอร์บทเรียนบางส่วน การโคลนแบบตื้น (หรือโคลนแบบบางส่วน) จะช่วยลดการดาวน์โหลดส่วนใหญ่โดยการตัดประวัติและ/หรือข้าม blobs

#### โคลนแบบตื้นอย่างรวดเร็ว — ประวัติขั้นต่ำ ไฟล์ทั้งหมด

แทนที่ `<your-username>` ในคำสั่งด้านล่างด้วย URL fork ของคุณ (หรือ URL upstream หากคุณต้องการ)

เพื่อโคลนเฉพาะประวัติการ commit ล่าสุด (ดาวน์โหลดขนาดเล็ก):

```bash|powershell
git clone --depth 1 https://github.com/<your-username>/ai-agents-for-beginners.git
```

เพื่อโคลน branch เฉพาะ:

```bash|powershell
git clone --depth 1 --branch <branch-name> https://github.com/<your-username>/ai-agents-for-beginners.git
```

#### โคลนแบบบางส่วน — blobs ขั้นต่ำ + เฉพาะโฟลเดอร์ที่เลือก

วิธีนี้ใช้การโคลนแบบบางส่วนและ sparse-checkout (ต้องการ Git 2.25+ และแนะนำให้ใช้ Git รุ่นใหม่ที่รองรับ partial clone):

```bash|powershell
git clone --depth 1 --filter=blob:none --sparse https://github.com/<your-username>/ai-agents-for-beginners.git
```

เข้าสู่โฟลเดอร์ repo:

สำหรับ bash:

```bash
cd ai-agents-for-beginners
```

สำหรับ Powershell:

```powershell
Set-Location ai-agents-for-beginners
```

จากนั้นระบุโฟลเดอร์ที่คุณต้องการ (ตัวอย่างด้านล่างแสดงสองโฟลเดอร์):

```bash|powershell
git sparse-checkout set 00-course-setup 01-intro-to-ai-agents
```

หลังจากโคลนและตรวจสอบไฟล์ หากคุณต้องการเฉพาะไฟล์และต้องการเพิ่มพื้นที่ว่าง (ไม่มีประวัติ git) กรุณาลบ metadata ของ repository (💀ไม่สามารถย้อนกลับได้ — คุณจะสูญเสียฟังก์ชันการทำงานของ Git ทั้งหมด: ไม่มี commits, pulls, pushes หรือการเข้าถึงประวัติ)

สำหรับ Linux/macOS:

```bash
rm -rf .git
```

สำหรับ Windows:

```powershell
Remove-Item -Recurse -Force .git
```

#### การใช้ GitHub Codespaces (แนะนำเพื่อหลีกเลี่ยงการดาวน์โหลดขนาดใหญ่ในเครื่อง)

- สร้าง Codespace ใหม่สำหรับ repo นี้ผ่าน [GitHub UI](https://github.com/codespaces)  

- ใน terminal ของ Codespace ที่สร้างใหม่ ให้รันคำสั่งโคลนแบบตื้น/บางส่วนด้านบนเพื่อนำเฉพาะโฟลเดอร์บทเรียนที่คุณต้องการเข้าสู่ workspace ของ Codespace
- ตัวเลือก: หลังจากโคลนใน Codespaces ให้ลบ .git เพื่อเรียกคืนพื้นที่เพิ่มเติม (ดูคำสั่งการลบด้านบน)
- หมายเหตุ: หากคุณต้องการเปิด repo โดยตรงใน Codespaces (โดยไม่ต้องโคลนเพิ่มเติม) โปรดทราบว่า Codespaces จะสร้างสภาพแวดล้อม devcontainer และอาจยังคงจัดเตรียมมากกว่าที่คุณต้องการ การโคลนสำเนาแบบตื้นใน Codespace ใหม่ช่วยให้คุณควบคุมการใช้งานดิสก์ได้มากขึ้น

#### เคล็ดลับ

- เปลี่ยน URL โคลนเสมอเป็น fork ของคุณหากคุณต้องการแก้ไข/commit
- หากคุณต้องการประวัติหรือไฟล์เพิ่มเติมในภายหลัง คุณสามารถ fetch หรือปรับ sparse-checkout เพื่อรวมโฟลเดอร์เพิ่มเติมได้

## การรันโค้ด

คอร์สนี้มีชุด Jupyter Notebooks ที่คุณสามารถรันเพื่อสัมผัสประสบการณ์การสร้าง AI Agents

ตัวอย่างโค้ดใช้:

**ต้องมีบัญชี GitHub - ฟรี**:

1) Semantic Kernel Agent Framework + GitHub Models Marketplace. ระบุว่า (semantic-kernel.ipynb)
2) AutoGen Framework + GitHub Models Marketplace. ระบุว่า (autogen.ipynb)

**ต้องมีการสมัครสมาชิก Azure**:
3) Azure AI Foundry + Azure AI Agent Service. ระบุว่า (azureaiagent.ipynb)

เราขอแนะนำให้คุณลองใช้ตัวอย่างทั้งสามประเภทเพื่อดูว่าแบบใดที่เหมาะกับคุณที่สุด

ไม่ว่าคุณจะเลือกตัวเลือกใด จะเป็นตัวกำหนดขั้นตอนการตั้งค่าที่คุณต้องปฏิบัติตามด้านล่าง:

## ความต้องการ

- Python 3.12+
  - **NOTE**: หากคุณยังไม่มี Python3.12 ติดตั้งอยู่ ให้แน่ใจว่าคุณติดตั้งมัน จากนั้นสร้าง venv ของคุณโดยใช้ python3.12 เพื่อให้แน่ใจว่าเวอร์ชันที่ถูกต้องถูกติดตั้งจากไฟล์ requirements.txt
  
    >ตัวอย่าง

    สร้างไดเรกทอรี Python venv:

    ``` bash
    python3 -m venv venv
    ```

    จากนั้นเปิดใช้งานสภาพแวดล้อม venv สำหรับ:

    macOS และ Linux

    ```bash
    source venv/bin/activate
    ```
  
    Windows

    ```bash
    venv\Scripts\activate
    ```

- บัญชี GitHub - สำหรับการเข้าถึง GitHub Models Marketplace
- การสมัครสมาชิก Azure - สำหรับการเข้าถึง Azure AI Foundry
- บัญชี Azure AI Foundry - สำหรับการเข้าถึง Azure AI Agent Service

เราได้รวมไฟล์ `requirements.txt` ไว้ใน root ของ repository นี้ ซึ่งมีแพ็กเกจ Python ที่จำเป็นทั้งหมดสำหรับการรันตัวอย่างโค้ด

คุณสามารถติดตั้งได้โดยรันคำสั่งต่อไปนี้ใน terminal ที่ root ของ repository:

```bash
pip install -r requirements.txt
```
เราขอแนะนำให้สร้าง Python virtual environment เพื่อหลีกเลี่ยงปัญหาและความขัดแย้งใด ๆ

## การตั้งค่า VSCode
ตรวจสอบให้แน่ใจว่าคุณใช้เวอร์ชัน Python ที่ถูกต้องใน VSCode

![image](https://github.com/user-attachments/assets/a85e776c-2edb-4331-ae5b-6bfdfb98ee0e)

## การตั้งค่าสำหรับตัวอย่างที่ใช้ GitHub Models 

### ขั้นตอนที่ 1: ดึง GitHub Personal Access Token (PAT) ของคุณ

คอร์สนี้ใช้ GitHub Models Marketplace ซึ่งให้การเข้าถึง Large Language Models (LLMs) ฟรีที่คุณจะใช้ในการสร้าง AI Agents

ในการใช้ GitHub Models คุณจะต้องสร้าง [GitHub Personal Access Token](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens)

คุณสามารถทำได้โดยไปที่ <a href="https://github.com/settings/personal-access-tokens" target="_blank">การตั้งค่า Personal Access Tokens</a> ในบัญชี GitHub ของคุณ

กรุณาปฏิบัติตาม [หลักการของการให้สิทธิ์น้อยที่สุด](https://docs.github.com/en/get-started/learning-to-code/storing-your-secrets-safely) เมื่อสร้าง token ของคุณ ซึ่งหมายความว่าคุณควรให้ token เฉพาะสิทธิ์ที่จำเป็นในการรันตัวอย่างโค้ดในคอร์สนี้

1. เลือกตัวเลือก `Fine-grained tokens` ที่ด้านซ้ายของหน้าจอโดยไปที่ **Developer settings**
   ![](../../../translated_images/profile_developer_settings.410a859fe749c755c859d414294c5908e307222b2c61819c3203bbeed4470e25.th.png)

    จากนั้นเลือก `Generate new token`.

    ![Generate Token](../../../translated_images/fga_new_token.1c1a234afe202ab37483944a291ee80c1868e1e78082fd6bd4180fea5d5a15b4.th.png)

2. ใส่ชื่อที่อธิบายได้สำหรับ token ของคุณที่สะท้อนถึงวัตถุประสงค์ของมัน เพื่อให้ง่ายต่อการระบุในภายหลัง


    🔐 คำแนะนำระยะเวลาของ Token

    ระยะเวลาที่แนะนำ: 30 วัน
    เพื่อความปลอดภัยที่มากขึ้น คุณสามารถเลือกช่วงเวลาที่สั้นลง เช่น 7 วัน 🛡️
    เป็นวิธีที่ดีในการตั้งเป้าหมายส่วนตัวและทำคอร์สให้เสร็จในขณะที่คุณมีแรงจูงใจในการเรียนรู้ 🚀.

    ![Token Name and Expiration](../../../translated_images/token-name-expiry-date.a095fb0de63868640a4c82d6b1bbc92b482930a663917a5983a3c7cd1ef86b77.th.png)

3. จำกัดขอบเขตของ token ให้กับ fork ของ repository นี้

    ![Limit scope to fork repository](../../../translated_images/token_repository_limit.924ade5e11d9d8bb6cd21293987e4579dea860e2ba66d607fb46e49524d53644.th.png)

4. จำกัดสิทธิ์ของ token: ภายใต้ **Permissions** คลิกแท็บ **Account** และคลิกปุ่ม "+ Add permissions" จะมี dropdown ปรากฏขึ้น กรุณาค้นหา **Models** และทำเครื่องหมายที่ช่องสำหรับมัน
    ![Add Models Permission](../../../translated_images/add_models_permissions.c0c44ed8b40fc143dc87792da9097d715b7de938354e8f771d65416ecc7816b8.th.png)

5. ตรวจสอบสิทธิ์ที่จำเป็นก่อนสร้าง token ![Verify Permissions](../../../translated_images/verify_permissions.06bd9e43987a8b219f171bbcf519e45ababae35b844f5e9757e10afcb619b936.th.png)

6. ก่อนสร้าง token ตรวจสอบให้แน่ใจว่าคุณพร้อมที่จะเก็บ token ไว้ในที่ปลอดภัย เช่น vault ของ password manager เนื่องจากมันจะไม่แสดงอีกหลังจากที่คุณสร้างมัน ![Store Token Securely](../../../translated_images/store_token_securely.08ee2274c6ad6caf3482f1cd1bad7ca3fdca1ce737bc485bfa6499c84297c789.th.png)

คัดลอก token ใหม่ที่คุณเพิ่งสร้างขึ้น ตอนนี้คุณจะเพิ่มมันลงในไฟล์ `.env` ที่รวมอยู่ในคอร์สนี้


### ขั้นตอนที่ 2: สร้างไฟล์ `.env` ของคุณ

เพื่อสร้างไฟล์ `.env` ให้รันคำสั่งต่อไปนี้ใน terminal ของคุณ

```bash
cp .env.example .env
```

คำสั่งนี้จะคัดลอกไฟล์ตัวอย่างและสร้าง `.env` ในไดเรกทอรีของคุณ ซึ่งคุณจะเติมค่าของตัวแปรสภาพแวดล้อม

เมื่อคุณคัดลอก token แล้ว ให้เปิดไฟล์ `.env` ใน text editor ที่คุณชื่นชอบและวาง token ของคุณลงในช่อง `GITHUB_TOKEN`
![GitHub Token Field](../../../translated_images/github_token_field.20491ed3224b5f4ab24d10ced7a68c4aba2948fe8999cfc8675edaa16f5e5681.th.png)


ตอนนี้คุณควรสามารถรันตัวอย่างโค้ดของคอร์สนี้ได้แล้ว

## การตั้งค่าสำหรับตัวอย่างที่ใช้ Azure AI Foundry และ Azure AI Agent Service

### ขั้นตอนที่ 1: ดึง Endpoint ของโปรเจกต์ Azure ของคุณ


ปฏิบัติตามขั้นตอนการสร้าง hub และโปรเจกต์ใน Azure AI Foundry ที่พบได้ที่นี่: [Hub resources overview](https://learn.microsoft.com/en-us/azure/ai-foundry/concepts/ai-resources)


เมื่อคุณสร้างโปรเจกต์ของคุณแล้ว คุณจะต้องดึง connection string สำหรับโปรเจกต์ของคุณ

คุณสามารถทำได้โดยไปที่หน้า **Overview** ของโปรเจกต์ใน Azure AI Foundry portal

![Project Connection String](../../../translated_images/project-endpoint.8cf04c9975bbfbf18f6447a599550edb052e52264fb7124d04a12e6175e330a5.th.png)

### ขั้นตอนที่ 2: สร้างไฟล์ `.env` ของคุณ

เพื่อสร้างไฟล์ `.env` ให้รันคำสั่งต่อไปนี้ใน terminal ของคุณ

```bash
cp .env.example .env
```

คำสั่งนี้จะคัดลอกไฟล์ตัวอย่างและสร้าง `.env` ในไดเรกทอรีของคุณ ซึ่งคุณจะเติมค่าของตัวแปรสภาพแวดล้อม

เมื่อคุณคัดลอก token แล้ว ให้เปิดไฟล์ `.env` ใน text editor ที่คุณชื่นชอบและวาง token ของคุณลงในช่อง `PROJECT_ENDPOINT`

### ขั้นตอนที่ 3: ลงชื่อเข้าใช้ Azure

เพื่อความปลอดภัยที่ดีที่สุด เราจะใช้ [keyless authentication](https://learn.microsoft.com/azure/developer/ai/keyless-connections?tabs=csharp%2Cazure-cli?WT.mc_id=academic-105485-koreyst) เพื่อยืนยันตัวตนกับ Azure OpenAI ด้วย Microsoft Entra ID 

ถัดไป เปิด terminal และรัน `az login --use-device-code` เพื่อเข้าสู่ระบบบัญชี Azure ของคุณ

เมื่อคุณเข้าสู่ระบบแล้ว ให้เลือก subscription ของคุณใน terminal


## ตัวแปรสภาพแวดล้อมเพิ่มเติม - Azure Search และ Azure OpenAI 

สำหรับบทเรียน Agentic RAG - บทเรียนที่ 5 - มีตัวอย่างที่ใช้ Azure Search และ Azure OpenAI

หากคุณต้องการรันตัวอย่างเหล่านี้ คุณจะต้องเพิ่มตัวแปรสภาพแวดล้อมต่อไปนี้ลงในไฟล์ `.env` ของคุณ:

### หน้า Overview (โปรเจกต์)

- `AZURE_SUBSCRIPTION_ID` - ตรวจสอบ **Project details** ในหน้า **Overview** ของโปรเจกต์ของคุณ

- `AZURE_AI_PROJECT_NAME` - ดูที่ด้านบนของหน้า **Overview** สำหรับโปรเจกต์ของคุณ

- `AZURE_OPENAI_SERVICE` - ค้นหานี้ในแท็บ **Included capabilities** สำหรับ **Azure OpenAI Service** ในหน้า **Overview**

### Management Center

- `AZURE_OPENAI_RESOURCE_GROUP` - ไปที่ **Project properties** ในหน้า **Overview** ของ **Management Center**

- `GLOBAL_LLM_SERVICE` - ภายใต้ **Connected resources** ค้นหาชื่อการเชื่อมต่อ **Azure AI Services** หากไม่พบ ให้ตรวจสอบ **Azure portal** ภายใต้ resource group ของคุณสำหรับชื่อ resource AI Services

### หน้า Models + Endpoints

- `AZURE_OPENAI_EMBEDDING_DEPLOYMENT_NAME` - เลือกโมเดล embedding ของคุณ (เช่น `text-embedding-ada-002`) และจด **Deployment name** จากรายละเอียดโมเดล

- `AZURE_OPENAI_CHAT_DEPLOYMENT_NAME` - เลือกโมเดล chat ของคุณ (เช่น `gpt-4o-mini`) และจด **Deployment name** จากรายละเอียดโมเดล

### Azure Portal

- `AZURE_OPENAI_ENDPOINT` - ค้นหา **Azure AI services** คลิกที่มัน จากนั้นไปที่ **Resource Management**, **Keys and Endpoint**, เลื่อนลงไปที่ "Azure OpenAI endpoints" และคัดลอก endpoint ที่ระบุว่า "Language APIs"

- `AZURE_OPENAI_API_KEY` - จากหน้าจอเดียวกัน คัดลอก KEY 1 หรือ KEY 2

- `AZURE_SEARCH_SERVICE_ENDPOINT` - ค้นหา resource **Azure AI Search** ของคุณ คลิกที่มัน และดู **Overview**

- `AZURE_SEARCH_API_KEY` - จากนั้นไปที่ **Settings** และ **Keys** เพื่อคัดลอก admin key หลักหรือรอง

### หน้าเว็บภายนอก

- `AZURE_OPENAI_API_VERSION` - เยี่ยมชมหน้า [API version lifecycle](https://learn.microsoft.com/en-us/azure/ai-services/openai/api-version-deprecation#latest-ga-api-release) ภายใต้ **Latest GA API release**

### ตั้งค่าการยืนยันตัวตนแบบ keyless

แทนที่จะ hardcode credentials ของคุณ เราจะใช้การเชื่อมต่อแบบ keyless กับ Azure OpenAI ในการทำเช่นนั้น เราจะ import `DefaultAzureCredential` และเรียกฟังก์ชัน `DefaultAzureCredential` เพื่อรับ credential

```python
from azure.identity import DefaultAzureCredential, InteractiveBrowserCredential
```

## ติดขัดตรงไหน?
หากคุณมีปัญหาในการตั้งค่านี้ สามารถเข้าร่วม <a href="https://discord.gg/kzRShWzttr" target="_blank">Azure AI Community Discord</a> หรือ <a href="https://github.com/microsoft/ai-agents-for-beginners/issues?WT.mc_id=academic-105485-koreyst" target="_blank">สร้างปัญหาใหม่</a> ได้เลย

## บทเรียนถัดไป

ตอนนี้คุณพร้อมที่จะรันโค้ดสำหรับคอร์สนี้แล้ว ขอให้สนุกกับการเรียนรู้เพิ่มเติมเกี่ยวกับโลกของ AI Agents!

[แนะนำ AI Agents และกรณีการใช้งานของ Agent](../01-intro-to-ai-agents/README.md)

---

**ข้อจำกัดความรับผิดชอบ**:  
เอกสารนี้ได้รับการแปลโดยใช้บริการแปลภาษา AI [Co-op Translator](https://github.com/Azure/co-op-translator) แม้ว่าเราจะพยายามให้การแปลมีความถูกต้อง แต่โปรดทราบว่าการแปลอัตโนมัติอาจมีข้อผิดพลาดหรือความไม่ถูกต้อง เอกสารต้นฉบับในภาษาดั้งเดิมควรถือเป็นแหล่งข้อมูลที่เชื่อถือได้ สำหรับข้อมูลที่สำคัญ ขอแนะนำให้ใช้บริการแปลภาษามืออาชีพ เราจะไม่รับผิดชอบต่อความเข้าใจผิดหรือการตีความผิดที่เกิดจากการใช้การแปลนี้