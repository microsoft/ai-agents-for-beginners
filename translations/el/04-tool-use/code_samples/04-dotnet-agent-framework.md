# 🛠️ Προχωρημένη Χρήση Εργαλείων με Azure OpenAI (Responses API) (.NET)

## 📋 Μαθησιακοί Στόχοι

Αυτό το σημειωματάριο παρουσιάζει πρότυπα ενσωμάτωσης εργαλείων επιπέδου επιχειρήσεων χρησιμοποιώντας το Microsoft Agent Framework σε .NET με Azure OpenAI (Responses API). Θα μάθετε να δημιουργείτε εξελιγμένους πράκτορες με πολλαπλά εξειδικευμένα εργαλεία, αξιοποιώντας τη στατική τυποποίηση της C# και τις δυνατότητες επιχειρησιακού επιπέδου του .NET.

### Προχωρημένες Δυνατότητες Εργαλείων που θα Κυριαρχήσετε

- 🔧 **Αρχιτεκτονική Πολλαπλών Εργαλείων**: Δημιουργία πρακτόρων με πολλαπλές εξειδικευμένες δυνατότητες  
- 🎯 **Εκτέλεση Εργαλείων με Ασφάλεια Τύπων**: Αξιοποίηση της επαλήθευσης κατά το compile-time της C#  
- 📊 **Πρότυπα Εργαλείων Επιχειρήσεων**: Σχεδιασμός εργαλείων έτοιμων για παραγωγή και διαχείριση σφαλμάτων  
- 🔗 **Σύνθεση Εργαλείων**: Συνδυασμός εργαλείων για σύνθετες επιχειρηματικές ροές εργασίας

## 🎯 Οφέλη Αρχιτεκτονικής Εργαλείων .NET

### Δυνατότητες Εργαλείων Επιχειρήσεων

- **Επαλήθευση κατά το Compile-Time**: Η στατική τυποποίηση διασφαλίζει τη σωστή παράμετρο εργαλείου  
- **Ένεση Εξαρτήσεων**: Ενσωμάτωση IoC container για τη διαχείριση εργαλείων  
- **Πρότυπα Async/Await**: Μη μπλοκαριστική εκτέλεση εργαλείων με σωστή διαχείριση πόρων  
- **Δομημένη Καταγραφή**: Ενσωματωμένη καταγραφή για παρακολούθηση εκτέλεσης εργαλείων

### Πρότυπα Έτοιμα για Παραγωγή

- **Διαχείριση Εξαιρέσεων**: Ολοκληρωμένη διαχείριση σφαλμάτων με τυποποιημένες εξαιρέσεις  
- **Διαχείριση Πόρων**: Σωστά πρότυπα διάθεσης και διαχείρισης μνήμης  
- **Παρακολούθηση Απόδοσης**: Ενσωματωμένα μετρικά και μετρητές απόδοσης  
- **Διαχείριση Ρυθμίσεων**: Ασφαλής ρύθμιση με επαλήθευση

## 🔧 Τεχνική Αρχιτεκτονική

### Βασικά Συστατικά Αρχιτεκτονικής Εργαλείων .NET

- **Microsoft.Extensions.AI**: Ομογενοποιημένο επίπεδο αφαίρεσης εργαλείων  
- **Microsoft.Agents.AI**: Ορχήστρα εργαλείων επιπέδου επιχειρήσεων  
- **Azure OpenAI (Responses API)**: Υψηλής απόδοσης πελάτης API με σύνδεση pool

### Υποδομή Εκτέλεσης Εργαλείων

```mermaid
graph LR
    A[Αίτημα Χρήστη] --> B[Ανάλυση Πράκτορα]
    B --> C[Επιλογή Εργαλείου]
    C --> D[Έλεγχος Τύπου]
    B --> E[Σύνδεση Παραμέτρου]
    E --> F[Εκτέλεση Εργαλείου]
    C --> F
    F --> G[Επεξεργασία Αποτελέσματος]
    D --> G
    G --> H[Απάντηση]
```

## 🛠️ Κατηγορίες & Πρότυπα Εργαλείων

### 1. **Εργαλεία Επεξεργασίας Δεδομένων**

- **Επαλήθευση Εισόδου**: Στατική τυποποίηση με σημειώσεις δεδομένων  
- **Ενέργειες Μετασχηματισμού**: Ασφαλής με τύπους μετατροπή και μορφοποίηση δεδομένων  
- **Επιχειρηματική Λογική**: Εργαλεία υπολογισμών και αναλύσεων ανά περιοχή  
- **Μορφοποίηση Εξόδου**: Δημιουργία δομημένων απαντήσεων

