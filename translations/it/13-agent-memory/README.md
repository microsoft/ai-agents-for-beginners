<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "1923cf93aba522a5f4a493597112a893",
  "translation_date": "2025-09-18T16:10:22+00:00",
  "source_file": "13-agent-memory/README.md",
  "language_code": "it"
}
-->
# Memoria per Agenti AI

Quando si parla dei vantaggi unici della creazione di Agenti AI, si discutono principalmente due aspetti: la capacità di utilizzare strumenti per completare compiti e la capacità di migliorare nel tempo. La memoria è alla base della creazione di agenti auto-miglioranti che possono offrire esperienze migliori agli utenti.

In questa lezione, esamineremo cos'è la memoria per gli Agenti AI e come possiamo gestirla e utilizzarla a beneficio delle nostre applicazioni.

## Introduzione

Questa lezione coprirà:

• **Comprendere la Memoria degli Agenti AI**: Cos'è la memoria e perché è essenziale per gli agenti.

• **Implementare e Archiviare la Memoria**: Metodi pratici per aggiungere capacità di memoria ai tuoi agenti AI, concentrandosi sulla memoria a breve e lungo termine.

• **Rendere gli Agenti AI Auto-Miglioranti**: Come la memoria consente agli agenti di apprendere dalle interazioni passate e migliorare nel tempo.

## Obiettivi di Apprendimento

Dopo aver completato questa lezione, saprai come:

• **Distinguere tra i diversi tipi di memoria degli agenti AI**, inclusa la memoria di lavoro, a breve termine e a lungo termine, oltre a forme specializzate come la memoria di persona e episodica.

• **Implementare e gestire la memoria a breve e lungo termine per gli agenti AI** utilizzando il framework Semantic Kernel, sfruttando strumenti come Mem0 e la memoria Whiteboard, e integrandoli con Azure AI Search.

• **Comprendere i principi alla base degli agenti AI auto-miglioranti** e come sistemi di gestione della memoria robusti contribuiscano all'apprendimento continuo e all'adattamento.

## Comprendere la Memoria degli Agenti AI

Alla base, **la memoria per gli agenti AI si riferisce ai meccanismi che consentono loro di conservare e richiamare informazioni**. Queste informazioni possono includere dettagli specifici di una conversazione, preferenze dell'utente, azioni passate o modelli appresi.

Senza memoria, le applicazioni AI sono spesso senza stato, il che significa che ogni interazione inizia da zero. Questo porta a un'esperienza utente ripetitiva e frustrante, in cui l'agente "dimentica" il contesto o le preferenze precedenti.

### Perché la Memoria è Importante?

L'intelligenza di un agente è strettamente legata alla sua capacità di richiamare e utilizzare informazioni passate. La memoria consente agli agenti di essere:

• **Riflessivi**: Apprendere dalle azioni e dai risultati passati.

• **Interattivi**: Mantenere il contesto durante una conversazione in corso.

• **Proattivi e Reattivi**: Anticipare bisogni o rispondere in modo appropriato basandosi su dati storici.

• **Autonomi**: Operare in modo più indipendente attingendo a conoscenze archiviate.

L'obiettivo dell'implementazione della memoria è rendere gli agenti più **affidabili e capaci**.

### Tipi di Memoria

#### Memoria di Lavoro

Pensala come un foglio di carta su cui l'agente annota informazioni immediate durante un compito o un processo di pensiero in corso. Contiene le informazioni necessarie per calcolare il passo successivo.

Per gli agenti AI, la memoria di lavoro spesso cattura le informazioni più rilevanti di una conversazione, anche se la cronologia completa della chat è lunga o troncata. Si concentra sull'estrazione di elementi chiave come requisiti, proposte, decisioni e azioni.

**Esempio di Memoria di Lavoro**

In un agente di prenotazione viaggi, la memoria di lavoro potrebbe catturare la richiesta attuale dell'utente, come "Voglio prenotare un viaggio a Parigi". Questo requisito specifico viene mantenuto nel contesto immediato dell'agente per guidare l'interazione corrente.

#### Memoria a Breve Termine

