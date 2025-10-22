<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f0ce2d470f3efad6f8c7df376f416a4b",
  "translation_date": "2025-07-12T07:37:33+00:00",
  "source_file": "00-course-setup/AzureSearch.md",
  "language_code": "da"
}
-->
# Azure AI Search Opsætningsguide

Denne guide hjælper dig med at opsætte Azure AI Search via Azure-portalen. Følg trinene nedenfor for at oprette og konfigurere din Azure AI Search-tjeneste.

## Forudsætninger

Før du går i gang, skal du sikre dig, at du har følgende:

- Et Azure-abonnement. Hvis du ikke har et Azure-abonnement, kan du oprette en gratis konto på [Azure Free Account](https://azure.microsoft.com/free/?wt.mc_id=studentamb_258691).

## Trin 1: Opret en Azure AI Search-tjeneste

1. Log ind på [Azure-portalen](https://portal.azure.com/?wt.mc_id=studentamb_258691).
2. Klik på **Create a resource** i navigationspanelet til venstre.
3. Skriv "Azure AI Search" i søgefeltet, og vælg **Azure AI Search** fra listen over resultater.
4. Klik på **Create**-knappen.
5. Under fanen **Basics** skal du angive følgende oplysninger:
   - **Subscription**: Vælg dit Azure-abonnement.
   - **Resource group**: Opret en ny resource group eller vælg en eksisterende.
   - **Resource name**: Indtast et unikt navn til din søgetjeneste.
   - **Region**: Vælg den region, der er tættest på dine brugere.
   - **Pricing tier**: Vælg en prisplan, der passer til dine behov. Du kan starte med Free-tier til testformål.
6. Klik på **Review + create**.
7. Gennemgå indstillingerne, og klik på **Create** for at oprette søgetjenesten.

## Trin 2: Kom i gang med Azure AI Search

1. Når udrulningen er færdig, skal du navigere til din søgetjeneste i Azure-portalen.
2. På oversigtssiden for søgetjenesten skal du klikke på **Quickstart**-knappen.
3. Følg trinene i Quickstart-guiden for at oprette et indeks, uploade data og udføre en søgeforespørgsel.

### Opret et indeks

1. I Quickstart-guiden skal du klikke på **Create an index**.
2. Definér indeks-skemaet ved at angive felterne og deres egenskaber (f.eks. datatype, søgbar, filtrerbar).
3. Klik på **Create** for at oprette indekset.

### Upload data

1. I Quickstart-guiden skal du klikke på **Upload data**.
2. Vælg en datakilde (f.eks. Azure Blob Storage, Azure SQL Database) og angiv de nødvendige forbindelsesoplysninger.
3. Kortlæg datakildens felter til indeksfelterne.
4. Klik på **Submit** for at uploade data til indekset.

### Udfør en søgeforespørgsel

1. I Quickstart-guiden skal du klikke på **Search explorer**.
2. Indtast en søgeforespørgsel i søgefeltet for at teste søgefunktionen.
3. Gennemgå søgeresultaterne og juster indeks-skemaet eller data efter behov.

## Trin 3: Brug Azure AI Search-værktøjer

Azure AI Search integreres med forskellige værktøjer for at forbedre dine søgemuligheder. Du kan bruge Azure CLI, Python SDK og andre værktøjer til avancerede konfigurationer og operationer.

### Brug af Azure CLI

1. Installer Azure CLI ved at følge vejledningen på [Install Azure CLI](https://learn.microsoft.com/en-us/cli/azure/install-azure-cli?wt.mc_id=studentamb_258691).
2. Log ind på Azure CLI med kommandoen:
   ```bash
   az login
   ```
3. Opret en ny søgetjeneste ved hjælp af Azure CLI:
   ```bash
   az search service create --resource-group <resource-group> --name <service-name> --sku Free
   ```
4. Opret et indeks ved hjælp af Azure CLI:
   ```bash
   az search index create --service-name <service-name> --name <index-name> --fields "field1:type, field2:type"
   ```

### Brug af Python SDK

1. Installer Azure Cognitive Search klientbiblioteket til Python:
   ```bash
   pip install azure-search-documents
   ```
2. Brug følgende Python-kode til at oprette et indeks og uploade dokumenter:
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

For mere detaljeret information, se følgende dokumentation:

- [Create an Azure Cognitive Search service](https://learn.microsoft.com/en-us/azure/search/search-create-service-portal?wt.mc_id=studentamb_258691)
- [Get started with Azure Cognitive Search](https://learn.microsoft.com/en-us/azure/search/search-get-started-portal?wt.mc_id=studentamb_258691)
- [Azure AI Search Tools](https://learn.microsoft.com/en-us/azure/ai-services/agents/how-to/tools/azure-ai-search?tabs=azurecli%2Cpython&pivots=code-examples?wt.mc_id=studentamb_258691)

## Konklusion

Du har nu med succes opsat Azure AI Search via Azure-portalen og integrerede værktøjer. Du kan nu udforske mere avancerede funktioner og muligheder i Azure AI Search for at forbedre dine søgeløsninger.

For yderligere hjælp, besøg [Azure Cognitive Search documentation](https://learn.microsoft.com/en-us/azure/search/?wt.mc_id=studentamb_258691).

**Ansvarsfraskrivelse**:  
Dette dokument er blevet oversat ved hjælp af AI-oversættelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selvom vi bestræber os på nøjagtighed, bedes du være opmærksom på, at automatiserede oversættelser kan indeholde fejl eller unøjagtigheder. Det oprindelige dokument på dets oprindelige sprog bør betragtes som den autoritative kilde. For kritisk information anbefales professionel menneskelig oversættelse. Vi påtager os intet ansvar for misforståelser eller fejltolkninger, der opstår som følge af brugen af denne oversættelse.