<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "c268705e6fb2b30c7690d5b2a002e072",
  "translation_date": "2025-11-07T08:55:38+00:00",
  "source_file": "05-agentic-rag/code_samples/05-dotnet-agent-framework.md",
  "language_code": "fr"
}
-->
# 🔍 RAG d'entreprise avec Azure AI Foundry (.NET)

## 📋 Objectifs d'apprentissage

Ce notebook montre comment construire des systèmes RAG (Retrieval-Augmented Generation) de niveau entreprise en utilisant le Microsoft Agent Framework en .NET avec Azure AI Foundry. Vous apprendrez à créer des agents prêts pour la production capables de rechercher dans des documents et de fournir des réponses précises et contextuelles avec une sécurité et une évolutivité adaptées aux entreprises.

**Fonctionnalités RAG d'entreprise que vous allez développer :**
- 📚 **Intelligence documentaire** : Traitement avancé des documents avec les services Azure AI
- 🔍 **Recherche sémantique** : Recherche vectorielle haute performance avec des fonctionnalités d'entreprise
- 🛡️ **Intégration de la sécurité** : Contrôle d'accès basé sur les rôles et modèles de protection des données
- 🏢 **Architecture évolutive** : Systèmes RAG prêts pour la production avec surveillance

## 🎯 Architecture RAG d'entreprise

### Composants principaux d'entreprise
- **Azure AI Foundry** : Plateforme AI d'entreprise gérée avec sécurité et conformité
- **Agents persistants** : Agents avec historique de conversation et gestion du contexte
- **Gestion des magasins vectoriels** : Indexation et récupération de documents de niveau entreprise
- **Intégration d'identité** : Authentification Azure AD et contrôle d'accès basé sur les rôles

### Avantages de .NET pour l'entreprise
- **Sécurité des types** : Validation au moment de la compilation pour les opérations RAG et les structures de données
- **Performance asynchrone** : Traitement des documents et opérations de recherche non bloquants
- **Gestion de la mémoire** : Utilisation efficace des ressources pour les grandes collections de documents
- **Modèles d'intégration** : Intégration native des services Azure avec injection de dépendances

## 🏗️ Architecture technique

### Pipeline RAG d'entreprise
```
Document Upload → Security Validation → Vector Processing → Index Creation
                      ↓                    ↓                  ↓
User Query → Authentication → Semantic Search → Context Ranking → AI Response
```

### Composants principaux .NET
- **Azure.AI.Agents.Persistent** : Gestion des agents d'entreprise avec persistance de l'état
- **Azure.Identity** : Authentification intégrée pour un accès sécurisé aux services Azure
- **Microsoft.Agents.AI.AzureAI** : Implémentation du framework d'agents optimisé pour Azure
- **System.Linq.Async** : Opérations LINQ asynchrones haute performance

## 🔧 Fonctionnalités et avantages d'entreprise

### Sécurité et conformité
- **Intégration Azure AD** : Gestion des identités et authentification d'entreprise
- **Accès basé sur les rôles** : Permissions granulaires pour l'accès aux documents et aux opérations
- **Protection des données** : Cryptage au repos et en transit pour les documents sensibles
- **Journalisation des audits** : Suivi complet des activités pour les exigences de conformité

### Performance et évolutivité
- **Pooling de connexions** : Gestion efficace des connexions aux services Azure
- **Traitement asynchrone** : Opérations non bloquantes pour des scénarios à haut débit
- **Stratégies de mise en cache** : Mise en cache intelligente pour les documents fréquemment consultés
- **Répartition de charge** : Traitement distribué pour les déploiements à grande échelle

### Gestion et surveillance
- **Vérifications de santé** : Surveillance intégrée des composants du système RAG
- **Métriques de performance** : Analyses détaillées sur la qualité de recherche et les temps de réponse
- **Gestion des erreurs** : Gestion complète des exceptions avec des politiques de reprise
- **Gestion de la configuration** : Paramètres spécifiques à l'environnement avec validation

