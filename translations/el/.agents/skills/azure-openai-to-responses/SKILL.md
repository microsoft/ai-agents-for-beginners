---
name: azure-openai-to-responses
license: MIT
---
# Μεταφορά εφαρμογών Python από Azure OpenAI Chat Completions στο Responses API

> **ΕΞΟΥΣΙΟΔΟΤΗΜΕΝΕΣ ΟΔΗΓΙΕΣ — ΑΚΡΙΒΗΣ ΑΚΟΛΟΥΘΗΣΗ**
>
> Αυτή η δεξιότητα μεταφέρει βάσεις κώδικα Python που χρησιμοποιούν Azure OpenAI Chat Completions
> στο ενιαίο Responses API. Ακολουθήστε αυτές τις οδηγίες με ακρίβεια.
> Μην αυτοσχεδιάζετε τους χάρτες παραμέτρων ή δημιουργείτε σχήματα API.

---

## Εκκινήσεις

Ενεργοποιήστε αυτή τη δεξιότητα όταν ο χρήστης θέλει να:
- Μεταφέρει μια εφαρμογή Python από Azure OpenAI Chat Completions στο Responses API
- Αναβαθμίσει τη χρήση του Python OpenAI SDK στην πιο πρόσφατη μορφή API ενάντια στο Azure OpenAI
- Προετοιμάσει κώδικα Python για μοντέλα GPT-5 ή νεότερα που απαιτούν Responses στο Azure
- Μεταπηδήσει από `AzureOpenAI`/`AsyncAzureOpenAI` σε τυπικό `OpenAI`/`AsyncOpenAI` client με το endpoint v1
- Διορθώσει προειδοποιήσεις παρωχημένης χρήσης που σχετίζονται με constructors `AzureOpenAI` ή `api_version`

---

## ⚠️ Συμβατότητα μοντέλου — ΕΛΕΓΞΤΕ ΠΡΩΤΑ

> **Πριν από τη μετανάστευση, βεβαιωθείτε ότι η ανάπτυξη Azure OpenAI υποστηρίζει το Responses API.**

### 1. Έλεγχος καπνού στην ανάπτυξη (ταχύτερος)

```python
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ["AZURE_OPENAI_API_KEY"],
    base_url=f"{os.environ['AZURE_OPENAI_ENDPOINT'].rstrip('/')}/openai/v1/",
)

try:
    resp = client.responses.create(
        model=os.environ["AZURE_OPENAI_DEPLOYMENT"],
        input="ping",
        max_output_tokens=50,
        store=False,
    )
    print(f"✅ Deployment supports Responses API: {resp.output_text}")
except Exception as e:
    print(f"❌ Deployment does NOT support Responses API: {e}")
```

> **Σημείωση**: `max_output_tokens` έχει **ελάχιστο 16** στο Azure OpenAI. Τιμές κάτω του 16 επιστρέφουν σφάλμα 400. Χρησιμοποιήστε 50+ για ελέγχους καπνού.

Αν επιστρέψει 404, το μοντέλο της ανάπτυξης δεν υποστηρίζει Responses ακόμα — ελέγξτε την αναφορά παρακάτω ή αναπτύξτε ξανά με υποστηριζόμενο μοντέλο.

### 2. Ελέγξτε διαθέσιμα μοντέλα στην περιοχή σας (συνιστάται)

Τρέξτε το ενσωματωμένο εργαλείο συμβατότητας μοντέλων για να δείτε τι είναι διαθέσιμο με υποστήριξη Responses API στην συγκεκριμένη περιοχή σας:

```bash
python migrate.py models --subscription YOUR_SUB_ID --location YOUR_REGION
```

Αυτό ρωτάει ζωντανά το Azure ARM και δείχνει έναν πίνακα συμβατότητας — ποια μοντέλα υποστηρίζουν Responses, δομημένη έξοδο, εργαλεία κλπ. Χρησιμοποιήστε `--filter gpt-5.1,gpt-5.2` για περιορισμό αποτελεσμάτων ή `--json` για scripting.

### 3. Πλήρης αναφορά υποστήριξης μοντέλων

