# AGENTS.md

## ภาพรวมโครงการ

ที่เก็บนี้ประกอบด้วย "AI Agents สำหรับผู้เริ่มต้น" - คอร์สการศึกษาครบวงจรที่สอนทุกสิ่งที่จำเป็นในการสร้าง AI Agents คอร์สประกอบด้วยบทเรียน 18 บท (หมายเลข 00-18) ครอบคลุมพื้นฐาน รูปแบบการออกแบบ เฟรมเวิร์ก การใช้งานจริง ตัวแทนในเครื่อง/อุปกรณ์ และความปลอดภัยของ AI agents

**เทคโนโลยีสำคัญ:**
- Python 3.12+
- Jupyter Notebooks สำหรับการเรียนรู้แบบอินเทอร์แอกทีฟ
- เฟรมเวิร์ก AI: Microsoft Agent Framework (MAF)
- บริการ Azure AI: Microsoft Foundry, Microsoft Foundry Agent Service V2

**สถาปัตยกรรม:**
- โครงสร้างตามบทเรียน (ไดเรกทอรี 00-15+)
- แต่ละบทเรียนประกอบด้วย: เอกสาร README, ตัวอย่างโค้ด (Jupyter notebooks) และรูปภาพ
- รองรับหลายภาษาโดยระบบแปลอัตโนมัติ
- โน้ตบุ๊ค Python หนึ่งไฟล์ต่อบทเรียนโดยใช้ Microsoft Agent Framework

## คำสั่งการตั้งค่า

### ความต้องการเบื้องต้น
- Python 3.12 หรือสูงกว่า
- สมัครสมาชิก Azure (สำหรับ Microsoft Foundry)
- ติดตั้งและเข้าสู่ระบบ Azure CLI (`az login`)

### การตั้งค่าเริ่มต้น

1. **โคลนหรือฟอร์กที่เก็บนี้:**
   ```bash
   gh repo fork microsoft/ai-agents-for-beginners --clone
   # หรือ
   git clone https://github.com/microsoft/ai-agents-for-beginners.git
   cd ai-agents-for-beginners
   ```

