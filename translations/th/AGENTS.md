# AGENTS.md

## ภาพรวมโครงการ

ที่เก็บนี้ประกอบด้วย "AI Agents for Beginners" - หลักสูตรการศึกษาแบบครบวงจรที่สอนทุกอย่างที่จำเป็นในการสร้าง AI Agents หลักสูตรประกอบด้วยบทเรียน 18 บท (หมายเลข 00-18) ซึ่งครอบคลุมพื้นฐาน, รูปแบบการออกแบบ, เฟรมเวิร์ก, การนำไปใช้งานในผลิตภัณฑ์, เอเย่นต์บนเครื่อง/ในอุปกรณ์ และความปลอดภัยของ AI Agents

**เทคโนโลยีสำคัญ:**
- Python 3.12+
- Jupyter Notebooks สำหรับการเรียนรู้แบบโต้ตอบ
- เฟรมเวิร์ก AI: Microsoft Agent Framework (MAF)
- บริการ Azure AI: Microsoft Foundry, Microsoft Foundry Agent Service V2

**สถาปัตยกรรม:**
- โครงสร้างตามบทเรียน (ไดเรกทอรี 00-18)
- แต่ละบทเรียนประกอบด้วย: เอกสาร README, ตัวอย่างโค้ด (Jupyter notebooks), และรูปภาพ
- รองรับหลายภาษาโดยระบบแปลอัตโนมัติ
- โน้ตบุ๊ค Python หนึ่งเล่มต่อบทเรียนโดยใช้ Microsoft Agent Framework

## คำสั่งติดตั้ง

### ข้อกำหนดเบื้องต้น
- Python 3.12 หรือสูงกว่า
- มีการสมัครสมาชิก Azure (สำหรับ Microsoft Foundry)
- ติดตั้งและล็อกอิน Azure CLI (`az login`)

### การตั้งค่าเริ่มต้น

1. **โคลนหรือฟอร์กที่เก็บนี้:**
   ```bash
   gh repo fork microsoft/ai-agents-for-beginners --clone
   # OR
   git clone https://github.com/microsoft/ai-agents-for-beginners.git
   cd ai-agents-for-beginners
   ```

2. **สร้างและเปิดใช้งานสภาพแวดล้อมเสมือน Python:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **ติดตั้ง dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **ตั้งค่าตัวแปรสภาพแวดล้อม:**
   ```bash
   cp .env.example .env
   # Edit .env with your API keys and endpoints
   ```

### ตัวแปรสภาพแวดล้อมที่จำเป็น

สำหรับ **Microsoft Foundry** (จำเป็น):
- `AZURE_AI_PROJECT_ENDPOINT` - จุดสิ้นสุดโปรเจกต์ Microsoft Foundry
- `AZURE_AI_MODEL_DEPLOYMENT_NAME` - ชื่อการนำโมเดลไปใช้ (เช่น gpt-5-mini)

สำหรับ **Azure AI Search** (บทเรียน 05 - RAG):
- `AZURE_SEARCH_SERVICE_ENDPOINT` - จุดสิ้นสุด Azure AI Search
- `AZURE_SEARCH_API_KEY` - คีย์ API ของ Azure AI Search

การตรวจสอบตัวตน: รัน `az login` ก่อนเปิดใช้โน้ตบุ๊ค (ใช้ `AzureCliCredential`)

## กระบวนการพัฒนา

### การเรียกใช้งาน Jupyter Notebooks

แต่ละบทเรียนมี Jupyter notebooks หลายเล่มสำหรับเฟรมเวิร์กต่างๆ:

1. **เริ่ม Jupyter:**
   ```bash
   jupyter notebook
   ```

2. **ไปยังไดเรกทอรีบทเรียน** (เช่น `01-intro-to-ai-agents/code_samples/`)

3. **เปิดและรันโน้ตบุ๊ค:**
   - `*-python-agent-framework.ipynb` - ใช้ Microsoft Agent Framework (Python)
   - `*-dotnet-agent-framework.ipynb` - ใช้ Microsoft Agent Framework (.NET)

### การทำงานกับ Microsoft Agent Framework

**Microsoft Agent Framework + Microsoft Foundry:**
- ต้องมีการสมัครสมาชิก Azure
- ใช้ `FoundryChatClient` สำหรับ Agent Service V2 (เอเย่นต์ที่เห็นได้ในพอร์ทัล Foundry)
- พร้อมใช้ในสภาพแวดล้อมจริงด้วยความสามารถตรวจสอบในตัว
- แบบไฟล์: `*-python-agent-framework.ipynb`

## คำแนะนำการทดสอบ

