# Agenti AI in Produzione: Osservabilità e Valutazione

[![Agenti AI in Produzione](../../../translated_images/it/lesson-10-thumbnail.2b79a30773db093e.webp)](https://youtu.be/l4TP6IyJxmQ?si=reGOyeqjxFevyDq9)

Man mano che gli agenti AI passano da prototipi sperimentali ad applicazioni nel mondo reale, diventa importante la capacità di comprendere il loro comportamento, monitorare le loro prestazioni e valutare sistematicamente i loro output.

## Obiettivi di Apprendimento

Dopo aver completato questa lezione, saprai/avrai compreso:
- Concetti fondamentali di osservabilità e valutazione degli agenti
- Tecniche per migliorare le prestazioni, i costi e l'efficacia degli agenti
- Cosa e come valutare i tuoi agenti AI in modo sistematico
- Come controllare i costi quando distribuisci agenti AI in produzione
- Come instradare/strumentare agenti costruiti con Microsoft Agent Framework

L'obiettivo è fornirti le conoscenze per trasformare i tuoi agenti "scatola nera" in sistemi trasparenti, gestibili e affidabili.

_**Nota:** È importante distribuire agenti AI che siano sicuri e affidabili. Dai un'occhiata anche alla lezione [Building Trustworthy AI Agents](./06-building-trustworthy-agents/README.md)._

## Tracce e Span

Gli strumenti di osservabilità come [Langfuse](https://langfuse.com/) o [Microsoft Foundry](https://learn.microsoft.com/en-us/azure/ai-foundry/what-is-azure-ai-foundry) di solito rappresentano le esecuzioni degli agenti come tracce e span.

- **Trace** rappresenta un task completo dell'agente dall'inizio alla fine (come gestire una richiesta utente).
- **Spans** sono passaggi individuali all'interno della trace (come chiamare un modello di linguaggio o recuperare dati).

![Albero delle tracce in Langfuse](https://langfuse.com/images/cookbook/example-autogen-evaluation/trace-tree.png)
<!-- Image URL retained for illustration purposes -->

Senza osservabilità, un agente AI può sembrare una "scatola nera" - il suo stato interno e il suo processo decisionale sono opachi, rendendo difficile diagnosticare problemi o ottimizzare le prestazioni. Con l'osservabilità, gli agenti diventano "scatole di vetro", offrendo trasparenza fondamentale per costruire fiducia e garantire che funzionino come previsto. 

## Perché l'Osservabilità Conta negli Ambienti di Produzione

La transizione degli agenti AI in ambienti di produzione introduce un nuovo insieme di sfide e requisiti. L'osservabilità non è più un "bel-to-have" ma una capacità critica:

*   **Debugging e Analisi delle Cause Radice**: Quando un agente fallisce o produce un output inatteso, gli strumenti di osservabilità forniscono le tracce necessarie per individuare la fonte dell'errore. Questo è particolarmente importante in agenti complessi che possono coinvolgere molteplici chiamate LLM, interazioni con strumenti e logica condizionale.
*   **Gestione della Latency e dei Costi**: Gli agenti AI spesso si basano su LLM e altre API esterne che vengono fatturate per token o per chiamata. L'osservabilità permette di tracciare con precisione queste chiamate, aiutando a identificare operazioni eccessivamente lente o costose. Questo consente ai team di ottimizzare i prompt, selezionare modelli più efficienti o riprogettare i flussi di lavoro per gestire i costi operativi e garantire una buona esperienza utente.
*   **Fiducia, Sicurezza e Conformità**: In molte applicazioni è importante garantire che gli agenti si comportino in modo sicuro ed etico. L'osservabilità fornisce una traccia di audit delle azioni e delle decisioni dell'agente. Questo può essere utilizzato per rilevare e mitigare problemi come prompt injection, la generazione di contenuti dannosi o la gestione impropria di informazioni personali identificabili (PII). Ad esempio, puoi esaminare le tracce per capire perché un agente ha fornito una certa risposta o ha utilizzato uno strumento specifico.
*   **Cicli di Miglioramento Continuo**: I dati di osservabilità sono la base di un processo di sviluppo iterativo. Monitorando le prestazioni degli agenti nel mondo reale, i team possono identificare aree di miglioramento, raccogliere dati per il fine-tuning dei modelli e validare l'impatto delle modifiche. Questo crea un loop di feedback in cui le intuizioni di produzione dall'evalutazione online informano la sperimentazione offline e il perfezionamento, portando a prestazioni dell'agente progressivamente migliori.

## Metriche Chiave da Monitorare

Per monitorare e comprendere il comportamento dell'agente, è necessario tracciare una gamma di metriche e segnali. Sebbene le metriche specifiche possano variare in base allo scopo dell'agente, alcune sono universalmente importanti.

Ecco alcune delle metriche più comuni che gli strumenti di osservabilità monitorano:

**Latency:** Quanto velocemente risponde l'agente? Tempi di attesa lunghi influiscono negativamente sull'esperienza utente. Dovresti misurare la latency per i task e per i singoli passaggi tracciando le esecuzioni dell'agente. Ad esempio, un agente che impiega 20 secondi per tutte le chiamate al modello potrebbe essere accelerato usando un modello più veloce o eseguendo le chiamate al modello in parallelo.

**Costi:** Qual è la spesa per esecuzione dell'agente? Gli agenti AI si basano su chiamate LLM fatturate per token o su API esterne. L'uso frequente di strumenti o molteplici prompt può aumentare rapidamente i costi. Ad esempio, se un agente chiama un LLM cinque volte per un miglioramento marginale della qualità, devi valutare se il costo è giustificato o se puoi ridurre il numero di chiamate o usare un modello più economico. Il monitoraggio in tempo reale può anche aiutare a identificare picchi inaspettati (es. bug che causano loop eccessivi di API).

**Errori di Richiesta:** Quante richieste ha fallito l'agente? Questo può includere errori API o chiamate a strumenti fallite. Per rendere il tuo agente più robusto in produzione, puoi impostare fallback o ritentativi. Esempio: se il provider LLM A è down, passi al provider LLM B come backup.

**Feedback Utente:** Implementare valutazioni dirette degli utenti fornisce preziose informazioni. Questo può includere valutazioni esplicite (👍pollice su/👎pollice giù, ⭐1-5 stelle) o commenti testuali. Feedback negativi costanti dovrebbero allertarti in quanto segnale che l'agente non sta funzionando come previsto.

**Feedback Utente Implicito:** I comportamenti degli utenti forniscono feedback indiretti anche senza valutazioni esplicite. Questo può includere riformulazioni immediate della domanda, query ripetute o il clic su un pulsante di retry. Esempio: se vedi che gli utenti chiedono ripetutamente la stessa domanda, è un segnale che l'agente non sta funzionando come previsto.

**Accuratezza:** Quanto frequentemente l'agente produce output corretti o desiderabili? Le definizioni di accuratezza variano (es. correttezza nella risoluzione di problemi, accuratezza nel recupero delle informazioni, soddisfazione dell'utente). Il primo passo è definire cosa significa successo per il tuo agente. Puoi tracciare l'accuratezza tramite controlli automatizzati, punteggi di valutazione o etichette di completamento del task. Ad esempio, contrassegnando le tracce come "succeeded" o "failed". 

**Metriche di Valutazione Automatica:** Puoi anche impostare valutazioni automatiche. Per esempio, puoi usare un LLM per valutare l'output dell'agente, ad es. se è utile, accurato o meno. Esistono anche diverse librerie open source che ti aiutano a valutare differenti aspetti dell'agente, es. [RAGAS](https://docs.ragas.io/) per agenti RAG o [LLM Guard](https://llm-guard.com/) per rilevare linguaggio dannoso o prompt injection. 

Nella pratica, una combinazione di queste metriche dà la migliore copertura dello stato di salute di un agente AI. Nel [notebook di esempio](./code_samples/10-expense_claim-demo.ipynb) di questo capitolo, mostreremo come queste metriche appaiono in esempi reali ma prima, impareremo come appare tipicamente un workflow di valutazione.

## Strumentare il tuo Agente

Per raccogliere dati di tracing, dovrai strumentare il tuo codice. L'obiettivo è strumentare il codice dell'agente per emettere tracce e metriche che possano essere catturate, elaborate e visualizzate da una piattaforma di osservabilità.

**OpenTelemetry (OTel):** [OpenTelemetry](https://opentelemetry.io/) è emerso come uno standard di settore per l'osservabilità degli LLM. Fornisce un insieme di API, SDK e strumenti per generare, raccogliere ed esportare dati di telemetry. 

Esistono molte librerie di strumentazione che avvolgono i framework di agenti esistenti e semplificano l'esportazione degli span OpenTelemetry verso uno strumento di osservabilità. Microsoft Agent Framework si integra nativamente con OpenTelemetry. Di seguito un esempio su come strumentare un agente MAF:

```python
from agent_framework.observability import get_tracer, get_meter

tracer = get_tracer()
meter = get_meter()

with tracer.start_as_current_span("agent_run"):
    # L'esecuzione dell'agente viene tracciata automaticamente
    pass
```

Il [notebook di esempio](./code_samples/10-expense_claim-demo.ipynb) in questo capitolo dimostrerà come strumentare il tuo agente MAF.

**Creazione Manuale di Span:** Sebbene le librerie di strumentazione forniscano una buona base, ci sono spesso casi in cui sono necessarie informazioni più dettagliate o personalizzate. Puoi creare manualmente gli span per aggiungere logica applicativa personalizzata. Ancora più importante, possono arricchire span creati automaticamente o manualmente con attributi personalizzati (noti anche come tag o metadata). Questi attributi possono includere dati specifici di business, calcoli intermedi o qualsiasi contesto che possa essere utile per il debugging o l'analisi, come `user_id`, `session_id`, o `model_version`.

Esempio di creazione manuale di tracce e span con il [Langfuse Python SDK](https://langfuse.com/docs/sdk/python/sdk-v3): 

```python
from langfuse import get_client
 
langfuse = get_client()
 
span = langfuse.start_span(name="my-span")
 
span.end()
```

## Valutazione dell'Agente

L'osservabilità ci fornisce metriche, ma la valutazione è il processo di analisi di quei dati (e di esecuzione di test) per determinare quanto bene un agente AI sta performando e come può essere migliorato. In altre parole, una volta che hai quelle tracce e metriche, come le usi per giudicare l'agente e prendere decisioni?

La valutazione regolare è importante perché gli agenti AI sono spesso non-deterministici e possono evolversi (tramite aggiornamenti o deriva del comportamento del modello) – senza valutazione, non sapresti se il tuo "agente intelligente" sta effettivamente svolgendo bene il suo lavoro o se ha avuto regressioni.

Esistono due categorie di valutazioni per gli agenti AI: **valutazione online** e **valutazione offline**. Entrambe sono preziose e si completano a vicenda. Di solito iniziamo con la valutazione offline, poiché questo è il passo minimo necessario prima di distribuire qualsiasi agente.

### Valutazione Offline

![Elementi del dataset in Langfuse](https://langfuse.com/images/cookbook/example-autogen-evaluation/example-dataset.png)

Questo comporta la valutazione dell'agente in un ambiente controllato, tipicamente utilizzando dataset di test, non query utente live. Usi dataset curati dove sai qual è l'output atteso o il comportamento corretto, e poi esegui il tuo agente su di essi.

Ad esempio, se hai costruito un agente per problemi matematici, potresti avere un [dataset di test](https://huggingface.co/datasets/gsm8k) di 100 problemi con risposte conosciute. La valutazione offline viene spesso eseguita durante lo sviluppo (e può far parte delle pipeline CI/CD) per verificare miglioramenti o proteggere contro regressioni. Il vantaggio è che è **ripetibile e puoi ottenere metriche di accuratezza chiare visto che hai la verità di riferimento**. Potresti anche simulare query utente e misurare le risposte dell'agente rispetto a risposte ideali o usare metriche automatiche come descritto sopra.

La sfida principale della valutazione offline è garantire che il tuo dataset di test sia completo e rimanga rilevante – l'agente potrebbe andare bene su un set di test fisso ma incontrare query molto diverse in produzione. Pertanto, dovresti mantenere i set di test aggiornati con nuovi casi limite ed esempi che riflettano scenari del mondo reale​. Una combinazione di piccoli "smoke test" e set di valutazione più ampi è utile: set piccoli per controlli rapidi e set più grandi per metriche di performance più ampie​.

### Valutazione Online 

![Panoramica delle metriche di osservabilità](https://langfuse.com/images/cookbook/example-autogen-evaluation/dashboard.png)

Questo si riferisce alla valutazione dell'agente in un ambiente live e reale, cioè durante l'uso effettivo in produzione. La valutazione online comporta il monitoraggio delle prestazioni dell'agente sulle interazioni reali degli utenti e l'analisi continua dei risultati.

Per esempio, potresti tracciare tassi di successo, punteggi di soddisfazione degli utenti o altre metriche sul traffico live. Il vantaggio della valutazione online è che **cattura cose che potresti non prevedere in un ambiente di laboratorio** – puoi osservare la deriva del modello nel tempo (se l'efficacia dell'agente diminuisce con il cambiare dei pattern di input) e intercettare query o situazioni inaspettate che non erano presenti nei tuoi dati di test​. Fornisce un quadro reale di come l'agente si comporta sul campo.

La valutazione online spesso comporta la raccolta di feedback implicito ed esplicito degli utenti, come discusso, e possibilmente l'esecuzione di test shadow o A/B test (dove una nuova versione dell'agente viene eseguita in parallelo per confrontarla con la vecchia). La sfida è che può essere complicato ottenere etichette o punteggi affidabili per le interazioni live – potresti fare affidamento sul feedback degli utenti o su metriche downstream (ad es. l'utente ha cliccato il risultato).

### Combinare i due

Le valutazioni online e offline non sono mutualmente esclusive; si completano molto bene. Le intuizioni dal monitoraggio online (ad es. nuovi tipi di query utente in cui l'agente performa male) possono essere usate per aumentare e migliorare i dataset di test offline. Viceversa, agenti che ottengono buoni risultati nei test offline possono essere poi distribuiti con maggiore fiducia e monitorati online.

In effetti, molti team adottano un ciclo:

_valutare offline -> distribuire -> monitorare online -> raccogliere nuovi casi di errore -> aggiungere al dataset offline -> perfezionare l'agente -> ripetere_.

## Problemi Comuni

Man mano che distribuisci agenti AI in produzione, potresti incontrare varie sfide. Ecco alcuni problemi comuni e le loro potenziali soluzioni:

| **Problema**    | **Soluzione possibile**   |
| ------------- | ------------------ |
| Agente AI non esegue i compiti in modo coerente | - Raffina il prompt fornito all'Agente AI; sii chiaro sugli obiettivi.<br>- Identifica dove dividere i compiti in sotto-task e gestirli con più agenti può aiutare. |
| L'agente AI entra in loop continui  | - Assicurati di avere termini e condizioni di terminazione chiari in modo che l'Agente sappia quando fermare il processo.<br>- Per compiti complessi che richiedono ragionamento e pianificazione, usa un modello più grande specializzato per compiti di ragionamento. |
| Le chiamate agli strumenti dell'agente AI non funzionano correttamente   | - Testa e valida l'output dello strumento al di fuori del sistema agente.<br>- Raffina i parametri definiti, i prompt e la denominazione degli strumenti.  |
| Il sistema multi-agente non funziona in modo coerente | - Raffina i prompt forniti a ciascun agente per assicurarti che siano specifici e distinti l'uno dall'altro.<br>- Costruisci un sistema gerarchico usando un agente "routing" o controller per determinare quale agente è quello corretto. |

Molti di questi problemi possono essere identificati più efficacemente con l'osservabilità in atto. Le tracce e le metriche di cui abbiamo parlato aiutano a individuare esattamente dove nel workflow dell'agente si verificano i problemi, rendendo il debugging e l'ottimizzazione molto più efficienti.

## Gestione dei costi
Ecco alcune strategie per gestire i costi di distribuzione degli agenti AI in produzione:

**Using Smaller Models:** I Small Language Models (SLMs) possono ottenere buone prestazioni in alcuni casi d'uso agentici e ridurranno significativamente i costi. Come accennato in precedenza, costruire un sistema di valutazione per determinare e confrontare le prestazioni rispetto ai modelli più grandi è il modo migliore per capire quanto bene un SLM si comporterà nel tuo caso d'uso. Prendi in considerazione l'uso di SLMs per attività più semplici come la classificazione delle intenzioni o l'estrazione di parametri, riservando i modelli più grandi per il ragionamento complesso.

**Using a Router Model:** Una strategia simile è utilizzare una diversità di modelli e dimensioni. Puoi usare un LLM/SLM o una funzione serverless per instradare le richieste in base alla complessità verso i modelli più adatti. Questo aiuterà anche a ridurre i costi garantendo al contempo le prestazioni sui compiti corretti. Ad esempio, instrada le query semplici verso modelli più piccoli e veloci, e usa i modelli grandi e costosi solo per compiti di ragionamento complesso.

**Caching Responses:** Identificare richieste e compiti comuni e fornire le risposte prima che passino attraverso il tuo sistema basato su agenti è un buon modo per ridurre il volume di richieste simili. Puoi anche implementare un flusso per determinare quanto una richiesta sia simile alle richieste memorizzate nella cache usando modelli AI più semplici. Questa strategia può ridurre significativamente i costi per le domande frequenti o i flussi di lavoro comuni.

## Vediamo come funziona nella pratica

Nel [notebook di esempio di questa sezione](./code_samples/10-expense_claim-demo.ipynb), vedremo esempi di come possiamo usare strumenti di osservabilità per monitorare e valutare il nostro agente.


### Hai altre domande sugli agenti AI in produzione?

Unisciti al [Microsoft Foundry Discord](https://aka.ms/ai-agents/discord) per incontrare altri studenti, partecipare alle ore di ricevimento e ottenere risposte alle tue domande sugli agenti AI.

## Lezione precedente

[Pattern di Metacognizione](../09-metacognition/README.md)

## Prossima lezione

[Protocolli agentici](../11-agentic-protocols/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
Dichiarazione di non responsabilità:
Questo documento è stato tradotto utilizzando il servizio di traduzione AI Co-op Translator (https://github.com/Azure/co-op-translator). Pur impegnandoci a garantire l'accuratezza, si prega di notare che le traduzioni automatiche possono contenere errori o inesattezze. Il documento originale nella sua lingua nativa deve essere considerato la fonte autorevole. Per informazioni critiche, si consiglia una traduzione professionale effettuata da un traduttore umano. Non siamo responsabili per eventuali fraintendimenti o interpretazioni errate derivanti dall'uso di questa traduzione.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->