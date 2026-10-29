# Azure AI Search स्थापनेचे मार्गदर्शक

हा मार्गदर्शक तुम्हाला Azure पोर्टल वापरून Azure AI Search सेटअप करण्यात मदत करेल. तुमची Azure AI Search सेवा तयार करण्यासाठी आणि संरचीत करण्यासाठी खालील चरणांचे अनुसरण करा.

## पूर्वअट

सुरू करण्यापूर्वी, खात्री करा की तुमच्याकडे खालील गोष्टी आहेत:

- एक Azure सदस्यता. जर तुमच्याकडे Azure सदस्यता नसेल, तर तुम्ही [Azure Free Account](https://azure.microsoft.com/free/?wt.mc_id=studentamb_258691) येथे मोफत खाते तयार करू शकता.

## चरण 1: Azure Storage Account तयार करा

1. नवीन Azure Storage Account तयार करण्यासाठी, [Create an Azure storage account](https://learn.microsoft.com/azure/storage/common/storage-account-create?tabs=azure-portal) या सूचना पाळा.
   **टीप**: Storage Account प्रकार Standard General Purpose V2 असल्याची खात्री करा.

## चरण 2: Azure AI Search सेवा तयार करा

1. [Azure portal](https://portal.azure.com/?wt.mc_id=studentamb_258691) मध्ये साइन इन करा.
2. डाव्या बाजूच्या नेव्हिगेशन पॅनमध्ये, **Create a resource** वर क्लिक करा.
3. शोध बॉक्समध्ये "Azure AI Search" टाईप करा आणि निकालांच्या यादीतून **Azure AI Search** निवडा.
4. **Create** बटणावर क्लिक करा.
5. **Basics** टॅबमध्ये, खालील माहिती भरा:
   - **Subscription**: तुमची Azure सदस्यता निवडा.
   - **Resource group**: नवीन resource group तयार करा किंवा विद्यमान निवडा.
   - **Resource name**: तुमच्या शोध सेवेचे एक अनोखे नाव प्रविष्ट करा.
   - **Region**: तुमच्या वापरकर्त्यांना सर्वात जवळचा प्रदेश निवडा.
   - **Pricing tier**: तुमच्या गरजेनुसार एक फायदा किंमतीची निवड करा. चाचणीसाठी Free tier वापरू शकता.
6. **Review + create** वर क्लिक करा.
7. सेटिंग्ज तपासा आणि शोध सेवा तयार करण्यासाठी **Create** क्लिक करा.

## चरण 3: Azure AI Search वापरण्यास प्रारंभ करा

1. एकदा तैनाती पूर्ण झाल्यावर, Azure पोर्टलमध्ये तुमच्या शोध सेवेवर जा.
2. शोध सेवा अवलोकन पॅनमध्ये, URL कॉपी करा. ते असे दिसले पाहिजे: `https://<service-name>.search.windows.net`.
3. **(संबंधितपणे)** Microsoft Entra ID (RBAC) सह keyless access सक्षम करा — कीची गरज नाही. या मार्गदर्शकातील नमुना index तयार करतात/अपडेट करतात आणि दस्तऐवज अपलोड करतात ज्यांना **Search Service Contributor** आणि **Search Index Data Contributor** भूमिका आवश्यक आहेत (किंवा, key-based auth साठी, **प्राथमिक प्रशासक की** — क्वेरी की नाही). फक्त तुम्ही RBAC वापरू शकत नसल्यास, **Settings > Keys** पॅन उघडा आणि **प्राथमिक प्रशासक की** कॉपी करा.
4. index तयार करण्यासाठी, डेटा अपलोड करण्यासाठी, आणि शोध करण्यासाठी [Quickstart guide](https://learn.microsoft.com/azure/search/search-get-started-portal?pivots=import-data-new) पृष्ठातील चरणांचे अनुसरण करा.

## चरण 4: Azure AI Search टूल्स वापरा

Azure AI Search विविध टूल्ससह एकत्रित होते जे तुमच्या शोध क्षमता वाढवतात. तुम्ही Azure CLI, Python SDK, .NET SDK आणि इतर टूल्स वापरून प्रगत संरचना आणि क्रियाकलाप करू शकता.

### Azure CLI वापरणे

1. [Install Azure CLI](https://learn.microsoft.com/cli/azure/install-azure-cli?wt.mc_id=studentamb_258691) येथे दिलेल्या सूचनांचे पालन करून Azure CLI इंस्टॉल करा.
2. Azure CLI मध्ये साइन इन करण्यासाठी खालील कमांड वापरा:

   ```bash
   az login
   ```
3. **(संबंधितपणे) Microsoft Entra ID (RBAC) सह keyless access सक्षम करा:**

    ```bash
    az search service update --name <service-name> --resource-group <resource-group> --auth-options aadOrApiKey
    az role assignment create --assignee <your-user-or-principal-id> --role "Search Service Contributor" --scope $(az search service show -g <resource-group> -n <service-name> --query id -o tsv)
    az role assignment create --assignee <your-user-or-principal-id> --role "Search Index Data Contributor" --scope $(az search service show -g <resource-group> -n <service-name> --query id -o tsv)
    # az search service show has no "endpoint" field; build the URL from the service name.
    export AZURE_SEARCH_SERVICE_ENDPOINT="https://<service-name>.search.windows.net"
    ```

    RBAC सक्षम झाल्यानंतर, खालील Python आणि .NET SDK नमुने `DefaultAzureCredential` सह प्रमाणीकरण करतात, जे तुमचा `az login` सत्र स्थानिक विकासादरम्यान वापरतात — प्रशासक की आवश्यक नाही. पाहा [Connect to Azure AI Search using roles](https://learn.microsoft.com/azure/search/search-security-rbac).

4. **(पर्यायी) की-आधारित प्रमाणीकरण** — फक्त जर तुम्ही RBAC वापरू शकत नसाल तर प्रशासक की जतन करा:

#### Azure AI Search उदाहरणासाठी.Endpoint आणि API की दोन्ही पर्यावरण चलांमध्ये संग्रहित करा.

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

### Python SDK वापरणे

1. Azure Cognitive Search क्लायंट लायब्ररी आणि Azure Identity Python साठी इंस्टॉल करा:

   ```bash
   pip install azure-search-documents azure-identity
   ```

2. index तयार करण्यासाठी आणि दस्तऐवज अपलोड करण्यासाठी खालील Python कोड वापरा:

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

### .NET SDK वापरणे

1. index तयार करण्यासाठी आणि दस्तऐवज अपलोड करण्यासाठी खालील कमांड चालवा:

    ```bash
    dotnet run ./AzureSearch.cs
    ```

    खालील .NET नमुना `DefaultAzureCredential` वापरतो, जो स्थानिक विकासादरम्यान तुमच्या Azure CLI साइन-इन (`az login`) वापरू शकतो.

2. इथे `AzureSearch.cs` चा .NET कोड आहे:

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

अधिक तपशीलवार माहितीसाठी, खालील दस्तऐवज पहा:

- [Create an Azure Cognitive Search service](https://learn.microsoft.com/azure/search/search-create-service-portal?wt.mc_id=studentamb_258691)
- [Get started with Azure Cognitive Search](https://learn.microsoft.com/azure/search/search-get-started-portal?wt.mc_id=studentamb_258691)
- [Azure AI Search Tools](https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-ai-search?tabs=azurecli%2Cpython&pivots=code-examples?wt.mc_id=studentamb_258691)

## निष्कर्ष

तुम्ही Azure पोर्टल आणि एकत्रित टूल्स वापरून यशस्वीपणे Azure AI Search सेटअप केले आहे. आता तुम्ही Azure AI Search च्या अधिक प्रगत वैशिष्ट्ये आणि क्षमता शोधण्या संदर्भात पुढे जाऊ शकता.

अधिक मदतीसाठी, [Azure Cognitive Search documentation](https://learn.microsoft.com/azure/search/?wt.mc_id=studentamb_258691) भेट द्या.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**अस्वीकरण**:
हा दस्तऐवज AI भाषांतर सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) चा वापर करून अनुवादित केला आहे. जरी आम्ही अचूकतेसाठी प्रयत्न करतो, तरी कृपया लक्षात घ्या की स्वयंचलित भाषांतरांमध्ये त्रुटी किंवा अचूकतेची कमतरता असू शकते. मूळ दस्तऐवज त्याच्या मूळ भाषेत अधिकृत स्रोत मानला पाहिजे. महत्त्वाची माहिती असल्यास, व्यावसायिक मानवी भाषांतराची शिफारस केली जाते. या भाषांतराच्या वापरामुळे उद्भवणाऱ्या कोणत्याही गैरसमज किंवा चुकीच्या अर्थलावणीसाठी आम्ही जबाबदार नाही.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->