### 2. **Εργαλεία Ενσωμάτωσης** 

- **Συνδετήρες API**: Ενσωμάτωση RESTful υπηρεσιών με HttpClient  
- **Εργαλεία Βάσεων Δεδομένων**: Ενσωμάτωση Entity Framework για πρόσβαση σε δεδομένα  
- **Λειτουργίες Αρχείων**: Ασφαλείς εργασίες αρχείων με επαλήθευση  
- **Εξωτερικές Υπηρεσίες**: Πρότυπα ενσωμάτωσης τρίτων υπηρεσιών

### 3. **Χρηστικά Εργαλεία**

- **Επεξεργασία Κειμένου**: Βοηθητικά προγράμματα χειρισμού και μορφοποίησης συμβολοσειρών  
- **Λειτουργίες Ημερομηνίας/Ώρας**: Υπολογισμοί ημερομηνίας/ώρας με ευαισθησία στον πολιτισμό  
- **Μαθηματικά Εργαλεία**: Τυπικοί υπολογισμοί και στατιστικές πράξεις  
- **Εργαλεία Επαλήθευσης**: Επιβεβαίωση κανόνων επιχειρήσεων και επαλήθευση δεδομένων

Έτοιμοι να δημιουργήσετε πράκτορες επιχειρησιακού επιπέδου με ισχυρές, ασφαλείς στην τυποποίηση δυνατότητες εργαλείων σε .NET; Ας σχεδιάσουμε επαγγελματικές λύσεις! 🏢⚡

## 🚀 Ξεκινώντας

### Απαιτήσεις

