# AGENTS.md

## Présentation du projet

This repository contains "AI Agents for Beginners" - a comprehensive educational course teaching everything needed to build AI Agents. The course consists of 15+ lessons covering fundamentals, design patterns, frameworks, and production deployment of AI agents.

**Technologies clés:**
- Python 3.12+
- Jupyter Notebooks pour l'apprentissage interactif
- Frameworks d'IA : Microsoft Agent Framework (MAF)
- Services Azure AI : Microsoft Foundry, Azure AI Foundry Agent Service V2

**Architecture:**
- Structure par leçons (répertoires 00-15+)
- Chaque leçon contient : documentation README, exemples de code (Jupyter notebooks) et images
- Support multilingue via un système de traduction automatisé
- Un notebook Python par leçon utilisant Microsoft Agent Framework

## Commandes d'installation

### Prérequis
- Python 3.12 ou supérieur
- Abonnement Azure (pour Azure AI Foundry)
- Azure CLI installé et authentifié (`az login`)

### Configuration initiale

1. **Cloner ou forker le dépôt:**
   ```bash
   gh repo fork microsoft/ai-agents-for-beginners --clone
   # OU
   git clone https://github.com/microsoft/ai-agents-for-beginners.git
   cd ai-agents-for-beginners
   ```

2. **Créer et activer l'environnement virtuel Python:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # Sur Windows : venv\Scripts\activate
   ```

3. **Installer les dépendances:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configurer les variables d'environnement:**
   ```bash
   cp .env.example .env
   # Modifiez le fichier .env avec vos clés d'API et vos points de terminaison.
   ```

### Variables d'environnement requises

Pour **Azure AI Foundry** (Requis):
- `AZURE_AI_PROJECT_ENDPOINT` - point de terminaison du projet Azure AI Foundry
- `AZURE_AI_MODEL_DEPLOYMENT_NAME` - nom du déploiement du modèle (par exemple, gpt-4o)

Pour **Azure AI Search** (Leçon 05 - RAG):
- `AZURE_SEARCH_SERVICE_ENDPOINT` - point de terminaison Azure AI Search
- `AZURE_SEARCH_API_KEY` - clé API Azure AI Search

Authentification : Exécutez `az login` avant d'exécuter les notebooks (utilise `AzureCliCredential`).

## Flux de développement

### Exécution des Jupyter Notebooks

Chaque leçon contient plusieurs Jupyter notebooks pour différents frameworks :

1. **Démarrer Jupyter:**
   ```bash
   jupyter notebook
   ```

2. **Naviguez vers un répertoire de leçon** (par ex., `01-intro-to-ai-agents/code_samples/`)

3. **Ouvrir et exécuter les notebooks:**
   - `*-python-agent-framework.ipynb` - Utilisation de Microsoft Agent Framework (Python)
   - `*-dotnet-agent-framework.ipynb` - Utilisation de Microsoft Agent Framework (.NET)

### Travailler avec Microsoft Agent Framework

**Microsoft Agent Framework + Azure AI Foundry:**
- Nécessite un abonnement Azure
- Utilise `AzureAIProjectAgentProvider` pour Agent Service V2 (agents visibles dans le portail Foundry)
- Prêt pour la production avec observabilité intégrée
- Modèle de fichier : `*-python-agent-framework.ipynb`

## Instructions de test

Il s'agit d'un dépôt éducatif avec du code d'exemple plutôt que du code de production disposant de tests automatisés. Pour vérifier votre configuration et vos modifications :

### Tests manuels

1. **Tester l'environnement Python:**
   ```bash
   python --version  # Devrait être 3.12 ou supérieur
   pip list | grep -E "(agent-framework|azure-ai|azure-identity)"
   ```

2. **Tester l'exécution du notebook:**
   ```bash
   # Convertir le notebook en script et l'exécuter (tester les imports)
   jupyter nbconvert --to script <lesson-folder>/code_samples/<notebook>.ipynb --stdout | python
   ```

3. **Vérifier les variables d'environnement:**
   ```bash
   python -c "import os; from dotenv import load_dotenv; load_dotenv(); print('✓ GITHUB_TOKEN' if os.getenv('GITHUB_TOKEN') else '✗ GITHUB_TOKEN missing')"
   ```

### Exécution de notebooks individuels

Ouvrez les notebooks dans Jupyter et exécutez les cellules séquentiellement. Chaque notebook est autonome et inclut :
- Instructions d'importation
- Chargement de la configuration
- Exemples d'implémentations d'agents
- Résultats attendus dans les cellules markdown

## Style de code

### Conventions Python

- **Version Python** : 3.12+
- **Style de code** : Suivre les conventions PEP 8 de Python
- **Notebooks** : Utiliser des cellules markdown claires pour expliquer les concepts
- **Imports** : Regrouper par bibliothèque standard, bibliothèques tierces, imports locaux

### Conventions pour les Jupyter Notebooks

- Inclure des cellules markdown descriptives avant les cellules de code
- Ajouter des exemples de sortie dans les notebooks à titre de référence
- Utiliser des noms de variables clairs correspondant aux concepts de la leçon
- Garder l'ordre d'exécution des notebooks linéaire (cellule 1 → 2 → 3...)

### Organisation des fichiers

```
<lesson-number>-<lesson-name>/
├── README.md                     # Lesson documentation
├── code_samples/
│   ├── <number>-python-agent-framework.ipynb
│   └── <number>-dotnet-agent-framework.ipynb  (optional)
└── images/
    └── *.png
