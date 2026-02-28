# Παράδειγμα Github MCP Server

## Περιγραφή

Αυτή ήταν μια επίδειξη που δημιουργήθηκε για το Hackathon AI Agents που διοργανώθηκε μέσω του Microsoft Reactor.

Το εργαλείο χρησιμοποιείται για να προτείνει έργα hackathon με βάση τα αποθετήρια Github ενός χρήστη.
Αυτό γίνεται με:

1. **Github Agent** - Χρήση του Github MCP Server για την ανάκτηση αποθετηρίων και πληροφοριών για αυτά τα αποθετήρια.
2. **Hackathon Agent** - Λαμβάνει τα δεδομένα από τον Github Agent και προτείνει δημιουργικές ιδέες έργων για το hackathon βάσει των έργων, των γλωσσών που χρησιμοποιεί ο χρήστης και των κατηγοριών έργων για το Hackathon AI Agents.
3. **Events Agent** - Βάσει της πρότασης του hackathon agent, ο events agent θα προτείνει σχετικές εκδηλώσεις από τη σειρά Hackathon AI Agent.
## Εκτέλεση του κώδικα 

### Μεταβλητές περιβάλλοντος

Αυτή η επίδειξη χρησιμοποιεί το Microsoft Agent Framework, το Azure OpenAI Service, τον Github MCP Server και το Azure AI Search.

Βεβαιωθείτε ότι έχετε ορίσει τις κατάλληλες μεταβλητές περιβάλλοντος για να χρησιμοποιήσετε αυτά τα εργαλεία:

```python
AZURE_AI_PROJECT_ENDPOINT=""
AZURE_AI_MODEL_DEPLOYMENT_NAME=""
AZURE_SEARCH_SERVICE_ENDPOINT=""
AZURE_SEARCH_API_KEY=""
``` 

## Εκτέλεση του Chainlit Server

Για να συνδεθείτε με τον MCP server, αυτή η επίδειξη χρησιμοποιεί το Chainlit ως διεπαφή συνομιλίας. 

Για να τρέξετε τον διακομιστή, χρησιμοποιήστε την ακόλουθη εντολή στο τερματικό σας:

```bash
chainlit run app.py -w
```

Αυτό θα ξεκινήσει τον Chainlit server σας στο `localhost:8000` καθώς και θα γεμίσει το Azure AI Search Index σας με το περιεχόμενο του `event-descriptions.md`. 

## Σύνδεση με τον MCP Server

Για να συνδεθείτε με τον Github MCP Server, επιλέξτε το εικονίδιο "plug" κάτω από το πλαίσιο συνομιλίας "Type your message here..":

![Σύνδεση MCP](../../../../../translated_images/el/mcp-chainlit-1.7ed66d648e3cfb28.webp)

Από εκεί μπορείτε να κάνετε κλικ στο "Connect an MCP" για να προσθέσετε την εντολή για σύνδεση με τον Github MCP Server:

```bash
npx -y @modelcontextprotocol/server-github --env GITHUB_PERSONAL_ACCESS_TOKEN=[YOUR PERSONAL ACCESS TOKEN]
```

Replace "[YOUR PERSONAL ACCESS TOKEN]" with your actual Personal Access Token. 

Μετά τη σύνδεση, θα πρέπει να δείτε έναν (1) δίπλα στο εικονίδιο plug για να επιβεβαιώσετε ότι είναι συνδεδεμένο. Αν όχι, δοκιμάστε να επανεκκινήσετε τον chainlit server με `chainlit run app.py -w`.

## Χρήση της επίδειξης 

Για να ξεκινήσετε τη ροή εργασίας των πρακτόρων για την προτροπή έργων hackathon, μπορείτε να πληκτρολογήσετε ένα μήνυμα όπως: 

"Προτείνετε έργα hackathon για τον χρήστη Github koreyspace"

Ο Router Agent θα αναλύσει το αίτημά σας και θα καθορίσει ποιος συνδυασμός πρακτόρων (GitHub, Hackathon, και Events) είναι καταλληλότερος για να χειριστεί το ερώτημά σας. Οι πράκτορες συνεργάζονται για να παρέχουν ολοκληρωμένες προτάσεις βάσει ανάλυσης των αποθετηρίων GitHub, ιδεασμού έργων και σχετικών τεχνολογικών εκδηλώσεων.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
Αποποίηση ευθυνών:
Το παρόν έγγραφο έχει μεταφραστεί χρησιμοποιώντας την υπηρεσία αυτόματης μετάφρασης με τεχνητή νοημοσύνη Co-op Translator (https://github.com/Azure/co-op-translator). Αν και καταβάλλουμε προσπάθειες για ακρίβεια, παρακαλείστε να λάβετε υπόψη ότι οι αυτοματοποιημένες μεταφράσεις ενδέχεται να περιέχουν σφάλματα ή ανακρίβειες. Το αρχικό έγγραφο στη γλώσσα του πρέπει να θεωρείται η αυθεντική πηγή. Για κρίσιμες πληροφορίες συνιστάται επαγγελματική μετάφραση από άνθρωπο. Δεν φέρουμε καμία ευθύνη για τυχόν παρεξηγήσεις ή λανθασμένες ερμηνείες που προκύπτουν από τη χρήση αυτής της μετάφρασης.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->