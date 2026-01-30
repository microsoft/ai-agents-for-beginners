# AGENTS.md

## ภาพรวมของโปรเจกต์

ที่เก็บข้อมูลนี้ประกอบด้วย "AI Agents for Beginners" - หลักสูตรการศึกษาที่ครอบคลุมทุกสิ่งที่จำเป็นในการสร้าง AI Agents หลักสูตรนี้ประกอบด้วยบทเรียนมากกว่า 15 บทที่ครอบคลุมพื้นฐาน รูปแบบการออกแบบ เฟรมเวิร์ก และการนำ AI Agents ไปใช้งานจริง

**เทคโนโลยีสำคัญ:**
- Python 3.12+
- Jupyter Notebooks สำหรับการเรียนรู้แบบโต้ตอบ
- เฟรมเวิร์ก AI: Semantic Kernel, AutoGen, Microsoft Agent Framework (MAF)
- บริการ Azure AI: Azure AI Foundry, Azure AI Agent Service
- GitHub Models Marketplace (มีระดับฟรีให้บริการ)

**สถาปัตยกรรม:**
- โครงสร้างตามบทเรียน (ไดเรกทอรี 00-15+)
- แต่ละบทเรียนประกอบด้วย: เอกสาร README ตัวอย่างโค้ด (Jupyter notebooks) และภาพประกอบ
- รองรับหลายภาษาโดยใช้ระบบแปลอัตโนมัติ
- มีตัวเลือกเฟรมเวิร์กหลายตัวในแต่ละบทเรียน (Semantic Kernel, AutoGen, Azure AI Agent Service)

## คำสั่งการตั้งค่า

### ข้อกำหนดเบื้องต้น
- Python 3.12 หรือสูงกว่า
- บัญชี GitHub (สำหรับ GitHub Models - ระดับฟรี)
- การสมัครสมาชิก Azure (ไม่บังคับ สำหรับบริการ Azure AI)

### การตั้งค่าเริ่มต้น

1. **โคลนหรือฟอร์กที่เก็บข้อมูล:**
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

สำหรับ **GitHub Models (ฟรี)**:
- `GITHUB_TOKEN` - โทเค็นการเข้าถึงส่วนบุคคลจาก GitHub

สำหรับ **Azure AI Services** (ไม่บังคับ):
- `PROJECT_ENDPOINT` - จุดเชื่อมต่อโครงการ Azure AI Foundry
- `AZURE_OPENAI_API_KEY` - คีย์ API ของ Azure OpenAI
- `AZURE_OPENAI_ENDPOINT` - URL จุดเชื่อมต่อ Azure OpenAI
- `AZURE_OPENAI_CHAT_DEPLOYMENT_NAME` - ชื่อการปรับใช้สำหรับโมเดลแชท
- `AZURE_OPENAI_EMBEDDING_DEPLOYMENT_NAME` - ชื่อการปรับใช้สำหรับ embeddings
- การตั้งค่า Azure เพิ่มเติมตามที่แสดงใน `.env.example`

## เวิร์กโฟลว์การพัฒนา

### การใช้งาน Jupyter Notebooks

แต่ละบทเรียนมี Jupyter notebooks หลายตัวสำหรับเฟรมเวิร์กต่าง ๆ:

1. **เริ่มต้น Jupyter:**
   ```bash
   jupyter notebook
   ```

2. **ไปยังไดเรกทอรีบทเรียน** (เช่น `01-intro-to-ai-agents/code_samples/`)

3. **เปิดและรัน notebooks:**
   - `*-semantic-kernel.ipynb` - ใช้เฟรมเวิร์ก Semantic Kernel
   - `*-autogen.ipynb` - ใช้เฟรมเวิร์ก AutoGen
   - `*-python-agent-framework.ipynb` - ใช้ Microsoft Agent Framework (Python)
   - `*-dotnet-agent-framework.ipynb` - ใช้ Microsoft Agent Framework (.NET)
   - `*-azureaiagent.ipynb` - ใช้ Azure AI Agent Service

### การทำงานกับเฟรมเวิร์กต่าง ๆ

**Semantic Kernel + GitHub Models:**
- มีระดับฟรีให้บริการพร้อมบัญชี GitHub
- เหมาะสำหรับการเรียนรู้และการทดลอง
- รูปแบบไฟล์: `*-semantic-kernel*.ipynb`

**AutoGen + GitHub Models:**
- มีระดับฟรีให้บริการพร้อมบัญชี GitHub
- ความสามารถในการจัดการหลายเอเจนต์
- รูปแบบไฟล์: `*-autogen.ipynb`

