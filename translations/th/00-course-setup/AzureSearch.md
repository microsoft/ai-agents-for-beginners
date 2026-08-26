# คู่มือการติดตั้ง Azure AI Search

คู่มือนี้จะช่วยคุณตั้งค่า Azure AI Search โดยใช้พอร์ทัล Azure โปรดทำตามขั้นตอนด้านล่างเพื่อสร้างและกำหนดค่าบริการ Azure AI Search ของคุณ

## ข้อกำหนดเบื้องต้น

ก่อนเริ่มต้น โปรดตรวจสอบว่าคุณมีสิ่งต่อไปนี้:

- บัญชีสมัครใช้งาน Azure หากคุณยังไม่มีบัญชีสมัครใช้งาน Azure คุณสามารถสร้างบัญชีฟรีได้ที่ [Azure Free Account](https://azure.microsoft.com/free/?wt.mc_id=studentamb_258691)

## ขั้นตอนที่ 1: สร้างบัญชี Storage บน Azure

1. ทำตามคำแนะนำนี้, [Create an Azure storage account](https://learn.microsoft.com/azure/storage/common/storage-account-create?tabs=azure-portal) เพื่อสร้างบัญชี Storage บน Azure ใหม่
   **หมายเหตุ**: โปรดตรวจสอบให้แน่ใจว่าประเภทของบัญชี Storage คือ Standard General Purpose V2

## ขั้นตอนที่ 2: สร้างบริการ Azure AI Search

1. ลงชื่อเข้าใช้ [พอร์ทัล Azure](https://portal.azure.com/?wt.mc_id=studentamb_258691)
2. ในแผงนำทางด้านซ้ายมือ คลิก **Create a resource**
3. ในช่องค้นหา พิมพ์ "Azure AI Search" และเลือก **Azure AI Search** จากรายการผลลัพธ์
4. คลิกปุ่ม **Create**
5. ในแท็บ **Basics** ให้กรอกข้อมูลต่อไปนี้:
   - **Subscription**: เลือกบัญชีสมัครใช้งาน Azure ของคุณ
   - **Resource group**: สร้างกลุ่มทรัพยากรใหม่หรือเลือกกลุ่มที่มีอยู่แล้ว
   - **Resource name**: กรอกชื่อที่ไม่ซ้ำสำหรับบริการค้นหาของคุณ
   - **Region**: เลือกพื้นที่ที่ใกล้ผู้ใช้ของคุณมากที่สุด
   - **Pricing tier**: เลือกระดับราคาที่เหมาะสมกับความต้องการของคุณ คุณสามารถเริ่มต้นด้วยระดับ Free สำหรับการทดสอบ
6. คลิก **Review + create**
7. ตรวจสอบการตั้งค่าและคลิก **Create** เพื่อสร้างบริการค้นหา

## ขั้นตอนที่ 3: เริ่มใช้งาน Azure AI Search

1. เมื่อติดตั้งเสร็จสิ้น ให้ไปที่บริการค้นหาของคุณในพอร์ทัล Azure
2. ในแผงภาพรวมของบริการค้นหา คัดลอก URL ซึ่งควรมีลักษณะเหมือน `https://<service-name>.search.windows.net`
3. **(แนะนำ)** เปิดใช้งานการเข้าถึงแบบไม่ต้องใช้กุญแจด้วย Microsoft Entra ID (RBAC) ดังที่แสดงในขั้นตอนที่ 4 ด้านล่าง — ไม่ต้องใช้กุญแจ ตัวอย่างในคู่มือนี้สร้าง/อัปเดตดัชนีและอัปโหลดเอกสาร ซึ่งต้องการบทบาท **Search Service Contributor** และ **Search Index Data Contributor** (หรือ สำหรับการรับรองความถูกต้องด้วยกุญแจ คือ **กุญแจผู้ดูแลระบบหลัก** — ไม่ใช่กุญแจสำหรับการสืบค้น) เฉพาะกรณีที่ไม่สามารถใช้ RBAC ได้ ให้เปิดแผง **Settings > Keys** และคัดลอก **กุญแจผู้ดูแลระบบหลัก**
4. ทำตามขั้นตอนในหน้า [Quickstart guide](https://learn.microsoft.com/azure/search/search-get-started-portal?pivots=import-data-new) เพื่อสร้างดัชนี อัปโหลดข้อมูล และทำการค้นหา

## ขั้นตอนที่ 4: ใช้เครื่องมือ Azure AI Search

Azure AI Search ผสานรวมกับเครื่องมือต่างๆ เพื่อเพิ่มประสิทธิภาพการค้นหาของคุณ คุณสามารถใช้ Azure CLI, Python SDK, .NET SDK และเครื่องมืออื่น ๆ สำหรับการกำหนดค่าและดำเนินการขั้นสูง

### การใช้ Azure CLI

1. ติดตั้ง Azure CLI โดยทำตามคำแนะนำที่ [Install Azure CLI](https://learn.microsoft.com/cli/azure/install-azure-cli?wt.mc_id=studentamb_258691)
2. ลงชื่อเข้าใช้ Azure CLI โดยใช้คำสั่ง:

   ```bash
   az login
   ```
3. **(แนะนำ) เปิดใช้งานการเข้าถึงแบบไม่ต้องใช้กุญแจด้วย Microsoft Entra ID (RBAC):**

    ```bash
    az search service update --name <service-name> --resource-group <resource-group> --auth-options aadOrApiKey
    az role assignment create --assignee <your-user-or-principal-id> --role "Search Service Contributor" --scope $(az search service show -g <resource-group> -n <service-name> --query id -o tsv)
    az role assignment create --assignee <your-user-or-principal-id> --role "Search Index Data Contributor" --scope $(az search service show -g <resource-group> -n <service-name> --query id -o tsv)
    # az search service show ไม่มีฟิลด์ "endpoint"; สร้าง URL จากชื่อบริการ.
    export AZURE_SEARCH_SERVICE_ENDPOINT="https://<service-name>.search.windows.net"
    ```

    เมื่อใช้ RBAC ที่เปิดใช้งาน ตัวอย่าง Python และ .NET SDK ด้านล่างจะรับรองตัวตนด้วย `DefaultAzureCredential` ซึ่งใช้เซสชัน `az login` ของคุณในระหว่างการพัฒนาในเครื่อง — ไม่ต้องใช้กุญแจผู้ดูแลระบบ ดูรายละเอียดได้ที่ [Connect to Azure AI Search using roles](https://learn.microsoft.com/azure/search/search-security-rbac)

4. **(กรณีสำรอง) การรับรองความถูกต้องด้วยกุญแจ** — เฉพาะในกรณีที่ไม่สามารถใช้ RBAC ได้ ให้เก็บกุญแจผู้ดูแลระบบด้วย:

#### เก็บทั้งจุดสิ้นสุดและกุญแจ API สำหรับอินสแตนซ์ Azure AI Search ลงในตัวแปรสภาพแวดล้อม

    ```bash
    # zsh/bash
    # az search service show ไม่มีฟิลด์ "endpoint"; สร้าง URL จากชื่อบริการ
    export AZURE_SEARCH_SERVICE_ENDPOINT="https://<service-name>.search.windows.net"
    export AZURE_SEARCH_API_KEY=$(az search admin-key show -g <resource-group> --service-name <service-name> --query "primaryKey" -o tsv)
    ```

    ```powershell
    # PowerShell
    # az search service show ไม่มีฟิลด์ "endpoint"; สร้าง URL จากชื่อบริการ
    $env:AZURE_SEARCH_SERVICE_ENDPOINT = "https://<service-name>.search.windows.net"
    $env:AZURE_SEARCH_API_KEY = $(az search admin-key show -g <resource-group> --service-name <service-name> --query "primaryKey" -o tsv)
    ```

### การใช้ Python SDK

1. ติดตั้งไลบรารีไคลเอนต์ Azure Cognitive Search และ Azure Identity สำหรับ Python:

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

    # แบบไม่ใช้กุญแจ (แนะนำ): ใช้ตัวตน `az login` ของคุณผ่าน Entra ID RBAC
    # ต้องการบทบาท "ผู้ร่วมให้บริการค้นหา" และ "ผู้ร่วมข้อมูลดัชนีค้นหา"
    credential = DefaultAzureCredential()
    # สำรอง (การพิสูจน์ตัวตนแบบใช้กุญแจ):
    # จาก azure.core.credentials นำเข้า AzureKeyCredential
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

    ตัวอย่าง .NET ด้านล่างใช้ `DefaultAzureCredential` ซึ่งสามารถใช้การลงชื่อเข้าใช้ Azure CLI ของคุณจาก `az login` ในระหว่างการพัฒนาในเครื่อง

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

คุณได้ตั้งค่า Azure AI Search เรียบร้อยแล้วโดยใช้พอร์ทัล Azure และเครื่องมือที่ผสานรวม คุณสามารถสำรวจคุณสมบัติและความสามารถขั้นสูงเพิ่มเติมของ Azure AI Search เพื่อเพิ่มประสิทธิภาพโซลูชันการค้นหาของคุณ

สำหรับความช่วยเหลือเพิ่มเติม โปรดเยี่ยมชม [เอกสาร Azure Cognitive Search](https://learn.microsoft.com/azure/search/?wt.mc_id=studentamb_258691)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ปฏิเสธความรับผิดชอบ**:
เอกสารนี้ได้รับการแปลโดยใช้บริการแปลภาษา AI [Co-op Translator](https://github.com/Azure/co-op-translator) ขณะที่เราพยายามให้ความถูกต้อง โปรดทราบว่าการแปลโดยอัตโนมัติอาจมีข้อผิดพลาดหรือความไม่ถูกต้อง เอกสารต้นฉบับในภาษาต้นทางควรถูกพิจารณาเป็นแหล่งข้อมูลที่เชื่อถือได้ สำหรับข้อมูลที่สำคัญ แนะนำให้ใช้การแปลโดยมนุษย์มืออาชีพ เราไม่รับผิดชอบต่อความเข้าใจผิดหรือการตีความที่ผิดพลาดที่เกิดขึ้นจากการใช้การแปลนี้
<!-- CO-OP TRANSLATOR DISCLAIMER END -->