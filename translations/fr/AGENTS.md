# AGENTS.md

## Aperçu du projet

Ce dépôt contient "Agents IA pour débutants" - un cours éducatif complet enseignant tout ce qu'il faut pour créer des agents IA. Le cours comprend plus de 15 leçons couvrant les fondamentaux, les modèles de conception, les frameworks et le déploiement en production des agents IA.

**Technologies clés :**
- Python 3.12+
- Jupyter Notebooks pour un apprentissage interactif
- Frameworks IA : Semantic Kernel, AutoGen, Microsoft Agent Framework (MAF)
- Services Azure AI : Azure AI Foundry, Azure AI Agent Service
- Marketplace de modèles GitHub (niveau gratuit disponible)

**Architecture :**
- Structure basée sur les leçons (répertoires 00-15+)
- Chaque leçon contient : documentation README, exemples de code (notebooks Jupyter) et images
- Support multilingue via un système de traduction automatisé
- Plusieurs options de frameworks par leçon (Semantic Kernel, AutoGen, Azure AI Agent Service)

## Commandes d'installation

### Prérequis
- Python 3.12 ou supérieur
- Compte GitHub (pour les modèles GitHub - niveau gratuit)
- Abonnement Azure (optionnel, pour les services Azure AI)

### Configuration initiale

1. **Cloner ou forker le dépôt :**
   ```bash
   gh repo fork microsoft/ai-agents-for-beginners --clone
   # OR
   git clone https://github.com/microsoft/ai-agents-for-beginners.git
   cd ai-agents-for-beginners
   ```

2. **Créer et activer un environnement virtuel Python :**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Installer les dépendances :**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configurer les variables d'environnement :**
   ```bash
   cp .env.example .env
   # Edit .env with your API keys and endpoints
   ```


### Variables d'environnement requises

Pour **Modèles GitHub (Gratuit)** :
- `GITHUB_TOKEN` - Jeton d'accès personnel de GitHub

Pour **Services Azure AI** (optionnel) :
- `PROJECT_ENDPOINT` - Point de terminaison du projet Azure AI Foundry
- `AZURE_OPENAI_API_KEY` - Clé API Azure OpenAI
- `AZURE_OPENAI_ENDPOINT` - URL du point de terminaison Azure OpenAI
- `AZURE_OPENAI_CHAT_DEPLOYMENT_NAME` - Nom du déploiement pour le modèle de chat
- `AZURE_OPENAI_EMBEDDING_DEPLOYMENT_NAME` - Nom du déploiement pour les embeddings
- Configuration Azure supplémentaire comme indiqué dans `.env.example`

## Flux de travail de développement

### Exécution des notebooks Jupyter

Chaque leçon contient plusieurs notebooks Jupyter pour différents frameworks :

1. **Démarrer Jupyter :**
   ```bash
   jupyter notebook
   ```

2. **Naviguer vers un répertoire de leçon** (par exemple, `01-intro-to-ai-agents/code_samples/`)

3. **Ouvrir et exécuter les notebooks :**
   - `*-semantic-kernel.ipynb` - Utilisation du framework Semantic Kernel
   - `*-autogen.ipynb` - Utilisation du framework AutoGen
   - `*-python-agent-framework.ipynb` - Utilisation du Microsoft Agent Framework (Python)
   - `*-dotnet-agent-framework.ipynb` - Utilisation du Microsoft Agent Framework (.NET)
   - `*-azureaiagent.ipynb` - Utilisation du service Azure AI Agent

### Travailler avec différents frameworks

**Semantic Kernel + Modèles GitHub :**
- Niveau gratuit disponible avec un compte GitHub
- Idéal pour l'apprentissage et l'expérimentation
- Modèle de fichier : `*-semantic-kernel*.ipynb`

**AutoGen + Modèles GitHub :**
- Niveau gratuit disponible avec un compte GitHub
- Capacités d'orchestration multi-agents
- Modèle de fichier : `*-autogen.ipynb`

**Microsoft Agent Framework (MAF) :**
- Dernier framework de Microsoft
- Disponible en Python et .NET
- Modèle de fichier : `*-agent-framework.ipynb`

**Service Azure AI Agent :**
- Nécessite un abonnement Azure
- Fonctionnalités prêtes pour la production
- Modèle de fichier : `*-azureaiagent.ipynb`

## Instructions de test

Ce dépôt est éducatif avec du code d'exemple plutôt que du code de production avec des tests automatisés. Pour vérifier votre configuration et vos modifications :

### Tests manuels

1. **Tester l'environnement Python :**
   ```bash
   python --version  # Should be 3.12+
   pip list | grep -E "(autogen|semantic-kernel|azure-ai)"
   ```

