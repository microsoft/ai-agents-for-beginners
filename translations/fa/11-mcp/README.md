<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "e255edb8423b34b4bba20263ef38f208",
  "translation_date": "2025-08-21T12:01:30+00:00",
  "source_file": "11-mcp/README.md",
  "language_code": "fa"
}
-->
# درس ۱۱: یکپارچه‌سازی پروتکل زمینه مدل (MCP)

## مقدمه‌ای بر پروتکل زمینه مدل (MCP)

پروتکل زمینه مدل (MCP) یک چارچوب پیشرفته است که برای استانداردسازی تعاملات بین مدل‌های هوش مصنوعی و برنامه‌های کاربردی طراحی شده است. MCP به عنوان پلی بین مدل‌های هوش مصنوعی و برنامه‌هایی که از آن‌ها استفاده می‌کنند عمل می‌کند و یک رابط کاربری یکپارچه ارائه می‌دهد، بدون توجه به نحوه پیاده‌سازی مدل.

جنبه‌های کلیدی MCP:

- **ارتباط استاندارد شده**: MCP یک زبان مشترک برای ارتباط برنامه‌ها با مدل‌های هوش مصنوعی ایجاد می‌کند  
- **مدیریت پیشرفته زمینه**: امکان انتقال کارآمد اطلاعات زمینه‌ای به مدل‌های هوش مصنوعی را فراهم می‌کند  
- **سازگاری بین پلتفرمی**: با زبان‌های برنامه‌نویسی مختلف از جمله C#، Java، JavaScript، Python و TypeScript کار می‌کند  
- **یکپارچه‌سازی آسان**: به توسعه‌دهندگان اجازه می‌دهد مدل‌های مختلف هوش مصنوعی را به راحتی در برنامه‌های خود ادغام کنند  

MCP به ویژه در توسعه عامل‌های هوش مصنوعی ارزشمند است، زیرا به عامل‌ها اجازه می‌دهد از طریق یک پروتکل یکپارچه با سیستم‌ها و منابع داده مختلف تعامل داشته باشند و انعطاف‌پذیری و قدرت بیشتری پیدا کنند.

## اهداف آموزشی
- درک MCP و نقش آن در توسعه عامل‌های هوش مصنوعی  
- راه‌اندازی و پیکربندی یک سرور MCP برای یکپارچه‌سازی با GitHub  
- ساخت یک سیستم چندعاملی با استفاده از ابزارهای MCP  
- پیاده‌سازی RAG (تولید تقویت‌شده با بازیابی) با Azure Cognitive Search  

## پیش‌نیازها
- Python 3.8+  
- Node.js 14+  
- اشتراک Azure  
- حساب کاربری GitHub  
- آشنایی اولیه با Semantic Kernel  

## دستورالعمل‌های راه‌اندازی

1. **راه‌اندازی محیط**  
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```

2. **پیکربندی خدمات Azure**  
   - ایجاد یک منبع Azure Cognitive Search  
   - راه‌اندازی سرویس Azure OpenAI  
   - پیکربندی متغیرهای محیطی در فایل `.env`  

3. **راه‌اندازی سرور MCP**  
   ```bash
   npm install -g @modelcontextprotocol/server-github
   ```

## ساختار پروژه

```
11-mcp/
├── code_samples/
│   ├── github-mcp/
│   │   ├── app.py              # Main application
│   │   ├── event-descriptions.md  # Event data
│   │   └── MCP_SETUP.md        # Setup guide
│   └── mcp-agents/             # Agent-to-agent communication
│       ├── client/             # MCP client implementation
│       ├── server/             # MCP server with agents
│       └── README.md           # Advanced agent examples
├── README.md
└── requirements.txt
```

## اجزای اصلی

### ۱. سیستم چندعاملی
- عامل GitHub: تحلیل مخازن  
- عامل Hackathon: پیشنهاد پروژه  
- عامل Events: پیشنهاد رویدادهای فناوری  

### ۲. یکپارچه‌سازی Azure
- جستجوی شناختی برای ایندکس‌گذاری رویدادها  
- Azure OpenAI برای هوشمندی عامل‌ها  
- پیاده‌سازی الگوی RAG  

### ۳. ابزارهای MCP
- تحلیل مخازن GitHub  
- بازرسی کد  
- استخراج متاداده  

## مرور کد

نمونه کد نشان می‌دهد:
1. یکپارچه‌سازی سرور MCP  
2. هماهنگی چندعامل  
3. یکپارچه‌سازی Azure Cognitive Search  
4. پیاده‌سازی الگوی RAG  

ویژگی‌های کلیدی:
- تحلیل بلادرنگ مخازن GitHub  
- پیشنهادهای هوشمندانه پروژه  
- تطبیق رویدادها با استفاده از Azure Search  
- پاسخ‌های استریم‌شده با Chainlit  

## اجرای نمونه

برای دستورالعمل‌های دقیق راه‌اندازی و اطلاعات بیشتر، به [Github MCP Server Example README](./code_samples/github-mcp/README.md) مراجعه کنید.

1. سرور MCP را اجرا کنید:  
   ```bash
   npx @modelcontextprotocol/server-github
   ```

2. برنامه را راه‌اندازی کنید:  
   ```bash
   chainlit run app.py -w
   ```

3. یکپارچه‌سازی را آزمایش کنید:  
   ```
   Example query: "Analyze repositories for username: <github_username>"
   ```

## رفع اشکال

مشکلات رایج و راه‌حل‌ها:
1. مشکلات اتصال MCP  
   - اطمینان حاصل کنید که سرور در حال اجرا است  
   - دسترسی به پورت را بررسی کنید  
   - توکن‌های GitHub را تأیید کنید  

2. مشکلات جستجوی Azure  
   - رشته‌های اتصال را بررسی کنید  
   - وجود ایندکس را تأیید کنید  
   - آپلود اسناد را بررسی کنید  

## مراحل بعدی
- بررسی ابزارهای اضافی MCP  
- پیاده‌سازی عامل‌های سفارشی  
- بهبود قابلیت‌های RAG  
- افزودن منابع رویداد بیشتر  
- **پیشرفته**: به [mcp-agents/](../../../11-mcp/code_samples/mcp-agents) برای مثال‌هایی از ارتباط عامل به عامل مراجعه کنید  

## منابع
- [MCP برای مبتدیان](https://aka.ms/mcp-for-beginners)  
- [مستندات MCP](https://github.com/microsoft/semantic-kernel/tree/main/python/semantic-kernel/semantic_kernel/connectors/mcp)  
- [مستندات Azure Cognitive Search](https://learn.microsoft.com/azure/search/)  
- [راهنماهای Semantic Kernel](https://learn.microsoft.com/semantic-kernel/)  

**سلب مسئولیت**:  
این سند با استفاده از سرویس ترجمه هوش مصنوعی [Co-op Translator](https://github.com/Azure/co-op-translator) ترجمه شده است. در حالی که ما برای دقت تلاش می‌کنیم، لطفاً توجه داشته باشید که ترجمه‌های خودکار ممکن است شامل خطاها یا نادرستی‌هایی باشند. سند اصلی به زبان اصلی آن باید به عنوان منبع معتبر در نظر گرفته شود. برای اطلاعات حساس، ترجمه حرفه‌ای انسانی توصیه می‌شود. ما هیچ مسئولیتی در قبال سوءتفاهم‌ها یا تفسیرهای نادرست ناشی از استفاده از این ترجمه نداریم.