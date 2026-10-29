# Руководство по настройке Azure AI Search

Это руководство поможет вам настроить Azure AI Search с использованием портала Azure. Следуйте приведённым ниже шагам, чтобы создать и настроить ваш сервис Azure AI Search.

## Необходимые условия

Перед началом убедитесь, что у вас есть следующее:

- Подписка на Azure. Если у вас нет подписки Azure, вы можете создать бесплатную учётную запись на [Azure Free Account](https://azure.microsoft.com/free/?wt.mc_id=studentamb_258691).

## Шаг 1: Создайте учётную запись хранения Azure

1. Следуйте этой инструкции, [Create an Azure storage account](https://learn.microsoft.com/azure/storage/common/storage-account-create?tabs=azure-portal), чтобы создать новую учётную запись хранения Azure.
   **ПРИМЕЧАНИЕ**: Убедитесь, что тип учётной записи хранения — Standard General Purpose V2.

## Шаг 2: Создайте сервис Azure AI Search

1. Войдите в [Azure портал](https://portal.azure.com/?wt.mc_id=studentamb_258691).
2. В левом навигационном меню нажмите **Создать ресурс**.
3. В строке поиска введите "Azure AI Search" и выберите **Azure AI Search** из списка результатов.
4. Нажмите кнопку **Создать**.
5. На вкладке **Основы** введите следующую информацию:
   - **Подписка**: Выберите вашу подписку Azure.
   - **Группа ресурсов**: Создайте новую группу ресурсов или выберите существующую.
   - **Имя ресурса**: Введите уникальное имя для вашего поискового сервиса.
   - **Регион**: Выберите регион, ближайший к вашим пользователям.
   - **Уровень тарифа**: Выберите тариф, подходящий для ваших требований. Для тестирования можно начать с бесплатного тарифа.
6. Нажмите **Проверить + создать**.
7. Проверьте настройки и нажмите **Создать** для создания поискового сервиса.

## Шаг 3: Начало работы с Azure AI Search

1. После завершения развертывания перейдите к вашему поисковому сервису в Azure портале.
2. В панели обзора сервиса поиска скопируйте URL. Он должен выглядеть как `https://<service-name>.search.windows.net`.
3. **(Рекомендуется)** Включите доступ без ключа с Microsoft Entra ID (RBAC), как показано в Шаге 4 ниже — ключ не нужен. Примеры в этом руководстве создают/обновляют индексы и загружают документы, для чего требуются роли **Search Service Contributor** и **Search Index Data Contributor** (или, для аутентификации на основе ключа, **primary admin key** — не query key). Только если вы не можете использовать RBAC, откройте панель **Настройки > Ключи** и скопируйте **primary admin key**.
4. Следуйте шагам на странице [Quickstart guide](https://learn.microsoft.com/azure/search/search-get-started-portal?pivots=import-data-new) для создания индекса, загрузки данных и выполнения поиска.

## Шаг 4: Использование инструментов Azure AI Search

Azure AI Search интегрируется с различными инструментами для расширения возможностей поиска. Вы можете использовать Azure CLI, Python SDK, .NET SDK и другие инструменты для продвинутой настройки и операций.

### Использование Azure CLI

1. Установите Azure CLI, следуя инструкциям на странице [Install Azure CLI](https://learn.microsoft.com/cli/azure/install-azure-cli?wt.mc_id=studentamb_258691).
2. Войдите в Azure CLI с помощью команды:

   ```bash
   az login
   ```
3. **(Рекомендуется) Включите доступ без ключа с Microsoft Entra ID (RBAC):**

    ```bash
    az search service update --name <service-name> --resource-group <resource-group> --auth-options aadOrApiKey
    az role assignment create --assignee <your-user-or-principal-id> --role "Search Service Contributor" --scope $(az search service show -g <resource-group> -n <service-name> --query id -o tsv)
    az role assignment create --assignee <your-user-or-principal-id> --role "Search Index Data Contributor" --scope $(az search service show -g <resource-group> -n <service-name> --query id -o tsv)
    # az search service show has no "endpoint" field; build the URL from the service name.
    export AZURE_SEARCH_SERVICE_ENDPOINT="https://<service-name>.search.windows.net"
    ```

    При включённом RBAC образцы на Python и .NET SDK аутентифицируются с помощью `DefaultAzureCredential`, который использует вашу сессию `az login` во время локальной разработки — ключ администратора не требуется. Смотрите [Connect to Azure AI Search using roles](https://learn.microsoft.com/azure/search/search-security-rbac).

4. **(Альтернативно) Аутентификация на основе ключа** — только если вы не можете использовать RBAC, сохраните также ключ администратора:

#### Сохраните как конечную точку, так и API-ключ Azure AI Search в переменные окружения.

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

### Использование Python SDK

1. Установите клиентскую библиотеку Azure Cognitive Search и Azure Identity для Python:

   ```bash
   pip install azure-search-documents azure-identity
   ```

2. Используйте следующий код Python для создания индекса и загрузки документов:

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

### Использование .NET SDK

1. Выполните следующую команду для создания индекса и загрузки документов:

    ```bash
    dotnet run ./AzureSearch.cs
    ```

    Пример на .NET ниже использует `DefaultAzureCredential`, который может использовать вашу регистрацию в Azure CLI из `az login` во время локальной разработки.

2. Вот код на .NET из `AzureSearch.cs`:

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

Для более подробной информации обратитесь к следующей документации:

- [Create an Azure Cognitive Search service](https://learn.microsoft.com/azure/search/search-create-service-portal?wt.mc_id=studentamb_258691)
- [Get started with Azure Cognitive Search](https://learn.microsoft.com/azure/search/search-get-started-portal?wt.mc_id=studentamb_258691)
- [Azure AI Search Tools](https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-ai-search?tabs=azurecli%2Cpython&pivots=code-examples?wt.mc_id=studentamb_258691)

## Заключение

Вы успешно настроили Azure AI Search с помощью портала Azure и интегрированных инструментов. Теперь вы можете исследовать более продвинутые функции и возможности Azure AI Search для улучшения ваших поисковых решений.

Для дальнейшей помощи посетите [документацию Azure Cognitive Search](https://learn.microsoft.com/azure/search/?wt.mc_id=studentamb_258691).

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Отказ от ответственности**:
Этот документ был переведен с использованием сервиса машинного перевода [Co-op Translator](https://github.com/Azure/co-op-translator). Несмотря на наши усилия по обеспечению точности, имейте в виду, что автоматический перевод может содержать ошибки или неточности. Оригинальный документ на его исходном языке следует считать авторитетным источником. Для получения критически важной информации рекомендуется обратиться к профессиональному человеческому переводу. Мы не несем ответственности за любые недоразумения или неправильные толкования, возникшие в результате использования этого перевода.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->