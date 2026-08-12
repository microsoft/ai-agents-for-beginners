# Εξερεύνηση του Πλαισίου Microsoft Agent

![Agent Framework](../../../translated_images/el/lesson-14-thumbnail.90df0065b9d234ee.webp)

### Εισαγωγή

Αυτό το μάθημα θα καλύψει:

- Κατανόηση του Πλαισίου Microsoft Agent: Κύρια χαρακτηριστικά και αξία  
- Εξερεύνηση των βασικών εννοιών του Πλαισίου Microsoft Agent
- Προηγμένα πρότυπα MAF: Ροές εργασίας, ενδιάμεσο λογισμικό και μνήμη

## Στόχοι Μάθησης

Μετά την ολοκλήρωση αυτού του μαθήματος, θα γνωρίζετε πώς να:

- Δημιουργείτε έτοιμους για παραγωγή AI Agents χρησιμοποιώντας το Πλαίσιο Microsoft Agent
- Εφαρμόζετε τα βασικά χαρακτηριστικά του Πλαισίου Microsoft Agent στις περιπτώσεις χρήσης Agentic σας
- Χρησιμοποιείτε προηγμένα πρότυπα που περιλαμβάνουν ροές εργασίας, ενδιάμεσο λογισμικό και παρατηρησιμότητα

## Παραδείγματα Κώδικα 

