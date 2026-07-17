[![كيفية تصميم وكلاء ذكاء اصطناعي جيدين](../../../translated_images/ar/lesson-4-thumbnail.546162853cb3daff.webp)](https://youtu.be/vieRiPRx-gI?si=cEZ8ApnT6Sus9rhn)

> _(انقر على الصورة أعلاه لمشاهدة فيديو الدرس)_

# نمط تصميم استخدام الأدوات

الأدوات مثيرة للاهتمام لأنها تتيح لوكلاء الذكاء الاصطناعي نطاقًا أوسع من القدرات. بدلاً من أن يمتلك الوكيل مجموعة محدودة من الإجراءات التي يمكنه تنفيذها، بإضافة أداة، يمكن للوكيل الآن تنفيذ مجموعة واسعة من الإجراءات. في هذا الفصل، سنلقي نظرة على نمط تصميم استخدام الأدوات، الذي يصف كيفية استخدام وكلاء الذكاء الاصطناعي لأدوات محددة لتحقيق أهدافهم.

## مقدمة

في هذا الدرس، نسعى للإجابة على الأسئلة التالية:

- ما هو نمط تصميم استخدام الأدوات؟
- ما هي حالات الاستخدام التي يمكن تطبيقه عليها؟
- ما هي العناصر/الوحدات الأساسية اللازمة لتنفيذ نمط التصميم؟
- ما هي الاعتبارات الخاصة لاستخدام نمط تصميم استخدام الأدوات لبناء وكلاء ذكاء اصطناعي موثوقين؟

## أهداف التعلم

بعد إكمال هذا الدرس، ستتمكن من:

- تعريف نمط تصميم استخدام الأدوات وهدفه.
- التعرف على حالات الاستخدام التي ينطبق عليها نمط تصميم استخدام الأدوات.
- فهم العناصر الرئيسية اللازمة لتنفيذ نمط التصميم.
- التعرف على الاعتبارات لضمان موثوقية وكلاء الذكاء الاصطناعي الذين يستخدمون هذا النمط.

## ما هو نمط تصميم استخدام الأدوات؟

يركز **نمط تصميم استخدام الأدوات** على تمكين نماذج اللغة الكبيرة (LLMs) من التفاعل مع أدوات خارجية لتحقيق أهداف محددة. الأدوات هي أكواد يمكن تنفيذها بواسطة الوكيل لأداء إجراءات. يمكن أن تكون الأداة دالة بسيطة مثل الآلة الحاسبة، أو استدعاء API لخدمة طرف ثالث مثل البحث عن أسعار الأسهم أو توقعات الطقس. في سياق وكلاء الذكاء الاصطناعي، تم تصميم الأدوات لتُنفّذ بواسطة الوكلاء استجابةً لـ **استدعاءات الدوال التي تُولدها النماذج**.

## ما هي حالات الاستخدام التي يمكن تطبيقه عليها؟

يمكن لوكلاء الذكاء الاصطناعي الاستفادة من الأدوات لإتمام المهام المعقدة، استرجاع المعلومات، أو اتخاذ القرارات. يُستخدم نمط تصميم استخدام الأدوات غالبًا في السيناريوهات التي تتطلب تفاعلاً ديناميكيًا مع أنظمة خارجية، مثل قواعد البيانات، خدمات الويب، أو مترجم الأكواد. هذه القدرة مفيدة لعدد من حالات الاستخدام المختلفة بما في ذلك:

- **استرجاع المعلومات الديناميكي:** يمكن للوكلاء استعلام APIs خارجية أو قواعد بيانات للحصول على بيانات محدثة (مثل استعلام قاعدة بيانات SQLite لتحليل البيانات، جلب أسعار الأسهم أو معلومات الطقس).
- **تنفيذ وتفسير الأكواد:** يمكن للوكلاء تنفيذ الأكواد أو السكريبتات لحل مسائل رياضية، توليد تقارير، أو إجراء المحاكاة.
- **تشغيل سير العمل تلقائيًا:** أتمتة الأعمال المتكررة أو متعددة الخطوات عن طريق دمج أدوات مثل مجدولات المهام، خدمات البريد الإلكتروني، أو خطوط بيانات.
- **دعم العملاء:** يمكن للوكلاء التفاعل مع أنظمة إدارة علاقات العملاء، منصات التذاكر، أو قواعد المعرفة لحل استفسارات المستخدمين.
- **توليد وتحرير المحتوى:** يمكن للوكلاء الاستفادة من أدوات مثل مدققي القواعد، ملخصات النصوص، أو تقييمات سلامة المحتوى لمساعدة مهام إنشاء المحتوى.

## ما هي العناصر/الوحدات الأساسية اللازمة لتنفيذ نمط تصميم استخدام الأدوات؟

تتيح هذه الوحدات الأساسية لوكيل الذكاء الاصطناعي أداء مجموعة واسعة من المهام. دعونا نلقي نظرة على العناصر الرئيسية اللازمة لتنفيذ نمط تصميم استخدام الأدوات:

- **مخططات الوظائف/الأدوات**: تعريفات مفصلة للأدوات المتاحة، تشمل اسم الوظيفة، الغرض منها، المعلمات المطلوبة، والمخرجات المتوقعة. تُمكّن هذه المخططات نموذج اللغة الكبير من فهم الأدوات المتوفرة وكيفية تكوين طلبات صحيحة.

- **منطق تنفيذ الوظائف**: يحكم كيفية ووقت استدعاء الأدوات بناءً على نية المستخدم وسياق المحادثة. قد يشمل ذلك وحدات التخطيط، آليات التوجيه، أو تدفقات شرطية تحدد استخدام الأداة بشكل ديناميكي.

- **نظام معالجة الرسائل**: مكونات تدير تدفق المحادثة بين مدخلات المستخدم، ردود نموذج اللغة، استدعاءات الأدوات، ومخرجات الأدوات.

- **إطار تكامل الأدوات**: البنية التحتية التي تربط الوكيل بالأدوات المختلفة، سواء أكانت دوال بسيطة أو خدمات خارجية معقدة.

- **التعامل مع الأخطاء والتحقق**: آليات معالجة الفشل في تنفيذ الأدوات، التحقق من المعاملات، وإدارة الردود غير المتوقعة.

- **إدارة الحالة**: تتبع سياق المحادثة، التفاعلات السابقة مع الأدوات، والبيانات المستمرة لضمان الاتساق عبر التفاعلات المتعددة.

بعد ذلك، دعونا نلقي نظرة أكثر تفصيلًا على استدعاء الوظائف/الأدوات.
 
### استدعاء الوظائف/الأدوات

استدعاء الوظائف هو الطريقة الأساسية التي نُمكّن بها نماذج اللغة الكبيرة من التفاعل مع الأدوات. ستلاحظ كثيرًا استخدام مصطلحي "الوظيفة" و"الأداة" بالتبادل لأن "الدوال" (كتل من الكود القابلة لإعادة الاستخدام) هي "الأدوات" التي يستخدمها الوكلاء لأداء المهام. ولكي يتم استدعاء كود الوظيفة، يجب على نموذج اللغة الكبيرة مقارنة طلب المستخدم مع وصف الوظائف. للقيام بذلك، يتم إرسال مخطط يحتوي على أوصاف جميع الوظائف المتاحة إلى النموذج. ثم يختار النموذج الوظيفة الأنسب للمهمة ويُرجع اسمها ومعاملاتها. تُستدعى الوظيفة المحددة، ويتم إرسال ردها مرة أخرى إلى النموذج الذي يستخدم المعلومات للرد على طلب المستخدم.

لكي يتمكن المطورون من تنفيذ استدعاء الوظائف للوكلاء، ستحتاج إلى:

1. نموذج LLM يدعم استدعاء الوظائف
2. مخطط يحتوي على أوصاف الوظائف
3. الكود الخاص بكل وظيفة موصوفة

دعونا نستخدم مثال الحصول على الوقت الحالي في مدينة لتوضيح ذلك:

1. **تهيئة نموذج LLM يدعم استدعاء الوظائف:**

    ليست جميع النماذج تدعم استدعاء الوظائف، لذلك من المهم التحقق من أن نموذج اللغة الكبير الذي تستخدمه يدعم ذلك. <a href="https://learn.microsoft.com/azure/ai-services/openai/how-to/function-calling" target="_blank">Azure OpenAI</a> يدعم استدعاء الوظائف. يمكننا البدء بتهيئة عميل OpenAI باستخدام Azure OpenAI **واجهة استجابات API** (نقطة النهاية المستقرة `/openai/v1/` — لا حاجة لـ `api_version`). 

    ```python
    # تهيئة عميل OpenAI لخدمة Azure OpenAI (واجهة برمجة التطبيقات للاستجابات، نقطة النهاية v1)
    client = OpenAI(
        base_url=f"{os.environ['AZURE_OPENAI_ENDPOINT'].rstrip('/')}/openai/v1/",
        api_key=os.environ["AZURE_OPENAI_API_KEY"],
    )
    deployment_name = os.environ["AZURE_OPENAI_DEPLOYMENT"]
    ```

1. **إنشاء مخطط للوظيفة**:

    بعد ذلك، سنعرف مخطط JSON يحتوي على اسم الوظيفة، وصف لما تقوم به، وأسماء ووصف معاملات الوظيفة.
    ثم نمرر هذا المخطط إلى العميل الذي تم إنشاؤه سابقًا، مع طلب المستخدم لمعرفة الوقت في سان فرانسيسكو. المهم ملاحظته هو أن **استدعاء الأداة** هو ما يُعاد، **وليس** الإجابة النهائية على السؤال. كما ذُكر سابقًا، يعيد نموذج اللغة الكبير اسم الوظيفة التي اختارها للمهمة، والمعاملات التي ستمرر إليها.

    ```python
    # وصف الدالة للنموذج للقراءة (تنسيق أداة API للاستجابات المسطحة)
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

    # تُرجع واجهة برمجة التطبيقات للردود استدعاءات الأدوات كعناصر function_call في response.output.
    # أضفها إلى المحادثة حتى يكون للنموذج السياق الكامل في الدور التالي.
    messages += response.output

    print("Model's response:")
    print(response.output)
  
    ```

    ```bash
    Model's response:
    [ResponseFunctionToolCall(arguments='{"location":"San Francisco"}', call_id='call_pOsKdUlqvdyttYB67MOj434b', name='get_current_time', type='function_call')]
    ```
  
1. **كود الوظيفة اللازم لتنفيذ المهمة:**

    بعد أن اختار نموذج اللغة الكبير الوظيفة التي يجب تشغيلها، يجب تنفيذ كود أداء المهمة.
    يمكننا تنفيذ الكود اللازم للحصول على الوقت الحالي بلغة بايثون. كما سنحتاج إلى كتابة الكود لاستخراج الاسم والمعاملات من رسالة الرد للحصول على النتيجة النهائية.

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
    # معالجة استدعاءات الدالة
    tool_calls = [item for item in response.output if item.type == "function_call"]
    if tool_calls:
        for tool_call in tool_calls:
            if tool_call.name == "get_current_time":

                function_args = json.loads(tool_call.arguments)

                time_response = get_current_time(
                    location=function_args.get("location")
                )

                # إعادة نتيجة الأداة كعنصر function_call_output
                messages.append({
                    "type": "function_call_output",
                    "call_id": tool_call.call_id,
                    "output": time_response,
                })
    else:
        print("No tool calls were made by the model.")

    # استدعاء API الثاني: الحصول على الاستجابة النهائية من النموذج
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

استدعاء الوظائف هو جوهر معظم، إن لم يكن كل، تصميم استخدام الأدوات لدى الوكلاء، لكن تنفيذه من الصفر يمكن أن يكون أحيانًا تحديًا.
كما تعلمنا في [الدرس 2](../../../02-explore-agentic-frameworks) توفر أُطُر العمل الوكيلة بنايات معدة مسبقًا لتنفيذ استخدام الأدوات.
 
## أمثلة على استخدام الأدوات مع أُطُر العمل الوكيلة

إليك بعض الأمثلة على كيفية تنفيذ نمط تصميم استخدام الأدوات باستخدام أُطُر عمل وكيلة مختلفة:

### إطار عمل Microsoft Agent

<a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Microsoft Agent Framework</a> هو إطار عمل ذكاء اصطناعي مفتوح المصدر لبناء وكلاء ذكاء اصطناعي. يبسط عملية استخدام استدعاء الوظائف من خلال السماح لك بتعريف الأدوات كدوال بايثون مزينة بالـ `@tool` décorator. يتولى الإطار التعامل مع التواصل ذهابًا وإيابًا بين النموذج والكود الخاص بك. كما يوفر الوصول إلى أدوات مدمجة مسبقًا مثل البحث في الملفات ومترجم الأكواد عبر `FoundryChatClient`.

يوضح الرسم البياني التالي عملية استدعاء الوظائف مع إطار عمل Microsoft Agent:

![function calling](../../../translated_images/ar/functioncalling-diagram.a84006fc287f6014.webp)

في إطار عمل Microsoft Agent، يتم تعريف الأدوات كدوال مزينة. يمكننا تحويل الدالة `get_current_time` التي رأيناها سابقًا إلى أداة باستخدام décorator `@tool`. سيقوم الإطار تلقائيًا بتسلسل الدالة ومعاملاتها، وإنشاء المخطط لإرساله إلى نموذج اللغة الكبير.

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

# إنشاء وكيل وتشغيله باستخدام الأداة
agent = provider.as_agent(name="TimeAgent", instructions="Use available tools to answer questions.", tools=get_current_time)
response = await agent.run("What time is it?")
```
  
### خدمة Microsoft Foundry Agent

<a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Microsoft Foundry Agent Service</a> هي أُطُر عمل وكيلة أحدث مصممة لتمكين المطورين من بناء، نشر، وتوسيع وكلاء ذكاء اصطناعي عالي الجودة قابلين للتطوير بأمان دون الحاجة لإدارة موارد الحوسبة والتخزين الأساسية. وهي مفيدة بشكل خاص للتطبيقات المؤسسية كونها خدمة مُدارة بالكامل بأمان من الدرجة المؤسسية.

عند مقارنتها بالتطوير باستخدام API نموذج اللغة الكبير مباشرة، تقدم خدمة Microsoft Foundry Agent بعض المزايا، بما في ذلك:

- استدعاء الأدوات تلقائيًا – لا حاجة لتحليل استدعاء الأداة، استدعاء الأداة، والتعامل مع الرد؛ كل هذا يتم الآن على الخادم
- إدارة البيانات بأمان – بدلاً من إدارة حالة المحادثة الخاصة بك، يمكنك الاعتماد على "الخيوط" لتخزين كل المعلومات التي تحتاجها
- أدوات جاهزة للاستخدام – أدوات يمكنك استخدامها للتفاعل مع مصادر بياناتك، مثل Bing، Azure AI Search، وAzure Functions.

يمكن تقسيم الأدوات المتاحة في خدمة Microsoft Foundry Agent إلى فئتين:

1. أدوات المعرفة:
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/bing-grounding?tabs=python&pivots=overview" target="_blank">التأسيس مع بحث Bing</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/file-search?tabs=python&pivots=overview" target="_blank">البحث في الملفات</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-ai-search?tabs=azurecli%2Cpython&pivots=overview-azure-ai-search" target="_blank">بحث Azure AI</a>

2. أدوات الإجراءات:
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/function-calling?tabs=python&pivots=overview" target="_blank">استدعاء الوظائف</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/code-interpreter?tabs=python&pivots=overview" target="_blank">مترجم الأكواد</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/openapi-spec?tabs=python&pivots=overview" target="_blank">أدوات معرفة بواسط OpenAPI</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-functions?pivots=overview" target="_blank">وظائف Azure</a>

تتيح خدمة الوكيل لنا استخدام هذه الأدوات معًا كمجموعة أدوات `toolset`. كما تستخدم `الخيوط` التي تتتبع سجل الرسائل من محادثة معينة.

تخيل أنك وكيل مبيعات في شركة تُدعى Contoso. تريد تطوير وكيل محادثة يمكنه الإجابة عن أسئلة حول بيانات مبيعاتك.

توضح الصورة التالية كيف يمكنك استخدام خدمة Microsoft Foundry Agent لتحليل بيانات مبيعاتك:

![Agentic Service In Action](../../../translated_images/ar/agent-service-in-action.34fb465c9a84659e.webp)

لاستخدام أي من هذه الأدوات مع الخدمة، يمكننا إنشاء عميل وتحديد أداة أو مجموعة أدوات. لتنفيذ ذلك عمليًا، يمكننا استخدام كود بايثون التالي. سيكون نموذج اللغة الكبير قادرًا على النظر في مجموعة الأدوات وتحديد ما إذا كان سيستخدم الدالة التي أنشأها المستخدم، `fetch_sales_data_using_sqlite_query`، أو مترجم الأكواد المدمج حسب طلب المستخدم.

```python 
import os
from azure.ai.projects import AIProjectClient
from azure.identity import DefaultAzureCredential
from fetch_sales_data_functions import fetch_sales_data_using_sqlite_query # دالة fetch_sales_data_using_sqlite_query التي يمكن العثور عليها في ملف fetch_sales_data_functions.py.
from azure.ai.projects.models import ToolSet, FunctionTool, CodeInterpreterTool

project_client = AIProjectClient.from_connection_string(
    credential=DefaultAzureCredential(),
    conn_str=os.environ["PROJECT_CONNECTION_STRING"],
)

# تهيئة مجموعة الأدوات
toolset = ToolSet()

# تهيئة وكيل استدعاء الدالة مع دالة fetch_sales_data_using_sqlite_query وإضافتها إلى مجموعة الأدوات
fetch_data_function = FunctionTool(fetch_sales_data_using_sqlite_query)
toolset.add(fetch_data_function)

# تهيئة أداة مترجم الشيفرة البرمجية وإضافتها إلى مجموعة الأدوات.
code_interpreter = CodeInterpreterTool()toolset.add(code_interpreter)

agent = project_client.agents.create_agent(
    model="gpt-4.1-mini", name="my-agent", instructions="You are helpful agent", 
    toolset=toolset
)
```

## ما هي الاعتبارات الخاصة لاستخدام نمط تصميم استخدام الأدوات لبناء وكلاء ذكاء اصطناعي موثوقين؟

من المخاوف الشائعة مع SQL التي تُولد ديناميكيًا بواسطة نماذج اللغة الكبيرة هو الأمان، خصوصًا خطر حقن SQL أو الإجراءات الخبيثة مثل حذف أو العبث بقاعدة البيانات. بينما هذه المخاوف صحيحة، يمكن التخفيف منها بفعالية من خلال تكوين أذونات وصول قاعدة البيانات بشكل صحيح. بالنسبة لمعظم قواعد البيانات، يتضمن هذا تكوين قاعدة البيانات كوضع للقراءة فقط. بالنسبة لخدمات قواعد البيانات مثل PostgreSQL أو Azure SQL، يجب تعيين تطبيقك بدور قراءة فقط (SELECT).

تشغيل التطبيق في بيئة آمنة يعزز الحماية بشكل أكبر. في السيناريوهات المؤسسية، يتم عادة استخراج وتحويل البيانات من الأنظمة التشغيلية إلى قاعدة بيانات للقراءة فقط أو مستودع بيانات مع مخطط سهل الاستخدام. يضمن هذا النهج أن تكون البيانات آمنة، ومحسنة للأداء والوصول، وأن يكون لتطبيقك وصول مقيد للقراءة فقط.

## أكواد عينية

- بايثون: [إطار الوكيل](./code_samples/04-python-agent-framework.ipynb)
- دوت نت: [إطار الوكيل](./code_samples/04-dotnet-agent-framework.md)

## هل لديك المزيد من الأسئلة حول نمط تصميم استخدام الأدوات؟

انضم إلى [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D) للقاء متعلمين آخرين، وحضور ساعات المكتب، والحصول على إجابات لأسئلتك حول وكلاء الذكاء الاصطناعي.

## موارد إضافية

- <a href="https://microsoft.github.io/build-your-first-agent-with-azure-ai-agent-service-workshop/" target="_blank">ورشة عمل خدمة وكلاء Azure AI</a>
- <a href="https://github.com/Azure-Samples/contoso-creative-writer/tree/main/docs/workshop" target="_blank">ورشة عمل Contoso Creative Writer متعددة الوكلاء</a>
- <a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">نظرة عامة على إطار عمل Microsoft Agent</a>


## اختبار الدخان لهذا الوكيل (اختياري)

بعد أن تتعلم كيفية نشر الوكلاء في [الدرس 16](../16-deploying-scalable-agents/README.md)، يمكنك اختبار الدخان لوكيل هذا الدرس `TravelToolAgent` (هل ما زال يستدعي أدواته ويجيب؟) باستخدام [`tests/lesson-04-smoke-tests.json`](../../../tests/lesson-04-smoke-tests.json). راجع [`tests/README.md`](../tests/README.md) لمعرفة كيفية تشغيله.

## الدرس السابق

[فهم أنماط التصميم الوكالية](../03-agentic-design-patterns/README.md)

## الدرس التالي

[Agentic RAG](../05-agentic-rag/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**تنويه**:
تمت ترجمة هذا المستند باستخدام خدمة الترجمة بالذكاء الاصطناعي [Co-op Translator](https://github.com/Azure/co-op-translator). بينما نسعى للدقة، يرجى العلم أن الترجمات الآلية قد تحتوي على أخطاء أو عدم دقة. يجب اعتبار المستند الأصلي بلغته الأصلية المصدر الرسمي والمعتمد. للمعلومات الهامة، يُنصح بالاستعانة بترجمة بشرية محترفة. نحن غير مسؤولين عن أي سوء فهم أو تفسير ناتج عن استخدام هذه الترجمة.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->