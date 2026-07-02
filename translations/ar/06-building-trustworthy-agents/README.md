[![وكلاء الذكاء الاصطناعي الموثوق بهم](../../../translated_images/ar/lesson-6-thumbnail.a58ab36c099038d4.webp)](https://youtu.be/iZKkMEGBCUQ?si=Q-kEbcyHUMPoHp8L)

> _(انقر على الصورة أعلاه لعرض فيديو هذا الدرس)_

# بناء وكلاء ذكاء اصطناعي موثوق بهم

## مقدمة

سيغطي هذا الدرس:

- كيفية بناء ونشر وكلاء ذكاء اصطناعي آمنين وفعّالين
- اعتبارات أمنية مهمة عند تطوير وكلاء الذكاء الاصطناعي.
- كيفية الحفاظ على خصوصية البيانات والمستخدم عند تطوير وكلاء الذكاء الاصطناعي.

## أهداف التعلم

بعد إكمال هذا الدرس، ستعرف كيف:

- تحديد وتخفيف المخاطر عند إنشاء وكلاء ذكاء اصطناعي.
- تنفيذ تدابير أمنية لضمان إدارة مناسبة للبيانات والوصول.
- إنشاء وكلاء ذكاء اصطناعي يحافظون على خصوصية البيانات ويوفرون تجربة مستخدم ذات جودة.

## السلامة

لنلقِ نظرة أولاً على بناء تطبيقات وكيلة آمنة. تعني السلامة أن يقوم وكيل الذكاء الاصطناعي بأداء وظيفته كما هو مصمم. كمنشئين لتطبيقات وكيلة، لدينا طرق وأدوات لتعظيم السلامة:

### بناء إطار عمل لرسائل النظام

إذا سبق لك بناء تطبيق ذكاء اصطناعي يستخدم نماذج اللغة الكبيرة (LLMs)، فأنت تعرف أهمية تصميم موجه نظام قوي أو رسالة نظام. تحدد هذه الرسائل القواعد العامة والتعليمات والإرشادات لكيفية تفاعل نموذج اللغة الكبير مع المستخدم والبيانات.

في حالة وكلاء الذكاء الاصطناعي، فإن موجه النظام يصبح أكثر أهمية لأن الوكلاء يحتاجون إلى تعليمات محددة جداً لإكمال المهام التي صممناها لهم.

لإنشاء موجهات نظام قابلة للتوسع، يمكننا استخدام إطار عمل رسالة النظام لبناء واحد أو أكثر من الوكلاء في تطبيقنا:

![بناء إطار عمل لرسائل النظام](../../../translated_images/ar/system-message-framework.3a97368c92d11d68.webp)

#### الخطوة 1: إنشاء رسالة نظام شاملة 

سيتم استخدام الموجه الشامل بواسطة نموذج اللغة الكبير لتوليد موجهات النظام للوكلاء الذين ننشئهم. نصممه كقالب بحيث يمكننا إنشاء وكلاء متعددين بكفاءة إذا لزم الأمر.

إليك مثال على رسالة نظام شاملة سنعطيها لنموذج اللغة الكبير:

```plaintext
You are an expert at creating AI agent assistants. 
You will be provided a company name, role, responsibilities and other
information that you will use to provide a system prompt for.
To create the system prompt, be descriptive as possible and provide a structure that a system using an LLM can better understand the role and responsibilities of the AI assistant. 
```

#### الخطوة 2: إنشاء موجه أساسي

الخطوة التالية هي إنشاء موجه أساسي لوصف وكيل الذكاء الاصطناعي. يجب أن تتضمن دور الوكيل، والمهام التي سيكملها، وأي مسؤوليات أخرى للوكيل.

إليك مثالاً:

```plaintext
You are a travel agent for Contoso Travel that is great at booking flights for customers. To help customers you can perform the following tasks: lookup available flights, book flights, ask for preferences in seating and times for flights, cancel any previously booked flights and alert customers on any delays or cancellations of flights.  
```

#### الخطوة 3: توفير رسالة النظام الأساسية إلى نموذج اللغة الكبير

الآن يمكننا تحسين رسالة النظام هذه من خلال تقديم رسالة النظام الشاملة كرسالة النظام ورسالة النظام الأساسية الخاصة بنا.

سيؤدي ذلك إلى إنتاج رسالة نظام مصممة بشكل أفضل لتوجيه وكلاء الذكاء الاصطناعي لدينا:

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

#### الخطوة 4: التكرار والتحسين

قيمة إطار عمل رسالة النظام هذا هي القدرة على توسيع إنشاء رسائل النظام لوكلاء متعددين بسهولة بالإضافة إلى تحسين رسائل النظام الخاصة بك مع مرور الوقت. نادرًا ما تحصل على رسالة نظام تعمل من المرة الأولى لحالتك كاملة. القدرة على إجراء تعديلات وتحسينات صغيرة عن طريق تغيير رسالة النظام الأساسية وتشغيلها عبر النظام ستسمح لك بالمقارنة وتقييم النتائج.

## فهم التهديدات

لبناء وكلاء ذكاء اصطناعي موثوق بهم، من المهم فهم وتخفيف المخاطر والتهديدات لوكيل الذكاء الاصطناعي الخاص بك. دعنا نلقي نظرة على بعض التهديدات المختلفة لوكلاء الذكاء الاصطناعي وكيف يمكنك التخطيط لها بشكل أفضل والاستعداد لها.

![فهم التهديدات](../../../translated_images/ar/understanding-threats.89edeada8a97fc0f.webp)

### المهمة والتعليمات

**الوصف:** يحاول المهاجمون تغيير التعليمات أو أهداف وكيل الذكاء الاصطناعي عبر الموجهات أو التلاعب بالمدخلات.

**التخفيف**: تنفيذ فحوصات التحقق ومرشحات الإدخال لاكتشاف الموجهات التي قد تكون خطيرة قبل أن تتم معالجتها بواسطة وكيل الذكاء الاصطناعي. بما أن هذه الهجمات تتطلب عادة تفاعلاً متكررًا مع الوكيل، فإن تقييد عدد الأدوار في المحادثة هو طريقة أخرى لمنع هذا النوع من الهجمات.

### الوصول إلى الأنظمة الحرجة

**الوصف:** إذا كان لدى وكيل الذكاء الاصطناعي وصول إلى أنظمة وخدمات تخزن بيانات حساسة، يمكن للمهاجمين اختراق الاتصال بين الوكيل وهذه الخدمات. يمكن أن تكون هذه هجمات مباشرة أو محاولات غير مباشرة للحصول على معلومات حول هذه الأنظمة عبر الوكيل.

**التخفيف**: يجب أن يكون وصول وكلاء الذكاء الاصطناعي إلى الأنظمة على أساس الحاجة فقط لمنع هذا النوع من الهجمات. يجب أن تكون الاتصالات بين الوكيل والنظام مؤمنة أيضًا. تنفيذ المصادقة والتحكم في الوصول هو طريقة أخرى لحماية هذه المعلومات.

### تحميل الموارد والخدمات بشكل زائد

**الوصف:** يمكن لوكلاء الذكاء الاصطناعي الوصول إلى أدوات وخدمات مختلفة لإكمال المهام. يمكن للمهاجمين استغلال هذه القدرة لمهاجمة هذه الخدمات عن طريق إرسال عدد كبير من الطلبات عبر وكيل الذكاء الاصطناعي، مما قد يؤدي إلى فشل النظام أو تكاليف مرتفعة.

**التخفيف:** تنفيذ سياسات لتقييد عدد الطلبات التي يمكن لوكيل الذكاء الاصطناعي إرسالها إلى خدمة معينة. كما أن تقييد عدد أدوار المحادثة والطلبات إلى وكيل الذكاء الاصطناعي هو أيضًا طريقة لمنع هذا النوع من الهجمات.

### تسميم قاعدة المعرفة

**الوصف:** هذا النوع من الهجوم لا يهاجم وكيل الذكاء الاصطناعي بشكل مباشر ولكنه يستهدف قاعدة المعرفة وغيرها من الخدمات التي يستخدمها الوكيل. قد يشمل ذلك فساد البيانات أو المعلومات التي يستخدمها الوكيل لإكمال مهمة، مما يؤدي إلى ردود متحيزة أو غير مقصودة للمستخدم.

**التخفيف:** إجراء تحقق منتظم للبيانات التي سيستخدمها وكيل الذكاء الاصطناعي في سير العمل الخاص به. ضمان أن الوصول إلى هذه البيانات آمن ولا يتم تغييره إلا من قبل أشخاص موثوق بهم لتجنب هذا النوع من الهجمات.

### الأخطاء المتسلسلة

**الوصف:** يستخدم وكلاء الذكاء الاصطناعي أدوات وخدمات مختلفة لإكمال المهام. يمكن أن تؤدي الأخطاء التي يسببها المهاجمون إلى فشل أنظمة أخرى مرتبطة بالوكيل، مما يجعل الهجوم أكثر انتشارًا وصعوبة في التتبع.

**التخفيف**: إحدى الطرق لتجنب ذلك هي تشغيل وكيل الذكاء الاصطناعي في بيئة محدودة، مثل أداء المهام في حاوية Docker، لمنع الهجمات المباشرة على النظام. إنشاء آليات استرداد ومنطق إعادة المحاولة عندما تستجيب بعض الأنظمة بخطأ هو طريقة أخرى لمنع فشل أنظمة أكبر.

## الإنسان في الحلقة

طريقة فعالة أخرى لبناء أنظمة وكلاء ذكاء اصطناعي موثوق بها هي استخدام الإنسان في الحلقة. هذا يخلق تدفقًا حيث يمكن للمستخدمين تقديم ملاحظات إلى الوكلاء أثناء التشغيل. يعمل المستخدمون كعوامل في نظام متعدد الوكلاء من خلال تقديم الموافقة أو إيقاف العملية الجارية.

![الإنسان في الحلقة](../../../translated_images/ar/human-in-the-loop.5f0068a678f62f4f.webp)

إليك مقتطف كود يستخدم <Microsoft Agent Framework> ليظهر كيف يتم تنفيذ هذا المفهوم:

```python
import os
from agent_framework.azure import AzureAIProjectAgentProvider
from azure.identity import AzureCliCredential

# إنشاء المزود بموافقة بشرية ضمن الحلقة
provider = AzureAIProjectAgentProvider(
    credential=AzureCliCredential(),
)

# إنشاء الوكيل مع خطوة موافقة بشرية
response = provider.create_response(
    input="Write a 4-line poem about the ocean.",
    instructions="You are a helpful assistant. Ask for user approval before finalizing.",
)

# يمكن للمستخدم مراجعة الرد والموافقة عليه
print(response.output_text)
user_input = input("Do you approve? (APPROVE/REJECT): ")
if user_input == "APPROVE":
    print("Response approved.")
else:
    print("Response rejected. Revising...")
```

## الخاتمة

يتطلب بناء وكلاء ذكاء اصطناعي موثوق بهم تصميمًا دقيقًا، وتدابير أمنية قوية، وتكرارًا مستمرًا. من خلال تنفيذ أنظمة موجهات شاملة منظمة، وفهم التهديدات المحتملة، وتطبيق استراتيجيات التخفيف، يمكن للمطورين إنشاء وكلاء ذكاء اصطناعي آمنين وفعّالين. بالإضافة إلى ذلك، يضمن دمج نهج الإنسان في الحلقة بقاء وكلاء الذكاء الاصطناعي متوافقين مع احتياجات المستخدم مع تقليل المخاطر. مع استمرار تطور الذكاء الاصطناعي، سيكون الحفاظ على موقف استباقي تجاه الأمن والخصوصية والاعتبارات الأخلاقية مفتاحًا لتعزيز الثقة والموثوقية في أنظمة الذكاء الاصطناعي.

## عينات الشيفرة

- [`code_samples/06-system-message-framework.ipynb`](code_samples/06-system-message-framework.ipynb): عرض خطوة بخطوة لإطار عمل موجه النظام الشامل.
- [`code_samples/06-human-in-the-loop.ipynb`](code_samples/06-human-in-the-loop.ipynb): بوابات الموافقة السابقة للعمل، وتصنيف المخاطر، وتسجيل التدقيق للوكلاء الموثوق بهم.

### هل لديك المزيد من الأسئلة حول بناء وكلاء ذكاء اصطناعي موثوق بهم؟

انضم إلى [Microsoft Foundry Discord](https://aka.ms/ai-agents/discord) للقاء متعلمين آخرين، حضور ساعات المكتب، والحصول على إجابات لأسئلتك حول وكلاء الذكاء الاصطناعي.

## موارد إضافية

- <a href="https://learn.microsoft.com/azure/ai-studio/responsible-use-of-ai-overview" target="_blank">نظرة عامة على الذكاء الاصطناعي المسؤول</a>
- <a href="https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai" target="_blank">تقييم نماذج الذكاء الاصطناعي التوليدية وتطبيقات الذكاء الاصطناعي</a>
- <a href="https://learn.microsoft.com/azure/ai-services/openai/concepts/system-message?context=%2Fazure%2Fai-studio%2Fcontext%2Fcontext&tabs=top-techniques" target="_blank">رسائل نظام الأمان</a>
- <a href="https://blogs.microsoft.com/wp-content/uploads/prod/sites/5/2022/06/Microsoft-RAI-Impact-Assessment-Template.pdf?culture=en-us&country=us" target="_blank">قالب تقييم المخاطر</a>

## الدرس السابق

[Agentic RAG](../05-agentic-rag/README.md)

## الدرس التالي

[نمط التصميم التخطيطي](../07-planning-design/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**تنويه**:
تمت ترجمة هذا المستند باستخدام خدمة الترجمة بالذكاء الاصطناعي [Co-op Translator](https://github.com/Azure/co-op-translator). بينما نسعى للدقة، يرجى العلم أن الترجمات الآلية قد تحتوي على أخطاء أو عدم دقة. يجب اعتبار المستند الأصلي بلغته الأصلية المصدر الرسمي والمعتمد. للمعلومات الهامة، يُنصح بالاستعانة بترجمة بشرية محترفة. نحن غير مسؤولين عن أي سوء فهم أو تفسير ناتج عن استخدام هذه الترجمة.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->