# Tworzenie aplikacji wieloagentowych z użyciem Microsoft Agent Framework Workflow

Ten samouczek przeprowadzi Cię przez zrozumienie i budowanie aplikacji wieloagentowych przy użyciu Microsoft Agent Framework. Poznamy podstawowe koncepcje systemów wieloagentowych, zagłębimy się w architekturę komponentu Workflow frameworka oraz przejdziemy przez praktyczne przykłady w Python i .NET dla różnych wzorców przepływu pracy.

## 1\. Zrozumienie systemów wieloagentowych

Agent AI to system wykraczający poza możliwości standardowego dużego modelu językowego (LLM). Potrafi on postrzegać swoje otoczenie, podejmować decyzje i działać w celu osiągnięcia określonych celów. System wieloagentowy obejmuje kilku takich agentów współpracujących, aby rozwiązać problem, który byłby trudny lub niemożliwy do rozwiązania przez pojedynczego agenta.

### Typowe scenariusze zastosowań

  * **Rozwiązywanie złożonych problemów**: Rozbicie dużego zadania (np. planowanie wydarzenia firmowego) na mniejsze podzadania obsługiwane przez wyspecjalizowanych agentów (np. agent budżetu, agent logistyki, agent marketingu).
  * **Wirtualni asystenci**: Główny agent asystent delegujący zadania takie jak planowanie, badania czy rezerwacje do innych wyspecjalizowanych agentów.
  * **Zautomatyzowane tworzenie treści**: Przepływ pracy, w którym jeden agent tworzy szkic treści, inny go weryfikuje pod kątem dokładności i tonu, a trzeci publikuje.

### Wzorce wieloagentowe

Systemy wieloagentowe mogą być organizowane w różnych wzorcach, które określają sposób ich interakcji:

  * **Sekwencyjny**: Agenci pracują w określonej kolejności, jak na linii montażowej. Wyjście jednego agenta staje się wejściem dla następnego.
  * **Równoległy**: Agenci pracują jednocześnie nad różnymi częściami zadania, a ich wyniki są zbierane na końcu.
  * **Warunkowy**: Przepływ pracy podąża różnymi ścieżkami w oparciu o wynik agenta, podobnie jak instrukcja if-then-else.

## 2\. Architektura Microsoft Agent Framework Workflow

