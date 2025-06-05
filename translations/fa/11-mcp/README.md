<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "bbce3572338711aeab758506379ab716",
  "translation_date": "2025-05-21T09:37:24+00:00",
  "source_file": "11-mcp/README.md",
  "language_code": "fa"
}
-->
# درس ۱۱: یکپارچه‌سازی Model Context Protocol (MCP)

## معرفی Model Context Protocol (MCP)

Model Context Protocol (MCP) یک چارچوب پیشرفته است که برای استانداردسازی تعاملات بین مدل‌های هوش مصنوعی و برنامه‌های کلاینت طراحی شده است. MCP به‌عنوان پلی میان مدل‌های هوش مصنوعی و برنامه‌هایی که از آن‌ها استفاده می‌کنند عمل می‌کند و رابطی یکنواخت فراهم می‌آورد، بدون توجه به پیاده‌سازی مدل زیرساختی.

جنبه‌های کلیدی MCP:

- **ارتباط استاندارد شده**: MCP زبان مشترکی برای ارتباط برنامه‌ها با مدل‌های هوش مصنوعی فراهم می‌کند  
- **مدیریت پیشرفته زمینه**: امکان انتقال مؤثر اطلاعات زمینه‌ای به مدل‌های هوش مصنوعی را فراهم می‌آورد  
- **سازگاری چندسکویی**: در زبان‌های برنامه‌نویسی مختلف از جمله C#، Java، JavaScript، Python و TypeScript کار می‌کند  
- **یکپارچه‌سازی بدون درز**: به توسعه‌دهندگان امکان می‌دهد به آسانی مدل‌های مختلف هوش مصنوعی را در برنامه‌های خود ادغام کنند  

MCP به‌ویژه در توسعه عامل‌های هوش مصنوعی ارزشمند است، زیرا به عامل‌ها اجازه می‌دهد از طریق پروتکلی واحد با سیستم‌ها و منابع داده مختلف تعامل داشته باشند و عامل‌ها را انعطاف‌پذیرتر و قدرتمندتر می‌کند.

## اهداف یادگیری
- درک MCP و نقش آن در توسعه عامل‌های هوش مصنوعی  
- راه‌اندازی و پیکربندی سرور MCP برای یکپارچه‌سازی با GitHub  
- ساخت یک سیستم چندعاملی با استفاده از ابزارهای MCP  
- پیاده‌سازی RAG (تولید تقویت‌شده بازیابی) با Azure Cognitive Search  

## پیش‌نیازها
- Python 3.8+  
- Node.js 14+  
- اشتراک Azure  
- حساب GitHub  
- درک پایه‌ای از Semantic Kernel  

## دستورالعمل‌های راه‌اندازی

1. **راه‌اندازی محیط**  
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```

2. **پیکربندی سرویس‌های Azure**  
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
│   └── github-mcp/
│       ├── app.py              # Main application
│       ├── event-descriptions.md  # Event data
│       └── MCP_SETUP.md        # Setup guide
├── README.md
└── requirements.txt
```

## اجزای اصلی

### ۱. سیستم چندعاملی  
- عامل GitHub: تحلیل مخزن  
- عامل Hackathon: پیشنهاد پروژه  
- عامل Events: پیشنهاد رویدادهای فناوری  

### ۲. یکپارچه‌سازی Azure  
- جستجوی شناختی برای فهرست‌بندی رویدادها  
- Azure OpenAI برای هوشمندی عامل  
- پیاده‌سازی الگوی RAG  

### ۳. ابزارهای MCP  
- تحلیل مخزن GitHub  
- بازرسی کد  
- استخراج فراداده  

## مرور کد

نمونه نشان می‌دهد:  
۱. یکپارچه‌سازی سرور MCP  
۲. هماهنگی چندعاملی  
۳. یکپارچه‌سازی Azure Cognitive Search  
۴. پیاده‌سازی الگوی RAG  

ویژگی‌های کلیدی:  
- تحلیل بلادرنگ مخزن GitHub  
- پیشنهادات هوشمند پروژه  
- تطبیق رویدادها با استفاده از Azure Search  
- پاسخ‌های جریان‌یافته با Chainlit  

## اجرای نمونه

برای دستورالعمل‌های دقیق راه‌اندازی و اطلاعات بیشتر، به [Github MCP Server Example README](./code_samples/github-mcp/README.md) مراجعه کنید.

1. سرور MCP را راه‌اندازی کنید:  
   ```bash
   npx @modelcontextprotocol/server-github
   ```

2. برنامه را اجرا کنید:  
   ```bash
   chainlit run app.py -w
   ```

3. یکپارچه‌سازی را آزمایش کنید:  
   ```
   Example query: "Analyze repositories for username: <github_username>"
   ```

## عیب‌یابی

مشکلات رایج و راه‌حل‌ها:  
۱. مشکلات اتصال MCP  
   - اطمینان از اجرای سرور  
   - بررسی در دسترس بودن پورت  
   - تأیید توکن‌های GitHub  

۲. مشکلات Azure Search  
   - اعتبارسنجی رشته‌های اتصال  
   - بررسی وجود شاخص  
   - تأیید بارگذاری سند  

## مراحل بعدی
- کاوش ابزارهای بیشتر MCP  
- پیاده‌سازی عامل‌های سفارشی  
- ارتقای قابلیت‌های RAG  
- افزودن منابع رویداد بیشتر  

## منابع
- [MCP for Beginners](https://aka.ms/mcp-for-beginners)  
- [MCP Documentation](https://github.com/microsoft/semantic-kernel/tree/main/python/semantic-kernel/semantic_kernel/connectors/mcp)  
- [Azure Cognitive Search Docs](https://learn.microsoft.com/azure/search/)  
- [Semantic Kernel Guides](https://learn.microsoft.com/semantic-kernel/)

**سلب مسئولیت**:  
این سند با استفاده از سرویس ترجمه هوش مصنوعی [Co-op Translator](https://github.com/Azure/co-op-translator) ترجمه شده است. در حالی که ما در تلاش برای دقت هستیم، لطفاً توجه داشته باشید که ترجمه‌های خودکار ممکن است شامل خطاها یا نادرستی‌هایی باشند. سند اصلی به زبان بومی خود باید به عنوان منبع معتبر در نظر گرفته شود. برای اطلاعات حیاتی، ترجمه حرفه‌ای انسانی توصیه می‌شود. ما مسئول هیچ گونه سوءتفاهم یا تفسیر نادرستی که از استفاده این ترجمه ناشی شود، نیستیم.