<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "11e38db0898a788612b917e329dcdb5b",
  "translation_date": "2025-11-07T08:48:48+00:00",
  "source_file": "00-course-setup/AzureSearch.md",
  "language_code": "bg"
}
-->
# Ръководство за настройка на Azure AI Search

Това ръководство ще ви помогне да настроите Azure AI Search чрез портала на Azure. Следвайте стъпките по-долу, за да създадете и конфигурирате вашата услуга Azure AI Search.

## Предпоставки

Преди да започнете, уверете се, че разполагате със следното:

- Абонамент за Azure. Ако нямате абонамент за Azure, можете да създадете безплатен акаунт на [Azure Free Account](https://azure.microsoft.com/free/?wt.mc_id=studentamb_258691).

## Стъпка 1: Създаване на акаунт за съхранение в Azure

1. Следвайте тези инструкции, [Създаване на акаунт за съхранение в Azure](https://learn.microsoft.com/azure/storage/common/storage-account-create?tabs=azure-portal), за да създадете нов акаунт за съхранение в Azure.  
   **NOTE**: Уверете се, че типът на акаунта за съхранение е Standard General Purpose V2.

## Стъпка 2: Създаване на услуга Azure AI Search

1. Влезте в [портала на Azure](https://portal.azure.com/?wt.mc_id=studentamb_258691).
2. В навигационния панел отляво кликнете върху **Create a resource**.
3. В полето за търсене въведете "Azure AI Search" и изберете **Azure AI Search** от списъка с резултати.
4. Кликнете върху бутона **Create**.
5. В раздела **Basics** предоставете следната информация:
   - **Subscription**: Изберете вашия абонамент за Azure.
   - **Resource group**: Създайте нова ресурсна група или изберете съществуваща.
   - **Resource name**: Въведете уникално име за вашата услуга за търсене.
   - **Region**: Изберете региона, който е най-близо до вашите потребители.
   - **Pricing tier**: Изберете ценови план, който отговаря на вашите изисквания. Можете да започнете с безплатния план за тестване.
6. Кликнете върху **Review + create**.
7. Прегледайте настройките и кликнете върху **Create**, за да създадете услугата за търсене.

## Стъпка 3: Започнете работа с Azure AI Search

1. След като разгръщането приключи, отидете на вашата услуга за търсене в портала на Azure.
2. В панела за преглед на услугата за търсене копирайте URL адреса. Той трябва да изглежда като `https://<service-name>.search.windows.net`.
3. В раздела Settings > Keys копирайте ключа за заявки.
4. Следвайте стъпките на страницата [Ръководство за бърз старт](https://learn.microsoft.com/azure/search/search-get-started-portal?pivots=import-data-new), за да създадете индекс, качите данни и изпълните заявка за търсене.

## Стъпка 4: Използване на инструменти за Azure AI Search

Azure AI Search се интегрира с различни инструменти за подобряване на вашите възможности за търсене. Можете да използвате Azure CLI, Python SDK, .NET SDK и други инструменти за разширени конфигурации и операции.

### Използване на Azure CLI

1. Инсталирайте Azure CLI, като следвате инструкциите на [Инсталиране на Azure CLI](https://learn.microsoft.com/cli/azure/install-azure-cli?wt.mc_id=studentamb_258691).
2. Влезте в Azure CLI, използвайки командата:

   ```bash
   az login
   ```

3. Съхранете както крайния точка, така и API ключа за инстанцията на Azure AI Search в променливи на средата.

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

### Използване на Python SDK

1. Инсталирайте клиентската библиотека за Azure Cognitive Search за Python:

   ```bash
   pip install azure-search-documents
   ```

2. Използвайте следния Python код, за да създадете индекс и качите документи:

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

### Използване на .NET SDK

1. Изпълнете следната команда, за да създадете индекс и качите документи:

    ```bash
    dotnet run ./AzureSearch.cs
    ```

2. Ето .NET кода на `AzureSearch.cs`:

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

За по-подробна информация, вижте следната документация:

- [Създаване на услуга Azure Cognitive Search](https://learn.microsoft.com/azure/search/search-create-service-portal?wt.mc_id=studentamb_258691)
- [Започнете работа с Azure Cognitive Search](https://learn.microsoft.com/azure/search/search-get-started-portal?wt.mc_id=studentamb_258691)
- [Инструменти за Azure AI Search](https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-ai-search?tabs=azurecli%2Cpython&pivots=code-examples?wt.mc_id=studentamb_258691)

## Заключение

Вие успешно настроихте Azure AI Search чрез портала на Azure и интегрираните инструменти. Сега можете да изследвате по-напреднали функции и възможности на Azure AI Search, за да подобрите вашите решения за търсене.

За допълнителна помощ посетете [документацията за Azure Cognitive Search](https://learn.microsoft.com/azure/search/?wt.mc_id=studentamb_258691).

---

**Отказ от отговорност**:  
Този документ е преведен с помощта на AI услуга за превод [Co-op Translator](https://github.com/Azure/co-op-translator). Въпреки че се стремим към точност, моля, имайте предвид, че автоматизираните преводи може да съдържат грешки или неточности. Оригиналният документ на неговия роден език трябва да се счита за авторитетен източник. За критична информация се препоръчва професионален човешки превод. Ние не носим отговорност за каквито и да е недоразумения или погрешни интерпретации, произтичащи от използването на този превод.