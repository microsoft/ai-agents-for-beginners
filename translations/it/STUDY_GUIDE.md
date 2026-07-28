# Agenti AI per Principianti - Guida di Studio

Usa questa guida come compagno pratico mentre procedi nel corso. Non è
pensata per sostituire le lezioni. Ti aiuta a decidere da dove iniziare, cosa
cercare in ogni lezione e come collegare le idee in una piccola demo funzionante
di un agente.

Se è la tua prima volta qui, inizia in modo semplice:

1. Leggi il [Setup del Corso](./00-course-setup/README.md).
2. Completa le Lezioni 01-06 in ordine.
3. Tieni a mente una piccola idea di demo mentre impari.
4. Dopo ogni lezione, chiediti: "Cosa può fare ora il mio agente che prima
   non poteva fare?"

## Una Demo Semplice da Tenere a Mente

Un buon modo per imparare gli agenti è seguire un'idea di demo durante il corso.

Demo di esempio: **un agente assistente al corso**.

L'utente chiede:

> "Voglio imparare come gli agenti usano gli strumenti. Trova le lezioni giuste, 
> riassumi cosa dovrei leggere prima e dammi un breve compito pratico."

Un chatbot normale può rispondere da ciò che già conosce. Un agente può fare di più:

1. **Leggere o cercare nei file del corso** per trovare le lezioni giuste.
2. **Usare strumenti** per recuperare link delle lezioni, esempi o materiale di supporto.
3. **Pianificare** un breve percorso di apprendimento invece di dare una risposta lunga.
4. **Usare il contesto** della conversazione attuale per restare concentrati sull’obiettivo
   dell'apprendente.
5. **Ricordare le preferenze utili** se l’applicazione supporta la memoria.
6. **Mostrare tracce, citazioni o registri** così che l’utente possa capire cosa è successo.
7. **Applicare salvaguardie** prima di compiere azioni rischiose o usare dati sensibili.

Mentre studi ogni lezione, torna a questa demo e chiediti: quale nuova capacità
aggiungerebbe questa lezione?

## Verso Cosa Stai Costruendo

Alla fine del corso, dovresti essere in grado di spiegare e costruire sistemi agenti
che combinano queste parti:

| Parte | Significato in linguaggio semplice | Nella demo |
|------|-------------------------------|-------------|
| Modello | Il motore di ragionamento che interpreta la richiesta dell'utente | Capisce che l'apprendente vuole lezioni sull'uso degli strumenti |
| Strumenti | Funzioni, API, file, browser o servizi che l’agente può usare | Cerca nel repository o recupera contenuti delle lezioni |
| Conoscenza | Documenti o dati usati per ancorare la risposta | File README del corso e materiale delle lezioni |
| Contesto | Informazioni incluse nella prossima chiamata al modello | L’obiettivo dell’utente e i risultati degli strumenti |
| Memoria | Informazioni salvate per uso futuro | L’apprendente preferisce esempi pratici in Python |
| Pianificazione | Scomporre un obiettivo grande in passi più piccoli | Trova lezioni, riassumile, suggerisci esercizi |
| Orchestrazione | Smistare il lavoro tra strumenti, passi o agenti | Un planner chiama uno strumento di ricerca, poi un sintetizzatore |
| Fiducia | Sicurezza, valutazione, osservabilità | Registra le chiamate agli strumenti e chiede prima di azioni ad alto impatto |

## Modelli e Provider

I campioni di codice del corso usano il **Microsoft Agent Framework (MAF)** e puntano all’**Azure OpenAI Responses API** — l'API raccomandata in futuro, che combina completamenti chat, chiamate a strumenti, input multimodale e conversazioni con stato in un’unica API. Ti connetti tramite un progetto **Microsoft Foundry** (con `FoundryChatClient`) o direttamente ad Azure OpenAI (con `OpenAIChatClient`).

Mentre lavori con le lezioni, hai alcune opzioni di provider:

