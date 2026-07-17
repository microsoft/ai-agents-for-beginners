# Daugiaagentinių programų kūrimas naudojant Microsoft Agent Framework Workflow

Šis pamokymas padės suprasti ir sukurti daugiaagentines programas naudojant Microsoft Agent Framework. Išnagrinėsime daugiaagentinių sistemų pagrindines sąvokas, panirsime į sistemos Workflow komponento architektūrą ir peržiūrėsime praktinius pavyzdžius tiek Python, tiek .NET kalbomis įvairiems procesų modeliams.

## 1\. Daugiaagentinių sistemų supratimas

Dirbtinio intelekto agentas yra sistema, kuri viršija standartinio didelio kalbos modelio (LLM) gebėjimus. Jis gali suvokti savo aplinką, priimti sprendimus ir imtis veiksmų, siekdamas konkrečių tikslų. Daugiaagentinė sistema apima kelis tokius agentus, kurie bendradarbiauja spręsdami problemą, kurią būtų sunku ar neįmanoma išspręsti vienam agentui.

### Dažni taikymo scenarijai

  * **Sudėtingų problemų sprendimas**: Didelio užduoties (pvz., įmonės renginio planavimo) skaidymas į mažesnes dalis, kurias atlieka specializuoti agentai (pvz., biudžeto agentas, logistikos agentas, rinkodaros agentas).
  * **Virtualūs asistentai**: Pagrindinis asistentas, deleguojantis užduotis, tokias kaip planavimas, tyrimai ir rezervacijos, kitiems specializuotiems agentams.
  * **Automatizuotas turinio kūrimas**: Procesas, kur vienas agentas rengia turinį, kitas peržiūri tikslumą ir toną, o trečias jį publikuoja.

### Daugiaagentinio bendradarbiavimo modeliai

Daugiaagentinės sistemos gali būti organizuotos pagal kelis modelius, kurie nusako, kaip jie tarpusavyje sąveikauja:

  * **Sekvenčių modelis**: Agentai dirba iš anksto nustatyta tvarka, tarsi surinkimo linijoje. Vieno agento išvestis tampa kito įvestimi.
  * **Lygiagretus modelis**: Agentai vienu metu dirba su skirtingomis užduoties dalimis, o jų rezultatai galiausiai apjungiami.
  * **Sąlyginis modelis**: Procesas vyksta skirtingais keliais, priklausomai nuo agentų išvesties, panašiai kaip if-then-else struktūra.

## 2\. Microsoft Agent Framework Workflow architektūra

