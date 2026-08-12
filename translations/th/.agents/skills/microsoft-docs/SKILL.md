---
name: microsoft-docs
description: ค้นหาเอกสารอย่างเป็นทางการของ Microsoft เพื่อค้นหาแนวคิด บทแนะนำ และตัวอย่างโค้ดสำหรับ
  Azure, .NET, Agent Framework, Aspire, VS Code, GitHub และอื่นๆ ใช้ Microsoft Learn
  MCP เป็นค่าเริ่มต้น โดยใช้ Context7 และ Aspire MCP สำหรับเนื้อหาที่อยู่นอก learn.microsoft.com.
---
# Microsoft Docs

ทักษะการค้นคว้าสำหรับระบบนิเวศเทคโนโลยีของ Microsoft ครอบคลุม learn.microsoft.com และเอกสารที่อยู่นอกเว็บไซต์นั้น (VS Code, GitHub, Aspire, ที่เก็บ Agent Framework).

---

## Default: Microsoft Learn MCP

ใช้เครื่องมือเหล่านี้สำหรับ **ทุกอย่างบน learn.microsoft.com** — Azure, .NET, M365, Power Platform, Agent Framework, Semantic Kernel, Windows และอื่นๆ นี่คือเครื่องมือหลักสำหรับคำถามเกี่ยวกับเอกสาร Microsoft ส่วนใหญ่

| Tool | Purpose |
|------|---------|
| `microsoft_docs_search` | ค้นหา learn.microsoft.com — แนวคิด, คำแนะนำ, แบบฝึกหัด, การกำหนดค่า |
| `microsoft_code_sample_search` | ค้นหาตัวอย่างโค้ดที่ใช้งานได้จากเอกสาร Learn ให้ส่ง `language` (`python`, `csharp`, ฯลฯ) เพื่อผลลัพธ์ที่ดีที่สุด |
| `microsoft_docs_fetch` | ดึงเนื้อหาเต็มหน้าจาก URL ที่ระบุ (เมื่อข้อความย่อจากการค้นหาไม่เพียงพอ) |

ใช้ `microsoft_docs_fetch` หลังการค้นหาเมื่อคุณต้องการบทแนะนำครบถ้วน ตัวเลือกการกำหนดค่าทั้งหมด หรือตอนที่ข้อความย่อจากการค้นหาถูกตัดทอนไป

---

## Exceptions: When to Use Other Tools

หมวดหมู่ต่อไปนี้อยู่ **นอก** learn.microsoft.com ให้ใช้เครื่องมือที่ระบุแทน

### .NET Aspire — Use Aspire MCP Server (preferred) or Context7

เอกสาร Aspire อยู่บน **aspire.dev** ไม่ใช่ Learn เครื่องมือที่ดีที่สุดขึ้นอยู่กับเวอร์ชัน Aspire CLI ของคุณ:

**CLI 13.2+** (แนะนำ) — เซิร์ฟเวอร์ Aspire MCP มีเครื่องมือค้นหาเอกสารในตัว:

| MCP Tool | Description |
|----------|-------------|
| `list_docs` | แสดงรายการเอกสารทั้งหมดที่มีจาก aspire.dev |
| `search_docs` | การค้นหาเชิงเล็กซิคอลแบบถ่วงน้ำหนักผ่านเนื้อหา aspire.dev |
| `get_doc` | ดึงเอกสารเฉพาะโดยใช้ slug |

