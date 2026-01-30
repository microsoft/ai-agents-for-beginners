# AGENTS.md

## Επισκόπηση Έργου

Αυτό το αποθετήριο περιέχει το "AI Agents for Beginners" - ένα ολοκληρωμένο εκπαιδευτικό μάθημα που διδάσκει όλα όσα χρειάζονται για τη δημιουργία AI Agents. Το μάθημα αποτελείται από περισσότερα από 15 μαθήματα που καλύπτουν βασικές αρχές, πρότυπα σχεδίασης, πλαίσια και ανάπτυξη AI agents σε παραγωγή.

**Κύριες Τεχνολογίες:**
- Python 3.12+
- Jupyter Notebooks για διαδραστική μάθηση
- Πλαίσια AI: Semantic Kernel, AutoGen, Microsoft Agent Framework (MAF)
- Υπηρεσίες Azure AI: Azure AI Foundry, Azure AI Agent Service
- GitHub Models Marketplace (διαθέσιμη δωρεάν βαθμίδα)

**Αρχιτεκτονική:**
- Δομή βασισμένη σε μαθήματα (κατάλογοι 00-15+)
- Κάθε μάθημα περιέχει: τεκμηρίωση README, δείγματα κώδικα (Jupyter notebooks) και εικόνες
- Υποστήριξη πολλών γλωσσών μέσω αυτοματοποιημένου συστήματος μετάφρασης
- Πολλαπλές επιλογές πλαισίων ανά μάθημα (Semantic Kernel, AutoGen, Azure AI Agent Service)

## Εντολές Ρύθμισης

### Προαπαιτούμενα
- Python 3.12 ή νεότερη έκδοση
- Λογαριασμός GitHub (για GitHub Models - δωρεάν βαθμίδα)
- Συνδρομή Azure (προαιρετική, για υπηρεσίες Azure AI)

### Αρχική Ρύθμιση

1. **Κλωνοποίηση ή fork του αποθετηρίου:**
   ```bash
   gh repo fork microsoft/ai-agents-for-beginners --clone
   # OR
   git clone https://github.com/microsoft/ai-agents-for-beginners.git
   cd ai-agents-for-beginners
   ```

2. **Δημιουργία και ενεργοποίηση εικονικού περιβάλλοντος Python:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Εγκατάσταση εξαρτήσεων:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Ρύθμιση μεταβλητών περιβάλλοντος:**
   ```bash
   cp .env.example .env
   # Edit .env with your API keys and endpoints
   ```

### Απαιτούμενες Μεταβλητές Περιβάλλοντος

Για **GitHub Models (Δωρεάν):**
- `GITHUB_TOKEN` - Προσωπικό token πρόσβασης από το GitHub

Για **Υπηρεσίες Azure AI** (προαιρετικά):
- `PROJECT_ENDPOINT` - Endpoint έργου Azure AI Foundry
- `AZURE_OPENAI_API_KEY` - Κλειδί API Azure OpenAI
- `AZURE_OPENAI_ENDPOINT` - URL endpoint Azure OpenAI
- `AZURE_OPENAI_CHAT_DEPLOYMENT_NAME` - Όνομα ανάπτυξης για το μοντέλο συνομιλίας
- `AZURE_OPENAI_EMBEDDING_DEPLOYMENT_NAME` - Όνομα ανάπτυξης για embeddings
- Πρόσθετη διαμόρφωση Azure όπως φαίνεται στο `.env.example`

## Ροή Εργασίας Ανάπτυξης

### Εκτέλεση Jupyter Notebooks

Κάθε μάθημα περιέχει πολλαπλά Jupyter notebooks για διαφορετικά πλαίσια:

1. **Εκκίνηση Jupyter:**
   ```bash
   jupyter notebook
   ```

2. **Πλοήγηση σε κατάλογο μαθήματος** (π.χ., `01-intro-to-ai-agents/code_samples/`)

3. **Άνοιγμα και εκτέλεση notebooks:**
   - `*-semantic-kernel.ipynb` - Χρήση πλαισίου Semantic Kernel
   - `*-autogen.ipynb` - Χρήση πλαισίου AutoGen
   - `*-python-agent-framework.ipynb` - Χρήση Microsoft Agent Framework (Python)
   - `*-dotnet-agent-framework.ipynb` - Χρήση Microsoft Agent Framework (.NET)
   - `*-azureaiagent.ipynb` - Χρήση Azure AI Agent Service

### Εργασία με Διαφορετικά Πλαίσια

**Semantic Kernel + GitHub Models:**
- Διαθέσιμη δωρεάν βαθμίδα με λογαριασμό GitHub
- Ιδανικό για μάθηση και πειραματισμό
- Μοτίβο αρχείου: `*-semantic-kernel*.ipynb`

