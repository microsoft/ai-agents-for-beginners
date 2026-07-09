# Tvorba multi-agentních aplikací pomocí Microsoft Agent Framework Workflow

Tento tutoriál vás provede pochopením a vytvářením multi-agentních aplikací pomocí Microsoft Agent Framework. Prozkoumáme základní koncepty multi-agentních systémů, ponoříme se do architektury komponenty Workflow tohoto frameworku a projdeme praktické příklady v Pythonu i .NET pro různé vzory workflow.

## 1\. Porozumění multi-agentním systémům

AI Agent je systém, který přesahuje schopnosti standardního velkého jazykového modelu (LLM). Dokáže vnímat své prostředí, činit rozhodnutí a podnikat kroky k dosažení konkrétních cílů. Multi-agentní systém zahrnuje několik těchto agentů, kteří spolupracují na řešení úlohy, kterou by bylo těžké nebo nemožné zvládnout jedinému agentovi samostatně.

### Běžné aplikační scénáře

  * **Řešení složitých problémů**: Rozdělění velkého úkolu (například plánování celofiremní události) na menší podúkoly, které řeší specializovaní agenti (například agent rozpočtu, agent logistiky, agent marketingu).
  * **Virtuální asistenti**: Hlavní asistenční agent delegující úkoly, jako je plánování, výzkum a rezervace, na jiné specializované agenty.
  * **Automatizovaná tvorba obsahu**: Workflow, kde jeden agent vytváří obsah, druhý jej kontroluje z hlediska přesnosti a tónu, a třetí ho publikuje.

### Vzory multi-agentních systémů

Multi-agentní systémy lze organizovat do několika vzorů, které určují, jak spolu interagují:

  * **Sekvenční**: Agenti pracují v předem definovaném pořadí, podobně jako výrobní linka. Výstup jednoho agenta se stává vstupem pro dalšího.
  * **Současné**: Agenti pracují paralelně na různých částech úkolu a jejich výsledky jsou na konci seskupeny.
  * **Podmíněné**: Workflow následuje různé cesty na základě výstupu agenta, podobně jako konstrukce if-then-else.

## 2\. Architektura Microsoft Agent Framework Workflow

