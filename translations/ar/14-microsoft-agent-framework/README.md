# استكشاف إطار عمل Microsoft Agent

![Agent Framework](../../../translated_images/ar/lesson-14-thumbnail.90df0065b9d234ee.webp)

### مقدمة

سيغطي هذا الدرس:

- فهم إطار عمل Microsoft Agent: الميزات الرئيسية والقيمة  
- استكشاف المفاهيم الأساسية لإطار عمل Microsoft Agent
- أنماط MAF المتقدمة: سير العمل، الوسيط، والذاكرة

## أهداف التعلم

بعد إكمال هذا الدرس، ستعرف كيف:

- بناء وكلاء ذكاء اصطناعي جاهزين للإنتاج باستخدام إطار عمل Microsoft Agent
- تطبيق الميزات الأساسية لإطار عمل Microsoft Agent على حالات الاستخدام العميلية الخاصة بك
- استخدام الأنماط المتقدمة بما في ذلك سير العمل، الوسيط، والرصد

## عينات الكود 

يمكن العثور على عينات الكود لـ [Microsoft Agent Framework (MAF)](https://learn.microsoft.com/en-us/agent-framework/overview/?wt.mc_id=youtube_26688_organicsocial_reactor&pivots=programming-language-python) في هذا المستودع تحت ملفات `xx-python-agent-framework` و `xx-dotnet-agent-framework`.

## فهم إطار عمل Microsoft Agent

![Framework Intro](../../../translated_images/ar/framework-intro.077af16617cf130c.webp)

[إطار عمل Microsoft Agent (MAF)](https://learn.microsoft.com/en-us/agent-framework/overview/?wt.mc_id=youtube_26688_organicsocial_reactor&pivots=programming-language-python) هو الإطار الموحد من مايكروسوفت لبناء وكلاء الذكاء الاصطناعي. يقدم مرونة لمعالجة مجموعة واسعة من حالات الاستخدام العميلية التي تُرى في بيئات الإنتاج والبحث بما في ذلك:

- **تنسيق الوكيل المتسلسل** في السيناريوهات التي تتطلب سير عمل خطوة بخطوة.
- **التنسيق المتزامن** في السيناريوهات التي يحتاج فيها الوكلاء لإكمال المهام في نفس الوقت.
- **تنسيق محادثة المجموعة** في السيناريوهات التي يمكن فيها للوكلاء التعاون سوياً على مهمة واحدة.
- **تنسيق التسليم** في السيناريوهات التي يقوم فيها الوكلاء بتسليم المهمة لبعضهم البعض مع إتمام المهام الفرعية.
- **التنسيق المغناطيسي** في السيناريوهات التي ينشئ فيها وكيل المدير ويعدل قائمة المهام ويتولى تنسيق الوكلاء الفرعيين لإكمال المهمة.

لتقديم وكلاء الذكاء الاصطناعي في الإنتاج، يشتمل MAF أيضاً على ميزات من أجل:

- **الرصد** من خلال استخدام OpenTelemetry حيث يتم توثيق كل إجراء للوكيل الذكي بما في ذلك استدعاء الأدوات، خطوات التنسيق، تدفقات التفكير، ورصد الأداء عبر لوحات معلومات Microsoft Foundry.
- **الأمان** من خلال استضافة الوكلاء بشكل أصلي على Microsoft Foundry الذي يتضمن ضوابط أمان مثل الوصول المعتمد على الدور، التعامل مع البيانات الخاصة، والسلامة المحتوى المدمجة.
- **التحمل** حيث يمكن لأنسجة ومهام الوكيل التوقف، الاستئناف، والتعافي من الأخطاء مما يتيح عمليات أطول.
- **التحكم** حيث تدعم سير العمل بمشاركة الإنسان حيث يتم تعليم المهام بأنها تتطلب موافقة بشرية.

كما يركز إطار عمل Microsoft Agent على قابلية التشغيل البيني عبر:

- **عدم الاعتماد على السحابة** - يمكن تشغيل الوكلاء في الحاويات، محليًا وعبر عدة سحب.
- **عدم الاعتماد على المزود** - يمكن إنشاء الوكلاء من خلال SDK المفضل لديك بما في ذلك Azure OpenAI و OpenAI
- **دمج المعايير المفتوحة** - يمكن للوكلاء استخدام بروتوكولات مثل Agent-to-Agent(A2A) و Model Context Protocol (MCP) لاكتشاف واستخدام وكلاء وأدوات أخرى.
- **الإضافات والموصلات** - يمكن إجراء اتصالات إلى خدمات البيانات والذاكرة مثل Microsoft Fabric و SharePoint و Pinecone و Qdrant.

لنلقِ نظرة على كيفية تطبيق هذه الميزات على بعض المفاهيم الأساسية لإطار عمل Microsoft Agent.

## المفاهيم الأساسية لإطار عمل Microsoft Agent

### الوكلاء

![Agent Framework](../../../translated_images/ar/agent-components.410a06daf87b4fef.webp)

**إنشاء الوكلاء**

يتم إنشاء الوكيل من خلال تحديد خدمة الاستدلال (موفر LLM)،
مجموعة من التعليمات التي يتبعها الوكيل الذكي، و`name` معين:

```python
agent = AzureOpenAIChatClient(credential=AzureCliCredential()).create_agent( instructions="You are good at recommending trips to customers based on their preferences.", name="TripRecommender" )
```

المثال أعلاه يستخدم `Azure OpenAI` لكن يمكن إنشاء الوكلاء باستخدام مجموعة متنوعة من الخدمات بما في ذلك `خدمة الوكيل Microsoft Foundry`:

```python
AzureAIAgentClient(async_credential=credential).create_agent( name="HelperAgent", instructions="You are a helpful assistant." ) as agent
```

OpenAI `Responses`، APIs `ChatCompletion`

```python
agent = OpenAIResponsesClient().create_agent( name="WeatherBot", instructions="You are a helpful weather assistant.", )
```

```python
agent = OpenAIChatClient().create_agent( name="HelpfulAssistant", instructions="You are a helpful assistant.", )
```

أو [MiniMax](https://platform.minimaxi.com/) الذي يوفر API متوافق مع OpenAI مع نوافذ سياقية كبيرة (حتى 204K توكن):

```python
agent = OpenAIChatClient(base_url="https://api.minimax.io/v1", api_key=os.environ["MINIMAX_API_KEY"], model_id="MiniMax-M3").create_agent( name="HelpfulAssistant", instructions="You are a helpful assistant.", )
```

أو وكلاء بعيدين باستخدام بروتوكول A2A:

```python
agent = A2AAgent( name=agent_card.name, description=agent_card.description, agent_card=agent_card, url="https://your-a2a-agent-host" )
```

**تشغيل الوكلاء**

يتم تشغيل الوكلاء باستخدام طرق `.run` أو `.run_stream` للاستجابات بدون أو مع تدفق.

```python
result = await agent.run("What are good places to visit in Amsterdam?")
print(result.text)
```

```python
async for update in agent.run_stream("What are the good places to visit in Amsterdam?"):
    if update.text:
        print(update.text, end="", flush=True)

```

يمكن لكل تشغيل وكيل أن يحتوي أيضاً على خيارات لتخصيص المعلمات مثل `max_tokens` المستخدمة من قبل الوكيل، `tools` التي يمكن للوكيل استدعاؤها، وحتى `model` نفسه المستخدم للوكيل.

هذا مفيد في الحالات التي تتطلب نماذج أو أدوات محددة لإكمال مهمة المستخدم.

**الأدوات**

يمكن تعريف الأدوات سواء عند تعريف الوكيل:

```python
def get_attractions( location: Annotated[str, Field(description="The location to get the top tourist attractions for")], ) -> str: """Get the top tourist attractions for a given location.""" return f"The top attractions for {location} are." 


# عند إنشاء ChatAgent مباشرةً

agent = ChatAgent( chat_client=OpenAIChatClient(), instructions="You are a helpful assistant", tools=[get_attractions]

```

وأيضاً عند تشغيل الوكيل:

```python

result1 = await agent.run( "What's the best place to visit in Seattle?", tools=[get_attractions] # أداة مقدمة لهذا التشغيل فقط )
```

**خيوط الوكيل**

تُستخدم خيوط الوكيل لمعالجة المحادثات متعددة الأدوار. يمكن إنشاء الخيوط إما بواسطة:

- استخدام `get_new_thread()` الذي يتيح حفظ الخيط مع مرور الوقت
- إنشاء خيط تلقائياً عند تشغيل وكيل ويظل الخيط فقط خلال التشغيل الحالي.

لإنشاء خيط، يكون الكود كالتالي:

```python
# إنشاء خيط جديد.
thread = agent.get_new_thread() # تشغيل الوكيل باستخدام الخيط.
response = await agent.run("Hello, I am here to help you book travel. Where would you like to go?", thread=thread)

```

يمكنك بعد ذلك تسلسل الخيط ليتم تخزينه للاستخدام لاحقاً:

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

**وسيط الوكيل**

يتفاعل الوكلاء مع الأدوات و LLMs لإكمال مهام المستخدمين. في سيناريوهات معينة، نريد تنفيذ أو تتبع أنشطة بين هذه التفاعلات. يتيح لنا وسيط الوكيل القيام بذلك من خلال:

*وسيط الدالة*

يسمح هذا الوسيط بتنفيذ إجراء بين الوكيل ودالة/أداة سيستدعيها. مثال عند استخدامه هو عندما تريد تسجيل استدعاء الدالة.

في الكود أدناه يحدد `next` ما إذا كان يجب استدعاء الوسيط التالي أو الدالة الفعلية.

```python
async def logging_function_middleware(
    context: FunctionInvocationContext,
    next: Callable[[FunctionInvocationContext], Awaitable[None]],
) -> None:
    """Function middleware that logs function execution."""
    # المعالجة المسبقة: تسجيل الدخول قبل تنفيذ الدالة
    print(f"[Function] Calling {context.function.name}")

    # الاستمرار إلى الوسيط التالي أو تنفيذ الدالة
    await next(context)

    # المعالجة اللاحقة: تسجيل الدخول بعد تنفيذ الدالة
    print(f"[Function] {context.function.name} completed")
```

*وسيط الدردشة*

يسمح هذا الوسيط بتنفيذ أو تسجيل إجراء بين الوكيل والطلبات بين LLM .

يحتوي هذا على معلومات مهمة مثل `messages` التي تُرسل إلى خدمة الذكاء الاصطناعي.

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

كما تم تغطيته في درس `ذاكرة الوكيل`، الذاكرة عنصر مهم لتمكين الوكيل من العمل عبر سياقات مختلفة. يوفر MAF عدة أنواع مختلفة من الذاكرات:

*التخزين في الذاكرة*

هذه هي الذاكرة المخزنة في الخيوط أثناء وقت تشغيل التطبيق.

```python
# إنشاء خيط جديد.
thread = agent.get_new_thread() # تشغيل الوكيل مع الخيط.
response = await agent.run("Hello, I am here to help you book travel. Where would you like to go?", thread=thread)
```

*الرسائل المستمرة*

تُستخدم هذه الذاكرة عند تخزين سجلات المحادثات عبر جلسات مختلفة. يتم تعريفها باستخدام `chat_message_store_factory`:

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


يتم إضافة هذه الذاكرة إلى السياق قبل تشغيل الوكلاء. يمكن تخزين هذه الذكريات في خدمات خارجية مثل mem0:

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

**رصد الوكلاء**

الرصد مهم لبناء نظم وكيلة موثوقة وقابلة للصيانة. يدمج MAF مع OpenTelemetry لتوفير التتبع والعدادات من أجل رصد أفضل.

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

### سير العمل

يقدم MAF سير عمل وهي خطوات محددة مسبقًا لإكمال مهمة وتشمل وكلاء الذكاء الاصطناعي كمكونات في تلك الخطوات.

تتكون سير العمل من مكونات مختلفة تسمح بتحكم أفضل في التدفق. كما تمكّن سير العمل من **تنسيق متعدد الوكلاء** و**نقاط التحقق** لحفظ حالات سير العمل.

المكونات الأساسية لسير العمل هي:

**المُنفِّذون**

يتلقى المنفذون رسائل الإدخال، يؤدون مهامهم المعينة، ثم ينتجون رسالة إخراج. هذا يدفع سير العمل نحو إكمال المهمة الأكبر. يمكن أن يكون المنفذون وكلاء ذكاء اصطناعي أو منطق مخصص.

**الحواف**

تُستخدم الحواف لتعريف تدفق الرسائل في سير العمل. يمكن أن تكون:

*الحواف المباشرة* - اتصالات بسيطة من واحد إلى واحد بين المنفذين:

```python
from agent_framework import WorkflowBuilder

builder = WorkflowBuilder()
builder.add_edge(source_executor, target_executor)
builder.set_start_executor(source_executor)
workflow = builder.build()
```

*الحواف الشرطية* - يتم تفعيلها بعد تحقيق شرط معين. على سبيل المثال، عندما لا تتوفر غرف في الفنادق، يمكن لمنفذ أن يقترح خيارات أخرى.

*حواف التبديل الحالة* - توجيه الرسائل إلى منفذين مختلفين بناءً على شروط محددة. مثلاً، إذا كان لعميل السفر وصول ذو أولوية، فسيتم التعامل مع مهامه عبر سير عمل آخر.

*حواف التفرع الخارجي* - إرسال رسالة واحدة إلى عدة أهداف.

*حواف التفرع الداخلي* - جمع رسائل متعددة من منفذين مختلفين وإرسالها إلى هدف واحد.

**الأحداث**

لتوفير رصد أفضل لسير العمل، يقدم MAF أحداثًا مدمجة للتنفيذ تشمل:

- `WorkflowStartedEvent`  - يبدأ تنفيذ سير العمل
- `WorkflowOutputEvent` - ينتج سير العمل مخرجات
- `WorkflowErrorEvent` - يواجه سير العمل خطأ
- `ExecutorInvokeEvent`  - يبدأ المنفذ المعالجة
- `ExecutorCompleteEvent`  - ينهي المنفذ المعالجة
- `RequestInfoEvent` - يتم إصدار طلب

## أنماط متقدمة في MAF

تغطي الأقسام أعلاه المفاهيم الرئيسية لإطار عمل الوكيل من مايكروسوفت. مع بناء وكلاء أكثر تعقيدًا، إليك بعض الأنماط المتقدمة التي يجب أخذها بعين الاعتبار:

- **تركيب الوسيط**: ربط عدة معالجات وسيطة (تسجيل، مصادقة، تحديد معدل) باستخدام وظائف ووسيط المحادثة للتحكم الدقيق في سلوك الوكيل.
- **نقاط تحقق سير العمل**: استخدام أحداث سير العمل والتسلسل للحفظ واستئناف عمليات الوكيل طويلة الأمد.
- **اختيار الأدوات الديناميكي**: دمج RAG على أوصاف الأدوات مع تسجيل الأدوات في MAF لعرض الأدوات الملائمة فقط لكل استعلام.
- **تحويل متعدد الوكلاء**: استخدام حواف سير العمل والتوجيه الشرطي لتنسيق التحويلات بين وكلاء متخصصين.

## استضافة وكلاء LangChain / LangGraph على Microsoft Foundry

إطار عمل الوكيل من مايكروسوفت هو **قابل للتشغيل المتداخل مع أُطُر أخرى** — لست مقيدًا بالوكلاء المكتوبين بـ MAF فقط. إذا كان لديك وكيل مبني بـ **LangChain** أو **LangGraph**، يمكنك تشغيله كـ **وكيل مستضاف في Microsoft Foundry** بحيث تدير Foundry وقت التشغيل، الجلسات، التوسع، الهوية، ونقاط نهاية البروتوكول، في حين يبقى منطق الوكيل في LangGraph.

يتم ذلك باستخدام حزمة `langchain_azure_ai.agents.hosting`، التي تعرض رسم LangGraph مُجمّع عبر نفس بروتوكولات وكلاء Foundry المستضافين.

**1. قم بتثبيت الإضافة الخاصة بالاستضافة:**

```bash
pip install -U "langchain-azure-ai[hosting]>=1.2.4" azure-identity
```

تثبت الإضافة `hosting` مكتبات بروتوكول Foundry: `azure-ai-agentserver-responses` (نقطة نهاية `/responses` المتوافقة مع OpenAI) و `azure-ai-agentserver-invocations` (نقطة نهاية `/invocations` العامة).

**2. اختر بروتوكول الاستضافة:**

| البروتوكول | فئة المضيف | نقطة النهاية | الاستخدام عند |
|----------|-----------|----------|----------|
| **الاستجابات** | `ResponsesHostServer` | `/responses` | تريد دردشة متوافقة مع OpenAI، تدفق، سجل الاستجابات، وترتيب المحادثات — الخيار الموصى به للوكلاء الحواريين. |
| **الاستدعاءات** | `InvocationsHostServer` | `/invocations` | تحتاج إلى شكل JSON مخصص، نقطة نهاية شبيهة بالويب هوك، أو معالجة غير حوارية. |

نظرًا لأن **واجهة برمجة التطبيقات Responses هي الواجهة الرئيسية لتطوير الوكلاء في Foundry**، ابدأ بـ `ResponsesHostServer` لمعظم الوكلاء.

**3. إعداد متغيرات البيئة** (`az login` أولًا حتى يتمكن `DefaultAzureCredential` من المصادقة):

```bash
export FOUNDRY_PROJECT_ENDPOINT="https://<resource>.services.ai.azure.com/api/projects/<project>"
export FOUNDRY_MODEL_NAME="gpt-5-mini"
```

عندما يعمل الوكيل لاحقًا كوكيل مستضاف في Foundry، يحقن النظام تلقائيًا `FOUNDRY_PROJECT_ENDPOINT`.

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

شغّله محليًا بـ `python main.py`، ثم أرسل طلب Responses إلى `http://localhost:8088/responses`.

**السلوكيات الرئيسية:**

- **المحادثات**: يواصل العملاء المحادثة بتمرير `previous_response_id` أو معرف `conversation`. إذا تم تجميع رسمك باستخدام نقطة فحص LangGraph، يقوم Foundry بربط حالة المحادثة بنقطة التحقق (استخدم نقطة فحص دائمة في الإنتاج؛ `MemorySaver` جيد للاختبار المحلي).
- **البشر في الحلقة**: إذا كان رسمك يستخدم `interrupt()` من LangGraph، يعرض `ResponsesHostServer` الانقطاع المعلق كبند `function_call` / `mcp_approval_request` في Responses، ويستأنف العملاء مع `function_call_output` / `mcp_approval_response` المطابق.
- **النشر في Foundry**: استخدم Azure Developer CLI — `azd ext install azure.ai.agents`، `azd ai agent init -m <manifest>`، `azd ai agent run` (محليًا، يتطلب Docker)، ثم `azd provision` و `azd deploy`. يتطلب نشر الوكيل المستضاف دور **مدير مشروع Foundry**.

نسخة تشغيلية من هذا المثال متوفرة في [code-samples/14-langchain-hosted-agent.py](../../../14-microsoft-agent-framework/code-samples/14-langchain-hosted-agent.py). للشرح الكامل (بروتوكول Invocations، مخططات الطلب المخصصة، واستكشاف الأخطاء)، راجع [استضافة وكلاء LangGraph كوكلاء مستضافين في Foundry](https://learn.microsoft.com/azure/foundry/how-to/develop/langchain-hosted-agents).

## عينات الشيفرة 

توجد عينات الشيفرة لإطار عمل الوكيل من مايكروسوفت في هذا المستودع تحت ملفات `xx-python-agent-framework` و `xx-dotnet-agent-framework`.

## هل لديك المزيد من الأسئلة حول إطار عمل الوكيل من مايكروسوفت؟

انضم إلى [مايكروسوفت Foundry على ديسكورد](https://discord.com/invite/ATgtXmAS5D) لمقابلة المتعلمين الآخرين، حضور ساعات المكتب، والحصول على إجابات لأسئلتك حول وكلاء الذكاء الاصطناعي.
## الدرس السابق

[ذاكرة لوكلاء الذكاء الاصطناعي](../13-agent-memory/README.md)

## الدرس التالي


[بناء وكلاء استخدام الحاسوب (CUA)](../15-browser-use/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**تنويه**:
تمت ترجمة هذا المستند باستخدام خدمة الترجمة بالذكاء الاصطناعي [Co-op Translator](https://github.com/Azure/co-op-translator). بينما نسعى للدقة، يرجى العلم أن الترجمات الآلية قد تحتوي على أخطاء أو عدم دقة. يجب اعتبار المستند الأصلي بلغته الأصلية المصدر الرسمي والمعتمد. للمعلومات الهامة، يُنصح بالاستعانة بترجمة بشرية محترفة. نحن غير مسؤولين عن أي سوء فهم أو تفسير ناتج عن استخدام هذه الترجمة.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->