**AutoGen + GitHub Models:**
- Διαθέσιμη δωρεάν βαθμίδα με λογαριασμό GitHub
- Δυνατότητες ορχήστρωσης πολλαπλών agents
- Μοτίβο αρχείου: `*-autogen.ipynb`

**Microsoft Agent Framework (MAF):**
- Νεότερο πλαίσιο από τη Microsoft
- Διαθέσιμο σε Python και .NET
- Μοτίβο αρχείου: `*-agent-framework.ipynb`

**Azure AI Agent Service:**
- Απαιτεί συνδρομή Azure
- Χαρακτηριστικά έτοιμα για παραγωγή
- Μοτίβο αρχείου: `*-azureaiagent.ipynb`

## Οδηγίες Δοκιμής

Αυτό είναι ένα εκπαιδευτικό αποθετήριο με παραδείγματα κώδικα και όχι κώδικα παραγωγής με αυτοματοποιημένες δοκιμές. Για να επαληθεύσετε τη ρύθμιση και τις αλλαγές σας:

### Χειροκίνητη Δοκιμή

1. **Δοκιμή περιβάλλοντος Python:**
   ```bash
   python --version  # Should be 3.12+
   pip list | grep -E "(autogen|semantic-kernel|azure-ai)"
   ```

2. **Δοκιμή εκτέλεσης notebook:**
   ```bash
   # Convert notebook to script and run (tests imports)
   jupyter nbconvert --to script <lesson-folder>/code_samples/<notebook>.ipynb --stdout | python
   ```

3. **Επαλήθευση μεταβλητών περιβάλλοντος:**
   ```bash
   python -c "import os; from dotenv import load_dotenv; load_dotenv(); print('✓ GITHUB_TOKEN' if os.getenv('GITHUB_TOKEN') else '✗ GITHUB_TOKEN missing')"
   ```

### Εκτέλεση Μεμονωμένων Notebooks

Ανοίξτε τα notebooks στο Jupyter και εκτελέστε τα κελιά διαδοχικά. Κάθε notebook είναι αυτοτελές και περιλαμβάνει:
- Δηλώσεις εισαγωγής
- Φόρτωση διαμόρφωσης
- Παραδείγματα υλοποίησης agents
- Αναμενόμενα αποτελέσματα σε κελιά markdown

## Στυλ Κώδικα

### Συμβάσεις Python

- **Έκδοση Python**: 3.12+
- **Στυλ Κώδικα**: Ακολουθήστε τις τυπικές συμβάσεις PEP 8 της Python
- **Notebooks**: Χρησιμοποιήστε καθαρά κελιά markdown για να εξηγήσετε έννοιες
- **Εισαγωγές**: Ομαδοποιήστε κατά βιβλιοθήκη, τρίτους, τοπικές εισαγωγές

### Συμβάσεις Jupyter Notebook

- Συμπεριλάβετε περιγραφικά κελιά markdown πριν από τα κελιά κώδικα
- Προσθέστε παραδείγματα εξόδου στα notebooks για αναφορά
- Χρησιμοποιήστε καθαρά ονόματα μεταβλητών που ταιριάζουν με τις έννοιες του μαθήματος
- Διατηρήστε τη σειρά εκτέλεσης των notebooks γραμμική (κελί 1 → 2 → 3...)

### Οργάνωση Αρχείων

```
<lesson-number>-<lesson-name>/
├── README.md                     # Lesson documentation
├── code_samples/
│   ├── <number>-semantic-kernel.ipynb
│   ├── <number>-autogen.ipynb
│   ├── <number>-python-agent-framework.ipynb
│   └── <number>-azureaiagent.ipynb
└── images/
    └── *.png
```

## Δημιουργία και Ανάπτυξη

### Δημιουργία Τεκμηρίωσης

Αυτό το αποθετήριο χρησιμοποιεί Markdown για τεκμηρίωση:
- Αρχεία README.md σε κάθε φάκελο μαθήματος
- Κύριο README.md στη ρίζα του αποθετηρίου
- Αυτοματοποιημένο σύστημα μετάφρασης μέσω GitHub Actions

### CI/CD Pipeline

Βρίσκεται στο `.github/workflows/`:

1. **co-op-translator.yml** - Αυτόματη μετάφραση σε 50+ γλώσσες
2. **welcome-issue.yml** - Καλωσορίζει νέους δημιουργούς θεμάτων
3. **welcome-pr.yml** - Καλωσορίζει νέους συνεισφέροντες pull request

### Ανάπτυξη

Αυτό είναι ένα εκπαιδευτικό αποθετήριο - δεν υπάρχει διαδικασία ανάπτυξης. Οι χρήστες:
1. Κάνουν fork ή κλωνοποιούν το αποθετήριο
2. Εκτελούν notebooks τοπικά ή στο GitHub Codespaces
3. Μαθαίνουν τροποποιώντας και πειραματιζόμενοι με παραδείγματα

