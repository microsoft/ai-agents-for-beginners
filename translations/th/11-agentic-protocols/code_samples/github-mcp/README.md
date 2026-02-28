# ตัวอย่างเซิร์ฟเวอร์ Github MCP

## คำอธิบาย

นี่คือการสาธิตที่สร้างขึ้นสำหรับ AI Agents Hackathon ที่จัดโดย Microsoft Reactor

เครื่องมือนี้ใช้เพื่อแนะนำโปรเจกต์แฮกกาธอนตามรีโปของผู้ใช้บน Github
สิ่งนี้ทำโดย:

1. **Github Agent** - ใช้ Github MCP Server เพื่อดึงรีโปและข้อมูลเกี่ยวกับรีโปเหล่านั้น
2. **Hackathon Agent** - รับข้อมูลจาก Github Agent และสร้างไอเดียโปรเจกต์แฮกกาธอนอย่างสร้างสรรค์โดยอิงจากโปรเจกต์ ภาษาที่ผู้ใช้ใช้ และแนวทางโปรเจกต์สำหรับ AI Agents hackathon
3. **Events Agent** - จากคำแนะนำของ hackathon agent, events agent จะเสนอเหตุการณ์ที่เกี่ยวข้องจากชุด AI Agent Hackathon

## การรันโค้ด

### ตัวแปรสภาพแวดล้อม

การสาธิตนี้ใช้ Microsoft Agent Framework, Azure OpenAI Service, Github MCP Server และ Azure AI Search

ตรวจสอบให้แน่ใจว่าคุณตั้งค่าตัวแปรสภาพแวดล้อมที่เหมาะสมเพื่อใช้เครื่องมือเหล่านี้:

```python
AZURE_AI_PROJECT_ENDPOINT=""
AZURE_AI_MODEL_DEPLOYMENT_NAME=""
AZURE_SEARCH_SERVICE_ENDPOINT=""
AZURE_SEARCH_API_KEY=""
``` 


## การรันเซิร์ฟเวอร์ Chainlit

เพื่อเชื่อมต่อกับ MCP server, การสาธิตนี้ใช้ Chainlit เป็นอินเทอร์เฟซแชท

เพื่อรันเซิร์ฟเวอร์, ใช้คำสั่งนี้ในเทอร์มินัลของคุณ:

```bash
chainlit run app.py -w
```


ซึ่งจะเริ่มต้นเซิร์ฟเวอร์ Chainlit ของคุณบน `localhost:8000` รวมทั้งเติมข้อมูลในดัชนี Azure AI Search ด้วยเนื้อหา `event-descriptions.md`

## การเชื่อมต่อกับ MCP Server

เพื่อเชื่อมต่อกับ Github MCP Server, เลือกไอคอน "ปลั๊ก" ใต้กล่องแชทที่มีข้อความ "พิมพ์ข้อความของคุณที่นี่..":

![MCP Connect](../../../../../translated_images/th/mcp-chainlit-1.7ed66d648e3cfb28.webp)

จากนั้นคุณสามารถคลิกที่ "เชื่อมต่อ MCP" เพื่อเพิ่มคำสั่งเชื่อมต่อกับ Github MCP Server:

```bash
npx -y @modelcontextprotocol/server-github --env GITHUB_PERSONAL_ACCESS_TOKEN=[YOUR PERSONAL ACCESS TOKEN]
```


แทนที่ "[YOUR PERSONAL ACCESS TOKEN]" ด้วยโทเค็นเข้าถึงส่วนตัวของคุณจริงๆ

หลังจากเชื่อมต่อแล้ว คุณควรเห็นหมายเลข (1) ข้างไอคอนปลั๊กเพื่อยืนยันว่ามีการเชื่อมต่อ หากไม่เชื่อมต่อ ให้ลองรีสตาร์ทเซิร์ฟเวอร์ chainlit ด้วย `chainlit run app.py -w`

## การใช้เดโม

เพื่อเริ่มเวิร์กโฟลว์ของเอเจนต์ในการแนะนำโปรเจกต์แฮกกาธอน คุณสามารถพิมพ์ข้อความเช่น:

"แนะนำโปรเจกต์แฮกกาธอนสำหรับผู้ใช้ Github ชื่อ koreyspace"

Router Agent จะวิเคราะห์คำขอของคุณและกำหนดว่าคอมบิเนชันของเอเจนต์ใด (GitHub, Hackathon และ Events) เหมาะสมที่สุดที่จะจัดการคำถามของคุณ เอเจนต์เหล่านี้ทำงานร่วมกันเพื่อให้คำแนะนำที่ครอบคลุมโดยอิงจากการวิเคราะห์รีโป GitHub, การหาไอเดียโปรเจกต์ และเหตุการณ์เทคโนโลยีที่เกี่ยวข้อง

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**คำปฏิเสธความรับผิดชอบ**:  
เอกสารนี้ได้ถูกแปลโดยใช้บริการแปลภาษาด้วย AI [Co-op Translator](https://github.com/Azure/co-op-translator) แม้เราจะพยายามให้มีความถูกต้อง แต่โปรดทราบว่าการแปลโดยอัตโนมัติอาจมีข้อผิดพลาดหรือความไม่ถูกต้อง เอกสารต้นฉบับในภาษาดั้งเดิมถือเป็นแหล่งข้อมูลที่น่าเชื่อถือที่สุด สำหรับข้อมูลที่สำคัญแนะนำให้ใช้การแปลโดยผู้เชี่ยวชาญมืออาชีพ เราไม่รับผิดชอบต่อความเข้าใจผิดหรือการตีความผิดใด ๆ ที่เกิดจากการใช้การแปลนี้
<!-- CO-OP TRANSLATOR DISCLAIMER END -->