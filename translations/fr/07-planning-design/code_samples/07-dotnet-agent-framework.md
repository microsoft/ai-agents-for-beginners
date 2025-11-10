<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "2d13c1e3518a0257a00fea949e2d0350",
  "translation_date": "2025-11-07T09:54:08+00:00",
  "source_file": "07-planning-design/code_samples/07-dotnet-agent-framework.md",
  "language_code": "fr"
}
-->
# 🎯 Planification et modèles de conception avec les modèles GitHub (.NET)

## 📋 Objectifs d'apprentissage

Ce notebook illustre des modèles de planification et de conception de niveau entreprise pour créer des agents intelligents en utilisant le Microsoft Agent Framework en .NET avec les modèles GitHub. Vous apprendrez à créer des agents capables de décomposer des problèmes complexes, de planifier des solutions en plusieurs étapes et d'exécuter des workflows sophistiqués en exploitant les fonctionnalités d'entreprise de .NET.

## ⚙️ Prérequis et configuration

**Environnement de développement :**
- SDK .NET 9.0 ou supérieur
- Visual Studio 2022 ou VS Code avec l'extension C#
- Accès à l'API des modèles GitHub

**Dépendances requises :**
```xml
<PackageReference Include="Microsoft.Extensions.AI" Version="9.9.0" />
<PackageReference Include="Microsoft.Extensions.AI.OpenAI" Version="9.9.0-preview.1.25458.4" />
<PackageReference Include="DotNetEnv" Version="3.1.1" />
```

**Configuration de l'environnement (fichier .env) :**
```env
GITHUB_TOKEN=your_github_personal_access_token
GITHUB_ENDPOINT=https://models.inference.ai.azure.com
GITHUB_MODEL_ID=gpt-4o-mini
```

## Exécution du code

Cette leçon inclut une implémentation d'application .NET en fichier unique. Pour l'exécuter :

```bash
# Make the file executable (Linux/macOS)
chmod +x 07-dotnet-agent-framework.cs

# Run the application
./07-dotnet-agent-framework.cs
```

Ou utilisez la commande dotnet run :

```bash
dotnet run 07-dotnet-agent-framework.cs
```

## Implémentation du code

L'implémentation complète est disponible dans `07-dotnet-agent-framework.cs`, qui démontre :

- Chargement de la configuration de l'environnement avec DotNetEnv
- Configuration du client OpenAI pour les modèles GitHub
- Définition de modèles de données structurés (Plan et TravelPlan) avec la sérialisation JSON
- Création d'un agent IA avec des sorties structurées en utilisant un schéma JSON
- Exécution de requêtes de planification avec des réponses typées

## Concepts clés

### Planification structurée avec des modèles typés

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

### Schéma JSON pour des sorties structurées

L'agent est configuré pour retourner des réponses conformes au schéma TravelPlan :

```csharp
ChatClientAgentOptions agentOptions = new(name: AGENT_NAME, instructions: AGENT_INSTRUCTIONS)
{
    ChatOptions = new()
    {
        ResponseFormat = ChatResponseFormatJson.ForJsonSchema(
            schema: AIJsonUtilities.CreateJsonSchema(typeof(TravelPlan)),
            schemaName: "TravelPlan",
            schemaDescription: "Travel Plan with main_task and subtasks")
    }
};
```

### Instructions pour l'agent de planification

L'agent agit comme un coordinateur, déléguant les tâches à des sous-agents spécialisés :

- FlightBooking : Pour réserver des vols et fournir des informations sur les vols
- HotelBooking : Pour réserver des hôtels et fournir des informations sur les hôtels
- CarRental : Pour réserver des voitures et fournir des informations sur la location de voitures
- ActivitiesBooking : Pour réserver des activités et fournir des informations sur les activités
- DestinationInfo : Pour fournir des informations sur les destinations
- DefaultAgent : Pour gérer les demandes générales

## Résultat attendu

Lorsque vous exécutez l'agent avec une demande de planification de voyage, il analysera la demande et générera un plan structuré avec des tâches appropriées assignées à des agents spécialisés, formaté en JSON conforme au schéma TravelPlan.

---

**Avertissement** :  
Ce document a été traduit à l'aide du service de traduction automatique [Co-op Translator](https://github.com/Azure/co-op-translator). Bien que nous nous efforcions d'assurer l'exactitude, veuillez noter que les traductions automatisées peuvent contenir des erreurs ou des inexactitudes. Le document original dans sa langue d'origine doit être considéré comme la source faisant autorité. Pour des informations critiques, il est recommandé de recourir à une traduction humaine professionnelle. Nous ne sommes pas responsables des malentendus ou des interprétations erronées résultant de l'utilisation de cette traduction.