# Kuriant daugiaveiksnius taikymus su Microsoft Agent Framework Workflow

Šiame vadove sužinosite, kaip suprasti ir kurti daugiaveiksnius taikymus naudojant Microsoft Agent Framework. Mes nagrinėsime pagrindines daugiaveiksnių sistemų sąvokas, gilinsimės į Framework Workflow komponento architektūrą ir peržiūrėsime praktinius pavyzdžius Python ir .NET kalbomis, skirtus skirtingiems darbo eigos modeliams.

## 1\. Daugiaveiksnių sistemų supratimas

Dirbtinio intelekto agentas yra sistema, kuri pranoksta standartinio didelio kalbos modelio (LLM) galimybes. Jis gali suvokti aplinką, priimti sprendimus ir atlikti veiksmus, siekdamas konkrečių tikslų. Daugiaveiksnė sistema apima kelis tokius agentus, kurie bendradarbiauja spręsdami problemą, kuri būtų sudėtinga arba neįmanoma vienam agentui.

### Dažniausi taikymo scenarijai

  * **Sudėtingų problemų sprendimas**: Didelės užduoties (pvz., įmonės renginio planavimas) suskaidymas į mažesnes užduotis, kurias atlieka specializuoti agentai (pvz., biudžeto agentas, logistikos agentas, rinkodaros agentas).
  * **Virtualūs asistentai**: Pagrindinis asistentas deleguoja užduotis, tokias kaip tvarkaraščių sudarymas, tyrimai ir rezervacijos, kitiems specializuotiems agentams.
  * **Automatizuotas turinio kūrimas**: Darbo eiga, kurioje vienas agentas rengia turinį, kitas peržiūri jį dėl tikslumo ir tono, o trečias publikuoja.

### Daugiaveiksnių sistemų modeliai

Daugiaveiksnės sistemos gali būti organizuotos pagal kelis modelius, kurie nustato jų sąveiką:

  * **Sekvencinis**: Agentai dirba iš anksto nustatyta tvarka, kaip surinkimo linijoje. Vieno agento išvestis tampa kito agento įvestimi.
  * **Lygiagretus**: Agentai dirba lygiagrečiai skirtingose užduoties dalyse, o jų rezultatai sujungiami pabaigoje.
  * **Sąlyginis**: Darbo eiga seka skirtingais keliais, priklausomai nuo agento išvesties, panašiai kaip if-then-else teiginys.

## 2\. Microsoft Agent Framework Workflow architektūra

