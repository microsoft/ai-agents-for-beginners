# Ρύθμιση Μαθήματος

## Εισαγωγή

Αυτό το μάθημα θα καλύψει το πώς να εκτελείτε τα παραδείγματα κώδικα αυτού του μαθήματος.

## Συμμετοχή με άλλους μαθητές και λήψη βοήθειας

Πριν ξεκινήσετε την κλωνοποίηση του repo σας, ενώστε το [κανάλι Discord AI Agents For Beginners](https://aka.ms/ai-agents/discord) για να λάβετε οποιαδήποτε βοήθεια με τη ρύθμιση, ερωτήσεις για το μάθημα ή για να συνδεθείτε με άλλους μαθητές.

## Κλωνοποίηση ή Fork αυτού του Repo

Για να ξεκινήσετε, παρακαλούμε κλωνοποιήστε ή κάντε fork το αποθετήριο GitHub. Αυτό θα δημιουργήσει τη δική σας έκδοση του υλικού του μαθήματος ώστε να μπορείτε να εκτελείτε, δοκιμάζετε και τροποποιείτε τον κώδικα!

Αυτό μπορεί να γίνει κάνοντας κλικ στο σύνδεσμο για <a href="https://github.com/microsoft/ai-agents-for-beginners/fork" target="_blank">να κάνετε fork το repo</a>

Τώρα θα πρέπει να έχετε τη δική σας έκδοση του μαθήματος στο ακόλουθο σύνδεσμο:

![Forked Repo](../../../translated_images/el/forked-repo.33f27ca1901baa6a.webp)

### Επιφανειακή Κλωνοποίηση (συνιστάται για εργαστήρια / Codespaces)

  >Το πλήρες αποθετήριο μπορεί να είναι μεγάλο (~3 GB) όταν κάνετε λήψη του πλήρους ιστορικού και όλων των αρχείων. Αν παρακολουθείτε μόνο το εργαστήριο ή χρειάζεστε μόνο μερικούς φακέλους μαθημάτων, μια επιφανειακή κλωνοποίηση (ή σπάνια κλωνοποίηση) αποφεύγει το μεγαλύτερο μέρος αυτής της λήψης περιορίζοντας το ιστορικό και/ή παραλείποντας blobs.

#### Γρήγορη επιφανειακή κλωνοποίηση — ελάχιστο ιστορικό, όλα τα αρχεία

Αντικαταστήστε `<your-username>` στις παρακάτω εντολές με το URL του Fork σας (ή το upstream URL αν προτιμάτε).

Για να κλωνοποιήσετε μόνο το τελευταίο ιστορικό commit (μικρή λήψη):

```bash|powershell
git clone --depth 1 https://github.com/<your-username>/ai-agents-for-beginners.git
```

Για να κλωνοποιήσετε ένα συγκεκριμένο branch:

```bash|powershell
git clone --depth 1 --branch <branch-name> https://github.com/<your-username>/ai-agents-for-beginners.git
```

#### Μερική (σπάνια) κλωνοποίηση — ελάχιστα blobs + μόνο επιλεγμένοι φάκελοι

Αυτό χρησιμοποιεί μερική κλωνοποίηση και sparse-checkout (απαιτεί Git 2.25+ και συνιστάται σύγχρονο Git με υποστήριξη μερικής κλωνοποίησης):

```bash|powershell
git clone --depth 1 --filter=blob:none --sparse https://github.com/<your-username>/ai-agents-for-beginners.git
```

Μεταβείτε στον φάκελο του repo:

```bash|powershell
cd ai-agents-for-beginners
```

Στη συνέχεια επιλέξτε τους φακέλους που θέλετε (το παράδειγμα παρακάτω δείχνει δύο φακέλους):

```bash|powershell
git sparse-checkout set 00-course-setup 01-intro-to-ai-agents
```

Μετά την κλωνοποίηση και τον έλεγχο των αρχείων, αν χρειάζεστε μόνο αρχεία και θέλετε να ελευθερώσετε χώρο (χωρίς ιστορικό git), παρακαλούμε διαγράψτε τα μεταδεδομένα του αποθετηρίου (💀μη αναστρέψιμο — θα χάσετε όλη τη λειτουργικότητα του Git: δεν θα υπάρχουν commits, pulls, pushes ή πρόσβαση στο ιστορικό).

```bash
# zsh/bash
rm -rf .git
```

```powershell
# PowerShell
Remove-Item -Recurse -Force .git
```

#### Χρήση GitHub Codespaces (συνιστάται για αποφυγή μεγάλων τοπικών λήψεων)

- Δημιουργήστε έναν νέο Codespace για αυτό το repo μέσω του [GitHub UI](https://github.com/codespaces).  

- Στο τερματικό του νεοδημιουργημένου Codespace, εκτελέστε μία από τις εντολές επιφανειακής/σπάνιας κλωνοποίησης παραπάνω για να φέρετε μόνο τους φακέλους των μαθημάτων που χρειάζεστε στον χώρο εργασίας του Codespace.
- Προαιρετικό: μετά την κλωνοποίηση μέσα σε Codespaces, αφαιρέστε το .git για να ανακτήσετε χώρο (βλέπε εντολές αφαίρεσης παραπάνω).
- Σημείωση: Αν προτιμάτε να ανοίξετε το repo απευθείας σε Codespaces (χωρίς επιπλέον κλωνοποίηση), λάβετε υπόψη ότι τα Codespaces θα κατασκευάσουν το περιβάλλον devcontainer και μπορεί να παρέχουν περισσότερα από όσα χρειάζεστε. Η κλωνοποίηση μιας επιφανειακής αντιγραφής μέσα σε φρέσκο Codespace σας δίνει περισσότερο έλεγχο στη χρήση δίσκου.

#### Συμβουλές

- Πάντοτε αντικαθιστάτε το URL κλωνοποίησης με το fork σας αν θέλετε να επεξεργαστείτε/κάνετε commit.
- Αν αργότερα χρειαστείτε περισσότερο ιστορικό ή αρχεία, μπορείτε να τα φέρετε ή να προσαρμόσετε το sparse-checkout για να συμπεριλάβετε επιπλέον φακέλους.

## Εκτέλεση Κώδικα

Αυτό το μάθημα προσφέρει μια σειρά από Jupyter Notebooks που μπορείτε να εκτελέσετε για πρακτική εμπειρία στην κατασκευή AI Agents.

Τα παραδείγματα κώδικα χρησιμοποιούν το **Microsoft Agent Framework (MAF)** με το `FoundryChatClient`, που συνδέεται με την **Microsoft Foundry Agent Service V2** (το Responses API) μέσω της **Microsoft Foundry**.

Όλα τα Python notebooks έχουν ετικέτα `*-python-agent-framework.ipynb`.

## Απαιτήσεις

- Python 3.12+
  - **ΣΗΜΕΙΩΣΗ**: Αν δεν έχετε εγκατεστημένο το Python3.12, βεβαιωθείτε ότι το εγκαθιστάτε. Στη συνέχεια, δημιουργήστε το venv σας χρησιμοποιώντας python3.12 για να διασφαλίσετε ότι εγκαθίστανται οι σωστές εκδόσεις από το αρχείο requirements.txt.
  
    >Παράδειγμα

    Δημιουργία καταλόγου Python venv:

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

- .NET 10+: Για τους δείγματος κώδικα που χρησιμοποιούν .NET, βεβαιωθείτε ότι έχετε εγκαταστήσει [.NET 10 SDK](https://dotnet.microsoft.com/download/dotnet/10.0) ή νεότερο. Έπειτα, ελέγξτε την εγκατεστημένη έκδοση .NET SDK:

    ```bash|powershell
    dotnet --list-sdks
    ```

- **Azure CLI** — Απαιτείται για αυθεντικοποίηση. Εγκαταστήστε από [aka.ms/installazurecli](https://aka.ms/installazurecli).
- **Azure Subscription** — Για πρόσβαση σε Microsoft Foundry και Microsoft Foundry Agent Service.
- **Microsoft Foundry Project** — Ένα έργο με αναπτυγμένο μοντέλο (π.χ., `gpt-5-mini`). Δείτε [Βήμα 1](#βήμα-1-δημιουργία-έργου-microsoft-foundry) παρακάτω.

Στο ριζικό κατάλογο αυτού του αποθετηρίου έχουμε συμπεριλάβει το αρχείο `requirements.txt` που περιέχει όλα τα απαιτούμενα πακέτα Python για την εκτέλεση των παραδειγμάτων κώδικα.

Μπορείτε να τα εγκαταστήσετε εκτελώντας την ακόλουθη εντολή στο τερματικό σας στον ριζικό κατάλογο του αποθετηρίου:

```bash|powershell
pip install -r requirements.txt
```

Συνιστούμε να δημιουργήσετε ένα εικονικό περιβάλλον Python για να αποφύγετε συγκρούσεις και προβλήματα.

## Ρύθμιση VSCode

Βεβαιωθείτε ότι χρησιμοποιείτε την σωστή έκδοση Python στο VSCode.

![image](https://github.com/user-attachments/assets/a85e776c-2edb-4331-ae5b-6bfdfb98ee0e)

## Ρύθμιση Microsoft Foundry και Microsoft Foundry Agent Service

### Βήμα 1: Δημιουργία έργου Microsoft Foundry

Χρειάζεστε ένα hub και ένα έργο Microsoft Foundry με αναπτυγμένο μοντέλο για να εκτελέσετε τα notebooks.

1. Μεταβείτε στο [ai.azure.com](https://ai.azure.com) και συνδεθείτε με τον λογαριασμό Azure σας.
2. Δημιουργήστε ένα **hub** (ή χρησιμοποιήστε ένα υπάρχον). Δείτε: [Επισκόπηση πόρων hub](https://learn.microsoft.com/azure/ai-foundry/concepts/ai-resources).
3. Μέσα στο hub, δημιουργήστε ένα **έργο**.
4. Αναπτύξτε ένα μοντέλο (π.χ., `gpt-5-mini`) από **Models + Endpoints** → **Deploy model**.

### Βήμα 2: Λήψη του Endpoint έργου και του ονόματος ανάπτυξης μοντέλου

Από το έργο σας στην πύλη Microsoft Foundry:

- **Project Endpoint** — Μεταβείτε στην σελίδα **Overview** και αντιγράψτε το URL του endpoint.

![Project Connection String](../../../translated_images/el/project-endpoint.8cf04c9975bbfbf1.webp)

- **Model Deployment Name** — Μεταβείτε σε **Models + Endpoints**, επιλέξτε το αναπτυγμένο μοντέλο σας και σημειώστε το **Deployment name** (π.χ., `gpt-5-mini`).

### Βήμα 3: Σύνδεση στο Azure με `az login`

Όλα τα notebooks χρησιμοποιούν το **`AzureCliCredential`** για αυθεντικοποίηση — δεν χρειάζεται να διαχειρίζεστε API κλειδιά. Απαιτεί να είστε συνδεδεμένοι μέσω του Azure CLI.

1. **Εγκαταστήστε το Azure CLI** αν δεν το έχετε ήδη: [aka.ms/installazurecli](https://aka.ms/installazurecli)

2. **Συνδεθείτε** εκτελώντας:

    ```bash|powershell
    az login
    ```

    Ή αν βρίσκεστε σε απομακρυσμένο περιβάλλον/Codespace χωρίς πρόγραμμα περιήγησης:

    ```bash|powershell
    az login --use-device-code
    ```

3. **Επιλέξτε τη συνδρομή σας** αν σας ζητηθεί — επιλέξτε αυτή που περιέχει το έργο Foundry σας.

4. **Επιβεβαιώστε** ότι είστε συνδεδεμένοι:

    ```bash|powershell
    az account show
    ```

> **Γιατί `az login`?** Τα notebooks αυθεντικοποιούνται χρησιμοποιώντας το `AzureCliCredential` από το πακέτο `azure-identity`. Αυτό σημαίνει ότι η συνεδρία Azure CLI σας παρέχει τα διαπιστευτήρια — δεν χρειάζονται API κλειδιά ή μυστικά στο `.env` αρχείο σας. Αυτή είναι μια [βέλτιστη πρακτική ασφάλειας](https://learn.microsoft.com/azure/developer/ai/keyless-connections).

### Βήμα 4: Δημιουργία του αρχείου `.env`

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

| Μεταβλητή | Πού να τη βρείτε |
|----------|-----------------|
| `AZURE_AI_PROJECT_ENDPOINT` | Πύλη Foundry → το έργο σας → σελίδα **Overview** |
| `AZURE_AI_MODEL_DEPLOYMENT_NAME` | Πύλη Foundry → **Models + Endpoints** → όνομα αναπτυγμένου μοντέλου |

Αυτά είναι για τα περισσότερα μαθήματα! Τα notebooks θα αυθεντικοποιηθούν αυτόματα μέσω της συνεδρίας `az login`.

### Βήμα 5: Εγκατάσταση εξαρτήσεων Python

```bash|powershell
pip install -r requirements.txt
```

Συνιστούμε να εκτελέσετε αυτό μέσα στο εικονικό περιβάλλον που δημιουργήσατε νωρίτερα.

## Επιπλέον ρύθμιση για το Μάθημα 5 (Agentic RAG)

Το μάθημα 5 χρησιμοποιεί το **Azure AI Search** για ανάκτηση-βελτιωμένη δημιουργία. Αν σκοπεύετε να εκτελέσετε αυτό το μάθημα, προσθέστε αυτές τις μεταβλητές στο αρχείο `.env`:

| Μεταβλητή | Πού να τη βρείτε |
|----------|-----------------|
| `AZURE_SEARCH_SERVICE_ENDPOINT` | Πύλη Azure → το πόρο **Azure AI Search** → **Overview** → URL |
| `AZURE_SEARCH_API_KEY` | Πύλη Azure → το πόρο **Azure AI Search** → **Settings** → **Keys** → κύριο διαχειριστικό κλειδί |

## Επιπλέον ρύθμιση για μαθήματα που καλούν απευθείας Azure OpenAI (Μαθήματα 6 και 8)

Μερικά notebooks στα μαθήματα 6 και 8 καλούν απευθείας το **Azure OpenAI** (χρησιμοποιώντας το **Responses API**) αντί να περάσουν από ένα έργο Microsoft Foundry. Αυτά τα δείγματα πριν χρησιμοποιούσαν GitHub Models, που έχει καταργηθεί (λήξη Ιούλιος 2026) και δεν υποστηρίζει το Responses API. Αν σκοπεύετε να εκτελέσετε αυτά τα δείγματα, προσθέστε αυτές τις μεταβλητές στο αρχείο `.env`:

| Μεταβλητή | Πού να τη βρείτε |
|----------|-----------------|
| `AZURE_OPENAI_ENDPOINT` | Πύλη Azure → το πόρο **Azure OpenAI** → **Keys and Endpoint** → Endpoint (π.χ. `https://<your-resource>.openai.azure.com`) |
| `AZURE_OPENAI_DEPLOYMENT` | Το όνομα του αναπτυγμένου μοντέλου σας (π.χ. `gpt-5-mini`) που υποστηρίζει το Responses API |
| `AZURE_OPENAI_API_KEY` | Προαιρετικό — μόνο αν χρησιμοποιείτε αυθεντικοποίηση με κλειδί αντί για `az login` / Entra ID |

> Το Responses API χρησιμοποιεί το σταθερό endpoint `/openai/v1/`, οπότε δεν απαιτείται `api-version`. Συνδεθείτε με `az login` για να χρησιμοποιήσετε αυθεντικοποίηση χωρίς κλειδί Entra ID.

## Εναλλακτικός Πάροχος: MiniMax (Συμβατό με OpenAI)

Το [MiniMax](https://platform.minimaxi.com/) παρέχει μοντέλα μεγάλης μνήμης (έως 204K tokens) μέσω ενός API συμβατού με OpenAI. Επειδή ο `OpenAIChatClient` του Microsoft Agent Framework λειτουργεί με οποιοδήποτε endpoint συμβατό με OpenAI, μπορείτε να χρησιμοποιήσετε το MiniMax ως άμεση εναλλακτική της Azure OpenAI ή του OpenAI.

Προσθέστε αυτές τις μεταβλητές στο αρχείο `.env` σας:

| Μεταβλητή | Πού να τη βρείτε |
|----------|-----------------|
| `MINIMAX_API_KEY` | [MiniMax Platform](https://platform.minimaxi.com/) → API Keys |
| `MINIMAX_BASE_URL` | Χρησιμοποιήστε `https://api.minimax.io/v1` (προεπιλεγμένη τιμή) |
| `MINIMAX_MODEL_ID` | Όνομα μοντέλου για χρήση (π.χ., `MiniMax-M3`) |

**Παραδείγματα μοντέλων**: `MiniMax-M3` (συνιστώμενο), `MiniMax-M2.7`, `MiniMax-M2.7-highspeed` (ταχύτερες απαντήσεις). Τα ονόματα και η διαθεσιμότητα των μοντέλων μπορεί να αλλάξουν με την πάροδο του χρόνου, και η πρόσβαση σε συγκεκριμένο μοντέλο μπορεί να εξαρτάται από τον λογαριασμό ή την περιοχή σας — ελέγξτε το [MiniMax Platform](https://platform.minimaxi.com/) για την τρέχουσα λίστα. Αν το `MiniMax-M3` δεν είναι διαθέσιμο για τον λογαριασμό σας, ορίστε το `MINIMAX_MODEL_ID` σε ένα μοντέλο που έχετε πρόσβαση (π.χ. `MiniMax-M2.7`).

Τα παραδείγματα κώδικα που χρησιμοποιούν `OpenAIChatClient` (π.χ., ροή εργασίας κράτησης ξενοδοχείου στο Μάθημα 14) θα εντοπίζουν και θα χρησιμοποιούν αυτόματα τη ρύθμιση MiniMax όταν το `MINIMAX_API_KEY` έχει οριστεί.

## Εναλλακτικός Πάροχος: Foundry Local (Εκτέλεση Μοντέλων στην Τοπική Συσκευή)

Το [Foundry Local](https://foundrylocal.ai) είναι ένα ελαφρύ runtime που κατεβάζει, διαχειρίζεται και εξυπηρετεί μοντέλα γλώσσας **εντελώς στη δική σας συσκευή** μέσω ενός API συμβατού με OpenAI — χωρίς σύννεφο, χωρίς συνδρομή Azure και χωρίς κλειδιά API. Είναι μια εξαιρετική επιλογή για ανάπτυξη εκτός σύνδεσης, πειραματισμό χωρίς κόστος cloud ή διατήρηση δεδομένων στη συσκευή.

Επειδή ο `OpenAIChatClient` του Microsoft Agent Framework λειτουργεί με οποιοδήποτε endpoint συμβατό με OpenAI, το Foundry Local είναι άμεση τοπική εναλλακτική του Azure OpenAI.

**1. Εγκαταστήστε το Foundry Local**

```bash
# Windows
winget install Microsoft.FoundryLocal

# macOS
brew install foundrylocal
```

**2. Κατεβάστε και εκτελέστε ένα μοντέλο** (αυτό ξεκινά επίσης την τοπική υπηρεσία):

```bash
foundry model list          # δείτε διαθέσιμα μοντέλα
foundry model run phi-4-mini
```

**3. Εγκαταστήστε το Python SDK** που χρησιμοποιείται για την εύρεση του τοπικού endpoint:

```bash
pip install foundry-local-sdk
```

**4. Δείξτε το Microsoft Agent Framework στο τοπικό μοντέλο σας:**

```python
from foundry_local import FoundryLocalManager
from agent_framework.openai import OpenAIChatClient

# Κατεβάζει (αν χρειάζεται) και εξυπηρετεί το μοντέλο τοπικά, στη συνέχεια ανακαλύπτει το endpoint/θύρα.
manager = FoundryLocalManager("phi-4-mini")

chat_client = OpenAIChatClient(
    base_url=manager.endpoint,      # π.χ. http://localhost:<port>/v1
    api_key=manager.api_key,        # πάντα "όχι-απαραίτητο" για το Foundry Local
    model_id=manager.get_model_info("phi-4-mini").id,
)

agent = chat_client.as_agent(
    name="LocalAgent",
    instructions="You are a helpful assistant running fully on-device.",
)
```

> **Σημείωση:** Το Foundry Local παρέχει ένα endpoint συμβατό με OpenAI **Chat Completions**. Χρησιμοποιήστε το για τοπική ανάπτυξη και σενάρια εκτός σύνδεσης. Για το πλήρες σύνολο λειτουργιών **Responses API** (καταστάσεις συνομιλιών, βαθιά ορχήστρα εργαλείων και ανάπτυξη τύπου agent), στρέψτε το σε **Azure OpenAI** ή ένα έργο **Microsoft Foundry**, όπως φαίνεται στα μαθήματα. Δείτε την [τεκμηρίωση Foundry Local](https://foundrylocal.ai) για τον τρέχοντα κατάλογο μοντέλων και την υποστήριξη πλατφόρμας.

## Επιπλέον ρύθμιση για το Μάθημα 8 (Ροή εργασίας Bing Grounding)


Το σημειωματάριο ροής εργασίας με συνθήκη στο μάθημα 8 χρησιμοποιεί **Bing grounding** μέσω Microsoft Foundry. Εάν σκοπεύετε να εκτελέσετε αυτό το δείγμα, προσθέστε αυτή τη μεταβλητή στο αρχείο `.env` σας:

| Μεταβλητή | Πού θα τη βρείτε |
|----------|-----------------|
| `BING_CONNECTION_ID` | Πύλη Microsoft Foundry → το έργο σας → **Management** → **Connected resources** → η σύνδεση Bing σας → αντιγράψτε το αναγνωριστικό σύνδεσης |

## Επίλυση Προβλημάτων

### Σφάλματα Επαλήθευσης Πιστοποιητικού SSL σε macOS

Εάν χρησιμοποιείτε macOS και αντιμετωπίζετε ένα σφάλμα όπως:

```plaintext
ssl.SSLCertVerificationError: [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: self-signed certificate in certificate chain
```

Αυτό είναι ένα γνωστό ζήτημα με την Python σε macOS όπου τα συστήματα SSL πιστοποιητικά δεν εμπιστεύονται αυτόματα. Δοκιμάστε τις ακόλουθες λύσεις με τη σειρά:

**Επιλογή 1: Εκτέλεση του σεναρίου Install Certificates της Python (συνιστάται)**

```bash
# Αντικαταστήστε το 3.XX με την εγκατεστημένη έκδοση Python σας (π.χ., 3.12 ή 3.13):
/Applications/Python\ 3.XX/Install\ Certificates.command
```

**Επιλογή 2: Χρήση `connection_verify=False` στο σημειωματάριό σας (μόνο για τα σημειωματάρια GitHub Models)**

Στο σημειωματάριο του Μαθήματος 6 (`06-building-trustworthy-agents/code_samples/06-system-message-framework.ipynb`), υπάρχει ήδη μια σχολιασμένη λύση. Αποσχολιάστε το `connection_verify=False` κατά τη δημιουργία του πελάτη:

```python
client = ChatCompletionsClient(
    endpoint=endpoint,
    credential=AzureKeyCredential(token),
    connection_verify=False,  # Απενεργοποιήστε την επαλήθευση SSL αν συναντήσετε σφάλματα πιστοποιητικού
)
```

> **⚠️ Προειδοποίηση:** Η απενεργοποίηση της επαλήθευσης SSL (`connection_verify=False`) μειώνει την ασφάλεια παρακάμπτοντας την επικύρωση πιστοποιητικού. Χρησιμοποιήστε το μόνο ως προσωρινή λύση σε περιβάλλοντα ανάπτυξης, ποτέ σε παραγωγή.

**Επιλογή 3: Εγκατάσταση και χρήση `truststore`**

```bash
pip install truststore
```

Στη συνέχεια προσθέστε τα ακόλουθα στην κορυφή του σημειωματαρίου ή του σεναρίου σας πριν κάνετε οποιαδήποτε κλήση δικτύου:

```python
import truststore
truststore.inject_into_ssl()
```

## Κόλλησες Κάπου;

Εάν αντιμετωπίσετε προβλήματα με αυτή τη ρύθμιση, μπείτε στο <a href="https://discord.gg/kzRShWzttr" target="_blank">Discord της Κοινότητας Azure AI</a> ή <a href="https://github.com/microsoft/ai-agents-for-beginners/issues?WT.mc_id=academic-105485-koreyst" target="_blank">δημιουργήστε ένα ζήτημα</a>.

## Επόμενο Μάθημα

Είστε πλέον έτοιμοι να εκτελέσετε τον κώδικα για αυτό το μάθημα. Καλή μάθηση στον κόσμο των AI Agents!

[Εισαγωγή στους AI Agents και Χρήσεις τους](../01-intro-to-ai-agents/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Αποποίηση ευθυνών**:
Αυτό το έγγραφο έχει μεταφραστεί χρησιμοποιώντας την υπηρεσία μετάφρασης με τεχνητή νοημοσύνη [Co-op Translator](https://github.com/Azure/co-op-translator). Ενώ επιδιώκουμε την ακρίβεια, παρακαλούμε να έχετε υπόψη ότι οι αυτοματοποιημένες μεταφράσεις ενδέχεται να περιέχουν λάθη ή ανακρίβειες. Το πρωτότυπο έγγραφο στη μητρική του γλώσσα πρέπει να θεωρείται η αυθεντική πηγή. Για κρίσιμες πληροφορίες, συνιστάται επαγγελματική ανθρώπινη μετάφραση. Δεν φέρουμε ευθύνη για τυχόν παρεξηγήσεις ή λανθασμένες ερμηνείες που προκύπτουν από τη χρήση αυτής της μετάφρασης.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->