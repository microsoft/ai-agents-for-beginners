# การพัฒนาบริการเอเจนต์ Microsoft Foundry

ในแบบฝึกหัดนี้ คุณจะใช้เครื่องมือ Microsoft Foundry Agent Service ใน [Microsoft Foundry portal](https://ai.azure.com/?WT.mc_id=academic-105485-koreyst) เพื่อสร้างเอเจนต์สำหรับการจองเที่ยวบิน เอเจนต์นี้จะสามารถโต้ตอบกับผู้ใช้และให้ข้อมูลเกี่ยวกับเที่ยวบินได้

## ข้อกำหนดเบื้องต้น

เพื่อทำแบบฝึกหัดนี้ให้เสร็จสมบูรณ์ คุณต้องมีสิ่งต่อไปนี้:
1. บัญชี Azure ที่มีการสมัครใช้งานที่ใช้งานอยู่ [สร้างบัญชีฟรี](https://azure.microsoft.com/free/?WT.mc_id=academic-105485-koreyst)
2. คุณต้องได้รับสิทธิ์ในการสร้าง Microsoft Foundry hub หรือมีคนสร้างให้คุณ
    - หากบทบาทของคุณคือ Contributor หรือ Owner คุณสามารถทำตามขั้นตอนในบทเรียนนี้ได้

## การสร้าง Microsoft Foundry hub

> **หมายเหตุ:** Microsoft Foundry เคยถูกเรียกว่า Azure AI Studio

1. ทำตามแนวทางจากโพสต์บล็อก [Microsoft Foundry](https://learn.microsoft.com/en-us/azure/ai-studio/?WT.mc_id=academic-105485-koreyst) สำหรับการสร้าง Microsoft Foundry hub
2. เมื่อสร้างโครงการแล้ว ให้ปิดคำแนะนำที่แสดงและตรวจสอบหน้าโครงการใน Microsoft Foundry portal ซึ่งควรจะแสดงเหมือนภาพตัวอย่างต่อไปนี้:

    ![Microsoft Foundry Project](../../../translated_images/th/azure-ai-foundry.88d0c35298348c2f.webp)

## การปรับใช้โมเดล

1. ในแผงด้านซ้ายสำหรับโครงการของคุณ ในส่วน **My assets** ให้เลือกหน้า **Models + endpoints**
2. ในหน้า **Models + endpoints** ภายใต้แท็บ **Model deployments** ในเมนู **+ Deploy model** ให้เลือก **Deploy base model**
3. ค้นหาโมเดล `gpt-5-mini` ในรายการ จากนั้นเลือกและยืนยัน

    > **หมายเหตุ**: การลด TPM ช่วยป้องกันการใช้งานเกินโควต้าในการสมัครใช้งานที่คุณกำลังใช้งาน

    ![Model Deployed](../../../translated_images/th/model-deployment.3749c53fb81e18fd.webp)

## การสร้างเอเจนต์

ตอนนี้ที่คุณได้ปรับใช้โมเดลแล้ว คุณสามารถสร้างเอเจนต์ได้ เอเจนต์คือโมเดล AI แบบสนทนาที่ใช้โต้ตอบกับผู้ใช้ได้

1. ในแผงด้านซ้ายสำหรับโครงการของคุณ ในส่วน **Build & Customize** ให้เลือกหน้า **Agents**
2. คลิก **+ Create agent** เพื่อสร้างเอเจนต์ใหม่ ในกล่องโต้ตอบ **Agent Setup**:
    - ป้อนชื่อสำหรับเอเจนต์ เช่น `FlightAgent`
    - ตรวจสอบให้แน่ใจว่าได้เลือกการปรับใช้โมเดล `gpt-5-mini` ที่คุณสร้างไว้ก่อนหน้า
    - ตั้งค่า **Instructions** ตามคำสั่งที่คุณต้องการให้เอเจนต์ปฏิบัติตาม ตัวอย่างเช่น:
    ```
    You are FlightAgent, a virtual assistant specialized in handling flight-related queries. Your role includes assisting users with searching for flights, retrieving flight details, checking seat availability, and providing real-time flight status. Follow the instructions below to ensure clarity and effectiveness in your responses:

    ### Task Instructions:
    1. **Recognizing Intent**:
       - Identify the user's intent based on their request, focusing on one of the following categories:
         - Searching for flights
         - Retrieving flight details using a flight ID
         - Checking seat availability for a specified flight
         - Providing real-time flight status using a flight number
       - If the intent is unclear, politely ask users to clarify or provide more details.
        
    2. **Processing Requests**:
        - Depending on the identified intent, perform the required task:
        - For flight searches: Request details such as origin, destination, departure date, and optionally return date.
        - For flight details: Request a valid flight ID.
        - For seat availability: Request the flight ID and date and validate inputs.
        - For flight status: Request a valid flight number.
        - Perform validations on provided data (e.g., formats of dates, flight numbers, or IDs). If the information is incomplete or invalid, return a friendly request for clarification.

    3. **Generating Responses**:
    - Use a tone that is friendly, concise, and supportive.
    - Provide clear and actionable suggestions based on the output of each task.
    - If no data is found or an error occurs, explain it to the user gently and offer alternative actions (e.g., refine search, try another query).
    
    ```
> [!NOTE]
> สำหรับคำสั่งที่ละเอียด คุณสามารถตรวจสอบ [ที่เก็บนี้](https://github.com/ShivamGoyal03/RoamMind) เพื่อข้อมูลเพิ่มเติม
    
> นอกจากนี้ คุณสามารถเพิ่ม **Knowledge Base** และ **Actions** เพื่อเพิ่มขีดความสามารถของเอเจนต์ในการให้ข้อมูลเพิ่มเติมและทำงานอัตโนมัติตามคำขอของผู้ใช้ สำหรับแบบฝึกหัดนี้ คุณสามารถข้ามขั้นตอนเหล่านี้ได้
    
![Agent Setup](../../../translated_images/th/agent-setup.9bbb8755bf5df672.webp)

3. หากต้องการสร้างเอเจนต์ AI หลายตัวใหม่ ให้คลิก **New Agent** เอเจนต์ที่สร้างใหม่จะปรากฏในหน้าหน้า Agents


## การทดสอบเอเจนต์

หลังจากสร้างเอเจนต์แล้ว คุณสามารถทดสอบดูว่าเอเจนต์ตอบสนองต่อคำถามของผู้ใช้อย่างไรใน Microsoft Foundry portal playground

1. ที่ด้านบนของแผง **Setup** สำหรับเอเจนต์ของคุณ ให้เลือก **Try in playground**
2. ในแผง **Playground** คุณสามารถโต้ตอบกับเอเจนต์โดยพิมพ์คำถามลงในหน้าต่างแชท ตัวอย่างเช่น คุณสามารถขอให้เอเจนต์ค้นหาเที่ยวบินจาก Seattle ไป New York ในวันที่ 28

    > **หมายเหตุ**: เอเจนต์อาจไม่ให้คำตอบที่ถูกต้อง เนื่องจากไม่มีการใช้ข้อมูลเรียลไทม์ในแบบฝึกหัดนี้ จุดประสงค์คือเพื่อทดสอบความสามารถของเอเจนต์ในการเข้าใจและตอบสนองคำถามของผู้ใช้ตามคำสั่งที่กำหนด

    ![Agent Playground](../../../translated_images/th/agent-playground.dc146586de715010.webp)

3. หลังทดสอบเอเจนต์ คุณสามารถปรับแต่งเพิ่มเติมโดยเพิ่มเจตนา ข้อมูลฝึกสอน และการกระทำ เพื่อเพิ่มความสามารถให้มากขึ้น

## การลบทรัพยากร

เมื่อคุณทดสอบเอเจนต์เสร็จแล้ว คุณสามารถลบเอเจนต์เพื่อหลีกเลี่ยงค่าใช้จ่ายเพิ่มเติม
1. เปิด [Azure portal](https://portal.azure.com) และดูเนื้อหาของ resource group ที่คุณใช้ปรับใช้ hub ในการฝึกหัดนี้
2. ที่แถบเครื่องมือ ให้เลือก **Delete resource group**
3. ป้อนชื่อ resource group และยืนยันว่าคุณต้องการลบ

## แหล่งข้อมูล

- [เอกสาร Microsoft Foundry](https://learn.microsoft.com/en-us/azure/ai-studio/?WT.mc_id=academic-105485-koreyst)
- [Microsoft Foundry portal](https://ai.azure.com/?WT.mc_id=academic-105485-koreyst)
- [เริ่มต้นใช้งาน Microsoft Foundry](https://techcommunity.microsoft.com/blog/educatordeveloperblog/getting-started-with-azure-ai-studio/4095602?WT.mc_id=academic-105485-koreyst)
- [พื้นฐานของเอเจนต์ AI บน Azure](https://learn.microsoft.com/en-us/training/modules/ai-agent-fundamentals/?WT.mc_id=academic-105485-koreyst)
- [Azure AI Discord](https://aka.ms/AzureAI/Discord)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ปฏิเสธความรับผิดชอบ**:
เอกสารนี้ได้รับการแปลโดยใช้บริการแปลภาษา AI [Co-op Translator](https://github.com/Azure/co-op-translator) ขณะที่เราพยายามให้ความถูกต้อง โปรดทราบว่าการแปลโดยอัตโนมัติอาจมีข้อผิดพลาดหรือความไม่ถูกต้อง เอกสารต้นฉบับในภาษาต้นทางควรถูกพิจารณาเป็นแหล่งข้อมูลที่เชื่อถือได้ สำหรับข้อมูลที่สำคัญ แนะนำให้ใช้การแปลโดยมนุษย์มืออาชีพ เราไม่รับผิดชอบต่อความเข้าใจผิดหรือการตีความที่ผิดพลาดที่เกิดขึ้นจากการใช้การแปลนี้
<!-- CO-OP TRANSLATOR DISCLAIMER END -->