# Δημιουργία Εφαρμογών Πολλαπλών Πρακτόρων με το Microsoft Agent Framework Workflow

Αυτός ο οδηγός θα σας βοηθήσει να κατανοήσετε και να δημιουργήσετε εφαρμογές πολλαπλών πρακτόρων χρησιμοποιώντας το Microsoft Agent Framework. Θα εξετάσουμε τις βασικές έννοιες των συστημάτων πολλαπλών πρακτόρων, θα εμβαθύνουμε στην αρχιτεκτονική του Workflow component του framework και θα δούμε πρακτικά παραδείγματα σε Python και .NET για διαφορετικά μοτίβα ροής εργασίας.

## 1\. Κατανόηση Συστημάτων Πολλαπλών Πρακτόρων

Ένας AI Agent είναι ένα σύστημα που υπερβαίνει τις δυνατότητες ενός τυπικού Μεγάλου Γλωσσικού Μοντέλου (LLM). Μπορεί να αντιλαμβάνεται το περιβάλλον του, να λαμβάνει αποφάσεις και να εκτελεί ενέργειες για την επίτευξη συγκεκριμένων στόχων. Ένα σύστημα πολλαπλών πρακτόρων περιλαμβάνει πολλούς από αυτούς τους πράκτορες που συνεργάζονται για την επίλυση ενός προβλήματος που θα ήταν δύσκολο ή αδύνατο να αντιμετωπιστεί από έναν μόνο πράκτορα.

### Συνήθεις Εφαρμογές

  * **Επίλυση Σύνθετων Προβλημάτων**: Διάσπαση μιας μεγάλης εργασίας (π.χ., οργάνωση μιας εκδήλωσης σε επίπεδο εταιρείας) σε μικρότερες υπο-εργασίες που αναλαμβάνονται από εξειδικευμένους πράκτορες (π.χ., πράκτορας προϋπολογισμού, πράκτορας logistics, πράκτορας μάρκετινγκ).
  * **Εικονικοί Βοηθοί**: Ένας κύριος πράκτορας βοηθός που αναθέτει εργασίες όπως προγραμματισμός, έρευνα και κρατήσεις σε άλλους εξειδικευμένους πράκτορες.
  * **Αυτοματοποιημένη Δημιουργία Περιεχομένου**: Μια ροή εργασίας όπου ένας πράκτορας συντάσσει περιεχόμενο, ένας άλλος το ελέγχει για ακρίβεια και ύφος, και ένας τρίτος το δημοσιεύει.

### Μοτίβα Πολλαπλών Πρακτόρων

Τα συστήματα πολλαπλών πρακτόρων μπορούν να οργανωθούν σε διάφορα μοτίβα, τα οποία καθορίζουν πώς αλληλεπιδρούν:

  * **Διαδοχικό**: Οι πράκτορες εργάζονται με προκαθορισμένη σειρά, όπως σε μια γραμμή συναρμολόγησης. Η έξοδος ενός πράκτορα γίνεται η είσοδος για τον επόμενο.
  * **Παράλληλο**: Οι πράκτορες εργάζονται ταυτόχρονα σε διαφορετικά μέρη μιας εργασίας, και τα αποτελέσματά τους συγκεντρώνονται στο τέλος.
  * **Υπό Όρους**: Η ροή ακολουθεί διαφορετικά μονοπάτια με βάση την έξοδο ενός πράκτορα, παρόμοια με μια δήλωση if-then-else.

## 2\. Η Αρχιτεκτονική του Microsoft Agent Framework Workflow

