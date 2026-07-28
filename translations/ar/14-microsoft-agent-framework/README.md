# استكشاف إطار عمل Microsoft Agent

![Agent Framework](../../../translated_images/ar/lesson-14-thumbnail.90df0065b9d234ee.webp)

### مقدمة

ستغطي هذه الدرس:

- فهم إطار عمل Microsoft Agent: الميزات الرئيسية والقيمة  
- استكشاف المفاهيم الأساسية لإطار عمل Microsoft Agent
- أنماط MAF المتقدمة: سير العمل، الوسائط الوسيطة، والذاكرة

## أهداف التعلم

بعد إكمال هذا الدرس، ستكون قادراً على:

- بناء وكلاء ذكاء صناعي جاهزين للإنتاج باستخدام إطار عمل Microsoft Agent
- تطبيق الميزات الأساسية لإطار عمل Microsoft Agent في حالات استخدامك الوكيلية
- استخدام الأنماط المتقدمة بما في ذلك سير العمل، الوسائط الوسيطة، والمراقبة

## أمثلة الشفرة 

يمكن العثور على أمثلة الشفرة الخاصة بـ [Microsoft Agent Framework (MAF)](https://aka.ms/ai-agents-beginners/agent-framework) في هذا المستودع ضمن الملفات `xx-python-agent-framework` و `xx-dotnet-agent-framework`.

## فهم إطار عمل Microsoft Agent

![Framework Intro](../../../translated_images/ar/framework-intro.077af16617cf130c.webp)

[Microsoft Agent Framework (MAF)](https://aka.ms/ai-agents-beginners/agent-framework) هو الإطار الموحد من مايكروسوفت لبناء وكلاء الذكاء الاصطناعي. يقدم المرونة لمعالجة مجموعة واسعة من حالات الاستخدام الوكيلية التي تُرى في بيئات الإنتاج والبحث، بما في ذلك:

- **تنسيق الوكيل المتسلسل** في السيناريوهات التي تتطلب سير عمل خطوة بخطوة.
- **التنسيق المتزامن** في السيناريوهات التي يحتاج فيها الوكلاء إلى إكمال المهام في نفس الوقت.
- **تنسيق المحادثة الجماعية** في السيناريوهات التي يمكن أن يتعاون فيها الوكلاء معاً على مهمة واحدة.
- **تنسيق التسليم** في السيناريوهات التي يقوم فيها الوكلاء بتسليم المهمة إلى بعضهم البعض مع إكمال المهام الجزئية.
- **التنسيق المغناطيسي** في السيناريوهات التي ينشئ فيها وكيل المدير ويعدل قائمة المهام ويتولى تنسيق الوكلاء الفرعيين لإكمال المهمة.

لتوفير وكلاء الذكاء الاصطناعي في الإنتاج، يتضمن MAF أيضاً ميزات لـ:

- **المراقبة** من خلال استخدام OpenTelemetry حيث يتم تتبع كل فعل لوكيل الذكاء الاصطناعي بما في ذلك استدعاءات الأدوات، خطوات التنسيق، تدفقات التفكير، ومراقبة الأداء عبر لوحات معلومات Microsoft Foundry.
- **الأمان** باستضافة الوكلاء أصلياً على Microsoft Foundry والتي تتضمن ضوابط أمان مثل الوصول المبني على الدور، معالجة البيانات الخاصة، والسلامة المضمنة للمحتوى.
- **المتانة** حيث يمكن إيقاف واستئناف واسترداد خيوط وأعمال الوكلاء من الأخطاء مما يمكن العمليات طويلة الأمد.
- **التحكم** حيث يتم دعم سير العمل بمشاركة الإنسان حيث تُعلَن المهام على أنها تتطلب موافقة بشرية.

يركز إطار عمل Microsoft Agent أيضاً على التوافقية من خلال:

- **كونه غير مرتبط بالسحابة** - يمكن تشغيل الوكلاء في الحاويات، على الأنظمة المحلية وعبر عدة سحب سحابية مختلفة.
- **كونه غير مرتبط بالمزود** - يمكن إنشاء الوكلاء من خلال SDK المفضل لديك بما في ذلك Azure OpenAI وOpenAI
- **تكامل المعايير المفتوحة** - يمكن للوكلاء استخدام بروتوكولات مثل Agent-to-Agent(A2A) وModel Context Protocol (MCP) لاكتشاف واستخدام وكلاء وأدوات أخرى.
- **الإضافات والموصلات** - يمكن إجراء اتصالات مع خدمات البيانات والذاكرة مثل Microsoft Fabric وSharePoint وPinecone وQdrant.

لنلق نظرة على كيفية تطبيق هذه الميزات على بعض المفاهيم الأساسية لإطار عمل Microsoft Agent.

## المفاهيم الأساسية لإطار عمل Microsoft Agent

### الوكلاء

![Agent Framework](../../../translated_images/ar/agent-components.410a06daf87b4fef.webp)

**إنشاء الوكلاء**

يتم إنشاء الوكيل عن طريق تعريف خدمة الاستدلال (مزود LLM)، مجموعة التعليمات التي يجب على وكيل الذكاء الاصطناعي اتباعها، و`الاسم` المعين:


```python
agent = AzureOpenAIChatClient(credential=AzureCliCredential()).create_agent( instructions="You are good at recommending trips to customers based on their preferences.", name="TripRecommender" )
```

المثال أعلاه يستخدم `Azure OpenAI` لكن يمكن إنشاء الوكلاء باستخدام مجموعة متنوعة من الخدمات بما في ذلك `Microsoft Foundry Agent Service`:

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

أو [MiniMax](https://platform.minimaxi.com/)، التي توفر واجهة برمجة تطبيقات متوافقة مع OpenAI مع نوافذ سياق كبيرة (حتى 204 ألف رمز):

```python
agent = OpenAIChatClient(base_url="https://api.minimax.io/v1", api_key=os.environ["MINIMAX_API_KEY"], model_id="MiniMax-M3").create_agent( name="HelpfulAssistant", instructions="You are a helpful assistant.", )
```

أو الوكلاء البعيدين باستخدام بروتوكول A2A:

```python
agent = A2AAgent( name=agent_card.name, description=agent_card.description, agent_card=agent_card, url="https://your-a2a-agent-host" )
```

**تشغيل الوكلاء**

يتم تشغيل الوكلاء باستخدام طريقتي `.run` أو `.run_stream` للحصول على استجابات غير متدفقة أو متدفقة على التوالي.

```python
result = await agent.run("What are good places to visit in Amsterdam?")
print(result.text)
```

```python
async for update in agent.run_stream("What are the good places to visit in Amsterdam?"):
    if update.text:
        print(update.text, end="", flush=True)

```

يمكن أيضاً تخصيص خيارات لكل تشغيل للوكيل مثل `max_tokens` التي يستخدمها الوكيل، و`tools` التي يستطيع الوكيل استدعاؤها، وحتى `model` المستخدم للوكيل.

هذا مفيد في الحالات التي تتطلب نماذج أو أدوات محددة لإكمال مهمة المستخدم.

**الأدوات**

يمكن تعريف الأدوات أثناء تعريف الوكيل:

```python
def get_attractions( location: Annotated[str, Field(description="The location to get the top tourist attractions for")], ) -> str: """Get the top tourist attractions for a given location.""" return f"The top attractions for {location} are." 


# عند إنشاء ChatAgent مباشرةً

agent = ChatAgent( chat_client=OpenAIChatClient(), instructions="You are a helpful assistant", tools=[get_attractions]

```

وأيضاً عند تشغيل الوكيل:

```python

result1 = await agent.run( "What's the best place to visit in Seattle?", tools=[get_attractions] # الأداة المقدمة لهذا التشغيل فقط )
```

**خيوط الوكيل**

تُستخدم خيوط الوكيل للتعامل مع المحادثات متعددة الدوران. يمكن إنشاء الخيوط إما عن طريق:

- استخدام `get_new_thread()` والتي تمكن من حفظ الخيط مع مرور الوقت
- إنشاء خيط تلقائياً عند تشغيل وكيل وبقاء الخيط فقط خلال التشغيل الحالي.

لإنشاء خيط، يبدو الكود كما يلي:

```python
# قم بإنشاء خيط جديد.
thread = agent.get_new_thread() # شغّل الوكيل مع الخيط.
response = await agent.run("Hello, I am here to help you book travel. Where would you like to go?", thread=thread)

```

ثم يمكنك تسلسل الخيط ليُخزن للاستخدام لاحقاً:

```python
# إنشاء خيط جديد.
thread = agent.get_new_thread() 

# تشغيل الوكيل مع الخيط.

response = await agent.run("Hello, how are you?", thread=thread) 

# تسلسل الخيط للتخزين.

serialized_thread = await thread.serialize() 

# فك تسلسل حالة الخيط بعد التحميل من التخزين.

resumed_thread = await agent.deserialize_thread(serialized_thread)
```

**الوسائط الوسيطة للوكيل**

يتفاعل الوكلاء مع الأدوات وLLMs لإكمال مهام المستخدمين. في بعض السيناريوهات، نريد تنفيذ أو تتبع ما بين هذه التفاعلات. تتيح الوسائط الوسيطة للوكيل القيام بذلك من خلال:

*وسائط الوظائف*

تتيح هذه الوسائط تنفيذ إجراء بين الوكيل والوظيفة/الأداة التي سيستدعيها. مثال على ذلك هو عندما تريد تسجيل استدعاء الوظيفة.

في الكود أدناه، يحدد `next` إذا ما كان يجب استدعاء الوسيط التالي أو الوظيفة الفعلية.

```python
async def logging_function_middleware(
    context: FunctionInvocationContext,
    next: Callable[[FunctionInvocationContext], Awaitable[None]],
) -> None:
    """Function middleware that logs function execution."""
    # المعالجة المسبقة: تسجيل الدخول قبل تنفيذ الوظيفة
    print(f"[Function] Calling {context.function.name}")

    # الاستمرار إلى الوسيط التالي أو تنفيذ الوظيفة
    await next(context)

    # المعالجة اللاحقة: تسجيل الدخول بعد تنفيذ الوظيفة
    print(f"[Function] {context.function.name} completed")
```

*وسائط المحادثة*

تسمح هذه الوسائط بتنفيذ أو تسجيل فعل بين الوكيل والطلبات بين LLM.

تحتوي على معلومات مهمة مثل `الرسائل` التي تُرسل إلى خدمة الذكاء الاصطناعي.

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

كما تم تغطيته في درس `Agentic Memory`، تعد الذاكرة عنصراً هاماً لتمكين الوكيل من العمل عبر سياقات مختلفة. يقدم MAF عدة أنواع من الذاكرات:

*التخزين في الذاكرة*

هذه هي الذاكرة المخزنة في الخيوط أثناء وقت تشغيل التطبيق.

```python
# إنشاء مؤشر ترابط جديد.
thread = agent.get_new_thread() # تشغيل الوكيل بالمؤشر الترابط.
response = await agent.run("Hello, I am here to help you book travel. Where would you like to go?", thread=thread)
```

*الرسائل الدائمة*

تُستخدم هذه الذاكرة عند تخزين تاريخ المحادثة عبر جلسات مختلفة. يتم تعريفها باستخدام `chat_message_store_factory` :

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

تضاف هذه الذاكرة إلى السياق قبل تشغيل الوكلاء. يمكن تخزين هذه الذكريات في خدمات خارجية مثل mem0:

```python
from agent_framework.mem0 import Mem0Provider

# استخدام Mem0 لإمكانيات الذاكرة المتقدمة
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

المراقبة مهمة لبناء أنظمة وكيلة موثوقة وسهلة الصيانة. يدمج MAF مع OpenTelemetry لتوفير التتبع والعدادات لمراقبة أفضل.

```python
from agent_framework.observability import get_tracer, get_meter

tracer = get_tracer()
meter = get_meter()
with tracer.start_as_current_span("my_custom_span"):
    # افعل شيئًا
    pass
counter = meter.create_counter("my_custom_counter")
counter.add(1, {"key": "value"})
```

### سير العمل

يقدم MAF سير عمل هي خطوات محددة مسبقًا لإكمال مهمة ويشمل وكلاء الذكاء الاصطناعي كعناصر في تلك الخطوات.

تتكون سير العمل من مكونات مختلفة تسمح بتحكم أفضل في التدفق. تسمح سير العمل أيضاً بـ **تنسيق متعدد الوكلاء** و **التدقيق** لحفظ حالات سير العمل.

المكونات الأساسية لسير العمل هي:

**المنفذون**

يستقبل المنفذون الرسائل المدخلة، يؤدون المهام المعينة، ثم ينتجون رسالة إخراج. هذا يحرك سير العمل نحو إكمال المهمة الأكبر. يمكن أن يكون المنفذ وكيل ذكاء اصطناعي أو منطق مخصص.

**الحواف**

تُستخدم الحواف لتعريف تدفق الرسائل في سير العمل. يمكن أن تكون:

*حواف مباشرة* - اتصالات بسيطة من واحد لواحد بين المنفذين:

```python
from agent_framework import WorkflowBuilder

builder = WorkflowBuilder()
builder.add_edge(source_executor, target_executor)
builder.set_start_executor(source_executor)
workflow = builder.build()
```

*حواف مشروطة* - تُفعل بعد تحقق شرط معين. على سبيل المثال، عندما تكون غرف الفنادق غير متوفرة، يمكن للمنفذ اقتراح خيارات أخرى.

*حواف تبديل-حالة* - توجيه الرسائل إلى منفذين مختلفين بناءً على شروط محددة. على سبيل المثال، إذا كان لدى العميل أولوية في السفر، فسيتم التعامل مع مهامه عبر سير عمل آخر.

*حواف التوزيع* - إرسال رسالة واحدة إلى عدة أهداف.

*حواف التجميع* - جمع رسائل متعددة من منفذين مختلفين وإرسالها إلى هدف واحد.

**الأحداث**

لتوفير مراقبة أفضل على سير العمل، يقدم MAF أحداثاً مدمجة للتنفيذ تشمل:

- `WorkflowStartedEvent`  - بدء تنفيذ سير العمل
- `WorkflowOutputEvent` - إنتاج سير العمل لإخراج
- `WorkflowErrorEvent` - حدوث خطأ أثناء سير العمل
- `ExecutorInvokeEvent`  - بدء المنفذ في المعالجة
- `ExecutorCompleteEvent`  -  انتهاء المنفذ من المعالجة
- `RequestInfoEvent` - إصدار طلب

## أنماط MAF المتقدمة

تغطي الأقسام أعلاه المفاهيم الأساسية لإطار عمل Microsoft Agent. عند بناء وكلاء أكثر تعقيداً، إليك بعض الأنماط المتقدمة للنظر فيها:

- **تركيب الوسائط الوسيطة**: ربط عدة معالجات للوسائط الوسيطة (تسجيل الدخول، المصادقة، تحديد المعدل) باستخدام وسائط الوظائف والدردشة للتحكم الدقيق في سلوك الوكيل.
- **تدقيق سير العمل**: استخدام أحداث سير العمل والتسلسل للحفظ والاستئناف في عمليات الوكيل طويلة الأمد.
- **اختيار الأدوات الديناميكي**: دمج RAG عبر أوصاف الأدوات مع تسجيل الأدوات في MAF لعرض الأدوات ذات الصلة فقط لكل استعلام.
- **التسليم متعدد الوكلاء**: استخدام حواف سير العمل والتوجيه الشرطي لتنسيق عمليات التسليم بين الوكلاء المتخصصين.

## استضافة وكلاء LangChain / LangGraph على Microsoft Foundry

إطار عمل Microsoft Agent هو **متوافق مع الأطر الأخرى** — لست محدوداً بالوكلاء المكتوبين باستخدام MAF. إذا كان لديك وكيل مُنشأ بـ **LangChain** أو **LangGraph**، يمكنك تشغيله كـ **وكيل مستضاف على Microsoft Foundry** بحيث تدير Foundry وقت التشغيل، الجلسات، التدرج، الهوية، ونقاط نهاية البروتوكول لك، بينما تبقى منطق وكيلك في LangGraph.

يتم هذا باستخدام حزمة `langchain_azure_ai.agents.hosting`، التي تعرض رسم بياني مجمع من LangGraph على نفس البروتوكولات التي يستخدمها الوكلاء المستضافون في Foundry.

**1. تثبيت الإضافة الخاصة بالاستضافة:**

```bash
pip install -U "langchain-azure-ai[hosting]>=1.2.4" azure-identity
```

تقوم الإضافة `hosting` بتثبيت مكتبات بروتوكول Foundry: `azure-ai-agentserver-responses` (نقطة نهاية `/responses` المتوافقة مع OpenAI) و `azure-ai-agentserver-invocations` (نقطة نهاية `/invocations` العامة).

**2. اختر بروتوكول استضافة:**

| البروتوكول | فئة المضيف | نقطة النهاية | الاستخدام عند |
|----------|-----------|----------|----------|
| **Responses** | `ResponsesHostServer` | `/responses` | تريد دردشة متوافقة مع OpenAI، والبث، وتاريخ الردود، وربط المحادثات — الإعداد الافتراضي الموصى به للوكلاء الحواريين. |
| **Invocations** | `InvocationsHostServer` | `/invocations` | تحتاج إلى شكل JSON مخصص، أو نقطة نهاية على شكل ويب هوك، أو معالجة غير حوارية. |

نظرًا لأن **واجهة برمجة تطبيقات Responses هي الواجهة الأساسية لتطوير الوكلاء في Foundry**، ابدأ بـ `ResponsesHostServer` لمعظم الوكلاء.

**3. تكوين متغيرات البيئة** (`az login` أولاً حتى يتمكن `DefaultAzureCredential` من المصادقة):

```bash
export FOUNDRY_PROJECT_ENDPOINT="https://<resource>.services.ai.azure.com/api/projects/<project>"
export FOUNDRY_MODEL_NAME="gpt-5-mini"
```

عندما يعمل الوكيل لاحقًا كوكيل مستضاف في Foundry، تقوم المنصة بحقن `FOUNDRY_PROJECT_ENDPOINT` تلقائيًا.

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
    deployment = os.environ.get("FOUNDRY_MODEL_NAME", "gpt-5-mini")
    credential = DefaultAzureCredential()
    project = AIProjectClient(endpoint=project_endpoint, credential=credential)
    openai_client = project.get_openai_client()
    token_provider = get_bearer_token_provider(credential, _AZURE_AI_SCOPE)

    # هنا يستهدف ChatOpenAI نقطة النهاية المتوافقة مع OpenAI (الردود) لمشروع Foundry.
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

قم بتشغيله محليًا باستخدام `python main.py`، ثم أرسل طلب Responses إلى `http://localhost:8088/responses`.

**السلوكيات الرئيسية:**

- **المحادثات**: يستمر العملاء في المحادثة عن طريق تمرير `previous_response_id` أو معرف `conversation`. إذا تم تجميع الرسم البياني الخاص بك مع نقطة تحقق LangGraph، يقوم Foundry بمطابقة حالة المحادثة مع نقطة التحقق (استخدم نقطة تحقق متينة في الإنتاج؛ `MemorySaver` مناسب للاختبار المحلي).
- **البشر في الحلقة**: إذا استخدم الرسم الخاص بك `interrupt()` في LangGraph، يعرض `ResponsesHostServer` المقاطعة المعلقة كعنصر `function_call` / `mcp_approval_request` في Responses، ويستأنف العملاء بـ `function_call_output` / `mcp_approval_response` المطابق.
- **النشر على Foundry**: استخدم Azure Developer CLI — `azd ext install azure.ai.agents`، `azd ai agent init -m <manifest>`، `azd ai agent run` (محلي، يتطلب Docker)، ثم `azd provision` و `azd deploy`. يتطلب نشر الوكيل المستضاف دور **مدير مشروع Foundry**.

نسخة قابلة للتشغيل من هذا المثال موجودة في [code-samples/14-langchain-hosted-agent.py](../../../14-microsoft-agent-framework/code-samples/14-langchain-hosted-agent.py). للشرح الكامل (بروتوكول Invocations، مخططات الطلب المخصصة، واستكشاف المشاكل)، راجع [استضافة وكلاء LangGraph كوكلاء مستضافين في Foundry](https://learn.microsoft.com/azure/foundry/how-to/develop/langchain-hosted-agents).

## أمثلة الشفرة 

يمكن العثور على أمثلة الشفرة لإطار عمل Microsoft Agent في هذا المستودع ضمن الملفات `xx-python-agent-framework` و `xx-dotnet-agent-framework`.

## هل لديك المزيد من الأسئلة حول إطار عمل Microsoft Agent؟

انضم إلى [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D) لللقاء مع متعلمين آخرين، وحضور ساعات المكتب، والحصول على إجابات لأسئلتك حول وكلاء الذكاء الاصطناعي.
## الدرس السابق

[الذاكرة لوكلاء الذكاء الاصطناعي](../13-agent-memory/README.md)

## الدرس التالي

[بناء وكلاء استخدام الحاسوب (CUA)](../15-browser-use/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**تنويه**:
تمت ترجمة هذا المستند باستخدام خدمة الترجمة بالذكاء الاصطناعي [Co-op Translator](https://github.com/Azure/co-op-translator). بينما نسعى للدقة، يرجى العلم أن الترجمات الآلية قد تحتوي على أخطاء أو عدم دقة. يجب اعتبار المستند الأصلي بلغته الأصلية المصدر الرسمي والمعتمد. للمعلومات الهامة، يُنصح بالاستعانة بترجمة بشرية محترفة. نحن غير مسؤولين عن أي سوء فهم أو تفسير ناتج عن استخدام هذه الترجمة.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->