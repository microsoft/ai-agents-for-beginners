# Οδηγός Ρύθμισης Azure AI Search

Αυτός ο οδηγός θα σας βοηθήσει να ρυθμίσετε το Azure AI Search χρησιμοποιώντας το Azure portal. Ακολουθήστε τα παρακάτω βήματα για να δημιουργήσετε και να διαμορφώσετε την υπηρεσία Azure AI Search.

## Προαπαιτούμενα

Πριν ξεκινήσετε, βεβαιωθείτε ότι έχετε τα ακόλουθα:

- Μια συνδρομή Azure. Αν δεν έχετε συνδρομή Azure, μπορείτε να δημιουργήσετε έναν δωρεάν λογαριασμό στο [Azure Free Account](https://azure.microsoft.com/free/?wt.mc_id=studentamb_258691).

## Βήμα 1: Δημιουργήστε έναν λογαριασμό Azure Storage

1. Ακολουθήστε αυτήν την οδηγία, [Create an Azure storage account](https://learn.microsoft.com/azure/storage/common/storage-account-create?tabs=azure-portal), για να δημιουργήσετε έναν νέο λογαριασμό Azure Storage.
   **ΣΗΜΕΙΩΣΗ**: Βεβαιωθείτε ότι ο τύπος του λογαριασμού Storage είναι Standard General Purpose V2.

## Βήμα 2: Δημιουργήστε μια υπηρεσία Azure AI Search

1. Συνδεθείτε στο [Azure portal](https://portal.azure.com/?wt.mc_id=studentamb_258691).
2. Στο αριστερό μενού πλοήγησης, κάντε κλικ στο **Create a resource**.
3. Στο πλαίσιο αναζήτησης, πληκτρολογήστε "Azure AI Search" και επιλέξτε **Azure AI Search** από τη λίστα αποτελεσμάτων.
4. Κάντε κλικ στο κουμπί **Create**.
5. Στην καρτέλα **Basics**, παρέχετε τις ακόλουθες πληροφορίες:
   - **Subscription**: Επιλέξτε τη συνδρομή Azure σας.
   - **Resource group**: Δημιουργήστε μια νέα ομάδα πόρων ή επιλέξτε μία υπάρχουσα.
   - **Resource name**: Εισάγετε μοναδικό όνομα για την υπηρεσία αναζήτησής σας.
   - **Region**: Επιλέξτε την περιοχή που βρίσκεται πιο κοντά στους χρήστες σας.
   - **Pricing tier**: Επιλέξτε επίπεδο τιμολόγησης που ταιριάζει στις απαιτήσεις σας. Μπορείτε να ξεκινήσετε με το δωρεάν επίπεδο για δοκιμές.
6. Κάντε κλικ στο **Review + create**.
7. Ελέγξτε τις ρυθμίσεις και κάντε κλικ στο **Create** για να δημιουργήσετε την υπηρεσία αναζήτησης.

## Βήμα 3: Ξεκινήστε με το Azure AI Search

1. Μόλις ολοκληρωθεί η ανάπτυξη, μεταβείτε στην υπηρεσία αναζήτησής σας στο Azure portal.
2. Στο παράθυρο επισκόπησης της υπηρεσίας αναζήτησης, αντιγράψτε το URL. Θα πρέπει να μοιάζει με `https://<service-name>.search.windows.net`.
3. **(Συνιστάται)** Ενεργοποιήστε την πρόσβαση χωρίς κλειδί με το Microsoft Entra ID (RBAC) όπως φαίνεται στο Βήμα 4 παρακάτω — δεν χρειάζεται κλειδί. Τα δείγματα σε αυτόν τον οδηγό δημιουργούν/ενημερώνουν ευρετήρια και ανεβάζουν έγγραφα, που απαιτούν τους ρόλους **Search Service Contributor** και **Search Index Data Contributor** (ή, για αυθεντικοποίηση με κλειδί, το **primary admin key** — όχι το query key). Μόνο αν δεν μπορείτε να χρησιμοποιήσετε RBAC, ανοίξτε το παράθυρο **Settings > Keys** και αντιγράψτε το **primary admin key**.
4. Ακολουθήστε τα βήματα στη σελίδα [Quickstart guide](https://learn.microsoft.com/azure/search/search-get-started-portal?pivots=import-data-new) για να δημιουργήσετε ένα ευρετήριο, να ανεβάσετε δεδομένα και να πραγματοποιήσετε αναζήτηση.

## Βήμα 4: Χρησιμοποιήστε εργαλεία Azure AI Search

Το Azure AI Search ενσωματώνεται με διάφορα εργαλεία για να ενισχύσει τις δυνατότητες αναζήτησής σας. Μπορείτε να χρησιμοποιήσετε το Azure CLI, το Python SDK, το .NET SDK και άλλα εργαλεία για προχωρημένες ρυθμίσεις και λειτουργίες.

### Χρήση Azure CLI

1. Εγκαταστήστε το Azure CLI ακολουθώντας τις οδηγίες στο [Install Azure CLI](https://learn.microsoft.com/cli/azure/install-azure-cli?wt.mc_id=studentamb_258691).
2. Συνδεθείτε στο Azure CLI με την εντολή:

   ```bash
   az login
   ```
3. **(Συνιστάται) Ενεργοποιήστε την πρόσβαση χωρίς κλειδί με το Microsoft Entra ID (RBAC):**

    ```bash
    az search service update --name <service-name> --resource-group <resource-group> --auth-options aadOrApiKey
    az role assignment create --assignee <your-user-or-principal-id> --role "Search Service Contributor" --scope $(az search service show -g <resource-group> -n <service-name> --query id -o tsv)
    az role assignment create --assignee <your-user-or-principal-id> --role "Search Index Data Contributor" --scope $(az search service show -g <resource-group> -n <service-name> --query id -o tsv)
    # Η εντολή az search service show δεν έχει πεδίο "endpoint". Δημιουργήστε το URL από το όνομα της υπηρεσίας.
    export AZURE_SEARCH_SERVICE_ENDPOINT="https://<service-name>.search.windows.net"
    ```

    Με το RBAC ενεργοποιημένο, τα παραδείγματα Python και .NET SDK παρακάτω αυθεντικοποιούνται με `DefaultAzureCredential`, το οποίο χρησιμοποιεί τη συνεδρία `az login` κατά την τοπική ανάπτυξη — δεν χρειάζεται κλειδί διαχειριστή. Δείτε [Connect to Azure AI Search using roles](https://learn.microsoft.com/azure/search/search-security-rbac).

4. **(Εφεδρική λύση) Αυθεντικοποίηση με κλειδί** — μόνο αν δεν μπορείτε να χρησιμοποιήσετε RBAC, αποθηκεύστε επίσης το κλειδί διαχειριστή:

#### Αποθηκεύστε τόσο το endpoint όσο και το API key για την περίπτωση Azure AI Search σε μεταβλητές περιβάλλοντος.

    ```bash
    # zsh/bash
    # az search service show δεν έχει πεδίο "endpoint"; κατασκευάστε το URL από το όνομα της υπηρεσίας.
    export AZURE_SEARCH_SERVICE_ENDPOINT="https://<service-name>.search.windows.net"
    export AZURE_SEARCH_API_KEY=$(az search admin-key show -g <resource-group> --service-name <service-name> --query "primaryKey" -o tsv)
    ```

    ```powershell
    # PowerShell
    # az search service show δεν έχει πεδίο "endpoint"; κατασκευάστε το URL από το όνομα της υπηρεσίας.
    $env:AZURE_SEARCH_SERVICE_ENDPOINT = "https://<service-name>.search.windows.net"
    $env:AZURE_SEARCH_API_KEY = $(az search admin-key show -g <resource-group> --service-name <service-name> --query "primaryKey" -o tsv)
    ```

### Χρήση Python SDK

1. Εγκαταστήστε τη βιβλιοθήκη πελάτη Azure Cognitive Search και το Azure Identity για Python:

   ```bash
   pip install azure-search-documents azure-identity
   ```

2. Χρησιμοποιήστε τον ακόλουθο κώδικα Python για να δημιουργήσετε ένα ευρετήριο και να ανεβάσετε έγγραφα:

    ```python
    import os
    from azure.identity import DefaultAzureCredential
    from azure.search.documents import SearchClient
    from azure.search.documents.indexes import SearchIndexClient
    from azure.search.documents.indexes.models import SearchIndex, SimpleField, edm

    service_endpoint = os.getenv("AZURE_SEARCH_SERVICE_ENDPOINT")
    index_name = "sample-index"

    # Χωρίς κλειδί (συνιστάται): χρησιμοποιεί την ταυτότητά σας `az login` μέσω Entra ID RBAC.
    # Απαιτεί τους ρόλους "Συντελεστής Υπηρεσίας Αναζήτησης" και "Συντελεστής Δεδομένων Ευρετηρίου Αναζήτησης".
    credential = DefaultAzureCredential()
    # Εναλλακτική (έλεγχος ταυτότητας με κλειδί):
    # από azure.core.credentials εισαγωγή AzureKeyCredential
    # διαπιστευτήριο = AzureKeyCredential(os.getenv("AZURE_SEARCH_API_KEY"))
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

### Χρήση .NET SDK

1. Εκτελέστε την ακόλουθη εντολή για να δημιουργήσετε ένα ευρετήριο και να ανεβάσετε έγγραφα:

    ```bash
    dotnet run ./AzureSearch.cs
    ```

    Το παράδειγμα .NET παρακάτω χρησιμοποιεί `DefaultAzureCredential`, που μπορεί να χρησιμοποιήσει την είσοδο σας στο Azure CLI από το `az login` κατά την τοπική ανάπτυξη.

2. Εδώ είναι ο κώδικας .NET από το `AzureSearch.cs`:

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

Για περισσότερες λεπτομερείς πληροφορίες, ανατρέξτε στην παρακάτω τεκμηρίωση:

- [Create an Azure Cognitive Search service](https://learn.microsoft.com/azure/search/search-create-service-portal?wt.mc_id=studentamb_258691)
- [Get started with Azure Cognitive Search](https://learn.microsoft.com/azure/search/search-get-started-portal?wt.mc_id=studentamb_258691)
- [Azure AI Search Tools](https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-ai-search?tabs=azurecli%2Cpython&pivots=code-examples?wt.mc_id=studentamb_258691)

## Συμπέρασμα

Έχετε ρυθμίσει με επιτυχία το Azure AI Search χρησιμοποιώντας το Azure portal και ενσωματωμένα εργαλεία. Μπορείτε τώρα να εξερευνήσετε πιο προχωρημένες δυνατότητες και λειτουργίες του Azure AI Search για να ενισχύσετε τις λύσεις αναζήτησής σας.

Για περαιτέρω βοήθεια, επισκεφτείτε την [τεκμηρίωση Azure Cognitive Search](https://learn.microsoft.com/azure/search/?wt.mc_id=studentamb_258691).

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Αποποίηση ευθυνών**:
Αυτό το έγγραφο έχει μεταφραστεί χρησιμοποιώντας την υπηρεσία μετάφρασης με τεχνητή νοημοσύνη [Co-op Translator](https://github.com/Azure/co-op-translator). Ενώ επιδιώκουμε την ακρίβεια, παρακαλούμε να έχετε υπόψη ότι οι αυτοματοποιημένες μεταφράσεις ενδέχεται να περιέχουν λάθη ή ανακρίβειες. Το πρωτότυπο έγγραφο στη μητρική του γλώσσα πρέπει να θεωρείται η αυθεντική πηγή. Για κρίσιμες πληροφορίες, συνιστάται επαγγελματική ανθρώπινη μετάφραση. Δεν φέρουμε ευθύνη για τυχόν παρεξηγήσεις ή λανθασμένες ερμηνείες που προκύπτουν από τη χρήση αυτής της μετάφρασης.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->