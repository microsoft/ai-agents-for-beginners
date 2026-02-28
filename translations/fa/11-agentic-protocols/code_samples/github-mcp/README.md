# مثال Github MCP Server

## توضیحات

این یک نسخه نمایشی است که برای هکاتون AI Agents که از طریق Microsoft Reactor برگزار شد، ایجاد شده است.

این ابزار برای پیشنهاد پروژه‌های هکاتون بر اساس مخازن Github یک کاربر استفاده می‌شود.
این کار از طریق موارد زیر انجام می‌شود:

1. **Github Agent** - استفاده از Github MCP Server برای بازیابی مخازن و اطلاعات مربوط به آن‌ها.
2. **Hackathon Agent** - داده‌ها را از Github Agent گرفته و ایده‌های خلاقانه پروژه هکاتون را بر اساس پروژه‌ها، زبان‌های مورد استفاده کاربر و مسیرهای پروژه برای هکاتون AI Agents ارائه می‌دهد.
3. **Events Agent** - بر اساس پیشنهادهای Hackathon Agent، Events Agent رویدادهای مرتبط از سری هکاتون AI Agent را پیشنهاد می‌دهد.
## اجرای کد 

### Environment Variables

این نسخه نمایشی از Microsoft Agent Framework، Azure OpenAI Service، Github MCP Server و Azure AI Search استفاده می‌کند.

اطمینان حاصل کنید که متغیرهای محیطی مناسب برای استفاده از این ابزارها تنظیم شده‌اند:

```python
AZURE_AI_PROJECT_ENDPOINT=""
AZURE_AI_MODEL_DEPLOYMENT_NAME=""
AZURE_SEARCH_SERVICE_ENDPOINT=""
AZURE_SEARCH_API_KEY=""
``` 

## Running the Chainlit Server

برای اتصال به سرور MCP، این نسخه نمایشی از Chainlit به‌عنوان رابط چت استفاده می‌کند。 

برای اجرای سرور، از دستور زیر در ترمینال خود استفاده کنید:

```bash
chainlit run app.py -w
```

این باید سرور Chainlit شما را روی `localhost:8000` راه‌اندازی کند و همچنین شاخص Azure AI Search شما را با محتوای `event-descriptions.md` پر کند。 

## Connecting to the MCP Server

برای اتصال به Github MCP Server، آیکون "plug" را زیر کادر چت "Type your message here.." انتخاب کنید:

![اتصال MCP](../../../../../translated_images/fa/mcp-chainlit-1.7ed66d648e3cfb28.webp)

از آن‌جا می‌توانید روی "Connect an MCP" کلیک کنید تا فرمان اتصال به Github MCP Server اضافه شود:

```bash
npx -y @modelcontextprotocol/server-github --env GITHUB_PERSONAL_ACCESS_TOKEN=[YOUR PERSONAL ACCESS TOKEN]
```

Replace "[YOUR PERSONAL ACCESS TOKEN]" with your actual Personal Access Token. 

پس از اتصال، باید عدد (1) را در کنار آیکون "plug" ببینید تا تأیید شود که متصل است. در غیر این صورت، سعی کنید سرور chainlit را با `chainlit run app.py -w` مجدداً راه‌اندازی کنید。

## Using the Demo 

برای شروع گردش کاری عامل (agent) در پیشنهاد پروژه‌های هکاتون، می‌توانید پیامی مانند زیر تایپ کنید: 

"Recommend hackathon projects for the Github user koreyspace"

Router Agent درخواست شما را تحلیل می‌کند و تعیین می‌کند که کدام ترکیب از عوامل (GitHub، Hackathon، and Events) برای رسیدگی به پرسش شما مناسب‌تر است. عوامل با هم کار می‌کنند تا پیشنهادهای جامع بر اساس تحلیل مخازن GitHub، ایده‌پردازی پروژه و رویدادهای مرتبط فنی ارائه دهند.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
سلب مسئولیت:
این سند با استفاده از سرویس ترجمهٔ هوش مصنوعی Co‑op Translator (https://github.com/Azure/co-op-translator) ترجمه شده است. در حالی که ما در تلاش برای دقت هستیم، لطفاً توجه داشته باشید که ترجمه‌های خودکار ممکن است حاوی خطا یا نادرستی باشند. سند اصلی به زبان مبدا باید به‌عنوان منبع معتبر تلقی شود. برای اطلاعات حساس یا حیاتی، ترجمهٔ حرفه‌ای انسانی توصیه می‌شود. ما در برابر هرگونه سوءتفاهم یا تفسیر نادرست ناشی از استفاده از این ترجمه مسئولیتی نداریم.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->