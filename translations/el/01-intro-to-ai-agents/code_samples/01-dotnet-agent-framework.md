# 🌍 Πράκτορας Ταξιδιών AI με το Microsoft Agent Framework (.NET)

## 📋 Επισκόπηση Σεναρίου

Αυτό το παράδειγμα δείχνει πώς να δημιουργήσετε έναν έξυπνο πράκτορα σχεδιασμού ταξιδιών χρησιμοποιώντας το Microsoft Agent Framework για .NET. Ο πράκτορας μπορεί να δημιουργεί αυτόματα εξατομικευμένα ημερήσια δρομολόγια για τυχαίους προορισμούς ανά τον κόσμο.

### Κύριες Δυνατότητες:

- 🎲 **Τυχαία Επιλογή Προορισμού**: Χρησιμοποιεί ένα προσαρμοσμένο εργαλείο για την επιλογή διακοπών
- 🗺️ **Έξυπνος Σχεδιασμός Ταξιδιού**: Δημιουργεί λεπτομερή ημερήσια δρομολόγια
- 🔄 **Ροή σε Πραγματικό Χρόνο**: Υποστηρίζει άμεσες και ροές απαντήσεων
- 🛠️ **Ενσωμάτωση Προσαρμοσμένων Εργαλείων**: Δείχνει πώς να επεκτείνετε τις δυνατότητες του πράκτορα

## 🔧 Τεχνική Αρχιτεκτονική

### Βασικές Τεχνολογίες

- **Microsoft Agent Framework**: Τελευταία υλοποίηση .NET για ανάπτυξη πρακτόρων AI
- **Azure OpenAI (Responses API)**: Χρησιμοποιεί το Azure OpenAI Responses API για εκτέλεση μοντέλου
- **Azure Identity**: Ασφαλής σύνδεση μέσω `AzureCliCredential` (`az login`)
- **Ασφαλής Διαχείριση Ρυθμίσεων**: Διαχείριση σημείου πρόσβασης μέσω μεταβλητών περιβάλλοντος

### Κύρια Συστατικά

1. **AIAgent**: Ο κύριος συντονιστής πράκτορας που διαχειρίζεται τη ροή της συνομιλίας
2. **Προσαρμοσμένα Εργαλεία**: Συνάρτηση `GetRandomDestination()` διαθέσιμη στον πράκτορα
3. **Πελάτης Απαντήσεων**: Διεπαφή συνομιλίας βασισμένη στο Azure OpenAI Responses
4. **Υποστήριξη Ροής**: Δυνατότητες παραγωγής απαντήσεων σε πραγματικό χρόνο

### Πρότυπο Ενσωμάτωσης

```mermaid
graph LR
    A[Αίτηση Χρήστη] --> B[Πράκτορας ΤΝ]
    B --> C[Azure OpenAI (API Απαντήσεων)]
    B --> D[Εργαλείο Τυχαίου Προορισμού]
    C --> E[Ταξιδιωτικό Πρόγραμμα]
    D --> E
```

## 🚀 Ξεκινώντας

### Προαπαιτούμενα

