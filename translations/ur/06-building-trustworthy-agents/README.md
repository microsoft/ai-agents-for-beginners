[![قابل اعتماد AI ایجنٹس](../../../translated_images/ur/lesson-6-thumbnail.a58ab36c099038d4.webp)](https://youtu.be/iZKkMEGBCUQ?si=Q-kEbcyHUMPoHp8L)

> _(ویڈیو دیکھنے کے لیے اوپر دی گئی تصویر پر کلک کریں)_

# قابل اعتماد AI ایجنٹس کی تعمیر

## تعارف

یہ سبق احاطہ کرے گا:

- محفوظ اور مؤثر AI ایجنٹس بنانے اور تعینات کرنے کا طریقہ
- AI ایجنٹس تیار کرتے وقت اہم حفاظتی اعتبارات۔
- AI ایجنٹس تیار کرتے وقت ڈیٹا اور صارف کی پرائیویسی کو کیسے برقرار رکھا جائے۔

## سیکھنے کے اہداف

اس سبق کی تکمیل کے بعد، آپ جان لیں گے کہ کیسے:

- AI ایجنٹس تخلیق کرتے وقت خطرات کی شناخت اور ان کو کم کیا جائے۔
- حفاظتی اقدامات نافذ کیے جائیں تاکہ ڈیٹا اور رسائی کو مناسب طریقے سے منظم کیا جا سکے۔
- ایسے AI ایجنٹس تخلیق کریں جو ڈیٹا کی پرائیویسی برقرار رکھیں اور معیاری صارف تجربہ فراہم کریں۔

## حفاظت

سب سے پہلے محفوظ ایجنٹک ایپلیکیشنز بنانے کو دیکھتے ہیں۔ حفاظت کا مطلب ہے کہ AI ایجنٹ متعین کے مطابق کام کرے۔ ایجنٹک ایپلیکیشنز کے بنانے والوں کے طور پر، ہمارے پاس حفاظت کو زیادہ سے زیادہ کرنے کے لیے طریقے اور اوزار موجود ہیں:

### ایک سسٹم میسج فریم ورک بنانے کا طریقہ

اگر آپ نے کبھی بڑی زبان کے ماڈلز (LLMs) استعمال کرتے ہوئے AI ایپلیکیشن بنائی ہے تو آپ جانتے ہیں کہ مضبوط سسٹم پرامپٹ یا سسٹم میسج ڈیزائن کرنا کتنا اہم ہے۔ یہ پرامپٹس میٹا قواعد، ہدایات، اور رہنما اصول قائم کرتے ہیں کہ LLM صارف اور ڈیٹا کے ساتھ کیسے تعامل کرے گا۔

AI ایجنٹس کے لیے، سسٹم پرامپٹ اور بھی زیادہ اہم ہوتا ہے کیونکہ AI ایجنٹس کو ہماری طرف سے بنائے گئے کام مکمل کرنے کے لیے انتہائی مخصوص ہدایات کی ضرورت ہوگی۔

قابل پھیلاؤ سسٹم پرامپٹس بنانے کے لیے، ہم اپنے ایپلیکیشن میں ایک یا زیادہ ایجنٹس بنانے کے لیے سسٹم میسج فریم ورک استعمال کر سکتے ہیں:

![سिस्टम میسج فریم ورک بنانا](../../../translated_images/ur/system-message-framework.3a97368c92d11d68.webp)

#### مرحلہ 1: ایک میٹا سسٹم میسج بنائیں

میٹا پرامپٹ کا استعمال LLM کی طرف سے ہمارے بنائے گئے ایجنٹس کے لیے سسٹم پرامپٹس تیار کرنے کے لیے کیا جائے گا۔ ہم اسے ایک ٹیمپلیٹ کے طور پر ڈیزائن کرتے ہیں تاکہ ضرورت پڑنے پر ہم مؤثر طریقے سے متعدد ایجنٹس بنا سکیں۔

یہاں ایک میٹا سسٹم میسج کی مثال ہے جو ہم LLM کو دیں گے:

```plaintext
You are an expert at creating AI agent assistants. 
You will be provided a company name, role, responsibilities and other
information that you will use to provide a system prompt for.
To create the system prompt, be descriptive as possible and provide a structure that a system using an LLM can better understand the role and responsibilities of the AI assistant. 
```

#### مرحلہ 2: ایک بنیادی پرامپٹ بنائیں

اگلا قدم AI ایجنٹ کی وضاحت کرنے کے لیے ایک بنیادی پرامپٹ بنانا ہے۔ آپ کو ایجنٹ کے کردار، ایجنٹ کے مکمل کرنے والے کام، اور ایجنٹ کی دیگر ذمہ داریوں کو شامل کرنا چاہیے۔

یہاں ایک مثال ہے:

```plaintext
You are a travel agent for Contoso Travel that is great at booking flights for customers. To help customers you can perform the following tasks: lookup available flights, book flights, ask for preferences in seating and times for flights, cancel any previously booked flights and alert customers on any delays or cancellations of flights.  
```

#### مرحلہ 3: بنیادی سسٹم میسج LLM کو فراہم کریں

اب ہم اس سسٹم میسج کو میٹا سسٹم میسج اور ہمارے بنیادی سسٹم میسج کو بطور سسٹم میسج فراہم کر کے مثالی بنا سکتے ہیں۔

اس سے ایک ایسا سسٹم میسج تیار ہوگا جو ہمارے AI ایجنٹس کی رہنمائی کے لیے بہتر ڈیزائن کیا گیا ہے:

```markdown
**Company Name:** Contoso Travel  
**Role:** Travel Agent Assistant

**Objective:**  
You are an AI-powered travel agent assistant for Contoso Travel, specializing in booking flights and providing exceptional customer service. Your main goal is to assist customers in finding, booking, and managing their flights, all while ensuring that their preferences and needs are met efficiently.

**Key Responsibilities:**

1. **Flight Lookup:**
    
    - Assist customers in searching for available flights based on their specified destination, dates, and any other relevant preferences.
    - Provide a list of options, including flight times, airlines, layovers, and pricing.
2. **Flight Booking:**
    
    - Facilitate the booking of flights for customers, ensuring that all details are correctly entered into the system.
    - Confirm bookings and provide customers with their itinerary, including confirmation numbers and any other pertinent information.
3. **Customer Preference Inquiry:**
    
    - Actively ask customers for their preferences regarding seating (e.g., aisle, window, extra legroom) and preferred times for flights (e.g., morning, afternoon, evening).
    - Record these preferences for future reference and tailor suggestions accordingly.
4. **Flight Cancellation:**
    
    - Assist customers in canceling previously booked flights if needed, following company policies and procedures.
    - Notify customers of any necessary refunds or additional steps that may be required for cancellations.
5. **Flight Monitoring:**
    
    - Monitor the status of booked flights and alert customers in real-time about any delays, cancellations, or changes to their flight schedule.
    - Provide updates through preferred communication channels (e.g., email, SMS) as needed.

**Tone and Style:**

- Maintain a friendly, professional, and approachable demeanor in all interactions with customers.
- Ensure that all communication is clear, informative, and tailored to the customer's specific needs and inquiries.

**User Interaction Instructions:**

- Respond to customer queries promptly and accurately.
- Use a conversational style while ensuring professionalism.
- Prioritize customer satisfaction by being attentive, empathetic, and proactive in all assistance provided.

**Additional Notes:**

- Stay updated on any changes to airline policies, travel restrictions, and other relevant information that could impact flight bookings and customer experience.
- Use clear and concise language to explain options and processes, avoiding jargon where possible for better customer understanding.

This AI assistant is designed to streamline the flight booking process for customers of Contoso Travel, ensuring that all their travel needs are met efficiently and effectively.

```

#### مرحلہ 4: بہتری اور تکرار کریں

اس سسٹم میسج فریم ورک کی قیمت یہ ہے کہ متعدد ایجنٹس کے لیے سسٹم میسجز بنانا آسان ہو جاتا ہے اور وقت کے ساتھ اپنے سسٹم میسجز کو بہتر بنایا جا سکتا ہے۔ عام طور پر پہلی بار آپ کے مکمل استعمال کے کیس کے لیے ایسا سسٹم میسج کام نہیں کرے گا۔ بنیادی سسٹم میسج میں معمولی تبدیلیاں کر کے اسے سسٹم سے گزارنا اور نتائج کا موازنہ کرنا آپ کو اصلاحات اور بہتری کرنے کی اجازت دے گا۔

## خطرات کو سمجھنا

قابل اعتماد AI ایجنٹس بنانے کے لیے، آپ کے AI ایجنٹ کے خطرات اور دھمکیوں کو سمجھنا اور ان کو کم کرنا ضروری ہے۔ آئیے AI ایجنٹس کو لاحق چند مختلف خطرات کا جائزہ لیتے ہیں اور دیکھتے ہیں کہ آپ کس طرح ان کے لیے بہتر منصوبہ بندی اور تیاری کر سکتے ہیں۔

![خطرات کو سمجھنا](../../../translated_images/ur/understanding-threats.89edeada8a97fc0f.webp)

### کام اور ہدایات

**تفصیل:** حملہ آور AI ایجنٹ کی ہدایات یا مقاصد کو پرامپٹنگ یا ان پٹس میں تبدیلی کے ذریعے تبدیل کرنے کی کوشش کرتے ہیں۔

**کمی:** خطرناک پرامپٹس کو AI ایجنٹ کے عمل سے پہلے پکڑنے کے لیے توثیق چیکس اور ان پٹ فلٹرز نافذ کریں۔ چونکہ یہ حملے عموماً ایجنٹ کے ساتھ بار بار رابطہ کی ضرورت رکھتے ہیں، گفتگو کے دوروں کی تعداد محدود کرنا ان خطرناک حملوں کو روکنے کا ایک طریقہ ہے۔

### تنقیدی نظاموں تک رسائی

**تفصیل:** اگر AI ایجنٹ کے پاس حساس ڈیٹا رکھنے والے نظاموں اور خدمات تک رسائی ہے، تو حملہ آور ایجنٹ اور ان خدمات کے درمیان مواصلت کو متاثر کر سکتے ہیں۔ یہ براہ راست حملے ہو سکتے ہیں یا ایجنٹ کے ذریعے ان نظاموں کے بارے میں معلومات حاصل کرنے کی بالواسطہ کوششیں ہو سکتی ہیں۔

**کمی:** AI ایجنٹس کو ان نظاموں تک "ضرورت کے تحت" رسائی دی جانی چاہیے تاکہ ایسے حملوں سے بچا جا سکے۔ ایجنٹ اور نظام کے درمیان مواصلت بھی محفوظ ہونی چاہیے۔ مصدقہ بنانے اور رسائی کنٹرول نافذ کرنا اس معلومات کی حفاظت کا ایک اور طریقہ ہے۔

### وسائل اور خدمات کا بوجھ

**تفصیل:** AI ایجنٹس مختلف آلات اور خدمات تک رسائی حاصل کر کے کام مکمل کرتے ہیں۔ حملہ آور AI ایجنٹ کے ذریعے زیادہ تعداد میں درخواستیں بھیج کر ان خدمات پر حملہ کر سکتے ہیں، جو کہ نظام کی ناکامی یا زیادہ اخراجات کا باعث بن سکتا ہے۔

**کمی:** خدمات کو کی جانے والی درخواستوں کی تعداد محدود کرنے کی پالیسیز نافذ کریں۔ آپ کے AI ایجنٹ کو کی جانے والی گفتگو کے دوروں اور درخواستوں کی تعداد محدود کرنا ایسے حملوں کو روکنے کا ایک اور طریقہ ہے۔

### علم کی بنیاد کو زہریلا کرنا

**تفصیل:** یہ حملہ براہ راست AI ایجنٹ کو نشانہ نہیں بناتا بلکہ علم کی بنیاد اور دیگر خدمات کو نشانہ بناتا ہے جو AI ایجنٹ کام مکمل کرنے کے لیے استعمال کرے گا۔ اس میں وہ ڈیٹا یا معلومات خراب کرنا شامل ہو سکتا ہے جو AI ایجنٹ کام مکمل کرنے کے لیے استعمال کرے گا، جس کے نتیجے میں صارف کو متعصب یا غیر ارادی جوابات مل سکتے ہیں۔

**کمی:** AI ایجنٹ کے ورک فلو میں استعمال ہونے والے ڈیٹا کی باقاعدہ تصدیق کریں۔ یقینی بنائیں کہ اس ڈیٹا تک رسائی محفوظ ہے اور اسے صرف معتبر افراد ہی تبدیل کر سکتے ہیں تاکہ اس قسم کے حملے سے بچا جا سکے۔

### کاسکیڈنگ غلطیاں

**تفصیل:** AI ایجنٹس مختلف آلات اور خدمات تک رسائی حاصل کرتے ہیں تاکہ کام مکمل کر سکیں۔ حملہ آوروں کی وجہ سے ہونے والی غلطیاں دیگر نظاموں کی ناکامی کا باعث بن سکتی ہیں جن سے AI ایجنٹ جڑا ہے، جس سے حملہ زیادہ پھیلا اور مزید پیچیدہ ہو جاتا ہے۔

**کمی:** اس سے بچاؤ کے لیے ایک طریقہ یہ ہے کہ AI ایجنٹ کو محدود ماحول میں چلایا جائے، جیسے کہ Docker کنٹینر میں کام کرنا، تاکہ براہ راست نظامی حملوں کو روکا جا سکے۔ جب کچھ نظام غلطی کا جواب دیں تو بیک اپ طریقے اور دوبارہ کوشش کی منطق بنانا بڑے نظام کی ناکامیوں کو روکنے کا ایک اور طریقہ ہے۔

## انسان-ان-دی-لوپ

قابل اعتماد AI ایجنٹ سسٹمز بنانے کا ایک اور مؤثر طریقہ انسان-ان-دی-لوپ کا استعمال ہے۔ یہ ایک ایسا سلسلہ بناتا ہے جہاں صارفین چلتے ہوئے ایجنٹس کو فیڈ بیک دے سکتے ہیں۔ صارفین بنیادی طور پر ایک کثیر ایجنٹ نظام میں ایجنٹس کا کردار ادا کرتے ہیں اور چلنے والے عمل کی منظوری یا ختمی کی اجازت دیتے ہیں۔

![انسان ان لوپ میں](../../../translated_images/ur/human-in-the-loop.5f0068a678f62f4f.webp)

یہاں مائیکروسافٹ ایجنٹ فریم ورک کا استعمال کرتے ہوئے ایک کوڈ ٹکڑا ہے جو دکھاتا ہے کہ یہ تصور کیسے نافذ کیا جاتا ہے:

```python
import os
from agent_framework.azure import AzureAIProjectAgentProvider
from azure.identity import AzureCliCredential

# ایک انسانی منظوری کے مرحلے کے ساتھ فراہم کنندہ تخلیق کریں
provider = AzureAIProjectAgentProvider(
    credential=AzureCliCredential(),
)

# ایک انسانی منظوری کے مرحلے کے ساتھ ایجنٹ بنائیں
response = provider.create_response(
    input="Write a 4-line poem about the ocean.",
    instructions="You are a helpful assistant. Ask for user approval before finalizing.",
)

# صارف جواب کا جائزہ لے سکتا ہے اور اسے منظور کر سکتا ہے
print(response.output_text)
user_input = input("Do you approve? (APPROVE/REJECT): ")
if user_input == "APPROVE":
    print("Response approved.")
else:
    print("Response rejected. Revising...")
```

## نتیجہ

قابل اعتماد AI ایجنٹس بنانے کے لیے محتاط ڈیزائن، مضبوط حفاظتی اقدامات، اور مسلسل تکرار کی ضرورت ہوتی ہے۔ مرتب شدہ میٹا پرامپٹنگ سسٹمز کو نافذ کر کے، ممکنہ خطرات کو سمجھ کر، اور کمی کی حکمت عملیوں کو اپناتے ہوئے، ڈویلپرز ایسے AI ایجنٹس تیار کر سکتے ہیں جو محفوظ اور مؤثر ہوں۔ اضافی طور پر، انسان-ان-دی-لوپ طریقہ کار کو شامل کرنے سے یہ یقینی بنتا ہے کہ AI ایجنٹس صارف کی ضروریات کے مطابق رہیں اور خطرات کم ہوں۔ جیسا کہ AI ترقی کرتا رہتا ہے، سیکیورٹی، نجی معلومات، اور اخلاقی پہلوؤں پر فعال توجہ برقرار رکھنا AI پر مبنی نظاموں میں اعتماد اور قابل اعتماد کو فروغ دینے کی کلید ہوگی۔

## کوڈ کے نمونے

- [`code_samples/06-system-message-framework.ipynb`](code_samples/06-system-message-framework.ipynb): میٹا-پرامپٹ سسٹم-میسج فریم ورک کی مرحلہ وار ڈیمانسٹریشن۔
- [`code_samples/06-human-in-the-loop.ipynb`](code_samples/06-human-in-the-loop.ipynb): پیشگی عمل کی منظوری کے گیٹس، خطرہ کی سطح بندی، اور قابل اعتماد ایجنٹس کے لیے آڈٹ لاگنگ۔

### قابل اعتماد AI ایجنٹس بنانے کے بارے میں مزید سوالات ہیں؟

دیگر سیکھنے والوں سے ملنے، آفیس اوقات میں شرکت کرنے، اور اپنے AI ایجنٹس کے سوالات کے جوابات حاصل کرنے کے لیے [Microsoft Foundry Discord](https://aka.ms/ai-agents/discord) میں شامل ہوں۔

## اضافی وسائل

- <a href="https://learn.microsoft.com/azure/ai-studio/responsible-use-of-ai-overview" target="_blank">ذمہ دار AI کا جائزہ</a>
- <a href="https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai" target="_blank">جنریٹیو AI ماڈلز اور AI ایپلیکیشنز کی تشخیص</a>
- <a href="https://learn.microsoft.com/azure/ai-services/openai/concepts/system-message?context=%2Fazure%2Fai-studio%2Fcontext%2Fcontext&tabs=top-techniques" target="_blank">حفاظتی سسٹم میسجز</a>
- <a href="https://blogs.microsoft.com/wp-content/uploads/prod/sites/5/2022/06/Microsoft-RAI-Impact-Assessment-Template.pdf?culture=en-us&country=us" target="_blank">خطرہ اندازہ ٹیمپلیٹ</a>

## گزشتہ سبق

[ایجنٹک RAG](../05-agentic-rag/README.md)

## اگلا سبق

[منصوبہ بندی کے ڈیزائن کا نمونہ](../07-planning-design/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ڈس کلیمر**:
یہ دستاویز AI ترجمہ سروس [Co-op Translator](https://github.com/Azure/co-op-translator) کے ذریعے ترجمہ کی گئی ہے۔ جبکہ ہم درستگی کے لیے کوشاں ہیں، براہ کرم اس بات سے آگاہ رہیں کہ خودکار ترجمے میں غلطیاں یا عدم درستیاں ہو سکتی ہیں۔ اصل دستاویز اپنے مادری زبان میں مستند ماخذ سمجھی جائے گی۔ حساس معلومات کے لیے پیشہ ور انسانی ترجمہ کی سفارش کی جاتی ہے۔ اس ترجمے کے استعمال سے پیدا ہونے والی کسی بھی غلط فہمی یا غلط تشریح کی ذمہ داری ہم قبول نہیں کرتے۔
<!-- CO-OP TRANSLATOR DISCLAIMER END -->