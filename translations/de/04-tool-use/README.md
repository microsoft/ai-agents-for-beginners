<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "4a5ccc4ad1dba85fbc2087cf3b986544",
  "translation_date": "2025-08-30T07:24:35+00:00",
  "source_file": "04-tool-use/README.md",
  "language_code": "de"
}
-->
[![Wie man gute KI-Agenten entwirft](../../../translated_images/lesson-4-thumbnail.546162853cb3daffd64edd92014f274103f76360dfb39fc6e6ee399494da38fd.de.png)](https://youtu.be/vieRiPRx-gI?si=cEZ8ApnT6Sus9rhn)

> _(Klicken Sie auf das Bild oben, um das Video zu dieser Lektion anzusehen)_

# Entwurfsmuster für die Nutzung von Tools

Tools sind interessant, weil sie KI-Agenten eine breitere Palette von Fähigkeiten ermöglichen. Anstatt dass der Agent nur eine begrenzte Anzahl von Aktionen ausführen kann, kann er durch das Hinzufügen eines Tools nun eine Vielzahl von Aktionen durchführen. In diesem Kapitel betrachten wir das Entwurfsmuster für die Nutzung von Tools, das beschreibt, wie KI-Agenten spezifische Tools verwenden können, um ihre Ziele zu erreichen.

## Einführung

In dieser Lektion wollen wir die folgenden Fragen beantworten:

- Was ist das Entwurfsmuster für die Nutzung von Tools?
- Für welche Anwendungsfälle kann es angewendet werden?
- Welche Elemente/Bausteine sind erforderlich, um das Entwurfsmuster umzusetzen?
- Welche besonderen Überlegungen gibt es, um mit diesem Entwurfsmuster vertrauenswürdige KI-Agenten zu entwickeln?

## Lernziele

Nach Abschluss dieser Lektion werden Sie in der Lage sein:

- Das Entwurfsmuster für die Nutzung von Tools und dessen Zweck zu definieren.
- Anwendungsfälle zu identifizieren, in denen das Entwurfsmuster anwendbar ist.
- Die Schlüsselelemente zu verstehen, die für die Implementierung des Entwurfsmusters erforderlich sind.
- Überlegungen zu erkennen, um die Vertrauenswürdigkeit von KI-Agenten sicherzustellen, die dieses Entwurfsmuster verwenden.

## Was ist das Entwurfsmuster für die Nutzung von Tools?

Das **Entwurfsmuster für die Nutzung von Tools** konzentriert sich darauf, LLMs (Large Language Models) die Fähigkeit zu geben, mit externen Tools zu interagieren, um spezifische Ziele zu erreichen. Tools sind Code, der von einem Agenten ausgeführt werden kann, um Aktionen durchzuführen. Ein Tool kann eine einfache Funktion wie ein Taschenrechner oder ein API-Aufruf eines Drittanbieters wie eine Aktienkursabfrage oder eine Wettervorhersage sein. Im Kontext von KI-Agenten sind Tools so konzipiert, dass sie von Agenten als Reaktion auf **modellgenerierte Funktionsaufrufe** ausgeführt werden.

## Für welche Anwendungsfälle kann es angewendet werden?

KI-Agenten können Tools nutzen, um komplexe Aufgaben zu erledigen, Informationen abzurufen oder Entscheidungen zu treffen. Das Entwurfsmuster für die Nutzung von Tools wird häufig in Szenarien verwendet, die eine dynamische Interaktion mit externen Systemen wie Datenbanken, Webdiensten oder Code-Interpretern erfordern. Diese Fähigkeit ist für eine Vielzahl von Anwendungsfällen nützlich, darunter:

- **Dynamische Informationsbeschaffung:** Agenten können externe APIs oder Datenbanken abfragen, um aktuelle Daten abzurufen (z. B. Abfragen einer SQLite-Datenbank für Datenanalysen, Abrufen von Aktienkursen oder Wetterinformationen).
- **Codeausführung und -interpretation:** Agenten können Code oder Skripte ausführen, um mathematische Probleme zu lösen, Berichte zu erstellen oder Simulationen durchzuführen.
- **Workflow-Automatisierung:** Automatisierung von wiederkehrenden oder mehrstufigen Workflows durch Integration von Tools wie Aufgabenplanern, E-Mail-Diensten oder Datenpipelines.
- **Kundensupport:** Agenten können mit CRM-Systemen, Ticketing-Plattformen oder Wissensdatenbanken interagieren, um Benutzeranfragen zu lösen.
- **Inhaltsgenerierung und -bearbeitung:** Agenten können Tools wie Grammatikprüfer, Textzusammenfasser oder Inhaltsbewertungstools nutzen, um bei der Erstellung von Inhalten zu helfen.

## Welche Elemente/Bausteine sind erforderlich, um das Entwurfsmuster für die Nutzung von Tools umzusetzen?

Diese Bausteine ermöglichen es dem KI-Agenten, eine Vielzahl von Aufgaben auszuführen. Schauen wir uns die Schlüsselelemente an, die für die Implementierung des Entwurfsmusters erforderlich sind:

- **Funktions-/Tool-Schemata:** Detaillierte Definitionen der verfügbaren Tools, einschließlich Funktionsname, Zweck, erforderlicher Parameter und erwarteter Ausgaben. Diese Schemata ermöglichen es dem LLM, zu verstehen, welche Tools verfügbar sind und wie gültige Anfragen erstellt werden.
- **Logik zur Funktionsausführung:** Bestimmt, wie und wann Tools basierend auf der Absicht des Benutzers und dem Gesprächskontext aufgerufen werden. Dies kann Planungsmodule, Routing-Mechanismen oder bedingte Abläufe umfassen, die die Tool-Nutzung dynamisch steuern.
- **Nachrichtenverwaltungssystem:** Komponenten, die den Gesprächsfluss zwischen Benutzereingaben, LLM-Antworten, Tool-Aufrufen und Tool-Ausgaben verwalten.
- **Tool-Integrationsframework:** Infrastruktur, die den Agenten mit verschiedenen Tools verbindet, sei es einfache Funktionen oder komplexe externe Dienste.
- **Fehlerbehandlung und Validierung:** Mechanismen zur Behandlung von Fehlern bei der Tool-Ausführung, zur Validierung von Parametern und zur Verwaltung unerwarteter Antworten.
- **Zustandsverwaltung:** Verfolgt den Gesprächskontext, frühere Tool-Interaktionen und persistente Daten, um Konsistenz über mehrstufige Interaktionen hinweg sicherzustellen.

Als Nächstes betrachten wir Funktions-/Tool-Aufrufe genauer.

### Funktions-/Tool-Aufrufe

Funktionsaufrufe sind der Hauptweg, um Large Language Models (LLMs) die Interaktion mit Tools zu ermöglichen. Oft werden „Funktion“ und „Tool“ synonym verwendet, da „Funktionen“ (wiederverwendbare Codeblöcke) die „Tools“ sind, die Agenten zur Durchführung von Aufgaben verwenden. Damit der Code einer Funktion aufgerufen werden kann, muss ein LLM die Anfrage des Benutzers mit der Beschreibung der Funktion vergleichen. Dazu wird ein Schema mit den Beschreibungen aller verfügbaren Funktionen an das LLM gesendet. Das LLM wählt dann die am besten geeignete Funktion für die Aufgabe aus und gibt deren Namen und Argumente zurück. Die ausgewählte Funktion wird aufgerufen, ihre Antwort wird an das LLM zurückgesendet, das die Informationen verwendet, um auf die Anfrage des Benutzers zu antworten.

Um Funktionsaufrufe für Agenten zu implementieren, benötigen Entwickler:

1. Ein LLM-Modell, das Funktionsaufrufe unterstützt
2. Ein Schema mit Funktionsbeschreibungen
3. Den Code für jede beschriebene Funktion

Schauen wir uns das Beispiel an, wie man die aktuelle Uhrzeit in einer Stadt abruft:

1. **Ein LLM initialisieren, das Funktionsaufrufe unterstützt:**

    Nicht alle Modelle unterstützen Funktionsaufrufe, daher ist es wichtig, sicherzustellen, dass das verwendete LLM dies tut. <a href="https://learn.microsoft.com/azure/ai-services/openai/how-to/function-calling" target="_blank">Azure OpenAI</a> unterstützt Funktionsaufrufe. Wir können beginnen, indem wir den Azure OpenAI-Client initialisieren.

    ```python
    # Initialize the Azure OpenAI client
    client = AzureOpenAI(
        azure_endpoint = os.getenv("AZURE_OPENAI_ENDPOINT"), 
        api_key=os.getenv("AZURE_OPENAI_API_KEY"),  
        api_version="2024-05-01-preview"
    )
    ```

1. **Ein Funktionsschema erstellen:**

    Als Nächstes definieren wir ein JSON-Schema, das den Funktionsnamen, die Beschreibung der Funktion und die Namen und Beschreibungen der Funktionsparameter enthält. Dieses Schema wird dann an den zuvor erstellten Client zusammen mit der Benutzeranfrage übergeben, um die Uhrzeit in San Francisco zu finden. Wichtig ist, dass ein **Tool-Aufruf** zurückgegeben wird, **nicht** die endgültige Antwort auf die Frage. Wie bereits erwähnt, gibt das LLM den Namen der Funktion zurück, die es für die Aufgabe ausgewählt hat, sowie die Argumente, die an sie übergeben werden.

    ```python
    # Function description for the model to read
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
  
    # Initial user message
    messages = [{"role": "user", "content": "What's the current time in San Francisco"}] 
  
    # First API call: Ask the model to use the function
      response = client.chat.completions.create(
          model=deployment_name,
          messages=messages,
          tools=tools,
          tool_choice="auto",
      )
  
      # Process the model's response
      response_message = response.choices[0].message
      messages.append(response_message)
  
      print("Model's response:")  

      print(response_message)
  
    ```

    ```bash
    Model's response:
    ChatCompletionMessage(content=None, role='assistant', function_call=None, tool_calls=[ChatCompletionMessageToolCall(id='call_pOsKdUlqvdyttYB67MOj434b', function=Function(arguments='{"location":"San Francisco"}', name='get_current_time'), type='function')])
    ```
  
1. **Der erforderliche Funktionscode zur Durchführung der Aufgabe:**

    Nachdem das LLM ausgewählt hat, welche Funktion ausgeführt werden soll, muss der Code implementiert und ausgeführt werden. Wir können den Code, um die aktuelle Uhrzeit abzurufen, in Python implementieren. Außerdem müssen wir den Code schreiben, um den Namen und die Argumente aus der response_message zu extrahieren, um das endgültige Ergebnis zu erhalten.

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
     # Handle function calls
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
  
      # Second API call: Get the final response from the model
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

Funktionsaufrufe sind das Herzstück der meisten, wenn nicht aller Entwürfe zur Nutzung von Tools durch Agenten. Die Implementierung von Grund auf kann jedoch manchmal herausfordernd sein. Wie wir in [Lektion 2](../../../02-explore-agentic-frameworks) gelernt haben, bieten agentische Frameworks uns vorgefertigte Bausteine zur Implementierung der Tool-Nutzung.

## Beispiele für die Nutzung von Tools mit agentischen Frameworks

Hier sind einige Beispiele, wie Sie das Entwurfsmuster für die Nutzung von Tools mit verschiedenen agentischen Frameworks implementieren können:

### Semantic Kernel

<a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Semantic Kernel</a> ist ein Open-Source-KI-Framework für .NET-, Python- und Java-Entwickler, die mit Large Language Models (LLMs) arbeiten. Es vereinfacht die Nutzung von Funktionsaufrufen, indem es Ihre Funktionen und deren Parameter automatisch durch einen Prozess namens <a href="https://learn.microsoft.com/semantic-kernel/concepts/ai-services/chat-completion/function-calling/?pivots=programming-language-python#1-serializing-the-functions" target="_blank">Serialisierung</a> beschreibt. Es verwaltet auch die Kommunikation zwischen dem Modell und Ihrem Code. Ein weiterer Vorteil der Verwendung eines agentischen Frameworks wie Semantic Kernel ist, dass Sie Zugriff auf vorgefertigte Tools wie <a href="https://github.com/microsoft/semantic-kernel/blob/main/python/samples/getting_started_with_agents/openai_assistant/step4_assistant_tool_file_search.py" target="_blank">File Search</a> und <a href="https://github.com/microsoft/semantic-kernel/blob/main/python/samples/getting_started_with_agents/openai_assistant/step3_assistant_tool_code_interpreter.py" target="_blank">Code Interpreter</a> haben.

Das folgende Diagramm veranschaulicht den Prozess des Funktionsaufrufs mit Semantic Kernel:

![Funktionsaufruf](../../../translated_images/functioncalling-diagram.a84006fc287f60140cc0a484ff399acd25f69553ea05186981ac4d5155f9c2f6.de.png)

In Semantic Kernel werden Funktionen/Tools als <a href="https://learn.microsoft.com/semantic-kernel/concepts/plugins/?pivots=programming-language-python" target="_blank">Plugins</a> bezeichnet. Wir können die `get_current_time`-Funktion, die wir zuvor gesehen haben, in ein Plugin umwandeln, indem wir sie in eine Klasse mit der Funktion darin umwandeln. Wir können auch den `kernel_function`-Dekorator importieren, der die Beschreibung der Funktion übernimmt. Wenn Sie dann einen Kernel mit dem GetCurrentTimePlugin erstellen, serialisiert der Kernel automatisch die Funktion und ihre Parameter und erstellt dabei das Schema, das an das LLM gesendet wird.

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

# Create the kernel
kernel = Kernel()

# Create the plugin
get_current_time_plugin = GetCurrentTimePlugin(location)

# Add the plugin to the kernel
kernel.add_plugin(get_current_time_plugin)
```
  
### Azure AI Agent Service

<a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Azure AI Agent Service</a> ist ein neueres agentisches Framework, das Entwicklern helfen soll, hochwertige und erweiterbare KI-Agenten sicher zu erstellen, bereitzustellen und zu skalieren, ohne die zugrunde liegenden Rechen- und Speicherressourcen verwalten zu müssen. Es ist besonders nützlich für Unternehmensanwendungen, da es sich um einen vollständig verwalteten Dienst mit Sicherheit auf Unternehmensniveau handelt.

Im Vergleich zur Entwicklung direkt mit der LLM-API bietet der Azure AI Agent Service einige Vorteile, darunter:

- Automatische Tool-Aufrufe – keine Notwendigkeit, einen Tool-Aufruf zu analysieren, das Tool aufzurufen und die Antwort zu verarbeiten; all dies wird jetzt serverseitig erledigt.
- Sicher verwaltete Daten – anstatt den eigenen Gesprächsstatus zu verwalten, können Sie sich auf Threads verlassen, um alle benötigten Informationen zu speichern.
- Out-of-the-box-Tools – Tools, die Sie verwenden können, um mit Ihren Datenquellen zu interagieren, wie Bing, Azure AI Search und Azure Functions.

Die im Azure AI Agent Service verfügbaren Tools lassen sich in zwei Kategorien unterteilen:

1. Wissens-Tools:
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/bing-grounding?tabs=python&pivots=overview" target="_blank">Grundlagen mit Bing-Suche</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/file-search?tabs=python&pivots=overview" target="_blank">Dateisuche</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-ai-search?tabs=azurecli%2Cpython&pivots=overview-azure-ai-search" target="_blank">Azure AI Search</a>

2. Aktions-Tools:
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/function-calling?tabs=python&pivots=overview" target="_blank">Funktionsaufrufe</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/code-interpreter?tabs=python&pivots=overview" target="_blank">Code Interpreter</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/openapi-spec?tabs=python&pivots=overview" target="_blank">Von OpenAI definierte Tools</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-functions?pivots=overview" target="_blank">Azure Functions</a>

Der Agent Service ermöglicht es uns, diese Tools zusammen als `toolset` zu verwenden. Er nutzt auch `threads`, die den Verlauf der Nachrichten aus einem bestimmten Gespräch verfolgen.

Stellen Sie sich vor, Sie sind ein Vertriebsmitarbeiter bei einem Unternehmen namens Contoso. Sie möchten einen Konversationsagenten entwickeln, der Fragen zu Ihren Vertriebsdaten beantworten kann.

Das folgende Bild zeigt, wie Sie den Azure AI Agent Service verwenden könnten, um Ihre Vertriebsdaten zu analysieren:

![Agentic Service in Aktion](../../../translated_images/agent-service-in-action.34fb465c9a84659edd3003f8cb62d6b366b310a09b37c44e32535021fbb5c93f.de.jpg)

Um eines dieser Tools mit dem Service zu verwenden, können wir einen Client erstellen und ein Tool oder ein Toolset definieren. Um dies praktisch umzusetzen, können wir den folgenden Python-Code verwenden. Das LLM kann das Toolset betrachten und je nach Benutzeranfrage entscheiden, ob es die vom Benutzer erstellte Funktion `fetch_sales_data_using_sqlite_query` oder den vorgefertigten Code Interpreter verwendet.

```python 
import os
from azure.ai.projects import AIProjectClient
from azure.identity import DefaultAzureCredential
from fetch_sales_data_functions import fetch_sales_data_using_sqlite_query # fetch_sales_data_using_sqlite_query function which can be found in a fetch_sales_data_functions.py file.
from azure.ai.projects.models import ToolSet, FunctionTool, CodeInterpreterTool

project_client = AIProjectClient.from_connection_string(
    credential=DefaultAzureCredential(),
    conn_str=os.environ["PROJECT_CONNECTION_STRING"],
)

# Initialize function calling agent with the fetch_sales_data_using_sqlite_query function and adding it to the toolset
fetch_data_function = FunctionTool(fetch_sales_data_using_sqlite_query)
toolset = ToolSet()
toolset.add(fetch_data_function)

# Initialize Code Interpreter tool and adding it to the toolset. 
code_interpreter = code_interpreter = CodeInterpreterTool()
toolset = ToolSet()
toolset.add(code_interpreter)

agent = project_client.agents.create_agent(
    model="gpt-4o-mini", name="my-agent", instructions="You are helpful agent", 
    toolset=toolset
)
```

## Welche besonderen Überlegungen gibt es, um mit dem Entwurfsmuster für die Nutzung von Tools vertrauenswürdige KI-Agenten zu entwickeln?

Ein häufiges Anliegen bei SQL, das dynamisch von LLMs generiert wird, ist die Sicherheit, insbesondere das Risiko von SQL-Injection oder böswilligen Aktionen wie dem Löschen oder Manipulieren der Datenbank. Obwohl diese Bedenken berechtigt sind, können sie durch die ordnungsgemäße Konfiguration der Datenbankzugriffsberechtigungen effektiv gemindert werden. Für die meisten Datenbanken bedeutet dies, die Datenbank als schreibgeschützt zu konfigurieren. Für Datenbankdienste wie PostgreSQL oder Azure SQL sollte der App eine schreibgeschützte (SELECT-)Rolle zugewiesen werden.

Das Ausführen der App in einer sicheren Umgebung erhöht den Schutz weiter. In Unternehmensszenarien werden Daten typischerweise aus operativen Systemen extrahiert und in eine schreibgeschützte Datenbank oder ein Data Warehouse mit einer benutzerfreundlichen Schema transformiert. Dieser Ansatz stellt sicher, dass die Daten sicher sind, für Leistung und Zugänglichkeit optimiert sind und dass die App eingeschränkten, schreibgeschützten Zugriff hat.

### Haben Sie weitere Fragen zum Entwurfsmuster für die Nutzung von Tools?
Tritt dem [Azure AI Foundry Discord](https://aka.ms/ai-agents/discord) bei, um andere Lernende zu treffen, Sprechstunden zu besuchen und Antworten auf deine Fragen zu AI Agents zu erhalten.

## Zusätzliche Ressourcen

## Vorherige Lektion

[Verständnis von agentischen Designmustern](../03-agentic-design-patterns/README.md)

## Nächste Lektion

[Agentic RAG](../05-agentic-rag/README.md)

---

**Haftungsausschluss**:  
Dieses Dokument wurde mit dem KI-Übersetzungsdienst [Co-op Translator](https://github.com/Azure/co-op-translator) übersetzt. Obwohl wir uns um Genauigkeit bemühen, weisen wir darauf hin, dass automatisierte Übersetzungen Fehler oder Ungenauigkeiten enthalten können. Das Originaldokument in seiner ursprünglichen Sprache sollte als maßgebliche Quelle betrachtet werden. Für kritische Informationen wird eine professionelle menschliche Übersetzung empfohlen. Wir übernehmen keine Haftung für Missverständnisse oder Fehlinterpretationen, die sich aus der Nutzung dieser Übersetzung ergeben.