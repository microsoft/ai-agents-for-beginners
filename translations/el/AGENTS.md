# AGENTS.md

## Επισκόπηση Έργου

Αυτό το αποθετήριο περιέχει "AI Agents για Αρχάριους" - ένα ολοκληρωμένο εκπαιδευτικό μάθημα που διδάσκει τα πάντα για την κατασκευή AI Agents. Το μάθημα περιλαμβάνει πάνω από 15 μαθήματα που καλύπτουν βασικές έννοιες, σχεδιαστικά μοτίβα, frameworks, και την παραγωγική ανάπτυξη των AI agents.

**Κύριες Τεχνολογίες:**
- Python 3.12+
- Jupyter Notebooks για διαδραστική μάθηση
- AI Frameworks: Microsoft Agent Framework (MAF)
- Azure AI Services: Microsoft Foundry, Azure AI Foundry Agent Service V2

**Αρχιτεκτονική:**
- Δομή με μαθήματα (φάκελοι 00-15+)
- Κάθε μάθημα περιλαμβάνει: τεκμηρίωση README, δείγματα κώδικα (Jupyter notebooks), και εικόνες
- Υποστήριξη πολλαπλών γλωσσών μέσω συστήματος αυτόματης μετάφρασης
- Ένα Python notebook ανά μάθημα που χρησιμοποιεί το Microsoft Agent Framework

## Εντολές Ρύθμισης

### Προαπαιτούμενα
- Python 3.12 ή νεότερη
- Συνδρομή Azure (για Azure AI Foundry)
- Εγκατεστημένο και αυθεντικοποιημένο Azure CLI (`az login`)

### Αρχική Ρύθμιση

1. **Κλωνοποίηση ή fork του αποθετηρίου:**
   ```bash
   gh repo fork microsoft/ai-agents-for-beginners --clone
   # Ή
   git clone https://github.com/microsoft/ai-agents-for-beginners.git
   cd ai-agents-for-beginners
   ```

