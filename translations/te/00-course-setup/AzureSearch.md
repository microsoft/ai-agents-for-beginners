# Azure AI సెర్చ్ సెటప్ గైడ్

ఈ గైడ్ Azure పోర్టల్ ఉపయోగించి Azure AI సెర్చ్‌ను సెట్ చేయటానికి సహాయపడుతుంది. మీ Azure AI సెర్చ్ సర్వీస్‌ను సృష్టించి కాన్ఫిగర్ చేయడానికి కింది దశలను అనుసరించండి.

## ముందుగా అవసరమైనవి

మీరు ప్రారంభించే ముందు, మీరు ఈ క్రింది వాటిని కలిగి ఉందని నిర్ధారించుకోండి:

- ఒక Azure సబ్‌స్క్రిప్షన్. మీ వద్ద Azure సబ్‌స్క్రిప్షన్ లేకపోతే, మీరు [Azure Free Account](https://azure.microsoft.com/free/?wt.mc_id=studentamb_258691) వద్ద ఉచిత ఖాతా సృష్టించవచ్చు.

## దశ 1: Azure స్టోరేజ్ ఖాతా సృష్టించండి

1. ఈ సూచనను అనుసరించండి, [Create an Azure storage account](https://learn.microsoft.com/azure/storage/common/storage-account-create?tabs=azure-portal), కొత్త Azure స్టోరేజ్ ఖాతాను సృష్టించడానికి.
   **గమనిక**: స్టోరేజ్ ఖాతా రకం Standard General Purpose V2 గా ఉన్నదని నిర్ధారించండి.

## దశ 2: Azure AI సెర్చ్ సర్వీస్ సృష్టించండి

1. [Azure portal](https://portal.azure.com/?wt.mc_id=studentamb_258691) లో సైన్ ఇన్ అవ్వండి.
2. ఎడమవైపున ఉన్న నావిగేషన్ ప్యానెల్‌లో, **Create a resource** పై క్లిక్ చేయండి.
3. సెర్చ్ బాక్స్‌లో "Azure AI Search" టైప్ చేసి ఫలితాల జాబితాలో నుండి **Azure AI Search** ను ఎంచుకోండి.
4. **Create** బటన్‌పై క్లిక్ చేయండి.
5. **Basics** టాబ్‌లో, క్రింది సమాచారం అందించండి:
   - **Subscription**: మీ Azure సబ్‌స్క్రిప్షన్ ను ఎంచుకోండి.
   - **Resource group**: కొత్త రిసోర్స్ గ్రూప్ సృష్టించండి లేదా ఉన్నదిలోంచి ఎంచుకోండి.
   - **Resource name**: మీ సెర్చ్ సర్వీస్ కొరకు ప్రత్యేకమైన పేరును నమోదు చేయండి.
   - **Region**: మీ వినియోగదారులకు అత్యంత సమీపమైన ప్రాంతాన్ని ఎంచుకోండి.
   - **Pricing tier**: మీ అవసరాలకు తగిన ధరా తరగతిని ఎంచుకోండి. మీరు పరీక్షల కోసం ఉచిత తరగతితో మొదలు పెట్టవచ్చు.
6. **Review + create** పై క్లిక్ చేయండి.
7. సెట్టింగ్స్ సమీక్షించి **Create** పై క్లిక్ చేసి సెర్చ్ సర్వీస్‌ను సృష్టించండి.

## దశ 3: Azure AI సెర్చ్‌తో ప్రారంభించండి

1. డిప్లాయ్‌మెంట్ పూర్తి అయిన వెంటనే, Azure పోర్టల్‌లో మీ సెర్చ్ సర్వీస్‌కు వెళ్లండి.
2. సెర్చ్ సర్వీస్ అవలోకన ప్యానెల్‌లో, URL ను కాపీ చేసుకోండి. ఇది `https://<service-name>.search.windows.net` వంటి దృశ్యమవుతుంటుంది.
3. **(సిఫార్సు)** కీ లేకుండా Microsoft Entra ID (RBAC)తో యాక్సెస్‌ను ప్రారంభించండి (దశ 4 లో చూపినట్లు) — ఏ కీ అవసరం లేదు. ఈ గైడ్‌లోని ఉదాహరణలు ఇండెక్స్‌లను సృష్టించటం/నవీకరించడం మరియు డాక్యుమెంట్లను అప్‌లోడ్ చేయడం చేస్తాయి, వీటికి **Search Service Contributor** మరియు **Search Index Data Contributor** పాత్రలు అవసరం అవుతాయి (లేదా కీ ఆధారితన్నప్పుడు, **ప్రధాన అడ్మిన్ కీ** అవసరం — క్వెరీ కీ కాదు). మీరు RBAC ఉపయోగించలేకపోతే మాత్రమే **Settings > Keys** ప్యానెల్ తెరవండి మరియు **ప్రధాన అడ్మిన్ కీ** ను కాపీ చేసుకోండి.
4. [Quickstart guide](https://learn.microsoft.com/azure/search/search-get-started-portal?pivots=import-data-new) పేజీలో ఇచ్చిన దశలను ಅನುసరించి ఇండెక్స్ సృష్టించండి, డేటా అప్‌లోడ్ చేయండి మరియు సెర్చ్ నిర్వహించండి.

## దశ 4: Azure AI సెర్చ్ టూల్స్ ఉపయోగించండి

Azure AI సెర్చ్ వివిధ టూల్స్‌తో సమగ్రంగా పని చేస్తుంది, ఇది మీ సెర్చ్ సామర్థ్యాలను మెరుగుపరుస్తుంది. మీరు Azure CLI, Python SDK, .NET SDK మరియు ఇతర టూల్స్‌ను ఆధునిక కాన్ఫిగరేషన్లు మరియు ఆపరేషన్ల కోసం ఉపయోగించవచ్చు.

### Azure CLI ఉపయోగించడం

1. [Install Azure CLI](https://learn.microsoft.com/cli/azure/install-azure-cli?wt.mc_id=studentamb_258691) వద్ద ఇచ్చిన సూచనలను అనుసరించి Azure CLIని ఇన్‌స్టాల్ చేసుకోండి.
2. ఈ కమాండ్ ఉపయోగించి Azure CLIలో సైన్ ఇన్ అవ్వండి:

   ```bash
   az login
   ```
3. **(సిఫార్సు) Microsoft Entra ID (RBAC)తో కీ లేకుండా యాక్సెస్ ప్రారంభించండి:**

    ```bash
    az search service update --name <service-name> --resource-group <resource-group> --auth-options aadOrApiKey
    az role assignment create --assignee <your-user-or-principal-id> --role "Search Service Contributor" --scope $(az search service show -g <resource-group> -n <service-name> --query id -o tsv)
    az role assignment create --assignee <your-user-or-principal-id> --role "Search Index Data Contributor" --scope $(az search service show -g <resource-group> -n <service-name> --query id -o tsv)
    # az search service ప్రదర్శనలో "endpoint" ఫీల్డ్ లేదు; సర్వీస్ పేరునుండి URL ను నిర్మించండి.
    export AZURE_SEARCH_SERVICE_ENDPOINT="https://<service-name>.search.windows.net"
    ```

    RBAC ప్రారంభించబడిన వేపు, క్రింది Python మరియు .NET SDK ఉదాహరణలు `DefaultAzureCredential`తో ధృవీకరణ చేస్తాయి, ఇది స్థానిక అభివృద్ధిలో మీ `az login` సెషన్‌ను ఉపయోగిస్తుంది — ఎటువంటి అడ్మిన్ కీ అవసరం లేదు. [Connect to Azure AI Search using roles](https://learn.microsoft.com/azure/search/search-security-rbac) చూడండి.

4. **(ప్రత్యామ్నాయం) కీ ఆధారిత ధృవీకరణ** — మీరు RBAC ఉపయోగించలేకపోతే మాత్రమే, అడ్మిన్ కీ కూడా నిల్వ చేయండి:

#### Azure AI సెర్చ్ ఇన్స్టెన్స్ కొరకు ఎండ్పాయింట్ మరియు API కీని ఎన్విరాన్‌మెంట్ వేరియబుల్స్‌గా నిల్వ చేయండి.

    ```bash
    # zsh/bash
    # az search service showకు "endpoint" ఫీల్డ్ లేదు; సేవా పేరుతో URL నిర్మించండి.
    export AZURE_SEARCH_SERVICE_ENDPOINT="https://<service-name>.search.windows.net"
    export AZURE_SEARCH_API_KEY=$(az search admin-key show -g <resource-group> --service-name <service-name> --query "primaryKey" -o tsv)
    ```

    ```powershell
    # PowerShell
    # az search service showకు "endpoint" ఫీల్డ్ లేదు; సేవా పేరుతో URL నిర్మించండి.
    $env:AZURE_SEARCH_SERVICE_ENDPOINT = "https://<service-name>.search.windows.net"
    $env:AZURE_SEARCH_API_KEY = $(az search admin-key show -g <resource-group> --service-name <service-name> --query "primaryKey" -o tsv)
    ```

### Python SDK ఉపయోగించడం

1. Azure Cognitive Search క్లయింట్ లైబ్రరీ మరియు Python కోసం Azure Identity ఇన్‌స్టాల్ చేయండి:

   ```bash
   pip install azure-search-documents azure-identity
   ```

2. క్రింది Python కోడ్‌ను ఉపయోగించి ఇండెక్స్ సృష్టించి డాక్యుమెంట్లను అప్‌లోడ్ చేయండి:

    ```python
    import os
    from azure.identity import DefaultAzureCredential
    from azure.search.documents import SearchClient
    from azure.search.documents.indexes import SearchIndexClient
    from azure.search.documents.indexes.models import SearchIndex, SimpleField, edm

    service_endpoint = os.getenv("AZURE_SEARCH_SERVICE_ENDPOINT")
    index_name = "sample-index"

    # కీ లేకుండా (推ार్తహమైనది): Entra ID RBAC ద్వారా మీ `az login` గుర్తింపు ఉపయోగిస్తుంది.
    # "Search Service Contributor" మరియు "Search Index Data Contributor" పాత్రల అవసరం.
    credential = DefaultAzureCredential()
    # ఫాల్బ్యాక్ (కీ ఆధారిత గుర్తింపు):
    # azure.core.credentials నుండి AzureKeyCredential ను దిగుమతి చేసుకోండి
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

1. ఇండెక్స్ సృష్టించడానికి మరియు డాక్యుమెంట్లను అప్‌లోడ్ చేయడానికి ఈ క్రింది కమాండ్‌ను నడపండి:

    ```bash
    dotnet run ./AzureSearch.cs
    ```

    క్రింద ఉన్న .NET ఉదాహరణ `DefaultAzureCredential` ఉపయోగిస్తుంది, ఇది స్థానిక అభివృద్ధి సమయంలో `az login` ద్వారా Azure CLI సైన్-ఇన్ ఉపయోగించవచ్చు.

2. ఇది `AzureSearch.cs` యొక్క .NET కోడ్:

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

మరిన్ని వివరాలు కోసం ఈ క్రింది డాక్యుమెంటేషన్‌ను చూడండి:

- [Create an Azure Cognitive Search service](https://learn.microsoft.com/azure/search/search-create-service-portal?wt.mc_id=studentamb_258691)
- [Get started with Azure Cognitive Search](https://learn.microsoft.com/azure/search/search-get-started-portal?wt.mc_id=studentamb_258691)
- [Azure AI Search Tools](https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-ai-search?tabs=azurecli%2Cpython&pivots=code-examples?wt.mc_id=studentamb_258691)

## ముగింపు

మీరు Azure పోర్టల్ మరియు సమగ్ర టూల్స్ ఉపయోగించి విజయవంతంగా Azure AI సెర్చ్ సెట్ చేసుకున్నారు. ఇప్పుడు మీరు మీ సెర్చ్ పరిష్కారాలను మెరుగుపరచడానికి Azure AI సెర్చ్ యొక్క మెరుగైన ఫీచర్లను పరిశీలించవచ్చు.

మరిన్ని సహాయం కొరకు [Azure Cognitive Search documentation](https://learn.microsoft.com/azure/search/?wt.mc_id=studentamb_258691) సందర్శించండి.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**అస్వీకరణ**:
ఈ పత్రం AI అనువాద సేవ [Co-op Translator](https://github.com/Azure/co-op-translator) ఉపయోగించి అనువదించబడింది. మేము ఖచ్చితత్వానికి ప్రయత్నిస్తున్నప్పటికీ, ఆటోమేటెడ్ అనువాదాలు తప్పులు లేదా అసమగ్రతలను కలిగి ఉండవచ్చు. దాని స్వదేశ భాషలో ఉన్న అసలు పత్రాన్ని అధికారం కలిగిన మూలంగా పరిగణించాలి. కీలకమైన సమాచారం కోసం, ప్రొఫెషనల్ మానవ అనువాదాన్ని సిఫారసు చేస్తాము. ఈ అనువాదం ఉపయోగం వల్ల కలిగే ఏవైనా అపార్థాలు లేదా తప్పుదారులు కోసం మేము బాధ్యత వహించము.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->