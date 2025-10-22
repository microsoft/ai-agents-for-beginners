<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "aff92c6f019b4627ca9399c6e3882e17",
  "translation_date": "2025-09-18T14:48:20+00:00",
  "source_file": "11-agentic-protocols/README.md",
  "language_code": "it"
}
-->
# Utilizzo dei protocolli agentici (MCP, A2A e NLWeb)

[![Protocolli agentici](../../../translated_images/lesson-11-thumbnail.b6c742949cf1ce2aa0255968d287b31c99b51dfa9c9beaede7c3fbed90e8fcfb.it.png)](https://youtu.be/X-Dh9R3Opn8)

> _(Clicca sull'immagine sopra per vedere il video di questa lezione)_

Con l'aumento dell'uso degli agenti AI, cresce anche la necessità di protocolli che garantiscano standardizzazione, sicurezza e supportino l'innovazione aperta. In questa lezione, tratteremo 3 protocolli che mirano a soddisfare questa esigenza: Model Context Protocol (MCP), Agent to Agent (A2A) e Natural Language Web (NLWeb).

## Introduzione

In questa lezione, vedremo:

• Come **MCP** consente agli agenti AI di accedere a strumenti e dati esterni per completare i compiti degli utenti.

• Come **A2A** abilita la comunicazione e la collaborazione tra diversi agenti AI.

• Come **NLWeb** porta interfacce in linguaggio naturale su qualsiasi sito web, permettendo agli agenti AI di scoprire e interagire con i contenuti.

## Obiettivi di apprendimento

• **Identificare** lo scopo principale e i benefici di MCP, A2A e NLWeb nel contesto degli agenti AI.

• **Spiegare** come ciascun protocollo faciliti la comunicazione e l'interazione tra LLM, strumenti e altri agenti.

• **Riconoscere** i ruoli distinti che ciascun protocollo svolge nella costruzione di sistemi agentici complessi.

## Model Context Protocol

Il **Model Context Protocol (MCP)** è uno standard aperto che fornisce un modo standardizzato per le applicazioni di fornire contesto e strumenti agli LLM. Questo consente un "adattatore universale" per diverse fonti di dati e strumenti che gli agenti AI possono connettere in modo coerente.

Esaminiamo i componenti di MCP, i benefici rispetto all'uso diretto delle API e un esempio di come gli agenti AI potrebbero utilizzare un server MCP.

### Componenti principali di MCP

MCP opera su un'architettura **client-server** e i componenti principali sono:

• **Host**: applicazioni LLM (ad esempio un editor di codice come VSCode) che avviano le connessioni a un server MCP.

• **Client**: componenti all'interno dell'applicazione host che mantengono connessioni uno-a-uno con i server.

• **Server**: programmi leggeri che espongono capacità specifiche.

Il protocollo include tre primitive principali che rappresentano le capacità di un server MCP:

• **Tools**: Azioni o funzioni discrete che un agente AI può chiamare per eseguire un'azione. Ad esempio, un servizio meteo potrebbe offrire uno strumento "get weather", o un server e-commerce potrebbe offrire uno strumento "purchase product". I server MCP pubblicizzano il nome, la descrizione e lo schema di input/output di ciascun tool nella loro lista di capacità.

• **Resources**: Elementi di dati o documenti in sola lettura che un server MCP può fornire e che i client possono recuperare su richiesta. Esempi includono contenuti di file, record di database o file di log. Le risorse possono essere testo (come codice o JSON) o binarie (come immagini o PDF).

• **Prompts**: Modelli predefiniti che forniscono suggerimenti per prompt, consentendo flussi di lavoro più complessi.

### Benefici di MCP

MCP offre vantaggi significativi per gli agenti AI:

• **Scoperta dinamica degli strumenti**: Gli agenti possono ricevere dinamicamente una lista di strumenti disponibili da un server insieme alle descrizioni delle loro funzioni. Questo contrasta con le API tradizionali, che spesso richiedono codifica statica per le integrazioni, il che significa che qualsiasi modifica all'API richiede aggiornamenti al codice. MCP offre un approccio "integra una volta", portando a una maggiore adattabilità.

• **Interoperabilità tra LLM**: MCP funziona con diversi LLM, fornendo flessibilità per cambiare modelli principali e valutare prestazioni migliori.

• **Sicurezza standardizzata**: MCP include un metodo di autenticazione standard, migliorando la scalabilità quando si aggiunge accesso a server MCP aggiuntivi. Questo è più semplice rispetto alla gestione di chiavi e tipi di autenticazione diversi per varie API tradizionali.

### Esempio di MCP

![Diagramma MCP](../../../translated_images/mcp-diagram.e4ca1cbd551444a12e1f0eb300191a036ab01124fce71c864fe9cb7f4ac2a15d.it.png)

Immagina che un utente voglia prenotare un volo utilizzando un assistente AI alimentato da MCP.

1. **Connessione**: L'assistente AI (il client MCP) si connette a un server MCP fornito da una compagnia aerea.

2. **Scoperta degli strumenti**: Il client chiede al server MCP della compagnia aerea: "Quali strumenti hai disponibili?" Il server risponde con strumenti come "search flights" e "book flights".

3. **Invocazione dello strumento**: L'utente chiede all'assistente AI: "Per favore cerca un volo da Portland a Honolulu." L'assistente AI, utilizzando il suo LLM, identifica che deve chiamare lo strumento "search flights" e passa i parametri rilevanti (origine, destinazione) al server MCP.

4. **Esecuzione e risposta**: Il server MCP, agendo come wrapper, effettua la chiamata effettiva all'API interna della compagnia aerea. Riceve quindi le informazioni sul volo (ad esempio dati JSON) e le invia all'assistente AI.

5. **Ulteriore interazione**: L'assistente AI presenta le opzioni di volo. Una volta selezionato un volo, l'assistente potrebbe invocare lo strumento "book flight" sullo stesso server MCP, completando la prenotazione.

## Protocollo Agent-to-Agent (A2A)

Mentre MCP si concentra sulla connessione degli LLM agli strumenti, il **protocollo Agent-to-Agent (A2A)** fa un passo avanti abilitando la comunicazione e la collaborazione tra diversi agenti AI. A2A collega agenti AI di diverse organizzazioni, ambienti e stack tecnologici per completare un compito condiviso.

Esamineremo i componenti e i benefici di A2A, insieme a un esempio di come potrebbe essere applicato nella nostra applicazione di viaggio.

### Componenti principali di A2A

A2A si concentra sull'abilitazione della comunicazione tra agenti e sul farli lavorare insieme per completare un sottocompito dell'utente. Ogni componente del protocollo contribuisce a questo:

#### Scheda dell'agente

Simile a come un server MCP condivide una lista di strumenti, una scheda dell'agente include:
- Il nome dell'agente.
- Una **descrizione dei compiti generali** che svolge.
- Una **lista di competenze specifiche** con descrizioni per aiutare altri agenti (o anche utenti umani) a capire quando e perché chiamare quell'agente.
- L'**URL dell'endpoint corrente** dell'agente.
- La **versione** e le **capacità** dell'agente, come risposte in streaming e notifiche push.

#### Executor dell'agente

L'Executor dell'agente è responsabile di **trasmettere il contesto della chat dell'utente all'agente remoto**, che ha bisogno di questo per comprendere il compito da completare. In un server A2A, un agente utilizza il proprio Large Language Model (LLM) per analizzare le richieste in arrivo ed eseguire compiti utilizzando i propri strumenti interni.

#### Artefatto

Una volta che un agente remoto ha completato il compito richiesto, il prodotto del suo lavoro viene creato come artefatto. Un artefatto **contiene il risultato del lavoro dell'agente**, una **descrizione di ciò che è stato completato** e il **contesto testuale** inviato attraverso il protocollo. Dopo che l'artefatto è stato inviato, la connessione con l'agente remoto viene chiusa fino a quando non è necessaria di nuovo.

#### Coda degli eventi

Questo componente viene utilizzato per **gestire aggiornamenti e trasmettere messaggi**. È particolarmente importante in produzione per sistemi agentici per evitare che la connessione tra agenti venga chiusa prima che un compito sia completato, soprattutto quando i tempi di completamento possono essere più lunghi.

### Benefici di A2A

• **Collaborazione migliorata**: Consente agli agenti di diversi fornitori e piattaforme di interagire, condividere contesto e lavorare insieme, facilitando l'automazione senza soluzione di continuità tra sistemi tradizionalmente disconnessi.

• **Flessibilità nella selezione del modello**: Ogni agente A2A può decidere quale LLM utilizzare per gestire le richieste, permettendo modelli ottimizzati o perfezionati per agente, a differenza di una singola connessione LLM in alcuni scenari MCP.

• **Autenticazione integrata**: L'autenticazione è integrata direttamente nel protocollo A2A, fornendo un robusto framework di sicurezza per le interazioni tra agenti.

### Esempio di A2A

![Diagramma A2A](../../../translated_images/A2A-Diagram.8666928d648acc2687db4093d7b09ea2a595622f8fe18194a026ee55fc23af8e.it.png)

Espandiamo il nostro scenario di prenotazione di viaggio, ma questa volta utilizzando A2A.

1. **Richiesta dell'utente a un multi-agente**: Un utente interagisce con un "Travel Agent" client/agente A2A, forse dicendo: "Per favore prenota un intero viaggio a Honolulu per la prossima settimana, inclusi voli, un hotel e un'auto a noleggio".

2. **Orchestrazione da parte del Travel Agent**: Il Travel Agent riceve questa richiesta complessa. Utilizza il suo LLM per ragionare sul compito e determinare che deve interagire con altri agenti specializzati.

3. **Comunicazione tra agenti**: Il Travel Agent utilizza il protocollo A2A per connettersi ad agenti downstream, come un "Airline Agent", un "Hotel Agent" e un "Car Rental Agent" creati da diverse aziende.

4. **Esecuzione del compito delegato**: Il Travel Agent invia compiti specifici a questi agenti specializzati (ad esempio, "Trova voli per Honolulu", "Prenota un hotel", "Noleggia un'auto"). Ciascuno di questi agenti specializzati, utilizzando i propri LLM e strumenti (che potrebbero essere server MCP stessi), esegue la propria parte della prenotazione.

5. **Risposta consolidata**: Una volta che tutti gli agenti downstream completano i loro compiti, il Travel Agent compila i risultati (dettagli del volo, conferma dell'hotel, prenotazione dell'auto a noleggio) e invia una risposta completa in stile chat all'utente.

## Natural Language Web (NLWeb)

I siti web sono stati a lungo il modo principale per gli utenti di accedere a informazioni e dati su internet.

Esaminiamo i diversi componenti di NLWeb, i benefici di NLWeb e un esempio di come NLWeb funziona guardando la nostra applicazione di viaggio.

### Componenti di NLWeb

- **Applicazione NLWeb (Codice del servizio principale)**: Il sistema che elabora domande in linguaggio naturale. Collega le diverse parti della piattaforma per creare risposte. Puoi pensarlo come il **motore che alimenta le funzionalità in linguaggio naturale** di un sito web.

- **Protocollo NLWeb**: Questo è un **insieme di regole di base per l'interazione in linguaggio naturale** con un sito web. Invia risposte in formato JSON (spesso utilizzando Schema.org). Il suo scopo è creare una base semplice per il "Web AI", nello stesso modo in cui HTML ha reso possibile condividere documenti online.

- **Server MCP (Endpoint del Model Context Protocol)**: Ogni configurazione NLWeb funziona anche come **server MCP**. Questo significa che può **condividere strumenti (come un metodo "ask") e dati** con altri sistemi AI. In pratica, questo rende i contenuti e le capacità del sito utilizzabili dagli agenti AI, permettendo al sito di diventare parte del più ampio "ecosistema agentico".

- **Modelli di embedding**: Questi modelli vengono utilizzati per **convertire i contenuti del sito web in rappresentazioni numeriche chiamate vettori** (embedding). Questi vettori catturano il significato in un modo che i computer possono confrontare e cercare. Vengono archiviati in un database speciale, e gli utenti possono scegliere quale modello di embedding vogliono utilizzare.

- **Database vettoriale (Meccanismo di recupero)**: Questo database **archivia gli embedding dei contenuti del sito web**. Quando qualcuno pone una domanda, NLWeb controlla il database vettoriale per trovare rapidamente le informazioni più pertinenti. Fornisce un elenco veloce di possibili risposte, classificate per somiglianza. NLWeb funziona con diversi sistemi di archiviazione vettoriale come Qdrant, Snowflake, Milvus, Azure AI Search ed Elasticsearch.

### NLWeb per esempio

![NLWeb](../../../translated_images/nlweb-diagram.c1e2390b310e5fe4b245b86690ac6c49c26e355da5ab124128c8675d58cc9b07.it.png)

Consideriamo di nuovo il nostro sito web di prenotazione viaggi, ma questa volta alimentato da NLWeb.

1. **Ingestione dei dati**: I cataloghi di prodotti esistenti del sito di viaggi (ad esempio, elenchi di voli, descrizioni di hotel, pacchetti turistici) vengono formattati utilizzando Schema.org o caricati tramite feed RSS. Gli strumenti di NLWeb ingeriscono questi dati strutturati, creano embedding e li archiviano in un database vettoriale locale o remoto.

2. **Query in linguaggio naturale (umano)**: Un utente visita il sito web e, invece di navigare tra i menu, digita in un'interfaccia chat: "Trova un hotel adatto alle famiglie a Honolulu con una piscina per la prossima settimana".

3. **Elaborazione NLWeb**: L'applicazione NLWeb riceve questa query. La invia a un LLM per la comprensione e contemporaneamente cerca nel suo database vettoriale gli elenchi di hotel pertinenti.

4. **Risultati accurati**: L'LLM aiuta a interpretare i risultati della ricerca dal database, identificare le migliori corrispondenze basate sui criteri "adatto alle famiglie", "piscina" e "Honolulu", e quindi formattare una risposta in linguaggio naturale. Fondamentalmente, la risposta si riferisce a hotel reali dal catalogo del sito, evitando informazioni inventate.

5. **Interazione con agenti AI**: Poiché NLWeb funziona come server MCP, un agente AI esterno per viaggi potrebbe anche connettersi all'istanza NLWeb di questo sito. L'agente AI potrebbe quindi utilizzare il metodo `ask` MCP per interrogare direttamente il sito: `ask("Ci sono ristoranti vegani consigliati nella zona di Honolulu dall'hotel?")`. L'istanza NLWeb elaborerebbe questa richiesta, sfruttando il suo database di informazioni sui ristoranti (se caricato), e restituirebbe una risposta JSON strutturata.

### Hai altre domande su MCP/A2A/NLWeb?

Unisciti al [Discord di Azure AI Foundry](https://aka.ms/ai-agents/discord) per incontrare altri studenti, partecipare a sessioni di domande e risposte e ottenere risposte alle tue domande sugli agenti AI.

## Risorse

- [MCP per principianti](https://aka.ms/mcp-for-beginners)  
- [Documentazione MCP](https://github.com/microsoft/semantic-kernel/tree/main/python/semantic-kernel/semantic_kernel/connectors/mcp)
- [Repo NLWeb](https://github.com/nlweb-ai/NLWeb)
- [Guide Semantic Kernel](https://learn.microsoft.com/semantic-kernel/)

---

**Disclaimer**:  
Questo documento è stato tradotto utilizzando il servizio di traduzione automatica [Co-op Translator](https://github.com/Azure/co-op-translator). Sebbene ci impegniamo per garantire l'accuratezza, si prega di notare che le traduzioni automatiche possono contenere errori o imprecisioni. Il documento originale nella sua lingua nativa dovrebbe essere considerato la fonte autorevole. Per informazioni critiche, si raccomanda una traduzione professionale effettuata da un traduttore umano. Non siamo responsabili per eventuali incomprensioni o interpretazioni errate derivanti dall'uso di questa traduzione.