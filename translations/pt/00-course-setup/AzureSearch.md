<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "11e38db0898a788612b917e329dcdb5b",
  "translation_date": "2025-11-07T08:34:20+00:00",
  "source_file": "00-course-setup/AzureSearch.md",
  "language_code": "pt"
}
-->
# Guia de Configuração do Azure AI Search

Este guia irá ajudá-lo a configurar o Azure AI Search utilizando o portal do Azure. Siga os passos abaixo para criar e configurar o seu serviço Azure AI Search.

## Pré-requisitos

Antes de começar, certifique-se de que possui o seguinte:

- Uma subscrição do Azure. Se não tiver uma subscrição do Azure, pode criar uma conta gratuita em [Conta Gratuita do Azure](https://azure.microsoft.com/free/?wt.mc_id=studentamb_258691).

## Passo 1: Criar uma Conta de Armazenamento do Azure

1. Siga estas instruções, [Criar uma conta de armazenamento do Azure](https://learn.microsoft.com/azure/storage/common/storage-account-create?tabs=azure-portal), para criar uma nova conta de armazenamento do Azure.
   **NOTA**: Certifique-se de que o tipo de conta de armazenamento é Standard General Purpose V2.

## Passo 2: Criar um Serviço Azure AI Search

1. Inicie sessão no [portal do Azure](https://portal.azure.com/?wt.mc_id=studentamb_258691).
2. No painel de navegação à esquerda, clique em **Criar um recurso**.
3. Na caixa de pesquisa, digite "Azure AI Search" e selecione **Azure AI Search** na lista de resultados.
4. Clique no botão **Criar**.
5. No separador **Informações básicas**, forneça as seguintes informações:
   - **Subscrição**: Selecione a sua subscrição do Azure.
   - **Grupo de recursos**: Crie um novo grupo de recursos ou selecione um existente.
   - **Nome do recurso**: Insira um nome único para o seu serviço de pesquisa.
   - **Região**: Selecione a região mais próxima dos seus utilizadores.
   - **Camada de preços**: Escolha uma camada de preços que atenda às suas necessidades. Pode começar com a camada gratuita para testes.
6. Clique em **Revisar + criar**.
7. Revise as configurações e clique em **Criar** para criar o serviço de pesquisa.

## Passo 3: Começar com o Azure AI Search

1. Assim que a implementação estiver concluída, navegue até ao seu serviço de pesquisa no portal do Azure.
2. No painel de visão geral do serviço de pesquisa, copie o URL. Deve ter o formato `https://<service-name>.search.windows.net`.
3. No painel Configurações > Chaves, copie a chave de consulta.
4. Siga os passos na página [Guia de introdução](https://learn.microsoft.com/azure/search/search-get-started-portal?pivots=import-data-new) para criar um índice, carregar dados e realizar uma consulta de pesquisa.

## Passo 4: Utilizar Ferramentas do Azure AI Search

O Azure AI Search integra-se com várias ferramentas para melhorar as suas capacidades de pesquisa. Pode utilizar Azure CLI, Python SDK, .NET SDK e outras ferramentas para configurações e operações avançadas.

### Utilizar Azure CLI

1. Instale o Azure CLI seguindo as instruções em [Instalar Azure CLI](https://learn.microsoft.com/cli/azure/install-azure-cli?wt.mc_id=studentamb_258691).
2. Inicie sessão no Azure CLI utilizando o comando:

   ```bash
   az login
   ```

3. Armazene o endpoint e a chave API da instância do Azure AI Search em variáveis de ambiente.

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

### Utilizar Python SDK

1. Instale a biblioteca cliente do Azure Cognitive Search para Python:

   ```bash
   pip install azure-search-documents
   ```

2. Utilize o seguinte código Python para criar um índice e carregar documentos:

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

### Utilizar .NET SDK

1. Execute o seguinte comando para criar um índice e carregar documentos:

    ```bash
    dotnet run ./AzureSearch.cs
    ```

2. Aqui está o código .NET de `AzureSearch.cs`:

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

Para mais informações detalhadas, consulte a seguinte documentação:

- [Criar um serviço Azure Cognitive Search](https://learn.microsoft.com/azure/search/search-create-service-portal?wt.mc_id=studentamb_258691)
- [Introdução ao Azure Cognitive Search](https://learn.microsoft.com/azure/search/search-get-started-portal?wt.mc_id=studentamb_258691)
- [Ferramentas do Azure AI Search](https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-ai-search?tabs=azurecli%2Cpython&pivots=code-examples?wt.mc_id=studentamb_258691)

## Conclusão

Você configurou com sucesso o Azure AI Search utilizando o portal do Azure e ferramentas integradas. Agora pode explorar funcionalidades e capacidades mais avançadas do Azure AI Search para melhorar as suas soluções de pesquisa.

Para mais assistência, visite a [documentação do Azure Cognitive Search](https://learn.microsoft.com/azure/search/?wt.mc_id=studentamb_258691).

---

**Aviso Legal**:  
Este documento foi traduzido utilizando o serviço de tradução por IA [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos pela precisão, esteja ciente de que traduções automáticas podem conter erros ou imprecisões. O documento original na sua língua nativa deve ser considerado a fonte autoritária. Para informações críticas, recomenda-se uma tradução profissional humana. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas decorrentes do uso desta tradução.