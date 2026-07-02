[![عامل‌های هوش مصنوعی قابل اعتماد](../../../translated_images/fa/lesson-6-thumbnail.a58ab36c099038d4.webp)](https://youtu.be/iZKkMEGBCUQ?si=Q-kEbcyHUMPoHp8L)

> _(برای مشاهده ویدئوی این درس روی تصویر بالا کلیک کنید)_

# ساخت عامل‌های هوش مصنوعی قابل اعتماد

## مقدمه

این درس شامل موارد زیر است:

- چگونه عامل‌های هوش مصنوعی ایمن و مؤثر بسازیم و مستقر کنیم
- ملاحظات مهم امنیتی هنگام توسعه عامل‌های هوش مصنوعی
- چگونگی حفظ داده‌ها و حریم خصوصی کاربران هنگام توسعه عامل‌های هوش مصنوعی

## اهداف یادگیری

پس از اتمام این درس، شما خواهید دانست چگونه:

- خطرات هنگام ایجاد عامل‌های هوش مصنوعی را شناسایی و کاهش دهید.
- اقدامات امنیتی را برای اطمینان از مدیریت صحیح داده‌ها و دسترسی پیاده‌سازی کنید.
- عامل‌های هوش مصنوعی بسازید که حریم خصوصی داده‌ها را حفظ کرده و تجربه کاربری با کیفیت را فراهم کنند.

## ایمنی

ابتدا بیایید به ساخت برنامه‌های عاملی ایمن نگاه کنیم. ایمنی یعنی عامل هوش مصنوعی همان‌گونه که طراحی شده عمل کند. به‌عنوان سازندگان برنامه‌های عاملی، روش‌ها و ابزارهایی برای حداکثرسازی ایمنی داریم:

### ساخت چارچوب پیام سیستمی

اگر تاکنون برنامه هوش مصنوعی با مدل‌های زبانی بزرگ (LLM) ساخته‌اید، اهمیت طراحی یک راه‌انداز یا پیام سیستمی قوی را می‌دانید. این پیام‌ها قوانین متا، دستورالعمل‌ها و راهنمایی‌های مربوط به نحوه تعامل مدل زبانی بزرگ با کاربر و داده‌ها را تعیین می‌کنند.

برای عامل‌های هوش مصنوعی، پیام سیستمی اهمیت بیشتری دارد چون عامل‌ها به دستورالعمل‌های بسیار خاصی نیاز دارند تا کارهایی که برای آن‌ها طراحی کرده‌ایم را انجام دهند.

برای ایجاد پیام‌های سیستمی مقیاس‌پذیر، می‌توانیم از چارچوب پیام سیستمی برای ساخت یک یا چند عامل در برنامه‌مان استفاده کنیم:

![ساخت چارچوب پیام سیستمی](../../../translated_images/fa/system-message-framework.3a97368c92d11d68.webp)

#### گام ۱: ایجاد پیام متا سیستم

پیام متا توسط یک مدل زبانی بزرگ استفاده می‌شود تا پیام‌های سیستمی برای عامل‌هایی که می‌سازیم ایجاد کند. آن را به‌صورت یک قالب طراحی می‌کنیم تا به صورت کارآمد چندین عامل در صورت نیاز بسازیم.

در اینجا نمونه‌ای از پیام متا برای مدل زبانی بزرگ داریم:

```plaintext
You are an expert at creating AI agent assistants. 
You will be provided a company name, role, responsibilities and other
information that you will use to provide a system prompt for.
To create the system prompt, be descriptive as possible and provide a structure that a system using an LLM can better understand the role and responsibilities of the AI assistant. 
```

#### گام ۲: ایجاد یک راه‌انداز پایه

قدم بعدی ایجاد یک راه‌انداز پایه برای توصیف عامل هوش مصنوعی است. شما باید نقش عامل، کارهایی که عامل انجام می‌دهد و سایر مسئولیت‌های عامل را شامل کنید.

در اینجا مثالی آورده شده است:

```plaintext
You are a travel agent for Contoso Travel that is great at booking flights for customers. To help customers you can perform the following tasks: lookup available flights, book flights, ask for preferences in seating and times for flights, cancel any previously booked flights and alert customers on any delays or cancellations of flights.  
```

#### گام ۳: ارائه پیام پایه سیستم به مدل زبانی بزرگ

اکنون می‌توانیم این پیام سیستم را بهینه کنیم با ارائه پیام متا سیستم به‌عنوان پیام سیستمی و پیام پایه سیستم خودمان.

این باعث تولید پیامی می‌شود که برای هدایت عامل‌های هوش مصنوعی ما بهتر طراحی شده است:

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

ارزش این چارچوب پیام سیستمی این است که بتوان پیام‌های سیستمی مرتبط با چندین عامل را آسان‌تر مقیاس داد و همچنین پیام‌های خود را با گذشت زمان بهبود داد. به‌ندرت پیش می‌آید که یک پیام سیستم دفعه اول به طور کامل برای کل مورد استفاده شما کار کند. توانایی ایجاد تغییرات کوچک و بهبودها با تغییر پیام پایه سیستم و اجرای آن از طریق سیستم به شما اجازه می‌دهد تا نتایج را مقایسه و ارزیابی کنید.

## درک تهدیدها

برای ساخت عامل‌های هوش مصنوعی قابل اعتماد، مهم است که خطرات و تهدیدها به عامل خود را درک و کاهش دهید. بیایید فقط به برخی از تهدیدها به عامل‌های هوش مصنوعی و شیوه‌هایی که بهتر برنامه‌ریزی و آماده شویم نگاه کنیم.

![درک تهدیدها](../../../translated_images/fa/understanding-threats.89edeada8a97fc0f.webp)

### کار و دستورالعمل

**توضیح:** مهاجمان سعی می‌کنند دستورالعمل‌ها یا اهداف عامل هوش مصنوعی را از طریق راه‌اندازی راهنما یا دستکاری ورودی‌ها تغییر دهند.

**کاهش:** بررسی صحت و فیلترهای ورودی را اجرا کنید تا راهنماهای بالقوه خطرناک قبل از پردازش توسط عامل شناسایی شوند. چون این حملات معمولاً نیاز به تعامل مکرر با عامل دارند، محدود کردن تعداد نوبت‌های مکالمه یکی دیگر از راه‌ها برای جلوگیری از این نوع حملات است.

### دسترسی به سیستم‌های حیاتی

**توضیح:** اگر عامل هوش مصنوعی به سیستم‌ها و خدماتی که داده‌های حساس ذخیره می‌کنند دسترسی داشته باشد، مهاجمان می‌توانند ارتباط بین عامل و این خدمات را مختل کنند. این ممکن است حملات مستقیم یا تلاش‌های غیرمستقیم برای کسب اطلاعات درباره این سیستم‌ها از طریق عامل باشد.

**کاهش:** عامل‌های هوش مصنوعی باید فقط در صورت نیاز به سیستم‌ها دسترسی داشته باشند تا از این نوع حملات جلوگیری شود. همچنین ارتباط بین عامل و سیستم باید امن باشد. پیاده‌سازی تأیید هویت و کنترل دسترسی نیز راهی برای حفاظت از این اطلاعات است.

### بارگذاری بیش از حد منابع و خدمات

**توضیح:** عامل‌های هوش مصنوعی می‌توانند از ابزارها و خدمات مختلف برای انجام کارها استفاده کنند. مهاجمان می‌توانند از این توانایی برای حمله به این خدمات با ارسال حجم بالایی از درخواست‌ها از طریق عامل استفاده کنند که ممکن است منجر به خرابی سیستم یا هزینه‌های بالا شود.

**کاهش:** سیاست‌هایی برای محدود کردن تعداد درخواست‌هایی که یک عامل هوش مصنوعی می‌تواند به یک سرویس ارسال کند پیاده کنید. محدود کردن تعداد نوبت‌های مکالمه و درخواست‌ها به عامل نیز راهی دیگر برای جلوگیری از این حملات است.

### مسموم‌سازی پایگاه دانش

**توضیح:** این نوع حمله به طور مستقیم عامل را هدف نمی‌گیرد بلکه پایگاه دانش و سایر خدماتی که عامل استفاده می‌کند را هدف قرار می‌دهد. این می‌تواند شامل خراب کردن داده‌ها یا اطلاعاتی باشد که عامل برای انجام کار از آن‌ها استفاده می‌کند، که منجر به پاسخ‌های متعصبانه یا ناخواسته به کاربر خواهد شد.

**کاهش:** از صحت داده‌هایی که عامل در جریان کار خود استفاده می‌کند به طور منظم اطمینان حاصل کنید. مطمئن شوید دسترسی به این داده‌ها امن است و تنها افراد مورد اعتماد آن‌ها را تغییر می‌دهند تا از این نوع حمله جلوگیری شود.

### خطاهای زنجیره‌ای

**توضیح:** عامل‌های هوش مصنوعی به ابزارها و خدمات مختلف برای انجام وظایف دسترسی دارند. خطاهایی که توسط مهاجمان ایجاد می‌شود می‌تواند باعث ناکارآمدی سایر سیستم‌هایی شود که عامل به آن‌ها متصل است و این حمله را گسترده‌تر و مشکل‌تر برای عیب‌یابی می‌کند.

**کاهش:** یک روش برای جلوگیری از این مسئله این است که عامل در یک محیط محدود فعالیت کند، مانند اجرای کارها در یک کانتینر داکر، تا از حمله مستقیم به سیستم جلوگیری شود. ایجاد مکانیزم‌های جایگزین و منطق تکرار هنگامی که برخی سیستم‌ها با خطا پاسخ می‌دهند نیز راهی برای جلوگیری از خرابی‌های بزرگ‌تر سیستم است.

## انسان در حلقه

روش مؤثر دیگری برای ساخت سیستم‌های عامل هوش مصنوعی قابل اعتماد استفاده از انسان در حلقه است. این یک روند ایجاد می‌کند که در آن کاربران قادر به ارائه بازخورد به عامل‌ها در حین اجرا هستند. کاربران در واقع به عنوان عامل‌هایی در یک سیستم چندعامله عمل می‌کنند و با ارائه تایید یا پایان دادن به فرآیند در حال اجرا.

![انسان در حلقه](../../../translated_images/fa/human-in-the-loop.5f0068a678f62f4f.webp)

این قطعه کد با استفاده از Microsoft Agent Framework نشان می‌دهد که این مفهوم چگونه پیاده‌سازی شده است:

```python
import os
from agent_framework.azure import AzureAIProjectAgentProvider
from azure.identity import AzureCliCredential

# ارائه‌دهنده را با تأیید انسان در حلقه ایجاد کنید
provider = AzureAIProjectAgentProvider(
    credential=AzureCliCredential(),
)

# عامل را با یک مرحله تأیید انسانی ایجاد کنید
response = provider.create_response(
    input="Write a 4-line poem about the ocean.",
    instructions="You are a helpful assistant. Ask for user approval before finalizing.",
)

# کاربر می‌تواند پاسخ را مرور و تأیید کند
print(response.output_text)
user_input = input("Do you approve? (APPROVE/REJECT): ")
if user_input == "APPROVE":
    print("Response approved.")
else:
    print("Response rejected. Revising...")
```

## نتیجه‌گیری

ساخت عامل‌های هوش مصنوعی قابل اعتماد نیازمند طراحی دقیق، اقدامات امنیتی قوی و تکرار مستمر است. با پیاده‌سازی سیستم‌های ساختارمند متا پرامپت، درک تهدیدهای احتمالی و به‌کارگیری استراتژی‌های کاهش ریسک، توسعه‌دهندگان می‌توانند عامل‌هایی بسازند که هم ایمن و هم مؤثر باشند. علاوه بر این، در نظر گرفتن رویکرد انسان در حلقه تضمین می‌کند که عامل‌های هوش مصنوعی با نیازهای کاربر هماهنگ باقی بمانند و در عین حال خطرات را به حداقل برسانند. با ادامه تکامل هوش مصنوعی، حفظ رویکردی پیشگیرانه در موضوعات امنیتی، حریم خصوصی و ملاحظات اخلاقی کلید ایجاد اعتماد و قابلیت اطمینان در سیستم‌های مبتنی بر هوش مصنوعی خواهد بود.

## نمونه‌های کد

- [`code_samples/06-system-message-framework.ipynb`](code_samples/06-system-message-framework.ipynb): نمایش گام به گام چارچوب پیام سیستم متا پرامپت.
- [`code_samples/06-human-in-the-loop.ipynb`](code_samples/06-human-in-the-loop.ipynb): دروازه‌های تأیید پیش‌اقدام، دسته‌بندی ریسک و ثبت ممیزی برای عامل‌های قابل اعتماد.

### سوال بیشتری درباره ساخت عامل‌های هوش مصنوعی قابل اعتماد دارید؟

به [Microsoft Foundry Discord](https://aka.ms/ai-agents/discord) بپیوندید تا با دیگر یادگیرندگان ملاقات کنید، در ساعت‌های اداری شرکت کنید و سوالات خود درباره عامل‌های هوش مصنوعی را پاسخ بگیرید.

## منابع بیشتر

- <a href="https://learn.microsoft.com/azure/ai-studio/responsible-use-of-ai-overview" target="_blank">مرور کلی هوش مصنوعی مسئولانه</a>
- <a href="https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai" target="_blank">ارزیابی مدل‌های تولیدی هوش مصنوعی و برنامه‌های هوش مصنوعی</a>
- <a href="https://learn.microsoft.com/azure/ai-services/openai/concepts/system-message?context=%2Fazure%2Fai-studio%2Fcontext%2Fcontext&tabs=top-techniques" target="_blank">پیام‌های سیستم ایمنی</a>
- <a href="https://blogs.microsoft.com/wp-content/uploads/prod/sites/5/2022/06/Microsoft-RAI-Impact-Assessment-Template.pdf?culture=en-us&country=us" target="_blank">قالب ارزیابی ریسک</a>

## درس قبلی

[Agentic RAG](../05-agentic-rag/README.md)

## درس بعدی

[الگوی طراحی برنامه‌ریزی](../07-planning-design/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**سلب مسئولیت**:
این سند با استفاده از سرویس ترجمه هوش مصنوعی [Co-op Translator](https://github.com/Azure/co-op-translator) ترجمه شده است. در حالی که ما در تلاش برای دقت هستیم، لطفاً توجه داشته باشید که ترجمه‌های خودکار ممکن است شامل خطاها یا نادرستی‌هایی باشند. سند اصلی به زبان مادری خود باید به عنوان منبع معتبر در نظر گرفته شود. برای اطلاعات حیاتی، ترجمه حرفه‌ای انسانی توصیه می‌شود. ما در قبال هرگونه سوء تفاهم یا برداشت نادرست ناشی از استفاده از این ترجمه مسئولیتی نداریم.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->