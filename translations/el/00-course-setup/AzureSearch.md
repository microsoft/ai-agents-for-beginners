<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f0ce2d470f3efad6f8c7df376f416a4b",
  "translation_date": "2025-07-12T07:36:58+00:00",
  "source_file": "00-course-setup/AzureSearch.md",
  "language_code": "el"
}
-->
# Οδηγός Ρύθμισης Azure AI Search

Αυτός ο οδηγός θα σας βοηθήσει να ρυθμίσετε το Azure AI Search χρησιμοποιώντας το Azure portal. Ακολουθήστε τα παρακάτω βήματα για να δημιουργήσετε και να διαμορφώσετε την υπηρεσία Azure AI Search.

## Προαπαιτούμενα

Πριν ξεκινήσετε, βεβαιωθείτε ότι έχετε τα εξής:

- Μια συνδρομή Azure. Αν δεν έχετε συνδρομή Azure, μπορείτε να δημιουργήσετε έναν δωρεάν λογαριασμό στο [Azure Free Account](https://azure.microsoft.com/free/?wt.mc_id=studentamb_258691).

## Βήμα 1: Δημιουργία υπηρεσίας Azure AI Search

1. Συνδεθείτε στο [Azure portal](https://portal.azure.com/?wt.mc_id=studentamb_258691).
2. Στο αριστερό μενού πλοήγησης, κάντε κλικ στο **Create a resource**.
3. Στο πεδίο αναζήτησης, πληκτρολογήστε "Azure AI Search" και επιλέξτε **Azure AI Search** από τη λίστα αποτελεσμάτων.
4. Κάντε κλικ στο κουμπί **Create**.
5. Στην καρτέλα **Basics**, συμπληρώστε τις παρακάτω πληροφορίες:
   - **Subscription**: Επιλέξτε τη συνδρομή Azure σας.
   - **Resource group**: Δημιουργήστε μια νέα ομάδα πόρων ή επιλέξτε μια υπάρχουσα.
   - **Resource name**: Εισάγετε ένα μοναδικό όνομα για την υπηρεσία αναζήτησής σας.
   - **Region**: Επιλέξτε την περιοχή που είναι πιο κοντά στους χρήστες σας.
   - **Pricing tier**: Επιλέξτε ένα επίπεδο τιμολόγησης που ταιριάζει στις ανάγκες σας. Μπορείτε να ξεκινήσετε με το Free tier για δοκιμές.
6. Κάντε κλικ στο **Review + create**.
7. Ελέγξτε τις ρυθμίσεις και πατήστε **Create** για να δημιουργήσετε την υπηρεσία αναζήτησης.

## Βήμα 2: Ξεκινήστε με το Azure AI Search

1. Μόλις ολοκληρωθεί η ανάπτυξη, μεταβείτε στην υπηρεσία αναζήτησής σας στο Azure portal.
2. Στη σελίδα επισκόπησης της υπηρεσίας αναζήτησης, κάντε κλικ στο κουμπί **Quickstart**.
3. Ακολουθήστε τα βήματα στον οδηγό Quickstart για να δημιουργήσετε ένα ευρετήριο, να ανεβάσετε δεδομένα και να εκτελέσετε ένα ερώτημα αναζήτησης.

### Δημιουργία Ευρετηρίου

1. Στον οδηγό Quickstart, κάντε κλικ στο **Create an index**.
2. Ορίστε το σχήμα του ευρετηρίου καθορίζοντας τα πεδία και τα χαρακτηριστικά τους (π.χ. τύπος δεδομένων, αν είναι αναζητήσιμα, φιλτραρίσιμα).
3. Κάντε κλικ στο **Create** για να δημιουργήσετε το ευρετήριο.

### Ανέβασμα Δεδομένων

1. Στον οδηγό Quickstart, κάντε κλικ στο **Upload data**.
2. Επιλέξτε μια πηγή δεδομένων (π.χ. Azure Blob Storage, Azure SQL Database) και δώστε τα απαραίτητα στοιχεία σύνδεσης.
3. Αντιστοιχίστε τα πεδία της πηγής δεδομένων με τα πεδία του ευρετηρίου.
4. Κάντε κλικ στο **Submit** για να ανεβάσετε τα δεδομένα στο ευρετήριο.

### Εκτέλεση Ερωτήματος Αναζήτησης

1. Στον οδηγό Quickstart, κάντε κλικ στο **Search explorer**.
2. Πληκτρολογήστε ένα ερώτημα αναζήτησης στο πεδίο αναζήτησης για να δοκιμάσετε τη λειτουργία αναζήτησης.
3. Εξετάστε τα αποτελέσματα αναζήτησης και προσαρμόστε το σχήμα του ευρετηρίου ή τα δεδομένα όπως χρειάζεται.

## Βήμα 3: Χρήση Εργαλείων Azure AI Search

Το Azure AI Search ενσωματώνεται με διάφορα εργαλεία για να βελτιώσει τις δυνατότητες αναζήτησής σας. Μπορείτε να χρησιμοποιήσετε το Azure CLI, το Python SDK και άλλα εργαλεία για προχωρημένες ρυθμίσεις και λειτουργίες.

### Χρήση Azure CLI

1. Εγκαταστήστε το Azure CLI ακολουθώντας τις οδηγίες στο [Install Azure CLI](https://learn.microsoft.com/en-us/cli/azure/install-azure-cli?wt.mc_id=studentamb_258691).
2. Συνδεθείτε στο Azure CLI χρησιμοποιώντας την εντολή:
   ```bash
   az login
   ```
3. Δημιουργήστε μια νέα υπηρεσία αναζήτησης χρησιμοποιώντας το Azure CLI:
   ```bash
   az search service create --resource-group <resource-group> --name <service-name> --sku Free
   ```
4. Δημιουργήστε ένα ευρετήριο χρησιμοποιώντας το Azure CLI:
   ```bash
   az search index create --service-name <service-name> --name <index-name> --fields "field1:type, field2:type"
   ```

### Χρήση Python SDK

1. Εγκαταστήστε τη βιβλιοθήκη πελάτη Azure Cognitive Search για Python:
   ```bash
   pip install azure-search-documents
   ```
2. Χρησιμοποιήστε τον παρακάτω κώδικα Python για να δημιουργήσετε ένα ευρετήριο και να ανεβάσετε έγγραφα:
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

Για πιο αναλυτικές πληροφορίες, ανατρέξτε στην παρακάτω τεκμηρίωση:

- [Create an Azure Cognitive Search service](https://learn.microsoft.com/en-us/azure/search/search-create-service-portal?wt.mc_id=studentamb_258691)
- [Get started with Azure Cognitive Search](https://learn.microsoft.com/en-us/azure/search/search-get-started-portal?wt.mc_id=studentamb_258691)
- [Azure AI Search Tools](https://learn.microsoft.com/en-us/azure/ai-services/agents/how-to/tools/azure-ai-search?tabs=azurecli%2Cpython&pivots=code-examples?wt.mc_id=studentamb_258691)

## Συμπέρασμα

Έχετε ρυθμίσει επιτυχώς το Azure AI Search χρησιμοποιώντας το Azure portal και τα ενσωματωμένα εργαλεία. Τώρα μπορείτε να εξερευνήσετε πιο προχωρημένες λειτουργίες και δυνατότητες του Azure AI Search για να βελτιώσετε τις λύσεις αναζήτησής σας.

Για περαιτέρω βοήθεια, επισκεφθείτε την [τεκμηρίωση Azure Cognitive Search](https://learn.microsoft.com/en-us/azure/search/?wt.mc_id=studentamb_258691).

**Αποποίηση ευθυνών**:  
Αυτό το έγγραφο έχει μεταφραστεί χρησιμοποιώντας την υπηρεσία αυτόματης μετάφρασης AI [Co-op Translator](https://github.com/Azure/co-op-translator). Παρόλο που επιδιώκουμε την ακρίβεια, παρακαλούμε να γνωρίζετε ότι οι αυτόματες μεταφράσεις ενδέχεται να περιέχουν λάθη ή ανακρίβειες. Το πρωτότυπο έγγραφο στη γλώσσα του θεωρείται η αυθεντική πηγή. Για κρίσιμες πληροφορίες, συνιστάται επαγγελματική ανθρώπινη μετάφραση. Δεν φέρουμε ευθύνη για τυχόν παρεξηγήσεις ή λανθασμένες ερμηνείες που προκύπτουν από τη χρήση αυτής της μετάφρασης.