<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "11e38db0898a788612b917e329dcdb5b",
  "translation_date": "2025-11-07T08:35:28+00:00",
  "source_file": "00-course-setup/AzureSearch.md",
  "language_code": "it"
}
-->
# Guida alla configurazione di Azure AI Search

Questa guida ti aiuterà a configurare Azure AI Search utilizzando il portale di Azure. Segui i passaggi qui sotto per creare e configurare il tuo servizio Azure AI Search.

## Prerequisiti

Prima di iniziare, assicurati di avere quanto segue:

- Un abbonamento Azure. Se non hai un abbonamento Azure, puoi creare un account gratuito su [Azure Free Account](https://azure.microsoft.com/free/?wt.mc_id=studentamb_258691).

## Passaggio 1: Creare un account di archiviazione Azure

1. Segui queste istruzioni, [Creare un account di archiviazione Azure](https://learn.microsoft.com/azure/storage/common/storage-account-create?tabs=azure-portal), per creare un nuovo account di archiviazione Azure.
   **NOTA**: Assicurati che il tipo di account di archiviazione sia Standard General Purpose V2.

## Passaggio 2: Creare un servizio Azure AI Search

1. Accedi al [portale di Azure](https://portal.azure.com/?wt.mc_id=studentamb_258691).
2. Nel pannello di navigazione a sinistra, clicca su **Crea una risorsa**.
3. Nella casella di ricerca, digita "Azure AI Search" e seleziona **Azure AI Search** dall'elenco dei risultati.
4. Clicca sul pulsante **Crea**.
5. Nella scheda **Informazioni di base**, fornisci le seguenti informazioni:
   - **Abbonamento**: Seleziona il tuo abbonamento Azure.
   - **Gruppo di risorse**: Crea un nuovo gruppo di risorse o selezionane uno esistente.
   - **Nome risorsa**: Inserisci un nome univoco per il tuo servizio di ricerca.
   - **Regione**: Seleziona la regione più vicina ai tuoi utenti.
   - **Livello di prezzo**: Scegli un livello di prezzo che soddisfi le tue esigenze. Puoi iniziare con il livello gratuito per i test.
6. Clicca su **Rivedi + crea**.
7. Rivedi le impostazioni e clicca su **Crea** per creare il servizio di ricerca.

## Passaggio 3: Iniziare con Azure AI Search

1. Una volta completata la distribuzione, vai al tuo servizio di ricerca nel portale di Azure.
2. Nel pannello di panoramica del servizio di ricerca, copia l'URL. Dovrebbe essere simile a `https://<service-name>.search.windows.net`.
3. Nel pannello Impostazioni > Chiavi, copia la chiave di query.
4. Segui i passaggi nella pagina [Guida rapida](https://learn.microsoft.com/azure/search/search-get-started-portal?pivots=import-data-new) per creare un indice, caricare dati ed eseguire una query di ricerca.

## Passaggio 4: Utilizzare gli strumenti di Azure AI Search

Azure AI Search si integra con vari strumenti per migliorare le tue capacità di ricerca. Puoi utilizzare Azure CLI, Python SDK, .NET SDK e altri strumenti per configurazioni e operazioni avanzate.

### Utilizzo di Azure CLI

1. Installa Azure CLI seguendo le istruzioni su [Installare Azure CLI](https://learn.microsoft.com/cli/azure/install-azure-cli?wt.mc_id=studentamb_258691).
2. Accedi ad Azure CLI utilizzando il comando:

   ```bash
   az login
   ```

3. Memorizza sia l'endpoint che la chiave API per l'istanza di Azure AI Search nelle variabili di ambiente.

    ```bash
    # zsh/bash
    export AZURE_SEARCH_SERVICE_ENDPOINT=$(az search service show -g <resource-group> -n <service-name> --query "endpoint" -o tsv)
    export AZURE_SEARCH_API_KEY=$(az search service admin-key list -g <resource-group> --search-service-name <service-name> --query "primaryKey" -o tsv)
    ```

    ```powershell
    # PowerShell
    $env:AZURE_SEARCH_SERVICE_ENDPOINT = az search service show -g <resource-group> -n <service-name> --query "endpoint" -o tsv
    $env:AZURE_SEARCH_API_KEY = $(az search service admin-key list -g <resource-group> --search-service-name <service-name> --query "primaryKey" -o tsv)
    ```

### Utilizzo di Python SDK

1. Installa la libreria client Azure Cognitive Search per Python:

   ```bash
   pip install azure-search-documents
   ```

2. Utilizza il seguente codice Python per creare un indice e caricare documenti:

    ```python
    import os
    from azure.core.credentials import AzureKeyCredential
    from azure.search.documents import SearchClient
    from azure.search.documents.indexes import SearchIndexClient
    from azure.search.documents.indexes.models import SearchIndex, SimpleField, edm

    service_endpoint = os.getenv("AZURE_SEARCH_SERVICE_ENDPOINT")
    api_key = os.getenv("AZURE_SEARCH_API_KEY")
    index_name = "sample-index"

    credential = AzureKeyCredential(api_key)
    index_client = SearchIndexClient(service_endpoint, credential)

    fields = [
        SimpleField(name="id", type=edm.String, key=True),
        SimpleField(name="content", type=edm.String, searchable=True),
    ]

    index = SearchIndex(name=index_name, fields=fields)

    index_client.create_index(index)

    search_client = SearchClient(service_endpoint, index_name, credential)

    documents = [
        {"id": "1", "content": "Hello world"},
        {"id": "2", "content": "Azure Cognitive Search"}
    ]

    search_client.upload_documents(documents)
    ```

### Utilizzo di .NET SDK

1. Esegui il seguente comando per creare un indice e caricare documenti:

    ```bash
    dotnet run ./AzureSearch.cs
    ```

2. Ecco il codice .NET di `AzureSearch.cs`:

    ```csharp
    #:package Azure.Search.Documents@11.*
    #:property PublishAot=false

    using Azure;
    using Azure.Search.Documents;
    using Azure.Search.Documents.Indexes;
    using Azure.Search.Documents.Indexes.Models;

    var serviceEndpoint = new Uri(Environment.GetEnvironmentVariable("AZURE_SEARCH_SERVICE_ENDPOINT")!);
    var apiKey = Environment.GetEnvironmentVariable("AZURE_SEARCH_API_KEY")!;
    var indexName = "sample-index";

    var credential = new AzureKeyCredential(apiKey);
    var indexClient = new SearchIndexClient(serviceEndpoint, credential);

    var fields = new List<SearchField>()
    {
        new SimpleField("id", SearchFieldDataType.String) { IsKey = true },
        new SearchableField("content")
    };

    var index = new SearchIndex(name: indexName, fields: fields);

    var response = await indexClient.CreateOrUpdateIndexAsync(index);
    Console.WriteLine($"Index '{response.Value.Name}' ready.");

    var searchClient = new SearchClient(serviceEndpoint, indexName, credential);

    var documents = new[]
    {
        new { id = "1", content = "Hello world" },
        new { id = "2", content = "Azure Cognitive Search" }
    };

    var result = await searchClient.UploadDocumentsAsync(documents);
    Console.WriteLine($"Uploaded {result.Value.Results.Count} documents to index '{response.Value.Name}'.");
    ```

Per ulteriori informazioni dettagliate, consulta la seguente documentazione:

- [Creare un servizio Azure Cognitive Search](https://learn.microsoft.com/azure/search/search-create-service-portal?wt.mc_id=studentamb_258691)
- [Iniziare con Azure Cognitive Search](https://learn.microsoft.com/azure/search/search-get-started-portal?wt.mc_id=studentamb_258691)
- [Strumenti di Azure AI Search](https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-ai-search?tabs=azurecli%2Cpython&pivots=code-examples?wt.mc_id=studentamb_258691)

## Conclusione

Hai configurato con successo Azure AI Search utilizzando il portale di Azure e gli strumenti integrati. Ora puoi esplorare funzionalità e capacità avanzate di Azure AI Search per migliorare le tue soluzioni di ricerca.

Per ulteriore assistenza, visita la [documentazione di Azure Cognitive Search](https://learn.microsoft.com/azure/search/?wt.mc_id=studentamb_258691).

---

**Disclaimer**:  
Questo documento è stato tradotto utilizzando il servizio di traduzione AI [Co-op Translator](https://github.com/Azure/co-op-translator). Sebbene ci impegniamo per garantire l'accuratezza, si prega di notare che le traduzioni automatiche possono contenere errori o imprecisioni. Il documento originale nella sua lingua nativa dovrebbe essere considerato la fonte autorevole. Per informazioni critiche, si raccomanda una traduzione professionale umana. Non siamo responsabili per eventuali incomprensioni o interpretazioni errate derivanti dall'uso di questa traduzione.