# AGENTS.md

## Επισκόπηση έργου

Αυτό το αποθετήριο περιέχει "AI Agents για Αρχάριους" - ένα ολοκληρωμένο εκπαιδευτικό μάθημα που διδάσκει όλα όσα χρειάζεστε για να δημιουργήσετε AI Agents. Το μάθημα αποτελείται από 15+ μαθήματα που καλύπτουν τα βασικά, πρότυπα σχεδίασης, frameworks και ανάπτυξη σε παραγωγή των AI agents.

**Κύριες Τεχνολογίες:**
- Python 3.12+
- Jupyter Notebooks για διαδραστική μάθηση
- AI Frameworks: Microsoft Agent Framework (MAF)
- Υπηρεσίες Azure AI: Microsoft Foundry, Azure AI Foundry Agent Service V2

**Αρχιτεκτονική:**
- Δομή βασισμένη σε μαθήματα (κατάλογοι 00-15+)
- Κάθε μάθημα περιλαμβάνει: έγγραφα README, δείγματα κώδικα (Jupyter notebooks), και εικόνες
- Υποστήριξη πολλαπλών γλωσσών μέσω αυτοματοποιημένου συστήματος μετάφρασης
- Ένα Python notebook ανά μάθημα που χρησιμοποιεί το Microsoft Agent Framework

## Εντολές Εγκατάστασης