- **Microsoft Foundry / Azure OpenAI (Responses API)** — il percorso principale usato nelle lezioni. Accedi con `az login` per un’autenticazione Entra ID senza chiavi.
- **Foundry Locale** — esegui modelli completamente sul dispositivo tramite un’API compatibile OpenAI (nessun cloud, nessuna chiave API). Ideale per sperimentazioni offline o senza costi. Vedi [Setup del Corso](./00-course-setup/README.md).
- **MiniMax** — un provider compatibile OpenAI con modelli a contesto esteso, utilizzabile come alternativa drop-in.

> **Nota:** GitHub Models è deprecato (sarà ritirato a luglio 2026) e non supporta Responses API. I campioni sono stati aggiornati per usare Azure OpenAI / Microsoft Foundry invece.

## Scegli il Tuo Percorso di Apprendimento

Puoi seguire il corso completo in ordine, oppure saltare a un percorso basato su ciò che vuoi
costruire.

| Se il tuo obiettivo è... | Inizia con | Poi studia |
|-----------------------|------------|------------|
| Capire cosa sono gli agenti | 01, 02, 03 | 04, 05, 06 |
| Costruire un agente che usa strumenti | 04 | 05, 07, 14 |
| Costruire un agente basato su RAG | 05 | 04, 06, 12 |
| Progettare flussi di lavoro a più passi | 07 | 08, 09, 14 |
| Capire i sistemi multi-agente | 08 | 07, 09, 11 |
| Preparare agenti per la produzione | 06, 10 | 12, 13, 16, 18 |
| Distribuire e scalare agenti su Foundry | 10, 16 | 06, 13, 18 |
| Costruire agenti locali / offline-first | 17 | 04, 05, 11 |
| Esplorare protocolli e automazione browser | 11, 15 | 10, 18 |

Consiglio: se sei nuovo agli agenti, non saltare le Lezioni 01-06. Ti daranno il
vocabolario necessario per il resto del corso.

## Guida Lezione per Lezione

| Lezione | Cosa impari | Prova questo dopo la lezione |
|--------|--------------|-------------------------------|
| [01 - Introduzione agli Agenti AI](./01-intro-to-ai-agents/README.md) | Cosa rende un agente diverso da un semplice chatbot. | Spiega la tua idea di demo come agente, non solo come app di chat. |
| [02 - Framework Agentici](./02-explore-agentic-frameworks/README.md) | Come i framework aiutano con modelli, strumenti, stato e flussi di lavoro. | Identifica quali parti della tua demo un framework gestirebbe. |
| [03 - Pattern di Design Agentico](./03-agentic-design-patterns/README.md) | Pattern comuni per progettare il comportamento dell’agente. | Disegna il percorso utente prima di scrivere codice. |
| [04 - Uso degli Strumenti](./04-tool-use/README.md) | Come gli agenti chiamano strumenti per ottenere dati o agire. | Definisci uno strumento di cui avrebbe bisogno il tuo agente demo. |
| [05 - RAG Agentico](./05-agentic-rag/README.md) | Come il retrieval ancorano le risposte dell’agente a documenti o dati. | Decidi quale fonte di conoscenza la tua demo dovrebbe cercare. |

