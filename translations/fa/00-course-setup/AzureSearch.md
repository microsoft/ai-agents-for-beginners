# راهنمای راه‌اندازی جستجوی هوش مصنوعی Azure

این راهنما به شما کمک می‌کند تا جستجوی هوش مصنوعی Azure را با استفاده از پرتال Azure راه‌اندازی کنید. برای ایجاد و پیکربندی سرویس جستجوی هوش مصنوعی Azure مراحل زیر را دنبال کنید.

## پیش‌نیازها

قبل از شروع، اطمینان حاصل کنید که موارد زیر را دارید:

- یک اشتراک Azure. اگر اشتراک Azure ندارید، می‌توانید یک حساب رایگان در [Azure Free Account](https://azure.microsoft.com/free/?wt.mc_id=studentamb_258691) ایجاد کنید.

## مرحله ۱: ایجاد یک حساب ذخیره‌سازی Azure

1. این دستورالعمل را دنبال کنید، [Create an Azure storage account](https://learn.microsoft.com/azure/storage/common/storage-account-create?tabs=azure-portal)، تا یک حساب ذخیره‌سازی جدید Azure ایجاد کنید.
   **توجه**: مطمئن شوید نوع حساب ذخیره‌سازی Standard General Purpose V2 باشد.

## مرحله ۲: ایجاد سرویس جستجوی هوش مصنوعی Azure

1. وارد [Azure portal](https://portal.azure.com/?wt.mc_id=studentamb_258691) شوید.
2. در پنل ناوبری سمت چپ، روی **Create a resource** کلیک کنید.
3. در کادر جستجو، «Azure AI Search» را تایپ کرده و **Azure AI Search** را از لیست نتایج انتخاب کنید.
4. روی دکمه **Create** کلیک کنید.
5. در تب **Basics** اطلاعات زیر را وارد کنید:
   - **Subscription**: اشتراک Azure خود را انتخاب کنید.
   - **Resource group**: یک گروه منبع جدید ایجاد کنید یا یک گروه موجود را انتخاب نمایید.
   - **Resource name**: یک نام یکتا برای سرویس جستجوی خود وارد کنید.
   - **Region**: منطقه‌ای را که به کاربران شما نزدیک‌تر است انتخاب کنید.
   - **Pricing tier**: سطح قیمتی که متناسب با نیازهای شماست انتخاب کنید. می‌توانید برای تست با سطح رایگان شروع کنید.
6. روی **Review + create** کلیک کنید.
7. تنظیمات را بازبینی کرده و روی **Create** کلیک کنید تا سرویس جستجو ایجاد شود.

## مرحله ۳: شروع کار با جستجوی هوش مصنوعی Azure

1. پس از اتمام استقرار، به سرویس جستجوی خود در پرتال Azure بروید.
2. در پنجره نمای کلی سرویس جستجو، URL را کپی کنید. این URL باید مانند `https://<service-name>.search.windows.net` باشد.
3. **(توصیه شده)** دسترسی بدون کلید با Microsoft Entra ID (RBAC) را فعال کنید، همانطور که در مرحله ۴ زیر نشان داده شده است — نیازی به کلید نیست. نمونه‌های موجود در این راهنما ایجاد/به‌روزرسانی فهرست‌ها و بارگذاری اسناد را انجام می‌دهند که نیازمند نقش‌های **Search Service Contributor** و **Search Index Data Contributor** هستند (یا برای احراز هویت بر اساس کلید، **primary admin key** — نه کلید پرس‌وجو). فقط اگر نمی‌توانید از RBAC استفاده کنید، به پنجره **Settings > Keys** بروید و **primary admin key** را کپی کنید.
4. مراحل صفحه [Quickstart guide](https://learn.microsoft.com/azure/search/search-get-started-portal?pivots=import-data-new) را برای ایجاد یک فهرست، بارگذاری داده‌ها و انجام جستجو دنبال کنید.

## مرحله ۴: استفاده از ابزارهای جستجوی هوش مصنوعی Azure

جستجوی هوش مصنوعی Azure با ابزارهای مختلفی ادغام می‌شود تا قابلیت‌های جستجوی شما را افزایش دهد. می‌توانید از Azure CLI، Python SDK، .NET SDK و سایر ابزارها برای پیکربندی‌ها و عملیات پیشرفته استفاده کنید.

### استفاده از Azure CLI

1. Azure CLI را با دنبال کردن دستورالعمل‌های موجود در [Install Azure CLI](https://learn.microsoft.com/cli/azure/install-azure-cli?wt.mc_id=studentamb_258691) نصب کنید.
2. با فرمان زیر وارد Azure CLI شوید:

   ```bash
   az login
   ```
3. **(توصیه شده) دسترسی بدون کلید با Microsoft Entra ID (RBAC) فعال کنید:**

    ```bash
    az search service update --name <service-name> --resource-group <resource-group> --auth-options aadOrApiKey
    az role assignment create --assignee <your-user-or-principal-id> --role "Search Service Contributor" --scope $(az search service show -g <resource-group> -n <service-name> --query id -o tsv)
    az role assignment create --assignee <your-user-or-principal-id> --role "Search Index Data Contributor" --scope $(az search service show -g <resource-group> -n <service-name> --query id -o tsv)
    # az search service show has no "endpoint" field; build the URL from the service name.
    export AZURE_SEARCH_SERVICE_ENDPOINT="https://<service-name>.search.windows.net"
    ```

    با فعال بودن RBAC، نمونه‌های Python و .NET SDK زیر با استفاده از `DefaultAzureCredential` احراز هویت می‌کنند، که در طول توسعه محلی از جلسه `az login` شما استفاده می‌کند — نیازی به کلید ادمین نیست. به [Connect to Azure AI Search using roles](https://learn.microsoft.com/azure/search/search-security-rbac) مراجعه کنید.

4. **(گزینه جایگزین) احراز هویت بر پایه کلید** — تنها در صورتی که نتوانید از RBAC استفاده کنید، کلید ادمین را هم ذخیره کنید:

#### هر دو نقطه انتهایی و کلید API مربوط به نمونه جستجوی هوش مصنوعی Azure را در متغیرهای محیطی ذخیره کنید.

   * **zsh / bash**
     ```bash
     # az search service show has no "endpoint" field; build the URL from the service name.
     export AZURE_SEARCH_SERVICE_ENDPOINT="https://<service-name>.search.windows.net"
     export AZURE_SEARCH_API_KEY=$(az search admin-key show -g <resource-group> --service-name <service-name> --query "primaryKey" -o tsv)
     ```

   * **PowerShell**
     ```powershell
     # az search service show has no "endpoint" field; build the URL from the service name.
     $env:AZURE_SEARCH_SERVICE_ENDPOINT = "https://<service-name>.search.windows.net"
     $env:AZURE_SEARCH_API_KEY = $(az search admin-key show -g <resource-group> --service-name <service-name> --query "primaryKey" -o tsv)
     ```

### استفاده از Python SDK

1. کتابخانه کلاینت Azure Cognitive Search و Azure Identity برای Python را نصب کنید:

   ```bash
   pip install azure-search-documents azure-identity
   ```

2. از کد Python زیر برای ایجاد یک فهرست و بارگذاری اسناد استفاده کنید:

    ```python
    import os
    from azure.identity import DefaultAzureCredential
    from azure.search.documents import SearchClient
    from azure.search.documents.indexes import SearchIndexClient
    from azure.search.documents.indexes.models import SearchIndex, SimpleField, edm

    service_endpoint = os.getenv("AZURE_SEARCH_SERVICE_ENDPOINT")
    index_name = "sample-index"

    # Keyless (recommended): uses your `az login` identity via Entra ID RBAC.
    # Requires the "Search Service Contributor" and "Search Index Data Contributor" roles.
    credential = DefaultAzureCredential()
    # Fallback (key-based auth):
    # from azure.core.credentials import AzureKeyCredential
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

1. فرمان زیر را برای ایجاد یک فهرست و بارگذاری اسناد اجرا کنید:

    ```bash
    dotnet run ./AzureSearch.cs
    ```

    نمونه .NET زیر از `DefaultAzureCredential` استفاده می‌کند، که می‌تواند در طول توسعه محلی از طریق ورود به Azure CLI از `az login` استفاده کند.

2. کد .NET مربوط به `AzureSearch.cs` به شرح زیر است:

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

برای اطلاعات دقیق‌تر به مستندات زیر مراجعه کنید:

- [Create an Azure Cognitive Search service](https://learn.microsoft.com/azure/search/search-create-service-portal?wt.mc_id=studentamb_258691)
- [Get started with Azure Cognitive Search](https://learn.microsoft.com/azure/search/search-get-started-portal?wt.mc_id=studentamb_258691)
- [Azure AI Search Tools](https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-ai-search?tabs=azurecli%2Cpython&pivots=code-examples?wt.mc_id=studentamb_258691)

## نتیجه‌گیری

شما با موفقیت جستجوی هوش مصنوعی Azure را از طریق پرتال Azure و ابزارهای یکپارچه راه‌اندازی کرده‌اید. اکنون می‌توانید قابلیت‌ها و ویژگی‌های پیشرفته‌تر جستجوی هوش مصنوعی Azure را برای بهبود راه‌حل‌های جستجوی خود بررسی کنید.

برای دریافت کمک بیشتر، به [مستندات Azure Cognitive Search](https://learn.microsoft.com/azure/search/?wt.mc_id=studentamb_258691) مراجعه کنید.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**سلب مسئولیت**:
این سند با استفاده از سرویس ترجمه هوش مصنوعی [Co-op Translator](https://github.com/Azure/co-op-translator) ترجمه شده است. در حالی که ما در تلاش برای دقت هستیم، لطفاً توجه داشته باشید که ترجمه‌های خودکار ممکن است شامل خطاها یا نادرستی‌هایی باشند. سند اصلی به زبان مادری خود باید به عنوان منبع معتبر در نظر گرفته شود. برای اطلاعات حیاتی، ترجمه حرفه‌ای انسانی توصیه می‌شود. ما در قبال هرگونه سوء تفاهم یا برداشت نادرست ناشی از استفاده از این ترجمه مسئولیتی نداریم.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->