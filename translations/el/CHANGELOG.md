# Ιστορικό αλλαγών

Όλες οι σημαντικές αλλαγές στο μάθημα **AI Agents for Beginners** τεκμηριώνονται σε αυτό το αρχείο.

## [Μη Κυκλοφορημένη Έκδοση] — 2026-07-06

Αυτή η έκδοση μεταφέρει το μάθημα στο **Azure OpenAI Responses API**, τυποποιεί την ονομασία προϊόντων στο **Microsoft Foundry** και το **Microsoft Agent Framework (MAF)**, αποσύρει τα GitHub Models, ενημερώνει τις εκδόσεις SDK και προσθέτει νέο περιεχόμενο για τοπικά μοντέλα και φιλοξενία άλλων πλαισίων στο Foundry.

### Προστέθηκε

- **Δεξιότητα Μετάβασης** — Εγκαταστάθηκε η Δεξιότητα Πράκτορα [`azure-openai-to-responses`](./.agents/skills/azure-openai-to-responses/SKILL.md) (από το [Azure-Samples/azure-openai-to-responses](https://github.com/Azure-Samples/azure-openai-to-responses)) κάτω από το `.agents/skills/`, συμπεριλαμβανομένων των αναφορών και του script σαρωτή.
- **Foundry Local (εκτέλεση μοντέλων στη συσκευή)** — Νέα ενότητα "Εναλλακτικός Πάροχος: Foundry Local" στο [00-course-setup/README.md](./00-course-setup/README.md) που καλύπτει την εγκατάσταση (`winget` / `brew`), το `foundry model run`, το `foundry-local-sdk`, και τη σύνδεση του `FoundryLocalManager` με το Microsoft Agent Framework μέσω `OpenAIChatClient`.
- **Φιλοξενία πρακτόρων LangChain / LangGraph στο Microsoft Foundry** — Νέα ενότητα στο [14-microsoft-agent-framework/README.md](./14-microsoft-agent-framework/README.md) και λειτουργικό δείγμα [14-langchain-hosted-agent.py](../../14-microsoft-agent-framework/code-samples/14-langchain-hosted-agent.py) που χρησιμοποιεί `langchain-azure-ai[hosting]` και `ResponsesHostServer` (το πρωτόκολλο `/responses`), βασισμένο στο [Microsoft Learn](https://learn.microsoft.com/azure/foundry/how-to/develop/langchain-hosted-agents).
- **Microsoft Project Opal** — Νέα ενότητα "Παράδειγμα Πραγματικού Κόσμου: Microsoft Project Opal" στο [15-browser-use/README.md](./15-browser-use/README.md) που πλαισιώνει το Opal ως πράκτορα χρήσης υπολογιστή για επιχειρήσεις και αντιστοιχίζει τις έννοιες του μαθήματος (άνθρωπος στο βρόχο, εμπιστοσύνη/ασφάλεια, σχεδιασμός, Δεξιότητες).
- **Δεύτερο Δείγμα Μαθήματος 02 Python** — Προστέθηκε το [02-python-agent-framework-azure-openai.ipynb](./02-explore-agentic-frameworks/code_samples/02-python-agent-framework-azure-openai.ipynb) (βλέπε "Αλλαγές" — μεταφέρθηκε από το πρώην notebook Semantic Kernel) και συνδέθηκε στο README του μαθήματος.
- Προστέθηκε ενότητα **Μοντέλα και Πάροχοι** στο [STUDY_GUIDE.md](./STUDY_GUIDE.md).

### Αλλαγές

- **Chat Completions → Responses API (Python).** Παραδείγματα που κάλεσαν απευθείας το μοντέλο μεταφέρθηκαν από το Chat Completions στο Responses API (`client.responses.create(input=..., store=False)`, `resp.output_text`), χρησιμοποιώντας τον πελάτη `OpenAI` στην σταθερή τελική σημείο Azure OpenAI `/openai/v1/` (χωρίς `api_version`). Επηρεασμένα παραδείγματα:
  - [06-building-trustworthy-agents/code_samples/06-system-message-framework.ipynb](./06-building-trustworthy-agents/code_samples/06-system-message-framework.ipynb)
  - [06-building-trustworthy-agents/code_samples/06-human-in-the-loop.ipynb](./06-building-trustworthy-agents/code_samples/06-human-in-the-loop.ipynb)
  - [04-tool-use/README.md](./04-tool-use/README.md) — η πλήρης περιήγηση στη λειτουργία κλήσης εργαλείων (το σχήμα εργαλείου απλοποιήθηκε στη μορφή Responses, τα αποτελέσματα εργαλείων επιστράφηκαν ως `function_call_output`, `max_output_tokens` κ.ά.).
- **GitHub Models → Azure OpenAI.** Τα GitHub Models καταργούνται (απόσυρση **Ιούλιος 2026**) και δεν υποστηρίζουν το Responses API. Όλοι οι διαδρομές κώδικα GitHub Models μετατράπηκαν σε Azure OpenAI / Microsoft Foundry σε Python και .NET παραδείγματα:
  - Python: notebooks ροής εργασίας Μαθήματος 08 (`01`–`03`), Μάθημα 14 (`14-handoff`, `14-human-loop`, `hotel_booking_workflow_sample.py`).
  - .NET: `01`–`04`, `07`, `08` `*-dotnet-agent-framework.cs` + συνοδευτικά `.md` έγγραφα, και τα notebooks/`.md` ροής εργασίας του Μαθήματος 08 dotNET (`01`–`03`) πλέον χρησιμοποιούν `AzureOpenAIClient(...).GetOpenAIResponseClient(deployment).CreateAIAgent(...)` με `AzureCliCredential`.
- **Semantic Kernel → Microsoft Agent Framework.** Το προηγούμενο `02-semantic-kernel.ipynb` ξαναγράφτηκε για χρήση με το Microsoft Agent Framework και Azure OpenAI (Responses API) και μετονομάστηκε σε `02-python-agent-framework-azure-openai.ipynb`.
- **Τυποποίηση στο `FoundryChatClient` + `as_agent`.** Ο κώδικας README και notebook που αναφερόταν σε `AzureAIProjectAgentProvider` τυποποιήθηκε στο κανονικό μοτίβο που χρησιμοποιείται από το Μάθημα 01 και τα δικά του παραδείγματα: `FoundryChatClient(project_endpoint=..., model=..., credential=AzureCliCredential())` με `provider.as_agent(...)`. Ενημερώθηκε σε όλα τα README και notebooks από Μάθημα 02 έως 14 (π.χ. μνήμη Μαθήματος 13, όλα τα notebooks Μαθήματος 14, `11-agentic-protocols/code_samples/github-mcp/app.py`).
- **Ονομασία προϊόντων.** Μετονομάστηκε σε όλο το αγγλικό περιεχόμενο:
  - "Azure AI Foundry" / "Azure AI Studio" → **Microsoft Foundry**
  - "Azure AI Agent Service" → **Microsoft Foundry Agent Service**
  - (Αμετάβλητο: "Azure OpenAI", "Azure AI Search", "Azure AI Inference" και ονόματα μεταβλητών περιβάλλοντος.)
- **Εξαρτήσεις** ([requirements.txt](../../requirements.txt)):
  - Καθορισμένες εκδόσεις `agent-framework>=1.10.0`, `agent-framework-foundry>=1.10.0`, `agent-framework-openai>=1.10.0`.
  - Καθορισμένη έκδοση `openai>=1.108.1` (ελάχιστο για το Responses API).
  - Αφαιρέθηκε `azure-ai-inference` (χρησιμοποιούταν μόνο από τα μεταφερμένα παραδείγματα GitHub Models).
- **Διαμόρφωση περιβάλλοντος** ([.env.example](../../.env.example)): αφαιρέθηκαν μεταβλητές GitHub Models (`GITHUB_TOKEN`, `GITHUB_ENDPOINT`, `GITHUB_MODEL_ID`), προστέθηκαν `AZURE_OPENAI_ENDPOINT`, `AZURE_OPENAI_DEPLOYMENT`, και προαιρετικά `AZURE_OPENAI_API_KEY`; ενημερώθηκε η ονομασία σε Microsoft Foundry.
- **Τεκμηρίωση** — Ενημερώθηκαν τα [00-course-setup/README.md](./00-course-setup/README.md), [AGENTS.md](./AGENTS.md), [README.md](./README.md) και [STUDY_GUIDE.md](./STUDY_GUIDE.md) για τα παραπάνω (μεταβλητές περιβάλλοντος ρύθμισης, απόσπασμα επιβεβαίωσης, καθοδήγηση παρόχου, ονομασία).

### Αφαιρέθηκαν

- Βήματα onboarding για τα GitHub Models και μεταβλητές περιβάλλοντος από τα έγγραφα ρύθμισης (αντικαταστάθηκαν από Azure OpenAI / Microsoft Foundry).

### Ασφάλεια / Ιδιωτικότητα (καθαρισμός πριν τη δημόσια κοινοποίηση)

- Καθαρίστηκαν αποτελέσματα εκτέλεσης Jupyter notebook που διέρρεαν πραγματικό **Azure subscription ID**, ονόματα resource-group / πόρων και Bing connection ID, καθώς και **τοπικές διαδρομές αρχείων και ονόματα χρηστών** προγραμματιστών, στα:
  - `08-multi-agent/code_samples/workflows-agent-framework/dotNET/04.dotnet-agent-framework-workflow-aifoundry-condition.ipynb`
  - `08-multi-agent/code_samples/workflows-agent-framework/python/04.python-agent-framework-workflow-aifoundry-condition.ipynb`
  - `15-browser-use/15-browser-user.ipynb`
- Επαληθεύτηκε ότι δεν έχουν απομείνει API κλειδιά, tokens, subscription IDs ή προσωπικές διαδρομές στο παρακολουθούμενο αγγλικό περιεχόμενο (οι αναφορές `GITHUB_TOKEN` που απομένουν είναι του GitHub Actions token σε ροές εργασίας και του GitHub MCP server PAT στη ρύθμιση του Μαθήματος 11 — και τα δύο νόμιμα και άσχετα με τα GitHub Models).

### Σημειώσεις και γνωστές περιορισμοί

- **Δεν εκτελέστηκαν/συγκροτήθηκαν.** Πρόκειται για εκπαιδευτικά παραδείγματα ενημερωμένα για σωστή χρήση API/ονόματος· δεν εκτελέστηκαν σε ζωντανές Azure υποδομές και τα .NET παραδείγματα δεν συγκροτήθηκαν σε αυτό το περιβάλλον. Επικυρώστε με το δικό σας Microsoft Foundry / Azure OpenAI deployment.
- **Η ανάπτυξη μοντέλου πρέπει να υποστηρίζει το Responses API.** Χρησιμοποιήστε ανάπτυξη όπως `gpt-4o-mini`, `gpt-4.1` ή μοντέλο `gpt-5.x`. Παλαιότερα μοντέλα υποστηρίζουν βασικές λειτουργίες Responses αλλά όχι κάθε δυνατότητα.
- **Έκδοση agent-framework.** Τα παραδείγματα στοχεύουν την τελευταία έκδοση MAF (`>=1.10.0`). Η κανονική κλήση δημιουργίας πράκτορα είναι `client.as_agent(...)`. Οι API επαληθεύτηκαν με βάση τα δημοσιευμένα έγγραφα του framework και μια εγκατεστημένη έκδοση. Αν καθορίσετε άλλη έκδοση, βεβαιωθείτε για τη διαθεσιμότητα μεθόδων (`as_agent` έναντι `create_agent`).
- **Notebook ροής εργασίας Μαθήματος 08, 04** διατηρεί σκόπιμα το `AzureAIAgentClient` (από `agent-framework-azure-ai`), γιατί χρησιμοποιεί εργαλεία φιλοξενίας Microsoft Foundry Agent Service (Bing grounding, code interpreter)· το οποίο βασίζεται ήδη σε Responses.
- **Προεπιλεγμένη ανάπτυξη .NET.** Δύο δείγματα ροής εργασίας Μαθήματος 08 dotNET προηγουμένως είχαν σκληροκωδικοποιημένο `gpt-4o`; τώρα προεπιλογή είναι το `AZURE_OPENAI_DEPLOYMENT` (`gpt-4o-mini`). Αν ένα δείγμα απαιτεί πολυτροπική/οπτική είσοδο, ορίστε το `AZURE_OPENAI_DEPLOYMENT` σε κατάλληλο μοντέλο.
- **Foundry Local** προσφέρει OpenAI-συμβατό τελικό σημείο **Chat Completions** και προορίζεται για τοπική ανάπτυξη. Χρησιμοποιήστε Azure OpenAI / Microsoft Foundry για πλήρη λειτουργικότητα Responses API.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Αποποίηση ευθυνών**:
Αυτό το έγγραφο έχει μεταφραστεί χρησιμοποιώντας την υπηρεσία μετάφρασης με τεχνητή νοημοσύνη [Co-op Translator](https://github.com/Azure/co-op-translator). Ενώ επιδιώκουμε την ακρίβεια, παρακαλούμε να έχετε υπόψη ότι οι αυτοματοποιημένες μεταφράσεις ενδέχεται να περιέχουν λάθη ή ανακρίβειες. Το πρωτότυπο έγγραφο στη μητρική του γλώσσα πρέπει να θεωρείται η αυθεντική πηγή. Για κρίσιμες πληροφορίες, συνιστάται επαγγελματική ανθρώπινη μετάφραση. Δεν φέρουμε ευθύνη για τυχόν παρεξηγήσεις ή λανθασμένες ερμηνείες που προκύπτουν από τη χρήση αυτής της μετάφρασης.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->