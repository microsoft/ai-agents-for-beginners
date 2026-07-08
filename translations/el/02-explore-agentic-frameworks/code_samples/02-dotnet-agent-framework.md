# 🔍 Εξερευνώντας το Microsoft Agent Framework - Βασικός Αντιπρόσωπος (.NET)

## 📋 Μαθησιακοί Στόχοι

Αυτό το παράδειγμα εξερευνά τις βασικές έννοιες του Microsoft Agent Framework μέσω μιας υλοποίησης βασικού αντιπροσώπου σε .NET. Θα μάθετε βασικά προτύπα πράκτορα και θα κατανοήσετε τον τρόπο λειτουργίας των ευφυών πρακτόρων κάτω από την επιφάνεια, χρησιμοποιώντας C# και το οικοσύστημα .NET.

### Τι θα Ανακαλύψετε

- 🏗️ **Αρχιτεκτονική Πράκτορα**: Κατανόηση της βασικής δομής των πρακτόρων AI σε .NET
- 🛠️ **Ενσωμάτωση Εργαλείων**: Πώς οι πράκτορες χρησιμοποιούν εξωτερικές λειτουργίες για επέκταση δυνατοτήτων  
- 💬 **Ροή Συζητήσεων**: Διαχείριση συνομιλιών πολλαπλών γύρων και συμφραζομένων με διαχείριση νημάτων
- 🔧 **Πρότυπα Διαμόρφωσης**: Καλές πρακτικές για ρύθμιση και διαχείριση πράκτορα σε .NET

## 🎯 Κύριες Εννοιες που Καλύπτονται

### Αρχές Πλαισίου Πρακτόρων

- **Αυτονομία**: Πώς οι πράκτορες λαμβάνουν ανεξάρτητες αποφάσεις χρησιμοποιώντας τις αφαιρέσεις AI του .NET
- **Αντιδραστικότητα**: Ανταπόκριση σε περιβαλλοντικές αλλαγές και εισόδους χρήστη
- **Προδραστικότητα**: Ανάληψη πρωτοβουλίας βασισμένη σε στόχους και συμφραζόμενα
- **Κοινωνική Ικανότητα**: Αλληλεπίδραση μέσω φυσικής γλώσσας με νήματα συνομιλίας

### Τεχνικά Συστατικά

- **AIAgent**: Κεντρικός συντονισμός πράκτορα και διαχείριση συνομιλίας (.NET)
- **Λειτουργίες Εργαλείων**: Επέκταση δυνατοτήτων πράκτορα με μεθόδους και χαρακτηριστικά C#
- **Ενσωμάτωση Azure OpenAI**: Αξιοποίηση μοντέλων γλώσσας μέσω του Azure OpenAI Responses API
- **Ασφαλής Διαμόρφωση**: Διαχείριση τερματικών σημείων βασισμένη σε περιβάλλον

## 🔧 Τεχνικό Υπόβαθρο

### Βασικές Τεχνολογίες

- Microsoft Agent Framework (.NET)
- Ενσωμάτωση Azure OpenAI (Responses API)
- Πρότυπα πελάτη Azure.AI.OpenAI
- Διαμόρφωση βάσει περιβάλλοντος με DotNetEnv

### Δυνατότητες Πράκτορα

- Κατανόηση και δημιουργία φυσικής γλώσσας
- Κλήση λειτουργιών και χρήση εργαλείων με χαρακτηριστικά C#
- Απαντήσεις με επίγνωση συμφραζομένων μέσω νημάτων συνομιλίας
- Επεκτάσιμη αρχιτεκτονική με πρότυπα εξάρτησης

## 📚 Σύγκριση Πλαισίων

Αυτό το παράδειγμα δείχνει την προσέγγιση του Microsoft Agent Framework σε σύγκριση με άλλα πλαίσια πρακτόρων:

| Χαρακτηριστικό | Microsoft Agent Framework | Άλλα Πλαίσια |
|---------|-------------------------|------------------|
| **Ενσωμάτωση** | Φυσικό οικοσύστημα Microsoft | Μεταβλητή συμβατότητα |
| **Απλότητα** | Καθαρό, διαισθητικό API | Συχνά σύνθετη εγκατάσταση |
| **Επεκτασιμότητα** | Εύκολη ενσωμάτωση εργαλείων | Εξαρτώμενη από το πλαίσιο |
| **Έτοιμο για Επιχειρήσεις** | Κατασκευασμένο για παραγωγή | Διαφοροποιείται ανάλογα με το πλαίσιο |

