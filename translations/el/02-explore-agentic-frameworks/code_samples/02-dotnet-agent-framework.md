<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "033f170be3b54183e2f6b5463371ab69",
  "translation_date": "2025-11-07T09:35:46+00:00",
  "source_file": "02-explore-agentic-frameworks/code_samples/02-dotnet-agent-framework.md",
  "language_code": "el"
}
-->
# 🔍 Εξερεύνηση Πλαισίων Πρακτόρων - Βασικός Πράκτορας (.NET)

## 📋 Στόχοι Μάθησης

Αυτό το σημειωματάριο εξερευνά τις θεμελιώδεις έννοιες του Microsoft Agent Framework μέσω μιας βασικής υλοποίησης πράκτορα στο .NET. Θα μάθετε βασικά μοτίβα πρακτόρων και θα κατανοήσετε πώς λειτουργούν οι έξυπνοι πράκτορες στο παρασκήνιο χρησιμοποιώντας C# και το οικοσύστημα .NET.

**Τι θα Ανακαλύψετε:**
- 🏗️ **Αρχιτεκτονική Πράκτορα**: Κατανόηση της βασικής δομής των AI πρακτόρων στο .NET
- 🛠️ **Ενσωμάτωση Εργαλείων**: Πώς οι πράκτορες χρησιμοποιούν εξωτερικές λειτουργίες για να επεκτείνουν τις δυνατότητες  
- 💬 **Ροή Συνομιλίας**: Διαχείριση συνομιλιών πολλαπλών γύρων και πλαισίου με διαχείριση νημάτων
- 🔧 **Μοτίβα Ρύθμισης**: Βέλτιστες πρακτικές για τη ρύθμιση και διαχείριση πρακτόρων στο .NET

## 🎯 Βασικές Έννοιες

### Αρχές Πλαισίου Πρακτόρων
- **Αυτονομία**: Πώς οι πράκτορες λαμβάνουν ανεξάρτητες αποφάσεις χρησιμοποιώντας αφαιρέσεις AI του .NET
- **Αντιδραστικότητα**: Ανταπόκριση σε αλλαγές περιβάλλοντος και εισόδους χρηστών
- **Προδραστικότητα**: Ανάληψη πρωτοβουλιών βάσει στόχων και πλαισίου
- **Κοινωνική Ικανότητα**: Αλληλεπίδραση μέσω φυσικής γλώσσας με νήματα συνομιλίας

### Τεχνικά Στοιχεία
- **AIAgent**: Κεντρική ορχήστρα πράκτορα και διαχείριση συνομιλιών (.NET)
- **Λειτουργίες Εργαλείων**: Επέκταση δυνατοτήτων πράκτορα με μεθόδους και χαρακτηριστικά C#
- **Ενσωμάτωση OpenAI**: Αξιοποίηση μοντέλων γλώσσας μέσω τυποποιημένων APIs του .NET
- **Διαχείριση Περιβάλλοντος**: Ασφαλής ρύθμιση και χειρισμός διαπιστευτηρίων με DotNetEnv

## ⚙️ Προαπαιτούμενα & Ρύθμιση

**Απαιτούμενες Εξαρτήσεις:**
- .NET 9.0 SDK ή νεότερο
- Visual Studio 2022 ή VS Code με επέκταση C#

**Πακέτα NuGet:**
- `Microsoft.Extensions.AI` - Βασικές αφαιρέσεις AI
- `Microsoft.Extensions.AI.OpenAI` - Ενσωμάτωση OpenAI (προεπισκόπηση)
- `DotNetEnv` - Διαχείριση μεταβλητών περιβάλλοντος

**Ρύθμιση Περιβάλλοντος (.env αρχείο):**
```env
GITHUB_TOKEN=your_github_personal_access_token
GITHUB_ENDPOINT=https://models.inference.ai.azure.com
GITHUB_MODEL_ID=gpt-4o-mini
```

## 🔧 Τεχνική Στοίβα

**Βασικές Τεχνολογίες:**
- Microsoft Agent Framework (.NET)
- Ενσωμάτωση API Μοντέλων GitHub
- Πρότυπα πελάτη συμβατά με OpenAI
- Ρύθμιση βάσει περιβάλλοντος με DotNetEnv

