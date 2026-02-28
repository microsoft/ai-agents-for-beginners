# Memoria per agenti AI 
[![Memoria per agenti](../../../translated_images/it/lesson-13-thumbnail.959e3bc52d210c64.webp)](https://youtu.be/QrYbHesIxpw?si=qNYW6PL3fb3lTPMk)

Quando si discutono i benefici unici della creazione di agenti AI, si affrontano principalmente due aspetti: la capacità di chiamare strumenti per completare attività e la capacità di migliorare nel tempo. La memoria è alla base della creazione di agenti che si auto-migliorano e che possono offrire esperienze migliori ai nostri utenti.

In questa lezione esamineremo cos'è la memoria per gli agenti AI e come possiamo gestirla e utilizzarla a beneficio delle nostre applicazioni.

## Introduzione

Questa lezione coprirà:

• **Comprendere la memoria degli agenti AI**: Cos'è la memoria e perché è essenziale per gli agenti.

• **Implementare e archiviare la memoria**: Metodi pratici per aggiungere capacità di memoria ai tuoi agenti AI, concentrandosi su memoria a breve termine e a lungo termine.

• **Rendere gli agenti AI auto-miglioranti**: Come la memoria consente agli agenti di apprendere dalle interazioni passate e migliorare nel tempo.

## Implementazioni disponibili

Questa lezione include due tutorial completi in notebook:

• **[13-agent-memory.ipynb](./13-agent-memory.ipynb)**: Implementa la memoria usando Mem0 e Azure AI Search con Microsoft Agent Framework

• **[13-agent-memory-cognee.ipynb](./13-agent-memory-cognee.ipynb)**: Implementa memoria strutturata usando Cognee, costruendo automaticamente un grafo della conoscenza supportato da embeddings, visualizzando il grafo e recupero intelligente

## Obiettivi di apprendimento

Dopo aver completato questa lezione, saprai come:

• **Differenziare tra vari tipi di memoria per agenti AI**, inclusi memoria di lavoro, a breve termine e a lungo termine, oltre a forme specializzate come memoria di persona ed episodica.

• **Implementare e gestire memoria a breve e a lungo termine per agenti AI** usando Microsoft Agent Framework, sfruttando strumenti come Mem0, Cognee, Whiteboard memory e integrando Azure AI Search.

• **Comprendere i principi alla base degli agenti AI auto-miglioranti** e come sistemi di gestione della memoria robusti contribuiscano all'apprendimento e all'adattamento continuo.

## Comprendere la memoria per agenti AI

Alla sua base, **la memoria per gli agenti AI si riferisce ai meccanismi che permettono loro di conservare e richiamare informazioni**. Queste informazioni possono essere dettagli specifici di una conversazione, preferenze dell'utente, azioni passate o anche pattern appresi.

Senza memoria, le applicazioni AI sono spesso senza stato, il che significa che ogni interazione ricomincia da zero. Questo porta a un'esperienza utente ripetitiva e frustrante in cui l'agente "dimentica" il contesto o le preferenze precedenti.

### Perché la memoria è importante?

L'intelligenza di un agente è profondamente legata alla sua capacità di richiamare e utilizzare informazioni passate. La memoria permette agli agenti di essere:

• **Riflessivi**: Apprendere da azioni e risultati passati.

• **Interattivi**: Mantenere il contesto durante una conversazione in corso.

• **Proattivi e Reattivi**: Anticipare bisogni o rispondere in modo appropriato basandosi su dati storici.

• **Autonomi**: Operare in modo più indipendente attingendo alla conoscenza memorizzata.

L'obiettivo dell'implementazione della memoria è rendere gli agenti più **affidabili e capaci**.

### Tipi di memoria

#### Memoria di lavoro

Pensala come un foglio di appunti che un agente usa durante un singolo compito o processo di pensiero in corso. Contiene informazioni immediate necessarie per calcolare il passo successivo.

Per gli agenti AI, la memoria di lavoro spesso cattura le informazioni più rilevanti di una conversazione, anche se l'intera cronologia della chat è lunga o troncata. Si concentra sull'estrazione di elementi chiave come requisiti, proposte, decisioni e azioni.

**Esempio di memoria di lavoro**

In un agente di prenotazione viaggi, la memoria di lavoro potrebbe catturare la richiesta attuale dell'utente, come "Voglio prenotare un viaggio a Parigi". Questo requisito specifico è mantenuto nel contesto immediato dell'agente per guidare l'interazione corrente.

#### Memoria a breve termine

Questo tipo di memoria conserva le informazioni per la durata di una singola conversazione o sessione. È il contesto della chat corrente, che permette all'agente di riferirsi ai turni precedenti del dialogo.

**Esempio di memoria a breve termine**

Se un utente chiede, "Quanto costerebbe un volo per Parigi?" e poi continua con "E per l'alloggio lì?", la memoria a breve termine assicura che l'agente sappia che "lì" si riferisce a "Parigi" nella stessa conversazione.

#### Memoria a lungo termine

Si tratta di informazioni che persistono attraverso più conversazioni o sessioni. Permette agli agenti di ricordare preferenze degli utenti, interazioni storiche o conoscenze generali per lunghi periodi. Questo è importante per la personalizzazione.

**Esempio di memoria a lungo termine**

Una memoria a lungo termine potrebbe memorizzare che "A Ben piace sciare e le attività all'aperto, ama il caffè con vista sulla montagna e vuole evitare le piste da sci avanzate a causa di una precedente lesione". Questa informazione, appresa da interazioni precedenti, influenza le raccomandazioni in future sessioni di pianificazione di viaggi, rendendole altamente personalizzate.

#### Memoria della persona

Questo tipo di memoria specializzato aiuta un agente a sviluppare una "personalità" o "persona" coerente. Permette all'agente di ricordare dettagli su se stesso o sul ruolo previsto, rendendo le interazioni più fluide e mirate.

**Esempio di memoria della persona**
Se l'agente di viaggio è progettato per essere un "esperto pianificatore di sci", la memoria della persona potrebbe rafforzare questo ruolo, influenzando le risposte per allinearsi con il tono e le conoscenze di un esperto.

#### Memoria del flusso di lavoro/episodica

Questa memoria conserva la sequenza di passaggi che un agente compie durante un compito complesso, inclusi successi e fallimenti. È come ricordare specifici "episodi" o esperienze passate per apprendere da esse.

**Esempio di memoria episodica**

Se l'agente ha tentato di prenotare un determinato volo ma è fallito a causa di indisponibilità, la memoria episodica potrebbe registrare questo fallimento, permettendo all'agente di provare voli alternativi o informare l'utente del problema in modo più informato durante un tentativo successivo.

#### Memoria delle entità

Questo implica l'estrazione e la memorizzazione di entità specifiche (come persone, luoghi o cose) ed eventi dalle conversazioni. Permette all'agente di costruire una comprensione strutturata degli elementi chiave discussi.

**Esempio di memoria delle entità**

Da una conversazione su un viaggio passato, l'agente potrebbe estrarre "Parigi", "Torre Eiffel" e "cena al ristorante Le Chat Noir" come entità. In un'interazione futura, l'agente potrebbe ricordare "Le Chat Noir" e offrire di fare una nuova prenotazione lì.

#### RAG Strutturato (Retrieval Augmented Generation)

Sebbene RAG sia una tecnica più ampia, il "RAG Strutturato" viene evidenziato come una potente tecnologia di memoria. Estrae informazioni dense e strutturate da varie fonti (conversazioni, email, immagini) e le utilizza per migliorare precisione, richiamo e velocità nelle risposte. A differenza del RAG classico che si basa esclusivamente sulla similarità semantica, il RAG Strutturato lavora con la struttura intrinseca delle informazioni.

**Esempio di RAG Strutturato**

Invece di limitarsi a trovare parole chiave corrispondenti, il RAG Strutturato potrebbe analizzare i dettagli di un volo (destinazione, data, ora, compagnia) da una email e memorizzarli in modo strutturato. Questo consente query precise come "Quale volo ho prenotato per Parigi martedì?"

## Implementazione e archiviazione della memoria

Implementare la memoria per gli agenti AI comporta un processo sistematico di **gestione della memoria**, che include la generazione, l'archiviazione, il recupero, l'integrazione, l'aggiornamento e anche il "dimenticare" (o eliminare) le informazioni. Il recupero è un aspetto particolarmente cruciale.

### Strumenti di memoria specializzati

#### Mem0

Un modo per memorizzare e gestire la memoria degli agenti è utilizzare strumenti specializzati come Mem0. Mem0 funziona come uno strato di memoria persistente, permettendo agli agenti di richiamare interazioni rilevanti, memorizzare preferenze degli utenti e contesti fattuali, e apprendere da successi e fallimenti nel tempo. L'idea è che agenti senza stato diventino con stato.

Funziona attraverso una **pipeline di memoria in due fasi: estrazione e aggiornamento**. Per prima cosa, i messaggi aggiunti a un thread dell'agente vengono inviati al servizio Mem0, che utilizza un Large Language Model (LLM) per riassumere la cronologia della conversazione ed estrarre nuove memorie. Successivamente, una fase di aggiornamento guidata dall'LLM determina se aggiungere, modificare o eliminare queste memorie, memorizzandole in un data store ibrido che può includere database vettoriali, grafici e chiave-valore. Questo sistema supporta anche vari tipi di memoria e può incorporare una memoria a grafo per gestire le relazioni tra entità.

#### Cognee

Un altro approccio potente è usare **Cognee**, una memoria semantica open source per agenti AI che trasforma dati strutturati e non strutturati in grafi della conoscenza interrogabili supportati da embeddings. Cognee fornisce un'**architettura dual-store** che combina ricerca per similarità vettoriale con relazioni a grafo, consentendo agli agenti di capire non solo quali informazioni sono simili, ma come i concetti sono correlati tra loro.

Eccelle nel **recupero ibrido** che fonde similarità vettoriale, struttura del grafo e ragionamento LLM - dal semplice lookup di chunk grezzi a domande e risposte consapevoli del grafo. Il sistema mantiene una **memoria viva** che evolve e cresce rimanendo interrogabile come un grafo connesso, supportando sia il contesto di sessione a breve termine sia la memoria persistente a lungo termine.

Il tutorial del notebook Cognee ([13-agent-memory-cognee.ipynb](./13-agent-memory-cognee.ipynb)) dimostra la costruzione di questo strato di memoria unificato, con esempi pratici di ingestione di fonti di dati diverse, visualizzazione del grafo della conoscenza e interrogazione con diverse strategie di ricerca adattate alle esigenze specifiche dell'agente.

### Archiviare la memoria con RAG

Oltre a strumenti di memoria specializzati come mem0 , puoi sfruttare servizi di ricerca robusti come **Azure AI Search come backend per l'archiviazione e il recupero delle memorie**, specialmente per il RAG strutturato.

Questo ti permette di ancorare le risposte del tuo agente ai tuoi dati, garantendo risposte più rilevanti e accurate. Azure AI Search può essere utilizzato per memorizzare memorie di viaggio specifiche per utente, cataloghi di prodotti o qualsiasi altra conoscenza di dominio.

Azure AI Search supporta capacità come **RAG Strutturato**, che eccelle nell'estrarre e recuperare informazioni dense e strutturate da grandi dataset come cronologie di conversazioni, email o anche immagini. Questo fornisce "precisione e richiamo sovrumani" rispetto agli approcci tradizionali di chunking del testo e embedding.

## Rendere gli agenti AI auto-miglioranti

Un modello comune per agenti che si auto-migliorano prevede l'introduzione di un **"agente di conoscenza"**. Questo agente separato osserva la conversazione principale tra l'utente e l'agente primario. Il suo ruolo è:

1. **Identificare informazioni preziose**: Determinare se una parte della conversazione vale la pena di essere salvata come conoscenza generale o come preferenza specifica dell'utente.

2. **Estrarre e riassumere**: Distillare l'apprendimento essenziale o la preferenza dalla conversazione.

3. **Memorizzare in una base di conoscenza**: Persistere queste informazioni estratte, spesso in un database vettoriale, in modo che possano essere recuperate in seguito.

4. **Arricchire query future**: Quando l'utente avvia una nuova query, l'agente di conoscenza recupera le informazioni memorizzate rilevanti e le aggiunge al prompt dell'utente, fornendo contesto cruciale all'agente primario (simile al RAG).

### Ottimizzazioni per la memoria

• **Gestione della latenza**: Per evitare di rallentare le interazioni dell'utente, si può utilizzare inizialmente un modello più economico e veloce per controllare rapidamente se un'informazione è preziosa da memorizzare o recuperare, invocando il processo di estrazione/recupero più complesso solo quando necessario.

• **Manutenzione della base di conoscenza**: Per una knowledge base in crescita, le informazioni meno usate possono essere spostate in "cold storage" per gestire i costi.

## Hai altre domande sulla memoria degli agenti?

Unisciti al [Discord di Microsoft Foundry](https://aka.ms/ai-agents/discord) per incontrare altri learner, partecipare alle ore d'ufficio e ottenere risposte alle tue domande sugli agenti AI.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
Dichiarazione di non responsabilità:
Questo documento è stato tradotto utilizzando il servizio di traduzione con intelligenza artificiale [Co-op Translator](https://github.com/Azure/co-op-translator). Sebbene ci impegniamo a garantire l'accuratezza, si prega di notare che le traduzioni automatiche possono contenere errori o inesattezze. Il documento originale nella sua lingua originale deve essere considerato la fonte autorevole. Per informazioni critiche si raccomanda una traduzione professionale eseguita da un traduttore umano. Non ci assumiamo alcuna responsabilità per eventuali incomprensioni o interpretazioni errate derivanti dall'uso di questa traduzione.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->