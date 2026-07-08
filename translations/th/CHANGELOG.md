# ประวัติการเปลี่ยนแปลง

การเปลี่ยนแปลงที่สำคัญทั้งหมดของคอร์ส **AI Agents for Beginners** ได้รับการบันทึกไว้ในไฟล์นี้

## [ยังไม่ปล่อย] — 2026-07-06

การอัปเดตนี้ย้ายคอร์สไปใช้ **Azure OpenAI Responses API** ยกระดับการตั้งชื่อผลิตภัณฑ์เป็นแบบมาตรฐานใน **Microsoft Foundry** และ **Microsoft Agent Framework (MAF)** ยกเลิก GitHub Models อัปเดตเวอร์ชัน SDK และเพิ่มเนื้อหาใหม่เกี่ยวกับโมเดลในเครื่องและการโฮสต์เฟรมเวิร์กอื่น ๆ บน Foundry

### เพิ่มเติม

- **ทักษะการย้ายข้อมูล** — ติดตั้ง Agent Skill [`azure-openai-to-responses`](./.agents/skills/azure-openai-to-responses/SKILL.md) (จาก [Azure-Samples/azure-openai-to-responses](https://github.com/Azure-Samples/azure-openai-to-responses)) ภายใต้ `.agents/skills/` รวมถึงการอ้างอิงและสคริปต์สแกนเนอร์
- **Foundry Local (รันโมเดลในเครื่อง)** — ส่วนใหม่ "ผู้ให้บริการทางเลือก: Foundry Local" ใน [00-course-setup/README.md](./00-course-setup/README.md) ครอบคลุมการติดตั้ง (`winget` / `brew`), `foundry model run`, `foundry-local-sdk` และการเชื่อมต่อ `FoundryLocalManager` กับ Microsoft Agent Framework ผ่าน `OpenAIChatClient`
- **โฮสต์ LangChain / LangGraph agents บน Microsoft Foundry** — ส่วนใหม่ใน [14-microsoft-agent-framework/README.md](./14-microsoft-agent-framework/README.md) พร้อมตัวอย่างรันได้ [14-langchain-hosted-agent.py](../../14-microsoft-agent-framework/code-samples/14-langchain-hosted-agent.py) ใช้ `langchain-azure-ai[hosting]` และ `ResponsesHostServer` (โปรโตคอล `/responses`) อ้างอิงจาก [Microsoft Learn](https://learn.microsoft.com/azure/foundry/how-to/develop/langchain-hosted-agents)
- **Microsoft Project Opal** — ส่วนใหม่ "ตัวอย่างโลกจริง: Microsoft Project Opal" ใน [15-browser-use/README.md](./15-browser-use/README.md) นำเสนอ Opal ในฐานะเอเจนต์ใช้คอมพิวเตอร์องค์กรและจับคู่กับแนวคิดในคอร์ส (คนในวงจร, ความน่าเชื่อถือ/ความปลอดภัย, การวางแผน, ทักษะ)
- **ตัวอย่าง Python ของบทเรียนที่สอง 02** — เพิ่ม [02-python-agent-framework-azure-openai.ipynb](./02-explore-agentic-frameworks/code_samples/02-python-agent-framework-azure-openai.ipynb) (ดูหัวข้อ "เปลี่ยนแปลง" — ย้ายมาจากโน้ตบุ๊ก Semantic Kernel เดิม) และลิงก์ใน README ของบทเรียน
- เพิ่มส่วน **โมเดลและผู้ให้บริการ** ใน [STUDY_GUIDE.md](./STUDY_GUIDE.md)

### เปลี่ยนแปลง

- **Chat Completions → Responses API (Python)** ตัวอย่างที่เรียกใช้โมเดลโดยตรงถูกโยกย้ายจาก Chat Completions ไปใช้ Responses API (`client.responses.create(input=..., store=False)`, `resp.output_text`) โดยใช้ไคลเอนต์ `OpenAI` กับจุดสิ้นสุด Azure OpenAI `/openai/v1/` ที่เสถียร (ไม่มี `api_version`) ตัวอย่างที่ได้รับผลกระทบได้แก่:
  - [06-building-trustworthy-agents/code_samples/06-system-message-framework.ipynb](./06-building-trustworthy-agents/code_samples/06-system-message-framework.ipynb)
  - [06-building-trustworthy-agents/code_samples/06-human-in-the-loop.ipynb](./06-building-trustworthy-agents/code_samples/06-human-in-the-loop.ipynb)
  - [04-tool-use/README.md](./04-tool-use/README.md) — การเดินเรื่องเต็มเกี่ยวกับการเรียกฟังก์ชัน (สคีมาของเครื่องมือปรับเป็นรูปแบบ Responses, ผลลัพธ์ของเครื่องมือคืนค่าเป็น `function_call_output`, `max_output_tokens` ฯลฯ)
- **GitHub Models → Azure OpenAI** GitHub Models ถูกเลิกใช้งาน (ยกเลิกใน **กรกฎาคม 2026**) และไม่รองรับ Responses API เส้นทางโค้ดของ GitHub Models ทั้งหมดถูกแปลงเป็น Azure OpenAI / Microsoft Foundry ในตัวอย่าง Python และ .NET:
  - Python: โน้ตบุ๊กเวิร์กโฟลว์บทเรียน 08 (`01`–`03`), บทเรียน 14 (`14-handoff`, `14-human-loop`, `hotel_booking_workflow_sample.py`)
  - .NET: `01`–`04`, `07`, `08` ไฟล์ `*-dotnet-agent-framework.cs` พร้อมเอกสาร `.md` ประกอบ และโน้ตบุ๊กเวิร์กโฟลว์บทเรียน 08 dotNET/`.md` (`01`–`03`) ปัจจุบันใช้ `AzureOpenAIClient(...).GetOpenAIResponseClient(deployment).CreateAIAgent(...)` ด้วย `AzureCliCredential`
- **Semantic Kernel → Microsoft Agent Framework** โน้ตบุ๊ก `02-semantic-kernel.ipynb` เดิมถูกเขียนใหม่เพื่อใช้ Microsoft Agent Framework กับ Azure OpenAI (Responses API) และเปลี่ยนชื่อเป็น `02-python-agent-framework-azure-openai.ipynb`
- **มาตรฐานเป็น `FoundryChatClient` + `as_agent`** README และโค้ดในโน้ตบุ๊กที่อ้างอิง `AzureAIProjectAgentProvider` ได้มาตรฐานเป็นรูปแบบหลักที่ใช้ในบทเรียน 01 และตัวอย่างของเฟรมเวิร์กเอง: `FoundryChatClient(project_endpoint=..., model=..., credential=AzureCliCredential())` พร้อม `provider.as_agent(...)` อัปเดตใน README และโน้ตบุ๊กของบทเรียน 02–14 (เช่น หน่วยความจำบทเรียน 13, โน้ตบุ๊กบทเรียน 14 ทั้งหมด, `11-agentic-protocols/code_samples/github-mcp/app.py`)
- **การตั้งชื่อผลิตภัณฑ์** เปลี่ยนชื่อในเนื้อหาภาษาอังกฤษทั้งหมด:
  - "Azure AI Foundry" / "Azure AI Studio" → **Microsoft Foundry**
  - "Azure AI Agent Service" → **Microsoft Foundry Agent Service**
  - (ไม่เปลี่ยนแปลง: "Azure OpenAI", "Azure AI Search", "Azure AI Inference" และชื่อตัวแปรใน environment)
- **Dependencies** ([requirements.txt](../../requirements.txt)):
  - กำหนดเวอร์ชัน `agent-framework>=1.10.0`, `agent-framework-foundry>=1.10.0`, `agent-framework-openai>=1.10.0`
  - กำหนดเวอร์ชัน `openai>=1.108.1` (ขั้นต่ำสำหรับ Responses API)
  - ลบ `azure-ai-inference` (ใช้เฉพาะในตัวอย่าง GitHub Models ที่ย้ายแล้ว)
- **การกำหนดค่าสภาพแวดล้อม** ([.env.example](../../.env.example)): ลบตัวแปร GitHub Models (`GITHUB_TOKEN`, `GITHUB_ENDPOINT`, `GITHUB_MODEL_ID`); เพิ่ม `AZURE_OPENAI_ENDPOINT`, `AZURE_OPENAI_DEPLOYMENT`, และตัวเลือก `AZURE_OPENAI_API_KEY`; อัปเดตชื่อเป็น Microsoft Foundry
- **เอกสาร** — อัปเดต [00-course-setup/README.md](./00-course-setup/README.md), [AGENTS.md](./AGENTS.md), [README.md](./README.md) และ [STUDY_GUIDE.md](./STUDY_GUIDE.md) สำหรับสิ่งที่กล่าวมาแล้ว (การตั้งค่าตัวแปร env, โค้ดตรวจสอบ, คำแนะนำผู้ให้บริการ, การตั้งชื่อ)

### ลบออก

- ขั้นตอนการเริ่มต้นใช้งาน GitHub Models และตัวแปรสภาพแวดล้อมจากเอกสารการตั้งค่า (ถูกแทนที่ด้วย Azure OpenAI / Microsoft Foundry)

### ด้านความปลอดภัย / ความเป็นส่วนตัว (การทำความสะอาดการแชร์สาธารณะ)

- ลบผลลัพธ์จากการรัน Jupyter notebook ที่รั่วไหล **Azure subscription ID** จริง, ชื่อ resource-group / resource, และ Bing connection ID รวมทั้ง **เส้นทางไฟล์และชื่อผู้ใช้ในเครื่อง** ของนักพัฒนาใน:
  - `08-multi-agent/code_samples/workflows-agent-framework/dotNET/04.dotnet-agent-framework-workflow-aifoundry-condition.ipynb`
  - `08-multi-agent/code_samples/workflows-agent-framework/python/04.python-agent-framework-workflow-aifoundry-condition.ipynb`
  - `15-browser-use/15-browser-user.ipynb`
- ตรวจสอบว่าไม่มีคีย์ API, โทเค็น, subscription ID หรือเส้นทางส่วนตัวเหลือในเนื้อหาภาษาอังกฤษที่ติดตาม (โทเค็น `GITHUB_TOKEN` ที่เหลือเป็นโทเค็น GitHub Actions ในเวิร์กโฟลว์และ GitHub MCP server PAT ในการตั้งค่าบทเรียน 11 — ทั้งสองเป็นสิ่งถูกต้องและไม่เกี่ยวข้องกับ GitHub Models)

### บันทึกและข้อจำกัดที่ทราบ

- **ไม่ได้รัน/คอมไพล์** ตัวอย่างเป็นการศึกษาอัปเดตเพื่อความถูกต้องของ API/การตั้งชื่อ; ไม่ได้รันกับทรัพยากร Azure จริง และตัวอย่าง .NET ไม่ได้คอมไพล์ในสภาพแวดล้อมนี้ ตรวจสอบกับการติดตั้ง Microsoft Foundry / Azure OpenAI ของคุณเอง
- **การปรับใช้โมเดลต้องรองรับ Responses API** ใช้การปรับใช้เช่น `gpt-4o-mini`, `gpt-4.1` หรือโมเดล `gpt-5.x` โมเดลเก่ารองรับฟังก์ชัน Responses หลักแต่ไม่ใช่ทุกฟีเจอร์
- **เวอร์ชัน agent-framework** ตัวอย่างใช้ MAF ล่าสุด (`>=1.10.0`) การเรียกสร้างเอเจนต์หลักคือ `client.as_agent(...)`; API ได้รับการตรวจสอบกับเอกสารเฟรมเวิร์กที่เผยแพร่และการติดตั้งจริง หากใช้เวอร์ชันอื่นให้ตรวจสอบความพร้อมของเมธอด (`as_agent` เทียบกับ `create_agent`)
- **โน้ตบุ๊กเวิร์กโฟลว์บทเรียน 08 (04)** ยังคงใช้ `AzureAIAgentClient` (จาก `agent-framework-azure-ai`) เพราะใช้ Microsoft Foundry Agent Service กับเครื่องมือโฮสต์ (Bing grounding, code interpreter) ซึ่งใช้ Responses แล้ว
- **การปรับใช้เริ่มต้นของ .NET** ตัวอย่างเวิร์กโฟลว์บทเรียน 08 dotNET สองตัวอย่างที่เคยตั้งค่าโมเดล `gpt-4o` แบบรหัสตายตัว ปัจจุบันตั้งเป็น `AZURE_OPENAI_DEPLOYMENT` (`gpt-4o-mini`) ค่าเริ่มต้น หากตัวอย่างใดต้องใช้การป้อนข้อมูลแบบ multimodal/vision ให้ตั้ง `AZURE_OPENAI_DEPLOYMENT` กับโมเดลที่เหมาะสม
- **Foundry Local** เปิดเผยจุดสิ้นสุด OpenAI-compatible แบบ **Chat Completions** และออกแบบมาสำหรับการพัฒนาในเครื่อง ใช้ Azure OpenAI / Microsoft Foundry สำหรับฟีเจอร์ชุดเต็มของ Responses API

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ปฏิเสธความรับผิดชอบ**:
เอกสารนี้ได้รับการแปลโดยใช้บริการแปลภาษา AI [Co-op Translator](https://github.com/Azure/co-op-translator) ขณะที่เราพยายามให้ความถูกต้อง โปรดทราบว่าการแปลโดยอัตโนมัติอาจมีข้อผิดพลาดหรือความไม่ถูกต้อง เอกสารต้นฉบับในภาษาต้นทางควรถูกพิจารณาเป็นแหล่งข้อมูลที่เชื่อถือได้ สำหรับข้อมูลที่สำคัญ แนะนำให้ใช้การแปลโดยมนุษย์มืออาชีพ เราไม่รับผิดชอบต่อความเข้าใจผิดหรือการตีความที่ผิดพลาดที่เกิดขึ้นจากการใช้การแปลนี้
<!-- CO-OP TRANSLATOR DISCLAIMER END -->