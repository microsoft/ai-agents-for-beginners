<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "498802b4c3c3cc486b86f27a12cebb34",
  "translation_date": "2025-08-30T13:35:52+00:00",
  "source_file": "06-building-trustworthy-agents/README.md",
  "language_code": "fa"
}
-->
[![Trustworthy AI Agents](../../../translated_images/lesson-6-thumbnail.a58ab36c099038d4f786c2b0d5d6e89f41f4c2ecc05ab10b67bced2695eeb218.fa.png)](https://youtu.be/iZKkMEGBCUQ?si=Q-kEbcyHUMPoHp8L)

> _(برای مشاهده ویدئوی این درس، روی تصویر بالا کلیک کنید)_

# ساخت عوامل هوش مصنوعی قابل اعتماد

## مقدمه

این درس شامل موارد زیر است:

- نحوه ساخت و استقرار عوامل هوش مصنوعی ایمن و مؤثر  
- ملاحظات امنیتی مهم در توسعه عوامل هوش مصنوعی  
- نحوه حفظ حریم خصوصی داده‌ها و کاربران در توسعه عوامل هوش مصنوعی  

## اهداف یادگیری

پس از اتمام این درس، شما خواهید دانست که چگونه:

- خطرات را هنگام ایجاد عوامل هوش مصنوعی شناسایی و کاهش دهید.  
- اقدامات امنیتی را برای مدیریت صحیح داده‌ها و دسترسی‌ها پیاده‌سازی کنید.  
- عوامل هوش مصنوعی ایجاد کنید که حریم خصوصی داده‌ها را حفظ کرده و تجربه کاربری باکیفیتی ارائه دهند.  

## ایمنی

ابتدا به ساخت برنامه‌های عامل‌محور ایمن می‌پردازیم. ایمنی به این معناست که عامل هوش مصنوعی همان‌طور که طراحی شده عمل کند. به‌عنوان سازندگان برنامه‌های عامل‌محور، ما روش‌ها و ابزارهایی برای به حداکثر رساندن ایمنی داریم:

### ایجاد چارچوب پیام سیستمی

اگر تاکنون برنامه‌ای با استفاده از مدل‌های زبانی بزرگ (LLM) ساخته‌اید، اهمیت طراحی یک پیام سیستمی قوی را می‌دانید. این پیام‌ها قوانین، دستورالعمل‌ها و راهنمایی‌های کلی را برای نحوه تعامل مدل با کاربر و داده‌ها تعیین می‌کنند.

برای عوامل هوش مصنوعی، پیام سیستمی حتی اهمیت بیشتری دارد، زیرا این عوامل به دستورالعمل‌های بسیار خاصی برای انجام وظایف طراحی‌شده نیاز دارند.

برای ایجاد پیام‌های سیستمی مقیاس‌پذیر، می‌توانیم از یک چارچوب پیام سیستمی برای ساخت یک یا چند عامل در برنامه خود استفاده کنیم:

![Building a System Message Framework](../../../translated_images/system-message-framework.3a97368c92d11d6814577b03cd128ec8c71a5fd1e26f341835cfa5df59ae87ae.fa.png)

#### مرحله ۱: ایجاد یک پیام سیستمی متا

پیام متا توسط یک LLM برای تولید پیام‌های سیستمی برای عواملی که ایجاد می‌کنیم استفاده می‌شود. ما آن را به‌صورت یک قالب طراحی می‌کنیم تا بتوانیم در صورت نیاز به‌طور کارآمد عوامل متعددی ایجاد کنیم.

در اینجا یک نمونه از پیام سیستمی متا آورده شده است که به LLM ارائه می‌دهیم:

```plaintext
You are an expert at creating AI agent assistants. 
You will be provided a company name, role, responsibilities and other
information that you will use to provide a system prompt for.
To create the system prompt, be descriptive as possible and provide a structure that a system using an LLM can better understand the role and responsibilities of the AI assistant. 
```

#### مرحله ۲: ایجاد یک پیام پایه

مرحله بعدی ایجاد یک پیام پایه برای توصیف عامل هوش مصنوعی است. شما باید نقش عامل، وظایفی که عامل انجام خواهد داد و هر مسئولیت دیگری را که بر عهده دارد، مشخص کنید.

در اینجا یک نمونه آورده شده است:

```plaintext
You are a travel agent for Contoso Travel that is great at booking flights for customers. To help customers you can perform the following tasks: lookup available flights, book flights, ask for preferences in seating and times for flights, cancel any previously booked flights and alert customers on any delays or cancellations of flights.  
```

#### مرحله ۳: ارائه پیام سیستمی پایه به LLM

اکنون می‌توانیم این پیام سیستمی را با ارائه پیام سیستمی متا به‌عنوان پیام سیستمی و پیام سیستمی پایه خود بهینه کنیم.

این کار یک پیام سیستمی تولید می‌کند که برای هدایت عوامل هوش مصنوعی ما بهتر طراحی شده است:

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

ارزش این چارچوب پیام سیستمی در این است که ایجاد پیام‌های سیستمی برای عوامل متعدد را آسان‌تر کرده و همچنین امکان بهبود پیام‌های سیستمی را در طول زمان فراهم می‌کند. به‌ندرت پیش می‌آید که پیام سیستمی شما از همان ابتدا برای تمام موارد استفاده شما مناسب باشد. با ایجاد تغییرات کوچک و بهبود پیام سیستمی پایه و اجرای آن در سیستم، می‌توانید نتایج را مقایسه و ارزیابی کنید.

## درک تهدیدات

برای ساخت عوامل هوش مصنوعی قابل اعتماد، درک و کاهش خطرات و تهدیدات مربوط به عامل هوش مصنوعی بسیار مهم است. بیایید به برخی از تهدیدات مختلفی که ممکن است عوامل هوش مصنوعی با آن‌ها مواجه شوند و نحوه برنامه‌ریزی و آماده‌سازی بهتر برای آن‌ها نگاهی بیندازیم.

![Understanding Threats](../../../translated_images/understanding-threats.89edeada8a97fc0f7053558567d5dd27c0c333b74e47fffdde490fa6777a4c17.fa.png)

### وظایف و دستورالعمل‌ها

**توضیح:** مهاجمان تلاش می‌کنند دستورالعمل‌ها یا اهداف عامل هوش مصنوعی را از طریق ورودی‌ها یا دستکاری تغییر دهند.

**کاهش خطر:** بررسی‌های اعتبارسنجی و فیلترهای ورودی را برای شناسایی ورودی‌های خطرناک قبل از پردازش توسط عامل هوش مصنوعی اجرا کنید. از آنجا که این حملات معمولاً به تعامل مکرر با عامل نیاز دارند، محدود کردن تعداد دفعات مکالمه نیز راهی برای جلوگیری از این نوع حملات است.

### دسترسی به سیستم‌های حساس

**توضیح:** اگر یک عامل هوش مصنوعی به سیستم‌ها و خدماتی که داده‌های حساس را ذخیره می‌کنند دسترسی داشته باشد، مهاجمان می‌توانند ارتباط بین عامل و این خدمات را به خطر بیندازند. این حملات می‌توانند مستقیم یا غیرمستقیم باشند.

**کاهش خطر:** عوامل هوش مصنوعی باید فقط در صورت نیاز به سیستم‌ها دسترسی داشته باشند تا از این نوع حملات جلوگیری شود. ارتباط بین عامل و سیستم نیز باید ایمن باشد. پیاده‌سازی احراز هویت و کنترل دسترسی نیز راه دیگری برای محافظت از این اطلاعات است.

### بارگذاری بیش از حد منابع و خدمات

**توضیح:** عوامل هوش مصنوعی می‌توانند برای انجام وظایف به ابزارها و خدمات مختلف دسترسی داشته باشند. مهاجمان می‌توانند از این قابلیت برای ارسال حجم زیادی از درخواست‌ها از طریق عامل هوش مصنوعی استفاده کنند که ممکن است منجر به خرابی سیستم یا هزینه‌های بالا شود.

**کاهش خطر:** سیاست‌هایی برای محدود کردن تعداد درخواست‌هایی که یک عامل هوش مصنوعی می‌تواند به یک سرویس ارسال کند، اجرا کنید. محدود کردن تعداد دفعات مکالمه و درخواست‌ها به عامل هوش مصنوعی نیز راه دیگری برای جلوگیری از این نوع حملات است.

### مسمومیت پایگاه دانش

**توضیح:** این نوع حمله مستقیماً عامل هوش مصنوعی را هدف قرار نمی‌دهد، بلکه پایگاه دانش و سایر خدماتی که عامل هوش مصنوعی از آن‌ها استفاده می‌کند را هدف قرار می‌دهد. این می‌تواند شامل خراب کردن داده‌ها یا اطلاعاتی باشد که عامل هوش مصنوعی برای انجام وظایف خود استفاده می‌کند و منجر به پاسخ‌های مغرضانه یا ناخواسته به کاربر می‌شود.

**کاهش خطر:** تأیید منظم داده‌هایی که عامل هوش مصنوعی در جریان کار خود استفاده می‌کند را انجام دهید. اطمینان حاصل کنید که دسترسی به این داده‌ها ایمن است و فقط توسط افراد مورد اعتماد تغییر می‌کند تا از این نوع حمله جلوگیری شود.

### خطاهای زنجیره‌ای

**توضیح:** عوامل هوش مصنوعی برای انجام وظایف به ابزارها و خدمات مختلف دسترسی دارند. خطاهایی که توسط مهاجمان ایجاد می‌شوند می‌توانند منجر به خرابی سایر سیستم‌هایی شوند که عامل هوش مصنوعی به آن‌ها متصل است و باعث گسترش حمله و دشوارتر شدن عیب‌یابی می‌شوند.

**کاهش خطر:** یکی از روش‌ها برای جلوگیری از این مشکل این است که عامل هوش مصنوعی در یک محیط محدود، مانند انجام وظایف در یک کانتینر Docker، عمل کند تا از حملات مستقیم به سیستم جلوگیری شود. ایجاد مکانیزم‌های جایگزین و منطق تلاش مجدد زمانی که سیستم‌های خاصی با خطا پاسخ می‌دهند نیز راه دیگری برای جلوگیری از خرابی‌های بزرگ‌تر سیستم است.

## انسان در حلقه

یکی دیگر از روش‌های مؤثر برای ساخت سیستم‌های عامل هوش مصنوعی قابل اعتماد، استفاده از انسان در حلقه است. این روش جریانی ایجاد می‌کند که در آن کاربران می‌توانند در حین اجرای عوامل به آن‌ها بازخورد دهند. کاربران عملاً به‌عنوان عامل در یک سیستم چندعاملی عمل می‌کنند و با تأیید یا متوقف کردن فرآیند در حال اجرا، نقش ایفا می‌کنند.

![Human in The Loop](../../../translated_images/human-in-the-loop.5f0068a678f62f4fc8373d5b78c4c22f35d9e4da35c93f66c3b634c1774eff34.fa.png)

در اینجا یک قطعه کد با استفاده از AutoGen آورده شده است که نشان می‌دهد این مفهوم چگونه پیاده‌سازی می‌شود:

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

## نتیجه‌گیری

ساخت عوامل هوش مصنوعی قابل اعتماد نیازمند طراحی دقیق، اقدامات امنیتی قوی و تکرار مداوم است. با پیاده‌سازی سیستم‌های متا پرامپت ساختاریافته، درک تهدیدات احتمالی و اعمال استراتژی‌های کاهش خطر، توسعه‌دهندگان می‌توانند عوامل هوش مصنوعی ایمن و مؤثری ایجاد کنند. علاوه بر این، گنجاندن رویکرد انسان در حلقه تضمین می‌کند که عوامل هوش مصنوعی با نیازهای کاربران همسو باقی می‌مانند و در عین حال خطرات را به حداقل می‌رسانند. با ادامه تکامل هوش مصنوعی، حفظ رویکردی پیشگیرانه در زمینه امنیت، حریم خصوصی و ملاحظات اخلاقی کلید ایجاد اعتماد و قابلیت اطمینان در سیستم‌های مبتنی بر هوش مصنوعی خواهد بود.

### سوالات بیشتری درباره ساخت عوامل هوش مصنوعی قابل اعتماد دارید؟

به [Azure AI Foundry Discord](https://aka.ms/ai-agents/discord) بپیوندید تا با دیگر یادگیرندگان ملاقات کنید، در ساعات اداری شرکت کنید و سوالات خود درباره عوامل هوش مصنوعی را مطرح کنید.

## منابع اضافی

- <a href="https://learn.microsoft.com/azure/ai-studio/responsible-use-of-ai-overview" target="_blank">مروری بر هوش مصنوعی مسئولانه</a>  
- <a href="https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai" target="_blank">ارزیابی مدل‌های هوش مصنوعی مولد و برنامه‌های هوش مصنوعی</a>  
- <a href="https://learn.microsoft.com/azure/ai-services/openai/concepts/system-message?context=%2Fazure%2Fai-studio%2Fcontext%2Fcontext&tabs=top-techniques" target="_blank">پیام‌های سیستمی ایمنی</a>  
- <a href="https://blogs.microsoft.com/wp-content/uploads/prod/sites/5/2022/06/Microsoft-RAI-Impact-Assessment-Template.pdf?culture=en-us&country=us" target="_blank">الگوی ارزیابی ریسک</a>  

## درس قبلی

[Agentic RAG](../05-agentic-rag/README.md)

## درس بعدی

[Planning Design Pattern](../07-planning-design/README.md)

---

**سلب مسئولیت**:  
این سند با استفاده از سرویس ترجمه هوش مصنوعی [Co-op Translator](https://github.com/Azure/co-op-translator) ترجمه شده است. در حالی که ما برای دقت تلاش می‌کنیم، لطفاً توجه داشته باشید که ترجمه‌های خودکار ممکن است شامل خطاها یا نادقتی‌هایی باشند. سند اصلی به زبان اصلی آن باید به عنوان منبع معتبر در نظر گرفته شود. برای اطلاعات حساس، ترجمه حرفه‌ای انسانی توصیه می‌شود. ما هیچ مسئولیتی در قبال سوءتفاهم‌ها یا تفسیرهای نادرست ناشی از استفاده از این ترجمه نداریم.