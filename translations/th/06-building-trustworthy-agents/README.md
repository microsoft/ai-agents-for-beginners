<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "498802b4c3c3cc486b86f27a12cebb34",
  "translation_date": "2025-08-29T15:10:33+00:00",
  "source_file": "06-building-trustworthy-agents/README.md",
  "language_code": "th"
}
-->
[![Trustworthy AI Agents](../../../translated_images/lesson-6-thumbnail.a58ab36c099038d4f786c2b0d5d6e89f41f4c2ecc05ab10b67bced2695eeb218.th.png)](https://youtu.be/iZKkMEGBCUQ?si=Q-kEbcyHUMPoHp8L)

> _(คลิกที่ภาพด้านบนเพื่อดูวิดีโอของบทเรียนนี้)_

# การสร้างตัวแทน AI ที่น่าเชื่อถือ

## บทนำ

บทเรียนนี้จะครอบคลุม:

- วิธีการสร้างและปรับใช้ตัวแทน AI ที่ปลอดภัยและมีประสิทธิภาพ
- ข้อควรพิจารณาด้านความปลอดภัยที่สำคัญเมื่อพัฒนาตัวแทน AI
- วิธีการรักษาความเป็นส่วนตัวของข้อมูลและผู้ใช้เมื่อพัฒนาตัวแทน AI

## เป้าหมายการเรียนรู้

หลังจากจบบทเรียนนี้ คุณจะสามารถ:

- ระบุและลดความเสี่ยงเมื่อสร้างตัวแทน AI
- ใช้มาตรการรักษาความปลอดภัยเพื่อให้แน่ใจว่าการจัดการข้อมูลและการเข้าถึงเป็นไปอย่างเหมาะสม
- สร้างตัวแทน AI ที่รักษาความเป็นส่วนตัวของข้อมูลและมอบประสบการณ์การใช้งานที่มีคุณภาพ

## ความปลอดภัย

เรามาเริ่มต้นด้วยการสร้างแอปพลิเคชันตัวแทนที่ปลอดภัยกันก่อน ความปลอดภัยหมายถึงการที่ตัวแทน AI ทำงานตามที่ออกแบบไว้ ในฐานะผู้สร้างแอปพลิเคชันตัวแทน เรามีวิธีการและเครื่องมือเพื่อเพิ่มความปลอดภัยให้สูงสุด:

### การสร้างกรอบข้อความระบบ

หากคุณเคยสร้างแอปพลิเคชัน AI โดยใช้ Large Language Models (LLMs) คุณจะทราบถึงความสำคัญของการออกแบบข้อความระบบที่แข็งแกร่ง ข้อความเหล่านี้กำหนดกฎเกณฑ์ คำแนะนำ และแนวทางสำหรับการที่ LLM จะโต้ตอบกับผู้ใช้และข้อมูล

สำหรับตัวแทน AI ข้อความระบบยิ่งมีความสำคัญมากขึ้น เนื่องจากตัวแทน AI จะต้องการคำแนะนำที่เฉพาะเจาะจงมากเพื่อทำงานที่เราออกแบบไว้ให้สำเร็จ

เพื่อสร้างข้อความระบบที่สามารถปรับขนาดได้ เราสามารถใช้กรอบข้อความระบบในการสร้างตัวแทนหนึ่งตัวหรือมากกว่าในแอปพลิเคชันของเรา:

![Building a System Message Framework](../../../translated_images/system-message-framework.3a97368c92d11d6814577b03cd128ec8c71a5fd1e26f341835cfa5df59ae87ae.th.png)

#### ขั้นตอนที่ 1: สร้างข้อความระบบเมตา

ข้อความเมตาจะถูกใช้โดย LLM เพื่อสร้างข้อความระบบสำหรับตัวแทนที่เราสร้างขึ้น เราออกแบบมันเป็นแม่แบบเพื่อให้สามารถสร้างตัวแทนหลายตัวได้อย่างมีประสิทธิภาพหากจำเป็น

ตัวอย่างข้อความระบบเมตาที่เราจะให้กับ LLM:

```plaintext
You are an expert at creating AI agent assistants. 
You will be provided a company name, role, responsibilities and other
information that you will use to provide a system prompt for.
To create the system prompt, be descriptive as possible and provide a structure that a system using an LLM can better understand the role and responsibilities of the AI assistant. 
```

#### ขั้นตอนที่ 2: สร้างข้อความพื้นฐาน

ขั้นตอนต่อไปคือการสร้างข้อความพื้นฐานเพื่ออธิบายตัวแทน AI คุณควรรวมบทบาทของตัวแทน งานที่ตัวแทนจะทำ และความรับผิดชอบอื่น ๆ ของตัวแทน

ตัวอย่าง:

```plaintext
You are a travel agent for Contoso Travel that is great at booking flights for customers. To help customers you can perform the following tasks: lookup available flights, book flights, ask for preferences in seating and times for flights, cancel any previously booked flights and alert customers on any delays or cancellations of flights.  
```

#### ขั้นตอนที่ 3: ให้ข้อความระบบพื้นฐานแก่ LLM

ตอนนี้เราสามารถปรับข้อความระบบนี้ให้เหมาะสมโดยให้ข้อความระบบเมตาเป็นข้อความระบบและข้อความระบบพื้นฐานของเรา

สิ่งนี้จะสร้างข้อความระบบที่ออกแบบมาอย่างดีขึ้นเพื่อแนะนำตัวแทน AI ของเรา:

```markdown
**Company Name:** Contoso Travel  
**Role:** Travel Agent Assistant

**Objective:**  
You are an AI-powered travel agent assistant for Contoso Travel, specializing in booking flights and providing exceptional customer service. Your main goal is to assist customers in finding, booking, and managing their flights, all while ensuring that their preferences and needs are met efficiently.

**Key Responsibilities:**

1. **Flight Lookup:**
    
    - Assist customers in searching for available flights based on their specified destination, dates, and any other relevant preferences.
    - Provide a list of options, including flight times, airlines, layovers, and pricing.
2. **Flight Booking:**
    
    - Facilitate the booking of flights for customers, ensuring that all details are correctly entered into the system.
    - Confirm bookings and provide customers with their itinerary, including confirmation numbers and any other pertinent information.
3. **Customer Preference Inquiry:**
    
    - Actively ask customers for their preferences regarding seating (e.g., aisle, window, extra legroom) and preferred times for flights (e.g., morning, afternoon, evening).
    - Record these preferences for future reference and tailor suggestions accordingly.
4. **Flight Cancellation:**
    
    - Assist customers in canceling previously booked flights if needed, following company policies and procedures.
    - Notify customers of any necessary refunds or additional steps that may be required for cancellations.
5. **Flight Monitoring:**
    
    - Monitor the status of booked flights and alert customers in real-time about any delays, cancellations, or changes to their flight schedule.
    - Provide updates through preferred communication channels (e.g., email, SMS) as needed.

**Tone and Style:**

- Maintain a friendly, professional, and approachable demeanor in all interactions with customers.
- Ensure that all communication is clear, informative, and tailored to the customer's specific needs and inquiries.

**User Interaction Instructions:**

- Respond to customer queries promptly and accurately.
- Use a conversational style while ensuring professionalism.
- Prioritize customer satisfaction by being attentive, empathetic, and proactive in all assistance provided.

**Additional Notes:**

- Stay updated on any changes to airline policies, travel restrictions, and other relevant information that could impact flight bookings and customer experience.
- Use clear and concise language to explain options and processes, avoiding jargon where possible for better customer understanding.

This AI assistant is designed to streamline the flight booking process for customers of Contoso Travel, ensuring that all their travel needs are met efficiently and effectively.

```

#### ขั้นตอนที่ 4: ทำซ้ำและปรับปรุง

คุณค่าของกรอบข้อความระบบนี้คือการทำให้การสร้างข้อความระบบสำหรับตัวแทนหลายตัวง่ายขึ้น รวมถึงการปรับปรุงข้อความระบบของคุณเมื่อเวลาผ่านไป โดยปกติแล้วคุณจะไม่สามารถมีข้อความระบบที่ทำงานได้สมบูรณ์แบบในครั้งแรกสำหรับกรณีการใช้งานทั้งหมด การปรับเปลี่ยนเล็กน้อยและการปรับปรุงโดยการเปลี่ยนข้อความระบบพื้นฐานและนำไปใช้ในระบบจะช่วยให้คุณเปรียบเทียบและประเมินผลลัพธ์ได้

## การทำความเข้าใจภัยคุกคาม

เพื่อสร้างตัวแทน AI ที่น่าเชื่อถือ สิ่งสำคัญคือต้องเข้าใจและลดความเสี่ยงและภัยคุกคามต่อตัวแทน AI ของคุณ เรามาดูตัวอย่างบางส่วนของภัยคุกคามที่อาจเกิดขึ้นกับตัวแทน AI และวิธีการวางแผนและเตรียมตัวให้ดีขึ้น

![Understanding Threats](../../../translated_images/understanding-threats.89edeada8a97fc0f7053558567d5dd27c0c333b74e47fffdde490fa6777a4c17.th.png)

### งานและคำสั่ง

**คำอธิบาย:** ผู้โจมตีพยายามเปลี่ยนคำสั่งหรือเป้าหมายของตัวแทน AI ผ่านการป้อนคำสั่งหรือการปรับเปลี่ยนข้อมูลที่ป้อนเข้า

**การลดความเสี่ยง:** ใช้การตรวจสอบความถูกต้องและตัวกรองข้อมูลเพื่อค้นหาคำสั่งที่อาจเป็นอันตรายก่อนที่จะถูกประมวลผลโดยตัวแทน AI เนื่องจากการโจมตีเหล่านี้มักต้องการการโต้ตอบกับตัวแทนบ่อยครั้ง การจำกัดจำนวนรอบในการสนทนาเป็นอีกวิธีหนึ่งในการป้องกันการโจมตีประเภทนี้

### การเข้าถึงระบบสำคัญ

**คำอธิบาย:** หากตัวแทน AI เข้าถึงระบบและบริการที่เก็บข้อมูลที่ละเอียดอ่อน ผู้โจมตีสามารถโจมตีการสื่อสารระหว่างตัวแทนและบริการเหล่านี้ได้ การโจมตีเหล่านี้อาจเป็นการโจมตีโดยตรงหรือความพยายามทางอ้อมในการรับข้อมูลเกี่ยวกับระบบเหล่านี้ผ่านตัวแทน

**การลดความเสี่ยง:** ตัวแทน AI ควรเข้าถึงระบบเฉพาะเมื่อจำเป็นเท่านั้นเพื่อป้องกันการโจมตีประเภทนี้ การสื่อสารระหว่างตัวแทนและระบบควรปลอดภัย การใช้การตรวจสอบสิทธิ์และการควบคุมการเข้าถึงเป็นอีกวิธีหนึ่งในการปกป้องข้อมูลนี้

### การใช้งานทรัพยากรและบริการเกินขนาด

**คำอธิบาย:** ตัวแทน AI สามารถเข้าถึงเครื่องมือและบริการต่าง ๆ เพื่อทำงานให้สำเร็จ ผู้โจมตีสามารถใช้ความสามารถนี้เพื่อโจมตีบริการเหล่านี้โดยการส่งคำขอจำนวนมากผ่านตัวแทน AI ซึ่งอาจส่งผลให้ระบบล้มเหลวหรือมีค่าใช้จ่ายสูง

**การลดความเสี่ยง:** ใช้นโยบายเพื่อจำกัดจำนวนคำขอที่ตัวแทน AI สามารถทำต่อบริการ การจำกัดจำนวนรอบการสนทนาและคำขอไปยังตัวแทน AI ของคุณเป็นอีกวิธีหนึ่งในการป้องกันการโจมตีประเภทนี้

### การปนเปื้อนฐานความรู้

**คำอธิบาย:** การโจมตีประเภทนี้ไม่ได้มุ่งเป้าไปที่ตัวแทน AI โดยตรง แต่เป้าหมายคือฐานความรู้และบริการอื่น ๆ ที่ตัวแทน AI จะใช้ สิ่งนี้อาจเกี่ยวข้องกับการทำให้ข้อมูลที่ตัวแทน AI จะใช้เสียหาย ซึ่งนำไปสู่การตอบสนองที่มีอคติหรือไม่ตั้งใจต่อผู้ใช้

**การลดความเสี่ยง:** ตรวจสอบข้อมูลที่ตัวแทน AI จะใช้ในกระบวนการทำงานอย่างสม่ำเสมอ ตรวจสอบให้แน่ใจว่าการเข้าถึงข้อมูลนี้ปลอดภัยและเปลี่ยนแปลงได้เฉพาะโดยบุคคลที่เชื่อถือได้เพื่อหลีกเลี่ยงการโจมตีประเภทนี้

### ข้อผิดพลาดที่ส่งผลต่อเนื่อง

**คำอธิบาย:** ตัวแทน AI เข้าถึงเครื่องมือและบริการต่าง ๆ เพื่อทำงานให้สำเร็จ ข้อผิดพลาดที่เกิดจากผู้โจมตีสามารถนำไปสู่ความล้มเหลวของระบบอื่น ๆ ที่ตัวแทน AI เชื่อมต่ออยู่ ทำให้การโจมตีแพร่กระจายและแก้ไขได้ยากขึ้น

**การลดความเสี่ยง:** วิธีหนึ่งในการหลีกเลี่ยงสิ่งนี้คือให้ตัวแทน AI ทำงานในสภาพแวดล้อมที่จำกัด เช่น การทำงานใน Docker container เพื่อป้องกันการโจมตีระบบโดยตรง การสร้างกลไกสำรองและตรรกะการลองใหม่เมื่อระบบบางระบบตอบกลับด้วยข้อผิดพลาดเป็นอีกวิธีหนึ่งในการป้องกันความล้มเหลวของระบบที่ใหญ่ขึ้น

## การมีมนุษย์ในกระบวนการ

อีกวิธีหนึ่งที่มีประสิทธิภาพในการสร้างระบบตัวแทน AI ที่น่าเชื่อถือคือการใช้มนุษย์ในกระบวนการ ซึ่งสร้างกระบวนการที่ผู้ใช้สามารถให้ข้อเสนอแนะกับตัวแทนระหว่างการทำงาน ผู้ใช้จะทำหน้าที่เป็นตัวแทนในระบบหลายตัวแทน โดยให้การอนุมัติหรือยุติกระบวนการที่กำลังดำเนินอยู่

![Human in The Loop](../../../translated_images/human-in-the-loop.5f0068a678f62f4fc8373d5b78c4c22f35d9e4da35c93f66c3b634c1774eff34.th.png)

นี่คือตัวอย่างโค้ดที่ใช้ AutoGen เพื่อแสดงให้เห็นว่าหลักการนี้ถูกนำไปใช้:

```python

# Create the agents.
model_client = OpenAIChatCompletionClient(model="gpt-4o-mini")
assistant = AssistantAgent("assistant", model_client=model_client)
user_proxy = UserProxyAgent("user_proxy", input_func=input)  # Use input() to get user input from console.

# Create the termination condition which will end the conversation when the user says "APPROVE".
termination = TextMentionTermination("APPROVE")

# Create the team.
team = RoundRobinGroupChat([assistant, user_proxy], termination_condition=termination)

# Run the conversation and stream to the console.
stream = team.run_stream(task="Write a 4-line poem about the ocean.")
# Use asyncio.run(...) when running in a script.
await Console(stream)

```

## สรุป

การสร้างตัวแทน AI ที่น่าเชื่อถือจำเป็นต้องมีการออกแบบอย่างรอบคอบ มาตรการรักษาความปลอดภัยที่แข็งแกร่ง และการปรับปรุงอย่างต่อเนื่อง โดยการใช้ระบบข้อความเมตาที่มีโครงสร้าง การทำความเข้าใจภัยคุกคามที่อาจเกิดขึ้น และการใช้กลยุทธ์ลดความเสี่ยง นักพัฒนาสามารถสร้างตัวแทน AI ที่ปลอดภัยและมีประสิทธิภาพได้ นอกจากนี้ การรวมกระบวนการที่มีมนุษย์ในกระบวนการช่วยให้ตัวแทน AI สอดคล้องกับความต้องการของผู้ใช้ในขณะที่ลดความเสี่ยงให้น้อยที่สุด เมื่อ AI ยังคงพัฒนา การรักษาท่าทีเชิงรุกเกี่ยวกับความปลอดภัย ความเป็นส่วนตัว และข้อพิจารณาด้านจริยธรรมจะเป็นกุญแจสำคัญในการสร้างความไว้วางใจและความน่าเชื่อถือในระบบที่ขับเคลื่อนด้วย AI

### มีคำถามเพิ่มเติมเกี่ยวกับการสร้างตัวแทน AI ที่น่าเชื่อถือหรือไม่?

เข้าร่วม [Azure AI Foundry Discord](https://aka.ms/ai-agents/discord) เพื่อพบปะกับผู้เรียนคนอื่น ๆ เข้าร่วมชั่วโมงทำการ และรับคำตอบสำหรับคำถามเกี่ยวกับตัวแทน AI ของคุณ

## แหล่งข้อมูลเพิ่มเติม

- <a href="https://learn.microsoft.com/azure/ai-studio/responsible-use-of-ai-overview" target="_blank">ภาพรวม AI ที่มีความรับผิดชอบ</a>
- <a href="https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai" target="_blank">การประเมินโมเดล AI เชิงสร้างสรรค์และแอปพลิเคชัน AI</a>
- <a href="https://learn.microsoft.com/azure/ai-services/openai/concepts/system-message?context=%2Fazure%2Fai-studio%2Fcontext%2Fcontext&tabs=top-techniques" target="_blank">ข้อความระบบเพื่อความปลอดภัย</a>
- <a href="https://blogs.microsoft.com/wp-content/uploads/prod/sites/5/2022/06/Microsoft-RAI-Impact-Assessment-Template.pdf?culture=en-us&country=us" target="_blank">แม่แบบการประเมินความเสี่ยง</a>

## บทเรียนก่อนหน้า

[Agentic RAG](../05-agentic-rag/README.md)

## บทเรียนถัดไป

[Planning Design Pattern](../07-planning-design/README.md)

---

**ข้อจำกัดความรับผิดชอบ**:  
เอกสารนี้ได้รับการแปลโดยใช้บริการแปลภาษา AI [Co-op Translator](https://github.com/Azure/co-op-translator) แม้ว่าเราจะพยายามให้การแปลมีความถูกต้อง แต่โปรดทราบว่าการแปลอัตโนมัติอาจมีข้อผิดพลาดหรือความไม่แม่นยำ เอกสารต้นฉบับในภาษาต้นทางควรถือเป็นแหล่งข้อมูลที่เชื่อถือได้ สำหรับข้อมูลที่สำคัญ ขอแนะนำให้ใช้บริการแปลภาษามนุษย์ที่เป็นมืออาชีพ เราจะไม่รับผิดชอบต่อความเข้าใจผิดหรือการตีความที่ผิดพลาดซึ่งเกิดจากการใช้การแปลนี้