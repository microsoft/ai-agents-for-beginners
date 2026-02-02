# Aufbau von Multi-Agenten-Anwendungen mit Microsoft Agent Framework Workflow

Dieses Tutorial führt Sie durch das Verständnis und die Entwicklung von Multi-Agenten-Anwendungen mit dem Microsoft Agent Framework. Wir werden die Kernkonzepte von Multi-Agenten-Systemen erkunden, die Architektur der Workflow-Komponente des Frameworks untersuchen und praktische Beispiele in Python und .NET für verschiedene Workflow-Muster durchgehen.

## 1\. Verständnis von Multi-Agenten-Systemen

Ein KI-Agent ist ein System, das über die Fähigkeiten eines standardmäßigen Large Language Models (LLM) hinausgeht. Es kann seine Umgebung wahrnehmen, Entscheidungen treffen und Maßnahmen ergreifen, um bestimmte Ziele zu erreichen. Ein Multi-Agenten-System umfasst mehrere dieser Agenten, die zusammenarbeiten, um ein Problem zu lösen, das für einen einzelnen Agenten schwierig oder unmöglich zu bewältigen wäre.

### Häufige Anwendungsszenarien

  * **Komplexe Problemlösung**: Aufteilung einer großen Aufgabe (z. B. Planung einer unternehmensweiten Veranstaltung) in kleinere Teilaufgaben, die von spezialisierten Agenten bearbeitet werden (z. B. ein Budget-Agent, ein Logistik-Agent, ein Marketing-Agent).
  * **Virtuelle Assistenten**: Ein Hauptassistent-Agent delegiert Aufgaben wie Terminplanung, Recherche und Buchungen an andere spezialisierte Agenten.
  * **Automatisierte Inhaltserstellung**: Ein Workflow, bei dem ein Agent Inhalte erstellt, ein anderer sie auf Genauigkeit und Ton überprüft und ein dritter sie veröffentlicht.

### Multi-Agenten-Muster

Multi-Agenten-Systeme können in verschiedenen Mustern organisiert werden, die bestimmen, wie sie interagieren:

  * **Sequenziell**: Agenten arbeiten in einer vordefinierten Reihenfolge, ähnlich einer Produktionslinie. Die Ausgabe eines Agenten wird zur Eingabe des nächsten.
  * **Parallel**: Agenten arbeiten gleichzeitig an verschiedenen Teilen einer Aufgabe, und ihre Ergebnisse werden am Ende zusammengeführt.
  * **Bedingt**: Der Workflow folgt unterschiedlichen Pfaden basierend auf der Ausgabe eines Agenten, ähnlich einer Wenn-Dann-Sonst-Anweisung.

## 2\. Die Workflow-Architektur des Microsoft Agent Frameworks

