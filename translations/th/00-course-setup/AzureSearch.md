<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "11e38db0898a788612b917e329dcdb5b",
  "translation_date": "2025-11-07T08:38:14+00:00",
  "source_file": "00-course-setup/AzureSearch.md",
  "language_code": "th"
}
-->
# คู่มือการตั้งค่า Azure AI Search

คู่มือนี้จะช่วยคุณตั้งค่า Azure AI Search โดยใช้ Azure portal ทำตามขั้นตอนด้านล่างเพื่อสร้างและกำหนดค่าบริการ Azure AI Search ของคุณ

## ข้อกำหนดเบื้องต้น

ก่อนเริ่มต้น ตรวจสอบให้แน่ใจว่าคุณมีสิ่งต่อไปนี้:

- การสมัครใช้งาน Azure หากคุณยังไม่มีบัญชี Azure คุณสามารถสร้างบัญชีฟรีได้ที่ [Azure Free Account](https://azure.microsoft.com/free/?wt.mc_id=studentamb_258691)

## ขั้นตอนที่ 1: สร้างบัญชี Azure Storage

1. ทำตามคำแนะนำนี้ [Create an Azure storage account](https://learn.microsoft.com/azure/storage/common/storage-account-create?tabs=azure-portal) เพื่อสร้างบัญชี Azure Storage ใหม่  
   **NOTE**: ตรวจสอบให้แน่ใจว่าประเภทของบัญชี Storage เป็น Standard General Purpose V2

## ขั้นตอนที่ 2: สร้างบริการ Azure AI Search

1. ลงชื่อเข้าใช้ [Azure portal](https://portal.azure.com/?wt.mc_id=studentamb_258691)
2. ในแถบนำทางด้านซ้าย คลิกที่ **Create a resource**
3. ในช่องค้นหา พิมพ์ "Azure AI Search" และเลือก **Azure AI Search** จากรายการผลลัพธ์
4. คลิกปุ่ม **Create**
5. ในแท็บ **Basics** ให้กรอกข้อมูลดังนี้:
   - **Subscription**: เลือกการสมัครใช้งาน Azure ของคุณ
   - **Resource group**: สร้างกลุ่มทรัพยากรใหม่หรือเลือกกลุ่มที่มีอยู่แล้ว
   - **Resource name**: ใส่ชื่อที่ไม่ซ้ำสำหรับบริการค้นหาของคุณ
   - **Region**: เลือกภูมิภาคที่ใกล้กับผู้ใช้งานของคุณมากที่สุด
   - **Pricing tier**: เลือกระดับราคาที่เหมาะสมกับความต้องการของคุณ คุณสามารถเริ่มต้นด้วยระดับ Free สำหรับการทดสอบ
6. คลิก **Review + create**
7. ตรวจสอบการตั้งค่าและคลิก **Create** เพื่อสร้างบริการค้นหา

## ขั้นตอนที่ 3: เริ่มต้นใช้งาน Azure AI Search

1. เมื่อการปรับใช้เสร็จสมบูรณ์ ให้ไปที่บริการค้นหาของคุณใน Azure portal
2. ในแผงภาพรวมของบริการค้นหา ให้คัดลอก URL ซึ่งควรมีลักษณะดังนี้ `https://<service-name>.search.windows.net`
3. ใน Settings > Keys ให้คัดลอก query key
4. ทำตามขั้นตอนในหน้า [Quickstart guide](https://learn.microsoft.com/azure/search/search-get-started-portal?pivots=import-data-new) เพื่อสร้างดัชนี อัปโหลดข้อมูล และดำเนินการค้นหา

## ขั้นตอนที่ 4: ใช้เครื่องมือ Azure AI Search

Azure AI Search สามารถทำงานร่วมกับเครื่องมือต่างๆ เพื่อเพิ่มประสิทธิภาพการค้นหา คุณสามารถใช้ Azure CLI, Python SDK, .NET SDK และเครื่องมืออื่นๆ สำหรับการตั้งค่าขั้นสูงและการดำเนินการ

### การใช้ Azure CLI

1. ติดตั้ง Azure CLI โดยทำตามคำแนะนำที่ [Install Azure CLI](https://learn.microsoft.com/cli/azure/install-azure-cli?wt.mc_id=studentamb_258691)
2. ลงชื่อเข้าใช้ Azure CLI โดยใช้คำสั่ง:

   ```bash
   az login
   ```

3. เก็บ endpoint และ API key ของ Azure AI Search instance ไว้ใน environment variables

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

### การใช้ Python SDK

1. ติดตั้งไลบรารี Azure Cognitive Search client สำหรับ Python:

   ```bash
   pip install azure-search-documents
   ```

2. ใช้โค้ด Python ด้านล่างเพื่อสร้างดัชนีและอัปโหลดเอกสาร:

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

### การใช้ .NET SDK

1. รันคำสั่งด้านล่างเพื่อสร้างดัชนีและอัปโหลดเอกสาร:

    ```bash
    dotnet run ./AzureSearch.cs
    ```

2. นี่คือโค้ด .NET ของ `AzureSearch.cs`:

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

สำหรับข้อมูลเพิ่มเติม ดูเอกสารดังต่อไปนี้:

- [Create an Azure Cognitive Search service](https://learn.microsoft.com/azure/search/search-create-service-portal?wt.mc_id=studentamb_258691)
- [Get started with Azure Cognitive Search](https://learn.microsoft.com/azure/search/search-get-started-portal?wt.mc_id=studentamb_258691)
- [Azure AI Search Tools](https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-ai-search?tabs=azurecli%2Cpython&pivots=code-examples?wt.mc_id=studentamb_258691)

## สรุป

คุณได้ตั้งค่า Azure AI Search โดยใช้ Azure portal และเครื่องมือที่เกี่ยวข้องเรียบร้อยแล้ว ตอนนี้คุณสามารถสำรวจฟีเจอร์และความสามารถขั้นสูงของ Azure AI Search เพื่อปรับปรุงโซลูชันการค้นหาของคุณได้

หากต้องการความช่วยเหลือเพิ่มเติม โปรดเยี่ยมชม [Azure Cognitive Search documentation](https://learn.microsoft.com/azure/search/?wt.mc_id=studentamb_258691)

---

**ข้อจำกัดความรับผิดชอบ**:  
เอกสารนี้ได้รับการแปลโดยใช้บริการแปลภาษา AI [Co-op Translator](https://github.com/Azure/co-op-translator) แม้ว่าเราจะพยายามให้การแปลมีความถูกต้อง แต่โปรดทราบว่าการแปลโดยอัตโนมัติอาจมีข้อผิดพลาดหรือความไม่ถูกต้อง เอกสารต้นฉบับในภาษาดั้งเดิมควรถือเป็นแหล่งข้อมูลที่เชื่อถือได้ สำหรับข้อมูลที่สำคัญ ขอแนะนำให้ใช้บริการแปลภาษามืออาชีพ เราไม่รับผิดชอบต่อความเข้าใจผิดหรือการตีความผิดที่เกิดจากการใช้การแปลนี้