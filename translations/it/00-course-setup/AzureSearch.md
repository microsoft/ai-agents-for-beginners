# Guida all'Installazione di Azure AI Search

Questa guida ti aiuterà a configurare Azure AI Search utilizzando il portale Azure. Segui i passaggi seguenti per creare e configurare il tuo servizio Azure AI Search.

## Prerequisiti

Prima di iniziare, assicurati di avere quanto segue:

- Una sottoscrizione Azure. Se non hai una sottoscrizione Azure, puoi crearne una gratuita su [Azure Free Account](https://azure.microsoft.com/free/?wt.mc_id=studentamb_258691).

## Passo 1: Crea un Account di Archiviazione Azure

1. Segui questa istruzione, [Create an Azure storage account](https://learn.microsoft.com/azure/storage/common/storage-account-create?tabs=azure-portal), per creare un nuovo Account di Archiviazione Azure.
   **NOTA**: Assicurati che il tipo di Account di Archiviazione sia Standard General Purpose V2.

## Passo 2: Crea un Servizio Azure AI Search

1. Accedi al [portale Azure](https://portal.azure.com/?wt.mc_id=studentamb_258691).
2. Nel pannello di navigazione a sinistra, clicca su **Crea una risorsa**.
3. Nella casella di ricerca, digita "Azure AI Search" e seleziona **Azure AI Search** dalla lista dei risultati.
4. Clicca sul pulsante **Crea**.
5. Nella scheda **Elementi base**, fornisci le seguenti informazioni:
   - **Sottoscrizione**: Seleziona la tua sottoscrizione Azure.
   - **Gruppo di risorse**: Crea un nuovo gruppo di risorse o seleziona uno esistente.
   - **Nome della risorsa**: Inserisci un nome univoco per il tuo servizio di ricerca.
   - **Regione**: Seleziona la regione più vicina ai tuoi utenti.
   - **Livello di prezzo**: Scegli un livello di prezzo che soddisfi le tue esigenze. Puoi iniziare con il livello Gratuito per i test.
6. Clicca su **Verifica + crea**.
7. Rivedi le impostazioni e clicca su **Crea** per creare il servizio di ricerca.

## Passo 3: Inizia con Azure AI Search

1. Una volta completata la distribuzione, accedi al tuo servizio di ricerca nel portale Azure.
2. Nel pannello panoramica del servizio di ricerca, copia l'URL. Dovrebbe essere simile a `https://<service-name>.search.windows.net`.
3. **(Raccomandato)** Abilita l'accesso senza chiave con Microsoft Entra ID (RBAC) come mostrato nel Passo 4 qui sotto — non è necessaria alcuna chiave. Gli esempi in questa guida creano/aggiornano indici e caricano documenti, il che richiede i ruoli **Search Service Contributor** e **Search Index Data Contributor** (oppure, per l'autenticazione basata su chiave, la **chiave amministratore primaria** — non la chiave di query). Solo se non puoi usare RBAC, apri il pannello **Impostazioni > Chiavi** e copia la **chiave amministratore primaria**.
4. Segui i passaggi nella pagina della [Guida introduttiva](https://learn.microsoft.com/azure/search/search-get-started-portal?pivots=import-data-new) per creare un indice, caricare dati ed eseguire una ricerca.

## Passo 4: Usa gli Strumenti di Azure AI Search

Azure AI Search si integra con vari strumenti per migliorare le capacità di ricerca. Puoi usare Azure CLI, SDK Python, SDK .NET e altri strumenti per configurazioni e operazioni avanzate.

### Uso di Azure CLI

1. Installa Azure CLI seguendo le istruzioni su [Install Azure CLI](https://learn.microsoft.com/cli/azure/install-azure-cli?wt.mc_id=studentamb_258691).
2. Accedi ad Azure CLI usando il comando:

   ```bash
   az login
   ```
3. **(Raccomandato) Abilita l'accesso senza chiave con Microsoft Entra ID (RBAC):**

    ```bash
    az search service update --name <service-name> --resource-group <resource-group> --auth-options aadOrApiKey
    az role assignment create --assignee <your-user-or-principal-id> --role "Search Service Contributor" --scope $(az search service show -g <resource-group> -n <service-name> --query id -o tsv)
    az role assignment create --assignee <your-user-or-principal-id> --role "Search Index Data Contributor" --scope $(az search service show -g <resource-group> -n <service-name> --query id -o tsv)
    # az search service show non ha il campo "endpoint"; costruisci l'URL dal nome del servizio.
    export AZURE_SEARCH_SERVICE_ENDPOINT="https://<service-name>.search.windows.net"
    ```

    Con RBAC abilitato, gli esempi di SDK Python e .NET qui sotto si autenticano con `DefaultAzureCredential`, che usa la tua sessione `az login` durante lo sviluppo locale — non è necessaria la chiave amministratore. Vedi [Connettersi a Azure AI Search usando i ruoli](https://learn.microsoft.com/azure/search/search-security-rbac).

4. **(Alternativa) Autenticazione con chiave** — solo se non puoi usare RBAC, memorizza anche la chiave amministratore:

#### Memorizza sia l'endpoint sia la chiave API dell'istanza Azure AI Search nelle variabili d'ambiente.

    ```bash
    # zsh/bash
    # az search service show non ha il campo "endpoint"; costruisci l'URL dal nome del servizio.
    export AZURE_SEARCH_SERVICE_ENDPOINT="https://<service-name>.search.windows.net"
    export AZURE_SEARCH_API_KEY=$(az search admin-key show -g <resource-group> --service-name <service-name> --query "primaryKey" -o tsv)
    ```

    ```powershell
    # PowerShell
    # az search service show non ha il campo "endpoint"; costruisci l'URL dal nome del servizio.
    $env:AZURE_SEARCH_SERVICE_ENDPOINT = "https://<service-name>.search.windows.net"
    $env:AZURE_SEARCH_API_KEY = $(az search admin-key show -g <resource-group> --service-name <service-name> --query "primaryKey" -o tsv)
    ```

### Uso dell'SDK Python

1. Installa la libreria client Azure Cognitive Search e Azure Identity per Python:

   ```bash
   pip install azure-search-documents azure-identity
   ```

2. Usa il seguente codice Python per creare un indice e caricare documenti:

    ```python
    import os
    from azure.identity import DefaultAzureCredential
    from azure.search.documents import SearchClient
    from azure.search.documents.indexes import SearchIndexClient
    from azure.search.documents.indexes.models import SearchIndex, SimpleField, edm

    service_endpoint = os.getenv("AZURE_SEARCH_SERVICE_ENDPOINT")
    index_name = "sample-index"

    # Senza chiave (consigliato): utilizza la tua identità `az login` tramite Entra ID RBAC.
    # Richiede i ruoli "Search Service Contributor" e "Search Index Data Contributor".
    credential = DefaultAzureCredential()
    # Metodo alternativo (autenticazione basata su chiave):
    # da azure.core.credentials importa AzureKeyCredential
    # credential = AzureKeyCredential(os.getenv("AZURE_SEARCH_API_KEY"))
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

### Uso dell'SDK .NET

1. Esegui il seguente comando per creare un indice e caricare documenti:

    ```bash
    dotnet run ./AzureSearch.cs
    ```

    L'esempio .NET qui sotto usa `DefaultAzureCredential`, il quale può utilizzare il tuo accesso Azure CLI da `az login` durante lo sviluppo locale.

2. Ecco il codice .NET di `AzureSearch.cs`:

    ```csharp
    #:package Azure.Search.Documents@11.*
    #:package Azure.Identity@1.21.0
    #:property PublishAot=false

    using Azure;
    using Azure.Identity;
    using Azure.Search.Documents;
    using Azure.Search.Documents.Indexes;
    using Azure.Search.Documents.Indexes.Models;

    var serviceEndpoint = new Uri(Environment.GetEnvironmentVariable("AZURE_SEARCH_SERVICE_ENDPOINT")!);
    var indexName = "sample-index";

    // Keyless (recommended): uses your `az login` identity via Entra ID RBAC.
    // Requires the "Search Service Contributor" and "Search Index Data Contributor" roles.
    var credential = new DefaultAzureCredential();
    // Fallback (key-based auth): the `using Azure;` directive above already imports
    // AzureKeyCredential; replace the credential line above with:
    // var credential = new AzureKeyCredential(Environment.GetEnvironmentVariable("AZURE_SEARCH_API_KEY")!);
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

Per informazioni più dettagliate, consulta la seguente documentazione:

- [Crea un servizio Azure Cognitive Search](https://learn.microsoft.com/azure/search/search-create-service-portal?wt.mc_id=studentamb_258691)
- [Inizia con Azure Cognitive Search](https://learn.microsoft.com/azure/search/search-get-started-portal?wt.mc_id=studentamb_258691)
- [Strumenti Azure AI Search](https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-ai-search?tabs=azurecli%2Cpython&pivots=code-examples?wt.mc_id=studentamb_258691)

## Conclusione

Hai configurato correttamente Azure AI Search utilizzando il portale Azure e gli strumenti integrati. Ora puoi esplorare funzionalità e capacità più avanzate di Azure AI Search per migliorare le tue soluzioni di ricerca.

Per ulteriore assistenza, visita la [documentazione di Azure Cognitive Search](https://learn.microsoft.com/azure/search/?wt.mc_id=studentamb_258691).

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:
Questo documento è stato tradotto utilizzando il servizio di traduzione AI [Co-op Translator](https://github.com/Azure/co-op-translator). Sebbene ci impegniamo per garantire la precisione, si prega di notare che le traduzioni automatizzate possono contenere errori o imprecisioni. Il documento originale nella sua lingua nativa deve essere considerato la fonte autorevole. Per informazioni critiche, si raccomanda una traduzione professionale effettuata da un essere umano. Non siamo responsabili per eventuali malintesi o interpretazioni errate derivanti dall’uso di questa traduzione.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->