## Οδηγίες Pull Request

### Πριν την Υποβολή

1. **Δοκιμάστε τις αλλαγές σας:**
   - Εκτελέστε πλήρως τα notebooks που επηρεάζονται
   - Επαληθεύστε ότι όλα τα κελιά εκτελούνται χωρίς σφάλματα
   - Ελέγξτε ότι τα αποτελέσματα είναι κατάλληλα

2. **Ενημερώσεις τεκμηρίωσης:**
   - Ενημερώστε το README.md αν προσθέσετε νέες έννοιες
   - Προσθέστε σχόλια στα notebooks για πολύπλοκο κώδικα
   - Βεβαιωθείτε ότι τα κελιά markdown εξηγούν τον σκοπό

3. **Αλλαγές αρχείων:**
   - Αποφύγετε την υποβολή αρχείων `.env` (χρησιμοποιήστε `.env.example`)
   - Μην υποβάλετε καταλόγους `venv/` ή `__pycache__/`
   - Διατηρήστε τις εξόδους των notebooks όταν δείχνουν έννοιες
   - Αφαιρέστε προσωρινά αρχεία και εφεδρικά notebooks (`*-backup.ipynb`)

### Μορφή Τίτλου PR

Χρησιμοποιήστε περιγραφικούς τίτλους:
- `[Lesson-XX] Προσθήκη νέου παραδείγματος για <έννοια>`
- `[Fix] Διόρθωση τυπογραφικού στο README του μαθήματος-XX`
- `[Update] Βελτίωση δείγματος κώδικα στο μάθημα-XX`
- `[Docs] Ενημέρωση οδηγιών ρύθμισης`

### Απαιτούμενοι Έλεγχοι

- Τα notebooks πρέπει να εκτελούνται χωρίς σφάλματα
- Τα αρχεία README πρέπει να είναι σαφή και ακριβή
- Ακολουθήστε υπάρχοντα πρότυπα κώδικα στο αποθετήριο
- Διατηρήστε τη συνέπεια με άλλα μαθήματα

## Πρόσθετες Σημειώσεις

### Συνηθισμένα Προβλήματα

1. **Ασυμβατότητα έκδοσης Python:**
   - Βεβαιωθείτε ότι χρησιμοποιείτε Python 3.12+
   - Ορισμένα πακέτα μπορεί να μην λειτουργούν με παλαιότερες εκδόσεις
   - Χρησιμοποιήστε `python3 -m venv` για να καθορίσετε την έκδοση Python ρητά

2. **Μεταβλητές περιβάλλοντος:**
   - Δημιουργήστε πάντα `.env` από `.env.example`
   - Μην υποβάλετε το αρχείο `.env` (είναι στο `.gitignore`)
   - Το token του GitHub χρειάζεται κατάλληλα δικαιώματα

3. **Συγκρούσεις πακέτων:**
   - Χρησιμοποιήστε ένα νέο εικονικό περιβάλλον
   - Εγκαταστήστε από το `requirements.txt` αντί για μεμονωμένα πακέτα
   - Ορισμένα notebooks μπορεί να απαιτούν πρόσθετα πακέτα που αναφέρονται στα κελιά markdown τους

4. **Υπηρεσίες Azure:**
   - Οι υπηρεσίες Azure AI απαιτούν ενεργή συνδρομή
   - Ορισμένα χαρακτηριστικά είναι συγκεκριμένα για την περιοχή
   - Περιορισμοί δωρεάν βαθμίδας ισχύουν για GitHub Models

### Διαδρομή Μάθησης

Συνιστώμενη πρόοδος μέσω των μαθημάτων:
1. **00-course-setup** - Ξεκινήστε εδώ για τη ρύθμιση του περιβάλλοντος
2. **01-intro-to-ai-agents** - Κατανοήστε τις βασικές αρχές των AI agents
3. **02-explore-agentic-frameworks** - Μάθετε για διαφορετικά πλαίσια
4. **03-agentic-design-patterns** - Βασικά πρότυπα σχεδίασης
5. Συνεχίστε μέσω των αριθμημένων μαθημάτων διαδοχικά

### Επιλογή Πλαισίου

Επιλέξτε πλαίσιο με βάση τους στόχους σας:
- **Μάθηση/Πρωτότυπα**: Semantic Kernel + GitHub Models (δωρεάν)
- **Συστήματα πολλαπλών agents**: AutoGen
- **Νεότερα χαρακτηριστικά**: Microsoft Agent Framework (MAF)
- **Ανάπτυξη παραγωγής**: Azure AI Agent Service

### Λήψη Βοήθειας

