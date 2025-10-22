<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f0ce2d470f3efad6f8c7df376f416a4b",
  "translation_date": "2025-07-12T07:36:05+00:00",
  "source_file": "00-course-setup/AzureSearch.md",
  "language_code": "pt"
}
-->
# Guia de Configuração do Azure AI Search

Este guia irá ajudá-lo a configurar o Azure AI Search através do portal Azure. Siga os passos abaixo para criar e configurar o seu serviço Azure AI Search.

## Pré-requisitos

Antes de começar, certifique-se de que tem o seguinte:

- Uma subscrição Azure. Se não tiver uma subscrição Azure, pode criar uma conta gratuita em [Azure Free Account](https://azure.microsoft.com/free/?wt.mc_id=studentamb_258691).

## Passo 1: Criar um Serviço Azure AI Search

1. Inicie sessão no [portal Azure](https://portal.azure.com/?wt.mc_id=studentamb_258691).
2. No painel de navegação à esquerda, clique em **Criar um recurso**.
3. Na caixa de pesquisa, escreva "Azure AI Search" e selecione **Azure AI Search** na lista de resultados.
4. Clique no botão **Criar**.
5. No separador **Básicos**, forneça as seguintes informações:
   - **Subscrição**: Selecione a sua subscrição Azure.
   - **Grupo de recursos**: Crie um novo grupo de recursos ou selecione um existente.
   - **Nome do recurso**: Introduza um nome único para o seu serviço de pesquisa.
   - **Região**: Selecione a região mais próxima dos seus utilizadores.
   - **Nível de preços**: Escolha um nível de preços que se adeque às suas necessidades. Pode começar com o nível Gratuito para testes.
6. Clique em **Analisar + criar**.
7. Reveja as definições e clique em **Criar** para criar o serviço de pesquisa.

## Passo 2: Começar a Usar o Azure AI Search

1. Assim que a implementação estiver concluída, navegue até ao seu serviço de pesquisa no portal Azure.
2. Na página de visão geral do serviço de pesquisa, clique no botão **Início rápido**.
3. Siga os passos no guia de Início rápido para criar um índice, carregar dados e realizar uma consulta de pesquisa.

### Criar um Índice

1. No guia de Início rápido, clique em **Criar um índice**.
2. Defina o esquema do índice especificando os campos e os seus atributos (por exemplo, tipo de dados, pesquisável, filtrável).
3. Clique em **Criar** para criar o índice.

### Carregar Dados

1. No guia de Início rápido, clique em **Carregar dados**.
2. Escolha uma fonte de dados (por exemplo, Azure Blob Storage, Azure SQL Database) e forneça os detalhes de ligação necessários.
3. Faça o mapeamento dos campos da fonte de dados para os campos do índice.
4. Clique em **Submeter** para carregar os dados para o índice.

### Realizar uma Consulta de Pesquisa

1. No guia de Início rápido, clique em **Explorador de pesquisa**.
2. Introduza uma consulta de pesquisa na caixa de pesquisa para testar a funcionalidade de pesquisa.
3. Reveja os resultados da pesquisa e ajuste o esquema do índice ou os dados conforme necessário.

## Passo 3: Utilizar as Ferramentas Azure AI Search

O Azure AI Search integra-se com várias ferramentas para melhorar as suas capacidades de pesquisa. Pode usar o Azure CLI, o SDK Python e outras ferramentas para configurações e operações avançadas.

### Utilizar o Azure CLI

1. Instale o Azure CLI seguindo as instruções em [Install Azure CLI](https://learn.microsoft.com/en-us/cli/azure/install-azure-cli?wt.mc_id=studentamb_258691).
2. Inicie sessão no Azure CLI usando o comando:
   ```bash
   az login
   ```
3. Crie um novo serviço de pesquisa usando o Azure CLI:
   ```bash
   az search service create --resource-group <resource-group> --name <service-name> --sku Free
   ```
4. Crie um índice usando o Azure CLI:
   ```bash
   az search index create --service-name <service-name> --name <index-name> --fields "field1:type, field2:type"
   ```

### Utilizar o SDK Python

1. Instale a biblioteca cliente Azure Cognitive Search para Python:
   ```bash
   pip install azure-search-documents
   ```
2. Utilize o seguinte código Python para criar um índice e carregar documentos:
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

Para informações mais detalhadas, consulte a documentação seguinte:

- [Create an Azure Cognitive Search service](https://learn.microsoft.com/en-us/azure/search/search-create-service-portal?wt.mc_id=studentamb_258691)
- [Get started with Azure Cognitive Search](https://learn.microsoft.com/en-us/azure/search/search-get-started-portal?wt.mc_id=studentamb_258691)
- [Azure AI Search Tools](https://learn.microsoft.com/en-us/azure/ai-services/agents/how-to/tools/azure-ai-search?tabs=azurecli%2Cpython&pivots=code-examples?wt.mc_id=studentamb_258691)

## Conclusão

Configurou com sucesso o Azure AI Search através do portal Azure e das ferramentas integradas. Agora pode explorar funcionalidades e capacidades mais avançadas do Azure AI Search para melhorar as suas soluções de pesquisa.

Para mais ajuda, visite a [documentação do Azure Cognitive Search](https://learn.microsoft.com/en-us/azure/search/?wt.mc_id=studentamb_258691).

**Aviso Legal**:  
Este documento foi traduzido utilizando o serviço de tradução automática [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos por garantir a precisão, por favor tenha em conta que traduções automáticas podem conter erros ou imprecisões. O documento original na sua língua nativa deve ser considerado a fonte autorizada. Para informações críticas, recomenda-se tradução profissional humana. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas decorrentes da utilização desta tradução.