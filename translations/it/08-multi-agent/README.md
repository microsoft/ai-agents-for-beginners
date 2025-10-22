<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "1a008c204051cba8d0e253b75f261c41",
  "translation_date": "2025-08-29T12:58:31+00:00",
  "source_file": "08-multi-agent/README.md",
  "language_code": "it"
}
-->
[![Progettazione Multi-Agente](../../../translated_images/lesson-8-thumbnail.278a3e4a59137d625df92de3f885d2da2a92b1f7017abba25a99fb25edd83a55.it.png)](https://youtu.be/V6HpE9hZEx0?si=A7K44uMCqgvLQVCa)

> _(Clicca sull'immagine sopra per vedere il video di questa lezione)_

# Modelli di progettazione multi-agente

Non appena inizi a lavorare su un progetto che coinvolge più agenti, dovrai considerare il modello di progettazione multi-agente. Tuttavia, potrebbe non essere immediatamente chiaro quando passare ai multi-agenti e quali siano i vantaggi.

## Introduzione

In questa lezione cercheremo di rispondere alle seguenti domande:

- Quali sono gli scenari in cui i multi-agenti sono applicabili?
- Quali sono i vantaggi di utilizzare multi-agenti rispetto a un singolo agente che svolge più compiti?
- Quali sono i componenti fondamentali per implementare il modello di progettazione multi-agente?
- Come possiamo avere visibilità su come i diversi agenti interagiscono tra loro?

## Obiettivi di apprendimento

Dopo questa lezione, dovresti essere in grado di:

- Identificare gli scenari in cui i multi-agenti sono applicabili.
- Riconoscere i vantaggi di utilizzare multi-agenti rispetto a un singolo agente.
- Comprendere i componenti fondamentali per implementare il modello di progettazione multi-agente.

Qual è il quadro generale?

*I multi-agenti sono un modello di progettazione che consente a più agenti di lavorare insieme per raggiungere un obiettivo comune*.

Questo modello è ampiamente utilizzato in vari campi, tra cui robotica, sistemi autonomi e calcolo distribuito.

## Scenari in cui i multi-agenti sono applicabili

Quali sono quindi gli scenari in cui è utile utilizzare i multi-agenti? La risposta è che ci sono molti scenari in cui impiegare più agenti è vantaggioso, soprattutto nei seguenti casi:

- **Carichi di lavoro elevati**: I carichi di lavoro elevati possono essere suddivisi in compiti più piccoli e assegnati a diversi agenti, consentendo un'elaborazione parallela e un completamento più rapido. Un esempio di questo è il caso di un grande compito di elaborazione dati.
- **Compiti complessi**: I compiti complessi, come i carichi di lavoro elevati, possono essere suddivisi in sotto-compiti più piccoli e assegnati a diversi agenti, ciascuno specializzato in un aspetto specifico del compito. Un buon esempio è il caso dei veicoli autonomi, dove diversi agenti gestiscono la navigazione, il rilevamento degli ostacoli e la comunicazione con altri veicoli.
- **Competenze diversificate**: Diversi agenti possono avere competenze diversificate, consentendo loro di gestire diversi aspetti di un compito in modo più efficace rispetto a un singolo agente. Per questo caso, un buon esempio è il settore sanitario, dove gli agenti possono gestire diagnosi, piani di trattamento e monitoraggio dei pazienti.

## Vantaggi di utilizzare multi-agenti rispetto a un singolo agente

Un sistema con un singolo agente potrebbe funzionare bene per compiti semplici, ma per compiti più complessi, utilizzare più agenti può offrire diversi vantaggi:

- **Specializzazione**: Ogni agente può essere specializzato per un compito specifico. La mancanza di specializzazione in un singolo agente significa avere un agente che può fare tutto, ma potrebbe confondersi su cosa fare quando affronta un compito complesso. Potrebbe, ad esempio, finire per svolgere un compito per il quale non è il più adatto.
- **Scalabilità**: È più facile scalare i sistemi aggiungendo più agenti piuttosto che sovraccaricare un singolo agente.
- **Tolleranza ai guasti**: Se un agente fallisce, gli altri possono continuare a funzionare, garantendo l'affidabilità del sistema.

Prendiamo un esempio: prenotare un viaggio per un utente. Un sistema con un singolo agente dovrebbe gestire tutti gli aspetti del processo di prenotazione del viaggio, dalla ricerca dei voli alla prenotazione di hotel e auto a noleggio. Per ottenere questo con un singolo agente, l'agente dovrebbe avere strumenti per gestire tutti questi compiti. Questo potrebbe portare a un sistema complesso e monolitico, difficile da mantenere e scalare. Un sistema multi-agente, invece, potrebbe avere diversi agenti specializzati nella ricerca di voli, nella prenotazione di hotel e auto a noleggio. Questo renderebbe il sistema più modulare, più facile da mantenere e scalabile.

Confrontiamolo con un'agenzia di viaggi gestita come un negozio a conduzione familiare rispetto a un'agenzia di viaggi gestita come un franchising. Il negozio a conduzione familiare avrebbe un singolo agente che gestisce tutti gli aspetti del processo di prenotazione del viaggio, mentre il franchising avrebbe diversi agenti che gestiscono diversi aspetti del processo di prenotazione del viaggio.

## Componenti fondamentali per implementare il modello di progettazione multi-agente

Prima di poter implementare il modello di progettazione multi-agente, è necessario comprendere i componenti fondamentali che costituiscono il modello.

Rendiamolo più concreto guardando di nuovo l'esempio della prenotazione di un viaggio per un utente. In questo caso, i componenti fondamentali includerebbero:

- **Comunicazione tra agenti**: Gli agenti per la ricerca di voli, la prenotazione di hotel e auto a noleggio devono comunicare e condividere informazioni sulle preferenze e sui vincoli dell'utente. È necessario decidere i protocolli e i metodi per questa comunicazione. Concretamente, ciò significa che l'agente per la ricerca di voli deve comunicare con l'agente per la prenotazione di hotel per garantire che l'hotel sia prenotato per le stesse date del volo. Questo significa che gli agenti devono condividere informazioni sulle date di viaggio dell'utente, il che implica decidere *quali agenti condividono informazioni e come le condividono*.
- **Meccanismi di coordinamento**: Gli agenti devono coordinare le loro azioni per garantire che le preferenze e i vincoli dell'utente siano rispettati. Una preferenza dell'utente potrebbe essere che desidera un hotel vicino all'aeroporto, mentre un vincolo potrebbe essere che le auto a noleggio sono disponibili solo presso l'aeroporto. Questo significa che l'agente per la prenotazione di hotel deve coordinarsi con l'agente per la prenotazione di auto a noleggio per garantire che le preferenze e i vincoli dell'utente siano rispettati. Questo implica decidere *come gli agenti coordinano le loro azioni*.
- **Architettura degli agenti**: Gli agenti devono avere una struttura interna per prendere decisioni e apprendere dalle loro interazioni con l'utente. Questo significa che l'agente per la ricerca di voli deve avere una struttura interna per prendere decisioni su quali voli raccomandare all'utente. Questo implica decidere *come gli agenti prendono decisioni e apprendono dalle loro interazioni con l'utente*. Esempi di come un agente apprende e migliora potrebbero essere che l'agente per la ricerca di voli utilizza un modello di apprendimento automatico per raccomandare voli all'utente in base alle sue preferenze passate.
- **Visibilità nelle interazioni multi-agente**: È necessario avere visibilità su come i diversi agenti interagiscono tra loro. Questo significa avere strumenti e tecniche per tracciare le attività e le interazioni degli agenti. Questo potrebbe essere sotto forma di strumenti di registrazione e monitoraggio, strumenti di visualizzazione e metriche di prestazione.
- **Modelli multi-agente**: Esistono diversi modelli per implementare sistemi multi-agente, come architetture centralizzate, decentralizzate e ibride. È necessario decidere il modello che meglio si adatta al proprio caso d'uso.
- **Intervento umano**: Nella maggior parte dei casi, ci sarà un intervento umano e sarà necessario istruire gli agenti su quando chiedere l'intervento umano. Questo potrebbe essere sotto forma di un utente che chiede un hotel o un volo specifico che gli agenti non hanno raccomandato o che chiede conferma prima di prenotare un volo o un hotel.

## Visibilità nelle interazioni multi-agente

È importante avere visibilità su come i diversi agenti interagiscono tra loro. Questa visibilità è essenziale per il debug, l'ottimizzazione e per garantire l'efficacia complessiva del sistema. Per ottenere ciò, è necessario avere strumenti e tecniche per tracciare le attività e le interazioni degli agenti. Questo potrebbe essere sotto forma di strumenti di registrazione e monitoraggio, strumenti di visualizzazione e metriche di prestazione.

Ad esempio, nel caso della prenotazione di un viaggio per un utente, si potrebbe avere un dashboard che mostra lo stato di ciascun agente, le preferenze e i vincoli dell'utente e le interazioni tra gli agenti. Questo dashboard potrebbe mostrare le date di viaggio dell'utente, i voli raccomandati dall'agente per i voli, gli hotel raccomandati dall'agente per gli hotel e le auto a noleggio raccomandate dall'agente per le auto a noleggio. Questo fornirebbe una visione chiara di come gli agenti interagiscono tra loro e se le preferenze e i vincoli dell'utente vengono rispettati.

Esaminiamo ciascuno di questi aspetti più nel dettaglio.

- **Strumenti di registrazione e monitoraggio**: È importante registrare ogni azione intrapresa da un agente. Una voce di registro potrebbe memorizzare informazioni sull'agente che ha intrapreso l'azione, l'azione intrapresa, l'ora in cui l'azione è stata intrapresa e il risultato dell'azione. Queste informazioni possono essere utilizzate per il debug, l'ottimizzazione e altro.
- **Strumenti di visualizzazione**: Gli strumenti di visualizzazione possono aiutare a vedere le interazioni tra gli agenti in modo più intuitivo. Ad esempio, si potrebbe avere un grafico che mostra il flusso di informazioni tra gli agenti. Questo potrebbe aiutare a identificare colli di bottiglia, inefficienze e altri problemi nel sistema.
- **Metriche di prestazione**: Le metriche di prestazione possono aiutare a tracciare l'efficacia del sistema multi-agente. Ad esempio, si potrebbe tracciare il tempo impiegato per completare un compito, il numero di compiti completati per unità di tempo e l'accuratezza delle raccomandazioni fatte dagli agenti. Queste informazioni possono aiutare a identificare aree di miglioramento e ottimizzare il sistema.

## Modelli multi-agente

Esaminiamo alcuni modelli concreti che possiamo utilizzare per creare applicazioni multi-agente. Ecco alcuni modelli interessanti da considerare:

### Chat di gruppo

Questo modello è utile quando si desidera creare un'applicazione di chat di gruppo in cui più agenti possono comunicare tra loro. I casi d'uso tipici per questo modello includono collaborazione di squadra, supporto clienti e social networking.

In questo modello, ogni agente rappresenta un utente nella chat di gruppo e i messaggi vengono scambiati tra gli agenti utilizzando un protocollo di messaggistica. Gli agenti possono inviare messaggi alla chat di gruppo, ricevere messaggi dalla chat di gruppo e rispondere ai messaggi di altri agenti.

Questo modello può essere implementato utilizzando un'architettura centralizzata in cui tutti i messaggi vengono instradati attraverso un server centrale, o un'architettura decentralizzata in cui i messaggi vengono scambiati direttamente.

![Chat di gruppo](../../../translated_images/multi-agent-group-chat.ec10f4cde556babd7b450fd01e1a0fac1f9788c27d3b9e54029377bb1bdd1db6.it.png)

### Passaggio di consegne

Questo modello è utile quando si desidera creare un'applicazione in cui più agenti possono passarsi compiti tra loro.

I casi d'uso tipici per questo modello includono supporto clienti, gestione dei compiti e automazione dei flussi di lavoro.

In questo modello, ogni agente rappresenta un compito o un passaggio in un flusso di lavoro, e gli agenti possono passarsi compiti basandosi su regole predefinite.

![Passaggio di consegne](../../../translated_images/multi-agent-hand-off.4c5fb00ba6f8750a0754bf29d49fa19d578080c61da40416df84d866bcdd87a3.it.png)

### Filtraggio collaborativo

Questo modello è utile quando si desidera creare un'applicazione in cui più agenti possono collaborare per fare raccomandazioni agli utenti.

Perché si vorrebbe che più agenti collaborassero? Perché ogni agente può avere competenze diverse e contribuire al processo di raccomandazione in modi diversi.

Prendiamo un esempio in cui un utente desidera una raccomandazione sul miglior titolo da acquistare sul mercato azionario.

- **Esperto di settore**: Un agente potrebbe essere esperto in un settore specifico.
- **Analisi tecnica**: Un altro agente potrebbe essere esperto in analisi tecnica.
- **Analisi fondamentale**: E un altro agente potrebbe essere esperto in analisi fondamentale. Collaborando, questi agenti possono fornire una raccomandazione più completa all'utente.

![Raccomandazione](../../../translated_images/multi-agent-filtering.d959cb129dc9f60826916f0f12fe7a8339b532f5f236860afb8f16b63ea10dc2.it.png)

## Scenario: Processo di rimborso

Consideriamo uno scenario in cui un cliente sta cercando di ottenere un rimborso per un prodotto. Ci possono essere diversi agenti coinvolti in questo processo, ma dividiamoli tra agenti specifici per questo processo e agenti generali che possono essere utilizzati in altri processi.

**Agenti specifici per il processo di rimborso**:

Di seguito alcuni agenti che potrebbero essere coinvolti nel processo di rimborso:

- **Agente cliente**: Questo agente rappresenta il cliente ed è responsabile dell'avvio del processo di rimborso.
- **Agente venditore**: Questo agente rappresenta il venditore ed è responsabile dell'elaborazione del rimborso.
- **Agente pagamento**: Questo agente rappresenta il processo di pagamento ed è responsabile del rimborso del pagamento del cliente.
- **Agente risoluzione**: Questo agente rappresenta il processo di risoluzione ed è responsabile della risoluzione di eventuali problemi che sorgono durante il processo di rimborso.
- **Agente conformità**: Questo agente rappresenta il processo di conformità ed è responsabile di garantire che il processo di rimborso sia conforme alle normative e alle politiche.

**Agenti generali**:

Questi agenti possono essere utilizzati in altre parti della tua attività.

- **Agente spedizione**: Questo agente rappresenta il processo di spedizione ed è responsabile della spedizione del prodotto al venditore. Questo agente può essere utilizzato sia per il processo di rimborso che per la spedizione generale di un prodotto, ad esempio in caso di acquisto.
- **Agente feedback**: Questo agente rappresenta il processo di feedback ed è responsabile della raccolta di feedback dal cliente. Il feedback potrebbe essere raccolto in qualsiasi momento e non solo durante il processo di rimborso.
- **Agente escalation**: Questo agente rappresenta il processo di escalation ed è responsabile di portare i problemi a un livello superiore di supporto. Puoi utilizzare questo tipo di agente per qualsiasi processo in cui è necessario eseguire un'escalation.
- **Agente notifiche**: Questo agente rappresenta il processo di notifica ed è responsabile dell'invio di notifiche al cliente in varie fasi del processo di rimborso.
- **Agente analisi**: Questo agente rappresenta il processo di analisi ed è responsabile dell'analisi dei dati relativi al processo di rimborso.
- **Agente audit**: Questo agente rappresenta il processo di audit ed è responsabile di verificare che il processo di rimborso venga eseguito correttamente.
- **Agente report**: Questo agente rappresenta il processo di reportistica ed è responsabile della generazione di report sul processo di rimborso.
- **Agente conoscenza**: Questo agente rappresenta il processo di conoscenza ed è responsabile del mantenimento di una base di conoscenza di informazioni relative al processo di rimborso. Questo agente potrebbe essere esperto sia sui rimborsi che su altre parti della tua attività.
- **Agente sicurezza**: Questo agente rappresenta il processo di sicurezza ed è responsabile di garantire la sicurezza del processo di rimborso.
- **Agente qualità**: Questo agente rappresenta il processo di qualità ed è responsabile di garantire la qualità del processo di rimborso.

Ci sono molti agenti elencati in precedenza, sia per il processo di rimborso specifico che per gli agenti generali che possono essere utilizzati in altre parti della tua attività. Speriamo che questo ti dia un'idea di come puoi decidere quali agenti utilizzare nel tuo sistema multi-agente.

## Compito
Progetta un sistema multi-agente per un processo di supporto clienti. Identifica gli agenti coinvolti nel processo, i loro ruoli e responsabilità, e come interagiscono tra loro. Considera sia agenti specifici per il processo di supporto clienti sia agenti generali che possono essere utilizzati in altre parti della tua attività.

> Rifletti prima di leggere la soluzione seguente, potresti aver bisogno di più agenti di quanto pensi.

> TIP: Pensa alle diverse fasi del processo di supporto clienti e considera anche gli agenti necessari per qualsiasi sistema.

## Soluzione

[Soluzione](./solution/solution.md)

## Verifica delle conoscenze

Domanda: Quando dovresti considerare l'uso di multi-agenti?

- [ ] A1: Quando hai un carico di lavoro ridotto e un compito semplice.
- [ ] A2: Quando hai un carico di lavoro elevato.
- [ ] A3: Quando hai un compito semplice.

[Quiz soluzione](./solution/solution-quiz.md)

## Riepilogo

In questa lezione, abbiamo esaminato il modello di progettazione multi-agente, inclusi gli scenari in cui i multi-agenti sono applicabili, i vantaggi dell'utilizzo di multi-agenti rispetto a un singolo agente, i componenti fondamentali per implementare il modello di progettazione multi-agente e come avere visibilità su come i diversi agenti interagiscono tra loro.

### Hai altre domande sul modello di progettazione multi-agente?

Unisciti al [Discord di Azure AI Foundry](https://aka.ms/ai-agents/discord) per incontrare altri studenti, partecipare agli orari d'ufficio e ottenere risposte alle tue domande sugli AI Agents.

## Risorse aggiuntive

## Lezione precedente

[Progettazione della pianificazione](../07-planning-design/README.md)

## Lezione successiva

[Metacognizione negli AI Agents](../09-metacognition/README.md)

---

**Disclaimer**:  
Questo documento è stato tradotto utilizzando il servizio di traduzione automatica [Co-op Translator](https://github.com/Azure/co-op-translator). Sebbene ci impegniamo per garantire l'accuratezza, si prega di notare che le traduzioni automatiche potrebbero contenere errori o imprecisioni. Il documento originale nella sua lingua nativa dovrebbe essere considerato la fonte autorevole. Per informazioni critiche, si consiglia una traduzione professionale eseguita da un traduttore umano. Non siamo responsabili per eventuali fraintendimenti o interpretazioni errate derivanti dall'uso di questa traduzione.