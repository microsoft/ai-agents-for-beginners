---
name: microsoft-docs
description: ค้นหาข้อมูลในเอกสารอย่างเป็นทางการของ Microsoft เพื่อค้นหาคอนเซปต์ บทเรียน
  และตัวอย่างโค้ดในหัวข้อต่างๆ เช่น Azure, .NET, Agent Framework, Aspire, VS Code,
  GitHub และอื่นๆ ใช้ Microsoft Learn MCP เป็นค่าเริ่มต้น พร้อมทั้ง Context7 และ Aspire
  MCP สำหรับเนื้อหาที่อยู่นอก learn.microsoft.com
---
# เอกสาร Microsoft

ทักษะการค้นคว้าสำหรับระบบนิเวศเทคโนโลยีของ Microsoft ครอบคลุม learn.microsoft.com และเอกสารที่อยู่นอกเหนือจากนั้น (VS Code, GitHub, Aspire, Agent Framework repos)

---

## ค่าปริยาย: Microsoft Learn MCP

ใช้เครื่องมือเหล่านี้สำหรับ **ทุกอย่างบน learn.microsoft.com** — Azure, .NET, M365, Power Platform, Agent Framework, Semantic Kernel, Windows และอื่นๆ นี่คือเครื่องมือหลักสำหรับคำค้นสอบถามเอกสาร Microsoft ส่วนใหญ่

| เครื่องมือ | วัตถุประสงค์ |
|------|---------|
| `microsoft_docs_search` | ค้นหา learn.microsoft.com — แนวคิด, คู่มือ, คำแนะนำ, การตั้งค่า |
| `microsoft_code_sample_search` | ค้นหาโค้ดตัวอย่างที่ใช้งานได้จากเอกสาร Learn ส่ง `language` (`python`, `csharp`, ฯลฯ) เพื่อผลลัพธ์ที่ดีที่สุด |
| `microsoft_docs_fetch` | รับเนื้อหาหน้าฉบับเต็มจาก URL เฉพาะ (เมื่อย่อหน้าในการค้นหาไม่เพียงพอ) |

ใช้ `microsoft_docs_fetch` หลังการค้นหาเมื่อคุณต้องการบทเรียนครบถ้วน ตัวเลือกการตั้งค่าทั้งหมด หรือเมื่อย่อหน้าการค้นหาถูกตัดทอน

---

## ข้อยกเว้น: เมื่อใช้เครื่องมืออื่น

หมวดหมู่ต่อไปนี้อยู่นอกเหนือ **learn.microsoft.com** โปรดใช้เครื่องมือที่ระบุแทน

### Aspire — ใช้ Aspire MCP Server (แนะนำ) หรือ Context7

เอกสาร Aspire อยู่บน **aspire.dev** ไม่ใช่ Learn เครื่องมือที่ดีที่สุดขึ้นกับเวอร์ชัน Aspire CLI ของคุณ:

**CLI 13.2+** (แนะนำ) — เซิร์ฟเวอร์ Aspire MCP มีเครื่องมือค้นหาเอกสารในตัว:

| เครื่องมือ MCP | คำอธิบาย |
|----------|-------------|
| `list_docs` | แสดงรายการเอกสารทั้งหมดที่มีจาก aspire.dev |
| `search_docs` | ค้นหาคำแบบถ่วงน้ำหนักในเนื้อหา aspire.dev |
| `get_doc` | ดึงเอกสารเฉพาะตาม slug |

