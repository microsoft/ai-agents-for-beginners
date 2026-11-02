# Ghid de configurare Azure AI Search

Acest ghid te va ajuta să configurezi Azure AI Search folosind portalul Azure. Urmează pașii de mai jos pentru a crea și configura serviciul tău Azure AI Search.

## Cerințe preliminare

Înainte de a începe, asigură-te că ai următoarele:

- Un abonament Azure. Dacă nu ai un abonament Azure, poți crea un cont gratuit la [Azure Free Account](https://azure.microsoft.com/free/?wt.mc_id=studentamb_258691).

## Pasul 1: Creează un cont de stocare Azure

1. Urmează această instrucțiune, [Create an Azure storage account](https://learn.microsoft.com/azure/storage/common/storage-account-create?tabs=azure-portal), pentru a crea un nou cont de stocare Azure.
   **NOTĂ**: Asigură-te că tipul contului de stocare este Standard General Purpose V2.

## Pasul 2: Creează un serviciu Azure AI Search

1. Conectează-te la [portalul Azure](https://portal.azure.com/?wt.mc_id=studentamb_258691).
2. În panoul de navigare din stânga, dă clic pe **Create a resource**.
3. În caseta de căutare, tastează „Azure AI Search” și selectează **Azure AI Search** din lista rezultatelor.
4. Apasă butonul **Create**.
5. În fila **Basics**, furnizează următoarele informații:
   - **Subscription**: Selectează abonamentul Azure.
   - **Resource group**: Creează un grup de resurse nou sau selectează unul existent.
   - **Resource name**: Introdu un nume unic pentru serviciul de căutare.
   - **Region**: Selectează regiunea cea mai apropiată de utilizatorii tăi.
   - **Pricing tier**: Alege un nivel de preț care se potrivește cerințelor tale. Poți începe cu nivelul Free pentru testare.
6. Apasă pe **Review + create**.
7. Verifică setările și apasă pe **Create** pentru a crea serviciul de căutare.

## Pasul 3: Începe să folosești Azure AI Search

1. După ce implementarea se finalizează, navighează la serviciul tău de căutare în portalul Azure.
2. În panoul de prezentare al serviciului de căutare, copiază URL-ul. Acesta ar trebui să arate ca `https://<service-name>.search.windows.net`.
3. **(Recomandat)** Activează accesul fără cheie cu Microsoft Entra ID (RBAC) așa cum este arătat în Pasul 4 de mai jos — nu este nevoie de cheie. Exemplele din acest ghid creează/actualizează indexuri și încarcă documente, pentru care sunt necesare rolurile **Search Service Contributor** și **Search Index Data Contributor** (sau, pentru autentificarea bazată pe cheie, **cheia de administrator primară** — nu cheia de interogare). Doar dacă nu poți utiliza RBAC, deschide panoul **Settings > Keys** și copiază **cheia de administrator primară**.
4. Urmează pașii din pagina [Quickstart guide](https://learn.microsoft.com/azure/search/search-get-started-portal?pivots=import-data-new) pentru a crea un index, a încărca date și a efectua o căutare.

## Pasul 4: Folosește uneltele Azure AI Search

Azure AI Search se integrează cu diverse unelte pentru a îmbunătăți capabilitățile de căutare. Poți folosi Azure CLI, SDK-ul Python, SDK-ul .NET și alte unelte pentru configurații și operațiuni avansate.

### Folosirea Azure CLI

1. Instalează Azure CLI urmând instrucțiunile de la [Install Azure CLI](https://learn.microsoft.com/cli/azure/install-azure-cli?wt.mc_id=studentamb_258691).
2. Conectează-te la Azure CLI folosind comanda:

   ```bash
   az login
   ```
3. **(Recomandat) Activează accesul fără cheie cu Microsoft Entra ID (RBAC):**

    ```bash
    az search service update --name <service-name> --resource-group <resource-group> --auth-options aadOrApiKey
    az role assignment create --assignee <your-user-or-principal-id> --role "Search Service Contributor" --scope $(az search service show -g <resource-group> -n <service-name> --query id -o tsv)
    az role assignment create --assignee <your-user-or-principal-id> --role "Search Index Data Contributor" --scope $(az search service show -g <resource-group> -n <service-name> --query id -o tsv)
    # az search service show has no "endpoint" field; build the URL from the service name.
    export AZURE_SEARCH_SERVICE_ENDPOINT="https://<service-name>.search.windows.net"
    ```

    Cu RBAC activat, exemplele de SDK Python și .NET de mai jos se autentifică cu `DefaultAzureCredential`, care folosește sesiunea ta `az login` în timpul dezvoltării locale — nu este nevoie de cheia de administrator. Vezi [Connect to Azure AI Search using roles](https://learn.microsoft.com/azure/search/search-security-rbac).

4. **(Alternativ) Autentificare pe bază de cheie** — doar dacă nu poți folosi RBAC, stochează și cheia de administrator:

#### Stochează atât endpoint-ul cât și cheia API pentru instanța Azure AI Search în variabilele de mediu.

   * **zsh / bash**
     ```bash
     # az search service show has no "endpoint" field; build the URL from the service name.
     export AZURE_SEARCH_SERVICE_ENDPOINT="https://<service-name>.search.windows.net"
     export AZURE_SEARCH_API_KEY=$(az search admin-key show -g <resource-group> --service-name <service-name> --query "primaryKey" -o tsv)
     ```

   * **PowerShell**
     ```powershell
     # az search service show has no "endpoint" field; build the URL from the service name.
     $env:AZURE_SEARCH_SERVICE_ENDPOINT = "https://<service-name>.search.windows.net"
     $env:AZURE_SEARCH_API_KEY = $(az search admin-key show -g <resource-group> --service-name <service-name> --query "primaryKey" -o tsv)
     ```

### Folosirea SDK-ului Python

1. Instalează biblioteca client Azure Cognitive Search și Azure Identity pentru Python:

   ```bash
   pip install azure-search-documents azure-identity
   ```

2. Folosește următorul cod Python pentru a crea un index și a încărca documente:

    ```python
    import os
    from azure.identity import DefaultAzureCredential
    from azure.search.documents import SearchClient
    from azure.search.documents.indexes import SearchIndexClient
    from azure.search.documents.indexes.models import SearchIndex, SimpleField, edm

    service_endpoint = os.getenv("AZURE_SEARCH_SERVICE_ENDPOINT")
    index_name = "sample-index"

    # Keyless (recommended): uses your `az login` identity via Entra ID RBAC.
    # Requires the "Search Service Contributor" and "Search Index Data Contributor" roles.
    credential = DefaultAzureCredential()
    # Fallback (key-based auth):
    # from azure.core.credentials import AzureKeyCredential
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

### Folosirea SDK-ului .NET

1. Rulează următoarea comandă pentru a crea un index și a încărca documente:

    ```bash
    dotnet run ./AzureSearch.cs
    ```

    Exemplul .NET de mai jos folosește `DefaultAzureCredential`, care poate utiliza logarea ta Azure CLI din `az login` în timpul dezvoltării locale.

2. Iată codul .NET al `AzureSearch.cs`:

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

Pentru informații mai detaliate, consultă următoarea documentație:

- [Create an Azure Cognitive Search service](https://learn.microsoft.com/azure/search/search-create-service-portal?wt.mc_id=studentamb_258691)
- [Get started with Azure Cognitive Search](https://learn.microsoft.com/azure/search/search-get-started-portal?wt.mc_id=studentamb_258691)
- [Azure AI Search Tools](https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-ai-search?tabs=azurecli%2Cpython&pivots=code-examples?wt.mc_id=studentamb_258691)

## Concluzie

Ai configurat cu succes Azure AI Search folosind portalul Azure și uneltele integrate. Acum poți explora funcții și capabilități mai avansate ale Azure AI Search pentru a îmbunătăți soluțiile tale de căutare.

Pentru asistență suplimentară, vizitează documentația [Azure Cognitive Search](https://learn.microsoft.com/azure/search/?wt.mc_id=studentamb_258691).

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Declinare a responsabilității**:
Acest document a fost tradus folosind serviciul de traducere AI [Co-op Translator](https://github.com/Azure/co-op-translator). În timp ce ne străduim pentru acuratețe, vă rugăm să rețineți că traducerile automate pot conține erori sau inexactități. Documentul original în limba sa nativă trebuie considerat sursa autorizată. Pentru informații critice, se recomandă traducerea profesională realizată de un om. Nu ne asumăm responsabilitatea pentru eventualele neînțelegeri sau interpretări greșite care decurg din utilizarea acestei traduceri.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->