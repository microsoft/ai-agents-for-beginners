# Водич за подешавање Azure AI претраге

Овај водич ће вам помоћи да подесите Azure AI претрагу користећи Azure портал. Следите кораке у наставку да бисте креирали и конфигурисали ваш Azure AI претраживачки сервис.

## Захтеви

Пре него што почнете, уверите се да имате следеће:

- Azure претплату. Ако немате Azure претплату, можете направити бесплатан налог на [Azure Free Account](https://azure.microsoft.com/free/?wt.mc_id=studentamb_258691).

## Корак 1: Креирајте Azure Storage налог

1. Пратите ова упутства, [Create an Azure storage account](https://learn.microsoft.com/azure/storage/common/storage-account-create?tabs=azure-portal), да бисте креирали нови Azure Storage налог.
   **НАПОМЕНА**: Обавезно изаберите тип Storage Account као Standard General Purpose V2.

## Корак 2: Креирајте Azure AI претраживачки сервис

1. Пријавите се у [Azure портал](https://portal.azure.com/?wt.mc_id=studentamb_258691).
2. У левом навигационом менију кликните на **Create a resource**.
3. У пољу за претрагу укуцајте "Azure AI Search" и изаберите **Azure AI Search** из листе резултата.
4. Кликните на дугме **Create**.
5. На картици **Basics**, унесите следеће информације:
   - **Subscription**: Изаберите вашу Azure претплату.
   - **Resource group**: Креирајте нову ресурсну групу или изаберите постојећу.
   - **Resource name**: Унесите јединствено име за ваш претраживачки сервис.
   - **Region**: Изаберите регију која је најближа вашим корисницима.
   - **Pricing tier**: Изаберите план цена који одговара вашим захтевима. Можете почети са бесплатним (Free) планом за тестирање.
6. Кликните **Review + create**.
7. Прегледајте подешавања и кликните **Create** да бисте креирали претраживачки сервис.

## Корак 3: Почетак рада са Azure AI претрагом

1. Када имплементација буде завршена, идите до вашег претраживачког сервиса у Azure порталу.
2. У прегледу сервиса копирајте URL адресу. Требало би да изгледа као `https://<service-name>.search.windows.net`.
3. **(Препоручено)** Омогућите приступ без кључа помоћу Microsoft Entra ID (RBAC) као што је приказано у кораку 4 испод — није потребан кључ. Примери у овом водичу креирају/ажурирају индексе и постављају документе, што захтева улоге **Search Service Contributor** и **Search Index Data Contributor** (или, за аутентификацију на основу кључа, **primary admin key** — а не query key). Само ако не можете да користите RBAC, отворите **Settings > Keys** и копирајте **primary admin key**.
4. Пратите кораке у [Quickstart guide](https://learn.microsoft.com/azure/search/search-get-started-portal?pivots=import-data-new) страници да бисте креирали индекс, поставили податке и извршили претрагу.

## Корак 4: Коришћење алата за Azure AI претрагу

Azure AI претрага се интегрише са различитим алатима за унапређење ваших претраживачких могућности. Можете користити Azure CLI, Python SDK, .NET SDK и друге алате за напредне конфигурације и операције.

### Коришћење Azure CLI

1. Инсталирајте Azure CLI пратећи упутства на [Install Azure CLI](https://learn.microsoft.com/cli/azure/install-azure-cli?wt.mc_id=studentamb_258691).
2. Пријавите се у Azure CLI користећи команду:

   ```bash
   az login
   ```
3. **(Препоручено) Омогућите приступ без кључа помоћу Microsoft Entra ID (RBAC):**

    ```bash
    az search service update --name <service-name> --resource-group <resource-group> --auth-options aadOrApiKey
    az role assignment create --assignee <your-user-or-principal-id> --role "Search Service Contributor" --scope $(az search service show -g <resource-group> -n <service-name> --query id -o tsv)
    az role assignment create --assignee <your-user-or-principal-id> --role "Search Index Data Contributor" --scope $(az search service show -g <resource-group> -n <service-name> --query id -o tsv)
    # az search service show has no "endpoint" field; build the URL from the service name.
    export AZURE_SEARCH_SERVICE_ENDPOINT="https://<service-name>.search.windows.net"
    ```

    Са омогућеним RBAC, примери у Python и .NET SDK доле се аутентификују помоћу `DefaultAzureCredential`, који користи вашу `az login` сесију током локалног развоја — није потребан администраторски кључ. Погледајте [Connect to Azure AI Search using roles](https://learn.microsoft.com/azure/search/search-security-rbac).

4. **(Резервно) Аутентификација на основу кључа** — само ако не можете да користите RBAC, сачувајте и администраторски кључ:

#### Сачувајте и крајњу тачку и API кључ за Azure AI претраживачки инстанс у променљиве окружења.

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

### Коришћење Python SDK

1. Инсталирајте библиотеку Azure Cognitive Search клијента и Azure Identity за Python:

   ```bash
   pip install azure-search-documents azure-identity
   ```

2. Користите следећи Python код да бисте креирали индекс и поставили документе:

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

### Коришћење .NET SDK

1. Покрените следећу команду да бисте креирали индекс и поставили документе:

    ```bash
    dotnet run ./AzureSearch.cs
    ```

    Пример за .NET испод користи `DefaultAzureCredential`, који може да користи вашу Azure CLI пријаву са `az login` током локалног развоја.

2. Ево .NET кода за `AzureSearch.cs`:

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

За детаљније информације, погледајте следећу документацију:

- [Create an Azure Cognitive Search service](https://learn.microsoft.com/azure/search/search-create-service-portal?wt.mc_id=studentamb_258691)
- [Get started with Azure Cognitive Search](https://learn.microsoft.com/azure/search/search-get-started-portal?wt.mc_id=studentamb_258691)
- [Azure AI Search Tools](https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-ai-search?tabs=azurecli%2Cpython&pivots=code-examples?wt.mc_id=studentamb_258691)

## Закључак

Успешно сте поставили Azure AI претрагу користећи Azure портал и интегрисане алате. Сада можете истражити напредније функције и могућности Azure AI претраге да побољшате ваша претраживачка решења.

За даљу помоћ, посетите [Azure Cognitive Search documentation](https://learn.microsoft.com/azure/search/?wt.mc_id=studentamb_258691).

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Изјава о одрицању одговорности**:
Овај документ је преведен коришћењем услуге за аутоматски превод [Co-op Translator](https://github.com/Azure/co-op-translator). Иако тежимо тачности, имајте у виду да аутоматски преводи могу садржати грешке или нетачности. Оригинални документ на његовом изворном језику треба сматрати ауторитативним извором. За критичне информације препоручује се професионални људски превод. Нисмо одговорни за било каква неспоразума или погрешна тумачења која произилазе из коришћења овог превода.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->