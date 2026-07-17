[![ตัวแทน AI ที่เชื่อถือได้](../../../translated_images/th/lesson-6-thumbnail.a58ab36c099038d4.webp)](https://youtu.be/iZKkMEGBCUQ?si=Q-kEbcyHUMPoHp8L)

> _(คลิกที่ภาพด้านบนเพื่อดูวิดีโอของบทเรียนนี้)_

# การสร้างตัวแทน AI ที่เชื่อถือได้

## บทนำ

บทเรียนนี้จะครอบคลุม:

- วิธีการสร้างและปรับใช้ตัวแทน AI ที่ปลอดภัยและมีประสิทธิภาพ
- ข้อควรพิจารณาด้านความปลอดภัยที่สำคัญเมื่อพัฒนาตัวแทน AI
- วิธีการรักษาข้อมูลและความเป็นส่วนตัวของผู้ใช้เมื่อพัฒนาตัวแทน AI

## เป้าหมายการเรียนรู้

หลังจากทำบทเรียนนี้เสร็จแล้ว คุณจะรู้วิธี:

- ระบุและลดความเสี่ยงเมื่อต้องสร้างตัวแทน AI
- ดำเนินมาตรการความปลอดภัยเพื่อให้แน่ใจว่าข้อมูลและการเข้าถึงได้รับการจัดการอย่างเหมาะสม
- สร้างตัวแทน AI ที่รักษาความเป็นส่วนตัวของข้อมูลและให้ประสบการณ์ผู้ใช้ที่มีคุณภาพ

## ความปลอดภัย

เรามาดูการสร้างแอปพลิเคชันเชิงตัวแทนที่ปลอดภัยก่อน ความปลอดภัยหมายถึงตัวแทน AI ทำงานตามที่ออกแบบไว้ ในฐานะผู้สร้างแอปพลิเคชันเชิงตัวแทน เรามีวิธีและเครื่องมือเพื่อเพิ่มความปลอดภัยสูงสุด:

### การสร้างโครงสร้างระบบข้อความ

ถ้าคุณเคยสร้างแอปพลิเคชัน AI โดยใช้โมเดลภาษาขนาดใหญ่ (LLMs) คุณจะรู้ถึงความสำคัญของการออกแบบพรอมต์ระบบหรือข้อความระบบที่มั่นคง พรอมต์เหล่านี้กำหนดกฎเกณฑ์ คำแนะนำ และแนวทางสำหรับวิธีที่ LLM จะโต้ตอบกับผู้ใช้และข้อมูล

สำหรับตัวแทน AI, พรอมต์ระบบมีความสำคัญยิ่งขึ้นเพราะตัวแทน AI จำเป็นต้องมีคำแนะนำที่เฉพาะเจาะจงมากเพื่อทำภารกิจที่เรากำหนดไว้ให้สำเร็จ

เพื่อสร้างพรอมต์ระบบที่ขยายขนาดได้ เราสามารถใช้โครงสร้างข้อความระบบเพื่อสร้างตัวแทนหนึ่งตัวหรือมากกว่าในแอปพลิเคชันของเรา:

![Building a System Message Framework](../../../translated_images/th/system-message-framework.3a97368c92d11d68.webp)

#### ขั้นตอนที่ 1: สร้างข้อความระบบเมตา

พรอมต์เมต้าจะถูกใช้โดย LLM เพื่อสร้างพรอมต์ระบบสำหรับตัวแทนที่เราสร้าง เราออกแบบมันเป็นแม่แบบเพื่อให้สามารถสร้างตัวแทนหลายตัวได้อย่างมีประสิทธิภาพหากจำเป็น

นี่คือตัวอย่างข้อความระบบเมต้าที่เราจะให้กับ LLM:

```plaintext
You are an expert at creating AI agent assistants. 
You will be provided a company name, role, responsibilities and other
information that you will use to provide a system prompt for.
To create the system prompt, be descriptive as possible and provide a structure that a system using an LLM can better understand the role and responsibilities of the AI assistant. 
```

#### ขั้นตอนที่ 2: สร้างพรอมต์พื้นฐาน

ขั้นตอนต่อไปคือการสร้างพรอมต์พื้นฐานเพื่ออธิบายตัวแทน AI คุณควรรวมบทบาทของตัวแทน งานที่ตัวแทนจะทำ และความรับผิดชอบอื่นใดของตัวแทน

นี่คือตัวอย่าง:

```plaintext
You are a travel agent for Contoso Travel that is great at booking flights for customers. To help customers you can perform the following tasks: lookup available flights, book flights, ask for preferences in seating and times for flights, cancel any previously booked flights and alert customers on any delays or cancellations of flights.  
```

#### ขั้นตอนที่ 3: ให้ข้อความระบบพื้นฐานกับ LLM

ตอนนี้เราสามารถเพิ่มประสิทธิภาพข้อความระบบนี้โดยการให้ข้อความระบบเมตาเป็นข้อความระบบและข้อความระบบพื้นฐานของเรา

นี่จะสร้างข้อความระบบที่ออกแบบมาเพื่อชี้นำตัวแทน AI ของเราดีขึ้น:

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

คุณค่าของโครงสร้างข้อความระบบนี้คือสามารถขยายการสร้างข้อความระบบจากตัวแทนหลายตัวได้ง่ายขึ้น รวมถึงการปรับปรุงข้อความระบบของคุณเมื่อเวลาผ่านไป ยากที่จะมีข้อความระบบที่ใช้งานครั้งแรกได้สำหรับกรณีการใช้งานทั้งหมด คุณจะสามารถปรับแต่งและปรับปรุงเล็กน้อยโดยการเปลี่ยนข้อความระบบพื้นฐานและเรียกใช้ผ่านระบบเพื่อเปรียบเทียบและประเมินผลลัพธ์

## ความเข้าใจเกี่ยวกับภัยคุกคาม

ในการสร้างตัวแทน AI ที่เชื่อถือได้ สิ่งสำคัญคือการเข้าใจและลดความเสี่ยงและภัยคุกคามต่อตัวแทน AI ของคุณ มาดูภัยคุกคามบางประเภทต่อตัวแทน AI และวิธีที่คุณสามารถวางแผนและเตรียมพร้อมได้ดียิ่งขึ้น

![Understanding Threats](../../../translated_images/th/understanding-threats.89edeada8a97fc0f.webp)

### งานและคำแนะนำ

**คำอธิบาย:** ผู้โจมตีพยายามเปลี่ยนคำแนะนำหรือเป้าหมายของตัวแทน AI ผ่านการกระตุ้นคำสั่งหรือการจัดการข้อมูลขาเข้า

**การลดความเสี่ยง:** ดำเนินการตรวจสอบความถูกต้องและการกรองข้อมูลขาเข้าเพื่อตรวจจับพรอมต์ที่อาจเป็นอันตรายก่อนที่จะถูกประมวลผลโดยตัวแทน AI เนื่องจากการโจมตีเหล่านี้มักต้องติดต่อกับตัวแทนบ่อยๆ การจำกัดจำนวนรอบสนทนาเป็นอีกวิธีหนึ่งในการป้องกันการโจมตีประเภทนี้

### การเข้าถึงระบบที่สำคัญ

**คำอธิบาย:** หากตัวแทน AI มีการเข้าถึงระบบและบริการที่เก็บข้อมูลที่ละเอียดอ่อน ผู้โจมตีสามารถเจาะการสื่อสารระหว่างตัวแทนและบริการเหล่านี้ได้ อาจเป็นการโจมตีโดยตรงหรือการพยายามโดยอ้อมเพื่อรับข้อมูลเกี่ยวกับระบบเหล่านี้ผ่านตัวแทน

**การลดความเสี่ยง:** ตัวแทน AI ควรมีการเข้าถึงระบบเฉพาะเมื่อต้องการเท่านั้นเพื่อป้องกันการโจมตีประเภทนี้ การสื่อสารระหว่างตัวแทนและระบบควรปลอดภัย การใช้การตรวจสอบสิทธิ์และควบคุมการเข้าถึงเป็นอีกวิธีหนึ่งในการปกป้องข้อมูลนี้

### การโหลดเกินของทรัพยากรและบริการ

**คำอธิบาย:** ตัวแทน AI สามารถเข้าถึงเครื่องมือและบริการต่างๆ เพื่อทำงานให้เสร็จ ผู้โจมตีสามารถใช้ความสามารถนี้โจมตีบริการเหล่านี้โดยส่งคำขอจำนวนมากผ่านตัวแทน AI ซึ่งอาจทำให้ระบบล้มเหลวหรือเกิดค่าใช้จ่ายสูง

**การลดความเสี่ยง:** ใช้นโยบายจำกัดจำนวนคำขอที่ตัวแทน AI สามารถส่งไปยังบริการได้ การจำกัดจำนวนรอบสนทนาและคำขอส่งไปยังตัวแทน AI ของคุณเป็นอีกวิธีป้องกันการโจมตีประเภทนี้

### การปนเปื้อนฐานความรู้

**คำอธิบาย:** การโจมตีประเภทนี้ไม่ได้มุ่งเป้าไปที่ตัวแทน AI โดยตรง แต่เป็นการโจมตีฐานความรู้และบริการอื่นๆ ที่ตัวแทน AI จะใช้ อาจเกี่ยวข้องกับการทำให้ข้อมูลหรือข้อมูลที่ตัวแทน AI ใช้เพื่อทำงานผิดพลาด ส่งผลให้ตอบสนองผิดพลาดหรือมีอคติ

**การลดความเสี่ยง:** ตรวจสอบและยืนยันข้อมูลที่ตัวแทน AI จะใช้ในเวิร์กโฟลว์อย่างสม่ำเสมอ ให้แน่ใจว่าการเข้าถึงข้อมูลเหล่านี้ปลอดภัยและสามารถเปลี่ยนแปลงได้โดยบุคคลที่เชื่อถือได้เท่านั้นเพื่อหลีกเลี่ยงการโจมตีประเภทนี้

### ข้อผิดพลาดแบบเรียงลำดับ

**คำอธิบาย:** ตัวแทน AI เข้าถึงเครื่องมือและบริการต่างๆ เพื่อทำงานให้สำเร็จ ข้อผิดพลาดที่เกิดจากผู้โจมตีอาจทำให้ระบบอื่นที่ตัวแทน AI เชื่อมต่อเกิดความล้มเหลว ทำให้การโจมตีขยายวงกว้างขึ้นและยากต่อการแก้ไข

**การลดความเสี่ยง:** หนึ่งในวิธีป้องกันคือให้ตัวแทน AI ทำงานในสภาพแวดล้อมจำกัด เช่น การทำงานใน Docker container เพื่อลดการโจมตีระบบโดยตรง การสร้างกลไกสำรองและตรรกะการลองทำใหม่เมื่อตัวระบบตอบกลับด้วยข้อผิดพลาดก็เป็นอีกวิธีในการป้องกันความล้มเหลวของระบบขนาดใหญ่

## ระบบผู้ใช้มีส่วนร่วม

อีกวิธีที่มีประสิทธิภาพในการสร้างระบบตัวแทน AI ที่เชื่อถือได้คือการใช้ระบบผู้ใช้มีส่วนร่วม (Human-in-the-loop) ซึ่งสร้างการไหลที่ผู้ใช้สามารถให้คำติชมกับตัวแทนระหว่างการทำงาน ผู้ใช้ทำหน้าที่เป็นตัวแทนในระบบหลายตัว และให้การอนุมัติหรือยุติกระบวนการที่กำลังทำงาน

![Human in The Loop](../../../translated_images/th/human-in-the-loop.5f0068a678f62f4f.webp)

นี่คือโค้ดตัวอย่างที่ใช้ Microsoft Agent Framework เพื่อแสดงแนวคิดนี้ว่าได้ถูกนำไปใช้อย่างไร:

```python
import os
from agent_framework.azure import AzureAIProjectAgentProvider
from azure.identity import AzureCliCredential

# สร้างผู้ให้บริการพร้อมการอนุมัติจากมนุษย์ในกระบวนการ
provider = AzureAIProjectAgentProvider(
    credential=AzureCliCredential(),
)

# สร้างเอเจนต์พร้อมขั้นตอนการอนุมัติจากมนุษย์
response = provider.create_response(
    input="Write a 4-line poem about the ocean.",
    instructions="You are a helpful assistant. Ask for user approval before finalizing.",
)

# ผู้ใช้สามารถตรวจสอบและอนุมัติการตอบกลับได้
print(response.output_text)
user_input = input("Do you approve? (APPROVE/REJECT): ")
if user_input == "APPROVE":
    print("Response approved.")
else:
    print("Response rejected. Revising...")
```

## สรุป

การสร้างตัวแทน AI ที่เชื่อถือได้ต้องการการออกแบบอย่างรอบคอบ มาตรการความปลอดภัยที่เข้มแข็ง และการปรับปรุงอย่างต่อเนื่อง การนำระบบคำสั่งเมตาที่มีโครงสร้างมาใช้ การเข้าใจภัยคุกคามที่เป็นไปได้ และการใช้กลยุทธ์ลดความเสี่ยง สามารถช่วยให้นักพัฒนาสร้างตัวแทน AI ที่ปลอดภัยและมีประสิทธิภาพ นอกจากนี้ การใช้แนวทางผู้ใช้มีส่วนร่วมจะช่วยให้ตัวแทน AI ยังคงสอดคล้องกับความต้องการของผู้ใช้ในขณะที่ลดความเสี่ยง เมื่อ AI ยังคงพัฒนา การรักษาท่าทีเชิงรุกในเรื่องความปลอดภัย ความเป็นส่วนตัว และจริยธรรมจะเป็นกุญแจสำคัญในการสร้างความไว้วางใจและความน่าเชื่อถือในระบบที่ขับเคลื่อนด้วย AI

## ตัวอย่างโค้ด

- [`code_samples/06-system-message-framework.ipynb`](code_samples/06-system-message-framework.ipynb): สาธิตทีละขั้นตอนของโครงสร้างระบบคำสั่งเมตา
- [`code_samples/06-human-in-the-loop.ipynb`](code_samples/06-human-in-the-loop.ipynb): ประตูอนุมัติก่อนดำเนินการ การจัดระดับความเสี่ยง และการบันทึกตรวจสอบสำหรับตัวแทนที่เชื่อถือได้

### มีคำถามเพิ่มเติมเกี่ยวกับการสร้างตัวแทน AI ที่เชื่อถือได้ไหม?

เข้าร่วม [Microsoft Foundry Discord](https://aka.ms/ai-agents/discord) เพื่อพบปะผู้เรียนอื่นๆ เข้าร่วมชั่วโมงทำงาน และรับคำตอบสำหรับคำถามเกี่ยวกับตัวแทน AI ของคุณ

## แหล่งข้อมูลเพิ่มเติม

- <a href="https://learn.microsoft.com/azure/ai-studio/responsible-use-of-ai-overview" target="_blank">ภาพรวมของ AI ที่รับผิดชอบ</a>
- <a href="https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai" target="_blank">การประเมินโมเดล AI สร้างสรรค์และแอปพลิเคชัน AI</a>
- <a href="https://learn.microsoft.com/azure/ai-services/openai/concepts/system-message?context=%2Fazure%2Fai-studio%2Fcontext%2Fcontext&tabs=top-techniques" target="_blank">ข้อความระบบความปลอดภัย</a>
- <a href="https://blogs.microsoft.com/wp-content/uploads/prod/sites/5/2022/06/Microsoft-RAI-Impact-Assessment-Template.pdf?culture=en-us&country=us" target="_blank">เทมเพลตการประเมินความเสี่ยง</a>

## บทเรียนก่อนหน้า

[Agentic RAG](../05-agentic-rag/README.md)

## บทเรียนถัดไป

[แพทเทิร์นการออกแบบวางแผน](../07-planning-design/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ปฏิเสธความรับผิดชอบ**:
เอกสารนี้ได้รับการแปลโดยใช้บริการแปลภาษา AI [Co-op Translator](https://github.com/Azure/co-op-translator) ขณะที่เราพยายามให้ความถูกต้อง โปรดทราบว่าการแปลโดยอัตโนมัติอาจมีข้อผิดพลาดหรือความไม่ถูกต้อง เอกสารต้นฉบับในภาษาต้นทางควรถูกพิจารณาเป็นแหล่งข้อมูลที่เชื่อถือได้ สำหรับข้อมูลที่สำคัญ แนะนำให้ใช้การแปลโดยมนุษย์มืออาชีพ เราไม่รับผิดชอบต่อความเข้าใจผิดหรือการตีความที่ผิดพลาดที่เกิดขึ้นจากการใช้การแปลนี้
<!-- CO-OP TRANSLATOR DISCLAIMER END -->