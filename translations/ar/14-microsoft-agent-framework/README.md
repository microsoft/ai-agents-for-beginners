# استكشاف إطار عمل Microsoft Agent

![Agent Framework](../../../translated_images/ar/lesson-14-thumbnail.90df0065b9d234ee.webp)

### المقدمة

ستغطي هذه الدرس:

- فهم إطار عمل Microsoft Agent: الميزات الرئيسية والقيمة  
- استكشاف المفاهيم الأساسية لإطار عمل Microsoft Agent
- أنماط MAF المتقدمة: سير العمل، الوسيط، والذاكرة

## أهداف التعلم

بعد إتمام هذا الدرس، ستعرف كيف:

- بناء وكلاء ذكاء اصطناعي جاهزين للإنتاج باستخدام إطار عمل Microsoft Agent
- تطبيق الميزات الأساسية لإطار عمل Microsoft Agent على حالات الاستخدام الوكالي الخاصة بك
- استخدام أنماط متقدمة بما في ذلك سير العمل، الوسيط، والمراقبة

## عينات الشفرة

عينات الشفرة لـ [Microsoft Agent Framework (MAF)](https://aka.ms/ai-agents-beginners/agent-framewrok) يمكن العثور عليها في هذا المستودع تحت ملفات `xx-python-agent-framework` و`xx-dotnet-agent-framework`.

## فهم إطار عمل Microsoft Agent

![Framework Intro](../../../translated_images/ar/framework-intro.077af16617cf130c.webp)

[Microsoft Agent Framework (MAF)](https://aka.ms/ai-agents-beginners/agent-framewrok) هو الإطار الموحد لمايكروسوفت لبناء وكلاء الذكاء الاصطناعي. يوفر المرونة لمعالجة مجموعة متنوعة من حالات الاستخدام الوكالي التي تُرى في بيئات الإنتاج والبحث بما في ذلك:

- **تنسيق الوكيل المتسلسل** في السيناريوهات التي تتطلب سير عمل خطوة بخطوة.
- **التنسيق المتزامن** في السيناريوهات التي تحتاج فيها الوكلاء لإتمام المهام في الوقت نفسه.
- **تنسيق الدردشة الجماعية** في السيناريوهات التي يمكن للوكلاء التعاون معًا في مهمة واحدة.
- **تنسيق التسليم** في السيناريوهات التي يسلم فيها الوكلاء المهام لبعضهم البعض مع اكتمال المهام الفرعية.
- **التنسيق المغناطيسي** في السيناريوهات التي يُنشئ فيها وكيل مدير قائمة مهام ويُعدلها ويتولى تنسيق الوكلاء الفرعيين لإكمال المهمة.

لتقديم وكلاء ذكاء اصطناعي في الإنتاج، يتضمن MAF أيضًا ميزات لـ:

- **المراقبة** من خلال استخدام OpenTelemetry حيث يتم تتبع كل إجراء للوكيل بما في ذلك استدعاء الأدوات، خطوات التنسيق، تدفقات التفكير، ومراقبة الأداء عبر لوحات تحكم Microsoft Foundry.
- **الأمان** باستضافة الوكلاء محليًا على Microsoft Foundry الذي يشمل ضوابط أمان مثل الوصول المبني على الأدوار، معالجة البيانات الخاصة، والسلامة المدمجة للمحتوى.
- **المتانة** إذ يمكن أن تتوقف خيوط الوكيل وسير العمل مؤقتًا وتستأنف وتتعافى من الأخطاء، مما يتيح عمليات طويلة الأمد.
- **التحكم** حيث يتم دعم سير عمل بإشراف بشري ويتم تعليم المهام التي تتطلب موافقة بشرية.

يركز إطار عمل Microsoft Agent أيضًا على التوافق من خلال:

- **عدم التقييد بالسحابة** - يمكن تشغيل الوكلاء في الحاويات، على الخوادم المحلية وعبر سحابات متعددة.
- **عدم التقييد بمزود الخدمة** - يمكن إنشاء الوكلاء باستخدام SDK المفضل لديك بما في ذلك Azure OpenAI وOpenAI.
- **دمج المعايير المفتوحة** - يمكن للوكلاء استخدام بروتوكولات مثل Agent-to-Agent (A2A) وبروتوكول سياق النموذج (MCP) لاكتشاف واستخدام وكلاء وأدوات أخرى.
- **الإضافات والموصلات** - يمكن إجراء اتصالات بخدمات البيانات والذاكرة مثل Microsoft Fabric، SharePoint، Pinecone وQdrant.

لنلق نظرة على كيفية تطبيق هذه الميزات على بعض المفاهيم الأساسية لإطار عمل Microsoft Agent.

## المفاهيم الأساسية لإطار عمل Microsoft Agent

### الوكلاء

![Agent Framework](../../../translated_images/ar/agent-components.410a06daf87b4fef.webp)

**إنشاء الوكلاء**

يتم إنشاء الوكلاء عن طريق تعريف خدمة الاستدلال (مزود LLM)، مجموعة التعليمات التي يجب على وكيل الذكاء الاصطناعي اتباعها، و`الاسم` المعين:

```python
agent = AzureOpenAIChatClient(credential=AzureCliCredential()).create_agent( instructions="You are good at recommending trips to customers based on their preferences.", name="TripRecommender" )
```

ما سبق يستخدم `Azure OpenAI` ولكن يمكن إنشاء الوكلاء باستخدام مجموعة متنوعة من الخدمات بما في ذلك `Microsoft Foundry Agent Service`:

```python
AzureAIAgentClient(async_credential=credential).create_agent( name="HelperAgent", instructions="You are a helpful assistant." ) as agent
```

OpenAI `Responses`، واجهات برمجة التطبيقات `ChatCompletion`

```python
agent = OpenAIResponsesClient().create_agent( name="WeatherBot", instructions="You are a helpful weather assistant.", )
```

```python
agent = OpenAIChatClient().create_agent( name="HelpfulAssistant", instructions="You are a helpful assistant.", )
```

أو الوكلاء عن بعد باستخدام بروتوكول A2A:

```python
agent = A2AAgent( name=agent_card.name, description=agent_card.description, agent_card=agent_card, url="https://your-a2a-agent-host" )
```

**تشغيل الوكلاء**

يتم تشغيل الوكلاء باستخدام طرق `.run` أو `.run_stream` للردود غير المتدفقة أو المتدفقة على التوالي.

```python
result = await agent.run("What are good places to visit in Amsterdam?")
print(result.text)
```

```python
async for update in agent.run_stream("What are the good places to visit in Amsterdam?"):
    if update.text:
        print(update.text, end="", flush=True)

```

يمكن لكل تشغيل وكيل أن يحتوي أيضًا على خيارات لتخصيص المعلمات مثل `max_tokens` المستخدم من قبل الوكيل، `tools` التي يمكن للوكيل استدعاؤها، وحتى `النموذج` نفسه المستخدم للوكيل.

هذا مفيد في الحالات التي تتطلب نماذج أو أدوات محددة لإكمال مهمة المستخدم.

**الأدوات**

يمكن تعريف الأدوات عند تعريف الوكيل:

```python
def get_attractions( location: Annotated[str, Field(description="The location to get the top tourist attractions for")], ) -> str: """Get the top tourist attractions for a given location.""" return f"The top attractions for {location} are." 


# عند إنشاء ChatAgent مباشرةً

agent = ChatAgent( chat_client=OpenAIChatClient(), instructions="You are a helpful assistant", tools=[get_attractions]

```

وأيضًا عند تشغيل الوكيل:

```python

result1 = await agent.run( "What's the best place to visit in Seattle?", tools=[get_attractions] # الأداة المقدمة لهذا التشغيل فقط )
```

**خيوط الوكلاء**

تُستخدم خيوط الوكلاء للتعامل مع المحادثات متعددة الأدوار. يمكن إنشاء الخيوط إما عن طريق:

- استخدام `get_new_thread()` الذي يُمكن حفظ الخيط مع مرور الوقت
- إنشاء خيط تلقائيًا عند تشغيل الوكيل ويستمر الخيط فقط خلال التشغيل الحالي.

لإنشاء خيط، يبدو الكود كما يلي:

```python
# أنشئ خيطًا جديدًا.
thread = agent.get_new_thread() # شغّل الوكيل مع الخيط.
response = await agent.run("Hello, I am here to help you book travel. Where would you like to go?", thread=thread)

```

يمكنك بعد ذلك تسلسل الخيط ليتم تخزينه للاستخدام لاحقًا:

```python
# إنشاء موضوع جديد.
thread = agent.get_new_thread() 

# تشغيل الوكيل مع الموضوع.

response = await agent.run("Hello, how are you?", thread=thread) 

# تحويل الموضوع إلى بيانات متسلسلة للتخزين.

serialized_thread = await thread.serialize() 

# فك تسلسل حالة الموضوع بعد التحميل من التخزين.

resumed_thread = await agent.deserialize_thread(serialized_thread)
```

**الوسيط الخاص بالوكيل**

يتفاعل الوكلاء مع الأدوات ونماذج LLM لإكمال مهام المستخدم. في بعض السيناريوهات، نريد تنفيذ أو تتبع ما بين هذه التفاعلات. الوسيط الخاص بالوكيل يتيح لنا فعل ذلك من خلال:

*برنامج وسيط الوظيفة*

يسمح هذا الوسيط بتنفيذ إجراء بين الوكيل والوظيفة أو الأداة التي سيتم استدعاؤها. مثال على استخدامه هو عندما ترغب في تسجيل بعض العمليات أثناء استدعاء الوظيفة.

في الكود أدناه، `next` يحدد ما إذا كان يجب استدعاء الوسيط التالي أو الوظيفة الفعلية.

```python
async def logging_function_middleware(
    context: FunctionInvocationContext,
    next: Callable[[FunctionInvocationContext], Awaitable[None]],
) -> None:
    """Function middleware that logs function execution."""
    # المعالجة المسبقة: تسجيل قبل تنفيذ الدالة
    print(f"[Function] Calling {context.function.name}")

    # المتابعة إلى الوسط أو تنفيذ الدالة التالية
    await next(context)

    # المعالجة اللاحقة: تسجيل بعد تنفيذ الدالة
    print(f"[Function] {context.function.name} completed")
```

*برنامج وسيط الدردشة*

هذا الوسيط يسمح لنا بتنفيذ أو تسجيل إجراء بين الوكيل والطلبات بين نموذج اللغة.

يحتوي هذا على معلومات مهمة مثل `الرسائل` التي يتم إرسالها إلى خدمة الذكاء الاصطناعي.

```python
async def logging_chat_middleware(
    context: ChatContext,
    next: Callable[[ChatContext], Awaitable[None]],
) -> None:
    """Chat middleware that logs AI interactions."""
    # المعالجة الأولية: تسجيل قبل استدعاء الذكاء الاصطناعي
    print(f"[Chat] Sending {len(context.messages)} messages to AI")

    # المتابعة إلى البرمجية الوسيطة التالية أو خدمة الذكاء الاصطناعي
    await next(context)

    # المعالجة اللاحقة: تسجيل بعد استجابة الذكاء الاصطناعي
    print("[Chat] AI response received")

```

**ذاكرة الوكيل**

كما تم تغطيته في درس `Agentic Memory`، الذاكرة عنصر مهم لتمكين الوكيل من العمل عبر سياقات مختلفة. يوفر MAF عدة أنواع مختلفة من الذكريات:

*التخزين في الذاكرة*

هذه هي الذاكرة المخزنة في الخيوط خلال وقت تشغيل التطبيق.

```python
# إنشاء مؤشر ترابط جديد.
thread = agent.get_new_thread() # تشغيل الوكيل مع مؤشر الترابط.
response = await agent.run("Hello, I am here to help you book travel. Where would you like to go?", thread=thread)
```

*الرسائل الدائمة*

تستخدم هذه الذاكرة لتخزين سجل المحادثة عبر جلسات مختلفة. يتم تعريفها باستخدام `chat_message_store_factory`:

```python
from agent_framework import ChatMessageStore

# إنشاء مخزن رسائل مخصص
def create_message_store():
    return ChatMessageStore()

agent = ChatAgent(
    chat_client=OpenAIChatClient(),
    instructions="You are a Travel assistant.",
    chat_message_store_factory=create_message_store
)

```

*الذاكرة الديناميكية*

تُضاف هذه الذاكرة إلى السياق قبل تشغيل الوكلاء. يمكن تخزين هذه الذكريات في خدمات خارجية مثل mem0:

```python
from agent_framework.mem0 import Mem0Provider

# استخدام Mem0 لقدرات الذاكرة المتقدمة
memory_provider = Mem0Provider(
    api_key="your-mem0-api-key",
    user_id="user_123",
    application_id="my_app"
)

agent = ChatAgent(
    chat_client=OpenAIChatClient(),
    instructions="You are a helpful assistant with memory.",
    context_providers=memory_provider
)

```

**مراقبة الوكيل**

المراقبة مهمة لبناء أنظمة وكيل موثوقة وقابلة للصيانة. يدمج MAF مع OpenTelemetry لتوفير التتبع والعدادات لرصد أفضل.

```python
from agent_framework.observability import get_tracer, get_meter

tracer = get_tracer()
meter = get_meter()
with tracer.start_as_current_span("my_custom_span"):
    # قم بشيء ما
    pass
counter = meter.create_counter("my_custom_counter")
counter.add(1, {"key": "value"})
```

### سير العمل

يقدم MAF سير عمل هي خطوات محددة مسبقًا لإكمال مهمة وتتضمن وكلاء الذكاء الاصطناعي كمكونات في تلك الخطوات.

يتألف سير العمل من مكونات مختلفة تسمح بتحكم أفضل في التدفق. كما يتيح سير العمل **تنسيق عدة وكلاء** و**حفظ نقاط التفتيش** لحفظ حالات سير العمل.

المكونات الأساسية لسير العمل هي:

**المنفذون (Executors)**

يتلقى المنفذون رسائل الإدخال، ينفذون المهام الموكلة إليهم، ثم ينتجون رسالة إخراج. هذا يدفع سير العمل نحو إكمال المهمة الأكبر. يمكن أن يكون المنفذ وكيل ذكاء اصطناعي أو منطق مخصص.

**الحواف (Edges)**

تُستخدم الحواف لتعريف تدفق الرسائل في سير العمل. يمكن أن تكون:

*حواف مباشرة* - اتصالات بسيطة واحد إلى واحد بين المنفذين:

```python
from agent_framework import WorkflowBuilder

builder = WorkflowBuilder()
builder.add_edge(source_executor, target_executor)
builder.set_start_executor(source_executor)
workflow = builder.build()
```

*حواف شرطية* - تُفعّل بعد تحقق شرط معين. على سبيل المثال، عندما تكون غرف الفنادق غير متوفرة، يمكن للمنفذ اقتراح خيارات أخرى.

*حواف تبديل الحالة* - توجه الرسائل إلى منفذين مختلفين بناءً على شروط محددة. على سبيل المثال، إذا كان لدى عميل السفر وصول ذو أولوية، فسيتم التعامل مع مهامه من خلال سير عمل آخر.

*حواف التفرع* - ترسل رسالة واحدة إلى عدة أهداف.

*حواف التجميع* - تجمع رسائل متعددة من منفذين مختلفين وترسل إلى هدف واحد.

**الأحداث**

لتوفير مراقبة أفضل لسير العمل، يقدم MAF أحداثًا مدمجة للتنفيذ تشمل:

- `WorkflowStartedEvent`  - يبدأ تنفيذ سير العمل
- `WorkflowOutputEvent` - يولد سير العمل إخراجًا
- `WorkflowErrorEvent` - يواجه سير العمل خطأ
- `ExecutorInvokeEvent`  - يبدأ المنفذ المعالجة
- `ExecutorCompleteEvent`  - ينهي المنفذ المعالجة
- `RequestInfoEvent` - تم إصدار طلب

## أنماط MAF المتقدمة

الأقسام السابقة تغطي المفاهيم الرئيسية لإطار عمل Microsoft Agent. مع بناء وكلاء أكثر تعقيدًا، إليك بعض الأنماط المتقدمة للنظر فيها:

- **تأليف الوسيط**: ربط عدة معالجات وسيطة (تسجيل الدخول، التفويض، تحديد المعدل) باستخدام وسيط الوظيفة والدردشة للتحكم الدقيق بسلوك الوكيل.
- **حفظ نقاط تفتيش سير العمل**: استخدام أحداث سير العمل والتسلسل لحفظ واستئناف عمليات الوكيل طويلة الأمد.
- **اختيار الأدوات الديناميكي**: الجمع بين RAG على وصف الأدوات وتسجيل الأدوات في MAF لعرض الأدوات ذات الصلة فقط لكل استعلام.
- **تسليم متعدد الوكلاء**: استخدام حواف سير العمل والتوجيه الشرطي لتنسيق التسليم بين الوكلاء المتخصصين.

## عينات الشفرة

عينات الشفرة لإطار عمل Microsoft Agent يمكن العثور عليها في هذا المستودع تحت ملفات `xx-python-agent-framework` و`xx-dotnet-agent-framework`.

## هل لديك المزيد من الأسئلة حول إطار عمل Microsoft Agent؟

انضم إلى [Microsoft Foundry Discord](https://aka.ms/ai-agents/discord) للاحتكاك مع متعلمين آخرين، حضور ساعات المكتب، والحصول على إجابات لأسئلتك حول وكلاء الذكاء الاصطناعي.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**تنويه**:  
تمت ترجمة هذا المستند باستخدام خدمة الترجمة الآلية [Co-op Translator](https://github.com/Azure/co-op-translator). بينما نسعى لتحقيق الدقة، يرجى العلم أن الترجمات الآلية قد تحتوي على أخطاء أو عدم دقة. يجب اعتبار المستند الأصلي بلغته الأصلية هو المصدر الرسمي والمعتمد. للمعلومات الحرجة، يُنصح بالاعتماد على الترجمة البشرية المهنية. نحن غير مسؤولين عن أي سوء فهم أو تفسيرات خاطئة ناتجة عن استخدام هذه الترجمة.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->