Workflow systém Agent Frameworku je pokročilý orchestrátor navržený pro řízení složitých interakcí mezi více agenty. Je postaven na grafové architektuře, která využívá [Pregel-style execution model](https://kowshik.github.io/JPregel/pregel_paper.pdf), kde zpracování probíhá v synchronizovaných krocích nazývaných "supersteppy."

### Základní komponenty

Architektura se skládá ze tří hlavních částí:

1.  **Executory**: To jsou základní zpracovatelské jednotky. V našich příkladech je `Agent` typ executoru. Každý executor může mít několik handlerů zpráv, které jsou automaticky volány na základě typu přijímané zprávy.
2.  **Hrany (Edges)**: Ty definují cestu, kterou zprávy putují mezi executory. Hrany mohou mít podmínky, což umožňuje dynamické směrování informací přes workflow graf.
3.  **Workflow**: Tato komponenta orchestruje celý proces, řídí executory, hrany a celkový tok zpracování. Zajistí, že zprávy jsou zpracovány ve správném pořadí a vysílá události pro sledovatelnost.

*Diagram znázorňující základní komponenty workflow systému.*

Tato struktura umožňuje vytvářet robustní a škálovatelné aplikace pomocí základních vzorů jako jsou sekvenční řetězce, fan-out/fan-in pro paralelní zpracování a logiku přepínačů pro podmíněné toky.

## 3\. Praktické příklady a analýza kódu

Nyní si ukážeme, jak implementovat různé vzory workflow pomocí frameworku. Podíváme se na kód v Pythonu i .NET u každého příkladu.

### Příklad 1: Základní sekvenční workflow

Toto je nejjednodušší vzor, kde výstup jednoho agenta je přímo předán dalšímu. Náš scénář zahrnuje hotelového agenta `FrontDesk`, který poskytuje cestovní doporučení, a agenta `Concierge`, který je přezkoumá.

*Diagram základního workflow FrontDesk -\> Concierge.*

#### Pozadí scénáře

Cestovatel požádá o doporučení v Paříži.

1.  Agent `FrontDesk`, navržený pro stručnost, doporučí návštěvu muzea Louvre.
2.  Agent `Concierge`, který preferuje autentické zážitky, toto doporučení obdrží. Přezkoumá doporučení a dá zpětnou vazbu, navrhuje lokálnější, méně turistickou alternativu.

#### Analýza implementace v Pythonu

V Python příkladu nejprve definujeme a vytvoříme oba agenty, každý s konkrétními instrukcemi.

```python
# 01.python-agent-framework-workflow-ghmodel-basic.ipynb

# Definujte role a instrukce agenta
REVIEWER_NAME = "Concierge"
REVIEWER_INSTRUCTIONS = """
    You are an are hotel concierge who has opinions about providing the most local and authentic experiences for travelers...
    """

FRONTDESK_NAME = "FrontDesk"
FRONTDESK_INSTRUCTIONS = """
    You are a Front Desk Travel Agent with ten years of experience and are known for brevity...
    """

# Vytvořte instance agenta
reviewer_agent = chat_client.as_agent(
    instructions=(REVIEWER_INSTRUCTIONS),
    name=REVIEWER_NAME,
)

front_desk_agent = chat_client.as_agent(
    instructions=(FRONTDESK_INSTRUCTIONS),
    name=FRONTDESK_NAME,
)
```

Poté se používá `WorkflowBuilder` k sestavení grafu. Agent `front_desk_agent` je nastaven jako výchozí bod a je vytvořena hrana, která propojuje jeho výstup s agentem `reviewer_agent`.

```python
# 01.python-agent-framework-workflow-ghmodel-basic.ipynb

workflow = WorkflowBuilder(start_executor=front_desk_agent).add_edge(front_desk_agent, reviewer_agent).build()
```

Nakonec je workflow spuštěn s počátečním uživatelským požadavkem.

```python
# 01.python-agent-framework-workflow-ghmodel-basic.ipynb

result =''
# run spustí workflow; get_outputs() vrátí výsledek vykonavatele výstupu.
events = await workflow.run('I would like to go to Paris.')
outputs = events.get_outputs()
result = outputs[0].text if outputs else ''
```

#### Analýza implementace v .NET (C#)

Implementace v .NET sleduje velmi podobnou logiku. Nejprve jsou definovány konstanty pro jména a instrukce agentů.

```csharp
// 01.dotnet-agent-framework-workflow-ghmodel-basic.ipynb

const string ReviewerAgentName = "Concierge";
const string ReviewerAgentInstructions = @"
    You are an are hotel concierge who has opinions about providing the most local and authentic experiences for travelers...";

const string FrontDeskAgentName = "FrontDesk";
const string FrontDeskAgentInstructions = @"""
    You are a Front Desk Travel Agent with ten years of experience and are known for brevity...";
```

Agenti jsou vytvořeni pomocí `AzureOpenAIClient` (Responses API) a poté `WorkflowBuilder` definuje sekvenční tok přidáním hrany z `frontDeskAgent` na `reviewerAgent`.

```csharp
// 01.dotnet-agent-framework-workflow-ghmodel-basic.ipynb

// Create AIAgent instances
AIAgent reviewerAgent = azureClient.GetOpenAIResponseClient(deployment).CreateAIAgent(
    name:ReviewerAgentName,instructions:ReviewerAgentInstructions);
AIAgent frontDeskAgent  = azureClient.GetOpenAIResponseClient(deployment).CreateAIAgent(
    name:FrontDeskAgentName,instructions:FrontDeskAgentInstructions);

// Build the workflow
var workflow = new WorkflowBuilder(frontDeskAgent)
            .AddEdge(frontDeskAgent, reviewerAgent)
            .Build();
```

Workflow je pak spuštěno s uživatelskou zprávou a výsledky jsou streamovány zpět.

### Příklad 2: Více-krokové sekvenční workflow

Tento vzor rozšiřuje základní sekvenci o více agentů. Je ideální pro procesy vyžadující několik fází zpřesnění nebo transformace.

#### Pozadí scénáře

Uživateli je poskytnut obrázek obývacího pokoje a požádá o cenovou nabídku na nábytek.

1.  **Prodejní agent**: Identifikuje nábytkové položky na obrázku a vytvoří seznam.
2.  **Cenový agent**: Bere seznam položek a poskytuje detailní rozpis cen, včetně rozpočtových, středních a prémiových možností.
3.  **Agent nabídek**: Přijímá ceník a formátuje jej do formální nabídky v Markdown.

*Diagram workflow Sales -\> Price -\> Quote.*

#### Analýza implementace v Pythonu

Jsou definováni tři agenti, každý se specializovanou rolí. Workflow je vytvořen dotazy `add_edge` k vytvoření řetězce: `sales_agent` -\> `price_agent` -\> `quote_agent`.

```python
# 02.python-agent-framework-workflow-ghmodel-sequential.ipynb

# Vytvořte tři specializované agenty
sales_agent = chat_client.as_agent(...)
price_agent = chat_client.as_agent(...)
quote_agent = chat_client.as_agent(...)

# Sestavte sekvenční pracovní postup
workflow = WorkflowBuilder(start_executor=sales_agent).add_edge(sales_agent, price_agent).add_edge(price_agent, quote_agent).build()
```

Vstupem je `ChatMessage`, které obsahuje text i URI obrázku. Framework se stará o předávání výstupu každého agenta dalšímu v sekvenci, až je vytvořena konečná nabídka.

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

#### Analýza implementace v .NET (C#)

Příklad v .NET odpovídá verzi pro Python. Vytvořeni jsou tři agenti (`salesagent`, `priceagent`, `quoteagent`). `WorkflowBuilder` je propojí sekvenčně.

```csharp
// 02.dotnet-agent-framework-workflow-ghmodel-sequential.ipynb

// Create agent instances
AIAgent salesagent = azureClient.GetOpenAIResponseClient(deployment).CreateAIAgent(...);
AIAgent priceagent  = azureClient.GetOpenAIResponseClient(deployment).CreateAIAgent(...);
AIAgent quoteagent = azureClient.GetOpenAIResponseClient(deployment).CreateAIAgent(...);

// Build the workflow by adding edges sequentially
var workflow = new WorkflowBuilder(salesagent)
            .AddEdge(salesagent,priceagent)
            .AddEdge(priceagent, quoteagent)
            .Build();
```

Uživatelská zpráva je sestavena s daty obrázku (v bajtech) i textovým promptem. Metoda `InProcessExecution.StreamAsync` spustí workflow a konečný výstup je zachycen ze streamu.

### Příklad 3: Současné workflow

Tento vzor se používá, kdy úkoly mohou být prováděny současně, aby se ušetřil čas. Zahrnuje "fan-out" k více agentům a "fan-in" pro agregaci výsledků.

#### Pozadí scénáře

Uživatel požádá o naplánování cesty do Seattlu.

1.  **Dispečer (Fan-Out)**: Uživatelský požadavek je odeslán současně dvěma agentům.
2.  **Výzkumný agent**: Zkoumá atrakce, počasí a klíčová rizika pro cestu do Seattlu v prosinci.
3.  **Plánovací agent**: Samostatně vytváří detailní denní cestovní itinerář.
4.  **Agregátor (Fan-In)**: Výstupy výzkumníka i plánovače jsou shromážděny a prezentovány společně jako konečný výsledek.

*Diagram současného workflow Výzkumníka a Plánovače.*

#### Analýza implementace v Pythonu

`ConcurrentBuilder` usnadňuje vytvoření tohoto vzoru. Stačí vyjmenovat účastnící agenty a builder automaticky vytvoří potřebnou logiku fan-out a fan-in.

```python
# 03.python-agent-framework-workflow-ghmodel-concurrent.ipynb

research_agent = chat_client.as_agent(name="Researcher-Agent", ...)
plan_agent = chat_client.as_agent(name="Plan-Agent", ...)

# ConcurrentBuilder řeší logiku rozvětvování a slučování
workflow = ConcurrentBuilder().participants([research_agent, plan_agent]).build()

# Spustit workflow
events = await workflow.run("Plan a trip to Seattle in December")
```

Framework zajišťuje, že `research_agent` a `plan_agent` běží paralelně a jejich konečné výstupy jsou seskupeny do seznamu.

#### Analýza implementace v .NET (C#)

V .NET je potřeba explicitnější definice. Vytváří se vlastní executory (`ConcurrentStartExecutor` a `ConcurrentAggregationExecutor`), které řídí logiku fan-out a fan-in.

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

`WorkflowBuilder` pak pomocí `AddFanOutEdge` a `AddFanInEdge` sestavuje graf s těmito vlastními executory a agenty.

```csharp
// 03.dotnet-agent-framework-workflow-ghmodel-concurrent.ipynb

var workflow = new WorkflowBuilder(startExecutor)
            .AddFanOutEdge(startExecutor, targets: [researcherAgent, plannerAgent])
            .AddFanInEdge(aggregationExecutor, sources: [researcherAgent, plannerAgent])
            .WithOutputFrom(aggregationExecutor)
            .Build();
```

### Příklad 4: Podmíněné workflow

Podmíněné workflow zavádí větvení logiky, které umožňuje systému zvolit různé cesty na základě mezivýsledků.

#### Pozadí scénáře

Tento workflow automatizuje tvorbu a publikaci technického tutoriálu.

1.  **Evangelist-Agent**: Napiše návrh tutoriálu na základě dané osnovy a URL.
2.  **Recenzent obsahu**: Přezkoumá návrh. Kontroluje, zda počet slov přesahuje 200 slov.
3.  **Podmíněné větvení**:
      * **Pokud schváleno (`Ano`)**: Workflow pokračuje k agentovi vydavatele.
      * **Pokud zamítnuto (`Ne`)**: Workflow se zastaví a vypíše důvod zamítnutí.
4.  **Agent vydavatel**: Pokud je návrh schválen, tento agent uloží obsah do Markdown souboru.

#### Analýza implementace v Pythonu

Tento příklad používá vlastní funkci `select_targets` k implementaci podmíněné logiky. Tato funkce je předána do `add_multi_selection_edge_group` a řídí workflow na základě pole `review_result` z výstupu recenzenta.

```python
# 04.python-agent-framework-workflow-aifoundry-condition.ipynb

# Tato funkce určuje další krok na základě výsledku hodnocení
def select_targets(review: ReviewResult, target_ids: list[str]) -> list[str]:
    handle_review_id, save_draft_id = target_ids
    if review.review_result == "Yes":
        # Pokud je schváleno, pokračujte k vykonavateli 'save_draft'
        return [save_draft_id]
    else:
        # Pokud je zamítnuto, pokračujte k vykonavateli 'handle_review' pro nahlášení neúspěchu
        return [handle_review_id]

# Stavitel pracovního postupu používá funkci výběru pro směrování
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

Vlastní executory jako `to_reviewer_result` slouží k parsování JSON výstupu agentů a jeho převodu na silně typované objekty, které může výběrová funkce prozkoumat.

#### Analýza implementace v .NET (C#)

Verze v .NET používá podobný přístup s funkcí podmínky. Definován je `Func<object?, bool>`, která kontroluje vlastnost `Result` objektu `ReviewResult`.

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

Parametr `condition` metody `AddEdge` umožňuje `WorkflowBuilder` vytvořit větvenou cestu. Workflow následuje hranu k `publishExecutor` pouze pokud podmínka `GetCondition(expectedResult: "Yes")` vrátí true. Jinak následuje cestu k `sendReviewerExecutor`.

## Závěr

Microsoft Agent Framework Workflow poskytuje robustní a flexibilní základ pro orchestraci složitých multi-agentních systémů. Využitím grafové architektury a základních komponent mohou vývojáři navrhovat a implementovat sofistikované workflow jak v Pythonu, tak v .NET. Ať vaše aplikace vyžaduje jednoduché sekvenční zpracování, paralelní vykonávání nebo dynamickou podmíněnou logiku, framework nabízí nástroje k vytváření výkonných, škálovatelných a typově bezpečných AI řešení.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Prohlášení o omezení odpovědnosti**:
Tento dokument byl přeložen pomocí AI překladatelské služby [Co-op Translator](https://github.com/Azure/co-op-translator). Přestože usilujeme o co největší přesnost, mějte prosím na paměti, že automatizované překlady mohou obsahovat chyby nebo nepřesnosti. Originální dokument v jeho mateřském jazyce by měl být považován za autoritativní zdroj. Pro kritické informace se doporučuje profesionální lidský překlad. Nejsme odpovědní za jakékoli nedorozumění nebo nesprávné interpretace vzniklé použitím tohoto překladu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->