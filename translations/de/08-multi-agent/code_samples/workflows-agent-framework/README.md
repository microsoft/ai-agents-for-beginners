# Multi-Agent-Anwendungen mit Microsoft Agent Framework Workflow entwickeln

Dieses Tutorial führt Sie durch das Verständnis und den Aufbau von Multi-Agent-Anwendungen mit dem Microsoft Agent Framework. Wir werden die Kernkonzepte von Multi-Agent-Systemen erkunden, uns die Architektur der Workflow-Komponente des Frameworks ansehen und praktische Beispiele sowohl in Python als auch in .NET für verschiedene Workflow-Muster durchgehen.

## 1\. Verständnis von Multi-Agent-Systemen

Ein KI-Agent ist ein System, das über die Fähigkeiten eines Standard-Large-Language-Models (LLM) hinausgeht. Es kann seine Umgebung wahrnehmen, Entscheidungen treffen und Aktionen ausführen, um bestimmte Ziele zu erreichen. Ein Multi-Agent-System umfasst mehrere dieser Agenten, die zusammenarbeiten, um ein Problem zu lösen, das für einen einzelnen Agenten allein schwer oder unmöglich zu bewältigen wäre.

### Häufige Anwendungsszenarien

  * **Komplexe Problemlösung**: Eine große Aufgabe (z. B. Planung einer firmenweiten Veranstaltung) wird in kleinere Teilaufgaben aufgeteilt, die von spezialisierten Agenten bearbeitet werden (z. B. ein Budget-Agent, ein Logistik-Agent, ein Marketing-Agent).
  * **Virtuelle Assistenten**: Ein Hauptassistent- Agent delegiert Aufgaben wie Terminplanung, Recherche und Buchungen an andere spezialisierte Agenten.
  * **Automatisierte Inhaltserstellung**: Ein Workflow, bei dem ein Agent Inhalte entwirft, ein anderer sie auf Genauigkeit und Ton überprüft und ein dritter sie veröffentlicht.

### Multi-Agent-Muster

Multi-Agent-Systeme können in verschiedenen Mustern organisiert sein, die bestimmen, wie sie interagieren:

  * **Sequenziell**: Agenten arbeiten in einer vordefinierten Reihenfolge, wie eine Fließbandarbeit. Die Ausgabe eines Agenten wird zur Eingabe für den nächsten.
  * **Parallel**: Agenten arbeiten gleichzeitig an verschiedenen Teilen einer Aufgabe, und deren Ergebnisse werden am Ende zusammengeführt.
  * **Bedingt**: Der Workflow folgt unterschiedlichen Pfaden basierend auf der Ausgabe eines Agenten, ähnlich einer if-dann-sonst-Anweisung.

## 2\. Die Microsoft Agent Framework Workflow-Architektur

