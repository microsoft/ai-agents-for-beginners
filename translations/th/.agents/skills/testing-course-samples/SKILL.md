---
name: testing-course-samples
description: ใช้เมื่อต้องการตรวจสอบความถูกต้อง ทดสอบ ทดสอบแบบ smoke-test หรือรันโน้ตบุ๊กและตัวอย่างโค้ดของคอร์สกับการตั้งค่า
  Microsoft Foundry / Azure OpenAI ที่ใช้งานจริง ครอบคลุมการตั้งค่าสภาพแวดล้อม (.env,
  az login, แพ็กเกจ), ตัวรัน scripts/validate-notebooks.ps1, การตีความผลลัพธ์ PASS/FAIL
  และบทเรียนใดที่ต้องการทรัพยากรเสริม (เช่น Azure AI Search, GitHub MCP, Foundry Local,
  Playwright)
---
# การทดสอบตัวอย่างคอร์ส

ตรวจสอบว่าหนังสือบันทึกบทเรียนและตัวอย่างโค้ดทำงานได้กับการตั้งค่า Microsoft Foundry / Azure OpenAI แบบสดหรือไม่
รีโพสนี้มาพร้อมกับตัวรันที่
[`scripts/validate-notebooks.ps1`](../../../../../scripts/validate-notebooks.ps1) ซึ่ง
รันทุกโน้ตบุ๊ก Python แบบไม่มีส่วนติดต่อผู้ใช้และพิมพ์ตารางผ่าน/ไม่ผ่าน

## เมื่อใดควรใช้
- "ตรวจสอบว่าทุกโน้ตบุ๊ก / ตัวอย่างโค้ดทำงานได้กับการสมัคร Azure ของฉัน"
- "ทดสอบเบื้องต้นคอร์สหลังอัปเกรดแพ็กเกจหรือเปลี่ยนโมเดล"
- "บทเรียนใดบ้างที่ยังผ่าน / ไม่ผ่านในสถานการณ์จริง?"

อย่าใช้สำหรับ AI Smoke Test GitHub Action (ที่ตรวจสอบเอเย่นต์โฮสต์ *ที่ใช้งานจริง* — ดู [`tests/README.md`](../../../tests/README.md)) สกิลนี้รันโน้ตบุ๊คแบบโลคัล



1. **Python 3.12+** พร้อม dependencies คอร์ส: `python -m pip install -r requirements.txt`
   พร้อมทั้ง executor: `python -m pip install nbconvert ipykernel`
2. **`.env` ที่โฟลเดอร์รากของรีโพ** (คัดลอกจาก [`.env.example`](../../../../../.env.example)) โดยมีอย่างน้อย:
   - `AZURE_AI_PROJECT_ENDPOINT` — จุดเชื่อมต่อโปรเจค Foundry
     (`https://<account>.services.ai.azure.com/api/projects/<project>`)
   - `AZURE_AI_MODEL_DEPLOYMENT_NAME` — การปรับใช้ที่ไม่ถูกยกเลิกใช้งาน (เช่น `gpt-5-mini`)
   - `AZURE_OPENAI_ENDPOINT` (`https://<account>.openai.azure.com`) และ `AZURE_OPENAI_DEPLOYMENT`
     สำหรับบทเรียนที่เรียกใช้ Azure OpenAI โดยตรง (บทเรียน 06, 02-azure-openai, 14 handoff/human-loop)
3. **`az login`** เสร็จสมบูรณ์ — ตัวอย่างโค้ดยืนยันตัวตนด้วย `AzureCliCredential` (Entra ID, ไม่ใช้กุญแจ)
4. ตรวจสอบว่าโมเดลที่ปรับใช้ยังอยู่:
   `az cognitiveservices account deployment list -g <rg> -n <account> -o table`


```powershell
# All Python notebooks (skips .NET, .venv, site-packages, translations, skill assets)
pwsh scripts/validate-notebooks.ps1

# A single lesson, with a longer per-cell timeout
pwsh scripts/validate-notebooks.ps1 -Filter '08-*' -Timeout 600

# Just list what would run (no execution)
pwsh scripts/validate-notebooks.ps1 -List

# Explicit interpreter (if `python` is not on PATH, e.g. Windows Store alias)
pwsh scripts/validate-notebooks.ps1 -Python "C:/path/to/python.exe"
```
สคริปต์จะเขียนสำเนาที่รันแล้ว ลงบันทึกต่อโน้ตบุ๊ก และ `results.json` ไปยัง
`$env:TEMP\aiab-nbval` และจะออกด้วยจำนวนกรณีที่ล้มเหลว


