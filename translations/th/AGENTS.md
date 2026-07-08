# AGENTS.md

## ภาพรวมโครงการ

ที่เก็บนี้ประกอบด้วย "AI Agents สำหรับผู้เริ่มต้น" - หลักสูตรการศึกษาครบวงจรสอนทุกสิ่งที่จำเป็นในการสร้าง AI Agents หลักสูตรประกอบด้วยบทเรียน 18 บทที่ครอบคลุมพื้นฐาน รูปแบบการออกแบบ เฟรมเวิร์ก และการนำ AI agents ไปใช้ในสภาพแวดล้อมจริง

**เทคโนโลยีหลัก:**
- Python 3.12+
- Jupyter Notebooks สำหรับการเรียนรู้อย่างโต้ตอบ
- เฟรมเวิร์ก AI: Microsoft Agent Framework (MAF)
- บริการ Azure AI: Microsoft Foundry, Microsoft Foundry Agent Service V2

**สถาปัตยกรรม:**
- โครงสร้างแบบบทเรียน (ไดเรกทอรี 00-15+)
- แต่ละบทเรียนประกอบด้วย: เอกสาร README, ตัวอย่างโค้ด (Jupyter notebooks), และภาพประกอบ
- สนับสนุนหลายภาษาโดยระบบแปลอัตโนมัติ
- โน้ตบุ๊ก Python 1 เล่มต่อบทเรียนโดยใช้ Microsoft Agent Framework

## คำสั่งการติดตั้ง

### สิ่งที่ต้องมีล่วงหน้า
- Python 3.12 ขึ้นไป
- การสมัครสมาชิก Azure (สำหรับ Microsoft Foundry)
- ติดตั้งและเข้าสู่ระบบ Azure CLI (`az login`)

### การตั้งค่าเริ่มต้น

1. **โคลนหรือฟอร์กที่เก็บ:**
   ```bash
   gh repo fork microsoft/ai-agents-for-beginners --clone
   # หรือ
   git clone https://github.com/microsoft/ai-agents-for-beginners.git
   cd ai-agents-for-beginners
   ```

