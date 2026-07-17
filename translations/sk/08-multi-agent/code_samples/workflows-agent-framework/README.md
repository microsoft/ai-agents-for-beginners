# Tvorba viacagentových aplikácií s Microsoft Agent Framework Workflow

Tento tutoriál vás prevedie pochopením a tvorbou viacagentových aplikácií pomocou Microsoft Agent Framework. Preskúmame základné koncepty viacagentových systémov, ponoríme sa do architektúry komponentu Workflow tohto frameworku a prejdeme praktické príklady v Pythone aj .NET pre rôzne vzory workflow.

## 1\. Pochopenie viacagentových systémov

AI Agent je systém, ktorý presahuje schopnosti štandardného veľkého jazykového modelu (LLM). Môže vnímať svoje prostredie, robiť rozhodnutia a vykonávať akcie na dosiahnutie konkrétnych cieľov. Viacagentový systém zahŕňa niekoľko takýchto agentov spolupracujúcich na riešení problému, ktorý by bolo ťažké alebo nemožné zvládnuť len jedným agentom.

### Bežné scenáre použitia

  * **Riešenie zložitých problémov**: Rozdelenie veľkej úlohy (napr. plánovanie celopodnikovej udalosti) na menšie podúlohy riešené špecializovanými agentmi (napr. agent rozpočtu, agent logistiky, marketingový agent).
  * **Virtuálni asistenti**: Hlavný asistent agent deleguje úlohy ako plánovanie, výskum a rezervácie iným špecializovaným agentom.
  * **Automatizovaná tvorba obsahu**: Workflow, kde jeden agent vytvára návrh obsahu, ďalší ho kontroluje na presnosť a tón a tretí ho publikuje.

### Viacagentové vzory

Viacagentové systémy môžu byť organizované v rôznych vzoroch, ktoré určujú, ako spolu komunikujú:

  * **Sekvenčný**: Agenti pracujú v preddefinovanom poradí, ako montážna linka. Výstup jedného agenta sa stáva vstupom ďalšieho.
  * **Súbežný**: Agenti pracujú paralelne na rôznych častiach úlohy a ich výsledky sa na konci zoskupia.
  * **Podmienkový**: Workflow nasleduje rôzne cesty na základe výstupu agenta, podobne ako príkaz if-then-else.

## 2\. Architektúra Microsoft Agent Framework Workflow

