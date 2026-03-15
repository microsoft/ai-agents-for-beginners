[![Agenti di IA Affidabili](../../../translated_images/it/lesson-6-thumbnail.a58ab36c099038d4.webp)](https://youtu.be/iZKkMEGBCUQ?si=Q-kEbcyHUMPoHp8L)

> _(Clicca sull'immagine sopra per vedere il video di questa lezione)_

# Costruire Agenti di IA Affidabili

## Introduzione

Questa lezione coprirà:

- Come costruire e distribuire Agenti di IA sicuri ed efficaci
- Importanti considerazioni sulla sicurezza nello sviluppo di Agenti di IA.
- Come mantenere la privacy dei dati e degli utenti nello sviluppo di Agenti di IA.

## Obiettivi di Apprendimento

Dopo aver completato questa lezione, saprai come:

- Identificare e mitigare i rischi nella creazione di Agenti di IA.
- Implementare misure di sicurezza per garantire che dati e accessi siano gestiti correttamente.
- Creare Agenti di IA che mantengano la privacy dei dati e offrano un'esperienza utente di qualità.

## Sicurezza

Iniziamo osservando come costruire applicazioni agentiche sicure. La sicurezza significa che l'agente IA si comporta come progettato. Come costruttori di applicazioni agentiche, disponiamo di metodi e strumenti per massimizzare la sicurezza:

### Costruire un Framework di Messaggi di Sistema

Se hai mai costruito un'applicazione IA usando modelli linguistici di grandi dimensioni (LLM), conosci l'importanza di progettare un prompt di sistema o messaggio di sistema robusto. Questi prompt stabiliscono le regole meta, le istruzioni e le linee guida su come l'LLM interagirà con l'utente e i dati.

Per gli Agenti di IA, il prompt di sistema è ancora più importante poiché gli Agenti di IA avranno bisogno di istruzioni altamente specifiche per completare i compiti che abbiamo progettato per loro.

Per creare prompt di sistema scalabili, possiamo utilizzare un framework di messaggi di sistema per costruire uno o più agenti nella nostra applicazione:

![Building a System Message Framework](../../../translated_images/it/system-message-framework.3a97368c92d11d68.webp)

#### Passo 1: Creare un Messaggio Meta di Sistema

Il meta prompt sarà usato da un LLM per generare i prompt di sistema per gli agenti che creiamo. Lo progettiamo come un modello in modo da poter creare in modo efficiente più agenti se necessario.

Ecco un esempio di messaggio meta di sistema che forniremmo all'LLM:

```plaintext
You are an expert at creating AI agent assistants. 
You will be provided a company name, role, responsibilities and other
information that you will use to provide a system prompt for.
To create the system prompt, be descriptive as possible and provide a structure that a system using an LLM can better understand the role and responsibilities of the AI assistant. 
```

#### Passo 2: Creare un prompt di base

Il passo successivo è creare un prompt di base per descrivere l'Agente di IA. Dovresti includere il ruolo dell'agente, i compiti che l'agente eseguirà e qualsiasi altra responsabilità dell'agente.

Ecco un esempio:

```plaintext
You are a travel agent for Contoso Travel that is great at booking flights for customers. To help customers you can perform the following tasks: lookup available flights, book flights, ask for preferences in seating and times for flights, cancel any previously booked flights and alert customers on any delays or cancellations of flights.  
```

#### Passo 3: Fornire il Messaggio di Sistema di Base all'LLM

Ora possiamo ottimizzare questo messaggio di sistema fornendo il messaggio meta di sistema come messaggio di sistema insieme al nostro messaggio di sistema di base.

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

#### Passo 4: Iterare e Migliorare

Il valore di questo framework di messaggi di sistema è poter creare messaggi di sistema da più agenti in modo più facile e migliorare i tuoi messaggi di sistema nel tempo. È raro che tu abbia un messaggio di sistema che funzioni alla prima esecuzione per il tuo caso d'uso completo. Essere in grado di fare piccoli aggiustamenti e miglioramenti modificando il messaggio di sistema di base e facendolo passare attraverso il sistema ti permetterà di confrontare e valutare i risultati.

## Comprendere le Minacce

Per costruire agenti di IA affidabili, è importante capire e mitigare i rischi e le minacce per il tuo agente IA. Vediamo solo alcune delle diverse minacce agli agenti di IA e come puoi pianificare e prepararti meglio.

![Understanding Threats](../../../translated_images/it/understanding-threats.89edeada8a97fc0f.webp)

### Compito e Istruzioni

**Descrizione:** Gli aggressori tentano di modificare le istruzioni o gli obiettivi dell'agente IA tramite prompting o manipolazione degli input.

**Mitigazione**: Esegui controlli di validazione e filtri sugli input per rilevare prompt potenzialmente pericolosi prima che siano elaborati dall'Agente IA. Poiché questi attacchi richiedono tipicamente interazioni frequenti con l'Agente, limitare il numero di turni in una conversazione è un altro modo per prevenire questi tipi di attacchi.

### Accesso a Sistemi Critici

**Descrizione**: Se un agente IA ha accesso a sistemi e servizi che conservano dati sensibili, gli aggressori possono compromettere la comunicazione tra l'agente e questi servizi. Questi possono essere attacchi diretti o tentativi indiretti di ottenere informazioni su questi sistemi tramite l'agente.

**Mitigazione**: Gli agenti IA dovrebbero avere accesso ai sistemi solo se necessario per prevenire questi tipi di attacchi. La comunicazione tra l'agente e il sistema dovrebbe inoltre essere sicura. Implementare autenticazione e controllo degli accessi è un altro modo per proteggere queste informazioni.

### Sovraccarico di Risorse e Servizi

**Descrizione:** Gli agenti IA possono accedere a diversi strumenti e servizi per completare i compiti. Gli aggressori possono usare questa capacità per attaccare questi servizi inviando un alto volume di richieste tramite l'Agente IA, il che può causare malfunzionamenti del sistema o costi elevati.

**Mitigazione:** Implementa politiche per limitare il numero di richieste che un agente IA può fare a un servizio. Limitare il numero di turni di conversazione e le richieste al tuo agente IA è un altro modo per prevenire questi tipi di attacchi.

### Avvelenamento della Base di Conoscenza

**Descrizione:** Questo tipo di attacco non prende di mira direttamente l'agente IA ma la base di conoscenza e altri servizi che l'agente IA utilizzerà. Potrebbe coinvolgere la corruzione dei dati o delle informazioni che l'agente IA userà per completare un compito, portando a risposte distorte o non intenzionali per l'utente.

**Mitigazione:** Effettua verifiche regolari dei dati che l'agente IA userà nei suoi flussi di lavoro. Assicura che l'accesso a questi dati sia sicuro e modificato solo da persone fidate per evitare questo tipo di attacco.

### Errori a Cascata

**Descrizione:** Gli agenti IA accedono a vari strumenti e servizi per completare compiti. Errori causati da aggressori possono portare a malfunzionamenti di altri sistemi connessi all'agente IA, causando un attacco più diffuso e più difficile da risolvere.

**Mitigazione**: Un metodo per evitare ciò è far operare l'Agente IA in un ambiente limitato, come eseguire compiti in un container Docker, per prevenire attacchi diretti ai sistemi. Creare meccanismi di fallback e logiche di ritentativo quando certi sistemi rispondono con un errore è un altro modo per prevenire guasti estesi.

## Human-in-the-Loop

Un altro modo efficace per costruire sistemi di agenti IA affidabili è usare un Human-in-the-loop. Questo crea un flusso dove gli utenti possono fornire feedback agli Agenti durante l’esecuzione. Gli utenti agiscono essenzialmente come agenti in un sistema multi-agente e fornendo approvazione o terminazione del processo in esecuzione.

![Human in The Loop](../../../translated_images/it/human-in-the-loop.5f0068a678f62f4f.webp)

Ecco uno snippet di codice che usa il Microsoft Agent Framework per mostrare come questo concetto è implementato:

```python
import os
from agent_framework.azure import AzureAIProjectAgentProvider
from azure.identity import AzureCliCredential

# Crea il provider con approvazione umana in loop
provider = AzureAIProjectAgentProvider(
    credential=AzureCliCredential(),
)

# Crea l'agente con un passaggio di approvazione umana
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

Costruire agenti di IA affidabili richiede una progettazione accurata, misure di sicurezza robuste e iterazioni continue. Implementando sistemi strutturati di meta prompt, comprendendo le potenziali minacce e applicando strategie di mitigazione, gli sviluppatori possono creare agenti di IA sicuri ed efficaci. Inoltre, incorporare un approccio human-in-the-loop assicura che gli agenti di IA rimangano allineati alle esigenze degli utenti minimizzando i rischi. Con l'evoluzione dell'IA, mantenere un atteggiamento proattivo su sicurezza, privacy e considerazioni etiche sarà fondamentale per favorire fiducia e affidabilità nei sistemi guidati dall'IA.

### Hai altre domande su come costruire Agenti di IA Affidabili?

Unisciti al [Microsoft Foundry Discord](https://aka.ms/ai-agents/discord) per incontrare altri studenti, partecipare alle ore di ufficio e ottenere risposta alle tue domande sugli Agenti di IA.

## Risorse Aggiuntive

- <a href="https://learn.microsoft.com/azure/ai-studio/responsible-use-of-ai-overview" target="_blank">Panoramica sull'IA Responsabile</a>
- <a href="https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai" target="_blank">Valutazione di modelli e applicazioni di IA generativa</a>
- <a href="https://learn.microsoft.com/azure/ai-services/openai/concepts/system-message?context=%2Fazure%2Fai-studio%2Fcontext%2Fcontext&tabs=top-techniques" target="_blank">Messaggi di sistema per la sicurezza</a>
- <a href="https://blogs.microsoft.com/wp-content/uploads/prod/sites/5/2022/06/Microsoft-RAI-Impact-Assessment-Template.pdf?culture=en-us&country=us" target="_blank">Template per la valutazione del rischio</a>

## Lezione Precedente

[Agentic RAG](../05-agentic-rag/README.md)

## Lezione Successiva

[Pattern di Progettazione di Pianificazione](../07-planning-design/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:
Questo documento è stato tradotto utilizzando il servizio di traduzione automatica [Co-op Translator](https://github.com/Azure/co-op-translator). Pur impegnandoci per garantire accuratezza, si prega di considerare che le traduzioni automatizzate possono contenere errori o inesattezze. Il documento originale nella lingua nativa deve essere considerato la fonte autorevole. Per informazioni critiche, si raccomanda la traduzione professionale effettuata da un umano. Non ci assumiamo responsabilità per eventuali incomprensioni o interpretazioni errate derivanti dall’uso di questa traduzione.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->