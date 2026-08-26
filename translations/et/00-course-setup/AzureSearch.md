# Azure AI Search seadistusjuhend

See juhend aitab teil seadistada Azure AI Searchi, kasutades Azure portaali. Järgige alltoodud samme, et luua ja konfigureerida oma Azure AI Search teenust.

## Nõuded

Enne alustamist veenduge, et teil on järgmised tingimused täidetud:

- Azure tellimus. Kui teil pole Azure tellimust, saate luua tasuta konto aadressil [Azure Free Account](https://azure.microsoft.com/free/?wt.mc_id=studentamb_258691).

## 1. samm: Loo Azure Storage konto

1. Järgige seda juhist, [Create an Azure storage account](https://learn.microsoft.com/azure/storage/common/storage-account-create?tabs=azure-portal), et luua uus Azure Storage konto.
   **MÄRKUS**: Veenduge, et Storage konto tüüp on Standard General Purpose V2.

## 2. samm: Loo Azure AI Search teenus

1. Logi sisse [Azure portaalis](https://portal.azure.com/?wt.mc_id=studentamb_258691).
2. Vasakpoolsel navigeerimispaanil klõpsake **Loo ressurss**.
3. Otsingukastis tippige "Azure AI Search" ja valige tulemuste hulgast **Azure AI Search**.
4. Klõpsake **Loo** nuppu.
5. Vahekaardil **Põhitõed** täitke järgmine info:
   - **Tellimus**: Valige oma Azure tellimus.
   - **Ressursirühm**: Looge uus ressursirühm või valige olemasolev.
   - **Ressursi nimi**: Sisestage otsinguteenuse unikaalne nimi.
   - **Regioon**: Valige regioon, mis on kasutajatele kõige lähemal.
   - **Hindamistasand**: Valige hinnaklass, mis vastab teie vajadustele. Testimiseks võite alustada tasuta tasemega.
6. Klõpsake **Kinnita ja loo**.
7. Kontrollige seadeid ja klõpsake **Loo**, et otsinguteenuse luua.

## 3. samm: Azure AI Search kasutuselevõtt

1. Pärast juurutamise lõppu minge Azure portaalis oma otsinguteenuse juurde.
2. Otsinguteenuse ülevaate paneelis kopeerige URL. See peaks välja nägema nagu `https://<service-name>.search.windows.net`.
3. **(Soovitatav)** Lülitage sisse võtmeteta juurdepääs Microsoft Entra ID-ga (RBAC) alloleva 4. sammuga — võtme kasutamine pole vajalik. Selle juhendi näited loovad/värskendavad indekseid ja laadivad üles dokumente, mille jaoks on vajalikud rollid **Search Service Contributor** ja **Search Index Data Contributor** (või võtmel põhineva autentimise puhul **esmane haldusvõti** — mitte päringuvõti). Ainult kui RBAC-i kasutada ei saa, avage **Seaded > Võtmed** paneel ja kopeerige **esmane haldusvõti**.
4. Järgige [Kiirstartu juhendis](https://learn.microsoft.com/azure/search/search-get-started-portal?pivots=import-data-new) toodud samme, et luua indeks, laadida andmeid ja teostada otsing.

## 4. samm: Kasutage Azure AI Search tööriistu

Azure AI Search integreerub erinevate tööriistadega, et täiustada teie otsinguvõimalusi. Võite kasutada Azure CLI-d, Python SDK-d, .NET SDK-d ja teisi tööriistu keerukamaks seadistuseks ja toiminguteks.

### Azure CLI kasutamine

1. Installige Azure CLI, järgides juhiseid lehel [Install Azure CLI](https://learn.microsoft.com/cli/azure/install-azure-cli?wt.mc_id=studentamb_258691).
2. Logige Azure CLI-sse sisse käsuga:

   ```bash
   az login
   ```
3. **(Soovitatav) Lülitage sisse võtmeteta juurdepääs Microsoft Entra ID-ga (RBAC):**

    ```bash
    az search service update --name <service-name> --resource-group <resource-group> --auth-options aadOrApiKey
    az role assignment create --assignee <your-user-or-principal-id> --role "Search Service Contributor" --scope $(az search service show -g <resource-group> -n <service-name> --query id -o tsv)
    az role assignment create --assignee <your-user-or-principal-id> --role "Search Index Data Contributor" --scope $(az search service show -g <resource-group> -n <service-name> --query id -o tsv)
    # az search teenuse näitamisel pole "endpoint" välja; loo URL teenuse nime põhjal.
    export AZURE_SEARCH_SERVICE_ENDPOINT="https://<service-name>.search.windows.net"
    ```

    RBAC sisselülitamisel autentivad allolevad Python ja .NET SDK näited `DefaultAzureCredential` abil, mis kasutab teie `az login` seanssi lokaalsel arendamisel — haldusvõtit pole vaja. Lisateavet leiate siit: [Connect to Azure AI Search using roles](https://learn.microsoft.com/azure/search/search-security-rbac).

4. **(Varuvariant) Võtmel põhinev autentimine** — ainult juhul, kui RBAC-i kasutada ei saa, salvestage ka haldusvõti:

#### Salvestage nii lõpp-punkt kui ka API võti Azure AI Search eksemplari keskkonnamuutujatesse.

    ```bash
    # zsh/bash
    # az search service show ei sisalda "endpoint" välja; koostage URL teenuse nime põhjal.
    export AZURE_SEARCH_SERVICE_ENDPOINT="https://<service-name>.search.windows.net"
    export AZURE_SEARCH_API_KEY=$(az search admin-key show -g <resource-group> --service-name <service-name> --query "primaryKey" -o tsv)
    ```

    ```powershell
    # PowerShell
    # az search service show ei sisalda "endpoint" välja; koostage URL teenuse nime põhjal.
    $env:AZURE_SEARCH_SERVICE_ENDPOINT = "https://<service-name>.search.windows.net"
    $env:AZURE_SEARCH_API_KEY = $(az search admin-key show -g <resource-group> --service-name <service-name> --query "primaryKey" -o tsv)
    ```

### Python SDK kasutamine

1. Installige Azure Cognitive Search klienditeek ja Azure Identity Pythonile:

   ```bash
   pip install azure-search-documents azure-identity
   ```

2. Kasutage järgmist Python koodi indeksi loomiseks ja dokumentide üleslaadimiseks:

    ```python
    import os
    from azure.identity import DefaultAzureCredential
    from azure.search.documents import SearchClient
    from azure.search.documents.indexes import SearchIndexClient
    from azure.search.documents.indexes.models import SearchIndex, SimpleField, edm

    service_endpoint = os.getenv("AZURE_SEARCH_SERVICE_ENDPOINT")
    index_name = "sample-index"

    # Võtmeta (soovitatav): kasutab teie `az login` identiteeti läbi Entra ID RBAC.
    # Nõuab "Search Service Contributor" ja "Search Index Data Contributor" rolle.
    credential = DefaultAzureCredential()
    # Tagasiheide (võtme-põhine autentimine):
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

1. Käivitage järgmine käsk indeksi loomiseks ja dokumentide üleslaadimiseks:

    ```bash
    dotnet run ./AzureSearch.cs
    ```

    Allolev .NET näide kasutab `DefaultAzureCredential`, mis võib kasutada teie Azure CLI sisselogimist `az login` kaudu lokaalsel arendamisel.

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

Täpsema info saamiseks vaadake järgmisi dokumente:

- [Loo Azure Cognitive Search teenus](https://learn.microsoft.com/azure/search/search-create-service-portal?wt.mc_id=studentamb_258691)
- [Alustage Azure Cognitive Search kasutamist](https://learn.microsoft.com/azure/search/search-get-started-portal?wt.mc_id=studentamb_258691)
- [Azure AI Search tööriistad](https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-ai-search?tabs=azurecli%2Cpython&pivots=code-examples?wt.mc_id=studentamb_258691)

## Kokkuvõte

Olete edukalt seadistanud Azure AI Searchi Azure portaali kaudu ja integreerinud tööriistad. Nüüd saate avastada Azure AI Searchi täiustatud funktsioone ja võimalusi, et täiustada oma otsingulahendusi.

Lisatuge leiate [Azure Cognitive Search dokumentatsioonist](https://learn.microsoft.com/azure/search/?wt.mc_id=studentamb_258691).

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Lahtiütlus**:
See dokument on tõlgitud kasutades AI tõlketeenust [Co-op Translator](https://github.com/Azure/co-op-translator). Kuigi me püüdleme täpsuse poole, palun pange tähele, et automatiseeritud tõlgetes võib esineda vigu või ebatäpsusi. Originaaldokument selle emakeeles tuleks pidada autoriteetseks allikaks. Olulise teabe puhul soovitatakse kasutada professionaalset inimtõlget. Me ei vastuta selle tõlkega seotud eksimustest või valesti mõistmistest.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->