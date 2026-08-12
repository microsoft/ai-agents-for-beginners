[![Trustworthy AI Agents](../../../translated_images/th/lesson-6-thumbnail.a58ab36c099038d4.webp)](https://youtu.be/iZKkMEGBCUQ?si=Q-kEbcyHUMPoHp8L)

> _(คลิกที่รูปภาพด้านบนเพื่อดูวิดีโอของบทเรียนนี้)_

# การสร้างเอเย่นต์ AI ที่น่าเชื่อถือ

## บทนำ

บทเรียนนี้จะครอบคลุม:

- วิธีการสร้างและใช้งานเอเย่นต์ AI ที่ปลอดภัยและมีประสิทธิภาพ
- ข้อควรพิจารณาด้านความปลอดภัยที่สำคัญเมื่อพัฒนาเอเย่นต์ AI
- วิธีการรักษาข้อมูลและความเป็นส่วนตัวของผู้ใช้เมื่อพัฒนาเอเย่นต์ AI

## เป้าหมายการเรียนรู้

หลังจากทำบทเรียนนี้เสร็จ คุณจะทราบวิธี:

- ระบุและลดความเสี่ยงเมื่อต้องสร้างเอเย่นต์ AI
- ใช้มาตรการรักษาความปลอดภัยเพื่อให้แน่ใจว่าการจัดการข้อมูลและการเข้าถึงเป็นไปอย่างเหมาะสม
- สร้างเอเย่นต์ AI ที่รักษาความเป็นส่วนตัวของข้อมูลและมอบประสบการณ์ผู้ใช้ที่มีคุณภาพ

## ความปลอดภัย

ก่อนอื่นเรามาดูการสร้างแอปพลิเคชันเอเย่นต์ที่ปลอดภัย ความปลอดภัยหมายถึงว่าเอเย่นต์ AI ทำงานตามที่ออกแบบไว้ ในฐานะผู้สร้างแอปพลิเคชันเอเย่นต์ เรามีวิธีการและเครื่องมือที่ช่วยเพิ่มความปลอดภัยสูงสุด:

### การสร้างกรอบการทำงานข้อความระบบ

หากคุณเคยสร้างแอป AI โดยใช้โมเดลภาษาขนาดใหญ่ (LLMs) คุณจะรู้ถึงความสำคัญของการออกแบบการตั้งค่าข้อความระบบหรือโปรมต์ระบบที่แข็งแกร่ง โปรมต์เหล่านี้กำหนดกฎเมตา คำแนะนำ และแนวทางว่าการโต้ตอบระหว่าง LLM กับผู้ใช้และข้อมูลจะเป็นอย่างไร

สำหรับเอเย่นต์ AI โปรมต์ระบบมีความสำคัญยิ่งขึ้น เพราะเอเย่นต์ AI จำเป็นต้องมีคำแนะนำที่เฉพาะเจาะจงมากเพื่อทำงานตามที่เรากำหนดไว้

เพื่อสร้างโปรมต์ระบบที่ขยายได้ เราสามารถใช้กรอบการทำงานข้อความระบบสำหรับการสร้างเอเย่นต์หนึ่งตัวหรือหลายตัวในแอปพลิเคชันของเรา:

![Building a System Message Framework](../../../translated_images/th/system-message-framework.3a97368c92d11d68.webp)

#### ขั้นตอนที่ 1: สร้าง Meta System Message

Meta prompt จะใช้โดย LLM เพื่อสร้างโปรมต์ระบบสำหรับเอเย่นต์ที่เราสร้าง เราออกแบบเป็นแม่แบบเพื่อให้สามารถสร้างเอเย่นต์หลายตัวได้อย่างมีประสิทธิภาพหากจำเป็น

นี่คือตัวอย่างของ meta system message ที่เราจะให้กับ LLM:

```plaintext
You are an expert at creating AI agent assistants. 
You will be provided a company name, role, responsibilities and other
information that you will use to provide a system prompt for.
To create the system prompt, be descriptive as possible and provide a structure that a system using an LLM can better understand the role and responsibilities of the AI assistant. 
```

#### ขั้นตอนที่ 2: สร้างโปรมต์พื้นฐาน

ขั้นตอนถัดไปคือการสร้างโปรมต์พื้นฐานเพื่ออธิบายเอเย่นต์ AI คุณควรรวมบทบาทของเอเย่นต์ งานที่เอเย่นต์ต้องทำ และความรับผิดชอบอื่น ๆ ของเอเย่นต์ด้วย

นี่คือตัวอย่าง:

```plaintext
You are a travel agent for Contoso Travel that is great at booking flights for customers. To help customers you can perform the following tasks: lookup available flights, book flights, ask for preferences in seating and times for flights, cancel any previously booked flights and alert customers on any delays or cancellations of flights.  
```

#### ขั้นตอนที่ 3: ให้ Basic System Message กับ LLM

ตอนนี้เราสามารถปรับปรุงข้อความระบบนี้โดยให้ meta system message เป็นข้อความระบบและข้อความระบบพื้นฐานของเรา

สิ่งนี้จะสร้างข้อความระบบที่ออกแบบมาอย่างดีกว่าสำหรับแนะนำเอเย่นต์ AI ของเรา:

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

#### ขั้นตอนที่ 4: ปรับปรุงและพัฒนา

คุณค่าของกรอบการทำงานข้อความระบบนี้คือความสามารถในการเพิ่มขนาดการสร้างข้อความระบบจากหลายเอเย่นต์ให้สะดวกขึ้น รวมถึงการปรับปรุงข้อความระบบของคุณเมื่อเวลาผ่านไป แทบจะไม่มีข้อความระบบที่สมบูรณ์แบบในการใช้งานครั้งแรก การทำการปรับแต่งเล็กน้อยและพัฒนาข้อความระบบพื้นฐานแล้วรันผ่านระบบจะช่วยให้คุณเปรียบเทียบและประเมินผลลัพธ์ได้

## การเข้าใจภัยคุกคาม

เพื่อสร้างเอเย่นต์ AI ที่น่าเชื่อถือ สิ่งสำคัญคือต้องเข้าใจและลดความเสี่ยงและภัยคุกคามต่อเอเย่นต์ AI ของคุณ มาดูเพียงบางภัยคุกคามต่อเอเย่นต์ AI และวิธีที่คุณสามารถวางแผนและเตรียมตัวเพื่อรับมือพวกเขาได้ดีขึ้น

![Understanding Threats](../../../translated_images/th/understanding-threats.89edeada8a97fc0f.webp)

### งานและคำสั่ง

**คำอธิบาย:** ผู้โจมตีพยายามเปลี่ยนคำสั่งหรือเป้าหมายของเอเย่นต์ AI ผ่านการตั้งโปรมต์หรือการจัดการอินพุต

**การลดความเสี่ยง**: ดำเนินการตรวจสอบความถูกต้องและกรองอินพุตเพื่อตรวจจับโปรมต์ที่อาจเป็นอันตรายก่อนที่เอเย่นต์ AI จะประมวลผล เนื่องจากการโจมตีประเภทนี้มักต้องการการโต้ตอบบ่อยครั้งกับเอเย่นต์ การจำกัดจำนวนรอบในการสนทนาจึงเป็นอีกวิธีหนึ่งที่ช่วยป้องกันการโจมตีเหล่านี้

### การเข้าถึงระบบสำคัญ

**คำอธิบาย:** หากเอเย่นต์ AI สามารถเข้าถึงระบบและบริการที่เก็บข้อมูลสำคัญได้ ผู้โจมตีสามารถเจาะเข้าไปในการสื่อสารระหว่างเอเย่นต์และบริการเหล่านี้ได้ การโจมตีเหล่านี้อาจเป็นการโจมตีโดยตรงหรือพยายามแสวงหาข้อมูลเกี่ยวกับระบบเหล่านี้ผ่านเอเย่นต์

**การลดความเสี่ยง:** เอเย่นต์ AI ควรเข้าถึงระบบตามความจำเป็นเท่านั้นเพื่อป้องกันการโจมตีประเภทนี้ การสื่อสารระหว่างเอเย่นต์และระบบควรปลอดภัย อีกทั้งควรมีการใช้งานระบบการพิสูจน์ตัวตนและการควบคุมการเข้าถึงเพื่อปกป้องข้อมูลนี้

### การโหลดเกินทรัพยากรและบริการ

**คำอธิบาย:** เอเย่นต์ AI สามารถเข้าถึงเครื่องมือและบริการต่าง ๆ เพื่อทำงานให้เสร็จ ผู้โจมตีสามารถใช้ความสามารถนี้โจมตีบริการเหล่านี้โดยส่งคำขอจำนวนมากผ่านเอเย่นต์ AI ซึ่งอาจทำให้ระบบล้มเหลวหรือเกิดค่าใช้จ่ายสูง

**การลดความเสี่ยง:** ใช้นโยบายจำกัดจำนวนคำขอที่เอเย่นต์ AI สามารถส่งไปยังบริการ จำกัดจำนวนรอบการสนทนาและคำขอไปยังเอเย่นต์ AI เป็นอีกวิธีหนึ่งในการป้องกันการโจมตีเหล่านี้

### การปนเปื้อนฐานความรู้

**คำอธิบาย:** การโจมตีประเภทนี้ไม่ได้มุ่งเป้าโดยตรงที่เอเย่นต์ AI แต่จะมุ่งเป้าไปที่ฐานความรู้และบริการอื่น ๆ ที่เอเย่นต์ AI ใช้ อาจรวมถึงการทำให้ข้อมูลหรือข้อมูลที่เอเย่นต์ AI ใช้ในการทำงานเสียหาย ส่งผลให้เกิดการตอบสนองที่มีอคติหรือไม่ตั้งใจต่อลูกค้า

**การลดความเสี่ยง:** ตรวจสอบและยืนยันข้อมูลที่เอเย่นต์ AI จะใช้ในเวิร์กโฟลว์อย่างสม่ำเสมอ ตรวจสอบให้มั่นใจว่าการเข้าถึงข้อมูลนี้ปลอดภัยและสามารถเปลี่ยนแปลงได้เฉพาะโดยบุคคลที่เชื่อถือได้เท่านั้นเพื่อหลีกเลี่ยงการโจมตีประเภทนี้

### ความผิดพลาดที่ซ้ำลามวงกว้าง

**คำอธิบาย:** เอเย่นต์ AI เข้าถึงเครื่องมือและบริการหลากหลายเพื่อทำงานให้เสร็จ ความผิดพลาดที่เกิดจากผู้โจมตีอาจทำให้ระบบอื่น ๆ ที่เอเย่นต์ AI เชื่อมต่อเกิดความล้มเหลว ทำให้การโจมตีแพร่ขยายและยากที่จะแก้ไข

**การลดความเสี่ยง:** วิธีหนึ่งคือให้เอเย่นต์ AI ทำงานในสภาพแวดล้อมจำกัด เช่น การทำงานในคอนเทนเนอร์ Docker เพื่อป้องกันการโจมตีระบบโดยตรง สร้างกลไกสำรองและตรรกะการลองใหม่เมื่อระบบบางอย่างตอบกลับด้วยข้อผิดพลาดเป็นอีกวิธีหนึ่งป้องกันความล้มเหลวของระบบขนาดใหญ่

## มนุษย์ในวงจร

อีกวิธีที่มีประสิทธิภาพในการสร้างระบบเอเย่นต์ AI ที่น่าเชื่อถือคือการใช้มนุษย์ในวงจร (Human-in-the-loop) ซึ่งสร้างกระบวนการที่ผู้ใช้สามารถให้ข้อเสนอแนะแก่เอเย่นต์ระหว่างที่ทำงาน ผู้ใช้จะทำหน้าที่เหมือนเอเย่นต์ในระบบเอเย่นต์หลายตัวและสามารถอนุมัติหรือยกเลิกกระบวนการที่กำลังดำเนินอยู่ได้

![Human in The Loop](../../../translated_images/th/human-in-the-loop.5f0068a678f62f4f.webp)

นี่คือตัวอย่างโค้ดโดยใช้ Microsoft Agent Framework เพื่อแสดงวิธีการใช้งานแนวคิดนี้:

```python
import os
from agent_framework.foundry import FoundryChatClient
from azure.identity import AzureCliCredential

# สร้างผู้ให้บริการพร้อมการอนุมัติจากมนุษย์ในขั้นตอน
provider = FoundryChatClient(
    project_endpoint=os.environ["AZURE_AI_PROJECT_ENDPOINT"],
    model=os.environ["AZURE_AI_MODEL_DEPLOYMENT_NAME"],
    credential=AzureCliCredential(),
)

# สร้างผู้ช่วยพร้อมขั้นตอนการอนุมัติจากมนุษย์
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

## สรุป

การสร้างเอเย่นต์ AI ที่น่าเชื่อถือจำเป็นต้องมีการออกแบบอย่างระมัดระวัง มีมาตรการรักษาความปลอดภัยที่เข้มแข็ง และปรับปรุงอย่างต่อเนื่อง โดยการใช้ระบบการตั้งค่าเมต้าโปรมต์ที่มีโครงสร้าง เข้าใจภัยคุกคามที่อาจเกิดขึ้น และนำกลยุทธ์ลดความเสี่ยงมาใช้ นักพัฒนาสามารถสร้างเอเย่นต์ AI ที่ทั้งปลอดภัยและมีประสิทธิภาพ นอกจากนี้ การผสานมนุษย์ในวงจรช่วยให้เอเย่นต์ AI ยังคงสอดคล้องกับความต้องการของผู้ใช้ในขณะที่ลดความเสี่ยง เมื่อ AI ยังคงพัฒนา การรักษาท่าทีเชิงรุกด้านความปลอดภัย ความเป็นส่วนตัว และจริยธรรมจะเป็นกุญแจสำคัญในการสร้างความไว้วางใจและความน่าเชื่อถือในระบบที่ขับเคลื่อนด้วย AI

## ตัวอย่างโค้ด

- [`code_samples/06-system-message-framework.ipynb`](code_samples/06-system-message-framework.ipynb): สาธิตขั้นตอนการทำงานของกรอบการทำงานเมต้า-โปรมต์ข้อความระบบ
- [`code_samples/06-human-in-the-loop.ipynb`](code_samples/06-human-in-the-loop.ipynb): เกตอนุมัติก่อนดำเนินการ การจัดระดับความเสี่ยง และการบันทึกการตรวจสอบสำหรับเอเย่นต์ที่น่าเชื่อถือ

### มีคำถามเพิ่มเติมเกี่ยวกับการสร้างเอเย่นต์ AI ที่น่าเชื่อถือไหม?

เข้าร่วม [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D) เพื่อพบปะผู้เรียนอื่น ๆ เข้าร่วมชั่วโมงทำงาน และถามคำถามเกี่ยวกับเอเย่นต์ AI ของคุณ

## แหล่งข้อมูลเพิ่มเติม

- <a href="https://learn.microsoft.com/azure/ai-studio/responsible-use-of-ai-overview" target="_blank">ภาพรวม AI ที่รับผิดชอบ</a>
- <a href="https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai" target="_blank">การประเมินโมเดล AI สร้างสรรค์และแอป AI</a>
- <a href="https://learn.microsoft.com/azure/ai-services/openai/concepts/system-message?context=%2Fazure%2Fai-studio%2Fcontext%2Fcontext&tabs=top-techniques" target="_blank">ข้อความระบบความปลอดภัย</a>
- <a href="https://blogs.microsoft.com/wp-content/uploads/prod/sites/5/2022/06/Microsoft-RAI-Impact-Assessment-Template.pdf?culture=en-us&country=us" target="_blank">แม่แบบการประเมินความเสี่ยง</a>

## บทเรียนที่แล้ว

[Agentic RAG](../05-agentic-rag/README.md)

## บทเรียนถัดไป

[แบบแผนการวางแผน](../07-planning-design/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ปฏิเสธความรับผิดชอบ**:
เอกสารนี้ได้รับการแปลโดยใช้บริการแปลภาษา AI [Co-op Translator](https://github.com/Azure/co-op-translator) ขณะที่เราพยายามให้ความถูกต้อง โปรดทราบว่าการแปลโดยอัตโนมัติอาจมีข้อผิดพลาดหรือความไม่ถูกต้อง เอกสารต้นฉบับในภาษาต้นทางควรถูกพิจารณาเป็นแหล่งข้อมูลที่เชื่อถือได้ สำหรับข้อมูลที่สำคัญ แนะนำให้ใช้การแปลโดยมนุษย์มืออาชีพ เราไม่รับผิดชอบต่อความเข้าใจผิดหรือการตีความที่ผิดพลาดที่เกิดขึ้นจากการใช้การแปลนี้
<!-- CO-OP TRANSLATOR DISCLAIMER END -->