# Azure AI Arama Kurulum Kılavuzu

Bu kılavuz, Azure portalını kullanarak Azure AI Arama'yı kurmanıza yardımcı olacaktır. Azure AI Arama hizmetinizi oluşturmak ve yapılandırmak için aşağıdaki adımları izleyin.

## Ön Koşullar

Başlamadan önce aşağıdakilere sahip olduğunuzdan emin olun:

- Bir Azure aboneliği. Azure aboneliğiniz yoksa, [Azure Ücretsiz Hesap](https://azure.microsoft.com/free/?wt.mc_id=studentamb_258691) sayfasından ücretsiz bir hesap oluşturabilirsiniz.

## Adım 1: Bir Azure Depolama Hesabı Oluşturun

1. Yeni bir Azure Depolama Hesabı oluşturmak için bu talimatı izleyin: [Bir Azure depolama hesabı oluşturma](https://learn.microsoft.com/azure/storage/common/storage-account-create?tabs=azure-portal).
   **NOT**: Depolama Hesabı türünün Standart Genel Amaç V2 olduğundan emin olun.

## Adım 2: Bir Azure AI Arama Hizmeti Oluşturun

1. [Azure portal](https://portal.azure.com/?wt.mc_id=studentamb_258691) adresine giriş yapın.
2. Sol gezinti panelinde **Kaynak oluştur** seçeneğine tıklayın.
3. Arama kutusuna "Azure AI Search" yazın ve sonuçlar listesinden **Azure AI Search**’ü seçin.
4. **Oluştur** butonuna tıklayın.
5. **Temel Bilgiler** sekmesinde aşağıdaki bilgileri sağlayın:
   - **Abonelik**: Azure aboneliğinizi seçin.
   - **Kaynak grubu**: Yeni bir kaynak grubu oluşturun veya mevcut birini seçin.
   - **Kaynak adı**: Arama hizmetiniz için benzersiz bir ad girin.
   - **Bölge**: Kullanıcılarınıza en yakın bölgeyi seçin.
   - **Fiyatlandırma katmanı**: İhtiyaçlarınıza uygun fiyatlandırma katmanını seçin. Test için Ücretsiz katman ile başlayabilirsiniz.
6. **İncele + oluştur** butonuna tıklayın.
7. Ayarları gözden geçirin ve arama hizmetini oluşturmak için **Oluştur** butonuna tıklayın.

## Adım 3: Azure AI Arama ile Başlayın

1. Dağıtım tamamlandıktan sonra, Azure portalında arama hizmetinize gidin.
2. Arama hizmeti genel görünüm panelinde URL’yi kopyalayın. Bu, `https://<service-name>.search.windows.net` şeklinde olmalıdır.
3. **(Önerilen)** Aşağıda Adım 4’te gösterildiği gibi Microsoft Entra ID (RBAC) ile anahtarsız erişimi etkinleştirin — anahtar gerekmez. Bu kılavuzdaki örnekler dizin oluşturma/güncelleme ve belge yükleme işlemleri yapar, bu işlemler için **Search Service Contributor** ve **Search Index Data Contributor** rolleri (veya anahtara dayalı yetkilendirme için **birincil yönetici anahtarı** — sorgu anahtarı değil) gereklidir. Sadece RBAC kullanamıyorsanız, **Ayarlar > Anahtarlar** panelini açarak **birincil yönetici anahtarını** kopyalayın.
4. Bir dizin oluşturmak, veri yüklemek ve arama yapmak için [Hızlı Başlangıç kılavuzu](https://learn.microsoft.com/azure/search/search-get-started-portal?pivots=import-data-new) sayfasındaki adımları izleyin.

## Adım 4: Azure AI Arama Araçlarını Kullanın

Azure AI Arama, arama yeteneklerinizi geliştirmek için çeşitli araçlarla entegre olur. Azure CLI, Python SDK, .NET SDK ve diğer araçları gelişmiş yapılandırmalar ve işlemler için kullanabilirsiniz.

### Azure CLI Kullanımı

1. [Azure CLI Kurulumu](https://learn.microsoft.com/cli/azure/install-azure-cli?wt.mc_id=studentamb_258691) talimatlarını izleyerek Azure CLI'yı yükleyin.
2. Azure CLI'ya şu komutla giriş yapın:

   ```bash
   az login
   ```
3. **(Önerilen) Microsoft Entra ID (RBAC) ile anahtarsız erişimi etkinleştirin:**

    ```bash
    az search service update --name <service-name> --resource-group <resource-group> --auth-options aadOrApiKey
    az role assignment create --assignee <your-user-or-principal-id> --role "Search Service Contributor" --scope $(az search service show -g <resource-group> -n <service-name> --query id -o tsv)
    az role assignment create --assignee <your-user-or-principal-id> --role "Search Index Data Contributor" --scope $(az search service show -g <resource-group> -n <service-name> --query id -o tsv)
    # az search service show'da "endpoint" alanı yok; URL'yi servis adından oluştur.
    export AZURE_SEARCH_SERVICE_ENDPOINT="https://<service-name>.search.windows.net"
    ```

    RBAC etkinleştirildiğinde, aşağıdaki Python ve .NET SDK örnekleri yerel geliştirme sırasında `az login` oturumunuzu kullanan `DefaultAzureCredential` ile kimlik doğrulaması yapar — yönetici anahtarına gerek yoktur. Ayrıntılar için [Rollerle Azure AI Search'a Bağlanma](https://learn.microsoft.com/azure/search/search-security-rbac) sayfasına bakınız.

4. **(Alternatif) Anahtara dayalı kimlik doğrulama** — sadece RBAC kullanamıyorsanız, yönetici anahtarını da şu şekilde kaydedin:

#### Azure AI Search örneği için hem uç nokta hem de API anahtarını ortam değişkenlerine kaydedin.

    ```bash
    # zsh/bash
    # az search service show komutunda "endpoint" alanı yok; servis adından URL oluşturun.
    export AZURE_SEARCH_SERVICE_ENDPOINT="https://<service-name>.search.windows.net"
    export AZURE_SEARCH_API_KEY=$(az search admin-key show -g <resource-group> --service-name <service-name> --query "primaryKey" -o tsv)
    ```

    ```powershell
    # PowerShell
    # az search service show komutunda "endpoint" alanı yok; servis adından URL oluşturun.
    $env:AZURE_SEARCH_SERVICE_ENDPOINT = "https://<service-name>.search.windows.net"
    $env:AZURE_SEARCH_API_KEY = $(az search admin-key show -g <resource-group> --service-name <service-name> --query "primaryKey" -o tsv)
    ```

### Python SDK Kullanımı

1. Azure Cognitive Search istemci kitaplığı ve Python için Azure Kimlik doğrulaması kitaplığını yükleyin:

   ```bash
   pip install azure-search-documents azure-identity
   ```

2. Bir dizin oluşturmak ve belgeleri yüklemek için aşağıdaki Python kodunu kullanın:

    ```python
    import os
    from azure.identity import DefaultAzureCredential
    from azure.search.documents import SearchClient
    from azure.search.documents.indexes import SearchIndexClient
    from azure.search.documents.indexes.models import SearchIndex, SimpleField, edm

    service_endpoint = os.getenv("AZURE_SEARCH_SERVICE_ENDPOINT")
    index_name = "sample-index"

    # Anahtarsız (önerilir): Entra ID RBAC aracılığıyla `az login` kimliğinizi kullanır.
    # "Arama Servisi Katkıda Bulunan" ve "Arama İndeksi Veri Katkıda Bulunan" rolleri gerektirir.
    credential = DefaultAzureCredential()
    # Yedek (anahtara dayalı kimlik doğrulama):
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

### .NET SDK Kullanımı

1. Bir dizin oluşturmak ve belgeleri yüklemek için aşağıdaki komutu çalıştırın:

    ```bash
    dotnet run ./AzureSearch.cs
    ```

    Aşağıdaki .NET örneği, yerel geliştirme sırasında `az login` ile Azure CLI oturumunuzu kullanabilen `DefaultAzureCredential` kullanır.

2. İşte `AzureSearch.cs` dosyasının .NET kodu:

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

Daha ayrıntılı bilgi için aşağıdaki belgelere bakabilirsiniz:

- [Azure Cognitive Search hizmeti oluşturma](https://learn.microsoft.com/azure/search/search-create-service-portal?wt.mc_id=studentamb_258691)
- [Azure Cognitive Search ile başlayın](https://learn.microsoft.com/azure/search/search-get-started-portal?wt.mc_id=studentamb_258691)
- [Azure AI Arama Araçları](https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-ai-search?tabs=azurecli%2Cpython&pivots=code-examples?wt.mc_id=studentamb_258691)

## Sonuç

Azure portalı ve entegre araçları kullanarak Azure AI Arama'yı başarıyla kurdunuz. Artık Azure AI Arama'nın daha gelişmiş özelliklerini ve yeteneklerini keşfederek arama çözümlerinizi geliştirebilirsiniz.

Daha fazla yardım için [Azure Cognitive Search belgeleri](https://learn.microsoft.com/azure/search/?wt.mc_id=studentamb_258691) sayfasını ziyaret edin.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Feragatname**:
Bu belge, AI çeviri hizmeti [Co-op Translator](https://github.com/Azure/co-op-translator) kullanılarak çevrilmiştir. Doğruluk için çaba sarf etsek de, otomatik çevirilerin hata veya yanlışlık içerebileceğini lütfen unutmayınız. Orijinal belge, kendi dilinde yetkili kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel insan çevirisi önerilir. Bu çevirinin kullanımı sonucu ortaya çıkabilecek yanlış anlamalardan veya yanlış yorumlamalardan sorumlu değiliz.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->