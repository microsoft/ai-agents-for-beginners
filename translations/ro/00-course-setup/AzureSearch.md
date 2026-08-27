# Ghid de Configurare Azure AI Search

Acest ghid vă va ajuta să configurați Azure AI Search folosind portalul Azure. Urmați pașii de mai jos pentru a crea și configura serviciul Azure AI Search.

## Cerințe preliminare

Înainte de a începe, asigurați-vă că aveți următoarele:

- Un abonament Azure. Dacă nu aveți un abonament Azure, puteți crea un cont gratuit la [Azure Free Account](https://azure.microsoft.com/free/?wt.mc_id=studentamb_258691).

## Pasul 1: Creați un cont de stocare Azure

1. Urmați această instrucțiune, [Create an Azure storage account](https://learn.microsoft.com/azure/storage/common/storage-account-create?tabs=azure-portal), pentru a crea un nou Cont de Stocare Azure.
   **NOTĂ**: Asigurați-vă că tipul contului de stocare este Standard General Purpose V2.

## Pasul 2: Creați un serviciu Azure AI Search

1. Conectați-vă la [portalul Azure](https://portal.azure.com/?wt.mc_id=studentamb_258691).
2. În panoul de navigare din stânga, faceți clic pe **Create a resource**.
3. În caseta de căutare, tastați „Azure AI Search” și selectați **Azure AI Search** din lista de rezultate.
4. Faceți clic pe butonul **Create**.
5. În fila **Basics**, furnizați următoarele informații:
   - **Subscription**: Selectați abonamentul dvs. Azure.
   - **Resource group**: Creați un grup de resurse nou sau selectați unul existent.
   - **Resource name**: Introduceți un nume unic pentru serviciul dvs. de căutare.
   - **Region**: Selectați regiunea cea mai apropiată de utilizatorii dvs.
   - **Pricing tier**: Alegeți un nivel de preț care să corespundă cerințelor dvs. Puteți începe cu nivelul gratuit pentru testare.
6. Faceți clic pe **Review + create**.
7. Revizuiți setările și faceți clic pe **Create** pentru a crea serviciul de căutare.

## Pasul 3: Începeți cu Azure AI Search

1. După ce implementarea este finalizată, navigați la serviciul dvs. de căutare în portalul Azure.
2. În panoul de prezentare al serviciului de căutare, copiați URL-ul. Ar trebui să arate ca `https://<service-name>.search.windows.net`.
3. **(Recomandat)** Activați accesul fără cheie cu Microsoft Entra ID (RBAC) așa cum este prezentat în Pasul 4 de mai jos — fără nevoie de cheie. Exemplele din acest ghid creează/actualizează indexuri și încarcă documente, ceea ce necesită rolurile **Search Service Contributor** și **Search Index Data Contributor** (sau, pentru autentificarea bazată pe cheie, **cheia administrativă principală** — nu cheia de interogare). Doar dacă nu puteți folosi RBAC, deschideți panoul **Settings > Keys** și copiați **cheia administrativă principală**.
4. Urmați pașii din pagina [Quickstart guide](https://learn.microsoft.com/azure/search/search-get-started-portal?pivots=import-data-new) pentru a crea un index, a încărca date și a efectua o căutare.

## Pasul 4: Utilizați uneltele Azure AI Search

Azure AI Search se integrează cu diverse unelte pentru a vă îmbunătăți capacitățile de căutare. Puteți utiliza Azure CLI, Python SDK, .NET SDK și alte unelte pentru configurări și operațiuni avansate.

### Folosind Azure CLI

1. Instalați Azure CLI urmând instrucțiunile de la [Install Azure CLI](https://learn.microsoft.com/cli/azure/install-azure-cli?wt.mc_id=studentamb_258691).
2. Conectați-vă la Azure CLI folosind comanda:

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

    Cu RBAC activat, exemplele Python și .NET SDK de mai jos se autentifică cu `DefaultAzureCredential`, care utilizează sesiunea `az login` în timpul dezvoltării locale — nu este nevoie de cheia administrativă. Consultați [Connect to Azure AI Search using roles](https://learn.microsoft.com/azure/search/search-security-rbac).

4. **(Fallback) Autentificare bazată pe cheie** — numai dacă nu puteți utiliza RBAC, stocați în continuare cheia administrativă:

#### Stocați atât adresa endpoint, cât și cheia API pentru instanța Azure AI Search ca variabile de mediu.

    ```bash
    # zsh/bash
    # az search service show nu are câmpul „endpoint”; construiți URL-ul folosind numele serviciului.
    export AZURE_SEARCH_SERVICE_ENDPOINT="https://<service-name>.search.windows.net"
    export AZURE_SEARCH_API_KEY=$(az search admin-key show -g <resource-group> --service-name <service-name> --query "primaryKey" -o tsv)
    ```

    ```powershell
    # PowerShell
    # az search service show nu are câmpul „endpoint”; construiți URL-ul folosind numele serviciului.
    $env:AZURE_SEARCH_SERVICE_ENDPOINT = "https://<service-name>.search.windows.net"
    $env:AZURE_SEARCH_API_KEY = $(az search admin-key show -g <resource-group> --service-name <service-name> --query "primaryKey" -o tsv)
    ```

### Folosind Python SDK

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

    # Fără cheie (recomandat): folosește identitatea ta `az login` prin RBAC Entra ID.
    # Necesită rolurile "Contributor pentru serviciul de căutare" și "Contributor pentru datele indexului de căutare".
    credential = DefaultAzureCredential()
    # Variante de rezervă (autentificare bazată pe cheie):
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

### Folosind .NET SDK

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
- [Uneltele Azure AI Search](https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-ai-search?tabs=azurecli%2Cpython&pivots=code-examples?wt.mc_id=studentamb_258691)

## Concluzie

Ați configurat cu succes Azure AI Search folosind portalul Azure și uneltele integrate. Acum puteți explora caracteristici și capacități avansate ale Azure AI Search pentru a vă îmbunătăți soluțiile de căutare.

Pentru asistență suplimentară, vizitați [documentația Azure Cognitive Search](https://learn.microsoft.com/azure/search/?wt.mc_id=studentamb_258691).

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Declinare a responsabilității**:
Acest document a fost tradus folosind serviciul de traducere AI [Co-op Translator](https://github.com/Azure/co-op-translator). În timp ce ne străduim pentru acuratețe, vă rugăm să rețineți că traducerile automate pot conține erori sau inexactități. Documentul original în limba sa nativă trebuie considerat sursa autorizată. Pentru informații critice, se recomandă traducerea profesională realizată de un om. Nu ne asumăm responsabilitatea pentru eventualele neînțelegeri sau interpretări greșite care decurg din utilizarea acestei traduceri.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->