# Agenti AI in Produzione: Osservabilità & Valutazione

[![Agenti AI in Produzione](../../../translated_images/it/lesson-10-thumbnail.2b79a30773db093e.webp)](https://youtu.be/l4TP6IyJxmQ?si=reGOyeqjxFevyDq9)

Man mano che gli agenti AI passano da prototipi sperimentali ad applicazioni nel mondo reale, diventa importante la capacità di comprendere il loro comportamento, monitorare le loro prestazioni e valutare sistematicamente i loro output.

## Obiettivi di Apprendimento

Dopo aver completato questa lezione, saprai come/comprenderai:
- Concetti fondamentali dell'osservabilità e della valutazione degli agenti
- Tecniche per migliorare le prestazioni, i costi e l'efficacia degli agenti
- Cosa e come valutare sistematicamente i tuoi agenti AI
- Come controllare i costi quando si distribuiscono agenti AI in produzione
- Come strumentare agenti costruiti con Microsoft Agent Framework

L'obiettivo è fornirti le conoscenze per trasformare i tuoi agenti “scatola nera” in sistemi trasparenti, gestibili e affidabili.

_**Nota:** È importante distribuire agenti AI che siano sicuri e affidabili. Consulta anche la lezione [Costruire Agenti AI Affidabili](../06-building-trustworthy-agents/README.md)._

## Tracce e Span

Gli strumenti di osservabilità come [Langfuse](https://langfuse.com/) o [Microsoft Foundry](https://learn.microsoft.com/en-us/azure/ai-foundry/what-is-azure-ai-foundry) solitamente rappresentano le esecuzioni degli agenti come tracce e span.

- **Traccia** rappresenta un compito completo dell'agente dall'inizio alla fine (ad esempio la gestione di una richiesta utente).
- **Span** sono singoli passaggi all'interno della traccia (ad esempio la chiamata a un modello di linguaggio o il recupero di dati).

![Albero delle tracce in Langfuse](https://langfuse.com/images/cookbook/example-autogen-evaluation/trace-tree.png)
<!-- URL dell'immagine mantenuto per scopi illustrativi -->

Senza osservabilità, un agente AI può sembrare una “scatola nera” - il suo stato interno e il ragionamento sono opachi, rendendo difficile diagnosticare problemi o ottimizzare le prestazioni. Con l'osservabilità, gli agenti diventano “scatole di vetro”, offrendo trasparenza vitale per costruire fiducia e garantire che operino come previsto.

## Perché l'Osservabilità è Importante negli Ambienti di Produzione

Il passaggio degli agenti AI agli ambienti di produzione introduce una nuova serie di sfide e requisiti. L'osservabilità non è più un "piacere da avere", ma una capacità critica:

*   **Debugging e Analisi della Causa Radice**: Quando un agente fallisce o produce un output inatteso, gli strumenti di osservabilità forniscono le tracce necessarie per individuare la sorgente dell’errore. Questo è particolarmente importante in agenti complessi che possono coinvolgere più chiamate LLM, interazioni con strumenti e logica condizionale.
*   **Gestione della Latency e dei Costi**: Gli agenti AI spesso si basano su LLM e altre API esterne fatturate per token o chiamata. L'osservabilità consente un tracciamento preciso di queste chiamate, aiutando a identificare operazioni eccessivamente lente o costose. Ciò permette ai team di ottimizzare i prompt, selezionare modelli più efficienti o riprogettare i flussi di lavoro per gestire i costi operativi e garantire una buona esperienza utente.
*   **Fiducia, Sicurezza e Conformità**: In molte applicazioni è importante garantire che gli agenti si comportino in modo sicuro ed etico. L'osservabilità fornisce una traccia di controllo delle azioni e decisioni dell'agente. Questo può essere usato per rilevare e mitigare problemi come injection di prompt, generazione di contenuti dannosi o gestione errata di informazioni personali identificabili (PII). Ad esempio, puoi rivedere le tracce per capire perché un agente ha fornito una certa risposta o ha utilizzato uno specifico strumento.
*   **Cicli di Miglioramento Continuo**: I dati di osservabilità sono la base di un processo di sviluppo iterativo. Monitorando come gli agenti performano nel mondo reale, i team possono identificare aree di miglioramento, raccogliere dati per la messa a punto dei modelli e validare l’impatto delle modifiche. Questo crea un ciclo di feedback in cui le informazioni di produzione dall'osservazione online informano gli esperimenti offline e il raffinamento, portando a prestazioni degli agenti progressivamente migliori.

## Metriche Chiave da Monitorare

Per monitorare e comprendere il comportamento degli agenti, dovrebbe essere tracciata una gamma di metriche e segnali. Sebbene le metriche specifiche possano variare in base allo scopo dell'agente, alcune sono universalmente importanti.

Ecco alcune delle metriche più comuni che gli strumenti di osservabilità monitorano:

**Latency:** Quanto velocemente risponde l'agente? Tempi di attesa prolungati impattano negativamente l’esperienza utente. Devi misurare la latenza per i compiti e i singoli passaggi tracciando le esecuzioni dell'agente. Ad esempio, un agente che impiega 20 secondi per tutte le chiamate al modello potrebbe essere accelerato utilizzando un modello più veloce o eseguendo le chiamate in parallelo.

**Costi:** Qual è la spesa per esecuzione dell'agente? Gli agenti AI si affidano a chiamate LLM fatturate per token o a API esterne. Un uso frequente degli strumenti o molte richieste possono aumentare rapidamente i costi. Ad esempio, se un agente chiama un LLM cinque volte per un miglioramento marginale della qualità, devi valutare se il costo è giustificato o se potresti ridurre il numero di chiamate o usare un modello più economico. Il monitoraggio in tempo reale può anche aiutare a identificare picchi inattesi (es. bug che causano loop eccessivi di API).

**Errori di Richiesta:** Quante richieste ha fallito l'agente? Questo può includere errori API o chiamate agli strumenti fallite. Per rendere il tuo agente più robusto contro questi errori in produzione, puoi impostare fallback o tentativi di ripetizione. Es. se il fornitore LLM A è inattivo, passi al fornitore LLM B come backup.

**Feedback Utente:** Implementare valutazioni dirette degli utenti fornisce preziose informazioni. Questo può includere valutazioni esplicite (👍pollice su/👎pollice giù, ⭐1-5 stelle) o commenti testuali. Feedback negativi costanti dovrebbero avvisarti in quanto segno che l'agente non funziona come previsto.

**Feedback Utente Implicito:** I comportamenti degli utenti forniscono feedback indiretti anche senza valutazioni esplicite. Questo può includere riformulazioni immediate della domanda, richieste ripetute o clic su un pulsante di retry. Ad esempio, se vedi che gli utenti pongono ripetutamente la stessa domanda, è un segno che l'agente non funziona come previsto.

**Accuratezza:** Quanto frequentemente l'agente produce output corretti o desiderabili? La definizione di accuratezza varia (es. correttezza nella risoluzione dei problemi, accuratezza nel recupero di informazioni, soddisfazione dell’utente). Il primo passo è definire cosa significa successo per il tuo agente. Puoi monitorare l’accuratezza tramite controlli automatizzati, punteggi di valutazione o etichette di completamento del compito. Ad esempio, marcando le tracce come "riuscito" o "fallito".

**Metriche di Valutazione Automatica:** Puoi anche impostare valutazioni automatiche. Ad esempio, puoi usare un LLM per valutare l’output dell’agente, es. se è utile, accurato o meno. Esistono inoltre diverse librerie open source che aiutano a valutare diversi aspetti dell'agente. Es. [RAGAS](https://docs.ragas.io/) per agenti RAG o [LLM Guard](https://llm-guard.com/) per rilevare linguaggio dannoso o injection di prompt.

In pratica, una combinazione di queste metriche fornisce la miglior copertura dello stato di salute di un agente AI. Nel [notebook di esempio](./code_samples/10-expense_claim-demo.ipynb) di questo capitolo, ti mostreremo come appaiono queste metriche in esempi reali, ma prima impareremo come è tipicamente un flusso di lavoro di valutazione.

## Strumenta il tuo Agente

Per raccogliere dati di tracciamento, dovrai strumentare il tuo codice. L’obiettivo è strumentare il codice dell’agente per emettere tracce e metriche che possono essere catturate, elaborate e visualizzate da una piattaforma di osservabilità.

**OpenTelemetry (OTel):** [OpenTelemetry](https://opentelemetry.io/) è emerso come standard industriale per l’osservabilità degli LLM. Fornisce una serie di API, SDK e strumenti per generare, raccogliere ed esportare dati di telemetria.

Esistono molte librerie di strumentazione che avvolgono framework agent esistenti e rendono semplice esportare gli span OpenTelemetry verso uno strumento di osservabilità. Microsoft Agent Framework si integra nativamente con OpenTelemetry. Di seguito un esempio di strumentazione di un agente MAF:

```python
from agent_framework.observability import get_tracer, get_meter

tracer = get_tracer()
meter = get_meter()

with tracer.start_as_current_span("agent_run"):
    # L'esecuzione dell'agente è tracciata automaticamente
    pass
```

Il [notebook di esempio](./code_samples/10-expense_claim-demo.ipynb) in questo capitolo mostrerà come strumentare il tuo agente MAF.

**Creazione Manuale di Span:** Sebbene le librerie di strumentazione forniscano una buona base, spesso ci sono casi in cui sono necessarie informazioni più dettagliate o personalizzate. Puoi creare manualmente span per aggiungere logica applicativa personalizzata. Ancora più importante, possono arricchire gli span creati automaticamente o manualmente con attributi personalizzati (noti anche come tag o metadata). Questi attributi possono includere dati specifici del business, calcoli intermedi o qualunque contesto utile per debug o analisi, come `user_id`, `session_id` o `model_version`.

Esempio di creazione manuale di tracce e span con il [Langfuse Python SDK](https://langfuse.com/docs/sdk/python/sdk-v3):

```python
from langfuse import get_client
 
langfuse = get_client()
 
span = langfuse.start_span(name="my-span")
 
span.end()
```

## Valutazione dell'Agente

L'osservabilità ci dà metriche, ma la valutazione è il processo di analisi di quei dati (e l’esecuzione di test) per determinare quanto bene un agente AI stia performando e come possa essere migliorato. In altre parole, una volta che hai quelle tracce e metriche, come le usi per giudicare l’agente e prendere decisioni?

La valutazione regolare è importante perché gli agenti AI sono spesso non deterministici e possono evolvere (tramite aggiornamenti o cambiamenti nel comportamento del modello) – senza valutazione, non sapresti se il tuo “agente intelligente” sta effettivamente facendo bene il suo lavoro o se ha subito regressioni.

Esistono due categorie di valutazioni per agenti AI: **valutazione online** e **valutazione offline**. Entrambe sono preziose e si completano a vicenda. Di solito cominciamo con la valutazione offline, poiché è il passaggio minimo necessario prima di distribuire qualsiasi agente.

### Valutazione Offline

![Elementi del dataset in Langfuse](https://langfuse.com/images/cookbook/example-autogen-evaluation/example-dataset.png)

Questo comporta la valutazione dell’agente in un ambiente controllato, tipicamente usando dataset di test, non query di utenti reali. Usi dataset curati in cui sai quale sia l’output atteso o il comportamento corretto, quindi esegui il tuo agente su quelli.

Per esempio, se hai costruito un agente per problemi matematici a parole, potresti avere un [dataset di test](https://huggingface.co/datasets/gsm8k) di 100 problemi con risposte note. La valutazione offline viene spesso fatta durante lo sviluppo (e può essere parte delle pipeline CI/CD) per verificare miglioramenti o prevenire regressioni. Il vantaggio è che è **ripetibile e puoi ottenere metriche di accuratezza chiare poiché hai la verità a terra**. Potresti anche simulare query utente e misurare le risposte dell’agente rispetto a risposte ideali o usare metriche automatizzate come descritto sopra.

La principale sfida della valutazione offline è garantire che il tuo dataset di test sia completo e rimanga rilevante – l’agente potrebbe performare bene su un set fisso ma incontrare query molto diverse in produzione. Pertanto, dovresti mantenere aggiornati i set di test con nuovi casi limite ed esempi che riflettano scenari del mondo reale. Una combinazione di piccoli casi di “smoke test” e set di valutazione più ampi è utile: i set piccoli per controlli rapidi e quelli più grandi per metriche di prestazioni più ampie.

### Valutazione Online

![Panoramica delle metriche di osservabilità](https://langfuse.com/images/cookbook/example-autogen-evaluation/dashboard.png)

Questo si riferisce alla valutazione dell’agente in un ambiente reale e vivo, cioè durante l’utilizzo effettivo in produzione. La valutazione online implica il monitoraggio continuo delle prestazioni dell’agente nelle interazioni reali con gli utenti e l’analisi dei risultati.

Per esempio, potresti tracciare tassi di successo, punteggi di soddisfazione degli utenti o altre metriche sul traffico live. Il vantaggio della valutazione online è che **cattura aspetti che potresti non anticipare in un ambiente di laboratorio** – puoi osservare derive del modello nel tempo (se l’efficacia dell’agente degrada man mano che cambiano i pattern di input) e intercettare query o situazioni inattese che non erano nei dati di test. Fornisce un quadro reale di come l’agente si comporta nel mondo reale.

La valutazione online spesso implica la raccolta di feedback utente implicito ed esplicito, come discusso, e possibilmente l’esecuzione di test shadow o test A/B (dove una nuova versione dell’agente gira in parallelo per confronto con quella vecchia). La sfida è che può essere complicato ottenere etichette o punteggi affidabili per le interazioni live – potresti dipendere dal feedback degli utenti o da metriche a valle (ad es. se l’utente ha cliccato il risultato).

### Combinare i due

Le valutazioni online e offline non sono mutuamente esclusive; si completano molto bene a vicenda. Le intuizioni dal monitoraggio online (es. nuovi tipi di query degli utenti in cui l’agente performa male) possono essere usate per arricchire e migliorare i dataset di test offline. Al contrario, agenti che performano bene nei test offline possono essere distribuiti con maggiore fiducia e monitorati online.

Infatti, molti team adottano un ciclo:

_valutare offline -> distribuire -> monitorare online -> raccogliere nuovi casi di fallimento -> aggiungere al dataset offline -> perfezionare l’agente -> ripetere_.

## Problemi Comuni

Quando distribuisci agenti AI in produzione, puoi incontrare varie sfide. Ecco alcuni problemi comuni e le loro possibili soluzioni:

| **Problema**    | **Soluzione Potenziale**   |
| ------------- | ------------------ |
| L’agente AI non esegue le attività in modo consistente | - Raffina il prompt dato all'agente AI; sii chiaro sugli obiettivi.<br>- Identifica se dividere i compiti in sotto-task gestiti da più agenti può aiutare. |
| L’agente AI entra in loop continui  | - Assicurati di avere termini e condizioni di terminazione chiari affinché l’agente sappia quando fermare il processo.<br>- Per compiti complessi che richiedono ragionamento e pianificazione, usa un modello più grande specializzato per compiti di ragionamento. |
| Le chiamate agli strumenti dell’agente AI non funzionano bene   | - Testa e valida l’output dello strumento al di fuori del sistema agente.<br>- Raffina i parametri definiti, i prompt e i nomi degli strumenti.  |
| Il sistema Multi-Agente non funziona consistentemente | - Raffina i prompt dati a ciascun agente per assicurarti che siano specifici e distinti tra loro.<br>- Costruisci un sistema gerarchico usando un agente “routing” o controller per determinare quale agente è quello corretto. |

Molti di questi problemi possono essere identificati più efficacemente con l’osservabilità attivata. Le tracce e metriche discusse in precedenza aiutano a individuare esattamente dove nel flusso dell’agente si verificano i problemi, rendendo il debugging e l’ottimizzazione molto più efficienti.

## Gestire i Costi


Ecco alcune strategie per gestire i costi di distribuzione degli agenti AI in produzione:

**Uso di modelli più piccoli:** I piccoli modelli di linguaggio (SLM) possono funzionare bene in alcuni casi d'uso agentici e ridurranno significativamente i costi. Come menzionato in precedenza, costruire un sistema di valutazione per determinare e confrontare le prestazioni rispetto a modelli più grandi è il modo migliore per capire quanto bene un SLM funzionerà nel tuo caso d'uso. Considera l'uso di SLM per compiti più semplici come la classificazione delle intenzioni o l'estrazione di parametri, riservando i modelli più grandi per ragionamenti complessi.

**Uso di un modello router:** Una strategia simile è usare una diversità di modelli e dimensioni. Puoi usare un LLM/SLM o una funzione serverless per indirizzare le richieste in base alla complessità verso i modelli più adatti. Ciò aiuterà anche a ridurre i costi, garantendo al contempo le prestazioni nei compiti giusti. Per esempio, indirizza le query semplici a modelli più piccoli e veloci, e usa modelli grandi costosi solo per compiti di ragionamento complesso.

**Caching delle risposte:** Identificare richieste e compiti comuni e fornire le risposte prima che passino attraverso il tuo sistema agentico è un buon modo per ridurre il volume di richieste simili. Puoi anche implementare un flusso per identificare quanto una richiesta sia simile alle richieste memorizzate nella cache usando modelli di AI più basilari. Questa strategia può ridurre significativamente i costi per domande frequenti o flussi di lavoro comuni.

## Vediamo come funziona in pratica

Nel [notebook d'esempio di questa sezione](./code_samples/10-expense_claim-demo.ipynb), vedremo esempi di come possiamo usare strumenti di osservabilità per monitorare e valutare il nostro agente.


### Hai altre domande sugli agenti AI in produzione?

Unisciti al [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D) per incontrare altri studenti, partecipare alle office hours e far rispondere alle tue domande sugli agenti AI.

## Lezione precedente

[Pattern di progettazione Metacognitivo](../09-metacognition/README.md)

## Lezione successiva

[Protocolli Agentici](../11-agentic-protocols/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:
Questo documento è stato tradotto utilizzando il servizio di traduzione AI [Co-op Translator](https://github.com/Azure/co-op-translator). Sebbene ci impegniamo per garantire la precisione, si prega di notare che le traduzioni automatizzate possono contenere errori o imprecisioni. Il documento originale nella sua lingua nativa deve essere considerato la fonte autorevole. Per informazioni critiche, si raccomanda una traduzione professionale effettuata da un essere umano. Non siamo responsabili per eventuali malintesi o interpretazioni errate derivanti dall’uso di questa traduzione.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->