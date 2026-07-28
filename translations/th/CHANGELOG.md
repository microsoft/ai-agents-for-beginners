# ประวัติการเปลี่ยนแปลง

การเปลี่ยนแปลงที่สำคัญทั้งหมดในหลักสูตร **AI Agents for Beginners** ได้ถูกรวบรวมไว้ในไฟล์นี้

## [เผยแพร่แล้ว] — 2026-07-14

การปล่อยเวอร์ชันนี้ย้ายหลักสูตรออกจากโมเดลที่ถูกยกเลิกสองรุ่น กระจายสมุดบันทึก Lesson ที่เหลือไปยัง Microsoft Agent Framework API เวอร์ชันเสถียร และตรวจสอบสมุดบันทึก Python กับการปรับใช้ Microsoft Foundry สด

### การเปลี่ยนแปลง

- **ย้ายออกจากโมเดลที่เลิกใช้ (`gpt-4.1` / `gpt-4.1-mini` → `gpt-5-mini`)** โดยทั้ง `gpt-4.1` และ `gpt-4.1-mini` ได้ถูกเลิกใช้แล้ว (วันที่เกษียณอย่างเป็นทางการ **14 ตุลาคม 2026**) แทนที่การอ้างอิงในหลักสูตรทั้งหมด (เอกสาร, `.env.example`, สมุดบันทึก Python/.NET และตัวอย่าง) ด้วย `gpt-5-mini` ที่ยังไม่ถูกเลิกใช้ ตัวอย่างการกำหนดเส้นทางโมเดลใน Lesson 16 ยังเปรียบเทียบขนาดเล็ก/ใหญ่โดยใช้ `gpt-5-nano` (เล็ก) และ `gpt-5-mini` (ใหญ่) ไฟล์บุคคลที่สามที่แนบมาภายนอก ([15-browser-use/llms.txt](../../15-browser-use/llms.txt)) ข้อความโมเดล GitHub ทางประวัติศาสตร์ และบันทึกความสามารถของสกิล `azure-openai-to-responses` ถูกปล่อยให้ไม่เปลี่ยนแปลงโดยตั้งใจ
- **สมุดบันทึก handoff ของ Lesson 14 ได้ย้ายไปยัง API เวอร์ชันเสถียรแล้ว** [14-handoff.ipynb](./14-microsoft-agent-framework/code-samples/14-handoff.ipynb) ใช้ `agent_framework.orchestrations.HandoffBuilder` กับ `.with_start_agent(...)`, `HandoffAgentUserRequest.create_response(...)`, การสตรีมตาม `event.type` และ `FoundryChatClient` (แทนที่สัญลักษณ์ก่อน 1.0 ที่ถูกลบไปอย่าง `HandoffBuilder`/`ChatMessage`/`RequestInfoEvent`)
- **สมุดบันทึก human-in-the-loop ของ Lesson 14 ได้ย้ายไปยัง API เวอร์ชันเสถียรแล้ว** [14-human-loop.ipynb](./14-microsoft-agent-framework/code-samples/14-human-loop.ipynb) ตอนนี้หยุดชั่วคราวผ่าน `ctx.request_info(...)` + `@response_handler` (แทนที่ `RequestInfoExecutor` / `RequestInfoMessage` / `RequestResponse` ที่ถูกลบไป) สร้างด้วย `WorkflowBuilder(start_executor=..., output_executors=[...])` ขับเคลื่อนผลลัพธ์ที่มีโครงสร้างผ่าน `default_options={"response_format": ...}` และใช้คำตอบแบบสคริปต์ทำให้สมุดบันทึกทำงานแบบไม่ต้องควบคุม (ไม่บล็อกโดย `input()`)
- **การกำหนดค่าสภาพแวดล้อม** ([.env.example](../../.env.example)): เปลี่ยนชื่อการปรับใช้โมเดลเป็น `gpt-5-mini`; เพิ่มตัวแปร `AZURE_AI_SMALL_MODEL` / `AZURE_AI_LARGE_MODEL` (การกำหนดเส้นทาง Lesson 16) และตัวแปรที่เคยขาดหายไป `AZURE_OPENAI_CHAT_DEPLOYMENT_NAME` (การใช้งานเบราว์เซอร์ของ Lesson 15)
- **การพึ่งพา** ([requirements.txt](../../requirements.txt)): กำหนดเวอร์ชัน `agent-framework`, `agent-framework-foundry` และ `agent-framework-openai` เป็น `~=1.10.0` เพื่อให้ชุดที่สอดคล้องกันและตรวจสอบแล้ว (เวอร์ชัน 1.11.0 มีการเปลี่ยนแปลงที่อาจทำให้เกิดปัญหาแบบทดลองบนส่วนที่หลักสูตรนี้ใช้)

