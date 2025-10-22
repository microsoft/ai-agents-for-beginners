<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f0ce2d470f3efad6f8c7df376f416a4b",
  "translation_date": "2025-07-12T07:35:51+00:00",
  "source_file": "00-course-setup/AzureSearch.md",
  "language_code": "pa"
}
-->
# Azure AI Search ਸੈਟਅਪ ਗਾਈਡ

ਇਹ ਗਾਈਡ ਤੁਹਾਨੂੰ Azure ਪੋਰਟਲ ਦੀ ਵਰਤੋਂ ਕਰਕੇ Azure AI Search ਸੈਟਅਪ ਕਰਨ ਵਿੱਚ ਮਦਦ ਕਰੇਗੀ। ਆਪਣੀ Azure AI Search ਸੇਵਾ ਬਣਾਉਣ ਅਤੇ ਸੰਰਚਿਤ ਕਰਨ ਲਈ ਹੇਠਾਂ ਦਿੱਤੇ ਕਦਮਾਂ ਦੀ ਪਾਲਣਾ ਕਰੋ।

## ਜ਼ਰੂਰੀ ਸ਼ਰਤਾਂ

ਸ਼ੁਰੂ ਕਰਨ ਤੋਂ ਪਹਿਲਾਂ, ਇਹ ਯਕੀਨੀ ਬਣਾਓ ਕਿ ਤੁਹਾਡੇ ਕੋਲ ਹੇਠਾਂ ਦਿੱਤੀਆਂ ਚੀਜ਼ਾਂ ਹਨ:

