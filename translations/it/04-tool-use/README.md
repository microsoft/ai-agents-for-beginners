[![Come progettare buoni agenti AI](../../../translated_images/it/lesson-4-thumbnail.546162853cb3daff.webp)](https://youtu.be/vieRiPRx-gI?si=cEZ8ApnT6Sus9rhn)

> _(Clicca sull'immagine sopra per visualizzare il video di questa lezione)_

# Pattern di Progettazione per l'Uso di Strumenti

Gli strumenti sono interessanti perché consentono agli agenti AI di avere una gamma più ampia di capacità. Invece di avere un insieme limitato di azioni che l'agente può eseguire, aggiungendo uno strumento, l'agente può ora eseguire un'ampia varietà di azioni. In questo capitolo, esamineremo il Pattern di Progettazione per l'Uso di Strumenti, che descrive come gli agenti AI possano utilizzare strumenti specifici per raggiungere i propri obiettivi.

## Introduzione

In questa lezione, cercheremo di rispondere alle seguenti domande:

- Cos'è il pattern di progettazione per l'uso di strumenti?
- Quali sono i casi d'uso a cui può essere applicato?
- Quali sono gli elementi/blocchi costitutivi necessari per implementare il pattern di progettazione?
- Quali sono le considerazioni speciali per utilizzare il Pattern di Progettazione per l'Uso di Strumenti per costruire agenti AI affidabili?

## Obiettivi di Apprendimento

Dopo aver completato questa lezione, sarai in grado di:

- Definire il Pattern di Progettazione per l'Uso di Strumenti e il suo scopo.
- Identificare i casi d'uso in cui il Pattern di Progettazione per l'Uso di Strumenti è applicabile.
- Comprendere gli elementi chiave necessari per implementare il pattern di progettazione.
- Riconoscere le considerazioni per garantire l'affidabilità degli agenti AI che utilizzano questo pattern di progettazione.

## Cos'è il Pattern di Progettazione per l'Uso di Strumenti?

Il **Pattern di Progettazione per l'Uso di Strumenti** si concentra nel fornire ai LLM la capacità di interagire con strumenti esterni per raggiungere obiettivi specifici. Gli strumenti sono codice che può essere eseguito da un agente per svolgere azioni. Uno strumento può essere una funzione semplice come una calcolatrice, o una chiamata API a un servizio di terze parti come la ricerca del prezzo delle azioni o la previsione del tempo. Nel contesto degli agenti AI, gli strumenti sono progettati per essere eseguiti dagli agenti in risposta a **chiamate di funzione generate dal modello**.

## A quali casi d'uso può essere applicato?

Gli agenti AI possono sfruttare gli strumenti per completare compiti complessi, recuperare informazioni o prendere decisioni. Il pattern di progettazione per l'uso di strumenti viene spesso utilizzato in scenari che richiedono interazione dinamica con sistemi esterni, come database, servizi web o interpreti di codice. Questa capacità è utile per vari casi d'uso tra cui:

- **Recupero Dinamico di Informazioni:** gli agenti possono interrogare API esterne o database per ottenere dati aggiornati (ad esempio, interrogare un database SQLite per l'analisi dei dati, recuperare prezzi azionari o informazioni meteo).
- **Esecuzione e Interpretazione di Codice:** gli agenti possono eseguire codice o script per risolvere problemi matematici, generare report o effettuare simulazioni.
- **Automazione del Flusso di Lavoro:** automatizzare flussi di lavoro ripetitivi o composti da più passaggi integrando strumenti come schedulatori di attività, servizi email o pipeline di dati.
- **Supporto Clienti:** gli agenti possono interagire con sistemi CRM, piattaforme di ticketing o basi di conoscenza per risolvere le richieste degli utenti.
- **Generazione e Modifica di Contenuti:** gli agenti possono utilizzare strumenti come correttori grammaticali, sintetizzatori di testo o valutatori di sicurezza dei contenuti per assistere nelle attività di creazione dei contenuti.

## Quali sono gli elementi/blocchi costitutivi necessari per implementare il pattern di progettazione per l’uso di strumenti?

Questi blocchi costitutivi consentono all'agente AI di eseguire una vasta gamma di compiti. Esaminiamo gli elementi chiave necessari per implementare il Pattern di Progettazione per l'Uso di Strumenti:

- **Schemi di Funzione/Strumento**: definizioni dettagliate degli strumenti disponibili, inclusi nome della funzione, scopo, parametri richiesti e output previsti. Questi schemi permettono al LLM di comprendere quali strumenti sono disponibili e come costruire richieste valide.

- **Logica di Esecuzione della Funzione**: governa come e quando gli strumenti vengono invocati in base all'intento dell'utente e al contesto della conversazione. Può includere moduli di pianificazione, meccanismi di instradamento o flussi condizionali che determinano dinamicamente l'uso degli strumenti.

- **Sistema di Gestione dei Messaggi**: componenti che gestiscono il flusso conversazionale tra input dell'utente, risposte LLM, chiamate agli strumenti e output degli strumenti.

- **Framework di Integrazione degli Strumenti**: infrastruttura che collega l'agente a vari strumenti, siano essi funzioni semplici o servizi esterni complessi.

- **Gestione degli Errori e Validazione**: meccanismi per gestire fallimenti nell'esecuzione degli strumenti, convalidare parametri e gestire risposte inattese.

- **Gestione dello Stato**: traccia il contesto della conversazione, le interazioni precedenti con gli strumenti e i dati persistenti per garantire coerenza nelle interazioni multi-turno.

Passiamo ora a esaminare in dettaglio la Chiamata di Funzione/Strumento.

### Chiamata di Funzione/Strumento

La chiamata di funzione è il modo principale con cui abilitiamo i Large Language Model (LLM) a interagire con gli strumenti. Spesso vedrai 'Funzione' e 'Strumento' usati in modo intercambiabile perché le 'funzioni' (blocchi di codice riutilizzabile) sono gli 'strumenti' che gli agenti usano per svolgere compiti. Per fare in modo che il codice di una funzione venga invocato, un LLM deve confrontare la richiesta dell'utente con la descrizione delle funzioni. Per fare questo viene inviato al LLM uno schema contenente le descrizioni di tutte le funzioni disponibili. L'LLM quindi seleziona la funzione più appropriata per il compito e ne restituisce il nome e gli argomenti. La funzione selezionata viene invocata, la sua risposta è inviata di nuovo al LLM, che utilizza le informazioni per rispondere alla richiesta dell'utente.

Per gli sviluppatori che vogliono implementare la chiamata di funzione per agenti, sono necessari:

1. Un modello LLM che supporti la chiamata di funzione
2. Uno schema contenente descrizioni delle funzioni
3. Il codice per ciascuna funzione descritta

Usiamo l'esempio di ottenere l'ora corrente in una città per illustrare:

1. **Inizializzare un LLM che supporta la chiamata di funzione:**

    Non tutti i modelli supportano la chiamata di funzione, quindi è importante verificare che l’LLM utilizzato lo supporti. <a href="https://learn.microsoft.com/azure/ai-services/openai/how-to/function-calling" target="_blank">Azure OpenAI</a> supporta la chiamata di funzione. Possiamo iniziare avviando il client Azure OpenAI. 

    ```python
    # Inizializza il client Azure OpenAI
    client = AzureOpenAI(
        azure_endpoint = os.getenv("AZURE_AI_PROJECT_ENDPOINT"), 
        api_key=os.getenv("AZURE_OPENAI_API_KEY"),  
        api_version="2024-05-01-preview"
    )
    ```

1. **Creare uno Schema per la Funzione:**

    Successivamente definiremo uno schema JSON che contiene il nome della funzione, la descrizione di cosa fa la funzione e i nomi e descrizioni dei parametri della funzione.
    Poi passeremo questo schema al client creato in precedenza, insieme alla richiesta dell’utente per trovare l’ora a San Francisco. È importante notare che viene restituita una **chiamata a strumento**, **non** la risposta finale alla domanda. Come detto prima, l’LLM restituisce il nome della funzione selezionata per il compito e gli argomenti da passarle.

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
  
    # Prima chiamata API: Chiedere al modello di utilizzare la funzione
      response = client.chat.completions.create(
          model=deployment_name,
          messages=messages,
          tools=tools,
          tool_choice="auto",
      )
  
      # Elaborare la risposta del modello
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

    Ora che l’LLM ha scelto quale funzione deve essere eseguita, il codice che svolge il compito deve essere implementato ed eseguito.
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
  
      # Seconda chiamata API: Ottieni la risposta finale dal modello
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

La Chiamata di Funzione è al centro della maggior parte, se non di tutti i design per l’uso di strumenti da parte degli agenti, tuttavia implementarla da zero a volte può essere una sfida.
Come abbiamo imparato in [Lezione 2](../../../02-explore-agentic-frameworks), i framework agentici ci forniscono blocchi predefiniti per implementare l’uso di strumenti.
 
## Esempi di Uso di Strumenti con Framework Agentici

Ecco alcuni esempi di come è possibile implementare il Pattern di Progettazione per l’Uso di Strumenti utilizzando diversi framework agentici:

### Microsoft Agent Framework

<a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Microsoft Agent Framework</a> è un framework AI open-source per costruire agenti AI. Semplifica il processo di uso della chiamata di funzione permettendo di definire strumenti come funzioni Python con il decoratore `@tool`. Il framework gestisce la comunicazione tra il modello e il tuo codice. Offre inoltre accesso a strumenti predefiniti come File Search e Code Interpreter tramite `AzureAIProjectAgentProvider`.

Il seguente diagramma illustra il processo di chiamata di funzione con il Microsoft Agent Framework:

![function calling](../../../translated_images/it/functioncalling-diagram.a84006fc287f6014.webp)

Nel Microsoft Agent Framework, gli strumenti sono definiti come funzioni decorate. Possiamo convertire la funzione `get_current_time` vista prima in uno strumento usando il decoratore `@tool`. Il framework serializza automaticamente la funzione e i suoi parametri, creando lo schema da inviare all’LLM.

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

# Crea un agente ed eseguilo con lo strumento
agent = await provider.create_agent(name="TimeAgent", instructions="Use available tools to answer questions.", tools=get_current_time)
response = await agent.run("What time is it?")
```
  
### Azure AI Agent Service

<a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Azure AI Agent Service</a> è un framework agentico più recente progettato per permettere agli sviluppatori di costruire, distribuire e scalare agenti AI di alta qualità, estensibili e sicuri senza dover gestire direttamente risorse di calcolo e storage sottostanti. È particolarmente utile per applicazioni enterprise, essendo un servizio completamente gestito con sicurezza di livello enterprise.

Rispetto allo sviluppo diretto con l’API LLM, Azure AI Agent Service offre alcuni vantaggi, tra cui:

- Chiamata automatica di strumenti – non è necessario analizzare una chiamata a strumento, invocare lo strumento e gestire la risposta; tutto questo è ora gestito lato server
- Dati gestiti in modo sicuro – invece di gestire lo stato della conversazione autonomamente, puoi fare affidamento sui thread per memorizzare tutte le informazioni necessarie
- Strumenti pronti all’uso – strumenti che puoi utilizzare per interagire con le tue fonti dati, come Bing, Azure AI Search e Azure Functions.

Gli strumenti disponibili in Azure AI Agent Service possono essere divisi in due categorie:

1. Strumenti di Conoscenza:
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/bing-grounding?tabs=python&pivots=overview" target="_blank">Grounding con Bing Search</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/file-search?tabs=python&pivots=overview" target="_blank">Ricerca File</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-ai-search?tabs=azurecli%2Cpython&pivots=overview-azure-ai-search" target="_blank">Azure AI Search</a>

2. Strumenti di Azione:
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/function-calling?tabs=python&pivots=overview" target="_blank">Chiamata di Funzione</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/code-interpreter?tabs=python&pivots=overview" target="_blank">Code Interpreter</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/openapi-spec?tabs=python&pivots=overview" target="_blank">Strumenti definiti da OpenAPI</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-functions?pivots=overview" target="_blank">Azure Functions</a>

Il servizio Agent ci permette di usare questi strumenti insieme come un `toolset`. Utilizza anche i `threads` che tengono traccia della cronologia dei messaggi di una specifica conversazione.

Immagina di essere un agente di vendita in un’azienda chiamata Contoso. Vuoi sviluppare un agente conversazionale che possa rispondere a domande sui dati di vendita.

L’immagine seguente illustra come potresti usare Azure AI Agent Service per analizzare i dati di vendita:

![Agentic Service In Action](../../../translated_images/it/agent-service-in-action.34fb465c9a84659e.webp)

Per usare uno qualsiasi di questi strumenti con il servizio, possiamo creare un client e definire uno strumento o un toolset. Per implementare questo praticamente possiamo usare il seguente codice Python. L’LLM potrà guardare al toolset e decidere se usare la funzione creata dall’utente, `fetch_sales_data_using_sqlite_query`, o il Code Interpreter predefinito a seconda della richiesta dell’utente.

```python 
import os
from azure.ai.projects import AIProjectClient
from azure.identity import DefaultAzureCredential
from fetch_sales_data_functions import fetch_sales_data_using_sqlite_query # funzione fetch_sales_data_using_sqlite_query che può essere trovata in un file fetch_sales_data_functions.py.
from azure.ai.projects.models import ToolSet, FunctionTool, CodeInterpreterTool

project_client = AIProjectClient.from_connection_string(
    credential=DefaultAzureCredential(),
    conn_str=os.environ["PROJECT_CONNECTION_STRING"],
)

# Inizializza il set di strumenti
toolset = ToolSet()

# Inizializza l'agente per le chiamate di funzione con la funzione fetch_sales_data_using_sqlite_query e la aggiunge al set di strumenti
fetch_data_function = FunctionTool(fetch_sales_data_using_sqlite_query)
toolset.add(fetch_data_function)

# Inizializza lo strumento Code Interpreter e lo aggiunge al set di strumenti.
code_interpreter = CodeInterpreterTool()toolset.add(code_interpreter)

agent = project_client.agents.create_agent(
    model="gpt-4o-mini", name="my-agent", instructions="You are helpful agent", 
    toolset=toolset
)
```

## Quali sono le considerazioni speciali per utilizzare il Pattern di Progettazione per l’Uso di Strumenti per costruire agenti AI affidabili?

Una preoccupazione comune con SQL generato dinamicamente da LLM è la sicurezza, in particolare il rischio di SQL injection o azioni dannose, come cancellazioni o manomissioni del database. Sebbene queste preoccupazioni siano valide, possono essere efficacemente mitigate configurando correttamente i permessi di accesso al database. Per la maggior parte dei database ciò comporta la configurazione del database in sola lettura. Per servizi di database come PostgreSQL o Azure SQL, l’app dovrebbe avere un ruolo in sola lettura (SELECT).

L’esecuzione dell’app in un ambiente sicuro migliora ulteriormente la protezione. Negli scenari enterprise, i dati vengono tipicamente estratti e trasformati da sistemi operativi in un database o data warehouse in sola lettura con uno schema user-friendly. Questo approccio assicura che i dati siano sicuri, ottimizzati per prestazioni e accessibilità, e che l’app abbia accesso limitato e in sola lettura.

## Codici di Esempio

- Python: [Agent Framework](./code_samples/04-python-agent-framework.ipynb)
- .NET: [Agent Framework](./code_samples/04-dotnet-agent-framework.md)

## Hai altre domande sui Pattern di Progettazione per l'Uso di Strumenti?

Unisciti al [Microsoft Foundry Discord](https://aka.ms/ai-agents/discord) per incontrare altri studenti, partecipare alle ore di supporto e ottenere risposte alle tue domande sugli agenti AI.

## Risorse Aggiuntive

- <a href="https://microsoft.github.io/build-your-first-agent-with-azure-ai-agent-service-workshop/" target="_blank">Workshop sul Servizio Azure AI Agents</a>
- <a href="https://github.com/Azure-Samples/contoso-creative-writer/tree/main/docs/workshop" target="_blank">Workshop Multi-Agente Contoso Creative Writer</a>
- <a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Panoramica Microsoft Agent Framework</a>

## Lezione Precedente

[Comprendere i Pattern di Progettazione Agentici](../03-agentic-design-patterns/README.md)

## Prossima Lezione
[Agentic RAG](../05-agentic-rag/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:
Questo documento è stato tradotto utilizzando il servizio di traduzione AI [Co-op Translator](https://github.com/Azure/co-op-translator). Sebbene ci impegniamo per garantire la precisione, si prega di notare che le traduzioni automatizzate possono contenere errori o imprecisioni. Il documento originale nella sua lingua nativa deve essere considerato la fonte autorevole. Per informazioni critiche, si raccomanda una traduzione professionale effettuata da un essere umano. Non siamo responsabili per eventuali malintesi o interpretazioni errate derivanti dall’uso di questa traduzione.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->