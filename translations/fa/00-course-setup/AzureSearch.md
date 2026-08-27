# راهنمای راه‌اندازی Azure AI Search

این راهنما به شما کمک می‌کند تا Azure AI Search را با استفاده از پرتال Azure راه‌اندازی کنید. مراحل زیر را دنبال کنید تا سرویس جستجوی Azure AI خود را ایجاد و پیکربندی کنید.

## پیش‌نیازها

قبل از شروع، اطمینان حاصل کنید که موارد زیر را دارید:

- یک اشتراک Azure. اگر اشتراک Azure ندارید، می‌توانید یک حساب رایگان در [Azure Free Account](https://azure.microsoft.com/free/?wt.mc_id=studentamb_258691) ایجاد کنید.

## مرحله ۱: ایجاد یک حساب ذخیره‌سازی Azure

۱. این دستورالعمل را دنبال کنید، [ایجاد حساب ذخیره‌سازی Azure](https://learn.microsoft.com/azure/storage/common/storage-account-create?tabs=azure-portal)، تا یک حساب ذخیره‌سازی جدید Azure ایجاد کنید.
   **توجه**: مطمئن شوید که نوع حساب ذخیره‌سازی Standard General Purpose V2 باشد.

## مرحله ۲: ایجاد سرویس Azure AI Search

۱. وارد [پرتال Azure](https://portal.azure.com/?wt.mc_id=studentamb_258691) شوید.
۲. در پنجره ناوبری سمت چپ، روی **ایجاد یک منبع** کلیک کنید.
۳. در جعبه جستجو، "Azure AI Search" را تایپ کنید و **Azure AI Search** را از فهرست نتایج انتخاب کنید.
۴. روی دکمه **ایجاد** کلیک کنید.
۵. در تب **اطلاعات پایه**، موارد زیر را وارد کنید:
   - **اشتراک**: اشتراک Azure خود را انتخاب کنید.
   - **گروه منابع**: یک گروه منابع جدید ایجاد کنید یا یک گروه موجود را انتخاب کنید.
   - **نام منبع**: یک نام منحصر به فرد برای سرویس جستجوی خود وارد کنید.
   - **ناحیه**: نزدیک‌ترین ناحیه به کاربران خود را انتخاب کنید.
   - **سطح قیمت‌گذاری**: یک سطح قیمت‌گذاری متناسب با نیازهای خود انتخاب کنید. می‌توانید برای تست، با سطح رایگان شروع کنید.
۶. روی **بررسی + ایجاد** کلیک کنید.
۷. تنظیمات را مرور کنید و برای ایجاد سرویس جستجو روی **ایجاد** کلیک کنید.

## مرحله ۳: شروع به کار با Azure AI Search

۱. پس از اتمام استقرار، به سرویس جستجوی خود در پرتال Azure بروید.
۲. در پنل نمای کلی سرویس جستجو، URL را کپی کنید. باید چیزی شبیه به `https://<service-name>.search.windows.net` باشد.
۳. **(توصیه شده)** دسترسی بدون کلید با Microsoft Entra ID (RBAC) را فعال کنید، همانطور که در مرحله ۴ زیر نشان داده شده است — نیازی به کلید نیست. نمونه‌های این راهنما برای ایجاد/به‌روزرسانی ایندکس‌ها و آپلود اسناد هستند که به نقش‌های **Search Service Contributor** و **Search Index Data Contributor** نیاز دارند (یا در حالت احراز هویت با کلید، به **کلید مدیریتی اصلی** — نه کلید پرس‌وجو). تنها اگر نمی‌توانید از RBAC استفاده کنید، پنل **Settings > Keys** را باز کنید و **کلید مدیریتی اصلی** را کپی کنید.
۴. مراحل صفحه [Quickstart guide](https://learn.microsoft.com/azure/search/search-get-started-portal?pivots=import-data-new) را دنبال کنید تا یک ایندکس بسازید، داده‌ها را آپلود کنید و جستجو انجام دهید.

## مرحله ۴: استفاده از ابزارهای Azure AI Search

Azure AI Search با ابزارهای مختلفی ادغام می‌شود تا قابلیت‌های جستجوی شما را افزایش دهد. می‌توانید از Azure CLI، Python SDK، .NET SDK و سایر ابزارها برای تنظیمات و عملیات پیشرفته استفاده کنید.

### استفاده از Azure CLI

۱. Azure CLI را با دنبال کردن دستورالعمل‌ها در [Install Azure CLI](https://learn.microsoft.com/cli/azure/install-azure-cli?wt.mc_id=studentamb_258691) نصب کنید.
۲. با فرمان زیر وارد Azure CLI شوید:

   ```bash
   az login
   ```
۳. **(توصیه شده) دسترسی بدون کلید با Microsoft Entra ID (RBAC) را فعال کنید:**

    ```bash
    az search service update --name <service-name> --resource-group <resource-group> --auth-options aadOrApiKey
    az role assignment create --assignee <your-user-or-principal-id> --role "Search Service Contributor" --scope $(az search service show -g <resource-group> -n <service-name> --query id -o tsv)
    az role assignment create --assignee <your-user-or-principal-id> --role "Search Index Data Contributor" --scope $(az search service show -g <resource-group> -n <service-name> --query id -o tsv)
    # سرویس جستجو show فیلد "endpoint" ندارد؛ URL را از نام سرویس بسازید.
    export AZURE_SEARCH_SERVICE_ENDPOINT="https://<service-name>.search.windows.net"
    ```

    با فعال بودن RBAC، نمونه‌های Python و .NET SDK زیر با `DefaultAzureCredential` احراز هویت می‌کنند، که در توسعه محلی از جلسه `az login` شما استفاده می‌کند — نیازی به کلید مدیریتی نیست. به [اتصال به Azure AI Search با استفاده از نقش‌ها](https://learn.microsoft.com/azure/search/search-security-rbac) مراجعه کنید.

۴. **(گزینه جایگزین) احراز هویت مبتنی بر کلید** — فقط اگر نمی‌توانید از RBAC استفاده کنید، کلید مدیر را نیز ذخیره کنید:

#### ذخیره هر دو مقدار نقطه انتهایی و کلید API برای نمونه Azure AI Search در متغیرهای محیطی.

    ```bash
    # zsh/bash
    # az search service show فیلد "endpoint" ندارد؛ URL را از نام سرویس بسازید.
    export AZURE_SEARCH_SERVICE_ENDPOINT="https://<service-name>.search.windows.net"
    export AZURE_SEARCH_API_KEY=$(az search admin-key show -g <resource-group> --service-name <service-name> --query "primaryKey" -o tsv)
    ```

    ```powershell
    # PowerShell
    # az search service show فیلد "endpoint" ندارد؛ URL را از نام سرویس بسازید.
    $env:AZURE_SEARCH_SERVICE_ENDPOINT = "https://<service-name>.search.windows.net"
    $env:AZURE_SEARCH_API_KEY = $(az search admin-key show -g <resource-group> --service-name <service-name> --query "primaryKey" -o tsv)
    ```

### استفاده از Python SDK

۱. کتابخانه مشتری Azure Cognitive Search و Azure Identity برای Python را نصب کنید:

   ```bash
   pip install azure-search-documents azure-identity
   ```

۲. از کد Python زیر برای ایجاد یک ایندکس و آپلود اسناد استفاده کنید:

    ```python
    import os
    from azure.identity import DefaultAzureCredential
    from azure.search.documents import SearchClient
    from azure.search.documents.indexes import SearchIndexClient
    from azure.search.documents.indexes.models import SearchIndex, SimpleField, edm

    service_endpoint = os.getenv("AZURE_SEARCH_SERVICE_ENDPOINT")
    index_name = "sample-index"

    # بدون کلید (توصیه شده): از طریق نقش‌های RBAC شناسه `az login` شما در Entra ID استفاده می‌کند.
    # نیاز به نقش‌های "Search Service Contributor" و "Search Index Data Contributor" دارد.
    credential = DefaultAzureCredential()
    # حالت جایگزین (تأیید هویت مبتنی بر کلید):
    # از azure.core.credentials وارد AzureKeyCredential شوید
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

۱. فرمان زیر را برای ایجاد ایندکس و آپلود اسناد اجرا کنید:

    ```bash
    dotnet run ./AzureSearch.cs
    ```

    نمونه .NET زیر از `DefaultAzureCredential` استفاده می‌کند که می‌تواند از ورود به Azure CLI شما با `az login` در توسعه محلی بهره‌مند شود.

۲. کد .NET فایل `AzureSearch.cs` به شرح زیر است:

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

برای اطلاعات دقیق‌تر، به مستندات زیر مراجعه کنید:

- [ایجاد سرویس Azure Cognitive Search](https://learn.microsoft.com/azure/search/search-create-service-portal?wt.mc_id=studentamb_258691)
- [شروع با Azure Cognitive Search](https://learn.microsoft.com/azure/search/search-get-started-portal?wt.mc_id=studentamb_258691)
- [ابزارهای Azure AI Search](https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-ai-search?tabs=azurecli%2Cpython&pivots=code-examples?wt.mc_id=studentamb_258691)

## نتیجه‌گیری

شما با موفقیت Azure AI Search را با استفاده از پرتال Azure و ابزارهای ادغام‌شده راه‌اندازی کرده‌اید. اکنون می‌توانید ویژگی‌ها و قابلیت‌های پیشرفته‌تر Azure AI Search را برای بهبود راه‌حل‌های جستجوی خود کشف کنید.

برای دریافت کمک بیشتر، به [مستندات Azure Cognitive Search](https://learn.microsoft.com/azure/search/?wt.mc_id=studentamb_258691) مراجعه کنید.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**سلب مسئولیت**:
این سند با استفاده از سرویس ترجمه هوش مصنوعی [Co-op Translator](https://github.com/Azure/co-op-translator) ترجمه شده است. در حالی که ما در تلاش برای دقت هستیم، لطفاً توجه داشته باشید که ترجمه‌های خودکار ممکن است شامل خطاها یا نادرستی‌هایی باشند. سند اصلی به زبان مادری خود باید به عنوان منبع معتبر در نظر گرفته شود. برای اطلاعات حیاتی، ترجمه حرفه‌ای انسانی توصیه می‌شود. ما در قبال هرگونه سوء تفاهم یا برداشت نادرست ناشی از استفاده از این ترجمه مسئولیتی نداریم.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->