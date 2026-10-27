# ఆజ్యూర్ ఎ.ఐ. సెర్చ్ సెటప్ గైడ్

ఈ గైడ్ మీకు ఆజ్యూర్ పోర్టల్ ఉపయోగించి ఆజ్యూర్ ఎ.ఐ. సెర్చ్ ను సెటప్ చేయడంలో సహాయం చేస్తుంది. మీ ఆజ్యూర్ ఎ.ఐ. సెర్చ్ సేవని సృష్టించి కాంఫిగర్ చేసుకోవడానికి దిగువ సూచనలను అనుసరించండి.

## మునుపటి అవసరాలు

మీరు ప్రారంభించడానికి ముందుగా, మీ దగ్గర ఈ క్రింది వాటి ఉండాలి:

- ఆజ్యూర్ సబ్‌స్క్రిప్షన్. మీరు ఆజ్యూర్ సబ్‌స్క్రిప్షన్ లేని సందర్భంలో, మీరు ఇక్కడ [Azure Free Account](https://azure.microsoft.com/free/?wt.mc_id=studentamb_258691) ఒక ఉచిత ఖాతాను సృష్టించవచ్చు.

## దశ 1: ఆజ్యూర్ స్టోరేజ్ అకౌంట్ సృష్టించండి

1. ఆజ్యూర్ స్టోరేజ్ అకౌంట్ సృష్టించడానికి ఈ సూచన, [Create an Azure storage account](https://learn.microsoft.com/azure/storage/common/storage-account-create?tabs=azure-portal) ను అనుసరించండి.
   **గమనిక**: స్టోరేజ్ అకౌంట్ రకం Standard General Purpose V2 గా ఉండాలని నిర్ధారించుకోండి.

## దశ 2: ఆజ్యూర్ ఎ.ఐ. సెర్చ్ సేవ సృష్టించండి

1. [Azure portal](https://portal.azure.com/?wt.mc_id=studentamb_258691) లో సైన్ ఇన్ అవ్వండి.
2. ఎడమ వైపు నావిగేషన్ ప్యానెల్లో, **Create a resource** పై క్లిక్ చేయండి.
3. సెర్చ్ బాక్స్ లో "Azure AI Search" టైప్ చేసి ఫలితాల్లోనుంచి **Azure AI Search** ను ఎంచుకోండి.
4. **Create** బటన్ పై క్లిక్ చేయండి.
5. **Basics** టాబ్ లో, ఈ సమాచారం అందించండి:
   - **Subscription**: మీ ఆజ్యూర్ సబ్‌స్క్రిప్షన్ ను ఎంచుకోండి.
   - **Resource group**: కొత్త రిసోర్స్ గ్రూపు సృష్టించండి లేదా ఉన్నదానిని ఎంచుకోండి.
   - **Resource name**: మీ సెర్చ్ సేవకు ఒక ప్రత్యేకమైన పేరు నమోదు చేయండి.
   - **Region**: మీ వినియోగదారులకు సన్నిహిత ప్రాంతాన్ని ఎంచుకోండి.
   - **Pricing tier**: మీ అవసరాలకు తగిన ధరల స్థాయిని ఎంచుకోండి. పరీక్షల కోసం మీరు ఫ్రీ టియర్ ప్రారంభించవచ్చు.
6. **Review + create** పై క్లిక్ చేయండి.
7. సెట్టింగ్స్ ను సమీక్షించి, సెర్చ్ సేవను సృష్టించడానికి **Create** పై క్లిక్ చేయండి.

## దశ 3: ఆజ్యూర్ ఎ.ఐ. సెర్చ్ తో ప్రారంభించండి

1. డిప్లాయ్‌మెంట్ పూర్తయిన తర్వాత, ఆజ్యూర్ పోర్టల్ లో మీ సెర్చ్ సేవ వైపు నావిగేట్ అవ్వండి.
2. సెర్చ్ సేవా అవలోకన ప్యానెల్లో, URL కాపీ చేసుకోండి. ఇది `https://<service-name>.search.windows.net` లాగా కనిపించాలి.
3. **(నిర్మాణ సూచన)** మైక్రోసాఫ్ట్ ఎంట్రా ఐడి (RBAC)తో కీ లేని యాక్సెస్ ను క్రింది దశ 4 లో చూపిన విధంగా సక్రియం చేయండి — కీ అవసరం లేదు. ఈ గైడ్ లోని ఉదాహరణలు సూచికలను సృష్టించడం/అప్‌డేట్ చేయడం మరియు డాక్యుమెంట్లు అప్లోడ్ చేయడం చేయడంతో మీకు **Search Service Contributor** మరియు **Search Index Data Contributor** పాత్రలు (లేదా కీ ఆధారిత ఆథ్ కోసం, ప్రధాన అడ్మిన్ కీ — క్వెరీ కీ కాదు) అవసరం ఉంటుంది. మీరు RBAC ఉపయోగించలేనప్పుడు మాత్రమే **Settings > Keys** ప్యానెల్ తెరిచి **primary admin key** ను కాపీ చేసుకోండి.
4. సూచికను సృష్టించడానికి, డేటా అప్లోడ్ చేయడానికి మరియు సెర్చ్ నిర్వహించడానికి [Quickstart guide](https://learn.microsoft.com/azure/search/search-get-started-portal?pivots=import-data-new) పేజీలో సూచనలు అనుసరించండి.

## దశ 4: ఆజ్యూర్ ఎ.ఐ. సెర్చ్ టూల్స్ ఉపయోగించండి

ఆజ్యూర్ ఎ.ఐ. సెర్చ్ వివిధ టూల్స్ తో ఒకీకరించబడింది, ఇది మీ సెర్చ్ సామర్థ్యాలను మెరుగుపరుస్తుంది. మీరు అభివృద్ధి చేసిన కాంఫిగరేషన్లు మరియు ఆపరేషన్ల కొరకు Azure CLI, Python SDK, .NET SDK మరియు ఇతర టూల్స్ ను ఉపయోగించవచ్చు.

### Azure CLI ఉపయోగించడం

1. [Install Azure CLI](https://learn.microsoft.com/cli/azure/install-azure-cli?wt.mc_id=studentamb_258691) వద్ద సూచనలు అనుసరించి Azure CLI ఇన్స్టాల్ చేయండి.
2. క్రింది కమాండ్ తో Azure CLI లో సైన్ ఇన్ అవ్వండి:

   ```bash
   az login
   ```
3. **(నిర్మాణ సూచన) మైక్రోసాఫ్ట్ ఎంట్రా ఐడి (RBAC) తో కీ లేని యాక్సెస్ సక్రియం చేయండి:**

    ```bash
    az search service update --name <service-name> --resource-group <resource-group> --auth-options aadOrApiKey
    az role assignment create --assignee <your-user-or-principal-id> --role "Search Service Contributor" --scope $(az search service show -g <resource-group> -n <service-name> --query id -o tsv)
    az role assignment create --assignee <your-user-or-principal-id> --role "Search Index Data Contributor" --scope $(az search service show -g <resource-group> -n <service-name> --query id -o tsv)
    # az search service show has no "endpoint" field; build the URL from the service name.
    export AZURE_SEARCH_SERVICE_ENDPOINT="https://<service-name>.search.windows.net"
    ```

    RBAC సక్రియం అయితే, కింద చూపిన Python మరియు .NET SDK ఉదాహరణలు `DefaultAzureCredential` తో అనుమతి పొందతాయి, ఇది మీ `az login` సెషన్ ను లోకల్ డెవలప్‌మెంట్ సమయంలో ఉపయోగిస్తుంది — అడ్మిన్ కీ అవసరం లేదు. [Connect to Azure AI Search using roles](https://learn.microsoft.com/azure/search/search-security-rbac) చూడండి.

4. **(ప్రత్యామ్నాయం) కీ ఆధారిత ఆథ్** — మీరు RBAC ఉపయోగించలేనప్పుడు మాత్రమే, అడ్మిన్ కీ కూడా భద్రపరచండి:

#### ఆజ్యూర్ ఎ.ఐ. సెర్చ్ ఇన్‌స్టాన్స్ ను పర్యావరణ వేరియబుల్‌లుగా ఎండ్పాయింట్ మరియు API కీ ని రెండునీ నిల్వ చేయండి.

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

### Python SDK ఉపయోగించడం

1. Azure Cognitive Search క్లయింట్ లైబ్రరీ మరియు Azure Identity అనుసంధానించిన Python ఇన్స్టాల్ చేయండి:

   ```bash
   pip install azure-search-documents azure-identity
   ```

2. ఒక సూచికను సృష్టించి డాక్యుమెంట్లను అప్లోడ్ చేయడానికి క్రింది Python కోడ్ ఉపయోగించండి:

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

### .NET SDK ఉపయోగించడం

1. సూచికను సృష్టించి డాక్యుమెంట్లను అప్లోడ్ చేయడానికి క్రింది కమాండ్ నడపండి:

    ```bash
    dotnet run ./AzureSearch.cs
    ```

    క్రింది .NET ఉదాహరణలు `DefaultAzureCredential` ఉపయోగిస్తుంది, ఇది లోకల్ డెవలప్‌మెంట్ సమయంలో మీ ఆజ్యూర్ CLI సైన్-ఇన్‌ను `az login` నుండి ఉపయోగించవచ్చు.

2. క్రింద ఇవ్వబడినది `AzureSearch.cs` యొక్క .NET కోడ్:

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

మరింత వివరమైన సమాచారం కోసం, ఈ క్రింది డాక్యుమెంటేషన్‌ను చూడండి:

- [Create an Azure Cognitive Search service](https://learn.microsoft.com/azure/search/search-create-service-portal?wt.mc_id=studentamb_258691)
- [Get started with Azure Cognitive Search](https://learn.microsoft.com/azure/search/search-get-started-portal?wt.mc_id=studentamb_258691)
- [Azure AI Search Tools](https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-ai-search?tabs=azurecli%2Cpython&pivots=code-examples?wt.mc_id=studentamb_258691)

## ముగింపు

మీరు ఆజ్యూర్ పోర్టల్ మరియు సంపూర్ణ టూల్స్ ఉపయోగించి విజయవంతంగా ఆజ్యూర్ ఎ.ఐ. సెర్చ్ సెటప్ చేసుకున్నారు. మీరు ఇప్పుడు ఆజ్యూర్ ఎ.ఐ. సెర్చ్ యొక్క మరిన్ని అభివృద్ధి చెందిన లక్షణాలు మరియు సామర్థ్యాలను పరిశీలించి మీ సెర్చ్ పరిష్కారాలను మెరుగుపరచవచ్చు.

మరింత సహాయానికి, [Azure Cognitive Search documentation](https://learn.microsoft.com/azure/search/?wt.mc_id=studentamb_258691) సందర్శించండి.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**అస్వీకరణ**:
ఈ పత్రం AI అనువాద సేవ [Co-op Translator](https://github.com/Azure/co-op-translator) ఉపయోగించి అనువదించబడింది. మేము ఖచ్చితత్వానికి ప్రయత్నిస్తున్నప్పటికీ, ఆటోమేటెడ్ అనువాదాలు తప్పులు లేదా అసమగ్రతలను కలిగి ఉండవచ్చు. దాని స్వదేశ భాషలో ఉన్న అసలు పత్రాన్ని అధికారం కలిగిన మూలంగా పరిగణించాలి. కీలకమైన సమాచారం కోసం, ప్రొఫెషనల్ మానవ అనువాదాన్ని సిఫారసు చేస్తాము. ఈ అనువాదం ఉపయోగం వల్ల కలిగే ఏవైనా అపార్థాలు లేదా తప్పుదారులు కోసం మేము బాధ్యత వహించము.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->