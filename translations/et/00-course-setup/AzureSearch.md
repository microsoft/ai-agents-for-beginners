# Azure AI Search seadistamise juhend

See juhend aitab teil seadistada Azure AI Search teenust Azure portaali kasutades. Järgige alltoodud samme, et luua ja konfigureerida oma Azure AI Search teenust.

## Nõuded

Enne alustamist veenduge, et teil on olemas järgmised:

- Azure tellimus. Kui teil ei ole Azure tellimust, saate luua tasuta konto aadressil [Azure Free Account](https://azure.microsoft.com/free/?wt.mc_id=studentamb_258691).

## 1. samm: Azure salvestuskonto loomine

1. Järgige seda juhist, [Loo Azure salvestuskonto](https://learn.microsoft.com/azure/storage/common/storage-account-create?tabs=azure-portal), et luua uus Azure salvestuskonto.
   **MÄRKUS**: Veenduge, et salvestuskonto tüübiks on Standard General Purpose V2.

## 2. samm: Azure AI Search teenuse loomine

1. Logige sisse [Azure portaalis](https://portal.azure.com/?wt.mc_id=studentamb_258691).
2. Vasakul navigeerimispaanil klõpsake **Loo ressurss**.
3. Otsingukasti tippige "Azure AI Search" ja valige tulemuste hulgast **Azure AI Search**.
4. Klõpsake nuppu **Loo**.
5. Vahekaardil **Põhiline** sisestage järgmine teave:
   - **Tellimus**: Valige oma Azure tellimus.
   - **Ressursirühm**: Looge uus ressursirühm või valige olemasolev.
   - **Ressursi nimi**: Sisestage oma otsinguteenusele unikaalne nimi.
   - **Regioon**: Valige kasutajatele lähim piirkond.
   - **Hinnaklass**: Valige hinnaklass vastavalt oma vajadustele. Testimiseks võite alustada tasuta tasemega.
6. Klõpsake **Ülevaade + loo**.
7. Kinnitage seaded ja klõpsake **Loo**, et teenus luua.

## 3. samm: Azure AI Search kasutuselevõtt

1. Kui juurutamine on lõpetatud, minge Azure portaalis oma otsinguteenuse lehele.
2. Otsinguteenuse ülevaate paanis kopeerige URL. See peaks välja nägema `https://<service-name>.search.windows.net`.
3. **(Soovitatav)** Lülitage sisse võtmeta juurdepääs Microsoft Entra ID (RBAC) abil, nagu näidatud allpool samm 4 — võtme kasutamine pole vajalik. Selle juhendi näited loovad/värskendavad indekseid ja laadivad dokumendid üles, mille jaoks on vajalikud rollid **Search Service Contributor** ja **Search Index Data Contributor** (või võtme-põhise autentimise puhul **põhiadministraatori võti** — mitte päringu võti). Kui te ei saa RBAC-i kasutada, avage **Seaded > Võtmed** ja kopeerige **põhiadministraatori võti**.
4. Järgige [Kiirjuhendi](https://learn.microsoft.com/azure/search/search-get-started-portal?pivots=import-data-new) samme, et luua indeks, üles laadida andmeid ja teha otsinguid.

## 4. samm: Azure AI Search tööriistade kasutamine

Azure AI Search integreerub erinevate tööriistadega, et parandada teie otsingu võimalusi. Võite kasutada Azure CLI-d, Python SDK-d, .NET SDK-d ja teisi tööriistu, et teostada keerukamaid konfiguratsioone ja toiminguid.

### Azure CLI kasutamine

1. Installige Azure CLI, järgides juhiseid aadressil [Install Azure CLI](https://learn.microsoft.com/cli/azure/install-azure-cli?wt.mc_id=studentamb_258691).
2. Logige sisse Azure CLI-sse käsuga:

   ```bash
   az login
   ```
3. **(Soovitatav) Võtmeta juurdepääsu lubamine Microsoft Entra ID (RBAC) abil:**

    ```bash
    az search service update --name <service-name> --resource-group <resource-group> --auth-options aadOrApiKey
    az role assignment create --assignee <your-user-or-principal-id> --role "Search Service Contributor" --scope $(az search service show -g <resource-group> -n <service-name> --query id -o tsv)
    az role assignment create --assignee <your-user-or-principal-id> --role "Search Index Data Contributor" --scope $(az search service show -g <resource-group> -n <service-name> --query id -o tsv)
    # az search teenuse kuvamisel puudub "endpoint" väli; ehita URL teenuse nime põhjal.
    export AZURE_SEARCH_SERVICE_ENDPOINT="https://<service-name>.search.windows.net"
    ```

    RBAC-i lubamise korral autentivad allpool olevad Python ja .NET SDK näited `DefaultAzureCredential` abil, mis kasutab teie `az login` sessiooni kohalikul arendamisel — administraatori võti ei ole vajalik. Vaadake [Ühendamine Azure AI Searchiga rollide kaudu](https://learn.microsoft.com/azure/search/search-security-rbac).

4. **(Varuvõimalus) Võtme-põhine autentimine** — ainult juhul, kui RBAC-i kasutada ei saa, salvestage administraatori võti:

#### Salvestage nii lõpp-punkt kui ka API võti Azure AI Searchi näite jaoks keskkonnamuutujatesse.

    ```bash
    # zsh/bash
    # az search service show-l pole "endpoint" välja; koostage URL teenuse nime põhjal.
    export AZURE_SEARCH_SERVICE_ENDPOINT="https://<service-name>.search.windows.net"
    export AZURE_SEARCH_API_KEY=$(az search admin-key show -g <resource-group> --service-name <service-name> --query "primaryKey" -o tsv)
    ```

    ```powershell
    # PowerShell
    # az search service show-l pole "endpoint" välja; koostage URL teenuse nime põhjal.
    $env:AZURE_SEARCH_SERVICE_ENDPOINT = "https://<service-name>.search.windows.net"
    $env:AZURE_SEARCH_API_KEY = $(az search admin-key show -g <resource-group> --service-name <service-name> --query "primaryKey" -o tsv)
    ```

### Python SDK kasutamine

1. Installige Azure Cognitive Search klientraamatukogu ja Azure Identity Python jaoks:

   ```bash
   pip install azure-search-documents azure-identity
   ```

2. Kasutage järgmist Python-koodi indeksi loomiseks ja dokumentide üleslaadimiseks:

    ```python
    import os
    from azure.identity import DefaultAzureCredential
    from azure.search.documents import SearchClient
    from azure.search.documents.indexes import SearchIndexClient
    from azure.search.documents.indexes.models import SearchIndex, SimpleField, edm

    service_endpoint = os.getenv("AZURE_SEARCH_SERVICE_ENDPOINT")
    index_name = "sample-index"

    # Võtmeta (soovitatav): kasutab teie `az login` identiteeti Entra ID RBAC kaudu.
    # Nõuab "Search Service Contributor" ja "Search Index Data Contributor" rolle.
    credential = DefaultAzureCredential()
    # Tagasiastumine (võtmepõhine autentimine):
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

    Allpool olev .NET näide kasutab `DefaultAzureCredential`, mis võib kasutada `az login` kaudu Azure CLI sisselogimist kohalikul arendamisel.

2. Siin on .NET kood failist `AzureSearch.cs`:

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

Täpsema info saamiseks vt allolevaid dokumente:

- [Azure Cognitive Search teenuse loomine](https://learn.microsoft.com/azure/search/search-create-service-portal?wt.mc_id=studentamb_258691)
- [Azure Cognitive Search kasutuselevõtt](https://learn.microsoft.com/azure/search/search-get-started-portal?wt.mc_id=studentamb_258691)
- [Azure AI Search tööriistad](https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-ai-search?tabs=azurecli%2Cpython&pivots=code-examples?wt.mc_id=studentamb_258691)

## Kokkuvõte

Olete edukalt seadistanud Azure AI Search teenuse Azure portaalis ja integreerinud tööriistad. Nüüd saate uurida Azure AI Search keerukamaid funktsioone ja võimalusi, et täiustada oma otsingulahendusi.

Täiendava abi saamiseks külastage [Azure Cognitive Search dokumentatsiooni](https://learn.microsoft.com/azure/search/?wt.mc_id=studentamb_258691).

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Lahtiütlus**:
See dokument on tõlgitud kasutades AI tõlketeenust [Co-op Translator](https://github.com/Azure/co-op-translator). Kuigi me püüdleme täpsuse poole, palun pange tähele, et automatiseeritud tõlgetes võib esineda vigu või ebatäpsusi. Originaaldokument selle emakeeles tuleks pidada autoriteetseks allikaks. Olulise teabe puhul soovitatakse kasutada professionaalset inimtõlget. Me ei vastuta selle tõlkega seotud eksimustest või valesti mõistmistest.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->