Το σύστημα ροής εργασίας του Agent Framework είναι μια προηγμένη μηχανή ορχήστρωσης σχεδιασμένη να διαχειρίζεται σύνθετες αλληλεπιδράσεις μεταξύ πολλών πρακτόρων. Είναι βασισμένο σε μια αρχιτεκτονική γραφήματος που χρησιμοποιεί ένα [μοντέλο εκτέλεσης τύπου Pregel](https://kowshik.github.io/JPregel/pregel_paper.pdf), όπου η επεξεργασία πραγματοποιείται σε συγχρονισμένα βήματα που ονομάζονται "supersteps".

### Βασικά Στοιχεία

Η αρχιτεκτονική αποτελείται από τρία κύρια μέρη:

1.  **Εκτελεστές**: Αυτές είναι οι βασικές μονάδες επεξεργασίας. Στα παραδείγματά μας, ένας `Agent` είναι ένας τύπος εκτελεστή. Κάθε εκτελεστής μπορεί να έχει πολλαπλούς χειριστές μηνυμάτων που ενεργοποιούνται αυτόματα με βάση τον τύπο του μηνύματος που λαμβάνεται.
2.  **Ακμές**: Αυτές καθορίζουν τη διαδρομή που ακολουθούν τα μηνύματα μεταξύ των εκτελεστών. Οι ακμές μπορούν να έχουν συνθήκες, επιτρέποντας δυναμική δρομολόγηση πληροφοριών μέσω του γραφήματος ροής εργασίας.
3.  **Ροή Εργασίας**: Αυτό το στοιχείο ορχηστρώνει ολόκληρη τη διαδικασία, διαχειρίζεται τους εκτελεστές, τις ακμές και τη συνολική ροή εκτέλεσης. Εξασφαλίζει ότι τα μηνύματα επεξεργάζονται με τη σωστή σειρά και μεταδίδει συμβάντα για παρατηρησιμότητα.

*Διάγραμμα που απεικονίζει τα βασικά στοιχεία του συστήματος ροής εργασίας.*

Αυτή η δομή επιτρέπει τη δημιουργία ισχυρών και επεκτάσιμων εφαρμογών χρησιμοποιώντας βασικά μοτίβα όπως διαδοχικές αλυσίδες, fan-out/fan-in για παράλληλη επεξεργασία και λογική switch-case για υπό όρους ροές.

## 3\. Πρακτικά Παραδείγματα και Ανάλυση Κώδικα

Ας δούμε πώς να υλοποιήσουμε διαφορετικά μοτίβα ροής εργασίας χρησιμοποιώντας το framework. Θα εξετάσουμε παραδείγματα κώδικα σε Python και .NET για κάθε περίπτωση.

### Περίπτωση 1: Βασική Διαδοχική Ροή Εργασίας

Αυτό είναι το απλούστερο μοτίβο, όπου η έξοδος ενός πράκτορα περνά απευθείας σε έναν άλλο. Το σενάριό μας περιλαμβάνει έναν πράκτορα `FrontDesk` που κάνει μια ταξιδιωτική πρόταση, η οποία στη συνέχεια εξετάζεται από έναν πράκτορα `Concierge`.

*Διάγραμμα της βασικής ροής FrontDesk -\> Concierge.*

#### Υπόβαθρο Σεναρίου

Ένας ταξιδιώτης ζητά μια πρόταση για το Παρίσι.

1.  Ο πράκτορας `FrontDesk`, σχεδιασμένος για συντομία, προτείνει την επίσκεψη στο Μουσείο του Λούβρου.
2.  Ο πράκτορας `Concierge`, που δίνει προτεραιότητα σε αυθεντικές εμπειρίες, λαμβάνει αυτήν την πρόταση. Εξετάζει την πρόταση και παρέχει σχόλια, προτείνοντας μια πιο τοπική, λιγότερο τουριστική εναλλακτική.

#### Ανάλυση Υλοποίησης σε Python

Στο παράδειγμα Python, πρώτα ορίζουμε και δημιουργούμε τους δύο πράκτορες, καθένας με συγκεκριμένες οδηγίες.

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

Στη συνέχεια, χρησιμοποιείται το `WorkflowBuilder` για την κατασκευή του γραφήματος. Ο `front_desk_agent` ορίζεται ως το σημείο εκκίνησης, και δημιουργείται μια ακμή για τη σύνδεση της εξόδου του με τον `reviewer_agent`.

```python
# 01.python-agent-framework-workflow-ghmodel-basic.ipynb

workflow = WorkflowBuilder().set_start_executor(front_desk_agent).add_edge(front_desk_agent, reviewer_agent).build()
```

Τέλος, η ροή εργασίας εκτελείται με την αρχική προτροπή του χρήστη.

```python
# 01.python-agent-framework-workflow-ghmodel-basic.ipynb

result =''
# The run_stream method executes the workflow and streams events.
async for event in workflow.run_stream('I would like to go to Paris.'):
    if isinstance(event, WorkflowEvent):
        result += str(event.data)
```

#### Ανάλυση Υλοποίησης σε .NET (C\#)

Η υλοποίηση σε .NET ακολουθεί παρόμοια λογική. Πρώτα, ορίζονται σταθερές για τα ονόματα και τις οδηγίες των πρακτόρων.

```csharp
// 01.dotnet-agent-framework-workflow-ghmodel-basic.ipynb

const string ReviewerAgentName = "Concierge";
const string ReviewerAgentInstructions = @"
    You are an are hotel concierge who has opinions about providing the most local and authentic experiences for travelers...";

const string FrontDeskAgentName = "FrontDesk";
const string FrontDeskAgentInstructions = @"""
    You are a Front Desk Travel Agent with ten years of experience and are known for brevity...";
```

Οι πράκτορες δημιουργούνται χρησιμοποιώντας έναν `OpenAIClient`, και στη συνέχεια το `WorkflowBuilder` ορίζει τη διαδοχική ροή προσθέτοντας μια ακμή από τον `frontDeskAgent` στον `reviewerAgent`.

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

Η ροή εργασίας εκτελείται με το μήνυμα του χρήστη, και τα αποτελέσματα μεταδίδονται πίσω.

### Περίπτωση 2: Διαδοχική Ροή Εργασίας Πολλαπλών Βημάτων

Αυτό το μοτίβο επεκτείνει τη βασική ακολουθία για να περιλαμβάνει περισσότερους πράκτορες. Είναι ιδανικό για διαδικασίες που απαιτούν πολλαπλά στάδια βελτίωσης ή μετασχηματισμού.

#### Υπόβαθρο Σεναρίου

Ένας χρήστης παρέχει μια εικόνα ενός καθιστικού και ζητά προσφορά για έπιπλα.

1.  **Sales-Agent**: Αναγνωρίζει τα έπιπλα στην εικόνα και δημιουργεί μια λίστα.
2.  **Price-Agent**: Παίρνει τη λίστα αντικειμένων και παρέχει αναλυτική ανάλυση τιμών, συμπεριλαμβανομένων επιλογών προϋπολογισμού, μεσαίας κατηγορίας και premium.
3.  **Quote-Agent**: Λαμβάνει τη λίστα με τις τιμές και τη μορφοποιεί σε ένα επίσημο έγγραφο προσφοράς σε Markdown.

*Διάγραμμα της ροής Sales -\> Price -\> Quote.*

#### Ανάλυση Υλοποίησης σε Python

Ορίζονται τρεις πράκτορες, καθένας με εξειδικευμένο ρόλο. Η ροή εργασίας κατασκευάζεται χρησιμοποιώντας `add_edge` για τη δημιουργία μιας αλυσίδας: `sales_agent` -\> `price_agent` -\> `quote_agent`.

```python
# 02.python-agent-framework-workflow-ghmodel-sequential.ipynb

# Create three specialized agents
sales_agent = chat_client.create_agent(...)
price_agent = chat_client.create_agent(...)
quote_agent = chat_client.create_agent(...)

# Build the sequential workflow
workflow = WorkflowBuilder().set_start_executor(sales_agent).add_edge(sales_agent, price_agent).add_edge(price_agent, quote_agent).build()
```

Η είσοδος είναι ένα `ChatMessage` που περιλαμβάνει τόσο κείμενο όσο και το URI της εικόνας. Το framework χειρίζεται τη μεταβίβαση της εξόδου κάθε πράκτορα στον επόμενο στη σειρά μέχρι να δημιουργηθεί η τελική προσφορά.

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

#### Ανάλυση Υλοποίησης σε .NET (C\#)

Το παράδειγμα σε .NET αντικατοπτρίζει την έκδοση Python. Δημιουργούνται τρεις πράκτορες (`salesagent`, `priceagent`, `quoteagent`). Το `WorkflowBuilder` τους συνδέει διαδοχικά.

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

Το μήνυμα του χρήστη κατασκευάζεται με τα δεδομένα της εικόνας (ως bytes) και την προτροπή κειμένου. Η μέθοδος `InProcessExecution.StreamAsync` ξεκινά τη ροή εργασίας, και η τελική έξοδος καταγράφεται από τη ροή.

### Περίπτωση 3: Παράλληλη Ροή Εργασίας

Αυτό το μοτίβο χρησιμοποιείται όταν οι εργασίες μπορούν να εκτελεστούν ταυτόχρονα για εξοικονόμηση χρόνου. Περιλαμβάνει ένα "fan-out" σε πολλούς πράκτορες και ένα "fan-in" για τη συγκέντρωση των αποτελεσμάτων.

#### Υπόβαθρο Σεναρίου

Ένας χρήστης ζητά να σχεδιάσει ένα ταξίδι στο Σιάτλ.

1.  **Dispatcher (Fan-Out)**: Το αίτημα του χρήστη αποστέλλεται ταυτόχρονα σε δύο πράκτορες.
2.  **Researcher-Agent**: Ερευνά αξιοθέατα, καιρικές συνθήκες και βασικές παραμέτρους για ένα ταξίδι στο Σιάτλ τον Δεκέμβριο.
3.  **Plan-Agent**: Δημιουργεί ανεξάρτητα ένα λεπτομερές ημερήσιο πρόγραμμα ταξιδιού.
4.  **Aggregator (Fan-In)**: Τα αποτελέσματα από τον ερευνητή και τον σχεδιαστή συγκεντρώνονται και παρουσιάζονται μαζί ως τελικό αποτέλεσμα.

*Διάγραμμα της παράλληλης ροής Researcher και Planner.*

#### Ανάλυση Υλοποίησης σε Python

Το `ConcurrentBuilder` απλοποιεί τη δημιουργία αυτού του μοτίβου. Απλώς παραθέτετε τους συμμετέχοντες πράκτορες, και ο builder δημιουργεί αυτόματα τη λογική fan-out και fan-in.

```python
# 03.python-agent-framework-workflow-ghmodel-concurrent.ipynb

research_agent = chat_client.create_agent(name="Researcher-Agent", ...)
plan_agent = chat_client.create_agent(name="Plan-Agent", ...)

# ConcurrentBuilder handles the fan-out/fan-in logic
workflow = ConcurrentBuilder().participants([research_agent, plan_agent]).build()

# Run the workflow
events = await workflow.run("Plan a trip to Seattle in December")
```

Το framework εξασφαλίζει ότι οι `research_agent` και `plan_agent` εκτελούνται παράλληλα, και οι τελικές τους έξοδοι συγκεντρώνονται σε μια λίστα.

#### Ανάλυση Υλοποίησης σε .NET (C\#)

Σε .NET, αυτό το μοτίβο απαιτεί πιο σαφή ορισμό. Δημιουργούνται προσαρμοσμένοι εκτελεστές (`ConcurrentStartExecutor` και `ConcurrentAggregationExecutor`) για τη διαχείριση της λογικής fan-out και fan-in.

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

Το `WorkflowBuilder` χρησιμοποιεί `AddFanOutEdge` και `AddFanInEdge` για την κατασκευή του γραφήματος με αυτούς τους προσαρμοσμένους εκτελεστές και τους πράκτορες.

```csharp
// 03.dotnet-agent-framework-workflow-ghmodel-concurrent.ipynb

var workflow = new WorkflowBuilder(startExecutor)
            .AddFanOutEdge(startExecutor, targets: [researcherAgent, plannerAgent])
            .AddFanInEdge(aggregationExecutor, sources: [researcherAgent, plannerAgent])
            .WithOutputFrom(aggregationExecutor)
            .Build();
```

### Περίπτωση 4: Υπό Όρους Ροή Εργασίας

Οι υπό όρους ροές εργασίας εισάγουν λογική διακλάδωσης, επιτρέποντας στο σύστημα να ακολουθεί διαφορετικά μονοπάτια με βάση ενδιάμεσα αποτελέσματα.

#### Υπόβαθρο Σεναρίου

Αυτή η ροή αυτοματοποιεί τη δημιουργία και δημοσίευση ενός τεχνικού οδηγού.

1.  **Evangelist-Agent**: Συντάσσει ένα προσχέδιο του οδηγού με βάση ένα δεδομένο περίγραμμα και URLs.
2.  **ContentReviewer-Agent**: Εξετάζει το προσχέδιο. Ελέγχει αν ο αριθμός λέξεων είναι πάνω από 200.
3.  **Υπό Όρους Διακλάδωση**:
      * **Αν Εγκριθεί (`Yes`)**: Η ροή συνεχίζει στον `Publisher-Agent`.
      * **Αν Απορριφθεί (`No`)**: Η ροή σταματά και εξάγει τον λόγο απόρριψης.
4.  **Publisher-Agent**: Αν το προσχέδιο εγκριθεί, αυτός ο πράκτορας αποθηκεύει το περιεχόμενο σε ένα αρχείο Markdown.

#### Ανάλυση Υλοποίησης σε Python

Αυτό το παράδειγμα χρησιμοποιεί μια προσαρμοσμένη συνάρτηση, `select_targets`, για την υλοποίηση της λογικής υπό όρους. Αυτή η συνάρτηση περνά στο `add_multi_selection_edge_group` και κατευθύνει τη ροή με βάση το πεδίο `review_result` από την έξοδο του εξεταστή.

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

Προσαρμοσμένοι εκτελεστές όπως ο `to_reviewer_result` χρησιμοποιούνται για την ανάλυση της JSON εξόδου από τους πράκτορες και τη μετατροπή της σε αντικείμενα με ισχυρή τυποποίηση που μπορεί να επιθεωρήσει η συνάρτηση επιλογής.

#### Ανάλυση Υλοποίησης σε .NET (C\#)

Η έκδοση σε .NET χρησιμοποιεί παρόμοια προσέγγιση με μια συνάρτηση συνθήκης. Ορίζεται ένα `Func<object?, bool>` για να ελέγξει την ιδιότητα `Result` του αντικειμένου `ReviewResult`.

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

Η παράμετρος `condition` της μεθόδου `AddEdge` επιτρέπει στο `WorkflowBuilder` να δημιουργήσει ένα μονοπάτι διακλάδωσης. Η ροή εργασίας θα ακολουθήσει την ακμή προς τον `publishExecutor` μόνο αν η συνθήκη `GetCondition(expectedResult: "Yes")` επιστρέψει true. Διαφορετικά, ακολουθεί το μονοπάτι προς τον `sendReviewerExecutor`.

## Συμπέρασμα

Το Microsoft Agent Framework Workflow παρέχει μια ισχυρή και ευέλικτη βάση για την ορχήστρωση σύνθετων συστημάτων πολλαπλών πρακτόρων. Με την αξιοποίηση της αρχιτεκτονικής γραφήματος και των βασικών στοιχείων του, οι προγραμματιστές μπορούν να σχεδιάσουν και να υλοποιήσουν εξελιγμένες ροές εργασίας σε Python και .NET. Είτε η εφαρμογή σας απαιτεί απλή διαδοχική επεξεργασία, παράλληλη εκτέλεση ή δυναμική λογική υπό όρους, το framework προσφέρει τα εργαλεία για τη δημιουργία ισχυρών, επεκτάσιμων και ασφαλών λύσεων με AI.

---

**Αποποίηση ευθύνης**:  
Αυτό το έγγραφο έχει μεταφραστεί χρησιμοποιώντας την υπηρεσία αυτόματης μετάφρασης [Co-op Translator](https://github.com/Azure/co-op-translator). Παρόλο που καταβάλλουμε προσπάθειες για ακρίβεια, παρακαλούμε να έχετε υπόψη ότι οι αυτοματοποιημένες μεταφράσεις ενδέχεται να περιέχουν σφάλματα ή ανακρίβειες. Το πρωτότυπο έγγραφο στη μητρική του γλώσσα θα πρέπει να θεωρείται η αυθεντική πηγή. Για κρίσιμες πληροφορίες, συνιστάται επαγγελματική ανθρώπινη μετάφραση. Δεν φέρουμε ευθύνη για τυχόν παρεξηγήσεις ή εσφαλμένες ερμηνείες που προκύπτουν από τη χρήση αυτής της μετάφρασης.