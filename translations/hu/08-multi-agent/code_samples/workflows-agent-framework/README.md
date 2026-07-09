# Többügynökös alkalmazások építése a Microsoft Agent Framework Workflow-jával

Ez az útmutató végigvezeti Önt a többügynökös alkalmazások megértésén és építésén a Microsoft Agent Framework használatával. Felfedezzük a többügynökös rendszerek alapvető fogalmait, mélyebben megvizsgáljuk a keretrendszer Workflow komponensének architektúráját, és gyakorlati példákon keresztül megmutatjuk, hogyan valósíthatók meg különböző workflow minták Python és .NET nyelven.

## 1\. A többügynökös rendszerek megértése

Egy AI Agent olyan rendszer, amely túlmutat egy szabványos nagy nyelvi modell (LLM) képességein. Képes érzékelni a környezetét, döntéseket hozni, és cselekedni egyedi célok elérése érdekében. A többügynökös rendszer több ilyen ügynök együttműködését jelenti egy olyan probléma megoldására, amelyet egyetlen ügynök nehezen vagy egyáltalán nem tudna egyedül kezelni.

### Gyakori alkalmazási forgatókönyvek

  * **Összetett problémamegoldás**: Egy nagy feladat (pl. vállalati rendezvény megszervezése) felosztása kisebb részfeladatokra, amelyeket specializált ügynökök végeznek (pl. költségvetési ügynök, logisztikai ügynök, marketing ügynök).
  * **Virtuális asszisztensek**: Egy fő asszisztens ügynök, amely feladatokat delegál, mint például időpont-egyeztetés, kutatás és foglalás más specializált ügynököknek.
  * **Automatizált tartalomkészítés**: Egy workflow, ahol az egyik ügynök tartalmat készít, egy másik ellenőrzi annak pontosságát és stílusát, egy harmadik pedig publikálja azt.

### Többügynökös minták

A többügynökös rendszerek többféle mintában szervezhetők, amelyek meghatározzák az interakciójuk módját:

  * **Szekvenciális**: Az ügynökök előre meghatározott sorrendben dolgoznak, mint egy összeszerelő sor. Az egyik ügynök kimenete a következő bemenete lesz.
  * **Párhuzamos**: Az ügynökök párhuzamosan dolgoznak a feladat különböző részein, és eredményeik a végén összesítődnek.
  * **Feltételes**: A workflow különböző útvonalakat követ az ügynök kimenete alapján, hasonlóan egy if-then-else szerkezethez.

## 2\. A Microsoft Agent Framework Workflow architektúrája