System workflow frameworka Agent Framework to zaawansowany silnik orkiestracji zaprojektowany do zarządzania złożonymi interakcjami między wieloma agentami. Opiera się na architekturze grafowej wykorzystującej [model wykonania w stylu Pregel](https://kowshik.github.io/JPregel/pregel_paper.pdf), w której przetwarzanie odbywa się w zsynchronizowanych krokach zwanych "supersteps".

### Główne komponenty

Architektura składa się z trzech głównych części:

1.  **Wykonawcy (Executors)**: To podstawowe jednostki przetwarzające. W naszych przykładach `Agent` jest typem wykonawcy. Każdy wykonawca może mieć wiele obsługujących komunikaty handlerów, które są wywoływane automatycznie w zależności od typu odebranego komunikatu.
2.  **Krawędzie (Edges)**: Definiują ścieżkę, którą podążają komunikaty między wykonawcami. Krawędzie mogą mieć warunki, co pozwala na dynamiczne kierowanie informacji w grafie przepływu pracy.
3.  **Workflow**: Ten komponent orkiestruje cały proces, zarządzając wykonawcami, krawędziami i całym przebiegiem wykonania. Zapewnia, że komunikaty są przetwarzane w prawidłowej kolejności i strumieniuje zdarzenia dla obserwowalności.

*Diagram ilustrujący główne komponenty systemu workflow.*

Ta struktura pozwala na budowanie solidnych i skalowalnych aplikacji wykorzystujących podstawowe wzorce takie jak łańcuchy sekwencyjne, fan-out/fan-in do przetwarzania równoległego oraz logikę switch-case do przepływów warunkowych.

## 3\. Praktyczne przykłady i analiza kodu

Teraz przyjrzyjmy się, jak zaimplementować różne wzorce workflow z użyciem frameworka. Omówimy przykłady kodu w Python i .NET dla każdego przypadku.

### Przypadek 1: Podstawowy sekwencyjny workflow

To najprostszy wzorzec, w którym wyjście jednego agenta jest przekazywane bezpośrednio kolejnemu. Nasz scenariusz to agent hotelowy `FrontDesk` rekomendujący podróż, która jest następnie recenzowana przez agenta `Concierge`.

*Diagram podstawowego przepływu FrontDesk -> Concierge.*

#### Tło scenariusza

Podróżny prosi o rekomendację w Paryżu.

1.  Agent `FrontDesk`, zaprojektowany zwięźle, proponuje odwiedzenie Muzeum Luwru.
2.  Agent `Concierge`, który stawia na autentyczne doświadczenia, otrzymuje tę sugestię. Przegląda rekomendację i udziela opinii, proponując bardziej lokalną, mniej turystyczną alternatywę.

#### Analiza implementacji w Python

W przykładzie Python najpierw definiujemy i tworzymy dwóch agentów, każdy z określonymi instrukcjami.

```python
# 01.python-agent-framework-workflow-ghmodel-basic.ipynb

# Zdefiniuj role agentów i instrukcje
REVIEWER_NAME = "Concierge"
REVIEWER_INSTRUCTIONS = """
    You are a hotel concierge who has opinions about providing the most local and authentic experiences for travelers...
    """

FRONTDESK_NAME = "FrontDesk"
FRONTDESK_INSTRUCTIONS = """
    You are a Front Desk Travel Agent with ten years of experience and are known for brevity...
    """

# Utwórz instancje agentów
reviewer_agent = chat_client.as_agent(
    instructions=(REVIEWER_INSTRUCTIONS),
    name=REVIEWER_NAME,
)

front_desk_agent = chat_client.as_agent(
    instructions=(FRONTDESK_INSTRUCTIONS),
    name=FRONTDESK_NAME,
)
```

Następnie `WorkflowBuilder` służy do konstrukcji grafu. `front_desk_agent` jest ustawiony jako punkt startowy, a krawędź tworzy połączenie z `reviewer_agent`.

```python
# 01.python-agent-framework-workflow-ghmodel-basic.ipynb

workflow = WorkflowBuilder(start_executor=front_desk_agent).add_edge(front_desk_agent, reviewer_agent).build()
```

W końcu workflow jest wykonywany z początkowym zapytaniem użytkownika.

```python
# 01.python-agent-framework-workflow-ghmodel-basic.ipynb

result =''
# run wykonuje przepływ pracy; get_outputs() zwraca wynik wykonawcy wyjścia.
events = await workflow.run('I would like to go to Paris.')
outputs = events.get_outputs()
result = outputs[0].text if outputs else ''
```

#### Analiza implementacji w .NET (C#)

Implementacja .NET stosuje bardzo podobną logikę. Najpierw definiowane są stałe z nazwami i instrukcjami agentów.

```csharp
// 01.dotnet-agent-framework-workflow-ghmodel-basic.ipynb

const string ReviewerAgentName = "Concierge";
const string ReviewerAgentInstructions = @"
    You are a hotel concierge who has opinions about providing the most local and authentic experiences for travelers...";

const string FrontDeskAgentName = "FrontDesk";
const string FrontDeskAgentInstructions = @"""
    You are a Front Desk Travel Agent with ten years of experience and are known for brevity...";
```

Agenci są tworzeni przy użyciu `AzureOpenAIClient` (API Responses), a następnie `WorkflowBuilder` definiuje sekwencyjny przepływ, dodając krawędź od `frontDeskAgent` do `reviewerAgent`.

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

Workflow jest wykonywany za pomocą wiadomości użytkownika, a wyniki są przesyłane strumieniowo.

### Przypadek 2: Wieloetapowy sekwencyjny workflow

Ten wzorzec rozszerza podstawową sekwencję o większą liczbę agentów. Jest idealny dla procesów wymagających wielu etapów udoskonaleń lub transformacji.

#### Tło scenariusza

Użytkownik przesyła zdjęcie salonu i prosi o wycenę mebli.

1.  **Sales-Agent**: Identyfikuje meble na zdjęciu i tworzy listę.
2.  **Price-Agent**: Przyjmuje listę i podaje szczegółowy podział cenowy, w tym opcje budżetowe, średniopółkowe i premium.
3.  **Quote-Agent**: Otrzymuje wycenioną listę i formatuje ją do formalnego dokumentu oferty w Markdown.

*Diagram przepływu Sales -> Price -> Quote.*

#### Analiza implementacji w Python

Definiujemy trzech agentów, każdy z wyspecjalizowaną rolą. Workflow budowany jest z użyciem `add_edge`, tworząc łańcuch: `sales_agent` -> `price_agent` -> `quote_agent`.

```python
# 02.python-agent-framework-workflow-ghmodel-sequential.ipynb

# Utwórz trzech wyspecjalizowanych agentów
sales_agent = chat_client.as_agent(...)
price_agent = chat_client.as_agent(...)
quote_agent = chat_client.as_agent(...)

# Zbuduj sekwencyjny przepływ pracy
workflow = WorkflowBuilder(start_executor=sales_agent).add_edge(sales_agent, price_agent).add_edge(price_agent, quote_agent).build()
```

Wejściem jest `ChatMessage`, które zawiera zarówno tekst, jak i URI obrazu. Framework obsługuje przekazywanie wyjścia każdego agenta do następnego w kolejności aż do wygenerowania końcowej oferty.

```python
# 02.python-agent-framework-workflow-ghmodel-sequential.ipynb

# Wiadomość użytkownika zawiera zarówno tekst, jak i obraz
message = ChatMessage(
        role=Role.USER,
        contents=[
            TextContent(text="Please find the relevant furniture..."),
            DataContent(uri=image_uri, media_type="image/png")
        ]
)

# Uruchom przepływ pracy
events = await workflow.run(message)
```

#### Analiza implementacji w .NET (C#)

Przykład .NET jest odpowiednikiem wersji Python. Tworzy trzech agentów (`salesagent`, `priceagent`, `quoteagent`). `WorkflowBuilder` łączy je sekwencyjnie.

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

Wiadomość użytkownika zawiera dane obrazu (jako bajty) oraz tekstowy prompt. Metoda `InProcessExecution.RunStreamingAsync` rozpoczyna workflow, a wynik końcowy jest przechwytywany ze strumienia.

### Przypadek 3: Równoległy workflow

Ten wzorzec stosowany jest, gdy zadania mogą być wykonywane jednocześnie, aby zaoszczędzić czas. Polega na "fan-out" do wielu agentów oraz "fan-in" agregującym wyniki.

#### Tło scenariusza

Użytkownik prosi o zaplanowanie podróży do Seattle.

1.  **Dispatcher (Fan-Out)**: Prośba użytkownika jest wysyłana do dwóch agentów jednocześnie.
2.  **Researcher-Agent**: Bada atrakcje, pogodę i kluczowe kwestie podróży do Seattle w grudniu.
3.  **Plan-Agent**: Niezależnie tworzy szczegółowy, dzienny plan podróży.
4.  **Aggregator (Fan-In)**: Wyniki od badacza i planisty są zbierane i prezentowane łącznie jako efekt końcowy.

*Diagram równoległego przepływu Researcher i Planner.*

#### Analiza implementacji w Python

`ConcurrentBuilder` upraszcza tworzenie tego wzorca. Wystarczy wymienić uczestniczących agentów, a builder automatycznie tworzy potrzebną logikę fan-out i fan-in.

```python
# 03.python-agent-framework-workflow-ghmodel-concurrent.ipynb

research_agent = chat_client.as_agent(name="Researcher-Agent", ...)
plan_agent = chat_client.as_agent(name="Plan-Agent", ...)

# ConcurrentBuilder obsługuje logikę rozgałęzienia/złączenia
workflow = ConcurrentBuilder().participants([research_agent, plan_agent]).build()

# Uruchom przepływ pracy
events = await workflow.run("Plan a trip to Seattle in December")
```

Framework zapewnia, że `research_agent` i `plan_agent` wykonują się równolegle, a ich końcowe wyjścia są zbierane do listy.

#### Analiza implementacji w .NET (C#)

W .NET ten wzorzec wymaga bardziej wyraźnej definicji. Tworzone są niestandardowe wykonawcy (`ConcurrentStartExecutor` i `ConcurrentAggregationExecutor`), którzy obsługują logikę fan-out i fan-in.

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

`WorkflowBuilder` następnie używa `AddFanOutEdge` i `AddFanInEdge` do budowy grafu z tymi niestandardowymi wykonawcami i agentami.

```csharp
// 03.dotnet-agent-framework-workflow-ghmodel-concurrent.ipynb

var workflow = new WorkflowBuilder(startExecutor)
            .AddFanOutEdge(startExecutor, targets: [researcherAgent, plannerAgent])
            .AddFanInEdge(aggregationExecutor, sources: [researcherAgent, plannerAgent])
            .WithOutputFrom(aggregationExecutor)
            .Build();
```

### Przypadek 4: Warunkowy workflow

Workflow warunkowy wprowadza logikę rozgałęziającą, pozwalając systemowi podążać różnymi ścieżkami w oparciu o wyniki pośrednie.

#### Tło scenariusza

Ten workflow automatyzuje tworzenie i publikację technicznego samouczka.

1.  **Evangelist-Agent**: Pisze szkic samouczka na podstawie podanego zarysu i URL.
2.  **ContentReviewer-Agent**: Recenzuje szkic. Sprawdza, czy liczba słów przekracza 200.
3.  **Rozgałęzienie warunkowe**:
      * **Jeśli zatwierdzony (`Tak`)**: Workflow przechodzi do `Publisher-Agent`.
      * **Jeśli odrzucony (`Nie`)**: Workflow zatrzymuje się i zwraca powód odrzucenia.
4.  **Publisher-Agent**: Jeśli szkic jest zatwierdzony, agent zapisuje zawartość do pliku Markdown.

#### Analiza implementacji w Python

Ten przykład używa niestandardowej funkcji `select_targets`, aby zaimplementować logikę warunkową. Funkcja ta jest przekazana do `add_multi_selection_edge_group` i kieruje workflow na podstawie pola `review_result` w wyjściu recenzenta.

```python
# 04.python-agent-framework-workflow-aifoundry-condition.ipynb

# Ta funkcja określa następny krok na podstawie wyniku recenzji
def select_targets(review: ReviewResult, target_ids: list[str]) -> list[str]:
    handle_review_id, save_draft_id = target_ids
    if review.review_result == "Yes":
        # Jeśli zatwierdzono, przejdź do wykonawcy 'save_draft'
        return [save_draft_id]
    else:
        # Jeśli odrzucono, przejdź do wykonawcy 'handle_review', aby zgłosić niepowodzenie
        return [handle_review_id]

# Konstruktor workflow używa funkcji wyboru do routingu
workflow = (
    WorkflowBuilder()
        .set_start_executor(evangelist_agent)
        .add_edge(evangelist_agent, reviewer_agent)
        .add_edge(reviewer_agent, to_reviewer_result)
        # Krawędź wielokrotnego wyboru implementuje logikę warunkową
        .add_multi_selection_edge_group(
            to_reviewer_result,
            [handle_review, save_draft],
            selection_func=select_targets,
        )
        .add_edge(save_draft, publisher_agent)
        .build()
)
```

Niestandardowe wykonawcy jak `to_reviewer_result` służą do parsowania JSON-owego wyjścia agentów i konwertowania go na typowane obiekty, które funkcja selekcyjna może analizować.

#### Analiza implementacji w .NET (C#)

W wersji .NET stosuje się podobne podejście z funkcją warunkową. Definiuje się `Func<object?, bool>`, która sprawdza właściwość `Result` obiektu `ReviewResult`.

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

Metoda `AddEdge` z parametrem `condition` pozwala `WorkflowBuilder` stworzyć rozgałęzioną ścieżkę. Workflow podąży krawędzią do `publishExecutor` tylko jeśli warunek `GetCondition(expectedResult: "Yes")` zwróci prawdę. W przeciwnym razie zostanie wybrana ścieżka do `sendReviewerExecutor`.

## Podsumowanie

Microsoft Agent Framework Workflow dostarcza solidną i elastyczną podstawę do orkiestracji złożonych systemów wieloagentowych. Wykorzystując jego architekturę grafową i główne komponenty, deweloperzy mogą projektować i implementować zaawansowane workflowy zarówno w Python, jak i .NET. Niezależnie od tego, czy Twoja aplikacja wymaga prostego przetwarzania sekwencyjnego, wykonania równoległego czy dynamicznej logiki warunkowej, framework oferuje narzędzia do budowy potężnych, skalowalnych i typowanych rozwiązań AI.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Zastrzeżenie**:
Niniejszy dokument został przetłumaczony za pomocą usługi tłumaczenia AI [Co-op Translator](https://github.com/Azure/co-op-translator). Choć dążymy do dokładności, prosimy pamiętać, że automatyczne tłumaczenia mogą zawierać błędy lub niedokładności. Oryginalny dokument w jego języku źródłowym należy uznawać za autorytatywne źródło. W przypadku informacji krytycznych zalecane jest skorzystanie z profesjonalnego tłumaczenia wykonanego przez człowieka. Nie ponosimy odpowiedzialności za jakiekolwiek nieporozumienia lub błędne interpretacje wynikające z użycia tego tłumaczenia.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->