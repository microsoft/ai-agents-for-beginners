[![پلاننگ ڈیزائن پیٹرن](../../../translated_images/ur/lesson-7-thumbnail.f7163ac557bea123.webp)](https://youtu.be/kPfJ2BrBCMY?si=9pYpPXp0sSbK91Dr)

> _(اوپر تصویر پر کلک کریں تاکہ اس سبق کی ویڈیو دیکھیں)_

# پلاننگ ڈیزائن

## تعارف

یہ سبق درج ذیل موضوعات کا احاطہ کرے گا

* ایک واضح مجموعی ہدف کی تعریف اور ایک پیچیدہ کام کو قابلِ منظم حصوں میں تقسیم کرنا۔
* زیادہ قابلِ بھروسہ اور مشین-قابلِ مطالعہ جوابات کے لئے منظم آؤٹ پٹ کا فائدہ اٹھانا۔
* متحرک کاموں اور غیر متوقع ان پٹس کو ہینڈل کرنے کے لیے ایونٹ-ڈرائیون طریقہ کار کا اطلاق۔

## سیکھنے کے مقاصد

اس سبق کو مکمل کرنے کے بعد، آپ درج ذیل چیزوں کی سمجھ رکھتے ہوں گے:

* AI ایجنٹ کے لیے ایک مجموعی ہدف کی شناخت اور تعین کرنا، تاکہ وہ واضح طور پر جان سکے کہ کیا حاصل کرنا ہے۔
* ایک پیچیدہ کام کو قابلِ انتظام ذیلی کاموں میں توڑنا اور انہیں منطقی ترتیب میں منظم کرنا۔
* ایجنٹس کو مناسب ٹولز (مثلاً سرچ ٹولز یا ڈیٹا اینالیٹکس ٹولز) سے لیس کرنا، یہ فیصلہ کرنا کہ کب اور کیسے استعمال کریں، اور جو غیر متوقع حالات پیش آئیں ان کو ہینڈل کرنا۔
* ذیلی کاموں کے نتائج کا جائزہ لینا، کارکردگی کو ناپنا، اور حتمی آؤٹ پٹ کو بہتر بنانے کے لیے اقدامات پر نظرثانی کرنا۔

## مجموعی ہدف کی تعریف اور کام کو ٹکڑوں میں بانٹنا

![اہداف اور کاموں کی تعریف](../../../translated_images/ur/defining-goals-tasks.d70439e19e37c47a.webp)

زیادہ تر حقیقی دنیا کے کام ایک قدم میں نمٹانے کے لیے بہت پیچیدہ ہوتے ہیں۔ ایک AI ایجنٹ کو اپنے منصوبہ بندی اور اقدامات کی رہنمائی کے لیے ایک جامع مقصد درکار ہوتا ہے۔ مثال کے طور پر، درج ذیل ہدف پر غور کریں:

    "3 دن کا سفرنامہ تیار کریں."

اگرچہ یہ بیان کرنا آسان ہے، پھر بھی اسے بہتر بنانے کی ضرورت ہے۔ جتنا واضح ہدف ہوگا، اتنا ہی بہتر ایجنٹ (اور کوئی بھی انسانی معاون) درست نتیجہ حاصل کرنے پر توجہ مرکوز کر سکتا ہے، جیسے کہ پرواز کے اختیارات، ہوٹل کی سفارشات، اور سرگرمیوں کی تجاویز کے ساتھ ایک جامع سفرنامہ تیار کرنا۔

### کاموں کی تقسیم

بڑے یا پیچیدہ کام چھوٹے، ہدف-مرکوز ذیلی کاموں میں تقسیم کرنے پر زیادہ قابلِ انتظام ہو جاتے ہیں۔
سفرنامہ کی مثال کے لیے، آپ ہدف کو درج ذیل ذیلی کاموں میں تقسیم کر سکتے ہیں:

* پرواز کی بکنگ
* ہوٹل کی بکنگ
* کار کرایہ
* شخصی سازی

ہر ذیلی کام کو پھر مخصوص ایجنٹس یا عمل کے ذریعے نمٹایا جا سکتا ہے۔ ایک ایجنٹ بہترین پرواز کے سودے تلاش کرنے میں مہارت رکھ سکتا ہے، دوسرا ہوٹل بکنگ پر توجہ مرکوز کرتا ہے، وغیرہ۔ ایک کوآرڈینیٹنگ یا "ڈاؤن اسٹریم" ایجنٹ پھر ان نتائج کو یکجا کر کے ایک مربوط سفرنامہ صارف تک پہنچا سکتا ہے۔

یہ ماڈیولر طریقہ کار بتدریج بہتریوں کی بھی اجازت دیتا ہے۔ مثال کے طور پر، آپ فوڈ سفارشات یا مقامی سرگرمیوں کی تجاویز کے لیے مخصوص ایجنٹس شامل کر سکتے ہیں اور وقت کے ساتھ سفرنامہ کو بہتر بنا سکتے ہیں۔

### Structured output

Large Language Models (LLMs) ساختہ آؤٹ پٹ (مثلاً JSON) تیار کر سکتے ہیں جو ڈاؤن اسٹریم ایجنٹس یا سروسز کے لیے پارس اور پراسیس کرنے میں آسان ہوتا ہے۔ یہ خاص طور پر کثیر-ایجنٹ منظرنامے میں مفید ہے، جہاں ہم پلاننگ آؤٹ پٹ موصول ہونے کے بعد ان کاموں پر عمل کر سکتے ہیں۔

مندرجہ ذیل Python کا ٹکڑا ایک سادہ پلاننگ ایجنٹ دکھاتا ہے جو مقصد کو ذیلی کاموں میں تقسیم کرتا ہے اور ایک ساختہ منصوبہ تیار کرتا ہے:

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

# سفر کے ضمنی کام کا ماڈل
class TravelSubTask(BaseModel):
    task_details: str
    assigned_agent: AgentEnum  # ہم چاہتے ہیں کہ یہ کام ایجنٹ کو تفویض کیا جائے

class TravelPlan(BaseModel):
    main_task: str
    subtasks: List[TravelSubTask]
    is_greeting: bool

provider = AzureAIProjectAgentProvider(credential=AzureCliCredential())

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

### پلاننگ ایجنٹ بمعہ ملٹی-ایجنٹ آرکسٹریکشن

اس مثال میں، ایک Semantic Router Agent ایک صارف کی درخواست وصول کرتا ہے (مثلاً، "I need a hotel plan for my trip.")۔

پلانر پھر:

* ہوٹل پلان وصول کرتا ہے: پلانر صارف کا پیغام لیتا ہے اور سسٹم پرامپٹ (جس میں دستیاب ایجنٹس کی تفصیلات شامل ہیں) کی بنیاد پر ایک ساختہ سفر منصوبہ تیار کرتا ہے۔
* ایجنٹس اور ان کے ٹولز کی فہرست بناتا ہے: ایجنٹ رجسٹری میں ایجنٹس کی فہرست ہوتی ہے (مثلاً پرواز، ہوٹل، کار کرایہ، اور سرگرمیاں) ساتھ میں وہ فنکشنز یا ٹولز جو وہ پیش کرتے ہیں۔
* منصوبہ متعلقہ ایجنٹس کو روٹ کرتا ہے: ذیلی کاموں کی تعداد کے لحاظ سے، پلانر یا تو پیغام براہِ راست مخصوص ایجنٹ کو بھیجتا ہے (سنگل-ٹاسک منظرناموں کے لیے) یا ملٹی-ایجنٹ تعاون کے لیے گروپ چیٹ مینیجر کے ذریعے ہم آہنگی کرتا ہے۔
* نتیجہ کا خلاصہ کرتا ہے: آخر میں، پلانر وضاحت کے لیے تیار کردہ منصوبے کا خلاصہ کرتا ہے۔
مندرجہ ذیل Python کوڈ کا نمونہ ان مراحل کی وضاحت کرتا ہے:

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

# سفر ذیلی کام ماڈل

class TravelSubTask(BaseModel):
    task_details: str
    assigned_agent: AgentEnum # ہم اس کام کو ایجنٹ کو تفویض کرنا چاہتے ہیں

class TravelPlan(BaseModel):
    main_task: str
    subtasks: List[TravelSubTask]
    is_greeting: bool
import json
import os
from typing import Optional

from agent_framework.azure import AzureAIProjectAgentProvider
from azure.identity import AzureCliCredential

# کلائنٹ بنائیں

provider = AzureAIProjectAgentProvider(credential=AzureCliCredential())

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

# جوابی مواد کو JSON کے طور پر لوڈ کرنے کے بعد پرنٹ کریں

pprint(json.loads(response_content))
```

What follows is the output from the previous code and you can then use this structured output to route to `assigned_agent` and summarize the travel plan to the end user.

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

An example notebook with the previous code sample is available [یہاں](07-python-agent-framework.ipynb).

### تکراری منصوبہ بندی

کچھ کام بیک اینڈ فورتھ یا دوبارہ منصوبہ بندی کی ضرورت رکھتے ہیں، جہاں ایک ذیلی کام کا نتیجہ اگلے پر اثر انداز ہوتا ہے۔ مثال کے طور پر، اگر ایجنٹ پروازیں بک کرنے کے دوران غیر متوقع ڈیٹا فارمیٹ دریافت کرتا ہے، تو اسے ہوٹل بکیگز پر جانے سے پہلے اپنی حکمتِ عملی کو اپنانے کی ضرورت پڑ سکتی ہے۔

مزید برآں، صارف کی رائے (مثلاً ایک انسان کا فیصلہ کہ وہ پہلے والی پرواز کو ترجیح دیتا ہے) جزوی دوبارہ منصوبہ بندی کو متحرک کر سکتی ہے۔ یہ متحرک، تکراری طریقہ کار یقینی بناتا ہے کہ حتمی حل حقیقی دنیا کی پابندیوں اور بدلتی ہوئی صارف ترجیحات کے مطابق ہو۔

مثال کے طور پر نمونہ کوڈ

```python
from agent_framework.azure import AzureAIProjectAgentProvider
from azure.identity import AzureCliCredential
#.. پچھلے کوڈ کی طرح ہی اور صارف کی ہسٹری اور موجودہ منصوبہ منتقل کریں

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
# .. دوبارہ منصوبہ بندی کریں اور کام متعلقہ ایجنٹس کو بھیجیں
```

مزید جامع منصوبہ بندی کے لیے پیچیدہ کام حل کرنے کے لیے Magnetic One کی <a href="https://www.microsoft.com/research/articles/magentic-one-a-generalist-multi-agent-system-for-solving-complex-tasks" target="_blank">بلاگ پوسٹ</a> دیکھیں۔

## خلاصہ

اس مضمون میں ہم نے ایک ایسے پلانر کی مثال دیکھی ہے جو متحرک طور پر دستیاب درج شدہ ایجنٹس کا انتخاب کر سکتا ہے۔ پلانر کا آؤٹ پٹ کاموں کو تقسیم کرتا ہے اور ایجنٹس کو تفویض کرتا ہے تاکہ وہ انجام دیے جا سکیں۔ فرض کیا جاتا ہے کہ ایجنٹس کے پاس وہ فنکشنز/ٹولز تک رسائی ہے جو کام انجام دینے کے لیے ضروری ہیں۔ ایجنٹس کے علاوہ آپ مزید حسبِ ضرورت نمونوں کو شامل کر سکتے ہیں جیسے reflection، summarizer، اور round robin chat۔

## اضافی وسائل

Magentic One - A Generalist multi-agent system for solving complex tasks اور اس نے متعدد چیلنجنگ ایجینٹک بینچ مارکس پر متاثر کن نتائج حاصل کیے ہیں۔ حوالہ: <a href="https://www.microsoft.com/research/articles/magentic-one-a-generalist-multi-agent-system-for-solving-complex-tasks" target="_blank">Magentic One</a>۔ اس عمل کاری میں آرکسٹریٹر مخصوص منصوبے بناتا ہے اور ان کاموں کو دستیاب ایجنٹس کو سونپ دیتا ہے۔ منصوبہ بندی کے علاوہ آرکسٹریٹر ایک ٹریکنگ میکنزم بھی استعمال کرتا ہے تاکہ کام کی پیش رفت کی نگرانی کی جا سکے اور ضرورت کے مطابق دوبارہ منصوبہ بندی کی جا سکے۔

### کیا آپ پلاننگ ڈیزائن پیٹرن کے بارے میں مزید سوالات رکھتے ہیں؟

Join the [Microsoft Foundry Discord](https://aka.ms/ai-agents/discord) to meet with other learners, attend office hours and get your AI Agents questions answered.

## پچھلا سبق

[قابل اعتماد AI ایجنٹس کی تعمیر](../06-building-trustworthy-agents/README.md)

## اگلا سبق

[کثیر ایجنٹ ڈیزائن پیٹرن](../08-multi-agent/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
ردِ ذمہ داری:

یہ دستاویز مصنوعی ذہانت کی ترجمہ سروس Co‑op Translator (https://github.com/Azure/co-op-translator) کے ذریعے ترجمہ کی گئی ہے۔ اگرچہ ہم درستگی کے لیے کوشاں ہیں، براہِ کرم خیال رکھیں کہ خودکار تراجم میں غلطیاں یا غیر درستیاں ہو سکتی ہیں۔ اصل دستاویز کو اس کی مقامی زبان میں ہی معتبر ماخذ سمجھا جائے۔ اہم معلومات کے لیے پیشہ ور انسانی مترجم سے ترجمہ کروانا تجویز کیا جاتا ہے۔ اس ترجمے کے استعمال سے پیدا ہونے والی کسی بھی غلط فہمی یا غلط تعبیر کے لیے ہم ذمہ دار نہیں ہوں گے۔
<!-- CO-OP TRANSLATOR DISCLAIMER END -->