### Απαιτήσεις
- Python 3.12 ή νεότερη
- Συνδρομή Azure (για Azure AI Foundry)
- Εγκατεστημένο και επαληθευμένο Azure CLI (`az login`)

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
   source venv/bin/activate  # Σε Windows: venv\Scripts\activate
   ```

3. **Εγκατάσταση εξαρτήσεων:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Ρύθμιση μεταβλητών περιβάλλοντος:**
   ```bash
   cp .env.example .env
   # Επεξεργαστείτε το .env με τα κλειδιά API και τα endpoints σας
   ```

### Απαιτούμενες Μεταβλητές Περιβάλλοντος

Για **Azure AI Foundry** (Απαραίτητο):
- `AZURE_AI_PROJECT_ENDPOINT` - Σημείο τερματισμού έργου Azure AI Foundry
- `AZURE_AI_MODEL_DEPLOYMENT_NAME` - Όνομα ανάπτυξης μοντέλου (π.χ., gpt-4o)

Για **Azure AI Search** (Μάθημα 05 - RAG):
- `AZURE_SEARCH_SERVICE_ENDPOINT` - Σημείο τερματισμού Azure AI Search
- `AZURE_SEARCH_API_KEY` - Κλειδί API Azure AI Search

Πιστοποίηση: Εκτελέστε `az login` πριν τρέξετε τα notebooks (χρησιμοποιεί `AzureCliCredential`).

## Ροή Εργασίας Ανάπτυξης

### Εκτέλεση Jupyter Notebooks

Κάθε μάθημα περιλαμβάνει πολλαπλά Jupyter notebooks για διάφορα frameworks:

1. **Εκκίνηση Jupyter:**
   ```bash
   jupyter notebook
   ```

2. **Πλοήγηση σε κατάλογο μαθήματος** (π.χ., `01-intro-to-ai-agents/code_samples/`)

3. **Άνοιγμα και εκτέλεση των notebooks:**
   - `*-python-agent-framework.ipynb` - Χρήση Microsoft Agent Framework (Python)
   - `*-dotnet-agent-framework.ipynb` - Χρήση Microsoft Agent Framework (.NET)

### Εργασία με Microsoft Agent Framework

**Microsoft Agent Framework + Azure AI Foundry:**
- Απαιτεί συνδρομή Azure
- Χρησιμοποιεί `AzureAIProjectAgentProvider` για Agent Service V2 (agents ορατοί στο portal του Foundry)
- Έτοιμο για παραγωγή με ενσωματωμένη παρακολούθηση
- Πρότυπο αρχείου: `*-python-agent-framework.ipynb`

## Οδηγίες Δοκιμών

Αυτό είναι εκπαιδευτικό αποθετήριο με παραδείγματα κώδικα και όχι κώδικας παραγωγής με αυτοματοποιημένες δοκιμές. Για να επαληθεύσετε τη ρύθμιση και τις αλλαγές σας:

### Χειροκίνητη Δοκιμή

1. **Δοκιμή περιβάλλοντος Python:**
   ```bash
   python --version  # Πρέπει να είναι 3.12+
   pip list | grep -E "(agent-framework|azure-ai|azure-identity)"
   ```

2. **Δοκιμή εκτέλεσης notebook:**
   ```bash
   # Μετατροπή τετραδίου σε σενάριο και εκτέλεση (εξετάζει εισαγωγές)
   jupyter nbconvert --to script <lesson-folder>/code_samples/<notebook>.ipynb --stdout | python
   ```

3. **Επαλήθευση μεταβλητών περιβάλλοντος:**
   ```bash
   python -c "import os; from dotenv import load_dotenv; load_dotenv(); print('✓ GITHUB_TOKEN' if os.getenv('GITHUB_TOKEN') else '✗ GITHUB_TOKEN missing')"
   ```

### Εκτέλεση Ατομικών Notebooks

Ανοίξτε notebooks στο Jupyter και εκτελέστε τα κελιά διαδοχικά. Κάθε notebook είναι αυτόνομο και περιλαμβάνει:
- Δηλώσεις εισαγωγής
- Φόρτωση ρυθμίσεων
- Παραδείγματα υλοποίησης agents
- Αναμενόμενα αποτελέσματα σε markdown κελιά

## Στυλ Κώδικα

### Συμβάσεις Python

- **Έκδοση Python**: 3.12+
- **Στυλ κώδικα**: Ακολουθήστε τα τυπικά πρότυπα PEP 8 της Python
- **Notebooks**: Χρησιμοποιήστε καθαρά markdown κελιά για εξηγήσεις εννοιών
- **Εισαγωγές**: Ομαδοποιήστε κατά standard βιβλιοθήκη, τρίτους, τοπικές εισαγωγές

### Συμβάσεις Jupyter Notebook

- Περιλάβετε περιγραφικά markdown κελιά πριν από κελιά κώδικα
- Προσθέστε παραδείγματα εξόδου στα notebooks για αναφορά
- Χρησιμοποιήστε σαφή ονόματα μεταβλητών που ταιριάζουν με τις έννοιες του μαθήματος
- Κρατήστε τη σειρά εκτέλεσης του notebook γραμμική (κελί 1 → 2 → 3...)

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

Αυτό το αποθετήριο χρησιμοποιεί Markdown για την τεκμηρίωση:
- Αρχεία README.md σε κάθε φάκελο μαθήματος
- Κύριο README.md στη ρίζα του αποθετηρίου
- Αυτοματοποιημένο σύστημα μετάφρασης μέσω GitHub Actions

### Pipeline CI/CD

Βρίσκεται σε `.github/workflows/`:

1. **co-op-translator.yml** - Αυτόματη μετάφραση σε 50+ γλώσσες
2. **welcome-issue.yml** - Καλωσορίζει δημιουργούς νέων issues
3. **welcome-pr.yml** - Καλωσορίζει συνεισφέροντες νέων pull requests

### Ανάπτυξη

Αυτό είναι εκπαιδευτικό αποθετήριο - δεν υπάρχει διαδικασία ανάπτυξης. Οι χρήστες:
1. Κάνουν fork ή κλωνοποίηση του αποθετηρίου
2. Τρέχουν notebooks τοπικά ή σε GitHub Codespaces
3. Μαθαίνουν τροποποιώντας και πειραματιζόμενοι με τα παραδείγματα

## Οδηγίες για Pull Request

### Πριν την Υποβολή

1. **Δοκιμάστε τις αλλαγές σας:**
   - Εκτελέστε πλήρως τα επηρεασμένα notebooks
   - Επαληθεύστε ότι όλα τα κελιά εκτελούνται χωρίς σφάλματα
   - Ελέγξτε ότι τα αποτελέσματα είναι κατάλληλα

2. **Ενημερώσεις τεκμηρίωσης:**
   - Ενημερώστε το README.md αν προσθέτετε νέες έννοιες
   - Προσθέστε σχόλια στα notebooks για σύνθετο κώδικα
   - Βεβαιωθείτε ότι τα markdown κελιά εξηγούν τον σκοπό

3. **Αλλαγές αρχείων:**
   - Αποφύγετε την δέσμευση αρχείων `.env` (χρησιμοποιήστε `.env.example`)
   - Μην δεσμεύετε καταλόγους `venv/` ή `__pycache__/`
   - Κρατήστε τα outputs των notebooks όταν αυτά δείχνουν έννοιες
   - Αφαιρέστε προσωρινά αρχεία και backup notebooks (`*-backup.ipynb`)

### Μορφή Τίτλου PR

Χρησιμοποιήστε περιγραφικούς τίτλους:
- `[Lesson-XX] Προσθήκη νέου παραδείγματος για <έννοια>`
- `[Fix] Διόρθωση ορθογραφικού λάθους στο README του μαθήματος-XX`
- `[Update] Βελτίωση παραδείγματος κώδικα στο μάθημα-XX`
- `[Docs] Ενημέρωση οδηγιών εγκατάστασης`

### Απαιτούμενοι Έλεγχοι

- Τα notebooks πρέπει να εκτελούνται χωρίς σφάλματα
- Τα αρχεία README πρέπει να είναι σαφή και ακριβή
- Ακολουθήστε τα υπάρχοντα πρότυπα κώδικα του αποθετηρίου
- Διατηρήστε συνέπεια με τα άλλα μαθήματα

## Επιπλέον Σημειώσεις

### Συνήθη Προβλήματα

1. **Ασυμβατότητα έκδοσης Python:**
   - Βεβαιωθείτε ότι χρησιμοποιείται Python 3.12+
   - Ορισμένα πακέτα μπορεί να μη λειτουργούν σε παλαιότερες εκδόσεις
   - Χρησιμοποιήστε `python3 -m venv` για να καθορίσετε ρητά την έκδοση Python

2. **Μεταβλητές περιβάλλοντος:**
   - Δημιουργήστε πάντα `.env` από `.env.example`
   - Μην δεσμεύετε το αρχείο `.env` (είναι στο `.gitignore`)
   - Το token GitHub χρειάζεται κατάλληλα δικαιώματα

3. **Συγκρούσεις πακέτων:**
   - Χρησιμοποιήστε νέο εικονικό περιβάλλον
   - Εγκαταστήστε από το `requirements.txt` αντί μεμονωμένα πακέτα
   - Κάποια notebooks μπορεί να χρειάζονται επιπλέον πακέτα που αναφέρονται στα markdown κελιά τους

4. **Υπηρεσίες Azure:**
   - Οι υπηρεσίες Azure AI απαιτούν ενεργή συνδρομή
   - Ορισμένα χαρακτηριστικά είναι περιορισμένα ανά περιοχή
   - Οι δωρεάν βαθμίδες έχουν περιορισμούς για GitHub Models

### Διαδρομή Μάθησης

Συνιστώμενη σειρά μαθημάτων:
1. **00-course-setup** - Ξεκινήστε εδώ για ρύθμιση περιβάλλοντος
2. **01-intro-to-ai-agents** - Κατανόηση των βασικών των AI agents
3. **02-explore-agentic-frameworks** - Μάθετε για διαφορετικά frameworks
4. **03-agentic-design-patterns** - Βασικά πρότυπα σχεδίασης
5. Συνεχίστε με τα μαθήματα με αριθμό διαδοχικά

### Επιλογή Framework

Επιλέξτε το framework ανάλογα με τους στόχους σας:
- **Όλα τα μαθήματα**: Microsoft Agent Framework (MAF) με `AzureAIProjectAgentProvider`
- **Οι agents καταχωρούνται στην πλευρά διακομιστή** στο Azure AI Foundry Agent Service V2 και είναι ορατοί στο portal Foundry

### Λήψη Βοήθειας

- Ενταχθείτε στην [Microsoft Foundry Community Discord](https://aka.ms/ai-agents/discord)
- Διαβάστε τα README των μαθημάτων για ειδικές οδηγίες
- Ελέγξτε το κύριο [README.md](./README.md) για επισκόπηση μαθήματος
- Αναφερθείτε στο [Course Setup](./00-course-setup/README.md) για λεπτομερείς οδηγίες εγκατάστασης

### Συμμετοχή

Αυτό είναι ένα ανοιχτό εκπαιδευτικό έργο. Καλωσορίζουμε συνεισφορές:
- Βελτίωση παραδειγμάτων κώδικα
- Διόρθωση ορθογραφικών ή λογικών σφαλμάτων
- Προσθήκη επεξηγηματικών σχολίων
- Πρόταση νέων θεμάτων μαθημάτων
- Μετάφραση σε επιπλέον γλώσσες

Δείτε τα [GitHub Issues](https://github.com/microsoft/ai-agents-for-beginners/issues) για τρέχουσες ανάγκες.

## Συγκεκριμένο Πλαίσιο Έργου

### Υποστήριξη Πολλαπλών Γλωσσών

Αυτό το αποθετήριο χρησιμοποιεί αυτοματοποιημένο σύστημα μετάφρασης:
- Υποστήριξη 50+ γλωσσών
- Μεταφράσεις στους καταλόγους `/translations/<lang-code>/`
- Το workflow του GitHub Actions διαχειρίζεται τις ενημερώσεις μεταφράσεων
- Τα αρχεία πηγής είναι στα Αγγλικά στη ρίζα του αποθετηρίου

### Δομή Μαθημάτων

Κάθε μάθημα ακολουθεί σταθερό πρότυπο:
1. Μικρογραφία βίντεο με σύνδεσμο
2. Γραπτό περιεχόμενο μαθήματος (README.md)
3. Δείγματα κώδικα σε πολλαπλά frameworks
4. Στόχοι μάθησης και προαπαιτούμενα
5. Επιπλέον εκπαιδευτικοί πόροι με συνδέσμους

### Ονομασία Δειγμάτων Κώδικα

Μορφή: `<lesson-number>-python-agent-framework.ipynb`
- `01-python-agent-framework.ipynb` - Μάθημα 1, MAF Python
- `14-sequential.ipynb` - Μάθημα 14, προχωρημένα πρότυπα MAF

### Ειδικοί Κατάλογοι

- `translated_images/` - Εντοπιοθετημένες εικόνες για μεταφράσεις
- `images/` - Αρχικές εικόνες για αγγλικό περιεχόμενο
- `.devcontainer/` - Ρύθμιση κοντέινερ ανάπτυξης VS Code
- `.github/` - Workflows και πρότυπα GitHub Actions

### Εξαρτήσεις

Κύρια πακέτα από το `requirements.txt`:
- `agent-framework` - Microsoft Agent Framework
- `a2a-sdk` - Υποστήριξη πρωτοκόλλου Agent-to-Agent
- `azure-ai-inference`, `azure-ai-projects` - Υπηρεσίες Azure AI
- `azure-identity` - Πιστοποίηση Azure (AzureCliCredential)
- `azure-search-documents` - Ενσωμάτωση Azure AI Search
- `mcp[cli]` - Υποστήριξη Model Context Protocol

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Αποποίηση Ευθυνών**:  
Αυτό το έγγραφο έχει μεταφραστεί χρησιμοποιώντας την υπηρεσία αυτόματης μετάφρασης AI [Co-op Translator](https://github.com/Azure/co-op-translator). Παρόλο που επιδιώκουμε την ακρίβεια, παρακαλούμε να έχετε υπόψη ότι οι αυτόματες μεταφράσεις ενδέχεται να περιέχουν σφάλματα ή ανακρίβειες. Το πρωτότυπο έγγραφο στη μητρική του γλώσσα πρέπει να θεωρείται η αυθεντική πηγή. Για κρίσιμες πληροφορίες συνιστάται η επαγγελματική ανθρώπινη μετάφραση. Δεν φέρουμε ευθύνη για οποιεσδήποτε παρεξηγήσεις ή λανθασμένες ερμηνείες προκύψουν από τη χρήση αυτής της μετάφρασης.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->