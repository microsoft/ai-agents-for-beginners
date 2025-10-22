<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f0ce2d470f3efad6f8c7df376f416a4b",
  "translation_date": "2025-07-12T07:34:03+00:00",
  "source_file": "00-course-setup/AzureSearch.md",
  "language_code": "zh"
}
-->
# Azure AI Search 设置指南

本指南将帮助你通过 Azure 门户设置 Azure AI Search。请按照以下步骤创建并配置你的 Azure AI Search 服务。

## 前提条件

开始之前，请确保你具备以下条件：

- 一个 Azure 订阅。如果你还没有 Azure 订阅，可以在 [Azure 免费账户](https://azure.microsoft.com/free/?wt.mc_id=studentamb_258691) 创建一个免费账户。

## 第一步：创建 Azure AI Search 服务

1. 登录到 [Azure 门户](https://portal.azure.com/?wt.mc_id=studentamb_258691)。
2. 在左侧导航栏中，点击 **创建资源**。
3. 在搜索框中输入 “Azure AI Search”，然后从结果列表中选择 **Azure AI Search**。
4. 点击 **创建** 按钮。
5. 在 **基础** 选项卡中，填写以下信息：
   - **订阅**：选择你的 Azure 订阅。
   - **资源组**：创建新的资源组或选择已有的资源组。
   - **资源名称**：输入你的搜索服务的唯一名称。
   - **区域**：选择离你的用户最近的区域。
   - **定价层**：选择适合你需求的定价层。你可以先选择免费层进行测试。
6. 点击 **查看 + 创建**。
7. 检查设置无误后，点击 **创建** 来创建搜索服务。

## 第二步：开始使用 Azure AI Search

1. 部署完成后，进入 Azure 门户中的搜索服务页面。
2. 在搜索服务概览页，点击 **快速入门** 按钮。
3. 按照快速入门指南的步骤创建索引、上传数据并执行搜索查询。

### 创建索引

1. 在快速入门指南中，点击 **创建索引**。
2. 定义索引架构，指定字段及其属性（例如，数据类型、是否可搜索、是否可筛选）。
3. 点击 **创建** 来创建索引。

### 上传数据

1. 在快速入门指南中，点击 **上传数据**。
2. 选择数据源（例如 Azure Blob 存储、Azure SQL 数据库），并提供必要的连接信息。
3. 将数据源字段映射到索引字段。
4. 点击 **提交** 将数据上传到索引。

### 执行搜索查询

1. 在快速入门指南中，点击 **搜索资源管理器**。
2. 在搜索框中输入查询语句，测试搜索功能。
3. 查看搜索结果，根据需要调整索引架构或数据。

## 第三步：使用 Azure AI Search 工具

Azure AI Search 支持多种工具，帮助你增强搜索功能。你可以使用 Azure CLI、Python SDK 以及其他工具进行高级配置和操作。

### 使用 Azure CLI

1. 按照 [安装 Azure CLI](https://learn.microsoft.com/en-us/cli/azure/install-azure-cli?wt.mc_id=studentamb_258691) 的说明安装 Azure CLI。
2. 使用以下命令登录 Azure CLI：
   ```bash
   az login
   ```
3. 使用 Azure CLI 创建新的搜索服务：
   ```bash
   az search service create --resource-group <resource-group> --name <service-name> --sku Free
   ```
4. 使用 Azure CLI 创建索引：
   ```bash
   az search index create --service-name <service-name> --name <index-name> --fields "field1:type, field2:type"
   ```

### 使用 Python SDK

1. 安装 Azure Cognitive Search 的 Python 客户端库：
   ```bash
   pip install azure-search-documents
   ```
2. 使用以下 Python 代码创建索引并上传文档：
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

更多详细信息，请参考以下文档：

- [创建 Azure Cognitive Search 服务](https://learn.microsoft.com/en-us/azure/search/search-create-service-portal?wt.mc_id=studentamb_258691)
- [开始使用 Azure Cognitive Search](https://learn.microsoft.com/en-us/azure/search/search-get-started-portal?wt.mc_id=studentamb_258691)
- [Azure AI Search 工具](https://learn.microsoft.com/en-us/azure/ai-services/agents/how-to/tools/azure-ai-search?tabs=azurecli%2Cpython&pivots=code-examples?wt.mc_id=studentamb_258691)

## 结论

你已成功通过 Azure 门户及集成工具完成 Azure AI Search 的设置。现在可以进一步探索 Azure AI Search 的高级功能和能力，提升你的搜索解决方案。

如需更多帮助，请访问 [Azure Cognitive Search 文档](https://learn.microsoft.com/en-us/azure/search/?wt.mc_id=studentamb_258691)。

**免责声明**：  
本文件使用 AI 翻译服务 [Co-op Translator](https://github.com/Azure/co-op-translator) 进行翻译。虽然我们力求准确，但请注意，自动翻译可能包含错误或不准确之处。原始文件的母语版本应被视为权威来源。对于重要信息，建议使用专业人工翻译。对于因使用本翻译而产生的任何误解或误释，我们不承担任何责任。