# Tvorba multi-agentných aplikácií s Microsoft Agent Framework Workflow

Tento tutoriál vás prevedie pochopením a tvorbou multi-agentných aplikácií pomocou Microsoft Agent Framework. Preskúmame základné koncepty multi-agentných systémov, ponoríme sa do architektúry komponentu Workflow frameworku a prejdeme praktickými príkladmi v Pythone aj .NET pre rôzne vzory pracovných tokov.

## 1\. Pochopenie multi-agentných systémov

AI agent je systém, ktorý presahuje schopnosti bežného veľkého jazykového modelu (LLM). Dokáže vnímať svoje prostredie, robiť rozhodnutia a konať na dosiahnutie konkrétnych cieľov. Multi-agentný systém zahŕňa niekoľko takýchto agentov spolupracujúcich na riešení problému, ktorý by pre jedného agenta bol náročný alebo nemožný vyriešiť sám.

### Bežné aplikačné scenáre

  * **Riešenie zložitých problémov**: Rozdelenie veľkej úlohy (napr. plánovanie firemnej udalosti) na menšie podúlohy, ktoré riešia špecializovaní agenti (napr. agent pre rozpočet, agent pre logistiku, agent pre marketing).
  * **Virtuálni asistenti**: Primárny asistent deleguje úlohy ako plánovanie, výskum a rezervácie ďalším špecializovaným agentom.
  * **Automatizovaná tvorba obsahu**: Pracovný tok, kde jeden agent vytvára návrh obsahu, druhý ho kontroluje na presnosť a tón a tretí ho uverejňuje.

### Vzory multi-agentov

Multi-agentné systémy môžu byť organizované v rôznych vzoroch, ktoré určujú, ako spolu komunikujú:

  * **Sekvenčné**: Agenti pracujú v preddefinovanom poradí, ako na výrobnej linke. Výstup jedného agenta sa stáva vstupom pre ďalšieho.
  * **Súbežné**: Agenti pracujú paralelne na rôznych častiach úlohy a ich výsledky sa na konci zoskupujú.
  * **Podmienené**: Pracovný tok nasleduje rôzne cesty podľa výstupu agenta, podobne ako vetvenie if-then-else.

## 2\. Architektúra Microsoft Agent Framework Workflow