Workflow systém Agent Frameworku je pokročilý orchestrujúci engine určený na riadenie zložitých interakcií medzi viacerými agentmi. Je založený na grafovej architektúre, ktorá používa [Pregel-style execution model](https://kowshik.github.io/JPregel/pregel_paper.pdf), kde spracovanie prebieha v synchronizovaných krokoch nazývaných "supersteps."

### Základné komponenty

Architektúra sa skladá z troch hlavných častí:

1.  **Executory**: Sú to základné spracovateľské jednotky. V našich príkladoch je `Agent` typ executor. Každý executor môže mať viacero spracovateľov správ, ktoré sa automaticky vyvolajú podľa typu prijatej správy.
2.  **Hrany (Edges)**: Definujú cestu, ktorou správy prechádzajú medzi executormi. Hrany môžu mať podmienky, čo umožňuje dynamické usmernenie toku informácií cez graf workflow.
3.  **Workflow**: Tento komponent orchestruje celý proces, riadi executory, hrany a celkový tok vykonávania. Zabezpečuje, že správy sa spracujú v správnom poradí a streamuje udalosti pre sledovateľnosť.

*Diagram znázorňujúci základné komponenty workflow systému.*

Táto štruktúra umožňuje budovať robustné a škálovateľné aplikácie využitím základných vzorov ako sekvenčné reťazce, fan-out/fan-in pre paralelné spracovanie a prepínač-case logiku pre podmienené toky.

## 3\. Praktické príklady a analýza kódu

Poďme teraz preskúmať implementáciu rôznych vzorov workflow pomocou frameworku. Pozrieme sa na kód v Pythone a .NET pre každý príklad.

### Prípad 1: Základný sekvenčný workflow

Toto je najjednoduchší vzor, kde výstup jedného agenta sa priamo posiela ďalšiemu. Scenár zahŕňa hotelového agenta `FrontDesk`, ktorý navrhne cestovnú radu, ktorú následne skontroluje agent `Concierge`.

*Diagram základného workflow FrontDesk -> Concierge.*

#### Pozadie scenára

Cestujúci žiada o odporúčanie v Paríži.

1.  Agent `FrontDesk`, navrhnutý na stručnosť, odporúča návštevu múzea Louvre.
2.  Agent `Concierge`, ktorý preferuje autentické zážitky, dostane toto odporúčanie. Skontroluje návrh a poskytne spätnú väzbu, navrhujúc lokálnejšiu, menej turistickú alternatívu.

#### Analýza implementácie v Pythone

V príklade v Pythone najprv definujeme a vytvoríme dvoch agentov, každý so špecifickými inštrukciami.

```python
# 01.python-agent-framework-workflow-ghmodel-basic.ipynb

# Definovať role agentov a inštrukcie
REVIEWER_NAME = "Concierge"
REVIEWER_INSTRUCTIONS = """
    You are a hotel concierge who has opinions about providing the most local and authentic experiences for travelers...
    """

FRONTDESK_NAME = "FrontDesk"
FRONTDESK_INSTRUCTIONS = """
    You are a Front Desk Travel Agent with ten years of experience and are known for brevity...
    """

# Vytvoriť inštancie agentov
reviewer_agent = chat_client.as_agent(
    instructions=(REVIEWER_INSTRUCTIONS),
    name=REVIEWER_NAME,
)

front_desk_agent = chat_client.as_agent(
    instructions=(FRONTDESK_INSTRUCTIONS),
    name=FRONTDESK_NAME,
)
```

Následne sa pomocou `WorkflowBuilder` vytvorí graf. `front_desk_agent` sa nastaví ako východiskový bod a vytvorí sa hrana pripojujúca jeho výstup k `reviewer_agent`.

```python
# 01.python-agent-framework-workflow-ghmodel-basic.ipynb

workflow = WorkflowBuilder(start_executor=front_desk_agent).add_edge(front_desk_agent, reviewer_agent).build()
```

Nakoniec sa spustí workflow s počiatočným vstupom od používateľa.

```python
# 01.python-agent-framework-workflow-ghmodel-basic.ipynb

result =''
# run vykoná workflow; get_outputs() vráti výsledok výkonného modulu.
events = await workflow.run('I would like to go to Paris.')
outputs = events.get_outputs()
result = outputs[0].text if outputs else ''
```

#### Analýza implementácie v .NET (C\#)

Implementácia v .NET nasleduje veľmi podobnú logiku. Najprv sa definujú konštanty pre mená agentov a inštrukcie.

```csharp
// 01.dotnet-agent-framework-workflow-ghmodel-basic.ipynb

const string ReviewerAgentName = "Concierge";
const string ReviewerAgentInstructions = @"
    You are a hotel concierge who has opinions about providing the most local and authentic experiences for travelers...";

const string FrontDeskAgentName = "FrontDesk";
const string FrontDeskAgentInstructions = @"""
    You are a Front Desk Travel Agent with ten years of experience and are known for brevity...";
```

Agenti sa vytvárajú pomocou `AzureOpenAIClient` (Responses API) a potom `WorkflowBuilder` definuje sekvenčný tok pridaním hrany z `frontDeskAgent` na `reviewerAgent`.

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

Workflow sa potom spustí so správou používateľa a výsledky sa streamujú späť.

### Prípad 2: Viacstupňový sekvenčný workflow

Tento vzor rozširuje základnú sekvenciu o viac agentov. Je ideálny pre procesy vyžadujúce viacero etáp zdokonalenia alebo transformácie.

#### Pozadie scenára

Používateľ poskytuje obrázok obývačky a žiada o cenovú ponuku na nábytok.

1.  **Obchodný agent**: Identifikuje položky nábytku na obrázku a vytvorí zoznam.
2.  **Cenový agent**: Vezme zoznam položiek a poskytne detailný cenový rozpis, vrátane rozpočtových, stredných a prémiových možností.
3.  **Agent ponuky**: Prijme ocenený zoznam a naformátuje ho do formálneho dokumentu s ponukou v Markdown.

*Diagram workflow Sales -> Price -> Quote.*

#### Analýza implementácie v Pythone

Definujú sa traja agenti, každý so špecializovanou úlohou. Workflow sa vytvára použitím `add_edge`, čím vznikne reťazec: `sales_agent` -> `price_agent` -> `quote_agent`.

```python
# 02.python-agent-framework-workflow-ghmodel-sequential.ipynb

# Vytvorte troch špecializovaných agentov
sales_agent = chat_client.as_agent(...)
price_agent = chat_client.as_agent(...)
quote_agent = chat_client.as_agent(...)

# Vytvorte sekvenčný pracovný tok
workflow = WorkflowBuilder(start_executor=sales_agent).add_edge(sales_agent, price_agent).add_edge(price_agent, quote_agent).build()
```

Vstupom je `ChatMessage`, ktorý obsahuje text aj URI obrázka. Framework zabezpečuje odovzdanie výstupu každého agenta nasledujúcemu v sekvencii až po generovanie konečnej ponuky.

```python
# 02.python-agent-framework-workflow-ghmodel-sequential.ipynb

# Správa používateľa obsahuje text aj obrázok
message = ChatMessage(
        role=Role.USER,
        contents=[
            TextContent(text="Please find the relevant furniture..."),
            DataContent(uri=image_uri, media_type="image/png")
        ]
)

# Spustite pracovný tok
events = await workflow.run(message)
```

#### Analýza implementácie v .NET (C\#)

Príklad v .NET zrkadlí verziu v Pythone. Vytvoria sa traja agenti (`salesagent`, `priceagent`, `quoteagent`). `WorkflowBuilder` ich spája sekvenčne.

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

Správa používateľa obsahuje dáta obrázka (ako bajty) a textový prompt. Metóda `InProcessExecution.RunStreamingAsync` spustí workflow a konečný výstup sa získa zo streamu.

### Prípad 3: Súbežný workflow

Tento vzor sa používa, keď je možné úlohy vykonávať súčasne na úsporu času. Zahŕňa "fan-out" k viacerým agentom a "fan-in" na zoskupovanie výsledkov.

#### Pozadie scenára

Používateľ žiada o plánovanie cesty do Seattle.

1.  **Dispatcher (fan-out)**: Užívateľova požiadavka je zároveň odoslaná dvom agentom.
2.  **Výskumný agent**: Skúma atrakcie, počasie a dôležité faktory pre cestu do Seattlu v decembri.
3.  **Plánovací agent**: Samostatne vytvára podrobný denný cestovný itinerár.
4.  **Zoskupovateľ (fan-in)**: Výstupy výskumníka a plánovača sa zhromaždia a predstavia ako konečný výsledok.

*Diagram súbežného workflow Výskumník a Plánovač.*

#### Analýza implementácie v Pythone

`ConcurrentBuilder` zjednodušuje vytvorenie tohto vzoru. Stačí len vymenovať zúčastnených agentov a builder automaticky vytvorí potrebnú logiku fan-out a fan-in.

```python
# 03.python-agent-framework-workflow-ghmodel-concurrent.ipynb

research_agent = chat_client.as_agent(name="Researcher-Agent", ...)
plan_agent = chat_client.as_agent(name="Plan-Agent", ...)

# ConcurrentBuilder spracováva logiku rozvetvenia/zjednotenia
workflow = ConcurrentBuilder().participants([research_agent, plan_agent]).build()

# Spustiť pracovný tok
events = await workflow.run("Plan a trip to Seattle in December")
```

Framework zabezpečuje, že `research_agent` a `plan_agent` sa vykonávajú paralelne a ich konečné výstupy sú zhromaždené do zoznamu.

#### Analýza implementácie v .NET (C\#)

V .NET tento vzor vyžaduje explicitnejšie definovanie. Vytvoria sa vlastné executory (`ConcurrentStartExecutor` a `ConcurrentAggregationExecutor`) na spracovanie logiky fan-out a fan-in.

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

`WorkflowBuilder` potom používa `AddFanOutEdge` a `AddFanInEdge` na zostavenie grafu s týmito vlastnými executormi a agentmi.

```csharp
// 03.dotnet-agent-framework-workflow-ghmodel-concurrent.ipynb

var workflow = new WorkflowBuilder(startExecutor)
            .AddFanOutEdge(startExecutor, targets: [researcherAgent, plannerAgent])
            .AddFanInEdge(aggregationExecutor, sources: [researcherAgent, plannerAgent])
            .WithOutputFrom(aggregationExecutor)
            .Build();
```

### Prípad 4: Podmienkový workflow

Podmienkové workflow zavádzajú rozvetvovaciu logiku, ktorá umožňuje systému vybrať rôzne cesty na základe medzivýsledkov.

#### Pozadie scenára

Tento workflow automatizuje tvorbu a publikovanie technického tutoriálu.

1.  **Evangelist-Agent**: Piše návrh tutoriálu na základe poskytnutého osnovy a URL.
2.  **ReviewAgent**: Kontroluje návrh. Skontroluje, či má dokument viac ako 200 slov.
3.  **Podmienková vetva**:
      * **Ak schválené (`Yes`)**: Workflow pokračuje k `Publisher-Agent`.
      * **Ak zamietnuté (`No`)**: Workflow sa zastaví a poskytne dôvod zamietnutia.
4.  **Publisher-Agent**: Ak je návrh schválený, tento agent uloží obsah do Markdown súboru.

#### Analýza implementácie v Pythone

Tento príklad používa vlastnú funkciu `select_targets` na implementáciu podmienkovej logiky. Táto funkcia sa odovzdáva do `add_multi_selection_edge_group` a riadi workflow na základe poľa `review_result` vo výstupe recenzenta.

```python
# 04.python-agent-framework-workflow-aifoundry-condition.ipynb

# Táto funkcia určuje ďalší krok na základe výsledku hodnotenia
def select_targets(review: ReviewResult, target_ids: list[str]) -> list[str]:
    handle_review_id, save_draft_id = target_ids
    if review.review_result == "Yes":
        # Ak je schválené, pokračujte na vykonávateľa 'save_draft'
        return [save_draft_id]
    else:
        # Ak je zamietnuté, pokračujte na vykonávateľa 'handle_review' na oznámenie zlyhania
        return [handle_review_id]

# Tvorca pracovného postupu používa výberovú funkciu na smerovanie
workflow = (
    WorkflowBuilder()
        .set_start_executor(evangelist_agent)
        .add_edge(evangelist_agent, reviewer_agent)
        .add_edge(reviewer_agent, to_reviewer_result)
        # Hrana viacerého výberu implementuje podmienkovú logiku
        .add_multi_selection_edge_group(
            to_reviewer_result,
            [handle_review, save_draft],
            selection_func=select_targets,
        )
        .add_edge(save_draft, publisher_agent)
        .build()
)
```

Vlastné executory ako `to_reviewer_result` sa používajú na parsovanie JSON výstupu od agentov a konverziu do silno typovaných objektov, ktoré môže výberová funkcia kontrolovať.

#### Analýza implementácie v .NET (C\#)

Verzia v .NET používa podobný prístup s podmienkovou funkciou. Definuje sa `Func<object?, bool>`, ktorá kontroluje vlastnosť `Result` objektu `ReviewResult`.

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

Parameter `condition` metódy `AddEdge` umožňuje `WorkflowBuilder` vytvoriť rozvetvenú cestu. Workflow bude nasledovať hranu k `publishExecutor` iba ak podmienka `GetCondition(expectedResult: "Yes")` vráti pravdu. Inak nasleduje cestu k `sendReviewerExecutor`.

## Záver

Microsoft Agent Framework Workflow poskytuje robustný a flexibilný základ pre orchestráciu zložitých viacagentových systémov. Využitím jeho grafovej architektúry a základných komponentov môžu vývojári navrhovať a implementovať pokročilé workflow v Pythone aj .NET. Či už vaša aplikácia vyžaduje jednoduché sekvenčné spracovanie, paralelnú exekúciu alebo dynamickú podmienkovú logiku, framework ponúka nástroje na tvorbu výkonných, škálovateľných a silne typovaných AI-riešení.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Vyhlásenie o zodpovednosti**:
Tento dokument bol preložený pomocou AI prekladateľskej služby [Co-op Translator](https://github.com/Azure/co-op-translator). Hoci sa snažíme o presnosť, vezmite prosím na vedomie, že automatické preklady môžu obsahovať chyby alebo nepresnosti. Pôvodný dokument v jeho natívnom jazyku by mal byť považovaný za autoritatívny zdroj. Pre kritické informácie sa odporúča profesionálny ľudský preklad. Nie sme zodpovední za žiadne nedorozumenia alebo nesprávne interpretácie vyplývajúce z použitia tohto prekladu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->