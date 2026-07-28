[![Esplorare i Framework degli Agenti AI](../../../translated_images/it/lesson-2-thumbnail.c65f44c93b8558df.webp)](https://youtu.be/ODwF-EZo_O8?si=1xoy_B9RNQfrYdF7)

> _(Clicca sull'immagine sopra per vedere il video di questa lezione)_

# Esplora i Framework degli Agenti AI

I framework per agenti AI sono piattaforme software progettate per semplificare la creazione, il deployment e la gestione degli agenti AI. Questi framework forniscono agli sviluppatori componenti predefiniti, astrazioni e strumenti che facilitano lo sviluppo di sistemi AI complessi.

Tali framework aiutano gli sviluppatori a concentrarsi sugli aspetti unici delle loro applicazioni fornendo approcci standardizzati alle sfide comuni nello sviluppo degli agenti AI. Migliorano la scalabilità, l'accessibilità e l'efficienza nella costruzione di sistemi AI.

## Introduzione 

Questa lezione tratterà:

- Cosa sono i Framework per Agenti AI e cosa consentono agli sviluppatori di ottenere?
- Come le squadre possono usarli per prototipare rapidamente, iterare e migliorare le capacità dei loro agenti?
- Quali sono le differenze tra i framework e gli strumenti creati da Microsoft (<a href="https://aka.ms/ai-agents-beginners/ai-agent-service" target="_blank">Microsoft Foundry Agent Service</a> e il <a href="https://learn.microsoft.com/azure/ai-services/openai/how-to/responses" target="_blank">Microsoft Agent Framework</a>)?
- Posso integrare direttamente i miei strumenti dell’ecosistema Azure esistente, o ho bisogno di soluzioni standalone?
- Cos’è Microsoft Foundry Agent Service e come mi può aiutare?

## Obiettivi di apprendimento

Gli obiettivi di questa lezione sono aiutarti a comprendere:

- Il ruolo dei Framework per Agenti AI nello sviluppo AI.
- Come sfruttare i Framework per Agenti AI per costruire agenti intelligenti.
- Le capacità chiave abilitate dai Framework per Agenti AI.
- Le differenze tra Microsoft Agent Framework e Microsoft Foundry Agent Service.

## Cosa sono i Framework per Agenti AI e cosa consentono agli sviluppatori di fare?

I Framework AI tradizionali possono aiutarti a integrare l’AI nelle tue app e migliorare queste app nei seguenti modi:

- **Personalizzazione**: l’AI può analizzare il comportamento e le preferenze degli utenti per fornire raccomandazioni, contenuti ed esperienze personalizzate.
Esempio: i servizi di streaming come Netflix usano l’AI per suggerire film e programmi in base alla cronologia di visione, migliorando il coinvolgimento e la soddisfazione dell’utente.
- **Automazione ed efficienza**: l’AI può automatizzare compiti ripetitivi, snellire i flussi di lavoro e migliorare l’efficienza operativa.
Esempio: le app per il servizio clienti usano chatbot alimentati da AI per gestire richieste comuni, riducendo i tempi di risposta e liberando agenti umani per questioni più complesse.
- **Esperienza utente migliorata**: l’AI può migliorare l’esperienza utente complessiva fornendo funzionalità intelligenti come riconoscimento vocale, elaborazione del linguaggio naturale e testo predittivo.
Esempio: assistenti virtuali come Siri e Google Assistant usano l’AI per capire e rispondere ai comandi vocali, facilitando l’interazione degli utenti con i loro dispositivi.

### Tutto ottimo, vero? Allora perché abbiamo bisogno del Framework per Agenti AI?

I Framework per Agenti AI rappresentano qualcosa in più dei semplici framework AI. Sono progettati per consentire la creazione di agenti intelligenti che possono interagire con gli utenti, altri agenti e l’ambiente per raggiungere obiettivi specifici. Questi agenti possono mostrare comportamenti autonomi, prendere decisioni e adattarsi a condizioni mutevoli. Vediamo alcune capacità chiave abilitate dai Framework per Agenti AI:

- **Collaborazione e coordinamento tra agenti**: permette la creazione di più agenti AI che possono lavorare insieme, comunicare e coordinarsi per risolvere compiti complessi.
- **Automazione e gestione dei compiti**: fornisce meccanismi per automatizzare flussi di lavoro a più fasi, delega di compiti e gestione dinamica tra agenti.
- **Comprensione contestuale e adattamento**: dota gli agenti della capacità di comprendere il contesto, adattarsi a ambienti mutevoli e prendere decisioni basate su informazioni in tempo reale.

In sintesi, gli agenti ti permettono di fare di più, portare l’automazione a un livello superiore, creare sistemi più intelligenti che si adattano e apprendono dall’ambiente.

## Come prototipare rapidamente, iterare e migliorare le capacità dell’agente?

Questo è un campo in rapido movimento, ma ci sono cose comuni alla maggior parte dei Framework per Agenti AI che possono aiutarti a prototipare e iterare rapidamente, cioè componenti modulari, strumenti collaborativi e apprendimento in tempo reale. Esploriamoli:

- **Usa componenti modulari**: gli SDK AI offrono componenti predefiniti come connettori AI e di memoria, chiamate a funzioni tramite linguaggio naturale o plugin di codice, modelli di prompt e altro.
- **Sfrutta strumenti collaborativi**: progetta agenti con ruoli e compiti specifici, permettendo loro di testare e affinare flussi di lavoro collaborativi.
- **Impara in tempo reale**: implementa loop di feedback in cui gli agenti apprendono dalle interazioni e regolano dinamicamente il loro comportamento.

### Usa componenti modulari

SDK come il Microsoft Agent Framework offrono componenti predefiniti come connettori AI, definizioni di strumenti e gestione agenti.

**Come le squadre possono usarli**: le squadre possono assemblare rapidamente questi componenti per creare un prototipo funzionante senza partire da zero, permettendo una rapida sperimentazione e iterazione.

**Come funziona nella pratica**: puoi usare un parser predefinito per estrarre informazioni dall’input utente, un modulo di memoria per archiviare e recuperare dati, e un generatore di prompt per interagire con gli utenti, tutto senza costruire questi componenti da zero.

**Esempio di codice**. Vediamo un esempio di come usare il Microsoft Agent Framework con `FoundryChatClient` per far rispondere il modello all’input utente con chiamate a strumenti:

``` python
# Esempio di Microsoft Agent Framework in Python

import asyncio
import os

from agent_framework import tool
from agent_framework.foundry import FoundryChatClient
from azure.identity import AzureCliCredential


# Definisci una funzione di esempio per prenotare un viaggio
@tool(approval_mode="never_require")
def book_flight(date: str, location: str) -> str:
    """Book travel given location and date."""
    return f"Travel was booked to {location} on {date}"


async def main():
    provider = FoundryChatClient(
        project_endpoint=os.environ["AZURE_AI_PROJECT_ENDPOINT"],
        model=os.environ["AZURE_AI_MODEL_DEPLOYMENT_NAME"],
        credential=AzureCliCredential(),
    )
    agent = provider.as_agent(
        name="travel_agent",
        instructions="Help the user book travel. Use the book_flight tool when ready.",
        tools=[book_flight],
    )

    response = await agent.run("I'd like to go to New York on January 1, 2025")
    print(response)
    # Esempio di output: Il tuo volo per New York del 1° gennaio 2025 è stato prenotato con successo. Buon viaggio! ✈️🗽


if __name__ == "__main__":
    asyncio.run(main())
```

Ciò che puoi vedere da questo esempio è come utilizzare un parser predefinito per estrarre informazioni chiave dall’input utente, come origine, destinazione e data di una richiesta di prenotazione volo. Questo approccio modulare ti permette di concentrarti sulla logica di alto livello.

### Sfrutta strumenti collaborativi

Framework come il Microsoft Agent Framework facilitano la creazione di più agenti che possono lavorare insieme.

**Come le squadre possono usarli**: le squadre possono progettare agenti con ruoli e compiti specifici, permettendo loro di testare e affinare flussi di lavoro collaborativi e migliorare l’efficienza complessiva del sistema.

**Come funziona nella pratica**: puoi creare un team di agenti dove ogni agente ha una funzione specializzata, come recupero dati, analisi o presa di decisioni. Questi agenti possono comunicare e condividere informazioni per raggiungere un obiettivo comune, come rispondere a una domanda dell’utente o completare un compito.

**Esempio di codice (Microsoft Agent Framework)**:

```python
# Creazione di più agenti che lavorano insieme utilizzando il Microsoft Agent Framework

import os
from agent_framework.foundry import FoundryChatClient
from azure.identity import AzureCliCredential

provider = FoundryChatClient(
    project_endpoint=os.environ["AZURE_AI_PROJECT_ENDPOINT"],
    model=os.environ["AZURE_AI_MODEL_DEPLOYMENT_NAME"],
    credential=AzureCliCredential(),
)

# Agente di Recupero Dati
agent_retrieve = provider.as_agent(
    name="dataretrieval",
    instructions="Retrieve relevant data using available tools.",
    tools=[retrieve_tool],
)

# Agente di Analisi Dati
agent_analyze = provider.as_agent(
    name="dataanalysis",
    instructions="Analyze the retrieved data and provide insights.",
    tools=[analyze_tool],
)

# Eseguire gli agenti in sequenza su un compito
retrieval_result = await agent_retrieve.run("Retrieve sales data for Q4")
analysis_result = await agent_analyze.run(f"Analyze this data: {retrieval_result}")
print(analysis_result)
```

Nel codice precedente vedi come creare un compito che coinvolge più agenti che collaborano per analizzare dati. Ogni agente svolge una funzione specifica, e il compito è eseguito coordinando gli agenti per raggiungere il risultato desiderato. Creando agenti dedicati con ruoli specializzati puoi migliorare l’efficienza e le prestazioni del compito.

### Impara in tempo reale

Framework avanzati forniscono capacità di comprensione contestuale e adattamento in tempo reale.

**Come le squadre possono usarli**: le squadre possono implementare loop di feedback in cui gli agenti apprendono dalle interazioni e regolano dinamicamente il loro comportamento, portando a un miglioramento e a un affinamento continui delle capacità.

**Come funziona nella pratica**: gli agenti possono analizzare feedback degli utenti, dati ambientali e risultati dei compiti per aggiornare la base di conoscenza, adattare algoritmi decisionali e migliorare le prestazioni nel tempo. Questo processo di apprendimento iterativo permette agli agenti di adattarsi a condizioni mutevoli e preferenze utente, migliorando l’efficacia complessiva del sistema.

## Quali sono le differenze tra Microsoft Agent Framework e Microsoft Foundry Agent Service?

Ci sono molti modi per confrontare questi approcci, ma vediamo alcune differenze chiave in termini di design, capacità e casi d’uso target:

## Microsoft Agent Framework (MAF)

Il Microsoft Agent Framework fornisce un SDK semplificato per costruire agenti AI usando `FoundryChatClient`. Permette agli sviluppatori di creare agenti che sfruttano i modelli Azure OpenAI con chiamate a strumenti integrate, gestione delle conversazioni e sicurezza di livello enterprise tramite l’identità Azure.

**Casi d’uso**: costruire agenti AI pronti per la produzione con uso di strumenti, flussi di lavoro multi-step e scenari di integrazione enterprise.

Ecco alcuni concetti fondamentali del Microsoft Agent Framework:

- **Agenti**. Un agente è creato via `FoundryChatClient` e configurato con nome, istruzioni e strumenti. L’agente può:
  - **Processare messaggi utente** e generare risposte usando i modelli Azure OpenAI.
  - **Chiamare strumenti** automaticamente basandosi sul contesto della conversazione.
  - **Mantenere lo stato della conversazione** attraverso molteplici interazioni.

  Ecco un frammento di codice che mostra come creare un agente:

    ```python
    import os
    from agent_framework.foundry import FoundryChatClient
    from azure.identity import AzureCliCredential

    provider = FoundryChatClient(
        project_endpoint=os.environ["AZURE_AI_PROJECT_ENDPOINT"],
        model=os.environ["AZURE_AI_MODEL_DEPLOYMENT_NAME"],
        credential=AzureCliCredential(),
    )
    agent = provider.as_agent(
        name="my_agent",
        instructions="You are a helpful assistant.",
    )

    response = await agent.run("Hello, World!")
    print(response)
    ```

- **Strumenti**. Il framework supporta la definizione di strumenti come funzioni Python che l’agente può invocare automaticamente. Gli strumenti sono registrati durante la creazione dell’agente:

    ```python
    def get_weather(location: str) -> str:
        """Get the current weather for a location."""
        return f"The weather in {location} is sunny, 72\u00b0F."

    agent = provider.as_agent(
        name="weather_agent",
        instructions="Help users check the weather.",
        tools=[get_weather],
    )
    ```

- **Coordinamento multi-agente**. Puoi creare più agenti con specializzazioni diverse e coordinare il loro lavoro:

    ```python
    planner = provider.as_agent(
        name="planner",
        instructions="Break down complex tasks into steps.",
    )

    executor = provider.as_agent(
        name="executor",
        instructions="Execute the planned steps using available tools.",
        tools=[execute_tool],
    )

    plan = await planner.run("Plan a trip to Paris")
    result = await executor.run(f"Execute this plan: {plan}")
    ```

- **Integrazione dell’identità Azure**. Il framework usa `AzureCliCredential` (o `DefaultAzureCredential`) per un’autenticazione sicura senza chiavi, eliminando la gestione diretta delle chiavi API.

## Microsoft Foundry Agent Service

Microsoft Foundry Agent Service è un’aggiunta più recente, presentata a Microsoft Ignite 2024. Permette lo sviluppo e il deployment di agenti AI con modelli più flessibili, come chiamate dirette a LLM open source come Llama 3, Mistral e Cohere.

Microsoft Foundry Agent Service fornisce meccanismi di sicurezza enterprise più robusti e metodi di archiviazione dati, rendendolo adatto ad applicazioni enterprise. 

Funziona “out-of-the-box” con il Microsoft Agent Framework per costruire e distribuire agenti.

Questo servizio è attualmente in anteprima pubblica e supporta Python e C# per la costruzione degli agenti.

Usando l’SDK Python di Microsoft Foundry Agent Service, possiamo creare un agente con uno strumento definito dall’utente:

```python
import asyncio
from azure.identity import DefaultAzureCredential
from azure.ai.projects import AIProjectClient

# Definire le funzioni degli strumenti
def get_specials() -> str:
    """Provides a list of specials from the menu."""
    return """
    Special Soup: Clam Chowder
    Special Salad: Cobb Salad
    Special Drink: Chai Tea
    """

def get_item_price(menu_item: str) -> str:
    """Provides the price of the requested menu item."""
    return "$9.99"


async def main() -> None:
    credential = DefaultAzureCredential()
    project_client = AIProjectClient.from_connection_string(
        credential=credential,
        conn_str="your-connection-string",
    )

    agent = project_client.agents.create_agent(
        model="gpt-5-mini",
        name="Host",
        instructions="Answer questions about the menu.",
        tools=[get_specials, get_item_price],
    )

    thread = project_client.agents.create_thread()

    user_inputs = [
        "Hello",
        "What is the special soup?",
        "How much does that cost?",
        "Thank you",
    ]

    for user_input in user_inputs:
        print(f"# User: '{user_input}'")
        message = project_client.agents.create_message(
            thread_id=thread.id,
            role="user",
            content=user_input,
        )
        run = project_client.agents.create_and_process_run(
            thread_id=thread.id, agent_id=agent.id
        )
        messages = project_client.agents.list_messages(thread_id=thread.id)
        print(f"# Agent: {messages.data[0].content[0].text.value}")


if __name__ == "__main__":
    asyncio.run(main())
```

### Concetti fondamentali

Microsoft Foundry Agent Service ha i seguenti concetti fondamentali:

- **Agente**. Microsoft Foundry Agent Service si integra con Microsoft Foundry. All’interno di Microsoft Foundry, un Agente AI agisce come un microservizio “intelligente” che può essere usato per rispondere a domande (RAG), eseguire azioni o automatizzare completamente flussi di lavoro. Ciò avviene combinando la potenza dei modelli generativi AI con strumenti che gli permettono di accedere e interagire con dati del mondo reale. Ecco un esempio di un agente:

    ```python
    agent = project_client.agents.create_agent(
        model="gpt-5-mini",
        name="my-agent",
        instructions="You are helpful agent",
        tools=code_interpreter.definitions,
        tool_resources=code_interpreter.resources,
    )
    ```

    In questo esempio, un agente è creato con il modello `gpt-5-mini`, un nome `my-agent`, e istruzioni `You are helpful agent`. L’agente è dotato di strumenti e risorse per svolgere attività di interpretazione del codice.

- **Thread e messaggi**. Il thread è un altro concetto importante. Rappresenta una conversazione o interazione tra un agente e un utente. I thread possono essere usati per tracciare il progresso della conversazione, memorizzare informazioni contestuali e gestire lo stato dell’interazione. Ecco un esempio di un thread:

    ```python
    thread = project_client.agents.create_thread()
    message = project_client.agents.create_message(
        thread_id=thread.id,
        role="user",
        content="Could you please create a bar chart for the operating profit using the following data and provide the file to me? Company A: $1.2 million, Company B: $2.5 million, Company C: $3.0 million, Company D: $1.8 million",
    )
    
    # Chiedi all'agente di eseguire il lavoro sul thread
    run = project_client.agents.create_and_process_run(thread_id=thread.id, agent_id=agent.id)
    
    # Recupera e registra tutti i messaggi per vedere la risposta dell'agente
    messages = project_client.agents.list_messages(thread_id=thread.id)
    print(f"Messages: {messages}")
    ```

    Nel codice precedente, viene creato un thread. Successivamente viene inviato un messaggio al thread. Chiamando `create_and_process_run`, si chiede all’agente di eseguire un lavoro sul thread. Infine, vengono recuperati e registrati i messaggi per vedere la risposta dell’agente. I messaggi indicano il progresso della conversazione tra utente e agente. È anche importante capire che i messaggi possono essere di tipi diversi come testo, immagine o file, cioè il lavoro degli agenti ha prodotto ad esempio un’immagine o una risposta testuale. Come sviluppatore, puoi quindi usare queste informazioni per elaborare ulteriormente la risposta o presentarla all’utente.

- **Si integra con il Microsoft Agent Framework**. Microsoft Foundry Agent Service funziona perfettamente con il Microsoft Agent Framework, il che significa che puoi costruire agenti usando `FoundryChatClient` e distribuirli tramite il servizio Agent per scenari di produzione.

**Casi d’uso**: Microsoft Foundry Agent Service è progettato per applicazioni enterprise che richiedono deployment di agenti AI sicuri, scalabili e flessibili.

## Qual è la differenza tra questi approcci?
 
Sembra ci sia sovrapposizione, ma ci sono alcune differenze chiave in termini di design, capacità e casi d’uso target:
 
- **Microsoft Agent Framework (MAF)**: è un SDK pronto per la produzione per costruire agenti AI. Fornisce una API semplificata per creare agenti con chiamate a strumenti, gestione delle conversazioni e integrazione con l’identità Azure.
- **Microsoft Foundry Agent Service**: è una piattaforma e servizio di deployment in Microsoft Foundry per agenti. Offre connettività integrata a servizi come Azure OpenAI, Azure AI Search, Bing Search ed esecuzione di codice.
 
Ancora indeciso su quale scegliere?

### Casi d’uso
 
Vediamo se possiamo aiutarti passando attraverso alcuni casi d’uso comuni:
 
> D: Sto costruendo applicazioni di agenti AI per la produzione e voglio partire velocemente
>

>R: Il Microsoft Agent Framework è una scelta eccellente. Fornisce una API semplice e pythonica tramite `FoundryChatClient` che ti permette di definire agenti con strumenti e istruzioni in poche righe di codice.

>D: Ho bisogno di deployment enterprise con integrazioni Azure come Search ed esecuzione di codice
>
> R: Microsoft Foundry Agent Service è la soluzione migliore. È un servizio piattaforma che offre funzionalità integrate per più modelli, Azure AI Search, Bing Search e Azure Functions. Permette di costruire agenti nel Foundry Portal e distribuirli su larga scala.
 
> D: Sono ancora confuso, dammi solo un’opzione
>
> R: Parti con il Microsoft Agent Framework per costruire i tuoi agenti, e poi usa Microsoft Foundry Agent Service quando devi distribuirli e scalarli in produzione. Questo approccio ti permette di iterare velocemente sulla logica degli agenti e avere una strada chiara per il deployment enterprise.
 
Riassumiamo le differenze chiave in una tabella:

| Framework | Focus | Concetti Fondamentali | Casi d’uso |
| --- | --- | --- | --- |
| Microsoft Agent Framework | SDK agente semplificato con chiamate a strumenti | Agenti, Strumenti, Identità Azure | Costruzione agenti AI, uso strumenti, flussi multi-step |
| Microsoft Foundry Agent Service | Modelli flessibili, sicurezza enterprise, generazione codice, chiamate a strumenti | Modularità, Collaborazione, Orchestrazione processi | Deployment di agenti AI sicuro, scalabile e flessibile |

## Posso integrare direttamente i miei strumenti dell’ecosistema Azure esistente o ho bisogno di soluzioni standalone?


La risposta è sì, puoi integrare i tuoi strumenti esistenti dell'ecosistema Azure direttamente con Microsoft Foundry Agent Service soprattutto, dato che è stato progettato per funzionare senza problemi con altri servizi Azure. Potresti ad esempio integrare Bing, Azure AI Search e Azure Functions. C'è anche una profonda integrazione con Microsoft Foundry.

Il Microsoft Agent Framework si integra anche con i servizi Azure tramite `FoundryChatClient` e l'identità Azure, permettendoti di chiamare i servizi Azure direttamente dai tuoi strumenti agent.

## Codici di esempio

- Python: [Agent Framework (Microsoft Foundry)](./code_samples/02-python-agent-framework.ipynb)
- Python: [Agent Framework (Azure OpenAI Responses API)](./code_samples/02-python-agent-framework-azure-openai.ipynb)
- .NET: [Agent Framework](./code_samples/02-dotnet-agent-framework.md)

## Hai altre domande sui framework per agenti AI?

Unisciti al [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D) per incontrare altri studenti, partecipare alle office hours e ottenere risposte alle tue domande sugli agenti AI.

## Riferimenti

- <a href="https://techcommunity.microsoft.com/blog/azure-ai-services-blog/introducing-azure-ai-agent-service/4298357" target="_blank">Azure Agent Service</a>
- <a href="https://learn.microsoft.com/azure/ai-services/openai/how-to/responses" target="_blank">Microsoft Agent Framework - Risposte Azure OpenAI</a>
- <a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Microsoft Foundry Agent Service</a>

## Lezione precedente

[Introduzione agli agenti AI e casi d'uso degli agenti](../01-intro-to-ai-agents/README.md)

## Lezione successiva

[Comprendere i pattern di design agentico](../03-agentic-design-patterns/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:
Questo documento è stato tradotto utilizzando il servizio di traduzione AI [Co-op Translator](https://github.com/Azure/co-op-translator). Sebbene ci impegniamo per garantire la precisione, si prega di notare che le traduzioni automatizzate possono contenere errori o imprecisioni. Il documento originale nella sua lingua nativa deve essere considerato la fonte autorevole. Per informazioni critiche, si raccomanda una traduzione professionale effettuata da un essere umano. Non siamo responsabili per eventuali malintesi o interpretazioni errate derivanti dall’uso di questa traduzione.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->