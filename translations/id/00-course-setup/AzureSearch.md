# Panduan Pengaturan Azure AI Search

Panduan ini akan membantu Anda mengatur Azure AI Search menggunakan portal Azure. Ikuti langkah-langkah di bawah ini untuk membuat dan mengonfigurasi layanan Azure AI Search Anda.

## Prasyarat

Sebelum Anda mulai, pastikan Anda memiliki hal-hal berikut:

- Langganan Azure. Jika Anda belum memiliki langganan Azure, Anda dapat membuat akun gratis di [Azure Free Account](https://azure.microsoft.com/free/?wt.mc_id=studentamb_258691).

## Langkah 1: Membuat Akun Penyimpanan Azure

1. Ikuti instruksi ini, [Create an Azure storage account](https://learn.microsoft.com/azure/storage/common/storage-account-create?tabs=azure-portal), untuk membuat Akun Penyimpanan Azure baru.
   **NOTE**: Pastikan tipe Akun Penyimpanan adalah Standard General Purpose V2.

## Langkah 2: Membuat Layanan Azure AI Search

1. Masuk ke [portal Azure](https://portal.azure.com/?wt.mc_id=studentamb_258691).
2. Di panel navigasi sebelah kiri, klik **Create a resource**.
3. Di kotak pencarian, ketik "Azure AI Search" dan pilih **Azure AI Search** dari daftar hasil.
4. Klik tombol **Create**.
5. Di tab **Basics**, isi informasi berikut:
   - **Subscription**: Pilih langganan Azure Anda.
   - **Resource group**: Buat grup sumber daya baru atau pilih yang sudah ada.
   - **Resource name**: Masukkan nama unik untuk layanan pencarian Anda.
   - **Region**: Pilih wilayah terdekat dengan pengguna Anda.
   - **Pricing tier**: Pilih tingkat harga yang sesuai dengan kebutuhan Anda. Anda dapat memulai dengan tier Gratis untuk pengujian.
6. Klik **Review + create**.
7. Tinju pengaturan dan klik **Create** untuk membuat layanan pencarian.

## Langkah 3: Memulai dengan Azure AI Search

1. Setelah penyebaran selesai, navigasi ke layanan pencarian Anda di portal Azure.
2. Di panel ringkasan layanan pencarian, salin URL tersebut. URL tersebut akan terlihat seperti `https://<service-name>.search.windows.net`.
3. **(Direkomendasikan)** Aktifkan akses tanpa kunci dengan Microsoft Entra ID (RBAC) seperti yang ditunjukkan pada Langkah 4 di bawah — tidak perlu kunci. Contoh dalam panduan ini membuat/memperbarui indeks dan mengunggah dokumen, yang membutuhkan peran **Search Service Contributor** dan **Search Index Data Contributor** (atau, untuk autentikasi berbasis kunci, menggunakan **primary admin key** — bukan query key). Hanya jika Anda tidak dapat menggunakan RBAC, buka panel **Settings > Keys** dan salin **primary admin key**.
4. Ikuti langkah-langkah di halaman [Panduan cepat](https://learn.microsoft.com/azure/search/search-get-started-portal?pivots=import-data-new) untuk membuat indeks, mengunggah data, dan melakukan pencarian.

## Langkah 4: Gunakan Alat Azure AI Search

Azure AI Search terintegrasi dengan berbagai alat untuk meningkatkan kemampuan pencarian Anda. Anda dapat menggunakan Azure CLI, Python SDK, .NET SDK, dan alat lainnya untuk konfigurasi dan operasi tingkat lanjut.

### Menggunakan Azure CLI

1. Instal Azure CLI dengan mengikuti instruksi di [Install Azure CLI](https://learn.microsoft.com/cli/azure/install-azure-cli?wt.mc_id=studentamb_258691).
2. Masuk ke Azure CLI menggunakan perintah:

   ```bash
   az login
   ```
3. **(Direkomendasikan) Aktifkan akses tanpa kunci dengan Microsoft Entra ID (RBAC):**

    ```bash
    az search service update --name <service-name> --resource-group <resource-group> --auth-options aadOrApiKey
    az role assignment create --assignee <your-user-or-principal-id> --role "Search Service Contributor" --scope $(az search service show -g <resource-group> -n <service-name> --query id -o tsv)
    az role assignment create --assignee <your-user-or-principal-id> --role "Search Index Data Contributor" --scope $(az search service show -g <resource-group> -n <service-name> --query id -o tsv)
    # az search service show tidak memiliki bidang "endpoint"; buat URL dari nama layanan.
    export AZURE_SEARCH_SERVICE_ENDPOINT="https://<service-name>.search.windows.net"
    ```

    Dengan RBAC diaktifkan, contoh Python dan .NET SDK di bawah mengautentikasi menggunakan `DefaultAzureCredential`, yang menggunakan sesi `az login` Anda selama pengembangan lokal — tidak perlu kunci admin. Lihat [Connect to Azure AI Search using roles](https://learn.microsoft.com/azure/search/search-security-rbac).

4. **(Cadangan) Autentikasi berbasis kunci** — hanya jika Anda tidak dapat menggunakan RBAC, simpan juga kunci admin:

#### Simpan baik endpoint maupun API key untuk instance Azure AI Search ke variabel lingkungan.

    ```bash
    # zsh/bash
    # az search service show tidak memiliki field "endpoint"; buat URL dari nama layanan.
    export AZURE_SEARCH_SERVICE_ENDPOINT="https://<service-name>.search.windows.net"
    export AZURE_SEARCH_API_KEY=$(az search admin-key show -g <resource-group> --service-name <service-name> --query "primaryKey" -o tsv)
    ```

    ```powershell
    # PowerShell
    # az search service show tidak memiliki field "endpoint"; buat URL dari nama layanan.
    $env:AZURE_SEARCH_SERVICE_ENDPOINT = "https://<service-name>.search.windows.net"
    $env:AZURE_SEARCH_API_KEY = $(az search admin-key show -g <resource-group> --service-name <service-name> --query "primaryKey" -o tsv)
    ```

### Menggunakan Python SDK

1. Instal perpustakaan klien Azure Cognitive Search dan Azure Identity untuk Python:

   ```bash
   pip install azure-search-documents azure-identity
   ```

2. Gunakan kode Python berikut untuk membuat indeks dan mengunggah dokumen:

    ```python
    import os
    from azure.identity import DefaultAzureCredential
    from azure.search.documents import SearchClient
    from azure.search.documents.indexes import SearchIndexClient
    from azure.search.documents.indexes.models import SearchIndex, SimpleField, edm

    service_endpoint = os.getenv("AZURE_SEARCH_SERVICE_ENDPOINT")
    index_name = "sample-index"

    # Keyless (disarankan): menggunakan identitas `az login` Anda melalui Entra ID RBAC.
    # Memerlukan peran "Search Service Contributor" dan "Search Index Data Contributor".
    credential = DefaultAzureCredential()
    # Cadangan (otentikasi berbasis kunci):
    # dari azure.core.credentials impor AzureKeyCredential
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

### Menggunakan .NET SDK

1. Jalankan perintah berikut untuk membuat indeks dan mengunggah dokumen:

    ```bash
    dotnet run ./AzureSearch.cs
    ```

    Contoh .NET di bawah menggunakan `DefaultAzureCredential`, yang dapat menggunakan sign-in Azure CLI Anda dari `az login` selama pengembangan lokal.

2. Berikut kode .NET dari `AzureSearch.cs`:

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

Untuk informasi lebih rinci, lihat dokumentasi berikut:

- [Buat layanan Azure Cognitive Search](https://learn.microsoft.com/azure/search/search-create-service-portal?wt.mc_id=studentamb_258691)
- [Mulai dengan Azure Cognitive Search](https://learn.microsoft.com/azure/search/search-get-started-portal?wt.mc_id=studentamb_258691)
- [Alat Azure AI Search](https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-ai-search?tabs=azurecli%2Cpython&pivots=code-examples?wt.mc_id=studentamb_258691)

## Kesimpulan

Anda telah berhasil mengatur Azure AI Search menggunakan portal Azure dan alat terkait. Kini Anda dapat mengeksplorasi fitur dan kemampuan Azure AI Search yang lebih canggih untuk meningkatkan solusi pencarian Anda.

Untuk bantuan lebih lanjut, kunjungi [dokumentasi Azure Cognitive Search](https://learn.microsoft.com/azure/search/?wt.mc_id=studentamb_258691).

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Penafian**:
Dokumen ini telah diterjemahkan menggunakan layanan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Meskipun kami berupaya untuk mencapai akurasi, harap diketahui bahwa terjemahan otomatis mungkin mengandung kesalahan atau ketidakakuratan. Dokumen asli dalam bahasa aslinya harus dianggap sebagai sumber yang sah. Untuk informasi penting, disarankan menggunakan terjemahan profesional oleh manusia. Kami tidak bertanggung jawab atas kesalahpahaman atau penafsiran yang keliru yang timbul dari penggunaan terjemahan ini.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->