เครื่องมือเหล่านี้มาพร้อมกับ Aspire CLI 13.2 ([PR #14028](https://github.com/microsoft/aspire/pull/14028)) ในการอัปเดต: `aspire update --self --channel daily`

**CLI 13.1** — เซิร์ฟเวอร์ MCP ให้บริการการค้นหาอินทิเกรชัน (`list_integrations`, `get_integration_docs`) แต่ **ไม่มี** การค้นหาเอกสาร ให้กลับไปใช้ Context7 แทน:

| ID ไลบรารี | ใช้สำหรับ |
|---|---|
| `/microsoft/aspire.dev` | หลัก — คู่มือ, การรวมระบบ, อ้างอิง CLI, การปรับใช้ |
| `/microsoft/aspire` | แหล่งรันไทม์ — API ภายใน, รายละเอียดการใช้งาน |
| `/communitytoolkit/aspire` | การรวมระบบจากชุมชน — Go, Java, Node.js, Ollama |

### VS Code — ใช้ Context7

เอกสาร VS Code อยู่บน **code.visualstudio.com** ไม่ใช่ Learn

| ID ไลบรารี | ใช้สำหรับ |
|---|---|
| `/websites/code_visualstudio` | เอกสารผู้ใช้ — การตั้งค่า, ฟีเจอร์, ดีบัก, การพัฒนาระยะไกล |
| `/websites/code_visualstudio_api` | Extension API — เว็บวิว, TreeViews, คำสั่ง, จุดเชื่อมต่อ |

### GitHub — ใช้ Context7

เอกสาร GitHub อยู่บน **docs.github.com** และ **cli.github.com**

| ID ไลบรารี | ใช้สำหรับ |
|---|---|
| `/websites/github_en` | Actions, API, repo, ความปลอดภัย, แอดมิน, Copilot |
| `/websites/cli_github` | คำสั่งและแฟล็ก GitHub CLI (`gh`) |

### Agent Framework — ใช้ Learn MCP + Context7

บทเรียน Agent Framework อยู่ใน learn.microsoft.com (ใช้ `microsoft_docs_search`) แต่ **GitHub repo** มีรายละเอียด API ที่มักจะล้ำหน้ากว่าเอกสารที่เผยแพร่ — โดยเฉพาะ DevUI REST API อ้างอิง, ตัวเลือก CLI, และ การรวม .NET

| ID ไลบรารี | ใช้สำหรับ |
|---|---|
| `/websites/learn_microsoft_en-us_agent-framework` | บทเรียน — คู่มือ DevUI, การติดตาม, การประสานงานเวิร์กโฟลว์ |
| `/microsoft/agent-framework` | รายละเอียด API — DevUI REST endpoints, แฟล็ก CLI, การยืนยันตัวตน, .NET `AddDevUI`/`MapDevUI` |

**เคล็ดลับ DevUI:** คิวรีแหล่ง Learn สำหรับคู่มือวิธีใช้ แล้วคิวรีแหล่ง repo สำหรับรายละเอียดระดับ API (สคีมา endpoint, การตั้งพร็อกซี, โทเค็นการยืนยัน)

---

## การตั้งค่า Context7

สำหรับคำถาม Context7 ใดๆ ให้แก้ไข ID ไลบรารีก่อน (ครั้งเดียวต่อเซสชัน):

1. เรียก `mcp_context7_resolve-library-id` พร้อมชื่อเทคโนโลยี
2. เรียก `mcp_context7_query-docs` ด้วย ID ไลบรารีที่ได้และคำถามเจาะจง

---

## การเขียนคำถามให้ได้ผล

ระบุให้ชัดเจน — รวมเวอร์ชัน, ความตั้งใจ, และภาษา:

```
# ❌ Too broad
"Azure Functions"
"agent framework"

# ✅ Specific
"Azure Functions Python v2 programming model"
"Cosmos DB partition key design best practices"
"GitHub Actions workflow_dispatch inputs matrix strategy"
"Aspire AddUvicornApp Python FastAPI integration"
"DevUI serve agents tracing OpenTelemetry directory discovery"
"Agent Framework workflow conditional edges branching handoff"
```

รวมบริบท:
- **เวอร์ชัน** เมื่อเกี่ยวข้อง (`.NET 8`, `Aspire 13`, `VS Code 1.96`)
- **ความตั้งใจงาน** (`quickstart`, `tutorial`, `overview`, `limits`, `API reference`)
- **ภาษา** สำหรับเอกสารหลายภาษา (`Python`, `TypeScript`, `C#`)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ปฏิเสธความรับผิดชอบ**:
เอกสารนี้ได้รับการแปลโดยใช้บริการแปลภาษา AI [Co-op Translator](https://github.com/Azure/co-op-translator) ขณะที่เราพยายามให้ความถูกต้อง โปรดทราบว่าการแปลโดยอัตโนมัติอาจมีข้อผิดพลาดหรือความไม่ถูกต้อง เอกสารต้นฉบับในภาษาต้นทางควรถูกพิจารณาเป็นแหล่งข้อมูลที่เชื่อถือได้ สำหรับข้อมูลที่สำคัญ แนะนำให้ใช้การแปลโดยมนุษย์มืออาชีพ เราไม่รับผิดชอบต่อความเข้าใจผิดหรือการตีความที่ผิดพลาดที่เกิดขึ้นจากการใช้การแปลนี้
<!-- CO-OP TRANSLATOR DISCLAIMER END -->