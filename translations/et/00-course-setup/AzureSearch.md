<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "11e38db0898a788612b917e329dcdb5b",
  "translation_date": "2025-11-07T08:55:12+00:00",
  "source_file": "00-course-setup/AzureSearch.md",
  "language_code": "et"
}
-->
# Azure AI Searchi seadistamise juhend

See juhend aitab teil seadistada Azure AI Searchi Azure'i portaalis. Järgige allolevaid samme, et luua ja konfigureerida oma Azure AI Search teenus.

## Eeltingimused

Enne alustamist veenduge, et teil on olemas järgmised asjad:

- Azure'i tellimus. Kui teil pole Azure'i tellimust, saate luua tasuta konto aadressil [Azure Free Account](https://azure.microsoft.com/free/?wt.mc_id=studentamb_258691).

## Samm 1: Looge Azure'i salvestuskonto

1. Järgige juhiseid [Looge Azure'i salvestuskonto](https://learn.microsoft.com/azure/storage/common/storage-account-create?tabs=azure-portal), et luua uus Azure'i salvestuskonto.  
   **NOTE**: Veenduge, et salvestuskonto tüüp oleks Standard General Purpose V2.

## Samm 2: Looge Azure AI Search teenus

1. Logige sisse [Azure'i portaalis](https://portal.azure.com/?wt.mc_id=studentamb_258691).
2. Vasakpoolsel navigeerimispaneelil klõpsake **Create a resource**.
3. Otsingukasti sisestage "Azure AI Search" ja valige tulemuste loendist **Azure AI Search**.
4. Klõpsake nuppu **Create**.
5. **Basics** vahekaardil sisestage järgmine teave:
   - **Subscription**: Valige oma Azure'i tellimus.
   - **Resource group**: Looge uus ressursigrupp või valige olemasolev.
   - **Resource name**: Sisestage oma otsinguteenusele unikaalne nimi.
   - **Region**: Valige oma kasutajatele lähim piirkond.
   - **Pricing tier**: Valige hinnaklass, mis vastab teie vajadustele. Testimiseks võite alustada tasuta tasemega.
6. Klõpsake **Review + create**.
7. Vaadake seaded üle ja klõpsake **Create**, et luua otsinguteenus.

## Samm 3: Alustage Azure AI Searchiga

1. Kui juurutamine on lõpule viidud, navigeerige oma otsinguteenusele Azure'i portaalis.
2. Otsinguteenuse ülevaate paneelil kopeerige URL. See peaks välja nägema nagu `https://<service-name>.search.windows.net`.
3. Seadete > Keys paneelil kopeerige päringuvõti.
4. Järgige [Kiirjuhendi](https://learn.microsoft.com/azure/search/search-get-started-portal?pivots=import-data-new) lehel toodud samme, et luua indeks, laadida andmeid üles ja teha otsingupäring.

## Samm 4: Kasutage Azure AI Search tööriistu

Azure AI Search integreerub erinevate tööriistadega, et täiustada teie otsinguvõimalusi. Võite kasutada Azure CLI-d, Python SDK-d, .NET SDK-d ja teisi tööriistu edasijõudnud konfiguratsioonide ja toimingute jaoks.

### Azure CLI kasutamine

1. Installige Azure CLI, järgides juhiseid [Install Azure CLI](https://learn.microsoft.com/cli/azure/install-azure-cli?wt.mc_id=studentamb_258691).
2. Logige Azure CLI-sse sisse järgmise käsuga:

   ```bash
   az login
   ```

3. Salvestage nii otsinguteenuse lõpp-punkt kui ka API võti keskkonnamuutujatesse.

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

### Python SDK kasutamine

1. Installige Azure Cognitive Search klienditeek Pythonile:

   ```bash
   pip install azure-search-documents
   ```

2. Kasutage järgmist Python koodi, et luua indeks ja laadida dokumendid üles:

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

### .NET SDK kasutamine

1. Käivitage järgmine käsk, et luua indeks ja laadida dokumendid üles:

    ```bash
    dotnet run ./AzureSearch.cs
    ```

2. Siin on .NET kood `AzureSearch.cs`:

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

Lisateabe saamiseks vaadake järgmist dokumentatsiooni:

- [Looge Azure Cognitive Search teenus](https://learn.microsoft.com/azure/search/search-create-service-portal?wt.mc_id=studentamb_258691)
- [Alustage Azure Cognitive Searchiga](https://learn.microsoft.com/azure/search/search-get-started-portal?wt.mc_id=studentamb_258691)
- [Azure AI Search tööriistad](https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-ai-search?tabs=azurecli%2Cpython&pivots=code-examples?wt.mc_id=studentamb_258691)

## Kokkuvõte

Olete edukalt seadistanud Azure AI Searchi Azure'i portaalis ja integreerinud tööriistad. Nüüd saate uurida Azure AI Searchi täpsemaid funktsioone ja võimalusi, et täiustada oma otsingulahendusi.

Lisateabe saamiseks külastage [Azure Cognitive Search dokumentatsiooni](https://learn.microsoft.com/azure/search/?wt.mc_id=studentamb_258691).

---

**Lahtiütlus**:  
See dokument on tõlgitud AI tõlketeenuse [Co-op Translator](https://github.com/Azure/co-op-translator) abil. Kuigi püüame tagada täpsust, palume arvestada, et automaatsed tõlked võivad sisaldada vigu või ebatäpsusi. Algne dokument selle algses keeles tuleks pidada autoriteetseks allikaks. Olulise teabe puhul soovitame kasutada professionaalset inimtõlget. Me ei vastuta selle tõlke kasutamisest tulenevate arusaamatuste või valesti tõlgenduste eest.