**Δυνατότητες Πράκτορα:**
- Κατανόηση και παραγωγή φυσικής γλώσσας
- Κλήση λειτουργιών και χρήση εργαλείων με χαρακτηριστικά C#
- Απαντήσεις με επίγνωση πλαισίου μέσω νημάτων συνομιλίας
- Επεκτάσιμη αρχιτεκτονική με μοτίβα έγχυσης εξαρτήσεων

## 📚 Σύγκριση Πλαισίων

Αυτό το παράδειγμα δείχνει την προσέγγιση του Microsoft Agent Framework στο .NET σε σύγκριση με άλλες πλατφόρμες:

| Χαρακτηριστικό | Πλαίσιο Πράκτορα .NET | Ισοδύναμα Python |
|----------------|-----------------------|------------------|
| **Ασφάλεια Τύπου** | Ισχυρή τυποποίηση με C# | Δυναμική τυποποίηση |
| **Ενσωμάτωση** | Εγγενές οικοσύστημα .NET | Ποικίλη συμβατότητα |
| **Απόδοση** | Απόδοση μεταγλωττισμένου κώδικα | Ερμηνευμένη εκτέλεση |
| **Έτοιμο για Επιχειρήσεις** | Σχεδιασμένο για παραγωγικές εφαρμογές .NET | Διαφέρει ανά πλαίσιο |
| **Εργαλεία** | Ενσωμάτωση Visual Studio | Εξαρτάται από το IDE |

## 🚀 Ξεκινώντας

Ακολουθήστε τα παρακάτω βήματα για να δημιουργήσετε τον πρώτο σας βασικό πράκτορα στο .NET και να κατανοήσετε θεμελιώδεις έννοιες πρακτόρων!

## 📦 Εγκατάσταση και Ρύθμιση

Αυτό το παράδειγμα είναι διαθέσιμο ως εκτελέσιμη εφαρμογή .NET Single File App. Δείτε το συνοδευτικό αρχείο `02-dotnet-agent-framework.cs` για την πλήρη υλοποίηση.

Για να εκτελέσετε αυτό το παράδειγμα:

```bash
chmod +x 02-dotnet-agent-framework.cs
./02-dotnet-agent-framework.cs
```

Ή χρησιμοποιώντας το dotnet CLI:

```bash
dotnet run 02-dotnet-agent-framework.cs
```

## 💡 Ανάλυση Κώδικα

Η πλήρης υλοποίηση περιλαμβάνει:

### 1. Εξαρτήσεις Πακέτων

```csharp
// Core AI abstraction layer for .NET applications
#r "nuget: Microsoft.Extensions.AI, 9.9.1"

// Microsoft Agent Framework OpenAI integration
#r "nuget: Microsoft.Agents.AI.OpenAI, 1.0.0-preview.251001.3"

// Core Microsoft Agent Framework library
#r "nuget: Microsoft.Agents.AI, 1.0.0-preview.251001.3"

// Environment variable management
#r "nuget: DotNetEnv, 3.1.1"
```

### 2. Βασικές Εισαγωγές

```csharp
using System;
using System.ComponentModel;
using System.ClientModel;
using Microsoft.Extensions.AI;
using Microsoft.Agents.AI;
using OpenAI;
using DotNetEnv;
```

### 3. Ρύθμιση Περιβάλλοντος

```csharp
// Load configuration from .env file
Env.Load("../../../.env");
```

### 4. Ορισμός Λειτουργιών Εργαλείων

```csharp
// Random destination generator tool
[Description("Provides a random vacation destination.")]
static string GetRandomDestination()
{
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
    
    var random = new Random();
    int index = random.Next(destinations.Count);
    return destinations[index];
}
```

### 5. Ρύθμιση και Πελάτης

```csharp
// Extract environment variables
var github_endpoint = Environment.GetEnvironmentVariable("GITHUB_ENDPOINT") ?? 
    throw new InvalidOperationException("GITHUB_ENDPOINT is not set.");
var github_model_id = Environment.GetEnvironmentVariable("GITHUB_MODEL_ID") ?? "gpt-4o-mini";
var github_token = Environment.GetEnvironmentVariable("GITHUB_TOKEN") ?? 
    throw new InvalidOperationException("GITHUB_TOKEN is not set.");

// Configure OpenAI client for GitHub Models
var openAIOptions = new OpenAIClientOptions()
{
    Endpoint = new Uri(github_endpoint)
};

// Initialize OpenAI client
var openAIClient = new OpenAIClient(new ApiKeyCredential(github_token), openAIOptions);
```

