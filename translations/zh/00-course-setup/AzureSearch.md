<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "11e38db0898a788612b917e329dcdb5b",
  "translation_date": "2025-11-07T08:26:32+00:00",
  "source_file": "00-course-setup/AzureSearch.md",
  "language_code": "zh"
}
-->
# Azure AI 搜索设置指南

本指南将帮助您通过 Azure 门户设置 Azure AI 搜索服务。请按照以下步骤创建和配置您的 Azure AI 搜索服务。

## 前提条件

在开始之前，请确保您具备以下条件：

- 一个 Azure 订阅。如果您还没有 Azure 订阅，可以在 [Azure 免费账户](https://azure.microsoft.com/free/?wt.mc_id=studentamb_258691) 创建一个免费账户。

## 第一步：创建 Azure 存储账户

1. 按照此说明 [创建 Azure 存储账户](https://learn.microsoft.com/azure/storage/common/storage-account-create?tabs=azure-portal)，创建一个新的 Azure 存储账户。
   **注意**：请确保存储账户类型为标准通用 V2。

## 第二步：创建 Azure AI 搜索服务

1. 登录 [Azure 门户](https://portal.azure.com/?wt.mc_id=studentamb_258691)。
2. 在左侧导航栏中，点击 **创建资源**。
3. 在搜索框中输入 "Azure AI Search"，然后从结果列表中选择 **Azure AI Search**。
4. 点击 **创建** 按钮。
5. 在 **基本信息** 选项卡中提供以下信息：
   - **订阅**：选择您的 Azure 订阅。
   - **资源组**：创建一个新的资源组或选择现有的资源组。
   - **资源名称**：输入您的搜索服务的唯一名称。
   - **区域**：选择离您的用户最近的区域。
   - **定价层**：选择适合您需求的定价层。您可以从免费层开始测试。
6. 点击 **查看 + 创建**。
7. 查看设置后，点击 **创建** 来创建搜索服务。

## 第三步：开始使用 Azure AI 搜索

1. 部署完成后，导航到 Azure 门户中的搜索服务。
2. 在搜索服务概览页面，复制 URL。它的格式应为 `https://<service-name>.search.windows.net`。
3. 在设置 > 密钥页面，复制查询密钥。
4. 按照 [快速入门指南](https://learn.microsoft.com/azure/search/search-get-started-portal?pivots=import-data-new) 页面中的步骤创建索引、上传数据并执行搜索查询。

## 第四步：使用 Azure AI 搜索工具

Azure AI 搜索与多种工具集成，以增强您的搜索功能。您可以使用 Azure CLI、Python SDK、.NET SDK 等工具进行高级配置和操作。

### 使用 Azure CLI

1. 按照 [安装 Azure CLI](https://learn.microsoft.com/cli/azure/install-azure-cli?wt.mc_id=studentamb_258691) 的说明安装 Azure CLI。
2. 使用以下命令登录 Azure CLI：

   ```bash
   az login
   ```

3. 将 Azure AI 搜索实例的端点和 API 密钥存储到环境变量中。

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

### 使用 Python SDK

1. 安装 Azure Cognitive Search 的 Python 客户端库：

   ```bash
   pip install azure-search-documents
   ```

2. 使用以下 Python 代码创建索引并上传文档：

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

### 使用 .NET SDK

1. 运行以下命令创建索引并上传文档：

    ```bash
    dotnet run ./AzureSearch.cs
    ```

2. 以下是 `AzureSearch.cs` 的 .NET 代码：

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

有关更详细的信息，请参考以下文档：

- [创建 Azure Cognitive Search 服务](https://learn.microsoft.com/azure/search/search-create-service-portal?wt.mc_id=studentamb_258691)
- [开始使用 Azure Cognitive Search](https://learn.microsoft.com/azure/search/search-get-started-portal?wt.mc_id=studentamb_258691)
- [Azure AI 搜索工具](https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-ai-search?tabs=azurecli%2Cpython&pivots=code-examples?wt.mc_id=studentamb_258691)

## 结论

您已成功通过 Azure 门户设置了 Azure AI 搜索服务并集成了相关工具。现在，您可以探索 Azure AI 搜索的更多高级功能和能力，以增强您的搜索解决方案。

如需进一步帮助，请访问 [Azure Cognitive Search 文档](https://learn.microsoft.com/azure/search/?wt.mc_id=studentamb_258691)。

---

**免责声明**：  
本文档使用AI翻译服务[Co-op Translator](https://github.com/Azure/co-op-translator)进行翻译。尽管我们努力确保翻译的准确性，但请注意，自动翻译可能包含错误或不准确之处。原始语言的文档应被视为权威来源。对于关键信息，建议使用专业人工翻译。我们不对因使用此翻译而产生的任何误解或误读承担责任。