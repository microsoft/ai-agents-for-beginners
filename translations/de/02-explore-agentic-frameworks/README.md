[![Erkundung von KI-Agenten-Frameworks](../../../translated_images/de/lesson-2-thumbnail.c65f44c93b8558df.webp)](https://youtu.be/ODwF-EZo_O8?si=1xoy_B9RNQfrYdF7)

> _(Klicken Sie auf das obige Bild, um das Video zu dieser Lektion anzusehen)_

# Erkunde KI-Agenten-Frameworks

KI-Agenten-Frameworks sind Softwareplattformen, die entwickelt wurden, um die Erstellung, Bereitstellung und Verwaltung von KI-Agenten zu vereinfachen. Diese Frameworks bieten Entwicklern vorgefertigte Komponenten, Abstraktionen und Werkzeuge, die die Entwicklung komplexer KI-Systeme erleichtern.

Diese Frameworks helfen Entwicklern, sich auf die einzigartigen Aspekte ihrer Anwendungen zu konzentrieren, indem sie standardisierte Ansätze für häufige Herausforderungen in der Entwicklung von KI-Agenten bereitstellen. Sie verbessern Skalierbarkeit, Zugänglichkeit und Effizienz beim Aufbau von KI-Systemen.

## Einführung 

Diese Lektion behandelt:

- Was sind KI-Agenten-Frameworks und was ermöglichen sie Entwicklern zu erreichen?
- Wie können Teams diese nutzen, um schnell Prototypen zu erstellen, iterieren und die Fähigkeiten ihres Agenten verbessern?
- Was sind die Unterschiede zwischen den von Microsoft erstellten Frameworks und Tools (<a href="https://aka.ms/ai-agents-beginners/ai-agent-service" target="_blank">Microsoft Foundry Agent Service</a> und dem <a href="https://learn.microsoft.com/azure/ai-services/openai/how-to/responses" target="_blank">Microsoft Agent Framework</a>)?
- Kann ich meine bestehenden Tools im Azure-Ökosystem direkt integrieren oder benötige ich eigenständige Lösungen?
- Was ist Microsoft Foundry Agent Service und wie hilft mir das?

## Lernziele

Die Ziele dieser Lektion sind, Ihnen zu helfen, zu verstehen:

- Die Rolle von KI-Agenten-Frameworks in der KI-Entwicklung.
- Wie man KI-Agenten-Frameworks nutzt, um intelligente Agenten zu bauen.
- Wesentliche Fähigkeiten, die durch KI-Agenten-Frameworks ermöglicht werden.
- Die Unterschiede zwischen dem Microsoft Agent Framework und Microsoft Foundry Agent Service.

## Was sind KI-Agenten-Frameworks und was ermöglichen sie Entwicklern?

Traditionelle KI-Frameworks können Ihnen helfen, KI in Ihre Apps zu integrieren und diese Apps auf folgende Weisen zu verbessern:

- **Personalisierung**: KI kann Nutzerverhalten und Vorlieben analysieren, um personalisierte Empfehlungen, Inhalte und Erlebnisse bereitzustellen.
Beispiel: Streaming-Dienste wie Netflix nutzen KI, um Filme und Serien basierend auf dem Sehverlauf vorzuschlagen und so Nutzerbindung und Zufriedenheit zu steigern.
- **Automatisierung und Effizienz**: KI kann repetitive Aufgaben automatisieren, Arbeitsabläufe optimieren und die Betriebseffizienz verbessern.
Beispiel: Kundenservice-Apps verwenden KI-gestützte Chatbots, um häufige Anfragen zu bearbeiten, Reaktionszeiten zu verkürzen und menschliche Mitarbeiter für komplexere Aufgaben freizustellen.
- **Verbessertes Nutzererlebnis**: KI kann das Nutzererlebnis insgesamt verbessern, indem sie intelligente Funktionen wie Spracherkennung, natürliche Sprachverarbeitung und prädiktiven Text bereitstellt.
Beispiel: Virtuelle Assistenten wie Siri und Google Assistant verwenden KI, um Sprachbefehle zu verstehen und darauf zu reagieren, was die Interaktion der Nutzer mit ihren Geräten erleichtert.

### Das klingt doch alles großartig, aber warum brauchen wir dann das KI-Agenten-Framework?

KI-Agenten-Frameworks sind mehr als nur KI-Frameworks. Sie sind darauf ausgelegt, die Erstellung intelligenter Agenten zu ermöglichen, die mit Nutzern, anderen Agenten und der Umgebung interagieren, um spezifische Ziele zu erreichen. Diese Agenten können autonomes Verhalten zeigen, Entscheidungen treffen und sich an veränderte Bedingungen anpassen. Schauen wir uns einige wichtige Fähigkeiten an, die durch KI-Agenten-Frameworks ermöglicht werden:

- **Agentenzusammenarbeit und Koordination**: Ermöglichen die Erstellung mehrerer KI-Agenten, die zusammenarbeiten, kommunizieren und koordinieren können, um komplexe Aufgaben zu lösen.
- **Automatisierung und Verwaltung von Aufgaben**: Bieten Mechanismen zur Automatisierung von mehrstufigen Arbeitsabläufen, Aufgabenverteilung und dynamischem Aufgabenmanagement unter Agenten.
- **Kontextuelles Verständnis und Anpassung**: Statten Agenten mit der Fähigkeit aus, Kontext zu verstehen, sich an wechselnde Umgebungen anzupassen und Entscheidungen basierend auf Echtzeitinformationen zu treffen.

Zusammengefasst erlauben Agenten Ihnen, mehr zu tun, Automatisierung auf ein neues Niveau zu heben und intelligentere Systeme zu schaffen, die sich an die Umgebung anpassen und daraus lernen können.

## Wie kann man schnell Prototypen erstellen, iterieren und die Fähigkeiten des Agenten verbessern?

Dies ist ein schnelllebiges Gebiet, aber es gibt einige gemeinsame Elemente in den meisten KI-Agenten-Frameworks, die Ihnen helfen können, schnell Prototypen zu entwickeln und zu iterieren, nämlich modulare Komponenten, kollaborative Werkzeuge und Lernen in Echtzeit. Lassen Sie uns diese näher betrachten:

- **Verwenden Sie modulare Komponenten**: KI-SDKs bieten vorgefertigte Komponenten wie KI- und Speicheranschlüsse, Funktionsaufrufe über natürliche Sprache oder Code-Plugins, Vorlagen für Eingabeaufforderungen und mehr.
- **Nutzen Sie kollaborative Werkzeuge**: Entwerfen Sie Agenten mit spezifischen Rollen und Aufgaben, sodass sie kollaborative Arbeitsabläufe testen und verfeinern können.
- **Lernen in Echtzeit**: Implementieren Sie Feedback-Schleifen, bei denen Agenten aus Interaktionen lernen und ihr Verhalten dynamisch anpassen.

### Verwenden Sie modulare Komponenten

SDKs wie das Microsoft Agent Framework bieten vorgefertigte Komponenten wie KI-Anschlüsse, Tool-Definitionen und Agentenmanagement.

**Wie Teams diese nutzen können**: Teams können diese Komponenten schnell zusammenstellen, um einen funktionalen Prototyp zu erstellen, ohne bei Null anfangen zu müssen, was schnelle Experimente und Iterationen erlaubt.

**Wie es in der Praxis funktioniert**: Sie können einen vorgefertigten Parser verwenden, um Informationen aus Benutzereingaben zu extrahieren, ein Speichermodul zur Datenablage und -abruf verwenden und einen Eingabegenerator, um mit Nutzern zu interagieren, alles ohne diese Komponenten selbst entwickeln zu müssen.

**Beispielcode**: Schauen wir uns ein Beispiel an, wie Sie das Microsoft Agent Framework mit `FoundryChatClient` nutzen können, damit das Modell auf Benutzereingaben mit Funktionsaufrufen reagiert:

``` python
# Microsoft Agent Framework Python Beispiel

import asyncio
import os

from agent_framework import tool
from agent_framework.foundry import FoundryChatClient
from azure.identity import AzureCliCredential


# Definieren Sie eine Beispiel-Tool-Funktion zur Reisebuchung
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
    # Beispielausgabe: Ihr Flug nach New York am 1. Januar 2025 wurde erfolgreich gebucht. Gute Reise! ✈️🗽


if __name__ == "__main__":
    asyncio.run(main())
```

Was Sie an diesem Beispiel sehen können, ist, wie Sie einen vorgefertigten Parser nutzen, um wichtige Informationen aus Benutzereingaben zu extrahieren, wie den Ursprung, das Ziel und das Datum einer Flugbuchungsanfrage. Dieser modulare Ansatz ermöglicht es Ihnen, sich auf die Logik auf höherer Ebene zu konzentrieren.

### Nutzen Sie kollaborative Werkzeuge

Frameworks wie das Microsoft Agent Framework erleichtern die Erstellung mehrerer Agenten, die zusammenarbeiten können.

**Wie Teams diese nutzen können**: Teams können Agenten mit spezifischen Rollen und Aufgaben erstellen, was es ermöglicht, kollaborative Arbeitsabläufe zu testen, zu verfeinern und die Gesamtsystemeffizienz zu steigern.

**Wie es in der Praxis funktioniert**: Sie können ein Team von Agenten erschaffen, bei dem jeder Agent eine spezialisierte Funktion hat, wie Datenabruf, Analyse oder Entscheidungsfindung. Diese Agenten können kommunizieren und Informationen teilen, um ein gemeinsames Ziel zu erreichen, z.B. eine Nutzeranfrage zu beantworten oder eine Aufgabe abzuschließen.

**Beispielcode (Microsoft Agent Framework)**:

```python
# Erstellen mehrerer Agenten, die zusammenarbeiten, unter Verwendung des Microsoft Agent Frameworks

import os
from agent_framework.foundry import FoundryChatClient
from azure.identity import AzureCliCredential

provider = FoundryChatClient(
    project_endpoint=os.environ["AZURE_AI_PROJECT_ENDPOINT"],
    model=os.environ["AZURE_AI_MODEL_DEPLOYMENT_NAME"],
    credential=AzureCliCredential(),
)

# Datenabruf-Agent
agent_retrieve = provider.as_agent(
    name="dataretrieval",
    instructions="Retrieve relevant data using available tools.",
    tools=[retrieve_tool],
)

# Datenanalyse-Agent
agent_analyze = provider.as_agent(
    name="dataanalysis",
    instructions="Analyze the retrieved data and provide insights.",
    tools=[analyze_tool],
)

# Agenten nacheinander für eine Aufgabe ausführen
retrieval_result = await agent_retrieve.run("Retrieve sales data for Q4")
analysis_result = await agent_analyze.run(f"Analyze this data: {retrieval_result}")
print(analysis_result)
```

Was Sie im vorherigen Code sehen, ist, wie Sie eine Aufgabe erstellen können, die mehrere Agenten umfasst, die zusammenarbeiten, um Daten zu analysieren. Jeder Agent führt eine spezifische Funktion aus und die Aufgabe wird durch die Koordination der Agenten umgesetzt, um das gewünschte Ergebnis zu erzielen. Durch das Erstellen dedizierter Agenten mit spezialisierten Rollen können Sie die Effizienz und Leistung der Aufgabe verbessern.

### Lernen in Echtzeit

Fortgeschrittene Frameworks bieten Fähigkeiten für kontextuelles Verständnis und Anpassung in Echtzeit.

**Wie Teams diese nutzen können**: Teams können Feedback-Schleifen implementieren, bei denen Agenten aus Interaktionen lernen und ihr Verhalten dynamisch anpassen, was zu kontinuierlicher Verbesserung und Verfeinerung der Fähigkeiten führt.

**Wie es in der Praxis funktioniert**: Agenten können Nutzerfeedback, Umgebungsdaten und Aufgabenergebnisse analysieren, um ihre Wissensbasis zu aktualisieren, Entscheidungsalgorithmen anzupassen und die Leistung im Laufe der Zeit zu verbessern. Dieser iterative Lernprozess ermöglicht es Agenten, sich an veränderte Bedingungen und Nutzerpräferenzen anzupassen und die Gesamteffektivität des Systems zu steigern.

## Was sind die Unterschiede zwischen dem Microsoft Agent Framework und Microsoft Foundry Agent Service?

Es gibt viele Ansatzpunkte für einen Vergleich, aber sehen wir uns einige wesentliche Unterschiede hinsichtlich Design, Fähigkeiten und Zielanwendungen an:

## Microsoft Agent Framework (MAF)

Das Microsoft Agent Framework bietet ein schlankes SDK zum Erstellen von KI-Agenten mit `FoundryChatClient`. Es ermöglicht Entwicklern, Agenten zu erschaffen, die Azure OpenAI-Modelle mit eingebauten Funktionsaufrufen, Gesprächsverwaltung und Unternehmenssicherheit über die Azure-Identität nutzen.

**Anwendungsfälle**: Aufbau produktionsreifer KI-Agenten mit Tool-Nutzung, mehrstufigen Arbeitsabläufen und Unternehmensintegrationsszenarien.

Hier sind einige wichtige Kernkonzepte des Microsoft Agent Framework:

- **Agenten**. Ein Agent wird über `FoundryChatClient` erstellt und mit Namen, Anweisungen und Tools konfiguriert. Der Agent kann:
  - **Benutzernachrichten verarbeiten** und Antworten mit Azure OpenAI-Modellen generieren.
  - **Tools automatisch aufrufen** basierend auf dem Gesprächskontext.
  - **Gesprächszustand verwalten** über mehrere Interaktionen hinweg.

  Hier ist ein Codeausschnitt, der zeigt, wie man einen Agenten erstellt:

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

- **Tools**. Das Framework unterstützt die Definition von Tools als Python-Funktionen, die der Agent automatisch aufrufen kann. Tools werden bei der Agentenerstellung registriert:

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

- **Multi-Agenten-Koordination**. Sie können mehrere Agenten mit unterschiedlichen Spezialisierungen erstellen und deren Arbeit koordinieren:

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

- **Azure-Identitätsintegration**. Das Framework nutzt `AzureCliCredential` (oder `DefaultAzureCredential`) für sichere, schlüssellose Authentifizierung, wodurch die Verwaltung von API-Schlüsseln entfällt.

## Microsoft Foundry Agent Service

Microsoft Foundry Agent Service ist eine neuere Ergänzung, eingeführt auf der Microsoft Ignite 2024. Es ermöglicht die Entwicklung und Bereitstellung von KI-Agenten mit flexibleren Modellen, wie dem direkten Aufruf von Open-Source-LLMs wie Llama 3, Mistral und Cohere.

Microsoft Foundry Agent Service bietet stärkere Sicherheitsmechanismen für Unternehmen und Datenaufbewahrungsmethoden, was es für unternehmerische Anwendungen geeignet macht.

Es funktioniert direkt mit dem Microsoft Agent Framework zusammen, um Agenten zu erstellen und bereitzustellen.

Dieser Service befindet sich aktuell in der Public Preview und unterstützt Python und C# zum Erstellen von Agenten.

Mit dem Microsoft Foundry Agent Service Python SDK können wir einen Agenten mit einem benutzerdefinierten Tool erstellen:

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

### Kernkonzepte

Microsoft Foundry Agent Service umfasst folgende Kernkonzepte:

- **Agent**. Microsoft Foundry Agent Service integriert sich in Microsoft Foundry. Innerhalb von Microsoft Foundry agiert ein KI-Agent als „intelligenter“ Microservice, der verwendet werden kann, um Fragen zu beantworten (RAG), Aktionen auszuführen oder Workflows vollständig zu automatisieren. Er erreicht dies durch die Kombination der Kraft generativer KI-Modelle mit Tools, die ihm erlauben, auf reale Datenquellen zuzugreifen und mit ihnen zu interagieren. Hier ein Beispiel für einen Agenten:

    ```python
    agent = project_client.agents.create_agent(
        model="gpt-5-mini",
        name="my-agent",
        instructions="You are helpful agent",
        tools=code_interpreter.definitions,
        tool_resources=code_interpreter.resources,
    )
    ```

    In diesem Beispiel wird ein Agent mit dem Modell `gpt-5-mini`, dem Namen `my-agent` und den Anweisungen `You are helpful agent` erstellt. Der Agent ist mit Tools und Ressourcen ausgestattet, um Aufgaben der Code-Interpretation auszuführen.

- **Thread und Nachrichten**. Der Thread ist ein weiteres wichtiges Konzept. Er repräsentiert ein Gespräch oder eine Interaktion zwischen einem Agenten und einem Nutzer. Threads können verwendet werden, um den Fortschritt eines Gesprächs zu verfolgen, Kontextinformationen zu speichern und den Status der Interaktion zu verwalten. Hier ein Beispiel für einen Thread:

    ```python
    thread = project_client.agents.create_thread()
    message = project_client.agents.create_message(
        thread_id=thread.id,
        role="user",
        content="Could you please create a bar chart for the operating profit using the following data and provide the file to me? Company A: $1.2 million, Company B: $2.5 million, Company C: $3.0 million, Company D: $1.8 million",
    )
    
    # Fordern Sie den Agenten auf, an dem Thread zu arbeiten
    run = project_client.agents.create_and_process_run(thread_id=thread.id, agent_id=agent.id)
    
    # Alle Nachrichten abrufen und protokollieren, um die Antwort des Agenten zu sehen
    messages = project_client.agents.list_messages(thread_id=thread.id)
    print(f"Messages: {messages}")
    ```

    Im vorherigen Code wird ein Thread erstellt. Danach wird eine Nachricht an den Thread gesendet. Durch den Aufruf von `create_and_process_run` wird der Agent aufgefordert, Arbeit im Thread auszuführen. Schließlich werden die Nachrichten abgerufen und protokolliert, um die Antwort des Agenten zu sehen. Die Nachrichten zeigen den Fortschritt des Gesprächs zwischen Nutzer und Agent. Es ist auch wichtig zu verstehen, dass die Nachrichten verschiedene Typen haben können, wie Text, Bild oder Datei - das heißt, die Arbeit des Agenten hat beispielsweise ein Bild oder eine Textantwort erzeugt. Als Entwickler können Sie diese Informationen dann nutzen, um die Antwort weiterzuverarbeiten oder dem Nutzer darzustellen.

- **Integration mit dem Microsoft Agent Framework**. Microsoft Foundry Agent Service arbeitet nahtlos mit dem Microsoft Agent Framework zusammen, was bedeutet, dass Sie Agenten mit `FoundryChatClient` erstellen und sie über den Agent Service für Produktionsszenarien bereitstellen können.

**Anwendungsfälle**: Microsoft Foundry Agent Service ist für Unternehmensanwendungen gedacht, die sichere, skalierbare und flexible Bereitstellung von KI-Agenten erfordern.

## Was ist der Unterschied zwischen diesen Ansätzen?
 
Es gibt zwar Überschneidungen, aber einige wesentliche Unterschiede hinsichtlich Design, Fähigkeiten und Zielanwendungen:
 
- **Microsoft Agent Framework (MAF)**: Ein produktionsreifes SDK zum Erstellen von KI-Agenten. Bietet eine schlanke API zur Erstellung von Agenten mit Funktionsaufrufen, Gesprächsverwaltung und Azure-Identitätsintegration.
- **Microsoft Foundry Agent Service**: Eine Plattform- und Bereitstellungsdienstleistung in Microsoft Foundry für Agenten. Bietet integrierte Anbindungen an Dienste wie Azure OpenAI, Azure AI Search, Bing Search und Codeausführung.
 
Noch unsicher, welches Sie wählen sollen?

### Anwendungsfälle
 
Schauen wir, ob wir Ihnen helfen können, indem wir einige gängige Anwendungsfälle durchgehen:
 
> F: Ich entwickle produktionsreife KI-Agenten-Anwendungen und möchte schnell starten
>

>A: Das Microsoft Agent Framework ist dafür eine großartige Wahl. Es bietet eine einfache, Python-ähnliche API über `FoundryChatClient`, mit der Sie Agenten mit Tools und Anweisungen in nur wenigen Codezeilen definieren können.

>F: Ich brauche eine unternehmensgerechte Bereitstellung mit Azure-Integrationen wie Suche und Codeausführung
>
> A: Microsoft Foundry Agent Service ist hier die beste Wahl. Es ist ein Plattformdienst mit integrierten Funktionen für mehrere Modelle, Azure AI Search, Bing Search und Azure Functions. Es ermöglicht Ihnen, Ihre Agenten im Foundry-Portal zu erstellen und skalierbar bereitzustellen.
 
> F: Ich bin noch verwirrt, geben Sie mir einfach eine Option
>
> A: Beginnen Sie mit dem Microsoft Agent Framework, um Ihre Agenten zu bauen, und nutzen Sie dann Microsoft Foundry Agent Service, wenn Sie sie in der Produktion bereitstellen und skalieren müssen. Dieser Ansatz erlaubt schnelle Iterationen an der Agentenlogik und bietet gleichzeitig einen klaren Weg zur Unternehmensbereitstellung.
 
Fassen wir die wichtigsten Unterschiede in einer Tabelle zusammen:

| Framework | Schwerpunkt | Kernkonzepte | Anwendungsfälle |
| --- | --- | --- | --- |
| Microsoft Agent Framework | Schlankes Agenten-SDK mit Funktionsaufrufen | Agenten, Tools, Azure-Identität | Erstellung von KI-Agenten, Tool-Nutzung, mehrstufige Arbeitsabläufe |
| Microsoft Foundry Agent Service | Flexible Modelle, Unternehmenssicherheit, Codegenerierung, Toolaufrufe | Modularität, Zusammenarbeit, Prozess-Orchestrierung | Sichere, skalierbare und flexible Bereitstellung von KI-Agenten |

## Kann ich meine bestehenden Azure-Ökosystem-Tools direkt integrieren oder benötige ich eigenständige Lösungen?


Die Antwort lautet ja, Sie können Ihre bestehenden Azure-Ökosystem-Tools direkt mit dem Microsoft Foundry Agent Service integrieren, insbesondere da dieser entwickelt wurde, um nahtlos mit anderen Azure-Diensten zusammenzuarbeiten. Sie könnten zum Beispiel Bing, Azure AI Search und Azure Functions integrieren. Es gibt auch eine tiefgehende Integration mit Microsoft Foundry.

Das Microsoft Agent Framework integriert sich auch über `FoundryChatClient` und Azure-Identität mit Azure-Diensten, sodass Sie Azure-Dienste direkt aus Ihren Agent-Tools aufrufen können.

## Beispielcodes

- Python: [Agent Framework (Microsoft Foundry)](./code_samples/02-python-agent-framework.ipynb)
- Python: [Agent Framework (Azure OpenAI Responses API)](./code_samples/02-python-agent-framework-azure-openai.ipynb)
- .NET: [Agent Framework](./code_samples/02-dotnet-agent-framework.md)

## Haben Sie weitere Fragen zu AI Agent Frameworks?

Treten Sie dem [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D) bei, um andere Lernende zu treffen, an Sprechstunden teilzunehmen und Antworten auf Ihre Fragen zu AI Agents zu erhalten.

## Verweise

- <a href="https://techcommunity.microsoft.com/blog/azure-ai-services-blog/introducing-azure-ai-agent-service/4298357" target="_blank">Azure Agent Service</a>
- <a href="https://learn.microsoft.com/azure/ai-services/openai/how-to/responses" target="_blank">Microsoft Agent Framework - Azure OpenAI Responses</a>
- <a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Microsoft Foundry Agent Service</a>

## Vorherige Lektion

[Einführung in AI Agents und Anwendungsfälle für Agenten](../01-intro-to-ai-agents/README.md)

## Nächste Lektion

[Verstehen von agentenbasierten Designmustern](../03-agentic-design-patterns/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Haftungsausschluss**:
Dieses Dokument wurde mit dem KI-Übersetzungsdienst [Co-op Translator](https://github.com/Azure/co-op-translator) übersetzt. Obwohl wir uns um Genauigkeit bemühen, beachten Sie bitte, dass automatisierte Übersetzungen Fehler oder Ungenauigkeiten enthalten können. Das Originaldokument in seiner Ursprungssprache gilt als maßgebliche Quelle. Bei kritischen Informationen wird eine professionelle menschliche Übersetzung empfohlen. Wir übernehmen keine Haftung für Missverständnisse oder Fehlinterpretationen, die aus der Verwendung dieser Übersetzung entstehen.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->