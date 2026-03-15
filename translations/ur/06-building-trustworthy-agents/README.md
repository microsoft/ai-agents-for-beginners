[![قابلِ اعتماد AI ایجنٹس](../../../translated_images/ur/lesson-6-thumbnail.a58ab36c099038d4.webp)](https://youtu.be/iZKkMEGBCUQ?si=Q-kEbcyHUMPoHp8L)

> _(اوپر موجود تصویر پر کلک کریں تاکہ اس سبق کی ویڈیو دیکھیں)_

# قابلِ اعتماد AI ایجنٹس بنانا

## تعارف

یہ سبق درج ذیل موضوعات کا احاطہ کرے گا:

- محفوظ اور مؤثر AI ایجنٹس کیسے بنائیں اور ڈپلائے کریں
- AI ایجنٹس تیار کرتے وقت اہم سیکیورٹی پہلو
- AI ایجنٹس تیار کرتے وقت ڈیٹا اور صارف کی رازداری کو کیسے برقرار رکھیں۔

## سیکھنے کے مقاصد

اس سبق کو مکمل کرنے کے بعد، آپ جان سکیں گے کہ:

- AI ایجنٹس بناتے وقت خطرات کی شناخت اور ان کا ازالہ کیسے کریں۔
- سیکیورٹی اقدامات نافذ کریں تاکہ ڈیٹا اور رسائی مناسب طریقے سے منظم ہوں۔
- ایسے AI ایجنٹس بنائیں جو ڈیٹا کی رازداری کو برقرار رکھیں اور معیاری صارف تجربہ فراہم کریں۔

## حفاظت

سب سے پہلے ہم محفوظ ایجنٹ پر مبنی ایپلیکیشنز بنانے کو دیکھتے ہیں۔ حفاظت کا مطلب ہے کہ AI ایجنٹ متعین کردہ طریقے سے کام کرے۔ ایجنٹ پر مبنی ایپلیکیشنز کے بنانے والے کے طور پر، ہمارے پاس حفاظت کو زیادہ سے زیادہ کرنے کے لیے طریقے اور اوزار موجود ہیں:

### سسٹم میسج فریم ورک کی تعمیر

اگر آپ نے کبھی بڑے لسانی ماڈلز (LLMs) استعمال کرتے ہوئے AI ایپلیکیشن بنائی ہے، تو آپ ایک مضبوط سسٹم پرامپٹ یا سسٹم پیغام ڈیزائن کرنے کی اہمیت جانتے ہیں۔ یہ پرامپٹس میٹا قواعد، ہدایات، اور رہنما اصول قائم کرتے ہیں کہ LLM صارف اور ڈیٹا کے ساتھ کیسے تعامل کرے گا۔

AI ایجنٹس کے لیے، سسٹم پرامپٹ اور بھی زیادہ اہم ہے کیونکہ AI ایجنٹس کو ان کاموں کو مکمل کرنے کے لیے بہت مخصوص ہدایات درکار ہوں گی جو ہم نے ان کے لیے ڈیزائن کیے ہیں۔

اسکیل ایبل سسٹم پرامپٹس بنانے کے لیے، ہم اپنی ایپلیکیشن میں ایک یا متعدد ایجنٹس بنانے کے لیے سسٹم میسج فریم ورک استعمال کر سکتے ہیں:

![سسٹم میسج فریم ورک بنانا](../../../translated_images/ur/system-message-framework.3a97368c92d11d68.webp)

#### مرحلہ 1: ایک میٹا سسٹم میسج بنائیں 

میٹا پرامپٹ کا استعمال LLM کے ذریعے ان ایجنٹس کے لیے سسٹم پرامپٹس تیار کرنے کے لیے کیا جائے گا جنہیں ہم بناتے ہیں۔ ہم اسے ایک ٹیمپلیٹ کے طور پر ڈیزائن کرتے ہیں تاکہ اگر ضرورت ہو تو ہم مؤثر طریقے سے متعدد ایجنٹس بنا سکیں۔

یہاں ایک مثال ہے جو ہم LLM کو دے سکتے ہیں:

```plaintext
You are an expert at creating AI agent assistants. 
You will be provided a company name, role, responsibilities and other
information that you will use to provide a system prompt for.
To create the system prompt, be descriptive as possible and provide a structure that a system using an LLM can better understand the role and responsibilities of the AI assistant. 
```

#### مرحلہ 2: ایک بنیادی پرامپٹ بنائیں

اگلا مرحلہ ایک بنیادی پرامپٹ تیار کرنا ہے تاکہ AI ایجنٹ کی وضاحت کی جا سکے۔ آپ کو ایجنٹ کے کردار، وہ کام جو ایجنٹ پورے کرے گا، اور ایجنٹ کی دیگر ذمہ داریاں شامل کرنی چاہئیں۔

مثال درج ذیل ہے:

```plaintext
You are a travel agent for Contoso Travel that is great at booking flights for customers. To help customers you can perform the following tasks: lookup available flights, book flights, ask for preferences in seating and times for flights, cancel any previously booked flights and alert customers on any delays or cancellations of flights.  
```

#### مرحلہ 3: LLM کو بنیادی سسٹم میسج فراہم کریں

اب ہم اس سسٹم میسج کو بہتر بنا سکتے ہیں، میٹا سسٹم میسج کو سسٹم میسج کے طور پر اور ہمارا بنیادی سسٹم میسج فراہم کر کے۔

یہ ایک ایسا سسٹم میسج پیدا کرے گا جو ہمارے AI ایجنٹس کی رہنمائی کے لیے بہتر ڈیزائن کیا گیا ہوگا:

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

#### مرحلہ 4: دہرائیں اور بہتر بنائیں

اس سسٹم میسج فریم ورک کی قدر یہ ہے کہ ایک سے زائد ایجنٹس کے سسٹم میسجز بنانا زیادہ آسان ہو جاتا ہے اور وقت کے ساتھ آپ کے سسٹم میسجز میں بہتری لانا ممکن ہوتا ہے۔ یہ شاذ و نادر ہی ہوتا ہے کہ آپ کا پہلا سسٹم میسج آپ کے مکمل استعمال کے کیس کے لیے بالکل درست ہو۔ بنیادی سسٹم میسج میں چھوٹے چھوٹے تبدیلیاں کر کے اور اسے سسٹم کے ذریعے چلوا کر نتائج کا موازنہ اور جائزہ لینا آپ کو بہتر بنانے میں مدد دے گا۔

## خطرات کو سمجھنا

قابلِ اعتماد AI ایجنٹس بنانے کے لیے، یہ ضروری ہے کہ آپ اپنے AI ایجنٹ کے لیے خطرات اور خطرات کو سمجھیں اور ان کا ازالہ کریں۔ آئیے AI ایجنٹس کے خلاف مختلف خطرات کے صرف چند پہلوؤں کو دیکھتے ہیں اور یہ کہ آپ بہتر منصوبہ بندی اور تیاری کیسے کر سکتے ہیں۔

![خطروں کو سمجھنا](../../../translated_images/ur/understanding-threats.89edeada8a97fc0f.webp)

### کام اور ہدایات

**تفصیل:** حملہ آور کوشش کرتے ہیں کہ پرامپٹنگ یا ان پٹس میں تبدیلی کر کے AI ایجنٹ کی ہدایات یا مقاصد تبدیل کر دیں۔

**احتیاطی اقدامات**: جانچ پڑتال اور ان پٹ فلٹرز نافذ کریں تاکہ ممکنہ طور پر خطرناک پرامپٹس کو AI ایجنٹ کے پروسیس ہونے سے پہلے پکڑا جا سکے۔ چونکہ یہ حملے عموماً ایجنٹ کے ساتھ بار بار تعامل مانگتے ہیں، لہٰذا گفتگو میں ٹرنز کی تعداد محدود کرنا بھی ان قسم کے حملوں کو روکنے کا ایک طریقہ ہے۔

### اہم نظاموں تک رسائی

**تفصیل**: اگر کسی AI ایجنٹ کو ایسے نظاموں اور سروسز تک رسائی حاصل ہو جو حساس ڈیٹا ذخیرہ کرتی ہیں، تو حملہ آور ایجنٹ اور ان سروسز کے درمیان مواصلات کو متاثر کر سکتے ہیں۔ یہ براہِ راست حملے ہو سکتے ہیں یا ایجنٹ کے ذریعے ان نظاموں کے بارے میں معلومات حاصل کرنے کی بالواسطہ کوششیں۔

**احتیاطی اقدامات**: ان قسم کے حملوں کو روکنے کے لیے AI ایجنٹس کو صرف ضرورت کے مطابق نظاموں تک رسائی ہونی چاہیے۔ ایجنٹ اور سسٹم کے درمیان مواصلات بھی محفوظ ہونی چاہئیں۔ توثیق (authentication) اور رسائی کنٹرول نافذ کرنا اس معلومات کے تحفظ کا ایک اور طریقہ ہے۔

### وسائل اور خدمات کا زیادہ بوجھ

**تفصیل:** AI ایجنٹس کام مکمل کرنے کے لیے مختلف ٹولز اور سروسز تک رسائی حاصل کر سکتے ہیں۔ حملہ آور اس صلاحیت کا استعمال کر کے ان سروسز پر AI ایجنٹ کے ذریعے بہت زیادہ درخواستیں بھیج سکتے ہیں، جس کے نتیجے میں نظام ناکام ہو سکتا ہے یا اخراجات بہت بڑھ سکتے ہیں۔

**احتیاطی اقدامات:** کسی سروس کے لیے AI ایجنٹ کی جانب سے بھیجی جانے والی درخواستوں کی تعداد محدود کرنے کے لیے پالیسیاں نافذ کریں۔ اپنے AI ایجنٹ کے ساتھ گفتگو کے ٹرنز اور درخواستوں کی تعداد محدود کرنا بھی ان قسم کے حملوں کو روکنے کا ایک طریقہ ہے۔

### علمی ذخیرے کی زہر آلودگی

**تفصیل:** اس قسم کا حملہ براہِ راست AI ایجنٹ کو نشانہ نہیں بناتا بلکہ اس علمی ذخیرے اور دیگر سروسز کو نشانہ بناتا ہے جو AI ایجنٹ کسی کام کو مکمل کرنے کے لیے استعمال کرے گا۔ اس میں وہ ڈیٹا یا معلومات خراب کرنا شامل ہو سکتا ہے جو AI ایجنٹ ٹاسک مکمل کرنے کے لیے استعمال کرے گا، جس سے صارف کو جانبدار یا غیر مراد جوابات مل سکتے ہیں۔

**احتیاطی اقدامات:** AI ایجنٹ کے ورک فلو میں استعمال ہونے والے ڈیٹا کی باقاعدہ تصدیق کریں۔ اس ڈیٹا تک رسائی کو محفوظ رکھیں اور صرف قابلِ اعتبار افراد ہی اس میں تبدیلی کر سکیں تاکہ اس قسم کے حملوں سے بچا جا سکے۔

### سلسلہ وار غلطیاں

**تفصیل:** AI ایجنٹس مختلف ٹولز اور سروسز تک رسائی حاصل کرتے ہیں تاکہ کام مکمل کر سکیں۔ حملہ آوروں کی وجہ سے پیدا ہونے والی غلطیاں دوسرے نظاموں کی ناکامی کا باعث بن سکتی ہیں جو AI ایجنٹ سے منسلک ہیں، جس سے حملہ زیادہ وسیع پیمانے پر پھیل سکتا ہے اور اس کا ٹroubleshoot مشکل ہو جاتا ہے۔

**احتیاطی اقدامات**: اس سے بچنے کا ایک طریقہ یہ ہے کہ AI ایجنٹ کو محدود ماحول میں چلایا جائے، مثلاً Docker container میں کام انجام دینا، تاکہ براہِ راست نظامی حملوں سے بچاؤ ممکن ہو۔ جب بعض نظام غلطی سے جواب دیں تو بیک اپ میکانزم اور ریٹری لاجک بنانا بڑے نظامی نقصانات کو روکتا ہے۔

## انسانی شمولیت

قابلِ اعتماد AI ایجنٹ سسٹمز بنانے کا ایک اور مؤثر طریقہ انسانی شمولیت (Human-in-the-Loop) استعمال کرنا ہے۔ اس سے ایک ایسا بہاؤ پیدا ہوتا ہے جہاں صارفین رن کے دوران ایجنٹس کو فیڈ بیک فراہم کر سکتے ہیں۔ صارفین بنیادی طور پر ایک ملٹی ایجنٹ سسٹم میں ایجنٹس کی طرح عمل کرتے ہیں اور رننگ پروسیس کی منظوری یا خاتمے کی فراہمی کے ذریعے شمولیت کرتے ہیں۔

![عمل میں انسان](../../../translated_images/ur/human-in-the-loop.5f0068a678f62f4f.webp)

یہاں Microsoft Agent Framework استعمال کرتے ہوئے ایک کوڈ سنیپٹ ہے جو دکھاتا ہے کہ یہ تصور کیسے نافذ کیا جاتا ہے:

```python
import os
from agent_framework.azure import AzureAIProjectAgentProvider
from azure.identity import AzureCliCredential

# انسانی منظوری کے عمل کے ساتھ فراہم کنندہ بنائیں
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

قابلِ اعتماد AI ایجنٹس بنانے کے لیے محتاط ڈیزائن، مضبوط سیکیورٹی اقدامات، اور مسلسل بہتری ضروری ہے۔ ساختی میٹا پرامپٹنگ سسٹمز نافذ کر کے، ممکنہ خطرات کو سمجھ کر، اور تخفیف کی حکمتِ عملیاں اپناتے ہوئے ڈویلپر ایسے AI ایجنٹس بنا سکتے ہیں جو محفوظ بھی ہوں اور مؤثر بھی۔ مزید یہ کہ انسانی شمولیت کا نقطۂ نظر شامل کرنے سے یہ یقینی بنتا ہے کہ AI ایجنٹس صارف کی ضروریات کے مطابق رہیں جبکہ خطرات کم سے کم ہوں۔ جیسا کہ AI ترقی کرتا رہتا ہے، سیکیورٹی، رازداری، اور اخلاقی غور و فکر پر پیشگی توجہ برقرار رکھنا AI سے چلنے والے نظاموں میں اعتماد اور اعتبار پیدا کرنے کی کنجی ہوگی۔

### قابلِ اعتماد AI ایجنٹس بنانے کے بارے میں مزید سوالات ہیں؟

دوسرے سیکھنے والوں سے ملنے، آفس آورز میں شرکت کرنے اور اپنے AI ایجنٹس کے سوالات کے جوابات حاصل کرنے کے لیے [Microsoft Foundry Discord](https://aka.ms/ai-agents/discord) میں شامل ہوں۔

## اضافی وسائل

- <a href="https://learn.microsoft.com/azure/ai-studio/responsible-use-of-ai-overview" target="_blank">ذمہ دار AI کا جائزہ</a>
- <a href="https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai" target="_blank">جنریٹو AI ماڈلز اور AI ایپلیکیشنز کا جائزہ</a>
- <a href="https://learn.microsoft.com/azure/ai-services/openai/concepts/system-message?context=%2Fazure%2Fai-studio%2Fcontext%2Fcontext&tabs=top-techniques" target="_blank">حفاظتی سسٹم پیغامات</a>
- <a href="https://blogs.microsoft.com/wp-content/uploads/prod/sites/5/2022/06/Microsoft-RAI-Impact-Assessment-Template.pdf?culture=en-us&country=us" target="_blank">خطرے کی تشخیص کا سانچہ</a>

## پچھلا سبق

[Agentic RAG](../05-agentic-rag/README.md)

## اگلا سبق

[منصوبہ بندی ڈیزائن پیٹرن](../07-planning-design/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
دستبرداری:
یہ دستاویز AI ترجمہ سروس [Co-op Translator](https://github.com/Azure/co-op-translator) کے ذریعے ترجمہ کی گئی ہے۔ اگرچہ ہم درستگی کے لیے کوشاں ہیں، براہِ کرم نوٹ کریں کہ خودکار ترجمے میں غلطیاں یا عدم درستیاں ہو سکتی ہیں۔ اصل دستاویز کو اس کی مادری زبان میں ہی مستند ماخذ سمجھا جانا چاہیے۔ اہم معلومات کے لیے پیشہ ور انسانی ترجمہ کی سفارش کی جاتی ہے۔ اس ترجمے کے استعمال سے پیدا ہونے والی کسی بھی غلط فہمی یا غلط تعبیر کے لیے ہم ذمہ دار نہیں ہیں۔
<!-- CO-OP TRANSLATOR DISCLAIMER END -->