**Microsoft Agent Framework (MAF):**
- เฟรมเวิร์กล่าสุดจาก Microsoft
- มีให้บริการใน Python และ .NET
- รูปแบบไฟล์: `*-agent-framework.ipynb`

**Azure AI Agent Service:**
- ต้องการการสมัครสมาชิก Azure
- ฟีเจอร์พร้อมใช้งานในระดับการผลิต
- รูปแบบไฟล์: `*-azureaiagent.ipynb`

## คำแนะนำการทดสอบ

ที่เก็บข้อมูลนี้เป็นที่เก็บการศึกษาโดยมีตัวอย่างโค้ดแทนที่จะเป็นโค้ดสำหรับการผลิตที่มีการทดสอบอัตโนมัติ ในการตรวจสอบการตั้งค่าและการเปลี่ยนแปลงของคุณ:

### การทดสอบด้วยตนเอง

1. **ทดสอบสภาพแวดล้อม Python:**
   ```bash
   python --version  # Should be 3.12+
   pip list | grep -E "(autogen|semantic-kernel|azure-ai)"
   ```

2. **ทดสอบการรัน notebook:**
   ```bash
   # Convert notebook to script and run (tests imports)
   jupyter nbconvert --to script <lesson-folder>/code_samples/<notebook>.ipynb --stdout | python
   ```

3. **ตรวจสอบตัวแปรสภาพแวดล้อม:**
   ```bash
   python -c "import os; from dotenv import load_dotenv; load_dotenv(); print('✓ GITHUB_TOKEN' if os.getenv('GITHUB_TOKEN') else '✗ GITHUB_TOKEN missing')"
   ```

### การรัน notebooks แต่ละตัว

เปิด notebooks ใน Jupyter และรันเซลล์ตามลำดับ แต่ละ notebook มีเนื้อหาในตัวและประกอบด้วย:
- คำสั่งนำเข้า
- การโหลดการตั้งค่า
- การใช้งานเอเจนต์ตัวอย่าง
- ผลลัพธ์ที่คาดหวังในเซลล์ markdown

## รูปแบบโค้ด

### ข้อกำหนด Python

- **เวอร์ชัน Python**: 3.12+
- **รูปแบบโค้ด**: ปฏิบัติตามข้อกำหนดมาตรฐาน Python PEP 8
- **Notebooks**: ใช้เซลล์ markdown ที่ชัดเจนเพื่ออธิบายแนวคิด
- **การนำเข้า**: จัดกลุ่มตามไลบรารีมาตรฐาน ไลบรารีบุคคลที่สาม และการนำเข้าภายใน

### ข้อกำหนด Jupyter Notebook

- รวมเซลล์ markdown ที่อธิบายก่อนเซลล์โค้ด
- เพิ่มตัวอย่างผลลัพธ์ใน notebooks เพื่ออ้างอิง
- ใช้ชื่อตัวแปรที่ชัดเจนที่สอดคล้องกับแนวคิดในบทเรียน
- รักษาลำดับการรัน notebook ให้เป็นเชิงเส้น (เซลล์ 1 → 2 → 3...)

### การจัดระเบียบไฟล์

```
<lesson-number>-<lesson-name>/
├── README.md                     # Lesson documentation
├── code_samples/
│   ├── <number>-semantic-kernel.ipynb
│   ├── <number>-autogen.ipynb
│   ├── <number>-python-agent-framework.ipynb
│   └── <number>-azureaiagent.ipynb
└── images/
    └── *.png
```

## การสร้างและการปรับใช้

### การสร้างเอกสาร

ที่เก็บข้อมูลนี้ใช้ Markdown สำหรับเอกสาร:
- ไฟล์ README.md ในแต่ละโฟลเดอร์บทเรียน
- README.md หลักที่รากของที่เก็บข้อมูล
- ระบบแปลอัตโนมัติผ่าน GitHub Actions

### CI/CD Pipeline

อยู่ใน `.github/workflows/`:

1. **co-op-translator.yml** - การแปลอัตโนมัติเป็นมากกว่า 50 ภาษา
2. **welcome-issue.yml** - ต้อนรับผู้สร้างปัญหาใหม่
3. **welcome-pr.yml** - ต้อนรับผู้ส่งคำขอ pull ใหม่

### การปรับใช้

ที่เก็บข้อมูลนี้เป็นที่เก็บการศึกษา - ไม่มีกระบวนการปรับใช้ ผู้ใช้:
1. ฟอร์กหรือโคลนที่เก็บข้อมูล
2. รัน notebooks ในเครื่องหรือใน GitHub Codespaces
3. เรียนรู้โดยการปรับเปลี่ยนและทดลองกับตัวอย่าง

## แนวทางการส่งคำขอ Pull

### ก่อนการส่ง