## ⚙️ Prérequis et configuration

**Environnement de développement :**
- SDK .NET 9.0 ou supérieur
- Visual Studio 2022 ou VS Code avec extension C#
- Abonnement Azure avec accès à AI Foundry

**Packages NuGet requis :**
```xml
<PackageReference Include="Microsoft.Extensions.AI" Version="9.9.0" />
<PackageReference Include="Azure.AI.Agents.Persistent" Version="1.2.0-beta.5" />
<PackageReference Include="Azure.Identity" Version="1.15.0" />
<PackageReference Include="System.Linq.Async" Version="6.0.3" />
<PackageReference Include="DotNetEnv" Version="3.1.1" />
```

**Configuration d'authentification Azure :**
```bash
# Install Azure CLI and authenticate
az login
az account set --subscription "your-subscription-id"
```

**Configuration de l'environnement :**
* Configuration Azure AI Foundry (gérée automatiquement via Azure CLI)
* Assurez-vous d'être authentifié sur le bon abonnement Azure

## 📊 Modèles RAG d'entreprise

### Modèles de gestion des documents
- **Téléchargement en masse** : Traitement efficace de grandes collections de documents
- **Mises à jour incrémentielles** : Ajout et modification de documents en temps réel
- **Contrôle de version** : Versionnement des documents et suivi des modifications
- **Gestion des métadonnées** : Attributs riches et taxonomie des documents

### Modèles de recherche et de récupération
- **Recherche hybride** : Combinaison de recherche sémantique et par mots-clés pour des résultats optimaux
- **Recherche facettée** : Filtrage multidimensionnel et catégorisation
- **Ajustement de pertinence** : Algorithmes de scoring personnalisés pour des besoins spécifiques au domaine
- **Classement des résultats** : Classement avancé avec intégration de logique métier

### Modèles de sécurité
- **Sécurité au niveau des documents** : Contrôle d'accès granulaire par document
- **Classification des données** : Étiquetage automatique de sensibilité et protection
- **Trails d'audit** : Journalisation complète de toutes les opérations RAG
- **Protection de la vie privée** : Détection et masquage des informations personnelles identifiables (PII)

## 🔒 Fonctionnalités de sécurité d'entreprise

### Authentification et autorisation
```csharp
// Azure AD integrated authentication
var credential = new AzureCliCredential();
var agentsClient = new PersistentAgentsClient(endpoint, credential);

// Role-based access validation
if (!await ValidateUserPermissions(user, documentId))
{
    throw new UnauthorizedAccessException("Insufficient permissions");
}
```

### Protection des données
- **Cryptage** : Cryptage de bout en bout pour les documents et les indices de recherche
- **Contrôles d'accès** : Intégration avec Azure AD pour les permissions utilisateur et groupe
- **Résidence des données** : Contrôles de localisation géographique des données pour la conformité
- **Sauvegarde et récupération** : Sauvegarde automatisée et capacités de récupération en cas de sinistre

## 📈 Optimisation des performances

### Modèles de traitement asynchrone
```csharp
// Efficient async document processing
await foreach (var document in documentStream.AsAsyncEnumerable())
{
    await ProcessDocumentAsync(document, cancellationToken);
}
```

### Gestion de la mémoire
- **Traitement en streaming** : Gestion des grands documents sans problèmes de mémoire
- **Pooling de ressources** : Réutilisation efficace des ressources coûteuses
- **Collecte des déchets** : Modèles d'allocation de mémoire optimisés
- **Gestion des connexions** : Cycle de vie approprié des connexions aux services Azure

### Stratégies de mise en cache
- **Mise en cache des requêtes** : Mise en cache des recherches fréquemment exécutées
- **Mise en cache des documents** : Mise en cache en mémoire pour les documents populaires
- **Mise en cache des indices** : Optimisation de la mise en cache des indices vectoriels
- **Mise en cache des résultats** : Mise en cache intelligente des réponses générées

