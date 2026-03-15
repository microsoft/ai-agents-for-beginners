# Utilizzare i protocolli agentici (MCP, A2A e NLWeb)

[![Protocolli agentici](../../../translated_images/it/lesson-11-thumbnail.b6c742949cf1ce2a.webp)](https://youtu.be/X-Dh9R3Opn8)

> _(Fai clic sull'immagine sopra per visualizzare il video di questa lezione)_

Man mano che l'uso degli agenti AI cresce, aumenta anche la necessità di protocolli che garantiscano standardizzazione, sicurezza e supportino l'innovazione aperta. In questa lezione, copriremo 3 protocolli che cercano di soddisfare questa esigenza - Model Context Protocol (MCP), Agent to Agent (A2A) e Natural Language Web (NLWeb).

## Introduzione

In questa lezione tratteremo:

• Come **MCP** permette agli Agenti AI di accedere a strumenti e dati esterni per completare i compiti dell'utente.

• Come **A2A** abilita la comunicazione e la collaborazione tra diversi agenti AI.

• Come **NLWeb** porta interfacce in linguaggio naturale a qualsiasi sito web permettendo agli Agenti AI di scoprire e interagire con i contenuti.

## Obiettivi di apprendimento

• **Individuare** lo scopo principale e i vantaggi di MCP, A2A e NLWeb nel contesto degli agenti AI.

• **Spiegare** come ciascun protocollo facilita la comunicazione e l'interazione tra LLM, strumenti e altri agenti.

• **Riconoscere** i ruoli distinti che ciascun protocollo svolge nella costruzione di sistemi agentici complessi.

## Model Context Protocol

The **Model Context Protocol (MCP)** è uno standard aperto che fornisce un modo standardizzato per le applicazioni di fornire contesto e strumenti agli LLM. Questo abilita un "adattatore universale" a diverse fonti di dati e strumenti a cui gli Agenti AI possono connettersi in modo coerente.

Esaminiamo i componenti di MCP, i vantaggi rispetto all'uso diretto delle API e un esempio di come gli agenti AI potrebbero utilizzare un server MCP.

### MCP Core Components

MCP opera su un'**architettura client-server** e i componenti principali sono:

• **Hosts** sono applicazioni LLM (per esempio un editor di codice come VSCode) che avviano le connessioni a un server MCP.

• **Clients** sono componenti all'interno dell'applicazione host che mantengono connessioni uno-a-uno con i server.

• **Servers** sono programmi leggeri che espongono capacità specifiche.

Nel protocollo sono incluse tre primitive principali che costituiscono le capacità di un server MCP:

• **Tools**: Queste sono azioni discrete o funzioni che un agente AI può chiamare per eseguire un'operazione. Per esempio, un servizio meteo potrebbe esporre uno strumento "get weather", oppure un server di e-commerce potrebbe esporre uno strumento "purchase product". I server MCP pubblicizzano il nome di ogni strumento, la descrizione e lo schema di input/output nella loro lista di capacità.

• **Resources**: Questi sono elementi di dati o documenti in sola lettura che un server MCP può fornire e che i client possono recuperare su richiesta. Esempi includono contenuti di file, record di database o file di log. Le risorse possono essere testo (come codice o JSON) o binarie (come immagini o PDF).

• **Prompts**: Questi sono modelli predefiniti che forniscono prompt suggeriti, permettendo flussi di lavoro più complessi.

### Benefits of MCP

MCP offre importanti vantaggi per gli Agenti AI:

• **Scoperta dinamica degli strumenti**: Gli agenti possono ricevere dinamicamente una lista degli strumenti disponibili da un server insieme a descrizioni di ciò che fanno. Questo contrasta con le API tradizionali, che spesso richiedono integrazioni codificate staticamente, il che significa che ogni modifica all'API richiede aggiornamenti del codice. MCP offre un approccio di "integrare una sola volta", portando a una maggiore adattabilità.

• **Interoperabilità tra LLM**: MCP funziona con diversi LLM, fornendo la flessibilità di cambiare i modelli principali per valutare migliori performance.

• **Sicurezza standardizzata**: MCP include un metodo di autenticazione standard, migliorando la scalabilità quando si aggiunge l'accesso a ulteriori server MCP. Questo è più semplice rispetto alla gestione di chiavi e tipi di autenticazione diversi per varie API tradizionali.

### MCP Example

![Diagramma MCP](../../../translated_images/it/mcp-diagram.e4ca1cbd551444a1.webp)

Immagina che un utente voglia prenotare un volo usando un assistente AI alimentato da MCP.

1. **Connection**: L'assistente AI (il client MCP) si connette a un server MCP fornito da una compagnia aerea.

2. **Tool Discovery**: Il client chiede al server MCP della compagnia aerea: "Quali strumenti avete disponibili?" Il server risponde con strumenti come "search flights" e "book flights".

3. **Tool Invocation**: Poi chiedi all'assistente AI: "Per favore cerca un volo da Portland a Honolulu." L'assistente AI, usando il suo LLM, identifica che deve chiamare lo strumento "search flights" e passa i parametri rilevanti (origine, destinazione) al server MCP.

4. **Execution and Response**: Il server MCP, agendo come wrapper, effettua la chiamata effettiva all'API interna di prenotazione della compagnia aerea. Riceve quindi le informazioni sui voli (es. dati JSON) e le invia indietro all'assistente AI.

5. **Further Interaction**: L'assistente AI presenta le opzioni di volo. Una volta selezionato un volo, l'assistente potrebbe invocare lo strumento "book flight" sullo stesso server MCP, completando la prenotazione.

## Agent-to-Agent Protocol (A2A)

Mentre MCP si concentra sul collegamento degli LLM agli strumenti, il **protocollo Agent-to-Agent (A2A)** va oltre abilitando la comunicazione e la collaborazione tra diversi agenti AI. A2A collega agenti AI attraverso diverse organizzazioni, ambienti e stack tecnologici per completare un compito condiviso.

Esamineremo i componenti e i vantaggi di A2A, insieme a un esempio di come potrebbe essere applicato nella nostra applicazione di viaggio.

### A2A Core Components

A2A si concentra sul permettere la comunicazione tra agenti e farli lavorare insieme per completare un sotto-compito dell'utente. Ogni componente del protocollo contribuisce a questo:

#### Scheda dell'agente

Simile a come un server MCP condivide una lista di strumenti, una Agent Card ha:
- Il nome dell'agente .
- Una **descrizione dei compiti generali** che svolge.
- Una **lista di abilità specifiche** con descrizioni per aiutare altri agenti (o anche utenti umani) a capire quando e perché vorrebbero chiamare quell'agente.
- L'**Endpoint URL corrente** dell'agente
- La **versione** e le **capacità** dell'agente come risposte in streaming e notifiche push.

#### Esecutore dell'agente

L'Esecutore dell'Agente è responsabile di **passare il contesto della chat dell'utente all'agente remoto**, l'agente remoto ha bisogno di questo per comprendere il compito che deve essere completato. In un server A2A, un agente usa il proprio Large Language Model (LLM) per analizzare le richieste in arrivo ed eseguire compiti utilizzando i propri strumenti interni.

#### Artefatto

Una volta che un agente remoto ha completato il compito richiesto, il suo prodotto di lavoro viene creato come artefatto. Un artefatto **contiene il risultato del lavoro dell'agente**, una **descrizione di ciò che è stato completato**, e il **contesto testuale** che viene inviato attraverso il protocollo. Dopo che l'artefatto è stato inviato, la connessione con l'agente remoto viene chiusa fino a quando non è nuovamente necessaria.

#### Coda di eventi

Questo componente viene utilizzato per **gestire aggiornamenti e passare messaggi**. È particolarmente importante in produzione per i sistemi agentici per evitare che la connessione tra agenti venga chiusa prima che un compito sia completato, specialmente quando i tempi di completamento possono essere lunghi.

### Benefits of A2A

• **Collaborazione migliorata**: Consente ad agenti di diversi fornitori e piattaforme di interagire, condividere contesto e collaborare, facilitando l'automazione senza soluzione di continuità attraverso sistemi tradizionalmente disconnessi.

• **Flessibilità nella selezione del modello**: Ogni agente A2A può decidere quale LLM utilizzare per soddisfare le proprie richieste, permettendo modelli ottimizzati o fine-tuned per agente, a differenza di una singola connessione LLM in alcuni scenari MCP.

• **Autenticazione integrata**: L'autenticazione è integrata direttamente nel protocollo A2A, fornendo un robusto framework di sicurezza per le interazioni tra agenti.

### A2A Example

![Diagramma A2A](../../../translated_images/it/A2A-Diagram.8666928d648acc26.webp)

Espandiamo il nostro scenario di prenotazione di viaggio, ma questa volta usando A2A.

1. **User Request to Multi-Agent**: Un utente interagisce con un "Agente di viaggio" A2A client/agent, magari dicendo: "Per favore prenota un viaggio completo per Honolulu per la prossima settimana, includendo voli, hotel e un'auto a noleggio".

2. **Orchestration by Travel Agent**: L'Agente di viaggio riceve questa richiesta complessa. Usa il suo LLM per ragionare sul compito e determinare che deve interagire con altri agenti specializzati.

3. **Inter-Agent Communication**: L'Agente di viaggio utilizza quindi il protocollo A2A per connettersi ad agenti a valle, come un "Agente della compagnia aerea", un "Agente hotel" e un "Agente autonoleggio" creati da diverse aziende.

4. **Delegated Task Execution**: L'Agente di viaggio invia compiti specifici a questi agenti specializzati (es. "Trova voli per Honolulu", "Prenota un hotel", "Noleggia un'auto"). Ciascuno di questi agenti specializzati, eseguendo i propri LLM e utilizzando i propri strumenti (che potrebbero essere essi stessi server MCP), svolge la sua parte specifica della prenotazione.

5. **Consolidated Response**: Una volta che tutti gli agenti a valle completano i loro compiti, l'Agente di viaggio compila i risultati (dettagli del volo, conferma dell'hotel, prenotazione del noleggio auto) e invia una risposta completa in stile chat all'utente.

## Natural Language Web (NLWeb)

I siti web sono da tempo il modo principale per gli utenti di accedere a informazioni e dati su Internet.

Vediamo i diversi componenti di NLWeb, i vantaggi di NLWeb e un esempio di come il nostro NLWeb funziona guardando la nostra applicazione di viaggio.

### Components of NLWeb

- **NLWeb Application (Core Service Code)**: Il sistema che elabora le domande in linguaggio naturale. Collega le diverse parti della piattaforma per creare risposte. Puoi pensarlo come il **motore che alimenta le funzionalità in linguaggio naturale** di un sito web.

- **NLWeb Protocol**: Questo è un **insieme base di regole per l'interazione in linguaggio naturale** con un sito web. Restituisce risposte in formato JSON (spesso usando Schema.org). Il suo scopo è creare una base semplice per il “AI Web”, nello stesso modo in cui HTML ha reso possibile condividere documenti online.

- **MCP Server (Model Context Protocol Endpoint)**: Ogni configurazione NLWeb funziona anche come **server MCP**. Ciò significa che può **condividere strumenti (come un metodo “ask”) e dati** con altri sistemi AI. In pratica, questo rende i contenuti e le capacità del sito web utilizzabili dagli agenti AI, permettendo al sito di diventare parte del più ampio “ecosistema di agenti”.

- **Embedding Models**: Questi modelli vengono utilizzati per **convertire i contenuti del sito web in rappresentazioni numeriche chiamate vettori** (embeddings). Questi vettori catturano il significato in un modo che i computer possono confrontare e cercare. Vengono memorizzati in un database speciale e gli utenti possono scegliere quale modello di embedding vogliono utilizzare.

- **Vector Database (Retrieval Mechanism)**: Questo database **archivia gli embeddings dei contenuti del sito web**. Quando qualcuno pone una domanda, NLWeb controlla il database di vettori per trovare rapidamente le informazioni più rilevanti. Fornisce una lista rapida di possibili risposte, classificate per similarità. NLWeb funziona con diversi sistemi di storage vettoriale come Qdrant, Snowflake, Milvus, Azure AI Search e Elasticsearch.

### NLWeb by Example

![NLWeb](../../../translated_images/it/nlweb-diagram.c1e2390b310e5fe4.webp)

Considera di nuovo il nostro sito di prenotazione viaggi, ma questa volta alimentato da NLWeb.

1. **Data Ingestion**: I cataloghi di prodotti esistenti del sito di viaggio (es. liste di voli, descrizioni degli hotel, pacchetti turistici) vengono formattati usando Schema.org o caricati tramite feed RSS. Gli strumenti di NLWeb acquisiscono questi dati strutturati, creano embeddings e li archiviano in un database vettoriale locale o remoto.

2. **Natural Language Query (Human)**: Un utente visita il sito e, invece di navigare nei menu, digita in un'interfaccia chat: "Trova un hotel adatto alle famiglie a Honolulu con piscina per la prossima settimana".

3. **NLWeb Processing**: L'applicazione NLWeb riceve questa query. Invia la query a un LLM per l'interpretazione e contemporaneamente interroga il suo database vettoriale per le inserzioni di hotel rilevanti.

4. **Accurate Results**: Il LLM aiuta a interpretare i risultati della ricerca dal database, identifica le corrispondenze migliori in base ai criteri "adatto alle famiglie", "piscina" e "Honolulu", e poi formatta una risposta in linguaggio naturale. Fondamentalmente, la risposta fa riferimento ad hotel reali dal catalogo del sito, evitando informazioni inventate.

5. **AI Agent Interaction**: Poiché NLWeb funge da server MCP, anche un agente di viaggio AI esterno potrebbe connettersi all'istanza NLWeb di questo sito. L'agente AI potrebbe quindi usare il metodo MCP `ask` per interrogare direttamente il sito: `ask("Ci sono ristoranti vegani consigliati dall'hotel nella zona di Honolulu?")`. L'istanza NLWeb elaborerebbe questa richiesta, sfruttando il suo database di informazioni sui ristoranti (se caricato), e restituirebbe una risposta strutturata in JSON.

### Hai altre domande su MCP/A2A/NLWeb?

Unisciti al [Discord di Microsoft Foundry](https://aka.ms/ai-agents/discord) per incontrare altri studenti, partecipare alle ore di supporto e far rispondere le tue domande sugli Agenti AI.

## Risorse

- [MCP per principianti](https://aka.ms/mcp-for-beginners)  
- [Documentazione MCP](https://learn.microsoft.com/python/api/overview/azure/ai-projects-readme)
- [Repository NLWeb](https://github.com/nlweb-ai/NLWeb)
- [Framework per agent Microsoft](https://aka.ms/ai-agents-beginners/agent-framewrok)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
Dichiarazione di non responsabilità:
Questo documento è stato tradotto utilizzando il servizio di traduzione automatica Co-op Translator (https://github.com/Azure/co-op-translator). Pur impegnandoci a garantire l'accuratezza, si prega di notare che le traduzioni automatiche possono contenere errori o imprecisioni. Il documento originale nella sua lingua nativa deve essere considerato la fonte autorevole. Per informazioni critiche si consiglia una traduzione professionale eseguita da un traduttore umano. Non ci riteniamo responsabili per eventuali incomprensioni o interpretazioni errate derivanti dall'uso di questa traduzione.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->