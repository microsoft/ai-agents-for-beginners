[![Agenti AI Affidabili](../../../translated_images/it/lesson-6-thumbnail.a58ab36c099038d4.webp)](https://youtu.be/iZKkMEGBCUQ?si=Q-kEbcyHUMPoHp8L)

> _(Clicca sull'immagine sopra per vedere il video di questa lezione)_

# Costruire Agenti AI Affidabili

## Introduzione

Questa lezione tratterà:

- Come costruire e distribuire Agenti AI sicuri ed efficaci
- Considerazioni importanti sulla sicurezza nello sviluppo di Agenti AI.
- Come mantenere la privacy dei dati e degli utenti nello sviluppo di Agenti AI.

## Obiettivi di Apprendimento

Al termine di questa lezione, saprai come:

- Identificare e mitigare i rischi durante la creazione di Agenti AI.
- Implementare misure di sicurezza per garantire che i dati e gli accessi siano gestiti correttamente.
- Creare Agenti AI che mantengono la privacy dei dati e offrono una qualità di esperienza utente.

## Sicurezza

Analizziamo prima come costruire applicazioni agentiche sicure. Sicurezza significa che l'agente AI si comporta come progettato. Come costruttori di applicazioni agentiche, disponiamo di metodi e strumenti per massimizzare la sicurezza:

### Costruire un Framework per Messaggi di Sistema

Se hai mai costruito un'app AI usando Large Language Models (LLM), conosci l'importanza di progettare un prompt di sistema o messaggio di sistema robusto. Questi prompt stabiliscono le regole meta, le istruzioni e le linee guida su come l'LLM interagirà con l'utente e con i dati.

Per gli Agenti AI, il prompt di sistema è ancora più importante poiché gli Agenti AI avranno bisogno di istruzioni altamente specifiche per completare i compiti che abbiamo progettato per loro.

Per creare prompt di sistema scalabili, possiamo usare un framework di messaggi di sistema per costruire uno o più agenti nella nostra applicazione:

![Costruire un Framework per Messaggi di Sistema](../../../translated_images/it/system-message-framework.3a97368c92d11d68.webp)

#### Passo 1: Creare un Meta Messaggio di Sistema

Il meta prompt sarà usato da un LLM per generare i prompt di sistema per gli agenti che creiamo. Lo progettiamo come un modello così da poter creare efficientemente più agenti se necessario.

Ecco un esempio di meta messaggio di sistema che potremmo dare all'LLM:

```plaintext
You are an expert at creating AI agent assistants. 
You will be provided a company name, role, responsibilities and other
information that you will use to provide a system prompt for.
To create the system prompt, be descriptive as possible and provide a structure that a system using an LLM can better understand the role and responsibilities of the AI assistant. 
```

#### Passo 2: Creare un prompt di base

Il passo successivo è creare un prompt di base per descrivere l'Agente AI. Dovresti includere il ruolo dell'agente, i compiti che l'agente completerà e qualsiasi altra responsabilità dell'agente.

Ecco un esempio:

```plaintext
You are a travel agent for Contoso Travel that is great at booking flights for customers. To help customers you can perform the following tasks: lookup available flights, book flights, ask for preferences in seating and times for flights, cancel any previously booked flights and alert customers on any delays or cancellations of flights.  
```

#### Passo 3: Fornire il Messaggio di Sistema di Base all'LLM

Ora possiamo ottimizzare questo messaggio di sistema fornendo il meta messaggio di sistema come messaggio di sistema e il nostro messaggio di sistema di base.

Questo produrrà un messaggio di sistema meglio progettato per guidare i nostri agenti AI:

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

Il valore di questo framework di messaggi di sistema è poter scalare la creazione di messaggi di sistema da più agenti più facilmente così come migliorare i tuoi messaggi di sistema nel tempo. È raro avere un messaggio di sistema che funzioni alla prima prova per il tuo caso d'uso completo. Essere in grado di fare piccoli aggiustamenti e miglioramenti modificando il messaggio di sistema di base ed eseguendolo attraverso il sistema ti permetterà di confrontare e valutare i risultati.

## Comprendere le Minacce

Per costruire agenti AI affidabili, è importante capire e mitigare i rischi e le minacce per il tuo agente AI. Esaminiamo solo alcune delle diverse minacce agli agenti AI e come puoi pianificare e prepararti meglio per queste.

![Comprendere le Minacce](../../../translated_images/it/understanding-threats.89edeada8a97fc0f.webp)

### Compito e Istruzione

**Descrizione:** Gli attaccanti tentano di modificare le istruzioni o gli obiettivi dell'agente AI tramite prompting o manipolazione degli input.

**Mitigazione:** Eseguire controlli di validazione e filtri sugli input per rilevare prompt potenzialmente pericolosi prima che vengano processati dall'Agente AI. Poiché questi attacchi richiedono tipicamente un'interazione frequente con l'Agente, limitare il numero di turni in una conversazione è un altro modo per prevenire questo tipo di attacchi.

### Accesso a Sistemi Critici

**Descrizione:** Se un agente AI ha accesso a sistemi e servizi che conservano dati sensibili, gli attaccanti possono compromettere la comunicazione tra l'agente e questi servizi. Questi possono essere attacchi diretti o tentativi indiretti di ottenere informazioni su questi sistemi tramite l'agente.

**Mitigazione:** Gli agenti AI dovrebbero avere accesso ai sistemi solo quando necessario per prevenire questo tipo di attacchi. La comunicazione tra agente e sistema dovrebbe inoltre essere sicura. Implementare autenticazione e controllo degli accessi è un altro modo per proteggere queste informazioni.

### Sovraccarico di Risorse e Servizi

**Descrizione:** Gli agenti AI possono accedere a diversi strumenti e servizi per completare i compiti. Gli attaccanti possono sfruttare questa capacità per attaccare questi servizi inviando un alto volume di richieste tramite l'Agente AI, causando potenziali malfunzionamenti o costi elevati.

**Mitigazione:** Implementare politiche per limitare il numero di richieste che un agente AI può fare a un servizio. Limitare il numero di turni di conversazione e richieste al tuo agente AI è un altro modo per prevenire questo tipo di attacchi.

### Avvelenamento della Base di Conoscenza

**Descrizione:** Questo tipo di attacco non prende di mira direttamente l'agente AI ma la base di conoscenza e altri servizi che l'agente AI utilizzerà. Ciò potrebbe comportare la corruzione dei dati o delle informazioni che l'agente AI utilizzerà per completare un compito, portando a risposte distorte o non intenzionate all'utente.

**Mitigazione:** Effettuare verifiche regolari dei dati che l'agente AI utilizzerà nei suoi workflow. Assicurarsi che l'accesso a questi dati sia sicuro e che siano modificati solo da persone di fiducia per evitare questo tipo di attacco.

### Errori a Cascata

**Descrizione:** Gli agenti AI accedono a vari strumenti e servizi per completare i compiti. Errori causati da attaccanti possono portare a malfunzionamenti di altri sistemi a cui l'agente AI è collegato, facendo sì che l'attacco si estenda e diventi più difficile da risolvere.

**Mitigazione:** Un metodo per evitare questo è far operare l'Agente AI in un ambiente limitato, come l'esecuzione di compiti in un container Docker, per prevenire attacchi diretti al sistema. Creare meccanismi di fallback e logiche di retry quando certi sistemi rispondono con errore è un altro modo per prevenire fallimenti di sistema più ampi.

## Human-in-the-Loop (Uomo nel Circuito)

Un altro modo efficace per costruire sistemi di Agenti AI affidabili è utilizzare un paradigma Human-in-the-loop. Questo crea un flusso in cui gli utenti sono in grado di fornire feedback agli Agenti durante l'esecuzione. Gli utenti agiscono essenzialmente come agenti in un sistema multi-agente e possono fornire approvazione o terminare il processo in esecuzione.

![Human in The Loop](../../../translated_images/it/human-in-the-loop.5f0068a678f62f4f.webp)

Ecco un snippet di codice che utilizza il Microsoft Agent Framework per mostrare come questo concetto viene implementato:

```python
import os
from agent_framework.foundry import FoundryChatClient
from azure.identity import AzureCliCredential

# Crea il provider con approvazione con intervento umano
provider = FoundryChatClient(
    project_endpoint=os.environ["AZURE_AI_PROJECT_ENDPOINT"],
    model=os.environ["AZURE_AI_MODEL_DEPLOYMENT_NAME"],
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

Costruire agenti AI affidabili richiede un'attenta progettazione, misure di sicurezza robuste e iterazione continua. Implementando sistemi strutturati di meta prompting, comprendendo le potenziali minacce e applicando strategie di mitigazione, gli sviluppatori possono creare agenti AI sicuri ed efficaci. Inoltre, incorporare un approccio human-in-the-loop assicura che gli agenti AI rimangano allineati alle esigenze degli utenti minimizzando i rischi. Man mano che l'AI continua a evolvere, mantenere una posizione proattiva su sicurezza, privacy e considerazioni etiche sarà fondamentale per favorire fiducia e affidabilità nei sistemi guidati dall'AI.

## Esempi di Codice

- [`code_samples/06-system-message-framework.ipynb`](code_samples/06-system-message-framework.ipynb): Dimostrazione passo-passo del framework di messaggi di sistema meta-prompt.
- [`code_samples/06-human-in-the-loop.ipynb`](code_samples/06-human-in-the-loop.ipynb): Gate di approvazione pre-azione, stratificazione del rischio e audit log per agenti affidabili.

### Hai altre domande su come costruire agenti AI affidabili?

Unisciti al [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D) per incontrare altri studenti, partecipare ad ore d’ufficio e ottenere risposte alle tue domande sugli Agenti AI.

## Risorse Aggiuntive

- <a href="https://learn.microsoft.com/azure/ai-studio/responsible-use-of-ai-overview" target="_blank">Panoramica sull’AI responsabile</a>
- <a href="https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai" target="_blank">Valutazione dei modelli AI generativi e applicazioni AI</a>
- <a href="https://learn.microsoft.com/azure/ai-services/openai/concepts/system-message?context=%2Fazure%2Fai-studio%2Fcontext%2Fcontext&tabs=top-techniques" target="_blank">Messaggi di sistema per la sicurezza</a>
- <a href="https://blogs.microsoft.com/wp-content/uploads/prod/sites/5/2022/06/Microsoft-RAI-Impact-Assessment-Template.pdf?culture=en-us&country=us" target="_blank">Template di Valutazione del Rischio</a>

## Lezione Precedente

[Agentic RAG](../05-agentic-rag/README.md)

## Lezione Successiva

[Planning Design Pattern](../07-planning-design/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:
Questo documento è stato tradotto utilizzando il servizio di traduzione AI [Co-op Translator](https://github.com/Azure/co-op-translator). Sebbene ci impegniamo per garantire la precisione, si prega di notare che le traduzioni automatizzate possono contenere errori o imprecisioni. Il documento originale nella sua lingua nativa deve essere considerato la fonte autorevole. Per informazioni critiche, si raccomanda una traduzione professionale effettuata da un essere umano. Non siamo responsabili per eventuali malintesi o interpretazioni errate derivanti dall’uso di questa traduzione.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->