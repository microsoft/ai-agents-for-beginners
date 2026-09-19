# Ghid de configurare Azure AI Search

Acest ghid vă va ajuta să configurați Azure AI Search folosind portalul Azure. Urmați pașii de mai jos pentru a crea și configura serviciul dvs. Azure AI Search.

## Cerințe preliminare

Înainte de a începe, asigurați-vă că aveți următoarele:

- Un abonament Azure. Dacă nu aveți un abonament Azure, puteți crea un cont gratuit la [Azure Free Account](https://azure.microsoft.com/free/?wt.mc_id=studentamb_258691).

## Pasul 1: Creați un cont de stocare Azure

1. Urmați această instrucțiune, [Create an Azure storage account](https://learn.microsoft.com/azure/storage/common/storage-account-create?tabs=azure-portal), pentru a crea un nou cont de stocare Azure.
   **NOTĂ**: Asigurați-vă că tipul contului de stocare este Standard General Purpose V2.

## Pasul 2: Creați un serviciu Azure AI Search

1. Autentificați-vă în [portalul Azure](https://portal.azure.com/?wt.mc_id=studentamb_258691).
2. În panoul de navigare din stânga, faceți clic pe **Create a resource**.
3. În caseta de căutare, tastați "Azure AI Search" și selectați **Azure AI Search** din lista de rezultate.
4. Faceți clic pe butonul **Create**.
5. În fila **Basics**, furnizați următoarele informații:
   - **Subscription**: Selectați abonamentul dvs. Azure.
   - **Resource group**: Creați un grup de resurse nou sau selectați unul existent.
   - **Resource name**: Introduceți un nume unic pentru serviciul de căutare.
   - **Region**: Selectați regiunea cea mai apropiată de utilizatorii dvs.
   - **Pricing tier**: Alegeți un nivel de tarifare care să corespundă cerințelor dvs. Puteți începe cu nivelul Free pentru testare.
6. Faceți clic pe **Review + create**.
7. Verificați setările și faceți clic pe **Create** pentru a crea serviciul de căutare.

## Pasul 3: Începeți cu Azure AI Search

1. Odată ce implementarea este completă, navigați la serviciul dvs. de căutare în portalul Azure.
2. În panoul de prezentare a serviciului de căutare, copiați URL-ul. Ar trebui să arate ca `https://<service-name>.search.windows.net`.
3. **(Recomandat)** Activați accesul fără cheie cu Microsoft Entra ID (RBAC) așa cum se arată în Pasul 4 de mai jos — nu este necesară o cheie. Exemplele din acest ghid creează/actualizează indici și încarcă documente, ceea ce necesită rolurile **Search Service Contributor** și **Search Index Data Contributor** (sau, în cazul autentificării bazate pe chei, **cheia principală de administrator** — nu cheia de interogare). Doar dacă nu puteți folosi RBAC, deschideți panoul **Settings > Keys** și copiați **cheia principală de administrator**.
4. Urmați pașii din pagina [Quickstart guide](https://learn.microsoft.com/azure/search/search-get-started-portal?pivots=import-data-new) pentru a crea un index, a încărca date și a efectua o căutare.

## Pasul 4: Folosiți instrumentele Azure AI Search

Azure AI Search se integrează cu diverse instrumente pentru a vă îmbunătăți capabilitățile de căutare. Puteți folosi Azure CLI, Python SDK, .NET SDK și alte instrumente pentru configurații și operații avansate.

### Utilizarea Azure CLI

1. Instalați Azure CLI urmând instrucțiunile de la [Install Azure CLI](https://learn.microsoft.com/cli/azure/install-azure-cli?wt.mc_id=studentamb_258691).
2. Autentificați-vă în Azure CLI folosind comanda:

   ```bash
   az login
   ```
3. **(Recomandat) Activați accesul fără cheie cu Microsoft Entra ID (RBAC):**

    ```bash
    az search service update --name <service-name> --resource-group <resource-group> --auth-options aadOrApiKey
    az role assignment create --assignee <your-user-or-principal-id> --role "Search Service Contributor" --scope $(az search service show -g <resource-group> -n <service-name> --query id -o tsv)
    az role assignment create --assignee <your-user-or-principal-id> --role "Search Index Data Contributor" --scope $(az search service show -g <resource-group> -n <service-name> --query id -o tsv)
    # az search service show nu are un câmp "endpoint"; construiește URL-ul din numele serviciului.
    export AZURE_SEARCH_SERVICE_ENDPOINT="https://<service-name>.search.windows.net"
    ```

    Cu RBAC activat, exemplele SDK Python și .NET de mai jos se autentifică cu `DefaultAzureCredential`, care folosește sesiunea dvs. `az login` în timpul dezvoltării locale — nu este nevoie de cheia de administrator. Vedeți [Connect to Azure AI Search using roles](https://learn.microsoft.com/azure/search/search-security-rbac).

4. **(Ca soluție de rezervă) Autentificare bazată pe cheie** — doar dacă nu puteți folosi RBAC, stocați și cheia admin:

#### Stocați atât endpoint-ul, cât și cheia API pentru instanța Azure AI Search în variabilele de mediu.

    ```bash
    # zsh/bash
    # az search service show nu are câmp "endpoint"; construiți URL-ul din numele serviciului.
    export AZURE_SEARCH_SERVICE_ENDPOINT="https://<service-name>.search.windows.net"
    export AZURE_SEARCH_API_KEY=$(az search admin-key show -g <resource-group> --service-name <service-name> --query "primaryKey" -o tsv)
    ```

    ```powershell
    # PowerShell
    # az search service show nu are câmp "endpoint"; construiți URL-ul din numele serviciului.
    $env:AZURE_SEARCH_SERVICE_ENDPOINT = "https://<service-name>.search.windows.net"
    $env:AZURE_SEARCH_API_KEY = $(az search admin-key show -g <resource-group> --service-name <service-name> --query "primaryKey" -o tsv)
    ```

### Utilizarea Python SDK

1. Instalați biblioteca client Azure Cognitive Search și Azure Identity pentru Python:

   ```bash
   pip install azure-search-documents azure-identity
   ```

2. Folosiți următorul cod Python pentru a crea un index și a încărca documente:

    ```python
    import os
    from azure.identity import DefaultAzureCredential
    from azure.search.documents import SearchClient
    from azure.search.documents.indexes import SearchIndexClient
    from azure.search.documents.indexes.models import SearchIndex, SimpleField, edm

    service_endpoint = os.getenv("AZURE_SEARCH_SERVICE_ENDPOINT")
    index_name = "sample-index"

    # Fără cheie (recomandat): folosește identitatea ta `az login` prin Entra ID RBAC.
    # Necesită rolurile „Search Service Contributor” și „Search Index Data Contributor”.
    credential = DefaultAzureCredential()
    # Soluție de rezervă (autentificare pe bază de cheie):
    # din azure.core.credentials import AzureKeyCredential
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

### Utilizarea .NET SDK

1. Rulați următoarea comandă pentru a crea un index și a încărca documente:

    ```bash
    dotnet run ./AzureSearch.cs
    ```

    Exemplul .NET de mai jos folosește `DefaultAzureCredential`, care poate utiliza autentificarea dvs. Azure CLI din `az login` în timpul dezvoltării locale.

2. Iată codul .NET din `AzureSearch.cs`:

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

Pentru informații mai detaliate, consultați următoarea documentație:

- [Creați un serviciu Azure Cognitive Search](https://learn.microsoft.com/azure/search/search-create-service-portal?wt.mc_id=studentamb_258691)
- [Începeți cu Azure Cognitive Search](https://learn.microsoft.com/azure/search/search-get-started-portal?wt.mc_id=studentamb_258691)
- [Instrumente Azure AI Search](https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-ai-search?tabs=azurecli%2Cpython&pivots=code-examples?wt.mc_id=studentamb_258691)

## Concluzie

Ați configurat cu succes Azure AI Search folosind portalul Azure și instrumentele integrate. Acum puteți explora funcții și capabilități mai avansate Azure AI Search pentru a îmbunătăți soluțiile dvs. de căutare.

Pentru asistență suplimentară, vizitați [documentația Azure Cognitive Search](https://learn.microsoft.com/azure/search/?wt.mc_id=studentamb_258691).

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Declinare a responsabilității**:
Acest document a fost tradus folosind serviciul de traducere AI [Co-op Translator](https://github.com/Azure/co-op-translator). În timp ce ne străduim pentru acuratețe, vă rugăm să rețineți că traducerile automate pot conține erori sau inexactități. Documentul original în limba sa nativă trebuie considerat sursa autorizată. Pentru informații critice, se recomandă traducerea profesională realizată de un om. Nu ne asumăm responsabilitatea pentru eventualele neînțelegeri sau interpretări greșite care decurg din utilizarea acestei traduceri.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->