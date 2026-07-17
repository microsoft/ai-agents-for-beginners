# 🎯 Planification & Modèles de Conception avec Azure OpenAI (API Responses) (.NET)

## 📋 Objectifs d'apprentissage

Ce carnet démontre des modèles de planification et de conception de niveau entreprise pour construire des agents intelligents en utilisant le Microsoft Agent Framework en .NET avec Azure OpenAI (API Responses). Vous apprendrez à créer des agents capables de décomposer des problèmes complexes, de planifier des solutions en plusieurs étapes et d'exécuter des workflows sophistiqués avec les fonctionnalités entreprise de .NET.

## ⚙️ Prérequis & Configuration

**Environnement de Développement :**
- SDK .NET 9.0 ou supérieur
- Visual Studio 2022 ou VS Code avec l'extension C#
- Un abonnement Azure avec une ressource Azure OpenAI et un déploiement de modèle
- L'interface en ligne de commande Azure CLI — connectez-vous avec `az login`

**Dépendances Requises :**
```xml
<PackageReference Include="Microsoft.Extensions.AI" Version="10.*" />
<PackageReference Include="Microsoft.Agents.AI" Version="1.*-*" />
<PackageReference Include="Microsoft.Agents.AI.OpenAI" Version="1.*-*" />
<PackageReference Include="Azure.AI.OpenAI" Version="2.1.0" />
<PackageReference Include="Azure.Identity" Version="1.13.1" />
<PackageReference Include="DotNetEnv" Version="3.1.1" />
```

**Configuration de l'Environnement (fichier .env) :**
```env
AZURE_OPENAI_ENDPOINT=https://<your-resource>.openai.azure.com
AZURE_OPENAI_DEPLOYMENT=gpt-4.1-mini
```

## Exécution du Code

Cette leçon inclut une implémentation d'application .NET Single File. Pour l'exécuter :

```bash
# Rendre le fichier exécutable (Linux/macOS)
chmod +x 07-dotnet-agent-framework.cs

# Exécuter l'application
./07-dotnet-agent-framework.cs
```

Ou utilisez la commande dotnet run :

```bash
dotnet run 07-dotnet-agent-framework.cs
```

## Implémentation du Code

L'implémentation complète est disponible dans `07-dotnet-agent-framework.cs`, qui démontre :

- Chargement de la configuration d'environnement avec DotNetEnv
- Configuration du client Azure OpenAI et création d'un agent IA avec `GetChatClient().AsAIAgent()`
- Définition de modèles de données structurés (Plan et TravelPlan) avec sérialisation JSON
- Création d'un agent IA avec sortie structurée utilisant un schéma JSON
- Exécution des requêtes de planification avec des réponses typées en toute sécurité

## Concepts Clés

### Planification Structurée avec Modèles Type-Sûrs

L'agent utilise des classes C# pour définir la structure des sorties de planification :

```csharp
public class Plan
{
    [JsonPropertyName("assigned_agent")]
    public string? Assigned_agent { get; set; }

    [JsonPropertyName("task_details")]
    public string? Task_details { get; set; }
}

public class TravelPlan
{
    [JsonPropertyName("main_task")]
    public string? Main_task { get; set; }

    [JsonPropertyName("subtasks")]
    public IList<Plan> Subtasks { get; set; }
}
```

### Schéma JSON pour Sorties Structurées

L'agent est configuré pour retourner des réponses correspondant au schéma TravelPlan :

```csharp
ChatClientAgentOptions agentOptions = new()
{
    Name = AGENT_NAME,
    Description = AGENT_INSTRUCTIONS,
    ChatOptions = new()
    {
        ResponseFormat = ChatResponseFormatJson.ForJsonSchema(
            schema: AIJsonUtilities.CreateJsonSchema(typeof(TravelPlan)),
            schemaName: "TravelPlan",
            schemaDescription: "Travel Plan with main_task and subtasks")
    }
};
```

### Instructions pour l'Agent de Planification

L'agent agit comme un coordinateur, déléguant les tâches à des sous-agents spécialisés :

- FlightBooking : Pour la réservation de vols et fournir des informations sur les vols
- HotelBooking : Pour la réservation d'hôtels et fournir des informations sur les hôtels
- CarRental : Pour la réservation de voitures et fournir des informations sur la location de voitures
- ActivitiesBooking : Pour la réservation d'activités et fournir des informations sur les activités
- DestinationInfo : Pour fournir des informations sur les destinations
- DefaultAgent : Pour gérer les requêtes générales

## Résultat Attendu

Lorsque vous exécutez l'agent avec une demande de planification de voyage, il analysera la demande et générera un plan structuré avec une affectation appropriée des tâches aux agents spécialisés, formaté en JSON conforme au schéma TravelPlan.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Avertissement** :
Ce document a été traduit à l'aide du service de traduction automatique [Co-op Translator](https://github.com/Azure/co-op-translator). Bien que nous nous efforçions d'assurer l'exactitude, veuillez noter que les traductions automatisées peuvent contenir des erreurs ou des inexactitudes. Le document original dans sa langue native doit être considéré comme la source faisant autorité. Pour les informations critiques, il est recommandé de recourir à une traduction professionnelle réalisée par un humain. Nous ne saurions être tenus responsables des malentendus ou erreurs d'interprétation découlant de l'utilisation de cette traduction.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->