# مثال سرور Github MCP

## توضیحات

این یک نمونهٔ نمایشی بود که برای رقابت AI Agents Hackathon که از طریق Microsoft Reactor برگزار شد ساخته شد.

این ابزار برای پیشنهاد پروژه‌های هکاتون بر اساس مخازن Github یک کاربر استفاده می‌شود.
این کار به روش‌های زیر انجام می‌شود:

1. **Github Agent** - استفاده از Github MCP Server برای بازیابی مخازن و اطلاعات مربوط به آن‌ها.
2. **Hackathon Agent** - داده‌ها را از Github Agent می‌گیرد و ایده‌های خلاقانهٔ پروژهٔ هکاتون را بر اساس پروژه‌ها، زبان‌های مورد استفادهٔ کاربر و مسیرهای پروژه برای AI Agents hackathon ارائه می‌دهد.
3. **Events Agent** - بر اساس پیشنهادهای Hackathon Agent، Events Agent رویدادهای مرتبط از مجموعهٔ AI Agent Hackathon را پیشنهاد می‌دهد.

## اجرای کد 

### متغیرهای محیطی

این دمو از Microsoft Agent Framework، Azure OpenAI Service، Github MCP Server و Azure AI Search استفاده می‌کند.

اطمینان حاصل کنید که متغیرهای محیطی مناسب برای استفاده از این ابزارها را تنظیم کرده‌اید:

```python
AZURE_AI_PROJECT_ENDPOINT=""
AZURE_AI_MODEL_DEPLOYMENT_NAME=""
AZURE_SEARCH_SERVICE_ENDPOINT=""
AZURE_SEARCH_API_KEY=""
``` 

## اجرای سرور Chainlit

برای اتصال به سرور MCP، این دمو از Chainlit به‌عنوان رابط گفتگو استفاده می‌کند. 

برای اجرای سرور، از فرمان زیر در ترمینال خود استفاده کنید:

```bash
chainlit run app.py -w
```

این باید سرور Chainlit شما را در `localhost:8000` راه‌اندازی کند و همچنین شاخص Azure AI Search شما را با محتوای `event-descriptions.md` پُر کند. 

## اتصال به سرور MCP

برای اتصال به Github MCP Server، آیکون "plug" را زیر کادر گفتگو "Type your message here.." انتخاب کنید:

![اتصال MCP](../../../../../translated_images/fa/mcp-chainlit-1.7ed66d648e3cfb28.webp)

از آنجا می‌توانید روی «Connect an MCP» کلیک کنید تا فرمان اتصال به Github MCP Server اضافه شود:

```bash
npx -y @modelcontextprotocol/server-github --env GITHUB_PERSONAL_ACCESS_TOKEN=[YOUR PERSONAL ACCESS TOKEN]
```

Replace "[YOUR PERSONAL ACCESS TOKEN]" with your actual Personal Access Token. 

پس از اتصال، باید یک (1) در کنار آیکون "plug" ببینید تا تأیید کند که متصل است. اگر نه، سعی کنید سرور chainlit را با `chainlit run app.py -w` ری‌استارت کنید.

## استفاده از دمو 

برای شروع جریان کاری عامل که پیشنهاد پروژه‌های هکاتون را ارائه می‌دهد، می‌توانید پیامی مانند زیر تایپ کنید: 

"Recommend hackathon projects for the Github user koreyspace"

Router Agent درخواست شما را تحلیل می‌کند و تعیین می‌کند کدام ترکیب از عوامل (GitHub، Hackathon و Events) برای رسیدگی به پرسش شما مناسب‌تر است. عوامل با هم همکاری می‌کنند تا پیشنهادات جامع بر اساس تحلیل مخازن GitHub، ایده‌پردازی پروژه و رویدادهای فناوری مرتبط ارائه دهند.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
سلب مسئولیت:
این سند با استفاده از سرویس ترجمهٔ هوش مصنوعی [Co-op Translator](https://github.com/Azure/co-op-translator) ترجمه شده است. اگرچه ما در تلاش برای دقت هستیم، لطفاً توجه داشته باشید که ترجمه‌های خودکار ممکن است حاوی خطاها یا نادرستی‌هایی باشند. نسخهٔ اصلی سند به زبان اصلی باید به‌عنوان منبع معتبر در نظر گرفته شود. برای اطلاعات حساس یا حیاتی، استفاده از ترجمهٔ حرفه‌ای توسط مترجم انسانی توصیه می‌شود. ما در قبال هرگونه سوءتفاهم یا تفسیر نادرست ناشی از استفاده از این ترجمه مسئولیتی نداریم.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->