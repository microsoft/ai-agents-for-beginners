<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "033f170be3b54183e2f6b5463371ab69",
  "translation_date": "2025-11-07T09:30:51+00:00",
  "source_file": "02-explore-agentic-frameworks/code_samples/02-dotnet-agent-framework.md",
  "language_code": "de"
}
-->
# 🔍 Erkundung von Agenten-Frameworks - Basisagent (.NET)

## 📋 Lernziele

Dieses Notebook untersucht die grundlegenden Konzepte des Microsoft Agent Frameworks durch eine einfache Agentenimplementierung in .NET. Sie lernen die Kernmuster von Agenten kennen und verstehen, wie intelligente Agenten mit C# und dem .NET-Ökosystem im Hintergrund arbeiten.

**Was Sie entdecken werden:**
- 🏗️ **Agentenarchitektur**: Verständnis der grundlegenden Struktur von KI-Agenten in .NET
- 🛠️ **Tool-Integration**: Wie Agenten externe Funktionen nutzen, um ihre Fähigkeiten zu erweitern  
- 💬 **Konversationsfluss**: Verwaltung von mehrstufigen Gesprächen und Kontext mit Thread-Management
- 🔧 **Konfigurationsmuster**: Best Practices für die Einrichtung und Verwaltung von Agenten in .NET

## 🎯 Wichtige behandelte Konzepte

### Prinzipien des Agenten-Frameworks
- **Autonomie**: Wie Agenten unabhängige Entscheidungen mithilfe von .NET-KI-Abstraktionen treffen
- **Reaktivität**: Reaktion auf Umweltveränderungen und Benutzereingaben
- **Proaktivität**: Eigeninitiative basierend auf Zielen und Kontext
- **Soziale Fähigkeit**: Interaktion durch natürliche Sprache mit Konversationsthreads

### Technische Komponenten
- **AIAgent**: Kernsteuerung des Agenten und Konversationsmanagement (.NET)
- **Tool-Funktionen**: Erweiterung der Agentenfähigkeiten mit C#-Methoden und Attributen
- **OpenAI-Integration**: Nutzung von Sprachmodellen über standardisierte .NET-APIs
- **Umgebungsmanagement**: Sichere Konfiguration und Umgang mit Anmeldedaten mit DotNetEnv

## ⚙️ Voraussetzungen & Einrichtung

**Erforderliche Abhängigkeiten:**
- .NET 9.0 SDK oder höher
- Visual Studio 2022 oder VS Code mit C#-Erweiterung

**NuGet-Pakete:**
- `Microsoft.Extensions.AI` - Kern-KI-Abstraktionen
- `Microsoft.Extensions.AI.OpenAI` - OpenAI-Integration (Vorschau)
- `DotNetEnv` - Verwaltung von Umgebungsvariablen

**Umgebungskonfiguration (.env-Datei):**
```env
GITHUB_TOKEN=your_github_personal_access_token
GITHUB_ENDPOINT=https://models.inference.ai.azure.com
GITHUB_MODEL_ID=gpt-4o-mini
```

## 🔧 Technischer Stack

**Kerntechnologien:**
- Microsoft Agent Framework (.NET)
- GitHub Models API-Integration
- OpenAI-kompatible Client-Muster
- Konfigurationsmanagement basierend auf Umgebungen mit DotNetEnv

**Agentenfähigkeiten:**
- Verständnis und Generierung natürlicher Sprache
- Funktionsaufrufe und Tool-Nutzung mit C#-Attributen
- Kontextbewusste Antworten mit Konversationsthreads
- Erweiterbare Architektur mit Dependency Injection-Mustern

## 📚 Framework-Vergleich

Dieses Beispiel zeigt den Ansatz des Microsoft Agent Frameworks in .NET im Vergleich zu anderen Plattformen:

