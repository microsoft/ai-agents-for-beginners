<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "7120197753abacc827b64ac2d5d6966f",
  "translation_date": "2025-11-13T10:54:57+00:00",
  "source_file": "02-explore-agentic-frameworks/README.md",
  "language_code": "de"
}
-->
[![Erforschung von AI-Agenten-Frameworks](../../../translated_images/lesson-2-thumbnail.c65f44c93b8558df4d5d407e29970e654629e614f357444a9c27c80feb54c79d.de.png)](https://youtu.be/ODwF-EZo_O8?si=1xoy_B9RNQfrYdF7)

> _(Klicken Sie auf das obige Bild, um das Video zu dieser Lektion anzusehen)_

# Erforsche AI-Agenten-Frameworks

AI-Agenten-Frameworks sind Softwareplattformen, die entwickelt wurden, um die Erstellung, Bereitstellung und Verwaltung von AI-Agenten zu vereinfachen. Diese Frameworks bieten Entwicklern vorgefertigte Komponenten, Abstraktionen und Tools, die die Entwicklung komplexer AI-Systeme erleichtern.

Diese Frameworks helfen Entwicklern, sich auf die einzigartigen Aspekte ihrer Anwendungen zu konzentrieren, indem sie standardisierte Ansätze für häufige Herausforderungen in der Entwicklung von AI-Agenten bereitstellen. Sie verbessern die Skalierbarkeit, Zugänglichkeit und Effizienz beim Aufbau von AI-Systemen.

## Einführung

Diese Lektion behandelt:

- Was sind AI-Agenten-Frameworks und was ermöglichen sie Entwicklern?
- Wie können Teams diese nutzen, um schnell Prototypen zu erstellen, zu iterieren und die Fähigkeiten ihrer Agenten zu verbessern?
- Was sind die Unterschiede zwischen den Frameworks und Tools, die von Microsoft <a href="https://aka.ms/ai-agents/autogen" target="_blank">AutoGen</a>, <a href="https://aka.ms/ai-agents-beginners/semantic-kernel" target="_blank">Semantic Kernel</a> und <a href="https://aka.ms/ai-agents-beginners/ai-agent-service" target="_blank">Azure AI Agent Service</a> entwickelt wurden?
- Kann ich meine bestehenden Azure-Ökosystem-Tools direkt integrieren, oder benötige ich eigenständige Lösungen?
- Was ist der Azure AI Agents Service und wie hilft er mir?

## Lernziele

Die Ziele dieser Lektion sind:

- Die Rolle von AI-Agenten-Frameworks in der AI-Entwicklung zu verstehen.
- Wie man AI-Agenten-Frameworks nutzt, um intelligente Agenten zu erstellen.
- Wichtige Fähigkeiten, die durch AI-Agenten-Frameworks ermöglicht werden.
- Die Unterschiede zwischen AutoGen, Semantic Kernel und Azure AI Agent Service zu erkennen.

## Was sind AI-Agenten-Frameworks und was ermöglichen sie Entwicklern?

Traditionelle AI-Frameworks können Ihnen helfen, AI in Ihre Apps zu integrieren und diese Apps auf folgende Weise zu verbessern:

- **Personalisierung**: AI kann das Nutzerverhalten und die Vorlieben analysieren, um personalisierte Empfehlungen, Inhalte und Erlebnisse bereitzustellen.  
Beispiel: Streaming-Dienste wie Netflix nutzen AI, um Filme und Serien basierend auf der Sehgewohnheiten vorzuschlagen, was die Nutzerbindung und Zufriedenheit erhöht.
- **Automatisierung und Effizienz**: AI kann repetitive Aufgaben automatisieren, Arbeitsabläufe optimieren und die betriebliche Effizienz steigern.  
Beispiel: Kundenservice-Apps nutzen AI-gestützte Chatbots, um häufige Anfragen zu bearbeiten, die Reaktionszeiten zu verkürzen und menschliche Agenten für komplexere Probleme freizustellen.
- **Verbesserte Nutzererfahrung**: AI kann die allgemeine Nutzererfahrung durch intelligente Funktionen wie Spracherkennung, Verarbeitung natürlicher Sprache und prädiktiven Text verbessern.  
Beispiel: Virtuelle Assistenten wie Siri und Google Assistant nutzen AI, um Sprachbefehle zu verstehen und darauf zu reagieren, was die Interaktion der Nutzer mit ihren Geräten erleichtert.

### Das klingt alles großartig, aber warum brauchen wir dann AI-Agenten-Frameworks?

AI-Agenten-Frameworks gehen über traditionelle AI-Frameworks hinaus. Sie sind darauf ausgelegt, die Erstellung intelligenter Agenten zu ermöglichen, die mit Nutzern, anderen Agenten und der Umgebung interagieren können, um spezifische Ziele zu erreichen. Diese Agenten können autonomes Verhalten zeigen, Entscheidungen treffen und sich an veränderte Bedingungen anpassen. Schauen wir uns einige der wichtigsten Fähigkeiten an, die durch AI-Agenten-Frameworks ermöglicht werden:

- **Agenten-Kollaboration und -Koordination**: Ermöglicht die Erstellung mehrerer AI-Agenten, die zusammenarbeiten, kommunizieren und koordinieren können, um komplexe Aufgaben zu lösen.
- **Automatisierung und Verwaltung von Aufgaben**: Bietet Mechanismen zur Automatisierung mehrstufiger Arbeitsabläufe, Aufgabenverteilung und dynamischen Aufgabenverwaltung zwischen Agenten.
- **Kontextuelles Verständnis und Anpassung**: Rüstet Agenten mit der Fähigkeit aus, Kontext zu verstehen, sich an veränderte Umgebungen anzupassen und Entscheidungen basierend auf Echtzeitinformationen zu treffen.

Zusammenfassend ermöglichen Agenten, mehr zu erreichen, die Automatisierung auf die nächste Stufe zu heben und intelligentere Systeme zu schaffen, die sich an ihre Umgebung anpassen und aus ihr lernen können.

## Wie kann man die Fähigkeiten eines Agenten schnell prototypisieren, iterieren und verbessern?

Dies ist ein sich schnell entwickelndes Feld, aber es gibt einige gemeinsame Elemente in den meisten AI-Agenten-Frameworks, die Ihnen helfen können, schnell Prototypen zu erstellen und zu iterieren, nämlich modulare Komponenten, kollaborative Tools und Echtzeitlernen. Schauen wir uns diese genauer an:

- **Verwendung modularer Komponenten**: AI-SDKs bieten vorgefertigte Komponenten wie AI- und Memory-Connectoren, Funktionsaufrufe mit natürlicher Sprache oder Code-Plugins, Prompt-Vorlagen und mehr.
- **Nutzung kollaborativer Tools**: Entwerfen Sie Agenten mit spezifischen Rollen und Aufgaben, um kollaborative Arbeitsabläufe zu testen und zu verfeinern.
- **Lernen in Echtzeit**: Implementieren Sie Feedback-Schleifen, bei denen Agenten aus Interaktionen lernen und ihr Verhalten dynamisch anpassen.

### Verwendung modularer Komponenten

SDKs wie Microsoft Semantic Kernel und LangChain bieten vorgefertigte Komponenten wie AI-Connectoren, Prompt-Vorlagen und Speicherverwaltung.

**Wie Teams diese nutzen können**: Teams können diese Komponenten schnell zusammenstellen, um einen funktionalen Prototyp zu erstellen, ohne von Grund auf neu beginnen zu müssen, was schnelles Experimentieren und Iterieren ermöglicht.

**Wie es in der Praxis funktioniert**: Sie können einen vorgefertigten Parser verwenden, um Informationen aus Benutzereingaben zu extrahieren, ein Speichermodul, um Daten zu speichern und abzurufen, und einen Prompt-Generator, um mit Benutzern zu interagieren – alles, ohne diese Komponenten selbst erstellen zu müssen.

**Beispielcode**. Schauen wir uns Beispiele an, wie Sie einen vorgefertigten AI-Connector mit Semantic Kernel Python und .Net verwenden können, der automatische Funktionsaufrufe nutzt, um auf Benutzereingaben zu reagieren:

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
  
Was Sie in diesem Beispiel sehen, ist, wie Sie einen vorgefertigten Parser nutzen können, um wichtige Informationen aus Benutzereingaben zu extrahieren, wie z. B. den Ursprung, das Ziel und das Datum einer Flugbuchungsanfrage. Dieser modulare Ansatz ermöglicht es Ihnen, sich auf die übergeordnete Logik zu konzentrieren.

### Nutzung kollaborativer Tools

Frameworks wie CrewAI, Microsoft AutoGen und Semantic Kernel erleichtern die Erstellung mehrerer Agenten, die zusammenarbeiten können.

**Wie Teams diese nutzen können**: Teams können Agenten mit spezifischen Rollen und Aufgaben entwerfen, um kollaborative Arbeitsabläufe zu testen und zu verfeinern und die Gesamteffizienz des Systems zu verbessern.

**Wie es in der Praxis funktioniert**: Sie können ein Team von Agenten erstellen, bei dem jeder Agent eine spezialisierte Funktion hat, wie z. B. Datenabruf, Analyse oder Entscheidungsfindung. Diese Agenten können kommunizieren und Informationen austauschen, um ein gemeinsames Ziel zu erreichen, wie z. B. eine Benutzeranfrage zu beantworten oder eine Aufgabe zu erledigen.

**Beispielcode (AutoGen)**:

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
  
Was Sie im vorherigen Code sehen, ist, wie Sie eine Aufgabe erstellen können, die mehrere Agenten umfasst, die zusammenarbeiten, um Daten zu analysieren. Jeder Agent erfüllt eine spezifische Funktion, und die Aufgabe wird durch die Koordination der Agenten ausgeführt, um das gewünschte Ergebnis zu erzielen. Durch die Erstellung spezialisierter Agenten mit spezifischen Rollen können Sie die Effizienz und Leistung von Aufgaben verbessern.

### Lernen in Echtzeit

Fortschrittliche Frameworks bieten Fähigkeiten für kontextuelles Verständnis und Anpassung in Echtzeit.

**Wie Teams diese nutzen können**: Teams können Feedback-Schleifen implementieren, bei denen Agenten aus Interaktionen lernen und ihr Verhalten dynamisch anpassen, was zu kontinuierlicher Verbesserung und Verfeinerung der Fähigkeiten führt.

**Wie es in der Praxis funktioniert**: Agenten können Benutzerfeedback, Umweltdaten und Aufgabenergebnisse analysieren, um ihre Wissensbasis zu aktualisieren, Entscheidungsalgorithmen anzupassen und ihre Leistung im Laufe der Zeit zu verbessern. Dieser iterative Lernprozess ermöglicht es Agenten, sich an veränderte Bedingungen und Benutzerpräferenzen anzupassen, was die Gesamteffektivität des Systems erhöht.

## Was sind die Unterschiede zwischen den Frameworks AutoGen, Semantic Kernel und Azure AI Agent Service?

Es gibt viele Möglichkeiten, diese Frameworks zu vergleichen, aber lassen Sie uns einige wichtige Unterschiede in Bezug auf ihr Design, ihre Fähigkeiten und ihre Zielanwendungsfälle betrachten:

## AutoGen

AutoGen ist ein Open-Source-Framework, das vom AI Frontiers Lab von Microsoft Research entwickelt wurde. Es konzentriert sich auf ereignisgesteuerte, verteilte *agentische* Anwendungen und ermöglicht mehrere LLMs und SLMs, Tools und fortschrittliche Multi-Agent-Designmuster.

AutoGen basiert auf dem Kernkonzept von Agenten, die autonome Einheiten sind, die ihre Umgebung wahrnehmen, Entscheidungen treffen und Maßnahmen ergreifen können, um spezifische Ziele zu erreichen. Agenten kommunizieren über asynchrone Nachrichten, was es ihnen ermöglicht, unabhängig und parallel zu arbeiten, wodurch die Skalierbarkeit und Reaktionsfähigkeit des Systems verbessert wird.

<a href="https://en.wikipedia.org/wiki/Actor_model" target="_blank">Agenten basieren auf dem Actor-Modell</a>. Laut Wikipedia ist ein Actor _der grundlegende Baustein der nebenläufigen Berechnung. Als Antwort auf eine empfangene Nachricht kann ein Actor: lokale Entscheidungen treffen, weitere Actors erstellen, weitere Nachrichten senden und bestimmen, wie auf die nächste empfangene Nachricht reagiert werden soll_.

**Anwendungsfälle**: Automatisierung von Code-Generierung, Datenanalysetätigkeiten und Erstellung benutzerdefinierter Agenten für Planungs- und Forschungsfunktionen.

Hier sind einige wichtige Kernkonzepte von AutoGen:

- **Agenten**. Ein Agent ist eine Softwareeinheit, die:
  - **Über Nachrichten kommuniziert**, diese Nachrichten können synchron oder asynchron sein.
  - **Ihren eigenen Zustand verwaltet**, der durch eingehende Nachrichten geändert werden kann.
  - **Maßnahmen ergreift** als Reaktion auf empfangene Nachrichten oder Änderungen ihres Zustands. Diese Maßnahmen können den Zustand des Agenten ändern und externe Effekte hervorrufen, wie z. B. das Aktualisieren von Nachrichtenprotokollen, das Senden neuer Nachrichten, das Ausführen von Code oder das Durchführen von API-Aufrufen.
    
  Hier ist ein kurzer Codeausschnitt, in dem Sie Ihren eigenen Agenten mit Chat-Funktionen erstellen:

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
  
    Im vorherigen Code wurde `MyAgent` erstellt und erbt von `RoutedAgent`. Es hat einen Nachrichten-Handler, der den Inhalt der Nachricht ausgibt und dann eine Antwort mit dem `AssistantAgent`-Delegaten sendet. Beachten Sie insbesondere, wie wir `self._delegate` eine Instanz von `AssistantAgent` zuweisen, einem vorgefertigten Agenten, der Chat-Vervollständigungen handhaben kann.

    Lassen Sie AutoGen als Nächstes über diesen Agententyp wissen und starten Sie das Programm:

    ```python
    
    # main.py
    runtime = SingleThreadedAgentRuntime()
    await MyAgent.register(runtime, "my_agent", lambda: MyAgent())

    runtime.start()  # Start processing messages in the background.
    await runtime.send_message(MyMessageType("Hello, World!"), AgentId("my_agent", "default"))
    ```
  
    Im vorherigen Code werden die Agenten bei der Laufzeit registriert und dann wird eine Nachricht an den Agenten gesendet, was zu folgendem Ergebnis führt:

    ```text
    # Output from the console:
    my_agent received message: Hello, World!
    my_assistant received message: Hello, World!
    my_assistant responded: Hello! How can I assist you today?
    ```
  
- **Multi-Agenten**. AutoGen unterstützt die Erstellung mehrerer Agenten, die zusammenarbeiten können, um komplexe Aufgaben zu erfüllen. Agenten können kommunizieren, Informationen austauschen und ihre Aktionen koordinieren, um Probleme effizienter zu lösen. Um ein Multi-Agenten-System zu erstellen, können Sie verschiedene Arten von Agenten mit spezialisierten Funktionen und Rollen definieren, wie z. B. Datenabruf, Analyse, Entscheidungsfindung und Benutzerinteraktion. Schauen wir uns an, wie eine solche Erstellung aussieht:

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
  
    Im vorherigen Code haben wir einen `GroupChatManager`, der bei der Laufzeit registriert ist. Dieser Manager ist für die Koordination der Interaktionen zwischen verschiedenen Arten von Agenten verantwortlich, wie z. B. Autoren, Illustratoren, Redakteuren und Benutzern.

- **Agenten-Laufzeit**. Das Framework bietet eine Laufzeitumgebung, die die Kommunikation zwischen Agenten ermöglicht, ihre Identitäten und Lebenszyklen verwaltet und Sicherheits- und Datenschutzgrenzen durchsetzt. Das bedeutet, dass Sie Ihre Agenten in einer sicheren und kontrollierten Umgebung ausführen können, um sicherzustellen, dass sie sicher und effizient interagieren können. Es gibt zwei interessante Laufzeiten:
  - **Eigenständige Laufzeit**. Dies ist eine gute Wahl für Einzelprozessanwendungen, bei denen alle Agenten in derselben Programmiersprache implementiert und im selben Prozess ausgeführt werden. Hier ist eine Illustration, wie es funktioniert:
  
    <a href="https://microsoft.github.io/autogen/stable/_images/architecture-standalone.svg" target="_blank">Eigenständige Laufzeit</a>  
Anwendungsstack

    *Agenten kommunizieren über Nachrichten durch die Laufzeit, und die Laufzeit verwaltet den Lebenszyklus der Agenten*

  - **Verteilte Agenten-Laufzeit**, geeignet für Multi-Prozess-Anwendungen, bei denen Agenten möglicherweise in verschiedenen Programmiersprachen implementiert und auf verschiedenen Maschinen ausgeführt werden. Hier ist eine Illustration, wie es funktioniert:
  
    <a href="https://microsoft.github.io/autogen/stable/_images/architecture-distributed.svg" target="_blank">Verteilte Laufzeit</a>

## Semantic Kernel + Agenten-Framework

Semantic Kernel ist ein unternehmensbereites AI-Orchestrierungs-SDK. Es besteht aus AI- und Memory-Connectoren sowie einem Agenten-Framework.

Lassen Sie uns zunächst einige Kernkomponenten behandeln:

- **AI-Connectoren**: Dies ist eine Schnittstelle zu externen AI-Diensten und Datenquellen für die Verwendung in Python und C#.

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
  
    Hier haben Sie ein einfaches Beispiel, wie Sie einen Kernel erstellen und einen Chat-Vervollständigungsdienst hinzufügen können. Semantic Kernel erstellt eine Verbindung zu einem externen AI-Dienst, in diesem Fall Azure OpenAI Chat Completion.

- **Plugins**: Diese kapseln Funktionen, die eine Anwendung nutzen kann. Es gibt sowohl fertige Plugins als auch benutzerdefinierte, die Sie erstellen können. Ein verwandtes Konzept sind "Prompt-Funktionen". Anstatt natürliche Sprachhinweise für Funktionsaufrufe bereitzustellen, senden Sie bestimmte Funktionen an das Modell. Basierend auf dem aktuellen Chat-Kontext kann das Modell eine dieser Funktionen aufrufen, um eine Anfrage oder Abfrage zu vervollständigen. Hier ist ein Beispiel:

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
  
    Hier haben Sie zunächst eine Vorlage `skPrompt`, die Platz für die Benutzereingabe `$userInput` lässt. Dann erstellen Sie die Kernel-Funktion `SummarizeText` und importieren sie in den Kernel mit dem Plugin-Namen `SemanticFunctions`. Beachten Sie den Funktionsnamen, der Semantic Kernel hilft zu verstehen, was die Funktion tut und wann sie aufgerufen werden sollte.

- **Native Funktion**: Es gibt auch native Funktionen, die das Framework direkt aufrufen kann, um die Aufgabe auszuführen. Hier ist ein Beispiel für eine solche Funktion, die den Inhalt aus einer Datei abruft:

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
  
- **Speicher**: Abstrahiert und vereinfacht das Kontextmanagement für AI-Apps. Die Idee des Speichers ist, dass dies etwas ist, das das LLM wissen sollte. Sie können diese Informationen in einem Vektorspeicher speichern, der letztendlich eine In-Memory-Datenbank oder eine Vektordatenbank oder Ähnliches ist. Hier ist ein Beispiel für ein sehr vereinfachtes Szenario, in dem *Fakten* zum Speicher hinzugefügt werden:

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
  
Diese Fakten werden dann in der Speichersammlung `SummarizedAzureDocs` gespeichert. Dies ist ein sehr vereinfachtes Beispiel, aber Sie können sehen, wie Informationen im Speicher abgelegt werden können, damit das LLM sie nutzen kann.

Das sind die Grundlagen des Semantic Kernel Frameworks, aber was ist mit dem Agent Framework?

## Azure AI Agent Service

Der Azure AI Agent Service ist eine neuere Ergänzung, die auf der Microsoft Ignite 2024 vorgestellt wurde. Er ermöglicht die Entwicklung und Bereitstellung von KI-Agenten mit flexibleren Modellen, wie z. B. dem direkten Aufruf von Open-Source-LLMs wie Llama 3, Mistral und Cohere.

Der Azure AI Agent Service bietet stärkere Sicherheitsmechanismen für Unternehmen und Methoden zur Datenspeicherung, was ihn für Unternehmensanwendungen geeignet macht.

Er funktioniert sofort mit Multi-Agent-Orchestrierungs-Frameworks wie AutoGen und Semantic Kernel.

Dieser Service befindet sich derzeit in der Public Preview und unterstützt Python und C# für die Entwicklung von Agenten.

Mit Semantic Kernel Python können wir einen Azure AI Agent mit einem benutzerdefinierten Plugin erstellen:

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

### Kernkonzepte

Der Azure AI Agent Service hat die folgenden Kernkonzepte:

- **Agent**. Der Azure AI Agent Service integriert sich in die Azure AI Foundry. Innerhalb der AI Foundry agiert ein KI-Agent als "intelligenter" Microservice, der Fragen beantworten (RAG), Aktionen ausführen oder Workflows vollständig automatisieren kann. Dies wird durch die Kombination der Leistungsfähigkeit generativer KI-Modelle mit Tools erreicht, die den Zugriff auf und die Interaktion mit realen Datenquellen ermöglichen. Hier ist ein Beispiel für einen Agenten:

    ```python
    agent = project_client.agents.create_agent(
        model="gpt-4o-mini",
        name="my-agent",
        instructions="You are helpful agent",
        tools=code_interpreter.definitions,
        tool_resources=code_interpreter.resources,
    )
    ```

    In diesem Beispiel wird ein Agent mit dem Modell `gpt-4o-mini`, einem Namen `my-agent` und Anweisungen `You are helpful agent` erstellt. Der Agent ist mit Tools und Ressourcen ausgestattet, um Aufgaben wie die Codeinterpretation auszuführen.

- **Thread und Nachrichten**. Der Thread ist ein weiteres wichtiges Konzept. Er repräsentiert ein Gespräch oder eine Interaktion zwischen einem Agenten und einem Benutzer. Threads können verwendet werden, um den Fortschritt eines Gesprächs zu verfolgen, Kontextinformationen zu speichern und den Zustand der Interaktion zu verwalten. Hier ist ein Beispiel für einen Thread:

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

    Im vorherigen Code wird ein Thread erstellt. Danach wird eine Nachricht an den Thread gesendet. Durch den Aufruf von `create_and_process_run` wird der Agent aufgefordert, an dem Thread zu arbeiten. Schließlich werden die Nachrichten abgerufen und protokolliert, um die Antwort des Agenten zu sehen. Die Nachrichten zeigen den Fortschritt des Gesprächs zwischen dem Benutzer und dem Agenten. Es ist auch wichtig zu verstehen, dass die Nachrichten unterschiedliche Typen haben können, wie Text, Bild oder Datei, was bedeutet, dass die Arbeit des Agenten beispielsweise in einem Bild oder einer Textantwort resultiert. Als Entwickler können Sie diese Informationen dann weiterverarbeiten oder dem Benutzer präsentieren.

- **Integration mit anderen KI-Frameworks**. Der Azure AI Agent Service kann mit anderen Frameworks wie AutoGen und Semantic Kernel interagieren, was bedeutet, dass Sie einen Teil Ihrer App in einem dieser Frameworks erstellen und beispielsweise den Agent Service als Orchestrator verwenden können, oder Sie können alles im Agent Service erstellen.

**Anwendungsfälle**: Der Azure AI Agent Service ist für Unternehmensanwendungen konzipiert, die eine sichere, skalierbare und flexible Bereitstellung von KI-Agenten erfordern.

## Was sind die Unterschiede zwischen diesen Frameworks?

Es scheint, als gäbe es viele Überschneidungen zwischen diesen Frameworks, aber es gibt einige wesentliche Unterschiede in Bezug auf Design, Fähigkeiten und Zielanwendungsfälle:

- **AutoGen**: Ein Experimentier-Framework, das sich auf Spitzenforschung zu Multi-Agent-Systemen konzentriert. Es ist der beste Ort, um komplexe Multi-Agent-Systeme zu experimentieren und zu prototypisieren.
- **Semantic Kernel**: Eine produktionsreife Agentenbibliothek für den Aufbau von Unternehmensanwendungen. Es konzentriert sich auf ereignisgesteuerte, verteilte Agentenanwendungen und ermöglicht mehrere LLMs und SLMs, Tools sowie Einzel-/Multi-Agent-Designmuster.
- **Azure AI Agent Service**: Eine Plattform- und Bereitstellungsdienst in der Azure Foundry für Agenten. Es bietet Konnektivität zu Diensten, die von Azure unterstützt werden, wie Azure OpenAI, Azure AI Search, Bing Search und Codeausführung.

Immer noch unsicher, welches Sie wählen sollen?

### Anwendungsfälle

Schauen wir, ob wir Ihnen helfen können, indem wir einige häufige Anwendungsfälle durchgehen:

> F: Ich experimentiere, lerne und baue Proof-of-Concept-Agentenanwendungen und möchte schnell bauen und experimentieren können.
>

>A: AutoGen wäre eine gute Wahl für dieses Szenario, da es sich auf ereignisgesteuerte, verteilte Agentenanwendungen konzentriert und fortschrittliche Multi-Agent-Designmuster unterstützt.

> F: Was macht AutoGen für diesen Anwendungsfall besser geeignet als Semantic Kernel und Azure AI Agent Service?
>
> A: AutoGen wurde speziell für ereignisgesteuerte, verteilte Agentenanwendungen entwickelt und eignet sich daher hervorragend für die Automatisierung von Codegenerierungs- und Datenanalysetätigkeiten. Es bietet die notwendigen Tools und Fähigkeiten, um komplexe Multi-Agent-Systeme effizient zu erstellen.

>F: Klingt so, als könnte Azure AI Agent Service hier auch funktionieren, es hat Tools für die Codegenerierung und mehr?

>
> A: Ja, der Azure AI Agent Service ist ein Plattformdienst für Agenten und bietet integrierte Funktionen für mehrere Modelle, Azure AI Search, Bing Search und Azure Functions. Es macht es einfach, Ihre Agenten im Foundry-Portal zu erstellen und in großem Maßstab bereitzustellen.

> F: Ich bin immer noch verwirrt, geben Sie mir einfach eine Option.
>
> A: Eine großartige Wahl ist es, Ihre Anwendung zuerst in Semantic Kernel zu erstellen und dann den Azure AI Agent Service zu verwenden, um Ihren Agenten bereitzustellen. Dieser Ansatz ermöglicht es Ihnen, Ihre Agenten einfach zu speichern und gleichzeitig die Möglichkeit zu nutzen, Multi-Agent-Systeme in Semantic Kernel zu erstellen. Darüber hinaus verfügt Semantic Kernel über einen Connector in AutoGen, was die gemeinsame Nutzung beider Frameworks erleichtert.

Lassen Sie uns die wichtigsten Unterschiede in einer Tabelle zusammenfassen:

| Framework | Fokus | Kernkonzepte | Anwendungsfälle |
| --- | --- | --- | --- |
| AutoGen | Ereignisgesteuerte, verteilte Agentenanwendungen | Agenten, Personas, Funktionen, Daten | Codegenerierung, Datenanalysetätigkeiten |
| Semantic Kernel | Verständnis und Generierung menschenähnlicher Textinhalte | Agenten, modulare Komponenten, Zusammenarbeit | Sprachverständnis, Inhaltserstellung |
| Azure AI Agent Service | Flexible Modelle, Unternehmenssicherheit, Codegenerierung, Tool-Aufrufe | Modularität, Zusammenarbeit, Prozess-Orchestrierung | Sichere, skalierbare und flexible Bereitstellung von KI-Agenten |

Was ist der ideale Anwendungsfall für jedes dieser Frameworks?

## Kann ich meine bestehenden Azure-Ökosystem-Tools direkt integrieren oder benötige ich eigenständige Lösungen?

Die Antwort ist ja, Sie können Ihre bestehenden Azure-Ökosystem-Tools direkt mit dem Azure AI Agent Service integrieren, insbesondere weil er so konzipiert wurde, dass er nahtlos mit anderen Azure-Diensten funktioniert. Sie könnten beispielsweise Bing, Azure AI Search und Azure Functions integrieren. Es gibt auch eine tiefe Integration mit der Azure AI Foundry.

Für AutoGen und Semantic Kernel können Sie ebenfalls mit Azure-Diensten integrieren, aber es kann erforderlich sein, die Azure-Dienste aus Ihrem Code aufzurufen. Eine weitere Möglichkeit zur Integration besteht darin, die Azure SDKs zu verwenden, um von Ihren Agenten aus mit Azure-Diensten zu interagieren. Wie bereits erwähnt, können Sie den Azure AI Agent Service auch als Orchestrator für Ihre in AutoGen oder Semantic Kernel erstellten Agenten verwenden, was einen einfachen Zugriff auf das Azure-Ökosystem ermöglicht.

## Beispielcodes

- Python: [Agent Framework](./code_samples/02-python-agent-framework.ipynb)
- .NET: [Agent Framework](./code_samples/02-dotnet-agent-framework.md)

## Haben Sie weitere Fragen zu KI-Agenten-Frameworks?

Treten Sie dem [Azure AI Foundry Discord](https://aka.ms/ai-agents/discord) bei, um andere Lernende zu treffen, an Sprechstunden teilzunehmen und Ihre Fragen zu KI-Agenten beantwortet zu bekommen.

## Referenzen

- <a href="https://techcommunity.microsoft.com/blog/azure-ai-services-blog/introducing-azure-ai-agent-service/4298357" target="_blank">Azure Agent Service</a>
- <a href="https://devblogs.microsoft.com/semantic-kernel/microsofts-agentic-ai-frameworks-autogen-and-semantic-kernel/" target="_blank">Semantic Kernel und AutoGen</a>
- <a href="https://learn.microsoft.com/semantic-kernel/frameworks/agent/?pivots=programming-language-python" target="_blank">Semantic Kernel Python Agent Framework</a>
- <a href="https://learn.microsoft.com/semantic-kernel/frameworks/agent/?pivots=programming-language-csharp" target="_blank">Semantic Kernel .Net Agent Framework</a>
- <a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Azure AI Agent Service</a>
- <a href="https://techcommunity.microsoft.com/blog/educatordeveloperblog/using-azure-ai-agent-service-with-autogen--semantic-kernel-to-build-a-multi-agen/4363121" target="_blank">Verwendung des Azure AI Agent Service mit AutoGen / Semantic Kernel zur Erstellung einer Multi-Agent-Lösung</a>

## Vorherige Lektion

[Einführung in KI-Agenten und Anwendungsfälle](../01-intro-to-ai-agents/README.md)

## Nächste Lektion

[Verständnis von agentischen Designmustern](../03-agentic-design-patterns/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Haftungsausschluss**:  
Dieses Dokument wurde mit dem KI-Übersetzungsdienst [Co-op Translator](https://github.com/Azure/co-op-translator) übersetzt. Obwohl wir uns um Genauigkeit bemühen, beachten Sie bitte, dass automatisierte Übersetzungen Fehler oder Ungenauigkeiten enthalten können. Das Originaldokument in seiner ursprünglichen Sprache sollte als maßgebliche Quelle betrachtet werden. Für kritische Informationen wird eine professionelle menschliche Übersetzung empfohlen. Wir übernehmen keine Haftung für Missverständnisse oder Fehlinterpretationen, die sich aus der Nutzung dieser Übersetzung ergeben.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->