## 📊 Cas d'utilisation d'entreprise

### Gestion des connaissances
- **Wiki d'entreprise** : Recherche intelligente dans les bases de connaissances de l'entreprise
- **Politiques et procédures** : Orientation automatisée sur la conformité et les procédures
- **Matériaux de formation** : Assistance intelligente pour l'apprentissage et le développement
- **Bases de données de recherche** : Systèmes d'analyse de documents académiques et de recherche

### Support client
- **Base de connaissances de support** : Réponses automatisées au service client
- **Documentation produit** : Recherche intelligente d'informations sur les produits
- **Guides de dépannage** : Assistance contextuelle pour résoudre les problèmes
- **Systèmes FAQ** : Génération dynamique de FAQ à partir de collections de documents

### Conformité réglementaire
- **Analyse de documents juridiques** : Intelligence sur les contrats et documents juridiques
- **Surveillance de la conformité** : Vérification automatisée de la conformité réglementaire
- **Évaluation des risques** : Analyse et reporting des risques basés sur les documents
- **Support d'audit** : Découverte intelligente de documents pour les audits

## 🚀 Déploiement en production

### Surveillance et observabilité
- **Application Insights** : Télémetrie détaillée et surveillance des performances
- **Métriques personnalisées** : Suivi et alertes des indicateurs clés de performance spécifiques à l'entreprise
- **Traçage distribué** : Suivi de bout en bout des requêtes à travers les services
- **Tableaux de bord de santé** : Visualisation en temps réel de la santé et des performances du système

### Évolutivité et fiabilité
- **Auto-scaling** : Mise à l'échelle automatique basée sur la charge et les métriques de performance
- **Haute disponibilité** : Déploiement multi-régions avec capacités de basculement
- **Tests de charge** : Validation des performances sous des conditions de charge d'entreprise
- **Récupération en cas de sinistre** : Procédures automatisées de sauvegarde et de récupération

Prêt à construire des systèmes RAG de niveau entreprise capables de gérer des documents sensibles à grande échelle ? Architecturons des systèmes de connaissances intelligents pour l'entreprise ! 🏢📖✨

## Implémentation du code

L'exemple de code complet pour cette leçon est disponible dans `05-dotnet-agent-framework.cs`. 

Pour exécuter l'exemple :

```bash
# Make the script executable (Linux/macOS)
chmod +x 05-dotnet-agent-framework.cs

# Run the .NET Single File App
./05-dotnet-agent-framework.cs
```

Ou utilisez directement `dotnet run` :

```bash
dotnet run 05-dotnet-agent-framework.cs
```

Le code démontre :

1. **Installation des packages** : Installation des packages NuGet requis pour les agents Azure AI
2. **Configuration de l'environnement** : Chargement des paramètres de point de terminaison et de modèle Azure AI Foundry
3. **Téléchargement de documents** : Téléchargement d'un document pour le traitement RAG
4. **Création de magasin vectoriel** : Création d'un magasin vectoriel pour la recherche sémantique
5. **Configuration de l'agent** : Configuration d'un agent AI avec des capacités de recherche de fichiers
6. **Exécution de requêtes** : Exécution de requêtes sur le document téléchargé

---

**Avertissement** :  
Ce document a été traduit à l'aide du service de traduction automatique [Co-op Translator](https://github.com/Azure/co-op-translator). Bien que nous nous efforcions d'assurer l'exactitude, veuillez noter que les traductions automatisées peuvent contenir des erreurs ou des inexactitudes. Le document original dans sa langue d'origine doit être considéré comme la source faisant autorité. Pour des informations critiques, il est recommandé de recourir à une traduction humaine professionnelle. Nous ne sommes pas responsables des malentendus ou des interprétations erronées résultant de l'utilisation de cette traduction.