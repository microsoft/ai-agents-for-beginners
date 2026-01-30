[![Wie man gute KI-Agenten entwirft](../../../translated_images/de/lesson-4-thumbnail.546162853cb3daff.webp)](https://youtu.be/vieRiPRx-gI?si=cEZ8ApnT6Sus9rhn)

> _(Klicken Sie auf das Bild oben, um das Video zu dieser Lektion anzusehen)_

# Entwurfsmuster für Werkzeugnutzung

Werkzeuge sind interessant, weil sie KI-Agenten eine breitere Palette von Fähigkeiten ermöglichen. Anstatt dass der Agent nur eine begrenzte Menge von Aktionen ausführen kann, kann der Agent mit einem zusätzlichen Werkzeug nun eine Vielzahl von Aktionen durchführen. In diesem Kapitel betrachten wir das Entwurfsmuster für Werkzeugnutzung, das beschreibt, wie KI-Agenten spezifische Werkzeuge verwenden können, um ihre Ziele zu erreichen.

## Einführung

In dieser Lektion wollen wir folgende Fragen beantworten:

- Was ist das Entwurfsmuster für Werkzeugnutzung?
- Für welche Anwendungsfälle kann es angewendet werden?
- Welche Elemente/Bausteine werden benötigt, um das Entwurfsmuster umzusetzen?
- Welche besonderen Überlegungen gibt es beim Einsatz des Entwurfsmusters für Werkzeugnutzung, um vertrauenswürdige KI-Agenten zu bauen?

## Lernziele

Nach Abschluss dieser Lektion sind Sie in der Lage:

- Das Entwurfsmuster für Werkzeugnutzung und dessen Zweck zu definieren.
- Anwendungsfälle zu identifizieren, in denen das Entwurfsmuster für Werkzeugnutzung anwendbar ist.
- Die Schlüsselaspekte zu verstehen, die für die Implementierung des Entwurfsmusters erforderlich sind.
- Überlegungen zu erkennen, die für die Gewährleistung von Vertrauenswürdigkeit bei KI-Agenten, die dieses Entwurfsmuster verwenden, notwendig sind.

## Was ist das Entwurfsmuster für Werkzeugnutzung?

Das **Entwurfsmuster für Werkzeugnutzung** konzentriert sich darauf, großen Sprachmodellen (LLMs) die Fähigkeit zu verleihen, mit externen Werkzeugen zu interagieren, um spezifische Ziele zu erreichen. Werkzeuge sind Code, der von einem Agenten ausgeführt werden kann, um Aktionen durchzuführen. Ein Werkzeug kann eine einfache Funktion wie ein Taschenrechner sein oder ein API-Aufruf zu einem Drittanbieterdienst wie Aktienkursabfrage oder Wettervorhersage. Im Kontext von KI-Agenten sind Werkzeuge so konzipiert, dass sie als Antwort auf **modellgenerierte Funktionsaufrufe** von Agenten ausgeführt werden.

## Für welche Anwendungsfälle kann es angewendet werden?

KI-Agenten können Werkzeuge nutzen, um komplexe Aufgaben zu erledigen, Informationen abzurufen oder Entscheidungen zu treffen. Das Entwurfsmuster für Werkzeugnutzung wird häufig in Szenarien verwendet, die eine dynamische Interaktion mit externen Systemen erfordern, wie Datenbanken, Webdiensten oder Code-Interpretern. Diese Fähigkeit ist für eine Reihe von Anwendungsfällen nützlich, darunter:

- **Dynamische Informationsabfrage:** Agenten können externe APIs oder Datenbanken abfragen, um aktuelle Daten zu erhalten (z.B. Abfrage einer SQLite-Datenbank für Datenanalysen, Abrufen von Aktienkursen oder Wetterinformationen).
- **Code-Ausführung und -Interpretation:** Agenten können Code oder Skripte ausführen, um mathematische Probleme zu lösen, Berichte zu generieren oder Simulationen durchzuführen.
- **Automatisierung von Arbeitsabläufen:** Automatisierung von repetitiven oder mehrstufigen Arbeitsabläufen durch Integration von Werkzeugen wie Aufgabenplanern, E-Mail-Diensten oder Daten-Pipelines.
- **Kundensupport:** Agenten können mit CRM-Systemen, Ticket-Plattformen oder Wissensdatenbanken interagieren, um Benutzeranfragen zu beantworten.
- **Inhaltserstellung und -bearbeitung:** Agenten können Werkzeuge wie Grammatikprüfer, Textzusammenfasser oder Tools zur Bewertung der Inhalts-Sicherheit nutzen, um bei der Inhaltserstellung zu helfen.

## Welche Elemente/Bausteine werden benötigt, um das Entwurfsmuster für Werkzeugnutzung umzusetzen?

Diese Bausteine ermöglichen es dem KI-Agenten, eine breite Palette von Aufgaben auszuführen. Schauen wir uns die Schlüsselelemente an, die für die Implementierung des Entwurfsmusters für Werkzeugnutzung erforderlich sind:

- **Funktions-/Werkzeug-Schemas**: Detaillierte Definitionen der verfügbaren Werkzeuge, einschließlich Funktionsname, Zweck, erforderliche Parameter und erwartete Ausgaben. Diese Schemas ermöglichen es dem LLM zu verstehen, welche Werkzeuge verfügbar sind und wie gültige Anfragen aufgebaut werden.

- **Logik der Funktionsausführung**: Bestimmt wie und wann Werkzeuge basierend auf der Absicht des Nutzers und dem Gesprächskontext aufgerufen werden. Dies kann Planungsmodule, Routing-Mechanismen oder bedingte Abläufe umfassen, die die Werkzeugnutzung dynamisch steuern.

- **Nachrichtenverarbeitungssystem**: Komponenten, die den Gesprächsfluss zwischen Benutzereingaben, LLM-Antworten, Werkzeugaufrufen und Werkzeugergebnissen verwalten.

- **Werkzeugintegrations-Framework**: Infrastruktur, die den Agenten mit verschiedenen Werkzeugen verbindet, egal ob einfache Funktionen oder komplexe externe Dienste.

- **Fehlerbehandlung & Validierung**: Mechanismen zur Handhabung von Fehlern bei der Werkzeugaussführung, Validierung von Parametern und Umgang mit unerwarteten Antworten.

- **Statusverwaltung**: Verfolgt Gesprächskontext, vorherige Werkzeuginteraktionen und persistente Daten, um Konsistenz über mehrmalige Interaktionen sicherzustellen.

Als nächstes betrachten wir Funktions-/Werkzeugaufrufe im Detail.

### Funktions-/Werkzeugaufrufe

Funktionsaufrufe sind der primäre Weg, wie wir großen Sprachmodellen (LLMs) ermöglichen, mit Werkzeugen zu interagieren. Oft werden „Funktion“ und „Werkzeug“ synonym verwendet, da „Funktionen“ (Blöcke wiederverwendbaren Codes) die „Werkzeuge“ sind, die Agenten zur Erledigung von Aufgaben verwenden. Damit der Code einer Funktion aufgerufen werden kann, muss ein LLM die Nutzeranfrage mit der Funktionsbeschreibung vergleichen. Dafür wird ein Schema mit den Beschreibungen aller verfügbaren Funktionen an das LLM gesendet. Das LLM wählt dann die passendste Funktion für die Aufgabe aus und gibt deren Namen und Argumente zurück. Die ausgewählte Funktion wird dann ausgeführt, die Antwort zurück an das LLM gesendet, das diese Information nutzt, um auf die Nutzeranfrage zu antworten.

Für Entwickler, die Funktionsaufrufe für Agenten implementieren möchten, sind folgende Dinge notwendig:

1. Ein LLM-Modell, das Funktionsaufrufe unterstützt
2. Ein Schema, das Funktionsbeschreibungen enthält
3. Der Code zu jeder beschriebenen Funktion

Wir verwenden das Beispiel, die aktuelle Uhrzeit in einer Stadt abzurufen, um dies zu veranschaulichen:

1. **Initialisierung eines LLM, das Funktionsaufrufe unterstützt:**

    Nicht alle Modelle unterstützen Funktionsaufrufe, daher ist es wichtig zu prüfen, ob das verwendete LLM dies tut. <a href="https://learn.microsoft.com/azure/ai-services/openai/how-to/function-calling" target="_blank">Azure OpenAI</a> unterstützt Funktionsaufrufe. Wir starten mit der Initialisierung des Azure OpenAI Clients.

    ```python
    # Initialisiere den Azure OpenAI-Client
    client = AzureOpenAI(
        azure_endpoint = os.getenv("AZURE_OPENAI_ENDPOINT"), 
        api_key=os.getenv("AZURE_OPENAI_API_KEY"),  
        api_version="2024-05-01-preview"
    )
    ```

1. **Erstellung eines Funktionsschemas:**

    Als nächstes definieren wir ein JSON-Schema, das den Funktionsnamen, eine Beschreibung der Funktion und die Namen und Beschreibungen der Funktionsparameter enthält.
    Dieses Schema wird dann an den zuvor erstellten Client zusammen mit der Nutzereingabe gesendet, um die Uhrzeit in San Francisco zu ermitteln. Wichtig ist, dass ein **Werkzeugaufruf** zurückgegeben wird, **nicht** die endgültige Antwort auf die Frage. Wie bereits erwähnt, gibt das LLM den Namen der für die Aufgabe ausgewählten Funktion und die zu übergebenden Argumente zurück.

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
  
    # Erster API-Aufruf: Fordere das Modell auf, die Funktion zu verwenden
      response = client.chat.completions.create(
          model=deployment_name,
          messages=messages,
          tools=tools,
          tool_choice="auto",
      )
  
      # Verarbeite die Antwort des Modells
      response_message = response.choices[0].message
      messages.append(response_message)
  
      print("Model's response:")  

      print(response_message)
  
    ```

    ```bash
    Model's response:
    ChatCompletionMessage(content=None, role='assistant', function_call=None, tool_calls=[ChatCompletionMessageToolCall(id='call_pOsKdUlqvdyttYB67MOj434b', function=Function(arguments='{"location":"San Francisco"}', name='get_current_time'), type='function')])
    ```
  
1. **Der Funktionscode zur Ausführung der Aufgabe:**

    Da das LLM die Funktion ausgewählt hat, die ausgeführt werden muss, muss der Code implementiert und ausgeführt werden, der die Aufgabe erledigt.
    Wir implementieren den Code, um die aktuelle Uhrzeit in Python zu erhalten. Außerdem müssen wir den Code schreiben, um Name und Argumente aus der response_message zu extrahieren, um das endgültige Ergebnis zu erhalten.

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
     # Funktionaufrufe verarbeiten
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
  
      # Zweiter API-Aufruf: Holen Sie sich die endgültige Antwort vom Modell
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

Funktionsaufrufe sind das Herzstück der meisten, wenn nicht aller Agenten-Werkzeugnutzungen, jedoch kann die Umsetzung von Grund auf manchmal herausfordernd sein.
Wie wir in [Lektion 2](../../../02-explore-agentic-frameworks) gelernt haben, bieten agentische Frameworks vorgefertigte Bausteine zur Implementierung der Werkzeugnutzung.

## Beispiele für Werkzeugnutzung mit agentischen Frameworks

Hier einige Beispiele, wie Sie das Entwurfsmuster für Werkzeugnutzung mit verschiedenen agentischen Frameworks umsetzen können:

### Semantic Kernel

<a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Semantic Kernel</a> ist ein Open-Source KI-Framework für .NET-, Python- und Java-Entwickler, die mit großen Sprachmodellen arbeiten. Es vereinfacht die Verwendung von Funktionsaufrufen, indem es Ihre Funktionen und deren Parameter über einen Prozess namens <a href="https://learn.microsoft.com/semantic-kernel/concepts/ai-services/chat-completion/function-calling/?pivots=programming-language-python#1-serializing-the-functions" target="_blank">Serialisierung</a> automatisch für das Modell beschreibt. Es verwaltet zudem die Hin- und Rückkommunikation zwischen dem Modell und Ihrem Code. Ein weiterer Vorteil bei der Verwendung eines agentischen Frameworks wie Semantic Kernel ist, dass es Ihnen Zugang zu vorgefertigten Werkzeugen wie <a href="https://github.com/microsoft/semantic-kernel/blob/main/python/samples/getting_started_with_agents/openai_assistant/step4_assistant_tool_file_search.py" target="_blank">Dateisuche</a> und <a href="https://github.com/microsoft/semantic-kernel/blob/main/python/samples/getting_started_with_agents/openai_assistant/step3_assistant_tool_code_interpreter.py" target="_blank">Code-Interpreter</a> ermöglicht.

Das folgende Diagramm veranschaulicht den Prozess des Funktionsaufrufs mit Semantic Kernel:

![function calling](../../../translated_images/de/functioncalling-diagram.a84006fc287f6014.webp)

In Semantic Kernel werden Funktionen/Werkzeuge <a href="https://learn.microsoft.com/semantic-kernel/concepts/plugins/?pivots=programming-language-python" target="_blank">Plugins</a> genannt. Wir können die Funktion `get_current_time`, die wir zuvor gesehen haben, in ein Plugin umwandeln, indem wir sie in eine Klasse mit der Funktion darin verwandeln. Außerdem importieren wir den `kernel_function` Dekorator, der die Beschreibung der Funktion erhält. Wenn Sie dann mit dem GetCurrentTimePlugin einen Kernel erstellen, serialisiert der Kernel automatisch die Funktion und ihre Parameter und erstellt dabei das Schema, das an das LLM gesendet wird.

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

# Erstelle den Kernel
kernel = Kernel()

# Erstelle das Plugin
get_current_time_plugin = GetCurrentTimePlugin(location)

# Füge das Plugin dem Kernel hinzu
kernel.add_plugin(get_current_time_plugin)
```
  
### Azure AI Agent Service

<a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Azure AI Agent Service</a> ist ein neueres agentisches Framework, das darauf ausgelegt ist, Entwickler dabei zu unterstützen, sicher qualitativ hochwertige, skalierbare und erweiterbare KI-Agenten zu erstellen und bereitzustellen, ohne die zugrundeliegende Rechen- und Speicherkapazität verwalten zu müssen. Es ist besonders für Unternehmensanwendungen nützlich, da es ein vollständig verwalteter Dienst mit unternehmensgerechter Sicherheit ist.

Im Vergleich zur direkten Entwicklung mit der LLM-API bietet Azure AI Agent Service einige Vorteile, darunter:

- Automatischer Werkzeugaufruf – kein Bedarf, einen Werkzeugaufruf zu parsen, das Werkzeug aufzurufen und die Antwort zu bearbeiten; dies erfolgt jetzt serverseitig
- Sicher verwaltete Daten – statt den eigenen Gesprächszustand zu verwalten, können Sie sich auf Threads verlassen, die alle notwendigen Informationen speichern
- Sofort einsetzbare Werkzeuge – Werkzeuge, mit denen Sie auf Ihre Datenquellen zugreifen können, wie Bing, Azure AI Search und Azure Functions.

Die verfügbaren Werkzeuge im Azure AI Agent Service lassen sich in zwei Kategorien einteilen:

1. Wissenswerkzeuge:
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/bing-grounding?tabs=python&pivots=overview" target="_blank">Grounding mit Bing Search</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/file-search?tabs=python&pivots=overview" target="_blank">Dateisuche</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-ai-search?tabs=azurecli%2Cpython&pivots=overview-azure-ai-search" target="_blank">Azure AI Search</a>

2. Aktionswerkzeuge:
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/function-calling?tabs=python&pivots=overview" target="_blank">Funktionsaufruf</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/code-interpreter?tabs=python&pivots=overview" target="_blank">Code-Interpreter</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/openapi-spec?tabs=python&pivots=overview" target="_blank">OpenAPI-definierte Werkzeuge</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-functions?pivots=overview" target="_blank">Azure Functions</a>

Der Agent Service ermöglicht uns, diese Werkzeuge als `Werkzeugset` gemeinsam zu nutzen. Zudem nutzt er `Threads`, die die Nachrichtenhistorie eines bestimmten Gesprächs verfolgen.

Stellen Sie sich vor, Sie sind Vertriebsagent bei einem Unternehmen namens Contoso. Sie möchten einen konversationellen Agenten entwickeln, der Fragen zu Ihren Verkaufsdaten beantworten kann.

Das folgende Bild zeigt, wie Sie Azure AI Agent Service verwenden könnten, um Ihre Verkaufsdaten zu analysieren:

![Agentic Service In Action](../../../translated_images/de/agent-service-in-action.34fb465c9a84659e.webp)

Um eines dieser Werkzeuge mit dem Service zu nutzen, können wir einen Client erstellen und ein Werkzeug oder Werkzeugset definieren. Praktisch umgesetzt kann dies mit dem folgenden Python-Code erfolgen. Das LLM kann das Werkzeugset betrachten und entscheiden, ob es die vom Nutzer erstellte Funktion `fetch_sales_data_using_sqlite_query` oder den vorgefertigten Code-Interpreter je nach Benutzeranfrage verwendet.

```python 
import os
from azure.ai.projects import AIProjectClient
from azure.identity import DefaultAzureCredential
from fetch_sales_data_functions import fetch_sales_data_using_sqlite_query # fetch_sales_data_using_sqlite_query Funktion, die in einer fetch_sales_data_functions.py Datei gefunden werden kann.
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

# Code-Interpreter-Tool initialisieren und zum Toolset hinzufügen.
code_interpreter = code_interpreter = CodeInterpreterTool()
toolset.add(code_interpreter)

agent = project_client.agents.create_agent(
    model="gpt-4o-mini", name="my-agent", instructions="You are helpful agent", 
    toolset=toolset
)
```

## Welche besonderen Überlegungen gibt es bei der Nutzung des Entwurfsmusters für Werkzeugnutzung, um vertrauenswürdige KI-Agenten zu bauen?

Eine häufige Sorge bei SQL, das dynamisch von LLMs generiert wird, betrifft die Sicherheit, insbesondere das Risiko von SQL-Injektionen oder schädlichen Aktionen wie dem Löschen oder Manipulieren der Datenbank. Obwohl diese Bedenken berechtigt sind, können sie effektiv durch die richtige Konfiguration der Datenbankzugriffsrechte gemindert werden. Für die meisten Datenbanken bedeutet dies, die Datenbank im Lesezugriff (read-only) zu konfigurieren. Für Datenbankdienste wie PostgreSQL oder Azure SQL sollte der App eine read-only (SELECT) Rolle zugewiesen werden.
Das Ausführen der App in einer sicheren Umgebung erhöht den Schutz zusätzlich. In Unternehmensszenarien werden Daten typischerweise aus operativen Systemen extrahiert und in eine schreibgeschützte Datenbank oder ein Data Warehouse mit einem benutzerfreundlichen Schema transformiert. Dieser Ansatz stellt sicher, dass die Daten sicher, leistungs- und zugänglichkeitsoptimiert sind und die App einen eingeschränkten, schreibgeschützten Zugriff hat.

## Beispiel-Code

- Python: [Agent Framework](./code_samples/04-python-agent-framework.ipynb)
- .NET: [Agent Framework](./code_samples/04-dotnet-agent-framework.md)

## Haben Sie weitere Fragen zu den Design Patterns des Tools?

Treten Sie dem [Azure AI Foundry Discord](https://aka.ms/ai-agents/discord) bei, um andere Lernende zu treffen, an Sprechstunden teilzunehmen und Ihre Fragen zu AI Agents beantwortet zu bekommen.

## Zusätzliche Ressourcen

- <a href="https://microsoft.github.io/build-your-first-agent-with-azure-ai-agent-service-workshop/" target="_blank">Azure AI Agents Service Workshop</a>
- <a href="https://github.com/Azure-Samples/contoso-creative-writer/tree/main/docs/workshop" target="_blank">Contoso Creative Writer Multi-Agent Workshop</a>
- <a href="https://learn.microsoft.com/semantic-kernel/concepts/ai-services/chat-completion/function-calling/?pivots=programming-language-python#1-serializing-the-functions" target="_blank">Semantic Kernel Function Calling Tutorial</a>
- <a href="https://github.com/microsoft/semantic-kernel/blob/main/python/samples/getting_started_with_agents/openai_assistant/step3_assistant_tool_code_interpreter.py" target="_blank">Semantic Kernel Code Interpreter</a>
- <a href="https://microsoft.github.io/autogen/dev/user-guide/core-user-guide/components/tools.html" target="_blank">Autogen Tools</a>

## Vorherige Lektion

[Understanding Agentic Design Patterns](../03-agentic-design-patterns/README.md)

## Nächste Lektion

[Agentic RAG](../05-agentic-rag/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Haftungsausschluss**:  
Dieses Dokument wurde mithilfe des KI-Übersetzungsdienstes [Co-op Translator](https://github.com/Azure/co-op-translator) übersetzt. Obwohl wir uns um Genauigkeit bemühen, beachten Sie bitte, dass automatisierte Übersetzungen Fehler oder Ungenauigkeiten enthalten können. Das Originaldokument in seiner ursprünglichen Sprache gilt als maßgebliche Quelle. Für wichtige Informationen wird eine professionelle menschliche Übersetzung empfohlen. Wir übernehmen keine Haftung für Missverständnisse oder Fehlinterpretationen, die sich aus der Nutzung dieser Übersetzung ergeben.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->