## 🚀 Ξεκινώντας

### Προαπαιτούμενα

- [.NET 10 SDK](https://dotnet.microsoft.com/download/dotnet/10.0) ή νεότερο
- Μια [συνδρομή Azure](https://azure.microsoft.com/free/) με πόρο Azure OpenAI και ανάπτυξη μοντέλου
- Το [Azure CLI](https://learn.microsoft.com/cli/azure/install-azure-cli) — είσοδος με `az login`

### Απαιτούμενες Μεταβλητές Περιβάλλοντος

```bash
# zsh/bash
export AZURE_OPENAI_ENDPOINT=https://<your-resource>.openai.azure.com
export AZURE_OPENAI_DEPLOYMENT=gpt-4o-mini
# Συνδεθείτε ώστε το AzureCliCredential να μπορεί να λάβει ένα token
az login
```

```powershell
# PowerShell
$env:AZURE_OPENAI_ENDPOINT = "https://<your-resource>.openai.azure.com"
$env:AZURE_OPENAI_DEPLOYMENT = "gpt-4o-mini"
# Στη συνέχεια συνδεθείτε ώστε το AzureCliCredential να μπορεί να λάβει ένα διακριτικό
az login
```

### Δείγμα Κώδικα

Για να εκτελέσετε το παράδειγμα κώδικα,

```bash
# zsh/bash
chmod +x ./02-dotnet-agent-framework.cs
./02-dotnet-agent-framework.cs
```

Ή χρησιμοποιώντας το dotnet CLI:

```bash
dotnet run ./02-dotnet-agent-framework.cs
```

Δείτε το [`02-dotnet-agent-framework.cs`](../../../../02-explore-agentic-frameworks/code_samples/02-dotnet-agent-framework.cs) για τον πλήρη κώδικα.

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

## 🎓 Βασικά Συμπεράσματα

1. **Αρχιτεκτονική Πράκτορα**: Το Microsoft Agent Framework προσφέρει μια καθαρή, τύπου ασφαλή προσέγγιση στην κατασκευή πρακτόρων AI σε .NET
2. **Ενσωμάτωση Εργαλείων**: Οι λειτουργίες που διακοσμούνται με χαρακτηριστικά `[Description]` γίνονται διαθέσιμα εργαλεία για τον πράκτορα
3. **Συμφραζόμενα Συνομιλίας**: Η διαχείριση νημάτων επιτρέπει συνομιλίες πολλαπλών γύρων με πλήρη επίγνωση συμφραζομένων
4. **Διαχείριση Διαμόρφωσης**: Οι μεταβλητές περιβάλλοντος και η ασφαλής διαχείριση διαπιστευτηρίων ακολουθούν τις βέλτιστες πρακτικές του .NET
5. **Azure OpenAI Responses API**: Ο πράκτορας χρησιμοποιεί το Azure OpenAI Responses API μέσω του Azure.AI.OpenAI SDK

## 🔗 Πρόσθετοι Πόροι

- [Έγγραφα Microsoft Agent Framework](https://learn.microsoft.com/agent-framework)
- [Azure OpenAI στο Microsoft Foundry](https://learn.microsoft.com/azure/ai-services/openai/)
- [Microsoft.Extensions.AI](https://learn.microsoft.com/dotnet/ai/microsoft-extensions-ai)
- [.NET Single File Apps](https://devblogs.microsoft.com/dotnet/announcing-dotnet-run-app)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Αποποίηση ευθυνών**:
Αυτό το έγγραφο έχει μεταφραστεί χρησιμοποιώντας την υπηρεσία μετάφρασης με τεχνητή νοημοσύνη [Co-op Translator](https://github.com/Azure/co-op-translator). Ενώ επιδιώκουμε την ακρίβεια, παρακαλούμε να έχετε υπόψη ότι οι αυτοματοποιημένες μεταφράσεις ενδέχεται να περιέχουν λάθη ή ανακρίβειες. Το πρωτότυπο έγγραφο στη μητρική του γλώσσα πρέπει να θεωρείται η αυθεντική πηγή. Για κρίσιμες πληροφορίες, συνιστάται επαγγελματική ανθρώπινη μετάφραση. Δεν φέρουμε ευθύνη για τυχόν παρεξηγήσεις ή λανθασμένες ερμηνείες που προκύπτουν από τη χρήση αυτής της μετάφρασης.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->