<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "e056335d729ba6e49571db7a6533825d",
  "translation_date": "2025-09-30T06:20:00+00:00",
  "source_file": "04-tool-use/README.md",
  "language_code": "ar"
}
-->
[![كيفية تصميم وكلاء ذكاء اصطناعي جيدين](../../../translated_images/lesson-4-thumbnail.546162853cb3daffd64edd92014f274103f76360dfb39fc6e6ee399494da38fd.ar.png)](https://youtu.be/vieRiPRx-gI?si=cEZ8ApnT6Sus9rhn)

> _(انقر على الصورة أعلاه لمشاهدة فيديو الدرس)_

# نمط تصميم استخدام الأدوات

الأدوات مثيرة للاهتمام لأنها تتيح لوكلاء الذكاء الاصطناعي امتلاك مجموعة أوسع من القدرات. بدلاً من أن يكون لدى الوكيل مجموعة محدودة من الإجراءات التي يمكنه تنفيذها، يمكنه الآن، بإضافة أداة، تنفيذ مجموعة واسعة من الإجراءات. في هذا الفصل، سنلقي نظرة على نمط تصميم استخدام الأدوات، الذي يصف كيفية استخدام وكلاء الذكاء الاصطناعي لأدوات محددة لتحقيق أهدافهم.

## المقدمة

في هذا الدرس، نسعى للإجابة على الأسئلة التالية:

- ما هو نمط تصميم استخدام الأدوات؟
- ما هي حالات الاستخدام التي يمكن تطبيقه عليها؟
- ما هي العناصر/الأسس اللازمة لتنفيذ نمط التصميم؟
- ما هي الاعتبارات الخاصة باستخدام نمط تصميم استخدام الأدوات لبناء وكلاء ذكاء اصطناعي موثوقين؟

## أهداف التعلم

بعد إكمال هذا الدرس، ستكون قادرًا على:

- تعريف نمط تصميم استخدام الأدوات والغرض منه.
- تحديد حالات الاستخدام التي يكون نمط تصميم استخدام الأدوات قابلاً للتطبيق عليها.
- فهم العناصر الأساسية اللازمة لتنفيذ نمط التصميم.
- التعرف على الاعتبارات لضمان موثوقية وكلاء الذكاء الاصطناعي باستخدام هذا النمط.

## ما هو نمط تصميم استخدام الأدوات؟

يركز **نمط تصميم استخدام الأدوات** على منح نماذج اللغة الكبيرة (LLMs) القدرة على التفاعل مع أدوات خارجية لتحقيق أهداف محددة. الأدوات هي أكواد يمكن تنفيذها بواسطة الوكيل لأداء إجراءات. يمكن أن تكون الأداة وظيفة بسيطة مثل آلة حاسبة، أو استدعاء API لخدمة طرف ثالث مثل البحث عن أسعار الأسهم أو توقعات الطقس. في سياق وكلاء الذكاء الاصطناعي، يتم تصميم الأدوات ليتم تنفيذها بواسطة الوكلاء استجابةً لـ **استدعاءات الوظائف التي يتم إنشاؤها بواسطة النموذج**.

## ما هي حالات الاستخدام التي يمكن تطبيقها عليها؟

يمكن لوكلاء الذكاء الاصطناعي الاستفادة من الأدوات لإكمال المهام المعقدة، استرجاع المعلومات، أو اتخاذ القرارات. يتم استخدام نمط تصميم استخدام الأدوات غالبًا في السيناريوهات التي تتطلب تفاعلًا ديناميكيًا مع أنظمة خارجية، مثل قواعد البيانات، خدمات الويب، أو مفسرات الأكواد. هذه القدرة مفيدة لعدد من حالات الاستخدام المختلفة بما في ذلك:

- **استرجاع المعلومات الديناميكي:** يمكن للوكلاء استعلام واجهات برمجة التطبيقات الخارجية أو قواعد البيانات لجلب بيانات محدثة (مثل استعلام قاعدة بيانات SQLite لتحليل البيانات، جلب أسعار الأسهم أو معلومات الطقس).
- **تنفيذ الأكواد وتفسيرها:** يمكن للوكلاء تنفيذ الأكواد أو النصوص البرمجية لحل المشكلات الرياضية، إنشاء تقارير، أو إجراء محاكاة.
- **أتمتة سير العمل:** أتمتة المهام المتكررة أو متعددة الخطوات من خلال دمج أدوات مثل جداول المهام، خدمات البريد الإلكتروني، أو خطوط البيانات.
- **دعم العملاء:** يمكن للوكلاء التفاعل مع أنظمة إدارة علاقات العملاء (CRM)، منصات التذاكر، أو قواعد المعرفة لحل استفسارات المستخدمين.
- **إنشاء المحتوى وتحريره:** يمكن للوكلاء الاستفادة من أدوات مثل مدققي القواعد، ملخصات النصوص، أو مقيمات سلامة المحتوى للمساعدة في مهام إنشاء المحتوى.

## ما هي العناصر/الأسس اللازمة لتنفيذ نمط تصميم استخدام الأدوات؟

تتيح هذه الأسس لوكيل الذكاء الاصطناعي أداء مجموعة واسعة من المهام. دعونا نلقي نظرة على العناصر الأساسية اللازمة لتنفيذ نمط تصميم استخدام الأدوات:

- **مخططات الوظائف/الأدوات:** تعريفات مفصلة للأدوات المتاحة، بما في ذلك اسم الوظيفة، الغرض، المعلمات المطلوبة، والمخرجات المتوقعة. تُمكّن هذه المخططات النموذج من فهم الأدوات المتاحة وكيفية إنشاء طلبات صالحة.
- **منطق تنفيذ الوظائف:** يحكم كيفية ومتى يتم استدعاء الأدوات بناءً على نية المستخدم وسياق المحادثة. قد يشمل ذلك وحدات التخطيط، آليات التوجيه، أو التدفقات الشرطية التي تحدد استخدام الأدوات ديناميكيًا.
- **نظام إدارة الرسائل:** مكونات تدير تدفق المحادثة بين مدخلات المستخدم، استجابات النموذج، استدعاءات الأدوات، ومخرجات الأدوات.
- **إطار تكامل الأدوات:** بنية تحتية تربط الوكيل بمختلف الأدوات، سواء كانت وظائف بسيطة أو خدمات خارجية معقدة.
- **معالجة الأخطاء والتحقق:** آليات لمعالجة الفشل في تنفيذ الأدوات، التحقق من المعلمات، وإدارة الاستجابات غير المتوقعة.
- **إدارة الحالة:** تتبع سياق المحادثة، التفاعلات السابقة مع الأدوات، والبيانات المستمرة لضمان الاتساق عبر التفاعلات متعددة الأدوار.

بعد ذلك، دعونا نلقي نظرة على استدعاء الوظائف/الأدوات بمزيد من التفصيل.

### استدعاء الوظائف/الأدوات

استدعاء الوظائف هو الطريقة الأساسية التي نُمكّن بها نماذج اللغة الكبيرة (LLMs) للتفاعل مع الأدوات. غالبًا ما ترى استخدام "الوظائف" و"الأدوات" بالتبادل لأن "الوظائف" (كتل من الأكواد القابلة لإعادة الاستخدام) هي "الأدوات" التي يستخدمها الوكلاء لتنفيذ المهام. لكي يتم استدعاء كود الوظيفة، يجب أن يقارن النموذج طلب المستخدم بوصف الوظيفة. يتم إرسال مخطط يحتوي على أوصاف جميع الوظائف المتاحة إلى النموذج. ثم يختار النموذج الوظيفة الأنسب للمهمة ويعيد اسمها ومعاملاتها. يتم استدعاء الوظيفة المختارة، ويتم إرسال استجابتها مرة أخرى إلى النموذج، الذي يستخدم المعلومات للرد على طلب المستخدم.

لتنفيذ استدعاء الوظائف للوكلاء، يحتاج المطورون إلى:

1. نموذج LLM يدعم استدعاء الوظائف
2. مخطط يحتوي على أوصاف الوظائف
3. الكود الخاص بكل وظيفة موصوفة

دعونا نستخدم مثال الحصول على الوقت الحالي في مدينة لتوضيح:

1. **تهيئة نموذج LLM يدعم استدعاء الوظائف:**

    ليس كل النماذج تدعم استدعاء الوظائف، لذا من المهم التحقق من أن النموذج الذي تستخدمه يدعم ذلك. <a href="https://learn.microsoft.com/azure/ai-services/openai/how-to/function-calling" target="_blank">Azure OpenAI</a> يدعم استدعاء الوظائف. يمكننا البدء بتهيئة عميل Azure OpenAI.

    ```python
    # Initialize the Azure OpenAI client
    client = AzureOpenAI(
        azure_endpoint = os.getenv("AZURE_OPENAI_ENDPOINT"), 
        api_key=os.getenv("AZURE_OPENAI_API_KEY"),  
        api_version="2024-05-01-preview"
    )
    ```

1. **إنشاء مخطط وظيفة:**

    بعد ذلك، سنقوم بتعريف مخطط JSON يحتوي على اسم الوظيفة، وصف لما تقوم به الوظيفة، وأسماء وأوصاف معلمات الوظيفة. ثم سنأخذ هذا المخطط ونمرره إلى العميل الذي تم إنشاؤه سابقًا، مع طلب المستخدم للعثور على الوقت في سان فرانسيسكو. من المهم ملاحظة أن ما يتم إرجاعه هو **استدعاء أداة**، وليس الإجابة النهائية على السؤال. كما ذكرنا سابقًا، يعيد النموذج اسم الوظيفة التي اختارها للمهمة، والمعاملات التي سيتم تمريرها إليها.

    ```python
    # Function description for the model to read
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
  
    # Initial user message
    messages = [{"role": "user", "content": "What's the current time in San Francisco"}] 
  
    # First API call: Ask the model to use the function
      response = client.chat.completions.create(
          model=deployment_name,
          messages=messages,
          tools=tools,
          tool_choice="auto",
      )
  
      # Process the model's response
      response_message = response.choices[0].message
      messages.append(response_message)
  
      print("Model's response:")  

      print(response_message)
  
    ```

    ```bash
    Model's response:
    ChatCompletionMessage(content=None, role='assistant', function_call=None, tool_calls=[ChatCompletionMessageToolCall(id='call_pOsKdUlqvdyttYB67MOj434b', function=Function(arguments='{"location":"San Francisco"}', name='get_current_time'), type='function')])
    ```
  
1. **الكود المطلوب لتنفيذ المهمة:**

    الآن بعد أن اختار النموذج الوظيفة التي تحتاج إلى التنفيذ، يجب تنفيذ الكود الذي يقوم بالمهمة. يمكننا تنفيذ الكود للحصول على الوقت الحالي باستخدام Python. سنحتاج أيضًا إلى كتابة الكود لاستخراج الاسم والمعاملات من response_message للحصول على النتيجة النهائية.

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
     # Handle function calls
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
  
      # Second API call: Get the final response from the model
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

استدعاء الوظائف هو جوهر معظم، إن لم يكن كل، تصميم استخدام الأدوات للوكلاء، ومع ذلك فإن تنفيذه من الصفر يمكن أن يكون أحيانًا تحديًا. كما تعلمنا في [الدرس 2](../../../02-explore-agentic-frameworks) توفر لنا الأطر الوكيلية كتل بناء مسبقة لتنفيذ استخدام الأدوات.

## أمثلة على استخدام الأدوات مع الأطر الوكيلية

فيما يلي بعض الأمثلة على كيفية تنفيذ نمط تصميم استخدام الأدوات باستخدام أطر وكيلية مختلفة:

### Semantic Kernel

<a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Semantic Kernel</a> هو إطار عمل مفتوح المصدر للذكاء الاصطناعي لمطوري .NET، Python، وJava الذين يعملون مع نماذج اللغة الكبيرة (LLMs). يُبسط عملية استخدام استدعاء الوظائف من خلال وصف وظائفك ومعاملاتها تلقائيًا للنموذج عبر عملية تُسمى <a href="https://learn.microsoft.com/semantic-kernel/concepts/ai-services/chat-completion/function-calling/?pivots=programming-language-python#1-serializing-the-functions" target="_blank">التسلسل</a>. كما يتولى التعامل مع التواصل ذهابًا وإيابًا بين النموذج وكودك. ميزة أخرى لاستخدام إطار وكيل مثل Semantic Kernel هي أنه يتيح لك الوصول إلى أدوات مسبقة البناء مثل <a href="https://github.com/microsoft/semantic-kernel/blob/main/python/samples/getting_started_with_agents/openai_assistant/step4_assistant_tool_file_search.py" target="_blank">البحث عن الملفات</a> و<a href="https://github.com/microsoft/semantic-kernel/blob/main/python/samples/getting_started_with_agents/openai_assistant/step3_assistant_tool_code_interpreter.py" target="_blank">مفسر الأكواد</a>.

يوضح الرسم البياني التالي عملية استدعاء الوظائف باستخدام Semantic Kernel:

![استدعاء الوظائف](../../../translated_images/functioncalling-diagram.a84006fc287f60140cc0a484ff399acd25f69553ea05186981ac4d5155f9c2f6.ar.png)

في Semantic Kernel تُسمى الوظائف/الأدوات <a href="https://learn.microsoft.com/semantic-kernel/concepts/plugins/?pivots=programming-language-python" target="_blank">الإضافات</a>. يمكننا تحويل وظيفة `get_current_time` التي رأيناها سابقًا إلى إضافة عن طريق تحويلها إلى فئة تحتوي على الوظيفة. يمكننا أيضًا استيراد الزخرفة `kernel_function`، التي تأخذ وصف الوظيفة. عندما تقوم بعد ذلك بإنشاء نواة مع GetCurrentTimePlugin، ستقوم النواة تلقائيًا بتسلسل الوظيفة ومعاملاتها، مما يُنشئ المخطط لإرساله إلى النموذج في العملية.

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

# Create the kernel
kernel = Kernel()

# Create the plugin
get_current_time_plugin = GetCurrentTimePlugin(location)

# Add the plugin to the kernel
kernel.add_plugin(get_current_time_plugin)
```
  
### خدمة Azure AI Agent

<a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">خدمة Azure AI Agent</a> هي إطار وكيل جديد مصمم لتمكين المطورين من بناء، نشر، وتوسيع وكلاء ذكاء اصطناعي عالي الجودة وقابل للتوسيع بأمان دون الحاجة إلى إدارة موارد الحوسبة والتخزين الأساسية. إنها مفيدة بشكل خاص للتطبيقات المؤسسية لأنها خدمة مُدارة بالكامل مع أمان على مستوى المؤسسات.

عند مقارنتها بالتطوير باستخدام واجهة برمجة تطبيقات LLM مباشرةً، توفر خدمة Azure AI Agent بعض المزايا، بما في ذلك:

- استدعاء الأدوات تلقائيًا – لا حاجة لتحليل استدعاء الأداة، تنفيذ الأداة، ومعالجة الاستجابة؛ يتم الآن تنفيذ كل هذا على الخادم.
- إدارة البيانات بأمان – بدلاً من إدارة حالة المحادثة الخاصة بك، يمكنك الاعتماد على المواضيع لتخزين جميع المعلومات التي تحتاجها.
- أدوات جاهزة للاستخدام – أدوات يمكنك استخدامها للتفاعل مع مصادر بياناتك، مثل Bing، Azure AI Search، وAzure Functions.

يمكن تقسيم الأدوات المتاحة في خدمة Azure AI Agent إلى فئتين:

1. أدوات المعرفة:
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/bing-grounding?tabs=python&pivots=overview" target="_blank">التأريض باستخدام بحث Bing</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/file-search?tabs=python&pivots=overview" target="_blank">البحث عن الملفات</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-ai-search?tabs=azurecli%2Cpython&pivots=overview-azure-ai-search" target="_blank">بحث Azure AI</a>

2. أدوات الإجراءات:
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/function-calling?tabs=python&pivots=overview" target="_blank">استدعاء الوظائف</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/code-interpreter?tabs=python&pivots=overview" target="_blank">مفسر الأكواد</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/openapi-spec?tabs=python&pivots=overview" target="_blank">أدوات محددة بواسطة OpenAPI</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-functions?pivots=overview" target="_blank">وظائف Azure</a>

تتيح خدمة الوكيل استخدام هذه الأدوات معًا كـ `toolset`. كما أنها تستخدم `threads` التي تتبع تاريخ الرسائل من محادثة معينة.

تخيل أنك وكيل مبيعات في شركة تدعى Contoso. تريد تطوير وكيل محادثة يمكنه الإجابة على الأسئلة حول بيانات مبيعاتك.

توضح الصورة التالية كيف يمكنك استخدام خدمة Azure AI Agent لتحليل بيانات مبيعاتك:

![خدمة الوكيل قيد العمل](../../../translated_images/agent-service-in-action.34fb465c9a84659edd3003f8cb62d6b366b310a09b37c44e32535021fbb5c93f.ar.jpg)

لاستخدام أي من هذه الأدوات مع الخدمة، يمكننا إنشاء عميل وتعريف أداة أو مجموعة أدوات. لتنفيذ ذلك عمليًا، يمكننا استخدام الكود التالي بلغة Python. سيتمكن النموذج من النظر إلى مجموعة الأدوات واتخاذ قرار باستخدام الوظيفة التي أنشأها المستخدم، `fetch_sales_data_using_sqlite_query`، أو مفسر الأكواد الجاهز بناءً على طلب المستخدم.

```python 
import os
from azure.ai.projects import AIProjectClient
from azure.identity import DefaultAzureCredential
from fetch_sales_data_functions import fetch_sales_data_using_sqlite_query # fetch_sales_data_using_sqlite_query function which can be found in a fetch_sales_data_functions.py file.
from azure.ai.projects.models import ToolSet, FunctionTool, CodeInterpreterTool

project_client = AIProjectClient.from_connection_string(
    credential=DefaultAzureCredential(),
    conn_str=os.environ["PROJECT_CONNECTION_STRING"],
)

# Initialize function calling agent with the fetch_sales_data_using_sqlite_query function and adding it to the toolset
fetch_data_function = FunctionTool(fetch_sales_data_using_sqlite_query)
toolset = ToolSet()
toolset.add(fetch_data_function)

# Initialize Code Interpreter tool and adding it to the toolset. 
code_interpreter = code_interpreter = CodeInterpreterTool()
toolset = ToolSet()
toolset.add(code_interpreter)

agent = project_client.agents.create_agent(
    model="gpt-4o-mini", name="my-agent", instructions="You are helpful agent", 
    toolset=toolset
)
```

## ما هي الاعتبارات الخاصة باستخدام نمط تصميم استخدام الأدوات لبناء وكلاء ذكاء اصطناعي موثوقين؟

مخاوف شائعة مع SQL الذي يتم إنشاؤه ديناميكيًا بواسطة نماذج اللغة الكبيرة (LLMs) هي الأمان، خصوصًا خطر حقن SQL أو الإجراءات الضارة، مثل حذف أو العبث بقاعدة البيانات. بينما هذه المخاوف صحيحة، يمكن التخفيف منها بشكل فعال من خلال تكوين أذونات الوصول إلى قاعدة البيانات بشكل صحيح. بالنسبة لمعظم قواعد البيانات، يتضمن ذلك تكوين قاعدة البيانات كقراءة فقط. بالنسبة لخدمات قواعد البيانات مثل PostgreSQL أو Azure SQL، يجب تعيين التطبيق دور قراءة فقط (SELECT).
تشغيل التطبيق في بيئة آمنة يعزز الحماية بشكل أكبر. في سيناريوهات المؤسسات، يتم عادةً استخراج البيانات وتحويلها من الأنظمة التشغيلية إلى قاعدة بيانات للقراءة فقط أو مستودع بيانات مع مخطط سهل الاستخدام. يضمن هذا النهج أن تكون البيانات آمنة، محسّنة للأداء وسهولة الوصول، وأن يكون للتطبيق وصول محدود للقراءة فقط.

### هل لديك المزيد من الأسئلة حول أنماط تصميم استخدام الأدوات؟

انضم إلى [مجتمع Azure AI Foundry على Discord](https://aka.ms/ai-agents/discord) للتواصل مع متعلمين آخرين، حضور ساعات الاستفسار، والحصول على إجابات لأسئلتك حول وكلاء الذكاء الاصطناعي.

## موارد إضافية

- <a href="https://microsoft.github.io/build-your-first-agent-with-azure-ai-agent-service-workshop/" target="_blank">ورشة عمل خدمة Azure AI Agents</a>
- <a href="https://github.com/Azure-Samples/contoso-creative-writer/tree/main/docs/workshop" target="_blank">ورشة عمل Contoso Creative Writer متعددة الوكلاء</a>
- <a href="https://learn.microsoft.com/semantic-kernel/concepts/ai-services/chat-completion/function-calling/?pivots=programming-language-python#1-serializing-the-functions" target="_blank">دليل استخدام استدعاء الوظائف في Semantic Kernel</a>
- <a href="https://github.com/microsoft/semantic-kernel/blob/main/python/samples/getting_started_with_agents/openai_assistant/step3_assistant_tool_code_interpreter.py" target="_blank">مفسر الكود في Semantic Kernel</a>
- <a href="https://microsoft.github.io/autogen/dev/user-guide/core-user-guide/components/tools.html" target="_blank">أدوات Autogen</a>

## الدرس السابق

[فهم أنماط التصميم الوكيلية](../03-agentic-design-patterns/README.md)

## الدرس التالي

[Agentic RAG](../05-agentic-rag/README.md)

---

**إخلاء المسؤولية**:  
تم ترجمة هذا المستند باستخدام خدمة الترجمة بالذكاء الاصطناعي [Co-op Translator](https://github.com/Azure/co-op-translator). بينما نسعى لتحقيق الدقة، يرجى العلم أن الترجمات الآلية قد تحتوي على أخطاء أو عدم دقة. يجب اعتبار المستند الأصلي بلغته الأصلية المصدر الموثوق. للحصول على معلومات حاسمة، يُوصى بالترجمة البشرية الاحترافية. نحن غير مسؤولين عن أي سوء فهم أو تفسيرات خاطئة تنشأ عن استخدام هذه الترجمة.