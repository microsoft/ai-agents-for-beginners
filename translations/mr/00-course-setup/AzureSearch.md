# Azure AI Search सेटअप मार्गदर्शक

हा मार्गदर्शक तुम्हाला Azure पोर्टल वापरून Azure AI Search सेटअप करण्यात मदत करेल. खालील चरणांचे अनुसरण करून तुमची Azure AI Search सेवा तयार करा आणि कॉन्फिगर करा.

## पूर्वनिर्धारित आवश्यकता

सुरू करण्यापूर्वी, खालील गोष्टींची खात्री करा:

- एक Azure सदस्यता. जर तुमच्याकडे Azure सदस्यता नसेल, तर तुम्ही [Azure Free Account](https://azure.microsoft.com/free/?wt.mc_id=studentamb_258691) येथे मोफत खाते तयार करू शकता.

## चरण 1: Azure स्टोरेज खाते तयार करा

1. या सूचनेचे अनुसरण करा, [Create an Azure storage account](https://learn.microsoft.com/azure/storage/common/storage-account-create?tabs=azure-portal) आणि नवीन Azure स्टोरेज खाते तयार करा.
   **टीप**: खात्री करा की स्टोरेज अकाउंटचा प्रकार Standard General Purpose V2 आहे.

## चरण 2: Azure AI Search सेवा तयार करा

1. [Azure पोर्टल](https://portal.azure.com/?wt.mc_id=studentamb_258691) मध्ये साइन इन करा.
2. डाव्या बाजूच्या नेव्हिगेशन पॅनमध्ये, **Create a resource** या वर क्लिक करा.
3. शोध बॉक्समध्ये "Azure AI Search" टाइप करा आणि निकालांच्या यादीतून **Azure AI Search** निवडा.
4. **Create** बटणावर क्लिक करा.
5. **Basics** टॅबमध्ये खालील माहिती द्या:
   - **Subscription**: तुमची Azure सदस्यता निवडा.
   - **Resource group**: नवीन रिसोर्स ग्रुप तयार करा किंवा विद्यमान एक निवडा.
   - **Resource name**: तुमच्या सर्च सेवेसाठी एक अद्वितीय नाव प्रविष्ट करा.
   - **Region**: तुमच्या वापरकर्त्यांच्या जवळचा प्रदेश निवडा.
   - **Pricing tier**: तुमच्या गरजेनुसार किंमत स्तर निवडा. चाचणीसाठी तुम्ही Free tier पासून सुरू करू शकता.
6. **Review + create** वर क्लिक करा.
7. सेटिंग्ज तपासा आणि सर्च सेवा तयार करण्यासाठी **Create** वर क्लिक करा.

## चरण 3: Azure AI Search वापर सुरू करा

1. एकदा डिप्लॉयमेंट पूर्ण झाल्यावर, Azure पोर्टलमध्ये तुमच्या सर्च सेवेकडे जा.
2. सर्च सेवा अवलोकन पॅनमध्ये, URL कॉपी करा. हा `https://<service-name>.search.windows.net` सारखा दिसेल.
3. **(शिफारस केलेले)** Microsoft Entra ID (RBAC) सह कीलेस अॅक्सेस सक्षम करा (खालील चरण 4 मध्ये दाखवले आहे) — कोणतीही की गरजेची नाही. या मार्गदर्शकातील उदाहरणे इंडेक्स तयार/अपडेट करतात आणि दस्तऐवज अपलोड करतात, ज्यासाठी **Search Service Contributor** आणि **Search Index Data Contributor** भूमिका आवश्यक आहेत (किंवा, की-आधारित प्रमाणीकरणासाठी, **प्राथमिक प्रशासकीय की** — क्वेरी की नाही). फक्त जर तुम्ही RBAC वापरू शकत नसाल तर, **Settings > Keys** पॅन उघडा आणि **प्राथमिक प्रशासकीय की** कॉपी करा.
4. [Quickstart guide](https://learn.microsoft.com/azure/search/search-get-started-portal?pivots=import-data-new) मधील चरणांचे अनुसरण करा जसे की इंडेक्स तयार करणे, डेटा अपलोड करणे आणि शोध करणे.

## चरण 4: Azure AI Search साधने वापरा

Azure AI Search विविध साधनांशी समाकलित होते ज्यामुळे तुमची शोध क्षमता वाढवता येते. प्रगत कॉन्फिगरेशन आणि ऑपरेशन्ससाठी तुम्ही Azure CLI, Python SDK, .NET SDK आणि इतर साधने वापरू शकता.

### Azure CLI वापरून

1. Azure CLI स्थापित करा, [Install Azure CLI](https://learn.microsoft.com/cli/azure/install-azure-cli?wt.mc_id=studentamb_258691) येथे दिलेल्या सूचनांचे पालन करा.
2. Azure CLI मध्ये साइन इन करा हा आदेश वापरून:

   ```bash
   az login
   ```
3. **(शिफारस केलेले) Microsoft Entra ID (RBAC) सह कीलेस अॅक्सेस सक्षम करा:**

    ```bash
    az search service update --name <service-name> --resource-group <resource-group> --auth-options aadOrApiKey
    az role assignment create --assignee <your-user-or-principal-id> --role "Search Service Contributor" --scope $(az search service show -g <resource-group> -n <service-name> --query id -o tsv)
    az role assignment create --assignee <your-user-or-principal-id> --role "Search Index Data Contributor" --scope $(az search service show -g <resource-group> -n <service-name> --query id -o tsv)
    # az search सेवा दर्शविताना "endpoint" फील्ड नाही; URL सेवा नावापासून तयार करा.
    export AZURE_SEARCH_SERVICE_ENDPOINT="https://<service-name>.search.windows.net"
    ```

    RBAC सक्षम असताना, खाली दिलेले Python आणि .NET SDK चे नमुने `DefaultAzureCredential` ने प्रमाणीकरण करतात, जे तुम्हच्या `az login` सत्राचा वापर करते स्थानिक विकासादरम्यान — कोणतीही प्रशासकीय की आवश्यक नाही. पहा [Connect to Azure AI Search using roles](https://learn.microsoft.com/azure/search/search-security-rbac).

4. **(पर्यायी) की-आधारित प्रमाणीकरण** — फक्त जर तुम्ही RBAC वापरू शकत नसाल तर, प्रशासकीय की देखील संग्रहित करा:

#### Azure AI Search इंस्टन्ससाठी दोन्ही, endpoint आणि API की पर्यावरण चलांमध्ये संग्रहित करा.

    ```bash
    # zsh/bash
    # az search service show मध्ये "endpoint" फील्ड नाही; सेवा नावापासून URL तयार करा.
    export AZURE_SEARCH_SERVICE_ENDPOINT="https://<service-name>.search.windows.net"
    export AZURE_SEARCH_API_KEY=$(az search admin-key show -g <resource-group> --service-name <service-name> --query "primaryKey" -o tsv)
    ```

    ```powershell
    # PowerShell
    # az search service show मध्ये "endpoint" फील्ड नाही; सेवा नावापासून URL तयार करा.
    $env:AZURE_SEARCH_SERVICE_ENDPOINT = "https://<service-name>.search.windows.net"
    $env:AZURE_SEARCH_API_KEY = $(az search admin-key show -g <resource-group> --service-name <service-name> --query "primaryKey" -o tsv)
    ```

### Python SDK वापरून

1. Azure Cognitive Search क्लायंट लायब्ररी आणि Azure Identity Python साठी स्थापित करा:

   ```bash
   pip install azure-search-documents azure-identity
   ```

2. खालील Python कोड वापरून इंडेक्स तयार करा आणि दस्तऐवज अपलोड करा:

    ```python
    import os
    from azure.identity import DefaultAzureCredential
    from azure.search.documents import SearchClient
    from azure.search.documents.indexes import SearchIndexClient
    from azure.search.documents.indexes.models import SearchIndex, SimpleField, edm

    service_endpoint = os.getenv("AZURE_SEARCH_SERVICE_ENDPOINT")
    index_name = "sample-index"

    # कीलेस (शिफारस केली आहे): Entra ID RBAC द्वारे तुमची `az login` ओळख वापरतो.
    # "सर्च सेवा योगदानकर्ता" आणि "सर्च निर्देशांक डेटा योगदानकर्ता" भूमिका आवश्यक आहेत.
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

### .NET SDK वापरून

1. इंडेक्स तयार करण्यासाठी आणि दस्तऐवज अपलोड करण्यासाठी खालील आदेश चालवा:

    ```bash
    dotnet run ./AzureSearch.cs
    ```

    खालील .NET नमुना `DefaultAzureCredential` वापरतो, जो `az login` मधील Azure CLI साइन-इनचा वापर स्थानिक विकासादरम्यान करू शकतो.

2. खाली `AzureSearch.cs` चे .NET कोड आहे:

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

तुम्ही Azure पोर्टल आणि समाकलित साधने वापरून यशस्वीपणे Azure AI Search सेटअप केले आहे. तुम्ही आता Azure AI Search च्या अधिक प्रगत वैशिष्ट्ये आणि क्षमतांचा अन्वेषण करू शकता ज्यामुळे तुमच्या शोध सोल्यूशन्स सुधारतील.

अधिक सहाय्यासाठी, [Azure Cognitive Search दस्तऐवज](https://learn.microsoft.com/azure/search/?wt.mc_id=studentamb_258691) भेट द्या.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**अस्वीकरण**:
हा दस्तऐवज AI भाषांतर सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) चा वापर करून अनुवादित केला आहे. जरी आम्ही अचूकतेसाठी प्रयत्न करतो, तरी कृपया लक्षात घ्या की स्वयंचलित भाषांतरांमध्ये त्रुटी किंवा अचूकतेची कमतरता असू शकते. मूळ दस्तऐवज त्याच्या मूळ भाषेत अधिकृत स्रोत मानला पाहिजे. महत्त्वाची माहिती असल्यास, व्यावसायिक मानवी भाषांतराची शिफारस केली जाते. या भाषांतराच्या वापरामुळे उद्भवणाऱ्या कोणत्याही गैरसमज किंवा चुकीच्या अर्थलावणीसाठी आम्ही जबाबदार नाही.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->