```

## Construction et déploiement

### Génération de la documentation

Ce dépôt utilise Markdown pour la documentation :
- Fichiers README.md dans chaque dossier de leçon
- README.md principal à la racine du dépôt
- Système de traduction automatisé via GitHub Actions

### Pipeline CI/CD

Situé dans `.github/workflows/` :

1. **co-op-translator.yml** - Traduction automatique vers 50+ langues
2. **welcome-issue.yml** - Accueille les auteurs de nouvelles issues
3. **welcome-pr.yml** - Accueille les contributeurs de nouvelles pull requests

### Déploiement

Il s'agit d'un dépôt éducatif - pas de processus de déploiement. Les utilisateurs :
1. Forkez ou clonez le dépôt
2. Exécutez les notebooks localement ou dans GitHub Codespaces
3. Apprenez en modifiant et en expérimentant les exemples

## Directives pour les pull requests

### Avant de soumettre

1. **Testez vos modifications:**
   - Exécutez complètement les notebooks affectés
   - Vérifiez que toutes les cellules s'exécutent sans erreurs
   - Vérifiez que les sorties sont appropriées

2. **Mises à jour de la documentation:**
   - Mettez à jour README.md si vous ajoutez de nouveaux concepts
   - Ajoutez des commentaires dans les notebooks pour le code complexe
   - Assurez-vous que les cellules markdown expliquent l'objectif

3. **Modifications de fichiers:**
   - Évitez de committer des fichiers `.env` (utilisez `.env.example`)
   - Ne commettez pas les répertoires `venv/` ou `__pycache__/`
   - Conservez les sorties des notebooks lorsqu'elles illustrent des concepts
   - Supprimez les fichiers temporaires et les notebooks de sauvegarde (`*-backup.ipynb`)

### Format du titre de la PR

Utilisez des titres descriptifs :
- `[Lesson-XX] Ajouter un nouvel exemple pour <concept>`
- `[Fix] Corriger une faute de frappe dans le README de la leçon-XX`
- `[Update] Améliorer l'exemple de code dans la leçon-XX`
- `[Docs] Mettre à jour les instructions d'installation`

### Vérifications requises

- Les notebooks doivent s'exécuter sans erreurs
- Les fichiers README doivent être clairs et précis
- Suivre les modèles de code existants dans le dépôt
- Maintenir la cohérence avec les autres leçons

## Remarques supplémentaires

### Pièges courants

1. **Incompatibilité de version Python :**
   - Assurez-vous d'utiliser Python 3.12+
   - Certains paquets peuvent ne pas fonctionner avec des versions plus anciennes
   - Utilisez `python3 -m venv` pour spécifier explicitement la version de Python

2. **Variables d'environnement :**
   - Créez toujours `.env` à partir de `.env.example`
   - Ne commettez pas le fichier `.env` (il est dans `.gitignore`)
   - Le token GitHub nécessite les permissions appropriées

