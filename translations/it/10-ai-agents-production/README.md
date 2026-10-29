# Agenti AI in Produzione: Osservabilità e Valutazione

[![AI Agents in Production](../../../translated_images/it/lesson-10-thumbnail.2b79a30773db093e.webp)](https://youtu.be/l4TP6IyJxmQ?si=reGOyeqjxFevyDq9)

Man mano che gli agenti AI passano da prototipi sperimentali ad applicazioni nel mondo reale, diventa importante la capacità di comprendere il loro comportamento, monitorare le prestazioni e valutare sistematicamente i loro output.

## Obiettivi di Apprendimento

Dopo aver completato questa lezione, saprai come/capirai:
- Concetti fondamentali di osservabilità e valutazione degli agenti
- Tecniche per migliorare le prestazioni, i costi e l'efficacia degli agenti
- Cosa valutare e come valutare sistematicamente i tuoi agenti AI
- Come controllare i costi quando si distribuiscono agenti AI in produzione
- Come strumentare agenti realizzati con Microsoft Agent Framework

L'obiettivo è fornirti le conoscenze per trasformare i tuoi agenti "scatola nera" in sistemi trasparenti, gestibili e affidabili.

_**Nota:** È importante distribuire agenti AI sicuri e affidabili. Dai un'occhiata anche alla lezione [Building Trustworthy AI Agents](../06-building-trustworthy-agents/README.md)._

## Tracce e Spans

Gli strumenti di osservabilità come [Langfuse](https://langfuse.com/) o [Microsoft Foundry](https://learn.microsoft.com/en-us/azure/ai-foundry/what-is-azure-ai-foundry) generalmente rappresentano le esecuzioni degli agenti come tracce e spans.

- **Trace** rappresenta un compito completo dell'agente dall'inizio alla fine (come gestire una query utente).
- **Spans** sono singoli passaggi all'interno della traccia (come chiamare un modello linguistico o recuperare dati).

![Trace tree in Langfuse](https://langfuse.com/images/cookbook/example-autogen-evaluation/trace-tree.png)
<!-- Image URL retained for illustration purposes -->

Senza osservabilità, un agente AI può sembrare una "scatola nera" - il suo stato interno e il ragionamento sono opachi, rendendo difficile diagnosticare problemi o ottimizzare le prestazioni. Con l'osservabilità, gli agenti diventano "scatole di vetro", offrendo trasparenza fondamentale per costruire fiducia e garantire che operino come previsto.

## Perché l'Osservabilità è Importante negli Ambienti di Produzione

Trasferire gli agenti AI in ambienti di produzione introduce nuove sfide e requisiti. L'osservabilità non è più un "piacere da avere", ma una capacità critica:

*   **Debug e Analisi della Causa Radice**: Quando un agente fallisce o produce un output inatteso, gli strumenti di osservabilità forniscono le tracce necessarie per individuare la fonte dell'errore. Questo è particolarmente importante in agenti complessi che possono includere molteplici chiamate a LLM, interazioni con strumenti e logiche condizionali.
*   **Gestione della Latency e dei Costi**: Gli agenti AI spesso si basano su LLM e altre API esterne che vengono fatturate per token o per chiamata. L'osservabilità consente un monitoraggio preciso di queste chiamate, aiutando a identificare operazioni troppo lente o costose. Ciò permette ai team di ottimizzare i prompt, scegliere modelli più efficienti o riprogettare i flussi di lavoro per gestire i costi operativi e garantire una buona esperienza utente.
*   **Fiducia, Sicurezza e Conformità**: In molte applicazioni è importante assicurarsi che gli agenti si comportino in modo sicuro ed etico. L'osservabilità fornisce una traccia di audit delle azioni e decisioni dell'agente. Questa può essere utilizzata per rilevare e mitigare problemi come l'iniezione di prompt, la generazione di contenuti dannosi o la gestione errata di informazioni personali identificabili (PII). Ad esempio, puoi esaminare le tracce per capire perché un agente ha fornito una certa risposta o ha utilizzato uno strumento specifico.
*   **Cicli di Miglioramento Continuo**: I dati di osservabilità sono la base di un processo di sviluppo iterativo. Monitorando come gli agenti si comportano nel mondo reale, i team possono identificare aree di miglioramento, raccogliere dati per l'ottimizzazione dei modelli e convalidare l'impatto delle modifiche. Ciò crea un ciclo di feedback in cui gli insight di produzione derivanti dalla valutazione online informano la sperimentazione e il perfezionamento offline, portando a prestazioni dell'agente progressivamente migliori.

## Metriche Chiave da Monitorare

Per monitorare e comprendere il comportamento degli agenti, una serie di metriche e segnali dovrebbe essere tracciata. Sebbene le metriche specifiche possano variare in base allo scopo dell'agente, alcune sono universalmente importanti.

Ecco alcune delle metriche più comuni che gli strumenti di osservabilità monitorano:

**Latency:** Quanto velocemente risponde l'agente? Tempi di attesa lunghi impattano negativamente l'esperienza utente. Devi misurare la latenza per i compiti e i singoli passaggi tracciando le esecuzioni dell'agente. Ad esempio, un agente che impiega 20 secondi per tutte le chiamate al modello potrebbe essere accelerato utilizzando un modello più veloce o eseguendo le chiamate in parallelo.

**Costi:** Qual è la spesa per ogni esecuzione dell'agente? Gli agenti AI si basano su chiamate LLM fatturate per token o su API esterne. L'uso frequente di strumenti o prompt multipli può aumentare rapidamente i costi. Per esempio, se un agente chiama un LLM cinque volte per un miglioramento marginale della qualità, devi valutare se il costo è giustificato o se puoi ridurre il numero di chiamate o usare un modello più economico. Il monitoraggio in tempo reale può anche aiutare a identificare picchi imprevisti (ad esempio, bug che causano loop eccessivi di API).

**Errori di Richiesta:** Quante richieste ha fallito l'agente? Questo può includere errori API o chiamate a strumenti fallite. Per rendere il tuo agente più robusto in produzione, puoi poi impostare fallback o ritentativi. Ad esempio, se il fornitore LLM A è non disponibile, passi al fornitore LLM B come backup.

**Feedback Utente:** Implementare valutazioni dirette degli utenti fornisce preziose informazioni. Questo può includere valutazioni esplicite (👍pollice su/👎giù, ⭐1-5 stelle) o commenti testuali. Feedback negativo consistente dovrebbe metterti in allerta perché è un segnale che l'agente non sta funzionando come previsto.

**Feedback Utente Implicito:** I comportamenti degli utenti forniscono feedback indiretti anche senza valutazioni esplicite. Questo può includere la riformulazione immediata della domanda, query ripetute o il clic su un pulsante di ritentativo. Ad esempio, se noti che gli utenti chiedono ripetutamente la stessa domanda, questo è un segnale che l'agente non funziona come previsto.

**Accuratezza:** Quanto frequentemente l'agente produce output corretti o desiderabili? Le definizioni di accuratezza variano (ad esempio, correttezza nella risoluzione dei problemi, accuratezza nel recupero informazioni, soddisfazione dell'utente). Il primo passo è definire cosa significa successo per il tuo agente. Puoi monitorare l'accuratezza tramite controlli automatizzati, punteggi di valutazione o etichette di completamento del compito. Ad esempio, marcando le tracce come "riuscito" o "fallito".

**Metriche di Valutazione Automatizzata:** Puoi anche impostare valutazioni automatizzate. Per esempio, puoi usare un LLM per valutare l'output dell'agente, ad esempio se è utile, accurato o meno. Ci sono anche diverse librerie open source che aiutano a valutare diversi aspetti dell'agente. Ad esempio, [RAGAS](https://docs.ragas.io/) per agenti RAG o [LLM Guard](https://github.com/protectai/llm-guard) per rilevare linguaggio dannoso o iniezioni di prompt.

In pratica, una combinazione di queste metriche offre la copertura migliore per la salute di un agente AI. Nel [notebook di esempio](./code_samples/10-expense_claim-demo.ipynb) di questo capitolo, ti mostreremo come queste metriche appaiono in esempi reali, ma prima impareremo com'è un flusso tipico di valutazione.

## Strumenta il tuo Agente

Per raccogliere dati di tracciamento, dovrai strumentare il tuo codice. L'obiettivo è strumentare il codice dell'agente per emettere tracce e metriche che possano essere catturate, elaborate e visualizzate da una piattaforma di osservabilità.

**OpenTelemetry (OTel):** [OpenTelemetry](https://opentelemetry.io/) è emersa come uno standard industriale per l'osservabilità degli LLM. Fornisce un set di API, SDK e strumenti per generare, raccogliere ed esportare dati di telemetria.

Ci sono molte librerie di strumentazione che avvolgono framework di agenti esistenti e facilitano l'esportazione di span OpenTelemetry verso uno strumento di osservabilità. Microsoft Agent Framework si integra nativamente con OpenTelemetry. Di seguito un esempio di strumentazione di un agente MAF:

```python
from agent_framework.observability import get_tracer, get_meter

tracer = get_tracer()
meter = get_meter()

with tracer.start_as_current_span("agent_run"):
    # Agent execution is traced automatically
    pass
```

Il [notebook di esempio](./code_samples/10-expense_claim-demo.ipynb) in questo capitolo dimostrerà come strumentare il tuo agente MAF.

**Creazione Manuale di Span:** Sebbene le librerie di strumentazione forniscano una buona base, ci sono spesso casi in cui serve un'informazione più dettagliata o personalizzata. Puoi creare manualmente degli span per aggiungere logica applicativa personalizzata. Ancora più importante, questi span creati automaticamente o manualmente possono essere arricchiti con attributi personalizzati (noti anche come tag o metadati). Questi attributi possono includere dati specifici di business, calcoli intermedi o qualsiasi contesto utile per debug o analisi, come `user_id`, `session_id`, o `model_version`.

Esempio di creazione manuale di tracce e spans con il [Langfuse Python SDK](https://langfuse.com/docs/sdk/python/sdk-v3):

```python
from langfuse import get_client
 
langfuse = get_client()
 
span = langfuse.start_span(name="my-span")
 
span.end()
```

## Valutazione degli Agenti

L'osservabilità ci fornisce metriche, ma la valutazione è il processo di analisi di quei dati (e l'esecuzione di test) per determinare quanto bene un agente AI sta performando e come può essere migliorato. In altre parole, una volta ottenute quelle tracce e metriche, come le usi per giudicare l’agente e prendere decisioni?

La valutazione regolare è importante perché gli agenti AI spesso non sono deterministici e possono evolvere (tramite aggiornamenti o variazioni del comportamento del modello) – senza valutazione, non sapresti se il tuo “agente intelligente” sta davvero facendo bene il suo lavoro o se ha subito regressioni.

Ci sono due categorie di valutazioni per gli agenti AI: **valutazione online** e **valutazione offline**. Entrambe sono preziose e si completano a vicenda. Di solito iniziamo con la valutazione offline, poiché è il passaggio minimo necessario prima di distribuire qualunque agente.

### Valutazione Offline

![Dataset items in Langfuse](https://langfuse.com/images/cookbook/example-autogen-evaluation/example-dataset.png)

Questa consiste nel valutare l’agente in un ambiente controllato, tipicamente usando dataset di test, non query utente in tempo reale. Si usano dataset curati dove si conosce quale sia l’output atteso o il comportamento corretto, e si esegue l’agente su questi.

Per esempio, se hai costruito un agente per problemi matematici, potresti avere un [dataset di test](https://huggingface.co/datasets/openai/gsm8k) di 100 problemi con risposte note. La valutazione offline viene spesso fatta durante lo sviluppo (e può far parte di pipeline CI/CD) per controllare miglioramenti o evitare regressioni. Il vantaggio è che è **ripetibile e puoi ottenere metriche di accuratezza chiare poiché hai la verità a terra**. Potresti anche simulare query utente e misurare le risposte rispetto alle risposte ideali o usare metriche automatizzate come descritto sopra.

La sfida principale della valutazione offline è assicurare che il dataset di test sia completo e rimanga rilevante – l’agente potrebbe performare bene su un set fisso, ma incontrare domande molto diverse in produzione. Perciò, dovresti tenere aggiornati i test con nuovi casi limite ed esempi che riflettono scenari reali​. Un mix di piccoli "test di fumo" e set più grandi è utile: piccoli set per controlli rapidi e set più ampi per metriche di performance più estese​.

### Valutazione Online

![Observability metrics overview](https://langfuse.com/images/cookbook/example-autogen-evaluation/dashboard.png)

Questa si riferisce alla valutazione dell’agente in un ambiente reale e dal vivo, cioè durante l’uso effettivo in produzione. La valutazione online implica il monitoraggio continuo delle prestazioni dell’agente sulle interazioni reali degli utenti e l’analisi dei risultati.

Per esempio, potresti tracciare i tassi di successo, score di soddisfazione utenti o altre metriche sul traffico reale. Il vantaggio della valutazione online è che **cattura aspetti che potresti non anticipare in laboratorio** – puoi osservare il drift del modello nel tempo (se l’efficacia dell’agente degrada con il cambiamento dei pattern di input) e catturare query o situazioni inattese che non erano nel dataset di test​. Offre un quadro reale di come l’agente si comporta nel mondo reale.

La valutazione online spesso coinvolge la raccolta di feedback impliciti ed espliciti degli utenti, come discusso, e possibilmente l’esecuzione di shadow test o A/B test (dove una nuova versione dell’agente gira in parallelo per confrontarla con la vecchia). La sfida è che può essere difficile ottenere etichette o punteggi affidabili per le interazioni dal vivo – potresti dover fare affidamento sul feedback degli utenti o su metriche a valle (ad esempio, se l’utente ha cliccato sul risultato).

### Combinare i due Approcci

Le valutazioni online e offline non sono mutualmente esclusive; sono altamente complementari. Le intuizioni dal monitoraggio online (ad esempio, nuovi tipi di query utenti dove l’agente performa male) possono essere usate per arricchire e migliorare i dataset di test offline. Viceversa, agenti che performano bene nei test offline possono poi essere distribuiti con maggiore sicurezza e monitorati online.

Infatti, molti team adottano un ciclo:

_valuta offline -> distribuisci -> monitora online -> raccogli nuovi casi di fallimento -> aggiungi al dataset offline -> affina agente -> ripeti_.

## Problemi Comuni

Distribuendo agenti AI in produzione, puoi incontrare varie sfide. Ecco alcuni problemi comuni e le possibili soluzioni:

| **Problema**    | **Potenziale Soluzione**   |
| ------------- | ------------------ |
| L'agente AI non esegue i compiti in modo coerente | - Affina il prompt fornito all'agente AI; sii chiaro sugli obiettivi.<br>- Identifica dove dividere il compito in sotto-compiti gestiti da molteplici agenti può aiutare. |
| L'agente AI entra in loop continui  | - Assicurati di avere termini e condizioni di terminazione chiari in modo che l'agente sappia quando interrompere il processo.<br>- Per compiti complessi che richiedono ragionamento e pianificazione, usa un modello più grande specializzato in ragionamento. |
| Le chiamate a strumenti dell'agente AI non funzionano bene   | - Testa e valida l'output dello strumento esternamente al sistema agente.<br>- Affina i parametri, i prompt e la denominazione degli strumenti.  |
| Il sistema multi-agente non funziona in modo coerente | - Affina i prompt forniti a ciascun agente per assicurarne la specificità e distinzione.<br>- Costruisci un sistema gerarchico usando un agente "routing" o controller per determinare quale agente è quello corretto. |

Molti di questi problemi possono essere identificati più efficacemente con l'osservabilità attiva. Le tracce e le metriche di cui abbiamo parlato aiutano a individuare esattamente dove nel flusso di lavoro dell'agente si verificano problemi, rendendo il debug e l'ottimizzazione molto più efficienti.

## Gestione dei Costi

Ecco alcune strategie per gestire i costi della distribuzione degli agenti AI in produzione:

**Utilizzo di Modelli Più Piccoli:** I Modelli Linguistici Piccoli (SLM) possono funzionare bene in alcuni casi d'uso agentici e ridurranno significativamente i costi. Come accennato in precedenza, costruire un sistema di valutazione per determinare e confrontare le prestazioni rispetto a modelli più grandi è il modo migliore per capire quanto bene un SLM si comporterà nel tuo caso d'uso. Considera l'utilizzo di SLM per compiti più semplici come la classificazione dell'intento o l'estrazione di parametri, riservando i modelli più grandi per ragionamenti complessi.

**Utilizzo di un Modello Router:** Una strategia simile è utilizzare una diversità di modelli e dimensioni. Puoi usare un LLM/SLM o una funzione serverless per instradare le richieste in base alla complessità verso i modelli più adatti. Questo aiuterà anche a ridurre i costi garantendo prestazioni ottimali nei compiti appropriati. Ad esempio, instrada le query semplici verso modelli più piccoli e veloci, e usa modelli grandi e costosi solo per compiti di ragionamento complessi.

**Caching delle Risposte:** Identificare richieste e compiti comuni e fornire le risposte prima che passino attraverso il tuo sistema agentico è un buon modo per ridurre il volume di richieste simili. Puoi persino implementare un flusso per identificare quanto una richiesta è simile a quelle memorizzate in cache usando modelli AI più basilari. Questa strategia può ridurre significativamente i costi per domande frequenti o flussi di lavoro comuni.

## Vediamo come funziona in pratica

Nel [notebook di esempio di questa sezione](./code_samples/10-expense_claim-demo.ipynb), vedremo esempi di come possiamo usare strumenti di osservabilità per monitorare e valutare il nostro agente.


### Hai altre domande sugli Agenti AI in Produzione?

Unisciti al [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D) per incontrare altri apprendenti, partecipare ad ore di ufficio e ottenere risposte alle tue domande sugli Agenti AI.

## Lezione Precedente

[Metacognition Design Pattern](../09-metacognition/README.md)

## Lezione Successiva

[Agentic Protocols](../11-agentic-protocols/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:
Questo documento è stato tradotto utilizzando il servizio di traduzione AI [Co-op Translator](https://github.com/Azure/co-op-translator). Sebbene ci impegniamo per garantire la precisione, si prega di notare che le traduzioni automatizzate possono contenere errori o imprecisioni. Il documento originale nella sua lingua nativa deve essere considerato la fonte autorevole. Per informazioni critiche, si raccomanda una traduzione professionale effettuata da un essere umano. Non siamo responsabili per eventuali malintesi o interpretazioni errate derivanti dall’uso di questa traduzione.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->