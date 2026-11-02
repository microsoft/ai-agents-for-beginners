[![نمط تصميم التخطيط](../../../translated_images/ar/lesson-7-thumbnail.f7163ac557bea123.webp)](https://youtu.be/kPfJ2BrBCMY?si=9pYpPXp0sSbK91Dr)

> _(انقر على الصورة أعلاه لمشاهدة فيديو هذا الدرس)_

# تصميم التخطيط

## مقدمة

سيغطي هذا الدرس

* تحديد هدف شامل واضح وتقسيم مهمة معقدة إلى مهام يمكن إدارتها.
* الاستفادة من الإخراج المنظم للحصول على استجابات أكثر موثوقية وقابلة للقراءة آليًا.
* تطبيق نهج مدفوع بالأحداث للتعامل مع المهام الديناميكية والمدخلات غير المتوقعة.

## أهداف التعلم

بعد إكمال هذا الدرس، سيكون لديك فهم حول:

* التعرف على هدف شامل لوكيل الذكاء الاصطناعي وضبطه، مع ضمان معرفته الواضحة بما يجب تحقيقه.
* تحليل مهمة معقدة إلى مهام فرعية يمكن إدارتها وتنظيمها في تسلسل منطقي.
* تزويد الوكلاء بالأدوات المناسبة (مثل أدوات البحث أو تحليلات البيانات)، وتحديد متى وكيف يتم استخدامها، والتعامل مع الحالات غير المتوقعة التي قد تنشأ.
* تقييم نتائج المهام الفرعية، قياس الأداء، والتكرار على الإجراءات لتحسين الناتج النهائي.

## تحديد الهدف الشامل وتقسيم المهمة

![تحديد الأهداف والمهام](../../../translated_images/ar/defining-goals-tasks.d70439e19e37c47a.webp)

معظم المهام الواقعية معقدة للغاية بحيث لا يمكن معالجتها في خطوة واحدة. يحتاج وكيل الذكاء الاصطناعي إلى هدف موجز يوجه تخطيطه وإجراءاته. على سبيل المثال، اعتبر الهدف:

    "إنشاء مسار سفر لمدة 3 أيام."

على الرغم من بساطة العبارة، إلا أنه لا يزال بحاجة إلى تحسين. فكلما كان الهدف أوضح، كان بإمكان الوكيل (وأي متعاونين بشريين) التركيز بشكل أفضل على تحقيق النتيجة الصحيحة، مثل إنشاء مسار شامل يشمل خيارات الرحلات الجوية، وتوصيات الفنادق، واقتراحات الأنشطة.

### تحليل المهمة

تصبح المهام الكبيرة أو المعقدة أكثر قابلية للإدارة عندما تُقسم إلى مهام فرعية موجهة بالهدف.
بالنسبة لمثال مسار السفر، يمكنك تقسيم الهدف إلى:

* حجز الرحلات الجوية
* حجز الفنادق
* تأجير السيارات
* التخصيص

يمكن بعد ذلك التعامل مع كل مهمة فرعية بواسطة وكلاء مخصصين أو عمليات. قد يتخصص وكيل في البحث عن أفضل عروض الرحلات الجوية، والآخر يركز على حجز الفنادق، وهكذا. يمكن لوكيل منسق أو "تدفق هابط" تجميع هذه النتائج في مسار سفر متكامِل للمستخدم النهائي.

يتيح هذا النهج المعياري أيضًا تحسينات تدريجية. على سبيل المثال، يمكنك إضافة وكلاء متخصصين في توصيات الطعام أو اقتراحات الأنشطة المحلية وصقل المسار مع مرور الوقت.

### الإخراج المنظم

يمكن لنماذج اللغات الكبيرة (LLMs) إنتاج إخراج منظم (مثل JSON) يكون أسهل لوكلاء أو خدمات التدفق الهابط لتحليله ومعالجته. هذا مفيد بشكل خاص في سياق تعدد الوكلاء، حيث يمكن تنفيذ هذه المهام بعد استلام إخراج التخطيط.

يوضح المقتطف الخاص بـ Python التالي وكيل تخطيط بسيط يقسم هدفًا إلى مهام فرعية وينتج خطة منظمة:

```python
from pydantic import BaseModel
from enum import Enum
from typing import List, Optional, Union
import json
import os
from typing import Optional
from pprint import pprint
from agent_framework.foundry import FoundryChatClient
from azure.identity import AzureCliCredential

class AgentEnum(str, Enum):
    FlightBooking = "flight_booking"
    HotelBooking = "hotel_booking"
    CarRental = "car_rental"
    ActivitiesBooking = "activities_booking"
    DestinationInfo = "destination_info"
    DefaultAgent = "default_agent"
    GroupChatManager = "group_chat_manager"

# نموذج مهمة فرعية للسفر
class TravelSubTask(BaseModel):
    task_details: str
    assigned_agent: AgentEnum  # نريد تعيين المهمة للوكيل

class TravelPlan(BaseModel):
    main_task: str
    subtasks: List[TravelSubTask]
    is_greeting: bool

provider = FoundryChatClient(
    project_endpoint=os.environ["AZURE_AI_PROJECT_ENDPOINT"],
    model=os.environ["AZURE_AI_MODEL_DEPLOYMENT_NAME"],
    credential=AzureCliCredential(),
)

# تعريف رسالة المستخدم
system_prompt = """You are a planner agent.
    Your job is to decide which agents to run based on the user's request.
    Provide your response in JSON format with the following structure:
{'main_task': 'Plan a family trip from Singapore to Melbourne.',
 'subtasks': [{'assigned_agent': 'flight_booking',
               'task_details': 'Book round-trip flights from Singapore to '
                               'Melbourne.'}
    Below are the available agents specialised in different tasks:
    - FlightBooking: For booking flights and providing flight information
    - HotelBooking: For booking hotels and providing hotel information
    - CarRental: For booking cars and providing car rental information
    - ActivitiesBooking: For booking activities and providing activity information
    - DestinationInfo: For providing information about destinations
    - DefaultAgent: For handling general requests"""

user_message = "Create a travel plan for a family of 2 kids from Singapore to Melbourne"

response = client.create_response(input=user_message, instructions=system_prompt)

response_content = response.output_text
pprint(json.loads(response_content))
```

### وكيل التخطيط مع تنسيق متعدد الوكلاء

في هذا المثال، يتلقى وكيل التوجيه الدلالي طلب المستخدم (مثل "أحتاج خطة فندق لرحلتي.").

ثم يقوم المخطط بـ:

* استلام خطة الفندق: يأخذ المخطط رسالة المستخدم، وبناءً على موجه النظام (بما في ذلك تفاصيل الوكلاء المتاحة)، ينتج خطة سفر منظمة.
* سرد الوكلاء وأدواتهم: يحتفظ سجل الوكلاء بقائمة من الوكلاء (مثل حجز الرحلات، الفنادق، تأجير السيارات، والأنشطة) مع الوظائف أو الأدوات التي يقدمونها.
* توجيه الخطة إلى الوكلاء المعنيين: بناءً على عدد المهام الفرعية، إما يرسل المخطط الرسالة مباشرة إلى وكيل مخصص (لسيناريوهات المهمة الفردية) أو ينسق عبر مدير دردشة مجموعة للتعاون متعدد الوكلاء.
* تلخيص النتيجة: في النهاية، يلخص المخطط الخطة المنتجة للوضوح.
يوضح مثال كود Python التالي هذه الخطوات:

```python

from pydantic import BaseModel

from enum import Enum
from typing import List, Optional, Union

class AgentEnum(str, Enum):
    FlightBooking = "flight_booking"
    HotelBooking = "hotel_booking"
    CarRental = "car_rental"
    ActivitiesBooking = "activities_booking"
    DestinationInfo = "destination_info"
    DefaultAgent = "default_agent"
    GroupChatManager = "group_chat_manager"

# نموذج المهمة الفرعية للسفر

class TravelSubTask(BaseModel):
    task_details: str
    assigned_agent: AgentEnum # نريد تعيين المهمة للوكيل

class TravelPlan(BaseModel):
    main_task: str
    subtasks: List[TravelSubTask]
    is_greeting: bool
import json
import os
from typing import Optional

from agent_framework.foundry import FoundryChatClient
from azure.identity import AzureCliCredential

# إنشاء العميل

provider = FoundryChatClient(
    project_endpoint=os.environ["AZURE_AI_PROJECT_ENDPOINT"],
    model=os.environ["AZURE_AI_MODEL_DEPLOYMENT_NAME"],
    credential=AzureCliCredential(),
)

from pprint import pprint

# تعريف رسالة المستخدم

system_prompt = """You are a planner agent.
    Your job is to decide which agents to run based on the user's request.
    Below are the available agents specialized in different tasks:
    - FlightBooking: For booking flights and providing flight information
    - HotelBooking: For booking hotels and providing hotel information
    - CarRental: For booking cars and providing car rental information
    - ActivitiesBooking: For booking activities and providing activity information
    - DestinationInfo: For providing information about destinations
    - DefaultAgent: For handling general requests"""

user_message = "Create a travel plan for a family of 2 kids from Singapore to Melbourne"

response = client.create_response(input=user_message, instructions=system_prompt)

response_content = response.output_text

# طباعة محتوى الرد بعد تحميله كـ JSON

pprint(json.loads(response_content))
```

ما يلي هو الإخراج من الكود السابق ويمكنك بعد ذلك استخدام هذا الإخراج المنظم لتوجيه إلى `assigned_agent` وتلخيص خطة السفر للمستخدم النهائي.

```json
{
    "is_greeting": "False",
    "main_task": "Plan a family trip from Singapore to Melbourne.",
    "subtasks": [
        {
            "assigned_agent": "flight_booking",
            "task_details": "Book round-trip flights from Singapore to Melbourne."
        },
        {
            "assigned_agent": "hotel_booking",
            "task_details": "Find family-friendly hotels in Melbourne."
        },
        {
            "assigned_agent": "car_rental",
            "task_details": "Arrange a car rental suitable for a family of four in Melbourne."
        },
        {
            "assigned_agent": "activities_booking",
            "task_details": "List family-friendly activities in Melbourne."
        },
        {
            "assigned_agent": "destination_info",
            "task_details": "Provide information about Melbourne as a travel destination."
        }
    ]
}
```

مثال على دفتر ملاحظات يحتوي على نموذج الكود السابق متاح [هنا](./code_samples/07-python-agent-framework.ipynb).

### التخطيط التكراري

تتطلب بعض المهام تكرارًا أو إعادة تخطيط، حيث تؤثر نتيجة مهمة فرعية على المهمة التالية. على سبيل المثال، إذا اكتشف الوكيل تنسيق بيانات غير متوقع أثناء حجز الرحلات، قد يحتاج إلى تعديل استراتيجيته قبل الانتقال إلى حجز الفنادق.

بالإضافة إلى ذلك، يمكن لتعليقات المستخدم (مثل قرار بشري بتفضيل رحلة أبكر) أن تحفز إعادة تخطيط جزئية. هذا النهج الديناميكي والمتكرر يضمن أن الحل النهائي يتوافق مع القيود الواقعية وتفضيلات المستخدم المتطورة.

على سبيل المثال، كود عينة

```python
import os
from agent_framework.foundry import FoundryChatClient
from azure.identity import AzureCliCredential
#.. نفس الكود السابق وتمرير سجل المستخدم والخطة الحالية

system_prompt = """You are a planner agent to optimize the
    Your job is to decide which agents to run based on the user's request.
    Below are the available agents specialized in different tasks:
    - FlightBooking: For booking flights and providing flight information
    - HotelBooking: For booking hotels and providing hotel information
    - CarRental: For booking cars and providing car rental information
    - ActivitiesBooking: For booking activities and providing activity information
    - DestinationInfo: For providing information about destinations
    - DefaultAgent: For handling general requests"""

user_message = "Create a travel plan for a family of 2 kids from Singapore to Melbourne"

response = client.create_response(
    input=user_message,
    instructions=system_prompt,
    context=f"Previous travel plan - {TravelPlan}",
)
# .. إعادة التخطيط وإرسال المهام إلى الوكلاء المعنيين
```

لمزيد من التخطيط الشامل، تحقق من Magnetic One <a href="https://www.microsoft.com/research/articles/magentic-one-a-generalist-multi-agent-system-for-solving-complex-tasks" target="_blank">مقال المدونة</a> لحل المهام المعقدة.

## الملخص

في هذا المقال نظرنا إلى مثال على كيفية إنشاء مخطط يمكنه اختيار الوكلاء المتاحين المحددين بطريقة ديناميكية. يقوم مخرجات المخطط بتقسيم المهام وتوزيع الوكلاء بحيث يمكن تنفيذها. ويفترض أن الوكلاء لديهم حق الوصول إلى الوظائف/الأدوات المطلوبة لأداء المهمة. بالإضافة إلى الوكلاء يمكنك تضمين أنماط أخرى مثل الانعكاس، الملخص، ودردشة الجولة لتخصيص أكثر.

## موارد إضافية

Magnetic One - نظام متعدد الوكلاء عام لحل المهام المعقدة وقد حقق نتائج مذهلة في عدة معايير تحدي وكيلية. المرجع: <a href="https://www.microsoft.com/research/articles/magentic-one-a-generalist-multi-agent-system-for-solving-complex-tasks" target="_blank">Magnetic One</a>. في هذا التنفيذ يقوم المنسق بإنشاء خطط محددة لكل مهمة ويفوض هذه المهام إلى الوكلاء المتاحين. بالإضافة إلى التخطيط، يستخدم المنسق أيضًا آلية تتبع لمراقبة تقدم المهمة وإعادة التخطيط عند الحاجة.

### هل لديك المزيد من الأسئلة حول نمط تصميم التخطيط؟

انضم إلى [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D) للقاء متعلمين آخرين، حضور ساعات المكتب والحصول على إجابات لأسئلة وكلاء الذكاء الاصطناعي الخاصة بك.

## الدرس السابق

[بناء وكلاء ذكاء اصطناعي جديرين بالثقة](../06-building-trustworthy-agents/README.md)

## الدرس التالي

[نمط تصميم متعدد الوكلاء](../08-multi-agent/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**تنويه**:
تمت ترجمة هذا المستند باستخدام خدمة الترجمة بالذكاء الاصطناعي [Co-op Translator](https://github.com/Azure/co-op-translator). بينما نسعى للدقة، يرجى العلم أن الترجمات الآلية قد تحتوي على أخطاء أو عدم دقة. يجب اعتبار المستند الأصلي بلغته الأصلية المصدر الرسمي والمعتمد. للمعلومات الهامة، يُنصح بالاستعانة بترجمة بشرية محترفة. نحن غير مسؤولين عن أي سوء فهم أو تفسير ناتج عن استخدام هذه الترجمة.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->