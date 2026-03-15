[![كيفية تصميم وكلاء ذكاء اصطناعي جيدين](../../../translated_images/ar/lesson-4-thumbnail.546162853cb3daff.webp)](https://youtu.be/vieRiPRx-gI?si=cEZ8ApnT6Sus9rhn)

> _(انقر على الصورة أعلاه لمشاهدة فيديو هذا الدرس)_

# نمط تصميم استخدام الأدوات

الأدوات مثيرة للاهتمام لأنها تتيح لوكلاء الذكاء الاصطناعي مجموعة أوسع من القدرات. بدلاً من أن يمتلك الوكيل مجموعة محدودة من الإجراءات التي يمكنه تنفيذها، يمكن للوكيل الآن أداء مجموعة واسعة من الإجراءات من خلال إضافة أداة. في هذا الفصل، سننظر إلى نمط تصميم استخدام الأدوات، الذي يصف كيف يمكن لوكلاء الذكاء الاصطناعي استخدام أدوات محددة لتحقيق أهدافهم.

## المقدمة

في هذا الدرس، نهدف إلى الإجابة على الأسئلة التالية:

- ما هو نمط تصميم استخدام الأدوات؟
- ما هي حالات الاستخدام التي يمكن تطبيقه عليها؟
- ما هي العناصر/الكتل الأساسية اللازمة لتطبيق نمط التصميم؟
- ما هي الاعتبارات الخاصة لاستخدام نمط تصميم استخدام الأدوات لبناء وكلاء ذكاء اصطناعي موثوقين؟

## أهداف التعلم

عند إكمال هذا الدرس، ستكون قادرًا على:

- تعريف نمط تصميم استخدام الأدوات وهدفه.
- تحديد حالات الاستخدام التي ينطبق عليها نمط تصميم استخدام الأدوات.
- فهم العناصر الرئيسية اللازمة لتطبيق نمط التصميم.
- التعرف على الاعتبارات لضمان الموثوقية في وكلاء الذكاء الاصطناعي الذين يستخدمون هذا النمط التصميمي.

## ما هو نمط تصميم استخدام الأدوات؟

يركز **نمط تصميم استخدام الأدوات** على منح نماذج اللغة الكبيرة (LLMs) القدرة على التفاعل مع أدوات خارجية لتحقيق أهداف محددة. الأدوات هي تعليمات برمجية يمكن تنفيذها بواسطة وكيل لأداء إجراءات. يمكن أن تكون الأداة دالة بسيطة مثل الآلة الحاسبة، أو استدعاء API لخدمة طرف ثالث مثل البحث عن أسعار الأسهم أو التنبؤ بالطقس. في سياق وكلاء الذكاء الاصطناعي، تم تصميم الأدوات لتُنفّذ بواسطة الوكلاء استجابةً لـ **مكالمات دوال مولدة عن طريق النموذج**.

## ما هي حالات الاستخدام التي يمكن تطبيقه عليها؟

يمكن لوكلاء الذكاء الاصطناعي الاستفادة من الأدوات لإكمال مهام معقدة، استرجاع المعلومات، أو اتخاذ القرارات. غالبًا ما يُستخدم نمط تصميم استخدام الأدوات في السيناريوهات التي تتطلب تفاعلًا ديناميكيًا مع الأنظمة الخارجية، مثل قواعد البيانات، خدمات الويب، أو مفسري الشفرات. هذه القدرة مفيدة لعدد من حالات الاستخدام المختلفة بما في ذلك:

- **استرجاع المعلومات الديناميكي:** يمكن للوكلاء الاستعلام من خلال واجهات برمجة تطبيقات خارجية أو قواعد بيانات لجلب بيانات محدثة (مثل الاستعلام من قاعدة بيانات SQLite لتحليل البيانات، جلب أسعار الأسهم أو معلومات الطقس).
- **تنفيذ الشفرات وتفسيرها:** يمكن للوكلاء تنفيذ الشفرات أو السكريبتات لحل المشكلات الرياضية، توليد التقارير، أو أداء المحاكاة.
- **أتمتة سير العمل:** أتمتة مهام متكررة أو متعددة الخطوات بدمج أدوات مثل مجدولي المهام، خدمات البريد الإلكتروني، أو خطوط أنابيب البيانات.
- **دعم العملاء:** يمكن للوكلاء التفاعل مع أنظمة إدارة علاقات العملاء، منصات التذاكر، أو قواعد المعرفة لحل استفسارات المستخدمين.
- **إنشاء وتحرير المحتوى:** يمكن للوكلاء الاستفادة من أدوات مثل مدققي القواعد اللغوية، ملخصات النصوص، أو أدوات تقييم سلامة المحتوى للمساعدة في مهام إنشاء المحتوى.

## ما هي العناصر/الكتل الأساسية اللازمة لتطبيق نمط تصميم استخدام الأدوات؟

تسمح هذه الكتل الأساسية لوكيل الذكاء الاصطناعي بأداء مجموعة واسعة من المهام. دعونا نلقي نظرة على العناصر الرئيسية اللازمة لتطبيق نمط تصميم استخدام الأدوات:

- **مخططات الدوال/الأدوات**: تعريفات مفصلة للأدوات المتاحة، بما في ذلك اسم الدالة، الغرض منها، المعلمات المطلوبة، والمخرجات المتوقعة. تتيح هذه المخططات للنموذج فهم الأدوات المتاحة وكيفية إنشاء طلبات صالحة.

- **منطق تنفيذ الدوال**: ينظم كيفية ووقت استدعاء الأدوات بناءً على نية المستخدم وسياق المحادثة. قد يشمل ذلك وحدات تخطيطية، آليات توجيه، أو تدفقات شرطية تحدد استخدام الأدوات بشكل ديناميكي.

- **نظام إدارة الرسائل**: مكونات تدير تدفق المحادثة بين مدخلات المستخدم، ردود النموذج، استدعاءات الأدوات، ومخرجات الأدوات.

- **إطار تكامل الأدوات**: البنية التحتية التي تربط الوكيل بالأدوات المختلفة، سواء كانت دوال بسيطة أو خدمات خارجية معقدة.

- **معالجة الأخطاء والتحقق**: آليات للتعامل مع فشل تنفيذ الأدوات، التحقق من المعلمات، وإدارة الاستجابات غير المتوقعة.

- **إدارة الحالة**: تتبع سياق المحادثة، التفاعلات السابقة مع الأدوات، والبيانات المستمرة لضمان الاتساق عبر التفاعلات متعددة الأدوار.

بعد ذلك، دعونا نلقي نظرة على استدعاء الدوال/الأدوات بمزيد من التفصيل.
 
### استدعاء الدوال/الأدوات

يُعد استدعاء الدوال الطريقة الأساسية التي نُمكّن من خلالها نماذج اللغة الكبيرة (LLMs) من التفاعل مع الأدوات. غالبًا ما ترى 'الدالة' و'الأداة' يُستخدمان بالتبادل لأن 'الدوال' (وحدات التعليمات البرمجية المعاد استخدامها) هي 'الأدوات' التي يستخدمها الوكلاء لأداء المهام. لكي يتم استدعاء رمز دالة، يجب على النموذج مقارنة طلب المستخدم بوصف الدوال. للقيام بذلك، يتم إرسال مخطط يحتوي على أوصاف جميع الدوال المتاحة إلى النموذج. ثم يختار النموذج الدالة الأنسب للمهمة ويُرجع اسمها والمعاملات الخاصة بها. يتم استدعاء الدالة المحددة، وتُرسل استجاباتها مرة أخرى إلى النموذج، الذي يستخدم المعلومات للرد على طلب المستخدم.

لكي يتمكن المطورون من تنفيذ استدعاء الدوال للوكلاء، سيحتاجون إلى:

1. نموذج LLM يدعم استدعاء الدوال
2. مخطط يحتوي على أوصاف الدوال
3. كود لكل دالة موصوفة

دعونا نستخدم مثال الحصول على الوقت الحالي في مدينة لتوضيح ذلك:

1. **تهيئة نموذج LLM يدعم استدعاء الدوال:**

    ليست كل النماذج تدعم استدعاء الدوال، لذا من المهم التحقق من دعم النموذج لذلك. يدعم <a href="https://learn.microsoft.com/azure/ai-services/openai/how-to/function-calling" target="_blank">Azure OpenAI</a> استدعاء الدوال. يمكننا البدء بتهيئة عميل Azure OpenAI.

    ```python
    # تهيئة عميل Azure OpenAI
    client = AzureOpenAI(
        azure_endpoint = os.getenv("AZURE_AI_PROJECT_ENDPOINT"), 
        api_key=os.getenv("AZURE_OPENAI_API_KEY"),  
        api_version="2024-05-01-preview"
    )
    ```

1. **إنشاء مخطط دالة:**

    بعد ذلك سنعرف مخطط JSON يحتوي على اسم الدالة، وصف لما تقوم به الدالة، وأسماء ووصف معاملات الدالة. 
    ثم نأخذ هذا المخطط ونرسله إلى العميل الذي أنشأناه سابقًا، مع طلب المستخدم للعثور على الوقت في سان فرانسيسكو. من المهم ملاحظة أن **مكالمة الأداة** هي ما يتم إرجاعه، **وليس** الجواب النهائي على السؤال. كما ذكرنا سابقًا، النموذج يُرجع اسم الدالة التي اختارها للمهمة والمعاملات التي سيتم تمريرها إليها.

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
  
    # أول استدعاء للواجهة البرمجية: اطلب من النموذج استخدام الدالة
      response = client.chat.completions.create(
          model=deployment_name,
          messages=messages,
          tools=tools,
          tool_choice="auto",
      )
  
      # معالجة استجابة النموذج
      response_message = response.choices[0].message
      messages.append(response_message)
  
      print("Model's response:")  

      print(response_message)
  
    ```

    ```bash
    Model's response:
    ChatCompletionMessage(content=None, role='assistant', function_call=None, tool_calls=[ChatCompletionMessageToolCall(id='call_pOsKdUlqvdyttYB67MOj434b', function=Function(arguments='{"location":"San Francisco"}', name='get_current_time'), type='function')])
    ```
  
1. **الكود اللازم لتنفيذ المهمة:**

    الآن بعد أن اختار النموذج أي دالة يجب تشغيلها، يجب تنفيذ الكود لتنفيذ المهمة.
    يمكننا تنفيذ كود الحصول على الوقت الحالي باستخدام بايثون. سنحتاج أيضًا إلى كتابة كود لاستخلاص الاسم والمعاملات من response_message للحصول على النتيجة النهائية.

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
     # التعامل مع استدعاءات الدالة
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
  
      # استدعاء واجهة برمجة التطبيقات الثانية: الحصول على الاستجابة النهائية من النموذج
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

استدعاء الدوال هو جوهر معظم، إن لم يكن كل، نمط تصميم استخدام الأدوات، ومع ذلك فإن تنفيذه من الصفر قد يكون تحديًا أحيانًا.
كما تعلمنا في [الدرس 2](../../../02-explore-agentic-frameworks) توفر الأُطُر الوكيلة كتلًا جاهزة لبناء تطبيقات استخدام الأدوات.

## أمثلة على استخدام الأدوات مع الأُطُر الوكيلة

فيما يلي بعض الأمثلة على كيفية تطبيق نمط تصميم استخدام الأدوات باستخدام أُطُر وكيلة مختلفة:

### إطار عمل Microsoft Agent

<a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">إطار عمل Microsoft Agent</a> هو إطار عمل مفتوح المصدر لبناء وكلاء الذكاء الاصطناعي. يُبسط عملية استخدام استدعاء الدوال من خلال السماح لك بتعريف الأدوات كدوال بايثون باستخدام المزخرف `@tool`. يدير الإطار التفاعل بين النموذج والكود الخاص بك. كما يوفر الوصول إلى أدوات جاهزة مثل البحث في الملفات ومفسر الشفرة عبر `AzureAIProjectAgentProvider`.

الرسم التوضيحي التالي يوضح عملية استدعاء الدوال باستخدام إطار عمل Microsoft Agent:

![function calling](../../../translated_images/ar/functioncalling-diagram.a84006fc287f6014.webp)

في إطار عمل Microsoft Agent، تُعرف الأدوات كدوال مزخرفة. يمكننا تحويل دالة `get_current_time` التي رأيناها سابقًا إلى أداة باستخدام المزخرف `@tool`. يقوم الإطار تلقائيًا بتسلسل الدالة ومعاملاتها، وإنشاء المخطط لإرساله إلى نموذج اللغة الكبيرة.

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

# إنشاء وكيل وتشغيله باستخدام الأداة
agent = await provider.create_agent(name="TimeAgent", instructions="Use available tools to answer questions.", tools=get_current_time)
response = await agent.run("What time is it?")
```
  
### خدمة Azure AI Agent

<a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">خدمة Azure AI Agent</a> هي إطار وكيل أحدث مصمم لتمكين المطورين من بناء، نشر، وتوسيع نطاق وكلاء ذكيين عالي الجودة وقابلين للتوسع بأمان دون الحاجة لإدارة الموارد الحاسوبية والتخزينية الأساسية. هو مفيد بشكل خاص لتطبيقات المؤسسات لأنه خدمة مُدارة بالكامل مع أمان على مستوى المؤسسات.

بالمقارنة مع تطوير باستخدام واجهة برمجة تطبيقات LLM مباشرةً، تقدم خدمة Azure AI Agent بعض المزايا، بما في ذلك:

- استدعاء الأدوات تلقائيًا – لا حاجة لتحليل مكالمة الأداة، استدعاء الأداة، والتعامل مع الاستجابة؛ فكل هذا يتم الآن على الخادم
- إدارة آمنة للبيانات – بدلاً من إدارة حالة المحادثة بنفسك، يمكنك الاعتماد على الخيوط لتخزين كل المعلومات التي تحتاجها
- أدوات جاهزة للاستخدام – أدوات يمكنك استخدامها للتفاعل مع مصادر بياناتك، مثل Bing، Azure AI Search، وAzure Functions.

يمكن تقسيم الأدوات المتاحة في خدمة Azure AI Agent إلى فئتين:

1. أدوات المعرفة:
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/bing-grounding?tabs=python&pivots=overview" target="_blank">التمكين بواسطة بحث Bing</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/file-search?tabs=python&pivots=overview" target="_blank">البحث في الملفات</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-ai-search?tabs=azurecli%2Cpython&pivots=overview-azure-ai-search" target="_blank">Azure AI Search</a>

2. أدوات الإجراءات:
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/function-calling?tabs=python&pivots=overview" target="_blank">استدعاء الدوال</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/code-interpreter?tabs=python&pivots=overview" target="_blank">مفسر الشفرة</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/openapi-spec?tabs=python&pivots=overview" target="_blank">أدوات معرفة بواسطة OpenAPI</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-functions?pivots=overview" target="_blank">وظائف Azure</a>

تتيح لنا خدمة الوكيل القدرة على استخدام هذه الأدوات معًا كمجموعة أدوات (`toolset`). كما تستخدم `threads` التي تتبع تاريخ الرسائل من محادثة معينة.

تخيل أنك وكيل مبيعات في شركة تسمى Contoso. تريد تطوير وكيل حواري يمكنه الرد على أسئلة تتعلق ببيانات المبيعات الخاصة بك.

توضح الصورة التالية كيف يمكنك استخدام خدمة Azure AI Agent لتحليل بيانات مبيعاتك:

![Agentic Service In Action](../../../translated_images/ar/agent-service-in-action.34fb465c9a84659e.webp)

لاستخدام أي من هذه الأدوات مع الخدمة، يمكننا إنشاء عميل وتعريف أداة أو مجموعة أدوات. لتنفيذ ذلك عمليًا يمكننا استخدام كود بايثون التالي. سيتمكن نموذج اللغة الكبيرة من النظر إلى مجموعة الأدوات وتحديد ما إذا كان سيستخدم الدالة التي أنشأها المستخدم، `fetch_sales_data_using_sqlite_query`، أو مفسر الشفرة المدمج اعتمادًا على طلب المستخدم.

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

# تهيئة وكيل استدعاء الدوال مع دالة fetch_sales_data_using_sqlite_query وإضافتها إلى مجموعة الأدوات
fetch_data_function = FunctionTool(fetch_sales_data_using_sqlite_query)
toolset.add(fetch_data_function)

# تهيئة أداة مفسر الكود وإضافتها إلى مجموعة الأدوات.
code_interpreter = code_interpreter = CodeInterpreterTool()
toolset.add(code_interpreter)

agent = project_client.agents.create_agent(
    model="gpt-4o-mini", name="my-agent", instructions="You are helpful agent", 
    toolset=toolset
)
```

## ما هي الاعتبارات الخاصة لاستخدام نمط تصميم استخدام الأدوات لبناء وكلاء ذكاء اصطناعي موثوقين؟

من المخاوف الشائعة المتعلقة بـ SQL الذي يتم إنشاؤه ديناميكيًا بواسطة نماذج اللغة الكبيرة هي الأمان، خصوصًا خطر حقن SQL أو الأفعال الخبيثة مثل حذف أو العبث بقاعدة البيانات. في حين أن هذه المخاوف صحيحة، يمكن التخفيف منها بفعالية من خلال تكوين أذونات الوصول إلى قاعدة البيانات بشكل صحيح. بالنسبة لمعظم قواعد البيانات، يتطلب هذا تكوين قاعدة البيانات للقراءة فقط. بالنسبة لخدمات قواعد البيانات مثل PostgreSQL أو Azure SQL، يجب تعيين دور للقراءة فقط (SELECT) للتطبيق.

يشكل تشغيل التطبيق في بيئة آمنة حماية إضافية. في السيناريوهات المؤسسية، يتم عادةً استخراج البيانات وتحويلها من أنظمة تشغيلية إلى قاعدة بيانات أو مستودع بيانات للقراءة فقط بهيكل بيانات سهل الاستخدام. هذه المقاربة تضمن أن البيانات آمنة، ومحسنة للأداء والوصول، وأن التطبيق يتمتع بإمكانية وصول مقيدة للقراءة فقط.

## الأكواد النموذجية

- بايثون: [إطار العمل الوكيل](./code_samples/04-python-agent-framework.ipynb)
- .NET: [إطار العمل الوكيل](./code_samples/04-dotnet-agent-framework.md)

## هل لديك المزيد من الأسئلة حول أنماط تصميم استخدام الأدوات؟

انضم إلى [خادم Microsoft Foundry على ديسكورد](https://aka.ms/ai-agents/discord) للتواصل مع متعلمين آخرين، حضور الساعات المكتبية، والحصول على إجابات لأسئلتك حول وكلاء الذكاء الاصطناعي.

## موارد إضافية

- <a href="https://microsoft.github.io/build-your-first-agent-with-azure-ai-agent-service-workshop/" target="_blank">ورشة عمل خدمة وكلاء Azure AI</a>
- <a href="https://github.com/Azure-Samples/contoso-creative-writer/tree/main/docs/workshop" target="_blank">ورشة عمل Contoso Creative Writer للوكيل المتعدد</a>
- <a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">نظرة عامة على إطار عمل Microsoft Agent</a>

## الدرس السابق

[فهم أنماط التصميم الوكيلية](../03-agentic-design-patterns/README.md)

## الدرس التالي
[وكيل RAG](../05-agentic-rag/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**إخلاء المسؤولية**:
تمت ترجمة هذا المستند باستخدام خدمة الترجمة بالذكاء الاصطناعي [Co-op Translator](https://github.com/Azure/co-op-translator). بينما نسعى لتحقيق الدقة، يرجى العلم أن الترجمات الآلية قد تحتوي على أخطاء أو عدم دقة. يجب اعتبار المستند الأصلي بلغته الأصلية المصدر المعتمد والموثوق. بالنسبة للمعلومات الحساسة أو الهامة، يُنصح باستخدام الترجمة المهنية من قبل مترجم بشري. نحن غير مسؤولين عن أي سوء فهم أو سوء تفسير ناتج عن استخدام هذه الترجمة.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->