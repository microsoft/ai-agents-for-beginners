<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f0ce2d470f3efad6f8c7df376f416a4b",
  "translation_date": "2025-07-12T07:39:08+00:00",
  "source_file": "00-course-setup/AzureSearch.md",
  "language_code": "sw"
}
-->
# Azure AI Search Setup Guide

Mwongozo huu utakusaidia kuanzisha Azure AI Search kwa kutumia Azure portal. Fuata hatua zilizo hapa chini kuunda na kusanidi huduma yako ya Azure AI Search.

## Prerequisites

Kabla ya kuanza, hakikisha una yafuatayo:

- Usajili wa Azure. Ikiwa huna usajili wa Azure, unaweza kuunda akaunti ya bure kwenye [Azure Free Account](https://azure.microsoft.com/free/?wt.mc_id=studentamb_258691).

## Step 1: Create an Azure AI Search Service

1. Ingia kwenye [Azure portal](https://portal.azure.com/?wt.mc_id=studentamb_258691).
2. Katika sehemu ya urambazaji upande wa kushoto, bonyeza **Create a resource**.
3. Katika kisanduku cha utafutaji, andika "Azure AI Search" kisha chagua **Azure AI Search** kutoka kwenye orodha ya matokeo.
4. Bonyeza kitufe cha **Create**.
5. Katika kichupo cha **Basics**, toa taarifa zifuatazo:
   - **Subscription**: Chagua usajili wako wa Azure.
   - **Resource group**: Unda kundi jipya la rasilimali au chagua lililopo.
   - **Resource name**: Weka jina la kipekee kwa huduma yako ya utafutaji.
   - **Region**: Chagua eneo lililo karibu zaidi na watumiaji wako.
   - **Pricing tier**: Chagua kiwango cha bei kinachokidhi mahitaji yako. Unaweza kuanza na kiwango cha Bure kwa majaribio.
6. Bonyeza **Review + create**.
7. Kagua mipangilio na bonyeza **Create** kuunda huduma ya utafutaji.

## Step 2: Get Started with Azure AI Search

1. Mara baada ya usambazaji kukamilika, nenda kwenye huduma yako ya utafutaji katika Azure portal.
2. Katika ukurasa wa muhtasari wa huduma ya utafutaji, bonyeza kitufe cha **Quickstart**.
3. Fuata hatua katika mwongozo wa Quickstart kuunda index, kupakia data, na kufanya swali la utafutaji.

### Create an Index

1. Katika mwongozo wa Quickstart, bonyeza **Create an index**.
2. Eleza muundo wa index kwa kubainisha sehemu na sifa zake (mfano, aina ya data, inatafutika, inaweza kuchujwa).
3. Bonyeza **Create** kuunda index.

### Upload Data

1. Katika mwongozo wa Quickstart, bonyeza **Upload data**.
2. Chagua chanzo cha data (mfano, Azure Blob Storage, Azure SQL Database) na toa maelezo ya muunganisho yanayohitajika.
3. Ramani sehemu za chanzo cha data kwa sehemu za index.
4. Bonyeza **Submit** kupakia data kwenye index.

### Perform a Search Query

1. Katika mwongozo wa Quickstart, bonyeza **Search explorer**.
2. Weka swali la utafutaji kwenye kisanduku cha utafutaji kujaribu utendaji wa utafutaji.
3. Kagua matokeo ya utafutaji na rekebisha muundo wa index au data kama inavyohitajika.

## Step 3: Use Azure AI Search Tools

Azure AI Search inaunganishwa na zana mbalimbali ili kuboresha uwezo wako wa utafutaji. Unaweza kutumia Azure CLI, Python SDK, na zana nyingine kwa usanidi na shughuli za hali ya juu.

### Using Azure CLI

1. Sakinisha Azure CLI kwa kufuata maelekezo kwenye [Install Azure CLI](https://learn.microsoft.com/en-us/cli/azure/install-azure-cli?wt.mc_id=studentamb_258691).
2. Ingia kwenye Azure CLI kwa kutumia amri:
   ```bash
   az login
   ```
3. Unda huduma mpya ya utafutaji kwa kutumia Azure CLI:
   ```bash
   az search service create --resource-group <resource-group> --name <service-name> --sku Free
   ```
4. Unda index kwa kutumia Azure CLI:
   ```bash
   az search index create --service-name <service-name> --name <index-name> --fields "field1:type, field2:type"
   ```

### Using Python SDK

1. Sakinisha maktaba ya mteja wa Azure Cognitive Search kwa Python:
   ```bash
   pip install azure-search-documents
   ```
2. Tumia msimbo wa Python ufuatao kuunda index na kupakia nyaraka:
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

Kwa maelezo zaidi, rejea nyaraka zifuatazo:

- [Create an Azure Cognitive Search service](https://learn.microsoft.com/en-us/azure/search/search-create-service-portal?wt.mc_id=studentamb_258691)
- [Get started with Azure Cognitive Search](https://learn.microsoft.com/en-us/azure/search/search-get-started-portal?wt.mc_id=studentamb_258691)
- [Azure AI Search Tools](https://learn.microsoft.com/en-us/azure/ai-services/agents/how-to/tools/azure-ai-search?tabs=azurecli%2Cpython&pivots=code-examples?wt.mc_id=studentamb_258691)

## Conclusion

Umefanikiwa kuanzisha Azure AI Search kwa kutumia Azure portal na zana zilizounganishwa. Sasa unaweza kuchunguza vipengele na uwezo wa hali ya juu wa Azure AI Search ili kuboresha suluhisho zako za utafutaji.

Kwa msaada zaidi, tembelea [Azure Cognitive Search documentation](https://learn.microsoft.com/en-us/azure/search/?wt.mc_id=studentamb_258691).

**Kiarifu cha Kutotegemea**:  
Hati hii imetafsiriwa kwa kutumia huduma ya tafsiri ya AI [Co-op Translator](https://github.com/Azure/co-op-translator). Ingawa tunajitahidi kwa usahihi, tafadhali fahamu kwamba tafsiri za kiotomatiki zinaweza kuwa na makosa au upungufu wa usahihi. Hati ya asili katika lugha yake ya asili inapaswa kuchukuliwa kama chanzo cha mamlaka. Kwa taarifa muhimu, tafsiri ya kitaalamu inayofanywa na binadamu inashauriwa. Hatubebei dhamana kwa kutoelewana au tafsiri potofu zinazotokana na matumizi ya tafsiri hii.