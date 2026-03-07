[![เอเจนต์ AI ที่น่าเชื่อถือ](../../../translated_images/th/lesson-6-thumbnail.a58ab36c099038d4.webp)](https://youtu.be/iZKkMEGBCUQ?si=Q-kEbcyHUMPoHp8L)

> _(คลิกที่ภาพด้านบนเพื่อดูวิดีโอของบทเรียนนี้)_

# การสร้างเอเจนต์ AI ที่น่าเชื่อถือ

## บทนำ

บทเรียนนี้จะครอบคลุม:

- วิธีการสร้างและปรับใช้เอเจนต์ AI ที่ปลอดภัยและมีประสิทธิภาพ
- ประเด็นด้านความปลอดภัยที่สำคัญเมื่อพัฒนาเอเจนต์ AI
- วิธีการรักษาข้อมูลและความเป็นส่วนตัวของผู้ใช้เมื่อพัฒนาเอเจนต์ AI

## เป้าหมายการเรียนรู้

หลังจากจบบทเรียนนี้ คุณจะทราบวิธี:

- ระบุและลดความเสี่ยงเมื่อสร้างเอเจนต์ AI
- ดำเนินมาตรการด้านความปลอดภัยเพื่อให้แน่ใจว่าการเข้าถึงและข้อมูลได้รับการจัดการอย่างถูกต้อง
- สร้างเอเจนต์ AI ที่รักษาความเป็นส่วนตัวของข้อมูลและมอบประสบการณ์ผู้ใช้ที่มีคุณภาพ

## ความปลอดภัย

มาเริ่มจากการสร้างแอปพลิเคชันที่มีเอเจนต์อย่างปลอดภัยก่อน ความปลอดภัยหมายถึงว่าเอเจนต์ AI ทำงานตามที่ออกแบบไว้ ในฐานะผู้พัฒนาแอปพลิเคชันที่มีเอเจนต์ เรามีวิธีการและเครื่องมือเพื่อเพิ่มความปลอดภัยให้สูงสุด:

### การสร้างกรอบข้อความระบบ

หากคุณเคยสร้างแอปพลิเคชัน AI โดยใช้โมเดลภาษาขนาดใหญ่ (LLMs) คุณจะรู้ถึงความสำคัญของการออกแบบพรอมต์ระบบหรือข้อความระบบที่แข็งแกร่ง ข้อความเหล่านี้กำหนดกฎเมตา คำสั่ง และแนวทางสำหรับการที่ LLM จะโต้ตอบกับผู้ใช้และข้อมูล

สำหรับเอเจนต์ AI ข้อความระบบมีความสำคัญยิ่งกว่าเพราะเอเจนต์ AI ต้องการคำสั่งที่เฉพาะเจาะจงมากเพื่อทำงานที่เราออกแบบไว้ให้เสร็จ

เพื่อสร้างพรอมต์ระบบที่สามารถปรับขนาดได้ เราสามารถใช้กรอบข้อความระบบเพื่อสร้างเอเจนต์หนึ่งตัวหรือหลายตัวในแอปของเรา:

![การสร้างกรอบข้อความระบบ](../../../translated_images/th/system-message-framework.3a97368c92d11d68.webp)

#### ขั้นตอนที่ 1: สร้างข้อความระบบเมตา

พรอมต์เมตาจะถูกใช้โดย LLM เพื่อสร้างพรอมต์ระบบสำหรับเอเจนต์ที่เราสร้าง เราออกแบบมันเป็นเทมเพลตเพื่อให้สามารถสร้างเอเจนต์หลายตัวได้อย่างมีประสิทธิภาพเมื่อจำเป็น

ตัวอย่างของข้อความระบบเมตาที่เราจะให้กับ LLM มีดังนี้:

```plaintext
You are an expert at creating AI agent assistants. 
You will be provided a company name, role, responsibilities and other
information that you will use to provide a system prompt for.
To create the system prompt, be descriptive as possible and provide a structure that a system using an LLM can better understand the role and responsibilities of the AI assistant. 
```

#### ขั้นตอนที่ 2: สร้างพรอมต์พื้นฐาน

ขั้นตอนต่อไปคือการสร้างพรอมต์พื้นฐานเพื่ออธิบายเอเจนต์ AI คุณควรระบุบทบาทของเอเจนต์ งานที่เอเจนต์จะทำ และความรับผิดชอบอื่น ๆ ของเอเจนต์

ตัวอย่างมีดังนี้:

```plaintext
You are a travel agent for Contoso Travel that is great at booking flights for customers. To help customers you can perform the following tasks: lookup available flights, book flights, ask for preferences in seating and times for flights, cancel any previously booked flights and alert customers on any delays or cancellations of flights.  
```

#### ขั้นตอนที่ 3: ให้ข้อความระบบพื้นฐานแก่ LLM

ตอนนี้เราสามารถเพิ่มประสิทธิภาพข้อความระบบนี้โดยการใช้ข้อความระบบเมตาเป็นข้อความระบบและข้อความระบบพื้นฐานของเรา

สิ่งนี้จะสร้างข้อความระบบที่ออกแบบมาได้ดีขึ้นเพื่อชี้นำเอเจนต์ AI ของเรา:

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

คุณค่าของกรอบข้อความระบบนี้คือช่วยให้สามารถขยายการสร้างข้อความระบบจากเอเจนต์หลายตัวได้ง่ายขึ้นรวมถึงการปรับปรุงข้อความระบบของคุณเมื่อเวลาผ่านไป มันเป็นเรื่องที่หาได้ยากที่ข้อความระบบจะได้ผลสมบูรณ์ในครั้งแรกสำหรับกรณีการใช้งานทั้งหมด การสามารถปรับเปลี่ยนเล็กน้อยและปรับปรุงโดยการเปลี่ยนข้อความระบบพื้นฐานแล้วรันผ่านระบบจะช่วยให้คุณเปรียบเทียบและประเมินผลลัพธ์ได้

## การเข้าใจภัยคุกคาม

เพื่อสร้างเอเจนต์ AI ที่เชื่อถือได้ สิ่งสำคัญคือต้องเข้าใจและลดความเสี่ยงรวมถึงภัยคุกคามต่อเอเจนต์ AI ของคุณ มาดูเพียงบางส่วนของภัยคุกคามต่าง ๆ ต่อเอเจนต์ AI และวิธีที่คุณสามารถวางแผนและเตรียมรับมือกับพวกมันได้ดีขึ้น

![การเข้าใจภัยคุกคาม](../../../translated_images/th/understanding-threats.89edeada8a97fc0f.webp)

### งานและคำสั่ง

**คำอธิบาย:** ผู้โจมตีพยายามเปลี่ยนคำสั่งหรือเป้าหมายของเอเจนต์ AI ผ่านการกระตุ้นคำสั่ง (prompting) หรือการจัดการอินพุต

**การลดความเสี่ยง:** ดำเนินการตรวจสอบการยืนยันและตัวกรองอินพุตเพื่อตรวจจับพรอมต์ที่อาจเป็นอันตรายก่อนที่จะถูกประมวลผลโดยเอเจนต์ AI เนื่องจากการโจมตีเหล่านี้มักต้องการการโต้ตอบบ่อยครั้งกับเอเจนต์ การจำกัดจำนวนรอบในการสนทนาก็เป็นอีกวิธีหนึ่งในการป้องกันการโจมตีประเภทนี้

### การเข้าถึงระบบที่สำคัญ

**คำอธิบาย:** หากเอเจนต์ AI สามารถเข้าถึงระบบและบริการที่เก็บข้อมูลที่ละเอียดอ่อน ผู้โจมตีสามารถบุกรุกการสื่อสารระหว่างเอเจนต์และบริการเหล่านี้ได้ การโจมตีอาจเป็นแบบตรงหรือพยายามสืบข้อมูลเกี่ยวกับระบบเหล่านี้ผ่านเอเจนต์

**การลดความเสี่ยง:** เอเจนต์ AI ควรมีสิทธิ์เข้าถึงระบบเฉพาะตามความจำเป็นเท่านั้นเพื่อลดการโจมตีประเภทนี้ การสื่อสารระหว่างเอเจนต์และระบบควรปลอดภัย การใช้งานการพิสูจน์ตัวตนและการควบคุมการเข้าถึงเป็นอีกวิธีหนึ่งในการปกป้องข้อมูลนี้

### การล้นทรัพยากรและบริการ

**คำอธิบาย:** เอเจนต์ AI สามารถเข้าถึงเครื่องมือและบริการต่าง ๆ เพื่อทำงาน ผู้โจมตีสามารถใช้ความสามารถนี้โจมตีบริการเหล่านี้โดยส่งคำขอจำนวนมากผ่านเอเจนต์ AI ซึ่งอาจนำไปสู่ความล้มเหลวของระบบหรือค่าใช้จ่ายสูง

**การลดความเสี่ยง:** ดำเนินนโยบายเพื่อจำกัดจำนวนคำขอที่เอเจนต์ AI สามารถส่งไปยังบริการ จำกัดจำนวนรอบการสนทนาและคำขอต่อเอเจนต์ AI ของคุณเป็นอีกวิธีหนึ่งในการป้องกันการโจมตีประเภทนี้

### การทำให้ฐานความรู้ปนเปื้อน

**คำอธิบาย:** การโจมตีประเภทนี้ไม่ได้มุ่งเป้าไปที่เอเจนต์ AI โดยตรง แต่จะมุ่งไปที่ฐานความรู้และบริการอื่น ๆ ที่เอเจนต์ AI จะใช้ ซึ่งอาจรวมถึงการทำให้ข้อมูลหรือข้อมูลที่เอเจนต์ใช้เกิดความเสียหาย นำไปสู่การตอบกลับที่มีอคติหรือไม่เป็นไปตามที่คาดหวังต่อผู้ใช้

**การลดความเสี่ยง:** ดำเนินการตรวจสอบความถูกต้องของข้อมูลที่เอเจนต์ AI จะใช้ในเวิร์กโฟลว์อย่างสม่ำเสมอ ตรวจสอบให้แน่ใจว่าการเข้าถึงข้อมูลนี้มีความปลอดภัยและมีการเปลี่ยนแปลงโดยบุคคลที่เชื่อถือได้เท่านั้นเพื่อลดความเสี่ยงของการโจมตีประเภทนี้

### ข้อผิดพลาดที่เป็นลูกโซ่

**คำอธิบาย:** เอเจนต์ AI เข้าถึงเครื่องมือและบริการต่าง ๆ เพื่อทำงาน ข้อผิดพลาดที่เกิดจากผู้โจมตีสามารถนำไปสู่ความล้มเหลวของระบบอื่น ๆ ที่เอเจนต์เชื่อมต่ออยู่ ทำให้การโจมตีขยายวงกว้างและยากต่อการแก้ไขปัญหา

**การลดความเสี่ยง:** หนึ่งในวิธีการหลีกเลี่ยงคือให้เอเจนต์ AI ทำงานในสภาพแวดล้อมจำกัด เช่น การทำงานในคอนเทนเนอร์ Docker เพื่อป้องกันการโจมตีโดยตรงต่อระบบ การสร้างกลไกสำรองและตรรกะการลองใหม่เมื่อระบบบางอย่างตอบกลับด้วยข้อผิดพลาดเป็นอีกวิธีหนึ่งเพื่อป้องกันความล้มเหลวของระบบในวงกว้าง

## มนุษย์ในวงจร

อีกวิธีที่มีประสิทธิภาพในการสร้างระบบเอเจนต์ AI ที่เชื่อถือได้คือการใช้มนุษย์ในวงจร วิธีนี้สร้างกระบวนการที่ผู้ใช้สามารถให้ข้อเสนอแนะแก่เอเจนต์ระหว่างการทำงาน ผู้ใช้ทำหน้าที่เสมือนเอเจนต์ในระบบหลายเอเจนต์และให้การอนุมัติหรือยุติการทำงานของกระบวนการที่กำลังรันได้

![มนุษย์ในวงจร](../../../translated_images/th/human-in-the-loop.5f0068a678f62f4f.webp)

นี่คือตัวอย่างโค้ดที่ใช้ Microsoft Agent Framework เพื่อแสดงแนวคิดนี้ว่าถูกนำไปใช้อย่างไร:

```python
import os
from agent_framework.azure import AzureAIProjectAgentProvider
from azure.identity import AzureCliCredential

# สร้างผู้ให้บริการโดยมีการอนุมัติแบบมีคนคอยควบคุม
provider = AzureAIProjectAgentProvider(
    credential=AzureCliCredential(),
)

# สร้างตัวแทนโดยมีขั้นตอนการอนุมัติจากมนุษย์
response = provider.create_response(
    input="Write a 4-line poem about the ocean.",
    instructions="You are a helpful assistant. Ask for user approval before finalizing.",
)

# ผู้ใช้สามารถตรวจสอบและอนุมัติคำตอบได้
print(response.output_text)
user_input = input("Do you approve? (APPROVE/REJECT): ")
if user_input == "APPROVE":
    print("Response approved.")
else:
    print("Response rejected. Revising...")
```

## บทสรุป

การสร้างเอเจนต์ AI ที่เชื่อถือได้ต้องการการออกแบบอย่างรอบคอบ มาตรการด้านความปลอดภัยที่แข็งแกร่ง และการวนซ้ำอย่างต่อเนื่อง โดยการใช้ระบบพรอมต์เมตาที่มีโครงสร้าง การเข้าใจภัยคุกคามที่อาจเกิดขึ้น และการใช้กลยุทธ์ลดความเสี่ยง นักพัฒนาสามารถสร้างเอเจนต์ AI ที่ปลอดภัยและมีประสิทธิภาพ นอกจากนี้ การผนวกวิธีการมีมนุษย์ในวงจรช่วยให้เอเจนต์ AI ยังคงสอดคล้องกับความต้องการของผู้ใช้ในขณะที่ลดความเสี่ยง เมื่อ AI ยังคงพัฒนา การรักษาท่าทีเชิงรุกด้านความปลอดภัย ความเป็นส่วนตัว และข้อพิจารณาทางจริยธรรมจะเป็นกุญแจสำคัญในการส่งเสริมความไว้ใจและความน่าเชื่อถือในระบบที่ขับเคลื่อนด้วย AI

### มีคำถามเพิ่มเติมเกี่ยวกับการสร้างเอเจนต์ AI ที่น่าเชื่อถือไหม?

เข้าร่วม [Microsoft Foundry Discord](https://aka.ms/ai-agents/discord) เพื่อพบกับผู้เรียนคนอื่น ๆ เข้าร่วมชั่วโมงทำการและให้คำถามเกี่ยวกับเอเจนต์ AI ของคุณได้รับคำตอบ

## แหล่งข้อมูลเพิ่มเติม

- <a href="https://learn.microsoft.com/azure/ai-studio/responsible-use-of-ai-overview" target="_blank">ภาพรวมการใช้ AI อย่างรับผิดชอบ</a>
- <a href="https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai" target="_blank">การประเมินโมเดลและแอปพลิเคชัน AI เชิงสร้างสรรค์</a>
- <a href="https://learn.microsoft.com/azure/ai-services/openai/concepts/system-message?context=%2Fazure%2Fai-studio%2Fcontext%2Fcontext&tabs=top-techniques" target="_blank">ข้อความระบบด้านความปลอดภัย</a>
- <a href="https://blogs.microsoft.com/wp-content/uploads/prod/sites/5/2022/06/Microsoft-RAI-Impact-Assessment-Template.pdf?culture=en-us&country=us" target="_blank">เทมเพลตการประเมินความเสี่ยง</a>

## บทเรียนก่อนหน้า

[Agentic RAG](../05-agentic-rag/README.md)

## บทเรียนถัดไป

[Planning Design Pattern](../07-planning-design/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
ข้อจำกัดความรับผิดชอบ:
เอกสารฉบับนี้ถูกแปลโดยใช้บริการแปลด้วยปัญญาประดิษฐ์ [Co-op Translator](https://github.com/Azure/co-op-translator) แม้เราจะพยายามให้การแปลมีความถูกต้อง โปรดทราบว่าการแปลโดยอัตโนมัติอาจมีข้อผิดพลาดหรือความคลาดเคลื่อน เอกสารต้นฉบับในภาษาดั้งเดิมควรถูกพิจารณาเป็นแหล่งข้อมูลที่เชื่อถือได้ สำหรับข้อมูลที่สำคัญ แนะนำให้ใช้บริการแปลโดยนักแปลมนุษย์มืออาชีพ เราไม่รับผิดชอบต่อความเข้าใจผิดหรือการตีความผิดพลาดใด ๆ ที่เกิดจากการใช้การแปลฉบับนี้
<!-- CO-OP TRANSLATOR DISCLAIMER END -->