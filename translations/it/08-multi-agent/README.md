[![Multi-agent Design](../../../translated_images/it/lesson-8-thumbnail.278a3e4a59137d62.webp)](https://youtu.be/V6HpE9hZEx0?si=A7K44uMCqgvLQVCa)

> _(Clicca sull'immagine sopra per vedere il video di questa lezione)_

# Pattern di design multi-agente

Appena inizi a lavorare su un progetto che coinvolge più agenti, dovrai considerare il pattern di design multi-agente. Tuttavia, potrebbe non essere immediatamente chiaro quando passare ai multi-agenti e quali sono i vantaggi.

## Introduzione

In questa lezione, cerchiamo di rispondere alle seguenti domande:

- Quali sono gli scenari in cui i multi-agenti sono applicabili?
- Quali sono i vantaggi di usare più agenti rispetto a un singolo agente che svolge più compiti?
- Quali sono i blocchi di costruzione per implementare il pattern di design multi-agente?
- Come possiamo avere visibilità su come i vari agenti interagiscono tra loro?

## Obiettivi didattici

Dopo questa lezione, dovresti essere in grado di:

- Identificare gli scenari in cui i multi-agenti sono applicabili
- Riconoscere i vantaggi dell’uso di più agenti rispetto a un agente singolo.
- Comprendere i blocchi di costruzione per implementare il pattern di design multi-agente.

Qual è il quadro generale?

*I multi-agenti sono un pattern di design che permette a più agenti di lavorare insieme per raggiungere un obiettivo comune*.

Questo pattern è ampiamente usato in vari campi, tra cui robotica, sistemi autonomi e calcolo distribuito.

## Scenari in cui i multi-agenti sono applicabili

Quali scenari sono adatti per l’uso dei multi-agenti? La risposta è che ci sono molti scenari in cui impiegare più agenti è vantaggioso, specialmente nei casi seguenti:

- **Grandi carichi di lavoro**: I grandi carichi di lavoro possono essere suddivisi in compiti più piccoli e assegnati a diversi agenti, permettendo un'elaborazione parallela e un completamento più rapido. Un esempio è un grande compito di elaborazione dati.
- **Compiti complessi**: Come per i grandi carichi di lavoro, i compiti complessi possono essere suddivisi in sotto-compiti affidati a diversi agenti, ognuno specializzato in un aspetto specifico. Un buon esempio sono i veicoli autonomi in cui diversi agenti gestiscono la navigazione, il rilevamento ostacoli e la comunicazione con altri veicoli.
- **Competenze diverse**: Diversi agenti possono avere competenze diverse, permettendo loro di gestire aspetti differenti di un compito in modo più efficace rispetto a un singolo agente. Un buon esempio è nel settore sanitario dove agenti possono gestire diagnosi, piani di trattamento e monitoraggio del paziente.

## Vantaggi dell'uso di multi-agenti rispetto a un singolo agente

Un sistema con un singolo agente può funzionare bene per compiti semplici, ma per quelli più complessi l'uso di più agenti può fornire vari vantaggi:

- **Specializzazione**: Ogni agente può essere specializzato per un compito specifico. La mancanza di specializzazione in un singolo agente significa che l'agente può fare tutto ma potrebbe confondersi di fronte a compiti complessi, svolgendo magari un compito per cui non è il più adatto.
- **Scalabilità**: È più facile scalare sistemi aggiungendo più agenti piuttosto che sovraccaricare un singolo agente.
- **Tolleranza ai guasti**: Se un agente fallisce, gli altri possono continuare a funzionare, garantendo l'affidabilità del sistema.

Facciamo un esempio: prenotiamo un viaggio per un utente. Un sistema con un solo agente dovrebbe gestire tutti gli aspetti della prenotazione del viaggio, dalla ricerca dei voli alla prenotazione di hotel e auto a noleggio. Per farlo, l’agente dovrebbe avere strumenti per gestire tutti questi compiti, portando a un sistema complesso e monolitico, difficile da mantenere e scalare. Un sistema multi-agente, invece, potrebbe avere diversi agenti specializzati nella ricerca di voli, prenotazione di hotel e auto a noleggio. Questo renderebbe il sistema più modulare, più facile da mantenere e scalabile.

Confronta questo con un'agenzia di viaggi gestita come un negozio di quartiere rispetto a una gestita come una catena. Il negozio di quartiere avrebbe un singolo agente che gestisce tutti gli aspetti della prenotazione, mentre la catena avrebbe diversi agenti che si occupano di aspetti diversi della prenotazione.

## Blocchi di costruzione per implementare il pattern di design multi-agente

Prima di poter implementare il pattern multi-agente, devi comprendere i blocchi di costruzione che compongono il pattern.

Rendi concreto questo concetto tornando all’esempio della prenotazione di un viaggio per un utente. In questo caso, i blocchi di costruzione includerebbero:

- **Comunicazione tra agenti**: Gli agenti per la ricerca voli, la prenotazione hotel e auto a noleggio devono comunicare e condividere informazioni sulle preferenze e vincoli dell’utente. Devi decidere i protocolli e i metodi per questa comunicazione. Concretamente, l’agente per la ricerca voli deve comunicare con quello per la prenotazione hotel per garantire che l’hotel sia prenotato per le stesse date del volo. Ciò significa che gli agenti devono condividere informazioni sulle date di viaggio dell’utente, quindi devi decidere *quali agenti condividono informazioni e come le condividono*.
- **Meccanismi di coordinamento**: Gli agenti devono coordinare le loro azioni per assicurare che le preferenze e i vincoli dell’utente siano rispettati. Una preferenza dell’utente potrebbe essere un hotel vicino all’aeroporto mentre un vincolo potrebbe essere che le auto a noleggio siano disponibili solo in aeroporto. Ciò significa che l’agente per la prenotazione hotel deve coordinarsi con quello per l’auto a noleggio per soddisfare le preferenze e i vincoli. Devi decidere *come gli agenti coordinano le loro azioni*.
- **Architettura degli agenti**: Gli agenti devono avere una struttura interna per prendere decisioni e imparare dalle loro interazioni con l’utente. Ciò significa che l’agente per la ricerca voli deve avere una struttura per decidere quali voli consigliare all’utente. Devi decidere *come gli agenti prendono decisioni e apprendono dalle loro interazioni con l’utente*. Un esempio potrebbe essere che l’agente per la ricerca voli usa un modello di machine learning per consigliare voli basati sulle preferenze passate dell’utente.
- **Visibilità nelle interazioni multi-agente**: Devi avere visibilità su come i molteplici agenti interagiscono tra loro. Ciò implica disporre di strumenti e tecniche per tracciare le attività e le interazioni degli agenti. Potrebbe trattarsi di strumenti di logging e monitoraggio, strumenti di visualizzazione e metriche di performance.
- **Pattern multi-agente**: Esistono diversi pattern per implementare sistemi multi-agente, come architetture centralizzate, decentralizzate e ibride. Devi scegliere il pattern che meglio si adatta al tuo caso d’uso.
- **Intervento umano**: Nella maggior parte dei casi, avrai un umano nel loop e devi istruire gli agenti su quando richiedere l’intervento umano. Questo potrebbe essere sotto forma di una richiesta dell’utente per un hotel o volo specifico che gli agenti non hanno raccomandato o una richiesta di conferma prima di prenotare volo o hotel.

## Visibilità nelle interazioni multi-agente

È importante avere visibilità su come i molteplici agenti interagiscono tra loro. Questa visibilità è essenziale per il debug, l’ottimizzazione e per assicurare l’efficacia complessiva del sistema. Per ottenere questo, devi avere strumenti e tecniche per tracciare le attività e le interazioni degli agenti. Potrebbe essere sotto forma di strumenti di logging e monitoraggio, strumenti di visualizzazione e metriche di performance.

Per esempio, quando si prenota un viaggio per un utente, potresti avere una dashboard che mostra lo stato di ciascun agente, le preferenze e i vincoli dell’utente e le interazioni tra agenti. Questa dashboard potrebbe mostrare le date del viaggio dell’utente, i voli raccomandati dall’agente voli, gli hotel consigliati dall’agente hotel e le auto a noleggio raccomandate dall’agente auto. Ciò ti darebbe una chiara visione di come gli agenti stanno interagendo e se le preferenze e i vincoli dell’utente vengono rispettati.

Esaminiamo ognuno di questi aspetti più in dettaglio.

- **Strumenti di logging e monitoraggio**: Vuoi che ogni azione presa da un agente venga registrata. Una voce di log potrebbe contenere informazioni sull’agente che ha compiuto l’azione, l’azione stessa, il momento in cui è stata fatta e il risultato. Queste informazioni possono essere usate per il debug, l’ottimizzazione e altro.

- **Strumenti di visualizzazione**: Gli strumenti di visualizzazione possono aiutarti a vedere le interazioni tra agenti in modo più intuitivo. Ad esempio, potresti avere un grafo che mostra il flusso di informazioni tra gli agenti. Questo può aiutarti a individuare colli di bottiglia, inefficienze e altri problemi nel sistema.

- **Metriche di performance**: Le metriche di performance possono aiutarti a monitorare l’efficacia del sistema multi-agente. Per esempio, potresti tracciare il tempo impiegato per completare un compito, il numero di compiti completati nell’unità di tempo e l’accuratezza delle raccomandazioni fornite dagli agenti. Queste informazioni possono aiutarti a identificare aree di miglioramento e ottimizzare il sistema.

## Pattern multi-agente

Esploriamo alcuni pattern concreti che possiamo usare per creare app multi-agente. Ecco alcuni pattern interessanti da considerare:

### Chat di gruppo

Questo pattern è utile quando vuoi creare un’applicazione di chat di gruppo dove più agenti possono comunicare tra loro. Gli usi tipici includono collaborazione in team, supporto clienti e social networking.

In questo pattern, ogni agente rappresenta un utente nella chat di gruppo e i messaggi vengono scambiati tra agenti usando un protocollo di messaggistica. Gli agenti possono inviare messaggi alla chat di gruppo, ricevere messaggi dalla chat e rispondere ai messaggi di altri agenti.

Questo pattern può essere implementato usando un’architettura centralizzata dove tutti i messaggi passano attraverso un server centrale, oppure un’architettura decentralizzata dove i messaggi sono scambiati direttamente.

![Group chat](../../../translated_images/it/multi-agent-group-chat.ec10f4cde556babd.webp)

### Passaggio di consegne

Questo pattern è utile quando vuoi creare un’applicazione in cui più agenti possono passarsi compiti l’un l’altro.

Gli usi tipici includono supporto clienti, gestione di compiti e automazione di workflow.

In questo pattern, ogni agente rappresenta un compito o una fase in un workflow, e gli agenti possono passarsi compiti sulla base di regole predefinite.

![Hand off](../../../translated_images/it/multi-agent-hand-off.4c5fb00ba6f8750a.webp)

### Filtraggio collaborativo

Questo pattern è utile quando vuoi creare un’applicazione in cui più agenti collaborano per fare raccomandazioni agli utenti.

Il motivo per cui vuoi che più agenti collaborino è che ogni agente può avere competenze diverse e contribuire al processo di raccomandazione in modi differenti.

Prendiamo l’esempio di un utente che desidera un suggerimento sul miglior titolo azionario da acquistare in borsa.

- **Esperto del settore**: Un agente potrebbe essere esperto in uno specifico settore.
- **Analisi tecnica**: Un altro agente potrebbe essere esperto in analisi tecnica.
- **Analisi fondamentale**: Un altro agente potrebbe essere esperto in analisi fondamentale. Collaborando, questi agenti possono fornire una raccomandazione più completa all’utente.

![Recommendation](../../../translated_images/it/multi-agent-filtering.d959cb129dc9f608.webp)

## Scenario: Processo di rimborso

Considera uno scenario in cui un cliente cerca di ottenere un rimborso per un prodotto; possono essere coinvolti diversi agenti in questo processo, ma dividiamoli in agenti specifici per questo processo e agenti generali che possono essere usati in altri processi.

**Agenti specifici per il processo di rimborso**:

Ecco alcuni agenti che potrebbero essere coinvolti nel processo di rimborso:

- **Agente cliente**: Questo agente rappresenta il cliente ed è responsabile di iniziare il processo di rimborso.
- **Agente venditore**: Questo agente rappresenta il venditore ed è responsabile dell’elaborazione del rimborso.
- **Agente pagamento**: Questo agente rappresenta il processo di pagamento ed è responsabile di rimborsare il pagamento del cliente.
- **Agente risoluzione**: Questo agente rappresenta il processo di risoluzione ed è responsabile di risolvere eventuali problemi che sorgono durante il processo di rimborso.
- **Agente conformità**: Questo agente rappresenta il processo di conformità ed è responsabile di garantire che il processo di rimborso rispetti regolamenti e politiche.

**Agenti generali**:

Questi agenti possono essere usati da altre parti del tuo business.

- **Agente spedizione**: Questo agente rappresenta il processo di spedizione ed è responsabile di spedire il prodotto indietro al venditore. Può essere usato sia per il processo di rimborso che per la spedizione generale di un prodotto tramite un acquisto.
- **Agente feedback**: Questo agente rappresenta il processo di raccolta feedback e si occupa di raccogliere opinioni dal cliente. Il feedback può essere richiesto in qualsiasi momento, non solo durante il rimborso.
- **Agente escalation**: Questo agente rappresenta il processo di escalation e si occupa di portare problemi a un livello superiore di supporto. Puoi usare questo tipo di agente per ogni processo in cui è necessario un’escalation.
- **Agente notifiche**: Questo agente rappresenta il processo di notifica ed è responsabile dell’invio di notifiche al cliente nelle varie fasi del processo di rimborso.
- **Agente analisi**: Questo agente rappresenta il processo di analisi ed è responsabile di analizzare i dati relativi al processo di rimborso.
- **Agente audit**: Questo agente rappresenta il processo di audit ed è responsabile di verificare che il processo di rimborso sia svolto correttamente.
- **Agente report**: Questo agente rappresenta il processo di reportistica ed è responsabile di generare report sul processo di rimborso.
- **Agente conoscenza**: Questo agente rappresenta il processo di gestione della conoscenza ed è responsabile del mantenimento di una base di conoscenze relativa ai rimborsi. Potrebbe avere conoscenze sia sui rimborsi che su altre parti del tuo business.
- **Agente sicurezza**: Questo agente rappresenta il processo di sicurezza ed è responsabile di garantire la sicurezza del processo di rimborso.
- **Agente qualità**: Questo agente rappresenta il processo di qualità ed è responsabile di assicurare la qualità del processo di rimborso.

Ci sono molti agenti elencati precedentemente, sia per il processo specifico di rimborso che per gli agenti generali che possono essere usati in altre parti del tuo business. Speriamo che questo ti dia un’idea su come decidere quali agenti utilizzare nel tuo sistema multi-agente.

## Compito

Progetta un sistema multi-agente per un processo di supporto clienti. Identifica gli agenti coinvolti nel processo, i loro ruoli e responsabilità, e come interagiscono tra loro. Considera sia agenti specifici per il processo di supporto clienti sia agenti generali che possono essere usati in altre parti del tuo business.


> Rifletti prima di leggere la seguente soluzione, potresti aver bisogno di più agenti di quanto pensi.

> SUGGERIMENTO: Pensa alle diverse fasi del processo di assistenza clienti e considera anche gli agenti necessari per qualsiasi sistema.

## Soluzione

[Soluzione](./solution/solution.md)

## Verifiche di conoscenza

### Domanda 1

Quale scenario è il più adatto per un sistema multi-agente?

- [ ] A1: Un bot di supporto risponde a domande comuni usando una base di conoscenza e un piccolo set di strumenti.
- [ ] A2: Un flusso di lavoro per i rimborsi necessita di ruoli separati per frode, pagamento e conformità, ognuno con i propri strumenti, e i loro risultati devono essere coordinati.
- [ ] A3: La stessa semplice richiesta di classificazione arriva migliaia di volte all’ora.

### Domanda 2

Quando un singolo agente è solitamente la scelta migliore?

- [ ] A1: Il compito può essere gestito con un solo set di istruzioni e strumenti, senza passaggi tra specialisti.
- [ ] A2: L’agente ha accesso a più di uno strumento.
- [ ] A3: Il flusso di lavoro richiede ruoli separati con permessi differenti e tracciamenti di audit indipendenti.

[Soluzione quiz](./solution/solution-quiz.md)

## Riepilogo

In questa lezione, abbiamo esaminato il pattern di progettazione multi-agente, inclusi gli scenari in cui i multi-agenti sono applicabili, i vantaggi di usare più agenti rispetto a un singolo agente, i blocchi costitutivi per implementare il pattern multi-agente e come avere visibilità su come i molteplici agenti interagiscono tra di loro.

### Hai altre domande sul pattern di progettazione Multi-Agente?

Unisciti al [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D) per incontrare altri studenti, partecipare alle ore d’ufficio e ricevere risposte alle tue domande sugli Agenti AI.

## Risorse aggiuntive

- <a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Documentazione Microsoft Agent Framework</a>
- <a href="https://www.analyticsvidhya.com/blog/2024/10/agentic-design-patterns/" target="_blank">Pattern di progettazione Agentic</a>


## Lezione precedente

[Pianificazione della progettazione](../07-planning-design/README.md)

## Lezione successiva

[Metacognizione negli agenti AI](../09-metacognition/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:
Questo documento è stato tradotto utilizzando il servizio di traduzione AI [Co-op Translator](https://github.com/Azure/co-op-translator). Sebbene ci impegniamo per garantire la precisione, si prega di notare che le traduzioni automatizzate possono contenere errori o imprecisioni. Il documento originale nella sua lingua nativa deve essere considerato la fonte autorevole. Per informazioni critiche, si raccomanda una traduzione professionale effettuata da un essere umano. Non siamo responsabili per eventuali malintesi o interpretazioni errate derivanti dall’uso di questa traduzione.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->