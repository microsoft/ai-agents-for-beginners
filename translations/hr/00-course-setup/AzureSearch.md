<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f0ce2d470f3efad6f8c7df376f416a4b",
  "translation_date": "2025-07-12T07:40:34+00:00",
  "source_file": "00-course-setup/AzureSearch.md",
  "language_code": "hr"
}
-->
# Vodič za postavljanje Azure AI Search

Ovaj vodič će vam pomoći da postavite Azure AI Search koristeći Azure portal. Slijedite korake u nastavku kako biste kreirali i konfigurirali svoju Azure AI Search uslugu.

## Preduvjeti

Prije nego što započnete, provjerite imate li sljedeće:

- Azure pretplatu. Ako nemate Azure pretplatu, možete otvoriti besplatan račun na [Azure Free Account](https://azure.microsoft.com/free/?wt.mc_id=studentamb_258691).

## Korak 1: Kreirajte Azure AI Search uslugu

1. Prijavite se na [Azure portal](https://portal.azure.com/?wt.mc_id=studentamb_258691).
2. U lijevom navigacijskom izborniku kliknite na **Create a resource**.
3. U tražilicu upišite "Azure AI Search" i odaberite **Azure AI Search** s popisa rezultata.
4. Kliknite na gumb **Create**.
5. Na kartici **Basics** unesite sljedeće podatke:
   - **Subscription**: Odaberite svoju Azure pretplatu.
   - **Resource group**: Kreirajte novu resource group ili odaberite postojeću.
   - **Resource name**: Unesite jedinstveno ime za svoju search uslugu.
   - **Region**: Odaberite regiju najbližu vašim korisnicima.
   - **Pricing tier**: Odaberite cjenovni plan koji odgovara vašim potrebama. Za testiranje možete započeti s Free tier.
6. Kliknite **Review + create**.
7. Pregledajte postavke i kliknite **Create** za kreiranje search usluge.

## Korak 2: Počnite koristiti Azure AI Search

1. Nakon što je implementacija završena, otvorite svoju search uslugu u Azure portalu.
2. Na stranici pregleda search usluge kliknite na gumb **Quickstart**.
3. Slijedite korake u Quickstart vodiču za kreiranje indeksa, učitavanje podataka i izvođenje pretraživanja.

### Kreiranje indeksa

1. U Quickstart vodiču kliknite na **Create an index**.
2. Definirajte shemu indeksa tako da navedete polja i njihove atribute (npr. tip podataka, pretraživo, filtrirajuće).
3. Kliknite **Create** za kreiranje indeksa.

### Učitavanje podataka

1. U Quickstart vodiču kliknite na **Upload data**.
2. Odaberite izvor podataka (npr. Azure Blob Storage, Azure SQL Database) i unesite potrebne podatke za povezivanje.
3. Mapirajte polja izvora podataka na polja indeksa.
4. Kliknite **Submit** za učitavanje podataka u indeks.

### Izvođenje pretraživanja

1. U Quickstart vodiču kliknite na **Search explorer**.
2. Unesite upit za pretraživanje u tražilicu kako biste testirali funkcionalnost pretraživanja.
3. Pregledajte rezultate pretraživanja i po potrebi prilagodite shemu indeksa ili podatke.

## Korak 3: Koristite Azure AI Search alate

Azure AI Search se integrira s različitim alatima za poboljšanje vaših mogućnosti pretraživanja. Možete koristiti Azure CLI, Python SDK i druge alate za napredne konfiguracije i operacije.

### Korištenje Azure CLI

1. Instalirajte Azure CLI slijedeći upute na [Install Azure CLI](https://learn.microsoft.com/en-us/cli/azure/install-azure-cli?wt.mc_id=studentamb_258691).
2. Prijavite se u Azure CLI koristeći naredbu:
   ```bash
   az login
   ```
3. Kreirajte novu search uslugu koristeći Azure CLI:
   ```bash
   az search service create --resource-group <resource-group> --name <service-name> --sku Free
   ```
4. Kreirajte indeks koristeći Azure CLI:
   ```bash
   az search index create --service-name <service-name> --name <index-name> --fields "field1:type, field2:type"
   ```

### Korištenje Python SDK-a

1. Instalirajte Azure Cognitive Search klijentsku biblioteku za Python:
   ```bash
   pip install azure-search-documents
   ```
2. Koristite sljedeći Python kod za kreiranje indeksa i učitavanje dokumenata:
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

Za detaljnije informacije, pogledajte sljedeću dokumentaciju:

- [Create an Azure Cognitive Search service](https://learn.microsoft.com/en-us/azure/search/search-create-service-portal?wt.mc_id=studentamb_258691)
- [Get started with Azure Cognitive Search](https://learn.microsoft.com/en-us/azure/search/search-get-started-portal?wt.mc_id=studentamb_258691)
- [Azure AI Search Tools](https://learn.microsoft.com/en-us/azure/ai-services/agents/how-to/tools/azure-ai-search?tabs=azurecli%2Cpython&pivots=code-examples?wt.mc_id=studentamb_258691)

## Zaključak

Uspješno ste postavili Azure AI Search koristeći Azure portal i integrirane alate. Sada možete istražiti naprednije značajke i mogućnosti Azure AI Search za poboljšanje vaših rješenja za pretraživanje.

Za dodatnu pomoć posjetite [Azure Cognitive Search documentation](https://learn.microsoft.com/en-us/azure/search/?wt.mc_id=studentamb_258691).

**Odricanje od odgovornosti**:  
Ovaj dokument je preveden korištenjem AI usluge za prevođenje [Co-op Translator](https://github.com/Azure/co-op-translator). Iako težimo točnosti, imajte na umu da automatski prijevodi mogu sadržavati pogreške ili netočnosti. Izvorni dokument na izvornom jeziku treba smatrati službenim i autoritativnim izvorom. Za kritične informacije preporučuje se profesionalni ljudski prijevod. Ne snosimo odgovornost za bilo kakve nesporazume ili pogrešna tumačenja koja proizlaze iz korištenja ovog prijevoda.