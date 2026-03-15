# Ρύθμιση μαθήματος

## Εισαγωγή

Αυτό το μάθημα θα καλύψει πώς να εκτελέσετε τα δείγματα κώδικα αυτού του μαθήματος.

## Συνδεθείτε με άλλους μαθητές και λάβετε βοήθεια

Πριν ξεκινήσετε να κλωνοποιείτε το repo σας, εγγραφείτε στο [AI Agents For Beginners Discord channel](https://aka.ms/ai-agents/discord) για να λάβετε βοήθεια με τη ρύθμιση, για οποιεσδήποτε ερωτήσεις σχετικά με το μάθημα ή για να συνδεθείτε με άλλους μαθητές.

## Κλωνοποίηση ή fork αυτού του αποθετηρίου

Για να ξεκινήσετε, παρακαλώ κλωνοποιήστε ή κάντε fork το GitHub Repository. Αυτό θα δημιουργήσει τη δική σας έκδοση του υλικού του μαθήματος ώστε να μπορείτε να εκτελείτε, να δοκιμάζετε και να τροποποιείτε τον κώδικα!

Αυτό μπορεί να γίνει κάνοντας κλικ στον σύνδεσμο για <a href="https://github.com/microsoft/ai-agents-for-beginners/fork" target="_blank">κάντε fork στο αποθετήριο</a>

Θα πρέπει τώρα να έχετε τη δική σας έκδοση του μαθήματος στο ακόλουθο σύνδεσμο:

![Αποθετήριο που έγινε fork](../../../translated_images/el/forked-repo.33f27ca1901baa6a.webp)

### Shallow Clone (συνιστάται για workshop / Codespaces)

  >Το πλήρες αποθετήριο μπορεί να είναι μεγάλο (~3 GB) όταν κάνετε λήψη ολόκληρου του ιστορικού και όλων των αρχείων. Αν παρακολουθείτε μόνο το εργαστήριο ή χρειάζεστε λίγους φακέλους μαθήματος, ένα shallow clone (ή ένα sparse clone) αποφύγει το μεγαλύτερο μέρος αυτής της λήψης με το να περικόψει το ιστορικό και/ή να παραλείψει blobs.

#### Γρήγορο shallow clone — ελάχιστο ιστορικό, όλα τα αρχεία

Αντικαταστήστε το `<your-username>` στις παρακάτω εντολές με το URL του fork σας (ή με το upstream URL αν προτιμάτε).

Για να κλωνοποιήσετε μόνο το πιο πρόσφατο ιστορικό commit (μικρή λήψη):

```bash|powershell
git clone --depth 1 https://github.com/<your-username>/ai-agents-for-beginners.git
```

Για να κλωνοποιήσετε ένα συγκεκριμένο branch:

```bash|powershell
git clone --depth 1 --branch <branch-name> https://github.com/<your-username>/ai-agents-for-beginners.git
```

#### Μερική (sparse) κλωνοποίηση — ελάχιστα blobs + μόνο επιλεγμένοι φάκελοι

Αυτό χρησιμοποιεί partial clone και sparse-checkout (απαιτεί Git 2.25+ και συνιστάται σύγχρονο Git με υποστήριξη partial clone):

```bash|powershell
git clone --depth 1 --filter=blob:none --sparse https://github.com/<your-username>/ai-agents-for-beginners.git
```

Περιηγηθείτε μέσα στον φάκελο του repo:

```bash|powershell
cd ai-agents-for-beginners
```

Στη συνέχεια ορίστε ποιους φακέλους θέλετε (το παράδειγμα παρακάτω δείχνει δύο φακέλους):

```bash|powershell
git sparse-checkout set 00-course-setup 01-intro-to-ai-agents
```

Μετά την κλωνοποίηση και την επαλήθευση των αρχείων, αν χρειάζεστε μόνο τα αρχεία και θέλετε να απελευθερώσετε χώρο (χωρίς ιστορικό git), παρακαλώ διαγράψτε τα μεταδεδομένα του αποθετηρίου (💀μη αναστρέψιμο — θα χάσετε όλη τη λειτουργικότητα του Git: κανένα commit, pull, push ή πρόσβαση στο ιστορικό).

```bash
# zsh/bash
rm -rf .git
```

```powershell
# PowerShell
Remove-Item -Recurse -Force .git
```

#### Χρήση GitHub Codespaces (συνιστάται για να αποφύγετε τοπικές μεγάλες λήψεις)

- Δημιουργήστε ένα νέο Codespace για αυτό το repo μέσω του [GitHub UI](https://github.com/codespaces).  

- Στο τερματικό του νεοδημιουργημένου codespace, εκτελέστε μία από τις εντολές shallow/sparse clone παραπάνω για να φέρετε μόνο τους φακέλους μάθησης που χρειάζεστε στο workspace του Codespace.
- Προαιρετικό: μετά την κλωνοποίηση μέσα στα Codespaces, αφαιρέστε το .git για να ανακτήσετε επιπλέον χώρο (δείτε τις εντολές αφαίρεσης παραπάνω).
- Σημείωση: Αν προτιμάτε να ανοίξετε το repo απευθείας στα Codespaces (χωρίς επιπλέον κλωνοποίηση), λάβετε υπόψη ότι τα Codespaces θα κατασκευάσουν το devcontainer περιβάλλον και ενδέχεται να προμηθεύσουν περισσότερα από όσα χρειάζεστε. Η κλωνοποίηση ενός shallow αντιγράφου μέσα σε ένα φρέσκο Codespace σας δίνει μεγαλύτερο έλεγχο της χρήσης του δίσκου.

#### Συμβουλές

- Πάντα αντικαθιστάτε το URL κλωνοποίησης με το fork σας αν θέλετε να επεξεργαστείτε/κάνετε commit.
- Αν αργότερα χρειαστείτε περισσότερο ιστορικό ή αρχεία, μπορείτε να τα κάνετε fetch ή να ρυθμίσετε ξανά το sparse-checkout για να συμπεριλάβετε επιπλέον φακέλους.

## Εκτέλεση του κώδικα

Αυτό το μάθημα προσφέρει μια σειρά από Jupyter Notebooks που μπορείτε να εκτελέσετε για να αποκτήσετε πρακτική εμπειρία στην κατασκευή AI Agents.

Τα δείγματα κώδικα χρησιμοποιούν το **Microsoft Agent Framework (MAF)** με τον `AzureAIProjectAgentProvider`, που συνδέεται με την **Azure AI Agent Service V2** (το Responses API) μέσω της **Microsoft Foundry**.

Όλα τα Python notebooks είναι επισημασμένα `*-python-agent-framework.ipynb`.

## Απαιτήσεις

- Python 3.12+
  - **ΣΗΜΕΙΩΣΗ**: Αν δεν έχετε εγκαταστήσει το Python3.12, βεβαιωθείτε ότι το εγκαθιστάτε. Στη συνέχεια δημιουργήστε το venv σας χρησιμοποιώντας python3.12 για να διασφαλίσετε ότι οι σωστές εκδόσεις εγκαθίστανται από το αρχείο requirements.txt.
  
    >Παράδειγμα

    Δημιουργήστε τον κατάλογο venv για Python:

    ```bash|powershell
    python -m venv venv
    ```

    Στη συνέχεια ενεργοποιήστε το περιβάλλον venv για:

    ```bash
    # zsh/bash
    source venv/bin/activate
    ```
  
    ```dos
    # Command Prompt for Windows
    venv\Scripts\activate
    ```

- .NET 10+: Για τα δείγματα κώδικα που χρησιμοποιούν .NET, βεβαιωθείτε ότι έχετε εγκαταστήσει το [.NET 10 SDK](https://dotnet.microsoft.com/download/dotnet/10.0) ή νεότερο. Στη συνέχεια, ελέγξτε την εγκατεστημένη έκδοση του .NET SDK σας:

    ```bash|powershell
    dotnet --list-sdks
    ```

- **Azure CLI** — Απαιτείται για την αυθεντικοποίηση. Εγκαταστήστε από [aka.ms/installazurecli](https://aka.ms/installazurecli).
- **Azure Subscription** — Για πρόσβαση στο Microsoft Foundry και στην Azure AI Agent Service.
- **Microsoft Foundry Project** — Ένα project με αναπτυχθέν μοντέλο (π.χ. `gpt-4o`). Δείτε το [Βήμα 1](../../../00-course-setup) παρακάτω.

Έχουμε συμπεριλάβει ένα αρχείο `requirements.txt` στη ρίζα αυτού του αποθετηρίου που περιέχει όλα τα απαιτούμενα πακέτα Python για να εκτελέσετε τα δείγματα κώδικα.

Μπορείτε να τα εγκαταστήσετε εκτελώντας την παρακάτω εντολή στο τερματικό σας στη ρίζα του αποθετηρίου:

```bash|powershell
pip install -r requirements.txt
```

Συνιστούμε τη δημιουργία ενός Python virtual environment για να αποφύγετε οποιεσδήποτε συγκρούσεις και προβλήματα.

## Ρύθμιση VSCode

Βεβαιωθείτε ότι χρησιμοποιείτε τη σωστή έκδοση του Python στο VSCode.

![εικόνα](https://github.com/user-attachments/assets/a85e776c-2edb-4331-ae5b-6bfdfb98ee0e)

## Ρύθμιση Microsoft Foundry και Azure AI Agent Service

### Βήμα 1: Δημιουργία ενός Microsoft Foundry Project

Χρειάζεστε ένα Azure AI Foundry **hub** και **project** με ένα αναπτυχθέν μοντέλο για να εκτελέσετε τα notebooks.

1. Πηγαίνετε στο [ai.azure.com](https://ai.azure.com) και συνδεθείτε με τον λογαριασμό Azure.
2. Δημιουργήστε ένα **hub** (ή χρησιμοποιήστε ένα υπάρχον). Δείτε: [Hub resources overview](https://learn.microsoft.com/azure/ai-foundry/concepts/ai-resources).
3. Μέσα στο hub, δημιουργήστε ένα **project**.
4. Αναπτύξτε ένα μοντέλο (π.χ. `gpt-4o`) από **Models + Endpoints** → **Deploy model**.

### Βήμα 2: Ανάκτηση του Endpoint του Project και του Ονόματος Ανάπτυξης Μοντέλου

Από το project σας στην πύλη Microsoft Foundry:

- **Project Endpoint** — Πηγαίνετε στη σελίδα **Overview** και αντιγράψτε το URL του endpoint.

![Project Connection String](../../../translated_images/el/project-endpoint.8cf04c9975bbfbf1.webp)

- **Model Deployment Name** — Πηγαίνετε σε **Models + Endpoints**, επιλέξτε το αναπτυγμένο μοντέλο σας και σημειώστε το **Deployment name** (π.χ., `gpt-4o`).

### Βήμα 3: Συνδεθείτε στο Azure με `az login`

Όλα τα notebooks χρησιμοποιούν **`AzureCliCredential`** για αυθεντικοποίηση — δεν χρειάζεται να διαχειρίζεστε API keys. Αυτό απαιτεί να είστε συνδεδεμένοι μέσω του Azure CLI.

1. **Εγκαταστήστε το Azure CLI** αν δεν το έχετε ήδη: [aka.ms/installazurecli](https://aka.ms/installazurecli)

2. **Συνδεθείτε** εκτελώντας:

    ```bash|powershell
    az login
    ```

    Ή αν βρίσκεστε σε απομακρυσμένο/Codespace περιβάλλον χωρίς πρόγραμμα περιήγησης:

    ```bash|powershell
    az login --use-device-code
    ```

3. **Επιλέξτε τη συνδρομή** σας αν ζητηθεί — επιλέξτε αυτή που περιέχει το Foundry project σας.

4. **Επαληθεύστε** ότι είστε συνδεδεμένοι:

    ```bash|powershell
    az account show
    ```

> **Γιατί `az login`;** Τα notebooks αυθεντικοποιούνται χρησιμοποιώντας `AzureCliCredential` από το πακέτο `azure-identity`. Αυτό σημαίνει ότι η συνεδρία Azure CLI σας παρέχει τα διαπιστευτήρια — δεν χρειάζονται API keys ή μυστικά στο αρχείο `.env` σας. Αυτό είναι μια [βέλτιστη πρακτική ασφάλειας](https://learn.microsoft.com/azure/developer/ai/keyless-connections).

### Βήμα 4: Δημιουργήστε το αρχείο `.env` σας

Αντιγράψτε το παράδειγμα αρχείου:

```bash
# zsh/bash
cp .env.example .env
```

```powershell
# PowerShell
Copy-Item .env.example .env
```

Ανοίξτε το `.env` και συμπληρώστε αυτές τις δύο τιμές:

```env
AZURE_AI_PROJECT_ENDPOINT=https://<your-project>.services.ai.azure.com/api/projects/<your-project-id>
AZURE_AI_MODEL_DEPLOYMENT_NAME=gpt-4o
```

| Variable | Πού να τη βρείτε |
|----------|-----------------|
| `AZURE_AI_PROJECT_ENDPOINT` | Foundry portal → your project → **Overview** page |
| `AZURE_AI_MODEL_DEPLOYMENT_NAME` | Foundry portal → **Models + Endpoints** → your deployed model's name |

Αυτό είναι όλο για τα περισσότερα μαθήματα! Τα notebooks θα αυθεντικοποιηθούν αυτόματα μέσω της συνεδρίας `az login`.

### Βήμα 5: Εγκαταστήστε τις εξαρτήσεις Python

```bash|powershell
pip install -r requirements.txt
```

Συνιστούμε να εκτελέσετε αυτό μέσα στο virtual environment που δημιουργήσατε νωρίτερα.

## Πρόσθετη ρύθμιση για το Μάθημα 5 (Agentic RAG)

Το Μάθημα 5 χρησιμοποιεί **Azure AI Search** για retrieval-augmented generation. Αν σκοπεύετε να εκτελέσετε εκείνο το μάθημα, προσθέστε αυτές τις μεταβλητές στο αρχείο `.env` σας:

| Variable | Πού να τη βρείτε |
|----------|-----------------|
| `AZURE_SEARCH_SERVICE_ENDPOINT` | Azure portal → your **Azure AI Search** resource → **Overview** → URL |
| `AZURE_SEARCH_API_KEY` | Azure portal → your **Azure AI Search** resource → **Settings** → **Keys** → primary admin key |

## Πρόσθετη ρύθμιση για το Μάθημα 6 και το Μάθημα 8 (GitHub Models)

Ορισμένα notebooks στα μαθήματα 6 και 8 χρησιμοποιούν **GitHub Models** αντί για Azure AI Foundry. Αν σκοπεύετε να εκτελέσετε αυτά τα δείγματα, προσθέστε αυτές τις μεταβλητές στο αρχείο `.env` σας:

| Variable | Πού να τη βρείτε |
|----------|-----------------|
| `GITHUB_TOKEN` | GitHub → **Settings** → **Developer settings** → **Personal access tokens** |
| `GITHUB_ENDPOINT` | Use `https://models.inference.ai.azure.com` (default value) |
| `GITHUB_MODEL_ID` | Model name to use (e.g. `gpt-4o-mini`) |

## Πρόσθετη ρύθμιση για το Μάθημα 8 (Bing Grounding Workflow)

Το conditional workflow notebook στο μάθημα 8 χρησιμοποιεί **Bing grounding** μέσω Azure AI Foundry. Αν σκοπεύετε να εκτελέσετε εκείνο το δείγμα, προσθέστε αυτή τη μεταβλητή στο αρχείο `.env` σας:

| Variable | Πού να τη βρείτε |
|----------|-----------------|
| `BING_CONNECTION_ID` | Azure AI Foundry portal → your project → **Management** → **Connected resources** → your Bing connection → copy the connection ID |

## Αντιμετώπιση προβλημάτων

### Σφάλματα επαλήθευσης πιστοποιητικού SSL σε macOS

Αν βρίσκεστε σε macOS και αντιμετωπίζετε ένα σφάλμα όπως:

```plaintext
ssl.SSLCertVerificationError: [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: self-signed certificate in certificate chain
```

Αυτό είναι ένα γνωστό ζήτημα με το Python σε macOS όπου τα συστήματα πιστοποιητικά SSL δεν εμπιστεύονται αυτόματα. Δοκιμάστε τις παρακάτω λύσεις με αυτή τη σειρά:

**Επιλογή 1: Εκτελέστε το script Install Certificates του Python (συνιστάται)**

```bash
# Αντικαταστήστε το 3.XX με την εγκατεστημένη έκδοση της Python σας (π.χ., 3.12 ή 3.13):
/Applications/Python\ 3.XX/Install\ Certificates.command
```

**Επιλογή 2: Χρησιμοποιήστε `connection_verify=False` στο notebook σας (μόνο για notebooks GitHub Models)**

Στο Notebook του Μαθήματος 6 (`06-building-trustworthy-agents/code_samples/06-system-message-framework.ipynb`), υπάρχει ήδη μια σχολιασμένη λύση. Αποσχολιάστε το `connection_verify=False` όταν δημιουργείτε τον client:

```python
client = ChatCompletionsClient(
    endpoint=endpoint,
    credential=AzureKeyCredential(token),
    connection_verify=False,  # Απενεργοποιήστε την επαλήθευση SSL εάν αντιμετωπίζετε σφάλματα πιστοποιητικού
)
```

> **⚠️ Προειδοποίηση:** Απενεργοποίηση της επαλήθευσης SSL (`connection_verify=False`) μειώνει την ασφάλεια παραλείποντας την επαλήθευση πιστοποιητικών. Χρησιμοποιήστε το μόνο ως προσωρινή λύση σε περιβάλλοντα ανάπτυξης, ποτέ σε παραγωγή.

**Επιλογή 3: Εγκαταστήστε και χρησιμοποιήστε το `truststore`**

```bash
pip install truststore
```

Στη συνέχεια προσθέστε τα ακόλουθα στο πάνω μέρος του notebook ή του script σας πριν κάνετε οποιεσδήποτε κλήσεις δικτύου:

```python
import truststore
truststore.inject_into_ssl()
```

## Κολλήσατε κάπου;

Αν έχετε οποιοδήποτε πρόβλημα με τη ρύθμιση, μπείτε στο <a href="https://discord.gg/kzRShWzttr" target="_blank">Κοινότητα Azure AI στο Discord</a> ή <a href="https://github.com/microsoft/ai-agents-for-beginners/issues?WT.mc_id=academic-105485-koreyst" target="_blank">δημιουργήστε ένα issue</a>.

## Επόμενο μάθημα

Είστε τώρα έτοιμοι να εκτελέσετε τον κώδικα για αυτό το μάθημα. Καλή συνέχεια στην εκμάθηση περισσότερων για τον κόσμο των AI Agents! 

[Εισαγωγή στους AI Agents και περιπτώσεις χρήσης των Agents](../01-intro-to-ai-agents/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
Αποποίηση ευθυνών:
Αυτό το έγγραφο έχει μεταφραστεί χρησιμοποιώντας την υπηρεσία μετάφρασης με τεχνητή νοημοσύνη Co-op Translator (https://github.com/Azure/co-op-translator). Αν και καταβάλλουμε προσπάθειες για ακρίβεια, παρακαλούμε να έχετε υπόψη ότι οι αυτοματοποιημένες μεταφράσεις ενδέχεται να περιέχουν λάθη ή ανακρίβειες. Το πρωτότυπο έγγραφο στην αρχική του γλώσσα πρέπει να θεωρείται η επίσημη πηγή. Σε περίπτωση κρίσιμων πληροφοριών προτείνεται επαγγελματική μετάφραση από άνθρωπο. Δεν ευθυνόμαστε για τυχόν παρεξηγήσεις ή λανθασμένες ερμηνείες που προκύπτουν από τη χρήση αυτής της μετάφρασης.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->