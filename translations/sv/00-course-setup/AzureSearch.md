<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f0ce2d470f3efad6f8c7df376f416a4b",
  "translation_date": "2025-07-12T07:37:22+00:00",
  "source_file": "00-course-setup/AzureSearch.md",
  "language_code": "sv"
}
-->
# Azure AI Search installationsguide

Den här guiden hjälper dig att ställa in Azure AI Search via Azure-portalen. Följ stegen nedan för att skapa och konfigurera din Azure AI Search-tjänst.

## Förutsättningar

Innan du börjar, se till att du har följande:

- Ett Azure-abonnemang. Om du inte har ett Azure-abonnemang kan du skapa ett gratis konto på [Azure Free Account](https://azure.microsoft.com/free/?wt.mc_id=studentamb_258691).

## Steg 1: Skapa en Azure AI Search-tjänst

1. Logga in på [Azure-portalen](https://portal.azure.com/?wt.mc_id=studentamb_258691).
2. Klicka på **Create a resource** i navigeringspanelen till vänster.
3. Skriv "Azure AI Search" i sökrutan och välj **Azure AI Search** från resultatlistan.
4. Klicka på **Create**-knappen.
5. På fliken **Basics**, ange följande information:
   - **Subscription**: Välj ditt Azure-abonnemang.
   - **Resource group**: Skapa en ny resursgrupp eller välj en befintlig.
   - **Resource name**: Ange ett unikt namn för din söktjänst.
   - **Region**: Välj den region som ligger närmast dina användare.
   - **Pricing tier**: Välj en prisklass som passar dina behov. Du kan börja med Free-tier för testning.
6. Klicka på **Review + create**.
7. Granska inställningarna och klicka på **Create** för att skapa söktjänsten.

## Steg 2: Kom igång med Azure AI Search

1. När distributionen är klar, gå till din söktjänst i Azure-portalen.
2. På översiktssidan för söktjänsten, klicka på **Quickstart**-knappen.
3. Följ stegen i Quickstart-guiden för att skapa ett index, ladda upp data och utföra en sökfråga.

### Skapa ett index

1. I Quickstart-guiden, klicka på **Create an index**.
2. Definiera indexschemat genom att specificera fälten och deras attribut (t.ex. datatyp, sökbar, filtrerbar).
3. Klicka på **Create** för att skapa indexet.

### Ladda upp data

1. I Quickstart-guiden, klicka på **Upload data**.
2. Välj en datakälla (t.ex. Azure Blob Storage, Azure SQL Database) och ange nödvändiga anslutningsuppgifter.
3. Mappa datakällans fält till indexets fält.
4. Klicka på **Submit** för att ladda upp data till indexet.

### Utför en sökfråga

1. I Quickstart-guiden, klicka på **Search explorer**.
2. Skriv in en sökfråga i sökrutan för att testa sökfunktionen.
3. Granska sökresultaten och justera indexschemat eller data vid behov.

## Steg 3: Använd Azure AI Search-verktyg

Azure AI Search integreras med olika verktyg för att förbättra dina sökmöjligheter. Du kan använda Azure CLI, Python SDK och andra verktyg för avancerade konfigurationer och operationer.

### Använda Azure CLI

1. Installera Azure CLI genom att följa instruktionerna på [Install Azure CLI](https://learn.microsoft.com/en-us/cli/azure/install-azure-cli?wt.mc_id=studentamb_258691).
2. Logga in i Azure CLI med kommandot:
   ```bash
   az login
   ```
3. Skapa en ny söktjänst med Azure CLI:
   ```bash
   az search service create --resource-group <resource-group> --name <service-name> --sku Free
   ```
4. Skapa ett index med Azure CLI:
   ```bash
   az search index create --service-name <service-name> --name <index-name> --fields "field1:type, field2:type"
   ```

### Använda Python SDK

1. Installera Azure Cognitive Search-klientbiblioteket för Python:
   ```bash
   pip install azure-search-documents
   ```
2. Använd följande Python-kod för att skapa ett index och ladda upp dokument:
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

För mer detaljerad information, se följande dokumentation:

- [Create an Azure Cognitive Search service](https://learn.microsoft.com/en-us/azure/search/search-create-service-portal?wt.mc_id=studentamb_258691)
- [Get started with Azure Cognitive Search](https://learn.microsoft.com/en-us/azure/search/search-get-started-portal?wt.mc_id=studentamb_258691)
- [Azure AI Search Tools](https://learn.microsoft.com/en-us/azure/ai-services/agents/how-to/tools/azure-ai-search?tabs=azurecli%2Cpython&pivots=code-examples?wt.mc_id=studentamb_258691)

## Avslutning

Du har nu framgångsrikt ställt in Azure AI Search via Azure-portalen och integrerat verktyg. Du kan nu utforska mer avancerade funktioner och möjligheter i Azure AI Search för att förbättra dina söklösningar.

För ytterligare hjälp, besök [Azure Cognitive Search documentation](https://learn.microsoft.com/en-us/azure/search/?wt.mc_id=studentamb_258691).

**Ansvarsfriskrivning**:  
Detta dokument har översatts med hjälp av AI-översättningstjänsten [Co-op Translator](https://github.com/Azure/co-op-translator). Även om vi strävar efter noggrannhet, vänligen observera att automatiska översättningar kan innehålla fel eller brister. Det ursprungliga dokumentet på dess modersmål bör betraktas som den auktoritativa källan. För kritisk information rekommenderas professionell mänsklig översättning. Vi ansvarar inte för några missförstånd eller feltolkningar som uppstår till följd av användningen av denna översättning.