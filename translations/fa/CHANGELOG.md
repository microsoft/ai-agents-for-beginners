# گزارش تغییرات

تمام تغییرات قابل توجه دوره **عامل‌های هوش مصنوعی برای مبتدیان** در این فایل مستند شده‌اند.

## [منتشر شده] — ۱۴-۰۷-۲۰۲۶

این نسخه دوره را از دو مدل جدیدا منسوخ شده جدا می‌کند، دفترچه‌های درس باقی‌مانده را به API پایدار Microsoft Agent Framework منتقل می‌کند و دفترچه‌های پایتون را در برابر پیاده‌سازی زنده Microsoft Foundry اعتبارسنجی می‌کند.

### تغییر یافته

- **انتقال از مدل‌های منسوخ شده (`gpt-4.1` / `gpt-4.1-mini` → `gpt-5-mini`).** هر دو `gpt-4.1` و `gpt-4.1-mini` اکنون منسوخ شده‌اند (تاریخ بازنشستگی اعلام شده **۱۴ اکتبر ۲۰۲۶**). تمام مراجع دوره (مستندات، `.env.example`، دفترچه‌های پایتون/.NET و نمونه‌ها) با مدل غیرمنسوخ `gpt-5-mini` جایگزین شدند. مثال مسیر‌یابی مدل درس ۱۶ یک تضاد کوچک/بزرگ را با استفاده از `gpt-5-nano` (کوچک) و `gpt-5-mini` (بزرگ) حفظ می‌کند. فایل‌های جانبی شخص ثالث ([15-browser-use/llms.txt](../../15-browser-use/llms.txt))، متن‌های تاریخی GitHub Models و یادداشت‌های قابلیت مهارت `azure-openai-to-responses` عمداً بدون تغییر باقی ماندند.
- **دفترچه واگذاری درس ۱۴ به API پایدار منتقل شد.** [14-handoff.ipynb](./14-microsoft-agent-framework/code-samples/14-handoff.ipynb) اکنون از `agent_framework.orchestrations.HandoffBuilder` با `.with_start_agent(...)`، `HandoffAgentUserRequest.create_response(...)`، پخش مبتنی بر `event.type` و `FoundryChatClient` استفاده می‌کند (جایگزین نشانگرهای حذف شده پیش‌از نسخه ۱.۰ `HandoffBuilder`/`ChatMessage`/`RequestInfoEvent`).
- **دفترچه انسانی-در-حلقه درس ۱۴ به API پایدار منتقل شد.** [14-human-loop.ipynb](./14-microsoft-agent-framework/code-samples/14-human-loop.ipynb) اکنون با `ctx.request_info(...)` + `@response_handler` متوقف می‌شود (جایگزین `RequestInfoExecutor` / `RequestInfoMessage` / `RequestResponse` حذف شده)، با `WorkflowBuilder(start_executor=..., output_executors=[...])` ساخته می‌شود، خروجی ساختاریافته را از طریق `default_options={"response_format": ...}` هدایت می‌کند و از پاسخ اسکریپت شده استفاده می‌کند تا دفترچه بدون نیاز به دخالت اجرا شود (بدون مسدود کننده `input()`).
- **پیکربندی محیط** ([.env.example](../../.env.example)): نام‌های خطر انتشار مدل به `gpt-5-mini` تغییر یافته‌اند؛ متغیرهای `AZURE_AI_SMALL_MODEL` / `AZURE_AI_LARGE_MODEL` (مسیر‌یابی درس ۱۶) و `AZURE_OPENAI_CHAT_DEPLOYMENT_NAME` که پیش‌تر نبود (درس ۱۵ استفاده مرورگر) اضافه شدند.
- **وابستگی‌ها** ([requirements.txt](../../requirements.txt)): بسته‌های `agent-framework`، `agent-framework-foundry` و `agent-framework-openai` به نسخه `~=1.10.0` ثابت شدند تا مجموعه‌ای خود‌سازگار و اعتبارسنجی شده باشند (نسخه ۱.۱۱.۰ تغییرات آزمایشی شکسته‌کننده روی سطوحی که این درس‌ها استفاده می‌کنند دارد).

### یادداشت‌ها و محدودیت‌های شناخته شده