2. **สร้างและเปิดใช้งานสภาพแวดล้อม Python เสมือน:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # บน Windows: venv\Scripts\activate
   ```

3. **ติดตั้ง dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **ตั้งค่าตัวแปรสภาพแวดล้อม:**
   ```bash
   cp .env.example .env
   # แก้ไข .env ด้วยคีย์ API และเอนด์พอยต์ของคุณ
   ```

### ตัวแปรสภาพแวดล้อมที่จำเป็น

สำหรับ **Microsoft Foundry** (จำเป็นต้องมี):
- `AZURE_AI_PROJECT_ENDPOINT` - จุดปลายโครงการ Microsoft Foundry
- `AZURE_AI_MODEL_DEPLOYMENT_NAME` - ชื่อการนำโมเดลไปใช้ (เช่น gpt-4o)

สำหรับ **Azure AI Search** (บทเรียน 05 - RAG):
- `AZURE_SEARCH_SERVICE_ENDPOINT` - จุดปลาย Azure AI Search
- `AZURE_SEARCH_API_KEY` - คีย์ API ของ Azure AI Search

การตรวจสอบสิทธิ์: รัน `az login` ก่อนรันโน้ตบุ๊ก (ใช้ `AzureCliCredential`)

## เวิร์กโฟลว์การพัฒนา

### การรัน Jupyter Notebooks

แต่ละบทเรียนประกอบด้วยโน้ตบุ๊ก Jupyter หลายเล่มสำหรับเฟรมเวิร์กต่าง ๆ:

1. **เริ่ม Jupyter:**
   ```bash
   jupyter notebook
   ```

2. **ไปยังไดเรกทอรีบทเรียน** (เช่น `01-intro-to-ai-agents/code_samples/`)

3. **เปิดและรันโน้ตบุ๊ก:**
   - `*-python-agent-framework.ipynb` - ใช้ Microsoft Agent Framework (Python)
   - `*-dotnet-agent-framework.ipynb` - ใช้ Microsoft Agent Framework (.NET)

### การทำงานกับ Microsoft Agent Framework

**Microsoft Agent Framework + Microsoft Foundry:**
- ต้องมีบัญชีสมาชิก Azure
- ใช้ `FoundryChatClient` สำหรับ Agent Service V2 (เอเจนต์เห็นได้ในพอร์ทัล Foundry)
- พร้อมใช้งานในสภาพแวดล้อมจริงพร้อมความสามารถในการตรวจสอบแบบบูรณาการ
- รูปแบบไฟล์: `*-python-agent-framework.ipynb`

## คำแนะนำการทดสอบ

นี่คือที่เก็บเพื่อการศึกษาโดยมีตัวอย่างโค้ดแทนที่จะเป็นโค้ดสำหรับการผลิตที่มีการทดสอบอัตโนมัติ เพื่อยืนยันการตั้งค่าและการเปลี่ยนแปลงของคุณ:

### การทดสอบด้วยตนเอง

1. **ทดสอบสภาพแวดล้อม Python:**
   ```bash
   python --version  # ควรเป็น 3.12 ขึ้นไป
   pip list | grep -E "(agent-framework|azure-ai|azure-identity)"
   ```

2. **ทดสอบการรันโน้ตบุ๊ก:**
   ```bash
   # แปลงโน้ตบุ๊กเป็นสคริปต์และรัน (ทดสอบการนำเข้า)
   jupyter nbconvert --to script <lesson-folder>/code_samples/<notebook>.ipynb --stdout | python
   ```

3. **ตรวจสอบตัวแปรสภาพแวดล้อม:**
   ```bash
   python -c "import os; from dotenv import load_dotenv; load_dotenv(); print('✓ AZURE_AI_PROJECT_ENDPOINT' if os.getenv('AZURE_AI_PROJECT_ENDPOINT') else '✗ AZURE_AI_PROJECT_ENDPOINT missing')"
   ```

### การรันโน้ตบุ๊กแต่ละเล่ม

เปิดโน้ตบุ๊กใน Jupyter และรันเซลล์ตามลำดับ โน้ตบุ๊กแต่ละเล่มมีความสมบูรณ์ในตัวเอง รวมถึง:
- คำสั่งนำเข้า
- การโหลดการตั้งค่า
- ตัวอย่างการใช้งานเอเจนต์
- ผลลัพธ์ที่คาดหวังในเซลล์ markdown

## รูปแบบโค้ด

### แนวปฏิบัติ Python

- **เวอร์ชัน Python**: 3.12+
- **รูปแบบโค้ด**: ปฏิบัติตามมาตรฐาน Python PEP 8
- **โน้ตบุ๊ก**: ใช้เซลล์ markdown อธิบายแนวคิดอย่างชัดเจน
- **การนำเข้า**: จัดกลุ่มตามไลบรารีมาตรฐาน, บุคคลที่สาม, และภายใน

### แนวปฏิบัติ Jupyter Notebook

- ใส่เซลล์ markdown อธิบายก่อนเซลล์โค้ด
- เพิ่มตัวอย่างผลลัพธ์ในโน้ตบุ๊กเพื่ออ้างอิง
- ใช้ชื่อตัวแปรชัดเจนสอดคล้องกับแนวคิดบทเรียน
- รักษาลำดับการรันโน้ตบุ๊กให้เป็นเส้นตรง (เซลล์ 1 → 2 → 3...)

### การจัดระเบียบไฟล์

```
<lesson-number>-<lesson-name>/
├── README.md                     # Lesson documentation
├── code_samples/
│   ├── <number>-python-agent-framework.ipynb
│   └── <number>-dotnet-agent-framework.ipynb  (optional)
└── images/
    └── *.png