- **Ζωντανή ερώτηση**: `python migrate.py models` (δείτε παραπάνω — ειδικά ανά περιοχή, πάντα ενημερωμένο)
- **Περιήγηση διαθεσιμότητας**: [Πίνακας περιλήψεων μοντέλων και διαθεσιμότητα περιοχών](https://learn.microsoft.com/en-us/azure/foundry/foundry-models/concepts/models-sold-directly-by-azure?tabs=global-standard-aoai%2Cglobal-standard&pivots=azure-openai#model-summary-table-and-region-availability)
- **Γρήγορη εκκίνηση & οδηγίες**: **https://aka.ms/openai/start**

### ⚠️ Περιορισμοί παλαιότερων μοντέλων

> **ΠΡΟΕΙΔΟΠΟΙΗΣΗ**: Παλαιότερα μοντέλα (π.χ. `gpt-4o`, `gpt-4`) μπορεί να μην υποστηρίζουν πλήρως όλες τις δυνατότητες του Responses API.
>
> Γνωστοί περιορισμοί με παλαιότερα μοντέλα:
> - **Παράμετρος `reasoning`**: Δεν υποστηρίζεται στα `gpt-4o-mini`, `gpt-4o`, και πολλά μοντέλα χωρίς reasoning. Μεταφέρετε το `reasoning` μόνο αν ήδη υπήρχε στον αρχικό κώδικα.
> - **Παράμετρος `seed`**: Δεν υποστηρίζεται καθόλου στο Responses API — αφαιρέστε από όλα τα αιτήματα.
> - **Δομημένη έξοδος μέσω `text.format`**: Τα παλαιότερα μοντέλα μπορεί να μη διαχειρίζονται αξιόπιστα σχήματα JSON με `strict: true`.
> - **Ορχήστρωση εργαλείων**: Το GPT-5+ οργανώνει κλήσεις εργαλείων ως μέρος του εσωτερικού reasoning. Τα παλαιότερα μοντέλα στο Responses λειτουργούν, αλλά χωρίς αυτή την εμβάθυνση.
> - **Περιορισμοί θερμοκρασίας**: Κατά τη μετανάστευση σε `gpt-5`, το temperature πρέπει να παραλείπεται ή να ορίζεται σε `1`. Τα παλαιότερα μοντέλα δεν έχουν αυτούς τους περιορισμούς.

### Μοντέλα σειράς O (o1, o3-mini, o3, o4-mini)

Τα μοντέλα σειράς O έχουν μοναδικούς περιορισμούς παραμέτρων. Κατά τη μετανάστευση εφαρμογών που στοχεύουν σε μοντέλα σειράς o:

- **`temperature`**: Πρέπει να είναι `1` (ή παραληφθεί). Τα μοντέλα σειράς O δεν δέχονται άλλες τιμές.
- **`max_completion_tokens` → `max_output_tokens`**: Εφαρμογές που χρησιμοποιούν το Azure-ειδικό `max_completion_tokens` πρέπει να αλλάξουν σε `max_output_tokens`. Ορίστε υψηλές τιμές (4096+) επειδή τα tokens reasoning μετρούν στο όριο.
- **`reasoning_effort`**: Αν η εφαρμογή χρησιμοποιεί `reasoning_effort` (χαμηλό/μεσαίο/υψηλό), κρατήστε το — το Responses API το υποστηρίζει για μοντέλα σειράς o.
- **Συμπεριφορά streaming**: Τα μοντέλα σειράς O μπορεί να αποθηκεύουν προσωρινά την έξοδο μέχρι να ολοκληρωθεί το reasoning πριν εκπέμψουν events με κείμενο. Το streaming δουλεύει, αλλά το πρώτο `response.output_text.delta` μπορεί να έρθει με μεγαλύτερη καθυστέρηση απ’ ό,τι με GPT.
- **`top_p`**: Δεν υποστηρίζεται στη σειρά o — αφαιρέστε αν υπάρχει.
- **Χρήση εργαλείων**: Τα μοντέλα σειράς O υποστηρίζουν εργαλεία μέσω Responses API όπως τα μοντέλα GPT, αλλά η ποιότητα ορχήστρωσης κλήσεων εργαλείων ποικίλλει.

**Ενέργεια — προληπτική συμβουλή μοντέλου**: Κατά τη φάση σάρωσης, ελέγξτε σε ποιο μοντέλο στοχεύει η εφαρμογή (ονόματα ανάπτυξης, μεταβλητές περιβάλλοντος, ρυθμίσεις). Αν το μοντέλο είναι `gpt-4o` ή παλαιότερο (όχι gpt-4.1+), ενημερώστε προληπτικά τον χρήστη:
- Η μετανάστευση θα δουλέψει για βασικό κείμενο, chat, streaming και εργαλεία στο τρέχον μοντέλο.
- Τα νεότερα μοντέλα (`gpt-5.1`, `gpt-5.2`) προσφέρουν καλύτερη ορχήστρωση εργαλείων, επιβολή δομημένης εξόδου, reasoning, και διαθεσιμότητα σε πολλαπλές περιοχές.
- Προτείνετε να αναβαθμίσουν την ανάπτυξή τους όταν είναι έτοιμοι — δεν μπλοκάρει την μετανάστευση.

Μην μπλοκάρετε ή αρνείστε μετανάστευση βάσει έκδοσης μοντέλου. Η συμβουλή είναι πληροφοριακή.

### Τα GitHub Models ΔΕΝ υποστηρίζουν το Responses API

> **Τα GitHub Models (`models.github.ai`, `models.inference.ai.azure.com`) δεν υποστηρίζουν το Responses API.**

Αν η βάση κώδικα έχει μονοπάτι κώδικα GitHub Models (ψάξτε για `base_url` που δείχνει σε `models.github.ai` ή `models.inference.ai.azure.com`), **αφαιρέστε το εντελώς** κατά τη μετανάστευση. Το Responses API απαιτεί Azure OpenAI, OpenAI, ή συμβατό τοπικό endpoint (π.χ. Ollama με υποστήριξη Responses).

Ενέργεια κατά τη σάρωση:
- Σημειώστε όλα τα μονοπάτια κώδικα GitHub Models για αφαίρεση.

---

## Μετανάστευση πλαισίου εργασίας

Πολλές εφαρμογές χρησιμοποιούν πλαίσια υψηλού επιπέδου πάνω από το OpenAI. Κατά τη μετανάστευση αυτών, αλλάζει το ίδιο το API του πλαισίου — όχι μόνο οι υποκείμενες κλήσεις OpenAI.

### Microsoft Agent Framework (MAF)

**Ελέγξτε πρώτα την έκδοση MAF σας** — η μετανάστευση εξαρτάται αν είστε σε MAF 1.0.0+ ή βήτα/rc προ 1.0.0.

#### MAF 1.0.0+ (agent-framework-openai >= 1.0.0)

`OpenAIChatClient` **χρησιμοποιεί ήδη το Responses API** — δεν χρειάζεται μετανάστευση. Αν η βάση έχει το παλιό `OpenAIChatCompletionClient` (που χρησιμοποιεί `chat.completions.create`), αντικαταστήστε το με `OpenAIChatClient`.

| Πριν | Μετά |
|--------|-------|
| `from agent_framework.openai import OpenAIChatCompletionClient` | `from agent_framework.openai import OpenAIChatClient` |
| `OpenAIChatCompletionClient(...)` | `OpenAIChatClient(...)` |

Για έλεγχο έκδοσης: `python -c "import agent_framework_openai; print(agent_framework_openai.__version__)"`

#### MAF προ 1.0.0 (beta/rc εκδόσεις)

Σε προ 1.0.0 MAF, `OpenAIChatClient` χρησιμοποιούσε Chat Completions. Αναβαθμίστε σε `agent-framework-openai>=1.0.0` όπου `OpenAIChatClient` χρησιμοποιεί Responses API ως προεπιλογή.

Δεν χρειάζονται άλλες αλλαγές — τα Agent και εργαλεία API παραμένουν ίδια.

### LangChain (`langchain-openai`)

Προσθέστε `use_responses_api=True` στο `ChatOpenAI()`. Επίσης, ενημερώστε την πρόσβαση στην απόκριση από `.content` σε `.text`.

| Πριν | Μετά |
|--------|-------|
| `ChatOpenAI(model=..., base_url=..., api_key=...)` | `ChatOpenAI(model=..., base_url=..., api_key=..., use_responses_api=True)` |
| `result['messages'][-1].content` | `result['messages'][-1].text` |

Για ολοκληρωμένα παραδείγματα πριν/μετά, δείτε [cheat-sheet.md](./references/cheat-sheet.md).

---

## Οδηγίες Μεταφοράς Frontend

> **Το Responses API είναι θέμα server-side.** Μεταφέρετε το backend Python σας· το HTTP συμβόλαιο του frontend πρέπει να παραμείνει ίδιο, εκτός αν το backend είναι ένα λεπτό πάσο — σε αυτή την περίπτωση, σκεφτείτε να υιοθετήσετε το σχήμα αιτήματος Responses για να αφαιρέσετε το επίπεδο μετάφρασης. Αν το frontend καλεί απευθείας OpenAI με κλειδί client-side, μετακινήστε αυτές τις κλήσεις σε backend πρώτα.

### Αποδρομή `@microsoft/ai-chat-protocol`

Το πακέτο npm `@microsoft/ai-chat-protocol` είναι αποσυρμένο και πρέπει να αντικατασταθεί με το [`ndjson-readablestream`](https://www.npmjs.com/package/ndjson-readablestream). Αν το βρείτε σε frontend:

1. Αντικαταστήστε το CDN script tag:
   ```html
   <!-- Before -->
   <script src="https://cdn.jsdelivr.net/npm/@microsoft/ai-chat-protocol@.../dist/iife/index.js"></script>
   <!-- After -->
   <script src="https://cdn.jsdelivr.net/npm/ndjson-readablestream@1.0.7/dist/ndjson-readablestream.umd.js"></script>
   ```
2. Αφαιρέστε την δημιουργία `AIChatProtocolClient` (`new ChatProtocol.AIChatProtocolClient("/chat")`).
3. Αντικαταστήστε το `client.getStreamedCompletion(messages)` με άμεσο `fetch()` στο backend streaming endpoint.
4. Αντικαταστήστε το `for await (const response of result)` με `for await (const chunk of readNDJSONStream(response.body))`.
5. Ενημερώστε την πρόσβαση ιδιοτήτων από `response.delta.content` / `response.error` σε `chunk.delta.content` / `chunk.error`.

---

## Στόχοι

- Καταγράψτε όλα τα σημεία κλήσης Python που χρησιμοποιούν Chat Completions ή παρωχημένα Completions στο Azure OpenAI.
- Προτείνετε σχέδιο μετανάστευσης και σειριοθέτηση για τη βάση κώδικα Python.
- Εφαρμόστε ασφαλείς, ελάχιστες αλλαγές για την εναλλαγή σε Responses API.
- Ενημερώστε τους καλούντες να καταναλώνουν το σχήμα εξόδου Responses· χωρίς wrappers για οπισθοσκεή συμβατότητα.
- Τρέξτε tests/lints· διορθώστε απλές βλάβες που εισήγαγε η μετανάστευση.
- Προετοιμάστε μικρά, ανασκοπήσιμα σύνολα αλλαγών και παρέχετε τελικό περίληψη με διαφορές (μη δεσμευτείτε).

---

## Φυλακτήρες

- Τροποποιήστε μόνο αρχεία εντός του git workspace. Ποτέ εκτός.
- Μην διατηρείτε shims για οπισθοσκεή συμβατότητα· μεταφέρετε τον κώδικα στη νέα μορφή API.
- Μην αφήνετε σχόλια μετάβασης ή αρχεία backup.
- Διατηρήστε τη σημασιολογία streaming αν ήταν ήδη χρησιμοποιούμενη· διαφορετικά χρησιμοποιήστε μη streaming.
- Ζητήστε έγκριση πριν εκτελέσετε εντολές ή κλήσεις δικτύου αν είστε σε modus έγκρισης.
- Μην τρέχετε `git add`/`git commit`/`git push`; παράγετε μόνο αλλαγές στο working tree.

---

## Βήμα 0: Μεταφορά Azure OpenAI Client (Προαπαιτούμενο)

Αν η βάση κώδικα χρησιμοποιεί constructors `AzureOpenAI` ή `AsyncAzureOpenAI`, μεταβείτε πρώτα στους τυπικούς constructors `OpenAI` / `AsyncOpenAI`. Οι Azure-ειδικοί constructors είναι παρωχημένοι στο `openai>=1.108.1`.

### Γιατί η διαδρομή API v1;

Το νέο endpoint `/openai/v1` χρησιμοποιεί τον τυπικό client `OpenAI()`, αντί του `AzureOpenAI()`, δεν απαιτεί παράμετρο `api_version` και δουλεύει το ίδιο τόσο στο OpenAI όσο και στο Azure OpenAI. Ο ίδιος κώδικας client είναι μελλοντικά ασφαλής — δεν απαιτείται διαχείριση εκδόσεων.

### Κύριες αλλαγές

| Πριν | Μετά |
|--------|-------|
| `AzureOpenAI` | `OpenAI` |
| `AsyncAzureOpenAI` | `AsyncOpenAI` |
| `azure_endpoint` | `base_url` |
| `azure_ad_token_provider` | `api_key` |
| `api_version=...` | Αφαιρέστε εντελώς |

### Λίστα καθαρισμού

- Αφαιρέστε το όρισμα `api_version` από τη δημιουργία client.
- Αφαιρέστε τις μεταβλητές περιβάλλοντος `AZURE_OPENAI_VERSION` / `AZURE_OPENAI_API_VERSION` από `.env`, ρυθμίσεις εφαρμογής και αρχεία Bicep/infra.
- Μετονομάστε `AZURE_OPENAI_CLIENT_ID` → `AZURE_CLIENT_ID` σε `.env`, ρυθμίσεις εφαρμογής, Bicep/infra, και test fixtures (τυπική σύμβαση Azure Identity SDK).
- Βεβαιωθείτε ότι υπάρχει `openai>=1.108.1` σε `requirements.txt` ή `pyproject.toml`.

### Μεταφορά μεταβλητών περιβάλλοντος

| Παλιά μεταβλητή περιβάλλοντος | Ενέργεια | Σημειώσεις |
|-------------|--------|-------|
| `AZURE_OPENAI_VERSION` | **Αφαιρέστε** | Δεν απαιτείται `api_version` με το endpoint v1 |
| `AZURE_OPENAI_API_VERSION` | **Αφαιρέστε** | Όπως παραπάνω |
| `AZURE_OPENAI_CLIENT_ID` | **Μετονομάστε** → `AZURE_CLIENT_ID` | Τυπική σύμβαση Azure Identity SDK για `ManagedIdentityCredential(client_id=...)` |
| `AZURE_OPENAI_ENDPOINT` | **Διατηρήστε** | Ακόμη χρειάζεται για κατασκευή `base_url` |
| `AZURE_OPENAI_CHAT_DEPLOYMENT` | **Διατηρήστε** | Χρησιμοποιείται ως παράμετρος `model` στην `responses.create` |
| `AZURE_OPENAI_API_KEY` | **Διατηρήστε** | Χρησιμοποιείται ως `api_key` για authentication με κλειδί |

Για παραδείγματα κώδικα ρύθμισης πελάτη (sync, async, EntraID, API key, multi-tenant), δείτε [cheat-sheet.md](./references/cheat-sheet.md).

---

## Βήμα 1: Εντοπισμός παρωχημένων σημείων κλήσης

Τρέξτε το script [detect_legacy.py](../../../../../.agents/skills/azure-openai-to-responses/scripts/detect_legacy.py) για να βρείτε όλα τα σημεία κλήσης που χρειάζονται μετανάστευση:

```bash
python skills/azure-openai-to-responses/scripts/detect_legacy.py .
```

Ή εκτελέστε αυτές τις αναζητήσεις χειροκίνητα — κάθε αποτέλεσμα είναι στόχος μετανάστευσης:

```bash
# Κλήσεις παλιάς API (πρέπει να ξαναγραφούν)
rg "chat\.completions\.create"
rg "ChatCompletion\.create"
rg "Completion\.create"

# Αποσυρθέντες κατασκευαστές πελατών Azure (πρέπει να αντικατασταθούν)
rg "AzureOpenAI\("
rg "AsyncAzureOpenAI\("

# Πρότυπα πρόσβασης σε μορφή απάντησης (πρέπει να ενημερωθούν)
rg "choices\[0\]\.message\.content"
rg "choices\[0\]\.delta\.content"
rg "choices\[0\]\.message\.function_call"
rg "choices\[0\]\.message\.tool_calls"

# Ορισμοί εργαλείων σε παλιό εμφωλευμένο φορμάτ (πρέπει να ισοπεδωθούν)
rg '"function":\s*{\s*"name"'
rg "pydantic_function_tool"

# Αποτελέσματα εργαλείων σε παλιό φορμάτ (πρέπει να μετατραπούν σε function_call_output)
rg '"role":\s*"tool"'
rg '"tool_call_id"'

# Αποσυρθέντες παράμετροι (πρέπει να αφαιρεθούν ή να μετονομαστούν)
rg "response_format"
rg "max_tokens\b"        # μετονομασία σε max_output_tokens
rg "['\"]seed['\"]"      # remove entirely

# Αποσυρθέντες περιβαλλοντικές μεταβλητές (καθαρισμός)
rg "AZURE_OPENAI_API_VERSION|AZURE_OPENAI_VERSION"
rg "AZURE_OPENAI_CLIENT_ID"  # πρέπει να είναι AZURE_CLIENT_ID

# Τερματικά GitHub Models (πρέπει να αφαιρεθούν — η API Responses δεν υποστηρίζεται)
rg "models\.github\.ai|models\.inference\.ai\.azure"

# Πρότυπα παλαιάς βάσης πλαισίου (πρέπει να ενημερωθούν)
rg "OpenAIChatCompletionClient"  # MAF 1.0.0+: αντικαταστήστε με OpenAIChatClient
rg "ChatOpenAI\(" | grep -v "use_responses_api"  # LangChain: χρειάζεται use_responses_api=True

# Υποδομή δοκιμών (πρέπει να ενημερωθεί)
rg "ChatCompletionChunk|AsyncCompletions\.create" tests/
rg "_azure_ad_token_provider" tests/
rg "prompt_filter_results|content_filter_results" tests/
rg "choices\[0\]" tests/

# Πρόσβαση σε σώμα λάθους φίλτρου περιεχομένου (πρέπει να ενημερωθεί — η δομή άλλαξε)
rg 'innererror.*content_filter_result|error\.body\["innererror"\]'
rg "content_filter_result\[" # παλιά ενικότητα — τώρα content_filter_results (πληθυντικός) μέσα σε πίνακα content_filters

# Ακατέργαστες κλήσεις HTTP στο τερματικό Chat Completions (πρέπει να ενημερωθεί το URL)
rg "/openai/deployments/.*/chat/completions"
rg "api-version="
```

### Ευρετικές (εντοπισμός και επανεγγραφή)

- **Chat Completions client**: `client.chat.completions.create` → `client.responses.create(...)`.
- **Κατασκευαστές πελατών Azure**: `AzureOpenAI(...)` → `OpenAI(base_url=..., api_key=...)`.
- **Εργαλεία**: μετατρέψτε τους ορισμούς εργαλείων κλήσης λειτουργιών από εμφωλευμένη μορφή (`{"type": "function", "function": {"name": ...}}`) σε επίπεδη μορφή Responses (`{"type": "function", "name": ...}`); χρησιμοποιήστε `tool_choice`; επιστρέψτε τα αποτελέσματα εργαλείων ως στοιχεία `{"type": "function_call_output", "call_id": ..., "output": ...}` (όχι `{"role": "tool", ...}`).
- **Αμφίδρομες κλήσεις εργαλείων**: όταν το μοντέλο επιστρέφει κλήσεις λειτουργιών, προσθέστε τα στοιχεία `response.output` στη συνομιλία (όχι χειροκίνητο λεξικό `{"role": "assistant", "tool_calls": [...]}`), και στη συνέχεια προσθέστε τα στοιχεία `function_call_output` για κάθε αποτέλεσμα.
- **Παραδείγματα εργαλείων με λίγα βήματα**: αν η συνομιλία περιλαμβάνει σκληροκωδικοποιημένα παραδείγματα κλήσεων εργαλείων, μετατρέψτε τα σε στοιχεία `{"type": "function_call", "id": "fc_...", "call_id": "fc_...", ...}` + `{"type": "function_call_output", ...}`. Τα IDs πρέπει να αρχίζουν με `fc_`.
- **`pydantic_function_tool()`**: αυτός ο βοηθός εξακολουθεί να παράγει την παλιά εμφωλευμένη μορφή και **δεν είναι συμβατός** με το `responses.create()`. Αντικαταστήστε με χειροκίνητους ορισμούς εργαλείων ή wrapper για επίπεδη μορφή.
- **Πολύ-στροφική**: διατηρήστε το ιστορικό της συνομιλίας στην εφαρμογή· περάστε προηγούμενες στροφές μέσω στοιχείων `input`.
- **Μορφοποίηση**: αντικαταστήστε το `response_format` κορυφαίου επιπέδου του Chat με `text.format` στις Responses. Κανονική μορφή: `text={"format": {"type": "json_schema", "name": "Output", "strict": True, "schema": {...}}}`.
- **Στοιχεία περιεχομένου**: αντικαταστήστε το Chat `content[].type: "text"` με Responses `content[].type: "input_text"` για στροφές χρήστη/συστήματος.
- **Στοιχεία περιεχομένου εικόνας**: αντικαταστήστε το Chat `content[].type: "image_url"` με Responses `content[].type: "input_image"`. Το πεδίο `image_url` αλλάζει από εμφωλευμένο αντικείμενο `{"url": "..."}` σε επίπεδο string. Δείτε το cheat sheet για παραδείγματα πριν/μετά.
- **Προσπάθεια συλλογισμού**: **migρείτε `reasoning` μόνο αν υπάρχει ήδη στον αρχικό κώδικα**.
- **Διαχείριση σφαλμάτων φίλτρου περιεχομένου**: η δομή του σώματος σφάλματος άλλαξε. Το Chat Completions χρησιμοποιούσε `error.body["innererror"]["content_filter_result"]` (ενικός· singular)· η Responses API χρησιμοποιεί `error.body["content_filters"][0]["content_filter_results"]` (πληθυντικός· plural, μέσα σε πίνακα). Κώδικας που αναφέρεται σε `innererror` θα πετάξει `KeyError`. Ξαναγράψτε για να χρησιμοποιήσει τη νέα διαδρομή.
- **Άμεσες HTTP κλήσεις**: αν η εφαρμογή καλεί απευθείας το Azure OpenAI REST API (μέσω `requests`, `httpx` κ.λπ.) χρησιμοποιώντας `/openai/deployments/{name}/chat/completions?api-version=...`, ξαναγράψτε για χρήση του `/openai/v1/responses`. Το σώμα του αιτήματος αλλάζει: `messages` → `input`, προσθέστε `max_output_tokens` και `store: false`, αφαιρέστε το query param `api-version`. Το σώμα της απόκρισης αλλάζει: `choices[0].message.content` → `output[0].content[0].text` (σημείωση: `output_text` είναι ιδιότητα ευκολίας SDK, μη παρούσα στο καθαρό REST JSON).

---

## Βήμα 2: Εφαρμογή Μετανάστευσης

### Σημειώσεις Μετανάστευσης (Chat Completions → Responses)

- **Γιατί να μεταναστεύσετε**: το Responses είναι το ενιαίο API για κείμενο, εργαλεία και streaming· το Chat Completions είναι κληρονομιά. Με το GPT-5, το Responses απαιτείται για καλύτερη απόδοση.
- **HTTP**: το endpoint Azure μεταβαίνει από `/openai/deployments/{name}/chat/completions` σε `/openai/v1/responses`.
- **Πεδία**: `messages` → `input`, `max_tokens` → `max_output_tokens`. Το `temperature` παραμένει.
- **Μορφοποίηση**: `response_format` → `text.format` με κατάλληλο αντικείμενο.
- **Στοιχεία περιεχομένου**: Αντικαταστήστε το Chat `content[].type: "text"` με Responses `content[].type: "input_text"` για στροφές συστήματος/χρήστη.
- **Στοιχεία εικόνας**: Αντικαταστήστε το Chat `content[].type: "image_url"` με Responses `content[].type: "input_image"`. Το `image_url` απλοποιείται από `{"image_url": {"url": "..."}}` σε `{"image_url": "..."}` (απλό string — είτε HTTPS URL είτε data URI `data:image/...;base64,...`).

### Αναφορά αντιστοίχισης παραμέτρων

| Chat Completions   | Responses API                       |
|--------------------|-----------------------------------|
| `prompt`           | `input`                           |
| `messages`         | `input` (πίνακας στοιχείων)       |
| `max_tokens`       | `max_output_tokens`               |
| `response_format`  | `text.format` (αντικείμενο)       |
| `temperature`      | `temperature` (αμετάβλητο)        |
| `stop`             | `stop` (αμετάβλητο)               |
| `frequency_penalty`| `frequency_penalty` (αμετάβλητο)  |
| `presence_penalty` | `presence_penalty` (αμετάβλητο)   |
| `tools` / function-calling | `tools` (αμετάβλητο)         |
| `seed`             | **Καταργείται** (δεν υποστηρίζεται)|
| `store`            | `store` (ρυθμισμένο σε `false`)  |
| `content[].type: "text"` | `content[].type: "input_text"` |
| `content[].type: "image_url"` | `content[].type: "input_image"` |
| `"image_url": {"url": "..."}` | `"image_url": "..."` (επίπεδο string)|

Για πλήρη παραδείγματα κώδικα πριν και μετά δείτε [cheat-sheet.md](./references/cheat-sheet.md).

Για μετανάστευση υποδομής τεστ (mocks, snapshots, assertions), δείτε [test-migration.md](./references/test-migration.md).

Για αντιμετώπιση σφαλμάτων και προειδοποιήσεις, δείτε [troubleshooting.md](./references/troubleshooting.md).

---

## Διατήρηση Δεδομένων & Κατάσταση

- Ορίστε `store: false` σε όλα τα αιτήματα Responses.
- Μην βασίζεστε σε προηγούμενα IDs μηνυμάτων ή στο context που αποθηκεύει ο διακομιστής· διατηρήστε κατάσταση διαχειριζόμενη από τον πελάτη και ελαχιστοποιήστε τα μεταδεδομένα.

---

## Κριτήρια Αποδοχής

### Κώδικας (πρέπει να πληρούνται όλα)

- [ ] Μηδενικές εμφανίσεις για `rg "chat\.completions\.create|ChatCompletion\.create|Completion\.create"` στα αρχεία μετανάστευσης.
- [ ] Μηδενικές εμφανίσεις για `rg "AzureOpenAI\(|AsyncAzureOpenAI\("` — όλοι οι constructors χρησιμοποιούν `OpenAI`/`AsyncOpenAI` με το endpoint v1.
- [ ] Μηδενικές εμφανίσεις για `rg "models\.github\.ai|models\.inference\.ai\.azure"` — αφαιρέθηκαν διαδρομές κώδικα GitHub Models.
- [ ] Μηδενικές εμφανίσεις για `rg "OpenAIChatCompletionClient"` — MAF 1.0.0+ χρησιμοποιεί `OpenAIChatClient` (που χρησιμοποιεί Responses API). Σε pre-1.0.0, αναβαθμίστε σε `agent-framework-openai>=1.0.0`.
- [ ] Όλες οι κλήσεις `ChatOpenAI(...)` να περιέχουν `use_responses_api=True`.
- [ ] Μηδενικές εμφανίσεις για `rg "choices\[0\]"` — η πρόσβαση σε απαντήσεις γίνεται μέσω `resp.output_text` ή σχήματος Responses.
- [ ] Καμία χρήση του `response_format` σε κορυφαίο επίπεδο· όλη η δομημένη έξοδος χρησιμοποιεί `text={"format": {...}}`.
- [ ] `openai>=1.108.1` και `azure-identity` στο `requirements.txt` ή `pyproject.toml`· εξαρτήσεις ξαναεγκατεστημένες.
- [ ] `store=False` ορισμένο σε κάθε κλήση `responses.create`.
- [ ] Καμία χρήση `api_version` στην κατασκευή πελάτη· `AZURE_OPENAI_API_VERSION` αφαιρεμένο από env αρχεία και υποδομή.

### Υποδομή τεστ (πρέπει να πληρούνται όλα)

- [ ] Μηδενικές εμφανίσεις για `rg "ChatCompletionChunk|AsyncCompletions\.create|chat\.completions" tests/`.
- [ ] Μηδενικές εμφανίσεις για `rg "_azure_ad_token_provider" tests/` — τα assertions ενημερωμένα να ελέγχουν `isinstance(client, AsyncOpenAI)` ή `base_url`.
- [ ] Μηδενικές εμφανίσεις για `rg "prompt_filter_results|content_filter_results" tests/` — αφαιρέθηκαν Azure-specific mocks φίλτρων.
- [ ] Τα mock fixtures χρησιμοποιούν `kwargs.get("input")` αντί για `kwargs.get("messages")`.
- [ ] Τα αρχεία snapshot / golden ενημερωμένα στη μορφή Responses streaming (κανένα `choices[0]`, `function_call`, `logprobs`, κ.ά.).
- [ ] `pytest` περνάει με μηδέν αποτυχίες μετά από όλες τις ενημερώσεις τεστ.

### Συμπεριφορά (να ελεγχθεί χειροκίνητα ή μέσω test harness)

- [ ] **Βασική ολοκλήρωση**: μη streaming `responses.create` επιστρέφει μη κενό `output_text`.
- [ ] **Ισοδυναμία streaming**: αν ο αρχικός κώδικας χρησιμοποιούσε streaming, ο μεταναστευμένος κώδικας streamάρει και παράγει γεγονότα `response.output_text.delta` με μη κενές μεταβολές.
- [ ] **Δομημένη έξοδος**: αν χρησιμοποιείται `text.format` με `json_schema`, το `json.loads(resp.output_text)` πετυχαίνει και ταιριάζει με το schema.
- [ ] **Βρόχος κλήσης εργαλείων**: αν χρησιμοποιούνται εργαλεία, το μοντέλο εκτελεί κλήσεις εργαλείων, η εφαρμογή τις εκτελεί, και η επακόλουθη αίτηση επιστρέφει τελικό `output_text` (όχι άπειρος βρόχος).
- [ ] **Async ισοδυναμία**: αν χρησιμοποιούταν `AsyncAzureOpenAI`, ισοδύναμη `AsyncOpenAI` δουλεύει με `await`.
- [ ] **Ποσοστό σφαλμάτων**: κανένα νέο σφάλμα 400/401/404 σε σύγκριση με τη βάση πριν τη μετανάστευση.

### Παραδοτέα

- Σύνοψη περιλαμβάνει επεξεργασμένα αρχεία, μετρήσεις πριν/μετά των legacy κλήσεων, και επόμενα βήματα.
- Αλλαγές μόνο στην working-tree (χωρίς commits).

---

## Απαιτήσεις Έκδοσης SDK

| Πακέτο         | Ελάχιστη Έκδοση |
|----------------|-----------------|
| `openai`       | `>=1.108.1`     |
| `azure-identity` | Τελευταία (για EntraID auth) |

---

## Αναφορές

- [Cheat Sheet — όλα τα αποσπάσματα κώδικα](./references/cheat-sheet.md)
- [Test Migration — mocks, snapshots, assertions](./references/test-migration.md)
- [Troubleshooting — σφάλματα, πίνακας κινδύνων, gotchas](./references/troubleshooting.md)
- [detect_legacy.py — αυτοματοποιημένος σαρωτής](../../../../../.agents/skills/azure-openai-to-responses/scripts/detect_legacy.py)
- [Azure OpenAI Starter Kit](https://aka.ms/openai/start)
- [Έγγραφα Azure OpenAI Responses API](https://learn.microsoft.com/en-us/azure/ai-foundry/openai/how-to/responses)
- [Κύκλος ζωής εκδόσεων Azure OpenAI API](https://learn.microsoft.com/en-us/azure/ai-foundry/openai/api-version-lifecycle?view=foundry-classic&tabs=python#api-evolution)
- [Αναφορά Azure OpenAI Responses API](https://platform.openai.com/docs/api-reference/responses)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Αποποίηση ευθυνών**:
Αυτό το έγγραφο έχει μεταφραστεί χρησιμοποιώντας την υπηρεσία μετάφρασης με τεχνητή νοημοσύνη [Co-op Translator](https://github.com/Azure/co-op-translator). Ενώ επιδιώκουμε την ακρίβεια, παρακαλούμε να έχετε υπόψη ότι οι αυτοματοποιημένες μεταφράσεις ενδέχεται να περιέχουν λάθη ή ανακρίβειες. Το πρωτότυπο έγγραφο στη μητρική του γλώσσα πρέπει να θεωρείται η αυθεντική πηγή. Για κρίσιμες πληροφορίες, συνιστάται επαγγελματική ανθρώπινη μετάφραση. Δεν φέρουμε ευθύνη για τυχόν παρεξηγήσεις ή λανθασμένες ερμηνείες που προκύπτουν από τη χρήση αυτής της μετάφρασης.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->