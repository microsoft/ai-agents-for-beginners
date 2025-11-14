<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "11e38db0898a788612b917e329dcdb5b",
  "translation_date": "2025-11-07T08:50:53+00:00",
  "source_file": "00-course-setup/AzureSearch.md",
  "language_code": "sl"
}
-->
# Vodnik za nastavitev Azure AI Search

Ta vodnik vam bo pomagal nastaviti Azure AI Search z uporabo portala Azure. Sledite spodnjim korakom za ustvarjanje in konfiguracijo vaše storitve Azure AI Search.

## Predpogoji

Preden začnete, se prepričajte, da imate naslednje:

- Naročnino na Azure. Če naročnine na Azure še nimate, lahko ustvarite brezplačen račun na [Azure Free Account](https://azure.microsoft.com/free/?wt.mc_id=studentamb_258691).

## Korak 1: Ustvarite Azure Storage Account

1. Sledite tem navodilom, [Ustvarite Azure Storage Account](https://learn.microsoft.com/azure/storage/common/storage-account-create?tabs=azure-portal), za ustvarjanje novega Azure Storage Account.
   **NOTE**: Prepričajte se, da je vrsta Storage Account Standard General Purpose V2.

## Korak 2: Ustvarite Azure AI Search Service

1. Prijavite se v [Azure portal](https://portal.azure.com/?wt.mc_id=studentamb_258691).
2. V levem navigacijskem meniju kliknite **Create a resource**.
3. V iskalno polje vnesite "Azure AI Search" in izberite **Azure AI Search** s seznama rezultatov.
4. Kliknite gumb **Create**.
5. Na zavihku **Basics** vnesite naslednje informacije:
   - **Subscription**: Izberite svojo naročnino na Azure.
   - **Resource group**: Ustvarite novo skupino virov ali izberite obstoječo.
   - **Resource name**: Vnesite edinstveno ime za vašo iskalno storitev.
   - **Region**: Izberite regijo, ki je najbližje vašim uporabnikom.
   - **Pricing tier**: Izberite cenovni razred, ki ustreza vašim zahtevam. Za testiranje lahko začnete z brezplačnim razredom.
6. Kliknite **Review + create**.
7. Preglejte nastavitve in kliknite **Create**, da ustvarite iskalno storitev.

## Korak 3: Začnite z Azure AI Search

1. Ko je uvajanje končano, pojdite na svojo iskalno storitev v portalu Azure.
2. Na pregledni plošči iskalne storitve kopirajte URL. Videti bi moral kot `https://<service-name>.search.windows.net`.
3. Na plošči Settings > Keys kopirajte ključ za poizvedbe.
4. Sledite korakom na strani [Quickstart guide](https://learn.microsoft.com/azure/search/search-get-started-portal?pivots=import-data-new) za ustvarjanje indeksa, nalaganje podatkov in izvedbo iskalne poizvedbe.

## Korak 4: Uporabite orodja Azure AI Search

Azure AI Search se integrira z različnimi orodji za izboljšanje vaših iskalnih zmogljivosti. Uporabite lahko Azure CLI, Python SDK, .NET SDK in druga orodja za napredne konfiguracije in operacije.

### Uporaba Azure CLI

1. Namestite Azure CLI z upoštevanjem navodil na [Install Azure CLI](https://learn.microsoft.com/cli/azure/install-azure-cli?wt.mc_id=studentamb_258691).
2. Prijavite se v Azure CLI z ukazom:

   ```bash
   az login
   ```

3. Shranite tako končno točko kot API ključ za instanco Azure AI Search v okoljske spremenljivke.

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

### Uporaba Python SDK

1. Namestite knjižnico odjemalca Azure Cognitive Search za Python:

   ```bash
   pip install azure-search-documents
   ```

2. Uporabite naslednjo Python kodo za ustvarjanje indeksa in nalaganje dokumentov:

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

### Uporaba .NET SDK

1. Zaženite naslednji ukaz za ustvarjanje indeksa in nalaganje dokumentov:

    ```bash
    dotnet run ./AzureSearch.cs
    ```

2. Tukaj je .NET koda za `AzureSearch.cs`:

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

Za podrobnejše informacije si oglejte naslednjo dokumentacijo:

- [Ustvarite storitev Azure Cognitive Search](https://learn.microsoft.com/azure/search/search-create-service-portal?wt.mc_id=studentamb_258691)
- [Začnite z Azure Cognitive Search](https://learn.microsoft.com/azure/search/search-get-started-portal?wt.mc_id=studentamb_258691)
- [Orodja Azure AI Search](https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-ai-search?tabs=azurecli%2Cpython&pivots=code-examples?wt.mc_id=studentamb_258691)

## Zaključek

Uspešno ste nastavili Azure AI Search z uporabo portala Azure in integriranih orodij. Zdaj lahko raziščete bolj napredne funkcije in zmogljivosti Azure AI Search za izboljšanje vaših iskalnih rešitev.

Za dodatno pomoč obiščite [dokumentacijo Azure Cognitive Search](https://learn.microsoft.com/azure/search/?wt.mc_id=studentamb_258691).

---

**Omejitev odgovornosti**:  
Ta dokument je bil preveden z uporabo storitve za prevajanje z umetno inteligenco [Co-op Translator](https://github.com/Azure/co-op-translator). Čeprav si prizadevamo za natančnost, vas prosimo, da upoštevate, da lahko avtomatski prevodi vsebujejo napake ali netočnosti. Izvirni dokument v njegovem maternem jeziku je treba obravnavati kot avtoritativni vir. Za ključne informacije priporočamo profesionalni človeški prevod. Ne prevzemamo odgovornosti za morebitne nesporazume ali napačne razlage, ki bi nastale zaradi uporabe tega prevoda.