<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "8164484c16b1ed3287ef9dae9fc437c1",
  "translation_date": "2025-07-24T08:16:19+00:00",
  "source_file": "10-ai-agents-production/README.md",
  "language_code": "it"
}
-->
# Agenti AI in Produzione: Osservabilità e Valutazione

Man mano che gli agenti AI passano da prototipi sperimentali ad applicazioni reali, diventa fondamentale comprendere il loro comportamento, monitorare le loro prestazioni e valutare sistematicamente i loro output.

## Obiettivi di Apprendimento

Dopo aver completato questa lezione, saprai come/avrai compreso:
- Concetti fondamentali di osservabilità e valutazione degli agenti
- Tecniche per migliorare le prestazioni, i costi e l'efficacia degli agenti
- Cosa e come valutare sistematicamente i tuoi agenti AI
- Come controllare i costi durante il deployment degli agenti AI in produzione
- Come strumentare gli agenti costruiti con AutoGen

L'obiettivo è fornirti le conoscenze necessarie per trasformare i tuoi agenti "scatola nera" in sistemi trasparenti, gestibili e affidabili.

_**Nota:** È importante distribuire agenti AI sicuri e affidabili. Dai un'occhiata alla lezione [Costruire Agenti AI Affidabili](./06-building-trustworthy-agents/README.md)._

## Tracce e Spans

