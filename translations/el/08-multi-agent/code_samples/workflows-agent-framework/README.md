# Δημιουργία Εφαρμογών Πολλαπλών Πρακτόρων με το Microsoft Agent Framework Workflow

Αυτό το σεμινάριο θα σας καθοδηγήσει στην κατανόηση και δημιουργία εφαρμογών πολλαπλών πρακτόρων χρησιμοποιώντας το Microsoft Agent Framework. Θα εξερευνήσουμε τις βασικές έννοιες των συστημάτων πολλαπλών πρακτόρων, θα εμβαθύνουμε στην αρχιτεκτονική του συστατικού Workflow του πλαισίου και θα περπατήσουμε μέσα από πρακτικά παραδείγματα τόσο σε Python όσο και σε .NET για διαφορετικά πρότυπα ροής εργασίας.

## 1\. Κατανόηση των Συστημάτων Πολλαπλών Πρακτόρων

Ένας Πράκτορας Τεχνητής Νοημοσύνης είναι ένα σύστημα που υπερβαίνει τις δυνατότητες ενός τυπικού Μεγάλου Μοντέλου Γλώσσας (LLM). Μπορεί να αντιλαμβάνεται το περιβάλλον του, να λαμβάνει αποφάσεις και να αναλαμβάνει δράσεις για την επίτευξη συγκεκριμένων στόχων. Ένα σύστημα πολλαπλών πρακτόρων περιλαμβάνει αρκετούς από αυτούς τους πράκτορες που συνεργάζονται για να λύσουν ένα πρόβλημα που θα ήταν δύσκολο ή αδύνατο για έναν μόνο πράκτορα να διαχειριστεί μόνος του.

### Συνηθισμένα Σενάρια Εφαρμογής

  * **Επίλυση Πολύπλοκων Προβλημάτων**: Διάσπαση ενός μεγάλου έργου (π.χ., οργάνωση εκδήλωσης σε όλη την εταιρεία) σε μικρότερα υπο-έργα που διαχειρίζονται εξειδικευμένοι πράκτορες (π.χ., πράκτορας προϋπολογισμού, πράκτορας logistics, πράκτορας marketing).
  * **Εικονικοί Βοηθοί**: Ένας κύριος βοηθός που αναθέτει εργασίες όπως προγραμματισμό, έρευνα και κρατήσεις σε άλλους εξειδικευμένους πράκτορες.
  * **Αυτοματοποιημένη Δημιουργία Περιεχομένου**: Μια ροή εργασίας όπου ένας πράκτορας δημιουργεί ένα προσχέδιο περιεχομένου, ένας άλλος το ελέγχει για ακρίβεια και τον τόνο, και ένας τρίτος το δημοσιεύει.

### Πρότυπα Πολλαπλών Πρακτόρων

Τα συστήματα πολλαπλών πρακτόρων μπορούν να οργανωθούν σε διάφορα πρότυπα που καθορίζουν τον τρόπο αλληλεπίδρασής τους:

  * **Αλληλουχιακό**: Οι πράκτορες εργάζονται σε προεπιλεγμένη σειρά, όπως σε γραμμή συναρμολόγησης. Η έξοδος ενός πράκτορα γίνεται είσοδος για τον επόμενο.
  * **Ταυτόχρονο**: Οι πράκτορες δουλεύουν παράλληλα σε διαφορετικά μέρη μιας εργασίας και τα αποτελέσματά τους συγκεντρώνονται στο τέλος.
  * **Υπό Όρους**: Η ροή εργασίας ακολουθεί διαφορετικές διαδρομές ανάλογα με την έξοδο ενός πράκτορα, παρόμοια με μια εντολή if-then-else.

## 2\. Αρχιτεκτονική του Microsoft Agent Framework Workflow

