<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f0ce2d470f3efad6f8c7df376f416a4b",
  "translation_date": "2025-07-12T07:36:25+00:00",
  "source_file": "00-course-setup/AzureSearch.md",
  "language_code": "it"
}
-->
# Guida all'installazione di Azure AI Search

Questa guida ti aiuterà a configurare Azure AI Search utilizzando il portale di Azure. Segui i passaggi seguenti per creare e configurare il tuo servizio Azure AI Search.

## Prerequisiti

Prima di iniziare, assicurati di avere quanto segue:

- Un abbonamento Azure. Se non hai un abbonamento Azure, puoi creare un account gratuito su [Azure Free Account](https://azure.microsoft.com/free/?wt.mc_id=studentamb_258691).

## Passo 1: Crea un servizio Azure AI Search

1. Accedi al [portale di Azure](https://portal.azure.com/?wt.mc_id=studentamb_258691).
2. Nel pannello di navigazione a sinistra, clicca su **Crea una risorsa**.
3. Nella casella di ricerca, digita "Azure AI Search" e seleziona **Azure AI Search** dall'elenco dei risultati.
4. Clicca sul pulsante **Crea**.
5. Nella scheda **Basi**, inserisci le seguenti informazioni:
   - **Subscription**: Seleziona il tuo abbonamento Azure.
   - **Resource group**: Crea un nuovo gruppo di risorse o seleziona uno esistente.
   - **Resource name**: Inserisci un nome univoco per il tuo servizio di ricerca.
   - **Region**: Seleziona la regione più vicina ai tuoi utenti.
   - **Pricing tier**: Scegli un livello di prezzo che soddisfi le tue esigenze. Puoi iniziare con il livello Free per i test.
6. Clicca su **Review + create**.
7. Controlla le impostazioni e clicca su **Create** per creare il servizio di ricerca.

## Passo 2: Inizia a usare Azure AI Search

1. Una volta completata la distribuzione, vai al tuo servizio di ricerca nel portale di Azure.
2. Nella pagina panoramica del servizio di ricerca, clicca sul pulsante **Quickstart**.
3. Segui i passaggi della guida Quickstart per creare un indice, caricare i dati ed eseguire una query di ricerca.

### Crea un indice

1. Nella guida Quickstart, clicca su **Create an index**.
2. Definisci lo schema dell'indice specificando i campi e i loro attributi (ad esempio, tipo di dato, ricercabile, filtrabile).
3. Clicca su **Create** per creare l'indice.

### Carica i dati

1. Nella guida Quickstart, clicca su **Upload data**.
2. Scegli una fonte dati (ad esempio, Azure Blob Storage, Azure SQL Database) e fornisci i dettagli di connessione necessari.
3. Mappa i campi della fonte dati ai campi dell'indice.
4. Clicca su **Submit** per caricare i dati nell'indice.

### Esegui una query di ricerca

1. Nella guida Quickstart, clicca su **Search explorer**.
2. Inserisci una query di ricerca nella casella per testare la funzionalità di ricerca.
3. Esamina i risultati della ricerca e, se necessario, modifica lo schema dell'indice o i dati.

## Passo 3: Usa gli strumenti di Azure AI Search

Azure AI Search si integra con diversi strumenti per migliorare le tue capacità di ricerca. Puoi utilizzare Azure CLI, Python SDK e altri strumenti per configurazioni e operazioni avanzate.

### Uso di Azure CLI

1. Installa Azure CLI seguendo le istruzioni su [Install Azure CLI](https://learn.microsoft.com/en-us/cli/azure/install-azure-cli?wt.mc_id=studentamb_258691).
2. Accedi ad Azure CLI usando il comando:
   ```bash
   az login
   ```
3. Crea un nuovo servizio di ricerca usando Azure CLI:
   ```bash
   az search service create --resource-group <resource-group> --name <service-name> --sku Free
   ```
4. Crea un indice usando Azure CLI:
   ```bash
   az search index create --service-name <service-name> --name <index-name> --fields "field1:type, field2:type"
   ```

### Uso del Python SDK

1. Installa la libreria client Azure Cognitive Search per Python:
   ```bash
   pip install azure-search-documents
   ```
2. Usa il seguente codice Python per creare un indice e caricare documenti:
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

Per informazioni più dettagliate, consulta la documentazione seguente:

- [Create an Azure Cognitive Search service](https://learn.microsoft.com/en-us/azure/search/search-create-service-portal?wt.mc_id=studentamb_258691)
- [Get started with Azure Cognitive Search](https://learn.microsoft.com/en-us/azure/search/search-get-started-portal?wt.mc_id=studentamb_258691)
- [Azure AI Search Tools](https://learn.microsoft.com/en-us/azure/ai-services/agents/how-to/tools/azure-ai-search?tabs=azurecli%2Cpython&pivots=code-examples?wt.mc_id=studentamb_258691)

## Conclusione

Hai configurato con successo Azure AI Search utilizzando il portale di Azure e gli strumenti integrati. Ora puoi esplorare funzionalità e capacità più avanzate di Azure AI Search per migliorare le tue soluzioni di ricerca.

Per ulteriore assistenza, visita la [documentazione di Azure Cognitive Search](https://learn.microsoft.com/en-us/azure/search/?wt.mc_id=studentamb_258691).

**Disclaimer**:  
Questo documento è stato tradotto utilizzando il servizio di traduzione automatica [Co-op Translator](https://github.com/Azure/co-op-translator). Pur impegnandoci per garantire l’accuratezza, si prega di notare che le traduzioni automatiche possono contenere errori o imprecisioni. Il documento originale nella sua lingua nativa deve essere considerato la fonte autorevole. Per informazioni critiche, si raccomanda una traduzione professionale effettuata da un umano. Non ci assumiamo alcuna responsabilità per eventuali malintesi o interpretazioni errate derivanti dall’uso di questa traduzione.