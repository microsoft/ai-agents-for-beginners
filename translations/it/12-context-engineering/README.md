# Ingegneria del Contesto per Agenti AI

[![Ingegneria del Contesto](../../../translated_images/it/lesson-12-thumbnail.ed19c94463e774d4.webp)](https://youtu.be/F5zqRV7gEag)

> _(Clicca sull'immagine sopra per vedere il video di questa lezione)_

Comprendere la complessità dell'applicazione per cui stai costruendo un agente AI è importante per realizzarne uno affidabile. Dobbiamo creare Agenti AI che gestiscano efficacemente le informazioni per affrontare bisogni complessi oltre l'ingegneria dei prompt.

In questa lezione, analizzeremo cos'è l'ingegneria del contesto e il suo ruolo nella costruzione di agenti AI.

## Introduzione

Questa lezione coprirà:

• **Cos'è l'Ingegneria del Contesto** e perché è diversa dall'ingegneria dei prompt.

• **Strategie per un'efficace Ingegneria del Contesto**, compreso come scrivere, selezionare, comprimere e isolare le informazioni.

• **Errori Comuni nel Contesto** che possono mandare fuori strada il tuo agente AI e come correggerli.

## Obiettivi di Apprendimento

Dopo aver completato questa lezione, saprai comprendere come:

• **Definire l'ingegneria del contesto** e differenziarla dall'ingegneria dei prompt.

• **Identificare i componenti chiave del contesto** nelle applicazioni di modelli linguistici ampi (LLM).

• **Applicare strategie per scrivere, selezionare, comprimere e isolare il contesto** per migliorare la performance dell'agente.

• **Riconoscere i comuni errori di contesto** come avvelenamento, distrazione, confusione e conflitto, e applicare tecniche di mitigazione.

## Cos'è l'Ingegneria del Contesto?

Per gli Agenti AI, il contesto è ciò che guida la pianificazione di un Agente AI per compiere certe azioni. L'Ingegneria del Contesto è la pratica di assicurarsi che l'Agente AI abbia le informazioni corrette per completare il prossimo passo del compito. La finestra di contesto è limitata in dimensione, quindi come costruttori di agenti dobbiamo sviluppare sistemi e processi per gestire l'aggiunta, la rimozione e la condensazione delle informazioni nella finestra di contesto.

### Ingegneria dei Prompt vs Ingegneria del Contesto

L'ingegneria dei prompt si concentra su un unico set di istruzioni statiche per guidare efficacemente gli Agenti AI con un insieme di regole. L'ingegneria del contesto è la gestione di un set dinamico di informazioni, compreso il prompt iniziale, per garantire che l'Agente AI abbia ciò di cui ha bisogno nel tempo. L'idea principale dell'ingegneria del contesto è rendere questo processo ripetibile e affidabile.

### Tipi di Contesto

[![Tipi di Contesto](../../../translated_images/it/context-types.fc10b8927ee43f06.webp)](https://youtu.be/F5zqRV7gEag)

È importante ricordare che il contesto non è una sola cosa. Le informazioni di cui l'Agente AI ha bisogno possono provenire da diverse fonti ed è compito nostro garantire che l'agente abbia accesso a queste fonti:

I tipi di contesto che un agente AI potrebbe dover gestire includono:

• **Istruzioni:** Sono come le "regole" dell'agente – prompt, messaggi di sistema, esempi few-shot (che mostrano all'AI come fare qualcosa) e descrizioni degli strumenti che può usare. Qui si combina il focus dell'ingegneria dei prompt con l'ingegneria del contesto.

• **Conoscenza:** Comprende fatti, informazioni recuperate da database o memorie a lungo termine accumulate dall'agente. Ciò include l'integrazione di un sistema di Retrieval Augmented Generation (RAG) se un agente necessita accesso a diversi archivi di conoscenze e database.

• **Strumenti:** Sono le definizioni di funzioni esterne, API e server MCP che l'agente può chiamare, insieme al feedback (i risultati) ottenuti dal loro utilizzo.

• **Storico della Conversazione:** Il dialogo in corso con un utente. Col passare del tempo, queste conversazioni diventano più lunghe e complesse, occupando spazio nella finestra di contesto.

• **Preferenze dell'Utente:** Informazioni apprese sui gusti o antipatie di un utente nel tempo. Queste potrebbero essere archiviate e richiamate per prendere decisioni chiave che aiutino l'utente.

## Strategie per un'efficace Ingegneria del Contesto

### Strategie di Pianificazione

[![Best Practice di Ingegneria del Contesto](../../../translated_images/it/best-practices.f4170873dc554f58.webp)](https://youtu.be/F5zqRV7gEag)

Una buona ingegneria del contesto inizia con una buona pianificazione. Ecco un approccio che ti aiuterà a iniziare a pensare a come applicare il concetto di ingegneria del contesto:

1. **Definire Risultati Chiari** - I risultati dei compiti assegnati agli Agenti AI dovrebbero essere ben definiti. Rispondi alla domanda - "Come sarà il mondo quando l'Agente AI avrà completato il suo compito?" In altre parole, quale cambiamento, informazione o risposta l'utente dovrebbe avere dopo aver interagito con l'Agente AI.
2. **Mappare il Contesto** - Una volta definiti i risultati per l'Agente AI, devi rispondere alla domanda "Quali informazioni servono all'Agente AI per completare questo compito?". In questo modo puoi iniziare a mappare il contesto su dove queste informazioni possono essere localizzate.
3. **Creare Pipeline del Contesto** - Ora che sai dove sono le informazioni, devi rispondere alla domanda "Come otterrà queste informazioni l'Agente?". Questo può essere fatto in vari modi, inclusi RAG, uso di server MCP e altri strumenti.

### Strategie Pratiche

La pianificazione è importante, ma una volta che le informazioni iniziano a fluire nella finestra di contesto del nostro agente, abbiamo bisogno di strategie pratiche per gestirle:

#### Gestione del Contesto

Mentre alcune informazioni verranno aggiunte automaticamente alla finestra di contesto, l'ingegneria del contesto riguarda l'assunzione di un ruolo più attivo su queste informazioni, che può essere fatto con alcune strategie:

 1. **Blocnotes dell'Agente**
 Permette a un Agente AI di prendere appunti su informazioni rilevanti riguardanti i compiti correnti e le interazioni con l'utente durante una singola sessione. Questo dovrebbe esistere fuori dalla finestra di contesto, in un file o oggetto in runtime che l'agente può recuperare più tardi durante la sessione se necessario.

 2. **Memorie**
 I blocnotes sono utili per gestire le informazioni al di fuori della finestra di contesto di una singola sessione. Le memorie permettono agli agenti di archiviare e recuperare informazioni rilevanti attraverso più sessioni. Questo può includere riassunti, preferenze dell'utente e feedback per miglioramenti futuri.

 3. **Compressione del Contesto**
  Quando la finestra di contesto cresce e si avvicina al limite, si possono usare tecniche come la sintesi e il trimming. Questo include mantenere solo le informazioni più rilevanti o rimuovere messaggi più vecchi.
  
 4. **Sistemi Multi-Agente**
  Sviluppare un sistema multi-agente è una forma di ingegneria del contesto perché ogni agente ha la sua propria finestra di contesto. Come quel contesto viene condiviso e passato ai diversi agenti è un altro aspetto da pianificare quando si costruiscono questi sistemi.
  
 5. **Ambientazioni Sandbox**
  Se un agente deve eseguire del codice o processare grandi quantità di informazioni in un documento, questo può consumare una larga quantità di token per processare i risultati. Invece di memorizzare tutto nella finestra di contesto, l'agente può usare un ambiente sandbox che esegue il codice e legge solo i risultati e altre informazioni rilevanti.
  
 6. **Oggetti di Stato Runtime**
   Questo avviene creando contenitori di informazioni per gestire situazioni in cui l'Agente deve accedere a certe informazioni. Per un compito complesso, questo permetterebbe all'Agente di memorizzare i risultati di ogni sottocompito passo dopo passo, lasciando il contesto collegato solo a quel sotto-compito specifico.

#### Ispezionare il Contesto

Dopo aver applicato una di queste strategie, vale la pena verificare cosa ha effettivamente ricevuto la chiamata al modello successiva. Una domanda utile per il debug è:

> L'agente ha caricato troppo contesto, il contesto sbagliato o ha perso il contesto di cui aveva bisogno?

Non è necessario registrare prompt grezzi, output degli strumenti o contenuti della memoria per rispondere a questa domanda. In produzione, preferisci piccoli record di ispezione del contesto che catturino conteggi, ID, hash e etichette di policy:

- **Selezione:** Traccia quanti chunk candidati, strumenti o memorie sono stati considerati, quanti sono stati selezionati e quale regola o punteggio ha filtrato gli altri.
- **Compressione:** Registra l'intervallo di origine o l'ID di tracciamento, l'ID del riassunto, una stima del numero di token prima e dopo la compressione, e se il contenuto grezzo è stato escluso dalla chiamata successiva.
- **Isolamento:** Nota quale sotto-compito è stato eseguito in un agente, sessione o sandbox separati, quale riassunto vincolato è stato restituito, e se output di strumenti lunghi sono rimasti fuori dal contesto dell'agente principale.
- **Memoria e RAG:** Conserva gli ID dei documenti recuperati, ID delle memorie, punteggi, ID selezionati e stato di redazione invece del testo completo recuperato.
- **Sicurezza e privacy:** Preferisci hash, ID, bucket di token e etichette di policy al testo sensibile del prompt, argomenti degli strumenti, risultati degli strumenti o corpi di memoria utente.

L'obiettivo non è mantenere più contesto. L'obiettivo è lasciare abbastanza evidenza in modo che uno sviluppatore possa capire quale strategia di contesto è stata applicata e se ha cambiato la chiamata al modello successiva nel modo previsto.

### Esempio di Ingegneria del Contesto

Supponiamo di voler un agente AI che **"Prenoti un viaggio per Parigi."**

• Un agente semplice che usa solo l'ingegneria dei prompt potrebbe rispondere semplicemente: **"Ok, quando vorresti andare a Parigi?"** Ha processato soltanto la tua domanda diretta nel momento in cui è stata posta.

• Un agente che usa le strategie di ingegneria del contesto descritte farebbe molto di più. Prima ancora di rispondere, il suo sistema potrebbe:

  ◦ **Controllare il tuo calendario** per date disponibili (recuperando dati in tempo reale).

 ◦ **Richiamare preferenze di viaggio passate** (dalla memoria a lungo termine) come la compagnia aerea preferita, il budget o se preferisci voli diretti.

 ◦ **Identificare strumenti disponibili** per la prenotazione di voli e hotel.

- Poi, una risposta esempio potrebbe essere:  "Ciao [Il Tuo Nome]! Vedo che sei libero la prima settimana di ottobre. Cerco voli diretti per Parigi su [Compagnia Aerea Preferita] entro il tuo solito budget di [Budget]?" Questa risposta più ricca e consapevole del contesto dimostra il potere dell'ingegneria del contesto.

## Errori Comuni nel Contesto

### Avvelenamento del Contesto

**Cos'è:** Quando una allucinazione (informazione falsa generata dal LLM) o un errore entra nel contesto e viene ripetutamente richiamata, spingendo l'agente a perseguire obiettivi impossibili o a sviluppare strategie insensate.

**Cosa fare:** Implementare **validazione del contesto** e **quarantena**. Validare le informazioni prima che vengano aggiunte alla memoria a lungo termine. Se si rileva un possibile avvelenamento, iniziare nuovi thread di contesto per impedire la diffusione delle informazioni errate.

**Esempio di Prenotazione Viaggio:** Il tuo agente allucina un **volo diretto da un piccolo aeroporto locale a una città internazionale distante** che in realtà non offre voli internazionali. Questo dettaglio del volo inesistente viene salvato nel contesto. Successivamente, quando chiedi all'agente di prenotare, continua a cercare biglietti per questa rotta impossibile, portando a errori ripetuti.

**Soluzione:** Implementare un passaggio che **valida l'esistenza e le rotte del volo tramite un'API in tempo reale** _prima_ di aggiungere il dettaglio del volo al contesto operativo dell'agente. Se la validazione fallisce, l'informazione errata viene "messa in quarantena" e non usata ulteriormente.

### Distrazione del Contesto

**Cos'è:** Quando il contesto diventa così grande che il modello si concentra troppo sulla storia accumulata invece di usare ciò che ha imparato durante l'addestramento, portando ad azioni ripetitive o inutili. I modelli possono cominciare a fare errori anche prima che la finestra di contesto sia piena.

**Cosa fare:** Usare **sintesi del contesto**. Comprimere periodicamente le informazioni accumulate in riassunti più brevi, mantenendo i dettagli importanti e rimuovendo la storia ridondante. Questo aiuta a "resettare" l'attenzione.

**Esempio di Prenotazione Viaggio:** Hai discusso di varie destinazioni da sogno per molto tempo, incluso un racconto dettagliato del tuo viaggio zaino in spalla di due anni fa. Quando chiedi finalmente di **"trovarmi un volo economico per il mese prossimo,"** l'agente si perde nei dettagli vecchi e irrilevanti e continua a chiedere del tuo equipaggiamento o itinerari passati, ignorando la richiesta attuale.

**Soluzione:** Dopo un certo numero di turni o quando il contesto diventa troppo grande, l'agente dovrebbe **riassumere le parti più recenti e rilevanti della conversazione** – concentrandosi sulle date di viaggio e destinazione attuali – e usare quel riassunto condensato per la chiamata successiva al LLM, scartando la chat storica meno rilevante.

### Confusione del Contesto

**Cos'è:** Quando il contesto inutile, spesso sotto forma di troppi strumenti disponibili, fa sì che il modello generi risposte sbagliate o chiami strumenti irrilevanti. I modelli più piccoli sono particolarmente inclini a questo.

**Cosa fare:** Implementare **gestione del carico degli strumenti** usando tecniche RAG. Conservare le descrizioni degli strumenti in un database vettoriale e selezionare _soltanto_ gli strumenti più rilevanti per ogni compito specifico. La ricerca mostra di limitare la selezione degli strumenti a meno di 30.

**Esempio di Prenotazione Viaggio:** Il tuo agente ha accesso a decine di strumenti: `book_flight`, `book_hotel`, `rent_car`, `find_tours`, `currency_converter`, `weather_forecast`, `restaurant_reservations`, ecc. Chiedi, **"Qual è il modo migliore per muoversi a Parigi?"** A causa del numero totale di strumenti, l'agente si confonde e tenta di chiamare `book_flight` _all'interno_ di Parigi, o `rent_car` anche se tu preferisci il trasporto pubblico, perché le descrizioni degli strumenti potrebbero sovrapporsi o semplicemente non riesce a individuare il migliore.

**Soluzione:** Usare **RAG sulle descrizioni degli strumenti**. Quando chiedi come muoverti a Parigi, il sistema recupera dinamicamente _solo_ gli strumenti più rilevanti come `rent_car` o `public_transport_info` basandosi sulla tua domanda, presentando un "carico" focalizzato di strumenti al LLM.

### Conflitto nel Contesto

**Cos'è:** Quando esistono informazioni contraddittorie all'interno del contesto, portando a ragionamenti incoerenti o risposte finali errate. Questo spesso accade quando le informazioni arrivano a fasi, e supposizioni errate iniziali rimangono nel contesto.

**Cosa fare:** Usare **potatura del contesto** e **offloading**. La potatura significa rimuovere informazioni obsolete o contraddittorie man mano che arrivano nuovi dettagli. L'offloading fornisce al modello uno spazio di lavoro "scratchpad" separato per processare le informazioni senza ingombrare il contesto principale.


**Esempio di prenotazione viaggi:** Inizialmente dici al tuo agente, **"Voglio volare in classe economica."** Più tardi nella conversazione, cambi idea e dici, **"In realtà, per questo viaggio, optiamo per la classe business."** Se entrambe le istruzioni rimangono nel contesto, l'agente potrebbe ricevere risultati di ricerca contrastanti o confondersi su quale preferenza dare priorità.

**Soluzione:** Implementare il **contesto di potatura**. Quando una nuova istruzione contraddice una vecchia, l'istruzione più vecchia viene rimossa o esplicitamente sovrascritta nel contesto. In alternativa, l'agente può utilizzare un **bloc-notes** per conciliare le preferenze contrastanti prima di decidere, assicurando che sia l'istruzione finale e coerente a guidare le sue azioni.

## Hai altre domande sull'Ingegneria del Contesto?

Unisciti al [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D) per incontrare altri apprendisti, partecipare a sessioni di assistenza e ricevere risposte alle tue domande sugli Agenti AI.
## Lezione precedente

[Agentic Protocols](../11-agentic-protocols/README.md)

## Prossima lezione

[Memoria per Agenti AI](../13-agent-memory/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:
Questo documento è stato tradotto utilizzando il servizio di traduzione AI [Co-op Translator](https://github.com/Azure/co-op-translator). Sebbene ci impegniamo per garantire la precisione, si prega di notare che le traduzioni automatizzate possono contenere errori o imprecisioni. Il documento originale nella sua lingua nativa deve essere considerato la fonte autorevole. Per informazioni critiche, si raccomanda una traduzione professionale effettuata da un essere umano. Non siamo responsabili per eventuali malintesi o interpretazioni errate derivanti dall’uso di questa traduzione.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->