# Ρύθμιση Μαθήματος

## Εισαγωγή

Αυτό το μάθημα θα καλύψει το πώς να εκτελέσετε τα δείγματα κώδικα αυτού του μαθήματος.

## Ενταχθείτε σε Άλλους Μαθητευόμενους και Λάβετε Βοήθεια

Πριν ξεκινήσετε να κλωνοποιείτε το αποθετήριο σας, ενταχθείτε στο [AI Agents For Beginners Discord κανάλι](https://aka.ms/ai-agents/discord) για να λάβετε οποιαδήποτε βοήθεια με τη ρύθμιση, ερωτήσεις σχετικά με το μάθημα ή για να συνδεθείτε με άλλους μαθητευόμενους.

## Κλωνοποιήστε ή Φορκάρετε αυτό το Αποθετήριο

Για να ξεκινήσετε, παρακαλώ κλωνοποιήστε ή φορκάρετε το GitHub Αποθετήριο. Αυτό θα δημιουργήσει τη δική σας έκδοση του υλικού του μαθήματος ώστε να μπορείτε να εκτελέσετε, να δοκιμάσετε και να τροποποιήσετε τον κώδικα!

Αυτό μπορεί να γίνει κάνοντας κλικ στον σύνδεσμο για <a href="https://github.com/microsoft/ai-agents-for-beginners/fork" target="_blank">φορκάρισμα του αποθετηρίου</a>

Πλέον θα πρέπει να έχετε τη δική σας φορκάρισμένη έκδοση αυτού του μαθήματος στον ακόλουθο σύνδεσμο:

![Forked Repo](../../../translated_images/el/forked-repo.33f27ca1901baa6a.webp)

### Επιφανειακό Κλωνάρισμα (συνιστάται για εργαστήρια / Codespaces)

  >Ολόκληρο το αποθετήριο μπορεί να είναι μεγάλο (~3 GB) όταν κατεβάζετε όλη την ιστορία και όλα τα αρχεία. Αν παρακολουθείτε μόνο το εργαστήριο ή χρειάζεστε μόνο μερικούς φακέλους μαθημάτων, ένα επιφανειακό κλωνάρισμα (ή ένα αραιό κλωνάρισμα) κατεβάζει πολύ λιγότερα.

#### Γρήγορο επιφανειακό κλωνάρισμα — ελάχιστο ιστορικό, όλα τα αρχεία

Αντικαταστήστε το `<your-username>` στις παρακάτω εντολές με το URL του φορκ σας (ή το upstream URL αν προτιμάτε).

Για να κλωνοποιήσετε μόνο το πιο πρόσφατο ιστορικό κωδικών (μικρό λήψη):

```bash
git clone --depth 1 https://github.com/<your-username>/ai-agents-for-beginners.git
```

Για να κλωνοποιήσετε ένα συγκεκριμένο branch:

```bash
git clone --depth 1 --branch <branch-name> https://github.com/<your-username>/ai-agents-for-beginners.git
```

#### Μερικό (αραιό) κλωνάρισμα — ελάχιστα blobs + μόνο επιλεγμένοι φάκελοι

Αυτό χρησιμοποιεί μερικό κλωνάρισμα και sparse-checkout (απαιτεί Git 2.25+ και συνιστάται σύγχρονο Git με υποστήριξη μερικού κλωναρίσματος):

```bash
git clone --depth 1 --filter=blob:none --sparse https://github.com/<your-username>/ai-agents-for-beginners.git
```

Πλοηγηθείτε στον φάκελο του αποθετηρίου:

```bash
cd ai-agents-for-beginners
```

Έπειτα ορίστε ποιοι φάκελοι θέλετε (το παράδειγμα παρακάτω δείχνει δύο φακέλους):

```bash
git sparse-checkout set 00-course-setup 01-intro-to-ai-agents
```

Μετά το κλωνάρισμα και την επαλήθευση των αρχείων, αν χρειάζεστε μόνο αρχεία και θέλετε να ελευθερώσετε χώρο (χωρίς ιστορικό git), διαγράψτε τα μεταδεδομένα του αποθετηρίου (💀μη αναστρέψιμο — θα χάσετε όλη τη λειτουργικότητα του Git):

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

- Στο τερματικό του νέου codespace, τρέξτε μία από τις εντολές για επιφανειακό/αραιό κλωνάρισμα παραπάνω για να φέρετε μόνο τους φακέλους μαθημάτων που χρειάζεστε στο χώρο εργασίας Codespace.
- Προαιρετικά: μετά το κλωνάρισμα μέσα σε Codespaces, αφαιρέστε το .git για να ανακτήσετε επιπλέον χώρο (δείτε τις εντολές αφαίρεσης παραπάνω).
- Σημείωση: Αν προτιμάτε να ανοίξετε το αποθετήριο απευθείας σε Codespaces (χωρίς επιπλέον κλωνάρισμα), να γνωρίζετε ότι το Codespaces θα δημιουργήσει το περιβάλλον devcontainer και μπορεί να παραμετροποιήσει περισσότερα απ' όσα χρειάζεστε.

#### Συμβουλές

- Πάντα αντικαταστήστε το URL του κλώνου με αυτό του φορκ σας αν θέλετε να επεξεργαστείτε/κάνετε commit.
- Αν αργότερα χρειαστείτε περισσότερο ιστορικό ή αρχεία, μπορείτε να τα κατεβάσετε ή να προσαρμόσετε το sparse-checkout για να συμπεριλάβετε επιπλέον φακέλους.

## Εκτέλεση του Κώδικα

Αυτό το μάθημα προσφέρει μια σειρά από Jupyter Notebooks που μπορείτε να εκτελέσετε για να αποκτήσετε πρακτική εμπειρία στην κατασκευή AI Agents.

Τα δείγματα κώδικα χρησιμοποιούν το **Microsoft Agent Framework (MAF)** με τον `FoundryChatClient`, που συνδέεται με την **Microsoft Foundry Agent Service V2** (το Responses API) μέσα από τη **Microsoft Foundry**.

Όλα τα Python notebooks είναι επισημασμένα με `*-python-agent-framework.ipynb`.

## Απαιτήσεις

- Python 3.12+
  - **ΣΗΜΕΙΩΣΗ**: Αν δεν έχετε εγκαταστήσει το Python3.12, βεβαιωθείτε ότι το εγκαθιστάτε. Έπειτα δημιουργήστε το venv σας χρησιμοποιώντας python3.12 για να εξασφαλίσετε ότι οι σωστές εκδόσεις εγκαθίστανται από το αρχείο requirements.txt.
  
    >Παράδειγμα

    Δημιουργία φακέλου Python venv:

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

- .NET 10+: Για τα δείγματα κώδικα που χρησιμοποιούν .NET, βεβαιωθείτε ότι εγκαθιστάτε το [.NET 10 SDK](https://dotnet.microsoft.com/download/dotnet/10.0) ή νεότερο. Έπειτα ελέγξτε την έκδοση του εγκατεστημένου σας .NET SDK:

    ```bash
    dotnet --list-sdks
    ```

- **Azure CLI** — Απαραίτητο για αυθεντικοποίηση. Εγκαταστήστε από [aka.ms/installazurecli](https://aka.ms/installazurecli).
- **Azure Συνδρομή** — Για πρόσβαση στη Microsoft Foundry και Microsoft Foundry Agent Service.
- **Microsoft Foundry Project** — Ένα έργο με αναπτυγμένο μοντέλο (π.χ., `gpt-5-mini`). Δείτε το [Βήμα 1](#βήμα-1-δημιουργία-έργου-microsoft-foundry) παρακάτω.

Περιλαμβάνουμε ένα αρχείο `requirements.txt` στον ριζικό φάκελο αυτού του αποθετηρίου που περιέχει όλα τα απαιτούμενα πακέτα Python για την εκτέλεση των δειγμάτων κώδικα.

Μπορείτε να τα εγκαταστήσετε τρέχοντας την ακόλουθη εντολή στο τερματικό σας στον ριζικό φάκελο του αποθετηρίου:

```bash
pip install -r requirements.txt
```

Συνιστούμε να δημιουργήσετε ένα εικονικό περιβάλλον Python για να αποφύγετε τυχόν συγκρούσεις και προβλήματα.

## Ρύθμιση VSCode

Βεβαιωθείτε ότι χρησιμοποιείτε τη σωστή έκδοση Python στο VSCode.

![image](https://github.com/user-attachments/assets/a85e776c-2edb-4331-ae5b-6bfdfb98ee0e)

## Ρύθμιση Microsoft Foundry και Microsoft Foundry Agent Service

### Βήμα 1: Δημιουργία Έργου Microsoft Foundry

Χρειάζεστε ένα **hub** και **έργο** στο Microsoft Foundry με ένα αναπτυγμένο μοντέλο για να τρέξετε τα notebooks.

1. Πηγαίνετε στο [ai.azure.com](https://ai.azure.com) και συνδεθείτε με τον λογαριασμό σας Azure.
2. Δημιουργήστε ένα **hub** (ή χρησιμοποιήστε ένα υπάρχον). Δείτε: [Βασικοί πόροι hub](https://learn.microsoft.com/azure/ai-foundry/concepts/ai-resources).
3. Μέσα στο hub, δημιουργήστε ένα **έργο**.
4. Αναπτύξτε ένα μοντέλο (π.χ., `gpt-5-mini`) από **Models + Endpoints** → **Deploy model**.

### Βήμα 2: Λήψη του Σημείου Τερματισμού Έργου και του Ονόματος Ανάπτυξης Μοντέλου

Από το έργο σας στην πύλη Microsoft Foundry:

- **Project Endpoint** — Μεταβείτε στη σελίδα **Overview** και αντιγράψτε το URL του τελικού σημείου.

![Project Connection String](../../../translated_images/el/project-endpoint.8cf04c9975bbfbf1.webp)

- **Model Deployment Name** — Μεταβείτε σε **Models + Endpoints**, επιλέξτε το αναπτυγμένο μοντέλο σας, και σημειώστε το **Όνομα Ανάπτυξης** (π.χ., `gpt-5-mini`).

### Βήμα 3: Συνδεθείτε στο Azure με `az login`

Τα περισσότερα notebooks αυθεντικοποιούνται μέσω της **Azure CLI σύνδεσης σας** — χρησιμοποιώντας `AzureCliCredential` ή `DefaultAzureCredential` (και τα δύο αντλούν τη συνεδρία `az login`) από το πακέτο `azure-identity` — οπότε δεν απαιτούνται API κλειδιά. Μερικά μαθήματα και προαιρετικές ενσωματώσεις χρησιμοποιούν API κλειδιά· ελέγξτε τις προϋποθέσεις κάθε μαθήματος για πρόσθετες μεταβλητές περιβάλλοντος. Αυτό απαιτεί να είστε συνδεδεμένοι μέσω της Azure CLI.

1. **Εγκαταστήστε το Azure CLI** αν δεν το έχετε ήδη: [aka.ms/installazurecli](https://aka.ms/installazurecli)

2. **Συνδεθείτε** εκτελώντας:

    ```bash
    az login
    ```

    Ή αν βρίσκεστε σε απομακρυσμένο περιβάλλον/Codespace χωρίς πρόγραμμα περιήγησης:

    ```bash
    az login --use-device-code
    ```

3. **Επιλέξτε τη συνδρομή σας** αν ζητηθεί — επιλέξτε αυτή που περιέχει το έργο Foundry σας.

4. **Επαληθεύστε** ότι είστε συνδεδεμένοι:

    ```bash
    az account show
    ```

> **Γιατί `az login`;** Τα notebooks αυθεντικοποιούνται χρησιμοποιώντας `AzureCliCredential` (ή `DefaultAzureCredential`, που επίσης αντλεί τη σύνδεση Azure CLI) από το πακέτο `azure-identity`. Αυτό σημαίνει ότι η συνεδρία Azure CLI παρέχει τα διαπιστευτήρια — δεν χρειάζονται API κλειδιά ή μυστικά στο αρχείο `.env`. Αυτή είναι μία [καλύτερη πρακτική ασφαλείας](https://learn.microsoft.com/azure/developer/ai/keyless-connections).

### Βήμα 4: Δημιουργήστε το αρχείο `.env` σας

Αντιγράψτε το αρχείο παραδείγματος:

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
| `AZURE_AI_MODEL_DEPLOYMENT_NAME` | Πύλη Foundry → **Models + Endpoints** → όνομα του αναπτυγμένου μοντέλου |

Αυτό είναι για τα περισσότερα μαθήματα! Τα notebooks θα αυθεντικοποιηθούν αυτόματα μέσω της συνεδρίας `az login`.

### Βήμα 5: Εγκατάσταση Εξαρτήσεων Python

```bash
pip install -r requirements.txt
```

Συνιστούμε να τρέξετε αυτό μέσα στο εικονικό περιβάλλον που δημιουργήσατε νωρίτερα.

## Προαιρετική Ρύθμιση: Azure AI Search (Μαθήματα 5 και 16)

Τα notebooks του Μαθήματος 5 (Agentic RAG) και Μαθήματος 16 τρέχουν απ’ ευθείας με μία **εσωτερική βάση γνώσης στη μνήμη** — δεν απαιτούνται επιπλέον πόροι Azure. Αν θέλετε να τα υποστηρίξετε με έναν πραγματικό **δείκτη Azure AI Search**, σημειώστε ότι **το notebook του Μαθήματος 16 χρησιμοποιεί προς το παρόν αυθεντικοποίηση με κλειδί**: αλλάζει από την αναζήτηση στη μνήμη στην Azure AI Search μόνο όταν **και οι δύο** `AZURE_SEARCH_SERVICE_ENDPOINT` **και** `AZURE_SEARCH_API_KEY` είναι ορισμένες, αλλιώς παραμένει στην αναζήτηση στη μνήμη — οπότε για να το τρέξετε με πραγματικό δείκτη πρέπει να ορίσετε και το κλειδί διαχειριστή. Η αυθεντικοποίηση χωρίς κλειδιά με το Microsoft Entra ID (RBAC) είναι η συνιστώμενη προσέγγιση για τον δικό σας κώδικα παραγωγής, σύμφωνη με τη ροή `az login` που χρησιμοποιείται σε όλο το μάθημα.

Τα βήματα RBAC παρακάτω ισχύουν για τα δείγματα οδηγού ρύθμισης και τον δικό σας κώδικα. Δεν ενεργοποιούν αυθεντικοποίηση χωρίς κλειδιά στο notebook του Μαθήματος 16· αυτό εξακολουθεί να απαιτεί τόσο το endpoint όσο και το κλειδί διαχειριστή για χρήση Azure AI Search.

1. **Ενεργοποιήστε πρόσβαση βάσει ρόλων** στην υπηρεσία αναζήτησης σας:

    ```bash
    az search service update --name <service-name> --resource-group <resource-group> --auth-options aadOrApiKey
    ```

2. **Αναθέστε στον εαυτό σας τους απαιτούμενους ρόλους** (δημιουργία/φόρτωση δεικτών και ερώτημα):

    ```bash
    az role assignment create --assignee <your-user-or-principal-id> --role "Search Service Contributor" --scope $(az search service show -g <resource-group> -n <service-name> --query id -o tsv)
    az role assignment create --assignee <your-user-or-principal-id> --role "Search Index Data Contributor" --scope $(az search service show -g <resource-group> -n <service-name> --query id -o tsv)
    ```

3. **Προσθέστε το endpoint** στο αρχείο `.env` σας:

| Μεταβλητή | Πού να την βρείτε |
|----------|-----------------|
| `AZURE_SEARCH_SERVICE_ENDPOINT` | Πύλη Azure → ο πόρος σας **Azure AI Search** → **Overview** → URL |
| `AZURE_SEARCH_API_KEY` | Απαραίτητο (μαζί με το endpoint) για ενεργοποίηση Azure AI Search στο notebook του Μαθήματος 16, που χρησιμοποιεί αυθεντικοποίηση με κλειδί. Πύλη Azure → **Settings** → **Keys** → πρωτεύον κλειδί διαχειριστή |

> **Γιατί χωρίς κλειδιά;** Τα κλειδιά διαχειριστή παρέχουν πλήρη πρόσβαση εγγραφής στην υπηρεσία αναζήτησης και μπορούν να διαρρεύσουν μέσω αρχείων `.env`. Με RBAC, χρησιμοποιείται η ταυτότητα σύνδεσης `az login` — το ίδιο πρότυπο χωρίς κλειδιά Entra ID που χρησιμοποιούν τα notebooks του μαθήματος (μέσω `AzureCliCredential` / `DefaultAzureCredential`). Δείτε [Σύνδεση στο Azure AI Search χρησιμοποιώντας ρόλους](https://learn.microsoft.com/azure/search/search-security-rbac).

Δείτε τον [οδηγό ρύθμισης Azure AI Search](./AzureSearch.md) για πλήρη δείγματα δημιουργίας δεικτών σε Python και .NET.

## Επιπλέον Ρύθμιση για Μαθήματα που Καλούν απευθείας Azure OpenAI (Μαθήματα 6 και 8)

Μερικά notebooks στα μαθήματα 6 και 8 καλούν το **Azure OpenAI** απευθείας (χρησιμοποιώντας το **Responses API**) αντί να περάσουν μέσω έργου Microsoft Foundry. Αυτά τα δείγματα χρησιμοποιούσαν προηγουμένως GitHub Models, που καταργήθηκε και δεν υποστηρίζει το Responses API. Προσθέστε αυτές τις μεταβλητές στο αρχείο `.env` σας:

| Μεταβλητή | Πού να την βρείτε |
|----------|-----------------|
| `AZURE_OPENAI_ENDPOINT` | Πύλη Azure → πόρος σας **Azure OpenAI** → **Keys and Endpoint** → Endpoint (π.χ. `https://<your-resource>.openai.azure.com`) |
| `AZURE_OPENAI_DEPLOYMENT` | Το όνομα του αναπτυγμένου μοντέλου σας (π.χ. `gpt-5-mini`) που υποστηρίζει το Responses API |
| `AZURE_OPENAI_API_KEY` | Προαιρετικό — μόνο αν χρησιμοποιείτε αυθεντικοποίηση με κλειδί αντί για `az login` / Entra ID |

> Το Responses API χρησιμοποιεί το σταθερό endpoint `/openai/v1/`, οπότε δεν απαιτείται `api-version`. Κάντε σύνδεση με `az login` για να χρησιμοποιήσετε αυθεντικοποίηση χωρίς κλειδιά Entra ID.

## Εναλλακτικός Πάροχος: MiniMax (Συμβατό με OpenAI)

[MiniMax](https://platform.minimaxi.com/) παρέχει μοντέλα με μεγάλο πλαίσιο συμφραζομένων (έως 204K tokens) μέσω συμβατού με OpenAI API. Επειδή το Microsoft Agent Framework's `OpenAIChatClient` λειτουργεί με οποιοδήποτε συμβατό με OpenAI endpoint, μπορείτε να χρησιμοποιήσετε το MiniMax ως λύση αντικατάστασης για μαθήματα που χρησιμοποιούν `OpenAIChatClient`.

Προσθέστε αυτές τις μεταβλητές στο αρχείο `.env` σας:

| Μεταβλητή | Πού να την βρείτε |
|----------|-----------------|
| `MINIMAX_API_KEY` | [MiniMax Platform](https://platform.minimaxi.com/) → API Keys |
| `MINIMAX_BASE_URL` | Χρησιμοποιήστε `https://api.minimax.io/v1` (προεπιλεγμένη τιμή) |
| `MINIMAX_MODEL_ID` | Το όνομα του μοντέλου για χρήση (π.χ., `MiniMax-M3`) |

**Παραδείγματα μοντέλων**: `MiniMax-M3` (συνιστώμενο), `MiniMax-M2.7`, `MiniMax-M2.7-highspeed` (ταχύτερες απαντήσεις). Τα ονόματα μοντέλων και η διαθεσιμότητα μπορεί να αλλάζουν με την πάροδο του χρόνου, και η πρόσβαση σε κάθε μοντέλο μπορεί να εξαρτάται από τον λογαριασμό σας.

Τα δείγματα κώδικα που χρησιμοποιούν `OpenAIChatClient` (π.χ., λειτουργία κράτησης ξενοδοχείου του Μαθήματος 14) θα εντοπίσουν και θα χρησιμοποιήσουν αυτόματα τη διαμόρφωση MiniMax σας όταν το `MINIMAX_API_KEY` είναι ορισμένο.


## Εναλλακτικός Πάροχος: Novita AI (Συμβατό με OpenAI)

[Novita AI](https://novita.ai/llm-api) παρέχει ένα API συμβατό με OpenAI για ανοιχτού κώδικα και frontier LLMs (DeepSeek, Llama, Qwen, και άλλα). Εφόσον το `OpenAIChatClient` του Microsoft Agent Framework λειτουργεί με οποιοδήποτε endpoint συμβατό με OpenAI, μπορείτε να χρησιμοποιήσετε το Novita AI ως εναλλακτική λύση αντικατάστασης για το Azure OpenAI ή OpenAI.

Προσθέστε αυτές τις μεταβλητές στο αρχείο `.env` σας:

| Μεταβλητή | Πού να τη βρείτε |
|----------|-----------------|
| `NOVITA_API_KEY` | [Novita AI Dashboard](https://novita.ai/settings/key-management) → API Keys |
| `NOVITA_BASE_URL` | Χρησιμοποιήστε `https://api.novita.ai/openai/v1` (προεπιλεγμένη τιμή) |
| `NOVITA_MODEL_ID` | Όνομα μοντέλου προς χρήση (π.χ., `moonshotai/kimi-k3`) |

**Παραδείγματα μοντέλων**: `moonshotai/kimi-k3`, `zai-org/glm-5.2`, `deepseek/deepseek-v4-flash-0731`. Το Novita AI φιλοξενεί επίσης πολλές άλλες οικογένειες ανοιχτού κώδικα μοντέλων (Llama, Qwen, GLM, και άλλα) — ελέγξτε τη [βιβλιοθήκη μοντέλων Novita AI](https://novita.ai/llm-api) για την τρέχουσα λίστα διαθέσιμων μοντέλων και τα IDs τους.

Τα τρέχοντα δείγματα δεν καταναλώνουν αυτόματα τις μεταβλητές `NOVITA_*`. Για να χρησιμοποιήσετε το Novita AI, περάστε αυτές τις τιμές ρητά κατά την κατασκευή του `OpenAIChatClient` στο δείγμα που τρέχετε.

## Εναλλακτικός Πάροχος: Foundry Local (Εκτέλεση Μοντέλων στη Συσκευή)

[Foundry Local](https://foundrylocal.ai) είναι ένα ελαφρύ runtime που κατεβάζει, διαχειρίζεται και εξυπηρετεί γλωσσικά μοντέλα **εντελώς στο δικό σας μηχάνημα** μέσω ενός API συμβατού με OpenAI — χωρίς σύννεφο.

Εφόσον το `OpenAIChatClient` του Microsoft Agent Framework λειτουργεί με οποιοδήποτε endpoint συμβατό με OpenAI, το Foundry Local είναι μια τοπική εναλλακτική λύση αντικατάστασης για το Azure OpenAI.

**1. Εγκαταστήστε το Foundry Local**

```bash
# Windows
winget install Microsoft.FoundryLocal

# macOS
brew install foundrylocal
```

**2. Κατεβάστε και τρέξτε ένα μοντέλο** (αυτό ξεκινάει επίσης την τοπική υπηρεσία):

```bash
foundry model list          # δείτε διαθέσιμα μοντέλα
foundry model run phi-4-mini
```

**3. Εγκαταστήστε το Python SDK** που χρησιμοποιείται για την ανακάλυψη τοπικού endpoint:

```bash
pip install foundry-local-sdk
```

**4. Κατευθύνετε το Microsoft Agent Framework στο τοπικό σας μοντέλο:**

```python
from foundry_local import FoundryLocalManager
from agent_framework.openai import OpenAIChatClient

# Κατεβάζει (αν χρειάζεται) και εξυπηρετεί το μοντέλο τοπικά, στη συνέχεια εντοπίζει το endpoint/port.
manager = FoundryLocalManager("phi-4-mini")

chat_client = OpenAIChatClient(
    base_url=manager.endpoint,      # π.χ. http://localhost:<port>/v1
    api_key=manager.api_key,        # πάντα "not-required" για Foundry Local
    model_id=manager.get_model_info("phi-4-mini").id,
)

agent = chat_client.as_agent(
    name="LocalAgent",
    instructions="You are a helpful assistant running fully on-device.",
)
```

> **Σημείωση:** Το Foundry Local εκθέτει ένα συμβατό με OpenAI endpoint **Chat Completions**. Χρησιμοποιήστε το για τοπική ανάπτυξη και σενάρια εκτός σύνδεσης. Για το πλήρες σύνολο λειτουργιών του **Responses API** (καταστάσεις συνομιλιών, κλπ.), χρησιμοποιήστε Azure OpenAI ή ένα έργο Microsoft Foundry.

## Πρόσθετη Ρύθμιση για το Μάθημα 8 (Workflow Bing Grounding)

Το notebook workflow υπό όρους στο μάθημα 8 χρησιμοποιεί **Bing grounding** μέσω Microsoft Foundry. Αν σκοπεύετε να τρέξετε αυτό το δείγμα, προσθέστε αυτή τη μεταβλητή στο αρχείο `.env` σας:

| Μεταβλητή | Πού να τη βρείτε |
|----------|-----------------|
| `BING_CONNECTION_ID` | Πύλη Microsoft Foundry → το έργο σας → **Management** → **Connected resources** → σύνδεση Bing σας → αντιγράψτε το connection ID |

## Επίλυση Προβλημάτων

### Σφάλματα Επαλήθευσης Πιστοποιητικού SSL σε macOS

Αν είστε σε macOS και συναντήσετε ένα σφάλμα όπως:

```plaintext
ssl.SSLCertVerificationError: [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: self-signed certificate in certificate chain
```

Αυτό είναι ένα γνωστό ζήτημα με το Python σε macOS όπου τα συστήματα πιστοποιητικά SSL δεν εμπιστεύονται αυτόματα. Δοκιμάστε τις ακόλουθες λύσεις με τη σειρά:

**Επιλογή 1: Εκτελέστε το script Install Certificates του Python (συνιστάται)**

```bash
# Αντικαταστήστε το 3.XX με την εγκατεστημένη έκδοση Python σας (π.χ., 3.12 ή 3.13):
/Applications/Python\ 3.XX/Install\ Certificates.command
```

**Επιλογή 2: Χρήση `connection_verify=False` στο notebook σας (μόνο για notebooks GitHub Models)**

Στο notebook του Μαθήματος 6 (`06-building-trustworthy-agents/code_samples/06-system-message-framework.ipynb`), υπάρχει ήδη μια σχολιασμένη προσωρινή λύση. Αποσχολιάστε το `connection_verify=False` όταν συναντήσετε σφάλματα πιστοποιητικών:

```python
client = ChatCompletionsClient(
    endpoint=endpoint,
    credential=AzureKeyCredential(token),
    connection_verify=False,  # Απενεργοποιήστε την επαλήθευση SSL αν συναντήσετε σφάλματα πιστοποιητικού
)
```

> **⚠️ Προειδοποίηση:** Η απενεργοποίηση της επαλήθευσης SSL (`connection_verify=False`) μειώνει την ασφάλεια παρακάμπτοντας την επικύρωση πιστοποιητικών. Χρησιμοποιήστε το μόνο ως προσωρινή λύση σε αναπτυξιακά περιβάλλοντα. Μην το χρησιμοποιείτε ποτέ στην παραγωγή.

**Επιλογή 3: Εγκαταστήστε και χρησιμοποιήστε το `truststore`**

```bash
pip install truststore
```

Στη συνέχεια προσθέστε το παρακάτω στην αρχή του notebook ή του script σας πριν κάνετε οποιαδήποτε κλήση δικτύου:

```python
import truststore
truststore.inject_into_ssl()
```

## Κολλήσατε Κάπου;

Αν έχετε οποιοδήποτε πρόβλημα με αυτή τη ρύθμιση, μπείτε στο <a href="https://discord.gg/kzRShWzttr" target="_blank">Azure AI Community Discord</a> ή <a href="https://github.com/microsoft/ai-agents-for-beginners/issues?WT.mc_id=academic-105485-koreyst" target="_blank">δημιουργήστε ένα issue</a>.

## Επόμενο Μάθημα

Είστε τώρα έτοιμοι να τρέξετε τον κώδικα για αυτό το μάθημα. Καλή εκμάθηση περισσότερων για τον κόσμο των AI Agents! 

[Εισαγωγή στους AI Agents και Περιπτώσεις Χρήσης](../01-intro-to-ai-agents/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Αποποίηση ευθυνών**:
Αυτό το έγγραφο έχει μεταφραστεί χρησιμοποιώντας την υπηρεσία μετάφρασης με τεχνητή νοημοσύνη [Co-op Translator](https://github.com/Azure/co-op-translator). Ενώ επιδιώκουμε την ακρίβεια, παρακαλούμε να έχετε υπόψη ότι οι αυτοματοποιημένες μεταφράσεις ενδέχεται να περιέχουν λάθη ή ανακρίβειες. Το πρωτότυπο έγγραφο στη μητρική του γλώσσα πρέπει να θεωρείται η αυθεντική πηγή. Για κρίσιμες πληροφορίες, συνιστάται επαγγελματική ανθρώπινη μετάφραση. Δεν φέρουμε ευθύνη για τυχόν παρεξηγήσεις ή λανθασμένες ερμηνείες που προκύπτουν από τη χρήση αυτής της μετάφρασης.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->