2. **Tester l'exécution des notebooks :**
   ```bash
   # Convert notebook to script and run (tests imports)
   jupyter nbconvert --to script <lesson-folder>/code_samples/<notebook>.ipynb --stdout | python
   ```

3. **Vérifier les variables d'environnement :**
   ```bash
   python -c "import os; from dotenv import load_dotenv; load_dotenv(); print('✓ GITHUB_TOKEN' if os.getenv('GITHUB_TOKEN') else '✗ GITHUB_TOKEN missing')"
   ```


### Exécution des notebooks individuels

Ouvrez les notebooks dans Jupyter et exécutez les cellules séquentiellement. Chaque notebook est autonome et inclut :
- Instructions d'importation
- Chargement de la configuration
- Implémentations d'agents d'exemple
- Résultats attendus dans les cellules markdown

## Style de code

### Conventions Python

- **Version Python** : 3.12+
- **Style de code** : Respecter les conventions standard PEP 8 de Python
- **Notebooks** : Utiliser des cellules markdown claires pour expliquer les concepts
- **Imports** : Regrouper par bibliothèque standard, tierce partie, imports locaux

### Conventions pour les notebooks Jupyter

- Inclure des cellules markdown descriptives avant les cellules de code
- Ajouter des exemples de sortie dans les notebooks pour référence
- Utiliser des noms de variables clairs correspondant aux concepts des leçons
- Maintenir un ordre d'exécution linéaire des notebooks (cellule 1 → 2 → 3...)

### Organisation des fichiers

```
<lesson-number>-<lesson-name>/
├── README.md                     # Lesson documentation
├── code_samples/
│   ├── <number>-semantic-kernel.ipynb
│   ├── <number>-autogen.ipynb
│   ├── <number>-python-agent-framework.ipynb
│   └── <number>-azureaiagent.ipynb
└── images/
    └── *.png
```


## Construction et déploiement

### Construction de la documentation

Ce dépôt utilise Markdown pour la documentation :
- Fichiers README.md dans chaque dossier de leçon
- README.md principal à la racine du dépôt
- Système de traduction automatisé via GitHub Actions

### Pipeline CI/CD

Situé dans `.github/workflows/` :

1. **co-op-translator.yml** - Traduction automatique en plus de 50 langues
2. **welcome-issue.yml** - Accueille les créateurs de nouveaux problèmes
3. **welcome-pr.yml** - Accueille les nouveaux contributeurs de pull requests

### Déploiement

Ce dépôt est éducatif - pas de processus de déploiement. Les utilisateurs :
1. Fork ou clone le dépôt
2. Exécutent les notebooks localement ou dans GitHub Codespaces
3. Apprennent en modifiant et en expérimentant les exemples

## Directives pour les pull requests

### Avant de soumettre

1. **Tester vos modifications :**
   - Exécuter complètement les notebooks concernés
   - Vérifier que toutes les cellules s'exécutent sans erreurs
   - Vérifier que les sorties sont appropriées

2. **Mises à jour de la documentation :**
   - Mettre à jour README.md si de nouveaux concepts sont ajoutés
   - Ajouter des commentaires dans les notebooks pour le code complexe
   - S'assurer que les cellules markdown expliquent l'objectif

3. **Modifications des fichiers :**
   - Éviter de commettre des fichiers `.env` (utiliser `.env.example`)
   - Ne pas commettre les répertoires `venv/` ou `__pycache__/`
   - Conserver les sorties des notebooks lorsqu'elles démontrent des concepts
   - Supprimer les fichiers temporaires et les notebooks de sauvegarde (`*-backup.ipynb`)

### Format des titres de PR

Utiliser des titres descriptifs :
- `[Lesson-XX] Ajouter un nouvel exemple pour <concept>`
- `[Fix] Corriger une faute de frappe dans le README de la leçon-XX`
- `[Update] Améliorer l'exemple de code dans la leçon-XX`
- `[Docs] Mettre à jour les instructions de configuration`

### Vérifications requises

- Les notebooks doivent s'exécuter sans erreurs
- Les fichiers README doivent être clairs et précis
- Respecter les modèles de code existants dans le dépôt
- Maintenir la cohérence avec les autres leçons

## Notes supplémentaires

### Points fréquents

1. **Incompatibilité de version Python :**
   - Assurez-vous d'utiliser Python 3.12+
   - Certains packages peuvent ne pas fonctionner avec des versions plus anciennes
   - Utilisez `python3 -m venv` pour spécifier explicitement la version de Python

2. **Variables d'environnement :**
   - Toujours créer `.env` à partir de `.env.example`
   - Ne pas commettre le fichier `.env` (il est dans `.gitignore`)
   - Le jeton GitHub nécessite des permissions appropriées

