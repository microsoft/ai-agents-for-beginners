# Vytváranie aplikácií s viacerými agentmi pomocou Microsoft Agent Framework Workflow

Tento návod vás prevedie pochopením a vytváraním aplikácií s viacerými agentmi pomocou Microsoft Agent Framework. Preskúmame základné koncepty systémov s viacerými agentmi, ponoríme sa do architektúry komponentu Workflow v rámci frameworku a prejdeme si praktické príklady v Pythone a .NET pre rôzne vzory workflowu.

## 1\. Pochopenie systémov s viacerými agentmi

AI Agent je systém, ktorý presahuje schopnosti štandardného veľkého jazykového modelu (LLM). Dokáže vnímať svoje prostredie, robiť rozhodnutia a vykonávať akcie na dosiahnutie konkrétnych cieľov. Systém s viacerými agentmi zahŕňa niekoľko takýchto agentov, ktorí spolupracujú na riešení problému, ktorý by bol pre jedného agenta náročný alebo nemožný.

### Bežné scenáre aplikácií

  * **Riešenie zložitých problémov**: Rozdelenie veľkej úlohy (napr. plánovanie firemného podujatia) na menšie podúlohy, ktoré riešia špecializovaní agenti (napr. agent pre rozpočet, agent pre logistiku, agent pre marketing).
  * **Virtuálni asistenti**: Primárny asistent deleguje úlohy, ako je plánovanie, výskum a rezervácie, na iných špecializovaných agentov.
  * **Automatizované vytváranie obsahu**: Workflow, kde jeden agent vytvorí návrh obsahu, druhý ho skontroluje z hľadiska presnosti a tónu a tretí ho publikuje.

### Vzory systémov s viacerými agentmi

Systémy s viacerými agentmi môžu byť organizované podľa rôznych vzorov, ktoré určujú, ako spolu komunikujú:

  * **Sekvenčné**: Agenti pracujú v preddefinovanom poradí, podobne ako na montážnej linke. Výstup jedného agenta sa stáva vstupom pre ďalšieho.
  * **Súbežné**: Agenti pracujú paralelne na rôznych častiach úlohy a ich výsledky sa na konci agregujú.
  * **Podmienené**: Workflow nasleduje rôzne cesty na základe výstupu agenta, podobne ako príkaz if-then-else.

## 2\. Architektúra Workflow v Microsoft Agent Framework