2. **สร้างและเปิดใช้งานสภาพแวดล้อมเสมือน Python:**
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
   # แก้ไข .env ด้วยคีย์ API และ endpoints ของคุณ
   ```

### ตัวแปรสภาพแวดล้อมที่จำเป็น

สำหรับ **Microsoft Foundry** (จำเป็น):
- `AZURE_AI_PROJECT_ENDPOINT` - จุดสิ้นสุดโปรเจค Microsoft Foundry
- `AZURE_AI_MODEL_DEPLOYMENT_NAME` - ชื่อการใช้งานโมเดล (เช่น gpt-5-mini)

สำหรับ **Azure AI Search** (บทเรียน 05 - RAG):
- `AZURE_SEARCH_SERVICE_ENDPOINT` - จุดเชื่อมต่อ Azure AI Search
- `AZURE_SEARCH_API_KEY` - คีย์ API ของ Azure AI Search

การรับรองความถูกต้อง: รัน `az login` ก่อนรันโน้ตบุ๊ค (ใช้ `AzureCliCredential`)

## กระบวนการพัฒนา

### การรัน Jupyter Notebooks

แต่ละบทเรียนประกอบด้วยหลาย Jupyter notebook สำหรับเฟรมเวิร์กต่างๆ:

1. **เริ่ม Jupyter:**
   ```bash
   jupyter notebook
   ```

2. **ไปที่ไดเรกทอรีบทเรียน** (เช่น `01-intro-to-ai-agents/code_samples/`)

3. **เปิดและรันโน้ตบุ๊ค:**
   - `*-python-agent-framework.ipynb` - ใช้ Microsoft Agent Framework (Python)
   - `*-dotnet-agent-framework.ipynb` - ใช้ Microsoft Agent Framework (.NET)

### การทำงานกับ Microsoft Agent Framework

**Microsoft Agent Framework + Microsoft Foundry:**
- ต้องมีบัญชี Azure
- ใช้ `FoundryChatClient` สำหรับ Agent Service V2 (มองเห็นตัวแทนในพอร์ทัล Foundry)
- พร้อมใช้การผลิตพร้อมการตรวจสอบในตัว
- รูปแบบไฟล์: `*-python-agent-framework.ipynb`

## คำแนะนำการทดสอบ

นี่คือที่เก็บสำหรับการศึกษาโดยมีตัวอย่างโค้ดแทนโค้ดโปรดักชันแบบทดสอบอัตโนมัติ ในการตรวจสอบการตั้งค่าและการเปลี่ยนแปลง:

### การทดสอบด้วยตนเอง

1. **ทดสอบสภาพแวดล้อม Python:**
   ```bash
   python --version  # ควรเป็น 3.12 ขึ้นไป
   pip list | grep -E "(agent-framework|azure-ai|azure-identity)"
   ```

2. **ทดสอบการรันโน้ตบุ๊ค:**
   ```bash
   # แปลงโน้ตบุ๊คเป็นสคริปต์และรัน (ทดสอบการนำเข้า)
   jupyter nbconvert --to script <lesson-folder>/code_samples/<notebook>.ipynb --stdout | python
   ```

3. **ตรวจสอบตัวแปรสภาพแวดล้อม:**
   ```bash
   python -c "import os; from dotenv import load_dotenv; load_dotenv(); print('✓ AZURE_AI_PROJECT_ENDPOINT' if os.getenv('AZURE_AI_PROJECT_ENDPOINT') else '✗ AZURE_AI_PROJECT_ENDPOINT missing')"
   ```

### การรันโน้ตบุ๊คแต่ละอัน

เปิดโน้ตบุ๊คใน Jupyter และรันเซลล์ทีละอัน โน้ตบุ๊คแต่ละไฟล์เป็นแบบแยกตัวและรวม:
- คำสั่งนำเข้า
- การโหลดการตั้งค่า
- การประกอบตัวแทนเป็นตัวอย่าง
- ผลลัพธ์ที่คาดหวังในเซลล์ markdown

### การทดสอบ smoke-test ตัวแทนที่เผยแพร่

สำหรับบทเรียนที่ตัวแทนถูกใช้งานใน Microsoft Foundry (01, 04, 05, 16) รีโปจัดเตรียมสมุดแสดงการทดสอบ smoke-test ภายใต้ `tests/` ที่รันโดยเวิร์กโฟลว์ `.github/workflows/smoke-test.yml` ผ่านแอคชั่น [AI Smoke Test](https://github.com/marketplace/actions/ai-smoke-test) นี่เป็นเกตน้ำหนักเบาหลังการใช้งานจริง (ตัวแทนเชื่อมต่อได้และตอบสนองตามคำสั่งพื้นฐาน?) ที่เสริมการประเมินในบทเรียน 10 และ 16 ดู [tests/README.md](./tests/README.md) สำหรับแผนที่สมุดรายการ-บทเรียน-ตัวแทน บทเรียน 17 ทำงานในเครื่องด้วย Foundry Local และไม่มีจุดเชื่อมต่อโฮสต์ จึงตรวจสอบโดยการรันโน้ตบุ๊คโดยตรง

## สไตล์โค้ด

### กฎการเขียน Python

- **เวอร์ชัน Python**: 3.12+
- **สไตล์โค้ด**: ปฏิบัติตามมาตรฐาน Python PEP 8
- **โน้ตบุ๊ค**: ใช้เซลล์ markdown ที่ชัดเจนในการอธิบายแนวคิด
- **การนำเข้า**: แบ่งกลุ่มตามไลบรารีมาตรฐาน ไลบรารีภายนอก และไลบรารีในเครื่อง

### กฎการใช้งาน Jupyter Notebook

- รวมเซลล์ markdown ที่อธิบายก่อนเซลล์โค้ด
- เพิ่มตัวอย่างผลลัพธ์ในโน้ตบุ๊คเพื่ออ้างอิง
- ใช้ชื่อตัวแปรที่ชัดเจนและตรงกับแนวคิดบทเรียน
- รักษาลำดับการรันโน้ตบุ๊คเป็นเส้นตรง (เซลล์ 1 → 2 → 3...)

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

## การสร้างและการปรับใช้

### การสร้างเอกสาร

ที่เก็บนี้ใช้ Markdown สำหรับเอกสาร:
- ไฟล์ README.md ในแต่ละโฟลเดอร์บทเรียน
- README.md หลักที่รูทของที่เก็บ
- ระบบแปลอัตโนมัติผ่าน GitHub Actions

### CI/CD Pipeline

อยู่ใน `.github/workflows/`:

1. **co-op-translator.yml** - การแปลอัตโนมัติเป็นมากกว่า 50 ภาษา
2. **welcome-issue.yml** - ต้อนรับผู้สร้าง issue ใหม่
3. **welcome-pr.yml** - ต้อนรับผู้ส่ง pull request ใหม่

### การปรับใช้

นี่เป็นที่เก็บสำหรับการศึกษา - ไม่มีขั้นตอนการปรับใช้ ผู้ใช้:
1. ฟอร์กหรือโคลนที่เก็บ
2. รันโน้ตบุ๊คในเครื่องหรือใน GitHub Codespaces
3. เรียนรู้โดยการแก้ไขและทดลองกับตัวอย่าง

## แนวทางการส่ง Pull Request

### ก่อนส่ง

1. **ทดสอบการเปลี่ยนแปลงของคุณ:**
   - รันโน้ตบุ๊คที่ได้รับผลกระทบทั้งหมด
   - ตรวจสอบให้แน่ใจว่าเซลล์ทั้งหมดรันโดยไม่มีข้อผิดพลาด
   - ตรวจสอบผลลัพธ์ว่าถูกต้องเหมาะสม

2. **อัปเดตเอกสาร:**
   - อัปเดต README.md หากเพิ่มแนวคิดใหม่
   - เพิ่มคอมเมนต์ในโน้ตบุ๊คสำหรับโค้ดที่ซับซ้อน
   - ให้แน่ใจว่าเซลล์ markdown อธิบายวัตถุประสงค์

3. **การเปลี่ยนแปลงไฟล์:**
   - หลีกเลี่ยงการ commit ไฟล์ `.env` (ใช้ `.env.example`)
   - อย่า commit โฟลเดอร์ `venv/` หรือ `__pycache__/`
   - เก็บผลลัพธ์โน้ตบุ๊คไว้เมื่อแสดงแนวคิด
   - ลบไฟล์ชั่วคราวและโน้ตบุ๊คสำรอง (`*-backup.ipynb`)

### รูปแบบหัวข้อ PR

ใช้หัวข้อที่ชัดเจน:
- `[Lesson-XX] เพิ่มตัวอย่างใหม่สำหรับ <concept>`
- `[Fix] แก้ไขคำผิดใน README ของบทเรียน-XX`
- `[Update] ปรับปรุงตัวอย่างโค้ดในบทเรียน-XX`
- `[Docs] อัปเดตคำแนะนำการตั้งค่า`

### การตรวจสอบที่จำเป็น

- โน้ตบุ๊คต้องรันโดยไม่มีข้อผิดพลาด
- ไฟล์ README ต้องชัดเจนและถูกต้อง
- ปฏิบัติตามรูปแบบโค้ดที่มีอยู่ในที่เก็บ
- รักษาความสอดคล้องกับบทเรียนอื่นๆ

## หมายเหตุเพิ่มเติม

### ปัญหาทั่วไป

1. **เวอร์ชัน Python ไม่ตรงกัน:**
   - ตรวจสอบให้แน่ใจว่าใช้ Python 3.12+ 
   - บางแพ็คเกจอาจไม่ทำงานกับเวอร์ชันเก่า
   - ใช้ `python3 -m venv` เพื่อกำหนดเวอร์ชัน Python อย่างชัดเจน

2. **ตัวแปรสภาพแวดล้อม:**
   - สร้าง `.env` จาก `.env.example` เสมอ
   - หลีกเลี่ยงการ commit ไฟล์ `.env` (อยู่ใน `.gitignore`)
   - ลงชื่อเข้าใช้ด้วย `az login` เพื่อรับรอง身份 Entra ID แบบไม่ใช้รหัสผ่าน

3. **ความขัดแย้งของแพ็คเกจ:**
   - ใช้สภาพแวดล้อมเสมือนใหม่
   - ติดตั้งจาก `requirements.txt` แทนติดตั้งแพ็คเกจแยก
   - บางโน้ตบุ๊คอาจต้องแพ็คเกจเพิ่มเติมซึ่งระบุไว้ในเซลล์ markdown ของตน

4. **บริการ Azure:**
   - บริการ Azure AI ต้องการสมาชิกใช้งานที่เปิดใช้งานอยู่
   - บางฟีเจอร์จำกัดเฉพาะภูมิภาค
   - ตรวจสอบให้มั่นใจว่าการใช้งานโมเดล Azure OpenAI ของคุณรองรับ Responses API

### เส้นทางการเรียนรู้

แนะนำการเรียนรู้ผ่านบทเรียน:
1. **00-course-setup** - เริ่มที่นี่สำหรับการตั้งค่าสภาพแวดล้อม
2. **01-intro-to-ai-agents** - เข้าใจพื้นฐานของ AI agents
3. **02-explore-agentic-frameworks** - เรียนรู้เกี่ยวกับเฟรมเวิร์กต่างๆ
4. **03-agentic-design-patterns** - รูปแบบการออกแบบหลัก
5. เรียนรู้อย่างต่อเนื่องตามลำดับหมายเลขบทเรียน

### การเลือกเฟรมเวิร์ก

เลือกเฟรมเวิร์กตามเป้าหมายของคุณ:
- **ทุกบทเรียน**: Microsoft Agent Framework (MAF) พร้อม `FoundryChatClient`
- **ตัวแทนลงทะเบียนฝั่งเซิร์ฟเวอร์** ใน Microsoft Foundry Agent Service V2 และมองเห็นในพอร์ทัล Foundry

### การขอความช่วยเหลือ

- เข้าร่วม [Microsoft Foundry Community Discord](https://aka.ms/ai-agents/discord)
- ตรวจสอบไฟล์ README ของบทเรียนเพื่อคำแนะนำเฉพาะ
- ดู [README.md](./README.md) หลักสำหรับภาพรวมคอร์ส
- ดู [การตั้งค่าคอร์ส](./00-course-setup/README.md) สำหรับคำแนะนำการตั้งค่าโดยละเอียด

### การมีส่วนร่วม

นี่คือโครงการศึกษาเปิดรับการมีส่วนร่วม:
- ปรับปรุงตัวอย่างโค้ด
- แก้ไขคำผิดหรือข้อผิดพลาด
- เพิ่มคอมเมนต์อธิบายชัดเจน
- แนะนำหัวข้อบทเรียนใหม่
- แปลเป็นภาษาต่างๆ เพิ่มเติม

ดูที่ [GitHub Issues](https://github.com/microsoft/ai-agents-for-beginners/issues) สำหรับความต้องการปัจจุบัน

## บริบทเฉพาะโครงการ

### รองรับหลายภาษา

ที่เก็บนี้ใช้ระบบแปลอัตโนมัติ:
- รองรับมากกว่า 50 ภาษา
- การแปลอยู่ในไดเรกทอรี `/translations/<lang-code>/`
- เวิร์กโฟลว์ GitHub Actions ดูแลการอัปเดตการแปล
- ไฟล์ต้นฉบับเป็นภาษาอังกฤษที่รูทของที่เก็บ

### โครงสร้างบทเรียน

แต่ละบทเรียนตามลำดับเดียวกัน:
1. ภาพย่อวิดีโอพร้อมลิงก์
2. เนื้อหาบทเรียนเป็นลายลักษณ์อักษร (README.md)
3. ตัวอย่างโค้ดในหลายเฟรมเวิร์ก
4. วัตถุประสงค์การเรียนรู้และข้อกำหนดเบื้องต้น
5. แหล่งเรียนรู้เพิ่มเติมที่ลิงก์ไว้

### การตั้งชื่อไฟล์ตัวอย่างโค้ด

รูปแบบ: `<lesson-number>-python-agent-framework.ipynb`
- `01-python-agent-framework.ipynb` - บทเรียน 1, MAF Python
- `14-sequential.ipynb` - บทเรียน 14, รูปแบบขั้นสูง MAF
- `16-python-agent-framework.ipynb` - บทเรียน 16, ตัวแทนสนับสนุนลูกค้าพร้อมใช้งานจริง
- `17-local-agent-foundry-local.ipynb` - บทเรียน 17, ตัวแทนในเครื่องด้วย Foundry Local + Qwen

### โฟลเดอร์พิเศษ

- `translated_images/` - รูปภาพแปลภาษาที่แปลแล้ว
- `images/` - รูปภาพต้นฉบับสำหรับเนื้อหาอังกฤษ
- `.devcontainer/` - การตั้งค่าคอนเทนเนอร์พัฒนา VS Code
- `.github/` - เวิร์กโฟลว์และเทมเพลต GitHub Actions

### Dependencies

แพ็คเกจสำคัญจาก `requirements.txt`:
- `agent-framework` - Microsoft Agent Framework
- `a2a-sdk` - การสนับสนุนโปรโตคอล Agent-to-Agent
- `azure-ai-inference`, `azure-ai-projects` - บริการ Azure AI
- `azure-identity` - การรับรอง Azure (AzureCliCredential)
- `azure-search-documents` - การรวม Azure AI Search
- `mcp[cli]` - การสนับสนุน Model Context Protocol

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ปฏิเสธความรับผิดชอบ**:
เอกสารนี้ได้รับการแปลโดยใช้บริการแปลภาษา AI [Co-op Translator](https://github.com/Azure/co-op-translator) ขณะที่เราพยายามให้ความถูกต้อง โปรดทราบว่าการแปลโดยอัตโนมัติอาจมีข้อผิดพลาดหรือความไม่ถูกต้อง เอกสารต้นฉบับในภาษาต้นทางควรถูกพิจารณาเป็นแหล่งข้อมูลที่เชื่อถือได้ สำหรับข้อมูลที่สำคัญ แนะนำให้ใช้การแปลโดยมนุษย์มืออาชีพ เราไม่รับผิดชอบต่อความเข้าใจผิดหรือการตีความที่ผิดพลาดที่เกิดขึ้นจากการใช้การแปลนี้
<!-- CO-OP TRANSLATOR DISCLAIMER END -->