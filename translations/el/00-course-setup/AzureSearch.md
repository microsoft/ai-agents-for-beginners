# Οδηγός Ρύθμισης Azure AI Search

Αυτός ο οδηγός θα σας βοηθήσει να ρυθμίσετε το Azure AI Search χρησιμοποιώντας το Azure portal. Ακολουθήστε τα παρακάτω βήματα για να δημιουργήσετε και να ρυθμίσετε την υπηρεσία Azure AI Search σας.

## Προαπαιτούμενα

Πριν ξεκινήσετε, βεβαιωθείτε ότι διαθέτετε τα εξής:

- Ένα συνδρομητικό πρόγραμμα Azure. Εάν δεν διαθέτετε συνδρομή Azure, μπορείτε να δημιουργήσετε έναν δωρεάν λογαριασμό στον [Azure Free Account](https://azure.microsoft.com/free/?wt.mc_id=studentamb_258691).

## Βήμα 1: Δημιουργία Λογαριασμού Αποθήκευσης Azure

1. Ακολουθήστε αυτή την οδηγία, [Create an Azure storage account](https://learn.microsoft.com/azure/storage/common/storage-account-create?tabs=azure-portal), για να δημιουργήσετε έναν νέο λογαριασμό αποθήκευσης Azure.
   **ΣΗΜΕΙΩΣΗ**: Βεβαιωθείτε ότι ο τύπος του Λογαριασμού Αποθήκευσης είναι Standard General Purpose V2.

## Βήμα 2: Δημιουργία Υπηρεσίας Azure AI Search

1. Συνδεθείτε στο [Azure portal](https://portal.azure.com/?wt.mc_id=studentamb_258691).
2. Στην αριστερή πλευρική μπάρα πλοήγησης, κάντε κλικ στο **Create a resource**.
3. Στο πεδίο αναζήτησης πληκτρολογήστε "Azure AI Search" και επιλέξτε **Azure AI Search** από τη λίστα αποτελεσμάτων.
4. Κάντε κλικ στο κουμπί **Create**.
5. Στην καρτέλα **Basics**, πληκτρολογήστε τις ακόλουθες πληροφορίες:
   - **Subscription**: Επιλέξτε τη συνδρομή Azure σας.
   - **Resource group**: Δημιουργήστε μια νέα ομάδα πόρων ή επιλέξτε μια υπάρχουσα.
   - **Resource name**: Εισάγετε ένα μοναδικό όνομα για την υπηρεσία αναζήτησής σας.
   - **Region**: Επιλέξτε την περιοχή που είναι πιο κοντά στους χρήστες σας.
   - **Pricing tier**: Επιλέξτε ένα επίπεδο τιμολόγησης που ικανοποιεί τις ανάγκες σας. Μπορείτε να ξεκινήσετε με το δωρεάν επίπεδο για δοκιμές.
6. Κάντε κλικ στο **Review + create**.
7. Ελέγξτε τις ρυθμίσεις και πατήστε **Create** για να δημιουργήσετε την υπηρεσία αναζήτησης.

## Βήμα 3: Ξεκινήστε με το Azure AI Search

1. Μόλις ολοκληρωθεί η ανάπτυξη, μεταβείτε στην υπηρεσία αναζήτησης στο Azure portal.
2. Στο παράθυρο επισκόπησης της υπηρεσίας αναζήτησης, αντιγράψτε το URL. Θα πρέπει να μοιάζει με `https://<service-name>.search.windows.net`.
3. **(Συνιστάται)** Ενεργοποιήστε την πρόσβαση χωρίς κλειδί με το Microsoft Entra ID (RBAC) όπως φαίνεται στο Βήμα 4 παρακάτω — δεν χρειάζεται κλειδί. Τα παραδείγματα σε αυτόν τον οδηγό δημιουργούν/ενημερώνουν ευρετήρια και ανεβάζουν έγγραφα, που απαιτούν τους ρόλους **Search Service Contributor** και **Search Index Data Contributor** (ή, για αυθεντικοποίηση με κλειδί, το **primary admin key** — όχι το κλειδί αναζήτησης). Μόνο αν δεν μπορείτε να χρησιμοποιήσετε RBAC, ανοίξτε το παράθυρο **Settings > Keys** και αντιγράψτε το **primary admin key**.
4. Ακολουθήστε τα βήματα στην σελίδα [Quickstart guide](https://learn.microsoft.com/azure/search/search-get-started-portal?pivots=import-data-new) για να δημιουργήσετε ένα ευρετήριο, να ανεβάσετε δεδομένα και να πραγματοποιήσετε μια αναζήτηση.

## Βήμα 4: Χρήση Εργαλείων Azure AI Search

Το Azure AI Search ενσωματώνεται με διάφορα εργαλεία για να βελτιώσει τις δυνατότητες αναζήτησής σας. Μπορείτε να χρησιμοποιήσετε το Azure CLI, το Python SDK, .NET SDK και άλλα εργαλεία για προχωρημένες ρυθμίσεις και λειτουργίες.

### Χρήση του Azure CLI

1. Εγκαταστήστε το Azure CLI ακολουθώντας τις οδηγίες στο [Install Azure CLI](https://learn.microsoft.com/cli/azure/install-azure-cli?wt.mc_id=studentamb_258691).
2. Συνδεθείτε στο Azure CLI χρησιμοποιώντας την εντολή:

   ```bash
   az login
   ```
3. **(Συνιστάται) Ενεργοποιήστε την πρόσβαση χωρίς κλειδί με Microsoft Entra ID (RBAC):**

    ```bash
    az search service update --name <service-name> --resource-group <resource-group> --auth-options aadOrApiKey
    az role assignment create --assignee <your-user-or-principal-id> --role "Search Service Contributor" --scope $(az search service show -g <resource-group> -n <service-name> --query id -o tsv)
    az role assignment create --assignee <your-user-or-principal-id> --role "Search Index Data Contributor" --scope $(az search service show -g <resource-group> -n <service-name> --query id -o tsv)
    # η εντολή az search service show δεν έχει πεδίο "endpoint". Δημιουργήστε το URL από το όνομα της υπηρεσίας.
    export AZURE_SEARCH_SERVICE_ENDPOINT="https://<service-name>.search.windows.net"
    ```

    Με ενεργοποιημένο το RBAC, τα παραδείγματα Python και .NET SDK παρακάτω αυθεντικοποιούνται με το `DefaultAzureCredential`, το οποίο χρησιμοποιεί τη συνεδρία `az login` κατά την τοπική ανάπτυξη — δεν απαιτείται κλειδί διαχειριστή. Δείτε το [Connect to Azure AI Search using roles](https://learn.microsoft.com/azure/search/search-security-rbac).

4. **(Εναλλακτική) Αυθεντικοποίηση με κλειδί** — μόνο αν δεν μπορείτε να χρησιμοποιήσετε RBAC, αποθηκεύστε επίσης το κλειδί διαχειριστή:

#### Αποθηκεύστε τόσο το endpoint όσο και το API key για την παρουσία Azure AI Search σε μεταβλητές περιβάλλοντος.

    ```bash
    # zsh/bash
    # az search service show δεν έχει πεδίο "endpoint"; δημιουργήστε το URL από το όνομα της υπηρεσίας.
    export AZURE_SEARCH_SERVICE_ENDPOINT="https://<service-name>.search.windows.net"
    export AZURE_SEARCH_API_KEY=$(az search admin-key show -g <resource-group> --service-name <service-name> --query "primaryKey" -o tsv)
    ```

    ```powershell
    # PowerShell
    # az search service show δεν έχει πεδίο "endpoint"; δημιουργήστε το URL από το όνομα της υπηρεσίας.
    $env:AZURE_SEARCH_SERVICE_ENDPOINT = "https://<service-name>.search.windows.net"
    $env:AZURE_SEARCH_API_KEY = $(az search admin-key show -g <resource-group> --service-name <service-name> --query "primaryKey" -o tsv)
    ```

### Χρήση Python SDK

1. Εγκαταστήστε τη βιβλιοθήκη πελάτη Azure Cognitive Search και το Azure Identity για Python:

   ```bash
   pip install azure-search-documents azure-identity
   ```

2. Χρησιμοποιήστε τον παρακάτω κώδικα Python για να δημιουργήσετε ένα ευρετήριο και να ανεβάσετε έγγραφα:

    ```python
    import os
    from azure.identity import DefaultAzureCredential
    from azure.search.documents import SearchClient
    from azure.search.documents.indexes import SearchIndexClient
    from azure.search.documents.indexes.models import SearchIndex, SimpleField, edm

    service_endpoint = os.getenv("AZURE_SEARCH_SERVICE_ENDPOINT")
    index_name = "sample-index"

    # Χωρίς κλειδί (συνιστάται): χρησιμοποιεί την ταυτότητά σας `az login` μέσω του Entra ID RBAC.
    # Απαιτεί τους ρόλους "Συνεισφέρων Υπηρεσίας Αναζήτησης" και "Συνεισφέρων Δεδομένων Ευρετηρίου Αναζήτησης".
    credential = DefaultAzureCredential()
    # Εναλλακτική λύση (έλεγχος ταυτότητας με κλειδί):
    # από azure.core.credentials εισαγωγή AzureKeyCredential
    # διαπιστευτήρια = AzureKeyCredential(os.getenv("AZURE_SEARCH_API_KEY"))
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

    Το δείγμα .NET παρακάτω χρησιμοποιεί το `DefaultAzureCredential`, το οποίο μπορεί να χρησιμοποιήσει την είσοδο Azure CLI σας από το `az login` κατά την τοπική ανάπτυξη.

2. Εδώ είναι ο κώδικας .NET του `AzureSearch.cs`:

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

Για πιο αναλυτικές πληροφορίες, ανατρέξτε στην ακόλουθη τεκμηρίωση:

- [Create an Azure Cognitive Search service](https://learn.microsoft.com/azure/search/search-create-service-portal?wt.mc_id=studentamb_258691)
- [Get started with Azure Cognitive Search](https://learn.microsoft.com/azure/search/search-get-started-portal?wt.mc_id=studentamb_258691)
- [Azure AI Search Tools](https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-ai-search?tabs=azurecli%2Cpython&pivots=code-examples?wt.mc_id=studentamb_258691)

## Συμπέρασμα

Έχετε ρυθμίσει επιτυχώς το Azure AI Search χρησιμοποιώντας το Azure portal και τα ενσωματωμένα εργαλεία. Τώρα μπορείτε να εξερευνήσετε πιο προχωρημένες λειτουργίες και δυνατότητες του Azure AI Search για να βελτιώσετε τις λύσεις αναζήτησής σας.

Για περαιτέρω βοήθεια, επισκεφθείτε την [τεκμηρίωση Azure Cognitive Search](https://learn.microsoft.com/azure/search/?wt.mc_id=studentamb_258691).

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Αποποίηση ευθυνών**:
Αυτό το έγγραφο έχει μεταφραστεί χρησιμοποιώντας την υπηρεσία μετάφρασης με τεχνητή νοημοσύνη [Co-op Translator](https://github.com/Azure/co-op-translator). Ενώ επιδιώκουμε την ακρίβεια, παρακαλούμε να έχετε υπόψη ότι οι αυτοματοποιημένες μεταφράσεις ενδέχεται να περιέχουν λάθη ή ανακρίβειες. Το πρωτότυπο έγγραφο στη μητρική του γλώσσα πρέπει να θεωρείται η αυθεντική πηγή. Για κρίσιμες πληροφορίες, συνιστάται επαγγελματική ανθρώπινη μετάφραση. Δεν φέρουμε ευθύνη για τυχόν παρεξηγήσεις ή λανθασμένες ερμηνείες που προκύπτουν από τη χρήση αυτής της μετάφρασης.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->