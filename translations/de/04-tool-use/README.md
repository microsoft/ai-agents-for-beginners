[![Wie man gute KI-Agenten entwirft](../../../translated_images/de/lesson-4-thumbnail.546162853cb3daff.webp)](https://youtu.be/vieRiPRx-gI?si=cEZ8ApnT6Sus9rhn)

> _(Klicken Sie auf das Bild oben, um das Video zu dieser Lektion anzusehen)_

# Tool Use Design Pattern

Werkzeuge sind interessant, weil sie KI-Agenten ermöglichen, ein breiteres Spektrum an Fähigkeiten zu haben. Anstatt dass der Agent nur über eine begrenzte Menge an Aktionen verfügt, die er ausführen kann, kann der Agent durch Hinzufügen eines Werkzeugs nun eine Vielzahl von Aktionen ausführen. In diesem Kapitel betrachten wir das Tool Use Design Pattern, das beschreibt, wie KI-Agenten bestimmte Werkzeuge nutzen können, um ihre Ziele zu erreichen.

## Einführung

In dieser Lektion möchten wir folgende Fragen beantworten:

- Was ist das Tool Use Design Pattern?
- Für welche Anwendungsfälle kann es eingesetzt werden?
- Welche Elemente/Bausteine werden benötigt, um das Design Pattern umzusetzen?
- Welche besonderen Überlegungen gibt es bei der Nutzung des Tool Use Design Pattern zum Aufbau vertrauenswürdiger KI-Agenten?

## Lernziele

Nach Abschluss dieser Lektion werden Sie in der Lage sein:

- Das Tool Use Design Pattern und seinen Zweck zu definieren.
- Anwendungsfälle zu identifizieren, in denen das Tool Use Design Pattern anwendbar ist.
- Die Schlüsselelemente zu verstehen, die zur Implementierung des Design Patterns benötigt werden.
- Überlegungen zu erkennen, die zur Gewährleistung von Vertrauenswürdigkeit bei KI-Agenten mit diesem Design Pattern notwendig sind.

## Was ist das Tool Use Design Pattern?

Das **Tool Use Design Pattern** konzentriert sich darauf, LLMs die Fähigkeit zu geben, mit externen Werkzeugen zu interagieren, um spezifische Ziele zu erreichen. Werkzeuge sind Code, der von einem Agenten ausgeführt werden kann, um Aktionen durchzuführen. Ein Werkzeug kann eine einfache Funktion wie ein Taschenrechner sein oder ein API-Aufruf zu einem Drittanbieterdienst wie Aktienkurse oder Wettervorhersage. Im Kontext von KI-Agenten sind Werkzeuge so gestaltet, dass sie auf **modellgenerierte Funktionsaufrufe** durch Agenten ausgeführt werden.

## Für welche Anwendungsfälle kann es eingesetzt werden?

KI-Agenten können Werkzeuge nutzen, um komplexe Aufgaben zu erledigen, Informationen abzurufen oder Entscheidungen zu treffen. Das Tool Use Design Pattern wird häufig in Szenarien eingesetzt, die eine dynamische Interaktion mit externen Systemen erfordern, wie Datenbanken, Webdienste oder Code-Interpreter. Diese Fähigkeit ist nützlich für verschiedene Anwendungsfälle, darunter:

- **Dynamische Informationsbeschaffung:** Agenten können externe APIs oder Datenbanken abfragen, um aktuelle Daten zu erhalten (z. B. Abfragen einer SQLite-Datenbank für Datenanalysen, Abrufen von Aktienkursen oder Wetterinformationen).
- **Code-Ausführung und -Interpretation:** Agenten können Code oder Skripte ausführen, um mathematische Probleme zu lösen, Berichte zu erstellen oder Simulationen durchzuführen.
- **Workflow-Automatisierung:** Automatisierung von sich wiederholenden oder mehrstufigen Arbeitsabläufen durch Integration von Werkzeugen wie Task-Scheduler, E-Mail-Diensten oder Datenpipelines.
- **Kundensupport:** Agenten können mit CRM-Systemen, Ticketplattformen oder Wissensdatenbanken interagieren, um Benutzeranfragen zu lösen.
- **Inhaltserstellung und -bearbeitung:** Agenten können Werkzeuge wie Grammatikprüfer, Textzusammenfasser oder Content-Sicherheitsprüfer nutzen, um bei der Erstellung von Inhalten zu helfen.

## Welche Elemente/Bausteine werden benötigt, um das Tool Use Design Pattern zu implementieren?

Diese Bausteine ermöglichen es dem KI-Agenten, ein breites Spektrum an Aufgaben auszuführen. Schauen wir uns die Schlüsselkomponenten für die Implementierung des Tool Use Design Pattern an:

- **Funktions-/Werkzeugschemata**: Detaillierte Definitionen der verfügbaren Werkzeuge, einschließlich Funktionsname, Zweck, erforderliche Parameter und erwartete Ausgaben. Diese Schemata ermöglichen es dem LLM zu verstehen, welche Werkzeuge verfügbar sind und wie gültige Anfragen aufgebaut werden.

- **Funktionsausführungslogik**: Regelt, wie und wann Werkzeuge basierend auf der Absicht des Nutzers und dem Gesprächskontext aufgerufen werden. Dies kann Planungsmodule, Routing-Mechanismen oder bedingte Abläufe umfassen, die die Werkzeugnutzung dynamisch steuern.

- **Nachrichtenverwaltungssystem**: Komponenten, die den Gesprächsfluss zwischen Benutzereingaben, LLM-Antworten, Werkzeugaufrufen und Werkzeugausgaben verwalten.

- **Werkzeugintegrations-Framework**: Infrastruktur, die den Agenten mit verschiedenen Werkzeugen verbindet, egal ob einfache Funktionen oder komplexe externe Dienste.

- **Fehlerbehandlung & Validierung**: Mechanismen zur Handhabung von Ausfällen bei der Werkzeugausführung, zur Validierung von Parametern und zum Umgang mit unerwarteten Antworten.

- **Zustandsverwaltung**: Verfolgt den Gesprächskontext, vorherige Werkzeuginteraktionen und persistente Daten, um Konsistenz über mehrstufige Interaktionen sicherzustellen.

Im Folgenden betrachten wir den Funktions-/Werkzeugaufruf etwas genauer.
 
### Funktions-/Werkzeugaufruf

Der Funktionsaufruf ist der Hauptweg, wie wir Large Language Models (LLMs) ermöglichen, mit Werkzeugen zu interagieren. Häufig werden "Funktion" und "Werkzeug" austauschbar verwendet, weil "Funktionen" (wiederverwendbare Codeblöcke) die "Werkzeuge" sind, die Agenten zur Aufgabenbearbeitung nutzen. Damit der Code einer Funktion aufgerufen werden kann, muss ein LLM die Anfrage des Benutzers mit der Funktionsbeschreibung abgleichen. Dazu wird ein Schema mit Beschreibungen aller verfügbaren Funktionen an das LLM gesendet. Das LLM wählt dann die passendste Funktion für die Aufgabe aus und gibt deren Namen und Argumente zurück. Die ausgewählte Funktion wird aufgerufen, deren Antwort wird an das LLM gesendet, welches die Informationen verwendet, um auf die Benutzeranfrage zu reagieren.

Entwickler, die Funktionsaufrufe für Agenten implementieren wollen, benötigen:

1. Ein LLM-Modell, das Funktionsaufrufe unterstützt
2. Ein Schema mit Funktionsbeschreibungen
3. Den Code für jede beschriebene Funktion

Nutzen wir das Beispiel, die aktuelle Zeit in einer Stadt abzurufen, zur Veranschaulichung:

1. **Initialisieren eines LLM, das Funktionsaufrufe unterstützt:**

    Nicht alle Modelle unterstützen Funktionsaufrufe, daher ist es wichtig sicherzustellen, dass Ihr LLM das tut.     <a href="https://learn.microsoft.com/azure/ai-services/openai/how-to/function-calling" target="_blank">Azure OpenAI</a> unterstützt Funktionsaufrufe. Wir können damit beginnen, den OpenAI-Client gegen die Azure OpenAI **Responses API** zu initialisieren (der stabile `/openai/v1/`-Endpunkt — kein `api_version` nötig). 

    ```python
    # Initialisieren Sie den OpenAI-Client für Azure OpenAI (Responses API, v1-Endpunkt)
    client = OpenAI(
        base_url=f"{os.environ['AZURE_OPENAI_ENDPOINT'].rstrip('/')}/openai/v1/",
        api_key=os.environ["AZURE_OPENAI_API_KEY"],
    )
    deployment_name = os.environ["AZURE_OPENAI_DEPLOYMENT"]
    ```

1. **Erstellen eines Funktionsschemas**:

    Definieren wir als nächstes ein JSON-Schema, das den Funktionsnamen, die Beschreibung der Funktion und die Namen sowie Beschreibungen der Funktionsparameter enthält.
    Dieses Schema wird dann zusammen mit der Benutzeranfrage, die die Zeit in San Francisco ermittelt, an den zuvor erstellten Client übergeben. Wichtig ist, dass ein **Werkzeugaufruf** zurückgegeben wird, **nicht** die endgültige Antwort auf die Frage. Wie bereits erwähnt, gibt das LLM den Namen der Funktion zurück, die es für die Aufgabe ausgewählt hat, sowie die Argumente, die übergeben werden.

    ```python
    # Funktionsbeschreibung für das Modell zum Lesen (Antworten API flaches Werkzeugformat)
    tools = [
        {
            "type": "function",
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
    ]
    ```
   
    ```python
  
    # Erste Benutzeranfrage
    messages = [{"role": "user", "content": "What's the current time in San Francisco"}]

    # Erster API-Aufruf: Fordere das Modell auf, die Funktion zu verwenden
    response = client.responses.create(
        model=deployment_name,
        input=messages,
        tools=tools,
        tool_choice="auto",
        store=False,
    )

    # Die Responses-API gibt Werkzeugaufrufe als function_call-Elemente in response.output zurück.
    # Füge sie dem Gespräch hinzu, damit das Modell im nächsten Schritt den vollständigen Kontext hat.
    messages += response.output

    print("Model's response:")
    print(response.output)
  
    ```

    ```bash
    Model's response:
    [ResponseFunctionToolCall(arguments='{"location":"San Francisco"}', call_id='call_pOsKdUlqvdyttYB67MOj434b', name='get_current_time', type='function_call')]
    ```
  
1. **Der Funktionscode, der zur Ausführung der Aufgabe benötigt wird:**

    Nachdem das LLM entschieden hat, welche Funktion ausgeführt werden muss, muss der Code implementiert und ausgeführt werden, der die Aufgabe tatsächlich erledigt.
    Wir können den Code in Python schreiben, um die aktuelle Zeit zu ermitteln. Außerdem müssen wir den Code schreiben, der den Namen und die Argumente aus der response_message extrahiert, um das endgültige Ergebnis zu erhalten.

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
    tool_calls = [item for item in response.output if item.type == "function_call"]
    if tool_calls:
        for tool_call in tool_calls:
            if tool_call.name == "get_current_time":

                function_args = json.loads(tool_call.arguments)

                time_response = get_current_time(
                    location=function_args.get("location")
                )

                # Gib das Werkzeugergebnis als ein Function_call_output-Element zurück
                messages.append({
                    "type": "function_call_output",
                    "call_id": tool_call.call_id,
                    "output": time_response,
                })
    else:
        print("No tool calls were made by the model.")

    # Zweiter API-Aufruf: Die endgültige Antwort vom Modell abrufen
    final_response = client.responses.create(
        model=deployment_name,
        input=messages,
        tools=tools,
        store=False,
    )

    return final_response.output_text
     ```

     ```bash
      get_current_time called with location: San Francisco
      Timezone found for san francisco
      The current time in San Francisco is 09:24 AM.
     ```

Funktionsaufrufe sind das Herzstück der meisten, wenn nicht aller Agenten-Werkzeugsdesigns, allerdings kann die Implementierung von Grund auf manchmal herausfordernd sein.
Wie wir in [Lektion 2](../../../02-explore-agentic-frameworks) gelernt haben, bieten agentische Frameworks vorgefertigte Bausteine, um Werkzeugnutzung zu implementieren.
 
## Beispiele für Werkzeugnutzung mit agentischen Frameworks

Hier einige Beispiele, wie Sie das Tool Use Design Pattern mit verschiedenen agentischen Frameworks umsetzen können:

### Microsoft Agent Framework

<a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Microsoft Agent Framework</a> ist ein Open-Source-KI-Framework zum Erstellen von KI-Agenten. Es vereinfacht den Prozess der Funktionsaufrufe, indem es Ihnen ermöglicht, Werkzeuge als Python-Funktionen mit dem `@tool`-Dekorator zu definieren. Das Framework übernimmt die Kommunikation zwischen dem Modell und Ihrem Code. Außerdem bietet es Zugriff auf vorgefertigte Werkzeuge wie Dateisuche und Code-Interpreter über `FoundryChatClient`.

Das folgende Diagramm verdeutlicht den Prozess des Funktionsaufrufs mit dem Microsoft Agent Framework:

![Funktionsaufruf](../../../translated_images/de/functioncalling-diagram.a84006fc287f6014.webp)

Im Microsoft Agent Framework werden Werkzeuge als dekorierte Funktionen definiert. Wir können die zuvor gesehene Funktion `get_current_time` in ein Werkzeug umwandeln, indem wir den `@tool`-Dekorator verwenden. Das Framework serialisiert die Funktion und ihre Parameter automatisch und erstellt das Schema, das an das LLM gesendet wird.

```python
import os
from agent_framework import tool
from agent_framework.foundry import FoundryChatClient
from azure.identity import AzureCliCredential

@tool(approval_mode="never_require")
def get_current_time(location: str) -> str:
    """Get the current time for a given location"""
    ...

# Erstellen Sie den Client
provider = FoundryChatClient(
    project_endpoint=os.environ["AZURE_AI_PROJECT_ENDPOINT"],
    model=os.environ["AZURE_AI_MODEL_DEPLOYMENT_NAME"],
    credential=AzureCliCredential(),
)

# Erstellen Sie einen Agenten und führen Sie ihn mit dem Tool aus
agent = provider.as_agent(name="TimeAgent", instructions="Use available tools to answer questions.", tools=get_current_time)
response = await agent.run("What time is it?")
```
  
### Microsoft Foundry Agent Service

<a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Microsoft Foundry Agent Service</a> ist ein neueres agentisches Framework, das Entwicklern ermöglicht, sicher hochwertige, erweiterbare KI-Agenten zu erstellen, bereitzustellen und zu skalieren, ohne sich um Infrastruktur und Speicherressourcen kümmern zu müssen. Es ist besonders nützlich für Unternehmensanwendungen, da es sich um einen vollständig verwalteten Dienst mit Unternehmenssicherheitsstandards handelt.

Im Vergleich zur direkten Entwicklung mit der LLM-API bietet der Microsoft Foundry Agent Service einige Vorteile, darunter:

- Automatischer Werkzeugaufruf – kein Parsen von Werkzeugaufrufen, kein Aufrufen des Werkzeugs oder Verarbeiten der Antwort mehr nötig; all dies erfolgt nun serverseitig
- Sicher verwaltete Daten – anstatt den eigenen Gesprächszustand zu verwalten, können Sie auf Threads vertrauen, um alle benötigten Informationen zu speichern
- Werkzeuge sofort einsatzbereit – Werkzeuge, mit denen Sie auf Ihre Datenquellen zugreifen können, wie Bing, Azure AI Search und Azure Functions.

Die im Microsoft Foundry Agent Service verfügbaren Werkzeuge lassen sich in zwei Kategorien einteilen:

1. Wissenswerkzeuge:
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/bing-grounding?tabs=python&pivots=overview" target="_blank">Verankerung mit Bing Search</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/file-search?tabs=python&pivots=overview" target="_blank">Dateisuche</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-ai-search?tabs=azurecli%2Cpython&pivots=overview-azure-ai-search" target="_blank">Azure AI Search</a>

2. Aktionswerkzeuge:
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/function-calling?tabs=python&pivots=overview" target="_blank">Funktionsaufrufe</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/code-interpreter?tabs=python&pivots=overview" target="_blank">Code-Interpreter</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/openapi-spec?tabs=python&pivots=overview" target="_blank">OpenAPI-definierte Werkzeuge</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-functions?pivots=overview" target="_blank">Azure Functions</a>

Der Agent Service ermöglicht es uns, diese Werkzeuge zusammen als ein `toolset` zu verwenden. Er nutzt auch `threads`, die den Nachrichtenverlauf eines bestimmten Gesprächs nachverfolgen.

Stellen Sie sich vor, Sie sind ein Vertriebsmitarbeiter bei einer Firma namens Contoso. Sie möchten einen Konversationsagenten entwickeln, der Fragen zu Ihren Verkaufsdaten beantworten kann.

Das folgende Bild zeigt, wie Sie den Microsoft Foundry Agent Service zur Analyse Ihrer Verkaufsdaten nutzen könnten:

![Agentic Service In Action](../../../translated_images/de/agent-service-in-action.34fb465c9a84659e.webp)

Um eines dieser Werkzeuge mit dem Dienst zu verwenden, können wir einen Client erstellen und ein Werkzeug oder Werkzeugset definieren. Praktisch umgesetzt verwenden wir dazu den folgenden Python-Code. Das LLM kann das Werkzeugset prüfen und je nach Benutzeranfrage entscheiden, ob es die benutzerdefinierte Funktion `fetch_sales_data_using_sqlite_query` oder den vorgefertigten Code-Interpreter verwendet.

```python 
import os
from azure.ai.projects import AIProjectClient
from azure.identity import DefaultAzureCredential
from fetch_sales_data_functions import fetch_sales_data_using_sqlite_query # fetch_sales_data_using_sqlite_query Funktion, die in einer fetch_sales_data_functions.py Datei zu finden ist.
from azure.ai.projects.models import ToolSet, FunctionTool, CodeInterpreterTool

project_client = AIProjectClient.from_connection_string(
    credential=DefaultAzureCredential(),
    conn_str=os.environ["PROJECT_CONNECTION_STRING"],
)

# Werkzeugset initialisieren
toolset = ToolSet()

# Funktionsaufruf-Agent mit der Funktion fetch_sales_data_using_sqlite_query initialisieren und zum Werkzeugset hinzufügen
fetch_data_function = FunctionTool(fetch_sales_data_using_sqlite_query)
toolset.add(fetch_data_function)

# Code Interpreter-Werkzeug initialisieren und zum Werkzeugset hinzufügen.
code_interpreter = CodeInterpreterTool()toolset.add(code_interpreter)

agent = project_client.agents.create_agent(
    model="gpt-5-mini", name="my-agent", instructions="You are helpful agent", 
    toolset=toolset
)
```

## Welche besonderen Überlegungen gibt es bei der Nutzung des Tool Use Design Pattern zum Aufbau vertrauenswürdiger KI-Agenten?

Ein häufiges Sicherheitsbedenken bei dynamisch von LLMs erzeugtem SQL betrifft SQL-Injection oder böswillige Aktionen wie das Löschen oder Manipulieren der Datenbank. Obwohl diese Bedenken berechtigt sind, können sie wirksam durch die richtige Konfiguration der Datenbankzugriffsrechte abgeschwächt werden. Für die meisten Datenbanken bedeutet dies die Konfiguration als schreibgeschützte Datenbank. Bei Datenbankdiensten wie PostgreSQL oder Azure SQL sollte der App eine schreibgeschützte (SELECT) Rolle zugewiesen werden.

Der Betrieb der App in einer sicheren Umgebung erhöht den Schutz weiter. In Unternehmensszenarien werden Daten typischerweise aus operativen Systemen extrahiert und transformiert in eine schreibgeschützte Datenbank oder ein Data Warehouse mit benutzerfreundlichem Schema. Dieser Ansatz gewährleistet Sicherheit der Daten, optimiert Leistung und Zugänglichkeit und begrenzt den App-Zugriff auf schreibgeschützten Zugriff.

## Beispielcodes

- Python: [Agent Framework](./code_samples/04-python-agent-framework.ipynb)
- .NET: [Agent Framework](./code_samples/04-dotnet-agent-framework.md)

## Haben Sie weitere Fragen zum Tool Use Design Pattern?

Treten Sie dem [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D) bei, um andere Lernende zu treffen, an Sprechstunden teilzunehmen und Ihre Fragen zu KI-Agenten beantwortet zu bekommen.

## Zusätzliche Ressourcen

- <a href="https://microsoft.github.io/build-your-first-agent-with-azure-ai-agent-service-workshop/" target="_blank">Azure AI Agents Service Workshop</a>
- <a href="https://github.com/Azure-Samples/contoso-creative-writer/tree/main/docs/workshop" target="_blank">Contoso Creative Writer Multi-Agent Workshop</a>
- <a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Microsoft Agent Framework Übersicht</a>


## Schnelltest dieses Agenten (Optional)

Nachdem Sie gelernt haben, Agenten in [Lektion 16](../16-deploying-scalable-agents/README.md) bereitzustellen, können Sie den `TravelToolAgent` dieser Lektion mit [`tests/lesson-04-smoke-tests.json`](../../../tests/lesson-04-smoke-tests.json) schnelltesten (ruft er seine Werkzeuge weiterhin auf und antwortet?). Siehe [`tests/README.md`](../tests/README.md) für die Ausführung.

## Vorherige Lektion

[Verstehen agentischer Designmuster](../03-agentic-design-patterns/README.md)

## Nächste Lektion

[Agentic RAG](../05-agentic-rag/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Haftungsausschluss**:
Dieses Dokument wurde mit dem KI-Übersetzungsdienst [Co-op Translator](https://github.com/Azure/co-op-translator) übersetzt. Obwohl wir uns um Genauigkeit bemühen, beachten Sie bitte, dass automatisierte Übersetzungen Fehler oder Ungenauigkeiten enthalten können. Das Originaldokument in seiner Ursprungssprache gilt als maßgebliche Quelle. Bei kritischen Informationen wird eine professionelle menschliche Übersetzung empfohlen. Wir übernehmen keine Haftung für Missverständnisse oder Fehlinterpretationen, die aus der Verwendung dieser Übersetzung entstehen.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->