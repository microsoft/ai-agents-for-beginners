# Memoria per agenti di IA 
[![Memoria agente](../../../translated_images/it/lesson-13-thumbnail.959e3bc52d210c64.webp)](https://youtu.be/QrYbHesIxpw?si=qNYW6PL3fb3lTPMk)

Quando si discutono i vantaggi unici della creazione di agenti di IA, si parla principalmente di due cose: la capacità di chiamare strumenti per completare compiti e la capacità di migliorare nel tempo. La memoria è alla base della creazione di un agente che si auto-migliora e che può creare esperienze migliori per i nostri utenti.

In questa lezione, esamineremo cos'è la memoria per gli agenti di IA e come possiamo gestirla e utilizzarla a vantaggio delle nostre applicazioni.

## Introduzione

Questa lezione tratterà:

• **Comprendere la memoria degli agenti di IA**: Cos'è la memoria e perché è essenziale per gli agenti.

• **Implementazione e memorizzazione della memoria**: Metodi pratici per aggiungere capacità di memoria ai tuoi agenti di IA, con un focus su memoria a breve termine e a lungo termine.

• **Rendere gli agenti di IA auto-miglioranti**: Come la memoria permette agli agenti di apprendere dalle interazioni passate e migliorare nel tempo.

## Implementazioni disponibili

Questa lezione include due tutorial completi in notebook:

• **[13-agent-memory.ipynb](./13-agent-memory.ipynb)**: Implementa la memoria usando Mem0 e Azure AI Search con Microsoft Agent Framework

• **[13-agent-memory-cognee.ipynb](./13-agent-memory-cognee.ipynb)**: Implementa memoria strutturata usando Cognee, costruendo automaticamente un grafo della conoscenza supportato da embeddings, visualizzando il grafo e recupero intelligente

## Obiettivi di apprendimento

Dopo aver completato questa lezione, saprai come:

• **Differenziare tra vari tipi di memoria degli agenti di IA**, inclusi working, a breve termine e a lungo termine, oltre a forme specializzate come persona ed episodica.

• **Implementare e gestire memoria a breve e a lungo termine per agenti di IA** usando Microsoft Agent Framework, sfruttando strumenti come Mem0, Cognee, Whiteboard memory e integrando Azure AI Search.

• **Comprendere i principi alla base degli agenti di IA auto-miglioranti** e come sistemi solidi di gestione della memoria contribuiscano all'apprendimento e all'adattamento continui.

## Comprendere la memoria degli agenti di IA

Alla base, **la memoria per gli agenti di IA si riferisce ai meccanismi che permettono loro di trattenere e richiamare informazioni**. Queste informazioni possono essere dettagli specifici su una conversazione, preferenze dell'utente, azioni passate o persino schemi appresi.

Senza memoria, le applicazioni di IA sono spesso prive di stato, il che significa che ogni interazione inizia da zero. Questo porta a un'esperienza utente ripetitiva e frustrante in cui l'agente "dimentica" il contesto o le preferenze precedenti.

### Perché la memoria è importante?

L'intelligenza di un agente è profondamente legata alla sua capacità di richiamare e utilizzare informazioni passate. La memoria consente agli agenti di essere:

• **Riflessivi**: Apprendere da azioni e risultati passati.

• **Interattivi**: Mantenere il contesto durante una conversazione in corso.

• **Proattivi e reattivi**: Anticipare bisogni o rispondere in modo appropriato basandosi sui dati storici.

• **Autonomi**: Operare in modo più indipendente attingendo alla conoscenza memorizzata.

L'obiettivo dell'implementazione della memoria è rendere gli agenti più **affidabili e capaci**.

### Tipi di memoria

#### Working Memory

Pensalo come a un pezzo di carta su cui un agente scrive durante un singolo compito o processo di pensiero in corso. Contiene informazioni immediate necessarie per calcolare il passo successivo.

Per gli agenti di IA, la working memory spesso cattura le informazioni più rilevanti da una conversazione, anche se la cronologia completa della chat è lunga o troncata. Si concentra sull'estrazione di elementi chiave come requisiti, proposte, decisioni e azioni.

**Esempio di Working Memory**

In un agente di prenotazione viaggi, la working memory potrebbe catturare la richiesta corrente dell'utente, ad esempio "Voglio prenotare un viaggio a Parigi". Questo requisito specifico viene mantenuto nel contesto immediato dell'agente per guidare l'interazione corrente.

#### Short Term Memory

Questo tipo di memoria conserva le informazioni per la durata di una singola conversazione o sessione. È il contesto della chat corrente, che consente all'agente di riferirsi ai turni precedenti nel dialogo.

**Esempio di Short Term Memory**

Se un utente chiede, "Quanto costerebbe un volo per Parigi?" e poi continua con "E l'alloggio lì?", la short-term memory assicura che l'agente sappia che "lì" si riferisce a "Parigi" nella stessa conversazione.

#### Long Term Memory

Si tratta di informazioni che persistono attraverso più conversazioni o sessioni. Permette agli agenti di ricordare preferenze degli utenti, interazioni storiche o conoscenze generali su periodi estesi. Questo è importante per la personalizzazione.

**Esempio di Long Term Memory**

Una memoria a lungo termine potrebbe memorizzare che "Ben ama lo sci e le attività all'aperto, preferisce il caffè con vista montagna e vuole evitare piste da sci avanzate a causa di una precedente lesione". Questa informazione, appresa da interazioni precedenti, influenza le raccomandazioni nelle future sessioni di pianificazione di viaggi, rendendole altamente personalizzate.

#### Persona Memory

Questo tipo di memoria specializzato aiuta un agente a sviluppare una "personalità" o "persona" coerente. Permette all'agente di ricordare dettagli su se stesso o sul ruolo previsto, rendendo le interazioni più fluide e mirate.

**Esempio di Persona Memory**
Se l'agente di viaggio è progettato per essere un "esperto pianificatore di sci", la persona memory potrebbe rafforzare questo ruolo, influenzando le risposte dell'agente per allinearle al tono e alla conoscenza di un esperto.

#### Workflow/Episodic Memory

Questa memoria memorizza la sequenza di passaggi che un agente compie durante un compito complesso, inclusi successi e fallimenti. È come ricordare specifici "episodi" o esperienze passate per apprendere da esse.

**Esempio di Episodic Memory**

Se l'agente ha tentato di prenotare un volo specifico ma ha fallito a causa di indisponibilità, l'episodic memory potrebbe registrare questo fallimento, permettendo all'agente di provare voli alternativi o informare l'utente del problema in modo più informato durante un tentativo successivo.

#### Entity Memory

Questo comporta l'estrazione e la memorizzazione di entità specifiche (come persone, luoghi o oggetti) ed eventi dalle conversazioni. Permette all'agente di costruire una comprensione strutturata degli elementi chiave discussi.

**Esempio di Entity Memory**

Da una conversazione su un viaggio passato, l'agente potrebbe estrarre "Parigi", "Torre Eiffel" e "cena al ristorante Le Chat Noir" come entità. In una futura interazione, l'agente potrebbe ricordare "Le Chat Noir" e offrire di effettuare una nuova prenotazione lì.

#### Structured RAG (Retrieval Augmented Generation)

Mentre RAG è una tecnica più ampia, il "Structured RAG" è evidenziato come una potente tecnologia di memoria. Estrae informazioni dense e strutturate da varie fonti (conversazioni, email, immagini) e le usa per migliorare precisione, richiamo e velocità nelle risposte. A differenza del RAG classico che si basa esclusivamente sulla similarità semantica, lo Structured RAG lavora con la struttura intrinseca delle informazioni.

**Esempio di Structured RAG**

Invece di limitarsi a corrispondere parole chiave, lo Structured RAG potrebbe analizzare i dettagli di un volo (destinazione, data, ora, compagnia aerea) da un'email e memorizzarli in modo strutturato. Questo consente query precise come "Quale volo ho prenotato per Parigi martedì?"

## Implementare e memorizzare la memoria

Implementare la memoria per gli agenti di IA comporta un processo sistematico di **gestione della memoria**, che include generare, memorizzare, recuperare, integrare, aggiornare e persino "dimenticare" (o eliminare) le informazioni. Il recupero è un aspetto particolarmente cruciale.

### Strumenti di memoria specializzati

#### Mem0

Un modo per memorizzare e gestire la memoria degli agenti è usare strumenti specializzati come Mem0. Mem0 funziona come uno strato di memoria persistente, permettendo agli agenti di richiamare interazioni rilevanti, memorizzare preferenze degli utenti e contesto fattuale, e apprendere da successi e fallimenti nel tempo. L'idea è che agenti senza stato diventino agenti con stato.

Funziona attraverso una **pipeline della memoria in due fasi: estrazione e aggiornamento**. Prima, i messaggi aggiunti al thread di un agente vengono inviati al servizio Mem0, che usa un Large Language Model (LLM) per riassumere la storia della conversazione ed estrarre nuove memorie. Successivamente, una fase di aggiornamento guidata dall'LLM determina se aggiungere, modificare o eliminare queste memorie, memorizzandole in un archivio ibrido che può includere database vettoriali, a grafo e key-value. Questo sistema supporta inoltre vari tipi di memoria e può incorporare una memoria a grafo per gestire le relazioni tra entità.

#### Cognee

Un altro approccio potente è usare **Cognee**, una memoria semantica open-source per agenti di IA che trasforma dati strutturati e non strutturati in grafi della conoscenza interrogabili supportati da embeddings. Cognee fornisce una **architettura dual-store** che combina ricerca per similarità vettoriale con relazioni a grafo, consentendo agli agenti di capire non solo quali informazioni siano simili, ma come i concetti siano correlati tra loro.

Eccelle nel **recupero ibrido** che fonde similarità vettoriale, struttura del grafo e ragionamento LLM — dalla semplice ricerca di chunk grezzi a risposte a domande consapevoli del grafo. Il sistema mantiene una **memoria viva** che evolve e cresce rimanendo interrogabile come un grafo connesso, supportando sia il contesto di sessione a breve termine sia la memoria persistente a lungo termine.

Il tutorial in notebook su Cognee ([13-agent-memory-cognee.ipynb](./13-agent-memory-cognee.ipynb)) dimostra la costruzione di questo livello di memoria unificato, con esempi pratici di ingestione di fonti di dati diverse, visualizzazione del grafo della conoscenza e query con diverse strategie di ricerca su misura per le esigenze specifiche degli agenti.

### Memorizzare la memoria con RAG

Oltre agli strumenti di memoria specializzati come mem0, è possibile sfruttare servizi di ricerca robusti come **Azure AI Search come backend per memorizzare e recuperare memorie**, specialmente per lo Structured RAG.

Questo ti permette di ancorare le risposte del tuo agente ai tuoi dati, garantendo risposte più rilevanti e accurate. Azure AI Search può essere usato per memorizzare memorie di viaggio specifiche dell'utente, cataloghi di prodotti o qualsiasi altra conoscenza di dominio.

Azure AI Search supporta funzionalità come **Structured RAG**, che eccelle nell'estrazione e nel recupero di informazioni dense e strutturate da grandi set di dati come cronologie di conversazioni, email o anche immagini. Questo fornisce una "precisione e un richiamo sovrumani" rispetto agli approcci tradizionali di suddivisione del testo ed embeddings.

## Rendere gli agenti di IA auto-miglioranti

Un pattern comune per agenti che si auto-migliorano prevede l'introduzione di un **"knowledge agent"**. Questo agente separato osserva la conversazione principale tra l'utente e l'agente primario. Il suo ruolo è:

1. **Identificare informazioni preziose**: Determinare se qualche parte della conversazione vale la pena essere salvata come conoscenza generale o come preferenza specifica dell'utente.

2. **Estrarre e riassumere**: Distillare l'apprendimento essenziale o la preferenza dalla conversazione.

3. **Memorizzare in una base di conoscenza**: Persistere queste informazioni estratte, spesso in un database vettoriale, in modo che possano essere recuperate in seguito.

4. **Arricchire le query future**: Quando l'utente inizia una nuova query, il knowledge agent recupera le informazioni memorizzate rilevanti e le aggiunge al prompt dell'utente, fornendo contesto cruciale all'agente primario (simile al RAG).

### Ottimizzazioni per la memoria

• **Gestione della latenza**: Per evitare di rallentare le interazioni degli utenti, si può usare inizialmente un modello più economico e veloce per verificare rapidamente se un'informazione vale la pena di essere memorizzata o recuperata, invocando il processo di estrazione/recupero più complesso solo quando necessario.

• **Manutenzione della base di conoscenza**: Per una base di conoscenza in crescita, le informazioni meno usate possono essere spostate in "cold storage" per gestire i costi.

## Hai altre domande sulla memoria degli agenti?

Unisciti al [Microsoft Foundry Discord](https://aka.ms/ai-agents/discord) per incontrare altri apprendenti, partecipare alle office hours e ottenere risposte alle tue domande sugli agenti di IA.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
Dichiarazione di non responsabilità:
Questo documento è stato tradotto utilizzando il servizio di traduzione automatica basato su IA Co-op Translator (https://github.com/Azure/co-op-translator). Pur impegnandoci per l’accuratezza, si prega di notare che le traduzioni automatiche possono contenere errori o imprecisioni. Il documento originale nella lingua di origine va considerato la fonte autorevole. Per informazioni critiche è consigliata una traduzione professionale effettuata da un traduttore umano. Non siamo responsabili per eventuali fraintendimenti o interpretazioni errate derivanti dall’uso di questa traduzione.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->