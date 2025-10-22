<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f0ce2d470f3efad6f8c7df376f416a4b",
  "translation_date": "2025-07-12T07:36:47+00:00",
  "source_file": "00-course-setup/AzureSearch.md",
  "language_code": "tr"
}
-->
# Azure AI Search Kurulum Kılavuzu

Bu kılavuz, Azure portalını kullanarak Azure AI Search hizmetini kurmanıza yardımcı olacaktır. Azure AI Search hizmetinizi oluşturmak ve yapılandırmak için aşağıdaki adımları izleyin.

## Gereksinimler

Başlamadan önce, aşağıdakilere sahip olduğunuzdan emin olun:

- Bir Azure aboneliği. Azure aboneliğiniz yoksa, ücretsiz bir hesap oluşturmak için [Azure Free Account](https://azure.microsoft.com/free/?wt.mc_id=studentamb_258691) sayfasını ziyaret edebilirsiniz.

## Adım 1: Azure AI Search Hizmeti Oluşturma

1. [Azure portalına](https://portal.azure.com/?wt.mc_id=studentamb_258691) giriş yapın.
2. Sol taraftaki gezinme panelinde **Create a resource** seçeneğine tıklayın.
3. Arama kutusuna "Azure AI Search" yazın ve sonuçlar listesinden **Azure AI Search** öğesini seçin.
4. **Create** butonuna tıklayın.
5. **Basics** sekmesinde aşağıdaki bilgileri girin:
   - **Subscription**: Azure aboneliğinizi seçin.
   - **Resource group**: Yeni bir kaynak grubu oluşturun veya mevcut birini seçin.
   - **Resource name**: Arama hizmetiniz için benzersiz bir isim girin.
   - **Region**: Kullanıcılarınıza en yakın bölgeyi seçin.
   - **Pricing tier**: İhtiyaçlarınıza uygun bir fiyatlandırma katmanı seçin. Test için Free katmanla başlayabilirsiniz.
6. **Review + create** butonuna tıklayın.
7. Ayarları gözden geçirin ve arama hizmetini oluşturmak için **Create** butonuna tıklayın.

## Adım 2: Azure AI Search ile Başlayın

1. Dağıtım tamamlandıktan sonra, Azure portalında arama hizmetinize gidin.
2. Arama hizmeti genel bakış sayfasında **Quickstart** butonuna tıklayın.
3. Quickstart kılavuzundaki adımları takip ederek bir indeks oluşturun, veri yükleyin ve arama sorgusu gerçekleştirin.

### İndeks Oluşturma

1. Quickstart kılavuzunda **Create an index** seçeneğine tıklayın.
2. Alanları ve özelliklerini (örneğin, veri tipi, aranabilirlik, filtrelenebilirlik) belirterek indeks şemasını tanımlayın.
3. İndeksi oluşturmak için **Create** butonuna tıklayın.

### Veri Yükleme

1. Quickstart kılavuzunda **Upload data** seçeneğine tıklayın.
2. Bir veri kaynağı seçin (örneğin, Azure Blob Storage, Azure SQL Database) ve gerekli bağlantı bilgilerini sağlayın.
3. Veri kaynağı alanlarını indeks alanlarına eşleyin.
4. Veriyi indekse yüklemek için **Submit** butonuna tıklayın.

### Arama Sorgusu Gerçekleştirme

1. Quickstart kılavuzunda **Search explorer** seçeneğine tıklayın.
2. Arama kutusuna bir sorgu girerek arama işlevini test edin.
3. Arama sonuçlarını inceleyin ve gerekirse indeks şemasını veya veriyi ayarlayın.

## Adım 3: Azure AI Search Araçlarını Kullanma

Azure AI Search, arama yeteneklerinizi geliştirmek için çeşitli araçlarla entegre olur. Gelişmiş yapılandırmalar ve işlemler için Azure CLI, Python SDK ve diğer araçları kullanabilirsiniz.

### Azure CLI Kullanımı

1. Azure CLI'yi kurmak için [Install Azure CLI](https://learn.microsoft.com/en-us/cli/azure/install-azure-cli?wt.mc_id=studentamb_258691) sayfasındaki talimatları izleyin.
2. Azure CLI'ye giriş yapmak için şu komutu kullanın:
   ```bash
   az login
   ```
3. Azure CLI kullanarak yeni bir arama hizmeti oluşturun:
   ```bash
   az search service create --resource-group <resource-group> --name <service-name> --sku Free
   ```
4. Azure CLI ile bir indeks oluşturun:
   ```bash
   az search index create --service-name <service-name> --name <index-name> --fields "field1:type, field2:type"
   ```

### Python SDK Kullanımı

1. Python için Azure Cognitive Search istemci kütüphanesini kurun:
   ```bash
   pip install azure-search-documents
   ```
2. Aşağıdaki Python kodunu kullanarak bir indeks oluşturun ve belgeleri yükleyin:
   ```python
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

Daha ayrıntılı bilgi için aşağıdaki dokümanlara bakabilirsiniz:

- [Create an Azure Cognitive Search service](https://learn.microsoft.com/en-us/azure/search/search-create-service-portal?wt.mc_id=studentamb_258691)
- [Get started with Azure Cognitive Search](https://learn.microsoft.com/en-us/azure/search/search-get-started-portal?wt.mc_id=studentamb_258691)
- [Azure AI Search Tools](https://learn.microsoft.com/en-us/azure/ai-services/agents/how-to/tools/azure-ai-search?tabs=azurecli%2Cpython&pivots=code-examples?wt.mc_id=studentamb_258691)

## Sonuç

Azure portalı ve entegre araçları kullanarak Azure AI Search hizmetini başarıyla kurdunuz. Artık Azure AI Search’ün daha gelişmiş özelliklerini ve yeteneklerini keşfederek arama çözümlerinizi geliştirebilirsiniz.

Daha fazla yardım için [Azure Cognitive Search dokümantasyonunu](https://learn.microsoft.com/en-us/azure/search/?wt.mc_id=studentamb_258691) ziyaret edin.

**Feragatname**:  
Bu belge, AI çeviri servisi [Co-op Translator](https://github.com/Azure/co-op-translator) kullanılarak çevrilmiştir. Doğruluk için çaba gösterilse de, otomatik çevirilerin hatalar veya yanlışlıklar içerebileceğini lütfen unutmayınız. Orijinal belge, kendi dilinde yetkili kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel insan çevirisi önerilir. Bu çevirinin kullanımı sonucu oluşabilecek yanlış anlamalar veya yorum hatalarından sorumlu değiliz.