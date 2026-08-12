# Memoria per Agenti AI 
[![Agent Memory](../../../translated_images/it/lesson-13-thumbnail.959e3bc52d210c64.webp)](https://youtu.be/QrYbHesIxpw?si=qNYW6PL3fb3lTPMk)

Quando si discutono i vantaggi unici della creazione di Agenti AI, si parla principalmente di due cose: la capacità di chiamare strumenti per completare compiti e la capacità di migliorare nel tempo. La memoria è alla base della creazione di un agente autolegittimante che può creare esperienze migliori per i nostri utenti.

In questa lezione, esamineremo cosa sia la memoria per gli Agenti AI e come possiamo gestirla e usarla a vantaggio delle nostre applicazioni.

## Introduzione

Questa lezione tratterà:

• **Comprendere la Memoria degli Agenti AI**: Cos'è la memoria e perché è essenziale per gli agenti.

• **Implementare e Archiviare la Memoria**: Metodi pratici per aggiungere capacità di memoria ai tuoi agenti AI, concentrandosi sulla memoria a breve termine e a lungo termine.

• **Rendere gli Agenti AI Autolegittimanti**: Come la memoria permette agli agenti di apprendere dalle interazioni passate e migliorare nel tempo.

## Implementazioni Disponibili

Questa lezione include due tutorial completi in notebook:

• **[13-agent-memory.ipynb](./13-agent-memory.ipynb)**: Implementa la memoria usando Mem0 e Azure AI Search con Microsoft Agent Framework

• **[13-agent-memory-cognee.ipynb](./13-agent-memory-cognee.ipynb)**: Implementa una memoria strutturata usando Cognee, costruendo automaticamente un grafo della conoscenza supportato da embeddings, visualizzando il grafo e effettuando recuperi intelligenti

## Obiettivi di Apprendimento

Dopo aver completato questa lezione, saprai come:

• **Distinguere tra vari tipi di memoria degli agenti AI**, inclusa la memoria di lavoro, a breve termine e a lungo termine, così come forme specializzate come la memoria di persona e la memoria episodica.

• **Implementare e gestire la memoria a breve e lungo termine per agenti AI** utilizzando Microsoft Agent Framework, sfruttando strumenti come Mem0, Cognee, memoria Whiteboard e integrandoli con Azure AI Search.

• **Comprendere i principi alla base degli agenti AI autolegittimanti** e come sistemi robusti di gestione della memoria contribuiscono all’apprendimento continuo e all’adattamento.

## Comprendere la Memoria degli Agenti AI

Al cuore, **la memoria per agenti AI si riferisce ai meccanismi che permettono loro di trattenere e richiamare informazioni**. Queste informazioni possono essere dettagli specifici su una conversazione, preferenze dell’utente, azioni passate o anche schemi appresi.

Senza memoria, le applicazioni AI sono spesso senza stato, il che significa che ogni interazione inizia da zero. Questo porta a un’esperienza utente ripetitiva e frustrante dove l’agente "dimentica" il contesto o le preferenze precedenti.

### Perché la Memoria è Importante?

L’intelligenza di un agente è profondamente legata alla sua capacità di richiamare e utilizzare informazioni passate. La memoria permette agli agenti di essere:

• **Riflessivi**: Apprendere da azioni e risultati passati.

• **Interattivi**: Mantenere il contesto durante una conversazione in corso.

• **Proattivi e Reattivi**: Anticipare bisogni o rispondere adeguatamente basandosi sui dati storici.

• **Autonomi**: Operare più indipendentemente attingendo alla conoscenza memorizzata.

L’obiettivo dell’implementazione della memoria è rendere gli agenti più **affidabili e capaci**.

### Tipi di Memoria

#### Memoria di Lavoro

Pensala come un foglio di appunti che un agente usa durante un singolo compito o processo di pensiero in corso. Contiene le informazioni immediate necessarie per calcolare il passo successivo.

Per gli agenti AI, la memoria di lavoro spesso cattura le informazioni più rilevanti da una conversazione, anche se la cronologia completa della chat è lunga o troncata. Si concentra sull’estrazione di elementi chiave come requisiti, proposte, decisioni e azioni.

**Esempio di Memoria di Lavoro**

In un agente di prenotazione viaggi, la memoria di lavoro potrebbe catturare la richiesta attuale dell’utente, come "Voglio prenotare un viaggio a Parigi". Questo requisito specifico viene mantenuto nel contesto immediato dell’agente per guidare l’interazione corrente.

#### Memoria a Breve Termine

Questo tipo di memoria conserva le informazioni per la durata di una singola conversazione o sessione. È il contesto della chat attuale, che permette all’agente di fare riferimento ai turni precedenti del dialogo.

Nei campioni Python del [Microsoft Agent Framework](https://github.com/microsoft/agent-framework), questo corrisponde a `AgentSession`, creato con `agent.create_session()`. La sessione è la memoria a breve termine integrata nel framework: mantiene il contesto della conversazione disponibile mentre la stessa sessione viene riutilizzata, ma quel contesto non viene mantenuto quando la sessione termina o l’applicazione si riavvia. Usa la memoria a lungo termine per fatti e preferenze che devono sopravvivere tra sessioni, tipicamente tramite un database, indice vettoriale o un altro archivio persistente.

**Esempio di Memoria a Breve Termine**

Se un utente chiede, "Quanto costa un volo per Parigi?" e poi segue con "E per l’alloggio?", la memoria a breve termine garantisce che l’agente sappia che "lì" si riferisce a "Parigi" nella stessa conversazione.

#### Memoria a Lungo Termine

Queste sono informazioni che persistono attraverso molte conversazioni o sessioni. Permette agli agenti di ricordare preferenze utente, interazioni storiche o conoscenze generali per lunghi periodi. Questo è importante per la personalizzazione.

**Esempio di Memoria a Lungo Termine**

Una memoria a lungo termine potrebbe conservare che "Ben ama sciare e attività all’aperto, gradisce il caffè con vista montagna, e vuole evitare piste da sci avanzate a causa di un infortunio passato". Queste informazioni, apprese da interazioni precedenti, influenzano raccomandazioni nelle future sessioni di pianificazione viaggi, rendendole molto personalizzate.

#### Memoria della Persona

Questo tipo di memoria specializzato aiuta un agente a sviluppare una "personalità" o "persona" coerente. Permette all’agente di ricordare dettagli su se stesso o sul suo ruolo previsto, rendendo le interazioni più fluide e focalizzate.

**Esempio di Memoria della Persona**
Se l’agente di viaggi è progettato per essere un "esperto pianificatore di sci," la memoria della persona potrebbe rafforzare questo ruolo, influenzando le sue risposte per allinearle al tono e alla conoscenza di un esperto.

#### Memoria di Workflow/Episodica

Questa memoria conserva la sequenza di passi che un agente compie durante un compito complesso, inclusi successi e fallimenti. È come ricordare specifici "episodi" o esperienze passate da cui imparare.

**Esempio di Memoria Episodica**

Se l’agente ha tentato di prenotare un volo specifico ma è fallito a causa della non disponibilità, la memoria episodica potrebbe registrare questo fallimento, permettendo all’agente di provare voli alternativi o informare l’utente del problema in modo più informato durante un tentativo successivo.

#### Memoria di Entità

Questo implica l’estrazione e la memorizzazione di entità specifiche (come persone, luoghi o cose) ed eventi dalle conversazioni. Permette all’agente di costruire una comprensione strutturata degli elementi chiave discussi.

**Esempio di Memoria di Entità**

Da una conversazione su un viaggio passato, l’agente potrebbe estrarre "Parigi," "Torre Eiffel," e "cena al ristorante Le Chat Noir" come entità. In una futura interazione, l’agente potrebbe ricordare "Le Chat Noir" e offrire di fare una nuova prenotazione lì.

#### RAG Strutturato (Retrieval Augmented Generation)

Mentre RAG è una tecnica più ampia, il "RAG Strutturato" è evidenziato come una tecnologia di memoria potente. Estrae informazioni dense e strutturate da varie fonti (conversazioni, email, immagini) e le usa per migliorare precisione, richiamo e velocità nelle risposte. A differenza del RAG classico che si basa solo sulla similarità semantica, il RAG Strutturato lavora con la struttura intrinseca delle informazioni.

**Esempio di RAG Strutturato**

Invece di limitarsi a far corrispondere parole chiave, il RAG Strutturato potrebbe analizzare dettagli del volo (destinazione, data, ora, compagnia aerea) da un’email e archiviarli in modo strutturato. Ciò consente query precise come "Quale volo ho prenotato per Parigi martedì?"

## Implementare e Archiviare la Memoria

Implementare la memoria per agenti AI comporta un processo sistematico di **gestione della memoria**, il quale include generazione, archiviazione, recupero, integrazione, aggiornamento e persino "dimenticanza" (o cancellazione) delle informazioni. Il recupero è un aspetto particolarmente cruciale.

### Strumenti di Memoria Specializzati

#### Mem0

Un modo per archiviare e gestire la memoria degli agenti è usare strumenti specializzati come Mem0. Mem0 funziona come uno strato di memoria persistente, consentendo agli agenti di richiamare interazioni rilevanti, archiviare preferenze utente e contesto fattuale, e apprendere da successi e fallimenti nel tempo. L’idea qui è che agenti senza stato diventano agenti con stato.

Funziona attraverso una **pipeline di memoria a due fasi: estrazione e aggiornamento**. Per prima cosa, i messaggi aggiunti a un thread di un agente sono inviati al servizio Mem0, che usa un Large Language Model (LLM) per sintetizzare la storia della conversazione ed estrarre nuove memorie. Successivamente, una fase di aggiornamento guidata da un LLM determina se aggiungere, modificare o cancellare queste memorie, archiviandole in uno store ibrido che può includere basi dati vettoriali, grafiche e key-value. Questo sistema supporta anche diversi tipi di memoria e può incorporare memoria a grafo per gestire relazioni tra entità.

#### Cognee

Un altro approccio potente è usare **Cognee**, una memoria semantica open-source per agenti AI che trasforma dati strutturati e non strutturati in grafi della conoscenza interrogabili supportati da embeddings. Cognee fornisce un’**architettura dual-store** che combina la ricerca di similarità vettoriale con relazioni grafiche, permettendo agli agenti di comprendere non solo quali informazioni sono simili, ma come i concetti sono collegati tra loro.

Eccelle nel **recupero ibrido** che fonde similarità vettoriale, struttura grafica e ragionamento LLM — dalla semplice ricerca per chunk grezzo alla risposta a domande consapevole del grafo. Il sistema mantiene una **memoria viva** che evolve e cresce pur rimanendo interrogabile come un unico grafo connesso, supportando sia il contesto di sessioni a breve termine che la memoria persistente a lungo termine.

Il tutorial in notebook di Cognee ([13-agent-memory-cognee.ipynb](./13-agent-memory-cognee.ipynb)) dimostra la costruzione di questo strato unificato di memoria, con esempi pratici di ingestione di fonti dati diverse, visualizzazione del grafo della conoscenza e interrogazione con diverse strategie di ricerca adattate ai bisogni specifici dell’agente.

### Archiviazione della Memoria con RAG

Oltre a strumenti di memoria specializzati come Mem0, puoi sfruttare servizi di ricerca robusti come **Azure AI Search come backend per archiviare e recuperare memorie**, specialmente per RAG strutturato.

Questo ti permette di ancorare le risposte del tuo agente ai tuoi dati, garantendo risposte più rilevanti e accurate. Azure AI Search può essere usato per archiviare memorie di viaggio specifiche utente, cataloghi prodotti o qualsivoglia conoscenza specifica di dominio.

Azure AI Search supporta funzionalità come **RAG Strutturato**, che eccelle nell’estrazione e recupero di informazioni dense e strutturate da grandi dataset come cronologie conversazioni, email o persino immagini. Questo fornisce una "precisione e richiamo superumani" rispetto a metodi tradizionali di chunking e embedding di testo.

## Rendere gli Agenti AI Autolegittimanti

Un modello comune per agenti autolegittimanti comporta l’introduzione di un **“agente della conoscenza”**. Questo agente separato osserva la conversazione principale tra l’utente e l’agente primario. Il suo ruolo è:

1. **Identificare informazioni preziose**: Determinare se una parte della conversazione vale la pena di essere salvata come conoscenza generale o come preferenza specifica dell’utente.

2. **Estrarre e sintetizzare**: Distillare l’apprendimento essenziale o la preferenza dalla conversazione.

3. **Archiviare in una base di conoscenza**: Conservare queste informazioni estratte, spesso in un database vettoriale, così che possano essere recuperate in seguito.

4. **Arricchire query future**: Quando l’utente avvia una nuova query, l’agente della conoscenza recupera informazioni memorizzate rilevanti e le aggiunge al prompt dell’utente, fornendo un contesto cruciale all’agente primario (simile a RAG).

### Ottimizzazioni per la Memoria

• **Gestione della latenza**: Per evitare di rallentare le interazioni utente, si può usare inizialmente un modello più economico e veloce per verificare rapidamente se un’informazione è preziosa da archiviare o recuperare, invocando il processo più complesso di estrazione/recupero solo quando necessario.

• **Manutenzione della base di conoscenza**: Per una base di conoscenza in crescita, le informazioni meno usate possono essere spostate in “cold storage” per gestire i costi.

## Hai altre domande sulla memoria degli agenti?

Unisciti al [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D) per incontrare altri studenti, partecipare a ore d’ufficio e far rispondere le tue domande sugli Agenti AI.
## Lezione Precedente

[Ingegneria del Contesto per Agenti AI](../12-context-engineering/README.md)

## Lezione Successiva

[Esplorando Microsoft Agent Framework](../14-microsoft-agent-framework/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:
Questo documento è stato tradotto utilizzando il servizio di traduzione AI [Co-op Translator](https://github.com/Azure/co-op-translator). Sebbene ci impegniamo per garantire la precisione, si prega di notare che le traduzioni automatizzate possono contenere errori o imprecisioni. Il documento originale nella sua lingua nativa deve essere considerato la fonte autorevole. Per informazioni critiche, si raccomanda una traduzione professionale effettuata da un essere umano. Non siamo responsabili per eventuali malintesi o interpretazioni errate derivanti dall’uso di questa traduzione.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->