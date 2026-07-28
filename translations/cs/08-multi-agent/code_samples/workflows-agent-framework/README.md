# Tvorba multiagentních aplikací pomocí Microsoft Agent Framework Workflow

Tento tutoriál vás provede pochopením a tvorbou multiagentních aplikací pomocí Microsoft Agent Framework. Prozkoumáme základní koncepty multiagentních systémů, ponoříme se do architektury komponenty Workflow tohoto frameworku a projdeme praktickými příklady v Pythonu a .NET pro různé vzory workflow.

## 1\. Pochopení multiagentních systémů

AI Agent je systém, který překračuje schopnosti standardního Velkého jazykového modelu (LLM). Dokáže vnímat své prostředí, činit rozhodnutí a podnikat kroky k dosažení konkrétních cílů. Multiagentní systém zahrnuje několik těchto agentů, kteří spolupracují na vyřešení problému, který by byl pro jednoho agenta obtížně nebo nemožně zvládnutelný.

### Běžné scénáře použití

  * **Komplexní řešení problémů**: Rozdělení velkého úkolu (např. plánování firemní akce) na menší podúkoly, které řeší specializovaní agenti (např. agent pro rozpočet, agent pro logistiku, agent pro marketing).
  * **Virtuální asistenti**: Hlavní asistenční agent deleguje úkoly jako plánování, výzkum a rezervace na jiné specializované agenty.
  * **Automatizovaná tvorba obsahu**: Workflow, kde jeden agent vytváří návrh obsahu, druhý ho kontroluje z hlediska přesnosti a tónu a třetí ho publikuje.

### Vzory multi-agentních systémů

Multiagentní systémy lze organizovat podle několika vzorů, které určují, jak spolu interagují:

  * **Sekvenční**: Agenti pracují v předem definovaném pořadí, jako montážní linka. Výstup jednoho agenta se stává vstupem pro dalšího.
  * **Současný**: Agenti pracují paralelně na různých částech úkolu a jejich výsledky se na konci agregují.
  * **Podmíněný**: Workflow následuje různé cesty podle výstupu agenta, podobně jako podmínka if-then-else.

## 2\. Architektura Microsoft Agent Framework Workflow

