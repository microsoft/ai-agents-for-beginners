# Посібник із налаштування Azure AI Search

Цей посібник допоможе вам налаштувати Azure AI Search за допомогою порталу Azure. Виконайте наведені нижче кроки, щоб створити та налаштувати службу Azure AI Search.

## Передумови

Перш ніж почати, переконайтеся, що у вас є наступне:

- Підписка Azure. Якщо у вас немає підписки Azure, ви можете створити безкоштовний обліковий запис на [Azure Free Account](https://azure.microsoft.com/free/?wt.mc_id=studentamb_258691).

## Крок 1: Створення облікового запису сховища Azure

1. Виконайте цю інструкцію, [Create an Azure storage account](https://learn.microsoft.com/azure/storage/common/storage-account-create?tabs=azure-portal), щоб створити новий обліковий запис сховища Azure.
   **ПРИМІТКА**: Переконайтеся, що тип облікового запису сховища — Standard General Purpose V2.

## Крок 2: Створення служби Azure AI Search

1. Увійдіть у [Azure портал](https://portal.azure.com/?wt.mc_id=studentamb_258691).
2. У лівій панелі навігації натисніть **Створити ресурс**.
3. У полі пошуку введіть "Azure AI Search" і виберіть **Azure AI Search** зі списку результатів.
4. Натисніть кнопку **Створити**.
5. На вкладці **Основи** заповніть такі дані:
   - **Підписка**: Виберіть вашу підписку Azure.
   - **Група ресурсів**: Створіть нову групу ресурсів або виберіть існуючу.
   - **Назва ресурсу**: Введіть унікальну назву для вашої служби пошуку.
   - **Регіон**: Виберіть регіон, найближчий до ваших користувачів.
   - **Ціновий рівень**: Виберіть ціновий рівень, який підходить вашим вимогам. Для тестування можна почати з Безкоштовного рівня.
6. Натисніть **Перевірити + створити**.
7. Перегляньте налаштування і натисніть **Створити**, щоб створити службу пошуку.

## Крок 3: Початок роботи з Azure AI Search

1. Після завершення розгортання перейдіть до вашої служби пошуку в порталі Azure.
2. У панелі огляду служби пошуку скопіюйте URL. Він повинен виглядати як `https://<service-name>.search.windows.net`.
3. **(Рекомендовано)** Увімкніть доступ без ключа з Microsoft Entra ID (RBAC), як показано в Кроці 4 нижче — ключ не потрібен. Зразки, наведені в цьому посібнику, створюють/оновлюють індекси та завантажують документи, для чого потрібні ролі **Search Service Contributor** і **Search Index Data Contributor** (або, якщо ви використовуєте автентифікацію за ключем, потрібен **primary admin key** — не query key). Якщо ви не можете використати RBAC, відкрийте панель **Settings > Keys** і скопіюйте **primary admin key**.
4. Виконайте кроки з [Quickstart guide](https://learn.microsoft.com/azure/search/search-get-started-portal?pivots=import-data-new), щоб створити індекс, завантажити дані та виконати пошук.

## Крок 4: Використання інструментів Azure AI Search

Azure AI Search інтегрується з різними інструментами для розширення можливостей пошуку. Ви можете використовувати Azure CLI, Python SDK, .NET SDK та інші інструменти для розширених налаштувань і операцій.

### Використання Azure CLI

1. Встановіть Azure CLI, дотримуючись інструкцій на сторінці [Install Azure CLI](https://learn.microsoft.com/cli/azure/install-azure-cli?wt.mc_id=studentamb_258691).
2. Увійдіть у Azure CLI за допомогою команди:

   ```bash
   az login
   ```
3. **(Рекомендовано) Увімкніть доступ без ключа з Microsoft Entra ID (RBAC):**

    ```bash
    az search service update --name <service-name> --resource-group <resource-group> --auth-options aadOrApiKey
    az role assignment create --assignee <your-user-or-principal-id> --role "Search Service Contributor" --scope $(az search service show -g <resource-group> -n <service-name> --query id -o tsv)
    az role assignment create --assignee <your-user-or-principal-id> --role "Search Index Data Contributor" --scope $(az search service show -g <resource-group> -n <service-name> --query id -o tsv)
    # az search service show не має поля "endpoint"; створіть URL зі назви служби.
    export AZURE_SEARCH_SERVICE_ENDPOINT="https://<service-name>.search.windows.net"
    ```

    При увімкненому RBAC зразки для Python і .NET SDK нижче аутентифікуються за допомогою `DefaultAzureCredential`, який використовує вашу сесію `az login` під час локальної розробки — ключ адміністратора не потрібен. Докладніше див. у [Connect to Azure AI Search using roles](https://learn.microsoft.com/azure/search/search-security-rbac).

4. **(Запасний варіант) Автентифікація на основі ключа** — тільки якщо ви не можете використовувати RBAC, збережіть також адміністраторський ключ:

#### Збережіть і кінцеву точку, і API-ключ для екземпляра Azure AI Search у змінні оточення.

    ```bash
    # zsh/bash
    # az search service show не має поля "endpoint"; побудуйте URL із назви служби.
    export AZURE_SEARCH_SERVICE_ENDPOINT="https://<service-name>.search.windows.net"
    export AZURE_SEARCH_API_KEY=$(az search admin-key show -g <resource-group> --service-name <service-name> --query "primaryKey" -o tsv)
    ```

    ```powershell
    # PowerShell
    # az search service show не має поля "endpoint"; побудуйте URL із назви служби.
    $env:AZURE_SEARCH_SERVICE_ENDPOINT = "https://<service-name>.search.windows.net"
    $env:AZURE_SEARCH_API_KEY = $(az search admin-key show -g <resource-group> --service-name <service-name> --query "primaryKey" -o tsv)
    ```

### Використання Python SDK

1. Встановіть бібліотеки Azure Cognitive Search client і Azure Identity для Python:

   ```bash
   pip install azure-search-documents azure-identity
   ```

2. Використайте наступний код Python для створення індексу та завантаження документів:

    ```python
    import os
    from azure.identity import DefaultAzureCredential
    from azure.search.documents import SearchClient
    from azure.search.documents.indexes import SearchIndexClient
    from azure.search.documents.indexes.models import SearchIndex, SimpleField, edm

    service_endpoint = os.getenv("AZURE_SEARCH_SERVICE_ENDPOINT")
    index_name = "sample-index"

    # Безключовий (рекомендується): використовує вашу особистість `az login` через RBAC Entra ID.
    # Потрібні ролі "Співавтор служби пошуку" та "Співавтор даних індексу пошуку".
    credential = DefaultAzureCredential()
    # Запасний варіант (авторизація на основі ключа):
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

### Використання .NET SDK

1. Виконайте наступну команду, щоб створити індекс та завантажити документи:

    ```bash
    dotnet run ./AzureSearch.cs
    ```

    Нижченаведений приклад .NET використовує `DefaultAzureCredential`, який може використовувати ваш вхід у Azure CLI через `az login` під час локальної розробки.

2. Ось код .NET файлу `AzureSearch.cs`:

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

Для детальнішої інформації зверніться до наступної документації:

- [Створення служби Azure Cognitive Search](https://learn.microsoft.com/azure/search/search-create-service-portal?wt.mc_id=studentamb_258691)
- [Початок роботи з Azure Cognitive Search](https://learn.microsoft.com/azure/search/search-get-started-portal?wt.mc_id=studentamb_258691)
- [Інструменти Azure AI Search](https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-ai-search?tabs=azurecli%2Cpython&pivots=code-examples?wt.mc_id=studentamb_258691)

## Висновок

Ви успішно налаштували Azure AI Search за допомогою порталу Azure та інтегрованих інструментів. Тепер ви можете досліджувати більш просунуті функції та можливості Azure AI Search для покращення ваших рішень з пошуку.

Для подальшої допомоги відвідайте [документацію Azure Cognitive Search](https://learn.microsoft.com/azure/search/?wt.mc_id=studentamb_258691).

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Відмова від відповідальності**:
Цей документ було перекладено за допомогою сервісу штучного інтелекту для перекладу [Co-op Translator](https://github.com/Azure/co-op-translator). Хоча ми прагнемо до точності, будь ласка, майте на увазі, що автоматичні переклади можуть містити помилки або неточності. Оригінальний документ рідною мовою слід вважати авторитетним джерелом. Для критично важливої інформації рекомендується професійний людський переклад. Ми не несемо відповідальності за будь-які непорозуміння або неправильні тлумачення, що виникли внаслідок використання цього перекладу.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->