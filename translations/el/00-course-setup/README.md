# Ρύθμιση Μαθήματος

## Εισαγωγή

Αυτό το μάθημα θα καλύψει πώς να εκτελείτε τα δείγματα κώδικα αυτού του μαθήματος.

## Συμμετοχή με Άλλους Μαθητές και Λήψη Βοήθειας

Πριν ξεκινήσετε να κλωνοποιείτε το αποθετήριο σας, συμμετάσχετε στο [κανάλι Discord AI Agents For Beginners](https://aka.ms/ai-agents/discord) για να λάβετε βοήθεια με τη ρύθμιση, ερωτήσεις σχετικά με το μάθημα ή για να συνδεθείτε με άλλους μαθητές.

## Κλωνοποιήστε ή Διακλαδώστε αυτό το Αποθετήριο

Για να ξεκινήσετε, παρακαλώ κλωνοποιήστε ή διακλαδώστε το Αποθετήριο GitHub. Αυτό θα δημιουργήσει μια δική σας έκδοση του υλικού του μαθήματος ώστε να μπορείτε να εκτελείτε, δοκιμάζετε και τροποποιείτε τον κώδικα!

Αυτό μπορεί να γίνει κάνοντας κλικ στο σύνδεσμο για <a href="https://github.com/microsoft/ai-agents-for-beginners/fork" target="_blank">να κάνετε διακλάδωση του αποθετηρίου</a>

Τώρα θα πρέπει να έχετε τη δική σας διακλαδωμένη έκδοση αυτού του μαθήματος στον παρακάτω σύνδεσμο:

![Forked Repo](../../../translated_images/el/forked-repo.33f27ca1901baa6a.webp)

### Απλή Κλωνοποίηση (συνιστάται για εργαστήριο / Codespaces)

  >Το πλήρες αποθετήριο μπορεί να είναι μεγάλο (~3 GB) όταν κατεβάζετε ολόκληρο το ιστορικό και όλα τα αρχεία. Εάν παρακολουθείτε μόνο το εργαστήριο ή χρειάζεστε μόνον μερικούς φακέλους μαθημάτων, μια απλή κλωνοποίηση (ή αραιή κλωνοποίηση) κατεβάζει πολύ λιγότερα.

#### Γρήγορη απλή κλωνοποίηση — ελάχιστο ιστορικό, όλα τα αρχεία

Αντικαταστήστε το `<your-username>` στις παρακάτω εντολές με το URL της διακλάδωσης σας (ή το αρχικό URL αν προτιμάτε).

Για να κλωνοποιήσετε μόνο το τελευταίο ιστορικό commit (μικρή λήψη):

```bash
git clone --depth 1 https://github.com/<your-username>/ai-agents-for-beginners.git
```

Για να κλωνοποιήσετε συγκεκριμένο κλάδο:

```bash
git clone --depth 1 --branch <branch-name> https://github.com/<your-username>/ai-agents-for-beginners.git
```

#### Μερική (αραιή) κλωνοποίηση — ελάχιστα blobs + μόνο επιλεγμένοι φάκελοι

Αυτό χρησιμοποιεί μερική κλωνοποίηση και sparse-checkout (απαιτεί Git 2.25+ και συνιστάται σύγχρονο Git με υποστήριξη μερικής κλωνοποίησης):

```bash
git clone --depth 1 --filter=blob:none --sparse https://github.com/<your-username>/ai-agents-for-beginners.git
```

Μεταβείτε στον φάκελο του αποθετηρίου:

```bash
cd ai-agents-for-beginners
```

Έπειτα καθορίστε ποιους φακέλους θέλετε (το παράδειγμα πιο κάτω δείχνει δύο φακέλους):

```bash
git sparse-checkout set 00-course-setup 01-intro-to-ai-agents
```

Μετά την κλωνοποίηση και την επαλήθευση των αρχείων, αν χρειάζεστε μόνο αρχεία και θέλετε να ελευθερώσετε χώρο (χωρίς ιστορικό git), παρακαλώ διαγράψτε τα μεταδεδομένα αποθετηρίου (💀αμετάκλητο — θα χάσετε όλη τη λειτουργικότητα Git):

```bash
# zsh/bash
rm -rf .git
```

```powershell
# PowerShell
Remove-Item -Recurse -Force .git
```

#### Χρήση GitHub Codespaces (συνιστάται για αποφυγή μεγάλων τοπικών λήψεων)

- Δημιουργήστε ένα νέο Codespace για αυτό το αποθετήριο μέσω του [GitHub UI](https://github.com/codespaces).  

- Στο τερματικό του νεοδημιουργημένου Codespace, εκτελέστε μία από τις εντολές απλής/αραιής κλωνοποίησης πιο πάνω για να φέρετε μόνο τους φακέλους μάθησης που χρειάζεστε στον χώρο εργασίας του Codespace.
- Προαιρετικό: μετά την κλωνοποίηση μέσα στα Codespaces, αφαιρέστε το .git για να ανακτήσετε επιπλέον χώρο (δείτε τις εντολές αφαίρεσης πιο πάνω).
- Σημείωση: Αν προτιμάτε να ανοίξετε το αποθετήριο απευθείας στα Codespaces (χωρίς επιπλέον κλωνοποίηση), να γνωρίζετε ότι τα Codespaces θα κατασκευάσουν το περιβάλλον devcontainer και μπορεί να προμηθεύσουν περισσότερο από ό,τι χρειάζεστε.

#### Συμβουλές

- Πάντα αντικαθιστάτε το URL κλωνοποίησης με το δικό σας αν θέλετε να κάνετε επεξεργασία/καταχώρηση.
- Αν χρειαστείτε αργότερα περισσότερα ιστορικά ή αρχεία, μπορείτε να τα ανακτήσετε ή να προσαρμόσετε το sparse-checkout για να συμπεριλάβετε επιπλέον φακέλους.

## Εκτέλεση του Κώδικα

Αυτό το μάθημα προσφέρει μια σειρά από Jupyter Notebooks που μπορείτε να εκτελέσετε για να αποκτήσετε πρακτική εμπειρία στην κατασκευή AI Agents.

Τα δείγματα κώδικα χρησιμοποιούν το **Microsoft Agent Framework (MAF)** με το `FoundryChatClient`, που συνδέεται με την **Microsoft Foundry Agent Service V2** (το Responses API) μέσω του **Microsoft Foundry**.

Όλα τα Python notebooks έχουν την ετικέτα `*-python-agent-framework.ipynb`.

## Απαιτήσεις

- Python 3.12+
  - **ΣΗΜΕΙΩΣΗ**: Αν δεν έχετε εγκαταστήσει την Python3.12, βεβαιωθείτε ότι την εγκαθιστάτε. Στη συνέχεια, δημιουργήστε το venv χρησιμοποιώντας python3.12 για να βεβαιωθείτε ότι οι σωστές εκδόσεις εγκαθίστανται από το αρχείο requirements.txt.
  
    >Παράδειγμα

    Δημιουργήστε φάκελο venv Python:

    ```bash
    python -m venv venv
    ```

    Έπειτα ενεργοποιήστε το περιβάλλον venv για:

    ```bash
    # zsh/bash
    source venv/bin/activate
    ```
  
    ```dos
    # Command Prompt for Windows
    venv\Scripts\activate
    ```

- .NET 10+: Για τα δείγματα κώδικα που χρησιμοποιούν .NET, βεβαιωθείτε ότι έχετε εγκαταστήσει το [.NET 10 SDK](https://dotnet.microsoft.com/download/dotnet/10.0) ή νεότερο. Στη συνέχεια, ελέγξτε την εγκατεστημένη έκδοση .NET SDK:

    ```bash
    dotnet --list-sdks
    ```

- **Azure CLI** — Απαιτείται για ταυτοποίηση. Εγκαταστήστε από [aka.ms/installazurecli](https://aka.ms/installazurecli).
- **Azure Subscription** — Για πρόσβαση σε Microsoft Foundry και Microsoft Foundry Agent Service.
- **Microsoft Foundry Project** — Ένα έργο με αναπτυγμένο μοντέλο (π.χ., `gpt-5-mini`). Δείτε [Βήμα 1](#βήμα-1-δημιουργήστε-ένα-έργο-microsoft-foundry) παρακάτω.

Έχουμε συμπεριλάβει ένα αρχείο `requirements.txt` στη ρίζα αυτού του αποθετηρίου που περιέχει όλα τα απαραίτητα πακέτα Python για να εκτελέσετε τα δείγματα κώδικα.

Μπορείτε να τα εγκαταστήσετε εκτελώντας την παρακάτω εντολή στο τερματικό σας στη ρίζα του αποθετηρίου:

```bash
pip install -r requirements.txt
```

Συνιστούμε να δημιουργήσετε ένα εικονικό περιβάλλον Python για να αποφύγετε τυχόν συγκρούσεις και προβλήματα.

## Ρύθμιση VSCode

Βεβαιωθείτε ότι χρησιμοποιείτε τη σωστή έκδοση της Python στο VSCode.

![image](https://github.com/user-attachments/assets/a85e776c-2edb-4331-ae5b-6bfdfb98ee0e)

## Ρύθμιση Microsoft Foundry και Microsoft Foundry Agent Service

### Βήμα 1: Δημιουργήστε ένα Έργο Microsoft Foundry

Χρειάζεστε ένα Microsoft Foundry **hub** και **έργο** με αναπτυγμένο μοντέλο για να τρέξετε τα notebooks.

1. Μεταβείτε στο [ai.azure.com](https://ai.azure.com) και συνδεθείτε με το λογαριασμό σας Azure.
2. Δημιουργήστε ένα **hub** (ή χρησιμοποιήστε ένα υπάρχον). Δείτε: [Επισκόπηση πόρων Hub](https://learn.microsoft.com/azure/ai-foundry/concepts/ai-resources).
3. Μέσα στο hub, δημιουργήστε ένα **έργο**.
4. Αναπτύξτε ένα μοντέλο (π.χ., `gpt-5-mini`) από **Models + Endpoints** → **Deploy model**.

### Βήμα 2: Αποκτήστε τη Διεύθυνση Τερματισμού (Endpoint) του Έργου και το Όνομα Ανάπτυξης Μοντέλου

Από το έργο σας στην πύλη Microsoft Foundry:

- **Project Endpoint** — Μεταβείτε στη σελίδα **Overview** και αντιγράψτε το URL τερματισμού.

![Project Connection String](../../../translated_images/el/project-endpoint.8cf04c9975bbfbf1.webp)

- **Model Deployment Name** — Μεταβείτε σε **Models + Endpoints**, επιλέξτε το αναπτυγμένο μοντέλο σας και σημειώστε το **Όνομα Ανάπτυξης** (π.χ., `gpt-5-mini`).

### Βήμα 3: Συνδεθείτε στο Azure με `az login`

Τα περισσότερα notebooks ταυτοποιούνται μέσω της **Azure CLI σύνδεσής σας** — χρησιμοποιώντας `AzureCliCredential` ή `DefaultAzureCredential` (τα οποία αναγνωρίζουν τη συνεδρία `az login`) από το πακέτο `azure-identity` — οπότε δεν απαιτούνται κλειδιά API. Μερικά μαθήματα και προαιρετικές ολοκληρώσεις χρησιμοποιούν κλειδιά API· ελέγξτε τις προϋποθέσεις κάθε μαθήματος για τυχόν επιπλέον μεταβλητές περιβάλλοντος. Αυτό απαιτεί να είστε συνδεδεμένοι μέσω της Azure CLI.

1. **Εγκαταστήστε την Azure CLI** αν δεν την έχετε ήδη: [aka.ms/installazurecli](https://aka.ms/installazurecli)

2. **Συνδεθείτε** εκτελώντας:

    ```bash
    az login
    ```

    Ή αν βρίσκεστε σε απομακρυσμένο περιβάλλον/Codespace χωρίς πρόγραμμα περιήγησης:

    ```bash
    az login --use-device-code
    ```

3. **Επιλέξτε τη συνδρομή σας** αν σας ζητηθεί — επιλέξτε αυτή που περιέχει το έργο Foundry σας.

4. **Επιβεβαιώστε** ότι είστε συνδεδεμένοι:

    ```bash
    az account show
    ```

> **Γιατί `az login`;** Τα notebooks ταυτοποιούνται χρησιμοποιώντας `AzureCliCredential` (ή `DefaultAzureCredential`, που επίσης αναγνωρίζει τη σύνδεση Azure CLI) από το πακέτο `azure-identity`. Αυτό σημαίνει ότι η συνεδρία Azure CLI παρέχει τα διαπιστευτήρια — δεν απαιτούνται κλειδιά API ή μυστικά στο αρχείο `.env`. Αυτή είναι μια [καλύτερη πρακτική ασφάλειας](https://learn.microsoft.com/azure/developer/ai/keyless-connections).

### Βήμα 4: Δημιουργήστε το αρχείο `.env`

Αντιγράψτε το παράδειγμα αρχείο:

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
AZURE_AI_MODEL_DEPLOYMENT_NAME=gpt-5-mini
```

| Μεταβλητή | Πού να την βρείτε |
|----------|-----------------|
| `AZURE_AI_PROJECT_ENDPOINT` | Πύλη Foundry → το έργο σας → σελίδα **Overview** |
| `AZURE_AI_MODEL_DEPLOYMENT_NAME` | Πύλη Foundry → **Models + Endpoints** → το όνομα του αναπτυγμένου μοντέλου σας |

Αυτό είναι όλο για τα περισσότερα μαθήματα! Τα notebooks θα αυθεντικοποιούνται αυτόματα μέσω της συνεδρίας `az login` σας.

### Βήμα 5: Εγκαταστήστε τις Εξαρτήσεις Python

```bash
pip install -r requirements.txt
```

Συνιστούμε να εκτελέσετε αυτό μέσα στο εικονικό περιβάλλον που δημιουργήσατε νωρίτερα.

## Προαιρετική Ρύθμιση: Azure AI Search (Μαθήματα 5 και 16)

Τα notebooks του μαθήματος 5 (Agentic RAG) και 16 λειτουργούν άμεσα με μια **εσωτερική βάση γνώσης στη μνήμη** — δεν χρειάζονται επιπλέον πόρους Azure. Αν θέλετε να τα υποστηρίξετε με έναν πραγματικό ευρετήριο **Azure AI Search**, σημειώστε ότι το **Notebook του μαθήματος 16 χρησιμοποιεί προς το παρόν αυθεντικοποίηση με κλειδί**: μεταβαίνει από αναζήτηση στη μνήμη σε Azure AI Search μόνο όταν **και** οι `AZURE_SEARCH_SERVICE_ENDPOINT` **και** `AZURE_SEARCH_API_KEY` έχουν οριστεί, αλλιώς παραμένει στην αναζήτηση στη μνήμη — έτσι για να το χρησιμοποιήσετε με πραγματικό ευρετήριο πρέπει να ορίσετε και το κλειδί διαχειριστή. Η αυθεντικοποίηση χωρίς κλειδί με Microsoft Entra ID (RBAC) είναι η συνιστώμενη προσέγγιση για τον δικό σας παραγωγικό κώδικα, σύμφωνα με τη ροή `az login` που χρησιμοποιείται παντού σε αυτό το μάθημα.

Τα βήματα RBAC πιο κάτω εφαρμόζονται στα δείγματα του οδηγού ρύθμισης και στον δικό σας κώδικα. Δεν ενεργοποιούν την αυθεντικοποίηση χωρίς κλειδί στο Notebook του μαθήματος 16· το μάθημα 16 εξακολουθεί να απαιτεί και το endpoint και το κλειδί διαχειριστή για χρήση του Azure AI Search.

1. **Ενεργοποιήστε την πρόσβαση βάσει ρόλων** στην υπηρεσία αναζήτησής σας:

    ```bash
    az search service update --name <service-name> --resource-group <resource-group> --auth-options aadOrApiKey
    ```

2. **Αναθέστε στον εαυτό σας τους απαιτούμενους ρόλους** (δημιουργία/φόρτωση ευρετηρίων και ερωτήματα):

    ```bash
    az role assignment create --assignee <your-user-or-principal-id> --role "Search Service Contributor" --scope $(az search service show -g <resource-group> -n <service-name> --query id -o tsv)
    az role assignment create --assignee <your-user-or-principal-id> --role "Search Index Data Contributor" --scope $(az search service show -g <resource-group> -n <service-name> --query id -o tsv)
    ```

3. **Προσθέστε το endpoint** στο αρχείο `.env` σας:

| Μεταβλητή | Πού να την βρείτε |
|----------|-----------------|
| `AZURE_SEARCH_SERVICE_ENDPOINT` | Πύλη Azure → τον πόρο **Azure AI Search** → **Overview** → URL |
| `AZURE_SEARCH_API_KEY` | Απαραίτητο (με το endpoint) για ενεργοποίηση Azure AI Search στο Notebook του μαθήματος 16, που χρησιμοποιεί αυθεντικοποίηση με κλειδί. Πύλη Azure → **Settings** → **Keys** → βασικό κλειδί διαχειριστή |

> **Γιατί χωρίς κλειδί;** Τα κλειδιά διαχειριστή παρέχουν πλήρη πρόσβαση εγγραφής στην υπηρεσία αναζήτησης και μπορούν να διαρρεύσουν μέσω αρχείων `.env`. Με RBAC, χρησιμοποιείται η ταυτότητα `az login` σας — το ίδιο μοτίβο χωρίς κλειδί Entra ID που χρησιμοποιούν τα notebooks του μαθήματος (μέσω `AzureCliCredential` / `DefaultAzureCredential`). Δείτε [Σύνδεση με Azure AI Search χρησιμοποιώντας ρόλους](https://learn.microsoft.com/azure/search/search-security-rbac).

Δείτε τον [οδηγό ρύθμισης Azure AI Search](./AzureSearch.md) για ολοκληρωμένα δείγματα δημιουργίας ευρετηρίου σε Python και .NET.

## Πρόσθετη Ρύθμιση για Μαθήματα που Καλούν απευθείας Azure OpenAI (Μαθήματα 6 και 8)

Μερικά notebooks στα μαθήματα 6 και 8 καλούν **Azure OpenAI** απευθείας (χρησιμοποιώντας το **Responses API**) αντί να περάσουν από ένα έργο Microsoft Foundry. Αυτά τα δείγματα προηγουμένως χρησιμοποιούσαν Μοντέλα GitHub, που είναι παρωχημένα και δεν υποστηρίζουν το Responses API. Προσθέστε αυτές τις μεταβλητές στο αρχείο `.env` σας:

| Μεταβλητή | Πού να την βρείτε |
|----------|-----------------|
| `AZURE_OPENAI_ENDPOINT` | Πύλη Azure → τον πόρο **Azure OpenAI** → **Keys and Endpoint** → Τερματισμός (π.χ. `https://<your-resource>.openai.azure.com`) |
| `AZURE_OPENAI_DEPLOYMENT` | Το όνομα του αναπτυγμένου μοντέλου σας (π.χ. `gpt-5-mini`) που υποστηρίζει το Responses API |
| `AZURE_OPENAI_API_KEY` | Προαιρετικό — μόνο αν χρησιμοποιείτε αυθεντικοποίηση με κλειδί αντί για `az login` / Entra ID |

> Το Responses API χρησιμοποιεί το σταθερό endpoint `/openai/v1/`, οπότε δεν απαιτείται `api-version`. Συνδεθείτε με `az login` για να χρησιμοποιήσετε αυθεντικοποίηση χωρίς κλειδί Entra ID.

## Εναλλακτικός Πάροχος: MiniMax (Συμβατός με OpenAI)

[MiniMax](https://platform.minimaxi.com/) παρέχει μοντέλα μεγάλης διάρκειας συμφραζομένων (έως 204K tokens) μέσω συμβατού API με το OpenAI. Επειδή το `OpenAIChatClient` του Microsoft Agent Framework λειτουργεί με οποιοδήποτε συμβατό endpoint OpenAI, μπορείτε να χρησιμοποιήσετε το MiniMax ως εναλλακτική λύση για τα μαθήματα που χρησιμοποιούν `OpenAIChatClient`.

Προσθέστε αυτές τις μεταβλητές στο αρχείο `.env` σας:

| Μεταβλητή | Πού να την βρείτε |
|----------|-----------------|
| `MINIMAX_API_KEY` | [MiniMax Platform](https://platform.minimaxi.com/) → Κλειδιά API |
| `MINIMAX_BASE_URL` | Χρησιμοποιήστε `https://api.minimax.io/v1` (προεπιλεγμένη τιμή) |
| `MINIMAX_MODEL_ID` | Όνομα μοντέλου προς χρήση (π.χ., `MiniMax-M3`) |

**Παραδείγματα μοντέλων**: `MiniMax-M3` (συνιστάται), `MiniMax-M2.7`, `MiniMax-M2.7-highspeed` (γρηγορότερες απαντήσεις). Τα ονόματα και η διαθεσιμότητα μοντέλων μπορούν να αλλάξουν με το χρόνο, και η πρόσβαση σε συγκεκριμένο μοντέλο μπορεί να εξαρτάται από το λογαριασμό σας.

Τα δείγματα κώδικα που χρησιμοποιούν `OpenAIChatClient` (π.χ., ροή κράτησης ξενοδοχείου στο μάθημα 14) θα ανιχνεύουν και θα χρησιμοποιούν αυτόματα τη διαμόρφωση MiniMax σας όταν έχει οριστεί το `MINIMAX_API_KEY`.


## Εναλλακτικός Πάροχος: Foundry Local (Εκτέλεση Μοντέλων Τοπικά)

[Foundry Local](https://foundrylocal.ai) είναι ένα ελαφρύ runtime που κατεβάζει, διαχειρίζεται, και εξυπηρετεί γλωσσικά μοντέλα **αποκλειστικά στη δική σου μηχανή** μέσω ενός API συμβατού με OpenAI — χωρίς να απαιτείται cloud.

Επειδή το `OpenAIChatClient` του Microsoft Agent Framework δουλεύει με οποιονδήποτε συμβατό endpoint OpenAI, το Foundry Local είναι μια τοπική επιλογή που αντικαθιστά το Azure OpenAI.

**1. Εγκατάσταση Foundry Local**

```bash
# Windows
winget install Microsoft.FoundryLocal

# macOS
brew install foundrylocal
```

**2. Κατεβάστε και εκτελέστε ένα μοντέλο** (αυτό ξεκινά και την τοπική υπηρεσία):

```bash
foundry model list          # δείτε διαθέσιμα μοντέλα
foundry model run phi-4-mini
```

**3. Εγκαταστήστε το Python SDK** που χρησιμοποιείται για την ανακάλυψη του τοπικού endpoint:

```bash
pip install foundry-local-sdk
```

**4. Διευθύνετε το Microsoft Agent Framework προς το τοπικό σας μοντέλο:**

```python
from foundry_local import FoundryLocalManager
from agent_framework.openai import OpenAIChatClient

# Κατεβάζει (αν χρειάζεται) και εξυπηρετεί το μοντέλο τοπικά, στη συνέχεια ανακαλύπτει το endpoint/θύρα.
manager = FoundryLocalManager("phi-4-mini")

chat_client = OpenAIChatClient(
    base_url=manager.endpoint,      # π.χ. http://localhost:<port>/v1
    api_key=manager.api_key,        # πάντα "μη-απαιτούμενο" για το Foundry Local
    model_id=manager.get_model_info("phi-4-mini").id,
)

agent = chat_client.as_agent(
    name="LocalAgent",
    instructions="You are a helpful assistant running fully on-device.",
)
```

> **Σημείωση:** Το Foundry Local παρέχει έναν OpenAI-συμβατό endpoint για **Chat Completions**. Χρησιμοποιήστε το για τοπική ανάπτυξη και σενάρια χωρίς σύνδεση. Για το πλήρες σύνολο λειτουργιών του **Responses API** (συνομιλίες με κατάσταση, κ.ά.), χρησιμοποιήστε το Azure OpenAI ή ένα έργο Microsoft Foundry.

## Επιπλέον Ρυθμίσεις για το Μάθημα 8 (Διαδικασία Bing Grounding)

Το notebook με τη συνθήκη ροής εργασίας στο μάθημα 8 χρησιμοποιεί **Bing grounding** μέσω Microsoft Foundry. Αν σκοπεύετε να τρέξετε αυτό το παράδειγμα, προσθέστε αυτήν τη μεταβλητή στο αρχείο `.env` σας:

| Μεταβλητή | Πού να την βρείτε |
|----------|-----------------|
| `BING_CONNECTION_ID` | Πύλη Microsoft Foundry → το έργο σας → **Διαχείριση** → **Συνδεδεμένοι πόροι** → η σύνδεση Bing σας → αντιγράψτε το ID σύνδεσης |

## Αντιμετώπιση Προβλημάτων

### Σφάλματα Επαλήθευσης Πιστοποιητικού SSL σε macOS

Αν χρησιμοποιείτε macOS και συναντήσετε σφάλμα όπως:

```plaintext
ssl.SSLCertVerificationError: [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: self-signed certificate in certificate chain
```

Αυτό είναι ένα γνωστό πρόβλημα με το Python σε macOS όπου τα συστήματα πιστοποιητικών SSL δεν γίνονται αυτόματα αξιόπιστα. Δοκιμάστε τις παρακάτω λύσεις με τη σειρά:

**Επιλογή 1: Εκτελέστε το script εγκατάστασης πιστοποιητικών του Python (συνιστάται)**

```bash
# Αντικαταστήστε το 3.XX με την εγκατεστημένη έκδοση Python σας (π.χ., 3.12 ή 3.13):
/Applications/Python\ 3.XX/Install\ Certificates.command
```

**Επιλογή 2: Χρησιμοποιήστε `connection_verify=False` στο notebook σας (μόνο για notebooks GitHub Models)**

Στο notebook του Μαθήματος 6 (`06-building-trustworthy-agents/code_samples/06-system-message-framework.ipynb`), υπάρχει ήδη μια σχολιασμένη παρακάμψη. Αποσχολιάστε το `connection_verify=False` όταν συναντήσετε σφάλματα πιστοποιητικού:

```python
client = ChatCompletionsClient(
    endpoint=endpoint,
    credential=AzureKeyCredential(token),
    connection_verify=False,  # Απενεργοποιήστε την επαλήθευση SSL εάν αντιμετωπίσετε σφάλματα πιστοποιητικών
)
```

> **⚠️ Προειδοποίηση:** Η απενεργοποίηση της επαλήθευσης SSL (`connection_verify=False`) μειώνει την ασφάλεια παρακάμπτοντας την επαλήθευση πιστοποιητικού. Χρησιμοποιήστε το μόνο ως προσωρινή λύση σε περιβάλλοντα ανάπτυξης. Μην το χρησιμοποιείτε σε παραγωγή.

**Επιλογή 3: Εγκαταστήστε και χρησιμοποιήστε το `truststore`**

```bash
pip install truststore
```

Στη συνέχεια, προσθέστε τα παρακάτω στην αρχή του notebook ή του script σας πριν κάνετε κλήσεις δικτύου:

```python
import truststore
truststore.inject_into_ssl()
```

## Μπλοκαρίσατε κάπου;

Αν αντιμετωπίζετε προβλήματα με αυτήν τη ρύθμιση, μπείτε στο <a href="https://discord.gg/kzRShWzttr" target="_blank">Azure AI Community Discord</a> ή <a href="https://github.com/microsoft/ai-agents-for-beginners/issues?WT.mc_id=academic-105485-koreyst" target="_blank">δημιουργήστε ένα issue</a>.

## Επόμενο Μάθημα

Τώρα είστε έτοιμοι να τρέξετε τον κώδικα για αυτό το μάθημα. Καλή εκμάθηση στον κόσμο των AI Agents! 

[Introduction to AI Agents and Agent Use Cases](../01-intro-to-ai-agents/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Αποποίηση ευθυνών**:
Αυτό το έγγραφο έχει μεταφραστεί χρησιμοποιώντας την υπηρεσία μετάφρασης με τεχνητή νοημοσύνη [Co-op Translator](https://github.com/Azure/co-op-translator). Ενώ επιδιώκουμε την ακρίβεια, παρακαλούμε να έχετε υπόψη ότι οι αυτοματοποιημένες μεταφράσεις ενδέχεται να περιέχουν λάθη ή ανακρίβειες. Το πρωτότυπο έγγραφο στη μητρική του γλώσσα πρέπει να θεωρείται η αυθεντική πηγή. Για κρίσιμες πληροφορίες, συνιστάται επαγγελματική ανθρώπινη μετάφραση. Δεν φέρουμε ευθύνη για τυχόν παρεξηγήσεις ή λανθασμένες ερμηνείες που προκύπτουν από τη χρήση αυτής της μετάφρασης.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->