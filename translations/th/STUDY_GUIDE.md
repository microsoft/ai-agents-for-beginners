# ตัวแทน AI สำหรับผู้เริ่มต้น - คู่มือการศึกษา & สรุปคอร์ส

This guide provides a summary of the "AI Agents for Beginners" course and explains key concepts, frameworks, and design patterns for building AI Agents.

## 1. บทนำสู่ตัวแทน AI

**ตัวแทน AI คืออะไร?**
AI Agents are systems that extend the capabilities of Large Language Models (LLMs) by giving them access to **tools**, **knowledge**, and **memory**. Unlike a standard LLM chatbot that only generates text based on training data, an AI Agent can:
- **รับรู้** สภาพแวดล้อมของมัน (via sensors or inputs).
- **คิดวิเคราะห์** เกี่ยวกับวิธีแก้ปัญหา.
- **ลงมือ** เพื่อเปลี่ยนแปลงสภาพแวดล้อม (via actuators or tool execution).

**ส่วนประกอบสำคัญของตัวแทน:**
- **สภาพแวดล้อม**: พื้นที่ที่ตัวแทนทำงาน (e.g., a booking system).
- **เซ็นเซอร์**: กลไกในการรวบรวมข้อมูล (e.g., reading an API).
- **ตัวกระตุ้น**: กลไกในการดำเนินการ (e.g., sending an email).
- **สมอง (LLM)**: เอนจินการใช้เหตุผลที่วางแผนและตัดสินใจว่าจะดำเนินการใด

## 2. เฟรมเวิร์กสำหรับตัวแทน

The course uses **Microsoft Agent Framework (MAF)** with **Azure AI Foundry Agent Service V2** for building agents:

| องค์ประกอบ | เน้น | เหมาะสำหรับ |
|-----------|-------|----------|
| **Microsoft Agent Framework** | SDK แบบรวมสำหรับ Python/C# สำหรับตัวแทน, เครื่องมือ, และเวิร์กโฟลว์ | การสร้างตัวแทนที่มีเครื่องมือ, เวิร์กโฟลว์หลายตัวแทน, และรูปแบบการใช้งานในโปรดักชัน. |
| **Azure AI Foundry Agent Service** | รันไทม์คลาวด์ที่จัดการให้ | การปรับใช้ที่ปลอดภัยและปรับขนาดได้ พร้อมการจัดการสถานะในตัว, การสังเกตการณ์, และความน่าเชื่อถือ. |

## 3. รูปแบบการออกแบบเชิงตัวแทน

Design patterns help structure how agents operate to solve problems reliably.

### **รูปแบบการใช้เครื่องมือ** (Lesson 4)
This pattern enables agents to interact with the outside world.
- **Concept**: ตัวแทนได้รับ "schema" (a list of available functions and their parameters). The LLM decides *which* tool to call and with *what* arguments based on the user's request.
- **Flow**: User Request -> LLM -> **การเลือกเครื่องมือ** -> **การเรียกใช้เครื่องมือ** -> LLM (with tool output) -> Final Response.
- **Use Cases**: Retrieving real-time data (weather, stock prices), performing calculations, executing code.

### **รูปแบบการวางแผน** (Lesson 7)
This pattern enables agents to solve complex, multi-step tasks.
- **Concept**: The agent breaks down a high-level goal into a sequence of smaller subtasks.
- **Approaches**:
  - **Task Decomposition**: Splitting "Plan a trip" into "Book flight", "Book hotel", "Rent car".
  - **Iterative Planning**: Re-evaluating the plan based on the output of previous steps (e.g., if the flight is full, choose a different date).
- **Implementation**: Often involves a "Planner" agent that generates a structured plan (e.g., JSON) which is then executed by other agents.

## 4. หลักการออกแบบ

When designing agents, consider three dimensions:
- **Space**: Agents should connect people and knowledge, be accessible but unobtrusive.
- **Time**: Agents should learn from the *Past*, provide relevant nudges in the *Now*, and adapt for the *Future*.
- **Core**: Embrace uncertainty but establish trust through transparency and user control.

## 5. สรุปบทเรียนสำคัญ

- **Lesson 1**: Agents are systems, not just models. They perceive, reason, and act.
- **Lesson 2**: Microsoft Agent Framework abstracts the complexity of tool calling and state management.
- **Lesson 3**: Design with transparency and user control in mind.
- **Lesson 4**: Tools are the "hands" of the agent. Schema definition is crucial for the LLM to understand how to use them.
- **Lesson 7**: Planning is the "executive function" of the agent, enabling it to tackle complex workflows.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
ข้อจำกัดความรับผิดชอบ:
เอกสารฉบับนี้ได้รับการแปลโดยใช้บริการแปลภาษาอัตโนมัติ AI [Co-op Translator](https://github.com/Azure/co-op-translator) แม้ว่าเราจะมุ่งมั่นเพื่อความถูกต้อง โปรดทราบว่าการแปลโดยอัตโนมัติอาจมีข้อผิดพลาดหรือความไม่ถูกต้องได้ เอกสารต้นฉบับในภาษาดั้งเดิมควรถือเป็นแหล่งข้อมูลอ้างอิงที่เชื่อถือได้ สำหรับข้อมูลที่มีความสำคัญ ขอแนะนำให้ใช้บริการแปลโดยนักแปลมืออาชีพ เราไม่รับผิดชอบต่อความเข้าใจผิดหรือการตีความที่ผิดพลาดใด ๆ ที่เกิดขึ้นจากการใช้การแปลนี้
<!-- CO-OP TRANSLATOR DISCLAIMER END -->