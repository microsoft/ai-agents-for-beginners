# راهنمای راه‌اندازی Azure AI Search

این راهنما به شما کمک می‌کند تا Azure AI Search را با استفاده از پرتال Azure راه‌اندازی کنید. مراحل زیر را دنبال کنید تا سرویس Azure AI Search خود را ایجاد و پیکربندی کنید.

## پیش‌نیازها

قبل از شروع، از موارد زیر اطمینان حاصل کنید:

- یک اشتراک Azure. اگر اشتراک Azure ندارید، می‌توانید یک حساب رایگان در [حساب رایگان Azure](https://azure.microsoft.com/free/?wt.mc_id=studentamb_258691) ایجاد کنید.

## مرحله 1: ایجاد یک حساب ذخیره‌سازی Azure

1. این دستورالعمل را دنبال کنید، [ایجاد یک حساب ذخیره‌سازی Azure](https://learn.microsoft.com/azure/storage/common/storage-account-create?tabs=azure-portal)، تا یک حساب ذخیره‌سازی Azure جدید ایجاد کنید.
   **توجه**: مطمئن شوید که نوع حساب ذخیره‌سازی Standard General Purpose V2 است.

## مرحله 2: ایجاد یک سرویس Azure AI Search

1. وارد [پرتال Azure](https://portal.azure.com/?wt.mc_id=studentamb_258691) شوید.
2. در پنل ناوبری سمت چپ، روی **ایجاد یک منبع** کلیک کنید.
3. در جعبه جستجو، "Azure AI Search" را تایپ کرده و **Azure AI Search** را از فهرست نتایج انتخاب کنید.
4. روی دکمه **ایجاد** کلیک کنید.
5. در تب **اساسی‌ها**، اطلاعات زیر را وارد کنید:
   - **اشتراک**: اشتراک Azure خود را انتخاب کنید.
   - **گروه منابع**: یک گروه منابع جدید ایجاد کنید یا گروه موجود را انتخاب کنید.
   - **نام منبع**: یک نام یکتا برای سرویس جستجوی خود وارد کنید.
   - **منطقه**: نزدیک‌ترین منطقه به کاربران خود را انتخاب کنید.
   - **سطح قیمت‌گذاری**: یک سطح قیمت متناسب با نیاز خود انتخاب کنید. می‌توانید برای آزمایش با سطح رایگان شروع کنید.
6. روی **بررسی + ایجاد** کلیک کنید.
7. تنظیمات را بررسی کرده و روی **ایجاد** کلیک کنید تا سرویس جستجو ایجاد شود.

## مرحله 3: شروع به کار با Azure AI Search

1. پس از تکمیل استقرار، به سرویس جستجوی خود در پرتال Azure بروید.
2. در پنل نمای کلی سرویس جستجو، URL را کپی کنید. باید مشابه `https://<service-name>.search.windows.net` باشد.
3. **(توصیه شده)** دسترسی بدون کلید با Microsoft Entra ID (RBAC) را فعال کنید همانطور که در مرحله 4 زیر نشان داده شده است — نیازی به کلید نیست. نمونه‌های این راهنما ایندکس‌ها را ایجاد/به‌روزرسانی کرده و اسناد را آپلود می‌کنند، که نیاز به نقش‌های **Search Service Contributor** و **Search Index Data Contributor** دارند (یا برای احراز هویت مبتنی بر کلید، کلید مدیریت اصلی — نه کلید پرس‌وجو). فقط در صورتی که نمی‌توانید از RBAC استفاده کنید، به بخش **تنظیمات > کلیدها** رفته و **کلید مدیریت اصلی** را کپی کنید.
4. مراحل صفحه [راهنمای شروع سریع](https://learn.microsoft.com/azure/search/search-get-started-portal?pivots=import-data-new) را برای ایجاد ایندکس، بارگذاری داده‌ها و انجام جستجو دنبال کنید.

## مرحله 4: استفاده از ابزارهای Azure AI Search

Azure AI Search با ابزارهای مختلفی یکپارچه می‌شود تا توانایی‌های جستجوی شما را افزایش دهد. می‌توانید از Azure CLI، Python SDK، .NET SDK و سایر ابزارها برای پیکربندی‌ها و عملیات پیشرفته استفاده کنید.

### استفاده از Azure CLI

1. Azure CLI را با دنبال کردن دستورالعمل‌های [نصب Azure CLI](https://learn.microsoft.com/cli/azure/install-azure-cli?wt.mc_id=studentamb_258691) نصب کنید.
2. با استفاده از دستور زیر وارد Azure CLI شوید:

   ```bash
   az login
   ```
3. **(توصیه شده) دسترسی بدون کلید با Microsoft Entra ID (RBAC) را فعال کنید:**

    ```bash
    az search service update --name <service-name> --resource-group <resource-group> --auth-options aadOrApiKey
    az role assignment create --assignee <your-user-or-principal-id> --role "Search Service Contributor" --scope $(az search service show -g <resource-group> -n <service-name> --query id -o tsv)
    az role assignment create --assignee <your-user-or-principal-id> --role "Search Index Data Contributor" --scope $(az search service show -g <resource-group> -n <service-name> --query id -o tsv)
    # سرویس جستجو show فیلد "endpoint" ندارد؛ آدرس URL را از نام سرویس بسازید.
    export AZURE_SEARCH_SERVICE_ENDPOINT="https://<service-name>.search.windows.net"
    ```

    با فعال‌سازی RBAC، نمونه‌های SDK پایتون و .NET زیر با استفاده از `DefaultAzureCredential` احراز هویت می‌کنند که در زمان توسعه محلی از جلسه `az login` شما استفاده می‌کند — نیازی به کلید مدیریت نیست. مشاهده کنید [اتصال به Azure AI Search با استفاده از نقش‌ها](https://learn.microsoft.com/azure/search/search-security-rbac).

4. **(راه‌حل جایگزین) احراز هویت مبتنی بر کلید** — فقط اگر نتوانید از RBAC استفاده کنید، کلید مدیریت را نیز ذخیره کنید:

#### ذخیره آدرس نقطه انتهایی و کلید API برای نمونه Azure AI Search در متغیرهای محیطی.

    ```bash
    # zsh/bash
    # دستور az search service show فیلد "endpoint" ندارد؛ URL را از نام سرویس بسازید.
    export AZURE_SEARCH_SERVICE_ENDPOINT="https://<service-name>.search.windows.net"
    export AZURE_SEARCH_API_KEY=$(az search admin-key show -g <resource-group> --service-name <service-name> --query "primaryKey" -o tsv)
    ```

    ```powershell
    # پاورشل
    # دستور az search service show فیلد "endpoint" ندارد؛ URL را از نام سرویس بسازید.
    $env:AZURE_SEARCH_SERVICE_ENDPOINT = "https://<service-name>.search.windows.net"
    $env:AZURE_SEARCH_API_KEY = $(az search admin-key show -g <resource-group> --service-name <service-name> --query "primaryKey" -o tsv)
    ```

### استفاده از Python SDK

1. کتابخانه مشتری Azure Cognitive Search و Azure Identity برای پایتون را نصب کنید:

   ```bash
   pip install azure-search-documents azure-identity
   ```

2. از کد پایتون زیر برای ایجاد ایندکس و بارگذاری اسناد استفاده کنید:

    ```python
    import os
    from azure.identity import DefaultAzureCredential
    from azure.search.documents import SearchClient
    from azure.search.documents.indexes import SearchIndexClient
    from azure.search.documents.indexes.models import SearchIndex, SimpleField, edm

    service_endpoint = os.getenv("AZURE_SEARCH_SERVICE_ENDPOINT")
    index_name = "sample-index"

    # بدون کلید (توصیه شده): از هویت `az login` شما از طریق دسترسی RBAC در Entra ID استفاده می‌کند.
    # نیازمند نقش‌های "مشارکت‌کننده سرویس جستجو" و "مشارکت‌کننده داده شاخص جستجو" است.
    credential = DefaultAzureCredential()
    # حالت جایگزین (احراز هویت مبتنی بر کلید):
    # از azure.core.credentials وارد کردن AzureKeyCredential
    # credential = AzureKeyCredential(os.getenv("AZURE_SEARCH_API_KEY"))
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

1. دستور زیر را برای ایجاد ایندکس و بارگذاری اسناد اجرا کنید:

    ```bash
    dotnet run ./AzureSearch.cs
    ```

    نمونه .NET زیر از `DefaultAzureCredential` استفاده می‌کند که می‌تواند از ورود به حساب Azure CLI شما در زمان توسعه محلی `az login` بهره ببرد.

2. این هم کد .NET فایل `AzureSearch.cs`:

    ```csharp
    #:package Azure.Search.Documents@11.*
    #:package Azure.Identity@1.21.0
    #:property PublishAot=false

    using Azure;
    using Azure.Identity;
    using Azure.Search.Documents;
    using Azure.Search.Documents.Indexes;
    using Azure.Search.Documents.Indexes.Models;

    var serviceEndpoint = new Uri(Environment.GetEnvironmentVariable("AZURE_SEARCH_SERVICE_ENDPOINT")!);
    var indexName = "sample-index";

    // Keyless (recommended): uses your `az login` identity via Entra ID RBAC.
    // Requires the "Search Service Contributor" and "Search Index Data Contributor" roles.
    var credential = new DefaultAzureCredential();
    // Fallback (key-based auth): the `using Azure;` directive above already imports
    // AzureKeyCredential; replace the credential line above with:
    // var credential = new AzureKeyCredential(Environment.GetEnvironmentVariable("AZURE_SEARCH_API_KEY")!);
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

- [ایجاد یک سرویس جستجوی شناختی Azure](https://learn.microsoft.com/azure/search/search-create-service-portal?wt.mc_id=studentamb_258691)
- [شروع به کار با Azure Cognitive Search](https://learn.microsoft.com/azure/search/search-get-started-portal?wt.mc_id=studentamb_258691)
- [ابزارهای Azure AI Search](https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-ai-search?tabs=azurecli%2Cpython&pivots=code-examples?wt.mc_id=studentamb_258691)

## نتیجه‌گیری

شما با موفقیت Azure AI Search را با استفاده از پرتال Azure و ابزارهای یکپارچه‌شده راه‌اندازی کرده‌اید. اکنون می‌توانید ویژگی‌ها و قابلیت‌های پیشرفته‌تر Azure AI Search را برای بهبود راه‌حل‌های جستجوی خود کاوش کنید.

برای کمک‌های بیشتر، به [مستندات Azure Cognitive Search](https://learn.microsoft.com/azure/search/?wt.mc_id=studentamb_258691) مراجعه کنید.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**سلب مسئولیت**:
این سند با استفاده از سرویس ترجمه هوش مصنوعی [Co-op Translator](https://github.com/Azure/co-op-translator) ترجمه شده است. در حالی که ما در تلاش برای دقت هستیم، لطفاً توجه داشته باشید که ترجمه‌های خودکار ممکن است شامل خطاها یا نادرستی‌هایی باشند. سند اصلی به زبان مادری خود باید به عنوان منبع معتبر در نظر گرفته شود. برای اطلاعات حیاتی، ترجمه حرفه‌ای انسانی توصیه می‌شود. ما در قبال هرگونه سوء تفاهم یا برداشت نادرست ناشی از استفاده از این ترجمه مسئولیتی نداریم.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->