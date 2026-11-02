---
name: microsoft-docs
description: Αναζητήστε επίσημη τεκμηρίωση της Microsoft για να βρείτε έννοιες, εκπαιδευτικά
  προγράμματα και παραδείγματα κώδικα σε Azure, .NET, Agent Framework, Aspire, VS
  Code, GitHub και άλλα. Χρησιμοποιεί το Microsoft Learn MCP ως προεπιλογή, με Context7
  και Aspire MCP για περιεχόμενο που βρίσκεται εκτός του learn.microsoft.com.
---
# Έγγραφα Microsoft

Δεξιότητα έρευνας για το οικοσύστημα τεχνολογίας της Microsoft. Καλύπτει το learn.microsoft.com και τεκμηρίωση που βρίσκεται εκτός αυτού (VS Code, GitHub, Aspire, αποθετήρια Agent Framework).

---

## Προεπιλογή: Microsoft Learn MCP

Χρησιμοποιήστε αυτά τα εργαλεία για **όλα στο learn.microsoft.com** — Azure, .NET, M365, Power Platform, Agent Framework, Semantic Kernel, Windows και άλλα. Αυτό είναι το κύριο εργαλείο για τη συντριπτική πλειονότητα των ερωτημάτων τεκμηρίωσης της Microsoft.

| Εργαλείο | Σκοπός |
|------|---------|
| `microsoft_docs_search` | Αναζήτηση στο learn.microsoft.com — έννοιες, οδηγοί, σεμινάρια, διαμόρφωση |
| `microsoft_code_sample_search` | Βρείτε λειτουργικά αποσπάσματα κώδικα από τεκμηρίωση Learn. Δώστε `language` (`python`, `csharp`, κτλ.) για καλύτερα αποτελέσματα |
| `microsoft_docs_fetch` | Πάρε πλήρες περιεχόμενο σελίδας από συγκεκριμένο URL (όταν τα αποσπάσματα αναζήτησης δεν αρκούν) |

Χρησιμοποιήστε `microsoft_docs_fetch` μετά την αναζήτηση όταν χρειάζεστε πλήρη σεμινάρια, όλες τις επιλογές διαμόρφωσης ή όταν τα αποσπάσματα αναζήτησης κόβονται.

---

## Εξαιρέσεις: Πότε να Χρησιμοποιήσετε Άλλα Εργαλεία

Οι ακόλουθες κατηγορίες βρίσκονται **εκτός** του learn.microsoft.com. Χρησιμοποιήστε το καθορισμένο εργαλείο αντί αυτού.

### Aspire — Χρησιμοποιήστε Aspire MCP Server (προτιμώμενο) ή Context7

Η τεκμηρίωση Aspire βρίσκεται στο **aspire.dev**, όχι στο Learn. Το καλύτερο εργαλείο εξαρτάται από την έκδοση της Aspire CLI που έχετε:

**CLI 13.2+** (συνιστάται) — Ο διακομιστής Aspire MCP περιλαμβάνει ενσωματωμένα εργαλεία αναζήτησης τεκμηρίωσης:

| Εργαλείο MCP | Περιγραφή |
|----------|-------------|
| `list_docs` | Λίστα με όλη τη διαθέσιμη τεκμηρίωση από το aspire.dev |
| `search_docs` | Σταθμισμένη λεξιλογική αναζήτηση στο περιεχόμενο του aspire.dev |
| `get_doc` | Ανακτά συγκεκριμένο έγγραφο με βάση το slug |

