# AI Agents for Beginners - Study Guide & Course Summary

This guide provides a summary of the "AI Agents for Beginners" course and explains key concepts, frameworks, and design patterns for building AI Agents.

## 1. Introduction to AI Agents

**What are AI Agents?**
AI Agents are systems that extend the capabilities of Large Language Models (LLMs) by giving them access to **tools**, **knowledge**, and **memory**. Unlike a standard LLM chatbot that only generates text based on training data, an AI Agent can:
- **รับรู้** สภาพแวดล้อมของมัน (ผ่านเซ็นเซอร์หรืออินพุต)
- **คิดวิเคราะห์** เกี่ยวกับวิธีแก้ปัญหา
- **ลงมือปฏิบัติ** เพื่อเปลี่ยนแปลงสภาพแวดล้อม (ผ่านแอกชูเอเตอร์หรือการเรียกใช้เครื่องมือ)

**Key Components of an Agent:**
- **สภาพแวดล้อม**: พื้นที่ที่เอเยนต์ทำงาน (เช่น ระบบจอง)
- **เซ็นเซอร์**: กลไกในการเก็บข้อมูล (เช่น การอ่าน API)
- **แอกชูเอเตอร์**: กลไกในการกระทำ (เช่น การส่งอีเมล)
- **สมอง (LLM)**: เครื่องยนต์การคิดวิเคราะห์ที่วางแผนและตัดสินใจว่าจะทำการใด

## 2. Agentic Frameworks

The course uses **Microsoft Agent Framework (MAF)** with **Azure AI Foundry Agent Service V2** for building agents:

| Component | Focus | Best For |
|-----------|-------|----------|
| **Microsoft Agent Framework** | SDK แบบรวม (Python/C#) สำหรับเอเยนต์ เครื่องมือ และเวิร์กโฟลว์ | การสร้างเอเยนต์ที่มีเครื่องมือ เวิร์กโฟลว์แบบหลายเอเยนต์ และรูปแบบการใช้งานในสภาพแวดล้อมการผลิต |
| **Azure AI Foundry Agent Service** | รันไทม์บนคลาวด์ที่มีการจัดการ | การปรับใช้ที่ปลอดภัยและขยายได้ พร้อมการจัดการสถานะในตัว การตรวจสอบ และความน่าเชื่อถือ |

## 3. Agentic Design Patterns

Design patterns help structure how agents operate to solve problems reliably.

### **Tool Use Pattern** (Lesson 4)
This pattern enables agents to interact with the outside world.
- **Concept**: เอเยนต์จะถูกจัดเตรียม "schema" (รายการฟังก์ชันที่ใช้ได้และพารามิเตอร์ของแต่ละฟังก์ชัน) ให้ LLM ตัดสินใจว่าจะเรียกใช้เครื่องมือใดและด้วยอาร์กิวเมนต์ใดตามคำขอของผู้ใช้
- **Flow**: User Request -> LLM -> **การเลือกเครื่องมือ** -> **การเรียกใช้งานเครื่องมือ** -> LLM (พร้อมผลลัพธ์จากเครื่องมือ) -> Final Response
- **Use Cases**: ดึงข้อมูลเรียลไทม์ (สภาพอากาศ ราคาหุ้น), การคำนวณ, การรันโค้ด

### **Planning Pattern** (Lesson 7)
This pattern enables agents to solve complex, multi-step tasks.
- **Concept**: เอเยนต์แบ่งเป้าหมายระดับสูงออกเป็นลำดับของงานย่อย ๆ
- **Approaches**:
  - **Task Decomposition**: แยก "วางแผนการเดินทาง" เป็น "จองตั๋วเครื่องบิน", "จองโรงแรม", "เช่ารถ"
  - **Iterative Planning**: ประเมินแผนใหม่ตามผลลัพธ์ของขั้นตอนก่อนหน้า (เช่น หากเที่ยวบินเต็ม ให้เลือกวันอื่น)
- **Implementation**: มักเกี่ยวข้องกับเอเยนต์ "Planner" ที่สร้างแผนที่มีโครงสร้าง (เช่น JSON) ซึ่งจากนั้นเอเยนต์อื่น ๆ จะนำไปปฏิบัติ

## 4. Design Principles

When designing agents, consider three dimensions:
- **พื้นที่**: เอเยนต์ควรเชื่อมโยงผู้คนและความรู้ เข้าถึงได้แต่ไม่รบกวน
- **เวลา**: เอเยนต์ควรเรียนรู้จาก *อดีต*, ให้การกระตุ้นที่เกี่ยวข้องใน *ปัจจุบัน*, และปรับตัวสำหรับ *อนาคต*
- **แกนหลัก**: ยอมรับความไม่แน่นอน แต่สร้างความเชื่อมั่นผ่านความโปร่งใสและการควบคุมโดยผู้ใช้

## 5. Summary of Key Lessons

- **บทเรียน 1**: เอเยนต์เป็นระบบ ไม่ใช่แค่โมเดล พวกมันรับรู้ คิดวิเคราะห์ และลงมือปฏิบัติ
- **บทเรียน 2**: Microsoft Agent Framework ช่วยปิดบังความซับซ้อนของการเรียกใช้เครื่องมือและการจัดการสถานะ
- **บทเรียน 3**: ออกแบบโดยคำนึงถึงความโปร่งใสและการควบคุมของผู้ใช้
- **บทเรียน 4**: เครื่องมือคือ "มือ" ของเอเยนต์ การกำหนด schema สำคัญเพื่อให้ LLM เข้าใจวิธีใช้งาน
- **บทเรียน 7**: การวางแผนเป็น "ฟังก์ชันบริหาร" ของเอเยนต์ ช่วยให้จัดการเวิร์กโฟลว์ที่ซับซ้อนได้

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**คำปฏิเสธความรับผิดชอบ**:
เอกสารฉบับนี้ได้รับการแปลโดยใช้บริการแปลด้วยปัญญาประดิษฐ์ [Co-op Translator](https://github.com/Azure/co-op-translator) แม้เราจะพยายามให้การแปลมีความถูกต้อง โปรดทราบว่าการแปลโดยอัตโนมัติอาจมีข้อผิดพลาดหรือความไม่ถูกต้องได้ เอกสารต้นฉบับในภาษาดั้งเดิมควรถูกถือเป็นแหล่งข้อมูลอ้างอิงหลัก สำหรับข้อมูลที่มีความสำคัญ แนะนำให้ใช้การแปลโดยนักแปลมืออาชีพ เราจะไม่รับผิดชอบต่อความเข้าใจผิดหรือการตีความผิดใดๆ ที่เกิดจากการใช้การแปลนี้
<!-- CO-OP TRANSLATOR DISCLAIMER END -->