Pracovný tok Agent Frameworku je pokročilý orchestrujúci motor, navrhnutý na riadenie komplexných interakcií medzi viacerými agentmi. Je postavený na grafovej architektúre, ktorá používa [Pregel-style execution model](https://kowshik.github.io/JPregel/pregel_paper.pdf), kde spracovanie prebieha vo synchronizovaných krokoch nazývaných "supersteps".

### Hlavné komponenty

Architektúra sa skladá z troch hlavných častí:

1.  **Executors (vykonávače)**: Základné jednotky spracovania. V našich príkladoch je `Agent` typ vykonávača. Každý vykonávač môže mať viacero spracovateľov správ, ktoré sú automaticky vyvolané podľa typu prijatej správy.
2.  **Edges (hrany)**: Definujú cestu, ktorú správy prechádzajú medzi vykonávačmi. Hrany môžu mať podmienky, čo umožňuje dynamické smerovanie informácií cez graf pracovného toku.
3.  **Workflow**: Tento komponent orchestruje celý proces, riadi vykonávače, hrany a celkový tok vykonávania. Zabezpečuje správne spracovanie správ v poradí a streamuje udalosti pre pozorovateľnosť.

*Diagram ilustrujúci hlavné komponenty systému pracovného toku.*

Táto štruktúra umožňuje budovať robustné a škálovateľné aplikácie využívajúce základné vzory ako sekvenčné reťazce, fan-out/fan-in pre paralelné spracovanie a switch-case logiku pre podmienené toky.

## 3\. Praktické príklady a analýza kódu

Teraz preskúmame, ako implementovať rôzne vzory pracovných tokov pomocou frameworku. Pozrieme sa na kód v Pythone aj .NET pre každý príklad.

### Prípad 1: Základný sekvenčný pracovný tok

Toto je najjednoduchší vzor, kde výstup jedného agenta je priamo odovzdaný ďalšiemu. Náš scenár zahŕňa hotelového agenta `FrontDesk`, ktorý navrhne cestovný tip, ktorý následne overí agent `Concierge`.

*Diagram základného pracovného toku FrontDesk -> Concierge.*

#### Pozadie scenára

Cestujúci žiada o odporúčanie v Paríži.

1.  Agent `FrontDesk`, zameraný na stručnosť, odporúča návštevu múzea Louvre.
2.  Agent `Concierge`, ktorý dáva prednosť autentickým zážitkom, prijíma toto odporúčanie. Skontroluje ho a poskytne spätnú väzbu, navrhujúc miestnu, menej turistickú alternatívu.

#### Analýza implementácie v Pythone

V Pythone najskôr definujeme a vytvoríme oboch agentov, každý so špecifickými inštrukciami.

```python
# 01.python-agent-framework-workflow-ghmodel-basic.ipynb

# Definujte role agentov a pokyny
REVIEWER_NAME = "Concierge"
REVIEWER_INSTRUCTIONS = """
    You are an are hotel concierge who has opinions about providing the most local and authentic experiences for travelers...
    """

FRONTDESK_NAME = "FrontDesk"
FRONTDESK_INSTRUCTIONS = """
    You are a Front Desk Travel Agent with ten years of experience and are known for brevity...
    """

# Vytvorte inštancie agentov
reviewer_agent = chat_client.as_agent(
    instructions=(REVIEWER_INSTRUCTIONS),
    name=REVIEWER_NAME,
)

front_desk_agent = chat_client.as_agent(
    instructions=(FRONTDESK_INSTRUCTIONS),
    name=FRONTDESK_NAME,
)
```

Potom sa použije `WorkflowBuilder` na vytvorenie grafu. `front_desk_agent` je nastavený ako východiskový bod a vytvorí sa hrana spájajúca jeho výstup s `reviewer_agent`.

```python
# 01.python-agent-framework-workflow-ghmodel-basic.ipynb

workflow = WorkflowBuilder(start_executor=front_desk_agent).add_edge(front_desk_agent, reviewer_agent).build()
```

Nakoniec sa pracovný tok vykoná s počiatočným vstupom od používateľa.

```python
# 01.python-agent-framework-workflow-ghmodel-basic.ipynb

result =''
# run spúšťa pracovný tok; get_outputs() vracia výsledok vykonávateľa výstupu.
events = await workflow.run('I would like to go to Paris.')
outputs = events.get_outputs()
result = outputs[0].text if outputs else ''
```

#### Analýza implementácie v .NET (C\#)

Implementácia v .NET nasleduje veľmi podobnú logiku. Najskôr sa definujú konštanty pre mená agentov a ich inštrukcie.

```csharp
// 01.dotnet-agent-framework-workflow-ghmodel-basic.ipynb

const string ReviewerAgentName = "Concierge";
const string ReviewerAgentInstructions = @"
    You are an are hotel concierge who has opinions about providing the most local and authentic experiences for travelers...";

const string FrontDeskAgentName = "FrontDesk";
const string FrontDeskAgentInstructions = @"""
    You are a Front Desk Travel Agent with ten years of experience and are known for brevity...";
```

Agenti sa vytvárajú pomocou `AzureOpenAIClient` (API odpovedí) a potom `WorkflowBuilder` definuje sekvenčný tok pridaním hrany z `frontDeskAgent` na `reviewerAgent`.

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

Workflow sa následne spúšťa so správou používateľa a výsledky sa streamujú späť.

### Prípad 2: Sekvenčný pracovný tok s viacerými krokmi

Tento vzor rozširuje základné sekvenčné usporiadanie o viac agentov. Je ideálny pre procesy, ktoré vyžadujú viacúrovňové spresnenia alebo transformácie.

#### Pozadie scenára

Používateľ poskytne obrázok obývačky a žiada o cenovú ponuku na nábytok.

1.  **Predajný agent**: Identifikuje položky nábytku na obrázku a vytvorí zoznam.
2.  **Cenový agent**: Preberá zoznam a poskytuje detailný rozpis cien vrátane lacných, stredných a prémiových možností.
3.  **Agent pre ponuku**: Prijíma ocenený zoznam a formátuje ho do formálneho dokumentu ponuky v Markdown.

*Diagram pracovného toku Sales -> Price -> Quote.*

#### Analýza implementácie v Pythone

Sú definovaní traja agenti, každý so špecializovanou úlohou. Workflow sa konštruuje pomocou `add_edge`, čím sa vytvorí reťazec: `sales_agent` -> `price_agent` -> `quote_agent`.

```python
# 02.python-agent-framework-workflow-ghmodel-sequential.ipynb

# Vytvorte troch špecializovaných agentov
sales_agent = chat_client.as_agent(...)
price_agent = chat_client.as_agent(...)
quote_agent = chat_client.as_agent(...)

# Vytvorte sekvenčný pracovný tok
workflow = WorkflowBuilder(start_executor=sales_agent).add_edge(sales_agent, price_agent).add_edge(price_agent, quote_agent).build()
```

Vstup je `ChatMessage` obsahujúca text aj URI obrázka. Framework zabezpečuje odovzdávanie výstupu každého agenta ďalšiemu v poradí až po vytvorenie konečnej ponuky.

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

# Spustiť tok práce
events = await workflow.run(message)
```

#### Analýza implementácie v .NET (C\#)

.NET príklad zrkadlí Python verziu. Sú vytvorení traja agenti (`salesagent`, `priceagent`, `quoteagent`). `WorkflowBuilder` ich spája sekvenčne.

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

Správa používateľa obsahuje dáta obrázka (vo formáte bytov) a textový prompt. Metóda `InProcessExecution.StreamAsync` spúšťa workflow a konečný výstup sa získava zo streamu.

### Prípad 3: Súbežný pracovný tok

Tento vzor sa používa, keď úlohy môžu byť vykonávané zároveň na úsporu času. Zahrňuje „fan-out“ na viac agentov a „fan-in“ na zbere výsledkov.

#### Pozadie scenára

Používateľ žiada o naplánovanie výletu do Seattlu.

1.  **Dispatcher (fan-out)**: Používateľova požiadavka je odoslaná súčasne dvom agentom.
2.  **Výskumný agent**: Študuje atrakcie, počasie a kľúčové aspekty cesty do Seattlu v decembri.
3.  **Plánovací agent**: Nezávisle vytvára denné detailné cestovné plány.
4.  **Aggregator (fan-in)**: Výstupy výskumníka a plánovača sa zhromaždia a predstavia ako konečný výsledok.

*Diagram súbežného pracovného toku výskumníka a plánovača.*

#### Analýza implementácie v Pythone

`ConcurrentBuilder` zjednodušuje vytvorenie tohto vzoru. Stačí v zozname uviesť zúčastnených agentov a builder automaticky vytvorí potrebnú logiku fan-out a fan-in.

```python
# 03.python-agent-framework-workflow-ghmodel-concurrent.ipynb

research_agent = chat_client.as_agent(name="Researcher-Agent", ...)
plan_agent = chat_client.as_agent(name="Plan-Agent", ...)

# ConcurrentBuilder spravuje logiku rozbočenia a zbiehania
workflow = ConcurrentBuilder().participants([research_agent, plan_agent]).build()

# Spustiť pracovný proces
events = await workflow.run("Plan a trip to Seattle in December")
```

Framework zabezpečí, že `research_agent` a `plan_agent` bežia paralelne a ich výstupy sú zhromaždené do zoznamu.

#### Analýza implementácie v .NET (C\#)

V .NET vyžaduje tento vzor explicitnejšiu definíciu. Vytvárajú sa vlastné vykonávače (`ConcurrentStartExecutor` a `ConcurrentAggregationExecutor`), ktoré spravujú logiku fan-out a fan-in.

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

`WorkflowBuilder` potom používa `AddFanOutEdge` a `AddFanInEdge` na konštrukciu grafu s týmito vlastnými vykonávačmi a agentmi.

```csharp
// 03.dotnet-agent-framework-workflow-ghmodel-concurrent.ipynb

var workflow = new WorkflowBuilder(startExecutor)
            .AddFanOutEdge(startExecutor, targets: [researcherAgent, plannerAgent])
            .AddFanInEdge(aggregationExecutor, sources: [researcherAgent, plannerAgent])
            .WithOutputFrom(aggregationExecutor)
            .Build();
```

### Prípad 4: Podmienený pracovný tok

Podmienené pracovné toky zavádzajú vetvenú logiku, ktorá umožňuje systému vybrať rôzne cesty na základe medzivýsledkov.

#### Pozadie scenára

Tento pracovný tok automatizuje tvorbu a publikáciu technického tutoriálu.

1.  **Evangelist-Agent**: Napíše návrh tutoriálu podľa poskytnutého osnovy a URL adries.
2.  **ContentReviewer-Agent**: Skontroluje návrh. Overí, či má viac ako 200 slov.
3.  **Podmienená vetva**:
      * **Ak schválené (`Yes`)**: Pracovný tok pokračuje k `Publisher-Agent`.
      * **Ak zamietnuté (`No`)**: Pracovný tok sa zastavuje a vypíše dôvod zamietnutia.
4.  **Publisher-Agent**: Ak je návrh schválený, tento agent uloží obsah do Markdown súboru.

#### Analýza implementácie v Pythone

Tento príklad používa vlastnú funkciu `select_targets` na implementáciu podmienenej logiky. Táto funkcia sa odovzdáva do `add_multi_selection_edge_group` a riadi pracovný tok podľa poľa `review_result` z výstupu recenzenta.

```python
# 04.python-agent-framework-workflow-aifoundry-condition.ipynb

# Táto funkcia určuje ďalší krok na základe výsledku kontroly
def select_targets(review: ReviewResult, target_ids: list[str]) -> list[str]:
    handle_review_id, save_draft_id = target_ids
    if review.review_result == "Yes":
        # Ak je schválené, pokračujte na vykonávateľa 'save_draft'
        return [save_draft_id]
    else:
        # Ak je zamietnuté, pokračujte na vykonávateľa 'handle_review' na nahlásenie neúspechu
        return [handle_review_id]

# Stavač pracovného postupu používa výberovú funkciu pre smerovanie
workflow = (
    WorkflowBuilder()
        .set_start_executor(evangelist_agent)
        .add_edge(evangelist_agent, reviewer_agent)
        .add_edge(reviewer_agent, to_reviewer_result)
        # Veľ viacnásobných výberov implementuje podmienkovú logiku
        .add_multi_selection_edge_group(
            to_reviewer_result,
            [handle_review, save_draft],
            selection_func=select_targets,
        )
        .add_edge(save_draft, publisher_agent)
        .build()
)
```

Vlastné vykonávače ako `to_reviewer_result` sa používajú na parsovanie JSON výstupu agentov a konverziu do silno typovaných objektov, ktoré funkcia výberu môže kontrolovať.

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

Paramater `condition` metódy `AddEdge` umožňuje `WorkflowBuilder` vytvoriť vetvenú cestu. Workflow bude nasledovať hranu k `publishExecutor` iba ak podmienka `GetCondition(expectedResult: "Yes")` vráti true. Inak pôjde cestou k `sendReviewerExecutor`.

## Záver

Microsoft Agent Framework Workflow poskytuje robustný a flexibilný základ na orchestráciu komplexných multi-agentných systémov. Vďaka grafovej architektúre a hlavným komponentom môžu vývojári navrhovať a implementovať sofistikované pracovné toky v Pythone aj .NET. Či už vaša aplikácia vyžaduje jednoduché sekvenčné spracovanie, paralelné vykonávanie alebo dynamickú podmienenú logiku, framework ponúka nástroje na vytvorenie výkonných, škálovateľných a typovo bezpečných riešení poháňaných AI.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Vyhlásenie o zodpovednosti**:
Tento dokument bol preložený pomocou AI prekladateľskej služby [Co-op Translator](https://github.com/Azure/co-op-translator). Hoci sa snažíme o presnosť, vezmite prosím na vedomie, že automatické preklady môžu obsahovať chyby alebo nepresnosti. Pôvodný dokument v jeho natívnom jazyku by mal byť považovaný za autoritatívny zdroj. Pre kritické informácie sa odporúča profesionálny ľudský preklad. Nie sme zodpovední za žiadne nedorozumenia alebo nesprávne interpretácie vyplývajúce z použitia tohto prekladu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->