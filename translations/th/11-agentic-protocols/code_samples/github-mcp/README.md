<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "9bf0395cbc541ce8db2a9699c8678dfc",
  "translation_date": "2025-08-29T16:08:44+00:00",
  "source_file": "11-agentic-protocols/code_samples/github-mcp/README.md",
  "language_code": "th"
}
-->
# ตัวอย่างเซิร์ฟเวอร์ Github MCP

## คำอธิบาย

นี่เป็นตัวอย่างที่สร้างขึ้นสำหรับงาน AI Agents Hackathon ซึ่งจัดโดย Microsoft Reactor

เครื่องมือนี้ใช้เพื่อแนะนำโปรเจกต์สำหรับ Hackathon โดยอิงจาก Github repos ของผู้ใช้  
กระบวนการทำงานมีดังนี้:

1. **Github Agent** - ใช้ Github MCP Server เพื่อดึงข้อมูล repos และรายละเอียดเกี่ยวกับ repos เหล่านั้น  
2. **Hackathon Agent** - นำข้อมูลจาก Github Agent มาสร้างไอเดียโปรเจกต์ Hackathon ที่สร้างสรรค์ โดยพิจารณาจากโปรเจกต์, ภาษาที่ผู้ใช้ใช้ และหัวข้อโปรเจกต์สำหรับ AI Agents Hackathon  
3. **Events Agent** - อิงจากคำแนะนำของ Hackathon Agent, Events Agent จะเสนออีเวนต์ที่เกี่ยวข้องจากซีรีส์ AI Agent Hackathon  

## การรันโค้ด

### ตัวแปรสภาพแวดล้อม

ตัวอย่างนี้ใช้ Azure Open AI Service, Semantic Kernel, Github MCP Server และ Azure AI Search  

ตรวจสอบให้แน่ใจว่าคุณได้ตั้งค่าตัวแปรสภาพแวดล้อมที่เหมาะสมเพื่อใช้งานเครื่องมือเหล่านี้:

```python
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME=""
AZURE_OPENAI_EMBEDDING_DEPLOYMENT_NAME=""
AZURE_OPENAI_ENDPOINT=""
AZURE_OPENAI_API_KEY=""
AZURE_OPENAI_API_VERSION=""
AZURE_SEARCH_SERVICE_ENDPOINT=""
AZURE_SEARCH_API_KEY=""
``` 

## การรัน Chainlit Server

เพื่อเชื่อมต่อกับ MCP Server ตัวอย่างนี้ใช้ Chainlit เป็นอินเทอร์เฟซแชท  

ในการรันเซิร์ฟเวอร์ ให้ใช้คำสั่งต่อไปนี้ในเทอร์มินัลของคุณ:

```bash
chainlit run app.py -w
```

คำสั่งนี้จะเริ่ม Chainlit Server บน `localhost:8000` และเติมข้อมูลใน Azure AI Search Index ด้วยเนื้อหา `event-descriptions.md`

## การเชื่อมต่อกับ MCP Server

เพื่อเชื่อมต่อกับ Github MCP Server ให้คลิกที่ไอคอน "ปลั๊ก" ใต้กล่องแชท "Type your message here..":

![MCP Connect](../../../../../translated_images/mcp-chainlit-1.7ed66d648e3cfb28f1ea5f320b91e4404df4a24a0f236ce3de999666621f1cfc.th.png)

จากนั้นคลิก "Connect an MCP" เพื่อเพิ่มคำสั่งสำหรับเชื่อมต่อกับ Github MCP Server:

```bash
npx -y @modelcontextprotocol/server-github --env GITHUB_PERSONAL_ACCESS_TOKEN=[YOUR PERSONAL ACCESS TOKEN]
```

แทนที่ "[YOUR PERSONAL ACCESS TOKEN]" ด้วย Personal Access Token ของคุณจริง ๆ  

หลังจากเชื่อมต่อ คุณควรเห็นตัวเลข (1) ถัดจากไอคอนปลั๊กเพื่อยืนยันว่าการเชื่อมต่อสำเร็จ หากไม่สำเร็จ ลองรีสตาร์ท Chainlit Server ด้วยคำสั่ง `chainlit run app.py -w`

## การใช้งานตัวอย่าง

เพื่อเริ่มกระบวนการทำงานของเอเจนต์ในการแนะนำโปรเจกต์ Hackathon คุณสามารถพิมพ์ข้อความเช่น:

"แนะนำโปรเจกต์ Hackathon สำหรับผู้ใช้ Github ชื่อ koreyspace"

Router Agent จะวิเคราะห์คำขอของคุณและกำหนดว่าควรใช้การผสมผสานของเอเจนต์ (GitHub, Hackathon, และ Events) แบบใดที่เหมาะสมที่สุดในการจัดการคำถามของคุณ เอเจนต์เหล่านี้จะทำงานร่วมกันเพื่อให้คำแนะนำที่ครอบคลุม โดยอิงจากการวิเคราะห์ Github repository, การสร้างไอเดียโปรเจกต์ และอีเวนต์เทคโนโลยีที่เกี่ยวข้อง

---

**ข้อจำกัดความรับผิดชอบ**:  
เอกสารนี้ได้รับการแปลโดยใช้บริการแปลภาษา AI [Co-op Translator](https://github.com/Azure/co-op-translator) แม้ว่าเราจะพยายามให้การแปลมีความถูกต้องมากที่สุด แต่โปรดทราบว่าการแปลอัตโนมัติอาจมีข้อผิดพลาดหรือความไม่ถูกต้อง เอกสารต้นฉบับในภาษาดั้งเดิมควรถือเป็นแหล่งข้อมูลที่เชื่อถือได้ สำหรับข้อมูลที่สำคัญ ขอแนะนำให้ใช้บริการแปลภาษามืออาชีพ เราไม่รับผิดชอบต่อความเข้าใจผิดหรือการตีความผิดที่เกิดจากการใช้การแปลนี้