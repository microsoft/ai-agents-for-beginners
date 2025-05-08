# Azure AI Search Kurulum Kılavuzu

Bu kılavuz, Azure portalını kullanarak Azure AI Search hizmetinizi nasıl oluşturacağınızı ve yapılandıracağınızı gösterecektir. Aşağıdaki adımları izleyerek Azure AI Search hizmetinizi oluşturun ve yapılandırın.

## Ön Koşullar

Başlamadan önce aşağıdakilere sahip olduğunuzdan emin olun:

- Bir Azure aboneliği. Eğer bir Azure aboneliğiniz yoksa [Azure Ücretsiz Hesap](https://azure.microsoft.com/free/?wt.mc_id=studentamb_258691) üzerinden ücretsiz bir hesap oluşturabilirsiniz.

## Adım 1: Azure AI Search Hizmeti Oluşturma

1. [Azure portal](https://portal.azure.com/?wt.mc_id=studentamb_258691)’a giriş yapın.  
2. Sol menüden **Kaynak oluştur** seçeneğine tıklayın.  
3. Arama kutusuna “Azure AI Search” yazın ve sonuçlardan **Azure AI Search**’ü seçin.  
4. **Oluştur** düğmesine tıklayın.  
5. **Temel Bilgiler (Basics)** sekmesinde aşağıdaki bilgileri girin:  
   - **Abonelik (Subscription)**: Azure aboneliğinizi seçin.  
   - **Kaynak grubu (Resource group)**: Yeni bir kaynak grubu oluşturun veya mevcut birini seçin.  
   - **Kaynak adı (Resource name)**: Arama hizmetiniz için benzersiz bir ad girin.  
   - **Bölge (Region)**: Kullanıcılarınıza en yakın bölgeyi seçin.  
   - **Fiyatlandırma katmanı (Pricing tier)**: Gereksinimlerinize uygun bir katman seçin. Test amacıyla Ücretsiz (Free) katmanıyla başlayabilirsiniz.  
6. **İncele + oluştur (Review + create)** düğmesine tıklayın.  
7. Ayarları gözden geçirin ve **Oluştur (Create)** düğmesine tıklayarak arama hizmetini oluşturun.

## Adım 2: Azure AI Search’e Başlama

1. Dağıtım tamamlandıktan sonra Azure portalda arama hizmetinize gidin.  
2. Arama hizmeti genel bakış sayfasında **Hızlı Başlangıç (Quickstart)** düğmesine tıklayın.  
3. Hızlı Başlangıç kılavuzundaki adımları izleyerek bir dizin oluşturun, veri yükleyin ve bir arama sorgusu gerçekleştirin.

### Dizin Oluşturma

1. Hızlı Başlangıç kılavuzunda **Dizin oluştur (Create an index)** seçeneğine tıklayın.  
2. Alan adlarını ve özelliklerini (ör. veri türü, aranabilirlik, filtrelenebilirlik) belirterek dizin şemasını tanımlayın.  
3. **Oluştur (Create)** düğmesine tıklayarak dizini oluşturun.

### Veri Yükleme

1. Hızlı Başlangıç kılavuzunda **Veri yükle (Upload data)** seçeneğine tıklayın.  
2. Bir veri kaynağı seçin (ör. Azure Blob Storage, Azure SQL Database) ve gerekli bağlantı bilgilerini girin.  
3. Veri kaynağı alanlarını dizin alanlarına eşleyin.  
4. **Gönder (Submit)** düğmesine tıklayarak veriyi dizine yükleyin.

### Arama Sorgusu Gerçekleştirme

1. Hızlı Başlangıç kılavuzunda **Arama Gezgini (Search explorer)** seçeneğine tıklayın.  
2. Arama kutusuna bir sorgu girerek arama işlevini test edin.  
3. Arama sonuçlarını inceleyin ve gerekirse dizin şemasını veya veriyi ayarlayın.

## Adım 3: Azure AI Search Araçlarını Kullanma

Azure AI Search, arama yeteneklerinizi artırmak için çeşitli araçlarla bütünleşir. Gelişmiş yapılandırmalar ve işlemler için Azure CLI, Python SDK ve diğer araçları kullanabilirsiniz.

### Azure CLI Kullanımı

1. [Azure CLI’yi yükleme](https://learn.microsoft.com/en-us/cli/azure/install-azure-cli?wt.mc_id=studentamb_258691) talimatlarını izleyerek Azure CLI’yi kurun.  
2. Aşağıdaki komutla Azure CLI’ya giriş yapın:  
   ```
   az login 
   ```

3. Azure CLI kullanarak yeni bir arama hizmeti oluşturun:

   ```
   az search service create --resource-group <resource-group> --name <service-name> --sku Free
   ```
4. Azure CLI ile bir dizin oluşturun:

   ```
   az search index create --service-name <service-name> --name <index-name> --fields "field1:type, field2:type"
   ```

### Python SDK Kullanımı

1. Python için Azure Cognitive Search istemci kitaplığını yükleyin:

   ```
   pip install azure-search-documents
   ```
2. Aşağıdaki Python kodunu kullanarak bir dizin oluşturun ve belgeleri yükleyin:

   ```
   from azure.core.credentials import AzureKeyCredential
   from azure.search.documents import SearchClient
   from azure.search.documents.indexes import SearchIndexClient
   from azure.search.documents.indexes.models import SearchIndex, SimpleField, edm

   service_endpoint = "https://<service-name>.search.windows.net"
   api_key = "<api-key>"

   index_client = SearchIndexClient(service_endpoint, AzureKeyCredential(api_key))

   fields = [
       SimpleField(name="id", type=edm.String, key=True),
       SimpleField(name="content", type=edm.String, searchable=True),
   ]

   index = SearchIndex(name="sample-index", fields=fields)

   index_client.create_index(index)

   search_client = SearchClient(service_endpoint, "sample-index", AzureKeyCredential(api_key))

   documents = [
       {"id": "1", "content": "Hello world"},
       {"id": "2", "content": "Azure Cognitive Search"}
   ]

   search_client.upload_documents(documents)
   ```

Daha ayrıntılı bilgi için aşağıdaki belgelere başvurun:

* [Azure Cognitive Search hizmeti oluşturma](https://learn.microsoft.com/en-us/azure/search/search-create-service-portal?wt.mc_id=studentamb_258691)
* [Azure Cognitive Search’e başlama](https://learn.microsoft.com/en-us/azure/search/search-get-started-portal?wt.mc_id=studentamb_258691)
* [Azure AI Search Araçları](https://learn.microsoft.com/en-us/azure/ai-services/agents/how-to/tools/azure-ai-search?tabs=azurecli%2Cpython&pivots=code-examples?wt.mc_id=studentamb_258691)

## Sonuç

Azure portalını kullanarak Azure AI Search hizmetinizi başarıyla oluşturup araçlarla entegre ettiniz. Artık Azure AI Search’in gelişmiş özelliklerini keşfederek arama çözümlerinizi daha da güçlendirebilirsiniz.

Daha fazla yardım için [Azure Cognitive Search belgeleri](https://learn.microsoft.com/en-us/azure/search/?wt.mc_id=studentamb_258691) sayfasını ziyaret edin.
