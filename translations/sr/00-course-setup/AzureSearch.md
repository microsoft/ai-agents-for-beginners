<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "11e38db0898a788612b917e329dcdb5b",
  "translation_date": "2025-11-07T08:49:33+00:00",
  "source_file": "00-course-setup/AzureSearch.md",
  "language_code": "sr"
}
-->
# Водич за подешавање Azure AI Search

Овај водич ће вам помоћи да подесите Azure AI Search користећи Azure портал. Пратите кораке испод да бисте креирали и конфигурисали вашу Azure AI Search услугу.

## Предуслови

Пре него што почнете, уверите се да имате следеће:

- Azure претплату. Ако немате Azure претплату, можете креирати бесплатан налог на [Azure Free Account](https://azure.microsoft.com/free/?wt.mc_id=studentamb_258691).

## Корак 1: Креирање Azure Storage налога

1. Пратите упутства [Креирање Azure Storage налога](https://learn.microsoft.com/azure/storage/common/storage-account-create?tabs=azure-portal) да бисте креирали нови Azure Storage налог.  
   **NOTE**: Уверите се да је тип Storage налога Standard General Purpose V2.

## Корак 2: Креирање Azure AI Search услуге

1. Пријавите се на [Azure портал](https://portal.azure.com/?wt.mc_id=studentamb_258691).
2. У левом навигационом панелу кликните на **Create a resource**.
3. У пољу за претрагу укуцајте "Azure AI Search" и изаберите **Azure AI Search** из листе резултата.
4. Кликните на дугме **Create**.
5. У картици **Basics**, наведите следеће информације:
   - **Subscription**: Изаберите вашу Azure претплату.
   - **Resource group**: Креирајте нову групу ресурса или изаберите постојећу.
   - **Resource name**: Унесите јединствено име за вашу услугу претраге.
   - **Region**: Изаберите регион најближи вашим корисницима.
   - **Pricing tier**: Изаберите ниво цена који одговара вашим потребама. Можете почети са бесплатним нивоом за тестирање.
6. Кликните на **Review + create**.
7. Прегледајте подешавања и кликните на **Create** да бисте креирали услугу претраге.

## Корак 3: Почетак рада са Azure AI Search

1. Када се распоређивање заврши, идите на вашу услугу претраге у Azure порталу.
2. У панелу прегледа услуге претраге, копирајте URL. Требало би да изгледа овако: `https://<service-name>.search.windows.net`.
3. У картици Settings > Keys, копирајте кључ за упите.
4. Пратите кораке на страници [Quickstart guide](https://learn.microsoft.com/azure/search/search-get-started-portal?pivots=import-data-new) да бисте креирали индекс, отпремили податке и извршили упит претраге.

## Корак 4: Коришћење алата Azure AI Search

Azure AI Search се интегрише са различитим алатима за побољшање ваших могућности претраге. Можете користити Azure CLI, Python SDK, .NET SDK и друге алате за напредне конфигурације и операције.

### Коришћење Azure CLI

1. Инсталирајте Azure CLI пратећи упутства на [Install Azure CLI](https://learn.microsoft.com/cli/azure/install-azure-cli?wt.mc_id=studentamb_258691).
2. Пријавите се на Azure CLI користећи команду:

   ```bash
   az login
   ```

3. Сачувајте и крајњу тачку и API кључ за Azure AI Search инстанцу у променљиве окружења.

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

### Коришћење Python SDK

1. Инсталирајте библиотеку клијента Azure Cognitive Search за Python:

   ```bash
   pip install azure-search-documents
   ```

2. Користите следећи Python код за креирање индекса и отпремање докумената:

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

### Коришћење .NET SDK

1. Покрените следећу команду за креирање индекса и отпремање докумената:

    ```bash
    dotnet run ./AzureSearch.cs
    ```

2. Ево .NET кода за `AzureSearch.cs`:

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

За више детаљних информација, погледајте следећу документацију:

- [Креирање Azure Cognitive Search услуге](https://learn.microsoft.com/azure/search/search-create-service-portal?wt.mc_id=studentamb_258691)
- [Почетак рада са Azure Cognitive Search](https://learn.microsoft.com/azure/search/search-get-started-portal?wt.mc_id=studentamb_258691)
- [Azure AI Search алати](https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-ai-search?tabs=azurecli%2Cpython&pivots=code-examples?wt.mc_id=studentamb_258691)

## Закључак

Успешно сте подесили Azure AI Search користећи Azure портал и интегрисане алате. Сада можете истраживати напредније функције и могућности Azure AI Search за побољшање ваших решења за претрагу.

За додатну помоћ, посетите [Azure Cognitive Search документацију](https://learn.microsoft.com/azure/search/?wt.mc_id=studentamb_258691).

---

**Одрицање од одговорности**:  
Овај документ је преведен помоћу услуге за превођење вештачке интелигенције [Co-op Translator](https://github.com/Azure/co-op-translator). Иако настојимо да обезбедимо тачност, молимо вас да имате у виду да аутоматски преводи могу садржати грешке или нетачности. Оригинални документ на његовом изворном језику треба сматрати ауторитативним извором. За критичне информације препоручује се професионални превод од стране људи. Не преузимамо одговорност за било каква погрешна тумачења или неспоразуме који могу настати услед коришћења овог превода.