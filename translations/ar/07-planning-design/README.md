<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "43069833a0412210ad5c3cc93d9c2146",
  "translation_date": "2025-09-18T14:11:06+00:00",
  "source_file": "07-planning-design/README.md",
  "language_code": "ar"
}
-->
[![تخطيط نمط التصميم](../../../translated_images/lesson-7-thumbnail.f7163ac557bea1236242cc86b178c3f1bbf5eb07b87f9cd7c256b366e32bcbb6.ar.png)](https://youtu.be/kPfJ2BrBCMY?si=9pYpPXp0sSbK91Dr)

> _(اضغط على الصورة أعلاه لمشاهدة فيديو الدرس)_

# تخطيط التصميم

## المقدمة

سيتناول هذا الدرس:

* تحديد هدف شامل واضح وتقسيم المهام المعقدة إلى مهام قابلة للإدارة.
* الاستفادة من المخرجات المنظمة للحصول على استجابات أكثر موثوقية وقابلة للقراءة آليًا.
* تطبيق نهج يعتمد على الأحداث للتعامل مع المهام الديناميكية والمدخلات غير المتوقعة.

## أهداف التعلم

بعد إكمال هذا الدرس، ستتمكن من فهم:

* كيفية تحديد ووضع هدف شامل لوكيل الذكاء الاصطناعي، لضمان معرفة واضحة بما يجب تحقيقه.
* كيفية تقسيم المهام المعقدة إلى مهام فرعية قابلة للإدارة وتنظيمها في تسلسل منطقي.
* تجهيز الوكلاء بالأدوات المناسبة (مثل أدوات البحث أو أدوات تحليل البيانات)، وتحديد متى وكيف يتم استخدامها، والتعامل مع المواقف غير المتوقعة التي قد تنشأ.
* تقييم نتائج المهام الفرعية، قياس الأداء، وتكرار الإجراءات لتحسين المخرجات النهائية.

## تحديد الهدف الشامل وتقسيم المهمة

![تحديد الأهداف والمهام](../../../translated_images/defining-goals-tasks.d70439e19e37c47ac76c48b209a4eb515bea5b8a5207f6b2e7b5e597f09ccf6a.ar.png)

معظم المهام في العالم الحقيقي معقدة للغاية بحيث لا يمكن التعامل معها في خطوة واحدة. يحتاج وكيل الذكاء الاصطناعي إلى هدف موجز لتوجيه تخطيطه وأفعاله. على سبيل المثال، ضع في اعتبارك الهدف:

    "إنشاء جدول رحلة لمدة 3 أيام."

على الرغم من أنه بسيط في التعبير، إلا أنه يحتاج إلى تحسين. كلما كان الهدف أكثر وضوحًا، كان الوكيل (وأي متعاون بشري) أكثر تركيزًا على تحقيق النتيجة الصحيحة، مثل إنشاء جدول شامل يتضمن خيارات الطيران، توصيات الفنادق، واقتراحات الأنشطة.

### تقسيم المهام

تصبح المهام الكبيرة أو المعقدة أكثر قابلية للإدارة عند تقسيمها إلى مهام فرعية صغيرة موجهة نحو الهدف.
بالنسبة لمثال جدول الرحلة، يمكن تقسيم الهدف إلى:

* حجز الطيران
* حجز الفنادق
* استئجار السيارات
* التخصيص الشخصي

يمكن بعد ذلك معالجة كل مهمة فرعية بواسطة وكلاء أو عمليات مخصصة. قد يتخصص وكيل واحد في البحث عن أفضل عروض الطيران، بينما يركز آخر على حجز الفنادق، وهكذا. يمكن لوكيل تنسيق أو "وكيل لاحق" تجميع هذه النتائج في جدول شامل للمستخدم النهائي.

هذا النهج المعياري يسمح أيضًا بتحسينات تدريجية. على سبيل المثال، يمكنك إضافة وكلاء متخصصين لتوصيات الطعام أو اقتراحات الأنشطة المحلية وتحسين الجدول بمرور الوقت.

### المخرجات المنظمة

يمكن لنماذج اللغة الكبيرة (LLMs) إنشاء مخرجات منظمة (مثل JSON) تكون أسهل للوكلاء أو الخدمات اللاحقة في تحليلها ومعالجتها. هذا مفيد بشكل خاص في سياق متعدد الوكلاء، حيث يمكن تنفيذ هذه المهام بعد استلام مخرجات التخطيط. راجع هذا 

للحصول على نظرة سريعة.

يوضح مقتطف Python التالي وكيل تخطيط بسيط يقوم بتقسيم الهدف إلى مهام فرعية وإنشاء خطة منظمة:

```python
from pydantic import BaseModel
from enum import Enum
from typing import List, Optional, Union
import json
import os
from typing import Optional
from pprint import pprint
from autogen_core.models import UserMessage, SystemMessage, AssistantMessage
from autogen_ext.models.azure import AzureAIChatCompletionClient
from azure.core.credentials import AzureKeyCredential

class AgentEnum(str, Enum):
    FlightBooking = "flight_booking"
    HotelBooking = "hotel_booking"
    CarRental = "car_rental"
    ActivitiesBooking = "activities_booking"
    DestinationInfo = "destination_info"
    DefaultAgent = "default_agent"
    GroupChatManager = "group_chat_manager"

# Travel SubTask Model
class TravelSubTask(BaseModel):
    task_details: str
    assigned_agent: AgentEnum  # we want to assign the task to the agent

class TravelPlan(BaseModel):
    main_task: str
    subtasks: List[TravelSubTask]
    is_greeting: bool

client = AzureAIChatCompletionClient(
    model="gpt-4o-mini",
    endpoint="https://models.inference.ai.azure.com",
    # To authenticate with the model you will need to generate a personal access token (PAT) in your GitHub settings.
    # Create your PAT token by following instructions here: https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens
    credential=AzureKeyCredential(os.environ["GITHUB_TOKEN"]),
    model_info={
        "json_output": False,
        "function_calling": True,
        "vision": True,
        "family": "unknown",
    },
)

# Define the user message
messages = [
    SystemMessage(content="""You are an planner agent.
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
    - DefaultAgent: For handling general requests""", source="system"),
    UserMessage(
        content="Create a travel plan for a family of 2 kids from Singapore to Melboune", source="user"),
]

response = await client.create(messages=messages, extra_create_args={"response_format": 'json_object'})

response_content: Optional[str] = response.content if isinstance(
    response.content, str) else None
if response_content is None:
    raise ValueError("Response content is not a valid JSON string" )

pprint(json.loads(response_content))

# # Ensure the response content is a valid JSON string before loading it
# response_content: Optional[str] = response.content if isinstance(
#     response.content, str) else None
# if response_content is None:
#     raise ValueError("Response content is not a valid JSON string")

# # Print the response content after loading it as JSON
# pprint(json.loads(response_content))

# Validate the response content with the MathReasoning model
# TravelPlan.model_validate(json.loads(response_content))
```

### وكيل التخطيط مع تنسيق متعدد الوكلاء

في هذا المثال، يتلقى وكيل التوجيه الدلالي طلب المستخدم (مثل "أحتاج إلى خطة فندق لرحلتي.").

ثم يقوم المخطط بما يلي:

* استلام خطة الفندق: يأخذ المخطط رسالة المستخدم وبناءً على موجه النظام (بما في ذلك تفاصيل الوكلاء المتاحة)، ينشئ خطة سفر منظمة.
* سرد الوكلاء وأدواتهم: يحتفظ سجل الوكلاء بقائمة من الوكلاء (مثل الطيران، الفنادق، استئجار السيارات، والأنشطة) مع الوظائف أو الأدوات التي يقدمونها.
* توجيه الخطة إلى الوكلاء المعنيين: بناءً على عدد المهام الفرعية، يقوم المخطط إما بإرسال الرسالة مباشرة إلى وكيل مخصص (للحالات ذات المهمة الواحدة) أو التنسيق عبر مدير دردشة جماعية للتعاون متعدد الوكلاء.
* تلخيص النتيجة: أخيرًا، يلخص المخطط الخطة الناتجة لتوضيحها.
يوضح مقتطف Python التالي هذه الخطوات:

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

# Travel SubTask Model

class TravelSubTask(BaseModel):
    task_details: str
    assigned_agent: AgentEnum # we want to assign the task to the agent

class TravelPlan(BaseModel):
    main_task: str
    subtasks: List[TravelSubTask]
    is_greeting: bool
import json
import os
from typing import Optional

from autogen_core.models import UserMessage, SystemMessage, AssistantMessage
from autogen_ext.models.openai import AzureOpenAIChatCompletionClient

# Create the client with type-checked environment variables

client = AzureOpenAIChatCompletionClient(
    azure_deployment=os.getenv("AZURE_OPENAI_DEPLOYMENT_NAME"),
    model=os.getenv("AZURE_OPENAI_DEPLOYMENT_NAME"),
    api_version=os.getenv("AZURE_OPENAI_API_VERSION"),
    azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"),
    api_key=os.getenv("AZURE_OPENAI_API_KEY"),
)

from pprint import pprint

# Define the user message

messages = [
    SystemMessage(content="""You are an planner agent.
    Your job is to decide which agents to run based on the user's request.
    Below are the available agents specialized in different tasks:
    - FlightBooking: For booking flights and providing flight information
    - HotelBooking: For booking hotels and providing hotel information
    - CarRental: For booking cars and providing car rental information
    - ActivitiesBooking: For booking activities and providing activity information
    - DestinationInfo: For providing information about destinations
    - DefaultAgent: For handling general requests""", source="system"),
    UserMessage(content="Create a travel plan for a family of 2 kids from Singapore to Melbourne", source="user"),
]

response = await client.create(messages=messages, extra_create_args={"response_format": TravelPlan})

# Ensure the response content is a valid JSON string before loading it

response_content: Optional[str] = response.content if isinstance(response.content, str) else None
if response_content is None:
    raise ValueError("Response content is not a valid JSON string")

# Print the response content after loading it as JSON

pprint(json.loads(response_content))
```

ما يلي هو المخرجات من الكود السابق ويمكنك بعد ذلك استخدام هذه المخرجات المنظمة لتوجيهها إلى `assigned_agent` وتلخيص خطة السفر للمستخدم النهائي.

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

يتوفر دفتر ملاحظات يحتوي على الكود السابق [هنا](07-autogen.ipynb).

### التخطيط التكراري

تتطلب بعض المهام تكرارًا أو إعادة تخطيط، حيث تؤثر نتيجة مهمة فرعية واحدة على المهمة التالية. على سبيل المثال، إذا اكتشف الوكيل تنسيق بيانات غير متوقع أثناء حجز الرحلات، فقد يحتاج إلى تعديل استراتيجيته قبل الانتقال إلى حجز الفنادق.

بالإضافة إلى ذلك، يمكن أن تؤدي ملاحظات المستخدم (مثل تفضيل الإنسان لرحلة مبكرة) إلى إعادة تخطيط جزئي. يضمن هذا النهج الديناميكي التكراري أن الحل النهائي يتماشى مع القيود الواقعية وتفضيلات المستخدم المتغيرة.

على سبيل المثال، كود عينة:

```python
from autogen_core.models import UserMessage, SystemMessage, AssistantMessage
#.. same as previous code and pass on the user history, current plan
messages = [
    SystemMessage(content="""You are a planner agent to optimize the
    Your job is to decide which agents to run based on the user's request.
    Below are the available agents specialized in different tasks:
    - FlightBooking: For booking flights and providing flight information
    - HotelBooking: For booking hotels and providing hotel information
    - CarRental: For booking cars and providing car rental information
    - ActivitiesBooking: For booking activities and providing activity information
    - DestinationInfo: For providing information about destinations
    - DefaultAgent: For handling general requests""", source="system"),
    UserMessage(content="Create a travel plan for a family of 2 kids from Singapore to Melbourne", source="user"),
    AssistantMessage(content=f"Previous travel plan - {TravelPlan}", source="assistant")
]
# .. re-plan and send the tasks to respective agents
```

للحصول على تخطيط أكثر شمولاً، تحقق من Magnetic One 

لحل المهام المعقدة.

## الملخص

في هذه المقالة، نظرنا في مثال على كيفية إنشاء مخطط يمكنه اختيار الوكلاء المتاحين بشكل ديناميكي. يقوم مخرجات المخطط بتقسيم المهام وتعيين الوكلاء بحيث يمكن تنفيذها. يُفترض أن الوكلاء لديهم إمكانية الوصول إلى الوظائف/الأدوات المطلوبة لأداء المهمة. بالإضافة إلى الوكلاء، يمكنك تضمين أنماط أخرى مثل الانعكاس، الملخص، والدردشة الدائرية لتخصيص إضافي.

## موارد إضافية

AutoGen Magnetic One - نظام متعدد الوكلاء عام لحل المهام المعقدة وقد حقق نتائج رائعة في العديد من معايير الوكلاء التحدي. المرجع:

. في هذا التنفيذ، يقوم المنسق بإنشاء خطة محددة للمهام وتفويض هذه المهام إلى الوكلاء المتاحين. بالإضافة إلى التخطيط، يستخدم المنسق أيضًا آلية تتبع لمراقبة تقدم المهمة وإعادة التخطيط حسب الحاجة.

### هل لديك المزيد من الأسئلة حول نمط تصميم التخطيط؟

انضم إلى [Discord الخاص بـ Azure AI Foundry](https://aka.ms/ai-agents/discord) للتواصل مع متعلمين آخرين، حضور ساعات المكتب، والحصول على إجابات لأسئلتك حول وكلاء الذكاء الاصطناعي.

## الدرس السابق

[بناء وكلاء ذكاء اصطناعي موثوقين](../06-building-trustworthy-agents/README.md)

## الدرس التالي

[نمط التصميم متعدد الوكلاء](../08-multi-agent/README.md)

---

**إخلاء المسؤولية**:  
تم ترجمة هذا المستند باستخدام خدمة الترجمة بالذكاء الاصطناعي [Co-op Translator](https://github.com/Azure/co-op-translator). بينما نسعى لتحقيق الدقة، يرجى العلم أن الترجمات الآلية قد تحتوي على أخطاء أو معلومات غير دقيقة. يجب اعتبار المستند الأصلي بلغته الأصلية المصدر الرسمي. للحصول على معلومات حاسمة، يُوصى بالاستعانة بترجمة بشرية احترافية. نحن غير مسؤولين عن أي سوء فهم أو تفسيرات خاطئة ناتجة عن استخدام هذه الترجمة.