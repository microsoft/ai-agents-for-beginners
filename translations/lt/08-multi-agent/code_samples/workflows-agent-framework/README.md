# Daugiaprogramių programų kūrimas su Microsoft Agent Framework Workflow

Ši pamoka padės jums suprasti ir sukurti daugiaprogrames programas, naudojant Microsoft Agent Framework. Mes išnagrinėsime daugiaprogramių sistemų pagrindines sąvokas, gilinsimės į sistemos Workflow komponento architektūrą ir pereisime praktinius pavyzdžius tiek Python, tiek .NET kalbomis, skirtingiems darbo srautų modeliams.

## 1\. Daugiaprogramių sistemų supratimas

AI agentas yra sistema, kuri viršija standartinio didelio kalbos modelio (LLM) galimybes. Ji gali suvokti savo aplinką, priimti sprendimus ir imtis veiksmų siekiant konkrečių tikslų. Daugiaprogramių sistema apima keletą tokių agentų, bendradarbiaujančių sprendžiant problemą, kuri vienam agentui būtų sunkiai arba neįmanoma išspręsti savarankiškai.

### Įprasti taikymo scenarijai

  * **Sudėtingų problemų sprendimas**: Didelio uždavinio (pvz., įmonės masto renginio planavimo) suskaidymas į mažesnes užduotis, kurias atlieka specializuoti agentai (pvz., biudžeto agentas, logistikos agentas, rinkodaros agentas).
  * **Virtualūs asistentai**: Pagrindinis asistento agentas deleguoja užduotis, tokias kaip tvarkaraščio sudarymas, tyrimai ir rezervavimas, kitiems specializuotiems agentams.
  * **Automatizuotas turinio kūrimas**: Darbo srautas, kai vienas agentas rengia turinį, kitas jį peržiūri dėl tikslumo ir tono, o trečias publikuoja.

### Daugiaprogramių modeliai

Daugiaprogramės sistemos gali būti organizuotos pagal kelis modelius, kurie nusako, kaip jos sąveikauja:

  * **Sekos**: Agentai dirba iš anksto nustatyta tvarka, panašiai kaip surinkimo linijoje. Vieno agente gautas rezultatas tampa įvestimi kitam.
  * **Lygiagretūs**: Agentai vienu metu dirba skirtingomis užduoties dalimis, o jų rezultatai sujungiami pabaigoje.
  * **Sąlyginiai**: Darbo srautas seka skirtingus kelius, priklausomai nuo agente gauto rezultato, panašiai kaip if-then-else sakinys.

## 2\. Microsoft Agent Framework Workflow architektūra

