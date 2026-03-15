[![Multi-Agent Design](../../../translated_images/it/lesson-8-thumbnail.278a3e4a59137d62.webp)](https://youtu.be/V6HpE9hZEx0?si=A7K44uMCqgvLQVCa)

> _(Clicca sull'immagine sopra per vedere il video di questa lezione)_

# Modelli di progettazione multi-agente

Non appena inizi a lavorare su un progetto che coinvolge più agenti, dovrai considerare il modello di progettazione multi-agente. Tuttavia, potrebbe non essere immediatamente chiaro quando passare ai multi-agenti e quali sono i vantaggi.

## Introduzione

In questa lezione, cerchiamo di rispondere alle seguenti domande:

- Quali sono gli scenari in cui i multi-agenti sono applicabili?
- Quali sono i vantaggi di utilizzare multi-agenti rispetto a un singolo agente che svolge più compiti?
- Quali sono i componenti fondamentali per implementare il modello di progettazione multi-agente?
- Come possiamo avere visibilità su come i molteplici agenti interagiscono tra loro?

## Obiettivi di apprendimento

Dopo questa lezione, dovresti essere in grado di:

- Identificare scenari in cui i multi-agenti sono applicabili
- Riconoscere i vantaggi di usare multi-agenti rispetto a un agente singolo.
- Comprendere i componenti fondamentali per implementare il modello di progettazione multi-agente.

Qual è il quadro generale?

*I multi-agenti sono un modello di progettazione che consente a più agenti di lavorare insieme per raggiungere un obiettivo comune*.

Questo modello è ampiamente utilizzato in vari campi, tra cui robotica, sistemi autonomi e calcolo distribuito.

## Scenari in cui i Multi-Agenti sono Applicabili

Quali scenari sono un buon caso d'uso per impiegare multi-agenti? La risposta è che ci sono molti scenari in cui l'impiego di più agenti è vantaggioso, soprattutto nei seguenti casi:

- **Grandi carichi di lavoro**: I grandi carichi di lavoro possono essere suddivisi in compiti più piccoli e assegnati a agenti differenti, permettendo un'elaborazione parallela e un completamento più rapido. Un esempio di questo è nel caso di un grande compito di elaborazione dati.
- **Compiti complessi**: I compiti complessi, come i grandi carichi di lavoro, possono essere suddivisi in sotto-compiti più piccoli e assegnati a diversi agenti, ciascuno specializzato in un aspetto specifico del compito. Un buon esempio è nel caso dei veicoli autonomi, dove agenti diversi gestiscono la navigazione, il rilevamento degli ostacoli e la comunicazione con altri veicoli.
- **Competenze diverse**: Diverse competenze possono essere possedute da agenti differenti, permettendo loro di gestire aspetti diversi di un compito in modo più efficace rispetto a un agente singolo. Un buon esempio in questo caso è nel settore sanitario, dove agenti possono gestire la diagnostica, i piani di trattamento e il monitoraggio del paziente.

## Vantaggi dell'Utilizzo dei Multi-Agenti rispetto a un Agente Singolo

Un sistema con un singolo agente potrebbe funzionare bene per compiti semplici, ma per compiti più complessi, l'uso di più agenti può offrire diversi vantaggi:

- **Specializzazione**: Ogni agente può essere specializzato per un compito specifico. La mancanza di specializzazione in un agente singolo significa avere un agente che può fare tutto ma potrebbe confondersi su cosa fare di fronte a un compito complesso. Potrebbe, ad esempio, finire per fare un compito per cui non è il più adatto.
- **Scalabilità**: È più facile scalare i sistemi aggiungendo più agenti anziché sovraccaricare un singolo agente.
- **Tolleranza ai guasti**: Se un agente si guasta, gli altri possono continuare a funzionare, assicurando l'affidabilità del sistema.

Facciamo un esempio: organizziamo un viaggio per un utente. Un sistema con un singolo agente dovrebbe gestire tutti gli aspetti del processo di prenotazione del viaggio, dalla ricerca dei voli alla prenotazione di hotel e auto a noleggio. Per realizzare ciò con un singolo agente, l'agente avrebbe bisogno di strumenti per gestire tutti questi compiti. Questo potrebbe portare a un sistema complesso e monolitico, difficile da mantenere e scalare. Un sistema multi-agente, invece, potrebbe avere agenti diversi specializzati nella ricerca di voli, nella prenotazione di hotel e auto a noleggio. Questo renderebbe il sistema più modulare, più facile da mantenere e scalabile.

Confronta questo con un'agenzia viaggi gestita come un negozio a conduzione familiare rispetto a un'agenzia viaggi gestita come una franchigia. Il negozio a conduzione familiare avrebbe un singolo agente che gestisce tutti gli aspetti del processo di prenotazione del viaggio, mentre la franchigia avrebbe agenti diversi che gestiscono aspetti diversi del processo di prenotazione.

## Componenti Fondamentali per Implementare il Modello di Progettazione Multi-Agente

Prima di poter implementare il modello di progettazione multi-agente, devi comprendere i componenti fondamentali che compongono il modello.

Rendiamo questo più concreto guardando di nuovo all'esempio della prenotazione di un viaggio per un utente. In questo caso, i componenti fondamentali includerebbero:

- **Comunicazione tra Agenti**: Gli agenti per la ricerca di voli, la prenotazione di hotel e auto a noleggio devono comunicare e condividere informazioni sulle preferenze e i vincoli dell'utente. Devi decidere i protocolli e i metodi per questa comunicazione. Concretamente ciò significa che l'agente per la ricerca voli deve comunicare con l'agente per la prenotazione hotel per assicurarsi che l'hotel sia prenotato per le stesse date del volo. Ciò significa che gli agenti devono condividere informazioni sulle date di viaggio dell'utente, pertanto devi decidere *quali agenti condividono le informazioni e come le condividono*.
- **Meccanismi di Coordinamento**: Gli agenti devono coordinare le loro azioni per assicurarsi che le preferenze e i vincoli dell'utente siano soddisfatti. Una preferenza dell'utente potrebbe essere quella di voler un hotel vicino all'aeroporto, mentre un vincolo potrebbe essere che le auto a noleggio sono disponibili solo in aeroporto. Ciò significa che l'agente per la prenotazione hotel deve coordinarsi con l'agente per la prenotazione auto a noleggio per assicurarsi che le preferenze e i vincoli dell'utente siano soddisfatti. Devi decidere *come gli agenti coordinano le loro azioni*.
- **Architettura dell'Agente**: Gli agenti devono avere una struttura interna per prendere decisioni e imparare dalle loro interazioni con l'utente. Ciò significa che l'agente per la ricerca voli deve avere una struttura interna per decidere quali voli raccomandare all'utente. Devi decidere *come gli agenti prendono decisioni e imparano dalle loro interazioni con l'utente*. Un esempio di come un agente impara e migliora potrebbe essere che l'agente per la ricerca voli utilizzi un modello di apprendimento automatico per raccomandare voli in base alle preferenze passate dell'utente.
- **Visibilità nelle Interazioni Multi-Agente**: Devi avere visibilità su come i molteplici agenti interagiscono tra loro. Ciò significa che devi avere strumenti e tecniche per il tracciamento delle attività e delle interazioni degli agenti. Questo può assumere la forma di strumenti di logging e monitoraggio, strumenti di visualizzazione e metriche di prestazione.
- **Modelli Multi-Agente**: Esistono diversi modelli per implementare sistemi multi-agente, come architetture centralizzate, decentralizzate e ibride. Devi decidere quale modello si adatta meglio al tuo caso d'uso.
- **Umano nel circuito**: Nella maggior parte dei casi, avrai un umano nel circuito e devi istruirlo su quando gli agenti devono chiedere un intervento umano. Questo può essere sotto forma di un utente che chiede un hotel o un volo specifico che gli agenti non hanno raccomandato o che chiede una conferma prima di prenotare un volo o un hotel.

## Visibilità nelle Interazioni Multi-Agente

È importante che tu abbia visibilità su come i molteplici agenti stanno interagendo tra loro. Questa visibilità è essenziale per il debug, l'ottimizzazione e per assicurare l'efficacia complessiva del sistema. Per ottenerla, devi disporre di strumenti e tecniche per tracciare le attività e le interazioni degli agenti. Questo può avvenire tramite strumenti di logging e monitoraggio, strumenti di visualizzazione e metriche di prestazione.

Ad esempio, nel caso della prenotazione di un viaggio per un utente, potresti avere una dashboard che mostra lo stato di ogni agente, le preferenze e i vincoli dell'utente, e le interazioni tra gli agenti. Questa dashboard potrebbe mostrare le date di viaggio dell'utente, i voli raccomandati dall'agente voli, gli hotel raccomandati dall'agente hotel e le auto a noleggio raccomandate dall'agente auto. Questo ti darebbe una visione chiara di come gli agenti interagiscono fra loro e se le preferenze e i vincoli dell'utente sono soddisfatti.

Esaminiamo ciascuno di questi aspetti più in dettaglio.

- **Strumenti di Logging e Monitoraggio**: Vuoi che venga registrata una traccia per ogni azione intrapresa da un agente. Una voce di log potrebbe memorizzare informazioni sull'agente che ha compiuto l'azione, l'azione effettuata, l'orario in cui è stata svolta e l'esito dell'azione. Queste informazioni possono essere utilizzate per il debug, l'ottimizzazione e altro.

- **Strumenti di Visualizzazione**: Gli strumenti di visualizzazione possono aiutarti a vedere le interazioni tra agenti in modo più intuitivo. Ad esempio, potresti avere un grafico che mostra il flusso di informazioni tra gli agenti. Questo potrebbe aiutarti a identificare colli di bottiglia, inefficienze e altri problemi nel sistema.

- **Metriche di Prestazione**: Le metriche di prestazione possono aiutarti a monitorare l'efficacia del sistema multi-agente. Ad esempio, potresti monitorare il tempo necessario per completare un compito, il numero di compiti completati per unità di tempo e l'accuratezza delle raccomandazioni fatte dagli agenti. Queste informazioni possono aiutarti a identificare aree di miglioramento e ottimizzare il sistema.

## Modelli Multi-Agente

Esploriamo alcuni modelli concreti che possiamo usare per creare applicazioni multi-agente. Ecco alcuni modelli interessanti da considerare:

### Chat di gruppo

Questo modello è utile quando vuoi creare un'applicazione di chat di gruppo in cui più agenti possono comunicare tra loro. Gli usi tipici di questo modello includono la collaborazione di team, il supporto clienti e i social network.

In questo modello, ogni agente rappresenta un utente nella chat di gruppo, e i messaggi vengono scambiati tra agenti usando un protocollo di messaggistica. Gli agenti possono inviare messaggi alla chat di gruppo, ricevere messaggi dalla chat di gruppo e rispondere ai messaggi degli altri agenti.

Questo modello può essere implementato usando un'architettura centralizzata in cui tutti i messaggi passano attraverso un server centrale, oppure un'architettura decentralizzata in cui i messaggi vengono scambiati direttamente.

![Group chat](../../../translated_images/it/multi-agent-group-chat.ec10f4cde556babd.webp)

### Passaggio di consegna

Questo modello è utile quando vuoi creare un'applicazione in cui più agenti possono passarsi compiti fra loro.

Gli usi tipici di questo modello includono supporto clienti, gestione delle attività e automazione dei flussi di lavoro.

In questo modello, ogni agente rappresenta un compito o un passo in un flusso di lavoro, e gli agenti possono passarsi i compiti ad altri agenti basandosi su regole predefinite.

![Hand off](../../../translated_images/it/multi-agent-hand-off.4c5fb00ba6f8750a.webp)

### Filtraggio collaborativo

Questo modello è utile quando vuoi creare un'applicazione in cui più agenti possono collaborare per fare raccomandazioni agli utenti.

Il motivo per cui vorresti che più agenti collaborino è che ogni agente può avere competenze diverse e può contribuire al processo di raccomandazione in modi differenti.

Prendiamo un esempio in cui un utente desidera una raccomandazione sul miglior titolo azionario da acquistare sul mercato azionario.

- **Esperto di settore**: Un agente potrebbe essere esperto in un settore specifico.
- **Analisi tecnica**: Un altro agente potrebbe essere esperto in analisi tecnica.
- **Analisi fondamentale**: Un altro agente ancora potrebbe essere esperto in analisi fondamentale. Collaborando, questi agenti possono fornire una raccomandazione più completa all'utente.

![Recommendation](../../../translated_images/it/multi-agent-filtering.d959cb129dc9f608.webp)

## Scenario: Processo di rimborso

Considera uno scenario in cui un cliente cerca di ottenere un rimborso per un prodotto; possono essere coinvolti diversi agenti in questo processo, ma dividiamoli tra agenti specifici per questo processo e agenti generali che possono essere usati in altri processi.

**Agenti specifici per il processo di rimborso**:

Seguono alcuni agenti che potrebbero essere coinvolti nel processo di rimborso:

- **Agente cliente**: Questo agente rappresenta il cliente ed è responsabile di avviare il processo di rimborso.
- **Agente venditore**: Questo agente rappresenta il venditore ed è responsabile dell'elaborazione del rimborso.
- **Agente pagamento**: Questo agente rappresenta il processo di pagamento ed è responsabile di rimborsare il pagamento del cliente.
- **Agente risoluzione**: Questo agente rappresenta il processo di risoluzione ed è responsabile di risolvere eventuali problemi sorti durante il processo di rimborso.
- **Agente conformità**: Questo agente rappresenta il processo di conformità ed è responsabile di assicurare che il processo di rimborso rispetti regolamenti e politiche.

**Agenti generali**:

Questi agenti possono essere utilizzati da altre parti della tua attività.

- **Agente spedizioni**: Questo agente rappresenta il processo di spedizione ed è responsabile della spedizione del prodotto al venditore. Questo agente può essere usato sia per il processo di rimborso sia per la spedizione generale di un prodotto tramite un acquisto, ad esempio.
- **Agente feedback**: Questo agente rappresenta il processo di raccolta feedback ed è responsabile di raccogliere il feedback dal cliente. Il feedback può essere raccolto in qualsiasi momento e non solo durante il processo di rimborso.
- **Agente escalation**: Questo agente rappresenta il processo di escalation ed è responsabile di portare i problemi a un livello di supporto superiore. Puoi usare questo tipo di agente per qualsiasi processo in cui è necessario un'escalation di un problema.
- **Agente notifiche**: Questo agente rappresenta il processo di notifiche ed è responsabile di inviare notifiche al cliente in varie fasi del processo di rimborso.
- **Agente analisi**: Questo agente rappresenta il processo di analisi ed è responsabile di analizzare i dati relativi al processo di rimborso.
- **Agente audit**: Questo agente rappresenta il processo di audit ed è responsabile di verificare che il processo di rimborso venga svolto correttamente.
- **Agente reportistica**: Questo agente rappresenta il processo di reportistica ed è responsabile di generare report sul processo di rimborso.
- **Agente conoscenza**: Questo agente rappresenta il processo di gestione della conoscenza ed è responsabile di mantenere una base di conoscenza relativa al processo di rimborso. Questo agente potrebbe essere esperto sia di rimborsi che di altre parti della tua attività.
- **Agente sicurezza**: Questo agente rappresenta il processo di sicurezza ed è responsabile di garantire la sicurezza del processo di rimborso.
- **Agente qualità**: Questo agente rappresenta il processo qualità ed è responsabile di assicurare la qualità del processo di rimborso.

Ci sono molti agenti elencati precedentemente, sia per il processo specifico di rimborso, sia per gli agenti generali che possono essere usati in altre parti della tua attività. Speriamo che questo ti dia un'idea su come puoi decidere quali agenti utilizzare nel tuo sistema multi-agente.

## Compito

Progetta un sistema multi-agente per un processo di supporto clienti. Identifica gli agenti coinvolti nel processo, i loro ruoli e responsabilità, e come interagiscono tra loro. Considera sia agenti specifici per il processo di supporto clienti sia agenti generali che possono essere utilizzati in altre parti della tua attività.
> Rifletti prima di leggere la seguente soluzione, potresti aver bisogno di più agenti di quanto pensi.

> SUGGERIMENTO: Rifletti sulle diverse fasi del processo di supporto clienti e considera anche gli agenti necessari per qualsiasi sistema.

## Soluzione

[Solution](./solution/solution.md)

## Verifiche di conoscenza

Domanda: Quando dovresti considerare l'uso di multi-agenti?

- [ ] A1: Quando hai un carico di lavoro ridotto e un compito semplice.
- [ ] A2: Quando hai un carico di lavoro elevato
- [ ] A3: Quando hai un compito semplice.

[Solution quiz](./solution/solution-quiz.md)

## Riepilogo

In questa lezione, abbiamo esaminato il modello progettuale multi-agente, inclusi gli scenari in cui i multi-agenti sono applicabili, i vantaggi dell'utilizzo di multi-agenti rispetto a un singolo agente, i componenti fondamentali per implementare il modello progettuale multi-agente e come avere visibilità su come i diversi agenti interagiscono tra di loro.

### Hai altre domande sul modello progettuale Multi-Agente?

Unisciti al [Microsoft Foundry Discord](https://aka.ms/ai-agents/discord) per incontrare altri studenti, partecipare a ore di ricevimento e ottenere risposte alle tue domande sugli Agenti AI.

## Risorse aggiuntive

- <a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Documentazione Microsoft Agent Framework</a>
- <a href="https://www.analyticsvidhya.com/blog/2024/10/agentic-design-patterns/" target="_blank">Modelli progettuali agentici</a>


## Lezione precedente

[Planning Design](../07-planning-design/README.md)

## Lezione successiva

[Metacognition in AI Agents](../09-metacognition/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Dichiarazione di Non Responsabilità**:  
Questo documento è stato tradotto utilizzando il servizio di traduzione automatica [Co-op Translator](https://github.com/Azure/co-op-translator). Pur impegnandoci per garantire accuratezza, si prega di considerare che le traduzioni automatiche possono contenere errori o inesattezze. Il documento originale nella sua lingua originale deve essere considerato la fonte autorevole. Per informazioni critiche si raccomanda una traduzione professionale effettuata da un umano. Non ci assumiamo alcuna responsabilità per eventuali malintesi o interpretazioni errate derivanti dall’uso di questa traduzione.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->