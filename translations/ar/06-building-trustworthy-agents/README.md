[![وكلاء الذكاء الاصطناعي الموثوقون](../../../translated_images/ar/lesson-6-thumbnail.a58ab36c099038d4.webp)](https://youtu.be/iZKkMEGBCUQ?si=Q-kEbcyHUMPoHp8L)

> _(انقر على الصورة أعلاه لمشاهدة فيديو هذا الدرس)_

# بناء وكلاء ذكاء اصطناعي موثوقين

## مقدمة

سيغطي هذا الدرس:

- كيفية بناء ونشر وكلاء ذكاء اصطناعي آمنين وفعالين
- اعتبارات أمنية مهمة عند تطوير وكلاء الذكاء الاصطناعي.
- كيفية الحفاظ على خصوصية البيانات والمستخدم عند تطوير وكلاء الذكاء الاصطناعي.

## أهداف التعلم

بعد إتمام هذا الدرس، ستعرف كيفية:

- تحديد وتخفيف المخاطر عند إنشاء وكلاء ذكاء اصطناعي.
- تنفيذ تدابير الأمن لضمان إدارة البيانات والوصول بشكل صحيح.
- إنشاء وكلاء ذكاء اصطناعي يحافظون على خصوصية البيانات ويقدمون تجربة مستخدم عالية الجودة.

## السلامة

لننظر أولًا إلى بناء تطبيقات وكيلة آمنة. تعني السلامة أن الوكيل الذكي يعمل كما هو مصمم. كبناة لتطبيقات وكيلة، لدينا طرق وأدوات لتعظيم السلامة:

### بناء إطار عمل رسالة النظام

إذا سبق لك بناء تطبيق ذكاء اصطناعي باستخدام نماذج اللغة الكبيرة (LLMs)، فأنت تعرف أهمية تصميم موجه نظام قوي أو رسالة نظام. هذه الموجهات تحدد القواعد الكبرى والتعليمات والإرشادات لكيفية تفاعل النموذج مع المستخدم والبيانات.

بالنسبة لوكلاء الذكاء الاصطناعي، موجه النظام أكثر أهمية لأن الوكلاء يحتاجون إلى تعليمات دقيقة جدًا لإكمال المهام التي صممناها لهم.

لإنشاء موجهات نظام قابلة للتوسع، يمكننا استخدام إطار عمل رسالة النظام لبناء وكيل أو أكثر في تطبيقنا:

![بناء إطار عمل رسالة النظام](../../../translated_images/ar/system-message-framework.3a97368c92d11d68.webp)

#### الخطوة 1: إنشاء رسالة نظام كبرى

سيتم استخدام الموجه الرئيسي من قبل نموذج اللغة الكبير لتوليد موجهات النظام للوكلاء الذين ننشئهم. نصممه كقالب بحيث يمكننا إنشاء عدة وكلاء بكفاءة إذا لزم الأمر.

إليك مثال على رسالة نظام كبرى يمكن أن نعطيها للنموذج:

```plaintext
You are an expert at creating AI agent assistants. 
You will be provided a company name, role, responsibilities and other
information that you will use to provide a system prompt for.
To create the system prompt, be descriptive as possible and provide a structure that a system using an LLM can better understand the role and responsibilities of the AI assistant. 
```

#### الخطوة 2: إنشاء موجه أساسي

الخطوة التالية هي إنشاء موجه أساسي لوصف الوكيل الذكي. يجب أن تتضمن دور الوكيل والمهام التي سيكملها وأي مسؤوليات أخرى للوكيل.

إليك مثال:

```plaintext
You are a travel agent for Contoso Travel that is great at booking flights for customers. To help customers you can perform the following tasks: lookup available flights, book flights, ask for preferences in seating and times for flights, cancel any previously booked flights and alert customers on any delays or cancellations of flights.  
```

#### الخطوة 3: تقديم رسالة النظام الأساسية للنموذج

الآن يمكننا تحسين رسالة النظام هذه من خلال توفير رسالة النظام الكبرى كرسالة نظام بالإضافة إلى رسالة النظام الأساسية الخاصة بنا.

هذا سينتج رسالة نظام مصممة بشكل أفضل لتوجيه وكلاء الذكاء الاصطناعي لدينا:

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

قيمة إطار عمل رسالة النظام هذا هي القدرة على توسيع إنشاء رسائل النظام من عدة وكلاء بسهولة بالإضافة إلى تحسين رسائل النظام مع الوقت. من النادر أن تحصل على رسالة نظام تعمل من المرة الأولى لحالة الاستخدام الكاملة الخاصة بك. القدرة على إجراء تعديلات صغيرة وتحسينات بتغيير رسالة النظام الأساسية وتشغيلها من خلال النظام سيسمح لك بالمقارنة وتقييم النتائج.

## فهم التهديدات

لبناء وكلاء ذكاء اصطناعي موثوقين، من المهم فهم وتخفيف المخاطر والتهديدات لوكيل الذكاء الاصطناعي الخاص بك. لننظر إلى بعض التهديدات المختلفة لوكلاء الذكاء الاصطناعي وكيف يمكنك التخطيط والاستعداد لها بشكل أفضل.

![فهم التهديدات](../../../translated_images/ar/understanding-threats.89edeada8a97fc0f.webp)

### المهمة والتعليمات

**الوصف:** يحاول المهاجمون تغيير تعليمات أو أهداف وكيل الذكاء الاصطناعي من خلال الموجه أو التلاعب بالمدخلات.

**التخفيف**: تنفيذ تحقق من الصحة وتصفيات للمدخلات لاكتشاف الموجهات الخطرة المحتملة قبل معالجتها من قبل وكيل الذكاء الاصطناعي. بما أن هذه الهجمات عادةً تتطلب تفاعل متكرر مع الوكيل، فإن تحديد عدد التفاعلات في المحادثة هو طريقة أخرى لمنع هذه الأنواع من الهجمات.

### الوصول إلى الأنظمة الحيوية

**الوصف**: إذا كان لدى وكيل الذكاء الاصطناعي وصول إلى أنظمة وخدمات تخزن بيانات حساسة، يمكن للمهاجمين اختراق الاتصال بين الوكيل وهذه الخدمات. يمكن أن تكون هذه هجمات مباشرة أو محاولات غير مباشرة للحصول على معلومات عن هذه الأنظمة عبر الوكيل.

**التخفيف**: يجب أن يمتلك وكلاء الذكاء الاصطناعي وصولًا فقط حسب الحاجة إلى الأنظمة لمنع هذه الأنواع من الهجمات. يجب أن يكون الاتصال بين الوكيل والنظام آمنًا أيضًا. تنفيذ التوثيق والتحكم في الوصول هو طريقة أخرى لحماية هذه المعلومات.

### تحميل زائد للموارد والخدمات

**الوصف:** يمكن لوكلاء الذكاء الاصطناعي الوصول إلى أدوات وخدمات مختلفة لإكمال المهام. يمكن للمهاجمين استغلال هذه القدرة لمهاجمة هذه الخدمات عن طريق إرسال حجم كبير من الطلبات من خلال وكيل الذكاء الاصطناعي، مما قد يؤدي إلى فشل النظام أو ارتفاع التكاليف.

**التخفيف:** تنفيذ سياسات للحد من عدد الطلبات التي يمكن لوكيل الذكاء الاصطناعي إرسالها إلى خدمة معينة. تحديد عدد الأدوار في المحادثة وعدد الطلبات إلى وكيل الذكاء الاصطناعي هو طريقة أخرى لمنع هذه الأنواع من الهجمات.

### تسميم قاعدة المعرفة

**الوصف:** لا تستهدف هذه الهجمة وكيل الذكاء الاصطناعي مباشرة، بل تستهدف قاعدة المعرفة والخدمات الأخرى التي يستخدمها الوكيل. يمكن أن تشمل هذه الهجمة فساد البيانات أو المعلومات التي يستخدمها الوكيل لإكمال المهمة، مما يؤدي إلى ردود متحيزة أو غير مقصودة للمستخدم.

**التخفيف:** إجراء تحقق منتظم على البيانات التي سيستخدمها وكيل الذكاء الاصطناعي في سير العمل. التأكد من أن الوصول إلى هذه البيانات آمن ولا يتم تغييره إلا من قبل أفراد موثوقين لتجنب هذا النوع من الهجمات.

### الأخطاء المتسلسلة

**الوصف:** يستخدم وكلاء الذكاء الاصطناعي أدوات وخدمات مختلفة لإكمال المهام. يمكن أن تؤدي الأخطاء التي تسببها الهجمات إلى فشل أنظمة أخرى متصلة بوكيل الذكاء الاصطناعي، مما يجعل الهجوم أكثر انتشارًا وصعوبة في التحليل.

**التخفيف**: أحد الطرق لتجنب ذلك هو تشغيل وكيل الذكاء الاصطناعي في بيئة محدودة، مثل تنفيذ المهام في حاوية Docker، لمنع الهجمات المباشرة على النظام. إنشاء آليات احتياطية ومنطق إعادة المحاولة عندما ترد أنظمة معينة بخطأ هو طريقة أخرى لمنع فشل الأنظمة الكبير.

## الإنسان في الحلقة

طريقة فعالة أخرى لبناء أنظمة وكلاء ذكاء اصطناعي موثوقين هي استخدام الإنسان في الحلقة. هذا يخلق تدفقًا يمكن للمستخدمين من خلاله تقديم ملاحظات للوكلاء أثناء التشغيل. المستخدمون يعملون أساسًا كوكلاء في نظام متعدد الوكلاء من خلال تقديم الموافقة أو إنهاء العملية الجارية.

![الإنسان في الحلقة](../../../translated_images/ar/human-in-the-loop.5f0068a678f62f4f.webp)

إليك مقتطف كود باستخدام إطار عمل Microsoft Agent لعرض كيفية تنفيذ هذا المفهوم:

```python
import os
from agent_framework.foundry import FoundryChatClient
from azure.identity import AzureCliCredential

# إنشاء المزود بموافقة بشرية في الحلقة
provider = FoundryChatClient(
    project_endpoint=os.environ["AZURE_AI_PROJECT_ENDPOINT"],
    model=os.environ["AZURE_AI_MODEL_DEPLOYMENT_NAME"],
    credential=AzureCliCredential(),
)

# إنشاء الوكيل مع خطوة موافقة بشرية
response = provider.create_response(
    input="Write a 4-line poem about the ocean.",
    instructions="You are a helpful assistant. Ask for user approval before finalizing.",
)

# يمكن للمستخدم مراجعة الاستجابة والموافقة عليها
print(response.output_text)
user_input = input("Do you approve? (APPROVE/REJECT): ")
if user_input == "APPROVE":
    print("Response approved.")
else:
    print("Response rejected. Revising...")
```

## الخاتمة

يتطلب بناء وكلاء ذكاء اصطناعي موثوقين تصميمًا دقيقًا وتدابير أمان قوية وتكرارًا مستمرًا. من خلال تنفيذ أنظمة توجيه ميتا منظمة، وفهم التهديدات المحتملة، وتطبيق استراتيجيات التخفيف، يمكن للمطورين إنشاء وكلاء ذكاء اصطناعي آمنين وفعالين. بالإضافة إلى ذلك، يضمن تضمين نهج الإنسان في الحلقة أن يظل وكلاء الذكاء الاصطناعي متماشين مع احتياجات المستخدم مع تقليل المخاطر. مع استمرار تطور الذكاء الاصطناعي، سيظل الحفاظ على موقف استباقي تجاه الأمان والخصوصية والاعتبارات الأخلاقية مفتاحًا لتعزيز الثقة والموثوقية في أنظمة الذكاء الاصطناعي.

## أمثلة الكود

- [`code_samples/06-system-message-framework.ipynb`](code_samples/06-system-message-framework.ipynb): عرض خطوة بخطوة لإطار عمل موجه رسالة النظام الميتا.
- [`code_samples/06-human-in-the-loop.ipynb`](code_samples/06-human-in-the-loop.ipynb): بوابات الموافقة قبل الإجراء، تصنيف المخاطر، وتسجيل التدقيق للوكلاء الموثوقين.

### هل لديك المزيد من الأسئلة حول بناء وكلاء ذكاء اصطناعي موثوقين؟

انضم إلى [خادم Microsoft Foundry على Discord](https://discord.com/invite/ATgtXmAS5D) للقاء المتعلمين الآخرين، حضور ساعات العمل، والحصول على إجابات لأسئلتك حول وكلاء الذكاء الاصطناعي.

## موارد إضافية

- <a href="https://learn.microsoft.com/azure/ai-studio/responsible-use-of-ai-overview" target="_blank">نظرة عامة على الذكاء الاصطناعي المسؤول</a>
- <a href="https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai" target="_blank">تقييم نماذج الذكاء الاصطناعي التوليدية وتطبيقات الذكاء الاصطناعي</a>
- <a href="https://learn.microsoft.com/azure/ai-services/openai/concepts/system-message?context=%2Fazure%2Fai-studio%2Fcontext%2Fcontext&tabs=top-techniques" target="_blank">رسائل نظام السلامة</a>
- <a href="https://blogs.microsoft.com/wp-content/uploads/prod/sites/5/2022/06/Microsoft-RAI-Impact-Assessment-Template.pdf?culture=en-us&country=us" target="_blank">قالب تقييم المخاطر</a>

## الدرس السابق

[Agentic RAG](../05-agentic-rag/README.md)

## الدرس التالي

[تصميم التخطيط](../07-planning-design/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**تنويه**:
تمت ترجمة هذا المستند باستخدام خدمة الترجمة بالذكاء الاصطناعي [Co-op Translator](https://github.com/Azure/co-op-translator). بينما نسعى للدقة، يرجى العلم أن الترجمات الآلية قد تحتوي على أخطاء أو عدم دقة. يجب اعتبار المستند الأصلي بلغته الأصلية المصدر الرسمي والمعتمد. للمعلومات الهامة، يُنصح بالاستعانة بترجمة بشرية محترفة. نحن غير مسؤولين عن أي سوء فهم أو تفسير ناتج عن استخدام هذه الترجمة.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->