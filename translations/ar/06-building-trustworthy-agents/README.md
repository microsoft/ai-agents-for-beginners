<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "498802b4c3c3cc486b86f27a12cebb34",
  "translation_date": "2025-08-29T09:13:47+00:00",
  "source_file": "06-building-trustworthy-agents/README.md",
  "language_code": "ar"
}
-->
[![وكلاء الذكاء الاصطناعي الموثوق بهم](../../../translated_images/lesson-6-thumbnail.a58ab36c099038d4f786c2b0d5d6e89f41f4c2ecc05ab10b67bced2695eeb218.ar.png)](https://youtu.be/iZKkMEGBCUQ?si=Q-kEbcyHUMPoHp8L)

> _(اضغط على الصورة أعلاه لمشاهدة فيديو الدرس)_

# بناء وكلاء ذكاء اصطناعي موثوق بهم

## المقدمة

سيتناول هذا الدرس:

- كيفية بناء ونشر وكلاء ذكاء اصطناعي آمنين وفعّالين.
- اعتبارات الأمان المهمة عند تطوير وكلاء الذكاء الاصطناعي.
- كيفية الحفاظ على خصوصية البيانات والمستخدم أثناء تطوير وكلاء الذكاء الاصطناعي.

## أهداف التعلم

بعد إكمال هذا الدرس، ستتمكن من:

- تحديد المخاطر والتخفيف منها عند إنشاء وكلاء الذكاء الاصطناعي.
- تنفيذ تدابير الأمان لضمان إدارة البيانات والوصول بشكل صحيح.
- إنشاء وكلاء ذكاء اصطناعي يحافظون على خصوصية البيانات ويوفرون تجربة مستخدم عالية الجودة.

## الأمان

لنبدأ أولاً بالنظر في كيفية بناء تطبيقات وكيلة آمنة. الأمان يعني أن وكيل الذكاء الاصطناعي يعمل كما هو مصمم. كمطوري تطبيقات وكيلة، لدينا طرق وأدوات لتعظيم الأمان:

### بناء إطار عمل لرسائل النظام

إذا سبق لك بناء تطبيق ذكاء اصطناعي باستخدام نماذج اللغة الكبيرة (LLMs)، فأنت تعرف أهمية تصميم رسالة نظام قوية. هذه الرسائل تحدد القواعد العامة والتعليمات والإرشادات لكيفية تفاعل النموذج مع المستخدم والبيانات.

بالنسبة لوكلاء الذكاء الاصطناعي، تصبح رسالة النظام أكثر أهمية لأن الوكلاء يحتاجون إلى تعليمات محددة للغاية لإكمال المهام المصممة لهم.

لإنشاء رسائل نظام قابلة للتوسع، يمكننا استخدام إطار عمل لرسائل النظام لبناء وكيل أو أكثر في تطبيقنا:

![بناء إطار عمل لرسائل النظام](../../../translated_images/system-message-framework.3a97368c92d11d6814577b03cd128ec8c71a5fd1e26f341835cfa5df59ae87ae.ar.png)

#### الخطوة 1: إنشاء رسالة نظام عامة

سيتم استخدام الرسالة العامة بواسطة نموذج اللغة الكبير (LLM) لتوليد رسائل النظام للوكلاء الذين نقوم بإنشائهم. نصممها كقالب بحيث يمكننا إنشاء عدة وكلاء بكفاءة إذا لزم الأمر.

إليك مثال على رسالة نظام عامة يمكننا تقديمها للنموذج:

```plaintext
You are an expert at creating AI agent assistants. 
You will be provided a company name, role, responsibilities and other
information that you will use to provide a system prompt for.
To create the system prompt, be descriptive as possible and provide a structure that a system using an LLM can better understand the role and responsibilities of the AI assistant. 
```

#### الخطوة 2: إنشاء رسالة أساسية

الخطوة التالية هي إنشاء رسالة أساسية لوصف وكيل الذكاء الاصطناعي. يجب أن تتضمن دور الوكيل، المهام التي سيكملها، وأي مسؤوليات أخرى للوكيل.

إليك مثال:

```plaintext
You are a travel agent for Contoso Travel that is great at booking flights for customers. To help customers you can perform the following tasks: lookup available flights, book flights, ask for preferences in seating and times for flights, cancel any previously booked flights and alert customers on any delays or cancellations of flights.  
```

#### الخطوة 3: تقديم رسالة النظام الأساسية للنموذج

الآن يمكننا تحسين هذه الرسالة عن طريق تقديم الرسالة العامة كنظام رسالة ورسالتنا الأساسية.

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

قيمة إطار عمل رسالة النظام تكمن في القدرة على إنشاء رسائل نظام لوكلاء متعددين بسهولة وكذلك تحسين رسائل النظام بمرور الوقت. من النادر أن تكون رسالة النظام مثالية من المرة الأولى لتغطية جميع حالات الاستخدام. القدرة على إجراء تعديلات صغيرة وتحسينات عن طريق تغيير الرسالة الأساسية وتشغيلها عبر النظام ستسمح لك بمقارنة النتائج وتقييمها.

## فهم التهديدات

لبناء وكلاء ذكاء اصطناعي موثوق بهم، من المهم فهم المخاطر والتهديدات التي تواجه وكيل الذكاء الاصطناعي والتخفيف منها. دعونا نلقي نظرة على بعض التهديدات المختلفة وكيف يمكنك التخطيط لها بشكل أفضل.

![فهم التهديدات](../../../translated_images/understanding-threats.89edeada8a97fc0f7053558567d5dd27c0c333b74e47fffdde490fa6777a4c17.ar.png)

### المهام والتعليمات

**الوصف:** يحاول المهاجمون تغيير تعليمات أو أهداف وكيل الذكاء الاصطناعي من خلال التلاعب بالمطالبات أو المدخلات.

**التخفيف:** تنفيذ فحوصات التحقق وفلاتر المدخلات للكشف عن المطالبات الخطرة المحتملة قبل معالجتها بواسطة وكيل الذكاء الاصطناعي. نظرًا لأن هذه الهجمات تتطلب عادةً تفاعلًا متكررًا مع الوكيل، فإن تقليل عدد الأدوار في المحادثة هو طريقة أخرى لمنع هذا النوع من الهجمات.

### الوصول إلى الأنظمة الحيوية

**الوصف:** إذا كان وكيل الذكاء الاصطناعي لديه وصول إلى أنظمة وخدمات تخزن بيانات حساسة، يمكن للمهاجمين اختراق الاتصال بين الوكيل وهذه الخدمات. قد تكون هذه هجمات مباشرة أو محاولات غير مباشرة للحصول على معلومات حول هذه الأنظمة من خلال الوكيل.

**التخفيف:** يجب أن يكون لوكلاء الذكاء الاصطناعي وصول إلى الأنظمة فقط عند الحاجة لمنع هذا النوع من الهجمات. يجب أن يكون الاتصال بين الوكيل والنظام آمنًا أيضًا. تنفيذ المصادقة والتحكم في الوصول هو طريقة أخرى لحماية هذه المعلومات.

### التحميل الزائد على الموارد والخدمات

**الوصف:** يمكن لوكلاء الذكاء الاصطناعي الوصول إلى أدوات وخدمات مختلفة لإكمال المهام. يمكن للمهاجمين استخدام هذه القدرة لمهاجمة هذه الخدمات عن طريق إرسال عدد كبير من الطلبات عبر وكيل الذكاء الاصطناعي، مما قد يؤدي إلى فشل النظام أو تكاليف عالية.

**التخفيف:** تنفيذ سياسات لتحديد عدد الطلبات التي يمكن لوكيل الذكاء الاصطناعي إرسالها إلى خدمة معينة. تقليل عدد الأدوار في المحادثة والطلبات إلى وكيل الذكاء الاصطناعي هو طريقة أخرى لمنع هذا النوع من الهجمات.

### تسميم قاعدة المعرفة

**الوصف:** هذا النوع من الهجوم لا يستهدف وكيل الذكاء الاصطناعي مباشرة، بل يستهدف قاعدة المعرفة والخدمات الأخرى التي يستخدمها الوكيل. قد يتضمن ذلك إفساد البيانات أو المعلومات التي يستخدمها الوكيل لإكمال مهمة، مما يؤدي إلى ردود منحازة أو غير مقصودة للمستخدم.

**التخفيف:** إجراء تحقق منتظم من البيانات التي سيستخدمها وكيل الذكاء الاصطناعي في سير العمل. ضمان أن الوصول إلى هذه البيانات آمن ويتم تغييره فقط بواسطة أفراد موثوق بهم لتجنب هذا النوع من الهجوم.

### الأخطاء المتتالية

**الوصف:** وكلاء الذكاء الاصطناعي يصلون إلى أدوات وخدمات مختلفة لإكمال المهام. الأخطاء التي يسببها المهاجمون يمكن أن تؤدي إلى فشل أنظمة أخرى متصلة بالوكيل، مما يجعل الهجوم أكثر انتشارًا وصعوبة في استكشاف الأخطاء وإصلاحها.

**التخفيف:** إحدى الطرق لتجنب ذلك هي أن يعمل وكيل الذكاء الاصطناعي في بيئة محدودة، مثل أداء المهام في حاوية Docker، لمنع الهجمات المباشرة على النظام. إنشاء آليات احتياطية ومنطق إعادة المحاولة عندما تستجيب أنظمة معينة بخطأ هو طريقة أخرى لمنع فشل الأنظمة الأكبر.

## الإنسان في الحلقة

طريقة فعالة أخرى لبناء أنظمة وكلاء ذكاء اصطناعي موثوق بها هي استخدام الإنسان في الحلقة. هذا يخلق تدفقًا حيث يمكن للمستخدمين تقديم ملاحظات للوكلاء أثناء التشغيل. يعمل المستخدمون بشكل أساسي كعملاء في نظام متعدد الوكلاء من خلال تقديم الموافقة أو إنهاء العملية الجارية.

![الإنسان في الحلقة](../../../translated_images/human-in-the-loop.5f0068a678f62f4fc8373d5b78c4c22f35d9e4da35c93f66c3b634c1774eff34.ar.png)

إليك مقتطف من الكود باستخدام AutoGen يوضح كيفية تنفيذ هذا المفهوم:

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

## الخاتمة

يتطلب بناء وكلاء ذكاء اصطناعي موثوق بهم تصميمًا دقيقًا، تدابير أمان قوية، وتكرارًا مستمرًا. من خلال تنفيذ أنظمة التوجيه العامة المنظمة، وفهم التهديدات المحتملة، وتطبيق استراتيجيات التخفيف، يمكن للمطورين إنشاء وكلاء ذكاء اصطناعي آمنين وفعّالين. بالإضافة إلى ذلك، يضمن دمج نهج الإنسان في الحلقة أن تظل وكلاء الذكاء الاصطناعي متوافقة مع احتياجات المستخدم مع تقليل المخاطر. مع استمرار تطور الذكاء الاصطناعي، سيكون الحفاظ على موقف استباقي بشأن الأمان والخصوصية والاعتبارات الأخلاقية مفتاحًا لتعزيز الثقة والموثوقية في الأنظمة المدفوعة بالذكاء الاصطناعي.

### هل لديك المزيد من الأسئلة حول بناء وكلاء ذكاء اصطناعي موثوق بهم؟

انضم إلى [Azure AI Foundry Discord](https://aka.ms/ai-agents/discord) للتواصل مع متعلمين آخرين، حضور ساعات المكتب، والحصول على إجابات لأسئلتك حول وكلاء الذكاء الاصطناعي.

## موارد إضافية

- <a href="https://learn.microsoft.com/azure/ai-studio/responsible-use-of-ai-overview" target="_blank">نظرة عامة على الذكاء الاصطناعي المسؤول</a>
- <a href="https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai" target="_blank">تقييم نماذج الذكاء الاصطناعي التوليدية وتطبيقات الذكاء الاصطناعي</a>
- <a href="https://learn.microsoft.com/azure/ai-services/openai/concepts/system-message?context=%2Fazure%2Fai-studio%2Fcontext%2Fcontext&tabs=top-techniques" target="_blank">رسائل نظام الأمان</a>
- <a href="https://blogs.microsoft.com/wp-content/uploads/prod/sites/5/2022/06/Microsoft-RAI-Impact-Assessment-Template.pdf?culture=en-us&country=us" target="_blank">نموذج تقييم المخاطر</a>

## الدرس السابق

[Agentic RAG](../05-agentic-rag/README.md)

## الدرس التالي

[نمط تصميم التخطيط](../07-planning-design/README.md)

---

**إخلاء المسؤولية**:  
تم ترجمة هذا المستند باستخدام خدمة الترجمة الآلية [Co-op Translator](https://github.com/Azure/co-op-translator). بينما نسعى لتحقيق الدقة، يرجى العلم أن الترجمات الآلية قد تحتوي على أخطاء أو عدم دقة. يجب اعتبار المستند الأصلي بلغته الأصلية هو المصدر الموثوق. للحصول على معلومات حساسة أو هامة، يُوصى بالاستعانة بترجمة بشرية احترافية. نحن غير مسؤولين عن أي سوء فهم أو تفسيرات خاطئة تنشأ عن استخدام هذه الترجمة.