[![Wie man gute KI-Agenten gestaltet](../../../translated_images/de/lesson-4-thumbnail.546162853cb3daff.webp)](https://youtu.be/vieRiPRx-gI?si=cEZ8ApnT6Sus9rhn)

> _(Klicken Sie auf das obige Bild, um das Video zu dieser Lektion anzusehen)_

# Tool Use Design Pattern

Werkzeuge sind interessant, weil sie KI-Agenten eine breitere Palette von Fähigkeiten ermöglichen. Anstatt dass der Agent nur eine begrenzte Menge von Aktionen ausführen kann, kann er durch das Hinzufügen eines Werkzeugs nun eine Vielzahl von Aktionen durchführen. In diesem Kapitel betrachten wir das Tool Use Design Pattern, das beschreibt, wie KI-Agenten spezifische Werkzeuge nutzen können, um ihre Ziele zu erreichen.

## Einführung

In dieser Lektion möchten wir die folgenden Fragen beantworten:

- Was ist das Tool Use Design Pattern?
- Für welche Anwendungsfälle kann es eingesetzt werden?
- Welche Elemente/Bausteine sind zur Implementierung des Design Patterns erforderlich?
- Welche besonderen Überlegungen sind bei der Verwendung des Tool Use Design Patterns zur Erstellung vertrauenswürdiger KI-Agenten zu berücksichtigen?

## Lernziele

Nach Abschluss dieser Lektion werden Sie in der Lage sein:

- Das Tool Use Design Pattern und seinen Zweck zu definieren.
- Anwendungsfälle zu identifizieren, in denen das Tool Use Design Pattern anwendbar ist.
- Die Schlüsselelemente zur Implementierung des Design Patterns zu verstehen.
- Überlegungen zur Gewährleistung von Vertrauenswürdigkeit bei KI-Agenten, die dieses Design Pattern verwenden, zu erkennen.

## Was ist das Tool Use Design Pattern?

Das **Tool Use Design Pattern** konzentriert sich darauf, LLMs die Fähigkeit zu geben, mit externen Werkzeugen zu interagieren, um bestimmte Ziele zu erreichen. Werkzeuge sind Code, der von einem Agenten ausgeführt werden kann, um Aktionen durchzuführen. Ein Werkzeug kann eine einfache Funktion wie ein Taschenrechner oder ein API-Aufruf zu einem Drittanbieterdienst, z. B. zur Abfrage von Aktienkursen oder Wettervorhersagen, sein. Im Kontext von KI-Agenten sind Werkzeuge so konzipiert, dass sie von Agenten als Reaktion auf **modellgenerierte Funktionsaufrufe** ausgeführt werden.

## Für welche Anwendungsfälle kann es eingesetzt werden?

KI-Agenten können Werkzeuge nutzen, um komplexe Aufgaben zu erledigen, Informationen abzurufen oder Entscheidungen zu treffen. Das Tool Use Design Pattern wird häufig in Szenarien verwendet, die eine dynamische Interaktion mit externen Systemen wie Datenbanken, Webdiensten oder Code-Interpretern erfordern. Diese Fähigkeit ist für eine Reihe unterschiedlicher Anwendungsfälle nützlich, darunter:

- **Dynamische Informationsabfrage:** Agenten können externe APIs oder Datenbanken abfragen, um aktuelle Daten zu erhalten (z. B. Abfragen einer SQLite-Datenbank für Datenanalysen, Abrufen von Aktienkursen oder Wetterinformationen).
- **Code-Ausführung und Interpretation:** Agenten können Code oder Skripte ausführen, um mathematische Probleme zu lösen, Berichte zu erstellen oder Simulationen durchzuführen.
- **Workflow-Automatisierung:** Automatisierung von wiederkehrenden oder mehrstufigen Workflows durch Integration von Werkzeugen wie Task-Schedulern, E-Mail-Diensten oder Datenpipelines.
- **Kundensupport:** Agenten können mit CRM-Systemen, Ticketing-Plattformen oder Wissensdatenbanken interagieren, um Benutzeranfragen zu lösen.
- **Inhaltsgenerierung und -bearbeitung:** Agenten können Werkzeuge wie Grammatikprüfer, Textzusammenfasser oder Bewertungswerkzeuge für die Inhaltsicherheit nutzen, um bei der Inhaltserstellung zu helfen.

## Welche Elemente/Bausteine sind zur Implementierung des Tool Use Design Patterns erforderlich?

Diese Bausteine ermöglichen es dem KI-Agenten, eine breite Palette von Aufgaben auszuführen. Werfen wir einen Blick auf die Schlüsselelemente zur Implementierung des Tool Use Design Patterns:

- **Funktions-/Werkzeugschemata**: Detaillierte Definitionen der verfügbaren Werkzeuge, einschließlich Funktionsname, Zweck, erforderliche Parameter und erwartete Ausgaben. Diese Schemata ermöglichen es dem LLM zu verstehen, welche Werkzeuge verfügbar sind und wie gültige Anfragen konstruiert werden.

- **Funktionsausführungslogik**: Bestimmt, wie und wann Werkzeuge basierend auf der Absicht des Benutzers und dem Gesprächskontext aufgerufen werden. Dies kann Planungsmodule, Routing-Mechanismen oder bedingte Abläufe umfassen, die die Werkzeugnutzung dynamisch bestimmen.

- **Nachrichtenverwaltungssystem**: Komponenten, die den Gesprächsablauf zwischen Benutzereingaben, LLM-Antworten, Werkzeugaufrufen und Werkzeugausgaben verwalten.

- **Werkzeugintegrationsrahmen**: Infrastruktur, die den Agenten mit verschiedenen Werkzeugen verbindet, egal ob es sich um einfache Funktionen oder komplexe externe Dienste handelt.

- **Fehlerbehandlung & Validierung**: Mechanismen zur Handhabung von Fehlern bei der Werkzeugausführung, zur Validierung von Parametern und zur Verwaltung unerwarteter Antworten.

- **Zustandsverwaltung**: Verfolgt den Gesprächskontext, vorherige Werkzeuginteraktionen und persistente Daten, um Konsistenz über mehrfache Interaktionen hinweg zu gewährleisten.

Als Nächstes betrachten wir das Funktions-/Werkzeugaufrufen im Detail.

### Funktions-/Werkzeugaufrufen

Das Funktionsaufrufen ist der Hauptweg, mit dem wir Large Language Models (LLMs) erlauben, mit Werkzeugen zu interagieren. Oft werden „Funktion“ und „Werkzeug“ austauschbar verwendet, weil „Funktionen“ (wiederverwendbarer Codeblock) die „Werkzeuge“ sind, die Agenten zur Durchführung von Aufgaben verwenden. Damit der Code einer Funktion aufgerufen wird, muss ein LLM die Benutzereingabe mit der Funktionsbeschreibung abgleichen. Hierfür wird ein Schema mit den Beschreibungen aller verfügbaren Funktionen an das LLM gesendet. Das LLM wählt dann die passendste Funktion für die Aufgabe aus und gibt deren Namen und Argumente zurück. Die ausgewählte Funktion wird aufgerufen, ihre Antwort an das LLM zurückgesendet, welches diese Informationen nutzt, um auf die Benutzeranfrage zu antworten.

Für Entwickler, die Funktionsaufrufe für Agenten implementieren möchten, benötigen Sie:

1. Ein LLM-Modell, das Funktionsaufrufe unterstützt
2. Ein Schema mit Funktionsbeschreibungen
3. Den Code für jede beschriebene Funktion

Nehmen wir als Beispiel das Abrufen der aktuellen Uhrzeit in einer Stadt:

1. **Initialisieren eines LLM, das Funktionsaufrufe unterstützt:**

    Nicht alle Modelle unterstützen Funktionsaufrufe, daher ist es wichtig sicherzustellen, dass das von Ihnen verwendete LLM dies tut. <a href="https://learn.microsoft.com/azure/ai-services/openai/how-to/function-calling" target="_blank">Azure OpenAI</a> unterstützt Funktionsaufrufe. Wir starten, indem wir den Azure OpenAI-Client initialisieren.

    ```python
    # Initialisiere den Azure OpenAI-Client
    client = AzureOpenAI(
        azure_endpoint = os.getenv("AZURE_AI_PROJECT_ENDPOINT"), 
        api_key=os.getenv("AZURE_OPENAI_API_KEY"),  
        api_version="2024-05-01-preview"
    )
    ```

1. **Erstellen eines Funktionsschemas**:

    Als Nächstes definieren wir ein JSON-Schema, das den Funktionsnamen, die Beschreibung der Funktion und die Namen sowie Beschreibungen der Funktionsparameter enthält.
    Wir übergeben dieses Schema dann zusammen mit der Benutzeranfrage, um die Zeit in San Francisco zu ermitteln, an den zuvor erstellten Client. Wichtig ist zu beachten, dass ein **Werkzeugaufruf** zurückgegeben wird, **nicht** die endgültige Antwort auf die Frage. Wie bereits erwähnt, gibt das LLM den Namen der für die Aufgabe ausgewählten Funktion und die übergebenen Argumente zurück.

    ```python
    # Funktionsbeschreibung für das Modell zum Lesen
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
  
    # Erste Benutzeranfrage
    messages = [{"role": "user", "content": "What's the current time in San Francisco"}] 
  
    # Erster API-Aufruf: Bitten Sie das Modell, die Funktion zu verwenden
      response = client.chat.completions.create(
          model=deployment_name,
          messages=messages,
          tools=tools,
          tool_choice="auto",
      )
  
      # Verarbeiten Sie die Antwort des Modells
      response_message = response.choices[0].message
      messages.append(response_message)
  
      print("Model's response:")  

      print(response_message)
  
    ```

    ```bash
    Model's response:
    ChatCompletionMessage(content=None, role='assistant', function_call=None, tool_calls=[ChatCompletionMessageToolCall(id='call_pOsKdUlqvdyttYB67MOj434b', function=Function(arguments='{"location":"San Francisco"}', name='get_current_time'), type='function')])
    ```
  
1. **Der Funktionscode zur Durchführung der Aufgabe:**

    Nun, da das LLM die auszuführende Funktion gewählt hat, muss der Code zur Durchführung der Aufgabe implementiert und ausgeführt werden.
    Wir können den Code zum Abrufen der aktuellen Uhrzeit in Python implementieren. Außerdem müssen wir Code schreiben, um Namen und Argumente aus der response_message zu extrahieren, um das Endergebnis zu erhalten.

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
     # Funktionsaufrufe verarbeiten
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
  
      # Zweiter API-Aufruf: Holen Sie die endgültige Antwort vom Modell
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

Funktionsaufruf ist das Herzstück der meisten, wenn nicht aller Agenten-Tool-Use-Designs, aber es kann manchmal schwierig sein, es von Grund auf zu implementieren.
Wie wir in [Lektion 2](../../../02-explore-agentic-frameworks) gelernt haben, bieten agentische Frameworks vorgefertigte Bausteine zur Implementierung der Werkzeugnutzung.

## Beispiele für Werkzeugnutzung mit agentischen Frameworks

Hier einige Beispiele, wie Sie das Tool Use Design Pattern mit verschiedenen agentischen Frameworks umsetzen können:

### Microsoft Agent Framework

<a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Microsoft Agent Framework</a> ist ein Open-Source-KI-Framework zum Erstellen von KI-Agenten. Es vereinfacht den Prozess des Funktionsaufrufs, indem Sie Werkzeuge als Python-Funktionen mit dem `@tool`-Dekorator definieren. Das Framework übernimmt die Kommunikation zwischen Modell und Ihrem Code. Außerdem bietet es Zugriff auf vorgefertigte Werkzeuge wie Dateisuche und Code Interpreter über den `AzureAIProjectAgentProvider`.

Das folgende Diagramm zeigt den Prozess des Funktionsaufrufs mit dem Microsoft Agent Framework:

![Funktionsaufruf](../../../translated_images/de/functioncalling-diagram.a84006fc287f6014.webp)

Im Microsoft Agent Framework werden Werkzeuge als dekorierte Funktionen definiert. Wir können die zuvor gezeigte `get_current_time`-Funktion in ein Werkzeug umwandeln, indem wir den `@tool`-Dekorator verwenden. Das Framework serialisiert automatisch die Funktion und ihre Parameter und erstellt das Schema, das an das LLM gesendet wird.

```python
from agent_framework import tool
from agent_framework.azure import AzureAIProjectAgentProvider
from azure.identity import AzureCliCredential

@tool
def get_current_time(location: str) -> str:
    """Get the current time for a given location"""
    ...

# Erstelle den Client
provider = AzureAIProjectAgentProvider(credential=AzureCliCredential())

# Erstelle einen Agenten und führe ihn mit dem Werkzeug aus
agent = await provider.create_agent(name="TimeAgent", instructions="Use available tools to answer questions.", tools=get_current_time)
response = await agent.run("What time is it?")
```
  
### Azure AI Agent Service

<a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Azure AI Agent Service</a> ist ein neueres agentisches Framework, das Entwicklern ermöglicht, sicher hochwertige und erweiterbare KI-Agenten zu erstellen, bereitzustellen und zu skalieren, ohne sich um die zugrundeliegenden Compute- und Speicherressourcen kümmern zu müssen. Es ist besonders nützlich für Unternehmensanwendungen, da es sich um einen vollständig verwalteten Dienst mit Unternehmenssicherheitsgrad handelt.

Im Vergleich zur direkten Entwicklung mit der LLM-API bietet Azure AI Agent Service einige Vorteile, darunter:

- Automatischer Werkzeugaufruf – keine Notwendigkeit, Werkzeugaufrufe zu analysieren, das Werkzeug aufzurufen und die Antwort zu verarbeiten; all dies wird jetzt serverseitig erledigt
- Sicher verwaltete Daten – anstatt den eigenen Gesprächszustand zu verwalten, können Threads verwendet werden, um alle benötigten Informationen zu speichern
- Fertige Werkzeuge – Werkzeuge, mit denen Sie mit Ihren Datenquellen interagieren können, wie Bing, Azure AI Search und Azure Functions.

Die in Azure AI Agent Service verfügbaren Werkzeuge lassen sich in zwei Kategorien unterteilen:

1. Knowledge Tools:
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/bing-grounding?tabs=python&pivots=overview" target="_blank">Grounding mit Bing Search</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/file-search?tabs=python&pivots=overview" target="_blank">Dateisuche</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-ai-search?tabs=azurecli%2Cpython&pivots=overview-azure-ai-search" target="_blank">Azure AI Search</a>

2. Action Tools:
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/function-calling?tabs=python&pivots=overview" target="_blank">Funktionsaufruf</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/code-interpreter?tabs=python&pivots=overview" target="_blank">Code Interpreter</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/openapi-spec?tabs=python&pivots=overview" target="_blank">OpenAPI-definierte Werkzeuge</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-functions?pivots=overview" target="_blank">Azure Functions</a>

Der Agent Service ermöglicht es uns, diese Werkzeuge zusammen als `toolset` zu verwenden. Außerdem nutzt er `threads`, die den Nachrichtenverlauf einer bestimmten Konversation nachverfolgen.

Stellen Sie sich vor, Sie sind Verkaufsagent bei einem Unternehmen namens Contoso. Sie möchten einen konversationellen Agenten entwickeln, der Fragen zu Ihren Verkaufsdaten beantworten kann.

Das folgende Bild zeigt, wie Sie Azure AI Agent Service verwenden können, um Ihre Verkaufsdaten zu analysieren:

![Agentic Service In Action](../../../translated_images/de/agent-service-in-action.34fb465c9a84659e.webp)

Um eines dieser Werkzeuge mit dem Dienst zu verwenden, können wir einen Client erstellen und ein Werkzeug oder Toolset definieren. Praktisch können wir dazu den folgenden Python-Code verwenden. Das LLM kann das Toolset betrachten und entscheiden, ob die vom Benutzer erstellte Funktion `fetch_sales_data_using_sqlite_query` oder der vorgefertigte Code Interpreter abhängig von der Benutzeranfrage verwendet werden soll.

```python 
import os
from azure.ai.projects import AIProjectClient
from azure.identity import DefaultAzureCredential
from fetch_sales_data_functions import fetch_sales_data_using_sqlite_query # fetch_sales_data_using_sqlite_query Funktion, die in einer Datei fetch_sales_data_functions.py zu finden ist.
from azure.ai.projects.models import ToolSet, FunctionTool, CodeInterpreterTool

project_client = AIProjectClient.from_connection_string(
    credential=DefaultAzureCredential(),
    conn_str=os.environ["PROJECT_CONNECTION_STRING"],
)

# Toolset initialisieren
toolset = ToolSet()

# Funktionsaufruf-Agent mit der fetch_sales_data_using_sqlite_query Funktion initialisieren und zum Toolset hinzufügen
fetch_data_function = FunctionTool(fetch_sales_data_using_sqlite_query)
toolset.add(fetch_data_function)

# Code Interpreter Tool initialisieren und zum Toolset hinzufügen.
code_interpreter = CodeInterpreterTool()toolset.add(code_interpreter)

agent = project_client.agents.create_agent(
    model="gpt-4o-mini", name="my-agent", instructions="You are helpful agent", 
    toolset=toolset
)
```

## Welche besonderen Überlegungen gibt es bei der Verwendung des Tool Use Design Patterns zur Erstellung vertrauenswürdiger KI-Agenten?

Eine häufige Sorge bei dynamisch von LLMs generiertem SQL ist die Sicherheit, insbesondere das Risiko von SQL-Injektionen oder böswilligen Aktionen, wie das Löschen oder Manipulieren der Datenbank. Obwohl diese Bedenken berechtigt sind, können sie durch richtig konfigurierte Datenbankzugriffsberechtigungen effektiv gemindert werden. Für die meisten Datenbanken bedeutet dies die Konfiguration der Datenbank als nur lesbar. Für Datenbankdienste wie PostgreSQL oder Azure SQL sollte der Anwendung eine nur-lesbare (SELECT) Rolle zugewiesen werden.

Der Betrieb der Anwendung in einer sicheren Umgebung erhöht den Schutz weiter. In Unternehmensszenarien werden Daten typischerweise aus operativen Systemen extrahiert und in eine nur-lesbare Datenbank oder ein Data Warehouse mit benutzerfreundlichem Schema transformiert. Dieser Ansatz stellt sicher, dass die Daten sicher sind, für Leistung und Zugänglichkeit optimiert wurden und die Anwendung nur eingeschränkten Lesenzugriff hat.

## Beispielcodes

- Python: [Agent Framework](./code_samples/04-python-agent-framework.ipynb)
- .NET: [Agent Framework](./code_samples/04-dotnet-agent-framework.md)

## Haben Sie weitere Fragen zum Tool Use Design Pattern?

Treten Sie dem [Microsoft Foundry Discord](https://aka.ms/ai-agents/discord) bei, um andere Lernende zu treffen, an offenen Sprechstunden teilzunehmen und Ihre Fragen zu KI-Agenten beantwortet zu bekommen.

## Zusätzliche Ressourcen

- <a href="https://microsoft.github.io/build-your-first-agent-with-azure-ai-agent-service-workshop/" target="_blank">Azure AI Agents Service Workshop</a>
- <a href="https://github.com/Azure-Samples/contoso-creative-writer/tree/main/docs/workshop" target="_blank">Contoso Creative Writer Multi-Agent Workshop</a>
- <a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Microsoft Agent Framework Übersicht</a>

## Vorherige Lektion

[Verstehen von agentischen Design Patterns](../03-agentic-design-patterns/README.md)

## Nächste Lektion
[Agentic RAG](../05-agentic-rag/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Haftungsausschluss**:
Dieses Dokument wurde mit dem KI-Übersetzungsdienst [Co-op Translator](https://github.com/Azure/co-op-translator) übersetzt. Obwohl wir uns um Genauigkeit bemühen, beachten Sie bitte, dass automatisierte Übersetzungen Fehler oder Ungenauigkeiten enthalten können. Das Originaldokument in seiner Ursprungssprache gilt als maßgebliche Quelle. Bei kritischen Informationen wird eine professionelle menschliche Übersetzung empfohlen. Wir übernehmen keine Haftung für Missverständnisse oder Fehlinterpretationen, die aus der Verwendung dieser Übersetzung entstehen.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->