[![Come progettare buoni agenti AI](../../../translated_images/it/lesson-4-thumbnail.546162853cb3daff.webp)](https://youtu.be/vieRiPRx-gI?si=cEZ8ApnT6Sus9rhn)

> _(Clicca sull'immagine sopra per vedere il video di questa lezione)_

# Pattern di Progettazione per l'Uso di Strumenti

Gli strumenti sono interessanti perché permettono agli agenti AI di avere un ampio ventaglio di capacità. Invece di avere un set limitato di azioni che un agente può eseguire, aggiungendo uno strumento, l’agente può ora compiere una vasta gamma di azioni. In questo capitolo, esamineremo il Pattern di Progettazione per l'Uso di Strumenti, che descrive come gli agenti AI possano usare specifici strumenti per raggiungere i propri obiettivi.

## Introduzione

In questa lezione, cercheremo di rispondere alle seguenti domande:

- Cos’è il pattern di progettazione per l’uso di strumenti?
- A quali casi d’uso può essere applicato?
- Quali sono gli elementi/blocchi costitutivi necessari per implementare il pattern di progettazione?
- Quali sono le considerazioni speciali per l’uso del Pattern di Progettazione per l’Uso di Strumenti per costruire agenti AI affidabili?

## Obiettivi di Apprendimento

Dopo aver completato questa lezione, sarai in grado di:

- Definire il Pattern di Progettazione per l’Uso di Strumenti e il suo scopo.
- Identificare i casi d’uso in cui è applicabile il Pattern di Progettazione per l’Uso di Strumenti.
- Comprendere gli elementi chiave necessari per implementare il pattern di progettazione.
- Riconoscere le considerazioni per garantire l’affidabilità degli agenti AI che usano questo pattern.

## Cos’è il Pattern di Progettazione per l’Uso di Strumenti?

Il **Pattern di Progettazione per l’Uso di Strumenti** si concentra sul fornire ai LLM la capacità di interagire con strumenti esterni per raggiungere obiettivi specifici. Gli strumenti sono codice eseguibile da un agente per compiere azioni. Uno strumento può essere una funzione semplice come una calcolatrice, oppure una chiamata API a un servizio di terze parti come la consultazione del prezzo di un’azione o la previsione meteo. Nel contesto degli agenti AI, gli strumenti sono progettati per essere eseguiti dagli agenti in risposta a **chiamate di funzione generate dal modello**.

## A quali casi d’uso può essere applicato?

Gli agenti AI possono sfruttare strumenti per completare compiti complessi, recuperare informazioni o prendere decisioni. Il pattern di progettazione per l’uso di strumenti viene spesso usato in scenari che richiedono un’interazione dinamica con sistemi esterni, come database, servizi web o interpreti di codice. Questa capacità è utile per diversi casi d’uso, tra cui:

- **Recupero dinamico di informazioni:** gli agenti possono interrogare API esterne o database per ottenere dati aggiornati (es., interrogare un database SQLite per analisi dati, recuperare prezzi azionari o informazioni meteo).
- **Esecuzione e interpretazione di codice:** gli agenti possono eseguire codice o script per risolvere problemi matematici, generare report o realizzare simulazioni.
- **Automazione dei flussi di lavoro:** automatizzare flussi di lavoro ripetitivi o multi-step integrando strumenti come scheduler di attività, servizi email o pipeline di dati.
- **Supporto clienti:** gli agenti possono interagire con sistemi CRM, piattaforme di ticketing o knowledge base per risolvere quesiti degli utenti.
- **Generazione e modifica di contenuti:** gli agenti possono utilizzare strumenti come correttori grammaticali, riassuntori di testo o valutatori della sicurezza dei contenuti per assistere nella creazione di contenuti.

## Quali sono gli elementi/blocchi costitutivi necessari per implementare il pattern di utilizzo degli strumenti?

Questi blocchi costitutivi permettono all’agente AI di svolgere una vasta gamma di compiti. Esaminiamo gli elementi chiave necessari per implementare il Pattern di Progettazione per l’Uso di Strumenti:

- **Schemi di Funzione/Strumento**: definizioni dettagliate degli strumenti disponibili, inclusi nome funzione, scopo, parametri richiesti e output attesi. Questi schemi consentono al LLM di comprendere quali strumenti sono disponibili e come costruire richieste valide.

- **Logica di Esecuzione di Funzioni**: regola come e quando gli strumenti vengono invocati in base all’intento dell’utente e al contesto della conversazione. Può includere moduli di pianificazione, meccanismi di instradamento o flussi condizionali che determinano dinamicamente l’uso dello strumento.

- **Sistema di Gestione dei Messaggi**: componenti che gestiscono il flusso conversazionale tra input utente, risposte LLM, chiamate agli strumenti e output degli strumenti.

- **Framework di Integrazione degli Strumenti**: infrastruttura che collega l’agente a vari strumenti, che siano funzioni semplici o servizi esterni complessi.

- **Gestione degli Errori & Validazione**: meccanismi per gestire i fallimenti nell’esecuzione degli strumenti, convalidare i parametri e gestire risposte inaspettate.

- **Gestione dello Stato**: traccia il contesto della conversazione, interazioni precedenti con gli strumenti e dati persistenti per garantire coerenza nelle interazioni multi-turno.

Successivamente, esaminiamo in dettaglio le Chiamate di Funzione/Strumento.

### Chiamata di Funzione/Strumento

La chiamata di funzione è il modo principale con cui permettiamo ai Modelli di Linguaggio di Grandi Dimensioni (LLM) di interagire con gli strumenti. Vedrai spesso "Funzione" e "Strumento" usati in modo intercambiabile perché le "funzioni" (blocchi di codice riutilizzabile) sono gli "strumenti" che gli agenti usano per svolgere compiti. Perché il codice di una funzione venga invocato, un LLM deve confrontare la richiesta dell’utente con la descrizione delle funzioni. Per fare ciò, uno schema contenente le descrizioni di tutte le funzioni disponibili viene inviato all’LLM. L’LLM quindi seleziona la funzione più adatta al compito e restituisce il suo nome e i relativi argomenti. La funzione selezionata viene invocata, la sua risposta viene inviata nuovamente all’LLM, che usa queste informazioni per rispondere alla richiesta dell’utente.

Per gli sviluppatori che vogliono implementare la chiamata di funzione per agenti, occorre:

1. Un modello LLM che supporti la chiamata di funzione
2. Uno schema contenente le descrizioni delle funzioni
3. Il codice per ogni funzione descritta

Usiamo l’esempio di ottenere l’ora corrente in una città per illustrare:

1. **Inizializzare un LLM che supporti la chiamata di funzione:**

    Non tutti i modelli supportano la chiamata di funzione, quindi è importante verificare che l’LLM utilizzato la supporti. <a href="https://learn.microsoft.com/azure/ai-services/openai/how-to/function-calling" target="_blank">Azure OpenAI</a> supporta la chiamata di funzione. Possiamo iniziare istanziando il client Azure OpenAI.

    ```python
    # Inizializza il client Azure OpenAI
    client = AzureOpenAI(
        azure_endpoint = os.getenv("AZURE_OPENAI_ENDPOINT"), 
        api_key=os.getenv("AZURE_OPENAI_API_KEY"),  
        api_version="2024-05-01-preview"
    )
    ```

2. **Creare uno Schema di Funzione**:

    Successivamente definiamo uno schema JSON contenente il nome della funzione, la descrizione di cosa fa la funzione e i nomi e descrizioni dei parametri della funzione.
    Passiamo poi questo schema al client creato in precedenza, insieme alla richiesta dell’utente di trovare l’ora a San Francisco. È importante notare che ciò che viene restituito è una **chiamata a strumento**, **non** la risposta finale alla domanda. Come detto prima, l’LLM restituisce il nome della funzione selezionata per il compito e gli argomenti che le verranno passati.

    ```python
    # Descrizione della funzione per il modello da leggere
    tools = [
        {
            "type": "function",
            "function": {
                "name": "get_current_time",
                "description": "Get the current time in a given location",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "location": {
                            "type": "string",
                            "description": "The city name, e.g. San Francisco",
                        },
                    },
                    "required": ["location"],
                },
            }
        }
    ]
    ```
   
    ```python
  
    # Messaggio iniziale dell'utente
    messages = [{"role": "user", "content": "What's the current time in San Francisco"}] 
  
    # Prima chiamata API: Chiedi al modello di usare la funzione
      response = client.chat.completions.create(
          model=deployment_name,
          messages=messages,
          tools=tools,
          tool_choice="auto",
      )
  
      # Elabora la risposta del modello
      response_message = response.choices[0].message
      messages.append(response_message)
  
      print("Model's response:")  

      print(response_message)
  
    ```

    ```bash
    Model's response:
    ChatCompletionMessage(content=None, role='assistant', function_call=None, tool_calls=[ChatCompletionMessageToolCall(id='call_pOsKdUlqvdyttYB67MOj434b', function=Function(arguments='{"location":"San Francisco"}', name='get_current_time'), type='function')])
    ```
  
3. **Il codice della funzione necessario per svolgere il compito:**

    Ora che l’LLM ha scelto quale funzione deve essere eseguita, il codice che realizza il compito deve essere implementato ed eseguito.
    Possiamo implementare il codice per ottenere l’ora corrente in Python. Dovremo anche scrivere il codice per estrarre il nome e gli argomenti dalla response_message per ottenere il risultato finale.

    ```python
      def get_current_time(location):
        """Get the current time for a given location"""
        print(f"get_current_time called with location: {location}")  
        location_lower = location.lower()
        
        for key, timezone in TIMEZONE_DATA.items():
            if key in location_lower:
                print(f"Timezone found for {key}")  
                current_time = datetime.now(ZoneInfo(timezone)).strftime("%I:%M %p")
                return json.dumps({
                    "location": location,
                    "current_time": current_time
                })
      
        print(f"No timezone data found for {location_lower}")  
        return json.dumps({"location": location, "current_time": "unknown"})
    ```

     ```python
     # Gestire le chiamate di funzione
      if response_message.tool_calls:
          for tool_call in response_message.tool_calls:
              if tool_call.function.name == "get_current_time":
     
                  function_args = json.loads(tool_call.function.arguments)
     
                  time_response = get_current_time(
                      location=function_args.get("location")
                  )
     
                  messages.append({
                      "tool_call_id": tool_call.id,
                      "role": "tool",
                      "name": "get_current_time",
                      "content": time_response,
                  })
      else:
          print("No tool calls were made by the model.")  
  
      # Seconda chiamata API: Ottenere la risposta finale dal modello
      final_response = client.chat.completions.create(
          model=deployment_name,
          messages=messages,
      )
  
      return final_response.choices[0].message.content
     ```

     ```bash
      get_current_time called with location: San Francisco
      Timezone found for san francisco
      The current time in San Francisco is 09:24 AM.
     ```

La Chiamata di Funzione è al centro della maggior parte, se non di tutti, i design di utilizzo di strumenti per agenti, tuttavia implementarla da zero può essere a volte una sfida.
Come abbiamo visto in [Lezione 2](../../../02-explore-agentic-frameworks) i framework agentici ci forniscono blocchi predefiniti per implementare l’uso di strumenti.
 
## Esempi di Uso di Strumenti con Framework Agentici

Ecco alcuni esempi di come puoi implementare il Pattern di Progettazione per l’Uso di Strumenti usando diversi framework agentici:

### Semantic Kernel

<a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Semantic Kernel</a> è un framework AI open-source per sviluppatori .NET, Python e Java che lavorano con Modelli di Linguaggio di Grandi Dimensioni (LLM). Semplifica il processo di uso della chiamata di funzione descrivendo automaticamente le tue funzioni e i loro parametri al modello tramite un processo chiamato <a href="https://learn.microsoft.com/semantic-kernel/concepts/ai-services/chat-completion/function-calling/?pivots=programming-language-python#1-serializing-the-functions" target="_blank">serializzazione</a>. Gestisce anche la comunicazione avanti e indietro tra modello e codice. Un altro vantaggio nell’usare un framework agentico come Semantic Kernel è che ti consente di accedere a strumenti precompilati come <a href="https://github.com/microsoft/semantic-kernel/blob/main/python/samples/getting_started_with_agents/openai_assistant/step4_assistant_tool_file_search.py" target="_blank">File Search</a> e <a href="https://github.com/microsoft/semantic-kernel/blob/main/python/samples/getting_started_with_agents/openai_assistant/step3_assistant_tool_code_interpreter.py" target="_blank">Code Interpreter</a>.

Il diagramma seguente illustra il processo di chiamata di funzione con Semantic Kernel:

![function calling](../../../translated_images/it/functioncalling-diagram.a84006fc287f6014.webp)

In Semantic Kernel le funzioni/strumenti sono chiamati <a href="https://learn.microsoft.com/semantic-kernel/concepts/plugins/?pivots=programming-language-python" target="_blank">Plugin</a>. Possiamo convertire la funzione `get_current_time` vista prima in un plugin trasformandola in una classe che la contiene. Possiamo anche importare il decoratore `kernel_function`, che prende in ingresso la descrizione della funzione. Quando crei un kernel con GetCurrentTimePlugin, il kernel serializzerà automaticamente la funzione e i suoi parametri, creando lo schema da inviare all’LLM nel processo.

```python
from semantic_kernel.functions import kernel_function

class GetCurrentTimePlugin:
    async def __init__(self, location):
        self.location = location

    @kernel_function(
        description="Get the current time for a given location"
    )
    def get_current_time(location: str = ""):
        ...

```

```python 
from semantic_kernel import Kernel

# Crea il kernel
kernel = Kernel()

# Crea il plugin
get_current_time_plugin = GetCurrentTimePlugin(location)

# Aggiungi il plugin al kernel
kernel.add_plugin(get_current_time_plugin)
```
  
### Azure AI Agent Service

<a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Azure AI Agent Service</a> è un framework agentico più recente progettato per permettere agli sviluppatori di costruire, distribuire e scalare agenti AI di alta qualità, estensibili e sicuri senza dover gestire le risorse di calcolo e storage sottostanti. È particolarmente utile per applicazioni aziendali, in quanto è un servizio completamente gestito con sicurezza da livello enterprise.

Rispetto allo sviluppo diretto con l’API LLM, Azure AI Agent Service offre alcuni vantaggi, tra cui:

- Chiamata automatica degli strumenti – non è necessario analizzare una chiamata a strumento, invocare lo strumento e gestire la risposta; tutto ciò viene ora gestito lato server
- Dati gestiti in modo sicuro – invece di gestire lo stato della conversazione in proprio, puoi affidarti ai threads per memorizzare tutte le informazioni necessarie
- Strumenti pronti all’uso – strumenti che puoi usare per interagire con le tue sorgenti dati, come Bing, Azure AI Search e Azure Functions.

Gli strumenti disponibili in Azure AI Agent Service possono essere divisi in due categorie:

1. Strumenti di Conoscenza:
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/bing-grounding?tabs=python&pivots=overview" target="_blank">Grounding con Bing Search</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/file-search?tabs=python&pivots=overview" target="_blank">File Search</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-ai-search?tabs=azurecli%2Cpython&pivots=overview-azure-ai-search" target="_blank">Azure AI Search</a>

2. Strumenti di Azione:
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/function-calling?tabs=python&pivots=overview" target="_blank">Function Calling</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/code-interpreter?tabs=python&pivots=overview" target="_blank">Code Interpreter</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/openapi-spec?tabs=python&pivots=overview" target="_blank">Strumenti definiti da OpenAPI</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-functions?pivots=overview" target="_blank">Azure Functions</a>

Il servizio Agent ci permette di usare questi strumenti insieme come un `toolset`. Utilizza anche i `threads` che tengono traccia della cronologia dei messaggi di una particolare conversazione.

Immagina di essere un agente di vendita in un’azienda chiamata Contoso. Vuoi sviluppare un agente conversazionale che possa rispondere a domande sui tuoi dati di vendita.

L’immagine seguente illustra come potresti usare Azure AI Agent Service per analizzare i tuoi dati di vendita:

![Agentic Service In Action](../../../translated_images/it/agent-service-in-action.34fb465c9a84659e.webp)

Per usare uno qualsiasi di questi strumenti con il servizio, possiamo creare un client e definire uno strumento o un set di strumenti. Per implementarlo praticamente possiamo usare il seguente codice Python. L’LLM potrà esaminare il toolset e decidere se usare la funzione creata dall’utente, `fetch_sales_data_using_sqlite_query`, o l’interprete di codice predefinito a seconda della richiesta dell’utente.

```python 
import os
from azure.ai.projects import AIProjectClient
from azure.identity import DefaultAzureCredential
from fetch_sales_data_functions import fetch_sales_data_using_sqlite_query # funzione fetch_sales_data_using_sqlite_query che si può trovare in un file fetch_sales_data_functions.py.
from azure.ai.projects.models import ToolSet, FunctionTool, CodeInterpreterTool

project_client = AIProjectClient.from_connection_string(
    credential=DefaultAzureCredential(),
    conn_str=os.environ["PROJECT_CONNECTION_STRING"],
)

# Inizializzare il set di strumenti
toolset = ToolSet()

# Inizializzare un agente di chiamata di funzione con la funzione fetch_sales_data_using_sqlite_query e aggiungerlo al set di strumenti
fetch_data_function = FunctionTool(fetch_sales_data_using_sqlite_query)
toolset.add(fetch_data_function)

# Inizializzare lo strumento Code Interpreter e aggiungerlo al set di strumenti.
code_interpreter = code_interpreter = CodeInterpreterTool()
toolset.add(code_interpreter)

agent = project_client.agents.create_agent(
    model="gpt-4o-mini", name="my-agent", instructions="You are helpful agent", 
    toolset=toolset
)
```

## Quali sono le considerazioni speciali per usare il Pattern di Progettazione per l’Uso di Strumenti per costruire agenti AI affidabili?

Una preoccupazione comune con l’SQL generato dinamicamente dagli LLM è la sicurezza, in particolare il rischio di SQL injection o azioni malevole, come il drop o la manomissione del database. Sebbene queste preoccupazioni siano valide, possono essere efficacemente mitigate configurando correttamente i permessi di accesso al database. Per la maggior parte dei database questo comporta la configurazione in sola lettura. Per servizi database come PostgreSQL o Azure SQL, l’applicazione dovrebbe essere assegnata a un ruolo di sola lettura (SELECT).
Eseguire l'app in un ambiente sicuro aumenta ulteriormente la protezione. Negli scenari aziendali, i dati vengono solitamente estratti e trasformati dai sistemi operativi in un database o data warehouse a sola lettura con uno schema intuitivo. Questo approccio garantisce che i dati siano sicuri, ottimizzati per prestazioni e accessibilità, e che l'app abbia un accesso ristretto e di sola lettura.

## Sample Codes

- Python: [Agent Framework](./code_samples/04-python-agent-framework.ipynb)
- .NET: [Agent Framework](./code_samples/04-dotnet-agent-framework.md)

## Hai altre domande sull'uso dei design pattern dello strumento?

Unisciti a [Azure AI Foundry Discord](https://aka.ms/ai-agents/discord) per incontrare altri studenti, partecipare agli office hours e ottenere risposte alle tue domande sugli AI Agents.

## Risorse aggiuntive

- <a href="https://microsoft.github.io/build-your-first-agent-with-azure-ai-agent-service-workshop/" target="_blank">Workshop sul servizio Azure AI Agents</a>
- <a href="https://github.com/Azure-Samples/contoso-creative-writer/tree/main/docs/workshop" target="_blank">Workshop Multi-Agente Contoso Creative Writer</a>
- <a href="https://learn.microsoft.com/semantic-kernel/concepts/ai-services/chat-completion/function-calling/?pivots=programming-language-python#1-serializing-the-functions" target="_blank">Tutorial Semantic Kernel Function Calling</a>
- <a href="https://github.com/microsoft/semantic-kernel/blob/main/python/samples/getting_started_with_agents/openai_assistant/step3_assistant_tool_code_interpreter.py" target="_blank">Semantic Kernel Code Interpreter</a>
- <a href="https://microsoft.github.io/autogen/dev/user-guide/core-user-guide/components/tools.html" target="_blank">Autogen Tools</a>

## Lezione precedente

[Understanding Agentic Design Patterns](../03-agentic-design-patterns/README.md)

## Lezione successiva

[Agentic RAG](../05-agentic-rag/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Avvertenza**:
Questo documento è stato tradotto utilizzando il servizio di traduzione automatica [Co-op Translator](https://github.com/Azure/co-op-translator). Pur cercando di garantire la massima accuratezza, si prega di notare che le traduzioni automatiche possono contenere errori o inesattezze. Il documento originale nella sua lingua originale deve essere considerato la fonte autorevole. Per informazioni critiche, si raccomanda una traduzione professionale effettuata da un esperto umano. Non siamo responsabili per eventuali incomprensioni o interpretazioni errate derivanti dall'uso di questa traduzione.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->