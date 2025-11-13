<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "e23058f87779da210fc0257ee2747c53",
  "translation_date": "2025-11-13T10:57:04+00:00",
  "source_file": "02-explore-agentic-frameworks/code_samples/02-dotnet-agent-framework.md",
  "language_code": "de"
}
-->
# 🔍 Erkundung des Microsoft Agent Frameworks - Basisagent (.NET)

## 📋 Lernziele

Dieses Beispiel untersucht die grundlegenden Konzepte des Microsoft Agent Frameworks anhand einer Basisagenten-Implementierung in .NET. Sie lernen die zentralen agentischen Muster kennen und verstehen, wie intelligente Agenten mit C# und dem .NET-Ökosystem im Hintergrund arbeiten.

### Was Sie entdecken werden

- 🏗️ **Agentenarchitektur**: Verständnis der grundlegenden Struktur von KI-Agenten in .NET  
- 🛠️ **Tool-Integration**: Wie Agenten externe Funktionen nutzen, um ihre Fähigkeiten zu erweitern  
- 💬 **Konversationsfluss**: Verwaltung von mehrstufigen Gesprächen und Kontext mit Thread-Management  
- 🔧 **Konfigurationsmuster**: Best Practices für die Einrichtung und Verwaltung von Agenten in .NET  

## 🎯 Wichtige behandelte Konzepte

### Prinzipien des Agentenframeworks

- **Autonomie**: Wie Agenten unabhängige Entscheidungen mithilfe von .NET-KI-Abstraktionen treffen  
- **Reaktivität**: Reaktion auf Umweltveränderungen und Benutzereingaben  
- **Proaktivität**: Eigeninitiative basierend auf Zielen und Kontext  
- **Soziale Fähigkeit**: Interaktion durch natürliche Sprache mit Konversationsthreads  

### Technische Komponenten

- **AIAgent**: Kernorchestrierung des Agenten und Konversationsmanagement (.NET)  
- **Tool-Funktionen**: Erweiterung der Agentenfähigkeiten mit C#-Methoden und Attributen  
- **OpenAI-Integration**: Nutzung von Sprachmodellen über standardisierte .NET-APIs  
- **Sichere Konfiguration**: API-Schlüsselverwaltung basierend auf Umgebungsvariablen  

## 🔧 Technologiestack

### Kerntechnologien

- Microsoft Agent Framework (.NET)  
- GitHub Models API-Integration  
- OpenAI-kompatible Clientmuster  
- Umgebungsbasierte Konfiguration mit DotNetEnv  

### Fähigkeiten des Agenten

- Verstehen und Generieren natürlicher Sprache  
- Funktionsaufrufe und Tool-Nutzung mit C#-Attributen  
- Kontextbewusste Antworten mit Konversationsthreads  
- Erweiterbare Architektur mit Dependency Injection-Mustern  

## 📚 Vergleich der Frameworks

Dieses Beispiel zeigt den Ansatz des Microsoft Agent Frameworks im Vergleich zu anderen agentischen Frameworks:

| Funktion         | Microsoft Agent Framework | Andere Frameworks       |
|------------------|---------------------------|-------------------------|
| **Integration**  | Native Microsoft-Umgebung | Unterschiedliche Kompatibilität |
| **Einfachheit**  | Saubere, intuitive API    | Oft komplexe Einrichtung |
| **Erweiterbarkeit** | Einfache Tool-Integration | Framework-abhängig       |
| **Unternehmensreife** | Für den produktiven Einsatz entwickelt | Variiert je nach Framework |

## 🚀 Erste Schritte

### Voraussetzungen

