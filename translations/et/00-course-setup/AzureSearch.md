# Azure AI Search seadistamise juhend

See juhend aitab sul seadistada Azure AI Searchi Azure portaalis. Järgi alltoodud samme, et luua ja konfigureerida oma Azure AI Search teenus.

## Eeltingimused

Enne alustamist veendu, et sul oleks olemas järgmised asjad:

- Azure tellimus. Kui sul pole Azure tellimust, saad tasuta konto luua aadressil [Azure Free Account](https://azure.microsoft.com/free/?wt.mc_id=studentamb_258691).

## Samm 1: Loo Azure Storage konto

1. Järgi juhist, [Create an Azure storage account](https://learn.microsoft.com/azure/storage/common/storage-account-create?tabs=azure-portal), et luua uus Azure Storage konto.
   **MÄRKUS**: Veendu, et Storage konto tüüp on Standard General Purpose V2.

## Samm 2: Loo Azure AI Search teenus

1. Logi sisse [Azure portaalis](https://portal.azure.com/?wt.mc_id=studentamb_258691).
2. Vasaku navigeerimispaneeli menüüs klõpsa **Create a resource**.
3. Otsi tekstikastis "Azure AI Search" ja vali tulemuste seast **Azure AI Search**.
4. Klõpsa nuppu **Create**.
5. Vahekaardil **Basics** esita järgmine info:
   - **Subscription**: Vali oma Azure tellimus.
   - **Resource group**: Loo uus või vali olemasolev ressursirühm.
   - **Resource name**: Sisesta otsimisteenuse ainulaadne nimi.
   - **Region**: Vali kasutajatele lähim piirkond.
   - **Pricing tier**: Vali hinnaklass vastavalt vajadusele. Katsetamiseks võid alustada tasuta paketist.
6. Klõpsa **Review + create**.
7. Vaata üle seaded ja klõpsa **Create**, et teenus luua.

## Samm 3: Azure AI Search kasutuselevõtt

1. Pärast juurutamise lõpetamist liigu Azure portaalis oma otsimisteenuse lehele.
2. Otsimisteenuse ülevaate paneelil kopeeri URL. See peaks välja nägema nagu `https://<service-name>.search.windows.net`.
3. **(Soovitatav)** Luba ilma võtit kasutamata ligipääs Microsoft Entra ID-ga (RBAC), nagu näidatud samm 4 allpool — võtit pole vaja. Sellised näited nagu selles juhendis loovad/täiustavad indekseid ja laadivad üles dokumente, mis nõuavad rolle **Search Service Contributor** ja **Search Index Data Contributor** (või võtmetega autentimisel **esmane admin võtme** — mitte päringuvõtit). Ainult juhul, kui sa ei saa RBAC-i kasutada, ava **Settings > Keys** paneel ja kopeeri **esmane admin võti**.
4. Järgi [Kiire alguse juhendi](https://learn.microsoft.com/azure/search/search-get-started-portal?pivots=import-data-new) samme, et luua indeks, üles laadida andmeid ja otsinguid teha.

## Samm 4: Kasuta Azure AI Search tööriistu

Azure AI Search integreerub mitmete tööriistadega, et täiustada otsinguvõimalusi. Sa saad kasutada Azure CLI, Python SDK, .NET SDK ja teisi tööriistu edasise konfiguratsiooni ja operatsioonide jaoks.

### Azure CLI kasutamine

1. Paigalda Azure CLI, järgides juhiseid aadressil [Install Azure CLI](https://learn.microsoft.com/cli/azure/install-azure-cli?wt.mc_id=studentamb_258691).
2. Logi Azure CLI sisse käsuga:

   ```bash
   az login
   ```
3. **(Soovitatav) Võtmeta ligipääsu lubamine Microsoft Entra ID-ga (RBAC):**

    ```bash
    az search service update --name <service-name> --resource-group <resource-group> --auth-options aadOrApiKey
    az role assignment create --assignee <your-user-or-principal-id> --role "Search Service Contributor" --scope $(az search service show -g <resource-group> -n <service-name> --query id -o tsv)
    az role assignment create --assignee <your-user-or-principal-id> --role "Search Index Data Contributor" --scope $(az search service show -g <resource-group> -n <service-name> --query id -o tsv)
    # az search service show has no "endpoint" field; build the URL from the service name.
    export AZURE_SEARCH_SERVICE_ENDPOINT="https://<service-name>.search.windows.net"
    ```

    RBAC lubamisega autentivad allolevad Python ja .NET SDK näited `DefaultAzureCredential` abil, mis kasutab sinu `az login` sessiooni kohaliku arendamise ajal — admin võtme vajadus puudub. Vaata lähemalt [Connect to Azure AI Search using roles](https://learn.microsoft.com/azure/search/search-security-rbac).

4. **(Varuplaan) Võtmega autentimine** — ainult juhul, kui sa ei saa RBAC-i kasutada, salvesta admin võti ka:

#### Salvesta nii lõpp-punkt kui ka API võti Azure AI Searchi näite jaoks keskkonnamuutujatesse.

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

### Python SDK kasutamine

1. Paigalda Azure Cognitive Search klienditeek ja Azure Identity Pythonile:

   ```bash
   pip install azure-search-documents azure-identity
   ```

2. Kasuta järgmist Python koodi indeksi loomiseks ja dokumentide üleslaadimiseks:

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

### .NET SDK kasutamine

1. Käivita järgmine käsk indeksi loomiseks ja dokumentide üleslaadimiseks:

    ```bash
    dotnet run ./AzureSearch.cs
    ```

    Allpool olev .NET näide kasutab `DefaultAzureCredential`, mis saab kasutada sinu Azure CLI sisselogimist aadressilt `az login` kohaliku arendamise ajal.

2. Siin on `AzureSearch.cs` .NET kood:

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

Täpsema info saamiseks vaata järgmist dokumentatsiooni:

- [Create an Azure Cognitive Search service](https://learn.microsoft.com/azure/search/search-create-service-portal?wt.mc_id=studentamb_258691)
- [Get started with Azure Cognitive Search](https://learn.microsoft.com/azure/search/search-get-started-portal?wt.mc_id=studentamb_258691)
- [Azure AI Search Tools](https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-ai-search?tabs=azurecli%2Cpython&pivots=code-examples?wt.mc_id=studentamb_258691)

## Kokkuvõte

Oled edukalt seadistanud Azure AI Searchi Azure portaali ja integreeritud tööriistade abil. Nüüd saad uurida Azure AI Searchi edasisi funktsioone ja võimalusi, et täiustada oma otsingulahendusi.

Lisatuge saamiseks külasta [Azure Cognitive Search dokumentatsiooni](https://learn.microsoft.com/azure/search/?wt.mc_id=studentamb_258691).

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Lahtiütlus**:
See dokument on tõlgitud kasutades AI tõlketeenust [Co-op Translator](https://github.com/Azure/co-op-translator). Kuigi me püüdleme täpsuse poole, palun pange tähele, et automatiseeritud tõlgetes võib esineda vigu või ebatäpsusi. Originaaldokument selle emakeeles tuleks pidada autoriteetseks allikaks. Olulise teabe puhul soovitatakse kasutada professionaalset inimtõlget. Me ei vastuta selle tõlkega seotud eksimustest või valesti mõistmistest.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->