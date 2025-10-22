<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f0ce2d470f3efad6f8c7df376f416a4b",
  "translation_date": "2025-07-12T07:39:57+00:00",
  "source_file": "00-course-setup/AzureSearch.md",
  "language_code": "ro"
}
-->
# Ghid de configurare Azure AI Search

Acest ghid te va ajuta să configurezi Azure AI Search folosind portalul Azure. Urmează pașii de mai jos pentru a crea și configura serviciul tău Azure AI Search.

## Cerințe preliminare

Înainte de a începe, asigură-te că ai următoarele:

- Un abonament Azure. Dacă nu ai un abonament Azure, poți crea un cont gratuit la [Azure Free Account](https://azure.microsoft.com/free/?wt.mc_id=studentamb_258691).

## Pasul 1: Creează un serviciu Azure AI Search

1. Conectează-te la [portalul Azure](https://portal.azure.com/?wt.mc_id=studentamb_258691).
2. În panoul de navigare din stânga, dă clic pe **Create a resource**.
3. În caseta de căutare, tastează „Azure AI Search” și selectează **Azure AI Search** din lista de rezultate.
4. Apasă butonul **Create**.
5. În fila **Basics**, completează următoarele informații:
   - **Subscription**: Selectează abonamentul tău Azure.
   - **Resource group**: Creează un grup de resurse nou sau selectează unul existent.
   - **Resource name**: Introdu un nume unic pentru serviciul tău de căutare.
   - **Region**: Alege regiunea cea mai apropiată de utilizatorii tăi.
   - **Pricing tier**: Alege un nivel de tarifare care să corespundă nevoilor tale. Poți începe cu nivelul Free pentru testare.
6. Apasă pe **Review + create**.
7. Verifică setările și apasă **Create** pentru a crea serviciul de căutare.

## Pasul 2: Începe să folosești Azure AI Search

1. După ce implementarea este finalizată, navighează la serviciul tău de căutare în portalul Azure.
2. În pagina de prezentare a serviciului de căutare, apasă pe butonul **Quickstart**.
3. Urmează pașii din ghidul Quickstart pentru a crea un index, a încărca date și a efectua o interogare de căutare.

### Creează un index

1. În ghidul Quickstart, apasă pe **Create an index**.
2. Definește schema indexului specificând câmpurile și atributele lor (de exemplu, tipul de date, dacă sunt căutabile, filtrabile).
3. Apasă **Create** pentru a crea indexul.

### Încarcă date

1. În ghidul Quickstart, apasă pe **Upload data**.
2. Alege o sursă de date (de exemplu, Azure Blob Storage, Azure SQL Database) și furnizează detaliile necesare de conectare.
3. Mapează câmpurile sursei de date la câmpurile indexului.
4. Apasă **Submit** pentru a încărca datele în index.

### Efectuează o interogare de căutare

1. În ghidul Quickstart, apasă pe **Search explorer**.
2. Introdu o interogare de căutare în caseta de căutare pentru a testa funcționalitatea.
3. Analizează rezultatele căutării și ajustează schema indexului sau datele după necesitate.

## Pasul 3: Folosește uneltele Azure AI Search

Azure AI Search se integrează cu diverse unelte pentru a-ți îmbunătăți capabilitățile de căutare. Poți folosi Azure CLI, Python SDK și alte unelte pentru configurări și operațiuni avansate.

### Folosirea Azure CLI

1. Instalează Azure CLI urmând instrucțiunile de la [Install Azure CLI](https://learn.microsoft.com/en-us/cli/azure/install-azure-cli?wt.mc_id=studentamb_258691).
2. Conectează-te la Azure CLI folosind comanda:
   ```bash
   az login
   ```
3. Creează un serviciu de căutare nou folosind Azure CLI:
   ```bash
   az search service create --resource-group <resource-group> --name <service-name> --sku Free
   ```
4. Creează un index folosind Azure CLI:
   ```bash
   az search index create --service-name <service-name> --name <index-name> --fields "field1:type, field2:type"
   ```

### Folosirea Python SDK

1. Instalează biblioteca client Azure Cognitive Search pentru Python:
   ```bash
   pip install azure-search-documents
   ```
2. Folosește următorul cod Python pentru a crea un index și a încărca documente:
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

Pentru informații mai detaliate, consultă următoarea documentație:

- [Create an Azure Cognitive Search service](https://learn.microsoft.com/en-us/azure/search/search-create-service-portal?wt.mc_id=studentamb_258691)
- [Get started with Azure Cognitive Search](https://learn.microsoft.com/en-us/azure/search/search-get-started-portal?wt.mc_id=studentamb_258691)
- [Azure AI Search Tools](https://learn.microsoft.com/en-us/azure/ai-services/agents/how-to/tools/azure-ai-search?tabs=azurecli%2Cpython&pivots=code-examples?wt.mc_id=studentamb_258691)

## Concluzie

Ai configurat cu succes Azure AI Search folosind portalul Azure și uneltele integrate. Acum poți explora funcționalități și capabilități mai avansate ale Azure AI Search pentru a-ți îmbunătăți soluțiile de căutare.

Pentru asistență suplimentară, vizitează [documentația Azure Cognitive Search](https://learn.microsoft.com/en-us/azure/search/?wt.mc_id=studentamb_258691).

**Declinare de responsabilitate**:  
Acest document a fost tradus folosind serviciul de traducere AI [Co-op Translator](https://github.com/Azure/co-op-translator). Deși ne străduim pentru acuratețe, vă rugăm să rețineți că traducerile automate pot conține erori sau inexactități. Documentul original în limba sa nativă trebuie considerat sursa autorizată. Pentru informații critice, se recomandă traducerea profesională realizată de un specialist uman. Nu ne asumăm răspunderea pentru eventualele neînțelegeri sau interpretări greșite rezultate din utilizarea acestei traduceri.