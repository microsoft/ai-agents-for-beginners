<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "d7c3b7bd1b3528074d8b6a7c5ad33b6f",
  "translation_date": "2025-11-18T16:32:05+00:00",
  "source_file": "04-tool-use/README.md",
  "language_code": "de"
}
-->
[![Wie man gute KI-Agenten entwirft](../../../translated_images/lesson-4-thumbnail.546162853cb3daffd64edd92014f274103f76360dfb39fc6e6ee399494da38fd.de.png)](https://youtu.be/vieRiPRx-gI?si=cEZ8ApnT6Sus9rhn)

> _(Klicken Sie auf das obige Bild, um das Video zu dieser Lektion anzusehen)_

# Designmuster für Werkzeugnutzung

Werkzeuge sind interessant, weil sie KI-Agenten eine breitere Palette an Fähigkeiten ermöglichen. Anstatt dass der Agent nur eine begrenzte Anzahl von Aktionen ausführen kann, kann er durch das Hinzufügen eines Werkzeugs nun eine Vielzahl von Aktionen durchführen. In diesem Kapitel betrachten wir das Designmuster für Werkzeugnutzung, das beschreibt, wie KI-Agenten spezifische Werkzeuge nutzen können, um ihre Ziele zu erreichen.

## Einführung

In dieser Lektion wollen wir die folgenden Fragen beantworten:

- Was ist das Designmuster für Werkzeugnutzung?
- Für welche Anwendungsfälle kann es angewendet werden?
- Welche Elemente/Bausteine sind erforderlich, um das Designmuster zu implementieren?
- Welche besonderen Überlegungen gibt es bei der Nutzung des Designmusters für Werkzeugnutzung, um vertrauenswürdige KI-Agenten zu entwickeln?

## Lernziele

Nach Abschluss dieser Lektion werden Sie in der Lage sein:

- Das Designmuster für Werkzeugnutzung und seinen Zweck zu definieren.
- Anwendungsfälle zu identifizieren, in denen das Designmuster für Werkzeugnutzung anwendbar ist.
- Die Schlüsselelemente zu verstehen, die zur Implementierung des Designmusters erforderlich sind.
- Überlegungen zu erkennen, um die Vertrauenswürdigkeit von KI-Agenten zu gewährleisten, die dieses Designmuster verwenden.

## Was ist das Designmuster für Werkzeugnutzung?

Das **Designmuster für Werkzeugnutzung** konzentriert sich darauf, LLMs die Fähigkeit zu geben, mit externen Werkzeugen zu interagieren, um spezifische Ziele zu erreichen. Werkzeuge sind Code, der von einem Agenten ausgeführt werden kann, um Aktionen durchzuführen. Ein Werkzeug kann eine einfache Funktion wie ein Taschenrechner oder ein API-Aufruf zu einem Drittanbieterdienst wie einer Aktienkursabfrage oder einer Wettervorhersage sein. Im Kontext von KI-Agenten sind Werkzeuge so konzipiert, dass sie von Agenten als Reaktion auf **modellgenerierte Funktionsaufrufe** ausgeführt werden.

## Für welche Anwendungsfälle kann es angewendet werden?

KI-Agenten können Werkzeuge nutzen, um komplexe Aufgaben zu erledigen, Informationen abzurufen oder Entscheidungen zu treffen. Das Designmuster für Werkzeugnutzung wird häufig in Szenarien verwendet, die eine dynamische Interaktion mit externen Systemen wie Datenbanken, Webdiensten oder Code-Interpretern erfordern. Diese Fähigkeit ist für eine Reihe verschiedener Anwendungsfälle nützlich, darunter:

- **Dynamische Informationsabfrage:** Agenten können externe APIs oder Datenbanken abfragen, um aktuelle Daten abzurufen (z. B. Abfrage einer SQLite-Datenbank für Datenanalysen, Abruf von Aktienkursen oder Wetterinformationen).
- **Codeausführung und -interpretation:** Agenten können Code oder Skripte ausführen, um mathematische Probleme zu lösen, Berichte zu erstellen oder Simulationen durchzuführen.
- **Workflow-Automatisierung:** Automatisierung von sich wiederholenden oder mehrstufigen Workflows durch Integration von Werkzeugen wie Aufgabenplanern, E-Mail-Diensten oder Datenpipelines.
- **Kundensupport:** Agenten können mit CRM-Systemen, Ticketing-Plattformen oder Wissensdatenbanken interagieren, um Benutzeranfragen zu lösen.
- **Inhaltsgenerierung und -bearbeitung:** Agenten können Werkzeuge wie Grammatikprüfer, Textzusammenfasser oder Inhaltsbewertungstools nutzen, um bei der Erstellung von Inhalten zu helfen.

## Welche Elemente/Bausteine sind erforderlich, um das Designmuster für Werkzeugnutzung zu implementieren?

Diese Bausteine ermöglichen es dem KI-Agenten, eine Vielzahl von Aufgaben auszuführen. Schauen wir uns die Schlüsselelemente an, die zur Implementierung des Designmusters für Werkzeugnutzung erforderlich sind:

- **Funktions-/Werkzeugschemata:** Detaillierte Definitionen der verfügbaren Werkzeuge, einschließlich Funktionsname, Zweck, erforderlicher Parameter und erwarteter Ausgaben. Diese Schemata ermöglichen es dem LLM, zu verstehen, welche Werkzeuge verfügbar sind und wie gültige Anfragen erstellt werden.
- **Logik zur Funktionsausführung:** Regelt, wie und wann Werkzeuge basierend auf der Absicht des Benutzers und dem Gesprächskontext aufgerufen werden. Dies kann Planermodule, Routing-Mechanismen oder bedingte Abläufe umfassen, die die Werkzeugnutzung dynamisch bestimmen.
- **Nachrichtenverwaltungssystem:** Komponenten, die den Gesprächsfluss zwischen Benutzereingaben, LLM-Antworten, Werkzeugaufrufen und Werkzeugausgaben verwalten.
- **Werkzeugintegrations-Framework:** Infrastruktur, die den Agenten mit verschiedenen Werkzeugen verbindet, sei es einfache Funktionen oder komplexe externe Dienste.
- **Fehlerbehandlung und Validierung:** Mechanismen zur Behandlung von Fehlern bei der Werkzeugausführung, zur Validierung von Parametern und zur Verwaltung unerwarteter Antworten.
- **Zustandsverwaltung:** Verfolgt den Gesprächskontext, frühere Werkzeuginteraktionen und persistente Daten, um Konsistenz über mehrfache Interaktionen hinweg zu gewährleisten.

Als Nächstes betrachten wir Funktions-/Werkzeugaufrufe genauer.

### Funktions-/Werkzeugaufrufe

Funktionsaufrufe sind die primäre Methode, um großen Sprachmodellen (LLMs) die Interaktion mit Werkzeugen zu ermöglichen. Oft werden „Funktion“ und „Werkzeug“ synonym verwendet, da „Funktionen“ (wiederverwendbare Codeblöcke) die „Werkzeuge“ sind, die Agenten zur Durchführung von Aufgaben verwenden. Damit der Code einer Funktion aufgerufen werden kann, muss ein LLM die Anfrage des Benutzers mit der Beschreibung der Funktion vergleichen. Dazu wird ein Schema mit den Beschreibungen aller verfügbaren Funktionen an das LLM gesendet. Das LLM wählt dann die am besten geeignete Funktion für die Aufgabe aus und gibt deren Namen und Argumente zurück. Die ausgewählte Funktion wird aufgerufen, ihre Antwort wird an das LLM zurückgesendet, das die Informationen verwendet, um auf die Anfrage des Benutzers zu antworten.

Um Funktionsaufrufe für Agenten zu implementieren, benötigen Entwickler:

1. Ein LLM-Modell, das Funktionsaufrufe unterstützt
2. Ein Schema mit Funktionsbeschreibungen
3. Den Code für jede beschriebene Funktion

Lassen Sie uns das Beispiel verwenden, die aktuelle Uhrzeit in einer Stadt zu erhalten, um dies zu veranschaulichen:

1. **Ein LLM initialisieren, das Funktionsaufrufe unterstützt:**

    Nicht alle Modelle unterstützen Funktionsaufrufe, daher ist es wichtig zu überprüfen, ob das verwendete LLM dies tut. <a href="https://learn.microsoft.com/azure/ai-services/openai/how-to/function-calling" target="_blank">Azure OpenAI</a> unterstützt Funktionsaufrufe. Wir können damit beginnen, den Azure OpenAI-Client zu initialisieren.

    ```python
    # Initialize the Azure OpenAI client
    client = AzureOpenAI(
        azure_endpoint = os.getenv("AZURE_OPENAI_ENDPOINT"), 
        api_key=os.getenv("AZURE_OPENAI_API_KEY"),  
        api_version="2024-05-01-preview"
    )
    ```

1. **Ein Funktionsschema erstellen:**

    Als Nächstes definieren wir ein JSON-Schema, das den Funktionsnamen, die Beschreibung der Funktion und die Namen und Beschreibungen der Funktionsparameter enthält. Dieses Schema wird dann an den zuvor erstellten Client übergeben, zusammen mit der Benutzeranfrage, die Uhrzeit in San Francisco zu finden. Wichtig ist, dass ein **Werkzeugaufruf** zurückgegeben wird, **nicht** die endgültige Antwort auf die Frage. Wie bereits erwähnt, gibt das LLM den Namen der Funktion zurück, die es für die Aufgabe ausgewählt hat, sowie die Argumente, die an sie übergeben werden.

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

    Nachdem das LLM ausgewählt hat, welche Funktion ausgeführt werden soll, muss der Code, der die Aufgabe ausführt, implementiert und ausgeführt werden. Wir können den Code implementieren, um die aktuelle Uhrzeit in Python zu erhalten. Außerdem müssen wir den Code schreiben, um den Namen und die Argumente aus der response_message zu extrahieren, um das endgültige Ergebnis zu erhalten.

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

Funktionsaufrufe stehen im Mittelpunkt der meisten, wenn nicht aller Entwürfe für die Werkzeugnutzung durch Agenten. Die Implementierung von Grund auf kann jedoch manchmal eine Herausforderung sein. Wie wir in [Lektion 2](../../../02-explore-agentic-frameworks) gelernt haben, bieten agentische Frameworks uns vorgefertigte Bausteine zur Implementierung der Werkzeugnutzung.

## Beispiele für Werkzeugnutzung mit agentischen Frameworks

Hier sind einige Beispiele, wie Sie das Designmuster für Werkzeugnutzung mit verschiedenen agentischen Frameworks implementieren können:

### Semantic Kernel

<a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Semantic Kernel</a> ist ein Open-Source-KI-Framework für .NET-, Python- und Java-Entwickler, die mit großen Sprachmodellen (LLMs) arbeiten. Es vereinfacht die Nutzung von Funktionsaufrufen, indem es Ihre Funktionen und deren Parameter automatisch durch einen Prozess namens <a href="https://learn.microsoft.com/semantic-kernel/concepts/ai-services/chat-completion/function-calling/?pivots=programming-language-python#1-serializing-the-functions" target="_blank">Serialisierung</a> beschreibt. Es verwaltet auch die Kommunikation zwischen dem Modell und Ihrem Code. Ein weiterer Vorteil der Verwendung eines agentischen Frameworks wie Semantic Kernel ist, dass Sie Zugriff auf vorgefertigte Werkzeuge wie <a href="https://github.com/microsoft/semantic-kernel/blob/main/python/samples/getting_started_with_agents/openai_assistant/step4_assistant_tool_file_search.py" target="_blank">Dateisuche</a> und <a href="https://github.com/microsoft/semantic-kernel/blob/main/python/samples/getting_started_with_agents/openai_assistant/step3_assistant_tool_code_interpreter.py" target="_blank">Code-Interpreter</a> haben.

Das folgende Diagramm veranschaulicht den Prozess des Funktionsaufrufs mit Semantic Kernel:

![Funktionsaufruf](../../../translated_images/functioncalling-diagram.a84006fc287f60140cc0a484ff399acd25f69553ea05186981ac4d5155f9c2f6.de.png)

In Semantic Kernel werden Funktionen/Werkzeuge <a href="https://learn.microsoft.com/semantic-kernel/concepts/plugins/?pivots=programming-language-python" target="_blank">Plugins</a> genannt. Wir können die `get_current_time`-Funktion, die wir zuvor gesehen haben, in ein Plugin umwandeln, indem wir sie in eine Klasse mit der Funktion darin umwandeln. Wir können auch den `kernel_function`-Dekorator importieren, der die Beschreibung der Funktion übernimmt. Wenn Sie dann einen Kernel mit dem GetCurrentTimePlugin erstellen, serialisiert der Kernel die Funktion und ihre Parameter automatisch und erstellt dabei das Schema, das an das LLM gesendet wird.

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

Im Vergleich zur direkten Entwicklung mit der LLM-API bietet der Azure AI Agent Service einige Vorteile, darunter:

- Automatische Werkzeugaufrufe – es ist nicht erforderlich, einen Werkzeugaufruf zu analysieren, das Werkzeug aufzurufen und die Antwort zu verarbeiten; all dies wird jetzt serverseitig erledigt.
- Sicher verwaltete Daten – anstatt den eigenen Gesprächszustand zu verwalten, können Sie sich auf Threads verlassen, um alle benötigten Informationen zu speichern.
- Out-of-the-box-Werkzeuge – Werkzeuge, die Sie verwenden können, um mit Ihren Datenquellen zu interagieren, wie Bing, Azure AI Search und Azure Functions.

Die im Azure AI Agent Service verfügbaren Werkzeuge können in zwei Kategorien unterteilt werden:

1. Wissenswerkzeuge:
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/bing-grounding?tabs=python&pivots=overview" target="_blank">Grundlagen mit Bing-Suche</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/file-search?tabs=python&pivots=overview" target="_blank">Dateisuche</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-ai-search?tabs=azurecli%2Cpython&pivots=overview-azure-ai-search" target="_blank">Azure AI Search</a>

2. Aktionswerkzeuge:
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/function-calling?tabs=python&pivots=overview" target="_blank">Funktionsaufrufe</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/code-interpreter?tabs=python&pivots=overview" target="_blank">Code-Interpreter</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/openapi-spec?tabs=python&pivots=overview" target="_blank">OpenAPI-definierte Werkzeuge</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-functions?pivots=overview" target="_blank">Azure Functions</a>

Der Agent Service ermöglicht es uns, diese Werkzeuge zusammen als `toolset` zu verwenden. Er nutzt auch `threads`, die den Verlauf der Nachrichten aus einem bestimmten Gespräch verfolgen.

Stellen Sie sich vor, Sie sind ein Vertriebsmitarbeiter bei einem Unternehmen namens Contoso. Sie möchten einen Konversationsagenten entwickeln, der Fragen zu Ihren Verkaufsdaten beantworten kann.

Das folgende Bild zeigt, wie Sie den Azure AI Agent Service nutzen könnten, um Ihre Verkaufsdaten zu analysieren:

![Agentic Service in Aktion](../../../translated_images/agent-service-in-action.34fb465c9a84659edd3003f8cb62d6b366b310a09b37c44e32535021fbb5c93f.de.jpg)

Um eines dieser Werkzeuge mit dem Service zu verwenden, können wir einen Client erstellen und ein Werkzeug oder ein Werkzeugset definieren. Um dies praktisch umzusetzen, können wir den folgenden Python-Code verwenden. Das LLM wird in der Lage sein, das Werkzeugset zu betrachten und je nach Benutzeranfrage entweder die vom Benutzer erstellte Funktion `fetch_sales_data_using_sqlite_query` oder den vorgefertigten Code-Interpreter zu verwenden.

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

## Welche besonderen Überlegungen gibt es bei der Nutzung des Designmusters für Werkzeugnutzung, um vertrauenswürdige KI-Agenten zu entwickeln?

Ein häufiges Anliegen bei SQL, das dynamisch von LLMs generiert wird, ist die Sicherheit, insbesondere das Risiko von SQL-Injection oder böswilligen Aktionen wie dem Löschen oder Manipulieren der Datenbank. Obwohl diese Bedenken berechtigt sind, können sie durch die ordnungsgemäße Konfiguration der Datenbankzugriffsberechtigungen effektiv gemindert werden. Für die meisten Datenbanken bedeutet dies, die Datenbank als schreibgeschützt zu konfigurieren. Für Datenbankdienste wie PostgreSQL oder Azure SQL sollte der App eine schreibgeschützte (SELECT-)Rolle zugewiesen werden.
Das Ausführen der App in einer sicheren Umgebung erhöht den Schutz zusätzlich. In Unternehmensszenarien werden Daten typischerweise aus operativen Systemen extrahiert und in eine schreibgeschützte Datenbank oder ein Data Warehouse mit einem benutzerfreundlichen Schema transformiert. Dieser Ansatz stellt sicher, dass die Daten sicher sind, für Leistung und Zugänglichkeit optimiert werden und die App nur eingeschränkten, schreibgeschützten Zugriff hat.

## Beispielcodes

- Python: [Agent Framework](./code_samples/04-python-agent-framework.ipynb)
- .NET: [Agent Framework](./code_samples/04-dotnet-agent-framework.md)

## Haben Sie weitere Fragen zu den Designmustern für die Nutzung des Tools?

Treten Sie dem [Azure AI Foundry Discord](https://aka.ms/ai-agents/discord) bei, um andere Lernende zu treffen, an Sprechstunden teilzunehmen und Ihre Fragen zu AI Agents beantwortet zu bekommen.

## Zusätzliche Ressourcen

- <a href="https://microsoft.github.io/build-your-first-agent-with-azure-ai-agent-service-workshop/" target="_blank">Azure AI Agents Service Workshop</a>
- <a href="https://github.com/Azure-Samples/contoso-creative-writer/tree/main/docs/workshop" target="_blank">Contoso Creative Writer Multi-Agent Workshop</a>
- <a href="https://learn.microsoft.com/semantic-kernel/concepts/ai-services/chat-completion/function-calling/?pivots=programming-language-python#1-serializing-the-functions" target="_blank">Semantic Kernel Function Calling Tutorial</a>
- <a href="https://github.com/microsoft/semantic-kernel/blob/main/python/samples/getting_started_with_agents/openai_assistant/step3_assistant_tool_code_interpreter.py" target="_blank">Semantic Kernel Code Interpreter</a>
- <a href="https://microsoft.github.io/autogen/dev/user-guide/core-user-guide/components/tools.html" target="_blank">Autogen Tools</a>

## Vorherige Lektion

[Verständnis von agentischen Designmustern](../03-agentic-design-patterns/README.md)

## Nächste Lektion

[Agentic RAG](../05-agentic-rag/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Haftungsausschluss**:  
Dieses Dokument wurde mit dem KI-Übersetzungsdienst [Co-op Translator](https://github.com/Azure/co-op-translator) übersetzt. Obwohl wir uns um Genauigkeit bemühen, beachten Sie bitte, dass automatisierte Übersetzungen Fehler oder Ungenauigkeiten enthalten können. Das Originaldokument in seiner ursprünglichen Sprache sollte als maßgebliche Quelle betrachtet werden. Für kritische Informationen wird eine professionelle menschliche Übersetzung empfohlen. Wir übernehmen keine Haftung für Missverständnisse oder Fehlinterpretationen, die sich aus der Nutzung dieser Übersetzung ergeben.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->