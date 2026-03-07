# Agenti AI in Produzione: Osservabilità e Valutazione

[![Agenti AI in Produzione](../../../translated_images/it/lesson-10-thumbnail.2b79a30773db093e.webp)](https://youtu.be/l4TP6IyJxmQ?si=reGOyeqjxFevyDq9)

Man mano che gli agenti AI passano da prototipi sperimentali ad applicazioni nel mondo reale, diventa importante la capacità di comprendere il loro comportamento, monitorarne le prestazioni e valutare sistematicamente i loro output.

## Obiettivi di apprendimento

Dopo aver completato questa lezione, saprai come/comprenderai:
- Concetti fondamentali di osservabilità e valutazione degli agenti
- Tecniche per migliorare le prestazioni, i costi e l'efficacia degli agenti
- Cosa e come valutare sistematicamente i tuoi agenti AI
- Come controllare i costi quando distribuisci agenti AI in produzione
- Come instrumentare agenti costruiti con Microsoft Agent Framework

L'obiettivo è fornirti le conoscenze per trasformare i tuoi agenti "scatola nera" in sistemi trasparenti, gestibili e affidabili.

_**Nota:** È importante distribuire agenti AI che siano sicuri e affidabili. Dai anche un'occhiata alla lezione [Costruire agenti AI affidabili](./06-building-trustworthy-agents/README.md)._

## Tracce e Span

Gli strumenti di osservabilità come [Langfuse](https://langfuse.com/) o [Microsoft Foundry](https://learn.microsoft.com/en-us/azure/ai-foundry/what-is-azure-ai-foundry) solitamente rappresentano le esecuzioni degli agenti come tracce e span.

- **Traccia** rappresenta un compito completo dell'agente dall'inizio alla fine (ad esempio la gestione di una richiesta utente).
- **Span** sono passaggi individuali all'interno della traccia (ad esempio la chiamata a un modello linguistico o il recupero di dati).

![Albero di tracce in Langfuse](https://langfuse.com/images/cookbook/example-autogen-evaluation/trace-tree.png)
<!-- Image URL retained for illustration purposes -->

Senza osservabilità, un agente AI può sembrare una "scatola nera" - il suo stato interno e il suo ragionamento sono opachi, rendendo difficile diagnosticare problemi o ottimizzare le prestazioni. Con l'osservabilità, gli agenti diventano "scatole di vetro", offrendo trasparenza vitale per costruire fiducia e garantire che funzionino come previsto. 

## Perché l'osservabilità è importante negli ambienti di produzione

Trasferire gli agenti AI in ambienti di produzione introduce una nuova serie di sfide e requisiti. L'osservabilità non è più un "bello da avere" ma una capacità critica:

*   **Debugging e analisi della causa principale:** Quando un agente fallisce o produce un output inaspettato, gli strumenti di osservabilità forniscono le tracce necessarie per individuare la sorgente dell'errore. Questo è particolarmente importante in agenti complessi che possono coinvolgere più chiamate LLM, interazioni con strumenti e logica condizionale.
*   **Gestione della latenza e dei costi:** Gli agenti AI spesso si basano su LLM e altre API esterne che sono fatturate per token o per chiamata. L'osservabilità permette di tracciare con precisione queste chiamate, aiutando a identificare operazioni che sono eccessivamente lente o costose. Questo consente ai team di ottimizzare i prompt, scegliere modelli più efficienti o riprogettare i flussi di lavoro per gestire i costi operativi e garantire una buona esperienza utente.
*   **Fiducia, sicurezza e conformità:** In molte applicazioni è importante garantire che gli agenti si comportino in modo sicuro ed etico. L'osservabilità fornisce una pista di controllo delle azioni e delle decisioni dell'agente. Questo può essere usato per rilevare e mitigare problemi come l'iniezione di prompt, la generazione di contenuti dannosi o la gestione scorretta di informazioni personali identificabili (PII). Ad esempio, puoi rivedere le tracce per capire perché un agente ha fornito una certa risposta o ha utilizzato uno strumento specifico.
*   **Cicli di miglioramento continuo:** I dati di osservabilità sono la base di un processo di sviluppo iterativo. Monitorando come gli agenti si comportano nel mondo reale, i team possono identificare aree di miglioramento, raccogliere dati per il fine-tuning dei modelli e validare l'impatto delle modifiche. Questo crea un ciclo di feedback in cui le intuizioni di produzione dall'analisi online informano sperimentazioni e perfezionamenti offline, portando a prestazioni dell'agente progressivamente migliori.

## Metriche chiave da monitorare

Per monitorare e comprendere il comportamento dell'agente, è necessario tracciare una serie di metriche e segnali. Sebbene le metriche specifiche possano variare in base allo scopo dell'agente, alcune sono universalmente importanti.

Ecco alcune delle metriche più comuni che gli strumenti di osservabilità monitorano:

**Latenza:** Quanto velocemente risponde l'agente? Tempi di attesa lunghi impattano negativamente l'esperienza utente. Dovresti misurare la latenza per i compiti e i singoli passaggi tracciando le esecuzioni dell'agente. Ad esempio, un agente che impiega 20 secondi per tutte le chiamate al modello potrebbe essere accelerato usando un modello più veloce o eseguendo le chiamate in parallelo.

**Costi:** Qual è la spesa per esecuzione dell'agente? Gli agenti AI si basano su chiamate LLM fatturate per token o su API esterne. L'uso frequente di strumenti o prompt multipli può aumentare rapidamente i costi. Ad esempio, se un agente chiama un LLM cinque volte per un miglioramento marginale della qualità, devi valutare se il costo è giustificato o se puoi ridurre il numero di chiamate o usare un modello più economico. Il monitoraggio in tempo reale può anche aiutare a identificare picchi inattesi (ad es. bug che causano loop eccessivi di API).

**Errori di richiesta:** Quante richieste ha fallito l'agente? Questo può includere errori API o chiamate a strumenti fallite. Per rendere il tuo agente più robusto in produzione, puoi impostare fallback o retry. Ad es., se il provider LLM A è down, passi al provider LLM B come backup.

**Feedback degli utenti:** L'implementazione di valutazioni dirette da parte degli utenti fornisce preziose informazioni. Questo può includere valutazioni esplicite (👍pollice in su/👎pollice giù, ⭐1-5 stelle) o commenti testuali. Feedback negativi coerenti dovrebbero avvisarti poiché sono un segnale che l'agente non sta funzionando come previsto. 

**Feedback implicito degli utenti:** I comportamenti degli utenti forniscono feedback indiretti anche senza valutazioni esplicite. Questo può includere riformulazioni immediate della domanda, query ripetute o il clic su un pulsante di retry. Ad es., se vedi che gli utenti pongono ripetutamente la stessa domanda, è un segno che l'agente non sta funzionando come previsto.

**Accuratezza:** Quanto frequentemente l'agente produce output corretti o desiderabili? Le definizioni di accuratezza variano (ad es., correttezza nella risoluzione di problemi, accuratezza nel recupero di informazioni, soddisfazione dell'utente). Il primo passo è definire cosa significa successo per il tuo agente. Puoi tracciare l'accuratezza tramite controlli automatizzati, punteggi di valutazione o etichette di completamento del compito. Ad esempio, contrassegnare le tracce come "riuscita" o "fallita". 

**Metriche di valutazione automatica:** Puoi anche impostare valutazioni automatiche. Ad esempio, puoi usare un LLM per valutare l'output dell'agente, ad es. se è utile, accurato o no. Esistono anche diverse librerie open source che aiutano a valutare diversi aspetti dell'agente. Ad es. [RAGAS](https://docs.ragas.io/) per agenti RAG o [LLM Guard](https://llm-guard.com/) per rilevare linguaggio dannoso o iniezione di prompt. 

In pratica, una combinazione di queste metriche offre la migliore copertura dello stato di salute di un agente AI. In questo capitolo, nel [notebook di esempio](./code_samples/10-expense_claim-demo.ipynb), ti mostreremo come appaiono queste metriche in esempi reali ma prima, impareremo come è fatto tipicamente un flusso di valutazione.

## Strumenta il tuo agente

Per raccogliere dati di tracing, dovrai instrumentare il tuo codice. L'obiettivo è instrumentare il codice dell'agente per emettere tracce e metriche che possano essere catturate, elaborate e visualizzate da una piattaforma di osservabilità.

**OpenTelemetry (OTel):** [OpenTelemetry](https://opentelemetry.io/) è emerso come standard industriale per l'osservabilità degli LLM. Fornisce un insieme di API, SDK e strumenti per generare, raccogliere ed esportare dati di telemetria. 

Esistono molte librerie di instrumentazione che avvolgono i framework di agenti esistenti e facilitano l'esportazione di span OpenTelemetry verso uno strumento di osservabilità. Microsoft Agent Framework si integra con OpenTelemetry nativamente. Di seguito è riportato un esempio su come instrumentare un agente MAF:

```python
from agent_framework.observability import get_tracer, get_meter

tracer = get_tracer()
meter = get_meter()

with tracer.start_as_current_span("agent_run"):
    # L'esecuzione dell'agente viene tracciata automaticamente
    pass
```

Il [notebook di esempio](./code_samples/10-expense_claim-demo.ipynb) in questo capitolo mostrerà come instrumentare il tuo agente MAF.

**Creazione manuale di span:** Mentre le librerie di instrumentazione forniscono una buona base, ci sono spesso casi in cui sono necessarie informazioni più dettagliate o personalizzate. Puoi creare span manualmente per aggiungere logica applicativa personalizzata. Ancora più importante, possono arricchire span creati automaticamente o manualmente con attributi personalizzati (noti anche come tag o metadata). Questi attributi possono includere dati specifici di business, calcoli intermedi o qualsiasi contesto che potrebbe essere utile per il debugging o l'analisi, come `user_id`, `session_id`, o `model_version`.

Esempio di creazione manuale di tracce e span con il [Langfuse Python SDK](https://langfuse.com/docs/sdk/python/sdk-v3): 

```python
from langfuse import get_client
 
langfuse = get_client()
 
span = langfuse.start_span(name="my-span")
 
span.end()
```

## Valutazione dell'agente

L'osservabilità ci fornisce metriche, ma la valutazione è il processo di analisi di quei dati (e di esecuzione di test) per determinare quanto bene un agente AI stia performando e come possa essere migliorato. In altre parole, una volta che hai quelle tracce e metriche, come le usi per giudicare l'agente e prendere decisioni?

La valutazione regolare è importante perché gli agenti AI sono spesso non deterministici e possono evolvere (tramite aggiornamenti o deriva del comportamento del modello) – senza valutazione non sapresti se il tuo "agente intelligente" sta effettivamente svolgendo bene il suo lavoro o se è regredito.

Ci sono due categorie di valutazioni per gli agenti AI: **valutazione online** e **valutazione offline**. Entrambe sono preziose e si completano a vicenda. Di solito iniziamo con la valutazione offline, poiché questa è la fase minima necessaria prima di distribuire un agente.

### Valutazione offline

![Elementi del dataset in Langfuse](https://langfuse.com/images/cookbook/example-autogen-evaluation/example-dataset.png)

Questo comporta la valutazione dell'agente in un ambiente controllato, tipicamente utilizzando dataset di test, non query degli utenti in tempo reale. Usi dataset curati in cui sai quale dovrebbe essere l'output atteso o il comportamento corretto, e poi esegui il tuo agente su di essi. 

Ad esempio, se hai costruito un agente per risolvere problemi matematici in linguaggio naturale, potresti avere un [dataset di test](https://huggingface.co/datasets/gsm8k) di 100 problemi con risposte note. La valutazione offline viene spesso eseguita durante lo sviluppo (e può far parte delle pipeline CI/CD) per verificare miglioramenti o proteggere contro regressioni. Il vantaggio è che è **ripetibile e puoi ottenere metriche di accuratezza chiare poiché hai la verità di base**. Potresti anche simulare query utente e misurare le risposte dell'agente rispetto a risposte ideali o usare metriche automatiche come descritto sopra. 

La sfida principale con la valutazione offline è garantire che il tuo dataset di test sia completo e rimanga rilevante – l'agente potrebbe comportarsi bene su un set di test fisso ma incontrare query molto diverse in produzione. Pertanto dovresti mantenere i set di test aggiornati con nuovi casi limite ed esempi che riflettano scenari del mondo reale​. Una combinazione di piccoli casi di "smoke test" e set di valutazione più ampi è utile: set piccoli per controlli rapidi e set più grandi per metriche di performance più estese​.

### Valutazione online

![Panoramica delle metriche di osservabilità](https://langfuse.com/images/cookbook/example-autogen-evaluation/dashboard.png)

Questo si riferisce alla valutazione dell'agente in un ambiente reale e attivo, cioè durante l'uso effettivo in produzione. La valutazione online implica il monitoraggio delle prestazioni dell'agente sulle interazioni reali degli utenti e l'analisi continua dei risultati. 

Ad esempio, potresti tracciare tassi di successo, punteggi di soddisfazione degli utenti o altre metriche sul traffico live. Il vantaggio della valutazione online è che **cattura cose che potresti non prevedere in un ambiente di laboratorio** – puoi osservare la deriva del modello nel tempo (se l'efficacia dell'agente diminuisce man mano che cambiano i pattern di input) e intercettare query o situazioni inaspettate che non erano nel tuo dataset di test​. Fornisce un quadro reale di come l'agente si comporta sul campo. 

La valutazione online spesso prevede la raccolta di feedback implicito ed esplicito degli utenti, come discusso, e possibilmente l'esecuzione di test in shadow o A/B test (dove una nuova versione dell'agente viene eseguita in parallelo per confrontarla con la vecchia). La sfida è che può essere difficile ottenere etichette o punteggi affidabili per le interazioni live – potresti fare affidamento sul feedback degli utenti o su metriche di downstream (come se l'utente ha cliccato il risultato).

### Combinare i due approcci

La valutazione online e quella offline non sono mutuamente esclusive; sono altamente complementari. Le intuizioni dal monitoraggio online (ad es., nuovi tipi di query utente in cui l'agente performa male) possono essere usate per arricchire e migliorare i dataset di test offline. Viceversa, agenti che performano bene nei test offline possono poi essere distribuiti con maggiore fiducia e monitorati online. 

In effetti, molti team adottano un ciclo:

_valuta offline -> distribuisci -> monitora online -> raccogli nuovi casi di errore -> aggiungi al dataset offline -> affina l'agente -> ripeti_.

## Problemi comuni

Man mano che distribuisci agenti AI in produzione, potresti incontrare varie sfide. Ecco alcuni problemi comuni e le loro possibili soluzioni:

| **Problema**    | **Soluzione potenziale**   |
| ------------- | ------------------ |
| L'agente AI non esegue i compiti in modo coerente | - Raffina il prompt fornito all'agente AI; sii chiaro sugli obiettivi.<br>- Identifica dove suddividere i compiti in sotto-compiti e gestirli tramite più agenti può aiutare. |
| L'agente AI va in loop continui  | - Assicurati di avere chiare condizioni di terminazione in modo che l'agente sappia quando interrompere il processo.<br>- Per compiti complessi che richiedono ragionamento e pianificazione, usa un modello più grande specializzato per i compiti di ragionamento. |
| Le chiamate agli strumenti dell'agente AI non funzionano bene   | - Testa e convalida l'output dello strumento al di fuori del sistema dell'agente.<br>- Raffina i parametri definiti, i prompt e la denominazione degli strumenti.  |
| Sistema multi-agente non performante in modo coerente | - Raffina i prompt dati a ogni agente per garantire che siano specifici e distinti l'uno dall'altro.<br>- Costruisci un sistema gerarchico usando un agente "routing" o controller per determinare quale agente è quello corretto. |

Molti di questi problemi possono essere identificati più efficacemente con l'osservabilità in atto. Le tracce e le metriche di cui abbiamo parlato aiutano a individuare esattamente dove nel flusso di lavoro dell'agente si verificano i problemi, rendendo il debugging e l'ottimizzazione molto più efficienti.

## Gestione dei costi
Ecco alcune strategie per gestire i costi di mettere in produzione agenti AI:

**Utilizzare modelli più piccoli:** I Modelli Linguistici di Piccole Dimensioni (SLMs) possono offrire buone prestazioni in alcuni casi d'uso agentici e ridurranno significativamente i costi. Come accennato in precedenza, costruire un sistema di valutazione per determinare e confrontare le prestazioni rispetto a modelli più grandi è il modo migliore per comprendere quanto bene uno SLM si comporterà nel tuo caso d'uso. Considera l'uso di SLMs per compiti più semplici come la classificazione delle intenzioni o l'estrazione di parametri, riservando i modelli più grandi per il ragionamento complesso.

**Utilizzare un modello router:** Una strategia simile è usare una varietà di modelli e dimensioni. Puoi usare un LLM/SLM o una funzione serverless per instradare le richieste in base alla complessità verso i modelli più adatti. Questo aiuterà anche a ridurre i costi garantendo al contempo prestazioni sui compiti giusti. Ad esempio, instrada query semplici verso modelli più piccoli e veloci, e utilizza i modelli grandi e costosi solo per compiti di ragionamento complesso.

**Caching delle risposte:** Identificare richieste e compiti comuni e fornire le risposte prima che passino attraverso il tuo sistema agentico è un buon modo per ridurre il volume di richieste simili. Puoi anche implementare un flusso per identificare quanto una richiesta sia simile alle richieste in cache usando modelli AI più basilari. Questa strategia può ridurre significativamente i costi per le domande frequenti o i workflow comuni.

## Vediamo come funziona nella pratica

Nel [notebook di esempio di questa sezione](./code_samples/10-expense_claim-demo.ipynb) vedremo esempi di come possiamo usare strumenti di osservabilità per monitorare e valutare il nostro agente.


### Hai altre domande sugli agenti AI in produzione?

Unisciti al [Microsoft Foundry Discord](https://aka.ms/ai-agents/discord) per incontrare altri studenti, partecipare alle ore di ricevimento e ottenere risposte alle tue domande sugli agenti AI.

## Lezione precedente

[Pattern di progettazione della metacognizione](../09-metacognition/README.md)

## Lezione successiva

[Protocolli agentici](../11-agentic-protocols/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
Esclusione di responsabilità:
Questo documento è stato tradotto utilizzando il servizio di traduzione automatica basato sull'intelligenza artificiale [Co-op Translator](https://github.com/Azure/co-op-translator). Pur impegnandoci a garantire la massima accuratezza, si prega di notare che le traduzioni automatiche possono contenere errori o inesattezze. Il documento originale nella sua lingua d'origine deve essere considerato la fonte autorevole. Per informazioni critiche si raccomanda una traduzione professionale effettuata da un traduttore umano. Non ci assumiamo alcuna responsabilità per eventuali incomprensioni o interpretazioni errate derivanti dall'uso di questa traduzione.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->