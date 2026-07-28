---
name: azure-openai-to-responses
license: MIT
---
# Μεταφορά Εφαρμογών Python από Azure OpenAI Chat Completions στο Responses API

> **ΑΥΣΤΗΡΕΣ ΟΔΗΓΙΕΣ — ΑΚΡΙΒΩΣ ΕΦΑΡΜΟΣΤΕΣ**
>
> Αυτή η δεξιότητα μεταφέρει βάσεις κώδικα Python που χρησιμοποιούν Azure OpenAI Chat Completions
> στο ενιαίο Responses API. Ακολουθήστε αυτές τις οδηγίες πιστά.
> Μην αυτοσχεδιάζετε αντιστοιχίσεις παραμέτρων ή εφευρίσκετε μορφές API.

---

## Προϋποθέσεις ενεργοποίησης

Ενεργοποιήστε αυτή τη δεξιότητα όταν ο χρήστης θέλει να:
- Μεταφέρει μια εφαρμογή Python από Azure OpenAI Chat Completions στο Responses API
- Αναβαθμίσει τη χρήση του Python OpenAI SDK στη νεότερη μορφή API στην Azure OpenAI
- Προετοιμάσει κώδικα Python για μοντέλα GPT-5 ή νεότερα που απαιτούν Responses στο Azure
- Μεταβεί από `AzureOpenAI`/`AsyncAzureOpenAI` σε τυπικό `OpenAI`/`AsyncOpenAI` πελάτη με το v1 endpoint
- Διορθώσει προειδοποιήσεις απόσυρσης που σχετίζονται με `AzureOpenAI` constructors ή `api_version`

---

## ⚠️ Συμβατότητα μοντέλων — ΕΛΕΓΞΤΕ ΠΡΩΤΑ

> **Πριν τη μετεγκατάσταση, βεβαιωθείτε ότι η ανάπτυξη Azure OpenAI υποστηρίζει το Responses API.**

### 1. Δοκιμή καπνού της ανάπτυξής σας (ταχύτερη)

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

> **Σημείωση**: Το `max_output_tokens` έχει **ελάχιστο όριο 16** στο Azure OpenAI. Τιμές κάτω από 16 επιστρέφουν σφάλμα 400. Χρησιμοποιήστε 50+ για δοκιμές καπνού.

Αν αυτό επιστρέψει 404, το μοντέλο της ανάπτυξης δεν υποστηρίζει ακόμα Responses — ελέγξτε την παρακάτω αναφορά ή αναπτύξτε ξανά με υποστηριζόμενο μοντέλο.

### 2. Ελέγξτε τα διαθέσιμα μοντέλα στην περιοχή σας (συνιστάται)

Εκτελέστε το ενσωματωμένο εργαλείο συμβατότητας μοντέλων για να δείτε τι είναι διαθέσιμο με υποστήριξη Responses API στην περιοχή σας:

```bash
python migrate.py models --subscription YOUR_SUB_ID --location YOUR_REGION
```

Αυτό ερωτά το Azure ARM live και δείχνει πίνακα συμβατότητας — ποια μοντέλα υποστηρίζουν Responses, δομημένη έξοδο, εργαλεία κ.λπ. Χρησιμοποιήστε `--filter gpt-5.1,gpt-5.2` για να περιορίσετε αποτελέσματα ή `--json` για σενάριο.

### 3. Πλήρης αναφορά υποστήριξης μοντέλων

