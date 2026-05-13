[![Intro to AI Agents](../../../translated_images/it/lesson-1-thumbnail.d21b2c34b32d35bb.webp)](https://youtu.be/3zgm60bXmQk?si=QA4CW2-cmul5kk3D)

> _(Fai clic sull'immagine sopra per guardare il video di questa lezione)_

# Introduzione agli Agenti AI e ai Casi d'Uso degli Agenti

Benvenuto al corso **Agenti AI per Principianti**! Questo corso ti fornisce le conoscenze di base — e codice funzionante reale — per iniziare a costruire Agenti AI da zero.

Vieni a salutarci nella <a href="https://discord.gg/kzRShWzttr" target="_blank">Community Discord di Azure AI</a> — è piena di studenti e sviluppatori AI pronti a rispondere alle tue domande.

Prima di iniziare a costruire, assicuriamoci di capire davvero cos'è un Agente AI e quando ha senso usarne uno.

---

## Introduzione

Questa lezione copre:

- Cosa sono gli Agenti AI e i diversi tipi che esistono
- Per quali tipi di attività gli Agenti AI sono più adatti
- I blocchi costitutivi fondamentali che utilizzerai nel progettare una soluzione Agentica

## Obiettivi di Apprendimento

Al termine di questa lezione, dovresti essere in grado di:

- Spiegare cos'è un Agente AI e come si differenzia da una soluzione AI normale
- Sapere quando è opportuno utilizzare un Agente AI (e quando no)
- Progettare a grandi linee una soluzione Agentica di base per un problema reale

---

## Definizione degli Agenti AI e Tipi di Agenti AI

### Cosa sono gli Agenti AI?

Ecco un modo semplice per pensarci:

> **Gli Agenti AI sono sistemi che permettono ai Large Language Models (LLM) di *fare cose* — offrendo loro strumenti e conoscenze per agire sul mondo, non solo rispondere a prompt.**

Approfondiamo un po':

- **Sistema** — Un Agente AI non è solo una cosa singola. È un insieme di parti che lavorano insieme. Alla base, ogni agente ha tre componenti:
  - **Ambiente** — Lo spazio in cui l'agente opera. Per un agente di prenotazioni di viaggio, sarebbe la piattaforma di prenotazione stessa.
  - **Sensori** — Come l'agente legge lo stato attuale del suo ambiente. Il nostro agente di viaggio potrebbe controllare la disponibilità degli hotel o i prezzi dei voli.
  - **Attuatori** — Come l'agente prende azione. L'agente di viaggio potrebbe prenotare una camera, inviare una conferma o cancellare una prenotazione.

![What Are AI Agents?](../../../translated_images/it/what-are-ai-agents.1ec8c4d548af601a.webp)

- **Large Language Models** — Gli agenti esistevano prima degli LLM, ma sono gli LLM ciò che rende gli agenti moderni così potenti. Possono comprendere il linguaggio naturale, ragionare sul contesto e trasformare una richiesta vaga dell'utente in un piano d'azione concreto.

- **Eseguire Azioni** — Senza un sistema agente, un LLM genera solo testo. All'interno di un sistema agente, l'LLM può effettivamente *eseguire* passaggi — cercare in un database, chiamare un'API, inviare un messaggio.

- **Accesso a Strumenti** — Gli strumenti che l'agente può usare dipendono da (1) l'ambiente in cui gira e (2) cosa lo sviluppatore ha deciso di dargli. Un agente di viaggio potrebbe cercare voli ma non modificare i record clienti — dipende da cosa configuri.

- **Memoria + Conoscenza** — Gli agenti possono avere memoria a breve termine (la conversazione attuale) e memoria a lungo termine (un database clienti, interazioni passate). L'agente di viaggio potrebbe "ricordare" che preferisci i posti vicino al finestrino.

---

### I Diversi Tipi di Agenti AI

Non tutti gli agenti sono costruiti allo stesso modo. Ecco una panoramica dei principali tipi, usando un agente di prenotazioni di viaggio come esempio:

| **Tipo di Agente** | **Cosa Fa** | **Esempio Agente di Viaggio** |
|---|---|---|
| **Agenti a Riflesso Semplice** | Segue regole fisse — senza memoria, senza pianificazione. | Riceve un'email di reclamo → la inoltra al servizio clienti. Fine. |
| **Agenti a Riflesso Basati su Modello** | Tiene un modello interno del mondo e lo aggiorna quando le cose cambiano. | Tiene traccia dei prezzi storici dei voli e segnala rotte che diventano improvvisamente costose. |
| **Agenti Basati su Obiettivi** | Ha un obiettivo in mente e capisce come raggiungerlo passo dopo passo. | Prenota un viaggio completo (voli, auto, hotel) partendo dal tuo punto attuale per portarti a destinazione. |
| **Agenti Basati su Utilità** | Non trova solo *una* soluzione — trova la *migliore* valutando i compromessi. | Bilancia costo vs. comodità per trovare il viaggio che soddisfa al meglio le tue preferenze. |
| **Agenti di Apprendimento** | Migliora col tempo apprendendo dai feedback. | Regola le raccomandazioni di prenotazione future in base ai risultati di sondaggi post-viaggio. |
| **Agenti Gerarchici** | Un agente di alto livello divide il lavoro in sotto-compiti e li delega ad agenti di livello inferiore. | Una richiesta "cancella viaggio" si divide in: cancella volo, cancella hotel, cancella noleggio auto — ciascuno gestito da un sotto-agente. |
| **Sistemi Multi-Agente (MAS)** | Più agenti indipendenti che lavorano insieme (o in competizione). | Cooperativo: agenti separati gestiscono hotel, voli e intrattenimento. Competitivo: più agenti competono per riempire camere d'hotel al miglior prezzo. |

---

## Quando Usare gli Agenti AI

Non perché *puoi* usare un Agente AI significa che *dovresti* sempre usarlo. Ecco le situazioni in cui gli agenti brillano davvero:

![When to use AI Agents?](../../../translated_images/it/when-to-use-ai-agents.54becb3bed74a479.webp)

- **Problemi a Senso Aperto** — Quando i passaggi per risolvere un problema non possono essere pre-programmati. Hai bisogno che l'LLM trovi dinamicamente il percorso.
- **Processi Multi-Passo** — Attività che richiedono l'uso di strumenti attraverso più turni, non solo una semplice ricerca o generazione.
- **Miglioramento nel Tempo** — Quando vuoi che il sistema diventi più intelligente basandosi sui feedback degli utenti o segnali ambientali.

Approfondiremo quando (e quando *non*) usare gli Agenti AI nella lezione **Costruire Agenti AI Affidabili** più avanti nel corso.

---

## Nozioni Base delle Soluzioni Agentiche

### Sviluppo degli Agenti

La prima cosa che fai costruendo un agente è definire *cosa può fare* — i suoi strumenti, azioni e comportamenti.

In questo corso, utilizziamo il **Azure AI Agent Service** come piattaforma principale. Supporta:

- Modelli di provider come OpenAI, Mistral e Meta (Llama)
- Dati con licenza da provider come Tripadvisor
- Definizioni di strumenti standardizzate OpenAPI 3.0

### Pattern Agentici

Comunichi con gli LLM tramite prompt. Con gli agenti, non puoi sempre creare manualmente ogni prompt — l'agente deve agire su molti passaggi. Ecco dove entrano i **Pattern Agentici**. Sono strategie riutilizzabili per promptare e orchestrare gli LLM in modo più scalabile e affidabile.

Questo corso si struttura intorno ai pattern agentici più comuni e utili.

### Framework Agentici

I Framework Agentici forniscono agli sviluppatori template pronti, strumenti e infrastruttura per costruire agenti. Rende più facile:

- Collegare strumenti e capacità
- Osservare cosa fa l'agente (e fare debug se qualcosa va storto)
- Collaborare tra più agenti

In questo corso ci concentriamo sul **Microsoft Agent Framework (MAF)** per costruire agenti pronti per la produzione.

---

## Esempi di Codice

Pronto a vederlo in azione? Ecco gli esempi di codice per questa lezione:

- 🐍 Python: [Agent Framework](./code_samples/01-python-agent-framework.ipynb)
- 🔷 .NET: [Agent Framework](./code_samples/01-dotnet-agent-framework.md)

---

## Hai Domande?

Unisciti al [Microsoft Foundry Discord](https://aka.ms/ai-agents/discord) per connetterti con altri studenti, partecipare a sessioni di office hours e ottenere risposte alle tue domande sugli Agenti AI dalla community.

---

## Lezione Precedente

[Course Setup](../00-course-setup/README.md)

## Lezione Successiva

[Exploring Agentic Frameworks](../02-explore-agentic-frameworks/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:
Questo documento è stato tradotto utilizzando il servizio di traduzione AI [Co-op Translator](https://github.com/Azure/co-op-translator). Sebbene ci impegniamo per garantire la precisione, si prega di notare che le traduzioni automatizzate possono contenere errori o imprecisioni. Il documento originale nella sua lingua nativa deve essere considerato la fonte autorevole. Per informazioni critiche, si raccomanda una traduzione professionale effettuata da un essere umano. Non siamo responsabili per eventuali malintesi o interpretazioni errate derivanti dall’uso di questa traduzione.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->