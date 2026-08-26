# Azure AI Search సెటప్ గైడ్

Azure పోర్టల్ ఉపయోగించి Azure AI Search ను సెటప్ చేయడానికి ఈ గైడ్ మీకు సహాయ పడుతుంది. కింద పేర్కొన్న దశలను అనుసరించి మీ Azure AI Search సేవని సృష్టించి కాన్ఫిగర్ చేయండి.

## ముందస్తు అవసరాలు

మీరు ప్రారంభించే ముందు, కింది వాటి కలిగి ఉన్నారో నిర్ధారించుకోండి:

- ఒక Azure సబ్‌స్క్రిప్షన్. మీకు Azure సబ్‌స్క్రిప్షన్ లేకపోతే, మీరు [Azure Free Account](https://azure.microsoft.com/free/?wt.mc_id=studentamb_258691) వద్ద ఉచిత ఖాతా సృష్టించవచ్చు.

## దశ 1: Azure స్టోరేజ్ ఖాతా సృష్టించండి

1. కొత్త Azure స్టోరేజ్ అకౌంట్ సృష్టించడానికి [Create an Azure storage account](https://learn.microsoft.com/azure/storage/common/storage-account-create?tabs=azure-portal) సూచనలను అనుసరించండి.
   **గమనిక**: స్టోరేజ్ అకౌంట్ రకం Standard General Purpose V2 అయ్యేలా చూసుకోండి.

## దశ 2: Azure AI Search సేవ సృష్టించండి

1. [Azure పోర్టల్](https://portal.azure.com/?wt.mc_id=studentamb_258691)లో సైన్ ఇన్ అవ్వండి.
2. ఎడమవైపు నావిగేషన్ ప్యానెల్లో, **Create a resource** క్లిక్ చేయండి.
3. శోధన బాక్స్ లో "Azure AI Search" టైప్ చేసి, ఫలితాల జాబితాలో **Azure AI Search** ను ఎంచుకోండి.
4. **Create** బటన్ క్లిక్ చేయండి.
5. **Basics** టాబ్ లో కిందివి అందించండి:
   - **Subscription**: మీ Azure సబ్‌స్క్రిప్షన్ ఎంచుకోండి.
   - **Resource group**: కొత్త రిసోర్స్ గ్రూప్ సృష్టించండి లేదా ప్రస్తుతాన్ని ఎంచుకోండి.
   - **Resource name**: మీ సెర్చ్ సర్వీస్ కు ప్రత్యేకమైన పేరు ఇవ్వండి.
   - **Region**: మీ వినియోగదారులకు దగ్గరగా ఉన్న ప్రాంతాన్ని ఎంచుకోండి.
   - **Pricing tier**: మీ అవసరాలకు దక్కబడే ధర స్థాయిని ఎంచుకోండి. పరీక్షల కోసమైతే Free tier తో ప్రారంభించవచ్చు.
6. **Review + create** క్లిక్ చేయండి.
7. సెట్టింగ్లను సమీక్షించి, సెర్చ్ సర్వీస్ సృష్టించడానికి **Create** క్లిక్ చేయండి.

## దశ 3: Azure AI Search ప్రారంభించండి

1. డిప్లాయ్‌మెంట్ పూర్తయిన వెంటనే, Azure పోర్టల్‌లో మీ సెర్చ్ సేవకి వెళ్ళండి.
2. సెర్చ్ సర్వీస్ ఓవర్వ్యూ ప్యానెల్లో URL ను కాపీ చేసుకోండి. ఇది `https://<service-name>.search.windows.net` లాగా కనిపించాలి.
3. **(సిఫార్సు చేయబడింది)** Microsoft Entra ID (RBAC)తో కీసు లేని యాక్సెస్ ను క్రింది దశ 4 లో చూపిన విధంగా ఎనేబుల్ చేయండి — కీ అవసరం లేదు. ఈ గైడ్ లోని నమూనాలు సూచికలు సృష్టించడం/నవీకరించడం మరియు డాక్యుమెంట్లు అప్లోడ్ చేయడం అవసరం, అందుకు **Search Service Contributor** మరియు **Search Index Data Contributor** పాత్రలు అవసరం (లేదా, కీ ఆధారిత అనుమతికి, **ప్రైమరీ అడ్మిన్ కీ** — క్వరి కీ కాదు). మీరు RBAC ఉపయోగించలేకపోతే मात्रै, **Settings > Keys** ప్యానెల్ ఓపెన్ చేసి **primary admin key** ను కాపీ చేసుకోండి.
4. సూచిక సృష్టించడానికి, డాటా అప్లోడ్ చేయడానికి మరియు సెర్చ్ నిర్వహించడానికి [Quickstart guide](https://learn.microsoft.com/azure/search/search-get-started-portal?pivots=import-data-new)లో ఉన్న దశల్ని అనుసరించండి.

## దశ 4: Azure AI Search టూల్స్ ఉపయోగించండి

Azure AI Search వివిధ టూల్స్‌తో ఇంటిగ్రేట్ చేయబడి, మీ సెర్చ్ సామర్థ్యాలను మెరుగుపరుస్తుంది. మీరు Azure CLI, Python SDK, .NET SDK మరియు ఇతర టూల్స్ ఉపయోగించి అభివృద్ది కాన్ఫిగరేషన్లు మరియు ఆపరేషన్లు నిర్వహించవచ్చు.

### Azure CLI ఉపయోగించడం

1. [Install Azure CLI](https://learn.microsoft.com/cli/azure/install-azure-cli?wt.mc_id=studentamb_258691) వద్ద ఇచ్చిన సూచనలను అనుసరించి Azure CLI ను ఇన్‌స్టాల్ చేయండి.
2. క్రింది క‌మాండ్ తో Azure CLI లో సైన్ ఇన్ అవ్వండి:

   ```bash
   az login
   ```
3. **(సిఫార్సు) Microsoft Entra ID (RBAC)తో కీసు లేని యాక్సెస్ ఎనేబుల్ చేయండి:**

    ```bash
    az search service update --name <service-name> --resource-group <resource-group> --auth-options aadOrApiKey
    az role assignment create --assignee <your-user-or-principal-id> --role "Search Service Contributor" --scope $(az search service show -g <resource-group> -n <service-name> --query id -o tsv)
    az role assignment create --assignee <your-user-or-principal-id> --role "Search Index Data Contributor" --scope $(az search service show -g <resource-group> -n <service-name> --query id -o tsv)
    # az search service ప్రదర్శనలో "endpoint" ఫీల్డ్ లేరు; URL ను సర్వీస్ పేరునుండి రూపొందించండి.
    export AZURE_SEARCH_SERVICE_ENDPOINT="https://<service-name>.search.windows.net"
    ```

    RBAC ఇనేబుల్ చేసిన తరువాత, క్రింద ఉన్న Python మరియు .NET SDK నమూనాలు `DefaultAzureCredential` తో ధృవీకరిస్తాయి, ఇది లోకల్ డెవలপ్మెంట్ సమయంలో మీ `az login` సెషన్ ఉపయోగిస్తుంది — అడ్మిన్ కీ అవసరం లేదు. [Connect to Azure AI Search using roles](https://learn.microsoft.com/azure/search/search-security-rbac) ని చూడండి.

4. **(ఫాల్‌బ్యాక్) కీ ఆధారిత అనుమతి** — RBAC ఉపయోగించలేకపోతే మాత్రమే, అడ్మిన్ కీని కూడా నిల్వ చేసుకోండి:

#### Azure AI Search ఉదాహరణకు ఎండ్పాయింట్ మరియు API కీని వాతావరణ వేరియബుల్స్‌గా నిల్వ చేయండి.

    ```bash
    # zsh/bash
    # az search service showలో "endpoint" ఫీల్డ్ లేదు; సర్వీస్ పేరుని ఉపయోగించి URLని నిర్మించండి.
    export AZURE_SEARCH_SERVICE_ENDPOINT="https://<service-name>.search.windows.net"
    export AZURE_SEARCH_API_KEY=$(az search admin-key show -g <resource-group> --service-name <service-name> --query "primaryKey" -o tsv)
    ```

    ```powershell
    # PowerShell
    # az search service show లో "endpoint" ఫీల్డ్ లేదు; సర్వీస్ పేరుని ఉపయోగించి URLని నిర్మించండి.
    $env:AZURE_SEARCH_SERVICE_ENDPOINT = "https://<service-name>.search.windows.net"
    $env:AZURE_SEARCH_API_KEY = $(az search admin-key show -g <resource-group> --service-name <service-name> --query "primaryKey" -o tsv)
    ```

### Python SDK ఉపయోగించడం

1. Python కోసం Azure Cognitive Search క్లయింట్ లైబ్రరీ మరియు Azure Identityని ఇన్‌స్టాల్ చేయండి:

   ```bash
   pip install azure-search-documents azure-identity
   ```

2. సూచిక సృష్టించడం మరియు డాక్యుమెంట్లను అప్లోడ్ చేయడానికి క్రింది Python కోడ్ ఉపయోగించండి:

    ```python
    import os
    from azure.identity import DefaultAzureCredential
    from azure.search.documents import SearchClient
    from azure.search.documents.indexes import SearchIndexClient
    from azure.search.documents.indexes.models import SearchIndex, SimpleField, edm

    service_endpoint = os.getenv("AZURE_SEARCH_SERVICE_ENDPOINT")
    index_name = "sample-index"

    # కీ లేని (సిఫార్సు చేయబడింది): మీ `az login` ఐడెంటిటీని Entra ID RBAC ద్వారా ఉపయోగిస్తుంది.
    # "సెర్చ్ సర్వీస్ కంట్రిబ్యూటర్" మరియు "సెర్చ్ ఇండెక్స్ డేటా కంట్రిబ్యూటర్" పాత్రలను అవసరం.
    credential = DefaultAzureCredential()
    # ఫాల్‌బ్యాక్ (కీ ఆధారిత ప్రమాణీకరణ):
    # azure.core.credentials నుండి AzureKeyCredential ని దిగుమతి చేసుకోండి
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

1. సూచిక సృష్టించడానికి మరియు డాక్యుమెంట్లు అప్లోడ్ చేయడానికి ఈ క‌మాండ్ ను రన్ చేయండి:

    ```bash
    dotnet run ./AzureSearch.cs
    ```

    క్రింద ఉన్న .NET నమూనా `DefaultAzureCredential` ఉపయోగిస్తుంది, ఇది లోకల్ డెవలప్మెంట్ సమయంలో మీ Azure CLI సైన్ ఇన్ (`az login`) ఉపయోగిస్తుంది.

2. ఇక్కడ `AzureSearch.cs` యొక్క .NET కోడ్ ఉంది:

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

మరింత వివరణాత్మక సమాచారం కోసం ఈ డాక్యుమెంటేషన్‌ను చూడండి:

- [Create an Azure Cognitive Search service](https://learn.microsoft.com/azure/search/search-create-service-portal?wt.mc_id=studentamb_258691)
- [Get started with Azure Cognitive Search](https://learn.microsoft.com/azure/search/search-get-started-portal?wt.mc_id=studentamb_258691)
- [Azure AI Search Tools](https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-ai-search?tabs=azurecli%2Cpython&pivots=code-examples?wt.mc_id=studentamb_258691)

## ముగింపు

మీరు Azure పోర్టల్ మరియు అనుసంధానించిన టూల్స్ ఉపయోగించి విజయవంతంగా Azure AI Search ను సెటప్ చేసుకున్నారు. మీరు ఇప్పుడు Azure AI Search యొక్క మరింత అభివృద్ధి చెందిన ఫీచర్లు మరియు సామర్థ్యాలను అన్వేషించవచ్చు మరియు మీ సెర్చ్ పరిష్కారాలను మెరుగుపరచవచ్చు.

అదనపు సహాయం కోసం, [Azure Cognitive Search documentation](https://learn.microsoft.com/azure/search/?wt.mc_id=studentamb_258691)ని సందర్శించండి.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**అస్వీకరణ**:
ఈ పత్రం AI అనువాద సేవ [Co-op Translator](https://github.com/Azure/co-op-translator) ఉపయోగించి అనువదించబడింది. మేము ఖచ్చితత్వానికి ప్రయత్నిస్తున్నప్పటికీ, ఆటోమేటెడ్ అనువాదాలు తప్పులు లేదా అసమగ్రతలను కలిగి ఉండవచ్చు. దాని స్వదేశ భాషలో ఉన్న అసలు పత్రాన్ని అధికారం కలిగిన మూలంగా పరిగణించాలి. కీలకమైన సమాచారం కోసం, ప్రొఫెషనల్ మానవ అనువాదాన్ని సిఫారసు చేస్తాము. ఈ అనువాదం ఉపయోగం వల్ల కలిగే ఏవైనా అపార్థాలు లేదా తప్పుదారులు కోసం మేము బాధ్యత వహించము.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->