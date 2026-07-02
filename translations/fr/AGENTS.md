# AGENTS.md

## Aperçu du projet

Ce dépôt contient "Agents IA pour Débutants" - un cours éducatif complet enseignant tout ce qu'il faut pour construire des agents IA. Le cours se compose de 18 leçons couvrant les fondamentaux, les modèles de conception, les frameworks et le déploiement en production des agents IA.

**Technologies clés :**
- Python 3.12+
- Jupyter Notebooks pour un apprentissage interactif
- Frameworks IA : Microsoft Agent Framework (MAF)
- Services Azure AI : Microsoft Foundry, Azure AI Foundry Agent Service V2

**Architecture :**
- Structure basée sur les leçons (répertoires 00-15+)
- Chaque leçon contient : documentation README, exemples de code (Jupyter notebooks), et images
- Support multilingue via un système de traduction automatisé
- Un notebook Python par leçon utilisant Microsoft Agent Framework

## Commandes d'installation

### Prérequis
- Python 3.12 ou supérieur
- Abonnement Azure (pour Azure AI Foundry)
- Azure CLI installé et authentifié (`az login`)

### Configuration initiale

1. **Cloner ou forker le dépôt :**
   ```bash
   gh repo fork microsoft/ai-agents-for-beginners --clone
   # OU
   git clone https://github.com/microsoft/ai-agents-for-beginners.git
   cd ai-agents-for-beginners
   ```

