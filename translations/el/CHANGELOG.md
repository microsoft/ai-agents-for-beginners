# Ιστορικό Αλλαγών

Όλες οι σημαντικές αλλαγές στο μάθημα **AI Agents for Beginners** τεκμηριώνονται σε αυτό το αρχείο.

## [Κυκλοφόρησε] — 2026-07-14

Αυτή η έκδοση μεταφέρει το μάθημα από δύο πρόσφατα αποσυρμένα μοντέλα, μετεγκαθιστά τα υπόλοιπα τετράδια μαθήματος στο σταθερό API του Microsoft Agent Framework και επικυρώνει τα τετράδια Python έναντι μιας ζωντανής ανάπτυξης Microsoft Foundry.

### Αλλαγές

- **Μετακόμισε από τα αποσυρμένα μοντέλα (`gpt-4.1` / `gpt-4.1-mini` → `gpt-5-mini`).** Τόσο το `gpt-4.1` όσο και το `gpt-4.1-mini` έχουν πλέον αποσυρθεί (η επίσημη ημερομηνία απόσυρσης είναι **14 Οκτωβρίου 2026**). Αντικαταστάθηκαν όλες οι αναφορές στο μάθημα (έγγραφα, `.env.example`, Python/.NET τετράδια και δείγματα) με το μη αποσυρμένο `gpt-5-mini`. Το παράδειγμα δρομολόγησης μοντέλου του Μαθήματος 16 διατηρεί αντίθεση μικρού/μεγάλου χρησιμοποιώντας `gpt-5-nano` (μικρό) και `gpt-5-mini` (μεγάλο). Τα ενσωματωμένα αρχεία τρίτων ([15-browser-use/llms.txt](../../15-browser-use/llms.txt)), το ιστορικό κείμενο GitHub Models και οι σημειώσεις ικανοτήτων του skill `azure-openai-to-responses` παρέμειναν σκόπιμα αμετάβλητα.
- **Το τετράδιο παράδοσης του Μαθήματος 14 μετεγκαταστάθηκε στο σταθερό API.** Το [14-handoff.ipynb](./14-microsoft-agent-framework/code-samples/14-handoff.ipynb) πλέον χρησιμοποιεί `agent_framework.orchestrations.HandoffBuilder` με `.with_start_agent(...)`, `HandoffAgentUserRequest.create_response(...)`, ροή βασισμένη σε `event.type`, και `FoundryChatClient` (αντικαθιστώντας τα αφαιρεθέντα σύμβολα προ-1.0 `HandoffBuilder`/`ChatMessage`/`RequestInfoEvent`).
- **Το τετράδιο ανθρώπου-στο-βρόχο του Μαθήματος 14 μετεγκαταστάθηκε στο σταθερό API.** Το [14-human-loop.ipynb](./14-microsoft-agent-framework/code-samples/14-human-loop.ipynb) πλέον σταματά μέσω `ctx.request_info(...)` + `@response_handler` (αντικαθιστώντας τα αφαιρεθέντα `RequestInfoExecutor` / `RequestInfoMessage` / `RequestResponse`), κατασκευάζεται με `WorkflowBuilder(start_executor=..., output_executors=[...])`, κατευθύνει δομημένη έξοδο μέσω `default_options={"response_format": ...}`, και χρησιμοποιεί σκηνοθετημένη απάντηση ώστε το τετράδιο να εκτελείται ανεξάρτητα (χωρίς μπλοκάρισμα από `input()`).
- **Ρύθμιση περιβάλλοντος** ([.env.example](../../.env.example)): άλλαξαν τα ονόματα ανάπτυξης μοντέλου σε `gpt-5-mini`, προστέθηκαν τα `AZURE_AI_SMALL_MODEL` / `AZURE_AI_LARGE_MODEL` (δρομολόγηση Μαθήματος 16) και το προηγουμένως απούσα `AZURE_OPENAI_CHAT_DEPLOYMENT_NAME` (χρήση browser Μαθήματος 15).
- **Εξαρτήσεις** ([requirements.txt](../../requirements.txt)): δέσμευση των `agent-framework`, `agent-framework-foundry`, και `agent-framework-openai` στο `~=1.10.0` για ένα αυτο-συνεπές, επικυρωμένο σύνολο (στην έκδοση 1.11.0 εισάγονται πειραματικές αλλαγές που σπάνε τις επιφάνειες που χρησιμοποιούν αυτά τα μαθήματα).

