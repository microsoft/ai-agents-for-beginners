# 🔍 RAG d'entreprise avec Microsoft Foundry (.NET)

## 📋 Objectifs d'apprentissage

Ce carnet montre comment construire des systèmes de génération augmentée par récupération (RAG) de qualité entreprise en utilisant le Microsoft Agent Framework en .NET avec Microsoft Foundry. Vous apprendrez à créer des agents prêts pour la production capables de rechercher dans des documents et de fournir des réponses précises, contextuelles, avec sécurité et scalabilité à l'échelle entreprise.

**Capacités RAG d'entreprise que vous allez développer :**
- 📚 **Intelligence Documentaire** : Traitement avancé des documents avec les services Azure AI
- 🔍 **Recherche Sémantique** : Recherche vectorielle haute performance avec fonctionnalités pour l'entreprise
- 🛡️ **Intégration de la Sécurité** : Contrôle d'accès basé sur les rôles et modèles de protection des données
- 🏢 **Architecture Scalables** : Systèmes RAG prêts pour la production avec surveillance

## 🎯 Architecture RAG d'entreprise

### Composants centraux d'entreprise
- **Microsoft Foundry** : Plateforme IA d’entreprise managée avec sécurité et conformité
- **Agents Persistants** : Agents à état avec historique de conversation et gestion du contexte
- **Gestion du Stockage Vectoriel** : Indexation et récupération des documents à l’échelle entreprise
- **Intégration d'Identité** : Authentification Azure AD et contrôle d’accès basé sur les rôles

### Avantages .NET pour l'entreprise
- **Sûreté de Type** : Validation à la compilation pour les opérations RAG et structures de données
- **Performance Asynchrone** : Traitement et recherche dans les documents sans blocage
- **Gestion de la Mémoire** : Utilisation efficace des ressources pour de grandes collections de documents
- **Modèles d’Intégration** : Intégration native des services Azure avec injection de dépendances

## 🏗️ Architecture technique

### Pipeline RAG d'entreprise
```
Document Upload → Security Validation → Vector Processing → Index Creation
                      ↓                    ↓                  ↓
User Query → Authentication → Semantic Search → Context Ranking → AI Response
```

### Composants centraux .NET
- **Azure.AI.Agents.Persistent** : Gestion des agents d’entreprise avec persistance d’état
- **Azure.Identity** : Authentification intégrée pour un accès sécurisé aux services Azure
- **Microsoft.Agents.AI.AzureAI** : Implémentation du framework agent optimisée pour Azure
- **System.Linq.Async** : Opérations LINQ asynchrones haute performance

## 🔧 Fonctionnalités et avantages d'entreprise

### Sécurité & conformité
- **Intégration Azure AD** : Gestion de l'identité d'entreprise et authentification
- **Contrôle d’Accès Basé sur les Rôles** : Permissions fines pour l’accès aux documents et opérations
- **Protection des Données** : Chiffrement au repos et en transit pour les documents sensibles
- **Journalisation d’Audit** : Suivi complet des activités pour exigences de conformité

### Performance & Scalabilité
- **Pooling de Connexions** : Gestion efficace des connexions aux services Azure
- **Traitement Asynchrone** : Opérations non-bloquantes pour scénarios à haut débit
- **Stratégies de Cache** : Mise en cache intelligente pour documents fréquemment consultés
- **Répartition de Charge** : Traitement distribué pour déploiements à grande échelle

### Gestion & Surveillance
- **Contrôles de Santé** : Surveillance intégrée des composants du système RAG
- **Métriques de Performance** : Analyses détaillées sur la qualité des recherches et temps de réponse
- **Gestion des Erreurs** : Gestion complète des exceptions avec stratégies de réessai
- **Gestion de la Configuration** : Paramètres spécifiques à l’environnement avec validation

## ⚙️ Prérequis & configuration

**Environnement de développement :**
- SDK .NET 9.0 ou version supérieure
- Visual Studio 2022 ou VS Code avec extension C#
- Abonnement Azure avec accès Microsoft Foundry

**Packages NuGet requis :**
```xml
<PackageReference Include="Microsoft.Extensions.AI" Version="9.9.0" />
<PackageReference Include="Azure.AI.Agents.Persistent" Version="1.2.0-beta.5" />
<PackageReference Include="Azure.Identity" Version="1.15.0" />
<PackageReference Include="System.Linq.Async" Version="6.0.3" />
<PackageReference Include="DotNetEnv" Version="3.1.1" />
```

**Configuration d’authentification Azure :**
```bash
# Installer Azure CLI et s'authentifier
az login
az account set --subscription "your-subscription-id"
```

**Configuration de l’environnement :**
* Configuration Microsoft Foundry (gérée automatiquement via Azure CLI)
* Assurez-vous d’être authentifié sur le bon abonnement Azure

## 📊 Modèles RAG d'entreprise

### Modèles de gestion documentaire
- **Chargement en masse** : Traitement efficace de grandes collections de documents
- **Mises à jour incrémentielles** : Ajout et modification de documents en temps réel
- **Contrôle de version** : Versionnage des documents et suivi des modifications
- **Gestion des Métadonnées** : Attributs riches et taxonomie des documents

### Modèles de recherche et récupération
- **Recherche Hybride** : Combinaison de recherche sémantique et par mots-clés pour résultats optimaux
- **Recherche Facettée** : Filtrage multidimensionnel et catégorisation
- **Affinage de la Pertinence** : Algorithmes de scoring personnalisés pour besoins spécifiques au domaine
- **Classement des Résultats** : Classement avancé avec intégration de logique métier

