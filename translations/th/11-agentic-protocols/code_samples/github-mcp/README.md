# Github MCP Server Example

## Description

นี่คือการสาธิตที่สร้างขึ้นสำหรับ AI Agents Hackathon ที่จัดผ่าน Microsoft Reactor

เครื่องมือนี้ใช้ในการแนะนำโปรเจกต์ hackathon ตาม repos บน Github ของผู้ใช้  
โดยทำได้ดังนี้:

1. **Github Agent** - ใช้ Github MCP Server เพื่อดึงข้อมูล repos และข้อมูลเกี่ยวกับ repos เหล่านั้น
2. **Hackathon Agent** - นำข้อมูลจาก Github Agent มาสร้างไอเดียโปรเจกต์ hackathon ที่สร้างสรรค์โดยอิงจากโปรเจกต์ ภาษาที่ผู้ใช้ใช้ และสายโปรเจกต์ของ AI Agents hackathon
3. **Events Agent** - ตามคำแนะนำจาก hackathon agent, events agent จะแนะนำกิจกรรมที่เกี่ยวข้องจากชุดกิจกรรม AI Agent Hackathon

## Running the code 

### Environment Variables

การสาธิตนี้ใช้ Microsoft Agent Framework, Azure OpenAI Service, Github MCP Server และ Azure AI Search

ตรวจสอบให้แน่ใจว่าคุณตั้งค่าตัวแปรสภาพแวดล้อมที่ถูกต้องสำหรับการใช้เครื่องมือเหล่านี้:

```python
AZURE_AI_PROJECT_ENDPOINT=""
AZURE_AI_MODEL_DEPLOYMENT_NAME=""
AZURE_SEARCH_SERVICE_ENDPOINT=""
AZURE_SEARCH_API_KEY=""
``` 


## Running the Chainlit Server

เพื่อต่อเชื่อมกับ MCP server, การสาธิตนี้ใช้ Chainlit เป็นอินเทอร์เฟซแชท

เพื่อรันเซิร์ฟเวอร์, ใช้คำสั่งต่อไปนี้ในเทอร์มินัลของคุณ:

```bash
chainlit run app.py -w
```


ซึ่งจะเริ่มเซิร์ฟเวอร์ Chainlit ของคุณที่ `localhost:8000` และยังเติมข้อมูลใน Azure AI Search Index ของคุณด้วยเนื้อหา `event-descriptions.md` ด้วย

## Connecting to the MCP Server

เพื่อเชื่อมต่อกับ Github MCP Server, เลือกไอคอน "ปลั๊ก" ใต้กล่องแชท "Type your message here..":

![MCP Connect](../../../../../translated_images/th/mcp-chainlit-1.7ed66d648e3cfb28.webp)

จากนั้นคุณสามารถคลิกที่ "Connect an MCP" เพื่อเพิ่มคำสั่งสำหรับเชื่อมต่อกับ Github MCP Server:

```bash
npx -y @modelcontextprotocol/server-github --env GITHUB_PERSONAL_ACCESS_TOKEN=[YOUR PERSONAL ACCESS TOKEN]
```


แทนที่ "[YOUR PERSONAL ACCESS TOKEN]" ด้วย Personal Access Token จริงของคุณ

หลังจากเชื่อมต่อ, คุณจะเห็น (1) ข้างไอคอนปลั๊กเพื่อยืนยันว่ามันเชื่อมต่อแล้ว หากไม่ ให้ลองรีสตาร์ทเซิร์ฟเวอร์ chainlit ด้วย `chainlit run app.py -w`

## Using the Demo 

เพื่อเริ่มกระบวนการแนะนำโปรเจกต์ hackathon ให้พิมพ์ข้อความเช่น:

"Recommend hackathon projects for the Github user koreyspace"

Router Agent จะวิเคราะห์คำขอของคุณและกำหนดว่าการรวมกันของ agent ไหน (GitHub, Hackathon, และ Events) ที่เหมาะสมที่สุดในการจัดการคำถามของคุณ ตัวแทนเหล่านี้ทำงานร่วมกันเพื่อให้คำแนะนำที่ครบถ้วนโดยอิงจากการวิเคราะห์ที่เก็บข้อมูล GitHub, การสร้างไอเดียโปรเจกต์ และกิจกรรมเทคโนโลยีที่เกี่ยวข้อง

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ข้อจำกัดความรับผิดชอบ**:  
เอกสารฉบับนี้ได้รับการแปลโดยใช้บริการแปลภาษาด้วย AI [Co-op Translator](https://github.com/Azure/co-op-translator) แม้เราจะพยายามให้ความแม่นยำ แต่โปรดทราบว่าการแปลโดยอัตโนมัติอาจมีข้อผิดพลาดหรือความคลาดเคลื่อน เอกสารต้นฉบับในภาษาดั้งเดิมควรถือเป็นแหล่งข้อมูลที่เป็นทางการ สำหรับข้อมูลที่สำคัญ แนะนำให้ใช้บริการแปลโดยมืออาชีพ เราจะไม่รับผิดชอบต่อความเข้าใจผิดหรือการตีความผิดใดๆ ที่เกิดจากการใช้การแปลนี้
<!-- CO-OP TRANSLATOR DISCLAIMER END -->