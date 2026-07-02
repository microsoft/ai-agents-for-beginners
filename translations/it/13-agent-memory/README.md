# Memoria per Agenti AI  
[![Agent Memory](../../../translated_images/it/lesson-13-thumbnail.959e3bc52d210c64.webp)](https://youtu.be/QrYbHesIxpw?si=qNYW6PL3fb3lTPMk)

Quando si parla dei vantaggi unici della creazione di Agenti AI, si discutono principalmente due cose: la capacità di richiamare strumenti per completare compiti e la capacità di migliorare nel tempo. La memoria è alla base della creazione di un agente che si auto-migliora e che può creare esperienze migliori per i nostri utenti.

In questa lezione, vedremo cos'è la memoria per gli Agenti AI e come possiamo gestirla e usarla a beneficio delle nostre applicazioni.

## Introduzione

Questa lezione coprirà:

• **Comprendere la Memoria degli Agenti AI**: Cos'è la memoria e perché è essenziale per gli agenti.

• **Implementare e Memorizzare la Memoria**: Metodi pratici per aggiungere capacità di memoria ai tuoi agenti AI, concentrandosi sulla memoria a breve e lungo termine.

• **Rendere gli Agenti AI Auto-Miglioranti**: Come la memoria permette agli agenti di apprendere dalle interazioni passate e migliorare nel tempo.

## Implementazioni Disponibili

Questa lezione include due tutorial completi in notebook:

• **[13-agent-memory.ipynb](./13-agent-memory.ipynb)**: Implementa la memoria usando Mem0 e Azure AI Search con Microsoft Agent Framework

• **[13-agent-memory-cognee.ipynb](./13-agent-memory-cognee.ipynb)**: Implementa memoria strutturata usando Cognee, costruendo automaticamente un grafo della conoscenza basato su embeddings, visualizzando il grafo e il retrieval intelligente

## Obiettivi di Apprendimento

Dopo aver completato questa lezione, saprai come:

• **Differenziare tra vari tipi di memoria degli agenti AI**, inclusi memoria di lavoro, a breve termine e a lungo termine, così come forme specializzate come la memoria persona ed episodica.

• **Implementare e gestire memoria a breve e lungo termine per agenti AI** usando Microsoft Agent Framework, sfruttando strumenti come Mem0, Cognee, memoria Whiteboard e integrando con Azure AI Search.

• **Comprendere i principi dietro agenti AI auto-miglioranti** e come sistemi robusti di gestione della memoria contribuiscono all’apprendimento e adattamento continui.

## Comprendere la Memoria degli Agenti AI

Alla base, **la memoria per gli agenti AI si riferisce ai meccanismi che consentono loro di trattenere e richiamare informazioni**. Queste informazioni possono essere dettagli specifici su una conversazione, preferenze dell’utente, azioni passate o anche schemi appresi.

Senza memoria, le applicazioni AI sono spesso senza stato, ovvero ogni interazione inizia da zero. Questo porta a un’esperienza utente ripetitiva e frustrante dove l’agente "dimentica" il contesto o le preferenze precedenti.

### Perché la Memoria è Importante?

L’intelligenza di un agente è strettamente legata alla sua capacità di richiamare e utilizzare informazioni passate. La memoria permette agli agenti di essere:

• **Riflessivi**: Imparando da azioni e risultati passati.

• **Interattivi**: Mantenendo il contesto durante una conversazione in corso.

• **Proattivi e Reattivi**: Anticipando necessità o rispondendo appropriatamente basandosi su dati storici.

• **Autonomi**: Operando in modo più indipendente attingendo a conoscenze memorizzate.

L’obiettivo di implementare la memoria è rendere gli agenti più **affidabili e capaci**.

### Tipi di Memoria

#### Memoria di Lavoro

Pensala come un pezzo di carta su cui un agente scrive durante un singolo compito o processo di pensiero in corso. Trattiene le informazioni immediate necessarie per calcolare il prossimo passo.

Per gli agenti AI, la memoria di lavoro spesso cattura le informazioni più rilevanti da una conversazione, anche se la storia completa della chat è lunga o troncata. Si concentra sull’estrazione di elementi chiave come requisiti, proposte, decisioni e azioni.

**Esempio di Memoria di Lavoro**

In un agente per prenotazioni di viaggio, la memoria di lavoro potrebbe catturare la richiesta attuale dell’utente, come "voglio prenotare un viaggio a Parigi". Questo requisito specifico è tenuto nel contesto immediato dell’agente per guidare l’interazione corrente.

#### Memoria a Breve Termine

Questo tipo di memoria trattiene informazioni per la durata di una singola conversazione o sessione. È il contesto della chat attuale, che consente all’agente di fare riferimento ai turni precedenti del dialogo.

Nei campioni Python del [Microsoft Agent Framework](https://github.com/microsoft/agent-framework), corrisponde a `AgentSession`, creato con `agent.create_session()`. La sessione è la memoria a breve termine integrata nel framework: mantiene disponibile il contesto della conversazione finché quella stessa sessione viene riutilizzata, ma quel contesto non viene persistito quando la sessione termina o l’applicazione si riavvia. Usa la memoria a lungo termine per fatti e preferenze che devono sopravvivere tra le sessioni, tipicamente tramite un database, un indice vettoriale o un altro archivio persistente.

**Esempio di Memoria a Breve Termine**

Se un utente chiede, "Quanto costa un volo per Parigi?" e poi aggiunge "E per l’alloggio lì?", la memoria a breve termine assicura che l’agente sappia che "lì" si riferisce a "Parigi" all’interno della stessa conversazione.

#### Memoria a Lungo Termine

Queste sono informazioni che persistono attraverso più conversazioni o sessioni. Permette agli agenti di ricordare preferenze dell’utente, interazioni storiche o conoscenze generali per periodi estesi. Questo è importante per la personalizzazione.

**Esempio di Memoria a Lungo Termine**

Una memoria a lungo termine potrebbe memorizzare che "Ben ama sciare e le attività all’aperto, preferisce il caffè con vista montagna e vuole evitare piste da sci avanzate a causa di un infortunio passato". Queste informazioni, apprese da interazioni precedenti, influenzano le raccomandazioni nelle future sessioni di pianificazione viaggi, rendendole altamente personalizzate.

#### Memoria Persona

Questo tipo specializzato di memoria aiuta un agente a sviluppare una "personalità" o "persona" coerente. Permette all’agente di ricordare dettagli su se stesso o sul ruolo previsto, rendendo le interazioni più fluide e focalizzate.

**Esempio di Memoria Persona**  
Se l’agente di viaggio è progettato per essere un "esperto pianificatore di sci," la memoria persona potrebbe rafforzare questo ruolo, influenzando le risposte per allinearle al tono e alle conoscenze di un esperto.

#### Memoria di Workflow/Episodica

Questa memoria archivia la sequenza di passi che un agente compie durante un compito complesso, inclusi successi e insuccessi. È come ricordare specifici "episodi" o esperienze passate per imparare da esse.

**Esempio di Memoria Episodica**

Se l’agente ha tentato di prenotare un volo specifico ma è fallito per indisponibilità, la memoria episodica potrebbe registrare questo fallimento, permettendo all’agente di provare voli alternativi o informare l’utente sul problema in modo più consapevole durante un tentativo successivo.

#### Memoria di Entità

Ciò comporta l’estrazione e la memorizzazione di entità specifiche (come persone, luoghi o cose) e eventi dalle conversazioni. Permette all’agente di costruire una comprensione strutturata degli elementi chiave discussi.

**Esempio di Memoria di Entità**

Da una conversazione riguardo a un viaggio passato, l’agente potrebbe estrarre "Parigi," "Torre Eiffel," e "cena al ristorante Le Chat Noir" come entità. In un’interazione futura, l’agente potrebbe ricordare "Le Chat Noir" e offrire di fare una nuova prenotazione lì.

#### RAG Strutturato (Retrieval Augmented Generation)

Sebbene RAG sia una tecnica più ampia, il "RAG Strutturato" è evidenziato come una potente tecnologia di memoria. Estrae informazioni dense e strutturate da varie fonti (conversazioni, email, immagini) e le usa per migliorare precisione, richiamo e velocità nelle risposte. Diversamente dal RAG classico che si basa solo sulla similarità semantica, il RAG Strutturato funziona con la struttura intrinseca delle informazioni.

**Esempio di RAG Strutturato**

Invece di limitarsi ad abbinare parole chiave, il RAG Strutturato potrebbe analizzare dettagli di un volo (destinazione, data, ora, compagnia aerea) da una email e memorizzarli in modo strutturato. Questo permette query precise tipo "Quale volo ho prenotato per Parigi martedì?"

## Implementare e Memorizzare la Memoria

Implementare la memoria per agenti AI comporta un processo sistematico di **gestione della memoria**, che include generazione, memorizzazione, recupero, integrazione, aggiornamento e persino "dimenticanza" (o eliminazione) delle informazioni. Il recupero è un aspetto particolarmente cruciale.

### Strumenti Specializzati per la Memoria

#### Mem0

Un modo per memorizzare e gestire la memoria degli agenti è usare strumenti specializzati come Mem0. Mem0 funziona come un livello di memoria persistente, permettendo agli agenti di richiamare interazioni rilevanti, memorizzare preferenze utente e contesto fattuale, e imparare da successi e fallimenti nel tempo. L’idea qui è che gli agenti senza stato diventino con stato.

Funziona attraverso una **pipeline di memoria a due fasi: estrazione e aggiornamento**. Prima, i messaggi aggiunti al thread di un agente sono inviati al servizio Mem0, che utilizza un Large Language Model (LLM) per riassumere la storia della conversazione ed estrarre nuove memorie. Successivamente, una fase di aggiornamento guidata da LLM determina se aggiungere, modificare o cancellare queste memorie, memorizzandole in un archivio dati ibrido che può includere database vettoriali, a grafo e key-value. Questo sistema supporta anche vari tipi di memoria e può incorporare memoria a grafo per gestire le relazioni tra entità.

#### Cognee

Un altro approccio potente è usare **Cognee**, una memoria semantica open-source per agenti AI che trasforma dati strutturati e non strutturati in grafi della conoscenza interrogabili supportati da embeddings. Cognee fornisce un’**architettura dual-store** che combina ricerca per similarità vettoriale con relazioni a grafo, permettendo agli agenti di capire non solo quali informazioni sono simili, ma come i concetti sono collegati tra loro.

Eccelle nel **recupero ibrido** che miscela similarità vettoriale, struttura a grafo e ragionamento LLM — dal semplice lookup di chunk alla risposta a domande consapevole del grafo. Il sistema mantiene una **memoria viva** che evolve e cresce rimanendo interrogabile come un grafo connesso, supportando sia il contesto di sessione a breve termine sia la memoria persistente a lungo termine.

Il tutorial in notebook di Cognee ([13-agent-memory-cognee.ipynb](./13-agent-memory-cognee.ipynb)) dimostra la costruzione di questo livello di memoria unificato, con esempi pratici di ingestione di fonti dati diverse, visualizzazione del grafo della conoscenza e interrogazioni con diverse strategie di ricerca adattate ai bisogni specifici dell’agente.

### Memorizzare la Memoria con RAG

Oltre a strumenti specializzati come mem0, puoi sfruttare servizi di ricerca robusti come **Azure AI Search come backend per memorizzare e recuperare le memorie**, specialmente per RAG strutturato.

Questo ti permette di fondare le risposte del tuo agente sui tuoi dati, garantendo risposte più rilevanti e accurate. Azure AI Search può essere usato per memorizzare ricordi di viaggio specifici per utente, cataloghi di prodotti o qualsiasi altra conoscenza di dominio specifico.

Azure AI Search supporta capacità come il **RAG Strutturato**, che eccelle nell’estrarre e recuperare informazioni dense e strutturate da grandi set di dati come storie di conversazioni, email o perfino immagini. Questo fornisce "precisione e richiamo superumani" rispetto ai tradizionali approcci basati su suddivisione di testo e embedding.

## Rendere gli Agenti AI Auto-Miglioranti

Un modello comune per agenti auto-miglioranti prevede l’introduzione di un **"agente della conoscenza"**. Questo agente separato osserva la conversazione principale tra l’utente e l’agente primario. Il suo ruolo è:

1. **Identificare informazioni preziose**: Determinare se qualche parte della conversazione vale la pena di essere salvata come conoscenza generale o preferenza specifica utente.

2. **Estrarre e riassumere**: Distillare l’apprendimento o la preferenza essenziale dalla conversazione.

3. **Memorizzare in una base di conoscenza**: Conservare queste informazioni estratte, spesso in un database vettoriale, per poterle recuperare in seguito.

4. **Arricchire le query future**: Quando l’utente inizia una nuova query, l’agente della conoscenza recupera le informazioni rilevanti memorizzate e le aggiunge al prompt dell’utente, fornendo contesto cruciale all’agente primario (simile a RAG).

### Ottimizzazioni per la Memoria

• **Gestione della Latenza**: Per evitare di rallentare le interazioni utente, un modello più economico e veloce può essere usato inizialmente per verificare rapidamente se l’informazione vale la pena di essere memorizzata o recuperata, invocando il processo di estrazione/recupero più complesso solo quando necessario.

• **Manutenzione della Base di Conoscenza**: Per una base di conoscenza in crescita, le informazioni meno usate possono essere spostate in "archiviazione fredda" per gestire i costi.

## Hai Altre Domande sulla Memoria degli Agenti?

Unisciti al [Microsoft Foundry Discord](https://aka.ms/ai-agents/discord) per incontrare altri studenti, partecipare a ore di ufficio e ricevere risposte alle tue domande sugli Agenti AI.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:
Questo documento è stato tradotto utilizzando il servizio di traduzione AI [Co-op Translator](https://github.com/Azure/co-op-translator). Sebbene ci impegniamo per garantire la precisione, si prega di notare che le traduzioni automatizzate possono contenere errori o imprecisioni. Il documento originale nella sua lingua nativa deve essere considerato la fonte autorevole. Per informazioni critiche, si raccomanda una traduzione professionale effettuata da un essere umano. Non siamo responsabili per eventuali malintesi o interpretazioni errate derivanti dall’uso di questa traduzione.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->