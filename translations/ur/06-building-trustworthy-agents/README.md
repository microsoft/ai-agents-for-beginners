<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "498802b4c3c3cc486b86f27a12cebb34",
  "translation_date": "2025-08-29T09:30:33+00:00",
  "source_file": "06-building-trustworthy-agents/README.md",
  "language_code": "ur"
}
-->
[![قابل اعتماد AI ایجنٹس](../../../translated_images/lesson-6-thumbnail.a58ab36c099038d4f786c2b0d5d6e89f41f4c2ecc05ab10b67bced2695eeb218.ur.png)](https://youtu.be/iZKkMEGBCUQ?si=Q-kEbcyHUMPoHp8L)

> _(اوپر دی گئی تصویر پر کلک کریں تاکہ اس سبق کی ویڈیو دیکھ سکیں)_

# قابل اعتماد AI ایجنٹس بنانا

## تعارف

اس سبق میں شامل ہوگا:

- محفوظ اور مؤثر AI ایجنٹس بنانے اور تعینات کرنے کا طریقہ
- AI ایجنٹس تیار کرتے وقت اہم حفاظتی پہلوؤں پر غور
- AI ایجنٹس تیار کرتے وقت ڈیٹا اور صارف کی پرائیویسی کو برقرار رکھنے کا طریقہ

## سیکھنے کے مقاصد

اس سبق کو مکمل کرنے کے بعد، آپ جان سکیں گے کہ:

- AI ایجنٹس بناتے وقت خطرات کی شناخت اور ان کا سدباب کیسے کریں۔
- ڈیٹا اور رسائی کو مناسب طریقے سے منظم کرنے کے لیے حفاظتی اقدامات نافذ کریں۔
- ایسے AI ایجنٹس بنائیں جو ڈیٹا کی پرائیویسی برقرار رکھیں اور صارفین کو معیاری تجربہ فراہم کریں۔

## حفاظت

سب سے پہلے محفوظ ایجنٹک ایپلیکیشنز بنانے پر نظر ڈالتے ہیں۔ حفاظت کا مطلب ہے کہ AI ایجنٹ وہی کام کرے جو اس کے لیے ڈیزائن کیا گیا ہے۔ ایجنٹک ایپلیکیشنز کے تخلیق کاروں کے طور پر، ہمارے پاس حفاظت کو زیادہ سے زیادہ کرنے کے لیے طریقے اور اوزار موجود ہیں:

### سسٹم میسج فریم ورک بنانا

اگر آپ نے کبھی بڑے زبان کے ماڈلز (LLMs) کا استعمال کرتے ہوئے AI ایپلیکیشن بنائی ہے، تو آپ جانتے ہیں کہ مضبوط سسٹم پرامپٹ یا سسٹم میسج ڈیزائن کرنا کتنا اہم ہے۔ یہ پرامپٹس وہ اصول، ہدایات، اور رہنما خطوط قائم کرتے ہیں جن کے تحت LLM صارف اور ڈیٹا کے ساتھ تعامل کرے گا۔

AI ایجنٹس کے لیے، سسٹم پرامپٹ اور بھی زیادہ اہم ہے کیونکہ AI ایجنٹس کو ان کاموں کو مکمل کرنے کے لیے انتہائی مخصوص ہدایات کی ضرورت ہوگی جو ہم نے ان کے لیے ڈیزائن کیے ہیں۔

اسکیل ایبل سسٹم پرامپٹس بنانے کے لیے، ہم اپنی ایپلیکیشن میں ایک یا زیادہ ایجنٹس بنانے کے لیے سسٹم میسج فریم ورک استعمال کر سکتے ہیں:

![سسٹم میسج فریم ورک بنانا](../../../translated_images/system-message-framework.3a97368c92d11d6814577b03cd128ec8c71a5fd1e26f341835cfa5df59ae87ae.ur.png)

#### مرحلہ 1: میٹا سسٹم میسج بنائیں

میٹا پرامپٹ LLM کے ذریعے ان ایجنٹس کے سسٹم پرامپٹس بنانے کے لیے استعمال ہوگا جو ہم تخلیق کرتے ہیں۔ ہم اسے ایک ٹیمپلیٹ کے طور پر ڈیزائن کرتے ہیں تاکہ ضرورت پڑنے پر کئی ایجنٹس کو مؤثر طریقے سے بنایا جا سکے۔

یہاں ایک مثال ہے کہ ہم LLM کو میٹا سسٹم میسج کیسے دیں گے:

```plaintext
You are an expert at creating AI agent assistants. 
You will be provided a company name, role, responsibilities and other
information that you will use to provide a system prompt for.
To create the system prompt, be descriptive as possible and provide a structure that a system using an LLM can better understand the role and responsibilities of the AI assistant. 
```

#### مرحلہ 2: ایک بنیادی پرامپٹ بنائیں

اگلا مرحلہ AI ایجنٹ کی وضاحت کے لیے ایک بنیادی پرامپٹ بنانا ہے۔ آپ کو ایجنٹ کا کردار، وہ کام جو ایجنٹ مکمل کرے گا، اور ایجنٹ کی دیگر ذمہ داریوں کو شامل کرنا چاہیے۔

یہاں ایک مثال ہے:

```plaintext
You are a travel agent for Contoso Travel that is great at booking flights for customers. To help customers you can perform the following tasks: lookup available flights, book flights, ask for preferences in seating and times for flights, cancel any previously booked flights and alert customers on any delays or cancellations of flights.  
```

#### مرحلہ 3: بنیادی سسٹم میسج LLM کو فراہم کریں

اب ہم اس سسٹم میسج کو بہتر بنا سکتے ہیں، میٹا سسٹم میسج کو سسٹم میسج کے طور پر فراہم کر کے اور ہمارا بنیادی سسٹم میسج شامل کر کے۔

یہ ایک ایسا سسٹم میسج تیار کرے گا جو ہمارے AI ایجنٹس کی رہنمائی کے لیے بہتر ڈیزائن کیا گیا ہو:

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

#### مرحلہ 4: تکرار کریں اور بہتر بنائیں

اس سسٹم میسج فریم ورک کی قدر یہ ہے کہ یہ کئی ایجنٹس کے لیے سسٹم میسجز بنانا آسان بناتا ہے اور وقت کے ساتھ ساتھ آپ کے سسٹم میسجز کو بہتر بناتا ہے۔ یہ کم ہی ہوتا ہے کہ آپ کا سسٹم میسج پہلی بار مکمل طور پر آپ کے استعمال کے کیس کے لیے کام کرے۔ بنیادی سسٹم میسج میں چھوٹے چھوٹے تبدیلیاں کر کے اور اسے سسٹم کے ذریعے چلانے سے آپ نتائج کا موازنہ اور جائزہ لے سکتے ہیں۔

## خطرات کو سمجھنا

قابل اعتماد AI ایجنٹس بنانے کے لیے، یہ ضروری ہے کہ آپ اپنے AI ایجنٹ کے خطرات اور دھمکیوں کو سمجھیں اور ان کا سدباب کریں۔ آئیے AI ایجنٹس کے مختلف خطرات اور ان سے بہتر منصوبہ بندی اور تیاری کے طریقوں پر نظر ڈالتے ہیں۔

![خطرات کو سمجھنا](../../../translated_images/understanding-threats.89edeada8a97fc0f7053558567d5dd27c0c333b74e47fffdde490fa6777a4c17.ur.png)

### کام اور ہدایات

**تفصیل:** حملہ آور AI ایجنٹ کی ہدایات یا اہداف کو پرامپٹنگ یا ان پٹ میں تبدیلی کے ذریعے بدلنے کی کوشش کرتے ہیں۔

**سدباب:** ممکنہ خطرناک پرامپٹس کا پتہ لگانے کے لیے توثیق کے چیک اور ان پٹ فلٹرز نافذ کریں، اس سے پہلے کہ وہ AI ایجنٹ کے ذریعے پروسیس ہوں۔ چونکہ یہ حملے عام طور پر ایجنٹ کے ساتھ بار بار تعامل کی ضرورت رکھتے ہیں، گفتگو میں ٹرنز کی تعداد کو محدود کرنا ان حملوں کو روکنے کا ایک اور طریقہ ہے۔

### اہم نظاموں تک رسائی

**تفصیل:** اگر AI ایجنٹ کو ان نظاموں اور خدمات تک رسائی حاصل ہو جو حساس ڈیٹا ذخیرہ کرتے ہیں، تو حملہ آور ایجنٹ اور ان خدمات کے درمیان مواصلات کو نقصان پہنچا سکتے ہیں۔ یہ براہ راست حملے یا ایجنٹ کے ذریعے ان نظاموں کے بارے میں معلومات حاصل کرنے کی کوششیں ہو سکتی ہیں۔

**سدباب:** AI ایجنٹس کو صرف ضرورت کے مطابق نظاموں تک رسائی دی جانی چاہیے تاکہ ان حملوں کو روکا جا سکے۔ ایجنٹ اور نظام کے درمیان مواصلات کو بھی محفوظ بنایا جانا چاہیے۔ تصدیق اور رسائی کنٹرول نافذ کرنا اس معلومات کو محفوظ رکھنے کا ایک اور طریقہ ہے۔

### وسائل اور خدمات کا زیادہ استعمال

**تفصیل:** AI ایجنٹس مختلف ٹولز اور خدمات تک رسائی حاصل کر سکتے ہیں تاکہ کام مکمل کر سکیں۔ حملہ آور اس صلاحیت کو ان خدمات پر حملہ کرنے کے لیے استعمال کر سکتے ہیں، AI ایجنٹ کے ذریعے بڑی تعداد میں درخواستیں بھیج کر، جس کے نتیجے میں نظام کی ناکامی یا زیادہ اخراجات ہو سکتے ہیں۔

**سدباب:** AI ایجنٹ کو کسی خدمت کے لیے درخواستوں کی تعداد محدود کرنے کی پالیسیاں نافذ کریں۔ گفتگو کے ٹرنز اور AI ایجنٹ کو دی جانے والی درخواستوں کی تعداد کو محدود کرنا ان حملوں کو روکنے کا ایک اور طریقہ ہے۔

### نالج بیس کو خراب کرنا

**تفصیل:** اس قسم کا حملہ براہ راست AI ایجنٹ کو نشانہ نہیں بناتا بلکہ نالج بیس اور دیگر خدمات کو نشانہ بناتا ہے جنہیں AI ایجنٹ استعمال کرے گا۔ اس میں ڈیٹا یا معلومات کو خراب کرنا شامل ہو سکتا ہے جسے AI ایجنٹ کام مکمل کرنے کے لیے استعمال کرے گا، جس کے نتیجے میں صارف کو متعصب یا غیر ارادی جوابات مل سکتے ہیں۔

**سدباب:** AI ایجنٹ کے ورک فلو میں استعمال ہونے والے ڈیٹا کی باقاعدہ تصدیق کریں۔ اس بات کو یقینی بنائیں کہ اس ڈیٹا تک رسائی محفوظ ہے اور صرف قابل اعتماد افراد کے ذریعے تبدیل کی گئی ہے تاکہ اس قسم کے حملے سے بچا جا سکے۔

### سلسلہ وار غلطیاں

**تفصیل:** AI ایجنٹس مختلف ٹولز اور خدمات تک رسائی حاصل کرتے ہیں تاکہ کام مکمل کر سکیں۔ حملہ آوروں کی وجہ سے ہونے والی غلطیاں ان دیگر نظاموں کی ناکامی کا باعث بن سکتی ہیں جن سے AI ایجنٹ جڑا ہوا ہے، جس سے حملہ زیادہ وسیع اور حل کرنے میں مشکل ہو جاتا ہے۔

**سدباب:** اس سے بچنے کا ایک طریقہ یہ ہے کہ AI ایجنٹ کو محدود ماحول میں کام کرنے دیں، جیسے کہ ڈوکر کنٹینر میں کام کرنا، تاکہ براہ راست نظام حملوں کو روکا جا سکے۔ جب کچھ نظام غلطی کے ساتھ جواب دیں تو فال بیک میکانزم اور ریٹری لاجک بنانا بڑے نظام کی ناکامیوں کو روکنے کا ایک اور طریقہ ہے۔

## انسان کو شامل کرنا

قابل اعتماد AI ایجنٹ سسٹمز بنانے کا ایک اور مؤثر طریقہ انسان کو شامل کرنا ہے۔ یہ ایک ایسا فلو بناتا ہے جہاں صارفین ایجنٹس کو چلانے کے دوران فیڈبیک فراہم کر سکتے ہیں۔ صارفین بنیادی طور پر ایک ملٹی ایجنٹ سسٹم میں ایجنٹس کے طور پر کام کرتے ہیں اور چلنے والے عمل کی منظوری یا ختم کرنے کی صلاحیت رکھتے ہیں۔

![انسان کو شامل کرنا](../../../translated_images/human-in-the-loop.5f0068a678f62f4fc8373d5b78c4c22f35d9e4da35c93f66c3b634c1774eff34.ur.png)

یہاں ایک کوڈ اسنیپٹ ہے جو AutoGen کا استعمال کرتے ہوئے اس تصور کو نافذ کرنے کا طریقہ دکھاتا ہے:

```python

# Create the agents.
model_client = OpenAIChatCompletionClient(model="gpt-4o-mini")
assistant = AssistantAgent("assistant", model_client=model_client)
user_proxy = UserProxyAgent("user_proxy", input_func=input)  # Use input() to get user input from console.

# Create the termination condition which will end the conversation when the user says "APPROVE".
termination = TextMentionTermination("APPROVE")

# Create the team.
team = RoundRobinGroupChat([assistant, user_proxy], termination_condition=termination)

# Run the conversation and stream to the console.
stream = team.run_stream(task="Write a 4-line poem about the ocean.")
# Use asyncio.run(...) when running in a script.
await Console(stream)

```

## نتیجہ

قابل اعتماد AI ایجنٹس بنانا محتاط ڈیزائن، مضبوط حفاظتی اقدامات، اور مسلسل بہتری کا تقاضا کرتا ہے۔ ساختی میٹا پرامپٹنگ سسٹمز کو نافذ کر کے، ممکنہ خطرات کو سمجھ کر، اور سدباب کی حکمت عملیوں کو اپنانے سے، ڈویلپرز محفوظ اور مؤثر AI ایجنٹس بنا سکتے ہیں۔ مزید برآں، انسان کو شامل کرنے کا طریقہ AI ایجنٹس کو صارف کی ضروریات کے مطابق رکھنے اور خطرات کو کم کرنے کو یقینی بناتا ہے۔ جیسے جیسے AI ترقی کرتا ہے، سیکیورٹی، پرائیویسی، اور اخلاقی پہلوؤں پر فعال موقف برقرار رکھنا AI سے چلنے والے نظاموں میں اعتماد اور قابل اعتمادیت کو فروغ دینے کی کلید ہوگا۔

### قابل اعتماد AI ایجنٹس بنانے کے بارے میں مزید سوالات ہیں؟

[Azure AI Foundry Discord](https://aka.ms/ai-agents/discord) میں شامل ہوں تاکہ دیگر سیکھنے والوں سے ملاقات کریں، آفس آورز میں شرکت کریں، اور اپنے AI ایجنٹس کے سوالات کے جوابات حاصل کریں۔

## اضافی وسائل

- <a href="https://learn.microsoft.com/azure/ai-studio/responsible-use-of-ai-overview" target="_blank">ذمہ دار AI کا جائزہ</a>
- <a href="https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai" target="_blank">جنریٹو AI ماڈلز اور AI ایپلیکیشنز کا جائزہ</a>
- <a href="https://learn.microsoft.com/azure/ai-services/openai/concepts/system-message?context=%2Fazure%2Fai-studio%2Fcontext%2Fcontext&tabs=top-techniques" target="_blank">حفاظتی سسٹم میسجز</a>
- <a href="https://blogs.microsoft.com/wp-content/uploads/prod/sites/5/2022/06/Microsoft-RAI-Impact-Assessment-Template.pdf?culture=en-us&country=us" target="_blank">خطرے کی تشخیص کا ٹیمپلیٹ</a>

## پچھلا سبق

[ایجنٹک RAG](../05-agentic-rag/README.md)

## اگلا سبق

[پلاننگ ڈیزائن پیٹرن](../07-planning-design/README.md)

---

**ڈسکلیمر**:  
یہ دستاویز AI ترجمہ سروس [Co-op Translator](https://github.com/Azure/co-op-translator) کا استعمال کرتے ہوئے ترجمہ کی گئی ہے۔ ہم درستگی کے لیے کوشش کرتے ہیں، لیکن براہ کرم آگاہ رہیں کہ خودکار ترجمے میں غلطیاں یا عدم درستگی ہو سکتی ہیں۔ اصل دستاویز، جو اس کی اصل زبان میں ہے، کو مستند ذریعہ سمجھا جانا چاہیے۔ اہم معلومات کے لیے، پیشہ ور انسانی ترجمہ کی سفارش کی جاتی ہے۔ اس ترجمے کے استعمال سے پیدا ہونے والی کسی بھی غلط فہمی یا غلط تشریح کے لیے ہم ذمہ دار نہیں ہیں۔