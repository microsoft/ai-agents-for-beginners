# Водич за подешавање Azure AI претраге

Овај водич ће вам помоћи да подесите Azure AI претрагу користећи Azure портал. Пратите кораке у наставку да бисте креирали и конфигурисали вашу Azure AI претраживачку услугу.

## Претходни услови

Пре него што почнете, уверите се да имате следеће:

- Azure претплату. Ако немате Azure претплату, можете направити бесплатан налог на [Azure Free Account](https://azure.microsoft.com/free/?wt.mc_id=studentamb_258691).

## Корак 1: Креирајте Azure Storage налог

1. Пратите упутства, [Create an Azure storage account](https://learn.microsoft.com/azure/storage/common/storage-account-create?tabs=azure-portal), да бисте креирали нови Azure Storage налог.
   **НАПОМЕНА**: Уверите се да је тип Storage налога Standard General Purpose V2.

## Корак 2: Креирајте Azure AI претраживачку услугу

1. Пријавите се на [Azure портал](https://portal.azure.com/?wt.mc_id=studentamb_258691).
2. У левом навигационом панелу кликните на **Create a resource**.
3. У пољу за претрагу укуцајте "Azure AI Search" и изаберите **Azure AI Search** из резултата.
4. Кликните на дугме **Create**.
5. На картици **Basics** унесите следеће информације:
   - **Subscription**: Изаберите вашу Azure претплату.
   - **Resource group**: Креирајте нову ресурсну групу или изаберите постојећу.
   - **Resource name**: Унесите јединствено име за вашу претраживачку услугу.
   - **Region**: Изаберите регион најближи вашим корисницима.
   - **Pricing tier**: Изаберите ниво цене који одговара вашим захтевима. Можете почети са бесплатним слојем за тестирање.
6. Кликните **Review + create**.
7. Прегледајте подешавања и кликните **Create** да бисте креирали претраживачку услугу.

## Корак 3: Почните са Azure AI претрагом

1. Када се дистрибуција заврши, идите у вашу претраживачку услугу у Azure порталу.
2. На прозору са прегледом претраживача копирајте URL. Требало би да изгледа као `https://<service-name>.search.windows.net`.
3. **(Препоручено)** Омогућите приступ без кључа преко Microsoft Entra ID (RBAC) као што је приказано у Кораку 4 испод — није потребан кључ. Примери у овом водичу креирају/ажурирају индексе и отпремају документе, што захтева улоге **Search Service Contributor** и **Search Index Data Contributor** (или, за аутентификацију на основу кључа, **primary admin key** — не query key). Само ако не можете користити RBAC, отворите **Settings > Keys** и копирајте **primary admin key**.
4. Пратите кораке на [Quickstart guide](https://learn.microsoft.com/azure/search/search-get-started-portal?pivots=import-data-new) страници да бисте креирали индекс, отпремили податке и извршили претрагу.

## Корак 4: Користите Azure AI претраживачке алате

Azure AI претрага се интегрише са различитим алатима за побољшање ваших могућности претраге. Можете користити Azure CLI, Python SDK, .NET SDK и друге алате за напредне конфигурације и операције.

### Коришћење Azure CLI

1. Инсталирајте Azure CLI пратећи упутства на [Install Azure CLI](https://learn.microsoft.com/cli/azure/install-azure-cli?wt.mc_id=studentamb_258691).
2. Пријавите се у Azure CLI користећи команду:

   ```bash
   az login
   ```
3. **(Препоручено) Омогућите приступ без кључа преко Microsoft Entra ID (RBAC):**

    ```bash
    az search service update --name <service-name> --resource-group <resource-group> --auth-options aadOrApiKey
    az role assignment create --assignee <your-user-or-principal-id> --role "Search Service Contributor" --scope $(az search service show -g <resource-group> -n <service-name> --query id -o tsv)
    az role assignment create --assignee <your-user-or-principal-id> --role "Search Index Data Contributor" --scope $(az search service show -g <resource-group> -n <service-name> --query id -o tsv)
    # az search сервиса приказује да нема поље "endpoint"; саставите URL из имена сервиса.
    export AZURE_SEARCH_SERVICE_ENDPOINT="https://<service-name>.search.windows.net"
    ```

    Са омогућеним RBAC, Python и .NET SDK примери испод аутентификују се са `DefaultAzureCredential`, која користи вашу `az login` сесију током локалног развоја — није потребан админ кључ. Види [Connect to Azure AI Search using roles](https://learn.microsoft.com/azure/search/search-security-rbac).

4. **(Алтернативно) Аутентификација на основу кључа** — само ако не можете користити RBAC, сачувајте и админ кључ:

#### Сачувајте установађујући ендпоинт и API кључ Azure AI претраживања као променљиве окружења.

    ```bash
    # zsh/bash
    # az search service show нема поље "endpoint"; направите URL из имена услуге.
    export AZURE_SEARCH_SERVICE_ENDPOINT="https://<service-name>.search.windows.net"
    export AZURE_SEARCH_API_KEY=$(az search admin-key show -g <resource-group> --service-name <service-name> --query "primaryKey" -o tsv)
    ```

    ```powershell
    # PowerShell
    # az search service show нема поље "endpoint"; направите URL из имена услуге.
    $env:AZURE_SEARCH_SERVICE_ENDPOINT = "https://<service-name>.search.windows.net"
    $env:AZURE_SEARCH_API_KEY = $(az search admin-key show -g <resource-group> --service-name <service-name> --query "primaryKey" -o tsv)
    ```

### Коришћење Python SDK-а

1. Инсталирајте Azure Cognitive Search клијент библиотеку и Azure Identity за Python:

   ```bash
   pip install azure-search-documents azure-identity
   ```

2. Користите следећи Python код за креирање индекса и отпремање докумената:

    ```python
    import os
    from azure.identity import DefaultAzureCredential
    from azure.search.documents import SearchClient
    from azure.search.documents.indexes import SearchIndexClient
    from azure.search.documents.indexes.models import SearchIndex, SimpleField, edm

    service_endpoint = os.getenv("AZURE_SEARCH_SERVICE_ENDPOINT")
    index_name = "sample-index"

    # Без кључа (препоручено): користи ваш идентитет из `az login` преко Entra ID RBAC.
    # Захтева улоге "Search Service Contributor" и "Search Index Data Contributor".
    credential = DefaultAzureCredential()
    # Резервна опција (аутентификација заснована на кључу):
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

### Коришћење .NET SDK-а

1. Покрените следећу команду за креирање индекса и отпремање докумената:

    ```bash
    dotnet run ./AzureSearch.cs
    ```

    Испод наведени .NET пример користи `DefaultAzureCredential`, која може користити вашу Azure CLI пријаву из `az login` током локалног развоја.

2. Ево .NET кода из `AzureSearch.cs`:

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

Успешно сте подесили Azure AI претрагу користећи Azure портал и интегрисане алате. Сада можете истражити напредније функције и могућности Azure AI претраге да унапредите ваша претраживачка решења.

За даљу помоћ, посетите [Azure Cognitive Search документацију](https://learn.microsoft.com/azure/search/?wt.mc_id=studentamb_258691).

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Изјава о одрицању одговорности**:
Овај документ је преведен коришћењем услуге за аутоматски превод [Co-op Translator](https://github.com/Azure/co-op-translator). Иако тежимо тачности, имајте у виду да аутоматски преводи могу садржати грешке или нетачности. Оригинални документ на његовом изворном језику треба сматрати ауторитативним извором. За критичне информације препоручује се професионални људски превод. Нисмо одговорни за било каква неспоразума или погрешна тумачења која произилазе из коришћења овог превода.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->