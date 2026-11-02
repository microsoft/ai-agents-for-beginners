# 🤝 Systèmes d'atelier multi-agents d'entreprise (.NET)

## 📋 Objectifs d'apprentissage

Ce carnet montre comment construire des systèmes multi-agents sophistiqués de qualité entreprise en utilisant le Microsoft Agent Framework dans .NET avec Azure OpenAI (API Responses). Vous apprendrez à orchestrer plusieurs agents spécialisés travaillant ensemble via des workflows structurés, en tirant parti des fonctionnalités d'entreprise de .NET pour des solutions prêtes pour la production.

**Capacités multi-agents d'entreprise que vous allez construire :**
- 👥 **Collaboration des agents** : Coordination d'agents typée avec validation à la compilation
- 🔄 **Orchestration de workflows** : Définition déclarative de workflows avec les patterns async de .NET
- 🎭 **Spécialisation des rôles** : Personnalités d'agents fortement typées et domaines d'expertise
- 🏢 **Intégration entreprise** : Patterns prêts pour la production avec surveillance et gestion des erreurs

## ⚙️ Prérequis et configuration

**Environnement de développement :**
- SDK .NET 9.0 ou supérieur
- Visual Studio 2022 ou VS Code avec extension C#
- Abonnement Azure (pour agents persistants)

**Packages NuGet requis :**
```xml
<PackageReference Include="Microsoft.Extensions.AI.Abstractions" Version="10.*" />
<PackageReference Include="Azure.AI.Agents.Persistent" Version="1.2.0-beta.10" />
<PackageReference Include="Azure.Identity" Version="1.15.0" />
<PackageReference Include="System.Linq.Async" Version="6.0.3" />
<PackageReference Include="Microsoft.Extensions.AI" Version="10.*" />
<PackageReference Include="DotNetEnv" Version="3.1.1" />
<PackageReference Include="Microsoft.Extensions.AI.OpenAI" Version="10.*" />
<PackageReference Include="OpenTelemetry.Api" Version="1.*" />
<PackageReference Include="Microsoft.Agents.AI.Workflows" Version="1.*" />
<PackageReference Include="Microsoft.Agents.AI.OpenAI" Version="1.*-*" />
```

## Exemple de code

Le code complet fonctionnel pour cette leçon est disponible dans le fichier C# joint : [`08-dotnet-agent-framework.cs`](../../../../08-multi-agent/code_samples/08-dotnet-agent-framework.cs)

Pour exécuter l'exemple :

```bash
# Rendre le fichier exécutable (Linux/macOS)
chmod +x 08-dotnet-agent-framework.cs

# Exécuter l'exemple
./08-dotnet-agent-framework.cs
```

Ou en utilisant le CLI .NET :

```bash
dotnet run 08-dotnet-agent-framework.cs
```

## Ce que cet exemple démontre

Ce système de workflow multi-agents crée un service de recommandation de voyages hôteliers avec deux agents spécialisés :

1. **Agent FrontDesk** : un agent de voyage qui fournit des recommandations d'activités et de lieux
2. **Agent Concierge** : révise les recommandations pour garantir des expériences authentiques, non touristiques

Les agents travaillent ensemble dans un workflow où :
- L'agent FrontDesk reçoit la demande de voyage initiale
- L'agent Concierge révise et affine la recommandation
- Le workflow diffuse les réponses en temps réel

## Concepts clés

### Coordination des agents
L'exemple montre une coordination d'agents typée utilisant Microsoft Agent Framework avec validation à la compilation.

### Orchestration de workflows
Utilise une définition déclarative de workflow avec les patterns async de .NET pour connecter plusieurs agents en pipeline.

### Diffusion en continu des réponses
Implémente la diffusion en temps réel des réponses des agents en utilisant des énumérables async et une architecture événementielle.

### Intégration en entreprise
Montre des patterns prêts pour la production incluant :
- Configuration via variables d'environnement
- Gestion sécurisée des identifiants
- Gestion des erreurs
- Traitement asynchrone d'événements

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Avertissement** :
Ce document a été traduit à l'aide du service de traduction automatique [Co-op Translator](https://github.com/Azure/co-op-translator). Bien que nous nous efforçions d'assurer l'exactitude, veuillez noter que les traductions automatisées peuvent contenir des erreurs ou des inexactitudes. Le document original dans sa langue native doit être considéré comme la source faisant autorité. Pour les informations critiques, il est recommandé de recourir à une traduction professionnelle réalisée par un humain. Nous ne saurions être tenus responsables des malentendus ou erreurs d'interprétation découlant de l'utilisation de cette traduction.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->