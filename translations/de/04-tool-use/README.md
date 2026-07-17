[![Wie man gute KI-Agenten entwirft](../../../translated_images/de/lesson-4-thumbnail.546162853cb3daff.webp)](https://youtu.be/vieRiPRx-gI?si=cEZ8ApnT6Sus9rhn)

> _(Klicken Sie auf das obige Bild, um das Video dieser Lektion anzusehen)_

# Entwurfsmuster für die Werkzeugnutzung

Werkzeuge sind interessant, weil sie KI-Agenten eine breitere Palette von Fähigkeiten ermöglichen. Anstatt dass der Agent nur eine begrenzte Anzahl von Aktionen ausführen kann, kann der Agent durch Hinzufügen eines Werkzeugs nun eine Vielzahl von Aktionen ausführen. In diesem Kapitel betrachten wir das Entwurfsmuster für die Werkzeugnutzung, das beschreibt, wie KI-Agenten bestimmte Werkzeuge nutzen können, um ihre Ziele zu erreichen.

## Einführung

In dieser Lektion möchten wir folgende Fragen beantworten:

- Was ist das Entwurfsmuster für die Werkzeugnutzung?
- Für welche Anwendungsfälle ist es anwendbar?
- Welche Elemente/Bausteine werden benötigt, um das Entwurfsmuster umzusetzen?
- Welche besonderen Überlegungen sind bei der Verwendung des Entwurfsmusters für die Werkzeugnutzung zu beachten, um vertrauenswürdige KI-Agenten zu bauen?

## Lernziele

Nach Abschluss dieser Lektion werden Sie in der Lage sein:

- Das Entwurfsmuster für die Werkzeugnutzung und dessen Zweck zu definieren.
- Anwendungsfälle zu erkennen, bei denen das Entwurfsmuster für die Werkzeugnutzung anwendbar ist.
- Die wichtigsten Elemente zum Implementieren des Entwurfsmusters zu verstehen.
- Überlegungen zur Gewährleistung der Vertrauenswürdigkeit von KI-Agenten bei Nutzung dieses Entwurfsmusters zu erkennen.

## Was ist das Entwurfsmuster für die Werkzeugnutzung?

Das **Entwurfsmuster für die Werkzeugnutzung** konzentriert sich darauf, LLMs die Fähigkeit zu geben, mit externen Werkzeugen zu interagieren, um spezifische Ziele zu erreichen. Werkzeuge sind Code, der von einem Agenten ausgeführt werden kann, um Aktionen durchzuführen. Ein Werkzeug kann eine einfache Funktion sein, wie ein Taschenrechner, oder ein API-Aufruf zu einem Drittanbieterdienst wie der Abfrage von Aktienkursen oder Wettervorhersagen. Im Kontext von KI-Agenten sind Werkzeuge so konzipiert, dass sie als Reaktion auf **modellgenerierte Funktionsaufrufe** von Agenten ausgeführt werden.

## Für welche Anwendungsfälle ist es anwendbar?

KI-Agenten können Werkzeuge nutzen, um komplexe Aufgaben zu erledigen, Informationen abzurufen oder Entscheidungen zu treffen. Das Entwurfsmuster für die Werkzeugnutzung wird häufig in Szenarien verwendet, die eine dynamische Interaktion mit externen Systemen wie Datenbanken, Webdiensten oder Code-Interpretern erfordern. Diese Fähigkeit ist nützlich für verschiedene Anwendungsfälle, darunter:

- **Dynamische Informationsbeschaffung:** Agenten können externe APIs oder Datenbanken abfragen, um aktuelle Daten abzurufen (z. B. Abfrage einer SQLite-Datenbank zur Datenanalyse, Abrufen von Aktienkursen oder Wetterinformationen).
- **Codeausführung und -interpretation:** Agenten können Code oder Skripte ausführen, um mathematische Probleme zu lösen, Berichte zu erstellen oder Simulationen durchzuführen.
- **Workflow-Automatisierung:** Automatisierung von sich wiederholenden oder mehrstufigen Arbeitsabläufen durch Integration von Werkzeugen wie Aufgabenplanern, E-Mail-Diensten oder Datenpipelines.
- **Kundensupport:** Agenten können mit CRM-Systemen, Ticketplattformen oder Wissensdatenbanken interagieren, um Benutzeranfragen zu lösen.
- **Inhaltserstellung und -bearbeitung:** Agenten können Werkzeuge wie Grammatikprüfer, Textzusammenfasser oder Inhalts-Sicherheitsbewertungsprogramme nutzen, um bei der Erstellung von Inhalten zu unterstützen.

## Welche Elemente/Bausteine sind nötig, um das Entwurfsmuster für die Werkzeugnutzung zu implementieren?

Diese Bausteine ermöglichen es dem KI-Agenten, eine Vielzahl von Aufgaben auszuführen. Betrachten wir die Schlüsselelemente, die zur Implementierung des Entwurfsmusters für die Werkzeugnutzung benötigt werden:

- **Funktions-/Werkzeugschemata**: Detaillierte Definitionen verfügbarer Werkzeuge, einschließlich Funktionsname, Zweck, erforderliche Parameter und erwartete Ausgaben. Diese Schemata ermöglichen es dem LLM, zu verstehen, welche Werkzeuge verfügbar sind und wie gültige Anfragen zu erstellen sind.

- **Logik zur Ausführung von Funktionen:** Steuert, wie und wann Werkzeuge basierend auf der Absicht des Benutzers und dem Gesprächskontext aufgerufen werden. Dies kann Planungsmodule, Routing-Mechanismen oder bedingte Abläufe umfassen, die die Werkzeugnutzung dynamisch steuern.

- **Nachrichtenverwaltungssystem:** Komponenten, die den Gesprächsverlauf zwischen Benutzereingaben, LLM-Antworten, Werkzeugaufrufen und Werkzeugausgaben verwalten.

- **Werkzeugintegrations-Framework:** Infrastruktur, die den Agenten mit verschiedenen Werkzeugen verbindet, egal ob einfache Funktionen oder komplexe externe Dienste.

- **Fehlerbehandlung und Validierung:** Mechanismen zur Behandlung von Fehlern bei der Werkzeugausführung, zur Validierung von Parametern und zur Verwaltung unerwarteter Antworten.

- **Zustandsverwaltung:** Verfolgt den Gesprächskontext, vorherige Werkzeuginteraktionen und persistente Daten, um Konsistenz über mehrere Gesprächsrunden hinweg sicherzustellen.

Als Nächstes betrachten wir den Funktions-/Werkzeugaufruf etwas genauer.
 
### Funktions-/Werkzeugaufruf

Funktionsaufrufe sind der primäre Weg, wie wir Large Language Models (LLMs) ermöglichen, mit Werkzeugen zu interagieren. Sie werden oft synonym verwendet, da „Funktionen“ (wiederverwendbare Codeblöcke) die „Werkzeuge“ sind, die Agenten zur Ausführung von Aufgaben benutzen. Damit der Code einer Funktion aufgerufen werden kann, muss ein LLM die Benutzeranfrage mit der Funktionsbeschreibung abgleichen. Hierfür wird ein Schema mit den Beschreibungen aller verfügbaren Funktionen an das LLM gesendet. Das LLM wählt dann die passendste Funktion für die Aufgabe aus und gibt deren Namen und Argumente zurück. Die ausgewählte Funktion wird ausgeführt, ihre Antwort wird an das LLM zurückgesendet, das diese Informationen nutzt, um auf die Benutzeranfrage zu antworten.

Entwickler benötigen für die Implementierung von Funktionsaufrufen bei Agenten:

1. Ein LLM-Modell, das Funktionsaufrufe unterstützt
2. Ein Schema mit Funktionsbeschreibungen
3. Den Code für jede beschriebene Funktion

Nutzen wir das Beispiel, die aktuelle Uhrzeit in einer Stadt zu ermitteln, zur Veranschaulichung:

1. **Initialisieren eines LLM, das Funktionsaufrufe unterstützt:**

    Nicht alle Modelle unterstützen Funktionsaufrufe, deshalb ist es wichtig zu prüfen, ob das verwendete LLM diese Funktion bietet.     <a href="https://learn.microsoft.com/azure/ai-services/openai/how-to/function-calling" target="_blank">Azure OpenAI</a> unterstützt Funktionsaufrufe. Wir können beginnen, indem wir den OpenAI-Client gegen die Azure OpenAI **Responses API** initialisieren (den stabilen `/openai/v1/` Endpunkt — keine `api_version` nötig). 

    ```python
    # Initialisieren Sie den OpenAI-Client für Azure OpenAI (Responses API, v1-Endpunkt)
    client = OpenAI(
        base_url=f"{os.environ['AZURE_OPENAI_ENDPOINT'].rstrip('/')}/openai/v1/",
        api_key=os.environ["AZURE_OPENAI_API_KEY"],
    )
    deployment_name = os.environ["AZURE_OPENAI_DEPLOYMENT"]
    ```

1. **Erstellen eines Funktionsschemas**:

    Als nächstes definieren wir ein JSON-Schema, das den Funktionsnamen, eine Beschreibung dessen, was die Funktion tut, sowie die Namen und Beschreibungen der Funktionsparameter enthält.
    Dieses Schema wird dann zusammen mit der Benutzeranfrage an den zuvor erstellten Client weitergegeben, um die Uhrzeit in San Francisco zu ermitteln. Wichtig ist, dass ein **Werkzeugaufruf** zurückgegeben wird, **nicht** die endgültige Antwort auf die Frage. Wie bereits erwähnt, gibt das LLM den Namen der für die Aufgabe ausgewählten Funktion und die Argumente zurück, die an diese übergeben werden.

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
  
    # Anfangsnachricht des Benutzers
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
  
1. **Der Funktion-Code zur Ausführung der Aufgabe:**

    Nachdem das LLM gewählt hat, welche Funktion ausgeführt werden muss, muss der Code zur Erledigung der Aufgabe implementiert und ausgeführt werden.
    Wir können den Code zur Ermittlung der aktuellen Uhrzeit in Python implementieren. Außerdem müssen wir Code schreiben, um aus der response_message den Funktionsnamen und die Argumente zu extrahieren, um das endgültige Ergebnis zu erhalten.

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
    # Funktionsaufrufe behandeln
    tool_calls = [item for item in response.output if item.type == "function_call"]
    if tool_calls:
        for tool_call in tool_calls:
            if tool_call.name == "get_current_time":

                function_args = json.loads(tool_call.arguments)

                time_response = get_current_time(
                    location=function_args.get("location")
                )

                # Gibt das Werkzeugergebnis als ein function_call_output-Element zurück
                messages.append({
                    "type": "function_call_output",
                    "call_id": tool_call.call_id,
                    "output": time_response,
                })
    else:
        print("No tool calls were made by the model.")

    # Zweiter API-Aufruf: Holen Sie die endgültige Antwort vom Modell
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

Funktionsaufrufe sind das Herzstück der meisten, wenn nicht aller Entwurfsmuster für die Werkzeugnutzung bei Agenten, ihre Implementierung von Grund auf kann jedoch manchmal eine Herausforderung darstellen.
Wie wir in [Lektion 2](../../../02-explore-agentic-frameworks) gelernt haben, bieten agentenhafte Frameworks vorgefertigte Bausteine zur Umsetzung der Werkzeugnutzung.
 
## Beispiele für Werkzeugnutzung mit agentenhaften Frameworks

Hier sind einige Beispiele, wie Sie das Entwurfsmuster für die Werkzeugnutzung mit verschiedenen agentenhaften Frameworks implementieren können:

### Microsoft Agent Framework

<a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Microsoft Agent Framework</a> ist ein Open-Source-KI-Framework zum Aufbau von KI-Agenten. Es vereinfacht den Prozess der Verwendung von Funktionsaufrufen, indem Sie Werkzeuge als Python-Funktionen mit dem `@tool`-Decorator definieren können. Das Framework übernimmt die Kommunikation zwischen dem Modell und Ihrem Code. Es bietet zudem Zugriff auf vorgefertigte Werkzeuge wie Dateisuche und Code-Interpreter über `FoundryChatClient`.

Das folgende Diagramm veranschaulicht den Prozess von Funktionsaufrufen mit dem Microsoft Agent Framework:

![Funktionsaufruf](../../../translated_images/de/functioncalling-diagram.a84006fc287f6014.webp)

Im Microsoft Agent Framework werden Werkzeuge als dekorierte Funktionen definiert. Wir können die zuvor gezeigte Funktion `get_current_time` durch den `@tool`-Decorator in ein Werkzeug umwandeln. Das Framework serialisiert automatisch die Funktion und ihre Parameter und erstellt das Schema, das an das LLM gesendet wird.

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

<a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Microsoft Foundry Agent Service</a> ist ein neueres agentenhaftes Framework, das Entwicklern ermöglicht, sicher KI-Agenten in hoher Qualität und Erweiterbarkeit zu bauen, bereitzustellen und zu skalieren, ohne sich um die zugrunde liegende Rechen- und Speicherinfrastruktur kümmern zu müssen. Es ist besonders nützlich für Unternehmenseinsätze, da es ein vollständig verwalteter Dienst mit Sicherheitsstandards auf Unternehmensniveau ist.

Im Vergleich zur direkten Entwicklung mit der LLM-API bietet Microsoft Foundry Agent Service einige Vorteile, darunter:

- Automatischer Werkzeugaufruf – kein Bedarf, Werkzeugaufrufe zu parsen, das Werkzeug aufzurufen und die Antwort zu verarbeiten; dies geschieht jetzt serverseitig
- Sicher verwaltete Daten – anstelle der Verwaltung eines eigenen Gesprächszustands können Threads genutzt werden, um alle benötigten Informationen zu speichern
- Sofort einsatzbereite Werkzeuge – Werkzeuge, mit denen Sie Ihre Datenquellen wie Bing, Azure AI Search und Azure Functions nutzen können.

Die im Microsoft Foundry Agent Service verfügbaren Werkzeuge lassen sich in zwei Kategorien einteilen:

1. Wissenswerkzeuge:
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/bing-grounding?tabs=python&pivots=overview" target="_blank">Anbindung an Bing Search</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/file-search?tabs=python&pivots=overview" target="_blank">Dateisuche</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-ai-search?tabs=azurecli%2Cpython&pivots=overview-azure-ai-search" target="_blank">Azure AI Search</a>

2. Aktionswerkzeuge:
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/function-calling?tabs=python&pivots=overview" target="_blank">Funktionsaufrufe</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/code-interpreter?tabs=python&pivots=overview" target="_blank">Code-Interpreter</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/openapi-spec?tabs=python&pivots=overview" target="_blank">OpenAPI-definierte Werkzeuge</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-functions?pivots=overview" target="_blank">Azure Functions</a>

Der Agent Service ermöglicht es uns, diese Werkzeuge gemeinsam als `toolset` zu nutzen. Außerdem nutzt er `Threads`, die die Nachrichtenhistorie eines bestimmten Gesprächs verfolgen.

Stellen Sie sich vor, Sie sind Vertriebsmitarbeiter bei einem Unternehmen namens Contoso. Sie möchten einen Konversationsagenten entwickeln, der Fragen zu Ihren Verkaufsdaten beantworten kann.

Das folgende Bild veranschaulicht, wie Sie Microsoft Foundry Agent Service zur Analyse Ihrer Verkaufsdaten nutzen könnten:

![Agentic Service im Einsatz](../../../translated_images/de/agent-service-in-action.34fb465c9a84659e.webp)

Um eines dieser Werkzeuge mit dem Service zu verwenden, können wir einen Client erstellen und ein Werkzeug oder Toolset definieren. Praktisch umgesetzt kann dies mit dem folgenden Python-Code geschehen. Das LLM wird das Toolset anschauen und je nach Benutzeranfrage entscheiden, ob es die vom Benutzer erstellte Funktion `fetch_sales_data_using_sqlite_query` oder den vorgefertigten Code Interpreter verwendet.

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

# Werkzeugset initialisieren
toolset = ToolSet()

# Funktion Calling Agent mit der Funktion fetch_sales_data_using_sqlite_query initialisieren und zum Werkzeugset hinzufügen
fetch_data_function = FunctionTool(fetch_sales_data_using_sqlite_query)
toolset.add(fetch_data_function)

# Code Interpreter Werkzeug initialisieren und zum Werkzeugset hinzufügen.
code_interpreter = CodeInterpreterTool()toolset.add(code_interpreter)

agent = project_client.agents.create_agent(
    model="gpt-4.1-mini", name="my-agent", instructions="You are helpful agent", 
    toolset=toolset
)
```

## Welche besonderen Überlegungen sind bei der Verwendung des Entwurfsmusters für die Werkzeugnutzung zur Entwicklung vertrauenswürdiger KI-Agenten zu beachten?

Ein häufiges Anliegen bei dynamisch von LLMs erzeugtem SQL ist die Sicherheit, insbesondere das Risiko von SQL-Injektionen oder schädlichen Aktionen wie dem Löschen oder Manipulieren der Datenbank. Obwohl diese Bedenken berechtigt sind, können sie effektiv durch eine angemessene Konfiguration der Datenbankzugriffsrechte gemindert werden. Für die meisten Datenbanken bedeutet dies die Konfiguration als schreibgeschützt. Bei Datenbankdiensten wie PostgreSQL oder Azure SQL sollte die App eine schreibgeschützte (SELECT) Rolle zugewiesen bekommen.

Der Betrieb der App in einer sicheren Umgebung erhöht den Schutz zusätzlich. In Unternehmensszenarien werden Daten typischerweise aus den operativen Systemen extrahiert und in eine schreibgeschützte Datenbank oder ein Data Warehouse mit benutzerfreundlichem Schema transformiert. Dieser Ansatz stellt sicher, dass die Daten sicher sind, für Leistung und Zugänglichkeit optimiert wurden und die App nur eingeschränkten, schreibgeschützten Zugriff hat.

## Beispielcode

- Python: [Agent Framework](./code_samples/04-python-agent-framework.ipynb)
- .NET: [Agent Framework](./code_samples/04-dotnet-agent-framework.md)

## Haben Sie weitere Fragen zum Entwurfsmuster für die Werkzeugnutzung?

Treten Sie dem [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D) bei, um andere Lernende zu treffen, an Sprechstunden teilzunehmen und Ihre Fragen zu KI-Agenten zu klären.

## Zusätzliche Ressourcen

- <a href="https://microsoft.github.io/build-your-first-agent-with-azure-ai-agent-service-workshop/" target="_blank">Azure AI Agents Service Workshop</a>
- <a href="https://github.com/Azure-Samples/contoso-creative-writer/tree/main/docs/workshop" target="_blank">Contoso Creative Writer Multi-Agent Workshop</a>
- <a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Microsoft Agent Framework Übersicht</a>


## Smoke-Tests für diesen Agenten (Optional)

Nachdem Sie gelernt haben, Agenten in [Lektionen 16](../16-deploying-scalable-agents/README.md) zu deployen, können Sie den `TravelToolAgent` dieser Lektion mit [`tests/lesson-04-smoke-tests.json`](../../../tests/lesson-04-smoke-tests.json) einem Smoke-Test unterziehen (ruft er seine Tools noch auf und antwortet?). Siehe [`tests/README.md`](../tests/README.md) für den Ablauf.

## Vorherige Lektion

[Agentur-Designmuster verstehen](../03-agentic-design-patterns/README.md)

## Nächste Lektion

[Agentur RAG](../05-agentic-rag/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Haftungsausschluss**:
Dieses Dokument wurde mit dem KI-Übersetzungsdienst [Co-op Translator](https://github.com/Azure/co-op-translator) übersetzt. Obwohl wir uns um Genauigkeit bemühen, beachten Sie bitte, dass automatisierte Übersetzungen Fehler oder Ungenauigkeiten enthalten können. Das Originaldokument in seiner Ursprungssprache gilt als maßgebliche Quelle. Bei kritischen Informationen wird eine professionelle menschliche Übersetzung empfohlen. Wir übernehmen keine Haftung für Missverständnisse oder Fehlinterpretationen, die aus der Verwendung dieser Übersetzung entstehen.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->