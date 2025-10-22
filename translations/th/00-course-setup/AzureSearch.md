<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f0ce2d470f3efad6f8c7df376f416a4b",
  "translation_date": "2025-07-12T07:37:11+00:00",
  "source_file": "00-course-setup/AzureSearch.md",
  "language_code": "th"
}
-->
# Azure AI Search Setup Guide

คู่มือนี้จะช่วยให้คุณตั้งค่า Azure AI Search ผ่านทาง Azure portal ทำตามขั้นตอนด้านล่างเพื่อสร้างและกำหนดค่าบริการ Azure AI Search ของคุณ

## Prerequisites

ก่อนเริ่มต้น ให้ตรวจสอบว่าคุณมีสิ่งต่อไปนี้:

- บัญชีสมาชิก Azure หากคุณยังไม่มีบัญชีสมาชิก Azure คุณสามารถสร้างบัญชีฟรีได้ที่ [Azure Free Account](https://azure.microsoft.com/free/?wt.mc_id=studentamb_258691)

## Step 1: Create an Azure AI Search Service

1. ลงชื่อเข้าใช้ที่ [Azure portal](https://portal.azure.com/?wt.mc_id=studentamb_258691)
2. ในแถบนำทางด้านซ้าย คลิกที่ **Create a resource**
3. ในช่องค้นหา พิมพ์ "Azure AI Search" แล้วเลือก **Azure AI Search** จากรายการผลลัพธ์
4. คลิกปุ่ม **Create**
5. ในแท็บ **Basics** กรอกข้อมูลดังนี้:
   - **Subscription**: เลือกบัญชีสมาชิก Azure ของคุณ
   - **Resource group**: สร้าง resource group ใหม่หรือเลือกกลุ่มที่มีอยู่แล้ว
   - **Resource name**: กรอกชื่อที่ไม่ซ้ำสำหรับบริการค้นหาของคุณ
   - **Region**: เลือกภูมิภาคที่ใกล้กับผู้ใช้ของคุณมากที่สุด
   - **Pricing tier**: เลือกระดับราคาที่เหมาะสมกับความต้องการ คุณสามารถเริ่มต้นด้วยระดับ Free สำหรับการทดสอบ
6. คลิก **Review + create**
7. ตรวจสอบการตั้งค่าแล้วคลิก **Create** เพื่อสร้างบริการค้นหา

## Step 2: Get Started with Azure AI Search

1. เมื่อติดตั้งเสร็จสมบูรณ์ ให้ไปที่บริการค้นหาของคุณใน Azure portal
2. ในหน้าภาพรวมของบริการค้นหา คลิกปุ่ม **Quickstart**
3. ทำตามขั้นตอนในคู่มือ Quickstart เพื่อสร้างดัชนี อัปโหลดข้อมูล และทำการค้นหา

### Create an Index

1. ในคู่มือ Quickstart คลิกที่ **Create an index**
2. กำหนดโครงสร้างดัชนีโดยระบุฟิลด์และคุณสมบัติของฟิลด์เหล่านั้น (เช่น ประเภทข้อมูล, สามารถค้นหาได้, สามารถกรองได้)
3. คลิก **Create** เพื่อสร้างดัชนี

### Upload Data

1. ในคู่มือ Quickstart คลิกที่ **Upload data**
2. เลือกแหล่งข้อมูล (เช่น Azure Blob Storage, Azure SQL Database) และกรอกรายละเอียดการเชื่อมต่อที่จำเป็น
3. ทำการแมปฟิลด์จากแหล่งข้อมูลไปยังฟิลด์ในดัชนี
4. คลิก **Submit** เพื่ออัปโหลดข้อมูลไปยังดัชนี

### Perform a Search Query

1. ในคู่มือ Quickstart คลิกที่ **Search explorer**
2. กรอกคำค้นหาในช่องค้นหาเพื่อลองทดสอบฟังก์ชันการค้นหา
3. ตรวจสอบผลลัพธ์การค้นหาและปรับแต่งโครงสร้างดัชนีหรือข้อมูลตามความจำเป็น

## Step 3: Use Azure AI Search Tools

Azure AI Search สามารถทำงานร่วมกับเครื่องมือต่างๆ เพื่อเพิ่มประสิทธิภาพการค้นหา คุณสามารถใช้ Azure CLI, Python SDK และเครื่องมืออื่นๆ สำหรับการตั้งค่าขั้นสูงและการดำเนินการต่างๆ

### Using Azure CLI

1. ติดตั้ง Azure CLI โดยทำตามคำแนะนำที่ [Install Azure CLI](https://learn.microsoft.com/en-us/cli/azure/install-azure-cli?wt.mc_id=studentamb_258691)
2. ลงชื่อเข้าใช้ Azure CLI ด้วยคำสั่ง:
   ```bash
   az login
   ```
3. สร้างบริการค้นหาใหม่โดยใช้ Azure CLI:
   ```bash
   az search service create --resource-group <resource-group> --name <service-name> --sku Free
   ```
4. สร้างดัชนีโดยใช้ Azure CLI:
   ```bash
   az search index create --service-name <service-name> --name <index-name> --fields "field1:type, field2:type"
   ```

### Using Python SDK

1. ติดตั้งไลบรารี Azure Cognitive Search สำหรับ Python:
   ```bash
   pip install azure-search-documents
   ```
2. ใช้โค้ด Python ด้านล่างเพื่อสร้างดัชนีและอัปโหลดเอกสาร:
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

สำหรับข้อมูลเพิ่มเติม โปรดดูเอกสารดังต่อไปนี้:

- [Create an Azure Cognitive Search service](https://learn.microsoft.com/en-us/azure/search/search-create-service-portal?wt.mc_id=studentamb_258691)
- [Get started with Azure Cognitive Search](https://learn.microsoft.com/en-us/azure/search/search-get-started-portal?wt.mc_id=studentamb_258691)
- [Azure AI Search Tools](https://learn.microsoft.com/en-us/azure/ai-services/agents/how-to/tools/azure-ai-search?tabs=azurecli%2Cpython&pivots=code-examples?wt.mc_id=studentamb_258691)

## Conclusion

คุณได้ตั้งค่า Azure AI Search ผ่าน Azure portal และเครื่องมือที่เกี่ยวข้องเรียบร้อยแล้ว ตอนนี้คุณสามารถสำรวจฟีเจอร์และความสามารถขั้นสูงของ Azure AI Search เพื่อพัฒนาการค้นหาของคุณให้ดียิ่งขึ้น

หากต้องการความช่วยเหลือเพิ่มเติม โปรดเยี่ยมชม [Azure Cognitive Search documentation](https://learn.microsoft.com/en-us/azure/search/?wt.mc_id=studentamb_258691)

**ข้อจำกัดความรับผิดชอบ**:  
เอกสารนี้ได้รับการแปลโดยใช้บริการแปลภาษาอัตโนมัติ [Co-op Translator](https://github.com/Azure/co-op-translator) แม้เราจะพยายามให้ความถูกต้องสูงสุด แต่โปรดทราบว่าการแปลอัตโนมัติอาจมีข้อผิดพลาดหรือความไม่ถูกต้อง เอกสารต้นฉบับในภาษาต้นทางถือเป็นแหล่งข้อมูลที่เชื่อถือได้ สำหรับข้อมูลที่สำคัญ ขอแนะนำให้ใช้บริการแปลโดยผู้เชี่ยวชาญมนุษย์ เราไม่รับผิดชอบต่อความเข้าใจผิดหรือการตีความผิดที่เกิดขึ้นจากการใช้การแปลนี้