### 6. Ρύθμιση Πράκτορα

```csharp
const string AGENT_NAME = "TravelAgent";

const string AGENT_INSTRUCTIONS = @"You are a helpful AI Agent that can help plan vacations for customers.

Important: When users specify a destination, always plan for that location. Only suggest random destinations when the user hasn't specified a preference.

When the conversation begins, introduce yourself with this message:
""Hello! I'm your TravelAgent assistant. I can help plan vacations and suggest interesting destinations for you. Here are some things you can ask me:
1. Plan a day trip to a specific location
2. Suggest a random vacation destination
3. Find destinations with specific features (beaches, mountains, historical sites, etc.)
4. Plan an alternative trip if you don't like my first suggestion

What kind of trip would you like me to help you plan today?""

Always prioritize user preferences. If they mention a specific destination like ""Bali"" or ""Paris,"" focus your planning on that location rather than suggesting alternatives.
";
```

### 7. Αρχικοποίηση Πράκτορα

```csharp
// Create AI agent with travel planning capabilities
AIAgent agent = new OpenAIClient(new ApiKeyCredential(github_token), openAIOptions)
    .GetChatClient(github_model_id)
    .CreateAIAgent(
        name: AGENT_NAME,
        instructions: AGENT_INSTRUCTIONS,
        tools: [AIFunctionFactory.Create((Func<string>)GetRandomDestination)]
    );
```

### 8. Διαχείριση Συνομιλιών

```csharp
// Create new conversation thread
AgentThread thread = agent.GetNewThread();

// Execute agent: First travel planning request
Console.WriteLine(await agent.RunAsync("Plan me a day trip", thread));

// Execute agent: Follow-up request with context awareness
Console.WriteLine(await agent.RunAsync("I don't like that destination. Plan me another vacation.", thread));
```

## 🎓 Βασικά Συμπεράσματα

1. **Αρχιτεκτονική Πράκτορα**: Το Microsoft Agent Framework παρέχει μια καθαρή, ασφαλή προσέγγιση για τη δημιουργία AI πρακτόρων στο .NET
2. **Ενσωμάτωση Εργαλείων**: Λειτουργίες με χαρακτηριστικά `[Description]` γίνονται διαθέσιμα εργαλεία για τον πράκτορα
3. **Πλαίσιο Συνομιλίας**: Η διαχείριση νημάτων επιτρέπει συνομιλίες πολλαπλών γύρων με πλήρη επίγνωση πλαισίου
4. **Διαχείριση Ρύθμισης**: Οι μεταβλητές περιβάλλοντος και η ασφαλής διαχείριση διαπιστευτηρίων ακολουθούν βέλτιστες πρακτικές του .NET
5. **Συμβατότητα OpenAI**: Η ενσωμάτωση Μοντέλων GitHub λειτουργεί απρόσκοπτα μέσω συμβατών APIs του OpenAI

## 🔗 Πρόσθετοι Πόροι

- [Τεκμηρίωση Microsoft Agent Framework](https://learn.microsoft.com/en-us/dotnet/ai/agents)
- [Αγορά Μοντέλων GitHub](https://github.com/marketplace/models)
- [Microsoft.Extensions.AI](https://learn.microsoft.com/en-us/dotnet/ai/microsoft-extensions-ai-overview)
- [.NET Single File Apps](https://devblogs.microsoft.com/dotnet/announcing-dotnet-run-app/)

---

**Αποποίηση ευθύνης**:  
Αυτό το έγγραφο έχει μεταφραστεί χρησιμοποιώντας την υπηρεσία αυτόματης μετάφρασης [Co-op Translator](https://github.com/Azure/co-op-translator). Παρόλο που καταβάλλουμε προσπάθειες για ακρίβεια, παρακαλούμε να έχετε υπόψη ότι οι αυτόματες μεταφράσεις ενδέχεται να περιέχουν λάθη ή ανακρίβειες. Το πρωτότυπο έγγραφο στη μητρική του γλώσσα θα πρέπει να θεωρείται η αυθεντική πηγή. Για κρίσιμες πληροφορίες, συνιστάται επαγγελματική ανθρώπινη μετάφραση. Δεν φέρουμε ευθύνη για τυχόν παρεξηγήσεις ή εσφαλμένες ερμηνείες που προκύπτουν από τη χρήση αυτής της μετάφρασης.