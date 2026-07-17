# Erkundung des Microsoft Agent Frameworks

![Agent Framework](../../../translated_images/de/lesson-14-thumbnail.90df0065b9d234ee.webp)

### Einführung

Diese Lektion behandelt:

- Verständnis des Microsoft Agent Frameworks: Hauptfunktionen und Wert  
- Erkundung der Schlüsselkonstrukte des Microsoft Agent Frameworks
- Fortgeschrittene MAF-Muster: Workflows, Middleware und Speicher

## Lernziele

Nach Abschluss dieser Lektion wissen Sie, wie Sie:

- Produktionsreife KI-Agenten mit dem Microsoft Agent Framework erstellen
- Die Kernfunktionen des Microsoft Agent Frameworks auf Ihre Agenten-Anwendungsfälle anwenden
- Erweiterte Muster wie Workflows, Middleware und Beobachtbarkeit nutzen

## Code-Beispiele 

Code-Beispiele für das [Microsoft Agent Framework (MAF)](https://aka.ms/ai-agents-beginners/agent-framework) finden Sie in diesem Repository unter den Dateien `xx-python-agent-framework` und `xx-dotnet-agent-framework`.

## Verständnis des Microsoft Agent Frameworks

![Framework Intro](../../../translated_images/de/framework-intro.077af16617cf130c.webp)

Das [Microsoft Agent Framework (MAF)](https://aka.ms/ai-agents-beginners/agent-framework) ist Microsofts einheitliches Framework zur Erstellung von KI-Agenten. Es bietet die Flexibilität, die breite Palette agentischer Anwendungsfälle abzudecken, die sowohl in produktiven als auch Forschungsumgebungen vorkommen, darunter:

- **Sequenzielle Agenten-Orchestrierung** in Szenarien, in denen Schritt-für-Schritt-Workflows benötigt werden.
- **Parallele Orchestrierung** in Szenarien, in denen Agenten Aufgaben gleichzeitig erledigen müssen.
- **Gruppen-Chat-Orchestrierung** in Szenarien, in denen Agenten gemeinsam an einer Aufgabe arbeiten können.
- **Übergabe-Orchestrierung** in Szenarien, in denen Agenten Aufgaben aneinander übergeben, wenn Teilschritte abgeschlossen sind.
- **Magnetische Orchestrierung** in Szenarien, in denen ein Manager-Agent eine Aufgabenliste erstellt und modifiziert und die Koordination von Unteragenten zur Aufgabe übernimmt.

Um KI-Agenten produktiv bereitzustellen, enthält MAF auch Funktionen für:

- **Beobachtbarkeit** durch den Einsatz von OpenTelemetry, wobei jede Aktion des KI-Agenten, einschließlich Werkzeugaufruf, Orchestrierungsschritten, Begründungsabläufen und Leistungsüberwachung über Microsoft Foundry-Dashboards, verfolgt wird.
- **Sicherheit** durch die native Bereitstellung der Agenten auf Microsoft Foundry, das Sicherheitskontrollen wie rollenbasierte Zugriffssteuerung, Umgang mit privaten Daten und integrierte Inhaltsicherheit umfasst.
- **Robustheit** durch Agenten-Threads und Workflows, die pausieren, fortgesetzt und Fehler beheben können, was längere Prozesse ermöglicht.
- **Kontrolle**, da Workflows mit menschlicher Einbindung unterstützt werden, bei denen Aufgaben als von menschlicher Genehmigung abhängig markiert sind.

Microsoft Agent Framework legt zudem Wert auf Interoperabilität durch:

- **Cloud-Unabhängigkeit** – Agenten können in Containern, lokal und auf verschiedenen Clouds ausgeführt werden.
- **Anbieter-Unabhängigkeit** – Agenten können mit Ihrem bevorzugten SDK erstellt werden, einschließlich Azure OpenAI und OpenAI.
- **Integration offener Standards** – Agenten können Protokolle wie Agent-to-Agent (A2A) und Model Context Protocol (MCP) nutzen, um andere Agenten und Werkzeuge zu entdecken und zu verwenden.
- **Plugins und Connectoren** – Verbindungen können zu Daten- und Speicherdiensten wie Microsoft Fabric, SharePoint, Pinecone und Qdrant hergestellt werden.

Schauen wir uns an, wie diese Funktionen auf einige der Kernkonzepte des Microsoft Agent Frameworks angewandt werden.

## Schlüsselkonstrukte des Microsoft Agent Frameworks

### Agenten

![Agent Framework](../../../translated_images/de/agent-components.410a06daf87b4fef.webp)

**Agenten erstellen**

Die Agentenerstellung erfolgt durch Definition des Inferenzdienstes (LLM-Anbieters), einer
Reihe von Anweisungen, denen der KI-Agent folgen soll, und der Zuweisung eines `Namens`:

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

oder [MiniMax](https://platform.minimaxi.com/), das eine OpenAI-kompatible API mit großen Kontextfenstern (bis zu 204K Tokens) bereitstellt:

```python
agent = OpenAIChatClient(base_url="https://api.minimax.io/v1", api_key=os.environ["MINIMAX_API_KEY"], model_id="MiniMax-M3").create_agent( name="HelpfulAssistant", instructions="You are a helpful assistant.", )
```

oder entfernte Agenten mit dem A2A-Protokoll:

```python
agent = A2AAgent( name=agent_card.name, description=agent_card.description, agent_card=agent_card, url="https://your-a2a-agent-host" )
```

**Agenten ausführen**

Agenten werden mit den Methoden `.run` oder `.run_stream` für nicht-Streaming- oder Streaming-Antworten ausgeführt.

```python
result = await agent.run("What are good places to visit in Amsterdam?")
print(result.text)
```

```python
async for update in agent.run_stream("What are the good places to visit in Amsterdam?"):
    if update.text:
        print(update.text, end="", flush=True)

```

Jeder Agentenlauf kann auch Optionen enthalten, um Parameter wie die verwendeten `max_tokens`, `tools`, die der Agent verwenden kann, und sogar das verwendete `model` anzupassen.

Das ist nützlich, wenn für die Erfüllung der Benutzeraufgabe bestimmte Modelle oder Werkzeuge erforderlich sind.

**Werkzeuge**

Werkzeuge können sowohl bei der Definition des Agenten festgelegt werden:

```python
def get_attractions( location: Annotated[str, Field(description="The location to get the top tourist attractions for")], ) -> str: """Get the top tourist attractions for a given location.""" return f"The top attractions for {location} are." 


# Beim direkten Erstellen eines ChatAgent

agent = ChatAgent( chat_client=OpenAIChatClient(), instructions="You are a helpful assistant", tools=[get_attractions]

```

als auch beim Ausführen des Agenten:

```python

result1 = await agent.run( "What's the best place to visit in Seattle?", tools=[get_attractions] # Werkzeug nur für diesen Lauf bereitgestellt )
```

**Agenten-Threads**

Agenten-Threads werden verwendet, um Multirunden-Konversationen zu verwalten. Threads können entweder durch:

- Nutzung von `get_new_thread()`, was ermöglicht, dass der Thread über die Zeit gespeichert wird.
- Automatische Erstellung eines Threads bei der Ausführung eines Agenten, wobei der Thread nur während des aktuellen Laufs besteht.

Zur Erstellung eines Threads sieht der Code so aus:

```python
# Erstelle einen neuen Thread.
thread = agent.get_new_thread() # Führe den Agenten mit dem Thread aus.
response = await agent.run("Hello, I am here to help you book travel. Where would you like to go?", thread=thread)

```

Der Thread kann dann serialisiert und für die spätere Verwendung gespeichert werden:

```python
# Einen neuen Thread erstellen.
thread = agent.get_new_thread() 

# Führe den Agenten mit dem Thread aus.

response = await agent.run("Hello, how are you?", thread=thread) 

# Serialisiere den Thread zur Speicherung.

serialized_thread = await thread.serialize() 

# Deserialisiere den Thread-Zustand nach dem Laden aus dem Speicher.

resumed_thread = await agent.deserialize_thread(serialized_thread)
```

**Agent Middleware**

Agenten interagieren mit Werkzeugen und LLMs, um Aufgaben der Benutzer zu erfüllen. In bestimmten Szenarien möchte man zwischen diesen Interaktionen Vorgänge ausführen oder verfolgen. Agent-Middleware ermöglicht dies durch:

*Funktions-Middleware*

Diese Middleware erlaubt, eine Aktion zwischen dem Agenten und einer Funktion/einem Werkzeug, das er aufruft, auszuführen. Zum Beispiel kann man die Middleware nutzen, um Funktionsaufrufe zu protokollieren.

Im Code unten definiert `next`, ob die nächste Middleware oder die eigentliche Funktion aufgerufen werden soll.

```python
async def logging_function_middleware(
    context: FunctionInvocationContext,
    next: Callable[[FunctionInvocationContext], Awaitable[None]],
) -> None:
    """Function middleware that logs function execution."""
    # Vorverarbeitung: Protokollieren vor der Funktionsausführung
    print(f"[Function] Calling {context.function.name}")

    # Fortfahren mit der nächsten Middleware oder Funktionsausführung
    await next(context)

    # Nachverarbeitung: Protokollieren nach der Funktionsausführung
    print(f"[Function] {context.function.name} completed")
```

*Chat-Middleware*

Diese Middleware erlaubt es, eine Aktion zwischen dem Agenten und den Anfragen an das LLM auszuführen oder zu protokollieren.

Sie enthält wichtige Informationen wie die `messages`, die an den KI-Dienst gesendet werden.

```python
async def logging_chat_middleware(
    context: ChatContext,
    next: Callable[[ChatContext], Awaitable[None]],
) -> None:
    """Chat middleware that logs AI interactions."""
    # Vorverarbeitung: Protokollieren vor dem KI-Aufruf
    print(f"[Chat] Sending {len(context.messages)} messages to AI")

    # Fortfahren zur nächsten Middleware oder zum KI-Dienst
    await next(context)

    # Nachbearbeitung: Protokollieren nach der KI-Antwort
    print("[Chat] AI response received")

```

**Agentenspeicher**

Wie in der Lektion `Agentic Memory` behandelt, ist Speicher ein wichtiges Element, um dem Agenten zu ermöglichen, über verschiedene Kontexte zu operieren. MAF bietet verschiedene Arten von Speicher:

*In-Memory-Speicher*

Das ist der in Threads während der Anwendungslaufzeit gespeicherte Speicher.

```python
# Erstellen Sie einen neuen Thread.
thread = agent.get_new_thread() # Führen Sie den Agenten mit dem Thread aus.
response = await agent.run("Hello, I am here to help you book travel. Where would you like to go?", thread=thread)
```

*Persistente Nachrichten*

Dieser Speicher wird verwendet, um den Gesprächsverlauf über verschiedene Sitzungen hinweg zu speichern. Er wird mit `chat_message_store_factory` definiert:

```python
from agent_framework import ChatMessageStore

# Erstelle einen benutzerdefinierten Nachrichtenspeicher
def create_message_store():
    return ChatMessageStore()

agent = ChatAgent(
    chat_client=OpenAIChatClient(),
    instructions="You are a Travel assistant.",
    chat_message_store_factory=create_message_store
)

```

*Dynamischer Speicher*

Dieser Speicher wird vor dem Ausführen von Agenten dem Kontext hinzugefügt. Diese Speicher können in externen Diensten wie mem0 abgelegt werden:

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

Beobachtbarkeit ist wichtig für den Aufbau zuverlässiger und wartbarer agentischer Systeme. MAF integriert OpenTelemetry, um Tracing und Metriken für bessere Beobachtbarkeit zu bieten.

```python
from agent_framework.observability import get_tracer, get_meter

tracer = get_tracer()
meter = get_meter()
with tracer.start_as_current_span("my_custom_span"):
    # mach etwas
    pass
counter = meter.create_counter("my_custom_counter")
counter.add(1, {"key": "value"})
```

### Workflows

MAF bietet Workflows an, die vordefinierte Schritte zur Erledigung einer Aufgabe umfassen und KI-Agenten als Komponenten in diesen Schritten enthalten.

Workflows bestehen aus verschiedenen Komponenten, die eine bessere Steuerung des Ablaufs erlauben. Workflows ermöglichen auch **Multi-Agent-Orchestrierung** und **Checkpointing**, um Workflow-Zustände zu speichern.

Die Kernkomponenten eines Workflows sind:

**Executor**

Executor erhalten Eingabenachrichten, führen ihre zugewiesenen Aufgaben aus und erzeugen dann eine Ausgabenachricht. Dadurch wird der Workflow vorangetrieben, um die größere Aufgabe zu erfüllen. Executor können entweder KI-Agenten oder benutzerdefinierte Logik sein.

**Kanten**

Kanten definieren den Nachrichtenfluss in einem Workflow. Diese können sein:

*Direkte Kanten* – einfache Eins-zu-Eins-Verbindungen zwischen Executor:

```python
from agent_framework import WorkflowBuilder

builder = WorkflowBuilder()
builder.add_edge(source_executor, target_executor)
builder.set_start_executor(source_executor)
workflow = builder.build()
```

*Bedingte Kanten* – werden aktiviert, nachdem eine bestimmte Bedingung erfüllt wurde. Zum Beispiel, wenn Hotelzimmer nicht verfügbar sind, kann ein Executor andere Optionen vorschlagen.

*Switch-Case-Kanten* – leiten Nachrichten auf verschiedene Executor basierend auf definierten Bedingungen. Zum Beispiel, wenn ein Reisekunde Vorrangzugang hat und seine Aufgaben durch einen anderen Workflow bearbeitet werden.

*Fan-out-Kanten* – senden eine Nachricht an mehrere Ziele.

*Fan-in-Kanten* – sammeln mehrere Nachrichten von verschiedenen Executor und senden sie an ein Ziel.

**Ereignisse**

Zur besseren Beobachtbarkeit von Workflows bietet MAF eingebaute Ereignisse während der Ausführung an, darunter:

- `WorkflowStartedEvent`  – Workflow-Ausführung beginnt
- `WorkflowOutputEvent` – Workflow erzeugt eine Ausgabe
- `WorkflowErrorEvent` – Workflow stößt auf einen Fehler
- `ExecutorInvokeEvent`  – Executor beginnt mit der Verarbeitung
- `ExecutorCompleteEvent`  – Executor beendet die Verarbeitung
- `RequestInfoEvent` – Eine Anforderung wird ausgegeben

## Fortgeschrittene MAF-Muster

Die obigen Abschnitte behandeln die Schlüsselkonstrukte des Microsoft Agent Frameworks. Beim Erstellen komplexerer Agenten gibt es einige fortgeschrittene Muster zu beachten:

- **Middleware-Komposition**: Verkettung mehrerer Middleware-Handler (Logging, Authentifizierung, Ratenbegrenzung) mit Funktion- und Chat-Middleware für feinkörnige Steuerung des Agentenverhaltens.
- **Workflow-Checkpointing**: Workflow-Ereignisse und Serialisierung verwenden, um lang laufende Agentenprozesse zu speichern und wieder aufzunehmen.
- **Dynamische Werkzeugauswahl**: RAG über Werkzeugbeschreibungen mit MAF-Werkzeugregistrierung kombinieren, um pro Abfrage nur relevante Werkzeuge anzuzeigen.
- **Multi-Agenten-Übergabe**: Workflow-Kanten und bedingtes Routing nutzen, um Übergaben zwischen spezialisierten Agenten zu orchestrieren.

## LangChain / LangGraph-Agenten auf Microsoft Foundry hosten

Microsoft Agent Framework ist **framework-übergreifend kompatibel** — Sie sind nicht auf mit MAF geschriebene Agenten beschränkt. Wenn Sie bereits einen Agenten mit **LangChain** oder **LangGraph** erstellt haben, können Sie ihn als **Microsoft Foundry gehosteten Agenten** ausführen, sodass Foundry Laufzeit, Sitzungen, Skalierung, Identität und Protokollendpunkte verwaltet, während Ihre Agentenlogik in LangGraph bleibt.

Dies erfolgt mit dem Paket `langchain_azure_ai.agents.hosting`, das einen kompilierten LangGraph-Graph über dieselben Protokolle bereitstellt, die von Foundry-gehosteten Agenten verwendet werden.

**1. Installieren Sie das Hosting-Extra:**

```bash
pip install -U "langchain-azure-ai[hosting]>=1.2.4" azure-identity
```

Das `hosting` Extra installiert die Foundry-Protokollbibliotheken: `azure-ai-agentserver-responses` (den OpenAI-kompatiblen `/responses`-Endpunkt) und `azure-ai-agentserver-invocations` (den generischen `/invocations`-Endpunkt).

**2. Wählen Sie ein Hosting-Protokoll:**

| Protokoll | Host-Klasse | Endpunkt | Verwendung wenn |
|----------|-------------|----------|---------------|
| **Responses** | `ResponsesHostServer` | `/responses` | Sie eine OpenAI-kompatible Chat-, Streaming-, Antwortverlauf- und Konversationsthread-Funktionalität möchten – der empfohlene Standard für konversationelle Agenten. |
| **Invocations** | `InvocationsHostServer` | `/invocations` | Sie ein benutzerdefiniertes JSON-Format, einen Webhook-artigen Endpunkt oder nicht-konversationelle Verarbeitung benötigen. |

Weil die **Responses-API die primäre API für agentenorientierte Entwicklung in Foundry ist**, beginnen Sie für die meisten Agenten mit `ResponsesHostServer`.

**3. Konfigurieren Sie Umgebungsvariablen** (`az login` zuerst, damit `DefaultAzureCredential` sich authentifizieren kann):

```bash
export FOUNDRY_PROJECT_ENDPOINT="https://<resource>.services.ai.azure.com/api/projects/<project>"
export FOUNDRY_MODEL_NAME="gpt-4.1"
```

Wenn der Agent später als gehosteter Agent in Foundry ausgeführt wird, injiziert die Plattform automatisch `FOUNDRY_PROJECT_ENDPOINT`.

**4. Stellen Sie einen LangGraph-Agenten über das Responses-Protokoll bereit:**

```python
import os

from azure.ai.projects import AIProjectClient
from azure.identity import DefaultAzureCredential, get_bearer_token_provider
from langchain.agents import create_agent
from langchain_openai import ChatOpenAI
from langchain_azure_ai.agents.hosting import ResponsesHostServer

_AZURE_AI_SCOPE = "https://ai.azure.com/.default"


def build_chat_model() -> ChatOpenAI:
    project_endpoint = os.environ["FOUNDRY_PROJECT_ENDPOINT"].rstrip("/")
    deployment = os.environ.get("FOUNDRY_MODEL_NAME", "gpt-4.1")
    credential = DefaultAzureCredential()
    project = AIProjectClient(endpoint=project_endpoint, credential=credential)
    openai_client = project.get_openai_client()
    token_provider = get_bearer_token_provider(credential, _AZURE_AI_SCOPE)

    # ChatOpenAI hier zielt auf den OpenAI-kompatiblen (Responses) Endpunkt des Foundry-Projekts ab.
    return ChatOpenAI(
        model=deployment,
        base_url=str(openai_client.base_url),
        api_key=token_provider,
    )


def main() -> None:
    graph = create_agent(build_chat_model(), tools=[])
    port = int(os.environ.get("PORT", "8088"))
    ResponsesHostServer(graph).run(port=port)


if __name__ == "__main__":
    main()
```

Führen Sie ihn lokal mit `python main.py` aus, und senden Sie dann eine Responses-Anfrage an `http://localhost:8088/responses`.

**Wichtige Verhaltensweisen:**

- **Konversationen**: Clients können eine Unterhaltung fortsetzen, indem sie `previous_response_id` oder eine `conversation` ID übergeben. Wenn Ihr Graph mit einem LangGraph-Checkpoint erstellt wurde, verwaltet Foundry den Konversationsstatus im Checkpoint (verwenden Sie für die Produktion einen dauerhaften Checkpoint; `MemorySaver` ist für lokale Tests ausreichend).
- **Mensch in der Schleife**: Wenn Ihr Graph LangGraph `interrupt()` verwendet, zeigt `ResponsesHostServer` die ausstehende Unterbrechung als Responses `function_call` / `mcp_approval_request` Element an, und Clients setzen mit einer passenden `function_call_output` / `mcp_approval_response` fort.
- **Deployment zu Foundry**: Verwenden Sie die Azure Developer CLI — `azd ext install azure.ai.agents`, `azd ai agent init -m <manifest>`, `azd ai agent run` (lokal, erfordert Docker), dann `azd provision` und `azd deploy`. Das Deployment gehosteter Agenten erfordert die Rolle **Foundry Project Manager**.

Eine lauffähige Version dieses Beispiels finden Sie in [code-samples/14-langchain-hosted-agent.py](../../../14-microsoft-agent-framework/code-samples/14-langchain-hosted-agent.py). Für die vollständige Anleitung (Invocations-Protokoll, benutzerdefinierte Anfrageschemata und Fehlerbehebung) siehe [Host LangGraph agents as Foundry hosted agents](https://learn.microsoft.com/azure/foundry/how-to/develop/langchain-hosted-agents).

## Code-Beispiele 

Code-Beispiele für Microsoft Agent Framework finden Sie in diesem Repository unter den Dateien `xx-python-agent-framework` und `xx-dotnet-agent-framework`.

## Haben Sie noch Fragen zum Microsoft Agent Framework?

Treten Sie dem [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D) bei, um andere Lernende zu treffen, an Office Hours teilzunehmen und Ihre Fragen zu KI-Agenten beantwortet zu bekommen.
## Vorherige Lektion

[Speicher für KI-Agenten](../13-agent-memory/README.md)

## Nächste Lektion

[Erstellung von Computerbenutzungsagenten (CUA)](../15-browser-use/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Haftungsausschluss**:
Dieses Dokument wurde mit dem KI-Übersetzungsdienst [Co-op Translator](https://github.com/Azure/co-op-translator) übersetzt. Obwohl wir uns um Genauigkeit bemühen, beachten Sie bitte, dass automatisierte Übersetzungen Fehler oder Ungenauigkeiten enthalten können. Das Originaldokument in seiner Ursprungssprache gilt als maßgebliche Quelle. Bei kritischen Informationen wird eine professionelle menschliche Übersetzung empfohlen. Wir übernehmen keine Haftung für Missverständnisse oder Fehlinterpretationen, die aus der Verwendung dieser Übersetzung entstehen.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->