- [.NET 10 SDK](https://dotnet.microsoft.com/download/dotnet/10.0) oder höher  
- [GitHub Models API-Zugriffstoken](https://docs.github.com/github-models/github-models-at-scale/using-your-own-api-keys-in-github-models)  

### Erforderliche Umgebungsvariablen

```bash
# zsh/bash
export GH_TOKEN=<your_github_token>
export GH_ENDPOINT=https://models.github.ai/inference
export GH_MODEL_ID=openai/gpt-5-mini
```
  
```powershell
# PowerShell
$env:GH_TOKEN = "<your_github_token>"
$env:GH_ENDPOINT = "https://models.github.ai/inference"
$env:GH_MODEL_ID = "openai/gpt-5-mini"
```
  

### Beispielcode

Um das Codebeispiel auszuführen:

```bash
# zsh/bash
chmod +x ./02-dotnet-agent-framework.cs
./02-dotnet-agent-framework.cs
```
  
Oder mit dem dotnet CLI:

```bash
dotnet run ./02-dotnet-agent-framework.cs
```
  
Siehe [`02-dotnet-agent-framework.cs`](../../../../02-explore-agentic-frameworks/code_samples/02-dotnet-agent-framework.cs) für den vollständigen Code.

```csharp
#!/usr/bin/dotnet run

#:package Microsoft.Extensions.AI@10.*
#:package Microsoft.Agents.AI.OpenAI@1.*-*

using System.ClientModel;
using System.ComponentModel;

using Microsoft.Agents.AI;
using Microsoft.Extensions.AI;

using OpenAI;

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

// Extract configuration from environment variables
// Retrieve the GitHub Models API endpoint, defaults to https://models.github.ai/inference if not specified
// Retrieve the model ID, defaults to openai/gpt-5-mini if not specified
// Retrieve the GitHub token for authentication, throws exception if not specified
var github_endpoint = Environment.GetEnvironmentVariable("GH_ENDPOINT") ?? "https://models.github.ai/inference";
var github_model_id = Environment.GetEnvironmentVariable("GH_MODEL_ID") ?? "openai/gpt-5-mini";
var github_token = Environment.GetEnvironmentVariable("GH_TOKEN") ?? throw new InvalidOperationException("GH_TOKEN is not set.");

// Configure OpenAI Client Options
// Create configuration options to point to GitHub Models endpoint
// This redirects OpenAI client calls to GitHub's model inference service
var openAIOptions = new OpenAIClientOptions()
{
    Endpoint = new Uri(github_endpoint)
};

// Initialize OpenAI Client with GitHub Models Configuration
// Create OpenAI client using GitHub token for authentication
// Configure it to use GitHub Models endpoint instead of OpenAI directly
var openAIClient = new OpenAIClient(new ApiKeyCredential(github_token), openAIOptions);

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
// Initialize complete agent pipeline: OpenAI client → Chat client → AI agent
// Configure agent with name, detailed instructions, and available tools
// This demonstrates the .NET agent creation pattern with full configuration
AIAgent agent = openAIClient
    .GetChatClient(github_model_id)
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
  

## 🎓 Wichtige Erkenntnisse

1. **Agentenarchitektur**: Das Microsoft Agent Framework bietet einen sauberen, typsicheren Ansatz zum Erstellen von KI-Agenten in .NET  
2. **Tool-Integration**: Funktionen, die mit `[Description]`-Attributen versehen sind, werden zu verfügbaren Tools für den Agenten  
3. **Konversationskontext**: Thread-Management ermöglicht mehrstufige Gespräche mit vollständigem Kontextbewusstsein  
4. **Konfigurationsmanagement**: Umgebungsvariablen und sichere Anmeldeinformationen folgen den Best Practices von .NET  
5. **OpenAI-Kompatibilität**: Die GitHub Models-Integration funktioniert nahtlos über OpenAI-kompatible APIs  

## 🔗 Zusätzliche Ressourcen

- [Microsoft Agent Framework Dokumentation](https://learn.microsoft.com/agent-framework)  
- [GitHub Models Marketplace](https://github.com/marketplace?type=models)  
- [Microsoft.Extensions.AI](https://learn.microsoft.com/dotnet/ai/microsoft-extensions-ai)  
- [.NET Single File Apps](https://devblogs.microsoft.com/dotnet/announcing-dotnet-run-app)  

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Haftungsausschluss**:  
Dieses Dokument wurde mit dem KI-Übersetzungsdienst [Co-op Translator](https://github.com/Azure/co-op-translator) übersetzt. Obwohl wir uns um Genauigkeit bemühen, beachten Sie bitte, dass automatisierte Übersetzungen Fehler oder Ungenauigkeiten enthalten können. Das Originaldokument in seiner ursprünglichen Sprache sollte als maßgebliche Quelle betrachtet werden. Für kritische Informationen wird eine professionelle menschliche Übersetzung empfohlen. Wir übernehmen keine Haftung für Missverständnisse oder Fehlinterpretationen, die sich aus der Nutzung dieser Übersetzung ergeben.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->