<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f82a3992438bcc028a2569c5fed828a9",
  "translation_date": "2025-11-07T09:20:31+00:00",
  "source_file": "04-tool-use/code_samples/04-dotnet-agent-framework.md",
  "language_code": "fr"
}
-->
# 🛠️ Utilisation avancée des outils avec les modèles GitHub (.NET)

## 📋 Objectifs d'apprentissage

Ce notebook illustre les modèles d'intégration d'outils de niveau entreprise en utilisant le Microsoft Agent Framework en .NET avec les modèles GitHub. Vous apprendrez à construire des agents sophistiqués avec plusieurs outils spécialisés, en tirant parti du typage fort de C# et des fonctionnalités d'entreprise de .NET.

**Compétences avancées en outils que vous maîtriserez :**
- 🔧 **Architecture multi-outils** : Construire des agents avec plusieurs capacités spécialisées
- 🎯 **Exécution d'outils type-safe** : Exploiter la validation au moment de la compilation de C#
- 📊 **Modèles d'outils d'entreprise** : Conception d'outils prêts pour la production et gestion des erreurs
- 🔗 **Composition d'outils** : Combiner des outils pour des workflows métier complexes

## 🎯 Avantages de l'architecture d'outils .NET

### Fonctionnalités d'outils d'entreprise
- **Validation au moment de la compilation** : Le typage fort garantit la correction des paramètres des outils
- **Injection de dépendances** : Intégration du conteneur IoC pour la gestion des outils
- **Modèles Async/Await** : Exécution non bloquante des outils avec une gestion appropriée des ressources
- **Journalisation structurée** : Intégration de la journalisation pour le suivi de l'exécution des outils

### Modèles prêts pour la production
- **Gestion des exceptions** : Gestion complète des erreurs avec des exceptions typées
- **Gestion des ressources** : Modèles de disposition appropriés et gestion de la mémoire
- **Surveillance des performances** : Métriques intégrées et compteurs de performance
- **Gestion de la configuration** : Configuration type-safe avec validation

## 🔧 Architecture technique

### Composants principaux des outils .NET
- **Microsoft.Extensions.AI** : Couche d'abstraction unifiée pour les outils
- **Microsoft.Agents.AI** : Orchestration d'outils de niveau entreprise
- **Intégration des modèles GitHub** : Client API haute performance avec gestion des connexions

### Pipeline d'exécution des outils
```
User Request → Agent Analysis → Tool Selection → Type Validation
                 ↓               ↓              ↓
         Parameter Binding → Tool Execution → Result Processing → Response
```

## 🛠️ Catégories et modèles d'outils

### 1. **Outils de traitement des données**
- **Validation des entrées** : Typage fort avec annotations de données
- **Opérations de transformation** : Conversion et formatage des données type-safe
- **Logique métier** : Outils de calcul et d'analyse spécifiques au domaine
- **Formatage des sorties** : Génération de réponses structurées

### 2. **Outils d'intégration**
- **Connecteurs API** : Intégration de services RESTful avec HttpClient
- **Outils de base de données** : Intégration d'Entity Framework pour l'accès aux données
- **Opérations sur fichiers** : Opérations sécurisées sur le système de fichiers avec validation
- **Services externes** : Modèles d'intégration de services tiers

### 3. **Outils utilitaires**
- **Traitement de texte** : Utilitaires de manipulation et de formatage de chaînes
- **Opérations sur les dates/heures** : Calculs de dates/heures tenant compte des cultures
- **Outils mathématiques** : Calculs précis et opérations statistiques
- **Outils de validation** : Validation des règles métier et vérification des données

## ⚙️ Prérequis et configuration

**Environnement de développement :**
- SDK .NET 9.0 ou supérieur
- Visual Studio 2022 ou VS Code avec extension C#
- Accès à l'API des modèles GitHub

**Packages NuGet requis :**
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

Prêt à construire des agents de niveau entreprise avec des capacités d'outils puissants et type-safe en .NET ? Architecturons des solutions professionnelles ! 🏢⚡

## 💻 Implémentation du code

L'implémentation complète en C# est disponible dans le fichier compagnon `04-dotnet-agent-framework.cs`. Cette application .NET Single File démontre :

- Chargement des variables d'environnement pour la configuration des modèles GitHub
- Définition d'outils personnalisés en utilisant des méthodes C# avec des attributs
- Création d'un agent IA avec intégration d'outils
- Gestion des fils de conversation
- Exécution des requêtes de l'agent avec invocation des outils

Pour exécuter l'exemple :

```bash
chmod +x 04-dotnet-agent-framework.cs
./04-dotnet-agent-framework.cs
```

Ou en utilisant le CLI .NET :

```bash
dotnet run 04-dotnet-agent-framework.cs
```

---

**Avertissement** :  
Ce document a été traduit à l'aide du service de traduction automatique [Co-op Translator](https://github.com/Azure/co-op-translator). Bien que nous nous efforcions d'assurer l'exactitude, veuillez noter que les traductions automatisées peuvent contenir des erreurs ou des inexactitudes. Le document original dans sa langue d'origine doit être considéré comme la source faisant autorité. Pour des informations critiques, il est recommandé de recourir à une traduction humaine professionnelle. Nous ne sommes pas responsables des malentendus ou des interprétations erronées résultant de l'utilisation de cette traduction.