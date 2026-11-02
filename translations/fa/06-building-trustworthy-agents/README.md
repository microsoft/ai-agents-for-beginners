[![عامل‌های هوش مصنوعی قابل اعتماد](../../../translated_images/fa/lesson-6-thumbnail.a58ab36c099038d4.webp)](https://youtu.be/iZKkMEGBCUQ?si=Q-kEbcyHUMPoHp8L)

> _(برای مشاهده ویدئوی این درس روی تصویر بالا کلیک کنید)_

# ساخت عامل‌های هوش مصنوعی قابل اعتماد

## مقدمه

این درس شامل موارد زیر است:

- چگونه عامل‌های هوش مصنوعی ایمن و مؤثر بسازیم و پیاده‌سازی کنیم
- ملاحظات مهم امنیتی هنگام توسعه عامل‌های هوش مصنوعی
- چگونه حفظ حریم خصوصی داده‌ها و کاربران را هنگام توسعه عامل‌های هوش مصنوعی حفظ کنیم

## اهداف یادگیری

پس از اتمام این درس، شما خواهید دانست چگونه:

- ریسک‌ها را هنگام ایجاد عامل‌های هوش مصنوعی شناسایی و کاهش دهید.
- روش‌های امنیتی را برای اطمینان از مدیریت صحیح داده‌ها و دسترسی‌ها اجرا کنید.
- عامل‌های هوش مصنوعی خلق کنید که حریم خصوصی داده‌ها را حفظ کنند و تجربه کاربری با کیفیت ارائه دهند.

## ایمنی

بیایید ابتدا به ساخت برنامه‌های عاملی ایمن نگاه کنیم. ایمنی به معنای عملکرد عامل هوش مصنوعی طبق طراحی است. به عنوان سازندگان برنامه‌های عاملی، روش‌ها و ابزارهایی برای بیشینه‌کردن ایمنی داریم:

### ساختار پیام سیستم

اگر تا به حال برنامه‌ای با مدل‌های زبان بزرگ (LLMها) ساخته‌اید، اهمیت طراحی یک پیام یا پرامپت سیستم قوی را می‌دانید. این پرامپت‌ها قوانین، دستورالعمل‌ها و راهنمایی‌های متا برای نحوه تعامل LLM با کاربر و داده‌ها را تعیین می‌کنند.

برای عامل‌های هوش مصنوعی، پرامپت سیستم حتی مهم‌تر است چرا که عامل‌ها نیاز به دستورالعمل‌های بسیار خاصی برای انجام وظایف طراحی شده دارند.

برای ساخت پرامپت‌های سیستم توسعه‌پذیر، می‌توانیم از چارچوب پیام سیستم برای ساخت یک یا چند عامل در برنامه خود استفاده کنیم:

![ساختار پیام سیستم](../../../translated_images/fa/system-message-framework.3a97368c92d11d68.webp)

#### مرحله ۱: ایجاد پیام متا سیستم

پیام متا توسط یک LLM برای تولید پرامپت‌های سیستم برای عامل‌هایی که می‌سازیم استفاده می‌شود. آن را به صورت یک قالب طراحی می‌کنیم تا بتوانیم در صورت نیاز چندین عامل را به‌صورت مؤثر ایجاد کنیم.

در اینجا یک نمونه پیام متا سیستم که به LLM می‌دهیم:

```plaintext
You are an expert at creating AI agent assistants. 
You will be provided a company name, role, responsibilities and other
information that you will use to provide a system prompt for.
To create the system prompt, be descriptive as possible and provide a structure that a system using an LLM can better understand the role and responsibilities of the AI assistant. 
```

#### مرحله ۲: ایجاد پرامپت پایه

گام بعدی ایجاد یک پرامپت پایه برای توصیف عامل هوش مصنوعی است. باید نقش عامل، وظایفی که عامل انجام می‌دهد و هر مسئولیت دیگر عامل را شامل شود.

نمونه‌ای در اینجا است:

```plaintext
You are a travel agent for Contoso Travel that is great at booking flights for customers. To help customers you can perform the following tasks: lookup available flights, book flights, ask for preferences in seating and times for flights, cancel any previously booked flights and alert customers on any delays or cancellations of flights.  
```

#### مرحله ۳: ارائه پیام پایه سیستم به LLM

اکنون می‌توانیم این پیام سیستم را با دادن پیام متا به‌عنوان پیام سیستم و پیام پایه بهینه کنیم.

این منجر به تولید پیامی می‌شود که بهتر طراحی شده است تا عامل‌های هوش مصنوعی ما را هدایت کند:

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

#### مرحله ۴: تکرار و بهبود

ارزش چارچوب پیام سیستم این است که بتوان پیام‌های سیستم را برای چند عامل راحت‌تر ساخت و همچنین پیام‌های سیستم را در طول زمان بهبود بخشید. به ندرت پیش می‌آید که پیام سیستم از اولین بار برای کل مورد کاربرد شما کار کند. توانایی اعمال تغییرات کوچک و بهبودها با تغییر پیام پایه و اجرای آن در سیستم به شما امکان مقایسه و ارزیابی نتایج را می‌دهد.

## فهم تهدیدها

برای ساخت عامل‌های هوش مصنوعی قابل اعتماد، اهمیت دارد که ریسک‌ها و تهدیدها را به خوبی بفهمیم و کاهش دهیم. بیایید فقط به برخی تهدیدهای مختلف عامل‌های هوش مصنوعی نگاه کنیم و چگونه می‌توانید بهتر برنامه‌ریزی و آماده شوید.

![فهم تهدیدها](../../../translated_images/fa/understanding-threats.89edeada8a97fc0f.webp)

### وظیفه و دستورالعمل

**توضیح:** مهاجمان تلاش می‌کنند با پرامپت‌دهی یا دستکاری ورودی‌ها دستورالعمل‌ها یا اهداف عامل هوش مصنوعی را تغییر دهند.

**کاهش خطر**: بررسی اعتبار و فیلترهای ورودی را اجرا کنید تا پرامپت‌های بالقوه خطرناک قبل از پردازش توسط عامل هوش مصنوعی شناسایی شوند. از آنجا که این حملات معمولاً به تعامل مکرر با عامل نیاز دارند، محدود کردن تعداد نوبت‌های مکالمه راه دیگری برای جلوگیری از این نوع حملات است.

### دسترسی به سیستم‌های حیاتی

**توضیح**: اگر عامل هوش مصنوعی به سیستم‌ها و خدماتی که داده‌های حساس ذخیره می‌کنند دسترسی داشته باشد، مهاجمان می‌توانند ارتباط بین عامل و این خدمات را به خطر بیندازند. این می‌تواند حملات مستقیم یا تلاش‌های غیرمستقیم برای به دست آوردن اطلاعات درباره این سیستم‌ها از طریق عامل باشد.

**کاهش خطر**: عامل‌های هوش مصنوعی باید فقط در صورت نیاز به سیستم‌ها دسترسی داشته باشند تا از این حملات جلوگیری شود. همچنین ارتباط بین عامل و سیستم باید امن باشد. پیاده‌سازی احراز هویت و کنترل دسترسی راه دیگری برای حفاظت از این اطلاعات است.

### بارگذاری زیاد منابع و خدمات

**توضیح:** عامل‌های هوش مصنوعی می‌توانند به ابزارها و خدمات مختلف برای انجام وظایف دسترسی داشته باشند. مهاجمان می‌توانند از این توانایی استفاده کنند تا با ارسال تعداد زیادی درخواست از طریق عامل، به این خدمات حمله کنند که ممکن است منجر به خرابی سیستم یا هزینه‌های بالا شود.

**کاهش خطر:** سیاست‌هایی برای محدود کردن تعداد درخواست‌هایی که یک عامل هوش مصنوعی می‌تواند به یک سرویس بفرستد اجرا کنید. محدود کردن تعداد نوبت‌های مکالمه و درخواست‌ها به عامل راه دیگری برای جلوگیری از این حملات است.

### مسمومیت پایگاه دانش

**توضیح:** این نوع حمله مستقیماً هدف عامل هوش مصنوعی نیست، بلکه پایگاه دانش و دیگر خدماتی که عامل استفاده می‌کند را هدف قرار می‌دهد. این می‌تواند شامل خراب کردن داده‌ها یا اطلاعاتی باشد که عامل برای انجام وظیفه استفاده می‌کند و منجر به پاسخ‌های جانبدارانه یا ناخواسته به کاربر شود.

**کاهش خطر:** بررسی‌های منظم از داده‌هایی که عامل هوش مصنوعی برای گردش کارش استفاده می‌کند را انجام دهید. اطمینان حاصل کنید دسترسی به این داده‌ها امن باشد و فقط توسط افراد مورد اعتماد تغییر کند تا از این نوع حمله جلوگیری شود.

### اشکالات پی‌درپی

**توضیح:** عامل‌های هوش مصنوعی به ابزارها و خدمات مختلف دسترسی دارند تا وظایف را انجام دهند. خطاهای ایجاد شده توسط مهاجمان می‌تواند به خرابی‌های سایر سیستم‌های متصل منجر شود و باعث شود حمله گسترده‌تر و سخت‌تر برای رفع شود.

**کاهش خطر**: یکی از روش‌ها این است که عامل را در محیط محدود شده‌ای مانند اجرای وظایف در یک کانتینر داکر قرار دهید تا حملات مستقیم به سیستم جلوگیری شود. ایجاد مکانیزم‌های پشتیبان و منطق تکرار زمانی که سیستم‌های خاص با خطا پاسخ می‌دهند راه دیگری برای جلوگیری از خرابی‌های بزرگ‌تر است.

## انسان در حلقه

یکی از روش‌های مؤثر دیگر برای ساخت سیستم‌های عامل هوش مصنوعی قابل اعتماد استفاده از روش انسان در حلقه است. این یک جریان ایجاد می‌کند که کاربران توانایی ارائه بازخورد به عامل‌ها در حین اجرا را دارند. کاربران اساساً در یک سیستم چندعامله به عنوان عامل عمل می‌کنند و با ارائه تأیید یا خاتمه فرآیند در حال اجرا کنترل دارند.

![انسان در حلقه](../../../translated_images/fa/human-in-the-loop.5f0068a678f62f4f.webp)

در اینجا قطعه کدی است که با استفاده از چارچوب Microsoft Agent نشان می‌دهد چگونه این مفهوم پیاده‌سازی می‌شود:

```python
import os
from agent_framework.foundry import FoundryChatClient
from azure.identity import AzureCliCredential

# ارائه‌دهنده را با تأیید انسان در حلقه ایجاد کنید
provider = FoundryChatClient(
    project_endpoint=os.environ["AZURE_AI_PROJECT_ENDPOINT"],
    model=os.environ["AZURE_AI_MODEL_DEPLOYMENT_NAME"],
    credential=AzureCliCredential(),
)

# عامل را با یک مرحله تأیید انسانی ایجاد کنید
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

ساخت عامل‌های هوش مصنوعی قابل اعتماد نیازمند طراحی دقیق، اقدامات امنیتی مستحکم و تکرار مداوم است. با پیاده‌سازی سیستم‌های ساختارمند پرامپت متا، درک تهدیدهای احتمالی و اجرای راهبردهای کاهش، توسعه‌دهندگان می‌توانند عامل‌های هوش مصنوعی ایمن و مؤثری ایجاد کنند. علاوه بر این، استفاده از رویکرد انسان در حلقه تضمین می‌کند که عامل‌ها با نیازهای کاربر هماهنگ ماندگار باشند و ریسک‌ها کاهش یابند. با پیشرفت هوش مصنوعی، حفظ نگرش پیشگیرانه در زمینه امنیت، حریم خصوصی و ملاحظات اخلاقی کلید ایجاد اعتماد و اطمینان در سیستم‌های هوش مصنوعی خواهد بود.

## نمونه کدها

- [`code_samples/06-system-message-framework.ipynb`](code_samples/06-system-message-framework.ipynb): نمایش گام به گام چارچوب سیستم پیام متا پرامپت.
- [`code_samples/06-human-in-the-loop.ipynb`](code_samples/06-human-in-the-loop.ipynb): دروازه‌های تأیید پیش از عمل، رتبه‌بندی ریسک و گزارش‌های حسابرسی برای عامل‌های قابل اعتماد.

### سوالات بیشتری درباره ساخت عامل‌های هوش مصنوعی قابل اعتماد دارید؟

به [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D) بپیوندید تا با یادگیرندگان دیگر ملاقات کنید، در ساعت‌های مشاوره شرکت کنید و سوالات مربوط به عامل‌های هوش مصنوعی خود را پاسخ بگیرید.

## منابع اضافی

- <a href="https://learn.microsoft.com/azure/ai-studio/responsible-use-of-ai-overview" target="_blank">بررسی کلی هوش مصنوعی مسئولانه</a>
- <a href="https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai" target="_blank">ارزیابی مدل‌ها و برنامه‌های هوش مصنوعی مولد</a>
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