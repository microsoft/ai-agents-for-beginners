# Test Smoke degli Agenti

Questa cartella contiene **cataloghi di test smoke** per gli agenti che costruisci durante il corso.
Un test smoke è un controllo economico e rapido per verificare che un **agente Microsoft Foundry ospitato
e distribuito** sia raggiungibile, risponda e rispetti le sue aspettative di prompt più basilari.
È una prima barriera — non un sostituto del processo completo di valutazione
che impari in [Lezione 10](../10-ai-agents-production/README.md) e
[Lezione 16](../16-deploying-scalable-agents/README.md).

I cataloghi sono utilizzati dall’azione GitHub [AI Smoke Test](https://github.com/marketplace/actions/ai-smoke-test)
tramite il workflow [`.github/workflows/smoke-test.yml`](../../../.github/workflows/smoke-test.yml).


## Come eseguire

1. **Distribuisci l’agente della lezione** su Microsoft Foundry come agente ospitato (vedi
   Lezione 16 per il flusso di lavoro di distribuzione). Prendi nota del **nome dell’agente** e del
   **endpoint del progetto Foundry**.
2. Aggiungi questi segreti al repository (Impostazioni → Segreti e variabili → Azioni):
   `AZURE_CLIENT_ID`, `AZURE_TENANT_ID`, `AZURE_SUBSCRIPTION_ID`. L’identità federata necessita del ruolo
   **Azure AI User** nell’ambito **progetto Foundry**.
3. Dalla scheda **Azioni**, esegui **Smoke-test hosted agents** e scegli il
   `tests_file` per la lezione, quindi inserisci `agent_name` e
   `project_endpoint` corrispondenti.

## Catalogo → lezione → nome dell’agente

| Catalogo | Lezione | Distribuisci agente come |
|---------|--------|-------------------------|
| [`lesson-01-smoke-tests.json`](../../../tests/lesson-01-smoke-tests.json) | [01 – Introduzione agli Agenti AI](../01-intro-to-ai-agents/README.md) | `TravelAgent` |
| [`lesson-04-smoke-tests.json`](../../../tests/lesson-04-smoke-tests.json) | [04 – Uso degli Strumenti](../04-tool-use/README.md) | `TravelToolAgent` |
| [`lesson-05-smoke-tests.json`](../../../tests/lesson-05-smoke-tests.json) | [05 – RAG Agentico](../05-agentic-rag/README.md) | `TravelRAGAgent` |
| [`lesson-16-smoke-tests.json`](../../../tests/lesson-16-smoke-tests.json) | [16 – Distribuzione di Agenti Scalabili](../16-deploying-scalable-agents/README.md) | `ContosoSupportAgent` |

## Quali lezioni hanno test smoke?

I test smoke si applicano alle lezioni in cui **distribuisci un agente** le cui risposte testuali possono
essere confrontate con contenuti noti. Le lezioni che sono concettuali, eseguite solo localmente,
o producono output creativo non deterministico sono escluse intenzionalmente:

- **Lezione 17 (Creazione di Agenti AI Locali)** viene eseguita interamente sul tuo workstation con
  Foundry Local e **non** espone un endpoint Foundry Responses, quindi questa
  azione non si applica. Validala eseguendo il notebook localmente.
- Le lezioni su pattern di design e teoria (02, 03, 06, 07, 09, 12) non rilasciano alcun
  agente distribuibile per il test smoke.

## Schema del catalogo (riferimento rapido)

Ogni catalogo è un documento JSON con un array di livello superiore `tests`. Ogni voce invia
un prompt e verifica la risposta:

| Campo | Significato |
|-------|------------|
| `id` | Identificatore univoco del passaggio stampato nel log. |
| `description` | Scopo leggibile dall’umano. |
| `prompt` | Il messaggio inviato all’agente. |
| `assertions.status` | Stato HTTP atteso (default 200). |
| `assertions.contains_any` | Passa se la risposta contiene una qualsiasi di queste sottostringhe. |
| `assertions.contains_all` | Passa se la risposta contiene tutte le sottostringhe. |
| `assertions.contains_none` | Passa se la risposta non contiene nessuna di queste sottostringhe. |
| `save_response_id_as` | Memorizza l’id della risposta per un passaggio multi-turno successivo. |
| `use_previous_response_id` | Invia questo turno concatenato a un id di risposta salvato. |

Le asserzioni sono controlli di sottostringhe case-insensitive. Consulta la
[documentazione dell’azione](https://github.com/marketplace/actions/ai-smoke-test) per
lo schema completo, incluse le risorse di conversazione gestite da Foundry.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:
Questo documento è stato tradotto utilizzando il servizio di traduzione AI [Co-op Translator](https://github.com/Azure/co-op-translator). Sebbene ci impegniamo per garantire la precisione, si prega di notare che le traduzioni automatizzate possono contenere errori o imprecisioni. Il documento originale nella sua lingua nativa deve essere considerato la fonte autorevole. Per informazioni critiche, si raccomanda una traduzione professionale effettuata da un essere umano. Non siamo responsabili per eventuali malintesi o interpretazioni errate derivanti dall’uso di questa traduzione.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->