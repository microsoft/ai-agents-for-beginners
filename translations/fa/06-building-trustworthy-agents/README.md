[![عامل‌های هوش مصنوعی قابل اعتماد](../../../translated_images/fa/lesson-6-thumbnail.a58ab36c099038d4.webp)](https://youtu.be/iZKkMEGBCUQ?si=Q-kEbcyHUMPoHp8L)

> _(برای مشاهده ویدئوی این درس روی تصویر بالا کلیک کنید)_

# ساخت عامل‌های هوش مصنوعی قابل اعتماد

## مقدمه

این درس شامل موارد زیر است:

- نحوه ساخت و راه‌اندازی عامل‌های هوش مصنوعی ایمن و موثر
- ملاحظات مهم امنیتی هنگام توسعه عامل‌های هوش مصنوعی.
- نحوه حفظ محرمانگی داده‌ها و کاربران هنگام توسعه عامل‌های هوش مصنوعی.

## اهداف یادگیری

پس از اتمام این درس، شما خواهید دانست چگونه:

- خطرات هنگام ایجاد عامل‌های هوش مصنوعی را شناسایی و کاهش دهید.
- اقدامات امنیتی را به منظور مدیریت صحیح داده‌ها و دسترسی‌ها اجرا کنید.
- عامل‌های هوش مصنوعی بسازید که محرمانگی داده‌ها را حفظ کرده و تجربه کاربری با کیفیتی ارائه دهند.

## ایمنی

ابتدا بیایید به ساخت برنامه‌های عاملیت‌دار ایمن بپردازیم. ایمنی به معنای عملکرد عامل هوش مصنوعی طبق طراحی است. به عنوان سازندگان برنامه‌های عاملیت‌دار، ما روش‌ها و ابزارهایی برای حداکثر کردن ایمنی داریم:

### ساخت چارچوب پیام سیستمی

اگر تا به حال برنامه‌ای با استفاده از مدل‌های زبان بزرگ (LLMs) ساخته‌اید، اهمیت طراحی یک دستور یا پیام سیستمی قوی را می‌دانید. این دستورات قواعد کلان، راهنماها و دستورالعمل‌هایی را تعیین می‌کنند که چگونه مدل زبان بزرگ با کاربر و داده‌ها تعامل خواهد داشت.

برای عامل‌های هوش مصنوعی، پیام سیستمی اهمیت بیشتری دارد زیرا عامل‌ها به دستورالعمل‌های بسیار خاصی نیاز دارند تا وظایفی که برایشان طراحی کرده‌ایم را انجام دهند.

برای ایجاد دستورات سیستمی قابل مقیاس، می‌توانیم از یک چارچوب پیام سیستمی برای ساخت یک یا چند عامل در برنامه خود استفاده کنیم:

![ساخت چارچوب پیام سیستمی](../../../translated_images/fa/system-message-framework.3a97368c92d11d68.webp)

#### گام ۱: ایجاد پیام سیستمی متا

دستور متا توسط یک مدل زبان بزرگ برای تولید دستورات سیستمی برای عامل‌هایی که ایجاد می‌کنیم استفاده خواهد شد. آن را به صورت قالب طراحی می‌کنیم تا در صورت نیاز بتوانیم به صورت مؤثر چندین عامل ایجاد کنیم.

در اینجا نمونه‌ای از پیام سیستمی متا که به مدل زبان بزرگ می‌دهیم آمده است:

```plaintext
You are an expert at creating AI agent assistants. 
You will be provided a company name, role, responsibilities and other
information that you will use to provide a system prompt for.
To create the system prompt, be descriptive as possible and provide a structure that a system using an LLM can better understand the role and responsibilities of the AI assistant. 
```

#### گام ۲: ساخت یک دستور پایه

گام بعدی ایجاد یک دستور پایه است برای توصیف عامل هوش مصنوعی. باید نقش عامل، وظایفی که عامل انجام می‌دهد و هر مسئولیت دیگر عامل را درج کنید.

نمونه‌ای از آن به این صورت است:

```plaintext
You are a travel agent for Contoso Travel that is great at booking flights for customers. To help customers you can perform the following tasks: lookup available flights, book flights, ask for preferences in seating and times for flights, cancel any previously booked flights and alert customers on any delays or cancellations of flights.  
```

#### گام ۳: ارائه پیام سیستمی پایه به مدل زبان بزرگ

اکنون می‌توانیم این پیام سیستمی را با ارائه پیام سیستمی متا به عنوان پیام سیستمی و پیام سیستمی پایه بهینه کنیم.

این کار یک پیام سیستمی می‌سازد که بهتر برای راهنمایی عامل‌های هوش مصنوعی ما طراحی شده است:

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

#### گام ۴: تکرار و بهبود

ارزش این چارچوب پیام سیستمی در توانایی مقیاس دادن ایجاد پیام‌های سیستمی از چندین عامل است و همچنین در بهبود پیام‌های سیستمی شما در طول زمان. به ندرت پیش می‌آید که پیام سیستمی که برای حالت کامل مورد استفاده شما در بار اول کار کند. توانایی ایجاد تغییرات کوچک و بهبودها با تغییر پیام سیستمی پایه و اجرای آن از طریق سیستم به شما اجازه می‌دهد تا نتایج را مقایسه و ارزیابی کنید.

## درک تهدیدات

برای ساخت عامل‌های هوش مصنوعی قابل اعتماد، مهم است که خطرات و تهدیدات علیه عامل هوش مصنوعی خود را بشناسید و کاهش دهید. بیایید تنها به چند تهدید مختلف علیه عامل‌های هوش مصنوعی و چگونگی برنامه‌ریزی و آماده‌سازی بهتر برای آنها نگاه کنیم.

![درک تهدیدات](../../../translated_images/fa/understanding-threats.89edeada8a97fc0f.webp)

### وظیفه و دستورالعمل

**توضیح:** مهاجمان تلاش می‌کنند دستورات یا اهداف عامل هوش مصنوعی را از طریق درخواست‌های ورودی یا دستکاری تغییر دهند.

**کاهش خطر:** اجرای بررسی‌های اعتبارسنجی و فیلترهای ورودی برای شناسایی درخواست‌های خطرناک احتمالی قبل از پردازش توسط عامل هوش مصنوعی. از آنجا که این حملات معمولاً نیاز به تعامل مکرر با عامل دارند، محدود کردن تعداد گردش‌های مکالمه نیز راهی دیگر برای جلوگیری از این نوع حملات است.

### دسترسی به سیستم‌های حیاتی

**توضیح:** اگر عامل هوش مصنوعی به سیستم‌ها و سرویس‌هایی که داده‌های حساس را ذخیره می‌کنند دسترسی داشته باشد، مهاجمان می‌توانند ارتباط بین عامل و این سرویس‌ها را مختل کنند. این ممکن است حملات مستقیم یا تلاش‌های غیرمستقیم برای کسب اطلاعات درباره این سیستم‌ها از طریق عامل باشد.

**کاهش خطر:** عامل‌های هوش مصنوعی باید فقط در صورت نیاز به سیستم‌ها دسترسی داشته باشند تا از این نوع حملات جلوگیری شود. ارتباط بین عامل و سیستم نیز باید ایمن باشد. اجرای احراز هویت و کنترل دسترسی راهی دیگر برای محافظت از این اطلاعات است.

### بارگذاری بیش از حد منابع و خدمات

**توضیح:** عامل‌های هوش مصنوعی می‌توانند از ابزارها و خدمات مختلفی برای انجام وظایف استفاده کنند. مهاجمان می‌توانند از این قابلیت برای حمله به این خدمات با ارسال حجم بالایی از درخواست‌ها از طریق عامل هوش مصنوعی استفاده کنند، که ممکن است به خرابی سیستم یا هزینه‌های بالا منجر شود.

**کاهش خطر:** سیاست‌هایی برای محدود کردن تعداد درخواست‌هایی که یک عامل هوش مصنوعی می‌تواند به یک سرویس ارسال کند، پیاده‌سازی کنید. محدود کردن تعداد گردش‌های مکالمه و درخواست‌ها به عامل هوش مصنوعی شما نیز راهی دیگر برای جلوگیری از این نوع حملات است.

### مسمومیت پایگاه دانش

**توضیح:** این نوع حمله مستقیماً عامل هوش مصنوعی را هدف نمی‌گیرد بلکه پایگاه دانش و سایر خدماتی که عامل استفاده می‌کند را هدف قرار می‌دهد. این می‌تواند شامل خراب کردن داده یا اطلاعاتی باشد که عامل برای انجام وظایف از آن استفاده می‌کند و منجر به پاسخ‌های جانبدارانه یا ناخواسته به کاربر شود.

**کاهش خطر:** بررسی منظم داده‌هایی که عامل هوش مصنوعی در جریان‌های کاری خود استفاده می‌کند انجام دهید. اطمینان حاصل کنید که دسترسی به این داده‌ها ایمن است و فقط توسط افراد معتمد تغییر می‌کند تا از این نوع حملات جلوگیری شود.

### خطاهای زنجیره‌ای

**توضیح:** عامل‌های هوش مصنوعی به ابزارها و سرویس‌های مختلفی برای انجام وظایف دسترسی دارند. خطاهایی که توسط مهاجمان ایجاد می‌شود می‌تواند منجر به خرابی سیستم‌های دیگری شود که عامل به آنها متصل است و باعث می‌شود حمله گسترده‌تر شده و عیب‌یابی آن دشوارتر شود.

**کاهش خطر:** یکی از روش‌ها برای جلوگیری از این موضوع این است که عامل هوش مصنوعی در محیط محدود شده‌ای مانند اجرای وظایف در یک کانتینر داکر کار کند، که از حملات مستقیم به سیستم جلوگیری می‌کند. ایجاد مکانیزم‌های پشتیبانی و منطق آزمون مجدد هنگام پاسخ خطا از برخی سیستم‌ها، راهی دیگر برای جلوگیری از خرابی‌های گسترده‌تر سیستم است.

## انسان در حلقه

راه مؤثر دیگری برای ساخت سیستم‌های عامل هوش مصنوعی قابل اعتماد، استفاده از روشی است که انسان در حلقه باشد. این روش جریان کاری ایجاد می‌کند که کاربران بتوانند در طول اجرای کار به عامل‌ها بازخورد دهند. کاربران عملاً به عنوان عامل در یک سیستم چندعامله عمل می‌کنند و با ارائه تأیید یا توقف فرآیند در حال اجرا.

![انسان در حلقه](../../../translated_images/fa/human-in-the-loop.5f0068a678f62f4f.webp)

در اینجا یک قطعه کد با استفاده از چارچوب Microsoft Agent آمده است که نشان می‌دهد این مفهوم چگونه پیاده‌سازی شده است:

```python
import os
from agent_framework.azure import AzureAIProjectAgentProvider
from azure.identity import AzureCliCredential

# ارائه‌دهنده را با تأیید انسان در حلقه ایجاد کنید
provider = AzureAIProjectAgentProvider(
    credential=AzureCliCredential(),
)

# عامل را با مرحله تأیید انسانی ایجاد کنید
response = provider.create_response(
    input="Write a 4-line poem about the ocean.",
    instructions="You are a helpful assistant. Ask for user approval before finalizing.",
)

# کاربر می‌تواند پاسخ را بررسی و تأیید کند
print(response.output_text)
user_input = input("Do you approve? (APPROVE/REJECT): ")
if user_input == "APPROVE":
    print("Response approved.")
else:
    print("Response rejected. Revising...")
```

## نتیجه‌گیری

ساخت عامل‌های هوش مصنوعی قابل اعتماد نیازمند طراحی دقیق، اقدامات امنیتی قوی و تکرار مستمر است. با پیاده‌سازی سیستم‌های ساختارمند متا پرامپتینگ، درک تهدیدات احتمالی و اتخاذ راهکارهای کاهش خطر، توسعه‌دهندگان می‌توانند عامل‌هایی بسازند که هم ایمن و هم موثر باشند. علاوه بر این، استفاده از روش انسان در حلقه تضمین می‌کند که عامل‌های هوش مصنوعی با نیازهای کاربران هماهنگ مانده و خطرات به حداقل برسد. با پیشرفت هوش مصنوعی، حفظ رویکردی پیشگیرانه در زمینه امنیت، حریم خصوصی و ملاحظات اخلاقی کلید ایجاد اعتماد و اطمینان‌پذیری در سیستم‌های مبتنی بر هوش مصنوعی خواهد بود.

### سوالات بیشتری درباره ساخت عامل‌های هوش مصنوعی قابل اعتماد دارید؟

به [Microsoft Foundry Discord](https://aka.ms/ai-agents/discord) بپیوندید تا با دیگر یادگیرندگان ملاقات کنید، در ساعات اداری شرکت کنید و به سوالات خود درباره عامل‌های هوش مصنوعی پاسخ بگیرید.

## منابع اضافی

- <a href="https://learn.microsoft.com/azure/ai-studio/responsible-use-of-ai-overview" target="_blank">نمای کلی هوش مصنوعی مسئولانه</a>
- <a href="https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai" target="_blank">ارزیابی مدل‌ها و برنامه‌های هوش مصنوعی مولد</a>
- <a href="https://learn.microsoft.com/azure/ai-services/openai/concepts/system-message?context=%2Fazure%2Fai-studio%2Fcontext%2Fcontext&tabs=top-techniques" target="_blank">پیام‌های سیستمی ایمنی</a>
- <a href="https://blogs.microsoft.com/wp-content/uploads/prod/sites/5/2022/06/Microsoft-RAI-Impact-Assessment-Template.pdf?culture=en-us&country=us" target="_blank">قالب ارزیابی ریسک</a>

## درس قبلی

[عامل RAG](../05-agentic-rag/README.md)

## درس بعد

[الگوی طراحی برنامه‌ریزی](../07-planning-design/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**سلب مسئولیت**:  
این سند با استفاده از سرویس ترجمه ماشینی [Co-op Translator](https://github.com/Azure/co-op-translator) ترجمه شده است. در حالی که ما در تلاش برای دقت هستیم، لطفاً توجه داشته باشید که ترجمه‌های خودکار ممکن است حاوی خطاها یا نادرستی‌هایی باشند. سند اصلی به زبان بومی خود باید به عنوان منبع معتبر در نظر گرفته شود. برای اطلاعات حیاتی، ترجمه حرفه‌ای انسانی توصیه می‌شود. ما مسئول هیچ گونه سوءتفاهم یا تفسیر نادرست ناشی از استفاده از این ترجمه نیستیم.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->