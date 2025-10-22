<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "9bf0395cbc541ce8db2a9699c8678dfc",
  "translation_date": "2025-08-29T16:08:33+00:00",
  "source_file": "11-agentic-protocols/code_samples/github-mcp/README.md",
  "language_code": "el"
}
-->
# Παράδειγμα Github MCP Server

## Περιγραφή

Αυτό ήταν ένα demo που δημιουργήθηκε για το Hackathon AI Agents που φιλοξενήθηκε μέσω του Microsoft Reactor.

Το εργαλείο χρησιμοποιείται για να προτείνει έργα hackathon με βάση τα repos του χρήστη στο Github. Αυτό γίνεται μέσω:

1. **Github Agent** - Χρησιμοποιώντας τον Github MCP Server για την ανάκτηση repos και πληροφοριών σχετικά με αυτά.
2. **Hackathon Agent** - Παίρνει τα δεδομένα από τον Github Agent και προτείνει δημιουργικές ιδέες για έργα hackathon με βάση τα έργα, τις γλώσσες που χρησιμοποιεί ο χρήστης και τις θεματικές ενότητες του hackathon AI Agents.
3. **Events Agent** - Με βάση την πρόταση του Hackathon Agent, ο Events Agent θα προτείνει σχετικά γεγονότα από τη σειρά AI Agent Hackathon.

## Εκτέλεση του κώδικα 

### Μεταβλητές Περιβάλλοντος

Αυτό το demo χρησιμοποιεί το Azure Open AI Service, το Semantic Kernel, τον Github MCP Server και το Azure AI Search.

Βεβαιωθείτε ότι έχετε ορίσει τις κατάλληλες μεταβλητές περιβάλλοντος για να χρησιμοποιήσετε αυτά τα εργαλεία:

```python
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME=""
AZURE_OPENAI_EMBEDDING_DEPLOYMENT_NAME=""
AZURE_OPENAI_ENDPOINT=""
AZURE_OPENAI_API_KEY=""
AZURE_OPENAI_API_VERSION=""
AZURE_SEARCH_SERVICE_ENDPOINT=""
AZURE_SEARCH_API_KEY=""
``` 

## Εκτέλεση του Chainlit Server

Για να συνδεθείτε στον MCP server, αυτό το demo χρησιμοποιεί το Chainlit ως διεπαφή συνομιλίας.

Για να εκτελέσετε τον server, χρησιμοποιήστε την παρακάτω εντολή στο τερματικό σας:

```bash
chainlit run app.py -w
```

Αυτό θα ξεκινήσει τον Chainlit server στο `localhost:8000` και θα γεμίσει το Azure AI Search Index με το περιεχόμενο του `event-descriptions.md`.

## Σύνδεση με τον MCP Server

Για να συνδεθείτε στον Github MCP Server, επιλέξτε το εικονίδιο "plug" κάτω από το πλαίσιο συνομιλίας "Type your message here..":

![MCP Connect](../../../../../translated_images/mcp-chainlit-1.7ed66d648e3cfb28f1ea5f320b91e4404df4a24a0f236ce3de999666621f1cfc.el.png)

Από εκεί μπορείτε να κάνετε κλικ στο "Connect an MCP" για να προσθέσετε την εντολή σύνδεσης με τον Github MCP Server:

```bash
npx -y @modelcontextprotocol/server-github --env GITHUB_PERSONAL_ACCESS_TOKEN=[YOUR PERSONAL ACCESS TOKEN]
```

Αντικαταστήστε το "[YOUR PERSONAL ACCESS TOKEN]" με το πραγματικό σας Personal Access Token.

Μετά τη σύνδεση, θα πρέπει να δείτε ένα (1) δίπλα στο εικονίδιο plug για να επιβεβαιώσετε ότι έχει συνδεθεί. Αν όχι, δοκιμάστε να επανεκκινήσετε τον Chainlit server με `chainlit run app.py -w`.

## Χρήση του Demo 

Για να ξεκινήσετε τη ροή εργασίας του agent που προτείνει έργα hackathon, μπορείτε να πληκτρολογήσετε ένα μήνυμα όπως:

"Πρότεινε έργα hackathon για τον χρήστη Github koreyspace"

Ο Router Agent θα αναλύσει το αίτημά σας και θα καθορίσει ποιος συνδυασμός agents (GitHub, Hackathon και Events) είναι ο πιο κατάλληλος για να χειριστεί το ερώτημά σας. Οι agents συνεργάζονται για να παρέχουν ολοκληρωμένες προτάσεις με βάση την ανάλυση των repos του Github, τη δημιουργία ιδεών για έργα και σχετικά τεχνολογικά γεγονότα.

---

**Αποποίηση ευθύνης**:  
Αυτό το έγγραφο έχει μεταφραστεί χρησιμοποιώντας την υπηρεσία αυτόματης μετάφρασης [Co-op Translator](https://github.com/Azure/co-op-translator). Παρόλο που καταβάλλουμε προσπάθειες για ακρίβεια, παρακαλούμε να έχετε υπόψη ότι οι αυτοματοποιημένες μεταφράσεις ενδέχεται να περιέχουν σφάλματα ή ανακρίβειες. Το πρωτότυπο έγγραφο στη μητρική του γλώσσα θα πρέπει να θεωρείται η αυθεντική πηγή. Για κρίσιμες πληροφορίες, συνιστάται επαγγελματική ανθρώπινη μετάφραση. Δεν φέρουμε ευθύνη για τυχόν παρεξηγήσεις ή εσφαλμένες ερμηνείες που προκύπτουν από τη χρήση αυτής της μετάφρασης.