- **اعتبارسنجی در برابر Microsoft Foundry زنده.** دفترچه‌های پایتون به‌صورت بدون‌سر با `nbconvert` روی پروژه Microsoft Foundry با `gpt-5-mini` (و `gpt-5-nano` برای مسیر‌یابی درس ۱۶) اجرا شدند. مدل‌های معادل غیرمنسوخ شده را در پروژه خود مستقر کنید؛ دفترچه‌ها نام استقرار را از `AZURE_AI_MODEL_DEPLOYMENT_NAME` / `AZURE_OPENAI_DEPLOYMENT` می‌خوانند.
- **هنوز به منابع اضافی برای برخی درس‌ها نیاز است.** درس ۰۵ به Azure AI Search نیاز دارد؛ جریان کاری مبنی بر Bing درس ۰۸ (`04.python-agent-framework-workflow-aifoundry-condition.ipynb`) به اتصال Bing و ابزارهای میزبانی شده توسط سرویس Agent Microsoft Foundry نیازمند است؛ درس ۱۳ (Cognee) و درس ۱۷ (Foundry Local) به محیط اجرای خود نیاز دارند.

## [منتشر شده] — ۱۳-۰۷-۲۰۲۶

این نسخه دو درس جدید اضافه می‌کند که قوس استقرار را کامل می‌کنند — مقیاس‌بندی عامل‌ها به Microsoft Foundry و کاهش به یک ایستگاه کاری — به علاوه یک خط لوله تست دودی، ناوبری دوره تازه‌شده، مهارت‌های یادگیری جدید و برندینگ به‌روزرسانی شده.

### اضافه شده

