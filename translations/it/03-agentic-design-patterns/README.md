<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "4c46e4ff9e349c521e2b0b17f51afa64",
  "translation_date": "2025-08-29T13:05:05+00:00",
  "source_file": "03-agentic-design-patterns/README.md",
  "language_code": "it"
}
-->
[![Come progettare buoni agenti AI](../../../translated_images/lesson-3-thumbnail.1092dd7a8f1074a5b26e35aa8f810814e05a22fed1765c20c14b2b508c7ae379.it.png)](https://youtu.be/m9lM8qqoOEA?si=4KimounNKvArQQ0K)

> _(Clicca sull'immagine sopra per vedere il video di questa lezione)_
# Principi di Design per Agenti AI

## Introduzione

Esistono molti modi per pensare alla costruzione di Sistemi Agentici AI. Dato che l'ambiguità è una caratteristica e non un difetto nel design dell'AI Generativa, a volte è difficile per gli ingegneri capire da dove iniziare. Abbiamo creato un insieme di principi di design UX centrati sull'uomo per consentire agli sviluppatori di costruire sistemi agentici incentrati sul cliente per soddisfare le loro esigenze aziendali. Questi principi di design non rappresentano un'architettura prescrittiva, ma piuttosto un punto di partenza per i team che stanno definendo e costruendo esperienze con agenti.

In generale, gli agenti dovrebbero:

- Ampliare e scalare le capacità umane (brainstorming, risoluzione di problemi, automazione, ecc.)
- Colmare lacune di conoscenza (aggiornarmi su domini di conoscenza, traduzione, ecc.)
- Facilitare e supportare la collaborazione nei modi in cui preferiamo lavorare con gli altri
- Renderci versioni migliori di noi stessi (ad esempio, coach di vita/gestore di compiti, aiutandoci a imparare abilità di regolazione emotiva e consapevolezza, costruendo resilienza, ecc.)

## Questa lezione coprirà

- Cosa sono i Principi di Design Agentico
- Quali sono alcune linee guida da seguire durante l'implementazione di questi principi di design
- Quali sono alcuni esempi di utilizzo dei principi di design

## Obiettivi di apprendimento

Dopo aver completato questa lezione, sarai in grado di:

1. Spiegare cosa sono i Principi di Design Agentico
2. Spiegare le linee guida per l'utilizzo dei Principi di Design Agentico
3. Comprendere come costruire un agente utilizzando i Principi di Design Agentico

## I Principi di Design Agentico

![Principi di Design Agentico](../../../translated_images/agentic-design-principles.1cfdf8b6d3cc73c2b738951ee7b2043e224441d98babcf654be69d866120f93a.it.png)

### Agente (Spazio)

Questo è l'ambiente in cui l'agente opera. Questi principi informano come progettiamo agenti per interagire nei mondi fisici e digitali.

- **Connettere, non collassare** – aiutare a connettere le persone ad altre persone, eventi e conoscenze utili per abilitare collaborazione e connessione.
- Gli agenti aiutano a connettere eventi, conoscenze e persone.
- Gli agenti avvicinano le persone. Non sono progettati per sostituire o sminuire le persone.
- **Facilmente accessibile ma occasionalmente invisibile** – l'agente opera principalmente in background e ci sollecita solo quando è rilevante e appropriato.
  - L'agente è facilmente individuabile e accessibile per utenti autorizzati su qualsiasi dispositivo o piattaforma.
  - L'agente supporta input e output multimodali (suono, voce, testo, ecc.).
  - L'agente può passare senza problemi tra primo piano e sfondo; tra proattivo e reattivo, a seconda della percezione delle esigenze dell'utente.
  - L'agente può operare in forma invisibile, ma il percorso del processo in background e la collaborazione con altri agenti sono trasparenti e controllabili dall'utente.

### Agente (Tempo)

Questo è il modo in cui l'agente opera nel tempo. Questi principi informano come progettiamo agenti che interagiscono attraverso passato, presente e futuro.

- **Passato**: Riflettere sulla storia che include sia stato che contesto.
  - L'agente fornisce risultati più pertinenti basati sull'analisi di dati storici più ricchi oltre l'evento, le persone o gli stati.
  - L'agente crea connessioni da eventi passati e riflette attivamente sulla memoria per interagire con situazioni attuali.
- **Presente**: Sollecitare più che notificare.
  - L'agente incarna un approccio completo all'interazione con le persone. Quando si verifica un evento, l'agente va oltre la notifica statica o altre formalità statiche. L'agente può semplificare i flussi o generare dinamicamente suggerimenti per dirigere l'attenzione dell'utente al momento giusto.
  - L'agente fornisce informazioni basate sull'ambiente contestuale, sui cambiamenti sociali e culturali e adattate all'intento dell'utente.
  - L'interazione con l'agente può essere graduale, evolvendo/crescendo in complessità per potenziare gli utenti nel lungo termine.
- **Futuro**: Adattarsi ed evolversi.
  - L'agente si adatta a vari dispositivi, piattaforme e modalità.
  - L'agente si adatta al comportamento dell'utente, alle esigenze di accessibilità ed è liberamente personalizzabile.
  - L'agente è modellato e si evolve attraverso l'interazione continua con l'utente.

### Agente (Core)

Questi sono gli elementi chiave nel nucleo del design di un agente.

- **Abbracciare l'incertezza ma stabilire fiducia**.
  - Un certo livello di incertezza dell'agente è previsto. L'incertezza è un elemento chiave del design dell'agente.
  - Fiducia e trasparenza sono strati fondamentali del design dell'agente.
  - Gli esseri umani hanno il controllo su quando l'agente è acceso/spento e lo stato dell'agente è chiaramente visibile in ogni momento.

## Le linee guida per implementare questi principi

Quando utilizzi i principi di design precedenti, segui le seguenti linee guida:

1. **Trasparenza**: Informa l'utente che è coinvolta l'AI, come funziona (incluso le azioni passate) e come fornire feedback e modificare il sistema.
2. **Controllo**: Consenti all'utente di personalizzare, specificare preferenze e personalizzare, e avere il controllo sul sistema e sui suoi attributi (inclusa la possibilità di dimenticare).
3. **Coerenza**: Mira a esperienze coerenti e multimodali su dispositivi e punti di accesso. Usa elementi UI/UX familiari dove possibile (ad esempio, icona del microfono per l'interazione vocale) e riduci il carico cognitivo del cliente il più possibile (ad esempio, risposte concise, aiuti visivi e contenuti "Scopri di più").

## Come progettare un agente di viaggio utilizzando questi principi e linee guida

Immagina di progettare un agente di viaggio, ecco come potresti pensare di utilizzare i Principi di Design e le Linee Guida:

1. **Trasparenza** – Fai sapere all'utente che l'agente di viaggio è un agente abilitato dall'AI. Fornisci alcune istruzioni di base su come iniziare (ad esempio, un messaggio di "Benvenuto", suggerimenti di esempio). Documenta chiaramente questo sulla pagina del prodotto. Mostra l'elenco dei suggerimenti che un utente ha chiesto in passato. Rendilo chiaro su come fornire feedback (pollice su e giù, pulsante Invia Feedback, ecc.). Articola chiaramente se l'agente ha restrizioni di utilizzo o di argomento.
2. **Controllo** – Assicurati che sia chiaro come l'utente può modificare l'agente dopo che è stato creato con cose come il Prompt di Sistema. Consenti all'utente di scegliere quanto dettagliato deve essere l'agente, il suo stile di scrittura e qualsiasi avvertenza su ciò di cui l'agente non dovrebbe parlare. Consenti all'utente di visualizzare e eliminare eventuali file o dati associati, suggerimenti e conversazioni passate.
3. **Coerenza** – Assicurati che le icone per Condividi Suggerimento, aggiungi un file o una foto e tagga qualcuno o qualcosa siano standard e riconoscibili. Usa l'icona della graffetta per indicare il caricamento/condivisione di file con l'agente e un'icona immagine per indicare il caricamento di grafica.

### Hai altre domande sui modelli di design agentico AI?

Unisciti al [Discord di Azure AI Foundry](https://aka.ms/ai-agents/discord) per incontrare altri studenti, partecipare a ore di ufficio e ottenere risposte alle tue domande sugli agenti AI.

## Risorse aggiuntive

## Lezione precedente

[Esplorare i Framework Agentici](../02-explore-agentic-frameworks/README.md)

## Prossima lezione

[Modello di Design per l'Uso degli Strumenti](../04-tool-use/README.md)

---

**Disclaimer**:  
Questo documento è stato tradotto utilizzando il servizio di traduzione automatica [Co-op Translator](https://github.com/Azure/co-op-translator). Sebbene ci impegniamo per garantire l'accuratezza, si prega di notare che le traduzioni automatiche potrebbero contenere errori o imprecisioni. Il documento originale nella sua lingua nativa dovrebbe essere considerato la fonte autorevole. Per informazioni critiche, si raccomanda una traduzione professionale eseguita da un traduttore umano. Non siamo responsabili per eventuali fraintendimenti o interpretazioni errate derivanti dall'uso di questa traduzione.