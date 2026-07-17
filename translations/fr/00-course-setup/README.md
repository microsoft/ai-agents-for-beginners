# Configuration du cours

## Introduction

Cette leçon expliquera comment exécuter les exemples de code de ce cours.

## Rejoignez les autres apprenants et obtenez de l'aide

Avant de commencer à cloner votre dépôt, rejoignez le [canal Discord AI Agents For Beginners](https://aka.ms/ai-agents/discord) pour obtenir de l’aide pour la configuration, poser des questions sur le cours, ou pour connecter avec d’autres apprenants.

## Cloner ou forker ce dépôt

Pour commencer, veuillez cloner ou forker le dépôt GitHub. Cela vous permettra de disposer de votre propre version du matériel du cours pour pouvoir exécuter, tester et ajuster le code !

Cela peut se faire en cliquant sur le lien pour <a href="https://github.com/microsoft/ai-agents-for-beginners/fork" target="_blank">forker le dépôt</a>

Vous devriez maintenant disposer de votre propre version forkée de ce cours à ce lien :

![Dépôt forké](../../../translated_images/fr/forked-repo.33f27ca1901baa6a.webp)

### Clone partiel (recommandé pour les ateliers / Codespaces)

  >Le dépôt complet peut être volumineux (~3 Go) si vous téléchargez tout l’historique et tous les fichiers. Si vous participez seulement à l’atelier ou si vous avez besoin uniquement de quelques dossiers de leçon, un clone partiel (ou sparse clone) évite la majorité du téléchargement en tronquant l’historique et/ou en sautant certains blobs.

#### Clone partiel rapide - historique minimal, tous les fichiers

Remplacez `<your-username>` dans les commandes ci-dessous par l’URL de votre fork (ou l’URL du dépôt en amont si vous préférez).

Pour cloner uniquement l’historique du dernier commit (téléchargement réduit) :

```bash|powershell
git clone --depth 1 https://github.com/<your-username>/ai-agents-for-beginners.git
```

Pour cloner une branche spécifique :

```bash|powershell
git clone --depth 1 --branch <branch-name> https://github.com/<your-username>/ai-agents-for-beginners.git
```

#### Clone partiel (sparse) — blobs minimaux + seulement les dossiers sélectionnés

Cela utilise le clone partiel et sparse-checkout (requiert Git 2.25+ et de préférence une version moderne de Git avec prise en charge du clone partiel) :

```bash|powershell
git clone --depth 1 --filter=blob:none --sparse https://github.com/<your-username>/ai-agents-for-beginners.git
```

Accédez au dossier du dépôt :

```bash|powershell
cd ai-agents-for-beginners
```

Puis spécifiez les dossiers souhaités (exemple ci-dessous montre deux dossiers) :

```bash|powershell
git sparse-checkout set 00-course-setup 01-intro-to-ai-agents
```

Après le clonage et la vérification des fichiers, si vous avez uniquement besoin des fichiers et souhaitez libérer de l’espace (sans historique git), veuillez supprimer les métadonnées du dépôt (💀 irréversible — vous perdrez toute fonctionnalité Git : pas de commits, pulls, pushes, ni accès à l’historique).

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

- Dans le terminal du Codespace nouvellement créé, exécutez l’une des commandes de clone partiel/sparse ci-dessus pour ne récupérer que les dossiers de leçon nécessaires dans l’espace de travail Codespace.
- Optionnel : après le clonage dans Codespaces, supprimez le dossier .git pour récupérer de l’espace supplémentaire (voir commandes de suppression ci-dessus).
- Note : Si vous préférez ouvrir le dépôt directement dans Codespaces (sans clonage supplémentaire), sachez que Codespaces construit l’environnement devcontainer et peut toujours provisionner plus que nécessaire. Cloner une copie partielle dans un Codespace neuf vous donne plus de contrôle sur l’usage du disque.

#### Conseils

- Remplacez toujours l’URL du clone par celle de votre fork si vous souhaitez modifier/committer.
- Si vous avez besoin ultérieurement de plus d’historique ou de fichiers, vous pouvez les récupérer ou ajuster sparse-checkout pour inclure des dossiers supplémentaires.

## Exécution du code

Ce cours propose une série de notebooks Jupyter que vous pouvez exécuter pour pratiquer la création d’agents IA.

Les exemples de code utilisent **Microsoft Agent Framework (MAF)** avec `FoundryChatClient`, qui se connecte au **Microsoft Foundry Agent Service V2** (l’API Responses) via **Microsoft Foundry**.

Tous les notebooks Python s’appellent `*-python-agent-framework.ipynb`.

## Prérequis

- Python 3.12+
  - **NOTE** : Si vous n’avez pas Python3.12 installé, assurez-vous de l’installer. Puis créez votre environnement virtuel avec python3.12 afin d’installer les bonnes versions listées dans requirements.txt.
  
    >Exemple

    Créez le dossier d’environnement virtuel Python :

    ```bash|powershell
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

- .NET 10+ : Pour les exemples en .NET, installez le [.NET 10 SDK](https://dotnet.microsoft.com/download/dotnet/10.0) ou une version ultérieure. Ensuite, vérifiez votre version du SDK .NET installé :

    ```bash|powershell
    dotnet --list-sdks
    ```

- **Azure CLI** — Nécessaire pour l’authentification. Installez-le depuis [aka.ms/installazurecli](https://aka.ms/installazurecli).
- **Abonnement Azure** — Pour accéder à Microsoft Foundry et Microsoft Foundry Agent Service.
- **Projet Microsoft Foundry** — Un projet avec un modèle déployé (ex. `gpt-4.1-mini`). Voir [Étape 1](#étape-1-créer-un-projet-microsoft-foundry) ci-dessous.

Un fichier `requirements.txt` est inclus à la racine de ce dépôt et contient tous les paquets Python nécessaires pour exécuter les exemples de code.

Vous pouvez les installer en exécutant la commande suivante dans votre terminal à la racine du dépôt :

```bash|powershell
pip install -r requirements.txt
```

Nous recommandons de créer un environnement virtuel Python pour éviter les conflits et problèmes.

## Configuration de VSCode

Assurez-vous d’utiliser la bonne version de Python dans VSCode.

![image](https://github.com/user-attachments/assets/a85e776c-2edb-4331-ae5b-6bfdfb98ee0e)

## Configuration de Microsoft Foundry et Microsoft Foundry Agent Service

### Étape 1 : Créer un projet Microsoft Foundry

Vous avez besoin d’un **hub** et d’un **projet** Microsoft Foundry avec un modèle déployé pour exécuter les notebooks.

1. Rendez-vous sur [ai.azure.com](https://ai.azure.com) et connectez-vous avec votre compte Azure.
2. Créez un **hub** (ou utilisez un existant). Voir : [Aperçu des ressources Hub](https://learn.microsoft.com/azure/ai-foundry/concepts/ai-resources).
3. Dans le hub, créez un **projet**.
4. Déployez un modèle (ex. `gpt-4.1-mini`) depuis **Models + Endpoints** → **Deploy model**.

### Étape 2 : Récupérer l’URL du point de terminaison du projet et le nom du déploiement du modèle

Depuis votre projet dans le portail Microsoft Foundry :

- **Point de terminaison du projet** — Allez sur la page **Overview** et copiez l’URL du point de terminaison.

![Chaîne de connexion du projet](../../../translated_images/fr/project-endpoint.8cf04c9975bbfbf1.webp)

- **Nom du déploiement du modèle** — Allez sur **Models + Endpoints**, sélectionnez votre modèle déployé, et notez le **Deployment name** (ex. `gpt-4.1-mini`).

### Étape 3 : Connectez-vous à Azure avec `az login`

Tous les notebooks utilisent **`AzureCliCredential`** pour l’authentification — pas de clés API à gérer. Cela nécessite que vous soyez connecté via la CLI Azure.

1. **Installez l’Azure CLI** si ce n’est pas déjà fait : [aka.ms/installazurecli](https://aka.ms/installazurecli)

2. **Connectez-vous** en lançant :

    ```bash|powershell
    az login
    ```

    Ou si vous êtes dans un environnement distant/Codespace sans navigateur :

    ```bash|powershell
    az login --use-device-code
    ```

3. **Sélectionnez votre abonnement** si demandé — choisissez celui contenant votre projet Foundry.

4. **Vérifiez** que vous êtes bien connecté :

    ```bash|powershell
    az account show
    ```

> **Pourquoi `az login` ?** Les notebooks s’authentifient avec `AzureCliCredential` du package `azure-identity`. Cela signifie que votre session Azure CLI fournit les identifiants — pas de clés API ou secrets dans votre fichier `.env`. C’est une [bonne pratique de sécurité](https://learn.microsoft.com/azure/developer/ai/keyless-connections).

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
AZURE_AI_MODEL_DEPLOYMENT_NAME=gpt-4.1-mini
```

| Variable | Où la trouver |
|----------|-----------------|
| `AZURE_AI_PROJECT_ENDPOINT` | Portail Foundry → votre projet → page **Overview** |
| `AZURE_AI_MODEL_DEPLOYMENT_NAME` | Portail Foundry → **Models + Endpoints** → nom du modèle déployé |

C’est tout pour la plupart des leçons ! Les notebooks s’authentifieront automatiquement via votre session `az login`.

### Étape 5 : Installez les dépendances Python

```bash|powershell
pip install -r requirements.txt
```

Nous recommandons d’exécuter cela dans l’environnement virtuel que vous avez créé plus tôt.

## Configuration supplémentaire pour la leçon 5 (Agentic RAG)

La leçon 5 utilise **Azure AI Search** pour la génération augmentée par récupération. Si vous prévoyez d’exécuter cette leçon, ajoutez ces variables dans votre fichier `.env` :

| Variable | Où la trouver |
|----------|-----------------|
| `AZURE_SEARCH_SERVICE_ENDPOINT` | Portail Azure → votre ressource **Azure AI Search** → **Overview** → URL |
| `AZURE_SEARCH_API_KEY` | Portail Azure → votre ressource **Azure AI Search** → **Settings** → **Keys** → clé admin principale |

## Configuration supplémentaire pour les leçons qui appellent directement Azure OpenAI (Leçons 6 et 8)

Certains notebooks des leçons 6 et 8 appellent directement **Azure OpenAI** (en utilisant l’**API Responses**) au lieu de passer par un projet Microsoft Foundry. Ces échantillons utilisaient auparavant les GitHub Models, désormais dépréciés (retrait prévu en juillet 2026) et ne supportant pas l’API Responses. Si vous comptez exécuter ces échantillons, ajoutez ces variables dans votre fichier `.env` :

| Variable | Où la trouver |
|----------|-----------------|
| `AZURE_OPENAI_ENDPOINT` | Portail Azure → votre ressource **Azure OpenAI** → **Keys and Endpoint** → Endpoint (ex. `https://<votre-ressource>.openai.azure.com`) |
| `AZURE_OPENAI_DEPLOYMENT` | Nom du modèle déployé (ex. `gpt-4.1-mini`) supportant l’API Responses |
| `AZURE_OPENAI_API_KEY` | Optionnel — uniquement si vous utilisez une authentification par clé au lieu de `az login` / Entra ID |

> L’API Responses utilise le point de terminaison stable `/openai/v1/`, donc aucun `api-version` n’est requis. Connectez-vous avec `az login` pour utiliser l’authentification Entra ID sans clé.

## Fournisseur alternatif : MiniMax (compatible OpenAI)

[MiniMax](https://platform.minimaxi.com/) fournit des modèles à contexte large (jusqu’à 204K tokens) via une API compatible OpenAI. Comme le `OpenAIChatClient` du Microsoft Agent Framework fonctionne avec n’importe quel point de terminaison compatible OpenAI, vous pouvez utiliser MiniMax comme alternative directe à Azure OpenAI ou OpenAI.

Ajoutez ces variables dans votre fichier `.env` :

| Variable | Où la trouver |
|----------|-----------------|
| `MINIMAX_API_KEY` | [MiniMax Platform](https://platform.minimaxi.com/) → Clés API |
| `MINIMAX_BASE_URL` | Utilisez `https://api.minimax.io/v1` (valeur par défaut) |
| `MINIMAX_MODEL_ID` | Nom du modèle à utiliser (ex. `MiniMax-M3`) |

**Exemples de modèles** : `MiniMax-M3` (recommandé), `MiniMax-M2.7`, `MiniMax-M2.7-highspeed` (réponses plus rapides). Les noms et la disponibilité des modèles peuvent évoluer, et l’accès dépend de votre compte ou région — consultez la [MiniMax Platform](https://platform.minimaxi.com/) pour la liste actuelle. Si `MiniMax-M3` n’est pas disponible pour votre compte, définissez `MINIMAX_MODEL_ID` sur un modèle accessible (ex. `MiniMax-M2.7`).

Les exemples utilisant `OpenAIChatClient` (ex. le workflow de réservation d’hôtel de la Leçon 14) détecteront et utiliseront automatiquement votre configuration MiniMax lorsque `MINIMAX_API_KEY` est défini.

## Fournisseur alternatif : Foundry Local (exécute les modèles localement)

[Foundry Local](https://foundrylocal.ai) est un runtime léger qui télécharge, gère et sert des modèles de langage **entièrement sur votre machine** via une API compatible OpenAI — pas de cloud, pas d’abonnement Azure, pas de clés API. C’est une excellente option pour le développement hors ligne, expérimenter sans coûts cloud, ou garder les données localement.

Comme le `OpenAIChatClient` du Microsoft Agent Framework fonctionne avec n’importe quel point de terminaison OpenAI-compatible, Foundry Local est une alternative locale prête à l’emploi à Azure OpenAI.

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

**4. Configurez Microsoft Agent Framework pour pointer vers votre modèle local :**

```python
from foundry_local import FoundryLocalManager
from agent_framework.openai import OpenAIChatClient

# Télécharge (si nécessaire) et sert le modèle localement, puis découvre le point de terminaison/le port.
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

> **Note :** Foundry Local expose un point de terminaison compatible OpenAI **Chat Completions**. Utilisez-le pour le développement local et hors ligne. Pour bénéficier de toutes les fonctionnalités de l’**API Responses** (conversations avec état, orchestration avancée d’outils, développement de style agent), visez **Azure OpenAI** ou un projet **Microsoft Foundry** comme montré dans les leçons. Consultez la [documentation Foundry Local](https://foundrylocal.ai) pour le catalogue actuel des modèles et la compatibilité des plateformes.


## Configuration supplémentaire pour la leçon 8 (Flux de travail Bing Grounding)

Le notebook du flux de travail conditionnel dans la leçon 8 utilise **Bing grounding** via Microsoft Foundry. Si vous prévoyez d’exécuter cet exemple, ajoutez cette variable à votre fichier `.env` :

| Variable | Où la trouver |
|----------|-----------------|
| `BING_CONNECTION_ID` | Portail Microsoft Foundry → votre projet → **Gestion** → **Ressources connectées** → votre connexion Bing → copiez l’ID de connexion |

## Dépannage

### Erreurs de vérification du certificat SSL sur macOS

Si vous êtes sur macOS et rencontrez une erreur telle que :

```plaintext
ssl.SSLCertVerificationError: [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: self-signed certificate in certificate chain
```

Il s’agit d’un problème connu avec Python sur macOS où les certificats SSL système ne sont pas automatiquement approuvés. Essayez les solutions suivantes dans l’ordre :

**Option 1 : Exécutez le script d’installation des certificats de Python (recommandé)**

```bash
# Remplacez 3.XX par la version de Python installée (par exemple, 3.12 ou 3.13) :
/Applications/Python\ 3.XX/Install\ Certificates.command
```

**Option 2 : Utilisez `connection_verify=False` dans votre notebook (uniquement pour les notebooks GitHub Models)**

Dans le notebook de la leçon 6 (`06-building-trustworthy-agents/code_samples/06-system-message-framework.ipynb`), une solution contournée commentée est déjà incluse. Décommentez `connection_verify=False` lors de la création du client :

```python
client = ChatCompletionsClient(
    endpoint=endpoint,
    credential=AzureKeyCredential(token),
    connection_verify=False,  # Désactivez la vérification SSL si vous rencontrez des erreurs de certificat
)
```

> **⚠️ Attention :** Désactiver la vérification SSL (`connection_verify=False`) réduit la sécurité en sautant la validation du certificat. Utilisez ceci uniquement comme solution temporaire en environnement de développement, jamais en production.

**Option 3 : Installez et utilisez `truststore`**

```bash
pip install truststore
```

Ajoutez ensuite ce qui suit en haut de votre notebook ou script avant d’effectuer toute requête réseau :

```python
import truststore
truststore.inject_into_ssl()
```

## Bloqué quelque part ?

Si vous avez des problèmes pour exécuter cette configuration, rejoignez notre <a href="https://discord.gg/kzRShWzttr" target="_blank">Discord de la communauté Azure AI</a> ou <a href="https://github.com/microsoft/ai-agents-for-beginners/issues?WT.mc_id=academic-105485-koreyst" target="_blank">créez un ticket</a>.

## Leçon suivante

Vous êtes maintenant prêt à exécuter le code de ce cours. Bon apprentissage du monde des Agents IA ! 

[Introduction aux Agents IA et cas d’utilisation des agents](../01-intro-to-ai-agents/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Avertissement** :
Ce document a été traduit à l'aide du service de traduction automatique [Co-op Translator](https://github.com/Azure/co-op-translator). Bien que nous nous efforçions d'assurer l'exactitude, veuillez noter que les traductions automatisées peuvent contenir des erreurs ou des inexactitudes. Le document original dans sa langue native doit être considéré comme la source faisant autorité. Pour les informations critiques, il est recommandé de recourir à une traduction professionnelle réalisée par un humain. Nous ne saurions être tenus responsables des malentendus ou erreurs d'interprétation découlant de l'utilisation de cette traduction.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->