Gli strumenti di osservabilità come [Langfuse](https://langfuse.com/) o [Azure AI Foundry](https://learn.microsoft.com/en-us/azure/ai-foundry/what-is-azure-ai-foundry) solitamente rappresentano le esecuzioni degli agenti come tracce e spans.

- **Traccia** rappresenta un compito completo dell'agente dall'inizio alla fine (ad esempio, gestire una query dell'utente).
- **Spans** sono i singoli passaggi all'interno della traccia (ad esempio, chiamare un modello linguistico o recuperare dati).

![Albero delle tracce in Langfuse](https://langfuse.com/images/cookbook/example-autogen-evaluation/trace-tree.png)

Senza osservabilità, un agente AI può sembrare una "scatola nera" - il suo stato interno e il suo ragionamento sono opachi, rendendo difficile diagnosticare problemi o ottimizzare le prestazioni. Con l'osservabilità, gli agenti diventano "scatole di vetro", offrendo trasparenza essenziale per costruire fiducia e garantire che operino come previsto.

## Perché l'Osservabilità è Importante negli Ambienti di Produzione

Il passaggio degli agenti AI agli ambienti di produzione introduce una nuova serie di sfide e requisiti. L'osservabilità non è più un "optional", ma una capacità critica:

*   **Debugging e Analisi delle Cause**: Quando un agente fallisce o produce un output inaspettato, gli strumenti di osservabilità forniscono le tracce necessarie per individuare la fonte dell'errore. Questo è particolarmente importante in agenti complessi che potrebbero coinvolgere molteplici chiamate LLM, interazioni con strumenti e logica condizionale.
*   **Gestione della Latenza e dei Costi**: Gli agenti AI spesso si affidano a LLM e altre API esterne che vengono fatturate per token o per chiamata. L'osservabilità consente di tracciare con precisione queste chiamate, aiutando a identificare operazioni eccessivamente lente o costose. Questo permette ai team di ottimizzare i prompt, selezionare modelli più efficienti o riprogettare i flussi di lavoro per gestire i costi operativi e garantire una buona esperienza utente.
*   **Fiducia, Sicurezza e Conformità**: In molte applicazioni, è importante garantire che gli agenti si comportino in modo sicuro ed etico. L'osservabilità fornisce una traccia di audit delle azioni e delle decisioni dell'agente. Questo può essere utilizzato per rilevare e mitigare problemi come l'iniezione di prompt, la generazione di contenuti dannosi o la gestione impropria di informazioni personali identificabili (PII). Ad esempio, puoi esaminare le tracce per capire perché un agente ha fornito una certa risposta o utilizzato uno specifico strumento.
*   **Cicli di Miglioramento Continuo**: I dati di osservabilità sono la base di un processo di sviluppo iterativo. Monitorando le prestazioni degli agenti nel mondo reale, i team possono identificare aree di miglioramento, raccogliere dati per il fine-tuning dei modelli e validare l'impatto delle modifiche. Questo crea un ciclo di feedback in cui le intuizioni di produzione derivanti dalla valutazione online informano la sperimentazione offline e il perfezionamento, portando a prestazioni degli agenti progressivamente migliori.

## Metriche Chiave da Monitorare

Per monitorare e comprendere il comportamento degli agenti, è necessario tracciare una serie di metriche e segnali. Sebbene le metriche specifiche possano variare in base allo scopo dell'agente, alcune sono universalmente importanti.

Ecco alcune delle metriche più comuni che gli strumenti di osservabilità monitorano:

**Latenza:** Quanto velocemente risponde l'agente? Tempi di attesa lunghi influenzano negativamente l'esperienza utente. Dovresti misurare la latenza per i compiti e i singoli passaggi tracciando le esecuzioni dell'agente. Ad esempio, un agente che impiega 20 secondi per tutte le chiamate al modello potrebbe essere accelerato utilizzando un modello più veloce o eseguendo le chiamate al modello in parallelo.

**Costi:** Qual è il costo per esecuzione dell'agente? Gli agenti AI si affidano a chiamate LLM fatturate per token o API esterne. L'uso frequente di strumenti o più prompt può aumentare rapidamente i costi. Ad esempio, se un agente chiama un LLM cinque volte per un miglioramento marginale della qualità, devi valutare se il costo è giustificato o se puoi ridurre il numero di chiamate o utilizzare un modello più economico. Il monitoraggio in tempo reale può anche aiutare a identificare picchi imprevisti (ad esempio, bug che causano loop API eccessivi).

**Errori di Richiesta:** Quante richieste ha fallito l'agente? Questo può includere errori API o chiamate agli strumenti fallite. Per rendere il tuo agente più robusto in produzione, puoi configurare fallback o retry. Ad esempio, se il provider LLM A è inattivo, puoi passare al provider LLM B come backup.

**Feedback degli Utenti:** Implementare valutazioni dirette degli utenti fornisce preziose informazioni. Questo può includere valutazioni esplicite (👍pollice in su/👎giù, ⭐1-5 stelle) o commenti testuali. Feedback negativi costanti dovrebbero allertarti, poiché indicano che l'agente non sta funzionando come previsto.

**Feedback Implicito degli Utenti:** I comportamenti degli utenti forniscono feedback indiretto anche senza valutazioni esplicite. Questo può includere la riformulazione immediata delle domande, query ripetute o il clic su un pulsante di retry. Ad esempio, se vedi che gli utenti pongono ripetutamente la stessa domanda, questo è un segnale che l'agente non sta funzionando come previsto.

**Accuratezza:** Con quale frequenza l'agente produce output corretti o desiderabili? Le definizioni di accuratezza variano (ad esempio, correttezza nella risoluzione dei problemi, accuratezza nel recupero delle informazioni, soddisfazione dell'utente). Il primo passo è definire cosa significa successo per il tuo agente. Puoi tracciare l'accuratezza tramite controlli automatizzati, punteggi di valutazione o etichette di completamento dei compiti. Ad esempio, contrassegnare le tracce come "riuscite" o "fallite".

**Metriche di Valutazione Automatica:** Puoi anche configurare valutazioni automatiche. Ad esempio, puoi utilizzare un LLM per valutare l'output dell'agente, ad esempio se è utile, accurato o meno. Esistono anche diverse librerie open source che ti aiutano a valutare diversi aspetti dell'agente. Ad esempio, [RAGAS](https://docs.ragas.io/) per agenti RAG o [LLM Guard](https://llm-guard.com/) per rilevare linguaggio dannoso o iniezione di prompt.

In pratica, una combinazione di queste metriche offre la migliore copertura sulla salute di un agente AI. Nel [notebook di esempio](../../../10-ai-agents-production/code_samples/10_autogen_evaluation.ipynb) di questo capitolo, ti mostreremo come appaiono queste metriche in esempi reali, ma prima impareremo come appare un tipico workflow di valutazione.

## Strumentare il tuo Agente

Per raccogliere dati di tracciamento, dovrai strumentare il tuo codice. L'obiettivo è strumentare il codice dell'agente per emettere tracce e metriche che possono essere catturate, elaborate e visualizzate da una piattaforma di osservabilità.

**OpenTelemetry (OTel):** [OpenTelemetry](https://opentelemetry.io/) è emerso come standard industriale per l'osservabilità degli LLM. Fornisce un set di API, SDK e strumenti per generare, raccogliere ed esportare dati di telemetria.

Esistono molte librerie di strumentazione che avvolgono i framework degli agenti esistenti e rendono facile esportare gli spans di OpenTelemetry a uno strumento di osservabilità. Di seguito è riportato un esempio di strumentazione di un agente AutoGen con la libreria di strumentazione [OpenLit](https://github.com/openlit/openlit):

```python
import openlit

openlit.init(tracer = langfuse._otel_tracer, disable_batch = True)
```

Il [notebook di esempio](../../../10-ai-agents-production/code_samples/10_autogen_evaluation.ipynb) in questo capitolo dimostrerà come strumentare il tuo agente AutoGen.

**Creazione Manuale di Spans:** Sebbene le librerie di strumentazione forniscano una buona base, ci sono spesso casi in cui sono necessarie informazioni più dettagliate o personalizzate. Puoi creare spans manualmente per aggiungere logica applicativa personalizzata. Ancora più importante, possono arricchire spans creati automaticamente o manualmente con attributi personalizzati (noti anche come tag o metadata). Questi attributi possono includere dati specifici del business, calcoli intermedi o qualsiasi contesto che potrebbe essere utile per il debugging o l'analisi, come `user_id`, `session_id` o `model_version`.

Esempio di creazione manuale di tracce e spans con il [Langfuse Python SDK](https://langfuse.com/docs/sdk/python/sdk-v3):

```python
from langfuse import get_client
 
langfuse = get_client()
 
span = langfuse.start_span(name="my-span")
 
span.end()
```

## Valutazione degli Agenti

L'osservabilità ci fornisce metriche, ma la valutazione è il processo di analisi di quei dati (e di esecuzione di test) per determinare quanto bene un agente AI sta performando e come può essere migliorato. In altre parole, una volta che hai quelle tracce e metriche, come le usi per giudicare l'agente e prendere decisioni?

La valutazione regolare è importante perché gli agenti AI sono spesso non deterministici e possono evolversi (attraverso aggiornamenti o cambiamenti nel comportamento del modello) – senza valutazione, non sapresti se il tuo "agente intelligente" sta effettivamente svolgendo bene il suo lavoro o se è regredito.

Ci sono due categorie di valutazioni per gli agenti AI: **valutazione online** e **valutazione offline**. Entrambe sono preziose e si completano a vicenda. Di solito si inizia con la valutazione offline, poiché questo è il passo minimo necessario prima di distribuire qualsiasi agente.

### Valutazione Offline

![Elementi del dataset in Langfuse](https://langfuse.com/images/cookbook/example-autogen-evaluation/example-dataset.png)

Questa consiste nel valutare l'agente in un ambiente controllato, tipicamente utilizzando dataset di test, non query di utenti live. Si utilizzano dataset curati in cui si conosce quale dovrebbe essere l'output previsto o il comportamento corretto, e poi si esegue l'agente su questi.

Ad esempio, se hai costruito un agente per problemi matematici, potresti avere un [dataset di test](https://huggingface.co/datasets/gsm8k) di 100 problemi con risposte note. La valutazione offline viene spesso eseguita durante lo sviluppo (e può far parte delle pipeline CI/CD) per verificare miglioramenti o prevenire regressioni. Il vantaggio è che è **ripetibile e puoi ottenere metriche di accuratezza chiare poiché hai una verità di riferimento**. Potresti anche simulare query degli utenti e misurare le risposte dell'agente rispetto alle risposte ideali o utilizzare metriche automatizzate come descritto sopra.

La sfida principale con la valutazione offline è garantire che il tuo dataset di test sia completo e rimanga rilevante – l'agente potrebbe performare bene su un set di test fisso ma incontrare query molto diverse in produzione. Pertanto, dovresti mantenere i set di test aggiornati con nuovi casi limite ed esempi che riflettano scenari reali​. Una combinazione di piccoli casi di "smoke test" e set di valutazione più ampi è utile: piccoli set per controlli rapidi e set più grandi per metriche di prestazione più ampie​.

### Valutazione Online

![Panoramica delle metriche di osservabilità](https://langfuse.com/images/cookbook/example-autogen-evaluation/dashboard.png)

Questa si riferisce alla valutazione dell'agente in un ambiente reale, ovvero durante l'uso effettivo in produzione. La valutazione online implica il monitoraggio delle prestazioni dell'agente sulle interazioni reali degli utenti e l'analisi continua dei risultati.

Ad esempio, potresti tracciare tassi di successo, punteggi di soddisfazione degli utenti o altre metriche sul traffico live. Il vantaggio della valutazione online è che **cattura cose che potresti non anticipare in un ambiente di laboratorio** – puoi osservare il drift del modello nel tempo (se l'efficacia dell'agente si degrada man mano che i pattern di input cambiano) e rilevare query o situazioni inaspettate che non erano nel tuo dataset di test​. Fornisce un quadro reale di come l'agente si comporta nel mondo reale.

La valutazione online spesso implica la raccolta di feedback impliciti ed espliciti degli utenti, come discusso, e possibilmente l'esecuzione di test ombra o test A/B (dove una nuova versione dell'agente viene eseguita in parallelo per confrontarsi con la vecchia). La sfida è che può essere difficile ottenere etichette o punteggi affidabili per le interazioni live – potresti fare affidamento su feedback degli utenti o metriche a valle (ad esempio, l'utente ha cliccato sul risultato).

### Combinare le Due

Le valutazioni online e offline non si escludono a vicenda; si completano a vicenda. Le intuizioni derivanti dal monitoraggio online (ad esempio, nuovi tipi di query degli utenti in cui l'agente performa male) possono essere utilizzate per arricchire e migliorare i dataset di test offline. Al contrario, gli agenti che performano bene nei test offline possono essere distribuiti e monitorati online con maggiore fiducia.

Infatti, molti team adottano un ciclo:

_valutare offline -> distribuire -> monitorare online -> raccogliere nuovi casi di fallimento -> aggiungere al dataset offline -> perfezionare l'agente -> ripetere_.

## Problemi Comuni

Quando distribuisci agenti AI in produzione, potresti incontrare varie sfide. Ecco alcuni problemi comuni e le loro possibili soluzioni:

| **Problema**    | **Soluzione Potenziale**   |
| ------------- | ------------------ |
| L'agente AI non svolge i compiti in modo coerente | - Affina il prompt dato all'agente AI; sii chiaro sugli obiettivi.<br>- Identifica dove suddividere i compiti in sottocompiti e gestirli con più agenti può essere utile. |
| L'agente AI entra in loop continui  | - Assicurati di avere termini e condizioni di terminazione chiari affinché l'agente sappia quando interrompere il processo.<br>- Per compiti complessi che richiedono ragionamento e pianificazione, utilizza un modello più grande specializzato per compiti di ragionamento. |
| Le chiamate agli strumenti dell'agente AI non funzionano bene   | - Testa e valida l'output dello strumento al di fuori del sistema dell'agente. |

- Affina i parametri definiti, i prompt e la denominazione degli strumenti.  |
| Sistema multi-agente non performante in modo coerente | - Affina i prompt forniti a ciascun agente per garantire che siano specifici e distinti l'uno dall'altro.<br>- Costruisci un sistema gerarchico utilizzando un agente "router" o controller per determinare quale agente sia quello corretto. |

Molti di questi problemi possono essere identificati in modo più efficace con un sistema di osservabilità in atto. I tracciamenti e le metriche di cui abbiamo parlato in precedenza aiutano a individuare esattamente dove, nel flusso di lavoro degli agenti, si verificano i problemi, rendendo il debugging e l'ottimizzazione molto più efficienti.

## Gestione dei Costi

Ecco alcune strategie per gestire i costi di implementazione degli agenti AI in produzione:

**Utilizzo di Modelli più Piccoli:** I Small Language Models (SLM) possono funzionare bene in alcuni casi d'uso agentici e ridurranno significativamente i costi. Come menzionato in precedenza, costruire un sistema di valutazione per determinare e confrontare le prestazioni rispetto ai modelli più grandi è il modo migliore per capire quanto bene un SLM possa funzionare per il tuo caso d'uso. Considera di utilizzare gli SLM per compiti più semplici come la classificazione delle intenzioni o l'estrazione di parametri, riservando i modelli più grandi per ragionamenti complessi.

**Utilizzo di un Modello Router:** Una strategia simile consiste nell'utilizzare una varietà di modelli di dimensioni diverse. Puoi utilizzare un LLM/SLM o una funzione serverless per indirizzare le richieste in base alla complessità verso i modelli più adatti. Questo aiuterà a ridurre i costi garantendo al contempo prestazioni adeguate per i compiti giusti. Ad esempio, indirizza le query semplici a modelli più piccoli e veloci, e utilizza modelli grandi e costosi solo per compiti di ragionamento complessi.

**Caching delle Risposte:** Identificare richieste e compiti comuni e fornire le risposte prima che passino attraverso il tuo sistema agentico è un buon modo per ridurre il volume di richieste simili. Puoi persino implementare un flusso per identificare quanto una richiesta sia simile alle richieste memorizzate nella cache utilizzando modelli AI più basilari. Questa strategia può ridurre significativamente i costi per domande frequenti o flussi di lavoro comuni.

## Vediamo come funziona in pratica

Nell'[notebook di esempio di questa sezione](../../../10-ai-agents-production/code_samples/10_autogen_evaluation.ipynb), vedremo esempi di come possiamo utilizzare strumenti di osservabilità per monitorare e valutare il nostro agente.

## Lezione Precedente

[Design Pattern di Metacognizione](../09-metacognition/README.md)

## Prossima Lezione

[MCP](../11-mcp/README.md)

**Disclaimer (Avvertenza)**:  
Questo documento è stato tradotto utilizzando il servizio di traduzione automatica [Co-op Translator](https://github.com/Azure/co-op-translator). Sebbene ci impegniamo per garantire l'accuratezza, si prega di tenere presente che le traduzioni automatiche possono contenere errori o imprecisioni. Il documento originale nella sua lingua nativa dovrebbe essere considerato la fonte autorevole. Per informazioni critiche, si raccomanda una traduzione professionale effettuata da un traduttore umano. Non siamo responsabili per eventuali incomprensioni o interpretazioni errate derivanti dall'uso di questa traduzione.