2. **Δημιουργία και ενεργοποίηση εικονικού περιβάλλοντος Python:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # Στα Windows: venv\Scripts\activate
   ```

3. **Εγκατάσταση εξαρτήσεων:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Ορισμός μεταβλητών περιβάλλοντος:**
   ```bash
   cp .env.example .env
   # Επεξεργαστείτε το .env με τα API κλειδιά και τα τελικά σημεία σας
   ```

### Απαιτούμενες Μεταβλητές Περιβάλλοντος

Για **Azure AI Foundry** (Απαραίτητο):
- `AZURE_AI_PROJECT_ENDPOINT` - Endpoint του έργου Azure AI Foundry
- `AZURE_AI_MODEL_DEPLOYMENT_NAME` - Όνομα ανάπτυξης μοντέλου (π.χ., gpt-4o)

Για **Azure AI Search** (Μάθημα 05 - RAG):
- `AZURE_SEARCH_SERVICE_ENDPOINT` - Endpoint Azure AI Search
- `AZURE_SEARCH_API_KEY` - Κλειδί API Azure AI Search

Αυθεντικοποίηση: Εκτελέστε `az login` πριν τρέξετε τα notebooks (χρησιμοποιεί `AzureCliCredential`).

## Ροή Ανάπτυξης

### Εκτέλεση Jupyter Notebooks

Κάθε μάθημα περιέχει πολλαπλά Jupyter notebooks για διαφορετικά frameworks:

1. **Εκκίνηση Jupyter:**
   ```bash
   jupyter notebook
   ```

2. **Πλοήγηση σε φάκελο μαθήματος** (π.χ., `01-intro-to-ai-agents/code_samples/`)

3. **Άνοιγμα και εκτέλεση notebooks:**
   - `*-python-agent-framework.ipynb` - Χρήση Microsoft Agent Framework (Python)
   - `*-dotnet-agent-framework.ipynb` - Χρήση Microsoft Agent Framework (.NET)

### Εργασία με Microsoft Agent Framework

**Microsoft Agent Framework + Azure AI Foundry:**
- Απαιτεί συνδρομή Azure
- Χρησιμοποιεί `AzureAIProjectAgentProvider` για Agent Service V2 (agents ορατοί στο Foundry portal)
- Έτοιμο για παραγωγή με ενσωματωμένη παρατηρησιμότητα
- Μοτίβο αρχείων: `*-python-agent-framework.ipynb`

## Οδηγίες Δοκιμών

Αυτό είναι ένα εκπαιδευτικό αποθετήριο με παραδείγματα κώδικα και όχι παραγωγικό κώδικα με αυτοματοποιημένες δοκιμές. Για να επαληθεύσετε τη ρύθμιση και τις αλλαγές σας:

### Χειροκίνητη Δοκιμή

1. **Ελέγξτε το περιβάλλον Python:**
   ```bash
   python --version  # Πρέπει να είναι 3.12+
   pip list | grep -E "(agent-framework|azure-ai|azure-identity)"
   ```

2. **Ελέγξτε την εκτέλεση του notebook:**
   ```bash
   # Μετατροπή του notebook σε script και εκτέλεση (ελέγχει τις εισαγωγές)
   jupyter nbconvert --to script <lesson-folder>/code_samples/<notebook>.ipynb --stdout | python
   ```

3. **Επαληθεύστε τις μεταβλητές περιβάλλοντος:**
   ```bash
   python -c "import os; from dotenv import load_dotenv; load_dotenv(); print('✓ GITHUB_TOKEN' if os.getenv('GITHUB_TOKEN') else '✗ GITHUB_TOKEN missing')"
   ```

### Εκτέλεση Ατομικών Notebooks

Ανοίξτε τα notebooks σε Jupyter και εκτελέστε τα κελιά διαδοχικά. Κάθε notebook είναι αυτόνομο και περιλαμβάνει:
- Δηλώσεις εισαγωγής
- Φόρτωση ρυθμίσεων
- Παραδείγματα υλοποίησης agents
- Αναμενόμενα αποτελέσματα σε markdown κελιά

## Στυλ Κώδικα

### Συμβάσεις Python

- **Έκδοση Python**: 3.12+
- **Στυλ Κώδικα**: Τήρηση τυπικών συμβάσεων Python PEP 8
- **Notebooks**: Χρήση σαφών markdown κελιών για εξήγηση εννοιών
- **Εισαγωγές**: Ομαδοποίηση κατά βιβλιοθήκες standard, τρίτων, τοπικές

### Συμβάσεις Jupyter Notebook

- Συμπερίληψη περιγραφικών markdown κελιών πριν από τα κελιά κώδικα
- Προσθήκη παραδειγμάτων εξόδου στα notebooks για αναφορά
- Χρήση σαφών ονομάτων μεταβλητών που ταιριάζουν με τις έννοιες του μαθήματος
- Γραμμική εκτέλεση κελιών (κελί 1 → 2 → 3...)

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

### Δημιουργία Τεκμηρίωσης

Αυτό το αποθετήριο χρησιμοποιεί Markdown για τεκμηρίωση:
- Αρχεία README.md σε κάθε φάκελο μαθήματος
- Κύριο README.md στη ρίζα του αποθετηρίου
- Σύστημα αυτόματης μετάφρασης μέσω GitHub Actions

### CI/CD Pipeline

Βρίσκεται στο `.github/workflows/`:

1. **co-op-translator.yml** - Αυτόματη μετάφραση σε 50+ γλώσσες
2. **welcome-issue.yml** - Καλωσορίζει νέους δημιουργούς θεμάτων
3. **welcome-pr.yml** - Καλωσορίζει νέους συνεργάτες pull request

### Ανάπτυξη

Αυτό είναι εκπαιδευτικό αποθετήριο - δεν υπάρχει διαδικασία ανάπτυξης. Οι χρήστες:
1. Κλωνοποιούν ή κάνουν fork το αποθετήριο
2. Τρέχουν τα notebooks τοπικά ή σε GitHub Codespaces
3. Μαθαίνουν τροποποιώντας και πειραματιζόμενοι με παραδείγματα

## Οδηγίες Pull Request

### Πριν την Υποβολή

1. **Δοκιμάστε τις αλλαγές σας:**
   - Τρέξτε πλήρως τα notebooks που επηρεάζονται
   - Επαληθεύστε ότι όλα τα κελιά εκτελούνται χωρίς σφάλματα
   - Ελέγξτε αν οι έξοδοι είναι κατάλληλες

2. **Ενημερώσεις τεκμηρίωσης:**
   - Ενημερώστε το README.md αν προσθέτετε νέες έννοιες
   - Προσθέστε σχόλια στα notebooks για σύνθετο κώδικα
   - Βεβαιωθείτε ότι τα markdown κελιά εξηγούν το σκοπό

3. **Αλλαγές αρχείων:**
   - Αποφύγετε την υποβολή αρχείων `.env` (χρησιμοποιείτε `.env.example`)
   - Μην υποβάλετε φακέλους `venv/` ή `__pycache__/`
   - Διατηρήστε τις εξόδους notebooks όταν δείχνουν έννοιες
   - Αφαιρέστε προσωρινά αρχεία και backup notebooks (`*-backup.ipynb`)

### Μορφή Τίτλου PR

Χρησιμοποιήστε περιγραφικούς τίτλους:
- `[Lesson-XX] Προσθήκη νέου παραδείγματος για <έννοια>`
- `[Fix] Διόρθωση ορθογραφικού λάθους στο lesson-XX README`
- `[Update] Βελτίωση δείγματος κώδικα στο lesson-XX`
- `[Docs] Ενημέρωση οδηγιών setup`

### Απαιτούμενοι Έλεγχοι

- Τα notebooks πρέπει να εκτελούνται χωρίς σφάλματα
- Τα αρχεία README πρέπει να είναι σαφή και ακριβή
- Ακολουθείτε υπάρχοντα πρότυπα κώδικα στο αποθετήριο
- Διατηρείτε συνοχή με τα άλλα μαθήματα

## Επιπλέον Σημειώσεις

### Συχνά Σφάλματα

1. **Μη συμβατή έκδοση Python:**
   - Χρησιμοποιήστε Python 3.12+
   - Ορισμένα πακέτα ίσως δεν λειτουργούν σε παλαιότερες εκδόσεις
   - Χρησιμοποιήστε `python3 -m venv` για να ορίσετε ρητά την έκδοση Python

2. **Μεταβλητές περιβάλλοντος:**
   - Πάντα δημιουργείτε `.env` από `.env.example`
   - Μην υποβάλετε το αρχείο `.env` (βρίσκεται στο `.gitignore`)
   - Το GitHub token χρειάζεται κατάλληλες άδειες

3. **Συγκρούσεις πακέτων:**
   - Χρησιμοποιήστε καθαρό εικονικό περιβάλλον
   - Εγκαταστήστε από `requirements.txt` αντί για μεμονωμένα πακέτα
   - Ορισμένα notebooks μπορεί να απαιτούν επιπλέον πακέτα που αναφέρονται στα markdown κελιά τους

4. **Υπηρεσίες Azure:**
   - Οι υπηρεσίες Azure AI απαιτούν ενεργή συνδρομή
   - Ορισμένα χαρακτηριστικά είναι περιορισμένα ανά περιοχή
   - Ισχύουν περιορισμοί δωρεάν επιπέδου για GitHub Models

### Μονοπάτι Μάθησης

Προτεινόμενη σειρά μαθημάτων:
1. **00-course-setup** - Ξεκινήστε εδώ για ρύθμιση περιβάλλοντος
2. **01-intro-to-ai-agents** - Κατανόηση βασικών AI agents
3. **02-explore-agentic-frameworks** - Μάθετε για διάφορα frameworks
4. **03-agentic-design-patterns** - Βασικά σχεδιαστικά μοτίβα
5. Συνεχίστε με τα μαθήματα στη σειριακή σειρά

### Επιλογή Framework

Επιλέξτε framework ανάλογα με τους στόχους σας:
- **Όλα τα μαθήματα**: Microsoft Agent Framework (MAF) με `AzureAIProjectAgentProvider`
- **Οι agents εγγράφονται server-side** στο Azure AI Foundry Agent Service V2 και είναι ορατοί στο Foundry portal

### Λήψη Βοήθειας

- Εγγραφείτε στην κοινότητα [Microsoft Foundry Community Discord](https://aka.ms/ai-agents/discord)
- Αναθεωρήστε τα README των μαθημάτων για συγκεκριμένη καθοδήγηση
- Ελέγξτε το κύριο [README.md](./README.md) για επισκόπηση μαθήματος
- Ανατρέξτε στο [Course Setup](./00-course-setup/README.md) για λεπτομερείς οδηγίες ρύθμισης

### Συνεισφορά

Αυτό είναι ένα ανοικτό εκπαιδευτικό έργο. Οι συνεισφορές είναι ευπρόσδεκτες:
- Βελτίωση παραδειγμάτων κώδικα
- Διόρθωση ορθογραφικών ή λανθασμένων στοιχείων
- Προσθήκη σχολίων για διευκρίνιση
- Πρόταση νέων θεμάτων μαθημάτων
- Μεταφράσεις σε επιπλέον γλώσσες

Δείτε τα [GitHub Issues](https://github.com/microsoft/ai-agents-for-beginners/issues) για τρέχουσες ανάγκες.

## Πλαίσιο Έργου

### Υποστήριξη Πολλών Γλωσσών

Αυτό το αποθετήριο χρησιμοποιεί σύστημα αυτόματης μετάφρασης:
- Υποστηρίζονται 50+ γλώσσες
- Μεταφράσεις στους φακέλους `/translations/<lang-code>/`
- Το workflow GitHub Actions διαχειρίζεται τις ενημερώσεις μετάφρασης
- Τα αρχεία πηγής είναι στα Αγγλικά στη ρίζα του αποθετηρίου

### Δομή Μαθημάτων

Κάθε μάθημα ακολουθεί συνεπή πρότυπο:
1. Thumbnail βίντεο με σύνδεσμο
2. Γραπτό περιεχόμενο μαθήματος (README.md)
3. Δείγματα κώδικα σε πολλαπλά frameworks
4. Στόχοι μάθησης και προαπαιτούμενα
5. Επιπλέον συνδεδεμένοι πόροι μάθησης

### Ονομασία Δειγμάτων Κώδικα

Μορφή: `<lesson-number>-python-agent-framework.ipynb`
- `01-python-agent-framework.ipynb` - Μάθημα 1, MAF Python
- `14-sequential.ipynb` - Μάθημα 14, εξελιγμένα μοτίβα MAF

### Ειδικοί Φάκελοι

- `translated_images/` - Τοπικές εικόνες για μεταφράσεις
- `images/` - Αρχικές εικόνες αγγλικού περιεχομένου
- `.devcontainer/` - Ρυθμίσεις κοντέινερ ανάπτυξης VS Code
- `.github/` - Workflows και πρότυπα GitHub Actions

### Εξαρτήσεις

Βασικά πακέτα από `requirements.txt`:
- `agent-framework` - Microsoft Agent Framework
- `a2a-sdk` - Υποστήριξη Agent-to-Agent πρωτοκόλλου
- `azure-ai-inference`, `azure-ai-projects` - Υπηρεσίες Azure AI
- `azure-identity` - Ταυτοποίηση Azure (AzureCliCredential)
- `azure-search-documents` - Ενσωμάτωση Azure AI Search
- `mcp[cli]` - Υποστήριξη Model Context Protocol

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Αποποίηση Ευθυνών**:  
Αυτή η γλώσσα έχει μεταφραστεί χρησιμοποιώντας την υπηρεσία αυτόματης μετάφρασης AI [Co-op Translator](https://github.com/Azure/co-op-translator). Παρότι επιδιώκουμε την ακρίβεια, παρακαλούμε να έχετε υπόψη σας ότι οι αυτοματοποιημένες μεταφράσεις μπορεί να περιέχουν λάθη ή ανακρίβειες. Το πρωτότυπο έγγραφο στη γλώσσα της αρχικής του μορφής πρέπει να θεωρείται η αυθεντική πηγή. Για κρίσιμες πληροφορίες, συνιστάται επαγγελματική ανθρώπινη μετάφραση. Δεν φέρουμε ευθύνη για τυχόν παρεξηγήσεις ή λανθασμένες ερμηνείες που προκύπτουν από τη χρήση αυτής της μετάφρασης.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->