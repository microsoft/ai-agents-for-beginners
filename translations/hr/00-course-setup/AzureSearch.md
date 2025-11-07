<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "11e38db0898a788612b917e329dcdb5b",
  "translation_date": "2025-11-07T08:50:12+00:00",
  "source_file": "00-course-setup/AzureSearch.md",
  "language_code": "hr"
}
-->
# Vodič za postavljanje Azure AI Search

Ovaj vodič pomoći će vam da postavite Azure AI Search koristeći Azure portal. Slijedite korake u nastavku kako biste kreirali i konfigurirali svoju Azure AI Search uslugu.

## Preduvjeti

Prije nego započnete, osigurajte sljedeće:

- Azure pretplatu. Ako nemate Azure pretplatu, možete kreirati besplatni račun na [Azure Free Account](https://azure.microsoft.com/free/?wt.mc_id=studentamb_258691).

## Korak 1: Kreiranje Azure Storage računa

1. Slijedite ove upute, [Kreiranje Azure Storage računa](https://learn.microsoft.com/azure/storage/common/storage-account-create?tabs=azure-portal), kako biste kreirali novi Azure Storage račun.
   **NAPOMENA**: Provjerite da je tip Storage računa Standard General Purpose V2.

## Korak 2: Kreiranje Azure AI Search usluge

1. Prijavite se na [Azure portal](https://portal.azure.com/?wt.mc_id=studentamb_258691).
2. U navigacijskom izborniku s lijeve strane kliknite na **Create a resource**.
3. U okvir za pretraživanje upišite "Azure AI Search" i odaberite **Azure AI Search** s popisa rezultata.
4. Kliknite na gumb **Create**.
5. Na kartici **Basics** unesite sljedeće informacije:
   - **Subscription**: Odaberite svoju Azure pretplatu.
   - **Resource group**: Kreirajte novu grupu resursa ili odaberite postojeću.
   - **Resource name**: Unesite jedinstveno ime za svoju uslugu pretraživanja.
   - **Region**: Odaberite regiju najbližu vašim korisnicima.
   - **Pricing tier**: Odaberite razinu cijene koja odgovara vašim potrebama. Možete započeti s besplatnom razinom za testiranje.
6. Kliknite **Review + create**.
7. Pregledajte postavke i kliknite **Create** kako biste kreirali uslugu pretraživanja.

## Korak 3: Početak rada s Azure AI Search

1. Kada je implementacija dovršena, idite na svoju uslugu pretraživanja na Azure portalu.
2. U preglednom panelu usluge pretraživanja kopirajte URL. Trebao bi izgledati ovako: `https://<service-name>.search.windows.net`.
3. U postavkama > Keys panelu kopirajte ključ za upite.
4. Slijedite korake na stranici [Quickstart guide](https://learn.microsoft.com/azure/search/search-get-started-portal?pivots=import-data-new) kako biste kreirali indeks, učitali podatke i izvršili upit za pretraživanje.

## Korak 4: Korištenje alata za Azure AI Search

Azure AI Search integrira se s raznim alatima za poboljšanje vaših mogućnosti pretraživanja. Možete koristiti Azure CLI, Python SDK, .NET SDK i druge alate za napredne konfiguracije i operacije.

### Korištenje Azure CLI

1. Instalirajte Azure CLI slijedeći upute na [Instalacija Azure CLI](https://learn.microsoft.com/cli/azure/install-azure-cli?wt.mc_id=studentamb_258691).
2. Prijavite se na Azure CLI koristeći naredbu:

   ```bash
   az login
   ```

3. Pohranite endpoint i API ključ za instancu Azure AI Search u varijable okruženja.

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

### Korištenje Python SDK-a

1. Instalirajte knjižnicu klijenta za Azure Cognitive Search za Python:

   ```bash
   pip install azure-search-documents
   ```

2. Koristite sljedeći Python kod za kreiranje indeksa i učitavanje dokumenata:

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

### Korištenje .NET SDK-a

1. Pokrenite sljedeću naredbu za kreiranje indeksa i učitavanje dokumenata:

    ```bash
    dotnet run ./AzureSearch.cs
    ```

2. Evo .NET koda za `AzureSearch.cs`:

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

Za detaljnije informacije, pogledajte sljedeću dokumentaciju:

- [Kreiranje Azure Cognitive Search usluge](https://learn.microsoft.com/azure/search/search-create-service-portal?wt.mc_id=studentamb_258691)
- [Početak rada s Azure Cognitive Search](https://learn.microsoft.com/azure/search/search-get-started-portal?wt.mc_id=studentamb_258691)
- [Alati za Azure AI Search](https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-ai-search?tabs=azurecli%2Cpython&pivots=code-examples?wt.mc_id=studentamb_258691)

## Zaključak

Uspješno ste postavili Azure AI Search koristeći Azure portal i integrirane alate. Sada možete istražiti napredne značajke i mogućnosti Azure AI Search kako biste poboljšali svoja rješenja za pretraživanje.

Za dodatnu pomoć, posjetite [Azure Cognitive Search dokumentaciju](https://learn.microsoft.com/azure/search/?wt.mc_id=studentamb_258691).

---

**Izjava o odricanju odgovornosti**:  
Ovaj dokument je preveden pomoću AI usluge za prevođenje [Co-op Translator](https://github.com/Azure/co-op-translator). Iako nastojimo osigurati točnost, imajte na umu da automatski prijevodi mogu sadržavati pogreške ili netočnosti. Izvorni dokument na izvornom jeziku treba smatrati autoritativnim izvorom. Za ključne informacije preporučuje se profesionalni prijevod od strane čovjeka. Ne preuzimamo odgovornost za nesporazume ili pogrešne interpretacije koje proizlaze iz korištenja ovog prijevoda.