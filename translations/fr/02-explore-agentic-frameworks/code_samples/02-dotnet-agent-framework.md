<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "e23058f87779da210fc0257ee2747c53",
  "translation_date": "2025-11-13T10:50:26+00:00",
  "source_file": "02-explore-agentic-frameworks/code_samples/02-dotnet-agent-framework.md",
  "language_code": "fr"
}
-->
# 🔍 Exploration du Microsoft Agent Framework - Agent de base (.NET)

## 📋 Objectifs d'apprentissage

Cet exemple explore les concepts fondamentaux du Microsoft Agent Framework à travers une implémentation basique d'un agent en .NET. Vous découvrirez les principaux modèles agentiques et comprendrez comment fonctionnent les agents intelligents en coulisses avec C# et l'écosystème .NET.

### Ce que vous allez découvrir

- 🏗️ **Architecture des agents** : Comprendre la structure de base des agents IA en .NET
- 🛠️ **Intégration des outils** : Comment les agents utilisent des fonctions externes pour étendre leurs capacités  
- 💬 **Flux de conversation** : Gérer des conversations multi-tours et le contexte avec la gestion des threads
- 🔧 **Modèles de configuration** : Meilleures pratiques pour la configuration et la gestion des agents en .NET

## 🎯 Concepts clés abordés

### Principes du Framework Agentique

- **Autonomie** : Comment les agents prennent des décisions indépendantes en utilisant les abstractions IA de .NET
- **Réactivité** : Répondre aux changements environnementaux et aux entrées utilisateur
- **Proactivité** : Prendre des initiatives basées sur des objectifs et le contexte
- **Capacité sociale** : Interagir en langage naturel avec des fils de conversation

### Composants techniques

- **AIAgent** : Orchestration centrale des agents et gestion des conversations (.NET)
- **Fonctions d'outils** : Extension des capacités des agents avec des méthodes et attributs C#
- **Intégration OpenAI** : Exploiter les modèles linguistiques via des API standardisées .NET
- **Configuration sécurisée** : Gestion des clés API basée sur l'environnement

## 🔧 Pile technologique

### Technologies principales

- Microsoft Agent Framework (.NET)
- Intégration de l'API GitHub Models
- Modèles compatibles OpenAI
- Configuration basée sur l'environnement avec DotNetEnv

### Capacités des agents

- Compréhension et génération de langage naturel
- Appels de fonctions et utilisation d'outils avec des attributs C#
- Réponses contextuelles avec fils de conversation
- Architecture extensible avec des modèles d'injection de dépendances

## 📚 Comparaison des frameworks

Cet exemple illustre l'approche du Microsoft Agent Framework par rapport à d'autres frameworks agentiques :

| Fonctionnalité | Microsoft Agent Framework | Autres frameworks |
|----------------|---------------------------|-------------------|
| **Intégration** | Écosystème natif Microsoft | Compatibilité variée |
| **Simplicité** | API propre et intuitive | Configuration souvent complexe |
| **Extensibilité** | Intégration facile des outils | Dépendant du framework |
| **Prêt pour l'entreprise** | Conçu pour la production | Variable selon le framework |

## 🚀 Premiers pas

### Prérequis

- [.NET 10 SDK](https://dotnet.microsoft.com/download/dotnet/10.0) ou version ultérieure
- [Jeton d'accès à l'API GitHub Models](https://docs.github.com/github-models/github-models-at-scale/using-your-own-api-keys-in-github-models)

### Variables d'environnement requises

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

### Exemple de code

Pour exécuter l'exemple de code,

```bash
# zsh/bash
chmod +x ./02-dotnet-agent-framework.cs
./02-dotnet-agent-framework.cs
```

Ou en utilisant le CLI dotnet :

```bash
dotnet run ./02-dotnet-agent-framework.cs
```

Voir [`02-dotnet-agent-framework.cs`](../../../../02-explore-agentic-frameworks/code_samples/02-dotnet-agent-framework.cs) pour le code complet.

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

## 🎓 Points clés à retenir

1. **Architecture des agents** : Le Microsoft Agent Framework offre une approche propre et typée pour construire des agents IA en .NET
2. **Intégration des outils** : Les fonctions décorées avec des attributs `[Description]` deviennent des outils disponibles pour l'agent
3. **Contexte de conversation** : La gestion des threads permet des conversations multi-tours avec une pleine conscience du contexte
4. **Gestion de la configuration** : Les variables d'environnement et la gestion sécurisée des identifiants suivent les meilleures pratiques .NET
5. **Compatibilité OpenAI** : L'intégration des modèles GitHub fonctionne parfaitement via des API compatibles OpenAI

## 🔗 Ressources supplémentaires

- [Documentation du Microsoft Agent Framework](https://learn.microsoft.com/agent-framework)
- [Marketplace GitHub Models](https://github.com/marketplace?type=models)
- [Microsoft.Extensions.AI](https://learn.microsoft.com/dotnet/ai/microsoft-extensions-ai)
- [.NET Single File Apps](https://devblogs.microsoft.com/dotnet/announcing-dotnet-run-app)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Avertissement** :  
Ce document a été traduit à l'aide du service de traduction IA [Co-op Translator](https://github.com/Azure/co-op-translator). Bien que nous nous efforcions d'assurer l'exactitude, veuillez noter que les traductions automatiques peuvent contenir des erreurs ou des inexactitudes. Le document original dans sa langue d'origine doit être considéré comme la source faisant autorité. Pour des informations critiques, il est recommandé de recourir à une traduction humaine professionnelle. Nous ne sommes pas responsables des malentendus ou des interprétations erronées résultant de l'utilisation de cette traduction.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->