# 🌍 Agent de voyage IA avec Microsoft Agent Framework (.NET)

## 📋 Aperçu du scénario

Cet exemple montre comment créer un agent intelligent de planification de voyages en utilisant le Microsoft Agent Framework pour .NET. L'agent peut générer automatiquement des itinéraires personnalisés pour des excursions d'une journée vers des destinations aléatoires dans le monde entier.

### Fonctionnalités clés :

- 🎲 **Sélection aléatoire de destination** : Utilise un outil personnalisé pour choisir des lieux de vacances
- 🗺️ **Planification intelligente de voyage** : Crée des itinéraires détaillés jour par jour
- 🔄 **Streaming en temps réel** : Prend en charge les réponses immédiates et en flux continu
- 🛠️ **Intégration d'outils personnalisés** : Démontre comment étendre les capacités de l'agent

## 🔧 Architecture technique

### Technologies principales

- **Microsoft Agent Framework** : Dernière implémentation .NET pour le développement d'agents IA
- **Azure OpenAI (API Responses)** : Utilise l'API Azure OpenAI Responses pour l'inférence du modèle
- **Azure Identity** : Connexion sécurisée via `AzureCliCredential` (`az login`)
- **Configuration sécurisée** : Gestion des points de terminaison basée sur l'environnement

### Composants clés

1. **AIAgent** : L'orchestrateur principal de l'agent qui gère le flux de la conversation
2. **Outils personnalisés** : fonction `GetRandomDestination()` accessible à l'agent
3. **Client Responses** : Interface de conversation basée sur Azure OpenAI Responses
4. **Support du streaming** : Capacités de génération de réponses en temps réel

### Modèle d’intégration

```mermaid
graph LR
    A[Demande de l'utilisateur] --> B[Agent IA]
    B --> C[Azure OpenAI (API des réponses)]
    B --> D[Outil GetRandomDestination]
    C --> E[Itinéraire de voyage]
    D --> E
```

## 🚀 Démarrage

### Prérequis

- [SDK .NET 10](https://dotnet.microsoft.com/download/dotnet/10.0) ou supérieur
- Un [abonnement Azure](https://azure.microsoft.com/free/) avec une ressource Azure OpenAI et un déploiement de modèle
- L’[Azure CLI](https://learn.microsoft.com/cli/azure/install-azure-cli) — connectez-vous avec `az login`

### Variables d’environnement requises

```bash
# zsh/bash
export AZURE_OPENAI_ENDPOINT=https://<your-resource>.openai.azure.com
export AZURE_OPENAI_DEPLOYMENT=gpt-5-mini
# Ensuite, connectez-vous pour que AzureCliCredential puisse obtenir un jeton
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

Pour exécuter l’exemple de code,

```bash
# zsh/bash
chmod +x ./01-dotnet-agent-framework.cs
./01-dotnet-agent-framework.cs
```

Ou en utilisant la CLI dotnet :

```bash
dotnet run ./01-dotnet-agent-framework.cs
```

Voir [`01-dotnet-agent-framework.cs`](../../../../01-intro-to-ai-agents/code_samples/01-dotnet-agent-framework.cs) pour le code complet.

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
var deployment = Environment.GetEnvironmentVariable("AZURE_OPENAI_DEPLOYMENT") ?? "gpt-5-mini";

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

## 🎓 Points clés à retenir

1. **Architecture de l’agent** : Le Microsoft Agent Framework fournit une approche propre et typée pour construire des agents IA en .NET
2. **Intégration d’outils** : Les fonctions décorées avec des attributs `[Description]` deviennent des outils accessibles pour l’agent
3. **Gestion de la configuration** : Les variables d’environnement et la gestion sécurisée des identifiants suivent les meilleures pratiques .NET
4. **Azure OpenAI Responses API** : L’agent utilise l’API Azure OpenAI Responses via le SDK Azure.AI.OpenAI

## 🔗 Ressources supplémentaires

- [Documentation Microsoft Agent Framework](https://learn.microsoft.com/agent-framework)
- [Azure OpenAI dans Microsoft Foundry](https://learn.microsoft.com/azure/ai-services/openai/)
- [Microsoft.Extensions.AI](https://learn.microsoft.com/dotnet/ai/microsoft-extensions-ai)
- [Applications à fichier unique .NET](https://devblogs.microsoft.com/dotnet/announcing-dotnet-run-app)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Avertissement** :
Ce document a été traduit à l'aide du service de traduction automatique [Co-op Translator](https://github.com/Azure/co-op-translator). Bien que nous nous efforçions d'assurer l'exactitude, veuillez noter que les traductions automatisées peuvent contenir des erreurs ou des inexactitudes. Le document original dans sa langue native doit être considéré comme la source faisant autorité. Pour les informations critiques, il est recommandé de recourir à une traduction professionnelle réalisée par un humain. Nous ne saurions être tenus responsables des malentendus ou erreurs d'interprétation découlant de l'utilisation de cette traduction.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->