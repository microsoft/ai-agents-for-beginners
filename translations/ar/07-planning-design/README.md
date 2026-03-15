[![نمط تصميم التخطيط](../../../translated_images/ar/lesson-7-thumbnail.f7163ac557bea123.webp)](https://youtu.be/kPfJ2BrBCMY?si=9pYpPXp0sSbK91Dr)

> _(انقر على الصورة أعلاه لمشاهدة فيديو هذا الدرس)_

# تصميم التخطيط

## مقدمة

سيغطي هذا الدرس

* تحديد هدف واضح شامل وتقسيم مهمة معقدة إلى مهام قابلة للإدارة.
* الاستفادة من الإخراج المنظم للحصول على ردود أكثر موثوقية وقابلة للقراءة آليًا.
* تطبيق نهج قائم على الأحداث للتعامل مع المهام الديناميكية والمدخلات غير المتوقعة.

## أهداف التعلم

بعد إكمال هذا الدرس، سيكون لديك فهم حول:

* التعرف على هدف شامل لوكيل الذكاء الاصطناعي وتحديده، مع ضمان معرفته الواضحة بما يجب تحقيقه.
* تفكيك مهمة معقدة إلى مهام فرعية يمكن إدارتها وتنظيمها في تسلسل منطقي.
* تزويد الوكلاء بالأدوات المناسبة (مثل أدوات البحث أو أدوات تحليل البيانات)، وتحديد متى وكيف تُستخدم، والتعامل مع المواقف غير المتوقعة التي تظهر.
* تقييم نتائج المهام الفرعية، وقياس الأداء، والتكرار على الإجراءات لتحسين الناتج النهائي.

## تحديد الهدف الشامل وتقسيم المهمة

![تحديد الأهداف والمهام](../../../translated_images/ar/defining-goals-tasks.d70439e19e37c47a.webp)

معظم المهام الحقيقية المعقدة يصعب التعامل معها في خطوة واحدة. يحتاج وكيل الذكاء الاصطناعي إلى هدف موجز يوجه تخطيطه وأفعاله. على سبيل المثال، اعتبر الهدف:

    "إنشاء خطة سفر لمدة 3 أيام."

على الرغم من بساطته في التعبير، إلا أنه لا يزال بحاجة إلى تحسين. كلما كان الهدف أوضح، كان بإمكان الوكيل (وأي متعاون بشري) التركيز بشكل أفضل على تحقيق النتيجة الصحيحة، مثل إنشاء خطة شاملة تشمل خيارات الرحلات الجوية، وتوصيات الفنادق، واقتراحات الأنشطة.

### تقسيم المهمة

تصبح المهام الكبيرة أو المعقدة أكثر قابلية للإدارة عند تقسيمها إلى مهام فرعية موجهة نحو الهدف.
بالنسبة لمثال خطة السفر، يمكنك تقسيم الهدف إلى:

* حجز الرحلات الجوية
* حجز الفندق
* تأجير السيارات
* التخصيص

يمكن بعد ذلك التعامل مع كل مهمة فرعية بواسطة وكلاء أو عمليات مخصصة. قد يتخصص أحد الوكلاء في البحث عن أفضل عروض الرحلات الجوية، وآخر يركز على حجز الفنادق، وهكذا. يمكن لوكيل تنسيقي أو "متدفق لأسفل" تجميع هذه النتائج في خطة متماسكة واحدة للمستخدم النهائي.

يسمح هذا النهج المعياري أيضًا بالتحسينات التدريجية. على سبيل المثال، يمكنك إضافة وكلاء متخصصين لتوصيات الطعام أو اقتراحات الأنشطة المحلية وتحسين الخطة مع مرور الوقت.

### الإخراج المنظم

يمكن لنماذج اللغة الكبيرة (LLMs) إنشاء إخراج منظم (مثل JSON) يكون أسهل على الوكلاء أو الخدمات اللاحقة لتحليله ومعالجته. هذا مفيد بشكل خاص في سياق متعدد الوكلاء، حيث يمكننا تنفيذ هذه المهام بعد استلام ناتج التخطيط.

يُظهر المقتطف التالي بلغة بايثون وكيل تخطيط بسيط يقوم بتفكيك هدف إلى مهام فرعية وإنشاء خطة منظمة:

```python
from pydantic import BaseModel
from enum import Enum
from typing import List, Optional, Union
import json
import os
from typing import Optional
from pprint import pprint
from agent_framework.azure import AzureAIProjectAgentProvider
from azure.identity import AzureCliCredential

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
    assigned_agent: AgentEnum  # نريد تعيين المهمة للوكيل

class TravelPlan(BaseModel):
    main_task: str
    subtasks: List[TravelSubTask]
    is_greeting: bool

provider = AzureAIProjectAgentProvider(credential=AzureCliCredential())

# تحديد رسالة المستخدم
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

### وكيل التخطيط مع تنظيم متعدد الوكلاء

في هذا المثال، يتلقى وكيل التوجيه الدلالي طلب المستخدم (مثل "أحتاج خطة فندق لرحلتي.").

يقوم المخطط بعد ذلك بـ:

* استلام خطة الفندق: يأخذ المخطط رسالة المستخدم وبناءً على طلب النظام (بما في ذلك تفاصيل الوكلاء المتاحة)، يُنشئ خطة سفر منظمة.
* سرد الوكلاء وأدواتهم: يحتفظ سجل الوكلاء بقائمة الوكلاء (مثل الطيران، الفندق، تأجير السيارات، والأنشطة) جنبًا إلى جنب مع الوظائف أو الأدوات التي يقدمونها.
* توجيه الخطة إلى الوكلاء المعنيين: اعتمادًا على عدد المهام الفرعية، إما يرسل المخطط الرسالة مباشرة إلى وكيل مخصص (للسيناريوهات ذات المهمة الواحدة) أو ينسق عبر مدير الدردشة الجماعية للتعاون متعدد الوكلاء.
* تلخيص النتيجة: أخيرًا، يلخص المخطط الخطة المولدة للوضوح.
يُوضح نموذج الكود التالي بلغة بايثون هذه الخطوات:

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

from agent_framework.azure import AzureAIProjectAgentProvider
from azure.identity import AzureCliCredential

# إنشاء العميل

provider = AzureAIProjectAgentProvider(credential=AzureCliCredential())

from pprint import pprint

# تحديد رسالة المستخدم

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

# طباعة محتوى الاستجابة بعد تحميله كـ JSON

pprint(json.loads(response_content))
```

فيما يلي الناتج من الكود السابق، ويمكنك بعد ذلك استخدام هذا الإخراج المنظم لتوجيهه إلى `assigned_agent` وتلخيص خطة السفر للمستخدم النهائي.

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

مثال على دفتر ملاحظات يحتوي على نموذج الكود السابق متوفر [هنا](07-python-agent-framework.ipynb).

### التخطيط التكراري

بعض المهام تتطلب تكرارًا أو إعادة تخطيط، حيث تؤثر نتيجة مهمة فرعية واحدة على التالية. على سبيل المثال، إذا اكتشف الوكيل تنسيق بيانات غير متوقع أثناء حجز الرحلات الجوية، فقد يحتاج إلى تعديل استراتيجيته قبل الانتقال إلى حجز الفنادق.

بالإضافة إلى ذلك، يمكن لملاحظات المستخدم (مثل قرار بشري بتفضيل رحلة أبكر) أن تثير إعادة تخطيط جزئي. هذا النهج الديناميكي والتكراري يضمن أن الحل النهائي يتماشى مع القيود الواقعية وتفضيلات المستخدم المتطورة.

على سبيل المثال كود

```python
from agent_framework.azure import AzureAIProjectAgentProvider
from azure.identity import AzureCliCredential
#.. نفس الشيفرة السابقة ومرر تاريخ المستخدم والخطة الحالية

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

للتخطيط الأكثر شمولاً، تفقد مدونة Magnetic One <a href="https://www.microsoft.com/research/articles/magentic-one-a-generalist-multi-agent-system-for-solving-complex-tasks" target="_blank">المدونة</a> لحل المهام المعقدة.

## الملخص

في هذه المقالة، نظرنا إلى مثال عن كيفية إنشاء مخطط يمكنه اختيار الوكلاء المتاحين المحددين بشكل ديناميكي. يقوم ناتج المخطط بتفكيك المهام وتعيين الوكلاء حتى يمكن تنفيذها. يُفترض أن الوكلاء لديهم وصول إلى الوظائف/الأدوات المطلوبة لأداء المهمة. بالإضافة إلى الوكلاء، يمكنك تضمين أنماط أخرى مثل الانعكاس، والملخص، ودردشة التناوب لتخصيص إضافي.

## موارد إضافية

Magentic One - نظام متعدد الوكلاء عام لحل المهام المعقدة وقد حقق نتائج رائعة في العديد من معايير الوكلاء التحديّة. المرجع: <a href="https://www.microsoft.com/research/articles/magentic-one-a-generalist-multi-agent-system-for-solving-complex-tasks" target="_blank">Magentic One</a>. في هذا التنفيذ، يقوم المنسق بإنشاء خطط محددة لكل مهمة ويوزع هذه المهام على الوكلاء المتاحين. بالإضافة إلى التخطيط، يستخدم المنسق أيضًا آلية تتبع لمراقبة تقدم المهمة وإعادة التخطيط حسب الحاجة.

### هل لديك المزيد من الأسئلة حول نمط تصميم التخطيط؟

انضم إلى [Discord مايكروسوفت فاوندرى](https://aka.ms/ai-agents/discord) للقاء متعلمين آخرين، وحضور ساعات العمل، والحصول على إجابات على أسئلتك حول وكلاء الذكاء الاصطناعي.

## الدرس السابق

[بناء وكلاء ذكاء اصطناعي جديرين بالثقة](../06-building-trustworthy-agents/README.md)

## الدرس التالي

[نمط التصميم متعدد الوكلاء](../08-multi-agent/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**تنويه**:  
تمت ترجمة هذا المستند باستخدام خدمة الترجمة الآلية [Co-op Translator](https://github.com/Azure/co-op-translator). بينما نسعى لتحقيق الدقة، يرجى العلم أن الترجمات الآلية قد تحتوي على أخطاء أو عدم دقة. يجب اعتبار المستند الأصلي بلغته الأصلية المصدر المعتمد. للمعلومات الحساسة أو الحاسمة، يُنصح بالاعتماد على ترجمة بشرية احترافية. نحن غير مسؤولين عن أي سوء فهم أو تفسير ناتج عن استخدام هذه الترجمة.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->