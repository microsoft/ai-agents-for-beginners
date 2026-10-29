# Vodič za postavljanje Azure AI Search

Ovaj vodič pomoći će vam postaviti Azure AI Search koristeći Azure portal. Slijedite dolje navedene korake za stvaranje i konfiguriranje vaše Azure AI Search usluge.

## Preduvjeti

Prije nego počnete, osigurajte da imate sljedeće:

- Pretplatu na Azure. Ako nemate pretplatu na Azure, možete otvoriti besplatan račun na [Azure Free Account](https://azure.microsoft.com/free/?wt.mc_id=studentamb_258691).

## Korak 1: Stvorite Azure Storage račun

1. Slijedite ovaj vodič, [Create an Azure storage account](https://learn.microsoft.com/azure/storage/common/storage-account-create?tabs=azure-portal), za stvaranje novog Azure Storage računa.
   **NAPOMENA**: Provjerite je li tip Storage računa Standard General Purpose V2.

## Korak 2: Stvorite Azure AI Search uslugu

1. Prijavite se u [Azure portal](https://portal.azure.com/?wt.mc_id=studentamb_258691).
2. U lijevom navigacijskom izborniku kliknite na **Create a resource**.
3. U polje za pretraživanje unesite "Azure AI Search" i odaberite **Azure AI Search** s popisa rezultata.
4. Kliknite na gumb **Create**.
5. Na kartici **Basics** unesite sljedeće podatke:
   - **Subscription**: Odaberite svoju Azure pretplatu.
   - **Resource group**: Stvorite novu grupu resursa ili odaberite postojeću.
   - **Resource name**: Unesite jedinstveno ime za vašu pretraživačku uslugu.
   - **Region**: Odaberite regiju najbližu vašim korisnicima.
   - **Pricing tier**: Odaberite razinu cijene koja odgovara vašim zahtjevima. Za testiranje možete početi s Besplatnim slojem.
6. Kliknite **Review + create**.
7. Pregledajte postavke i kliknite **Create** za stvaranje pretraživačke usluge.

## Korak 3: Počnite koristiti Azure AI Search

1. Nakon dovršetka implementacije, idite na svoju pretraživačku uslugu u Azure portalu.
2. U pregledu usluge kopirajte URL. Trebao bi izgledati kao `https://<service-name>.search.windows.net`.
3. **(Preporučeno)** Omogućite pristup bez ključa s Microsoft Entra ID (RBAC) kako je prikazano u Koraku 4 dolje — nije potreban ključ. Primjeri u ovom vodiču stvaraju/obnavljaju indekse i učitavaju dokumente, za što su potrebne uloge **Search Service Contributor** i **Search Index Data Contributor** (ili, za autentifikaciju pomoću ključa, **primarni administratorski ključ** — nije potrebno koristiti ključ za upite). Samo ako ne možete koristiti RBAC, otvorite **Settings > Keys** i kopirajte **primarni administratorski ključ**.
4. Slijedite korake u [Quickstart guide](https://learn.microsoft.com/azure/search/search-get-started-portal?pivots=import-data-new) za stvaranje indeksa, učitavanje podataka i izvođenje pretraživanja.

## Korak 4: Koristite Azure AI Search alate

Azure AI Search integrira se s raznim alatima kako bi unaprijedio vaše mogućnosti pretraživanja. Možete koristiti Azure CLI, Python SDK, .NET SDK i druge alate za napredne konfiguracije i operacije.

### Korištenje Azure CLI

1. Instalirajte Azure CLI slijedeći upute na [Install Azure CLI](https://learn.microsoft.com/cli/azure/install-azure-cli?wt.mc_id=studentamb_258691).
2. Prijavite se u Azure CLI koristeći naredbu:

   ```bash
   az login
   ```
3. **(Preporučeno) Omogućite pristup bez ključa s Microsoft Entra ID (RBAC):**

    ```bash
    az search service update --name <service-name> --resource-group <resource-group> --auth-options aadOrApiKey
    az role assignment create --assignee <your-user-or-principal-id> --role "Search Service Contributor" --scope $(az search service show -g <resource-group> -n <service-name> --query id -o tsv)
    az role assignment create --assignee <your-user-or-principal-id> --role "Search Index Data Contributor" --scope $(az search service show -g <resource-group> -n <service-name> --query id -o tsv)
    # az search service show has no "endpoint" field; build the URL from the service name.
    export AZURE_SEARCH_SERVICE_ENDPOINT="https://<service-name>.search.windows.net"
    ```

    S omogućenim RBAC-om, primjeri za Python i .NET SDK ispod autentificiraju se s `DefaultAzureCredential`, koji koristi vašu `az login` sesiju tijekom lokalnog razvoja — nije potreban administratorski ključ. Pogledajte [Connect to Azure AI Search using roles](https://learn.microsoft.com/azure/search/search-security-rbac).

4. **(Rezervna opcija) Autentifikacija temeljena na ključu** — samo ako ne možete koristiti RBAC, spremite i administratorski ključ:

#### Spremite i krajnju točku i API ključ za Azure AI Search instancu u varijable okoline.

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

### Korištenje Python SDK-a

1. Instalirajte Azure Cognitive Search klijentsku biblioteku i Azure Identity za Python:

   ```bash
   pip install azure-search-documents azure-identity
   ```

2. Upotrijebite sljedeći Python kod za stvaranje indeksa i učitavanje dokumenata:

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

### Korištenje .NET SDK-a

1. Pokrenite sljedeću naredbu za stvaranje indeksa i učitavanje dokumenata:

    ```bash
    dotnet run ./AzureSearch.cs
    ```

    .NET primjer ispod koristi `DefaultAzureCredential`, koji može koristiti vašu Azure CLI prijavu iz `az login` tijekom lokalnog razvoja.

2. Evo .NET koda za `AzureSearch.cs`:

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

Za detaljnije informacije, pogledajte sljedeću dokumentaciju:

- [Create an Azure Cognitive Search service](https://learn.microsoft.com/azure/search/search-create-service-portal?wt.mc_id=studentamb_258691)
- [Get started with Azure Cognitive Search](https://learn.microsoft.com/azure/search/search-get-started-portal?wt.mc_id=studentamb_258691)
- [Azure AI Search Tools](https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-ai-search?tabs=azurecli%2Cpython&pivots=code-examples?wt.mc_id=studentamb_258691)

## Zaključak

Uspješno ste postavili Azure AI Search koristeći Azure portal i integrirane alate. Sada možete istražiti naprednije značajke i mogućnosti Azure AI Search kako biste unaprijedili svoja rješenja za pretraživanje.

Za dodatnu pomoć posjetite [Azure Cognitive Search documentation](https://learn.microsoft.com/azure/search/?wt.mc_id=studentamb_258691).

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Napomena**:
Ovaj dokument je preveden korištenjem AI prevoditeljskog servisa [Co-op Translator](https://github.com/Azure/co-op-translator). Iako težimo točnosti, imajte na umu da automatski prijevodi mogu sadržavati greške ili netočnosti. Izvorni dokument na izvornom jeziku treba smatrati autoritativnim izvorom. Za važne informacije preporuča se profesionalni ljudski prijevod. Nismo odgovorni za bilo kakva nesporazumevanja ili pogrešne interpretacije koje proizlaze iz korištenja ovog prijevoda.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->