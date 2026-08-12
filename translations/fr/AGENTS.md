# AGENTS.md

## Vue d'ensemble du projet

Ce dépôt contient "Agents IA pour débutants" - un cours éducatif complet enseignant tout ce qui est nécessaire pour construire des agents IA. Le cours comprend 18 leçons (numérotées de 00 à 18) couvrant les fondamentaux, les modèles de conception, les frameworks, le déploiement en production, les agents locaux/sur appareil, et la sécurité des agents IA.

**Technologies clés :**
- Python 3.12+
- Jupyter Notebooks pour un apprentissage interactif
- Frameworks IA : Microsoft Agent Framework (MAF)
- Services Azure AI : Microsoft Foundry, Microsoft Foundry Agent Service V2

**Architecture :**
- Structure basée sur les leçons (répertoires 00-15+)
- Chaque leçon contient : documentation README, exemples de code (notebooks Jupyter), et images
- Support multilingue via un système de traduction automatisé
- Un notebook Python par leçon utilisant Microsoft Agent Framework

## Commandes d'installation

### Prérequis
- Python 3.12 ou supérieur
- Abonnement Azure (pour Microsoft Foundry)
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
   # Modifiez .env avec vos clés API et points de terminaison
   ```

### Variables d'environnement requises

Pour **Microsoft Foundry** (obligatoire) :
- `AZURE_AI_PROJECT_ENDPOINT` - point de terminaison du projet Microsoft Foundry
- `AZURE_AI_MODEL_DEPLOYMENT_NAME` - nom du déploiement du modèle (ex : gpt-5-mini)

Pour **Azure AI Search** (Leçon 05 - RAG) :
- `AZURE_SEARCH_SERVICE_ENDPOINT` - point de terminaison Azure AI Search
- `AZURE_SEARCH_API_KEY` - clé API Azure AI Search

Authentification : Exécutez `az login` avant d'exécuter les notebooks (utilise `AzureCliCredential`).

## Flux de développement

### Exécution des Jupyter Notebooks

Chaque leçon contient plusieurs notebooks Jupyter pour différents frameworks :

1. **Démarrer Jupyter :**
   ```bash
   jupyter notebook
   ```

2. **Naviguer vers un répertoire de leçon** (ex : `01-intro-to-ai-agents/code_samples/`)

3. **Ouvrir et exécuter les notebooks :**
   - `*-python-agent-framework.ipynb` - Utilisant Microsoft Agent Framework (Python)
   - `*-dotnet-agent-framework.ipynb` - Utilisant Microsoft Agent Framework (.NET)

### Travailler avec Microsoft Agent Framework

**Microsoft Agent Framework + Microsoft Foundry :**
- Nécessite un abonnement Azure
- Utilise `FoundryChatClient` pour Agent Service V2 (agents visibles dans le portail Foundry)
- Prêt pour la production avec observabilité intégrée
- Modèle de fichier : `*-python-agent-framework.ipynb`

## Instructions de test

Ceci est un dépôt éducatif avec du code d'exemple plutôt que du code de production avec des tests automatisés. Pour vérifier votre configuration et vos modifications :

### Tests manuels

1. **Tester l'environnement Python :**
   ```bash
   python --version  # Doit être 3.12+
   pip list | grep -E "(agent-framework|azure-ai|azure-identity)"
   ```

2. **Tester l'exécution du notebook :**
   ```bash
   # Convertir le carnet en script et exécuter (teste les importations)
   jupyter nbconvert --to script <lesson-folder>/code_samples/<notebook>.ipynb --stdout | python
   ```

3. **Vérifier les variables d'environnement :**
   ```bash
   python -c "import os; from dotenv import load_dotenv; load_dotenv(); print('✓ AZURE_AI_PROJECT_ENDPOINT' if os.getenv('AZURE_AI_PROJECT_ENDPOINT') else '✗ AZURE_AI_PROJECT_ENDPOINT missing')"
   ```

### Exécution des notebooks individuellement

Ouvrez les notebooks dans Jupyter et exécutez les cellules séquentiellement. Chaque notebook est autonome et comprend :
- Instructions d'importation
- Chargement de configuration
- Exemples d'implémentations d'agents
- Résultats attendus dans les cellules markdown

### Test rapide des agents déployés

Pour les leçons où un agent est déployé en tant qu'agent hébergé Microsoft Foundry (01, 04, 05, 16), le dépôt inclut des catalogues de tests rapides sous `tests/` qui sont exécutés par le workflow `.github/workflows/smoke-test.yml` via l'action [AI Smoke Test](https://github.com/marketplace/actions/ai-smoke-test). Ce sont des contrôles post-déploiement légers (l'agent est-il accessible et suit-il les attentes basiques d'invite ?), complétant le pipeline d'évaluation des leçons 10 et 16. Voir [tests/README.md](./tests/README.md) pour la correspondance catalogue-leçon-agent. La leçon 17 s'exécute localement avec Foundry Local et n'a pas de point de terminaison hébergé, donc elle est validée en exécutant directement son notebook.

## Style de code

### Conventions Python

- **Version Python** : 3.12+
- **Style de code** : Suivre les conventions standards PEP 8 de Python
- **Notebooks** : Utiliser des cellules markdown claires pour expliquer les concepts
- **Imports** : Grouper par bibliothèque standard, tierce partie, imports locaux

### Conventions Jupyter Notebook

- Inclure des cellules markdown descriptives avant les cellules de code
- Ajouter des exemples de sortie dans les notebooks pour référence
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

1. **co-op-translator.yml** - Traduction automatique en plus de 50 langues
2. **welcome-issue.yml** - Accueille les créateurs de nouvelles issues
3. **welcome-pr.yml** - Accueille les contributeurs de pull requests

### Déploiement

Il s'agit d'un dépôt éducatif - pas de processus de déploiement. Les utilisateurs doivent :
1. Forker ou cloner le dépôt
2. Exécuter les notebooks localement ou via GitHub Codespaces
3. Apprendre en modifiant et en expérimentant avec les exemples

## Directives pour les Pull Requests

### Avant de soumettre

1. **Tester vos modifications :**
   - Exécutez complètement les notebooks affectés
   - Vérifiez que toutes les cellules s'exécutent sans erreurs
   - Contrôlez que les sorties sont appropriées

2. **Mises à jour de la documentation :**
   - Mettez à jour README.md si vous ajoutez de nouveaux concepts
   - Ajoutez des commentaires dans les notebooks pour le code complexe
   - Assurez-vous que les cellules markdown expliquent leur but

3. **Modifications de fichiers :**
   - Évitez de committer des fichiers `.env` (utilisez `.env.example`)
   - Ne commettez pas les répertoires `venv/` ou `__pycache__/`
   - Conservez les sorties de notebook lorsqu'elles démontrent des concepts
   - Supprimez les fichiers temporaires et notebooks de sauvegarde (`*-backup.ipynb`)

### Format des titres des PR

Utilisez des titres descriptifs :
- `[Lesson-XX] Ajouter un nouvel exemple pour <concept>`
- `[Fix] Correction d'une faute dans README de la leçon-XX`
- `[Update] Amélioration de l'exemple de code dans la leçon-XX`
- `[Docs] Mise à jour des instructions d'installation`

