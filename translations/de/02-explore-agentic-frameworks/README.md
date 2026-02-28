[![Erkundung von KI-Agenten-Frameworks](../../../translated_images/de/lesson-2-thumbnail.c65f44c93b8558df.webp)](https://youtu.be/ODwF-EZo_O8?si=1xoy_B9RNQfrYdF7)

> _(Klicken Sie auf das obige Bild, um das Video zu dieser Lektion anzusehen)_

# Erkunden von KI-Agenten-Frameworks

KI-Agenten-Frameworks sind Softwareplattformen, die entwickelt wurden, um die Erstellung, Bereitstellung und Verwaltung von KI-Agenten zu vereinfachen. Diese Frameworks stellen Entwicklern vorgefertigte Komponenten, Abstraktionen und Werkzeuge zur Verfügung, die die Entwicklung komplexer KI-Systeme beschleunigen.

Diese Frameworks helfen Entwicklern, sich auf die einzigartigen Aspekte ihrer Anwendungen zu konzentrieren, indem sie standardisierte Ansätze für häufige Herausforderungen in der Entwicklung von KI-Agenten bieten. Sie verbessern Skalierbarkeit, Zugänglichkeit und Effizienz beim Aufbau von KI-Systemen.

## Einleitung 

Diese Lektion behandelt:

- Was sind KI-Agenten-Frameworks und was ermöglichen sie Entwicklern zu erreichen?
- Wie können Teams diese nutzen, um schnell Prototypen zu erstellen, zu iterieren und die Fähigkeiten ihres Agenten zu verbessern?
- Was sind die Unterschiede zwischen den Frameworks und Tools, die von Microsoft erstellt wurden (<a href="https://aka.ms/ai-agents-beginners/ai-agent-service" target="_blank">Azure AI Agent Service</a> und dem <a href="https://learn.microsoft.com/azure/ai-services/openai/how-to/responses" target="_blank">Microsoft Agent Framework</a>)?
- Kann ich meine vorhandenen Azure-Ökosystem-Tools direkt integrieren, oder benötige ich eigenständige Lösungen?
- Was ist Azure AI Agents service und wie hilft mir das?

## Lernziele

Die Ziele dieser Lektion sind, Ihnen zu helfen zu verstehen:

- Die Rolle von KI-Agenten-Frameworks in der KI-Entwicklung.
- Wie man KI-Agenten-Frameworks einsetzt, um intelligente Agenten zu bauen.
- Wichtige Fähigkeiten, die durch KI-Agenten-Frameworks ermöglicht werden.
- Die Unterschiede zwischen dem Microsoft Agent Framework und Azure AI Agent Service.

## Was sind KI-Agenten-Frameworks und was ermöglichen sie Entwicklern zu tun?

Traditionelle KI-Frameworks können Ihnen helfen, KI in Ihre Apps zu integrieren und diese Apps in den folgenden Punkten zu verbessern:

- **Personalisierung**: KI kann das Nutzerverhalten und Präferenzen analysieren, um personalisierte Empfehlungen, Inhalte und Erlebnisse zu bieten.
Beispiel: Streaming-Dienste wie Netflix verwenden KI, um Filme und Serien basierend auf der Sehhistorie vorzuschlagen und so die Nutzerbindung und Zufriedenheit zu erhöhen.
- **Automatisierung und Effizienz**: KI kann sich wiederholende Aufgaben automatisieren, Workflows straffen und die operative Effizienz verbessern.
Beispiel: Kundenservice-Anwendungen nutzen KI-gestützte Chatbots, um häufige Anfragen zu bearbeiten, Antwortzeiten zu verkürzen und menschliche Agenten für komplexere Probleme freizustellen.
- **Verbessertes Benutzererlebnis**: KI kann das gesamte Benutzererlebnis verbessern, indem intelligente Funktionen wie Spracherkennung, natürliche Sprachverarbeitung und prädiktiver Text bereitgestellt werden.
Beispiel: Virtuelle Assistenten wie Siri und Google Assistant verwenden KI, um Sprachbefehle zu verstehen und darauf zu reagieren, wodurch die Interaktion der Nutzer mit ihren Geräten erleichtert wird.

### Das klingt alles großartig, also warum brauchen wir das KI-Agenten-Framework?

KI-Agenten-Frameworks sind mehr als nur klassische KI-Frameworks. Sie sind darauf ausgelegt, die Erstellung intelligenter Agenten zu ermöglichen, die mit Nutzern, anderen Agenten und der Umgebung interagieren, um spezifische Ziele zu erreichen. Diese Agenten können autonomes Verhalten zeigen, Entscheidungen treffen und sich an veränderte Bedingungen anpassen. Schauen wir uns einige wichtige Fähigkeiten an, die KI-Agenten-Frameworks ermöglichen:

- **Agentenzusammenarbeit und Koordination**: Ermöglichen die Erstellung mehrerer KI-Agenten, die zusammenarbeiten, kommunizieren und koordinieren, um komplexe Aufgaben zu lösen.
- **Aufgabenautomatisierung und -verwaltung**: Bieten Mechanismen zur Automatisierung mehrstufiger Workflows, Aufgabenzuweisung und dynamischen Aufgabenverwaltung zwischen Agenten.
- **Kontextuelles Verständnis und Anpassung**: Rüsten Agenten mit der Fähigkeit aus, Kontext zu verstehen, sich an verändernde Umgebungen anzupassen und Entscheidungen auf Basis von Echtzeitinformationen zu treffen.

Zusammenfassend ermöglichen Agenten mehr — sie heben Automatisierung auf die nächste Ebene und schaffen intelligentere Systeme, die sich an ihre Umgebung anpassen und daraus lernen können.

## Wie kann man schnell Prototypen erstellen, iterieren und die Fähigkeiten des Agenten verbessern?

Dieses Feld entwickelt sich schnell, aber es gibt einige Gemeinsamkeiten in den meisten KI-Agenten-Frameworks, die Ihnen helfen können, schnell Prototypen zu erstellen und zu iterieren, nämlich modulare Komponenten, kollaborative Werkzeuge und Lernen in Echtzeit. Lassen Sie uns diese genauer betrachten:

- **Verwenden Sie modulare Komponenten**: KI-SDKs bieten vorgefertigte Komponenten wie KI- und Speicher-Connectoren, Funktionsaufrufe durch natürliche Sprache oder Code-Plugins, Prompt-Vorlagen und mehr.
- **Nutzen Sie kollaborative Tools**: Entwerfen Sie Agenten mit spezifischen Rollen und Aufgaben, sodass sie kollaborative Workflows testen und verfeinern können.
- **Lernen in Echtzeit**: Implementieren Sie Feedback-Schleifen, bei denen Agenten aus Interaktionen lernen und ihr Verhalten dynamisch anpassen.

### Verwenden Sie modulare Komponenten

SDKs wie das Microsoft Agent Framework bieten vorgefertigte Komponenten wie KI-Connectoren, Tool-Definitionen und Agentenmanagement.

**Wie Teams diese nutzen können**: Teams können diese Komponenten schnell zusammenstellen, um einen funktionalen Prototyp zu erstellen, ohne von null anfangen zu müssen. Dies ermöglicht schnelles Experimentieren und Iterieren.

**Wie es in der Praxis funktioniert**: Sie können einen vorgefertigten Parser verwenden, um Informationen aus Benutzereingaben zu extrahieren, ein Memory-Modul, um Daten zu speichern und abzurufen, und einen Prompt-Generator, um mit Nutzern zu interagieren — alles ohne diese Komponenten selbst bauen zu müssen.

**Beispielcode**. Schauen wir uns ein Beispiel an, wie Sie das Microsoft Agent Framework mit `AzureAIProjectAgentProvider` verwenden können, damit das Modell auf Benutzereingaben mit Toolaufrufen reagiert:

``` python
# Microsoft Agent Framework Python Beispiel

import asyncio
import os
from typing import Annotated

from agent_framework.azure import AzureAIProjectAgentProvider
from azure.identity import AzureCliCredential


# Definieren Sie eine Beispiel-Tool-Funktion zur Buchung von Reisen
def book_flight(date: str, location: str) -> str:
    """Book travel given location and date."""
    return f"Travel was booked to {location} on {date}"


async def main():
    provider = AzureAIProjectAgentProvider(credential=AzureCliCredential())
    agent = await provider.create_agent(
        name="travel_agent",
        instructions="Help the user book travel. Use the book_flight tool when ready.",
        tools=[book_flight],
    )

    response = await agent.run("I'd like to go to New York on January 1, 2025")
    print(response)
    # Beispielausgabe: Ihr Flug nach New York am 1. Januar 2025 wurde erfolgreich gebucht. Gute Reise! ✈️🗽


if __name__ == "__main__":
    asyncio.run(main())
```

Was Sie an diesem Beispiel sehen können, ist, wie Sie einen vorgefertigten Parser nutzen können, um Schlüsselinformationen aus Benutzereingaben zu extrahieren, wie Herkunft, Ziel und Datum einer Flugbuchungsanfrage. Dieser modulare Ansatz ermöglicht es Ihnen, sich auf die übergeordnete Logik zu konzentrieren.

### Nutzen Sie kollaborative Tools

Frameworks wie das Microsoft Agent Framework erleichtern die Erstellung mehrerer Agenten, die zusammenarbeiten können.

**Wie Teams diese nutzen können**: Teams können Agenten mit spezifischen Rollen und Aufgaben entwerfen, sodass sie kollaborative Workflows testen und verfeinern und die Gesamteffizienz des Systems verbessern können.

**Wie es in der Praxis funktioniert**: Sie können ein Team von Agenten erstellen, wobei jeder Agent eine spezialisierte Funktion hat, wie Datenabruf, Analyse oder Entscheidungsfindung. Diese Agenten können kommunizieren und Informationen teilen, um ein gemeinsames Ziel zu erreichen, z. B. eine Benutzeranfrage beantworten oder eine Aufgabe abschließen.

**Beispielcode (Microsoft Agent Framework)**:

```python
# Mehrere Agenten erstellen, die zusammen mit dem Microsoft Agent Framework arbeiten

import os
from agent_framework.azure import AzureAIProjectAgentProvider
from azure.identity import AzureCliCredential

provider = AzureAIProjectAgentProvider(credential=AzureCliCredential())

# Datenabruf-Agent
agent_retrieve = await provider.create_agent(
    name="dataretrieval",
    instructions="Retrieve relevant data using available tools.",
    tools=[retrieve_tool],
)

# Datenanalyse-Agent
agent_analyze = await provider.create_agent(
    name="dataanalysis",
    instructions="Analyze the retrieved data and provide insights.",
    tools=[analyze_tool],
)

# Agenten nacheinander für eine Aufgabe ausführen
retrieval_result = await agent_retrieve.run("Retrieve sales data for Q4")
analysis_result = await agent_analyze.run(f"Analyze this data: {retrieval_result}")
print(analysis_result)
```

Was Sie im vorherigen Code sehen, ist, wie Sie eine Aufgabe erstellen können, die mehrere Agenten umfasst, die zusammenarbeiten, um Daten zu analysieren. Jeder Agent führt eine spezifische Funktion aus, und die Aufgabe wird durch Koordinierung der Agenten ausgeführt, um das gewünschte Ergebnis zu erzielen. Durch die Erstellung dedizierter Agenten mit spezialisierten Rollen können Sie die Aufgabeneffizienz und Leistung verbessern.

### Lernen in Echtzeit

Fortgeschrittene Frameworks bieten Fähigkeiten für Echtzeit-Kontextverständnis und Anpassung.

**Wie Teams diese nutzen können**: Teams können Feedback-Schleifen implementieren, in denen Agenten aus Interaktionen lernen und ihr Verhalten dynamisch anpassen, was zu kontinuierlicher Verbesserung und Verfeinerung der Fähigkeiten führt.

**Wie es in der Praxis funktioniert**: Agenten können Nutzerfeedback, Umgebungsdaten und Aufgabenergebnisse analysieren, um ihre Wissensbasis zu aktualisieren, Entscheidungsalgorithmen anzupassen und die Leistung im Laufe der Zeit zu verbessern. Dieser iterative Lernprozess ermöglicht es Agenten, sich an sich ändernde Bedingungen und Nutzerpräferenzen anzupassen und so die Gesamteffektivität des Systems zu steigern.

## Was sind die Unterschiede zwischen dem Microsoft Agent Framework und Azure AI Agent Service?

Es gibt viele Möglichkeiten, diese Ansätze zu vergleichen, aber schauen wir uns einige Schlüsseldifferenzen in Bezug auf Design, Fähigkeiten und Zielanwendungsfälle an:

## Microsoft Agent Framework (MAF)

Das Microsoft Agent Framework bietet ein schlankes SDK zum Erstellen von KI-Agenten mit `AzureAIProjectAgentProvider`. Es ermöglicht Entwicklern, Agenten zu erstellen, die Azure OpenAI-Modelle mit integriertem Toolaufruf, Konversationsmanagement und unternehmensgerechter Sicherheit über Azure-Identität nutzen.

**Anwendungsfälle**: Erstellen produktionsreifer KI-Agenten mit Toolnutzung, mehrstufigen Workflows und Szenarien zur Unternehmensintegration.

Hier sind einige wichtige Kernkonzepte des Microsoft Agent Framework:

- **Agents**. Ein Agent wird über `AzureAIProjectAgentProvider` erstellt und mit einem Namen, Anweisungen und Tools konfiguriert. Der Agent kann:
  - **Benutzernachrichten verarbeiten** und Antworten mithilfe von Azure OpenAI-Modellen generieren.
  - **Tools automatisch aufrufen** basierend auf dem Konversationskontext.
  - **Den Konversationszustand** über mehrere Interaktionen hinweg beibehalten.

  Hier ist ein Codeausschnitt, der zeigt, wie man einen Agenten erstellt:

    ```python
    import os
    from agent_framework.azure import AzureAIProjectAgentProvider
    from azure.identity import AzureCliCredential

    provider = AzureAIProjectAgentProvider(credential=AzureCliCredential())
    agent = await provider.create_agent(
        name="my_agent",
        instructions="You are a helpful assistant.",
    )

    response = await agent.run("Hello, World!")
    print(response)
    ```

- **Tools**. Das Framework unterstützt die Definition von Tools als Python-Funktionen, die der Agent automatisch aufrufen kann. Tools werden bei der Erstellung des Agenten registriert:

    ```python
    def get_weather(location: str) -> str:
        """Get the current weather for a location."""
        return f"The weather in {location} is sunny, 72\u00b0F."

    agent = await provider.create_agent(
        name="weather_agent",
        instructions="Help users check the weather.",
        tools=[get_weather],
    )
    ```

- **Multi-Agent-Koordination**. Sie können mehrere Agenten mit unterschiedlichen Spezialisierungen erstellen und ihre Arbeit koordinieren:

    ```python
    planner = await provider.create_agent(
        name="planner",
        instructions="Break down complex tasks into steps.",
    )

    executor = await provider.create_agent(
        name="executor",
        instructions="Execute the planned steps using available tools.",
        tools=[execute_tool],
    )

    plan = await planner.run("Plan a trip to Paris")
    result = await executor.run(f"Execute this plan: {plan}")
    ```

- **Azure-Identitätsintegration**. Das Framework verwendet `AzureCliCredential` (oder `DefaultAzureCredential`) für eine sichere, schlüsselose Authentifizierung, wodurch die Notwendigkeit entfällt, API-Schlüssel direkt zu verwalten.

## Azure AI Agent Service

Azure AI Agent Service ist eine neuere Ergänzung, eingeführt auf der Microsoft Ignite 2024. Es ermöglicht die Entwicklung und Bereitstellung von KI-Agenten mit flexibleren Modellen, wie dem direkten Aufruf von Open-Source-LLMs wie Llama 3, Mistral und Cohere.

Azure AI Agent Service bietet stärkere Mechanismen für Unternehmenssicherheit und Methoden zur Datenspeicherung, wodurch es sich für Unternehmensanwendungen eignet.

Es funktioniert direkt mit dem Microsoft Agent Framework zum Erstellen und Bereitstellen von Agenten.

Dieser Service befindet sich derzeit in der Public Preview und unterstützt Python und C# zum Erstellen von Agenten.

Mit dem Python-SDK des Azure AI Agent Service können wir einen Agenten mit einem benutzerdefinierten Tool erstellen:

```python
import asyncio
from azure.identity import DefaultAzureCredential
from azure.ai.projects import AIProjectClient

# Definieren Sie Werkzeugfunktionen
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
        model="gpt-4o-mini",
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

### Kernkonzepte

Azure AI Agent Service hat die folgenden Kernkonzepte:

- **Agent**. Azure AI Agent Service integriert sich mit Microsoft Foundry. Innerhalb von AI Foundry fungiert ein AI Agent als "smartes" Microservice, das verwendet werden kann, um Fragen zu beantworten (RAG), Aktionen auszuführen oder Workflows vollständig zu automatisieren. Dies wird erreicht, indem die Leistungsfähigkeit generativer KI-Modelle mit Tools kombiniert wird, die es dem Agenten ermöglichen, auf reale Datenquellen zuzugreifen und mit ihnen zu interagieren. Hier ist ein Beispiel für einen Agenten:

    ```python
    agent = project_client.agents.create_agent(
        model="gpt-4o-mini",
        name="my-agent",
        instructions="You are helpful agent",
        tools=code_interpreter.definitions,
        tool_resources=code_interpreter.resources,
    )
    ```

    In diesem Beispiel wird ein Agent mit dem Modell `gpt-4o-mini`, dem Namen `my-agent` und den Anweisungen `You are helpful agent` erstellt. Der Agent ist mit Tools und Ressourcen ausgestattet, um Aufgaben zur Code-Interpretation durchzuführen.

- **Thread and messages**. Der Thread ist ein weiteres wichtiges Konzept. Er repräsentiert eine Konversation oder Interaktion zwischen einem Agenten und einem Nutzer. Threads können verwendet werden, um den Fortschritt einer Unterhaltung zu verfolgen, Kontextinformationen zu speichern und den Zustand der Interaktion zu verwalten. Hier ist ein Beispiel für einen Thread:

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

    Im vorherigen Code wird ein Thread erstellt. Danach wird eine Nachricht an den Thread gesendet. Durch den Aufruf von `create_and_process_run` wird der Agent gebeten, Arbeit im Thread auszuführen. Schließlich werden die Nachrichten abgerufen und protokolliert, um die Antwort des Agenten zu sehen. Die Nachrichten zeigen den Fortschritt der Konversation zwischen dem Nutzer und dem Agenten an. Es ist auch wichtig zu verstehen, dass die Nachrichten verschiedene Typen haben können, wie Text, Bild oder Datei — das heißt, die Arbeit des Agenten kann beispielsweise in einer Bild- oder Textantwort resultieren. Als Entwickler können Sie diese Informationen dann weiterverarbeiten oder dem Nutzer präsentieren.

- **Integrates with the Microsoft Agent Framework**. Azure AI Agent Service arbeitet nahtlos mit dem Microsoft Agent Framework zusammen, was bedeutet, dass Sie Agenten mit `AzureAIProjectAgentProvider` erstellen und sie für Produktionsszenarien über den Agent Service bereitstellen können.

**Anwendungsfälle**: Azure AI Agent Service ist für Unternehmensanwendungen konzipiert, die eine sichere, skalierbare und flexible Bereitstellung von KI-Agenten erfordern.

## Wo liegt der Unterschied zwischen diesen Ansätzen?
 
Es scheint Überschneidungen zu geben, aber es gibt einige wichtige Unterschiede in Bezug auf Design, Fähigkeiten und Zielanwendungsfälle:
 
- **Microsoft Agent Framework (MAF)**: Ist ein produktionsbereites SDK zum Erstellen von KI-Agenten. Es bietet eine schlanke API zum Erstellen von Agenten mit Toolaufrufen, Konversationsmanagement und Azure-Identitätsintegration.
- **Azure AI Agent Service**: Ist eine Plattform- und Bereitstellungsdienstleistung in Azure Foundry für Agenten. Es bietet integrierte Konnektivität zu Diensten wie Azure OpenAI, Azure AI Search, Bing Search und Codeausführung.
 
Immer noch nicht sicher, welche Sie wählen sollen?

### Anwendungsfälle
 
Lassen Sie uns sehen, ob wir Ihnen helfen können, indem wir einige gängige Anwendungsfälle durchgehen:
 
> Q: Ich entwickle produktionsfähige KI-Agenten-Anwendungen und möchte schnell loslegen
>
> A: Das Microsoft Agent Framework ist eine ausgezeichnete Wahl. Es bietet eine einfache, pythonische API über `AzureAIProjectAgentProvider`, mit der Sie Agenten mit Tools und Anweisungen in nur wenigen Codezeilen definieren können.
>
>Q: Ich benötige eine unternehmensgerechte Bereitstellung mit Azure-Integrationen wie Search und Codeausführung
>
> A: Azure AI Agent Service ist die beste Wahl. Es ist ein Plattformdienst, der integrierte Funktionen für mehrere Modelle, Azure AI Search, Bing Search und Azure Functions bietet. Es erleichtert den Aufbau Ihrer Agenten im Foundry-Portal und deren Bereitstellung im großen Maßstab.
> 
> Q: Ich bin immer noch verwirrt, geben Sie mir einfach eine Option
>
> A: Beginnen Sie mit dem Microsoft Agent Framework, um Ihre Agenten zu entwickeln, und nutzen Sie dann Azure AI Agent Service, wenn Sie sie in der Produktion bereitstellen und skalieren müssen. Dieser Ansatz ermöglicht es Ihnen, schnell an Ihrer Agentenlogik zu iterieren und gleichzeitig einen klaren Weg zur Unternehmensbereitstellung zu haben.
 
Fassen wir die wichtigsten Unterschiede in einer Tabelle zusammen:

| Framework | Fokus | Kernkonzepte | Anwendungsfälle |
| --- | --- | --- | --- |
| Microsoft Agent Framework | Vereinfachtes Agenten-SDK mit Toolaufrufen | Agenten, Tools, Azure-Identität | Erstellen von KI-Agenten, Tool-Einsatz, mehrstufige Workflows |
| Azure AI Agent Service | Flexible Modelle, Unternehmenssicherheit, Code-Generierung, Toolaufrufe | Modularität, Zusammenarbeit, Prozessorchestrierung | Sichere, skalierbare und flexible Bereitstellung von KI-Agenten |

## Kann ich meine vorhandenen Azure-Ökosystem-Tools direkt integrieren, oder benötige ich eigenständige Lösungen?
Die Antwort ist ja, Sie können Ihre bestehenden Azure-Ökosystem-Tools direkt mit dem Azure AI Agent Service integrieren, insbesondere da er so entwickelt wurde, dass er nahtlos mit anderen Azure-Diensten zusammenarbeitet. Sie könnten zum Beispiel Bing, Azure AI Search und Azure Functions integrieren. Es gibt außerdem eine tiefe Integration mit Microsoft Foundry.

Das Microsoft Agent Framework integriert sich außerdem mit Azure-Diensten über `AzureAIProjectAgentProvider` und Azure identity, sodass Sie Azure-Dienste direkt aus Ihren Agent-Tools aufrufen können.

## Beispielcodes

- Python: [Agent Framework](./code_samples/02-python-agent-framework.ipynb)
- .NET: [Agent Framework](./code_samples/02-dotnet-agent-framework.md)

## Haben Sie weitere Fragen zu KI-Agenten-Frameworks?

Treten Sie dem [Microsoft Foundry Discord](https://aka.ms/ai-agents/discord) bei, um sich mit anderen Lernenden zu vernetzen, an Sprechstunden teilzunehmen und Antworten auf Ihre Fragen zu KI-Agenten zu erhalten.

## Referenzen

- <a href="https://techcommunity.microsoft.com/blog/azure-ai-services-blog/introducing-azure-ai-agent-service/4298357" target="_blank">Azure Agent Service</a>
- <a href="https://learn.microsoft.com/azure/ai-services/openai/how-to/responses" target="_blank">Microsoft Agent Framework - Azure OpenAI Responses</a>
- <a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Azure AI Agent service</a>

## Vorherige Lektion

[Einführung in KI-Agenten und Anwendungsfälle von Agenten](../01-intro-to-ai-agents/README.md)

## Nächste Lektion

[Agentische Designmuster verstehen](../03-agentic-design-patterns/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
Haftungsausschluss:
Dieses Dokument wurde mithilfe des KI-Übersetzungsdienstes Co-op Translator (https://github.com/Azure/co-op-translator) übersetzt. Obwohl wir uns um Genauigkeit bemühen, beachten Sie bitte, dass automatisierte Übersetzungen Fehler oder Ungenauigkeiten enthalten können. Das Originaldokument in seiner Ausgangssprache sollte als maßgebliche Quelle gelten. Für kritische Informationen wird eine professionelle menschliche Übersetzung empfohlen. Wir haften nicht für Missverständnisse oder Fehlinterpretationen, die sich aus der Verwendung dieser Übersetzung ergeben.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->