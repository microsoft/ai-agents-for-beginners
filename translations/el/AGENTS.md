# AGENTS.md

## Επισκόπηση Έργου

Αυτό το αποθετήριο περιέχει "AI Agents για Αρχάριους" - ένα ολοκληρωμένο εκπαιδευτικό μάθημα που διδάσκει τα πάντα για την κατασκευή AI Agents. Το μάθημα αποτελείται από 18 μαθήματα (αριθμημένα 00-18) που καλύπτουν τα βασικά, τα μοτίβα σχεδίασης, τα frameworks, την παραγωγική ανάπτυξη, τους τοπικούς/ενσωματωμένους agents και την ασφάλεια των AI agents.

**Κύριες Τεχνολογίες:**
- Python 3.12+
- Jupyter Notebooks για διαδραστική εκμάθηση
- AI Frameworks: Microsoft Agent Framework (MAF)
- Υπηρεσίες AI Azure: Microsoft Foundry, Microsoft Foundry Agent Service V2

**Αρχιτεκτονική:**
- Δομή βάσει μαθημάτων (φάκελοι 00-18)
- Κάθε μάθημα περιέχει: τεκμηρίωση README, δείγματα κώδικα (Jupyter notebooks) και εικόνες
- Υποστήριξη πολλαπλών γλωσσών μέσω αυτοματοποιημένου συστήματος μετάφρασης
- Ένα Jupyter notebook ανά μάθημα που χρησιμοποιεί το Microsoft Agent Framework

## Εντολές Ρύθμισης

### Προαπαιτούμενα
- Python 3.12 ή νεότερη έκδοση
- Συνδρομή Azure (για Microsoft Foundry)
- Εγκατεστημένο και αυθεντικοποιημένο Azure CLI (`az login`)

### Αρχική Ρύθμιση

1. **Κλωνοποιήστε ή κάντε fork το αποθετήριο:**
   ```bash
   gh repo fork microsoft/ai-agents-for-beginners --clone
   # OR
   git clone https://github.com/microsoft/ai-agents-for-beginners.git
   cd ai-agents-for-beginners
   ```

2. **Δημιουργήστε και ενεργοποιήστε εικονικό περιβάλλον Python:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Εγκαταστήστε τις εξαρτήσεις:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Ρυθμίστε τις μεταβλητές περιβάλλοντος:**
   ```bash
   cp .env.example .env
   # Edit .env with your API keys and endpoints
   ```

### Απαραίτητες Μεταβλητές Περιβάλλοντος

Για **Microsoft Foundry** (Απαραίτητο):
- `AZURE_AI_PROJECT_ENDPOINT` - Τελικό σημείο έργου Microsoft Foundry
- `AZURE_AI_MODEL_DEPLOYMENT_NAME` - Όνομα ανάπτυξης μοντέλου (π.χ., gpt-5-mini)

Για **Azure AI Search** (Μάθημα 05 - RAG):
- `AZURE_SEARCH_SERVICE_ENDPOINT` - Τελικό σημείο Azure AI Search
- `AZURE_SEARCH_API_KEY` - Κλειδί API Azure AI Search

Αυθεντικοποίηση: Εκτελέστε `az login` πριν τρέξετε τα notebooks (χρησιμοποιεί `AzureCliCredential`).

## Ροή Εργασίας Ανάπτυξης

### Εκτέλεση Jupyter Notebooks

Κάθε μάθημα περιέχει πολλαπλά Jupyter notebooks για διαφορετικά frameworks:

1. **Ξεκινήστε το Jupyter:**
   ```bash
   jupyter notebook
   ```

2. **Πλοηγηθείτε σε φάκελο μαθήματος** (π.χ., `01-intro-to-ai-agents/code_samples/`)

3. **Ανοίξτε και εκτελέστε τα notebooks:**
   - `*-python-agent-framework.ipynb` - Με χρήση Microsoft Agent Framework (Python)
   - `*-dotnet-agent-framework.ipynb` - Με χρήση Microsoft Agent Framework (.NET)

### Χρήση του Microsoft Agent Framework

**Microsoft Agent Framework + Microsoft Foundry:**
- Απαιτεί συνδρομή Azure
- Χρησιμοποιεί `FoundryChatClient` για Agent Service V2 (agents ορατοί στο portal του Foundry)
- Έτοιμο για παραγωγή με ενσωματωμένη παρακολούθηση
- Μοτίβο αρχείου: `*-python-agent-framework.ipynb`

## Οδηγίες Δοκιμών

Αυτό είναι εκπαιδευτικό αποθετήριο με παραδείγματα κώδικα και όχι παραγωγικός κώδικας με αυτόματες δοκιμές. Για να επαληθεύσετε τη ρύθμισή σας και αλλαγές:

