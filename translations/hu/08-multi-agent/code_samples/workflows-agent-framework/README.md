# Többügynökös alkalmazások építése a Microsoft Agent Framework Workflow segítségével

Ez az útmutató bemutatja, hogyan érthetjük meg és építhetünk többügynökös alkalmazásokat a Microsoft Agent Framework segítségével. Megvizsgáljuk a többügynökös rendszerek alapfogalmait, elmélyedünk a keretrendszer Workflow komponensének architektúrájában, és gyakorlati példákon keresztül bemutatjuk a különböző workflow mintákat Pythonban és .NET-ben.

## 1\. Többügynökös rendszerek megértése

Egy AI ügynök olyan rendszer, amely túlmutat egy hagyományos Nagy Nyelvi Modell (LLM) képességein. Képes érzékelni a környezetét, döntéseket hozni és cselekedni, hogy meghatározott célokat érjen el. Egy többügynökös rendszer több ilyen ügynök együttműködését foglalja magában, hogy megoldjanak egy olyan problémát, amelyet egyetlen ügynök önmagában nehezen vagy egyáltalán nem tudna kezelni.

### Gyakori alkalmazási forgatókönyvek

  * **Komplex problémamegoldás**: Egy nagy feladat (pl. egy vállalati esemény megtervezése) kisebb alfeladatokra bontása, amelyeket specializált ügynökök kezelnek (pl. költségvetési ügynök, logisztikai ügynök, marketing ügynök).
  * **Virtuális asszisztensek**: Egy fő asszisztens ügynök, amely feladatokat delegál, például időpont-egyeztetést, kutatást és foglalást más specializált ügynököknek.
  * **Automatizált tartalomkészítés**: Egy workflow, ahol egy ügynök megírja a tartalmat, egy másik ellenőrzi a pontosságot és a hangnemet, egy harmadik pedig publikálja.

### Többügynökös minták

A többügynökös rendszerek különböző minták szerint szervezhetők, amelyek meghatározzák, hogyan lépnek kapcsolatba egymással:

  * **Szekvenciális**: Az ügynökök előre meghatározott sorrendben dolgoznak, mint egy futószalag. Az egyik ügynök kimenete a következő bemenete lesz.
  * **Párhuzamos**: Az ügynökök párhuzamosan dolgoznak egy feladat különböző részein, és az eredményeiket a végén összesítik.
  * **Feltételes**: A workflow különböző útvonalakat követ az ügynök kimenetétől függően, hasonlóan egy if-then-else szerkezethez.

## 2\. A Microsoft Agent Framework Workflow architektúrája