นี่คือที่เก็บเพื่อการศึกษาโดยมีตัวอย่างโค้ดแทนที่จะเป็นโค้ดผลิตภัณฑ์ที่มีการทดสอบอัตโนมัติ ในการยืนยันการตั้งค่าและการเปลี่ยนแปลงของคุณ:

### การทดสอบแบบแมนนวล

1. **ทดสอบสภาพแวดล้อม Python:**
   ```bash
   python --version  # Should be 3.12+
   pip list | grep -E "(agent-framework|azure-ai|azure-identity)"
   ```

2. **ทดสอบการรันโน้ตบุ๊ค:**
   ```bash
   # Convert notebook to script and run (tests imports)
   jupyter nbconvert --to script <lesson-folder>/code_samples/<notebook>.ipynb --stdout | python
   ```

3. **ตรวจสอบตัวแปรสภาพแวดล้อม:**
   ```bash
   python -c "import os; from dotenv import load_dotenv; load_dotenv(); print('✓ AZURE_AI_PROJECT_ENDPOINT' if os.getenv('AZURE_AI_PROJECT_ENDPOINT') else '✗ AZURE_AI_PROJECT_ENDPOINT missing')"
   ```

### การรันโน้ตบุ๊คแต่ละเล่ม

เปิดโน้ตบุ๊คใน Jupyter และรันเซลล์ทีละขั้นตอน แต่ละโน้ตบุ๊คเป็นอิสระและประกอบด้วย:
- คำสั่งนำเข้า
- การโหลดการตั้งค่า
- ตัวอย่างการใช้งานเอเย่นต์
- ข้อมูลผลลัพธ์ที่คาดหวังในเซลล์ markdown

### การตรวจสอบเบื้องต้นของเอเย่นต์ที่เผยแพร่