### Vérifications requises

- Les notebooks doivent s'exécuter sans erreurs
- Les fichiers README doivent être clairs et exacts
- Suivre les modèles de code existants dans le dépôt
- Maintenir la cohérence avec les autres leçons

## Notes supplémentaires

### Pièges courants

1. **Incompatibilité de version Python :**
   - Assurez-vous d'utiliser Python 3.12+
   - Certains paquets ne fonctionnent pas avec des versions plus anciennes
   - Utilisez `python3 -m venv` pour spécifier explicitement la version de Python

2. **Variables d'environnement :**
   - Créez toujours un `.env` à partir de `.env.example`
   - Ne commettez pas le fichier `.env` (il est dans `.gitignore`)
   - Connectez-vous avec `az login` pour une authentification Entra ID sans clé

3. **Conflits de packages :**
   - Utilisez un environnement virtuel propre
   - Installez depuis `requirements.txt` plutôt que des paquets individuels
   - Certains notebooks peuvent nécessiter des paquets additionnels mentionnés dans leurs cellules markdown

4. **Services Azure :**
   - Les services Azure AI requièrent un abonnement actif
   - Certaines fonctionnalités sont spécifiques à une région
   - Assurez-vous que votre déploiement de modèle Azure OpenAI supporte l'API Responses

