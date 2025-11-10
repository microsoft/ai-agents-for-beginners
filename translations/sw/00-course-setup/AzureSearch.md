<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "11e38db0898a788612b917e329dcdb5b",
  "translation_date": "2025-11-07T08:45:24+00:00",
  "source_file": "00-course-setup/AzureSearch.md",
  "language_code": "sw"
}
-->
# Mwongozo wa Kuweka Azure AI Search

Mwongozo huu utakusaidia kuweka Azure AI Search kwa kutumia Azure portal. Fuata hatua zilizo hapa chini kuunda na kusanidi huduma yako ya Azure AI Search.

## Mahitaji ya Awali

Kabla ya kuanza, hakikisha unayo yafuatayo:

- Usajili wa Azure. Ikiwa huna usajili wa Azure, unaweza kuunda akaunti ya bure kwenye [Akaunti ya Bure ya Azure](https://azure.microsoft.com/free/?wt.mc_id=studentamb_258691).

## Hatua ya 1: Unda Akaunti ya Hifadhi ya Azure

1. Fuata maelekezo haya, [Unda akaunti ya hifadhi ya Azure](https://learn.microsoft.com/azure/storage/common/storage-account-create?tabs=azure-portal), kuunda Akaunti mpya ya Hifadhi ya Azure.
   **NOTE**: Hakikisha aina ya Akaunti ya Hifadhi ni Standard General Purpose V2.

## Hatua ya 2: Unda Huduma ya Azure AI Search

1. Ingia kwenye [Azure portal](https://portal.azure.com/?wt.mc_id=studentamb_258691).
2. Katika paneli ya urambazaji upande wa kushoto, bonyeza **Create a resource**.
3. Katika kisanduku cha utafutaji, andika "Azure AI Search" na uchague **Azure AI Search** kutoka kwenye orodha ya matokeo.
4. Bonyeza kitufe cha **Create**.
5. Katika kichupo cha **Basics**, toa maelezo yafuatayo:
   - **Subscription**: Chagua usajili wako wa Azure.
   - **Resource group**: Unda kikundi kipya cha rasilimali au chagua kilichopo.
   - **Resource name**: Weka jina la kipekee kwa huduma yako ya utafutaji.
   - **Region**: Chagua eneo lililo karibu na watumiaji wako.
   - **Pricing tier**: Chagua kiwango cha bei kinachokidhi mahitaji yako. Unaweza kuanza na kiwango cha Bure kwa majaribio.
6. Bonyeza **Review + create**.
7. Kagua mipangilio na bonyeza **Create** kuunda huduma ya utafutaji.

## Hatua ya 3: Anza na Azure AI Search

1. Mara baada ya usanidi kukamilika, nenda kwenye huduma yako ya utafutaji katika Azure portal.
2. Katika paneli ya muhtasari wa huduma ya utafutaji, nakili URL. Inapaswa kuonekana kama `https://<service-name>.search.windows.net`.
3. Katika Settings > Keys, nakili funguo ya maswali.
4. Fuata hatua kwenye ukurasa wa [Mwongozo wa Haraka](https://learn.microsoft.com/azure/search/search-get-started-portal?pivots=import-data-new) kuunda faharasa, kupakia data, na kufanya maswali ya utafutaji.

## Hatua ya 4: Tumia Zana za Azure AI Search

Azure AI Search inaunganishwa na zana mbalimbali ili kuboresha uwezo wako wa utafutaji. Unaweza kutumia Azure CLI, Python SDK, .NET SDK na zana nyingine kwa usanidi wa hali ya juu na operesheni.

### Kutumia Azure CLI

1. Sakinisha Azure CLI kwa kufuata maelekezo kwenye [Sakinisha Azure CLI](https://learn.microsoft.com/cli/azure/install-azure-cli?wt.mc_id=studentamb_258691).
2. Ingia kwenye Azure CLI kwa kutumia amri:

   ```bash
   az login
   ```

3. Hifadhi endpoint na API key ya Azure AI Search kwenye vigezo vya mazingira.

    ```bash
    # zsh/bash
    export AZURE_SEARCH_SERVICE_ENDPOINT=$(az search service show -g <resource-group> -n <service-name> --query "endpoint" -o tsv)
    export AZURE_SEARCH_API_KEY=$(az search service admin-key list -g <resource-group> --search-service-name <service-name> --query "primaryKey" -o tsv)
    ```

    ```powershell
    # PowerShell
    $env:AZURE_SEARCH_SERVICE_ENDPOINT = az search service show -g <resource-group> -n <service-name> --query "endpoint" -o tsv
    $env:AZURE_SEARCH_API_KEY = $(az search service admin-key list -g <resource-group> --search-service-name <service-name> --query "primaryKey" -o tsv)
    ```

### Kutumia Python SDK

1. Sakinisha maktaba ya mteja ya Azure Cognitive Search kwa Python:

   ```bash
   pip install azure-search-documents
   ```

2. Tumia msimbo wa Python ufuatao kuunda faharasa na kupakia nyaraka:

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

### Kutumia .NET SDK

1. Endesha amri ifuatayo kuunda faharasa na kupakia nyaraka:

    ```bash
    dotnet run ./AzureSearch.cs
    ```

2. Huu hapa ni msimbo wa .NET wa `AzureSearch.cs`:

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

Kwa maelezo zaidi, rejelea nyaraka zifuatazo:

- [Unda huduma ya Azure Cognitive Search](https://learn.microsoft.com/azure/search/search-create-service-portal?wt.mc_id=studentamb_258691)
- [Anza na Azure Cognitive Search](https://learn.microsoft.com/azure/search/search-get-started-portal?wt.mc_id=studentamb_258691)
- [Zana za Azure AI Search](https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-ai-search?tabs=azurecli%2Cpython&pivots=code-examples?wt.mc_id=studentamb_258691)

## Hitimisho

Umefanikiwa kuweka Azure AI Search kwa kutumia Azure portal na zana zilizounganishwa. Sasa unaweza kuchunguza vipengele vya hali ya juu na uwezo wa Azure AI Search ili kuboresha suluhisho zako za utafutaji.

Kwa msaada zaidi, tembelea [Nyaraka za Azure Cognitive Search](https://learn.microsoft.com/azure/search/?wt.mc_id=studentamb_258691).

---

**Kanusho**:  
Hati hii imetafsiriwa kwa kutumia huduma ya tafsiri ya AI [Co-op Translator](https://github.com/Azure/co-op-translator). Ingawa tunajitahidi kwa usahihi, tafadhali fahamu kuwa tafsiri za kiotomatiki zinaweza kuwa na makosa au kutokuwa sahihi. Hati ya asili katika lugha yake ya awali inapaswa kuzingatiwa kama chanzo cha mamlaka. Kwa taarifa muhimu, tafsiri ya kitaalamu ya binadamu inapendekezwa. Hatutawajibika kwa kutoelewana au tafsiri zisizo sahihi zinazotokana na matumizi ya tafsiri hii.