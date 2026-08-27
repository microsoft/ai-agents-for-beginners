# Azure AI Search oppsettsveiledning

Denne veiledningen hjelper deg med å sette opp Azure AI Search ved hjelp av Azure-portalen. Følg trinnene nedenfor for å opprette og konfigurere Azure AI Search-tjenesten din.

## Forutsetninger

Før du begynner, må du sikre deg følgende:

- Et Azure-abonnement. Hvis du ikke har et Azure-abonnement, kan du opprette en gratis konto på [Azure Free Account](https://azure.microsoft.com/free/?wt.mc_id=studentamb_258691).

## Trinn 1: Opprett en Azure Storage-konto

1. Følg denne instruksjonen, [Opprett en Azure Storage-konto](https://learn.microsoft.com/azure/storage/common/storage-account-create?tabs=azure-portal), for å opprette en ny Azure Storage-konto.
   **MERK**: Sørg for at typen Storage-konto er Standard General Purpose V2.

## Trinn 2: Opprett en Azure AI Search-tjeneste

1. Logg inn på [Azure-portalen](https://portal.azure.com/?wt.mc_id=studentamb_258691).
2. Klikk på **Opprett en ressurs** i navigasjonsruten til venstre.
3. Skriv "Azure AI Search" i søkefeltet og velg **Azure AI Search** fra resultatlisten.
4. Klikk på **Opprett**-knappen.
5. På fanen **Grunnleggende**, fyll inn følgende informasjon:
   - **Abonnement**: Velg ditt Azure-abonnement.
   - **Ressursgruppe**: Opprett en ny ressursgruppe eller velg en eksisterende.
   - **Ressursnavn**: Skriv inn et unikt navn for søketjenesten din.
   - **Region**: Velg regionen som er nærmest brukerne dine.
   - **Prisnivå**: Velg et prisnivå som passer dine behov. Du kan starte med Gratis-nivået for testing.
6. Klikk **Gjennomgå + opprett**.
7. Gjennomgå innstillingene og klikk **Opprett** for å opprette søketjenesten.

## Trinn 3: Kom i gang med Azure AI Search

1. Når distribusjonen er fullført, naviger til søketjenesten din i Azure-portalen.
2. I oversiktsruten for søketjenesten kopierer du nettadressen. Den skal se slik ut: `https://<service-name>.search.windows.net`.
3. **(Anbefalt)** Aktiver nøkkelfri tilgang med Microsoft Entra ID (RBAC) som vist i Trinn 4 nedenfor — ingen nøkkel nødvendig. Eksemplene i denne veiledningen oppretter/oppdaterer indekser og laster opp dokumenter, som krever rollene **Search Service Contributor** og **Search Index Data Contributor** (eller for nøkkelbasert autentisering, **primær administrasjonsnøkkel** — ikke spørringsnøkkelen). Bare hvis du ikke kan bruke RBAC, åpne **Innstillinger > Nøkler** og kopier **primær administrasjonsnøkkel**.
4. Følg trinnene på [Kom i gang-veiledningen](https://learn.microsoft.com/azure/search/search-get-started-portal?pivots=import-data-new) for å opprette en indeks, laste opp data og utføre et søk.

## Trinn 4: Bruk Azure AI Search-verktøy

Azure AI Search integreres med ulike verktøy for å forbedre søkefunksjonaliteten din. Du kan bruke Azure CLI, Python SDK, .NET SDK og andre verktøy for avanserte konfigurasjoner og operasjoner.

### Bruke Azure CLI

1. Installer Azure CLI ved å følge instruksjonene på [Installer Azure CLI](https://learn.microsoft.com/cli/azure/install-azure-cli?wt.mc_id=studentamb_258691).
2. Logg inn i Azure CLI med kommandoen:

   ```bash
   az login
   ```
3. **(Anbefalt) Aktiver nøkkelfri tilgang med Microsoft Entra ID (RBAC):**

    ```bash
    az search service update --name <service-name> --resource-group <resource-group> --auth-options aadOrApiKey
    az role assignment create --assignee <your-user-or-principal-id> --role "Search Service Contributor" --scope $(az search service show -g <resource-group> -n <service-name> --query id -o tsv)
    az role assignment create --assignee <your-user-or-principal-id> --role "Search Index Data Contributor" --scope $(az search service show -g <resource-group> -n <service-name> --query id -o tsv)
    # az search service show har ikke noe "endpoint"-felt; bygg URL-en fra tjenestenavnet.
    export AZURE_SEARCH_SERVICE_ENDPOINT="https://<service-name>.search.windows.net"
    ```

    Med RBAC aktivert autentiserer Python- og .NET SDK-eksemplene nedenfor med `DefaultAzureCredential`, som bruker din `az login`-økt under lokal utvikling — ingen administrasjonsnøkkel nødvendig. Se [Koble til Azure AI Search ved hjelp av roller](https://learn.microsoft.com/azure/search/search-security-rbac).

4. **(Reserve) Nøkkelbasert autentisering** — bare hvis du ikke kan bruke RBAC, lagre administrasjonsnøkkelen også:

#### Lagre både endepunkt og API-nøkkel for Azure AI Search-instansen som miljøvariabler.

    ```bash
    # zsh/bash
    # az search service show har ikke feltet "endpoint"; bygg URL-en fra tjenestenavnet.
    export AZURE_SEARCH_SERVICE_ENDPOINT="https://<service-name>.search.windows.net"
    export AZURE_SEARCH_API_KEY=$(az search admin-key show -g <resource-group> --service-name <service-name> --query "primaryKey" -o tsv)
    ```

    ```powershell
    # PowerShell
    # az search service show har ikke feltet "endpoint"; bygg URL-en fra tjenestenavnet.
    $env:AZURE_SEARCH_SERVICE_ENDPOINT = "https://<service-name>.search.windows.net"
    $env:AZURE_SEARCH_API_KEY = $(az search admin-key show -g <resource-group> --service-name <service-name> --query "primaryKey" -o tsv)
    ```

### Bruke Python SDK

1. Installer Azure Cognitive Search-klientbiblioteket og Azure Identity for Python:

   ```bash
   pip install azure-search-documents azure-identity
   ```

2. Bruk følgende Python-kode for å opprette en indeks og laste opp dokumenter:

    ```python
    import os
    from azure.identity import DefaultAzureCredential
    from azure.search.documents import SearchClient
    from azure.search.documents.indexes import SearchIndexClient
    from azure.search.documents.indexes.models import SearchIndex, SimpleField, edm

    service_endpoint = os.getenv("AZURE_SEARCH_SERVICE_ENDPOINT")
    index_name = "sample-index"

    # Keyless (anbefalt): bruker din `az login` identitet via Entra ID RBAC.
    # Krever rollene "Search Service Contributor" og "Search Index Data Contributor".
    credential = DefaultAzureCredential()
    # Tilbakefall (nøkkelbasert autentisering):
    # fra azure.core.credentials import AzureKeyCredential
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

### Bruke .NET SDK

1. Kjør følgende kommando for å opprette en indeks og laste opp dokumenter:

    ```bash
    dotnet run ./AzureSearch.cs
    ```

    .NET-eksemplet nedenfor bruker `DefaultAzureCredential`, som kan bruke din Azure CLI pålogging via `az login` under lokal utvikling.

2. Her er .NET-koden i `AzureSearch.cs`:

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

For mer detaljert informasjon, se følgende dokumentasjon:

- [Opprett en Azure Cognitive Search-tjeneste](https://learn.microsoft.com/azure/search/search-create-service-portal?wt.mc_id=studentamb_258691)
- [Kom i gang med Azure Cognitive Search](https://learn.microsoft.com/azure/search/search-get-started-portal?wt.mc_id=studentamb_258691)
- [Azure AI Search-verktøy](https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-ai-search?tabs=azurecli%2Cpython&pivots=code-examples?wt.mc_id=studentamb_258691)

## Konklusjon

Du har nå satt opp Azure AI Search ved hjelp av Azure-portalen og integrerte verktøy. Du kan nå utforske mer avanserte funksjoner og muligheter i Azure AI Search for å forbedre søkeløsningene dine.

For ytterligere hjelp, besøk [Azure Cognitive Search-dokumentasjonen](https://learn.microsoft.com/azure/search/?wt.mc_id=studentamb_258691).

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfraskrivelse**:
Dette dokumentet er oversatt ved hjelp av AI-oversettelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selv om vi streber etter nøyaktighet, vær oppmerksom på at automatiske oversettelser kan inneholde feil eller unøyaktigheter. Det opprinnelige dokumentet på originalspråket skal betraktes som den autoritative kilden. For kritisk informasjon anbefales profesjonell menneskelig oversettelse. Vi er ikke ansvarlige for eventuelle misforståelser eller feiltolkninger som oppstår ved bruk av denne oversettelsen.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->