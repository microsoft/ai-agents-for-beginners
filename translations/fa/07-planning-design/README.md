[![الگوی طراحی برنامه‌ریزی](../../../translated_images/fa/lesson-7-thumbnail.f7163ac557bea123.webp)](https://youtu.be/kPfJ2BrBCMY?si=9pYpPXp0sSbK91Dr)

> _(برای مشاهده ویدیو این درس روی تصویر بالا کلیک کنید)_

# برنامه‌ریزی طراحی

## مقدمه

این درس موارد زیر را پوشش می‌دهد:

* تعریف هدف کلی واضح و شکستن یک کار پیچیده به وظایف قابل مدیریت.
* استفاده از خروجی ساخت‌یافته برای پاسخ‌های قابل اطمینان‌تر و قابل خواندن توسط ماشین.
* به‌کارگیری رویکرد رویدادمحور برای مدیریت وظایف پویا و ورودی‌های غیرمنتظره.

## اهداف یادگیری

پس از تکمیل این درس، شما با موارد زیر آشنا خواهید شد:

* شناسایی و تعیین هدف کلی برای یک عامل هوش مصنوعی، به نحوی که به‌وضوح بداند چه چیزی باید به دست آید.
* تجزیه یک کار پیچیده به وظایف فرعی قابل مدیریت و سازماندهی آن‌ها در یک توالی منطقی.
* تجهیز عوامل به ابزارهای مناسب (مثلاً ابزارهای جستجو یا ابزارهای تحلیل داده)، تعیین زمان و نحوه استفاده از آن‌ها و مدیریت موقعیت‌های غیرمنتظره‌ای که پیش می‌آید.
* ارزیابی نتایج وظایف فرعی، اندازه‌گیری عملکرد و تکرار اقدامات برای بهبود خروجی نهایی.

## تعریف هدف کلی و شکستن یک کار

![تعریف اهداف و وظایف](../../../translated_images/fa/defining-goals-tasks.d70439e19e37c47a.webp)

اکثر وظایف دنیای واقعی به قدری پیچیده‌اند که نمی‌توان در یک مرحله آن‌ها را انجام داد. یک عامل هوش مصنوعی به یک هدف مختصر نیاز دارد تا برنامه‌ریزی و اقدامات خود را هدایت کند. برای مثال، هدف زیر را در نظر بگیرید:

    "تهیه برنامه سفر ۳ روزه."

اگرچه بیان آن ساده است، اما هنوز نیاز به تصحیحات دارد. هر چه هدف واضح‌تر باشد، عامل (و هر همکار انسانی) بهتر می‌تواند بر دستیابی به نتیجه صحیح تمرکز کند، مثلا ایجاد یک برنامه جامع با گزینه‌های پرواز، توصیه‌های هتل و پیشنهادات فعالیت‌ها.

### تجزیه وظیفه

وظایف بزرگ یا پیچیده زمانی که به وظایف فرعی کوچکتر و هدفمند تقسیم شوند، قابل مدیریت‌تر می‌شوند.
برای مثال برنامه سفر، می‌توانید هدف را به موارد زیر تقسیم کنید:

* رزرو پرواز
* رزرو هتل
* اجاره خودرو
* شخصی‌سازی

سپس هر وظیفه فرعی می‌تواند توسط عوامل یا فرآیندهای اختصاصی انجام شود. یک عامل ممکن است در جستجوی بهترین تخفیف‌های پرواز تخصص داشته باشد، دیگری بر رزرو هتل تمرکز کند و غیره. یک عامل هماهنگ‌کننده یا «فراگیر» سپس این نتایج را در یک برنامه یکپارچه برای کاربر نهایی ترکیب می‌کند.

این رویکرد مدولار امکان بهبود تدریجی را نیز فراهم می‌کند. به عنوان مثال، می‌توانید عوامل تخصصی برای توصیه‌های غذایی یا پیشنهادات فعالیت‌های محلی اضافه کرده و برنامه را به مرور زمان بهبود دهید.

### خروجی ساخت‌یافته

مدل‌های زبان بزرگ (LLMها) می‌توانند خروجی ساخت‌یافته (مثلاً JSON) تولید کنند که برای عوامل یا خدمات پایین‌دستی آسان‌تر برای تجزیه و پردازش است. این خصوصاً در زمینه چند عامله مفید است، جایی که می‌توانیم پس از دریافت خروجی برنامه‌ریزی، این وظایف را اجرا کنیم.

قطعه کد پایتون زیر یک عامل برنامه‌ریز ساده را نشان می‌دهد که یک هدف را به وظایف فرعی تقسیم کرده و یک برنامه ساخت‌یافته تولید می‌کند:

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

# مدل زیرکار سفر
class TravelSubTask(BaseModel):
    task_details: str
    assigned_agent: AgentEnum  # ما می‌خواهیم این کار را به نماینده واگذار کنیم

class TravelPlan(BaseModel):
    main_task: str
    subtasks: List[TravelSubTask]
    is_greeting: bool

provider = AzureAIProjectAgentProvider(credential=AzureCliCredential())

# تعریف پیام کاربر
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

### عامل برنامه‌ریز با هماهنگی چند عامله

در این مثال، یک عامل مسیریاب معنایی درخواست کاربر را دریافت می‌کند (مثلاً «من به یک برنامه هتل برای سفرم نیاز دارم.»).

برنامه‌ریز سپس:

* دریافت برنامه هتل: برنامه‌ریز پیام کاربر را دریافت می‌کند و بر اساس پرسش سیستم (شامل جزئیات عوامل موجود)، یک برنامه سفر ساخت‌یافته تولید می‌کند.
* فهرست کردن عوامل و ابزارهای آنها: ثبت عامل‌ها فهرستی از عوامل (مثلاً برای پرواز، هتل، اجاره خودرو و فعالیت‌ها) همراه با توابع یا ابزارهای آن‌ها در اختیار دارد.
* ارسال برنامه به عوامل مربوطه: بسته به تعداد وظایف فرعی، برنامه‌ریز یا پیام را مستقیماً به یک عامل اختصاصی (برای سناریوهای تک وظیفه‌ای) می‌فرستد یا از طریق مدیر گروه گفتگو برای همکاری چند عامله هماهنگ می‌کند.
* خلاصه‌سازی نتیجه: در نهایت، برنامه‌ریز برنامه ایجاد شده را برای وضوح خلاصه می‌کند.
نمونه کد پایتون زیر این مراحل را نشان می‌دهد:

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

# مدل زیروظیفه سفر

class TravelSubTask(BaseModel):
    task_details: str
    assigned_agent: AgentEnum # می‌خواهیم وظیفه را به عامل تخصیص دهیم

class TravelPlan(BaseModel):
    main_task: str
    subtasks: List[TravelSubTask]
    is_greeting: bool
import json
import os
from typing import Optional

from agent_framework.azure import AzureAIProjectAgentProvider
from azure.identity import AzureCliCredential

# ایجاد کلاینت

provider = AzureAIProjectAgentProvider(credential=AzureCliCredential())

from pprint import pprint

# تعریف پیام کاربر

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

# چاپ محتوای پاسخ پس از بارگذاری آن به صورت JSON

pprint(json.loads(response_content))
```

آنچه در ادامه می‌آید خروجی کد قبلی است و شما می‌توانید از این خروجی ساختاریافته برای ارسال به `assigned_agent` و خلاصه کردن برنامه سفر به کاربر نهایی استفاده کنید.

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

دفترچه نمونه‌ای با نمونه کد فوق [اینجا](07-python-agent-framework.ipynb) موجود است.

### برنامه‌ریزی تکراری

برخی وظایف نیاز به رفت و برگشت یا برنامه‌ریزی مجدد دارند، جایی که نتیجه یک وظیفه فرعی بر وظیفه بعدی تأثیر می‌گذارد. برای مثال، اگر عامل هنگام رزرو پروازها با قالب داده ناشناخته‌ای مواجه شود، ممکن است نیاز داشته باشد استراتژی خود را تغییر دهد قبل از ادامه به رزرو هتل‌ها.

علاوه بر این، بازخورد کاربر (مثلاً تصمیم یک انسان به ترجیح پرواز زودتر) می‌تواند باعث برنامه‌ریزی مجدد جزئی شود. این رویکرد پویا و تکراری اطمینان می‌دهد که راه‌حل نهایی با محدودیت‌های دنیای واقعی و ترجیحات در حال تغییر کاربر سازگار باشد.

مثال کد

```python
from agent_framework.azure import AzureAIProjectAgentProvider
from azure.identity import AzureCliCredential
#.. مشابه کد قبلی و ارسال تاریخچه کاربر، برنامه فعلی

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
# .. برنامه‌ریزی مجدد و ارسال وظایف به نمایندگان مربوطه
```

برای برنامه‌ریزی جامع‌تر، پست وبلاگی Magnetic One را بررسی کنید <a href="https://www.microsoft.com/research/articles/magentic-one-a-generalist-multi-agent-system-for-solving-complex-tasks" target="_blank">اینجا</a> برای حل وظایف پیچیده.

## خلاصه

در این مقاله نمونه‌ای مشاهده کردیم که چگونه می‌توانیم یک برنامه‌ریز ایجاد کنیم که بتواند عوامل موجود تعریف‌شده را به طور پویا انتخاب کند. خروجی برنامه‌ریز وظایف را تجزیه کرده و عوامل را تخصیص می‌دهد تا بتوانند اجرا شوند. فرض بر این است که عوامل به توابع / ابزارهای لازم برای انجام کار دسترسی دارند. علاوه بر عوامل می‌توانید الگوهای دیگری مانند بازتاب، خلاصه‌ساز و گفتگو به صورت نوبتی را برای سفارشی‌سازی بیشتر اضافه کنید.

## منابع اضافی

Magnetic One - یک سیستم چند عامله عمومی برای حل وظایف پیچیده که نتایج چشمگیری در معیارهای چند عامله چالش‌برانگیز کسب کرده است. منبع: <a href="https://www.microsoft.com/research/articles/magentic-one-a-generalist-multi-agent-system-for-solving-complex-tasks" target="_blank">Magnetic One</a>. در این پیاده‌سازی، هماهنگ‌کننده طرح‌های خاص وظایف را ایجاد کرده و این وظایف را به عوامل موجود محول می‌کند. علاوه بر برنامه‌ریزی، هماهنگ‌کننده مکانیزم پیگیری برای نظارت بر پیشرفت وظیفه به‌کار می‌برد و در صورت نیاز برنامه‌ریزی مجدد انجام می‌دهد.

### سوال بیشتری درباره الگوی طراحی برنامه‌ریزی دارید؟

در [دیسکورد مایکروسافت فاندری](https://aka.ms/ai-agents/discord) عضو شوید تا با دیگر یادگیرندگان ملاقات کنید، در ساعت‌های مشاوره شرکت کنید و سوالات خود درباره عوامل هوش مصنوعی را پاسخ بگیرید.

## درس قبلی

[ساخت عوامل هوش مصنوعی قابل اعتماد](../06-building-trustworthy-agents/README.md)

## درس بعدی

[الگوی طراحی چند عامله](../08-multi-agent/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**تذکر مهم**:  
این سند با استفاده از سرویس ترجمه هوش مصنوعی [Co-op Translator](https://github.com/Azure/co-op-translator) ترجمه شده است. در حالی که ما در تلاش برای دقت بالا هستیم، لطفاً توجه داشته باشید که ترجمه‌های خودکار ممکن است دارای خطاها یا نواقصی باشند. سند اصلی به زبان مادری خود منبع معتبر محسوب می‌شود. برای اطلاعات حساس و حیاتی، ترجمه حرفه‌ای انسانی توصیه می‌شود. ما در قبال هرگونه سوتفاهم یا برداشت نادرست ناشی از استفاده از این ترجمه مسئولیتی نداریم.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->