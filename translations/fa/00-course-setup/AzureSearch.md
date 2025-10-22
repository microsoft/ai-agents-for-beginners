<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f0ce2d470f3efad6f8c7df376f416a4b",
  "translation_date": "2025-07-12T07:33:38+00:00",
  "source_file": "00-course-setup/AzureSearch.md",
  "language_code": "fa"
}
-->
# راهنمای راه‌اندازی Azure AI Search

این راهنما به شما کمک می‌کند تا Azure AI Search را با استفاده از پرتال Azure راه‌اندازی کنید. مراحل زیر را دنبال کنید تا سرویس Azure AI Search خود را ایجاد و پیکربندی کنید.

## پیش‌نیازها

قبل از شروع، مطمئن شوید که موارد زیر را دارید:

- یک اشتراک Azure. اگر اشتراک Azure ندارید، می‌توانید یک حساب رایگان در [Azure Free Account](https://azure.microsoft.com/free/?wt.mc_id=studentamb_258691) ایجاد کنید.

## مرحله ۱: ایجاد سرویس Azure AI Search

1. وارد [Azure portal](https://portal.azure.com/?wt.mc_id=studentamb_258691) شوید.
2. در پنل ناوبری سمت چپ، روی **Create a resource** کلیک کنید.
3. در کادر جستجو، عبارت "Azure AI Search" را تایپ کرده و **Azure AI Search** را از لیست نتایج انتخاب کنید.
4. روی دکمه **Create** کلیک کنید.
5. در تب **Basics** اطلاعات زیر را وارد کنید:
   - **Subscription**: اشتراک Azure خود را انتخاب کنید.
   - **Resource group**: یک گروه منابع جدید ایجاد کنید یا یک گروه موجود را انتخاب کنید.
   - **Resource name**: یک نام یکتا برای سرویس جستجوی خود وارد کنید.
   - **Region**: منطقه‌ای که به کاربران شما نزدیک‌تر است را انتخاب کنید.
   - **Pricing tier**: سطح قیمت‌گذاری متناسب با نیازهای خود را انتخاب کنید. می‌توانید برای آزمایش با سطح رایگان شروع کنید.
6. روی **Review + create** کلیک کنید.
7. تنظیمات را بررسی کرده و روی **Create** کلیک کنید تا سرویس جستجو ایجاد شود.

## مرحله ۲: شروع کار با Azure AI Search

1. پس از اتمام استقرار، به سرویس جستجوی خود در پرتال Azure بروید.
2. در صفحه نمای کلی سرویس جستجو، روی دکمه **Quickstart** کلیک کنید.
3. مراحل راهنمای Quickstart را دنبال کنید تا یک ایندکس ایجاد کنید، داده‌ها را بارگذاری کنید و یک پرس‌وجوی جستجو انجام دهید.

### ایجاد یک ایندکس

1. در راهنمای Quickstart، روی **Create an index** کلیک کنید.
2. ساختار ایندکس را با مشخص کردن فیلدها و ویژگی‌های آن‌ها (مثلاً نوع داده، قابل جستجو بودن، قابل فیلتر بودن) تعریف کنید.
3. روی **Create** کلیک کنید تا ایندکس ایجاد شود.

### بارگذاری داده‌ها

1. در راهنمای Quickstart، روی **Upload data** کلیک کنید.
2. یک منبع داده انتخاب کنید (مثلاً Azure Blob Storage، Azure SQL Database) و جزئیات اتصال لازم را وارد کنید.
3. فیلدهای منبع داده را به فیلدهای ایندکس نگاشت کنید.
4. روی **Submit** کلیک کنید تا داده‌ها به ایندکس بارگذاری شوند.

### انجام یک پرس‌وجوی جستجو

1. در راهنمای Quickstart، روی **Search explorer** کلیک کنید.
2. یک پرس‌وجوی جستجو در کادر جستجو وارد کنید تا عملکرد جستجو را آزمایش کنید.
3. نتایج جستجو را بررسی کرده و در صورت نیاز ساختار ایندکس یا داده‌ها را تنظیم کنید.

## مرحله ۳: استفاده از ابزارهای Azure AI Search

Azure AI Search با ابزارهای مختلفی ادغام می‌شود تا قابلیت‌های جستجوی شما را بهبود بخشد. می‌توانید از Azure CLI، Python SDK و سایر ابزارها برای پیکربندی‌ها و عملیات پیشرفته استفاده کنید.

### استفاده از Azure CLI

1. Azure CLI را با دنبال کردن دستورالعمل‌های موجود در [Install Azure CLI](https://learn.microsoft.com/en-us/cli/azure/install-azure-cli?wt.mc_id=studentamb_258691) نصب کنید.
2. با استفاده از دستور زیر وارد Azure CLI شوید:
   ```bash
   az login
   ```
3. با استفاده از Azure CLI یک سرویس جستجوی جدید ایجاد کنید:
   ```bash
   az search service create --resource-group <resource-group> --name <service-name> --sku Free
   ```
4. با استفاده از Azure CLI یک ایندکس ایجاد کنید:
   ```bash
   az search index create --service-name <service-name> --name <index-name> --fields "field1:type, field2:type"
   ```

### استفاده از Python SDK

1. کتابخانه کلاینت Azure Cognitive Search برای Python را نصب کنید:
   ```bash
   pip install azure-search-documents
   ```
2. از کد Python زیر برای ایجاد ایندکس و بارگذاری اسناد استفاده کنید:
   ```python
   from azure.core.credentials import AzureKeyCredential
   from azure.search.documents import SearchClient
   from azure.search.documents.indexes import SearchIndexClient
   from azure.search.documents.indexes.models import SearchIndex, SimpleField, edm

   service_endpoint = "https://<service-name>.search.windows.net"
   api_key = "<api-key>"

   index_client = SearchIndexClient(service_endpoint, AzureKeyCredential(api_key))

   fields = [
       SimpleField(name="id", type=edm.String, key=True),
       SimpleField(name="content", type=edm.String, searchable=True),
   ]

   index = SearchIndex(name="sample-index", fields=fields)

   index_client.create_index(index)

   search_client = SearchClient(service_endpoint, "sample-index", AzureKeyCredential(api_key))

   documents = [
       {"id": "1", "content": "Hello world"},
       {"id": "2", "content": "Azure Cognitive Search"}
   ]

   search_client.upload_documents(documents)
   ```

برای اطلاعات دقیق‌تر، به مستندات زیر مراجعه کنید:

- [Create an Azure Cognitive Search service](https://learn.microsoft.com/en-us/azure/search/search-create-service-portal?wt.mc_id=studentamb_258691)
- [Get started with Azure Cognitive Search](https://learn.microsoft.com/en-us/azure/search/search-get-started-portal?wt.mc_id=studentamb_258691)
- [Azure AI Search Tools](https://learn.microsoft.com/en-us/azure/ai-services/agents/how-to/tools/azure-ai-search?tabs=azurecli%2Cpython&pivots=code-examples?wt.mc_id=studentamb_258691)

## نتیجه‌گیری

شما با موفقیت Azure AI Search را با استفاده از پرتال Azure و ابزارهای مرتبط راه‌اندازی کردید. اکنون می‌توانید ویژگی‌ها و قابلیت‌های پیشرفته‌تر Azure AI Search را برای بهبود راه‌حل‌های جستجوی خود کاوش کنید.

برای دریافت کمک بیشتر، به [مستندات Azure Cognitive Search](https://learn.microsoft.com/en-us/azure/search/?wt.mc_id=studentamb_258691) مراجعه کنید.

**سلب مسئولیت**:  
این سند با استفاده از سرویس ترجمه هوش مصنوعی [Co-op Translator](https://github.com/Azure/co-op-translator) ترجمه شده است. در حالی که ما در تلاش برای دقت هستیم، لطفاً توجه داشته باشید که ترجمه‌های خودکار ممکن است حاوی خطاها یا نواقصی باشند. سند اصلی به زبان بومی خود باید به عنوان منبع معتبر در نظر گرفته شود. برای اطلاعات حیاتی، ترجمه حرفه‌ای انسانی توصیه می‌شود. ما مسئول هیچ گونه سوءتفاهم یا تفسیر نادرستی که از استفاده این ترجمه ناشی شود، نیستیم.