[![الگوی طراحی برنامه‌ریزی](../../../translated_images/fa/lesson-7-thumbnail.f7163ac557bea123.webp)](https://youtu.be/kPfJ2BrBCMY?si=9pYpPXp0sSbK91Dr)

> _(برای مشاهده ویدیوی این درس روی تصویر بالا کلیک کنید)_

# طراحی برنامه‌ریزی

## مقدمه

این درس شامل موارد زیر است

* تعریف هدف کلی واضح و تقسیم یک کار پیچیده به کارهای قابل مدیریت.
* بهره‌گیری از خروجی ساختاریافته برای پاسخ‌های قابل اطمینان‌تر و قابل خواندن توسط ماشین.
* به‌کارگیری رویکرد رویداد-محور برای مدیریت کارهای پویا و ورودی‌های غیرمنتظره.

## اهداف یادگیری

پس از تکمیل این درس، شما درک خواهید داشت از:

* شناسایی و تعیین هدف کلی برای یک عامل هوش مصنوعی، به گونه‌ای که به‌روشنی بداند چه چیزی باید به دست آید.
* تجزیه یک کار پیچیده به زیرکارهای قابل مدیریت و سازماندهی آن‌ها در یک توالی منطقی.
* تجهیز عوامل با ابزارهای مناسب (مثلاً ابزارهای جستجو یا ابزارهای تحلیل داده)، تصمیم‌گیری درباره زمان و نحوه استفاده از آن‌ها، و مدیریت موقعیت‌های غیرمنتظره که پیش می‌آید.
* ارزیابی نتایج زیرکارها، اندازه‌گیری عملکرد و تکرار اقدامات برای بهبود خروجی نهایی.

## تعریف هدف کلی و تجزیه یک کار

![تعریف اهداف و کارها](../../../translated_images/fa/defining-goals-tasks.d70439e19e37c47a.webp)

بیشتر کارهای دنیای واقعی برای انجام در یک مرحله خیلی پیچیده هستند. یک عامل هوش مصنوعی نیازمند یک هدف مختصر است که برنامه‌ریزی و اقداماتش را هدایت کند. به عنوان مثال، هدف زیر را در نظر بگیرید:

    "ایجاد یک برنامه سفر ۳ روزه."

اگرچه بیان آن ساده است، اما هنوز نیاز به پالایش دارد. هرچه هدف واضح‌تر باشد، عامل (و هر همکار انسانی) بهتر می‌تواند بر رسیدن به نتیجه مناسب متمرکز شود، مثلاً ایجاد یک برنامه جامع با گزینه‌های پرواز، توصیه‌های هتل و پیشنهادهای فعالیت‌ها.

### تجزیه کار

کارهای بزرگ یا پیچیده وقتی به زیرکارهای کوچک‌تر و هدفمند تقسیم شوند، قابل مدیریت‌تر می‌شوند.
برای مثال برنامه سفر، می‌توانید هدف را به موارد زیر تقسیم کنید:

* رزرو پرواز
* رزرو هتل
* اجاره خودرو
* شخصی‌سازی

سپس هر زیرکار می‌تواند توسط عوامل یا فرآیندهای اختصاصی انجام شود. یک عامل ممکن است در جستجوی بهترین قیمت‌های پرواز تخصص داشته باشد، دیگری بر رزرو هتل تمرکز کند و همین‌طور ادامه دهد. یک عامل هماهنگ‌کننده یا «پایینی» می‌تواند این نتایج را به یک برنامه منسجم برای کاربر نهایی ترکیب کند.

این رویکرد ماژولار همچنین امکان بهبود تدریجی را فراهم می‌کند. برای مثال، می‌توانید عوامل تخصصی برای توصیه‌های غذایی یا پیشنهاد فعالیت‌های محلی اضافه کنید و برنامه سفر را به مرور زمان اصلاح کنید.

### خروجی ساختاریافته

مدل‌های زبانی بزرگ (LLMs) می‌توانند خروجی ساختاریافته (مثلاً JSON) تولید کنند که برای عوامل یا خدمات پایین‌دستی راحت‌تر قابل تجزیه و پردازش است. این موضوع در محیط‌های چندعاملی مخصوصاً مفید است، جایی که می‌توانیم پس از دریافت خروجی برنامه‌ریزی، به این کارها عمل کنیم.

قطعه کد پایتون زیر نمونه ساده‌ای از یک عامل برنامه‌ریز است که یک هدف را به زیرکارها تقسیم می‌کند و برنامه ساختاریافته‌ای تولید می‌کند:

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

# مدل زیرکار سفر
class TravelSubTask(BaseModel):
    task_details: str
    assigned_agent: AgentEnum  # ما می‌خواهیم وظیفه را به نماینده تخصیص دهیم

class TravelPlan(BaseModel):
    main_task: str
    subtasks: List[TravelSubTask]
    is_greeting: bool

provider = FoundryChatClient(
    project_endpoint=os.environ["AZURE_AI_PROJECT_ENDPOINT"],
    model=os.environ["AZURE_AI_MODEL_DEPLOYMENT_NAME"],
    credential=AzureCliCredential(),
)

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

### عامل برنامه‌ریز با ارکستراسیون چندعاملی

در این مثال، یک عامل مسیریابی معنایی درخواست کاربر را دریافت می‌کند (مثلاً "من به یک برنامه هتل برای سفرم نیاز دارم.").

سپس برنامه‌ریز:

* برنامه هتل را دریافت می‌کند: برنامه‌ریز پیام کاربر را گرفته و بر اساس یک هشدار سیستمی (شامل جزئیات عوامل در دسترس)، برنامه سفر ساختاریافته‌ای تولید می‌کند.
* عوامل و ابزارهایشان را فهرست می‌کند: فهرست‌عامل‌ها شامل لیستی از عوامل (مثلاً برای پرواز، هتل، اجاره خودرو و فعالیت‌ها) به همراه عملکردها یا ابزارهایی است که ارائه می‌دهند.
* برنامه را به عوامل مربوطه ارسال می‌کند: بسته به تعداد زیرکارها، برنامه‌ریز یا مستقیماً پیام را به عامل اختصاصی (برای سناریوهای تک‌کار) می‌فرستد یا از طریق مدیر گروه چت برای همکاری چندعاملی هماهنگی می‌کند.
* نتیجه را خلاصه می‌کند: در نهایت برنامه‌ریز برنامه تولیدشده را برای وضوح خلاصه می‌کند.
کد پایتون زیر این مراحل را نشان می‌دهد:

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

# مدل زیرکار سفر

class TravelSubTask(BaseModel):
    task_details: str
    assigned_agent: AgentEnum # می‌خواهیم وظیفه را به نماینده اختصاص دهیم

class TravelPlan(BaseModel):
    main_task: str
    subtasks: List[TravelSubTask]
    is_greeting: bool
import json
import os
from typing import Optional

from agent_framework.foundry import FoundryChatClient
from azure.identity import AzureCliCredential

# ایجاد کلاینت

provider = FoundryChatClient(
    project_endpoint=os.environ["AZURE_AI_PROJECT_ENDPOINT"],
    model=os.environ["AZURE_AI_MODEL_DEPLOYMENT_NAME"],
    credential=AzureCliCredential(),
)

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

# چاپ محتوای پاسخ بعد از بارگزاری آن به صورت JSON

pprint(json.loads(response_content))
```

آنچه در ادامه می‌آید خروجی کد قبلی است و سپس می‌توانید از این خروجی ساختاریافته برای روت کردن به `assigned_agent` و خلاصه‌سازی برنامه سفر برای کاربر نهایی استفاده کنید.

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

یک دفترچه نمونه با کد قبلی در این آدرس موجود است [اینجا](./code_samples/07-python-agent-framework.ipynb).

### برنامه‌ریزی تکراری

برخی کارها نیازمند رفت و برگشت یا برنامه‌ریزی مجدد هستند، طوری که نتیجه یک زیرکار روی بعدی تأثیر می‌گذارد. به عنوان مثال، اگر عامل در حین رزرو پرواز با یک فرمت داده غیرمنتظره مواجه شود، ممکن است نیاز به تعدیل استراتژی خود قبل از ادامه به رزرو هتل داشته باشد.

علاوه بر این، بازخورد کاربر (مثلاً تصمیم انسان به ترجیح یک پرواز زودتر) می‌تواند باعث برنامه‌ریزی مجدد جزئی شود. این رویکرد پویا و تکراری تضمین می‌کند که راه‌حل نهایی با محدودیت‌های دنیای واقعی و ترجیحات در حال تغییر کاربر هماهنگ باشد.

مثلاً کد نمونه

```python
import os
from agent_framework.foundry import FoundryChatClient
from azure.identity import AzureCliCredential
#.. همانند کد قبلی و ارسال تاریخچه کاربر، برنامه جاری

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
# .. برنامه‌ریزی مجدد و ارسال وظایف به عامل‌های مربوطه
```

برای برنامه‌ریزی جامع‌تر، پست بلاگ <a href="https://www.microsoft.com/research/articles/magentic-one-a-generalist-multi-agent-system-for-solving-complex-tasks" target="_blank">Magnetic One</a> را برای حل کارهای پیچیده بررسی کنید.

## خلاصه

در این مقاله به مثالی نگاه کردیم درباره اینکه چگونه می‌توانیم برنامه‌ریزی‌کننده‌ای بسازیم که بتواند عوامل در دسترس تعریف‌شده را به‌صورت پویا انتخاب کند. خروجی برنامه‌ریز کارها را تجزیه می‌کند و عوامل را اختصاص می‌دهد تا بتوانند اجرا شوند. فرض بر این است که عوامل به عملکردها/ابزارهای مورد نیاز برای انجام کار دسترسی دارند. علاوه بر عوامل می‌توانید الگوهای دیگری مانند انعکاس، خلاصه‌کننده، و چت چرخشی را برای سفارشی‌سازی بیشتر اضافه کنید.

## منابع اضافی

Magnetic One - یک سیستم چندعاملی عمومی برای حل کارهای پیچیده است و در چندین معیار عامل چالشی نتایج قابل توجهی کسب کرده است. مرجع: <a href="https://www.microsoft.com/research/articles/magentic-one-a-generalist-multi-agent-system-for-solving-complex-tasks" target="_blank">Magnetic One</a>. در این پیاده‌سازی، هماهنگ‌کننده برنامه‌های خاص کار ایجاد کرده و این کارها را به عوامل در دسترس واگذار می‌کند. علاوه بر برنامه‌ریزی، هماهنگ‌کننده از مکانیزم پیگیری برای نظارت بر پیشرفت کار و برنامه‌ریزی مجدد در صورت نیاز استفاده می‌کند.

### سوالات بیشتری درباره الگوی طراحی برنامه‌ریزی دارید؟

به [Discord مایکروسافت Foundry](https://discord.com/invite/ATgtXmAS5D) بپیوندید تا با دیگر یادگیرندگان ملاقات کنید، در ساعات دفتر شرکت کنید و سوالات هوش مصنوعی عوامل خود را پاسخ بگیرید.

## درس قبلی

[ساخت عوامل هوش مصنوعی قابل اعتماد](../06-building-trustworthy-agents/README.md)

## درس بعدی

[الگوی طراحی چندعاملی](../08-multi-agent/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**سلب مسئولیت**:
این سند با استفاده از سرویس ترجمه هوش مصنوعی [Co-op Translator](https://github.com/Azure/co-op-translator) ترجمه شده است. در حالی که ما در تلاش برای دقت هستیم، لطفاً توجه داشته باشید که ترجمه‌های خودکار ممکن است شامل خطاها یا نادرستی‌هایی باشند. سند اصلی به زبان مادری خود باید به عنوان منبع معتبر در نظر گرفته شود. برای اطلاعات حیاتی، ترجمه حرفه‌ای انسانی توصیه می‌شود. ما در قبال هرگونه سوء تفاهم یا برداشت نادرست ناشی از استفاده از این ترجمه مسئولیتی نداریم.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->