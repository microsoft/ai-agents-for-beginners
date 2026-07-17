# 🌍 KI-Reiseagent mit Microsoft Agent Framework (.NET)

## 📋 Szenarioübersicht

Dieses Beispiel zeigt, wie man einen intelligenten Reiseplanungsagenten mithilfe des Microsoft Agent Frameworks für .NET erstellt. Der Agent kann automatisch personalisierte Tagesausflug-Routen für zufällige Reiseziele weltweit generieren.

### Hauptfunktionen:

- 🎲 **Zufällige Zielauswahl**: Verwendet ein benutzerdefiniertes Tool, um Urlaubsorte auszuwählen
- 🗺️ **Intelligente Reiseplanung**: Erstellt detaillierte Tagesabläufe
- 🔄 **Echtzeit-Streaming**: Unterstützt sowohl sofortige als auch Streaming-Antworten
- 🛠️ **Integration benutzerdefinierter Tools**: Zeigt, wie Agent-Fähigkeiten erweitert werden können

## 🔧 Technische Architektur

### Kerntechnologien

- **Microsoft Agent Framework**: Neueste .NET-Implementierung für KI-Agentenentwicklung
- **Azure OpenAI (Responses API)**: Verwendet die Azure OpenAI Responses API für Modellausführung
- **Azure Identity**: Sicheres Anmelden über `AzureCliCredential` (`az login`)
- **Sichere Konfiguration**: Endpunktverwaltung auf Basis von Umgebungsvariablen

### Hauptkomponenten

1. **AIAgent**: Der Hauptagent-Orchestrator, der den Gesprächsablauf steuert
2. **Benutzerdefinierte Tools**: `GetRandomDestination()`-Funktion, die dem Agenten zur Verfügung steht
3. **Responses-Client**: Gesprächsschnittstelle basierend auf Azure OpenAI Responses
4. **Streaming-Unterstützung**: Echtzeit-Antwortgenerierung

### Integrationsmuster

```mermaid
graph LR
    A[Benutzeranfrage] --> B[KI-Agent]
    B --> C[Azure OpenAI (Antworten API)]
    B --> D[GetRandomDestination Werkzeug]
    C --> E[Reiseplan]
    D --> E
```

## 🚀 Erste Schritte

### Voraussetzungen

- [.NET 10 SDK](https://dotnet.microsoft.com/download/dotnet/10.0) oder höher
- Ein [Azure-Abonnement](https://azure.microsoft.com/free/) mit einer Azure OpenAI-Ressource und einer Modellausführung
- Die [Azure CLI](https://learn.microsoft.com/cli/azure/install-azure-cli) — Anmeldung mit `az login`

### Erforderliche Umgebungsvariablen

```bash
# zsh/bash
export AZURE_OPENAI_ENDPOINT=https://<your-resource>.openai.azure.com
export AZURE_OPENAI_DEPLOYMENT=gpt-4.1-mini
# Melden Sie sich dann an, damit AzureCliCredential ein Token erhalten kann
az login
```

```powershell
# PowerShell
$env:AZURE_OPENAI_ENDPOINT = "https://<your-resource>.openai.azure.com"
$env:AZURE_OPENAI_DEPLOYMENT = "gpt-4.1-mini"
# Melden Sie sich dann an, damit AzureCliCredential ein Token erhalten kann
az login
```

### Beispielcode

Um das Beispiel auszuführen,

```bash
# zsh/bash
chmod +x ./01-dotnet-agent-framework.cs
./01-dotnet-agent-framework.cs
```

Oder mit der dotnet CLI:

```bash
dotnet run ./01-dotnet-agent-framework.cs
```

Siehe [`01-dotnet-agent-framework.cs`](../../../../01-intro-to-ai-agents/code_samples/01-dotnet-agent-framework.cs) für den vollständigen Code.

```csharp
#!/usr/bin/dotnet run

#:package Microsoft.Extensions.AI@10.4.1
#:package Microsoft.Agents.AI.OpenAI@1.1.0
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

// Create AI Agent with Travel Planning Capabilities
// Get the Responses client for the specified deployment and create the AI agent
// Configure agent with travel planning instructions and random destination tool
// The agent can now plan trips using the GetRandomDestination function
AIAgent agent = azureClient
    .GetChatClient(deployment)
    .AsAIAgent(
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

## 🎓 Wichtige Erkenntnisse

1. **Agent-Architektur**: Das Microsoft Agent Framework bietet einen sauberen, typsicheren Ansatz zur Entwicklung von KI-Agenten in .NET
2. **Tool-Integration**: Funktionen mit `[Description]`-Attributen werden als verfügbare Tools für den Agenten aktiviert
3. **Konfigurationsverwaltung**: Umgebungsvariablen und sichere Anmeldeinformationen folgen den besten .NET-Praktiken
4. **Azure OpenAI Responses API**: Der Agent verwendet die Azure OpenAI Responses API über das Azure.AI.OpenAI SDK

## 🔗 Zusätzliche Ressourcen

- [Microsoft Agent Framework Dokumentation](https://learn.microsoft.com/agent-framework)
- [Azure OpenAI in Microsoft Foundry](https://learn.microsoft.com/azure/ai-services/openai/)
- [Microsoft.Extensions.AI](https://learn.microsoft.com/dotnet/ai/microsoft-extensions-ai)
- [.NET Einzeldokument-Anwendungen](https://devblogs.microsoft.com/dotnet/announcing-dotnet-run-app)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Haftungsausschluss**:
Dieses Dokument wurde mit dem KI-Übersetzungsdienst [Co-op Translator](https://github.com/Azure/co-op-translator) übersetzt. Obwohl wir uns um Genauigkeit bemühen, beachten Sie bitte, dass automatisierte Übersetzungen Fehler oder Ungenauigkeiten enthalten können. Das Originaldokument in seiner Ursprungssprache gilt als maßgebliche Quelle. Bei kritischen Informationen wird eine professionelle menschliche Übersetzung empfohlen. Wir übernehmen keine Haftung für Missverständnisse oder Fehlinterpretationen, die aus der Verwendung dieser Übersetzung entstehen.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->