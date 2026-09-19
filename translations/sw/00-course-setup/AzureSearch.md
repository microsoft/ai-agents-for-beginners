# Mwongozo wa Usanidi wa Azure AI Search

Mwongozo huu utakusaidia kusanidi Azure AI Search kwa kutumia portal ya Azure. Fuata hatua zilizo hapa chini kuunda na kusanidi huduma yako ya Azure AI Search.

## Masharti ya Awali

Kabla hujaanza, hakikisha una yafuatayo:

- Usajili wa Azure. Ikiwa huna usajili wa Azure, unaweza kuunda akaunti ya bure kwenye [Azure Free Account](https://azure.microsoft.com/free/?wt.mc_id=studentamb_258691).

## Hatua ya 1: Unda Akaunti ya Uhifadhi ya Azure

1. Fuata maelekezo haya, [Create an Azure storage account](https://learn.microsoft.com/azure/storage/common/storage-account-create?tabs=azure-portal), kuunda Akaunti mpya ya Uhifadhi ya Azure.
   **NOTE**: Hakikisha kuwa aina ya Akaunti ya Uhifadhi ni Standard General Purpose V2.

## Hatua ya 2: Unda Huduma ya Azure AI Search

1. Ingia kwenye [Azure portal](https://portal.azure.com/?wt.mc_id=studentamb_258691).
2. Katika sehemu ya urambazaji upande wa kushoto, bofya **Create a resource**.
3. Katika kisanduku cha utafutaji, andika "Azure AI Search" na chagua **Azure AI Search** kutoka kwenye orodha ya matokeo.
4. Bofya kitufe cha **Create**.
5. Kwenye kichupo cha **Basics**, toa taarifa zifuatazo:
   - **Subscription**: Chagua usajili wako wa Azure.
   - **Resource group**: Unda kundi jipya la rasilimali au chagua lililopo.
   - **Resource name**: Weka jina la kipekee kwa huduma yako ya utafutaji.
   - **Region**: Chagua eneo linalokaribia watumiaji wako.
   - **Pricing tier**: Chagua ngazi ya bei inayokidhi mahitaji yako. Unaweza kuanza na ngazi ya Bure kwa majaribio.
6. Bofya **Review + create**.
7. Kagua mipangilio na bofya **Create** kuunda huduma ya utafutaji.

## Hatua ya 3: Anza na Azure AI Search

1. Mara utekelezaji ukimalizika, nenda kwenye huduma yako ya utafutaji kwenye portal ya Azure.
2. Kwenye paneli ya muhtasari wa huduma ya utafutaji, nakili URL. Inapaswa kuonekana kama `https://<service-name>.search.windows.net`.
3. **(Inapendekezwa)** Washa upatikanaji bila funguo kwa Microsoft Entra ID (RBAC) kama inavyoonyeshwa katika Hatua ya 4 hapa chini — hakuna funguo huluhikiwa. Sampuli katika mwongozo huu huzuia/kuboresha viashiria na kupakia nyaraka, ambavyo vinahitaji majukumu ya **Search Service Contributor** na **Search Index Data Contributor** (au, kwa uthibitishaji wa kulingana na funguo, **funguo kuu ya msimamizi** — si funguo ya uchunguzi). Ikiwa huwezi kutumia RBAC, fungua paneli ya **Settings > Keys** na nakili **funguo kuu ya msimamizi**.
4. Fuata hatua kwenye ukurasa wa [Quickstart guide](https://learn.microsoft.com/azure/search/search-get-started-portal?pivots=import-data-new) kuunda kiashiria, kupakia data, na kufanya utafutaji.

## Hatua ya 4: Tumia Zana za Azure AI Search

Azure AI Search inaunganisha na zana mbalimbali kuboresha uwezo wako wa utafutaji. Unaweza kutumia Azure CLI, Python SDK, .NET SDK na zana nyingine kwa usanidi na operesheni za hali ya juu.

### Kutumia Azure CLI

1. Sakinisha Azure CLI kwa kufuata maelekezo kwenye [Install Azure CLI](https://learn.microsoft.com/cli/azure/install-azure-cli?wt.mc_id=studentamb_258691).
2. Ingia kwenye Azure CLI kwa kutumia amri:

   ```bash
   az login
   ```
3. **(Inapendekezwa) Washa upatikanaji bila funguo kwa Microsoft Entra ID (RBAC):**

    ```bash
    az search service update --name <service-name> --resource-group <resource-group> --auth-options aadOrApiKey
    az role assignment create --assignee <your-user-or-principal-id> --role "Search Service Contributor" --scope $(az search service show -g <resource-group> -n <service-name> --query id -o tsv)
    az role assignment create --assignee <your-user-or-principal-id> --role "Search Index Data Contributor" --scope $(az search service show -g <resource-group> -n <service-name> --query id -o tsv)
    # huduma ya az search show haina uwanja wa "endpoint"; tengeneza URL kutoka kwa jina la huduma.
    export AZURE_SEARCH_SERVICE_ENDPOINT="https://<service-name>.search.windows.net"
    ```

    Kwa kuwa RBAC imewezeshwa, sampuli za Python na .NET SDK zilizo hapa chini zinafanya uthibitishaji kwa kutumia `DefaultAzureCredential`, ambayo hutumia kikao chako cha `az login` wakati wa maendeleo ya ndani — hakuna funguo ya msimamizi inahitajika. Angalia [Connect to Azure AI Search using roles](https://learn.microsoft.com/azure/search/search-security-rbac).

4. **(Chaguzi mbadala) Uthibitishaji kwa kutumia funguo** — ni kwa tu kama huwezi kutumia RBAC, hifadhi funguo ya msimamizi pia:

#### Hifadhi anwani ya mwisho pamoja na funguo ya API kwa mfano wa Azure AI Search kwenye mabadiliko ya mazingira.

    ```bash
    # zsh/bash
    # az search service show haina sehemu ya "endpoint"; tengeneza URL kutoka jina la huduma.
    export AZURE_SEARCH_SERVICE_ENDPOINT="https://<service-name>.search.windows.net"
    export AZURE_SEARCH_API_KEY=$(az search admin-key show -g <resource-group> --service-name <service-name> --query "primaryKey" -o tsv)
    ```

    ```powershell
    # PowerShell
    # az search service show haina sehemu ya "endpoint"; tengeneza URL kutoka jina la huduma.
    $env:AZURE_SEARCH_SERVICE_ENDPOINT = "https://<service-name>.search.windows.net"
    $env:AZURE_SEARCH_API_KEY = $(az search admin-key show -g <resource-group> --service-name <service-name> --query "primaryKey" -o tsv)
    ```

### Kutumia Python SDK

1. Sakinisha maktaba ya mteja wa Azure Cognitive Search na Azure Identity kwa Python:

   ```bash
   pip install azure-search-documents azure-identity
   ```

2. Tumia msimbo wa Python uliofuata kuunda kiashiria na kupakia nyaraka:

    ```python
    import os
    from azure.identity import DefaultAzureCredential
    from azure.search.documents import SearchClient
    from azure.search.documents.indexes import SearchIndexClient
    from azure.search.documents.indexes.models import SearchIndex, SimpleField, edm

    service_endpoint = os.getenv("AZURE_SEARCH_SERVICE_ENDPOINT")
    index_name = "sample-index"

    # Bila funguo (inapendekezwa): inatumia utambulisho wako wa `az login` kupitia Entra ID RBAC.
    # Inahitaji mihadhara ya "Mchangiaji wa Huduma ya Utafutaji" na "Mchangiaji wa Data ya Kihifadhi cha Utafutaji".
    credential = DefaultAzureCredential()
    # Mbali (uthibitishaji unaotegemea funguo):
    # kutoka azure.core.credentials ingiza AzureKeyCredential
    # uteuzi = AzureKeyCredential(os.getenv("AZURE_SEARCH_API_KEY"))
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

### Kutumia .NET SDK

1. Endesha amri ifuatayo kuunda kiashiria na kupakia nyaraka:

    ```bash
    dotnet run ./AzureSearch.cs
    ```

    Sampuli ya .NET hapa chini inatumia `DefaultAzureCredential`, ambayo inaweza kutumia usajili wako wa Azure CLI kutoka `az login` wakati wa maendeleo ya ndani.

2. Hapa ni msimbo wa .NET wa `AzureSearch.cs`:

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

Kwa maelezo ya kina zaidi, rejelea nyaraka zifuatazo:

- [Create an Azure Cognitive Search service](https://learn.microsoft.com/azure/search/search-create-service-portal?wt.mc_id=studentamb_258691)
- [Get started with Azure Cognitive Search](https://learn.microsoft.com/azure/search/search-get-started-portal?wt.mc_id=studentamb_258691)
- [Azure AI Search Tools](https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-ai-search?tabs=azurecli%2Cpython&pivots=code-examples?wt.mc_id=studentamb_258691)

## Hitimisho

Umeshanidi kwa mafanikio Azure AI Search kwa kutumia portal ya Azure na zana zilizounganishwa. Sasa unaweza kuchunguza sifa na uwezo wa hali ya juu wa Azure AI Search kuboresha suluhisho zako za utafutaji.

Kwa msaada zaidi, tembelea [Azure Cognitive Search documentation](https://learn.microsoft.com/azure/search/?wt.mc_id=studentamb_258691).

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Kionyozo**:
Hati hii imetafsiriwa kwa kutumia huduma ya tafsiri ya AI [Co-op Translator](https://github.com/Azure/co-op-translator). Ingawa tunajitahidi kupata usahihi, tafadhali fahamu kwamba tafsiri za kiotomatiki zinaweza kuwa na makosa au upungufu wa usahihi. Hati ya asili katika lugha yake halisi inapaswa kuchukuliwa kama chanzo cha mamlaka. Kwa taarifa muhimu, tafsiri ya kitaalamu inayofanywa na binadamu inapendekezwa. Hatutojibu kwa kuelewa vibaya au tafsiri potofu zinazotokea kutokana na matumizi ya tafsiri hii.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->