### Σημειώσεις και γνωστοί περιορισμοί

- **Επικυρώθηκε έναντι ζωντανού Microsoft Foundry.** Τα τετράδια Python εκτελέστηκαν χωρίς περιβάλλον χρήστη με `nbconvert` σε έργο Microsoft Foundry χρησιμοποιώντας `gpt-5-mini` (και `gpt-5-nano` για τη δρομολόγηση Μαθήματος 16). Αναπτύξτε ισοδύναμα μη αποσυρμένα μοντέλα στο δικό σας έργο· τα τετράδια διαβάζουν το όνομα ανάπτυξης από `AZURE_AI_MODEL_DEPLOYMENT_NAME` / `AZURE_OPENAI_DEPLOYMENT`.
- **Ακόμη απαιτούνται επιπλέον πόροι για μερικά μαθήματα.** Το Μάθημα 05 χρειάζεται Azure AI Search· η ροή εργασιών υπόβαθρου Bing του Μαθήματος 08 (`04.python-agent-framework-workflow-aifoundry-condition.ipynb`) χρειάζεται σύνδεση Bing και εργαλεία φιλοξενούμενα από Microsoft Foundry Agent Service· τα Μαθήματα 13 (Cognee) και 17 (Foundry Local) χρειάζονται δικά τους περιβάλλοντα εκτέλεσης.

## [Κυκλοφόρησε] — 2026-07-13

Αυτή η έκδοση προσθέτει δύο νέα μαθήματα που ολοκληρώνουν την ακολουθία ανάπτυξης — κλιμάκωση πρακτόρων στο Microsoft Foundry και κατέβασμα σε έναν μόνο υπολογιστή — συν μια ροή δοκιμής καπνού, ανανεωμένη πλοήγηση μαθήματος, νέες δεξιότητες μαθητών, και ανανεωμένη επωνυμία.

### Προσθήκες

