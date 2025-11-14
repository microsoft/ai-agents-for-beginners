<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "11e38db0898a788612b917e329dcdb5b",
  "translation_date": "2025-11-07T08:23:58+00:00",
  "source_file": "00-course-setup/AzureSearch.md",
  "language_code": "ru"
}
-->
# Руководство по настройке Azure AI Search

Это руководство поможет вам настроить Azure AI Search через портал Azure. Следуйте приведенным ниже шагам, чтобы создать и настроить службу Azure AI Search.

## Предварительные требования

Перед началом убедитесь, что у вас есть следующее:

- Подписка на Azure. Если у вас нет подписки на Azure, вы можете создать бесплатный аккаунт на [Azure Free Account](https://azure.microsoft.com/free/?wt.mc_id=studentamb_258691).

## Шаг 1: Создание учетной записи хранилища Azure

1. Следуйте инструкции [Создание учетной записи хранилища Azure](https://learn.microsoft.com/azure/storage/common/storage-account-create?tabs=azure-portal), чтобы создать новую учетную запись хранилища Azure.  
   **NOTE**: Убедитесь, что тип учетной записи хранилища — Standard General Purpose V2.

## Шаг 2: Создание службы Azure AI Search

1. Войдите в [портал Azure](https://portal.azure.com/?wt.mc_id=studentamb_258691).
2. В левой панели навигации нажмите **Создать ресурс**.
3. В поле поиска введите "Azure AI Search" и выберите **Azure AI Search** из списка результатов.
4. Нажмите кнопку **Создать**.
5. На вкладке **Основные сведения** укажите следующую информацию:
   - **Подписка**: Выберите вашу подписку на Azure.
   - **Группа ресурсов**: Создайте новую группу ресурсов или выберите существующую.
   - **Имя ресурса**: Введите уникальное имя для вашей службы поиска.
   - **Регион**: Выберите регион, ближайший к вашим пользователям.
   - **Уровень цен**: Выберите уровень цен, который соответствует вашим требованиям. Для тестирования можно начать с бесплатного уровня.
6. Нажмите **Проверить и создать**.
7. Проверьте настройки и нажмите **Создать**, чтобы создать службу поиска.

## Шаг 3: Начало работы с Azure AI Search

1. После завершения развертывания перейдите к вашей службе поиска в портале Azure.
2. В панели обзора службы поиска скопируйте URL. Он должен выглядеть как `https://<service-name>.search.windows.net`.
3. В разделе Настройки > Ключи скопируйте ключ запроса.
4. Следуйте шагам на странице [Руководство по быстрому старту](https://learn.microsoft.com/azure/search/search-get-started-portal?pivots=import-data-new), чтобы создать индекс, загрузить данные и выполнить поисковый запрос.

## Шаг 4: Использование инструментов Azure AI Search

Azure AI Search интегрируется с различными инструментами для улучшения возможностей поиска. Вы можете использовать Azure CLI, Python SDK, .NET SDK и другие инструменты для расширенной настройки и операций.

### Использование Azure CLI

1. Установите Azure CLI, следуя инструкции [Установка Azure CLI](https://learn.microsoft.com/cli/azure/install-azure-cli?wt.mc_id=studentamb_258691).
2. Войдите в Azure CLI, используя команду:

   ```bash
   az login
   ```

3. Сохраните как endpoint, так и API-ключ для экземпляра Azure AI Search в переменные окружения.

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

### Использование Python SDK

1. Установите клиентскую библиотеку Azure Cognitive Search для Python:

   ```bash
   pip install azure-search-documents
   ```

2. Используйте следующий код на Python для создания индекса и загрузки документов:

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

### Использование .NET SDK

1. Выполните следующую команду для создания индекса и загрузки документов:

    ```bash
    dotnet run ./AzureSearch.cs
    ```

2. Вот код на .NET для `AzureSearch.cs`:

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

Для получения более подробной информации обратитесь к следующей документации:

- [Создание службы Azure Cognitive Search](https://learn.microsoft.com/azure/search/search-create-service-portal?wt.mc_id=studentamb_258691)
- [Начало работы с Azure Cognitive Search](https://learn.microsoft.com/azure/search/search-get-started-portal?wt.mc_id=studentamb_258691)
- [Инструменты Azure AI Search](https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-ai-search?tabs=azurecli%2Cpython&pivots=code-examples?wt.mc_id=studentamb_258691)

## Заключение

Вы успешно настроили Azure AI Search через портал Azure и интегрированные инструменты. Теперь вы можете изучить более продвинутые функции и возможности Azure AI Search для улучшения ваших поисковых решений.

Для получения дополнительной помощи посетите [документацию Azure Cognitive Search](https://learn.microsoft.com/azure/search/?wt.mc_id=studentamb_258691).

---

**Отказ от ответственности**:  
Этот документ был переведен с использованием сервиса автоматического перевода [Co-op Translator](https://github.com/Azure/co-op-translator). Несмотря на наши усилия обеспечить точность, автоматические переводы могут содержать ошибки или неточности. Оригинальный документ на его родном языке следует считать авторитетным источником. Для получения критически важной информации рекомендуется профессиональный перевод человеком. Мы не несем ответственности за любые недоразумения или неправильные интерпретации, возникающие в результате использования данного перевода.