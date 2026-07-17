# Construirea aplicațiilor multi-agent cu Microsoft Agent Framework Workflow

Acest tutorial vă va ghida prin înțelegerea și construirea aplicațiilor multi-agent folosind Microsoft Agent Framework. Vom explora conceptele de bază ale sistemelor multi-agent, vom analiza arhitectura componentei Workflow a framework-ului și vom parcurge exemple practice atât în Python, cât și în .NET pentru diferite modele de workflow.

## 1\. Înțelegerea sistemelor multi-agent

Un Agent AI este un sistem care depășește capabilitățile unui Model de Limbaj Mare (LLM) standard. Acesta poate percepe mediul său, lua decizii și întreprinde acțiuni pentru a atinge obiective specifice. Un sistem multi-agent implică mai mulți astfel de agenți care colaborează pentru a rezolva o problemă care ar fi dificilă sau imposibilă pentru un singur agent să o gestioneze singur.

### Scenarii comune de aplicare

  * **Rezolvarea problemelor complexe**: Descompunerea unei sarcini mari (de exemplu, planificarea unui eveniment la nivel de companie) în sub-sarcini mai mici gestionate de agenți specializați (de exemplu, un agent pentru buget, un agent de logistică, un agent de marketing).
  * **Asistenți virtuali**: Un agent asistent principal care delegă sarcini precum programarea, cercetarea și rezervările către alți agenți specializați.
  * **Crearea automată de conținut**: Un workflow în care un agent redactează conținut, altul îl revizuiește pentru acuratețe și ton, iar un al treilea îl publică.

### Modele multi-agent

Sistemele multi-agent pot fi organizate în mai multe modele, care determină modul în care acestea interacționează:

  * **Secvențial**: Agenții lucrează într-o ordine prestabilită, asemenea unei linii de asamblare. Ieșirea unui agent devine intrarea pentru următorul.
  * **Concurrent**: Agenții lucrează în paralel la diferite părți ale unei sarcini, iar rezultatele lor sunt agregate la final.
  * **Condițional**: Workflow-ul urmează căi diferite bazate pe ieșirea unui agent, similar unei instrucțiuni if-then-else.

## 2\. Arhitectura Workflow-ului Microsoft Agent Framework