- ਇੱਕ Azure ਸਬਸਕ੍ਰਿਪਸ਼ਨ। ਜੇ ਤੁਹਾਡੇ ਕੋਲ Azure ਸਬਸਕ੍ਰਿਪਸ਼ਨ ਨਹੀਂ ਹੈ, ਤਾਂ ਤੁਸੀਂ [Azure Free Account](https://azure.microsoft.com/free/?wt.mc_id=studentamb_258691) 'ਤੇ ਮੁਫ਼ਤ ਖਾਤਾ ਬਣਾਉ ਸਕਦੇ ਹੋ।

## ਕਦਮ 1: Azure AI Search ਸੇਵਾ ਬਣਾਓ

1. [Azure portal](https://portal.azure.com/?wt.mc_id=studentamb_258691) ਵਿੱਚ ਸਾਈਨ ਇਨ ਕਰੋ।
2. ਖੱਬੇ ਪਾਸੇ ਨੈਵੀਗੇਸ਼ਨ ਪੈਨ ਵਿੱਚ, **Create a resource** 'ਤੇ ਕਲਿੱਕ ਕਰੋ।
3. ਖੋਜ ਬਾਕਸ ਵਿੱਚ "Azure AI Search" ਲਿਖੋ ਅਤੇ ਨਤੀਜਿਆਂ ਵਿੱਚੋਂ **Azure AI Search** ਚੁਣੋ।
4. **Create** ਬਟਨ 'ਤੇ ਕਲਿੱਕ ਕਰੋ।
5. **Basics** ਟੈਬ ਵਿੱਚ ਹੇਠਾਂ ਦਿੱਤੀ ਜਾਣਕਾਰੀ ਭਰੋ:
   - **Subscription**: ਆਪਣੀ Azure ਸਬਸਕ੍ਰਿਪਸ਼ਨ ਚੁਣੋ।
   - **Resource group**: ਨਵਾਂ resource group ਬਣਾਓ ਜਾਂ ਮੌਜੂਦਾ ਚੁਣੋ।
   - **Resource name**: ਆਪਣੀ search service ਲਈ ਇੱਕ ਵਿਲੱਖਣ ਨਾਮ ਦਿਓ।
   - **Region**: ਆਪਣੇ ਯੂਜ਼ਰਾਂ ਦੇ ਸਭ ਤੋਂ ਨੇੜਲੇ ਖੇਤਰ ਨੂੰ ਚੁਣੋ।
   - **Pricing tier**: ਆਪਣੀਆਂ ਲੋੜਾਂ ਮੁਤਾਬਕ ਇੱਕ ਪ੍ਰਾਈਸਿੰਗ ਟੀਅਰ ਚੁਣੋ। ਟੈਸਟਿੰਗ ਲਈ ਤੁਸੀਂ Free ਟੀਅਰ ਨਾਲ ਸ਼ੁਰੂ ਕਰ ਸਕਦੇ ਹੋ।
6. **Review + create** 'ਤੇ ਕਲਿੱਕ ਕਰੋ।
7. ਸੈਟਿੰਗਜ਼ ਦੀ ਸਮੀਖਿਆ ਕਰੋ ਅਤੇ search service ਬਣਾਉਣ ਲਈ **Create** 'ਤੇ ਕਲਿੱਕ ਕਰੋ।

## ਕਦਮ 2: Azure AI Search ਨਾਲ ਸ਼ੁਰੂਆਤ ਕਰੋ

1. ਜਦੋਂ ਡਿਪਲੋਇਮੈਂਟ ਮੁਕੰਮਲ ਹੋ ਜਾਵੇ, ਤਾਂ Azure ਪੋਰਟਲ ਵਿੱਚ ਆਪਣੀ search service 'ਤੇ ਜਾਓ।
2. search service ਦੇ ਓਵਰਵਿਊ ਪੇਜ 'ਤੇ **Quickstart** ਬਟਨ 'ਤੇ ਕਲਿੱਕ ਕਰੋ।
3. Quickstart ਗਾਈਡ ਵਿੱਚ ਦਿੱਤੇ ਕਦਮਾਂ ਦੀ ਪਾਲਣਾ ਕਰਦੇ ਹੋਏ ਇੱਕ ਇੰਡੈਕਸ ਬਣਾਓ, ਡਾਟਾ ਅਪਲੋਡ ਕਰੋ ਅਤੇ search query ਚਲਾਓ।

### ਇੰਡੈਕਸ ਬਣਾਓ

1. Quickstart ਗਾਈਡ ਵਿੱਚ **Create an index** 'ਤੇ ਕਲਿੱਕ ਕਰੋ।
2. ਇੰਡੈਕਸ ਸਕੀਮਾ ਨੂੰ ਪਰਿਭਾਸ਼ਿਤ ਕਰੋ, ਜਿਸ ਵਿੱਚ ਫੀਲਡਾਂ ਅਤੇ ਉਹਨਾਂ ਦੇ ਗੁਣ (ਜਿਵੇਂ ਕਿ ਡਾਟਾ ਟਾਈਪ, searchable, filterable) ਸ਼ਾਮਲ ਹਨ।
3. ਇੰਡੈਕਸ ਬਣਾਉਣ ਲਈ **Create** 'ਤੇ ਕਲਿੱਕ ਕਰੋ।

### ਡਾਟਾ ਅਪਲੋਡ ਕਰੋ

1. Quickstart ਗਾਈਡ ਵਿੱਚ **Upload data** 'ਤੇ ਕਲਿੱਕ ਕਰੋ।
2. ਇੱਕ ਡਾਟਾ ਸੋਰਸ ਚੁਣੋ (ਜਿਵੇਂ Azure Blob Storage, Azure SQL Database) ਅਤੇ ਜ਼ਰੂਰੀ ਕਨੈਕਸ਼ਨ ਵੇਰਵੇ ਦਿਓ।
3. ਡਾਟਾ ਸੋਰਸ ਫੀਲਡਾਂ ਨੂੰ ਇੰਡੈਕਸ ਫੀਲਡਾਂ ਨਾਲ ਮੈਪ ਕਰੋ।
4. ਡਾਟਾ ਇੰਡੈਕਸ ਵਿੱਚ ਅਪਲੋਡ ਕਰਨ ਲਈ **Submit** 'ਤੇ ਕਲਿੱਕ ਕਰੋ।

### Search Query ਚਲਾਓ

1. Quickstart ਗਾਈਡ ਵਿੱਚ **Search explorer** 'ਤੇ ਕਲਿੱਕ ਕਰੋ।
2. search ਬਾਕਸ ਵਿੱਚ ਇੱਕ search query ਦਾਖਲ ਕਰੋ ਤਾਂ ਜੋ search ਫੰਕਸ਼ਨਾਲਿਟੀ ਦੀ ਜਾਂਚ ਕੀਤੀ ਜਾ ਸਕੇ।
3. search ਨਤੀਜਿਆਂ ਦੀ ਸਮੀਖਿਆ ਕਰੋ ਅਤੇ ਜਰੂਰਤ ਮੁਤਾਬਕ ਇੰਡੈਕਸ ਸਕੀਮਾ ਜਾਂ ਡਾਟਾ ਨੂੰ ਸੋਧੋ।

## ਕਦਮ 3: Azure AI Search ਟੂਲਜ਼ ਦੀ ਵਰਤੋਂ ਕਰੋ

Azure AI Search ਵੱਖ-ਵੱਖ ਟੂਲਜ਼ ਨਾਲ ਇੰਟੀਗ੍ਰੇਟ ਹੁੰਦਾ ਹੈ ਤਾਂ ਜੋ ਤੁਹਾਡੇ search ਸਮਰੱਥਾਵਾਂ ਨੂੰ ਵਧਾਇਆ ਜਾ ਸਕੇ। ਤੁਸੀਂ Azure CLI, Python SDK ਅਤੇ ਹੋਰ ਟੂਲਜ਼ ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਅਡਵਾਂਸਡ ਸੰਰਚਨਾਵਾਂ ਅਤੇ ਓਪਰੇਸ਼ਨਾਂ ਕਰ ਸਕਦੇ ਹੋ।

### Azure CLI ਦੀ ਵਰਤੋਂ

1. [Install Azure CLI](https://learn.microsoft.com/en-us/cli/azure/install-azure-cli?wt.mc_id=studentamb_258691) 'ਤੇ ਦਿੱਤੀਆਂ ਹਦਾਇਤਾਂ ਦੀ ਪਾਲਣਾ ਕਰਕੇ Azure CLI ਇੰਸਟਾਲ ਕਰੋ।
2. ਹੇਠਾਂ ਦਿੱਤੇ ਕਮਾਂਡ ਨਾਲ Azure CLI ਵਿੱਚ ਸਾਈਨ ਇਨ ਕਰੋ:
   ```bash
   az login
   ```
3. Azure CLI ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਨਵੀਂ search service ਬਣਾਓ:
   ```bash
   az search service create --resource-group <resource-group> --name <service-name> --sku Free
   ```
4. Azure CLI ਨਾਲ ਇੰਡੈਕਸ ਬਣਾਓ:
   ```bash
   az search index create --service-name <service-name> --name <index-name> --fields "field1:type, field2:type"
   ```

### Python SDK ਦੀ ਵਰਤੋਂ

1. Python ਲਈ Azure Cognitive Search ਕਲਾਇੰਟ ਲਾਇਬ੍ਰੇਰੀ ਇੰਸਟਾਲ ਕਰੋ:
   ```bash
   pip install azure-search-documents
   ```
2. ਹੇਠਾਂ ਦਿੱਤੇ Python ਕੋਡ ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਇੰਡੈਕਸ ਬਣਾਓ ਅਤੇ ਦਸਤਾਵੇਜ਼ ਅਪਲੋਡ ਕਰੋ:
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

ਵਧੇਰੇ ਵਿਸਥਾਰ ਲਈ, ਹੇਠਾਂ ਦਿੱਤੇ ਦਸਤਾਵੇਜ਼ਾਂ ਨੂੰ ਵੇਖੋ:

- [Create an Azure Cognitive Search service](https://learn.microsoft.com/en-us/azure/search/search-create-service-portal?wt.mc_id=studentamb_258691)
- [Get started with Azure Cognitive Search](https://learn.microsoft.com/en-us/azure/search/search-get-started-portal?wt.mc_id=studentamb_258691)
- [Azure AI Search Tools](https://learn.microsoft.com/en-us/azure/ai-services/agents/how-to/tools/azure-ai-search?tabs=azurecli%2Cpython&pivots=code-examples?wt.mc_id=studentamb_258691)

## ਨਤੀਜਾ

ਤੁਸੀਂ Azure ਪੋਰਟਲ ਅਤੇ ਇੰਟੀਗ੍ਰੇਟ ਕੀਤੇ ਟੂਲਜ਼ ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਸਫਲਤਾਪੂਰਵਕ Azure AI Search ਸੈਟਅਪ ਕਰ ਲਿਆ ਹੈ। ਹੁਣ ਤੁਸੀਂ Azure AI Search ਦੀਆਂ ਹੋਰ ਅਡਵਾਂਸਡ ਵਿਸ਼ੇਸ਼ਤਾਵਾਂ ਅਤੇ ਸਮਰੱਥਾਵਾਂ ਦੀ ਖੋਜ ਕਰ ਸਕਦੇ ਹੋ ਤਾਂ ਜੋ ਆਪਣੀਆਂ search ਹੱਲਾਂ ਨੂੰ ਹੋਰ ਬਿਹਤਰ ਬਣਾਇਆ ਜਾ ਸਕੇ।

ਵਧੇਰੇ ਮਦਦ ਲਈ, [Azure Cognitive Search documentation](https://learn.microsoft.com/en-us/azure/search/?wt.mc_id=studentamb_258691) 'ਤੇ ਜਾਓ।

**ਅਸਵੀਕਾਰੋਪਣ**:  
ਇਹ ਦਸਤਾਵੇਜ਼ AI ਅਨੁਵਾਦ ਸੇਵਾ [Co-op Translator](https://github.com/Azure/co-op-translator) ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਅਨੁਵਾਦਿਤ ਕੀਤਾ ਗਿਆ ਹੈ। ਜਦੋਂ ਕਿ ਅਸੀਂ ਸਹੀਅਤ ਲਈ ਕੋਸ਼ਿਸ਼ ਕਰਦੇ ਹਾਂ, ਕਿਰਪਾ ਕਰਕੇ ਧਿਆਨ ਰੱਖੋ ਕਿ ਸਵੈਚਾਲਿਤ ਅਨੁਵਾਦਾਂ ਵਿੱਚ ਗਲਤੀਆਂ ਜਾਂ ਅਸਮਰਥਤਾਵਾਂ ਹੋ ਸਕਦੀਆਂ ਹਨ। ਮੂਲ ਦਸਤਾਵੇਜ਼ ਆਪਣੀ ਮੂਲ ਭਾਸ਼ਾ ਵਿੱਚ ਪ੍ਰਮਾਣਿਕ ਸਰੋਤ ਮੰਨਿਆ ਜਾਣਾ ਚਾਹੀਦਾ ਹੈ। ਮਹੱਤਵਪੂਰਨ ਜਾਣਕਾਰੀ ਲਈ, ਪੇਸ਼ੇਵਰ ਮਨੁੱਖੀ ਅਨੁਵਾਦ ਦੀ ਸਿਫਾਰਸ਼ ਕੀਤੀ ਜਾਂਦੀ ਹੈ। ਅਸੀਂ ਇਸ ਅਨੁਵਾਦ ਦੀ ਵਰਤੋਂ ਤੋਂ ਉਤਪੰਨ ਕਿਸੇ ਵੀ ਗਲਤਫਹਮੀ ਜਾਂ ਗਲਤ ਵਿਆਖਿਆ ਲਈ ਜ਼ਿੰਮੇਵਾਰ ਨਹੀਂ ਹਾਂ।