Agent Framework darbo eigos sistema yra pažangi orkestravimo variklis, skirtas valdyti sudėtingas sąveikas tarp daugelio agentų. Ji sukurta remiantis grafų architektūra, naudojančia [Pregel stiliaus vykdymo modelį](https://kowshik.github.io/JPregel/pregel_paper.pdf), kur apdorojimas vyksta sinchronizuotais žingsniais, vadinamais „superžingsniais“.

### Pagrindiniai komponentai

Architektūra susideda iš trijų pagrindinių dalių:

1.  **Vykdytojai**: Tai pagrindiniai apdorojimo vienetai. Mūsų pavyzdžiuose `Agent` yra vykdytojo tipas. Kiekvienas vykdytojas gali turėti kelis pranešimų tvarkytojus, kurie automatiškai aktyvuojami pagal gauto pranešimo tipą.
2.  **Kraštai**: Jie apibrėžia kelią, kuriuo pranešimai keliauja tarp vykdytojų. Kraštai gali turėti sąlygas, leidžiančias dinamiškai nukreipti informaciją per darbo eigos grafiką.
3.  **Darbo eiga**: Šis komponentas organizuoja visą procesą, valdo vykdytojus, kraštus ir bendrą vykdymo eigą. Jis užtikrina, kad pranešimai būtų apdorojami tinkama tvarka ir transliuoja įvykius stebėjimui.

*Diagramoje pavaizduoti pagrindiniai darbo eigos sistemos komponentai.*

Ši struktūra leidžia kurti patikimus ir mastelio keičiamus taikymus, naudojant pagrindinius modelius, tokius kaip sekvencinės grandinės, fan-out/fan-in lygiagrečiam apdorojimui ir switch-case logiką sąlyginiams srautams.

## 3\. Praktiniai pavyzdžiai ir kodo analizė

Dabar peržiūrėsime, kaip įgyvendinti skirtingus darbo eigos modelius naudojant Framework. Kiekvienam pavyzdžiui pateiksime Python ir .NET kodą.

### Atvejis 1: Paprasta sekvencinė darbo eiga

Tai paprasčiausias modelis, kai vieno agento išvestis tiesiogiai perduodama kitam. Mūsų scenarijuje dalyvauja viešbučio `FrontDesk` agentas, kuris pateikia kelionės rekomendaciją, kurią peržiūri `Concierge` agentas.

*Diagramoje pavaizduota paprasta FrontDesk -\> Concierge darbo eiga.*

#### Scenarijaus fonas

Kelionės prašytojas prašo rekomendacijos Paryžiuje.

1.  `FrontDesk` agentas, orientuotas į trumpumą, siūlo aplankyti Luvro muziejų.
2.  `Concierge` agentas, kuris teikia pirmenybę autentiškoms patirtims, gauna šį pasiūlymą. Jis peržiūri rekomendaciją ir pateikia atsiliepimą, siūlydamas vietinę, mažiau turistinę alternatyvą.

#### Python įgyvendinimo analizė

Python pavyzdyje pirmiausia apibrėžiame ir sukuriame du agentus, kiekvieną su konkrečiomis instrukcijomis.

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

Tada naudojamas `WorkflowBuilder`, kad būtų sukurtas grafikas. `front_desk_agent` nustatomas kaip pradinė taškas, o kraštas sukuriamas, kad sujungtų jo išvestį su `reviewer_agent`.

```python
# 01.python-agent-framework-workflow-ghmodel-basic.ipynb

workflow = WorkflowBuilder().set_start_executor(front_desk_agent).add_edge(front_desk_agent, reviewer_agent).build()
```

Galiausiai darbo eiga vykdoma su pradiniu vartotojo prašymu.

```python
# 01.python-agent-framework-workflow-ghmodel-basic.ipynb

result =''
# The run_stream method executes the workflow and streams events.
async for event in workflow.run_stream('I would like to go to Paris.'):
    if isinstance(event, WorkflowEvent):
        result += str(event.data)
```

#### .NET (C\#) įgyvendinimo analizė

.NET įgyvendinimas seka labai panašią logiką. Pirmiausia apibrėžiami konstantai agentų pavadinimams ir instrukcijoms.

```csharp
// 01.dotnet-agent-framework-workflow-ghmodel-basic.ipynb

const string ReviewerAgentName = "Concierge";
const string ReviewerAgentInstructions = @"
    You are an are hotel concierge who has opinions about providing the most local and authentic experiences for travelers...";

const string FrontDeskAgentName = "FrontDesk";
const string FrontDeskAgentInstructions = @"""
    You are a Front Desk Travel Agent with ten years of experience and are known for brevity...";
```

Agentai sukuriami naudojant `OpenAIClient`, o tada `WorkflowBuilder` apibrėžia sekvencinį srautą, pridėdamas kraštą nuo `frontDeskAgent` iki `reviewerAgent`.

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

Darbo eiga vykdoma su vartotojo pranešimu, o rezultatai transliuojami atgal.

### Atvejis 2: Daugiapakopė sekvencinė darbo eiga

Šis modelis išplečia paprastą sekvenciją, įtraukiant daugiau agentų. Jis idealus procesams, kuriems reikia kelių etapų tobulinimo ar transformacijos.

#### Scenarijaus fonas

Vartotojas pateikia svetainės nuotrauką ir prašo baldų kainos pasiūlymo.

1.  **Sales-Agent**: Identifikuoja baldų elementus nuotraukoje ir sudaro sąrašą.
2.  **Price-Agent**: Pateikia sąrašo elementų kainų detalizaciją, įskaitant biudžetines, vidutinės klasės ir prabangias parinktis.
3.  **Quote-Agent**: Gautą kainų sąrašą paverčia oficialiu pasiūlymo dokumentu Markdown formatu.

*Diagramoje pavaizduota Sales -\> Price -\> Quote darbo eiga.*

#### Python įgyvendinimo analizė

Trys agentai apibrėžiami, kiekvienas su specializuotu vaidmeniu. Darbo eiga konstruojama naudojant `add_edge`, kad būtų sukurta grandinė: `sales_agent` -\> `price_agent` -\> `quote_agent`.

```python
# 02.python-agent-framework-workflow-ghmodel-sequential.ipynb

# Create three specialized agents
sales_agent = chat_client.create_agent(...)
price_agent = chat_client.create_agent(...)
quote_agent = chat_client.create_agent(...)

# Build the sequential workflow
workflow = WorkflowBuilder().set_start_executor(sales_agent).add_edge(sales_agent, price_agent).add_edge(price_agent, quote_agent).build()
```

Įvestis yra `ChatMessage`, kuri apima tekstą ir nuotraukos URI. Framework automatiškai perduoda kiekvieno agento išvestį kitam sekoje, kol sukuriamas galutinis pasiūlymas.

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

#### .NET (C\#) įgyvendinimo analizė

.NET pavyzdys atspindi Python versiją. Trys agentai (`salesagent`, `priceagent`, `quoteagent`) sukuriami. `WorkflowBuilder` juos sujungia sekvenciškai.

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

Vartotojo pranešimas sudaromas su nuotraukos duomenimis (kaip baitais) ir tekstiniu prašymu. `InProcessExecution.StreamAsync` metodas inicijuoja darbo eigą, o galutinis rezultatas gaunamas iš srauto.

### Atvejis 3: Lygiagreti darbo eiga

Šis modelis naudojamas, kai užduotys gali būti atliekamos vienu metu, taupant laiką. Jis apima „fan-out“ keliems agentams ir „fan-in“ rezultatų sujungimui.

#### Scenarijaus fonas

Vartotojas prašo suplanuoti kelionę į Sietlą.

1.  **Dispatcher (Fan-Out)**: Vartotojo prašymas siunčiamas dviem agentams vienu metu.
2.  **Researcher-Agent**: Tyrinėja lankytinas vietas, orus ir pagrindinius aspektus kelionei į Sietlą gruodžio mėnesį.
3.  **Plan-Agent**: Nepriklausomai sudaro detalų dienos kelionės planą.
4.  **Aggregator (Fan-In)**: Abu agentų rezultatai surenkami ir pateikiami kartu kaip galutinis rezultatas.

*Diagramoje pavaizduota lygiagreti Researcher ir Planner darbo eiga.*

#### Python įgyvendinimo analizė

`ConcurrentBuilder` supaprastina šio modelio kūrimą. Jūs tiesiog nurodote dalyvaujančius agentus, o kūrėjas automatiškai sukuria reikalingą fan-out ir fan-in logiką.

```python
# 03.python-agent-framework-workflow-ghmodel-concurrent.ipynb

research_agent = chat_client.create_agent(name="Researcher-Agent", ...)
plan_agent = chat_client.create_agent(name="Plan-Agent", ...)

# ConcurrentBuilder handles the fan-out/fan-in logic
workflow = ConcurrentBuilder().participants([research_agent, plan_agent]).build()

# Run the workflow
events = await workflow.run("Plan a trip to Seattle in December")
```

Framework užtikrina, kad `research_agent` ir `plan_agent` vykdytų lygiagrečiai, o jų galutiniai rezultatai būtų surinkti į sąrašą.

#### .NET (C\#) įgyvendinimo analizė

.NET versijoje šis modelis reikalauja aiškesnio apibrėžimo. Sukuriami specialūs vykdytojai (`ConcurrentStartExecutor` ir `ConcurrentAggregationExecutor`), kad būtų valdomas fan-out ir fan-in logika.

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

`WorkflowBuilder` tada naudoja `AddFanOutEdge` ir `AddFanInEdge`, kad sukurtų grafiką su šiais specialiais vykdytojais ir agentais.

```csharp
// 03.dotnet-agent-framework-workflow-ghmodel-concurrent.ipynb

var workflow = new WorkflowBuilder(startExecutor)
            .AddFanOutEdge(startExecutor, targets: [researcherAgent, plannerAgent])
            .AddFanInEdge(aggregationExecutor, sources: [researcherAgent, plannerAgent])
            .WithOutputFrom(aggregationExecutor)
            .Build();
```

### Atvejis 4: Sąlyginė darbo eiga

Sąlyginės darbo eigos įveda šakos logiką, leidžiančią sistemai sekti skirtingais keliais, priklausomai nuo tarpinių rezultatų.

#### Scenarijaus fonas

Ši darbo eiga automatizuoja techninio vadovo kūrimą ir publikavimą.

1.  **Evangelist-Agent**: Rašo vadovo juodraštį pagal pateiktą planą ir URL.
2.  **ContentReviewer-Agent**: Peržiūri juodraštį. Tikrina, ar žodžių skaičius viršija 200.
3.  **Sąlyginė šaka**:
      * **Jei patvirtinta (`Yes`)**: Darbo eiga pereina prie `Publisher-Agent`.
      * **Jei atmesta (`No`)**: Darbo eiga sustoja ir pateikia atmetimo priežastį.
4.  **Publisher-Agent**: Jei juodraštis patvirtintas, šis agentas išsaugo turinį Markdown faile.

#### Python įgyvendinimo analizė

Šiame pavyzdyje naudojama speciali funkcija `select_targets`, kad būtų įgyvendinta sąlyginė logika. Ši funkcija perduodama `add_multi_selection_edge_group` ir nukreipia darbo eigą pagal `review_result` lauką iš peržiūros agento išvesties.

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

Specialūs vykdytojai, tokie kaip `to_reviewer_result`, naudojami JSON išvesties iš agentų analizavimui ir konvertavimui į stipriai tipizuotus objektus, kuriuos gali patikrinti pasirinkimo funkcija.

#### .NET (C\#) įgyvendinimo analizė

.NET versija naudoja panašų požiūrį su sąlygos funkcija. Apibrėžiamas `Func<object?, bool>`, kad būtų patikrinta `Result` savybė iš `ReviewResult` objekto.

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

`AddEdge` metodo `condition` parametras leidžia `WorkflowBuilder` sukurti šakos kelią. Darbo eiga seks kraštą į `publishExecutor` tik tuo atveju, jei sąlyga `GetCondition(expectedResult: "Yes")` grąžins true. Priešingu atveju ji seks kelią į `sendReviewerExecutor`.

## Išvada

Microsoft Agent Framework Workflow suteikia patikimą ir lankstų pagrindą sudėtingų daugiaveiksnių sistemų orkestravimui. Naudodami jo grafų architektūrą ir pagrindinius komponentus, kūrėjai gali kurti ir įgyvendinti sudėtingas darbo eigas Python ir .NET kalbomis. Nesvarbu, ar jūsų taikymui reikia paprasto sekvencinio apdorojimo, lygiagretaus vykdymo, ar dinaminės sąlyginės logikos, Framework siūlo įrankius, leidžiančius kurti galingus, mastelio keičiamus ir tipų saugius AI sprendimus.

---

**Atsakomybės atsisakymas**:  
Šis dokumentas buvo išverstas naudojant AI vertimo paslaugą [Co-op Translator](https://github.com/Azure/co-op-translator). Nors siekiame tikslumo, prašome atkreipti dėmesį, kad automatiniai vertimai gali turėti klaidų ar netikslumų. Originalus dokumentas jo gimtąja kalba turėtų būti laikomas autoritetingu šaltiniu. Kritinei informacijai rekomenduojama naudoti profesionalų žmogaus vertimą. Mes neprisiimame atsakomybės už nesusipratimus ar klaidingus interpretavimus, atsiradusius dėl šio vertimo naudojimo.