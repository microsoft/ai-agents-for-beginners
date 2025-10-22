<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f0ce2d470f3efad6f8c7df376f416a4b",
  "translation_date": "2025-07-12T07:38:38+00:00",
  "source_file": "00-course-setup/AzureSearch.md",
  "language_code": "id"
}
-->
# Panduan Pengaturan Azure AI Search

Panduan ini akan membantu Anda mengatur Azure AI Search menggunakan portal Azure. Ikuti langkah-langkah di bawah ini untuk membuat dan mengonfigurasi layanan Azure AI Search Anda.

## Prasyarat

Sebelum memulai, pastikan Anda memiliki hal berikut:

- Langganan Azure. Jika Anda belum memiliki langganan Azure, Anda dapat membuat akun gratis di [Azure Free Account](https://azure.microsoft.com/free/?wt.mc_id=studentamb_258691).

## Langkah 1: Membuat Layanan Azure AI Search

1. Masuk ke [portal Azure](https://portal.azure.com/?wt.mc_id=studentamb_258691).
2. Di panel navigasi sebelah kiri, klik **Create a resource**.
3. Di kotak pencarian, ketik "Azure AI Search" dan pilih **Azure AI Search** dari daftar hasil.
4. Klik tombol **Create**.
5. Pada tab **Basics**, isi informasi berikut:
   - **Subscription**: Pilih langganan Azure Anda.
   - **Resource group**: Buat resource group baru atau pilih yang sudah ada.
   - **Resource name**: Masukkan nama unik untuk layanan pencarian Anda.
   - **Region**: Pilih wilayah yang paling dekat dengan pengguna Anda.
   - **Pricing tier**: Pilih tier harga yang sesuai dengan kebutuhan Anda. Anda bisa mulai dengan tier Gratis untuk pengujian.
6. Klik **Review + create**.
7. Tinjau pengaturan dan klik **Create** untuk membuat layanan pencarian.

## Langkah 2: Memulai dengan Azure AI Search

1. Setelah penyebaran selesai, buka layanan pencarian Anda di portal Azure.
2. Di halaman ringkasan layanan pencarian, klik tombol **Quickstart**.
3. Ikuti langkah-langkah dalam panduan Quickstart untuk membuat indeks, mengunggah data, dan melakukan kueri pencarian.

### Membuat Indeks

1. Dalam panduan Quickstart, klik **Create an index**.
2. Tentukan skema indeks dengan menyebutkan bidang dan atributnya (misalnya, tipe data, dapat dicari, dapat difilter).
3. Klik **Create** untuk membuat indeks.

### Mengunggah Data

1. Dalam panduan Quickstart, klik **Upload data**.
2. Pilih sumber data (misalnya, Azure Blob Storage, Azure SQL Database) dan berikan detail koneksi yang diperlukan.
3. Pemetaan bidang sumber data ke bidang indeks.
4. Klik **Submit** untuk mengunggah data ke indeks.

### Melakukan Kueri Pencarian

1. Dalam panduan Quickstart, klik **Search explorer**.
2. Masukkan kueri pencarian di kotak pencarian untuk menguji fungsi pencarian.
3. Tinjau hasil pencarian dan sesuaikan skema indeks atau data jika diperlukan.

## Langkah 3: Menggunakan Alat Azure AI Search

Azure AI Search terintegrasi dengan berbagai alat untuk meningkatkan kemampuan pencarian Anda. Anda dapat menggunakan Azure CLI, Python SDK, dan alat lainnya untuk konfigurasi dan operasi lanjutan.

### Menggunakan Azure CLI

1. Instal Azure CLI dengan mengikuti petunjuk di [Install Azure CLI](https://learn.microsoft.com/en-us/cli/azure/install-azure-cli?wt.mc_id=studentamb_258691).
2. Masuk ke Azure CLI menggunakan perintah:
   ```bash
   az login
   ```
3. Buat layanan pencarian baru menggunakan Azure CLI:
   ```bash
   az search service create --resource-group <resource-group> --name <service-name> --sku Free
   ```
4. Buat indeks menggunakan Azure CLI:
   ```bash
   az search index create --service-name <service-name> --name <index-name> --fields "field1:type, field2:type"
   ```

### Menggunakan Python SDK

1. Instal pustaka klien Azure Cognitive Search untuk Python:
   ```bash
   pip install azure-search-documents
   ```
2. Gunakan kode Python berikut untuk membuat indeks dan mengunggah dokumen:
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

Untuk informasi lebih rinci, lihat dokumentasi berikut:

- [Create an Azure Cognitive Search service](https://learn.microsoft.com/en-us/azure/search/search-create-service-portal?wt.mc_id=studentamb_258691)
- [Get started with Azure Cognitive Search](https://learn.microsoft.com/en-us/azure/search/search-get-started-portal?wt.mc_id=studentamb_258691)
- [Azure AI Search Tools](https://learn.microsoft.com/en-us/azure/ai-services/agents/how-to/tools/azure-ai-search?tabs=azurecli%2Cpython&pivots=code-examples?wt.mc_id=studentamb_258691)

## Kesimpulan

Anda telah berhasil mengatur Azure AI Search menggunakan portal Azure dan alat yang terintegrasi. Sekarang Anda dapat mengeksplorasi fitur dan kemampuan Azure AI Search yang lebih canggih untuk meningkatkan solusi pencarian Anda.

Untuk bantuan lebih lanjut, kunjungi [Azure Cognitive Search documentation](https://learn.microsoft.com/en-us/azure/search/?wt.mc_id=studentamb_258691).

**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan layanan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Meskipun kami berupaya untuk akurasi, harap diketahui bahwa terjemahan otomatis mungkin mengandung kesalahan atau ketidakakuratan. Dokumen asli dalam bahasa aslinya harus dianggap sebagai sumber yang sah. Untuk informasi penting, disarankan menggunakan terjemahan profesional oleh manusia. Kami tidak bertanggung jawab atas kesalahpahaman atau penafsiran yang keliru yang timbul dari penggunaan terjemahan ini.