1. **ทดสอบการเปลี่ยนแปลงของคุณ:**
   - รัน notebooks ที่ได้รับผลกระทบทั้งหมด
   - ตรวจสอบให้แน่ใจว่าเซลล์ทั้งหมดรันโดยไม่มีข้อผิดพลาด
   - ตรวจสอบว่าผลลัพธ์เหมาะสม

2. **อัปเดตเอกสาร:**
   - อัปเดต README.md หากเพิ่มแนวคิดใหม่
   - เพิ่มความคิดเห็นใน notebooks สำหรับโค้ดที่ซับซ้อน
   - ตรวจสอบให้แน่ใจว่าเซลล์ markdown อธิบายวัตถุประสงค์

3. **การเปลี่ยนแปลงไฟล์:**
   - หลีกเลี่ยงการคอมมิตไฟล์ `.env` (ใช้ `.env.example`)
   - อย่าคอมมิตไดเรกทอรี `venv/` หรือ `__pycache__/`
   - รักษาผลลัพธ์ notebook เมื่อแสดงแนวคิด
   - ลบไฟล์ชั่วคราวและ notebooks สำรอง (`*-backup.ipynb`)

### รูปแบบชื่อ PR

ใช้ชื่อที่อธิบาย:
- `[Lesson-XX] เพิ่มตัวอย่างใหม่สำหรับ <concept>`
- `[Fix] แก้ไขคำผิดใน lesson-XX README`
- `[Update] ปรับปรุงตัวอย่างโค้ดใน lesson-XX`
- `[Docs] อัปเดตคำแนะนำการตั้งค่า`

### การตรวจสอบที่จำเป็น

- Notebooks ควรรันโดยไม่มีข้อผิดพลาด
- ไฟล์ README ควรชัดเจนและถูกต้อง
- ปฏิบัติตามรูปแบบโค้ดที่มีอยู่ในที่เก็บข้อมูล
- รักษาความสอดคล้องกับบทเรียนอื่น ๆ

## หมายเหตุเพิ่มเติม

### สิ่งที่ควรระวัง

1. **เวอร์ชัน Python ไม่ตรงกัน:**
   - ตรวจสอบให้แน่ใจว่าใช้ Python 3.12+
   - ไลบรารีบางตัวอาจไม่ทำงานกับเวอร์ชันเก่า
   - ใช้ `python3 -m venv` เพื่อระบุเวอร์ชัน Python อย่างชัดเจน

2. **ตัวแปรสภาพแวดล้อม:**
   - สร้าง `.env` จาก `.env.example` เสมอ
   - อย่าคอมมิตไฟล์ `.env` (อยู่ใน `.gitignore`)
   - โทเค็น GitHub ต้องมีสิทธิ์ที่เหมาะสม

3. **ความขัดแย้งของแพ็กเกจ:**
   - ใช้สภาพแวดล้อมเสมือนใหม่
   - ติดตั้งจาก `requirements.txt` แทนที่จะเป็นแพ็กเกจแต่ละตัว
   - notebooks บางตัวอาจต้องการแพ็กเกจเพิ่มเติมที่กล่าวถึงในเซลล์ markdown ของพวกเขา

4. **บริการ Azure:**
   - บริการ Azure AI ต้องการการสมัครสมาชิกที่ใช้งานอยู่
   - ฟีเจอร์บางอย่างมีเฉพาะในบางภูมิภาค
   - ข้อจำกัดของระดับฟรีใช้กับ GitHub Models

### เส้นทางการเรียนรู้

ลำดับการเรียนรู้ที่แนะนำผ่านบทเรียน:
1. **00-course-setup** - เริ่มต้นที่นี่สำหรับการตั้งค่าสภาพแวดล้อม
2. **01-intro-to-ai-agents** - ทำความเข้าใจพื้นฐานของ AI agent
3. **02-explore-agentic-frameworks** - เรียนรู้เกี่ยวกับเฟรมเวิร์กต่าง ๆ
4. **03-agentic-design-patterns** - รูปแบบการออกแบบหลัก
5. ดำเนินการต่อผ่านบทเรียนที่มีหมายเลขตามลำดับ

### การเลือกเฟรมเวิร์ก

เลือกเฟรมเวิร์กตามเป้าหมายของคุณ:
- **การเรียนรู้/การสร้างต้นแบบ**: Semantic Kernel + GitHub Models (ฟรี)
- **ระบบหลายเอเจนต์**: AutoGen
- **ฟีเจอร์ล่าสุด**: Microsoft Agent Framework (MAF)
- **การปรับใช้ในระดับการผลิต**: Azure AI Agent Service

### การขอความช่วยเหลือ

