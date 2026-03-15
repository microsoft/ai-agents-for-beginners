[![ای آئی ایجنٹ فریم ورکس کی تلاش](../../../translated_images/ur/lesson-2-thumbnail.c65f44c93b8558df.webp)](https://youtu.be/ODwF-EZo_O8?si=1xoy_B9RNQfrYdF7)

> _(اس سبق کی ویڈیو دیکھنے کے لیے اوپر دی گئی تصویر پر کلک کریں)_

# ای آئی ایجنٹ فریم ورکس کی تلاش

ای آئی ایجنٹ فریم ورکس ایسے سافٹ ویئر پلیٹ فارمز ہیں جو ای آئی ایجنٹس کی تخلیق، تعیناتی، اور انتظام کو آسان بنانے کے لیے تیار کیے گئے ہیں۔ یہ فریم ورکس ڈویلپرز کو پہلے سے بنائے گئے اجزاء، تجریدات، اور ٹولز مہیا کرتے ہیں جو پیچیدہ ای آئی سسٹمز کی ترقی کو تیز کرتے ہیں۔

یہ فریم ورکس ڈویلپرز کو اپنی درخواستوں کے منفرد پہلوؤں پر توجہ مرکوز کرنے میں مدد دیتے ہیں، کیونکہ یہ ای آئی ایجنٹ کی تیاری میں عام چیلنجز کے لیے معیاری راستے فراہم کرتے ہیں۔ یہ AI سسٹمز کی تعمیر میں توسیع پذیری، دستیابی، اور کارکردگی کو بہتر بناتے ہیں۔

## تعارف

اس سبق میں یہ باتیں شامل ہوں گی:

- ای آئی ایجنٹ فریم ورکس کیا ہیں اور یہ ڈویلپرز کو کیا حاصل کرنے میں مدد دیتے ہیں؟
- ٹیمیں ان کا استعمال کیسے کر سکتی ہیں تاکہ اپنے ایجنٹ کی صلاحیتوں کو جلدی پروٹوٹائپ، دہرائیں، اور بہتر بنائیں؟
- مائیکروسافٹ کے بنانے والے فریم ورکس اور ٹولز (جیسے <a href="https://aka.ms/ai-agents-beginners/ai-agent-service" target="_blank">Azure AI Agent Service</a> اور <a href="https://learn.microsoft.com/azure/ai-services/openai/how-to/responses" target="_blank">Microsoft Agent Framework</a>) میں کیا فرق ہے؟
- کیا میں اپنے موجودہ Azure ماحولیاتی نظام کے ٹولز کو براہ راست جوڑ سکتا ہوں، یا مجھے الگ سے حل چاہیے؟
- Azure AI Agents سروس کیا ہے اور یہ میری مدد کیسے کر رہی ہے؟

## سیکھنے کے مقاصد

اس سبق کے مقاصد یہ ہیں کہ آپ کو سمجھنے میں مدد دے:

- ای آئی ایجنٹ فریم ورکس کا AI ترقی میں کردار کیا ہے۔
- ای آئی ایجنٹ فریم ورکس کو کیسے استعمال کریں تاکہ ذہین ایجنٹس بنائے جا سکیں۔
- ای آئی ایجنٹ فریم ورکس کی اہم صلاحیتیں کیا ہیں۔
- Microsoft Agent Framework اور Azure AI Agent Service میں کیا فرق ہے۔

## ای آئی ایجنٹ فریم ورکس کیا ہیں اور یہ ڈویلپرز کو کیا کرنے کی اجازت دیتے ہیں؟

روایتی AI فریم ورکس آپ کی ایپس میں AI کو شامل کرنے اور ان ایپس کو بہتر بنانے میں مدد کر سکتے ہیں، جیسے:

- **ذاتی نوعیت**: AI صارف کے رویے اور ترجیحات کا تجزیہ کر کے ذاتی سفارشات، مواد، اور تجربے فراہم کر سکتا ہے۔
مثال: Netflix جیسی اسٹریمنگ سروسز AI استعمال کرتی ہیں تاکہ صارف کی دیکھنے کی تاریخ کی بنیاد پر فلمیں اور شو تجویز کریں، جس سے صارف کی دلچسپی اور اطمینان بڑھتا ہے۔
- **خود کاری اور کارکردگی**: AI دوہرانے والے کاموں کو خودکار بنا سکتا ہے، ورک فلو کو ہموار کر سکتا ہے، اور آپریشنل کارکردگی بڑھا سکتا ہے۔
مثال: کسٹمر سروس ایپس AI سے چلنے والے چیٹ بوٹس استعمال کرتی ہیں تاکہ عام سوالات کے جوابات دیں، جس سے جواب دینے کا وقت کم ہوتا ہے اور انسانی ایجنٹس کو پیچیدہ مسائل کے لیے آزاد چھوڑا جاتا ہے۔
- **بہتر صارف تجربہ**: AI زبانی شناخت، قدرتی زبان پروسیسنگ، اور پیش گوئی والی تحریر جیسی ذہین خصوصیات فراہم کر کے صارف کے مجموعی تجربے کو بہتر بناتا ہے۔
مثال: Siri اور Google Assistant جیسے ورچوئل اسسٹنٹس AI کا استعمال کرتے ہیں تاکہ آواز کے کمانڈز کو سمجھ کر جواب دیں، جس سے صارفین کے لیے اپنے آلات سے بات چیت آسان ہو جاتی ہے۔

### یہ سب اچھا لگتا ہے، تو پھر ہمیں AI Agent Framework کیوں چاہیے؟

AI ایجنٹ فریم ورکس صرف AI فریم ورکس سے کچھ زیادہ ہیں۔ یہ ذہین ایجنٹس کی تخلیق کے لیے بنائے گئے ہیں جو صارفین، دوسرے ایجنٹس، اور ماحول کے ساتھ بات چیت کر کے مخصوص مقاصد حاصل کر سکتے ہیں۔ یہ ایجنٹس خود مختار رویہ دکھا سکتے ہیں، فیصلے کر سکتے ہیں، اور بدلتی ہوئی صورتحال کے مطابق خود کو ڈھال سکتے ہیں۔ آئیے AI ایجنٹ فریم ورکس کے ذریعے فعال کچھ اہم صلاحیتوں پر نظر ڈالیں:

- **ایجنٹ کا تعاون اور ہم آہنگی**: متعدد AI ایجنٹس کی تخلیق ممکن بنائیں جو مل کر کام کریں، رابطہ کریں، اور پیچیدہ کام حل کریں۔
- **کاموں کی خود کاری اور انتظام**: کثیر مرحلوں والے ورک فلو، کاموں کی تقسیم، اور ایجنٹس کے درمیان متحرک کاموں کا انتظام فراہم کریں۔
- **سیاق و سباق کی سمجھ اور موافقت**: ایجنٹس کو ایسا لیس کریں جو سیاق و سباق کو سمجھ سکیں، بدلتے ماحول کے ساتھ خود کو مطابقت دے سکیں، اور موجودہ معلومات کی بنیاد پر فیصلے کر سکیں۔

تو خلاصہ یہ ہے کہ ایجنٹس آپ کو مزید کرنے دیتے ہیں، خود کاری کو اگلے درجے تک لے جاتے ہیں، اور ایسے زیادہ ذہین نظام بناتے ہیں جو اپنے ماحول سے سیکھ کر خود کو ڈھال سکتے ہیں۔

## ایجنٹ کی صلاحیتوں کو جلدی پروٹوٹائپ، دہرائیں، اور بہتر کیسے کریں؟

یہ ایک تیزی سے بدلنے والا میدان ہے، لیکن زیادہ تر AI ایجنٹ فریم ورکس میں کچھ ایسی باتیں عام ہوتی ہیں جو جلدی پروٹوٹائپ اور دہرائی میں مدد دیتی ہیں، جیسے ماڈیولر اجزاء، تعاون کرنے والے ٹولز، اور حقیقی وقت میں سیکھنا۔ آئیے ان پر تفصیل سے بات کرتے ہیں:

- **ماڈیولر اجزاء استعمال کریں**: AI SDKs پہلے سے بنائے ہوئے اجزاء پیش کرتے ہیں جیسے AI اور میموری کنیکٹرز، قدرتی زبان یا کوڈ پلگ انز کے ذریعے فعالیت کال کرنا، پرامپٹ ٹیمپلیٹس وغیرہ۔
- **تعاون کرنے والے ٹولز استعمال کریں**: خاص کرداروں اور کاموں کے ساتھ ایجنٹس بنائیں، تاکہ وہ مشترکہ ورک فلو کو آزما سکیں اور بہتر بنا سکیں۔
- **حقیقی وقت میں سیکھیں**: تاثرات کے لوپ نافذ کریں جہاں ایجنٹس تعاملات سے سیکھیں اور اپنی کارکردگی کو متحرک طور پر ترتیب دیں۔

### ماڈیولر اجزاء استعمال کریں

Microsoft Agent Framework جیسے SDKs پہلے سے بنائے گئے اجزاء پیش کرتے ہیں جیسے AI کنیکٹرز، ٹول ڈیفینیشنز، اور ایجنٹ مینجمنٹ۔

**ٹیمز انہیں کیسے استعمال کر سکتی ہیں**: ٹیمیں جلدی ان اجزاء کو جوڑ کر ایک فنکشنل پروٹوٹائپ بنا سکتی ہیں بغیر ابتدائی سے شروع کیے، جو تیز تجربہ اور دہرائی کی اجازت دیتا ہے۔

**عملی طور پر یہ کیسے کام کرتا ہے**: آپ صارف کے ان پٹ سے معلومات نکالنے کے لیے پہلے سے بنائے گئے پارسر، ڈیٹا ذخیرہ اور بازیافت کے لیے میموری ماڈیول، اور صارف سے رابطے کے لیے پرامپٹ جنریٹر استعمال کر سکتے ہیں، یہ تمام کچھ بھی بناۓ بغیر۔

**مثال کوڈ**: آئیے مائیکروسافٹ ایجنٹ فریم ورک کے ساتھ `AzureAIProjectAgentProvider` استعمال کرنے کی مثال دیکھیں تاکہ ماڈل صارف کے ان پٹ پر ٹول کال کے ذریعے جواب دے سکے:

``` python
# Microsoft ایجنٹ فریم ورک کی پائتھون مثال

import asyncio
import os
from typing import Annotated

from agent_framework.azure import AzureAIProjectAgentProvider
from azure.identity import AzureCliCredential


# سفر کی بکنگ کے لیے ایک نمونہ ٹول فنکشن متعین کریں
def book_flight(date: str, location: str) -> str:
    """Book travel given location and date."""
    return f"Travel was booked to {location} on {date}"


async def main():
    provider = AzureAIProjectAgentProvider(credential=AzureCliCredential())
    agent = await provider.create_agent(
        name="travel_agent",
        instructions="Help the user book travel. Use the book_flight tool when ready.",
        tools=[book_flight],
    )

    response = await agent.run("I'd like to go to New York on January 1, 2025")
    print(response)
    # مثالی نتیجہ: آپ کی 1 جنوری 2025 کو نیویارک کے لیے پرواز کامیابی سے بک ہو گئی ہے۔ سفر بخیر! ✈️🗽


if __name__ == "__main__":
    asyncio.run(main())
```

اس مثال سے آپ دیکھ سکتے ہیں کہ صارف کے ان پٹ سے کلیدی معلومات جیسے پرواز کی اصل جگہ، منزل، اور تاریخ نکالنے کے لیے پہلے سے بنائے گئے پارسر کو کیسے استعمال کیا جا سکتا ہے۔ یہ ماڈیولر نقطہ نظر آپ کو اعلی سطحی منطق پر توجہ مرکوز کرنے کی اجازت دیتا ہے۔

### تعاون کرنے والے ٹولز استعمال کریں

Microsoft Agent Framework جیسے فریم ورکس متعدد ایجنٹس کی تخلیق کو آسان بناتے ہیں جو مل کر کام کر سکتے ہیں۔

**ٹیمز انہیں کیسے استعمال کر سکتی ہیں**: ٹیمیں خاص کردار اور کاموں کے لیے ایجنٹس ڈیزائن کر سکتی ہیں، تاکہ وہ مشترکہ ورک فلو آزما سکیں اور نظام کی مجموعی کارکردگی کو بہتر بنا سکیں۔

**عملی طور پر یہ کیسے کام کرتا ہے**: آپ ایجنٹس کی ایسی ٹیم بنا سکتے ہیں جہاں ہر ایجنٹ کا ایک خاص کام ہو، جیسے ڈیٹا بازیافت، تجزیہ، یا فیصلہ سازی۔ یہ ایجنٹس معلومات کا تبادلہ کر کے مشترکہ مقصد حاصل کرتے ہیں، مثلاً صارف کے سوال کا جواب دینا یا کام مکمل کرنا۔

**مثال کوڈ (Microsoft Agent Framework)**:

```python
# Microsoft Agent Framework کے استعمال سے مل کر کام کرنے والے متعدد ایجنٹس بنانا

import os
from agent_framework.azure import AzureAIProjectAgentProvider
from azure.identity import AzureCliCredential

provider = AzureAIProjectAgentProvider(credential=AzureCliCredential())

# ڈیٹا بازیابی ایجنٹ
agent_retrieve = await provider.create_agent(
    name="dataretrieval",
    instructions="Retrieve relevant data using available tools.",
    tools=[retrieve_tool],
)

# ڈیٹا تجزیہ ایجنٹ
agent_analyze = await provider.create_agent(
    name="dataanalysis",
    instructions="Analyze the retrieved data and provide insights.",
    tools=[analyze_tool],
)

# ایجنٹس کو کسی کام پر ترتیب وار چلائیں
retrieval_result = await agent_retrieve.run("Retrieve sales data for Q4")
analysis_result = await agent_analyze.run(f"Analyze this data: {retrieval_result}")
print(analysis_result)
```

پچھلے کوڈ میں آپ دیکھ سکتے ہیں کہ کس طرح ایک ایسا کام بنایا گیا ہے جس میں متعدد ایجنٹس مل کر ڈیٹا کا تجزیہ کر رہے ہیں۔ ہر ایجنٹ ایک مخصوص کام انجام دیتا ہے، اور یہ کام ایجنٹس کی ہم آہنگی سے مکمل ہوتا ہے۔ خاص کرداروں کے ساتھ مخصوص ایجنٹس بنا کر آپ کام کی کارکردگی اور انجام دہی بہتر بنا سکتے ہیں۔

### حقیقی وقت میں سیکھیں

جدید فریم ورکس حقیقی وقت میں سیاق و سباق کو سمجھنے اور موافقت کی صلاحیتیں فراہم کرتے ہیں۔

**ٹیمز انہیں کیسے استعمال کر سکتی ہیں**: ٹیمیں تاثرات کے لوپس نافذ کر سکتی ہیں جہاں ایجنٹس تعاملات سے سیکھیں اور اپنی کارکردگی کو مسلسل بہتر بنائیں۔

**عملی طور پر یہ کیسے کام کرتا ہے**: ایجنٹس صارف کی رائے، ماحولیاتی ڈیٹا، اور کام کے نتائج کا تجزیہ کر کے اپنے علم کو اپ ڈیٹ کرتے ہیں، فیصلہ سازی کے الگورتھمز کو ایڈجسٹ کرتے ہیں، اور وقت کے ساتھ اپنی کارکردگی کو بہتر بناتے ہیں۔ یہ دہرائی والا سیکھنے کا عمل ایجنٹس کو بدلتے حالات اور صارف کی ترجیحات کے مطابق خود کو ڈھالنے کے قابل بناتا ہے، جس سے مجموعی نظام کی تاثیر میں اضافہ ہوتا ہے۔

## Microsoft Agent Framework اور Azure AI Agent Service میں کیا فرق ہے؟

ان طریقوں کا موازنہ کئی طریقوں سے کیا جا سکتا ہے، لیکن آئیے ان کے ڈیزائن، صلاحیتوں، اور استعمال کے ہدف کے اعتبار سے چند اہم اختلافات دیکھتے ہیں:

## Microsoft Agent Framework (MAF)

Microsoft Agent Framework ایک ہموار SDK فراہم کرتا ہے جو `AzureAIProjectAgentProvider` کے ذریعے AI ایجنٹس بنانے کے لیے ہے۔ یہ ڈویلپرز کو Azure OpenAI ماڈلز کے ساتھ ٹول کالنگ، گفتگو کا انتظام، اور Azure شناخت کے ذریعے انٹرپرائز گریڈ سیکیورٹی کے ساتھ ایجنٹس بنانے کی اجازت دیتا ہے۔

**استعمال کے مقاصد**: ٹول کے استعمال، کثیر مرحلہ ورک فلو، اور انٹرپرائز انٹیگریشن سیناریوز کے ساتھ تیار شدہ AI ایجنٹس کی تعمیر۔

Microsoft Agent Framework کے کچھ اہم بنیادی تصورات یہ ہیں:

- **ایجنٹس**۔ ایجنٹ کو `AzureAIProjectAgentProvider` کے ذریعے بنایا جاتا ہے اور نام، ہدایات، اور ٹولز کے ساتھ کنفیگر کیا جاتا ہے۔ ایجنٹ:
  - **صارف کے پیغامات کو پروسیس کرتا ہے** اور Azure OpenAI ماڈلز کے ذریعے جوابات تیار کرتا ہے۔
  - **بات چیت کے سیاق و سباق کی بنیاد پر خودکار طریقے سے ٹول کالز کرتا ہے**۔
  - **کئی تعاملات کے دوران بات چیت کی حالت برقرار رکھتا ہے**۔

  یہاں ایک کوڈ کا ٹکڑا ہے جو ایجنٹ بنانے کا طریقہ دکھاتا ہے:

    ```python
    import os
    from agent_framework.azure import AzureAIProjectAgentProvider
    from azure.identity import AzureCliCredential

    provider = AzureAIProjectAgentProvider(credential=AzureCliCredential())
    agent = await provider.create_agent(
        name="my_agent",
        instructions="You are a helpful assistant.",
    )

    response = await agent.run("Hello, World!")
    print(response)
    ```

- **ٹولز**۔ فریم ورک Python فنکشنز کے طور پر ٹولز کی تعریف کی حمایت کرتا ہے جو ایجنٹ خودکار طور پر کال کر سکتا ہے۔ ٹولز کو ایجنٹ بنانے کے وقت رجسٹر کیا جاتا ہے:

    ```python
    def get_weather(location: str) -> str:
        """Get the current weather for a location."""
        return f"The weather in {location} is sunny, 72\u00b0F."

    agent = await provider.create_agent(
        name="weather_agent",
        instructions="Help users check the weather.",
        tools=[get_weather],
    )
    ```

- **کثیر ایجنٹ ہم آہنگی**۔ آپ مختلف تخصصات کے ساتھ متعدد ایجنٹس بنا سکتے ہیں اور ان کے کام کو ہم آہنگ کر سکتے ہیں:

    ```python
    planner = await provider.create_agent(
        name="planner",
        instructions="Break down complex tasks into steps.",
    )

    executor = await provider.create_agent(
        name="executor",
        instructions="Execute the planned steps using available tools.",
        tools=[execute_tool],
    )

    plan = await planner.run("Plan a trip to Paris")
    result = await executor.run(f"Execute this plan: {plan}")
    ```

- **Azure شناخت انٹیگریشن**۔ فریم ورک `AzureCliCredential` (یا `DefaultAzureCredential`) استعمال کرتا ہے جو محفوظ، بغیر کلید کے اتھوینٹیکیشن فراہم کرتا ہے، اور API کلیداں براہ راست منظم کرنے کی ضرورت ختم کر دیتا ہے۔

## Azure AI Agent Service

Azure AI Agent Service مائیکروسافٹ اگنائٹ 2024 میں پیش کی گئی نئی سروس ہے۔ یہ AI ایجنٹس کی ترقی اور تعیناتی کے لیے زیادہ لچکدار ماڈلز کی اجازت دیتی ہے، جیسے کہ اوپن سورس LLMs جیسے Llama 3، Mistral، اور Cohere کو براہ راست کال کرنا۔

Azure AI Agent Service مضبوط انٹرپرائز سیکیورٹی میکانزم اور ڈیٹا اسٹوریج طریقے فراہم کرتا ہے، جس سے یہ انٹرپرائز ایپلی کیشنز کے لیے موزوں ہے۔

یہ Microsoft Agent Framework کے ساتھ بکس سے کام کرتا ہے تاکہ ایجنٹس کی تعمیر اور تعیناتی آسان بن سکے۔

یہ سروس موجودہ طور پر پبلک پریویو میں ہے اور ایجنٹس بنانے کے لیے Python اور C# کو سپورٹ کرتی ہے۔

Azure AI Agent Service Python SDK کے ذریعے ہم ایک یوزر ڈیفائنڈ ٹول کے ساتھ ایجنٹ بنا سکتے ہیں:

```python
import asyncio
from azure.identity import DefaultAzureCredential
from azure.ai.projects import AIProjectClient

# ٹول کے افعال متعین کریں
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
        model="gpt-4o-mini",
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

Azure AI Agent Service کے بنیادی تصورات یہ ہیں:

- **ایجنٹ**۔ Azure AI Agent Service Microsoft Foundry کے ساتھ انٹیگریٹ کرتا ہے۔ AI Foundry کے اندر، ایک AI ایجنٹ ایک "اسمارٹ" مائیکرو سروس کی طرح کام کرتا ہے جو سوالات کے جواب دینے (RAG)، عمل انجام دینے، یا مکمل خود کاری کرنے کے لیے استعمال ہو سکتا ہے۔ یہ تخلیقی AI ماڈلز کی طاقت کو ایسے ٹولز کے ساتھ جوڑتا ہے جو اسے حقیقی دنیا کے ڈیٹا ذرائع تک رسائی اور ان کے ساتھ تعامل کرنے کی اجازت دیتے ہیں۔ یہاں ایک ایجنٹ کی مثال ہے:

    ```python
    agent = project_client.agents.create_agent(
        model="gpt-4o-mini",
        name="my-agent",
        instructions="You are helpful agent",
        tools=code_interpreter.definitions,
        tool_resources=code_interpreter.resources,
    )
    ```

    اس مثال میں، ایک ایجنٹ `gpt-4o-mini` ماڈل، نام `my-agent`، اور ہدایات `You are helpful agent` کے ساتھ بنایا گیا ہے۔ ایجنٹ کو کوڈ تشریح کے کام انجام دینے کے لیے ٹولز اور وسائل دیے گئے ہیں۔

- **تھریڈ اور پیغامات**۔ تھریڈ ایک اور اہم تصور ہے۔ یہ ایجنٹ اور صارف کے درمیان گفتگو یا تعامل کی نمائندگی کرتا ہے۔ تھریڈز کا استعمال گفتگو کی پیش رفت کو ٹریک کرنے، سیاق و سباق کی معلومات کو ذخیرہ کرنے، اور تعامل کی حالت کو منظم کرنے کے لیے کیا جاتا ہے۔ یہاں ایک تھریڈ کی مثال ہے:

    ```python
    thread = project_client.agents.create_thread()
    message = project_client.agents.create_message(
        thread_id=thread.id,
        role="user",
        content="Could you please create a bar chart for the operating profit using the following data and provide the file to me? Company A: $1.2 million, Company B: $2.5 million, Company C: $3.0 million, Company D: $1.8 million",
    )
    
    # Ask the agent to perform work on the thread
    run = project_client.agents.create_and_process_run(thread_id=thread.id, agent_id=agent.id)
    
    # Fetch and log all messages to see the agent's response
    messages = project_client.agents.list_messages(thread_id=thread.id)
    print(f"Messages: {messages}")
    ```

    پچھلے کوڈ میں تھریڈ بنایا گیا ہے۔ اس کے بعد تھریڈ کو ایک پیغام بھیجا گیا ہے۔ `create_and_process_run` کال کر کے، ایجنٹ کو تھریڈ پر کام کرنے کو کہا گیا ہے۔ آخر میں، پیغامات بازیافت کیے گئے اور ایجنٹ کے جواب کو لاگ کیا گیا۔ یہ پیغامات صارف اور ایجنٹ کے درمیان گفتگو کی پیش رفت کو ظاہر کرتے ہیں۔ یہ بھی سمجھنا ضروری ہے کہ پیغامات مختلف اقسام کے ہو سکتے ہیں، جیسے کہ ٹیکسٹ، تصویر، یا فائل، یعنی ایجنٹ کا کام ایسی مثالیں فراہم کر سکتا ہے۔ بطور ڈویلپر آپ اس معلومات کو مزید پراسیس کر کے صارف کو پیش کر سکتے ہیں۔

- **Microsoft Agent Framework کے ساتھ انٹیگریشن**۔ Azure AI Agent Service Microsoft Agent Framework کے ساتھ بغیر کسی رکاوٹ کے کام کرتا ہے، جس کا مطلب ہے کہ آپ `AzureAIProjectAgentProvider` استعمال کرتے ہوئے ایجنٹس بنا سکتے ہیں اور ان کو Agent Service کے ذریعے پیداوار کے منظرناموں میں تعینات کر سکتے ہیں۔

**استعمال کے مقاصد**: Azure AI Agent Service انٹرپرائز ایپلی کیشنز کے لیے ڈیزائن کیا گیا ہے جنہیں محفوظ، قابل توسیع، اور لچکدار AI ایجنٹ تعیناتی کی ضرورت ہو۔

## ان طریقوں میں کیا فرق ہے؟

یہ لگتا ہے کہ ان دونوں میں کچھ حد تک اوورلیپ ہے، مگر ان کے ڈیزائن، صلاحیتوں، اور استعمال کے ہدف کے لحاظ سے کچھ کلیدی اختلافات ہیں:

- **Microsoft Agent Framework (MAF)**: AI ایجنٹس بنانے کے لیے تیار شدہ SDK ہے۔ یہ ٹول کالنگ، گفتگو کی مینجمنٹ، اور Azure شناخت کے ساتھ ایجنٹس بنانے کے لیے آسان API فراہم کرتا ہے۔
- **Azure AI Agent Service**: Azure Foundry میں ایک پلیٹ فارم اور تعیناتی سروس ہے۔ یہ Azure OpenAI، Azure AI سرچ، Bing سرچ، اور کوڈ ایگزیکیوشن جیسی خدمات سے بنیادی رابطہ فراہم کرتا ہے۔

اب بھی فیصلہ نہیں کر پائے کہ کون سا استعمال کریں؟

### استعمال کے مقاصد

آئیں دیکھتے ہیں کچھ عام استعمال کے مقاصد کے ذریعے کہ ہم آپ کی مدد کیسے کر سکتے ہیں:

> سوال: میں پرڈکشن ای آئی ایجنٹ ایپلی کیشنز بنا رہا ہوں اور چاہتا ہوں کہ جلدی شروع کروں۔
>
> جواب: Microsoft Agent Framework ایک بہت اچھا انتخاب ہے۔ یہ `AzureAIProjectAgentProvider` کے ذریعے ایک سادہ، Pythonic API فراہم کرتا ہے جو چند لائنوں میں ٹولز اور ہدایات کے ساتھ ایجنٹس کی تعریف کرنے دیتا ہے۔

> سوال: مجھے انٹرپرائز گریڈ تعیناتی چاہیے جیسے Azure سرچ اور کوڈ ایگزیکیوشن کے ساتھ۔
>
> جواب: Azure AI Agent Service بہترین انتخاب ہے۔ یہ ایک پلیٹ فارم سروس ہے جو متعدد ماڈلز، Azure AI سرچ، Bing سرچ، اور Azure فنکشنز کی بلٹ ان صلاحیتیں فراہم کرتی ہے۔ آپ آسانی سے اپنے ایجنٹس کو Foundry پورٹل میں بنا کر بڑے پیمانے پر تعینات کر سکتے ہیں۔

> سوال: میں ابھی بھی الجھن میں ہوں، بس مجھے ایک آپشن بتائیں۔
>
> جواب: Microsoft Agent Framework سے شروع کریں تاکہ اپنے ایجنٹس بنائیں، اور پھر Azure AI Agent Service استعمال کریں جب آپ کو پروڈکشن میں تعینات اور اسکیل کرنے کی ضرورت ہو۔ اس طریقے سے آپ اپنی ایجنٹ منطق پر جلدی کام کر سکتے ہیں جبکہ انٹرپرائز تعیناتی کا واضح راستہ بھی رکھ سکتے ہیں۔

آئیے کلیدی فرق جدول میں خلاصہ کریں:

| فریم ورک | توجہ | بنیادی تصورات | استعمال کے مقاصد |
| --- | --- | --- | --- |
| Microsoft Agent Framework | ٹول کالنگ کے ساتھ ہموار ایجنٹ SDK | ایجنٹس، ٹولز، Azure شناخت | AI ایجنٹس بنانا، ٹول استعمال، کثیر مرحلہ ورک فلو |
| Azure AI Agent Service | لچکدار ماڈلز، انٹرپرائز سیکیورٹی، کوڈ جنریشن، ٹول کالنگ | ماڈیولیریٹی، تعاون، عمل کی ترتیب | محفوظ، قابل توسیع، اور لچکدار AI ایجنٹ تعیناتی |

## کیا میں اپنے موجودہ Azure ماحولیاتی نظام کے ٹولز کو براہ راست جوڑ سکتا ہوں، یا مجھے الگ سے حل چاہیے؟
جواب ہاں ہے، آپ اپنے موجودہ Azure ماحولیاتی نظام کے اوزار کو براہ راست Azure AI Agent Service کے ساتھ مربوط کر سکتے ہیں، خاص طور پر کیونکہ یہ دوسرے Azure خدمات کے ساتھ بغیر کسی رکاوٹ کے کام کرنے کے لئے بنایا گیا ہے۔ آپ مثال کے طور پر Bing، Azure AI Search، اور Azure Functions کو مربوط کر سکتے ہیں۔ Microsoft Foundry کے ساتھ بھی گہرا انضمام موجود ہے۔

Microsoft Agent Framework بھی `AzureAIProjectAgentProvider` اور Azure شناخت کے ذریعے Azure خدمات کے ساتھ مربوط ہوتا ہے، جو آپ کو اپنے ایجنٹ کے اوزار سے براہ راست Azure خدمات کو کال کرنے کی اجازت دیتا ہے۔

## Sample Codes

- Python: [Agent Framework](./code_samples/02-python-agent-framework.ipynb)
- .NET: [Agent Framework](./code_samples/02-dotnet-agent-framework.md)

## Got More Questions about AI Agent Frameworks?

دوسرے سیکھنے والوں سے ملنے، آفس گھنٹوں میں شرکت کرنے اور اپنے AI Agents کے سوالات کے جوابات حاصل کرنے کے لیے [Microsoft Foundry Discord](https://aka.ms/ai-agents/discord) میں شامل ہوں۔

## References

- <a href="https://techcommunity.microsoft.com/blog/azure-ai-services-blog/introducing-azure-ai-agent-service/4298357" target="_blank">Azure Agent Service</a>
- <a href="https://learn.microsoft.com/azure/ai-services/openai/how-to/responses" target="_blank">Microsoft Agent Framework - Azure OpenAI Responses</a>
- <a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Azure AI Agent service</a>

## Previous Lesson

[Introduction to AI Agents and Agent Use Cases](../01-intro-to-ai-agents/README.md)

## Next Lesson

[Understanding Agentic Design Patterns](../03-agentic-design-patterns/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**اعتراضیہ نوٹ**:
اس دستاویز کا ترجمہ AI ترجمہ سروس [Co-op Translator](https://github.com/Azure/co-op-translator) کے ذریعے کیا گیا ہے۔ اگرچہ ہم درستگی کے لیے کوشاں ہیں، براہ کرم آگاہ رہیں کہ خودکار ترجمے میں غلطیاں یا عدم صحت ہو سکتی ہے۔ اصل دستاویز اپنی مادری زبان میں معتبر ماخذ سمجھی جانی چاہیے۔ اہم معلومات کے لیے پیشہ ورانہ انسانی ترجمہ تجویز کیا جاتا ہے۔ اس ترجمے کے استعمال سے ہونے والی کسی بھی غلط فہمی یا غلط تعبیر کی ذمہ داری ہم پر عائد نہیں ہوگی۔
<!-- CO-OP TRANSLATOR DISCLAIMER END -->