### Χειροκίνητες Δοκιμές

1. **Δοκιμάστε το περιβάλλον Python:**
   ```bash
   python --version  # Should be 3.12+
   pip list | grep -E "(agent-framework|azure-ai|azure-identity)"
   ```

2. **Δοκιμάστε την εκτέλεση notebook:**
   ```bash
   # Convert notebook to script and run (tests imports)
   jupyter nbconvert --to script <lesson-folder>/code_samples/<notebook>.ipynb --stdout | python
   ```

3. **Επαληθεύστε τις μεταβλητές περιβάλλοντος:**
   ```bash
   python -c "import os; from dotenv import load_dotenv; load_dotenv(); print('✓ AZURE_AI_PROJECT_ENDPOINT' if os.getenv('AZURE_AI_PROJECT_ENDPOINT') else '✗ AZURE_AI_PROJECT_ENDPOINT missing')"
   ```

### Εκτέλεση Ατομικών Notebooks

Ανοίξτε notebooks στο Jupyter και εκτελέστε τα κελιά διαδοχικά. Κάθε notebook είναι αυτοτελές και περιλαμβάνει:
- Δηλώσεις import
- Φόρτωση ρυθμίσεων
- Παραδείγματα υλοποίησης agent
- Προβλεπόμενα αποτελέσματα σε κελιά markdown

### Smoke-Test Διεξαγωγή για Αναπτυγμένους Agents

