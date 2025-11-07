<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "11e38db0898a788612b917e329dcdb5b",
  "translation_date": "2025-11-07T08:52:54+00:00",
  "source_file": "00-course-setup/AzureSearch.md",
  "language_code": "uk"
}
-->
# Посібник з налаштування Azure AI Search

Цей посібник допоможе вам налаштувати Azure AI Search за допомогою порталу Azure. Дотримуйтесь наведених нижче кроків, щоб створити та налаштувати вашу службу Azure AI Search.

## Попередні вимоги

Перед початком переконайтеся, що у вас є наступне:

- Підписка на Azure. Якщо у вас немає підписки на Azure, ви можете створити безкоштовний обліковий запис на [Azure Free Account](https://azure.microsoft.com/free/?wt.mc_id=studentamb_258691).

## Крок 1: Створення облікового запису Azure Storage

1. Дотримуйтесь інструкцій [Створення облікового запису Azure Storage](https://learn.microsoft.com/azure/storage/common/storage-account-create?tabs=azure-portal), щоб створити новий обліковий запис Azure Storage.
   **NOTE**: Переконайтеся, що тип облікового запису Storage — Standard General Purpose V2.

## Крок 2: Створення служби Azure AI Search

1. Увійдіть до [порталу Azure](https://portal.azure.com/?wt.mc_id=studentamb_258691).
2. У лівій навігаційній панелі натисніть **Create a resource**.
3. У полі пошуку введіть "Azure AI Search" і виберіть **Azure AI Search** зі списку результатів.
4. Натисніть кнопку **Create**.
5. У вкладці **Basics** надайте наступну інформацію:
   - **Subscription**: Виберіть вашу підписку на Azure.
   - **Resource group**: Створіть нову групу ресурсів або виберіть існуючу.
   - **Resource name**: Введіть унікальне ім'я для вашої служби пошуку.
   - **Region**: Виберіть регіон, найближчий до ваших користувачів.
   - **Pricing tier**: Виберіть рівень цін, який відповідає вашим вимогам. Ви можете почати з безкоштовного рівня для тестування.
6. Натисніть **Review + create**.
7. Перегляньте налаштування та натисніть **Create**, щоб створити службу пошуку.

## Крок 3: Початок роботи з Azure AI Search

1. Після завершення розгортання перейдіть до вашої служби пошуку в порталі Azure.
2. У панелі огляду служби пошуку скопіюйте URL-адресу. Вона повинна виглядати як `https://<service-name>.search.windows.net`.
3. У розділі Settings > Keys скопіюйте ключ запиту.
4. Дотримуйтесь кроків на сторінці [Швидкий старт](https://learn.microsoft.com/azure/search/search-get-started-portal?pivots=import-data-new), щоб створити індекс, завантажити дані та виконати пошуковий запит.

## Крок 4: Використання інструментів Azure AI Search

Azure AI Search інтегрується з різними інструментами для покращення ваших можливостей пошуку. Ви можете використовувати Azure CLI, Python SDK, .NET SDK та інші інструменти для розширених конфігурацій та операцій.

### Використання Azure CLI

1. Встановіть Azure CLI, дотримуючись інструкцій на [Встановлення Azure CLI](https://learn.microsoft.com/cli/azure/install-azure-cli?wt.mc_id=studentamb_258691).
2. Увійдіть до Azure CLI за допомогою команди:

   ```bash
   az login
   ```

3. Збережіть як змінні середовища як кінцеву точку, так і API-ключ для екземпляра Azure AI Search.

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

### Використання Python SDK

1. Встановіть бібліотеку клієнта Azure Cognitive Search для Python:

   ```bash
   pip install azure-search-documents
   ```

2. Використовуйте наступний код Python для створення індексу та завантаження документів:

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

### Використання .NET SDK

1. Виконайте наступну команду для створення індексу та завантаження документів:

    ```bash
    dotnet run ./AzureSearch.cs
    ```

2. Ось код .NET для `AzureSearch.cs`:

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

Для отримання більш детальної інформації зверніться до наступної документації:

- [Створення служби Azure Cognitive Search](https://learn.microsoft.com/azure/search/search-create-service-portal?wt.mc_id=studentamb_258691)
- [Початок роботи з Azure Cognitive Search](https://learn.microsoft.com/azure/search/search-get-started-portal?wt.mc_id=studentamb_258691)
- [Інструменти Azure AI Search](https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-ai-search?tabs=azurecli%2Cpython&pivots=code-examples?wt.mc_id=studentamb_258691)

## Висновок

Ви успішно налаштували Azure AI Search за допомогою порталу Azure та інтегрованих інструментів. Тепер ви можете досліджувати більш розширені функції та можливості Azure AI Search для покращення ваших рішень пошуку.

Для додаткової допомоги відвідайте [документацію Azure Cognitive Search](https://learn.microsoft.com/azure/search/?wt.mc_id=studentamb_258691).

---

**Відмова від відповідальності**:  
Цей документ був перекладений за допомогою сервісу автоматичного перекладу [Co-op Translator](https://github.com/Azure/co-op-translator). Хоча ми прагнемо до точності, будь ласка, майте на увазі, що автоматичні переклади можуть містити помилки або неточності. Оригінальний документ на його рідній мові слід вважати авторитетним джерелом. Для критичної інформації рекомендується професійний людський переклад. Ми не несемо відповідальності за будь-які непорозуміння або неправильні тлумачення, що виникають внаслідок використання цього перекладу.