- Εγγραφείτε στο [Azure AI Foundry Community Discord](https://aka.ms/ai-agents/discord)
- Ανατρέξτε στα αρχεία README των μαθημάτων για συγκεκριμένες οδηγίες
- Ελέγξτε το κύριο [README.md](./README.md) για επισκόπηση του μαθήματος
- Ανατρέξτε στο [Course Setup](./00-course-setup/README.md) για λεπτομερείς οδηγίες ρύθμισης

### Συνεισφορά

Αυτό είναι ένα ανοιχτό εκπαιδευτικό έργο. Συνεισφορές ευπρόσδεκτες:
- Βελτίωση παραδειγμάτων κώδικα
- Διόρθωση τυπογραφικών ή σφαλμάτων
- Προσθήκη διευκρινιστικών σχολίων
- Πρόταση νέων θεμάτων μαθημάτων
- Μετάφραση σε πρόσθετες γλώσσες

Δείτε τα [GitHub Issues](https://github.com/microsoft/ai-agents-for-beginners/issues) για τρέχουσες ανάγκες.

## Συγκεκριμένο Πλαίσιο Έργου

### Υποστήριξη Πολλών Γλωσσών

Αυτό το αποθετήριο χρησιμοποιεί ένα αυτοματοποιημένο σύστημα μετάφρασης:
- Υποστηρίζονται 50+ γλώσσες
- Μεταφράσεις σε καταλόγους `/translations/<lang-code>/`
- Η ροή εργασίας GitHub Actions χειρίζεται ενημερώσεις μετάφρασης
- Τα αρχεία προέλευσης είναι στα Αγγλικά στη ρίζα του αποθετηρίου

### Δομή Μαθήματος

Κάθε μάθημα ακολουθεί ένα συνεπές μοτίβο:
1. Μικρογραφία βίντεο με σύνδεσμο
2. Γραπτό περιεχόμενο μαθήματος (README.md)
3. Δείγματα κώδικα σε πολλαπλά πλαίσια
4. Στόχοι μάθησης και προαπαιτούμενα
5. Πρόσθετοι πόροι μάθησης συνδεδεμένοι

### Ονομασία Δειγμάτων Κώδικα

Μορφή: `<lesson-number>-<framework-name>.ipynb`
- `04-semantic-kernel.ipynb` - Μάθημα 4, Semantic Kernel
- `07-autogen.ipynb` - Μάθημα 7, AutoGen
- `14-python-agent-framework.ipynb` - Μάθημα 14, MAF Python
- `14-dotnet-agent-framework.ipynb` - Μάθημα 14, MAF .NET

### Ειδικοί Κατάλογοι

- `translated_images/` - Τοπικές εικόνες για μεταφράσεις
- `images/` - Αρχικές εικόνες για περιεχόμενο στα Αγγλικά
- `.devcontainer/` - Διαμόρφωση container ανάπτυξης VS Code
- `.github/` - Ροές εργασίας και πρότυπα GitHub Actions

### Εξαρτήσεις

Κύρια πακέτα από το `requirements.txt`:
- `autogen-agentchat`, `autogen-core`, `autogen-ext` - Πλαίσιο AutoGen
- `semantic-kernel` - Πλαίσιο Semantic Kernel
- `agent-framework` - Microsoft Agent Framework
- `azure-ai-inference`, `azure-ai-projects` - Υπηρεσίες Azure AI
- `azure-search-documents` - Ενσωμάτωση αναζήτησης Azure AI
- `chromadb` - Βάση δεδομένων διανυσμάτων για παραδείγματα RAG
- `chainlit` - Πλαίσιο UI συνομιλίας
- `browser_use` - Αυτοματοποίηση περιηγητή για agents
- `mcp[cli]` - Υποστήριξη Model Context Protocol
- `mem0ai` - Διαχείριση μνήμης για agents

---

**Αποποίηση ευθύνης**:  
Αυτό το έγγραφο έχει μεταφραστεί χρησιμοποιώντας την υπηρεσία μετάφρασης AI [Co-op Translator](https://github.com/Azure/co-op-translator). Παρόλο που καταβάλλουμε προσπάθειες για ακρίβεια, παρακαλούμε να έχετε υπόψη ότι οι αυτοματοποιημένες μεταφράσεις ενδέχεται να περιέχουν λάθη ή ανακρίβειες. Το πρωτότυπο έγγραφο στη μητρική του γλώσσα θα πρέπει να θεωρείται η αυθεντική πηγή. Για κρίσιμες πληροφορίες, συνιστάται επαγγελματική ανθρώπινη μετάφραση. Δεν φέρουμε ευθύνη για τυχόν παρεξηγήσεις ή εσφαλμένες ερμηνείες που προκύπτουν από τη χρήση αυτής της μετάφρασης.