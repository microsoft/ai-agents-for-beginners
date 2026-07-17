# Teste Smoke pentru Agenti

Acest dosar conține **cataloge de teste smoke** pentru agenții pe care îi construiești în curs.
Un test smoke este o verificare ieftină și rapidă că un **agent găzduit Microsoft Foundry
implementat** este accesibil, răspunde și respectă cele mai de bază așteptări ale promptului său.
Este o poartă inițială - nu un înlocuitor pentru întregul proces de evaluare
pe care îl înveți în [Lecția 10](../10-ai-agents-production/README.md) și
[Lecția 16](../16-deploying-scalable-agents/README.md).

Catalogele sunt utilizate de [AI Smoke Test](https://github.com/marketplace/actions/ai-smoke-test)
GitHub Action prin intermediul workflow-ului [`.github/workflows/smoke-test.yml`](../../../.github/workflows/smoke-test.yml).


## Cum să rulezi

1. **Deplasează agentul lecției** către Microsoft Foundry ca agent găzduit (vezi
   Lecția 16 pentru workflow-ul de implementare). Reține **numele agentului** și
   **endpoint-ul proiectului Foundry**.
2. Adaugă aceste secrete în repository (Setări → Secrete și variabile → Acțiuni):
   `AZURE_CLIENT_ID`, `AZURE_TENANT_ID`, `AZURE_SUBSCRIPTION_ID`. Identitatea federată
   are nevoie de rolul **Azure AI User** la **nivel de proiect Foundry**.
3. Din fila **Acțiuni**, rulează **Smoke-test hosted agents** și alege
   fișierul `tests_file` pentru lecție, apoi furnizează `agent_name` și
   `project_endpoint` corespunzătoare.

## Catalog → lecție → numele agentului

| Catalog | Lecție | Deplasează agentul ca |
|---------|--------|---------------------|
| [`lesson-01-smoke-tests.json`](../../../tests/lesson-01-smoke-tests.json) | [01 – Intro la Agenți AI](../01-intro-to-ai-agents/README.md) | `TravelAgent` |
| [`lesson-04-smoke-tests.json`](../../../tests/lesson-04-smoke-tests.json) | [04 – Utilizarea Instrumentelor](../04-tool-use/README.md) | `TravelToolAgent` |
| [`lesson-05-smoke-tests.json`](../../../tests/lesson-05-smoke-tests.json) | [05 – Agentic RAG](../05-agentic-rag/README.md) | `TravelRAGAgent` |
| [`lesson-16-smoke-tests.json`](../../../tests/lesson-16-smoke-tests.json) | [16 – Implementarea Agenților Scalabili](../16-deploying-scalable-agents/README.md) | `ContosoSupportAgent` |

## Ce lecții au teste smoke?

Testele smoke se aplică lecțiilor în care **deplasezi un agent** ale cărui răspunsuri text pot
fi verificate față de conținut cunoscut. Lecțiile conceptuale, care rulează numai local,
sau care produc un output creativ nedeterminist sunt excluse intenționat:

- **Lecția 17 (Crearea Agenților AI Locali)** rulează integral pe statia ta de lucru cu
  Foundry Local și **nu** expune un endpoint Foundry Responses, deci această
  acțiune nu se aplică. Validează prin rularea notebook-ului local.
- Lecțiile despre modele de design și teorie (02, 03, 06, 07, 09, 12) nu furnizează niciun
  agent de implementat pentru testare smoke.

## Schema catalogului (referință rapidă)

Fiecare catalog este un document JSON cu un array principal `tests`. Fiecare intrare face POST
cu un prompt și verifică răspunsul:

| Câmp | Semnificație |
|-------|------------|
| `id` | Identificator unic al pasului, tipărit în jurnal. |
| `description` | Scop lizibil pentru om. |
| `prompt` | Mesajul trimis agentului. |
| `assertions.status` | Status HTTP așteptat (implicit 200). |
| `assertions.contains_any` | Trece dacă răspunsul conține oricare dintre aceste subșiruri. |
| `assertions.contains_all` | Trece dacă răspunsul conține fiecare subșir. |
| `assertions.contains_none` | Trece dacă răspunsul nu conține niciunul dintre aceste subșiruri. |
| `save_response_id_as` | Salvează id-ul răspunsului pentru un pas ulterior cu mai multe interacțiuni. |
| `use_previous_response_id` | Trimite acest pas legat de un id de răspuns salvat anterior. |

Verificările sunt căutări de subșiruri insensibile la majuscule. Vezi
[documentația acțiunii](https://github.com/marketplace/actions/ai-smoke-test) pentru
schema completă, inclusiv resursele de conversație gestionate de Foundry.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Declinare a responsabilității**:
Acest document a fost tradus folosind serviciul de traducere AI [Co-op Translator](https://github.com/Azure/co-op-translator). În timp ce ne străduim pentru acuratețe, vă rugăm să rețineți că traducerile automate pot conține erori sau inexactități. Documentul original în limba sa nativă trebuie considerat sursa autorizată. Pentru informații critice, se recomandă traducerea profesională realizată de un om. Nu ne asumăm responsabilitatea pentru eventualele neînțelegeri sau interpretări greșite care decurg din utilizarea acestei traduceri.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->