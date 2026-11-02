# Gabay sa Pag-set Up ng Azure AI Search

Tutulungan ka ng gabay na ito na i-set up ang Azure AI Search gamit ang Azure portal. Sundin ang mga hakbang sa ibaba upang lumikha at i-configure ang iyong Azure AI Search service.

## Mga Kinakailangan

Bago ka magsimula, siguraduhin mong mayroon ka ng mga sumusunod:

- Isang Azure subscription. Kung wala ka pang Azure subscription, maaari kang gumawa ng libreng account sa [Azure Free Account](https://azure.microsoft.com/free/?wt.mc_id=studentamb_258691).

## Hakbang 1: Lumikha ng Azure Storage Account

1. Sundin ang instruksiyon na ito, [Create an Azure storage account](https://learn.microsoft.com/azure/storage/common/storage-account-create?tabs=azure-portal), upang gumawa ng bagong Azure Storage Account.
   **TANDAAN**: Siguraduhing ang uri ng Storage Account ay Standard General Purpose V2.

## Hakbang 2: Lumikha ng Azure AI Search Service

1. Mag-sign in sa [Azure portal](https://portal.azure.com/?wt.mc_id=studentamb_258691).
2. Sa kaliwang navigation pane, i-click ang **Create a resource**.
3. Sa search box, i-type ang "Azure AI Search" at piliin ang **Azure AI Search** mula sa listahan ng mga resulta.
4. I-click ang **Create** button.
5. Sa **Basics** tab, ibigay ang mga sumusunod na impormasyon:
   - **Subscription**: Piliin ang iyong Azure subscription.
   - **Resource group**: Gumawa ng bagong resource group o piliin ang umiiral na isa.
   - **Resource name**: Maglagay ng natatanging pangalan para sa iyong search service.
   - **Region**: Piliin ang rehiyon na pinakamalapit sa iyong mga gumagamit.
   - **Pricing tier**: Piliin ang pricing tier na angkop sa iyong pangangailangan. Maaari kang magsimula sa Free tier para sa pagsubok.
6. I-click ang **Review + create**.
7. Suriin ang mga setting at i-click ang **Create** upang likhain ang search service.

## Hakbang 3: Simulan ang Paggamit ng Azure AI Search

1. Kapag natapos na ang deployment, pumunta sa iyong search service sa Azure portal.
2. Sa search service overview pane, kopyahin ang URL. Dapat itong mukhang `https://<service-name>.search.windows.net`.
3. **(Inirerekomenda)** Paganahin ang keyless access gamit ang Microsoft Entra ID (RBAC) tulad ng ipinapakita sa Hakbang 4 sa ibaba — hindi nangangailangan ng key. Ang mga halimbawa sa gabay na ito ay lumilikha/nag-a-update ng indexes at nag-upload ng mga dokumento, na nangangailangan ng mga role na **Search Service Contributor** at **Search Index Data Contributor** (o, para sa key-based auth, ang **primary admin key** — hindi ang query key). Kung hindi mo magagamit ang RBAC, buksan ang **Settings > Keys** pane at kopyahin ang **primary admin key**.
4. Sundan ang mga hakbang sa [Quickstart guide](https://learn.microsoft.com/azure/search/search-get-started-portal?pivots=import-data-new) na pahina upang gumawa ng index, mag-upload ng data, at magsagawa ng paghahanap.

## Hakbang 4: Gamitin ang Azure AI Search Tools

Ang Azure AI Search ay nagsasama-sama ng iba't ibang mga tool upang mapahusay ang iyong kakayahan sa paghahanap. Maaari mong gamitin ang Azure CLI, Python SDK, .NET SDK at iba pang mga tool para sa mas advanced na mga konfigurasyon at operasyon.

### Paggamit ng Azure CLI

1. I-install ang Azure CLI sa pamamagitan ng pagsunod sa mga instruksiyon sa [Install Azure CLI](https://learn.microsoft.com/cli/azure/install-azure-cli?wt.mc_id=studentamb_258691).
2. Mag-sign in sa Azure CLI gamit ang utos:

   ```bash
   az login
   ```
3. **(Inirerekomenda) Paganahin ang keyless access gamit ang Microsoft Entra ID (RBAC):**

    ```bash
    az search service update --name <service-name> --resource-group <resource-group> --auth-options aadOrApiKey
    az role assignment create --assignee <your-user-or-principal-id> --role "Search Service Contributor" --scope $(az search service show -g <resource-group> -n <service-name> --query id -o tsv)
    az role assignment create --assignee <your-user-or-principal-id> --role "Search Index Data Contributor" --scope $(az search service show -g <resource-group> -n <service-name> --query id -o tsv)
    # az search service show has no "endpoint" field; build the URL from the service name.
    export AZURE_SEARCH_SERVICE_ENDPOINT="https://<service-name>.search.windows.net"
    ```

    Sa pagkakaroon ng RBAC, ang mga halimbawa ng Python at .NET SDK sa ibaba ay nag-a-authenticate gamit ang `DefaultAzureCredential`, na gumagamit ng iyong `az login` session habang lokal na nagde-develop — hindi kailangan ng admin key. Tingnan ang [Connect to Azure AI Search using roles](https://learn.microsoft.com/azure/search/search-security-rbac).

4. **(Fallback) Key-based auth** — kung hindi mo magagamit ang RBAC, itago rin ang admin key:

#### Itago ang parehong endpoint at API key para sa Azure AI Search instance sa mga environment variable.

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

### Paggamit ng Python SDK

1. I-install ang Azure Cognitive Search client library at Azure Identity para sa Python:

   ```bash
   pip install azure-search-documents azure-identity
   ```

2. Gamitin ang sumusunod na Python code upang lumikha ng index at mag-upload ng mga dokumento:

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

### Paggamit ng .NET SDK

1. Patakbuhin ang sumusunod na utos upang lumikha ng index at mag-upload ng mga dokumento:

    ```bash
    dotnet run ./AzureSearch.cs
    ```

    Ang .NET sample sa ibaba ay gumagamit ng `DefaultAzureCredential`, na maaaring gamitin ang pag-sign in mo sa Azure CLI mula sa `az login` habang lokal na nagde-develop.

2. Narito ang .NET code ng `AzureSearch.cs`:

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

Para sa mas detalyadong impormasyon, sumangguni sa mga sumusunod na dokumentasyon:

- [Create an Azure Cognitive Search service](https://learn.microsoft.com/azure/search/search-create-service-portal?wt.mc_id=studentamb_258691)
- [Get started with Azure Cognitive Search](https://learn.microsoft.com/azure/search/search-get-started-portal?wt.mc_id=studentamb_258691)
- [Azure AI Search Tools](https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-ai-search?tabs=azurecli%2Cpython&pivots=code-examples?wt.mc_id=studentamb_258691)

## Konklusyon

Matagumpay mong na-set up ang Azure AI Search gamit ang Azure portal at mga pinagsamang tool. Maaari mo na ngayong tuklasin pa ang mga mas advanced na tampok at kakayahan ng Azure AI Search upang mapahusay ang iyong mga solusyon sa paghahanap.

Para sa karagdagang tulong, bisitahin ang [Azure Cognitive Search documentation](https://learn.microsoft.com/azure/search/?wt.mc_id=studentamb_258691).

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Pagtatanggi**:
Ang dokumentong ito ay isinalin gamit ang serbisyo ng AI translation na [Co-op Translator](https://github.com/Azure/co-op-translator). Bagama't nagsusumikap kami para sa katumpakan, pakatandaan na ang awtomatikong pagsasalin ay maaaring maglaman ng mga pagkakamali o hindi pagkakatugma. Ang orihinal na dokumento sa orihinal nitong wika ang dapat ituring na pangunahing sanggunian. Para sa mahahalagang impormasyon, inirerekomenda ang propesyonal na pagsasalin ng tao. Hindi kami mananagot sa anumang maling pagkakaintindi o maling interpretasyon na nagmula sa paggamit ng pagsasaling ito.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->