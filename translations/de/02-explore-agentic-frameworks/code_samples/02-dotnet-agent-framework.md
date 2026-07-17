# 🔍 Erforschung des Microsoft Agent Framework - Grundlegender Agent (.NET)

## 📋 Lernziele

Dieses Beispiel erkundet die grundlegenden Konzepte des Microsoft Agent Frameworks durch eine einfache Agentenimplementierung in .NET. Sie lernen grundlegende agentenbasierte Muster und verstehen, wie intelligente Agenten unter der Haube mit C# und dem .NET-Ökosystem arbeiten.

### Was Sie entdecken werden

- 🏗️ **Agentenarchitektur**: Verständnis der grundlegenden Struktur von KI-Agenten in .NET
- 🛠️ **Werkzeugintegration**: Wie Agenten externe Funktionen zur Erweiterung der Fähigkeiten nutzen  
- 💬 **Gesprächsablauf**: Verwaltung mehrerer Gesprächsrunden und Kontext mit Thread-Management
- 🔧 **Konfigurationsmuster**: Best Practices für Agenten-Setup und Verwaltung in .NET

## 🎯 Wichtige behandelte Konzepte

### Agentenframework-Prinzipien

- **Autonomie**: Wie Agenten eigenständige Entscheidungen mit .NET KI-Abstraktionen treffen
- **Reaktivität**: Reaktion auf Umweltänderungen und Benutzereingaben
- **Proaktivität**: Initiative ergreifen basierend auf Zielen und Kontext
- **Soziale Fähigkeiten**: Interaktion durch natürliche Sprache mit Gesprächsfäden

### Technische Komponenten

- **AIAgent**: Kerndienst zur Agentenorchestrierung und Gesprächsverwaltung (.NET)
- **Werkzeugfunktionen**: Erweiterung der Agentenfähigkeiten mit C#-Methoden und Attributen
- **Azure OpenAI Integration**: Nutzung von Sprachmodellen über die Azure OpenAI Responses API
- **Sichere Konfiguration**: Endpoint-Management basierend auf Umgebungsvariablen

## 🔧 Technischer Stack

### Kerntechnologien

- Microsoft Agent Framework (.NET)
- Azure OpenAI (Responses API) Integration
- Azure.AI.OpenAI Client-Muster
- Umgebungsbasierte Konfiguration mit DotNetEnv

### Agentenfähigkeiten

- Verständnis und Erzeugung natürlicher Sprache
- Funktionsaufrufe und Werkzeugnutzung mit C#-Attributen
- Kontextbewusste Antworten mit Gesprächssitzungen
- Erweiterbare Architektur mit Dependency Injection-Mustern

## 📚 Framework-Vergleich

Dieses Beispiel zeigt den Ansatz des Microsoft Agent Framework im Vergleich zu anderen agentenbasierten Frameworks:

| Funktion | Microsoft Agent Framework | Andere Frameworks |
|---------|-------------------------|------------------|
| **Integration** | Native Microsoft-Umgebung | Unterschiedliche Kompatibilität |
| **Einfachheit** | Saubere, intuitive API | Oft komplexe Einrichtung |
| **Erweiterbarkeit** | Einfache Werkzeugintegration | Framework-abhängig |
| **Enterprise-Ready** | Für Produktion ausgelegt | Varriert je nach Framework |

## 🚀 Erste Schritte

### Voraussetzungen

