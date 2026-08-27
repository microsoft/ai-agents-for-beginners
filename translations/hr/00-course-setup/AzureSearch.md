# Vodič za postavljanje Azure AI Search

Ovaj vodič pomoći će vam postaviti Azure AI Search koristeći Azure portal. Slijedite korake u nastavku za stvaranje i konfiguraciju vaše Azure AI Search usluge.

## Preduvjeti

Prije nego što počnete, osigurajte da imate sljedeće:

- Pretplatu na Azure. Ako nemate pretplatu na Azure, možete napraviti besplatan račun na [Azure Free Account](https://azure.microsoft.com/free/?wt.mc_id=studentamb_258691).

## Korak 1: Stvorite Azure Storage račun

1. Slijedite ovaj postupak, [Create an Azure storage account](https://learn.microsoft.com/azure/storage/common/storage-account-create?tabs=azure-portal), za stvaranje novog Azure Storage računa.
   **NAPOMENA**: Provjerite je li tip Storage računa Standard General Purpose V2.

## Korak 2: Stvorite Azure AI Search servis

1. Prijavite se u [Azure portal](https://portal.azure.com/?wt.mc_id=studentamb_258691).
2. U lijevoj navigacijskoj traci kliknite na **Create a resource**.
3. U tražilicu unesite "Azure AI Search" i odaberite **Azure AI Search** s popisa rezultata.
4. Kliknite na gumb **Create**.
5. Na kartici **Basics** unesite sljedeće podatke:
   - **Subscription**: Odaberite vašu Azure pretplatu.
   - **Resource group**: Stvorite novu grupu resursa ili odaberite postojeću.
   - **Resource name**: Unesite jedinstveno ime za vašu pretraživačku uslugu.
   - **Region**: Odaberite regiju najbližu vašim korisnicima.
   - **Pricing tier**: Odaberite sloj cijena koji odgovara vašim potrebama. Za testiranje možete započeti s Free slojem.
6. Kliknite na **Review + create**.
7. Pregledajte postavke i kliknite **Create** za stvaranje pretraživačke usluge.

## Korak 3: Počnite raditi s Azure AI Search

1. Kad je implementacija dovršena, idite na vašu pretraživačku uslugu u Azure portalu.
2. U pregledu pretraživačke usluge kopirajte URL. Trebao bi izgledati kao `https://<service-name>.search.windows.net`.
3. **(Preporučeno)** Omogućite pristup bez ključa s Microsoft Entra ID (RBAC) kao što je prikazano u Koraku 4 u nastavku — nije potreban ključ. Primjeri u ovom vodiču stvaraju/ ažuriraju indekse i prenose dokumente, što zahtijeva uloge **Search Service Contributor** i **Search Index Data Contributor** (ili, za autentikaciju na ključ, **primary admin key** — ne query ključ). Ako ne možete koristiti RBAC, otvorite **Settings > Keys** i kopirajte **primary admin key**.
4. Slijedite korake u [Quickstart guide](https://learn.microsoft.com/azure/search/search-get-started-portal?pivots=import-data-new) stranici za stvaranje indeksa, prijenos podataka i izvođenje pretrage.

## Korak 4: Koristite Azure AI Search alate

Azure AI Search integrira se s raznim alatima za unaprjeđenje vaših pretraživačkih mogućnosti. Možete koristiti Azure CLI, Python SDK, .NET SDK i druge alate za napredne konfiguracije i operacije.

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
    # az search service show nema polje "endpoint"; izgradi URL iz naziva usluge.
    export AZURE_SEARCH_SERVICE_ENDPOINT="https://<service-name>.search.windows.net"
    ```

    Kad je RBAC omogućen, Python i .NET SDK primjeri u nastavku autentificiraju se koristeći `DefaultAzureCredential`, koji koristi vašu `az login` sesiju tijekom lokalnog razvoja — nije potreban administratorski ključ. Pogledajte [Connect to Azure AI Search using roles](https://learn.microsoft.com/azure/search/search-security-rbac).

4. **(Alternativa) Autentifikacija na ključ** — samo ako ne možete koristiti RBAC, spremite i administrativni ključ:

#### Spremite i endpoint i API ključ Azure AI Search instance u varijable okoline.

    ```bash
    # zsh/bash
    # az search service show nema "endpoint" polje; izgradite URL iz imena servisa.
    export AZURE_SEARCH_SERVICE_ENDPOINT="https://<service-name>.search.windows.net"
    export AZURE_SEARCH_API_KEY=$(az search admin-key show -g <resource-group> --service-name <service-name> --query "primaryKey" -o tsv)
    ```

    ```powershell
    # PowerShell
    # az search service show nema "endpoint" polje; izgradite URL iz imena servisa.
    $env:AZURE_SEARCH_SERVICE_ENDPOINT = "https://<service-name>.search.windows.net"
    $env:AZURE_SEARCH_API_KEY = $(az search admin-key show -g <resource-group> --service-name <service-name> --query "primaryKey" -o tsv)
    ```

### Korištenje Python SDK

1. Instalirajte Azure Cognitive Search klient biblioteku i Azure Identity za Python:

   ```bash
   pip install azure-search-documents azure-identity
   ```

2. Koristite sljedeći Python kod za stvaranje indeksa i prijenos dokumenata:

    ```python
    import os
    from azure.identity import DefaultAzureCredential
    from azure.search.documents import SearchClient
    from azure.search.documents.indexes import SearchIndexClient
    from azure.search.documents.indexes.models import SearchIndex, SimpleField, edm

    service_endpoint = os.getenv("AZURE_SEARCH_SERVICE_ENDPOINT")
    index_name = "sample-index"

    # Keyless (preporučeno): koristi vaš identitet `az login` putem Entra ID RBAC.
    # Zahtijeva uloge "Search Service Contributor" i "Search Index Data Contributor".
    credential = DefaultAzureCredential()
    # Rezervna opcija (autentifikacija na temelju ključa):
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

### Korištenje .NET SDK

1. Pokrenite sljedeću naredbu za stvaranje indeksa i prijenos dokumenata:

    ```bash
    dotnet run ./AzureSearch.cs
    ```

    .NET primjer u nastavku koristi `DefaultAzureCredential`, koji može koristiti vašu Azure CLI prijavu iz `az login` tijekom lokalnog razvoja.

2. Evo .NET koda datoteke `AzureSearch.cs`:

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

Uspješno ste postavili Azure AI Search koristeći Azure portal i integrirane alate. Sada možete istražiti naprednije značajke i mogućnosti Azure AI Search za unaprjeđenje vaših pretraživačkih rješenja.

Za dodatnu pomoć, posjetite [Azure Cognitive Search dokumentaciju](https://learn.microsoft.com/azure/search/?wt.mc_id=studentamb_258691).

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Napomena**:
Ovaj dokument je preveden korištenjem AI prevoditeljskog servisa [Co-op Translator](https://github.com/Azure/co-op-translator). Iako težimo točnosti, imajte na umu da automatski prijevodi mogu sadržavati greške ili netočnosti. Izvorni dokument na izvornom jeziku treba smatrati autoritativnim izvorom. Za važne informacije preporuča se profesionalni ljudski prijevod. Nismo odgovorni za bilo kakva nesporazumevanja ili pogrešne interpretacije koje proizlaze iz korištenja ovog prijevoda.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->