# Panduan Persediaan Azure AI Search

Panduan ini akan membantu anda menyediakan Azure AI Search menggunakan portal Azure. Ikuti langkah-langkah di bawah untuk mencipta dan mengkonfigurasi perkhidmatan Azure AI Search anda.

## Prasyarat

Sebelum anda bermula, pastikan anda mempunyai perkara berikut:

- Langganan Azure. Jika anda tidak mempunyai langganan Azure, anda boleh mencipta akaun percuma di [Azure Free Account](https://azure.microsoft.com/free/?wt.mc_id=studentamb_258691).

## Langkah 1: Cipta Akaun Penyimpanan Azure

1. Ikuti arahan ini, [Create an Azure storage account](https://learn.microsoft.com/azure/storage/common/storage-account-create?tabs=azure-portal), untuk mencipta Akaun Penyimpanan Azure baru.
   **NOTE**: Pastikan jenis Akaun Penyimpanan adalah Standard General Purpose V2.

## Langkah 2: Cipta Perkhidmatan Azure AI Search

1. Log masuk ke [portal Azure](https://portal.azure.com/?wt.mc_id=studentamb_258691).
2. Dalam panel navigasi di sebelah kiri, klik **Create a resource**.
3. Dalam kotak carian, taip "Azure AI Search" dan pilih **Azure AI Search** daripada senarai hasil.
4. Klik butang **Create**.
5. Dalam tab **Basics**, isikan maklumat berikut:
   - **Subscription**: Pilih langganan Azure anda.
   - **Resource group**: Cipta kumpulan sumber baru atau pilih yang sedia ada.
   - **Resource name**: Masukkan nama unik untuk perkhidmatan carian anda.
   - **Region**: Pilih rantau yang paling dekat dengan pengguna anda.
   - **Pricing tier**: Pilih tier harga yang sesuai dengan keperluan anda. Anda boleh bermula dengan tier Percuma untuk ujian.
6. Klik **Review + create**.
7. Semak tetapan dan klik **Create** untuk mencipta perkhidmatan carian.

## Langkah 3: Bermula dengan Azure AI Search

1. Setelah penyebaran selesai, pergi ke perkhidmatan carian anda di portal Azure.
2. Dalam panel gambaran keseluruhan perkhidmatan carian, salin URL tersebut. Ia sepatutnya kelihatan seperti `https://<service-name>.search.windows.net`.
3. **(Disyorkan)** Aktifkan akses tanpa kunci dengan Microsoft Entra ID (RBAC) seperti yang ditunjukkan dalam Langkah 4 di bawah — tiada kunci diperlukan. Sampel dalam panduan ini mencipta/mengemas kini indeks dan memuat naik dokumen, yang memerlukan peranan **Search Service Contributor** dan **Search Index Data Contributor** (atau, untuk pengesahan berasaskan kunci, **primary admin key** — bukan query key). Hanya jika anda tidak dapat menggunakan RBAC, buka panel **Settings > Keys** dan salin **primary admin key**.
4. Ikuti langkah dalam halaman [Quickstart guide](https://learn.microsoft.com/azure/search/search-get-started-portal?pivots=import-data-new) untuk mencipta indeks, memuat naik data, dan menjalankan carian.

## Langkah 4: Gunakan Alat Azure AI Search

Azure AI Search berintegrasi dengan pelbagai alat untuk meningkatkan keupayaan carian anda. Anda boleh menggunakan Azure CLI, Python SDK, .NET SDK dan alat lain untuk konfigurasi dan operasi lanjutan.

### Menggunakan Azure CLI

1. Pasang Azure CLI dengan mengikuti arahan di [Install Azure CLI](https://learn.microsoft.com/cli/azure/install-azure-cli?wt.mc_id=studentamb_258691).
2. Log masuk ke Azure CLI menggunakan arahan:

   ```bash
   az login
   ```
3. **(Disyorkan) Aktifkan akses tanpa kunci dengan Microsoft Entra ID (RBAC):**

    ```bash
    az search service update --name <service-name> --resource-group <resource-group> --auth-options aadOrApiKey
    az role assignment create --assignee <your-user-or-principal-id> --role "Search Service Contributor" --scope $(az search service show -g <resource-group> -n <service-name> --query id -o tsv)
    az role assignment create --assignee <your-user-or-principal-id> --role "Search Index Data Contributor" --scope $(az search service show -g <resource-group> -n <service-name> --query id -o tsv)
    # az search service show tidak mempunyai medan "endpoint"; bina URL dari nama perkhidmatan.
    export AZURE_SEARCH_SERVICE_ENDPOINT="https://<service-name>.search.windows.net"
    ```

    Dengan RBAC diaktifkan, sampel Python dan .NET SDK di bawah mengesahkan dengan `DefaultAzureCredential`, yang menggunakan sesi `az login` anda semasa pembangunan tempatan — tiada kunci admin diperlukan. Lihat [Connect to Azure AI Search using roles](https://learn.microsoft.com/azure/search/search-security-rbac).

4. **(Fallback) Pengesahan berasaskan kunci** — hanya jika anda tidak dapat menggunakan RBAC, simpan kunci admin juga:

#### Simpan kedua-dua endpoint dan API key untuk contoh Azure AI Search ke pembolehubah persekitaran.

    ```bash
    # zsh/bash
    # az search service show tidak mempunyai medan "endpoint"; bina URL dari nama perkhidmatan.
    export AZURE_SEARCH_SERVICE_ENDPOINT="https://<service-name>.search.windows.net"
    export AZURE_SEARCH_API_KEY=$(az search admin-key show -g <resource-group> --service-name <service-name> --query "primaryKey" -o tsv)
    ```

    ```powershell
    # PowerShell
    # az search service show tidak mempunyai medan "endpoint"; bina URL dari nama perkhidmatan.
    $env:AZURE_SEARCH_SERVICE_ENDPOINT = "https://<service-name>.search.windows.net"
    $env:AZURE_SEARCH_API_KEY = $(az search admin-key show -g <resource-group> --service-name <service-name> --query "primaryKey" -o tsv)
    ```

### Menggunakan Python SDK

1. Pasang perpustakaan klien Azure Cognitive Search dan Azure Identity untuk Python:

   ```bash
   pip install azure-search-documents azure-identity
   ```

2. Gunakan kod Python berikut untuk mencipta indeks dan memuat naik dokumen:

    ```python
    import os
    from azure.identity import DefaultAzureCredential
    from azure.search.documents import SearchClient
    from azure.search.documents.indexes import SearchIndexClient
    from azure.search.documents.indexes.models import SearchIndex, SimpleField, edm

    service_endpoint = os.getenv("AZURE_SEARCH_SERVICE_ENDPOINT")
    index_name = "sample-index"

    # Tanpa kunci (disyorkan): menggunakan identiti `az login` anda melalui Entra ID RBAC.
    # Memerlukan peranan "Search Service Contributor" dan "Search Index Data Contributor".
    credential = DefaultAzureCredential()
    # Sandaran (pengesahan berasaskan kunci):
    # dari azure.core.credentials import AzureKeyCredential
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

1. Jalankan arahan berikut untuk mencipta indeks dan memuat naik dokumen:

    ```bash
    dotnet run ./AzureSearch.cs
    ```

    Sampel .NET di bawah menggunakan `DefaultAzureCredential`, yang boleh menggunakan log masuk Azure CLI anda dari `az login` semasa pembangunan tempatan.

2. Berikut adalah kod .NET untuk `AzureSearch.cs`:

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

Untuk maklumat lebih terperinci, rujuk dokumentasi berikut:

- [Create an Azure Cognitive Search service](https://learn.microsoft.com/azure/search/search-create-service-portal?wt.mc_id=studentamb_258691)
- [Get started with Azure Cognitive Search](https://learn.microsoft.com/azure/search/search-get-started-portal?wt.mc_id=studentamb_258691)
- [Azure AI Search Tools](https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-ai-search?tabs=azurecli%2Cpython&pivots=code-examples?wt.mc_id=studentamb_258691)

## Kesimpulan

Anda telah berjaya menyediakan Azure AI Search menggunakan portal Azure dan mengintegrasikan alat-alat. Anda boleh meneroka ciri dan keupayaan Azure AI Search yang lebih maju untuk meningkatkan penyelesaian carian anda.

Untuk bantuan lanjut, lawati [dokumentasi Azure Cognitive Search](https://learn.microsoft.com/azure/search/?wt.mc_id=studentamb_258691).

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Penafian**:
Dokumen ini telah diterjemahkan menggunakan perkhidmatan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Walaupun kami berusaha untuk ketepatan, sila ambil maklum bahawa terjemahan automatik mungkin mengandungi kesilapan atau ketidaktepatan. Dokumen asal dalam bahasa asalnya harus dianggap sebagai sumber yang sahih. Untuk maklumat penting, terjemahan oleh manusia profesional adalah disyorkan. Kami tidak bertanggungjawab terhadap sebarang salah faham atau salah tafsir yang timbul daripada penggunaan terjemahan ini.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->