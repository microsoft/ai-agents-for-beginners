# Vytváření aplikací s více agenty pomocí Microsoft Agent Framework Workflow

Tento návod vás provede porozuměním a vytvářením aplikací s více agenty pomocí Microsoft Agent Framework. Prozkoumáme základní koncepty systémů s více agenty, ponoříme se do architektury komponenty Workflow tohoto frameworku a projdeme si praktické příklady v Pythonu a .NET pro různé vzory workflow.

## 1\. Porozumění systémům s více agenty

AI agent je systém, který přesahuje schopnosti standardního modelu velkého jazykového modelu (LLM). Dokáže vnímat své prostředí, rozhodovat se a podnikat kroky k dosažení konkrétních cílů. Systém s více agenty zahrnuje několik těchto agentů, kteří spolupracují na řešení problému, který by byl pro jednoho agenta obtížný nebo nemožný.

### Běžné scénáře použití

  * **Řešení složitých problémů**: Rozdělení velkého úkolu (např. plánování celofiremní akce) na menší podúkoly, které řeší specializovaní agenti (např. agent pro rozpočet, agent pro logistiku, agent pro marketing).
  * **Virtuální asistenti**: Hlavní asistent deleguje úkoly, jako je plánování, výzkum a rezervace, na jiné specializované agenty.
  * **Automatizovaná tvorba obsahu**: Workflow, kde jeden agent vytváří návrh obsahu, druhý kontroluje jeho přesnost a tón, a třetí ho publikuje.

### Vzory systémů s více agenty

Systémy s více agenty mohou být organizovány podle různých vzorů, které určují, jak spolu komunikují:

  * **Sekvenční**: Agenti pracují v předem definovaném pořadí, podobně jako na montážní lince. Výstup jednoho agenta se stává vstupem pro dalšího.
  * **Paralelní**: Agenti pracují současně na různých částech úkolu a jejich výsledky se na konci agregují.
  * **Podmíněné**: Workflow následuje různé cesty na základě výstupu agenta, podobně jako podmíněné příkazy typu if-then-else.

## 2\. Architektura Workflow v Microsoft Agent Framework