Agent Framework darbo srautų sistema yra pažangi suderinimo variklis, skirtas valdyti sudėtingą sąveiką tarp kelių agentų. Ji sukurta ant grafu paremtos architektūros, naudojančios [Pregel tipo vykdymo modelį](https://kowshik.github.io/JPregel/pregel_paper.pdf), kur apdorojimas vyksta sinchronizuotomis žingsnių grupėmis, vadinamomis „superžingsniais“.

### Pagrindiniai komponentai

Architektūra sudaryta iš trijų pagrindinių dalių:

1.  **Vykdytojai (Executors)**: Tai pagrindiniai apdorojimo vienetai. Mūsų pavyzdžiuose `Agent` yra vykdytojo tipas. Kiekvienas vykdytojas gali turėti kelis žinučių apdorojimo tvarkyklius, kurie automatiškai kviečiami pagal gautų žinučių tipą.
2.  **Briaunos (Edges)**: Jos apibrėžia žinučių kelią tarp vykdytojų. Briaunos gali turėti sąlygas, leidžiančias dinamiškai nukreipti informaciją per darbo srautų grafiką.
3.  **Darbo srautas (Workflow)**: Šis komponentas koordinuoja visą procesą, valdydamas vykdytojus, briaunas ir bendrą vykdymo eigą. Užtikrina, kad žinutės būtų apdorojamos teisinga tvarka ir transliuoja įvykius stebimumui.

*Diagrama, vaizduojanti darbo srautų sistemos pagrindinius komponentus.*

Ši struktūra leidžia kurti tvirtas ir mastelio keitimo galimybes turinčias programas, naudojant pagrindinius modelius, tokius kaip sekvinės grandinės, fan-out/fan-in lygiagrečiam apdorojimui ir switch-case logiką sąlyginiams srautams.

## 3\. Praktiniai pavyzdžiai ir kodo analizė

Dabar pažvelkime, kaip įgyvendinti skirtingus darbo srautų modelius naudojant šią sistemą. Aptarsime tiek Python, tiek .NET kodo pavyzdžius kiekvienam pavyzdžiui.

### Atvejis 1: Pagrindinis sekos darbo srautas

Tai paprasčiausias modelis, kai vieno agente pagamintas rezultatas tiesiogiai perduodamas kitam. Mūsų scenarijuje yra viešbučio `FrontDesk` agentas, pateikiantis kelionių rekomendaciją, kurią vėliau peržiūri `Concierge` agentas.

*Pagrindinio FrontDesk -> Concierge darbo srauto diagrama.*

#### Scenarijaus fonas

Keliautojas prašo rekomendacijos Paryžiuje.

1.  `FrontDesk` agentas, orientuotas į trumpumą, siūlo aplankyti Luvro muziejų.
2.  `Concierge` agentas, kuris vertina autentiškas patirtis, gauna šį pasiūlymą, peržiūri rekomendaciją ir pateikia atsiliepimą, siūlydamas vietinį, mažiau turistinį alternatyvų variantą.

#### Python įgyvendinimo analizė

Python pavyzdyje pirmiausia apibrėžiame ir sukuriame du agentus, kiekvienas su konkrečiomis instrukcijomis.

```python
# 01.python-agent-framework-workflow-ghmodel-basic.ipynb

# Apibrėžkite agentų vaidmenis ir instrukcijas
REVIEWER_NAME = "Concierge"
REVIEWER_INSTRUCTIONS = """
    You are an are hotel concierge who has opinions about providing the most local and authentic experiences for travelers...
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

Toliau `WorkflowBuilder` naudojamas grafui konstrukcijai. `front_desk_agent` nustatomas kaip pradžios taškas, ir sukuriama briauna, jungiant jo išvestį su `reviewer_agent`.

```python
# 01.python-agent-framework-darbo eiga-ghmodel-pagrindinis.ipynb

workflow = WorkflowBuilder(start_executor=front_desk_agent).add_edge(front_desk_agent, reviewer_agent).build()
```

Galiausiai darbo srautas vykdomas su pradiniu naudotojo užklausa.

```python
# 01.python-agent-framework-workflow-ghmodel-basic.ipynb

result =''
# run vykdo darbo eigą; get_outputs() grąžina vykdytojo rezultatą.
events = await workflow.run('I would like to go to Paris.')
outputs = events.get_outputs()
result = outputs[0].text if outputs else ''
```

#### .NET (C\#) įgyvendinimo analizė

.NET įgyvendinimas seka labai panašia logika. Pirmiausia apibrėžiami konstantai agentų vardams ir instrukcijoms.

```csharp
// 01.dotnet-agent-framework-workflow-ghmodel-basic.ipynb

const string ReviewerAgentName = "Concierge";
const string ReviewerAgentInstructions = @"
    You are an are hotel concierge who has opinions about providing the most local and authentic experiences for travelers...";

const string FrontDeskAgentName = "FrontDesk";
const string FrontDeskAgentInstructions = @"""
    You are a Front Desk Travel Agent with ten years of experience and are known for brevity...";
```

Agentai sukuriami naudojant `AzureOpenAIClient` (Responses API), tada `WorkflowBuilder` apibrėžia sekos srautą pridėdamas briauną nuo `frontDeskAgent` iki `reviewerAgent`.

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

Darbo srautas vykdomas su naudotojo žinute, o rezultatai perduodami transliacijos būdu.

### Atvejis 2: Daugiažingsnis sekos darbo srautas

Šis modelis praplečia pagrindinę seką, įtraukiant daugiau agentų. Idealus procesams, kuriems reikalingi keli tobulinimo ar transformacijos etapai.

#### Scenarijaus fonas

Vartotojas pateikia gyvenamojo kambario nuotrauką ir prašo baldų kainos pasiūlymo.

1.  **Pardavimų agentas**: Nustato baldų elementus nuotraukoje ir sudaro sąrašą.
2.  **Kainų agentas**: Remdamasis sąrašu pateikia detalią kainų suvestinę – biudžetinė, vidutinė ir premium kainų grupės.
3.  **Pasiūlymo agentas**: Priima įkainuotą sąrašą ir pateikia jį formalioje pasiūlymo dokumento formoje Markdown formatu.

*Pardavimų -> Kainų -> Pasiūlymo darbo srauto diagrama.*

#### Python įgyvendinimo analizė

Apibrėžiami trys agentai, kiekvienas su specializuota funkcija. Darbo srautas sukuriamas naudojant `add_edge` briaunas grandinės forma: `sales_agent` -> `price_agent` -> `quote_agent`.

```python
# 02.python-agent-framework-workflow-ghmodel-sequential.ipynb

# Sukurkite tris specializuotus agentus
sales_agent = chat_client.as_agent(...)
price_agent = chat_client.as_agent(...)
quote_agent = chat_client.as_agent(...)

# Sukurkite seką vykdomą darbo eigą
workflow = WorkflowBuilder(start_executor=sales_agent).add_edge(sales_agent, price_agent).add_edge(price_agent, quote_agent).build()
```

Įvestis yra `ChatMessage`, kuriame yra teksto užklausa ir paveikslėlio URI. Sistema perduoda kiekvieno agente rezultatą kitam tol, kol sugeneruojamas galutinis pasiūlymas.

```python
# 02.python-agent-framework-workflow-ghmodel-sequential.ipynb

# Vartotojo žinutė turi tiek tekstą, tiek paveikslėlį
message = ChatMessage(
        role=Role.USER,
        contents=[
            TextContent(text="Please find the relevant furniture..."),
            DataContent(uri=image_uri, media_type="image/png")
        ]
)

# Paleisti darbo eigą
events = await workflow.run(message)
```

#### .NET (C\#) įgyvendinimo analizė

.NET pavyzdyje analogiškai sukuriami trys agentai (`salesagent`, `priceagent`, `quoteagent`). `WorkflowBuilder` sujungia juos sekos tvarka.

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

Vartotojo žinutė sudaroma su vaizdo duomenimis (baitais) ir teksto užklausa. Metodas `InProcessExecution.StreamAsync` pradeda darbo srautą, o galutinis rezultatas gaunamas iš transliacijos.

### Atvejis 3: Lygiagretusis darbo srautas

Šis modelis naudojamas, kai užduotys gali būti atliekamos vienu metu, sutaupant laiko. Jame taikomas „fan-out“ keliems agentams ir „fan-in“ rezultatų sujungimui.

#### Scenarijaus fonas

Vartotojas prašo suplanuoti kelionę į Sietlą.

1.  **Paskirstytojas (Fan-Out)**: Vartotojo užklausa siunčiama dviem agentams vienu metu.
2.  **Tyrimų agentas**: Atlieka tyrimus apie lankytinas vietas, orą ir svarbias kelionės į Sietlą gruodį detales.
3.  **Planuotojo agentas**: Savarankiškai rengia išsamų kasdienės kelionės maršrutą.
4.  **Sujungėjas (Fan-In)**: Surenka abiejų agentų rezultatus ir pateikia juos kaip galutinį atsakymą.

*Lygiagretaus Tyrėjo ir Planuotojo darbo srauto diagrama.*

#### Python įgyvendinimo analizė

`ConcurrentBuilder` palengvina šio modelio kūrimą. Tiesiog nurodote dalyvius agentus, o builderis automatiškai sukuria reikalingą fan-out ir fan-in logiką.

```python
# 03.python-agent-framework-workflow-ghmodel-concurrent.ipynb

research_agent = chat_client.as_agent(name="Researcher-Agent", ...)
plan_agent = chat_client.as_agent(name="Plan-Agent", ...)

# ConcurrentBuilder tvarko fan-out/fan-in logiką
workflow = ConcurrentBuilder().participants([research_agent, plan_agent]).build()

# Paleiskite darbo eigą
events = await workflow.run("Plan a trip to Seattle in December")
```

Sistema užtikrina, kad `research_agent` ir `plan_agent` veiks lygiagrečiai, o jų galutiniai rezultatai bus surinkti į sąrašą.

#### .NET (C\#) įgyvendinimo analizė

.NET šis modelis reikalauja aiškesnio apibrėžimo. Sukuriami specialūs vykdytojai (`ConcurrentStartExecutor` ir `ConcurrentAggregationExecutor`), kurie valdo fan-out ir fan-in logiką.

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

Tada `WorkflowBuilder` naudoja `AddFanOutEdge` ir `AddFanInEdge`, kad sudarytų grafiką su tais vykdytojais ir agentais.

```csharp
// 03.dotnet-agent-framework-workflow-ghmodel-concurrent.ipynb

var workflow = new WorkflowBuilder(startExecutor)
            .AddFanOutEdge(startExecutor, targets: [researcherAgent, plannerAgent])
            .AddFanInEdge(aggregationExecutor, sources: [researcherAgent, plannerAgent])
            .WithOutputFrom(aggregationExecutor)
            .Build();
```

### Atvejis 4: Sąlyginis darbo srautas

Sąlyginiai darbo srautai įveda šakojimosi logiką, leidžiančią sistemai eiti skirtingais keliais, priklausomai nuo tarpinio rezultato.

#### Scenarijaus fonas

Šis darbo srautas automatizuoja techninio mokymo kurso kūrimą ir publikavimą.

1.  **Evangelistas-agentas**: Rašo mokymo kursų juodraštį pagal pateiktą planą ir URL.
2.  **Turinio peržiūros agentas**: Peržiūri juodraštį. Patikrina, ar žodžių skaičius viršija 200 žodžių.
3.  **Sąlyginis šakos pasirinkimas**:
      * **Jei patvirtinta („Taip“) :** Darbo srautas tęsiasi su `Publisher-Agent`.
      * **Jei atmesta („Ne“) :** Darbo srautas sustoja ir pateikia atmetimo priežastį.
4.  **Publikavimo agentas**: Jei juodraštis patvirtintas, šis agentas įrašo turinį į Markdown failą.

#### Python įgyvendinimo analizė

Šiame pavyzdyje naudojama speciali funkcija `select_targets`, įgyvendinanti sąlyginę logiką. Funkcija perduodama `add_multi_selection_edge_group` ir nukreipia darbo srautą pagal peržiūros rezultato lauką `review_result` iš peržiūros agente išvesties.

```python
# 04.python-agent-framework-workflow-aifoundry-condition.ipynb

# Ši funkcija nustato kitą veiksmą pagal peržiūros rezultatą
def select_targets(review: ReviewResult, target_ids: list[str]) -> list[str]:
    handle_review_id, save_draft_id = target_ids
    if review.review_result == "Yes":
        # Jei patvirtinta, tęskite 'save_draft' vykdytoją
        return [save_draft_id]
    else:
        # Jei atmesta, tęskite 'handle_review' vykdytoją, kad praneštumėte apie nesėkmę
        return [handle_review_id]

# Darbo eigos kūrėjas naudoja atrankos funkciją maršrutizavimui
workflow = (
    WorkflowBuilder()
        .set_start_executor(evangelist_agent)
        .add_edge(evangelist_agent, reviewer_agent)
        .add_edge(reviewer_agent, to_reviewer_result)
        # Daugiafunkcis pasirinkimo kraštas įgyvendina sąlyginę logiką
        .add_multi_selection_edge_group(
            to_reviewer_result,
            [handle_review, save_draft],
            selection_func=select_targets,
        )
        .add_edge(save_draft, publisher_agent)
        .build()
)
```

Specialūs vykdytojai, tokie kaip `to_reviewer_result`, naudojami parsinant JSON iš agentų ir konvertuojant jį į stipriai tipizuotus objektus, kuriuos funkcija gali patikrinti.

#### .NET (C\#) įgyvendinimo analizė

.NET versija naudoja panašią prieigą su sąlygos funkcija. Apibrėžtas `Func<object?, bool>`, kuris tikrina `ReviewResult` objekto `Result` savybę.

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

Metodas `AddEdge` su `condition` parametru leidžia `WorkflowBuilder` sukurti šakotą kelią. Darbo srautas eis per briauną į `publishExecutor` tik tada, jei sąlyga `GetCondition(expectedResult: "Yes")` yra teisinga. Priešingu atveju jis eis keliu į `sendReviewerExecutor`.

## Išvada

Microsoft Agent Framework Workflow suteikia tvirtą ir lankstų pagrindą sudėtingų daugiaprogramių sistemų orkestravimui. Pasinaudodami grafu paremtos architektūros ir pagrindiniais komponentais, programuotojai gali kurti ir įgyvendinti pažangius darbo srautus tiek Python, tiek .NET aplinkose. Nesvarbu, ar jūsų programa reikalauja paprasto sekvinio apdorojimo, lygiagretaus vykdymo ar dinaminės sąlyginės logikos, ši sistema siūlo įrankius galingoms, mastelį keičiančioms ir tipams saugioms AI pagrįstoms sprendimų kūrimui.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Atsakomybės apribojimas**:
Šis dokumentas buvo išverstas naudojant dirbtinio intelekto vertimo paslaugą [Co-op Translator](https://github.com/Azure/co-op-translator). Nors siekiame tikslumo, prašome atkreipti dėmesį, kad automatiniai vertimai gali turėti klaidų ar netikslumų. Originalus dokumentas jo gimtąja kalba laikomas autoritetingu šaltiniu. Svarbiai informacijai rekomenduojama naudoti profesionalų žmogiškąjį vertimą. Mes neatsakome už jokius nesusipratimus ar neteisingą interpretaciją, kilusią naudojantis šiuo vertimu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->