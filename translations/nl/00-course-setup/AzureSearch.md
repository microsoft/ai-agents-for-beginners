# Azure AI Search Setup Gids

Deze gids helpt u bij het instellen van Azure AI Search via het Azure-portaal. Volg de onderstaande stappen om uw Azure AI Search-service te maken en te configureren.

## Vereisten

Zorg voordat u begint dat u het volgende heeft:

- Een Azure-abonnement. Als u geen Azure-abonnement heeft, kunt u een gratis account aanmaken via [Azure Free Account](https://azure.microsoft.com/free/?wt.mc_id=studentamb_258691).

## Stap 1: Maak een Azure Storage-account aan

1. Volg deze instructie, [Maak een Azure storage-account aan](https://learn.microsoft.com/azure/storage/common/storage-account-create?tabs=azure-portal), om een nieuw Azure Storage-account te maken.
   **OPMERKING**: Zorg ervoor dat het type Storage-account Standaard General Purpose V2 is.

## Stap 2: Maak een Azure AI Search-service aan

1. Meld u aan bij het [Azure-portaal](https://portal.azure.com/?wt.mc_id=studentamb_258691).
2. Klik in het navigatievenster aan de linkerkant op **Resource maken**.
3. Typ in het zoekvak "Azure AI Search" en selecteer **Azure AI Search** uit de lijst met resultaten.
4. Klik op de knop **Maken**.
5. Vul in het tabblad **Basisgegevens** de volgende informatie in:
   - **Abonnement**: Selecteer uw Azure-abonnement.
   - **Resourcegroep**: Maak een nieuwe resourcegroep of selecteer een bestaande.
   - **Naam resource**: Voer een unieke naam in voor uw zoekservice.
   - **Regio**: Kies de regio die het dichtst bij uw gebruikers ligt.
   - **Prijslaag**: Kies een prijslaag die aan uw behoeften voldoet. U kunt beginnen met de Gratis-laag voor tests.
6. Klik op **Controleren + maken**.
7. Controleer de instellingen en klik op **Maken** om de zoekservice aan te maken.

## Stap 3: Aan de slag met Azure AI Search

1. Zodra de implementatie is voltooid, navigeert u naar uw zoekservice in het Azure-portaal.
2. Kopieer in het overzichtsscherm van de zoekservice de URL. Deze zou eruit moeten zien als `https://<service-name>.search.windows.net`.
3. **(Aanbevolen)** Schakel sleutelvrije toegang in met Microsoft Entra ID (RBAC) zoals hieronder in Stap 4 — geen sleutel nodig. De voorbeelden in deze gids maken indexen aan/bijwerken en uploaden documenten, dit vereist de rollen **Search Service Contributor** en **Search Index Data Contributor** (of bij sleutelgebaseerde verificatie de **primaire beheerderssleutel** — niet de query-sleutel). Alleen als u RBAC niet kunt gebruiken opent u het paneel **Instellingen > Sleutels** en kopieert u de **primaire beheerderssleutel**.
4. Volg de stappen in de [Quickstart-gids](https://learn.microsoft.com/azure/search/search-get-started-portal?pivots=import-data-new) om een index te maken, gegevens te uploaden en een zoekopdracht uit te voeren.

## Stap 4: Gebruik Azure AI Search Tools

Azure AI Search integreert met diverse tools om uw zoekmogelijkheden te verbeteren. U kunt Azure CLI, Python SDK, .NET SDK en andere tools gebruiken voor geavanceerde configuraties en bewerkingen.

### Gebruik van Azure CLI

1. Installeer de Azure CLI door de instructies te volgen op [Azure CLI installeren](https://learn.microsoft.com/cli/azure/install-azure-cli?wt.mc_id=studentamb_258691).
2. Meld u aan bij Azure CLI met het commando:

   ```bash
   az login
   ```
3. **(Aanbevolen) Schakel sleutelvrije toegang in met Microsoft Entra ID (RBAC):**

    ```bash
    az search service update --name <service-name> --resource-group <resource-group> --auth-options aadOrApiKey
    az role assignment create --assignee <your-user-or-principal-id> --role "Search Service Contributor" --scope $(az search service show -g <resource-group> -n <service-name> --query id -o tsv)
    az role assignment create --assignee <your-user-or-principal-id> --role "Search Index Data Contributor" --scope $(az search service show -g <resource-group> -n <service-name> --query id -o tsv)
    # az search service show heeft geen "endpoint" veld; bouw de URL op basis van de servicenaam.
    export AZURE_SEARCH_SERVICE_ENDPOINT="https://<service-name>.search.windows.net"
    ```

    Met ingeschakelde RBAC authenticeren de Python- en .NET SDK-voorbeelden hieronder met `DefaultAzureCredential`, wat uw `az login`-sessie tijdens lokale ontwikkeling gebruikt — geen beheerderssleutel nodig. Zie [Verbind met Azure AI Search met behulp van rollen](https://learn.microsoft.com/azure/search/search-security-rbac).

4. **(Fallback) Sleutelgebaseerde verificatie** — alleen als u RBAC niet kunt gebruiken, sla dan ook de beheerderssleutel op:

#### Sla zowel endpoint als API-sleutel voor Azure AI Search instantie op in omgevingsvariabelen.

    ```bash
    # zsh/bash
    # az search service show heeft geen "endpoint"-veld; bouw de URL op basis van de servicenaam.
    export AZURE_SEARCH_SERVICE_ENDPOINT="https://<service-name>.search.windows.net"
    export AZURE_SEARCH_API_KEY=$(az search admin-key show -g <resource-group> --service-name <service-name> --query "primaryKey" -o tsv)
    ```

    ```powershell
    # PowerShell
    # az search service show heeft geen "endpoint"-veld; bouw de URL op basis van de servicenaam.
    $env:AZURE_SEARCH_SERVICE_ENDPOINT = "https://<service-name>.search.windows.net"
    $env:AZURE_SEARCH_API_KEY = $(az search admin-key show -g <resource-group> --service-name <service-name> --query "primaryKey" -o tsv)
    ```

### Gebruik van Python SDK

1. Installeer de Azure Cognitive Search clientbibliotheek en Azure Identity voor Python:

   ```bash
   pip install azure-search-documents azure-identity
   ```

2. Gebruik de volgende Python-code om een index te maken en documenten te uploaden:

    ```python
    import os
    from azure.identity import DefaultAzureCredential
    from azure.search.documents import SearchClient
    from azure.search.documents.indexes import SearchIndexClient
    from azure.search.documents.indexes.models import SearchIndex, SimpleField, edm

    service_endpoint = os.getenv("AZURE_SEARCH_SERVICE_ENDPOINT")
    index_name = "sample-index"

    # Sleutelloos (aanbevolen): gebruikt je `az login` identiteit via Entra ID RBAC.
    # Vereist de rollen "Search Service Contributor" en "Search Index Data Contributor".
    credential = DefaultAzureCredential()
    # Terugval (sleutelgebaseerde authenticatie):
    # van azure.core.credentials importeer AzureKeyCredential
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

### Gebruik van .NET SDK

1. Voer het volgende commando uit om een index te maken en documenten te uploaden:

    ```bash
    dotnet run ./AzureSearch.cs
    ```

    Het .NET-voorbeeld hieronder gebruikt `DefaultAzureCredential`, wat uw Azure CLI-aanmelding met `az login` kan gebruiken tijdens lokale ontwikkeling.

2. Hier is de .NET-code van `AzureSearch.cs`:

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

Voor meer gedetailleerde informatie, raadpleeg de volgende documentatie:

- [Maak een Azure Cognitive Search service aan](https://learn.microsoft.com/azure/search/search-create-service-portal?wt.mc_id=studentamb_258691)
- [Aan de slag met Azure Cognitive Search](https://learn.microsoft.com/azure/search/search-get-started-portal?wt.mc_id=studentamb_258691)
- [Azure AI Search Tools](https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-ai-search?tabs=azurecli%2Cpython&pivots=code-examples?wt.mc_id=studentamb_258691)

## Conclusie

U heeft Azure AI Search succesvol ingesteld via het Azure-portaal en geïntegreerde tools. U kunt nu meer geavanceerde functies en mogelijkheden van Azure AI Search verkennen om uw zoekoplossingen te verbeteren.

Voor verdere hulp, bezoek de [Azure Cognitive Search documentatie](https://learn.microsoft.com/azure/search/?wt.mc_id=studentamb_258691).

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:
Dit document is vertaald met behulp van de AI vertaaldienst [Co-op Translator](https://github.com/Azure/co-op-translator). Hoewel we streven naar nauwkeurigheid, dient u er rekening mee te houden dat geautomatiseerde vertalingen fouten of onnauwkeurigheden kunnen bevatten. Het originele document in de oorspronkelijke taal moet worden beschouwd als de gezaghebbende bron. Voor kritieke informatie wordt professionele menselijke vertaling aanbevolen. Wij zijn niet aansprakelijk voor eventuele misverstanden of verkeerde interpretaties die voortvloeien uit het gebruik van deze vertaling.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->