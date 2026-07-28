[![Introduzione agli Agenti AI](../../../translated_images/it/lesson-1-thumbnail.d21b2c34b32d35bb.webp)](https://youtu.be/3zgm60bXmQk?si=QA4CW2-cmul5kk3D)

> _(Clicca sull'immagine sopra per guardare il video di questa lezione)_

# Introduzione agli Agenti AI e Casi d'Uso degli Agenti

Benvenuto al corso **Agenti AI per Principianti**! Questo corso ti fornisce le conoscenze fondamentali — e codice funzionante reale — per iniziare a costruire Agenti AI da zero.

Vieni a salutarci nella <a href="https://discord.gg/kzRShWzttr" target="_blank">Community Discord di Azure AI</a> — è piena di studenti e creatori di AI felici di rispondere alle domande.

Prima di iniziare a costruire, assicuriamoci di capire effettivamente cos'è un Agente AI e quando ha senso usarne uno.

---

## Introduzione

Questa lezione tratta:

- Cosa sono gli Agenti AI e i diversi tipi che esistono
- Per quali tipi di compiti gli Agenti AI sono più adatti
- I componenti fondamentali che userai nel progettare una soluzione agentica

## Obiettivi di Apprendimento

Alla fine di questa lezione, dovresti essere in grado di:

- Spiegare cos'è un Agente AI e in che modo è diverso da una soluzione AI tradizionale
- Sapere quando utilizzare un Agente AI (e quando non farlo)
- Abbozzare una progettazione base di una soluzione agentica per un problema reale

---

## Definizione degli Agenti AI e Tipi di Agenti AI

### Cosa sono gli Agenti AI?

Ecco un modo semplice per pensarci:

> **Gli Agenti AI sono sistemi che permettono ai Large Language Models (LLM) di *fare cose* — fornendo loro strumenti e conoscenze per agire sul mondo, non solo rispondere a richieste.**

Approfondiamo un po':

- **Sistema** — Un Agente AI non è solo una cosa. È un insieme di parti che lavorano insieme. Alla base, ogni agente ha tre componenti:
  - **Ambiente** — Lo spazio in cui l’agente opera. Per un agente di prenotazione viaggi, sarebbe la piattaforma di prenotazione stessa.
  - **Sensori** — Come l’agente legge lo stato attuale del suo ambiente. Il nostro agente di viaggi potrebbe controllare la disponibilità degli hotel o i prezzi dei voli.
  - **Attuatori** — Come l’agente compie azioni. L’agente di viaggi potrebbe prenotare una stanza, inviare una conferma o cancellare una prenotazione.

![Cosa Sono gli Agenti AI?](../../../translated_images/it/what-are-ai-agents.1ec8c4d548af601a.webp)

- **Large Language Models** — Gli agenti esistevano prima degli LLM, ma sono gli LLM che rendono gli agenti moderni così potenti. Possono comprendere il linguaggio naturale, ragionare sul contesto e trasformare una richiesta vaga dell'utente in un piano d'azione concreto.

- **Eseguire Azioni** — Senza un sistema agente, un LLM genera solo testo. All'interno di un sistema agente, l’LLM può effettivamente *eseguire* passi — cercare in un database, chiamare un API, inviare un messaggio.

- **Accesso agli Strumenti** — Gli strumenti che l’agente può usare dipendono da (1) l’ambiente in cui opera e (2) cosa lo sviluppatore ha deciso di fornire. Un agente di viaggi potrebbe cercare voli ma non modificare i record clienti — tutto dipende da cosa colleghi.

- **Memoria + Conoscenza** — Gli agenti possono avere memoria a breve termine (la conversazione corrente) e memoria a lungo termine (un database clienti, interazioni passate). L’agente di viaggi potrebbe "ricordare" che preferisci i posti vicino al finestrino.

---

### I Diversi Tipi di Agenti AI

Non tutti gli agenti sono costruiti allo stesso modo. Ecco una panoramica dei tipi principali, usando un agente di prenotazione viaggi come esempio continuo:

| **Tipo di Agente** | **Cosa Fa** | **Esempio Agente Viaggi** |
|---|---|---|
| **Agenti Riflessi Semplici** | Segue regole fisse — niente memoria, niente pianificazione. | Vede una email di reclamo → la inoltra al servizio clienti. Fine. |
| **Agenti Riflessi Basati su Modello** | Mantiene un modello interno del mondo e lo aggiorna con i cambiamenti. | Tiene traccia dei prezzi storici dei voli e segnala rotte improvvisamente costose. |
| **Agenti Basati su Obiettivi** | Ha un obiettivo e capisce come raggiungerlo passo dopo passo. | Prenota un viaggio completo (voli, auto, hotel) partendo dalla tua posizione attuale per portarti a destinazione. |
| **Agenti Basati su Utilità** | Non trova solo *una* soluzione — trova la *migliore* valutando i compromessi. | Bilancia costo e comodità per trovare il viaggio che meglio soddisfa le tue preferenze. |
| **Agenti che Apprendono** | Migliora nel tempo imparando dal feedback. | Adatta le raccomandazioni future basandosi sui risultati dei sondaggi post-viaggio. |
| **Agenti Gerarchici** | Un agente di alto livello suddivide il lavoro in sotto-compiti e li delega ad agenti di livello inferiore. | Una richiesta di "cancellare viaggio" viene divisa in: cancella volo, cancella hotel, cancella noleggio auto — ciascuno gestito da un sotto-agente. |
| **Sistemi Multi-Agente (MAS)** | Molti agenti indipendenti che lavorano insieme (o competono). | Cooperativo: agenti separati gestiscono hotel, voli e intrattenimento. Competitivo: vari agenti competono per riempire stanze d’hotel al miglior prezzo. |

---

## Quando Usare gli Agenti AI

Solo perché *puoi* usare un Agente AI non significa che *dovresti* sempre farlo. Ecco le situazioni in cui gli agenti danno il meglio:

![Quando usare gli Agenti AI?](../../../translated_images/it/when-to-use-ai-agents.54becb3bed74a479.webp)

- **Problemi a Risposta Aperta** — Quando i passi per risolvere un problema non possono essere programmati a priori. Hai bisogno che l’LLM trovi dinamicamente il percorso.
- **Processi a Passi Multipli** — Compiti che richiedono l’uso di strumenti attraverso vari passaggi, non solo una singola ricerca o generazione.
- **Miglioramento nel Tempo** — Quando vuoi che il sistema diventi più intelligente grazie al feedback degli utenti o segnali ambientali.

Approfondiremo quando (e quando *non*) usare Agenti AI nella lezione **Costruire Agenti AI Affidabili** più avanti nel corso.

---

## Nozioni Base sulle Soluzioni Agentiche

### Sviluppo di Agenti

La prima cosa da fare quando costruisci un agente è definire *cosa può fare* — i suoi strumenti, azioni e comportamenti.

In questo corso, usiamo il **Microsoft Foundry Agent Service** come piattaforma principale. Supporta:

- Modelli da provider come OpenAI, Mistral e Meta (Llama)
- Dati autorizzati da provider come Tripadvisor
- Definizioni di strumenti standardizzate OpenAPI 3.0

### Schemi Agentici

Comunichi con gli LLM tramite prompt. Con gli agenti, non puoi sempre creare manualmente ogni singolo prompt — l’agente deve agire attraverso molti passi. Ecco dove entrano in gioco gli **Schemi Agentici**. Sono strategie riutilizzabili per guidare e orchestrare gli LLM in modo più scalabile e affidabile.

Questo corso è strutturato attorno agli schemi agentici più comuni e utili.

### Framework Agentici

I Framework Agentici forniscono agli sviluppatori modelli pronti, strumenti e infrastruttura per costruire agenti. Rendono più facile:

- Collegare strumenti e capacità
- Osservare cosa sta facendo l’agente (e fare debug se qualcosa va storto)
- Collaborare tra più agenti

In questo corso, ci concentriamo sul **Microsoft Agent Framework (MAF)** per costruire agenti pronti per la produzione.

---

## Esempi di Codice

Pronto a vederlo in azione? Ecco gli esempi di codice per questa lezione:

- 🐍 Python: [Agent Framework](./code_samples/01-python-agent-framework.ipynb)
- 🔷 .NET: [Agent Framework](./code_samples/01-dotnet-agent-framework.md)

---

## Hai Domande?

Unisciti al [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D) per connetterti con altri studenti, partecipare alle ore di ufficio, e ottenere risposte alle tue domande sugli Agenti AI dalla community.


---

## Test Rapido di Questo Agente (Opzionale)

Una volta imparato a distribuire agenti in [Lezione 16](../16-deploying-scalable-agents/README.md), puoi aggiungere un rapido controllo post-distribuzione per l’`TravelAgent` di questa lezione con il catalogo pronto [`tests/lesson-01-smoke-tests.json`](../../../tests/lesson-01-smoke-tests.json). Vedi [`tests/README.md`](../tests/README.md) per come eseguirlo.

---

## Lezione Precedente

[Installazione del Corso](../00-course-setup/README.md)

## Lezione Successiva

[Esplorare Framework Agentici](../02-explore-agentic-frameworks/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:
Questo documento è stato tradotto utilizzando il servizio di traduzione AI [Co-op Translator](https://github.com/Azure/co-op-translator). Sebbene ci impegniamo per garantire la precisione, si prega di notare che le traduzioni automatizzate possono contenere errori o imprecisioni. Il documento originale nella sua lingua nativa deve essere considerato la fonte autorevole. Per informazioni critiche, si raccomanda una traduzione professionale effettuata da un essere umano. Non siamo responsabili per eventuali malintesi o interpretazioni errate derivanti dall’uso di questa traduzione.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->