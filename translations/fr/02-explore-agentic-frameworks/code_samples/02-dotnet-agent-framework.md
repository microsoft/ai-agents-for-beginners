<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "033f170be3b54183e2f6b5463371ab69",
  "translation_date": "2025-11-07T09:30:26+00:00",
  "source_file": "02-explore-agentic-frameworks/code_samples/02-dotnet-agent-framework.md",
  "language_code": "fr"
}
-->
# 🔍 Exploration des cadres agentiques - Agent de base (.NET)

## 📋 Objectifs d'apprentissage

Ce notebook explore les concepts fondamentaux du Microsoft Agent Framework à travers une implémentation basique d'un agent en .NET. Vous apprendrez les modèles agentiques essentiels et comprendrez comment fonctionnent les agents intelligents en utilisant C# et l'écosystème .NET.

**Ce que vous allez découvrir :**
- 🏗️ **Architecture des agents** : Comprendre la structure de base des agents IA en .NET
- 🛠️ **Intégration des outils** : Comment les agents utilisent des fonctions externes pour étendre leurs capacités  
- 💬 **Flux de conversation** : Gérer des conversations multi-tours et le contexte avec la gestion des threads
- 🔧 **Modèles de configuration** : Meilleures pratiques pour la configuration et la gestion des agents en .NET

## 🎯 Concepts clés abordés

### Principes du cadre agentique
- **Autonomie** : Comment les agents prennent des décisions indépendantes en utilisant les abstractions IA de .NET
- **Réactivité** : Répondre aux changements environnementaux et aux entrées utilisateur
- **Proactivité** : Prendre des initiatives basées sur des objectifs et le contexte
- **Capacité sociale** : Interagir via le langage naturel avec des fils de conversation

### Composants techniques
- **AIAgent** : Orchestration centrale des agents et gestion des conversations (.NET)
- **Fonctions d'outils** : Extension des capacités des agents avec des méthodes et attributs C#
- **Intégration OpenAI** : Exploiter les modèles de langage via des API standardisées .NET
- **Gestion de l'environnement** : Configuration sécurisée et gestion des identifiants avec DotNetEnv

## ⚙️ Prérequis et configuration

**Dépendances requises :**
- SDK .NET 9.0 ou supérieur
- Visual Studio 2022 ou VS Code avec extension C#

**Packages NuGet :**
- `Microsoft.Extensions.AI` - Abstractions IA principales
- `Microsoft.Extensions.AI.OpenAI` - Intégration OpenAI (aperçu)
- `DotNetEnv` - Gestion des variables d'environnement

**Configuration de l'environnement (fichier .env) :**
```env
GITHUB_TOKEN=your_github_personal_access_token
GITHUB_ENDPOINT=https://models.inference.ai.azure.com
GITHUB_MODEL_ID=gpt-4o-mini
```

## 🔧 Pile technique

**Technologies principales :**
- Microsoft Agent Framework (.NET)
- Intégration API Models GitHub
- Modèles compatibles OpenAI
- Configuration basée sur l'environnement avec DotNetEnv

**Capacités des agents :**
- Compréhension et génération de langage naturel
- Appels de fonctions et utilisation d'outils avec des attributs C#
- Réponses contextuelles avec fils de conversation
- Architecture extensible avec modèles d'injection de dépendances

## 📚 Comparaison des cadres

Cet exemple illustre l'approche du Microsoft Agent Framework en .NET par rapport à d'autres plateformes :

| Fonctionnalité | Cadre Agent .NET | Équivalents Python |
|----------------|------------------|--------------------|
| **Sécurité des types** | Typage fort avec C# | Typage dynamique |
| **Intégration** | Écosystème natif .NET | Compatibilité variée |
| **Performance** | Performance du code compilé | Exécution interprétée |
| **Prêt pour l'entreprise** | Conçu pour les applications .NET en production | Variable selon le cadre |
| **Outils** | Intégration Visual Studio | Dépendant de l'IDE |

## 🚀 Premiers pas

Suivez les cellules ci-dessous pour construire votre premier agent de base en .NET et comprendre les concepts agentiques fondamentaux !

## 📦 Installation et configuration

Cet exemple est disponible sous forme d'application .NET Single File exécutable. Consultez le fichier `02-dotnet-agent-framework.cs` accompagnant pour l'implémentation complète.

Pour exécuter cet exemple :

```bash
chmod +x 02-dotnet-agent-framework.cs
./02-dotnet-agent-framework.cs
```

Ou en utilisant la CLI dotnet :

```bash
dotnet run 02-dotnet-agent-framework.cs
```

## 💡 Analyse du code

L'implémentation complète inclut :

### 1. Dépendances des packages

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

### 2. Importations essentielles

```csharp
using System;
using System.ComponentModel;
using System.ClientModel;
using Microsoft.Extensions.AI;
using Microsoft.Agents.AI;
using OpenAI;
using DotNetEnv;
```

### 3. Configuration de l'environnement

```csharp
// Load configuration from .env file
Env.Load("../../../.env");
```

### 4. Définition des fonctions d'outils

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

### 5. Configuration et mise en place du client

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

### 6. Configuration de l'agent

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

### 7. Initialisation de l'agent

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

### 8. Gestion des conversations

```csharp
// Create new conversation thread
AgentThread thread = agent.GetNewThread();

// Execute agent: First travel planning request
Console.WriteLine(await agent.RunAsync("Plan me a day trip", thread));

// Execute agent: Follow-up request with context awareness
Console.WriteLine(await agent.RunAsync("I don't like that destination. Plan me another vacation.", thread));
```

## 🎓 Points clés à retenir

1. **Architecture des agents** : Le Microsoft Agent Framework offre une approche propre et sécurisée pour créer des agents IA en .NET
2. **Intégration des outils** : Les fonctions décorées avec des attributs `[Description]` deviennent des outils disponibles pour l'agent
3. **Contexte des conversations** : La gestion des threads permet des conversations multi-tours avec une pleine conscience du contexte
4. **Gestion de la configuration** : Les variables d'environnement et la gestion sécurisée des identifiants suivent les meilleures pratiques .NET
5. **Compatibilité OpenAI** : L'intégration des modèles GitHub fonctionne parfaitement via des API compatibles OpenAI

## 🔗 Ressources supplémentaires

- [Documentation Microsoft Agent Framework](https://learn.microsoft.com/en-us/dotnet/ai/agents)
- [Marketplace Models GitHub](https://github.com/marketplace/models)
- [Microsoft.Extensions.AI](https://learn.microsoft.com/en-us/dotnet/ai/microsoft-extensions-ai-overview)
- [Applications .NET Single File](https://devblogs.microsoft.com/dotnet/announcing-dotnet-run-app/)

---

**Avertissement** :  
Ce document a été traduit à l'aide du service de traduction automatique [Co-op Translator](https://github.com/Azure/co-op-translator). Bien que nous nous efforcions d'assurer l'exactitude, veuillez noter que les traductions automatisées peuvent contenir des erreurs ou des inexactitudes. Le document original dans sa langue d'origine doit être considéré comme la source faisant autorité. Pour des informations critiques, il est recommandé de recourir à une traduction humaine professionnelle. Nous ne sommes pas responsables des malentendus ou des interprétations erronées résultant de l'utilisation de cette traduction.