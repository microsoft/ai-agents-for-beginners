[![Planning Design Pattern](../../../translated_images/ur/lesson-7-thumbnail.f7163ac557bea123.webp)](https://youtu.be/kPfJ2BrBCMY?si=9pYpPXp0sSbK91Dr)

> _(اس سبق کی ویڈیو دیکھنے کے لیے اوپر تصویر پر کلک کریں)_

# منصوبہ بندی کا ڈیزائن

## تعارف

یہ سبق درج ذیل موضوعات کا احاطہ کرے گا

* ایک واضح مجموعی مقصد کی تعریف اور ایک پیچیدہ کام کو قابلِ انتظام ذیلی کاموں میں تقسیم کرنا۔
* منظم آؤٹ پٹ کا استعمال تاکہ زیادہ قابلِ بھروسہ اور مشین پڑھنے کے قابل جوابات حاصل کیے جائیں۔
* ایک ایونٹ پر مبنی طریقہ کار کا اطلاق تاکہ متحرک کاموں اور غیر متوقع انپٹس کو سنبھالا جا سکے۔

## تعلیمی مقاصد

اس سبق کی تکمیل کے بعد، آپ کو درج ذیل باتوں کی سمجھ حاصل ہوگی:

* ایک AI ایجنٹ کے لیے ایک مجموعی ہدف کی شناخت اور تعین کرنا، یہ یقینی بناتے ہوئے کہ اسے واضح طور پر معلوم ہو کہ کیا حاصل کرنا ہے۔
* ایک پیچیدہ کام کو قابلِ انتظام ذیلی کاموں میں تقسیم کرنا اور انہیں منطقی ترتیب میں منظم کرنا۔
* ایجنٹس کو مناسب آلات (جیسے تلاش کے اوزار یا ڈیٹا انیلیٹکس کے اوزار) سے لیس کرنا، فیصلہ کرنا کہ کب اور کیسے استعمال کیے جائیں، اور غیر متوقع حالات کو سنبھالنا۔
* ذیلی کاموں کے نتائج کا جائزہ لینا، کارکردگی کی پیمائش کرنا، اور حتمی نتیجہ بہتر بنانے کے لیے کارروائیوں پر دوبارہ غور کرنا۔

## مجموعی ہدف کی تعریف اور کام کو توڑنا

![Defining Goals and Tasks](../../../translated_images/ur/defining-goals-tasks.d70439e19e37c47a.webp)

زیادہ تر حقیقی دنیا کے کام اتنے پیچیدہ ہوتے ہیں کہ انہیں ایک قدم میں مکمل نہیں کیا جا سکتا۔ ایک AI ایجنٹ کو اپنے منصوبہ بندی اور کارروائیوں کی رہنمائی کے لیے ایک مختصر مقصد کی ضرورت ہوتی ہے۔ مثال کے طور پر، ہدف کو غور کریں:

    "3 دن کا سفرنامہ تیار کریں۔"

اگرچہ یہ بیان کرنا آسان ہے، اس میں ابھی بھی اصلاح کی ضرورت ہے۔ جتنا زیادہ واضح ہدف ہوگا، ایجنٹ (اور کوئی بھی انسانی شریک کار) بہتر طریقے سے درست نتیجہ حاصل کرنے پر توجہ مرکوز کر سکے گا، جیسے کہ پرواز کے اختیارات، ہوٹل کی سفارشات، اور سرگرمیوں کی تجاویز کے ساتھ ایک جامع سفرنامہ تیار کرنا۔

### کام کی تقسیم

بڑے یا پیچیدہ کام چھوٹے، ہدف پر مبنی ذیلی کاموں میں تقسیم ہونے پر زیادہ قابلِ انتظام ہو جاتے ہیں۔
سفرنامہ کی مثال کے لیے، آپ اس ہدف کو تقسیم کر سکتے ہیں:

* پرواز کی بکنگ
* ہوٹل کی بکنگ
* کار کرایہ پر لینا
* ذاتی بنانا

ہر ذیلی کام کو پھر مخصوص ایجنٹس یا عمل کے ذریعے نمٹا جا سکتا ہے۔ ایک ایجنٹ بہترین پرواز کے سودا تلاش کرنے میں مہارت رکھتا ہے، دوسرا ہوٹل کی بکنگ پر توجہ دیتا ہے، وغیرہ۔ ایک ہم آہنگ کرنے والا یا "نیچے کی طرف" ایجنٹ پھر ان نتائج کو ایک مربوط سفرنامہ میں جمع کر کے آخر صارف تک پہنچا سکتا ہے۔

یہ ماڈیولر طریقہ کار بتدریج بہتری کی بھی اجازت دیتا ہے۔ مثال کے طور پر، آپ فوڈ کی سفارشات یا مقامی سرگرمیوں کی تجاویز کے لیے مخصوص ایجنٹس شامل کر سکتے ہیں اور وقت کے ساتھ سفرنامے کو بہتر بنا سکتے ہیں۔

### منظم آؤٹ پٹ

بڑے زبان کے ماڈلز (LLMs) منظم آؤٹ پٹ (جیسے JSON) پیدا کر سکتے ہیں جو نیچے کی طرف ایجنٹس یا خدمات کے لیے پارس اور پروسیس کرنا آسان ہوتا ہے۔ یہ خاص طور پر ایک کثیر ایجنٹ سیاق و سباق میں مفید ہے، جہاں ہم ان کاموں پر منصوبہ بندی کے آؤٹ پٹ کے موصول ہونے کے بعد عمل کر سکتے ہیں۔

درج ذیل پائتھان کا ٹکڑا ایک سادہ منصوبہ ساز ایجنٹ کو دکھاتا ہے جو ہدف کو ذیلی کاموں میں تقسیم کرتا ہے اور ایک منظم منصوبہ تیار کرتا ہے:

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

# ماڈل ضمنی کام برائے سفر
class TravelSubTask(BaseModel):
    task_details: str
    assigned_agent: AgentEnum  # ہم کام ایجنٹ کو تفویض کرنا چاہتے ہیں

class TravelPlan(BaseModel):
    main_task: str
    subtasks: List[TravelSubTask]
    is_greeting: bool

provider = FoundryChatClient(
    project_endpoint=os.environ["AZURE_AI_PROJECT_ENDPOINT"],
    model=os.environ["AZURE_AI_MODEL_DEPLOYMENT_NAME"],
    credential=AzureCliCredential(),
)

# صارف کا پیغام متعین کریں
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

### ملٹی ایجنٹ ہم آہنگی کے ساتھ منصوبہ ساز ایجنٹ

اس مثال میں، ایک سیمانٹک راؤٹر ایجنٹ صارف کی درخواست وصول کرتا ہے (مثلاً، "مجھے اپنی سفر کے لیے ہوٹل کا منصوبہ چاہیے۔").

منصوبہ ساز پھر:

* ہوٹل پلان وصول کرتا ہے: منصوبہ ساز صارف کا پیغام لیتا ہے اور ایک نظامی پرامپٹ کی بنیاد پر (جس میں دستیاب ایجنٹس کی تفصیلات شامل ہیں) ایک منظم سفر کا منصوبہ تیار کرتا ہے۔
* ایجنٹس اور ان کے آلات کی فہرست دیتا ہے: ایجنٹ رجسٹری ایجنٹس کی فہرست رکھتی ہے (مثلاً پرواز، ہوٹل، کار کرایہ، اور سرگرمیاں) اور وہ فنکشنز یا آلات جو وہ فراہم کرتے ہیں۔
* منصوبہ متعلقہ ایجنٹس کو بھیجتا ہے: ذیلی کاموں کی تعداد کے لحاظ سے، منصوبہ ساز پیغام کو براہ راست مخصوص ایجنٹ کو بھیجتا ہے (سنگل ٹاسک کے حالات میں) یا کثیر ایجنٹ تعاون کے لیے گروپ چیٹ مینیجر کے ذریعے ہم آہنگی کرتا ہے۔
* نتیجہ کا خلاصہ کرتا ہے: آخر میں، منصوبہ ساز وضاحت کے لیے تیار کردہ منصوبے کا خلاصہ کرتا ہے۔
درج ذیل پائتھان کوڈ ان مراحل کی وضاحت کرتا ہے:

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

# ماڈل ضمنی سفر کا

class TravelSubTask(BaseModel):
    task_details: str
    assigned_agent: AgentEnum # ہم ایجنٹ کو کام تفویض کرنا چاہتے ہیں

class TravelPlan(BaseModel):
    main_task: str
    subtasks: List[TravelSubTask]
    is_greeting: bool
import json
import os
from typing import Optional

from agent_framework.foundry import FoundryChatClient
from azure.identity import AzureCliCredential

# کلائنٹ بنائیں

provider = FoundryChatClient(
    project_endpoint=os.environ["AZURE_AI_PROJECT_ENDPOINT"],
    model=os.environ["AZURE_AI_MODEL_DEPLOYMENT_NAME"],
    credential=AzureCliCredential(),
)

from pprint import pprint

# صارف کا پیغام متعین کریں

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

# JSON کے طور پر لوڈ کرنے کے بعد جواب کا مواد پرنٹ کریں

pprint(json.loads(response_content))
```

جو کچھ نیچے ہے وہ پچھلے کوڈ کا آؤٹ پٹ ہے اور آپ پھر اس منظم آؤٹ پٹ کو `assigned_agent` کو بھیجنے اور سفر کے منصوبے کو آخری صارف تک پہنچانے کے لیے استعمال کر سکتے ہیں۔

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

ایک مثال نوٹ بک جس میں پچھلا کوڈ نمونہ شامل ہے، دستیاب ہے [یہاں](./code_samples/07-python-agent-framework.ipynb)۔

### تکراری منصوبہ بندی

کچھ کام پیچھے پیچھے یا دوبارہ منصوبہ بندی کا تقاضا کرتے ہیں، جہاں ایک ذیلی کام کا نتیجہ اگلے کو متاثر کرتا ہے۔ مثلاً، اگر ایجنٹ پروازوں کی بکنگ کے دوران غیر متوقع ڈیٹا فارمیٹ دریافت کرتا ہے، تو اسے ہوٹل کی بکنگ شروع کرنے سے پہلے اپنی حکمت عملی کو ایڈجسٹ کرنا پڑ سکتا ہے۔

مزید برآں، صارف کی رائے (مثلاً ایک انسان کا فیصلہ کہ وہ جلدی پرواز پسند کرتا ہے) جزوی دوبارہ منصوبہ بندی کو متحرک کر سکتی ہے۔ یہ متحرک، تکراری طریقہ کار یقینی بناتا ہے کہ حتمی حل حقیقی دنیا کی حدود اور بدلتی ہوئی صارف کی ترجیحات کے مطابق ہو۔

مثلاً نمونہ کوڈ

```python
import os
from agent_framework.foundry import FoundryChatClient
from azure.identity import AzureCliCredential
#.. سابقہ کوڈ کی طرح اور صارف کی تاریخ، موجودہ منصوبہ فراہم کریں

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
# .. دوبارہ منصوبہ بندی کریں اور کام متعلقہ ایجنٹوں کو بھیجیں
```

جامع منصوبہ بندی کے لیے، پیچیدہ کاموں کے حل کے لیے Magnetic One کا <a href="https://www.microsoft.com/research/articles/magentic-one-a-generalist-multi-agent-system-for-solving-complex-tasks" target="_blank">بلاگ پوسٹ</a> دیکھیں۔

## خلاصہ

اس مضمون میں ہم نے دیکھا ہے کہ ہم کیسے ایک ایسا منصوبہ ساز بنا سکتے ہیں جو دستیاب ایجنٹس کو متحرک طور پر منتخب کر سکے۔ منصوبہ ساز کا آؤٹ پٹ کاموں کو تقسیم کرتا ہے اور ایجنٹس کو تفویض کرتا ہے تاکہ وہ عمل درآمد کر سکیں۔ فرض کیا جاتا ہے کہ ایجنٹس کے پاس وہ فنکشنز/آلات موجود ہیں جو کام انجام دینے کے لیے ضروری ہیں۔ ایجنٹس کے علاوہ آپ عکاسی، خلاصہ ساز، اور راؤنڈ رابن چیٹ جیسے دیگر پیٹرنز بھی شامل کر سکتے ہیں تاکہ مزید تخصیص کی جا سکے۔

## اضافی ذرائع

Magentic One - پیچیدہ کاموں کے حل کے لیے ایک جنرلِسٹ کثیر ایجنٹ سسٹم ہے جس نے متعدد چیلنجنگ ایجنٹک بنچ مارکس پر شاندار نتائج حاصل کیے ہیں۔ حوالہ: <a href="https://www.microsoft.com/research/articles/magentic-one-a-generalist-multi-agent-system-for-solving-complex-tasks" target="_blank">Magentic One</a>۔ اس نفاذ میں، ہم آہنگ کنندہ مخصوص کاموں کے منصوبے بناتا ہے اور ان کاموں کو دستیاب ایجنٹس کو تفویض کرتا ہے۔ منصوبہ بندی کے علاوہ، ہم آہنگ کنندہ کام کی پیش رفت کی نگرانی کے لیے ایک ٹریکنگ میکانزم بھی استعمال کرتا ہے اور ضرورت پڑنے پر دوبارہ منصوبہ بندی کرتا ہے۔

### منصوبہ بندی کے ڈیزائن پیٹرن کے بارے میں مزید سوالات ہیں؟

مزید سیکھنے والوں سے ملنے، آفس آورز میں شرکت کرنے اور اپنے AI ایجنٹس کے سوالات کے جوابات حاصل کرنے کے لیے [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D) میں شامل ہوں۔

## پچھلا سبق

[قابلِ بھروسہ AI ایجنٹس کی تعمیر](../06-building-trustworthy-agents/README.md)

## اگلا سبق

[کثیر ایجنٹ ڈیزائن پیٹرن](../08-multi-agent/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ڈس کلیمر**:
یہ دستاویز AI ترجمہ سروس [Co-op Translator](https://github.com/Azure/co-op-translator) کے ذریعے ترجمہ کی گئی ہے۔ جبکہ ہم درستگی کے لیے کوشاں ہیں، براہ کرم اس بات سے آگاہ رہیں کہ خودکار ترجمے میں غلطیاں یا عدم درستیاں ہو سکتی ہیں۔ اصل دستاویز اپنے مادری زبان میں مستند ماخذ سمجھی جائے گی۔ حساس معلومات کے لیے پیشہ ور انسانی ترجمہ کی سفارش کی جاتی ہے۔ اس ترجمے کے استعمال سے پیدا ہونے والی کسی بھی غلط فہمی یا غلط تشریح کی ذمہ داری ہم قبول نہیں کرتے۔
<!-- CO-OP TRANSLATOR DISCLAIMER END -->