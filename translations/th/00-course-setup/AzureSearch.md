# คู่มือการตั้งค่า Azure AI Search

คู่มือนี้จะช่วยคุณตั้งค่า Azure AI Search โดยใช้พอร์ทัล Azure ปฏิบัติตามขั้นตอนด้านล่างเพื่อสร้างและกำหนดค่าบริการ Azure AI Search ของคุณ

## ข้อกำหนดเบื้องต้น

ก่อนเริ่มต้น ให้ตรวจสอบว่าคุณมีสิ่งต่อไปนี้:

- การสมัครใช้งาน Azure หากคุณยังไม่มีการสมัครใช้งาน Azure คุณสามารถสร้างบัญชีฟรีได้ที่ [Azure Free Account](https://azure.microsoft.com/free/?wt.mc_id=studentamb_258691)

## ขั้นตอนที่ 1: สร้างบัญชีที่เก็บข้อมูล Azure

1. ทำตามคำแนะนำนี้, [Create an Azure storage account](https://learn.microsoft.com/azure/storage/common/storage-account-create?tabs=azure-portal) เพื่อสร้างบัญชีที่เก็บข้อมูล Azure ใหม่
   **หมายเหตุ**: ให้แน่ใจว่าประเภทของบัญชีที่เก็บข้อมูลเป็น Standard General Purpose V2

## ขั้นตอนที่ 2: สร้างบริการ Azure AI Search

1. ลงชื่อเข้าใช้ [Azure portal](https://portal.azure.com/?wt.mc_id=studentamb_258691)
2. ในแผงนำทางด้านซ้าย คลิกที่ **Create a resource**
3. ในช่องค้นหา พิมพ์ "Azure AI Search" แล้วเลือก **Azure AI Search** จากรายการผลลัพธ์
4. คลิกปุ่ม **Create**
5. ในแท็บ **Basics** กรอกข้อมูลดังนี้:
   - **Subscription**: เลือกการสมัครใช้งาน Azure ของคุณ
   - **Resource group**: สร้างกลุ่มทรัพยากรใหม่หรือเลือกกลุ่มที่มีอยู่แล้ว
   - **Resource name**: กรอกชื่อที่ไม่ซ้ำสำหรับบริการค้นหาของคุณ
   - **Region**: เลือกภูมิภาคที่ใกล้เคียงกับผู้ใช้ของคุณมากที่สุด
   - **Pricing tier**: เลือกระดับราคาที่เหมาะสมกับความต้องการของคุณ คุณสามารถเริ่มต้นด้วยระดับฟรีสำหรับการทดสอบ
6. คลิก **Review + create**
7. ตรวจสอบการตั้งค่าและคลิก **Create** เพื่อสร้างบริการค้นหา

## ขั้นตอนที่ 3: เริ่มต้นใช้งาน Azure AI Search

1. เมื่อติดตั้งเสร็จสมบูรณ์ ให้ไปยังบริการค้นหาของคุณในพอร์ทัล Azure
2. ในแผงภาพรวมบริการค้นหา ให้คัดลอก URL ที่ควรมีลักษณะเช่น `https://<service-name>.search.windows.net`
3. **(แนะนำ)** เปิดใช้งานการเข้าถึงโดยไม่ใช้กุญแจผ่าน Microsoft Entra ID (RBAC) ดังที่แสดงในขั้นตอนที่ 4 ด้านล่าง — ไม่ต้องใช้กุญแจ ตัวอย่างในคู่มือนี้สร้าง/อัปเดตดัชนีและอัปโหลดเอกสาร ซึ่งต้องการบทบาท **Search Service Contributor** และ **Search Index Data Contributor** (หรือ สำหรับการยืนยันตัวตนด้วยกุญแจใช้ **primary admin key** — ไม่ใช่กุญแจสำหรับการค้นหา) หากคุณไม่สามารถใช้ RBAC ได้ ให้เปิดแผง **Settings > Keys** และคัดลอก **primary admin key**
4. ปฏิบัติตามขั้นตอนในหน้า [Quickstart guide](https://learn.microsoft.com/azure/search/search-get-started-portal?pivots=import-data-new) เพื่อสร้างดัชนี อัปโหลดข้อมูล และทำการค้นหา

## ขั้นตอนที่ 4: ใช้เครื่องมือ Azure AI Search

Azure AI Search ผสานรวมกับเครื่องมือหลายชนิดเพื่อเพิ่มประสิทธิภาพการค้นหาของคุณ คุณสามารถใช้ Azure CLI, Python SDK, .NET SDK และเครื่องมืออื่น ๆ สำหรับการกำหนดค่าขั้นสูงและการดำเนินงาน

### การใช้ Azure CLI

1. ติดตั้ง Azure CLI โดยทำตามคำแนะนำที่ [Install Azure CLI](https://learn.microsoft.com/cli/azure/install-azure-cli?wt.mc_id=studentamb_258691)
2. ลงชื่อเข้าใช้ Azure CLI โดยใช้คำสั่ง:

   ```bash
   az login
   ```
3. **(แนะนำ) เปิดใช้งานการเข้าถึงโดยไม่ใช้กุญแจผ่าน Microsoft Entra ID (RBAC):**

    ```bash
    az search service update --name <service-name> --resource-group <resource-group> --auth-options aadOrApiKey
    az role assignment create --assignee <your-user-or-principal-id> --role "Search Service Contributor" --scope $(az search service show -g <resource-group> -n <service-name> --query id -o tsv)
    az role assignment create --assignee <your-user-or-principal-id> --role "Search Index Data Contributor" --scope $(az search service show -g <resource-group> -n <service-name> --query id -o tsv)
    # az search service show has no "endpoint" field; build the URL from the service name.
    export AZURE_SEARCH_SERVICE_ENDPOINT="https://<service-name>.search.windows.net"
    ```

    เมื่อเปิดใช้งาน RBAC ตัวอย่าง Python และ .NET SDK ด้านล่างจะยืนยันตัวตนด้วย `DefaultAzureCredential` ซึ่งใช้ `az login` session ของคุณในระหว่างการพัฒนาท้องถิ่น — ไม่ต้องใช้กุญแจ admin ดูที่ [Connect to Azure AI Search using roles](https://learn.microsoft.com/azure/search/search-security-rbac)

4. **(ลักษณะสำรอง) การยืนยันตัวตนด้วยกุญแจ** — เฉพาะเมื่อคุณไม่สามารถใช้ RBAC ได้ ให้เก็บกุญแจ admin ไว้ด้วย:

#### เก็บทั้ง endpoint และ API key ของอินสแตนซ์ Azure AI Search ไปยังตัวแปรสภาพแวดล้อม

   * **zsh / bash**
     ```bash
     # az search service show has no "endpoint" field; build the URL from the service name.
     export AZURE_SEARCH_SERVICE_ENDPOINT="https://<service-name>.search.windows.net"
     export AZURE_SEARCH_API_KEY=$(az search admin-key show -g <resource-group> --service-name <service-name> --query "primaryKey" -o tsv)
     ```

   * **PowerShell**
     ```powershell
     # az search service show has no "endpoint" field; build the URL from the service name.
     $env:AZURE_SEARCH_SERVICE_ENDPOINT = "https://<service-name>.search.windows.net"
     $env:AZURE_SEARCH_API_KEY = $(az search admin-key show -g <resource-group> --service-name <service-name> --query "primaryKey" -o tsv)
     ```

### การใช้ Python SDK

1. ติดตั้งไลบรารี Azure Cognitive Search client และ Azure Identity สำหรับ Python:

   ```bash
   pip install azure-search-documents azure-identity
   ```

2. ใช้โค้ด Python ต่อไปนี้เพื่อสร้างดัชนีและอัปโหลดเอกสาร:

    ```python
    import os
    from azure.identity import DefaultAzureCredential
    from azure.search.documents import SearchClient
    from azure.search.documents.indexes import SearchIndexClient
    from azure.search.documents.indexes.models import SearchIndex, SimpleField, edm

    service_endpoint = os.getenv("AZURE_SEARCH_SERVICE_ENDPOINT")
    index_name = "sample-index"

    # Keyless (recommended): uses your `az login` identity via Entra ID RBAC.
    # Requires the "Search Service Contributor" and "Search Index Data Contributor" roles.
    credential = DefaultAzureCredential()
    # Fallback (key-based auth):
    # from azure.core.credentials import AzureKeyCredential
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

### การใช้ .NET SDK

1. รันคำสั่งต่อไปนี้เพื่อสร้างดัชนีและอัปโหลดเอกสาร:

    ```bash
    dotnet run ./AzureSearch.cs
    ```

    ตัวอย่าง .NET ด้านล่างใช้ `DefaultAzureCredential` ซึ่งสามารถใช้ Azure CLI sign-in ของคุณจาก `az login` ในระหว่างการพัฒนาท้องถิ่น

2. นี่คือโค้ด .NET ของ `AzureSearch.cs`:

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

สำหรับข้อมูลโดยละเอียดเพิ่มเติม โปรดดูเอกสารต่อไปนี้:

- [Create an Azure Cognitive Search service](https://learn.microsoft.com/azure/search/search-create-service-portal?wt.mc_id=studentamb_258691)
- [Get started with Azure Cognitive Search](https://learn.microsoft.com/azure/search/search-get-started-portal?wt.mc_id=studentamb_258691)
- [Azure AI Search Tools](https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-ai-search?tabs=azurecli%2Cpython&pivots=code-examples?wt.mc_id=studentamb_258691)

## สรุป

คุณได้ตั้งค่า Azure AI Search สำเร็จโดยใช้พอร์ทัล Azure และเครื่องมือผสานรวม คุณสามารถสำรวจฟีเจอร์และความสามารถขั้นสูงของ Azure AI Search เพื่อเพิ่มประสิทธิภาพโซลูชันการค้นหาของคุณ

หากต้องการความช่วยเหลือเพิ่มเติม โปรดเยี่ยมชม [Azure Cognitive Search documentation](https://learn.microsoft.com/azure/search/?wt.mc_id=studentamb_258691)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ปฏิเสธความรับผิดชอบ**:
เอกสารนี้ได้รับการแปลโดยใช้บริการแปลภาษา AI [Co-op Translator](https://github.com/Azure/co-op-translator) ขณะที่เราพยายามให้ความถูกต้อง โปรดทราบว่าการแปลโดยอัตโนมัติอาจมีข้อผิดพลาดหรือความไม่ถูกต้อง เอกสารต้นฉบับในภาษาต้นทางควรถูกพิจารณาเป็นแหล่งข้อมูลที่เชื่อถือได้ สำหรับข้อมูลที่สำคัญ แนะนำให้ใช้การแปลโดยมนุษย์มืออาชีพ เราไม่รับผิดชอบต่อความเข้าใจผิดหรือการตีความที่ผิดพลาดที่เกิดขึ้นจากการใช้การแปลนี้
<!-- CO-OP TRANSLATOR DISCLAIMER END -->