การล้มเหลวชั่วคราว (ขีดจำกัดอัตรา HTTP 429 สำหรับการสมัครสมาชิกที่ใช้ร่วมกัน, เป็นครั้งคราว
การผิดพลาดของ `AzureCliCredential` token เล็กน้อย หรือการหมดเวลารอ จะถูกลองใหม่โดยอัตโนมัติ
(`-Retries`, ค่าเริ่มต้น 2, พร้อม `-RetryDelaySeconds` backoff, ค่าเริ่มต้น 20) หาก
การปรับใช้โมเดลมีการตอบกลับ 429 อย่างสม่ำเสมอ ให้ตรวจสอบโควต้า GlobalStandard
TPM ของการสมัครใช้งาน (`az cognitiveservices usage list -l <region>`) — การเพิ่มขีดความสามารถของการปรับใช้เดียว
จะไม่ช่วยเมื่อโควต้าของ *การสมัครใช้งาน* หมด

## การตีความผลลัพธ์
- `PASS` — โน้ตบุ๊กทำงานเรียบร้อยตั้งแต่ต้นจนจบโดยไม่มีข้อผิดพลาดของเซลล์
- `FAIL` — แสดงบรรทัดแรกของ `*Error` / `*Exception`; เปิด
  `log_*.txt` ที่ตรงกันในโฟลเดอร์ผลลัพธ์เพื่อดู traceback แบบเต็ม
- ความล้มเหลวของโน้ตบุ๊กเดียวจำกัดโดย `-Timeout` (ต่อเซลล์) ดังนั้นเซลล์ที่
  ค้างซึ่งมี human-in-the-loop จะปรากฏเป็น `StdinNotImplementedError` แทนที่จะค้างอยู่

## บทเรียนที่ต้องการทรัพยากรเสริม (คาดว่าจะล้มเหลวหากไม่มี)
| บทเรียน | ความต้องการเสริม |
|--------|-------------------|
| 05 Agentic RAG | Azure AI Search (`AZURE_SEARCH_SERVICE_ENDPOINT`, key) — มีเส้นทาง fallback ในหน่วยความจำ |
| 11 MCP / GitHub | เซิร์ฟเวอร์ GitHub MCP + PAT |
| 13 memory (cognee) | `cognee` ตั้งค่าด้วยผู้ให้บริการโมเดล |
| 15 browser-use | ติดตั้งเบราว์เซอร์ Playwright (`playwright install`) + `AZURE_OPENAI_CHAT_DEPLOYMENT_NAME` |
| 17 local agent | Foundry Local runtime + โมเดล Qwen ที่ดาวน์โหลดแล้ว (บนอุปกรณ์, ไม่มีคลาวด์) |
| `*-dotnet-*` โน้ตบุ๊ก | เคอร์เนล .NET Interactive (ไม่รวมตามค่าเริ่มต้น; ใช้ `-IncludeDotnet`) |

## การรายงานผลกลับ
สรุปเป็นตารางผ่าน/ไม่ผ่านจัดกลุ่มตามบทเรียน แยกความผิดปกติจริง
(บั๊กโค้ด/การตั้งค่าที่ต้องแก้ไข) ออกจากช่องว่างสภาพแวดล้อม (ขาด Search/Foundry Local/PAT)
และระบุ `log_*.txt` ที่ล้มเหลวสำหรับแต่ละข้อผิดพลาดจริง

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ปฏิเสธความรับผิดชอบ**:
เอกสารนี้ได้รับการแปลโดยใช้บริการแปลภาษา AI [Co-op Translator](https://github.com/Azure/co-op-translator) ขณะที่เราพยายามให้ความถูกต้อง โปรดทราบว่าการแปลโดยอัตโนมัติอาจมีข้อผิดพลาดหรือความไม่ถูกต้อง เอกสารต้นฉบับในภาษาต้นทางควรถูกพิจารณาเป็นแหล่งข้อมูลที่เชื่อถือได้ สำหรับข้อมูลที่สำคัญ แนะนำให้ใช้การแปลโดยมนุษย์มืออาชีพ เราไม่รับผิดชอบต่อความเข้าใจผิดหรือการตีความที่ผิดพลาดที่เกิดขึ้นจากการใช้การแปลนี้
<!-- CO-OP TRANSLATOR DISCLAIMER END -->