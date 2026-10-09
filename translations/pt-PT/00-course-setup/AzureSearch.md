# Guia de Configuração do Azure AI Search

Este guia irá ajudá-lo a configurar o Azure AI Search utilizando o portal Azure. Siga os passos abaixo para criar e configurar o seu serviço Azure AI Search.

## Pré-requisitos

Antes de começar, certifique-se de que tem o seguinte:

- Uma subscrição Azure. Se não tiver uma subscrição Azure, pode criar uma conta gratuita em [Azure Free Account](https://azure.microsoft.com/free/?wt.mc_id=studentamb_258691).

## Passo 1: Criar uma Conta de Armazenamento Azure

1. Siga esta instrução, [Create an Azure storage account](https://learn.microsoft.com/azure/storage/common/storage-account-create?tabs=azure-portal), para criar uma nova Conta de Armazenamento Azure.
   **NOTA**: Certifique-se de que o tipo de Conta de Armazenamento é Standard General Purpose V2.

## Passo 2: Criar um Serviço Azure AI Search

1. Inicie sessão no [portal Azure](https://portal.azure.com/?wt.mc_id=studentamb_258691).
2. No painel de navegação à esquerda, clique em **Create a resource**.
3. Na caixa de pesquisa, escreva "Azure AI Search" e selecione **Azure AI Search** da lista de resultados.
4. Clique no botão **Create**.
5. No separador **Basics**, forneça as seguintes informações:
   - **Subscription**: Selecione a sua subscrição Azure.
   - **Resource group**: Crie um novo grupo de recursos ou selecione um existente.
   - **Resource name**: Introduza um nome único para o seu serviço de pesquisa.
   - **Region**: Selecione a região mais próxima dos seus utilizadores.
   - **Pricing tier**: Escolha um nível de preços adequado às suas necessidades. Pode começar pelo nível Gratuito para testes.
6. Clique em **Review + create**.
7. Reveja as configurações e clique em **Create** para criar o serviço de pesquisa.

## Passo 3: Começar com Azure AI Search

1. Após a conclusão da implementação, navegue até ao seu serviço de pesquisa no portal Azure.
2. No painel de resumo do serviço de pesquisa, copie a URL. Esta deve ser semelhante a `https://<service-name>.search.windows.net`.
3. **(Recomendado)** Ative o acesso sem chave com o Microsoft Entra ID (RBAC) conforme mostrado no Passo 4 abaixo — não é necessária chave. Os exemplos neste guia criam/atualizam índices e carregam documentos, o que requer os papéis **Search Service Contributor** e **Search Index Data Contributor** (ou, para autenticação baseada em chave, a **primary admin key** — não a chave de consulta). Apenas se não puder usar RBAC, abra o painel **Settings > Keys** e copie a **primary admin key**.
4. Siga os passos na página do [Guia rápido](https://learn.microsoft.com/azure/search/search-get-started-portal?pivots=import-data-new) para criar um índice, carregar dados e realizar uma pesquisa.

## Passo 4: Utilizar as Ferramentas do Azure AI Search

O Azure AI Search integra-se com várias ferramentas para melhorar as suas funcionalidades de pesquisa. Pode usar Azure CLI, Python SDK, .NET SDK e outras ferramentas para configurações e operações avançadas.

### Usar Azure CLI

1. Instale o Azure CLI seguindo as instruções em [Install Azure CLI](https://learn.microsoft.com/cli/azure/install-azure-cli?wt.mc_id=studentamb_258691).
2. Inicie sessão no Azure CLI utilizando o comando:

   ```bash
   az login
   ```
3. **(Recomendado) Ative o acesso sem chave com o Microsoft Entra ID (RBAC):**

    ```bash
    az search service update --name <service-name> --resource-group <resource-group> --auth-options aadOrApiKey
    az role assignment create --assignee <your-user-or-principal-id> --role "Search Service Contributor" --scope $(az search service show -g <resource-group> -n <service-name> --query id -o tsv)
    az role assignment create --assignee <your-user-or-principal-id> --role "Search Index Data Contributor" --scope $(az search service show -g <resource-group> -n <service-name> --query id -o tsv)
    # o comando az search service show não tem o campo "endpoint"; construa a URL a partir do nome do serviço.
    export AZURE_SEARCH_SERVICE_ENDPOINT="https://<service-name>.search.windows.net"
    ```

    Com o RBAC ativado, os exemplos do Python e .NET SDK abaixo autenticam com `DefaultAzureCredential`, que usa a sua sessão `az login` durante o desenvolvimento local — não é necessária chave administrativa. Consulte [Connect to Azure AI Search using roles](https://learn.microsoft.com/azure/search/search-security-rbac).

4. **(Solução alternativa) Autenticação baseada em chave** — apenas se não puder usar RBAC, guarde também a chave administrativa:

#### Guarde tanto o endpoint como a chave API da instância Azure AI Search em variáveis de ambiente.

    ```bash
    # zsh/bash
    # az search service show não tem campo "endpoint"; construa a URL a partir do nome do serviço.
    export AZURE_SEARCH_SERVICE_ENDPOINT="https://<service-name>.search.windows.net"
    export AZURE_SEARCH_API_KEY=$(az search admin-key show -g <resource-group> --service-name <service-name> --query "primaryKey" -o tsv)
    ```

    ```powershell
    # PowerShell
    # az search service show não tem campo "endpoint"; construa a URL a partir do nome do serviço.
    $env:AZURE_SEARCH_SERVICE_ENDPOINT = "https://<service-name>.search.windows.net"
    $env:AZURE_SEARCH_API_KEY = $(az search admin-key show -g <resource-group> --service-name <service-name> --query "primaryKey" -o tsv)
    ```

### Usar Python SDK

1. Instale a biblioteca cliente do Azure Cognitive Search e Azure Identity para Python:

   ```bash
   pip install azure-search-documents azure-identity
   ```

2. Use o seguinte código em Python para criar um índice e carregar documentos:

    ```python
    import os
    from azure.identity import DefaultAzureCredential
    from azure.search.documents import SearchClient
    from azure.search.documents.indexes import SearchIndexClient
    from azure.search.documents.indexes.models import SearchIndex, SimpleField, edm

    service_endpoint = os.getenv("AZURE_SEARCH_SERVICE_ENDPOINT")
    index_name = "sample-index"

    # Sem chave (recomendado): usa a sua identidade `az login` através do RBAC do Entra ID.
    # Requer as funções "Colaborador de Serviço de Pesquisa" e "Colaborador de Dados de Índice de Pesquisa".
    credential = DefaultAzureCredential()
    # Alternativa (autenticação baseada em chave):
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

### Usar .NET SDK

1. Execute o seguinte comando para criar um índice e carregar documentos:

    ```bash
    dotnet run ./AzureSearch.cs
    ```

    O exemplo .NET abaixo usa `DefaultAzureCredential`, que pode usar a sua sessão de login do Azure CLI `az login` durante o desenvolvimento local.

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

Para obter informações mais detalhadas, consulte a documentação seguinte:

- [Criar um serviço Azure Cognitive Search](https://learn.microsoft.com/azure/search/search-create-service-portal?wt.mc_id=studentamb_258691)
- [Começar com Azure Cognitive Search](https://learn.microsoft.com/azure/search/search-get-started-portal?wt.mc_id=studentamb_258691)
- [Ferramentas do Azure AI Search](https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-ai-search?tabs=azurecli%2Cpython&pivots=code-examples?wt.mc_id=studentamb_258691)

## Conclusão

Configurou com sucesso o Azure AI Search usando o portal Azure e as ferramentas integradas. Agora pode explorar funcionalidades e capacidades mais avançadas do Azure AI Search para melhorar as suas soluções de pesquisa.

Para obter ajuda adicional, visite a [documentação do Azure Cognitive Search](https://learn.microsoft.com/azure/search/?wt.mc_id=studentamb_258691).

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Aviso Legal**:
Este documento foi traduzido utilizando o serviço de tradução automática [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos pela precisão, esteja ciente de que traduções automáticas podem conter erros ou imprecisões. O documento original na sua língua nativa deve ser considerado a fonte autorizada. Para informações críticas, recomenda-se tradução profissional humana. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas resultantes da utilização desta tradução.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->