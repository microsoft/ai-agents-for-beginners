<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "11e38db0898a788612b917e329dcdb5b",
  "translation_date": "2025-11-07T08:36:48+00:00",
  "source_file": "00-course-setup/AzureSearch.md",
  "language_code": "tr"
}
-->
# Azure AI Search Kurulum Kılavuzu

Bu kılavuz, Azure portalını kullanarak Azure AI Search hizmetini kurmanıza yardımcı olacaktır. Azure AI Search hizmetinizi oluşturmak ve yapılandırmak için aşağıdaki adımları takip edin.

## Ön Koşullar

Başlamadan önce aşağıdakilere sahip olduğunuzdan emin olun:

- Bir Azure aboneliği. Eğer bir Azure aboneliğiniz yoksa, [Azure Ücretsiz Hesap](https://azure.microsoft.com/free/?wt.mc_id=studentamb_258691) adresinden ücretsiz bir hesap oluşturabilirsiniz.

## Adım 1: Azure Depolama Hesabı Oluşturma

1. Yeni bir Azure Depolama Hesabı oluşturmak için [Azure depolama hesabı oluşturma](https://learn.microsoft.com/azure/storage/common/storage-account-create?tabs=azure-portal) talimatlarını takip edin.  
   **NOT**: Depolama Hesabı türünün Standart Genel Amaçlı V2 olduğundan emin olun.

## Adım 2: Azure AI Search Hizmeti Oluşturma

1. [Azure portalına](https://portal.azure.com/?wt.mc_id=studentamb_258691) giriş yapın.
2. Sol taraftaki gezinme panelinde **Kaynak oluştur** seçeneğine tıklayın.
3. Arama kutusuna "Azure AI Search" yazın ve sonuçlar arasından **Azure AI Search** seçeneğini seçin.
4. **Oluştur** düğmesine tıklayın.
5. **Temel Bilgiler** sekmesinde aşağıdaki bilgileri sağlayın:
   - **Abonelik**: Azure aboneliğinizi seçin.
   - **Kaynak grubu**: Yeni bir kaynak grubu oluşturun veya mevcut birini seçin.
   - **Kaynak adı**: Arama hizmetiniz için benzersiz bir ad girin.
   - **Bölge**: Kullanıcılarınıza en yakın bölgeyi seçin.
   - **Fiyatlandırma katmanı**: Gereksinimlerinize uygun bir fiyatlandırma katmanı seçin. Test için Ücretsiz katmanla başlayabilirsiniz.
6. **Gözden geçir + oluştur** seçeneğine tıklayın.
7. Ayarları gözden geçirin ve arama hizmetini oluşturmak için **Oluştur** seçeneğine tıklayın.

## Adım 3: Azure AI Search ile Başlangıç

1. Dağıtım tamamlandıktan sonra Azure portalında arama hizmetinize gidin.
2. Arama hizmeti genel bakış panelinde URL'yi kopyalayın. Şu şekilde görünmelidir: `https://<service-name>.search.windows.net`.
3. Ayarlar > Anahtarlar panelinde sorgu anahtarını kopyalayın.
4. [Hızlı başlangıç kılavuzu](https://learn.microsoft.com/azure/search/search-get-started-portal?pivots=import-data-new) sayfasındaki adımları takip ederek bir dizin oluşturun, veri yükleyin ve bir arama sorgusu gerçekleştirin.

## Adım 4: Azure AI Search Araçlarını Kullanma

Azure AI Search, arama yeteneklerinizi geliştirmek için çeşitli araçlarla entegre olur. Azure CLI, Python SDK, .NET SDK ve diğer araçları gelişmiş yapılandırmalar ve işlemler için kullanabilirsiniz.

### Azure CLI Kullanımı

1. [Azure CLI'yi yükleme](https://learn.microsoft.com/cli/azure/install-azure-cli?wt.mc_id=studentamb_258691) talimatlarını takip ederek Azure CLI'yi yükleyin.
2. Aşağıdaki komutla Azure CLI'ye giriş yapın:

   ```bash
   az login
   ```

3. Azure AI Search örneği için hem uç noktayı hem de API anahtarını ortam değişkenlerine kaydedin.

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

### Python SDK Kullanımı

1. Python için Azure Cognitive Search istemci kütüphanesini yükleyin:

   ```bash
   pip install azure-search-documents
   ```

2. Aşağıdaki Python kodunu kullanarak bir dizin oluşturun ve belgeleri yükleyin:

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

### .NET SDK Kullanımı

1. Bir dizin oluşturmak ve belgeleri yüklemek için aşağıdaki komutu çalıştırın:

    ```bash
    dotnet run ./AzureSearch.cs
    ```

2. İşte `AzureSearch.cs` için .NET kodu:

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

Daha ayrıntılı bilgi için aşağıdaki belgeleri inceleyin:

- [Azure Cognitive Search hizmeti oluşturma](https://learn.microsoft.com/azure/search/search-create-service-portal?wt.mc_id=studentamb_258691)
- [Azure Cognitive Search ile başlama](https://learn.microsoft.com/azure/search/search-get-started-portal?wt.mc_id=studentamb_258691)
- [Azure AI Search Araçları](https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-ai-search?tabs=azurecli%2Cpython&pivots=code-examples?wt.mc_id=studentamb_258691)

## Sonuç

Azure portalını kullanarak Azure AI Search hizmetini başarıyla kurdunuz ve araçları entegre ettiniz. Artık Azure AI Search'ün daha gelişmiş özelliklerini ve yeteneklerini keşfederek arama çözümlerinizi geliştirebilirsiniz.

Daha fazla yardım için [Azure Cognitive Search belgeleri](https://learn.microsoft.com/azure/search/?wt.mc_id=studentamb_258691) adresini ziyaret edin.

---

**Feragatname**:  
Bu belge, AI çeviri hizmeti [Co-op Translator](https://github.com/Azure/co-op-translator) kullanılarak çevrilmiştir. Doğruluk için çaba göstersek de, otomatik çevirilerin hata veya yanlışlıklar içerebileceğini lütfen unutmayın. Belgenin orijinal dili, yetkili kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel insan çevirisi önerilir. Bu çevirinin kullanımından kaynaklanan yanlış anlamalar veya yanlış yorumlamalar için sorumluluk kabul etmiyoruz.