### หมายเหตุและข้อจำกัดที่ทราบ

- **ตรวจสอบกับ Microsoft Foundry แบบสด** สมุดบันทึก Python ถูกรันแบบ headless ด้วย `nbconvert` กับโครงการ Microsoft Foundry ที่ใช้ `gpt-5-mini` (และ `gpt-5-nano` สำหรับการกำหนดเส้นทางของ Lesson 16) ปรับใช้โมเดลที่เทียบเท่าที่ยังไม่ถูกเลิกใช้ในโครงการของคุณเอง; สมุดบันทึกจะอ่านชื่อการปรับใช้จาก `AZURE_AI_MODEL_DEPLOYMENT_NAME` / `AZURE_OPENAI_DEPLOYMENT`
- **ยังคงต้องใช้ทรัพยากรเพิ่มเติมในบางบทเรียน** Lesson 05 ต้องใช้ Azure AI Search; workflow การอิง Bing ใน Lesson 08 (`04.python-agent-framework-workflow-aifoundry-condition.ipynb`) ต้องการการเชื่อมต่อ Bing และเครื่องมือที่โฮสต์บน Microsoft Foundry Agent Service; Lesson 13 (Cognee) และ Lesson 17 (Foundry Local) ต้องใช้ runtime ของตัวเอง

## [เผยแพร่แล้ว] — 2026-07-13

การปล่อยเวอร์ชันนี้เพิ่มสองบทเรียนใหม่ที่เสร็จสมบูรณ์ในส่วนการปรับใช้ — ขยายตัวเอเยนต์ไปยัง Microsoft Foundry และลงมาถึงเครื่องเดียว — พร้อมท่อทดสอบควัน การนำทางหลักสูตรที่ปรับปรุง ทักษะผู้เรียนใหม่ และการอัพเดตแบรนด์

### เพิ่มเติม