Das Workflow-System des Agent Frameworks ist eine fortschrittliche Orchestrierungs-Engine, die komplexe Interaktionen zwischen mehreren Agenten verwaltet. Es basiert auf einer graphbasierten Architektur, die ein [Pregel-ähnliches Ausführungsmodell](https://kowshik.github.io/JPregel/pregel_paper.pdf) verwendet, bei dem die Verarbeitung in synchronisierten Schritten, sogenannten "Supersteps", erfolgt.

### Kernkomponenten

Die Architektur besteht aus drei Hauptteilen:

1.  **Executors**: Dies sind die grundlegenden Verarbeitungseinheiten. In unseren Beispielen ist ein `Agent` eine Art Executor. Jeder Executor kann mehrere Nachrichtenhandler haben, die automatisch basierend auf der Art der empfangenen Nachricht aufgerufen werden.
2.  **Edges**: Diese definieren den Pfad, den Nachrichten zwischen den Executoren nehmen. Edges können Bedingungen haben, die eine dynamische Weiterleitung von Informationen durch den Workflow-Graphen ermöglichen.
3.  **Workflow**: Diese Komponente orchestriert den gesamten Prozess, verwaltet die Executors, Edges und den gesamten Ablauf der Ausführung. Sie stellt sicher, dass Nachrichten in der richtigen Reihenfolge verarbeitet werden und streamt Ereignisse für die Beobachtbarkeit.

*Eine Diagramm-Darstellung der Kernkomponenten des Workflow-Systems.*

Diese Struktur ermöglicht den Aufbau robuster und skalierbarer Anwendungen mit grundlegenden Mustern wie sequenziellen Ketten, Fan-Out/Fan-In für parallele Verarbeitung und Switch-Case-Logik für bedingte Abläufe.

## 3\. Praktische Beispiele und Code-Analyse

Nun schauen wir uns an, wie verschiedene Workflow-Muster mit dem Framework implementiert werden können. Wir betrachten sowohl Python- als auch .NET-Code für jedes Beispiel.

### Fall 1: Basis-Sequenzieller Workflow

Dies ist das einfachste Muster, bei dem die Ausgabe eines Agenten direkt an einen anderen weitergegeben wird. Unser Szenario umfasst einen Hotel-`FrontDesk`-Agenten, der eine Reiseempfehlung gibt, die anschließend von einem `Concierge`-Agenten überprüft wird.

*Diagramm des Basis-Workflows FrontDesk -\> Concierge.*

#### Szenario-Hintergrund

Ein Reisender fragt nach einer Empfehlung in Paris.

1.  Der `FrontDesk`-Agent, der auf Kürze ausgelegt ist, schlägt vor, das Louvre-Museum zu besuchen.
2.  Der `Concierge`-Agent, der authentische Erlebnisse priorisiert, erhält diesen Vorschlag. Er überprüft die Empfehlung und gibt Feedback, indem er eine lokalere, weniger touristische Alternative vorschlägt.

#### Python-Implementierungsanalyse

Im Python-Beispiel definieren und erstellen wir zunächst die beiden Agenten, jeweils mit spezifischen Anweisungen.

```python
# 01.python-agent-framework-workflow-ghmodel-basic.ipynb

# Define agent roles and instructions
REVIEWER_NAME = "Concierge"
REVIEWER_INSTRUCTIONS = """
    You are an are hotel concierge who has opinions about providing the most local and authentic experiences for travelers...
    """

FRONTDESK_NAME = "FrontDesk"
FRONTDESK_INSTRUCTIONS = """
    You are a Front Desk Travel Agent with ten years of experience and are known for brevity...
    """

# Create agent instances
reviewer_agent = chat_client.create_agent(
    instructions=(REVIEWER_INSTRUCTIONS),
    name=REVIEWER_NAME,
)

front_desk_agent = chat_client.create_agent(
    instructions=(FRONTDESK_INSTRUCTIONS),
    name=FRONTDESK_NAME,
)
```

Anschließend wird der `WorkflowBuilder` verwendet, um den Graphen zu erstellen. Der `front_desk_agent` wird als Ausgangspunkt festgelegt, und eine Edge wird erstellt, um dessen Ausgabe mit dem `reviewer_agent` zu verbinden.

```python
# 01.python-agent-framework-workflow-ghmodel-basic.ipynb

workflow = WorkflowBuilder().set_start_executor(front_desk_agent).add_edge(front_desk_agent, reviewer_agent).build()
```

Schließlich wird der Workflow mit der anfänglichen Benutzeraufforderung ausgeführt.

```python
# 01.python-agent-framework-workflow-ghmodel-basic.ipynb

result =''
# The run_stream method executes the workflow and streams events.
async for event in workflow.run_stream('I would like to go to Paris.'):
    if isinstance(event, WorkflowEvent):
        result += str(event.data)
```

#### .NET (C\#) Implementierungsanalyse

Die .NET-Implementierung folgt einer sehr ähnlichen Logik. Zunächst werden Konstanten für die Namen und Anweisungen der Agenten definiert.

```csharp
// 01.dotnet-agent-framework-workflow-ghmodel-basic.ipynb

const string ReviewerAgentName = "Concierge";
const string ReviewerAgentInstructions = @"
    You are an are hotel concierge who has opinions about providing the most local and authentic experiences for travelers...";

const string FrontDeskAgentName = "FrontDesk";
const string FrontDeskAgentInstructions = @"""
    You are a Front Desk Travel Agent with ten years of experience and are known for brevity...";
```

Die Agenten werden mit einem `OpenAIClient` erstellt, und dann definiert der `WorkflowBuilder` den sequenziellen Ablauf, indem eine Edge vom `frontDeskAgent` zum `reviewerAgent` hinzugefügt wird.

```csharp
// 01.dotnet-agent-framework-workflow-ghmodel-basic.ipynb

// Create AIAgent instances
AIAgent reviewerAgent = openAIClient.GetChatClient(github_model_id).CreateAIAgent(
    name:ReviewerAgentName,instructions:ReviewerAgentInstructions);
AIAgent frontDeskAgent  = openAIClient.GetChatClient(github_model_id).CreateAIAgent(
    name:FrontDeskAgentName,instructions:FrontDeskAgentInstructions);

// Build the workflow
var workflow = new WorkflowBuilder(frontDeskAgent)
            .AddEdge(frontDeskAgent, reviewerAgent)
            .Build();
```

Der Workflow wird dann mit der Nachricht des Benutzers ausgeführt, und die Ergebnisse werden zurückgestreamt.

### Fall 2: Mehrstufiger Sequenzieller Workflow

Dieses Muster erweitert die Basis-Sequenz, um mehr Agenten einzubeziehen. Es eignet sich ideal für Prozesse, die mehrere Stufen der Verfeinerung oder Transformation erfordern.

#### Szenario-Hintergrund

Ein Benutzer stellt ein Bild eines Wohnzimmers bereit und fragt nach einem Möbelangebot.

1.  **Sales-Agent**: Identifiziert die Möbelstücke im Bild und erstellt eine Liste.
2.  **Price-Agent**: Nimmt die Liste der Artikel und liefert eine detaillierte Preisübersicht, einschließlich Budget-, Mittelklasse- und Premium-Optionen.
3.  **Quote-Agent**: Erhält die preislich bewertete Liste und formatiert sie in ein formales Angebotsdokument in Markdown.

*Diagramm des Workflows Sales -\> Price -\> Quote.*

#### Python-Implementierungsanalyse

Drei Agenten werden definiert, jeder mit einer spezialisierten Rolle. Der Workflow wird mit `add_edge` erstellt, um eine Kette zu bilden: `sales_agent` -\> `price_agent` -\> `quote_agent`.

```python
# 02.python-agent-framework-workflow-ghmodel-sequential.ipynb

# Create three specialized agents
sales_agent = chat_client.create_agent(...)
price_agent = chat_client.create_agent(...)
quote_agent = chat_client.create_agent(...)

# Build the sequential workflow
workflow = WorkflowBuilder().set_start_executor(sales_agent).add_edge(sales_agent, price_agent).add_edge(price_agent, quote_agent).build()
```

Die Eingabe ist eine `ChatMessage`, die sowohl Text als auch die Bild-URI enthält. Das Framework übernimmt die Weitergabe der Ausgabe jedes Agenten an den nächsten in der Sequenz, bis das endgültige Angebot erstellt ist.

```python
# 02.python-agent-framework-workflow-ghmodel-sequential.ipynb

# The user message contains both text and an image
message = ChatMessage(
        role=Role.USER,
        contents=[
            TextContent(text="Please find the relevant furniture..."),
            DataContent(uri=image_uri, media_type="image/png")
        ]
)

# Run the workflow
async for event in workflow.run_stream(message):
    ...
```

#### .NET (C\#) Implementierungsanalyse

Das .NET-Beispiel spiegelt die Python-Version wider. Drei Agenten (`salesagent`, `priceagent`, `quoteagent`) werden erstellt. Der `WorkflowBuilder` verknüpft sie sequenziell.

```csharp
// 02.dotnet-agent-framework-workflow-ghmodel-sequential.ipynb

// Create agent instances
AIAgent salesagent = openAIClient.GetChatClient(github_model_id).CreateAIAgent(...);
AIAgent priceagent  = openAIClient.GetChatClient(github_model_id).CreateAIAgent(...);
AIAgent quoteagent = openAIClient.GetChatClient(github_model_id).CreateAIAgent(...);

// Build the workflow by adding edges sequentially
var workflow = new WorkflowBuilder(salesagent)
            .AddEdge(salesagent,priceagent)
            .AddEdge(priceagent, quoteagent)
            .Build();
```

Die Nachricht des Benutzers wird mit den Bilddaten (als Bytes) und der Textaufforderung erstellt. Die Methode `InProcessExecution.StreamAsync` startet den Workflow, und die endgültige Ausgabe wird aus dem Stream erfasst.

### Fall 3: Paralleler Workflow

Dieses Muster wird verwendet, wenn Aufgaben gleichzeitig ausgeführt werden können, um Zeit zu sparen. Es umfasst ein "Fan-Out" zu mehreren Agenten und ein "Fan-In", um die Ergebnisse zu aggregieren.

#### Szenario-Hintergrund

Ein Benutzer bittet um die Planung einer Reise nach Seattle.

1.  **Dispatcher (Fan-Out)**: Die Anfrage des Benutzers wird gleichzeitig an zwei Agenten gesendet.
2.  **Researcher-Agent**: Recherchiert Attraktionen, Wetter und wichtige Überlegungen für eine Reise nach Seattle im Dezember.
3.  **Plan-Agent**: Erstellt unabhängig einen detaillierten Tagesablauf für die Reise.
4.  **Aggregator (Fan-In)**: Die Ausgaben von sowohl dem Researcher als auch dem Planner werden gesammelt und zusammen als Endergebnis präsentiert.

*Diagramm des parallelen Workflows Researcher und Planner.*

#### Python-Implementierungsanalyse

Der `ConcurrentBuilder` vereinfacht die Erstellung dieses Musters. Sie listen einfach die teilnehmenden Agenten auf, und der Builder erstellt automatisch die notwendige Fan-Out- und Fan-In-Logik.

```python
# 03.python-agent-framework-workflow-ghmodel-concurrent.ipynb

research_agent = chat_client.create_agent(name="Researcher-Agent", ...)
plan_agent = chat_client.create_agent(name="Plan-Agent", ...)

# ConcurrentBuilder handles the fan-out/fan-in logic
workflow = ConcurrentBuilder().participants([research_agent, plan_agent]).build()

# Run the workflow
events = await workflow.run("Plan a trip to Seattle in December")
```

Das Framework stellt sicher, dass der `research_agent` und der `plan_agent` parallel ausgeführt werden, und ihre endgültigen Ausgaben werden in einer Liste gesammelt.

#### .NET (C\#) Implementierungsanalyse

In .NET erfordert dieses Muster eine explizitere Definition. Benutzerdefinierte Executors (`ConcurrentStartExecutor` und `ConcurrentAggregationExecutor`) werden erstellt, um die Fan-Out- und Fan-In-Logik zu handhaben.

```csharp
// 03.dotnet-agent-framework-workflow-ghmodel-concurrent.ipynb

// Custom executor to broadcast the message to all agents
public class ConcurrentStartExecutor() : ...
{
    public async ValueTask HandleAsync(string message, IWorkflowContext context)
    {
        // Send message to all connected agents
        await context.SendMessageAsync(new ChatMessage(ChatRole.User, message));
        // Send a token to start processing
        await context.SendMessageAsync(new TurnToken(emitEvents: true));
    }
}

// Custom executor to collect results
public class ConcurrentAggregationExecutor() : ...
{
    private readonly List<ChatMessage> _messages = [];
    public async ValueTask HandleAsync(ChatMessage message, IWorkflowContext context)
    {
        this._messages.Add(message);
        // Once both agents have responded, yield the final output
        if (this._messages.Count == 2)
        {
            ...
            await context.YieldOutputAsync(formattedMessages);
        }
    }
}
```

Der `WorkflowBuilder` verwendet dann `AddFanOutEdge` und `AddFanInEdge`, um den Graphen mit diesen benutzerdefinierten Executors und den Agenten zu erstellen.

```csharp
// 03.dotnet-agent-framework-workflow-ghmodel-concurrent.ipynb

var workflow = new WorkflowBuilder(startExecutor)
            .AddFanOutEdge(startExecutor, targets: [researcherAgent, plannerAgent])
            .AddFanInEdge(aggregationExecutor, sources: [researcherAgent, plannerAgent])
            .WithOutputFrom(aggregationExecutor)
            .Build();
```

### Fall 4: Bedingter Workflow

Bedingte Workflows führen Verzweigungslogik ein, die es dem System ermöglicht, basierend auf Zwischenergebnissen unterschiedliche Pfade einzuschlagen.

#### Szenario-Hintergrund

Dieser Workflow automatisiert die Erstellung und Veröffentlichung eines technischen Tutorials.

1.  **Evangelist-Agent**: Schreibt einen Entwurf des Tutorials basierend auf einer gegebenen Gliederung und URLs.
2.  **ContentReviewer-Agent**: Überprüft den Entwurf. Es wird geprüft, ob die Wortanzahl über 200 Wörter liegt.
3.  **Bedingte Verzweigung**:
      * **Wenn genehmigt (`Ja`)**: Der Workflow geht zum `Publisher-Agent` weiter.
      * **Wenn abgelehnt (`Nein`)**: Der Workflow stoppt und gibt den Grund für die Ablehnung aus.
4.  **Publisher-Agent**: Wenn der Entwurf genehmigt wird, speichert dieser Agent den Inhalt in einer Markdown-Datei.

#### Python-Implementierungsanalyse

Dieses Beispiel verwendet eine benutzerdefinierte Funktion, `select_targets`, um die bedingte Logik zu implementieren. Diese Funktion wird an `add_multi_selection_edge_group` übergeben und leitet den Workflow basierend auf dem Feld `review_result` aus der Ausgabe des Reviewers.

```python
# 04.python-agent-framework-workflow-aifoundry-condition.ipynb

# This function determines the next step based on the review result
def select_targets(review: ReviewResult, target_ids: list[str]) -> list[str]:
    handle_review_id, save_draft_id = target_ids
    if review.review_result == "Yes":
        # If approved, proceed to the 'save_draft' executor
        return [save_draft_id]
    else:
        # If rejected, proceed to the 'handle_review' executor to report failure
        return [handle_review_id]

# The workflow builder uses the selection function for routing
workflow = (
    WorkflowBuilder()
        .set_start_executor(evangelist_agent)
        .add_edge(evangelist_agent, reviewer_agent)
        .add_edge(reviewer_agent, to_reviewer_result)
        # The multi-selection edge implements the conditional logic
        .add_multi_selection_edge_group(
            to_reviewer_result,
            [handle_review, save_draft],
            selection_func=select_targets,
        )
        .add_edge(save_draft, publisher_agent)
        .build()
)
```

Benutzerdefinierte Executors wie `to_reviewer_result` werden verwendet, um die JSON-Ausgabe der Agenten zu analysieren und in stark typisierte Objekte umzuwandeln, die die Auswahlfunktion inspizieren kann.

#### .NET (C\#) Implementierungsanalyse

Die .NET-Version verwendet einen ähnlichen Ansatz mit einer Bedingungsfunktion. Eine `Func<object?, bool>` wird definiert, um die Eigenschaft `Result` des `ReviewResult`-Objekts zu überprüfen.

```csharp
// 04.dotnet-agent-framework-workflow-aifoundry-condition.ipynb

// This function creates a lambda for the condition check
public Func<object?, bool> GetCondition(string expectedResult) =>
        reviewResult => reviewResult is ReviewResult review && review.Result == expectedResult;

// The workflow is built with conditional edges
var workflow = new WorkflowBuilder(draftExecutor)
            .AddEdge(draftExecutor, contentReviewerExecutor)
            // Add an edge to the publisher only if the review result is "Yes"
            .AddEdge(contentReviewerExecutor, publishExecutor, condition: GetCondition(expectedResult: "Yes"))
            // Add an edge to the reviewer feedback executor if the result is "No"
            .AddEdge(contentReviewerExecutor, sendReviewerExecutor, condition: GetCondition(expectedResult: "No"))
            .Build();
```

Der Parameter `condition` der Methode `AddEdge` ermöglicht es dem `WorkflowBuilder`, einen Verzweigungspfad zu erstellen. Der Workflow folgt nur der Edge zu `publishExecutor`, wenn die Bedingung `GetCondition(expectedResult: "Yes")` wahr ist. Andernfalls folgt er dem Pfad zu `sendReviewerExecutor`.

## Fazit

Das Microsoft Agent Framework Workflow bietet eine robuste und flexible Grundlage für die Orchestrierung komplexer Multi-Agenten-Systeme. Durch die Nutzung seiner graphbasierten Architektur und Kernkomponenten können Entwickler anspruchsvolle Workflows in Python und .NET entwerfen und implementieren. Egal, ob Ihre Anwendung einfache sequenzielle Verarbeitung, parallele Ausführung oder dynamische bedingte Logik erfordert, das Framework bietet die Werkzeuge, um leistungsstarke, skalierbare und typensichere KI-gestützte Lösungen zu erstellen.

---

**Haftungsausschluss**:  
Dieses Dokument wurde mit dem KI-Übersetzungsdienst [Co-op Translator](https://github.com/Azure/co-op-translator) übersetzt. Obwohl wir uns um Genauigkeit bemühen, beachten Sie bitte, dass automatisierte Übersetzungen Fehler oder Ungenauigkeiten enthalten können. Das Originaldokument in seiner ursprünglichen Sprache sollte als maßgebliche Quelle betrachtet werden. Für kritische Informationen wird eine professionelle menschliche Übersetzung empfohlen. Wir übernehmen keine Haftung für Missverständnisse oder Fehlinterpretationen, die sich aus der Nutzung dieser Übersetzung ergeben.