2. **Créer et activer un environnement virtuel Python :**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # Sous Windows : venv\Scripts\activate
   ```

3. **Installer les dépendances :**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configurer les variables d'environnement :**
   ```bash
   cp .env.example .env
   # Modifiez le fichier .env avec vos clés API et points de terminaison
   ```

### Variables d'environnement requises

Pour **Azure AI Foundry** (Requis) :
- `AZURE_AI_PROJECT_ENDPOINT` - point de terminaison du projet Azure AI Foundry
- `AZURE_AI_MODEL_DEPLOYMENT_NAME` - nom du déploiement du modèle (ex. : gpt-4o)

Pour **Azure AI Search** (Leçon 05 - RAG) :
- `AZURE_SEARCH_SERVICE_ENDPOINT` - point de terminaison Azure AI Search
- `AZURE_SEARCH_API_KEY` - clé API Azure AI Search

Authentification : Exécutez `az login` avant d'exécuter les notebooks (utilise `AzureCliCredential`).

## Workflow de développement

### Exécution des Jupyter Notebooks

Chaque leçon contient plusieurs notebooks Jupyter pour différents frameworks :

1. **Démarrer Jupyter :**
   ```bash
   jupyter notebook
   ```

2. **Naviguer vers un répertoire de leçon** (ex. `01-intro-to-ai-agents/code_samples/`)

3. **Ouvrir et exécuter les notebooks :**
   - `*-python-agent-framework.ipynb` - Utilisation du Microsoft Agent Framework (Python)
   - `*-dotnet-agent-framework.ipynb` - Utilisation du Microsoft Agent Framework (.NET)

### Travail avec Microsoft Agent Framework

**Microsoft Agent Framework + Azure AI Foundry :**
- Nécessite un abonnement Azure
- Utilise `AzureAIProjectAgentProvider` pour l'Agent Service V2 (agents visibles dans le portail Foundry)
- Prêt pour la production avec observabilité intégrée
- Modèle de fichier : `*-python-agent-framework.ipynb`

## Instructions de test

Ce dépôt est éducatif avec des exemples de code plutôt que du code de production avec tests automatisés. Pour vérifier votre configuration et vos modifications :

### Tests manuels

1. **Tester l'environnement Python :**
   ```bash
   python --version  # Devrait être 3.12+
   pip list | grep -E "(agent-framework|azure-ai|azure-identity)"
   ```

2. **Tester l'exécution des notebooks :**
   ```bash
   # Convertir le carnet en script et exécuter (teste les imports)
   jupyter nbconvert --to script <lesson-folder>/code_samples/<notebook>.ipynb --stdout | python
   ```

3. **Vérifier les variables d'environnement :**
   ```bash
   python -c "import os; from dotenv import load_dotenv; load_dotenv(); print('✓ GITHUB_TOKEN' if os.getenv('GITHUB_TOKEN') else '✗ GITHUB_TOKEN missing')"
   ```

### Exécution des notebooks individuels

Ouvrez les notebooks dans Jupyter et exécutez les cellules séquentiellement. Chaque notebook est autonome et inclut :
- Instructions d'import
- Chargement de configurations
- Implémentations exemples d'agents
- Résultats attendus dans les cellules markdown

## Style de code

### Conventions Python

- **Version Python** : 3.12+
- **Style de code** : suivre les conventions PEP 8 de Python
- **Notebooks** : utiliser des cellules markdown claires pour expliquer les concepts
- **Imports** : grouper la librairie standard, tierces parties, imports locaux

### Conventions pour Jupyter Notebook

- Inclure des cellules markdown descriptives avant les cellules de code
- Ajouter des exemples de sorties dans les notebooks pour référence
- Utiliser des noms de variables clairs correspondant aux concepts de la leçon
- Garder l'ordre d'exécution des cellules linéaire (cellule 1 → 2 → 3...)

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

## Build et déploiement

### Construction de la documentation

Ce dépôt utilise Markdown pour la documentation :
- fichiers README.md dans chaque dossier de leçon
- README.md principal à la racine du dépôt
- Système de traduction automatisé via GitHub Actions

### Pipeline CI/CD

Situé dans `.github/workflows/` :

1. **co-op-translator.yml** - Traduction automatique en 50+ langues
2. **welcome-issue.yml** - Accueille les nouveaux créateurs d'issues
3. **welcome-pr.yml** - Accueille les nouveaux contributeurs de pull requests

### Déploiement

Il s'agit d'un dépôt éducatif - pas de processus de déploiement. Les utilisateurs :
1. Forkent ou clonent le dépôt
2. Exécutent les notebooks localement ou dans GitHub Codespaces
3. Apprennent en modifiant et expérimentant avec les exemples

## Guide pour les Pull Requests

### Avant de soumettre

1. **Tester vos modifications :**
   - Exécuter complètement les notebooks affectés
   - Vérifier que toutes les cellules s'exécutent sans erreurs
   - S'assurer que les sorties sont appropriées

2. **Mises à jour de la documentation :**
   - Mettre à jour README.md si de nouveaux concepts sont ajoutés
   - Ajouter des commentaires dans les notebooks pour les codes complexes
   - Veiller à ce que les cellules markdown expliquent le but

3. **Modifications des fichiers :**
   - Éviter de committer les fichiers `.env` (utiliser `.env.example`)
   - Ne pas committer les dossiers `venv/` ou `__pycache__/`
   - Garder les sorties des notebooks quand elles illustrent des concepts
   - Supprimer les fichiers temporaires et backups de notebooks (`*-backup.ipynb`)

### Format du titre de PR

Utiliser des titres descriptifs :
- `[Lesson-XX] Ajouter nouvel exemple pour <concept>`
- `[Fix] Corriger une faute dans le README de la leçon-XX`
- `[Update] Améliorer l'exemple de code dans la leçon-XX`
- `[Docs] Mettre à jour les instructions d'installation`

### Vérifications requises

- Les notebooks doivent s'exécuter sans erreurs
- Les fichiers README doivent être clairs et précis
- Suivre les modèles de code existants dans le dépôt
- Maintenir la cohérence avec les autres leçons

## Notes supplémentaires

### Pièges courants

1. **Incompatibilité de version Python :**
   - S'assurer d'utiliser Python 3.12+
   - Certains paquets peuvent ne pas fonctionner avec des versions antérieures
   - Utiliser `python3 -m venv` pour spécifier explicitement la version Python

2. **Variables d'environnement :**
   - Toujours créer `.env` à partir de `.env.example`
   - Ne pas committer le fichier `.env` (il est dans `.gitignore`)
   - Le token GitHub nécessite les permissions appropriées

