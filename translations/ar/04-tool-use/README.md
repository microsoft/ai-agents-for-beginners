[![كيفية تصميم وكلاء ذكاء اصطناعي جيدين](../../../translated_images/ar/lesson-4-thumbnail.546162853cb3daff.webp)](https://youtu.be/vieRiPRx-gI?si=cEZ8ApnT6Sus9rhn)

> _(انقر على الصورة أعلاه لمشاهدة فيديو هذا الدرس)_

# نمط تصميم استخدام الأدوات

الأدوات مثيرة للاهتمام لأنها تسمح لوكلاء الذكاء الاصطناعي بامتلاك نطاق أوسع من القدرات. بدلاً من أن يكون للوكيل مجموعة محدودة من الإجراءات التي يمكنه القيام بها، بإضافة أداة، يمكن للوكيل الآن أداء مجموعة واسعة من الإجراءات. في هذا الفصل، سوف ندرس نمط تصميم استخدام الأدوات، الذي يصف كيف يمكن لوكلاء الذكاء الاصطناعي استخدام أدوات محددة لتحقيق أهدافهم.

## المقدمة

في هذا الدرس، نسعى للإجابة على الأسئلة التالية:

- ما هو نمط تصميم استخدام الأدوات؟
- ما هي حالات الاستخدام التي يمكن تطبيقه عليها؟
- ما هي العناصر/الكتل الإنشائية اللازمة لتطبيق نمط التصميم؟
- ما هي الاعتبارات الخاصة باستخدام نمط تصميم استخدام الأدوات لبناء وكلاء ذكاء اصطناعي موثوقين؟

## أهداف التعلم

بعد إكمال هذا الدرس، ستكون قادرًا على:

- تعريف نمط تصميم استخدام الأدوات وهدفه.
- تحديد حالات الاستخدام التي يمكن فيها تطبيق نمط تصميم استخدام الأدوات.
- فهم العناصر الرئيسية اللازمة لتطبيق نمط التصميم.
- التعرف على الاعتبارات لضمان الموثوقية في الوكلاء باستخدام هذا النمط.

## ما هو نمط تصميم استخدام الأدوات؟

يركز **نمط تصميم استخدام الأدوات** على تمكين نماذج اللغة الكبيرة (LLMs) من التفاعل مع الأدوات الخارجية لتحقيق أهداف محددة. الأدوات هي شفرة يمكن تنفيذها بواسطة الوكيل لأداء إجراءات. يمكن أن تكون الأداة دالة بسيطة مثل آلة حاسبة، أو استدعاء لواجهة برمجة تطبيقات (API) لخدمة طرف ثالث مثل البحث عن سعر السهم أو توقع الطقس. في سياق وكلاء الذكاء الاصطناعي، تم تصميم الأدوات ليتم تنفيذها بواسطة الوكلاء استجابةً لـ **مكالمات الدالة التي يولدها النموذج**.

## ما هي حالات الاستخدام التي يمكن تطبيقها؟

يمكن لوكلاء الذكاء الاصطناعي الاستفادة من الأدوات لإكمال مهام معقدة، استرجاع المعلومات، أو اتخاذ القرارات. يُستخدم نمط تصميم استخدام الأدوات غالبًا في السيناريوهات التي تتطلب تفاعلًا ديناميكيًا مع أنظمة خارجية مثل قواعد البيانات، الخدمات الويب، أو مفسرات الشفرات. هذه القدرة مفيدة لعدد من حالات الاستخدام المختلفة بما في ذلك:

- **استرجاع معلومات ديناميكية:** يمكن للوكلاء استعلام واجهات برمجة التطبيقات الخارجية أو قواعد البيانات لجلب بيانات محدثة (مثل الاستعلام عن قاعدة بيانات SQLite لتحليل البيانات، جلب أسعار الأسهم أو معلومات الطقس).
- **تنفيذ الشفرة والتفسير:** يمكن للوكلاء تنفيذ الشفرات أو السكريبتات لحل المسائل الرياضية، إنشاء تقارير، أو أداء المحاكاة.
- **أتمتة سير العمل:** أتمتة عمليات متكررة أو متعددة الخطوات من خلال دمج أدوات مثل مجدولات المهام، خدمات البريد الإلكتروني، أو خطوط نقل البيانات.
- **دعم العملاء:** يمكن للوكلاء التفاعل مع أنظمة إدارة علاقات العملاء (CRM)، منصات التذاكر، أو قواعد المعرفة لحل استفسارات المستخدمين.
- **إنشاء المحتوى والتحرير:** يمكن للوكلاء الاستعانة بأدوات مثل مدققي القواعد النحوية، ملخصات النصوص، أو مقيمي سلامة المحتوى للمساعدة في مهام إنشاء المحتوى.

## ما هي العناصر/الكتل الإنشائية اللازمة لتطبيق نمط تصميم استخدام الأدوات؟

تتيح هذه الكتل الإنشائية لوكيل الذكاء الاصطناعي أداء مجموعة واسعة من المهام. دعونا نلقي نظرة على العناصر الرئيسية اللازمة لتطبيق نمط تصميم استخدام الأدوات:

- **مخططات الدوال/الأدوات**: تعريفات مفصلة للأدوات المتاحة، تتضمن اسم الدالة، الغرض، المعلمات المطلوبة، والمخرجات المتوقعة. تمكِّن هذه المخططات نموذج اللغة الكبير (LLM) من فهم الأدوات المتوفرة وكيفية إنشاء طلبات صحيحة.

- **منطق تنفيذ الدوال**: تحكم في كيفية وموعد استدعاء الأدوات استنادًا إلى نية المستخدم وسياق المحادثة. قد يشمل ذلك وحدات التخطيط، آليات التوجيه، أو التدفقات الشرطية التي تحدد استخدام الأدوات بشكل ديناميكي.

- **نظام معالجة الرسائل**: مكونات تدير تدفق المحادثة بين مدخلات المستخدم، استجابات نموذج اللغة الكبير، مكالمات الأدوات، ومخرجات الأدوات.

- **إطار تكامل الأدوات**: البنية التحتية التي تربط الوكيل بالأدوات المختلفة، سواء كانت دوال بسيطة أو خدمات خارجية معقدة.

- **معالجة الأخطاء والتحقق**: آليات للتعامل مع فشل تنفيذ الأدوات، التحقق من المعلمات، وإدارة الاستجابات غير المتوقعة.

- **إدارة الحالة**: تتبع سياق المحادثة، التفاعلات السابقة مع الأدوات، والبيانات الدائمة لضمان الاتساق عبر التفاعلات متعددة الأدوار.

بعد ذلك، دعونا نلقي نظرة مفصلة على استدعاء الدوال/الأدوات.

### استدعاء الدوال/الأدوات

استدعاء الدوال هو الطريقة الأساسية التي نرمّز بها تمكين نماذج اللغة الكبيرة (LLMs) من التفاعل مع الأدوات. ستلاحظ غالبًا استخدام 'الدالة' و'الأداة' بالتبادل لأن 'الدوال' (كتل البرمجيات القابلة لإعادة الاستخدام) هي 'الأدوات' التي يستخدمها الوكلاء لأداء المهام. لكي يتم استدعاء شفرة دالة ما، يجب على نموذج اللغة الكبير مقارنة طلب المستخدم بوصافة الدالة. للقيام بذلك، يتم إرسال مخطط يحتوي على وصف كل الدوال المتاحة إلى نموذج اللغة الكبير. ثم يختار نموذج اللغة الكبير الدالة الأكثر ملاءمة للمهمة ويرجع اسمها ومعاملاتها. يتم استدعاء الدالة المختارة، ويتم إرسال استجابتها إلى نموذج اللغة الكبير، الذي يستخدم المعلومات للرد على طلب المستخدم.

لكي يتمكن المطورون من تنفيذ استدعاء الدوال للوكلاء، ستحتاج إلى:

1. نموذج LLM يدعم استدعاء الدوال
2. مخطط يحتوي على وصف الدوال
3. شفرة لكل دالة موصوفة

لنستخدم مثال الحصول على الوقت الحالي في مدينة لتوضيح ذلك:

1. **تهيئة نموذج LLM يدعم استدعاء الدوال:**

    ليست جميع النماذج تدعم استدعاء الدوال، لذا من المهم التحقق مما إذا كان النموذج الذي تستخدمه يفعل ذلك. يدعم <a href="https://learn.microsoft.com/azure/ai-services/openai/how-to/function-calling" target="_blank">Azure OpenAI</a> استدعاء الدوال. يمكننا البدء بمبادرة عميل Azure OpenAI.

    ```python
    # تهيئة عميل Azure OpenAI
    client = AzureOpenAI(
        azure_endpoint = os.getenv("AZURE_OPENAI_ENDPOINT"), 
        api_key=os.getenv("AZURE_OPENAI_API_KEY"),  
        api_version="2024-05-01-preview"
    )
    ```

1. **إنشاء مخطط دالة:**

    بعد ذلك سنقوم بتعريف مخطط JSON يحتوي على اسم الدالة، وصف ما تقوم به الدالة، وأسماء وأوصاف معلمات الدالة. ثم نأخذ هذا المخطط ونمرره إلى العميل المُنشأ سابقًا، إلى جانب طلب المستخدم للعثور على الوقت في سان فرانسيسكو. المهم أن نلاحظ أن **مكالمة الأداة** هي التي يتم إرجاعها، **ليست** الإجابة النهائية على السؤال. كما ذكرنا سابقًا، يعيد نموذج اللغة الكبير اسم الدالة التي اختارها للمهمة، والمعاملات التي ستمرير إليها.

    ```python
    # وصف الدالة للنموذج للقراءة
    tools = [
        {
            "type": "function",
            "function": {
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
        }
    ]
    ```
   
    ```python
  
    # رسالة المستخدم الابتدائية
    messages = [{"role": "user", "content": "What's the current time in San Francisco"}] 
  
    # أول استدعاء لواجهة البرمجة: طلب من النموذج استخدام الدالة
      response = client.chat.completions.create(
          model=deployment_name,
          messages=messages,
          tools=tools,
          tool_choice="auto",
      )
  
      # معالجة رد النموذج
      response_message = response.choices[0].message
      messages.append(response_message)
  
      print("Model's response:")  

      print(response_message)
  
    ```

    ```bash
    Model's response:
    ChatCompletionMessage(content=None, role='assistant', function_call=None, tool_calls=[ChatCompletionMessageToolCall(id='call_pOsKdUlqvdyttYB67MOj434b', function=Function(arguments='{"location":"San Francisco"}', name='get_current_time'), type='function')])
    ```
  
1. **شفرة الدالة اللازمة لأداء المهمة:**

    بعد أن اختار نموذج اللغة الكبير الدالة التي يجب تشغيلها، يجب تنفيذ وتشغيل الشفرة التي تؤدي المهمة.
    يمكننا تنفيذ الشفرة للحصول على الوقت الحالي في بايثون. سنحتاج أيضًا إلى كتابة الشفرة لاستخراج الاسم والمعاملات من response_message للحصول على النتيجة النهائية.

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
     # معالجة استدعاءات الوظائف
      if response_message.tool_calls:
          for tool_call in response_message.tool_calls:
              if tool_call.function.name == "get_current_time":
     
                  function_args = json.loads(tool_call.function.arguments)
     
                  time_response = get_current_time(
                      location=function_args.get("location")
                  )
     
                  messages.append({
                      "tool_call_id": tool_call.id,
                      "role": "tool",
                      "name": "get_current_time",
                      "content": time_response,
                  })
      else:
          print("No tool calls were made by the model.")  
  
      # استدعاء API الثاني: الحصول على الاستجابة النهائية من النموذج
      final_response = client.chat.completions.create(
          model=deployment_name,
          messages=messages,
      )
  
      return final_response.choices[0].message.content
     ```

     ```bash
      get_current_time called with location: San Francisco
      Timezone found for san francisco
      The current time in San Francisco is 09:24 AM.
     ```

استدعاء الدوال هو جوهر معظم، إن لم يكن كل، تصميم استخدام الأدوات للوكيل، ومع ذلك قد يكون تنفيذها من الصفر تحديًا أحيانًا.
كما تعلمنا في [الدرس 2](../../../02-explore-agentic-frameworks) توفر أطر العمل الوكلائية لنا كتل بناء مُعدة مسبقًا لتطبيق استخدام الأدوات.

## أمثلة على استخدام الأدوات مع أطر العمل الوكلائية

فيما يلي بعض الأمثلة على كيفية تنفيذ نمط تصميم استخدام الأدوات باستخدام أطر العمل الوكلائية المختلفة:

### Semantic Kernel

<a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Semantic Kernel</a> هو إطار عمل مفتوح المصدر للذكاء الاصطناعي لمطوري .NET و Python و Java الذين يعملون مع نماذج اللغة الكبيرة. يبسط عملية استخدام استدعاء الدوال من خلال وصف دوالك ومعاملاتها للنموذج تلقائيًا عبر عملية تسمى <a href="https://learn.microsoft.com/semantic-kernel/concepts/ai-services/chat-completion/function-calling/?pivots=programming-language-python#1-serializing-the-functions" target="_blank">التسلسل</a> (serializing). كما أنه يتعامل مع الاتصال ذهابًا وإيابًا بين النموذج والشفرة الخاصة بك. ميزة أخرى لاستخدام إطار عمل وكيل مثل Semantic Kernel هو أنه يتيح لك الوصول إلى أدوات مُعدة مسبقًا مثل <a href="https://github.com/microsoft/semantic-kernel/blob/main/python/samples/getting_started_with_agents/openai_assistant/step4_assistant_tool_file_search.py" target="_blank">البحث في الملفات</a> و<a href="https://github.com/microsoft/semantic-kernel/blob/main/python/samples/getting_started_with_agents/openai_assistant/step3_assistant_tool_code_interpreter.py" target="_blank">مفسر الشفرات</a>.

يوضح الرسم البياني التالي عملية استدعاء الدوال مع Semantic Kernel:

![function calling](../../../translated_images/ar/functioncalling-diagram.a84006fc287f6014.webp)

في Semantic Kernel تُسمى الدوال/الأدوات <a href="https://learn.microsoft.com/semantic-kernel/concepts/plugins/?pivots=programming-language-python" target="_blank">الإضافات (Plugins)</a>. يمكننا تحويل الدالة `get_current_time` التي رأيناها سابقًا إلى إضافة عن طريق تحويلها إلى صنف يحتوي على الدالة. يمكننا أيضًا استيراد مزين `kernel_function`، الذي يأخذ وصف الدالة. عند إنشاء Kernel باستخدام GetCurrentTimePlugin، يقوم Kernel تلقائيًا بتسلسل الدالة ومعاملاتها، وينشئ المخطط لإرساله إلى نموذج اللغة الكبير في هذه العملية.

```python
from semantic_kernel.functions import kernel_function

class GetCurrentTimePlugin:
    async def __init__(self, location):
        self.location = location

    @kernel_function(
        description="Get the current time for a given location"
    )
    def get_current_time(location: str = ""):
        ...

```

```python 
from semantic_kernel import Kernel

# إنشاء النواة
kernel = Kernel()

# إنشاء الملحق
get_current_time_plugin = GetCurrentTimePlugin(location)

# إضافة الملحق إلى النواة
kernel.add_plugin(get_current_time_plugin)
```
  
### خدمة Azure AI Agent

<a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">خدمة Azure AI Agent</a> هي إطار عمل وكيل أحدث، مصمم لتمكين المطورين من بناء ونشر وتوسيع نطاق وكلاء ذكاء اصطناعي عالي الجودة وقابل للتوسيع بأمان دون الحاجة لإدارة الموارد الحسابية والتخزينية الأساسية. وهي مفيدة بشكل خاص لتطبيقات المؤسسات حيث أنها خدمة مدارة بالكامل مع أمان بدرجة المؤسسات.

مقارنةً بالتطوير باستخدام واجهة برمجة تطبيقات LLM مباشرة، توفر خدمة Azure AI Agent بعض المزايا، بما في ذلك:

- استدعاء الأدوات آليًا – لا حاجة لتحليل مكالمة أداة، أو استدعاء الأداة، أو معالجة الاستجابة؛ فكل ذلك يتم الآن من جانب الخادم
- إدارة بيانات آمنة – بدلاً من إدارة حالة المحادثة بنفسك، يمكنك الاعتماد على الخيوط التي تخزن كل المعلومات التي تحتاجها
- أدوات متاحة جاهزة – أدوات يمكنك استخدامها للتفاعل مع مصادر بياناتك، مثل Bing، Azure AI Search، و Azure Functions.

يمكن تقسيم الأدوات المتاحة في خدمة Azure AI Agent إلى فئتين:

1. أدوات المعرفة:
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/bing-grounding?tabs=python&pivots=overview" target="_blank">التأسيس مع Bing Search</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/file-search?tabs=python&pivots=overview" target="_blank">البحث في الملفات</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-ai-search?tabs=azurecli%2Cpython&pivots=overview-azure-ai-search" target="_blank">بحث Azure AI</a>

2. أدوات الإجراء:
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/function-calling?tabs=python&pivots=overview" target="_blank">استدعاء الدوال</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/code-interpreter?tabs=python&pivots=overview" target="_blank">مفسر الشفرة</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/openapi-spec?tabs=python&pivots=overview" target="_blank">أدوات معرفّة بواسطة OpenAPI</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-functions?pivots=overview" target="_blank">وظائف Azure</a>

تتيح لنا خدمة Agent استخدام هذه الأدوات معًا كمجموعة أدوات (`toolset`). كما أنها تستخدم `الخيوط` التي تتتبع تاريخ الرسائل من محادثة معينة.

تخيل أنك وكيل مبيعات في شركة تسمى Contoso. تريد تطوير وكيل محادثة يمكنه الإجابة على أسئلة حول بيانات المبيعات الخاصة بك.

توضح الصورة التالية كيف يمكنك استخدام خدمة Azure AI Agent لتحليل بيانات المبيعات الخاصة بك:

![Agentic Service In Action](../../../translated_images/ar/agent-service-in-action.34fb465c9a84659e.webp)

لاستخدام أي من هذه الأدوات مع الخدمة، يمكننا إنشاء عميل وتعريف أداة أو مجموعة أدوات. لتطبيق هذا عمليًا، يمكننا استخدام كود Python التالي. سيتمكن نموذج اللغة الكبير (LLM) من النظر في مجموعة الأدوات وتقرير ما إذا كان يستخدم الدالة التي أنشأها المستخدم، `fetch_sales_data_using_sqlite_query`، أو مفسر الشفرة المُعد مسبقًا بناءً على طلب المستخدم.

```python 
import os
from azure.ai.projects import AIProjectClient
from azure.identity import DefaultAzureCredential
from fetch_sales_data_functions import fetch_sales_data_using_sqlite_query # دالة fetch_sales_data_using_sqlite_query والتي يمكن العثور عليها في ملف fetch_sales_data_functions.py.
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

# تهيئة أداة مترجم الأكواد وإضافتها إلى مجموعة الأدوات.
code_interpreter = code_interpreter = CodeInterpreterTool()
toolset.add(code_interpreter)

agent = project_client.agents.create_agent(
    model="gpt-4o-mini", name="my-agent", instructions="You are helpful agent", 
    toolset=toolset
)
```

## ما هي الاعتبارات الخاصة باستخدام نمط تصميم استخدام الأدوات لبناء وكلاء ذكاء اصطناعي موثوقين؟

قلق شائع يتعلق بالاستعلامات الديناميكية SQL التي يولدها نماذج اللغة الكبيرة هو الأمان، وخصوصًا خطر حقن SQL أو الإجراءات الخبيثة، مثل حذف أو العبث بقاعدة البيانات. بينما هذه المخاوف صحيحة، يمكن التخفيف منها بفعالية عن طريق تهيئة أذونات وصول قاعدة البيانات بشكل صحيح. بالنسبة لمعظم قواعد البيانات، يتضمن ذلك إعداد قاعدة البيانات كقراءة فقط. بالنسبة لخدمات قواعد البيانات مثل PostgreSQL أو Azure SQL، يجب تعيين التطبيق على دور قراءة فقط (SELECT).
تشغيل التطبيق في بيئة آمنة يعزز الحماية بشكل أكبر. في سيناريوهات الشركات، يتم عادةً استخراج البيانات وتحويلها من أنظمة التشغيل إلى قاعدة بيانات أو مستودع بيانات للقراءة فقط مع مخطط سهل الاستخدام. يضمن هذا النهج أن تكون البيانات آمنة، ومحسّنة للأداء وسهولة الوصول، وأن يكون وصول التطبيق مقيدًا وقراءة فقط.

## أمثلة على الأكواد

- Python: [Agent Framework](./code_samples/04-python-agent-framework.ipynb)
- .NET: [Agent Framework](./code_samples/04-dotnet-agent-framework.md)

## هل لديك المزيد من الأسئلة حول استخدام الأنماط التصميمية للأدوات؟

انضم إلى [Azure AI Foundry Discord](https://aka.ms/ai-agents/discord) للقاء متعلمين آخرين، وحضور ساعات العمل، والحصول على إجابات لأسئلتك حول وكلاء الذكاء الاصطناعي.

## موارد إضافية

- <a href="https://microsoft.github.io/build-your-first-agent-with-azure-ai-agent-service-workshop/" target="_blank">ورشة عمل خدمة وكلاء Azure AI</a>
- <a href="https://github.com/Azure-Samples/contoso-creative-writer/tree/main/docs/workshop" target="_blank">ورشة عمل Contoso Creative Writer متعددة الوكلاء</a>
- <a href="https://learn.microsoft.com/semantic-kernel/concepts/ai-services/chat-completion/function-calling/?pivots=programming-language-python#1-serializing-the-functions" target="_blank">دليل استدعاء الدوال في Semantic Kernel</a>
- <a href="https://github.com/microsoft/semantic-kernel/blob/main/python/samples/getting_started_with_agents/openai_assistant/step3_assistant_tool_code_interpreter.py" target="_blank">مفسر الأكواد في Semantic Kernel</a>
- <a href="https://microsoft.github.io/autogen/dev/user-guide/core-user-guide/components/tools.html" target="_blank">أدوات Autogen</a>

## الدرس السابق

[فهم أنماط التصميم الوكالية](../03-agentic-design-patterns/README.md)

## الدرس التالي

[Agentic RAG](../05-agentic-rag/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**إخلاء المسؤولية**:
تم ترجمة هذا المستند باستخدام خدمة الترجمة بالذكاء الاصطناعي [Co-op Translator](https://github.com/Azure/co-op-translator). بينما نسعى لتحقيق الدقة، يرجى العلم أن الترجمات الآلية قد تحتوي على أخطاء أو عدم دقة. يجب اعتبار المستند الأصلي بلغته الأصلية المصدر المعتمد. بالنسبة للمعلومات الحيوية، يُنصح بالاستعانة بالترجمة البشرية المهنية. نحن غير مسؤولين عن أي سوء فهم أو تفسيرات خاطئة ناتجة عن استخدام هذه الترجمة.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->