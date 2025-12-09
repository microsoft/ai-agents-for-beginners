<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "11e38db0898a788612b917e329dcdb5b",
  "translation_date": "2025-12-03T17:28:06+00:00",
  "source_file": "00-course-setup/AzureSearch.md",
  "language_code": "te"
}
-->
# Azure AI Search సెటప్ గైడ్

ఈ గైడ్ మీకు Azure పోర్టల్ ఉపయోగించి Azure AI Search సెటప్ చేయడంలో సహాయపడుతుంది. మీ Azure AI Search సేవను సృష్టించడానికి మరియు కాన్ఫిగర్ చేయడానికి క్రింది దశలను అనుసరించండి.

## ముందస్తు అవసరాలు

ప్రారంభించడానికి ముందు, మీ వద్ద ఈ క్రింది వాటి ఉనికి నిర్ధారించుకోండి:

- ఒక Azure సబ్‌స్క్రిప్షన్. మీ వద్ద Azure సబ్‌స్క్రిప్షన్ లేకపోతే, [Azure Free Account](https://azure.microsoft.com/free/?wt.mc_id=studentamb_258691) వద్ద ఉచిత ఖాతాను సృష్టించవచ్చు.

## దశ 1: Azure స్టోరేజ్ ఖాతాను సృష్టించండి

1. కొత్త Azure స్టోరేజ్ ఖాతాను సృష్టించడానికి ఈ సూచనను అనుసరించండి, [Create an Azure storage account](https://learn.microsoft.com/azure/storage/common/storage-account-create?tabs=azure-portal).
   **NOTE**: స్టోరేజ్ ఖాతా రకం Standard General Purpose V2 అని నిర్ధారించుకోండి.

## దశ 2: Azure AI Search సేవను సృష్టించండి

1. [Azure పోర్టల్](https://portal.azure.com/?wt.mc_id=studentamb_258691)లో సైన్ ఇన్ చేయండి.
2. ఎడమవైపు నావిగేషన్ ప్యానెల్‌లో **Create a resource** పై క్లిక్ చేయండి.
3. సెర్చ్ బాక్స్‌లో "Azure AI Search" అని టైప్ చేసి, ఫలితాల జాబితా నుండి **Azure AI Search** ను ఎంచుకోండి.
4. **Create** బటన్ పై క్లిక్ చేయండి.
5. **Basics** ట్యాబ్‌లో ఈ సమాచారం అందించండి:
   - **Subscription**: మీ Azure సబ్‌స్క్రిప్షన్‌ను ఎంచుకోండి.
   - **Resource group**: కొత్త రిసోర్స్ గ్రూప్‌ను సృష్టించండి లేదా ఉన్నదాన్ని ఎంచుకోండి.
   - **Resource name**: మీ సెర్చ్ సేవకు ప్రత్యేకమైన పేరు ఇవ్వండి.
   - **Region**: మీ వినియోగదారులకు దగ్గరగా ఉన్న ప్రాంతాన్ని ఎంచుకోండి.
   - **Pricing tier**: మీ అవసరాలకు అనుగుణంగా ప్రైసింగ్ టియర్‌ను ఎంచుకోండి. టెస్టింగ్ కోసం Free టియర్‌తో ప్రారంభించవచ్చు.
6. **Review + create** పై క్లిక్ చేయండి.
7. సెట్టింగులను సమీక్షించి, సెర్చ్ సేవను సృష్టించడానికి **Create** పై క్లిక్ చేయండి.

## దశ 3: Azure AI Search తో ప్రారంభించండి

1. డిప్లాయ్‌మెంట్ పూర్తయిన తర్వాత, Azure పోర్టల్‌లో మీ సెర్చ్ సేవకు వెళ్లండి.
2. సెర్చ్ సేవ అవలోకనం ప్యానెల్‌లో, URL కాపీ చేయండి. ఇది `https://<service-name>.search.windows.net` లాగా కనిపిస్తుంది.
3. Settings > Keys ప్యానెల్‌లో, క్వెరీ కీని కాపీ చేయండి.
4. [Quickstart guide](https://learn.microsoft.com/azure/search/search-get-started-portal?pivots=import-data-new) పేజీలో సూచించిన దశలను అనుసరించి, ఒక ఇండెక్స్ సృష్టించండి, డేటాను అప్‌లోడ్ చేయండి, మరియు సెర్చ్ క్వెరీని అమలు చేయండి.

## దశ 4: Azure AI Search టూల్స్ ఉపయోగించండి

Azure AI Search వివిధ టూల్స్‌తో ఇంటిగ్రేట్ అవుతుంది, ఇది మీ సెర్చ్ సామర్థ్యాలను మెరుగుపరుస్తుంది. మీరు Azure CLI, Python SDK, .NET SDK మరియు ఇతర టూల్స్‌ను అధునాతన కాన్ఫిగరేషన్లు మరియు ఆపరేషన్ల కోసం ఉపయోగించవచ్చు.

### Azure CLI ఉపయోగించడం

1. [Install Azure CLI](https://learn.microsoft.com/cli/azure/install-azure-cli?wt.mc_id=studentamb_258691) వద్ద సూచనలను అనుసరించి Azure CLIని ఇన్‌స్టాల్ చేయండి.
2. ఈ కమాండ్‌ను ఉపయోగించి Azure CLIలో సైన్ ఇన్ చేయండి:

   ```bash
   az login
   ```

3. Azure AI Search ఇన్‌స్టాన్స్ కోసం ఎండ్‌పాయింట్ మరియు API కీని ఎన్విరాన్‌మెంట్ వేరియబుల్స్‌లో నిల్వ చేయండి.

    ```bash
    # జెడ్‌ష్/బాష్
    export AZURE_SEARCH_SERVICE_ENDPOINT=$(az search service show -g <resource-group> -n <service-name> --query "endpoint" -o tsv)
    export AZURE_SEARCH_API_KEY=$(az search service admin-key list -g <resource-group> --search-service-name <service-name> --query "primaryKey" -o tsv)
    ```

    ```powershell
    # పవర్‌షెల్
    $env:AZURE_SEARCH_SERVICE_ENDPOINT = az search service show -g <resource-group> -n <service-name> --query "endpoint" -o tsv
    $env:AZURE_SEARCH_API_KEY = $(az search service admin-key list -g <resource-group> --search-service-name <service-name> --query "primaryKey" -o tsv)
    ```

### Python SDK ఉపయోగించడం

1. Python కోసం Azure Cognitive Search క్లయింట్ లైబ్రరీని ఇన్‌స్టాల్ చేయండి:

   ```bash
   pip install azure-search-documents
   ```

2. ఈ Python కోడ్‌ను ఉపయోగించి ఒక ఇండెక్స్ సృష్టించండి మరియు డాక్యుమెంట్లను అప్‌లోడ్ చేయండి:

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

### .NET SDK ఉపయోగించడం

1. ఈ కమాండ్‌ను అమలు చేసి ఒక ఇండెక్స్ సృష్టించండి మరియు డాక్యుమెంట్లను అప్‌లోడ్ చేయండి:

    ```bash
    dotnet run ./AzureSearch.cs
    ```

2. ఇక్కడ `AzureSearch.cs` యొక్క .NET కోడ్ ఉంది:

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

మరింత వివరమైన సమాచారం కోసం, ఈ డాక్యుమెంటేషన్‌ను చూడండి:

- [Create an Azure Cognitive Search service](https://learn.microsoft.com/azure/search/search-create-service-portal?wt.mc_id=studentamb_258691)
- [Get started with Azure Cognitive Search](https://learn.microsoft.com/azure/search/search-get-started-portal?wt.mc_id=studentamb_258691)
- [Azure AI Search Tools](https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-ai-search?tabs=azurecli%2Cpython&pivots=code-examples?wt.mc_id=studentamb_258691)

## ముగింపు

మీరు Azure పోర్టల్ మరియు ఇంటిగ్రేటెడ్ టూల్స్ ఉపయోగించి Azure AI Search ను విజయవంతంగా సెటప్ చేసారు. ఇప్పుడు మీరు Azure AI Search యొక్క అధునాతన ఫీచర్లు మరియు సామర్థ్యాలను అన్వేషించి మీ సెర్చ్ సొల్యూషన్లను మెరుగుపరచవచ్చు.

మరింత సహాయం కోసం, [Azure Cognitive Search documentation](https://learn.microsoft.com/azure/search/?wt.mc_id=studentamb_258691) ను సందర్శించండి.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**విమర్శ**:  
ఈ పత్రాన్ని AI అనువాద సేవ [Co-op Translator](https://github.com/Azure/co-op-translator) ఉపయోగించి అనువదించారు. మేము ఖచ్చితత్వానికి ప్రయత్నిస్తున్నప్పటికీ, ఆటోమేటెడ్ అనువాదాలలో తప్పులు లేదా అసమానతలు ఉండవచ్చు. దాని స్వదేశీ భాషలోని అసలు పత్రాన్ని అధికారం కలిగిన మూలంగా పరిగణించాలి. కీలకమైన సమాచారం కోసం, ప్రొఫెషనల్ మానవ అనువాదాన్ని సిఫారసు చేస్తాము. ఈ అనువాదాన్ని ఉపయోగించడం వల్ల కలిగే ఏవైనా అపార్థాలు లేదా తప్పుదారులు కోసం మేము బాధ్యత వహించము.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->