3. **Conflits de paquets :**
   - Utilisez un environnement virtuel propre
   - Installez depuis `requirements.txt` plutôt que des paquets individuels
   - Certains notebooks peuvent nécessiter des paquets supplémentaires mentionnés dans leurs cellules markdown

4. **Services Azure :**
   - Les services Azure AI requièrent un abonnement actif
   - Certaines fonctionnalités sont spécifiques à une région
   - Des limitations de niveau gratuit s'appliquent aux GitHub Models

### Parcours d'apprentissage

Progression recommandée à travers les leçons :
1. **00-course-setup** - Commencez ici pour la configuration de l'environnement
2. **01-intro-to-ai-agents** - Comprendre les fondamentaux des agents IA
3. **02-explore-agentic-frameworks** - Découvrir les différents frameworks
4. **03-agentic-design-patterns** - Principaux design patterns
5. Poursuivez ensuite les leçons numérotées dans l'ordre

### Choix du framework

Choisissez le framework en fonction de vos objectifs :
- **Toutes les leçons** : Microsoft Agent Framework (MAF) avec `AzureAIProjectAgentProvider`
- **Les agents s'enregistrent côté serveur** dans Azure AI Foundry Agent Service V2 et sont visibles dans le portail Foundry

### Obtenir de l'aide

- Rejoignez la [Communauté Microsoft Foundry sur Discord](https://aka.ms/ai-agents/discord)
- Consultez les fichiers README des leçons pour des instructions spécifiques
- Consultez le [README.md](./README.md) principal pour l'aperçu du cours
- Reportez-vous à [Configuration du cours](./00-course-setup/README.md) pour des instructions détaillées de configuration

### Contribution

Il s'agit d'un projet éducatif ouvert. Contributions bienvenues :
- Améliorer les exemples de code
- Corriger les fautes ou erreurs
- Ajouter des commentaires clarificateurs
- Suggérer de nouveaux sujets de leçon
- Traduire vers des langues supplémentaires

Consultez les [GitHub Issues](https://github.com/microsoft/ai-agents-for-beginners/issues) pour les besoins actuels.

## Contexte spécifique au projet

### Support multilingue

Ce dépôt utilise un système de traduction automatisé :
- Prise en charge de 50+ langues
- Traductions dans les répertoires `/translations/<lang-code>/`
- Le workflow GitHub Actions gère les mises à jour des traductions
- Les fichiers source sont en anglais à la racine du dépôt

### Structure des leçons

Chaque leçon suit un schéma cohérent :
1. Miniature vidéo avec lien
2. Contenu écrit de la leçon (README.md)
3. Exemples de code dans plusieurs frameworks
4. Objectifs d'apprentissage et prérequis
5. Ressources d'apprentissage supplémentaires liées

### Nommage des exemples de code

Format : `<lesson-number>-python-agent-framework.ipynb`
- `01-python-agent-framework.ipynb` - Leçon 1, MAF Python
- `14-sequential.ipynb` - Leçon 14, motifs avancés MAF

### Répertoires spéciaux

- `translated_images/` - Images localisées pour les traductions
- `images/` - Images originales pour le contenu en anglais
- `.devcontainer/` - Configuration du conteneur de développement VS Code
- `.github/` - Workflows et templates GitHub Actions

### Dépendances

Principaux paquets dans `requirements.txt` :
- `agent-framework` - Microsoft Agent Framework
- `a2a-sdk` - Support du protocole Agent-à-Agent
- `azure-ai-inference`, `azure-ai-projects` - Services Azure AI
- `azure-identity` - Authentification Azure (AzureCliCredential)
- `azure-search-documents` - Intégration Azure AI Search
- `mcp[cli]` - Support du Model Context Protocol

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
Avis de non-responsabilité :
Ce document a été traduit à l'aide du service de traduction par IA [Co-op Translator](https://github.com/Azure/co-op-translator). Bien que nous nous efforcions d'assurer l'exactitude, veuillez noter que les traductions automatiques peuvent comporter des erreurs ou des inexactitudes. Le document original, dans sa langue d'origine, doit être considéré comme la source faisant autorité. Pour les informations critiques, il est recommandé de recourir à une traduction professionnelle réalisée par un traducteur humain. Nous déclinons toute responsabilité en cas de malentendus ou d'interprétations erronées résultant de l'utilisation de cette traduction.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->