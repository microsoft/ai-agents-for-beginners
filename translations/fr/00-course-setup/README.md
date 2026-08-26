# Configuration du cours

## Introduction

Cette leçon expliquera comment exécuter les exemples de code de ce cours.

## Rejoignez d'autres apprenants et obtenez de l'aide

Avant de commencer à cloner votre dépôt, rejoignez le [canal Discord AI Agents For Beginners](https://aka.ms/ai-agents/discord) pour obtenir de l'aide sur la configuration, poser vos questions sur le cours ou pour connecter avec d'autres apprenants.

## Cloner ou forker ce dépôt

Pour commencer, veuillez cloner ou forker le dépôt GitHub. Cela vous permettra d'avoir votre propre version du matériel du cours afin que vous puissiez exécuter, tester et modifier le code !

Cela peut être fait en cliquant sur le lien <a href="https://github.com/microsoft/ai-agents-for-beginners/fork" target="_blank">forker le dépôt</a>

Vous devriez maintenant avoir votre propre version forkée de ce cours accessible via le lien suivant :

![Dépôt forké](../../../translated_images/fr/forked-repo.33f27ca1901baa6a.webp)

### Clone superficiel (recommandé pour atelier / Codespaces)

  >Le dépôt complet peut être volumineux (~3 Go) lorsque vous téléchargez tout l'historique et tous les fichiers. Si vous assistez seulement à l'atelier ou si vous avez besoin uniquement de quelques dossiers de leçon, un clone superficiel (ou clone partiel) télécharge beaucoup moins.

#### Clone superficiel rapide — historique minimal, tous les fichiers

Remplacez `<your-username>` dans les commandes ci-dessous par l'URL de votre fork (ou l'URL d'origine si vous préférez).

Pour cloner uniquement l'historique des derniers commits (téléchargement réduit) :

```bash
git clone --depth 1 https://github.com/<your-username>/ai-agents-for-beginners.git
```

Pour cloner une branche spécifique :

```bash
git clone --depth 1 --branch <branch-name> https://github.com/<your-username>/ai-agents-for-beginners.git
```

#### Clone partiel (sparse) — blobs minimaux + seulement dossiers sélectionnés

Utilise un clone partiel et sparse-checkout (nécessite Git 2.25+ et Git moderne avec support du clone partiel) :

```bash
git clone --depth 1 --filter=blob:none --sparse https://github.com/<your-username>/ai-agents-for-beginners.git
```

Accédez au dossier du dépôt :

```bash
cd ai-agents-for-beginners
```

Puis spécifiez les dossiers souhaités (exemple ci-dessous montre deux dossiers) :

```bash
git sparse-checkout set 00-course-setup 01-intro-to-ai-agents
```

Après avoir cloné et vérifié les fichiers, si vous n'avez besoin que des fichiers et souhaitez libérer de l'espace (pas d'historique Git), veuillez supprimer les métadonnées du dépôt (💀 irréversible — vous perdrez toute fonctionnalité Git) :

```bash
# zsh/bash
rm -rf .git
```

```powershell
# PowerShell
Remove-Item -Recurse -Force .git
```

#### Utilisation de GitHub Codespaces (recommandé pour éviter de gros téléchargements locaux)

- Créez un nouveau Codespace pour ce dépôt via l'[interface GitHub](https://github.com/codespaces).  

- Dans le terminal du Codespace nouvellement créé, exécutez l'une des commandes de clone superficiel/sparse ci-dessus pour importer seulement les dossiers de leçon nécessaires dans le workspace Codespace.
- Optionnel : après clonage dans Codespaces, supprimez `.git` pour récupérer de l’espace supplémentaire (voir les commandes de suppression ci-dessus).
- Remarque : si vous préférez ouvrir directement le dépôt dans Codespaces (sans clone supplémentaire), sachez que Codespaces construira l’environnement devcontainer et pourra toujours approvisionner plus que nécessaire.

#### Astuces

- Remplacez toujours l'URL de clonage par votre fork si vous voulez modifier/committer.
- Si vous avez besoin ultérieurement de plus d’historique ou de fichiers, vous pouvez les récupérer ou ajuster sparse-checkout pour inclure des dossiers supplémentaires.

## Exécution du code

Ce cours propose une série de notebooks Jupyter que vous pouvez exécuter pour acquérir une expérience pratique de la création d’agents IA.

Les exemples de code utilisent **Microsoft Agent Framework (MAF)** avec le `FoundryChatClient`, qui se connecte à **Microsoft Foundry Agent Service V2** (l’API Responses) via **Microsoft Foundry**.

Tous les notebooks Python sont nommés `*-python-agent-framework.ipynb`.

## Pré-requis

- Python 3.12+
  - **NOTE** : Si vous n’avez pas Python3.12 installé, assurez-vous de l’installer. Ensuite, créez votre environnement virtuel en utilisant python3.12 pour garantir l’installation des bonnes versions à partir du fichier requirements.txt.
  
    >Exemple

    Créez un répertoire d’environnement virtuel Python :

    ```bash
    python -m venv venv
    ```

    Puis activez l’environnement virtuel pour :

    ```bash
    # zsh/bash
    source venv/bin/activate
    ```
  
    ```dos
    # Command Prompt for Windows
    venv\Scripts\activate
    ```

- .NET 10+ : Pour les exemples de code utilisant .NET, assurez-vous d’installer le [.NET 10 SDK](https://dotnet.microsoft.com/download/dotnet/10.0) ou supérieur. Ensuite, vérifiez votre version .NET SDK installée :

    ```bash
    dotnet --list-sdks
    ```

- **Azure CLI** — requis pour l’authentification. Installez-le depuis [aka.ms/installazurecli](https://aka.ms/installazurecli).
- **Abonnement Azure** — pour accéder à Microsoft Foundry et Microsoft Foundry Agent Service.
- **Projet Microsoft Foundry** — un projet avec un modèle déployé (ex., `gpt-5-mini`). Voir [Étape 1](#étape-1-créer-un-projet-microsoft-foundry) ci-dessous.

Nous avons inclus un fichier `requirements.txt` à la racine de ce dépôt qui contient tous les paquets Python nécessaires pour exécuter les exemples de code.

Vous pouvez les installer en exécutant la commande suivante dans votre terminal à la racine du dépôt :

```bash
pip install -r requirements.txt
```

Nous recommandons de créer un environnement virtuel Python pour éviter tout conflit ou problème.

## Configuration de VSCode

Assurez-vous d’utiliser la bonne version de Python dans VSCode.

![image](https://github.com/user-attachments/assets/a85e776c-2edb-4331-ae5b-6bfdfb98ee0e)

## Configuration de Microsoft Foundry et Microsoft Foundry Agent Service

### Étape 1 : Créer un projet Microsoft Foundry

Vous avez besoin d’un **hub** Microsoft Foundry et d’un **projet** avec un modèle déployé pour exécuter les notebooks.

1. Allez sur [ai.azure.com](https://ai.azure.com) et connectez-vous avec votre compte Azure.
2. Créez un **hub** (ou utilisez-en un existant). Voir : [Vue d’ensemble des ressources du hub](https://learn.microsoft.com/azure/ai-foundry/concepts/ai-resources).
3. À l’intérieur du hub, créez un **projet**.
4. Déployez un modèle (ex., `gpt-5-mini`) via **Models + Endpoints** → **Deploy model**.

### Étape 2 : Récupérer l’endpoint de votre projet et le nom de déploiement du modèle

Depuis votre projet dans le portail Microsoft Foundry :

- **Point de terminaison du projet** — Allez à la page **Overview** et copiez l’URL de l’endpoint.

![Chaîne de connexion du projet](../../../translated_images/fr/project-endpoint.8cf04c9975bbfbf1.webp)

- **Nom du déploiement du modèle** — Allez dans **Models + Endpoints**, sélectionnez votre modèle déployé et notez le **Nom du déploiement** (ex., `gpt-5-mini`).

### Étape 3 : Connectez-vous à Azure avec `az login`

La plupart des notebooks s’authentifient via votre **connexion Azure CLI** — en utilisant `AzureCliCredential` ou `DefaultAzureCredential` (qui détectent tous les deux votre session `az login`) depuis le paquet `azure-identity` — ils ne nécessitent pas de clés d’API. Certaines leçons et intégrations optionnelles utilisent des clés d’API ; vérifiez les prérequis de chaque leçon pour d’autres variables d’environnement. Cela exige que vous soyez connecté via l’Azure CLI.

1. **Installez Azure CLI** si ce n’est pas déjà fait : [aka.ms/installazurecli](https://aka.ms/installazurecli)

2. **Connectez-vous** en exécutant :

    ```bash
    az login
    ```

    Ou, si vous êtes dans un environnement distant/Codespace sans navigateur :

    ```bash
    az login --use-device-code
    ```

3. **Sélectionnez votre abonnement** si demandé — choisissez celui qui contient votre projet Foundry.

4. **Vérifiez** que vous êtes connecté :

    ```bash
    az account show
    ```

> **Pourquoi `az login` ?** Les notebooks authentifient en utilisant `AzureCliCredential` (ou `DefaultAzureCredential`, qui détecte aussi votre connexion Azure CLI) du paquet `azure-identity`. Cela signifie que votre session Azure CLI fournit les identifiants — pas de clés API ni secrets dans votre fichier `.env`. C’est une [meilleure pratique de sécurité](https://learn.microsoft.com/azure/developer/ai/keyless-connections).

### Étape 4 : Créez votre fichier `.env`

Copiez le fichier exemple :

```bash
# zsh/bash
cp .env.example .env
```

```powershell
# PowerShell
Copy-Item .env.example .env
```

Ouvrez `.env` et remplissez ces deux valeurs :

```env
AZURE_AI_PROJECT_ENDPOINT=https://<your-project>.services.ai.azure.com/api/projects/<your-project-id>
AZURE_AI_MODEL_DEPLOYMENT_NAME=gpt-5-mini
```

| Variable | Où le trouver |
|----------|-----------------|
| `AZURE_AI_PROJECT_ENDPOINT` | Portail Foundry → votre projet → page **Overview** |
| `AZURE_AI_MODEL_DEPLOYMENT_NAME` | Portail Foundry → **Models + Endpoints** → nom de votre modèle déployé |

C’est tout pour la plupart des leçons ! Les notebooks s’authentifieront automatiquement via votre session `az login`.

### Étape 5 : Installer les dépendances Python

```bash
pip install -r requirements.txt
```

Nous recommandons d’exécuter cela dans l’environnement virtuel que vous avez créé auparavant.

## Configuration optionnelle : Azure AI Search (leçons 5 et 16)

Les notebooks de la leçon 5 (Agentic RAG) et de la leçon 16 fonctionnent immédiatement avec une **base de connaissances en mémoire** — aucune ressource Azure supplémentaire requise. Si vous souhaitez les connecter à un véritable index **Azure AI Search**, notez que le **notebook de la leçon 16 utilise actuellement une authentification basée sur clé** : il bascule de la recherche en mémoire à Azure AI Search uniquement lorsque **les deux** variables `AZURE_SEARCH_SERVICE_ENDPOINT` **et** `AZURE_SEARCH_API_KEY` sont définies, sinon il reste en recherche en mémoire — donc pour l'exécuter avec un index réel, vous devez aussi configurer la clé d’administration. L’authentification sans clé avec Microsoft Entra ID (RBAC) est la méthode recommandée pour vos propres codes de production, en cohérence avec le flux `az login` utilisé partout ailleurs dans ce cours.

Les étapes RBAC ci-dessous s’appliquent aux exemples du guide d’installation et à votre propre code. Elles n’activent pas l’authentification sans clé dans le notebook de la leçon 16 ; celle-ci nécessite encore l’endpoint et la clé d’administration pour utiliser Azure AI Search.

1. **Activez l’accès basé sur les rôles** sur votre service de recherche :

    ```bash
    az search service update --name <service-name> --resource-group <resource-group> --auth-options aadOrApiKey
    ```

2. **Attribuez-vous les rôles requis** (création/chargement d’index et requête) :

    ```bash
    az role assignment create --assignee <your-user-or-principal-id> --role "Search Service Contributor" --scope $(az search service show -g <resource-group> -n <service-name> --query id -o tsv)
    az role assignment create --assignee <your-user-or-principal-id> --role "Search Index Data Contributor" --scope $(az search service show -g <resource-group> -n <service-name> --query id -o tsv)
    ```

3. **Ajoutez l’endpoint** à votre fichier `.env` :

| Variable | Où le trouver |
|----------|-----------------|
| `AZURE_SEARCH_SERVICE_ENDPOINT` | Portail Azure → votre ressource **Azure AI Search** → **Overview** → URL |
| `AZURE_SEARCH_API_KEY` | Requise (avec l’endpoint) pour activer Azure AI Search dans le notebook de la leçon 16, qui utilise l’authentification par clé. Portail Azure → **Settings** → **Keys** → clé admin primaire |

> **Pourquoi sans clé ?** Les clés d’admin donnent un accès complet en écriture à votre service de recherche et peuvent fuiter via les fichiers `.env`. Avec RBAC, c’est votre identité `az login` qui est utilisée — le même schéma sans clé Entra ID que les notebooks du cours utilisent (via `AzureCliCredential` / `DefaultAzureCredential`). Voir [Connexion à Azure AI Search avec rôles](https://learn.microsoft.com/azure/search/search-security-rbac).

Voir le [guide de configuration Azure AI Search](./AzureSearch.md) pour des exemples complets de création d’index en Python et .NET.

## Configuration supplémentaire pour les leçons qui appellent directement Azure OpenAI (leçons 6 et 8)

Certains notebooks des leçons 6 et 8 appellent directement **Azure OpenAI** (via l’**API Responses**) au lieu de passer par un projet Microsoft Foundry. Ces exemples utilisaient auparavant GitHub Models, qui est déprécié et ne supporte pas l’API Responses. Ajoutez ces variables à votre fichier `.env` :

| Variable | Où le trouver |
|----------|-----------------|
| `AZURE_OPENAI_ENDPOINT` | Portail Azure → votre ressource **Azure OpenAI** → **Keys and Endpoint** → Endpoint (ex. `https://<votre-ressource>.openai.azure.com`) |
| `AZURE_OPENAI_DEPLOYMENT` | Le nom de votre modèle déployé (ex. `gpt-5-mini`) qui supporte l’API Responses |
| `AZURE_OPENAI_API_KEY` | Optionnel — uniquement si vous utilisez l’authentification par clé au lieu de `az login` / Entra ID |

> L’API Responses utilise le point de terminaison stable `/openai/v1/`, aucune `api-version` n’est requise. Connectez-vous avec `az login` pour utiliser l’authentification sans clé Entra ID.

## Fournisseur alternatif : MiniMax (compatible OpenAI)

[MiniMax](https://platform.minimaxi.com/) fournit des modèles à contexte large (jusqu’à 204K tokens) via une API compatible OpenAI. Comme le `OpenAIChatClient` du Microsoft Agent Framework fonctionne avec toute API compatible OpenAI, vous pouvez utiliser MiniMax comme alternative plug-and-play pour les leçons qui utilisent `OpenAIChatClient`.

Ajoutez ces variables dans votre fichier `.env` :

| Variable | Où le trouver |
|----------|-----------------|
| `MINIMAX_API_KEY` | [Plateforme MiniMax](https://platform.minimaxi.com/) → Clés API |
| `MINIMAX_BASE_URL` | Utilisez `https://api.minimax.io/v1` (valeur par défaut) |
| `MINIMAX_MODEL_ID` | Nom du modèle à utiliser (ex., `MiniMax-M3`) |

**Exemples de modèles** : `MiniMax-M3` (recommandé), `MiniMax-M2.7`, `MiniMax-M2.7-highspeed` (réponses plus rapides). Les noms et disponibilités des modèles peuvent changer, et l’accès à un modèle dépend de votre compte.

Les exemples de code qui utilisent `OpenAIChatClient` (par exemple, le workflow de réservation hôtelier de la leçon 14) détecteront et utiliseront automatiquement votre configuration MiniMax lorsque `MINIMAX_API_KEY` est défini.


## Fournisseur alternatif : Foundry Local (Exécuter les modèles en local)

[Foundry Local](https://foundrylocal.ai) est un environnement léger qui télécharge, gère et sert les modèles de langage **entièrement sur votre propre machine** via une API compatible OpenAI — sans nécessiter le cloud.

Étant donné que le `OpenAIChatClient` du Microsoft Agent Framework fonctionne avec toute interface compatible OpenAI, Foundry Local est une alternative locale prête à l'emploi à Azure OpenAI.

**1. Installer Foundry Local**

```bash
# Windows
winget install Microsoft.FoundryLocal

# macOS
brew install foundrylocal
```

**2. Télécharger et exécuter un modèle** (cela démarre également le service local) :

```bash
foundry model list          # voir les modèles disponibles
foundry model run phi-4-mini
```

**3. Installer le SDK Python** utilisé pour découvrir l'endpoint local :

```bash
pip install foundry-local-sdk
```

**4. Configurer le Microsoft Agent Framework pour pointer vers votre modèle local :**

```python
from foundry_local import FoundryLocalManager
from agent_framework.openai import OpenAIChatClient

# Télécharge (si nécessaire) et sert le modèle localement, puis découvre le point de terminaison/port.
manager = FoundryLocalManager("phi-4-mini")

chat_client = OpenAIChatClient(
    base_url=manager.endpoint,      # par ex. http://localhost:<port>/v1
    api_key=manager.api_key,        # toujours "non requis" pour Foundry Local
    model_id=manager.get_model_info("phi-4-mini").id,
)

agent = chat_client.as_agent(
    name="LocalAgent",
    instructions="You are a helpful assistant running fully on-device.",
)
```

> **Note :** Foundry Local expose un endpoint **Chat Completions** compatible OpenAI. Utilisez-le pour le développement local et les scénarios hors ligne. Pour l'ensemble complet des fonctionnalités de l' **API Responses** (conversations avec mémoire d'état, etc.), utilisez Azure OpenAI ou un projet Microsoft Foundry.

## Configuration supplémentaire pour la leçon 8 (Flux de travail Bing Grounding)

Le notebook du flux de travail conditionnel dans la leçon 8 utilise le **Bing grounding** via Microsoft Foundry. Si vous prévoyez d’exécuter cet exemple, ajoutez cette variable à votre fichier `.env` :

| Variable | Où la trouver |
|----------|---------------|
| `BING_CONNECTION_ID` | Portail Microsoft Foundry → votre projet → **Gestion** → **Ressources connectées** → votre connexion Bing → copier l’ID de connexion |

## Dépannage

### Erreurs de vérification du certificat SSL sur macOS

Si vous êtes sur macOS et rencontrez une erreur telle que :

```plaintext
ssl.SSLCertVerificationError: [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: self-signed certificate in certificate chain
```

C’est un problème connu avec Python sur macOS où les certificats SSL système ne sont pas automatiquement approuvés. Essayez les solutions suivantes dans l’ordre :

**Option 1 : Exécuter le script Install Certificates de Python (recommandé)**

```bash
# Remplacez 3.XX par votre version Python installée (par exemple, 3.12 ou 3.13) :
/Applications/Python\ 3.XX/Install\ Certificates.command
```

**Option 2 : Utiliser `connection_verify=False` dans votre notebook (uniquement pour les notebooks GitHub Models)**

Dans le notebook de la leçon 6 (`06-building-trustworthy-agents/code_samples/06-system-message-framework.ipynb`), un contournement commenté est déjà inclus. Décommentez `connection_verify=False` lorsque vous rencontrez des erreurs de certificat :

```python
client = ChatCompletionsClient(
    endpoint=endpoint,
    credential=AzureKeyCredential(token),
    connection_verify=False,  # Désactivez la vérification SSL si vous rencontrez des erreurs de certificat
)
```

> **⚠️ Avertissement :** Désactiver la vérification SSL (`connection_verify=False`) réduit la sécurité en sautant la validation des certificats. Utilisez-le uniquement comme solution temporaire en environnement de développement. Ne jamais l’utiliser en production.

**Option 3 : Installer et utiliser `truststore`**

```bash
pip install truststore
```

Ensuite, ajoutez ce qui suit en haut de votre notebook ou script avant tout appel réseau :

```python
import truststore
truststore.inject_into_ssl()
```

## Bloqué quelque part ?

Si vous avez des problèmes pour exécuter cette configuration, rejoignez notre <a href="https://discord.gg/kzRShWzttr" target="_blank">Discord de la communauté Azure AI</a> ou <a href="https://github.com/microsoft/ai-agents-for-beginners/issues?WT.mc_id=academic-105485-koreyst" target="_blank">créez un ticket</a>.

## Prochaine leçon

Vous êtes maintenant prêt à exécuter le code de ce cours. Bonne découverte du monde des agents IA !

[Introduction aux agents IA et cas d’usage des agents](../01-intro-to-ai-agents/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Avertissement** :
Ce document a été traduit à l'aide du service de traduction automatique [Co-op Translator](https://github.com/Azure/co-op-translator). Bien que nous nous efforçions d'assurer l'exactitude, veuillez noter que les traductions automatisées peuvent contenir des erreurs ou des inexactitudes. Le document original dans sa langue native doit être considéré comme la source faisant autorité. Pour les informations critiques, il est recommandé de recourir à une traduction professionnelle réalisée par un humain. Nous ne saurions être tenus responsables des malentendus ou erreurs d'interprétation découlant de l'utilisation de cette traduction.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->