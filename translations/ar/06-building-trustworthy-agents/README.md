[![وكلاء الذكاء الاصطناعي الموثوق بهم](../../../translated_images/ar/lesson-6-thumbnail.a58ab36c099038d4.webp)](https://youtu.be/iZKkMEGBCUQ?si=Q-kEbcyHUMPoHp8L)

> _(انقر على الصورة أعلاه لمشاهدة فيديو هذا الدرس)_

# بناء وكلاء ذكاء اصطناعي موثوق بهم

## المقدمة

سيغطي هذا الدرس:

- كيفية بناء ونشر وكلاء ذكاء اصطناعي آمنين وفعالين
- اعتبارات الأمان المهمة عند تطوير وكلاء الذكاء الاصطناعي.
- كيفية الحفاظ على خصوصية البيانات والمستخدم عند تطوير وكلاء الذكاء الاصطناعي.

## أهداف التعلم

بعد إكمال هذا الدرس، ستعرف كيف:

- تحديد وتقليل المخاطر عند إنشاء وكلاء الذكاء الاصطناعي.
- تنفيذ تدابير أمان لضمان إدارة البيانات والوصول بشكل صحيح.
- إنشاء وكلاء ذكاء اصطناعي يحافظون على خصوصية البيانات ويوفرون تجربة مستخدم عالية الجودة.

## السلامة

دعونا ننظر أولاً في بناء تطبيقات وكيلة آمنة. السلامة تعني أن الوكيل الذكي يؤدي حسب التصميم. بصفتنا منشئي تطبيقات وكيلة، لدينا طرق وأدوات لتعظيم السلامة:

### بناء إطار رسالة النظام

إذا كنت قد أنشأت تطبيق ذكاء اصطناعي باستخدام نماذج اللغة الكبيرة (LLMs)، فأنت تعرف أهمية تصميم موجه نظام قوي أو رسالة نظام. تضع هذه الموجهات القواعد العليا والتعليمات والإرشادات لكيفية تعامل نموذج اللغة الكبير مع المستخدم والبيانات.

بالنسبة لوكلاء الذكاء الاصطناعي، فإن موجه النظام أهم حتى أن وكلاء الذكاء الاصطناعي سيحتاجون إلى تعليمات محددة للغاية لإكمال المهام التي صممناها لهم.

لإنشاء موجهات نظام قابلة للتوسع، يمكننا استخدام إطار رسالة نظام لبناء وكيل واحد أو أكثر في تطبيقنا:

![بناء إطار رسالة النظام](../../../translated_images/ar/system-message-framework.3a97368c92d11d68.webp)

#### الخطوة 1: إنشاء رسالة نظام عليا

سيُستخدم الموجه الأعلى بواسطة نموذج اللغة الكبير لتوليد موجهات النظام للوكلاء الذين ننشئهم. نصممه كقالب حتى نتمكن من إنشاء عدة وكلاء بكفاءة إذا لزم الأمر.

إليك مثال على رسالة نظام عليا سنعطيها لنموذج اللغة الكبير:

```plaintext
You are an expert at creating AI agent assistants. 
You will be provided a company name, role, responsibilities and other
information that you will use to provide a system prompt for.
To create the system prompt, be descriptive as possible and provide a structure that a system using an LLM can better understand the role and responsibilities of the AI assistant. 
```

#### الخطوة 2: إنشاء موجه أساسي

الخطوة التالية هي إنشاء موجه أساسي لوصف وكيل الذكاء الاصطناعي. يجب أن تتضمن دور الوكيل، والمهام التي سيُكملها الوكيل، وأي مسؤوليات أخرى للوكيل.

إليك مثال:

```plaintext
You are a travel agent for Contoso Travel that is great at booking flights for customers. To help customers you can perform the following tasks: lookup available flights, book flights, ask for preferences in seating and times for flights, cancel any previously booked flights and alert customers on any delays or cancellations of flights.  
```

#### الخطوة 3: تزويد نموذج اللغة الكبير برسالة نظام أساسية

الآن يمكننا تحسين رسالة النظام هذه من خلال تقديم رسالة النظام العليا كرسالة النظام ورسالة النظام الأساسية لدينا.

سيؤدي هذا إلى إنشاء رسالة نظام مصممة بشكل أفضل لتوجيه وكلاء الذكاء الاصطناعي لدينا:

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

تكمن قيمة هذا الإطار في تمكين التوسع في إنشاء رسائل النظام من عدة وكلاء بسهولة بالإضافة إلى تحسين رسائل النظام الخاصة بك مع مرور الوقت. من النادر أن يكون لديك رسالة نظام تعمل في المرة الأولى لحالة الاستخدام الكاملة الخاصة بك. القدرة على إجراء تعديلات صغيرة وتحسينات من خلال تغيير رسالة النظام الأساسية وتشغيلها عبر النظام ستمكنك من المقارنة وتقييم النتائج.

## فهم التهديدات

لبناء وكلاء ذكاء اصطناعي موثوق بهم، من المهم فهم المخاطر والتهديدات التي تواجه وكيل الذكاء الاصطناعي وتقليلها. لننظر في بعض فقط من التهديدات المختلفة لوكلاء الذكاء الاصطناعي وكيف يمكنك التخطيط والتحضير بشكل أفضل لها.

![فهم التهديدات](../../../translated_images/ar/understanding-threats.89edeada8a97fc0f.webp)

### المهمة والتعليمات

**الوصف:** يحاول المهاجمون تغيير تعليمات أو أهداف وكيل الذكاء الاصطناعي من خلال التحفيز أو التلاعب بالمدخلات.

**التخفيف**: نفذ فحوصات التحقق ومرشحات الإدخال لاكتشاف الموجهات الخطرة قبل أن تتم معالجتها بواسطة وكيل الذكاء الاصطناعي. بما أن هذه الهجمات عادة ما تتطلب تفاعلًا متكررًا مع الوكيل، فإن الحد من عدد الأدوار في المحادثة هو طريقة أخرى لمنع هذه الأنواع من الهجمات.

### الوصول إلى الأنظمة الحرجة

**الوصف**: إذا كان لوكيل الذكاء الاصطناعي إمكانية الوصول إلى أنظمة وخدمات تخزن بيانات حساسة، يمكن للمهاجمين اختراق الاتصال بين الوكيل وهذه الخدمات. يمكن أن تكون هذه هجمات مباشرة أو محاولات غير مباشرة للحصول على معلومات حول هذه الأنظمة من خلال الوكيل.

**التخفيف**: يجب أن يكون لوكلاء الذكاء الاصطناعي حق الوصول إلى الأنظمة فقط حسب الحاجة لمنع هذه الأنواع من الهجمات. يجب أن يكون الاتصال بين الوكيل والنظام آمنًا أيضًا. تنفيذ التوثيق والتحكم في الوصول هو طريقة أخرى لحماية هذه المعلومات.

### التحميل الزائد على الموارد والخدمات

**الوصف:** يمكن لوكلاء الذكاء الاصطناعي الوصول إلى أدوات وخدمات مختلفة لإكمال المهام. يمكن للمهاجمين استخدام هذه القدرة لمهاجمة هذه الخدمات عن طريق إرسال حجم مرتفع من الطلبات عبر وكيل الذكاء الاصطناعي، مما قد يؤدي إلى فشل النظام أو تكاليف عالية.

**التخفيف:** نفذ سياسات للحد من عدد الطلبات التي يمكن لوكيل الذكاء الاصطناعي تقديمها إلى خدمة. الحد من عدد أدوار المحادثة والطلبات إلى وكيل الذكاء الاصطناعي الخاص بك هو طريقة أخرى لمنع هذه الأنواع من الهجمات.

### تسميم قاعدة المعرفة

**الوصف:** هذا النوع من الهجمات لا يستهدف وكيل الذكاء الاصطناعي مباشرةً بل يستهدف قاعدة المعرفة والخدمات الأخرى التي سيستخدمها الوكيل. قد يشمل ذلك فساد البيانات أو المعلومات التي سيستخدمها وكيل الذكاء الاصطناعي لإكمال المهمة، مما يؤدي إلى استجابات متحيزة أو غير مقصودة للمستخدم.

**التخفيف:** قم بإجراء تحقق منتظم من البيانات التي سيستخدمها وكيل الذكاء الاصطناعي في سير العمل الخاص به. تأكد من أن الوصول إلى هذه البيانات آمن ولا يتم تغييره إلا بواسطة أشخاص موثوق بهم لتجنب هذا النوع من الهجمات.

### الأخطاء المتسلسلة

**الوصف:** يصل وكلاء الذكاء الاصطناعي إلى أدوات وخدمات متنوعة لإكمال المهام. يمكن أن تؤدي الأخطاء التي يسببها المهاجمون إلى فشل أنظمة أخرى متصلة بوكيل الذكاء الاصطناعي، مما يجعل الهجوم أكثر انتشارًا وأصعب في التشخيص.

**التخفيف**: إحدى الطرق لتجنب ذلك هي جعل وكيل الذكاء الاصطناعي يعمل في بيئة محدودة، مثل أداء المهام في حاوية Docker، لمنع الهجمات المباشرة على النظام. إنشاء آليات تراجع ومنطق إعادة المحاولة عندما تستجيب بعض الأنظمة بخطأ هو طريقة أخرى لمنع فشل أنظمة أكبر.

## الإنسان في الحلقة

طريقة فعالة أخرى لبناء أنظمة وكلاء ذكاء اصطناعي موثوقة هي استخدام الإنسان في الحلقة. يخلق هذا تدفقًا حيث يمكن للمستخدمين تقديم ملاحظات للوكلاء أثناء التشغيل. يعمل المستخدمون بشكل أساسي كوكلاء في نظام متعدد الوكلاء ومن خلال تقديم الموافقة أو إنهاء العملية الجارية.

![الإنسان في الحلقة](../../../translated_images/ar/human-in-the-loop.5f0068a678f62f4f.webp)

فيما يلي مقطع كود يستخدم Microsoft Agent Framework ليوضح كيف تم تنفيذ هذا المفهوم:

```python
import os
from agent_framework.azure import AzureAIProjectAgentProvider
from azure.identity import AzureCliCredential

# إنشاء المزود بموافقة بشرية متداخلة
provider = AzureAIProjectAgentProvider(
    credential=AzureCliCredential(),
)

# إنشاء الوكيل بخطوة موافقة بشرية
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

## الخلاصة

يتطلب بناء وكلاء ذكاء اصطناعي موثوق بهم تصميمًا دقيقًا، وتدابير أمان قوية، وتكرارًا مستمرًا. من خلال تنفيذ أنظمة تحفيز ميتا منظمة، وفهم التهديدات المحتملة، وتطبيق استراتيجيات التخفيف، يمكن للمطورين إنشاء وكلاء ذكاء اصطناعي يكونون آمنين وفعالين. بالإضافة إلى ذلك، يضمن دمج نهج الإنسان في الحلقة بقاء وكلاء الذكاء الاصطناعي متماشين مع احتياجات المستخدم مع تقليل المخاطر. مع استمرار تطور الذكاء الاصطناعي، سيكون الحفاظ على موقف استباقي تجاه الأمن والخصوصية والاعتبارات الأخلاقية مفتاحًا لتعزيز الثقة والموثوقية في الأنظمة المدفوعة بالذكاء الاصطناعي.

### هل لديك المزيد من الأسئلة حول بناء وكلاء ذكاء اصطناعي موثوق بهم؟

انضم إلى [Microsoft Foundry Discord](https://aka.ms/ai-agents/discord) للقاء متعلمين آخرين، وحضور ساعات المكتب، والحصول على إجابات لأسئلتك حول وكلاء الذكاء الاصطناعي.

## موارد إضافية

- <a href="https://learn.microsoft.com/azure/ai-studio/responsible-use-of-ai-overview" target="_blank">نظرة عامة على الذكاء الاصطناعي المسؤول</a>
- <a href="https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai" target="_blank">تقييم نماذج وتطبيقات الذكاء الاصطناعي التوليدي</a>
- <a href="https://learn.microsoft.com/azure/ai-services/openai/concepts/system-message?context=%2Fazure%2Fai-studio%2Fcontext%2Fcontext&tabs=top-techniques" target="_blank">رسائل نظام الأمان</a>
- <a href="https://blogs.microsoft.com/wp-content/uploads/prod/sites/5/2022/06/Microsoft-RAI-Impact-Assessment-Template.pdf?culture=en-us&country=us" target="_blank">قالب تقييم المخاطر</a>

## الدرس السابق

[Agentic RAG](../05-agentic-rag/README.md)

## الدرس التالي

[نمط تصميم التخطيط](../07-planning-design/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**إخلاء مسؤولية**:  
تمت ترجمة هذا المستند باستخدام خدمة الترجمة الآلية [Co-op Translator](https://github.com/Azure/co-op-translator). بينما نسعى لتحقيق الدقة، يرجى العلم بأن الترجمات الآلية قد تحتوي على أخطاء أو عدم دقة. يجب اعتبار النسخة الأصلية من المستند بلغتها الأصلية المصدر الموثوق والمعتمد. للمعلومات الحساسة أو الهامة، يُنصح بالاستعانة بترجمة احترافية من قبل مترجمين بشريين. نحن غير مسؤولين عن أي سوء فهم أو تفسيرات خاطئة قد تنشأ عن استخدام هذه الترجمة.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->