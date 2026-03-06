# Erkundung des Microsoft Agent Framework

![Agent Framework](../../../translated_images/de/lesson-14-thumbnail.90df0065b9d234ee.webp)

### Einführung

Diese Lektion behandelt:

- Verständnis des Microsoft Agent Framework: Hauptmerkmale und Wert  
- Erkundung der Schlüsselkonzepte des Microsoft Agent Framework
- Fortgeschrittene MAF-Muster: Workflows, Middleware und Speicher

## Lernziele

Nach Abschluss dieser Lektion wissen Sie, wie Sie:

- Produktionsreife KI-Agenten mit Microsoft Agent Framework erstellen
- Die Kernfunktionen des Microsoft Agent Framework auf Ihre agentischen Anwendungsfälle anwenden
- Fortgeschrittene Muster wie Workflows, Middleware und Beobachtbarkeit verwenden

## Codebeispiele 

Codebeispiele für [Microsoft Agent Framework (MAF)](https://aka.ms/ai-agents-beginners/agent-framewrok) sind in diesem Repository unter den Dateien `xx-python-agent-framework` und `xx-dotnet-agent-framework` zu finden.

## Verständnis des Microsoft Agent Framework

![Framework Intro](../../../translated_images/de/framework-intro.077af16617cf130c.webp)

[Microsoft Agent Framework (MAF)](https://aka.ms/ai-agents-beginners/agent-framewrok) ist Microsofts einheitliches Framework zum Erstellen von KI-Agenten. Es bietet die Flexibilität, die breite Vielfalt agentischer Anwendungsfälle zu adressieren, die sowohl in Produktions- als auch in Forschungsumgebungen vorkommen, darunter:

- **Sequenzielle Agenten-Orchestrierung** in Szenarien, in denen Schritt-für-Schritt-Workflows nötig sind.
- **Gleichzeitige Orchestrierung** in Szenarien, in denen Agenten Aufgaben gleichzeitig erledigen müssen.
- **Gruppenchat-Orchestrierung** in Szenarien, in denen Agenten gemeinsam an einer Aufgabe arbeiten.
- **Übergabe-Orchestrierung** in Szenarien, in denen Agenten Aufgaben untereinander übergeben, sobald Teilschritte abgeschlossen sind.
- **Magnetische Orchestrierung** in Szenarien, in denen ein Manager-Agent eine Aufgabenliste erstellt und verwaltet und die Koordination der Unteragenten zur Aufgabenerledigung übernimmt.

Um KI-Agenten in der Produktion bereitzustellen, enthält MAF zudem Funktionen für:

- **Beobachtbarkeit** durch die Nutzung von OpenTelemetry, wobei jede Aktion des KI-Agenten, inklusive Werkzeugaufrufen, Orchestrierungsschritten, Reasoning-Flows und Leistungsüberwachung über Microsoft Foundry Dashboards, erfasst wird.
- **Sicherheit** durch nativen Hosting der Agenten auf Microsoft Foundry, das Sicherheitskontrollen wie rollenbasierte Zugriffe, Umgang mit privaten Daten und integrierte Inhaltsicherheit umfasst.
- **Zuverlässigkeit** da Agentenprozesse und Workflows pausieren, fortsetzen und Fehler wiederherstellen können, was längere Abläufe ermöglicht.
- **Kontrolle** durch Unterstützung von Human-in-the-Loop Workflows, bei denen Aufgaben als menschlich genehmigungspflichtig markiert werden.

Microsoft Agent Framework legt außerdem Wert auf Interoperabilität durch:

- **Cloud-Agnostizität** - Agenten können in Containern, lokal und auf verschiedenen Clouds ausgeführt werden.
- **Anbieter-Agnostizität** - Agenten können mit dem bevorzugten SDK erstellt werden, einschließlich Azure OpenAI und OpenAI
- **Integration offener Standards** - Agenten können Protokolle wie Agent-to-Agent (A2A) und Model Context Protocol (MCP) verwenden, um andere Agenten und Werkzeuge zu entdecken und zu nutzen.
- **Plugins und Connectoren** - Verbindungen können zu Daten- und Speicher-Diensten wie Microsoft Fabric, SharePoint, Pinecone und Qdrant hergestellt werden.

Sehen wir uns an, wie diese Funktionen auf einige der Kernkonzepte des Microsoft Agent Framework angewandt werden.

## Schlüsselkonzepte des Microsoft Agent Framework

### Agenten

![Agent Framework](../../../translated_images/de/agent-components.410a06daf87b4fef.webp)

**Agenten erstellen**

Die Agentenerstellung erfolgt durch die Definition des Inferenzdienstes (LLM-Anbieter), einer Reihe von Anweisungen, denen der KI-Agent folgen soll, und einem zugewiesenen `name`:

```python
agent = AzureOpenAIChatClient(credential=AzureCliCredential()).create_agent( instructions="You are good at recommending trips to customers based on their preferences.", name="TripRecommender" )
```

Oben wird `Azure OpenAI` verwendet, aber Agenten können mit verschiedenen Diensten erstellt werden, darunter `Microsoft Foundry Agent Service`:

```python
AzureAIAgentClient(async_credential=credential).create_agent( name="HelperAgent", instructions="You are a helpful assistant." ) as agent
```

OpenAI `Responses`, `ChatCompletion` APIs

```python
agent = OpenAIResponsesClient().create_agent( name="WeatherBot", instructions="You are a helpful weather assistant.", )
```

```python
agent = OpenAIChatClient().create_agent( name="HelpfulAssistant", instructions="You are a helpful assistant.", )
```

oder entfernte Agenten über das A2A-Protokoll:

```python
agent = A2AAgent( name=agent_card.name, description=agent_card.description, agent_card=agent_card, url="https://your-a2a-agent-host" )
```

**Agenten ausführen**

Agenten werden mit den Methoden `.run` oder `.run_stream` ausgeführt, je nachdem, ob nicht-streaming oder streaming Antworten gebraucht werden.

```python
result = await agent.run("What are good places to visit in Amsterdam?")
print(result.text)
```

```python
async for update in agent.run_stream("What are the good places to visit in Amsterdam?"):
    if update.text:
        print(update.text, end="", flush=True)

```

Jeder Agentenlauf kann auch Optionen zur Anpassung von Parametern wie `max_tokens` verwenden, welche vom Agent genutzt werden, `tools`, die der Agent aufrufen darf, sowie das tatsächlich verwendete `model`.

Dies ist nützlich in Fällen, in denen bestimmte Modelle oder Werkzeuge zur Erfüllung einer Benutzeraufgabe erforderlich sind.

**Werkzeuge**

Werkzeuge können sowohl bei der Definierung des Agenten festgelegt werden:

```python
def get_attractions( location: Annotated[str, Field(description="The location to get the top tourist attractions for")], ) -> str: """Get the top tourist attractions for a given location.""" return f"The top attractions for {location} are." 


# Beim direkten Erstellen eines ChatAgenten

agent = ChatAgent( chat_client=OpenAIChatClient(), instructions="You are a helpful assistant", tools=[get_attractions]

```

als auch beim Ausführen des Agenten:

```python

result1 = await agent.run( "What's the best place to visit in Seattle?", tools=[get_attractions] # Werkzeug nur für diesen Lauf bereitgestellt )
```

**Agenten-Threads**

Agenten-Threads werden verwendet, um Multi-Turn-Konversationen zu handhaben. Threads können entweder erstellt werden durch:

- Verwendung von `get_new_thread()`, wodurch der Thread langfristig gespeichert wird
- Automatische Thread-Erstellung bei Ausführung eines Agenten, wobei der Thread nur während des laufenden Requests besteht.

Der Code zur Thread-Erstellung sieht so aus:

```python
# Erstelle einen neuen Thread.
thread = agent.get_new_thread() # Führe den Agenten mit dem Thread aus.
response = await agent.run("Hello, I am here to help you book travel. Where would you like to go?", thread=thread)

```

Sie können den Thread anschließend serialisieren, um ihn später zu speichern:

```python
# Erstellen Sie einen neuen Thread.
thread = agent.get_new_thread() 

# Führen Sie den Agenten mit dem Thread aus.

response = await agent.run("Hello, how are you?", thread=thread) 

# Serialisieren Sie den Thread zur Speicherung.

serialized_thread = await thread.serialize() 

# Deserialisieren Sie den Thread-Zustand nach dem Laden aus dem Speicher.

resumed_thread = await agent.deserialize_thread(serialized_thread)
```

**Agenten-Middleware**

Agenten interagieren mit Werkzeugen und LLMs, um Benutzeraufgaben zu erledigen. In bestimmten Szenarien möchten wir Aktionen ausführen oder nachverfolgen zwischen diesen Interaktionen. Agenten-Middleware ermöglicht dies durch:

*Funktions-Middleware*

Diese Middleware erlaubt es, eine Aktion zwischen dem Agenten und einer Funktion/einem Werkzeug, das aufgerufen wird, auszuführen. Ein Beispiel hierfür ist das Logging eines Funktionsaufrufs.

Im folgenden Code definiert `next`, ob die nächste Middleware oder die eigentliche Funktion aufgerufen wird.

```python
async def logging_function_middleware(
    context: FunctionInvocationContext,
    next: Callable[[FunctionInvocationContext], Awaitable[None]],
) -> None:
    """Function middleware that logs function execution."""
    # Vorverarbeitung: Protokoll vor der Funktionsausführung
    print(f"[Function] Calling {context.function.name}")

    # Weiter zur nächsten Middleware oder Funktionsausführung
    await next(context)

    # Nachbearbeitung: Protokoll nach der Funktionsausführung
    print(f"[Function] {context.function.name} completed")
```

*Chat-Middleware*

Diese Middleware ermöglicht es, eine Aktion zwischen dem Agenten und den Anfragen an das LLM auszuführen oder zu protokollieren.

Sie enthält wichtige Informationen wie die `messages`, die an den KI-Dienst gesendet werden.

```python
async def logging_chat_middleware(
    context: ChatContext,
    next: Callable[[ChatContext], Awaitable[None]],
) -> None:
    """Chat middleware that logs AI interactions."""
    # Vorverarbeitung: Protokollieren vor dem KI-Aufruf
    print(f"[Chat] Sending {len(context.messages)} messages to AI")

    # Weiter zum nächsten Middleware- oder KI-Dienst
    await next(context)

    # Nachverarbeitung: Protokollieren nach KI-Antwort
    print("[Chat] AI response received")

```

**Agenten-Speicher**

Wie in der Lektion `Agentic Memory` behandelt, ist Speicher ein wichtiges Element, damit der Agent über verschiedene Kontexte hinweg agieren kann. MAF bietet mehrere verschiedene Speicherarten:

*Speicher im Arbeitsspeicher*

Dies ist der Speicher, der in Threads während der Laufzeit der Anwendung gespeichert wird.

```python
# Erstellen Sie einen neuen Thread.
thread = agent.get_new_thread() # Führen Sie den Agenten mit dem Thread aus.
response = await agent.run("Hello, I am here to help you book travel. Where would you like to go?", thread=thread)
```

*Persistente Nachrichten*

Dieser Speicher wird verwendet, um Gesprächsverläufe über verschiedene Sitzungen hinweg zu speichern. Er wird definiert durch die `chat_message_store_factory`:

```python
from agent_framework import ChatMessageStore

# Erstellen Sie einen benutzerdefinierten Nachrichtenpeicher
def create_message_store():
    return ChatMessageStore()

agent = ChatAgent(
    chat_client=OpenAIChatClient(),
    instructions="You are a Travel assistant.",
    chat_message_store_factory=create_message_store
)

```

*Dynamischer Speicher*

Dieser Speicher wird zum Kontext hinzugefügt, bevor Agenten ausgeführt werden. Diese Speicher können in externen Diensten wie mem0 gespeichert werden:

```python
from agent_framework.mem0 import Mem0Provider

# Verwendung von Mem0 für erweiterte Speicherfunktionen
memory_provider = Mem0Provider(
    api_key="your-mem0-api-key",
    user_id="user_123",
    application_id="my_app"
)

agent = ChatAgent(
    chat_client=OpenAIChatClient(),
    instructions="You are a helpful assistant with memory.",
    context_providers=memory_provider
)

```

**Agenten-Beobachtbarkeit**

Beobachtbarkeit ist wichtig für den Aufbau zuverlässiger und wartbarer agentischer Systeme. MAF integriert OpenTelemetry, um Tracing und Metriken für bessere Beobachtbarkeit bereitzustellen.

```python
from agent_framework.observability import get_tracer, get_meter

tracer = get_tracer()
meter = get_meter()
with tracer.start_as_current_span("my_custom_span"):
    # etwas tun
    pass
counter = meter.create_counter("my_custom_counter")
counter.add(1, {"key": "value"})
```

### Workflows

MAF bietet Workflows, die vordefinierte Schritte zur Erfüllung einer Aufgabe sind und KI-Agenten als Komponenten in diesen Schritten beinhalten.

Workflows bestehen aus verschiedenen Komponenten, die einen besseren Kontrollfluss erlauben. Workflows ermöglichen außerdem **Multi-Agenten-Orchestrierung** und **Checkpointing**, um Workflow-Zustände zu speichern.

Die Kernkomponenten eines Workflows sind:

**Executor**

Executors erhalten Eingabenachrichten, führen ihre zugewiesenen Aufgaben aus und produzieren dann eine Ausgabenachricht. Dies bringt den Workflow voran, um die umfassendere Aufgabe zu erfüllen. Executors können entweder KI-Agenten oder benutzerdefinierte Logik sein.

**Kanten**

Kanten definieren den Fluss von Nachrichten in einem Workflow. Diese können sein:

*Direkte Kanten* - Einfache Eins-zu-Eins-Verbindungen zwischen Executoren:

```python
from agent_framework import WorkflowBuilder

builder = WorkflowBuilder()
builder.add_edge(source_executor, target_executor)
builder.set_start_executor(source_executor)
workflow = builder.build()
```

*Bedingte Kanten* - Werden aktiviert, wenn eine bestimmte Bedingung erfüllt ist. Zum Beispiel, wenn Hotelzimmer nicht verfügbar sind, kann ein Executor andere Optionen vorschlagen.

*Switch-Case-Kanten* - Leiten Nachrichten basierend auf definierten Bedingungen an verschiedene Executor weiter. Zum Beispiel, wenn ein Reisekunde Prioritätszugang hat und seine Aufgaben über einen anderen Workflow abgehandelt werden.

*Fan-out-Kanten* - Senden eine Nachricht an mehrere Ziele.

*Fan-in-Kanten* - Sammeln mehrere Nachrichten von verschiedenen Executoren und senden sie an ein Ziel.

**Ereignisse**

Zur besseren Beobachtbarkeit von Workflows bietet MAF integrierte Ereignisse für die Ausführung, darunter:

- `WorkflowStartedEvent`  - Workflow-Ausführung beginnt
- `WorkflowOutputEvent` - Workflow erzeugt eine Ausgabe
- `WorkflowErrorEvent` - Workflow trifft auf einen Fehler
- `ExecutorInvokeEvent`  - Executor beginnt Verarbeiten
- `ExecutorCompleteEvent`  -  Executor beendet Verarbeiten
- `RequestInfoEvent` - Eine Anfrage wird ausgelöst

## Fortgeschrittene MAF-Muster

Die obigen Abschnitte behandeln die Schlüsselkonzepte des Microsoft Agent Framework. Wenn Sie komplexere Agenten bauen, hier einige fortgeschrittene Muster zur Berücksichtigung:

- **Middleware-Komposition**: Verkettung mehrerer Middleware-Handler (Logging, Auth, Rate-Limiting) mittels Funktions- und Chat-Middleware für feingranulare Steuerung des Agentenverhaltens.
- **Workflow-Checkpointing**: Verwendung von Workflow-Ereignissen und Serialisierung zum Speichern und Fortsetzen lang laufender Agentenprozesse.
- **Dynamische Werkzeugauswahl**: Kombination von RAG über Werkzeugbeschreibungen mit der MAF-Werkzeugregistrierung, um nur relevante Werkzeuge pro Anfrage bereitzustellen.
- **Multi-Agenten-Übergabe**: Verwendung von Workflow-Kanten und bedingter Weiterleitung zur Orchestrierung der Übergabe zwischen spezialisierten Agenten.

## Codebeispiele 

Codebeispiele für Microsoft Agent Framework sind in diesem Repository unter den Dateien `xx-python-agent-framework` und `xx-dotnet-agent-framework` zu finden.

## Haben Sie weitere Fragen zum Microsoft Agent Framework?

Treten Sie dem [Microsoft Foundry Discord](https://aka.ms/ai-agents/discord) bei, um andere Lernende zu treffen, Office Hours zu besuchen und Antworten auf Ihre Fragen zu AI-Agenten zu erhalten.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Haftungsausschluss**:  
Dieses Dokument wurde mit dem KI-Übersetzungsdienst [Co-op Translator](https://github.com/Azure/co-op-translator) übersetzt. Obwohl wir um Genauigkeit bemüht sind, weisen wir darauf hin, dass automatisierte Übersetzungen Fehler oder Ungenauigkeiten enthalten können. Das Originaldokument in seiner Ursprungssprache gilt als maßgebliche Quelle. Für wichtige Informationen wird eine professionelle menschliche Übersetzung empfohlen. Wir übernehmen keine Haftung für Missverständnisse oder Fehlinterpretationen, die aus der Verwendung dieser Übersetzung entstehen.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->