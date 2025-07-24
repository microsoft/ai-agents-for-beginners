<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "e255edb8423b34b4bba20263ef38f208",
  "translation_date": "2025-07-24T07:38:51+00:00",
  "source_file": "11-mcp/README.md",
  "language_code": "th"
}
-->
# บทเรียนที่ 11: การผสานรวม Model Context Protocol (MCP)

## แนะนำ Model Context Protocol (MCP)

Model Context Protocol (MCP) เป็นกรอบการทำงานที่ล้ำสมัยซึ่งถูกออกแบบมาเพื่อสร้างมาตรฐานในการโต้ตอบระหว่างโมเดล AI และแอปพลิเคชันของผู้ใช้งาน MCP ทำหน้าที่เป็นสะพานเชื่อมระหว่างโมเดล AI และแอปพลิเคชันที่ใช้งาน โดยให้ส่วนติดต่อที่สอดคล้องกันไม่ว่าจะเป็นการใช้งานโมเดลแบบใดก็ตาม

จุดเด่นของ MCP:

- **การสื่อสารที่เป็นมาตรฐาน**: MCP สร้างภาษากลางสำหรับแอปพลิเคชันในการสื่อสารกับโมเดล AI  
- **การจัดการบริบทที่มีประสิทธิภาพ**: ช่วยให้สามารถส่งข้อมูลบริบทไปยังโมเดล AI ได้อย่างมีประสิทธิภาพ  
- **ความเข้ากันได้ข้ามแพลตฟอร์ม**: รองรับการทำงานกับภาษาโปรแกรมหลากหลาย เช่น C#, Java, JavaScript, Python และ TypeScript  
- **การผสานรวมที่ราบรื่น**: ช่วยให้นักพัฒนาสามารถผสานรวมโมเดล AI ต่างๆ เข้ากับแอปพลิเคชันได้ง่าย  

MCP มีคุณค่าอย่างยิ่งในงานพัฒนา AI agent เนื่องจากช่วยให้ agent สามารถโต้ตอบกับระบบและแหล่งข้อมูลต่างๆ ผ่านโปรโตคอลเดียว ทำให้ agent มีความยืดหยุ่นและทรงพลังมากขึ้น

## วัตถุประสงค์การเรียนรู้
- เข้าใจว่า MCP คืออะไรและบทบาทของมันในงานพัฒนา AI agent  
- ตั้งค่าและกำหนดค่า MCP server สำหรับการผสานรวมกับ GitHub  
- สร้างระบบ multi-agent โดยใช้เครื่องมือ MCP  
- นำ RAG (Retrieval Augmented Generation) ไปใช้ร่วมกับ Azure Cognitive Search  

## สิ่งที่ต้องเตรียม
- Python 3.8+  
- Node.js 14+  
- การสมัครใช้งาน Azure  
- บัญชี GitHub  
- ความเข้าใจพื้นฐานเกี่ยวกับ Semantic Kernel  

## คำแนะนำในการตั้งค่า

