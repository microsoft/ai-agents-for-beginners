<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "11e38db0898a788612b917e329dcdb5b",
  "translation_date": "2025-11-07T08:44:01+00:00",
  "source_file": "00-course-setup/AzureSearch.md",
  "language_code": "ms"
}
-->
# Panduan Penyediaan Azure AI Search

Panduan ini akan membantu anda menyediakan Azure AI Search menggunakan portal Azure. Ikuti langkah-langkah di bawah untuk mencipta dan mengkonfigurasi perkhidmatan Azure AI Search anda.

## Prasyarat

Sebelum anda bermula, pastikan anda mempunyai perkara berikut:

- Langganan Azure. Jika anda belum mempunyai langganan Azure, anda boleh mencipta akaun percuma di [Azure Free Account](https://azure.microsoft.com/free/?wt.mc_id=studentamb_258691).

## Langkah 1: Cipta Akaun Penyimpanan Azure

1. Ikuti arahan ini, [Cipta akaun penyimpanan Azure](https://learn.microsoft.com/azure/storage/common/storage-account-create?tabs=azure-portal), untuk mencipta Akaun Penyimpanan Azure yang baharu.
   **NOTE**: Pastikan jenis Akaun Penyimpanan adalah Standard General Purpose V2.

## Langkah 2: Cipta Perkhidmatan Azure AI Search

1. Log masuk ke [portal Azure](https://portal.azure.com/?wt.mc_id=studentamb_258691).
2. Di panel navigasi sebelah kiri, klik pada **Create a resource**.
3. Dalam kotak carian, taip "Azure AI Search" dan pilih **Azure AI Search** daripada senarai hasil.
4. Klik butang **Create**.
5. Dalam tab **Basics**, sediakan maklumat berikut:
   - **Subscription**: Pilih langganan Azure anda.
   - **Resource group**: Cipta kumpulan sumber baharu atau pilih yang sedia ada.
   - **Resource name**: Masukkan nama unik untuk perkhidmatan carian anda.
   - **Region**: Pilih kawasan yang paling dekat dengan pengguna anda.
   - **Pricing tier**: Pilih tahap harga yang sesuai dengan keperluan anda. Anda boleh bermula dengan tahap Percuma untuk ujian.
6. Klik **Review + create**.
7. Semak tetapan dan klik **Create** untuk mencipta perkhidmatan carian.

## Langkah 3: Bermula dengan Azure AI Search

1. Setelah penyebaran selesai, navigasi ke perkhidmatan carian anda di portal Azure.
2. Di panel gambaran keseluruhan perkhidmatan carian, salin URL. Ia sepatutnya kelihatan seperti `https://<service-name>.search.windows.net`.
3. Di panel Settings > Keys, salin kunci pertanyaan.
4. Ikuti langkah-langkah di halaman [Panduan Pantas](https://learn.microsoft.com/azure/search/search-get-started-portal?pivots=import-data-new) untuk mencipta indeks, memuat naik data, dan menjalankan pertanyaan carian.

## Langkah 4: Gunakan Alat Azure AI Search

Azure AI Search berintegrasi dengan pelbagai alat untuk meningkatkan keupayaan carian anda. Anda boleh menggunakan Azure CLI, Python SDK, .NET SDK dan alat lain untuk konfigurasi dan operasi lanjutan.

### Menggunakan Azure CLI

1. Pasang Azure CLI dengan mengikuti arahan di [Pasang Azure CLI](https://learn.microsoft.com/cli/azure/install-azure-cli?wt.mc_id=studentamb_258691).
2. Log masuk ke Azure CLI menggunakan arahan:

   ```bash
   az login
   ```

3. Simpan kedua-dua endpoint dan kunci API untuk instance Azure AI Search ke dalam pembolehubah persekitaran.

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

1. Pasang pustaka klien Azure Cognitive Search untuk Python:

   ```bash
   pip install azure-search-documents
   ```

2. Gunakan kod Python berikut untuk mencipta indeks dan memuat naik dokumen:

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

1. Jalankan arahan berikut untuk mencipta indeks dan memuat naik dokumen:

    ```bash
    dotnet run ./AzureSearch.cs
    ```

2. Berikut adalah kod .NET untuk `AzureSearch.cs`:

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

Untuk maklumat lebih terperinci, rujuk dokumentasi berikut:

- [Cipta perkhidmatan Azure Cognitive Search](https://learn.microsoft.com/azure/search/search-create-service-portal?wt.mc_id=studentamb_258691)
- [Bermula dengan Azure Cognitive Search](https://learn.microsoft.com/azure/search/search-get-started-portal?wt.mc_id=studentamb_258691)
- [Alat Azure AI Search](https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-ai-search?tabs=azurecli%2Cpython&pivots=code-examples?wt.mc_id=studentamb_258691)

## Kesimpulan

Anda telah berjaya menyediakan Azure AI Search menggunakan portal Azure dan alat yang diintegrasikan. Anda kini boleh meneroka ciri dan keupayaan lanjutan Azure AI Search untuk meningkatkan penyelesaian carian anda.

Untuk bantuan lanjut, lawati [dokumentasi Azure Cognitive Search](https://learn.microsoft.com/azure/search/?wt.mc_id=studentamb_258691).

---

**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan perkhidmatan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Walaupun kami berusaha untuk ketepatan, sila ambil perhatian bahawa terjemahan automatik mungkin mengandungi kesilapan atau ketidaktepatan. Dokumen asal dalam bahasa asalnya harus dianggap sebagai sumber yang berwibawa. Untuk maklumat penting, terjemahan manusia profesional adalah disyorkan. Kami tidak bertanggungjawab atas sebarang salah faham atau salah tafsir yang timbul daripada penggunaan terjemahan ini.