Az Agent Framework workflow rendszere egy fejlett orkestrációs motor, amely a több ügynök közötti komplex interakciók kezelésére lett tervezve. Egy gráf-alapú architektúrán alapul, amely egy [Pregel-stílusú végrehajtási modellt](https://kowshik.github.io/JPregel/pregel_paper.pdf) használ, ahol a feldolgozás szinkronizált lépésekben, úgynevezett "superstep"-ekben történik.

### Fő komponensek

Az architektúra három fő részből áll:

1.  **Végrehajtók (Executors)**: Ezek az alapvető feldolgozó egységek. Példáinkban az `Agent` egy végrehajtó típusa. Minden végrehajtónak lehet több üzenetkezelője, amelyeket automatikusan meghív a fogadott üzenet típusa alapján.
2.  **Élek (Edges)**: Ezek határozzák meg az üzenetek útját a végrehajtók között. Az élek feltételeket tartalmazhatnak, lehetővé téve az információ dinamikus irányítását a workflow gráfban.
3.  **Workflow**: Ez a komponens irányítja az egész folyamatot, kezeli a végrehajtókat, az éleket és az általános végrehajtási folyamatot. Biztosítja, hogy az üzenetek helyes sorrendben legyenek feldolgozva, és eseményeket közvetít a megfigyelhetőség érdekében.

*Egy diagram, amely bemutatja a workflow rendszer fő komponenseit.*

Ez a struktúra lehetővé teszi robusztus és skálázható alkalmazások építését alapvető minták, például szekvenciális láncok, párhuzamos feldolgozás (fan-out/fan-in) és feltételes elágazások (switch-case logika) használatával.

## 3\. Gyakorlati példák és kódelemzés

Most nézzük meg, hogyan valósíthatók meg különböző workflow minták a keretrendszer segítségével. Minden példát Pythonban és .NET-ben is bemutatunk.

### Eset 1: Egyszerű szekvenciális workflow

Ez a legegyszerűbb minta, ahol az egyik ügynök kimenete közvetlenül a másik bemenete lesz. Forgatókönyvünkben egy szállodai `FrontDesk` ügynök utazási ajánlást tesz, amelyet egy `Concierge` ügynök felülvizsgál.

*Diagram az alapvető FrontDesk -\> Concierge workflow-ról.*

#### Forgatókönyv háttér

Egy utazó ajánlást kér Párizsban.

1.  A `FrontDesk` ügynök, amely a tömörségre van tervezve, a Louvre Múzeum meglátogatását javasolja.
2.  A `Concierge` ügynök, aki az autentikus élményeket részesíti előnyben, megkapja ezt az ajánlást. Felülvizsgálja, és egy helyi, kevésbé turistás alternatívát javasol.

#### Python implementáció elemzése

A Python példában először definiáljuk és létrehozzuk a két ügynököt, mindegyiket specifikus utasításokkal.

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

Ezután a `WorkflowBuilder` segítségével felépítjük a gráfot. A `front_desk_agent` a kezdőpont, és egy él köti össze a kimenetét a `reviewer_agent`-tel.

```python
# 01.python-agent-framework-workflow-ghmodel-basic.ipynb

workflow = WorkflowBuilder().set_start_executor(front_desk_agent).add_edge(front_desk_agent, reviewer_agent).build()
```

Végül a workflow-t a felhasználó kezdeti kérdésével futtatjuk.

```python
# 01.python-agent-framework-workflow-ghmodel-basic.ipynb

result =''
# The run_stream method executes the workflow and streams events.
async for event in workflow.run_stream('I would like to go to Paris.'):
    if isinstance(event, WorkflowEvent):
        result += str(event.data)
```

#### .NET (C#) implementáció elemzése

A .NET implementáció nagyon hasonló logikát követ. Először konstansokat definiálunk az ügynökök neveihez és utasításaihoz.

```csharp
// 01.dotnet-agent-framework-workflow-ghmodel-basic.ipynb

const string ReviewerAgentName = "Concierge";
const string ReviewerAgentInstructions = @"
    You are an are hotel concierge who has opinions about providing the most local and authentic experiences for travelers...";

const string FrontDeskAgentName = "FrontDesk";
const string FrontDeskAgentInstructions = @"""
    You are a Front Desk Travel Agent with ten years of experience and are known for brevity...";
```

Az ügynököket egy `OpenAIClient` segítségével hozzuk létre, majd a `WorkflowBuilder` meghatározza a szekvenciális folyamatot azzal, hogy egy élt ad hozzá a `frontDeskAgent` és a `reviewerAgent` között.

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

A workflow-t ezután a felhasználó üzenetével futtatjuk, és az eredményeket visszacsatoljuk.

### Eset 2: Többlépcsős szekvenciális workflow

Ez a minta kiterjeszti az alapvető szekvenciát több ügynökre. Ideális olyan folyamatokhoz, amelyek több szakaszban történő finomítást vagy átalakítást igényelnek.

#### Forgatókönyv háttér

Egy felhasználó egy nappali képét adja meg, és árajánlatot kér a bútorokra.

1.  **Sales-Agent**: Azonosítja a képen látható bútorokat, és listát készít.
2.  **Price-Agent**: A bútorok listáját felhasználva részletes árajánlatot ad, beleértve a költséghatékony, középkategóriás és prémium opciókat.
3.  **Quote-Agent**: Az árazott listát formális árajánlat-dokumentummá alakítja Markdown formátumban.

*Diagram a Sales -\> Price -\> Quote workflow-ról.*

#### Python implementáció elemzése

Három ügynököt definiálunk, mindegyik speciális szereppel. A workflow-t az `add_edge` segítségével építjük fel, hogy létrehozzuk a láncot: `sales_agent` -\> `price_agent` -\> `quote_agent`.

```python
# 02.python-agent-framework-workflow-ghmodel-sequential.ipynb

# Create three specialized agents
sales_agent = chat_client.create_agent(...)
price_agent = chat_client.create_agent(...)
quote_agent = chat_client.create_agent(...)

# Build the sequential workflow
workflow = WorkflowBuilder().set_start_executor(sales_agent).add_edge(sales_agent, price_agent).add_edge(price_agent, quote_agent).build()
```

A bemenet egy `ChatMessage`, amely tartalmazza a szöveget és a kép URI-ját. A keretrendszer biztosítja, hogy az egyes ügynökök kimenete a következő bemenete legyen, amíg a végső árajánlat létre nem jön.

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

#### .NET (C#) implementáció elemzése

A .NET példa tükrözi a Python verziót. Három ügynököt (`salesagent`, `priceagent`, `quoteagent`) hozunk létre. A `WorkflowBuilder` szekvenciálisan kapcsolja össze őket.

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

A felhasználó üzenetét a kép adataival (bájtokként) és a szöveges kérdéssel együtt állítjuk össze. Az `InProcessExecution.StreamAsync` metódus elindítja a workflow-t, és a végső kimenetet a streamből kapjuk meg.

### Eset 3: Párhuzamos workflow

Ez a minta akkor használatos, amikor a feladatok egyszerre végezhetők el az idő megtakarítása érdekében. Ez magában foglalja a "fan-out" (szétosztás) és a "fan-in" (összesítés) logikát.

#### Forgatókönyv háttér

Egy felhasználó Seattle-i utazást szeretne tervezni.

1.  **Dispatcher (Fan-Out)**: A felhasználó kérését egyszerre két ügynöknek küldi el.
2.  **Researcher-Agent**: Kutatást végez a látnivalókról, időjárásról és a decemberi utazás kulcsfontosságú szempontjairól.
3.  **Plan-Agent**: Függetlenül részletes napi utazási tervet készít.
4.  **Aggregator (Fan-In)**: Az eredményeket mindkét ügynöktől összegyűjti, és együttesen bemutatja.

*Diagram a párhuzamos Researcher és Planner workflow-ról.*

#### Python implementáció elemzése

A `ConcurrentBuilder` egyszerűsíti ennek a mintának a létrehozását. Csak meg kell adni a résztvevő ügynököket, és a builder automatikusan létrehozza a szükséges fan-out és fan-in logikát.

```python
# 03.python-agent-framework-workflow-ghmodel-concurrent.ipynb

research_agent = chat_client.create_agent(name="Researcher-Agent", ...)
plan_agent = chat_client.create_agent(name="Plan-Agent", ...)

# ConcurrentBuilder handles the fan-out/fan-in logic
workflow = ConcurrentBuilder().participants([research_agent, plan_agent]).build()

# Run the workflow
events = await workflow.run("Plan a trip to Seattle in December")
```

A keretrendszer biztosítja, hogy a `research_agent` és a `plan_agent` párhuzamosan fusson, és a végső kimenetüket egy listába gyűjti.

#### .NET (C#) implementáció elemzése

A .NET-ben ez a minta explicit definíciót igényel. Egyedi végrehajtókat (`ConcurrentStartExecutor` és `ConcurrentAggregationExecutor`) hozunk létre a fan-out és fan-in logika kezelésére.

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

A `WorkflowBuilder` ezután az `AddFanOutEdge` és `AddFanInEdge` metódusokat használja a gráf felépítéséhez ezekkel az egyedi végrehajtókkal és az ügynökökkel.

```csharp
// 03.dotnet-agent-framework-workflow-ghmodel-concurrent.ipynb

var workflow = new WorkflowBuilder(startExecutor)
            .AddFanOutEdge(startExecutor, targets: [researcherAgent, plannerAgent])
            .AddFanInEdge(aggregationExecutor, sources: [researcherAgent, plannerAgent])
            .WithOutputFrom(aggregationExecutor)
            .Build();
```

### Eset 4: Feltételes workflow

A feltételes workflow-k elágazó logikát vezetnek be, lehetővé téve a rendszer számára, hogy az eredmények alapján különböző útvonalakat kövessen.

#### Forgatókönyv háttér

Ez a workflow egy technikai útmutató létrehozását és publikálását automatizálja.

1.  **Evangelist-Agent**: Az útmutató vázlata és URL-ek alapján megírja a tervezetet.
2.  **ContentReviewer-Agent**: Felülvizsgálja a tervezetet. Ellenőrzi, hogy a szószám meghaladja-e a 200 szót.
3.  **Feltételes elágazás**:
      * **Ha elfogadott (`Yes`)**: A workflow a `Publisher-Agent`-hez folytatódik.
      * **Ha elutasított (`No`)**: A workflow leáll, és megadja az elutasítás okát.
4.  **Publisher-Agent**: Ha a tervezetet elfogadják, ez az ügynök elmenti a tartalmat egy Markdown fájlba.

#### Python implementáció elemzése

Ebben a példában egy egyedi függvényt, `select_targets`-t használunk a feltételes logika megvalósításához. Ezt a függvényt az `add_multi_selection_edge_group`-hoz adjuk, amely a `review_result` mező alapján irányítja a workflow-t.

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

Egyedi végrehajtókat, például `to_reviewer_result`-t használunk az ügynökök JSON kimenetének elemzésére és erősen típusos objektumokká alakítására, amelyeket a kiválasztási függvény vizsgálhat.

#### .NET (C#) implementáció elemzése

A .NET verzió hasonló megközelítést alkalmaz egy feltétel függvénnyel. Egy `Func<object?, bool>` függvényt definiálunk, amely ellenőrzi a `ReviewResult` objektum `Result` tulajdonságát.

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

Az `AddEdge` metódus `condition` paramétere lehetővé teszi a `WorkflowBuilder` számára, hogy elágazó útvonalat hozzon létre. A workflow csak akkor követi az élt a `publishExecutor`-hoz, ha a `GetCondition(expectedResult: "Yes")` feltétel igazat ad vissza. Ellenkező esetben a `sendReviewerExecutor`-hoz vezet.

## Összegzés

A Microsoft Agent Framework Workflow robusztus és rugalmas alapot biztosít a komplex, többügynökös rendszerek orkestrációjához. Gráf-alapú architektúrájának és fő komponenseinek köszönhetően a fejlesztők kifinomult workflow-kat tervezhetnek és valósíthatnak meg Pythonban és .NET-ben. Akár egyszerű szekvenciális feldolgozásra, párhuzamos végrehajtásra vagy dinamikus feltételes logikára van szükség, a keretrendszer eszközöket kínál erőteljes, skálázható és típusbiztos AI-alapú megoldások építéséhez.

---

**Felelősségkizárás**:  
Ez a dokumentum az [Co-op Translator](https://github.com/Azure/co-op-translator) AI fordítószolgáltatás segítségével készült. Bár törekszünk a pontosságra, kérjük, vegye figyelembe, hogy az automatikus fordítások hibákat vagy pontatlanságokat tartalmazhatnak. Az eredeti dokumentum az eredeti nyelvén tekintendő hiteles forrásnak. Kritikus információk esetén javasolt a professzionális, emberi fordítás igénybevétele. Nem vállalunk felelősséget a fordítás használatából eredő félreértésekért vagy téves értelmezésekért.