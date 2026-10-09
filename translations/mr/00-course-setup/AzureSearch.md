# Azure AI Search सेटअप मार्गदर्शक

हा मार्गदर्शक तुम्हाला Azure पोर्टल वापरून Azure AI Search सेटअप करण्यात मदत करेल. Azure AI Search सेवा तयार करण्यासाठी आणि कॉन्फिगर करण्यासाठी खालील टप्पे अनुसरा.

## पूर्वअट

सुरू करण्यापूर्वी, तुम्हास खालील गोष्टी सुनिश्चित कराव्या लागतील:

- एक Azure सदस्यता. जर तुमच्याकडे Azure सदस्यता नसेल, तर तुम्ही [Azure Free Account](https://azure.microsoft.com/free/?wt.mc_id=studentamb_258691) येथे मोफत खाते तयार करू शकता.

## पाऊल 1: Azure स्टोरेज खाते तयार करा

1. नवीन Azure स्टोरेज खाते तयार करण्यासाठी, [Create an Azure storage account](https://learn.microsoft.com/azure/storage/common/storage-account-create?tabs=azure-portal) या सूचनेचे पालन करा.
   **नोट**: खात्री करा की स्टोरेज खात्याचा प्रकार Standard General Purpose V2 आहे.

## पाऊल 2: Azure AI Search सेवा तयार करा

1. [Azure पोर्टल](https://portal.azure.com/?wt.mc_id=studentamb_258691) मध्ये साइन इन करा.
2. डाव्या बाजूच्या नेव्हिगेशन पॅनमध्ये, **Create a resource** वर क्लिक करा.
3. शोध बॉक्समध्ये "Azure AI Search" टाइप करा आणि निकालांच्या यादीतून **Azure AI Search** निवडा.
4. **Create** बटणावर क्लिक करा.
5. **Basics** टॅबमध्ये खालील माहिती भरा:
   - **Subscription**: तुमची Azure सदस्यता निवडा.
   - **Resource group**: नवीन रिसोर्स ग्रुप तयार करा किंवा पूर्वीचा एक निवडा.
   - **Resource name**: तुमच्या शोध सेवेचा एक अद्वितीय नाव टाका.
   - **Region**: तुमच्या वापरकर्त्यांजवळचा प्रदेश निवडा.
   - **Pricing tier**: तुमच्या गरजेनुसार किंमत स्तर निवडा. तुम्ही चाचणीसाठी Free tier पर्याय निवडू शकता.
6. **Review + create** क्लिक करा.
7. सेटिंग्ज पुनरावलोकन करून **Create** क्लिक करा आणि शोध सेवा तयार करा.

## पाऊल 3: Azure AI Search सह प्रारंभ करा

1. तैनाती पूर्ण झाल्यानंतर, Azure पोर्टलमधील तुमच्या शोध सेवेवर जा.
2. शोध सेवा अवलोकन पॅनमध्ये URL कॉपी करा. तो `https://<service-name>.search.windows.net` यासारखा दिसेल.
3. **(शिफारस केलेले)** खालील पाऊल 4 मध्ये दाखविल्याप्रमाणे Microsoft Entra ID (RBAC) सह की नसलेला प्रवेश सक्षम करा - कीची गरज नाही. या मार्गदर्शकातील उदाहरणे निर्देशांक तयार करतात/अद्यतनित करतात आणि दस्तऐवज अपलोड करतात, ज्यासाठी **Search Service Contributor** आणि **Search Index Data Contributor** भूमिका आवश्यक आहेत (किंवा, की-आधारित प्रमाणीकरणासाठी, **primary admin key** - क्वेरी की नाही). फक्त जर तुम्ही RBAC वापरू शकत नसाल तर, **Settings > Keys** पॅन उघडा आणि **primary admin key** कॉपी करा.
4. निर्देशांक तयार करण्यासाठी, डेटा अपलोड करण्यासाठी आणि शोधसाठी [Quickstart guide](https://learn.microsoft.com/azure/search/search-get-started-portal?pivots=import-data-new) पृष्ठावरील टप्पे अनुसरा.

## पाऊल 4: Azure AI Search साधने वापरा

Azure AI Search विविध साधनांसह एकत्रित होते ज्यामुळे तुमच्या शोध क्षमतांचा विस्तार होतो. तुम्ही Azure CLI, Python SDK, .NET SDK आणि इतर साधनांसह प्रगत कॉन्फिगरेशन आणि ऑपरेशन्स करू शकता.

### Azure CLI वापरणे

1. [Install Azure CLI](https://learn.microsoft.com/cli/azure/install-azure-cli?wt.mc_id=studentamb_258691) येथे दिलेल्या सूचनांचे पालन करून Azure CLI इंस्टॉल करा.
2. Azure CLI मध्ये साइन इन करण्यासाठी पुढील आदेश वापरा:

   ```bash
   az login
   ```
3. **(शिफारस)** Microsoft Entra ID (RBAC) सह की नसलेला प्रवेश सक्षम करा:

    ```bash
    az search service update --name <service-name> --resource-group <resource-group> --auth-options aadOrApiKey
    az role assignment create --assignee <your-user-or-principal-id> --role "Search Service Contributor" --scope $(az search service show -g <resource-group> -n <service-name> --query id -o tsv)
    az role assignment create --assignee <your-user-or-principal-id> --role "Search Index Data Contributor" --scope $(az search service show -g <resource-group> -n <service-name> --query id -o tsv)
    # az search सेवा शो मध्ये "endpoint" फील्ड नाही; सेवा नावावरून URL तयार करा.
    export AZURE_SEARCH_SERVICE_ENDPOINT="https://<service-name>.search.windows.net"
    ```

    RBAC सक्षम केल्याने, खालील Python आणि .NET SDK उदाहरणे `DefaultAzureCredential` सह प्रमाणीकरण करतात, जी स्थानिक विकासादरम्यान तुमच्या `az login` सत्राचा वापर करते - कोणतीही प्रशासकीय की आवश्यक नाही. पाहा [Connect to Azure AI Search using roles](https://learn.microsoft.com/azure/search/search-security-rbac).

4. **(एफलबॅक) की-आधारित प्रमाणीकरण** — फक्त जर तुम्ही RBAC वापरू शकत नसाल तर प्रशासकीय की देखील संग्रहित करा:

#### Azure AI Search इन्स्टन्ससाठी दोन्ही एन्डपॉइंट आणि API की पर्यावरण चलांमध्ये संचयित करा.

    ```bash
    # zsh/bash
    # az search service show मध्ये "endpoint" फील्ड नाही; सेवेच्या नावावरून URL तयार करा.
    export AZURE_SEARCH_SERVICE_ENDPOINT="https://<service-name>.search.windows.net"
    export AZURE_SEARCH_API_KEY=$(az search admin-key show -g <resource-group> --service-name <service-name> --query "primaryKey" -o tsv)
    ```

    ```powershell
    # PowerShell
    # az search service show मध्ये "endpoint" फील्ड नाही; सेवेच्या नावावरून URL तयार करा.
    $env:AZURE_SEARCH_SERVICE_ENDPOINT = "https://<service-name>.search.windows.net"
    $env:AZURE_SEARCH_API_KEY = $(az search admin-key show -g <resource-group> --service-name <service-name> --query "primaryKey" -o tsv)
    ```

### Python SDK वापरणे

1. Azure Cognitive Search क्लायंट लायब्ररी आणि Azure Identity Python साठी इंस्टॉल करा:

   ```bash
   pip install azure-search-documents azure-identity
   ```

2. निर्देशांक तयार करण्यासाठी आणि दस्तऐवज अपलोड करण्यासाठी खालील Python कोड वापरा:

    ```python
    import os
    from azure.identity import DefaultAzureCredential
    from azure.search.documents import SearchClient
    from azure.search.documents.indexes import SearchIndexClient
    from azure.search.documents.indexes.models import SearchIndex, SimpleField, edm

    service_endpoint = os.getenv("AZURE_SEARCH_SERVICE_ENDPOINT")
    index_name = "sample-index"

    # कीलेस (शिफारस केलेले): Entra ID RBAC द्वारा तुमची `az login` ओळख वापरतो.
    # "Search Service Contributor" आणि "Search Index Data Contributor" भूमिका आवश्यक आहेत.
    credential = DefaultAzureCredential()
    # फॉलबॅक (की-आधारित प्रमाणीकरण):
    # azure.core.credentials मधून AzureKeyCredential आयात करा
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

1. निर्देशांक तयार करण्यासाठी आणि दस्तऐवज अपलोड करण्यासाठी खालील आदेश चालवा:

    ```bash
    dotnet run ./AzureSearch.cs
    ```

    खालील .NET उदाहरण `DefaultAzureCredential` वापरते, जे स्थानिक विकासादरम्यान `az login` मधून Azure CLI साइन-इन वापरू शकते.

2. येथे `AzureSearch.cs` ची .NET कोड आहे:

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

अधिक सविस्तर माहितीसाठी, खालील दस्तऐवज पहा:

- [Azure Cognitive Search सेवा तयार करा](https://learn.microsoft.com/azure/search/search-create-service-portal?wt.mc_id=studentamb_258691)
- [Azure Cognitive Search सह प्रारंभ करा](https://learn.microsoft.com/azure/search/search-get-started-portal?wt.mc_id=studentamb_258691)
- [Azure AI Search साधने](https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-ai-search?tabs=azurecli%2Cpython&pivots=code-examples?wt.mc_id=studentamb_258691)

## निष्कर्ष

तुम्ही Azure पोर्टल वापरून Azure AI Search यशस्वीपणे सेटअप केला आहे आणि एकत्रित साधने वापरली आहेत. आता तुम्ही Azure AI Search चे अधिक प्रगत वैशिष्ट्ये आणि क्षमता अन्वेषित करू शकता आणि तुमच्या शोध सोल्यूशन्स वाढवू शकता.

अधिक मदतीसाठी, [Azure Cognitive Search दस्तऐवज](https://learn.microsoft.com/azure/search/?wt.mc_id=studentamb_258691) येथे भेट द्या.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**अस्वीकरण**:
हा दस्तऐवज AI भाषांतर सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) चा वापर करून अनुवादित केला आहे. जरी आम्ही अचूकतेसाठी प्रयत्न करतो, तरी कृपया लक्षात घ्या की स्वयंचलित भाषांतरांमध्ये त्रुटी किंवा अचूकतेची कमतरता असू शकते. मूळ दस्तऐवज त्याच्या मूळ भाषेत अधिकृत स्रोत मानला पाहिजे. महत्त्वाची माहिती असल्यास, व्यावसायिक मानवी भाषांतराची शिफारस केली जाते. या भाषांतराच्या वापरामुळे उद्भवणाऱ्या कोणत्याही गैरसमज किंवा चुकीच्या अर्थलावणीसाठी आम्ही जबाबदार नाही.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->