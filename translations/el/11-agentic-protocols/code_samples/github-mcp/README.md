# Παράδειγμα διακομιστή Github MCP

## Περιγραφή

Αυτή ήταν μια επίδειξη δημιουργημένη για το AI Agents Hackathon που διοργανώθηκε μέσω του Microsoft Reactor.

Τα εργαλεία χρησιμοποιούνται για να προτείνουν έργα για hackathon βάσει των αποθετηρίων Github ενός χρήστη.
Αυτό γίνεται με:

1. **Github Agent** - Χρησιμοποιώντας τον Github MCP Server για την ανάκτηση αποθετηρίων και πληροφοριών σχετικά με αυτά τα αποθετήρια.
2. **Hackathon Agent** - Λαμβάνει τα δεδομένα από τον Github Agent και δημιουργεί δημιουργικές ιδέες έργων για το hackathon βάσει των έργων, των γλωσσών που χρησιμοποιεί ο χρήστης και των κατηγοριών έργων για το AI Agents hackathon.
3. **Events Agent** - Βάσει της πρότασης του Hackathon Agent, ο Events Agent θα προτείνει σχετικές εκδηλώσεις από τη σειρά AI Agent Hackathon.
## Εκτέλεση του κώδικα 

### Μεταβλητές περιβάλλοντος

Αυτή η επίδειξη χρησιμοποιεί το Microsoft Agent Framework, την υπηρεσία Azure OpenAI, τον Github MCP Server και το Azure AI Search.

Βεβαιωθείτε ότι έχετε ορίσει τις κατάλληλες μεταβλητές περιβάλλοντος για να χρησιμοποιήσετε αυτά τα εργαλεία:

```python
AZURE_AI_PROJECT_ENDPOINT=""
AZURE_AI_MODEL_DEPLOYMENT_NAME=""
AZURE_SEARCH_SERVICE_ENDPOINT=""
AZURE_SEARCH_API_KEY=""
``` 

## Εκτέλεση του Chainlit Server

Για να συνδεθείτε στον MCP server, αυτή η επίδειξη χρησιμοποιεί το Chainlit ως διεπαφή chat. 

Για να εκτελέσετε τον server, χρησιμοποιήστε την ακόλουθη εντολή στο τερματικό σας:

```bash
chainlit run app.py -w
```

Αυτό θα πρέπει να ξεκινήσει τον Chainlit server σας στο `localhost:8000` καθώς και να γεμίσει τον Azure AI Search Index σας με το περιεχόμενο `event-descriptions.md`. 

## Σύνδεση στον MCP Server

Για να συνδεθείτε στον Github MCP Server, επιλέξτε το εικονίδιο "plug" κάτω από το πλαίσιο συνομιλίας "Type your message here..":

![Σύνδεση MCP](../../../../../translated_images/el/mcp-chainlit-1.7ed66d648e3cfb28.webp)

Από εκεί μπορείτε να κάνετε κλικ στο "Connect an MCP" για να προσθέσετε την εντολή για σύνδεση στον Github MCP Server:

```bash
npx -y @modelcontextprotocol/server-github --env GITHUB_PERSONAL_ACCESS_TOKEN=[YOUR PERSONAL ACCESS TOKEN]
```

Replace "[YOUR PERSONAL ACCESS TOKEN]" with your actual Personal Access Token. 

After connecting, you should see a (1) next to the plug icon to confirm that its connected. If not, try restarting the chainlit server with `chainlit run app.py -w`.

## Χρήση της επίδειξης 

Για να ξεκινήσετε τη ροή εργασίας των agents για την πρόταση έργων για hackathon, μπορείτε να πληκτρολογήσετε ένα μήνυμα όπως: 

"Recommend hackathon projects for the Github user koreyspace"

Ο Router Agent θα αναλύσει το αίτημά σας και θα καθορίσει ποιος συνδυασμός agents (GitHub, Hackathon, και Events) είναι πιο κατάλληλος για να χειριστεί το αίτημά σας. Οι agents συνεργάζονται για να παρέχουν ολοκληρωμένες προτάσεις βάσει της ανάλυσης αποθετηρίων GitHub, της ιδεοποίησης έργων και σχετικών τεχνικών εκδηλώσεων.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
Αποποίηση ευθυνών:
Αυτό το έγγραφο έχει μεταφραστεί με χρήση υπηρεσίας μετάφρασης τεχνητής νοημοσύνης [Co-op Translator](https://github.com/Azure/co-op-translator). Παρότι καταβάλλουμε προσπάθειες για την ακρίβεια, παρακαλούμε να λάβετε υπόψη ότι οι αυτοματοποιημένες μεταφράσεις ενδέχεται να περιέχουν σφάλματα ή ανακρίβειες. Το πρωτότυπο έγγραφο στη γλώσσα του πρέπει να θεωρείται η αυθεντική πηγή. Για κρίσιμες πληροφορίες, συνιστάται επαγγελματική μετάφραση από άνθρωπο. Δεν φέρουμε ευθύνη για τυχόν παρερμηνείες ή παρανοήσεις που προκύπτουν από τη χρήση αυτής της μετάφρασης.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->