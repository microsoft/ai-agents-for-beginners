# Erkundung des Microsoft Agent Frameworks

![Agent Framework](../../../translated_images/de/lesson-14-thumbnail.90df0065b9d234ee.webp)

### Einführung

Diese Lektion behandelt:

- Verständnis des Microsoft Agent Frameworks: Hauptmerkmale und Nutzen  
- Erkundung der Schlüsselkonzepte des Microsoft Agent Frameworks
- Fortgeschrittene MAF-Muster: Workflows, Middleware und Speicher

## Lernziele

Nach Abschluss dieser Lektion wissen Sie, wie man:

- Produktionsreife KI-Agenten mit dem Microsoft Agent Framework entwickelt
- Die Kernfunktionen des Microsoft Agent Frameworks auf Ihre agentischen Anwendungsfälle anwendet
- Fortgeschrittene Muster einschließlich Workflows, Middleware und Beobachtbarkeit einsetzt

## Codebeispiele 

Codebeispiele für [Microsoft Agent Framework (MAF)](https://aka.ms/ai-agents-beginners/agent-framework) finden Sie in diesem Repository unter den Dateien `xx-python-agent-framework` und `xx-dotnet-agent-framework`.

## Verständnis des Microsoft Agent Frameworks

![Framework Intro](../../../translated_images/de/framework-intro.077af16617cf130c.webp)

[Microsoft Agent Framework (MAF)](https://aka.ms/ai-agents-beginners/agent-framework) ist Microsofts einheitliches Framework zur Erstellung von KI-Agenten. Es bietet die Flexibilität, die vielfältigen agentischen Anwendungsfälle zu adressieren, die sowohl in Produktions- als auch in Forschungsumgebungen vorkommen, einschließlich:

- **Sequenzielle Agenten-Orchestrierung** in Szenarien, in denen Schritt-für-Schritt-Workflows erforderlich sind.
- **Parallele Orchestrierung** in Szenarien, in denen Agenten Aufgaben gleichzeitig erledigen müssen.
- **Gruppenchat-Orchestrierung** in Szenarien, in denen Agenten gemeinsam an einer Aufgabe zusammenarbeiten.
- **Übergabe-Orchestrierung** in Szenarien, in denen Agenten die Aufgabe aneinander übergeben, sobald Teilaufgaben abgeschlossen sind.
- **Magnetische Orchestrierung** in Szenarien, in denen ein leitender Agent eine Aufgabenliste erstellt und modifiziert und die Koordination der Unteragenten zur Erledigung der Aufgabe übernimmt.

Um KI-Agenten produktiv auszuliefern, bietet MAF außerdem Funktionen für:

- **Beobachtbarkeit** durch die Verwendung von OpenTelemetry, bei der jede Aktion des KI-Agenten einschließlich Tool-Aufruf, Orchestrierungsschritten, Denkprozessen und Leistungsüberwachung über Microsoft Foundry-Dashboards verfolgt wird.
- **Sicherheit** durch das native Hosting der Agenten auf Microsoft Foundry, welches Sicherheitskontrollen wie rollenbasierte Zugriffssteuerung, private Datenverwaltung und eingebaute Inhaltsicherheit umfasst.
- **Robustheit** da Agenten-Threads und Workflows pausieren, fortsetzen und sich von Fehlern erholen können, was längere Prozesse ermöglicht.
- **Steuerung** durch unterstützte Human-in-the-loop-Workflows, bei denen Aufgaben als menschliche Genehmigung erforderlich gekennzeichnet sind.

Microsoft Agent Framework ist außerdem auf Interoperabilität ausgerichtet durch:

- **Cloud-Unabhängigkeit** - Agenten können in Containern, lokal oder in mehreren verschiedenen Clouds ausgeführt werden.
- **Anbieter-Unabhängigkeit** - Agenten können mit Ihrem bevorzugten SDK erstellt werden, einschließlich Azure OpenAI und OpenAI.
- **Integration offener Standards** - Agenten können Protokolle wie Agent-to-Agent(A2A) und Model Context Protocol (MCP) nutzen, um andere Agenten und Werkzeuge zu entdecken und zu verwenden.
- **Plugins und Konnektoren** - Verbindungen können zu Daten- und Speicher-Diensten wie Microsoft Fabric, SharePoint, Pinecone und Qdrant hergestellt werden.

Sehen wir uns an, wie diese Funktionen auf einige der Kernkonzepte des Microsoft Agent Frameworks angewandt werden.

## Schlüsselkonzepte des Microsoft Agent Frameworks

### Agenten

![Agent Framework](../../../translated_images/de/agent-components.410a06daf87b4fef.webp)

**Erstellung von Agenten**

Die Erstellung eines Agenten erfolgt durch die Definition des Inferenzdienstes (LLM-Anbieter), einer
Reihe von Anweisungen für den KI-Agenten und der Zuweisung eines `Namens`:

```python
agent = AzureOpenAIChatClient(credential=AzureCliCredential()).create_agent( instructions="You are good at recommending trips to customers based on their preferences.", name="TripRecommender" )
```

Das obige Beispiel verwendet `Azure OpenAI`, aber Agenten können mit verschiedenen Diensten erstellt werden, einschließlich `Microsoft Foundry Agent Service`:

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

oder [MiniMax](https://platform.minimaxi.com/), das eine OpenAI-kompatible API mit großen Kontextfenstern (bis zu 204.000 Tokens) bereitstellt:

```python
agent = OpenAIChatClient(base_url="https://api.minimax.io/v1", api_key=os.environ["MINIMAX_API_KEY"], model_id="MiniMax-M3").create_agent( name="HelpfulAssistant", instructions="You are a helpful assistant.", )
```

oder entfernte Agenten unter Verwendung des A2A-Protokolls:

```python
agent = A2AAgent( name=agent_card.name, description=agent_card.description, agent_card=agent_card, url="https://your-a2a-agent-host" )
```

**Ausführung von Agenten**

Agenten werden über die Methoden `.run` oder `.run_stream` für nicht streamende bzw. streamende Antworten ausgeführt.

```python
result = await agent.run("What are good places to visit in Amsterdam?")
print(result.text)
```

```python
async for update in agent.run_stream("What are the good places to visit in Amsterdam?"):
    if update.text:
        print(update.text, end="", flush=True)

```

Für jeden Lauf kann der Agent mit Optionen angepasst werden, z. B. `max_tokens`, die vom Agenten genutzt werden, `tools` die der Agent aufrufen darf, und sogar das eingesetzte `Modell`.

Dies ist besonders nützlich, wenn bestimmte Modelle oder Tools für die Erfüllung einer Benutzeraufgabe benötigt werden.

**Werkzeuge**

Werkzeuge können sowohl bei der Definition des Agenten festgelegt werden:

```python
def get_attractions( location: Annotated[str, Field(description="The location to get the top tourist attractions for")], ) -> str: """Get the top tourist attractions for a given location.""" return f"The top attractions for {location} are." 


# Wenn ein ChatAgent direkt erstellt wird

agent = ChatAgent( chat_client=OpenAIChatClient(), instructions="You are a helpful assistant", tools=[get_attractions]

```

als auch bei der Ausführung des Agenten:

```python

result1 = await agent.run( "What's the best place to visit in Seattle?", tools=[get_attractions] # Werkzeug nur für diesen Durchlauf bereitgestellt )
```

**Agenten-Threads**

Agenten-Threads werden verwendet, um Mehr-Runden-Gespräche zu verwalten. Threads können entweder durch:

- Verwendung von `get_new_thread()`, wodurch der Thread über die Zeit gespeichert werden kann
- Automatische Erstellung eines Threads bei der Ausführung eines Agenten, der nur während der aktuellen Ausführung besteht

Die Thread-Erstellung sieht im Code so aus:

```python
# Erstelle einen neuen Thread.
thread = agent.get_new_thread() # Führe den Agenten mit dem Thread aus.
response = await agent.run("Hello, I am here to help you book travel. Where would you like to go?", thread=thread)

```

Anschließend kann der Thread serialisiert und für die spätere Verwendung gespeichert werden:

```python
# Erstelle einen neuen Thread.
thread = agent.get_new_thread() 

# Führe den Agenten mit dem Thread aus.

response = await agent.run("Hello, how are you?", thread=thread) 

# Serialisiere den Thread zur Speicherung.

serialized_thread = await thread.serialize() 

# Deserialisiere den Thread-Zustand nach dem Laden aus der Speicherung.

resumed_thread = await agent.deserialize_thread(serialized_thread)
```

**Agenten-Middleware**

Agenten interagieren mit Werkzeugen und LLMs, um Benutzeraufgaben zu erledigen. In bestimmten Szenarien wollen wir zwischen diesen Interaktionen Aktionen ausführen oder protokollieren. Agenten-Middleware ermöglicht dies durch:

*Funktions-Middleware*

Diese Middleware erlaubt es uns, eine Aktion zwischen Agent und einer Funktion oder einem Tool auszuführen, das aufgerufen wird. Ein Beispiel hierfür ist das Logging des Funktionsaufrufs.

Im nachfolgenden Code definiert `next`, ob die nächste Middleware oder die eigentliche Funktion aufgerufen wird.

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

    # Nachverarbeitung: Protokoll nach der Funktionsausführung
    print(f"[Function] {context.function.name} completed")
```

*Chat-Middleware*

Diese Middleware ermöglicht es, Aktionen zwischen Agent und den Anfragen an das LLM auszuführen oder zu protokollieren.

Dies enthält wichtige Informationen wie die `messages`, die an den KI-Dienst gesendet werden.

```python
async def logging_chat_middleware(
    context: ChatContext,
    next: Callable[[ChatContext], Awaitable[None]],
) -> None:
    """Chat middleware that logs AI interactions."""
    # Vorverarbeitung: Protokoll vor dem KI-Aufruf
    print(f"[Chat] Sending {len(context.messages)} messages to AI")

    # Weiter zum nächsten Middleware- oder KI-Dienst
    await next(context)

    # Nachverarbeitung: Protokoll nach KI-Antwort
    print("[Chat] AI response received")

```

**Agenten-Speicher**

Wie in der Lektion `Agentic Memory` behandelt, ist Speicher ein wichtiges Element, um den Agenten über verschiedene Kontexte hinweg zu betreiben. MAF bietet verschiedene Speicherarten:

*Speicher im Arbeitsspeicher*

Dies ist Speicher, der während der Laufzeit innerhalb von Threads gehalten wird.

```python
# Erstelle einen neuen Thread.
thread = agent.get_new_thread() # Führe den Agenten mit dem Thread aus.
response = await agent.run("Hello, I am here to help you book travel. Where would you like to go?", thread=thread)
```

*Persistente Nachrichten*

Dieser Speicher wird verwendet, um Konversationsverläufe über verschiedene Sitzungen hinweg zu speichern. Er wird mit `chat_message_store_factory` definiert:

```python
from agent_framework import ChatMessageStore

# Erstellen Sie einen benutzerdefinierten Nachrichtenspeicher
def create_message_store():
    return ChatMessageStore()

agent = ChatAgent(
    chat_client=OpenAIChatClient(),
    instructions="You are a Travel assistant.",
    chat_message_store_factory=create_message_store
)

```

*Dynamischer Speicher*

Dieser Speicher wird dem Kontext hinzugefügt, bevor Agenten ausgeführt werden. Diese Speicher können in externen Diensten wie mem0 gespeichert werden:

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

Beobachtbarkeit ist wichtig, um zuverlässige und wartbare agentische Systeme zu bauen. MAF integriert OpenTelemetry um Tracing und Metriken für bessere Beobachtbarkeit bereitzustellen.

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

MAF bietet Workflows, die vordefinierte Schritte zur Erledigung einer Aufgabe darstellen und KI-Agenten als Komponenten in diesen Schritten beinhalten.

Workflows bestehen aus verschiedenen Komponenten, die bessere Kontrollflüsse erlauben. Sie ermöglichen auch **Multi-Agent-Orchestrierung** und **Checkpointing**, um Workflow-Zustände zu speichern.

Die Kernkomponenten eines Workflows sind:

**Ausführende Einheiten**

Ausführende Einheiten erhalten Eingaben, führen ihre Aufgaben aus und erzeugen Ausgaben. So treibt dies den Workflow voran und führt zur Erledigung der Hauptaufgabe. Ausführende Einheiten können KI-Agenten oder benutzerdefinierte Logik sein.

**Kanten**

Kanten definieren den Nachrichtenfluss in einem Workflow. Diese können sein:

*Direkte Kanten* - Einfache Eins-zu-Eins-Verbindungen zwischen Ausführenden:

```python
from agent_framework import WorkflowBuilder

builder = WorkflowBuilder()
builder.add_edge(source_executor, target_executor)
builder.set_start_executor(source_executor)
workflow = builder.build()
```

*Bedingte Kanten* - Werden aktiviert, wenn bestimmte Bedingungen erfüllt sind. Beispielsweise kann ein Ausführender andere Optionen vorschlagen, wenn Hotelzimmer nicht verfügbar sind.

*Switch-Case-Kanten* - Leiten Nachrichten basierend auf definierten Bedingungen an verschiedene Ausführende weiter. Zum Beispiel, wenn Reisekunden Prioritätszugang haben und ihre Aufgaben durch einen anderen Workflow bearbeitet werden.

*Fan-out-Kanten* - Senden eine Nachricht an mehrere Ziele.

*Fan-in-Kanten* - Sammeln mehrere Nachrichten von verschiedenen Ausführenden und senden sie an ein Ziel.

**Ereignisse**

Für bessere Beobachtbarkeit bieten Workflows eingebaute Ereignisse an, darunter:

- `WorkflowStartedEvent`  - Workflow-Ausführung beginnt
- `WorkflowOutputEvent` - Workflow produziert eine Ausgabe
- `WorkflowErrorEvent` - Workflow stößt auf einen Fehler
- `ExecutorInvokeEvent`  - Ausführende Einheit beginnt mit der Verarbeitung
- `ExecutorCompleteEvent`  - Ausführende Einheit beendet die Verarbeitung
- `RequestInfoEvent` - Eine Anfrage wird gesendet

## Fortgeschrittene MAF-Muster

Die oberen Abschnitte behandeln die Schlüsselkonzepte des Microsoft Agent Frameworks. Beim Aufbau komplexerer Agenten sollten Sie folgende fortgeschrittene Muster berücksichtigen:

- **Middleware-Komposition**: Verketten Sie mehrere Middleware-Handler (Logging, Authentifizierung, Ratenbegrenzung) mit Funktions- und Chat-Middleware für eine feinkörnige Steuerung des Agentenverhaltens.
- **Workflow-Checkpointing**: Nutzen Sie Workflow-Ereignisse und Serialisierung, um langlaufende Agent-Prozesse zu speichern und fortzusetzen.
- **Dynamische Werkzeugauswahl**: Kombinieren Sie RAG über Werkzeugbeschreibungen mit MAFs Werkzeugregistrierung, um nur relevante Werkzeuge pro Anfrage anzuzeigen.
- **Multi-Agenten-Übergabe**: Verwenden Sie Workflow-Kanten und bedingtes Routing zur Orchestrierung von Übergaben zwischen spezialisierten Agenten.

## Hosting von LangChain / LangGraph-Agenten auf Microsoft Foundry

Microsoft Agent Framework ist **framework-interoperabel** — Sie sind nicht auf Agenten beschränkt, die mit MAF geschrieben wurden. Wenn Sie bereits einen Agenten mit **LangChain** oder **LangGraph** erstellt haben, können Sie ihn als **Microsoft Foundry gehosteten Agenten** ausführen, sodass Foundry die Laufzeit, Sitzungen, Skalierung, Identität und Protokollendpunkte verwaltet, während Ihre Agentenlogik in LangGraph bleibt.

Dies geschieht mit dem Paket `langchain_azure_ai.agents.hosting`, das ein kompiliertes LangGraph-Graph über dieselben Protokolle bereitstellt, die von Foundry-gehosteten Agenten verwendet werden.

**1. Installieren Sie das Hosting-Extra:**

```bash
pip install -U "langchain-azure-ai[hosting]>=1.2.4" azure-identity
```

Das `hosting`-Extra installiert die Foundry-Protokollbibliotheken: `azure-ai-agentserver-responses` (der OpenAI-kompatible `/responses` Endpunkt) und `azure-ai-agentserver-invocations` (der generische `/invocations` Endpunkt).

**2. Wählen Sie ein Hosting-Protokoll:**

| Protokoll | Host-Klasse | Endpunkt | Verwendung |
|----------|-------------|----------|------------|
| **Responses** | `ResponsesHostServer` | `/responses` | Sie möchten OpenAI-kompatiblen Chat, Streaming, Antwortverlauf und Konversations-Threading — die empfohlene Standardoption für konversationelle Agenten. |
| **Invocations** | `InvocationsHostServer` | `/invocations` | Sie benötigen eine kundenspezifische JSON-Struktur, einen Webhook-ähnlichen Endpunkt oder nicht-konversationelle Verarbeitung. |

Weil die **Responses-API die primäre API für agentenbasierte Entwicklung in Foundry ist**, starten Sie für die meisten Agenten mit `ResponsesHostServer`.

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

    # ChatOpenAI hier zielt auf den OpenAI-kompatiblen (Responses) Endpunkt des Foundry-Projekts.
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

- **Gespräche**: Clients setzen eine Konversation fort, indem sie `previous_response_id` oder eine `conversation`-ID übergeben. Wenn Ihr Graph mit einem LangGraph-Checkpoint kompiliert ist, verknüpft Foundry den Konversationszustand mit dem Checkpoint (verwenden Sie in der Produktion einen dauerhaften Checkpointer; `MemorySaver` eignet sich für lokale Tests).
- **Human-in-the-loop**: Wenn Ihr Graph LangGraph `interrupt()` verwendet, zeigt `ResponsesHostServer` die ausstehende Unterbrechung als Responses-`function_call` / `mcp_approval_request`-Element an, und Clients setzen mit einem passenden `function_call_output` / `mcp_approval_response` fort.
- **Deployment zu Foundry**: Nutzen Sie die Azure Developer CLI — `azd ext install azure.ai.agents`, `azd ai agent init -m <manifest>`, `azd ai agent run` (lokal, benötigt Docker), dann `azd provision` und `azd deploy`. Für das Deployment als gehosteter Agent ist die Rolle **Foundry Project Manager** erforderlich.

Eine ausführbare Version dieses Beispiels finden Sie in [code-samples/14-langchain-hosted-agent.py](../../../14-microsoft-agent-framework/code-samples/14-langchain-hosted-agent.py). Für die komplette Anleitung (Invocations-Protokoll, benutzerdefinierte Anfrageschemata und Fehlersuche) siehe [Host LangGraph agents as Foundry hosted agents](https://learn.microsoft.com/azure/foundry/how-to/develop/langchain-hosted-agents).

## Codebeispiele 

Codebeispiele für Microsoft Agent Framework finden Sie in diesem Repository unter den Dateien `xx-python-agent-framework` und `xx-dotnet-agent-framework`.

## Weitere Fragen zum Microsoft Agent Framework?

Treten Sie dem [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D) bei, um andere Lernende zu treffen, an Sprechstunden teilzunehmen und Ihre Fragen zu KI-Agenten zu klären.
## Vorherige Lektion

[Speicher für KI-Agenten](../13-agent-memory/README.md)

## Nächste Lektion

[Erstellung von Computer-Nutzungs-Agenten (CUA)](../15-browser-use/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Haftungsausschluss**:
Dieses Dokument wurde mit dem KI-Übersetzungsdienst [Co-op Translator](https://github.com/Azure/co-op-translator) übersetzt. Obwohl wir uns um Genauigkeit bemühen, beachten Sie bitte, dass automatisierte Übersetzungen Fehler oder Ungenauigkeiten enthalten können. Das Originaldokument in seiner Ursprungssprache gilt als maßgebliche Quelle. Bei kritischen Informationen wird eine professionelle menschliche Übersetzung empfohlen. Wir übernehmen keine Haftung für Missverständnisse oder Fehlinterpretationen, die aus der Verwendung dieser Übersetzung entstehen.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->