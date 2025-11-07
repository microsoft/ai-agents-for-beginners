<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "11e38db0898a788612b917e329dcdb5b",
  "translation_date": "2025-11-07T08:40:05+00:00",
  "source_file": "00-course-setup/AzureSearch.md",
  "language_code": "no"
}
-->
# Veiledning for oppsett av Azure AI Search

Denne veiledningen hjelper deg med å sette opp Azure AI Search ved hjelp av Azure-portalen. Følg trinnene nedenfor for å opprette og konfigurere din Azure AI Search-tjeneste.

## Forutsetninger

Før du begynner, må du ha følgende:

- Et Azure-abonnement. Hvis du ikke har et Azure-abonnement, kan du opprette en gratis konto på [Azure Free Account](https://azure.microsoft.com/free/?wt.mc_id=studentamb_258691).

## Trinn 1: Opprett en Azure Storage-konto

1. Følg denne instruksjonen, [Opprett en Azure Storage-konto](https://learn.microsoft.com/azure/storage/common/storage-account-create?tabs=azure-portal), for å opprette en ny Azure Storage-konto.
   **NOTE**: Sørg for at typen Storage-konto er Standard General Purpose V2.

## Trinn 2: Opprett en Azure AI Search-tjeneste

1. Logg inn på [Azure-portalen](https://portal.azure.com/?wt.mc_id=studentamb_258691).
2. Klikk på **Opprett en ressurs** i navigasjonsfeltet til venstre.
3. Skriv "Azure AI Search" i søkeboksen og velg **Azure AI Search** fra resultatlisten.
4. Klikk på **Opprett**-knappen.
5. I **Grunnleggende**-fanen, oppgi følgende informasjon:
   - **Abonnement**: Velg ditt Azure-abonnement.
   - **Ressursgruppe**: Opprett en ny ressursgruppe eller velg en eksisterende.
   - **Ressursnavn**: Angi et unikt navn for søketjenesten din.
   - **Region**: Velg regionen nærmest brukerne dine.
   - **Prisnivå**: Velg et prisnivå som passer dine behov. Du kan starte med gratisnivået for testing.
6. Klikk **Gjennomgå + opprett**.
7. Gjennomgå innstillingene og klikk **Opprett** for å opprette søketjenesten.

## Trinn 3: Kom i gang med Azure AI Search

1. Når distribusjonen er fullført, naviger til søketjenesten din i Azure-portalen.
2. I oversiktspanelet for søketjenesten, kopier URL-en. Den skal se slik ut: `https://<service-name>.search.windows.net`.
3. I Innstillinger > Nøkler-panelet, kopier spørringsnøkkelen.
4. Følg trinnene på [Hurtigstart-veiledningen](https://learn.microsoft.com/azure/search/search-get-started-portal?pivots=import-data-new) for å opprette en indeks, laste opp data og utføre en søkespørring.

## Trinn 4: Bruk Azure AI Search-verktøy

Azure AI Search integreres med ulike verktøy for å forbedre søkefunksjonaliteten din. Du kan bruke Azure CLI, Python SDK, .NET SDK og andre verktøy for avanserte konfigurasjoner og operasjoner.

### Bruke Azure CLI

1. Installer Azure CLI ved å følge instruksjonene på [Installer Azure CLI](https://learn.microsoft.com/cli/azure/install-azure-cli?wt.mc_id=studentamb_258691).
2. Logg inn på Azure CLI ved å bruke kommandoen:

   ```bash
   az login
   ```

3. Lagre både endepunkt og API-nøkkel for Azure AI Search-instansen til miljøvariabler.

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

### Bruke Python SDK

1. Installer Azure Cognitive Search-klientbiblioteket for Python:

   ```bash
   pip install azure-search-documents
   ```

2. Bruk følgende Python-kode for å opprette en indeks og laste opp dokumenter:

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

### Bruke .NET SDK

1. Kjør følgende kommando for å opprette en indeks og laste opp dokumenter:

    ```bash
    dotnet run ./AzureSearch.cs
    ```

2. Her er .NET-koden for `AzureSearch.cs`:

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

For mer detaljert informasjon, se følgende dokumentasjon:

- [Opprett en Azure Cognitive Search-tjeneste](https://learn.microsoft.com/azure/search/search-create-service-portal?wt.mc_id=studentamb_258691)
- [Kom i gang med Azure Cognitive Search](https://learn.microsoft.com/azure/search/search-get-started-portal?wt.mc_id=studentamb_258691)
- [Azure AI Search-verktøy](https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-ai-search?tabs=azurecli%2Cpython&pivots=code-examples?wt.mc_id=studentamb_258691)

## Konklusjon

Du har nå satt opp Azure AI Search ved hjelp av Azure-portalen og integrerte verktøy. Du kan nå utforske mer avanserte funksjoner og muligheter i Azure AI Search for å forbedre søkeløsningene dine.

For ytterligere hjelp, besøk [Azure Cognitive Search-dokumentasjonen](https://learn.microsoft.com/azure/search/?wt.mc_id=studentamb_258691).

---

**Ansvarsfraskrivelse**:  
Dette dokumentet er oversatt ved hjelp av AI-oversettelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selv om vi streber etter nøyaktighet, vær oppmerksom på at automatiserte oversettelser kan inneholde feil eller unøyaktigheter. Det originale dokumentet på sitt opprinnelige språk bør anses som den autoritative kilden. For kritisk informasjon anbefales profesjonell menneskelig oversettelse. Vi er ikke ansvarlige for misforståelser eller feiltolkninger som oppstår ved bruk av denne oversettelsen.