Workflow systém Agent Framework je pokročilý orchestrátor navržený pro správu složitých interakcí mezi více agenty. Je postaven na architektuře založené na grafech, která využívá [Pregel-style model zpracování](https://kowshik.github.io/JPregel/pregel_paper.pdf), kde zpracování probíhá v synchronizovaných krocích nazývaných "superkroky".

### Základní komponenty

Architektura se skládá ze tří hlavních částí:

1.  **Executors**: Základní jednotky zpracování. V našich příkladech je `Agent` typem executor. Každý executor může mít více handlerů zpráv, které se automaticky spouštějí na základě typu přijaté zprávy.
2.  **Edges**: Definují cestu, kterou zprávy putují mezi executory. Hrany mohou mít podmínky, což umožňuje dynamické směrování informací skrz graf workflow.
3.  **Workflow**: Tato komponenta orchestruje celý proces, spravuje executory, hrany a celkový tok zpracování. Zajišťuje, že zprávy jsou zpracovány ve správném pořadí, a streamuje události pro sledování.

*Diagram znázorňující základní komponenty systému workflow.*

Tato struktura umožňuje vytvářet robustní a škálovatelné aplikace pomocí základních vzorů, jako jsou sekvenční řetězce, fan-out/fan-in pro paralelní zpracování a switch-case logika pro podmíněné toky.

## 3\. Praktické příklady a analýza kódu

Nyní se podíváme, jak implementovat různé vzory workflow pomocí frameworku. Pro každý příklad si ukážeme kód v Pythonu i .NET.

### Případ 1: Základní sekvenční workflow

Toto je nejjednodušší vzor, kde výstup jednoho agenta je přímo předán dalšímu. Náš scénář zahrnuje hotelového agenta `FrontDesk`, který poskytuje doporučení na cestování, a agenta `Concierge`, který toto doporučení zhodnotí.

*Diagram základního workflow FrontDesk -\> Concierge.*

#### Pozadí scénáře

Cestovatel žádá o doporučení v Paříži.

1.  Agent `FrontDesk`, navržený pro stručnost, doporučuje návštěvu Louvru.
2.  Agent `Concierge`, který upřednostňuje autentické zážitky, toto doporučení obdrží. Zhodnotí návrh a poskytne zpětnou vazbu, navrhující více lokální, méně turistickou alternativu.

#### Analýza implementace v Pythonu

V Pythonu nejprve definujeme a vytvoříme dva agenty, každý s konkrétními instrukcemi.

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

Poté použijeme `WorkflowBuilder` k vytvoření grafu. `front_desk_agent` je nastaven jako výchozí bod a je vytvořena hrana, která propojuje jeho výstup s `reviewer_agent`.

```python
# 01.python-agent-framework-workflow-ghmodel-basic.ipynb

workflow = WorkflowBuilder().set_start_executor(front_desk_agent).add_edge(front_desk_agent, reviewer_agent).build()
```

Nakonec je workflow spuštěn s počátečním uživatelským dotazem.

```python
# 01.python-agent-framework-workflow-ghmodel-basic.ipynb

result =''
# The run_stream method executes the workflow and streams events.
async for event in workflow.run_stream('I would like to go to Paris.'):
    if isinstance(event, WorkflowEvent):
        result += str(event.data)
```

#### Analýza implementace v .NET (C\#)

Implementace v .NET sleduje velmi podobnou logiku. Nejprve jsou definovány konstanty pro názvy agentů a jejich instrukce.

```csharp
// 01.dotnet-agent-framework-workflow-ghmodel-basic.ipynb

const string ReviewerAgentName = "Concierge";
const string ReviewerAgentInstructions = @"
    You are an are hotel concierge who has opinions about providing the most local and authentic experiences for travelers...";

const string FrontDeskAgentName = "FrontDesk";
const string FrontDeskAgentInstructions = @"""
    You are a Front Desk Travel Agent with ten years of experience and are known for brevity...";
```

Agenti jsou vytvořeni pomocí `OpenAIClient` a poté `WorkflowBuilder` definuje sekvenční tok přidáním hrany z `frontDeskAgent` na `reviewerAgent`.

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

Workflow je poté spuštěn s uživatelskou zprávou a výsledky jsou streamovány zpět.

### Případ 2: Vícekrokový sekvenční workflow

Tento vzor rozšiřuje základní sekvenci o více agentů. Je ideální pro procesy, které vyžadují více fází zdokonalení nebo transformace.

#### Pozadí scénáře

Uživatel poskytne obrázek obývacího pokoje a žádá o cenovou nabídku na nábytek.

1.  **Sales-Agent**: Identifikuje položky nábytku na obrázku a vytvoří seznam.
2.  **Price-Agent**: Vezme seznam položek a poskytne podrobný rozpis cen, včetně možností rozpočtu, střední třídy a prémiových variant.
3.  **Quote-Agent**: Obdrží oceněný seznam a formátuje ho do formální nabídky v Markdownu.

*Diagram workflow Sales -\> Price -\> Quote.*

#### Analýza implementace v Pythonu

Jsou definováni tři agenti, každý se specializovanou rolí. Workflow je vytvořeno pomocí `add_edge` k vytvoření řetězce: `sales_agent` -\> `price_agent` -\> `quote_agent`.

```python
# 02.python-agent-framework-workflow-ghmodel-sequential.ipynb

# Create three specialized agents
sales_agent = chat_client.create_agent(...)
price_agent = chat_client.create_agent(...)
quote_agent = chat_client.create_agent(...)

# Build the sequential workflow
workflow = WorkflowBuilder().set_start_executor(sales_agent).add_edge(sales_agent, price_agent).add_edge(price_agent, quote_agent).build()
```

Vstup je `ChatMessage`, který obsahuje text i URI obrázku. Framework zajišťuje předání výstupu každého agenta dalšímu v sekvenci, dokud není vytvořena finální nabídka.

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

#### Analýza implementace v .NET (C\#)

Příklad v .NET zrcadlí verzi v Pythonu. Jsou vytvořeni tři agenti (`salesagent`, `priceagent`, `quoteagent`). `WorkflowBuilder` je propojuje sekvenčně.

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

Uživatelská zpráva je vytvořena s daty obrázku (jako bajty) a textovým dotazem. Metoda `InProcessExecution.StreamAsync` spustí workflow a finální výstup je zachycen ze streamu.

### Případ 3: Paralelní workflow

Tento vzor se používá, když lze úkoly provádět současně, aby se ušetřil čas. Zahrnuje "fan-out" na více agentů a "fan-in" pro agregaci výsledků.

#### Pozadí scénáře

Uživatel žádá o plánování výletu do Seattlu.

1.  **Dispatcher (Fan-Out)**: Uživatelský požadavek je současně odeslán dvěma agentům.
2.  **Researcher-Agent**: Zkoumá atrakce, počasí a klíčové aspekty výletu do Seattlu v prosinci.
3.  **Plan-Agent**: Nezávisle vytváří podrobný denní itinerář.
4.  **Aggregator (Fan-In)**: Výstupy od výzkumníka a plánovače jsou shromážděny a prezentovány jako finální výsledek.

*Diagram paralelního workflow Researcher a Planner.*

#### Analýza implementace v Pythonu

`ConcurrentBuilder` zjednodušuje vytvoření tohoto vzoru. Stačí uvést zúčastněné agenty a builder automaticky vytvoří potřebnou logiku fan-out a fan-in.

```python
# 03.python-agent-framework-workflow-ghmodel-concurrent.ipynb

research_agent = chat_client.create_agent(name="Researcher-Agent", ...)
plan_agent = chat_client.create_agent(name="Plan-Agent", ...)

# ConcurrentBuilder handles the fan-out/fan-in logic
workflow = ConcurrentBuilder().participants([research_agent, plan_agent]).build()

# Run the workflow
events = await workflow.run("Plan a trip to Seattle in December")
```

Framework zajišťuje, že `research_agent` a `plan_agent` pracují paralelně a jejich finální výstupy jsou shromážděny do seznamu.

#### Analýza implementace v .NET (C\#)

V .NET tento vzor vyžaduje explicitnější definici. Vytvářejí se vlastní executory (`ConcurrentStartExecutor` a `ConcurrentAggregationExecutor`) pro zpracování logiky fan-out a fan-in.

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

`WorkflowBuilder` poté používá `AddFanOutEdge` a `AddFanInEdge` k vytvoření grafu s těmito vlastními executory a agenty.

```csharp
// 03.dotnet-agent-framework-workflow-ghmodel-concurrent.ipynb

var workflow = new WorkflowBuilder(startExecutor)
            .AddFanOutEdge(startExecutor, targets: [researcherAgent, plannerAgent])
            .AddFanInEdge(aggregationExecutor, sources: [researcherAgent, plannerAgent])
            .WithOutputFrom(aggregationExecutor)
            .Build();
```

### Případ 4: Podmíněné workflow

Podmíněné workflow zavádí větvení logiky, což umožňuje systému zvolit různé cesty na základě mezivýsledků.

#### Pozadí scénáře

Tento workflow automatizuje tvorbu a publikaci technického tutoriálu.

1.  **Evangelist-Agent**: Napíše návrh tutoriálu na základě dané osnovy a URL.
2.  **ContentReviewer-Agent**: Zkontroluje návrh. Zjišťuje, zda počet slov přesahuje 200.
3.  **Podmíněná větev**:
      * **Pokud schváleno (`Ano`)**: Workflow pokračuje k `Publisher-Agent`.
      * **Pokud zamítnuto (`Ne`)**: Workflow se zastaví a výstupem je důvod zamítnutí.
4.  **Publisher-Agent**: Pokud je návrh schválen, tento agent uloží obsah do Markdown souboru.

#### Analýza implementace v Pythonu

Tento příklad používá vlastní funkci `select_targets` k implementaci podmíněné logiky. Tato funkce je předána `add_multi_selection_edge_group` a řídí workflow na základě pole `review_result` z výstupu recenzenta.

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

Vlastní executory jako `to_reviewer_result` se používají k analýze JSON výstupu od agentů a jeho převodu na silně typované objekty, které může inspekční funkce zkoumat.

#### Analýza implementace v .NET (C\#)

Verze v .NET používá podobný přístup s podmínkovou funkcí. Je definována `Func<object?, bool>` pro kontrolu vlastnosti `Result` objektu `ReviewResult`.

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

Parametr `condition` metody `AddEdge` umožňuje `WorkflowBuilder` vytvořit větvenou cestu. Workflow bude následovat hranu k `publishExecutor` pouze pokud podmínka `GetCondition(expectedResult: "Yes")` vrátí true. Jinak následuje cestu k `sendReviewerExecutor`.

## Závěr

Microsoft Agent Framework Workflow poskytuje robustní a flexibilní základ pro orchestraci složitých systémů s více agenty. Využitím jeho architektury založené na grafech a základních komponent mohou vývojáři navrhovat a implementovat sofistikované workflow v Pythonu i .NET. Ať už vaše aplikace vyžaduje jednoduché sekvenční zpracování, paralelní provádění nebo dynamickou podmíněnou logiku, framework nabízí nástroje pro vytváření výkonných, škálovatelných a typově bezpečných řešení poháněných AI.

---

**Upozornění**:  
Tento dokument byl přeložen pomocí služby pro automatický překlad [Co-op Translator](https://github.com/Azure/co-op-translator). I když se snažíme o co největší přesnost, mějte prosím na paměti, že automatické překlady mohou obsahovat chyby nebo nepřesnosti. Za závazný zdroj by měl být považován původní dokument v jeho původním jazyce. Pro důležité informace doporučujeme profesionální lidský překlad. Neodpovídáme za žádná nedorozumění nebo nesprávné výklady vyplývající z použití tohoto překladu.