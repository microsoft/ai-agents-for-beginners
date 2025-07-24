<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "c6a79c8f2b56a80370ff7e447765524f",
  "translation_date": "2025-07-24T07:30:52+00:00",
  "source_file": "00-course-setup/README.md",
  "language_code": "fr"
}
-->
# Configuration du cours

## Introduction

Cette leçon explique comment exécuter les exemples de code de ce cours.

## Cloner ou forker ce dépôt

Pour commencer, veuillez cloner ou forker le dépôt GitHub. Cela vous permettra de créer votre propre version du matériel du cours afin de pouvoir exécuter, tester et modifier le code !

Cela peut être fait en cliquant sur le lien pour

Vous devriez maintenant avoir votre propre version forkée de ce cours dans le lien suivant :

![Dépôt forké](../../../translated_images/forked-repo.33f27ca1901baa6a5e13ec3eb1f0ddd3a44d936d91cc8cfb19bfdb9688bd2c3d.fr.png)

## Exécution du code

Ce cours propose une série de notebooks Jupyter que vous pouvez exécuter pour acquérir une expérience pratique dans la création d'agents d'IA.

Les exemples de code utilisent soit :

**Nécessite un compte GitHub - Gratuit** :

1) Framework Semantic Kernel Agent + Marketplace des modèles GitHub. Identifié comme (semantic-kernel.ipynb)  
2) Framework AutoGen + Marketplace des modèles GitHub. Identifié comme (autogen.ipynb)

**Nécessite un abonnement Azure** :  
3) Azure AI Foundry + Service Azure AI Agent. Identifié comme (azureaiagent.ipynb)

Nous vous encourageons à essayer les trois types d'exemples pour voir lequel vous convient le mieux.

L'option que vous choisissez déterminera les étapes de configuration à suivre ci-dessous :

## Prérequis

- Python 3.12+  
  - **NOTE** : Si vous n'avez pas Python 3.12 installé, assurez-vous de l'installer. Ensuite, créez votre environnement virtuel (venv) en utilisant python3.12 pour garantir que les bonnes versions sont installées à partir du fichier requirements.txt.  
- Un compte GitHub - Pour accéder au Marketplace des modèles GitHub  
- Un abonnement Azure - Pour accéder à Azure AI Foundry  
- Un compte Azure AI Foundry - Pour accéder au service Azure AI Agent  

Nous avons inclus un fichier `requirements.txt` à la racine de ce dépôt qui contient tous les packages Python nécessaires pour exécuter les exemples de code.

Vous pouvez les installer en exécutant la commande suivante dans votre terminal à la racine du dépôt :

```bash
pip install -r requirements.txt
```  
Nous recommandons de créer un environnement virtuel Python pour éviter tout conflit ou problème.

## Configuration de VSCode

Assurez-vous d'utiliser la bonne version de Python dans VSCode.

