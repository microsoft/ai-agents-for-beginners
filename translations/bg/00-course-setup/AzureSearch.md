# Ръководство за настройка на Azure AI Search

Това ръководство ще ви помогне да настроите Azure AI Search чрез портала на Azure. Следвайте стъпките по-долу, за да създадете и конфигурирате вашата услуга Azure AI Search.

## Предварителни изисквания

Преди да започнете, уверете се, че имате следното:

- Абонамент за Azure. Ако нямате абонамент за Azure, можете да създадете безплатен акаунт на [Azure Free Account](https://azure.microsoft.com/free/?wt.mc_id=studentamb_258691).

## Стъпка 1: Създаване на Azure Storage акаунт

1. Следвайте това указание, [Create an Azure storage account](https://learn.microsoft.com/azure/storage/common/storage-account-create?tabs=azure-portal), за да създадете нов Azure Storage акаунт.
   **ЗАБЕЛЕЖКА**: Уверете се, че типът на Storage акаунта е Standard General Purpose V2.

## Стъпка 2: Създаване на Azure AI Search услуга

1. Влезте в [Azure портала](https://portal.azure.com/?wt.mc_id=studentamb_258691).
2. В лявото навигационно меню кликнете върху **Create a resource**.
3. В полето за търсене въведете "Azure AI Search" и изберете **Azure AI Search** от списъка с резултати.
4. Кликнете върху бутона **Create**.
5. В раздела **Basics** посочете следната информация:
   - **Subscription**: Изберете вашия абонамент за Azure.
   - **Resource group**: Създайте нова ресурсна група или изберете съществуваща.
   - **Resource name**: Въведете уникално име за вашата услуга за търсене.
   - **Region**: Изберете региона, най-близък до вашите потребители.
   - **Pricing tier**: Изберете ниво на ценообразуване, което отговаря на вашите нужди. Можете да започнете с безплатното ниво за тестване.
6. Кликнете върху **Review + create**.
7. Прегледайте настройките и кликнете върху **Create**, за да създадете услугата за търсене.

## Стъпка 3: Започнете с Azure AI Search

1. След като разгръщането приключи, отидете до вашата услуга за търсене в Azure портала.
2. В страницата с общ преглед на услугата за търсене копирайте URL адреса. Той трябва да изглежда като `https://<service-name>.search.windows.net`.
3. **(Препоръчително)** Активирайте достъп без ключ чрез Microsoft Entra ID (RBAC), както е показано в Стъпка 4 по-долу — не е нужен ключ. Примерите в това ръководство създават/актуализират индекси и качват документи, което изисква ролите **Search Service Contributor** и **Search Index Data Contributor** (или, при автентикация с ключ, **първичния администраторски ключ** — не ключът за заявки). Само ако не можете да използвате RBAC, отворете панела **Settings > Keys** и копирайте **първичния администраторски ключ**.
4. Следвайте стъпките в [Quickstart guide](https://learn.microsoft.com/azure/search/search-get-started-portal?pivots=import-data-new) за създаване на индекс, качване на данни и извършване на търсене.

## Стъпка 4: Използване на инструментите на Azure AI Search

Azure AI Search се интегрира с различни инструменти за подобряване на вашите възможности за търсене. Можете да използвате Azure CLI, Python SDK, .NET SDK и други инструменти за разширена конфигурация и операции.

### Използване на Azure CLI

1. Инсталирайте Azure CLI като следвате инструкциите на [Install Azure CLI](https://learn.microsoft.com/cli/azure/install-azure-cli?wt.mc_id=studentamb_258691).
2. Влезте в Azure CLI, като използвате командата:

   ```bash
   az login
   ```
3. **(Препоръчително) Активирайте достъп без ключ чрез Microsoft Entra ID (RBAC):**

    ```bash
    az search service update --name <service-name> --resource-group <resource-group> --auth-options aadOrApiKey
    az role assignment create --assignee <your-user-or-principal-id> --role "Search Service Contributor" --scope $(az search service show -g <resource-group> -n <service-name> --query id -o tsv)
    az role assignment create --assignee <your-user-or-principal-id> --role "Search Index Data Contributor" --scope $(az search service show -g <resource-group> -n <service-name> --query id -o tsv)
    # Услугата az search show няма поле "endpoint"; изградете URL от името на услугата.
    export AZURE_SEARCH_SERVICE_ENDPOINT="https://<service-name>.search.windows.net"
    ```

    С RBAC активиран, примерите с Python и .NET SDK по-долу се удостоверяват с `DefaultAzureCredential`, който използва вашата сесия `az login` по време на локална разработка — не е нужен администраторски ключ. Вижте [Connect to Azure AI Search using roles](https://learn.microsoft.com/azure/search/search-security-rbac).

4. **(Резервно решение) Автентикация с ключ** — само ако не можете да използвате RBAC, съхранявайте и администраторския ключ:

#### Запишете както крайна точка, така и API ключ за Azure AI Search инстанция в променливи на средата.

    ```bash
    # zsh/bash
    # az search service show няма поле "endpoint"; създайте URL от името на услугата.
    export AZURE_SEARCH_SERVICE_ENDPOINT="https://<service-name>.search.windows.net"
    export AZURE_SEARCH_API_KEY=$(az search admin-key show -g <resource-group> --service-name <service-name> --query "primaryKey" -o tsv)
    ```

    ```powershell
    # PowerShell
    # az search service show няма поле "endpoint"; създайте URL от името на услугата.
    $env:AZURE_SEARCH_SERVICE_ENDPOINT = "https://<service-name>.search.windows.net"
    $env:AZURE_SEARCH_API_KEY = $(az search admin-key show -g <resource-group> --service-name <service-name> --query "primaryKey" -o tsv)
    ```

### Използване на Python SDK

1. Инсталирайте клиентската библиотека Azure Cognitive Search и Azure Identity за Python:

   ```bash
   pip install azure-search-documents azure-identity
   ```

2. Използвайте следния Python код за създаване на индекс и качване на документи:

    ```python
    import os
    from azure.identity import DefaultAzureCredential
    from azure.search.documents import SearchClient
    from azure.search.documents.indexes import SearchIndexClient
    from azure.search.documents.indexes.models import SearchIndex, SimpleField, edm

    service_endpoint = os.getenv("AZURE_SEARCH_SERVICE_ENDPOINT")
    index_name = "sample-index"

    # Без ключ (препоръчително): използва вашата идентичност от `az login` чрез Entra ID RBAC.
    # Изисква ролите "Search Service Contributor" и "Search Index Data Contributor".
    credential = DefaultAzureCredential()
    # Резервен вариант (автентикация с ключ):
    # от azure.core.credentials импортирайте AzureKeyCredential
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

### Използване на .NET SDK

1. Изпълнете следната команда, за да създадете индекс и да качите документи:

    ```bash
    dotnet run ./AzureSearch.cs
    ```

    Примерът с .NET по-долу използва `DefaultAzureCredential`, който може да използва вашето влизане в Azure CLI от `az login` по време на локалната разработка.

2. Ето .NET кода на `AzureSearch.cs`:

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

За по-подробна информация вижте следната документация:

- [Create an Azure Cognitive Search service](https://learn.microsoft.com/azure/search/search-create-service-portal?wt.mc_id=studentamb_258691)
- [Get started with Azure Cognitive Search](https://learn.microsoft.com/azure/search/search-get-started-portal?wt.mc_id=studentamb_258691)
- [Azure AI Search Tools](https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-ai-search?tabs=azurecli%2Cpython&pivots=code-examples?wt.mc_id=studentamb_258691)

## Заключение

Успешно сте настроили Azure AI Search чрез Azure портала и интегрираните инструменти. Сега можете да разгледате по-напредналите функции и възможности на Azure AI Search за подобряване на вашите решения за търсене.

За допълнителна помощ посетете [документацията на Azure Cognitive Search](https://learn.microsoft.com/azure/search/?wt.mc_id=studentamb_258691).

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Отказ от отговорност**:
Този документ е преведен с помощта на AI преводачески услуга [Co-op Translator](https://github.com/Azure/co-op-translator). Въпреки че се стремим към точност, моля имайте предвид, че автоматизираните преводи могат да съдържат грешки или неточности. Оригиналният документ на неговия роден език трябва да се счита за авторитетен източник. За критична информация се препоръчва професионален човешки превод. Ние не носим отговорност за каквито и да е недоразумения или неправилни тълкувания, произтичащи от използването на този превод.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->