Αυτά περιλαμβάνονται στην Aspire CLI 13.2 ([PR #14028](https://github.com/microsoft/aspire/pull/14028)). Για ενημέρωση: `aspire update --self --channel daily`.

**CLI 13.1** — Ο διακομιστής MCP παρέχει αναζήτηση ενσωμάτωσης (`list_integrations`, `get_integration_docs`) αλλά **όχι** αναζήτηση τεκμηρίωσης. Επιστρέψτε στη χρήση του Context7:

| Αναγνωριστικό Βιβλιοθήκης | Χρησιμοποιείται για |
|---|---|
| `/microsoft/aspire.dev` | Κύριο — οδηγοί, ενσωματώσεις, αναφορά CLI, ανάπτυξη |
| `/microsoft/aspire` | Πηγή χρόνου εκτέλεσης — εσωτερικά API, λεπτομέρειες υλοποίησης |
| `/communitytoolkit/aspire` | Κοινότητα ενσωματώσεις — Go, Java, Node.js, Ollama |

### VS Code — Χρησιμοποιήστε Context7

Η τεκμηρίωση του VS Code βρίσκεται στο **code.visualstudio.com**, όχι στο Learn.

| Αναγνωριστικό Βιβλιοθήκης | Χρησιμοποιείται για |
|---|---|
| `/websites/code_visualstudio` | Τεκμηρίωση χρήστη — ρυθμίσεις, λειτουργίες, αποσφαλμάτωση, απομακρυσμένη ανάπτυξη |
| `/websites/code_visualstudio_api` | API επεκτάσεων — webviews, TreeViews, εντολές, σημεία συμβολής |

### GitHub — Χρησιμοποιήστε Context7

Η τεκμηρίωση του GitHub βρίσκεται στα **docs.github.com** και **cli.github.com**.

| Αναγνωριστικό Βιβλιοθήκης | Χρησιμοποιείται για |
|---|---|
| `/websites/github_en` | Actions, API, αποθετήρια, ασφάλεια, διαχείριση, Copilot |
| `/websites/cli_github` | Εντολές και σημαίες GitHub CLI (`gh`) |

### Agent Framework — Χρησιμοποιήστε Learn MCP + Context7

Τα σεμινάρια Agent Framework βρίσκονται στο learn.microsoft.com (χρησιμοποιήστε `microsoft_docs_search`), αλλά το **αποθετήριο GitHub** διαθέτει λεπτομέρειες API που συχνά προηγούνται των δημοσιευμένων εγγράφων — ιδιαίτερα η αναφορά DevUI REST API, οι επιλογές CLI και η ενσωμάτωση .NET.

| Αναγνωριστικό Βιβλιοθήκης | Χρησιμοποιείται για |
|---|---|
| `/websites/learn_microsoft_en-us_agent-framework` | Σεμινάρια — οδηγοί DevUI, ιχνηλάτηση, ορχήστρωση ροής εργασίας |
| `/microsoft/agent-framework` | Λεπτομέρειες API — τελικά σημεία DevUI REST, σημαίες CLI, αυθεντικοποίηση, .NET `AddDevUI`/`MapDevUI` |

**Συμβουλή DevUI:** Ερωτήστε την πηγή του ιστότοπου Learn για οδηγούς χρήσης και μετά την πηγή του αποθετηρίου για ειδικές λεπτομέρειες API (σχήματα τελικών σημείων, διαμόρφωση proxy, διακριτικά αυθεντικοποίησης).

---

## Διαμόρφωση Context7

Για κάθε ερώτημα Context7, επιλύστε πρώτα το αναγνωριστικό βιβλιοθήκης (μία φορά ανά συνεδρία):

1. Καλέστε `mcp_context7_resolve-library-id` με το όνομα της τεχνολογίας
2. Καλέστε `mcp_context7_query-docs` με το επιστρεφόμενο αναγνωριστικό βιβλιοθήκης και ένα συγκεκριμένο ερώτημα

---

## Συγγραφή Αποτελεσματικών Ερωτημάτων

Να είστε συγκεκριμένοι — συμπεριλάβετε έκδοση, σκοπό και γλώσσα:

```
# ❌ Too broad
"Azure Functions"
"agent framework"

# ✅ Specific
"Azure Functions Python v2 programming model"
"Cosmos DB partition key design best practices"
"GitHub Actions workflow_dispatch inputs matrix strategy"
"Aspire AddUvicornApp Python FastAPI integration"
"DevUI serve agents tracing OpenTelemetry directory discovery"
"Agent Framework workflow conditional edges branching handoff"
```

Συμπεριλάβετε πλαίσιο:
- **Έκδοση** όταν είναι σχετικό (`.NET 8`, `Aspire 13`, `VS Code 1.96`)
- **Σκοπός εργασίας** (`quickstart`, `tutorial`, `overview`, `limits`, `API reference`)
- **Γλώσσα** για πολυγλωσσική τεκμηρίωση (`Python`, `TypeScript`, `C#`)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Αποποίηση ευθυνών**:
Αυτό το έγγραφο έχει μεταφραστεί χρησιμοποιώντας την υπηρεσία μετάφρασης με τεχνητή νοημοσύνη [Co-op Translator](https://github.com/Azure/co-op-translator). Ενώ επιδιώκουμε την ακρίβεια, παρακαλούμε να έχετε υπόψη ότι οι αυτοματοποιημένες μεταφράσεις ενδέχεται να περιέχουν λάθη ή ανακρίβειες. Το πρωτότυπο έγγραφο στη μητρική του γλώσσα πρέπει να θεωρείται η αυθεντική πηγή. Για κρίσιμες πληροφορίες, συνιστάται επαγγελματική ανθρώπινη μετάφραση. Δεν φέρουμε ευθύνη για τυχόν παρεξηγήσεις ή λανθασμένες ερμηνείες που προκύπτουν από τη χρήση αυτής της μετάφρασης.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->