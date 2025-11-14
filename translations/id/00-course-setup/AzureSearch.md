<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "11e38db0898a788612b917e329dcdb5b",
  "translation_date": "2025-11-07T08:43:27+00:00",
  "source_file": "00-course-setup/AzureSearch.md",
  "language_code": "id"
}
-->
# Panduan Pengaturan Azure AI Search

Panduan ini akan membantu Anda mengatur Azure AI Search menggunakan portal Azure. Ikuti langkah-langkah di bawah ini untuk membuat dan mengonfigurasi layanan Azure AI Search Anda.

## Prasyarat

Sebelum memulai, pastikan Anda memiliki hal berikut:

- Langganan Azure. Jika Anda belum memiliki langganan Azure, Anda dapat membuat akun gratis di [Azure Free Account](https://azure.microsoft.com/free/?wt.mc_id=studentamb_258691).

## Langkah 1: Buat Akun Penyimpanan Azure

1. Ikuti petunjuk ini, [Buat akun penyimpanan Azure](https://learn.microsoft.com/azure/storage/common/storage-account-create?tabs=azure-portal), untuk membuat Akun Penyimpanan Azure baru.
   **NOTE**: Pastikan jenis Akun Penyimpanan adalah Standard General Purpose V2.

## Langkah 2: Buat Layanan Azure AI Search

1. Masuk ke [portal Azure](https://portal.azure.com/?wt.mc_id=studentamb_258691).
2. Di panel navigasi sebelah kiri, klik **Create a resource**.
3. Di kotak pencarian, ketik "Azure AI Search" dan pilih **Azure AI Search** dari daftar hasil.
4. Klik tombol **Create**.
5. Di tab **Basics**, berikan informasi berikut:
   - **Subscription**: Pilih langganan Azure Anda.
   - **Resource group**: Buat grup sumber daya baru atau pilih yang sudah ada.
   - **Resource name**: Masukkan nama unik untuk layanan pencarian Anda.
   - **Region**: Pilih wilayah yang paling dekat dengan pengguna Anda.
   - **Pricing tier**: Pilih tingkat harga yang sesuai dengan kebutuhan Anda. Anda dapat memulai dengan tingkat Gratis untuk pengujian.
6. Klik **Review + create**.
7. Tinjau pengaturan dan klik **Create** untuk membuat layanan pencarian.

## Langkah 3: Mulai dengan Azure AI Search

1. Setelah penyebaran selesai, navigasikan ke layanan pencarian Anda di portal Azure.
2. Di panel ikhtisar layanan pencarian, salin URL. URL tersebut akan terlihat seperti `https://<service-name>.search.windows.net`.
3. Di Settings > Keys, salin query key.
4. Ikuti langkah-langkah di halaman [Panduan Memulai Cepat](https://learn.microsoft.com/azure/search/search-get-started-portal?pivots=import-data-new) untuk membuat indeks, mengunggah data, dan melakukan kueri pencarian.

## Langkah 4: Gunakan Alat Azure AI Search

Azure AI Search terintegrasi dengan berbagai alat untuk meningkatkan kemampuan pencarian Anda. Anda dapat menggunakan Azure CLI, Python SDK, .NET SDK, dan alat lainnya untuk konfigurasi dan operasi lanjutan.

### Menggunakan Azure CLI

1. Instal Azure CLI dengan mengikuti petunjuk di [Instal Azure CLI](https://learn.microsoft.com/cli/azure/install-azure-cli?wt.mc_id=studentamb_258691).
2. Masuk ke Azure CLI menggunakan perintah:

   ```bash
   az login
   ```

3. Simpan endpoint dan API key untuk instance Azure AI Search ke variabel lingkungan.

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

### Menggunakan Python SDK

1. Instal pustaka klien Azure Cognitive Search untuk Python:

   ```bash
   pip install azure-search-documents
   ```

2. Gunakan kode Python berikut untuk membuat indeks dan mengunggah dokumen:

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

### Menggunakan .NET SDK

1. Jalankan perintah berikut untuk membuat indeks dan mengunggah dokumen:

    ```bash
    dotnet run ./AzureSearch.cs
    ```

2. Berikut adalah kode .NET dari `AzureSearch.cs`:

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

Untuk informasi lebih rinci, lihat dokumentasi berikut:

- [Buat layanan Azure Cognitive Search](https://learn.microsoft.com/azure/search/search-create-service-portal?wt.mc_id=studentamb_258691)
- [Mulai dengan Azure Cognitive Search](https://learn.microsoft.com/azure/search/search-get-started-portal?wt.mc_id=studentamb_258691)
- [Alat Azure AI Search](https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-ai-search?tabs=azurecli%2Cpython&pivots=code-examples?wt.mc_id=studentamb_258691)

## Kesimpulan

Anda telah berhasil mengatur Azure AI Search menggunakan portal Azure dan alat terintegrasi. Sekarang Anda dapat menjelajahi fitur dan kemampuan lanjutan Azure AI Search untuk meningkatkan solusi pencarian Anda.

Untuk bantuan lebih lanjut, kunjungi [dokumentasi Azure Cognitive Search](https://learn.microsoft.com/azure/search/?wt.mc_id=studentamb_258691).

---

**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan layanan penerjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Meskipun kami berupaya untuk memberikan hasil yang akurat, harap diketahui bahwa terjemahan otomatis mungkin mengandung kesalahan atau ketidakakuratan. Dokumen asli dalam bahasa aslinya harus dianggap sebagai sumber yang otoritatif. Untuk informasi yang bersifat kritis, disarankan menggunakan jasa penerjemahan manusia profesional. Kami tidak bertanggung jawab atas kesalahpahaman atau penafsiran yang timbul dari penggunaan terjemahan ini.