| Funktion | .NET Agent Framework | Python-Äquivalente |
|----------|-----------------------|--------------------|
| **Typensicherheit** | Starke Typisierung mit C# | Dynamische Typisierung |
| **Integration** | Native .NET-Ökosystem | Unterschiedliche Kompatibilität |
| **Leistung** | Kompilierte Code-Leistung | Interpretierte Ausführung |
| **Unternehmensbereit** | Entwickelt für Produktionsanwendungen in .NET | Variiert je nach Framework |
| **Werkzeuge** | Integration in Visual Studio | Abhängig von der IDE |

## 🚀 Erste Schritte

Folgen Sie den untenstehenden Schritten, um Ihren ersten Basisagenten in .NET zu erstellen und grundlegende Agentenkonzepte zu verstehen!

## 📦 Installation und Einrichtung

Dieses Beispiel ist als ausführbare .NET Single File App verfügbar. Siehe die begleitende Datei `02-dotnet-agent-framework.cs` für die vollständige Implementierung.

Um dieses Beispiel auszuführen:

```bash
chmod +x 02-dotnet-agent-framework.cs
./02-dotnet-agent-framework.cs
```

Oder mit dem dotnet CLI:

```bash
dotnet run 02-dotnet-agent-framework.cs
```

## 💡 Code-Durchlauf

Die vollständige Implementierung umfasst:

### 1. Paketabhängigkeiten

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

### 2. Wichtige Importe

```csharp
using System;
using System.ComponentModel;
using System.ClientModel;
using Microsoft.Extensions.AI;
using Microsoft.Agents.AI;
using OpenAI;
using DotNetEnv;
```

### 3. Umgebungskonfiguration

```csharp
// Load configuration from .env file
Env.Load("../../../.env");
```

### 4. Definition von Tool-Funktionen

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

### 5. Konfiguration und Client-Einrichtung

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

### 6. Agentenkonfiguration

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

### 7. Initialisierung des Agenten

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

### 8. Konversationsmanagement

```csharp
// Create new conversation thread
AgentThread thread = agent.GetNewThread();

// Execute agent: First travel planning request
Console.WriteLine(await agent.RunAsync("Plan me a day trip", thread));

// Execute agent: Follow-up request with context awareness
Console.WriteLine(await agent.RunAsync("I don't like that destination. Plan me another vacation.", thread));
```

## 🎓 Wichtige Erkenntnisse

1. **Agentenarchitektur**: Das Microsoft Agent Framework bietet einen klaren, typensicheren Ansatz für den Aufbau von KI-Agenten in .NET
2. **Tool-Integration**: Funktionen, die mit `[Description]`-Attributen versehen sind, werden zu verfügbaren Tools für den Agenten
3. **Konversationskontext**: Thread-Management ermöglicht mehrstufige Gespräche mit vollständigem Kontextbewusstsein
4. **Konfigurationsmanagement**: Umgebungsvariablen und sicherer Umgang mit Anmeldedaten folgen den Best Practices von .NET
5. **OpenAI-Kompatibilität**: GitHub Models-Integration funktioniert nahtlos über OpenAI-kompatible APIs

## 🔗 Zusätzliche Ressourcen

- [Microsoft Agent Framework Dokumentation](https://learn.microsoft.com/en-us/dotnet/ai/agents)
- [GitHub Models Marketplace](https://github.com/marketplace/models)
- [Microsoft.Extensions.AI](https://learn.microsoft.com/en-us/dotnet/ai/microsoft-extensions-ai-overview)
- [.NET Single File Apps](https://devblogs.microsoft.com/dotnet/announcing-dotnet-run-app/)

---

**Haftungsausschluss**:  
Dieses Dokument wurde mit dem KI-Übersetzungsdienst [Co-op Translator](https://github.com/Azure/co-op-translator) übersetzt. Obwohl wir uns um Genauigkeit bemühen, beachten Sie bitte, dass automatisierte Übersetzungen Fehler oder Ungenauigkeiten enthalten können. Das Originaldokument in seiner ursprünglichen Sprache sollte als maßgebliche Quelle betrachtet werden. Für kritische Informationen wird eine professionelle menschliche Übersetzung empfohlen. Wir übernehmen keine Haftung für Missverständnisse oder Fehlinterpretationen, die sich aus der Nutzung dieser Übersetzung ergeben.