### Modèles de sécurité
- **Sécurité au niveau du document** : Contrôle d’accès précis par document
- **Classification des Données** : Étiquetage automatique de la sensibilité et protection
- **Pistes d’Audit** : Journalisation complète de toutes les opérations RAG
- **Protection de la Vie Privée** : Détection et anonymisation des informations personnelles (PII)

## 🔒 Fonctionnalités de sécurité d’entreprise

### Authentification & Autorisation
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
- **Chiffrement** : Chiffrement de bout en bout des documents et des index de recherche
- **Contrôles d’accès** : Intégration avec Azure AD pour permissions utilisateurs et groupes
- **Résidence des données** : Contrôles géographiques de localisation des données pour conformité
- **Sauvegarde & Récupération** : Capacités automatisées de sauvegarde et reprise après sinistre

## 📈 Optimisation de la performance

### Modèles de traitement asynchrone
```csharp
// Efficient async document processing
await foreach (var document in documentStream.AsAsyncEnumerable())
{
    await ProcessDocumentAsync(document, cancellationToken);
}
```

### Gestion de la mémoire
- **Traitement en streaming** : Gestion des gros documents sans problème de mémoire
- **Pooling de ressources** : Réutilisation efficace des ressources coûteuses
- **Collecte des déchets** : Modèles optimisés d’allocation mémoire
- **Gestion des connexions** : Cycle de vie adéquat des connexions aux services Azure

### Stratégies de cache
- **Mise en cache des requêtes** : Mise en cache des recherches fréquemment exécutées
- **Mise en cache documentaire** : Cache en mémoire pour documents chauds
- **Mise en cache des index** : Mise en cache optimisée des index vectoriels
- **Mise en cache des résultats** : Caching intelligent des réponses générées

## 📊 Cas d’utilisation d’entreprise

### Gestion des connaissances
- **Wiki d’entreprise** : Recherche intelligente à travers les bases de connaissances de l’entreprise
- **Politiques & Procédures** : Conformité automatisée et orientation des procédures
- **Matériel de formation** : Assistance intelligente en apprentissage et développement
- **Bases de données de recherche** : Systèmes d’analyse de publications académiques et de recherche

### Support client
- **Base de connaissances support** : Réponses automatisées du service client
- **Documentation produit** : Recherche intelligente d’informations produit
- **Guides de dépannage** : Assistance contextuelle à la résolution de problèmes
- **Systèmes FAQ** : Génération dynamique de FAQ à partir de collections documentaires

### Conformité réglementaire
- **Analyse de documents juridiques** : Intelligence des contrats et documents légaux
- **Surveillance de conformité** : Contrôle automatisé de la conformité réglementaire
- **Évaluation des risques** : Analyse et rapport des risques basés sur les documents
- **Support d’audit** : Découverte intelligente documentaire pour audits

## 🚀 Déploiement en production

### Surveillance & observabilité
- **Application Insights** : Télémétrie détaillée et surveillance des performances
- **Métriques personnalisées** : Suivi des KPI métier et alertes
- **Tracing distribué** : Suivi complet des requêtes à travers les services
- **Tableaux de bord de santé** : Visualisation en temps réel de la santé système et des performances

### Scalabilité & fiabilité
- **Mise à l’échelle automatique** : Adaptation automatique basée sur la charge et métriques de performance
- **Haute disponibilité** : Déploiement multi-régions avec capacités de bascule
- **Tests de charge** : Validation de performance sous conditions de charge d’entreprise
- **Reprise après sinistre** : Procédures automatisées de sauvegarde et de restauration

Prêt à construire des systèmes RAG d’entreprise capables de gérer des documents sensibles à grande échelle ? Architecturons ensemble des systèmes de connaissances intelligents pour l’entreprise ! 🏢📖✨

## Implémentation du code

Le code complet et fonctionnel de cette leçon est disponible dans `05-dotnet-agent-framework.cs`.

Pour exécuter l’exemple :

```bash
# Rendre le script exécutable (Linux/macOS)
chmod +x 05-dotnet-agent-framework.cs

# Exécuter l'application .NET fichier unique
./05-dotnet-agent-framework.cs
```

Ou utilisez `dotnet run` directement :

```bash
dotnet run 05-dotnet-agent-framework.cs
```

Le code démontre :

1. **Installation des packages** : Installation des packages NuGet requis pour Azure AI Agents
2. **Configuration de l’environnement** : Chargement des paramètres du point de terminaison Microsoft Foundry et modèle
3. **Chargement de documents** : Téléversement d’un document pour traitement RAG
4. **Création du stockage vectoriel** : Création d’un magasin vectoriel pour la recherche sémantique
5. **Configuration de l’agent** : Configuration d’un agent IA avec capacités de recherche fichier
6. **Exécution des requêtes** : Exécution de requêtes sur le document téléversé

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Avertissement** :
Ce document a été traduit à l'aide du service de traduction automatique [Co-op Translator](https://github.com/Azure/co-op-translator). Bien que nous nous efforçions d'assurer l'exactitude, veuillez noter que les traductions automatisées peuvent contenir des erreurs ou des inexactitudes. Le document original dans sa langue native doit être considéré comme la source faisant autorité. Pour les informations critiques, il est recommandé de recourir à une traduction professionnelle réalisée par un humain. Nous ne saurions être tenus responsables des malentendus ou erreurs d'interprétation découlant de l'utilisation de cette traduction.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->