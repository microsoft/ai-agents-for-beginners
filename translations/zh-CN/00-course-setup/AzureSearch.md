# Azure AI 搜索设置指南

本指南将帮助您使用 Azure 门户设置 Azure AI 搜索。请按照以下步骤创建和配置您的 Azure AI 搜索服务。

## 前提条件

在开始之前，请确保您具备以下条件：

- 一个 Azure 订阅。如果您没有 Azure 订阅，可以在 [Azure 免费账户](https://azure.microsoft.com/free/?wt.mc_id=studentamb_258691) 创建一个免费账户。

## 第 1 步：创建 Azure 存储帐户

1. 按照此说明，[创建 Azure 存储帐户](https://learn.microsoft.com/azure/storage/common/storage-account-create?tabs=azure-portal) 来创建新的 Azure 存储帐户。
   <strong>注意</strong>：确保存储帐户类型是标准通用用途 V2。

## 第 2 步：创建 Azure AI 搜索服务

1. 登录到 [Azure 门户](https://portal.azure.com/?wt.mc_id=studentamb_258691)。
2. 在左侧导航窗格中，点击 <strong>创建资源</strong>。
3. 在搜索框中输入 “Azure AI 搜索”，然后从结果列表中选择 **Azure AI 搜索**。
4. 点击 <strong>创建</strong> 按钮。
5. 在 <strong>基础</strong> 选项卡中，填写以下信息：
   - <strong>订阅</strong>：选择您的 Azure 订阅。
   - <strong>资源组</strong>：创建新的资源组或选择已有资源组。
   - <strong>资源名称</strong>：输入搜索服务的唯一名称。
   - <strong>区域</strong>：选择最靠近您的用户的区域。
   - <strong>定价层</strong>：根据您的需求选择定价层。您可以从免费的测试层开始。
6. 点击 **查看 + 创建**。
7. 审核设置后，点击 <strong>创建</strong> 以创建搜索服务。

## 第 3 步：开始使用 Azure AI 搜索

1. 部署完成后，导航到 Azure 门户中的搜索服务。
2. 在搜索服务概览窗格，复制 URL。它应类似于 `https://<service-name>.search.windows.net`。
3. <strong>（推荐）</strong>启用使用 Microsoft Entra ID（RBAC）的无密钥访问，如下面第 4 步所示 — 无需密钥。本指南中的示例创建/更新索引并上传文档，这需要 <strong>搜索服务贡献者</strong> 和 <strong>搜索索引数据贡献者</strong> 角色（或使用基于密钥的身份验证时使用 <strong>主管理员密钥</strong> — 不是查询密钥）。仅当您无法使用 RBAC 时，请打开 **设置 > 密钥** 窗格并复制 <strong>主管理员密钥</strong>。
4. 按照 [快速入门指南](https://learn.microsoft.com/azure/search/search-get-started-portal?pivots=import-data-new) 中的步骤创建索引、上传数据并执行搜索。

## 第 4 步：使用 Azure AI 搜索工具

Azure AI 搜索集成了多种工具以增强您的搜索功能。您可以使用 Azure CLI、Python SDK、.NET SDK 以及其他工具进行高级配置和操作。

### 使用 Azure CLI

1. 按照 [安装 Azure CLI](https://learn.microsoft.com/cli/azure/install-azure-cli?wt.mc_id=studentamb_258691) 中的说明安装 Azure CLI。
2. 使用以下命令登录 Azure CLI：

   ```bash
   az login
   ```
3. **（推荐）启用 Microsoft Entra ID（RBAC）的无密钥访问：**

    ```bash
    az search service update --name <service-name> --resource-group <resource-group> --auth-options aadOrApiKey
    az role assignment create --assignee <your-user-or-principal-id> --role "Search Service Contributor" --scope $(az search service show -g <resource-group> -n <service-name> --query id -o tsv)
    az role assignment create --assignee <your-user-or-principal-id> --role "Search Index Data Contributor" --scope $(az search service show -g <resource-group> -n <service-name> --query id -o tsv)
    # az search service show has no "endpoint" field; build the URL from the service name.
    export AZURE_SEARCH_SERVICE_ENDPOINT="https://<service-name>.search.windows.net"
    ```

    启用 RBAC 后，下面的 Python 和 .NET SDK 示例将使用 `DefaultAzureCredential` 进行身份验证，本地开发期间使用您的 `az login` 会话 — 无需管理员密钥。详见 [使用角色连接 Azure AI 搜索](https://learn.microsoft.com/azure/search/search-security-rbac)。

4. **（没法使用 RBAC 时）基于密钥的身份验证** — 仅当您不能使用 RBAC 时，存储管理员密钥：

#### 将 Azure AI 搜索实例的端点和 API 密钥存储为环境变量。

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

### 使用 Python SDK

1. 安装 Azure 认知搜索客户端库和 Azure 身份库的 Python 版本：

   ```bash
   pip install azure-search-documents azure-identity
   ```

2. 使用以下 Python 代码创建索引并上传文档：

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

### 使用 .NET SDK

1. 运行以下命令创建索引并上传文档：

    ```bash
    dotnet run ./AzureSearch.cs
    ```

    下面的 .NET 示例使用 `DefaultAzureCredential`，本地开发期间可以使用您通过 `az login` 登录的 Azure CLI。

2. 这是 `AzureSearch.cs` 的 .NET 代码示例：

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

有关更详细的信息，请参阅以下文档：

- [创建 Azure 认知搜索服务](https://learn.microsoft.com/azure/search/search-create-service-portal?wt.mc_id=studentamb_258691)
- [开始使用 Azure 认知搜索](https://learn.microsoft.com/azure/search/search-get-started-portal?wt.mc_id=studentamb_258691)
- [Azure AI 搜索工具](https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-ai-search?tabs=azurecli%2Cpython&pivots=code-examples?wt.mc_id=studentamb_258691)

## 总结

您已成功使用 Azure 门户和集成工具设置了 Azure AI 搜索。现在，您可以探索 Azure AI 搜索的更高级功能和能力，以增强您的搜索解决方案。

如需进一步帮助，请访问 [Azure 认知搜索文档](https://learn.microsoft.com/azure/search/?wt.mc_id=studentamb_258691)。

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免责声明**：
本文件由 AI 翻译服务 [Co-op Translator](https://github.com/Azure/co-op-translator) 翻译完成。尽管我们力求准确，但请注意，自动翻译可能包含错误或不准确之处。原始语言版文件应视为权威来源。对于重要信息，建议使用专业人工翻译。我们对因使用本翻译而产生的任何误解或误释不承担责任。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->