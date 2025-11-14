<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "5f5a5f2902f32272257506d88d3c43a1",
  "translation_date": "2025-11-07T09:13:02+00:00",
  "source_file": "08-multi-agent/code_samples/08-dotnet-agent-framework.md",
  "language_code": "fr"
}
-->
# 🤝 Systèmes de flux de travail multi-agents pour entreprises (.NET)

## 📋 Objectifs d'apprentissage

Ce notebook montre comment construire des systèmes multi-agents sophistiqués de niveau entreprise en utilisant le Microsoft Agent Framework dans .NET avec les modèles GitHub. Vous apprendrez à orchestrer plusieurs agents spécialisés travaillant ensemble via des flux de travail structurés, en exploitant les fonctionnalités d'entreprise de .NET pour des solutions prêtes à la production.

**Capacités multi-agents pour entreprises que vous allez développer :**
- 👥 **Collaboration entre agents** : Coordination des agents avec validation au moment de la compilation
- 🔄 **Orchestration de flux de travail** : Définition déclarative de flux de travail avec les modèles asynchrones de .NET
- 🎭 **Spécialisation des rôles** : Personnalités d'agents fortement typées et domaines d'expertise
- 🏢 **Intégration d'entreprise** : Modèles prêts pour la production avec surveillance et gestion des erreurs

## ⚙️ Prérequis et configuration

**Environnement de développement :**
- SDK .NET 9.0 ou supérieur
- Visual Studio 2022 ou VS Code avec extension C#
- Abonnement Azure (pour les agents persistants)

**Packages NuGet requis :**
```xml
<PackageReference Include="Microsoft.Extensions.AI.Abstractions" Version="9.9.0" />
<PackageReference Include="Azure.AI.Agents.Persistent" Version="1.2.0-beta.4" />
<PackageReference Include="Azure.Identity" Version="1.15.0" />
<PackageReference Include="System.Linq.Async" Version="6.0.3" />
<PackageReference Include="Microsoft.Extensions.AI" Version="9.8.0" />
<PackageReference Include="DotNetEnv" Version="3.1.1" />
<PackageReference Include="Microsoft.Extensions.AI.OpenAI" Version="9.9.0-preview.1.25458.4" />
```

## Exemple de code

Le code complet fonctionnel pour cette leçon est disponible dans le fichier C# associé : [`08-dotnet-agent-framework.cs`](../../../../08-multi-agent/code_samples/08-dotnet-agent-framework.cs)

Pour exécuter l'exemple :

```bash
# Make the file executable (Linux/macOS)
chmod +x 08-dotnet-agent-framework.cs

# Run the sample
./08-dotnet-agent-framework.cs
```

Ou en utilisant l'interface CLI .NET :

```bash
dotnet run 08-dotnet-agent-framework.cs
```

## Ce que cet exemple démontre

Ce système de flux de travail multi-agents crée un service de recommandations de voyage pour hôtels avec deux agents spécialisés :

1. **Agent FrontDesk** : Un agent de voyage qui fournit des recommandations d'activités et de lieux
2. **Agent Concierge** : Examine les recommandations pour garantir des expériences authentiques et non touristiques

Les agents collaborent dans un flux de travail où :
- L'agent FrontDesk reçoit la demande initiale de voyage
- L'agent Concierge examine et affine la recommandation
- Le flux de travail diffuse les réponses en temps réel

## Concepts clés

### Coordination des agents
L'exemple démontre une coordination des agents avec validation au moment de la compilation en utilisant le Microsoft Agent Framework.

### Orchestration de flux de travail
Utilise une définition déclarative de flux de travail avec les modèles asynchrones de .NET pour connecter plusieurs agents dans un pipeline.

### Diffusion des réponses
Implémente une diffusion en temps réel des réponses des agents en utilisant des énumérables asynchrones et une architecture événementielle.

### Intégration d'entreprise
Présente des modèles prêts pour la production, notamment :
- Configuration via des variables d'environnement
- Gestion sécurisée des identifiants
- Gestion des erreurs
- Traitement d'événements asynchrones

---

**Avertissement** :  
Ce document a été traduit à l'aide du service de traduction automatique [Co-op Translator](https://github.com/Azure/co-op-translator). Bien que nous nous efforcions d'assurer l'exactitude, veuillez noter que les traductions automatisées peuvent contenir des erreurs ou des inexactitudes. Le document original dans sa langue d'origine doit être considéré comme la source faisant autorité. Pour des informations critiques, il est recommandé de recourir à une traduction humaine professionnelle. Nous ne sommes pas responsables des malentendus ou des interprétations erronées résultant de l'utilisation de cette traduction.