Workflow systém Agent Framework je pokročilý orchestrátor určený na správu zložitých interakcií medzi viacerými agentmi. Je postavený na architektúre založenej na grafoch, ktorá využíva [Pregel-style model vykonávania](https://kowshik.github.io/JPregel/pregel_paper.pdf), kde spracovanie prebieha v synchronizovaných krokoch nazývaných "supersteps."

### Základné komponenty

Architektúra sa skladá z troch hlavných častí:

1.  **Executors**: Základné jednotky spracovania. V našich príkladoch je `Agent` typom executor. Každý executor môže mať viacero spracovateľov správ, ktoré sa automaticky vyvolajú na základe typu prijatej správy.
2.  **Edges**: Definujú cestu, ktorou správy prechádzajú medzi executormi. Edges môžu mať podmienky, ktoré umožňujú dynamické smerovanie informácií cez graf workflowu.
3.  **Workflow**: Tento komponent orchestruje celý proces, spravuje executory, edges a celkový tok vykonávania. Zabezpečuje, že správy sú spracované v správnom poradí a streamuje udalosti pre pozorovateľnosť.

*Diagram znázorňujúci základné komponenty systému workflow.*

Táto štruktúra umožňuje vytvárať robustné a škálovateľné aplikácie pomocou základných vzorov, ako sú sekvenčné reťazce, fan-out/fan-in pre paralelné spracovanie a switch-case logika pre podmienené toky.

## 3\. Praktické príklady a analýza kódu

Teraz sa pozrime, ako implementovať rôzne vzory workflowu pomocou frameworku. Pre každý príklad si ukážeme kód v Pythone aj .NET.

### Prípad 1: Základný sekvenčný workflow

Toto je najjednoduchší vzor, kde výstup jedného agenta je priamo odovzdaný ďalšiemu. Naša situácia zahŕňa hotelového agenta `FrontDesk`, ktorý poskytuje odporúčanie na cestovanie, ktoré následne preskúma agent `Concierge`.

*Diagram základného workflowu FrontDesk -\> Concierge.*

#### Pozadie scenára

Cestovateľ žiada odporúčanie v Paríži.

1.  Agent `FrontDesk`, navrhnutý na stručnosť, odporúča návštevu Louvru.
2.  Agent `Concierge`, ktorý uprednostňuje autentické zážitky, prijíma toto odporúčanie. Preskúma ho a poskytne spätnú väzbu, navrhujúc miestnu, menej turistickú alternatívu.

#### Analýza implementácie v Pythone

V príklade v Pythone najprv definujeme a vytvoríme dvoch agentov, každý s konkrétnymi pokynmi.

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

Potom sa pomocou `WorkflowBuilder` zostaví graf. `front_desk_agent` je nastavený ako východiskový bod a vytvorí sa edge na prepojenie jeho výstupu s `reviewer_agent`.

```python
# 01.python-agent-framework-workflow-ghmodel-basic.ipynb

workflow = WorkflowBuilder().set_start_executor(front_desk_agent).add_edge(front_desk_agent, reviewer_agent).build()
```

Nakoniec sa workflow spustí s počiatočným vstupom od používateľa.

```python
# 01.python-agent-framework-workflow-ghmodel-basic.ipynb

result =''
# The run_stream method executes the workflow and streams events.
async for event in workflow.run_stream('I would like to go to Paris.'):
    if isinstance(event, WorkflowEvent):
        result += str(event.data)
```

#### Analýza implementácie v .NET (C\#)

Implementácia v .NET nasleduje veľmi podobnú logiku. Najprv sa definujú konštanty pre názvy agentov a ich pokyny.

```csharp
// 01.dotnet-agent-framework-workflow-ghmodel-basic.ipynb

const string ReviewerAgentName = "Concierge";
const string ReviewerAgentInstructions = @"
    You are an are hotel concierge who has opinions about providing the most local and authentic experiences for travelers...";

const string FrontDeskAgentName = "FrontDesk";
const string FrontDeskAgentInstructions = @"""
    You are a Front Desk Travel Agent with ten years of experience and are known for brevity...";
```

Agenti sa vytvoria pomocou `OpenAIClient` a potom `WorkflowBuilder` definuje sekvenčný tok pridaním edge od `frontDeskAgent` k `reviewerAgent`.

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

Workflow sa potom spustí s používateľovou správou a výsledky sa streamujú späť.

### Prípad 2: Viacstupňový sekvenčný workflow

Tento vzor rozširuje základnú sekvenciu o viac agentov. Je ideálny pre procesy, ktoré vyžadujú viacero fáz zdokonaľovania alebo transformácie.

#### Pozadie scenára

Používateľ poskytne obrázok obývačky a žiada cenovú ponuku na nábytok.

1.  **Sales-Agent**: Identifikuje nábytok na obrázku a vytvorí zoznam.
2.  **Price-Agent**: Vezme zoznam položiek a poskytne podrobný cenový rozpis vrátane možností rozpočtu, strednej triedy a prémiových možností.
3.  **Quote-Agent**: Prijme ocenený zoznam a naformátuje ho do formálneho dokumentu cenovej ponuky v Markdown.

*Diagram workflowu Sales -\> Price -\> Quote.*

#### Analýza implementácie v Pythone

Definujú sa traja agenti, každý so špecializovanou úlohou. Workflow sa zostaví pomocou `add_edge` na vytvorenie reťazca: `sales_agent` -\> `price_agent` -\> `quote_agent`.

```python
# 02.python-agent-framework-workflow-ghmodel-sequential.ipynb

# Create three specialized agents
sales_agent = chat_client.create_agent(...)
price_agent = chat_client.create_agent(...)
quote_agent = chat_client.create_agent(...)

# Build the sequential workflow
workflow = WorkflowBuilder().set_start_executor(sales_agent).add_edge(sales_agent, price_agent).add_edge(price_agent, quote_agent).build()
```

Vstup je `ChatMessage`, ktorý obsahuje text aj URI obrázka. Framework zabezpečí odovzdanie výstupu každého agenta ďalšiemu v sekvencii, až kým sa nevygeneruje finálna ponuka.

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

#### Analýza implementácie v .NET (C\#)

Príklad v .NET zrkadlí verziu v Pythone. Vytvoria sa traja agenti (`salesagent`, `priceagent`, `quoteagent`). `WorkflowBuilder` ich prepojí sekvenčne.

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

Používateľova správa sa zostaví s údajmi o obrázku (ako bajty) a textovým promptom. Metóda `InProcessExecution.StreamAsync` spustí workflow a finálny výstup sa zachytí zo streamu.

### Prípad 3: Súbežný workflow

Tento vzor sa používa, keď je možné úlohy vykonávať súčasne na úsporu času. Zahŕňa "fan-out" na viacerých agentov a "fan-in" na agregáciu výsledkov.

#### Pozadie scenára

Používateľ žiada naplánovať výlet do Seattlu.

1.  **Dispatcher (Fan-Out)**: Požiadavka používateľa sa naraz odošle dvom agentom.
2.  **Researcher-Agent**: Skúma atrakcie, počasie a kľúčové faktory pre výlet do Seattlu v decembri.
3.  **Plan-Agent**: Nezávisle vytvorí podrobný denný itinerár cesty.
4.  **Aggregator (Fan-In)**: Výstupy od výskumníka a plánovača sa zhromaždia a prezentujú spolu ako finálny výsledok.

*Diagram súbežného workflowu Researcher a Planner.*

#### Analýza implementácie v Pythone

`ConcurrentBuilder` zjednodušuje vytvorenie tohto vzoru. Stačí uviesť zúčastnených agentov a builder automaticky vytvorí potrebnú logiku fan-out a fan-in.

```python
# 03.python-agent-framework-workflow-ghmodel-concurrent.ipynb

research_agent = chat_client.create_agent(name="Researcher-Agent", ...)
plan_agent = chat_client.create_agent(name="Plan-Agent", ...)

# ConcurrentBuilder handles the fan-out/fan-in logic
workflow = ConcurrentBuilder().participants([research_agent, plan_agent]).build()

# Run the workflow
events = await workflow.run("Plan a trip to Seattle in December")
```

Framework zabezpečí, že `research_agent` a `plan_agent` vykonajú úlohy paralelne a ich finálne výstupy sa zhromaždia do zoznamu.

#### Analýza implementácie v .NET (C\#)

V .NET si tento vzor vyžaduje explicitnejšiu definíciu. Vytvoria sa vlastné executory (`ConcurrentStartExecutor` a `ConcurrentAggregationExecutor`) na spracovanie logiky fan-out a fan-in.

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

`WorkflowBuilder` potom použije `AddFanOutEdge` a `AddFanInEdge` na zostavenie grafu s týmito vlastnými executormi a agentmi.

```csharp
// 03.dotnet-agent-framework-workflow-ghmodel-concurrent.ipynb

var workflow = new WorkflowBuilder(startExecutor)
            .AddFanOutEdge(startExecutor, targets: [researcherAgent, plannerAgent])
            .AddFanInEdge(aggregationExecutor, sources: [researcherAgent, plannerAgent])
            .WithOutputFrom(aggregationExecutor)
            .Build();
```

### Prípad 4: Podmienený workflow

Podmienené workflowy zavádzajú vetvenú logiku, ktorá umožňuje systému zvoliť rôzne cesty na základe medzivýsledkov.

#### Pozadie scenára

Tento workflow automatizuje vytvorenie a publikovanie technického návodu.

1.  **Evangelist-Agent**: Napíše návrh návodu na základe daného obrysu a URL.
2.  **ContentReviewer-Agent**: Skontroluje návrh. Overí, či má text viac ako 200 slov.
3.  **Podmienená vetva**:
      * **Ak schválené (`Áno`)**: Workflow pokračuje k `Publisher-Agent`.
      * **Ak zamietnuté (`Nie`)**: Workflow sa zastaví a výstupom je dôvod zamietnutia.
4.  **Publisher-Agent**: Ak je návrh schválený, tento agent uloží obsah do Markdown súboru.

#### Analýza implementácie v Pythone

Tento príklad používa vlastnú funkciu `select_targets` na implementáciu podmienenej logiky. Táto funkcia sa odovzdá `add_multi_selection_edge_group` a smeruje workflow na základe poľa `review_result` z výstupu recenzenta.

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

Vlastné executory, ako `to_reviewer_result`, sa používajú na analýzu JSON výstupu od agentov a jeho konverziu na silne typované objekty, ktoré môže funkcia výberu preskúmať.

#### Analýza implementácie v .NET (C\#)

Verzia v .NET používa podobný prístup s funkciou podmienky. Definuje sa `Func<object?, bool>` na kontrolu vlastnosti `Result` objektu `ReviewResult`.

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

Parameter `condition` metódy `AddEdge` umožňuje `WorkflowBuilder` vytvoriť vetvenú cestu. Workflow bude nasledovať edge k `publishExecutor` iba vtedy, ak podmienka `GetCondition(expectedResult: "Yes")` vráti true. Inak nasleduje cestu k `sendReviewerExecutor`.

## Záver

Microsoft Agent Framework Workflow poskytuje robustný a flexibilný základ na orchestráciu zložitých systémov s viacerými agentmi. Využitím jeho architektúry založenej na grafoch a základných komponentov môžu vývojári navrhovať a implementovať sofistikované workflowy v Pythone aj .NET. Či už vaša aplikácia vyžaduje jednoduché sekvenčné spracovanie, paralelné vykonávanie alebo dynamickú podmienenú logiku, framework ponúka nástroje na vytváranie výkonných, škálovateľných a typovo bezpečných AI riešení.

---

**Upozornenie**:  
Tento dokument bol preložený pomocou služby AI prekladu [Co-op Translator](https://github.com/Azure/co-op-translator). Hoci sa snažíme o presnosť, upozorňujeme, že automatizované preklady môžu obsahovať chyby alebo nepresnosti. Pôvodný dokument v jeho rodnom jazyku by mal byť považovaný za autoritatívny zdroj. Pre kritické informácie sa odporúča profesionálny ľudský preklad. Nenesieme zodpovednosť za akékoľvek nedorozumenia alebo nesprávne interpretácie vyplývajúce z použitia tohto prekladu.