- [.NET 10 SDK](https://dotnet.microsoft.com/download/dotnet/10.0) oder höher
- Ein [Azure-Abonnement](https://azure.microsoft.com/free/) mit einer Azure OpenAI-Ressource und einer Modellbereitstellung
- Die [Azure CLI](https://learn.microsoft.com/cli/azure/install-azure-cli) — Anmeldung mit `az login`

### Erforderliche Umgebungsvariablen

```bash
# zsh/bash
export AZURE_OPENAI_ENDPOINT=https://<your-resource>.openai.azure.com
export AZURE_OPENAI_DEPLOYMENT=gpt-4.1-mini
# Melden Sie sich dann an, damit AzureCliCredential ein Token abrufen kann
az login
```

```powershell
# PowerShell
$env:AZURE_OPENAI_ENDPOINT = "https://<your-resource>.openai.azure.com"
$env:AZURE_OPENAI_DEPLOYMENT = "gpt-4.1-mini"
# Dann melden Sie sich an, damit AzureCliCredential ein Token erhalten kann
az login
```

### Beispielcode

Um das Codebeispiel auszuführen,

```bash
# zsh/bash
chmod +x ./02-dotnet-agent-framework.cs
./02-dotnet-agent-framework.cs
```

Oder mit der dotnet CLI:

```bash
dotnet run ./02-dotnet-agent-framework.cs
```

Siehe [`02-dotnet-agent-framework.cs`](../../../../02-explore-agentic-frameworks/code_samples/02-dotnet-agent-framework.cs) für den vollständigen Code.

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
var deployment = Environment.GetEnvironmentVariable("AZURE_OPENAI_DEPLOYMENT") ?? "gpt-4.1-mini";

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
    .GetChatClient(deployment)
    .AsAIAgent(
        name: AGENT_NAME,
        instructions: AGENT_INSTRUCTIONS,
        tools: [AIFunctionFactory.Create(GetRandomDestination)]
    );

// Create New Session for Context Management.
// Initialize a new conversation session to maintain context across multiple interactions
// Sessions enable the agent to remember previous exchanges and maintain conversational state
// This is essential for multi-turn conversations and contextual understanding
AgentSession session = await agent.CreateSessionAsync();

// Execute Agent: First Travel Planning Request
// Run the agent with an initial request that will likely trigger the random destination tool
// The agent will analyze the request, use the GetRandomDestination tool, and create an itinerary
// Using the session parameter maintains conversation context for subsequent interactions
await foreach (var update in agent.RunStreamingAsync("Plan me a day trip", session))
{
    await Task.Delay(10);
    Console.Write(update);
}

Console.WriteLine();

// Execute Agent: Follow-up Request with Context Awareness
// Demonstrate contextual conversation by referencing the previous response
// The agent remembers the previous destination suggestion and will provide an alternative
// This showcases the power of conversation sessions and contextual understanding in .NET agents
await foreach (var update in agent.RunStreamingAsync("I don't like that destination. Plan me another vacation.", session))
{
    await Task.Delay(10);
    Console.Write(update);
}
```

## 🎓 Wichtige Erkenntnisse

1. **Agentenarchitektur**: Das Microsoft Agent Framework bietet einen sauberen, typensicheren Ansatz zum Erstellen von KI-Agenten in .NET
2. **Werkzeugintegration**: Funktionen mit `[Description]`-Attributen werden für den Agenten verfügbare Werkzeuge
3. **Gesprächskontext**: Sitzungsverwaltung ermöglicht mehrstufige Gespräche mit vollem Kontextbewusstsein
4. **Konfigurationsmanagement**: Umgebungsvariablen und sichere Anmeldeinformationen folgen den .NET-Best-Practices
5. **Azure OpenAI Responses API**: Der Agent nutzt die Azure OpenAI Responses API über das Azure.AI.OpenAI SDK

## 🔗 Weitere Ressourcen

- [Microsoft Agent Framework Dokumentation](https://learn.microsoft.com/agent-framework)
- [Azure OpenAI in Microsoft Foundry](https://learn.microsoft.com/azure/ai-services/openai/)
- [Microsoft.Extensions.AI](https://learn.microsoft.com/dotnet/ai/microsoft-extensions-ai)
- [.NET Single File Apps](https://devblogs.microsoft.com/dotnet/announcing-dotnet-run-app)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Haftungsausschluss**:
Dieses Dokument wurde mit dem KI-Übersetzungsdienst [Co-op Translator](https://github.com/Azure/co-op-translator) übersetzt. Obwohl wir uns um Genauigkeit bemühen, beachten Sie bitte, dass automatisierte Übersetzungen Fehler oder Ungenauigkeiten enthalten können. Das Originaldokument in seiner Ursprungssprache gilt als maßgebliche Quelle. Bei kritischen Informationen wird eine professionelle menschliche Übersetzung empfohlen. Wir übernehmen keine Haftung für Missverständnisse oder Fehlinterpretationen, die aus der Verwendung dieser Übersetzung entstehen.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->