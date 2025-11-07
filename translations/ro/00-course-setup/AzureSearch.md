<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "11e38db0898a788612b917e329dcdb5b",
  "translation_date": "2025-11-07T08:48:08+00:00",
  "source_file": "00-course-setup/AzureSearch.md",
  "language_code": "ro"
}
-->
# Ghid de configurare Azure AI Search

Acest ghid te va ajuta să configurezi Azure AI Search folosind portalul Azure. Urmează pașii de mai jos pentru a crea și configura serviciul Azure AI Search.

## Cerințe preliminare

Înainte de a începe, asigură-te că ai următoarele:

- Un abonament Azure. Dacă nu ai un abonament Azure, poți crea un cont gratuit la [Cont Gratuit Azure](https://azure.microsoft.com/free/?wt.mc_id=studentamb_258691).

## Pasul 1: Creează un cont de stocare Azure

1. Urmează instrucțiunile de aici, [Crearea unui cont de stocare Azure](https://learn.microsoft.com/azure/storage/common/storage-account-create?tabs=azure-portal), pentru a crea un nou cont de stocare Azure.  
   **NOTE**: Asigură-te că tipul contului de stocare este Standard General Purpose V2.

## Pasul 2: Creează un serviciu Azure AI Search

1. Autentifică-te în [portalul Azure](https://portal.azure.com/?wt.mc_id=studentamb_258691).
2. În panoul de navigare din stânga, dă clic pe **Create a resource**.
3. În caseta de căutare, tastează "Azure AI Search" și selectează **Azure AI Search** din lista de rezultate.
4. Dă clic pe butonul **Create**.
5. În fila **Basics**, furnizează următoarele informații:
   - **Subscription**: Selectează abonamentul tău Azure.
   - **Resource group**: Creează un nou grup de resurse sau selectează unul existent.
   - **Resource name**: Introdu un nume unic pentru serviciul tău de căutare.
   - **Region**: Selectează regiunea cea mai apropiată de utilizatorii tăi.
   - **Pricing tier**: Alege un nivel de preț care să corespundă cerințelor tale. Poți începe cu nivelul gratuit pentru testare.
6. Dă clic pe **Review + create**.
7. Revizuiește setările și dă clic pe **Create** pentru a crea serviciul de căutare.

## Pasul 3: Începe să utilizezi Azure AI Search

1. După finalizarea implementării, navighează la serviciul tău de căutare în portalul Azure.
2. În panoul de prezentare generală al serviciului de căutare, copiază URL-ul. Ar trebui să arate astfel: `https://<service-name>.search.windows.net`.
3. În panoul Settings > Keys, copiază cheia de interogare.
4. Urmează pașii de pe pagina [Ghid de început rapid](https://learn.microsoft.com/azure/search/search-get-started-portal?pivots=import-data-new) pentru a crea un index, a încărca date și a efectua o interogare de căutare.

## Pasul 4: Utilizează instrumentele Azure AI Search

Azure AI Search se integrează cu diverse instrumente pentru a îmbunătăți capacitățile de căutare. Poți utiliza Azure CLI, Python SDK, .NET SDK și alte instrumente pentru configurări și operațiuni avansate.

### Utilizarea Azure CLI

1. Instalează Azure CLI urmând instrucțiunile de aici: [Instalare Azure CLI](https://learn.microsoft.com/cli/azure/install-azure-cli?wt.mc_id=studentamb_258691).
2. Autentifică-te în Azure CLI folosind comanda:

   ```bash
   az login
   ```

3. Stochează endpoint-ul și cheia API pentru instanța Azure AI Search în variabile de mediu.

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

### Utilizarea Python SDK

1. Instalează biblioteca client Azure Cognitive Search pentru Python:

   ```bash
   pip install azure-search-documents
   ```

2. Utilizează următorul cod Python pentru a crea un index și a încărca documente:

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

### Utilizarea .NET SDK

1. Rulează următoarea comandă pentru a crea un index și a încărca documente:

    ```bash
    dotnet run ./AzureSearch.cs
    ```

2. Iată codul .NET din `AzureSearch.cs`:

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

Pentru informații mai detaliate, consultă următoarea documentație:

- [Crearea unui serviciu Azure Cognitive Search](https://learn.microsoft.com/azure/search/search-create-service-portal?wt.mc_id=studentamb_258691)
- [Începe cu Azure Cognitive Search](https://learn.microsoft.com/azure/search/search-get-started-portal?wt.mc_id=studentamb_258691)
- [Instrumente Azure AI Search](https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-ai-search?tabs=azurecli%2Cpython&pivots=code-examples?wt.mc_id=studentamb_258691)

## Concluzie

Ai configurat cu succes Azure AI Search folosind portalul Azure și instrumentele integrate. Acum poți explora funcționalități și capabilități mai avansate ale Azure AI Search pentru a îmbunătăți soluțiile tale de căutare.

Pentru asistență suplimentară, vizitează [Documentația Azure Cognitive Search](https://learn.microsoft.com/azure/search/?wt.mc_id=studentamb_258691).

---

**Declinare de responsabilitate**:  
Acest document a fost tradus folosind serviciul de traducere AI [Co-op Translator](https://github.com/Azure/co-op-translator). Deși ne străduim să asigurăm acuratețea, vă rugăm să fiți conștienți că traducerile automate pot conține erori sau inexactități. Documentul original în limba sa maternă ar trebui considerat sursa autoritară. Pentru informații critice, se recomandă traducerea profesională realizată de oameni. Nu ne asumăm responsabilitatea pentru neînțelegeri sau interpretări greșite care pot apărea din utilizarea acestei traduceri.