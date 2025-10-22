<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f0ce2d470f3efad6f8c7df376f416a4b",
  "translation_date": "2025-07-12T07:36:15+00:00",
  "source_file": "00-course-setup/AzureSearch.md",
  "language_code": "br"
}
-->
# Guia de Configuração do Azure AI Search

Este guia vai ajudar você a configurar o Azure AI Search usando o portal do Azure. Siga os passos abaixo para criar e configurar seu serviço Azure AI Search.

## Pré-requisitos

Antes de começar, certifique-se de que você tem o seguinte:

- Uma assinatura do Azure. Se você não tem uma assinatura do Azure, pode criar uma conta gratuita em [Azure Free Account](https://azure.microsoft.com/free/?wt.mc_id=studentamb_258691).

## Passo 1: Criar um Serviço Azure AI Search

1. Faça login no [portal do Azure](https://portal.azure.com/?wt.mc_id=studentamb_258691).
2. No painel de navegação à esquerda, clique em **Criar um recurso**.
3. Na caixa de pesquisa, digite "Azure AI Search" e selecione **Azure AI Search** na lista de resultados.
4. Clique no botão **Criar**.
5. Na aba **Básico**, forneça as seguintes informações:
   - **Assinatura**: Selecione sua assinatura do Azure.
   - **Grupo de recursos**: Crie um novo grupo de recursos ou selecione um existente.
   - **Nome do recurso**: Insira um nome único para seu serviço de busca.
   - **Região**: Selecione a região mais próxima dos seus usuários.
   - **Camada de preço**: Escolha uma camada de preço que atenda às suas necessidades. Você pode começar com a camada Gratuita para testes.
6. Clique em **Revisar + criar**.
7. Revise as configurações e clique em **Criar** para criar o serviço de busca.

## Passo 2: Comece a Usar o Azure AI Search

1. Após a implantação ser concluída, navegue até seu serviço de busca no portal do Azure.
2. Na página de visão geral do serviço de busca, clique no botão **Início rápido**.
3. Siga os passos do guia de Início rápido para criar um índice, enviar dados e realizar uma consulta de busca.

### Criar um Índice

1. No guia de Início rápido, clique em **Criar um índice**.
2. Defina o esquema do índice especificando os campos e seus atributos (por exemplo, tipo de dado, pesquisável, filtrável).
3. Clique em **Criar** para criar o índice.

### Enviar Dados

1. No guia de Início rápido, clique em **Enviar dados**.
2. Escolha uma fonte de dados (por exemplo, Azure Blob Storage, Azure SQL Database) e forneça os detalhes de conexão necessários.
3. Mapeie os campos da fonte de dados para os campos do índice.
4. Clique em **Enviar** para carregar os dados no índice.

### Realizar uma Consulta de Busca

1. No guia de Início rápido, clique em **Explorador de busca**.
2. Digite uma consulta de busca na caixa de pesquisa para testar a funcionalidade de busca.
3. Revise os resultados da busca e ajuste o esquema do índice ou os dados conforme necessário.

## Passo 3: Usar as Ferramentas do Azure AI Search

O Azure AI Search se integra com várias ferramentas para aprimorar suas capacidades de busca. Você pode usar o Azure CLI, SDK para Python e outras ferramentas para configurações e operações avançadas.

### Usando o Azure CLI

1. Instale o Azure CLI seguindo as instruções em [Install Azure CLI](https://learn.microsoft.com/en-us/cli/azure/install-azure-cli?wt.mc_id=studentamb_258691).
2. Faça login no Azure CLI usando o comando:
   ```bash
   az login
   ```
3. Crie um novo serviço de busca usando o Azure CLI:
   ```bash
   az search service create --resource-group <resource-group> --name <service-name> --sku Free
   ```
4. Crie um índice usando o Azure CLI:
   ```bash
   az search index create --service-name <service-name> --name <index-name> --fields "field1:type, field2:type"
   ```

### Usando o SDK para Python

1. Instale a biblioteca cliente do Azure Cognitive Search para Python:
   ```bash
   pip install azure-search-documents
   ```
2. Use o código Python a seguir para criar um índice e enviar documentos:
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

Para informações mais detalhadas, consulte a documentação a seguir:

- [Create an Azure Cognitive Search service](https://learn.microsoft.com/en-us/azure/search/search-create-service-portal?wt.mc_id=studentamb_258691)
- [Get started with Azure Cognitive Search](https://learn.microsoft.com/en-us/azure/search/search-get-started-portal?wt.mc_id=studentamb_258691)
- [Azure AI Search Tools](https://learn.microsoft.com/en-us/azure/ai-services/agents/how-to/tools/azure-ai-search?tabs=azurecli%2Cpython&pivots=code-examples?wt.mc_id=studentamb_258691)

## Conclusão

Você configurou com sucesso o Azure AI Search usando o portal do Azure e as ferramentas integradas. Agora, você pode explorar recursos e funcionalidades mais avançadas do Azure AI Search para aprimorar suas soluções de busca.

Para mais ajuda, visite a [documentação do Azure Cognitive Search](https://learn.microsoft.com/en-us/azure/search/?wt.mc_id=studentamb_258691).

**Aviso Legal**:  
Este documento foi traduzido utilizando o serviço de tradução por IA [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos para garantir a precisão, esteja ciente de que traduções automáticas podem conter erros ou imprecisões. O documento original em seu idioma nativo deve ser considerado a fonte autorizada. Para informações críticas, recomenda-se tradução profissional humana. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas decorrentes do uso desta tradução.