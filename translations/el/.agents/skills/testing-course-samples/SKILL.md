---
name: testing-course-samples
---
# Δοκιμή των Δειγμάτων Μαθήματος

Επαληθεύστε ότι τα τετράδια μαθημάτων και τα δείγματα κώδικα εκτελούνται σε ένα ζωντανό
περιβάλλον Microsoft Foundry / Azure OpenAI. Το αποθετήριο παρέχει έναν εκτελεστή στο
[`scripts/validate-notebooks.ps1`](../../../../../scripts/validate-notebooks.ps1) που
εκτελεί κάθε τετράδιο Python χωρίς περιβάλλον χρήστη και εμφανίζει έναν πίνακα ΔΙΕΛΕΙΨΗ/ΑΠΟΤΥΧΙΑ.

## Πότε να χρησιμοποιήσετε
- "Επαληθεύστε όλα τα τετράδια / δείγματα έναντι της συνδρομής Azure."
- "Κάντε μια γρήγορη δοκιμή του μαθήματος μετά την αναβάθμιση πακέτων ή αλλαγή μοντέλων."
- "Ποια μαθήματα περνούν / αποτυγχάνουν ζωντανά;"

Μην χρησιμοποιείτε αυτό για το AI Smoke Test GitHub Action (που επαληθεύει *αναπτυγμένους*
φιλοξενούμενους πράκτορες — δείτε το [`tests/README.md`](../../../tests/README.md)). Αυτή η δεξιότητα
εκτελεί τα τετράδια τοπικά.

## Προαπαιτούμενα (ελέγξτε πρώτα)
1. **Python 3.12+** με εξαρτήσεις μαθήματος: `python -m pip install -r requirements.txt`
   συν τον εκτελεστή: `python -m pip install nbconvert ipykernel`.
2. **`.env` στη ρίζα του αποθετηρίου** (αντιγράψτε από [`.env.example`](../../../../../.env.example)) με τουλάχιστον:
   - `AZURE_AI_PROJECT_ENDPOINT` — τελικό σημείο έργου Foundry
     (`https://<account>.services.ai.azure.com/api/projects/<project>`)
   - `AZURE_AI_MODEL_DEPLOYMENT_NAME` — μια μη αποσυρθείσα ανάπτυξη (π.χ. `gpt-4.1-mini`)
   - `AZURE_OPENAI_ENDPOINT` (`https://<account>.openai.azure.com`) και `AZURE_OPENAI_DEPLOYMENT`
     για μαθήματα που καλούν απευθείας Azure OpenAI (Μάθημα 06, 02-azure-openai, 14 handoff/human-loop).
3. **Ολοκληρωμένη `az login`** — τα δείγματα πιστοποιούνται με `AzureCliCredential` (Entra ID, χωρίς κλειδί).
4. Επαληθεύστε ότι η ανάπτυξη μοντέλου υπάρχει:
   `az cognitiveservices account deployment list -g <rg> -n <account> -o table`.

## Εκτέλεση της επαλήθευσης
```powershell
# Όλα τα Python notebooks (παραλείπει .NET, .venv, site-packages, μεταφράσεις, περιουσιακά στοιχεία δεξιοτήτων)
pwsh scripts/validate-notebooks.ps1

# Ένα μόνο μάθημα, με μεγαλύτερο χρονικό όριο ανά κελί
pwsh scripts/validate-notebooks.ps1 -Filter '08-*' -Timeout 600

# Απλώς απαριθμήστε τι θα εκτελούνταν (χωρίς εκτέλεση)
pwsh scripts/validate-notebooks.ps1 -List

# Ρητός διερμηνέας (αν το `python` δεν είναι στο PATH, π.χ. ψευδώνυμο του Windows Store)
pwsh scripts/validate-notebooks.ps1 -Python "C:/path/to/python.exe"
```
Το σενάριο γράφει εκτελεσμένα αντίγραφα, καταγραφές ανά τετράδιο και `results.json` στον
φάκελο `$env:TEMP\aiab-nbval` και τερματίζει με τον αριθμό των αποτυχιών.

## Ερμηνεία αποτελεσμάτων
- `PASS` — το τετράδιο εκτελέστηκε από την αρχή ως το τέλος χωρίς σφάλματα κελιών.
- `FAIL` — εμφανίζεται η πρώτη γραμμή `*Error` / `*Exception`; ανοίξτε το αντίστοιχο
  αρχείο `log_*.txt` στον φάκελο εξόδου για την πλήρη ιχνηλάτηση σφαλμάτων.
- Η αποτυχία ενός μόνο τετραδίου περιορίζεται από το `-Timeout` (ανά κελί), ώστε ένα κολλημένο
  κελί "ανθρώπου-στο-βρόχο" να εμφανίζεται ως `StdinNotImplementedError` αντί να κολλάει.

## Μαθήματα που χρειάζονται επιπλέον πόρους (αναμένεται να αποτύχουν χωρίς αυτούς)
| Μάθημα | Επιπλέον απαίτηση |
|--------|-------------------|
| 05 Agentic RAG | Azure AI Search (`AZURE_SEARCH_SERVICE_ENDPOINT`, κλειδί) — διαθέτει εναλλακτική μνήμη σε RAM |
| 11 MCP / GitHub | GitHub MCP server + PAT |
| 13 memory (cognee) | `cognee` ρυθμισμένο με πάροχο μοντέλου |
| 15 browser-use | Εγκατεστημένοι browsers Playwright (`playwright install`) + `AZURE_OPENAI_CHAT_DEPLOYMENT_NAME` |
| 17 local agent | Foundry Local runtime + ένα κατεβασμένο μοντέλο Qwen (σε συσκευή, χωρίς cloud) |
| `*-dotnet-*` τετράδια | Πυρήνας .NET Interactive (εξαιρείται από προεπιλογή· χρησιμοποιήστε `-IncludeDotnet`) |

## Αναφορά πίσω
Περίληψη ως πίνακα ΔΙΕΛΕΙΨΗ/ΑΠΟΤΥΧΙΑ ομαδοποιημένο κατά μάθημα. Διαχωρίστε τις γνήσιες υποβαθμίσεις
(σφάλματα κώδικα/διαμόρφωσης προς διόρθωση) από τις ελλείψεις στο περιβάλλον (έλλειψη Search/Foundry Local/PAT),
και αναφέρετε το αποτυχημένο αρχείο `log_*.txt` για κάθε πραγματική αποτυχία.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Αποποίηση ευθυνών**:
Αυτό το έγγραφο έχει μεταφραστεί χρησιμοποιώντας την υπηρεσία μετάφρασης με τεχνητή νοημοσύνη [Co-op Translator](https://github.com/Azure/co-op-translator). Ενώ επιδιώκουμε την ακρίβεια, παρακαλούμε να έχετε υπόψη ότι οι αυτοματοποιημένες μεταφράσεις ενδέχεται να περιέχουν λάθη ή ανακρίβειες. Το πρωτότυπο έγγραφο στη μητρική του γλώσσα πρέπει να θεωρείται η αυθεντική πηγή. Για κρίσιμες πληροφορίες, συνιστάται επαγγελματική ανθρώπινη μετάφραση. Δεν φέρουμε ευθύνη για τυχόν παρεξηγήσεις ή λανθασμένες ερμηνείες που προκύπτουν από τη χρήση αυτής της μετάφρασης.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->