Agent Framework workflow sistema yra pažangi orkestravimo sistema, skirta valdyti sudėtingas sąveikas tarp kelių agentų. Ji sukurta pagal grafų architektūrą, naudojančią [Pregel stiliaus vykdymo modelį](https://kowshik.github.io/JPregel/pregel_paper.pdf), kuriame apdorojimas vyksta sinchronizuotais žingsniais, vadinamais "supersteps".

### Pagrindiniai komponentai

Architektūra susideda iš trijų pagrindinių dalių:

1.  **Executoriai**: Tai pagrindiniai apdorojimo vienetai. Mūsų pavyzdžiuose `Agent` yra executoriumo tipas. Kiekvienas executoriumi gali turėti kelis žinučių tvarkytuvus, kurie automatiškai kviečiami pagal gautos žinutės tipą.
2.  **Briaunos (Edges)**: Nustato kelią, kuriuo žinutės keliauja tarp executoriumi. Briaunos gali turėti sąlygas, leidžiančias dinamiškai nukreipti informaciją per procesų grafą.
3.  **Workflow**: Šis komponentas koordinuoja visą procesą, valdydamas executoriumi, briaunas ir bendrą vykdymo srautą. Užtikrina, kad žinutės būtų apdorojamos teisinga tvarka ir srautina įvykius stebėjimui.

*Diagrama, iliustruojanti pagrindinius workflow sistemos komponentus.*

Ši struktūra leidžia kurti patikimas ir horizontaliai išplečiamas programas, naudojant pagrindinius modelius, kaip sekos grandinės, fan-out/fan-in lygiagretų apdorojimą ir switch-case logiką sąlyginiams srautams.

## 3\. Praktiniai pavyzdžiai ir kodo analizė

Dabar pažiūrėkime, kaip įgyvendinti skirtingus workflow modelius naudojant šį framework. Peržiūrėsime tiek Python, tiek .NET pavyzdžius kiekvienam atvejui.

### Atvejis 1: Pagrindinis sekveninis workflow

Tai paprasčiausias modelis, kai vieno agento išvestis perduodama tiesiogiai kitam. Mūsų scenarijuje yra viešbučio `FrontDesk` agentas, kuris pateikia kelionių rekomendaciją, o ją peržiūri `Concierge` agentas.

*Diagrama, atvaizduojanti bazinį FrontDesk -> Concierge workflow.*

#### Scenarijaus kontekstas

Keliautojas prašo rekomendacijos Paryžiuje.

1.  `FrontDesk` agentas, kuris siekia glaustumo, siūlo aplankyti Luvro muziejų.
2.  `Concierge` agentas, kuris vertina autentiškas patirtis, gauna šį pasiūlymą. Jis peržiūri rekomendaciją ir pateikia atsiliepimą, siūlydamas labiau vietinį, mažiau turistinį variantą.

#### Python įgyvendinimo analizė

Python pavyzdyje pirmiausia apibrėžiame ir sukuriame abu agentus su specifinėmis instrukcijomis.

```python
# 01.python-agent-framework-workflow-ghmodel-basic.ipynb

# Apibrėžkite agentų vaidmenis ir nurodymus
REVIEWER_NAME = "Concierge"
REVIEWER_INSTRUCTIONS = """
    You are a hotel concierge who has opinions about providing the most local and authentic experiences for travelers...
    """

FRONTDESK_NAME = "FrontDesk"
FRONTDESK_INSTRUCTIONS = """
    You are a Front Desk Travel Agent with ten years of experience and are known for brevity...
    """

# Sukurkite agentų egzempliorius
reviewer_agent = chat_client.as_agent(
    instructions=(REVIEWER_INSTRUCTIONS),
    name=REVIEWER_NAME,
)

front_desk_agent = chat_client.as_agent(
    instructions=(FRONTDESK_INSTRUCTIONS),
    name=FRONTDESK_NAME,
)
```

Toliau naudojame `WorkflowBuilder` grafui sudaryti. `front_desk_agent` nustatomas kaip pradžios taškas, o briauna sujungiama jo išvestį su `reviewer_agent`.

```python
# 01.python-agent-framework-workflow-ghmodel-basic.ipynb

workflow = WorkflowBuilder(start_executor=front_desk_agent).add_edge(front_desk_agent, reviewer_agent).build()
```

Galiausiai workflow paleidžiamas su pradiniu vartotojo užklausos tekstu.

```python
# 01.python-agent-framework-workflow-ghmodel-basic.ipynb

result =''
# run vykdo darbo eigą; get_outputs() grąžina rezultato vykdytojo išvestį.
events = await workflow.run('I would like to go to Paris.')
outputs = events.get_outputs()
result = outputs[0].text if outputs else ''
```

#### .NET (C#) įgyvendinimo analizė

.NET įgyvendinimas seka labai panašią logiką. Pirmiausia apibrėžiami agentų vardai ir instrukcijos.

```csharp
// 01.dotnet-agent-framework-workflow-ghmodel-basic.ipynb

const string ReviewerAgentName = "Concierge";
const string ReviewerAgentInstructions = @"
    You are a hotel concierge who has opinions about providing the most local and authentic experiences for travelers...";

const string FrontDeskAgentName = "FrontDesk";
const string FrontDeskAgentInstructions = @"""
    You are a Front Desk Travel Agent with ten years of experience and are known for brevity...";
```

Agentai kuriami naudojant `AzureOpenAIClient` (Responses API), o `WorkflowBuilder` apibrėžia sekveninį srautą pridedant briauną iš `frontDeskAgent` į `reviewerAgent`.

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

Workflow paleidžiamas su vartotojo žinute, o rezultatai srautu grąžinami atgal.

### Atvejis 2: Daugiaslavio sekveninis workflow

Šis modelis išplečia bazinę seką, įtraukiant daugiau agentų. Tinka procesams, kuriems reikia kelių etapų apdorojimo ar transformacijos.

#### Scenarijaus kontekstas

Vartotojas pateikia svetainės vaizdą ir prašo baldų kainos pasiūlymo.

1.  **Pardavimo agentas**: Nustato baldų elementus vaizde ir sudaro sąrašą.
2.  **Kainų agentas**: Priima sąrašą ir pateikia detalią kainų struktūrą, įskaitant biudžetinį, vidutinės klasės ir premium variantus.
3.  **Pasiūlymo agentas**: Gautą kainų sąrašą suformuoja į oficialų pasiūlymo dokumentą Markdown formatu.

*Diagrama, atvaizduojanti Sales -> Price -> Quote workflow.*

#### Python įgyvendinimo analizė

Apibrėžiami trys agentai, kiekvienas su specialia funkcija. Workflow konstruojamas naudojant `add_edge` sukuriant grandinę: `sales_agent` -> `price_agent` -> `quote_agent`.

```python
# 02.python-agent-framework-workflow-ghmodel-sequential.ipynb

# Sukurkite tris specializuotus agentus
sales_agent = chat_client.as_agent(...)
price_agent = chat_client.as_agent(...)
quote_agent = chat_client.as_agent(...)

# Sukurkite nuoseklų darbo srautą
workflow = WorkflowBuilder(start_executor=sales_agent).add_edge(sales_agent, price_agent).add_edge(price_agent, quote_agent).build()
```

Įvestis yra `ChatMessage`, apimanti tekstą ir vaizdo URI. Framework automatiškai perduoda kiekvieno agento išvestį į kitą sekoje, kol sugeneruojamas galutinis pasiūlymas.

```python
# 02.python-agent-framework-workflow-ghmodel-sequential.ipynb

# Vartotojo žinutėje yra ir tekstas, ir paveikslėlis
message = ChatMessage(
        role=Role.USER,
        contents=[
            TextContent(text="Please find the relevant furniture..."),
            DataContent(uri=image_uri, media_type="image/png")
        ]
)

# Vykdyti darbo eigą
events = await workflow.run(message)
```

#### .NET (C#) įgyvendinimo analizė

.NET versija atitinka Python pavyzdį. Sukuriami trys agentai (`salesagent`, `priceagent`, `quoteagent`), o `WorkflowBuilder` juos sujungia sekveniniu būdu.

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

Vartotojo žinutė sudaryta iš vaizdo duomenų (baitais) ir teksto užklausos. Metodas `InProcessExecution.RunStreamingAsync` paleidžia workflow, o galutinė išvestis gaunama iš srauto.

### Atvejis 3: Lygiagretus workflow

Šis modelis taikomas, kai užduotys gali būti vykdomos vienu metu siekiant taupyti laiką. Tai apima „fan-out“ keliems agentams ir „fan-in“ rezultatų sujungimą.

#### Scenarijaus kontekstas

Vartotojas prašo suplanuoti kelionę į Seattlę.

1.  **Dispečeris (Fan-Out)**: Vartotojo prašymas vienu metu nukreipiamas dviems agentams.
2.  **Tyrimų agentas**: Atliekami tyrimai apie lankytinas vietas, orą ir svarbius aspektus kelionei į Seattlę gruodį.
3.  **Plano agentas**: Nepriklausomai sudaro detalų dienos kelionės planą.
4.  **Agregatorius (Fan-In)**: Surenkami abiejų agentų rezultatai ir pateikiami kaip galutinis atsakymas.

*Diagrama, atvaizduojanti lygiagretų Researcher ir Planner workflow.*

#### Python įgyvendinimo analizė

`ConcurrentBuilder` supaprastina šio modelio kūrimą. Pakanka išvardinti dalyvaujančius agentus, ir builderis automatiškai sukuria reikalingą fan-out ir fan-in logiką.

```python
# 03.python-agent-framework-workflow-ghmodel-concurrent.ipynb

research_agent = chat_client.as_agent(name="Researcher-Agent", ...)
plan_agent = chat_client.as_agent(name="Plan-Agent", ...)

# ConcurrentBuilder valdo fan-out/fan-in logiką
workflow = ConcurrentBuilder().participants([research_agent, plan_agent]).build()

# Vykdyti darbo eigą
events = await workflow.run("Plan a trip to Seattle in December")
```

Framework užtikrina, kad `research_agent` ir `plan_agent` vykdytųsi lygiagrečiai, o jų rezultatai sujungiami į sąrašą.

#### .NET (C#) įgyvendinimo analizė

.NET versijoje šį modelį reikia apibrėžti aiškiau. Sukuriami specialūs executoriumi (`ConcurrentStartExecutor` ir `ConcurrentAggregationExecutor`) fan-out ir fan-in logikai valdyti.

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

Tada `WorkflowBuilder` naudoja `AddFanOutEdge` ir `AddFanInEdge`, kad sudarytų grafą su minėtais specialiais executoriumi ir agentais.

```csharp
// 03.dotnet-agent-framework-workflow-ghmodel-concurrent.ipynb

var workflow = new WorkflowBuilder(startExecutor)
            .AddFanOutEdge(startExecutor, targets: [researcherAgent, plannerAgent])
            .AddFanInEdge(aggregationExecutor, sources: [researcherAgent, plannerAgent])
            .WithOutputFrom(aggregationExecutor)
            .Build();
```

### Atvejis 4: Sąlyginis workflow

Sąlyginiai workflow pritaiko šakų logiką, leidžiančią sistemai pasirinkti skirtingus kelius pagal tarpinį rezultatą.

#### Scenarijaus kontekstas

Šis workflow automatizuoja techninio pamokymo kūrimą ir publikavimą.

1.  **Evangelistas-agentas**: Rašo pamokymo juodraštį pagal pateiktą planą ir nuorodas.
2.  **Turinio peržiūros agentas**: Peržiūri juodraštį. Patikrina, ar žodžių skaičius viršija 200.
3.  **Sąlyginė šaka**:
      * **Jei patvirtinta („Taip“) :** workflow tęsiasi prie `Publisher-Agent`.
      * **Jei atmesta („Ne“) :** workflow sustoja ir pateikia atmetimo priežastį.
4.  **Publisher-Agent**: Jei juodraštis patvirtintas, šis agentas išsaugo turinį Markdown faile.

#### Python įgyvendinimo analizė

Šiame pavyzdyje naudojama vartotojo funkcija `select_targets`, įgyvendinanti sąlyginę logiką. Ši funkcija perduodama `add_multi_selection_edge_group` ir nukreipia workflow pagal `review_result` lauką iš reviewer agento išvesties.

```python
# 04.python-agent-framework-workflow-aifoundry-condition.ipynb

# Ši funkcija nustato kitą žingsnį pagal peržiūros rezultatą
def select_targets(review: ReviewResult, target_ids: list[str]) -> list[str]:
    handle_review_id, save_draft_id = target_ids
    if review.review_result == "Yes":
        # Jei patvirtinta, tęskite prie vykdytojo 'save_draft'
        return [save_draft_id]
    else:
        # Jei atmesta, tęskite prie vykdytojo 'handle_review', kad praneštumėte apie nesėkmę
        return [handle_review_id]

# Darbo eigos kūrėjas naudoja pasirinkimo funkciją maršrutizavimui
workflow = (
    WorkflowBuilder()
        .set_start_executor(evangelist_agent)
        .add_edge(evangelist_agent, reviewer_agent)
        .add_edge(reviewer_agent, to_reviewer_result)
        # Daugiapakopė pasirinkimo briauna įgyvendina sąlyginę logiką
        .add_multi_selection_edge_group(
            to_reviewer_result,
            [handle_review, save_draft],
            selection_func=select_targets,
        )
        .add_edge(save_draft, publisher_agent)
        .build()
)
```

Specialūs executoriumi, tokie kaip `to_reviewer_result`, naudojami JSON išvesties iš agentų atskaitai ir konvertavimui į stipriai tipizuotus objektus, kuriuos funkicja gali analizuoti.

#### .NET (C#) įgyvendinimo analizė

.NET versija naudoja panašų metodą su sąlygos funkcija. Apibrėžiamas `Func<object?, bool>`, tikrinantis `ReviewResult` objekto `Result` savybę.

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

Metodas `AddEdge` su `condition` parametru leidžia `WorkflowBuilder` sukurti šakotą kelią. Workflow eis per briauną į `publishExecutor` tik jei sąlyga `GetCondition(expectedResult: "Yes")` grąžina true. Kitu atveju keliu eis į `sendReviewerExecutor`.

## Išvados

Microsoft Agent Framework Workflow suteikia tvirtą ir lankstų pagrindą sudėtingų daugiaagentinių sistemų orkestravimui. Pasinaudojant grafinės architektūros ir pagrindinių komponentų galimybėmis, programuotojai gali kurti ir įgyvendinti sudėtingus procesus tiek Python, tiek .NET aplinkoje. Nesvarbu, ar jūsų programa reikalauja paprasto sekveninio apdorojimo, lygiagretaus vykdymo ar dinaminės sąlyginės logikos, šis framework’as siūlo įrankius galingiems, skalabiliems ir tipams saugiems DI sprendimams kurti.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Atsakomybės apribojimas**:
Šis dokumentas buvo išverstas naudojant dirbtinio intelekto vertimo paslaugą [Co-op Translator](https://github.com/Azure/co-op-translator). Nors siekiame tikslumo, prašome atkreipti dėmesį, kad automatiniai vertimai gali turėti klaidų ar netikslumų. Originalus dokumentas jo gimtąja kalba laikomas autoritetingu šaltiniu. Svarbiai informacijai rekomenduojama naudoti profesionalų žmogiškąjį vertimą. Mes neatsakome už jokius nesusipratimus ar neteisingą interpretaciją, kilusią naudojantis šiuo vertimu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->