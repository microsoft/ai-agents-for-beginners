# Guia de Configuração do Azure AI Search

Este guia irá ajudá-lo a configurar o Azure AI Search utilizando o portal Azure. Siga os passos abaixo para criar e configurar o seu serviço Azure AI Search.

## Pré-requisitos

Antes de começar, certifique-se de que possui o seguinte:

- Uma subscrição Azure. Se não possuir uma subscrição Azure, pode criar uma conta gratuita em [Azure Free Account](https://azure.microsoft.com/free/?wt.mc_id=studentamb_258691).

## Passo 1: Criar uma Conta de Armazenamento Azure

1. Siga esta instrução, [Create an Azure storage account](https://learn.microsoft.com/azure/storage/common/storage-account-create?tabs=azure-portal), para criar uma nova Conta de Armazenamento Azure.
   **NOTA**: Certifique-se de que o tipo de Conta de Armazenamento é Standard General Purpose V2.

## Passo 2: Criar um Serviço Azure AI Search

1. Inicie sessão no [portal Azure](https://portal.azure.com/?wt.mc_id=studentamb_258691).
2. No painel de navegação à esquerda, clique em **Criar um recurso**.
3. Na caixa de pesquisa, digite "Azure AI Search" e selecione **Azure AI Search** na lista de resultados.
4. Clique no botão **Criar**.
5. No separador **Básicos**, forneça as seguintes informações:
   - **Subscrição**: Selecione a sua subscrição Azure.
   - **Grupo de recursos**: Crie um novo grupo de recursos ou selecione um existente.
   - **Nome do recurso**: Insira um nome único para o seu serviço de pesquisa.
   - **Região**: Selecione a região mais próxima dos seus utilizadores.
   - **Nível de preços**: Escolha um nível de preços que se adeque às suas necessidades. Pode começar com o nível Gratuito para testes.
6. Clique em **Analisar + criar**.
7. Reveja as definições e clique em **Criar** para criar o serviço de pesquisa.

## Passo 3: Começar a usar o Azure AI Search

1. Uma vez que o deployment esteja concluído, navegue para o seu serviço de pesquisa no portal Azure.
2. No painel de visão geral do serviço de pesquisa, copie o URL. Deve ter o formato `https://<service-name>.search.windows.net`.
3. **(Recomendado)** Ative o acesso sem chave com Microsoft Entra ID (RBAC) conforme mostrado no Passo 4 abaixo — não é necessária chave. Os exemplos neste guia criam/atualizam índices e carregam documentos, o que requer os papéis **Search Service Contributor** e **Search Index Data Contributor** (ou, para autenticação baseada em chave, a **chave administrativa principal** — não a chave de consulta). Só se não puder usar RBAC, abra o painel **Definições > Chaves** e copie a **chave administrativa principal**.
4. Siga os passos na página do [Guia de primeiros passos](https://learn.microsoft.com/azure/search/search-get-started-portal?pivots=import-data-new) para criar um índice, carregar dados e realizar uma pesquisa.

## Passo 4: Utilizar Ferramentas Azure AI Search

O Azure AI Search integra-se com várias ferramentas para melhorar as suas capacidades de pesquisa. Pode usar o Azure CLI, Python SDK, .NET SDK e outras ferramentas para configurações e operações avançadas.

### Usar o Azure CLI

1. Instale o Azure CLI seguindo as instruções em [Install Azure CLI](https://learn.microsoft.com/cli/azure/install-azure-cli?wt.mc_id=studentamb_258691).
2. Inicie sessão no Azure CLI usando o comando:

   ```bash
   az login
   ```
3. **(Recomendado) Ative o acesso sem chave com Microsoft Entra ID (RBAC):**

    ```bash
    az search service update --name <service-name> --resource-group <resource-group> --auth-options aadOrApiKey
    az role assignment create --assignee <your-user-or-principal-id> --role "Search Service Contributor" --scope $(az search service show -g <resource-group> -n <service-name> --query id -o tsv)
    az role assignment create --assignee <your-user-or-principal-id> --role "Search Index Data Contributor" --scope $(az search service show -g <resource-group> -n <service-name> --query id -o tsv)
    # az search service show não tem um campo "endpoint"; construa o URL a partir do nome do serviço.
    export AZURE_SEARCH_SERVICE_ENDPOINT="https://<service-name>.search.windows.net"
    ```

    Com o RBAC ativado, os exemplos em Python e .NET SDK abaixo autenticar-se-ão com `DefaultAzureCredential`, que utiliza a sua sessão `az login` durante o desenvolvimento local — não é necessária chave administrativa. Veja [Connect to Azure AI Search using roles](https://learn.microsoft.com/azure/search/search-security-rbac).

4. **(Alternativa) Autenticação baseada em chave** — apenas se não puder usar RBAC, armazene também a chave administrativa:

#### Armazene tanto o endpoint como a chave API da instância Azure AI Search em variáveis de ambiente.

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

### Usar o Python SDK

1. Instale a biblioteca cliente Azure Cognitive Search e o Azure Identity para Python:

   ```bash
   pip install azure-search-documents azure-identity
   ```

2. Utilize o seguinte código Python para criar um índice e carregar documentos:

    ```python
    import os
    from azure.identity import DefaultAzureCredential
    from azure.search.documents import SearchClient
    from azure.search.documents.indexes import SearchIndexClient
    from azure.search.documents.indexes.models import SearchIndex, SimpleField, edm

    service_endpoint = os.getenv("AZURE_SEARCH_SERVICE_ENDPOINT")
    index_name = "sample-index"

    # Sem chave (recomendado): utiliza a sua identidade `az login` via RBAC do Entra ID.
    # Requer os papéis "Colaborador do Serviço de Pesquisa" e "Colaborador de Dados do Índice de Pesquisa".
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

### Usar o .NET SDK

1. Execute o seguinte comando para criar um índice e carregar documentos:

    ```bash
    dotnet run ./AzureSearch.cs
    ```

    O exemplo .NET abaixo usa `DefaultAzureCredential`, que pode utilizar o seu início de sessão Azure CLI com `az login` durante o desenvolvimento local.

2. Aqui está o código .NET do `AzureSearch.cs`:

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

Para informações mais detalhadas, consulte a documentação seguinte:

- [Create an Azure Cognitive Search service](https://learn.microsoft.com/azure/search/search-create-service-portal?wt.mc_id=studentamb_258691)
- [Get started with Azure Cognitive Search](https://learn.microsoft.com/azure/search/search-get-started-portal?wt.mc_id=studentamb_258691)
- [Azure AI Search Tools](https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-ai-search?tabs=azurecli%2Cpython&pivots=code-examples?wt.mc_id=studentamb_258691)

## Conclusão

Configurou com sucesso o Azure AI Search utilizando o portal Azure e as ferramentas integradas. Agora pode explorar funcionalidades e capacidades mais avançadas do Azure AI Search para melhorar as suas soluções de pesquisa.

Para assistência adicional, visite a [documentação do Azure Cognitive Search](https://learn.microsoft.com/azure/search/?wt.mc_id=studentamb_258691).

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Aviso Legal**:
Este documento foi traduzido utilizando o serviço de tradução automática [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos pela precisão, esteja ciente de que traduções automáticas podem conter erros ou imprecisões. O documento original na sua língua nativa deve ser considerado a fonte autorizada. Para informações críticas, recomenda-se tradução profissional humana. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas resultantes da utilização desta tradução.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->