สำหรับบทเรียนที่มีการนำเอเย่นต์ไปเผยแพร่ในฐานะเอเย่นต์ Microsoft Foundry (01, 04, 05, 16) ที่เก็บนี้จะมาพร้อมกับแคตตาล็อกทดสอบเบื้องต้นใต้ `tests/` ซึ่งถูกรันโดย workflow `.github/workflows/smoke-test.yml` ผ่าน action [AI Smoke Test](https://github.com/marketplace/actions/ai-smoke-test) ซึ่งเป็นประตูตรวจสอบเบื้องต้นหลังปล่อยใช้งาน (สามารถเข้าถึงเอเย่นต์และปฏิบัติตามคำสั่งพื้นฐานหรือไม่?) ซึ่งช่วยเสริมท่อประเมินผลในบทเรียน 10 และ 16 ดูรายละเอียดการจับคู่แค็ตตาล็อก-บทเรียน-เอเย่นต์ใน [tests/README.md](./tests/README.md) บทเรียน 17 รันในเครื่องด้วย Foundry Local และไม่มีจุดสิ้นสุดบนโฮสต์ จึงตรวจสอบโดยการรันโน้ตบุ๊คโดยตรง

## รูปแบบโค้ด

### ข้อกำหนด Python

- **เวอร์ชัน Python**: 3.12+
- **รูปแบบโค้ด**: ปฏิบัติตามมาตรฐาน PEP 8 ของ Python
- **โน้ตบุ๊ค**: ใช้เซลล์ markdown อธิบายแนวคิดอย่างชัดเจน
- **คำสั่งนำเข้า**: แบ่งกลุ่มคำสั่งนำเข้าตามไลบรารีมาตรฐาน, บุคคลที่สาม, นำเข้าท้องถิ่น

### ข้อกำหนด Jupyter Notebook

- มีเซลล์ markdown อธิบายก่อนเซลล์โค้ด
- เพิ่มตัวอย่างผลลัพธ์ในโน้ตบุ๊คเพื่ออ้างอิง
- ใช้ชื่อตัวแปรที่ชัดเจนและสอดคล้องกับแนวคิดบทเรียน
- รันโน้ตบุ๊คตามลำดับเซลล์แบบเชิงเส้น (เซลล์ 1 → 2 → 3…)

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

## การสร้างและนำไปใช้งาน

### การสร้างเอกสาร

ที่เก็บนี้ใช้ Markdown สำหรับเอกสาร:
- ไฟล์ README.md ในแต่ละโฟลเดอร์บทเรียน
- README.md หลักที่รากที่เก็บข้อมูล
- ระบบแปลอัตโนมัติผ่าน GitHub Actions

### ท่อ CI/CD

อยู่ใน `.github/workflows/`:

1. **co-op-translator.yml** - แปลอัตโนมัติเป็นกว่า 50 ภาษา
2. **welcome-issue.yml** - ต้อนรับผู้สร้างอีชชูใหม่
3. **welcome-pr.yml** - ต้อนรับผู้ส่ง Pull Request ใหม่

### การนำไปใช้งาน

นี่เป็นที่เก็บเพื่อการศึกษา - ไม่มีขั้นตอนการนำไปใช้งาน ผู้ใช้:
1. Fork หรือโคลนที่เก็บ
2. รันโน้ตบุ๊คในเครื่องหรือใน GitHub Codespaces
3. เรียนรู้โดยการแก้ไขและทดลองตัวอย่าง

## แนวทางการส่ง Pull Request

### ก่อนส่ง

1. **ทดสอบการเปลี่ยนแปลงของคุณ:**
   - รันโน้ตบุ๊คที่เกี่ยวข้องให้ครบถ้วน
   - ตรวจสอบให้แน่ใจว่าเซลล์ทั้งหมดรันไม่มีข้อผิดพลาด
   - ตรวจสอบว่าผลลัพธ์เหมาะสม

2. **ปรับปรุงเอกสาร:**
   - อัพเดต README.md หากเพิ่มแนวคิดใหม่
   - เพิ่มคอมเมนต์ในโน้ตบุ๊คสำหรับโค้ดที่ซับซ้อน
   - ตรวจสอบว่าเซลล์ markdown อธิบายจุดประสงค์ชัดเจน

3. **การเปลี่ยนแปลงไฟล์:**
   - หลีกเลี่ยงการคอมมิตไฟล์ `.env` (ใช้ `.env.example` แทน)
   - ไม่คอมมิตไดเรกทอรี `venv/` หรือ `__pycache__/`
   - เก็บผลลัพธ์โน้ตบุ๊คเมื่อแสดงแนวคิด
   - ลบไฟล์ชั่วคราวและสำรองโน้ตบุ๊ค (`*-backup.ipynb`)

### รูปแบบหัวข้อ PR

ใช้หัวข้อที่สื่อความหมาย:
- `[Lesson-XX] Add new example for <concept>`
- `[Fix] Correct typo in lesson-XX README`
- `[Update] Improve code sample in lesson-XX`
- `[Docs] Update setup instructions`

### การตรวจสอบที่จำเป็น

- โน้ตบุ๊ครันได้โดยไม่มีข้อผิดพลาด
- ไฟล์ README ควรชัดเจนและถูกต้อง
- ปฏิบัติตามรูปแบบโค้ดที่มีในที่เก็บนี้
- รักษาความสอดคล้องกับบทเรียนอื่นๆ

## หมายเหตุเพิ่มเติม

### ข้อควรระวังทั่วไป

1. **เวอร์ชัน Python ไม่ตรงกัน:**
   - ใช้ Python 3.12+ ให้แน่ใจ
   - บางแพ็กเกจอาจไม่ทำงานกับเวอร์ชันเก่า
   - ใช้ `python3 -m venv` เพื่อระบุเวอร์ชัน Python อย่างชัดเจน

2. **ตัวแปรสภาพแวดล้อม:**
   - สร้าง `.env` จาก `.env.example` เสมอ
   - อย่าคอมมิตไฟล์ `.env` (อยู่ใน `.gitignore`)
   - ลงชื่อเข้าใช้ด้วย `az login` สำหรับการตรวจสอบตัวตน Entra ID แบบไม่มีคีย์

3. **ความขัดแย้งของแพ็กเกจ:**
   - ใช้สภาพแวดล้อมเสมือนใหม่
   - ติดตั้งจาก `requirements.txt` แทนติดตั้งแยกแพ็กเกจ
   - บางโน้ตบุ๊คอาจต้องติดตั้งแพ็กเกจเพิ่มเติมตามที่ระบุในเซลล์ markdown

4. **บริการ Azure:**
   - บริการ Azure AI ต้องมีการสมัครสมาชิกที่เปิดใช้งาน
   - บางฟีเจอร์ขึ้นกับภูมิภาค
   - ตรวจสอบให้แน่ใจว่าการนำโมเดล Azure OpenAI ของคุณรองรับ Responses API

### เส้นทางการเรียนรู้

แนะนำให้เรียนตามลำดับบทเรียน:
1. **00-course-setup** - เริ่มที่นี่สำหรับการตั้งค่าสภาพแวดล้อม
2. **01-intro-to-ai-agents** - ทำความเข้าใจพื้นฐานของเอเย่นต์ AI
3. **02-explore-agentic-frameworks** - เรียนรู้เกี่ยวกับเฟรมเวิร์กต่างๆ
4. **03-agentic-design-patterns** - รูปแบบการออกแบบหลัก
5. เรียนต่อเนื่องผ่านบทเรียนที่มีหมายเลขตามลำดับ

### การเลือกเฟรมเวิร์ก

เลือกเฟรมเวิร์กตามเป้าหมายของคุณ:
- **ทุกบทเรียน**: Microsoft Agent Framework (MAF) พร้อม `FoundryChatClient`
- **เอเย่นต์จดทะเบียนฝั่งเซิร์ฟเวอร์** ใน Microsoft Foundry Agent Service V2 และแสดงตรงพอร์ทัล Foundry

### การขอความช่วยเหลือ

- เข้าร่วม [Microsoft Foundry Community Discord](https://aka.ms/ai-agents/discord)
- ตรวจสอบไฟล์ README ของบทเรียนสำหรับคำแนะนำเฉพาะ
- เยี่ยมชม [README.md หลัก](./README.md) สำหรับภาพรวมของหลักสูตร
- ดู [Course Setup](./00-course-setup/README.md) สำหรับคำแนะนำการตั้งค่าโดยละเอียด

### การมีส่วนร่วม

นี่เป็นโครงการการศึกษาที่เปิดรับสมาชิก: 
- ปรับปรุงตัวอย่างโค้ด
- แก้ไขไวยากรณ์หรือข้อผิดพลาด
- เพิ่มคอมเมนต์อธิบาย
- เสนอหัวข้อบทเรียนใหม่
- แปลเป็นภาษาอื่นเพิ่มเติม

ดูที่ [GitHub Issues](https://github.com/microsoft/ai-agents-for-beginners/issues) สำหรับความต้องการปัจจุบัน

## บริบทเฉพาะโครงการ

### การรองรับหลายภาษา

ที่เก็บนี้ใช้ระบบแปลอัตโนมัติ:
- รองรับมากกว่า 50 ภาษา
- แปลอยู่ในไดเรกทอรี `/translations/<lang-code>/`
- GitHub Actions workflow จัดการการอัปเดตการแปล
- ไฟล์ต้นฉบับเป็นภาษาอังกฤษที่รากที่เก็บ

### โครงสร้างบทเรียน

แต่ละบทเรียนเป็นไปตามรูปแบบเดียวกัน:
1. ภาพขนาดย่อวิดีโอพร้อมลิงก์
2. เนื้อหาบทเรียนแบบเขียน (README.md)
3. ตัวอย่างโค้ดในหลายเฟรมเวิร์ก
4. วัตถุประสงค์การเรียนรู้และข้อกำหนดเบื้องต้น
5. แหล่งเรียนรู้เพิ่มเติมที่มีลิงก์

### การตั้งชื่อไฟล์ตัวอย่างโค้ด

รูปแบบ: `<lesson-number>-python-agent-framework.ipynb`
- `01-python-agent-framework.ipynb` - บทเรียน 1, MAF Python
- `14-sequential.ipynb` - บทเรียน 14, รูปแบบขั้นสูงของ MAF
- `16-python-agent-framework.ipynb` - บทเรียน 16, เอเย่นต์สนับสนุนลูกค้าที่ใช้งานจริง
- `17-local-agent-foundry-local.ipynb` - บทเรียน 17, เอเย่นต์ท้องถิ่นพร้อม Foundry Local + Qwen

### ไดเรกทอรีพิเศษ

- `translated_images/` - รูปภาพที่แปลท้องถิ่น
- `images/` - รูปภาพต้นฉบับสำหรับเนื้อหาอังกฤษ
- `.devcontainer/` - การกำหนดคอนเทนเนอร์สำหรับพัฒนา VS Code
- `.github/` - GitHub Actions workflows และเทมเพลต

### Dependencies

แพ็กเกจสำคัญจาก `requirements.txt`:
- `agent-framework` - Microsoft Agent Framework
- `a2a-sdk` - การรองรับโปรโตคอล Agent-to-Agent
- `azure-ai-inference`, `azure-ai-projects` - บริการ Azure AI
- `azure-identity` - การตรวจสอบตัวตน Azure (AzureCliCredential)
- `azure-search-documents` - การเชื่อมต่อ Azure AI Search
- `mcp[cli]` - การรองรับโปรโตคอล Model Context

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ปฏิเสธความรับผิดชอบ**:
เอกสารนี้ได้รับการแปลโดยใช้บริการแปลภาษา AI [Co-op Translator](https://github.com/Azure/co-op-translator) ขณะที่เราพยายามให้ความถูกต้อง โปรดทราบว่าการแปลโดยอัตโนมัติอาจมีข้อผิดพลาดหรือความไม่ถูกต้อง เอกสารต้นฉบับในภาษาต้นทางควรถูกพิจารณาเป็นแหล่งข้อมูลที่เชื่อถือได้ สำหรับข้อมูลที่สำคัญ แนะนำให้ใช้การแปลโดยมนุษย์มืออาชีพ เราไม่รับผิดชอบต่อความเข้าใจผิดหรือการตีความที่ผิดพลาดที่เกิดขึ้นจากการใช้การแปลนี้
<!-- CO-OP TRANSLATOR DISCLAIMER END -->