[![Erkundung von KI-Agenten-Frameworks](../../../translated_images/de/lesson-2-thumbnail.c65f44c93b8558df.webp)](https://youtu.be/ODwF-EZo_O8?si=1xoy_B9RNQfrYdF7)

> _(Klicken Sie auf das obige Bild, um das Video dieser Lektion anzusehen)_

# KI-Agenten-Frameworks erkunden

KI-Agenten-Frameworks sind Softwareplattformen, die entwickelt wurden, um die Erstellung, Bereitstellung und Verwaltung von KI-Agenten zu vereinfachen. Diese Frameworks bieten Entwicklern vorgefertigte Komponenten, Abstraktionen und Werkzeuge, die die Entwicklung komplexer KI-Systeme rationalisieren.

Diese Frameworks helfen Entwicklern, sich auf die einzigartigen Aspekte ihrer Anwendungen zu konzentrieren, indem sie standardisierte Ansätze für häufige Herausforderungen in der Entwicklung von KI-Agenten bereitstellen. Sie verbessern Skalierbarkeit, Zugänglichkeit und Effizienz beim Aufbau von KI-Systemen.

## Einführung 

Diese Lektion behandelt:

- Was sind KI-Agenten-Frameworks und was ermöglichen sie Entwicklern?
- Wie können Teams diese nutzen, um schnell Prototypen zu erstellen, zu iterieren und die Fähigkeiten ihrer Agenten zu verbessern?
- Was sind die Unterschiede zwischen den von Microsoft erstellten Frameworks und Tools (<a href="https://aka.ms/ai-agents-beginners/ai-agent-service" target="_blank">Microsoft Foundry Agent Service</a> und <a href="https://learn.microsoft.com/azure/ai-services/openai/how-to/responses" target="_blank">Microsoft Agent Framework</a>)?
- Kann ich meine bestehenden Azure-Ökosystem-Tools direkt integrieren oder benötige ich eigenständige Lösungen?
- Was ist der Microsoft Foundry Agent Service und wie unterstützt er mich?

## Lernziele

Die Ziele dieser Lektion sind, Ihnen zu helfen:

- Die Rolle von KI-Agenten-Frameworks in der KI-Entwicklung zu verstehen.
- Wie man KI-Agenten-Frameworks nutzt, um intelligente Agenten zu bauen.
- Zentrale Fähigkeiten, die durch KI-Agenten-Frameworks ermöglicht werden.
- Die Unterschiede zwischen Microsoft Agent Framework und Microsoft Foundry Agent Service.

## Was sind KI-Agenten-Frameworks und was ermöglichen sie Entwicklern?

Traditionelle KI-Frameworks können Ihnen helfen, KI in Ihre Apps zu integrieren und diese Apps auf folgende Weise zu verbessern:

- **Personalisierung**: KI kann das Nutzerverhalten und Vorlieben analysieren, um personalisierte Empfehlungen, Inhalte und Erlebnisse bereitzustellen.
Beispiel: Streamingdienste wie Netflix nutzen KI, um Filme und Serien basierend auf dem Betrachtungsverlauf vorzuschlagen, was die Nutzerbindung und Zufriedenheit erhöht.
- **Automatisierung und Effizienz**: KI kann repetitive Aufgaben automatisieren, Arbeitsabläufe optimieren und die betriebliche Effizienz verbessern.
Beispiel: Kundendienst-Apps setzen KI-gestützte Chatbots ein, um häufige Anfragen zu bearbeiten, Antwortzeiten zu verkürzen und menschliche Agenten für komplexere Probleme freizustellen.
- **Verbessertes Benutzererlebnis**: KI kann das gesamte Nutzererlebnis durch intelligente Funktionen wie Spracherkennung, natürliche Sprachverarbeitung und vorausschauende Texteingabe verbessern.
Beispiel: Virtuelle Assistenten wie Siri und Google Assistant verwenden KI, um Sprachbefehle zu verstehen und zu beantworten, was die Interaktion mit Geräten erleichtert.

### Das klingt alles großartig, aber warum brauchen wir das KI-Agenten-Framework?

KI-Agenten-Frameworks sind mehr als nur KI-Frameworks. Sie sind darauf ausgelegt, die Erstellung intelligenter Agenten zu ermöglichen, die mit Nutzern, anderen Agenten und der Umgebung interagieren können, um spezifische Ziele zu erreichen. Diese Agenten können autonom handeln, Entscheidungen treffen und sich an veränderte Bedingungen anpassen. Schauen wir uns einige zentrale Fähigkeiten an, die durch KI-Agenten-Frameworks ermöglicht werden:

- **Agentenzusammenarbeit und Koordination**: Ermöglichen die Erstellung mehrerer KI-Agenten, die zusammenarbeiten, kommunizieren und koordinieren, um komplexe Aufgaben zu lösen.
- **Automatisierung und Verwaltung von Aufgaben**: Bieten Mechanismen zur Automatisierung mehrstufiger Arbeitsabläufe, Aufgabenverteilung und dynamischem Aufgabenmanagement zwischen Agenten.
- **Kontextuelles Verständnis und Anpassungsfähigkeit**: Statten Agenten mit der Fähigkeit aus, Kontext zu verstehen, sich an veränderte Umgebungen anzupassen und basierend auf Echtzeitinformationen Entscheidungen zu treffen.

Zusammenfassend ermöglichen Agenten Ihnen, mehr zu tun, Automatisierung auf die nächste Stufe zu heben und intelligentere Systeme zu schaffen, die sich an ihre Umgebung anpassen und daraus lernen können.

## Wie kann man schnell Prototypen erstellen, iterieren und die Fähigkeiten des Agenten verbessern?

Dieses Feld entwickelt sich schnell, aber es gibt einige Bestandteile, die bei den meisten KI-Agenten-Frameworks üblich sind und Ihnen helfen, schnell zu prototypisieren und zu iterieren, nämlich modulare Komponenten, kollaborative Werkzeuge und Echtzeit-Lernen. Schauen wir uns diese an:

- **Verwenden Sie modulare Komponenten**: KI-SDKs bieten vorgefertigte Komponenten wie KI- und Speicherkonnektoren, Funktionsaufrufe mittels natürlicher Sprache oder Code-Plugins, Prompt-Vorlagen und mehr.
- **Nutzen Sie kollaborative Werkzeuge**: Entwerfen Sie Agenten mit spezifischen Rollen und Aufgaben, die das Testen und Verfeinern kooperativer Arbeitsabläufe ermöglichen.
- **Lernen in Echtzeit**: Implementieren Sie Feedback-Schleifen, bei denen Agenten aus Interaktionen lernen und ihr Verhalten dynamisch anpassen.

### Nutzung modularer Komponenten

SDKs wie das Microsoft Agent Framework bieten vorgefertigte Komponenten wie KI-Konnektoren, Werkzeugdefinitionen und Agentenverwaltung.

**Wie Teams diese nutzen können**: Teams können diese Komponenten schnell zusammenstellen, um einen funktionsfähigen Prototyp zu erstellen, ohne bei Null anfangen zu müssen, was schnelles Experimentieren und Iterieren ermöglicht.

**So funktioniert es in der Praxis**: Sie können einen vorgefertigten Parser verwenden, um Informationen aus Nutzereingaben zu extrahieren, ein Speichermodul, um Daten zu speichern und abzurufen, und einen Prompt-Generator, um mit Nutzern zu interagieren – alles ohne, diese Komponenten selbst entwickeln zu müssen.

**Beispielcode**. Schauen wir uns ein Beispiel an, wie das Microsoft Agent Framework mit `FoundryChatClient` genutzt wird, damit das Modell auf Nutzereingaben mit Werkzeugaufrufen reagieren kann:

``` python
# Microsoft Agent Framework Python Beispiel

import asyncio
import os

from agent_framework import tool
from agent_framework.foundry import FoundryChatClient
from azure.identity import AzureCliCredential


# Definieren Sie eine Beispiel-Toolfunktion zur Buchung von Reisen
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

Was Sie an diesem Beispiel sehen können, ist, wie Sie einen vorgefertigten Parser nutzen, um wichtige Informationen aus der Nutzereingabe zu extrahieren, wie beispielsweise den Abflugort, Zielort und das Datum einer Flugbuchungsanfrage. Dieser modulare Ansatz ermöglicht es, sich auf die übergeordnete Logik zu konzentrieren.

### Nutzung kollaborativer Werkzeuge

Frameworks wie das Microsoft Agent Framework erleichtern die Erstellung mehrerer Agenten, die zusammenarbeiten können.

**Wie Teams diese nutzen können**: Teams können Agenten mit spezifischen Rollen und Aufgaben entwerfen, was das Testen und Verfeinern kollaborativer Arbeitsabläufe ermöglicht und so die Gesamteffizienz des Systems verbessert.

**So funktioniert es in der Praxis**: Sie können ein Team von Agenten erstellen, bei dem jeder Agent eine spezialisierte Funktion hat, wie Datenerfassung, Analyse oder Entscheidungsfindung. Diese Agenten können kommunizieren und Informationen teilen, um ein gemeinsames Ziel zu erreichen, beispielsweise eine Nutzeranfrage zu beantworten oder eine Aufgabe zu erledigen.

**Beispielcode (Microsoft Agent Framework)**:

```python
# Erstellen mehrerer Agenten, die zusammen mit dem Microsoft Agent Framework arbeiten

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

Im vorherigen Code sehen Sie, wie eine Aufgabe erstellt wird, die mehrere Agenten zusammenarbeiten lässt, um Daten zu analysieren. Jeder Agent führt eine spezifische Funktion aus, und die Aufgabe wird durch Koordination der Agenten ausgeführt, um das gewünschte Ergebnis zu erreichen. Durch die Erstellung dedizierter Agenten mit spezialisierten Rollen können Sie die Effizienz und Leistung der Aufgaben verbessern.

### Lernen in Echtzeit

Fortgeschrittene Frameworks bieten Fähigkeiten für kontextuelles Verständnis und Anpassung in Echtzeit.

**Wie Teams diese nutzen können**: Teams können Feedback-Schleifen implementieren, bei denen Agenten aus Interaktionen lernen und ihr Verhalten dynamisch anpassen, was zu kontinuierlicher Verbesserung und Verfeinerung der Fähigkeiten führt.

**So funktioniert es in der Praxis**: Agenten können Nutzerfeedback, Umweltdaten und Arbeitsergebnisse analysieren, um ihre Wissensbasis zu aktualisieren, Entscheidungsalgorithmen anzupassen und ihre Leistung im Laufe der Zeit zu verbessern. Dieser iterative Lernprozess ermöglicht es Agenten, sich an veränderte Bedingungen und Nutzerpräferenzen anzupassen und die Gesamteffektivität des Systems zu steigern.

## Was sind die Unterschiede zwischen Microsoft Agent Framework und Microsoft Foundry Agent Service?

Es gibt viele Vergleichsmöglichkeiten, aber werfen wir einen Blick auf einige Schlüsseldifferenzen hinsichtlich Design, Fähigkeiten und Zielanwendungen:

## Microsoft Agent Framework (MAF)

Das Microsoft Agent Framework bietet ein schlankes SDK zum Erstellen von KI-Agenten mit `FoundryChatClient`. Es ermöglicht Entwicklern, Agenten zu erstellen, die Azure OpenAI-Modelle mit eingebautem Werkzeugaufruf, Gesprächsverwaltung und unternehmensgerechter Sicherheit über Azure-Identität nutzen.

**Anwendungsfälle**: Erstellung produktionsbereiter KI-Agenten mit Werkzeugnutzung, mehrstufigen Arbeitsabläufen und Integrationsszenarien für Unternehmen.

Hier sind einige wichtige Kernkonzepte des Microsoft Agent Framework:

- **Agenten**. Ein Agent wird über `FoundryChatClient` erstellt und mit Name, Anweisungen und Werkzeugen konfiguriert. Der Agent kann:
  - **Nutzernachrichten verarbeiten** und Antworten mit Azure OpenAI-Modellen generieren.
  - **Werkzeuge aufrufen** automatisch basierend auf dem Gesprächskontext.
  - **Den Gesprächszustand verwalten** über mehrere Interaktionen hinweg.

  Hier ein Codeausschnitt, der zeigt, wie man einen Agenten erstellt:

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

- **Werkzeuge**. Das Framework unterstützt die Definition von Werkzeugen als Python-Funktionen, die der Agent automatisch aufrufen kann. Werkzeuge werden beim Erstellen des Agenten registriert:

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

- **Integration der Azure-Identität**. Das Framework verwendet `AzureCliCredential` (oder `DefaultAzureCredential`) für sichere, schlüsselose Authentifizierung, um die direkte Verwaltung von API-Schlüsseln zu vermeiden.

## Microsoft Foundry Agent Service

Microsoft Foundry Agent Service ist eine neuere Ergänzung, vorgestellt auf der Microsoft Ignite 2024. Es ermöglicht die Entwicklung und Bereitstellung von KI-Agenten mit flexibleren Modellen, etwa durch direkten Aufruf von Open-Source-LLMs wie Llama 3, Mistral und Cohere.

Microsoft Foundry Agent Service bietet stärkere Sicherheitsmechanismen für Unternehmen und Methoden zur Datenspeicherung, wodurch es sich gut für Unternehmensanwendungen eignet.

Es funktioniert „out-of-the-box“ mit dem Microsoft Agent Framework zum Erstellen und Bereitstellen von Agenten.

Dieser Service befindet sich derzeit in der öffentlichen Vorschau und unterstützt Python und C# für die Agentenerstellung.

Mit dem Microsoft Foundry Agent Service Python SDK können wir einen Agenten mit einem benutzerdefinierten Werkzeug erstellen:

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
        model="gpt-4.1-mini",
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

Microsoft Foundry Agent Service verfügt über folgende Kernkonzepte:

- **Agent**. Microsoft Foundry Agent Service ist in Microsoft Foundry integriert. Innerhalb von Microsoft Foundry agiert ein KI-Agent als „intelligenter“ Microservice, der genutzt werden kann, um Fragen zu beantworten (RAG), Aktionen auszuführen oder komplette Arbeitsabläufe zu automatisieren. Dies erreicht er durch die Kombination der Leistungsfähigkeit generativer KI-Modelle mit Werkzeugen, die ihm den Zugriff auf und die Interaktion mit realen Datenquellen ermöglichen. Hier ein Beispiel für einen Agenten:

    ```python
    agent = project_client.agents.create_agent(
        model="gpt-4.1-mini",
        name="my-agent",
        instructions="You are helpful agent",
        tools=code_interpreter.definitions,
        tool_resources=code_interpreter.resources,
    )
    ```

    In diesem Beispiel wird ein Agent mit dem Modell `gpt-4.1-mini`, dem Namen `my-agent` und den Anweisungen „You are helpful agent“ erstellt. Der Agent ist mit Werkzeugen und Ressourcen ausgestattet, um Aufgaben der Code-Interpretation durchzuführen.

- **Thread und Nachrichten**. Der Thread ist ein weiteres wichtiges Konzept. Er repräsentiert eine Unterhaltung oder Interaktion zwischen einem Agenten und einem Nutzer. Threads können genutzt werden, um den Fortschritt eines Gesprächs zu verfolgen, Kontextinformationen zu speichern und den Status der Interaktion zu verwalten. Hier ein Beispiel für einen Thread:

    ```python
    thread = project_client.agents.create_thread()
    message = project_client.agents.create_message(
        thread_id=thread.id,
        role="user",
        content="Could you please create a bar chart for the operating profit using the following data and provide the file to me? Company A: $1.2 million, Company B: $2.5 million, Company C: $3.0 million, Company D: $1.8 million",
    )
    
    # Fordern Sie den Agenten auf, Arbeiten am Thread durchzuführen
    run = project_client.agents.create_and_process_run(thread_id=thread.id, agent_id=agent.id)
    
    # Alle Nachrichten abrufen und protokollieren, um die Antwort des Agenten zu sehen
    messages = project_client.agents.list_messages(thread_id=thread.id)
    print(f"Messages: {messages}")
    ```

    Im vorherigen Code wird ein Thread erstellt. Danach wird dem Thread eine Nachricht gesendet. Durch den Aufruf von `create_and_process_run` wird der Agent gebeten, im Thread zu arbeiten. Schließlich werden die Nachrichten abgerufen und protokolliert, um die Antwort des Agenten zu sehen. Die Nachrichten zeigen den Fortschritt der Unterhaltung zwischen Nutzer und Agenten an. Es ist auch wichtig zu verstehen, dass die Nachrichten unterschiedliche Typen haben können, wie Text, Bild oder Datei, d.h. die Arbeit des Agenten hat beispielsweise zu einer Bild- oder Textantwort geführt. Als Entwickler können Sie diese Informationen verwenden, um die Antwort weiterzuverarbeiten oder dem Nutzer darzustellen.

- **Integration mit dem Microsoft Agent Framework**. Microsoft Foundry Agent Service arbeitet nahtlos mit dem Microsoft Agent Framework zusammen, was bedeutet, dass Sie Agenten mit `FoundryChatClient` erstellen und über den Agent Service für Produktionsszenarien bereitstellen können.

**Anwendungsfälle**: Microsoft Foundry Agent Service ist für Unternehmensanwendungen ausgelegt, die eine sichere, skalierbare und flexible Bereitstellung von KI-Agenten erfordern.

## Was ist der Unterschied zwischen diesen Ansätzen?
 
Es gibt Überschneidungen, aber einige Schlüsselunterschiede hinsichtlich Design, Fähigkeiten und Zielanwendungen:
 
- **Microsoft Agent Framework (MAF)**: Ist ein produktionsreifes SDK zum Erstellen von KI-Agenten. Es bietet eine schlanke API zum Erstellen von Agenten mit Werkzeugaufruf, Gesprächsverwaltung und Azure-Identitätsintegration.
- **Microsoft Foundry Agent Service**: Ist eine Plattform- und Bereitstellungsdienstleistung in Microsoft Foundry für Agenten. Es bietet integrierte Konnektivität zu Services wie Azure OpenAI, Azure AI Search, Bing Search und Code-Ausführung.
 
Noch unsicher, welches Sie wählen sollen?

### Anwendungsfälle
 
Schauen wir, ob wir Ihnen helfen können, indem wir einige gängige Anwendungsfälle ansehen:
 
> F: Ich entwickle produktionsreife KI-Agenten-Anwendungen und möchte schnell starten
>

>A: Das Microsoft Agent Framework ist eine ausgezeichnete Wahl. Es bietet eine einfache, Python-orientierte API via `FoundryChatClient`, mit der Sie Agenten mit Werkzeugen und Anweisungen in nur wenigen Codezeilen definieren können.

>F: Ich benötige eine unternehmensgerechte Bereitstellung mit Azure-Integrationen wie Search und Code-Ausführung
>
> A: Microsoft Foundry Agent Service passt am besten. Es ist ein Plattformdienst, der integrierte Fähigkeiten für mehrere Modelle, Azure AI Search, Bing Search und Azure Functions bietet. Es erleichtert den Bau Ihrer Agenten im Foundry-Portal und die Bereitstellung in großem Maßstab.
 
> F: Ich bin immer noch verwirrt, geben Sie mir bitte nur eine Option
>
> A: Beginnen Sie mit dem Microsoft Agent Framework, um Ihre Agenten zu entwickeln, und verwenden Sie dann Microsoft Foundry Agent Service, wenn Sie sie produktiv bereitstellen und skalieren müssen. Dieser Ansatz ermöglicht Ihnen schnelles Iterieren der Agentenlogik und bietet gleichzeitig einen klaren Pfad zur Unternehmensbereitstellung.
 
Fassen wir die wichtigsten Unterschiede in einer Tabelle zusammen:

| Framework | Fokus | Kernkonzepte | Anwendungsfälle |
| --- | --- | --- | --- |
| Microsoft Agent Framework | Schlankes Agenten-SDK mit Werkzeugaufruf | Agenten, Werkzeuge, Azure-Identität | Bau von KI-Agenten, Werkzeugnutzung, mehrstufige Arbeitsabläufe |
| Microsoft Foundry Agent Service | Flexible Modelle, Unternehmenssicherheit, Code-Generierung, Werkzeugaufruf | Modularität, Zusammenarbeit, Prozess-Orchestrierung | Sichere, skalierbare und flexible Bereitstellung von KI-Agenten |

## Kann ich meine bestehenden Tools aus dem Azure-Ökosystem direkt integrieren oder benötige ich eigenständige Lösungen?


Die Antwort lautet ja, Sie können Ihre bestehenden Azure-Ökosystem-Tools direkt mit dem Microsoft Foundry Agent Service integrieren, insbesondere da dieser so entwickelt wurde, dass er nahtlos mit anderen Azure-Diensten zusammenarbeitet. Sie könnten zum Beispiel Bing, Azure AI Search und Azure Functions integrieren. Es gibt auch eine tiefe Integration mit Microsoft Foundry.

Das Microsoft Agent Framework integriert sich auch über `FoundryChatClient` und Azure-Identität mit Azure-Diensten, sodass Sie Azure-Dienste direkt von Ihren Agenten-Tools aus aufrufen können.

## Beispielcodes

- Python: [Agent Framework (Microsoft Foundry)](./code_samples/02-python-agent-framework.ipynb)
- Python: [Agent Framework (Azure OpenAI Responses API)](./code_samples/02-python-agent-framework-azure-openai.ipynb)
- .NET: [Agent Framework](./code_samples/02-dotnet-agent-framework.md)

## Haben Sie weitere Fragen zu AI Agent Frameworks?

Treten Sie dem [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D) bei, um andere Lernende zu treffen, Office Hours zu besuchen und Ihre Fragen zu AI Agents beantwortet zu bekommen.

## Referenzen

- <a href="https://techcommunity.microsoft.com/blog/azure-ai-services-blog/introducing-azure-ai-agent-service/4298357" target="_blank">Azure Agent Service</a>
- <a href="https://learn.microsoft.com/azure/ai-services/openai/how-to/responses" target="_blank">Microsoft Agent Framework - Azure OpenAI Responses</a>
- <a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Microsoft Foundry Agent Service</a>

## Vorherige Lektion

[Einführung in AI Agents und Agent Use Cases](../01-intro-to-ai-agents/README.md)

## Nächste Lektion

[Verständnis von Agentic Design Patterns](../03-agentic-design-patterns/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Haftungsausschluss**:
Dieses Dokument wurde mit dem KI-Übersetzungsdienst [Co-op Translator](https://github.com/Azure/co-op-translator) übersetzt. Obwohl wir uns um Genauigkeit bemühen, beachten Sie bitte, dass automatisierte Übersetzungen Fehler oder Ungenauigkeiten enthalten können. Das Originaldokument in seiner Ursprungssprache gilt als maßgebliche Quelle. Bei kritischen Informationen wird eine professionelle menschliche Übersetzung empfohlen. Wir übernehmen keine Haftung für Missverständnisse oder Fehlinterpretationen, die aus der Verwendung dieser Übersetzung entstehen.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->