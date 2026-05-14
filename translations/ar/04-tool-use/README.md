[![كيفية تصميم وكلاء ذكاء اصطناعي جيدين](../../../translated_images/ar/lesson-4-thumbnail.546162853cb3daff.webp)](https://youtu.be/vieRiPRx-gI?si=cEZ8ApnT6Sus9rhn)

> _(انقر على الصورة أعلاه لمشاهدة فيديو هذا الدرس)_

# نمط تصميم استخدام الأدوات

الأدوات مثيرة للاهتمام لأنها تتيح لوكلاء الذكاء الاصطناعي مجموعة أوسع من القدرات. بدلاً من أن يكون لدى الوكيل مجموعة محدودة من الإجراءات التي يمكنه تنفيذها، من خلال إضافة أداة، يمكن للوكيل الآن تنفيذ مجموعة واسعة من الإجراءات. في هذا الفصل، سننظر في نمط تصميم استخدام الأدوات، الذي يصف كيف يمكن لوكلاء الذكاء الاصطناعي استخدام أدوات محددة لتحقيق أهدافهم.

## المقدمة

في هذا الدرس، نسعى للإجابة على الأسئلة التالية:

- ما هو نمط تصميم استخدام الأدوات؟
- ما هي حالات الاستخدام التي يمكن تطبيقه عليها؟
- ما هي العناصر/الكتل الأساسية اللازمة لتنفيذ نمط التصميم؟
- ما هي الاعتبارات الخاصة باستخدام نمط تصميم استخدام الأدوات لبناء وكلاء ذكاء اصطناعي موثوقين؟

## أهداف التعلم

بعد إكمال هذا الدرس، ستكون قادرًا على:

- تعريف نمط تصميم استخدام الأدوات وغرضه.
- تحديد حالات الاستخدام التي ينطبق عليها نمط تصميم استخدام الأدوات.
- فهم العناصر الرئيسية اللازمة لتنفيذ نمط التصميم.
- التعرف على الاعتبارات لضمان الموثوقية في وكلاء الذكاء الاصطناعي الذين يستخدمون هذا النمط.

## ما هو نمط تصميم استخدام الأدوات؟

يركز **نمط تصميم استخدام الأدوات** على إعطاء نماذج اللغة الكبيرة (LLMs) القدرة على التفاعل مع أدوات خارجية لتحقيق أهداف محددة. الأدوات هي كود يمكن تنفيذه بواسطة الوكيل لأداء إجراءات. يمكن أن تكون الأداة دالة بسيطة مثل الآلة الحاسبة، أو استدعاء API لخدمة طرف ثالث مثل البحث عن سعر الأسهم أو توقع الطقس. في سياق وكلاء الذكاء الاصطناعي، تم تصميم الأدوات ليتم تنفيذها من قبل الوكلاء استجابة لـ **نداءات الوظائف التي يولدها النموذج**.

## ما هي حالات الاستخدام التي يمكن تطبيقها عليها؟

يمكن لوكلاء الذكاء الاصطناعي الاستفادة من الأدوات لإكمال مهام معقدة، استرجاع المعلومات، أو اتخاذ القرارات. وغالبًا ما يُستخدم نمط تصميم استخدام الأدوات في السيناريوهات التي تتطلب تفاعلًا ديناميكيًا مع أنظمة خارجية، مثل قواعد البيانات، خدمات الويب، أو مفسري الأكواد. هذه القدرة مفيدة لعدد من حالات الاستخدام المختلفة بما في ذلك:

- **استرجاع المعلومات الديناميكي:** يمكن للوكلاء الاستعلام من خلال APIs خارجية أو قواعد بيانات لجلب بيانات محدثة (مثل استعلام قاعدة بيانات SQLite لتحليل البيانات، جلب أسعار الأسهم أو معلومات الطقس).
- **تنفيذ وتفسير الأكواد:** يمكن للوكلاء تنفيذ الأكواد أو السكريبتات لحل المشكلات الرياضية، توليد تقارير، أو إجراء محاكاة.
- **أتمتة سير العمل:** أتمتة سير العمل المتكرر أو متعدد الخطوات عن طريق دمج أدوات مثل جداول المهام، خدمات البريد الإلكتروني، أو خطوط بيانات.
- **دعم العملاء:** يمكن للوكلاء التفاعل مع أنظمة إدارة علاقات العملاء، منصات التذاكر، أو قواعد المعرفة لحل استفسارات المستخدمين.
- **توليد وتحرير المحتوى:** يمكن للوكلاء الاستفادة من أدوات مثل فاحصي القواعد اللغوية، ملخصات النصوص، أو مقيمي سلامة المحتوى للمساعدة في مهام إنشاء المحتوى.

## ما هي العناصر/الكتل الأساسية اللازمة لتنفيذ نمط تصميم استخدام الأدوات؟

تتيح هذه الكتل الأساسية لوكيل الذكاء الاصطناعي أداء مجموعة واسعة من المهام. لننظر إلى العناصر الأساسية اللازمة لتنفيذ نمط تصميم استخدام الأدوات:

- **مخططات الوظائف/الأدوات**: تعريفات مفصلة للأدوات المتاحة، بما في ذلك اسم الوظيفة، الغرض، المعاملات المطلوبة، والمخرجات المتوقعة. تمكّن هذه المخططات نموذج اللغة الكبير من فهم الأدوات المتاحة وكيفية بناء طلبات صالحة.

- **منطق تنفيذ الوظيفة**: يحكم كيف ومتى يتم استدعاء الأدوات بناءً على نية المستخدم وسياق المحادثة. قد تشمل وحدات تخطيط، آليات التوجيه، أو تدفقات شرطية تحدد استخدام الأداة ديناميكيًا.

- **نظام معالجة الرسائل**: مكونات تدير تدفق المحادثة بين مدخلات المستخدم، استجابات LLM، نداءات الأدوات، ومخرجات الأدوات.

- **إطار تكامل الأدوات**: البنية التحتية التي تربط الوكيل بمختلف الأدوات، سواء كانت دوال بسيطة أو خدمات خارجية معقدة.

- **التعامل مع الأخطاء والتحقق**: آليات للتعامل مع إخفاقات تنفيذ الأدوات، التحقق من المعاملات، وإدارة الاستجابات غير المتوقعة.

- **إدارة الحالة**: تتبع سياق المحادثة، التفاعلات السابقة مع الأدوات، والبيانات الدائمة لضمان الاتساق عبر التفاعلات متعددة الجولات.

بعد ذلك، دعونا ننظر إلى نداء الوظائف/الأدوات بمزيد من التفصيل.
 
### نداء الوظائف/الأدوات

نداء الوظائف هو الطريقة الأساسية التي تتيح لنماذج اللغة الكبيرة (LLMs) التفاعل مع الأدوات. سترى غالبًا استخدام "وظيفة" و"أداة" بالتبادل لأن "الوظائف" (كتل من الكود القابل لإعادة الاستخدام) هي "الأدوات" التي يستخدمها الوكلاء لأداء المهام. لكي يتم استدعاء كود الوظيفة، يجب على LLM مقارنة طلب المستخدم بوصف الوظائف. لهذا الغرض، يتم إرسال مخطط يحتوي على أوصاف جميع الوظائف المتاحة إلى LLM. ثم يختار LLM الوظيفة الأنسب للمهمة ويعيد اسمها وحججها. تُستدعى الوظيفة المختارة، ويرسل ردها مرة أخرى إلى LLM، الذي يستخدم المعلومات للرد على طلب المستخدم.

لتنفيذ نداء الوظائف لوكلاء الذكاء الاصطناعي، ستحتاج إلى:

1. نموذج LLM يدعم نداء الوظائف  
2. مخطط يحتوي على أوصاف الوظائف  
3. كود لكل وظيفة موصوفة  

لنستخدم مثال الحصول على الوقت الحالي في مدينة لتوضيح ذلك:

1. **تهيئة LLM يدعم نداء الوظائف:**

    ليست جميع النماذج تدعم نداء الوظائف، لذا من المهم التحقق من أن النموذج الذي تستخدمه يدعم ذلك. يدعم <a href="https://learn.microsoft.com/azure/ai-services/openai/how-to/function-calling" target="_blank">Azure OpenAI</a> نداء الوظائف. يمكننا البدء بإنشاء عميل Azure OpenAI.

    ```python
    # تهيئة عميل Azure OpenAI
    client = AzureOpenAI(
        azure_endpoint = os.getenv("AZURE_AI_PROJECT_ENDPOINT"), 
        api_key=os.getenv("AZURE_OPENAI_API_KEY"),  
        api_version="2024-05-01-preview"
    )
    ```

1. **إنشاء مخطط وظيفة:**

    بعد ذلك، سنعرّف مخطط JSON يحتوي على اسم الوظيفة، وصف ما تفعله الوظيفة، وأسماء وأوصاف المعاملات الخاصة بالوظيفة. ثم نأخذ هذا المخطط ونمرره إلى العميل الذي أنشأناه مسبقًا، مع طلب المستخدم للعثور على الوقت في سان فرانسيسكو. ما هو مهم أن نلاحظه هو أن **نداء الأداة** هو ما يتم إرجاعه، **وليس** الجواب النهائي للسؤال. كما ذكرنا سابقًا، يعيد LLM اسم الوظيفة التي اختارها للمهمة، والحجج التي سيتم تمريرها إليها.

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
  
    # رسالة المستخدم الأولية
    messages = [{"role": "user", "content": "What's the current time in San Francisco"}] 
  
    # المكالمة الأولى للواجهة البرمجية: اطلب من النموذج استخدام الوظيفة
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
  
1. **كود الوظيفة المطلوب لتنفيذ المهمة:**

    بعد أن يختار LLM الوظيفة التي يجب تشغيلها، يجب تنفيذ الكود الذي ينفذ المهمة.  
    يمكننا تنفيذ الكود للحصول على الوقت الحالي باستخدام بايثون. كما أننا بحاجة إلى كتابة كود لاستخراج الاسم والحجج من response_message للحصول على النتيجة النهائية.

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

يعد نداء الوظائف جوهر معظم، إن لم يكن كل، نمط تصميم استخدام أدوات الوكلاء، ومع ذلك فإن تنفيذه من الصفر يمكن أن يكون تحديًا أحيانًا. كما تعلمنا في [الدرس 2](../../../02-explore-agentic-frameworks) توفر أُطُر العمل الوكيلة كتل بناء جاهزة لتنفيذ استخدام الأدوات.
 
## أمثلة استخدام الأدوات مع أُطُر العمل الوكيلة

إليك بعض الأمثلة على كيفية تنفيذ نمط تصميم استخدام الأدوات باستخدام أُطُر العمل الوكيلة المختلفة:

### إطار عمل مايكروسوفت للوكلاء

<a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">إطار عمل مايكروسوفت للوكلاء</a> هو إطار عمل ذكاء اصطناعي مفتوح المصدر لبناء وكلاء ذكاء اصطناعي. يبسط عملية استخدام نداء الوظائف من خلال السماح لك بتعريف الأدوات كدوال بايثون باستخدام المزخرف `@tool`. يتولى الإطار التعامل مع التواصل ذهابًا وإيابًا بين النموذج وكودك. كما يوفر وصولًا إلى أدوات معرفة مسبقًا مثل بحث الملفات ومفسر الكود عبر `AzureAIProjectAgentProvider`.

يوضح الرسم البياني التالي عملية نداء الوظائف مع إطار عمل مايكروسوفت للوكلاء:

![نداء الوظائف](../../../translated_images/ar/functioncalling-diagram.a84006fc287f6014.webp)

في إطار عمل مايكروسوفت للوكلاء، تُعرّف الأدوات كدوال مزخرفة. يمكننا تحويل دالة `get_current_time` التي رأيناها سابقًا إلى أداة باستخدام المزخرف `@tool`. سيقوم الإطار تلقائيًا بتسلسل الوظيفة ومعاملاتها، وإنشاء المخطط لإرساله إلى LLM.

```python
from agent_framework import tool
from agent_framework.azure import AzureAIProjectAgentProvider
from azure.identity import AzureCliCredential

@tool
def get_current_time(location: str) -> str:
    """Get the current time for a given location"""
    ...

# إنشاء العميل
provider = AzureAIProjectAgentProvider(credential=AzureCliCredential())

# إنشاء وكيل وتشغيل الأداة معه
agent = await provider.create_agent(name="TimeAgent", instructions="Use available tools to answer questions.", tools=get_current_time)
response = await agent.run("What time is it?")
```
  
### خدمة وكيل الذكاء الاصطناعي من Azure

<a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">خدمة وكيل الذكاء الاصطناعي من Azure</a> هي إطار عمل وكيل أحدث مصمم لتمكين المطورين من بناء ونشر وتوسيع وكلاء ذكاء اصطناعي عالي الجودة وقابلين للتوسع بطريقة آمنة دون الحاجة لإدارة موارد الحوسبة والتخزين الأساسية. وهو مفيد بشكل خاص لتطبيقات المؤسسات لأنه خدمة مُدارة بالكامل مع أمان على مستوى المؤسسات.

عند المقارنة بالتطوير باستخدام LLM API مباشرة، توفر خدمة وكيل الذكاء الاصطناعي من Azure بعض الميزات، بما في ذلك:

- نداء الأدوات تلقائيًا – لا حاجة لتحليل نداء الأداة، استدعاء الأداة، والتعامل مع الاستجابة؛ يتم كل ذلك الآن على الخادم  
- إدارة البيانات بأمان – بدلاً من إدارة حالة المحادثة بنفسك، يمكنك الاعتماد على الخيوط (threads) لتخزين جميع المعلومات التي تحتاجها  
- أدوات جاهزة للاستخدام – أدوات يمكنك استخدامها للتفاعل مع مصادر بياناتك مثل Bing، Azure AI Search، و Azure Functions.

يمكن تقسيم الأدوات المتاحة في خدمة وكيل الذكاء الاصطناعي من Azure إلى فئتين:

1. أدوات المعرفة:  
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/bing-grounding?tabs=python&pivots=overview" target="_blank">التأسيس باستخدام بحث Bing</a>  
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/file-search?tabs=python&pivots=overview" target="_blank">بحث الملفات</a>  
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-ai-search?tabs=azurecli%2Cpython&pivots=overview-azure-ai-search" target="_blank">بحث Azure AI</a>

2. أدوات العمل:  
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/function-calling?tabs=python&pivots=overview" target="_blank">نداء الوظائف</a>  
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/code-interpreter?tabs=python&pivots=overview" target="_blank">مفسر الكود</a>  
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/openapi-spec?tabs=python&pivots=overview" target="_blank">أدوات معرفة بواسطة OpenAPI</a>  
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-functions?pivots=overview" target="_blank">وظائف Azure</a>

تتيح خدمة الوكيل لنا استخدام هذه الأدوات معًا كمجموعة أدوات (`toolset`). كما تستخدم الـ `threads` التي تتتبع تاريخ الرسائل من محادثة معينة.

تخيل أنك وكيل مبيعات في شركة تسمى Contoso. تريد تطوير وكيل محادثة يمكنه الإجابة على الأسئلة حول بيانات المبيعات الخاصة بك.

توضح الصورة التالية كيف يمكنك استخدام خدمة وكيل الذكاء الاصطناعي من Azure لتحليل بيانات مبيعاتك:

![خدمة الوكيل قيد التنفيذ](../../../translated_images/ar/agent-service-in-action.34fb465c9a84659e.webp)

لاستخدام أي من هذه الأدوات مع الخدمة يمكننا إنشاء عميل وتحديد أداة أو مجموعة أدوات. لتطبيق ذلك عمليًا يمكننا استخدام كود بايثون التالي. سيكون بإمكان LLM النظر إلى مجموعة الأدوات واتخاذ قرار سواء باستخدام الدالة التي أنشأها المستخدم، `fetch_sales_data_using_sqlite_query`، أو مفسر الكود المدمج اعتمادًا على طلب المستخدم.

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

# تهيئة وكيل استدعاء الدوال مع دالة fetch_sales_data_using_sqlite_query وإضافتها إلى مجموعة الأدوات
fetch_data_function = FunctionTool(fetch_sales_data_using_sqlite_query)
toolset.add(fetch_data_function)

# تهيئة أداة مفسر الأكواد وإضافتها إلى مجموعة الأدوات.
code_interpreter = CodeInterpreterTool()toolset.add(code_interpreter)

agent = project_client.agents.create_agent(
    model="gpt-4o-mini", name="my-agent", instructions="You are helpful agent", 
    toolset=toolset
)
```

## ما هي الاعتبارات الخاصة باستخدام نمط تصميم استخدام الأدوات لبناء وكلاء ذكاء اصطناعي موثوقين؟

أحد المخاوف الشائعة مع SQL المولد ديناميكيًا بواسطة LLMs هو الأمان، خصوصًا خطر حقن SQL أو الأفعال الخبيثة، مثل حذف أو العبث بقاعدة البيانات. بينما هذه المخاوف صحيحة، يمكن التخفيف منها بشكل فعّال من خلال تكوين أذونات الوصول لقاعدة البيانات بشكل ملائم. بالنسبة لمعظم قواعد البيانات، يتطلب هذا تكوين قاعدة البيانات كـ "قراءة فقط". بالنسبة لخدمات قواعد البيانات مثل PostgreSQL أو Azure SQL، يجب تعيين دور التطبيق كقراءة فقط (SELECT).

تشغيل التطبيق في بيئة آمنة يعزز الحماية بشكل أكبر. في سيناريوهات المؤسسات، عادةً ما يتم استخراج وتحويل البيانات من الأنظمة التشغيلية إلى قاعدة بيانات قراءة فقط أو مستودع بيانات مع مخطط سهل الاستخدام. يضمن هذا الأسلوب أن البيانات آمنة، ومحسّنة للأداء وسهولة الوصول، وأن التطبيق يملك وصولاً محدودًا للقراءة فقط.

## أمثلة رموز

- بايثون: [إطار العمل الوكيلي](./code_samples/04-python-agent-framework.ipynb)
- .NET: [إطار العمل الوكيلي](./code_samples/04-dotnet-agent-framework.md)

## هل لديك المزيد من الأسئلة حول نمط تصميم استخدام الأدوات؟

انضم إلى [خادم Microsoft Foundry على Discord](https://aka.ms/ai-agents/discord) لتلتقي مع متعلمين آخرين، تحضر ساعات العمل، وتحصل على إجابات لأسئلتك حول وكلاء الذكاء الاصطناعي.

## موارد إضافية

- <a href="https://microsoft.github.io/build-your-first-agent-with-azure-ai-agent-service-workshop/" target="_blank">ورشة عمل خدمة وكلاء الذكاء الاصطناعي من Azure</a>
- <a href="https://github.com/Azure-Samples/contoso-creative-writer/tree/main/docs/workshop" target="_blank">ورشة عمل Contoso Creative Writer متعددة الوكلاء</a>
- <a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">نظرة عامة على إطار عمل مايكروسوفت للوكلاء</a>

## الدرس السابق

[فهم أنماط تصميم الوكلاء](../03-agentic-design-patterns/README.md)

## الدرس التالي
[الاسترجاع الوكيل](../05-agentic-rag/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**تنويه**:
تمت ترجمة هذا المستند باستخدام خدمة الترجمة بالذكاء الاصطناعي [Co-op Translator](https://github.com/Azure/co-op-translator). بينما نسعى للدقة، يرجى العلم أن الترجمات الآلية قد تحتوي على أخطاء أو عدم دقة. يجب اعتبار المستند الأصلي بلغته الأصلية المصدر الرسمي والمعتمد. للمعلومات الهامة، يُنصح بالاستعانة بترجمة بشرية محترفة. نحن غير مسؤولين عن أي سوء فهم أو تفسير ناتج عن استخدام هذه الترجمة.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->