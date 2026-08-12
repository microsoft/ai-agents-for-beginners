[![AI ایجنٹ فریم ورکس کی کھوج](../../../translated_images/ur/lesson-2-thumbnail.c65f44c93b8558df.webp)](https://youtu.be/ODwF-EZo_O8?si=1xoy_B9RNQfrYdF7)

> _(ویڈیو دیکھنے کے لئے اوپر تصویر پر کلک کریں)_

# AI ایجنٹ فریم ورکس کی کھوج

AI ایجنٹ فریم ورکس ایسے سافٹ ویئر پلیٹ فارمز ہیں جو AI ایجنٹس کی تخلیق، تعیناتی، اور انتظام کو آسان بنانے کے لیے ڈیزائن کیے گئے ہیں۔ یہ فریم ورکس ڈویلپرز کو پہلے سے بنے ہوئے اجزاء، خلاصہ جات، اور اوزار فراہم کرتے ہیں جو پیچیدہ AI نظاموں کی ترقی کو ہموار کرتے ہیں۔

یہ فریم ورکس ڈویلپرز کو ان کی ایپلیکیشنز کے منفرد پہلوؤں پر توجہ مرکوز کرنے میں مدد دیتے ہیں، عمومی چیلنجز کے لیے معیاری طریقے فراہم کر کے AI ایجنٹ ترقی کو آسان بناتے ہیں۔ یہ AI نظاموں کی scalability، accessibility، اور efficiency کو بڑھاتے ہیں۔

## تعارف

اس سبق میں یہ موضوعات شامل ہوں گے:

- AI ایجنٹ فریم ورکس کیا ہیں اور یہ ڈویلپرز کو کیا حاصل کرنے کی اجازت دیتے ہیں؟
- ٹیمیں ان کا استعمال کرکے اپنے ایجنٹس کی صلاحیتوں کو جلدی پروٹوٹائپ، iterations، اور بہتر کیسے بنا سکتی ہیں؟
- Microsoft کے بنائے گئے فریم ورکس اور اوزار میں کیا فرق ہے (<a href="https://aka.ms/ai-agents-beginners/ai-agent-service" target="_blank">Microsoft Foundry Agent Service</a> اور <a href="https://learn.microsoft.com/azure/ai-services/openai/how-to/responses" target="_blank">Microsoft Agent Framework</a>)؟
- کیا میں اپنے موجودہ Azure ایکو سسٹم کے ٹولز کو براہِ راست ایک ساتھ استعمال کر سکتا ہوں، یا مجھے علحیدہ حل کی ضرورت ہے؟
- Microsoft Foundry Agent Service کیا ہے اور یہ میری کیسے مدد کر رہا ہے؟

## سیکھنے کے مقاصد

اس سبق کے مقاصد آپ کو یہ سمجھنے میں مدد دینا ہیں:

- AI ایجنٹ فریم ورکس کا AI ترقی میں کردار۔
- ذہین ایجنٹس بنانے کے لیے AI ایجنٹ فریم ورکس کا استعمال کیسے کیا جائے۔
- AI ایجنٹ فریم ورکس کی کلیدی صلاحیتیں۔
- Microsoft Agent Framework اور Microsoft Foundry Agent Service کے درمیان فرق۔

## AI ایجنٹ فریم ورکس کیا ہیں اور یہ ڈویلپرز کو کیا کرنے کی اجازت دیتے ہیں؟

روایتی AI فریم ورکس آپ کی ایپس میں AI کو شامل کرنے اور ان ایپس کو بہتر بنانے میں درج ذیل طریقوں سے مدد کرتے ہیں:

- **ذاتی نوعیت**: AI صارف کے رویے اور ترجیحات کا تجزیہ کرکے ذاتی نوعیت کی سفارشات، مواد، اور تجربے فراہم کر سکتا ہے۔
مثال: Netflix جیسی اسٹریمنگ سروسز AI کا استعمال کرکے دیکھنے کی تاریخ کی بنیاد پر فلمیں اور شو تجویز کرتی ہیں، جو صارف کی دلچسپی اور اطمینان کو بڑھاتا ہے۔
- **خودکاری اور کارکردگی**: AI دہرانے والے کاموں کو خودکار بنا سکتا ہے، ورک فلو کو آسان بنا سکتا ہے، اور آپریشن کی کارکردگی بہتر بنا سکتا ہے۔
مثال: کسٹمر سروس ایپس AI پر مبنی چیٹ بوٹس استعمال کرتی ہیں جو عام سوالات کا جواب دیتی ہیں، جس سے جواب دہی کے وقت کم ہوتے ہیں اور انسانی ایجنٹس کو پیچیدہ مسائل پر توجہ دینے کا موقع ملتا ہے۔
- **بہتر صارف تجربہ**: AI صوتی پہچان، قدرتی زبان کی پروسیسنگ، اور پیشن گوئی والے متن جیسے ذہین فیچرز فراہم کرکے مجموعی صارف تجربہ بہتر بنا سکتا ہے۔
مثال: Siri اور Google Assistant جیسے ورچوئل اسسٹنٹس AI کا استعمال کرکے آواز کے کمانڈز کو سمجھتے اور جواب دیتے ہیں، جس سے صارفین کے لیے ڈیوائسز کے ساتھ تعامل آسان ہوتا ہے۔

### یہ سب اچھا ہے، تو پھر AI ایجنٹ فریم ورک کیوں چاہیے؟

AI ایجنٹ فریم ورکس صرف AI فریم ورکس سے زیادہ ہیں۔ یہ ذہین ایجنٹس کی تخلیق کے لیے بنائے گئے ہیں جو صارفین، دیگر ایجنٹس، اور ماحول کے ساتھ مخصوص مقاصد کے لیے تعامل کر سکتے ہیں۔ یہ ایجنٹس خودکار رویہ دکھا سکتے ہیں، فیصلے کر سکتے ہیں، اور بدلتے ہوئے حالات کے مطابق ڈھل سکتے ہیں۔ آئیے کچھ کلیدی صلاحیتوں پر نظر ڈالیں جو AI ایجنٹ فریم ورکس فراہم کرتے ہیں:

- **ایجنٹ تعاون اور ہم آہنگی**: متعدد AI ایجنٹس کی تخلیق ممکن بنائیں جو ایک ساتھ کام کر سکیں، بات چیت کر سکیں، اور پیچیدہ کام حل کرنے کے لیے ہم آہنگی رکھ سکیں۔
- **کام کی خودکار سازی اور انتظام**: متعدد مرحلوں والے ورک فلو کی خودکار کاری، کام کی تقسیم، اور ایجنٹس کے درمیان متحرک کام کی مینجمنٹ کے طریقے فراہم کریں۔
- **سیاق و سباق کی سمجھ اور مطابقت**: ایجنٹس کو سیاق و سباق کو سمجھنے، بدلتے ہوئے ماحول میں ڈھلنے، اور حقیقی وقت کی معلومات کی بنیاد پر فیصلے کرنے کی صلاحیت سے لیس کریں۔

خلاصہ یہ ہے کہ ایجنٹس آپ کو زیادہ کرنے دیتے ہیں، خودکاری کو اگلے درجے پر لے جانے دیتے ہیں، اور زیادہ ذہین نظام بنانے دیتے ہیں جو اپنے ماحول سے سیکھ اور ڈھل سکتے ہیں۔

## ایجنٹ کی صلاحیتوں کو جلدی پروٹوٹائپ، iterations، اور بہتر کیسے بنایا جائے؟

یہ ایک تیزی سے بدلنے والا میدان ہے، لیکن زیادہ تر AI ایجنٹ فریم ورکس میں کچھ عمومی چیزیں ہیں جو آپ کو جلدی پروٹوٹائپ بنانے اور iterations کرنے میں مدد دیتی ہیں، یعنی ماڈیولر اجزاء، اشتراکی اوزار، اور حقیقی وقت کی سیکھنے کی صلاحیت۔ آئیے ان پر تفصیل سے بات کرتے ہیں:

- **ماڈیولر اجزاء کا استعمال**: AI SDK پہلے سے بنے ہوئے اجزاء فراہم کرتے ہیں جیسے AI اور میموری کنیکٹرز، قدرتی زبان یا کوڈ پلگ ان کی مدد سے فنکشن کالنگ، پرامپٹ ٹیمپلیٹس، وغیرہ۔
- **اشتراکی اوزار سے فائدہ اٹھائیں**: مخصوص کردار اور کام کے ساتھ ایجنٹس ڈیزائن کریں، تاکہ وہ اشتراکی ورک فلو کو ٹیسٹ اور بہتر بنا سکیں۔
- **حقیقی وقت میں سیکھیں**: فیڈبیک لوپس کو نافذ کریں جہاں ایجنٹس تعاملات سے سیکھیں اور اپنے رویے کو متحرک طور پر ایڈجسٹ کریں۔

### ماڈیولر اجزاء کا استعمال کریں

Microsoft Agent Framework جیسے SDK پہلے سے بنے ہوئے اجزاء پیش کرتے ہیں جیسے AI کنیکٹرز، ٹول کی تعریفیں، اور ایجنٹ مینجمنٹ۔

**ٹیمیں ان کا استعمال کیسے کر سکتی ہیں**: ٹیمیں ان اجزاء کو جلدی جمع کر کے بغیر شروع کیے ایک فعال پروٹوٹائپ بنا سکتی ہیں، جس سے تیزی سے تجربہ کرنے اور بہتری کی گنجائش ہوتی ہے۔

**عملی طور پر یہ کیسے کام کرتا ہے**: آپ صارف کی ان پٹ سے معلومات نکالنے کے لیے پہلے سے بنے ہوئے پارسر، ڈیٹا ذخیرہ کرنے اور حاصل کرنے کے لیے میموری ماڈیول، اور صارف سے بات چیت کے لیے پرامپٹ جنریٹر استعمال کر سکتے ہیں، یہ سب بغیر اجزاء کو دوبارہ بنانے کے۔

**مثالی کوڈ**۔ آئیے دیکھتے ہیں کہ آپ Microsoft Agent Framework کو `FoundryChatClient` کے ساتھ کیسے استعمال کر سکتے ہیں تاکہ ماڈل صارف کی ان پٹ پر ٹول کالنگ کے ساتھ جواب دے سکے:

``` python
# مائیکروسافٹ ایجنٹ فریم ورک پائتھن کی مثال

import asyncio
import os

from agent_framework import tool
from agent_framework.foundry import FoundryChatClient
from azure.identity import AzureCliCredential


# سفر کی بکنگ کے لیے ایک نمونہ ٹول فنکشن کی تعریف کریں
@tool(approval_mode="never_require")
def book_flight(date: str, location: str) -> str:
    """Book travel given location and date."""
    return f"Travel was booked to {location} on {date}"


async def main():
    provider = FoundryChatClient(
        project_endpoint=os.environ["AZURE_AI_PROJECT_ENDPOINT"],
        model=os.environ["AZURE_AI_MODEL_DEPLOYMENT_NAME"],
        credential=AzureCliCredential(),
    )
    agent = provider.as_agent(
        name="travel_agent",
        instructions="Help the user book travel. Use the book_flight tool when ready.",
        tools=[book_flight],
    )

    response = await agent.run("I'd like to go to New York on January 1, 2025")
    print(response)
    # مثال کا نتیجہ: آپ کی پرواز 1 جنوری 2025 کو نیویارک کے لیے کامیابی سے بک ہو گئی ہے۔ محفوظ سفر! ✈️🗽


if __name__ == "__main__":
    asyncio.run(main())
```

اس مثال سے آپ دیکھ سکتے ہیں کہ کس طرح آپ پہلے سے بنے ہوئے پارسر کی مدد سے صارف کی ان پٹ سے کلیدی معلومات نکال سکتے ہیں، جیسے پرواز کی بکنگ کی درخواست کے لئے آغاز، منزل، اور تاریخ۔ یہ ماڈیولر طریقہ کار آپ کو اعلی سطحی منطق پر توجہ دینے کی اجازت دیتا ہے۔

### اشتراکی اوزار سے فائدہ اٹھائیں

Microsoft Agent Framework جیسے فریم ورکس متعدد ایجنٹس کی تخلیق میں مدد دیتے ہیں جو مل کر کام کر سکیں۔

**ٹیمیں ان کا استعمال کیسے کر سکتی ہیں**: ٹیمیں مخصوص کرداروں اور کاموں کے ساتھ ایجنٹس ڈیزائن کر کے اشتراکی ورک فلو کو بہتر بنا سکتی ہیں اور مجموعی نظام کی کارکردگی کو بڑھا سکتی ہیں۔

**عملی طور پر یہ کیسے ہوتا ہے**: آپ مختلف خصوصیات رکھنے والے ایجنٹس کی ایک ٹیم بنا سکتے ہیں، جیسے ڈیٹا ریکوری، تجزیہ، یا فیصلہ سازی۔ یہ ایجنٹس بات چیت کر کے معلومات شیئر کر سکتے ہیں تاکہ صارف کے سوال کا جواب دے سکیں یا کوئی کام مکمل کر سکیں۔

**مثالی کوڈ (Microsoft Agent Framework)**:

```python
# مائیکروسافٹ ایجنٹ فریم ورک استعمال کرتے ہوئے ایک ساتھ کام کرنے والے متعدد ایجنٹس تخلیق کرنا

import os
from agent_framework.foundry import FoundryChatClient
from azure.identity import AzureCliCredential

provider = FoundryChatClient(
    project_endpoint=os.environ["AZURE_AI_PROJECT_ENDPOINT"],
    model=os.environ["AZURE_AI_MODEL_DEPLOYMENT_NAME"],
    credential=AzureCliCredential(),
)

# ڈیٹا بازیافت ایجنٹ
agent_retrieve = provider.as_agent(
    name="dataretrieval",
    instructions="Retrieve relevant data using available tools.",
    tools=[retrieve_tool],
)

# ڈیٹا تجزیہ ایجنٹ
agent_analyze = provider.as_agent(
    name="dataanalysis",
    instructions="Analyze the retrieved data and provide insights.",
    tools=[analyze_tool],
)

# کسی کام پر ایجنٹس کو ترتیب سے چلانا
retrieval_result = await agent_retrieve.run("Retrieve sales data for Q4")
analysis_result = await agent_analyze.run(f"Analyze this data: {retrieval_result}")
print(analysis_result)
```

پچھلے کوڈ میں آپ دیکھ سکتے ہیں کہ کس طرح آپ ایک ایسا کام بنا سکتے ہیں جس میں متعدد ایجنٹس ڈیٹا کا تجزیہ کرنے کے لیے مل کر کام کرتے ہیں۔ ہر ایجنٹ مخصوص کام انجام دیتا ہے، اور کام کا نفاذ ایجنٹس کی ہم آہنگی سے ہوتا ہے تاکہ مطلوبہ نتیجہ حاصل ہو۔ مخصوص کرداروں کے ساتھ ایجنٹس بنانے سے آپ کام کی کارکردگی اور کارگزاری بہتر بنا سکتے ہیں۔

### حقیقی وقت میں سیکھیں

جدید فریم ورکس حقیقی وقت میں سیاق و سباق کی سمجھنے اور مطابقت کی صلاحیتیں فراہم کرتے ہیں۔

**ٹیمیں ان کا استعمال کیسے کر سکتی ہیں**: ٹیمیں فیڈبیک لوپس نافذ کر سکتی ہیں جہاں ایجنٹس تعاملات سے سیکھتے ہیں اور اپنے رویے کو متحرک طور پر ایڈجسٹ کرتے ہیں، جو صلاحیتوں کی مسلسل بہتری اور نکھار کا باعث بنتا ہے۔

**عملی طور پر یہ کیسے ہوتا ہے**: ایجنٹس صارف کی فیڈبیک، ماحول کا ڈیٹا، اور کام کے نتائج کا تجزیہ کرتے ہیں تاکہ اپنی معلومات کی بنیاد کو اپ ڈیٹ کریں، فیصلے کے الگورتھمز کو ایڈجسٹ کریں، اور وقت کے ساتھ کارکردگی بہتر بنائیں۔ یہ تکراری سیکھنے کا عمل ایجنٹس کو بدلتے حالات اور صارف کی ترجیحات کے مطابق ڈھالنے کی اجازت دیتا ہے، جس سے مجموعی نظام کی تاثیر بہتر ہوتی ہے۔

## Microsoft Agent Framework اور Microsoft Foundry Agent Service میں کیا فرق ہے؟

ان طریقوں کا موازنہ کرنے کے کئی طریقے ہیں، لیکن آئیں چند کلیدی اختلافات کو ان کے ڈیزائن، صلاحیتوں، اور ہدف کے استعمال کی بنا پر دیکھتے ہیں:

## Microsoft Agent Framework (MAF)

Microsoft Agent Framework ایک آسان SDK فراہم کرتا ہے جو `FoundryChatClient` کے ذریعے AI ایجنٹس بنانے کے لیے ہے۔ یہ ڈویلپرز کو Azure OpenAI ماڈلز کے ساتھ ٹول کالنگ، گفتگو کا انتظام، اور Azure شناخت کے ذریعے انٹرپرائز سیکیورٹی فراہم کرتا ہے۔

**استعمال کے میدان**: ٹول استعمال، کثیر مرحلہ ورک فلو، اور انٹرپرائز انٹیگریشن سیناریوز کے ساتھ پروڈکشن کے قابل AI ایجنٹ بنانا۔

Microsoft Agent Framework کے چند اہم بنیادی تصورات یہ ہیں:

- **ایجنٹس**: ایجنٹ `FoundryChatClient` کے ذریعے بنایا جاتا ہے اور اسے نام، ہدایات، اور ٹولز سے ترتیب دیا جاتا ہے۔ ایجنٹ کر سکتا ہے:
  - **صارف کے پیغامات کو پراسیس کرنا** اور Azure OpenAI ماڈلز کے ذریعے جوابات پیدا کرنا۔
  - **مکالمے کے سیاق و سباق کی بنیاد پر خودکار طور پر ٹولز کو کال کرنا**۔
  - **متعدد بار تعاملات کے دوران گفتگو کی حالت برقرار رکھنا**۔

  یہاں ایک کوڈ کا ٹکڑا ہے جو ایک ایجنٹ بنانے کا طریقہ دکھاتا ہے:

    ```python
    import os
    from agent_framework.foundry import FoundryChatClient
    from azure.identity import AzureCliCredential

    provider = FoundryChatClient(
        project_endpoint=os.environ["AZURE_AI_PROJECT_ENDPOINT"],
        model=os.environ["AZURE_AI_MODEL_DEPLOYMENT_NAME"],
        credential=AzureCliCredential(),
    )
    agent = provider.as_agent(
        name="my_agent",
        instructions="You are a helpful assistant.",
    )

    response = await agent.run("Hello, World!")
    print(response)
    ```

- **ٹولز**: یہ فریم ورک Python فنکشنز کے طور پر ٹولز کی تعریف کی حمایت کرتا ہے جنہیں ایجنٹ خودکار طور پر کال کر سکتا ہے۔ ٹولز ایجنٹ بنانے کے دوران رجسٹر کیے جاتے ہیں:

    ```python
    def get_weather(location: str) -> str:
        """Get the current weather for a location."""
        return f"The weather in {location} is sunny, 72\u00b0F."

    agent = provider.as_agent(
        name="weather_agent",
        instructions="Help users check the weather.",
        tools=[get_weather],
    )
    ```

- **کثیر ایجنٹ ہم آہنگی**: آپ مختلف مہارتوں کے حامل متعدد ایجنٹس بنا سکتے ہیں اور ان کے کام کی ہم آہنگی کر سکتے ہیں:

    ```python
    planner = provider.as_agent(
        name="planner",
        instructions="Break down complex tasks into steps.",
    )

    executor = provider.as_agent(
        name="executor",
        instructions="Execute the planned steps using available tools.",
        tools=[execute_tool],
    )

    plan = await planner.run("Plan a trip to Paris")
    result = await executor.run(f"Execute this plan: {plan}")
    ```

- **Azure شناختی انضمام**: فریم ورک `AzureCliCredential` (یا `DefaultAzureCredential`) استعمال کرتا ہے تاکہ محفوظ، بغیر کلید کی تصدیق فراہم کرے، جس سے API کیز کے انتظام کی ضرورت ختم ہو جاتی ہے۔

## Microsoft Foundry Agent Service

Microsoft Foundry Agent Service حالیہ اضافہ ہے، جسے Microsoft Ignite 2024 میں متعارف کرایا گیا۔ یہ AI ایجنٹس کی تخلیق اور تعیناتی کی اجازت دیتا ہے جو زیادہ لچکدار ماڈلز استعمال کرتے ہیں، جیسے کہ براہِ راست اوپن سورس LLMs جیسے Llama 3، Mistral، اور Cohere کو کال کرنا۔

Microsoft Foundry Agent Service مضبوط انٹرپرائز سیکیورٹی میکانزمز اور ڈیٹا اسٹوریج کے طریقے فراہم کرتا ہے، جس سے یہ انٹرپرائز ایپلیکیشنز کے لیے موزوں ہے۔

یہ Microsoft Agent Framework کے ساتھ مل کر کام کرتا ہے تاکہ ایجنٹس بنانے اور تعینات کرنے میں آسانی ہو۔

یہ سروس فی الحال Public Preview میں ہے اور Python اور C# میں ایجنٹس بنانے کی حمایت کرتی ہے۔

Microsoft Foundry Agent Service Python SDK کا استعمال کرتے ہوئے، ہم ایک صارف کے بنائے ہوئے ٹول کے ساتھ ایک ایجنٹ بنا سکتے ہیں:

```python
import asyncio
from azure.identity import DefaultAzureCredential
from azure.ai.projects import AIProjectClient

# ٹول فنکشنز کی تعریف کریں
def get_specials() -> str:
    """Provides a list of specials from the menu."""
    return """
    Special Soup: Clam Chowder
    Special Salad: Cobb Salad
    Special Drink: Chai Tea
    """

def get_item_price(menu_item: str) -> str:
    """Provides the price of the requested menu item."""
    return "$9.99"


async def main() -> None:
    credential = DefaultAzureCredential()
    project_client = AIProjectClient.from_connection_string(
        credential=credential,
        conn_str="your-connection-string",
    )

    agent = project_client.agents.create_agent(
        model="gpt-5-mini",
        name="Host",
        instructions="Answer questions about the menu.",
        tools=[get_specials, get_item_price],
    )

    thread = project_client.agents.create_thread()

    user_inputs = [
        "Hello",
        "What is the special soup?",
        "How much does that cost?",
        "Thank you",
    ]

    for user_input in user_inputs:
        print(f"# User: '{user_input}'")
        message = project_client.agents.create_message(
            thread_id=thread.id,
            role="user",
            content=user_input,
        )
        run = project_client.agents.create_and_process_run(
            thread_id=thread.id, agent_id=agent.id
        )
        messages = project_client.agents.list_messages(thread_id=thread.id)
        print(f"# Agent: {messages.data[0].content[0].text.value}")


if __name__ == "__main__":
    asyncio.run(main())
```

### بنیادی تصورات

Microsoft Foundry Agent Service کے بنیادی تصورات یہ ہیں:

- **ایجنٹ**: Microsoft Foundry Agent Service Microsoft Foundry کے ساتھ انٹیگریٹ کرتا ہے۔ Microsoft Foundry میں، ایک AI ایجنٹ ایک "سمارٹ" مائیکرو سروس کی طرح کام کرتا ہے جو سوالات کے جواب (RAG)، عمل انجام دینے، یا مکمل خودکار ورک فلو بنانے کے لیے استعمال کیا جا سکتا ہے۔ یہ تخلیقی AI ماڈلز کی طاقت کو ایسے اوزار کے ساتھ ملاتا ہے جو حقیقی دنیا کے ڈیٹا ذرائع تک رسائی اور ان سے تعامل کی اجازت دیتے ہیں۔ یہاں ایک ایجنٹ کی مثال ہے:

    ```python
    agent = project_client.agents.create_agent(
        model="gpt-5-mini",
        name="my-agent",
        instructions="You are helpful agent",
        tools=code_interpreter.definitions,
        tool_resources=code_interpreter.resources,
    )
    ```

    اس مثال میں ایک ایجنٹ `gpt-5-mini` ماڈل، نام `my-agent`، اور ہدایات `You are helpful agent` کے ساتھ بنایا گیا ہے۔ ایجنٹ ٹولز اور وسائل سے لیس ہے تاکہ کوڈ کی تفسیر کے کام انجام دے سکے۔

- **تھریڈ اور پیغامات**: تھریڈ ایک اور اہم تصور ہے۔ یہ ایجنٹ اور صارف کے درمیان گفتگو یا تعامل کی نمائندگی کرتا ہے۔ تھریڈز گفتگو کی پیش رفت کو ٹریک کرنے، سیاق و سباق کی معلومات ذخیرہ کرنے، اور تعامل کی حالت کو منظم کرنے کے لیے استعمال کیے جا سکتے ہیں۔ یہاں تھریڈ کی ایک مثال ہے:

    ```python
    thread = project_client.agents.create_thread()
    message = project_client.agents.create_message(
        thread_id=thread.id,
        role="user",
        content="Could you please create a bar chart for the operating profit using the following data and provide the file to me? Company A: $1.2 million, Company B: $2.5 million, Company C: $3.0 million, Company D: $1.8 million",
    )
    
    # ایجنٹ سے کہیں کہ وہ تھریڈ پر کام کرے
    run = project_client.agents.create_and_process_run(thread_id=thread.id, agent_id=agent.id)
    
    # ایجنٹ کے جواب کو دیکھنے کے لیے تمام پیغامات لائیں اور لاگ کریں
    messages = project_client.agents.list_messages(thread_id=thread.id)
    print(f"Messages: {messages}")
    ```

    پچھلے کوڈ میں ایک تھریڈ بنایا گیا ہے۔ اس کے بعد تھریڈ کو ایک پیغام بھیجا جاتا ہے۔ `create_and_process_run` کال کرکے، ایجنٹ سے تھریڈ پر کام کرنے کو کہا جاتا ہے۔ آخر میں، پیغامات کو بازیافت کر کے لاگ کیا جاتا ہے تاکہ ایجنٹ کی جواب دہی دیکھی جا سکے۔ پیغامات صارف اور ایجنٹ کے درمیان گفتگو کی پیش رفت کو ظاہر کرتے ہیں۔ یہ بھی سمجھنا ضروری ہے کہ پیغامات مختلف اقسام کے ہو سکتے ہیں جیسے متن، تصویر، یا فائل، یعنی ایجنٹ کا کام ایک تصویر یا متن جیسا نتیجہ دے سکتا ہے۔ بطور ڈویلپر، آپ اس معلومات کا استعمال کرکے جواب کو مزید پراسیس کر سکتے ہیں یا صارف کے سامنے پیش کر سکتے ہیں۔

- **Microsoft Agent Framework کے ساتھ انضمام**: Microsoft Foundry Agent Service Microsoft Agent Framework کے ساتھ بغیر رکاوٹ کام کرتا ہے، یعنی آپ `FoundryChatClient` کا استعمال کرکے ایجنٹس بنا سکتے ہیں اور ان کو Agent Service کے ذریعے پیداوار میں تعینات کر سکتے ہیں۔

**استعمال کے میدان**: Microsoft Foundry Agent Service انٹرپرائز ایپلیکیشنز کے لیے ڈیزائن کیا گیا ہے جنہیں محفوظ، مقیاس پذیر، اور لچکدار AI ایجنٹ تعیناتی کی ضرورت ہوتی ہے۔

## ان طریقوں کے درمیان کیا فرق ہے؟
 
یہ تو لگتا ہے کہ کچھ اوورلیپ ہے، لیکن ان کے ڈیزائن، صلاحیتوں، اور ہدف کے استعمال کی بنیاد پر چند کلیدی اختلافات ہیں:
 
- **Microsoft Agent Framework (MAF)**: AI ایجنٹس بنانے کے لیے ایک پروڈکشن کے قابل SDK ہے۔ یہ ٹول کالنگ، گفتگو کے انتظام، اور Azure شناختی انضمام کے ساتھ ایجنٹس بنانے کے لیے ایک آسان API فراہم کرتا ہے۔
- **Microsoft Foundry Agent Service**: Microsoft Foundry میں ایک پلیٹ فارم اور تعیناتی سروس ہے۔ یہ Azure OpenAI، Azure AI Search، Bing Search، اور کوڈ ایکزیکیوشن جیسی خدمات سے بلٹ ان کنیکٹیویٹی فراہم کرتا ہے۔
 
ابھی بھی فیصلہ نہ کر پائے کہ کون سا استعمال کریں؟

### استعمال کے منظرنامے
 
آئیے کچھ عام استعمال کے منظرناموں پر چلتے ہیں تاکہ مدد ملے:
 
> سوال: میں پروڈکشن AI ایجنٹ ایپلیکیشنز بنا رہا ہوں اور جلدی شروع کرنا چاہتا ہوں۔
>

>جواب: Microsoft Agent Framework بہترین انتخاب ہے۔ یہ `FoundryChatClient` کے ذریعے ایک سادہ، Pythonic API فراہم کرتا ہے جو آپ کو چند کوڈ لائنوں میں ایجنٹس کو ٹولز اور ہدایات کے ساتھ ڈیفائن کرنے دیتا ہے۔

>سوال: مجھے Azure انٹیگریشنز جیسے سرچ اور کوڈ ایکزیکیوشن کے ساتھ انٹرپرائز گریڈ تعیناتی چاہیے۔
>
> جواب: Microsoft Foundry Agent Service بہترین فٹ ہے۔ یہ ایک پلیٹ فارم سروس ہے جو متعدد ماڈلز، Azure AI سرچ، Bing سرچ، اور Azure Functions کی بلٹ ان صلاحیتیں فراہم کرتی ہے۔ آپ آسانی سے Foundry پورٹل میں اپنے ایجنٹس بنا سکتے ہیں اور انہیں اسکیل پر تعینات کر سکتے ہیں۔
 
> سوال: میں ابھی بھی الجھن میں ہوں، مجھے صرف ایک آپشن دیں۔
>
> جواب: Microsoft Agent Framework سے شروع کریں تاکہ ایجنٹس بنائیں، اور پھر جب پروڈکشن میں تعیناتی اور اسکیلنگ کی ضرورت ہو تو Microsoft Foundry Agent Service استعمال کریں۔ اس طریقے سے آپ اپنے ایجنٹ منطق پر تیزی سے iteration کر سکیں گے اور انٹرپرائز تعیناتی کے واضح راستے بھی حاصل ہوں گے۔
 
آئیے کچھ کلیدی اختلافات کو جدول میں خلاصہ کریں:

| فریم ورک | توجہ | بنیادی تصورات | استعمال کے منظرنامے |
| --- | --- | --- | --- |
| Microsoft Agent Framework | ٹول کالنگ کے ساتھ اسٹریم لائنڈ ایجنٹ SDK | ایجنٹس، ٹولز، Azure شناختی انضمام | AI ایجنٹس کی تعمیر، ٹول استعمال، کثیر مرحلہ ورک فلو |
| Microsoft Foundry Agent Service | لچکدار ماڈلز، انٹرپرائز سیکیورٹی، کوڈ جنریشن، ٹول کالنگ | ماڈیولیریٹی، تعاون، پراسیس آرکسٹریشن | محفوظ، مقیاس پذیر، اور لچکدار AI ایجنٹ تعیناتی |

## کیا میں اپنے موجودہ Azure ایکو سسٹم کے ٹولز کو براہِ راست شامل کر سکتا ہوں، یا مجھے علحیدہ حل کی ضرورت ہے؟


جواب ہاں ہے، آپ اپنے موجودہ Azure ماحولیاتی نظام کے اوزاروں کو خاص طور پر Microsoft Foundry Agent Service کے ساتھ براہ راست مربوط کر سکتے ہیں، کیونکہ یہ دوسرے Azure سروسز کے ساتھ بغیر کسی رکاوٹ کے کام کرنے کے لیے بنایا گیا ہے۔ مثلاً، آپ Bing، Azure AI Search، اور Azure Functions کی انضمام کر سکتے ہیں۔ Microsoft Foundry کے ساتھ گہری انضمام بھی موجود ہے۔

Microsoft Agent Framework بھی `FoundryChatClient` اور Azure شناخت کے ذریعے Azure سروسز کے ساتھ مربوط ہوتا ہے، جس سے آپ اپنے ایجنٹ اوزاروں سے براہ راست Azure سروسز کو کال کر سکتے ہیں۔

## نمونہ کوڈز

- Python: [Agent Framework (Microsoft Foundry)](./code_samples/02-python-agent-framework.ipynb)
- Python: [Agent Framework (Azure OpenAI Responses API)](./code_samples/02-python-agent-framework-azure-openai.ipynb)
- .NET: [Agent Framework](./code_samples/02-dotnet-agent-framework.md)

## AI Agent Frameworks کے بارے میں مزید سوالات ہیں؟

[Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D) میں شامل ہوں تاکہ دوسرے سیکھنے والوں سے ملیں، دفتر کے اوقات میں شرکت کریں اور اپنے AI Agents کے سوالات کے جواب حاصل کریں۔

## حوالہ جات

- <a href="https://techcommunity.microsoft.com/blog/azure-ai-services-blog/introducing-azure-ai-agent-service/4298357" target="_blank">Azure Agent Service</a>
- <a href="https://learn.microsoft.com/azure/ai-services/openai/how-to/responses" target="_blank">Microsoft Agent Framework - Azure OpenAI Responses</a>
- <a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Microsoft Foundry Agent Service</a>

## پچھلا سبق

[Introduction to AI Agents and Agent Use Cases](../01-intro-to-ai-agents/README.md)

## اگلا سبق

[Understanding Agentic Design Patterns](../03-agentic-design-patterns/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ڈس کلیمر**:
یہ دستاویز AI ترجمہ سروس [Co-op Translator](https://github.com/Azure/co-op-translator) کے ذریعے ترجمہ کی گئی ہے۔ جبکہ ہم درستگی کے لیے کوشاں ہیں، براہ کرم اس بات سے آگاہ رہیں کہ خودکار ترجمے میں غلطیاں یا عدم درستیاں ہو سکتی ہیں۔ اصل دستاویز اپنے مادری زبان میں مستند ماخذ سمجھی جائے گی۔ حساس معلومات کے لیے پیشہ ور انسانی ترجمہ کی سفارش کی جاتی ہے۔ اس ترجمے کے استعمال سے پیدا ہونے والی کسی بھی غلط فہمی یا غلط تشریح کی ذمہ داری ہم قبول نہیں کرتے۔
<!-- CO-OP TRANSLATOR DISCLAIMER END -->