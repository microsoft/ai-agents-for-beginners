[![كيفية تصميم وكلاء ذكاء اصطناعي جيدين](../../../translated_images/ar/lesson-4-thumbnail.546162853cb3daff.webp)](https://youtu.be/vieRiPRx-gI?si=cEZ8ApnT6Sus9rhn)

> _(انقر على الصورة أعلاه لمشاهدة فيديو هذا الدرس)_

# نمط تصميم استخدام الأدوات

الأدوات مثيرة للاهتمام لأنها تسمح لوكلاء الذكاء الاصطناعي بأن يكون لديهم نطاق أوسع من القدرات. بدلاً من أن يكون لدى الوكيل مجموعة محدودة من الإجراءات التي يمكنه القيام بها، من خلال إضافة أداة، يمكن للوكيل الآن تنفيذ مجموعة واسعة من الإجراءات. في هذا الفصل، سنلقي نظرة على نمط تصميم استخدام الأدوات، الذي يصف كيف يمكن لوكلاء الذكاء الاصطناعي استخدام أدوات محددة لتحقيق أهدافهم.

## المقدمة

في هذا الدرس، نسعى للإجابة على الأسئلة التالية:

- ما هو نمط تصميم استخدام الأدوات؟
- ما هي الحالات التي يمكن تطبيقه عليها؟
- ما هي العناصر/الكتل الأساسية اللازمة لتنفيذ نمط التصميم؟
- ما هي الاعتبارات الخاصة باستخدام نمط تصميم استخدام الأدوات لبناء وكلاء ذكاء اصطناعي جديرين بالثقة؟

## أهداف التعلم

بعد إتمام هذا الدرس، ستتمكن من:

- تعريف نمط تصميم استخدام الأدوات وغرضه.
- تحديد الحالات التي يمكن تطبيق نمط تصميم استخدام الأدوات عليها.
- فهم العناصر الرئيسية اللازمة لتنفيذ نمط التصميم.
- التعرف على الاعتبارات لضمان الثقة في وكلاء الذكاء الاصطناعي الذين يستخدمون هذا النمط.

## ما هو نمط تصميم استخدام الأدوات؟

يركز **نمط تصميم استخدام الأدوات** على منح نماذج اللغة الكبيرة (LLMs) القدرة على التفاعل مع أدوات خارجية لتحقيق أهداف محددة. الأدوات هي شفرة يمكن تنفيذها بواسطة وكيل لأداء إجراءات. يمكن أن تكون الأداة وظيفة بسيطة مثل الآلة الحاسبة، أو نداء API إلى خدمة طرف ثالث مثل البحث عن أسعار الأسهم أو توقعات الطقس. في سياق وكلاء الذكاء الاصطناعي، تم تصميم الأدوات ليتم تنفيذها من قبل الوكلاء استجابة لـ **مكالمات الوظائف التي يولدها النموذج**.

## ما هي الحالات التي يمكن تطبيقه عليها؟

يمكن لوكلاء الذكاء الاصطناعي الاستفادة من الأدوات لإكمال مهام معقدة، واسترجاع المعلومات، أو اتخاذ قرارات. يستخدم نمط تصميم استخدام الأدوات غالبًا في السيناريوهات التي تتطلب تفاعلاً ديناميكيًا مع أنظمة خارجية، مثل قواعد البيانات، وخدمات الويب، أو مفسري الشفرة. هذه القدرة مفيدة لعدد من الحالات المختلفة بما في ذلك:

- **استرجاع المعلومات الديناميكي:** يمكن للوكلاء الاستعلام من APIs خارجية أو قواعد بيانات للحصول على بيانات محدثة (مثلاً، الاستعلام من قاعدة بيانات SQLite لتحليل البيانات، جلب أسعار الأسهم أو معلومات الطقس).
- **تنفيذ وتفسير الشفرة:** يمكن للوكلاء تنفيذ الشفرات أو السكربتات لحل المشكلات الرياضية، إنشاء تقارير، أو إجراء محاكاة.
- **أتمتة سير العمل:** أتمتة مهام متكررة أو متعددة الخطوات من خلال دمج أدوات مثل جداول المهام، خدمات البريد الإلكتروني، أو خطوط بيانات.
- **دعم العملاء:** يمكن للوكلاء التفاعل مع أنظمة إدارة علاقات العملاء، منصات التذاكر، أو قواعد المعرفة لحل استفسارات المستخدمين.
- **إنشاء وتحرير المحتوى:** يمكن للوكلاء الاستعانة بأدوات مثل مدقق قواعد النحو، ملخصات النصوص، أو مقيمات سلامة المحتوى للمساعدة في مهام إنشاء المحتوى.

## ما هي العناصر/الكتل الأساسية اللازمة لتنفيذ نمط تصميم استخدام الأدوات؟

تتيح هذه الكتل الأساسية لوكيل الذكاء الاصطناعي أداء مجموعة واسعة من المهام. دعونا نلقي نظرة على العناصر الرئيسية اللازمة لتنفيذ نمط تصميم استخدام الأدوات:

- **مخططات الوظائف/الأدوات**: تعريفات مفصلة للأدوات المتاحة، بما في ذلك اسم الوظيفة، الغرض، المعلمات المطلوبة، والمخرجات المتوقعة. تمكّن هذه المخططات نموذج اللغة من فهم الأدوات المتاحة وكيفية تكوين طلبات صحيحة.

- **منطق تنفيذ الوظائف**: يتحكم في كيفية ووقت استدعاء الأدوات بناءً على نية المستخدم وسياق المحادثة. قد يشمل ذلك وحدات التخطيط، آليات التوجيه، أو تدفقات شرطية تحدد استخدام الأدوات بشكل ديناميكي.

- **نظام معالجة الرسائل**: المكونات التي تدير تدفق المحادثة بين مدخلات المستخدم، استجابات نموذج اللغة، مكالمات الأدوات، ومخرجات الأدوات.

- **إطار تكامل الأدوات**: البنية التحتية التي تربط الوكيل بالأدوات المختلفة، سواء كانت وظائف بسيطة أو خدمات خارجية معقدة.

- **معالجة الأخطاء والتحقق**: آليات للتعامل مع فشل تنفيذ الأدوات، التحقق من المعلمات، وإدارة الردود غير المتوقعة.

- **إدارة الحالة**: تتبع سياق المحادثة، التفاعلات السابقة مع الأدوات، والبيانات المستمرة لضمان الاتساق عبر التفاعلات متعددة الأدوار.

بعد ذلك، دعونا نلقي نظرة على استدعاء الوظائف/الأدوات بتفصيل أكثر.
 
### استدعاء الوظائف/الأدوات

استدعاء الوظائف هو الطريقة الأساسية التي نُمكن بها نماذج اللغة الكبيرة (LLMs) من التفاعل مع الأدوات. سترى غالبًا استخدام 'وظيفة' و'أداة' بالتبادل لأن 'الوظائف' (كتل من الشفرة القابلة لإعادة الاستخدام) هي 'الأدوات' التي يستخدمها الوكلاء لأداء المهام. لكي يتم استدعاء شفرة وظيفة، يجب على نموذج اللغة مقارنة طلب المستخدم بوصف الوظائف. للقيام بذلك، يتم إرسال مخطط يحتوي على أوصاف جميع الوظائف المتاحة إلى نموذج اللغة. يختار نموذج اللغة بعد ذلك الوظيفة الأنسب للمهمة ويُرجع اسمها والوسائط الخاصة بها. يتم استدعاء الوظيفة المحددة، ثم تُرسل استجابتها إلى نموذج اللغة، الذي يستخدم المعلومات للرد على طلب المستخدم.

لتنفيذ استدعاء الوظائف للوكلاء، ستحتاج إلى:

1. نموذج لغة كبير يدعم استدعاء الوظائف
2. مخطط يحتوي على أوصاف الوظائف
3. الشفرة الخاصة بكل وظيفة موصوفة

لنستخدم مثال الحصول على الوقت الحالي في مدينة لتوضيح ذلك:

1. **تفعيل نموذج لغة كبير يدعم استدعاء الوظائف:**

    ليست كل النماذج تدعم استدعاء الوظائف، لذلك من المهم التأكد من أن نموذج اللغة الذي تستخدمه يدعم ذلك. <a href="https://learn.microsoft.com/azure/ai-services/openai/how-to/function-calling" target="_blank">Azure OpenAI</a> يدعم استدعاء الوظائف. يمكننا البدء بتفعيل عميل OpenAI ضد واجهة برمجة التطبيقات Azure OpenAI **Responses API** (النقطة النهائية المستقرة `/openai/v1/` — لا حاجة إلى `api_version`). 

    ```python
    # تهيئة عميل OpenAI لـ Azure OpenAI (واجهة برمجة تطبيقات الاستجابات، نقطة النهاية v1)
    client = OpenAI(
        base_url=f"{os.environ['AZURE_OPENAI_ENDPOINT'].rstrip('/')}/openai/v1/",
        api_key=os.environ["AZURE_OPENAI_API_KEY"],
    )
    deployment_name = os.environ["AZURE_OPENAI_DEPLOYMENT"]
    ```

1. **إنشاء مخطط وظيفة**:

    بعد ذلك سنقوم بتعريف مخطط JSON يحتوي على اسم الوظيفة، وصف لما تقوم به الوظيفة، وأسماء ووصف معلمات الوظيفة.
    ثم نأخذ هذا المخطط ونمرره إلى العميل الذي تم إنشاؤه سابقًا، جنبًا إلى جنب مع طلب المستخدم للعثور على الوقت في سان فرانسيسكو. الأمر المهم الذي يجب ملاحظته هو أن **نداء الأداة** هو ما يتم إرجاعه، **وليس** الإجابة النهائية على السؤال. كما ذكرنا سابقًا، يعيد نموذج اللغة اسم الوظيفة التي اختارها للمهمة، والوسائط التي سيتم تمريرها إليها.

    ```python
    # وصف الدالة للنموذج للقراءة (تنسيق أداة API للردود المسطحة)
    tools = [
        {
            "type": "function",
            "name": "get_current_time",
            "description": "Get the current time in a given location",
            "parameters": {
                "type": "object",
                "properties": {
                    "location": {
                        "type": "string",
                        "description": "The city name, e.g. San Francisco",
                    },
                },
                "required": ["location"],
            },
        }
    ]
    ```
   
    ```python
  
    # رسالة المستخدم الأولية
    messages = [{"role": "user", "content": "What's the current time in San Francisco"}]

    # أول استدعاء API: اطلب من النموذج استخدام الدالة
    response = client.responses.create(
        model=deployment_name,
        input=messages,
        tools=tools,
        tool_choice="auto",
        store=False,
    )

    # تقوم واجهة برمجة التطبيقات للردود بإرجاع استدعاءات الأدوات كعناصر function_call في response.output.
    # أضفها إلى المحادثة بحيث يكون لدى النموذج السياق الكامل في الدور التالي.
    messages += response.output

    print("Model's response:")
    print(response.output)
  
    ```

    ```bash
    Model's response:
    [ResponseFunctionToolCall(arguments='{"location":"San Francisco"}', call_id='call_pOsKdUlqvdyttYB67MOj434b', name='get_current_time', type='function_call')]
    ```
  
1. **الشفرة المطلوبة لتنفيذ المهمة:**

    الآن بعد أن اختار نموذج اللغة الوظيفة التي تحتاج إلى التنفيذ، يجب تنفيذ الشفرة التي تنفذ المهمة وتشغيلها.
    يمكننا تنفيذ الشفرة للحصول على الوقت الحالي بلغة Python. سنحتاج أيضًا إلى كتابة الشفرة لاستخراج الاسم والوسائط من response_message للحصول على النتيجة النهائية.

    ```python
      def get_current_time(location):
        """Get the current time for a given location"""
        print(f"get_current_time called with location: {location}")  
        location_lower = location.lower()
        
        for key, timezone in TIMEZONE_DATA.items():
            if key in location_lower:
                print(f"Timezone found for {key}")  
                current_time = datetime.now(ZoneInfo(timezone)).strftime("%I:%M %p")
                return json.dumps({
                    "location": location,
                    "current_time": current_time
                })
      
        print(f"No timezone data found for {location_lower}")  
        return json.dumps({"location": location, "current_time": "unknown"})
    ```

     ```python
    # معالجة استدعاءات الدوال
    tool_calls = [item for item in response.output if item.type == "function_call"]
    if tool_calls:
        for tool_call in tool_calls:
            if tool_call.name == "get_current_time":

                function_args = json.loads(tool_call.arguments)

                time_response = get_current_time(
                    location=function_args.get("location")
                )

                # إرجاع نتيجة الأداة كعنصر function_call_output
                messages.append({
                    "type": "function_call_output",
                    "call_id": tool_call.call_id,
                    "output": time_response,
                })
    else:
        print("No tool calls were made by the model.")

    # الاستدعاء الثاني لواجهة البرمجة: الحصول على الاستجابة النهائية من النموذج
    final_response = client.responses.create(
        model=deployment_name,
        input=messages,
        tools=tools,
        store=False,
    )

    return final_response.output_text
     ```

     ```bash
      get_current_time called with location: San Francisco
      Timezone found for san francisco
      The current time in San Francisco is 09:24 AM.
     ```

استدعاء الوظائف هو جوهر معظم، إن لم يكن كل، تصميم استخدام الأدوات للوكلاء، ومع ذلك قد يكون تنفيذه من الصفر تحديًا في بعض الأحيان.
كما تعلمنا في [الدرس 2](../../../02-explore-agentic-frameworks) توفر الأُطُر العاملية لدينا كتل بناء جاهزة لتنفيذ استخدام الأدوات.
 
## أمثلة على استخدام الأدوات مع الأُطُر العاملية

إليك بعض الأمثلة على كيفية تنفيذ نمط تصميم استخدام الأدوات باستخدام أُطُر عاملية مختلفة:

### إطار عمل Microsoft Agent

<a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">إطار عمل Microsoft Agent</a> هو إطار عمل ذكاء اصطناعي مفتوح المصدر لبناء وكلاء ذكاء اصطناعي. يبسط عملية استخدام استدعاء الوظائف من خلال السماح لك بتعريف الأدوات كدوال Python مع المزخرف `@tool`. يدير الإطار الاتصال ذهابًا وإيابًا بين النموذج والشفرة الخاصة بك. كما يوفر الوصول إلى أدوات مبنية مسبقًا مثل بحث الملفات ومفسر الشفرة عبر `FoundryChatClient`.

يوضح المخطط التالي عملية استدعاء الوظائف مع إطار عمل Microsoft Agent:

![استدعاء الوظيفة](../../../translated_images/ar/functioncalling-diagram.a84006fc287f6014.webp)

في إطار عمل Microsoft Agent، تُعرف الأدوات كدوال مزخرفة. يمكننا تحويل الدالة `get_current_time` التي رأيناها سابقًا إلى أداة باستخدام المزخرف `@tool`. يقوم الإطار تلقائيًا بتسلسل الوظائف ومعلماتها، وإنشاء المخطط لإرساله إلى نموذج اللغة.

```python
import os
from agent_framework import tool
from agent_framework.foundry import FoundryChatClient
from azure.identity import AzureCliCredential

@tool(approval_mode="never_require")
def get_current_time(location: str) -> str:
    """Get the current time for a given location"""
    ...

# إنشاء العميل
provider = FoundryChatClient(
    project_endpoint=os.environ["AZURE_AI_PROJECT_ENDPOINT"],
    model=os.environ["AZURE_AI_MODEL_DEPLOYMENT_NAME"],
    credential=AzureCliCredential(),
)

# إنشاء وكيل وتشغيله مع الأداة
agent = provider.as_agent(name="TimeAgent", instructions="Use available tools to answer questions.", tools=get_current_time)
response = await agent.run("What time is it?")
```
  
### خدمة Microsoft Foundry Agent

<a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">خدمة Microsoft Foundry Agent</a> هي إطار عامل أحدث مصمم لتمكين المطورين من بناء وتشغيل وتوسيع نطاق وكلاء ذكاء اصطناعي عالي الجودة، وقابل للتوسع بأمان دون الحاجة إلى إدارة موارد الحوسبة والتخزين الأساسية. وهي مفيدة بشكل خاص لتطبيقات المؤسسات لأنها خدمة مُدارة بالكامل مع أمان من الدرجة المؤسساتية.

عند المقارنة بالتطوير باستخدام واجهة برمجة تطبيقات LLM مباشرة، توفر خدمة Microsoft Foundry Agent بعض المزايا، بما في ذلك:

- استدعاء الأدوات تلقائيًا – لا حاجة لتحليل نداء الأداة، استدعاء الأداة، ومعالجة الرد؛ يتم كل ذلك الآن على جانب الخادم
- إدارة البيانات بأمان – بدلاً من إدارة حالة المحادثة الخاصة بك، يمكنك الاعتماد على الخيوط لتخزين كل المعلومات التي تحتاجها
- أدوات جاهزة للاستخدام – أدوات يمكنك استخدامها للتفاعل مع مصادر بياناتك، مثل Bing، Azure AI Search، و Azure Functions.

الأدوات المتاحة في خدمة Microsoft Foundry Agent يمكن تقسيمها إلى فئتين:

1. أدوات المعرفة:
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/bing-grounding?tabs=python&pivots=overview" target="_blank">التأسيس باستخدام بحث Bing</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/file-search?tabs=python&pivots=overview" target="_blank">بحث الملفات</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-ai-search?tabs=azurecli%2Cpython&pivots=overview-azure-ai-search" target="_blank">بحث Azure AI</a>

2. أدوات العمل:
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/function-calling?tabs=python&pivots=overview" target="_blank">استدعاء الوظائف</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/code-interpreter?tabs=python&pivots=overview" target="_blank">مفسر الشفرة</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/openapi-spec?tabs=python&pivots=overview" target="_blank">الأدوات المعرفة باستخدام OpenAPI</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-functions?pivots=overview" target="_blank">وظائف Azure</a>

تتيح لنا خدمة الوكلاء القدرة على استخدام هذه الأدوات معًا كمجموعة أدوات. كما تستخدم `الخيوط` التي تتتبع تاريخ الرسائل من محادثة معينة.

تخيل أنك وكيل مبيعات في شركة تُدعى Contoso. تريد تطوير وكيل محادثة يمكنه الإجابة على أسئلة حول بيانات مبيعاتك.

توضح الصورة التالية كيفية استخدام خدمة Microsoft Foundry Agent لتحليل بيانات مبيعاتك:

![خدمة الوكيل أثناء العمل](../../../translated_images/ar/agent-service-in-action.34fb465c9a84659e.webp)

لاستخدام أي من هذه الأدوات مع الخدمة، يمكننا إنشاء عميل وتعريف أداة أو مجموعة أدوات. لتنفيذ ذلك عمليًا، يمكننا استخدام الشفرة Python التالية. سيتمكن نموذج اللغة من النظر إلى مجموعة الأدوات وتحديد ما إذا كان سيستخدم الدالة التي أنشأها المستخدم، `fetch_sales_data_using_sqlite_query`، أو مفسر الشفرة المبني مسبقًا بناءً على طلب المستخدم.

```python 
import os
from azure.ai.projects import AIProjectClient
from azure.identity import DefaultAzureCredential
from fetch_sales_data_functions import fetch_sales_data_using_sqlite_query # دالة fetch_sales_data_using_sqlite_query الموجودة في ملف fetch_sales_data_functions.py.
from azure.ai.projects.models import ToolSet, FunctionTool, CodeInterpreterTool

project_client = AIProjectClient.from_connection_string(
    credential=DefaultAzureCredential(),
    conn_str=os.environ["PROJECT_CONNECTION_STRING"],
)

# تهيئة مجموعة الأدوات
toolset = ToolSet()

# تهيئة وكيل استدعاء الدوال مع دالة fetch_sales_data_using_sqlite_query وإضافتها إلى مجموعة الأدوات
fetch_data_function = FunctionTool(fetch_sales_data_using_sqlite_query)
toolset.add(fetch_data_function)

# تهيئة أداة مترجم الكود وإضافتها إلى مجموعة الأدوات.
code_interpreter = CodeInterpreterTool()toolset.add(code_interpreter)

agent = project_client.agents.create_agent(
    model="gpt-5-mini", name="my-agent", instructions="You are helpful agent", 
    toolset=toolset
)
```

## ما هي الاعتبارات الخاصة باستخدام نمط تصميم استخدام الأدوات لبناء وكلاء ذكاء اصطناعي جديرين بالثقة؟

من المخاوف الشائعة مع SQL الذي يولده نموذج اللغة ديناميكيًا هو الأمان، خصوصًا خطر حقن SQL أو الأفعال الخبيثة، مثل حذف أو التلاعب بقاعدة البيانات. في حين أن هذه المخاوف صحيحة، يمكن التخفيف منها بشكل فعال من خلال تكوين أذونات الوصول إلى قاعدة البيانات بشكل صحيح. بالنسبة لمعظم قواعد البيانات، يتضمن ذلك تكوين قاعدة البيانات كقراءة فقط. لخدمات قواعد البيانات مثل PostgreSQL أو Azure SQL، يجب تعيين دور قراءة فقط (SELECT) للتطبيق.

تشغيل التطبيق في بيئة آمنة يعزز الحماية بشكل إضافي. في سيناريوهات المؤسسات، عادةً ما يتم استخراج البيانات وتحويلها من الأنظمة التشغيلية إلى قاعدة بيانات أو مستودع بيانات للقراءة فقط مع مخطط سهل الاستخدام. يضمن هذا النهج أمان البيانات وتحسين الأداء وسهولة الوصول، وأن يكون للتطبيق وصول محدود ومقيد بالقراءة فقط.

## شفرات نموذجية

- بايثون: [إطار العمل للوكيل](./code_samples/04-python-agent-framework.ipynb)
- .NET: [إطار العمل للوكيل](./code_samples/04-dotnet-agent-framework.md)

## هل لديك المزيد من الأسئلة حول أنماط تصميم استخدام الأدوات؟

انضم إلى [خادم Discord الخاص بـ Microsoft Foundry](https://discord.com/invite/ATgtXmAS5D) للقاء متعلمين آخرين، حضور ساعات المكتبة والحصول على إجابات لأسئلتك حول وكلاء الذكاء الاصطناعي.

## موارد إضافية

- <a href="https://microsoft.github.io/build-your-first-agent-with-azure-ai-agent-service-workshop/" target="_blank">ورشة عمل خدمة وكلاء الذكاء الاصطناعي من Azure</a>
- <a href="https://github.com/Azure-Samples/contoso-creative-writer/tree/main/docs/workshop" target="_blank">ورشة عمل Contoso Creative Writer متعددة الوكلاء</a>
- <a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">نظرة عامة على إطار عمل الوكيل من Microsoft</a>


## اختبار سريع لهذا الوكيل (اختياري)

بعد أن تتعلم كيفية نشر الوكلاء في [الدرس 16](../16-deploying-scalable-agents/README.md)، يمكنك إجراء اختبار سريع لوكيل الدرس هذا `TravelToolAgent` (هل لا يزال يستدعي أداوته ويرد؟) باستخدام [`tests/lesson-04-smoke-tests.json`](../../../tests/lesson-04-smoke-tests.json). انظر [`tests/README.md`](../tests/README.md) لمعرفة كيفية تشغيله.

## الدرس السابق

[فهم أنماط التصميم الوكيلية](../03-agentic-design-patterns/README.md)

## الدرس التالي

[وكالة RAG](../05-agentic-rag/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**تنويه**:
تمت ترجمة هذا المستند باستخدام خدمة الترجمة بالذكاء الاصطناعي [Co-op Translator](https://github.com/Azure/co-op-translator). بينما نسعى للدقة، يرجى العلم أن الترجمات الآلية قد تحتوي على أخطاء أو عدم دقة. يجب اعتبار المستند الأصلي بلغته الأصلية المصدر الرسمي والمعتمد. للمعلومات الهامة، يُنصح بالاستعانة بترجمة بشرية محترفة. نحن غير مسؤولين عن أي سوء فهم أو تفسير ناتج عن استخدام هذه الترجمة.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->