Sistemul de workflow al Agent Framework este un motor avansat de orchestrare proiectat pentru a gestiona interacțiuni complexe între mai mulți agenți. Este construit pe o arhitectură bazată pe graf care utilizează un [model de execuție de tip Pregel](https://kowshik.github.io/JPregel/pregel_paper.pdf), unde procesarea are loc în pași sincronizați numiți "superpași."

### Componente principale

Arhitectura este compusă din trei părți principale:

1.  **Executori**: Acestea sunt unitățile fundamentale de procesare. În exemplele noastre, un `Agent` este un tip de executor. Fiecare executor poate avea mai mulți handleri de mesaje care sunt invocați automat în funcție de tipul mesajului primit.
2.  **Muchii**: Definiesc traseul pe care îl iau mesajele între executori. Muchiile pot avea condiții, permițând rutarea dinamică a informației prin graful workflow-ului.
3.  **Workflow**: Această componentă orchestrează întregul proces, gestionând executori, muchii și fluxul general de execuție. Asigură procesarea mesajelor în ordinea corectă și transmite fluxuri de evenimente pentru observabilitate.

*Un diagram care ilustrează componentele principale ale sistemului de workflow.*

Această structură permite construirea de aplicații robuste și scalabile folosind modele fundamentale precum lanțuri secvențiale, fan-out/fan-in pentru procesare paralelă și logică switch-case pentru fluxuri condiționale.

## 3\. Exemple practice și analiză de cod

Acum să explorăm cum să implementăm diferite modele de workflow folosind framework-ul. Vom examina atât cod Python, cât și .NET pentru fiecare exemplu.

### Cazul 1: Workflow secvențial de bază

Acesta este cel mai simplu model, în care ieșirea unui agent este transmisă direct către altul. Scenariul nostru implică un agent `FrontDesk` al unui hotel care face o recomandare de călătorie, ce este apoi revizuită de un agent `Concierge`.

*Diagramă a workflow-ului de bază FrontDesk -\> Concierge.*

#### Contextul scenariului

Un călător cere o recomandare în Paris.

1.  Agentul `FrontDesk`, proiectat pentru concizie, sugerează vizitarea Muzeului Louvre.
2.  Agentul `Concierge`, care prioritizează experiențe autentice, primește această sugestie. Revizuiește recomandarea și oferă feedback, sugerând o alternativă mai locală, mai puțin turistică.

#### Analiza implementării în Python

În exemplul Python, mai întâi definim și creăm cei doi agenți, fiecare cu instrucțiuni specifice.

```python
# 01.python-agent-framework-workflow-ghmodel-basic.ipynb

# Definirea rolurilor și instrucțiunilor agentului
REVIEWER_NAME = "Concierge"
REVIEWER_INSTRUCTIONS = """
    You are a hotel concierge who has opinions about providing the most local and authentic experiences for travelers...
    """

FRONTDESK_NAME = "FrontDesk"
FRONTDESK_INSTRUCTIONS = """
    You are a Front Desk Travel Agent with ten years of experience and are known for brevity...
    """

# Crearea instanțelor agentului
reviewer_agent = chat_client.as_agent(
    instructions=(REVIEWER_INSTRUCTIONS),
    name=REVIEWER_NAME,
)

front_desk_agent = chat_client.as_agent(
    instructions=(FRONTDESK_INSTRUCTIONS),
    name=FRONTDESK_NAME,
)
```

Apoi, `WorkflowBuilder` este folosit pentru a construi graful. Agentul `front_desk_agent` este setat ca punct de pornire, iar o muchie este creată pentru a conecta ieșirea acestuia la `reviewer_agent`.

```python
# 01.python-agent-framework-workflow-ghmodel-basic.ipynb

workflow = WorkflowBuilder(start_executor=front_desk_agent).add_edge(front_desk_agent, reviewer_agent).build()
```

În final, workflow-ul este executat cu promptul inițial al utilizatorului.

```python
# 01.python-agent-framework-workflow-ghmodel-basic.ipynb

result =''
# run execută fluxul de lucru; get_outputs() returnează rezultatul executorului de ieșiri.
events = await workflow.run('I would like to go to Paris.')
outputs = events.get_outputs()
result = outputs[0].text if outputs else ''
```

#### Analiza implementării în .NET (C\#)

Implementarea în .NET urmează o logică foarte similară. Mai întâi sunt definite constante pentru numele agenților și instrucțiunile acestora.

```csharp
// 01.dotnet-agent-framework-workflow-ghmodel-basic.ipynb

const string ReviewerAgentName = "Concierge";
const string ReviewerAgentInstructions = @"
    You are a hotel concierge who has opinions about providing the most local and authentic experiences for travelers...";

const string FrontDeskAgentName = "FrontDesk";
const string FrontDeskAgentInstructions = @"""
    You are a Front Desk Travel Agent with ten years of experience and are known for brevity...";
```

Agenții sunt creați utilizând un `AzureOpenAIClient` (Answers API), apoi `WorkflowBuilder` definește fluxul secvențial adăugând o muchie de la `frontDeskAgent` la `reviewerAgent`.

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

Workflow-ul este apoi rulat cu mesajul utilizatorului, iar rezultatele sunt transmise în flux înapoi.

### Cazul 2: Workflow secvențial cu mai mulți pași

Acest model extinde secvența de bază pentru a include mai mulți agenți. Este ideal pentru procese care necesită multiple etape de rafinare sau transformare.

#### Contextul scenariului

Un utilizator oferă o imagine a unui living și cere o ofertă pentru mobilă.

1.  **Agent de vânzări**: Identifică obiectele de mobilier din imagine și creează o listă.
2.  **Agent de prețuri**: Primește lista de obiecte și oferă o defalcare detaliată a prețurilor, inclusiv opțiuni de buget, medii și premium.
3.  **Agent de ofertă**: Primește lista cu prețuri și o formulează într-un document formal de ofertă în Markdown.

*Diagramă a workflow-ului Sales -\> Price -\> Quote.*

#### Analiza implementării în Python

Trei agenți sunt definiți, fiecare cu un rol specializat. Workflow-ul este construit folosind `add_edge` pentru a crea un lanț: `sales_agent` -\> `price_agent` -\> `quote_agent`.

```python
# 02.python-agent-framework-workflow-ghmodel-sequential.ipynb

# Creează trei agenți specializați
sales_agent = chat_client.as_agent(...)
price_agent = chat_client.as_agent(...)
quote_agent = chat_client.as_agent(...)

# Construiește fluxul de lucru secvențial
workflow = WorkflowBuilder(start_executor=sales_agent).add_edge(sales_agent, price_agent).add_edge(price_agent, quote_agent).build()
```

Intrarea este un `ChatMessage` care include atât text, cât și URI-ul imaginii. Framework-ul gestionează transmiterea ieșirii fiecărui agent către următorul în secvență până când oferta finală este generată.

```python
# 02.python-agent-framework-workflow-ghmodel-sequential.ipynb

# Mesajul utilizatorului conține atât text, cât și o imagine
message = ChatMessage(
        role=Role.USER,
        contents=[
            TextContent(text="Please find the relevant furniture..."),
            DataContent(uri=image_uri, media_type="image/png")
        ]
)

# Execută fluxul de lucru
events = await workflow.run(message)
```

#### Analiza implementării în .NET (C\#)

Exemplul .NET oglindește versiunea Python. Trei agenți (`salesagent`, `priceagent`, `quoteagent`) sunt creați. `WorkflowBuilder` îi leagă secvențial.

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

Mesajul utilizatorului este construit cu datele imaginii (ca bytes) și promptul text. Metoda `InProcessExecution.RunStreamingAsync` inițiază workflow-ul, iar ieșirea finală este capturată din flux.

### Cazul 3: Workflow concurent

Acest model se utilizează când sarcinile pot fi executate simultan pentru a economisi timp. Implică un "fan-out" către mai mulți agenți și un "fan-in" pentru agregarea rezultatelor.

#### Contextul scenariului

Un utilizator cere să planifice o călătorie la Seattle.

1.  **Dispatcher (Fan-Out)**: Cererea utilizatorului este trimisă simultan către doi agenți.
2.  **Agent de cercetare**: Cercetează atracții, vreme și considerente cheie pentru o călătorie la Seattle în decembrie.
3.  **Agent de planificare**: Creează independent un itinerar detaliat, zi cu zi.
4.  **Aggregator (Fan-In)**: Rezultatele de la cercetător și planificator sunt colectate și prezentate împreună ca rezultat final.

*Diagramă a workflow-ului concurent Researcher și Planner.*

#### Analiza implementării în Python

`ConcurrentBuilder` simplifică crearea acestui model. Pur și simplu enumerați agenții participanți, iar builder-ul creează automat logica necesară fan-out și fan-in.

```python
# 03.python-agent-framework-workflow-ghmodel-concurrent.ipynb

research_agent = chat_client.as_agent(name="Researcher-Agent", ...)
plan_agent = chat_client.as_agent(name="Plan-Agent", ...)

# ConcurrentBuilder gestionează logica de dispersie/recuperare
workflow = ConcurrentBuilder().participants([research_agent, plan_agent]).build()

# Rulează fluxul de lucru
events = await workflow.run("Plan a trip to Seattle in December")
```

Framework-ul asigură că `research_agent` și `plan_agent` execută în paralel, iar ieșirile finale sunt colectate într-o listă.

#### Analiza implementării în .NET (C\#)

În .NET, acest model necesită o definiție mai explicită. Executori personalizați (`ConcurrentStartExecutor` și `ConcurrentAggregationExecutor`) sunt creați pentru a gestiona logica fan-out și fan-in.

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

`WorkflowBuilder` folosește apoi `AddFanOutEdge` și `AddFanInEdge` pentru a construi graful cu acești executori personalizați și agenții.

```csharp
// 03.dotnet-agent-framework-workflow-ghmodel-concurrent.ipynb

var workflow = new WorkflowBuilder(startExecutor)
            .AddFanOutEdge(startExecutor, targets: [researcherAgent, plannerAgent])
            .AddFanInEdge(aggregationExecutor, sources: [researcherAgent, plannerAgent])
            .WithOutputFrom(aggregationExecutor)
            .Build();
```

### Cazul 4: Workflow condițional

Workflow-urile condiționale introduc o logică de ramificare, permițând sistemului să urmeze căi diferite bazate pe rezultate intermediare.

#### Contextul scenariului

Acest workflow automatizează crearea și publicarea unui tutorial tehnic.

1.  **Agentul evangelist**: Scrie un draft al tutorialului bazat pe un plan și URL-uri date.
2.  **Agentul de revizuire de conținut**: Revizuiește draftul. Verifică dacă numărul de cuvinte depășește 200.
3.  **Ramificare condițională**:
      * **Dacă este aprobat (`Yes`)**: Workflow-ul continuă către agentul `Publisher`.
      * **Dacă este respins (`No`)**: Workflow-ul se oprește și afișează motivul respingerii.
4.  **Agentul Publisher**: Dacă draftul este aprobat, acest agent salvează conținutul într-un fișier Markdown.

#### Analiza implementării în Python

Acest exemplu folosește o funcție personalizată, `select_targets`, pentru a implementa logica condițională. Această funcție este transmisă la `add_multi_selection_edge_group` și direcționează workflow-ul bazat pe câmpul `review_result` din ieșirea agentului de revizuire.

```python
# 04.python-agent-framework-workflow-aifoundry-condition.ipynb

# Această funcție determină pasul următor bazat pe rezultatul recenziei
def select_targets(review: ReviewResult, target_ids: list[str]) -> list[str]:
    handle_review_id, save_draft_id = target_ids
    if review.review_result == "Yes":
        # Dacă este aprobat, continuă la executorul 'save_draft'
        return [save_draft_id]
    else:
        # Dacă este respins, continuă la executorul 'handle_review' pentru a raporta eșecul
        return [handle_review_id]

# Constructorul de fluxuri de lucru folosește funcția de selecție pentru rutare
workflow = (
    WorkflowBuilder()
        .set_start_executor(evangelist_agent)
        .add_edge(evangelist_agent, reviewer_agent)
        .add_edge(reviewer_agent, to_reviewer_result)
        # Muchia de selecție multiplă implementează logica condițională
        .add_multi_selection_edge_group(
            to_reviewer_result,
            [handle_review, save_draft],
            selection_func=select_targets,
        )
        .add_edge(save_draft, publisher_agent)
        .build()
)
```

Executori personalizați precum `to_reviewer_result` sunt folosiți pentru a analiza ieșirea JSON de la agenți și a o converti în obiecte tipizate pe care funcția de selecție le poate inspecta.

#### Analiza implementării în .NET (C\#)

Varianta .NET folosește o abordare similară cu o funcție condiție definită ca `Func<object?, bool>` pentru a verifica proprietatea `Result` a obiectului `ReviewResult`.

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

Parametrul `condition` al metodei `AddEdge` permite lui `WorkflowBuilder` să creeze un drum ramificat. Workflow-ul va urma muchia către `publishExecutor` doar dacă condiția `GetCondition(expectedResult: "Yes")` returnează adevărat. Altfel, urmează calea către `sendReviewerExecutor`.

## Concluzie

Microsoft Agent Framework Workflow oferă o bază robustă și flexibilă pentru orchestrarea sistemelor complexe multi-agent. Folosind arhitectura sa bazată pe graf și componentele principale, dezvoltatorii pot proiecta și implementa workflow-uri sofisticate atât în Python, cât și în .NET. Indiferent dacă aplicația dumneavoastră necesită procesare secvențială simplă, execuție paralelă sau logică condițională dinamică, framework-ul oferă instrumentele necesare pentru a construi soluții AI puternice, scalabile și tip-sigure.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Declinare a responsabilității**:
Acest document a fost tradus folosind serviciul de traducere AI [Co-op Translator](https://github.com/Azure/co-op-translator). În timp ce ne străduim pentru acuratețe, vă rugăm să rețineți că traducerile automate pot conține erori sau inexactități. Documentul original în limba sa nativă trebuie considerat sursa autorizată. Pentru informații critice, se recomandă traducerea profesională realizată de un om. Nu ne asumăm responsabilitatea pentru eventualele neînțelegeri sau interpretări greșite care decurg din utilizarea acestei traduceri.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->