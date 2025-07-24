<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "e255edb8423b34b4bba20263ef38f208",
  "translation_date": "2025-07-24T08:28:10+00:00",
  "source_file": "11-mcp/README.md",
  "language_code": "th"
}
-->
# บทเรียนที่ 11: การผสานรวม Model Context Protocol (MCP)

## แนะนำ Model Context Protocol (MCP)

Model Context Protocol (MCP) เป็นกรอบการทำงานที่ล้ำสมัยซึ่งออกแบบมาเพื่อมาตรฐานการสื่อสารระหว่างโมเดล AI และแอปพลิเคชันของลูกค้า MCP ทำหน้าที่เป็นสะพานเชื่อมระหว่างโมเดล AI และแอปพลิเคชันที่ใช้งาน โดยให้ส่วนต่อประสานที่สอดคล้องกันไม่ว่าจะเป็นการใช้งานโมเดลแบบใดก็ตาม

จุดเด่นของ MCP:

- **การสื่อสารที่เป็นมาตรฐาน**: MCP สร้างภาษากลางสำหรับแอปพลิเคชันในการสื่อสารกับโมเดล AI
- **การจัดการบริบทที่มีประสิทธิภาพ**: ช่วยให้สามารถส่งข้อมูลบริบทไปยังโมเดล AI ได้อย่างมีประสิทธิภาพ
- **ความเข้ากันได้ข้ามแพลตฟอร์ม**: ใช้งานได้กับหลายภาษาโปรแกรม เช่น C#, Java, JavaScript, Python และ TypeScript
- **การผสานรวมที่ง่ายดาย**: ช่วยให้นักพัฒนาสามารถผสานรวมโมเดล AI ต่างๆ เข้ากับแอปพลิเคชันได้อย่างง่ายดาย

MCP มีคุณค่าอย่างยิ่งในพัฒนาตัวแทน AI เนื่องจากช่วยให้ตัวแทนสามารถโต้ตอบกับระบบและแหล่งข้อมูลต่างๆ ผ่านโปรโตคอลเดียว ทำให้ตัวแทนมีความยืดหยุ่นและทรงพลังมากขึ้น

## วัตถุประสงค์การเรียนรู้
- เข้าใจว่า MCP คืออะไรและบทบาทของมันในพัฒนาตัวแทน AI
- ตั้งค่าและกำหนดค่าเซิร์ฟเวอร์ MCP สำหรับการผสานรวมกับ GitHub
- สร้างระบบหลายตัวแทนโดยใช้เครื่องมือ MCP
- ใช้ RAG (Retrieval Augmented Generation) กับ Azure Cognitive Search

## สิ่งที่ต้องเตรียม
- Python 3.8+
- Node.js 14+
- การสมัครใช้งาน Azure
- บัญชี GitHub
- ความเข้าใจพื้นฐานเกี่ยวกับ Semantic Kernel

## คำแนะนำการตั้งค่า

1. **การตั้งค่าสภาพแวดล้อม**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```

2. **กำหนดค่าบริการ Azure**
   - สร้างทรัพยากร Azure Cognitive Search
   - ตั้งค่าบริการ Azure OpenAI
   - กำหนดค่าตัวแปรสภาพแวดล้อมใน `.env`

3. **ตั้งค่าเซิร์ฟเวอร์ MCP**
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

### 1. ระบบหลายตัวแทน
- ตัวแทน GitHub: วิเคราะห์ที่เก็บข้อมูล
- ตัวแทน Hackathon: แนะนำโปรเจกต์
- ตัวแทน Events: แนะนำกิจกรรมด้านเทคโนโลยี

### 2. การผสานรวม Azure
- Cognitive Search สำหรับการจัดทำดัชนีกิจกรรม
- Azure OpenAI สำหรับความฉลาดของตัวแทน
- การใช้งานรูปแบบ RAG

### 3. เครื่องมือ MCP
- การวิเคราะห์ที่เก็บข้อมูล GitHub
- การตรวจสอบโค้ด
- การดึงข้อมูลเมตา

## การเดินชมโค้ด

ตัวอย่างนี้แสดงให้เห็น:
1. การผสานรวมเซิร์ฟเวอร์ MCP
2. การจัดการระบบหลายตัวแทน
3. การผสานรวม Azure Cognitive Search
4. การใช้งานรูปแบบ RAG

คุณสมบัติเด่น:
- การวิเคราะห์ที่เก็บข้อมูล GitHub แบบเรียลไทม์
- การแนะนำโปรเจกต์อย่างชาญฉลาด
- การจับคู่กิจกรรมโดยใช้ Azure Search
- การตอบสนองแบบสตรีมด้วย Chainlit

## การรันตัวอย่าง

สำหรับคำแนะนำการตั้งค่าโดยละเอียดและข้อมูลเพิ่มเติม โปรดดูที่ [Github MCP Server Example README](./code_samples/github-mcp/README.md)

1. เริ่มเซิร์ฟเวอร์ MCP:
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

ปัญหาทั่วไปและวิธีแก้ไข:
1. ปัญหาการเชื่อมต่อ MCP
   - ตรวจสอบว่าเซิร์ฟเวอร์กำลังทำงานอยู่
   - ตรวจสอบความพร้อมใช้งานของพอร์ต
   - ยืนยันโทเค็น GitHub

2. ปัญหา Azure Search
   - ตรวจสอบความถูกต้องของสตริงการเชื่อมต่อ
   - ตรวจสอบการมีอยู่ของดัชนี
   - ยืนยันการอัปโหลดเอกสาร

## ขั้นตอนถัดไป
- สำรวจเครื่องมือ MCP เพิ่มเติม
- ใช้งานตัวแทนแบบกำหนดเอง
- เพิ่มความสามารถ RAG
- เพิ่มแหล่งข้อมูลกิจกรรมเพิ่มเติม
- **ขั้นสูง**: ดูตัวอย่าง [mcp-agents/](../../../11-mcp/code_samples/mcp-agents) สำหรับการสื่อสารระหว่างตัวแทน

## แหล่งข้อมูล
- [MCP สำหรับผู้เริ่มต้น](https://aka.ms/mcp-for-beginners)  
- [เอกสาร MCP](https://github.com/microsoft/semantic-kernel/tree/main/python/semantic-kernel/semantic_kernel/connectors/mcp)
- [เอกสาร Azure Cognitive Search](https://learn.microsoft.com/azure/search/)
- [คู่มือ Semantic Kernel](https://learn.microsoft.com/semantic-kernel/)

**ข้อจำกัดความรับผิดชอบ**:  
เอกสารนี้ได้รับการแปลโดยใช้บริการแปลภาษา AI [Co-op Translator](https://github.com/Azure/co-op-translator) แม้ว่าเราจะพยายามอย่างเต็มที่เพื่อความถูกต้อง โปรดทราบว่าการแปลอัตโนมัติอาจมีข้อผิดพลาดหรือความไม่แม่นยำ เอกสารต้นฉบับในภาษาต้นทางควรถูกพิจารณาเป็นแหล่งข้อมูลที่เชื่อถือได้ สำหรับข้อมูลที่สำคัญ แนะนำให้ใช้บริการแปลภาษามนุษย์มืออาชีพ เราจะไม่รับผิดชอบต่อความเข้าใจผิดหรือการตีความที่ผิดพลาดซึ่งเกิดจากการใช้การแปลนี้