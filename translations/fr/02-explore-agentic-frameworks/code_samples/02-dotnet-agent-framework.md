# 🔍 Exploration du Microsoft Agent Framework - Agent de base (.NET)

## 📋 Objectifs d'apprentissage

Cet exemple explore les concepts fondamentaux du Microsoft Agent Framework à travers une implémentation simple d'agent en .NET. Vous apprendrez les principaux schémas agentiques et comprendrez comment les agents intelligents fonctionnent en coulisses en utilisant C# et l'écosystème .NET.

### Ce que vous allez découvrir

- 🏗️ **Architecture de l'agent** : Comprendre la structure de base des agents IA en .NET
- 🛠️ **Intégration d'outils** : Comment les agents utilisent des fonctions externes pour étendre leurs capacités  
- 💬 **Flux de conversation** : Gérer les conversations multi-tours et le contexte avec la gestion des threads
- 🔧 **Schémas de configuration** : Bonnes pratiques pour la configuration et la gestion des agents en .NET

## 🎯 Concepts clés abordés

### Principes du cadre agentique

- **Autonomie** : Comment les agents prennent des décisions indépendantes en utilisant les abstractions AI de .NET
- **Réactivité** : Répondre aux changements environnementaux et aux entrées utilisateur
- **Proactivité** : Prendre l'initiative en fonction des objectifs et du contexte
- **Capacité sociale** : Interagir par langage naturel avec des fils de conversation

### Composants techniques

- **AIAgent** : Orchestration principale de l'agent et gestion des conversations (.NET)
- **Fonctions outils** : Étendre les capacités de l'agent avec des méthodes et attributs C#
- **Intégration Azure OpenAI** : Exploitation des modèles de langage via l'API Azure OpenAI Responses
- **Configuration sécurisée** : Gestion des points de terminaison basée sur l'environnement

## 🔧 Pile technique

### Technologies principales

- Microsoft Agent Framework (.NET)
- Intégration Azure OpenAI (API Responses)
- Modèles clients Azure.AI.OpenAI
- Configuration basée sur l'environnement avec DotNetEnv

### Capacités de l'agent

- Compréhension et génération du langage naturel
- Appel de fonctions et utilisation d'outils avec attributs C#
- Réponses contextuelles grâce aux sessions de conversation
- Architecture extensible avec des schémas d'injection de dépendances

## 📚 Comparaison des frameworks

Cet exemple illustre l'approche du Microsoft Agent Framework comparée à d'autres frameworks agentiques :

| Fonctionnalité | Microsoft Agent Framework | Autres Frameworks |
|---------|-------------------------|------------------|
| **Intégration** | Écosystème Microsoft natif | Compatibilité variée |
| **Simplicité** | API propre et intuitive | Mise en place souvent complexe |
| **Extensibilité** | Intégration facile des outils | Dépend du framework |
| **Prêt pour l'entreprise** | Conçu pour la production | Variable selon le framework |

## 🚀 Premiers pas

### Prérequis

- [SDK .NET 10](https://dotnet.microsoft.com/download/dotnet/10.0) ou version supérieure
- Un [abonnement Azure](https://azure.microsoft.com/free/) avec une ressource Azure OpenAI et un déploiement de modèle
- Le [CLI Azure](https://learn.microsoft.com/cli/azure/install-azure-cli) — connectez-vous avec `az login`

### Variables d’environnement requises

```bash
# zsh/bash
export AZURE_OPENAI_ENDPOINT=https://<your-resource>.openai.azure.com
export AZURE_OPENAI_DEPLOYMENT=gpt-5-mini
# Connectez-vous ensuite pour que AzureCliCredential puisse obtenir un jeton
az login
```

```powershell
# PowerShell
$env:AZURE_OPENAI_ENDPOINT = "https://<your-resource>.openai.azure.com"
$env:AZURE_OPENAI_DEPLOYMENT = "gpt-5-mini"
# Ensuite, connectez-vous pour que AzureCliCredential puisse obtenir un jeton
az login
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

Consultez [`02-dotnet-agent-framework.cs`](../../../../02-explore-agentic-frameworks/code_samples/02-dotnet-agent-framework.cs) pour le code complet.

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
var deployment = Environment.GetEnvironmentVariable("AZURE_OPENAI_DEPLOYMENT") ?? "gpt-5-mini";

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

## 🎓 Points clés à retenir

1. **Architecture de l'agent** : Le Microsoft Agent Framework propose une approche propre et typée pour construire des agents IA en .NET
2. **Intégration d’outils** : Les fonctions décorées avec l'attribut `[Description]` deviennent des outils disponibles pour l'agent
3. **Contexte de la conversation** : La gestion des sessions permet des conversations multi-tours avec pleine conscience du contexte
4. **Gestion de la configuration** : Les variables d'environnement et la gestion sécurisée des identifiants suivent les meilleures pratiques .NET
5. **API Azure OpenAI Responses** : L'agent utilise l'API Azure OpenAI Responses via le SDK Azure.AI.OpenAI

## 🔗 Ressources supplémentaires

- [Documentation Microsoft Agent Framework](https://learn.microsoft.com/agent-framework)
- [Azure OpenAI dans Microsoft Foundry](https://learn.microsoft.com/azure/ai-services/openai/)
- [Microsoft.Extensions.AI](https://learn.microsoft.com/dotnet/ai/microsoft-extensions-ai)
- [Applications Single File .NET](https://devblogs.microsoft.com/dotnet/announcing-dotnet-run-app)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Avertissement** :
Ce document a été traduit à l'aide du service de traduction automatique [Co-op Translator](https://github.com/Azure/co-op-translator). Bien que nous nous efforçions d'assurer l'exactitude, veuillez noter que les traductions automatisées peuvent contenir des erreurs ou des inexactitudes. Le document original dans sa langue native doit être considéré comme la source faisant autorité. Pour les informations critiques, il est recommandé de recourir à une traduction professionnelle réalisée par un humain. Nous ne saurions être tenus responsables des malentendus ou erreurs d'interprétation découlant de l'utilisation de cette traduction.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->