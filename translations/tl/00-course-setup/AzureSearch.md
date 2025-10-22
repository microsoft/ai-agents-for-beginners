<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f0ce2d470f3efad6f8c7df376f416a4b",
  "translation_date": "2025-07-12T07:38:58+00:00",
  "source_file": "00-course-setup/AzureSearch.md",
  "language_code": "tl"
}
-->
# Azure AI Search Setup Guide

Tutulungan ka ng gabay na ito na i-setup ang Azure AI Search gamit ang Azure portal. Sundin ang mga hakbang sa ibaba para gumawa at i-configure ang iyong Azure AI Search service.

## Prerequisites

Bago ka magsimula, siguraduhing mayroon kang mga sumusunod:

- Isang Azure subscription. Kung wala ka pang Azure subscription, maaari kang gumawa ng libreng account sa [Azure Free Account](https://azure.microsoft.com/free/?wt.mc_id=studentamb_258691).

## Step 1: Gumawa ng Azure AI Search Service

1. Mag-sign in sa [Azure portal](https://portal.azure.com/?wt.mc_id=studentamb_258691).
2. Sa kaliwang navigation pane, i-click ang **Create a resource**.
3. Sa search box, i-type ang "Azure AI Search" at piliin ang **Azure AI Search** mula sa listahan ng mga resulta.
4. I-click ang **Create** button.
5. Sa **Basics** tab, ilagay ang mga sumusunod na impormasyon:
   - **Subscription**: Piliin ang iyong Azure subscription.
   - **Resource group**: Gumawa ng bagong resource group o piliin ang isang umiiral na.
   - **Resource name**: Maglagay ng natatanging pangalan para sa iyong search service.
   - **Region**: Piliin ang rehiyon na pinakamalapit sa iyong mga gumagamit.
   - **Pricing tier**: Pumili ng pricing tier na angkop sa iyong pangangailangan. Maaari kang magsimula sa Free tier para sa testing.
6. I-click ang **Review + create**.
7. Suriin ang mga settings at i-click ang **Create** para likhain ang search service.

## Step 2: Magsimula sa Azure AI Search

1. Kapag natapos na ang deployment, pumunta sa iyong search service sa Azure portal.
2. Sa search service overview page, i-click ang **Quickstart** button.
3. Sundin ang mga hakbang sa Quickstart guide para gumawa ng index, mag-upload ng data, at magsagawa ng search query.

### Gumawa ng Index

1. Sa Quickstart guide, i-click ang **Create an index**.
2. I-define ang index schema sa pamamagitan ng pagtukoy sa mga fields at kanilang mga attributes (halimbawa, data type, searchable, filterable).
3. I-click ang **Create** para likhain ang index.

### Mag-upload ng Data

1. Sa Quickstart guide, i-click ang **Upload data**.
2. Pumili ng data source (halimbawa, Azure Blob Storage, Azure SQL Database) at ilagay ang kinakailangang detalye ng koneksyon.
3. I-map ang mga data source fields sa index fields.
4. I-click ang **Submit** para i-upload ang data sa index.

### Magsagawa ng Search Query

1. Sa Quickstart guide, i-click ang **Search explorer**.
2. Maglagay ng search query sa search box para subukan ang search functionality.
3. Suriin ang mga resulta ng paghahanap at ayusin ang index schema o data kung kinakailangan.

## Step 3: Gamitin ang Azure AI Search Tools

Ang Azure AI Search ay maaaring gamitin kasama ng iba't ibang tools para mapahusay ang iyong search capabilities. Maaari mong gamitin ang Azure CLI, Python SDK, at iba pang tools para sa mas advanced na configurations at operasyon.

### Paggamit ng Azure CLI

1. I-install ang Azure CLI sa pamamagitan ng pagsunod sa mga tagubilin sa [Install Azure CLI](https://learn.microsoft.com/en-us/cli/azure/install-azure-cli?wt.mc_id=studentamb_258691).
2. Mag-sign in sa Azure CLI gamit ang command:
   ```bash
   az login
   ```
3. Gumawa ng bagong search service gamit ang Azure CLI:
   ```bash
   az search service create --resource-group <resource-group> --name <service-name> --sku Free
   ```
4. Gumawa ng index gamit ang Azure CLI:
   ```bash
   az search index create --service-name <service-name> --name <index-name> --fields "field1:type, field2:type"
   ```

### Paggamit ng Python SDK

1. I-install ang Azure Cognitive Search client library para sa Python:
   ```bash
   pip install azure-search-documents
   ```
2. Gamitin ang sumusunod na Python code para gumawa ng index at mag-upload ng mga dokumento:
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

Para sa mas detalyadong impormasyon, tingnan ang mga sumusunod na dokumentasyon:

- [Create an Azure Cognitive Search service](https://learn.microsoft.com/en-us/azure/search/search-create-service-portal?wt.mc_id=studentamb_258691)
- [Get started with Azure Cognitive Search](https://learn.microsoft.com/en-us/azure/search/search-get-started-portal?wt.mc_id=studentamb_258691)
- [Azure AI Search Tools](https://learn.microsoft.com/en-us/azure/ai-services/agents/how-to/tools/azure-ai-search?tabs=azurecli%2Cpython&pivots=code-examples?wt.mc_id=studentamb_258691)

## Conclusion

Matagumpay mong na-setup ang Azure AI Search gamit ang Azure portal at mga integrated tools. Maaari mo nang tuklasin ang mas advanced na mga feature at kakayahan ng Azure AI Search para mapabuti ang iyong mga search solution.

Para sa karagdagang tulong, bisitahin ang [Azure Cognitive Search documentation](https://learn.microsoft.com/en-us/azure/search/?wt.mc_id=studentamb_258691).

**Paalala**:  
Ang dokumentong ito ay isinalin gamit ang AI translation service na [Co-op Translator](https://github.com/Azure/co-op-translator). Bagamat nagsusumikap kami para sa katumpakan, pakatandaan na ang mga awtomatikong pagsasalin ay maaaring maglaman ng mga pagkakamali o di-tumpak na impormasyon. Ang orihinal na dokumento sa orihinal nitong wika ang dapat ituring na pangunahing sanggunian. Para sa mahahalagang impormasyon, inirerekomenda ang propesyonal na pagsasalin ng tao. Hindi kami mananagot sa anumang hindi pagkakaunawaan o maling interpretasyon na maaaring magmula sa paggamit ng pagsasaling ito.