- **Μάθημα 16 — Ανάπτυξη Κλιμακούμενων Πρακτόρων με Microsoft Foundry.** Νέο μάθημα [16-deploying-scalable-agents/README.md](./16-deploying-scalable-agents/README.md) και εκτελέσιμο τετράδιο [16-python-agent-framework.ipynb](./16-deploying-scalable-agents/code_samples/16-python-agent-framework.ipynb) που δημιουργεί έναν παραγωγικό πράκτορα υποστήριξης πελατών (εργαλεία, RAG, μνήμη, δρομολόγηση μοντέλου, προσωρινή αποθήκευση αποκρίσεων, ανθρώπινη έγκριση, πύλη αξιολόγησης, και εντοπισμό OpenTelemetry), με διαγράμματα ανάπτυξης/ανάπτυξης/εκτέλεσης Mermaid, έλεγχο γνώσεων, ανάθεση και πρόκληση.
- **Μάθημα 17 — Δημιουργία Τοπικών Πρακτόρων AI με Foundry Local και Qwen.** Νέο μάθημα [17-creating-local-ai-agents/README.md](./17-creating-local-ai-agents/README.md) και τετράδιο [17-local-agent-foundry-local.ipynb](./17-creating-local-ai-agents/code_samples/17-local-agent-foundry-local.ipynb) που δημιουργεί πλήρη βοηθό μηχανικού σε συσκευή (λειτουργίες Qwen μέσω Foundry Local, εργαλεία αρχείων σε sandbox, τοπικό RAG με Chroma, προαιρετικό τοπικό MCP), με διαγράμματα μόνο-τοπικού / τοπικού-RAG / κλήσης εργαλείων, έλεγχο γνώσεων, ανάθεση, και πρόκληση.
- **Ροή δοκιμής καπνού.** Νέο [AI Smoke Test](https://github.com/marketplace/actions/ai-smoke-test) workflow [.github/workflows/smoke-test.yml](../../.github/workflows/smoke-test.yml) καθώς και κατάλογοι ανά μάθημα υπό [tests/](./tests/README.md) για τους αναπτύξιμους πράκτορες στα Μαθήματα 01, 04, 05, και 16, με index README που αντιστοιχίζει κάθε κατάλογο στο μάθημά του και το όνομα πράκτορα. Το Μάθημα 16 αποκτά τμήμα "Επικύρωση Αναπτυγμένου Πράκτορα με Δοκιμές Καπνού". Τα Μαθήματα 01/04/05 προσθέτουν προαιρετική αναφορά δοκιμής καπνού.
- **Δεξιότητες μαθητών.** Νέες Δεξιότητες Πρακτόρων υπό `.agents/skills/`: [deploying-scalable-agents](./.agents/skills/deploying-scalable-agents/SKILL.md), [local-ai-agents](./.agents/skills/local-ai-agents/SKILL.md) (πακέτο οδηγιών Μαθημάτων 16 και 17), και [testing-course-samples](./.agents/skills/testing-course-samples/SKILL.md) (πώς να επικυρώνετε τα δείγματα τετραδίων έναντι μιας ζωντανής εγκατάστασης Microsoft Foundry / Azure OpenAI).
- **Εκτελεστής επικύρωσης τετραδίων.** Νέο [scripts/validate-notebooks.ps1](../../scripts/validate-notebooks.ps1) που εκτελεί κάθε τετράδιο Python χωρίς περιβάλλον χρήστη με `nbconvert` και τυπώνει μήτρα ΠΕΡΝΗΣΕ/ΑΠΟΤΥΧΙΑ (συμπεριλαμβανομένου του `results.json`). Ανιχνεύει αυτόματα τη ρίζα του αποθετηρίου και την Python, εξαιρεί μη-μαθησιακά τετράδια (`.venv`, `site-packages`, `translations`, πόροι προτύπου δεξιοτήτων) και τετράδια `.NET` από προεπιλογή, και υποστηρίζει `-Filter`, `-Timeout`, `-List`, `-IncludeDotnet`, και `-Python`.
- **Πλοήγηση μαθήματος.** Προστέθηκαν σύνδεσμοι Προηγούμενου/Επόμενου σε μαθήματα 11–15 (προηγουμένως απούσα) ώστε όλο το μάθημα να αλυσιδώνεται 00 → 18 και στις δύο κατευθύνσεις.
- **Νέες μικρογραφίες.** Μικρογραφίες για Μαθήματα 16 και 17, συν ανανεωμένη κοινωνική εικόνα αποθετηρίου [images/repo-thumbnailv3.png](./images/repo-thumbnailv3.png) (τώρα διαφημίζει τα δύο νέα μαθήματα και το URL `aka.ms/ai-agents-beginners`).
- **Εξαρτήσεις** ([requirements.txt](../../requirements.txt)): προστέθηκαν `foundry-local-sdk` και `chromadb` για το Μάθημα 17.

### Αλλαγές

- **Κύριο πίνακα μαθημάτων [README.md](./README.md)**: Τα Μαθήματα 16 και 17 τώρα συνδέονται με το περιεχόμενό τους (προηγουμένως "Coming Soon"). Η εικόνα αποθετηρίου ενημερώθηκε σε `repo-thumbnailv3.png`.
- **[STUDY_GUIDE.md](./STUDY_GUIDE.md)**: προστέθηκαν Μαθήματα 16 και 17 στον οδηγό μάθησης ανά μάθημα και στις διαδρομές μάθησης, καθώς και τμήμα "Επικύρωση Αναπτυγμένων Πρακτόρων με Δοκιμές Καπνού".
- **[AGENTS.md](./AGENTS.md)**: ενημερώθηκε ο αριθμός/περιγραφή μαθημάτων (00–18), προστέθηκε τμήμα επικύρωσης δοκιμών καπνού, και παραδείγματα ονοματοδοσίας δειγμάτων Μαθημάτων 16/17.
- **[18-securing-ai-agents/README.md](./18-securing-ai-agents/README.md)**: Το "Προηγούμενο Μάθημα" τώρα δείχνει στο Μάθημα 17 (ήταν Μάθημα 15), ολοκληρώνοντας την αλυσίδα.
- **Τυποποιημένες αναφορές μοντέλων σε μη αποσυρμένα μοντέλα.** Αντικαταστάθηκαν όλες οι αναφορές `gpt-4o` / `gpt-4o-mini` σε όλο το μάθημα (έγγραφα, `.env.example`, τετράδια και δείγματα Python/.NET) με το `gpt-4.1-mini` — το `gpt-4o` (όλες οι εκδόσεις) αποσύρεται το 2026. Το παράδειγμα δρομολόγησης μοντέλου του Μαθήματος 16 διατηρεί αντίθεση μικρού/μεγάλου με χρήση `gpt-4.1-mini` (μικρό) και `gpt-4.1` (μεγάλο). Τα τετράδια Python επιλέγουν τώρα το μοντέλο από μεταβλητές περιβάλλοντος (`AZURE_AI_MODEL_DEPLOYMENT_NAME` / `AZURE_OPENAI_DEPLOYMENT`) αντί να κάνουν hard-code σε όνομα μοντέλου.

### Σημειώσεις και γνωστοί περιορισμοί

- **Δεν εκτελέστηκαν έναντι ζωντανού Azure.** Τα τετράδια των νέων μαθημάτων είναι εκπαιδευτικά δείγματα· τρέξτε και επικυρώστε τα έναντι της δικής σας εγκατάστασης Microsoft Foundry / Foundry Local. Η ροή δοκιμής καπνού απαιτεί να αναπτύξετε τον πράκτορα του μαθήματος και να ρυθμίσετε μυστικά Azure OIDC (`AZURE_CLIENT_ID`, `AZURE_TENANT_ID`, `AZURE_SUBSCRIPTION_ID`) με το ρόλο **Azure AI User** στο εύρος έργου Foundry.
- **Το Μάθημα 17 είναι μόνο τοπικό.** Δεν διαθέτει endpoint Foundry Responses, οπότε η ενέργεια δοκιμής καπνού δεν ισχύει· επικυρώστε το τρέχοντας το τετράδιο στον υπολογιστή σας.

## [Κυκλοφόρησε] — 2026-07-06

Αυτή η έκδοση μετεγκαθιστά το μάθημα στο **Azure OpenAI Responses API**, τυποποιεί την ονοματοδοσία προϊόντων σε **Microsoft Foundry** και το **Microsoft Agent Framework (MAF)**, αποσύρει GitHub Models, ενημερώνει εκδόσεις SDK, και προσθέτει νέο περιεχόμενο για τοπικά μοντέλα και φιλοξενία άλλων πλαισίων σε Foundry.

### Προσθήκες

- **Δεξιότητα μετεγκατάστασης** — Εγκαταστάθηκε η Agent Skill [`azure-openai-to-responses`](./.agents/skills/azure-openai-to-responses/SKILL.md) (από [Azure-Samples/azure-openai-to-responses](https://github.com/Azure-Samples/azure-openai-to-responses)) υπό `.agents/skills/`, συμπεριλαμβανομένων των αναφορών της και του script σάρωσης.
- **Foundry Local (εκτέλεση μοντέλων στη συσκευή)** — Νέο τμήμα "Εναλλακτικός Πάροχος: Foundry Local" στο [00-course-setup/README.md](./00-course-setup/README.md) που καλύπτει εγκατάσταση (`winget` / `brew`), `foundry model run`, το `foundry-local-sdk`, και τη σύνδεση του `FoundryLocalManager` με το Microsoft Agent Framework μέσω `OpenAIChatClient`.
- **Φιλοξενία πρακτόρων LangChain / LangGraph στο Microsoft Foundry** — Νέο τμήμα στο [14-microsoft-agent-framework/README.md](./14-microsoft-agent-framework/README.md) μαζί με εκτελέσιμο δείγμα [14-langchain-hosted-agent.py](../../14-microsoft-agent-framework/code-samples/14-langchain-hosted-agent.py) που χρησιμοποιεί το `langchain-azure-ai[hosting]` και τον `ResponsesHostServer` (το πρωτόκολλο `/responses`), βασισμένο στο [Microsoft Learn](https://learn.microsoft.com/azure/foundry/how-to/develop/langchain-hosted-agents).
- **Microsoft Project Opal** — Νέο τμήμα "Πραγματικό Παράδειγμα: Microsoft Project Opal" στο [15-browser-use/README.md](./15-browser-use/README.md) που παρουσιάζει τον Opal ως πράκτορα επιχείρησης χρήσης υπολογιστή και τον συνδέει με έννοιες μαθήματος (άνθρωπος στον βρόχο, εμπιστοσύνη/ασφάλεια, σχεδιασμός, Δεξιότητες).
- **Δεύτερο δείγμα Python για το Μάθημα 02** — Προστέθηκε το [02-python-agent-framework-azure-openai.ipynb](./02-explore-agentic-frameworks/code_samples/02-python-agent-framework-azure-openai.ipynb) (βλέπε "Αλλαγές" — μετεγκαταστάθηκε από το προηγούμενο τετράδιο Semantic Kernel) και συνδέθηκε στο README του μαθήματος.
- Προστέθηκε τμήμα Μοντέλων και Παρόχων στο [STUDY_GUIDE.md](./STUDY_GUIDE.md).

### Αλλαγές

- **Chat Completions → Responses API (Python).** Τα δείγματα που καλούσαν απευθείας το μοντέλο μετεγκαταστάθηκαν από Chat Completions στο Responses API (`client.responses.create(input=..., store=False)`, `resp.output_text`), χρησιμοποιώντας τον πελάτη `OpenAI` έναντι του σταθερού endpoint Azure OpenAI `/openai/v1/` (χωρίς `api_version`). Τα δείγματα που επηρεάστηκαν περιλαμβάνουν:
  - [06-building-trustworthy-agents/code_samples/06-system-message-framework.ipynb](./06-building-trustworthy-agents/code_samples/06-system-message-framework.ipynb)
  - [06-building-trustworthy-agents/code_samples/06-human-in-the-loop.ipynb](./06-building-trustworthy-agents/code_samples/06-human-in-the-loop.ipynb)
  - [04-tool-use/README.md](./04-tool-use/README.md) — η πλήρης περιήγηση στην κλήση λειτουργιών (το σχήμα εργαλείου απλοποιήθηκε στη μορφή Responses, τα αποτελέσματα εργαλείων επιστρέφονται ως `function_call_output`, `max_output_tokens`, κλπ.).

- **GitHub Models → Azure OpenAI.** Τα GitHub Models έχουν αποσυρθεί (παύση **Ιούλιος 2026**) και δεν υποστηρίζουν το Responses API. Όλοι οι κώδικες GitHub Models μετατράπηκαν σε Azure OpenAI / Microsoft Foundry σε παραδείγματα Python και .NET:
  - Python: Τετράδια εργασίας μαθήματος 08 (`01`–`03`), μάθημα 14 (`14-handoff`, `14-human-loop`, `hotel_booking_workflow_sample.py`).
  - .NET: `01`–`04`, `07`, `08` `*-dotnet-agent-framework.cs` + συμπληρωματικά `.md` έγγραφα, και τα τετράδια εργασίας/`.md` dotNET μαθήματος 08 (`01`–`03`) πλέον χρησιμοποιούν `AzureOpenAIClient(...).GetOpenAIResponseClient(deployment).CreateAIAgent(...)` με `AzureCliCredential`.
- **Semantic Kernel → Microsoft Agent Framework.** Το προηγούμενο `02-semantic-kernel.ipynb` επαναγράφηκε για να χρησιμοποιεί το Microsoft Agent Framework με Azure OpenAI (Responses API) και μετονομάστηκε σε `02-python-agent-framework-azure-openai.ipynb`.
- **Τυποποιήθηκε σε `FoundryChatClient` + `as_agent`.** Ο κώδικας README και τετραδίων που αναφερόταν σε `AzureAIProjectAgentProvider` τυποποιήθηκε στον κανόνα που χρησιμοποιείται από το μάθημα 01 και τα δικά του δείγματα του πλαισίου: `FoundryChatClient(project_endpoint=..., model=..., credential=AzureCliCredential())` με `provider.as_agent(...)`. Ενημερώθηκε σε όλα τα README και τετράδια μαθημάτων 02–14 (π.χ., μνήμη μαθήματος 13, όλα τα τετράδια μαθήματος 14, `11-agentic-protocols/code_samples/github-mcp/app.py`).
- **Ονομασία προϊόντος.** Μετονομάστηκε σε όλο το αγγλικό περιεχόμενο:
  - "Azure AI Foundry" / "Azure AI Studio" → **Microsoft Foundry**
  - "Azure AI Agent Service" → **Microsoft Foundry Agent Service**
  - (Άθικτο: "Azure OpenAI", "Azure AI Search", "Azure AI Inference" και ονόματα μεταβλητών περιβάλλοντος.)
- **Εξαρτήσεις** ([requirements.txt](../../requirements.txt)):
  - Καθορισμένες εκδόσεις `agent-framework>=1.10.0`, `agent-framework-foundry>=1.10.0`, `agent-framework-openai>=1.10.0`.
  - Καθορισμένη έκδοση `openai>=1.108.1` (ελάχιστο για το Responses API).
  - Αφαιρέθηκε `azure-ai-inference` (χρησιμοποιούνταν μόνο στα μεταφερμένα δείγματα GitHub Models).
- **Διαμόρφωση περιβάλλοντος** ([.env.example](../../.env.example)): αφαιρέθηκαν οι μεταβλητές GitHub Models (`GITHUB_TOKEN`, `GITHUB_ENDPOINT`, `GITHUB_MODEL_ID`); προστέθηκαν `AZURE_OPENAI_ENDPOINT`, `AZURE_OPENAI_DEPLOYMENT`, και προαιρετικό `AZURE_OPENAI_API_KEY`; ενημερώθηκε η ονομασία σε Microsoft Foundry.
- **Τεκμηρίωση** — Ενημερώθηκαν [00-course-setup/README.md](./00-course-setup/README.md), [AGENTS.md](./AGENTS.md), [README.md](./README.md), και [STUDY_GUIDE.md](./STUDY_GUIDE.md) για τα παραπάνω (ρύθμιση μεταβλητών περιβάλλοντος, απόσπασμα επαλήθευσης, οδηγίες παρόχου, ονομασία).

### Αφαιρέσεις

- Βήματα εισαγωγής GitHub Models και μεταβλητές περιβάλλοντος από τα έγγραφα ρύθμισης (αντικαταστάθηκαν από Azure OpenAI / Microsoft Foundry).

### Ασφάλεια / Ιδιωτικότητα (καθαρισμός κοινοποίησης)

- Καθαρίστηκαν εκτελέσεις Jupyter notebook που διέρρευσαν πραγματικά **Azure subscription ID**, ονόματα resource-group / πόρων και Bing connection ID, καθώς και τοπικοί **δρόμοι αρχείων και ονόματα χρηστών προγραμματιστών** στα:
  - `08-multi-agent/code_samples/workflows-agent-framework/dotNET/04.dotnet-agent-framework-workflow-aifoundry-condition.ipynb`
  - `08-multi-agent/code_samples/workflows-agent-framework/python/04.python-agent-framework-workflow-aifoundry-condition.ipynb`
  - `15-browser-use/15-browser-user.ipynb`
- Επιβεβαιώθηκε ότι δεν απομένουν API keys, tokens, subscription IDs ή προσωπικοί δρόμοι μέσα στο παρακολουθούμενο αγγλικό περιεχόμενο (τα υπολειπόμενα αναφορές `GITHUB_TOKEN` είναι το token GitHub Actions στις ροές εργασίας και το GitHub MCP server PAT στο μάθημα 11 — και τα δύο νόμιμα και άσχετα με τα GitHub Models).

### Σημειώσεις και γνωστοί περιορισμοί

- **Δεν εκτελέστηκαν/μεταγλωττίστηκαν.** Πρόκειται για εκπαιδευτικά παραδείγματα ενημερωμένα για ορθότητα API/ονομασίας· δεν εκτελέστηκαν σε ζώντες πόρους Azure και τα δείγματα .NET δεν μεταγλωττίστηκαν σε αυτό το περιβάλλον. Επαληθεύστε στον δικό σας Microsoft Foundry / Azure OpenAI περιβάλλον ανάπτυξης.
- **Η ανάπτυξη μοντέλου πρέπει να υποστηρίζει το Responses API.** Χρησιμοποιήστε ανάπτυξη όπως `gpt-4.1-mini`, `gpt-4.1` ή μοντέλο `gpt-5.x`. Παλαιότερα μοντέλα υποστηρίζουν βασικές λειτουργίες Responses, αλλά όχι όλα τα χαρακτηριστικά.
- **Έκδοση agent-framework.** Τα δείγματα στοχεύουν στην τελευταία έκδοση MAF (`>=1.10.0`). Η τυπική κλήση δημιουργίας agent είναι `client.as_agent(...)`; τα APIs επαληθεύτηκαν με τα δημοσιευμένα έγγραφα και μια εγκατεστημένη έκδοση. Αν χρησιμοποιήσετε διαφορετική έκδοση, επιβεβαιώστε τη διαθεσιμότητα της μεθόδου (`as_agent` έναντι `create_agent`).
- **Το τετράδιο εργασίας μάθημα 08 notebook 04** διατηρεί σκόπιμα `AzureAIAgentClient` (από `agent-framework-azure-ai`) διότι χρησιμοποιεί εργαλεία Microsoft Foundry Agent Service (Bing grounding, code interpreter); βασίζεται ήδη σε Responses.
- **Προεπιλεγμένη ανάπτυξη .NET.** Δύο δείγματα dotNET για το μάθημα 08 παλιά είχαν σκληροκωδικοποιημένο συγκεκριμένο μοντέλο· πλέον χρησιμοποιούν προεπιλεγμένα το `AZURE_OPENAI_DEPLOYMENT` (`gpt-4.1-mini`). Αν παράδειγμα βασίζεται σε multimodal/vision input, ορίστε το `AZURE_OPENAI_DEPLOYMENT` σε κατάλληλο μοντέλο.
- **Foundry Local** προσφέρει OpenAI-συμβατό endpoint **Chat Completions** και προορίζεται για τοπική ανάπτυξη· χρησιμοποιήστε Azure OpenAI / Microsoft Foundry για το πλήρες σύνολο λειτουργιών Responses API.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Αποποίηση ευθυνών**:
Αυτό το έγγραφο έχει μεταφραστεί χρησιμοποιώντας την υπηρεσία μετάφρασης με τεχνητή νοημοσύνη [Co-op Translator](https://github.com/Azure/co-op-translator). Ενώ επιδιώκουμε την ακρίβεια, παρακαλούμε να έχετε υπόψη ότι οι αυτοματοποιημένες μεταφράσεις ενδέχεται να περιέχουν λάθη ή ανακρίβειες. Το πρωτότυπο έγγραφο στη μητρική του γλώσσα πρέπει να θεωρείται η αυθεντική πηγή. Για κρίσιμες πληροφορίες, συνιστάται επαγγελματική ανθρώπινη μετάφραση. Δεν φέρουμε ευθύνη για τυχόν παρεξηγήσεις ή λανθασμένες ερμηνείες που προκύπτουν από τη χρήση αυτής της μετάφρασης.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->