- **บทเรียน 16 — การปรับใช้เอเยนต์ที่ปรับขนาดได้ด้วย Microsoft Foundry** บทเรียนใหม่ [16-deploying-scalable-agents/README.md](./16-deploying-scalable-agents/README.md) และสมุดบันทึกที่รันได้ [16-python-agent-framework.ipynb](./16-deploying-scalable-agents/code_samples/16-python-agent-framework.ipynb) สร้างเอเยนต์สนับสนุนลูกค้าระดับผลิตจริง (เครื่องมือ, RAG, หน่วยความจำ, การกำหนดเส้นทางโมเดล, การแคชคำตอบ, การอนุมัติของมนุษย์, ประตูประเมิน และการติดตาม OpenTelemetry) พร้อมแผนภาพ Mermaid ของการพัฒนา/ปรับใช้/รันไทม์ การตรวจสอบความรู้ งานมอบหมาย และความท้าทาย
- **บทเรียน 17 — การสร้างเอเยนต์ AI ในเครื่องด้วย Foundry Local และ Qwen** บทเรียนใหม่ [17-creating-local-ai-agents/README.md](./17-creating-local-ai-agents/README.md) และสมุดบันทึก [17-local-agent-foundry-local.ipynb](./17-creating-local-ai-agents/code_samples/17-local-agent-foundry-local.ipynb) สร้างผู้ช่วยวิศวกรรมบนอุปกรณ์เต็มรูปแบบ (เรียกใช้ฟังก์ชัน Qwen ผ่าน Foundry Local, เครื่องมือไฟล์แบบ sandboxed, RAG ท้องถิ่นด้วย Chroma, MCP ท้องถิ่นเป็นทางเลือก) พร้อมแผนภาพเฉพาะทางสำหรับ local-only / local-RAG / การเรียกเครื่องมือ, การตรวจสอบความรู้ งานมอบหมาย และความท้าทาย
- **ท่อทดสอบควัน** เวิร์กโฟลว์ใหม่ [AI Smoke Test](https://github.com/marketplace/actions/ai-smoke-test) [.github/workflows/smoke-test.yml](../../.github/workflows/smoke-test.yml) พร้อมแคตตาล็อกต่อบทเรียนภายใต้ [tests/](./tests/README.md) สำหรับเอเยนต์ที่สามารถปรับใช้ได้ใน Lessons 01, 04, 05 และ 16 พร้อม README ดัชนีที่แมปแต่ละแคตตาล็อกไปยังบทเรียนและชื่อเอเยนต์ที่โฮสต์ Lesson 16 มีส่วน "Validating a Deployed Agent with Smoke Tests"; Lessons 01/04/05 มีการชี้แนะทดสอบควันเป็นทางเลือก
- **ทักษะผู้เรียน** ทักษะเอเยนต์ใหม่ภายใต้ `.agents/skills/`: [deploying-scalable-agents](./.agents/skills/deploying-scalable-agents/SKILL.md), [local-ai-agents](./.agents/skills/local-ai-agents/SKILL.md) (บรรจุคำแนะนำจากบทเรียน 16 และ 17), และ [testing-course-samples](./.agents/skills/testing-course-samples/SKILL.md) (วิธีตรวจสอบตัวอย่างสมุดบันทึกกับ Microsoft Foundry / Azure OpenAI แบบสด)
- **ตัวรันตรวจสอบสมุดบันทึก** ใหม่ [scripts/validate-notebooks.ps1](../../scripts/validate-notebooks.ps1) ที่รันสมุดบันทึก Python ทุกเล่มแบบ headless ด้วย `nbconvert` และแสดงตาราง PASS/FAIL (พร้อม `results.json`) โดยอัตโนมัติตรวจจับ root ของ repo และ Python, ยกเว้นสมุดบันทึกที่ไม่ใช่ส่วนของหลักสูตร (`.venv`, `site-packages`, `translations`, สินทรัพย์เทมเพลตสกิล) และสมุดบันทึก `.NET` ตามค่าเริ่มต้น และรองรับ `-Filter`, `-Timeout`, `-List`, `-IncludeDotnet`, และ `-Python`
- **การนำทางหลักสูตร** เพิ่มลิงก์บทเรียนก่อนหน้า/ถัดไปใน Lessons 11–15 (ที่ก่อนหน้านี้ขาดไป) ทำให้หลักสูตรทั้งหมดเชื่อมต่อ 00 → 18 ในสองทิศทาง
- **รูปขนาดย่อใหม่** รูปขนาดย่อของบทเรียนสำหรับ Lessons 16 และ 17 พร้อมภาพโซเชียลของ repo ที่ปรับปรุงใหม่ [images/repo-thumbnailv3.png](./images/repo-thumbnailv3.png) (โฆษณาบทเรียนใหม่สองบทและ URL `aka.ms/ai-agents-beginners`)
- **การพึ่งพา** ([requirements.txt](../../requirements.txt)): เพิ่ม `foundry-local-sdk` และ `chromadb` สำหรับ Lesson 17

### การเปลี่ยนแปลง

- **ตารางบทเรียนหลัก [README.md](./README.md)**: Lessons 16 และ 17 ตอนนี้ลิงก์สู่เนื้อหาของตนแล้ว (ก่อนหน้านี้เป็น "เร็วๆ นี้"); ภาพ repo เปลี่ยนเป็น `repo-thumbnailv3.png`
- **[STUDY_GUIDE.md](./STUDY_GUIDE.md)**: เพิ่ม Lessons 16 และ 17 เข้าไปในคู่มือบทเรียนทีละบทและเส้นทางการเรียนรู้ และส่วน "Validating Deployed Agents with Smoke Tests"
- **[AGENTS.md](./AGENTS.md)**: อัปเดตจำนวน/คำอธิบายบทเรียน (00–18), เพิ่มส่วนการตรวจสอบทดสอบควัน และเพิ่มตัวอย่างการตั้งชื่อตัวอย่าง Lesson 16/17
- **[18-securing-ai-agents/README.md](./18-securing-ai-agents/README.md)**: "บทเรียนก่อนหน้า" ตอนนี้ชี้ไปยัง Lesson 17 (จากเดิมเป็น Lesson 15) ปิดห่วงโซ่
- **มาตรฐานการอ้างอิงโมเดลไปยังโมเดลที่ไม่ถูกเลิกใช้** แทนที่การอ้างอิงทุกตัว `gpt-4o` / `gpt-4o-mini` ทั่วหลักสูตร (เอกสาร, `.env.example`, สมุดบันทึก Python/.NET และตัวอย่าง) ด้วย `gpt-4.1-mini` — `gpt-4o` (ทุกรุ่น) จะถูกเกษียณในปี 2026 ตัวอย่างการกำหนดเส้นทางโมเดลใน Lesson 16 ยังคงเปรียบเทียบขนาดเล็ก/ใหญ่โดยใช้ `gpt-4.1-mini` (เล็ก) และ `gpt-4.1` (ใหญ่) สมุดบันทึก Python ตอนนี้เลือกโมเดลจากตัวแปรสภาพแวดล้อม (`AZURE_AI_MODEL_DEPLOYMENT_NAME` / `AZURE_OPENAI_DEPLOYMENT`) แทนการเขียนชื่อโมเดลไว้ตรงๆ

### หมายเหตุและข้อจำกัดที่ทราบ

- **ไม่ได้รันกับ Azure สด** สมุดบันทึกบทเรียนใหม่เป็นตัวอย่างเพื่อการศึกษา; รันและตรวจสอบกับการตั้งค่า Microsoft Foundry / Foundry Local ของคุณเอง เวิร์กโฟลว์ทดสอบควันต้องการให้คุณปรับใช้เอเยนต์ของบทเรียนและกำหนดค่า Azure OIDC secrets (`AZURE_CLIENT_ID`, `AZURE_TENANT_ID`, `AZURE_SUBSCRIPTION_ID`) โดยมีบทบาท **Azure AI User** ที่ขอบเขตโปรเจกต์ Foundry
- **Lesson 17 เป็นเฉพาะในเครื่อง** ไม่มีปลายทาง Foundry Responses ดังนั้นการกระทำทดสอบควันจึงไม่ใช้กับบทเรียนนี้; ตรวจสอบโดยรันสมุดบันทึกบนเครื่องของคุณเอง

## [เผยแพร่แล้ว] — 2026-07-06

การปล่อยเวอร์ชันนี้ย้ายหลักสูตรเข้าสู่ **Azure OpenAI Responses API** มาตรฐานการตั้งชื่อผลิตภัณฑ์เกี่ยวกับ **Microsoft Foundry** และ **Microsoft Agent Framework (MAF)** เลิกใช้ GitHub Models อัปเดตเวอร์ชัน SDK และเพิ่มเนื้อหาใหม่เกี่ยวกับโมเดลท้องถิ่นและการโฮสต์เฟรมเวิร์กอื่นบน Foundry

### เพิ่มเติม

- **ทักษะการย้ายระบบ** — ติดตั้ง Agent Skill [`azure-openai-to-responses`](./.agents/skills/azure-openai-to-responses/SKILL.md) (จาก [Azure-Samples/azure-openai-to-responses](https://github.com/Azure-Samples/azure-openai-to-responses)) ใต้ `.agents/skills/` รวมทั้งการอ้างอิงและสคริปต์สแกนเนอร์
- **Foundry Local (รันโมเดลบนอุปกรณ์)** — ส่วนใหม่ "Alternative Provider: Foundry Local" ใน [00-course-setup/README.md](./00-course-setup/README.md) ครอบคลุมการติดตั้ง (`winget` / `brew`), `foundry model run`, `foundry-local-sdk` และการเชื่อมต่อ `FoundryLocalManager` เข้ากับ Microsoft Agent Framework ผ่าน `OpenAIChatClient`
- **โฮสต์เอเยนต์ LangChain / LangGraph บน Microsoft Foundry** — ส่วนใหม่ใน [14-microsoft-agent-framework/README.md](./14-microsoft-agent-framework/README.md) พร้อมตัวอย่างที่รันได้ [14-langchain-hosted-agent.py](../../14-microsoft-agent-framework/code-samples/14-langchain-hosted-agent.py) ที่ใช้ `langchain-azure-ai[hosting]` และ `ResponsesHostServer` (โปรโตคอล `/responses`), อ้างอิงจาก [Microsoft Learn](https://learn.microsoft.com/azure/foundry/how-to/develop/langchain-hosted-agents)
- **Microsoft Project Opal** — ส่วนใหม่ "ตัวอย่างจริงในโลกจริง: Microsoft Project Opal" ใน [15-browser-use/README.md](./15-browser-use/README.md) ที่กรอบ Opal เป็นเอเยนต์ใช้คอมพิวเตอร์องค์กรและเชื่อมโยงกับแนวคิดของหลักสูตร (human-in-the-loop, ความไว้วางใจ/ความปลอดภัย, การวางแผน, ทักษะ)
- **ตัวอย่าง Python Lesson 02 ตัวที่สอง** — เพิ่ม [02-python-agent-framework-azure-openai.ipynb](./02-explore-agentic-frameworks/code_samples/02-python-agent-framework-azure-openai.ipynb) (ดู "เปลี่ยนแปลง" — ย้ายมาจากสมุดบันทึก Semantic Kernel เดิม) และลิงก์ใน README บทเรียน
- เพิ่มส่วน Models and Providers ใน [STUDY_GUIDE.md](./STUDY_GUIDE.md)

### การเปลี่ยนแปลง

- **Chat Completions → Responses API (Python)** ตัวอย่างที่เรียกโมเดลโดยตรงถูกย้ายจาก Chat Completions ไปยัง Responses API (`client.responses.create(input=..., store=False)`, `resp.output_text`) โดยใช้ไคลเอนต์ `OpenAI` กับจุดสิ้นสุด Azure OpenAI `/openai/v1/` เวอร์ชันเสถียร (ไม่มี `api_version`) ตัวอย่างที่ได้รับผลกระทบได้แก่:
  - [06-building-trustworthy-agents/code_samples/06-system-message-framework.ipynb](./06-building-trustworthy-agents/code_samples/06-system-message-framework.ipynb)
  - [06-building-trustworthy-agents/code_samples/06-human-in-the-loop.ipynb](./06-building-trustworthy-agents/code_samples/06-human-in-the-loop.ipynb)
  - [04-tool-use/README.md](./04-tool-use/README.md) — เดินผ่านการเรียกใช้ฟังก์ชันอย่างเต็มรูปแบบ (โครงสร้างเครื่องมือแบนลงเป็นรูปแบบ Responses, ผลลัพธ์เครื่องมือส่งคืนเป็น `function_call_output`, `max_output_tokens`, ฯลฯ)

- **โมเดล GitHub → Azure OpenAI.** โมเดล GitHub ถูกเลิกใช้แล้ว (เลิกใช้ **กรกฎาคม 2026**) และไม่รองรับ Responses API เส้นทางโค้ดของโมเดล GitHub ทั้งหมดถูกแปลงเป็น Azure OpenAI / Microsoft Foundry ในตัวอย่าง Python และ .NET:
  - Python: โน้ตบุ๊กเวิร์กโฟลว์บทเรียน 08 (`01`–`03`), บทเรียน 14 (`14-handoff`, `14-human-loop`, `hotel_booking_workflow_sample.py`).
  - .NET: `01`–`04`, `07`, `08` `*-dotnet-agent-framework.cs` + เอกสาร `.md` ที่เกี่ยวข้อง และโน้ตบุ๊ก/`.md` เวิร์กโฟลว์บทเรียน 08 dotNET (`01`–`03`) ตอนนี้ใช้ `AzureOpenAIClient(...).GetOpenAIResponseClient(deployment).CreateAIAgent(...)` กับ `AzureCliCredential`
- **Semantic Kernel → Microsoft Agent Framework.** `02-semantic-kernel.ipynb` เดิมถูกเขียนใหม่ให้ใช้ Microsoft Agent Framework กับ Azure OpenAI (Responses API) และเปลี่ยนชื่อเป็น `02-python-agent-framework-azure-openai.ipynb`
- **มาตรฐานเป็น `FoundryChatClient` + `as_agent`.** README และโค้ดในโน้ตบุ๊กที่อ้างอิง `AzureAIProjectAgentProvider` ได้มาตรฐานตามรูปแบบหลักที่ใช้ในบทเรียน 01 และตัวอย่างของเฟรมเวิร์กเอง: `FoundryChatClient(project_endpoint=..., model=..., credential=AzureCliCredential())` พร้อม `provider.as_agent(...)` ปรับปรุงใน README และโน้ตบุ๊กบทเรียน 02–14 (เช่น memory ของบทเรียน 13, โน้ตบุ๊กทั้งหมดของบทเรียน 14, `11-agentic-protocols/code_samples/github-mcp/app.py`)
- **การตั้งชื่อผลิตภัณฑ์.** เปลี่ยนชื่อในเนื้อหาภาษาอังกฤษทั้งหมด:
  - "Azure AI Foundry" / "Azure AI Studio" → **Microsoft Foundry**
  - "Azure AI Agent Service" → **Microsoft Foundry Agent Service**
  - (ไม่เปลี่ยน: "Azure OpenAI", "Azure AI Search", "Azure AI Inference", และชื่อตัวแปรสภาพแวดล้อม)
- **การพึ่งพา** ([requirements.txt](../../requirements.txt)):
  - กำหนดเวอร์ชัน `agent-framework>=1.10.0`, `agent-framework-foundry>=1.10.0`, `agent-framework-openai>=1.10.0`
  - กำหนดเวอร์ชัน `openai>=1.108.1` (ขั้นต่ำสำหรับ Responses API)
  - ลบ `azure-ai-inference` (เคยใช้แค่กับตัวอย่างโมเดล GitHub ที่ย้ายมา)
- **การตั้งค่าสภาพแวดล้อม** ([.env.example](../../.env.example)): ลบตัวแปรโมเดล GitHub (`GITHUB_TOKEN`, `GITHUB_ENDPOINT`, `GITHUB_MODEL_ID`); เพิ่ม `AZURE_OPENAI_ENDPOINT`, `AZURE_OPENAI_DEPLOYMENT` และ `AZURE_OPENAI_API_KEY` แบบเลือกได้; ปรับการตั้งชื่อเป็น Microsoft Foundry
- **เอกสาร** — ปรับปรุง [00-course-setup/README.md](./00-course-setup/README.md), [AGENTS.md](./AGENTS.md), [README.md](./README.md), และ [STUDY_GUIDE.md](./STUDY_GUIDE.md) สำหรับสิ่งดังกล่าวข้างต้น (ตั้งค่าสตริงตัวแปรสภาพแวดล้อม, โค้ดตรวจสอบ, คำแนะนำผู้ให้บริการ, การตั้งชื่อ)

### ถูกลบออก

- ขั้นตอนการเริ่มใช้งานโมเดล GitHub และตัวแปรสภาพแวดล้อมจากเอกสารการตั้งค่า (ถูกแทนที่ด้วย Azure OpenAI / Microsoft Foundry)

### ความปลอดภัย / ความเป็นส่วนตัว (ล้างข้อมูลก่อนเผยแพร่สาธารณะ)

- ลบผลลัพธ์การรันโน้ตบุ๊ก Jupyter ที่รั่วไหล **Azure subscription ID** จริง, ชื่อ resource-group / resource, และ Bing connection ID รวมถึง **เส้นทางไฟล์ในเครื่องและชื่อผู้ใช้ของนักพัฒนา** ใน:
  - `08-multi-agent/code_samples/workflows-agent-framework/dotNET/04.dotnet-agent-framework-workflow-aifoundry-condition.ipynb`
  - `08-multi-agent/code_samples/workflows-agent-framework/python/04.python-agent-framework-workflow-aifoundry-condition.ipynb`
  - `15-browser-use/15-browser-user.ipynb`
- ตรวจสอบว่าปลอด API key, token, subscription ID, หรือเส้นทางส่วนตัวที่หลงเหลือในเนื้อหาภาษาอังกฤษที่ติดตาม (การอ้างอิง `GITHUB_TOKEN` ที่เหลือคือ token ของ GitHub Actions ใน workflows และ PAT ของ GitHub MCP server ในการตั้งค่าบทเรียน 11 — ซึ่งถูกต้องและไม่ได้เกี่ยวข้องกับโมเดล GitHub)

### หมายเหตุและข้อจำกัดที่ทราบ

- **ไม่ได้รัน/คอมไพล์จริง.** ตัวอย่างเหล่านี้เป็นการศึกษาที่อัปเดตให้ถูกต้องตาม API/การตั้งชื่อ; ไม่ได้รันกับ Azure จริง และตัวอย่าง .NET ไม่ได้ถูกคอมไพล์ในสภาพแวดล้อมนี้ ตรวจสอบกับการปรับใช้ Microsoft Foundry / Azure OpenAI ของคุณเอง
- **การปรับใช้โมเดลต้องรองรับ Responses API.** ใช้การปรับใช้เช่น `gpt-4.1-mini`, `gpt-4.1`, หรือโมเดล `gpt-5.x` โมเดลเก่าๆ รองรับฟังก์ชัน Responses หลักแต่ไม่รองรับทุกฟีเจอร์
- **เวอร์ชัน agent-framework.** ตัวอย่างกำหนดเป้าหมาย MAF ล่าสุด (`>=1.10.0`) คำสั่งสร้างเอเจนต์ที่เป็นหลักคือ `client.as_agent(...)`; API ได้รับการตรวจสอบกับเอกสารที่เผยแพร่ของเฟรมเวิร์กและ build ที่ติดตั้ง หากกำหนดเวอร์ชันต่างออกไป โปรดยืนยันว่ามีวิธีการ (`as_agent` กับ `create_agent`)
- **โน้ตบุ๊กเวิร์กโฟลว์บทเรียน 08 เล่ม 04** ยังคงใช้ `AzureAIAgentClient` (จาก `agent-framework-azure-ai`) เพราะใช้เครื่องมือที่โฮสต์บน Microsoft Foundry Agent Service (Bing grounding, code interpreter); ซึ่งใช้ Responses API อยู่แล้ว
- **การปรับใช้เริ่มต้นสำหรับ .NET.** ตัวอย่างเวิร์กโฟลว์ dotNET บทเรียน 08 สองตัวอย่างก่อนหน้าที่กำหนดโมเดลแบบฮาร์ดโค้ดได้เปลี่ยนเป็นค่าเริ่มต้นเป็น `AZURE_OPENAI_DEPLOYMENT` (`gpt-4.1-mini`) หากตัวอย่างต้องการ multimodal/vision input ให้ตั้ง `AZURE_OPENAI_DEPLOYMENT` เป็นโมเดลที่เหมาะสม
- **Foundry Local** เปิดใช้ endpoint **Chat Completions** ที่เข้ากันได้กับ OpenAI และเหมาะสำหรับการพัฒนาท้องถิ่น; ให้ใช้ Azure OpenAI / Microsoft Foundry สำหรับชุดฟีเจอร์ Responses API เต็มรูปแบบ

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ปฏิเสธความรับผิดชอบ**:
เอกสารนี้ได้รับการแปลโดยใช้บริการแปลภาษา AI [Co-op Translator](https://github.com/Azure/co-op-translator) ขณะที่เราพยายามให้ความถูกต้อง โปรดทราบว่าการแปลโดยอัตโนมัติอาจมีข้อผิดพลาดหรือความไม่ถูกต้อง เอกสารต้นฉบับในภาษาต้นทางควรถูกพิจารณาเป็นแหล่งข้อมูลที่เชื่อถือได้ สำหรับข้อมูลที่สำคัญ แนะนำให้ใช้การแปลโดยมนุษย์มืออาชีพ เราไม่รับผิดชอบต่อความเข้าใจผิดหรือการตีความที่ผิดพลาดที่เกิดขึ้นจากการใช้การแปลนี้
<!-- CO-OP TRANSLATOR DISCLAIMER END -->