3. **Conflits de packages :**
   - Utiliser un environnement virtuel frais
   - Installer à partir de `requirements.txt` plutôt que des packages individuels
   - Certains notebooks peuvent nécessiter des packages supplémentaires mentionnés dans leurs cellules markdown

4. **Services Azure :**
   - Les services Azure AI nécessitent un abonnement actif
   - Certaines fonctionnalités sont spécifiques à la région
   - Les limitations du niveau gratuit s'appliquent aux modèles GitHub

### Parcours d'apprentissage

Progression recommandée à travers les leçons :
1. **00-course-setup** - Commencez ici pour la configuration de l'environnement
2. **01-intro-to-ai-agents** - Comprendre les fondamentaux des agents IA
3. **02-explore-agentic-frameworks** - Apprendre sur différents frameworks
4. **03-agentic-design-patterns** - Modèles de conception essentiels
5. Continuez à travers les leçons numérotées séquentiellement

### Sélection de framework

Choisissez le framework en fonction de vos objectifs :
- **Apprentissage/Prototypage** : Semantic Kernel + Modèles GitHub (gratuit)
- **Systèmes multi-agents** : AutoGen
- **Dernières fonctionnalités** : Microsoft Agent Framework (MAF)
- **Déploiement en production** : Service Azure AI Agent

### Obtenir de l'aide

- Rejoignez le [Discord de la communauté Azure AI Foundry](https://aka.ms/ai-agents/discord)
- Consultez les fichiers README des leçons pour des conseils spécifiques
- Vérifiez le [README.md principal](./README.md) pour un aperçu du cours
- Référez-vous à [Course Setup](./00-course-setup/README.md) pour des instructions détaillées de configuration

### Contribuer

Ce projet éducatif est ouvert. Contributions bienvenues :
- Améliorer les exemples de code
- Corriger les fautes de frappe ou erreurs
- Ajouter des commentaires clarifiants
- Suggérer de nouveaux sujets de leçon
- Traduire dans des langues supplémentaires

Consultez [GitHub Issues](https://github.com/microsoft/ai-agents-for-beginners/issues) pour les besoins actuels.

## Contexte spécifique au projet

### Support multilingue

Ce dépôt utilise un système de traduction automatisé :
- Plus de 50 langues prises en charge
- Traductions dans les répertoires `/translations/<lang-code>/`
- Le workflow GitHub Actions gère les mises à jour de traduction
- Les fichiers source sont en anglais à la racine du dépôt

### Structure des leçons

Chaque leçon suit un modèle cohérent :
1. Vignette vidéo avec lien
2. Contenu écrit de la leçon (README.md)
3. Exemples de code dans plusieurs frameworks
4. Objectifs d'apprentissage et prérequis
5. Ressources d'apprentissage supplémentaires liées

### Nommage des exemples de code

Format : `<lesson-number>-<framework-name>.ipynb`
- `04-semantic-kernel.ipynb` - Leçon 4, Semantic Kernel
- `07-autogen.ipynb` - Leçon 7, AutoGen
- `14-python-agent-framework.ipynb` - Leçon 14, MAF Python
- `14-dotnet-agent-framework.ipynb` - Leçon 14, MAF .NET

### Répertoires spéciaux

- `translated_images/` - Images localisées pour les traductions
- `images/` - Images originales pour le contenu en anglais
- `.devcontainer/` - Configuration du conteneur de développement VS Code
- `.github/` - Workflows et modèles GitHub Actions

### Dépendances

Packages clés de `requirements.txt` :
- `autogen-agentchat`, `autogen-core`, `autogen-ext` - Framework AutoGen
- `semantic-kernel` - Framework Semantic Kernel
- `agent-framework` - Microsoft Agent Framework
- `azure-ai-inference`, `azure-ai-projects` - Services Azure AI
- `azure-search-documents` - Intégration Azure AI Search
- `chromadb` - Base de données vectorielle pour les exemples RAG
- `chainlit` - Framework d'interface utilisateur de chat
- `browser_use` - Automatisation de navigateur pour les agents
- `mcp[cli]` - Support du protocole de contexte de modèle
- `mem0ai` - Gestion de la mémoire pour les agents

---

**Avertissement** :  
Ce document a été traduit à l'aide du service de traduction automatique [Co-op Translator](https://github.com/Azure/co-op-translator). Bien que nous nous efforcions d'assurer l'exactitude, veuillez noter que les traductions automatisées peuvent contenir des erreurs ou des inexactitudes. Le document original dans sa langue d'origine doit être considéré comme la source faisant autorité. Pour des informations critiques, il est recommandé de recourir à une traduction humaine professionnelle. Nous déclinons toute responsabilité en cas de malentendus ou d'interprétations erronées résultant de l'utilisation de cette traduction.