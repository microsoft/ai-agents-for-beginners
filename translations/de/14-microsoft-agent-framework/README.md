# Erkundung des Microsoft Agent Frameworks

![Agent Framework](../../../translated_images/de/lesson-14-thumbnail.90df0065b9d234ee.webp)

### Einführung

Diese Lektion behandelt:

- Verständnis des Microsoft Agent Frameworks: Hauptmerkmale und Mehrwert  
- Erkundung der Schlüsselkonzepte des Microsoft Agent Frameworks
- Fortgeschrittene MAF-Muster: Workflows, Middleware und Speicher

## Lernziele

Nach Abschluss dieser Lektion wissen Sie, wie Sie:

- Produktionsreife KI-Agenten mit Microsoft Agent Framework erstellen
- Die Kernfunktionen des Microsoft Agent Frameworks auf Ihre agentischen Anwendungsfälle anwenden
- Fortschrittliche Muster verwenden, einschließlich Workflows, Middleware und Beobachtbarkeit

## Codebeispiele 

Codebeispiele für das [Microsoft Agent Framework (MAF)](https://learn.microsoft.com/en-us/agent-framework/overview/?wt.mc_id=youtube_26688_organicsocial_reactor&pivots=programming-language-python) finden Sie in diesem Repository unter den Dateien `xx-python-agent-framework` und `xx-dotnet-agent-framework`.

## Verständnis des Microsoft Agent Frameworks

![Framework Intro](../../../translated_images/de/framework-intro.077af16617cf130c.webp)

[Microsoft Agent Framework (MAF)](https://learn.microsoft.com/en-us/agent-framework/overview/?wt.mc_id=youtube_26688_organicsocial_reactor&pivots=programming-language-python) ist Microsofts einheitliches Framework zum Erstellen von KI-Agenten. Es bietet die Flexibilität, die breite Vielfalt agentischer Anwendungsfälle zu adressieren, die sowohl in Produktions- als auch in Forschungsumgebungen vorkommen, darunter:

- **Sequenzielle Agent-Orchestrierung** in Szenarien, in denen schrittweise Workflows erforderlich sind.
- **Parallele Orchestrierung** in Szenarien, in denen Agenten Aufgaben gleichzeitig ausführen müssen.
- **Gruppenchat-Orchestrierung** in Szenarien, in denen Agenten gemeinsam an einer Aufgabe arbeiten können.
- **Übergabe-Orchestrierung** in Szenarien, in denen Agenten Aufgaben aneinander weiterreichen, sobald Teilaufgaben erledigt sind.
- **Magnetische Orchestrierung** in Szenarien, in denen ein Manager-Agent eine Aufgabenliste erstellt und ändert sowie die Koordination der Subagenten zur Aufgabenerfüllung übernimmt.

Um KI-Agenten in der Produktion bereitzustellen, verfügt MAF auch über Funktionen für:

- **Beobachtbarkeit** durch die Nutzung von OpenTelemetry, wobei jede Aktion des KI-Agenten inklusive Tool-Aufruf, Orchestrierungsschritten, Begründungsabläufen und Leistungsüberwachung über Microsoft Foundry-Dashboards verfolgt wird.
- **Sicherheit** durch das native Hosting der Agenten auf Microsoft Foundry, das Sicherheitskontrollen wie rollenbasierte Zugriffssteuerung, den Umgang mit privaten Daten und integrierte Inhalts-sicherheit umfasst.
- **Beständigkeit** da Agenten-Threads und Workflows pausieren, fortgesetzt und Fehler wiederhergestellt werden können, was längere Abläufe ermöglicht.
- **Steuerung** da menschliche Eingriffe unterstützt werden, wobei Aufgaben als genehmigungspflichtig markiert werden können.

Microsoft Agent Framework legt zudem Wert auf Interoperabilität durch:

- **Cloud-Unabhängigkeit** - Agenten können in Containern, lokal oder in verschiedenen Clouds ausgeführt werden.
- **Anbieter-Unabhängigkeit** - Agenten können mit dem bevorzugten SDK erstellt werden, einschließlich Azure OpenAI und OpenAI.
- **Integration offener Standards** - Agenten können Protokolle wie Agent-to-Agent(A2A) und Model Context Protocol (MCP) nutzen, um andere Agenten und Tools zu entdecken und zu verwenden.
- **Plugins und Konnektoren** - Verbindungen können zu Daten- und Speicherdiensten wie Microsoft Fabric, SharePoint, Pinecone und Qdrant hergestellt werden.

Sehen wir uns an, wie diese Funktionen auf einige der Kernkonzepte von Microsoft Agent Framework angewendet werden.

## Schlüsselkonzepte des Microsoft Agent Frameworks

### Agenten

![Agent Framework](../../../translated_images/de/agent-components.410a06daf87b4fef.webp)

**Agenten erstellen**

Agentenerstellung geschieht durch die Definition des Inferenzdienstes (LLM-Anbieter), einer
Menge von Anweisungen, denen der KI-Agent folgen soll, und einem zugewiesenen `name`:

```python
agent = AzureOpenAIChatClient(credential=AzureCliCredential()).create_agent( instructions="You are good at recommending trips to customers based on their preferences.", name="TripRecommender" )
```

Obiges verwendet `Azure OpenAI`, aber Agenten können mit einer Vielzahl von Diensten erstellt werden, einschließlich `Microsoft Foundry Agent Service`:

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

oder [MiniMax](https://platform.minimaxi.com/), das eine OpenAI-kompatible API mit großen Kontextfenstern (bis zu 204K Tokens) anbietet:

```python
agent = OpenAIChatClient(base_url="https://api.minimax.io/v1", api_key=os.environ["MINIMAX_API_KEY"], model_id="MiniMax-M3").create_agent( name="HelpfulAssistant", instructions="You are a helpful assistant.", )
```

oder entfernte Agenten, die das A2A-Protokoll verwenden:

```python
agent = A2AAgent( name=agent_card.name, description=agent_card.description, agent_card=agent_card, url="https://your-a2a-agent-host" )
```

**Agenten ausführen**

Agenten werden mit den Methoden `.run` oder `.run_stream` für nicht-streamende bzw. streamende Antworten ausgeführt.

```python
result = await agent.run("What are good places to visit in Amsterdam?")
print(result.text)
```

```python
async for update in agent.run_stream("What are the good places to visit in Amsterdam?"):
    if update.text:
        print(update.text, end="", flush=True)

```

Jeder Agentenlauf kann auch Optionen zur Anpassung von Parametern wie `max_tokens`, den vom Agenten aufrufbaren `tools` und sogar dem verwendeten `model` enthalten.

Dies ist nützlich in Fällen, in denen spezielle Modelle oder Tools für die Erfüllung einer Benutzeraufgabe erforderlich sind.

**Tools**

Tools können sowohl bei der Definition des Agenten definiert werden:

```python
def get_attractions( location: Annotated[str, Field(description="The location to get the top tourist attractions for")], ) -> str: """Get the top tourist attractions for a given location.""" return f"The top attractions for {location} are." 


# Beim direkten Erstellen eines ChatAgenten

agent = ChatAgent( chat_client=OpenAIChatClient(), instructions="You are a helpful assistant", tools=[get_attractions]

```

als auch beim Ausführen des Agenten:

```python

result1 = await agent.run( "What's the best place to visit in Seattle?", tools=[get_attractions] # Werkzeug nur für diesen Durchlauf bereitgestellt )
```

**Agenten-Threads**

Agenten-Threads werden verwendet, um mehrstufige Gespräche zu verwalten. Threads können entweder durch:

- Verwendung von `get_new_thread()` erstellt werden, was ermöglicht, den Thread über die Zeit zu speichern
- Automatische Thread-Erstellung beim Ausführen eines Agenten, wobei der Thread nur während des aktuellen Laufs existiert.

Zum Erstellen eines Threads sieht der Code so aus:

```python
# Einen neuen Thread erstellen.
thread = agent.get_new_thread() # Führen Sie den Agenten mit dem Thread aus.
response = await agent.run("Hello, I am here to help you book travel. Where would you like to go?", thread=thread)

```

Der Thread kann dann zur späteren Verwendung serialisiert werden:

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

Agenten interagieren mit Tools und LLMs, um Benutzeraufgaben zu erfüllen. In bestimmten Szenarien möchte man Aktionen direkt zwischen diesen Interaktionen ausführen oder verfolgen. Agenten-Middleware ermöglicht dies durch:

*Funktions-Middleware*

Diese Middleware erlaubt es, zwischen Agent und einer Funktion/einem Tool, das aufgerufen wird, eine Aktion auszuführen. Ein Beispiel wäre das Logging des Funktionsaufrufs.

Im Code unten definiert `next`, ob die nächste Middleware oder die tatsächliche Funktion aufgerufen werden soll.

```python
async def logging_function_middleware(
    context: FunctionInvocationContext,
    next: Callable[[FunctionInvocationContext], Awaitable[None]],
) -> None:
    """Function middleware that logs function execution."""
    # Vorverarbeitung: Protokoll vor der Funktionsausführung
    print(f"[Function] Calling {context.function.name}")

    # Weiter zum nächsten Middleware oder zur Funktionsausführung
    await next(context)

    # Nachbearbeitung: Protokoll nach der Funktionsausführung
    print(f"[Function] {context.function.name} completed")
```

*Chat-Middleware*

Diese Middleware ermöglicht das Ausführen oder Protokollieren einer Aktion zwischen Agent und den Anfragen an das LLM.

Diese enthält wichtige Informationen wie die `messages`, die an den KI-Dienst gesendet werden.

```python
async def logging_chat_middleware(
    context: ChatContext,
    next: Callable[[ChatContext], Awaitable[None]],
) -> None:
    """Chat middleware that logs AI interactions."""
    # Vorverarbeitung: Protokoll vor dem KI-Aufruf
    print(f"[Chat] Sending {len(context.messages)} messages to AI")

    # Fortfahren zum nächsten Middleware- oder KI-Dienst
    await next(context)

    # Nachverarbeitung: Protokoll nach der KI-Antwort
    print("[Chat] AI response received")

```

**Agenten-Speicher**

Wie in der Lektion `Agentic Memory` behandelt, ist Speicher ein wichtiges Element, damit der Agent über verschiedene Kontexte hinweg arbeitet. MAF bietet verschiedene Speicherarten:

*In-Memory Speicher*

Dies ist der Speicher, der in Threads während der Laufzeit der Anwendung gehalten wird.

```python
# Erstelle einen neuen Thread.
thread = agent.get_new_thread() # Führe den Agenten mit dem Thread aus.
response = await agent.run("Hello, I am here to help you book travel. Where would you like to go?", thread=thread)
```

*Persistente Nachrichten*

Dieser Speicher wird verwendet, um Gesprächsverläufe über verschiedene Sitzungen hinweg zu speichern. Er wird mit dem `chat_message_store_factory` definiert:

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

Dieser Speicher wird vor dem Ausführen der Agenten zum Kontext hinzugefügt. Diese Speicher können in externen Diensten wie mem0 gespeichert werden:

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

Beobachtbarkeit ist wichtig für den Aufbau zuverlässiger und wartbarer agentischer Systeme. MAF integriert OpenTelemetry zur Bereitstellung von Tracing und Messungen für bessere Beobachtbarkeit.

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

MAF bietet Workflows, die vordefinierte Schritte zur Erfüllung einer Aufgabe sind und KI-Agenten als Komponenten in diesen Schritten enthalten.

Workflows bestehen aus verschiedenen Komponenten, die eine bessere Steuerung des Ablaufs ermöglichen. Workflows unterstützen auch **Multi-Agent Orchestrierung** und **Checkpointing**, um Workflow-Zustände zu speichern.

Die Kernkomponenten eines Workflows sind:

**Ausführende (Executors)**

Executors empfangen Eingabenachrichten, führen ihre zugewiesenen Aufgaben aus und erzeugen dann eine Ausgabenachricht. Dadurch wird der Workflow weiter vorangetrieben, um die größere Aufgabe abzuschließen. Executors können entweder KI-Agenten oder benutzerdefinierte Logik sein.

**Kanten (Edges)**

Kanten definieren den Nachrichtenfluss in einem Workflow. Diese können sein:

*Direkte Kanten* - Einfache eins-zu-eins-Verbindungen zwischen Executoren:

```python
from agent_framework import WorkflowBuilder

builder = WorkflowBuilder()
builder.add_edge(source_executor, target_executor)
builder.set_start_executor(source_executor)
workflow = builder.build()
```

*Bedingte Kanten* - Werden nach Erfüllung bestimmter Bedingungen aktiviert. Zum Beispiel, wenn Hotelzimmer nicht verfügbar sind, kann ein Executor andere Optionen vorschlagen.

*Switch-Case-Kanten* - Leiten Nachrichten basierend auf definierten Bedingungen an unterschiedliche Executor weiter. Zum Beispiel, wenn ein Reisekunde bevorzugten Zugang hat, werden seine Aufgaben über einen anderen Workflow bearbeitet.

*Fan-out-Kanten* - Senden eine Nachricht an mehrere Ziele.

*Fan-in-Kanten* - Sammeln mehrere Nachrichten von verschiedenen Executoren und senden diese an ein Ziel.

**Ereignisse**

Zur besseren Beobachtbarkeit von Workflows bietet MAF integrierte Ereignisse für die Ausführung, darunter:

- `WorkflowStartedEvent`  - Workflow-Ausführung beginnt
- `WorkflowOutputEvent` - Workflow erzeugt eine Ausgabe
- `WorkflowErrorEvent` - Workflow erleidet einen Fehler
- `ExecutorInvokeEvent`  - Executor startet Verarbeitung
- `ExecutorCompleteEvent`  -  Executor beendet Verarbeitung
- `RequestInfoEvent` - Eine Anfrage wird gestellt

## Fortgeschrittene MAF-Muster

Die obigen Abschnitte behandeln die Schlüsselkonzepte des Microsoft Agent Frameworks. Wenn Sie komplexere Agenten bauen, sind hier einige fortgeschrittene Muster zu berücksichtigen:

- **Middleware-Komposition**: Verketten Sie mehrere Middleware-Handler (Logging, Authentifizierung, Rate-Limiting) mit Funktions- und Chat-Middleware für feinkörnige Kontrolle über das Verhalten des Agenten.
- **Workflow-Checkpointing**: Nutzen Sie Workflow-Ereignisse und Serialisierung, um langlaufende Agentenprozesse zu speichern und fortzusetzen.
- **Dynamische Tool-Auswahl**: Kombinieren Sie RAG über Tool-Beschreibungen mit der Tool-Registrierung von MAF, um für jede Anfrage nur relevante Tools anzubieten.
- **Multi-Agent-Übergabe**: Verwenden Sie Workflow-Kanten und bedingte Weiterleitung, um Übergaben zwischen spezialisierten Agenten zu orchestrieren.

## Hosting von LangChain / LangGraph Agenten auf Microsoft Foundry

Microsoft Agent Framework ist **framework-interoperabel** – Sie sind nicht auf mit MAF geschriebene Agenten beschränkt. Wenn Sie bereits einen Agenten mit **LangChain** oder **LangGraph** gebaut haben, können Sie diesen als **Microsoft Foundry gehosteten Agenten** ausführen, sodass Foundry Laufzeit, Sitzungen, Skalierung, Identität und Protokollendpunkte für Sie verwaltet, während Ihre Agentenlogik in LangGraph bleibt.

Dies wird mit dem Paket `langchain_azure_ai.agents.hosting` realisiert, das einen kompilierten LangGraph-Graphen über dieselben Protokolle bereitstellt, die auch von Foundry-gehosteten Agenten verwendet werden.

**1. Installieren Sie das Hosting-Extra:**

```bash
pip install -U "langchain-azure-ai[hosting]>=1.2.4" azure-identity
```

Das `hosting`-Extra installiert die Foundry-Protokollbibliotheken: `azure-ai-agentserver-responses` (der OpenAI-kompatible `/responses` Endpunkt) und `azure-ai-agentserver-invocations` (der generische `/invocations` Endpunkt).

**2. Wählen Sie ein Hosting-Protokoll:**

| Protokoll | Host-Klasse | Endpunkt | Verwendung |
|----------|-----------|----------|----------|
| **Responses** | `ResponsesHostServer` | `/responses` | Sie möchten OpenAI-kompatiblen Chat, Streaming, Antwortverlauf und Gesprächsthreads — die empfohlene Standardoption für konversationelle Agenten. |
| **Invocations** | `InvocationsHostServer` | `/invocations` | Sie benötigen eine benutzerdefinierte JSON-Struktur, einen Webhook-ähnlichen Endpunkt oder nicht-konversationelle Verarbeitung. |

Da die **Responses API die primäre API für agenten-basierte Entwicklung in Foundry ist**, starten Sie für die meisten Agenten mit `ResponsesHostServer`.

**3. Konfigurieren Sie Umgebungsvariablen** (`az login` zuerst, damit `DefaultAzureCredential` authentifizieren kann):

```bash
export FOUNDRY_PROJECT_ENDPOINT="https://<resource>.services.ai.azure.com/api/projects/<project>"
export FOUNDRY_MODEL_NAME="gpt-5-mini"
```

Wenn der Agent später als gehosteter Agent in Foundry läuft, injiziert die Plattform automatisch `FOUNDRY_PROJECT_ENDPOINT`.

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
    deployment = os.environ.get("FOUNDRY_MODEL_NAME", "gpt-5-mini")
    credential = DefaultAzureCredential()
    project = AIProjectClient(endpoint=project_endpoint, credential=credential)
    openai_client = project.get_openai_client()
    token_provider = get_bearer_token_provider(credential, _AZURE_AI_SCOPE)

    # ChatOpenAI zielt hier auf den OpenAI-kompatiblen (Responses) Endpunkt des Foundry-Projekts ab.
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

Führen Sie ihn lokal mit `python main.py` aus und senden Sie dann eine Responses-Anfrage an `http://localhost:8088/responses`.

**Wichtiges Verhalten:**

- **Gespräche**: Clients setzen ein Gespräch fort, indem sie `previous_response_id` oder eine `conversation`-ID übergeben. Wenn Ihr Graph mit einem LangGraph-Checkpointing kompiliert ist, speichert Foundry den Gesprächszustand zum Checkpoint (verwenden Sie in der Produktion einen dauerhaften Checkpointer; `MemorySaver` ist für lokale Tests ausreichend).
- **Mensch-in-der-Schleife**: Wenn Ihr Graph LangGraph `interrupt()` verwendet, zeigt `ResponsesHostServer` die ausstehende Unterbrechung als Responses `function_call` / `mcp_approval_request` Element an, und Clients setzen mit einem passenden `function_call_output` / `mcp_approval_response` fort.
- **Bereitstellung zu Foundry**: Verwenden Sie die Azure Developer CLI — `azd ext install azure.ai.agents`, `azd ai agent init -m <manifest>`, `azd ai agent run` (lokal, benötigt Docker), dann `azd provision` und `azd deploy`. Die Bereitstellung gehosteter Agenten erfordert die Rolle **Foundry Project Manager**.

Eine ausführbare Version dieses Beispiels befindet sich in [code-samples/14-langchain-hosted-agent.py](../../../14-microsoft-agent-framework/code-samples/14-langchain-hosted-agent.py). Für die vollständige Schritt-für-Schritt-Anleitung (Invocations-Protokoll, benutzerdefinierte Anfrageschemata und Fehlerbehebung) siehe [Host LangGraph agents as Foundry hosted agents](https://learn.microsoft.com/azure/foundry/how-to/develop/langchain-hosted-agents).

## Codebeispiele 

Codebeispiele für Microsoft Agent Framework finden Sie in diesem Repository unter den Dateien `xx-python-agent-framework` und `xx-dotnet-agent-framework`.

## Haben Sie weitere Fragen zum Microsoft Agent Framework?

Treten Sie dem [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D) bei, um andere Lernende zu treffen, an Sprechstunden teilzunehmen und Ihre Fragen zu KI-Agenten beantwortet zu bekommen.
## Vorherige Lektion

[Speicher für KI-Agenten](../13-agent-memory/README.md)

## Nächste Lektion

[Computer Use Agents (CUA) erstellen](../15-browser-use/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Haftungsausschluss**:
Dieses Dokument wurde mit dem KI-Übersetzungsdienst [Co-op Translator](https://github.com/Azure/co-op-translator) übersetzt. Obwohl wir uns um Genauigkeit bemühen, beachten Sie bitte, dass automatisierte Übersetzungen Fehler oder Ungenauigkeiten enthalten können. Das Originaldokument in seiner Ursprungssprache gilt als maßgebliche Quelle. Bei kritischen Informationen wird eine professionelle menschliche Übersetzung empfohlen. Wir übernehmen keine Haftung für Missverständnisse oder Fehlinterpretationen, die aus der Verwendung dieser Übersetzung entstehen.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->