- [.NET 10 SDK](https://dotnet.microsoft.com/download/dotnet/10.0) ή νεότερη έκδοση  
- Ένας [λογαριασμός Azure](https://azure.microsoft.com/free/) με πόρο Azure OpenAI και ανάπτυξη μοντέλου  
- Το [Azure CLI](https://learn.microsoft.com/cli/azure/install-azure-cli) — εισέλθετε με `az login`

### Απαιτούμενες Μεταβλητές Περιβάλλοντος

```bash
# zsh/bash
export AZURE_OPENAI_ENDPOINT=https://<your-resource>.openai.azure.com
export AZURE_OPENAI_DEPLOYMENT=gpt-4o-mini
# Συνδεθείτε για να μπορέσει το AzureCliCredential να πάρει ένα token
az login
```

```powershell
# PowerShell
$env:AZURE_OPENAI_ENDPOINT = "https://<your-resource>.openai.azure.com"
$env:AZURE_OPENAI_DEPLOYMENT = "gpt-4o-mini"
# Στη συνέχεια, συνδεθείτε ώστε το AzureCliCredential να μπορεί να πάρει ένα διακριτικό
az login
```

### Παραδειγματικός Κώδικας

Για να εκτελέσετε το παράδειγμα κώδικα,

```bash
# zsh/bash
chmod +x ./04-dotnet-agent-framework.cs
./04-dotnet-agent-framework.cs
```

Ή χρησιμοποιώντας το dotnet CLI:

```bash
dotnet run ./04-dotnet-agent-framework.cs
```

Δείτε το [`04-dotnet-agent-framework.cs`](../../../../04-tool-use/code_samples/04-dotnet-agent-framework.cs) για ολοκληρωμένο κώδικα.

```csharp
#!/usr/bin/dotnet run

#:package Microsoft.Extensions.AI@10.*
#:package Microsoft.Agents.AI.OpenAI@1.*-*
#:package Azure.AI.OpenAI@2.1.0
#:package Azure.Identity@1.13.1

using System.ComponentModel;

using Microsoft.Agents.AI;
using Microsoft.Extensions.AI;

using Azure.AI.OpenAI;
using Azure.Identity;

// Tool Function: Random Destination Generator
// This static method will be available to the agent as a callable tool
// The [Description] attribute helps the AI understand when to use this function
// This demonstrates how to create custom tools for AI agents
[Description("Provides a random vacation destination.")]
static string GetRandomDestination()
{
    // List of popular vacation destinations around the world
    // The agent will randomly select from these options
    var destinations = new List<string>
    {
        "Paris, France",
        "Tokyo, Japan",
        "New York City, USA",
        "Sydney, Australia",
        "Rome, Italy",
        "Barcelona, Spain",
        "Cape Town, South Africa",
        "Rio de Janeiro, Brazil",
        "Bangkok, Thailand",
        "Vancouver, Canada"
    };

    // Generate random index and return selected destination
    // Uses System.Random for simple random selection
    var random = new Random();
    int index = random.Next(destinations.Count);
    return destinations[index];
}

// Azure OpenAI with the Responses API (stable v1 endpoint). Sign in with `az login`.
var azureEndpoint = Environment.GetEnvironmentVariable("AZURE_OPENAI_ENDPOINT")
    ?? throw new InvalidOperationException("AZURE_OPENAI_ENDPOINT is not set.");
var deployment = Environment.GetEnvironmentVariable("AZURE_OPENAI_DEPLOYMENT") ?? "gpt-4o-mini";

var azureClient = new AzureOpenAIClient(new Uri(azureEndpoint), new AzureCliCredential());

// Define Agent Identity and Comprehensive Instructions
// Agent name for identification and logging purposes
var AGENT_NAME = "TravelAgent";

// Detailed instructions that define the agent's personality, capabilities, and behavior
// This system prompt shapes how the agent responds and interacts with users
var AGENT_INSTRUCTIONS = """
You are a helpful AI Agent that can help plan vacations for customers.

Important: When users specify a destination, always plan for that location. Only suggest random destinations when the user hasn't specified a preference.

When the conversation begins, introduce yourself with this message:
"Hello! I'm your TravelAgent assistant. I can help plan vacations and suggest interesting destinations for you. Here are some things you can ask me:
1. Plan a day trip to a specific location
2. Suggest a random vacation destination
3. Find destinations with specific features (beaches, mountains, historical sites, etc.)
4. Plan an alternative trip if you don't like my first suggestion

What kind of trip would you like me to help you plan today?"

Always prioritize user preferences. If they mention a specific destination like "Bali" or "Paris," focus your planning on that location rather than suggesting alternatives.
""";

// Create AI Agent with Advanced Travel Planning Capabilities
// Get the Responses client for the deployment and create the AI agent
// Configure agent with name, detailed instructions, and available tools
// This demonstrates the .NET agent creation pattern with full configuration
AIAgent agent = azureClient
    .GetOpenAIResponseClient(deployment)
    .CreateAIAgent(
        name: AGENT_NAME,
        instructions: AGENT_INSTRUCTIONS,
        tools: [AIFunctionFactory.Create(GetRandomDestination)]
    );

// Create New Conversation Thread for Context Management
// Initialize a new conversation thread to maintain context across multiple interactions
// Threads enable the agent to remember previous exchanges and maintain conversational state
// This is essential for multi-turn conversations and contextual understanding
AgentThread thread = agent.GetNewThread();

// Execute Agent: First Travel Planning Request
// Run the agent with an initial request that will likely trigger the random destination tool
// The agent will analyze the request, use the GetRandomDestination tool, and create an itinerary
// Using the thread parameter maintains conversation context for subsequent interactions
await foreach (var update in agent.RunStreamingAsync("Plan me a day trip", thread))
{
    await Task.Delay(10);
    Console.Write(update);
}

Console.WriteLine();

// Execute Agent: Follow-up Request with Context Awareness
// Demonstrate contextual conversation by referencing the previous response
// The agent remembers the previous destination suggestion and will provide an alternative
// This showcases the power of conversation threads and contextual understanding in .NET agents
await foreach (var update in agent.RunStreamingAsync("I don't like that destination. Plan me another vacation.", thread))
{
    await Task.Delay(10);
    Console.Write(update);
}
```

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Αποποίηση ευθυνών**:
Αυτό το έγγραφο έχει μεταφραστεί χρησιμοποιώντας την υπηρεσία μετάφρασης με τεχνητή νοημοσύνη [Co-op Translator](https://github.com/Azure/co-op-translator). Ενώ επιδιώκουμε την ακρίβεια, παρακαλούμε να έχετε υπόψη ότι οι αυτοματοποιημένες μεταφράσεις ενδέχεται να περιέχουν λάθη ή ανακρίβειες. Το πρωτότυπο έγγραφο στη μητρική του γλώσσα πρέπει να θεωρείται η αυθεντική πηγή. Για κρίσιμες πληροφορίες, συνιστάται επαγγελματική ανθρώπινη μετάφραση. Δεν φέρουμε ευθύνη για τυχόν παρεξηγήσεις ή λανθασμένες ερμηνείες που προκύπτουν από τη χρήση αυτής της μετάφρασης.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->