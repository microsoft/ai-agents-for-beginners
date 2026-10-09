# Utilizzo dei Protocolli Agentici (MCP, A2A e NLWeb)

[![Protocolli Agentici](../../../translated_images/it/lesson-11-thumbnail.b6c742949cf1ce2a.webp)](https://youtu.be/X-Dh9R3Opn8)

> _(Clicca sull'immagine sopra per vedere il video di questa lezione)_

Con l'aumento dell'uso degli agenti AI, cresce anche la necessità di protocolli che garantiscano standardizzazione, sicurezza e supportino l'innovazione aperta. In questa lezione, tratteremo 3 protocolli che cercano di soddisfare questa esigenza - Model Context Protocol (MCP), Agent to Agent (A2A) e Natural Language Web (NLWeb).

## Introduzione

In questa lezione, tratteremo:

• Come **MCP** permette agli Agenti AI di accedere a strumenti esterni e dati per completare le attività dell'utente.

• Come **A2A** abilita la comunicazione e la collaborazione tra diversi agenti AI.

• Come **NLWeb** porta interfacce in linguaggio naturale a qualsiasi sito web permettendo agli Agenti AI di scoprire e interagire con il contenuto.

## Obiettivi di Apprendimento

• **Identificare** lo scopo principale e i benefici di MCP, A2A e NLWeb nel contesto degli agenti AI.

• **Spiegare** come ciascun protocollo faciliti la comunicazione e l'interazione tra LLM, strumenti e altri agenti.

• **Riconoscere** i ruoli distinti che ciascun protocollo svolge nella costruzione di sistemi agentici complessi.

## Model Context Protocol

Il **Model Context Protocol (MCP)** è uno standard aperto che fornisce un modo standardizzato per le applicazioni di fornire contesto e strumenti agli LLM. Questo abilita un "adattatore universale" a diverse fonti di dati e strumenti a cui gli Agenti AI possono connettersi in modo coerente.

Vediamo i componenti di MCP, i benefici rispetto all'uso diretto delle API e un esempio di come gli agenti AI potrebbero utilizzare un server MCP.

### Componenti Core di MCP

MCP opera su un'**architettura client-server** e i componenti core sono:

• **Host** sono applicazioni LLM (ad esempio un editor di codice come VSCode) che avviano le connessioni a un Server MCP.

• **Client** sono componenti all'interno dell'applicazione host che mantengono connessioni uno a uno con i server.

• **Server** sono programmi leggeri che espongono capacità specifiche.

Incluse nel protocollo ci sono tre primitive core che sono le capacità di un Server MCP:

• **Strumenti**: Sono azioni o funzioni discrete che un agente AI può chiamare per svolgere un'azione. Ad esempio, un servizio meteo potrebbe esporre uno strumento "ottieni meteo", o un server e-commerce potrebbe esporre uno strumento "acquista prodotto". I server MCP pubblicizzano il nome di ogni strumento, la descrizione e lo schema input/output nella loro lista di capacità.

• **Risorse**: Sono elementi di dati di sola lettura o documenti che un server MCP può fornire, e che i client possono recuperare su richiesta. Esempi includono contenuti di file, record di database o file di log. Le risorse possono essere testo (come codice o JSON) o binarie (come immagini o PDF).

• **Prompt**: Sono modelli predefiniti che forniscono suggerimenti di prompt, permettendo flussi di lavoro più complessi.

### Benefici di MCP

MCP offre vantaggi significativi per gli Agenti AI:

• **Scoperta Dinamica degli Strumenti**: Gli agenti possono ricevere dinamicamente una lista di strumenti disponibili da un server insieme a descrizioni di cosa fanno. Questo contrasta con le API tradizionali, che spesso richiedono codifica statica per integrazioni, significando che ogni cambiamento dell'API necessita aggiornamenti di codice. MCP offre un approccio "integra una volta", portando a una maggiore adattabilità.

• **Interoperabilità tra LLM**: MCP funziona con diversi LLM, fornendo flessibilità per cambiare modelli core per ottenere migliori prestazioni.

• **Sicurezza Standardizzata**: MCP include un metodo standard di autenticazione, migliorando la scalabilità quando si aggiunge accesso a ulteriori server MCP. Questo è più semplice che gestire diverse chiavi e tipi di autenticazione per varie API tradizionali.

### Esempio MCP

![Diagramma MCP](../../../translated_images/it/mcp-diagram.e4ca1cbd551444a1.webp)

Immagina che un utente voglia prenotare un volo usando un assistente AI alimentato da MCP.

1. **Connessione**: L'assistente AI (il client MCP) si connette a un server MCP fornito da una compagnia aerea.

2. **Scoperta degli Strumenti**: Il client chiede al server MCP della compagnia aerea: "Quali strumenti avete disponibili?" Il server risponde con strumenti come "cerca voli" e "prenota voli".

3. **Invocazione dello Strumento**: Poi chiedi all'assistente AI, "Per favore cerca un volo da Portland a Honolulu." L'assistente AI, usando il suo LLM, identifica che deve chiamare lo strumento "cerca voli" e passa i parametri rilevanti (origine, destinazione) al server MCP.

4. **Esecuzione e Risposta**: Il server MCP, agendo come wrapper, effettua la chiamata reale all'API interna di prenotazione della compagnia aerea. Riceve poi le informazioni sul volo (es. dati JSON) e le invia all'assistente AI.

5. **Ulteriore Interazione**: L'assistente AI presenta le opzioni di volo. Una volta selezionato un volo, l'assistente potrebbe invocare lo strumento "prenota volo" sullo stesso server MCP, completando la prenotazione.

## Protocollo Agente-a-Agente (A2A)

Mentre MCP si concentra sul collegare LLM a strumenti, il **protocollo Agent-to-Agent (A2A)** fa un passo avanti abilitando la comunicazione e la collaborazione tra diversi agenti AI. A2A connette agenti AI attraverso diverse organizzazioni, ambienti e stack tecnologici per completare un compito condiviso.

Esamineremo i componenti e i benefici di A2A, insieme a un esempio di come potrebbe essere applicato nella nostra applicazione di viaggi.

### Componenti Core di A2A

A2A si concentra sull'abilitare la comunicazione tra agenti e farli collaborare per completare un sottocompito dell'utente. Ogni componente del protocollo contribuisce a questo:

#### Scheda Agente

Simile a come un server MCP condivide una lista di strumenti, una Scheda Agente ha:
- Il Nome dell'Agente.
- Una **descrizione delle attività generali** che completa.
- Una **lista di competenze specifiche** con descrizioni per aiutare altri agenti (o anche utenti umani) a capire quando e perché vorrebbero chiamare quell'agente.
- L'**URL dell'Endpoint attuale** dell'agente.
- La **versione** e le **capacità** dell'agente come risposte in streaming e notifiche push.

#### Esecutore Agente

L'Esecutore Agente è responsabile di **trasmettere il contesto della chat utente all'agente remoto**, che ha bisogno di questo per comprendere il compito da svolgere. In un server A2A, un agente usa il proprio Large Language Model (LLM) per analizzare le richieste in arrivo ed eseguire compiti usando i propri strumenti interni.

#### Artefatto

Una volta che un agente remoto ha completato il compito richiesto, il suo prodotto di lavoro viene creato come artefatto. Un artefatto **contiene il risultato del lavoro dell'agente**, una **descrizione di ciò che è stato completato** e il **contesto testuale** inviato attraverso il protocollo. Dopo l'invio dell'artefatto, la connessione con l'agente remoto viene chiusa finché non è di nuovo necessaria.

#### Coda Eventi

Questo componente è usato per **gestire aggiornamenti e trasmettere messaggi**. È particolarmente importante in produzione per sistemi agentici per evitare che la connessione tra agenti venga chiusa prima che un compito sia completato, specialmente quando i tempi di completamento possono essere lunghi.

### Benefici di A2A

• **Collaborazione Potenziata**: Permette ad agenti di diversi fornitori e piattaforme di interagire, condividere contesto e lavorare insieme, facilitando l'automazione fluida tra sistemi tradizionalmente disconnessi.

• **Flessibilità nella Selezione del Modello**: Ogni agente A2A può decidere quale LLM usare per soddisfare le sue richieste, permettendo modelli ottimizzati o specializzati per agente, a differenza di una singola connessione LLM in alcuni scenari MCP.

• **Autenticazione Integrata**: L'autenticazione è integrata direttamente nel protocollo A2A, fornendo un robusto framework di sicurezza per le interazioni tra agenti.

### Esempio A2A

![Diagramma A2A](../../../translated_images/it/A2A-Diagram.8666928d648acc26.webp)

Espandiamo il nostro scenario di prenotazione viaggi, ma questa volta usando A2A.

1. **Richiesta dell'Utente a Multi-Agente**: Un utente interagisce con un cliente/agente "Agente di Viaggi" A2A, magari dicendo: "Per favore prenota un viaggio completo a Honolulu per la prossima settimana, includendo voli, hotel e noleggio auto".

2. **Orchestrazione dall'Agente di Viaggi**: L'Agente di Viaggi riceve questa richiesta complessa. Usa il suo LLM per ragionare sul compito e determinare che deve interagire con altri agenti specializzati.

3. **Comunicazione tra Agenti**: L'Agente di Viaggi usa quindi il protocollo A2A per collegarsi con agenti a valle, come un "Agente Compagnia Aerea", un "Agente Hotel" e un "Agente Noleggio Auto" creati da aziende diverse.

4. **Esecuzione Delegata del Compito**: L'Agente di Viaggi invia compiti specifici a questi agenti specializzati (es. "Trova voli per Honolulu," "Prenota un hotel," "Noleggia un'auto"). Ciascuno di questi agenti specializzati, con i propri LLM e utilizzando i propri strumenti (che potrebbero essere a loro volta server MCP), svolge la sua specifica parte della prenotazione.

5. **Risposta Consolidata**: Una volta che tutti gli agenti a valle completano i loro compiti, l'Agente di Viaggi compila i risultati (dettagli del volo, conferma hotel, prenotazione noleggio auto) e invia una risposta completa in stile chat all'utente.

## Natural Language Web (NLWeb)

I siti web sono stati a lungo il modo principale per gli utenti di accedere a informazioni e dati su Internet.

Diamo un'occhiata ai diversi componenti di NLWeb, ai benefici di NLWeb e a un esempio di come funziona il nostro NLWeb osservando la nostra applicazione di viaggi.

### Componenti di NLWeb

- **Applicazione NLWeb (Codice del Servizio Core)**: Il sistema che elabora domande in linguaggio naturale. Collega le diverse parti della piattaforma per creare risposte. Puoi pensarla come il **motore che alimenta le funzionalità in linguaggio naturale** di un sito web.

- **Protocollo NLWeb**: Questo è un **insieme base di regole per l'interazione in linguaggio naturale** con un sito web. Restituisce risposte in formato JSON (spesso usando Schema.org). Il suo scopo è creare una base semplice per il “Web AI,” allo stesso modo in cui HTML ha reso possibile condividere documenti online.

- **Server MCP (Endpoint Model Context Protocol)**: Ogni configurazione NLWeb funziona anche come **server MCP**. Questo significa che può **condividere strumenti (come un metodo “ask”) e dati** con altri sistemi AI. In pratica, questo rende il contenuto e le capacità del sito utilizzabili dagli agenti AI, permettendo al sito di diventare parte del più ampio “ecosistema agentico.”

- **Modelli di Embedding**: Questi modelli sono usati per **convertire il contenuto del sito web in rappresentazioni numeriche chiamate vettori** (embedding). Questi vettori catturano il significato in un modo che i computer possono confrontare e cercare. Sono memorizzati in un database speciale, e gli utenti possono scegliere quale modello di embedding vogliono usare.

- **Database Vettoriale (Meccanismo di Recupero)**: Questo database **memorizza gli embedding del contenuto del sito**. Quando qualcuno fa una domanda, NLWeb controlla il database vettoriale per trovare rapidamente le informazioni più rilevanti. Fornisce una lista veloce di possibili risposte, classificate per similarità. NLWeb funziona con diversi sistemi di archiviazione vettoriale come Qdrant, Snowflake, Milvus, Azure AI Search e Elasticsearch.

### NLWeb con un Esempio

![NLWeb](../../../translated_images/it/nlweb-diagram.c1e2390b310e5fe4.webp)

Considera di nuovo il nostro sito web per la prenotazione viaggi, ma questa volta è alimentato da NLWeb.

1. **Ingestione Dati**: I cataloghi prodotto esistenti del sito di viaggi (es. elenchi voli, descrizioni hotel, pacchetti turistici) vengono formattati usando Schema.org o caricati tramite feed RSS. Gli strumenti di NLWeb ingeriscono questi dati strutturati, creano embedding e li memorizzano in un database vettoriale locale o remoto.

2. **Query in Linguaggio Naturale (Umano)**: Un utente visita il sito e, invece di navigare menu, scrive in un'interfaccia chat: "Trova un hotel adatto alle famiglie a Honolulu con piscina per la prossima settimana".

3. **Elaborazione NLWeb**: L'app NLWeb riceve questa richiesta. La invia a un LLM per comprenderla e contemporaneamente cerca nel suo database vettoriale gli elenchi hotel rilevanti.

4. **Risultati Precisi**: L'LLM aiuta a interpretare i risultati della ricerca nel database, identifica le migliori corrispondenze basate sui criteri "adatto alle famiglie," "piscina" e "Honolulu" e poi formatta una risposta in linguaggio naturale. Fondamentale, la risposta si riferisce ad hotel reali dal catalogo del sito, evitando informazioni inventate.

5. **Interazione Agente AI**: Poiché NLWeb funge da server MCP, un agente AI esterno di viaggi può anche collegarsi a questa istanza NLWeb del sito. L'agente AI potrebbe quindi usare il metodo MCP `ask` per interrogare direttamente il sito: `ask("Ci sono ristoranti vegani raccomandati nella zona di Honolulu dall'hotel?")`. L'istanza NLWeb elaborerebbe questo, sfruttando il suo database di informazioni sui ristoranti (se caricato), e restituirebbe una risposta JSON strutturata.

### Hai altre domande su MCP/A2A/NLWeb?

Unisciti al [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D) per incontrare altri studenti, partecipare agli orari di ufficio e ricevere risposte alle tue domande sugli Agenti AI.

## Risorse

- [MCP per Principianti](https://aka.ms/mcp-for-beginners)  
- [Documentazione MCP](https://learn.microsoft.com/python/api/overview/azure/ai-projects-readme)
- [Repository NLWeb](https://github.com/nlweb-ai/NLWeb)
- [Microsoft Agent Framework](https://learn.microsoft.com/en-us/agent-framework/overview/?wt.mc_id=youtube_26688_organicsocial_reactor&pivots=programming-language-python)

## Lezione Precedente

[Agenti AI in Produzione](../10-ai-agents-production/README.md)

## Lezione Successiva

[Context Engineering per Agenti AI](../12-context-engineering/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:
Questo documento è stato tradotto utilizzando il servizio di traduzione AI [Co-op Translator](https://github.com/Azure/co-op-translator). Sebbene ci impegniamo per garantire la precisione, si prega di notare che le traduzioni automatizzate possono contenere errori o imprecisioni. Il documento originale nella sua lingua nativa deve essere considerato la fonte autorevole. Per informazioni critiche, si raccomanda una traduzione professionale effettuata da un essere umano. Non siamo responsabili per eventuali malintesi o interpretazioni errate derivanti dall’uso di questa traduzione.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->