Questo tipo di memoria conserva informazioni per la durata di una singola conversazione o sessione. È il contesto della chat corrente, che consente all'agente di fare riferimento ai turni precedenti del dialogo.

**Esempio di Memoria a Breve Termine**

Se un utente chiede, "Quanto costerebbe un volo per Parigi?" e poi segue con "E l'alloggio lì?", la memoria a breve termine garantisce che l'agente sappia che "lì" si riferisce a "Parigi" all'interno della stessa conversazione.

#### Memoria a Lungo Termine

Questa è l'informazione che persiste attraverso più conversazioni o sessioni. Consente agli agenti di ricordare preferenze dell'utente, interazioni storiche o conoscenze generali per periodi prolungati. Questo è importante per la personalizzazione.

**Esempio di Memoria a Lungo Termine**

Una memoria a lungo termine potrebbe conservare che "Ben ama sciare e le attività all'aperto, preferisce il caffè con vista sulle montagne e vuole evitare piste da sci avanzate a causa di un infortunio passato". Queste informazioni, apprese da interazioni precedenti, influenzano le raccomandazioni nelle future sessioni di pianificazione dei viaggi, rendendole altamente personalizzate.

#### Memoria di Persona

Questo tipo di memoria specializzata aiuta un agente a sviluppare una "personalità" o "persona" coerente. Consente all'agente di ricordare dettagli su se stesso o sul suo ruolo previsto, rendendo le interazioni più fluide e mirate.

**Esempio di Memoria di Persona**

Se l'agente di viaggio è progettato per essere un "esperto di pianificazione sciistica", la memoria di persona potrebbe rafforzare questo ruolo, influenzando le sue risposte per allinearsi al tono e alla conoscenza di un esperto.

#### Memoria Episodica/Workflow

Questa memoria conserva la sequenza di passaggi che un agente compie durante un compito complesso, inclusi successi e fallimenti. È come ricordare specifici "episodi" o esperienze passate per apprendere da essi.

**Esempio di Memoria Episodica**

Se l'agente ha tentato di prenotare un volo specifico ma ha fallito a causa di indisponibilità, la memoria episodica potrebbe registrare questo fallimento, consentendo all'agente di provare voli alternativi o informare l'utente del problema in modo più consapevole durante un tentativo successivo.

#### Memoria di Entità

Questa memoria riguarda l'estrazione e il ricordo di entità specifiche (come persone, luoghi o cose) ed eventi dalle conversazioni. Consente all'agente di costruire una comprensione strutturata degli elementi chiave discussi.

**Esempio di Memoria di Entità**

Da una conversazione su un viaggio passato, l'agente potrebbe estrarre "Parigi", "Torre Eiffel" e "cena al ristorante Le Chat Noir" come entità. In una futura interazione, l'agente potrebbe ricordare "Le Chat Noir" e offrire di effettuare una nuova prenotazione lì.

#### RAG Strutturato (Retrieval Augmented Generation)

Mentre il RAG è una tecnica più ampia, il "RAG Strutturato" è evidenziato come una tecnologia di memoria potente. Estrae informazioni dense e strutturate da varie fonti (conversazioni, email, immagini) e le utilizza per migliorare precisione, richiamo e velocità nelle risposte. A differenza del RAG classico che si basa esclusivamente sulla somiglianza semantica, il RAG Strutturato lavora con la struttura intrinseca delle informazioni.

**Esempio di RAG Strutturato**

Invece di limitarsi a corrispondere parole chiave, il RAG Strutturato potrebbe analizzare i dettagli di un volo (destinazione, data, ora, compagnia aerea) da un'email e archiviarli in modo strutturato. Questo consente query precise come "Quale volo ho prenotato per Parigi martedì?"

## Implementare e Archiviare la Memoria

Implementare la memoria per gli agenti AI implica un processo sistematico di **gestione della memoria**, che include generare, archiviare, recuperare, integrare, aggiornare e persino "dimenticare" (o eliminare) informazioni. Il recupero è un aspetto particolarmente cruciale.

### Strumenti Specializzati per la Memoria