```

## การสร้างและการนำไปใช้

### การสร้างเอกสาร

ที่เก็บนี้ใช้ Markdown สำหรับเอกสาร:
- ไฟล์ README.md ในแต่ละโฟลเดอร์บทเรียน
- README.md หลักที่รูทของที่เก็บ
- ระบบแปลอัตโนมัติผ่าน GitHub Actions

### เส้นทาง CI/CD

ตั้งอยู่ใน `.github/workflows/`:

1. **co-op-translator.yml** - แปลอัตโนมัติไปยัง 50+ ภาษา
2. **welcome-issue.yml** - ต้อนรับผู้สร้างอีชชูใหม่
3. **welcome-pr.yml** - ต้อนรับผู้ส่งคำร้องขอดึง (pull request) ใหม่

### การนำไปใช้

นี่คือที่เก็บเพื่อการศึกษา - ไม่มีขั้นตอนการนำไปใช้ ผู้ใช้:
1. ฟอร์กหรือโคลนที่เก็บ
2. รันโน้ตบุ๊กในเครื่องหรือใน GitHub Codespaces
3. เรียนรู้โดยการแก้ไขและทดลองกับตัวอย่าง

## แนวทางการส่งคำร้องขอดึง (Pull Request)

### ก่อนส่ง

1. **ทดสอบการเปลี่ยนแปลง:**
   - รันโน้ตบุ๊กที่เกี่ยวข้องให้ครบถ้วน
   - ตรวจสอบว่าเซลล์ทั้งหมดรันไม่มีข้อผิดพลาด
   - ตรวจสอบผลลัพธ์ว่าเหมาะสม

2. **อัปเดตเอกสาร:**
   - เปลี่ยน README.md หากเพิ่มแนวคิดใหม่
   - เพิ่มคำอธิบายในโน้ตบุ๊กสำหรับโค้ดที่ซับซ้อน
   - ให้เซลล์ markdown อธิบายวัตถุประสงค์

3. **เปลี่ยนแปลงไฟล์:**
   - หลีกเลี่ยงการคอมมิตไฟล์ `.env` (ใช้ `.env.example`)
   - หลีกเลี่ยงการคอมมิตโฟลเดอร์ `venv/` หรือ `__pycache__/`
   - รักษาผลลัพธ์ในโน้ตบุ๊กเมื่อแสดงแนวคิด
   - ลบไฟล์ชั่วคราวและโน้ตบุ๊กสำรอง (`*-backup.ipynb`)

### รูปแบบชื่อหัวข้อ PR

ใช้ชื่อหัวข้อที่ชัดเจน:
- `[Lesson-XX] เพิ่มตัวอย่างใหม่สำหรับ <concept>`
- `[Fix] แก้ไขคำพิมพ์ผิดใน README ของ lesson-XX`
- `[Update] ปรับปรุงตัวอย่างโค้ดใน lesson-XX`
- `[Docs] อัปเดตคำแนะนำการตั้งค่า`

### การตรวจสอบที่จำเป็น

- โน้ตบุ๊กควรรันไม่มีข้อผิดพลาด
- README ควรชัดเจนและถูกต้อง
- ปฏิบัติตามรูปแบบโค้ดที่มีอยู่ในที่เก็บ
- รักษาความสอดคล้องกับบทเรียนอื่น ๆ

## หมายเหตุเพิ่มเติม

### ความผิดพลาดที่พบบ่อย

1. **เวอร์ชัน Python ไม่ตรงกัน:**
   - ใช้ Python 3.12 ขึ้นไป
   - บางแพ็กเกจอาจไม่ทำงานบนเวอร์ชันเก่า
   - ใช้ `python3 -m venv` เพื่อระบุเวอร์ชัน Python โดยชัดเจน

2. **ตัวแปรสภาพแวดล้อม:**
   - สร้าง `.env` จาก `.env.example` เสมอ
   - อย่าคอมมิตไฟล์ `.env` (มีอยู่ใน `.gitignore`)
   - เข้าสู่ระบบด้วย `az login` เพื่อการตรวจสอบสิทธิ์ Entra ID แบบไม่ใช้คีย์

3. **ความขัดแย้งของแพ็กเกจ:**
   - ใช้สภาพแวดล้อมเสมือนใหม่
   - ติดตั้งจาก `requirements.txt` แทนติดตั้งทีละแพ็กเกจ
   - บางโน้ตบุ๊กอาจต้องการแพ็กเกจเพิ่มเติมซึ่งระบุในเซลล์ markdown

4. **บริการ Azure:**
   - บริการ Azure AI ต้องการการสมัครสมาชิกที่ยังใช้งานอยู่
   - บางฟีเจอร์จำกัดเฉพาะบางภูมิภาค
   - ตรวจสอบให้แน่ใจว่าโมเดล Azure OpenAI ของคุณรองรับ Responses API

### เส้นทางการเรียนรู้

แนะนำให้เรียนตามลำดับบทเรียน:
1. **00-course-setup** - เริ่มที่นี่สำหรับการตั้งค่าสภาพแวดล้อม
2. **01-intro-to-ai-agents** - เข้าใจพื้นฐาน AI agents
3. **02-explore-agentic-frameworks** - เรียนรู้เกี่ยวกับเฟรมเวิร์กต่าง ๆ
4. **03-agentic-design-patterns** - รูปแบบการออกแบบหลัก
5. เรียนต่อเนื่องตามหมายเลขบทเรียน

### การเลือกเฟรมเวิร์ก

เลือกเฟรมเวิร์กตามเป้าหมายของคุณ:
- **ทุกบทเรียน**: Microsoft Agent Framework (MAF) พร้อม `FoundryChatClient`
- **เอเจนต์ลงทะเบียนฝั่งเซิร์ฟเวอร์** ใน Microsoft Foundry Agent Service V2 และมองเห็นผ่านพอร์ทัล Foundry

### การขอความช่วยเหลือ

- เข้าร่วม [Microsoft Foundry Community Discord](https://aka.ms/ai-agents/discord)
- ตรวจสอบไฟล์ README ของบทเรียนสำหรับคำแนะนำเฉพาะด้าน
- ดู [README.md](./README.md) หลักของหลักสูตร
- อ้างอิง [Course Setup](./00-course-setup/README.md) สำหรับคำแนะนำการตั้งค่าโดยละเอียด

### การมีส่วนร่วม

นี่คือโครงการการศึกษาที่เปิดกว้าง ยินดีรับความร่วมมือ:
- ปรับปรุงตัวอย่างโค้ด
- แก้ไขคำผิดหรือข้อผิดพลาด
- เพิ่มคำอธิบายที่ชัดเจน
- เสนอหัวข้อบทเรียนใหม่
- แปลเป็นภาษาอื่นเพิ่มเติม

ดูรายการ [GitHub Issues](https://github.com/microsoft/ai-agents-for-beginners/issues) สำหรับความต้องการปัจจุบัน

## บริบทเฉพาะโครงการ

### การสนับสนุนหลายภาษา

ที่เก็บนี้ใช้ระบบแปลอัตโนมัติ:
- รองรับ 50+ ภาษา
- ไฟล์แปลอยู่ในไดเรกทอรี `/translations/<lang-code>/`
- ใช้ GitHub Actions สำหรับอัปเดตการแปล
- ไฟล์ต้นฉบับเป็นภาษาอังกฤษที่รูทของที่เก็บ

### โครงสร้างบทเรียน

แต่ละบทเรียนมีรูปแบบสม่ำเสมอ:
1. ภาพวิดีโอพร้อมลิงก์
2. เนื้อหาเขียนบทเรียน (README.md)
3. ตัวอย่างโค้ดในหลายเฟรมเวิร์ก
4. วัตถุประสงค์การเรียนรู้และสิ่งที่ต้องมีล่วงหน้า
5. แหล่งเรียนรู้เพิ่มเติมลิงก์ไว้

### การตั้งชื่อไฟล์ตัวอย่างโค้ด

รูปแบบ: `<lesson-number>-python-agent-framework.ipynb`
- `01-python-agent-framework.ipynb` - บทเรียน 1, MAF Python
- `14-sequential.ipynb` - บทเรียน 14, รูปแบบ MAF ขั้นสูง

### โฟลเดอร์พิเศษ

- `translated_images/` - ภาพสำหรับการแปลท้องถิ่น
- `images/` - ภาพต้นฉบับสำหรับเนื้อหาอังกฤษ
- `.devcontainer/` - การตั้งค่า container พัฒนา VS Code
- `.github/` - workflow และเทมเพลตของ GitHub Actions

### dependencies

แพ็กเกจสำคัญจาก `requirements.txt`:
- `agent-framework` - Microsoft Agent Framework
- `a2a-sdk` - สนับสนุนโปรโตคอล Agent-to-Agent
- `azure-ai-inference`, `azure-ai-projects` - บริการ Azure AI
- `azure-identity` - การตรวจสอบสิทธิ์ Azure (AzureCliCredential)
- `azure-search-documents` - การรวม Azure AI Search
- `mcp[cli]` - สนับสนุน Model Context Protocol

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ปฏิเสธความรับผิดชอบ**:
เอกสารนี้ได้รับการแปลโดยใช้บริการแปลภาษา AI [Co-op Translator](https://github.com/Azure/co-op-translator) ขณะที่เราพยายามให้ความถูกต้อง โปรดทราบว่าการแปลโดยอัตโนมัติอาจมีข้อผิดพลาดหรือความไม่ถูกต้อง เอกสารต้นฉบับในภาษาต้นทางควรถูกพิจารณาเป็นแหล่งข้อมูลที่เชื่อถือได้ สำหรับข้อมูลที่สำคัญ แนะนำให้ใช้การแปลโดยมนุษย์มืออาชีพ เราไม่รับผิดชอบต่อความเข้าใจผิดหรือการตีความที่ผิดพลาดที่เกิดขึ้นจากการใช้การแปลนี้
<!-- CO-OP TRANSLATOR DISCLAIMER END -->