Az Agent Framework workflow rendszere egy fejlett koordinációs motor, amely több ügynök közötti összetett interakciók kezelésére szolgál. Egy gráf-alapú architektúrán alapul, amely egy [Pregel-stílusú végrehajtási modellt](https://kowshik.github.io/JPregel/pregel_paper.pdf) használ, ahol a feldolgozás szinkronizált lépésekben, úgynevezett "superstep"-ekben történik.

### Fő komponensek

Az architektúra három fő részből áll:

1.  **Végrehajtók**: Ezek az alapvető feldolgozó egységek. Példáinkban az `Agent` egy ilyen végrehajtó típus. Minden végrehajtónak lehet több üzenetkezelője, amelyek a kapott üzenet típusától függően automatikusan meghívódnak.
2.  **Élek**: Meghatározzák az üzenetek útját a végrehajtók között. Az élekhez feltételek rendelhetők, amelyek dinamikus útválasztást tesznek lehetővé a workflow gráfban.
3.  **Workflow**: Ez a komponens koordinálja az egész folyamatot, kezeli a végrehajtókat, az éleket és a végrehajtás teljes menetét. Biztosítja, hogy az üzenetek helyes sorrendben kerüljenek feldolgozásra és eseményeket továbbít a megfigyelés céljára.

*Egy ábra a workflow rendszer fő komponenseiről.*

Ez a struktúra lehetővé teszi robosztus és skálázható alkalmazások építését alapvető minták felhasználásával, mint a szekvenciális láncok, fan-out/fan-in párhuzamos feldolgozás, valamint feltételes switch-case logika.

## 3\. Gyakorlati példák és kódelemzés

Most nézzük meg, hogyan valósíthatók meg különböző workflow minták a keretrendszer segítségével. Minden példát bemutatunk Python és .NET kóddal.

### 1. eset: Egyszerű szekvenciális workflow

Ez a legegyszerűbb minta, ahol az egyik ügynök kimenetét közvetlenül átadjuk a másiknak. Forgatókönyvünkben egy szállodai `FrontDesk` ügynök utazási ajánlást tesz, amelyet egy `Concierge` ügynök felülvizsgál.

*Az alapvető FrontDesk -> Concierge workflow ábrája.*

#### Forgatókönyv háttere

Egy utazó Párizsban kér ajánlást.

1.  A tömörségre tervezett `FrontDesk` ügynök azt javasolja, hogy látogassák meg a Louvre Múzeumot.
2.  A hiteles élményeket előnyben részesítő `Concierge` ügynök megkapja ezt az ajánlást, átnézi, visszajelzést ad, és egy helyibb, kevésbé turista alternatívát javasol.

#### Python megvalósítás elemzése

A Python példában először definiáljuk és létrehozzuk a két ügynököt, mindegyiket egyedi utasításokkal.

```python
# 01.python-agent-framework-workflow-ghmodel-basic.ipynb

# Ügynök szerepkörök és utasítások meghatározása
REVIEWER_NAME = "Concierge"
REVIEWER_INSTRUCTIONS = """
    You are an are hotel concierge who has opinions about providing the most local and authentic experiences for travelers...
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

Ezután a `WorkflowBuilder`-rel építjük fel a gráfot. A `front_desk_agent` az indulópont, és egy él jön létre, amely összeköti a kimenetét a `reviewer_agent`-tel.

```python
# 01.python-agent-framework-munkafolyamat-ghmodel-alap.ipynb

workflow = WorkflowBuilder(start_executor=front_desk_agent).add_edge(front_desk_agent, reviewer_agent).build()
```

Végül a workflow a kezdeti felhasználói üzenettel kerül végrehajtásra.

```python
# 01.python-agent-framework-workflow-ghmodel-basic.ipynb

result =''
# a run végrehajtja a munkafolyamatot; a get_outputs() visszaadja a kimeneti végrehajtó eredményét.
events = await workflow.run('I would like to go to Paris.')
outputs = events.get_outputs()
result = outputs[0].text if outputs else ''
```

#### .NET (C#) megvalósítás elemzése

A .NET megvalósítás nagyon hasonló logikát követ. Először konstansokat definiálunk az ügynökök neveihez és instrukcióihoz.

```csharp
// 01.dotnet-agent-framework-workflow-ghmodel-basic.ipynb

const string ReviewerAgentName = "Concierge";
const string ReviewerAgentInstructions = @"
    You are an are hotel concierge who has opinions about providing the most local and authentic experiences for travelers...";

const string FrontDeskAgentName = "FrontDesk";
const string FrontDeskAgentInstructions = @"""
    You are a Front Desk Travel Agent with ten years of experience and are known for brevity...";
```

Az ügynökök egy `AzureOpenAIClient` (Responses API) segítségével jönnek létre, majd a `WorkflowBuilder` egy él hozzáadásával határozza meg a szekvenciális folyamatot a `frontDeskAgent` és a `reviewerAgent` között.

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

A workflow ezután a felhasználói üzenettel fut, és az eredmények streamelve érkeznek vissza.

### 2. eset: Többlépéses szekvenciális workflow

Ez a minta kibővíti az alap szekvenciát további ügynökökkel. Ideális olyan folyamatokhoz, amelyek több szakaszból álló finomítást vagy átalakítást igényelnek.

#### Forgatókönyv háttere

Egy felhasználó egy nappali képét adja meg, és bútordíjat kér.

1.  **Értékesítési ügynök**: Azonosítja a képen szereplő bútorokat, és listát készít.
2.  **Ár-ügynök**: A tételek listája alapján részletes árkalkulációt ad, beleértve a költségvetési, középkategóriás és prémium opciókat.
3.  **Ajánlat-ügynök**: Megkapja az árazott listát, és formázza azt hivatalos ajánlat dokumentummá Markdown formátumban.

*Az Értékesítés -> Ár -> Ajánlat workflow ábrája.*

#### Python megvalósítás elemzése

Három ügynök definiálása történik, mindegyik specializált szerepkörrel. A workflow `add_edge` használatával láncolva van: `sales_agent` -> `price_agent` -> `quote_agent`.

```python
# 02.python-agent-framework-workflow-ghmodel-sequential.ipynb

# Három specializált ügynök létrehozása
sales_agent = chat_client.as_agent(...)
price_agent = chat_client.as_agent(...)
quote_agent = chat_client.as_agent(...)

# A szekvenciális munkafolyamat felépítése
workflow = WorkflowBuilder(start_executor=sales_agent).add_edge(sales_agent, price_agent).add_edge(price_agent, quote_agent).build()
```

A bemenet egy `ChatMessage`, amely tartalmazza a szöveget és a kép URI-ját. A keretrendszer gondoskodik arról, hogy az egyes ügynökök kimenete átadásra kerüljön a következőnek, amíg a végső ajánlat létrejön.

```python
# 02.python-agent-framework-workflow-ghmodel-sequential.ipynb

# A felhasználói üzenet szöveget és képet is tartalmaz
message = ChatMessage(
        role=Role.USER,
        contents=[
            TextContent(text="Please find the relevant furniture..."),
            DataContent(uri=image_uri, media_type="image/png")
        ]
)

# Futtasd a munkafolyamatot
events = await workflow.run(message)
```

#### .NET (C#) megvalósítás elemzése

A .NET példa a Python verzió tükrözése. Három ügynök (`salesagent`, `priceagent`, `quoteagent`) jön létre. A `WorkflowBuilder` összekapcsolja őket szekvenciálisan.

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

A felhasználói üzenet képadatokat (bájtként) és szöveges promptot is tartalmaz. Az `InProcessExecution.StreamAsync` metódus indítja el a workflow-t, a végső kimenet pedig a streamből kerül kiolvasásra.

### 3. eset: Párhuzamos workflow

Ezt a mintát akkor használjuk, amikor a feladatok egyidejű végrehajtása időt takarít meg. Egy "fan-out" több ügynökhöz és egy "fan-in" az eredmények összesítéséhez tartozik.

#### Forgatókönyv háttere

Egy felhasználó Seattli utazás tervezését kéri.

1.  **Kiosztó (Fan-Out)**: A felhasználó kérését két ügynöknek egyszerre küldjük.
2.  **Kutató-ügynök**: Kutatja a látnivalókat, időjárást és fontos szempontokat Seattle körül decemberben.
3.  **Tervező-ügynök**: Függetlenül elkészíti a részletes, napokra bontott utazási tervet.
4.  **Összesítő (Fan-In)**: Mindkét kutató és tervező kimenetét begyűjti és együttesen mutatja be a végeredményt.

*A párhuzamos Kutató és Tervező workflow ábrája.*

#### Python megvalósítás elemzése

A `ConcurrentBuilder` megkönnyíti ennek a mintának az elkészítését. Csak felsoroljuk a részt vevő ügynököket, és a builder automatikusan létrehozza a szükséges fan-out és fan-in logikát.

```python
# 03.python-agent-framework-workflow-ghmodel-concurrent.ipynb

research_agent = chat_client.as_agent(name="Researcher-Agent", ...)
plan_agent = chat_client.as_agent(name="Plan-Agent", ...)

# A ConcurrentBuilder kezeli a szétosztás/összefogás logikáját
workflow = ConcurrentBuilder().participants([research_agent, plan_agent]).build()

# Futtasd a munkafolyamatot
events = await workflow.run("Plan a trip to Seattle in December")
```

A keretrendszer biztosítja, hogy a `research_agent` és `plan_agent` párhuzamosan fussanak, és végső eredményeik listaként kerülnek összegyűjtésre.

#### .NET (C#) megvalósítás elemzése

A .NET-ben ez a minta explicitebb definíciót igényel. Egyedi végrehajtók (`ConcurrentStartExecutor` és `ConcurrentAggregationExecutor`) kezeli a fan-out és fan-in logikát.

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

A `WorkflowBuilder` ezt követően az `AddFanOutEdge` és `AddFanInEdge` metódusokat használja, hogy a gráfot ezekkel az egyedi végrehajtókkal és az ügynökökkel megépítse.

```csharp
// 03.dotnet-agent-framework-workflow-ghmodel-concurrent.ipynb

var workflow = new WorkflowBuilder(startExecutor)
            .AddFanOutEdge(startExecutor, targets: [researcherAgent, plannerAgent])
            .AddFanInEdge(aggregationExecutor, sources: [researcherAgent, plannerAgent])
            .WithOutputFrom(aggregationExecutor)
            .Build();
```

### 4. eset: Feltételes workflow

A feltételes workflow-k elágazó logikát vezetnek be, amely lehetővé teszi, hogy a rendszer közbülső eredmények alapján különböző útvonalakat kövessen.

#### Forgatókönyv háttere

Ez a workflow egy technikai oktatóanyag létrehozását és közzétételét automatizálja.

1.  **Evangelista-ügynök**: Vázlatot ír az oktatóanyaghoz egy adott vázlat és URL-ek alapján.
2.  **Tartalomellenőr-ügynök**: Átvizsgálja a vázlatot. Ellenőrzi, hogy a szószám meghaladja-e a 200 szót.
3.  **Feltételes elágazás**:
      * **Ha elfogadva (`Igen`)**: A workflow folytatódik a `Publisher-Agent` irányába.
      * **Ha elutasítva (`Nem`)**: A workflow leáll és visszaadja az elutasítás okát.
4.  **Kiadó-ügynök**: Ha a vázlat elfogadott, ez az ügynök menti a tartalmat Markdown fájlba.

#### Python megvalósítás elemzése

Ez a példa egy egyedi `select_targets` függvényt használ a feltételes logika megvalósítására. Ezt a függvényt átadjuk az `add_multi_selection_edge_group`-nek, és a `review_result` mező alapján irányítja a workflow-t a felügyelő kimenetéből.

```python
# 04.python-agent-framework-workflow-aifoundry-condition.ipynb

# Ez a függvény határozza meg a következő lépést az értékelési eredmény alapján
def select_targets(review: ReviewResult, target_ids: list[str]) -> list[str]:
    handle_review_id, save_draft_id = target_ids
    if review.review_result == "Yes":
        # Ha jóváhagyott, lépjen tovább a 'save_draft' végrehajtóra
        return [save_draft_id]
    else:
        # Ha elutasították, lépjen tovább a 'handle_review' végrehajtóra a hiba jelentéséhez
        return [handle_review_id]

# A munkafolyamat-készítő az útválasztáshoz kiválasztási függvényt használ
workflow = (
    WorkflowBuilder()
        .set_start_executor(evangelist_agent)
        .add_edge(evangelist_agent, reviewer_agent)
        .add_edge(reviewer_agent, to_reviewer_result)
        # A többszörös kiválasztású él megvalósítja a feltételes logikát
        .add_multi_selection_edge_group(
            to_reviewer_result,
            [handle_review, save_draft],
            selection_func=select_targets,
        )
        .add_edge(save_draft, publisher_agent)
        .build()
)
```

Egyedi végrehajtók, mint a `to_reviewer_result` használatosak arra, hogy az ügynökök JSON kimenetét erősen típusos objektumokká alakítsák, amelyeket a kiválasztó függvény vizsgálhat.

#### .NET (C#) megvalósítás elemzése

A .NET verzió hasonló megközelítést alkalmaz feltételes függvénnyel. Egy `Func<object?, bool>`-t definiálnak, amely ellenőrzi a `ReviewResult` objektum `Result` tulajdonságát.

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

Az `AddEdge` metódus `condition` paramétere lehetővé teszi, hogy a `WorkflowBuilder` elágazó utat hozzon létre. A workflow csak akkor követi a `publishExecutor`-hez vezető ágat, ha a `GetCondition(expectedResult: "Yes")` feltétel igaz. Egyébként a `sendReviewerExecutor` irányába halad.

## Következtetés

A Microsoft Agent Framework Workflow robosztus és rugalmas alapot biztosít összetett, többügynökös rendszerek összehangolására. A gráf-alapú architektúra és a fő komponensek kihasználásával a fejlesztők kifinomult workflow-kat tervezhetnek és valósíthatnak meg Pythonban és .NET-ben egyaránt. Akár egyszerű szekvenciális feldolgozásra, párhuzamos végrehajtásra vagy dinamikus feltételes logikára van szükség, a keretrendszer eszközöket kínál erős, skálázható és típusbiztos, AI-alapú megoldások létrehozásához.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Jogi nyilatkozat**:
Ez a dokumentum az AI fordítási szolgáltatás, a [Co-op Translator](https://github.com/Azure/co-op-translator) segítségével készült. Bár az pontosságra törekszünk, kérjük, vegye figyelembe, hogy az automatikus fordítások hibákat vagy pontatlanságokat tartalmazhatnak. Az eredeti dokumentum az anyanyelvén tekintendő hiteles forrásnak. Fontos információk esetén professzionális emberi fordítást javasolunk. Nem vállalunk felelősséget semmilyen félreértésért vagy téves értelmezésért, amely ebből a fordításból ered.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->