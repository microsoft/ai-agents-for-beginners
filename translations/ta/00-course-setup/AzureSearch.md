<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f0ce2d470f3efad6f8c7df376f416a4b",
  "translation_date": "2025-10-11T11:25:28+00:00",
  "source_file": "00-course-setup/AzureSearch.md",
  "language_code": "ta"
}
-->
# Azure AI Search அமைப்பு வழிகாட்டி

இந்த வழிகாட்டி Azure portal-ஐப் பயன்படுத்தி Azure AI Search-ஐ அமைக்க உதவுகிறது. Azure AI Search சேவையை உருவாக்கி அமைக்க கீழே உள்ள படிகளை பின்பற்றவும்.

## முன் தேவைகள்

தொடங்குவதற்கு முன், உங்களிடம் பின்வரும் பொருட்கள் இருக்க வேண்டும்:

- ஒரு Azure சந்தா. Azure சந்தா இல்லையெனில், [Azure Free Account](https://azure.microsoft.com/free/?wt.mc_id=studentamb_258691) இல் இலவச கணக்கை உருவாக்கலாம்.

## படி 1: Azure AI Search சேவையை உருவாக்கவும்

1. [Azure portal](https://portal.azure.com/?wt.mc_id=studentamb_258691) இல் உள்நுழைக.
2. இடது பக்க வழிசெலுத்தல் பட்டியில் **Create a resource** என்பதைக் கிளிக் செய்யவும்.
3. தேடல் பெட்டியில் "Azure AI Search" எனத் தட்டச்சு செய்து, முடிவுகளில் **Azure AI Search** ஐத் தேர்ந்தெடுக்கவும்.
4. **Create** பொத்தானைக் கிளிக் செய்யவும்.
5. **Basics** தாவலில் பின்வரும் தகவல்களை வழங்கவும்:
   - **Subscription**: உங்கள் Azure சந்தாவைத் தேர்ந்தெடுக்கவும்.
   - **Resource group**: புதிய resource group ஒன்றை உருவாக்கவும் அல்லது ஏற்கனவே உள்ள ஒன்றைத் தேர்ந்தெடுக்கவும்.
   - **Resource name**: உங்கள் தேடல் சேவைக்கு தனித்துவமான பெயரை உள்ளிடவும்.
   - **Region**: உங்கள் பயனர்களுக்கு அருகிலுள்ள பிராந்தியத்தைத் தேர்ந்தெடுக்கவும்.
   - **Pricing tier**: உங்கள் தேவைகளுக்கு ஏற்ப ஒரு விலை நிலையைத் தேர்ந்தெடுக்கவும். சோதனைக்காக இலவச நிலையைத் தொடங்கலாம்.
6. **Review + create** என்பதைக் கிளிக் செய்யவும்.
7. அமைப்புகளை மதிப்பீடு செய்து, தேடல் சேவையை உருவாக்க **Create** என்பதைக் கிளிக் செய்யவும்.

## படி 2: Azure AI Search-ஐ தொடங்கவும்

1. அமைப்பு முடிந்தவுடன், Azure portal-இல் உங்கள் தேடல் சேவைக்கு செல்லவும்.
2. தேடல் சேவை மேற்பார்வை பக்கத்தில் **Quickstart** பொத்தானைக் கிளிக் செய்யவும்.
3. Quickstart வழிகாட்டியில் உள்ள படிகளைப் பின்பற்றி ஒரு index உருவாக்கவும், தரவுகளைப் பதிவேற்றவும், மற்றும் தேடல் கேள்வியைச் செய்யவும்.

### Index உருவாக்கம்

1. Quickstart வழிகாட்டியில் **Create an index** என்பதைக் கிளிக் செய்யவும்.
2. index schema-ஐ வரையறுக்க, புலங்கள் மற்றும் அவற்றின் பண்புகளை (எ.கா., தரவுத் வகை, தேடக்கூடியது, வடிகட்டக்கூடியது) குறிப்பிடவும்.
3. **Create** என்பதைக் கிளிக் செய்து index-ஐ உருவாக்கவும்.

### தரவுகளைப் பதிவேற்றம்

1. Quickstart வழிகாட்டியில் **Upload data** என்பதைக் கிளிக் செய்யவும்.
2. ஒரு தரவூற்று (எ.கா., Azure Blob Storage, Azure SQL Database) தேர்ந்தெடுத்து தேவையான இணைப்பு விவரங்களை வழங்கவும்.
3. தரவூற்று புலங்களை index புலங்களுக்கு வரைபடம் செய்யவும்.
4. **Submit** என்பதைக் கிளிக் செய்து தரவுகளை index-க்கு பதிவேற்றவும்.

### தேடல் கேள்வி செய்யவும்

1. Quickstart வழிகாட்டியில் **Search explorer** என்பதைக் கிளிக் செய்யவும்.
2. தேடல் பெட்டியில் ஒரு தேடல் கேள்வியை உள்ளீடு செய்து தேடல் செயல்பாட்டைச் சோதிக்கவும்.
3. தேடல் முடிவுகளை மதிப்பீடு செய்து, index schema அல்லது தரவுகளை தேவையானவாறு சரிசெய்யவும்.

## படி 3: Azure AI Search கருவிகளைப் பயன்படுத்தவும்

Azure AI Search பல கருவிகளுடன் ஒருங்கிணைக்கிறது, இது உங்கள் தேடல் திறன்களை மேம்படுத்த உதவுகிறது. Azure CLI, Python SDK மற்றும் பிற கருவிகளை மேம்பட்ட அமைப்புகள் மற்றும் செயல்பாடுகளுக்கு பயன்படுத்தலாம்.

### Azure CLI பயன்படுத்துதல்

1. [Install Azure CLI](https://learn.microsoft.com/en-us/cli/azure/install-azure-cli?wt.mc_id=studentamb_258691) வழிகாட்டியைப் பின்பற்றி Azure CLI-ஐ நிறுவவும்.
2. கீழே உள்ள கட்டளையைப் பயன்படுத்தி Azure CLI-இல் உள்நுழைக:
   ```bash
   az login
   ```
3. Azure CLI-ஐப் பயன்படுத்தி புதிய தேடல் சேவையை உருவாக்கவும்:
   ```bash
   az search service create --resource-group <resource-group> --name <service-name> --sku Free
   ```
4. Azure CLI-ஐப் பயன்படுத்தி index ஒன்றை உருவாக்கவும்:
   ```bash
   az search index create --service-name <service-name> --name <index-name> --fields "field1:type, field2:type"
   ```

### Python SDK பயன்படுத்துதல்

1. Python-க்கு Azure Cognitive Search client library-ஐ நிறுவவும்:
   ```bash
   pip install azure-search-documents
   ```
2. கீழே உள்ள Python குறியீட்டைப் பயன்படுத்தி index உருவாக்கவும் மற்றும் ஆவணங்களைப் பதிவேற்றவும்:
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

மேலும் விரிவான தகவலுக்கு, பின்வரும் ஆவணங்களைப் பார்க்கவும்:

- [Create an Azure Cognitive Search service](https://learn.microsoft.com/en-us/azure/search/search-create-service-portal?wt.mc_id=studentamb_258691)
- [Get started with Azure Cognitive Search](https://learn.microsoft.com/en-us/azure/search/search-get-started-portal?wt.mc_id=studentamb_258691)
- [Azure AI Search Tools](https://learn.microsoft.com/en-us/azure/ai-services/agents/how-to/tools/azure-ai-search?tabs=azurecli%2Cpython&pivots=code-examples?wt.mc_id=studentamb_258691)

## முடிவு

Azure portal-ஐப் பயன்படுத்தி Azure AI Search-ஐ வெற்றிகரமாக அமைத்து, கருவிகளை ஒருங்கிணைத்துள்ளீர்கள். Azure AI Search-இன் மேம்பட்ட அம்சங்கள் மற்றும் திறன்களை ஆராய்ந்து உங்கள் தேடல் தீர்வுகளை மேம்படுத்தலாம்.

மேலும் உதவிக்காக, [Azure Cognitive Search documentation](https://learn.microsoft.com/en-us/azure/search/?wt.mc_id=studentamb_258691) ஐப் பார்வையிடவும்.

---

**குறிப்பு**:  
இந்த ஆவணம் [Co-op Translator](https://github.com/Azure/co-op-translator) என்ற AI மொழிபெயர்ப்பு சேவையைப் பயன்படுத்தி மொழிபெயர்க்கப்பட்டுள்ளது. நாங்கள் துல்லியத்திற்காக முயற்சிக்கின்றோம், ஆனால் தானியங்கி மொழிபெயர்ப்புகளில் பிழைகள் அல்லது தவறான தகவல்கள் இருக்கக்கூடும் என்பதை தயவுசெய்து கவனத்தில் கொள்ளவும். அதன் தாய்மொழியில் உள்ள மூல ஆவணம் அதிகாரப்பூர்வ ஆதாரமாக கருதப்பட வேண்டும். முக்கியமான தகவல்களுக்கு, தொழில்முறை மனித மொழிபெயர்ப்பு பரிந்துரைக்கப்படுகிறது. இந்த மொழிபெயர்ப்பைப் பயன்படுத்துவதால் ஏற்படும் எந்த தவறான புரிதல்கள் அல்லது தவறான விளக்கங்களுக்கு நாங்கள் பொறுப்பல்ல.