# Tworzenie aplikacji wieloagentowych z Microsoft Agent Framework Workflow

Ten poradnik pomoże Ci zrozumieć i zbudować aplikacje wieloagentowe przy użyciu Microsoft Agent Framework. Zbadamy podstawowe pojęcia systemów wieloagentowych, zagłębimy się w architekturę komponentu Workflow frameworku i przejdziemy przez praktyczne przykłady w Pythonie i .NET dla różnych wzorców przepływu pracy.

## 1\. Zrozumienie systemów wieloagentowych

Agent AI to system, który wykracza poza możliwości standardowego modelu językowego (LLM). Potrafi postrzegać swoje otoczenie, podejmować decyzje i wykonywać działania w celu osiągnięcia określonych celów. System wieloagentowy obejmuje kilka takich agentów współpracujących w celu rozwiązania problemu, który byłby trudny lub niemożliwy do rozwiązania przez pojedynczego agenta.

### Typowe scenariusze zastosowań

  * **Rozwiązywanie złożonych problemów**: Rozbijanie dużego zadania (np. planowanie wydarzenia firmowego) na mniejsze podzadania obsługiwane przez wyspecjalizowane agenty (np. agent budżetowy, agent logistyczny, agent marketingowy).
  * **Wirtualni asystenci**: Główny agent asystent deleguje zadania, takie jak planowanie, badania i rezerwacje, do innych wyspecjalizowanych agentów.
  * **Automatyczne tworzenie treści**: Przepływ pracy, w którym jeden agent tworzy szkic treści, drugi sprawdza jej dokładność i ton, a trzeci publikuje ją.

### Wzorce wieloagentowe

Systemy wieloagentowe mogą być organizowane w różne wzorce, które określają sposób ich interakcji:

  * **Sekwencyjny**: Agenci pracują w określonej kolejności, jak na linii montażowej. Wynik jednego agenta staje się wejściem dla następnego.
  * **Równoległy**: Agenci pracują równolegle nad różnymi częściami zadania, a ich wyniki są agregowane na końcu.
  * **Warunkowy**: Przepływ pracy podąża różnymi ścieżkami w zależności od wyniku działania agenta, podobnie jak instrukcja if-then-else.

## 2\. Architektura Workflow w Microsoft Agent Framework

