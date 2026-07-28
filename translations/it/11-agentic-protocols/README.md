# Uso dei Protocolli Agenti (MCP, A2A e NLWeb)

[![Agentic Protocols](../../../translated_images/it/lesson-11-thumbnail.b6c742949cf1ce2a.webp)](https://youtu.be/X-Dh9R3Opn8)

> _(Clicca sull'immagine sopra per vedere il video di questa lezione)_

Con l'aumento dell'uso degli agenti AI, cresce anche la necessità di protocolli che garantiscano standardizzazione, sicurezza e supportino l’innovazione aperta. In questa lezione, copriremo 3 protocolli che mirano a soddisfare questa esigenza - Model Context Protocol (MCP), Agent to Agent (A2A) e Natural Language Web (NLWeb).

## Introduzione

In questa lezione, tratteremo:

• Come **MCP** consente agli Agenti AI di accedere a strumenti e dati esterni per completare i compiti degli utenti.

• Come **A2A** abilita la comunicazione e la collaborazione tra diversi agenti AI.

• Come **NLWeb** porta interfacce in linguaggio naturale a qualsiasi sito web permettendo agli Agenti AI di scoprire e interagire con i contenuti.

## Obiettivi di Apprendimento

• **Identificare** lo scopo principale e i benefici di MCP, A2A e NLWeb nel contesto degli agenti AI.

• **Spiegare** come ciascun protocollo facilita la comunicazione e l’interazione tra LLM, strumenti e altri agenti.

• **Riconoscere** i distinti ruoli che ogni protocollo svolge nella costruzione di sistemi agentici complessi.

## Model Context Protocol

Il **Model Context Protocol (MCP)** è uno standard aperto che fornisce un modo standardizzato per le applicazioni di fornire contesto e strumenti agli LLM. Questo consente un "adattatore universale" per diverse fonti di dati e strumenti a cui gli Agenti AI possono connettersi in modo coerente.

Esaminiamo i componenti di MCP, i benefici rispetto all'uso diretto delle API, e un esempio di come gli agenti AI potrebbero usare un server MCP.

### Componenti Core di MCP

MCP opera su un’**architettura client-server** e i componenti principali sono:

• **Host** sono applicazioni LLM (per esempio un editor di codice come VSCode) che avviano le connessioni a un server MCP.

• **Client** sono componenti all’interno dell’applicazione host che mantengono connessioni uno a uno con i server.

• **Server** sono programmi leggeri che espongono capacità specifiche.

Inclusi nel protocollo ci sono tre primitive core che rappresentano le capacità di un server MCP:

• **Strumenti**: Azioni o funzioni discrete che un agente AI può chiamare per eseguire un’azione. Ad esempio, un servizio meteorologico potrebbe esporre lo strumento "get weather", o un server e-commerce lo strumento "purchase product". I server MCP pubblicizzano il nome, la descrizione e lo schema input/output di ogni strumento nella loro lista di capacità.

• **Risorse**: Sono elementi dati o documenti in sola lettura che un server MCP può fornire e che i client possono recuperare su richiesta. Esempi includono contenuti di file, record di database o file di log. Le risorse possono essere testuali (come codice o JSON) o binarie (come immagini o PDF).

• **Prompt**: Sono modelli predefiniti che offrono suggerimenti di prompt, permettendo flussi di lavoro più complessi.

### Benefici di MCP

MCP offre vantaggi significativi per gli Agenti AI:

• **Scoperta Dinamica degli Strumenti**: Gli agenti possono ricevere dinamicamente una lista degli strumenti disponibili da un server insieme alle descrizioni delle loro funzioni. Questo contrasta con le API tradizionali, che spesso richiedono codifica statica per integrazioni, quindi ogni cambiamento dell’API necessita aggiornamenti di codice. MCP offre un approccio "integra una volta", portando a maggiore adattabilità.

• **Interoperabilità tra LLM**: MCP funziona attraverso diversi LLM, offrendo flessibilità nello switch tra modelli core per valutare le migliori prestazioni.

• **Sicurezza Standardizzata**: MCP include un metodo standard di autenticazione, migliorando la scalabilità nell’aggiunta di accesso a server MCP aggiuntivi. È più semplice rispetto alla gestione di chiavi e tipi di autenticazione differenti per varie API tradizionali.

### Esempio MCP

![MCP Diagram](../../../translated_images/it/mcp-diagram.e4ca1cbd551444a1.webp)

Immagina che un utente voglia prenotare un volo usando un assistente AI alimentato da MCP.

1. **Connessione**: L’assistente AI (client MCP) si connette a un server MCP fornito da una compagnia aerea.

2. **Scoperta Strumenti**: Il client chiede al server MCP della compagnia aerea, "Quali strumenti hai disponibili?" Il server risponde con strumenti come "search flights" e "book flights".

3. **Invocazione Strumenti**: Poi si chiede all’assistente AI, "Per favore cerca un volo da Portland a Honolulu." L’assistente AI, usando il suo LLM, identifica che deve chiamare lo strumento "search flights" e passa i parametri rilevanti (origine, destinazione) al server MCP.

4. **Esecuzione e Risposta**: Il server MCP, agendo come wrapper, fa la chiamata reale all’API interna di prenotazione della compagnia aerea. Poi riceve l’informazione sul volo (es. dati JSON) e la invia all’assistente AI.

5. **Ulteriore Interazione**: L’assistente AI presenta le opzioni di volo. Una volta che l’utente seleziona un volo, l’assistente potrebbe invocare lo strumento "book flight" sullo stesso server MCP, completando la prenotazione.

## Protocollo Agente-a-Agente (A2A)

Mentre MCP si concentra sulla connessione tra LLM e strumenti, il **protocollo Agent-to-Agent (A2A)** va oltre abilitando la comunicazione e la collaborazione tra diversi agenti AI. A2A collega agenti AI attraverso diverse organizzazioni, ambienti e stack tecnologici per completare un compito condiviso.

Esamineremo i componenti e i benefici di A2A, insieme a un esempio di come potrebbe essere applicato nella nostra applicazione di viaggio.

### Componenti Core di A2A

A2A si concentra sull’abilitare la comunicazione tra agenti e farli lavorare insieme per completare un sotto-compito dell’utente. Ciascun componente del protocollo contribuisce a questo:

#### Agent Card

Simile a come un server MCP condivide una lista di strumenti, una Agent Card ha:
- Il Nome dell’Agente.
- Una **descrizione dei compiti generali** che completa.
- Una **lista di abilità specifiche** con descrizioni per aiutare altri agenti (o anche utenti umani) a capire quando e perché vorrebbero chiamare quell’agente.
- L’**URL Endpoint attuale** dell’agente.
- La **versione** e le **capacità** dell’agente, come risposte in streaming e notifiche push.

#### Agent Executor

L’Agent Executor è responsabile di **passare il contesto della chat utente all’agente remoto**, l’agente remoto ne ha bisogno per capire il compito da completare. In un server A2A, un agente usa il proprio Large Language Model (LLM) per interpretare le richieste in arrivo ed eseguire compiti usando i propri strumenti interni.

#### Artefatto

Una volta che un agente remoto ha completato il compito richiesto, il suo prodotto di lavoro viene creato come un artefatto. Un artefatto **contiene il risultato del lavoro dell’agente**, una **descrizione di ciò che è stato completato** e il **contesto testuale** trasmesso tramite il protocollo. Dopo l’invio dell’artefatto, la connessione con l’agente remoto viene chiusa fino a quando non è nuovamente necessaria.

#### Event Queue

Questo componente è usato per **gestire aggiornamenti e passare messaggi**. È particolarmente importante in produzione per sistemi agentici per evitare che la connessione tra agenti venga chiusa prima del completamento di un compito, soprattutto quando i tempi di completamento possono essere lunghi.

### Benefici di A2A

• **Collaborazione Migliorata**: Permette a agenti di diversi fornitori e piattaforme di interagire, condividere contesto e lavorare insieme, facilitando un’automazione fluida tra sistemi tradizionalmente disconnessi.

• **Flessibilità di Selezione del Modello**: Ogni agente A2A può decidere quale LLM utilizzare per gestire le sue richieste, consentendo modelli ottimizzati o affinati per agente, a differenza di una singola connessione LLM in alcuni scenari MCP.

• **Autenticazione Integrata**: L’autenticazione è integrata direttamente nel protocollo A2A, fornendo un robusto quadro di sicurezza per le interazioni tra agenti.

### Esempio A2A

![A2A Diagram](../../../translated_images/it/A2A-Diagram.8666928d648acc26.webp)

Espandiamo lo scenario di prenotazione viaggio, ma questa volta usando A2A.

1. **Richiesta Utente a Multi-Agente**: Un utente interagisce con un "Agente di Viaggio", client/agente A2A, magari dicendo, "Per favore prenota un viaggio completo a Honolulu per la prossima settimana, includendo voli, hotel e noleggio auto".

2. **Orchestrazione dall’Agente di Viaggio**: L’Agente di Viaggio riceve questa richiesta complessa. Usa il suo LLM per ragionare sul compito e determina che deve interagire con altri agenti specializzati.

3. **Comunicazione tra Agenti**: L’Agente di Viaggio usa quindi il protocollo A2A per connettersi con agenti a valle, come un "Agente Compagnia Aerea", un "Agente Hotel" e un "Agente Noleggio Auto" creati da diverse compagnie.

4. **Esecuzione Delegata del Compito**: L’Agente di Viaggio invia compiti specifici a questi agenti specializzati (es., "Trova voli per Honolulu", "Prenota un hotel", "Noleggia un’auto"). Ognuno di questi agenti specializzati, usando propri LLM e strumenti (che potrebbero essere a loro volta server MCP), esegue la propria parte specifica della prenotazione.

5. **Risposta Consolidata**: Una volta che tutti gli agenti a valle completano i loro compiti, l’Agente di Viaggio compila i risultati (dettagli volo, conferma hotel, prenotazione noleggio auto) e invia una risposta completa in stile chat all’utente.

## Natural Language Web (NLWeb)

I siti web sono da tempo il modo principale con cui gli utenti accedono a informazioni e dati attraverso internet.

Vediamo i diversi componenti di NLWeb, i benefici di NLWeb e un esempio di come funziona il nostro NLWeb esaminando la nostra applicazione di viaggio.

### Componenti di NLWeb

- **Applicazione NLWeb (Codice Servizio Core)**: Il sistema che elabora domande in linguaggio naturale. Connette le diverse parti della piattaforma per creare risposte. Puoi pensarlo come il **motore che alimenta le funzionalità in linguaggio naturale** di un sito web.

- **Protocollo NLWeb**: Questo è un **set base di regole per l’interazione in linguaggio naturale** con un sito web. Invia risposte in formato JSON (spesso usando Schema.org). Il suo scopo è creare una base semplice per il “Web AI,” nello stesso modo in cui HTML ha reso possibile condividere documenti online.

- **Server MCP (Endpoint Model Context Protocol)**: Ogni configurazione NLWeb funziona anche come **server MCP**. Ciò significa che può **condividere strumenti (come un metodo “ask”) e dati** con altri sistemi AI. In pratica, questo rende i contenuti e le capacità del sito web utilizzabili da agenti AI, permettendo al sito di diventare parte dell’"ecosistema agenti" più ampio.

- **Modelli di Embedding**: Questi modelli sono usati per **convertire i contenuti del sito web in rappresentazioni numeriche chiamate vettori** (embedding). Questi vettori catturano il significato in modo che i computer possano confrontare e cercare. Sono memorizzati in un database speciale, e gli utenti possono scegliere quale modello embedding usare.

- **Database Vettoriale (Meccanismo di Recupero)**: Questo database **memorizza gli embedding del contenuto del sito web**. Quando qualcuno fa una domanda, NLWeb controlla il database vettoriale per trovare rapidamente le informazioni più rilevanti. Offre una lista veloce di possibili risposte ordinate per similarità. NLWeb funziona con diversi sistemi di archiviazione vettoriale come Qdrant, Snowflake, Milvus, Azure AI Search e Elasticsearch.

### NLWeb con un Esempio

![NLWeb](../../../translated_images/it/nlweb-diagram.c1e2390b310e5fe4.webp)

Considera di nuovo il nostro sito di prenotazioni di viaggio, ma questa volta alimentato da NLWeb.

1. **Ingestione Dati**: I cataloghi di prodotti esistenti del sito di viaggio (es., elenchi voli, descrizioni hotel, pacchetti tour) sono formattati usando Schema.org o caricati tramite feed RSS. Gli strumenti di NLWeb ingeriscono questi dati strutturati, creano embedding e li archiviano in un database vettoriale locale o remoto.

2. **Query in Linguaggio Naturale (Umano)**: Un utente visita il sito web e, invece di navigare i menu, digita in un’interfaccia chat: "Trova un hotel per famiglie a Honolulu con piscina per la prossima settimana".

3. **Elaborazione NLWeb**: L’applicazione NLWeb riceve questa query. La invia a un LLM per la comprensione e contemporaneamente cerca nel suo database vettoriale le liste di hotel rilevanti.

4. **Risultati Precisi**: L’LLM aiuta a interpretare i risultati di ricerca dal database, identificare le migliori corrispondenze basate sui criteri "family-friendly," "piscina," e "Honolulu," e quindi formatta una risposta in linguaggio naturale. Fondamentale, la risposta si riferisce a hotel reali dal catalogo del sito, evitando informazioni inventate.

5. **Interazione con Agente AI**: Poiché NLWeb funziona come server MCP, un agente di viaggio AI esterno potrebbe anche connettersi all’istanza NLWeb di questo sito. L’agente AI potrebbe quindi usare il metodo `ask` MCP per interrogare direttamente il sito: `ask("Ci sono ristoranti vegani consigliati dall’hotel nell’area di Honolulu?")`. L’istanza NLWeb elaborerebbe questo, sfruttando il suo database di informazioni sui ristoranti (se caricato), e restituirebbe una risposta JSON strutturata.

### Hai altre domande su MCP/A2A/NLWeb?

Unisciti al [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D) per incontrare altri studenti, partecipare a ore di ufficio e far rispondere le tue domande sugli Agenti AI.

## Risorse

- [MCP per Principianti](https://aka.ms/mcp-for-beginners)  
- [Documentazione MCP](https://learn.microsoft.com/python/api/overview/azure/ai-projects-readme)
- [Repo NLWeb](https://github.com/nlweb-ai/NLWeb)
- [Microsoft Agent Framework](https://aka.ms/ai-agents-beginners/agent-framework)

## Lezione Precedente

[Agenti AI in Produzione](../10-ai-agents-production/README.md)

## Lezione Successiva

[Ingegneria del Contesto per Agenti AI](../12-context-engineering/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:
Questo documento è stato tradotto utilizzando il servizio di traduzione AI [Co-op Translator](https://github.com/Azure/co-op-translator). Sebbene ci impegniamo per garantire la precisione, si prega di notare che le traduzioni automatizzate possono contenere errori o imprecisioni. Il documento originale nella sua lingua nativa deve essere considerato la fonte autorevole. Per informazioni critiche, si raccomanda una traduzione professionale effettuata da un essere umano. Non siamo responsabili per eventuali malintesi o interpretazioni errate derivanti dall’uso di questa traduzione.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->