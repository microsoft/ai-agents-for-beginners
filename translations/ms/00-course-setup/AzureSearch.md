<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f0ce2d470f3efad6f8c7df376f416a4b",
  "translation_date": "2025-07-12T07:38:47+00:00",
  "source_file": "00-course-setup/AzureSearch.md",
  "language_code": "ms"
}
-->
# Panduan Persediaan Azure AI Search

Panduan ini akan membantu anda menyediakan Azure AI Search menggunakan portal Azure. Ikuti langkah-langkah di bawah untuk mencipta dan mengkonfigurasi perkhidmatan Azure AI Search anda.

## Prasyarat

Sebelum anda bermula, pastikan anda mempunyai perkara berikut:

- Langganan Azure. Jika anda belum mempunyai langganan Azure, anda boleh mencipta akaun percuma di [Azure Free Account](https://azure.microsoft.com/free/?wt.mc_id=studentamb_258691).

## Langkah 1: Cipta Perkhidmatan Azure AI Search

1. Log masuk ke [portal Azure](https://portal.azure.com/?wt.mc_id=studentamb_258691).
2. Dalam panel navigasi sebelah kiri, klik **Create a resource**.
3. Dalam kotak carian, taip "Azure AI Search" dan pilih **Azure AI Search** daripada senarai hasil.
4. Klik butang **Create**.
5. Dalam tab **Basics**, berikan maklumat berikut:
   - **Subscription**: Pilih langganan Azure anda.
   - **Resource group**: Cipta kumpulan sumber baru atau pilih yang sedia ada.
   - **Resource name**: Masukkan nama unik untuk perkhidmatan carian anda.
   - **Region**: Pilih rantau yang paling dekat dengan pengguna anda.
   - **Pricing tier**: Pilih tahap harga yang sesuai dengan keperluan anda. Anda boleh mulakan dengan tahap Percuma untuk ujian.
6. Klik **Review + create**.
7. Semak tetapan dan klik **Create** untuk mencipta perkhidmatan carian.

## Langkah 2: Mula Menggunakan Azure AI Search

1. Setelah penyebaran selesai, pergi ke perkhidmatan carian anda dalam portal Azure.
2. Pada halaman gambaran keseluruhan perkhidmatan carian, klik butang **Quickstart**.
3. Ikuti langkah dalam panduan Quickstart untuk mencipta indeks, memuat naik data, dan menjalankan pertanyaan carian.

### Cipta Indeks

1. Dalam panduan Quickstart, klik **Create an index**.
2. Tentukan skema indeks dengan menyatakan medan dan atributnya (contohnya, jenis data, boleh dicari, boleh ditapis).
3. Klik **Create** untuk mencipta indeks.

### Muat Naik Data

1. Dalam panduan Quickstart, klik **Upload data**.
2. Pilih sumber data (contohnya, Azure Blob Storage, Azure SQL Database) dan berikan butiran sambungan yang diperlukan.
3. Peta medan sumber data ke medan indeks.
4. Klik **Submit** untuk memuat naik data ke indeks.

### Jalankan Pertanyaan Carian

1. Dalam panduan Quickstart, klik **Search explorer**.
2. Masukkan pertanyaan carian dalam kotak carian untuk menguji fungsi carian.
3. Semak hasil carian dan laraskan skema indeks atau data jika perlu.

## Langkah 3: Gunakan Alat Azure AI Search

Azure AI Search boleh diintegrasikan dengan pelbagai alat untuk meningkatkan keupayaan carian anda. Anda boleh menggunakan Azure CLI, Python SDK, dan alat lain untuk konfigurasi dan operasi lanjutan.

### Menggunakan Azure CLI

1. Pasang Azure CLI dengan mengikuti arahan di [Install Azure CLI](https://learn.microsoft.com/en-us/cli/azure/install-azure-cli?wt.mc_id=studentamb_258691).
2. Log masuk ke Azure CLI menggunakan arahan:
   ```bash
   az login
   ```
3. Cipta perkhidmatan carian baru menggunakan Azure CLI:
   ```bash
   az search service create --resource-group <resource-group> --name <service-name> --sku Free
   ```
4. Cipta indeks menggunakan Azure CLI:
   ```bash
   az search index create --service-name <service-name> --name <index-name> --fields "field1:type, field2:type"
   ```

### Menggunakan Python SDK

1. Pasang perpustakaan klien Azure Cognitive Search untuk Python:
   ```bash
   pip install azure-search-documents
   ```
2. Gunakan kod Python berikut untuk mencipta indeks dan memuat naik dokumen:
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

Untuk maklumat lebih terperinci, rujuk dokumentasi berikut:

- [Create an Azure Cognitive Search service](https://learn.microsoft.com/en-us/azure/search/search-create-service-portal?wt.mc_id=studentamb_258691)
- [Get started with Azure Cognitive Search](https://learn.microsoft.com/en-us/azure/search/search-get-started-portal?wt.mc_id=studentamb_258691)
- [Azure AI Search Tools](https://learn.microsoft.com/en-us/azure/ai-services/agents/how-to/tools/azure-ai-search?tabs=azurecli%2Cpython&pivots=code-examples?wt.mc_id=studentamb_258691)

## Kesimpulan

Anda telah berjaya menyediakan Azure AI Search menggunakan portal Azure dan alat yang diintegrasikan. Kini anda boleh meneroka ciri dan keupayaan lanjutan Azure AI Search untuk meningkatkan penyelesaian carian anda.

Untuk bantuan lanjut, lawati [Azure Cognitive Search documentation](https://learn.microsoft.com/en-us/azure/search/?wt.mc_id=studentamb_258691).

**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan perkhidmatan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Walaupun kami berusaha untuk ketepatan, sila ambil maklum bahawa terjemahan automatik mungkin mengandungi kesilapan atau ketidaktepatan. Dokumen asal dalam bahasa asalnya harus dianggap sebagai sumber yang sahih. Untuk maklumat penting, terjemahan profesional oleh manusia adalah disyorkan. Kami tidak bertanggungjawab atas sebarang salah faham atau salah tafsir yang timbul daripada penggunaan terjemahan ini.