System Workflow w Agent Framework to zaawansowany silnik orkiestracji zaprojektowany do zarządzania złożonymi interakcjami między wieloma agentami. Jest oparty na architekturze grafowej, która wykorzystuje [model wykonania w stylu Pregel](https://kowshik.github.io/JPregel/pregel_paper.pdf), gdzie przetwarzanie odbywa się w zsynchronizowanych krokach zwanych "supersteps".

### Główne komponenty

Architektura składa się z trzech głównych części:

1.  **Wykonawcy (Executors)**: Podstawowe jednostki przetwarzania. W naszych przykładach `Agent` jest typem wykonawcy. Każdy wykonawca może mieć wiele obsługiwanych wiadomości, które są automatycznie wywoływane w zależności od rodzaju otrzymanej wiadomości.
2.  **Krawędzie (Edges)**: Określają ścieżkę, którą wiadomości przemieszczają się między wykonawcami. Krawędzie mogą mieć warunki, umożliwiając dynamiczne kierowanie informacji przez graf przepływu pracy.
3.  **Workflow**: Ten komponent orkiestruje cały proces, zarządzając wykonawcami, krawędziami i ogólnym przepływem wykonania. Zapewnia, że wiadomości są przetwarzane w odpowiedniej kolejności i przesyła zdarzenia dla obserwowalności.

*Diagram ilustrujący główne komponenty systemu Workflow.*

Ta struktura pozwala na budowanie solidnych i skalowalnych aplikacji przy użyciu podstawowych wzorców, takich jak sekwencyjne łańcuchy, fan-out/fan-in dla przetwarzania równoległego oraz logika switch-case dla przepływów warunkowych.

## 3\. Praktyczne przykłady i analiza kodu

Przejdźmy teraz do implementacji różnych wzorców przepływu pracy przy użyciu frameworku. Przyjrzymy się przykładom w Pythonie i .NET dla każdego przypadku.

### Przypadek 1: Podstawowy sekwencyjny przepływ pracy

To najprostszy wzorzec, w którym wynik jednego agenta jest bezpośrednio przekazywany do kolejnego. Nasz scenariusz obejmuje agenta hotelowego `FrontDesk`, który przedstawia rekomendację podróży, a następnie jest ona oceniana przez agenta `Concierge`.

*Diagram podstawowego przepływu FrontDesk -> Concierge.*

#### Tło scenariusza

Podróżnik pyta o rekomendację w Paryżu.

1.  Agent `FrontDesk`, zaprojektowany z myślą o zwięzłości, sugeruje odwiedzenie Luwru.
2.  Agent `Concierge`, który priorytetowo traktuje autentyczne doświadczenia, otrzymuje tę sugestię. Przegląda rekomendację i proponuje bardziej lokalną, mniej turystyczną alternatywę.

#### Analiza implementacji w Pythonie

W przykładzie w Pythonie najpierw definiujemy i tworzymy dwóch agentów, z których każdy ma określone instrukcje.

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

Następnie używamy `WorkflowBuilder`, aby skonstruować graf. `front_desk_agent` jest ustawiony jako punkt początkowy, a krawędź jest tworzona, aby połączyć jego wynik z `reviewer_agent`.

```python
# 01.python-agent-framework-workflow-ghmodel-basic.ipynb

workflow = WorkflowBuilder().set_start_executor(front_desk_agent).add_edge(front_desk_agent, reviewer_agent).build()
```

Na końcu przepływ pracy jest wykonywany z początkowym zapytaniem użytkownika.

```python
# 01.python-agent-framework-workflow-ghmodel-basic.ipynb

result =''
# The run_stream method executes the workflow and streams events.
async for event in workflow.run_stream('I would like to go to Paris.'):
    if isinstance(event, WorkflowEvent):
        result += str(event.data)
```

#### Analiza implementacji w .NET (C#)

Implementacja w .NET podąża bardzo podobną logiką. Najpierw definiowane są stałe dla nazw agentów i ich instrukcji.

```csharp
// 01.dotnet-agent-framework-workflow-ghmodel-basic.ipynb

const string ReviewerAgentName = "Concierge";
const string ReviewerAgentInstructions = @"
    You are an are hotel concierge who has opinions about providing the most local and authentic experiences for travelers...";

const string FrontDeskAgentName = "FrontDesk";
const string FrontDeskAgentInstructions = @"""
    You are a Front Desk Travel Agent with ten years of experience and are known for brevity...";
```

Agenci są tworzeni przy użyciu `OpenAIClient`, a następnie `WorkflowBuilder` definiuje sekwencyjny przepływ, dodając krawędź od `frontDeskAgent` do `reviewerAgent`.

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

Przepływ pracy jest następnie uruchamiany z wiadomością użytkownika, a wyniki są przesyłane strumieniowo.

### Przypadek 2: Wieloetapowy sekwencyjny przepływ pracy

Ten wzorzec rozszerza podstawową sekwencję o więcej agentów. Jest idealny dla procesów wymagających wielu etapów udoskonalania lub transformacji.

#### Tło scenariusza

Użytkownik dostarcza obraz salonu i prosi o wycenę mebli.

1.  **Sales-Agent**: Identyfikuje elementy mebli na obrazie i tworzy listę.
2.  **Price-Agent**: Bierze listę elementów i dostarcza szczegółowy podział cenowy, w tym opcje budżetowe, średnie i premium.
3.  **Quote-Agent**: Otrzymuje wycenioną listę i formatuje ją w formalny dokument wyceny w Markdown.

*Diagram przepływu Sales -> Price -> Quote.*

#### Analiza implementacji w Pythonie

Trzej agenci są definiowani, każdy z wyspecjalizowaną rolą. Przepływ pracy jest konstruowany przy użyciu `add_edge`, aby stworzyć łańcuch: `sales_agent` -> `price_agent` -> `quote_agent`.

```python
# 02.python-agent-framework-workflow-ghmodel-sequential.ipynb

# Create three specialized agents
sales_agent = chat_client.create_agent(...)
price_agent = chat_client.create_agent(...)
quote_agent = chat_client.create_agent(...)

# Build the sequential workflow
workflow = WorkflowBuilder().set_start_executor(sales_agent).add_edge(sales_agent, price_agent).add_edge(price_agent, quote_agent).build()
```

Wejście to `ChatMessage`, które zawiera zarówno tekst, jak i URI obrazu. Framework obsługuje przekazywanie wyniku każdego agenta do następnego w sekwencji, aż do wygenerowania końcowej wyceny.

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

#### Analiza implementacji w .NET (C#)

Przykład w .NET odzwierciedla wersję w Pythonie. Trzej agenci (`salesagent`, `priceagent`, `quoteagent`) są tworzeni. `WorkflowBuilder` łączy ich sekwencyjnie.

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

Wiadomość użytkownika jest konstruowana z danymi obrazu (jako bajty) i tekstowym zapytaniem. Metoda `InProcessExecution.StreamAsync` inicjuje przepływ pracy, a końcowy wynik jest przechwytywany ze strumienia.

### Przypadek 3: Równoległy przepływ pracy

Ten wzorzec jest używany, gdy zadania mogą być wykonywane jednocześnie, aby zaoszczędzić czas. Obejmuje "fan-out" do wielu agentów i "fan-in" do agregacji wyników.

#### Tło scenariusza

Użytkownik prosi o zaplanowanie podróży do Seattle.

1.  **Dispatcher (Fan-Out)**: Żądanie użytkownika jest wysyłane do dwóch agentów jednocześnie.
2.  **Researcher-Agent**: Bada atrakcje, pogodę i kluczowe kwestie dotyczące podróży do Seattle w grudniu.
3.  **Plan-Agent**: Niezależnie tworzy szczegółowy plan podróży dzień po dniu.
4.  **Aggregator (Fan-In)**: Wyniki od badacza i planisty są zbierane i prezentowane razem jako końcowy wynik.

*Diagram równoległego przepływu Researcher i Planner.*

#### Analiza implementacji w Pythonie

`ConcurrentBuilder` upraszcza tworzenie tego wzorca. Wystarczy wymienić uczestniczących agentów, a builder automatycznie tworzy niezbędną logikę fan-out i fan-in.

```python
# 03.python-agent-framework-workflow-ghmodel-concurrent.ipynb

research_agent = chat_client.create_agent(name="Researcher-Agent", ...)
plan_agent = chat_client.create_agent(name="Plan-Agent", ...)

# ConcurrentBuilder handles the fan-out/fan-in logic
workflow = ConcurrentBuilder().participants([research_agent, plan_agent]).build()

# Run the workflow
events = await workflow.run("Plan a trip to Seattle in December")
```

Framework zapewnia, że `research_agent` i `plan_agent` wykonują się równolegle, a ich końcowe wyniki są zbierane w listę.

#### Analiza implementacji w .NET (C#)

W .NET ten wzorzec wymaga bardziej szczegółowej definicji. Tworzone są niestandardowe wykonawcy (`ConcurrentStartExecutor` i `ConcurrentAggregationExecutor`), aby obsłużyć logikę fan-out i fan-in.

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

`WorkflowBuilder` używa `AddFanOutEdge` i `AddFanInEdge`, aby skonstruować graf z tymi niestandardowymi wykonawcami i agentami.

```csharp
// 03.dotnet-agent-framework-workflow-ghmodel-concurrent.ipynb

var workflow = new WorkflowBuilder(startExecutor)
            .AddFanOutEdge(startExecutor, targets: [researcherAgent, plannerAgent])
            .AddFanInEdge(aggregationExecutor, sources: [researcherAgent, plannerAgent])
            .WithOutputFrom(aggregationExecutor)
            .Build();
```

### Przypadek 4: Warunkowy przepływ pracy

Warunkowe przepływy pracy wprowadzają logikę rozgałęziania, pozwalając systemowi na podążanie różnymi ścieżkami w zależności od wyników pośrednich.

#### Tło scenariusza

Ten przepływ pracy automatyzuje tworzenie i publikację technicznego poradnika.

1.  **Evangelist-Agent**: Pisze szkic poradnika na podstawie podanego zarysu i URL-i.
2.  **ContentReviewer-Agent**: Przegląda szkic. Sprawdza, czy liczba słów przekracza 200.
3.  **Rozgałęzienie warunkowe**:
      * **Jeśli zatwierdzono (`Yes`)**: Przepływ pracy przechodzi do `Publisher-Agent`.
      * **Jeśli odrzucono (`No`)**: Przepływ pracy zatrzymuje się i wyświetla powód odrzucenia.
4.  **Publisher-Agent**: Jeśli szkic zostanie zatwierdzony, ten agent zapisuje treść do pliku Markdown.

#### Analiza implementacji w Pythonie

Ten przykład używa niestandardowej funkcji `select_targets`, aby zaimplementować logikę warunkową. Funkcja ta jest przekazywana do `add_multi_selection_edge_group` i kieruje przepływ pracy na podstawie pola `review_result` z wyniku recenzenta.

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

Niestandardowi wykonawcy, tacy jak `to_reviewer_result`, są używani do parsowania wyjścia JSON od agentów i konwertowania go na obiekty silnie typowane, które funkcja selekcji może analizować.

#### Analiza implementacji w .NET (C#)

Wersja .NET używa podobnego podejścia z funkcją warunkową. Definiowany jest `Func<object?, bool`, aby sprawdzić właściwość `Result` obiektu `ReviewResult`.

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

Parametr `condition` metody `AddEdge` pozwala `WorkflowBuilder` na stworzenie rozgałęzienia. Przepływ pracy podąży krawędzią do `publishExecutor` tylko wtedy, gdy warunek `GetCondition(expectedResult: "Yes")` zwróci wartość true. W przeciwnym razie podąży ścieżką do `sendReviewerExecutor`.

## Podsumowanie

Microsoft Agent Framework Workflow zapewnia solidne i elastyczne podstawy do orkiestracji złożonych systemów wieloagentowych. Dzięki wykorzystaniu jego architektury grafowej i głównych komponentów, programiści mogą projektować i implementować zaawansowane przepływy pracy w Pythonie i .NET. Niezależnie od tego, czy Twoja aplikacja wymaga prostego przetwarzania sekwencyjnego, równoległego wykonania czy dynamicznej logiki warunkowej, framework oferuje narzędzia do budowy potężnych, skalowalnych i typowo bezpiecznych rozwiązań opartych na AI.

---

**Zastrzeżenie**:  
Ten dokument został przetłumaczony za pomocą usługi tłumaczenia AI [Co-op Translator](https://github.com/Azure/co-op-translator). Chociaż dokładamy wszelkich starań, aby tłumaczenie było precyzyjne, prosimy pamiętać, że automatyczne tłumaczenia mogą zawierać błędy lub nieścisłości. Oryginalny dokument w jego rodzimym języku powinien być uznawany za wiarygodne źródło. W przypadku informacji krytycznych zaleca się skorzystanie z profesjonalnego tłumaczenia przez człowieka. Nie ponosimy odpowiedzialności za jakiekolwiek nieporozumienia lub błędne interpretacje wynikające z użycia tego tłumaczenia.