<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "498802b4c3c3cc486b86f27a12cebb34",
  "translation_date": "2025-08-29T12:59:22+00:00",
  "source_file": "06-building-trustworthy-agents/README.md",
  "language_code": "it"
}
-->
[![Agenti AI Affidabili](../../../translated_images/lesson-6-thumbnail.a58ab36c099038d4f786c2b0d5d6e89f41f4c2ecc05ab10b67bced2695eeb218.it.png)](https://youtu.be/iZKkMEGBCUQ?si=Q-kEbcyHUMPoHp8L)

> _(Clicca sull'immagine sopra per guardare il video di questa lezione)_

# Creare Agenti AI Affidabili

## Introduzione

Questa lezione tratterà:

- Come costruire e distribuire Agenti AI sicuri ed efficaci.
- Considerazioni importanti sulla sicurezza nello sviluppo di Agenti AI.
- Come mantenere la privacy dei dati e degli utenti durante lo sviluppo di Agenti AI.

## Obiettivi di Apprendimento

Dopo aver completato questa lezione, saprai come:

- Identificare e mitigare i rischi nella creazione di Agenti AI.
- Implementare misure di sicurezza per garantire una corretta gestione dei dati e degli accessi.
- Creare Agenti AI che rispettino la privacy dei dati e offrano un'esperienza utente di qualità.

## Sicurezza

Iniziamo esaminando come costruire applicazioni agentiche sicure. La sicurezza significa che l'agente AI si comporta come previsto. Come sviluppatori di applicazioni agentiche, abbiamo metodi e strumenti per massimizzare la sicurezza:

### Creare un Framework per i Messaggi di Sistema

Se hai mai sviluppato un'applicazione AI utilizzando Large Language Models (LLMs), conosci l'importanza di progettare un prompt di sistema robusto o un messaggio di sistema. Questi prompt stabiliscono le regole, le istruzioni e le linee guida per come l'LLM interagirà con l'utente e i dati.

Per gli Agenti AI, il messaggio di sistema è ancora più importante, poiché gli Agenti AI necessitano di istruzioni altamente specifiche per completare i compiti per cui sono stati progettati.

Per creare prompt di sistema scalabili, possiamo utilizzare un framework per i messaggi di sistema per costruire uno o più agenti nella nostra applicazione:

![Creare un Framework per i Messaggi di Sistema](../../../translated_images/system-message-framework.3a97368c92d11d6814577b03cd128ec8c71a5fd1e26f341835cfa5df59ae87ae.it.png)

#### Passo 1: Creare un Meta Messaggio di Sistema

Il meta prompt sarà utilizzato da un LLM per generare i messaggi di sistema per gli agenti che creiamo. Lo progettiamo come un modello per poter creare più agenti in modo efficiente, se necessario.

Ecco un esempio di meta messaggio di sistema che potremmo fornire all'LLM:

```plaintext
You are an expert at creating AI agent assistants. 
You will be provided a company name, role, responsibilities and other
information that you will use to provide a system prompt for.
To create the system prompt, be descriptive as possible and provide a structure that a system using an LLM can better understand the role and responsibilities of the AI assistant. 
```

#### Passo 2: Creare un Prompt di Base

Il passo successivo è creare un prompt di base per descrivere l'Agente AI. Dovresti includere il ruolo dell'agente, i compiti che l'agente svolgerà e qualsiasi altra responsabilità dell'agente.

Ecco un esempio:

```plaintext
You are a travel agent for Contoso Travel that is great at booking flights for customers. To help customers you can perform the following tasks: lookup available flights, book flights, ask for preferences in seating and times for flights, cancel any previously booked flights and alert customers on any delays or cancellations of flights.  
```

#### Passo 3: Fornire il Messaggio di Sistema di Base all'LLM

Ora possiamo ottimizzare questo messaggio di sistema fornendo il meta messaggio di sistema come messaggio di sistema e il nostro messaggio di sistema di base.

Questo produrrà un messaggio di sistema meglio progettato per guidare i nostri Agenti AI:

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

Il valore di questo framework per i messaggi di sistema è la possibilità di scalare la creazione di messaggi di sistema per più agenti e migliorare i messaggi di sistema nel tempo. È raro che un messaggio di sistema funzioni perfettamente al primo tentativo per il tuo caso d'uso completo. Essere in grado di apportare piccole modifiche e miglioramenti cambiando il messaggio di sistema di base e facendolo passare attraverso il sistema ti permetterà di confrontare e valutare i risultati.

## Comprendere le Minacce

Per costruire agenti AI affidabili, è importante comprendere e mitigare i rischi e le minacce per il tuo agente AI. Esaminiamo alcune delle diverse minacce agli agenti AI e come puoi pianificare e prepararti meglio per affrontarle.

![Comprendere le Minacce](../../../translated_images/understanding-threats.89edeada8a97fc0f7053558567d5dd27c0c333b74e47fffdde490fa6777a4c17.it.png)

### Compiti e Istruzioni

**Descrizione:** Gli attaccanti tentano di modificare le istruzioni o gli obiettivi dell'agente AI attraverso prompt o manipolazione degli input.

**Mitigazione**: Esegui controlli di validazione e filtri sugli input per rilevare prompt potenzialmente pericolosi prima che vengano elaborati dall'Agente AI. Poiché questi attacchi richiedono tipicamente interazioni frequenti con l'Agente, limitare il numero di turni in una conversazione è un altro modo per prevenire questi tipi di attacchi.

### Accesso a Sistemi Critici

**Descrizione**: Se un agente AI ha accesso a sistemi e servizi che memorizzano dati sensibili, gli attaccanti possono compromettere la comunicazione tra l'agente e questi servizi. Questi possono essere attacchi diretti o tentativi indiretti di ottenere informazioni su questi sistemi tramite l'agente.

**Mitigazione**: Gli agenti AI dovrebbero avere accesso ai sistemi solo quando necessario per prevenire questi tipi di attacchi. La comunicazione tra l'agente e il sistema dovrebbe essere sicura. Implementare autenticazione e controllo degli accessi è un altro modo per proteggere queste informazioni.

### Sovraccarico di Risorse e Servizi

**Descrizione:** Gli agenti AI possono accedere a diversi strumenti e servizi per completare i compiti. Gli attaccanti possono sfruttare questa capacità per attaccare questi servizi inviando un alto volume di richieste tramite l'Agente AI, causando guasti ai sistemi o costi elevati.

**Mitigazione:** Implementa politiche per limitare il numero di richieste che un agente AI può fare a un servizio. Limitare il numero di turni di conversazione e richieste al tuo agente AI è un altro modo per prevenire questi tipi di attacchi.

### Avvelenamento della Base di Conoscenza

**Descrizione:** Questo tipo di attacco non prende di mira direttamente l'agente AI, ma la base di conoscenza e altri servizi che l'agente AI utilizzerà. Questo potrebbe comportare la corruzione dei dati o delle informazioni che l'agente AI utilizzerà per completare un compito, portando a risposte distorte o non intenzionali per l'utente.

**Mitigazione:** Esegui verifiche regolari sui dati che l'agente AI utilizzerà nei suoi flussi di lavoro. Assicurati che l'accesso a questi dati sia sicuro e che possano essere modificati solo da persone fidate per evitare questo tipo di attacco.

### Errori a Cascata

**Descrizione:** Gli agenti AI accedono a vari strumenti e servizi per completare i compiti. Gli errori causati dagli attaccanti possono portare a guasti di altri sistemi a cui l'agente AI è connesso, rendendo l'attacco più diffuso e difficile da risolvere.

**Mitigazione**: Un metodo per evitare ciò è far operare l'Agente AI in un ambiente limitato, come eseguire i compiti in un container Docker, per prevenire attacchi diretti ai sistemi. Creare meccanismi di fallback e logiche di ripetizione quando certi sistemi rispondono con un errore è un altro modo per prevenire guasti più ampi.

## Human-in-the-Loop

Un altro modo efficace per costruire sistemi di Agenti AI affidabili è utilizzare un approccio Human-in-the-Loop. Questo crea un flusso in cui gli utenti possono fornire feedback agli Agenti durante l'esecuzione. Gli utenti agiscono essenzialmente come agenti in un sistema multi-agente, fornendo approvazione o terminazione del processo in corso.

![Human in The Loop](../../../translated_images/human-in-the-loop.5f0068a678f62f4fc8373d5b78c4c22f35d9e4da35c93f66c3b634c1774eff34.it.png)

Ecco un esempio di codice che utilizza AutoGen per mostrare come viene implementato questo concetto:

```python

# Create the agents.
model_client = OpenAIChatCompletionClient(model="gpt-4o-mini")
assistant = AssistantAgent("assistant", model_client=model_client)
user_proxy = UserProxyAgent("user_proxy", input_func=input)  # Use input() to get user input from console.

# Create the termination condition which will end the conversation when the user says "APPROVE".
termination = TextMentionTermination("APPROVE")

# Create the team.
team = RoundRobinGroupChat([assistant, user_proxy], termination_condition=termination)

# Run the conversation and stream to the console.
stream = team.run_stream(task="Write a 4-line poem about the ocean.")
# Use asyncio.run(...) when running in a script.
await Console(stream)

```

## Conclusione

Costruire agenti AI affidabili richiede una progettazione attenta, misure di sicurezza robuste e iterazione continua. Implementando sistemi strutturati di meta prompting, comprendendo le potenziali minacce e applicando strategie di mitigazione, gli sviluppatori possono creare agenti AI sicuri ed efficaci. Inoltre, incorporare un approccio Human-in-the-Loop garantisce che gli agenti AI rimangano allineati alle esigenze degli utenti, riducendo al minimo i rischi. Man mano che l'AI continua a evolversi, mantenere un atteggiamento proattivo su sicurezza, privacy e considerazioni etiche sarà fondamentale per promuovere fiducia e affidabilità nei sistemi basati sull'AI.

### Hai altre domande sulla creazione di Agenti AI Affidabili?

Unisciti al [Discord di Azure AI Foundry](https://aka.ms/ai-agents/discord) per incontrare altri studenti, partecipare a sessioni di supporto e ottenere risposte alle tue domande sugli Agenti AI.

## Risorse Aggiuntive

- <a href="https://learn.microsoft.com/azure/ai-studio/responsible-use-of-ai-overview" target="_blank">Panoramica sull'uso responsabile dell'AI</a>
- <a href="https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai" target="_blank">Valutazione dei modelli generativi di AI e delle applicazioni AI</a>
- <a href="https://learn.microsoft.com/azure/ai-services/openai/concepts/system-message?context=%2Fazure%2Fai-studio%2Fcontext%2Fcontext&tabs=top-techniques" target="_blank">Messaggi di sistema per la sicurezza</a>
- <a href="https://blogs.microsoft.com/wp-content/uploads/prod/sites/5/2022/06/Microsoft-RAI-Impact-Assessment-Template.pdf?culture=en-us&country=us" target="_blank">Modello di valutazione del rischio</a>

## Lezione Precedente

[Agentic RAG](../05-agentic-rag/README.md)

## Prossima Lezione

[Planning Design Pattern](../07-planning-design/README.md)

---

**Disclaimer**:  
Questo documento è stato tradotto utilizzando il servizio di traduzione automatica [Co-op Translator](https://github.com/Azure/co-op-translator). Sebbene ci impegniamo per garantire l'accuratezza, si prega di notare che le traduzioni automatiche possono contenere errori o imprecisioni. Il documento originale nella sua lingua nativa dovrebbe essere considerato la fonte autorevole. Per informazioni critiche, si raccomanda una traduzione professionale effettuata da un traduttore umano. Non siamo responsabili per eventuali incomprensioni o interpretazioni errate derivanti dall'uso di questa traduzione.