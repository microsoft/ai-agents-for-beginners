# تطوير خدمة وكيل Microsoft Foundry

في هذا التمرين، تستخدم أدوات خدمة وكيل Microsoft Foundry في [بوابة Microsoft Foundry](https://ai.azure.com/?WT.mc_id=academic-105485-koreyst) لإنشاء وكيل لحجز الرحلات الجوية. سيتمكن الوكيل من التفاعل مع المستخدمين وتزويدهم بمعلومات حول الرحلات.

## المتطلبات الأساسية

لإكمال هذا التمرين، تحتاج إلى ما يلي:
1. حساب Azure مع اشتراك نشط. [إنشاء حساب مجانًا](https://azure.microsoft.com/free/?WT.mc_id=academic-105485-koreyst).
2. تحتاج إلى أذونات لإنشاء محور Microsoft Foundry أو أن يكون لديك واحد تم إنشاؤه لك.
    - إذا كان دورك هو المساهم أو المالك، يمكنك اتباع الخطوات في هذا البرنامج التعليمي.

## إنشاء محور Microsoft Foundry

> **ملاحظة:** كان يُعرف Microsoft Foundry سابقًا باسم Azure AI Studio.

1. اتبع هذه الإرشادات من منشور مدونة [Microsoft Foundry](https://learn.microsoft.com/en-us/azure/ai-studio/?WT.mc_id=academic-105485-koreyst) لإنشاء محور Microsoft Foundry.
2. عندما يتم إنشاء مشروعك، أغلق أي نصائح معروضة وراجع صفحة المشروع في بوابة Microsoft Foundry، والتي يجب أن تبدو مشابهة للصورة التالية:

    ![Microsoft Foundry Project](../../../translated_images/ar/azure-ai-foundry.88d0c35298348c2f.webp)

## نشر نموذج

1. في الجزء الأيسر الخاص بمشروعك، في قسم **الأصول الخاصة بي**، حدد صفحة **النماذج + نقاط النهاية**.
2. في صفحة **النماذج + نقاط النهاية**، في علامة التبويب **نشر النماذج**، في قائمة **+ نشر نموذج**، اختر **نشر نموذج أساسي**.
3. ابحث عن نموذج `gpt-5-mini` في القائمة، ثم حدده وأكد عليه.

    > **ملاحظة**: تقليل TPM يساعد في تجنب الإفراط في استخدام الحصة المتاحة في الاشتراك الذي تستخدمه.

    ![Model Deployed](../../../translated_images/ar/model-deployment.3749c53fb81e18fd.webp)

## إنشاء وكيل

الآن بعد أن نشرت نموذجًا، يمكنك إنشاء وكيل. الوكيل هو نموذج ذكاء اصطناعي محادثي يمكن استخدامه للتفاعل مع المستخدمين.

1. في الجزء الأيسر الخاص بمشروعك، في قسم **البناء والتخصيص**، حدد صفحة **الوكلاء**.
2. انقر فوق **+ إنشاء وكيل** لإنشاء وكيل جديد. ضمن مربع الحوار **إعداد الوكيل**:
    - أدخل اسمًا للوكيل، مثل `FlightAgent`.
    - تأكد من تحديد نشر نموذج `gpt-5-mini` الذي أنشأته سابقًا
    - قم بتعيين **التعليمات** حسب الموجه الذي تريد أن يتبعه الوكيل. إليك مثالًا:
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
> لموجه تفصيلي، يمكنك مراجعة [هذا المستودع](https://github.com/ShivamGoyal03/RoamMind) لمزيد من المعلومات.
    
> علاوة على ذلك، يمكنك إضافة **قاعدة المعرفة** و **الإجراءات** لتعزيز قدرات الوكيل لتقديم المزيد من المعلومات وأداء المهام الآلية بناءً على طلبات المستخدم. بالنسبة لهذا التمرين، يمكنك تخطي هذه الخطوات.
    
![Agent Setup](../../../translated_images/ar/agent-setup.9bbb8755bf5df672.webp)

3. لإنشاء وكيل متعدد الذكاء الاصطناعي جديد، ببساطة انقر فوق **وكيل جديد**. ثم سيتم عرض الوكيل الجديد في صفحة الوكلاء.


## اختبار الوكيل

بعد إنشاء الوكيل، يمكنك اختباره لمعرفة كيف يرد على استفسارات المستخدمين في ساحة تجربة بوابة Microsoft Foundry.

1. في أعلى لوحة **الإعداد** الخاصة بوكيلك، اختر **التجريب في الساحة**.
2. في لوحة **الساحة**، يمكنك التفاعل مع الوكيل عن طريق كتابة الاستفسارات في نافذة الدردشة. على سبيل المثال، يمكنك طلب من الوكيل البحث عن رحلات من سياتل إلى نيويورك في اليوم الثامن والعشرين.

    > **ملاحظة**: قد لا يقدم الوكيل ردودًا دقيقة، لأن هذا التمرين لا يستخدم بيانات في الوقت الحقيقي. الغرض هو اختبار قدرة الوكيل على فهم والرد على استفسارات المستخدم بناءً على التعليمات المقدمة.

    ![Agent Playground](../../../translated_images/ar/agent-playground.dc146586de715010.webp)

3. بعد اختبار الوكيل، يمكنك تخصيصه بشكل أكبر عن طريق إضافة المزيد من النوايا وبيانات التدريب والإجراءات لتعزيز قدراته.

## تنظيف الموارد

عند الانتهاء من اختبار الوكيل، يمكنك حذفه لتجنب تكبد تكاليف إضافية.
1. افتح [بوابة Azure](https://portal.azure.com) وعرض محتويات مجموعة الموارد حيث نشرت الموارد الخاصة بالمحور المستخدم في هذا التمرين.
2. في شريط الأدوات، اختر **حذف مجموعة الموارد**.
3. أدخل اسم مجموعة الموارد وأكد رغبتك في حذفها.

## الموارد

- [توثيق Microsoft Foundry](https://learn.microsoft.com/en-us/azure/ai-studio/?WT.mc_id=academic-105485-koreyst)
- [بوابة Microsoft Foundry](https://ai.azure.com/?WT.mc_id=academic-105485-koreyst)
- [البدء مع Microsoft Foundry](https://techcommunity.microsoft.com/blog/educatordeveloperblog/getting-started-with-azure-ai-studio/4095602?WT.mc_id=academic-105485-koreyst)
- [أساسيات وكلاء الذكاء الاصطناعي على Azure](https://learn.microsoft.com/en-us/training/modules/ai-agent-fundamentals/?WT.mc_id=academic-105485-koreyst)
- [Azure AI Discord](https://aka.ms/AzureAI/Discord)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**تنويه**:
تمت ترجمة هذا المستند باستخدام خدمة الترجمة بالذكاء الاصطناعي [Co-op Translator](https://github.com/Azure/co-op-translator). بينما نسعى للدقة، يرجى العلم أن الترجمات الآلية قد تحتوي على أخطاء أو عدم دقة. يجب اعتبار المستند الأصلي بلغته الأصلية المصدر الرسمي والمعتمد. للمعلومات الهامة، يُنصح بالاستعانة بترجمة بشرية محترفة. نحن غير مسؤولين عن أي سوء فهم أو تفسير ناتج عن استخدام هذه الترجمة.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->