Για μαθήματα όπου ένας agent αναπτύσσεται ως Microsoft Foundry hosted agent (01, 04, 05, 16), το αποθετήριο περιλαμβάνει smoke-test καταλόγους κάτω από `tests/` που εκτελούνται από το `.github/workflows/smoke-test.yml` workflow μέσω της ενέργειας [AI Smoke Test](https://github.com/marketplace/actions/ai-smoke-test). Αυτά λειτουργούν ως ελαφριά πύλη μετά την ανάπτυξη (είναι ο agent προσβάσιμος και ακολουθεί βασικές προσδοκίες prompt;), συμπληρώνοντας τη διαδικασία αξιολόγησης στα Μαθήματα 10 και 16. Δείτε το [tests/README.md](./tests/README.md) για τη χαρτογράφηση καταλόγου-μαθήματος-agent. Το Μάθημα 17 τρέχει τοπικά με Foundry Local και δεν έχει hosted endpoint, οπότε επαληθεύεται εκτελώντας απευθείας το notebook του.

## Στυλ Κώδικα

### Συμβάσεις Python

- **Έκδοση Python**: 3.12+
- **Στυλ Κώδικα**: Ακολουθήστε τα τυπικά πρότυπα Python PEP 8
- **Notebooks**: Χρησιμοποιήστε καθαρά κελιά markdown για εξήγηση εννοιών
- **Imports**: Ομαδοποιήστε κατά standard library, τρίτους, τοπικά imports

### Συμβάσεις Jupyter Notebook

- Συμπεριλάβετε περιγραφικά κελιά markdown πριν τα κελιά κώδικα
- Προσθέστε παραδείγματα εξόδου στα notebooks για αναφορά
- Χρησιμοποιήστε καθαρά ονόματα μεταβλητών που ταιριάζουν με τις έννοιες του μαθήματος
- Διατηρήστε γραμμική σειρά εκτέλεσης notebook (κελί 1 → 2 → 3...)

### Οργάνωση Αρχείων

```
<lesson-number>-<lesson-name>/
├── README.md                     # Lesson documentation
├── code_samples/
│   ├── <number>-python-agent-framework.ipynb
│   └── <number>-dotnet-agent-framework.ipynb  (optional)
└── images/
    └── *.png
```

## Κατασκευή και Ανάπτυξη

### Κατασκευή Τεκμηρίωσης

Αυτό το αποθετήριο χρησιμοποιεί Markdown για τεκμηρίωση:
- Αρχεία README.md σε κάθε φάκελο μαθήματος
- Κεντρικό README.md στη ρίζα αποθετηρίου
- Αυτοματοποιημένο σύστημα μετάφρασης μέσω GitHub Actions

### CI/CD Pipeline

Βρίσκεται στο `.github/workflows/`:

1. **co-op-translator.yml** - Αυτόματη μετάφραση σε 50+ γλώσσες
2. **welcome-issue.yml** - Καλωσορίζει νέους δημιουργούς ζητημάτων
3. **welcome-pr.yml** - Καλωσορίζει νέους συνεισφέροντες pull requests

### Ανάπτυξη

Αυτό είναι εκπαιδευτικό αποθετήριο - δεν υπάρχει διαδικασία ανάπτυξης. Οι χρήστες:
1. Κάνουν fork ή κλωνοποιούν το αποθετήριο
2. Τρέχουν notebooks τοπικά ή σε GitHub Codespaces
3. Μαθαίνουν τροποποιώντας και πειραματιζόμενοι με παραδείγματα

## Οδηγίες Pull Request

### Πριν την Υποβολή

1. **Δοκιμάστε τις αλλαγές σας:**
   - Τρέξτε πλήρως τα επηρεασμένα notebooks
   - Επαληθεύστε ότι όλα τα κελιά εκτελούνται χωρίς σφάλματα
   - Ελέγξτε αν οι έξοδοι είναι κατάλληλες

2. **Ενημερώσεις τεκμηρίωσης:**
   - Ενημερώστε το README.md αν προσθέτετε νέες έννοιες
   - Προσθέστε σχόλια στα notebooks για πολύπλοκο κώδικα
   - Βεβαιωθείτε ότι τα markdown κελιά εξηγούν τον σκοπό τους

3. **Αλλαγές αρχείων:**
   - Αποφύγετε την υποβολή `.env` αρχείων (χρησιμοποιήστε `.env.example`)
   - Μην κάνετε commit τους φακέλους `venv/` ή `__pycache__/`
   - Διατηρήστε τις εξόδους notebooks όταν δείχνουν έννοιες
   - Αφαιρέστε προσωρινά αρχεία και αντίγραφα ασφαλείας notebooks (`*-backup.ipynb`)

### Μορφή Τίτλου PR

Χρησιμοποιήστε περιγραφικούς τίτλους:
- `[Lesson-XX] Add new example for <concept>`
- `[Fix] Correct typo in lesson-XX README`
- `[Update] Improve code sample in lesson-XX`
- `[Docs] Update setup instructions`

### Απαιτούμενοι Έλεγχοι

- Τα notebooks πρέπει να εκτελούνται χωρίς σφάλματα
- Τα αρχεία README πρέπει να είναι σαφή και ακριβή
- Ακολουθήστε υπάρχοντα μοτίβα κώδικα στο αποθετήριο
- Διατηρήστε συνέπεια με άλλα μαθήματα

## Πρόσθετες Σημειώσεις

### Συχνά Προβλήματα

1. **Ασυμφωνία έκδοσης Python:**
   - Βεβαιωθείτε ότι χρησιμοποιείται Python 3.12+
   - Μερικά πακέτα ενδέχεται να μην λειτουργούν σε παλαιότερες εκδόσεις
   - Χρησιμοποιήστε `python3 -m venv` για να καθορίσετε ρητά την έκδοση Python

2. **Μεταβλητές περιβάλλοντος:**
   - Πάντα να δημιουργείτε `.env` από `.env.example`
   - Μην κάνετε commit το αρχείο `.env` (είναι σε `.gitignore`)
   - Συνδεθείτε με `az login` για αυθεντικοποίηση Entra ID χωρίς κλειδί

3. **Σύγκρουση πακέτων:**
   - Χρησιμοποιήστε φρέσκο εικονικό περιβάλλον
   - Εγκαταστήστε από `requirements.txt` αντί για μεμονωμένα πακέτα
   - Ορισμένα notebooks ενδέχεται να απαιτούν επιπλέον πακέτα που αναφέρονται στα markdown κελιά τους

4. **Υπηρεσίες Azure:**
   - Οι υπηρεσίες Azure AI απαιτούν ενεργή συνδρομή
   - Ορισμένα χαρακτηριστικά είναι συγκεκριμένα ανά περιοχή
   - Βεβαιωθείτε ότι η ανάπτυξη μοντέλου Azure OpenAI υποστηρίζει το Responses API

### Διαδρομή Μάθησης

Συνιστώμενη προοδευτική σειρά μαθημάτων:
1. **00-course-setup** - Ξεκινήστε εδώ για ρύθμιση περιβάλλοντος
2. **01-intro-to-ai-agents** - Κατανοήστε τα βασικά των AI agents
3. **02-explore-agentic-frameworks** - Μάθετε για διάφορα frameworks
4. **03-agentic-design-patterns** - Βασικά μοτίβα σχεδίασης
5. Συνεχίστε διαδοχικά στα αριθμημένα μαθήματα

### Επιλογή Framework

Επιλέξτε framework βασισμένο στους στόχους σας:
- **Όλα τα μαθήματα**: Microsoft Agent Framework (MAF) με `FoundryChatClient`
- **Οι agents εγγράφονται server-side** στη Microsoft Foundry Agent Service V2 και είναι ορατοί στο portal Foundry

### Λήψη Βοήθειας

- Ενταχθείτε στο [Microsoft Foundry Community Discord](https://aka.ms/ai-agents/discord)
- Εξετάστε τα αρχεία README των μαθημάτων για συγκεκριμένες οδηγίες
- Ελέγξτε το κύριο [README.md](./README.md) για επισκόπηση μαθήματος
- Ανατρέξτε στον [Course Setup](./00-course-setup/README.md) για λεπτομερείς οδηγίες ρύθμισης

### Συνεισφορά

Αυτό είναι ένα ανοιχτό εκπαιδευτικό έργο. Καλώς δεχούνται συνεισφορές:
- Βελτίωση παραδειγμάτων κώδικα
- Διόρθωση ορθογραφικών ή λαθών
- Προσθήκη διευκρινιστικών σχολίων
- Πρόταση θεμάτων για νέα μαθήματα
- Μετάφραση σε επιπλέον γλώσσες

Δείτε τα [GitHub Issues](https://github.com/microsoft/ai-agents-for-beginners/issues) για τρέχουσες ανάγκες.

## Συγκεκριμένο Πλαίσιο Έργου

### Υποστήριξη Πολλαπλών Γλωσσών

Αυτό το αποθετήριο χρησιμοποιεί αυτοματοποιημένο σύστημα μετάφρασης:
- Υποστήριξη 50+ γλωσσών
- Μεταφράσεις σε `/translations/<lang-code>/` φακέλους
- Το workflow GitHub Actions διαχειρίζεται ενημερώσεις μετάφρασης
- Τα αρχεία πηγής είναι στα Αγγλικά στη ρίζα του αποθετηρίου

### Δομή Μαθήματος

Κάθε μάθημα ακολουθεί ένα σταθερό μοτίβο:
1. Μικρογραφία βίντεο με σύνδεσμο
2. Γραπτό περιεχόμενο μαθήματος (README.md)
3. Παραδείγματα κώδικα σε πολλά frameworks
4. Στόχοι μάθησης και προαπαιτούμενα
5. Επιπλέον πόροι μάθησης με συνδέσμους

### Ονομασία Δειγμάτων Κώδικα

Μορφή: `<lesson-number>-python-agent-framework.ipynb`
- `01-python-agent-framework.ipynb` - Μάθημα 1, MAF Python
- `14-sequential.ipynb` - Μάθημα 14, Προχωρημένα μοτίβα MAF
- `16-python-agent-framework.ipynb` - Μάθημα 16, παραγωγικός agent υποστήριξης πελατών
- `17-local-agent-foundry-local.ipynb` - Μάθημα 17, τοπικός agent με Foundry Local + Qwen

### Ειδικοί Φάκελοι

- `translated_images/` - Τοπικές εικόνες για μεταφράσεις
- `images/` - Πρωτότυπες εικόνες για αγγλικό περιεχόμενο
- `.devcontainer/` - Ρυθμίσεις κοντέινερ ανάπτυξης VS Code
- `.github/` - Workflows και πρότυπα GitHub Actions

### Εξαρτήσεις

Κύρια πακέτα από `requirements.txt`:
- `agent-framework` - Microsoft Agent Framework
- `a2a-sdk` - Υποστήριξη πρωτοκόλλου Agent-to-Agent
- `azure-ai-inference`, `azure-ai-projects` - Υπηρεσίες Azure AI
- `azure-identity` - Αυθεντικοποίηση Azure (AzureCliCredential)
- `azure-search-documents` - Ενσωμάτωση Azure AI Search
- `mcp[cli]` - Υποστήριξη Πρωτοκόλλου Context Model

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Αποποίηση ευθυνών**:
Αυτό το έγγραφο έχει μεταφραστεί χρησιμοποιώντας την υπηρεσία μετάφρασης με τεχνητή νοημοσύνη [Co-op Translator](https://github.com/Azure/co-op-translator). Ενώ επιδιώκουμε την ακρίβεια, παρακαλούμε να έχετε υπόψη ότι οι αυτοματοποιημένες μεταφράσεις ενδέχεται να περιέχουν λάθη ή ανακρίβειες. Το πρωτότυπο έγγραφο στη μητρική του γλώσσα πρέπει να θεωρείται η αυθεντική πηγή. Για κρίσιμες πληροφορίες, συνιστάται επαγγελματική ανθρώπινη μετάφραση. Δεν φέρουμε ευθύνη για τυχόν παρεξηγήσεις ή λανθασμένες ερμηνείες που προκύπτουν από τη χρήση αυτής της μετάφρασης.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->