ฟีเจอร์เหล่านี้มาพร้อมกับ Aspire CLI 13.2 ([PR #14028](https://github.com/dotnet/aspire/pull/14028)). ในการอัปเดต: `aspire update --self --channel daily`. อ้างอิง: https://davidpine.dev/posts/aspire-docs-mcp-tools/

**CLI 13.1** — เซิร์ฟเวอร์ MCP มีการค้นหาอินทิเกรชัน (`list_integrations`, `get_integration_docs`) แต่ **ไม่มี** การค้นหาเอกสาร ให้ถอยกลับไปใช้ Context7:

| Library ID | Use for |
|---|---|
| `/microsoft/aspire.dev` | หลัก — คำแนะนำ, การผนวกรวม, เอกสารอ้างอิง CLI, การปรับใช้ |
| `/dotnet/aspire` | แหล่งรันไทม์ — โครงสร้างภายใน API, รายละเอียดการใช้งาน |
| `/communitytoolkit/aspire` | การผนวกรวมของชุมชน — Go, Java, Node.js, Ollama |

### VS Code — Use Context7

เอกสาร VS Code อยู่บน **code.visualstudio.com** ไม่ใช่ Learn

| Library ID | Use for |
|---|---|
| `/websites/code_visualstudio` | เอกสารผู้ใช้ — การตั้งค่า, คุณสมบัติ, การดีบัก, การพัฒนาแบบระยะไกล |
| `/websites/code_visualstudio_api` | Extension API — webviews, TreeViews, คำสั่ง, จุดการขยาย |

### GitHub — Use Context7

เอกสาร GitHub อยู่บน **docs.github.com** และ **cli.github.com**

| Library ID | Use for |
|---|---|
| `/websites/github_en` | Actions, API, ที่เก็บ, ความปลอดภัย, การจัดการ, Copilot |
| `/websites/cli_github` | คำสั่งและแฟล็กของ GitHub CLI (`gh`) |

### Agent Framework — Use Learn MCP + Context7

บทแนะนำ Agent Framework อยู่บน learn.microsoft.com (ใช้ `microsoft_docs_search`) แต่ที่เก็บ **GitHub repo** มีรายละเอียดระดับ API ที่มักล้ำหน้ากว่าเอกสารที่เผยแพร่อยู่ — โดยเฉพาะ DevUI REST API reference, ตัวเลือก CLI, และการรวมกับ .NET

| Library ID | Use for |
|---|---|
| `/websites/learn_microsoft_en-us_agent-framework` | บทแนะนำ — คำแนะนำ DevUI, การติดตาม, การประสานงานเวิร์กโฟลว์ |
| `/microsoft/agent-framework` | รายละเอียด API — จุดสิ้นสุด DevUI REST, แฟล็ก CLI, การยืนยันตัวตน, .NET `AddDevUI`/`MapDevUI` |

**DevUI tip:** ค้นหาแหล่งที่มาบนเว็บไซต์ Learn สำหรับคำแนะนำแบบ how-to แล้วดูแหล่งที่มาจาก repo สำหรับรายละเอียดระดับ API (schemas ของ endpoint, การกำหนดค่า proxy, โทเค็นการยืนยันตัวตน)

---

## Context7 Setup

สำหรับการค้นหา Context7 ใดๆ ให้ระบุ library ID ก่อน (ครั้งเดียวต่อเซสชัน):

1. Call `mcp_context7_resolve-library-id` with the technology name
2. Call `mcp_context7_query-docs` with the returned library ID and a specific query

---

## Writing Effective Queries

การระบุให้ชัดเจน — รวมเวอร์ชัน เจตนา และภาษา:

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

Include context:
- **Version** when relevant (`.NET 8`, `Aspire 13`, `VS Code 1.96`)
- **Task intent** (`quickstart`, `tutorial`, `overview`, `limits`, `API reference`)
- **Language** for polyglot docs (`Python`, `TypeScript`, `C#`)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
ข้อปฏิเสธ:
เอกสารฉบับนี้ได้รับการแปลโดยใช้บริการแปลด้วยปัญญาประดิษฐ์ [Co-op Translator](https://github.com/Azure/co-op-translator). แม้ว่าเราจะพยายามให้การแปลมีความถูกต้อง โปรดทราบว่าการแปลโดยอัตโนมัติอาจมีข้อผิดพลาดหรือความไม่แม่นยำ เอกสารต้นฉบับในภาษาเดิมควรถือเป็นแหล่งข้อมูลที่เชื่อถือได้ สำหรับข้อมูลที่มีความสำคัญ ขอแนะนำให้ใช้การแปลโดยนักแปลมนุษย์มืออาชีพ เราไม่รับผิดชอบต่อความเข้าใจผิดหรือการตีความผิดใด ๆ ที่เกิดจากการใช้การแปลฉบับนี้
<!-- CO-OP TRANSLATOR DISCLAIMER END -->