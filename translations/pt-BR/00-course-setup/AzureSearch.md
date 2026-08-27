# Guia de Configuração do Azure AI Search

Este guia ajudará você a configurar o Azure AI Search usando o portal do Azure. Siga os passos abaixo para criar e configurar seu serviço Azure AI Search.

## Pré-requisitos

Antes de começar, certifique-se de ter o seguinte:

- Uma assinatura do Azure. Se você não tiver uma assinatura do Azure, pode criar uma conta gratuita em [Azure Free Account](https://azure.microsoft.com/free/?wt.mc_id=studentamb_258691).

## Passo 1: Criar uma Conta de Armazenamento do Azure

1. Siga esta instrução, [Create an Azure storage account](https://learn.microsoft.com/azure/storage/common/storage-account-create?tabs=azure-portal), para criar uma nova Conta de Armazenamento do Azure.
   **NOTA**: Certifique-se de que o tipo da Conta de Armazenamento seja Standard General Purpose V2.

## Passo 2: Criar um Serviço Azure AI Search

1. Faça login no [portal do Azure](https://portal.azure.com/?wt.mc_id=studentamb_258691).
2. No painel de navegação à esquerda, clique em **Create a resource**.
3. Na caixa de pesquisa, digite "Azure AI Search" e selecione **Azure AI Search** na lista de resultados.
4. Clique no botão **Create**.
5. Na aba **Basics**, forneça as seguintes informações:
   - **Subscription**: Selecione sua assinatura do Azure.
   - **Resource group**: Crie um novo grupo de recursos ou selecione um existente.
   - **Resource name**: Insira um nome único para seu serviço de busca.
   - **Region**: Selecione a região mais próxima dos seus usuários.
   - **Pricing tier**: Escolha um nível de preços que atenda às suas necessidades. Você pode começar com o nível Gratuito para testes.
6. Clique em **Review + create**.
7. Revise as configurações e clique em **Create** para criar o serviço de busca.

## Passo 3: Comece a usar o Azure AI Search

1. Após a implantação ser concluída, navegue até seu serviço de busca no portal do Azure.
2. No painel de visão geral do serviço de busca, copie o URL. Ele deve ser parecido com `https://<service-name>.search.windows.net`.
3. **(Recomendado)** Ative o acesso sem chave com Microsoft Entra ID (RBAC) conforme mostrado no Passo 4 abaixo — nenhuma chave necessária. Os exemplos neste guia criam/atualizam índices e enviam documentos, o que requer os papéis **Search Service Contributor** e **Search Index Data Contributor** (ou, para autenticação baseada em chave, a **chave de administrador primária** — não a chave de consulta). Caso não seja possível usar RBAC, abra o painel **Settings > Keys** e copie a **chave de administrador primária**.
4. Siga os passos da página [Quickstart guide](https://learn.microsoft.com/azure/search/search-get-started-portal?pivots=import-data-new) para criar um índice, enviar dados e realizar uma busca.

## Passo 4: Usar as Ferramentas do Azure AI Search

O Azure AI Search integra-se com várias ferramentas para aprimorar suas capacidades de busca. Você pode usar Azure CLI, SDK Python, SDK .NET e outras ferramentas para configurações e operações avançadas.

### Usando Azure CLI

1. Instale o Azure CLI seguindo as instruções em [Install Azure CLI](https://learn.microsoft.com/cli/azure/install-azure-cli?wt.mc_id=studentamb_258691).
2. Faça login no Azure CLI usando o comando:

   ```bash
   az login
   ```
3. **(Recomendado) Ative o acesso sem chave com Microsoft Entra ID (RBAC):**

    ```bash
    az search service update --name <service-name> --resource-group <resource-group> --auth-options aadOrApiKey
    az role assignment create --assignee <your-user-or-principal-id> --role "Search Service Contributor" --scope $(az search service show -g <resource-group> -n <service-name> --query id -o tsv)
    az role assignment create --assignee <your-user-or-principal-id> --role "Search Index Data Contributor" --scope $(az search service show -g <resource-group> -n <service-name> --query id -o tsv)
    # o comando az search service show não tem campo "endpoint"; construa a URL a partir do nome do serviço.
    export AZURE_SEARCH_SERVICE_ENDPOINT="https://<service-name>.search.windows.net"
    ```

    Com o RBAC ativado, os exemplos do SDK Python e .NET abaixo autenticam com `DefaultAzureCredential`, que usa sua sessão de `az login` durante o desenvolvimento local — não é necessária a chave de administrador. Veja [Conectar-se ao Azure AI Search usando funções](https://learn.microsoft.com/azure/search/search-security-rbac).

4. **(Alternativa) Autenticação baseada em chave** — somente se não for possível usar RBAC, armazene também a chave de administrador:

#### Armazene tanto o endpoint quanto a chave de API da instância Azure AI Search em variáveis de ambiente.

    ```bash
    # zsh/bash
    # az search service show não tem campo "endpoint"; construa o URL a partir do nome do serviço.
    export AZURE_SEARCH_SERVICE_ENDPOINT="https://<service-name>.search.windows.net"
    export AZURE_SEARCH_API_KEY=$(az search admin-key show -g <resource-group> --service-name <service-name> --query "primaryKey" -o tsv)
    ```

    ```powershell
    # PowerShell
    # az search service show não tem campo "endpoint"; construa o URL a partir do nome do serviço.
    $env:AZURE_SEARCH_SERVICE_ENDPOINT = "https://<service-name>.search.windows.net"
    $env:AZURE_SEARCH_API_KEY = $(az search admin-key show -g <resource-group> --service-name <service-name> --query "primaryKey" -o tsv)
    ```

### Usando SDK Python

1. Instale a biblioteca cliente Azure Cognitive Search e Azure Identity para Python:

   ```bash
   pip install azure-search-documents azure-identity
   ```

2. Use o seguinte código Python para criar um índice e enviar documentos:

    ```python
    import os
    from azure.identity import DefaultAzureCredential
    from azure.search.documents import SearchClient
    from azure.search.documents.indexes import SearchIndexClient
    from azure.search.documents.indexes.models import SearchIndex, SimpleField, edm

    service_endpoint = os.getenv("AZURE_SEARCH_SERVICE_ENDPOINT")
    index_name = "sample-index"

    # Sem chave (recomendado): usa sua identidade `az login` via RBAC do Entra ID.
    # Requer as funções "Colaborador do Serviço de Pesquisa" e "Colaborador de Dados do Índice de Pesquisa".
    credential = DefaultAzureCredential()
    # Alternativa (autenticação baseada em chave):
    # de azure.core.credentials import AzureKeyCredential
    # credencial = AzureKeyCredential(os.getenv("AZURE_SEARCH_API_KEY"))
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

### Usando SDK .NET

1. Execute o seguinte comando para criar um índice e enviar documentos:

    ```bash
    dotnet run ./AzureSearch.cs
    ```

    O exemplo .NET abaixo usa `DefaultAzureCredential`, que pode usar seu login do Azure CLI de `az login` durante o desenvolvimento local.

2. Aqui está o código .NET de `AzureSearch.cs`:

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

Para informações mais detalhadas, consulte a documentação a seguir:

- [Criar um serviço Azure Cognitive Search](https://learn.microsoft.com/azure/search/search-create-service-portal?wt.mc_id=studentamb_258691)
- [Comece a usar o Azure Cognitive Search](https://learn.microsoft.com/azure/search/search-get-started-portal?wt.mc_id=studentamb_258691)
- [Ferramentas do Azure AI Search](https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-ai-search?tabs=azurecli%2Cpython&pivots=code-examples?wt.mc_id=studentamb_258691)

## Conclusão

Você configurou com sucesso o Azure AI Search usando o portal do Azure e ferramentas integradas. Agora você pode explorar recursos e capacidades mais avançadas do Azure AI Search para aprimorar suas soluções de busca.

Para mais ajuda, visite a [documentação do Azure Cognitive Search](https://learn.microsoft.com/azure/search/?wt.mc_id=studentamb_258691).

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Aviso Legal**:
Este documento foi traduzido usando o serviço de tradução por IA [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos pela precisão, por favor, esteja ciente de que traduções automatizadas podem conter erros ou imprecisões. O documento original em seu idioma nativo deve ser considerado a fonte autorizada. Para informações críticas, recomenda-se tradução profissional humana. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas decorrentes do uso desta tradução.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->