Un modo per archiviare e gestire la memoria degli agenti è utilizzare strumenti specializzati come Mem0. Mem0 funziona come uno strato di memoria persistente, consentendo agli agenti di richiamare interazioni rilevanti, archiviare preferenze dell'utente e contesti fattuali, e apprendere da successi e fallimenti nel tempo. L'idea qui è che gli agenti senza stato si trasformino in agenti con stato.

Funziona attraverso una **pipeline di memoria a due fasi: estrazione e aggiornamento**. Innanzitutto, i messaggi aggiunti al thread di un agente vengono inviati al servizio Mem0, che utilizza un Large Language Model (LLM) per riassumere la cronologia delle conversazioni ed estrarre nuove memorie. Successivamente, una fase di aggiornamento guidata da LLM determina se aggiungere, modificare o eliminare queste memorie, archiviandole in un archivio dati ibrido che può includere database vettoriali, grafici e chiave-valore. Questo sistema supporta anche vari tipi di memoria e può incorporare la memoria grafica per gestire le relazioni tra entità.

### Archiviare la Memoria con RAG

Oltre agli strumenti di memoria specializzati come Mem0, puoi sfruttare servizi di ricerca robusti come **Azure AI Search come backend per archiviare e recuperare memorie**, specialmente per il RAG Strutturato.

Questo consente di basare le risposte dell'agente sui tuoi dati, garantendo risposte più pertinenti e accurate. Azure AI Search può essere utilizzato per archiviare memorie specifiche dell'utente sui viaggi, cataloghi di prodotti o qualsiasi altra conoscenza specifica del dominio.

Azure AI Search supporta funzionalità come **RAG Strutturato**, che eccelle nell'estrazione e nel recupero di informazioni dense e strutturate da grandi dataset come cronologie di conversazioni, email o persino immagini. Questo offre "precisione e richiamo sovrumani" rispetto agli approcci tradizionali di suddivisione del testo e embedding.

## Rendere gli Agenti AI Auto-Miglioranti

Un modello comune per gli agenti auto-miglioranti prevede l'introduzione di un **"agente di conoscenza"**. Questo agente separato osserva la conversazione principale tra l'utente e l'agente primario. Il suo ruolo è:

1. **Identificare informazioni preziose**: Determinare se una parte della conversazione vale la pena di essere salvata come conoscenza generale o preferenza specifica dell'utente.

2. **Estrarre e riassumere**: Distillare l'apprendimento o la preferenza essenziale dalla conversazione.

3. **Archiviare in una base di conoscenza**: Conservare queste informazioni estratte, spesso in un database vettoriale, in modo che possano essere recuperate in seguito.

4. **Arricchire le query future**: Quando l'utente avvia una nuova query, l'agente di conoscenza recupera le informazioni archiviate rilevanti e le aggiunge al prompt dell'utente, fornendo un contesto cruciale all'agente primario (simile al RAG).

### Ottimizzazioni per la Memoria

• **Gestione della Latenza**: Per evitare di rallentare le interazioni con l'utente, può essere utilizzato inizialmente un modello più economico e veloce per verificare rapidamente se le informazioni sono preziose da archiviare o recuperare, invocando solo il processo di estrazione/recupero più complesso quando necessario.

• **Manutenzione della Base di Conoscenza**: Per una base di conoscenza in crescita, le informazioni meno utilizzate possono essere spostate in "archiviazione a freddo" per gestire i costi.

## Hai Altre Domande sull'Ingegneria del Contesto?

Unisciti al [Discord di Azure AI Foundry](https://aka.ms/ai-agents/discord) per incontrare altri studenti, partecipare agli orari di ricevimento e ottenere risposte alle tue domande sugli Agenti AI.

---

**Disclaimer**:  
Questo documento è stato tradotto utilizzando il servizio di traduzione automatica [Co-op Translator](https://github.com/Azure/co-op-translator). Sebbene ci impegniamo per garantire l'accuratezza, si prega di notare che le traduzioni automatiche possono contenere errori o imprecisioni. Il documento originale nella sua lingua nativa dovrebbe essere considerato la fonte autorevole. Per informazioni critiche, si raccomanda una traduzione professionale effettuata da un traduttore umano. Non siamo responsabili per eventuali fraintendimenti o interpretazioni errate derivanti dall'uso di questa traduzione.