- **درس ۱۶ — استقرار عامل‌های مقیاس‌پذیر با Microsoft Foundry.** درس جدید [16-deploying-scalable-agents/README.md](./16-deploying-scalable-agents/README.md) و دفترچه قابل اجرا [16-python-agent-framework.ipynb](./16-deploying-scalable-agents/code_samples/16-python-agent-framework.ipynb) ساخت یک عامل پشتیبانی مشتری در محیط تولید (ابزارها، RAG، حافظه، مسیر‌یابی مدل، کش پاسخ، تأیید انسانی، دروازه ارزیابی و ردگیری OpenTelemetry)، با نمودارهای Mermaid توسعه/استقرار/اجرایی، بررسی دانش، تمرین و چالش.
- **درس ۱۷ — ساخت عامل‌های هوش مصنوعی محلی با Foundry Local و Qwen.** درس جدید [17-creating-local-ai-agents/README.md](./17-creating-local-ai-agents/README.md) و دفترچه [17-local-agent-foundry-local.ipynb](./17-creating-local-ai-agents/code_samples/17-local-agent-foundry-local.ipynb) ساخت دستیار مهندسی کاملاً روی دستگاه (فراخوانی تابع Qwen از طریق Foundry Local، ابزارهای فایل محدودشده، RAG محلی با Chroma، MCP محلی اختیاری)، با نمودارهای فقط‌محلی / محلی-RAG / فراخوانی ابزار، بررسی دانش، تمرین و چالش.
- **خط لوله تست دود.** جریان کاری جدید [AI Smoke Test](https://github.com/marketplace/actions/ai-smoke-test) [.github/workflows/smoke-test.yml](../../.github/workflows/smoke-test.yml) به همراه فهرست‌های مجزا برای هر درس تحت [tests/](./tests/README.md) برای عامل‌های قابل استقرار در دروس ۰۱، ۰۴، ۰۵ و ۱۶، با README شاخصی که هر فهرست را به درس و نام عامل میزبانی شده آن نگاشت می‌کند. درس ۱۶ بخشی به نام "اعتبارسنجی عامل مستقر شده با تست‌های دودی" اضافه کرد؛ دروس ۰۱/۰۴/۰۵ اشاره‌گر تست دود اختیاری دارند.
- **مهارت‌های یادگیرنده.** مهارت‌های عامل جدید در `.agents/skills/`: [deploying-scalable-agents](./.agents/skills/deploying-scalable-agents/SKILL.md)، [local-ai-agents](./.agents/skills/local-ai-agents/SKILL.md) (مجموعه راهنمایی‌های دروس ۱۶ و ۱۷) و [testing-course-samples](./.agents/skills/testing-course-samples/SKILL.md) (چگونگی اعتبارسنجی نمونه دفترچه‌ها در برابر Microsoft Foundry / Azure OpenAI زنده).
- **اجرای اعتبارسنجی دفترچه‌ها.** اسکریپت جدید [scripts/validate-notebooks.ps1](../../scripts/validate-notebooks.ps1) که همه دفترچه‌های پایتون را بدون سر و با `nbconvert` اجرا می‌کند و ماتریس موفق/ناموفق (به‌همراه `results.json`) چاپ می‌کند. ریشه مخزن و پایتون را خودکار شناسایی می‌کند، به‌طور پیش‌فرض دفترچه‌های خارج از دوره (`.venv`، `site-packages`، `translations`، دارایی‌های قالب مهارت) و دفترچه‌های `.NET` را مستثنی می‌کند، و از گزینه‌های `-Filter`، `-Timeout`، `-List`، `-IncludeDotnet` و `-Python` پشتیبانی می‌کند.
- **ناوبری دوره.** لینک‌های درس قبلی/بعدی به دروس ۱۱–۱۵ اضافه شده‌اند (که قبلاً مفقود بودند) تا کل دوره در هر دو جهت ۰۰ → ۱۸ پیوسته باشد.
- **تصاویر کوچک جدید.** تصاویر کوچک دروس ۱۶ و ۱۷، به همراه تصویر اجتماعی مخزن تازه‌شده [images/repo-thumbnailv3.png](./images/repo-thumbnailv3.png) (اکنون دو درس جدید و آدرس `aka.ms/ai-agents-beginners` را تبلیغ می‌کند).
- **وابستگی‌ها** ([requirements.txt](../../requirements.txt)): بسته‌های `foundry-local-sdk` و `chromadb` برای درس ۱۷ اضافه شدند.

### تغییر یافته

- **جدول درس اصلی [README.md](./README.md)**: دروس ۱۶ و ۱۷ اکنون به محتوای خود لینک دارند (که قبلاً "به‌زودی می‌آید" بودند)؛ تصویر مخزن به `repo-thumbnailv3.png` ارتقاء یافت.
- **[STUDY_GUIDE.md](./STUDY_GUIDE.md)**: دروس ۱۶ و ۱۷ به راهنمای درس به درس و مسیرهای یادگیری اضافه شدند، به‌علاوه بخش "اعتبارسنجی عامل‌های مستقر شده با تست دود".
- **[AGENTS.md](./AGENTS.md)**: تعداد/توضیحات درس‌ها (۰۰–۱۸) به‌روزرسانی شدند، بخش اعتبارسنجی تست دود اضافه شد، و مثال‌های نامگذاری نمونه‌های دروس ۱۶/۱۷ افزوده شدند.
- **[18-securing-ai-agents/README.md](./18-securing-ai-agents/README.md)**: "درس قبلی" اکنون به درس ۱۷ اشاره می‌کند (قبلاً درس ۱۵ بود)، زنجیره را می‌بندد.
- **استانداردسازی مراجع مدل روی مدل‌های غیر منسوخ.** تمام ارجاعات به `gpt-4o` / `gpt-4o-mini` در کل دوره (مستندات، `.env.example`، دفترچه‌های پایتون/.NET و نمونه‌ها) با `gpt-4.1-mini` جایگزین شدند — `gpt-4o` (همه نسخه‌ها) در سال ۲۰۲۶ بازنشسته می‌شود. مثال مسیر‌یابی مدل درس ۱۶ تضاد کوچک/بزرگ را با استفاده از `gpt-4.1-mini` (کوچک) و `gpt-4.1` (بزرگ) حفظ می‌کند. دفترچه‌های پایتون اکنون مدل را از متغیرهای محیطی (`AZURE_AI_MODEL_DEPLOYMENT_NAME` / `AZURE_OPENAI_DEPLOYMENT`) انتخاب می‌کنند به جای برنامه‌نویسی نام مدل.

### یادداشت‌ها و محدودیت‌های شناخته شده

- **در برابر Azure زنده اجرا نشده‌اند.** دفترچه‌های دروس جدید نمونه‌های آموزشی هستند؛ آنها را در برابر تنظیمات Microsoft Foundry / Foundry Local خود اجرا و اعتبارسنجی کنید. جریان کاری تست دود مستلزم این است که عامل درس را مستقر کرده و اسرار OIDC Azure (`AZURE_CLIENT_ID`، `AZURE_TENANT_ID`، `AZURE_SUBSCRIPTION_ID`) را با نقش **Azure AI User** در محدوده پروژه Foundry پیکربندی کنید.
- **درس ۱۷ فقط محلی است.** نقطه پاسخ‌دهی Foundry ندارد، بنابراین اقدامات تست دود شامل آن نمی‌شود؛ آن را با اجرای دفترچه روی ایستگاه کاری خود اعتبارسنجی کنید.

## [منتشر شده] — ۰۶-۰۷-۲۰۲۶

این نسخه دوره را به **Azure OpenAI Responses API** منتقل می‌کند، نامگذاری محصول را در **Microsoft Foundry** و **Microsoft Agent Framework (MAF)** استاندارد می‌سازد، GitHub Models را بازنشسته می‌کند، نسخه‌های SDK را به‌روزرسانی می‌کند و مطالب جدیدی در مورد مدل‌های محلی و میزبانی فریم‌ورک‌های دیگر روی Foundry اضافه می‌کند.

### اضافه شده

- **مهارت مهاجرت** — مهارت عامل [`azure-openai-to-responses`](./.agents/skills/azure-openai-to-responses/SKILL.md) از [Azure-Samples/azure-openai-to-responses](https://github.com/Azure-Samples/azure-openai-to-responses) نصب شده در `.agents/skills/`، شامل ارجاعات و اسکریپت اسکنر آن.
- **Foundry Local (اجرای مدل‌ها روی دستگاه)** — بخش جدید "ارائه دهنده جایگزین: Foundry Local" در [00-course-setup/README.md](./00-course-setup/README.md) که نصب (`winget` / `brew`)، اجرای `foundry model run`، `foundry-local-sdk` و اتصال `FoundryLocalManager` به Microsoft Agent Framework از طریق `OpenAIChatClient` را شامل می‌شود.
- **میزبانی عامل‌های LangChain / LangGraph روی Microsoft Foundry** — بخش جدید در [14-microsoft-agent-framework/README.md](./14-microsoft-agent-framework/README.md) به همراه نمونه قابل اجرا [14-langchain-hosted-agent.py](../../14-microsoft-agent-framework/code-samples/14-langchain-hosted-agent.py) که از `langchain-azure-ai[hosting]` و `ResponsesHostServer` (پروتکل `/responses`) استفاده می‌کند، براساس [Microsoft Learn](https://learn.microsoft.com/azure/foundry/how-to/develop/langchain-hosted-agents).
- **Microsoft Project Opal** — بخش جدید "مثال دنیای واقعی: Microsoft Project Opal" در [15-browser-use/README.md](./15-browser-use/README.md) که Opal را به عنوان یک عامل کاربرد کامپیوتر سازمانی چارچوب‌بندی می‌کند و آن را به مفاهیم دوره (انسان در حلقه، اعتماد/امنیت، برنامه‌ریزی، مهارت‌ها) نگاشت می‌کند.
- **نمونه دوم پایتون درس ۰۲** — افزودن [02-python-agent-framework-azure-openai.ipynb](./02-explore-agentic-frameworks/code_samples/02-python-agent-framework-azure-openai.ipynb) (نگاه کنید به "تغییر یافته" — مهاجرت از دفترچه Semantic Kernel قبلی) و لینک آن در README درس.
- افزودن بخش مدل‌ها و ارائه‌دهندگان به [STUDY_GUIDE.md](./STUDY_GUIDE.md).

### تغییر یافته

- **تکمیل چت → Responses API (پایتون).** نمونه‌هایی که مدل را مستقیماً فراخوانی می‌کردند از Chat Completions به Responses API منتقل شدند (`client.responses.create(input=..., store=False)`, `resp.output_text`)، با استفاده از کلاینت `OpenAI` در نقطه انتهایی پایدار Azure OpenAI `/openai/v1/` (بدون نسخه `api_version`). نمونه‌های تحت تأثیر شامل:
  - [06-building-trustworthy-agents/code_samples/06-system-message-framework.ipynb](./06-building-trustworthy-agents/code_samples/06-system-message-framework.ipynb)
  - [06-building-trustworthy-agents/code_samples/06-human-in-the-loop.ipynb](./06-building-trustworthy-agents/code_samples/06-human-in-the-loop.ipynb)
  - [04-tool-use/README.md](./04-tool-use/README.md) — راهنمای کامل فراخوانی تابع (اسکیما ابزار به فرمت Responses تغییر یافته، نتایج ابزار به عنوان `function_call_output`، `max_output_tokens` و غیره برگشت داده می‌شوند).

- **مدل‌های GitHub → Azure OpenAI.** مدل‌های GitHub منسوخ شده‌اند (بازنشستگی در **ژوئیه ۲۰۲۶**) و از API پاسخ‌ها پشتیبانی نمی‌کنند. همه مسیرهای کد مدل‌های GitHub به Azure OpenAI / Microsoft Foundry در نمونه‌های پایتون و .NET تبدیل شدند:
  - پایتون: دفترچه‌های کار درس ۰۸ (`۰۱`–`۰۳`)، درس ۱۴ (`۱۴-handoff`, `۱۴-human-loop`, `hotel_booking_workflow_sample.py`).
  - .NET: `۰۱`–`۰۴`، `۰۷`، `۰۸` فایل‌های `*-dotnet-agent-framework.cs` همراه با مستندات `.md` مربوطه، و دفترچه‌های کار dotNET درس ۰۸/`.md` (`۰۱`–`۰۳`) اکنون از `AzureOpenAIClient(...).GetOpenAIResponseClient(deployment).CreateAIAgent(...)` با `AzureCliCredential` استفاده می‌کنند.
- **هسته معنایی → چارچوب عامل مایکروسافت.** دفترچه قبلی `۰۲-semantic-kernel.ipynb` بازنویسی شده تا از چارچوب عامل مایکروسافت با Azure OpenAI (API پاسخ‌ها) استفاده کند و به `۰۲-python-agent-framework-azure-openai.ipynb` تغییر نام یافت.
- **استانداردسازی بر روی `FoundryChatClient` + `as_agent`.** کد README و دفترچه‌هایی که به `AzureAIProjectAgentProvider` اشاره داشتند، بر اساس الگوی استاندارد شده‌ای که در درس ۰۱ و نمونه‌های چارچوب استفاده شده است: `FoundryChatClient(project_endpoint=..., model=..., credential=AzureCliCredential())` با `provider.as_agent(...)` به‌روزرسانی شدند. این تغییرات در تمامی README و دفترچه‌های درس ۰۲–۱۴ اعمال شد (مثلاً حافظه درس ۱۳، همه دفترچه‌های درس ۱۴، `11-agentic-protocols/code_samples/github-mcp/app.py`).
- **نام‌گذاری محصولات.** در سراسر محتوای انگلیسی تغییر نام داده شد:
  - "Azure AI Foundry" / "Azure AI Studio" → **Microsoft Foundry**
  - "Azure AI Agent Service" → **Microsoft Foundry Agent Service**
  - (بدون تغییر: "Azure OpenAI"، "Azure AI Search"، "Azure AI Inference"، و نام متغیرهای محیطی.)
- **وابستگی‌ها** ([requirements.txt](../../requirements.txt)):
  - قفل شده‌ی نسخه‌های `agent-framework>=1.10.0`، `agent-framework-foundry>=1.10.0`، `agent-framework-openai>=1.10.0`.
  - قفل شده‌ی نسخه‌ی حداقل `openai>=1.108.1` (برای API پاسخ‌ها).
  - حذف `azure-ai-inference` (صرفاً توسط نمونه‌های مهاجرت کرده GitHub Models استفاده می‌شد).
- **پیکربندی محیط** ([.env.example](../../.env.example)): متغیرهای GitHub Models (`GITHUB_TOKEN`، `GITHUB_ENDPOINT`، `GITHUB_MODEL_ID`) حذف شده‌اند؛ `AZURE_OPENAI_ENDPOINT`، `AZURE_OPENAI_DEPLOYMENT`، و متغیر اختیاری `AZURE_OPENAI_API_KEY` افزوده شد؛ نام‌ها به Microsoft Foundry به‌روز شدند.
- **مستندات** — فایل‌های [00-course-setup/README.md](./00-course-setup/README.md)، [AGENTS.md](./AGENTS.md)، [README.md](./README.md)، و [STUDY_GUIDE.md](./STUDY_GUIDE.md) برای موارد فوق به‌روزرسانی شدند (تنظیم متغیرهای محیط، قطعه تایید، راهنمای تامین‌کننده، نام‌گذاری).

### حذف شده‌ها

- مراحل راه‌اندازی مدل‌های GitHub و متغیرهای محیطی مرتبط در مستندات راه‌اندازی (که با Azure OpenAI / Microsoft Foundry جایگزین شده‌اند).

### امنیت / حریم خصوصی (پاکسازی اشتراک‌گذاری عمومی)

- خروجی‌های اجرای دفترچه‌های Jupyter که شناسه واقعی **اشتراک Azure**، نام‌گروه منابع / منابع، و شناسه اتصال بینگ را افشا می‌کردند، به همراه مسیرهای فایل محلی و نام‌های کاربری توسعه‌دهنده پاک شدند در:
  - `08-multi-agent/code_samples/workflows-agent-framework/dotNET/04.dotnet-agent-framework-workflow-aifoundry-condition.ipynb`
  - `08-multi-agent/code_samples/workflows-agent-framework/python/04.python-agent-framework-workflow-aifoundry-condition.ipynb`
  - `15-browser-use/15-browser-user.ipynb`
- تأیید شد که در محتوای انگلیسی ردیابی شده هیچ کلید API، توکن، شناسه اشتراک یا مسیر شخصی باقی نمانده است (ارجاعات به `GITHUB_TOKEN` که باقی است، توکن GitHub Actions در گردش‌های کاری و PAT سرور GitHub MCP در راه‌اندازی درس ۱۱ است — هر دو مشروع و بدون ارتباط با مدل‌های GitHub).

### نکات و محدودیت‌های شناخته شده

- **اجرا / کامپایل نشده‌اند.** این نمونه‌ها به‌روزرسانی‌های آموزشی برای صحت API/نام‌گذاری هستند؛ روی منابع زنده Azure اجرا نشده‌اند و نمونه‌های .NET هم در این محیط کامپایل نشده‌اند. لطفاً در برابر پیاده‌سازی Microsoft Foundry / Azure OpenAI خودتان اعتبارسنجی کنید.
- **پیاده‌سازی مدل باید از API پاسخ‌ها پشتیبانی کند.** از پیاده‌سازی‌ای مانند `gpt-4.1-mini`، `gpt-4.1`، یا مدل `gpt-5.x` استفاده کنید. مدل‌های قدیمی‌تر از عملکرد اصلی پاسخ‌ها پشتیبانی می‌کنند اما همه ویژگی‌ها را ندارند.
- **نسخه چارچوب عامل.** نمونه‌ها آخرین نسخه MAF (`>=1.10.0`) را هدف قرار داده‌اند. فراخوانی استاندارد ایجاد عامل `client.as_agent(...)` است؛ APIها براساس مستندات منتشر شده چارچوب و بیلد نصب شده ارزیابی شدند. اگر نسخه متفاوتی را قفل می‌کنید، در دسترس بودن متد را تأیید کنید (`as_agent` در مقابل `create_agent`).
- **دفترچه کار درس ۰۸ شماره ۰۴** عمداً `AzureAIAgentClient` (از `agent-framework-azure-ai`) را نگه می‌دارد چون از ابزارهای میزبانی شده Microsoft Foundry Agent Service (پایه‌بندی بینگ، مفسر کد) استفاده می‌کند؛ هم‌اکنون بر پایه پاسخ‌ها است.
- **پیاده‌سازی پیش‌فرض .NET.** دو نمونه گردش کار dotNET درس ۰۸ قبلاً مدل خاصی را به صورت سخت‌کد داشتند؛ اکنون به صورت پیش‌فرض `AZURE_OPENAI_DEPLOYMENT` (`gpt-4.1-mini`) است. اگر نمونه‌ای بر ورودی چندرسانه‌ای/بینایی تکیه دارد، `AZURE_OPENAI_DEPLOYMENT` را به مدل مناسب تغییر دهید.
- **Foundry Local** یک نقطه پایان سازگار با OpenAI برای **تکمیل گفتگوها** ارائه می‌دهد و برای توسعه محلی در نظر گرفته شده است؛ برای مجموعه کامل ویژگی API پاسخ‌ها از Azure OpenAI / Microsoft Foundry استفاده کنید.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**سلب مسئولیت**:
این سند با استفاده از سرویس ترجمه هوش مصنوعی [Co-op Translator](https://github.com/Azure/co-op-translator) ترجمه شده است. در حالی که ما در تلاش برای دقت هستیم، لطفاً توجه داشته باشید که ترجمه‌های خودکار ممکن است شامل خطاها یا نادرستی‌هایی باشند. سند اصلی به زبان مادری خود باید به عنوان منبع معتبر در نظر گرفته شود. برای اطلاعات حیاتی، ترجمه حرفه‌ای انسانی توصیه می‌شود. ما در قبال هرگونه سوء تفاهم یا برداشت نادرست ناشی از استفاده از این ترجمه مسئولیتی نداریم.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->