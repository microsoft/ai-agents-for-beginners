[![Come progettare buoni agenti AI](../../../translated_images/it/lesson-4-thumbnail.546162853cb3daff.webp)](https://youtu.be/vieRiPRx-gI?si=cEZ8ApnT6Sus9rhn)

> _(Fare clic sull'immagine sopra per guardare il video di questa lezione)_

# Pattern di progettazione per l'uso degli strumenti

Gli strumenti sono interessanti perché permettono agli agenti AI di avere una gamma più ampia di capacità. Invece che l'agente abbia un set limitato di azioni che può eseguire, aggiungendo uno strumento, l'agente ora può eseguire una vasta gamma di azioni. In questo capitolo, esamineremo il Pattern di progettazione per l'uso degli strumenti, che descrive come gli agenti AI possono utilizzare strumenti specifici per raggiungere i propri obiettivi.

## Introduzione

In questa lezione cercheremo di rispondere alle seguenti domande:

- Cos'è il pattern di progettazione per l'uso degli strumenti?
- Quali sono i casi d'uso a cui può essere applicato?
- Quali sono gli elementi/blocchi costitutivi necessari per implementare il pattern di progettazione?
- Quali sono le considerazioni speciali per usare il Pattern di progettazione per l'uso degli strumenti per costruire agenti AI affidabili?

## Obiettivi di apprendimento

Dopo aver completato questa lezione, sarai in grado di:

- Definire il Pattern di progettazione per l'uso degli strumenti e il suo scopo.
- Identificare i casi d'uso in cui è applicabile il Pattern di progettazione per l'uso degli strumenti.
- Comprendere gli elementi chiave necessari per implementare il pattern di progettazione.
- Riconoscere le considerazioni per garantire l'affidabilità negli agenti AI che utilizzano questo pattern di progettazione.

## Cos'è il Pattern di progettazione per l'uso degli strumenti?

Il **Pattern di progettazione per l'uso degli strumenti** si concentra sull'offrire agli LLM la capacità di interagire con strumenti esterni per raggiungere obiettivi specifici. Gli strumenti sono codice eseguibile da un agente per compiere azioni. Uno strumento può essere una funzione semplice come una calcolatrice o una chiamata API a un servizio di terze parti come la ricerca del prezzo azionario o la previsione meteo. Nel contesto degli agenti AI, gli strumenti sono progettati per essere eseguiti dagli agenti in risposta a **chiamate di funzione generate dal modello**.

## Quali sono i casi d'uso a cui può essere applicato?

Gli agenti AI possono sfruttare gli strumenti per completare compiti complessi, recuperare informazioni o prendere decisioni. Il pattern di progettazione per l'uso degli strumenti viene spesso utilizzato in scenari che richiedono interazione dinamica con sistemi esterni, come database, servizi web o interpreti di codice. Questa capacità è utile per diversi casi d'uso, inclusi:

- **Recupero dinamico delle informazioni:** Gli agenti possono interrogare API esterne o database per ottenere dati aggiornati (es. interrogare un database SQLite per analisi dati, acquisire prezzi azionari o informazioni meteorologiche).
- **Esecuzione e interpretazione di codice:** Gli agenti possono eseguire codice o script per risolvere problemi matematici, generare report o eseguire simulazioni.
- **Automazione dei flussi di lavoro:** Automatizzazione di flussi di lavoro ripetitivi o a più fasi integrando strumenti come pianificatori di attività, servizi email o pipeline di dati.
- **Supporto clienti:** Gli agenti possono interagire con sistemi CRM, piattaforme di ticketing o knowledge base per risolvere richieste degli utenti.
- **Generazione e modifica dei contenuti:** Gli agenti possono sfruttare strumenti come correttori grammaticali, sintetizzatori di testi o valutatori di sicurezza dei contenuti per assistenza nelle attività di creazione dei contenuti.

## Quali sono gli elementi/blocchi costitutivi necessari per implementare il pattern di progettazione per l'uso degli strumenti?

Questi blocchi costitutivi permettono all'agente AI di eseguire un’ampia varietà di compiti. Vediamo quali sono gli elementi chiave necessari per implementare il Pattern di progettazione per l'uso degli strumenti:

- **Schema delle funzioni/strumenti**: Definizioni dettagliate degli strumenti disponibili, inclusi nome della funzione, scopo, parametri richiesti e output attesi. Questi schema permettono all’LLM di comprendere quali strumenti sono disponibili e come costruire richieste valide.

- **Logica di esecuzione delle funzioni**: Regola come e quando gli strumenti vengono invocati in base all'intento dell'utente e al contesto della conversazione. Può includere moduli pianificatori, meccanismi di instradamento o flussi condizionali che determinano dinamicamente l’uso degli strumenti.

- **Sistema di gestione dei messaggi**: Componenti che gestiscono il flusso conversazionale tra input dell’utente, risposte LLM, chiamate agli strumenti e output degli strumenti.

- **Framework di integrazione degli strumenti**: Infrastruttura che connette l'agente ai vari strumenti, siano essi funzioni semplici o servizi esterni complessi.

- **Gestione degli errori e validazione**: Meccanismi per gestire fallimenti nell’esecuzione degli strumenti, convalidare i parametri e gestire risposte inattese.

- **Gestione dello stato**: Tiene traccia del contesto della conversazione, delle interazioni precedenti con gli strumenti e dei dati persistenti per garantire coerenza nelle interazioni a più turni.

Successivamente, diamo uno sguardo più dettagliato alle chiamate di funzione/strumento.

### Chiamata di funzione/strumento

La chiamata di funzione è il modo principale con cui abilitiamo i Modelli di Linguaggio Estesi (LLM) a interagire con gli strumenti. Spesso vedrai i termini 'Funzione' e 'Strumento' usati in modo intercambiabile perché le 'funzioni' (blocchi di codice riutilizzabile) sono gli 'strumenti' che gli agenti usano per eseguire compiti. Per poter invocare il codice di una funzione, un LLM deve confrontare la richiesta dell’utente con la descrizione delle funzioni. A tal fine, uno schema contenente le descrizioni di tutte le funzioni disponibili viene inviato all’LLM. L’LLM quindi seleziona la funzione più appropriata per il compito e ne restituisce il nome e gli argomenti. La funzione selezionata viene invocata, la sua risposta viene restituita all’LLM, che usa l’informazione per rispondere alla richiesta dell’utente.

Per implementare la chiamata di funzione per agenti, avrai bisogno di:

1. Un modello LLM che supporti la chiamata di funzione
2. Uno schema contenente le descrizioni delle funzioni
3. Il codice per ogni funzione descritta

Usiamo l'esempio di ottenere l'ora attuale in una città per illustrare:

1. **Inizializzare un LLM che supporta la chiamata di funzione:**

    Non tutti i modelli supportano la chiamata di funzione, quindi è importante verificare che l'LLM che stai utilizzando lo faccia.     <a href="https://learn.microsoft.com/azure/ai-services/openai/how-to/function-calling" target="_blank">Azure OpenAI</a> supporta la chiamata di funzione. Possiamo iniziare creando il client Azure OpenAI. 

    ```python
    # Inizializza il client Azure OpenAI
    client = AzureOpenAI(
        azure_endpoint = os.getenv("AZURE_AI_PROJECT_ENDPOINT"), 
        api_key=os.getenv("AZURE_OPENAI_API_KEY"),  
        api_version="2024-05-01-preview"
    )
    ```

1. **Creare uno schema di funzione**:

    Successivamente definiremo uno schema JSON che contiene il nome della funzione, la descrizione di cosa fa la funzione, e i nomi e le descrizioni dei parametri della funzione. 
    Passeremo quindi questo schema al client creato precedentemente, insieme alla richiesta dell’utente per trovare l’ora a San Francisco. È importante notare che ciò che viene restituito è una **chiamata a uno strumento**, **non** la risposta finale alla domanda. Come detto prima, l’LLM restituisce il nome della funzione che ha selezionato per il compito, e gli argomenti che verranno passati ad essa.

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
  
1. **Il codice della funzione necessario per eseguire il compito:**

    Ora che l’LLM ha scelto quale funzione deve essere eseguita, il codice che esegue il compito deve essere implementato ed eseguito.
    Possiamo implementare il codice per ottenere l’ora attuale in Python. Dovremo anche scrivere il codice per estrarre il nome e gli argomenti dal response_message per ottenere il risultato finale.

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
  
      # Seconda chiamata API: ottenere la risposta finale dal modello
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

La chiamata di funzione è al centro della maggior parte, se non di tutti, i design per l’uso degli strumenti negli agenti, tuttavia implementarla da zero a volte può essere impegnativo.
Come abbiamo imparato in [Lezione 2](../../../02-explore-agentic-frameworks), i framework agentic ci forniscono blocchi pre-costruiti per implementare l’uso degli strumenti.
 
## Esempi di uso degli strumenti con framework agentic

Ecco alcuni esempi di come puoi implementare il Pattern di progettazione per l’uso degli strumenti utilizzando diversi framework agentic:

### Microsoft Agent Framework

<a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Microsoft Agent Framework</a> è un framework AI open source per costruire agenti AI. Semplifica il processo di utilizzo della chiamata di funzione permettendo di definire gli strumenti come funzioni Python con il decoratore `@tool`. Il framework gestisce la comunicazione di andata e ritorno tra il modello e il tuo codice. Fornisce anche accesso a strumenti pre-costruiti come Ricerca File e Interprete di Codice tramite `AzureAIProjectAgentProvider`.

Il diagramma seguente illustra il processo di chiamata di funzione con Microsoft Agent Framework:

![chiamata di funzione](../../../translated_images/it/functioncalling-diagram.a84006fc287f6014.webp)

Nel Microsoft Agent Framework, gli strumenti sono definiti come funzioni decorate. Possiamo convertire la funzione `get_current_time` vista prima in uno strumento usando il decoratore `@tool`. Il framework serializzerà automaticamente la funzione e i suoi parametri, creando lo schema da inviare all’LLM.

```python
from agent_framework import tool
from agent_framework.azure import AzureAIProjectAgentProvider
from azure.identity import AzureCliCredential

@tool
def get_current_time(location: str) -> str:
    """Get the current time for a given location"""
    ...

# Crea il client
provider = AzureAIProjectAgentProvider(credential=AzureCliCredential())

# Crea un agente ed esegui con lo strumento
agent = await provider.create_agent(name="TimeAgent", instructions="Use available tools to answer questions.", tools=get_current_time)
response = await agent.run("What time is it?")
```
  
### Azure AI Agent Service

<a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Azure AI Agent Service</a> è un framework agentic più recente progettato per permettere agli sviluppatori di costruire, distribuire e scalare agenti AI di alta qualità e estensibili in modo sicuro, senza dover gestire direttamente le risorse di calcolo e archiviazione sottostanti. È particolarmente utile per applicazioni enterprise in quanto è un servizio completamente gestito con sicurezza di livello enterprise.

Rispetto allo sviluppo diretto con l’API LLM, Azure AI Agent Service offre alcuni vantaggi, tra cui:

- Chiamata automatica agli strumenti: non è necessario analizzare una chiamata a uno strumento, invocarne l’esecuzione e gestire la risposta; tutto ciò viene effettuato lato server
- Gestione sicura dei dati: invece di gestire autonomamente lo stato della conversazione, si può fare affidamento sui thread per memorizzare tutte le informazioni necessarie
- Strumenti pronti all’uso: strumenti con cui interagire con le tue fonti dati, come Bing, Azure AI Search e Azure Functions.

Gli strumenti disponibili in Azure AI Agent Service possono essere divisi in due categorie:

1. Strumenti di conoscenza:
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/bing-grounding?tabs=python&pivots=overview" target="_blank">Grounding con Bing Search</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/file-search?tabs=python&pivots=overview" target="_blank">Ricerca File</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-ai-search?tabs=azurecli%2Cpython&pivots=overview-azure-ai-search" target="_blank">Azure AI Search</a>

2. Strumenti di azione:
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/function-calling?tabs=python&pivots=overview" target="_blank">Chiamata di funzione</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/code-interpreter?tabs=python&pivots=overview" target="_blank">Interprete di codice</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/openapi-spec?tabs=python&pivots=overview" target="_blank">Strumenti definiti da OpenAPI</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-functions?pivots=overview" target="_blank">Azure Functions</a>

Il servizio Agent permette di usare questi strumenti insieme come un `toolset`. Utilizza anche `threads` che tengono traccia della cronologia dei messaggi di una determinata conversazione.

Immagina di essere un agente di vendita in un’azienda chiamata Contoso. Vuoi sviluppare un agente conversazionale che possa rispondere a domande sui tuoi dati di vendita.

L’immagine seguente illustra come potresti usare Azure AI Agent Service per analizzare i tuoi dati di vendita:

![Servizio agentic in azione](../../../translated_images/it/agent-service-in-action.34fb465c9a84659e.webp)

Per usare uno qualsiasi di questi strumenti con il servizio possiamo creare un client e definire uno strumento o un toolset. Per implementare questo praticamente possiamo usare il seguente codice Python. L’LLM sarà in grado di esaminare il toolset e scegliere se usare la funzione creata dall’utente, `fetch_sales_data_using_sqlite_query`, o l’interprete di codice pre-costruito, a seconda della richiesta dell’utente.

```python 
import os
from azure.ai.projects import AIProjectClient
from azure.identity import DefaultAzureCredential
from fetch_sales_data_functions import fetch_sales_data_using_sqlite_query # funzione fetch_sales_data_using_sqlite_query che si trova in un file fetch_sales_data_functions.py.
from azure.ai.projects.models import ToolSet, FunctionTool, CodeInterpreterTool

project_client = AIProjectClient.from_connection_string(
    credential=DefaultAzureCredential(),
    conn_str=os.environ["PROJECT_CONNECTION_STRING"],
)

# Inizializza il set di strumenti
toolset = ToolSet()

# Inizializza l'agente di chiamata funzione con la funzione fetch_sales_data_using_sqlite_query e aggiungila al set di strumenti
fetch_data_function = FunctionTool(fetch_sales_data_using_sqlite_query)
toolset.add(fetch_data_function)

# Inizializza lo strumento Code Interpreter e aggiungilo al set di strumenti.
code_interpreter = code_interpreter = CodeInterpreterTool()
toolset.add(code_interpreter)

agent = project_client.agents.create_agent(
    model="gpt-4o-mini", name="my-agent", instructions="You are helpful agent", 
    toolset=toolset
)
```

## Quali sono le considerazioni speciali per usare il Pattern di progettazione per l'uso degli strumenti per costruire agenti AI affidabili?

Una preoccupazione comune con le query SQL generate dinamicamente dagli LLM riguarda la sicurezza, in particolare il rischio di SQL injection o azioni malevole, come cancellare o manomettere il database. Anche se queste preoccupazioni sono valide, possono essere efficacemente mitigate configurando correttamente i permessi di accesso al database. Per la maggior parte dei database questo comporta configurare il database in sola lettura. Per servizi database come PostgreSQL o Azure SQL, l’app dovrebbe ricevere un ruolo in sola lettura (SELECT).

Eseguire l’app in un ambiente sicuro migliora ulteriormente la protezione. Nei scenari enterprise, i dati sono tipicamente estratti e trasformati dai sistemi operativi in un database o data warehouse in sola lettura con uno schema adatto all’uso utente. Questo approccio garantisce che i dati siano sicuri, ottimizzati per prestazioni e accessibilità e che l’app abbia accesso ristretto e in sola lettura.

## Codici di esempio

- Python: [Agent Framework](./code_samples/04-python-agent-framework.ipynb)
- .NET: [Agent Framework](./code_samples/04-dotnet-agent-framework.md)

## Hai altre domande sul Pattern di progettazione per l’uso degli strumenti?

Unisciti al [Microsoft Foundry Discord](https://aka.ms/ai-agents/discord) per incontrare altri studenti, partecipare alle office hours e ottenere risposte alle tue domande sugli agenti AI.

## Risorse aggiuntive

- <a href="https://microsoft.github.io/build-your-first-agent-with-azure-ai-agent-service-workshop/" target="_blank">Workshop di Azure AI Agents Service</a>
- <a href="https://github.com/Azure-Samples/contoso-creative-writer/tree/main/docs/workshop" target="_blank">Workshop Multi-Agente Contoso Creative Writer</a>
- <a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Panoramica di Microsoft Agent Framework</a>

## Lezione precedente

[Comprendere i Pattern Agentic](../03-agentic-design-patterns/README.md)

## Prossima lezione
[Agentic RAG](../05-agentic-rag/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Dichiarazione di Non Responsabilità**:  
Questo documento è stato tradotto utilizzando il servizio di traduzione automatica AI [Co-op Translator](https://github.com/Azure/co-op-translator). Pur impegnandoci a garantire l'accuratezza, si prega di notare che le traduzioni automatiche possono contenere errori o imprecisioni. Il documento originale nella sua lingua madre deve essere considerato la fonte autorevole. Per informazioni critiche, si raccomanda una traduzione professionale effettuata da un essere umano. Non ci assumiamo alcuna responsabilità per eventuali malintesi o interpretazioni errate derivanti dall'uso di questa traduzione.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->