Το σύστημα ροής εργασίας του Agent Framework είναι ένας προχωρημένος μηχανισμός ορχήστρωσης σχεδιασμένος να διαχειρίζεται πολύπλοκες αλληλεπιδράσεις μεταξύ πολλαπλών πρακτόρων. Βασίζεται σε μια αρχιτεκτονική τύπου γράφου που χρησιμοποιεί ένα [μοντέλο εκτέλεσης Pregel](https://kowshik.github.io/JPregel/pregel_paper.pdf), όπου η επεξεργασία γίνεται σε συγχρονισμένα βήματα που ονομάζονται "supersteps".

### Βασικά Συστατικά

Η αρχιτεκτονική αποτελείται από τρία βασικά μέρη:

1.  **Εκτελεστές**: Αυτές είναι οι βασικές μονάδες επεξεργασίας. Στα παραδείγματά μας, ένας `Agent` είναι ένας τύπος εκτελεστή. Κάθε εκτελεστής μπορεί να έχει πολλαπλούς χειριστές μηνυμάτων που καλούνται αυτόματα ανάλογα με τον τύπο του μηνύματος που λαμβάνεται.
2.  **Άκρες**: Καθορίζουν τη διαδρομή που ακολουθούν τα μηνύματα μεταξύ των εκτελεστών. Οι άκρες μπορούν να έχουν συνθήκες, επιτρέποντας δυναμική δρομολόγηση πληροφοριών μέσω του γράφου ροής εργασίας.
3.  **Workflow**: Αυτό το συστατικό ορχηστρώνει τη συνολική διαδικασία, διαχειρίζεται τους εκτελεστές, τις άκρες και τη συνολική ροή εκτέλεσης. Εξασφαλίζει ότι τα μηνύματα επεξεργάζονται με τη σωστή σειρά και ροές συμβάντων για παρατηρησιμότητα.

*Ένα διάγραμμα που παρουσιάζει τα βασικά συστατικά του συστήματος ροής εργασίας.*

Αυτή η δομή επιτρέπει τη δημιουργία ισχυρών και επεκτάσιμων εφαρμογών χρησιμοποιώντας βασικά πρότυπα όπως διαδοχικές αλυσίδες, fan-out/fan-in για παράλληλη επεξεργασία και λογική switch-case για υπό όρους ροές.

## 3\. Πρακτικά Παραδείγματα και Ανάλυση Κώδικα

Τώρα, ας εξερευνήσουμε πώς να υλοποιήσουμε διαφορετικά πρότυπα ροής εργασίας χρησιμοποιώντας το πλαίσιο. Θα δούμε κώδικα σε Python και .NET για κάθε παράδειγμα.

### Περίπτωση 1: Βασική Αλληλουχιακή Ροή Εργασίας

Αυτό είναι το απλούστερο πρότυπο, όπου η έξοδος ενός πράκτορα μεταβιβάζεται άμεσα σε έναν άλλο. Το σενάριό μας περιλαμβάνει έναν πράκτορα `FrontDesk` του ξενοδοχείου που κάνει μια ταξιδιωτική πρόταση, η οποία στη συνέχεια ελέγχεται από έναν πράκτορα `Concierge`.

*Διάγραμμα της βασικής ροής FrontDesk -> Concierge.*

#### Υπόβαθρο Σεναρίου

Ένας ταξιδιώτης ζητά μια πρόταση για το Παρίσι.

1.  Ο πράκτορας `FrontDesk`, σχεδιασμένος για συντομία, προτείνει επίσκεψη στο Μουσείο του Λούβρου.
2.  Ο πράκτορας `Concierge`, που δίνει προτεραιότητα σε αυθεντικές εμπειρίες, λαμβάνει αυτή την πρόταση. Εξετάζει την πρόταση και παρέχει ανατροφοδότηση, προτείνοντας μια πιο τοπική, λιγότερο τουριστική εναλλακτική.

#### Ανάλυση Υλοποίησης σε Python

Στο παράδειγμα Python, πρώτα ορίζουμε και δημιουργούμε τους δύο πράκτορες, ο καθένας με συγκεκριμένες οδηγίες.

```python
# 01.python-agent-framework-workflow-ghmodel-basic.ipynb

# Ορίστε ρόλους και οδηγίες πράκτορα
REVIEWER_NAME = "Concierge"
REVIEWER_INSTRUCTIONS = """
    You are an are hotel concierge who has opinions about providing the most local and authentic experiences for travelers...
    """

FRONTDESK_NAME = "FrontDesk"
FRONTDESK_INSTRUCTIONS = """
    You are a Front Desk Travel Agent with ten years of experience and are known for brevity...
    """

# Δημιουργία στιγμιότυπων πράκτορα
reviewer_agent = chat_client.as_agent(
    instructions=(REVIEWER_INSTRUCTIONS),
    name=REVIEWER_NAME,
)

front_desk_agent = chat_client.as_agent(
    instructions=(FRONTDESK_INSTRUCTIONS),
    name=FRONTDESK_NAME,
)
```

Έπειτα, ο `WorkflowBuilder` χρησιμοποιείται για να κατασκευάσει το γράφο. Ο `front_desk_agent` ορίζεται ως το αρχικό σημείο, και δημιουργείται μια άκρη που συνδέει την έξοδό του με τον `reviewer_agent`.

```python
# 01.python-agent-framework-workflow-ghmodel-basic.ipynb

workflow = WorkflowBuilder(start_executor=front_desk_agent).add_edge(front_desk_agent, reviewer_agent).build()
```

Τέλος, η ροή εργασίας εκτελείται με το αρχικό μήνυμα του χρήστη.

```python
# 01.python-agent-framework-workflow-ghmodel-basic.ipynb

result =''
# run εκτελεί τη ροή εργασίας· get_outputs() επιστρέφει το αποτέλεσμα του εκτελεστή εξόδου.
events = await workflow.run('I would like to go to Paris.')
outputs = events.get_outputs()
result = outputs[0].text if outputs else ''
```

#### Ανάλυση Υλοποίησης σε .NET (C#)

Η υλοποίηση .NET ακολουθεί παρόμοια λογική. Πρώτα καθορίζονται σταθερές για τα ονόματα και τις οδηγίες των πρακτόρων.

```csharp
// 01.dotnet-agent-framework-workflow-ghmodel-basic.ipynb

const string ReviewerAgentName = "Concierge";
const string ReviewerAgentInstructions = @"
    You are an are hotel concierge who has opinions about providing the most local and authentic experiences for travelers...";

const string FrontDeskAgentName = "FrontDesk";
const string FrontDeskAgentInstructions = @"""
    You are a Front Desk Travel Agent with ten years of experience and are known for brevity...";
```

Οι πράκτορες δημιουργούνται χρησιμοποιώντας έναν `AzureOpenAIClient` (API Responses) και στη συνέχεια ο `WorkflowBuilder` ορίζει τη διαδοχική ροή προσθέτοντας μια άκρη από τον `frontDeskAgent` στον `reviewerAgent`.

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

Η ροή εργασίας εκτελείται με το μήνυμα του χρήστη και τα αποτελέσματα μεταδίδονται σε ροή.

### Περίπτωση 2: Αλληλουχιακή Ροή Εργασίας με Πολλά Βήματα

Αυτό το πρότυπο επεκτείνει τη βασική αλληλουχιακή ροή για να συμπεριλάβει περισσότερους πράκτορες. Είναι ιδανικό για διαδικασίες που απαιτούν πολλαπλές φάσεις βελτίωσης ή μετασχηματισμού.

#### Υπόβαθρο Σεναρίου

Ένας χρήστης παρέχει μια εικόνα από ένα σαλόνι και ζητά προσφορά επίπλων.

1.  **Πράκτορας Πωλήσεων**: Αναγνωρίζει τα έπιπλα στην εικόνα και δημιουργεί μια λίστα.
2.  **Πράκτορας Τιμής**: Λαμβάνει τη λίστα με τα είδη και παρέχει αναλυτική κατάτμηση τιμών, περιλαμβάνοντας επιλογές προϋπολογισμού, μεσαίου εύρους και premium.
3.  **Πράκτορας Προσφοράς**: Λαμβάνει τη λίστα με τις τιμές και τη μορφοποιεί σε επίσημο έγγραφο προσφοράς σε Markdown.

*Διάγραμμα της ροής Sales -> Price -> Quote.*

#### Ανάλυση Υλοποίησης σε Python

Ορίζονται τρεις πράκτορες, έκαστος με εξειδικευμένο ρόλο. Η ροή εργασίας κατασκευάζεται χρησιμοποιώντας `add_edge` για τη δημιουργία της αλυσίδας: `sales_agent` -> `price_agent` -> `quote_agent`.

```python
# 02.python-agent-framework-workflow-ghmodel-sequential.ipynb

# Δημιουργήστε τρεις εξειδικευμένους πράκτορες
sales_agent = chat_client.as_agent(...)
price_agent = chat_client.as_agent(...)
quote_agent = chat_client.as_agent(...)

# Δημιουργήστε την αλληλουχία ροής εργασίας
workflow = WorkflowBuilder(start_executor=sales_agent).add_edge(sales_agent, price_agent).add_edge(price_agent, quote_agent).build()
```

Η είσοδος είναι ένα `ChatMessage` που περιλαμβάνει τόσο κείμενο όσο και το URI της εικόνας. Το πλαίσιο διαχειρίζεται τη μεταβίβαση της εξόδου κάθε πράκτορα στον επόμενο στη σειρά μέχρι να παραχθεί η τελική προσφορά.

```python
# 02.python-agent-framework-workflow-ghmodel-sequential.ipynb

# Το μήνυμα του χρήστη περιέχει τόσο κείμενο όσο και εικόνα
message = ChatMessage(
        role=Role.USER,
        contents=[
            TextContent(text="Please find the relevant furniture..."),
            DataContent(uri=image_uri, media_type="image/png")
        ]
)

# Εκτέλεσε τη ροή εργασίας
events = await workflow.run(message)
```

#### Ανάλυση Υλοποίησης σε .NET (C#)

Το παράδειγμα .NET μιμείται την έκδοση Python. Δημιουργούνται τρεις πράκτορες (`salesagent`, `priceagent`, `quoteagent`). Ο `WorkflowBuilder` τους συνδέει αλληλουχιακά.

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

Το μήνυμα του χρήστη κατασκευάζεται με τα δεδομένα της εικόνας (ως bytes) και το κείμενο. Η μέθοδος `InProcessExecution.StreamAsync` ξεκινά τη ροή εργασίας και η τελική έξοδος λαμβάνεται από τη ροή.

### Περίπτωση 3: Ταυτόχρονη Ροή Εργασίας

Αυτό το πρότυπο χρησιμοποιείται όταν οι εργασίες μπορούν να εκτελεστούν ταυτόχρονα για εξοικονόμηση χρόνου. Περιλαμβάνει "fan-out" σε πολλούς πράκτορες και "fan-in" για τη συγκέντρωση των αποτελεσμάτων.

#### Υπόβαθρο Σεναρίου

Ένας χρήστης ζητά να οργανωθεί ένα ταξίδι στο Σιάτλ.

1.  **Dispatcher (Fan-Out)**: Το αίτημα του χρήστη αποστέλλεται ταυτόχρονα σε δύο πράκτορες.
2.  **Πράκτορας Έρευνας**: Ερευνά αξιοθέατα, καιρό και βασικά σημεία για ταξίδι στο Σιάτλ τον Δεκέμβριο.
3.  **Πράκτορας Σχεδιασμού**: Δημιουργεί ανεξάρτητα ένα λεπτομερές πρόγραμμα ημέρας-προς-ημέρα.
4.  **Aggregator (Fan-In)**: Συγκεντρώνει και παρουσιάζει μαζί τα αποτελέσματα των ερευνητή και σχεδιαστή ως τελικό αποτέλεσμα.

*Διάγραμμα της ταυτόχρονης ροής Researcher και Planner.*

#### Ανάλυση Υλοποίησης σε Python

Ο `ConcurrentBuilder` απλοποιεί τη δημιουργία αυτού του προτύπου. Απλά απαριθμείτε τους συμμετέχοντες πράκτορες και ο builder δημιουργεί αυτόματα τη λογική fan-out και fan-in.

```python
# 03.python-agent-framework-workflow-ghmodel-concurrent.ipynb

research_agent = chat_client.as_agent(name="Researcher-Agent", ...)
plan_agent = chat_client.as_agent(name="Plan-Agent", ...)

# Το ConcurrentBuilder χειρίζεται τη λογική fan-out/fan-in
workflow = ConcurrentBuilder().participants([research_agent, plan_agent]).build()

# Εκτέλεση της ροής εργασίας
events = await workflow.run("Plan a trip to Seattle in December")
```

Το πλαίσιο εξασφαλίζει ότι οι `research_agent` και `plan_agent` εκτελούνται παράλληλα και οι τελικές εξόδους τους συλλέγονται σε λίστα.

#### Ανάλυση Υλοποίησης σε .NET (C#)

Στο .NET, αυτό το πρότυπο απαιτεί πιο ρητό ορισμό. Δημιουργούνται προσαρμοσμένοι εκτελεστές (`ConcurrentStartExecutor` και `ConcurrentAggregationExecutor`) για τη διαχείριση της λογικής fan-out και fan-in.

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

Ο `WorkflowBuilder` χρησιμοποιεί `AddFanOutEdge` και `AddFanInEdge` για να κατασκευάσει το γράφο με αυτούς τους προσαρμοσμένους εκτελεστές και τους πράκτορες.

```csharp
// 03.dotnet-agent-framework-workflow-ghmodel-concurrent.ipynb

var workflow = new WorkflowBuilder(startExecutor)
            .AddFanOutEdge(startExecutor, targets: [researcherAgent, plannerAgent])
            .AddFanInEdge(aggregationExecutor, sources: [researcherAgent, plannerAgent])
            .WithOutputFrom(aggregationExecutor)
            .Build();
```

### Περίπτωση 4: Υπό Όρους Ροή Εργασίας

Οι υπό όρους ροές εργασίας εισάγουν διακλαδώσεις λογικής, επιτρέποντας στο σύστημα να ακολουθεί διαφορετικές διαδρομές βάσει ενδιάμεσων αποτελεσμάτων.

#### Υπόβαθρο Σεναρίου

Αυτή η ροή εργασίας αυτοματοποιεί τη δημιουργία και δημοσίευση ενός τεχνικού σεμιναρίου.

1.  **Πράκτορας Ευαγγελιστή**: Γράφει προσχέδιο του σεμιναρίου με βάση ένα δοσμένο περίγραμμα και URLs.
2.  **Πράκτορας Επαλήθευσης Περιεχομένου**: Εξετάζει το προσχέδιο. Ελέγχει αν ο αριθμός λέξεων είναι πάνω από 200.
3.  **Υπό Όρους Κλάδος**:
      * **Εάν Εγκριθεί (`Ναι`)**: Η ροή εργασίας συνεχίζει στον `Publisher-Agent`.
      * **Εάν Απορριφθεί (`Όχι`)**: Η ροή εργασίας σταματά και εξάγει τον λόγο απόρριψης.
4.  **Πράκτορας Δημοσίευσης**: Αν το προσχέδιο εγκριθεί, αυτός ο πράκτορας αποθηκεύει το περιεχόμενο σε αρχείο Markdown.

#### Ανάλυση Υλοποίησης σε Python

Αυτό το παράδειγμα χρησιμοποιεί μια προσαρμοσμένη συνάρτηση, `select_targets`, για να υλοποιήσει τη λογική υπό όρων. Η συνάρτηση αυτή περνά στο `add_multi_selection_edge_group` και κατευθύνει τη ροή εργασίας βάσει του πεδίου `review_result` από την έξοδο του αξιολογητή.

```python
# 04.python-agent-framework-workflow-aifoundry-condition.ipynb

# Αυτή η λειτουργία καθορίζει το επόμενο βήμα με βάση το αποτέλεσμα της αξιολόγησης
def select_targets(review: ReviewResult, target_ids: list[str]) -> list[str]:
    handle_review_id, save_draft_id = target_ids
    if review.review_result == "Yes":
        # Εάν εγκριθεί, προχωρήστε στον εκτελεστή 'save_draft'
        return [save_draft_id]
    else:
        # Εάν απορριφθεί, προχωρήστε στον εκτελεστή 'handle_review' για να αναφέρετε αποτυχία
        return [handle_review_id]

# Ο κατασκευαστής ροής εργασίας χρησιμοποιεί τη λειτουργία επιλογής για δρομολόγηση
workflow = (
    WorkflowBuilder()
        .set_start_executor(evangelist_agent)
        .add_edge(evangelist_agent, reviewer_agent)
        .add_edge(reviewer_agent, to_reviewer_result)
        # Η άκρη πολλαπλής επιλογής υλοποιεί τη συνθηματική λογική
        .add_multi_selection_edge_group(
            to_reviewer_result,
            [handle_review, save_draft],
            selection_func=select_targets,
        )
        .add_edge(save_draft, publisher_agent)
        .build()
)
```

Προσαρμοσμένοι εκτελεστές όπως `to_reviewer_result` χρησιμοποιούνται για να αναλύσουν την έξοδο JSON από τους πράκτορες και να την μετατρέψουν σε ισχυρά τυποποιημένα αντικείμενα για να μπορεί να τα ελέγχει η συνάρτηση επιλογής.

#### Ανάλυση Υλοποίησης σε .NET (C#)

Η έκδοση .NET ακολουθεί παρόμοια προσέγγιση με μια συνάρτηση συνθήκης. Ορίζεται μια `Func<object?, bool>` που ελέγχει την ιδιότητα `Result` του αντικειμένου `ReviewResult`.

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

Η μέθοδος `AddEdge` χρησιμοποιεί το παράμετρο `condition` ώστε ο `WorkflowBuilder` να δημιουργήσει διακλαδώσεις διαδρομών. Η ροή θα ακολουθήσει την άκρη προς τον `publishExecutor` μόνο αν η συνθήκη `GetCondition(expectedResult: "Yes")` επιστρέψει αληθής. Διαφορετικά, ακολουθεί τη διαδρομή προς τον `sendReviewerExecutor`.

## Συμπέρασμα

Το Microsoft Agent Framework Workflow παρέχει ένα ισχυρό και ευέλικτο θεμέλιο για την ορχήστρωση πολύπλοκων συστημάτων πολλαπλών πρακτόρων. Εκμεταλλευόμενο την αρχιτεκτονική βασισμένη σε γράφους και τα βασικά συστατικά του, οι προγραμματιστές μπορούν να σχεδιάσουν και να υλοποιήσουν εξελιγμένες ροές εργασίας τόσο σε Python όσο και σε .NET. Είτε η εφαρμογή σας απαιτεί απλή αλληλουχιακή επεξεργασία, παράλληλη εκτέλεση ή δυναμική λογική υπό όρους, το πλαίσιο προσφέρει τα εργαλεία για την κατασκευή ισχυρών, επεκτάσιμων και τύπου ασφαλών λύσεων AI-powered.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Αποποίηση ευθυνών**:
Αυτό το έγγραφο έχει μεταφραστεί χρησιμοποιώντας την υπηρεσία μετάφρασης με τεχνητή νοημοσύνη [Co-op Translator](https://github.com/Azure/co-op-translator). Ενώ επιδιώκουμε την ακρίβεια, παρακαλούμε να έχετε υπόψη ότι οι αυτοματοποιημένες μεταφράσεις ενδέχεται να περιέχουν λάθη ή ανακρίβειες. Το πρωτότυπο έγγραφο στη μητρική του γλώσσα πρέπει να θεωρείται η αυθεντική πηγή. Για κρίσιμες πληροφορίες, συνιστάται επαγγελματική ανθρώπινη μετάφραση. Δεν φέρουμε ευθύνη για τυχόν παρεξηγήσεις ή λανθασμένες ερμηνείες που προκύπτουν από τη χρήση αυτής της μετάφρασης.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->