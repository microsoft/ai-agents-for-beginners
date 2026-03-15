[![Introduzione agli Agenti AI](../../../translated_images/it/lesson-1-thumbnail.d21b2c34b32d35bb.webp)](https://youtu.be/3zgm60bXmQk?si=QA4CW2-cmul5kk3D)

> _(Fai clic sull'immagine sopra per guardare il video di questa lezione)_


# Introduzione agli Agenti AI e Casi d'Uso degli Agenti

Benvenuti al corso "AI Agents for Beginners"! Questo corso fornisce conoscenze fondamentali ed esempi applicati per la creazione di Agenti AI.

Unisciti alla <a href="https://discord.gg/kzRShWzttr" target="_blank">Community Discord di Azure AI</a> per incontrare altri studenti e costruttori di Agenti AI e porre qualsiasi domanda tu abbia su questo corso.

Per iniziare questo corso, cominciamo con una migliore comprensione di cosa sono gli Agenti AI e di come possiamo usarli nelle applicazioni e nei flussi di lavoro che creiamo.

## Introduzione

Questa lezione copre:

- Cosa sono gli Agenti AI e quali sono i diversi tipi di agenti?
- Per quali casi d'uso sono più adatti gli Agenti AI e come possono aiutarci?
- Quali sono alcuni dei blocchi di base quando si progettano soluzioni agentiche?

## Obiettivi di apprendimento
Al termine di questa lezione, dovresti essere in grado di:

- Comprendere i concetti degli Agenti AI e come si differenziano da altre soluzioni AI.
- Applicare gli Agenti AI nel modo più efficiente.
- Progettare soluzioni agentiche in modo produttivo sia per gli utenti che per i clienti.

## Definizione di Agenti AI e Tipi di Agenti AI

### Cosa sono gli Agenti AI?

Gli Agenti AI sono **sistemi** che permettono ai **Modelli Linguistici di Grandi Dimensioni(LLMs)** di **eseguire azioni** estendendo le loro capacità fornendo ai LLMs **accesso a strumenti** e **conoscenza**.

Suddividiamo questa definizione in parti più piccole:

- **Sistema** - È importante pensare agli agenti non come a un singolo componente ma come a un sistema di molti componenti. A livello base, i componenti di un Agente AI sono:
  - **Ambiente** - Lo spazio definito in cui l'Agente AI opera. Per esempio, se avessimo un agente di prenotazione viaggi, l'ambiente potrebbe essere il sistema di prenotazione viaggi che l'Agente AI usa per completare i compiti.
  - **Sensori** - Gli ambienti hanno informazioni e forniscono feedback. Gli Agenti AI usano sensori per raccogliere e interpretare queste informazioni sullo stato attuale dell'ambiente. Nell'esempio dell'Agente di Prenotazione Viaggi, il sistema di prenotazione può fornire informazioni come la disponibilità degli hotel o i prezzi dei voli.
  - **Attuatori** - Una volta che l'Agente AI riceve lo stato corrente dell'ambiente, per il compito attuale l'agente determina quale azione eseguire per modificare l'ambiente. Per l'agente di prenotazione viaggi, potrebbe essere prenotare una camera disponibile per l'utente.

![Cosa sono gli Agenti AI?](../../../translated_images/it/what-are-ai-agents.1ec8c4d548af601a.webp)

**Large Language Models** - Il concetto di agenti esisteva prima della creazione dei LLMs. Il vantaggio di costruire Agenti AI con i LLMs è la loro capacità di interpretare il linguaggio umano e i dati. Questa capacità permette ai LLMs di interpretare le informazioni ambientali e definire un piano per modificare l'ambiente.

**Eseguire Azioni** - Al di fuori dei sistemi Agente AI, i LLMs sono limitati a situazioni in cui l'azione è generare contenuti o informazioni basate sul prompt di un utente. All'interno dei sistemi Agente AI, i LLMs possono portare a termine compiti interpretando la richiesta dell'utente e utilizzando gli strumenti disponibili nel loro ambiente.

**Accesso agli Strumenti** - A quali strumenti il LLM ha accesso è definito da 1) l'ambiente in cui opera e 2) dallo sviluppatore dell'Agente AI. Per il nostro esempio dell'agente di viaggio, gli strumenti dell'agente sono limitati dalle operazioni disponibili nel sistema di prenotazione e/o lo sviluppatore può limitare l'accesso agli strumenti dell'agente ai soli voli.

**Memoria+Conoscenza** - La memoria può essere a breve termine nel contesto della conversazione tra l'utente e l'agente. A lungo termine, al di fuori delle informazioni fornite dall'ambiente, gli Agenti AI possono anche recuperare conoscenze da altri sistemi, servizi, strumenti e persino altri agenti. Nell'esempio dell'agente di viaggio, questa conoscenza potrebbe essere l'informazione sulle preferenze di viaggio dell'utente presente in un database clienti.

### I diversi tipi di agenti

Ora che abbiamo una definizione generale di Agenti AI, analizziamo alcuni tipi specifici di agenti e come verrebbero applicati a un agente di prenotazione viaggi.

| **Agent Type**                | **Description**                                                                                                                       | **Example**                                                                                                                                                                                                                   |
| ----------------------------- | ------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Simple Reflex Agents**      | Perform immediate actions based on predefined rules.                                                                                  | Travel agent interprets the context of the email and forwards travel complaints to customer service.                                                                                                                          |
| **Model-Based Reflex Agents** | Perform actions based on a model of the world and changes to that model.                                                              | Travel agent prioritizes routes with significant price changes based on access to historical pricing data.                                                                                                             |
| **Goal-Based Agents**         | Create plans to achieve specific goals by interpreting the goal and determining actions to reach it.                                  | Travel agent books a journey by determining necessary travel arrangements (car, public transit, flights) from the current location to the destination.                                                                                |
| **Utility-Based Agents**      | Consider preferences and weigh tradeoffs numerically to determine how to achieve goals.                                               | Travel agent maximizes utility by weighing convenience vs. cost when booking travel.                                                                                                                                          |
| **Learning Agents**           | Improve over time by responding to feedback and adjusting actions accordingly.                                                        | Travel agent improves by using customer feedback from post-trip surveys to make adjustments to future bookings.                                                                                                               |
| **Hierarchical Agents**       | Feature multiple agents in a tiered system, with higher-level agents breaking tasks into subtasks for lower-level agents to complete. | Travel agent cancels a trip by dividing the task into subtasks (for example, canceling specific bookings) and having lower-level agents complete them, reporting back to the higher-level agent.                                     |
| **Multi-Agent Systems (MAS)** | Agents complete tasks independently, either cooperatively or competitively.                                                           | Cooperative: Multiple agents book specific travel services such as hotels, flights, and entertainment. Competitive: Multiple agents manage and compete over a shared hotel booking calendar to book customers into the hotel. |

## Quando usare gli Agenti AI

Nella sezione precedente, abbiamo usato il caso d'uso dell'Agente di Viaggio per spiegare come i diversi tipi di agenti possono essere utilizzati in differenti scenari di prenotazione di viaggi. Continueremo a usare questa applicazione durante il corso.

Vediamo i tipi di casi d'uso per i quali gli Agenti AI sono più indicati:

![Quando usare gli Agenti AI?](../../../translated_images/it/when-to-use-ai-agents.54becb3bed74a479.webp)


- **Problemi aperti** - consentire al LLM di determinare i passaggi necessari per completare un compito perché non sempre possono essere codificati rigidamente in un flusso di lavoro.
- **Processi a più fasi** - attività che richiedono un livello di complessità in cui l'Agente AI deve utilizzare strumenti o informazioni su più interazioni invece di un recupero in singola soluzione.  
- **Miglioramento nel tempo** - attività in cui l'agente può migliorare nel tempo ricevendo feedback dall'ambiente o dagli utenti per offrire una maggiore utilità.

Affronteremo ulteriori considerazioni sull'uso degli Agenti AI nella lezione Costruire Agenti AI Affidabili.

## Nozioni di base sulle soluzioni agentiche

### Sviluppo degli agenti

Il primo passo nella progettazione di un sistema Agente AI è definire gli strumenti, le azioni e i comportamenti. In questo corso, ci concentriamo sull'utilizzo del **Azure AI Agent Service** per definire i nostri Agenti. Offre funzionalità come:

- Selezione di modelli aperti come OpenAI, Mistral e Llama
- Utilizzo di dati con licenza tramite fornitori come Tripadvisor
- Utilizzo di strumenti standardizzati OpenAPI 3.0

### Pattern agentici

La comunicazione con i LLM avviene tramite prompt. Data la natura semi-autonoma degli Agenti AI, non è sempre possibile o necessario ripromptare manualmente il LLM dopo un cambiamento nell'ambiente. Utilizziamo **Pattern agentici** che ci permettono di inviare prompt al LLM su più passaggi in modo più scalabile.

Questo corso è suddiviso in alcuni dei pattern agentici attualmente più popolari.

### Framework agentici

I framework agentici consentono agli sviluppatori di implementare i pattern agentici tramite codice. Questi framework offrono template, plugin e strumenti per una migliore collaborazione tra Agenti AI. Questi vantaggi permettono una migliore osservabilità e risoluzione dei problemi dei sistemi Agente AI.

In questo corso esploreremo il Microsoft Agent Framework (MAF) per costruire agenti AI pronti per la produzione.

## Esempi di codice

- Python: [Framework per agenti](./code_samples/01-python-agent-framework.ipynb)
- .NET: [Framework per agenti](./code_samples/01-dotnet-agent-framework.md)

## Hai altre domande sugli Agenti AI?

Unisciti al [Discord di Microsoft Foundry](https://aka.ms/ai-agents/discord) per incontrare altri studenti, partecipare alle ore d'ufficio e ottenere risposte alle tue domande sugli Agenti AI.

## Lezione precedente

[Configurazione del corso](../00-course-setup/README.md)

## Lezione successiva

[Esplorazione dei framework agentici](../02-explore-agentic-frameworks/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
Dichiarazione di non responsabilità:
Questo documento è stato tradotto utilizzando il servizio di traduzione basato su intelligenza artificiale [Co-op Translator](https://github.com/Azure/co-op-translator). Pur facendo del nostro meglio per garantirne l'accuratezza, si prega di notare che le traduzioni automatiche possono contenere errori o inesattezze. Il documento originale nella sua lingua d'origine deve essere considerato la fonte autorevole. Per informazioni critiche è consigliata una traduzione professionale a cura di un traduttore umano. Non siamo responsabili per eventuali incomprensioni o interpretazioni errate derivanti dall'uso di questa traduzione.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->