3. **Conflits de paquets :**
   - Utiliser un nouvel environnement virtuel
   - Installer depuis `requirements.txt` plutôt que des paquets individuels
   - Certains notebooks peuvent requérir des paquets supplémentaires mentionnés dans leurs cellules markdown

4. **Services Azure :**
   - Les services Azure AI requièrent un abonnement actif
   - Certaines fonctionnalités sont spécifiques à certaines régions
   - Limites de la couche gratuite applicables aux modèles GitHub

### Parcours d'apprentissage

Progression recommandée à travers les leçons :
1. **00-course-setup** - Commencer ici pour la configuration de l'environnement
2. **01-intro-to-ai-agents** - Comprendre les fondamentaux des agents IA
3. **02-explore-agentic-frameworks** - Découvrir différents frameworks
4. **03-agentic-design-patterns** - Modèles de conception fondamentaux
5. Continuer les leçons numérotées séquentiellement

### Choix du framework

Choisir le framework selon vos objectifs :
- **Toutes les leçons** : Microsoft Agent Framework (MAF) avec `AzureAIProjectAgentProvider`
- **Les agents s'enregistrent côté serveur** dans Azure AI Foundry Agent Service V2 et sont visibles dans le portail Foundry

### Obtenir de l'aide

- Rejoindre le [Discord de la communauté Microsoft Foundry](https://aka.ms/ai-agents/discord)
- Consulter les fichiers README des leçons pour des conseils spécifiques
- Voir le [README.md principal](./README.md) pour l'aperçu du cours
- Se référer à [Course Setup](./00-course-setup/README.md) pour les instructions de configuration détaillées

### Contribution

Ceci est un projet éducatif ouvert. Contributions bienvenues :
- Améliorer les exemples de code
- Corriger les coquilles ou erreurs
- Ajouter des commentaires explicatifs
- Proposer de nouveaux sujets de leçons
- Traduire en langues supplémentaires

Voir les [Issues GitHub](https://github.com/microsoft/ai-agents-for-beginners/issues) pour les besoins actuels.

## Contexte spécifique au projet

### Support multilingue

Ce dépôt utilise un système de traduction automatisé :
- Plus de 50 langues supportées
- Traductions dans les répertoires `/translations/<lang-code>/`
- Workflow GitHub Actions gère les mises à jour de traduction
- Les fichiers sources sont en anglais à la racine du dépôt

### Structure des leçons

Chaque leçon suit un modèle cohérent :
1. Vignette vidéo avec lien
2. Contenu écrit de la leçon (README.md)
3. Exemples de code dans plusieurs frameworks
4. Objectifs d’apprentissage et prérequis
5. Ressources d’apprentissage complémentaires liées

### Nommage des exemples de code

Format : `<numéro-leçon>-python-agent-framework.ipynb`
- `01-python-agent-framework.ipynb` - Leçon 1, MAF Python
- `14-sequential.ipynb` - Leçon 14, modèles avancés MAF

### Répertoires spéciaux

- `translated_images/` - Images localisées pour les traductions
- `images/` - Images originales pour le contenu anglais
- `.devcontainer/` - Configuration du container de développement VS Code
- `.github/` - Workflows GitHub Actions et templates

### Dépendances

Paquets clés dans `requirements.txt` :
- `agent-framework` - Microsoft Agent Framework
- `a2a-sdk` - support protocole Agent-à-Agent
- `azure-ai-inference`, `azure-ai-projects` - services Azure AI
- `azure-identity` - authentification Azure (AzureCliCredential)
- `azure-search-documents` - intégration Azure AI Search
- `mcp[cli]` - support Model Context Protocol

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Avertissement** :
Ce document a été traduit à l'aide du service de traduction automatique [Co-op Translator](https://github.com/Azure/co-op-translator). Bien que nous nous efforçions d'assurer l'exactitude, veuillez noter que les traductions automatisées peuvent contenir des erreurs ou des inexactitudes. Le document original dans sa langue native doit être considéré comme la source faisant autorité. Pour les informations critiques, il est recommandé de recourir à une traduction professionnelle réalisée par un humain. Nous ne saurions être tenus responsables des malentendus ou erreurs d'interprétation découlant de l'utilisation de cette traduction.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->