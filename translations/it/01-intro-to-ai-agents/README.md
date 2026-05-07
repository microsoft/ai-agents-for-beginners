[![Introduzione agli Agenti AI](../../../translated_images/it/lesson-1-thumbnail.d21b2c34b32d35bb.webp)](https://youtu.be/3zgm60bXmQk?si=QA4CW2-cmul5kk3D)

> _(Clicca sull'immagine sopra per guardare il video di questa lezione)_

# Introduzione agli Agenti AI e Casi d'Uso degli Agenti

Benvenuto al corso **Agenti AI per Principianti**! Questo corso ti fornisce le conoscenze fondamentali — e codice funzionante reale — per iniziare a costruire Agenti AI da zero.

Vieni a salutarci nella <a href="https://discord.gg/kzRShWzttr" target="_blank">Community Discord di Azure AI</a> — è piena di studenti e costruttori di AI felici di rispondere alle domande.

Prima di iniziare a costruire, assicuriamoci di capire davvero cos’è un Agente AI *e* quando ha senso usarne uno.

---

## Introduzione

Questa lezione tratta:

- Cosa sono gli Agenti AI, e i diversi tipi che esistono  
- Per quali tipi di compiti gli Agenti AI sono più adatti  
- I blocchi fondamentali che utilizzerai nella progettazione di una soluzione Agentica  

## Obiettivi di Apprendimento

Al termine di questa lezione, dovresti essere in grado di:

- Spiegare cos’è un Agente AI e in cosa differisce da una soluzione AI normale  
- Sapere quando usare un Agente AI (e quando no)  
- Abbozzare una progettazione base di una soluzione Agentica per un problema reale  

---

## Definizione di Agenti AI e Tipi di Agenti AI

### Cosa sono gli Agenti AI?

Ecco un modo semplice per pensarci:

> **Gli Agenti AI sono sistemi che permettono ai Modelli di Linguaggio di Grande Scala (LLM) di *fare cose* — fornendo loro strumenti e conoscenze per agire sul mondo, non soltanto rispondere a prompt.**

Scomponiamolo un po':

- **Sistema** — Un Agente AI non è un singolo elemento. È una raccolta di parti che lavorano insieme. Nel suo nucleo, ogni agente ha tre componenti:  
  - **Ambiente** — Lo spazio in cui l'agente opera. Per un agente di prenotazioni di viaggio, sarebbe la piattaforma di prenotazione stessa.  
  - **Sensori** — Come l'agente legge lo stato attuale del suo ambiente. Il nostro agente di viaggio potrebbe controllare la disponibilità degli hotel o i prezzi dei voli.  
  - **Attuatori** — Come l'agente agisce. L'agente di viaggio potrebbe prenotare una camera, inviare una conferma o cancellare una prenotazione.  

![Cosa Sono gli Agenti AI?](../../../translated_images/it/what-are-ai-agents.1ec8c4d548af601a.webp)

- **Modelli di Linguaggio di Grande Scala** — Gli agenti esistevano prima degli LLM, ma sono gli LLM che rendono gli agenti moderni così potenti. Possono comprendere il linguaggio naturale, ragionare sul contesto, e trasformare una richiesta vaga dell’utente in un piano concreto d’azione.

- **Eseguono Azioni** — Senza un sistema agente, un LLM genera solo testo. All’interno di un sistema agente, l’LLM può effettivamente *eseguire* i passaggi — cercare nel database, chiamare un’API, inviare un messaggio.

- **Accesso agli Strumenti** — Gli strumenti che un agente può usare dipendono da (1) l’ambiente in cui funziona e (2) cosa lo sviluppatore ha scelto di fornirgli. Un agente di viaggio può cercare voli ma non modificare i dati dei clienti — dipende tutto da cosa colleghi.

- **Memoria + Conoscenza** — Gli agenti possono avere memoria a breve termine (la conversazione attuale) e memoria a lungo termine (un database clienti, interazioni passate). L’agente di viaggio potrebbe "ricordare" che preferisci i posti vicino al finestrino.

---

### I Diversi Tipi di Agenti AI

Non tutti gli agenti sono costruiti allo stesso modo. Ecco una ripartizione dei tipi principali, usando l’agente di prenotazione viaggi come esempio ricorrente:

| **Tipo di Agente** | **Cosa Fa** | **Esempio Agente di Viaggio** |
|---|---|---|
| **Agenti a Riflesso Semplice** | Segue regole codificate — senza memoria, senza pianificazione. | Vede una email di reclamo → la inoltra al servizio clienti. Tutto qui. |
| **Agenti a Riflesso Basati su Modello** | Mantiene un modello interno del mondo e lo aggiorna quando le cose cambiano. | Monitora i prezzi storici dei voli e segnala i percorsi improvvisamente costosi. |
| **Agenti Basati su Obiettivi** | Ha un obiettivo in mente e lo raggiunge passo dopo passo. | Prenota un viaggio completo (voli, auto, hotel) partendo dalla tua posizione attuale per portarti a destinazione. |
| **Agenti Basati su Utilità** | Non trova solo *una* soluzione — trova la *migliore* valutando i compromessi. | Bilancia costo vs comodità per trovare il viaggio che corrisponde meglio alle tue preferenze. |
| **Agenti Apprendenti** | Migliora nel tempo imparando dai feedback. | Adatta le raccomandazioni future sulla base dei risultati di un sondaggio post-viaggio. |
| **Agenti Gerarchici** | Un agente di alto livello suddivide il lavoro in sottocompiti e li delega ad agenti di livello inferiore. | Una richiesta "cancella viaggio" viene suddivisa in: cancella volo, cancella hotel, cancella noleggio auto — ognuno gestito da un sotto-agente. |
| **Sistemi Multi-Agente (MAS)** | Più agenti indipendenti che lavorano insieme (o competono). | Cooperativo: agenti separati gestiscono hotel, voli e intrattenimento. Competitivo: agenti multipli competono per riempire le camere d’hotel al miglior prezzo. |

---

## Quando Usare gli Agenti AI

Solo perché *puoi* usare un Agente AI non significa che *dovresti* sempre farlo. Ecco le situazioni in cui gli agenti brillano davvero:

![Quando usare gli Agenti AI?](../../../translated_images/it/when-to-use-ai-agents.54becb3bed74a479.webp)

- **Problemi a Apertura Indefinita** — Quando i passaggi per risolvere un problema non possono essere pre-programmati. Hai bisogno che l’LLM scopra dinamicamente il percorso.  
- **Processi a Più Passi** — Compiti che richiedono l’uso di strumenti in più turni, non solo una singola ricerca o generazione.  
- **Miglioramento nel Tempo** — Quando vuoi che il sistema diventi più intelligente basandosi su feedback degli utenti o segnali ambientali.  

Approfondiremo quando (e quando *non*) usare Agenti AI nella lezione **Costruire Agenti AI Affidabili** più avanti nel corso.

---

## Nozioni Base sulle Soluzioni Agentiche

### Sviluppo dell’Agente

La prima cosa che fai costruendo un agente è definire *cosa può fare* — i suoi strumenti, azioni e comportamenti.

In questo corso, usiamo il **Azure AI Agent Service** come piattaforma principale. Supporta:

- Modelli aperti come OpenAI, Mistral e Llama  
- Dati con licenza da provider come Tripadvisor  
- Definizioni di strumenti standardizzate OpenAPI 3.0  

### Pattern Agentici

Comunicare con gli LLM avviene tramite prompt. Con gli agenti, non puoi sempre creare ogni prompt manualmente — l’agente deve agire su molti passaggi. Qui entrano in gioco i **Pattern Agentici**. Sono strategie riutilizzabili per promptare e orchestrare gli LLM in modo più scalabile e affidabile.

Questo corso è strutturato attorno ai pattern agentici più comuni e utili.

### Framework Agentici

I Framework Agentici offrono agli sviluppatori modelli, strumenti e infrastrutture pronti all’uso per costruire agenti. Rendono più facile:

- Collegare strumenti e capacità  
- Osservare cosa fa l’agente (e fare debug in caso di errori)  
- Collaborare tra più agenti  

In questo corso, ci concentriamo sul **Microsoft Agent Framework (MAF)** per costruire agenti pronti per la produzione.

---

## Esempi di Codice

Pronto a vederlo in azione? Ecco gli esempi di codice per questa lezione:

- 🐍 Python: [Agent Framework](./code_samples/01-python-agent-framework.ipynb)  
- 🔷 .NET: [Agent Framework](./code_samples/01-dotnet-agent-framework.md)  

---

## Hai Domande?

Unisciti al [Microsoft Foundry Discord](https://aka.ms/ai-agents/discord) per connetterti con altri studenti, partecipare alle ore d’ufficio, e far rispondere la community alle tue domande sugli Agenti AI.

---

## Lezione Precedente

[Setup del Corso](../00-course-setup/README.md)

## Lezione Successiva

[Esplorare i Framework Agentici](../02-explore-agentic-frameworks/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:  
Questo documento è stato tradotto utilizzando il servizio di traduzione AI [Co-op Translator](https://github.com/Azure/co-op-translator). Anche se ci impegniamo per garantire l’accuratezza, si prega di tenere presente che le traduzioni automatiche possono contenere errori o imprecisioni. Il documento originale nella lingua nativa deve essere considerato la fonte autorevole. Per informazioni critiche, si raccomanda una traduzione professionale effettuata da un umano. Non siamo responsabili per eventuali malintesi o interpretazioni errate derivanti dall’uso di questa traduzione.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->