![image](https://github.com/user-attachments/assets/a85e776c-2edb-4331-ae5b-6bfdfb98ee0e)

## Configuration pour les exemples utilisant les modèles GitHub

### Étape 1 : Récupérer votre jeton d'accès personnel GitHub (PAT)

Ce cours utilise le Marketplace des modèles GitHub, qui offre un accès gratuit à des modèles de langage (LLMs) que vous utiliserez pour créer des agents d'IA.

Pour utiliser les modèles GitHub, vous devrez créer un [jeton d'accès personnel GitHub](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens).

Cela peut être fait en accédant à votre compte GitHub.

Veuillez suivre le [principe du moindre privilège](https://docs.github.com/en/get-started/learning-to-code/storing-your-secrets-safely) lors de la création de votre jeton. Cela signifie que vous ne devez accorder au jeton que les permissions nécessaires pour exécuter les exemples de code de ce cours.

1. Sélectionnez l'option `Fine-grained tokens` sur le côté gauche de votre écran.

    Ensuite, sélectionnez `Generate new token`.

    ![Générer un jeton](../../../translated_images/generate-new-token.8772e24e8e2e067f2e6742500eaf68bb5c5f8999537bd79a040d2ecc09c7fdcb.fr.png)

1. Entrez un nom descriptif pour votre jeton qui reflète son objectif, afin de pouvoir l'identifier facilement plus tard. Définissez une date d'expiration (recommandé : 30 jours ; vous pouvez choisir une période plus courte comme 7 jours si vous préférez une posture plus sécurisée).

    ![Nom et expiration du jeton](../../../translated_images/token-name-expiry-date.a095fb0de63868640a4c82d6b1bbc92b482930a663917a5983a3c7cd1ef86b77.fr.png)

1. Limitez la portée du jeton à votre fork de ce dépôt.

    ![Limiter la portée au dépôt forké](../../../translated_images/select-fork-repository.4497f6bb05ccd6b474ed134493a815fc34f94f89db2b1630c494adff7b5b558a.fr.png)

1. Restreignez les permissions du jeton : Sous **Permissions**, activez **Account Permissions**, accédez à **Models** et activez uniquement l'accès en lecture requis pour les modèles GitHub.

    ![Permissions du compte](../../../translated_images/account-permissions.de1806fad33a72c6194d2688cf2c10f2adb9ff7a5c1041a2329cbef46bffbba0.fr.png)

    ![Accès en lecture aux modèles](../../../translated_images/models-read-access.c00bc44e28c40450a85542e19f8e8c68284c71861c076b7dbc078b4c7e51faa6.fr.png)

Copiez votre nouveau jeton que vous venez de créer. Vous allez maintenant l'ajouter à votre fichier `.env` inclus dans ce cours.

### Étape 2 : Créer votre fichier `.env`

Pour créer votre fichier `.env`, exécutez la commande suivante dans votre terminal.

```bash
cp .env.example .env
```

Cela copiera le fichier exemple et créera un `.env` dans votre répertoire, où vous remplirez les valeurs des variables d'environnement.

Avec votre jeton copié, ouvrez le fichier `.env` dans votre éditeur de texte préféré et collez votre jeton dans le champ `GITHUB_TOKEN`.

Vous devriez maintenant être en mesure d'exécuter les exemples de code de ce cours.

## Configuration pour les exemples utilisant Azure AI Foundry et le service Azure AI Agent

### Étape 1 : Récupérer l'endpoint de votre projet Azure

Suivez les étapes pour créer un hub et un projet dans Azure AI Foundry ici : [Vue d'ensemble des ressources du hub](https://learn.microsoft.com/en-us/azure/ai-foundry/concepts/ai-resources)

Une fois votre projet créé, vous devrez récupérer la chaîne de connexion de votre projet.

Cela peut être fait en accédant à la page **Vue d'ensemble** de votre projet dans le portail Azure AI Foundry.

![Chaîne de connexion du projet](../../../translated_images/project-endpoint.8cf04c9975bbfbf18f6447a599550edb052e52264fb7124d04a12e6175e330a5.fr.png)

### Étape 2 : Créer votre fichier `.env`

Pour créer votre fichier `.env`, exécutez la commande suivante dans votre terminal.

```bash
cp .env.example .env
```

Cela copiera le fichier exemple et créera un `.env` dans votre répertoire, où vous remplirez les valeurs des variables d'environnement.

Avec votre jeton copié, ouvrez le fichier `.env` dans votre éditeur de texte préféré et collez votre jeton dans le champ `PROJECT_ENDPOINT`.

### Étape 3 : Se connecter à Azure

En tant que bonne pratique de sécurité, nous utiliserons [l'authentification sans clé](https://learn.microsoft.com/azure/developer/ai/keyless-connections?tabs=csharp%2Cazure-cli?WT.mc_id=academic-105485-koreyst) pour nous authentifier auprès d'Azure OpenAI avec Microsoft Entra ID.

Ensuite, ouvrez un terminal et exécutez `az login --use-device-code` pour vous connecter à votre compte Azure.

Une fois connecté, sélectionnez votre abonnement dans le terminal.

## Variables d'environnement supplémentaires - Azure Search et Azure OpenAI

Pour la leçon Agentic RAG - Leçon 5 - il existe des exemples utilisant Azure Search et Azure OpenAI.

Si vous souhaitez exécuter ces exemples, vous devrez ajouter les variables d'environnement suivantes à votre fichier `.env` :

### Page Vue d'ensemble (Projet)

- `AZURE_SUBSCRIPTION_ID` - Consultez les **Détails du projet** sur la page **Vue d'ensemble** de votre projet.

- `AZURE_AI_PROJECT_NAME` - Regardez en haut de la page **Vue d'ensemble** de votre projet.

- `AZURE_OPENAI_SERVICE` - Trouvez cela dans l'onglet **Capacités incluses** pour **Azure OpenAI Service** sur la page **Vue d'ensemble**.

### Centre de gestion

- `AZURE_OPENAI_RESOURCE_GROUP` - Allez dans **Propriétés du projet** sur la page **Vue d'ensemble** du **Centre de gestion**.

- `GLOBAL_LLM_SERVICE` - Sous **Ressources connectées**, trouvez le nom de connexion des **Services Azure AI**. Si non listé, vérifiez le **portail Azure** sous votre groupe de ressources pour le nom de la ressource AI Services.

### Page Modèles + Endpoints

- `AZURE_OPENAI_EMBEDDING_DEPLOYMENT_NAME` - Sélectionnez votre modèle d'embedding (par ex., `text-embedding-ada-002`) et notez le **Nom du déploiement** dans les détails du modèle.

- `AZURE_OPENAI_CHAT_DEPLOYMENT_NAME` - Sélectionnez votre modèle de chat (par ex., `gpt-4o-mini`) et notez le **Nom du déploiement** dans les détails du modèle.

### Portail Azure

- `AZURE_OPENAI_ENDPOINT` - Recherchez **Services Azure AI**, cliquez dessus, puis allez dans **Gestion des ressources**, **Clés et Endpoint**, faites défiler jusqu'aux "Endpoints Azure OpenAI" et copiez celui qui indique "APIs de langage".

- `AZURE_OPENAI_API_KEY` - Depuis le même écran, copiez la CLÉ 1 ou la CLÉ 2.

- `AZURE_SEARCH_SERVICE_ENDPOINT` - Trouvez votre ressource **Azure AI Search**, cliquez dessus et consultez **Vue d'ensemble**.

- `AZURE_SEARCH_API_KEY` - Ensuite, allez dans **Paramètres**, puis **Clés** pour copier la clé administrateur principale ou secondaire.

### Page externe

- `AZURE_OPENAI_API_VERSION` - Consultez la page [Cycle de vie des versions API](https://learn.microsoft.com/en-us/azure/ai-services/openai/api-version-deprecation#latest-ga-api-release) sous **Dernière version GA de l'API**.

### Configurer l'authentification sans clé

Plutôt que de coder en dur vos identifiants, nous utiliserons une connexion sans clé avec Azure OpenAI. Pour ce faire, nous importerons `DefaultAzureCredential` et appellerons ensuite la fonction `DefaultAzureCredential` pour obtenir les identifiants.

```python
from azure.identity import DefaultAzureCredential, InteractiveBrowserCredential
```

## Bloqué quelque part ?

Si vous rencontrez des problèmes pour exécuter cette configuration, rejoignez notre

## Leçon suivante

Vous êtes maintenant prêt à exécuter le code de ce cours. Bonne exploration du monde des agents d'IA !

[Introduction aux agents d'IA et cas d'utilisation des agents](../01-intro-to-ai-agents/README.md)

**Avertissement** :  
Ce document a été traduit à l'aide du service de traduction automatique [Co-op Translator](https://github.com/Azure/co-op-translator). Bien que nous nous efforcions d'assurer l'exactitude, veuillez noter que les traductions automatisées peuvent contenir des erreurs ou des inexactitudes. Le document original dans sa langue d'origine doit être considéré comme la source faisant autorité. Pour des informations critiques, il est recommandé de recourir à une traduction professionnelle réalisée par un humain. Nous déclinons toute responsabilité en cas de malentendus ou d'interprétations erronées résultant de l'utilisation de cette traduction.