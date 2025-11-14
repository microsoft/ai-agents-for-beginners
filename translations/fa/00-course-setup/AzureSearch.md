<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "11e38db0898a788612b917e329dcdb5b",
  "translation_date": "2025-11-07T08:25:14+00:00",
  "source_file": "00-course-setup/AzureSearch.md",
  "language_code": "fa"
}
-->
# راهنمای راه‌اندازی Azure AI Search

این راهنما به شما کمک می‌کند تا Azure AI Search را با استفاده از پورتال Azure راه‌اندازی کنید. مراحل زیر را دنبال کنید تا سرویس Azure AI Search خود را ایجاد و پیکربندی کنید.

## پیش‌نیازها

قبل از شروع، مطمئن شوید که موارد زیر را دارید:

- یک اشتراک Azure. اگر اشتراک Azure ندارید، می‌توانید یک حساب رایگان در [حساب رایگان Azure](https://azure.microsoft.com/free/?wt.mc_id=studentamb_258691) ایجاد کنید.

## مرحله ۱: ایجاد یک حساب ذخیره‌سازی Azure

1. دستورالعمل [ایجاد یک حساب ذخیره‌سازی Azure](https://learn.microsoft.com/azure/storage/common/storage-account-create?tabs=azure-portal) را دنبال کنید تا یک حساب ذخیره‌سازی جدید Azure ایجاد کنید.  
   **NOTE**: مطمئن شوید که نوع حساب ذخیره‌سازی Standard General Purpose V2 باشد.

## مرحله ۲: ایجاد سرویس Azure AI Search

1. وارد [پورتال Azure](https://portal.azure.com/?wt.mc_id=studentamb_258691) شوید.
2. در پنل ناوبری سمت چپ، روی **Create a resource** کلیک کنید.
3. در کادر جستجو، "Azure AI Search" را تایپ کنید و **Azure AI Search** را از لیست نتایج انتخاب کنید.
4. روی دکمه **Create** کلیک کنید.
5. در تب **Basics** اطلاعات زیر را وارد کنید:
   - **Subscription**: اشتراک Azure خود را انتخاب کنید.
   - **Resource group**: یک گروه منابع جدید ایجاد کنید یا یکی از موجود را انتخاب کنید.
   - **Resource name**: یک نام منحصر به فرد برای سرویس جستجوی خود وارد کنید.
   - **Region**: منطقه‌ای را که به کاربران شما نزدیک‌تر است انتخاب کنید.
   - **Pricing tier**: یک سطح قیمت‌گذاری که نیازهای شما را برآورده می‌کند انتخاب کنید. می‌توانید برای آزمایش با سطح رایگان شروع کنید.
6. روی **Review + create** کلیک کنید.
7. تنظیمات را بررسی کرده و روی **Create** کلیک کنید تا سرویس جستجو ایجاد شود.

## مرحله ۳: شروع به کار با Azure AI Search

1. پس از تکمیل استقرار، به سرویس جستجوی خود در پورتال Azure بروید.
2. در پنل نمای کلی سرویس جستجو، URL را کپی کنید. باید به صورت `https://<service-name>.search.windows.net` باشد.
3. در بخش Settings > Keys، کلید جستجو را کپی کنید.
4. مراحل موجود در صفحه [راهنمای شروع سریع](https://learn.microsoft.com/azure/search/search-get-started-portal?pivots=import-data-new) را دنبال کنید تا یک ایندکس ایجاد کنید، داده‌ها را آپلود کنید و یک جستجوی کوئری انجام دهید.

## مرحله ۴: استفاده از ابزارهای Azure AI Search

Azure AI Search با ابزارهای مختلفی برای بهبود قابلیت‌های جستجوی شما ادغام می‌شود. می‌توانید از Azure CLI، Python SDK، .NET SDK و سایر ابزارها برای تنظیمات پیشرفته و عملیات استفاده کنید.

### استفاده از Azure CLI

1. Azure CLI را با دنبال کردن دستورالعمل‌های [نصب Azure CLI](https://learn.microsoft.com/cli/azure/install-azure-cli?wt.mc_id=studentamb_258691) نصب کنید.
2. با استفاده از دستور زیر وارد Azure CLI شوید:

   ```bash
   az login
   ```

3. هر دو endpoint و API key مربوط به نمونه Azure AI Search را در متغیرهای محیطی ذخیره کنید.

    ```bash
    # zsh/bash
    export AZURE_SEARCH_SERVICE_ENDPOINT=$(az search service show -g <resource-group> -n <service-name> --query "endpoint" -o tsv)
    export AZURE_SEARCH_API_KEY=$(az search service admin-key list -g <resource-group> --search-service-name <service-name> --query "primaryKey" -o tsv)
    ```

    ```powershell
    # PowerShell
    $env:AZURE_SEARCH_SERVICE_ENDPOINT = az search service show -g <resource-group> -n <service-name> --query "endpoint" -o tsv
    $env:AZURE_SEARCH_API_KEY = $(az search service admin-key list -g <resource-group> --search-service-name <service-name> --query "primaryKey" -o tsv)
    ```

### استفاده از Python SDK

1. کتابخانه مشتری Azure Cognitive Search برای Python را نصب کنید:

   ```bash
   pip install azure-search-documents
   ```

2. از کد Python زیر برای ایجاد یک ایندکس و آپلود اسناد استفاده کنید:

    ```python
    import os
    from azure.core.credentials import AzureKeyCredential
    from azure.search.documents import SearchClient
    from azure.search.documents.indexes import SearchIndexClient
    from azure.search.documents.indexes.models import SearchIndex, SimpleField, edm

    service_endpoint = os.getenv("AZURE_SEARCH_SERVICE_ENDPOINT")
    api_key = os.getenv("AZURE_SEARCH_API_KEY")
    index_name = "sample-index"

    credential = AzureKeyCredential(api_key)
    index_client = SearchIndexClient(service_endpoint, credential)

    fields = [
        SimpleField(name="id", type=edm.String, key=True),
        SimpleField(name="content", type=edm.String, searchable=True),
    ]

    index = SearchIndex(name=index_name, fields=fields)

    index_client.create_index(index)

    search_client = SearchClient(service_endpoint, index_name, credential)

    documents = [
        {"id": "1", "content": "Hello world"},
        {"id": "2", "content": "Azure Cognitive Search"}
    ]

    search_client.upload_documents(documents)
    ```

### استفاده از .NET SDK

1. دستور زیر را برای ایجاد یک ایندکس و آپلود اسناد اجرا کنید:

    ```bash
    dotnet run ./AzureSearch.cs
    ```

2. این کد .NET مربوط به `AzureSearch.cs` است:

    ```csharp
    #:package Azure.Search.Documents@11.*
    #:property PublishAot=false

    using Azure;
    using Azure.Search.Documents;
    using Azure.Search.Documents.Indexes;
    using Azure.Search.Documents.Indexes.Models;

    var serviceEndpoint = new Uri(Environment.GetEnvironmentVariable("AZURE_SEARCH_SERVICE_ENDPOINT")!);
    var apiKey = Environment.GetEnvironmentVariable("AZURE_SEARCH_API_KEY")!;
    var indexName = "sample-index";

    var credential = new AzureKeyCredential(apiKey);
    var indexClient = new SearchIndexClient(serviceEndpoint, credential);

    var fields = new List<SearchField>()
    {
        new SimpleField("id", SearchFieldDataType.String) { IsKey = true },
        new SearchableField("content")
    };

    var index = new SearchIndex(name: indexName, fields: fields);

    var response = await indexClient.CreateOrUpdateIndexAsync(index);
    Console.WriteLine($"Index '{response.Value.Name}' ready.");

    var searchClient = new SearchClient(serviceEndpoint, indexName, credential);

    var documents = new[]
    {
        new { id = "1", content = "Hello world" },
        new { id = "2", content = "Azure Cognitive Search" }
    };

    var result = await searchClient.UploadDocumentsAsync(documents);
    Console.WriteLine($"Uploaded {result.Value.Results.Count} documents to index '{response.Value.Name}'.");
    ```

برای اطلاعات بیشتر، به مستندات زیر مراجعه کنید:

- [ایجاد سرویس Azure Cognitive Search](https://learn.microsoft.com/azure/search/search-create-service-portal?wt.mc_id=studentamb_258691)
- [شروع به کار با Azure Cognitive Search](https://learn.microsoft.com/azure/search/search-get-started-portal?wt.mc_id=studentamb_258691)
- [ابزارهای Azure AI Search](https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-ai-search?tabs=azurecli%2Cpython&pivots=code-examples?wt.mc_id=studentamb_258691)

## نتیجه‌گیری

شما با موفقیت Azure AI Search را با استفاده از پورتال Azure راه‌اندازی کرده و ابزارها را ادغام کرده‌اید. اکنون می‌توانید ویژگی‌ها و قابلیت‌های پیشرفته‌تر Azure AI Search را برای بهبود راه‌حل‌های جستجوی خود بررسی کنید.

برای کمک بیشتر، به [مستندات Azure Cognitive Search](https://learn.microsoft.com/azure/search/?wt.mc_id=studentamb_258691) مراجعه کنید.

---

**سلب مسئولیت**:  
این سند با استفاده از سرویس ترجمه هوش مصنوعی [Co-op Translator](https://github.com/Azure/co-op-translator) ترجمه شده است. در حالی که ما تلاش می‌کنیم دقت را حفظ کنیم، لطفاً توجه داشته باشید که ترجمه‌های خودکار ممکن است شامل خطاها یا نادرستی‌ها باشند. سند اصلی به زبان اصلی آن باید به عنوان منبع معتبر در نظر گرفته شود. برای اطلاعات حساس، ترجمه حرفه‌ای انسانی توصیه می‌شود. ما مسئولیتی در قبال سوء تفاهم‌ها یا تفسیرهای نادرست ناشی از استفاده از این ترجمه نداریم.