### Parcours d'apprentissage

Progression recommandée à travers les leçons :
1. **00-course-setup** - Commencez ici pour la configuration de l'environnement
2. **01-intro-to-ai-agents** - Comprendre les fondamentaux des agents IA
3. **02-explore-agentic-frameworks** - Découvrir différents frameworks
4. **03-agentic-design-patterns** - Modèles de conception principaux
5. Continuez à travers les leçons numérotées dans l'ordre

### Choix du framework

Choisissez votre framework selon vos objectifs :
- **Toutes les leçons** : Microsoft Agent Framework (MAF) avec `FoundryChatClient`
- **Agents enregistrés côté serveur** dans Microsoft Foundry Agent Service V2 et visibles dans le portail Foundry

### Obtenir de l'aide

- Rejoignez le [Microsoft Foundry Community Discord](https://aka.ms/ai-agents/discord)
- Consultez les fichiers README des leçons pour des conseils spécifiques
- Vérifiez le [README.md](./README.md) principal pour un aperçu du cours
- Reportez-vous à [Course Setup](./00-course-setup/README.md) pour des instructions détaillées d'installation

### Contribution

Ceci est un projet éducatif ouvert. Contributions bienvenues :
- Améliorer les exemples de code
- Corriger les fautes ou erreurs
- Ajouter des commentaires explicatifs
- Suggérer de nouveaux sujets de leçons
- Traduire vers d'autres langues

Voir les [GitHub Issues](https://github.com/microsoft/ai-agents-for-beginners/issues) pour les besoins actuels.

## Contexte spécifique au projet

### Support multilingue

Ce dépôt utilise un système de traduction automatisé :
- Plus de 50 langues supportées
- Traductions dans les répertoires `/translations/<code-lang>/`
- Workflow GitHub Actions gère les mises à jour des traductions
- Les fichiers sources sont en anglais à la racine du dépôt

### Structure des leçons

Chaque leçon suit un modèle cohérent :
1. Miniature vidéo avec lien
2. Contenu écrit de la leçon (README.md)
3. Exemples de code dans plusieurs frameworks
4. Objectifs d'apprentissage et prérequis
5. Ressources supplémentaires liées

### Nomination des exemples de code

Format : `<numéro-leçon>-python-agent-framework.ipynb`
- `01-python-agent-framework.ipynb` - Leçon 1, MAF Python
- `14-sequential.ipynb` - Leçon 14, modèles avancés MAF
- `16-python-agent-framework.ipynb` - Leçon 16, agent support client en production
- `17-local-agent-foundry-local.ipynb` - Leçon 17, agent local avec Foundry Local + Qwen

### Répertoires spéciaux

- `translated_images/` - Images localisées pour les traductions
- `images/` - Images originales pour le contenu en anglais
- `.devcontainer/` - Configuration du conteneur de développement VS Code
- `.github/` - Workflows et templates GitHub Actions

### Dépendances

Principaux packages dans `requirements.txt` :
- `agent-framework` - Microsoft Agent Framework
- `a2a-sdk` - Support du protocole Agent-to-Agent
- `azure-ai-inference`, `azure-ai-projects` - Services Azure AI
- `azure-identity` - Authentification Azure (AzureCliCredential)
- `azure-search-documents` - Intégration Azure AI Search
- `mcp[cli]` - Support du Model Context Protocol

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Avertissement** :
Ce document a été traduit à l'aide du service de traduction automatique [Co-op Translator](https://github.com/Azure/co-op-translator). Bien que nous nous efforçions d'assurer l'exactitude, veuillez noter que les traductions automatisées peuvent contenir des erreurs ou des inexactitudes. Le document original dans sa langue native doit être considéré comme la source faisant autorité. Pour les informations critiques, il est recommandé de recourir à une traduction professionnelle réalisée par un humain. Nous ne saurions être tenus responsables des malentendus ou erreurs d'interprétation découlant de l'utilisation de cette traduction.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->