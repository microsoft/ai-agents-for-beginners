# Azure AI 搜索设置指南

本指南将帮助您使用 Azure 门户设置 Azure AI 搜索。请按照以下步骤创建和配置您的 Azure AI 搜索服务。

## 先决条件

在开始之前，请确保您具备以下条件：

- 一个 Azure 订阅。如果您没有 Azure 订阅，可以在 [Azure 免费帐户](https://azure.microsoft.com/free/?wt.mc_id=studentamb_258691) 上创建一个。

## 步骤 1：创建 Azure AI 搜索服务

1. 登录 [Azure 门户](https://portal.azure.com/?wt.mc_id=studentamb_258691)。
2. 在左侧导航窗格中，单击 **创建资源**。
3. 在搜索框中，键入 "Azure Cognitive Search"，然后从结果列表中选择 **Azure Cognitive Search**。
4. 单击 **创建** 按钮。
5. 在 **基础** 选项卡中，提供以下信息：
   - **订阅**：选择您的 Azure 订阅。
   - **资源组**：创建一个新的资源组或选择一个现有的资源组。
   - **资源名称**：为您的搜索服务输入一个唯一的名称。
   - **区域**：选择最靠近您的用户的区域。
   - **定价层**：选择适合您需求的定价层。您可以从免费层开始进行测试。
6. 单击 **查看 + 创建**。
7. 查看设置并单击 **创建** 以创建搜索服务。

## 步骤 2：开始使用 Azure AI 搜索

1. 部署完成后，在 Azure 门户中导航到您的搜索服务。
2. 在搜索服务概述页面中，单击 **快速入门** 按钮。
3. 按照快速入门指南中的步骤创建索引、上传数据和执行搜索查询。

### 创建索引

1. 在快速入门指南中，单击 **创建索引**。
2. 通过指定字段及其属性（例如，数据类型、可搜索、可筛选）来定义索引架构。
3. 单击 **创建** 以创建索引。

### 上传数据

1. 在快速入门指南中，单击 **上传数据**。
2. 选择一个数据源（例如，Azure Blob 存储、Azure SQL 数据库）并提供必要的连接详细信息。
3. 将数据源字段映射到索引字段。
4. 单击 **提交** 以上传数据到索引。

### 执行搜索查询

1. 在快速入门指南中，单击 **搜索浏览器**。
2. 在搜索框中输入搜索查询以测试搜索功能。
3. 查看搜索结果并根据需要调整索引架构或数据。

## 步骤 3：使用 Azure AI 搜索工具

Azure AI 搜索与各种工具集成，以增强您的搜索能力。您可以使用 Azure CLI、Python SDK 和其他工具进行高级配置和操作。

### 使用 Azure CLI

1. 按照 [安装 Azure CLI](https://learn.microsoft.com/zh-CN/cli/azure/install-azure-cli?wt.mc_id=studentamb_258691) 上的说明安装 Azure CLI。
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

1. 安装适用于 Python 的 Azure Cognitive Search 客户端库：

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

有关更多详细信息，请参阅以下文档：

- [创建 Azure Cognitive Search 服务](https://learn.microsoft.com/zh-cn/azure/search/search-create-service-portal?wt.mc_id=studentamb_258691)
- [开始使用 Azure Cognitive Search](https://learn.microsoft.com/zh-cn/azure/search/search-get-started-portal?wt.mc_id=studentamb_258691)
- [Azure AI 搜索工具](https://learn.microsoft.com/zh-cn/azure/ai-services/agents/how-to/tools/azure-ai-search?tabs=azurecli%2Cpython&pivots=code-examples?wt.mc_id=studentamb_258691)

## 总结

您已使用 Azure 门户和集成工具成功设置了 Azure AI 搜索。现在，您可以探索 Azure AI 搜索的更多高级特性和功能，以增强您的搜索解决方案。

如需进一步的帮助，请访问 [Azure Cognitive Search 文档](https://learn.microsoft.com/zh-cn/azure/search/?wt.mc_id=studentamb_258691)。