- **Ζωντανή ερώτηση**: `python migrate.py models` (βλέπε παραπάνω — ειδικό για περιοχή, πάντα ενημερωμένη)
- **Περιηγηθείτε τη διαθεσιμότητα**: [Πίνακας περίληψης μοντέλων και διαθεσιμότητας περιοχών](https://learn.microsoft.com/en-us/azure/foundry/foundry-models/concepts/models-sold-directly-by-azure?tabs=global-standard-aoai%2Cglobal-standard&pivots=azure-openai#model-summary-table-and-region-availability)
- **Γρήγορη εκκίνηση & οδηγίες**: **https://aka.ms/openai/start**

### ⚠️ Περιορισμοί παλιότερων μοντέλων

> **ΠΡΟΕΙΔΟΠΟΙΗΣΗ**: Τα παλαιότερα μοντέλα (προ του `gpt-4.1`) ενδέχεται να μην υποστηρίζουν πλήρως όλες τις δυνατότητες του Responses API.
>
> Γνωστοί περιορισμοί με παλιά μοντέλα:
> - **παράμετρος `reasoning`**: Δεν υποστηρίζεται σε πολλά μοντέλα χωρίς reasoning. Μεταφέρετε το `reasoning` μόνο αν υπήρχε ήδη στον αρχικό κώδικα.
> - **παράμετρος `seed`**: Δεν υποστηρίζεται καθόλου στο Responses API — αφαιρέστε την από όλα τα αιτήματα.
> - **Δομημένη έξοδος μέσω `text.format`**: Τα παλιά μοντέλα μπορεί να μην εφαρμόζουν αξιόπιστα σχήματα JSON με `strict: true`.
> - **Ορχήστρωση εργαλείων**: Το GPT-5+ οργανώνει κλήσεις εργαλείων ως μέρος εσωτερικού reasoning. Τα παλιά μοντέλα στο Responses λειτουργούν αλλά χωρίς αυτήν την ενσωμάτωση.
> - **Περιορισμοί θερμοκρασίας**: Κατά τη μετεγκατάσταση σε `gpt-5`, η θερμοκρασία πρέπει να παραληφθεί ή να οριστεί σε `1`. Τα παλιά μοντέλα δεν έχουν τέτοιο περιορισμό.

### Μοντέλα λογικής σειράς O (o1, o3-mini, o3, o4-mini)

Τα μοντέλα O-series έχουν μοναδικούς περιορισμούς παραμέτρων. Κατά τη μετεγκατάσταση εφαρμογών που στοχεύουν μοντέλα O-series:

- **`temperature`**: Πρέπει να είναι `1` (ή να παραληφθεί). Τα μοντέλα O-series δεν δέχονται άλλες τιμές.
- **`max_completion_tokens` → `max_output_tokens`**: Οι εφαρμογές που χρησιμοποιούν το Azure-ειδικό `max_completion_tokens` πρέπει να περάσουν σε `max_output_tokens`. Θέστε υψηλές τιμές (4096+) γιατί οι tokens του reasoning υπολογίζονται στο όριο.
- **`reasoning_effort`**: Αν η εφαρμογή χρησιμοποιεί `reasoning_effort` (χαμηλή/μεσαία/υψηλή), κρατήστε το — το Responses API υποστηρίζει αυτή την παράμετρο για μοντέλα o-series.
- **Συμπεριφορά ροής (streaming)**: Τα μοντέλα O-series μπορεί να αποθηκεύουν την έξοδο μέχρι να ολοκληρωθεί το reasoning πριν εκπέμψουν συμβάντα κειμένου delta. Το streaming λειτουργεί ακόμα, αλλά το πρώτο `response.output_text.delta` μπορεί να φτάσει με καθυστέρηση μεγαλύτερη από τα μοντέλα GPT.
- **`top_p`**: Δεν υποστηρίζεται στα o-series — αφαιρέστε το αν υπάρχει.
- **Χρήση εργαλείων**: Τα μοντέλα O-series υποστηρίζουν εργαλεία μέσω Responses API όπως και τα μοντέλα GPT, αλλά η ποιότητα ορχήστρωσης κλήσεων εργαλείων ποικίλλει ανάλογα με το μοντέλο.

**Ενέργεια — προληπτική συμβουλή μοντέλου**: Κατά τη φάση ανίχνευσης, ελέγξτε ποιο μοντέλο στοχεύει η εφαρμογή (ονόματα ανάπτυξης, μεταβλητές περιβάλλοντος, ρυθμίσεις). Αν το μοντέλο προηγήθηκε του `gpt-4.1` (όχι gpt-4.1+), ενημερώστε προληπτικά τον χρήστη:
- Η μετεγκατάσταση θα λειτουργήσει για βασικό κείμενο, chat, streaming και εργαλεία στο τρέχον μοντέλο τους.
- Νεότερα μοντέλα (`gpt-5.1`, `gpt-5.2`) προσφέρουν καλύτερη ορχήστρωση εργαλείων, επιβολή δομημένης εξόδου, reasoning και διαθεσιμότητα σε διάφορες περιοχές.
- Πρέπει να εξετάσουν την αναβάθμιση της ανάπτυξής τους όταν είναι έτοιμοι — δεν μπλοκάρει τη μετεγκατάσταση.

Μην μπλοκάρετε ή αρνείστε τη μετεγκατάσταση βάσει έκδοσης μοντέλου. Η συμβουλή είναι ενημερωτική.

### Τα GitHub Models δεν υποστηρίζουν το Responses API

> **Τα GitHub Models (`models.github.ai`, `models.inference.ai.azure.com`) δεν υποστηρίζουν το Responses API.**

Αν η βάση κώδικα έχει διαδρομή κώδικα GitHub Models (ψάξτε για `base_url` που δείχνει σε `models.github.ai` ή `models.inference.ai.azure.com`), **αφαιρέστε την ολικά** κατά τη μετεγκατάσταση. Το Responses API απαιτεί Azure OpenAI, OpenAI ή συμβατό τοπικό endpoint (π.χ., Ollama με υποστήριξη Responses).

Ενέργεια κατά τη σάρωση:
- Επισημάνετε οποιεσδήποτε διαδρομές κώδικα GitHub Models για αφαίρεση.

---

## Μετεγκατάσταση Πλαισίου Εργασίας

Πολλές εφαρμογές χρησιμοποιούν ανώτερα πλαίσια πάνω από OpenAI. Κατά τη μετεγκατάσταση αυτών, αλλάζει το ίδιο το API του πλαισίου — όχι μόνο οι κλήσεις OpenAI από κάτω.

### Microsoft Agent Framework (MAF)

**Ελέγξτε πρώτα την έκδοση MAF** — η μετεγκατάσταση εξαρτάται αν είστε σε MAF 1.0.0+ ή προ-1.0.0 beta/rc.

#### MAF 1.0.0+ (agent-framework-openai >= 1.0.0)

Το `OpenAIChatClient` **χρησιμοποιεί ήδη το Responses API** — δεν απαιτείται μετεγκατάσταση. Αν η βάση κώδικα χρησιμοποιεί τον παλιό `OpenAIChatCompletionClient` (που καλεί `chat.completions.create`), αντικαταστήστε τον με `OpenAIChatClient`.

| Πριν | Μετά |
|--------|-------|
| `from agent_framework.openai import OpenAIChatCompletionClient` | `from agent_framework.openai import OpenAIChatClient` |
| `OpenAIChatCompletionClient(...)` | `OpenAIChatClient(...)` |

Για να ελέγξετε την έκδοση: `python -c "import agent_framework_openai; print(agent_framework_openai.__version__)"`

#### MAF προ-1.0.0 (beta/rc εκδόσεις)

Στο MAF προ-1.0.0, το `OpenAIChatClient` χρησιμοποιούσε Chat Completions. Αναβαθμίστε σε `agent-framework-openai>=1.0.0` όπου το `OpenAIChatClient` χρησιμοποιεί το Responses API από προεπιλογή.

Δεν χρειάζονται άλλες αλλαγές — τα APIs του `Agent` και των εργαλείων παραμένουν ίδια.

### LangChain (`langchain-openai`)

Προσθέστε `use_responses_api=True` στο `ChatOpenAI()`. Επίσης ενημερώστε την πρόσβαση στα αποτελέσματα από `.content` σε `.text`.

| Πριν | Μετά |
|--------|-------|
| `ChatOpenAI(model=..., base_url=..., api_key=...)` | `ChatOpenAI(model=..., base_url=..., api_key=..., use_responses_api=True)` |
| `result['messages'][-1].content` | `result['messages'][-1].text` |

Για πλήρη παραδείγματα κώδικα πριν/μετά, δείτε [cheat-sheet.md](./references/cheat-sheet.md).

---

## Οδηγίες Μετεγκατάστασης Frontend

> **Το Responses API είναι θέμα πλευράς διακομιστή.** Μεταφέρετε το backend Python σας· η σύμβαση HTTP του frontend πρέπει να παραμείνει αμετάβλητη εκτός αν το backend είναι λεπτό πέρασμα — τότε εξετάστε την υιοθέτηση της μορφής αιτήματος Responses για να εξαλειφθεί ένα επίπεδο μετάφρασης. Αν το frontend καλεί το OpenAI απευθείας με κλειδί client-side, μετακινήστε αυτές τις κλήσεις πρώτα σε backend.

### Απόσυρση `@microsoft/ai-chat-protocol`

Το npm πακέτο `@microsoft/ai-chat-protocol` είναι αποσυρμένο και πρέπει να αντικατασταθεί με το [`ndjson-readablestream`](https://www.npmjs.com/package/ndjson-readablestream). Αν το συναντήσετε σε frontend:

1. Αντικαταστήστε το CDN script tag:
   ```html
   <!-- Before -->
   <script src="https://cdn.jsdelivr.net/npm/@microsoft/ai-chat-protocol@.../dist/iife/index.js"></script>
   <!-- After -->
   <script src="https://cdn.jsdelivr.net/npm/ndjson-readablestream@1.0.7/dist/ndjson-readablestream.umd.js"></script>
   ```
2. Αφαιρέστε τη δημιουργία `AIChatProtocolClient` (`new ChatProtocol.AIChatProtocolClient("/chat")`).
3. Αντικαταστήστε το `client.getStreamedCompletion(messages)` με άμεση κλήση `fetch()` στο backend streaming endpoint.
4. Αντικαταστήστε `for await (const response of result)` με `for await (const chunk of readNDJSONStream(response.body))`.
5. Ενημερώστε την πρόσβαση στις ιδιότητες από `response.delta.content` / `response.error` σε `chunk.delta.content` / `chunk.error`.

---

## Στόχοι

- Καταγράψτε όλες τις κλήσεις Python που χρησιμοποιούν Chat Completions ή legacy Completions στην Azure OpenAI.
- Προτείνετε σχέδιο και αλληλουχία μετεγκατάστασης για τον κώδικα Python.
- Εφαρμόστε ασφαλείς, ελάχιστες αλλαγές για να γίνει μετάβαση στο Responses API.
- Ενημερώστε τους καλούντες να καταναλώνουν το σχήμα εξόδου Responses· χωρίς wrappers συμβατότητας.
- Εκτελέστε δοκιμές και linters· διορθώστε μικρά σφάλματα από τη μετεγκατάσταση.
- Προετοιμάστε μικρές σειρές αλλαγών προς αναθεώρηση και δώστε τελική περίληψη με διαφορές (μην κάνετε commit).

---

## Κανόνες προστασίας

- Τροποποιήστε μόνο αρχεία μέσα στον χώρο εργασίας git. Ποτέ έξω από αυτόν.
- Μην διατηρείτε shim συμβατότητας προς τα πίσω· μεταφέρετε τον κώδικα στην νέα μορφή API.
- Μην αφήνετε σχόλια προσωρινής χρήσης ή αρχεία backup.
- Διατηρήστε τις ροές (streaming) αν χρησιμοποιούνταν· αλλιώς χρησιμοποιήστε μη-ροή.
- Ζητήστε έγκριση πριν εκτελέσετε εντολές ή δικτυακές κλήσεις αν βρίσκεστε σε λειτουργία έγκρισης.
- Μην τρέχετε `git add`/`git commit`/`git push`; παράγετε μόνο επεξεργασίες δέντρου εργασίας.

---

## Βήμα 0: Μετεγκατάσταση πελάτη Azure OpenAI (προαπαιτούμενο)

Αν η βάση κώδικα χρησιμοποιεί τους constructors `AzureOpenAI` ή `AsyncAzureOpenAI`, μεταβείτε πρώτα στους τυπικούς constructors `OpenAI` / `AsyncOpenAI`. Οι Azure-ειδικοί constructors έχουν αποσυρθεί στο `openai>=1.108.1`.

### Γιατί το endpoint v1 API;

Το νέο endpoint `/openai/v1` χρησιμοποιεί τον τυπικό πελάτη `OpenAI()` αντί `AzureOpenAI()`, δεν απαιτεί παράμετρο `api_version` και λειτουργεί ταυτόσημα σε OpenAI και Azure OpenAI. Ο ίδιος κώδικας πελάτη είναι μελλοντικά ασφαλής — χωρίς ανάγκη διαχείρισης εκδόσεων.

### Κύριες αλλαγές

| Πριν | Μετά |
|--------|-------|
| `AzureOpenAI` | `OpenAI` |
| `AsyncAzureOpenAI` | `AsyncOpenAI` |
| `azure_endpoint` | `base_url` |
| `azure_ad_token_provider` | `api_key` |
| `api_version=...` | Αφαιρέστε ολικά |

### Λίστα ελέγχου καθαρισμού

- Αφαιρέστε την παράμετρο `api_version` από τη δημιουργία πελάτη.
- Αφαιρέστε τις μεταβλητές περιβάλλοντος `AZURE_OPENAI_VERSION` / `AZURE_OPENAI_API_VERSION` από `.env`, ρυθμίσεις app και αρχεία Bicep/infra.
- Μετονομάστε `AZURE_OPENAI_CLIENT_ID` → `AZURE_CLIENT_ID` σε `.env`, ρυθμίσεις app, Bicep/infra και fixtures τεστ (τυπική σύμβαση Azure Identity SDK).
- Βεβαιωθείτε ότι έχετε `openai>=1.108.1` στο `requirements.txt` ή `pyproject.toml`.

### Μετεγκατάσταση μεταβλητών περιβάλλοντος

| Παλιά env var | Ενέργεια | Σημειώσεις |
|-------------|--------|-------|
| `AZURE_OPENAI_VERSION` | **Αφαιρέστε** | Δεν χρειάζεται `api_version` με το endpoint v1 |
| `AZURE_OPENAI_API_VERSION` | **Αφαιρέστε** | Όπως παραπάνω |
| `AZURE_OPENAI_CLIENT_ID` | **Μετονομάστε** → `AZURE_CLIENT_ID` | Τυπική σύμβαση Azure Identity SDK για `ManagedIdentityCredential(client_id=...)` |
| `AZURE_OPENAI_ENDPOINT` | **Διατηρείστε** | Ακόμα χρειάζεται για τη δημιουργία `base_url` |
| `AZURE_OPENAI_CHAT_DEPLOYMENT` | **Διατηρείστε** | Χρησιμοποιείται ως παράμετρος `model` στο `responses.create` |
| `AZURE_OPENAI_API_KEY` | **Διατηρείστε** | Χρησιμοποιείται ως `api_key` για έλεγχο ταυτότητας με κλειδί |

Για παραδείγματα κώδικα ρύθμισης πελάτη (συγχρονισμένο, ασύγχρονο, EntraID, API key, πολλαπλοί tenants), δείτε [cheat-sheet.md](./references/cheat-sheet.md).

---

## Βήμα 1: Εντοπισμός Legacy Call Sites

Εκτελέστε το σενάριο [detect_legacy.py](../../../../../.agents/skills/azure-openai-to-responses/scripts/detect_legacy.py) για να βρείτε όλες τις κλήσεις που χρειάζονται μετεγκατάσταση:

```bash
python skills/azure-openai-to-responses/scripts/detect_legacy.py .
```

Ή εκτελέστε αυτές τις αναζητήσεις χειροκίνητα — κάθε εύρημα είναι στόχος μετεγκατάστασης:

```bash
# Κλήσεις παλαιού API (πρέπει να ξαναγραφούν)
rg "chat\.completions\.create"
rg "ChatCompletion\.create"
rg "Completion\.create"

# Αποσυρθέντες κατασκευαστές πελατών Azure (πρέπει να αντικατασταθούν)
rg "AzureOpenAI\("
rg "AsyncAzureOpenAI\("

# Πρότυπα πρόσβασης σχήματος απάντησης (πρέπει να ενημερωθούν)
rg "choices\[0\]\.message\.content"
rg "choices\[0\]\.delta\.content"
rg "choices\[0\]\.message\.function_call"
rg "choices\[0\]\.message\.tool_calls"

# Ορισμοί εργαλείων σε παλαιό εμφωλευμένο μορφότυπο (πρέπει να απο-φωλιάσουν)
rg '"function":\s*{\s*"name"'
rg "pydantic_function_tool"

# Αποτελέσματα εργαλείων σε παλαιό μορφότυπο (πρέπει να μετατραπούν σε function_call_output)
rg '"role":\s*"tool"'
rg '"tool_call_id"'

# Αποσυρθέντες παράμετροι (πρέπει να αφαιρεθούν ή να μετονομαστούν)
rg "response_format"
rg "max_tokens\b"        # μετονομασία σε max_output_tokens
rg "['\"]seed['\"]"      # remove entirely

# Αποσυρθέντες μεταβλητές περιβάλλοντος (καθαρισμός)
rg "AZURE_OPENAI_API_VERSION|AZURE_OPENAI_VERSION"
rg "AZURE_OPENAI_CLIENT_ID"  # πρέπει να είναι AZURE_CLIENT_ID

# Τερματικά μοντέλων GitHub (πρέπει να αφαιρεθούν — η API απαντήσεων δεν υποστηρίζεται)
rg "models\.github\.ai|models\.inference\.ai\.azure"

# Πρότυπα παλαιάς έκδοσης σε επίπεδο πλαισίου (πρέπει να ενημερωθούν)
rg "OpenAIChatCompletionClient"  # MAF 1.0.0+: αντικατάσταση με OpenAIChatClient
rg "ChatOpenAI\(" | grep -v "use_responses_api"  # LangChain: απαιτεί use_responses_api=True

# Υποδομή δοκιμών (πρέπει να ενημερωθεί)
rg "ChatCompletionChunk|AsyncCompletions\.create" tests/
rg "_azure_ad_token_provider" tests/
rg "prompt_filter_results|content_filter_results" tests/
rg "choices\[0\]" tests/

# Πρόσβαση στο σώμα σφάλματος φίλτρου περιεχομένου (πρέπει να ενημερωθεί — αλλάζει δομή)
rg 'innererror.*content_filter_result|error\.body\["innererror"\]'
rg "content_filter_result\[" # παλαιός ενικός τύπος — τώρα content_filter_results (πληθυντικός) μέσα στον πίνακα content_filters

# Ακατέργαστες κλήσεις HTTP στο τερματικό Chat Completions (πρέπει να ενημερωθεί το URL)
rg "/openai/deployments/.*/chat/completions"
rg "api-version="
```

### Ευρετικές (ανίχνευση και επανεγγραφή)

- **Πελάτης Chat Completions**: `client.chat.completions.create` → `client.responses.create(...)`.

- **Κατασκευαστές πελατών Azure**: `AzureOpenAI(...)` → `OpenAI(base_url=..., api_key=...)`.
- **Εργαλεία**: μετατρέψτε τους ορισμούς εργαλείων κλήσης λειτουργιών από εμφωλευμένη μορφή (`{"type": "function", "function": {"name": ...}}`) σε επίπεδη μορφή Responses (`{"type": "function", "name": ...}`); χρησιμοποιήστε `tool_choice`; επιστρέψτε αποτελέσματα εργαλείων ως στοιχεία `{"type": "function_call_output", "call_id": ..., "output": ...}` (όχι `{"role": "tool", ...}`).
- **Περίοδοι εργαλείων**: όταν το μοντέλο επιστρέφει κλήσεις λειτουργιών, προσθέστε τα στοιχεία `response.output` στη συνομιλία (όχι ένα χειροκίνητο λεξικό `{"role": "assistant", "tool_calls": [...]}`), μετά προσθέστε στοιχεία `function_call_output` για κάθε αποτέλεσμα.
- **Παραδείγματα εργαλείων λίγων βολών**: εάν η συνομιλία περιλαμβάνει σκληροκωδικοποιημένα παραδείγματα κλήσεων εργαλείων, μετατρέψτε τα σε στοιχεία `{"type": "function_call", "id": "fc_...", "call_id": "fc_...", ...}` + `{"type": "function_call_output", ...}`. Τα αναγνωριστικά πρέπει να ξεκινούν με `fc_`.
- **`pydantic_function_tool()`**: αυτό το βοηθητικό εξακολουθεί να παράγει την παλιά εμφωλευμένη μορφή και **δεν είναι συμβατό** με `responses.create()`. Αντικαταστήστε με χειροκίνητους ορισμούς εργαλείων ή έναν wrapper για επίπεδη μορφή.
- **Πολλαπλούς γύρους**: διατηρήστε το ιστορικό συνομιλίας στην εφαρμογή· περάστε προηγούμενους γύρους μέσω στοιχείων `input`.
- **Μορφοποίηση**: αντικαταστήστε το επίπεδο κορυφής `response_format` του Chat με `text.format` στις Responses. Κανονική μορφή: `text={"format": {"type": "json_schema", "name": "Output", "strict": True, "schema": {...}}}`.
- **Στοιχεία περιεχομένου**: αντικαταστήστε το Chat `content[].type: "text"` με Responses `content[].type: "input_text"` για στροφές χρήστη/συστήματος.
- **Στοιχεία περιεχομένου εικόνας**: αντικαταστήστε το Chat `content[].type: "image_url"` με Responses `content[].type: "input_image"`. Το πεδίο `image_url` αλλάζει από εμφωλευμένο αντικείμενο `{"url": "..."}` σε απλή συμβολοσειρά. Δείτε το cheat sheet για παραδείγματα πριν/μετά.
- **Προσπάθεια λογικής**: **μεταφέρετε το `reasoning` μόνο αν υπάρχει ήδη στον αρχικό κώδικα**.
- **Διαχείριση σφαλμάτων φίλτρου περιεχομένου**: η δομή του σώματος σφάλματος άλλαξε. Τα Chat Completions χρησιμοποιούσαν `error.body["innererror"]["content_filter_result"]` (ενικός); η Responses API χρησιμοποιεί `error.body["content_filters"][0]["content_filter_results"]` (πληθυντικός, μέσα σε πίνακα). Κώδικας που προσπελαύνει το `innererror` θα προκαλέσει `KeyError`. Ξαναγράψτε για να χρησιμοποιήσετε το νέο μονοπάτι.
- **Απευθείας HTTP κλήσεις**: αν η εφαρμογή κάνει κλήσεις Azure OpenAI REST API απευθείας (μέσω `requests`, `httpx`, κλπ.) χρησιμοποιώντας `/openai/deployments/{name}/chat/completions?api-version=...`, ξαναγράψτε σε `/openai/v1/responses`. Το σώμα του αιτήματος αλλάζει: `messages` → `input`, προσθέστε `max_output_tokens` και `store: false`, αφαιρέστε το query param `api-version`. Το σώμα της απάντησης αλλάζει: `choices[0].message.content` → `output[0].content[0].text` (σημείωση: το `output_text` είναι ιδιότητα ευκολίας SDK, απουσιάζει από το ακατέργαστο JSON).

---

## Βήμα 2: Εφαρμογή Μεταφοράς

### Σημειώσεις Μεταφοράς (Chat Completions → Responses)

- **Γιατί να μεταφερθεί**: Το Responses είναι η ενοποιημένη API για κείμενο, εργαλεία και ροή· το Chat Completions είναι παλαιό. Με GPT-5, το Responses απαιτείται για καλύτερη απόδοση.
- **HTTP**: Το Azure endpoint αλλαγές από `/openai/deployments/{name}/chat/completions` σε `/openai/v1/responses`.
- **Πεδία**: `messages` → `input`, `max_tokens` → `max_output_tokens`. `temperature` παραμένει ίση.
- **Μορφοποίηση**: `response_format` → `text.format` με κατάλληλο αντικείμενο.
- **Στοιχεία περιεχομένου**: Αντικαταστήστε το Chat `content[].type: "text"` με Responses `content[].type: "input_text"` για στροφές συστήματος/χρήστη.
- **Στοιχεία περιεχομένου εικόνας**: Αντικαταστήστε το Chat `content[].type: "image_url"` με Responses `content[].type: "input_image"`. Απλοποιήστε το πεδίο `image_url` από `{"image_url": {"url": "..."}}` σε `{"image_url": "..."}` (απλή συμβολοσειρά — είτε HTTPS URL είτε URI δεδομένων `data:image/...;base64,...`).

### Αναφορά Αντιστοίχισης Παραμέτρων

| Chat Completions | Responses API |
|-----------------|---------------|
| `prompt` | `input` |
| `messages` | `input` (πίνακας στοιχείων) |
| `max_tokens` | `max_output_tokens` |
| `response_format` | `text.format` (αντικείμενο) |
| `temperature` | `temperature` (αμετάβλητο) |
| `stop` | `stop` (αμετάβλητο) |
| `frequency_penalty` | `frequency_penalty` (αμετάβλητο) |
| `presence_penalty` | `presence_penalty` (αμετάβλητο) |
| `tools` / function-calling | `tools` (αμετάβλητο) |
| `seed` | **Καταργήστε** (μη υποστηριζόμενο) |
| `store` | `store` (ορίστε σε `false`) |
| `content[].type: "text"` | `content[].type: "input_text"` |
| `content[].type: "image_url"` | `content[].type: "input_image"` |
| `"image_url": {"url": "..."}` | `"image_url": "..."` (απλή συμβολοσειρά) |

Για πλήρη παραδείγματα κώδικα πριν/μετά, δείτε [cheat-sheet.md](./references/cheat-sheet.md).

Για μεταφορά υποδομής δοκιμών (mocks, snapshots, assertions), δείτε [test-migration.md](./references/test-migration.md).

Για αντιμετώπιση σφαλμάτων και προβλημάτων, δείτε [troubleshooting.md](./references/troubleshooting.md).

---

## Διατήρηση Δεδομένων & Κατάσταση

- Ορίστε `store: false` σε όλα τα αιτήματα Responses.
- Μην βασίζεστε σε προηγούμενα αναγνωριστικά μηνυμάτων ή συμφραζόμενα αποθηκευμένα στον διακομιστή· κρατήστε κατάσταση διαχειριζόμενη από τον πελάτη και ελαχιστοποιήστε τα μεταδεδομένα.

---

## Κριτήρια Αποδοχής

### Διαύλους επιπέδου κώδικα (όλοι πρέπει να περάσουν)

- [ ] Μηδενικές εμφανίσεις για `rg "chat\.completions\.create|ChatCompletion\.create|Completion\.create"` σε αρχεία μετά τη μεταφορά.
- [ ] Μηδενικές εμφανίσεις για `rg "AzureOpenAI\(|AsyncAzureOpenAI\("` — όλοι οι κατασκευαστές χρησιμοποιούν `OpenAI`/`AsyncOpenAI` με το v1 endpoint.
- [ ] Μηδενικές εμφανίσεις για `rg "models\.github\.ai|models\.inference\.ai\.azure"` — οι διαδρομές κώδικα GitHub Models αφαιρέθηκαν.
- [ ] Μηδενικές εμφανίσεις για `rg "OpenAIChatCompletionClient"` — o κώδικας MAF 1.0.0+ χρησιμοποιεί `OpenAIChatClient` (που χρησιμοποιεί Responses API). Σε pre-1.0.0, αναβαθμίστε σε `agent-framework-openai>=1.0.0`.
- [ ] Όλες οι κλήσεις `ChatOpenAI(...)` περιλαμβάνουν `use_responses_api=True`.
- [ ] Μηδενικές εμφανίσεις για `rg "choices\[0\]"` — όλη η πρόσβαση απαντήσεων χρησιμοποιεί `resp.output_text` ή το σχήμα εξόδου Responses.
- [ ] Καμία χρήση `response_format` σε επίπεδο κορυφής· όλη η δομημένη έξοδος χρησιμοποιεί `text={"format": {...}}`.
- [ ] `openai>=1.108.1` και `azure-identity` στο `requirements.txt` ή `pyproject.toml`; οι εξαρτήσεις έχουν επανεγκατασταθεί.
- [ ] `store=False` ορισμένο σε κάθε κλήση `responses.create`.
- [ ] Καμία `api_version` στην κατασκευή πελάτη· `AZURE_OPENAI_API_VERSION` αφαιρέθηκε από αρχεία περιβάλλοντος και υποδομή.

### Διαύλους υποδομής δοκιμών (όλοι πρέπει να περάσουν)

- [ ] Μηδενικές εμφανίσεις για `rg "ChatCompletionChunk|AsyncCompletions\.create|chat\.completions" tests/`.
- [ ] Μηδενικές εμφανίσεις για `rg "_azure_ad_token_provider" tests/` — οι assertions ενημερώθηκαν να ελέγχουν `isinstance(client, AsyncOpenAI)` ή `base_url`.
- [ ] Μηδενικές εμφανίσεις για `rg "prompt_filter_results|content_filter_results" tests/` — τα Azure-specific φίλτρα mocks αφαιρέθηκαν.
- [ ] Τα mock fixtures χρησιμοποιούν `kwargs.get("input")` όχι `kwargs.get("messages")`.
- [ ] Snapshot / golden αρχεία ανανεώθηκαν στο σχήμα ροής Responses (χωρίς `choices[0]`, `function_call`, `logprobs`, κλπ.).
- [ ] `pytest` περνάει χωρίς αποτυχίες μετά τις ενημερώσεις όλων των δοκιμών.

### Διαύλους συμπεριφοράς (επαληθεύστε χειροκίνητα ή με test harness)

- [ ] **Βασική ολοκλήρωση**: το μη ροής `responses.create` επιστρέφει μη κενό `output_text`.
- [ ] **Ισοτιμία ροής**: αν ο αρχικός κώδικας χρησιμοποιούσε ροή, ο μεταφερμένος κώδικας κάνει ροή και παράγει γεγονότα `response.output_text.delta` με μη κενά δελτά.
- [ ] **Δομημένη έξοδος**: αν χρησιμοποιείται `text.format` με `json_schema`, το `json.loads(resp.output_text)` επιτυγχάνει και ταιριάζει με το σχήμα.
- [ ] **Βρόχος κλήσης εργαλείων**: αν χρησιμοποιούνται εργαλεία, το μοντέλο εκδίδει κλήσεις εργαλείων, η εφαρμογή τις εκτελεί, και το επόμενο αίτημα επιστρέφει τελικό `output_text` (χωρίς άπειρο βρόχο).
- [ ] **Ισοτιμία Async**: αν χρησιμοποιήθηκε `AsyncAzureOpenAI`, το αντίστοιχο `AsyncOpenAI` λειτουργεί με `await`.
- [ ] **Ποσοστό σφαλμάτων**: δεν υπάρχουν νέα σφάλματα 400/401/404 σε σύγκριση με τη βάση πριν τη μεταφορά.

### Παραδοτέα

- Η περίληψη περιλαμβάνει επεξεργασμένα αρχεία, μετρήσεις πριν/μετά των παλαιών σημείων κλήσης, και επόμενα βήματα.
- Οι αλλαγές είναι μόνο επεξεργασίες δέντρου εργασίας (χωρίς commits).

---

## Απαιτήσεις Έκδοσης SDK

| Πακέτο | Ελάχιστη Έκδοση |
|---------|----------------|
| `openai` | `>=1.108.1` |
| `azure-identity` | Νεότερο (για πιστοποίηση EntraID) |

---

## Αναφορές

- [Φύλλο Αναφοράς — όλα τα αποσπάσματα κώδικα](./references/cheat-sheet.md)
- [Μεταφορά Δοκιμών — mocks, snapshots, assertions](./references/test-migration.md)
- [Αντιμετώπιση προβλημάτων — σφάλματα, πίνακας κινδύνων, προβλήματα](./references/troubleshooting.md)
- [detect_legacy.py — αυτόματος σαρωτής](../../../../../.agents/skills/azure-openai-to-responses/scripts/detect_legacy.py)
- [Azure OpenAI Starter Kit](https://aka.ms/openai/start)
- [Τεκμηρίωση Azure OpenAI Responses API](https://learn.microsoft.com/en-us/azure/ai-foundry/openai/how-to/responses)
- [Κύκλος ζωής έκδοσης Azure OpenAI API](https://learn.microsoft.com/en-us/azure/ai-foundry/openai/api-version-lifecycle?view=foundry-classic&tabs=python#api-evolution)
- [OpenAI Responses API αναφορά](https://platform.openai.com/docs/api-reference/responses)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Αποποίηση ευθυνών**:
Αυτό το έγγραφο έχει μεταφραστεί χρησιμοποιώντας την υπηρεσία μετάφρασης με τεχνητή νοημοσύνη [Co-op Translator](https://github.com/Azure/co-op-translator). Ενώ επιδιώκουμε την ακρίβεια, παρακαλούμε να έχετε υπόψη ότι οι αυτοματοποιημένες μεταφράσεις ενδέχεται να περιέχουν λάθη ή ανακρίβειες. Το πρωτότυπο έγγραφο στη μητρική του γλώσσα πρέπει να θεωρείται η αυθεντική πηγή. Για κρίσιμες πληροφορίες, συνιστάται επαγγελματική ανθρώπινη μετάφραση. Δεν φέρουμε ευθύνη για τυχόν παρεξηγήσεις ή λανθασμένες ερμηνείες που προκύπτουν από τη χρήση αυτής της μετάφρασης.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->