Παραδείγματα κώδικα για [Microsoft Agent Framework (MAF)](https://aka.ms/ai-agents-beginners/agent-framework) βρίσκονται σε αυτό το αποθετήριο κάτω από τα αρχεία `xx-python-agent-framework` και `xx-dotnet-agent-framework`.

## Κατανόηση του Πλαισίου Microsoft Agent

![Framework Intro](../../../translated_images/el/framework-intro.077af16617cf130c.webp)

[Microsoft Agent Framework (MAF)](https://aka.ms/ai-agents-beginners/agent-framework) είναι το ενιαίο πλαίσιο της Microsoft για τη δημιουργία AI agents. Προσφέρει ευελιξία για την αντιμετώπιση της μεγάλης ποικιλίας περιπτώσεων χρήσης agentic που βλέπουμε σε παραγωγικά και ερευνητικά περιβάλλοντα, συμπεριλαμβανομένων:

- **Διαδοχική ορχήστρωση Agent** σε σενάρια όπου απαιτούνται ροές εργασίας βήμα προς βήμα.
- **Παράλληλη ορχήστρωση** σε σενάρια όπου οι agents πρέπει να ολοκληρώσουν εργασίες ταυτόχρονα.
- **Ορχήστρωση ομάδας συνομιλίας** σε σενάρια όπου οι agents μπορούν να συνεργαστούν σε μία εργασία.
- **Ορχήστρωση παράδοσης** σε σενάρια όπου οι agents παραδίδουν την εργασία ο ένας στον άλλο καθώς ολοκληρώνονται τα υπο-καθήκοντα.
- **Μαγνητική ορχήστρωση** σε σενάρια όπου ένας διαχειριστής agent δημιουργεί και τροποποιεί μια λίστα εργασιών και χειρίζεται το συντονισμό των υποagents για να ολοκληρωθεί η εργασία.

Για την παράδοση AI Agents σε παραγωγή, το MAF περιλαμβάνει επίσης λειτουργίες για:

- **Παρατηρησιμότητα** μέσω της χρήσης του OpenTelemetry όπου κάθε ενέργεια του AI Agent συμπεριλαμβανομένης της κλήσης εργαλείων, βημάτων ορχήστρωσης, ροών λογικής και παρακολούθησης απόδοσης μέσω των πινάκων οργάνων Microsoft Foundry.
- **Ασφάλεια** φιλοξενώντας τους agents ιθαγενώς στο Microsoft Foundry το οποίο περιλαμβάνει ελέγχους ασφαλείας όπως πρόσβαση βασισμένη σε ρόλους, χειρισμό ιδιωτικών δεδομένων και ενσωματωμένη ασφάλεια περιεχομένου.
- **Αντοχή** καθώς τα νήματα και οι ροές εργασίας των agents μπορούν να παύσουν, να συνεχίσουν και να ανακάμψουν από σφάλματα, επιτρέποντας μακρύτερης διάρκειας διαδικασίες.
- **Έλεγχο** καθώς υποστηρίζονται ροές εργασίας με ανθρώπινη παρέμβαση όπου οι εργασίες επισημαίνονται ως απαιτούμενες για ανθρώπινη έγκριση.

Το Microsoft Agent Framework εστιάζει επίσης στο να είναι διαλειτουργικό μέσω:

- **Ανεξαρτησία από το Cloud** - Οι agents μπορούν να τρέχουν σε containers, on-premises και σε πολλαπλά διαφορετικά clouds.
- **Ανεξαρτησία από τον πάροχο** - Οι agents μπορούν να δημιουργηθούν μέσω του προτιμώμενου SDK σας, συμπεριλαμβανομένων των Azure OpenAI και OpenAI
- **Ενσωμάτωση Ανοιχτών Προτύπων** - Οι agents μπορούν να χρησιμοποιούν πρωτόκολλα όπως Agent-to-Agent (A2A) και Model Context Protocol (MCP) για να ανακαλύπτουν και να χρησιμοποιούν άλλους agents και εργαλεία.
- **Plugins και Συνδέσεις** - Πραγματοποιούνται συνδέσεις με υπηρεσίες δεδομένων και μνήμης όπως Microsoft Fabric, SharePoint, Pinecone και Qdrant.

Ας δούμε πώς αυτά τα χαρακτηριστικά εφαρμόζονται σε μερικές από τις βασικές έννοιες του Microsoft Agent Framework.

## Βασικές Έννοιες του Microsoft Agent Framework

### Agents

![Agent Framework](../../../translated_images/el/agent-components.410a06daf87b4fef.webp)

**Δημιουργία Agents**

Η δημιουργία ενός agent γίνεται ορίζοντας την υπηρεσία συμπερασμού (Πάροχος LLM), ένα
σύνολο οδηγιών που πρέπει να ακολουθήσει ο AI Agent, και ένα εκχωρημένο `name`:

```python
agent = AzureOpenAIChatClient(credential=AzureCliCredential()).create_agent( instructions="You are good at recommending trips to customers based on their preferences.", name="TripRecommender" )
```

Το παραπάνω χρησιμοποιεί το `Azure OpenAI` αλλά οι agents μπορούν να δημιουργηθούν χρησιμοποιώντας ποικιλία υπηρεσιών, συμπεριλαμβανομένης της `Microsoft Foundry Agent Service`:

```python
AzureAIAgentClient(async_credential=credential).create_agent( name="HelperAgent", instructions="You are a helpful assistant." ) as agent
```

OpenAI `Responses`, `ChatCompletion` APIs

```python
agent = OpenAIResponsesClient().create_agent( name="WeatherBot", instructions="You are a helpful weather assistant.", )
```

```python
agent = OpenAIChatClient().create_agent( name="HelpfulAssistant", instructions="You are a helpful assistant.", )
```

ή [MiniMax](https://platform.minimaxi.com/), που παρέχει API συμβατό με το OpenAI με μεγάλα παράθυρα πλαισίου (έως 204K tokens):

```python
agent = OpenAIChatClient(base_url="https://api.minimax.io/v1", api_key=os.environ["MINIMAX_API_KEY"], model_id="MiniMax-M3").create_agent( name="HelpfulAssistant", instructions="You are a helpful assistant.", )
```

ή απομακρυσμένους agents χρησιμοποιώντας το πρωτόκολλο A2A:

```python
agent = A2AAgent( name=agent_card.name, description=agent_card.description, agent_card=agent_card, url="https://your-a2a-agent-host" )
```

**Εκτέλεση Agents**

Οι agents εκτελούνται χρησιμοποιώντας τις μεθόδους `.run` ή `.run_stream` για είτε απαντήσεις χωρίς streaming είτε με streaming.

```python
result = await agent.run("What are good places to visit in Amsterdam?")
print(result.text)
```

```python
async for update in agent.run_stream("What are the good places to visit in Amsterdam?"):
    if update.text:
        print(update.text, end="", flush=True)

```

Κάθε εκτέλεση agent μπορεί επίσης να έχει επιλογές για προσαρμογή παραμέτρων όπως τα `max_tokens` που χρησιμοποιούνται από τον agent, τα `tools` που ο agent μπορεί να καλέσει, και ακόμη και το ίδιο το `model` που χρησιμοποιείται για τον agent.

Αυτό είναι χρήσιμο σε περιπτώσεις όπου απαιτούνται συγκεκριμένα μοντέλα ή εργαλεία για να ολοκληρωθεί η εργασία ενός χρήστη.

**Εργαλεία**

Τα εργαλεία μπορούν να οριστούν τόσο κατά τον ορισμό του agent:

```python
def get_attractions( location: Annotated[str, Field(description="The location to get the top tourist attractions for")], ) -> str: """Get the top tourist attractions for a given location.""" return f"The top attractions for {location} are." 


# Όταν δημιουργείτε έναν ChatAgent απευθείας

agent = ChatAgent( chat_client=OpenAIChatClient(), instructions="You are a helpful assistant", tools=[get_attractions]

```

και επίσης κατά την εκτέλεση του agent:

```python

result1 = await agent.run( "What's the best place to visit in Seattle?", tools=[get_attractions] # Εργαλείο παρεχόμενο μόνο για αυτή την εκτέλεση )
```

**Νήματα Agent**

Τα νήματα Agent χρησιμοποιούνται για να χειριστούν συνομιλίες με πολλούς γύρους. Τα νήματα μπορούν να δημιουργηθούν είτε:

- Χρησιμοποιώντας το `get_new_thread()` που επιτρέπει το νήμα να αποθηκευτεί με την πάροδο του χρόνου
- Δημιουργώντας αυτόματα ένα νήμα κατά την εκτέλεση ενός agent και το νήμα να διαρκεί μόνο κατά την τρέχουσα εκτέλεση.

Για να δημιουργήσετε ένα νήμα, ο κώδικας φαίνεται έτσι:

```python
# Δημιουργήστε ένα νέο νήμα.
thread = agent.get_new_thread() # Εκτέλεση του πράκτορα με το νήμα.
response = await agent.run("Hello, I am here to help you book travel. Where would you like to go?", thread=thread)

```

Στη συνέχεια μπορείτε να σειριοποιήσετε το νήμα για αποθήκευση προς μεταγενέστερη χρήση:

```python
# Δημιουργήστε ένα νέο νήμα.
thread = agent.get_new_thread() 

# Εκτελέστε τον πράκτορα με το νήμα.

response = await agent.run("Hello, how are you?", thread=thread) 

# Σειριοποιήστε το νήμα για αποθήκευση.

serialized_thread = await thread.serialize() 

# Αποσειριοποιήστε την κατάσταση του νήματος μετά τη φόρτωση από την αποθήκη.

resumed_thread = await agent.deserialize_thread(serialized_thread)
```

**Ενδιάμεσο λογισμικό Agent**

Οι agents αλληλεπιδρούν με εργαλεία και LLMs για να ολοκληρώσουν τις εργασίες των χρηστών. Σε ορισμένα σενάρια, θέλουμε να εκτελέσουμε ή να παρακολουθήσουμε τη διαδικασία ανάμεσα σε αυτές τις αλληλεπιδράσεις. Το ενδιάμεσο λογισμικό agent μας το επιτρέπει μέσω:

*Ενδιάμεσο λογισμικό λειτουργίας*

Αυτό το ενδιάμεσο λογισμικό μας επιτρέπει να εκτελέσουμε μια ενέργεια μεταξύ του agent και μιας λειτουργίας/εργαλείου που θα καλεί. Ένα παράδειγμα χρήσης είναι η καταγραφή κλήσης λειτουργίας.

Στον παρακάτω κώδικα, το `next` ορίζει αν το επόμενο ενδιάμεσο λογισμικό ή η πραγματική λειτουργία πρέπει να κληθεί.

```python
async def logging_function_middleware(
    context: FunctionInvocationContext,
    next: Callable[[FunctionInvocationContext], Awaitable[None]],
) -> None:
    """Function middleware that logs function execution."""
    # Προεπεξεργασία: Καταγραφή πριν από την εκτέλεση της συνάρτησης
    print(f"[Function] Calling {context.function.name}")

    # Συνεχίστε στο επόμενο middleware ή στην εκτέλεση της συνάρτησης
    await next(context)

    # Μετα-επεξεργασία: Καταγραφή μετά την εκτέλεση της συνάρτησης
    print(f"[Function] {context.function.name} completed")
```

*Ενδιάμεσο λογισμικό συνομιλίας*

Αυτό το ενδιάμεσο λογισμικό μας επιτρέπει να εκτελέσουμε ή να καταγράψουμε μια ενέργεια ανάμεσα στον agent και τα αιτήματα προς το LLM.

Αυτό περιέχει σημαντικές πληροφορίες όπως τα `messages` που στέλνονται στην υπηρεσία AI.

```python
async def logging_chat_middleware(
    context: ChatContext,
    next: Callable[[ChatContext], Awaitable[None]],
) -> None:
    """Chat middleware that logs AI interactions."""
    # Προεπεξεργασία: Καταγραφή πριν από την κλήση AI
    print(f"[Chat] Sending {len(context.messages)} messages to AI")

    # Συνέχεια στο επόμενο middleware ή υπηρεσία AI
    await next(context)

    # Μετα-επεξεργασία: Καταγραφή μετά την απάντηση AI
    print("[Chat] AI response received")

```

**Μνήμη Agent**

Όπως καλύφθηκε στο μάθημα `Agentic Memory`, η μνήμη είναι ένα σημαντικό στοιχείο που επιτρέπει στον agent να λειτουργεί σε διαφορετικά συμφραζόμενα. Το MAF προσφέρει διάφορους τύπους μνήμης:

*Μνήμη στη Ροή*

Αυτή είναι η μνήμη που αποθηκεύεται στα νήματα κατά το χρόνο εκτέλεσης της εφαρμογής.

```python
# Δημιουργήστε ένα νέο νήμα.
thread = agent.get_new_thread() # Εκτελέστε το πράκτορα με το νήμα.
response = await agent.run("Hello, I am here to help you book travel. Where would you like to go?", thread=thread)
```

*Μόνιμα Μηνύματα*

Αυτή η μνήμη χρησιμοποιείται κατά την αποθήκευση ιστορικού συνομιλιών μεταξύ διαφορετικών συνεδριών. Ορίζεται με τη χρήση του `chat_message_store_factory` :

```python
from agent_framework import ChatMessageStore

# Δημιουργήστε ένα προσαρμοσμένο κατάστημα μηνυμάτων
def create_message_store():
    return ChatMessageStore()

agent = ChatAgent(
    chat_client=OpenAIChatClient(),
    instructions="You are a Travel assistant.",
    chat_message_store_factory=create_message_store
)

```

*Δυναμική Μνήμη*

Αυτή η μνήμη προστίθεται στο συμφραζόμενο πριν τρέξουν οι agents. Αυτές οι μνήμες μπορούν να αποθηκευτούν σε εξωτερικές υπηρεσίες όπως το mem0:

```python
from agent_framework.mem0 import Mem0Provider

# Χρήση Mem0 για προχωρημένες δυνατότητες μνήμης
memory_provider = Mem0Provider(
    api_key="your-mem0-api-key",
    user_id="user_123",
    application_id="my_app"
)

agent = ChatAgent(
    chat_client=OpenAIChatClient(),
    instructions="You are a helpful assistant with memory.",
    context_providers=memory_provider
)

```

**Παρατηρησιμότητα Agent**

Η παρατηρησιμότητα είναι σημαντική για την κατασκευή αξιόπιστων και διαχειρίσιμων συστημάτων agentic. Το MAF ενσωματώνεται με το OpenTelemetry για να παρέχει ιχνηλάτηση και μετρητές για καλύτερη παρατηρησιμότητα.

```python
from agent_framework.observability import get_tracer, get_meter

tracer = get_tracer()
meter = get_meter()
with tracer.start_as_current_span("my_custom_span"):
    # κάνε κάτι
    pass
counter = meter.create_counter("my_custom_counter")
counter.add(1, {"key": "value"})
```

### Ροές Εργασίας

Το MAF προσφέρει ροές εργασίας που είναι προκαθορισμένα βήματα για την ολοκλήρωση μιας εργασίας και περιλαμβάνουν AI agents ως συνιστώσες σε αυτά τα βήματα.

Οι ροές εργασίας αποτελούνται από διάφορα στοιχεία που επιτρέπουν καλύτερο έλεγχο ροής. Επίσης επιτρέπουν **πολλαπλή ορχήστρωση agents** και **checkpointing** για την αποθήκευση καταστάσεων ροής εργασίας.

Τα βασικά στοιχεία μιας ροής εργασίας είναι:

**Εκτελεστές**

Οι εκτελεστές λαμβάνουν εισερχόμενα μηνύματα, εκτελούν τις ανατεθειμένες εργασίες τους και στη συνέχεια παράγουν ένα εξερχόμενο μήνυμα. Αυτό προωθεί τη ροή εργασίας προς την ολοκλήρωση της μεγαλύτερης εργασίας. Οι εκτελεστές μπορεί να είναι είτε AI agent είτε προσαρμοσμένη λογική.

**Ακμές**

Οι ακμές χρησιμοποιούνται για να ορίσουν τη ροή των μηνυμάτων σε μια ροή εργασίας. Αυτές μπορεί να είναι:

*Άμεσες Ακμές* - Απλές συνδέσεις ένα προς ένα μεταξύ των εκτελεστών:

```python
from agent_framework import WorkflowBuilder

builder = WorkflowBuilder()
builder.add_edge(source_executor, target_executor)
builder.set_start_executor(source_executor)
workflow = builder.build()
```

*Υποκείμενες Ακμές* - Ενεργοποιούνται αφού πληρούται μια συγκεκριμένη προϋπόθεση. Για παράδειγμα, όταν δεν είναι διαθέσιμα δωμάτια ξενοδοχείου, ένας εκτελεστής μπορεί να προτείνει άλλες επιλογές.

*Ακμές επιλογής* - Κατευθύνουν μηνύματα σε διαφορετικούς εκτελεστές με βάση ορισμένες προϋποθέσεις. Για παράδειγμα, αν πελάτης ταξιδιού έχει προτεραιότητα πρόσβασης, οι εργασίες του θα χειρίζονται μέσω άλλης ροής εργασίας.

*Ακμές πολλαπλού προορισμού* - Στέλνουν ένα μήνυμα σε πολλαπλούς παραλήπτες.

*Ακμές πολλαπλού εισερχόμενου* - Συλλέγουν πολλαπλά μηνύματα από διαφορετικούς εκτελεστές και τα στέλνουν σε έναν παραλήπτη.

**Γεγονότα**

Για καλύτερη παρατηρησιμότητα στις ροές εργασίας, το MAF προσφέρει ενσωματωμένα γεγονότα για την εκτέλεση περιλαμβανομένων:

- `WorkflowStartedEvent`  - Η εκτέλεση της ροής εργασίας ξεκινά
- `WorkflowOutputEvent` - Η ροή εργασίας παράγει ένα αποτέλεσμα
- `WorkflowErrorEvent` - Η ροή εργασίας αντιμετωπίζει σφάλμα
- `ExecutorInvokeEvent`  - Ο εκτελεστής ξεκινά την επεξεργασία
- `ExecutorCompleteEvent`  -  Ο εκτελεστής ολοκληρώνει την επεξεργασία
- `RequestInfoEvent` - Ένα αίτημα εκδίδεται

## Προηγμένα Πρότυπα MAF

Τα παραπάνω τμήματα καλύπτουν τις βασικές έννοιες του Microsoft Agent Framework. Καθώς δημιουργείτε πιο σύνθετους agents, εδώ είναι μερικά προηγμένα πρότυπα που πρέπει να εξετάσετε:

- **Σύνθεση Ενδιάμεσου λογισμικού**: Αλληλουχία πολλών ενδιάμεσων χειριστών (καταγραφή, έλεγχος ταυτότητας, περιορισμός ρυθμού) χρησιμοποιώντας λειτουργία και συνομιλιακό ενδιάμεσο λογισμικό για λεπτομερή έλεγχο της συμπεριφοράς του agent.
- **Αποθήκευση ελέγχων ροής εργασίας**: Χρησιμοποιήστε γεγονότα ροής εργασίας και σειριοποίηση για να αποθηκεύσετε και να συνεχίσετε μακροχρόνιες διαδικασίες agent.
- **Δυναμική επιλογή εργαλείων**: Συνδυάστε RAG πάνω σε περιγραφές εργαλείων με την εγγραφή εργαλείων του MAF για να παρουσιάσετε μόνο σχετικά εργαλεία ανά ερώτημα.
- **Πολυ-ταξινόμηση παραδόσεων**: Χρησιμοποιήστε ακμές ροής εργασίας και υπό όρους δρομολόγηση για να οργανώσετε παραδόσεις μεταξύ εξειδικευμένων agents.

## Φιλοξενία Agents LangChain / LangGraph στο Microsoft Foundry

Το Microsoft Agent Framework είναι **διαλειτουργικό πλαίσιο** — δεν περιορίζεστε στους agents που έχουν γραφτεί με το MAF. Αν έχετε ήδη έναν agent που έχει δημιουργηθεί με **LangChain** ή **LangGraph**, μπορείτε να τον τρέξετε ως **hosted agent στο Microsoft Foundry** ώστε το Foundry να διαχειρίζεται το runtime, τις συνεδρίες, την κλιμάκωση, την ταυτότητα και τα endpoints πρωτοκόλλου για εσάς, ενώ η λογική του agent παραμένει στο LangGraph.

Αυτό επιτυγχάνεται με το πακέτο `langchain_azure_ai.agents.hosting`, που εκθέτει έναν συναρμολογημένο γράφο LangGraph πάνω στα ίδια πρωτόκολλα που χρησιμοποιούν οι hosted agents του Foundry.

**1. Εγκαταστήστε το πρόσθετο φιλοξενίας:**

```bash
pip install -U "langchain-azure-ai[hosting]>=1.2.4" azure-identity
```

Το πρόσθετο `hosting` εγκαθιστά τις βιβλιοθήκες πρωτοκόλλου Foundry: `azure-ai-agentserver-responses` (το endpoint `/responses` συμβατό με το OpenAI) και `azure-ai-agentserver-invocations` (το γενικό endpoint `/invocations`).

**2. Επιλέξτε πρωτόκολλο φιλοξενίας:**

| Πρωτόκολλο | Κλάση host | Endpoint | Χρήση όταν |
|----------|-----------|----------|----------|
| **Responses** | `ResponsesHostServer` | `/responses` | Θέλετε συνομιλία συμβατή με OpenAI, streaming, ιστορικό απαντήσεων και νηματοποίηση συνομιλιών — η προτεινόμενη προεπιλογή για συνομιλιακούς agents. |
| **Invocations** | `InvocationsHostServer` | `/invocations` | Χρειάζεστε προσαρμοσμένο σχήμα JSON, endpoint τύπου webhook ή μη συνομιλιακή επεξεργασία. |

Επειδή η **API Responses είναι η πρωταρχική API για την ανάπτυξη agents στο Foundry**, ξεκινήστε με το `ResponsesHostServer` για τους περισσότερους agents.

**3. Διαμορφώστε μεταβλητές περιβάλλοντος** (`az login` πρώτα ώστε το `DefaultAzureCredential` να μπορέσει να αυθεντικοποιήσει):

```bash
export FOUNDRY_PROJECT_ENDPOINT="https://<resource>.services.ai.azure.com/api/projects/<project>"
export FOUNDRY_MODEL_NAME="gpt-5-mini"
```

Όταν ο agent τρέχει αργότερα ως hosted agent στο Foundry, η πλατφόρμα εγχέει αυτόματα το `FOUNDRY_PROJECT_ENDPOINT`.

**4. Εκθέστε έναν agent LangGraph μέσω του πρωτοκόλλου Responses:**

```python
import os

from azure.ai.projects import AIProjectClient
from azure.identity import DefaultAzureCredential, get_bearer_token_provider
from langchain.agents import create_agent
from langchain_openai import ChatOpenAI
from langchain_azure_ai.agents.hosting import ResponsesHostServer

_AZURE_AI_SCOPE = "https://ai.azure.com/.default"


def build_chat_model() -> ChatOpenAI:
    project_endpoint = os.environ["FOUNDRY_PROJECT_ENDPOINT"].rstrip("/")
    deployment = os.environ.get("FOUNDRY_MODEL_NAME", "gpt-5-mini")
    credential = DefaultAzureCredential()
    project = AIProjectClient(endpoint=project_endpoint, credential=credential)
    openai_client = project.get_openai_client()
    token_provider = get_bearer_token_provider(credential, _AZURE_AI_SCOPE)

    # Το ChatOpenAI εδώ στοχεύει στο συμβατό με OpenAI τελικό σημείο (Responses) του έργου Foundry.
    return ChatOpenAI(
        model=deployment,
        base_url=str(openai_client.base_url),
        api_key=token_provider,
    )


def main() -> None:
    graph = create_agent(build_chat_model(), tools=[])
    port = int(os.environ.get("PORT", "8088"))
    ResponsesHostServer(graph).run(port=port)


if __name__ == "__main__":
    main()
```

Τρέξτε το τοπικά με `python main.py`, στη συνέχεια στείλτε ένα αίτημα Responses στο `http://localhost:8088/responses`.

**Βασικές συμπεριφορές:**

- **Συνομιλίες**: Οι πελάτες συνεχίζουν μια συνομιλία περνώντας `previous_response_id` ή ένα `conversation` ID. Αν ο γράφος σας έχει συναρμολογηθεί με LangGraph checkpointer, το Foundry συνδέει την κατάσταση συνομιλίας με τον έλεγχό (χρησιμοποιήστε έναν ανθεκτικό checkpointer για παραγωγή· το `MemorySaver` είναι εντάξει για τοπικές δοκιμές).
- **Ανθρώπινη παρέμβαση**: Αν ο γράφος σας χρησιμοποιεί LangGraph `interrupt()`, το `ResponsesHostServer` εμφανίζει την εκκρεμής διακοπή ως στοιχείο `function_call` / `mcp_approval_request` των Responses, και οι πελάτες συνεχίζουν με ένα αντίστοιχο `function_call_output` / `mcp_approval_response`.
- **Ανάπτυξη στο Foundry**: Χρησιμοποιήστε το Azure Developer CLI — `azd ext install azure.ai.agents`, `azd ai agent init -m <manifest>`, `azd ai agent run` (τοπικά, απαιτεί Docker), μετά `azd provision` και `azd deploy`. Η ανάπτυξη hosted agent απαιτεί το ρόλο **Foundry Project Manager**.

Μια εκτελέσιμη έκδοση αυτού του παραδείγματος βρίσκεται στο [code-samples/14-langchain-hosted-agent.py](../../../14-microsoft-agent-framework/code-samples/14-langchain-hosted-agent.py). Για πλήρη οδηγό (πρωτόκολλο Invocations, προσαρμοσμένα σχήματα αιτήσεων και αντιμετώπιση προβλημάτων), δείτε το [Host LangGraph agents as Foundry hosted agents](https://learn.microsoft.com/azure/foundry/how-to/develop/langchain-hosted-agents).

## Παραδείγματα Κώδικα 

Παραδείγματα κώδικα για το Microsoft Agent Framework βρίσκονται σε αυτό το αποθετήριο κάτω από τα αρχεία `xx-python-agent-framework` και `xx-dotnet-agent-framework`.

## Έχετε Περισσότερες Ερωτήσεις Για το Microsoft Agent Framework;

Εγγραφείτε στο [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D) για να συναντήσετε άλλους μαθητές, να παρακολουθήσετε ώρες γραφείου και να λάβετε απαντήσεις στις ερωτήσεις σας για AI Agents.
## Προηγούμενο Μάθημα

[Μνήμη για AI Agents](../13-agent-memory/README.md)

## Επόμενο Μάθημα

[Δημιουργία Agents Χρήσης Υπολογιστή (CUA)](../15-browser-use/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Αποποίηση ευθυνών**:
Αυτό το έγγραφο έχει μεταφραστεί χρησιμοποιώντας την υπηρεσία μετάφρασης με τεχνητή νοημοσύνη [Co-op Translator](https://github.com/Azure/co-op-translator). Ενώ επιδιώκουμε την ακρίβεια, παρακαλούμε να έχετε υπόψη ότι οι αυτοματοποιημένες μεταφράσεις ενδέχεται να περιέχουν λάθη ή ανακρίβειες. Το πρωτότυπο έγγραφο στη μητρική του γλώσσα πρέπει να θεωρείται η αυθεντική πηγή. Για κρίσιμες πληροφορίες, συνιστάται επαγγελματική ανθρώπινη μετάφραση. Δεν φέρουμε ευθύνη για τυχόν παρεξηγήσεις ή λανθασμένες ερμηνείες που προκύπτουν από τη χρήση αυτής της μετάφρασης.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->