| [06 - Agenti Affidabili](./06-building-trustworthy-agents/README.md) | Come aggiungere protezioni, supervisione e comportamenti più sicuri. | Aggiungi una regola per quando l'agente deve prima chiedere all'utente. |
| [07 - Progettazione della Pianificazione](./07-planning-design/README.md) | Come gli agenti suddividono obiettivi più grandi in passi più piccoli. | Scrivi un piano in tre fasi per la tua richiesta demo. |
| [08 - Progettazione Multi-Agente](./08-multi-agent/README.md) | Quando suddividere il lavoro tra agenti specializzati. | Decidi se la tua demo necessita di un agente o di più agenti. |
| [09 - Metacognizione](./09-metacognition/README.md) | Come gli agenti possono rivedere e migliorare il proprio output. | Aggiungi un controllo finale prima che l'agente risponda. |
| [10 - Agenti AI in Produzione](./10-ai-agents-production/README.md) | Cosa cambia quando un agente passa dalla demo alla produzione. | Elenca cosa vorresti monitorare: qualità, costo, latenza, errori. |
| [11 - Protocolli Agentici](./11-agentic-protocols/README.md) | Come i protocolli collegano agenti a strumenti e altri agenti. | Identifica dove un protocollo standard potrebbe semplificare l'integrazione. |
| [12 - Ingegneria del Contesto](./12-context-engineering/README.md) | Come selezionare, tagliare, isolare e gestire il contesto. | Decidi cosa deve stare nel prompt e cosa invece deve restare fuori. |
| [13 - Memoria dell'Agente](./13-agent-memory/README.md) | Come gli agenti possono salvare informazioni utili tra le interazioni. | Scegli una preferenza sicura che la tua demo potrebbe ricordare. |
| [14 - Microsoft Agent Framework](./14-microsoft-agent-framework/README.md) | Blocchi costitutivi specifici del framework per agenti e flussi di lavoro, più ospitare agenti LangChain/LangGraph su Microsoft Foundry. | Mappa i passaggi della tua demo ai concetti del framework. |
| [15 - Agenti per l'Uso del Computer](./15-browser-use/README.md) | Come gli agenti possono interagire con il browser o le interfacce utente, compresi esempi reali come Microsoft Project Opal. | Scegli un'attività del browser che dovrebbe comunque richiedere la conferma dell'utente. |
| [16 - Distribuzione di Agenti Scalabili](./16-deploying-scalable-agents/README.md) | Come portare un agente da prototipo a una distribuzione di produzione scalabile e osservabile su Microsoft Foundry (agenti ospitati, instradamento dei modelli, caching, cancelli di valutazione, test di fumo). | Elenca le preoccupazioni di produzione che la tua demo deve ancora affrontare: hosting, instradamento, costo, valutazione. |
| [17 - Creazione di Agenti AI Locali](./17-creating-local-ai-agents/README.md) | Come costruire agenti local-first che girano interamente sulla tua macchina con Foundry Local e Qwen (strumenti locali, RAG locale, MCP locale). | Decidi quali parti della tua demo dovrebbero restare private e girare localmente. |
| [18 - Sicurezza degli Agenti AI](./18-securing-ai-agents/README.md) | Come rendere le azioni degli agenti più verificabili e a prova di manomissione. | Decidi quali azioni nella tua demo dovrebbero essere registrate o convalidate. |

## Validare gli Agenti Distribuiti con Test di Fumo

Quando distribuisci un agente (Lezione 16), un **test di fumo** è il primo controllo
più economico per verificare che la distribuzione risponda effettivamente. Questo repository include cataloghi pronti all'uso
sotto [tests/](./tests/README.md) per gli agenti distribuibili nelle Lezioni
01, 04, 05 e 16, collegati a

[AI Smoke Test](https://github.com/marketplace/actions/ai-smoke-test) Azione GitHub.
Eseguila dalla scheda **Actions** dopo aver distribuito l'agente della lezione.
I test smoke sono una prima barriera — la valutazione offline e online (Lezioni 10 e 16)
ti indicano quanto l'agente sia *bravo*.

## Idee chiave in termini accessibili ai principianti

### Strumenti

Uno strumento è qualcosa che l'agente può chiamare per svolgere lavoro al di fuori del modello. Un buon strumento
ha un nome chiaro, un lavoro specifico, input tipizzati, output prevedibile e un modo sicuro
di fallire.

Per la demo dell'assistente del corso, uno strumento potrebbe essere:

- `search_lessons(query)`
- `read_lesson(path)`
- `create_practice_task(topic)`

### RAG e Conoscenza

RAG aiuta l'agente a rispondere dalla fonte materiale anziché indovinare. In questo
corso, tale materiale può essere i README delle lezioni, esempi di codice o risorse esterne
collegate dalle lezioni.

Usa RAG quando la risposta deve essere fondata su documenti, dati o file di progetto
correnti.

### Pianificazione

La pianificazione è utile quando la richiesta ha più di un passaggio. Mantieni i piani brevi e
abbastanza visibili da poter essere ispezionati da uno sviluppatore o utente.

Per la demo, un piano potrebbe essere:

1. Trova lezioni relative all'uso degli strumenti.
2. Riassumi le lezioni più rilevanti.
3. Raccomanda un compito pratico.

### Contesto

Il contesto è ciò che il modello vede in questo momento. Un contesto troppo scarso può far
perdere dettagli importanti all'agente. Un contesto troppo ampio può rendere l'agente più lento,
più costoso o più facile da confondere.

Una buona ingegneria del contesto significa scegliere le informazioni giuste per la prossima chiamata
al modello.

### Memoria

La memoria è l'informazione salvata per dopo. Non salvare tutto. Salva le informazioni
solo quando sono utili, sicure e facili da aggiornare o cancellare.

Per esempio, ricordare che "l'apprendente preferisce esempi in Python" può essere utile.
Ricordare dati personali sensibili di solito non lo è.

### Valutazione e Osservabilità

La valutazione chiede: l'agente ha fatto la cosa giusta?

L'osservabilità chiede: possiamo vedere come è successo?

Per agenti in produzione, tieni traccia di chiamate al modello, chiamate agli strumenti, contesto recuperato,
latenza, costi, errori e feedback degli utenti.

### Fiducia e Sicurezza

Agenti affidabili necessitano più di un semplice prompt utile. Usa strumenti a minimo privilegio,
approvazione umana per azioni ad alto impatto, redazione dei dati dove necessario e log o
ricevute per azioni che devono essere controllate.

## Una routine di revisione di 15 minuti

Usa questa routine dopo ogni lezione:

1. **Riassumi la lezione in una frase.**
2. **Nomina la nuova capacità dell'agente.** Per esempio: uso dello strumento, recupero,
   pianificazione, memoria, osservabilità o sicurezza.
3. **Aggiungila alla demo dell'assistente del corso.** Cosa cambia nella demo ora?
4. **Individua il rischio.** Cosa potrebbe andare storto se questa capacità fosse usata male?
5. **Scrivi una domanda di test.** Come controlleresti che l'agente si comporta bene?

## Controllo rapido di auto-valutazione

Prima di andare avanti, prova a rispondere a queste domande:

1. Cosa può fare un agente che una normale chatbot non può fare da sola?
2. Quale strumento avrebbe bisogno prima il tuo agente, e perché?
3. Quale fonte di conoscenza dovrebbe fondare la risposta dell'agente?
4. Quale contesto dovrebbe essere incluso nella prossima chiamata al modello?

5. Cosa dovrebbe ricordare l'agente e cosa dovrebbe evitare di memorizzare?
6. Quando dovrebbe l'agente chiedere l'approvazione umana?
7. Quali registri, tracce o ricevute ti aiuterebbero a fare il debug o a verificare l'agente successivamente?


## Esercizio finale suggerito

Alla fine del corso, crea un piccolo agente che aiuti un apprendista a navigare in questo
repository.

Versione minima:

- Accettare un argomento dall'utente.
- Trovare le lezioni più rilevanti.
- Riassumere cosa leggere per primo.
- Suggerire un compito pratico.
- Mostrare quali file o link delle lezioni sono stati utilizzati.

Versione avanzata:

- Ricordare il linguaggio di programmazione preferito dall'apprendente.
- Usare un piano semplice prima di rispondere.
- Aggiungere un passaggio di autocontrollo prima della risposta finale.
- Registrare le chiamate agli strumenti e le fonti recuperate.
- Chiedere conferma prima di aprire il browser o eseguire attività di automazione UI.

Questo ti offre un modo piccolo ma realistico per praticare strumenti, RAG, pianificazione,
contesto, memoria, osservabilità e fiducia in un unico progetto.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:
Questo documento è stato tradotto utilizzando il servizio di traduzione AI [Co-op Translator](https://github.com/Azure/co-op-translator). Sebbene ci impegniamo per garantire la precisione, si prega di notare che le traduzioni automatizzate possono contenere errori o imprecisioni. Il documento originale nella sua lingua nativa deve essere considerato la fonte autorevole. Per informazioni critiche, si raccomanda una traduzione professionale effettuata da un essere umano. Non siamo responsabili per eventuali malintesi o interpretazioni errate derivanti dall’uso di questa traduzione.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->