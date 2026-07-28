[![قابل اعتماد AI ایجنٹس](../../../translated_images/ur/lesson-6-thumbnail.a58ab36c099038d4.webp)](https://youtu.be/iZKkMEGBCUQ?si=Q-kEbcyHUMPoHp8L)

> _(ویڈیو دیکھنے کے لیے اوپر تصویر پر کلک کریں)_

# قابل اعتماد AI ایجنٹس کی تعمیر

## تعارف

یہ سبق مندرجہ ذیل موضوعات کا احاطہ کرے گا:

- محفوظ اور مؤثر AI ایجنٹس بنانے اور تعینات کرنے کا طریقہ
- AI ایجنٹس کی ترقی کے دوران اہم حفاظتی پہلوؤں کا جائزہ
- AI ایجنٹس بناتے وقت ڈیٹا اور صارف کی پرائیویسی کا خیال رکھنا

## تعلیمی مقاصد

اس سبق کو مکمل کرنے کے بعد، آپ جان چکے ہوں گے کہ کیسے:

- AI ایجنٹس بناتے ہوئے خطرات کی نشاندہی اور انہدام کریں۔
- اس بات کو یقینی بنانے کے لیے حفاظتی تدابیر نافذ کریں کہ ڈیٹا اور رسائی مناسب طریقے سے منظم ہو۔
- ایسے AI ایجنٹس بنائیں جو ڈیٹا کی پرائیویسی برقرار رکھیں اور صارف کو بہترین تجربہ فراہم کریں۔

## حفاظت

آئیے پہلے محفوظ ایجنٹک ایپلیکیشنز کی تعمیر پر غور کریں۔ حفاظت کا مطلب ہے کہ AI ایجنٹ اپنی ڈیزائن کے مطابق کام کرے۔ ایجنٹک ایپلیکیشنز کے بنانے والے کے طور پر ہمارے پاس حفاظت کو زیادہ سے زیادہ بڑھانے کے طریقے اور اوزار موجود ہیں:

### سسٹم میسج فریم ورک کی تعمیر

اگر آپ نے کبھی بڑے زبان کے ماڈلز (LLMs) استعمال کر کے AI ایپلیکیشن بنایا ہے، تو آپ جانتے ہوں گے کہ مضبوط سسٹم پرامپٹ یا سسٹم میسج ڈیزائن کرنا کتنا ضروری ہے۔ یہ پرامپٹس میٹا قواعد، ہدایات، اور رہنما اصول مقرر کرتے ہیں کہ LLM صارف اور ڈیٹا سے کیسے بات چیت کرے گا۔

AI ایجنٹس کے لیے سسٹم پرامپٹ اور بھی اہم ہے کیونکہ AI ایجنٹس کو ان کاموں کو مکمل کرنے کے لیے بہت مخصوص ہدایات درکار ہوں گی جو ہم نے ان کے لیے ڈیزائن کی ہیں۔

سکیل ایبل سسٹم پرامپٹس بنانے کے لیے ہم اپنے ایپلیکیشن میں ایک یا اس سے زیادہ ایجنٹس بنانے کے لیے سسٹم میسج فریم ورک استعمال کر سکتے ہیں:

![سسٹم میسج فریم ورک کی تعمیر](../../../translated_images/ur/system-message-framework.3a97368c92d11d68.webp)

#### مرحلہ 1: میٹا سسٹم میسج بنائیں

میٹا پرامپٹ LLM کے ذریعے ایجنٹس کے لیے سسٹم پرامپٹس بنانے کے لیے استعمال ہوگا۔ ہم اسے ٹیمپلیٹ کی طرح ڈیزائن کرتے ہیں تاکہ ضرورت پڑنے پر کئی ایجنٹس کو مؤثر طریقے سے بنایا جا سکے۔

یہاں میٹا سسٹم میسج کی ایک مثال ہے جو ہم LLM کو دیں گے:

```plaintext
You are an expert at creating AI agent assistants. 
You will be provided a company name, role, responsibilities and other
information that you will use to provide a system prompt for.
To create the system prompt, be descriptive as possible and provide a structure that a system using an LLM can better understand the role and responsibilities of the AI assistant. 
```

#### مرحلہ 2: ایک بنیادی پرامپٹ بنائیں

اگلا مرحلہ AI ایجنٹ کو بیان کرنے کے لیے ایک بنیادی پرامپٹ بنانا ہے۔ آپ کو ایجنٹ کا کردار، ایجنٹ کے مکمل کرنے والے کام، اور ایجنٹ کی دیگر ذمہ داریاں شامل کرنی چاہیے۔

یہاں ایک مثال ہے:

```plaintext
You are a travel agent for Contoso Travel that is great at booking flights for customers. To help customers you can perform the following tasks: lookup available flights, book flights, ask for preferences in seating and times for flights, cancel any previously booked flights and alert customers on any delays or cancellations of flights.  
```

#### مرحلہ 3: بنیادی سسٹم میسج LLM کو فراہم کریں

اب ہم میٹا سسٹم میسج کو سسٹم میسج کے طور پر اور ہمارا بنیادی سسٹم میسج فراہم کر کے اس سسٹم میسج کو بہتر بنا سکتے ہیں۔

اس سے ایک ایسا سسٹم میسج تیار ہوگا جو ہمارے AI ایجنٹس کو رہنمائی کے لیے بہتر ڈیزائن کیا گیا ہو:

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

#### مرحلہ 4: بہتری اور ترمیم

اس سسٹم میسج فریم ورک کی قدر یہ ہے کہ ایک سے زیادہ ایجنٹس کے لیے سسٹم میسجز بنانا آسان ہو جائے اور وقت کے ساتھ آپ کے سسٹم میسجز کی بہتری ممکن ہو۔ کم ہی ایسا ہوتا ہے کہ آپ کا سسٹم میسج پہلی بار آپ کے مکمل استعمال کے لیے بالکل درست ہو۔ بنیادی سسٹم میسج میں معمولی تبدیلیاں کر کے اسے دوبارہ چلانا آپ کو نتائج کا موازنہ اور تجزیہ کرنے کی اجازت دیتا ہے۔

## خطرات کو سمجھنا

قابل اعتماد AI ایجنٹس بنانے کے لیے ضروری ہے کہ آپ اپنے AI ایجنٹ کے لیے خطرات اور دھمکیوں کو سمجھیں اور کم کریں۔ آئیے کچھ مختلف خطرات کا جائزہ لیتے ہیں جو AI ایجنٹس کو لاحق ہو سکتے ہیں اور دیکھتے ہیں کہ آپ ان کے لیے بہتر منصوبہ بندی اور تیار کیسے کر سکتے ہیں۔

![خطرات کو سمجھنا](../../../translated_images/ur/understanding-threats.89edeada8a97fc0f.webp)

### کام اور ہدایات

**تفصیل:** حملہ آور AI ایجنٹ کی ہدایات یا مقاصد کو پرامپٹنگ یا ان پٹس کو منیپولیٹ کر کے تبدیل کرنے کی کوشش کرتے ہیں۔

**کم از کم کرنا**: ممکنہ خطرناک پرامپٹس کا پتہ لگانے کے لیے توثیقی چیکس اور ان پٹ فلٹرز کا نفاذ کریں تاکہ AI ایجنٹ انہیں پروسیس کرنے سے پہلے روک دے۔ چونکہ یہ حملے عام طور پر ایجنٹ کے ساتھ بار بار بات چیت کی ضرورت رکھتے ہیں، اس لیے گفتگو کے دوروں کی تعداد محدود کرنا ان حملوں کو روکنے کا ایک طریقہ ہے۔

### اہم نظام تک رسائی

**تفصیل:** اگر AI ایجنٹ کو حساس ڈیٹا ذخیرہ کرنے والے نظاموں اور خدمات تک رسائی حاصل ہے تو حملہ آور ایجنٹ اور ان خدمات کے درمیان مواصلات کو سمجھوتہ کر سکتے ہیں۔ یہ براہ راست حملے ہو سکتے ہیں یا ایجنٹ کے ذریعے ان نظاموں کے بارے میں معلومات حاصل کرنے کی کوششیں ہوں گی۔

**کم از کم کرنا:** AI ایجنٹس کو صرف ضرورت کی بنیاد پر نظاموں تک رسائی دینی چاہیے تاکہ ان قسم کے حملوں کو روکا جا سکے۔ ایجنٹ اور نظام کے درمیان مواصلات بھی محفوظ ہونی چاہیے۔ توثیق اور رسائی کنٹرول نافذ کرنا اس معلومات کی حفاظت کا ایک اور طریقہ ہے۔

### وسائل اور خدمات پر بوجھ بڑھانا

**تفصیل:** AI ایجنٹس مختلف ٹولز اور خدمات تک رسائی حاصل کر سکتے ہیں تاکہ کام مکمل کر سکیں۔ حملہ آور اس صلاحیت کو خدمات پر حملہ کرنے کے لیے استعمال کر سکتے ہیں، جیسے کہ AI ایجنٹ کے ذریعے زیادہ درخواستیں بھیج کر، جس کے نتیجے میں نظام ناکام ہو سکتا ہے یا اعلی لاگت آ سکتی ہے۔

**کم از کم کرنا:** ایسی پالیسیاں نافذ کریں جو AI ایجنٹ کو خدمات پر کی جانے والی درخواستوں کی تعداد محدود کریں۔ AI ایجنٹ کے لیے گفتگو کے دوروں اور درخواستوں کی تعداد محدود کرنا بھی ان حملوں کو روکنے کا ایک طریقہ ہے۔

### معلوماتی بنیاد کی زہر آلودگی

**تفصیل:** اس قسم کا حملہ AI ایجنٹ کو براہ راست نشانہ نہیں بناتا بلکہ معلوماتی بنیاد اور دیگر خدمات کو نشانہ بناتا ہے جو AI ایجنٹ استعمال کرتا ہے۔ اس میں وہ ڈیٹا یا معلومات خراب کرنا شامل ہو سکتا ہے جو AI ایجنٹ کام مکمل کرنے کے لیے استعمال کرتا ہے، جس سے صارف کو متعصب یا غیر متوقع جوابات مل سکتے ہیں۔

**کم از کم کرنا:** AI ایجنٹ کے کام کے فلو میں استعمال ہونے والے ڈیٹا کی باقاعدہ جانچ پڑتال کریں۔ یقینی بنائیں کہ اس ڈیٹا تک رسائی محفوظ ہو اور صرف قابل اعتماد افراد ہی اسے تبدیل کریں تاکہ اس قسم کے حملے سے بچاؤ ہو۔

### زنجیری غلطیاں

**تفصیل:** AI ایجنٹس مختلف ٹولز اور خدمات تک رسائی حاصل کرتے ہیں تاکہ کام مکمل کر سکیں۔ حملہ آوروں کی جانب سے کی جانے والی غلطیاں دوسرے نظاموں کی ناکامی کا باعث بن سکتی ہیں جن سے AI ایجنٹ جُڑا ہوتا ہے، جس سے حملہ مزید پھیل سکتا ہے اور مسئلہ حل کرنا مشکل ہو جائے گا۔

**کم از کم کرنا:** ایک طریقہ یہ ہے کہ AI ایجنٹ کو محدود ماحول میں کام کرنے دیں، جیسے کہ Docker کنٹینر میں کام انجام دینا، تاکہ براہ راست نظامی حملے روکے جا سکیں۔ جب کچھ نظام غلطی کے ساتھ جواب دیتے ہیں تو بیک اپ میکانزم اور دوبارہ کوشش کرنے کی منطق بنانا بڑے نظامی نقصانات کو روکنے کا ایک اور طریقہ ہے۔

## انسانی مداخلت کا سلسلہ

قابل اعتماد AI ایجنٹ سسٹمز بنانے کا ایک اور مؤثر طریقہ انسانی مداخلت کا سلسلہ ہے۔ اس سے ایک ایسا سلسلہ بن جاتا ہے جس میں صارفین عمل کے دوران AI ایجنٹس کو رائے دے سکتے ہیں۔ صارفین ایک کثیر ایجنٹی سسٹم میں ایجنٹس کی طرح کام کرتے ہیں، منظوری یا عمل روکنے کے ذریعے۔

![انسانی مداخلت کا سلسلہ](../../../translated_images/ur/human-in-the-loop.5f0068a678f62f4f.webp)

یہ ایک کوڈ اسنیپٹ ہے جو Microsoft Agent Framework استعمال کرتے ہوئے دکھاتا ہے کہ یہ تصور کیسے نافذ کیا جاتا ہے:

```python
import os
from agent_framework.foundry import FoundryChatClient
from azure.identity import AzureCliCredential

# فراہم کنندہ کو انسانی منظوری کے ساتھ بنائیں
provider = FoundryChatClient(
    project_endpoint=os.environ["AZURE_AI_PROJECT_ENDPOINT"],
    model=os.environ["AZURE_AI_MODEL_DEPLOYMENT_NAME"],
    credential=AzureCliCredential(),
)

# ایجنٹ کو انسانی منظوری کے مرحلے کے ساتھ بنائیں
response = provider.create_response(
    input="Write a 4-line poem about the ocean.",
    instructions="You are a helpful assistant. Ask for user approval before finalizing.",
)

# صارف جواب کا جائزہ لے سکتا ہے اور منظوری دے سکتا ہے
print(response.output_text)
user_input = input("Do you approve? (APPROVE/REJECT): ")
if user_input == "APPROVE":
    print("Response approved.")
else:
    print("Response rejected. Revising...")
```

## نتیجہ

قابل اعتماد AI ایجنٹس کی تعمیر میں محتاط ڈیزائن، مضبوط حفاظتی تدابیر، اور مسلسل بہتری کی ضرورت ہوتی ہے۔ منظم میٹا پرامپٹنگ سسٹمز کا نفاذ، ممکنہ خطرات کی سمجھ، اور روک تھام کی حکمت عملیوں کے ذریعے، ڈویلپر ایسے AI ایجنٹس بنا سکتے ہیں جو محفوظ اور مؤثر دونوں ہوں۔ اس کے علاوہ، انسانی مداخلت کا طریقہ اپنانا یقینی بناتا ہے کہ AI ایجنٹس صارف کی ضروریات کے مطابق رہیں اور خطرات کم ہوں۔ جیسے جیسے AI ترقی کرتا رہے گا، سیکورٹی، پرائیویسی، اور اخلاقی پہلوؤں پر پیشگی توجہ برقرار رکھنا AI پر مبنی نظاموں میں اعتماد اور بھروسہ قائم رکھنے کے لیے کلیدی ہوگا۔

## کوڈ کے نمونے

- [`code_samples/06-system-message-framework.ipynb`](code_samples/06-system-message-framework.ipynb): میٹا پرامپٹ سسٹم میسج فریم ورک کی مرحلہ وار نمائش۔
- [`code_samples/06-human-in-the-loop.ipynb`](code_samples/06-human-in-the-loop.ipynb): قابل اعتماد ایجنٹس کے لیے عمل سے پہلے منظوری کے دروازے، خطرے کی درجہ بندی، اور آڈٹ لاگنگ۔

### قابل اعتماد AI ایجنٹس کی تعمیر پر مزید سوالات ہیں؟

مزید سیکھنے والوں سے ملنے، آفس آور میں شرکت کرنے اور اپنے AI ایجنٹس کے سوالات کے جواب حاصل کرنے کے لیے [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D) میں شامل ہوں۔

## اضافی وسائل

- <a href="https://learn.microsoft.com/azure/ai-studio/responsible-use-of-ai-overview" target="_blank">ذمے دار AI کا جائزہ</a>
- <a href="https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai" target="_blank">جنریٹو AI ماڈلز اور AI ایپلیکیشنز کی تشخیص</a>
- <a href="https://learn.microsoft.com/azure/ai-services/openai/concepts/system-message?context=%2Fazure%2Fai-studio%2Fcontext%2Fcontext&tabs=top-techniques" target="_blank">حفاظتی نظامی پیغامات</a>
- <a href="https://blogs.microsoft.com/wp-content/uploads/prod/sites/5/2022/06/Microsoft-RAI-Impact-Assessment-Template.pdf?culture=en-us&country=us" target="_blank">خطرہ تشخیص ٹیمپلیٹ</a>

## پچھلا سبق

[ایجنٹک RAG](../05-agentic-rag/README.md)

## اگلا سبق

[منصوبہ بندی کا ڈیزائن پیٹرن](../07-planning-design/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ڈس کلیمر**:
یہ دستاویز AI ترجمہ سروس [Co-op Translator](https://github.com/Azure/co-op-translator) کے ذریعے ترجمہ کی گئی ہے۔ جبکہ ہم درستگی کے لیے کوشاں ہیں، براہ کرم اس بات سے آگاہ رہیں کہ خودکار ترجمے میں غلطیاں یا عدم درستیاں ہو سکتی ہیں۔ اصل دستاویز اپنے مادری زبان میں مستند ماخذ سمجھی جائے گی۔ حساس معلومات کے لیے پیشہ ور انسانی ترجمہ کی سفارش کی جاتی ہے۔ اس ترجمے کے استعمال سے پیدا ہونے والی کسی بھی غلط فہمی یا غلط تشریح کی ذمہ داری ہم قبول نہیں کرتے۔
<!-- CO-OP TRANSLATOR DISCLAIMER END -->