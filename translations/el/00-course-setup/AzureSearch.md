<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "11e38db0898a788612b917e329dcdb5b",
  "translation_date": "2025-11-07T08:37:34+00:00",
  "source_file": "00-course-setup/AzureSearch.md",
  "language_code": "el"
}
-->
# Οδηγός Ρύθμισης του Azure AI Search

Αυτός ο οδηγός θα σας βοηθήσει να ρυθμίσετε το Azure AI Search χρησιμοποιώντας την πύλη Azure. Ακολουθήστε τα παρακάτω βήματα για να δημιουργήσετε και να διαμορφώσετε την υπηρεσία Azure AI Search.

## Προαπαιτούμενα

Πριν ξεκινήσετε, βεβαιωθείτε ότι έχετε τα εξής:

- Μια συνδρομή Azure. Αν δεν έχετε συνδρομή Azure, μπορείτε να δημιουργήσετε έναν δωρεάν λογαριασμό στο [Azure Free Account](https://azure.microsoft.com/free/?wt.mc_id=studentamb_258691).

## Βήμα 1: Δημιουργία Λογαριασμού Αποθήκευσης Azure

1. Ακολουθήστε αυτές τις οδηγίες, [Create an Azure storage account](https://learn.microsoft.com/azure/storage/common/storage-account-create?tabs=azure-portal), για να δημιουργήσετε έναν νέο λογαριασμό αποθήκευσης Azure.
   **NOTE**: Βεβαιωθείτε ότι ο τύπος του λογαριασμού αποθήκευσης είναι Standard General Purpose V2.

## Βήμα 2: Δημιουργία Υπηρεσίας Azure AI Search

1. Συνδεθείτε στην [πύλη Azure](https://portal.azure.com/?wt.mc_id=studentamb_258691).
2. Στο αριστερό μενού πλοήγησης, κάντε κλικ στο **Create a resource**.
3. Στο πλαίσιο αναζήτησης, πληκτρολογήστε "Azure AI Search" και επιλέξτε **Azure AI Search** από τη λίστα αποτελεσμάτων.
4. Κάντε κλικ στο κουμπί **Create**.
5. Στην καρτέλα **Basics**, παρέχετε τις ακόλουθες πληροφορίες:
   - **Subscription**: Επιλέξτε τη συνδρομή σας στο Azure.
   - **Resource group**: Δημιουργήστε μια νέα ομάδα πόρων ή επιλέξτε μια υπάρχουσα.
   - **Resource name**: Εισάγετε ένα μοναδικό όνομα για την υπηρεσία αναζήτησης.
   - **Region**: Επιλέξτε την περιοχή που είναι πιο κοντά στους χρήστες σας.
   - **Pricing tier**: Επιλέξτε ένα επίπεδο τιμολόγησης που ταιριάζει στις ανάγκες σας. Μπορείτε να ξεκινήσετε με το Free tier για δοκιμές.
6. Κάντε κλικ στο **Review + create**.
7. Ελέγξτε τις ρυθμίσεις και κάντε κλικ στο **Create** για να δημιουργήσετε την υπηρεσία αναζήτησης.

## Βήμα 3: Ξεκινήστε με το Azure AI Search

1. Μόλις ολοκληρωθεί η ανάπτυξη, μεταβείτε στην υπηρεσία αναζήτησης σας στην πύλη Azure.
2. Στον πίνακα επισκόπησης της υπηρεσίας αναζήτησης, αντιγράψτε το URL. Θα πρέπει να μοιάζει με `https://<service-name>.search.windows.net`.
3. Στην καρτέλα Settings > Keys, αντιγράψτε το query key.
4. Ακολουθήστε τα βήματα στη σελίδα [Quickstart guide](https://learn.microsoft.com/azure/search/search-get-started-portal?pivots=import-data-new) για να δημιουργήσετε ένα index, να ανεβάσετε δεδομένα και να εκτελέσετε ένα ερώτημα αναζήτησης.

## Βήμα 4: Χρησιμοποιήστε Εργαλεία του Azure AI Search

Το Azure AI Search ενσωματώνεται με διάφορα εργαλεία για να βελτιώσει τις δυνατότητες αναζήτησης σας. Μπορείτε να χρησιμοποιήσετε το Azure CLI, Python SDK, .NET SDK και άλλα εργαλεία για προηγμένες διαμορφώσεις και λειτουργίες.

### Χρήση του Azure CLI

1. Εγκαταστήστε το Azure CLI ακολουθώντας τις οδηγίες στο [Install Azure CLI](https://learn.microsoft.com/cli/azure/install-azure-cli?wt.mc_id=studentamb_258691).
2. Συνδεθείτε στο Azure CLI χρησιμοποιώντας την εντολή:

   ```bash
   az login
   ```

3. Αποθηκεύστε το endpoint και το API key της υπηρεσίας Azure AI Search σε μεταβλητές περιβάλλοντος.

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

### Χρήση του Python SDK

1. Εγκαταστήστε τη βιβλιοθήκη πελάτη Azure Cognitive Search για Python:

   ```bash
   pip install azure-search-documents
   ```

2. Χρησιμοποιήστε τον παρακάτω κώδικα Python για να δημιουργήσετε ένα index και να ανεβάσετε έγγραφα:

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

### Χρήση του .NET SDK

1. Εκτελέστε την παρακάτω εντολή για να δημιουργήσετε ένα index και να ανεβάσετε έγγραφα:

    ```bash
    dotnet run ./AzureSearch.cs
    ```

2. Εδώ είναι ο κώδικας .NET του `AzureSearch.cs`:

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

Για περισσότερες λεπτομέρειες, ανατρέξτε στην ακόλουθη τεκμηρίωση:

- [Create an Azure Cognitive Search service](https://learn.microsoft.com/azure/search/search-create-service-portal?wt.mc_id=studentamb_258691)
- [Get started with Azure Cognitive Search](https://learn.microsoft.com/azure/search/search-get-started-portal?wt.mc_id=studentamb_258691)
- [Azure AI Search Tools](https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-ai-search?tabs=azurecli%2Cpython&pivots=code-examples?wt.mc_id=studentamb_258691)

## Συμπέρασμα

Έχετε ρυθμίσει επιτυχώς το Azure AI Search χρησιμοποιώντας την πύλη Azure και τα ενσωματωμένα εργαλεία. Τώρα μπορείτε να εξερευνήσετε πιο προηγμένες λειτουργίες και δυνατότητες του Azure AI Search για να βελτιώσετε τις λύσεις αναζήτησης σας.

Για περαιτέρω βοήθεια, επισκεφθείτε την [τεκμηρίωση του Azure Cognitive Search](https://learn.microsoft.com/azure/search/?wt.mc_id=studentamb_258691).

---

**Αποποίηση ευθύνης**:  
Αυτό το έγγραφο έχει μεταφραστεί χρησιμοποιώντας την υπηρεσία αυτόματης μετάφρασης [Co-op Translator](https://github.com/Azure/co-op-translator). Παρόλο που καταβάλλουμε προσπάθειες για ακρίβεια, παρακαλούμε να έχετε υπόψη ότι οι αυτόματες μεταφράσεις ενδέχεται να περιέχουν λάθη ή ανακρίβειες. Το πρωτότυπο έγγραφο στη μητρική του γλώσσα θα πρέπει να θεωρείται η αυθεντική πηγή. Για κρίσιμες πληροφορίες, συνιστάται επαγγελματική ανθρώπινη μετάφραση. Δεν φέρουμε ευθύνη για τυχόν παρεξηγήσεις ή εσφαλμένες ερμηνείες που προκύπτουν από τη χρήση αυτής της μετάφρασης.