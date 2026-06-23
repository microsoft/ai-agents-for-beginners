[![Agent affidabili di IA](../../../translated_images/it/lesson-6-thumbnail.a58ab36c099038d4.webp)](https://youtu.be/iZKkMEGBCUQ?si=Q-kEbcyHUMPoHp8L)

> _(Clicca sull'immagine sopra per vedere il video di questa lezione)_

# Costruire agenti di IA affidabili

## Introduzione

Questa lezione tratterà:

- Come costruire e distribuire agenti di IA sicuri ed efficaci
- Importanti considerazioni sulla sicurezza nello sviluppo di agenti di IA.
- Come mantenere la privacy dei dati e degli utenti durante lo sviluppo di agenti di IA.

## Obiettivi di apprendimento

Dopo aver completato questa lezione, saprai come:

- Identificare e mitigare i rischi nella creazione di agenti di IA.
- Implementare misure di sicurezza per assicurare che i dati e gli accessi siano gestiti correttamente.
- Creare agenti di IA che mantengano la privacy dei dati e offrano un'esperienza utente di qualità.

## Sicurezza

Esaminiamo prima come costruire applicazioni agentiche sicure. La sicurezza significa che l'agente di IA funziona come progettato. In quanto costruttori di applicazioni agentiche, abbiamo metodi e strumenti per massimizzare la sicurezza:

### Costruire un framework di messaggi di sistema

Se hai mai costruito un'applicazione di IA utilizzando Large Language Models (LLM), conosci l'importanza di progettare un prompt di sistema o un messaggio di sistema robusto. Questi prompt stabiliscono le regole meta, istruzioni e linee guida su come l'LLM interagirà con l'utente e i dati.

Per gli agenti di IA, il prompt di sistema è ancora più importante poiché gli agenti di IA necessiteranno di istruzioni altamente specifiche per completare i compiti da noi progettati.

Per creare prompt di sistema scalabili, possiamo usare un framework di messaggi di sistema per costruire uno o più agenti nella nostra applicazione:

![Costruire un framework di messaggi di sistema](../../../translated_images/it/system-message-framework.3a97368c92d11d68.webp)

#### Passo 1: Creare un messaggio meta di sistema 

Il meta prompt verrà usato da un LLM per generare i prompt di sistema per gli agenti che creiamo. Lo progettiamo come un modello in modo da poter creare efficientemente più agenti se necessario.

Ecco un esempio di messaggio meta di sistema che forniremmo all'LLM:

```plaintext
You are an expert at creating AI agent assistants. 
You will be provided a company name, role, responsibilities and other
information that you will use to provide a system prompt for.
To create the system prompt, be descriptive as possible and provide a structure that a system using an LLM can better understand the role and responsibilities of the AI assistant. 
```

#### Passo 2: Creare un prompt di base

Il passo successivo è creare un prompt di base per descrivere l'agente di IA. Dovresti includere il ruolo dell'agente, i compiti che l'agente completerà e qualsiasi altra responsabilità dell'agente.

Ecco un esempio:

```plaintext
You are a travel agent for Contoso Travel that is great at booking flights for customers. To help customers you can perform the following tasks: lookup available flights, book flights, ask for preferences in seating and times for flights, cancel any previously booked flights and alert customers on any delays or cancellations of flights.  
```

#### Passo 3: Fornire il messaggio di sistema di base all'LLM

Ora possiamo ottimizzare questo messaggio di sistema fornendo il messaggio meta come messaggio di sistema insieme al nostro messaggio di sistema di base.

Questo produrrà un messaggio di sistema meglio progettato per guidare i nostri agenti di IA:

```markdown
**Company Name:** Contoso Travel  
**Role:** Travel Agent Assistant

**Objective:**  
You are an AI-powered travel agent assistant for Contoso Travel, specializing in booking flights and providing exceptional customer service. Your main goal is to assist customers in finding, booking, and managing their flights, all while ensuring that their preferences and needs are met efficiently.

**Key Responsibilities:**

1. **Flight Lookup:**
    
    - Assist customers in searching for available flights based on their specified destination, dates, and any other relevant preferences.
    - Provide a list of options, including flight times, airlines, layovers, and pricing.
2. **Flight Booking:**
    
    - Facilitate the booking of flights for customers, ensuring that all details are correctly entered into the system.
    - Confirm bookings and provide customers with their itinerary, including confirmation numbers and any other pertinent information.
3. **Customer Preference Inquiry:**
    
    - Actively ask customers for their preferences regarding seating (e.g., aisle, window, extra legroom) and preferred times for flights (e.g., morning, afternoon, evening).
    - Record these preferences for future reference and tailor suggestions accordingly.
4. **Flight Cancellation:**
    
    - Assist customers in canceling previously booked flights if needed, following company policies and procedures.
    - Notify customers of any necessary refunds or additional steps that may be required for cancellations.
5. **Flight Monitoring:**
    
    - Monitor the status of booked flights and alert customers in real-time about any delays, cancellations, or changes to their flight schedule.
    - Provide updates through preferred communication channels (e.g., email, SMS) as needed.

**Tone and Style:**

- Maintain a friendly, professional, and approachable demeanor in all interactions with customers.
- Ensure that all communication is clear, informative, and tailored to the customer's specific needs and inquiries.

**User Interaction Instructions:**

- Respond to customer queries promptly and accurately.
- Use a conversational style while ensuring professionalism.
- Prioritize customer satisfaction by being attentive, empathetic, and proactive in all assistance provided.

**Additional Notes:**

- Stay updated on any changes to airline policies, travel restrictions, and other relevant information that could impact flight bookings and customer experience.
- Use clear and concise language to explain options and processes, avoiding jargon where possible for better customer understanding.

This AI assistant is designed to streamline the flight booking process for customers of Contoso Travel, ensuring that all their travel needs are met efficiently and effectively.

```

#### Passo 4: Iterare e migliorare

Il valore di questo framework di messaggi di sistema è poter scalare la creazione di messaggi di sistema da più agenti più facilmente e migliorare i tuoi messaggi di sistema nel tempo. È raro avere un messaggio di sistema che funzioni alla prima volta per il tuo caso d'uso completo. Essere in grado di fare piccoli aggiustamenti e miglioramenti cambiando il messaggio di sistema di base e eseguendolo attraverso il sistema ti permette di confrontare e valutare i risultati.

## Comprendere le minacce

Per costruire agenti di IA affidabili, è importante comprendere e mitigare i rischi e le minacce al tuo agente di IA. Vediamo alcune delle diverse minacce agli agenti di IA e come puoi pianificare e prepararti meglio per esse.

![Comprendere le minacce](../../../translated_images/it/understanding-threats.89edeada8a97fc0f.webp)

### Compito e istruzione

**Descrizione:** Gli attaccanti tentano di cambiare le istruzioni o gli obiettivi dell'agente di IA attraverso prompting o manipolazione degli input.

**Mitigazione:** Eseguire controlli di validazione e filtri sugli input per rilevare prompt potenzialmente pericolosi prima che vengano elaborati dall'agente di IA. Poiché questi attacchi richiedono normalmente interazioni frequenti con l'agente, limitare il numero di turni in una conversazione è un altro modo per prevenire questo tipo di attacchi.

### Accesso a sistemi critici

**Descrizione:** Se un agente di IA ha accesso a sistemi e servizi che memorizzano dati sensibili, gli attaccanti possono compromettere la comunicazione tra l'agente e questi servizi. Questi possono essere attacchi diretti o tentativi indiretti di ottenere informazioni su tali sistemi attraverso l'agente.

**Mitigazione:** Gli agenti di IA dovrebbero avere accesso ai sistemi solo in base alla necessità per evitare questo tipo di attacchi. La comunicazione tra agente e sistema dovrebbe essere inoltre sicura. Implementare autenticazione e controllo degli accessi è un altro modo per proteggere queste informazioni.

### Sovraccarico di risorse e servizi

**Descrizione:** Gli agenti di IA possono accedere a diversi strumenti e servizi per completare i compiti. Gli attaccanti possono sfruttare questa capacità per attaccare questi servizi inviando un alto volume di richieste attraverso l'agente di IA, che può causare malfunzionamenti del sistema o costi elevati.

**Mitigazione:** Implementare politiche per limitare il numero di richieste che un agente di IA può fare a un servizio. Limitare il numero di turni di conversazione e le richieste al tuo agente di IA è un altro modo per prevenire questi tipi di attacchi.

### Avvelenamento della base di conoscenza

**Descrizione:** Questo tipo di attacco non prende di mira direttamente l'agente di IA ma la base di conoscenza e altri servizi che l'agente utilizzerà. Può comportare la corruzione dei dati o delle informazioni che l'agente di IA userà per completare un compito, portando a risposte faziose o non intenzionali all'utente.

**Mitigazione:** Eseguire regolarmente verifiche dei dati che l'agente di IA userà nei suoi flussi di lavoro. Assicurati che l'accesso a questi dati sia sicuro e che possa essere modificato solo da persone affidabili per evitare questo tipo di attacchi.

### Errori a cascata

**Descrizione:** Gli agenti di IA accedono a vari strumenti e servizi per completare i compiti. Errori causati da attaccanti possono portare a malfunzionamenti di altri sistemi collegati all'agente di IA, causando un attacco più diffuso e difficile da risolvere.

**Mitigazione:** Un metodo per evitare questo è far operare l'agente di IA in un ambiente limitato, ad esempio eseguendo compiti in un container Docker, per prevenire attacchi diretti al sistema. Creare meccanismi di fallback e logiche di ritentativo quando certi sistemi rispondono con un errore è un altro modo per prevenire malfunzionamenti più ampi.

## Uomo nel ciclo

Un altro modo efficace di costruire sistemi agentici di IA affidabili è usare un approccio Human-in-the-loop. Questo crea un flusso in cui gli utenti possono fornire feedback agli agenti durante l'esecuzione. Gli utenti agiscono essenzialmente come agenti in un sistema multi-agente fornendo approvazione o terminazione del processo in esecuzione.

![Uomo nel ciclo](../../../translated_images/it/human-in-the-loop.5f0068a678f62f4f.webp)

Ecco un frammento di codice che usa il Microsoft Agent Framework per mostrare come viene implementato questo concetto:

```python
import os
from agent_framework.azure import AzureAIProjectAgentProvider
from azure.identity import AzureCliCredential

# Crea il provider con approvazione umana in loop
provider = AzureAIProjectAgentProvider(
    credential=AzureCliCredential(),
)

# Crea l'agente con una fase di approvazione umana
response = provider.create_response(
    input="Write a 4-line poem about the ocean.",
    instructions="You are a helpful assistant. Ask for user approval before finalizing.",
)

# L'utente può rivedere e approvare la risposta
print(response.output_text)
user_input = input("Do you approve? (APPROVE/REJECT): ")
if user_input == "APPROVE":
    print("Response approved.")
else:
    print("Response rejected. Revising...")
```

## Conclusione

Costruire agenti di IA affidabili richiede una progettazione attenta, misure di sicurezza robuste e un'iterazione continua. Implementando sistemi strutturati di meta-prompting, comprendendo le potenziali minacce e applicando strategie di mitigazione, gli sviluppatori possono creare agenti di IA sicuri ed efficaci. Inoltre, l'incorporazione di un approccio human-in-the-loop garantisce che gli agenti rimangano allineati ai bisogni degli utenti minimizzando i rischi. Con l'evoluzione dell'IA, mantenere un atteggiamento proattivo su sicurezza, privacy e considerazioni etiche sarà la chiave per favorire fiducia e affidabilità nei sistemi basati su IA.

## Esempi di codice

- [`code_samples/06-system-message-framework.ipynb`](code_samples/06-system-message-framework.ipynb): Dimostrazione passo dopo passo del framework di meta-prompt e messaggio di sistema.
- [`code_samples/06-human-in-the-loop.ipynb`](code_samples/06-human-in-the-loop.ipynb): Gate di approvazione pre-azione, classificazione del rischio e audit logging per agenti affidabili.

### Hai altre domande su come costruire agenti di IA affidabili?

Unisciti al [Microsoft Foundry Discord](https://aka.ms/ai-agents/discord) per incontrare altri studenti, partecipare a ore di ufficio e far rispondere alle tue domande sugli agenti di IA.

## Risorse aggiuntive

- <a href="https://learn.microsoft.com/azure/ai-studio/responsible-use-of-ai-overview" target="_blank">Panoramica sull'IA responsabile</a>
- <a href="https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai" target="_blank">Valutazione di modelli generativi di IA e applicazioni di IA</a>
- <a href="https://learn.microsoft.com/azure/ai-services/openai/concepts/system-message?context=%2Fazure%2Fai-studio%2Fcontext%2Fcontext&tabs=top-techniques" target="_blank">Messaggi di sistema per la sicurezza</a>
- <a href="https://blogs.microsoft.com/wp-content/uploads/prod/sites/5/2022/06/Microsoft-RAI-Impact-Assessment-Template.pdf?culture=en-us&country=us" target="_blank">Modello di valutazione dei rischi</a>

## Lezione precedente

[Agentic RAG](../05-agentic-rag/README.md)

## Lezione successiva

[Design Pattern di pianificazione](../07-planning-design/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:
Questo documento è stato tradotto utilizzando il servizio di traduzione AI [Co-op Translator](https://github.com/Azure/co-op-translator). Sebbene ci impegniamo per garantire la precisione, si prega di notare che le traduzioni automatizzate possono contenere errori o imprecisioni. Il documento originale nella sua lingua nativa deve essere considerato la fonte autorevole. Per informazioni critiche, si raccomanda una traduzione professionale effettuata da un essere umano. Non siamo responsabili per eventuali malintesi o interpretazioni errate derivanti dall’uso di questa traduzione.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->