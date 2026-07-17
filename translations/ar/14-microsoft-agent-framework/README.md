# استكشاف إطار عمل وكيل مايكروسوفت

![Agent Framework](../../../translated_images/ar/lesson-14-thumbnail.90df0065b9d234ee.webp)

### مقدمة

ستغطي هذه الدرس:

- فهم إطار عمل وكيل مايكروسوفت: الميزات الرئيسية والقيمة  
- استكشاف المفاهيم الرئيسية لإطار عمل وكيل مايكروسوفت
- أنماط MAF المتقدمة: تدفقات العمل، الوسائط الوسيطة، والذاكرة

## أهداف التعلم

بعد إكمال هذا الدرس، ستعرف كيفية:

- بناء وكلاء ذكاء صناعي جاهزين للإنتاج باستخدام إطار عمل وكيل مايكروسوفت
- تطبيق الميزات الأساسية لإطار عمل وكيل مايكروسوفت على حالات الاستخدام الوكالية الخاصة بك
- استخدام أنماط متقدمة تشمل تدفقات العمل، الوسائط الوسيطة، والرصد

## عينات الكود 

يمكن العثور على عينات الكود الخاصة بـ [Microsoft Agent Framework (MAF)](https://aka.ms/ai-agents-beginners/agent-framework) في هذا المستودع تحت ملفات `xx-python-agent-framework` و `xx-dotnet-agent-framework`.

## فهم إطار عمل وكيل مايكروسوفت

![Framework Intro](../../../translated_images/ar/framework-intro.077af16617cf130c.webp)

[إطار عمل وكيل مايكروسوفت (MAF)](https://aka.ms/ai-agents-beginners/agent-framework) هو الإطار الموحد لمايكروسوفت لبناء وكلاء الذكاء الصناعي. يوفر المرونة لمعالجة التنوع الكبير في حالات الاستخدام الوكالية التي تُرى في كل من بيئات الإنتاج والبحوث بما في ذلك:

- **تنسيق العملاء المتسلسل** في السيناريوهات التي تحتاج إلى تدفقات عمل خطوة بخطوة.
- **التنسيق المتزامن** في السيناريوهات التي يحتاج فيها العملاء لإكمال المهام في نفس الوقت.
- **تنسيق محادثات المجموعة** في السيناريوهات التي يمكن للعملاء التعاون فيها معًا على مهمة واحدة.
- **تنسيق التسليم** في السيناريوهات التي يسلم فيها العملاء المهمة لبعضهم البعض مع إكمال المهام الفرعية.
- **التنسيق المغناطيسي** في السيناريوهات التي ينشئ فيها وكيل المدير ويعدل قائمة المهام ويتولى تنسيق الوكلاء الفرعيين لإكمال المهمة.

لتقديم وكلاء الذكاء الصناعي في الإنتاج، يتضمن MAF أيضًا ميزات لـ:

- **الرصد** من خلال استخدام OpenTelemetry حيث يتم تتبع كل إجراء لوكيل الذكاء الصناعي بما في ذلك استدعاء الأدوات، خطوات التنسيق، تدفقات الاستدلال، ومراقبة الأداء من خلال لوحات معلومات Microsoft Foundry.
- **الأمان** عن طريق استضافة الوكلاء محليًا على Microsoft Foundry التي تتضمن ضوابط أمان مثل التحكم في الوصول بناءً على الدور، التعامل مع البيانات الخاصة، والسلامة المدمجة للمحتوى.
- **الدوام** حيث يمكن أن تتوقف خيوط الوكيل وتدفقات العمل، ثم تستأنف وتتعافى من الأخطاء مما يتيح عمليات تشغيل لفترة أطول.
- **التحكم** حيث يتم دعم تدفقات العمل التي تتطلب تدخل الإنسان حيث يتم تمييز المهام على أنها بحاجة إلى موافقة بشرية.

يركز إطار عمل وكيل مايكروسوفت أيضًا على التوافقية من خلال:

- **الاستقلالية عن السحابة** - يمكن تشغيل الوكلاء في حاويات، على الأنظمة المحلية وعبر سُحب متعددة مختلفة.
- **الاستقلالية عن المزود** - يمكن إنشاء الوكلاء عبر SDK المفضل لديك بما في ذلك Azure OpenAI و OpenAI
- **دمج المعايير المفتوحة** - يمكن للوكلاء استخدام بروتوكولات مثل وكيل إلى وكيل (A2A) وبروتوكول سياق النموذج (MCP) لاكتشاف واستخدام وكلاء وأدوات أخرى.
- **الإضافات والموصلات** - يمكن إنشاء اتصالات بخدمات البيانات والذاكرة مثل Microsoft Fabric و SharePoint و Pinecone و Qdrant.

لنلقِ نظرة على كيفية تطبيق هذه الميزات على بعض المفاهيم الأساسية لإطار عمل وكيل مايكروسوفت.

## المفاهيم الأساسية لإطار عمل وكيل مايكروسوفت

### الوكلاء

![Agent Framework](../../../translated_images/ar/agent-components.410a06daf87b4fef.webp)

**إنشاء الوكلاء**

يتم إنشاء الوكيل عن طريق تعريف خدمة الاستدلال (مقدم LLM)،
مجموعة من التعليمات التي يجب على وكيل الذكاء الاصطناعي اتباعها، و`الاسم` المخصص:

```python
agent = AzureOpenAIChatClient(credential=AzureCliCredential()).create_agent( instructions="You are good at recommending trips to customers based on their preferences.", name="TripRecommender" )
```

المثال أعلاه يستخدم `Azure OpenAI` لكن يمكن إنشاء الوكلاء باستخدام مجموعة متنوعة من الخدمات بما في ذلك `خدمة وكيل Microsoft Foundry`:

```python
AzureAIAgentClient(async_credential=credential).create_agent( name="HelperAgent", instructions="You are a helpful assistant." ) as agent
```

واجهات OpenAI `Responses`، و`ChatCompletion`

```python
agent = OpenAIResponsesClient().create_agent( name="WeatherBot", instructions="You are a helpful weather assistant.", )
```

```python
agent = OpenAIChatClient().create_agent( name="HelpfulAssistant", instructions="You are a helpful assistant.", )
```

أو [MiniMax](https://platform.minimaxi.com/)، التي توفر واجهة برمجة تطبيقات متوافقة مع OpenAI مع نوافذ سياق كبيرة (حتى 204 ألف رمز):

```python
agent = OpenAIChatClient(base_url="https://api.minimax.io/v1", api_key=os.environ["MINIMAX_API_KEY"], model_id="MiniMax-M3").create_agent( name="HelpfulAssistant", instructions="You are a helpful assistant.", )
```

أو وكلاء بعيدين باستخدام بروتوكول A2A:

```python
agent = A2AAgent( name=agent_card.name, description=agent_card.description, agent_card=agent_card, url="https://your-a2a-agent-host" )
```

**تشغيل الوكلاء**

يتم تشغيل الوكلاء باستخدام طُرق `.run` أو `.run_stream` للحصول على استجابات غير متدفقة أو متدفقة.

```python
result = await agent.run("What are good places to visit in Amsterdam?")
print(result.text)
```

```python
async for update in agent.run_stream("What are the good places to visit in Amsterdam?"):
    if update.text:
        print(update.text, end="", flush=True)

```

يمكن أيضًا لكل تشغيل وكيل أن يحتوي على خيارات لتخصيص المعاملات مثل `max_tokens` المستخدمة من قبل الوكيل، و`الأدوات` التي يمكن للوكيل استدعاؤها، وحتى `النموذج` نفسه المستخدم للوكيل.

هذا مفيد في الحالات التي تتطلب فيها نماذج أو أدوات محددة لإكمال مهمة المستخدم.

**الأدوات**

يمكن تحديد الأدوات عند تعريف الوكيل:

```python
def get_attractions( location: Annotated[str, Field(description="The location to get the top tourist attractions for")], ) -> str: """Get the top tourist attractions for a given location.""" return f"The top attractions for {location} are." 


# عند إنشاء وكيل الدردشة مباشرة

agent = ChatAgent( chat_client=OpenAIChatClient(), instructions="You are a helpful assistant", tools=[get_attractions]

```

وأيضًا عند تشغيل الوكيل:

```python

result1 = await agent.run( "What's the best place to visit in Seattle?", tools=[get_attractions] # أداة مقدمة لهذه الجلسة فقط )
```

**خيوط الوكيل**

تُستخدم خيوط الوكيل للتعامل مع المحادثات متعددة الدوران. يمكن إنشاء الخيوط إما بـ:

- استخدام `get_new_thread()` الذي يمكن من حفظ الخيط مع مرور الوقت
- إنشاء خيط تلقائيًا عند تشغيل وكيل ويستمر فقط أثناء التشغيل الحالي.

لإنشاء خيط، يبدو الكود هكذا:

```python
# إنشاء موضوع جديد.
thread = agent.get_new_thread() # تشغيل الوكيل مع الموضوع.
response = await agent.run("Hello, I am here to help you book travel. Where would you like to go?", thread=thread)

```

يمكنك بعد ذلك تسلسل الخيط ليتم تخزينه للاستخدام لاحقًا:

```python
# إنشاء مؤشر ترابط جديد.
thread = agent.get_new_thread() 

# تشغيل الوكيل مع مؤشر الترابط.

response = await agent.run("Hello, how are you?", thread=thread) 

# تسلسل مؤشر الترابط للتخزين.

serialized_thread = await thread.serialize() 

# فك تسلسل حالة مؤشر الترابط بعد التحميل من التخزين.

resumed_thread = await agent.deserialize_thread(serialized_thread)
```

**الوسائط الوسيطة للوكيل**

يتفاعل الوكلاء مع الأدوات وLLMs لإكمال مهام المستخدم. في سيناريوهات معينة، نرغب في تنفيذ أو تتبع عمليات ما بين هذه التفاعلات. الوسائط الوسيطة للوكيل تتيح لنا القيام بذلك من خلال:

*الوسائط الوسيطة الدالية*

هذه الوسائط تتيح لنا تنفيذ إجراء بين الوكيل والدالة/الأداة التي سيستدعيها. مثال على استخدام هذه الحالة هو عندما ترغب في تسجيل استدعاء الدالة.

في الكود أدناه `next` يحدد ما إذا كان يجب استدعاء الوسيط التالي أو الدالة الفعلية.

```python
async def logging_function_middleware(
    context: FunctionInvocationContext,
    next: Callable[[FunctionInvocationContext], Awaitable[None]],
) -> None:
    """Function middleware that logs function execution."""
    # المعالجة المسبقة: تسجيل دخول قبل تنفيذ الدالة
    print(f"[Function] Calling {context.function.name}")

    # الاستمرار إلى البرنامج الوسيط التالي أو تنفيذ الدالة
    await next(context)

    # المعالجة اللاحقة: تسجيل دخول بعد تنفيذ الدالة
    print(f"[Function] {context.function.name} completed")
```

*الوسائط الوسيطة للمحادثة*

هذه الوسائط تتيح لنا تنفيذ أو تسجيل إجراء بين الوكيل والطلبات بين LLM.

تحتوي هذه على معلومات مهمة مثل `الرسائل` التي تُرسل إلى خدمة الذكاء الاصطناعي.

```python
async def logging_chat_middleware(
    context: ChatContext,
    next: Callable[[ChatContext], Awaitable[None]],
) -> None:
    """Chat middleware that logs AI interactions."""
    # المعالجة المسبقة: تسجيل قبل استدعاء الذكاء الاصطناعي
    print(f"[Chat] Sending {len(context.messages)} messages to AI")

    # المتابعة إلى الوسيط التالي أو خدمة الذكاء الاصطناعي
    await next(context)

    # المعالجة اللاحقة: تسجيل بعد استجابة الذكاء الاصطناعي
    print("[Chat] AI response received")

```

**ذاكرة الوكيل**

كما تم تغطيته في درس `ذاكرة الوكيل`، الذاكرة عنصر مهم لتمكين الوكيل من العمل عبر سياقات مختلفة. يوفر MAF عدة أنواع مختلفة من الذكريات:

*التخزين داخل الذاكرة*

هذه هي الذاكرة المخزنة في الخيوط أثناء وقت تشغيل التطبيق.

```python
# إنشاء خيط جديد.
thread = agent.get_new_thread() # تشغيل الوكيل مع الخيط.
response = await agent.run("Hello, I am here to help you book travel. Where would you like to go?", thread=thread)
```

*الرسائل المستمرة*

تُستخدم هذه الذاكرة عند حفظ تاريخ المحادثة عبر جلسات مختلفة. يتم تعريفها باستخدام `chat_message_store_factory` :

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

**رصد الوكيل**

الرصد مهم لبناء أنظمة وكيلة موثوقة وقابلة للصيانة. يدمج MAF مع OpenTelemetry لتوفير تتبع ومقاييس لرصد أفضل.

```python
from agent_framework.observability import get_tracer, get_meter

tracer = get_tracer()
meter = get_meter()
with tracer.start_as_current_span("my_custom_span"):
    # قم بشيء
    pass
counter = meter.create_counter("my_custom_counter")
counter.add(1, {"key": "value"})
```

### تدفقات العمل

يقدم MAF تدفقات عمل هي خطوات محددة مسبقًا لإكمال مهمة وتضم وكلاء الذكاء الصناعي كمكونات في تلك الخطوات.

تتكون تدفقات العمل من مكونات مختلفة تسمح بتحكم أفضل في التدفق. كما تتيح تدفقات العمل **تنسيقًا متعدد الوكلاء** و**حفظ النقاط المرجعية** لحفظ حالات تدفق العمل.

المكونات الأساسية لتدفق العمل هي:

**المنفذون**

يستقبل المنفذون رسائل الإدخال، يؤدون مهامهم المعينة، ثم ينتجون رسالة إخراج. هذا يحرك تدفق العمل نحو إكمال المهمة الأكبر. يمكن أن يكون المنفذون وكلاء ذكاء صناعي أو منطق مخصص.

**الحواف**

تُستخدم الحواف لتعريف تدفق الرسائل في تدفق العمل. يمكن أن تكون:

*الحواف المباشرة* - اتصالات بسيطة من واحد إلى واحد بين المنفذين:

```python
from agent_framework import WorkflowBuilder

builder = WorkflowBuilder()
builder.add_edge(source_executor, target_executor)
builder.set_start_executor(source_executor)
workflow = builder.build()
```

*الحواف الشرطية* - تُفعل بعد تحقق شرط معين. على سبيل المثال، عندما تكون غرف الفنادق غير متوفرة، يمكن للمنفذ اقتراح خيارات أخرى.

*حواف حالة التبديل* - توجيه الرسائل إلى منفذين مختلفين بناءً على شروط محددة. على سبيل المثال، إذا كان لدى زبون السفر وصول ذي أولوية، ستتم معالجة مهامه من خلال تدفق عمل آخر.

*حواف التوزيع* - إرسال رسالة واحدة إلى أهداف متعددة.

*حواف التجميع* - جمع رسائل متعددة من منفذين مختلفين وإرسالها إلى هدف واحد.

**الأحداث**

لتوفير رصد أفضل لتدفقات العمل، يقدم MAF أحداثًا مدمجة للتنفيذ تشمل:

- `WorkflowStartedEvent`  - بدء تنفيذ تدفق العمل
- `WorkflowOutputEvent` - إنتاج تدفق العمل لإخراج
- `WorkflowErrorEvent` - مواجهة تدفق العمل لخطأ
- `ExecutorInvokeEvent`  - بدء المعالج للمعالجة
- `ExecutorCompleteEvent`  - الانتهاء من المعالجة من قبل المعالج
- `RequestInfoEvent` - إصدار طلب

## أنماط MAF المتقدمة

تغطي الأقسام أعلاه المفاهيم الرئيسية لإطار عمل وكيل مايكروسوفت. أثناء بناء وكلاء أكثر تعقيدًا، إليك بعض الأنماط المتقدمة للنظر فيها:

- **تركيب الوسائط الوسيطة**: ربط العديد من معالجات الوسائط الوسيطة (التسجيل، المصادقة، تحديد المعدل) باستخدام الوسائط الوسيطة الدالية والمحادثة للتحكم الدقيق في سلوك الوكيل.
- **حفظ نقاط تدفق العمل**: استخدام أحداث تدفق العمل والتسلسل لحفظ واستئناف عمليات الوكيل طويلة الأمد.
- **اختيار الأدوات الديناميكي**: دمج RAG على وصف الأدوات مع تسجيل أدوات MAF لتقديم الأدوات المناسبة فقط لكل استعلام.
- **تسليم متعدد الوكلاء**: استخدام حواف تدفق العمل والتوجيه الشرطي لتنسيق التسليم بين وكلاء متخصصين.

## استضافة وكلاء LangChain / LangGraph على Microsoft Foundry

إطار عمل وكيل مايكروسوفت هو **متوافق مع أطر عمل أخرى** — لست مقيدًا بالوكلاء المكتوبين بـ MAF. إذا كان لديك وكيل بالفعل مبني بـ **LangChain** أو **LangGraph**، يمكنك تشغيله كـ **وكيل مستضاف على Microsoft Foundry** بحيث تقوم Foundry بإدارة وقت التشغيل، الجلسات، التوسع، الهوية، ونقاط نهاية البروتوكول لك، بينما يبقى منطق وكيلك في LangGraph.

يتم ذلك باستخدام حزمة `langchain_azure_ai.agents.hosting`، التي تعرض رسم LangGraph مجمع عبر نفس البروتوكولات التي يستخدمها وكلاء Foundry المستضافين.

**1. تثبيت الإضافة الخاصة بالاستضافة:**

```bash
pip install -U "langchain-azure-ai[hosting]>=1.2.4" azure-identity
```

يقوم الإضافة `hosting` بتثبيت مكتبات بروتوكول Foundry: `azure-ai-agentserver-responses` (نقطة نهاية `/responses` المتوافقة مع OpenAI) و `azure-ai-agentserver-invocations` (نقطة النهاية العامة `/invocations`).

**2. اختر بروتوكول استضافة:**

| البروتوكول | فئة المضيف | نقطة النهاية | متى تستخدم |
|----------|-----------|----------|----------|
| **Responses** | `ResponsesHostServer` | `/responses` | ترغب في دردشة متوافقة مع OpenAI، بث، سجل الردود، وربط المحادثة — الخيار الافتراضي الموصى به للوكلاء المحادثين. |
| **Invocations** | `InvocationsHostServer` | `/invocations` | تحتاج إلى شكل JSON مخصص، أو نقطة نهاية نمط webhook، أو معالجة غير محادثية. |

لأن **واجهة Responses API هي الواجهة الأساسية لتطوير وكلاء الأسلوب في Foundry**، ابدأ بـ `ResponsesHostServer` لمعظم الوكلاء.

**3. تكوين متغيرات البيئة** (`az login` أولاً حتى يمكن لـ `DefaultAzureCredential` المصادقة):

```bash
export FOUNDRY_PROJECT_ENDPOINT="https://<resource>.services.ai.azure.com/api/projects/<project>"
export FOUNDRY_MODEL_NAME="gpt-4.1"
```

عندما يعمل الوكيل لاحقًا كوكيل مستضاف في Foundry، يقوم النظام بحقن `FOUNDRY_PROJECT_ENDPOINT` تلقائيًا.

**4. عرض وكيل LangGraph عبر بروتوكول Responses:**

```python
import os

from azure.ai.projects import AIProjectClient
from azure.identity import DefaultAzureCredential, get_bearer_token_provider
from langchain.agents import create_agent
from langchain_openai import ChatOpenAI
from langchain_azure_ai.agents.hosting import ResponsesHostServer

_AZURE_AI_SCOPE = "https://ai.azure.com/.default"


def build_chat_model() -> ChatOpenAI:
    project_endpoint = os.environ["FOUNDRY_PROJECT_ENDPOINT"].rstrip("/")
    deployment = os.environ.get("FOUNDRY_MODEL_NAME", "gpt-4.1")
    credential = DefaultAzureCredential()
    project = AIProjectClient(endpoint=project_endpoint, credential=credential)
    openai_client = project.get_openai_client()
    token_provider = get_bearer_token_provider(credential, _AZURE_AI_SCOPE)

    # هنا يستهدف ChatOpenAI نقطة النهاية (Responses) المتوافقة مع OpenAI الخاصة بمشروع Foundry.
    return ChatOpenAI(
        model=deployment,
        base_url=str(openai_client.base_url),
        api_key=token_provider,
    )


def main() -> None:
    graph = create_agent(build_chat_model(), tools=[])
    port = int(os.environ.get("PORT", "8088"))
    ResponsesHostServer(graph).run(port=port)


if __name__ == "__main__":
    main()
```

شغّله محليًا باستخدام `python main.py`، ثم أرسل طلب Responses إلى `http://localhost:8088/responses`.

**السلوكيات الرئيسية:**

- **المحادثات**: يواصل العملاء المحادثة بتمرير `previous_response_id` أو معرف `conversation`. إذا تم تجميع رسمك مع نقطة تفتيش LangGraph، يقوم Foundry بمفتاح حالة المحادثة إلى نقطة التفتيش (استخدم نقطة تفتيش دائمة في الإنتاج؛ `MemorySaver` جيد للاختبار المحلي).
- **وجود الإنسان في الحلقة**: إذا استخدم رسمك `interrupt()` في LangGraph، يقوم `ResponsesHostServer` بإظهار الانقطاع المعلق كـ  `function_call` / `mcp_approval_request` في Responses، ويستأنف العملاء بـ `function_call_output` / `mcp_approval_response` المطابقة.
- **النشر على Foundry**: استخدم CLI المطور من Azure — `azd ext install azure.ai.agents`، `azd ai agent init -m <manifest>`, `azd ai agent run` (محلي، يتطلب Docker)، ثم `azd provision` و `azd deploy`. يتطلب نشر الوكيل المستضاف دور **مدير مشروع Foundry**.

نسخة قابلة للتشغيل من هذا المثال موجودة في [code-samples/14-langchain-hosted-agent.py](../../../14-microsoft-agent-framework/code-samples/14-langchain-hosted-agent.py). للشرح الكامل (بروتوكول Invocations، مخططات الطلب المخصصة، واستكشاف الأخطاء)، راجع [استضافة وكلاء LangGraph كعملاء مستضافين في Foundry](https://learn.microsoft.com/azure/foundry/how-to/develop/langchain-hosted-agents).

## عينات الكود 

يمكن العثور على عينات الكود لإطار عمل وكيل مايكروسوفت في هذا المستودع تحت ملفات `xx-python-agent-framework` و `xx-dotnet-agent-framework`.

## هل لديك المزيد من الأسئلة حول إطار عمل وكيل مايكروسوفت؟

انضم إلى [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D) للقاء متعلمين آخرين، حضور ساعات المكتب والحصول على إجابات لأسئلة عملاء الذكاء الاصطناعي الخاصة بك.
## الدرس السابق

[ذاكرة لوكلاء الذكاء الصناعي](../13-agent-memory/README.md)

## الدرس التالي

[بناء وكلاء استخدام الكمبيوتر (CUA)](../15-browser-use/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**تنويه**:
تمت ترجمة هذا المستند باستخدام خدمة الترجمة بالذكاء الاصطناعي [Co-op Translator](https://github.com/Azure/co-op-translator). بينما نسعى للدقة، يرجى العلم أن الترجمات الآلية قد تحتوي على أخطاء أو عدم دقة. يجب اعتبار المستند الأصلي بلغته الأصلية المصدر الرسمي والمعتمد. للمعلومات الهامة، يُنصح بالاستعانة بترجمة بشرية محترفة. نحن غير مسؤولين عن أي سوء فهم أو تفسير ناتج عن استخدام هذه الترجمة.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->