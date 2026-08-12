# Többügynökös Alkalmazások Építése a Microsoft Agent Framework Workflow-val

Ez a bemutató végigvezet a Microsoft Agent Framework használatán többügynökös alkalmazások megértésében és építésében. Felfedezzük a többügynökös rendszerek alapvető fogalmait, mélyrehatóan megvizsgáljuk a keretrendszer Workflow komponensének architektúráját, és gyakorlati példákon keresztül bemutatjuk Python és .NET nyelveken különböző workflow minták esetén.

## 1\. A Többügynökös Rendszerek Megértése

Egy MI Ügynök olyan rendszer, amely meghaladja a szokásos Nagy Nyelvi Modell (LLM) képességeit. Képes érzékelni a környezetét, döntéseket hozni és végrehajtani bizonyos célok eléréséhez szükséges lépéseket. Egy többügynökös rendszer több ilyen ügynök együttműködését jelenti egy olyan probléma megoldása érdekében, amelyet egyetlen ügynök nehezen vagy egyáltalán nem tudna önállóan kezelni.

### Gyakori Alkalmazási Forgatókönyvek

  * **Komplex Problémamegoldás**: Egy nagyobb feladat (pl. céges rendezvény tervezése) lebontása kisebb részfeladatokra, amelyeket speciális ügynökök kezelnek (pl. költségvetési ügynök, logisztikai ügynök, marketing ügynök).
  * **Virtuális Asszisztensek**: Egy elsődleges asszisztens ügynök feladatokat delegál, mint például időpont-egyeztetés, kutatás és foglalás, más specializált ügynökök számára.
  * **Automatizált Tartalomkészítés**: Egy olyan munkafolyamat, ahol egy ügynök tartalmat készít, egy másik ellenőrzi annak pontosságát és stílusát, egy harmadik pedig publikálja azt.

### Többügynökös Minták

A többügynökös rendszerek többféle mintában szervezhetők, amelyek meghatározzák az ügynökök közötti interakció módját:

  * **Szekvenciális**: Az ügynökök előre meghatározott sorrendben dolgoznak, mint egy futószalag. Az egyik ügynök kimenete a következő bemenete lesz.
  * **Párhuzamos**: Az ügynökök párhuzamosan dolgoznak a feladat különböző részein, és a végeredményt összevonják.
  * **Feltételes**: A munkafolyamat különböző utak követésére képes az ügynök kimenete alapján, hasonlóan egy if-then-else szerkezethez.

## 2\. A Microsoft Agent Framework Workflow Architektúrája