- [.NET 10 SDK](https://dotnet.microsoft.com/download/dotnet/10.0) ή νεότερο
- Ένας [λογαριασμός Azure](https://azure.microsoft.com/free/) με πόρο Azure OpenAI και ανάπτυξη μοντέλου
- Το [Azure CLI](https://learn.microsoft.com/cli/azure/install-azure-cli) — σύνδεση με `az login`

### Απαιτούμενες Μεταβλητές Περιβάλλοντος

```bash
# zsh/bash
export AZURE_OPENAI_ENDPOINT=https://<your-resource>.openai.azure.com
export AZURE_OPENAI_DEPLOYMENT=gpt-4o-mini
# Στη συνέχεια, συνδεθείτε ώστε το AzureCliCredential να μπορεί να πάρει ένα διακριτικό
az login
```

```powershell
# PowerShell
$env:AZURE_OPENAI_ENDPOINT = "https://<your-resource>.openai.azure.com"
$env:AZURE_OPENAI_DEPLOYMENT = "gpt-4o-mini"
# Συνδεθείτε ώστε το AzureCliCredential να μπορεί να λάβει ένα διακριτικό
az login
```

### Παράδειγμα Κώδικα

Για να εκτελέσετε το παράδειγμα κώδικα,

```bash
# zsh/bash
chmod +x ./01-dotnet-agent-framework.cs
./01-dotnet-agent-framework.cs
```

Ή με χρήση του dotnet CLI:

```bash
dotnet run ./01-dotnet-agent-framework.cs
```

Δείτε το [`01-dotnet-agent-framework.cs`](../../../../01-intro-to-ai-agents/code_samples/01-dotnet-agent-framework.cs) για πλήρη κώδικα.

```csharp
#!/usr/bin/dotnet run

#:package Microsoft.Extensions.AI@9.*
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

// Create AI Agent with Travel Planning Capabilities
// Get the Responses client for the specified deployment and create the AI agent
// Configure agent with travel planning instructions and random destination tool
// The agent can now plan trips using the GetRandomDestination function
AIAgent agent = azureClient
    .GetOpenAIResponseClient(deployment)
    .CreateAIAgent(
        instructions: "You are a helpful AI Agent that can help plan vacations for customers at random destinations",
        tools: [AIFunctionFactory.Create(GetRandomDestination)]
    );

// Execute Agent: Plan a Day Trip
// Run the agent with streaming enabled for real-time response display
// Shows the agent's thinking and response as it generates the content
// Provides better user experience with immediate feedback
await foreach (var update in agent.RunStreamingAsync("Plan me a day trip"))
{
    await Task.Delay(10);
    Console.Write(update);
}
```

## 🎓 Βασικά Συμπεράσματα

1. **Αρχιτεκτονική Πράκτορα**: Το Microsoft Agent Framework παρέχει μια καθαρή και τύπου ασφαλή προσέγγιση για την κατασκευή AI πρακτόρων σε .NET
2. **Ενσωμάτωση Εργαλείων**: Οι συναρτήσεις με χαρακτηριστικά `[Description]` γίνονται διαθέσιμα εργαλεία για τον πράκτορα
3. **Διαχείριση Ρυθμίσεων**: Οι μεταβλητές περιβάλλοντος και η ασφαλής διαχείριση διαπιστευτηρίων ακολουθούν τις βέλτιστες πρακτικές του .NET
4. **Azure OpenAI Responses API**: Ο πράκτορας χρησιμοποιεί το Azure OpenAI Responses API μέσω του Azure.AI.OpenAI SDK

## 🔗 Πρόσθετοι Πόροι

- [Microsoft Agent Framework Documentation](https://learn.microsoft.com/agent-framework)
- [Azure OpenAI στο Microsoft Foundry](https://learn.microsoft.com/azure/ai-services/openai/)
- [Microsoft.Extensions.AI](https://learn.microsoft.com/dotnet/ai/microsoft-extensions-ai)
- [.NET Εφαρμογές Αρχείων Μονής Ενότητας](https://devblogs.microsoft.com/dotnet/announcing-dotnet-run-app)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Αποποίηση ευθυνών**:
Αυτό το έγγραφο έχει μεταφραστεί χρησιμοποιώντας την υπηρεσία μετάφρασης με τεχνητή νοημοσύνη [Co-op Translator](https://github.com/Azure/co-op-translator). Ενώ επιδιώκουμε την ακρίβεια, παρακαλούμε να έχετε υπόψη ότι οι αυτοματοποιημένες μεταφράσεις ενδέχεται να περιέχουν λάθη ή ανακρίβειες. Το πρωτότυπο έγγραφο στη μητρική του γλώσσα πρέπει να θεωρείται η αυθεντική πηγή. Για κρίσιμες πληροφορίες, συνιστάται επαγγελματική ανθρώπινη μετάφραση. Δεν φέρουμε ευθύνη για τυχόν παρεξηγήσεις ή λανθασμένες ερμηνείες που προκύπτουν από τη χρήση αυτής της μετάφρασης.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->