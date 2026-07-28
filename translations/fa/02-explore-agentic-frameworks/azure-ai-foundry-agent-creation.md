# توسعه سرویس Microsoft Foundry Agent

در این تمرین، از ابزارهای سرویس Microsoft Foundry Agent در [پرتال Microsoft Foundry](https://ai.azure.com/?WT.mc_id=academic-105485-koreyst) برای ایجاد یک عامل برای رزرو پرواز استفاده می‌کنید. این عامل قادر خواهد بود با کاربران تعامل کند و اطلاعاتی درباره پروازها ارائه دهد.

## پیش‌نیازها

برای تکمیل این تمرین به موارد زیر نیاز دارید:
1. یک حساب Azure با اشتراک فعال. [ایجاد حساب رایگان](https://azure.microsoft.com/free/?WT.mc_id=academic-105485-koreyst).
2. شما باید مجوز ایجاد یک هاب Microsoft Foundry را داشته باشید یا یکی برای شما ایجاد شده باشد.
    - اگر نقش شما Contributor یا Owner است، می‌توانید مراحل این آموزش را دنبال کنید.

## ایجاد یک هاب Microsoft Foundry

> **توجه:** Microsoft Foundry قبلاً با نام Azure AI Studio شناخته می‌شد.

1. این دستورالعمل‌ها را از پست وبلاگ [Microsoft Foundry](https://learn.microsoft.com/en-us/azure/ai-studio/?WT.mc_id=academic-105485-koreyst) برای ایجاد یک هاب Microsoft Foundry دنبال کنید.
2. پس از ایجاد پروژه خود، هر نکته‌ای که نمایش داده می‌شود را ببندید و صفحه پروژه را در پرتال Microsoft Foundry بررسی کنید که باید شبیه تصویر زیر باشد:

    ![Microsoft Foundry Project](../../../translated_images/fa/azure-ai-foundry.88d0c35298348c2f.webp)

## استقرار یک مدل

1. در پنل سمت چپ پروژه خود، در بخش **My assets** صفحه **Models + endpoints** را انتخاب کنید.
2. در صفحه **Models + endpoints**، در تب **Model deployments**، در منوی **+ Deploy model**، گزینه **Deploy base model** را انتخاب کنید.
3. مدل `gpt-5-mini` را در فهرست جستجو کنید، سپس آن را انتخاب و تأیید کنید.

    > **توجه**: کاهش TPM به جلوگیری از استفاده بیش از حد از سهمیه اشتراک استفاده‌شده کمک می‌کند.

    ![Model Deployed](../../../translated_images/fa/model-deployment.3749c53fb81e18fd.webp)

## ایجاد یک عامل

اکنون که مدل را مستقر کرده‌اید، می‌توانید یک عامل ایجاد کنید. عامل یک مدل هوش مصنوعی مکالمه‌ای است که می‌تواند برای تعامل با کاربران استفاده شود.

1. در پنل سمت چپ پروژه خود، در بخش **Build & Customize** صفحه **Agents** را انتخاب کنید.
2. برای ایجاد یک عامل جدید، روی **+ Create agent** کلیک کنید. در کادر گفتگوی **Agent Setup**:
    - نامی برای عامل وارد کنید، مانند `FlightAgent`.
    - اطمینان حاصل کنید که استقرار مدل `gpt-5-mini` که قبلاً ایجاد کردید انتخاب شده باشد.
    - دستورالعمل‌ها را مطابق با درخواست مورد نظر برای عامل تنظیم کنید. در اینجا یک نمونه آمده است:
    ```
    You are FlightAgent, a virtual assistant specialized in handling flight-related queries. Your role includes assisting users with searching for flights, retrieving flight details, checking seat availability, and providing real-time flight status. Follow the instructions below to ensure clarity and effectiveness in your responses:

    ### Task Instructions:
    1. **Recognizing Intent**:
       - Identify the user's intent based on their request, focusing on one of the following categories:
         - Searching for flights
         - Retrieving flight details using a flight ID
         - Checking seat availability for a specified flight
         - Providing real-time flight status using a flight number
       - If the intent is unclear, politely ask users to clarify or provide more details.
        
    2. **Processing Requests**:
        - Depending on the identified intent, perform the required task:
        - For flight searches: Request details such as origin, destination, departure date, and optionally return date.
        - For flight details: Request a valid flight ID.
        - For seat availability: Request the flight ID and date and validate inputs.
        - For flight status: Request a valid flight number.
        - Perform validations on provided data (e.g., formats of dates, flight numbers, or IDs). If the information is incomplete or invalid, return a friendly request for clarification.

    3. **Generating Responses**:
    - Use a tone that is friendly, concise, and supportive.
    - Provide clear and actionable suggestions based on the output of each task.
    - If no data is found or an error occurs, explain it to the user gently and offer alternative actions (e.g., refine search, try another query).
    
    ```
> [!NOTE]
> برای دریافت جزئیات بیشتر در مورد درخواست، می‌توانید به [این مخزن](https://github.com/ShivamGoyal03/RoamMind) مراجعه کنید.
    
> همچنین می‌توانید **پایگاه دانش** و **اقدامات** را برای افزایش قابلیت‌های عامل به منظور ارائه اطلاعات بیشتر و انجام وظایف خودکار مبتنی بر درخواست‌های کاربر اضافه کنید. برای این تمرین می‌توانید این مراحل را رد کنید.
    
![Agent Setup](../../../translated_images/fa/agent-setup.9bbb8755bf5df672.webp)

3. برای ایجاد یک عامل چندهوش مصنوعی جدید، کافیست روی **New Agent** کلیک کنید. عامل تازه ایجاد شده سپس در صفحه Agents نمایش داده می‌شود.


## آزمایش عامل

پس از ایجاد عامل، می‌توانید آن را آزمایش کنید تا ببینید چگونه به پرسش‌های کاربران در محیط پرتال Microsoft Foundry پاسخ می‌دهد.

1. در بالای پنل **Setup** عامل خود، گزینه **Try in playground** را انتخاب کنید.
2. در پنل **Playground**، می‌توانید با تایپ پرس و جو در پنجره چت با عامل تعامل کنید. به عنوان مثال، می‌توانید از عامل بخواهید برای پروازها از سیاتل به نیویورک در ۲۸ام جستجو کند.

    > **توجه**: عامل ممکن است پاسخ‌های دقیقی ارائه ندهد چون در این تمرین از داده‌های زمان واقعی استفاده نمی‌شود. هدف، آزمایش توانایی عامل در درک و پاسخ به پرسش‌های کاربر بر اساس دستورالعمل‌های داده شده است.

    ![Agent Playground](../../../translated_images/fa/agent-playground.dc146586de715010.webp)

3. پس از آزمایش عامل، می‌توانید با افزودن نمایش نیت بیشتر، داده‌های آموزشی و اقدامات، آن را بیشتر سفارشی کنید تا قابلیت‌هایش بهتر شود.

## پاک‌سازی منابع

پس از پایان آزمایش عامل، می‌توانید آن را حذف کنید تا از بروز هزینه‌های اضافی جلوگیری شود.
1. وارد [پرتال Azure](https://portal.azure.com) شوید و محتوای گروه منابعی که در آن هاب را مستقر کرده‌اید که منابع استفاده شده در این تمرین است را مشاهده کنید.
2. در نوار ابزار، گزینه **Delete resource group** را انتخاب کنید.
3. نام گروه منابع را وارد کنید و تأیید کنید که می‌خواهید آن را حذف کنید.

## منابع

- [مستندات Microsoft Foundry](https://learn.microsoft.com/en-us/azure/ai-studio/?WT.mc_id=academic-105485-koreyst)
- [پرتال Microsoft Foundry](https://ai.azure.com/?WT.mc_id=academic-105485-koreyst)
- [شروع کار با Microsoft Foundry](https://techcommunity.microsoft.com/blog/educatordeveloperblog/getting-started-with-azure-ai-studio/4095602?WT.mc_id=academic-105485-koreyst)
- [مبانی عوامل هوش مصنوعی در Azure](https://learn.microsoft.com/en-us/training/modules/ai-agent-fundamentals/?WT.mc_id=academic-105485-koreyst)
- [Azure AI Discord](https://aka.ms/AzureAI/Discord)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**سلب مسئولیت**:
این سند با استفاده از سرویس ترجمه هوش مصنوعی [Co-op Translator](https://github.com/Azure/co-op-translator) ترجمه شده است. در حالی که ما در تلاش برای دقت هستیم، لطفاً توجه داشته باشید که ترجمه‌های خودکار ممکن است شامل خطاها یا نادرستی‌هایی باشند. سند اصلی به زبان مادری خود باید به عنوان منبع معتبر در نظر گرفته شود. برای اطلاعات حیاتی، ترجمه حرفه‌ای انسانی توصیه می‌شود. ما در قبال هرگونه سوء تفاهم یا برداشت نادرست ناشی از استفاده از این ترجمه مسئولیتی نداریم.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->