Az Agent Framework munkafolyamat rendszere egy fejlett koordinációs motor, amely összetett interakciókat képes kezelni több ügynök között. Egy gráf-alapú architektúrán alapul, amely [Pregel-stílusú végrehajtási modellt](https://kowshik.github.io/JPregel/pregel_paper.pdf) használ, ahol a feldolgozás szinkronizált lépésekben, úgynevezett „szuperlépésekben” történik.

### Alapelemek

Az architektúra három fő részből áll:

1.  **Végrehajtók**: Ezek az alapvető feldolgozó egységek. A példáinkban egy `Agent` egy végrehajtó típus. Minden végrehajtónak több üzenetkezelője lehet, amelyek a beérkező üzenet típusától függően automatikusan hívódnak meg.
2.  **Élek**: Meghatározzák az üzenetek útvonalát a végrehajtók között. Az élekhez feltételek rendelhetők, lehetővé téve az információ dinamikus irányítását a munkafolyamat gráfjában.
3.  **Workflow**: Ez a komponens koordinálja az egész folyamatot, kezeli a végrehajtókat, az éleket és az általános végrehajtási folyamatot. Biztosítja, hogy az üzenetek a helyes sorrendben legyenek feldolgozva, és eseményeket sugároz az megfigyelhetőség érdekében.

*Egy diagram a workflow rendszer alapelemeiről.*

Ez a struktúra lehetővé teszi robusztus és skálázható alkalmazások építését alapvető minták, mint például a szekvenciális láncok, a párhuzamos feldolgozást biztosító fan-out/fan-in és a feltételes elágazásos logika használatával.

## 3\. Gyakorlati Példák és Kód Elemzés

Most nézzük meg, hogyan lehet megvalósítani különböző workflow mintákat a keretrendszer segítségével. Mind Python, mind .NET kód példákat bemutatunk.

### 1. Példa: Egyszerű Szekvenciális Workflow

Ez a legegyszerűbb minta, ahol egy ügynök kimenete közvetlenül átadásra kerül egy másiknak. A forgatókönyvben egy `FrontDesk` (recepció) nevű szállodai ügynök javaslatot tesz, amelyet aztán egy `Concierge` (portás) ügynök felülvizsgál.

*Az alap FrontDesk -\> Concierge munkafolyamat ábrája.*

#### Forgatókönyv Háttér

Egy utazó Párizsban kér ajánlást.

1.  A rövid és tömör megfogalmazású `FrontDesk` ügynök azt javasolja, hogy látogassák meg a Louvre Múzeumot.
2.  A hiteles élményeket előnyben részesítő `Concierge` ügynök megkapja a javaslatot, felülvizsgálja azt, és visszajelzést ad, ami egy inkább helyi és kevésbé túlturistás alternatívát javasol.

#### Python Megvalósítás Elemzése

A Python példában először definiáljuk és létrehozzuk a két ügynököt, mindkettőt specifikus utasításokkal.

```python
# 01.python-agent-framework-workflow-ghmodel-basic.ipynb

# Ügynök szerepek és utasítások meghatározása
REVIEWER_NAME = "Concierge"
REVIEWER_INSTRUCTIONS = """
    You are a hotel concierge who has opinions about providing the most local and authentic experiences for travelers...
    """

FRONTDESK_NAME = "FrontDesk"
FRONTDESK_INSTRUCTIONS = """
    You are a Front Desk Travel Agent with ten years of experience and are known for brevity...
    """

# Ügynök példányok létrehozása
reviewer_agent = chat_client.as_agent(
    instructions=(REVIEWER_INSTRUCTIONS),
    name=REVIEWER_NAME,
)

front_desk_agent = chat_client.as_agent(
    instructions=(FRONTDESK_INSTRUCTIONS),
    name=FRONTDESK_NAME,
)
```

Ezután a `WorkflowBuilder` segít a gráf felépítésében. A `front_desk_agent` az indulópont, és hozzá kötünk egy élt, amely összekapcsolja a kimenetét a `reviewer_agent`-tel.

```python
# 01.python-ügynök-keretrendszer-munkafolyamat-ghmodell-alap.ipynb

workflow = WorkflowBuilder(start_executor=front_desk_agent).add_edge(front_desk_agent, reviewer_agent).build()
```

Végül a workflow futtatva lesz a kezdeti felhasználói bemenettel.

```python
# 01.python-agent-framework-workflow-ghmodel-basic.ipynb

result =''
# a run végrehajtja a munkafolyamatot; a get_outputs() visszaadja a kimeneti végrehajtó eredményét.
events = await workflow.run('I would like to go to Paris.')
outputs = events.get_outputs()
result = outputs[0].text if outputs else ''
```

#### .NET (C\#) Megvalósítás Elemzése

A .NET megvalósítás hasonló logikát követ. Először konstansokat definiál az ügynökök neveivel és utasításaival.

```csharp
// 01.dotnet-agent-framework-workflow-ghmodel-basic.ipynb

const string ReviewerAgentName = "Concierge";
const string ReviewerAgentInstructions = @"
    You are a hotel concierge who has opinions about providing the most local and authentic experiences for travelers...";

const string FrontDeskAgentName = "FrontDesk";
const string FrontDeskAgentInstructions = @"""
    You are a Front Desk Travel Agent with ten years of experience and are known for brevity...";
```

Az ügynökök egy `AzureOpenAIClient` (Responses API) segítségével jönnek létre, majd a `WorkflowBuilder` meghatározza a szekvenciális áramlást azzal, hogy egy élt ad a `frontDeskAgent`-től a `reviewerAgent`-hez.

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

A workflow ezután fut a felhasználó üzenetével, és az eredmény visszaáramlik.

### 2. Példa: Többlépcsős Szekvenciális Workflow

Ez a minta kiterjeszti az alapvető szekvenciát több ügynökre. Ideális olyan folyamatokhoz, amelyek többszörös finomítást vagy átalakítást igényelnek.

#### Forgatókönyv Háttér

Egy felhasználó beküld egy képet egy nappaliról és kér egy bútor árajánlatot.

1.  **Értékesítési Ügynök**: Azonosítja a képen lévő bútorokat és listát készít.
2.  **Árazási Ügynök**: Felveszi a listát és részletes ármegosztást ad, beleértve a költségvetési, középkategóriás és prémium opciókat.
3.  **Ajánlat Készítő Ügynök**: Megkapja az árakkal ellátott listát és formázza azt hivatalos ajánlat dokumentummá Markdown formátumban.

*Az Értékesítési -\> Árazási -\> Ajánlat munkafolyamat ábrája.*

#### Python Megvalósítás Elemzése

Három ügynök van definiálva, mindegyik specializált szereppel. A workflow `add_edge`-ek segítségével láncolódik: `sales_agent` -\> `price_agent` -\> `quote_agent`.

```python
# 02.python-agent-framework-workflow-ghmodel-sequential.ipynb

# Hozzon létre három specializált ügynököt
sales_agent = chat_client.as_agent(...)
price_agent = chat_client.as_agent(...)
quote_agent = chat_client.as_agent(...)

# Építse fel a sorrendben következő munkafolyamatot
workflow = WorkflowBuilder(start_executor=sales_agent).add_edge(sales_agent, price_agent).add_edge(price_agent, quote_agent).build()
```

A bemenet egy `ChatMessage`, amely tartalmazza a szöveget és a kép URI-jét. A keretrendszer biztosítja, hogy az egyes ügynökök kimenete a soron következőbe kerüljön, amíg el nem készül a végső ajánlat.

```python
# 02.python-agent-framework-workflow-ghmodel-sequential.ipynb

# A felhasználói üzenet tartalmaz szöveget és egy képet is
message = ChatMessage(
        role=Role.USER,
        contents=[
            TextContent(text="Please find the relevant furniture..."),
            DataContent(uri=image_uri, media_type="image/png")
        ]
)

# Futtassa a munkafolyamatot
events = await workflow.run(message)
```

#### .NET (C\#) Megvalósítás Elemzése

A .NET példa megfelel a Python verziónak. Három ügynök (`salesagent`, `priceagent`, `quoteagent`) jön létre. A `WorkflowBuilder` összekapcsolja őket szekvenciálisan.

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

A felhasználó üzenete tartalmazza a képadatokat (bájtokként) és a szöveges promptot. Az `InProcessExecution.RunStreamingAsync` metódus indítja a workflow-t, és a végeredményt a streamből kapjuk vissza.

### 3. Példa: Párhuzamos Workflow

Ez a minta akkor alkalmazandó, amikor a feladatokat egyidejűleg lehet végezni az idő megtakarítása érdekében. Ez egy „fan-out” folyamatot foglal magában több ügynökhöz, majd egy „fan-in” lépést az eredmények összesítésére.

#### Forgatókönyv Háttér

Egy felhasználó egy Seattle-i utazás tervezését kéri.

1.  **Kiosztó (Fan-Out)**: A felhasználó kérése egyszerre két ügynökhöz kerül.
2.  **Kutató Ügynök**: Kutatást végez a látnivalókról, időjárásról és fontos szempontokról Seattle-ben decemberben.
3.  **Tervező Ügynök**: Függetlenül elkészít egy részletes napi utazási tervet.
4.  **Összesítő (Fan-In)**: A kutató és a tervező kimeneteit összegyűjti és egyesíti, majd bemutatja a végső eredményeként.

*A párhuzamosan futó Kutató és Tervező workflow ábrája.*

#### Python Megvalósítás Elemzése

A `ConcurrentBuilder` leegyszerűsíti ennek a mintának a létrehozását. Csak fel kell sorolni a résztvevő ügynököket, és az építő automatikusan létrehozza a szükséges fan-out és fan-in logikát.

```python
# 03.python-agent-framework-workflow-ghmodel-concurrent.ipynb

research_agent = chat_client.as_agent(name="Researcher-Agent", ...)
plan_agent = chat_client.as_agent(name="Plan-Agent", ...)

# A ConcurrentBuilder kezeli a fan-out/fan-in logikát
workflow = ConcurrentBuilder().participants([research_agent, plan_agent]).build()

# Futtassa a munkafolyamatot
events = await workflow.run("Plan a trip to Seattle in December")
```

A keretrendszer biztosítja, hogy a `research_agent` és a `plan_agent` párhuzamosan fusson, és a végső kimeneteiket listába gyűjti.

#### .NET (C\#) Megvalósítás Elemzése

A .NET esetében ezt a mintát explicitabban kell definiálni. Egyedi végrehajtók (`ConcurrentStartExecutor` és `ConcurrentAggregationExecutor`) felelnek a fan-out és fan-in logika kezeléséért.

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

A `WorkflowBuilder` azután az `AddFanOutEdge` és `AddFanInEdge` metódusokkal építi fel a gráfot ezekkel az egyedi végrehajtókkal és az ügynökökkel.

```csharp
// 03.dotnet-agent-framework-workflow-ghmodel-concurrent.ipynb

var workflow = new WorkflowBuilder(startExecutor)
            .AddFanOutEdge(startExecutor, targets: [researcherAgent, plannerAgent])
            .AddFanInEdge(aggregationExecutor, sources: [researcherAgent, plannerAgent])
            .WithOutputFrom(aggregationExecutor)
            .Build();
```

### 4. Példa: Feltételes Workflow

A feltételes workflow-k elágazó logikát vezetnek be, lehetővé téve, hogy a rendszer különböző útvonalakat kövessen köztes eredmények alapján.

#### Forgatókönyv Háttér

Ez a workflow automatizálja egy technikai bemutató elkészítését és közzétételét.

1.  **Evangelista Ügynök**: Vázlat alapján és URL-ek segítségével megír egy tervezetet a bemutatóról.
2.  **Tartalom Ellenőrző Ügynök**: Felülvizsgálja a tervezetet. Ellenőrzi, hogy a szószám meghaladja-e a 200 szót.
3.  **Feltételes Ág**:
      * **Ha Jóváhagyva (`Igen`)**: A workflow a `Publisher-Agent` felé halad tovább.
      * **Ha Elutasítva (`Nem`)**: A workflow megáll, és kiírja az elutasítás okát.
4.  **Publikáló Ügynök**: Ha a tervezet jóváhagyásra kerül, ez az ügynök a tartalmat Markdown fájlba menti.

#### Python Megvalósítás Elemzése

Ez a példa egy egyedi `select_targets` függvényt használ a feltételes logika megvalósítására. Ezt a függvényt átadják az `add_multi_selection_edge_group` metódusnak, és ez irányítja a workflow-t a felülvizsgáló kimenetében található `review_result` mező alapján.

```python
# 04.python-agent-framework-workflow-aifoundry-condition.ipynb

# Ez a függvény az értékelés eredménye alapján határozza meg a következő lépést
def select_targets(review: ReviewResult, target_ids: list[str]) -> list[str]:
    handle_review_id, save_draft_id = target_ids
    if review.review_result == "Yes":
        # Ha jóváhagyott, folytassa a 'save_draft' végrehajtóval
        return [save_draft_id]
    else:
        # Ha elutasított, folytassa a 'handle_review' végrehajtóval a hiba jelentéséhez
        return [handle_review_id]

# A munkafolyamat-építő a kiválasztási függvényt használja az útválasztáshoz
workflow = (
    WorkflowBuilder()
        .set_start_executor(evangelist_agent)
        .add_edge(evangelist_agent, reviewer_agent)
        .add_edge(reviewer_agent, to_reviewer_result)
        # A többválasztásos él megvalósítja a feltételes logikát
        .add_multi_selection_edge_group(
            to_reviewer_result,
            [handle_review, save_draft],
            selection_func=select_targets,
        )
        .add_edge(save_draft, publisher_agent)
        .build()
)
```

Egyedi végrehajtók, például `to_reviewer_result` szolgálnak arra, hogy az ügynökök JSON kimenetét feldolgozzák és erősen típusos objektumokká alakítsák, amelyeket a kijelölő függvény ellenőrizhet.

#### .NET (C\#) Megvalósítás Elemzése

A .NET verzió hasonló megközelítést alkalmaz egy feltételfüggvénnyel. Egy `Func<object?, bool>` definícióval ellenőrzi a `ReviewResult` objektum `Result` tulajdonságát.

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

Az `AddEdge` metódus `condition` paramétere lehetővé teszi, hogy a `WorkflowBuilder` elágazó utat hozzon létre. A workflow csak akkor követi az utat a `publishExecutor` felé, ha a `GetCondition(expectedResult: "Yes")` igaz értéket ad vissza. Ellenkező esetben a `sendReviewerExecutor` irányába tart.

## Összefoglalás

A Microsoft Agent Framework Workflow robusztus és rugalmas alapot nyújt összetett, többügynökös rendszerek koordinálásához. Gráf-alapú architektúráját és alapelemeit kihasználva a fejlesztők kifinomult workflow-kat tervezhetnek és valósíthatnak meg Python és .NET környezetben egyaránt. Legyen az egyszerű szekvenciális feldolgozás, párhuzamos végrehajtás, vagy dinamikus feltételes logika, a keretrendszer eszközöket biztosít erőteljes, skálázható és típusbiztos MI-megoldások építéséhez.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Jogi nyilatkozat**:
Ez a dokumentum az AI fordítási szolgáltatás, a [Co-op Translator](https://github.com/Azure/co-op-translator) segítségével készült. Bár az pontosságra törekszünk, kérjük, vegye figyelembe, hogy az automatikus fordítások hibákat vagy pontatlanságokat tartalmazhatnak. Az eredeti dokumentum az anyanyelvén tekintendő hiteles forrásnak. Fontos információk esetén professzionális emberi fordítást javasolunk. Nem vállalunk felelősséget semmilyen félreértésért vagy téves értelmezésért, amely ebből a fordításból ered.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->