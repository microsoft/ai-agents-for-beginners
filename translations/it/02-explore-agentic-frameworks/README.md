<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "7120197753abacc827b64ac2d5d6966f",
  "translation_date": "2025-11-13T12:16:53+00:00",
  "source_file": "02-explore-agentic-frameworks/README.md",
  "language_code": "it"
}
-->
[![Esplorare i Framework per Agenti AI](../../../translated_images/lesson-2-thumbnail.c65f44c93b8558df4d5d407e29970e654629e614f357444a9c27c80feb54c79d.it.png)](https://youtu.be/ODwF-EZo_O8?si=1xoy_B9RNQfrYdF7)

> _(Clicca sull'immagine sopra per vedere il video di questa lezione)_

# Esplora i Framework per Agenti AI

I framework per agenti AI sono piattaforme software progettate per semplificare la creazione, il deployment e la gestione degli agenti AI. Questi framework offrono ai sviluppatori componenti predefiniti, astrazioni e strumenti che facilitano lo sviluppo di sistemi AI complessi.

Questi framework aiutano gli sviluppatori a concentrarsi sugli aspetti unici delle loro applicazioni fornendo approcci standardizzati alle sfide comuni nello sviluppo di agenti AI. Migliorano la scalabilità, l'accessibilità e l'efficienza nella costruzione di sistemi AI.

## Introduzione 

Questa lezione coprirà:

- Cosa sono i Framework per Agenti AI e cosa permettono agli sviluppatori di ottenere?
- Come possono i team utilizzarli per prototipare rapidamente, iterare e migliorare le capacità del loro agente?
- Quali sono le differenze tra i framework e gli strumenti creati da Microsoft <a href="https://aka.ms/ai-agents/autogen" target="_blank">AutoGen</a>, <a href="https://aka.ms/ai-agents-beginners/semantic-kernel" target="_blank">Semantic Kernel</a> e <a href="https://aka.ms/ai-agents-beginners/ai-agent-service" target="_blank">Azure AI Agent Service</a>?
- Posso integrare direttamente gli strumenti esistenti del mio ecosistema Azure o ho bisogno di soluzioni autonome?
- Cos'è il servizio Azure AI Agents e come mi sta aiutando?

## Obiettivi di apprendimento

Gli obiettivi di questa lezione sono aiutarti a comprendere:

- Il ruolo dei Framework per Agenti AI nello sviluppo AI.
- Come sfruttare i Framework per Agenti AI per costruire agenti intelligenti.
- Le capacità chiave abilitate dai Framework per Agenti AI.
- Le differenze tra AutoGen, Semantic Kernel e Azure AI Agent Service.

## Cosa sono i Framework per Agenti AI e cosa permettono agli sviluppatori di fare?

I framework AI tradizionali possono aiutarti a integrare l'AI nelle tue app e a migliorare queste app nei seguenti modi:

- **Personalizzazione**: L'AI può analizzare il comportamento e le preferenze degli utenti per fornire raccomandazioni, contenuti ed esperienze personalizzate.
Esempio: Servizi di streaming come Netflix utilizzano l'AI per suggerire film e serie basandosi sulla cronologia di visualizzazione, migliorando il coinvolgimento e la soddisfazione degli utenti.
- **Automazione ed Efficienza**: L'AI può automatizzare attività ripetitive, semplificare i flussi di lavoro e migliorare l'efficienza operativa.
Esempio: Le app di assistenza clienti utilizzano chatbot alimentati dall'AI per gestire richieste comuni, riducendo i tempi di risposta e liberando gli agenti umani per questioni più complesse.
- **Esperienza Utente Migliorata**: L'AI può migliorare l'esperienza utente complessiva fornendo funzionalità intelligenti come il riconoscimento vocale, l'elaborazione del linguaggio naturale e il testo predittivo.
Esempio: Assistenti virtuali come Siri e Google Assistant utilizzano l'AI per comprendere e rispondere ai comandi vocali, rendendo più facile per gli utenti interagire con i loro dispositivi.

### Sembra tutto fantastico, giusto? Allora perché abbiamo bisogno dei Framework per Agenti AI?

I framework per agenti AI rappresentano qualcosa di più rispetto ai semplici framework AI. Sono progettati per consentire la creazione di agenti intelligenti che possono interagire con gli utenti, altri agenti e l'ambiente per raggiungere obiettivi specifici. Questi agenti possono mostrare comportamenti autonomi, prendere decisioni e adattarsi a condizioni mutevoli. Vediamo alcune capacità chiave abilitate dai Framework per Agenti AI:

- **Collaborazione e Coordinamento tra Agenti**: Consentono la creazione di più agenti AI che possono lavorare insieme, comunicare e coordinarsi per risolvere compiti complessi.
- **Automazione e Gestione dei Compiti**: Forniscono meccanismi per automatizzare flussi di lavoro multi-step, delega dei compiti e gestione dinamica dei compiti tra agenti.
- **Comprensione Contestuale e Adattamento**: Dotano gli agenti della capacità di comprendere il contesto, adattarsi agli ambienti mutevoli e prendere decisioni basate su informazioni in tempo reale.

In sintesi, gli agenti ti permettono di fare di più, portare l'automazione al livello successivo, creare sistemi più intelligenti che possono adattarsi e apprendere dal loro ambiente.

## Come prototipare rapidamente, iterare e migliorare le capacità dell'agente?

Questo è un panorama in rapida evoluzione, ma ci sono alcune cose comuni alla maggior parte dei Framework per Agenti AI che possono aiutarti a prototipare e iterare rapidamente, ovvero componenti modulari, strumenti collaborativi e apprendimento in tempo reale. Approfondiamo questi aspetti:

- **Usa Componenti Modulari**: Gli SDK AI offrono componenti predefiniti come connettori AI e di memoria, chiamate di funzione utilizzando linguaggio naturale o plugin di codice, modelli di prompt e altro.
- **Sfrutta Strumenti Collaborativi**: Progetta agenti con ruoli e compiti specifici, permettendo loro di testare e perfezionare i flussi di lavoro collaborativi.
- **Apprendi in Tempo Reale**: Implementa cicli di feedback in cui gli agenti apprendono dalle interazioni e regolano il loro comportamento dinamicamente.

### Usa Componenti Modulari

SDK come Microsoft Semantic Kernel e LangChain offrono componenti predefiniti come connettori AI, modelli di prompt e gestione della memoria.

**Come possono usarli i team**: I team possono assemblare rapidamente questi componenti per creare un prototipo funzionale senza partire da zero, consentendo una sperimentazione e iterazione rapide.

**Come funziona in pratica**: Puoi utilizzare un parser predefinito per estrarre informazioni dall'input dell'utente, un modulo di memoria per archiviare e recuperare dati e un generatore di prompt per interagire con gli utenti, tutto senza dover costruire questi componenti da zero.

**Esempio di codice**. Vediamo esempi di come puoi utilizzare un connettore AI predefinito con Semantic Kernel Python e .Net che utilizza la chiamata automatica di funzioni per far rispondere il modello all'input dell'utente:

``` python
# Semantic Kernel Python Example

import asyncio
from typing import Annotated

from semantic_kernel.connectors.ai import FunctionChoiceBehavior
from semantic_kernel.connectors.ai.open_ai import AzureChatCompletion, AzureChatPromptExecutionSettings
from semantic_kernel.contents import ChatHistory
from semantic_kernel.functions import kernel_function
from semantic_kernel.kernel import Kernel

# Define a ChatHistory object to hold the conversation's context
chat_history = ChatHistory()
chat_history.add_user_message("I'd like to go to New York on January 1, 2025")


# Define a sample plugin that contains the function to book travel
class BookTravelPlugin:
    """A Sample Book Travel Plugin"""

    @kernel_function(name="book_flight", description="Book travel given location and date")
    async def book_flight(
        self, date: Annotated[str, "The date of travel"], location: Annotated[str, "The location to travel to"]
    ) -> str:
        return f"Travel was booked to {location} on {date}"

# Create the Kernel
kernel = Kernel()

# Add the sample plugin to the Kernel object
kernel.add_plugin(BookTravelPlugin(), plugin_name="book_travel")

# Define the Azure OpenAI AI Connector
chat_service = AzureChatCompletion(
    deployment_name="YOUR_DEPLOYMENT_NAME", 
    api_key="YOUR_API_KEY", 
    endpoint="https://<your-resource>.azure.openai.com/",
)

# Define the request settings to configure the model with auto-function calling
request_settings = AzureChatPromptExecutionSettings(function_choice_behavior=FunctionChoiceBehavior.Auto())


async def main():
    # Make the request to the model for the given chat history and request settings
    # The Kernel contains the sample that the model will request to invoke
    response = await chat_service.get_chat_message_content(
        chat_history=chat_history, settings=request_settings, kernel=kernel
    )
    assert response is not None

    """
    Note: In the auto function calling process, the model determines it can invoke the 
    `BookTravelPlugin` using the `book_flight` function, supplying the necessary arguments. 
    
    For example:

    "tool_calls": [
        {
            "id": "call_abc123",
            "type": "function",
            "function": {
                "name": "BookTravelPlugin-book_flight",
                "arguments": "{'location': 'New York', 'date': '2025-01-01'}"
            }
        }
    ]

    Since the location and date arguments are required (as defined by the kernel function), if the 
    model lacks either, it will prompt the user to provide them. For instance:

    User: Book me a flight to New York.
    Model: Sure, I'd love to help you book a flight. Could you please specify the date?
    User: I want to travel on January 1, 2025.
    Model: Your flight to New York on January 1, 2025, has been successfully booked. Safe travels!
    """

    print(f"`{response}`")
    # Example AI Model Response: `Your flight to New York on January 1, 2025, has been successfully booked. Safe travels! ✈️🗽`

    # Add the model's response to our chat history context
    chat_history.add_assistant_message(response.content)


if __name__ == "__main__":
    asyncio.run(main())
```
```csharp
// Semantic Kernel C# example

using Microsoft.SemanticKernel;
using Microsoft.SemanticKernel.ChatCompletion;
using System.ComponentModel;
using Microsoft.SemanticKernel.Connectors.AzureOpenAI;

ChatHistory chatHistory = [];
chatHistory.AddUserMessage("I'd like to go to New York on January 1, 2025");

var kernelBuilder = Kernel.CreateBuilder();
kernelBuilder.AddAzureOpenAIChatCompletion(
    deploymentName: "NAME_OF_YOUR_DEPLOYMENT",
    apiKey: "YOUR_API_KEY",
    endpoint: "YOUR_AZURE_ENDPOINT"
);
kernelBuilder.Plugins.AddFromType<BookTravelPlugin>("BookTravel"); 
var kernel = kernelBuilder.Build();

var settings = new AzureOpenAIPromptExecutionSettings()
{
    FunctionChoiceBehavior = FunctionChoiceBehavior.Auto()
};

var chatCompletion = kernel.GetRequiredService<IChatCompletionService>();

var response = await chatCompletion.GetChatMessageContentAsync(chatHistory, settings, kernel);

/*
Behind the scenes, the model recognizes the tool to call, what arguments it already has (location) and (date)
{

"tool_calls": [
    {
        "id": "call_abc123",
        "type": "function",
        "function": {
            "name": "BookTravelPlugin-book_flight",
            "arguments": "{'location': 'New York', 'date': '2025-01-01'}"
        }
    }
]
*/

Console.WriteLine(response.Content);
chatHistory.AddMessage(response!.Role, response!.Content!);

// Example AI Model Response: Your flight to New York on January 1, 2025, has been successfully booked. Safe travels! ✈️🗽

// Define a plugin that contains the function to book travel
public class BookTravelPlugin
{
    [KernelFunction("book_flight")]
    [Description("Book travel given location and date")]
    public async Task<string> BookFlight(DateTime date, string location)
    {
        return await Task.FromResult( $"Travel was booked to {location} on {date}");
    }
}
```

Da questo esempio puoi vedere come puoi sfruttare un parser predefinito per estrarre informazioni chiave dall'input dell'utente, come origine, destinazione e data di una richiesta di prenotazione di volo. Questo approccio modulare ti consente di concentrarti sulla logica di alto livello.

### Sfrutta Strumenti Collaborativi

Framework come CrewAI, Microsoft AutoGen e Semantic Kernel facilitano la creazione di più agenti che possono lavorare insieme.

**Come possono usarli i team**: I team possono progettare agenti con ruoli e compiti specifici, permettendo loro di testare e perfezionare i flussi di lavoro collaborativi e migliorare l'efficienza complessiva del sistema.

**Come funziona in pratica**: Puoi creare un team di agenti in cui ogni agente ha una funzione specializzata, come il recupero di dati, l'analisi o il processo decisionale. Questi agenti possono comunicare e condividere informazioni per raggiungere un obiettivo comune, come rispondere a una domanda dell'utente o completare un compito.

**Esempio di codice (AutoGen)**:

```python
# creating agents, then create a round robin schedule where they can work together, in this case in order

# Data Retrieval Agent
# Data Analysis Agent
# Decision Making Agent

agent_retrieve = AssistantAgent(
    name="dataretrieval",
    model_client=model_client,
    tools=[retrieve_tool],
    system_message="Use tools to solve tasks."
)

agent_analyze = AssistantAgent(
    name="dataanalysis",
    model_client=model_client,
    tools=[analyze_tool],
    system_message="Use tools to solve tasks."
)

# conversation ends when user says "APPROVE"
termination = TextMentionTermination("APPROVE")

user_proxy = UserProxyAgent("user_proxy", input_func=input)

team = RoundRobinGroupChat([agent_retrieve, agent_analyze, user_proxy], termination_condition=termination)

stream = team.run_stream(task="Analyze data", max_turns=10)
# Use asyncio.run(...) when running in a script.
await Console(stream)
```

Quello che vedi nel codice precedente è come puoi creare un compito che coinvolge più agenti che lavorano insieme per analizzare i dati. Ogni agente svolge una funzione specifica e il compito viene eseguito coordinando gli agenti per raggiungere il risultato desiderato. Creando agenti dedicati con ruoli specializzati, puoi migliorare l'efficienza e le prestazioni del compito.

### Apprendi in Tempo Reale

I framework avanzati forniscono capacità per la comprensione contestuale e l'adattamento in tempo reale.

**Come possono usarli i team**: I team possono implementare cicli di feedback in cui gli agenti apprendono dalle interazioni e regolano il loro comportamento dinamicamente, portando a un miglioramento continuo e al perfezionamento delle capacità.

**Come funziona in pratica**: Gli agenti possono analizzare il feedback degli utenti, i dati ambientali e i risultati dei compiti per aggiornare la loro base di conoscenze, regolare gli algoritmi decisionali e migliorare le prestazioni nel tempo. Questo processo di apprendimento iterativo consente agli agenti di adattarsi alle condizioni mutevoli e alle preferenze degli utenti, migliorando l'efficacia complessiva del sistema.

## Quali sono le differenze tra i framework AutoGen, Semantic Kernel e Azure AI Agent Service?

Ci sono molti modi per confrontare questi framework, ma vediamo alcune differenze chiave in termini di design, capacità e casi d'uso target:

## AutoGen

AutoGen è un framework open-source sviluppato dal laboratorio AI Frontiers di Microsoft Research. Si concentra su applicazioni *agentiche* distribuite e basate su eventi, abilitando più LLM e SLM, strumenti e modelli di design avanzati per multi-agenti.

AutoGen è costruito attorno al concetto centrale di agenti, che sono entità autonome in grado di percepire il loro ambiente, prendere decisioni e intraprendere azioni per raggiungere obiettivi specifici. Gli agenti comunicano attraverso messaggi asincroni, permettendo loro di lavorare indipendentemente e in parallelo, migliorando la scalabilità e la reattività del sistema.

<a href="https://en.wikipedia.org/wiki/Actor_model" target="_blank">Gli agenti si basano sul modello attore</a>. Secondo Wikipedia, un attore è _il blocco di base della computazione concorrente. In risposta a un messaggio ricevuto, un attore può: prendere decisioni locali, creare più attori, inviare più messaggi e determinare come rispondere al prossimo messaggio ricevuto_.

**Casi d'uso**: Automazione della generazione di codice, analisi dei dati e costruzione di agenti personalizzati per funzioni di pianificazione e ricerca.

Ecco alcuni concetti fondamentali di AutoGen:

- **Agenti**. Un agente è un'entità software che:
  - **Comunica tramite messaggi**, che possono essere sincroni o asincroni.
  - **Mantiene il proprio stato**, che può essere modificato dai messaggi in arrivo.
  - **Esegue azioni** in risposta ai messaggi ricevuti o ai cambiamenti nel proprio stato. Queste azioni possono modificare lo stato dell'agente e produrre effetti esterni, come aggiornare i log dei messaggi, inviare nuovi messaggi, eseguire codice o effettuare chiamate API.
    
  Ecco un breve snippet di codice in cui crei il tuo agente con capacità di chat:

    ```python
    from autogen_agentchat.agents import AssistantAgent
    from autogen_agentchat.messages import TextMessage
    from autogen_ext.models.openai import OpenAIChatCompletionClient


    class MyAgent(RoutedAgent):
        def __init__(self, name: str) -> None:
            super().__init__(name)
            model_client = OpenAIChatCompletionClient(model="gpt-4o")
            self._delegate = AssistantAgent(name, model_client=model_client)
    
        @message_handler
        async def handle_my_message_type(self, message: MyMessageType, ctx: MessageContext) -> None:
            print(f"{self.id.type} received message: {message.content}")
            response = await self._delegate.on_messages(
                [TextMessage(content=message.content, source="user")], ctx.cancellation_token
            )
            print(f"{self.id.type} responded: {response.chat_message.content}")
    ```
    
    Nel codice precedente, `MyAgent` è stato creato e eredita da `RoutedAgent`. Ha un gestore di messaggi che stampa il contenuto del messaggio e poi invia una risposta utilizzando il delegato `AssistantAgent`. Nota in particolare come assegni a `self._delegate` un'istanza di `AssistantAgent`, che è un agente predefinito in grado di gestire completamenti di chat.


    Facciamo sapere ad AutoGen di questo tipo di agente e avviamo il programma:

    ```python
    
    # main.py
    runtime = SingleThreadedAgentRuntime()
    await MyAgent.register(runtime, "my_agent", lambda: MyAgent())

    runtime.start()  # Start processing messages in the background.
    await runtime.send_message(MyMessageType("Hello, World!"), AgentId("my_agent", "default"))
    ```

    Nel codice precedente gli agenti sono registrati con il runtime e poi viene inviato un messaggio all'agente, risultando nel seguente output:

    ```text
    # Output from the console:
    my_agent received message: Hello, World!
    my_assistant received message: Hello, World!
    my_assistant responded: Hello! How can I assist you today?
    ```

- **Multi-agenti**. AutoGen supporta la creazione di più agenti che possono lavorare insieme per raggiungere compiti complessi. Gli agenti possono comunicare, condividere informazioni e coordinare le loro azioni per risolvere i problemi in modo più efficiente. Per creare un sistema multi-agente, puoi definire diversi tipi di agenti con funzioni e ruoli specializzati, come il recupero di dati, l'analisi, il processo decisionale e l'interazione con l'utente. Vediamo come appare una tale creazione per avere un'idea:

    ```python
    editor_description = "Editor for planning and reviewing the content."

    # Example of declaring an Agent
    editor_agent_type = await EditorAgent.register(
    runtime,
    editor_topic_type,  # Using topic type as the agent type.
    lambda: EditorAgent(
        description=editor_description,
        group_chat_topic_type=group_chat_topic_type,
        model_client=OpenAIChatCompletionClient(
            model="gpt-4o-2024-08-06",
            # api_key="YOUR_API_KEY",
        ),
        ),
    )

    # remaining declarations shortened for brevity

    # Group chat
    group_chat_manager_type = await GroupChatManager.register(
    runtime,
    "group_chat_manager",
    lambda: GroupChatManager(
        participant_topic_types=[writer_topic_type, illustrator_topic_type, editor_topic_type, user_topic_type],
        model_client=OpenAIChatCompletionClient(
            model="gpt-4o-2024-08-06",
            # api_key="YOUR_API_KEY",
        ),
        participant_descriptions=[
            writer_description, 
            illustrator_description, 
            editor_description, 
            user_description
        ],
        ),
    )
    ```

    Nel codice precedente abbiamo un `GroupChatManager` che è registrato con il runtime. Questo manager è responsabile del coordinamento delle interazioni tra diversi tipi di agenti, come scrittori, illustratori, editori e utenti.

- **Runtime degli Agenti**. Il framework fornisce un ambiente di runtime, abilitando la comunicazione tra agenti, gestisce le loro identità e cicli di vita, e applica confini di sicurezza e privacy. Questo significa che puoi eseguire i tuoi agenti in un ambiente sicuro e controllato, garantendo che possano interagire in modo sicuro ed efficiente. Ci sono due runtime di interesse:
  - **Runtime autonomo**. Questa è una buona scelta per applicazioni a processo singolo in cui tutti gli agenti sono implementati nello stesso linguaggio di programmazione e eseguiti nello stesso processo. Ecco un'illustrazione di come funziona:
  
    <a href="https://microsoft.github.io/autogen/stable/_images/architecture-standalone.svg" target="_blank">Runtime autonomo</a>   
Stack applicativo

    *gli agenti comunicano tramite messaggi attraverso il runtime, e il runtime gestisce il ciclo di vita degli agenti*

  - **Runtime distribuito**, è adatto per applicazioni multi-processo in cui gli agenti possono essere implementati in diversi linguaggi di programmazione e eseguiti su macchine diverse. Ecco un'illustrazione di come funziona:
  
    <a href="https://microsoft.github.io/autogen/stable/_images/architecture-distributed.svg" target="_blank">Runtime distribuito</a>

## Semantic Kernel + Framework per Agenti

Semantic Kernel è un SDK di orchestrazione AI pronto per l'impresa. Consiste in connettori AI e di memoria, insieme a un Framework per Agenti.

Vediamo prima alcuni componenti fondamentali:

- **Connettori AI**: Questa è un'interfaccia con servizi AI esterni e fonti di dati per l'uso sia in Python che in C#.

  ```python
  # Semantic Kernel Python
  from semantic_kernel.connectors.ai.open_ai import AzureChatCompletion
  from semantic_kernel.kernel import Kernel

  kernel = Kernel()
  kernel.add_service(
    AzureChatCompletion(
        deployment_name="your-deployment-name",
        api_key="your-api-key",
        endpoint="your-endpoint",
    )
  )
  ```  

    ```csharp
    // Semantic Kernel C#
    using Microsoft.SemanticKernel;

    // Create kernel
    var builder = Kernel.CreateBuilder();
    
    // Add a chat completion service:
    builder.Services.AddAzureOpenAIChatCompletion(
        "your-resource-name",
        "your-endpoint",
        "your-resource-key",
        "deployment-model");
    var kernel = builder.Build();
    ```

    Qui hai un semplice esempio di come puoi creare un kernel e aggiungere un servizio di completamento chat. Semantic Kernel crea una connessione a un servizio AI esterno, in questo caso, Azure OpenAI Chat Completion.

- **Plugin**: Questi racchiudono funzioni che un'applicazione può utilizzare. Ci sono sia plugin già pronti che personalizzati che puoi creare. Un concetto correlato è quello delle "funzioni di prompt". Invece di fornire suggerimenti in linguaggio naturale per l'invocazione delle funzioni, trasmetti determinate funzioni al modello. Basandosi sul contesto attuale della chat, il modello può scegliere di chiamare una di queste funzioni per completare una richiesta o una query. Ecco un esempio:

  ```python
  from semantic_kernel.connectors.ai.open_ai.services.azure_chat_completion import AzureChatCompletion


  async def main():
      from semantic_kernel.functions import KernelFunctionFromPrompt
      from semantic_kernel.kernel import Kernel

      kernel = Kernel()
      kernel.add_service(AzureChatCompletion())

      user_input = input("User Input:> ")

      kernel_function = KernelFunctionFromPrompt(
          function_name="SummarizeText",
          prompt="""
          Summarize the provided unstructured text in a sentence that is easy to understand.
          Text to summarize: {{$user_input}}
          """,
      )

      response = await kernel_function.invoke(kernel=kernel, user_input=user_input)
      print(f"Model Response: {response}")

      """
      Sample Console Output:

      User Input:> I like dogs
      Model Response: The text expresses a preference for dogs.
      """


  if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
  ```

    ```csharp
    var userInput = Console.ReadLine();

    // Define semantic function inline.
    string skPrompt = @"Summarize the provided unstructured text in a sentence that is easy to understand.
                        Text to summarize: {{$userInput}}";
    
    // create the function from the prompt
    KernelFunction summarizeFunc = kernel.CreateFunctionFromPrompt(
        promptTemplate: skPrompt,
        functionName: "SummarizeText"
    );

    //then import into the current kernel
    kernel.ImportPluginFromFunctions("SemanticFunctions", [summarizeFunc]);

    ```

    Qui, hai prima un prompt template `skPrompt` che lascia spazio all'utente per inserire testo, `$userInput`. Poi crei la funzione del kernel `SummarizeText` e la importi nel kernel con il nome del plugin `SemanticFunctions`. Nota il nome della funzione che aiuta Semantic Kernel a capire cosa fa la funzione e quando dovrebbe essere chiamata.

- **Funzione nativa**: Ci sono anche funzioni native che il framework può chiamare direttamente per svolgere il compito. Ecco un esempio di una funzione che recupera il contenuto da un file:

    ```csharp
    public class NativeFunctions {

        [SKFunction, Description("Retrieve content from local file")]
        public async Task<string> RetrieveLocalFile(string fileName, int maxSize = 5000)
        {
            string content = await File.ReadAllTextAsync(fileName);
            if (content.Length <= maxSize) return content;
            return content.Substring(0, maxSize);
        }
    }
    
    //Import native function
    string plugInName = "NativeFunction";
    string functionName = "RetrieveLocalFile";

   //To add the functions to a kernel use the following function
    kernel.ImportPluginFromType<NativeFunctions>();

    ```

- **Memoria**: Astrae e semplifica la gestione del contesto per le app AI. L'idea della memoria è che questa è qualcosa che l'LLM dovrebbe conoscere. Puoi archiviare queste informazioni in un archivio vettoriale che finisce per essere un database in memoria o un database vettoriale o simile. Ecco un esempio di uno scenario molto semplificato in cui *fatti* vengono aggiunti alla memoria:

    ```csharp
    var facts = new Dictionary<string,string>();
    facts.Add(
        "Azure Machine Learning; https://learn.microsoft.com/azure/machine-learning/",
        @"Azure Machine Learning is a cloud service for accelerating and
        managing the machine learning project lifecycle. Machine learning professionals,
        data scientists, and engineers can use it in their day-to-day workflows"
    );
    
    facts.Add(
        "Azure SQL Service; https://learn.microsoft.com/azure/azure-sql/",
        @"Azure SQL is a family of managed, secure, and intelligent products
        that use the SQL Server database engine in the Azure cloud."
    );
    
    string memoryCollectionName = "SummarizedAzureDocs";
    
    foreach (var fact in facts) {
        await memoryBuilder.SaveReferenceAsync(
            collection: memoryCollectionName,
            description: fact.Key.Split(";")[1].Trim(),
            text: fact.Value,
            externalId: fact.Key.Split(";")[2].Trim(),
            externalSourceName: "Azure Documentation"
        );
    }
    ```

Questi fatti vengono poi memorizzati nella collezione di memoria `SummarizedAzureDocs`. Questo è un esempio molto semplificato, ma puoi vedere come è possibile memorizzare informazioni nella memoria per l'uso da parte del LLM.

Quindi, queste sono le basi del framework Semantic Kernel, ma che dire del framework Agent?

## Servizio Azure AI Agent

Il servizio Azure AI Agent è un'aggiunta più recente, introdotta al Microsoft Ignite 2024. Consente lo sviluppo e la distribuzione di agenti AI con modelli più flessibili, come la chiamata diretta a LLM open-source come Llama 3, Mistral e Cohere.

Azure AI Agent Service offre meccanismi di sicurezza aziendale più robusti e metodi di archiviazione dei dati, rendendolo adatto per applicazioni aziendali.

Funziona immediatamente con framework di orchestrazione multi-agente come AutoGen e Semantic Kernel.

Questo servizio è attualmente in Public Preview e supporta Python e C# per la creazione di agenti.

Utilizzando Semantic Kernel Python, possiamo creare un Azure AI Agent con un plugin definito dall'utente:

```python
import asyncio
from typing import Annotated

from azure.identity.aio import DefaultAzureCredential

from semantic_kernel.agents import AzureAIAgent, AzureAIAgentSettings, AzureAIAgentThread
from semantic_kernel.contents import ChatMessageContent
from semantic_kernel.contents import AuthorRole
from semantic_kernel.functions import kernel_function


# Define a sample plugin for the sample
class MenuPlugin:
    """A sample Menu Plugin used for the concept sample."""

    @kernel_function(description="Provides a list of specials from the menu.")
    def get_specials(self) -> Annotated[str, "Returns the specials from the menu."]:
        return """
        Special Soup: Clam Chowder
        Special Salad: Cobb Salad
        Special Drink: Chai Tea
        """

    @kernel_function(description="Provides the price of the requested menu item.")
    def get_item_price(
        self, menu_item: Annotated[str, "The name of the menu item."]
    ) -> Annotated[str, "Returns the price of the menu item."]:
        return "$9.99"


async def main() -> None:
    ai_agent_settings = AzureAIAgentSettings.create()

    async with (
        DefaultAzureCredential() as creds,
        AzureAIAgent.create_client(
            credential=creds,
            conn_str=ai_agent_settings.project_connection_string.get_secret_value(),
        ) as client,
    ):
        # Create agent definition
        agent_definition = await client.agents.create_agent(
            model=ai_agent_settings.model_deployment_name,
            name="Host",
            instructions="Answer questions about the menu.",
        )

        # Create the AzureAI Agent using the defined client and agent definition
        agent = AzureAIAgent(
            client=client,
            definition=agent_definition,
            plugins=[MenuPlugin()],
        )

        # Create a thread to hold the conversation
        # If no thread is provided, a new thread will be
        # created and returned with the initial response
        thread: AzureAIAgentThread | None = None

        user_inputs = [
            "Hello",
            "What is the special soup?",
            "How much does that cost?",
            "Thank you",
        ]

        try:
            for user_input in user_inputs:
                print(f"# User: '{user_input}'")
                # Invoke the agent for the specified thread
                response = await agent.get_response(
                    messages=user_input,
                    thread_id=thread,
                )
                print(f"# {response.name}: {response.content}")
                thread = response.thread
        finally:
            await thread.delete() if thread else None
            await client.agents.delete_agent(agent.id)


if __name__ == "__main__":
    asyncio.run(main())
```

### Concetti principali

Azure AI Agent Service ha i seguenti concetti principali:

- **Agente**. Azure AI Agent Service si integra con Azure AI Foundry. All'interno di AI Foundry, un AI Agent agisce come un microservizio "intelligente" che può essere utilizzato per rispondere a domande (RAG), eseguire azioni o automatizzare completamente i flussi di lavoro. Lo fa combinando la potenza dei modelli generativi AI con strumenti che gli consentono di accedere e interagire con fonti di dati reali. Ecco un esempio di agente:

    ```python
    agent = project_client.agents.create_agent(
        model="gpt-4o-mini",
        name="my-agent",
        instructions="You are helpful agent",
        tools=code_interpreter.definitions,
        tool_resources=code_interpreter.resources,
    )
    ```

    In questo esempio, viene creato un agente con il modello `gpt-4o-mini`, un nome `my-agent` e istruzioni `You are helpful agent`. L'agente è dotato di strumenti e risorse per eseguire compiti di interpretazione del codice.

- **Thread e messaggi**. Il thread è un altro concetto importante. Rappresenta una conversazione o interazione tra un agente e un utente. I thread possono essere utilizzati per tracciare i progressi di una conversazione, memorizzare informazioni contestuali e gestire lo stato dell'interazione. Ecco un esempio di thread:

    ```python
    thread = project_client.agents.create_thread()
    message = project_client.agents.create_message(
        thread_id=thread.id,
        role="user",
        content="Could you please create a bar chart for the operating profit using the following data and provide the file to me? Company A: $1.2 million, Company B: $2.5 million, Company C: $3.0 million, Company D: $1.8 million",
    )
    
    # Ask the agent to perform work on the thread
    run = project_client.agents.create_and_process_run(thread_id=thread.id, agent_id=agent.id)
    
    # Fetch and log all messages to see the agent's response
    messages = project_client.agents.list_messages(thread_id=thread.id)
    print(f"Messages: {messages}")
    ```

    Nel codice precedente, viene creato un thread. Successivamente, un messaggio viene inviato al thread. Chiamando `create_and_process_run`, si chiede all'agente di lavorare sul thread. Infine, i messaggi vengono recuperati e registrati per vedere la risposta dell'agente. I messaggi indicano i progressi della conversazione tra l'utente e l'agente. È anche importante capire che i messaggi possono essere di diversi tipi, come testo, immagine o file, ovvero il lavoro dell'agente ha prodotto, ad esempio, un'immagine o una risposta testuale. Come sviluppatore, puoi quindi utilizzare queste informazioni per elaborare ulteriormente la risposta o presentarla all'utente.

- **Integrazione con altri framework AI**. Azure AI Agent Service può interagire con altri framework come AutoGen e Semantic Kernel, il che significa che puoi costruire parte della tua applicazione in uno di questi framework e, ad esempio, utilizzare il servizio Agent come orchestratore oppure costruire tutto nel servizio Agent.

**Casi d'uso**: Azure AI Agent Service è progettato per applicazioni aziendali che richiedono distribuzione di agenti AI sicura, scalabile e flessibile.

## Qual è la differenza tra questi framework?

Sembra che ci sia molta sovrapposizione tra questi framework, ma ci sono alcune differenze chiave in termini di design, capacità e casi d'uso target:

- **AutoGen**: È un framework di sperimentazione focalizzato sulla ricerca all'avanguardia sui sistemi multi-agente. È il luogo ideale per sperimentare e prototipare sistemi multi-agente sofisticati.
- **Semantic Kernel**: È una libreria di agenti pronta per la produzione per costruire applicazioni agentiche aziendali. Si concentra su applicazioni agentiche distribuite e basate su eventi, abilitando più LLM e SLM, strumenti e modelli di progettazione a singolo/multi-agente.
- **Azure AI Agent Service**: È una piattaforma e un servizio di distribuzione in Azure Foundry per agenti. Offre connettività ai servizi supportati da Azure come Azure OpenAI, Azure AI Search, Bing Search ed esecuzione di codice.

Non sei ancora sicuro di quale scegliere?

### Casi d'uso

Vediamo se possiamo aiutarti esaminando alcuni casi d'uso comuni:

> D: Sto sperimentando, imparando e costruendo applicazioni agentiche proof-of-concept, e voglio poter costruire e sperimentare rapidamente
>

>R: AutoGen sarebbe una buona scelta per questo scenario, poiché si concentra su applicazioni agentiche distribuite e basate su eventi e supporta modelli avanzati di progettazione multi-agente.

> D: Cosa rende AutoGen una scelta migliore rispetto a Semantic Kernel e Azure AI Agent Service per questo caso d'uso?
>
> R: AutoGen è specificamente progettato per applicazioni agentiche distribuite e basate su eventi, rendendolo particolarmente adatto per automatizzare compiti di generazione di codice e analisi dei dati. Fornisce gli strumenti e le capacità necessarie per costruire sistemi multi-agente complessi in modo efficiente.

>D: Sembra che anche Azure AI Agent Service potrebbe funzionare qui, ha strumenti per la generazione di codice e altro?

>
> R: Sì, Azure AI Agent Service è un servizio di piattaforma per agenti e aggiunge funzionalità integrate per modelli multipli, Azure AI Search, Bing Search e Azure Functions. Rende facile costruire i tuoi agenti nel Foundry Portal e distribuirli su larga scala.

> D: Sono ancora confuso, dammi solo un'opzione
>
> R: Una scelta eccellente è costruire la tua applicazione in Semantic Kernel prima e poi utilizzare Azure AI Agent Service per distribuire il tuo agente. Questo approccio ti consente di mantenere facilmente i tuoi agenti sfruttando al contempo la potenza di costruire sistemi multi-agente in Semantic Kernel. Inoltre, Semantic Kernel ha un connettore in AutoGen, rendendo facile utilizzare entrambi i framework insieme.

Riassumiamo le differenze chiave in una tabella:

| Framework | Focus | Concetti principali | Casi d'uso |
| --- | --- | --- | --- |
| AutoGen | Applicazioni agentiche distribuite e basate su eventi | Agenti, Personas, Funzioni, Dati | Generazione di codice, compiti di analisi dei dati |
| Semantic Kernel | Comprensione e generazione di contenuti simili al linguaggio umano | Agenti, Componenti modulari, Collaborazione | Comprensione del linguaggio naturale, generazione di contenuti |
| Azure AI Agent Service | Modelli flessibili, sicurezza aziendale, Generazione di codice, Chiamata di strumenti | Modularità, Collaborazione, Orchestrazione dei processi | Distribuzione di agenti AI sicura, scalabile e flessibile |

Qual è il caso d'uso ideale per ciascuno di questi framework?

## Posso integrare direttamente i miei strumenti dell'ecosistema Azure esistenti o ho bisogno di soluzioni autonome?

La risposta è sì, puoi integrare direttamente i tuoi strumenti dell'ecosistema Azure esistenti con Azure AI Agent Service, soprattutto perché è stato progettato per funzionare senza problemi con altri servizi Azure. Potresti, ad esempio, integrare Bing, Azure AI Search e Azure Functions. C'è anche un'integrazione profonda con Azure AI Foundry.

Per AutoGen e Semantic Kernel, puoi anche integrare con i servizi Azure, ma potrebbe essere necessario chiamare i servizi Azure dal tuo codice. Un altro modo per integrare è utilizzare gli SDK Azure per interagire con i servizi Azure dai tuoi agenti. Inoltre, come menzionato, puoi utilizzare Azure AI Agent Service come orchestratore per i tuoi agenti costruiti in AutoGen o Semantic Kernel, il che darebbe un facile accesso all'ecosistema Azure.

## Codici di esempio

- Python: [Agent Framework](./code_samples/02-python-agent-framework.ipynb)
- .NET: [Agent Framework](./code_samples/02-dotnet-agent-framework.md)

## Hai altre domande sui framework AI Agent?

Unisciti al [Discord di Azure AI Foundry](https://aka.ms/ai-agents/discord) per incontrare altri studenti, partecipare agli orari d'ufficio e ottenere risposte alle tue domande sugli AI Agent.

## Riferimenti

- <a href="https://techcommunity.microsoft.com/blog/azure-ai-services-blog/introducing-azure-ai-agent-service/4298357" target="_blank">Azure Agent Service</a>
- <a href="https://devblogs.microsoft.com/semantic-kernel/microsofts-agentic-ai-frameworks-autogen-and-semantic-kernel/" target="_blank">Semantic Kernel e AutoGen</a>
- <a href="https://learn.microsoft.com/semantic-kernel/frameworks/agent/?pivots=programming-language-python" target="_blank">Semantic Kernel Python Agent Framework</a>
- <a href="https://learn.microsoft.com/semantic-kernel/frameworks/agent/?pivots=programming-language-csharp" target="_blank">Semantic Kernel .Net Agent Framework</a>
- <a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Azure AI Agent service</a>
- <a href="https://techcommunity.microsoft.com/blog/educatordeveloperblog/using-azure-ai-agent-service-with-autogen--semantic-kernel-to-build-a-multi-agen/4363121" target="_blank">Utilizzo di Azure AI Agent Service con AutoGen / Semantic Kernel per costruire una soluzione multi-agente</a>

## Lezione precedente

[Introduzione agli AI Agent e ai casi d'uso degli agenti](../01-intro-to-ai-agents/README.md)

## Prossima lezione

[Comprendere i modelli di progettazione agentica](../03-agentic-design-patterns/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer (Avvertenza)**:  
Questo documento è stato tradotto utilizzando il servizio di traduzione automatica [Co-op Translator](https://github.com/Azure/co-op-translator). Sebbene ci impegniamo per garantire l'accuratezza, si prega di notare che le traduzioni automatiche possono contenere errori o imprecisioni. Il documento originale nella sua lingua nativa dovrebbe essere considerato la fonte autorevole. Per informazioni critiche, si raccomanda una traduzione professionale umana. Non siamo responsabili per eventuali incomprensioni o interpretazioni errate derivanti dall'uso di questa traduzione.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->