Workflow systém Agent Frameworku je pokročilý orchestrální motor navržený pro správu komplexních interakcí mezi více agenty. Je postaven na architektuře založené na grafech, která využívá [Pregel-style execution model](https://kowshik.github.io/JPregel/pregel_paper.pdf), kde zpracování probíhá ve synchronizovaných krocích nazvaných "supersteps."

### Základní komponenty

Architektura se skládá ze tří hlavních částí:

1.  **Executory**: Jsou to základní zpracovatelské jednotky. V našich příkladech je `Agent` typ exekutora. Každý exekutor může mít několik obslužných funkcí zpráv, které jsou automaticky vyvolávány na základě typu přijaté zprávy.
2.  **Hrany (Edges)**: Definují cestu, kterou zprávy putují mezi exekutory. Hrany mohou mít podmínky, které umožňují dynamické směrování informací grafem workflow.
3.  **Workflow**: Tato komponenta orchestruje celý proces, řídí executory, hrany a celkový tok vykonávání. Zajišťuje, že zprávy jsou zpracovány ve správném pořadí a streamuje události pro pozorovatelnost.

*Schéma znázorňující základní komponenty workflow systému.*

Tato struktura umožňuje vytvářet robustní a škálovatelné aplikace využívající základní vzory jako sekvenční řetězce, fan-out/fan-in pro paralelní zpracování a logiku switch-case pro podmíněné toky.

## 3\. Praktické příklady a analýza kódu

Nyní si ukážeme, jak implementovat různé vzory workflow pomocí frameworku. Podíváme se na kód v Pythonu i .NET pro každý příklad.

### Případ 1: Základní sekvenční workflow

Toto je nejjednodušší vzor, kdy se výstup jednoho agenta předává přímo dalšímu. Náš scénář zahrnuje hotelového agenta `FrontDesk`, který dělá doporučení na cestu, a agenta `Concierge`, který toto doporučení přezkoumá.

*Schéma základního workflow FrontDesk -> Concierge.*

#### Kontext scénáře

Cestovatel žádá o doporučení v Paříži.

1.  Agent `FrontDesk`, navržený pro stručnost, doporučí návštěvu muzea Louvre.
2.  Agent `Concierge`, který upřednostňuje autentické zážitky, toto doporučení obdrží, zkontroluje a poskytne zpětnou vazbu, naznačující lokálnější a méně turistickou alternativu.

#### Analýza implementace v Pythonu

V příkladu v Pythonu nejprve definujeme a vytvoříme dva agenty, z nichž každý má své specifické instrukce.

```python
# 01.python-agent-framework-workflow-ghmodel-basic.ipynb

# Definujte role agentů a instrukce
REVIEWER_NAME = "Concierge"
REVIEWER_INSTRUCTIONS = """
    You are a hotel concierge who has opinions about providing the most local and authentic experiences for travelers...
    """

FRONTDESK_NAME = "FrontDesk"
FRONTDESK_INSTRUCTIONS = """
    You are a Front Desk Travel Agent with ten years of experience and are known for brevity...
    """

# Vytvořte instance agentů
reviewer_agent = chat_client.as_agent(
    instructions=(REVIEWER_INSTRUCTIONS),
    name=REVIEWER_NAME,
)

front_desk_agent = chat_client.as_agent(
    instructions=(FRONTDESK_INSTRUCTIONS),
    name=FRONTDESK_NAME,
)
```

Dále použijeme `WorkflowBuilder` pro sestavení grafu. `front_desk_agent` je nastaven jako startovní bod a vytvoří se hrana spojující jeho výstup s `reviewer_agent`.

```python
# 01.python-agent-framework-workflow-ghmodel-basic.ipynb

workflow = WorkflowBuilder(start_executor=front_desk_agent).add_edge(front_desk_agent, reviewer_agent).build()
```

Nakonec je workflow spuštěn s počátečním uživatelským promptem.

```python
# 01.python-agent-framework-workflow-ghmodel-basic.ipynb

result =''
# run spustí pracovní postup; get_outputs() vrací výsledek výstupu vykonavatele.
events = await workflow.run('I would like to go to Paris.')
outputs = events.get_outputs()
result = outputs[0].text if outputs else ''
```

#### Analýza implementace v .NET (C\#)

Implementace v .NET sleduje velmi podobnou logiku. Nejprve jsou definovány konstanty pro jména agentů a jejich instrukce.

```csharp
// 01.dotnet-agent-framework-workflow-ghmodel-basic.ipynb

const string ReviewerAgentName = "Concierge";
const string ReviewerAgentInstructions = @"
    You are a hotel concierge who has opinions about providing the most local and authentic experiences for travelers...";

const string FrontDeskAgentName = "FrontDesk";
const string FrontDeskAgentInstructions = @"""
    You are a Front Desk Travel Agent with ten years of experience and are known for brevity...";
```

Agenti jsou vytvořeni pomocí `AzureOpenAIClient` (Responses API) a následně `WorkflowBuilder` definuje sekvenční tok přidáním hrany z `frontDeskAgent` na `reviewerAgent`.

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

Workflow je pak spuštěno s uživatelskou zprávou a výsledky jsou streamovány zpět.

### Případ 2: Více-krokové sekvenční workflow

Tento vzor rozšiřuje základní sekvenci o více agentů. Je ideální pro procesy vyžadující více etap zpracování nebo transformace.

#### Kontext scénáře

Uživatel poskytne obrázek obývacího pokoje a žádá o cenovou nabídku nábytku.

1.  **Sales-Agent**: Identifikuje položky nábytku na obrázku a vytvoří seznam.
2.  **Price-Agent**: Přijme seznam položek a poskytne podrobný rozpis cen, zahrnující rozpočtové, střední a prémiové možnosti.
3.  **Quote-Agent**: Obdrží oceněný seznam a formátuje ho do formální cenové nabídky v Markdownu.

*Schéma workflow Sales -> Price -> Quote.*

#### Analýza implementace v Pythonu

Jsou definováni tři agenti, každý se specializovanou rolí. Workflow je sestaven pomocí `add_edge` vytvořením řetězce: `sales_agent` -> `price_agent` -> `quote_agent`.

```python
# 02.python-agent-framework-workflow-ghmodel-sequential.ipynb

# Vytvořte tři specializované agenty
sales_agent = chat_client.as_agent(...)
price_agent = chat_client.as_agent(...)
quote_agent = chat_client.as_agent(...)

# Sestavte sekvenční pracovní postup
workflow = WorkflowBuilder(start_executor=sales_agent).add_edge(sales_agent, price_agent).add_edge(price_agent, quote_agent).build()
```

Vstupem je `ChatMessage`, který obsahuje text i URI obrázku. Framework přenáší výstup každého agenta dalšímu v sekvenci až do vygenerování finální nabídky.

```python
# 02.python-agent-framework-workflow-ghmodel-sequential.ipynb

# Uživatelská zpráva obsahuje jak text, tak obrázek
message = ChatMessage(
        role=Role.USER,
        contents=[
            TextContent(text="Please find the relevant furniture..."),
            DataContent(uri=image_uri, media_type="image/png")
        ]
)

# Spusťte pracovní postup
events = await workflow.run(message)
```

#### Analýza implementace v .NET (C\#)

.NET příklad kopíruje verzi v Pythonu. Jsou vytvořeni tři agenti (`salesagent`, `priceagent`, `quoteagent`). `WorkflowBuilder` je propojí sekvenčně.

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

Uživatelská zpráva je vytvořena s daty obrázku (ve formě bajtů) a textovým promptem. Metoda `InProcessExecution.RunStreamingAsync` spouští workflow a finální výstup je přijat ze streamu.

### Případ 3: Současný workflow

Tento vzor se používá, když lze úkoly vykonávat současně pro urychlení. Zahrnuje "fan-out" k více agentům a "fan-in" pro agregaci výsledků.

#### Kontext scénáře

Uživatel žádá o plán cesty do Seattlu.

1.  **Dispatcher (Fan-Out)**: Uživatelský požadavek je odeslán současně dvěma agentům.
2.  **Researcher-Agent**: Zkoumá atrakce, počasí a klíčové aspekty cesty do Seattlu v prosinci.
3.  **Plan-Agent**: Samostatně vytváří podrobný denní itinerář cesty.
4.  **Aggregator (Fan-In)**: Výstupy od researchera a plánovače jsou shromážděny a předloženy jako finální výsledek.

*Schéma současného workflow Researcher a Planner.*

#### Analýza implementace v Pythonu

`ConcurrentBuilder` usnadňuje tvorbu tohoto vzoru. Stačí vyjmenovat zúčastněné agenty a builder automaticky vytvoří potřebný fan-out a fan-in logiku.

```python
# 03.python-agent-framework-workflow-ghmodel-concurrent.ipynb

research_agent = chat_client.as_agent(name="Researcher-Agent", ...)
plan_agent = chat_client.as_agent(name="Plan-Agent", ...)

# ConcurrentBuilder zpracovává logiku rozvětvení/slučování
workflow = ConcurrentBuilder().participants([research_agent, plan_agent]).build()

# Spusťte pracovní postup
events = await workflow.run("Plan a trip to Seattle in December")
```

Framework zajišťuje, že `research_agent` a `plan_agent` běží paralelně a jejich finální výstupy jsou shromážděny do seznamu.

#### Analýza implementace v .NET (C\#)

V .NET je tento vzor definován explicitněji. Jsou vytvořeny vlastní exekutory (`ConcurrentStartExecutor` a `ConcurrentAggregationExecutor`), které zpracovávají fan-out a fan-in logiku.

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

`WorkflowBuilder` pak používá `AddFanOutEdge` a `AddFanInEdge` pro sestavení grafu s těmito vlastními exekutory a agenty.

```csharp
// 03.dotnet-agent-framework-workflow-ghmodel-concurrent.ipynb

var workflow = new WorkflowBuilder(startExecutor)
            .AddFanOutEdge(startExecutor, targets: [researcherAgent, plannerAgent])
            .AddFanInEdge(aggregationExecutor, sources: [researcherAgent, plannerAgent])
            .WithOutputFrom(aggregationExecutor)
            .Build();
```

### Případ 4: Podmíněný workflow

Podmíněné workflow zavádí větvenou logiku, která umožňuje systému ubírat se různými cestami na základě mezivýsledků.

#### Kontext scénáře

Tento workflow automatizuje tvorbu a publikaci technického tutoriálu.

1.  **Evangelist-Agent**: Napsání návrhu tutoriálu na základě dané osnovy a URL.
2.  **ContentReviewer-Agent**: Přezkoumá návrh. Kontroluje, zda počet slov přesahuje 200 slov.
3.  **Podmíněná větev**:
      * **Pokud je schváleno (`Ano`)**: Workflow pokračuje k `Publisher-Agent`.
      * **Pokud je zamítnuto (`Ne`)**: Workflow se zastaví a vypíše důvod zamítnutí.
4.  **Publisher-Agent**: Pokud je návrh schválen, tento agent uloží obsah do Markdown souboru.

#### Analýza implementace v Pythonu

V tomto příkladu se používá vlastní funkce `select_targets`, která implementuje podmíněnou logiku. Tato funkce je předána do `add_multi_selection_edge_group` a řídí workflow podle pole `review_result` z výstupu recenzenta.

```python
# 04.python-agent-framework-workflow-aifoundry-condition.ipynb

# Tato funkce určuje další krok na základě výsledku hodnocení
def select_targets(review: ReviewResult, target_ids: list[str]) -> list[str]:
    handle_review_id, save_draft_id = target_ids
    if review.review_result == "Yes":
        # Pokud je schváleno, pokračujte k exekutoru 'save_draft'
        return [save_draft_id]
    else:
        # Pokud je zamítnuto, pokračujte k exekutoru 'handle_review' pro nahlášení neúspěchu
        return [handle_review_id]

# Sestavovač workflow používá selekční funkci pro směrování
workflow = (
    WorkflowBuilder()
        .set_start_executor(evangelist_agent)
        .add_edge(evangelist_agent, reviewer_agent)
        .add_edge(reviewer_agent, to_reviewer_result)
        # Hrana s více výběry implementuje podmíněnou logiku
        .add_multi_selection_edge_group(
            to_reviewer_result,
            [handle_review, save_draft],
            selection_func=select_targets,
        )
        .add_edge(save_draft, publisher_agent)
        .build()
)
```

Vlastní exekutory jako `to_reviewer_result` se používají pro parsování JSON výstupu od agentů a převod na silně typované objekty, které může výběrová funkce kontrolovat.

#### Analýza implementace v .NET (C\#)

Verze v .NET používá podobný přístup s podmíněnou funkcí. Definuje se `Func<object?, bool>`, která kontroluje vlastnost `Result` objektu `ReviewResult`.

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

Parametr `condition` metody `AddEdge` umožňuje `WorkflowBuilderu` vytvořit větvenou cestu. Workflow poběží po hraně k `publishExecutor` pouze v případě, že podmínka `GetCondition(expectedResult: "Yes")` vrátí true. V opačném případě pokračuje cestou k `sendReviewerExecutor`.

## Závěr

Microsoft Agent Framework Workflow poskytuje robustní a flexibilní základ pro orchestraci komplexních multiagentních systémů. Využitím jeho grafové architektury a základních komponent mohou vývojáři navrhovat a implementovat sofistikované workflow jak v Pythonu, tak v .NET. Ať už vaše aplikace vyžaduje jednoduché sekvenční zpracování, paralelní vykonávání nebo dynamickou podmíněnou logiku, framework nabízí nástroje pro tvorbu výkonných, škálovatelných a typově bezpečných řešení poháněných AI.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Prohlášení o omezení odpovědnosti**:
Tento dokument byl přeložen pomocí AI překladatelské služby [Co-op Translator](https://github.com/Azure/co-op-translator). Přestože usilujeme o co největší přesnost, mějte prosím na paměti, že automatizované překlady mohou obsahovat chyby nebo nepřesnosti. Originální dokument v jeho mateřském jazyce by měl být považován za autoritativní zdroj. Pro kritické informace se doporučuje profesionální lidský překlad. Nejsme odpovědní za jakékoli nedorozumění nebo nesprávné interpretace vzniklé použitím tohoto překladu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->