- เข้าร่วม [Azure AI Foundry Community Discord](https://aka.ms/ai-agents/discord)
- ทบทวนไฟล์ README ของบทเรียนสำหรับคำแนะนำเฉพาะ
- ตรวจสอบ [README.md หลัก](./README.md) สำหรับภาพรวมของหลักสูตร
- ดู [Course Setup](./00-course-setup/README.md) สำหรับคำแนะนำการตั้งค่าโดยละเอียด

### การมีส่วนร่วม

นี่เป็นโปรเจกต์การศึกษาแบบเปิด ยินดีต้อนรับการมีส่วนร่วม:
- ปรับปรุงตัวอย่างโค้ด
- แก้ไขคำผิดหรือข้อผิดพลาด
- เพิ่มความคิดเห็นที่ชัดเจน
- เสนอหัวข้อบทเรียนใหม่
- แปลเป็นภาษาเพิ่มเติม

ดู [GitHub Issues](https://github.com/microsoft/ai-agents-for-beginners/issues) สำหรับความต้องการปัจจุบัน

## บริบทเฉพาะของโปรเจกต์

### การสนับสนุนหลายภาษา

ที่เก็บข้อมูลนี้ใช้ระบบแปลอัตโนมัติ:
- รองรับมากกว่า 50 ภาษา
- การแปลในไดเรกทอรี `/translations/<lang-code>/`
- การอัปเดตการแปลจัดการโดย GitHub Actions workflow
- ไฟล์ต้นฉบับอยู่ในภาษาอังกฤษที่รากของที่เก็บข้อมูล

### โครงสร้างบทเรียน

แต่ละบทเรียนมีรูปแบบที่สอดคล้องกัน:
1. ภาพตัวอย่างวิดีโอพร้อมลิงก์
2. เนื้อหาบทเรียนที่เขียนไว้ (README.md)
3. ตัวอย่างโค้ดในเฟรมเวิร์กหลายตัว
4. วัตถุประสงค์การเรียนรู้และข้อกำหนดเบื้องต้น
5. ทรัพยากรการเรียนรู้เพิ่มเติมที่ลิงก์ไว้

### การตั้งชื่อตัวอย่างโค้ด

รูปแบบ: `<lesson-number>-<framework-name>.ipynb`
- `04-semantic-kernel.ipynb` - บทเรียนที่ 4, Semantic Kernel
- `07-autogen.ipynb` - บทเรียนที่ 7, AutoGen
- `14-python-agent-framework.ipynb` - บทเรียนที่ 14, MAF Python
- `14-dotnet-agent-framework.ipynb` - บทเรียนที่ 14, MAF .NET

### ไดเรกทอรีพิเศษ

- `translated_images/` - ภาพที่แปลสำหรับการแปล
- `images/` - ภาพต้นฉบับสำหรับเนื้อหาภาษาอังกฤษ
- `.devcontainer/` - การตั้งค่าคอนเทนเนอร์การพัฒนา VS Code
- `.github/` - GitHub Actions workflows และเทมเพลต

### Dependencies

แพ็กเกจสำคัญจาก `requirements.txt`:
- `autogen-agentchat`, `autogen-core`, `autogen-ext` - เฟรมเวิร์ก AutoGen
- `semantic-kernel` - เฟรมเวิร์ก Semantic Kernel
- `agent-framework` - Microsoft Agent Framework
- `azure-ai-inference`, `azure-ai-projects` - บริการ Azure AI
- `azure-search-documents` - การรวม Azure AI Search
- `chromadb` - ฐานข้อมูลเวกเตอร์สำหรับตัวอย่าง RAG
- `chainlit` - เฟรมเวิร์ก UI แชท
- `browser_use` - การทำงานอัตโนมัติของเบราว์เซอร์สำหรับเอเจนต์
- `mcp[cli]` - การสนับสนุน Model Context Protocol
- `mem0ai` - การจัดการหน่วยความจำสำหรับเอเจนต์

---

**ข้อจำกัดความรับผิดชอบ**:  
เอกสารนี้ได้รับการแปลโดยใช้บริการแปลภาษา AI [Co-op Translator](https://github.com/Azure/co-op-translator) แม้ว่าเราจะพยายามให้การแปลมีความถูกต้อง แต่โปรดทราบว่าการแปลอัตโนมัติอาจมีข้อผิดพลาดหรือความไม่ถูกต้อง เอกสารต้นฉบับในภาษาดั้งเดิมควรถือเป็นแหล่งข้อมูลที่เชื่อถือได้ สำหรับข้อมูลที่สำคัญ ขอแนะนำให้ใช้บริการแปลภาษามนุษย์ที่มีความเชี่ยวชาญ เราไม่รับผิดชอบต่อความเข้าใจผิดหรือการตีความผิดที่เกิดจากการใช้การแปลนี้