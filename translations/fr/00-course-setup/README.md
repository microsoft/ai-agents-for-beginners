# Mise en place du cours

## Introduction

Cette leçon expliquera comment exécuter les exemples de code de ce cours.

## Rejoindre les autres apprenants et obtenir de l’aide

Avant de commencer à cloner votre dépôt, rejoignez le [canal Discord AI Agents For Beginners](https://aka.ms/ai-agents/discord) pour obtenir de l’aide lors de la configuration, poser des questions sur le cours, ou pour vous connecter avec d’autres apprenants.

## Cloner ou forker ce dépôt

Pour commencer, veuillez cloner ou forker le dépôt GitHub. Cela vous permettra d’avoir votre propre version du matériel du cours afin que vous puissiez exécuter, tester et modifier le code !

Cela peut se faire en cliquant sur le lien pour <a href="https://github.com/microsoft/ai-agents-for-beginners/fork" target="_blank">forker le dépôt</a>

Vous devriez maintenant avoir votre propre version forkée de ce cours via le lien suivant :

![Dépôt forké](../../../translated_images/fr/forked-repo.33f27ca1901baa6a.webp)

### Clone superficiel (recommandé pour atelier / Codespaces)

  >Le dépôt complet peut être volumineux (~3 Go) si vous téléchargez tout l’historique et tous les fichiers. Si vous assistez seulement à l’atelier ou avez besoin de quelques dossiers de leçons, un clone superficiel (ou un clone sparse) télécharge beaucoup moins.

#### Clone superficiel rapide — historique minimal, tous fichiers

Remplacez `<your-username>` dans les commandes ci-dessous par l’URL de votre fork (ou l’URL upstream si vous préférez).

Pour cloner uniquement l’historique du dernier commit (téléchargement léger) :

```bash
git clone --depth 1 https://github.com/<your-username>/ai-agents-for-beginners.git
```

Pour cloner une branche spécifique :

```bash
git clone --depth 1 --branch <branch-name> https://github.com/<your-username>/ai-agents-for-beginners.git
```

#### Clone partiel (sparse) — blobs minimaux + seulement certains dossiers

Cela utilise le clone partiel et le sparse-checkout (nécessite Git 2.25+ et il est recommandé d’utiliser une version moderne de Git avec support du clone partiel) :

```bash
git clone --depth 1 --filter=blob:none --sparse https://github.com/<your-username>/ai-agents-for-beginners.git
```

Accédez au dossier du dépôt :

```bash
cd ai-agents-for-beginners
```

Ensuite, précisez quels dossiers vous souhaitez (l’exemple ci-dessous montre deux dossiers) :

```bash
git sparse-checkout set 00-course-setup 01-intro-to-ai-agents
```

Après le clonage et la vérification des fichiers, si vous n’avez que besoin des fichiers et souhaitez libérer de l’espace (aucun historique git), veuillez supprimer les métadonnées du dépôt (💀 irréversible — vous perdrez toute la fonctionnalité Git) :

```bash
# zsh/bash
rm -rf .git
```

```powershell
# PowerShell
Remove-Item -Recurse -Force .git
```

#### Utilisation de GitHub Codespaces (recommandé pour éviter les gros téléchargements locaux)

- Créez un nouveau Codespace pour ce dépôt via l’[interface GitHub](https://github.com/codespaces).  

- Dans le terminal du Codespace nouvellement créé, exécutez une des commandes de clone superficiel/sparse ci-dessus pour importer uniquement les dossiers de leçon dont vous avez besoin dans l’espace de travail Codespace.
- Optionnel : après clonage dans Codespaces, supprimez .git pour récupérer de l’espace supplémentaire (voir les commandes de suppression ci-dessus).
- Remarque : si vous préférez ouvrir directement le dépôt dans Codespaces (sans clone supplémentaire), sachez que Codespaces construira l’environnement devcontainer et peut toujours provisionner plus que ce dont vous avez besoin.

#### Conseils

- Remplacez toujours l’URL du clone par celle de votre fork si vous souhaitez modifier/commiter.
- Si vous avez besoin plus tard d’historique ou fichiers, vous pouvez les récupérer ou ajuster le sparse-checkout pour inclure des dossiers supplémentaires.

## Exécuter le code

Ce cours propose une série de notebooks Jupyter que vous pouvez exécuter pour acquérir une expérience pratique de création d’Agents IA.

Les exemples de code utilisent **Microsoft Agent Framework (MAF)** avec le `FoundryChatClient`, qui se connecte au **Microsoft Foundry Agent Service V2** (l’API Responses) via **Microsoft Foundry**.

Tous les notebooks Python sont nommés `*-python-agent-framework.ipynb`.

## Prérequis

- Python 3.12+
  - **NOTE** : Si vous n’avez pas Python3.12 installé, assurez-vous de l’installer. Créez ensuite votre environnement virtuel avec python3.12 pour garantir que les versions correctes sont installées depuis requirements.txt.
  
    >Exemple

    Créez le dossier de l’environnement virtuel Python :

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

- .NET 10+ : Pour les exemples utilisant .NET, assurez-vous d’installer le [.NET 10 SDK](https://dotnet.microsoft.com/download/dotnet/10.0) ou plus récent. Puis vérifiez la version du SDK .NET installée :

    ```bash
    dotnet --list-sdks
    ```

- **Azure CLI** — Nécessaire pour l’authentification. Installez à partir de [aka.ms/installazurecli](https://aka.ms/installazurecli).
- **Abonnement Azure** — Pour accéder à Microsoft Foundry et Microsoft Foundry Agent Service.
- **Projet Microsoft Foundry** — Un projet avec un modèle déployé (par exemple, `gpt-5-mini`). Voir [Étape 1](#étape-1-créer-un-projet-microsoft-foundry) ci-dessous.

Un fichier `requirements.txt` est inclus à la racine de ce dépôt contenant tous les paquets Python requis pour exécuter les exemples de code.

Vous pouvez les installer en exécutant la commande suivante dans votre terminal à la racine du dépôt :

```bash
pip install -r requirements.txt
```

Nous recommandons de créer un environnement virtuel Python pour éviter tout conflit ou problème.

## Configuration de VSCode

Assurez-vous que vous utilisez la bonne version de Python dans VSCode.

![image](https://github.com/user-attachments/assets/a85e776c-2edb-4331-ae5b-6bfdfb98ee0e)

## Configurer Microsoft Foundry et Microsoft Foundry Agent Service

### Étape 1 : Créer un projet Microsoft Foundry

Vous avez besoin d’un **hub** Microsoft Foundry et d’un **projet** avec un modèle déployé pour exécuter les notebooks.

1. Rendez-vous sur [ai.azure.com](https://ai.azure.com) et connectez-vous avec votre compte Azure.
2. Créez un **hub** (ou utilisez un existant). Voir : [Aperçu des ressources Hub](https://learn.microsoft.com/azure/ai-foundry/concepts/ai-resources).
3. Dans le hub, créez un **projet**.
4. Déployez un modèle (par exemple, `gpt-5-mini`) via **Models + Endpoints** → **Déployer modèle**.

### Étape 2 : Récupérez l’endpoint de votre projet et le nom du déploiement du modèle

Depuis votre projet dans le portail Microsoft Foundry :

- **Endpoint du projet** — Allez sur la page **Overview** et copiez l’URL de l’endpoint.

![Chaîne de connexion du projet](../../../translated_images/fr/project-endpoint.8cf04c9975bbfbf1.webp)

- **Nom du déploiement du modèle** — Allez dans **Models + Endpoints**, sélectionnez votre modèle déployé, et notez le **Nom du déploiement** (ex. `gpt-5-mini`).

### Étape 3 : Connectez-vous à Azure avec `az login`

La plupart des notebooks s’authentifient via votre **connexion Azure CLI** — utilisant `AzureCliCredential` ou `DefaultAzureCredential` (qui récupèrent votre session `az login`) depuis le package `azure-identity` — ils ne nécessitent donc pas de clés API. Quelques leçons et intégrations optionnelles utilisent des clés API ; vérifiez les prérequis de chaque leçon pour d’éventuelles variables d’environnement additionnelles. Cela nécessite d’être connecté via Azure CLI.

1. **Installez Azure CLI** si ce n’est pas déjà fait : [aka.ms/installazurecli](https://aka.ms/installazurecli)

2. **Connectez-vous** en exécutant :

    ```bash
    az login
    ```

    Ou si vous êtes dans un environnement distant/Codespace sans navigateur :

    ```bash
    az login --use-device-code
    ```

3. **Sélectionnez votre abonnement** si cela est demandé — choisissez celui contenant votre projet Foundry.

4. **Vérifiez** que vous êtes connecté :

    ```bash
    az account show
    ```

> **Pourquoi `az login` ?** Les notebooks s’authentifient avec `AzureCliCredential` (ou `DefaultAzureCredential`, qui récupère également votre connexion Azure CLI) du package `azure-identity`. Cela signifie que votre session Azure CLI fournit les identifiants — pas de clés API ou secrets dans votre fichier `.env`. C’est une [bonne pratique de sécurité](https://learn.microsoft.com/azure/developer/ai/keyless-connections).

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

| Variable | Où la trouver |
|----------|-----------------|
| `AZURE_AI_PROJECT_ENDPOINT` | Portail Foundry → votre projet → page **Overview** |
| `AZURE_AI_MODEL_DEPLOYMENT_NAME` | Portail Foundry → **Models + Endpoints** → nom de votre modèle déployé |

C’est tout pour la plupart des leçons ! Les notebooks s’authentifieront automatiquement via votre session `az login`.

### Étape 5 : Installez les dépendances Python

```bash
pip install -r requirements.txt
```

Nous recommandons d’exécuter cela dans l’environnement virtuel que vous avez créé précédemment.

## Configuration optionnelle : Azure AI Search (Leçons 5 et 16)

Les notebooks des Leçons 5 (Agentic RAG) et 16 fonctionnent immédiatement avec une **base de connaissances en mémoire** — aucune ressource Azure supplémentaire requise. Si vous souhaitez les supporter avec un vrai index **Azure AI Search**, notez que le **notebook de la Leçon 16 utilise actuellement une authentification par clé** : il passe de la recherche en mémoire à Azure AI Search uniquement lorsque **les deux** variables `AZURE_SEARCH_SERVICE_ENDPOINT` **et** `AZURE_SEARCH_API_KEY` sont définies ; sinon il continue avec la recherche en mémoire — donc pour l’exécuter avec un vrai index, vous devez aussi définir la clé admin. L’authentification sans clé avec Microsoft Entra ID (RBAC) est la méthode recommandée pour votre propre code en production, conforme au flux `az login` utilisé partout ailleurs dans ce cours.

Les étapes RBAC ci-dessous s’appliquent aux exemples du guide de configuration et à votre propre code. Elles ne permettent pas l’authentification sans clé dans le notebook de la Leçon 16 ; celle-ci nécessite encore l’endpoint et la clé admin pour utiliser Azure AI Search.

1. **Activez l’accès basé sur les rôles** sur votre service de recherche :

    ```bash
    az search service update --name <service-name> --resource-group <resource-group> --auth-options aadOrApiKey
    ```

2. **Attribuez-vous les rôles nécessaires** (création/chargement d’index et requêtes) :

    ```bash
    az role assignment create --assignee <your-user-or-principal-id> --role "Search Service Contributor" --scope $(az search service show -g <resource-group> -n <service-name> --query id -o tsv)
    az role assignment create --assignee <your-user-or-principal-id> --role "Search Index Data Contributor" --scope $(az search service show -g <resource-group> -n <service-name> --query id -o tsv)
    ```

3. **Ajoutez l’endpoint** à votre fichier `.env` :

| Variable | Où la trouver |
|----------|-----------------|
| `AZURE_SEARCH_SERVICE_ENDPOINT` | Portail Azure → votre ressource **Azure AI Search** → **Overview** → URL |
| `AZURE_SEARCH_API_KEY` | Obligatoire (avec l’endpoint) pour activer Azure AI Search dans le notebook de la Leçon 16, qui utilise une authentification par clé. Portail Azure → **Paramètres** → **Clés** → clé admin primaire |

> **Pourquoi sans clé ?** Les clés administrateur donnent un accès complet en écriture à votre service de recherche et peuvent fuir via les fichiers `.env`. Avec RBAC, c’est votre identité `az login` qui est utilisée à la place — le même modèle sans clé Entra ID que les notebooks du cours utilisent (via `AzureCliCredential` / `DefaultAzureCredential`). Voir [Connexion à Azure AI Search via les rôles](https://learn.microsoft.com/azure/search/search-security-rbac).

Voir le [guide de configuration Azure AI Search](./AzureSearch.md) pour des exemples complets de création d’index en Python et .NET.

## Configuration supplémentaire pour les leçons qui appellent directement Azure OpenAI (Leçons 6 et 8)

Certains notebooks des leçons 6 et 8 appellent **Azure OpenAI** directement (via l’**API Responses**) au lieu de passer par un projet Microsoft Foundry. Ces exemples utilisaient auparavant des modèles GitHub, qui sont obsolètes et ne supportent pas l’API Responses. Ajoutez ces variables dans votre fichier `.env` :

| Variable | Où la trouver |
|----------|-----------------|
| `AZURE_OPENAI_ENDPOINT` | Portail Azure → votre ressource **Azure OpenAI** → **Clés et endpoint** → Endpoint (ex. `https://<votre-ressource>.openai.azure.com`) |
| `AZURE_OPENAI_DEPLOYMENT` | Nom de votre modèle déployé (ex. `gpt-5-mini`) qui supporte l’API Responses |
| `AZURE_OPENAI_API_KEY` | Optionnel — uniquement si vous utilisez une authentification par clé au lieu de `az login` / Entra ID |

> L’API Responses utilise l’endpoint stable `/openai/v1/`, donc aucune `api-version` n’est requise. Connectez-vous avec `az login` pour utiliser l’authentification sans clé Entra ID.

## Fournisseur alternatif : MiniMax (compatible OpenAI)

[MiniMax](https://platform.minimaxi.com/) propose des modèles à contexte large (jusqu’à 204K tokens) via une API compatible OpenAI. Comme le `OpenAIChatClient` du Microsoft Agent Framework fonctionne avec tout endpoint compatible OpenAI, vous pouvez utiliser MiniMax comme alternative de remplacement pour les leçons utilisant `OpenAIChatClient`.

Ajoutez ces variables dans votre fichier `.env` :

| Variable | Où la trouver |
|----------|-----------------|
| `MINIMAX_API_KEY` | [MiniMax Platform](https://platform.minimaxi.com/) → Clés API |
| `MINIMAX_BASE_URL` | Utilisez `https://api.minimax.io/v1` (valeur par défaut) |
| `MINIMAX_MODEL_ID` | Nom du modèle à utiliser (ex. `MiniMax-M3`) |

**Exemples de modèles** : `MiniMax-M3` (recommandé), `MiniMax-M2.7`, `MiniMax-M2.7-highspeed` (réponses plus rapides). Les noms et disponibilités des modèles peuvent changer avec le temps, et l’accès à un modèle donné peut dépendre de votre compte.

Les exemples de code utilisant `OpenAIChatClient` (ex. workflow de réservation hôtel de la leçon 14) détecteront automatiquement et utiliseront votre configuration MiniMax lorsque `MINIMAX_API_KEY` est défini.


## Fournisseur alternatif : Novita AI (compatible OpenAI)

[Novita AI](https://novita.ai/llm-api) fournit une API compatible OpenAI pour les LLM open-source et de pointe (DeepSeek, Llama, Qwen, et plus). Puisque `OpenAIChatClient` du Microsoft Agent Framework fonctionne avec n'importe quel point de terminaison compatible OpenAI, vous pouvez utiliser Novita AI comme une alternative prête à l'emploi à Azure OpenAI ou OpenAI.

Ajoutez ces variables à votre fichier `.env` :

| Variable | Où la trouver |
|----------|-----------------|
| `NOVITA_API_KEY` | [Tableau de bord Novita AI](https://novita.ai/settings/key-management) → Clés API |
| `NOVITA_BASE_URL` | Utilisez `https://api.novita.ai/openai/v1` (valeur par défaut) |
| `NOVITA_MODEL_ID` | Nom du modèle à utiliser (ex. : `moonshotai/kimi-k3`) |

**Exemples de modèles** : `moonshotai/kimi-k3`, `zai-org/glm-5.2`, `deepseek/deepseek-v4-flash-0731`. Novita AI héberge également de nombreuses autres familles de modèles open-source (Llama, Qwen, GLM, et plus) — consultez la [bibliothèque de modèles Novita AI](https://novita.ai/llm-api) pour la liste actuelle des modèles disponibles et leurs identifiants.

Les exemples actuels ne consomment pas automatiquement les variables `NOVITA_*`. Pour utiliser Novita AI, transmettez explicitement ces valeurs lors de la construction de `OpenAIChatClient` dans l'exemple que vous exécutez.

## Fournisseur alternatif : Foundry Local (Exécutez des modèles sur votre appareil)

[Foundry Local](https://foundrylocal.ai) est un runtime léger qui télécharge, gère et sert les modèles de langue **entièrement sur votre propre machine** via une API compatible OpenAI — sans besoin de cloud.

Comme le `OpenAIChatClient` du Microsoft Agent Framework fonctionne avec tout endpoint compatible OpenAI, Foundry Local est une alternative locale prête à l'emploi à Azure OpenAI.

**1. Installez Foundry Local**

```bash
# Windows
winget install Microsoft.FoundryLocal

# macOS
brew install foundrylocal
```

**2. Téléchargez et lancez un modèle** (cela démarre aussi le service local) :

```bash
foundry model list          # voir les modèles disponibles
foundry model run phi-4-mini
```

**3. Installez le SDK Python** utilisé pour découvrir le point de terminaison local :

```bash
pip install foundry-local-sdk
```

**4. Configurez le Microsoft Agent Framework sur votre modèle local :**

```python
from foundry_local import FoundryLocalManager
from agent_framework.openai import OpenAIChatClient

# Télécharge (si nécessaire) et sert le modèle localement, puis découvre le point de terminaison/port.
manager = FoundryLocalManager("phi-4-mini")

chat_client = OpenAIChatClient(
    base_url=manager.endpoint,      # par exemple http://localhost:<port>/v1
    api_key=manager.api_key,        # toujours "non requis" pour Foundry Local
    model_id=manager.get_model_info("phi-4-mini").id,
)

agent = chat_client.as_agent(
    name="LocalAgent",
    instructions="You are a helpful assistant running fully on-device.",
)
```

> **Remarque :** Foundry Local expose un point de terminaison **Chat Completions** compatible OpenAI. Utilisez-le pour le développement local et les scénarios hors ligne. Pour l'ensemble des fonctionnalités de l’**API Réponses** (conversations avec état, etc.), utilisez Azure OpenAI ou un projet Microsoft Foundry.

## Configuration supplémentaire pour la Leçon 8 (Workflow de Grounding Bing)

Le notebook du workflow conditionnel dans la leçon 8 utilise le **grounding Bing** via Microsoft Foundry. Si vous prévoyez d’exécuter cet exemple, ajoutez cette variable à votre fichier `.env` :

| Variable | Où la trouver |
|----------|-----------------|
| `BING_CONNECTION_ID` | Portail Microsoft Foundry → votre projet → **Gestion** → **Ressources connectées** → votre connexion Bing → copiez l’ID de connexion |

## Dépannage

### Erreurs de vérification de certificat SSL sur macOS

Si vous êtes sur macOS et rencontrez une erreur telle que :

```plaintext
ssl.SSLCertVerificationError: [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: self-signed certificate in certificate chain
```

Il s'agit d'un problème connu avec Python sur macOS où les certificats SSL du système ne sont pas automatiquement reconnus comme fiables. Essayez les solutions suivantes dans l’ordre :

**Option 1 : Exécutez le script Install Certificates de Python (recommandé)**

```bash
# Remplacez 3.XX par votre version Python installée (par exemple, 3.12 ou 3.13) :
/Applications/Python\ 3.XX/Install\ Certificates.command
```

**Option 2 : Utilisez `connection_verify=False` dans votre notebook (uniquement pour les notebooks GitHub Models)**

Dans le notebook de la Leçon 6 (`06-building-trustworthy-agents/code_samples/06-system-message-framework.ipynb`), une solution de contournement commentée est déjà incluse. Décommentez `connection_verify=False` si vous rencontrez des erreurs de certificat :

```python
client = ChatCompletionsClient(
    endpoint=endpoint,
    credential=AzureKeyCredential(token),
    connection_verify=False,  # Désactiver la vérification SSL si vous rencontrez des erreurs de certificat
)
```

> **⚠️ Attention :** Désactiver la vérification SSL (`connection_verify=False`) réduit la sécurité en sautant la validation du certificat. N’utilisez ceci que temporairement en environnement de développement. Ne jamais l’utiliser en production.

**Option 3 : Installez et utilisez `truststore`**

```bash
pip install truststore
```

Ensuite, ajoutez ce qui suit en haut de votre notebook ou script avant tout appel réseau :

```python
import truststore
truststore.inject_into_ssl()
```

## Bloqué quelque part ?

Si vous rencontrez des problèmes avec cette configuration, rejoignez notre <a href="https://discord.gg/kzRShWzttr" target="_blank">Azure AI Community Discord</a> ou <a href="https://github.com/microsoft/ai-agents-for-beginners/issues?WT.mc_id=academic-105485-koreyst" target="_blank">créez une issue</a>.

## Leçon suivante

Vous êtes maintenant prêt à exécuter le code de ce cours. Bon apprentissage dans l’univers des agents IA !

[Introduction aux agents IA et cas d'utilisation d'agents](../01-intro-to-ai-agents/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Avertissement** :
Ce document a été traduit à l'aide du service de traduction automatique [Co-op Translator](https://github.com/Azure/co-op-translator). Bien que nous nous efforçions d'assurer l'exactitude, veuillez noter que les traductions automatisées peuvent contenir des erreurs ou des inexactitudes. Le document original dans sa langue native doit être considéré comme la source faisant autorité. Pour les informations critiques, il est recommandé de recourir à une traduction professionnelle réalisée par un humain. Nous ne saurions être tenus responsables des malentendus ou erreurs d'interprétation découlant de l'utilisation de cette traduction.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->