Das Workflow-System des Agent Frameworks ist eine fortschrittliche Orchestrierungs-Engine, die entwickelt wurde, um komplexe Interaktionen zwischen mehreren Agenten zu steuern. Es basiert auf einer graphbasierten Architektur, die ein [Pregel-ähnliches Ausführungsmodell](https://kowshik.github.io/JPregel/pregel_paper.pdf) verwendet, bei dem die Verarbeitung in synchronisierten Schritten, sogenannten „Supersteps“, erfolgt.

### Kernkomponenten

Die Architektur besteht aus drei Hauptteilen:

1.  **Executor**: Dies sind die grundlegenden Verarbeitungseinheiten. In unseren Beispielen ist ein `Agent` eine Art Executor. Jeder Executor kann mehrere Nachrichten-Handler haben, die automatisch je nach empfangenem Nachrichtentyp aufgerufen werden.
2.  **Kanten**: Diese definieren den Pfad, den Nachrichten zwischen Executoren nehmen. Kanten können Bedingungen haben, die eine dynamische Weiterleitung von Informationen durch den Workflow-Graphen ermöglichen.
3.  **Workflow**: Diese Komponente orchestriert den gesamten Prozess, verwaltet die Executor, Kanten und den Gesamtfluss der Ausführung. Sie stellt sicher, dass Nachrichten in der richtigen Reihenfolge verarbeitet werden und streamt Events für die Beobachtbarkeit.

*Eine Abbildung, die die Kernkomponenten des Workflow-Systems veranschaulicht.*

Diese Struktur ermöglicht den Aufbau robuster und skalierbarer Anwendungen mithilfe grundlegender Muster wie sequenziellen Ketten, Fan-Out/Fan-In für parallele Verarbeitung und Switch-Case-Logik für bedingte Abläufe.

## 3\. Praktische Beispiele und Code-Analyse

Nun sehen wir uns an, wie verschiedene Workflow-Muster mit dem Framework implementiert werden können. Wir betrachten jeweils Python- und .NET-Code für jedes Beispiel.

### Fall 1: Einfacher sequenzieller Workflow

Dies ist das einfachste Muster, bei dem die Ausgabe eines Agenten direkt an einen anderen weitergegeben wird. Unser Szenario beinhaltet einen Hotel-`FrontDesk`-Agenten, der eine Reiseempfehlung ausspricht, die anschließend von einem `Concierge`-Agenten geprüft wird.

*Diagramm des einfachen FrontDesk -> Concierge-Workflows.*

#### Szenario-Hintergrund

Ein Reisender fragt nach einer Empfehlung in Paris.

1.  Der `FrontDesk`-Agent, der für kurze Antworten ausgelegt ist, empfiehlt einen Besuch im Louvre.
2.  Der `Concierge`-Agent, der authentische Erlebnisse priorisiert, erhält diesen Vorschlag, prüft ihn und gibt Feedback, wobei er eine lokalere, weniger touristische Alternative vorschlägt.

#### Analyse der Python-Implementierung

Im Python-Beispiel definieren und erstellen wir zunächst die beiden Agenten, jeweils mit spezifischen Anweisungen.

```python
# 01.python-agent-framework-workflow-ghmodel-basic.ipynb

# Agentenrollen und Anweisungen definieren
REVIEWER_NAME = "Concierge"
REVIEWER_INSTRUCTIONS = """
    You are a hotel concierge who has opinions about providing the most local and authentic experiences for travelers...
    """

FRONTDESK_NAME = "FrontDesk"
FRONTDESK_INSTRUCTIONS = """
    You are a Front Desk Travel Agent with ten years of experience and are known for brevity...
    """

# Agenteninstanzen erstellen
reviewer_agent = chat_client.as_agent(
    instructions=(REVIEWER_INSTRUCTIONS),
    name=REVIEWER_NAME,
)

front_desk_agent = chat_client.as_agent(
    instructions=(FRONTDESK_INSTRUCTIONS),
    name=FRONTDESK_NAME,
)
```

Danach wird der `WorkflowBuilder` verwendet, um den Graphen zu konstruieren. Der `front_desk_agent` wird als Startpunkt festgelegt, und es wird eine Kante erstellt, die seine Ausgabe mit dem `reviewer_agent` verbindet.

```python
# 01.python-agent-framework-workflow-ghmodel-basic.ipynb

workflow = WorkflowBuilder(start_executor=front_desk_agent).add_edge(front_desk_agent, reviewer_agent).build()
```

Abschließend wird der Workflow mit der ursprünglichen Benutzeranfrage ausgeführt.

```python
# 01.python-agent-framework-workflow-ghmodel-basic.ipynb

result =''
# run führt den Arbeitsablauf aus; get_outputs() gibt das Ergebnis des Ausführenden zurück.
events = await workflow.run('I would like to go to Paris.')
outputs = events.get_outputs()
result = outputs[0].text if outputs else ''
```

#### Analyse der .NET (C#) Implementierung

Die .NET-Implementierung folgt einer sehr ähnlichen Logik. Zunächst werden Konstanten für die Namen und Anweisungen der Agenten definiert.

```csharp
// 01.dotnet-agent-framework-workflow-ghmodel-basic.ipynb

const string ReviewerAgentName = "Concierge";
const string ReviewerAgentInstructions = @"
    You are a hotel concierge who has opinions about providing the most local and authentic experiences for travelers...";

const string FrontDeskAgentName = "FrontDesk";
const string FrontDeskAgentInstructions = @"""
    You are a Front Desk Travel Agent with ten years of experience and are known for brevity...";
```

Die Agenten werden mit einem `AzureOpenAIClient` (Responses API) erstellt, und dann definiert der `WorkflowBuilder` den sequenziellen Fluss, indem er eine Kante vom `frontDeskAgent` zum `reviewerAgent` hinzufügt.

```csharp
// 01.dotnet-agent-framework-workflow-ghmodel-basic.ipynb

// Create AIAgent instances
AIAgent reviewerAgent = azureClient.GetChatClient(deployment).AsAIAgent(
    name:ReviewerAgentName,instructions:ReviewerAgentInstructions);
AIAgent frontDeskAgent  = azureClient.GetChatClient(deployment).AsAIAgent(
    name:FrontDeskAgentName,instructions:FrontDeskAgentInstructions);

// Build the workflow
var workflow = new WorkflowBuilder(frontDeskAgent)
            .AddEdge(frontDeskAgent, reviewerAgent)
            .Build();
```

Der Workflow wird danach mit der Nachricht des Benutzers ausgeführt, und die Ergebnisse werden zurückgestreamt.

### Fall 2: Mehrstufiger sequenzieller Workflow

Dieses Muster erweitert die einfache Reihenfolge um weitere Agenten. Es eignet sich ideal für Prozesse, die mehrere Verfeinerungs- oder Transformationsschritte erfordern.

#### Szenario-Hintergrund

Ein Benutzer liefert ein Bild eines Wohnzimmers und bittet um ein Möbelangebot.

1.  **Sales-Agent**: Identifiziert die Möbelstücke im Bild und erstellt eine Liste.
2.  **Price-Agent**: Nimmt die Liste der Artikel und erstellt eine detaillierte Preisaufstellung mit Budget-, Mittelklasse- und Premiumoptionen.
3.  **Quote-Agent**: Erhält die Preise und formatiert sie in ein formales Angebotsdokument im Markdown-Format.

*Diagramm des Sales -> Price -> Quote-Workflows.*

#### Analyse der Python-Implementierung

Drei Agenten werden definiert, jeder mit einer spezialisierten Rolle. Der Workflow wird mit `add_edge` erstellt, um eine Kette zu bilden: `sales_agent` -> `price_agent` -> `quote_agent`.

```python
# 02.python-agent-framework-workflow-ghmodel-sequential.ipynb

# Erstellen Sie drei spezialisierte Agenten
sales_agent = chat_client.as_agent(...)
price_agent = chat_client.as_agent(...)
quote_agent = chat_client.as_agent(...)

# Erstellen Sie den sequentiellen Arbeitsablauf
workflow = WorkflowBuilder(start_executor=sales_agent).add_edge(sales_agent, price_agent).add_edge(price_agent, quote_agent).build()
```

Die Eingabe ist eine `ChatMessage`, die sowohl Text als auch die Bild-URI enthält. Das Framework sorgt dafür, dass die Ausgabe jedes Agenten an den nächsten in der Sequenz weitergegeben wird, bis das finale Angebot erstellt ist.

```python
# 02.python-agent-framework-workflow-ghmodel-sequential.ipynb

# Die Benutzernachricht enthält sowohl Text als auch ein Bild
message = ChatMessage(
        role=Role.USER,
        contents=[
            TextContent(text="Please find the relevant furniture..."),
            DataContent(uri=image_uri, media_type="image/png")
        ]
)

# Führen Sie den Workflow aus
events = await workflow.run(message)
```

#### Analyse der .NET (C#) Implementierung

Das .NET-Beispiel spiegelt die Python-Version wider. Drei Agenten (`salesagent`, `priceagent`, `quoteagent`) werden erstellt. Der `WorkflowBuilder` verknüpft sie sequenziell.

```csharp
// 02.dotnet-agent-framework-workflow-ghmodel-sequential.ipynb

// Create agent instances
AIAgent salesagent = azureClient.GetChatClient(deployment).AsAIAgent(...);
AIAgent priceagent  = azureClient.GetChatClient(deployment).AsAIAgent(...);
AIAgent quoteagent = azureClient.GetChatClient(deployment).AsAIAgent(...);

// Build the workflow by adding edges sequentially
var workflow = new WorkflowBuilder(salesagent)
            .AddEdge(salesagent,priceagent)
            .AddEdge(priceagent, quoteagent)
            .Build();
```

Die Nachricht des Benutzers wird mit den Bilddaten (als Bytes) und dem Textprompt erstellt. Die Methode `InProcessExecution.RunStreamingAsync` startet den Workflow, und die finale Ausgabe wird aus dem Stream erfasst.

### Fall 3: Parallel-Workflow

Dieses Muster wird verwendet, wenn Aufgaben gleichzeitig ausgeführt werden können, um Zeit zu sparen. Es beinhaltet einen „Fan-Out“ zu mehreren Agenten und einen „Fan-In“ zur Zusammenführung der Ergebnisse.

#### Szenario-Hintergrund

Ein Benutzer bittet um die Planung einer Reise nach Seattle.

1.  **Dispatcher (Fan-Out)**: Die Anfrage des Benutzers wird gleichzeitig an zwei Agenten gesendet.
2.  **Researcher-Agent**: Recherchiert Sehenswürdigkeiten, Wetter und wichtige Überlegungen für eine Reise nach Seattle im Dezember.
3.  **Plan-Agent**: Erstellt unabhängig eine detaillierte Tagesplanung der Reise.
4.  **Aggregator (Fan-In)**: Die Ausgaben von Researcher und Planer werden gesammelt und zusammen als Endergebnis präsentiert.

*Diagramm des parallelen Researcher- und Planer-Workflows.*

#### Analyse der Python-Implementierung

Der `ConcurrentBuilder` erleichtert die Erstellung dieses Musters. Man listet einfach die beteiligten Agenten auf, und der Builder erstellt automatisch die notwendige Fan-Out- und Fan-In-Logik.

```python
# 03.python-agent-framework-workflow-ghmodel-concurrent.ipynb

research_agent = chat_client.as_agent(name="Researcher-Agent", ...)
plan_agent = chat_client.as_agent(name="Plan-Agent", ...)

# ConcurrentBuilder verwaltet die Fan-out/Fan-in-Logik
workflow = ConcurrentBuilder().participants([research_agent, plan_agent]).build()

# Führe den Workflow aus
events = await workflow.run("Plan a trip to Seattle in December")
```

Das Framework stellt sicher, dass `research_agent` und `plan_agent` parallel ausgeführt werden und ihre finalen Ausgaben in einer Liste gesammelt werden.

#### Analyse der .NET (C#) Implementierung

In .NET erfordert dieses Muster eine explizitere Definition. Eigene Executor (`ConcurrentStartExecutor` und `ConcurrentAggregationExecutor`) werden erstellt, um die Fan-Out- und Fan-In-Logik zu handhaben.

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

Der `WorkflowBuilder` verwendet dann `AddFanOutEdge` und `AddFanInEdge`, um den Graphen mit diesen benutzerdefinierten Executoren und den Agenten zu erstellen.

```csharp
// 03.dotnet-agent-framework-workflow-ghmodel-concurrent.ipynb

var workflow = new WorkflowBuilder(startExecutor)
            .AddFanOutEdge(startExecutor, targets: [researcherAgent, plannerAgent])
            .AddFanInEdge(aggregationExecutor, sources: [researcherAgent, plannerAgent])
            .WithOutputFrom(aggregationExecutor)
            .Build();
```

### Fall 4: Bedingter Workflow

Bedingte Workflows führen Verzweigungslogik ein und ermöglichen es dem System, je nach Zwischenergebnissen unterschiedliche Pfade zu nehmen.

#### Szenario-Hintergrund

Dieser Workflow automatisiert die Erstellung und Veröffentlichung eines technischen Tutorials.

1.  **Evangelist-Agent**: Schreibt einen Entwurf des Tutorials basierend auf einer vorgegebenen Gliederung und URLs.
2.  **ContentReviewer-Agent**: Prüft den Entwurf. Es wird überprüft, ob der Wortumfang 200 Wörter übersteigt.
3.  **Bedingter Zweig**:
      * **Wenn genehmigt (`Ja`)**: Der Workflow fährt mit dem `Publisher-Agent` fort.
      * **Wenn abgelehnt (`Nein`)**: Der Workflow stoppt und gibt den Ablehnungsgrund aus.
4.  **Publisher-Agent**: Wenn der Entwurf genehmigt ist, speichert dieser Agent den Inhalt in einer Markdown-Datei.

#### Analyse der Python-Implementierung

Dieses Beispiel verwendet eine benutzerdefinierte Funktion `select_targets`, um die bedingte Logik zu implementieren. Diese Funktion wird an `add_multi_selection_edge_group` übergeben und lenkt den Workflow basierend auf dem Feld `review_result` aus der Ausgabe des Reviewers.

```python
# 04.python-agent-framework-workflow-aifoundry-condition.ipynb

# Diese Funktion bestimmt den nächsten Schritt basierend auf dem Prüfergebnis
def select_targets(review: ReviewResult, target_ids: list[str]) -> list[str]:
    handle_review_id, save_draft_id = target_ids
    if review.review_result == "Yes":
        # Wenn genehmigt, fahre mit dem Executor 'save_draft' fort
        return [save_draft_id]
    else:
        # Wenn abgelehnt, fahre mit dem Executor 'handle_review' fort, um den Fehler zu melden
        return [handle_review_id]

# Der Workflow-Builder verwendet die Auswahlfunktion zur Steuerung
workflow = (
    WorkflowBuilder()
        .set_start_executor(evangelist_agent)
        .add_edge(evangelist_agent, reviewer_agent)
        .add_edge(reviewer_agent, to_reviewer_result)
        # Die Mehrfachauswahl-Kante implementiert die Bedingungslogik
        .add_multi_selection_edge_group(
            to_reviewer_result,
            [handle_review, save_draft],
            selection_func=select_targets,
        )
        .add_edge(save_draft, publisher_agent)
        .build()
)
```

Benutzerdefinierte Executor wie `to_reviewer_result` werden verwendet, um die JSON-Ausgabe der Agenten zu parsen und in stark typisierte Objekte umzuwandeln, die die Auswahlfunktion inspizieren kann.

#### Analyse der .NET (C#) Implementierung

Die .NET-Version verwendet einen ähnlichen Ansatz mit einer Bedingungsfunktion. Ein `Func<object?, bool>` wird definiert, um die `Result`-Eigenschaft des `ReviewResult`-Objekts zu prüfen.

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

Der `AddEdge`-Methode wird der `condition`-Parameter übergeben, der es dem `WorkflowBuilder` erlaubt, einen Verzweigungspfad zu erstellen. Der Workflow folgt nur dann der Kante zum `publishExecutor`, wenn die Bedingung `GetCondition(expectedResult: "Yes")` true ergibt. Andernfalls folgt er dem Pfad zum `sendReviewerExecutor`.

## Fazit

Das Microsoft Agent Framework Workflow bietet eine robuste und flexible Basis für die Orchestrierung komplexer Multi-Agent-Systeme. Durch die Nutzung der graphbasierten Architektur und Kernkomponenten können Entwickler anspruchsvolle Workflows sowohl in Python als auch in .NET gestalten und implementieren. Egal, ob Ihre Anwendung einfache sequenzielle Verarbeitung, parallele Ausführung oder dynamische bedingte Logik benötigt, das Framework bietet die Werkzeuge, um leistungsstarke, skalierbare und typsichere KI-gestützte Lösungen zu erstellen.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Haftungsausschluss**:
Dieses Dokument wurde mit dem KI-Übersetzungsdienst [Co-op Translator](https://github.com/Azure/co-op-translator) übersetzt. Obwohl wir uns um Genauigkeit bemühen, beachten Sie bitte, dass automatisierte Übersetzungen Fehler oder Ungenauigkeiten enthalten können. Das Originaldokument in seiner Ursprungssprache gilt als maßgebliche Quelle. Bei kritischen Informationen wird eine professionelle menschliche Übersetzung empfohlen. Wir übernehmen keine Haftung für Missverständnisse oder Fehlinterpretationen, die aus der Verwendung dieser Übersetzung entstehen.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->