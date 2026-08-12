[![Come progettare buoni agenti AI](../../../translated_images/it/lesson-3-thumbnail.1092dd7a8f1074a5.webp)](https://youtu.be/m9lM8qqoOEA?si=4KimounNKvArQQ0K)

> _(Clicca sull’immagine sopra per vedere il video di questa lezione)_
# Principi di progettazione agentica AI

## Introduzione

Esistono molti modi di pensare alla costruzione di sistemi agentici AI. Dato che l’ambiguità è una caratteristica e non un difetto nella progettazione di AI generativa, a volte è difficile per gli ingegneri capire da dove iniziare. Abbiamo creato un set di principi di progettazione UX centrati sull’uomo per permettere agli sviluppatori di costruire sistemi agentici centrati sul cliente per risolvere le loro esigenze di business. Questi principi di progettazione non sono un’architettura prescrittiva ma piuttosto un punto di partenza per i team che stanno definendo e costruendo esperienze agentiche.

In generale, gli agenti dovrebbero:

- Ampliare e scalare le capacità umane (brainstorming, problem solving, automazione, ecc.)
- Colmare le lacune di conoscenza (aggiornarmi su domini di conoscenza, traduzione, ecc.)
- Facilitare e supportare la collaborazione nei modi in cui preferiamo lavorare con gli altri
- Renderci versioni migliori di noi stessi (ad esempio, coach di vita/maestro dei compiti, aiutandoci a imparare regolazione emotiva e abilità di mindfulness, costruendo resilienza, ecc.)

## Questa lezione coprirà

- Cosa sono i principi di progettazione agentica
- Quali linee guida seguire durante l’implementazione di questi principi di progettazione
- Alcuni esempi di utilizzo dei principi di progettazione

## Obiettivi di apprendimento

Dopo aver completato questa lezione, sarai in grado di:

1. Spiegare cosa sono i principi di progettazione agentica
2. Spiegare le linee guida per l’utilizzo dei principi di progettazione agentica
3. Capire come costruire un agente usando i principi di progettazione agentica

## I principi di progettazione agentica

![Principi di progettazione agentica](../../../translated_images/it/agentic-design-principles.1cfdf8b6d3cc73c2.webp)

### Agente (Spazio)

Questo è l’ambiente in cui l’agente opera. Questi principi guidano il modo in cui progettiamo agenti per interagire con i mondi fisici e digitali.

- **Connettere, non collassare** – aiutare a connettere persone ad altre persone, eventi e conoscenze azionabili per permettere collaborazione e connessione.
- Gli agenti aiutano a connettere eventi, conoscenze e persone.
- Gli agenti avvicinano le persone. Non sono progettati per sostituire o sminuire gli individui.
- **Facilmente accessibile ma occasionalmente invisibile** – l’agente opera in gran parte in background e ci dà un piccolo segnale solo quando è rilevante e appropriato.
  - L’agente è facilmente individuabile e accessibile da utenti autorizzati su qualsiasi dispositivo o piattaforma.
  - L’agente supporta input e output multimodali (suono, voce, testo, ecc.).
  - L’agente può transitare senza soluzione di continuità tra primo piano e secondo piano; tra modalità proattiva e reattiva, a seconda della percezione delle esigenze dell’utente.
  - L’agente può operare in forma invisibile, ma il suo percorso di processo in background e la collaborazione con altri agenti sono trasparenti e controllabili dall’utente.

### Agente (Tempo)

Questo è il modo in cui l’agente opera nel tempo. Questi principi guidano come progettiamo agenti che interagiscono attraverso passato, presente e futuro.

- **Passato**: riflettendo sulla storia che include sia stato che contesto.
  - L’agente fornisce risultati più rilevanti basati sull’analisi di dati storici più ricchi oltre al singolo evento, persone o stati.
  - L’agente crea connessioni da eventi passati e riflette attivamente sulla memoria per interagire con situazioni attuali.
- **Presente**: spingere più che notificare.
  - L’agente incarna un approccio comprensivo all’interazione con le persone. Quando accade un evento, l’agente va oltre la notifica statica o altre formalità statiche. L’agente può semplificare flussi o generare dinamicamente segnali per indirizzare l’attenzione dell’utente nel momento giusto.
  - L’agente fornisce informazioni basate sull’ambiente contestuale, sui cambiamenti sociali e culturali e adattate all’intento dell’utente.
  - L’interazione con l’agente può essere graduale, evolvendosi/crescendo in complessità per potenziare gli utenti nel lungo termine.
- **Futuro**: adattarsi ed evolversi.
  - L’agente si adatta a vari dispositivi, piattaforme e modalità.
  - L’agente si adatta al comportamento dell’utente, alle esigenze di accessibilità ed è liberamente personalizzabile.
  - L’agente è plasmato e si evolve attraverso un’interazione continua con l’utente.

### Agente (Nucleo)

Questi sono gli elementi chiave nel nucleo del design di un agente.

- **Abbracciare l’incertezza ma stabilire fiducia**.
  - Un certo livello di incertezza dell’agente è previsto. L’incertezza è un elemento chiave nel design degli agenti.
  - Fiducia e trasparenza sono livelli fondamentali nel design degli agenti.
  - Gli umani controllano quando l’agente è acceso/spento e lo stato dell’agente è chiaramente visibile in ogni momento.

## Le linee guida per implementare questi principi

Quando usi i principi di progettazione precedenti, segui le linee guida seguenti:

1. **Trasparenza**: informa l’utente che è coinvolta l’IA, come funziona (comprese azioni passate) e come fornire feedback e modificare il sistema.
2. **Controllo**: consenti all’utente di personalizzare, specificare preferenze e personalizzarsi, e di avere controllo sul sistema e le sue caratteristiche (inclusa la possibilità di dimenticare).
3. **Coerenza**: punta a esperienze coerenti e multimodali across dispositivi e endpoint. Usa elementi UI/UX familiari dove possibile (ad esempio, icona del microfono per interazione vocale) e riduci il carico cognitivo del cliente il più possibile (ad esempio, risposte concise, aiuti visivi e contenuti ‘Scopri di più’).

## Come progettare un agente di viaggio usando questi principi e linee guida

Immagina di progettare un agente di viaggio, ecco come potresti pensare di usare i principi e le linee guida di progettazione:

1. **Trasparenza** – Fai sapere all’utente che l’agente di viaggio è un agente abilitato dall’IA. Fornisci alcune istruzioni di base per iniziare (ad esempio, un messaggio di “Ciao”, prompt esemplari). Documentalo chiaramente nella pagina del prodotto. Mostra la lista dei prompt che un utente ha usato in passato. Fai sapere come dare feedback (pollice su e giù, pulsante Invia feedback, ecc.). Articola chiaramente se l’agente ha restrizioni su usi o argomenti.
2. **Controllo** – Assicurati che sia chiaro come l’utente può modificare l’agente dopo la creazione con elementi come il Prompt di sistema. Permetti all’utente di scegliere quanto dettagliato sia l’agente, lo stile di scrittura e eventuali limitazioni su ciò di cui l’agente non dovrebbe parlare. Permetti all’utente di visualizzare ed eliminare file associati o dati, prompt e conversazioni passate.
3. **Coerenza** – Assicurati che le icone per condividere il prompt, aggiungere un file o una foto e taggare qualcuno o qualcosa siano standard e riconoscibili. Usa l’icona della graffetta per indicare il caricamento/condivisione file con l’agente, e l’icona immagine per indicare il caricamento grafici.

## Codici di esempio

- Python: [Agent Framework](./code_samples/03-python-agent-framework.ipynb)
- .NET: [Agent Framework](./code_samples/03-dotnet-agent-framework.md)


## Hai altre domande sui modelli di progettazione agentica AI?

Unisciti al [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D) per incontrare altri studenti, partecipare a sessioni di consulenza e ottenere risposte alle tue domande sugli agenti AI.

## Risorse aggiuntive

- <a href="https://openai.com" target="_blank">Pratiche per governare sistemi AI agentici | OpenAI</a>
- <a href="https://microsoft.com" target="_blank">Il progetto HAX Toolkit - Microsoft Research</a>
- <a href="https://responsibleaitoolbox.ai" target="_blank">Responsible AI Toolbox</a>

## Lezione precedente

[Esplorare framework agentici](../02-explore-agentic-frameworks/README.md)

## Lezione successiva

[Modello di progettazione dell’uso degli strumenti](../04-tool-use/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:
Questo documento è stato tradotto utilizzando il servizio di traduzione AI [Co-op Translator](https://github.com/Azure/co-op-translator). Sebbene ci impegniamo per garantire la precisione, si prega di notare che le traduzioni automatizzate possono contenere errori o imprecisioni. Il documento originale nella sua lingua nativa deve essere considerato la fonte autorevole. Per informazioni critiche, si raccomanda una traduzione professionale effettuata da un essere umano. Non siamo responsabili per eventuali malintesi o interpretazioni errate derivanti dall’uso di questa traduzione.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->