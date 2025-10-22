<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f0ce2d470f3efad6f8c7df376f416a4b",
  "translation_date": "2025-07-12T07:37:43+00:00",
  "source_file": "00-course-setup/AzureSearch.md",
  "language_code": "no"
}
-->
# Azure AI Search Oppsettveiledning

Denne veiledningen hjelper deg med å sette opp Azure AI Search ved bruk av Azure-portalen. Følg trinnene nedenfor for å opprette og konfigurere din Azure AI Search-tjeneste.

## Forutsetninger

Før du begynner, sørg for at du har følgende:

- Et Azure-abonnement. Hvis du ikke har et Azure-abonnement, kan du opprette en gratis konto på [Azure Free Account](https://azure.microsoft.com/free/?wt.mc_id=studentamb_258691).

## Trinn 1: Opprett en Azure AI Search-tjeneste

1. Logg inn på [Azure-portalen](https://portal.azure.com/?wt.mc_id=studentamb_258691).
2. I navigasjonsruten til venstre klikker du på **Create a resource**.
3. Skriv "Azure AI Search" i søkeboksen og velg **Azure AI Search** fra resultatlisten.
4. Klikk på **Create**-knappen.
5. Under fanen **Basics**, fyll ut følgende informasjon:
   - **Subscription**: Velg ditt Azure-abonnement.
   - **Resource group**: Opprett en ny ressursgruppe eller velg en eksisterende.
   - **Resource name**: Skriv inn et unikt navn for søketjenesten din.
   - **Region**: Velg regionen som er nærmest brukerne dine.
   - **Pricing tier**: Velg en prisplan som passer dine behov. Du kan starte med Free-tier for testing.
6. Klikk på **Review + create**.
7. Gå gjennom innstillingene og klikk **Create** for å opprette søketjenesten.

## Trinn 2: Kom i gang med Azure AI Search

1. Når distribusjonen er fullført, naviger til søketjenesten din i Azure-portalen.
2. På oversiktssiden for søketjenesten klikker du på **Quickstart**-knappen.
3. Følg trinnene i Quickstart-veiledningen for å opprette et indeks, laste opp data og utføre et søk.

### Opprett et indeks

1. I Quickstart-veiledningen klikker du på **Create an index**.
2. Definer indeksens skjema ved å spesifisere feltene og deres egenskaper (f.eks. datatype, søkbar, filtrerbar).
3. Klikk på **Create** for å opprette indeksen.

### Last opp data

1. I Quickstart-veiledningen klikker du på **Upload data**.
2. Velg en datakilde (f.eks. Azure Blob Storage, Azure SQL Database) og oppgi nødvendige tilkoblingsdetaljer.
3. Koble datakildens felter til indeksens felter.
4. Klikk på **Submit** for å laste opp data til indeksen.

### Utfør et søk

1. I Quickstart-veiledningen klikker du på **Search explorer**.
2. Skriv inn en søkespørring i søkeboksen for å teste søkefunksjonaliteten.
3. Gå gjennom søkeresultatene og juster indeksens skjema eller data etter behov.

## Trinn 3: Bruk Azure AI Search-verktøy

Azure AI Search integreres med ulike verktøy for å forbedre søkefunksjonaliteten. Du kan bruke Azure CLI, Python SDK og andre verktøy for avanserte konfigurasjoner og operasjoner.

### Bruke Azure CLI

1. Installer Azure CLI ved å følge instruksjonene på [Install Azure CLI](https://learn.microsoft.com/en-us/cli/azure/install-azure-cli?wt.mc_id=studentamb_258691).
2. Logg inn i Azure CLI med kommandoen:
   ```bash
   az login
   ```
3. Opprett en ny søketjeneste med Azure CLI:
   ```bash
   az search service create --resource-group <resource-group> --name <service-name> --sku Free
   ```
4. Opprett et indeks med Azure CLI:
   ```bash
   az search index create --service-name <service-name> --name <index-name> --fields "field1:type, field2:type"
   ```

### Bruke Python SDK

1. Installer Azure Cognitive Search-klientbiblioteket for Python:
   ```bash
   pip install azure-search-documents
   ```
2. Bruk følgende Python-kode for å opprette et indeks og laste opp dokumenter:
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

For mer detaljert informasjon, se følgende dokumentasjon:

- [Create an Azure Cognitive Search service](https://learn.microsoft.com/en-us/azure/search/search-create-service-portal?wt.mc_id=studentamb_258691)
- [Get started with Azure Cognitive Search](https://learn.microsoft.com/en-us/azure/search/search-get-started-portal?wt.mc_id=studentamb_258691)
- [Azure AI Search Tools](https://learn.microsoft.com/en-us/azure/ai-services/agents/how-to/tools/azure-ai-search?tabs=azurecli%2Cpython&pivots=code-examples?wt.mc_id=studentamb_258691)

## Konklusjon

Du har nå satt opp Azure AI Search ved hjelp av Azure-portalen og integrerte verktøy. Du kan nå utforske mer avanserte funksjoner og muligheter i Azure AI Search for å forbedre søkeløsningene dine.

For ytterligere hjelp, besøk [Azure Cognitive Search documentation](https://learn.microsoft.com/en-us/azure/search/?wt.mc_id=studentamb_258691).

**Ansvarsfraskrivelse**:  
Dette dokumentet er oversatt ved hjelp av AI-oversettelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selv om vi streber etter nøyaktighet, vennligst vær oppmerksom på at automatiske oversettelser kan inneholde feil eller unøyaktigheter. Det opprinnelige dokumentet på originalspråket skal anses som den autoritative kilden. For kritisk informasjon anbefales profesjonell menneskelig oversettelse. Vi er ikke ansvarlige for eventuelle misforståelser eller feiltolkninger som oppstår ved bruk av denne oversettelsen.