1. **การตั้งค่าสภาพแวดล้อม**  
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```

2. **กำหนดค่า Azure Services**  
   - สร้างทรัพยากร Azure Cognitive Search  
   - ตั้งค่า Azure OpenAI service  
   - กำหนดค่า environment variables ในไฟล์ `.env`  

3. **ตั้งค่า MCP Server**  
   ```bash
   npm install -g @modelcontextprotocol/server-github
   ```

## โครงสร้างโปรเจกต์

```
11-mcp/
├── code_samples/
│   ├── github-mcp/
│   │   ├── app.py              # Main application
│   │   ├── event-descriptions.md  # Event data
│   │   └── MCP_SETUP.md        # Setup guide
│   └── mcp-agents/             # Agent-to-agent communication
│       ├── client/             # MCP client implementation
│       ├── server/             # MCP server with agents
│       └── README.md           # Advanced agent examples
├── README.md
└── requirements.txt
```

## ส่วนประกอบหลัก

### 1. ระบบ Multi-Agent
- GitHub Agent: วิเคราะห์ repository  
- Hackathon Agent: แนะนำโปรเจกต์  
- Events Agent: แนะนำงานเทคโนโลยี  

### 2. การผสานรวม Azure
- Cognitive Search สำหรับการจัดทำดัชนีงานอีเวนต์  
- Azure OpenAI สำหรับความฉลาดของ agent  
- การนำ RAG pattern ไปใช้  

### 3. เครื่องมือ MCP
- การวิเคราะห์ repository บน GitHub  
- การตรวจสอบโค้ด  
- การดึงข้อมูลเมตา  

## การอธิบายโค้ด

ตัวอย่างนี้แสดงให้เห็นถึง:
1. การผสานรวม MCP server  
2. การจัดการ multi-agent  
3. การผสานรวม Azure Cognitive Search  
4. การนำ RAG pattern ไปใช้  

คุณสมบัติเด่น:
- การวิเคราะห์ repository บน GitHub แบบเรียลไทม์  
- การแนะนำโปรเจกต์อย่างชาญฉลาด  
- การจับคู่อีเวนต์โดยใช้ Azure Search  
- การตอบสนองแบบสตรีมด้วย Chainlit  

## การรันตัวอย่าง

สำหรับคำแนะนำการตั้งค่าโดยละเอียดและข้อมูลเพิ่มเติม โปรดดูที่ [Github MCP Server Example README](./code_samples/github-mcp/README.md)

1. เริ่มต้น MCP server:  
   ```bash
   npx @modelcontextprotocol/server-github
   ```

2. เปิดแอปพลิเคชัน:  
   ```bash
   chainlit run app.py -w
   ```

3. ทดสอบการผสานรวม:  
   ```
   Example query: "Analyze repositories for username: <github_username>"
   ```

## การแก้ไขปัญหา

ปัญหาที่พบบ่อยและวิธีแก้ไข:
1. ปัญหาการเชื่อมต่อ MCP  
   - ตรวจสอบว่า server กำลังทำงานอยู่  
   - ตรวจสอบความพร้อมใช้งานของพอร์ต  
   - ยืนยัน GitHub tokens  

2. ปัญหา Azure Search  
   - ตรวจสอบ connection strings  
   - ตรวจสอบการมีอยู่ของดัชนี  
   - ยืนยันการอัปโหลดเอกสาร  

## ขั้นตอนถัดไป
- สำรวจเครื่องมือ MCP เพิ่มเติม  
- สร้าง agent แบบกำหนดเอง  
- เพิ่มความสามารถของ RAG  
- เพิ่มแหล่งข้อมูลอีเวนต์เพิ่มเติม  
- **ขั้นสูง**: ดูตัวอย่างการสื่อสารระหว่าง agent ได้ที่ [mcp-agents/](../../../11-mcp/code_samples/mcp-agents)  

## แหล่งข้อมูล
- [MCP สำหรับผู้เริ่มต้น](https://aka.ms/mcp-for-beginners)  
- [เอกสาร MCP](https://github.com/microsoft/semantic-kernel/tree/main/python/semantic-kernel/semantic_kernel/connectors/mcp)  
- [เอกสาร Azure Cognitive Search](https://learn.microsoft.com/azure/search/)  
- [คู่มือ Semantic Kernel](https://learn.microsoft.com/semantic-kernel/)  

**ข้อจำกัดความรับผิดชอบ**:  
เอกสารนี้ได้รับการแปลโดยใช้บริการแปลภาษา AI [Co-op Translator](https://github.com/Azure/co-op-translator) แม้ว่าเราจะพยายามให้การแปลมีความถูกต้อง แต่โปรดทราบว่าการแปลอัตโนมัติอาจมีข้อผิดพลาดหรือความไม่ถูกต้อง เอกสารต้นฉบับในภาษาดั้งเดิมควรถือเป็นแหล่งข้อมูลที่เชื่อถือได้ สำหรับข้อมูลที่สำคัญ ขอแนะนำให้ใช้บริการแปลภาษามืออาชีพ เราไม่รับผิดชอบต่อความเข้าใจผิดหรือการตีความที่ผิดพลาดซึ่งเกิดจากการใช้การแปลนี้